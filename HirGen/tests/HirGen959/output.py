import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_572 = relay.var("var_572", dtype = "float32", shape = (10, 15, 1))#candidate|572|(10, 15, 1)|var|float32
uop_573 = relay.acosh(var_572.astype('float32')) # shape=(10, 15, 1)
output = uop_573
output2 = uop_573
func_579 = relay.Function([var_572,], output)
mod['func_579'] = func_579
mod = relay.transform.InferType()(mod)
mutated_mod['func_579'] = func_579
mutated_mod = relay.transform.InferType()(mutated_mod)
var_580 = relay.var("var_580", dtype = "float32", shape = (10, 15, 1))#candidate|580|(10, 15, 1)|var|float32
func_579_call = mutated_mod.get_global_var('func_579')
call_581 = func_579_call(var_580)
output = call_581
func_582 = relay.Function([var_580], output)
mutated_mod['func_582'] = func_582
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1636 = relay.var("var_1636", dtype = "uint8", shape = ())#candidate|1636|()|var|uint8
var_1637 = relay.var("var_1637", dtype = "uint8", shape = (6, 2, 6))#candidate|1637|(6, 2, 6)|var|uint8
bop_1638 = relay.bitwise_or(var_1636.astype('uint8'), var_1637.astype('uint8')) # shape=(6, 2, 6)
bop_1644 = relay.logical_or(var_1636.astype('bool'), var_1637.astype('bool')) # shape=(6, 2, 6)
func_579_call = mod.get_global_var('func_579')
func_582_call = mutated_mod.get_global_var('func_582')
var_1657 = relay.var("var_1657", dtype = "float32", shape = (150,))#candidate|1657|(150,)|var|float32
call_1656 = func_579_call(relay.reshape(var_1657.astype('float32'), [10, 15, 1]))
call_1658 = func_579_call(relay.reshape(var_1657.astype('float32'), [10, 15, 1]))
func_579_call = mod.get_global_var('func_579')
func_582_call = mutated_mod.get_global_var('func_582')
call_1665 = func_579_call(relay.reshape(var_1657.astype('float32'), [10, 15, 1]))
call_1666 = func_579_call(relay.reshape(var_1657.astype('float32'), [10, 15, 1]))
func_579_call = mod.get_global_var('func_579')
func_582_call = mutated_mod.get_global_var('func_582')
call_1675 = func_579_call(relay.reshape(var_1657.astype('float32'), [10, 15, 1]))
call_1676 = func_579_call(relay.reshape(var_1657.astype('float32'), [10, 15, 1]))
output = relay.Tuple([bop_1638,bop_1644,call_1656,var_1657,call_1665,call_1675,])
output2 = relay.Tuple([bop_1638,bop_1644,call_1658,var_1657,call_1666,call_1676,])
func_1678 = relay.Function([var_1636,var_1637,var_1657,], output)
mod['func_1678'] = func_1678
mod = relay.transform.InferType()(mod)
var_1679 = relay.var("var_1679", dtype = "uint8", shape = ())#candidate|1679|()|var|uint8
var_1680 = relay.var("var_1680", dtype = "uint8", shape = (6, 2, 6))#candidate|1680|(6, 2, 6)|var|uint8
var_1681 = relay.var("var_1681", dtype = "float32", shape = (150,))#candidate|1681|(150,)|var|float32
output = func_1678(var_1679,var_1680,var_1681,)
func_1682 = relay.Function([var_1679,var_1680,var_1681,], output)
mutated_mod['func_1682'] = func_1682
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2327 = relay.var("var_2327", dtype = "bool", shape = (8, 13, 2))#candidate|2327|(8, 13, 2)|var|bool
const_2328 = relay.const([[[True,False],[False,False],[False,True],[False,False],[True,False],[True,False],[False,False],[True,False],[True,True],[True,False],[False,False],[False,False],[True,True]],[[True,True],[False,False],[True,True],[False,True],[False,True],[False,False],[True,True],[False,False],[False,True],[True,True],[True,False],[False,False],[False,False]],[[False,False],[False,True],[True,False],[False,False],[False,True],[True,True],[False,True],[False,True],[True,True],[False,False],[True,False],[True,False],[True,False]],[[False,True],[False,True],[False,False],[True,False],[True,True],[False,True],[True,True],[False,False],[False,False],[False,False],[True,True],[True,False],[True,False]],[[False,False],[True,False],[False,True],[True,False],[False,True],[False,False],[False,True],[True,False],[False,False],[True,False],[False,True],[True,False],[True,False]],[[False,False],[False,True],[True,True],[False,False],[True,False],[True,False],[True,False],[False,True],[False,False],[True,True],[False,True],[True,False],[False,True]],[[True,True],[False,True],[True,False],[True,False],[True,False],[True,True],[False,False],[False,False],[False,True],[False,False],[False,False],[False,True],[True,True]],[[True,False],[True,True],[True,False],[False,True],[True,True],[True,True],[True,True],[True,False],[False,False],[False,False],[False,True],[True,False],[True,False]]], dtype = "bool")#candidate|2328|(8, 13, 2)|const|bool
bop_2329 = relay.logical_and(var_2327.astype('bool'), relay.reshape(const_2328.astype('bool'), relay.shape_of(var_2327))) # shape=(8, 13, 2)
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
const_2360 = relay.const(6, dtype = "uint8")#candidate|2360|()|const|uint8
var_2361 = relay.var("var_2361", dtype = "uint8", shape = (72,))#candidate|2361|(72,)|var|uint8
const_2362 = relay.const([[2.881502,1.120844],[-4.131297,3.054136],[4.581677,-0.657257],[5.485360,0.997613],[-6.298052,1.784441],[3.903438,-8.463584],[-3.398708,-4.128298],[-6.599500,7.602788],[4.999207,-1.596298],[-4.806135,-8.987341],[-7.706958,-9.412551],[0.109653,6.379157],[2.657447,5.550243],[-7.697456,2.545869],[-8.122998,1.194738],[4.417716,-3.784318],[9.009603,-3.651682],[8.441715,8.815868],[-8.991010,7.019954],[0.283695,4.033694],[1.645629,-0.637716],[-3.006152,-5.016378],[7.281317,7.911093],[-8.385608,4.297240],[6.601666,-1.467522],[-7.489780,-8.834383],[2.207818,-3.889705],[-9.647525,6.724479],[-5.677594,0.657157],[6.607718,0.553708],[-6.922045,6.838650],[9.508810,-2.502847],[-0.367194,7.190603],[5.184046,0.945902],[3.074685,3.554027],[-6.854999,9.501383],[-6.263667,9.767409],[-0.202287,-8.507038],[-0.241291,-6.794802],[-5.478466,-9.658978],[9.210516,9.693629],[1.232083,7.827346],[-0.866904,1.953968],[6.250473,-6.010554],[2.319320,5.987758],[-8.348179,-5.939784],[1.284385,-2.563373],[-1.964210,-0.489479],[-4.843609,-2.243684],[4.190129,-3.313989],[-2.483633,-6.256169],[-2.967451,-9.092967],[-4.852757,-3.948703],[0.792181,1.216168],[7.315260,5.601456],[-9.423779,7.685999],[0.517029,3.978698],[6.112531,5.848725],[7.595764,6.081289],[-9.186506,6.487236],[6.677333,9.328588],[9.042211,8.553177],[3.148503,-4.669903],[-2.954075,-4.169965],[3.920393,-6.836588],[-2.827149,-1.936130],[5.496063,3.131493],[4.893841,7.273751],[-6.469789,-2.891066],[1.235583,-5.581028],[-7.048971,7.769289],[-0.429546,-5.064297],[6.261400,-6.176614],[-6.174411,6.206451],[-7.695662,0.397316]], dtype = "float32")#candidate|2362|(75, 2)|const|float32
call_2359 = relay.TupleGetItem(func_1678_call(relay.reshape(const_2360.astype('uint8'), []), relay.reshape(var_2361.astype('uint8'), [6, 2, 6]), relay.reshape(const_2362.astype('float32'), [150,]), ), 1)
call_2363 = relay.TupleGetItem(func_1682_call(relay.reshape(const_2360.astype('uint8'), []), relay.reshape(var_2361.astype('uint8'), [6, 2, 6]), relay.reshape(const_2362.astype('float32'), [150,]), ), 1)
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
call_2365 = relay.TupleGetItem(func_1678_call(relay.reshape(const_2360.astype('uint8'), []), relay.reshape(var_2361.astype('uint8'), [6, 2, 6]), relay.reshape(const_2362.astype('float32'), [150,]), ), 1)
call_2366 = relay.TupleGetItem(func_1682_call(relay.reshape(const_2360.astype('uint8'), []), relay.reshape(var_2361.astype('uint8'), [6, 2, 6]), relay.reshape(const_2362.astype('float32'), [150,]), ), 1)
uop_2370 = relay.tan(const_2328.astype('float32')) # shape=(8, 13, 2)
output = relay.Tuple([bop_2329,call_2359,const_2360,var_2361,const_2362,call_2365,uop_2370,])
output2 = relay.Tuple([bop_2329,call_2363,const_2360,var_2361,const_2362,call_2366,uop_2370,])
func_2381 = relay.Function([var_2327,var_2361,], output)
mod['func_2381'] = func_2381
mod = relay.transform.InferType()(mod)
var_2382 = relay.var("var_2382", dtype = "bool", shape = (8, 13, 2))#candidate|2382|(8, 13, 2)|var|bool
var_2383 = relay.var("var_2383", dtype = "uint8", shape = (72,))#candidate|2383|(72,)|var|uint8
output = func_2381(var_2382,var_2383,)
func_2384 = relay.Function([var_2382,var_2383,], output)
mutated_mod['func_2384'] = func_2384
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2517 = relay.var("var_2517", dtype = "float32", shape = (5, 7, 7))#candidate|2517|(5, 7, 7)|var|float32
uop_2518 = relay.cosh(var_2517.astype('float32')) # shape=(5, 7, 7)
output = relay.Tuple([uop_2518,])
output2 = relay.Tuple([uop_2518,])
func_2525 = relay.Function([var_2517,], output)
mod['func_2525'] = func_2525
mod = relay.transform.InferType()(mod)
mutated_mod['func_2525'] = func_2525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2526 = relay.var("var_2526", dtype = "float32", shape = (5, 7, 7))#candidate|2526|(5, 7, 7)|var|float32
func_2525_call = mutated_mod.get_global_var('func_2525')
call_2527 = func_2525_call(var_2526)
output = call_2527
func_2528 = relay.Function([var_2526], output)
mutated_mod['func_2528'] = func_2528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2656 = relay.var("var_2656", dtype = "float32", shape = (12, 10, 6))#candidate|2656|(12, 10, 6)|var|float32
uop_2657 = relay.log(var_2656.astype('float32')) # shape=(12, 10, 6)
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
var_2663 = relay.var("var_2663", dtype = "uint8", shape = ())#candidate|2663|()|var|uint8
var_2664 = relay.var("var_2664", dtype = "uint8", shape = (72,))#candidate|2664|(72,)|var|uint8
const_2665 = relay.const([-3.043958,-4.052477,4.268870,-2.433945,3.118716,6.873433,5.559954,-1.078650,-2.567912,0.321671,0.033451,0.535568,7.788082,-0.533237,-3.859787,5.323591,7.949895,6.720520,5.610490,-6.223577,1.368973,-9.356533,-6.237238,8.323839,5.186788,-4.014330,-3.832966,9.140302,-1.005811,2.600497,1.792418,-0.812022,-0.802421,6.676706,5.818396,-0.651770,5.973495,-8.825071,1.018632,5.052894,-2.798236,5.240526,2.765821,-3.570037,-8.497714,2.310522,1.425259,3.633849,7.420992,8.630629,-5.128658,-1.305427,-6.616562,6.532392,-9.152707,6.219582,-6.035376,6.657816,3.814874,6.703453,6.233751,6.304003,-2.950248,-4.646679,0.323617,3.860566,5.800314,-1.397671,-5.026627,4.261428,-9.383253,8.934629,-3.157105,-4.041894,-4.067494,1.869534,-0.531181,-3.803380,9.868703,2.926678,-5.080798,-8.253336,-8.007631,-5.965769,-9.521091,0.256757,-0.236359,3.437780,0.886130,-0.079114,-9.497688,-3.732216,-7.289012,0.835492,4.390755,-6.867981,9.971988,-3.266060,0.715672,-8.699293,-0.419980,-6.378394,-5.859351,2.690774,-0.695510,-1.533476,-6.867532,7.049257,9.573379,-3.110617,1.329889,4.347608,-1.742485,-3.735722,-1.632182,9.383230,-2.072791,5.918583,-3.595206,3.767593,-0.229031,2.679311,-7.526255,5.523843,9.869801,-2.878578,-9.099497,-2.067547,2.649547,1.258921,9.461139,3.409940,-8.841765,8.245229,3.096683,5.494764,-9.125062,-0.349943,-4.764433,-9.958275,-6.795545,-1.012152,-1.380574,8.188058,-6.874766,6.701963,2.021353,0.478979,6.476562,-9.393751], dtype = "float32")#candidate|2665|(150,)|const|float32
call_2662 = relay.TupleGetItem(func_1678_call(relay.reshape(var_2663.astype('uint8'), []), relay.reshape(var_2664.astype('uint8'), [6, 2, 6]), relay.reshape(const_2665.astype('float32'), [150,]), ), 0)
call_2666 = relay.TupleGetItem(func_1682_call(relay.reshape(var_2663.astype('uint8'), []), relay.reshape(var_2664.astype('uint8'), [6, 2, 6]), relay.reshape(const_2665.astype('float32'), [150,]), ), 0)
output = relay.Tuple([uop_2657,call_2662,var_2663,var_2664,const_2665,])
output2 = relay.Tuple([uop_2657,call_2666,var_2663,var_2664,const_2665,])
func_2685 = relay.Function([var_2656,var_2663,var_2664,], output)
mod['func_2685'] = func_2685
mod = relay.transform.InferType()(mod)
mutated_mod['func_2685'] = func_2685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2685_call = mutated_mod.get_global_var('func_2685')
var_2687 = relay.var("var_2687", dtype = "float32", shape = (12, 10, 6))#candidate|2687|(12, 10, 6)|var|float32
var_2688 = relay.var("var_2688", dtype = "uint8", shape = ())#candidate|2688|()|var|uint8
var_2689 = relay.var("var_2689", dtype = "uint8", shape = (72,))#candidate|2689|(72,)|var|uint8
call_2686 = func_2685_call(var_2687,var_2688,var_2689,)
output = call_2686
func_2690 = relay.Function([var_2687,var_2688,var_2689,], output)
mutated_mod['func_2690'] = func_2690
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2748 = relay.const([[[-3,9,-6,4,4,6,6,2,-7,-8],[4,-9,-3,3,-7,3,3,-3,-5,-1]],[[-2,-4,-3,2,9,9,5,6,-6,-7],[6,-4,10,-10,-4,-3,-9,7,-3,-6]],[[-10,-6,4,5,2,2,2,9,-3,6],[-1,6,-5,-4,3,-1,-6,7,10,7]],[[-6,2,-4,9,-9,9,-3,9,-9,6],[-4,2,-5,-9,3,-9,-6,-4,-9,10]],[[-7,7,3,5,9,-3,-10,5,5,10],[-10,6,9,8,2,-7,6,-6,10,-10]],[[-5,-3,9,-10,-2,2,-1,-7,8,-10],[3,7,9,-10,-9,9,-5,-10,-10,9]],[[-5,3,-1,6,-8,-10,-2,-2,-2,-4],[-3,6,-5,2,-9,9,-4,-9,3,-4]],[[2,3,1,-6,8,-6,3,10,-10,-5],[-5,-2,7,6,5,-2,-6,-10,2,1]],[[-8,-2,-1,-8,5,10,8,-1,-1,6],[6,4,2,-10,2,6,-10,-2,1,2]],[[5,-7,3,-9,-2,-2,-2,-2,-2,9],[-2,5,-3,5,-7,1,-10,-7,4,-7]],[[3,-7,-8,7,9,-6,-3,5,8,-10],[-8,8,-9,2,5,10,-1,-10,3,-8]],[[7,5,5,-6,1,-9,-8,8,-4,-1],[-10,-6,9,7,-5,-6,9,2,1,-6]],[[-3,1,1,-9,8,3,-2,-8,-5,4],[-1,4,-2,-3,-2,5,-3,-9,8,9]],[[-9,-5,-1,1,-7,6,5,-10,-6,-10],[-2,-6,-3,-9,-10,-6,-9,9,3,6]],[[6,10,3,6,2,8,1,1,6,3],[-8,-6,-10,-9,-6,3,-10,-1,2,4]]], dtype = "uint16")#candidate|2748|(15, 2, 10)|const|uint16
var_2749 = relay.var("var_2749", dtype = "uint16", shape = (15, 2, 10))#candidate|2749|(15, 2, 10)|var|uint16
bop_2750 = relay.subtract(const_2748.astype('uint16'), relay.reshape(var_2749.astype('uint16'), relay.shape_of(const_2748))) # shape=(15, 2, 10)
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
var_2765 = relay.var("var_2765", dtype = "uint8", shape = ())#candidate|2765|()|var|uint8
const_2766 = relay.const([[10,-1,9,-3,-8,-10,-10,10,5,-7,3,-7],[-3,-2,8,9,5,4,-1,-4,-1,-4,7,8],[8,-7,3,7,-4,2,-1,9,-10,-10,9,2],[8,4,9,-9,7,8,-1,-7,4,-6,-10,-10],[7,1,-4,7,-8,7,-3,4,2,2,-7,-8],[-10,-5,-7,-1,5,-10,7,-10,10,-4,-4,7]], dtype = "uint8")#candidate|2766|(6, 12)|const|uint8
var_2767 = relay.var("var_2767", dtype = "float32", shape = (75, 2))#candidate|2767|(75, 2)|var|float32
call_2764 = relay.TupleGetItem(func_1678_call(relay.reshape(var_2765.astype('uint8'), []), relay.reshape(const_2766.astype('uint8'), [6, 2, 6]), relay.reshape(var_2767.astype('float32'), [150,]), ), 4)
call_2768 = relay.TupleGetItem(func_1682_call(relay.reshape(var_2765.astype('uint8'), []), relay.reshape(const_2766.astype('uint8'), [6, 2, 6]), relay.reshape(var_2767.astype('float32'), [150,]), ), 4)
output = relay.Tuple([bop_2750,call_2764,var_2765,const_2766,var_2767,])
output2 = relay.Tuple([bop_2750,call_2768,var_2765,const_2766,var_2767,])
func_2800 = relay.Function([var_2749,var_2765,var_2767,], output)
mod['func_2800'] = func_2800
mod = relay.transform.InferType()(mod)
mutated_mod['func_2800'] = func_2800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2800_call = mutated_mod.get_global_var('func_2800')
var_2802 = relay.var("var_2802", dtype = "uint16", shape = (15, 2, 10))#candidate|2802|(15, 2, 10)|var|uint16
var_2803 = relay.var("var_2803", dtype = "uint8", shape = ())#candidate|2803|()|var|uint8
var_2804 = relay.var("var_2804", dtype = "float32", shape = (75, 2))#candidate|2804|(75, 2)|var|float32
call_2801 = func_2800_call(var_2802,var_2803,var_2804,)
output = call_2801
func_2805 = relay.Function([var_2802,var_2803,var_2804,], output)
mutated_mod['func_2805'] = func_2805
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2938 = relay.var("var_2938", dtype = "float32", shape = (2, 9, 2))#candidate|2938|(2, 9, 2)|var|float32
var_2939 = relay.var("var_2939", dtype = "float32", shape = (2, 9, 2))#candidate|2939|(2, 9, 2)|var|float32
bop_2940 = relay.floor_divide(var_2938.astype('float32'), relay.reshape(var_2939.astype('float32'), relay.shape_of(var_2938))) # shape=(2, 9, 2)
func_2381_call = mod.get_global_var('func_2381')
func_2384_call = mutated_mod.get_global_var('func_2384')
var_2944 = relay.var("var_2944", dtype = "bool", shape = (208,))#candidate|2944|(208,)|var|bool
var_2945 = relay.var("var_2945", dtype = "uint8", shape = (36, 2))#candidate|2945|(36, 2)|var|uint8
call_2943 = relay.TupleGetItem(func_2381_call(relay.reshape(var_2944.astype('bool'), [8, 13, 2]), relay.reshape(var_2945.astype('uint8'), [72,]), ), 6)
call_2946 = relay.TupleGetItem(func_2384_call(relay.reshape(var_2944.astype('bool'), [8, 13, 2]), relay.reshape(var_2945.astype('uint8'), [72,]), ), 6)
uop_2974 = relay.asin(var_2939.astype('float64')) # shape=(2, 9, 2)
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
var_2978 = relay.var("var_2978", dtype = "uint8", shape = ())#candidate|2978|()|var|uint8
const_2979 = relay.const([[-1.191462,-8.585904],[3.887625,5.185608],[-2.077136,-2.316110],[6.399773,-5.125532],[1.140776,-4.541592],[4.346606,5.103786],[6.154137,-2.355440],[3.481661,-8.971714],[-3.562742,0.182127],[-2.666949,4.359520],[-7.142785,-5.876719],[5.649593,-7.177501],[-1.042429,9.643037],[9.275655,-0.595497],[-6.030977,-2.792525],[-7.278969,2.043794],[-0.540951,7.078286],[-6.158409,9.931312],[-2.058996,-2.053695],[1.922171,-7.479207],[6.394363,7.659705],[-7.177489,2.826785],[-1.682604,-3.192187],[9.015189,6.553813],[-1.124724,-4.930365],[8.789564,-3.191886],[-3.373338,9.539159],[1.435466,4.913793],[-9.678078,2.856076],[-6.717477,8.453150],[6.029158,8.681061],[1.206414,-8.654441],[9.769491,-2.732921],[-3.743390,7.234103],[1.108211,-0.118882],[-9.836690,-6.346112],[2.750740,-2.177622],[-7.842212,-1.775935],[3.870359,-0.048937],[9.028153,4.003136],[-3.788683,9.619974],[-8.036081,6.419797],[-4.992051,-8.259229],[6.236265,8.449667],[-5.530973,-5.866396],[3.407447,-5.700527],[-4.896758,2.453519],[0.504880,9.734997],[1.519437,2.474843],[9.193968,1.071878],[-3.222909,-1.550628],[-3.118367,-9.257416],[8.019985,-9.564844],[-1.626018,-9.521759],[6.173383,-8.317615],[-5.689854,-1.477580],[-1.920856,1.573495],[-7.878064,4.082305],[-1.393077,-8.423157],[4.630022,8.098054],[2.956027,6.974254],[9.468664,1.256061],[-5.511609,0.555035],[6.612381,-4.220328],[0.599224,0.369915],[-5.469934,8.129204],[-4.951339,-9.393230],[-5.115840,8.891162],[7.044920,9.368677],[-5.744508,6.117524],[-1.874275,4.896044],[7.471873,-6.278558],[6.272137,-8.205881],[-0.499377,-2.415595],[-5.468740,1.773460]], dtype = "float32")#candidate|2979|(75, 2)|const|float32
call_2977 = relay.TupleGetItem(func_1678_call(relay.reshape(var_2978.astype('uint8'), []), relay.reshape(var_2945.astype('uint8'), [6, 2, 6]), relay.reshape(const_2979.astype('float32'), [150,]), ), 0)
call_2980 = relay.TupleGetItem(func_1682_call(relay.reshape(var_2978.astype('uint8'), []), relay.reshape(var_2945.astype('uint8'), [6, 2, 6]), relay.reshape(const_2979.astype('float32'), [150,]), ), 0)
output = relay.Tuple([bop_2940,call_2943,var_2944,var_2945,uop_2974,call_2977,var_2978,const_2979,])
output2 = relay.Tuple([bop_2940,call_2946,var_2944,var_2945,uop_2974,call_2980,var_2978,const_2979,])
func_2982 = relay.Function([var_2938,var_2939,var_2944,var_2945,var_2978,], output)
mod['func_2982'] = func_2982
mod = relay.transform.InferType()(mod)
var_2983 = relay.var("var_2983", dtype = "float32", shape = (2, 9, 2))#candidate|2983|(2, 9, 2)|var|float32
var_2984 = relay.var("var_2984", dtype = "float32", shape = (2, 9, 2))#candidate|2984|(2, 9, 2)|var|float32
var_2985 = relay.var("var_2985", dtype = "bool", shape = (208,))#candidate|2985|(208,)|var|bool
var_2986 = relay.var("var_2986", dtype = "uint8", shape = (36, 2))#candidate|2986|(36, 2)|var|uint8
var_2987 = relay.var("var_2987", dtype = "uint8", shape = ())#candidate|2987|()|var|uint8
output = func_2982(var_2983,var_2984,var_2985,var_2986,var_2987,)
func_2988 = relay.Function([var_2983,var_2984,var_2985,var_2986,var_2987,], output)
mutated_mod['func_2988'] = func_2988
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3035 = relay.var("var_3035", dtype = "float32", shape = ())#candidate|3035|()|var|float32
var_3036 = relay.var("var_3036", dtype = "float32", shape = (2, 8, 15))#candidate|3036|(2, 8, 15)|var|float32
bop_3037 = relay.floor_mod(var_3035.astype('float32'), var_3036.astype('float32')) # shape=(2, 8, 15)
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
const_3041 = relay.const([-8,-10,-10,-8,2,7,-7,-5,7,-5,-10,-6,-4,5,8,10,-6,5,-3,6,-8,9,4,-4,-1,2,3,-2,-5,-2,-3,-2,-1,5,-9,9,-6,3,-4,4,7,9,-4,-6,10,-5,-8,-1,4,-7,9,-10,-6,-8,1,6,-8,5,-5,-4,-9,-7,-3,-10,-8,-2,2,-3,-7,7,-3,-6], dtype = "uint8")#candidate|3041|(72,)|const|uint8
const_3042 = relay.const([[8.167638,-7.982946,1.229299,8.036291,-5.302446,-0.309116,0.145521,4.779012,-5.174777,-8.412829,-8.807025,-6.879945,-3.854540,7.240797,5.146532,9.859398,6.598154,8.688798,-6.045769,-2.362659,9.496455,0.214144,-8.834154,-9.298360,4.053170,3.771608,7.432082,-8.086261,8.727058,-3.136731,9.108214,8.474933,6.894199,9.538380,5.418256,-3.548259,-3.683697,-8.682970,5.432381,-4.249858,5.634577,-1.942402,2.459610,-8.413785,0.771709,6.002013,6.595185,4.622412,8.111509,-3.401982,-7.656135,-6.371021,-2.771472,2.348947,6.508575,5.813271,0.691318,3.154569,-3.313551,2.714097,-9.931066,3.890934,9.331643,4.074916,0.558089,-4.192881,-7.712466,4.511138,8.436896,-7.996472,-8.555733,5.517107,-2.472235,-9.555620,3.546480,-8.751148,-1.447233,8.825142,-2.814826,-0.995426,-8.112818,2.827750,7.307628,4.295032,5.498348,7.244352,2.427142,7.171222,0.787354,2.828602,9.088991,9.412978,9.315051,1.758553,3.819066,2.827655,-7.641571,-8.149123,1.317368,-1.740610,-5.453101,-4.051638,0.181643,4.894636,3.051165,8.767527,-9.304291,-7.305542,4.471998,6.816320,-8.748199,-9.777931,3.685430,-7.525390,-9.426747,1.310904,4.237964,7.460703,9.708489,3.644782,7.025121,8.353734,6.106916,9.317767,3.022803,4.888167,6.145150,5.073596,7.995305,-0.970870,-6.727468,-8.481254,2.323821,-6.065780,-0.207097,-6.266298,-1.138211,4.086113,8.113363,-3.207590,3.550098,-4.319067,8.739834,5.995718,-9.703166,5.013278,5.208067,-8.304413,2.472887,8.875708]], dtype = "float32")#candidate|3042|(1, 150)|const|float32
call_3040 = relay.TupleGetItem(func_1678_call(relay.reshape(var_3035.astype('uint8'), []), relay.reshape(const_3041.astype('uint8'), [6, 2, 6]), relay.reshape(const_3042.astype('float32'), [150,]), ), 3)
call_3043 = relay.TupleGetItem(func_1682_call(relay.reshape(var_3035.astype('uint8'), []), relay.reshape(const_3041.astype('uint8'), [6, 2, 6]), relay.reshape(const_3042.astype('float32'), [150,]), ), 3)
func_2982_call = mod.get_global_var('func_2982')
func_2988_call = mutated_mod.get_global_var('func_2988')
const_3048 = relay.const([[4.596084,-0.868024,-2.194597,7.168818,5.665358,-2.016595,3.634322,-0.869374,-3.664633,9.161102,0.139442,-5.161629],[7.329524,5.950704,-5.300116,-3.372867,-8.173225,-3.259496,-9.399802,-2.414387,-1.324939,-7.197211,-7.278466,-5.437549],[-7.054859,-5.125513,8.400123,7.754439,8.651157,-6.830886,1.116929,1.065439,8.007086,-6.457425,-8.678822,6.921051]], dtype = "float32")#candidate|3048|(3, 12)|const|float32
var_3049 = relay.var("var_3049", dtype = "bool", shape = (2, 104))#candidate|3049|(2, 104)|var|bool
call_3047 = relay.TupleGetItem(func_2982_call(relay.reshape(const_3048.astype('float32'), [2, 9, 2]), relay.reshape(const_3048.astype('float32'), [2, 9, 2]), relay.reshape(var_3049.astype('bool'), [208,]), relay.reshape(const_3041.astype('uint8'), [36, 2]), relay.reshape(var_3035.astype('uint8'), []), ), 1)
call_3050 = relay.TupleGetItem(func_2988_call(relay.reshape(const_3048.astype('float32'), [2, 9, 2]), relay.reshape(const_3048.astype('float32'), [2, 9, 2]), relay.reshape(var_3049.astype('bool'), [208,]), relay.reshape(const_3041.astype('uint8'), [36, 2]), relay.reshape(var_3035.astype('uint8'), []), ), 1)
output = relay.Tuple([bop_3037,call_3040,const_3041,const_3042,call_3047,const_3048,var_3049,])
output2 = relay.Tuple([bop_3037,call_3043,const_3041,const_3042,call_3050,const_3048,var_3049,])
func_3055 = relay.Function([var_3035,var_3036,var_3049,], output)
mod['func_3055'] = func_3055
mod = relay.transform.InferType()(mod)
var_3056 = relay.var("var_3056", dtype = "float32", shape = ())#candidate|3056|()|var|float32
var_3057 = relay.var("var_3057", dtype = "float32", shape = (2, 8, 15))#candidate|3057|(2, 8, 15)|var|float32
var_3058 = relay.var("var_3058", dtype = "bool", shape = (2, 104))#candidate|3058|(2, 104)|var|bool
output = func_3055(var_3056,var_3057,var_3058,)
func_3059 = relay.Function([var_3056,var_3057,var_3058,], output)
mutated_mod['func_3059'] = func_3059
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3670 = relay.var("var_3670", dtype = "float32", shape = ())#candidate|3670|()|var|float32
var_3671 = relay.var("var_3671", dtype = "float32", shape = (10, 6, 10))#candidate|3671|(10, 6, 10)|var|float32
bop_3672 = relay.power(var_3670.astype('float32'), var_3671.astype('float32')) # shape=(10, 6, 10)
func_2800_call = mod.get_global_var('func_2800')
func_2805_call = mutated_mod.get_global_var('func_2805')
var_3698 = relay.var("var_3698", dtype = "uint16", shape = (300,))#candidate|3698|(300,)|var|uint16
const_3699 = relay.const([[6.318776,-3.657607,-6.314861,5.678321,-8.713303,-0.524986],[-6.919318,6.196949,-3.434502,-4.357695,2.183154,6.747615],[-8.083079,-9.728406,6.108537,8.299176,9.986620,8.159599],[7.330558,7.458065,-3.040725,-9.292480,3.397167,1.671233],[5.954775,-5.761368,-2.066773,4.576851,-2.160416,5.996519],[1.218212,-2.506335,-0.554914,-1.678223,-8.170490,-8.334768],[1.899010,-7.795190,-6.469841,-7.299733,4.448778,-9.021077],[-3.721333,5.020413,5.911264,-5.704871,1.496588,9.174249],[-3.601742,6.176697,0.859604,0.166295,9.777065,9.036808],[6.773624,9.463323,1.442983,-1.160234,7.741589,-1.789013],[5.739649,0.836802,-0.741867,-7.256224,-0.527118,6.697114],[4.777998,-2.695755,-8.682827,-6.530349,-2.504791,3.961308],[6.326736,4.010061,1.578705,2.351748,7.359678,5.822251],[-3.055285,-2.036289,-2.964357,-4.572567,5.699908,-3.406844],[5.199228,0.083451,-5.331118,2.325929,8.956150,-2.545253],[-1.622430,8.502163,0.346661,8.934206,-8.819573,-4.008243],[-3.522308,2.807564,-1.298443,3.056494,-0.043293,2.990760],[7.184907,0.421509,8.567403,5.961242,6.347169,7.552283],[-5.862091,-1.539930,8.486498,3.958694,-8.490347,4.757580],[-4.911142,-8.034185,4.154503,1.899762,-0.043225,7.408608],[-5.631860,8.416511,7.758888,-9.246654,-8.060586,5.189769],[-8.345089,3.165537,6.458362,3.925285,5.588053,-8.144422],[9.513043,-1.617882,-6.751203,9.063567,-5.728913,7.311049],[-9.671090,8.148429,-1.870408,-3.906843,2.410971,4.700597],[-9.622343,-6.209006,-6.689038,-5.493789,-2.896784,7.591034]], dtype = "float32")#candidate|3699|(25, 6)|const|float32
call_3697 = relay.TupleGetItem(func_2800_call(relay.reshape(var_3698.astype('uint16'), [15, 2, 10]), relay.reshape(var_3670.astype('uint8'), []), relay.reshape(const_3699.astype('float32'), [75, 2]), ), 3)
call_3700 = relay.TupleGetItem(func_2805_call(relay.reshape(var_3698.astype('uint16'), [15, 2, 10]), relay.reshape(var_3670.astype('uint8'), []), relay.reshape(const_3699.astype('float32'), [75, 2]), ), 3)
func_2982_call = mod.get_global_var('func_2982')
func_2988_call = mutated_mod.get_global_var('func_2988')
var_3714 = relay.var("var_3714", dtype = "float32", shape = (18, 2))#candidate|3714|(18, 2)|var|float32
var_3715 = relay.var("var_3715", dtype = "bool", shape = (1, 208))#candidate|3715|(1, 208)|var|bool
call_3713 = relay.TupleGetItem(func_2982_call(relay.reshape(var_3714.astype('float32'), [2, 9, 2]), relay.reshape(var_3714.astype('float32'), [2, 9, 2]), relay.reshape(var_3715.astype('bool'), [208,]), relay.reshape(call_3697.astype('uint8'), [36, 2]), relay.reshape(var_3670.astype('uint8'), []), ), 3)
call_3716 = relay.TupleGetItem(func_2988_call(relay.reshape(var_3714.astype('float32'), [2, 9, 2]), relay.reshape(var_3714.astype('float32'), [2, 9, 2]), relay.reshape(var_3715.astype('bool'), [208,]), relay.reshape(call_3697.astype('uint8'), [36, 2]), relay.reshape(var_3670.astype('uint8'), []), ), 3)
uop_3722 = relay.atanh(var_3714.astype('float32')) # shape=(18, 2)
var_3733 = relay.var("var_3733", dtype = "bool", shape = (3, 208))#candidate|3733|(3, 208)|var|bool
bop_3734 = relay.multiply(var_3715.astype('uint64'), var_3733.astype('uint64')) # shape=(3, 208)
bop_3741 = relay.not_equal(uop_3722.astype('bool'), var_3670.astype('bool')) # shape=(18, 2)
func_2685_call = mod.get_global_var('func_2685')
func_2690_call = mutated_mod.get_global_var('func_2690')
var_3751 = relay.var("var_3751", dtype = "float32", shape = (60, 12))#candidate|3751|(60, 12)|var|float32
call_3750 = relay.TupleGetItem(func_2685_call(relay.reshape(var_3751.astype('float32'), [12, 10, 6]), relay.reshape(var_3670.astype('uint8'), []), relay.reshape(call_3697.astype('uint8'), [72,]), ), 2)
call_3752 = relay.TupleGetItem(func_2690_call(relay.reshape(var_3751.astype('float32'), [12, 10, 6]), relay.reshape(var_3670.astype('uint8'), []), relay.reshape(call_3697.astype('uint8'), [72,]), ), 2)
uop_3780 = relay.tan(uop_3722.astype('float32')) # shape=(18, 2)
uop_3784 = relay.acosh(uop_3780.astype('float64')) # shape=(18, 2)
bop_3788 = relay.multiply(uop_3784.astype('float64'), call_3750.astype('float64')) # shape=(18, 2)
bop_3791 = relay.multiply(uop_3784.astype('float64'), call_3752.astype('float64')) # shape=(18, 2)
func_2982_call = mod.get_global_var('func_2982')
func_2988_call = mutated_mod.get_global_var('func_2988')
call_3800 = relay.TupleGetItem(func_2982_call(relay.reshape(uop_3722.astype('float32'), [2, 9, 2]), relay.reshape(uop_3784.astype('float32'), [2, 9, 2]), relay.reshape(var_3715.astype('bool'), [208,]), relay.reshape(call_3713.astype('uint8'), [36, 2]), relay.reshape(call_3750.astype('uint8'), []), ), 7)
call_3801 = relay.TupleGetItem(func_2988_call(relay.reshape(uop_3722.astype('float32'), [2, 9, 2]), relay.reshape(uop_3784.astype('float32'), [2, 9, 2]), relay.reshape(var_3715.astype('bool'), [208,]), relay.reshape(call_3713.astype('uint8'), [36, 2]), relay.reshape(call_3750.astype('uint8'), []), ), 7)
bop_3803 = relay.bitwise_and(uop_3784.astype('int32'), relay.reshape(uop_3722.astype('int32'), relay.shape_of(uop_3784))) # shape=(18, 2)
uop_3806 = relay.cosh(bop_3803.astype('float64')) # shape=(18, 2)
output = relay.Tuple([bop_3672,call_3697,var_3698,const_3699,call_3713,bop_3734,bop_3741,var_3751,bop_3788,call_3800,uop_3806,])
output2 = relay.Tuple([bop_3672,call_3700,var_3698,const_3699,call_3716,bop_3734,bop_3741,var_3751,bop_3791,call_3801,uop_3806,])
func_3812 = relay.Function([var_3670,var_3671,var_3698,var_3714,var_3715,var_3733,var_3751,], output)
mod['func_3812'] = func_3812
mod = relay.transform.InferType()(mod)
var_3813 = relay.var("var_3813", dtype = "float32", shape = ())#candidate|3813|()|var|float32
var_3814 = relay.var("var_3814", dtype = "float32", shape = (10, 6, 10))#candidate|3814|(10, 6, 10)|var|float32
var_3815 = relay.var("var_3815", dtype = "uint16", shape = (300,))#candidate|3815|(300,)|var|uint16
var_3816 = relay.var("var_3816", dtype = "float32", shape = (18, 2))#candidate|3816|(18, 2)|var|float32
var_3817 = relay.var("var_3817", dtype = "bool", shape = (1, 208))#candidate|3817|(1, 208)|var|bool
var_3818 = relay.var("var_3818", dtype = "bool", shape = (3, 208))#candidate|3818|(3, 208)|var|bool
var_3819 = relay.var("var_3819", dtype = "float32", shape = (60, 12))#candidate|3819|(60, 12)|var|float32
output = func_3812(var_3813,var_3814,var_3815,var_3816,var_3817,var_3818,var_3819,)
func_3820 = relay.Function([var_3813,var_3814,var_3815,var_3816,var_3817,var_3818,var_3819,], output)
mutated_mod['func_3820'] = func_3820
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4148 = relay.const([[[8.318566,7.685442,-2.285312,-4.148715,-6.030871,6.394229,-2.745696,-4.663346,-6.036846,2.917527,7.605290]],[[-6.006881,8.327632,8.752402,2.401142,-8.381384,3.278955,-7.354917,1.040644,3.979031,6.323594,2.015838]],[[-0.908006,5.680221,8.862473,-6.153785,-3.155352,-2.135488,-4.784358,-0.453405,-6.727724,5.672242,-0.126787]],[[6.329113,-1.535516,5.098191,3.082253,-5.060765,4.435265,3.127436,-6.195568,4.864900,-4.650504,-3.304862]],[[3.696167,5.109300,2.865036,3.272513,-7.119069,9.107728,8.207312,-3.538224,3.029081,3.852876,-2.374219]],[[-4.863118,-7.110443,8.440001,9.832164,-8.357977,-6.190617,0.590323,-6.961931,2.891555,5.605574,2.811639]],[[-9.396716,-1.669924,-0.355468,-0.243992,-5.411916,7.562232,-6.084997,3.874514,-4.907258,-9.401591,9.477690]],[[-4.259803,4.590936,-5.964588,5.298244,0.061608,-1.888486,9.009021,8.281045,3.028005,-0.469298,2.309641]],[[-2.757723,6.967871,-5.704609,6.468140,3.719021,6.666553,-3.096419,4.920097,0.620348,9.005712,-4.894159]],[[4.808238,-6.729223,1.477862,2.192567,4.628433,-6.026634,0.285401,-7.478749,-0.144557,-0.382250,-9.526670]],[[-8.633918,-8.739662,4.741734,0.144931,4.733640,3.602751,6.318414,-2.686725,3.231942,-3.282831,-7.269227]],[[-1.464766,0.310586,-1.100374,-0.655091,-5.316542,2.022058,1.783642,-0.179318,-0.649088,2.942542,7.798337]]], dtype = "float64")#candidate|4148|(12, 1, 11)|const|float64
uop_4149 = relay.exp(const_4148.astype('float64')) # shape=(12, 1, 11)
func_2982_call = mod.get_global_var('func_2982')
func_2988_call = mutated_mod.get_global_var('func_2988')
const_4155 = relay.const([0.449498,-6.747050,8.659550,-6.052086,-6.827433,1.001291,-7.052665,8.647223,7.358010,-2.467687,-2.789300,-7.434684,-4.044533,-5.470883,-0.377708,-9.662845,-6.309727,8.593404,8.249385,-4.690021,-9.354330,8.095903,1.343499,6.410065,-3.313758,-3.459952,7.824530,-8.558319,8.047826,3.532397,6.433202,6.026219,-3.543905,5.898503,4.803820,-7.844355], dtype = "float32")#candidate|4155|(36,)|const|float32
var_4156 = relay.var("var_4156", dtype = "bool", shape = (1, 208))#candidate|4156|(1, 208)|var|bool
const_4157 = relay.const([-1,-1,5,9,-8,-9,10,-3,6,-4,-4,-10,9,-1,5,9,-6,-7,2,1,4,8,-5,-5,-4,7,9,6,-5,1,4,10,-2,3,4,5,-5,-5,5,1,-1,7,6,-2,-4,-2,2,-2,-10,8,10,3,-8,8,-10,-3,7,-1,-5,5,5,-10,1,1,7,-7,-5,-4,9,-4,-1,10], dtype = "uint8")#candidate|4157|(72,)|const|uint8
const_4158 = relay.const(2, dtype = "uint8")#candidate|4158|()|const|uint8
call_4154 = relay.TupleGetItem(func_2982_call(relay.reshape(const_4155.astype('float32'), [2, 9, 2]), relay.reshape(const_4155.astype('float32'), [2, 9, 2]), relay.reshape(var_4156.astype('bool'), [208,]), relay.reshape(const_4157.astype('uint8'), [36, 2]), relay.reshape(const_4158.astype('uint8'), []), ), 5)
call_4159 = relay.TupleGetItem(func_2988_call(relay.reshape(const_4155.astype('float32'), [2, 9, 2]), relay.reshape(const_4155.astype('float32'), [2, 9, 2]), relay.reshape(var_4156.astype('bool'), [208,]), relay.reshape(const_4157.astype('uint8'), [36, 2]), relay.reshape(const_4158.astype('uint8'), []), ), 5)
func_3055_call = mod.get_global_var('func_3055')
func_3059_call = mutated_mod.get_global_var('func_3059')
const_4161 = relay.const([-9.407015,-0.192245,-0.707278,3.218600,8.751257,-5.768685,8.653503,1.181249,-7.915817,-5.669453,3.978272,1.247507,-3.193722,-0.185929,9.137226,-1.021298,-0.734434,3.448013,-1.093897,0.173035,-5.396084,7.356758,6.125319,5.609227,7.210324,-5.019292,0.222422,7.184489,-8.148879,6.414674,-8.986683,-9.267741,-8.277598,2.846695,-7.101697,-5.644195,-6.945449,-9.597585,-1.425024,4.211388,6.334913,-3.811510,-1.218357,-3.129903,-5.865393,-2.515036,-8.591429,6.343585,-3.774915,6.522996,5.047274,0.497548,3.626401,-6.638528,5.192072,4.379787,6.103722,0.595111,-8.897709,-7.772934,0.242165,9.613962,3.681691,3.489429,4.036107,-8.449261,-2.204398,-4.096201,8.500701,-3.988516,-8.436057,-2.031036,2.672465,3.429650,3.739055,-4.809134,4.519197,-1.000061,-9.390172,-5.100845,4.746989,1.404575,9.123451,9.307025,-5.980317,1.789641,-0.023237,-3.847947,-2.212934,9.133497,0.945460,-4.603005,1.851937,-2.146165,-3.817561,4.096169,0.289829,-3.370445,-9.190473,-3.062139,0.816224,2.026793,0.990889,6.059042,-3.831036,8.813527,5.446497,-5.379346,6.048261,-3.374791,8.716109,4.671030,-1.223947,3.511223,7.248537,4.522423,-5.835354,-6.270542,-0.656682,3.287045,-6.893875,0.132772,-4.218379,-7.370610,-0.960308,-4.350569,-9.886984,-7.997739,7.958463,3.163525,1.844504,0.554221,-5.883955,5.581285,7.658800,8.455779,-7.405206,0.336395,-1.854320,-0.977689,6.531028,-3.619081,-9.891607,-2.074374,2.547437,-5.136150,2.075887,-1.738265,-3.800893,-9.673776,-3.064981,8.494375,-2.014134,1.291630,7.427655,7.001651,-7.156040,-1.252452,9.539597,-4.219178,1.776218,4.645635,-7.177238,-0.101357,-9.819772,3.210625,-5.813584,7.348212,3.431150,4.637978,-6.844167,9.157717,-9.433388,8.577619,5.397403,-3.494227,-3.837465,1.954645,7.663801,4.303384,-6.636671,-6.186186,-0.947763,-5.755247,1.963467,-1.536718,-2.207573,-5.606337,1.714179,-1.814196,-0.873535,6.343232,0.984801,8.928517,-2.813145,-7.517786,4.512326,2.411134,-8.024133,-5.260255,9.943100,2.366218,-9.540240,6.379392,7.791759,-7.502225,-0.477040,-2.377330,-1.856989,8.682142,6.792125,-5.114858,-7.181044,-9.380381,8.735006,-2.806346,8.010839,-0.236952,-0.350420,0.007242,-5.856498,3.270206,-4.581683,-8.645203,4.879885,9.226940,5.775974,-7.837484,-7.068890,-7.757247,2.789924,-0.693032,-1.608453,-6.777822,-8.382795,-9.291333,-2.984372,-3.862251,5.795308,2.032611], dtype = "float32")#candidate|4161|(240,)|const|float32
call_4160 = relay.TupleGetItem(func_3055_call(relay.reshape(const_4158.astype('float32'), []), relay.reshape(const_4161.astype('float32'), [2, 8, 15]), relay.reshape(var_4156.astype('bool'), [2, 104]), ), 0)
call_4162 = relay.TupleGetItem(func_3059_call(relay.reshape(const_4158.astype('float32'), []), relay.reshape(const_4161.astype('float32'), [2, 8, 15]), relay.reshape(var_4156.astype('bool'), [2, 104]), ), 0)
bop_4164 = relay.bitwise_and(var_4156.astype('uint64'), const_4158.astype('uint64')) # shape=(1, 208)
func_3055_call = mod.get_global_var('func_3055')
func_3059_call = mutated_mod.get_global_var('func_3059')
call_4170 = relay.TupleGetItem(func_3055_call(relay.reshape(const_4158.astype('float32'), []), relay.reshape(call_4160.astype('float32'), [2, 8, 15]), relay.reshape(bop_4164.astype('bool'), [2, 104]), ), 6)
call_4171 = relay.TupleGetItem(func_3059_call(relay.reshape(const_4158.astype('float32'), []), relay.reshape(call_4160.astype('float32'), [2, 8, 15]), relay.reshape(bop_4164.astype('bool'), [2, 104]), ), 6)
output = relay.Tuple([uop_4149,call_4154,const_4155,const_4157,call_4160,const_4161,bop_4164,call_4170,])
output2 = relay.Tuple([uop_4149,call_4159,const_4155,const_4157,call_4162,const_4161,bop_4164,call_4171,])
func_4176 = relay.Function([var_4156,], output)
mod['func_4176'] = func_4176
mod = relay.transform.InferType()(mod)
mutated_mod['func_4176'] = func_4176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4177 = relay.var("var_4177", dtype = "bool", shape = (1, 208))#candidate|4177|(1, 208)|var|bool
func_4176_call = mutated_mod.get_global_var('func_4176')
call_4178 = func_4176_call(var_4177)
output = call_4178
func_4179 = relay.Function([var_4177], output)
mutated_mod['func_4179'] = func_4179
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4617 = relay.const([[[-4.392765,-3.419173,0.877632,4.958955,-3.167968,6.112809,-1.445290,-1.178224,-9.371107,-4.930672,7.506507,-5.433793,4.878982,4.862243],[1.459192,-6.129337,5.191043,6.282540,0.173861,0.728798,-8.985076,6.503547,6.395075,6.896811,-0.072065,0.806132,-7.047509,6.336282],[7.285934,-4.895890,9.479265,-0.464977,3.282131,8.874283,-2.263464,-8.649041,8.836363,1.136735,2.205574,3.959842,5.392200,7.574333],[-4.523089,8.039645,-2.757937,-9.389270,-3.996364,-8.255842,-1.185980,-7.066756,-5.483606,2.772785,1.254397,-8.063256,5.918692,-0.445101],[-5.255828,9.359488,-9.683581,-1.140810,-6.084849,5.055186,3.809127,-6.598504,7.530949,-8.695279,6.280036,-6.094735,6.329765,-8.030924],[-1.160138,4.169181,-1.811282,9.405718,9.980750,6.755959,-0.970629,5.614916,-2.511373,5.110325,-3.493485,2.872927,5.955239,-2.225336],[7.907084,-5.469527,-9.133670,-0.409129,-0.471154,6.364161,-2.188277,4.705197,2.692121,-2.164493,-4.664472,-3.335717,-2.964586,-4.712802],[8.371597,-4.719576,6.957609,-7.613602,-1.452344,3.810202,-8.050770,-6.938126,3.955813,7.008038,-6.405220,3.418891,5.501832,-2.302105],[6.946158,0.452561,6.439777,8.703526,-9.241592,-4.445978,5.476525,1.902767,0.850379,-2.171237,4.747957,6.405897,3.373993,-8.014382],[-6.914947,-6.386651,-2.122219,-1.364254,5.216429,-4.916875,3.200268,-6.502124,-6.865992,-6.411230,-2.043258,3.299522,-6.906773,2.704955],[3.645507,-3.356118,-7.422998,8.406542,3.083048,0.720040,-2.121995,-1.057916,-8.390772,-1.994400,5.730497,-8.894045,8.930069,3.940113]],[[9.645912,6.262658,4.278709,-5.936722,6.611396,-9.608696,-0.678128,9.144022,4.192194,-1.945527,7.764756,7.106993,-4.239818,-8.059176],[8.650497,2.203377,-7.752499,5.265549,9.584960,-0.733089,5.975042,4.479618,-8.412565,-0.906171,-3.070020,9.481835,5.375693,-8.687806],[3.591605,9.000841,0.306090,3.570061,-0.463382,6.226327,-3.733691,-3.448625,-5.330573,5.937493,-2.287600,-5.361117,1.999755,-4.415189],[-2.823938,-1.901657,2.427073,-0.100450,-8.652504,7.302283,-9.224960,-6.900746,-3.187606,8.336882,-8.437530,5.624414,-2.092550,-0.265991],[6.102390,6.664051,3.019343,5.290587,1.064652,3.058441,7.879194,-7.870316,3.330854,4.495949,7.188150,-9.120372,3.670627,0.115593],[-5.692557,5.884419,-0.459621,1.775318,-0.342461,0.395739,0.864836,-7.925318,5.184834,-0.528401,1.146165,-3.810372,-8.930679,2.621045],[-9.197670,-1.290721,-5.394897,-1.188977,-1.630752,-9.763442,3.485324,-4.577838,2.517853,1.008510,-1.940033,3.215929,9.976710,-3.528064],[6.904615,-7.317867,-7.532315,-5.723232,-3.764421,-5.028583,-2.680196,-8.812073,-6.022684,-2.456274,8.132897,-4.502397,-2.144125,1.676633],[5.448885,4.016814,1.217102,-2.564246,-3.337321,-0.490308,6.053676,8.097988,-8.139680,4.940611,1.213193,-4.910849,-8.052703,-9.904484],[-9.570567,-3.606460,9.704911,-7.795895,4.051994,9.273440,3.650953,2.978330,-7.088046,5.181291,-9.192148,0.838465,-5.564726,-8.546559],[-1.570453,4.798823,-1.963637,-3.856516,-4.382572,0.387152,9.227959,3.044671,-9.388231,0.345917,-1.482914,0.429599,-0.363631,-3.953443]],[[-0.508283,0.003037,6.903782,-8.377606,-7.646440,7.417057,1.760058,8.647379,4.292067,-7.553947,7.023509,-9.117798,-1.604493,-6.946657],[-5.192441,6.404855,5.714441,9.655900,-7.224452,-9.656715,-8.030992,0.891500,-1.874508,-7.023253,5.766257,-8.731978,3.890560,-6.063975],[-8.011240,-9.865033,9.863443,-5.709556,-7.238272,3.463021,8.825610,5.455943,-9.002780,9.374972,5.109010,-7.839472,-9.384582,0.313452],[-4.966425,2.102661,-0.415812,3.012690,-0.275008,-7.055668,-8.148381,2.424565,-2.454673,0.838867,9.735864,5.443513,6.132876,9.867318],[-3.426873,4.245987,3.274467,-7.917991,-1.402871,7.798388,4.547462,9.683326,-9.579033,9.909106,1.912605,1.812351,0.519400,-3.692798],[-7.728019,0.345732,-4.722250,7.806983,6.613758,-1.703439,-0.068510,-5.253326,6.133643,0.899127,-0.382120,-4.124386,3.737060,-9.243050],[2.963252,4.559217,9.016114,-5.850785,2.655080,6.014001,0.300219,-7.321812,5.336270,3.228715,-6.108555,-6.767450,3.912013,2.407126],[-2.106545,-7.175556,-1.619675,-0.182186,-5.039109,2.884295,-7.022945,-3.961872,-4.625294,8.988327,-4.689615,2.132648,8.178773,9.388297],[-6.462816,-0.169716,9.160243,-4.539931,-2.301818,8.397093,-7.346157,3.489109,6.159803,-4.237660,-8.275016,9.026212,8.223035,-0.650227],[9.464484,0.145593,-6.228528,-1.912476,-2.802914,9.017800,1.771064,8.892805,3.658413,8.616909,7.457799,3.263263,5.703845,-3.780894],[5.128128,-6.390143,-7.004272,-3.035378,7.317617,-2.845943,-0.554469,-4.864483,-6.390772,6.849848,-5.889423,-6.038436,-8.127993,-5.369708]]], dtype = "float32")#candidate|4617|(3, 11, 14)|const|float32
uop_4618 = relay.asinh(const_4617.astype('float32')) # shape=(3, 11, 14)
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
const_4634 = relay.const(-10, dtype = "uint8")#candidate|4634|()|const|uint8
var_4635 = relay.var("var_4635", dtype = "uint8", shape = (72,))#candidate|4635|(72,)|var|uint8
const_4636 = relay.const([-8.834016,-2.976407,-7.587729,2.076844,-4.475894,-3.303532,-8.865608,5.672172,9.599306,0.787638,-4.239489,-8.426402,0.421846,-2.717627,-7.125443,-1.961956,-6.134480,-4.107020,9.059146,1.172813,-9.623692,-6.954162,3.222893,-0.559234,-1.537351,-0.654289,-2.408912,-2.995200,-3.700632,-4.269247,-1.863308,7.453284,9.688623,2.018186,-0.731088,5.452674,1.443381,8.902088,2.762316,4.453839,8.391713,-5.072551,-4.850171,3.890628,8.282817,-3.222266,-3.076831,9.359986,9.996748,-2.154312,2.732609,-2.473948,4.626226,4.124119,-1.604568,2.902890,-7.584484,4.420490,-1.546453,-1.643054,-5.908684,1.674951,-7.692507,9.211727,-2.797126,4.856555,4.347582,-4.892308,-4.301203,6.398138,-2.782349,-3.655187,-2.948352,4.362416,2.841733,-0.658127,-0.812177,-0.725795,-3.241596,1.351738,-2.202007,5.766885,-2.003826,-2.278258,8.779085,6.979604,-8.479871,6.308000,1.924044,0.272262,-3.556535,0.268753,-7.237450,7.764928,3.121920,0.916140,-9.767125,7.636160,-3.416426,7.597183,6.644099,7.036381,-8.618075,-7.369981,0.198224,-7.704187,2.326693,2.134697,-4.435524,8.894046,7.487689,0.376294,5.661257,-9.065428,-7.207547,3.049080,7.888077,-6.774211,0.499545,9.351929,-3.060538,-2.986895,5.755341,3.073729,7.733787,3.465652,6.055939,-3.784095,7.840035,-0.847191,-2.754634,7.748806,-4.000187,0.531794,-7.787727,5.141247,0.320569,7.604680,4.727904,-8.701729,5.081204,9.433470,-9.486817,9.317626,-1.662904,0.756382,4.561896,-1.664687,-1.809006,-2.876660], dtype = "float32")#candidate|4636|(150,)|const|float32
call_4633 = relay.TupleGetItem(func_1678_call(relay.reshape(const_4634.astype('uint8'), []), relay.reshape(var_4635.astype('uint8'), [6, 2, 6]), relay.reshape(const_4636.astype('float32'), [150,]), ), 0)
call_4637 = relay.TupleGetItem(func_1682_call(relay.reshape(const_4634.astype('uint8'), []), relay.reshape(var_4635.astype('uint8'), [6, 2, 6]), relay.reshape(const_4636.astype('float32'), [150,]), ), 0)
func_3055_call = mod.get_global_var('func_3055')
func_3059_call = mutated_mod.get_global_var('func_3059')
const_4643 = relay.const([6.324872,9.386966,-0.029370,-7.548662,8.719530,9.938958,-2.256480,9.111488,-3.587491,9.734557,-6.974350,-0.445870,-0.056047,-9.227924,-7.544486,0.669309,-6.666587,0.989785,-0.301003,3.391491,-0.353155,1.844990,6.800640,2.342524,6.440501,-0.338007,-3.943491,-1.035503,-0.375560,-6.648068,3.504778,-6.904023,-4.608989,-4.132560,4.558528,-5.913063,-5.931832,-4.997518,9.368423,-6.185924,-4.021100,-7.391174,2.276817,-2.416446,7.577713,-5.473877,-9.352319,-7.847988,-3.084727,4.549742,4.372646,2.809245,2.977215,5.235261,3.687845,2.637548,-5.816684,-5.734123,-5.775256,5.557001,-2.839386,-6.620010,-6.555231,2.616715,-3.909519,-4.986652,4.421619,0.224894,-0.601579,7.859540,-0.441088,7.790953,-5.491211,8.711570,-4.868109,2.644030,-3.503478,6.949484,-7.983962,-2.278844,7.248907,-8.393100,-4.536152,7.864970,-3.441001,8.109581,7.607420,-5.644034,-5.142279,-5.681451,-5.636519,1.810011,-0.434633,-2.617557,-6.621855,1.109463,1.614116,-3.304550,3.215146,-9.698199,-9.625626,8.206589,6.286547,7.548852,4.791672,-6.882065,5.604244,-9.984173,2.859157,4.291923,4.862732,5.616149,-0.181299,5.662344,-8.335199,-8.294026,7.020339,-3.682318,1.693722,-8.427051,-4.994746,-1.340053,1.527620,4.958924,4.196274,-1.819212,0.949000,-7.369477,2.274447,0.061103,4.886696,-5.681081,8.121650,3.679513,-5.660139,1.888084,1.052624,8.763140,9.035458,7.389055,5.105360,6.987985,6.615365,-7.326828,9.931092,-2.771672,3.196478,9.222898,-2.235157,6.709644,9.262565,1.695789,0.816307,0.129193,9.402247,4.622999,-6.526447,2.682839,-9.793542,-7.236855,3.483444,7.873911,0.412321,-8.110692,5.035349,-9.516057,-1.008282,6.221108,-1.075255,-8.950276,6.416008,-5.229003,9.290784,-1.345915,-8.259030,1.960943,1.646948,-7.456052,-4.755688,-2.013897,9.151818,-5.385865,-7.995766,6.081244,-4.851629,-7.892503,5.389457,1.285720,-5.022597,4.669979,-7.585894,2.395629,8.478186,-7.490290,-7.617113,3.332805,0.098201,3.458807,-4.553120,1.940475,5.355925,-3.512728,-9.349450,3.329105,0.303652,5.068701,5.283021,-5.693392,4.602157,-4.016928,4.214668,9.903256,8.523011,6.238924,2.985476,-0.168139,-4.969484,4.477248,-0.041197,-9.513860,1.096990,2.963281,-4.472833,4.475839,-6.883085,5.737238,-7.640295,7.377596,2.748622,3.096089,3.007269,9.052638,-5.415953,-5.062186,9.574114,6.685631,9.737991,-5.128816,-5.647303,3.057489], dtype = "float32")#candidate|4643|(240,)|const|float32
const_4644 = relay.const([[True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,True,False,False,False,True]], dtype = "bool")#candidate|4644|(1, 208)|const|bool
call_4642 = relay.TupleGetItem(func_3055_call(relay.reshape(const_4634.astype('float32'), []), relay.reshape(const_4643.astype('float32'), [2, 8, 15]), relay.reshape(const_4644.astype('bool'), [2, 104]), ), 1)
call_4645 = relay.TupleGetItem(func_3059_call(relay.reshape(const_4634.astype('float32'), []), relay.reshape(const_4643.astype('float32'), [2, 8, 15]), relay.reshape(const_4644.astype('bool'), [2, 104]), ), 1)
uop_4652 = relay.sigmoid(uop_4618.astype('float64')) # shape=(3, 11, 14)
uop_4656 = relay.atanh(uop_4652.astype('float64')) # shape=(3, 11, 14)
output = relay.Tuple([call_4633,const_4634,var_4635,const_4636,call_4642,const_4643,const_4644,uop_4656,])
output2 = relay.Tuple([call_4637,const_4634,var_4635,const_4636,call_4645,const_4643,const_4644,uop_4656,])
func_4669 = relay.Function([var_4635,], output)
mod['func_4669'] = func_4669
mod = relay.transform.InferType()(mod)
mutated_mod['func_4669'] = func_4669
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4670 = relay.var("var_4670", dtype = "uint8", shape = (72,))#candidate|4670|(72,)|var|uint8
func_4669_call = mutated_mod.get_global_var('func_4669')
call_4671 = func_4669_call(var_4670)
output = call_4671
func_4672 = relay.Function([var_4670], output)
mutated_mod['func_4672'] = func_4672
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5050 = relay.const([[[-5.289350,-7.480173,6.555727],[-5.966376,4.967002,-3.394621]]], dtype = "float64")#candidate|5050|(1, 2, 3)|const|float64
uop_5051 = relay.erf(const_5050.astype('float64')) # shape=(1, 2, 3)
func_2800_call = mod.get_global_var('func_2800')
func_2805_call = mutated_mod.get_global_var('func_2805')
const_5066 = relay.const([-1,8,-10,9,6,-9,-5,-2,2,-2,2,-1,4,-10,-3,9,10,7,8,7,-6,-9,-5,7,-5,-6,-2,4,10,-8,7,-6,-5,-8,9,-8,-2,-5,8,-8,10,1,-10,-10,9,3,7,2,2,-6,-5,-5,9,-6,3,-9,-8,7,-7,10,4,1,-3,-3,5,6,-2,-7,-3,10,-6,1,3,-4,4,6,7,7,-2,-5,-10,7,1,6,6,2,-7,8,2,8,-5,-3,-2,4,-3,-3,9,-6,3,-4,8,-4,2,6,-1,-1,-9,-1,-5,6,-4,-2,6,-3,9,-1,5,3,7,-5,-4,-7,9,5,-4,3,-8,1,2,-7,1,-10,-5,-6,-2,1,7,10,-5,-3,6,7,8,9,9,-1,-4,-9,-5,9,7,-5,7,2,2,3,1,9,-9,1,4,10,-4,7,5,-7,8,-7,-9,1,6,7,-5,9,7,-3,2,9,2,5,1,-10,-6,-4,-9,6,8,-3,2,-8,-1,-9,2,-1,1,-4,2,1,-4,-4,-1,-8,-4,3,-2,4,-2,8,-1,10,7,-6,9,-6,6,6,10,8,5,-1,-4,2,-10,-10,1,4,-6,-8,2,8,6,5,7,2,-5,-9,-10,5,-3,-2,6,2,-8,9,-6,8,-2,-8,8,-1,2,4,-2,1,-3,-10,1,-3,4,-1,-8,4,3,8,-1,4,10,-5,-6,-10,1,8,-3,3,2,2,2,-1,-8,-6,-10,2,8,-4,6,-3,-3,-3,3,-6,9,-6,-1,-7,8,8,4,7,7,-8], dtype = "uint16")#candidate|5066|(300,)|const|uint16
const_5067 = relay.const(-1, dtype = "uint8")#candidate|5067|()|const|uint8
var_5068 = relay.var("var_5068", dtype = "float32", shape = (1, 150))#candidate|5068|(1, 150)|var|float32
call_5065 = relay.TupleGetItem(func_2800_call(relay.reshape(const_5066.astype('uint16'), [15, 2, 10]), relay.reshape(const_5067.astype('uint8'), []), relay.reshape(var_5068.astype('float32'), [75, 2]), ), 4)
call_5069 = relay.TupleGetItem(func_2805_call(relay.reshape(const_5066.astype('uint16'), [15, 2, 10]), relay.reshape(const_5067.astype('uint8'), []), relay.reshape(var_5068.astype('float32'), [75, 2]), ), 4)
const_5072 = relay.const([[[9.411887,-4.670207,-2.508655],[0.416115,4.172303,9.945207]],[[-6.996881,4.434072,-2.268169],[1.656095,8.574047,-1.696884]],[[-0.647821,-0.411154,-9.368728],[0.604102,-6.715743,-9.997563]],[[-5.486334,5.341831,6.248921],[8.554455,-4.167614,-1.680584]],[[0.183112,-0.206052,3.275066],[-8.910091,1.489392,-2.441721]],[[-1.112418,0.101172,-6.698254],[-0.731448,8.742637,-9.075193]],[[-9.264161,-4.241078,-4.064538],[1.836948,8.395256,-9.453154]],[[3.856361,-8.861190,-1.692287],[-2.345366,1.936563,3.555983]]], dtype = "float64")#candidate|5072|(8, 2, 3)|const|float64
bop_5073 = relay.multiply(const_5050.astype('uint16'), const_5072.astype('uint16')) # shape=(8, 2, 3)
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
var_5078 = relay.var("var_5078", dtype = "uint8", shape = (18, 4))#candidate|5078|(18, 4)|var|uint8
call_5077 = relay.TupleGetItem(func_1678_call(relay.reshape(const_5067.astype('uint8'), []), relay.reshape(var_5078.astype('uint8'), [6, 2, 6]), relay.reshape(call_5065.astype('float32'), [150,]), ), 2)
call_5079 = relay.TupleGetItem(func_1682_call(relay.reshape(const_5067.astype('uint8'), []), relay.reshape(var_5078.astype('uint8'), [6, 2, 6]), relay.reshape(call_5065.astype('float32'), [150,]), ), 2)
func_2685_call = mod.get_global_var('func_2685')
func_2690_call = mutated_mod.get_global_var('func_2690')
const_5090 = relay.const([-9.216699,7.629594,-1.346318,0.380350,-8.668832,-8.832964,-9.698882,4.732719,2.245132,-1.095400,-3.830387,-5.530282,-0.401854,3.562966,3.287427,-3.809214,-6.046958,7.759589,3.222237,-9.304725,2.655186,-1.036942,0.462071,3.886913,2.149553,-8.432783,0.170073,-6.969519,-7.158405,8.653354,5.000378,-4.176000,0.316599,-8.278865,-8.049422,5.479998,3.628310,4.699848,0.889590,-2.478966,-5.259000,4.815694,0.711331,-4.625256,9.251454,5.198065,4.529938,-0.435081,5.375616,8.147794,9.653026,-0.448819,2.490219,-3.043798,-1.598352,3.062478,2.795404,-7.280320,-4.297142,4.647196,-1.652240,-6.739866,-3.230669,2.419039,0.345899,7.274139,7.556717,-6.134470,9.630662,8.947335,1.243275,-5.344498,9.172135,0.001620,5.511577,3.107830,4.579127,4.308938,-3.905193,-3.131070,-2.229900,2.392254,1.850167,-4.021649,-9.576514,-7.312703,-6.796943,-8.893996,-4.851191,1.535144,-0.406026,0.396906,7.596460,9.018441,7.157238,9.743171,7.568287,2.995456,-4.905823,8.803541,-5.383572,-9.613118,4.138718,-5.012215,-4.584017,6.251423,9.623414,6.995819,-4.444217,-3.149568,-9.488493,1.408981,-8.639149,-3.225339,-9.287274,7.538469,6.257691,5.990422,0.871413,-3.080689,1.356960,-7.715835,5.091124,1.332226,3.842761,8.550697,-6.495563,0.175288,-5.738487,8.218312,-2.802575,2.438944,1.835666,-8.609008,-4.113413,-7.277973,-7.602361,-2.417472,-3.962501,5.602268,-3.389841,5.679711,3.393266,1.331666,-5.506163,-9.005731,-6.292588,7.947469,-2.652850,-7.212256,-1.915652,5.548703,6.404698,-0.812824,5.127071,6.997547,5.863501,-7.525412,-1.853599,-5.120274,1.248549,5.967075,-1.799517,8.041201,-8.847423,2.457181,-3.168850,5.113585,2.804902,-4.376060,-9.412467,-1.544432,-7.299737,-3.868974,-0.650635,-4.692811,-4.138960,1.420818,-1.033470,2.516529,-8.062680,4.647654,0.165694,8.504051,7.099058,-1.928193,9.397011,6.767425,0.200456,-5.745484,-0.047186,2.138325,-5.022224,8.184937,8.747770,4.350229,5.631777,2.223264,-0.591085,7.191844,-0.251009,8.249443,-8.415821,5.688842,-7.943557,-2.659463,-5.727403,0.451692,-7.967157,1.528231,-9.412646,-8.060974,-3.833208,-4.638399,-2.702444,-7.052612,2.114054,-1.207688,-7.656366,-4.997973,-1.281754,3.131318,-5.442513,1.115334,4.633261,2.687446,-2.860698,7.094562,8.545784,8.527403,-8.432958,-8.238088,4.997468,6.489590,-8.317919,-8.741399,-3.449532,-9.844265,7.692912,-5.199182,-6.634731,-2.326539,0.516865,5.006160,8.786422,-1.050990,-4.653684,-8.923097,7.957845,6.768784,7.784124,-7.757127,1.688918,-8.412680,1.567745,6.814514,-4.375896,-5.955632,-2.628642,-3.421839,-8.426424,5.850323,3.334765,-1.110771,1.914073,0.131573,2.960562,2.771341,-0.589088,4.823019,-9.474320,3.848649,-2.221636,-1.794715,-7.481381,1.594689,3.967818,7.883845,-1.744201,7.276381,-3.139988,-4.594034,9.455070,-4.464168,1.536665,0.333884,9.149771,9.192356,-9.747409,-3.835505,-9.882749,9.358374,-0.907685,0.285513,-8.372739,-5.601528,3.061230,-9.471340,-9.540417,-0.747555,3.943381,6.470040,-4.456689,-9.266667,-9.844780,5.128466,-9.539424,-8.156985,-7.530290,3.508612,3.730313,9.367820,-0.818550,0.110639,-3.781428,5.205735,4.219944,-2.870928,3.460031,-0.928703,3.248279,-3.138499,-8.124544,-3.716613,-1.591677,3.130753,-8.110872,-6.489487,-7.303673,3.586096,0.781652,-0.044408,-6.301183,7.912812,-0.433757,7.050235,1.136723,0.662085,9.772636,-4.603187,-5.000989,5.641570,-5.718308,4.844867,1.543770,-1.899012,8.818861,1.266409,0.609007,8.397024,-3.652595,-2.924841,9.363494,2.651255,5.163924,-1.750407,6.143514,-8.922920,-2.783604,-7.871701,5.023732,-6.426093,-6.689922,-8.216014,-1.123288,0.644390,-6.213963,3.357769,1.273182,-4.432256,-4.441387,-2.857640,-6.206921,-6.421320,2.215513,-1.269698,2.831819,9.490199,-5.773954,5.737901,-2.954425,4.600082,-0.928565,-0.387907,2.508743,5.265617,5.732832,9.901509,-2.531081,-1.636478,9.995377,-6.473940,-8.793350,-9.964463,8.713759,2.231909,-1.432781,1.671644,4.946950,-1.864665,-0.194746,0.557816,-2.481412,-0.388786,-9.527390,-8.498729,7.039559,-6.659773,-2.998870,5.796284,-7.433456,2.648965,6.989789,-6.922125,-1.559826,-9.777292,-7.493904,5.856078,-0.322442,4.456500,-6.943698,-8.950192,9.912693,3.156420,8.151458,8.152689,-5.471832,-0.343715,2.529590,-6.855654,-1.388738,8.945231,-6.351441,0.012064,-3.030333,0.489479,-5.328004,-9.480282,-8.449519,1.438306,-0.008400,-0.492489,-8.986671,8.255043,8.967748,3.793980,-7.640596,-3.198005,2.275304,1.060464,-7.244451,9.198461,8.672151,-2.277338,2.527443,2.808751,4.613631,-9.396629,6.822901,6.778894,-8.656078,-0.285560,6.711675,3.255684,-0.981721,-9.164143,-4.089992,4.479085,-4.255982,2.328433,6.705817,1.306655,-9.162266,-3.486580,0.172500,-1.637034,9.861714,-0.284005,1.568828,3.923429,4.083521,9.804822,5.792047,1.771370,-8.267673,-4.321894,3.896018,-7.743148,6.337226,1.339936,3.669264,-9.092929,-8.805226,6.002666,9.498395,4.176286,5.210218,-8.788194,4.245786,-4.763404,-8.898953,-1.774762,-8.593192,-5.241229,1.649914,1.357964,4.654318,7.144531,-2.918547,-1.018191,-2.545470,-5.329615,-8.288078,-2.598132,-6.611752,1.325857,4.754216,1.425684,6.059961,-9.289924,1.076441,4.029833,9.991035,2.445971,5.997689,1.961678,5.051073,8.880069,-7.343517,-1.471830,-2.062703,-9.364435,1.577649,-5.720420,5.390372,5.884041,-4.567147,9.111961,-1.188156,2.498592,-9.664295,9.699554,5.622961,1.484598,-4.051410,-3.835856,-8.820238,7.290552,-5.526142,-2.244355,-3.899537,9.645309,-6.047918,-8.327529,2.259602,-4.509555,0.192987,4.574461,9.460745,-9.176878,-5.745902,-8.044974,9.365008,-6.069276,0.503637,7.120176,3.751106,-6.339856,-0.866696,-3.256488,9.660605,7.216312,-8.317165,5.275323,-5.869409,0.696665,-9.554199,9.328948,6.403745,-7.980204,-7.201501,-2.769645,-5.685596,5.065659,-3.835724,-9.168566,-1.302420,-1.700744,-4.117003,-1.253935,7.234342,-8.704142,-2.610587,-4.320778,0.663356,-6.147176,-8.105954,2.718517,-5.114417,9.095409,-1.554106,-0.866337,-7.082870,5.200663,-5.724741,7.910634,-1.766525,9.587515,6.650565,-4.056621,-1.025396,-8.834214,-7.724212,5.905351,-0.442105,2.017715,-0.055434,6.268780,-8.013067,-4.362229,2.062554,-1.595583,7.857413,-7.588441,7.855454,2.344444,9.583569,4.091341,-9.549998,-6.629739,0.843538,8.371864,3.124685,-0.674294,-2.690912,-3.926728,-2.310953,7.429251,6.377482,-8.876453,-0.923914,-8.522631,7.743526,1.115410,0.465833,-8.724979,6.762583,-0.690943,1.408773,-9.382406,9.438675,3.778085,-6.768081,2.615496,-1.200480,-3.957623,-7.531419,-5.280481,-0.362805,7.381214,-1.875814,3.090080,4.446501,-6.331802,-8.019521,-1.750108,-1.736077,-5.257592,-2.703635,-5.169746,6.558144,-1.346159,2.721409,-0.983769,-3.221875,5.321931,6.231329,1.518934,6.726700,1.065269,-6.701651,7.356035,9.818357,0.262542,-8.385940,-0.928255,6.637185,0.642668,-2.659520,-6.443340,8.409763,8.953736,-6.638138,5.439183,-8.237898,-0.750273,5.255266,0.450638,6.166989,-1.272704,-9.502571,9.212166,7.716100,3.203687,-5.447357,7.273333,5.728838,2.833293,6.194963,1.346187,6.728481,-0.235424,-9.515678,-6.319718,7.880104,8.582319,4.690808,6.717152,6.572661,-9.511863], dtype = "float32")#candidate|5090|(720,)|const|float32
call_5089 = relay.TupleGetItem(func_2685_call(relay.reshape(const_5090.astype('float32'), [12, 10, 6]), relay.reshape(const_5067.astype('uint8'), []), relay.reshape(var_5078.astype('uint8'), [72,]), ), 3)
call_5091 = relay.TupleGetItem(func_2690_call(relay.reshape(const_5090.astype('float32'), [12, 10, 6]), relay.reshape(const_5067.astype('uint8'), []), relay.reshape(var_5078.astype('uint8'), [72,]), ), 3)
func_2525_call = mod.get_global_var('func_2525')
func_2528_call = mutated_mod.get_global_var('func_2528')
var_5093 = relay.var("var_5093", dtype = "float32", shape = (245,))#candidate|5093|(245,)|var|float32
call_5092 = relay.TupleGetItem(func_2525_call(relay.reshape(var_5093.astype('float32'), [5, 7, 7])), 0)
call_5094 = relay.TupleGetItem(func_2528_call(relay.reshape(var_5093.astype('float32'), [5, 7, 7])), 0)
output = relay.Tuple([uop_5051,call_5065,const_5066,const_5067,var_5068,bop_5073,call_5077,var_5078,call_5089,const_5090,call_5092,var_5093,])
output2 = relay.Tuple([uop_5051,call_5069,const_5066,const_5067,var_5068,bop_5073,call_5079,var_5078,call_5091,const_5090,call_5094,var_5093,])
func_5100 = relay.Function([var_5068,var_5078,var_5093,], output)
mod['func_5100'] = func_5100
mod = relay.transform.InferType()(mod)
var_5101 = relay.var("var_5101", dtype = "float32", shape = (1, 150))#candidate|5101|(1, 150)|var|float32
var_5102 = relay.var("var_5102", dtype = "uint8", shape = (18, 4))#candidate|5102|(18, 4)|var|uint8
var_5103 = relay.var("var_5103", dtype = "float32", shape = (245,))#candidate|5103|(245,)|var|float32
output = func_5100(var_5101,var_5102,var_5103,)
func_5104 = relay.Function([var_5101,var_5102,var_5103,], output)
mutated_mod['func_5104'] = func_5104
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5119 = relay.var("var_5119", dtype = "int32", shape = (4, 14, 13))#candidate|5119|(4, 14, 13)|var|int32
const_5120 = relay.const([[[8,-7,-8,2,8,5,-8,-9,-9,-3,10,-9,-2],[3,6,1,7,-3,-4,5,2,-3,-6,5,7,2],[-7,-10,-8,8,-8,8,-6,10,-9,-1,-7,-3,1],[10,7,5,-5,-6,7,8,4,3,-10,-9,-10,-2],[-9,1,3,7,-3,8,9,-2,-10,2,-8,-4,-7],[-9,-7,5,-6,-5,-8,-10,9,1,-4,2,5,7],[-10,4,-6,-8,2,7,10,6,8,-10,-8,5,-6],[-5,3,-4,5,-2,-3,-1,4,2,4,1,-7,-1],[2,6,-2,-8,-5,8,4,-8,-2,1,-9,-9,2],[4,-3,-4,-8,-4,3,5,-6,-7,-7,-7,-6,-5],[1,9,-6,-3,-8,7,-9,-8,4,-2,10,-3,6],[6,-6,8,-4,1,10,2,-2,7,9,8,1,-6],[-1,6,8,-3,2,2,-8,8,6,7,-9,1,-10],[-3,-9,1,-9,9,-10,10,4,10,4,2,-9,7]],[[-5,-10,-5,5,-4,-6,-7,8,7,-9,-9,-3,-10],[2,3,-9,-6,-3,-2,9,-7,8,-9,-1,-4,7],[3,8,-4,3,8,8,-1,-8,-1,8,9,-4,-2],[-5,7,-10,2,4,-8,3,-6,-1,2,-9,-4,3],[-5,-4,-3,-1,-2,1,-1,-10,-1,-5,4,6,-5],[8,-4,-7,-7,-3,-1,-1,7,7,-10,-9,9,-7],[-1,-8,-8,8,-9,-10,-7,9,7,-2,-5,-4,-7],[-5,8,9,7,-8,8,-8,2,-5,10,6,5,6],[7,4,-5,-10,1,2,1,-2,7,-5,-7,-7,-4],[6,3,9,2,-3,2,-9,7,10,1,-6,-1,9],[-3,3,-1,9,1,-3,-3,7,4,-8,-7,-8,10],[9,6,9,4,9,3,9,-5,-4,-9,-4,6,3],[-2,-6,-6,6,-2,-5,7,4,-9,-1,-5,3,-7],[-6,-2,-8,1,-9,-8,-1,7,1,-10,-3,7,-3]],[[10,-6,-4,-2,3,-1,4,1,2,-6,-10,5,3],[-8,4,5,-7,1,-5,-8,-2,3,6,2,10,8],[-5,9,-3,-10,-8,10,-6,-9,-5,9,5,-5,-10],[10,5,9,3,7,4,-2,2,10,-5,9,5,7],[-4,10,9,1,9,3,-7,-9,-8,5,-5,8,-1],[9,-6,5,-9,1,6,2,-3,9,-5,-1,9,5],[-1,1,-9,-10,-9,5,10,5,-10,-9,-10,-3,7],[10,-1,8,-7,6,3,2,-8,9,-5,-2,-1,-7],[1,8,5,-4,2,-8,4,4,7,9,-5,3,-3],[4,-8,-7,-3,7,-4,4,-6,2,6,9,-3,1],[5,5,-9,-1,2,-5,4,2,-6,3,-9,-4,-2],[10,-9,1,-3,1,-7,-8,-2,-5,7,-6,4,-5],[-4,-9,1,-10,-8,-6,1,-4,4,9,-7,6,-2],[8,-2,8,-3,-10,6,-9,-3,9,6,4,7,8]],[[8,9,6,5,-2,2,1,4,-4,-4,-9,2,-6],[7,-10,9,-9,-7,8,3,-4,-9,-8,2,7,-10],[-7,-4,-1,-6,6,-6,-6,9,4,7,-8,-2,-9],[-10,-10,-3,-5,2,7,-6,7,-7,-6,8,10,-7],[-2,-7,-5,7,9,6,10,9,-8,-10,8,8,8],[1,1,-8,-1,4,-2,-3,5,-5,9,-2,-1,-2],[2,1,7,-7,4,-1,-10,10,10,-3,7,1,3],[3,-6,1,8,-9,7,-3,-1,5,3,-7,3,9],[-9,-5,2,4,-4,9,10,5,1,-8,6,8,-1],[2,5,3,2,6,-4,5,9,10,-9,7,-4,-6],[8,-10,9,2,-7,-7,1,-4,-4,-4,2,-2,-8],[-3,-2,3,-3,1,-8,3,8,-4,-3,-5,-7,2],[1,-10,-1,-3,2,-4,-10,-4,-8,2,8,4,-4],[10,7,1,-4,-1,6,9,-10,10,10,8,2,5]]], dtype = "int32")#candidate|5120|(4, 14, 13)|const|int32
bop_5121 = relay.less(var_5119.astype('bool'), relay.reshape(const_5120.astype('bool'), relay.shape_of(var_5119))) # shape=(4, 14, 13)
func_579_call = mod.get_global_var('func_579')
func_582_call = mutated_mod.get_global_var('func_582')
var_5130 = relay.var("var_5130", dtype = "float32", shape = (25, 6))#candidate|5130|(25, 6)|var|float32
call_5129 = func_579_call(relay.reshape(var_5130.astype('float32'), [10, 15, 1]))
call_5131 = func_579_call(relay.reshape(var_5130.astype('float32'), [10, 15, 1]))
output = relay.Tuple([bop_5121,call_5129,var_5130,])
output2 = relay.Tuple([bop_5121,call_5131,var_5130,])
func_5133 = relay.Function([var_5119,var_5130,], output)
mod['func_5133'] = func_5133
mod = relay.transform.InferType()(mod)
mutated_mod['func_5133'] = func_5133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5133_call = mutated_mod.get_global_var('func_5133')
var_5135 = relay.var("var_5135", dtype = "int32", shape = (4, 14, 13))#candidate|5135|(4, 14, 13)|var|int32
var_5136 = relay.var("var_5136", dtype = "float32", shape = (25, 6))#candidate|5136|(25, 6)|var|float32
call_5134 = func_5133_call(var_5135,var_5136,)
output = call_5134
func_5137 = relay.Function([var_5135,var_5136,], output)
mutated_mod['func_5137'] = func_5137
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5313 = relay.var("var_5313", dtype = "float64", shape = (9, 3, 8))#candidate|5313|(9, 3, 8)|var|float64
uop_5314 = relay.sqrt(var_5313.astype('float64')) # shape=(9, 3, 8)
func_2982_call = mod.get_global_var('func_2982')
func_2988_call = mutated_mod.get_global_var('func_2988')
var_5317 = relay.var("var_5317", dtype = "float32", shape = (36,))#candidate|5317|(36,)|var|float32
var_5318 = relay.var("var_5318", dtype = "bool", shape = (208,))#candidate|5318|(208,)|var|bool
const_5319 = relay.const([5,-7,10,9,3,-2,8,5,3,-1,-7,-7,5,-4,3,4,-5,-3,9,10,-4,8,-10,7,4,-4,-7,3,6,-9,-5,7,5,5,-9,-5,9,4,6,-1,-1,3,-9,-10,-6,-1,3,8,-7,-2,-10,-1,2,-8,-9,1,7,8,2,8,8,-6,-9,-10,9,-7,1,-10,3,1,9,2], dtype = "uint8")#candidate|5319|(72,)|const|uint8
var_5320 = relay.var("var_5320", dtype = "uint8", shape = ())#candidate|5320|()|var|uint8
call_5316 = relay.TupleGetItem(func_2982_call(relay.reshape(var_5317.astype('float32'), [2, 9, 2]), relay.reshape(var_5317.astype('float32'), [2, 9, 2]), relay.reshape(var_5318.astype('bool'), [208,]), relay.reshape(const_5319.astype('uint8'), [36, 2]), relay.reshape(var_5320.astype('uint8'), []), ), 5)
call_5321 = relay.TupleGetItem(func_2988_call(relay.reshape(var_5317.astype('float32'), [2, 9, 2]), relay.reshape(var_5317.astype('float32'), [2, 9, 2]), relay.reshape(var_5318.astype('bool'), [208,]), relay.reshape(const_5319.astype('uint8'), [36, 2]), relay.reshape(var_5320.astype('uint8'), []), ), 5)
output = relay.Tuple([uop_5314,call_5316,var_5317,var_5318,const_5319,var_5320,])
output2 = relay.Tuple([uop_5314,call_5321,var_5317,var_5318,const_5319,var_5320,])
func_5331 = relay.Function([var_5313,var_5317,var_5318,var_5320,], output)
mod['func_5331'] = func_5331
mod = relay.transform.InferType()(mod)
mutated_mod['func_5331'] = func_5331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5331_call = mutated_mod.get_global_var('func_5331')
var_5333 = relay.var("var_5333", dtype = "float64", shape = (9, 3, 8))#candidate|5333|(9, 3, 8)|var|float64
var_5334 = relay.var("var_5334", dtype = "float32", shape = (36,))#candidate|5334|(36,)|var|float32
var_5335 = relay.var("var_5335", dtype = "bool", shape = (208,))#candidate|5335|(208,)|var|bool
var_5336 = relay.var("var_5336", dtype = "uint8", shape = ())#candidate|5336|()|var|uint8
call_5332 = func_5331_call(var_5333,var_5334,var_5335,var_5336,)
output = call_5332
func_5337 = relay.Function([var_5333,var_5334,var_5335,var_5336,], output)
mutated_mod['func_5337'] = func_5337
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5673 = relay.var("var_5673", dtype = "float64", shape = (11, 8, 5))#candidate|5673|(11, 8, 5)|var|float64
uop_5674 = relay.asin(var_5673.astype('float64')) # shape=(11, 8, 5)
func_4669_call = mod.get_global_var('func_4669')
func_4672_call = mutated_mod.get_global_var('func_4672')
const_5685 = relay.const([4,8,9,-6,-8,-3,7,6,8,-5,-5,8,-1,2,5,-6,-9,2,4,3,1,1,-10,7,-8,-2,-3,10,-9,3,-4,-2,7,-1,4,-5,3,-4,10,1,-2,-4,3,6,-6,7,-1,-3,5,-9,7,5,-7,-1,8,8,4,6,6,3,-2,2,-1,4,-8,-6,-7,6,-10,5,-10,-10], dtype = "uint8")#candidate|5685|(72,)|const|uint8
call_5684 = relay.TupleGetItem(func_4669_call(relay.reshape(const_5685.astype('uint8'), [72,])), 7)
call_5686 = relay.TupleGetItem(func_4672_call(relay.reshape(const_5685.astype('uint8'), [72,])), 7)
func_2685_call = mod.get_global_var('func_2685')
func_2690_call = mutated_mod.get_global_var('func_2690')
var_5696 = relay.var("var_5696", dtype = "float32", shape = (720,))#candidate|5696|(720,)|var|float32
var_5697 = relay.var("var_5697", dtype = "uint8", shape = ())#candidate|5697|()|var|uint8
call_5695 = relay.TupleGetItem(func_2685_call(relay.reshape(var_5696.astype('float32'), [12, 10, 6]), relay.reshape(var_5697.astype('uint8'), []), relay.reshape(const_5685.astype('uint8'), [72,]), ), 1)
call_5698 = relay.TupleGetItem(func_2690_call(relay.reshape(var_5696.astype('float32'), [12, 10, 6]), relay.reshape(var_5697.astype('uint8'), []), relay.reshape(const_5685.astype('uint8'), [72,]), ), 1)
func_5100_call = mod.get_global_var('func_5100')
func_5104_call = mutated_mod.get_global_var('func_5104')
const_5704 = relay.const([-6.779063,9.373740,-3.487849,-3.871717,6.686538,-4.041120,6.084163,2.433762,0.451226,1.677892,-9.902231,-7.311171,2.135338,-0.656372,8.624742,-5.749647,5.735916,8.370841,2.802406,-4.117982,1.357556,7.190075,9.960131,8.174013,4.318513,-9.214784,-2.122086,-7.488213,-8.973938,-1.798541,7.594966,0.559533,6.891655,7.056089,8.608245,5.095208,-5.929004,6.918564,6.556316,-1.008093,-5.567912,9.461005,7.288817,-0.293937,-9.996138,5.772975,4.290543,-2.322205,3.710372,3.336325,-7.626663,9.235266,0.339414,-0.312833,4.146898,4.258583,0.521337,5.921302,-0.001747,-0.680199,-6.882473,3.670945,5.538765,-2.850424,3.620625,1.413510,5.505310,-5.221845,6.655013,3.011378,3.142167,-0.750376,6.001248,9.335092,2.580117,9.635893,2.702423,-8.455361,-1.696839,-7.249172,-3.117093,9.545030,-3.028429,9.536558,-5.223629,5.497720,5.450537,4.199487,7.268009,9.427189,-3.696524,-7.303495,1.108904,-4.687705,-6.289748,8.316770,-6.897011,-9.062753,-6.622018,1.927829,-8.438630,-6.313983,-4.928986,7.391354,-4.149824,3.333575,7.256778,-7.047232,-2.017575,-8.188035,9.178047,6.061749,4.751718,1.163724,7.585136,-4.664863,1.028743,-2.973239,-7.347309,2.323582,-8.012758,-8.636250,-2.485203,-9.006169,8.711651,0.148381,-0.550619,8.094549,-0.720451,3.318015,7.061300,-4.175417,-1.152095,-0.023050,-4.520728,0.209119,-2.264816,-9.283886,-4.371365,0.912733,9.804870,7.005034,-9.142108,6.481230,3.100072,-8.694852,6.270515,7.881087,8.625124,-3.647198], dtype = "float32")#candidate|5704|(150,)|const|float32
var_5705 = relay.var("var_5705", dtype = "float32", shape = (245,))#candidate|5705|(245,)|var|float32
call_5703 = relay.TupleGetItem(func_5100_call(relay.reshape(const_5704.astype('float32'), [1, 150]), relay.reshape(const_5685.astype('uint8'), [18, 4]), relay.reshape(var_5705.astype('float32'), [245,]), ), 5)
call_5706 = relay.TupleGetItem(func_5104_call(relay.reshape(const_5704.astype('float32'), [1, 150]), relay.reshape(const_5685.astype('uint8'), [18, 4]), relay.reshape(var_5705.astype('float32'), [245,]), ), 5)
output = relay.Tuple([uop_5674,call_5684,const_5685,call_5695,var_5696,var_5697,call_5703,const_5704,var_5705,])
output2 = relay.Tuple([uop_5674,call_5686,const_5685,call_5698,var_5696,var_5697,call_5706,const_5704,var_5705,])
func_5731 = relay.Function([var_5673,var_5696,var_5697,var_5705,], output)
mod['func_5731'] = func_5731
mod = relay.transform.InferType()(mod)
var_5732 = relay.var("var_5732", dtype = "float64", shape = (11, 8, 5))#candidate|5732|(11, 8, 5)|var|float64
var_5733 = relay.var("var_5733", dtype = "float32", shape = (720,))#candidate|5733|(720,)|var|float32
var_5734 = relay.var("var_5734", dtype = "uint8", shape = ())#candidate|5734|()|var|uint8
var_5735 = relay.var("var_5735", dtype = "float32", shape = (245,))#candidate|5735|(245,)|var|float32
output = func_5731(var_5732,var_5733,var_5734,var_5735,)
func_5736 = relay.Function([var_5732,var_5733,var_5734,var_5735,], output)
mutated_mod['func_5736'] = func_5736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5789 = relay.var("var_5789", dtype = "float64", shape = (8, 11, 6))#candidate|5789|(8, 11, 6)|var|float64
uop_5790 = relay.log(var_5789.astype('float64')) # shape=(8, 11, 6)
func_2525_call = mod.get_global_var('func_2525')
func_2528_call = mutated_mod.get_global_var('func_2528')
const_5807 = relay.const([[-2.220924,-0.074958,-2.252316,-2.976612,7.166071,-8.461092,1.395591,-1.476870,-5.915239,8.041181,1.615247,3.367268,-3.324847,-6.401390,-3.408773,-6.349966,4.513177,8.951704,3.585456,8.012929,-2.606586,-2.714024,-5.672767,-1.314551,1.021274,-5.481695,4.669718,1.001607,8.410408,-0.534172,0.738888,-8.917324,-9.647619,-6.423928,1.124284],[-2.079006,5.818576,2.044600,0.760985,-0.712884,7.899089,3.289135,-9.832282,8.290857,-3.747691,1.990055,-1.423124,-1.388919,9.082499,-5.890694,8.001402,2.242927,0.941275,-4.314670,-2.980597,3.958070,9.878374,-8.025962,-8.698680,3.061694,-0.768516,-2.413264,-1.496167,3.573675,1.466805,3.286621,-3.864898,3.895993,5.244130,-1.874235],[5.431051,-8.114340,-4.519126,-4.372690,-9.780446,9.122864,3.448607,4.051906,2.504956,4.166565,-4.041369,7.160807,9.686023,-6.445666,-8.901641,5.325722,-9.020608,-2.567101,-1.571454,9.068808,8.252470,8.782526,-3.058801,-9.072724,3.042005,-6.351137,-3.771702,-3.671921,9.753453,2.016467,3.691359,8.648134,-7.122989,-2.186130,-2.522023],[4.942910,0.593563,-6.525634,6.027004,3.696469,4.197437,-3.674783,4.314984,5.567570,5.189392,-3.433931,1.135533,-5.718994,3.297489,5.382086,5.685332,4.020478,4.092210,-6.471236,4.678801,-3.795148,-5.363740,-5.794578,1.886610,-4.423506,-1.616620,-2.657715,-3.597825,4.325032,3.226121,5.496345,2.669784,6.146875,1.915311,5.295835],[5.826817,9.508418,-3.612887,8.630376,6.995803,-1.913535,-7.037768,-9.149992,-5.229907,5.822020,-7.178017,-1.560499,2.199834,-5.166642,5.185787,9.706939,1.094185,-5.095486,2.255616,-7.654916,9.443591,-4.740572,1.301609,-5.506004,8.898032,9.626213,1.200045,1.666565,-4.975781,5.591228,-1.171011,-9.929992,4.021370,2.940649,0.432787],[0.764254,8.575406,-9.945807,-9.848047,-0.653854,-0.062787,1.396083,7.517805,7.339347,4.563383,6.280114,1.762430,3.896303,5.564939,7.911503,-8.554245,2.839114,3.600715,-3.171855,4.835742,3.217690,6.835270,6.290910,3.415131,-9.229167,7.723480,-2.072337,1.425668,6.565976,1.939496,2.044202,3.921816,5.253450,2.434376,1.748212],[-5.619706,-3.633736,5.221553,-5.973154,-5.526759,4.242377,-4.781167,7.094646,-4.366748,-4.661707,7.511271,4.966920,1.781016,0.965252,4.341764,6.364643,1.656992,9.238379,2.180612,-9.749814,-2.241531,8.353638,0.064062,-7.143791,8.449538,9.590969,3.757005,5.618088,4.147764,4.206627,4.617805,-3.680885,-8.312507,-7.214004,5.369222]], dtype = "float32")#candidate|5807|(7, 35)|const|float32
call_5806 = relay.TupleGetItem(func_2525_call(relay.reshape(const_5807.astype('float32'), [5, 7, 7])), 0)
call_5808 = relay.TupleGetItem(func_2528_call(relay.reshape(const_5807.astype('float32'), [5, 7, 7])), 0)
func_2525_call = mod.get_global_var('func_2525')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_5818 = relay.TupleGetItem(func_2525_call(relay.reshape(const_5807.astype('float32'), [5, 7, 7])), 0)
call_5819 = relay.TupleGetItem(func_2528_call(relay.reshape(const_5807.astype('float32'), [5, 7, 7])), 0)
output = relay.Tuple([uop_5790,call_5806,const_5807,call_5818,])
output2 = relay.Tuple([uop_5790,call_5808,const_5807,call_5819,])
func_5820 = relay.Function([var_5789,], output)
mod['func_5820'] = func_5820
mod = relay.transform.InferType()(mod)
var_5821 = relay.var("var_5821", dtype = "float64", shape = (8, 11, 6))#candidate|5821|(8, 11, 6)|var|float64
output = func_5820(var_5821)
func_5822 = relay.Function([var_5821], output)
mutated_mod['func_5822'] = func_5822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6075 = relay.var("var_6075", dtype = "float32", shape = (1, 11, 6))#candidate|6075|(1, 11, 6)|var|float32
uop_6076 = relay.erf(var_6075.astype('float32')) # shape=(1, 11, 6)
bop_6081 = relay.floor_mod(uop_6076.astype('float64'), relay.reshape(var_6075.astype('float64'), relay.shape_of(uop_6076))) # shape=(1, 11, 6)
output = relay.Tuple([bop_6081,])
output2 = relay.Tuple([bop_6081,])
func_6087 = relay.Function([var_6075,], output)
mod['func_6087'] = func_6087
mod = relay.transform.InferType()(mod)
mutated_mod['func_6087'] = func_6087
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6088 = relay.var("var_6088", dtype = "float32", shape = (1, 11, 6))#candidate|6088|(1, 11, 6)|var|float32
func_6087_call = mutated_mod.get_global_var('func_6087')
call_6089 = func_6087_call(var_6088)
output = call_6089
func_6090 = relay.Function([var_6088], output)
mutated_mod['func_6090'] = func_6090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6664 = relay.var("var_6664", dtype = "uint32", shape = ())#candidate|6664|()|var|uint32
var_6665 = relay.var("var_6665", dtype = "uint32", shape = (8, 13, 7))#candidate|6665|(8, 13, 7)|var|uint32
bop_6666 = relay.add(var_6664.astype('uint32'), var_6665.astype('uint32')) # shape=(8, 13, 7)
func_5820_call = mod.get_global_var('func_5820')
func_5822_call = mutated_mod.get_global_var('func_5822')
var_6684 = relay.var("var_6684", dtype = "float64", shape = (528,))#candidate|6684|(528,)|var|float64
call_6683 = relay.TupleGetItem(func_5820_call(relay.reshape(var_6684.astype('float64'), [8, 11, 6])), 2)
call_6685 = relay.TupleGetItem(func_5822_call(relay.reshape(var_6684.astype('float64'), [8, 11, 6])), 2)
output = relay.Tuple([bop_6666,call_6683,var_6684,])
output2 = relay.Tuple([bop_6666,call_6685,var_6684,])
func_6693 = relay.Function([var_6664,var_6665,var_6684,], output)
mod['func_6693'] = func_6693
mod = relay.transform.InferType()(mod)
var_6694 = relay.var("var_6694", dtype = "uint32", shape = ())#candidate|6694|()|var|uint32
var_6695 = relay.var("var_6695", dtype = "uint32", shape = (8, 13, 7))#candidate|6695|(8, 13, 7)|var|uint32
var_6696 = relay.var("var_6696", dtype = "float64", shape = (528,))#candidate|6696|(528,)|var|float64
output = func_6693(var_6694,var_6695,var_6696,)
func_6697 = relay.Function([var_6694,var_6695,var_6696,], output)
mutated_mod['func_6697'] = func_6697
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7146 = relay.const([[[-5.536795,-8.224400,-8.346543,-4.013459,-6.498299,8.067044,3.027599,4.249978,6.166305],[5.100107,-4.103256,-5.033528,-2.720111,7.885544,9.384260,-7.587658,-6.198619,-5.904743],[0.862153,4.891605,-4.105038,-4.702882,-8.629571,1.879785,2.358246,-5.170032,2.907496],[-5.412083,4.136163,5.039614,-7.074063,-5.321261,-2.628952,-5.262130,9.332321,0.618325],[-2.203065,-3.887710,-2.321157,-3.363689,-7.049470,9.287680,7.938868,-6.492813,7.612202],[-3.853717,0.487677,-6.116869,8.967551,1.469349,5.597294,5.519830,-9.097092,-1.027752],[1.379841,6.194808,4.529334,4.005937,-0.864371,7.969043,-4.683454,9.646610,4.262443],[1.514848,-8.535246,7.860286,-6.420949,-7.947068,-2.370242,0.680306,6.940348,-2.592383],[6.672935,-2.546036,8.352752,7.561945,6.638123,2.266679,-9.689080,0.787491,3.463038],[-4.282420,6.114245,-1.450313,1.008507,-9.534659,-0.455146,-1.333098,-4.262175,4.737403],[-7.030927,0.580466,-8.168762,-3.585342,-8.225393,0.981048,8.191330,4.671497,-6.087729],[-9.816899,2.323058,8.342540,4.550773,7.780642,-5.110767,4.002586,9.116722,-0.913485],[8.482388,-2.932811,-7.687950,1.649769,-3.681953,8.830631,3.114656,-3.121004,-2.393771]],[[-2.807880,4.614369,3.837147,0.288723,0.366531,-1.155044,-0.467353,-6.291931,6.585851],[-7.445826,-6.758299,3.867450,-0.540198,-1.404745,0.630211,-2.078168,-7.695524,7.644917],[3.415368,6.272752,4.775107,-0.216497,4.705812,-6.294062,8.021104,-8.188124,2.729897],[8.954050,-0.595853,8.820375,-3.199172,7.361075,8.480722,0.683587,3.694988,0.944560],[-1.081374,-2.066087,6.019387,-7.675783,-4.507300,-2.211050,-2.771565,9.375300,1.327437],[-3.546184,-4.693572,9.283860,-1.927786,-2.110728,2.248752,-7.325095,6.148831,1.378225],[7.346379,1.980777,-1.211091,-3.667269,-6.616974,6.312040,-9.556814,5.914448,-6.522842],[-3.888712,3.113949,-9.393301,3.879644,-7.294167,-7.131833,8.820833,5.711340,8.431644],[-3.143132,-4.929730,7.558713,4.731963,9.119430,-5.465792,8.942575,-3.944391,6.487950],[7.120932,1.024634,0.095394,4.927677,-5.365928,7.784953,8.373347,1.482349,-1.904927],[2.434678,-7.895750,5.940743,-6.891822,6.906775,3.113944,-1.125299,8.406272,3.165071],[7.982135,3.859348,8.871937,1.676708,6.615518,7.147005,4.645538,9.492746,8.503783],[-0.959905,0.979875,7.445344,-2.717232,7.530141,2.982589,-2.444538,2.817934,-0.640305]],[[-3.582949,9.723450,-7.053904,-2.921019,-7.949929,7.380963,-1.499774,4.337602,-1.163424],[-3.117233,-4.577455,-3.277464,-2.413712,-9.449016,2.895419,5.315506,-6.914452,1.494395],[9.547163,-4.240732,4.822447,0.111903,3.829737,9.473163,2.039121,-9.785149,9.880406],[-5.374133,8.161720,5.883499,3.111641,8.809194,-8.571786,6.922048,-1.947473,6.969183],[8.857954,9.823876,3.451811,-9.286136,-5.792542,0.085038,-8.648042,-0.057456,-8.575948],[-2.625156,-9.933897,-4.306531,-3.742070,-3.069315,2.570343,-3.065022,-6.239123,-7.715841],[-1.781499,4.675382,1.799199,-7.689755,-5.361084,-9.668970,-3.556816,-7.612540,-8.488062],[9.544538,-3.256803,7.971030,0.948402,4.520011,9.982756,-4.785649,-8.589629,-2.032445],[-9.244725,8.290349,7.138224,0.723898,-5.072500,-8.723072,-9.253458,9.123709,7.831890],[0.481317,-9.357762,1.637509,-3.392242,2.320471,3.659215,-4.142342,-7.859120,-9.853279],[1.860303,-6.573937,0.191438,-7.166030,-0.879433,0.985016,-4.582488,9.389272,1.215278],[-6.953804,-9.517405,-1.762858,-8.205012,7.168064,6.635890,-4.901719,3.191474,-4.826779],[-1.870482,6.809425,1.972350,-7.212606,8.273125,-3.260419,-3.628168,-7.126164,7.434127]],[[-4.167444,4.043600,-8.908457,9.045235,-4.227204,1.638672,-7.614167,6.725183,5.031849],[-2.255655,1.331931,1.871240,-4.246273,-2.498237,-7.268677,7.039034,6.089016,-7.985515],[9.086316,7.507208,-5.778996,7.227021,-2.714583,-0.670764,3.247804,9.458857,-4.569043],[-4.414546,3.799912,3.567762,-9.970649,-7.532371,-6.219897,-5.089091,0.922585,0.495850],[-2.031515,-8.016144,6.427359,-1.280643,0.226233,4.789265,-2.479035,-9.427325,4.254608],[9.576972,-2.903366,0.539043,-8.460869,7.051708,4.611610,-1.915119,0.626436,-3.048171],[4.724504,2.122281,3.317886,0.365253,-8.358939,6.805262,2.308530,-8.823852,-0.273420],[-3.022635,9.428460,-7.446557,-3.121854,-2.635127,1.374556,9.133725,-6.378822,9.576634],[2.536723,5.531351,-8.884050,0.453558,-8.132951,-7.838324,-1.694407,1.593338,-7.345024],[-7.331682,-1.142164,-5.263380,-5.076863,5.581751,-5.272687,-5.752410,7.858749,7.817179],[-3.229504,9.942793,-1.385635,2.541380,8.737824,-4.674603,2.870388,-4.041727,-3.309210],[4.946283,-3.691256,7.812401,-6.974813,8.303379,0.096754,1.829524,9.271609,-4.076049],[-3.704930,-0.073783,6.779521,5.799627,-1.899289,-1.052597,-1.950325,1.367189,-7.542186]],[[7.879309,-2.226630,-1.822529,-5.969788,5.792747,4.005309,5.635899,3.998800,6.722688],[9.850329,6.763507,-8.472468,-6.709549,-5.850445,-3.517219,-1.615225,5.206458,-3.823600],[-2.843231,8.788580,-0.347722,-8.478952,2.293968,-4.051422,-3.932243,7.798792,9.775668],[3.317334,3.451879,6.605681,9.901737,3.709260,-3.328559,-1.451836,-9.600437,-5.245819],[-6.998788,2.696588,-1.206108,-0.350338,0.773117,8.503545,-2.984660,-5.954639,-8.686900],[0.181982,2.070901,-6.567440,-4.689799,-9.695573,-0.242328,1.164574,8.472630,-1.138528],[-8.261528,-0.676738,5.735225,-0.630274,3.520744,2.127055,-7.742374,0.133589,9.625453],[3.178164,-7.015395,6.672030,-8.291153,-3.095838,9.734594,-0.826407,1.680209,4.189922],[-3.602986,-4.929355,-0.597356,7.768041,-5.447911,-0.570706,-4.629047,3.582532,7.344823],[0.697206,-4.806413,-1.594899,4.142875,4.853026,4.420081,5.029347,0.684541,7.969225],[4.754981,-7.149416,4.926563,4.066591,2.022581,3.191147,1.930516,-8.704440,-2.125628],[5.028018,3.294925,-3.791634,1.682078,-4.646607,-1.418541,-1.389621,-1.521463,1.323500],[5.442733,5.622340,-6.957038,-0.688584,-6.749375,5.378055,3.283454,-9.593529,6.101277]],[[5.639917,-4.425164,1.330564,-2.975858,-7.159269,0.230957,-8.765324,-4.849585,3.966020],[-0.826101,0.776336,-3.928789,4.438737,3.747652,5.823052,2.300927,-8.216228,-4.881360],[-2.079283,8.062592,-5.802759,-1.704877,-8.674177,-6.408379,5.880913,2.514252,9.724255],[5.527460,3.798276,-9.973706,-4.940556,6.763285,7.612905,-4.654872,-0.324854,-1.871974],[-5.137273,-4.444366,-1.271615,-8.425183,8.859325,-3.093006,-8.882314,-7.872465,-5.664910],[-0.565299,-4.241757,7.056583,8.862856,4.397469,-3.291637,-0.912335,-5.702559,3.985546],[-4.851719,7.159121,7.390304,-3.845361,1.723003,0.454778,-7.605242,-9.930742,0.360630],[-6.255338,-4.769606,6.311826,-4.538994,1.923312,-5.881629,0.788927,3.751455,-9.453248],[-5.198807,-9.116099,4.617846,9.519247,3.607399,-3.019454,-9.396254,9.657468,-6.627861],[9.526050,3.874783,-5.957402,6.082787,-1.472218,-7.350704,3.542090,5.816195,-0.144470],[5.129884,-2.647484,-9.123253,8.363089,-2.237752,6.224798,1.790154,6.472040,2.896165],[-3.039085,9.667608,0.830596,-7.070889,-7.834462,-3.193640,-1.024760,-7.120011,-6.485177],[-3.768980,8.722185,1.301146,2.623279,0.521828,8.039535,-6.084279,2.671246,-3.045830]],[[7.729076,0.618336,-3.570525,8.940072,5.134798,-9.987496,-6.404062,-1.329818,6.417325],[-6.212992,-4.886650,3.226505,-9.963009,-0.404695,5.059619,0.015054,4.938903,-1.148803],[-4.008029,-8.819467,3.486079,-9.533242,2.530665,-3.870419,-1.964032,-0.989040,-6.823855],[-1.723107,0.550965,7.550478,8.563846,-3.068733,0.430079,-6.803887,-8.301897,-1.771547],[6.184981,7.839471,6.702908,3.208598,-3.239644,-9.040805,8.041086,4.304728,6.257567],[7.380885,4.228292,1.899659,-7.939123,6.425636,5.032971,2.180718,-2.289947,2.401016],[-3.518896,6.718931,-7.430603,8.964017,-4.428819,7.561260,1.637760,-1.916565,-4.967722],[-7.074589,8.533299,7.232767,2.732152,-8.115826,1.289661,8.902315,-2.864430,-3.656016],[-9.976831,5.094862,-4.786084,2.839832,8.597586,5.143973,6.860227,6.919591,5.418894],[0.581839,1.064429,-1.330322,-5.007294,-9.890681,-0.505708,8.167587,-4.842907,3.545328],[3.815605,0.584109,-0.550815,-0.230074,-5.572096,-7.735922,-9.284452,-4.052184,2.164543],[-0.547757,-7.917215,6.144482,2.340815,8.122786,1.770809,6.340593,8.432223,6.525266],[4.263674,-5.228319,0.993459,8.607320,-5.109549,9.162923,-0.964694,8.533891,-2.616773]],[[5.118525,-1.780346,-4.523139,0.226580,-7.985543,-2.250962,-4.469783,-2.314263,1.634182],[3.324172,8.898957,-2.684947,-2.510878,6.932378,6.375000,-9.708928,1.688301,8.885975],[-7.144725,0.222951,-1.168357,-7.728585,5.467944,4.470714,9.603420,3.731076,-5.558396],[6.832223,-1.293843,7.359788,5.341447,-8.970342,-2.064249,-9.032413,-6.334294,5.369836],[7.628517,2.391626,-4.397633,1.708546,-2.290720,5.081278,-7.508585,9.249229,9.584949],[-6.590787,-3.548644,3.729377,-1.837662,3.553859,-4.694023,7.930849,-4.983026,-6.992562],[9.672874,-5.737595,2.987390,4.828623,9.689987,-3.497775,5.823669,4.846969,-7.923684],[-4.460745,-6.660181,5.139921,-1.344724,-8.112260,-1.031597,-1.014285,-8.698238,3.760423],[-9.491807,5.779441,2.587234,-9.413082,-9.078215,-7.152137,-9.310945,4.498721,-7.820366],[8.500805,-2.996186,4.963459,5.931845,-9.459535,3.962858,2.726511,-3.849139,6.029166],[-0.054577,-5.004003,1.985453,7.687483,1.705588,-9.729904,-2.265838,3.028109,7.072481],[2.050397,-1.471170,-3.997877,1.044470,9.011742,-4.565376,0.718084,-2.981253,1.015236],[-4.683998,1.304989,8.612190,4.068267,-7.690613,-9.954558,4.754349,-5.356424,-7.307442]],[[9.252955,-6.172412,0.294323,4.771826,6.868031,4.294956,3.137725,-4.396675,5.466574],[-9.345142,5.804846,0.372338,-0.273734,1.359242,-9.289214,5.241650,5.679224,-4.716655],[-1.917258,0.858224,6.886314,-5.133832,-9.945696,-0.761159,6.133352,-8.226334,1.424527],[-3.008481,-2.856469,-4.078751,8.948697,3.838663,4.373939,-4.903979,7.411675,7.033796],[-4.261907,-8.881980,-7.247171,-6.584892,2.651747,-4.506928,9.148442,9.074135,-0.054181],[-8.919305,3.347591,-3.448337,-3.069559,2.388971,-3.837384,-0.668258,-0.431259,1.086641],[5.445039,-4.335970,-8.120789,9.742730,-8.790644,-4.524496,-2.806185,-8.841229,-3.695479],[-7.807225,0.385282,-8.230803,2.499273,-2.413363,9.178066,-7.865561,-6.156274,-2.026342],[-0.663230,-1.180228,-7.171617,6.427629,7.127924,-6.609773,7.599085,-8.950214,-4.647510],[-2.904788,-9.914003,-6.127216,7.526474,-6.844940,1.046379,-1.410363,7.627216,-3.509765],[9.279885,-4.024895,-9.327027,-6.853856,-5.253770,-7.965607,-2.125440,-3.483049,-6.682091],[-5.291468,0.531063,9.261491,5.060188,-5.540656,-6.118475,-7.086491,7.469200,-6.392169],[-3.271928,1.887726,-0.878781,7.983188,-2.788230,0.173415,-1.667182,-1.988801,-5.112409]],[[2.115730,-1.122407,-7.578330,-8.664808,-2.912580,-6.045436,6.669937,-3.222151,7.830241],[2.975726,5.126445,-5.779897,-6.470691,-0.878696,-0.306972,-3.166069,7.088198,-5.806668],[3.040833,-4.487019,-4.615191,-4.689311,8.773853,-8.421121,6.299126,-2.540984,5.404991],[4.916514,5.094055,5.720976,0.105461,0.170217,-1.320729,-9.884159,9.246093,2.167270],[2.005666,4.404038,-8.709454,8.942957,9.268340,-7.358978,-3.933280,-4.992689,-8.353900],[-0.239210,1.277547,-6.186821,9.111166,2.772240,8.615196,-5.989757,9.427820,-3.250012],[8.835324,0.297466,5.024796,8.211644,-0.637316,4.433671,9.943582,-2.488614,-4.011731],[-9.185244,4.395378,-9.761576,0.191236,-5.634852,-7.577385,-0.145645,-2.629796,1.688985],[-7.473492,-8.636967,-9.254508,3.332012,0.336411,3.211394,-4.689564,3.399066,3.874746],[-1.951251,-9.352261,6.804319,5.326375,-0.570790,-4.692425,4.258385,-4.990659,1.725189],[-7.623881,9.886135,-5.825847,7.226223,-3.386623,-3.759359,-0.300150,-2.260263,1.187820],[8.468837,-0.901913,7.256423,0.095873,9.346714,-7.333309,7.439863,3.991666,-8.493337],[7.467475,-4.322449,-8.403404,2.274257,6.822100,1.833129,-2.236821,-7.090878,-0.620592]],[[9.205018,-6.183274,5.688584,8.860418,4.765726,2.882814,-5.235948,2.709491,4.930065],[9.333778,-9.020744,-5.081876,-7.455676,7.839105,9.394823,-6.748278,8.592498,9.927628],[0.433459,0.517773,4.443694,-4.091632,4.065272,-3.688283,3.779583,-8.374749,9.137826],[3.445469,7.269501,-3.541834,-1.697585,6.597591,9.514039,-1.971094,0.574126,-9.631132],[0.002175,-3.258155,-4.011959,1.938257,-8.073672,-3.294615,-9.275818,8.747103,-4.381882],[2.904682,-0.062925,-0.078574,7.331049,-1.113492,9.434180,-5.781890,0.561782,2.630353],[1.108437,9.047515,-0.657279,1.400529,8.504889,-7.240776,-9.026398,-5.041473,-7.624905],[7.366651,-2.778008,-8.644859,-1.175604,-7.865574,5.013698,2.066110,-9.908882,6.948684],[-4.174944,2.880382,7.312389,0.220826,2.845020,5.089050,3.616835,-0.124650,-6.640883],[8.213225,4.194216,7.379832,4.095349,0.708116,7.887355,0.094480,-3.928979,-4.933373],[-5.185095,1.267231,9.499831,-6.089987,7.381795,-9.200697,6.959124,-2.181060,6.335512],[-3.191556,0.559065,-1.001575,-0.842861,-2.532133,8.010981,-4.573470,3.303476,1.706510],[-5.827059,9.599709,-0.448718,-6.679428,4.096423,-2.961167,-5.692085,0.665596,3.688265]],[[-8.074142,6.283297,-2.359847,8.821251,7.659974,-4.199962,-9.117440,-7.570310,9.505605],[5.234093,-0.025427,-8.321010,-7.430043,6.759349,-5.231354,0.298220,-0.258077,-4.329622],[9.132268,-5.282034,-5.795190,-2.761701,8.978727,-7.314837,8.381704,-1.138319,-7.680673],[2.698692,9.851139,-5.771283,3.850202,4.002978,9.123414,-6.058459,1.175352,8.201096],[1.134152,-0.924939,-9.758703,6.215339,0.984249,7.647695,5.781348,-9.140758,-0.226389],[-1.951746,-3.556677,5.069870,7.445928,0.201966,-0.281672,-4.911079,-5.362608,6.859686],[7.003983,-8.679966,-1.875812,-0.686589,-8.192689,6.425257,-4.806774,-5.442611,7.564993],[-3.350412,0.598260,0.280938,-3.154256,-3.873827,8.674646,3.299107,-2.888982,8.513544],[9.215818,-0.429357,-2.274223,-4.116420,-5.067634,8.169080,8.332686,-7.151322,0.598413],[-5.316769,-0.312520,-6.773279,-7.379754,-5.725107,-8.986370,-0.892837,-3.045798,5.390875],[-1.231664,0.002547,5.249468,-7.984445,-2.560663,0.089059,-5.158755,9.721489,-5.179294],[-0.204090,3.597799,-4.575140,-3.844142,9.053804,3.480031,3.179865,3.602994,-1.554572],[-9.413753,2.115234,-4.697937,-7.338255,-2.885406,3.368790,-4.575455,-1.246868,-2.362028]],[[1.347235,9.518527,7.876175,1.153930,-1.833421,6.220297,4.470190,1.993452,-3.716884],[-7.278601,-2.626709,-4.582697,3.881114,-3.390614,-8.414962,-2.663370,8.983448,7.403514],[1.032512,-6.365640,4.469390,-6.261275,8.347576,7.045187,2.352674,-9.297260,-9.294343],[7.302279,2.863277,7.093964,0.766961,7.325594,2.217014,1.055220,-2.256802,-0.149200],[-6.991436,-8.765390,-4.085115,1.741150,2.291506,-6.169771,8.726136,-9.299966,1.724498],[-4.668624,3.208459,0.960429,-6.742351,3.388183,-0.236738,-1.399526,5.634711,-7.110661],[-2.461720,9.104571,-3.497556,-7.974799,-3.515602,-7.602135,-4.150786,-5.845070,5.385055],[6.883373,-4.818097,-6.391254,-6.089346,7.964886,0.366355,-5.194075,-7.053029,-3.562493],[4.506639,-3.174409,1.478902,3.703422,2.373835,9.168469,5.428819,9.042055,-5.350342],[9.336986,-9.024650,-7.945457,-2.445251,-7.253120,-2.771116,9.544240,3.865364,1.473800],[6.954709,-5.162715,-0.681181,7.827322,-0.091978,-7.731825,-4.623784,-5.705066,-2.599171],[-6.941468,9.155612,8.000442,4.978401,0.371319,-6.367087,1.936023,9.790749,7.772950],[-4.238210,1.120092,7.823723,4.935729,0.147025,-3.664732,-4.052539,7.998886,4.770309]],[[8.791522,4.251962,2.843058,-6.393511,5.510411,6.207856,4.376877,4.538410,-0.834083],[-3.075999,-7.535254,5.343650,-1.486924,-7.425459,0.797482,-0.621285,-5.036012,3.405881],[-9.434117,4.667863,5.980928,-6.909150,-9.453297,-9.515602,-9.367748,-9.501347,-9.338167],[4.872975,5.534243,-5.344860,-5.368594,8.291812,4.186413,-7.926511,-7.035769,7.288032],[-4.010697,1.413290,-0.598470,-0.560586,-1.664969,0.199591,-3.744341,0.792295,-6.483793],[8.113354,3.475617,-3.146254,2.615693,-6.944108,-8.564621,-8.904279,3.837061,5.142726],[6.957333,-8.475574,-9.851705,-7.450343,-5.451368,-3.042962,-5.895640,6.417817,-7.167768],[-7.733696,3.062015,-8.960603,-3.266113,-0.978010,-1.536486,9.853705,7.987320,6.879175],[-8.889156,4.581706,-5.046941,1.664755,0.554302,-1.680252,-3.635328,6.124443,9.999522],[5.273488,-7.472728,6.222073,6.832571,-2.745348,-8.276187,-3.812664,-3.722142,9.199846],[5.775711,2.363529,-8.652340,6.152002,-2.301430,-4.150460,-0.904472,8.423923,3.835882],[9.531404,-7.782034,-0.517516,6.384148,6.676795,-6.953152,-4.878031,8.766597,-0.701294],[4.199816,6.584225,-3.884375,1.206311,6.136455,-2.638007,4.540848,-1.680988,3.764719]],[[-1.838660,9.662691,-7.141315,4.463329,-5.981311,-2.939434,-8.107469,-8.961156,6.587256],[9.158557,4.482653,-3.475889,1.308087,7.249969,9.846342,-4.693692,8.074652,4.376385],[6.029952,1.986685,2.195021,-5.723846,8.899823,6.636378,-8.564330,-7.442261,-8.965179],[5.391437,-9.715672,3.341739,8.126953,-2.131403,4.355864,9.287584,-7.045147,-6.567327],[-7.376855,2.429836,9.802630,8.681272,5.598878,4.429760,-8.003800,2.281837,3.107819],[-2.853211,5.907172,-3.481883,-4.163195,7.509899,-1.653082,-1.525194,5.559782,-7.552159],[3.121912,-5.995337,3.880791,-0.952611,-7.223907,8.642556,-9.348721,-8.544830,-0.030861],[-6.417883,-8.855401,1.340686,-3.079931,-3.049484,3.788860,-1.537904,-0.148256,2.480150],[0.553783,9.924900,2.643819,9.228250,-0.345053,5.718425,-9.448771,7.703985,-1.999771],[9.950155,-7.493617,-1.277776,4.513150,-1.880541,3.855200,8.503308,5.061582,-9.437616],[1.682508,-5.456489,5.578653,-7.749783,-2.601996,5.620838,-2.286379,6.025860,-7.129987],[-9.641584,-7.402708,0.901208,-6.946898,-5.308156,6.754278,9.313780,1.798491,-5.684978],[0.656295,-2.602696,-6.795112,-7.484803,8.507316,0.255185,9.949811,9.642452,8.031340]]], dtype = "float64")#candidate|7146|(15, 13, 9)|const|float64
uop_7147 = relay.sqrt(const_7146.astype('float64')) # shape=(15, 13, 9)
func_2800_call = mod.get_global_var('func_2800')
func_2805_call = mutated_mod.get_global_var('func_2805')
const_7165 = relay.const([5,-4,-8,8,9,4,1,-10,-1,10,2,8,-4,6,-7,9,4,-1,-4,-8,2,2,3,-8,10,2,5,7,-2,-1,-4,3,4,8,2,-2,10,-6,5,-7,-1,7,8,-5,-1,-1,5,-10,-7,6,6,2,3,9,1,2,-3,-7,-5,1,-7,10,8,2,2,-5,-7,6,-4,-7,-9,6,-10,-4,5,2,10,5,-5,3,4,-6,4,10,-5,4,8,7,-5,4,6,2,-9,4,-4,1,-7,-9,-7,3,-8,7,1,5,-6,-7,-6,-8,8,10,1,9,8,-2,-7,-10,-2,-10,-2,-10,-5,-9,-6,5,-1,5,8,-3,-2,-3,10,3,-10,-6,9,1,2,2,-8,-1,5,4,-10,10,-4,10,-6,-7,-5,1,10,7,-3,-10,-7,2,7,-5,-5,-8,8,4,-10,-2,-5,-10,-4,-6,5,8,5,3,-9,10,3,-2,5,-5,-6,-1,-2,7,7,3,-7,3,2,-5,-4,5,-2,-8,-5,-3,2,4,-6,-9,2,6,-2,3,-7,-5,1,8,-8,-10,1,-6,9,6,2,-10,-7,6,-5,5,7,-5,-1,4,1,-4,7,-5,3,4,9,2,10,9,-8,9,4,6,7,7,-3,-10,3,1,-9,1,-6,-7,-2,-4,-1,-10,9,10,-7,5,8,-4,-3,6,7,1,10,-2,4,-7,-2,-10,2,-8,9,-10,-9,7,-7,-3,10,-10,3,5,1,-4,8,4,6,-10,5,1,4,5,8,-8,1,-9,1,4,5,-6,2,2,4,-10], dtype = "uint16")#candidate|7165|(300,)|const|uint16
const_7166 = relay.const(10, dtype = "uint8")#candidate|7166|()|const|uint8
const_7167 = relay.const([[7.348020,4.966634],[-8.279277,-1.027186],[-7.552140,-6.789710],[-1.047910,-5.703430],[1.288734,-9.596570],[-0.962374,-1.146333],[-3.477657,-1.093478],[2.662992,1.227137],[6.089516,-2.359185],[-7.379449,-2.337732],[-4.902234,4.469080],[-8.548492,1.911427],[-8.534524,0.072812],[-8.098955,-2.577713],[8.329841,7.068385],[0.172710,7.078474],[8.164942,-3.830108],[-0.930936,4.270651],[9.057710,2.849216],[-3.841633,-8.168877],[-4.348023,-4.930672],[0.950358,2.797292],[0.342213,4.278401],[5.202370,-0.865176],[-2.497316,-3.926896],[3.352211,2.997825],[-7.537154,1.836020],[9.090513,-2.723682],[0.021503,-9.955149],[6.630412,6.233071],[-8.976150,0.161427],[8.254844,2.257258],[-6.157192,-3.349856],[9.731172,2.503657],[-9.017525,-4.732178],[-9.899324,1.524802],[7.313874,-5.034097],[4.404844,-3.770304],[5.430474,5.076730],[7.283159,-8.439506],[6.851153,7.037194],[0.597478,-1.112340],[8.479752,4.686978],[6.090554,9.124970],[4.385244,-7.696216],[6.722236,-5.040164],[-8.200422,7.942378],[-1.465226,-6.124351],[-7.383957,-0.791228],[-8.937639,3.852828],[-0.393297,0.576131],[0.158680,-6.895561],[-2.494080,8.696587],[9.853041,-4.572471],[-4.493616,3.579778],[-1.687234,-4.665402],[-7.015589,-3.738525],[9.402964,-5.344597],[-6.625418,-3.590633],[5.316570,-2.708999],[0.727217,9.409278],[-7.136459,-9.691750],[-8.351040,8.624215],[8.886882,6.712475],[2.235713,-6.209010],[-5.965067,-7.684650],[-2.343333,-7.656849],[1.584952,-2.178735],[6.653308,-1.443583],[4.091440,-9.790462],[-5.845379,-8.232099],[7.838396,4.395741],[8.824706,9.499439],[8.255663,9.210499],[-5.589445,1.254487]], dtype = "float32")#candidate|7167|(75, 2)|const|float32
call_7164 = relay.TupleGetItem(func_2800_call(relay.reshape(const_7165.astype('uint16'), [15, 2, 10]), relay.reshape(const_7166.astype('uint8'), []), relay.reshape(const_7167.astype('float32'), [75, 2]), ), 2)
call_7168 = relay.TupleGetItem(func_2805_call(relay.reshape(const_7165.astype('uint16'), [15, 2, 10]), relay.reshape(const_7166.astype('uint8'), []), relay.reshape(const_7167.astype('float32'), [75, 2]), ), 2)
output = relay.Tuple([uop_7147,call_7164,const_7165,const_7166,const_7167,])
output2 = relay.Tuple([uop_7147,call_7168,const_7165,const_7166,const_7167,])
func_7172 = relay.Function([], output)
mod['func_7172'] = func_7172
mod = relay.transform.InferType()(mod)
output = func_7172()
func_7173 = relay.Function([], output)
mutated_mod['func_7173'] = func_7173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_7225 = relay.TupleGetItem(func_7172_call(), 2)
call_7226 = relay.TupleGetItem(func_7173_call(), 2)
output = call_7225
output2 = call_7226
func_7228 = relay.Function([], output)
mod['func_7228'] = func_7228
mod = relay.transform.InferType()(mod)
mutated_mod['func_7228'] = func_7228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mutated_mod.get_global_var('func_7228')
call_7229 = func_7228_call()
output = call_7229
func_7230 = relay.Function([], output)
mutated_mod['func_7230'] = func_7230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_7304 = func_7228_call()
call_7305 = func_7228_call()
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_7315 = func_7228_call()
call_7316 = func_7228_call()
output = relay.Tuple([call_7304,call_7315,])
output2 = relay.Tuple([call_7305,call_7316,])
func_7325 = relay.Function([], output)
mod['func_7325'] = func_7325
mod = relay.transform.InferType()(mod)
mutated_mod['func_7325'] = func_7325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7325_call = mutated_mod.get_global_var('func_7325')
call_7326 = func_7325_call()
output = call_7326
func_7327 = relay.Function([], output)
mutated_mod['func_7327'] = func_7327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_7399 = relay.TupleGetItem(func_7172_call(), 2)
call_7400 = relay.TupleGetItem(func_7173_call(), 2)
func_4669_call = mod.get_global_var('func_4669')
func_4672_call = mutated_mod.get_global_var('func_4672')
const_7411 = relay.const([-4,6,-6,-10,3,3,-3,9,4,-1,7,7,8,5,7,-10,-5,-10,7,3,10,-8,-5,-10,4,9,-7,-7,-6,-9,-10,-1,3,-5,3,-4,6,-6,1,-9,9,8,4,-3,10,3,-10,7,8,-8,2,2,6,-8,-5,-3,4,-2,-9,-9,8,-2,-6,2,3,-5,-1,-2,6,-5,-6,5], dtype = "uint8")#candidate|7411|(72,)|const|uint8
call_7410 = relay.TupleGetItem(func_4669_call(relay.reshape(const_7411.astype('uint8'), [72,])), 7)
call_7412 = relay.TupleGetItem(func_4672_call(relay.reshape(const_7411.astype('uint8'), [72,])), 7)
output = relay.Tuple([call_7399,call_7410,const_7411,])
output2 = relay.Tuple([call_7400,call_7412,const_7411,])
func_7413 = relay.Function([], output)
mod['func_7413'] = func_7413
mod = relay.transform.InferType()(mod)
mutated_mod['func_7413'] = func_7413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mutated_mod.get_global_var('func_7413')
call_7414 = func_7413_call()
output = call_7414
func_7415 = relay.Function([], output)
mutated_mod['func_7415'] = func_7415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_7433 = func_7228_call()
call_7434 = func_7228_call()
func_2982_call = mod.get_global_var('func_2982')
func_2988_call = mutated_mod.get_global_var('func_2988')
var_7456 = relay.var("var_7456", dtype = "float32", shape = (36,))#candidate|7456|(36,)|var|float32
const_7457 = relay.const([[False,True],[True,False],[False,False],[True,True],[False,False],[True,False],[True,False],[False,True],[True,True],[False,False],[True,True],[True,False],[False,False],[False,False],[True,True],[False,True],[False,True],[True,True],[True,False],[False,True],[False,True],[True,True],[False,True],[True,True],[False,True],[True,False],[True,False],[False,True],[True,False],[True,False],[False,True],[True,False],[False,False],[True,True],[False,True],[False,False],[True,True],[True,True],[False,False],[False,True],[False,True],[True,True],[False,True],[False,True],[True,False],[True,True],[True,False],[False,False],[False,True],[True,False],[True,False],[False,False],[True,True],[True,False],[False,True],[True,False],[False,False],[True,False],[True,True],[True,False],[True,False],[False,True],[False,False],[True,False],[True,False],[False,False],[False,False],[False,False],[False,True],[False,False],[False,True],[False,True],[True,True],[True,False],[False,True],[False,False],[True,False],[True,False],[False,False],[False,False],[False,True],[False,True],[True,True],[True,True],[False,True],[True,True],[False,True],[False,True],[False,True],[True,True],[False,True],[True,False],[False,False],[False,False],[False,False],[False,False],[True,True],[True,True],[False,False],[False,False],[True,False],[True,True],[True,True],[False,False]], dtype = "bool")#candidate|7457|(104, 2)|const|bool
var_7458 = relay.var("var_7458", dtype = "uint8", shape = (72,))#candidate|7458|(72,)|var|uint8
var_7459 = relay.var("var_7459", dtype = "uint8", shape = ())#candidate|7459|()|var|uint8
call_7455 = relay.TupleGetItem(func_2982_call(relay.reshape(var_7456.astype('float32'), [2, 9, 2]), relay.reshape(var_7456.astype('float32'), [2, 9, 2]), relay.reshape(const_7457.astype('bool'), [208,]), relay.reshape(var_7458.astype('uint8'), [36, 2]), relay.reshape(var_7459.astype('uint8'), []), ), 7)
call_7460 = relay.TupleGetItem(func_2988_call(relay.reshape(var_7456.astype('float32'), [2, 9, 2]), relay.reshape(var_7456.astype('float32'), [2, 9, 2]), relay.reshape(const_7457.astype('bool'), [208,]), relay.reshape(var_7458.astype('uint8'), [36, 2]), relay.reshape(var_7459.astype('uint8'), []), ), 7)
func_2381_call = mod.get_global_var('func_2381')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_7463 = relay.TupleGetItem(func_2381_call(relay.reshape(const_7457.astype('bool'), [8, 13, 2]), relay.reshape(var_7458.astype('uint8'), [72,]), ), 2)
call_7464 = relay.TupleGetItem(func_2384_call(relay.reshape(const_7457.astype('bool'), [8, 13, 2]), relay.reshape(var_7458.astype('uint8'), [72,]), ), 2)
var_7484 = relay.var("var_7484", dtype = "uint8", shape = (10, 5, 10))#candidate|7484|(10, 5, 10)|var|uint8
bop_7485 = relay.floor_mod(call_7463.astype('float32'), var_7484.astype('float32')) # shape=(10, 5, 10)
bop_7488 = relay.floor_mod(call_7464.astype('float32'), var_7484.astype('float32')) # shape=(10, 5, 10)
output = relay.Tuple([call_7433,call_7455,var_7456,const_7457,var_7458,var_7459,bop_7485,])
output2 = relay.Tuple([call_7434,call_7460,var_7456,const_7457,var_7458,var_7459,bop_7488,])
func_7489 = relay.Function([var_7456,var_7458,var_7459,var_7484,], output)
mod['func_7489'] = func_7489
mod = relay.transform.InferType()(mod)
mutated_mod['func_7489'] = func_7489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7489_call = mutated_mod.get_global_var('func_7489')
var_7491 = relay.var("var_7491", dtype = "float32", shape = (36,))#candidate|7491|(36,)|var|float32
var_7492 = relay.var("var_7492", dtype = "uint8", shape = (72,))#candidate|7492|(72,)|var|uint8
var_7493 = relay.var("var_7493", dtype = "uint8", shape = ())#candidate|7493|()|var|uint8
var_7494 = relay.var("var_7494", dtype = "uint8", shape = (10, 5, 10))#candidate|7494|(10, 5, 10)|var|uint8
call_7490 = func_7489_call(var_7491,var_7492,var_7493,var_7494,)
output = call_7490
func_7495 = relay.Function([var_7491,var_7492,var_7493,var_7494,], output)
mutated_mod['func_7495'] = func_7495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7325_call = mod.get_global_var('func_7325')
func_7327_call = mutated_mod.get_global_var('func_7327')
call_7497 = relay.TupleGetItem(func_7325_call(), 0)
call_7498 = relay.TupleGetItem(func_7327_call(), 0)
output = relay.Tuple([call_7497,])
output2 = relay.Tuple([call_7498,])
func_7501 = relay.Function([], output)
mod['func_7501'] = func_7501
mod = relay.transform.InferType()(mod)
output = func_7501()
func_7502 = relay.Function([], output)
mutated_mod['func_7502'] = func_7502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_7510 = relay.TupleGetItem(func_7172_call(), 3)
call_7511 = relay.TupleGetItem(func_7173_call(), 3)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_7521 = relay.TupleGetItem(func_7413_call(), 2)
call_7522 = relay.TupleGetItem(func_7415_call(), 2)
func_2982_call = mod.get_global_var('func_2982')
func_2988_call = mutated_mod.get_global_var('func_2988')
const_7526 = relay.const([1.414097,-9.756003,9.958511,-8.842277,-6.307710,-6.806712,8.557699,3.759821,-2.329364,8.129013,-6.063885,-0.522723,5.400981,3.537994,-6.496965,5.856386,6.040138,9.206570,-2.312259,8.559491,3.341779,-6.263095,2.796271,0.334199,-0.092383,-1.093188,8.148545,2.360628,5.063027,3.725039,-1.330225,0.130372,-1.253170,-1.526001,-3.075711,-0.222798], dtype = "float32")#candidate|7526|(36,)|const|float32
var_7527 = relay.var("var_7527", dtype = "bool", shape = (208,))#candidate|7527|(208,)|var|bool
call_7525 = relay.TupleGetItem(func_2982_call(relay.reshape(const_7526.astype('float32'), [2, 9, 2]), relay.reshape(const_7526.astype('float32'), [2, 9, 2]), relay.reshape(var_7527.astype('bool'), [208,]), relay.reshape(call_7521.astype('uint8'), [36, 2]), relay.reshape(call_7510.astype('uint8'), []), ), 5)
call_7528 = relay.TupleGetItem(func_2988_call(relay.reshape(const_7526.astype('float32'), [2, 9, 2]), relay.reshape(const_7526.astype('float32'), [2, 9, 2]), relay.reshape(var_7527.astype('bool'), [208,]), relay.reshape(call_7521.astype('uint8'), [36, 2]), relay.reshape(call_7510.astype('uint8'), []), ), 5)
func_3812_call = mod.get_global_var('func_3812')
func_3820_call = mutated_mod.get_global_var('func_3820')
var_7545 = relay.var("var_7545", dtype = "float32", shape = (2, 300))#candidate|7545|(2, 300)|var|float32
var_7546 = relay.var("var_7546", dtype = "uint16", shape = (300,))#candidate|7546|(300,)|var|uint16
var_7547 = relay.var("var_7547", dtype = "bool", shape = (624,))#candidate|7547|(624,)|var|bool
var_7548 = relay.var("var_7548", dtype = "float32", shape = (720,))#candidate|7548|(720,)|var|float32
call_7544 = relay.TupleGetItem(func_3812_call(relay.reshape(call_7510.astype('float32'), []), relay.reshape(var_7545.astype('float32'), [10, 6, 10]), relay.reshape(var_7546.astype('uint16'), [300,]), relay.reshape(const_7526.astype('float32'), [18, 2]), relay.reshape(var_7527.astype('bool'), [1, 208]), relay.reshape(var_7547.astype('bool'), [3, 208]), relay.reshape(var_7548.astype('float32'), [60, 12]), ), 10)
call_7549 = relay.TupleGetItem(func_3820_call(relay.reshape(call_7510.astype('float32'), []), relay.reshape(var_7545.astype('float32'), [10, 6, 10]), relay.reshape(var_7546.astype('uint16'), [300,]), relay.reshape(const_7526.astype('float32'), [18, 2]), relay.reshape(var_7527.astype('bool'), [1, 208]), relay.reshape(var_7547.astype('bool'), [3, 208]), relay.reshape(var_7548.astype('float32'), [60, 12]), ), 10)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_7558 = relay.TupleGetItem(func_7413_call(), 2)
call_7559 = relay.TupleGetItem(func_7415_call(), 2)
output = relay.Tuple([call_7510,call_7521,call_7525,const_7526,var_7527,call_7544,var_7545,var_7546,var_7547,var_7548,call_7558,])
output2 = relay.Tuple([call_7511,call_7522,call_7528,const_7526,var_7527,call_7549,var_7545,var_7546,var_7547,var_7548,call_7559,])
func_7579 = relay.Function([var_7527,var_7545,var_7546,var_7547,var_7548,], output)
mod['func_7579'] = func_7579
mod = relay.transform.InferType()(mod)
var_7580 = relay.var("var_7580", dtype = "bool", shape = (208,))#candidate|7580|(208,)|var|bool
var_7581 = relay.var("var_7581", dtype = "float32", shape = (2, 300))#candidate|7581|(2, 300)|var|float32
var_7582 = relay.var("var_7582", dtype = "uint16", shape = (300,))#candidate|7582|(300,)|var|uint16
var_7583 = relay.var("var_7583", dtype = "bool", shape = (624,))#candidate|7583|(624,)|var|bool
var_7584 = relay.var("var_7584", dtype = "float32", shape = (720,))#candidate|7584|(720,)|var|float32
output = func_7579(var_7580,var_7581,var_7582,var_7583,var_7584,)
func_7585 = relay.Function([var_7580,var_7581,var_7582,var_7583,var_7584,], output)
mutated_mod['func_7585'] = func_7585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_7616 = relay.TupleGetItem(func_7501_call(), 0)
call_7617 = relay.TupleGetItem(func_7502_call(), 0)
output = relay.Tuple([call_7616,])
output2 = relay.Tuple([call_7617,])
func_7630 = relay.Function([], output)
mod['func_7630'] = func_7630
mod = relay.transform.InferType()(mod)
output = func_7630()
func_7631 = relay.Function([], output)
mutated_mod['func_7631'] = func_7631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_7676 = relay.TupleGetItem(func_7413_call(), 0)
call_7677 = relay.TupleGetItem(func_7415_call(), 0)
output = relay.Tuple([call_7676,])
output2 = relay.Tuple([call_7677,])
func_7729 = relay.Function([], output)
mod['func_7729'] = func_7729
mod = relay.transform.InferType()(mod)
output = func_7729()
func_7730 = relay.Function([], output)
mutated_mod['func_7730'] = func_7730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_7734 = relay.TupleGetItem(func_7172_call(), 0)
call_7735 = relay.TupleGetItem(func_7173_call(), 0)
uop_7747 = relay.asin(call_7734.astype('float32')) # shape=(15, 13, 9)
uop_7749 = relay.asin(call_7735.astype('float32')) # shape=(15, 13, 9)
func_7489_call = mod.get_global_var('func_7489')
func_7495_call = mutated_mod.get_global_var('func_7495')
const_7770 = relay.const([-3.498230,-2.520636,-0.485969,-8.330087,-8.517176,9.226277,-9.828330,5.752141,3.229372,-7.808496,6.304981,-8.908008,-9.620708,-5.125771,4.402516,9.342652,8.664267,-9.448782,2.981253,-6.515091,6.343284,-0.211223,-8.236518,-6.631722,7.344933,-0.982696,-0.283111,-5.092172,1.374409,-8.488396,7.182536,3.210055,-0.516216,-1.503490,-5.860678,4.729733], dtype = "float32")#candidate|7770|(36,)|const|float32
var_7771 = relay.var("var_7771", dtype = "uint8", shape = (72,))#candidate|7771|(72,)|var|uint8
const_7772 = relay.const(-1, dtype = "uint8")#candidate|7772|()|const|uint8
var_7773 = relay.var("var_7773", dtype = "uint8", shape = (500,))#candidate|7773|(500,)|var|uint8
call_7769 = relay.TupleGetItem(func_7489_call(relay.reshape(const_7770.astype('float32'), [36,]), relay.reshape(var_7771.astype('uint8'), [72,]), relay.reshape(const_7772.astype('uint8'), []), relay.reshape(var_7773.astype('uint8'), [10, 5, 10]), ), 6)
call_7774 = relay.TupleGetItem(func_7495_call(relay.reshape(const_7770.astype('float32'), [36,]), relay.reshape(var_7771.astype('uint8'), [72,]), relay.reshape(const_7772.astype('uint8'), []), relay.reshape(var_7773.astype('uint8'), [10, 5, 10]), ), 6)
output = relay.Tuple([uop_7747,call_7769,const_7770,var_7771,const_7772,var_7773,])
output2 = relay.Tuple([uop_7749,call_7774,const_7770,var_7771,const_7772,var_7773,])
func_7777 = relay.Function([var_7771,var_7773,], output)
mod['func_7777'] = func_7777
mod = relay.transform.InferType()(mod)
var_7778 = relay.var("var_7778", dtype = "uint8", shape = (72,))#candidate|7778|(72,)|var|uint8
var_7779 = relay.var("var_7779", dtype = "uint8", shape = (500,))#candidate|7779|(500,)|var|uint8
output = func_7777(var_7778,var_7779,)
func_7780 = relay.Function([var_7778,var_7779,], output)
mutated_mod['func_7780'] = func_7780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7630_call = mod.get_global_var('func_7630')
func_7631_call = mutated_mod.get_global_var('func_7631')
call_7788 = relay.TupleGetItem(func_7630_call(), 0)
call_7789 = relay.TupleGetItem(func_7631_call(), 0)
func_3055_call = mod.get_global_var('func_3055')
func_3059_call = mutated_mod.get_global_var('func_3059')
const_7812 = relay.const(0.908497, dtype = "float32")#candidate|7812|()|const|float32
const_7813 = relay.const([4.893777,-1.683869,-8.922262,-5.523062,3.294977,-5.049558,3.899762,-4.287986,4.212427,-2.672696,8.349046,-7.964975,-4.034644,-5.853771,-6.246361,-3.314818,7.830927,5.914405,-9.817640,8.679172,-2.866986,9.769645,-2.379372,3.314359,-3.948013,-1.925086,-0.611827,-2.349692,-0.548924,5.623598,-5.995697,-5.061430,-6.989680,0.997199,-9.568088,-7.398356,-0.930530,-4.729700,-3.281921,-3.291955,-2.189424,-9.250011,-9.360776,8.046509,3.451234,3.264086,-7.760529,-7.548109,8.056140,-2.442876,-2.541167,5.878091,-0.314886,-6.248125,7.789138,-7.550192,1.907726,-7.282026,5.462630,-3.759840,-4.947212,4.883988,-5.350052,3.572717,5.059292,3.277649,4.944561,1.361317,-1.816721,-5.885839,-4.713024,5.638882,8.861331,4.660666,-0.216874,-6.148307,6.858532,7.434332,7.809142,-3.763804,-4.998490,-7.817336,-6.354140,-9.923119,0.724032,-5.586493,1.734014,4.810861,2.099166,1.498967,0.615203,6.161926,0.171979,-7.038723,6.255499,-3.439118,-5.664995,3.428154,-3.375506,9.655190,-1.363950,8.799223,-3.584989,1.474167,-9.866950,1.918119,-1.739725,-3.702725,0.628730,-1.520717,0.459341,0.238148,0.492946,-8.742391,-7.858635,-8.407337,2.484904,-4.462638,-8.711155,-5.259977,-1.528963,-6.877093,-3.281055,3.712804,4.814173,-5.903798,-7.289683,-1.360767,1.473578,7.567522,2.695598,-5.617163,4.423466,-6.561305,-8.562793,-8.769777,-8.444193,9.973493,-9.834673,-9.440534,-3.427878,-2.210194,-9.577825,6.036013,-6.037620,6.588033,-0.235232,-8.377715,-2.142458,3.688769,4.237370,-7.871307,8.587701,-7.422314,-4.170336,1.069148,-4.471112,8.304469,5.054281,-0.388344,8.182898,5.412497,9.608708,1.704359,-9.964045,4.955207,3.186383,5.037570,0.937922,-9.210404,-0.859113,4.396413,6.062618,-3.341068,0.214041,-0.582721,-8.487421,-4.711711,-6.804155,-4.377306,-4.599819,-8.502795,1.267115,-1.251427,-3.560715,-2.348122,7.150519,7.849045,-0.348016,7.546089,-3.086625,-2.807458,1.826748,-5.516380,-7.883292,-3.964963,-0.315577,-6.775662,-9.411327,0.325829,4.241952,1.060357,4.669263,-1.173034,-5.306746,2.665257,0.274301,-2.535811,-1.705512,-1.523776,1.536248,6.032758,-5.976131,4.627170,1.042264,5.567706,-8.244614,2.366611,8.884036,1.125959,2.133235,-5.743981,-8.095196,7.489161,0.681672,9.554218,-5.167949,0.668222,5.768681,6.829427,8.398032,9.210734,1.318555,1.834564,-1.098787,8.831368,2.187654,9.490706,-0.884879,-8.223897], dtype = "float32")#candidate|7813|(240,)|const|float32
var_7814 = relay.var("var_7814", dtype = "bool", shape = (52, 4))#candidate|7814|(52, 4)|var|bool
call_7811 = relay.TupleGetItem(func_3055_call(relay.reshape(const_7812.astype('float32'), []), relay.reshape(const_7813.astype('float32'), [2, 8, 15]), relay.reshape(var_7814.astype('bool'), [2, 104]), ), 4)
call_7815 = relay.TupleGetItem(func_3059_call(relay.reshape(const_7812.astype('float32'), []), relay.reshape(const_7813.astype('float32'), [2, 8, 15]), relay.reshape(var_7814.astype('bool'), [2, 104]), ), 4)
output = relay.Tuple([call_7788,call_7811,const_7812,const_7813,var_7814,])
output2 = relay.Tuple([call_7789,call_7815,const_7812,const_7813,var_7814,])
func_7816 = relay.Function([var_7814,], output)
mod['func_7816'] = func_7816
mod = relay.transform.InferType()(mod)
var_7817 = relay.var("var_7817", dtype = "bool", shape = (52, 4))#candidate|7817|(52, 4)|var|bool
output = func_7816(var_7817)
func_7818 = relay.Function([var_7817], output)
mutated_mod['func_7818'] = func_7818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_7829 = relay.TupleGetItem(func_7501_call(), 0)
call_7830 = relay.TupleGetItem(func_7502_call(), 0)
output = relay.Tuple([call_7829,])
output2 = relay.Tuple([call_7830,])
func_7845 = relay.Function([], output)
mod['func_7845'] = func_7845
mod = relay.transform.InferType()(mod)
mutated_mod['func_7845'] = func_7845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7845_call = mutated_mod.get_global_var('func_7845')
call_7846 = func_7845_call()
output = call_7846
func_7847 = relay.Function([], output)
mutated_mod['func_7847'] = func_7847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7325_call = mod.get_global_var('func_7325')
func_7327_call = mutated_mod.get_global_var('func_7327')
call_7892 = relay.TupleGetItem(func_7325_call(), 0)
call_7893 = relay.TupleGetItem(func_7327_call(), 0)
func_3812_call = mod.get_global_var('func_3812')
func_3820_call = mutated_mod.get_global_var('func_3820')
var_7909 = relay.var("var_7909", dtype = "float32", shape = ())#candidate|7909|()|var|float32
var_7910 = relay.var("var_7910", dtype = "float32", shape = (300, 2))#candidate|7910|(300, 2)|var|float32
const_7911 = relay.const([-4.122196,-5.705934,-1.119311,-8.330281,-0.512765,-9.281963,2.976285,4.770498,3.136473,-8.879439,3.551668,7.573977,7.105711,-3.547331,-3.493727,-5.843205,-7.822022,-3.041542,7.612960,-5.434238,-0.490440,0.583780,-0.733327,7.165305,-1.336115,2.045690,-5.118545,8.420990,-0.708877,-7.826775,-3.150798,5.359830,6.059803,7.440480,-5.273160,-2.691419], dtype = "float32")#candidate|7911|(36,)|const|float32
var_7912 = relay.var("var_7912", dtype = "bool", shape = (208,))#candidate|7912|(208,)|var|bool
const_7913 = relay.const([True,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False], dtype = "bool")#candidate|7913|(624,)|const|bool
var_7914 = relay.var("var_7914", dtype = "float32", shape = (720,))#candidate|7914|(720,)|var|float32
call_7908 = relay.TupleGetItem(func_3812_call(relay.reshape(var_7909.astype('float32'), []), relay.reshape(var_7910.astype('float32'), [10, 6, 10]), relay.reshape(call_7892.astype('uint16'), [300,]), relay.reshape(const_7911.astype('float32'), [18, 2]), relay.reshape(var_7912.astype('bool'), [1, 208]), relay.reshape(const_7913.astype('bool'), [3, 208]), relay.reshape(var_7914.astype('float32'), [60, 12]), ), 10)
call_7915 = relay.TupleGetItem(func_3820_call(relay.reshape(var_7909.astype('float32'), []), relay.reshape(var_7910.astype('float32'), [10, 6, 10]), relay.reshape(call_7892.astype('uint16'), [300,]), relay.reshape(const_7911.astype('float32'), [18, 2]), relay.reshape(var_7912.astype('bool'), [1, 208]), relay.reshape(const_7913.astype('bool'), [3, 208]), relay.reshape(var_7914.astype('float32'), [60, 12]), ), 10)
output = relay.Tuple([call_7892,call_7908,var_7909,var_7910,const_7911,var_7912,const_7913,var_7914,])
output2 = relay.Tuple([call_7893,call_7915,var_7909,var_7910,const_7911,var_7912,const_7913,var_7914,])
func_7917 = relay.Function([var_7909,var_7910,var_7912,var_7914,], output)
mod['func_7917'] = func_7917
mod = relay.transform.InferType()(mod)
mutated_mod['func_7917'] = func_7917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7917_call = mutated_mod.get_global_var('func_7917')
var_7919 = relay.var("var_7919", dtype = "float32", shape = ())#candidate|7919|()|var|float32
var_7920 = relay.var("var_7920", dtype = "float32", shape = (300, 2))#candidate|7920|(300, 2)|var|float32
var_7921 = relay.var("var_7921", dtype = "bool", shape = (208,))#candidate|7921|(208,)|var|bool
var_7922 = relay.var("var_7922", dtype = "float32", shape = (720,))#candidate|7922|(720,)|var|float32
call_7918 = func_7917_call(var_7919,var_7920,var_7921,var_7922,)
output = call_7918
func_7923 = relay.Function([var_7919,var_7920,var_7921,var_7922,], output)
mutated_mod['func_7923'] = func_7923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_7937 = relay.TupleGetItem(func_7413_call(), 0)
call_7938 = relay.TupleGetItem(func_7415_call(), 0)
func_7917_call = mod.get_global_var('func_7917')
func_7923_call = mutated_mod.get_global_var('func_7923')
const_7960 = relay.const(6.932254, dtype = "float32")#candidate|7960|()|const|float32
var_7961 = relay.var("var_7961", dtype = "float32", shape = (1, 600))#candidate|7961|(1, 600)|var|float32
var_7962 = relay.var("var_7962", dtype = "bool", shape = (208,))#candidate|7962|(208,)|var|bool
const_7963 = relay.const([3.268349,1.738404,-4.560341,2.880048,6.045854,-4.338566,-5.983959,-0.782273,6.221385,-2.130709,-2.602920,4.801192,3.259427,-1.692856,5.731733,-3.686901,0.341663,-1.220161,7.508827,4.602372,1.146654,-0.063425,6.258973,5.395636,4.063491,1.401769,-7.491675,-0.428797,9.692215,-2.915710,-1.122547,0.165577,-8.471586,5.905179,-0.647163,-9.270617,3.855541,9.963783,-4.917003,9.053361,-3.796832,9.123802,7.535009,-1.527231,-8.966039,-6.301488,7.726083,-3.590859,5.157024,5.632261,-9.759093,7.986318,-8.411094,7.744998,2.697970,-9.619509,9.977190,-8.493458,0.540375,9.688701,-7.074755,0.651088,-3.059007,9.349276,1.936819,4.314021,5.194160,7.674045,4.670316,-6.546709,0.564413,-0.873364,-1.386539,-2.209181,8.844285,-5.928425,4.952445,0.555617,2.519665,0.308006,6.132604,4.401759,1.483058,9.461404,5.518284,6.574626,-4.511378,0.057406,1.745220,3.004570,2.626285,-7.096071,6.204354,-2.381308,-4.067025,1.587511,-3.867374,-9.946282,-4.772809,-2.062878,6.444594,-9.323739,6.097634,7.691721,5.170043,1.423631,-2.333722,2.296504,6.270883,-3.129896,1.087752,-0.900960,-0.111187,0.261918,-6.191343,-1.601463,-8.968129,0.649104,-2.778632,-1.106315,4.663823,3.940669,5.816072,5.265805,-5.299182,-8.763839,-5.709281,-6.409815,-0.249243,9.718580,9.381902,-5.540009,-0.284239,-4.244889,-0.390958,1.900780,-2.506888,5.224771,5.952046,3.221735,3.928025,-5.026725,-2.731310,-4.277777,-9.032330,4.409704,-4.375268,7.498143,0.753295,3.149709,-9.556001,-7.397020,1.594555,-1.206841,-8.747515,6.750191,-5.616280,3.115457,-6.991756,6.632486,0.211575,-7.068638,-6.303440,0.143493,2.810140,-1.589191,3.549918,2.769793,-6.024513,2.742812,3.728250,-8.072391,-4.276891,-2.998139,-8.608021,-8.057921,-9.679988,1.494834,-8.679168,-1.087524,5.341879,-0.726530,9.004130,-8.191456,5.587243,5.117603,-7.510446,-0.320839,7.887006,7.572955,-6.512328,-3.855771,-3.388741,-1.022057,-7.846384,5.911223,5.889528,-1.519582,7.404094,-9.272375,-4.544460,6.780592,-2.271532,-7.701000,-6.721343,8.918285,1.861012,8.701129,0.661784,-4.838363,-2.824840,6.690854,9.954407,5.649007,-7.796112,-6.708906,7.614100,5.595197,1.704471,7.261584,2.621372,0.687636,-1.490307,1.723547,-3.416492,2.922013,1.011728,-6.981496,-9.287292,3.709767,1.618758,-3.203750,7.960494,-0.294957,3.394245,-9.280426,-1.629065,3.569946,-5.784047,-2.741566,-8.281265,8.547250,7.323527,1.072227,7.024037,-0.162846,-5.107347,7.565067,3.935417,-5.898637,-7.667897,0.124826,-3.831531,6.366928,8.604091,3.884670,-8.502601,2.047084,-7.956448,3.251517,4.994209,8.316881,-6.069739,4.829879,-0.374460,-6.888168,-8.641213,-5.069202,-2.253551,6.010706,9.320096,-5.181580,-0.535246,9.042769,-9.948914,-1.113205,9.334957,9.772175,4.370602,4.544677,-5.089648,-3.709043,2.968404,-1.936429,-2.642067,-9.756922,-5.160574,5.854650,-9.937367,-8.968472,-3.647061,6.178794,-8.534950,9.977762,6.847973,9.500776,8.933474,8.711958,-6.042096,-1.302368,4.837493,6.015146,7.852667,-3.463644,0.188552,-1.561394,-0.516697,3.314991,-3.657963,-3.091113,9.619249,-8.911338,7.147449,-5.334575,2.845335,-0.523624,9.473462,-1.945438,7.156796,-6.947529,8.471205,-2.145731,-5.279165,-9.855385,-2.938084,0.644454,3.734503,-2.529778,5.054783,-8.915734,-6.768734,4.724422,-2.314140,-5.851741,7.955344,6.359852,-2.344025,-9.291852,3.736541,0.037304,8.902390,-2.252512,-4.350686,9.544058,3.701135,-1.204748,-3.550026,6.399036,-2.777643,-9.537594,-0.888502,-7.496867,4.785373,-7.683362,-1.934280,4.515706,-5.924789,-3.922531,-4.984763,-5.307026,7.504812,9.264312,-8.035173,6.747774,1.573290,-2.852917,9.271477,-8.722260,8.497671,1.666632,-8.390711,1.283675,-3.313797,-1.089756,9.638733,-6.585240,7.724220,2.332288,-5.471337,-9.810330,-1.635670,-7.893853,-3.164247,8.749745,2.240073,1.560112,2.546229,-3.472063,-7.487546,-7.675872,1.774088,-5.710255,7.396902,-6.337160,-3.212161,3.160226,-6.547977,-7.685600,-8.034578,-8.868635,4.709221,2.489262,0.016923,-3.218696,-0.818564,2.670031,-1.096537,8.442589,2.341560,5.146644,-3.805944,3.126952,-6.413917,8.429904,1.204844,-9.616867,0.984782,4.619288,5.180271,-8.993442,-2.938140,6.406107,-8.526961,-8.072880,9.216591,1.070061,-0.006312,-8.523924,3.835250,8.129929,8.543960,3.315582,-4.897380,9.271703,-2.584921,8.571653,-4.153004,5.236291,4.426709,-7.935565,-2.818100,3.399377,-5.884773,2.665744,5.101157,-5.885992,6.710453,-8.882103,-1.643165,3.173408,5.084081,-6.583838,-2.544517,-1.111442,3.720175,-8.158936,3.163203,2.531661,1.306986,1.989265,2.826277,5.908411,1.761220,-7.791947,-3.213807,-3.543873,2.982247,7.521998,5.186831,8.456079,-1.979193,-8.169140,6.092428,-5.694290,-2.950382,-5.760932,2.183283,-0.839226,9.109132,6.047318,1.324057,5.339294,-0.405780,-6.040207,5.296307,-4.927217,6.546771,6.905730,-3.311192,7.531242,0.404535,6.700998,3.662534,2.657316,-4.995700,-1.517375,-6.649749,-5.754183,-8.148370,-0.393525,8.610773,-5.238805,9.900109,8.469132,8.741693,0.761518,-4.049803,7.664574,-7.982022,-3.570023,2.175832,-5.921897,1.727755,-2.278217,9.554019,9.977715,-5.903539,9.407945,5.492663,3.940349,6.514520,4.468055,4.906621,-7.508628,3.685883,9.528406,2.948349,-4.723543,-6.896320,4.073463,-1.308871,-1.172269,-6.256277,-9.528555,8.046573,-5.453740,-5.015072,-3.624320,-9.534209,-3.470256,-7.056257,1.179300,7.193705,-8.859191,-3.094042,-8.778868,-8.125587,9.171265,-0.949452,-0.823903,-4.020674,2.127126,-8.896105,-3.076191,-1.467672,-0.896796,-9.434036,-7.420885,0.304742,-0.820420,-9.216329,-8.128122,6.530144,9.141756,-5.412492,8.210438,-1.375780,1.313639,2.401920,-3.788263,-0.721221,-5.245880,-1.156475,7.924497,8.542508,0.651395,-6.372902,-2.537956,-8.495307,0.493618,2.706422,0.516107,2.719596,-5.316789,-9.390018,-3.689648,4.337399,-3.420930,-5.716458,3.047214,5.899377,3.888470,3.945782,1.948956,-7.176604,-7.734332,-4.832788,7.644813,-3.565598,-6.736355,-4.146555,-8.247652,0.439166,8.085713,-1.815327,5.438441,-4.128160,1.865454,-7.790729,7.471816,4.201501,-9.630292,1.229625,-7.938899,6.517506,-1.875249,4.019699,2.890672,6.759503,-4.562818,7.540676,9.859215,8.650103,4.929492,-4.401656,-7.408185,-6.130011,6.413296,-8.012297,-3.542929,-9.247729,-7.641214,9.033093,-0.679858,-9.355904,-4.567267,-3.001021,5.770118,-3.116243,8.751474,4.419378,-4.955479,-9.046042,6.618037,4.496832,-6.782982,4.399651,-6.732264,-6.567308,1.762817,9.274264,-5.813440,-6.206774,0.012164,2.598297,0.985135,-3.871877,-1.155545,2.861061,-7.992483,7.006538,-3.137704,8.409769,5.592308,3.700113,-2.976643,-0.728667,-9.070265,0.326597,2.038688,-9.946373,6.566321,3.579839,4.348387,-0.054565,9.787523,-8.500209,-6.388880,-4.117417,2.336830,-0.182462,0.530054,-4.460517,1.968272,0.744112,-0.850823,4.763931,8.776244,-6.544812,0.269097,-1.001444,-6.019094,-1.688178,-6.143746,4.716229,-5.881891,8.252693,-4.229569,9.237473,1.414948,0.973330,-4.580777,-4.877226,8.019779,-3.874810,1.784828,1.810918,4.846652,-7.168861,7.540939,7.411691,8.891938,4.678080,9.010568,-3.740724,1.498419,-1.381682,-5.668467,1.883409,8.467687], dtype = "float32")#candidate|7963|(720,)|const|float32
call_7959 = relay.TupleGetItem(func_7917_call(relay.reshape(const_7960.astype('float32'), []), relay.reshape(var_7961.astype('float32'), [300, 2]), relay.reshape(var_7962.astype('bool'), [208,]), relay.reshape(const_7963.astype('float32'), [720,]), ), 6)
call_7964 = relay.TupleGetItem(func_7923_call(relay.reshape(const_7960.astype('float32'), []), relay.reshape(var_7961.astype('float32'), [300, 2]), relay.reshape(var_7962.astype('bool'), [208,]), relay.reshape(const_7963.astype('float32'), [720,]), ), 6)
output = relay.Tuple([call_7937,call_7959,const_7960,var_7961,var_7962,const_7963,])
output2 = relay.Tuple([call_7938,call_7964,const_7960,var_7961,var_7962,const_7963,])
func_7975 = relay.Function([var_7961,var_7962,], output)
mod['func_7975'] = func_7975
mod = relay.transform.InferType()(mod)
mutated_mod['func_7975'] = func_7975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7975_call = mutated_mod.get_global_var('func_7975')
var_7977 = relay.var("var_7977", dtype = "float32", shape = (1, 600))#candidate|7977|(1, 600)|var|float32
var_7978 = relay.var("var_7978", dtype = "bool", shape = (208,))#candidate|7978|(208,)|var|bool
call_7976 = func_7975_call(var_7977,var_7978,)
output = call_7976
func_7979 = relay.Function([var_7977,var_7978,], output)
mutated_mod['func_7979'] = func_7979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7630_call = mod.get_global_var('func_7630')
func_7631_call = mutated_mod.get_global_var('func_7631')
call_8030 = relay.TupleGetItem(func_7630_call(), 0)
call_8031 = relay.TupleGetItem(func_7631_call(), 0)
func_7325_call = mod.get_global_var('func_7325')
func_7327_call = mutated_mod.get_global_var('func_7327')
call_8032 = relay.TupleGetItem(func_7325_call(), 0)
call_8033 = relay.TupleGetItem(func_7327_call(), 0)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_8045 = relay.TupleGetItem(func_7501_call(), 0)
call_8046 = relay.TupleGetItem(func_7502_call(), 0)
output = relay.Tuple([call_8030,call_8032,call_8045,])
output2 = relay.Tuple([call_8031,call_8033,call_8046,])
func_8047 = relay.Function([], output)
mod['func_8047'] = func_8047
mod = relay.transform.InferType()(mod)
output = func_8047()
func_8048 = relay.Function([], output)
mutated_mod['func_8048'] = func_8048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_8058 = relay.TupleGetItem(func_7413_call(), 0)
call_8059 = relay.TupleGetItem(func_7415_call(), 0)
output = relay.Tuple([call_8058,])
output2 = relay.Tuple([call_8059,])
func_8065 = relay.Function([], output)
mod['func_8065'] = func_8065
mod = relay.transform.InferType()(mod)
mutated_mod['func_8065'] = func_8065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8065_call = mutated_mod.get_global_var('func_8065')
call_8066 = func_8065_call()
output = call_8066
func_8067 = relay.Function([], output)
mutated_mod['func_8067'] = func_8067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_8085 = relay.TupleGetItem(func_7501_call(), 0)
call_8086 = relay.TupleGetItem(func_7502_call(), 0)
output = call_8085
output2 = call_8086
func_8089 = relay.Function([], output)
mod['func_8089'] = func_8089
mod = relay.transform.InferType()(mod)
output = func_8089()
func_8090 = relay.Function([], output)
mutated_mod['func_8090'] = func_8090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_8158 = relay.TupleGetItem(func_7172_call(), 1)
call_8159 = relay.TupleGetItem(func_7173_call(), 1)
func_7975_call = mod.get_global_var('func_7975')
func_7979_call = mutated_mod.get_global_var('func_7979')
var_8178 = relay.var("var_8178", dtype = "float32", shape = (600,))#candidate|8178|(600,)|var|float32
const_8179 = relay.const([True,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True], dtype = "bool")#candidate|8179|(208,)|const|bool
call_8177 = relay.TupleGetItem(func_7975_call(relay.reshape(var_8178.astype('float32'), [1, 600]), relay.reshape(const_8179.astype('bool'), [208,]), ), 0)
call_8180 = relay.TupleGetItem(func_7979_call(relay.reshape(var_8178.astype('float32'), [1, 600]), relay.reshape(const_8179.astype('bool'), [208,]), ), 0)
func_579_call = mod.get_global_var('func_579')
func_582_call = mutated_mod.get_global_var('func_582')
var_8185 = relay.var("var_8185", dtype = "float32", shape = (150,))#candidate|8185|(150,)|var|float32
call_8184 = func_579_call(relay.reshape(var_8185.astype('float32'), [10, 15, 1]))
call_8186 = func_579_call(relay.reshape(var_8185.astype('float32'), [10, 15, 1]))
const_8206 = relay.const([[[-4,3,-2,-8,5,10,3,10,4,-6,6]]], dtype = "uint8")#candidate|8206|(1, 1, 11)|const|uint8
bop_8207 = relay.greater_equal(call_8158.astype('bool'), const_8206.astype('bool')) # shape=(1, 1, 11)
bop_8210 = relay.greater_equal(call_8159.astype('bool'), const_8206.astype('bool')) # shape=(1, 1, 11)
bop_8217 = relay.minimum(call_8184.astype('int32'), call_8177.astype('int32')) # shape=(10, 15, 300)
bop_8220 = relay.minimum(call_8186.astype('int32'), call_8180.astype('int32')) # shape=(10, 15, 300)
func_7489_call = mod.get_global_var('func_7489')
func_7495_call = mutated_mod.get_global_var('func_7495')
var_8226 = relay.var("var_8226", dtype = "float32", shape = (9, 4))#candidate|8226|(9, 4)|var|float32
const_8227 = relay.const([[-6,-4],[-9,-1],[2,-3],[-3,10],[-4,-2],[2,5],[-5,-2],[-10,-6],[5,7],[6,7],[6,-7],[-10,3],[-5,-3],[2,9],[-10,10],[1,6],[-5,10],[-1,-1],[6,5],[4,-10],[-7,-8],[-4,8],[7,-5],[5,-4],[4,-6],[-10,1],[-5,-4],[4,-8],[10,10],[2,-9],[10,-7],[5,7],[-5,4],[10,-5],[-2,3],[-4,9]], dtype = "uint8")#candidate|8227|(36, 2)|const|uint8
var_8228 = relay.var("var_8228", dtype = "uint8", shape = (500,))#candidate|8228|(500,)|var|uint8
call_8225 = relay.TupleGetItem(func_7489_call(relay.reshape(var_8226.astype('float32'), [36,]), relay.reshape(const_8227.astype('uint8'), [72,]), relay.reshape(call_8158.astype('uint8'), []), relay.reshape(var_8228.astype('uint8'), [10, 5, 10]), ), 4)
call_8229 = relay.TupleGetItem(func_7495_call(relay.reshape(var_8226.astype('float32'), [36,]), relay.reshape(const_8227.astype('uint8'), [72,]), relay.reshape(call_8158.astype('uint8'), []), relay.reshape(var_8228.astype('uint8'), [10, 5, 10]), ), 4)
bop_8240 = relay.not_equal(var_8228.astype('bool'), call_8158.astype('bool')) # shape=(500,)
bop_8243 = relay.not_equal(var_8228.astype('bool'), call_8159.astype('bool')) # shape=(500,)
output = relay.Tuple([var_8178,const_8179,var_8185,bop_8207,bop_8217,call_8225,var_8226,const_8227,bop_8240,])
output2 = relay.Tuple([var_8178,const_8179,var_8185,bop_8210,bop_8220,call_8229,var_8226,const_8227,bop_8243,])
func_8254 = relay.Function([var_8178,var_8185,var_8226,var_8228,], output)
mod['func_8254'] = func_8254
mod = relay.transform.InferType()(mod)
var_8255 = relay.var("var_8255", dtype = "float32", shape = (600,))#candidate|8255|(600,)|var|float32
var_8256 = relay.var("var_8256", dtype = "float32", shape = (150,))#candidate|8256|(150,)|var|float32
var_8257 = relay.var("var_8257", dtype = "float32", shape = (9, 4))#candidate|8257|(9, 4)|var|float32
var_8258 = relay.var("var_8258", dtype = "uint8", shape = (500,))#candidate|8258|(500,)|var|uint8
output = func_8254(var_8255,var_8256,var_8257,var_8258,)
func_8259 = relay.Function([var_8255,var_8256,var_8257,var_8258,], output)
mutated_mod['func_8259'] = func_8259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7845_call = mod.get_global_var('func_7845')
func_7847_call = mutated_mod.get_global_var('func_7847')
call_8288 = relay.TupleGetItem(func_7845_call(), 0)
call_8289 = relay.TupleGetItem(func_7847_call(), 0)
output = call_8288
output2 = call_8289
func_8292 = relay.Function([], output)
mod['func_8292'] = func_8292
mod = relay.transform.InferType()(mod)
output = func_8292()
func_8293 = relay.Function([], output)
mutated_mod['func_8293'] = func_8293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8292_call = mod.get_global_var('func_8292')
func_8293_call = mutated_mod.get_global_var('func_8293')
call_8297 = func_8292_call()
call_8298 = func_8292_call()
output = call_8297
output2 = call_8298
func_8306 = relay.Function([], output)
mod['func_8306'] = func_8306
mod = relay.transform.InferType()(mod)
mutated_mod['func_8306'] = func_8306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8306_call = mutated_mod.get_global_var('func_8306')
call_8307 = func_8306_call()
output = call_8307
func_8308 = relay.Function([], output)
mutated_mod['func_8308'] = func_8308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_8376 = relay.TupleGetItem(func_7413_call(), 1)
call_8377 = relay.TupleGetItem(func_7415_call(), 1)
func_5331_call = mod.get_global_var('func_5331')
func_5337_call = mutated_mod.get_global_var('func_5337')
var_8386 = relay.var("var_8386", dtype = "float64", shape = (216,))#candidate|8386|(216,)|var|float64
const_8387 = relay.const([-2.796331,-3.706120,-3.916987,5.510092,1.896210,-6.618384,-8.096153,-3.739465,-5.912620,0.257547,2.978098,1.189632,-3.220592,1.448117,9.732131,-7.555765,1.346543,5.403957,0.993651,-9.205394,-9.299227,-0.987806,-3.509163,6.877238,1.939370,9.325774,5.687444,6.082910,7.289854,5.015117,-6.948958,1.307048,-8.345833,2.745512,5.260502,-5.860571], dtype = "float32")#candidate|8387|(36,)|const|float32
var_8388 = relay.var("var_8388", dtype = "bool", shape = (208,))#candidate|8388|(208,)|var|bool
const_8389 = relay.const(-1, dtype = "uint8")#candidate|8389|()|const|uint8
call_8385 = relay.TupleGetItem(func_5331_call(relay.reshape(var_8386.astype('float64'), [9, 3, 8]), relay.reshape(const_8387.astype('float32'), [36,]), relay.reshape(var_8388.astype('bool'), [208,]), relay.reshape(const_8389.astype('uint8'), []), ), 0)
call_8390 = relay.TupleGetItem(func_5337_call(relay.reshape(var_8386.astype('float64'), [9, 3, 8]), relay.reshape(const_8387.astype('float32'), [36,]), relay.reshape(var_8388.astype('bool'), [208,]), relay.reshape(const_8389.astype('uint8'), []), ), 0)
output = relay.Tuple([call_8376,call_8385,var_8386,const_8387,var_8388,const_8389,])
output2 = relay.Tuple([call_8377,call_8390,var_8386,const_8387,var_8388,const_8389,])
func_8391 = relay.Function([var_8386,var_8388,], output)
mod['func_8391'] = func_8391
mod = relay.transform.InferType()(mod)
var_8392 = relay.var("var_8392", dtype = "float64", shape = (216,))#candidate|8392|(216,)|var|float64
var_8393 = relay.var("var_8393", dtype = "bool", shape = (208,))#candidate|8393|(208,)|var|bool
output = func_8391(var_8392,var_8393,)
func_8394 = relay.Function([var_8392,var_8393,], output)
mutated_mod['func_8394'] = func_8394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8089_call = mod.get_global_var('func_8089')
func_8090_call = mutated_mod.get_global_var('func_8090')
call_8419 = func_8089_call()
call_8420 = func_8089_call()
func_7489_call = mod.get_global_var('func_7489')
func_7495_call = mutated_mod.get_global_var('func_7495')
var_8443 = relay.var("var_8443", dtype = "float32", shape = (36,))#candidate|8443|(36,)|var|float32
const_8444 = relay.const([-8,9,-3,7,1,-2,3,-5,-8,5,1,8,3,8,-5,1,7,5,8,-9,9,8,-3,-8,7,1,-9,10,8,3,4,-7,1,-2,-7,-10,2,-10,-10,6,-4,-7,-9,-6,4,10,-1,-8,2,3,-3,-6,2,-2,6,4,-6,-2,-6,1,6,-8,2,-1,-8,-4,9,7,-7,8,6,3], dtype = "uint8")#candidate|8444|(72,)|const|uint8
var_8445 = relay.var("var_8445", dtype = "uint8", shape = ())#candidate|8445|()|var|uint8
const_8446 = relay.const([[4,8,5,-8,1,-1,-6,-9,-6,8,7,7,7,9,5,-5,-9,10,-10,2,10,2,2,-10,-10,-4,-4,10,2,1,7,6,-1,-3,-5,-2,-10,-10,6,1,-10,-2,-7,-8,-4,-6,-4,-10,-9,4],[7,10,10,2,-1,3,9,6,10,2,-2,6,3,9,-8,-7,-8,-4,8,-6,8,-8,7,-2,-9,-2,5,7,5,-9,8,7,4,8,-7,10,-6,-4,-4,1,-1,4,-2,-3,6,7,7,-2,7,-10],[6,2,10,-4,-2,-8,7,-8,-1,-5,2,-1,-8,-7,-4,-9,-9,-10,-7,-1,-9,-2,1,5,-3,-10,-6,4,-5,1,10,-8,3,7,-4,8,9,10,-2,-3,7,9,-2,9,4,7,-10,-2,-4,-2],[7,-10,10,8,6,8,-3,-9,10,4,-8,7,-5,2,9,-8,3,-5,-9,-6,2,-2,-3,-2,1,-8,-7,8,5,1,-3,10,-6,-9,-8,2,1,7,-7,6,6,-8,10,-5,5,8,-7,-1,5,-10],[9,5,7,3,-2,3,-4,1,6,-6,3,6,4,5,-9,2,-8,-7,10,3,10,2,-7,-5,-10,-2,7,-7,3,-8,-6,10,7,2,-5,9,-1,7,-5,-8,5,2,-6,-3,-8,3,3,-1,-9,8],[-6,-9,-10,-4,3,2,10,2,-2,6,7,-7,1,1,-8,3,-3,-2,3,8,6,3,-3,-3,-1,-6,-8,-9,8,8,6,-2,8,-4,10,4,-3,1,2,-2,2,-1,2,9,9,-7,-3,-6,5,-9],[-3,8,-9,-1,-4,6,-2,8,9,5,7,5,-3,8,-2,-2,9,10,-10,3,-5,-1,9,2,-9,8,-10,-5,-5,-2,9,3,-3,-9,5,6,4,8,9,1,-8,3,3,5,-10,-6,-9,10,-1,5],[-3,-5,-10,-8,4,8,-8,4,-8,1,3,8,6,6,-7,5,-5,4,-5,6,-4,3,-3,5,-3,-9,4,2,3,9,-10,9,3,1,-8,7,-1,-5,-7,-8,-7,-9,-4,2,1,-9,-4,-6,-4,4],[8,-3,4,-5,-10,-9,2,9,9,5,-1,-10,-3,-3,-7,-8,-10,4,-10,-5,4,9,-4,-1,-10,-4,1,7,4,10,8,-6,8,2,-3,-8,3,-2,-6,1,-1,8,-10,-5,-6,6,10,2,-6,-8],[3,5,-3,-2,-1,-6,9,4,10,4,2,-8,3,-2,6,5,6,-5,8,10,4,2,10,3,-3,6,6,-10,5,6,-2,3,3,-6,9,10,2,7,6,-3,-6,6,4,10,8,5,9,7,-5,-4]], dtype = "uint8")#candidate|8446|(10, 50)|const|uint8
call_8442 = relay.TupleGetItem(func_7489_call(relay.reshape(var_8443.astype('float32'), [36,]), relay.reshape(const_8444.astype('uint8'), [72,]), relay.reshape(var_8445.astype('uint8'), []), relay.reshape(const_8446.astype('uint8'), [10, 5, 10]), ), 0)
call_8447 = relay.TupleGetItem(func_7495_call(relay.reshape(var_8443.astype('float32'), [36,]), relay.reshape(const_8444.astype('uint8'), [72,]), relay.reshape(var_8445.astype('uint8'), []), relay.reshape(const_8446.astype('uint8'), [10, 5, 10]), ), 0)
output = relay.Tuple([call_8419,call_8442,var_8443,const_8444,var_8445,const_8446,])
output2 = relay.Tuple([call_8420,call_8447,var_8443,const_8444,var_8445,const_8446,])
func_8449 = relay.Function([var_8443,var_8445,], output)
mod['func_8449'] = func_8449
mod = relay.transform.InferType()(mod)
mutated_mod['func_8449'] = func_8449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8449_call = mutated_mod.get_global_var('func_8449')
var_8451 = relay.var("var_8451", dtype = "float32", shape = (36,))#candidate|8451|(36,)|var|float32
var_8452 = relay.var("var_8452", dtype = "uint8", shape = ())#candidate|8452|()|var|uint8
call_8450 = func_8449_call(var_8451,var_8452,)
output = call_8450
func_8453 = relay.Function([var_8451,var_8452,], output)
mutated_mod['func_8453'] = func_8453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7630_call = mod.get_global_var('func_7630')
func_7631_call = mutated_mod.get_global_var('func_7631')
call_8677 = relay.TupleGetItem(func_7630_call(), 0)
call_8678 = relay.TupleGetItem(func_7631_call(), 0)
func_5133_call = mod.get_global_var('func_5133')
func_5137_call = mutated_mod.get_global_var('func_5137')
const_8689 = relay.const([-6,3,-3,3,-4,2,-2,-7,4,3,1,-9,10,-2,5,-5,2,2,-10,9,-4,7,7,5,5,5,7,-4,-3,2,-4,6,-6,3,3,-1,-10,5,4,9,9,7,10,-2,8,9,-2,9,-7,-3,-2,-9,5,-10,-3,8,4,9,7,-7,7,6,-4,7,-5,2,-7,10,5,10,-8,2,-4,-8,-4,3,-2,1,3,-7,-10,-6,10,-10,-3,-4,9,-4,9,-3,6,2,-6,-4,-3,-5,-10,4,6,-4,4,-1,4,-7,7,5,7,-1,-2,-2,-4,2,10,3,-9,5,4,10,1,-10,9,-2,-3,-1,-8,2,2,7,9,7,4,3,8,-6,3,7,-1,10,4,1,-6,3,8,-1,-9,-6,2,10,3,9,4,-7,5,-9,1,-10,-4,7,4,-8,8,-5,-3,10,-3,-3,-5,1,8,-10,1,-7,4,8,4,10,-2,-4,-9,5,5,10,8,3,-3,-8,4,1,1,-7,-9,-9,-1,-8,-1,-4,-10,-8,6,-8,-4,-3,-2,-6,8,-8,-10,8,1,-2,10,9,-8,10,-6,-3,5,-7,-2,9,-6,-7,-3,-8,2,9,5,3,2,-7,4,-9,8,7,2,-10,-3,7,-5,-2,-4,-10,-8,-2,8,1,1,-4,-9,-7,-7,9,7,7,10,8,10,-1,-10,-1,4,4,-3,2,-9,10,9,5,-5,7,-2,7,4,-2,-3,-5,-2,-2,-7,-6,-3,-2,6,-8,2,6,2,-7,3,1,2,-5,-6,1,9,-2,4,7,-5,-10,-10,-2,2,-9,9,-3,9,-5,-4,10,4,8,-8,-7,-9,10,3,-4,-1,2,-6,-1,2,9,4,9,-3,-3,9,-6,7,10,5,-7,-6,8,-3,-6,-7,-10,8,7,6,4,2,-6,5,-10,-7,-9,-7,6,6,-8,-10,-1,10,10,2,3,-6,-4,2,-3,5,3,-9,-4,2,-7,2,1,-10,8,-6,7,-8,5,6,-1,2,-3,-5,-7,8,-9,3,-2,2,-6,-9,-2,-5,8,-7,-10,-5,9,9,6,9,10,7,7,-10,-8,8,-7,-9,4,-6,-4,-9,-8,6,-8,3,-8,-7,-10,10,7,1,4,-1,-5,-5,5,-1,-2,8,3,7,-2,8,3,-3,9,6,-4,-2,-3,2,-10,-2,-2,-2,4,8,-4,-9,8,9,5,-3,-2,2,1,-3,6,5,8,5,-7,-7,3,7,-7,1,2,5,-8,-9,-2,1,-10,6,-4,-9,7,-1,1,2,-4,3,6,10,-6,2,-3,-6,1,-10,-4,-3,4,-1,-2,4,5,-2,5,4,10,9,-1,6,-6,7,7,3,6,8,-7,3,-10,-3,-6,-6,3,10,8,-5,6,6,-4,7,-1,5,5,-9,5,-10,9,7,-1,5,7,-6,4,6,-1,5,6,-1,9,8,2,-5,1,-2,-1,2,8,10,-9,9,7,-3,3,-6,4,6,-9,4,5,4,2,3,-5,-2,-9,-6,5,1,-1,-2,-10,-10,1,3,-9,-3,5,3,-9,6,-5,6,10,-10,4,-8,2,5,2,-1,-7,4,-10,-3,1,9,-10,6,2,-2,7,1,8,3,6,-2,6,-4,-2,-7,4,9,-9,-5,2,-7,9,-6,-6,6,-3,-6,4,-7,-6,-9,8,-8,4,10,-3,5,-7,-9,-10,-8,3,3,-1,-4,-5,-9,3,-4,1,5,2,-5,10,5,-9,6,4,-1,-2,-4,-8,-1,-2,-1,8,-8,5,9,-7,7,7,10,-3,-6,6,1,5,-8,-7,-2,5,3,-3,-7,-9,8,8,-7,9,-9,3,10,3,7,-6,-3,8,3,10,-2,4,7,8,-6,-5,-1,-4,8,-10,7,3,1,8,3,-1,9,4,9,9,-8,-10,-5,-1,-4,-8], dtype = "int32")#candidate|8689|(728,)|const|int32
const_8690 = relay.const([[4.756550,-9.901900,-4.577245,0.040585,-9.568345,-2.635789],[3.072335,0.549185,-5.002344,3.739586,5.283740,-6.822716],[-1.275664,6.027849,2.032437,-4.871738,6.052153,-1.562328],[2.154116,-6.582970,-9.484762,-8.120640,4.763433,8.614352],[9.692964,-3.098707,-2.983332,9.215546,-8.276256,-7.803016],[6.947001,-3.077084,9.173099,-0.500823,-0.323218,5.812225],[7.713531,8.171634,5.661258,7.183205,4.374508,5.207364],[-3.940524,-1.447935,-9.310505,-3.525414,4.243319,-4.864606],[3.135438,-0.059753,0.127713,-0.669338,5.345924,8.076850],[8.584863,-3.912562,1.614637,-5.594220,-4.140027,-5.043023],[9.158684,-7.939721,-2.478267,-3.063369,4.723216,2.413298],[-6.129852,5.992233,3.102929,-0.764257,3.696261,-8.322077],[4.795175,1.542822,8.318653,-4.210785,-8.215503,-8.933317],[1.346582,3.453001,2.332290,2.690460,-0.857536,1.131952],[-8.647965,-4.939158,-9.391394,-7.603759,-4.256177,0.640403],[2.801814,-2.525936,-2.583509,-0.336568,3.511643,-3.573427],[5.388323,-1.952335,7.614959,7.541607,-9.026122,8.914329],[-3.431946,-9.104795,8.652516,5.406996,4.045589,0.203999],[-9.311576,2.875717,2.113085,-5.947525,7.895252,-5.273824],[-1.131641,-9.332866,-2.356103,-9.846223,6.017087,0.612760],[-5.104460,-8.272923,-8.277971,-4.299018,9.040364,4.069585],[8.570329,5.492722,-0.760768,2.804567,-3.371220,0.764854],[-3.673848,2.101095,-2.234244,-1.891384,6.302012,-2.119033],[-4.052860,-3.223968,-7.809922,-5.952846,5.270553,3.525361],[-8.870480,3.772357,-6.494123,5.612391,-3.559103,1.763818]], dtype = "float32")#candidate|8690|(25, 6)|const|float32
call_8688 = relay.TupleGetItem(func_5133_call(relay.reshape(const_8689.astype('int32'), [4, 14, 13]), relay.reshape(const_8690.astype('float32'), [25, 6]), ), 2)
call_8691 = relay.TupleGetItem(func_5137_call(relay.reshape(const_8689.astype('int32'), [4, 14, 13]), relay.reshape(const_8690.astype('float32'), [25, 6]), ), 2)
uop_8699 = relay.sinh(call_8688.astype('float64')) # shape=(25, 6)
uop_8701 = relay.sinh(call_8691.astype('float64')) # shape=(25, 6)
output = relay.Tuple([call_8677,const_8689,const_8690,uop_8699,])
output2 = relay.Tuple([call_8678,const_8689,const_8690,uop_8701,])
func_8711 = relay.Function([], output)
mod['func_8711'] = func_8711
mod = relay.transform.InferType()(mod)
mutated_mod['func_8711'] = func_8711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8711_call = mutated_mod.get_global_var('func_8711')
call_8712 = func_8711_call()
output = call_8712
func_8713 = relay.Function([], output)
mutated_mod['func_8713'] = func_8713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_8761 = func_7228_call()
call_8762 = func_7228_call()
func_7777_call = mod.get_global_var('func_7777')
func_7780_call = mutated_mod.get_global_var('func_7780')
const_8775 = relay.const([9,-2,6,-6,-1,-6,3,-1,-6,10,9,6,4,6,-5,-7,4,9,1,6,4,-1,3,5,10,-5,-3,-5,-4,4,9,6,-3,3,2,7,1,-5,1,2,-7,10,-10,10,-9,-5,-8,-2,-6,2,-4,6,-9,10,10,1,10,9,8,4,-4,6,10,10,2,-5,-2,-4,9,9,7,-9], dtype = "uint8")#candidate|8775|(72,)|const|uint8
const_8776 = relay.const([7,-9,-9,-9,-4,4,4,9,2,10,2,-1,1,3,3,9,-7,10,-3,2,6,3,-2,9,4,2,-1,9,9,3,7,-1,-2,2,-9,-3,10,7,8,8,5,8,-2,-9,8,-2,-6,9,5,-3,8,1,4,2,4,-4,9,-7,10,2,8,4,9,1,-7,-10,2,2,9,-10,1,4,-7,-1,-8,4,6,-1,-1,1,-1,-2,-2,1,-6,6,4,-9,4,-7,-2,-10,10,5,6,-9,5,-9,6,10,-10,1,-8,-4,-10,-5,-1,5,8,3,4,-2,5,-7,3,3,6,5,4,-8,-10,9,2,3,3,-6,1,-7,-9,-9,4,4,-8,7,10,-6,-10,2,-10,2,4,-10,5,-3,-4,5,-6,1,9,6,3,10,1,-7,-10,6,-6,8,6,6,-4,9,9,6,7,-9,-5,4,-2,7,-10,5,9,-9,-5,-6,-5,10,4,4,-7,-2,2,8,-6,6,-6,-4,-2,-2,8,-7,3,-7,-3,-8,3,-3,-5,9,-6,9,-3,8,8,4,8,-10,-9,9,9,-4,-7,-7,8,6,-8,7,-10,1,-7,-5,-4,-7,2,-5,-3,-1,-6,7,-4,-9,9,-6,-2,-6,-1,3,4,10,-6,-4,6,1,6,7,10,2,3,-8,-4,4,-3,-1,-5,-2,-6,9,-6,3,10,-1,9,10,1,6,2,1,7,4,-4,2,-5,-3,3,2,-7,4,6,7,3,5,3,3,-9,-3,-5,5,6,-2,4,-4,1,-7,3,-4,-7,-6,-6,-2,7,-10,-8,6,-2,7,-6,-7,1,4,5,-2,9,-5,-8,2,10,-10,6,6,-6,-4,-6,-9,-4,-10,-1,3,10,-4,5,-6,7,-7,5,3,-6,4,-9,-8,-6,-3,-1,-4,4,-1,-6,-6,-6,10,-6,-1,-9,6,-9,-10,-3,9,-1,4,3,-6,4,-3,-5,-10,-5,7,7,3,-8,-9,10,-2,3,6,-3,6,-4,-6,4,-4,-8,-7,4,10,-7,-2,9,5,2,-9,-4,2,7,-1,-5,-4,-5,9,10,-1,10,-1,-7,-4,-8,4,9,-1,4,-9,-6,4,-3,9,2,-2,3,-3,2,9,-10,3,9,-8,-6,1,-10,-3,8,8,-2,-2,4,5,-3,-7,7,4,5,-6,9,-3,4,5,8,4,4,6,3,5,6,-1,-3,7,-7,9,4,-8,-7,-2,6,6,-2,-9,6,3,9,4,-8,-2,-8,4,2,-10,-5,-8,8,1,8,5,6,-5,1,-7,-4,6,9,-4,2,-3,-8,-7,5,-8,-8,7,10,-8], dtype = "uint8")#candidate|8776|(500,)|const|uint8
call_8774 = relay.TupleGetItem(func_7777_call(relay.reshape(const_8775.astype('uint8'), [72,]), relay.reshape(const_8776.astype('uint8'), [500,]), ), 4)
call_8777 = relay.TupleGetItem(func_7780_call(relay.reshape(const_8775.astype('uint8'), [72,]), relay.reshape(const_8776.astype('uint8'), [500,]), ), 4)
var_8785 = relay.var("var_8785", dtype = "uint8", shape = (500,))#candidate|8785|(500,)|var|uint8
bop_8786 = relay.less_equal(const_8776.astype('bool'), relay.reshape(var_8785.astype('bool'), relay.shape_of(const_8776))) # shape=(500,)
output = relay.Tuple([call_8761,call_8774,const_8775,bop_8786,])
output2 = relay.Tuple([call_8762,call_8777,const_8775,bop_8786,])
func_8789 = relay.Function([var_8785,], output)
mod['func_8789'] = func_8789
mod = relay.transform.InferType()(mod)
mutated_mod['func_8789'] = func_8789
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8790 = relay.var("var_8790", dtype = "uint8", shape = (500,))#candidate|8790|(500,)|var|uint8
func_8789_call = mutated_mod.get_global_var('func_8789')
call_8791 = func_8789_call(var_8790)
output = call_8791
func_8792 = relay.Function([var_8790], output)
mutated_mod['func_8792'] = func_8792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8089_call = mod.get_global_var('func_8089')
func_8090_call = mutated_mod.get_global_var('func_8090')
call_8817 = func_8089_call()
call_8818 = func_8089_call()
output = call_8817
output2 = call_8818
func_8849 = relay.Function([], output)
mod['func_8849'] = func_8849
mod = relay.transform.InferType()(mod)
output = func_8849()
func_8850 = relay.Function([], output)
mutated_mod['func_8850'] = func_8850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8047_call = mod.get_global_var('func_8047')
func_8048_call = mutated_mod.get_global_var('func_8048')
call_8862 = relay.TupleGetItem(func_8047_call(), 0)
call_8863 = relay.TupleGetItem(func_8048_call(), 0)
func_7579_call = mod.get_global_var('func_7579')
func_7585_call = mutated_mod.get_global_var('func_7585')
const_8867 = relay.const([True,False,True,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False], dtype = "bool")#candidate|8867|(208,)|const|bool
const_8868 = relay.const([4.136251,-7.180051,2.096671,3.258505,-9.754494,-4.571244,-4.230050,1.743573,-7.546042,-4.913826,0.044235,-3.327370,-7.865984,9.235647,6.433563,0.196060,4.391292,1.788213,3.083836,-5.090668,0.341586,9.077630,-4.766456,3.656773,-7.077411,-3.334593,-8.731769,-2.721841,-0.297804,4.207909,-6.321734,-2.465005,-6.804754,-1.501684,3.957324,3.785552,4.851616,-0.148591,3.265728,-2.851117,7.592963,0.239126,9.812895,-0.397298,-2.051107,8.934211,1.983605,-9.174566,-6.513237,4.238748,1.765924,-0.073785,9.932839,-3.476248,-1.065978,7.370119,1.521405,1.588944,-9.899842,2.612830,8.699672,4.794065,-5.635036,-3.563431,-4.163376,-9.537203,-5.238263,-7.813571,7.644101,-6.492084,-0.792476,-7.167309,3.496688,-4.429733,9.994248,-8.824128,2.128541,8.098646,7.307335,-2.636980,-7.237645,2.491991,8.154101,-9.353570,-9.064587,-5.710230,-6.773890,-1.654648,-9.192135,2.594346,-4.829256,1.483303,8.635088,-8.092104,-2.939072,-8.384739,4.085449,-5.483076,-2.360471,-0.258657,9.975839,1.973652,9.978159,1.999625,-9.008036,3.249320,-3.311240,-0.926563,-1.730160,-8.584397,6.571227,2.439581,-3.935225,5.517294,-5.188524,7.187412,-2.647450,-5.219388,6.584976,-5.100351,-6.065698,-6.498917,-7.370982,9.353662,4.528556,3.632884,-7.173629,-0.557238,-3.330045,5.669375,7.176340,6.697497,0.467232,1.278064,8.372137,9.323691,4.716082,9.893045,-1.594144,-6.768471,-7.830203,7.228297,-1.371571,-3.567517,6.003843,-3.809757,-1.315635,1.260883,7.800651,-8.192326,-4.525773,-2.662923,-3.210610,3.047873,-7.151339,-8.847899,4.591491,-0.974732,2.195161,8.989763,-6.671601,3.816891,6.662965,4.446115,2.631816,7.018168,2.971863,-2.796997,8.006959,-8.073717,4.093193,3.170347,-4.370284,6.653445,-2.090329,2.187953,-3.508511,6.411003,7.082224,-2.887928,2.513697,-3.434305,0.421864,-9.038623,-1.354773,6.084327,4.909989,-2.317139,-8.251090,-4.901859,-5.012420,6.092932,-3.047491,-6.701752,0.633514,7.037744,6.761101,8.507992,-9.109681,5.501129,2.566140,-0.745558,1.841080,-1.651875,-7.756712,-2.120458,-4.652354,6.562474,4.993936,-8.612324,-8.083126,8.516156,3.789965,1.204826,-6.001871,-4.085326,4.365375,-4.761299,-2.965279,-9.847288,3.433496,3.542899,-4.731011,3.195497,8.588470,1.266734,3.284564,4.073634,8.223897,-1.655722,0.489857,1.875542,7.941245,-9.852376,4.321295,6.218377,0.522229,-0.211537,7.255099,3.544866,-6.172233,6.967281,5.207456,-4.791866,8.028527,-2.263035,-3.820661,2.944625,-2.223939,5.522465,-6.895377,-1.924263,9.555746,0.648646,-4.717301,5.601472,7.189410,-6.518867,7.256545,-1.496080,7.180698,-3.403844,-6.522882,-7.302370,9.151933,-0.303172,-8.444774,8.228175,-2.833979,-1.592184,-5.340569,3.302603,-5.837487,-7.076295,-1.270206,-4.493368,-3.816748,3.606656,-0.154945,5.173118,4.467259,4.985268,-7.761426,-0.661515,-7.329639,-9.958535,-9.986492,-6.125498,1.212312,6.761362,9.425126,-7.538995,-7.084676,4.248630,1.068478,-6.254910,-4.196233,-2.261323,-9.691992,1.230468,5.398667,8.356084,4.161549,5.643636,5.595356,8.005669,-4.828161,-0.184877,7.619859,-4.646102,-9.807770,-1.857736,-6.183558,1.990402,6.031145,7.014113,-9.046364,-7.819799,0.455590,7.075216,-0.923803,9.581415,-9.433128,7.765627,7.538135,-4.425255,-8.081536,6.602076,5.346240,-3.199860,3.064574,0.301682,-1.225976,-5.114966,7.436601,-3.098828,-0.730417,0.913281,1.666184,-6.585683,-0.747845,-4.094361,6.660155,9.803117,5.393873,9.253397,-1.568716,-3.143270,3.846118,-5.707275,-5.772967,-1.784302,-0.942668,8.998069,1.668942,1.947349,-4.940449,-8.260464,9.339919,-0.844799,9.484393,2.944577,3.522881,5.438850,-4.485420,2.192420,-6.134391,8.332107,8.443350,3.929149,4.781736,-6.761654,-5.040101,1.054482,9.766683,-8.867651,-2.081527,-7.245996,-1.670598,-8.960142,7.143515,6.497447,9.308121,-2.026957,-6.222265,2.751463,-9.253058,4.412472,3.574468,-4.348859,8.493051,2.769095,3.963042,0.566237,4.425454,-9.064797,9.057473,1.214752,5.222656,-7.142284,8.404356,6.841738,9.608446,-8.449901,7.078277,6.205861,-3.407158,-2.178021,-0.983422,3.580701,9.770109,-1.647517,2.180650,-4.148590,-1.085822,-1.672134,-6.760549,9.197018,8.127517,-6.698997,4.518408,3.186946,8.043644,4.608547,9.016662,9.205649,-2.639570,0.440972,0.107314,-0.513488,-4.259519,9.454406,-7.687740,8.459752,7.022471,9.561604,3.620806,-6.939306,-8.761701,1.811363,-3.136881,4.030757,-0.760841,-7.404140,-3.688504,3.129116,-2.181246,1.334927,-0.365052,-0.485324,4.610534,-3.156850,-1.265357,9.876612,-4.442779,-8.495920,9.903353,7.575053,-2.730180,-5.336358,1.668775,-2.747765,-2.882481,-5.602359,-9.844019,-8.907653,-3.588964,-1.349436,7.475142,-0.090790,-5.064209,-0.692482,-3.039011,-6.418727,-9.064638,1.038321,-7.521327,8.145715,8.075566,4.557626,-6.697749,0.766828,-1.993243,1.291025,3.642419,0.117857,-4.606853,-2.580749,-2.877446,0.032905,6.730402,-7.390232,-7.626923,-2.224629,1.005751,4.775510,-2.289915,3.208556,3.862838,-0.536498,-7.603712,-2.346787,-6.561031,1.425408,6.592674,2.595417,7.130198,9.508289,1.239096,9.942111,8.446370,-7.140462,-5.159102,0.110767,-6.200744,-2.260874,3.943062,3.748198,5.251236,-0.577125,4.560889,9.034838,0.665950,6.194663,0.666060,-1.535419,9.553150,-1.431754,-6.312818,7.580469,8.336462,9.175200,8.555465,-1.267762,0.206070,5.879222,-6.128084,6.426879,0.445969,-6.806090,9.512152,-6.651279,8.053734,-4.663068,-7.393867,-0.967354,-6.569068,-0.198554,-6.335824,-4.187436,-1.245657,8.270342,8.190547,-0.246588,0.226935,9.712764,3.232230,7.117101,-4.564610,-0.545341,-8.662588,-0.187114,-9.310596,-1.788786,-3.410300,-7.722604,-4.024682,8.124445,-5.936996,1.731828,2.409871,3.446308,-4.850672,0.411249,-9.198016,7.625118,3.673585,4.971205,-2.353592,-6.803117,7.215762,9.248961,-8.612959,3.448347,2.235238,-8.056284,1.594684,0.489575,0.940356,-2.871003,5.181702,-3.768201,3.705665,-9.480442,5.285123,-7.192779,-2.432144,-3.661907,1.864499,6.511857], dtype = "float32")#candidate|8868|(600,)|const|float32
const_8869 = relay.const([False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,True], dtype = "bool")#candidate|8869|(624,)|const|bool
const_8870 = relay.const([[-6.844605],[3.929073],[6.804067],[0.862114],[6.854972],[7.816754],[6.604880],[-9.010370],[3.860033],[8.098128],[7.362188],[4.830388],[-8.639068],[-5.484404],[8.966556],[4.200972],[-6.600274],[9.109318],[-2.285489],[-4.281423],[7.945067],[8.622346],[8.661602],[-8.855931],[-7.111339],[-4.122295],[0.757115],[5.133187],[-6.541240],[-6.101422],[-3.433170],[9.911444],[-7.905865],[-3.612162],[-4.935188],[-6.034372],[2.942293],[-6.102734],[2.189770],[9.295999],[-3.206801],[4.268611],[5.952242],[7.387078],[-4.874109],[6.369782],[-1.311998],[5.341266],[-1.795374],[3.667882],[-7.091692],[-8.350113],[-2.813077],[-2.714332],[-1.797713],[3.714415],[-3.330096],[-1.394754],[9.239230],[5.751231],[7.253064],[-7.238102],[-9.127996],[-4.157449],[9.912713],[7.354960],[2.236491],[9.106642],[-1.209389],[7.791534],[6.440887],[6.713064],[4.595433],[3.581183],[-0.500955],[-9.161142],[-1.845477],[8.452167],[8.430213],[9.583279],[9.050095],[-4.450572],[-4.846412],[-1.324235],[-7.557945],[2.605897],[-5.867455],[3.366147],[-5.339316],[-6.030357],[7.111165],[-8.221101],[8.946168],[-8.082932],[5.646321],[-0.837864],[-5.453720],[5.371034],[-4.425593],[0.932110],[8.008321],[9.592332],[-6.676525],[3.422712],[3.168473],[4.670276],[6.280590],[-5.228110],[1.849133],[0.612628],[-6.799384],[9.919031],[-5.067823],[-4.807746],[1.684218],[2.334530],[-2.923402],[-3.815175],[3.811399],[-3.181805],[-0.406953],[-6.140310],[0.828335],[-1.837382],[3.201170],[-2.759765],[4.119830],[1.226950],[-6.213350],[5.281163],[8.188270],[9.545088],[9.705508],[-3.585653],[2.791399],[6.470454],[-4.842413],[3.863450],[1.527990],[-6.275525],[1.283177],[-9.172077],[5.759399],[9.179481],[0.678720],[2.874236],[9.393757],[3.760962],[-1.311668],[-9.072543],[-4.123208],[0.664210],[6.233556],[-8.227493],[7.532966],[2.964511],[8.842917],[2.868537],[9.694727],[2.500342],[6.562989],[-7.670037],[2.199919],[9.293483],[2.367828],[8.388987],[-6.387382],[4.204030],[-1.523502],[-8.796655],[-8.010638],[-6.758176],[7.503846],[-5.101194],[-1.241524],[-6.305408],[-9.588989],[7.278262],[-0.625690],[-2.337942],[-5.909263],[3.545490],[-8.083970],[-4.919280],[-5.389844],[-5.296071],[-3.699814],[8.464859],[0.724358],[8.399378],[0.378469],[6.549340],[-3.688086],[2.973277],[-0.606169],[-1.501309],[9.919929],[7.446416],[-3.910228],[-5.195994],[-9.929413],[-4.939723],[-0.309820],[-3.127244],[2.809822],[9.932886],[4.335225],[4.904456],[3.484066],[-2.549525],[-2.930541],[-0.344540],[-1.510355],[3.550997],[8.573919],[-7.541059],[5.454225],[2.868460],[-5.593926],[3.110379],[3.733118],[-7.690271],[1.680364],[-2.108062],[-0.618452],[-4.149765],[9.336539],[-0.205404],[-6.641514],[0.512242],[-9.064446],[1.673061],[-2.167063],[7.710470],[6.289498],[-9.764292],[1.503238],[6.939183],[-4.115344],[-7.629448],[9.053395],[7.441702],[2.160322],[-6.539147],[-9.616997],[-8.244026],[8.426594],[-5.820315],[-9.831525],[-5.672755],[-0.712016],[-7.819369],[5.482488],[-9.241129],[1.860094],[-0.062020],[-9.160583],[4.632972],[-9.077261],[2.712100],[5.002838],[3.753218],[-0.839474],[-7.596076],[4.425833],[-6.404171],[-4.436037],[7.338539],[-6.549864],[9.701464],[-8.055393],[-1.757927],[-7.546517],[6.737186],[-9.778728],[9.828399],[-8.512761],[-4.740279],[-7.913120],[1.069778],[-8.685841],[1.660716],[-6.074588],[-5.966815],[-6.217187],[-6.010233],[-4.654397],[7.604384],[-0.122959],[7.950394],[-8.361693],[1.432425],[5.974946],[8.092617],[-7.671916],[0.834363],[-0.091145],[3.040183],[0.109088],[0.508545],[-3.949117],[4.842986],[2.159697],[0.539289],[4.896700],[-3.773506],[6.981426],[-0.203269],[3.720253],[-9.146675],[-5.866097],[-0.223130],[-0.548569],[5.854735],[-2.762624],[9.821198],[-6.938580],[5.113060],[-3.856179],[3.036891],[0.739092],[8.297216],[8.309590],[1.271916],[1.822003],[4.032047],[1.757707],[-7.832413],[7.249793],[1.601149],[-4.370601],[-0.632310],[6.945585],[-4.418076],[-8.609567],[6.422014],[1.844974],[-1.275414],[-2.453488],[-9.704601],[3.743769],[2.905647],[7.177735],[-8.538771],[5.398343],[-9.680278],[0.129647],[-4.513355],[-9.400808],[-2.306391],[5.920427],[-4.142972],[-3.818506],[7.726913],[-6.783044],[-6.527318],[4.006054],[-8.242206],[3.516176],[-3.926239],[2.098375],[-2.194541],[9.488104],[6.960411],[-0.927345],[2.089079],[-2.856686],[-9.001794],[-6.378484],[0.526270],[5.590586],[8.304224],[-2.172735],[-9.945204],[-9.163803],[-8.690606],[9.389530],[-5.017316],[-8.489294],[8.629087],[6.119907],[-8.754333],[-0.762769],[-7.886320],[-9.793243],[-8.070949],[0.686236],[6.685251],[0.415235],[5.699254],[-2.976253],[2.759716],[7.901551],[-9.819320],[-3.822938],[-3.203223],[-2.344343],[5.882006],[3.235992],[-0.729374],[6.375024],[-7.003654],[-8.770782],[-0.696211],[6.089222],[2.840830],[-9.980545],[5.149018],[3.426159],[8.549570],[9.059153],[1.414895],[-3.252448],[4.620010],[2.958030],[3.160297],[-3.141706],[5.563163],[6.113074],[-6.753457],[-1.329384],[-5.623977],[7.702483],[-0.303912],[-1.179371],[-0.731199],[6.290995],[7.346866],[-8.043975],[3.866890],[-8.777196],[-9.086220],[-0.121128],[8.913686],[-6.866834],[-7.833904],[-5.381454],[2.152135],[4.732357],[-8.672571],[9.629885],[1.285640],[-6.610370],[-2.204067],[6.222793],[-9.944725],[-3.437033],[-9.698372],[8.677247],[9.956724],[-0.529666],[-8.779004],[-5.215669],[-9.274610],[1.102637],[7.456175],[7.214123],[6.513942],[-9.424060],[-6.608050],[8.430055],[5.238781],[6.121311],[6.079916],[-2.804844],[-3.636380],[-8.035933],[6.482459],[-9.271892],[-5.627385],[-8.994941],[-7.142894],[0.867785],[4.941335],[3.753513],[3.665140],[9.521871],[5.441808],[1.291353],[4.047320],[8.089042],[-2.492340],[-0.789598],[-4.978271],[8.529150],[-9.484543],[0.461366],[4.232773],[-0.479087],[-9.852753],[-6.624292],[-0.391237],[-1.239967],[-9.349435],[-7.640542],[1.181570],[-5.850674],[-3.315805],[6.695059],[0.842655],[9.265582],[-2.771197],[2.521129],[5.303473],[7.047728],[3.511271],[-3.694462],[5.997231],[9.114119],[-9.612306],[0.179442],[5.555435],[9.168268],[-3.054623],[9.071064],[3.669931],[6.815944],[2.436245],[3.747769],[-0.294012],[-7.822194],[-4.556662],[8.226159],[7.115121],[3.137422],[0.109866],[-3.461901],[-7.092034],[-7.267073],[-4.573074],[8.356415],[-1.442282],[-2.028347],[8.733342],[3.071081],[-5.664258],[1.207315],[-8.833226],[-7.459397],[-3.374173],[9.529290],[-9.064092],[-1.031692],[6.921861],[9.663663],[-2.580176],[4.159344],[9.193293],[-4.129421],[1.490849],[-1.436974],[2.934051],[-6.385527],[-1.784868],[-5.492286],[-4.431647],[-9.903267],[1.979030],[-4.600694],[7.392678],[-6.223053],[-5.570219],[1.075348],[7.258680],[-6.216836],[7.962382],[-7.715459],[-8.483632],[-8.055892],[4.437399],[2.800204],[-1.278103],[-9.556533],[2.932066],[-6.631583],[-9.028439],[-7.186050],[-4.725917],[-4.594806],[-4.840127],[-5.112034],[0.691241],[-4.815314],[2.534928],[8.456992],[6.252290],[-4.951424],[-0.539469],[1.871575],[2.223060],[8.880891],[0.211805],[-3.132153],[0.579247],[3.745552],[5.214764],[9.735806],[2.325173],[1.017013],[-9.232192],[7.506243],[8.807208],[1.582709],[1.182519],[7.161843],[-8.377003],[-7.870793],[6.657337],[1.783364],[-9.280266],[-5.397557],[-3.153424],[-8.572125],[7.060921],[-7.392618],[-2.672319],[-7.179610],[5.736008],[-6.939174],[-8.513150],[-5.260585],[-6.874192],[-2.714882],[9.072124],[-8.131680],[8.110512],[-0.570886],[-0.180404],[1.935587],[-5.554148],[4.845467],[5.383652],[-7.790181],[7.813511],[3.028311],[1.034854],[-1.951567],[5.318288],[5.104922],[-5.067329],[-2.713680],[-0.747680],[3.742432],[3.381603],[-5.777616],[-5.470741],[5.701430],[8.796732],[-1.850914],[-2.603866],[5.680051],[6.344705],[7.952360],[-8.773084],[-1.664584],[-8.250233],[-7.316147],[8.337983],[4.629864],[-4.366133],[-6.236263],[7.496600],[7.757020],[3.778672],[0.162702],[2.403797],[5.456116],[-3.694495],[6.101793],[7.720910],[1.556316],[-1.910241],[-3.567750],[0.705159],[3.521385],[-4.218074],[-4.393031],[2.054856],[-2.179050],[3.163661],[-4.536246],[-5.846397],[-4.130312],[-4.342577],[-8.202659],[9.361381],[9.426742],[1.006377],[4.359147],[5.434236],[0.216976],[-8.912831],[0.722532],[9.671689],[-1.584941],[7.787308],[9.215496],[0.769530],[-4.615563],[-5.411975],[2.479382],[-1.598775],[2.250679],[6.648613],[-6.955095],[7.271369],[-3.911758],[6.699347],[4.950215],[6.850415],[3.441884],[-5.177138],[7.536577],[-5.234740],[7.708686],[-8.499362],[-3.934022],[4.307616],[-2.342930],[-2.887181]], dtype = "float32")#candidate|8870|(720, 1)|const|float32
call_8866 = relay.TupleGetItem(func_7579_call(relay.reshape(const_8867.astype('bool'), [208,]), relay.reshape(const_8868.astype('float32'), [2, 300]), relay.reshape(call_8862.astype('uint16'), [300,]), relay.reshape(const_8869.astype('bool'), [624,]), relay.reshape(const_8870.astype('float32'), [720,]), ), 5)
call_8871 = relay.TupleGetItem(func_7585_call(relay.reshape(const_8867.astype('bool'), [208,]), relay.reshape(const_8868.astype('float32'), [2, 300]), relay.reshape(call_8862.astype('uint16'), [300,]), relay.reshape(const_8869.astype('bool'), [624,]), relay.reshape(const_8870.astype('float32'), [720,]), ), 5)
uop_8883 = relay.sin(call_8866.astype('float32')) # shape=(18, 2)
uop_8885 = relay.sin(call_8871.astype('float32')) # shape=(18, 2)
func_579_call = mod.get_global_var('func_579')
func_582_call = mutated_mod.get_global_var('func_582')
const_8887 = relay.const([-8.518436,4.442830,-9.264459,-9.150180,-1.088911,-9.944034,6.925085,4.532981,5.183301,7.123088,-3.923460,0.273353,4.468054,-3.764610,6.519762,5.426420,-1.335842,2.287331,9.611900,0.802128,9.251660,-7.709620,1.311371,-4.912422,-2.827850,-4.796586,3.614176,9.653453,6.539412,6.622328,9.348682,-9.505064,-2.644381,7.782791,0.172619,4.902579,-9.090077,4.118961,-6.302747,-0.621096,2.662246,1.270484,-2.289505,-8.308408,-2.383313,7.805688,-9.687186,7.234188,1.256274,5.391070,-5.519348,7.859497,-1.363888,-2.288197,4.386751,7.593663,7.009548,4.240100,-1.987084,8.270506,-6.656317,-1.468438,-5.061890,5.796096,-1.344705,-4.600556,6.927155,-9.755672,0.965827,-7.176713,2.727322,2.158370,8.560412,4.341863,-1.654244,-8.319275,2.106675,-8.220801,2.241262,6.153475,-4.694312,-2.902189,-9.987933,7.935971,7.528973,-8.294568,5.636175,9.517574,-1.724044,-8.316096,-6.172502,1.111077,-3.289123,8.553651,3.245993,8.814900,8.552549,-2.871535,-2.257135,6.452805,8.257996,4.777104,4.164230,3.389470,2.156379,1.829719,1.576395,9.034879,-8.153672,1.879549,6.835311,4.933764,-6.646741,-4.916939,8.300317,-3.040188,0.784795,2.622671,-4.490095,7.052648,4.799591,8.882985,6.625290,-3.194429,-8.033603,-5.371292,-1.553220,-9.215975,4.116702,-3.992501,-2.346026,7.125960,-8.525621,-0.863252,-5.230007,-8.820480,-3.809600,-3.686103,-7.864299,8.198590,-8.927329,-9.124461,9.567481,4.685474,-6.353127,8.654484,-0.625006,-0.977176,-1.702942,9.273607], dtype = "float32")#candidate|8887|(150,)|const|float32
call_8886 = func_579_call(relay.reshape(const_8887.astype('float32'), [10, 15, 1]))
call_8888 = func_579_call(relay.reshape(const_8887.astype('float32'), [10, 15, 1]))
func_3055_call = mod.get_global_var('func_3055')
func_3059_call = mutated_mod.get_global_var('func_3059')
const_8890 = relay.const(8.920546, dtype = "float32")#candidate|8890|()|const|float32
const_8891 = relay.const([-9.142075,-5.331579,-3.669414,8.732552,1.703190,-2.851909,-1.160743,-3.273757,7.160564,6.605335,-7.234331,-8.501062,-1.971523,-4.519306,4.041804,-8.317019,9.236619,1.403921,7.322970,3.747609,-6.572608,-3.103941,-2.677608,6.204304,-2.251216,5.695059,-7.324062,-6.241634,5.535197,-6.607887,2.594324,1.501249,9.405705,-3.047025,2.370315,7.851130,4.189222,3.060171,-1.433146,-0.582937,9.972978,5.160085,1.104002,5.994085,1.252206,-7.959160,-6.477283,4.102707,-3.316901,-8.143406,8.455433,-9.329568,6.543098,8.576887,-4.025150,-2.344523,5.528992,9.123235,7.482997,-4.247174,-6.904771,8.026530,-0.871677,-4.462539,-7.775558,-0.793887,-9.072590,3.541042,-1.988512,3.765577,-5.302045,8.220271,-2.201271,-9.936383,8.356851,-2.481047,4.339123,-4.268876,-9.016036,2.177307,4.574168,-9.990353,-1.387919,8.904472,-5.787045,4.728930,8.457544,7.487779,2.765054,9.261562,-1.782108,-5.645569,-5.544554,4.198015,3.434743,8.836275,-2.734992,-5.994431,2.734213,-9.380877,-4.436662,-0.321856,-2.924418,1.068633,-8.554644,-5.296419,-8.173068,-6.087143,8.645007,7.560158,-0.788281,2.549549,2.676005,9.689191,8.586575,-7.123067,9.824223,1.512405,-1.901176,5.486918,-8.065054,2.590308,-5.241879,5.092104,1.077946,-6.834203,5.533067,3.334109,7.434061,-9.409148,-8.595012,1.005848,7.693641,0.890986,1.328953,-8.369442,-3.350306,2.332607,-7.345457,-3.197707,7.059083,7.478738,-8.657634,0.750724,-0.713925,-4.926849,0.718015,-9.342207,4.371861,-2.763372,5.945830,-3.814521,0.835758,-6.368367,-4.069065,2.737721,-5.537594,-9.852041,2.409989,-9.024728,3.859625,-0.433444,-4.356735,-7.610248,-1.848656,6.212291,5.916197,1.300165,9.876149,-2.236670,-2.576139,1.065355,7.645523,0.404767,-7.163842,-7.654503,1.318654,-0.206953,4.841928,0.267969,7.978477,2.044469,-3.093065,5.617278,2.084478,8.050911,-6.295736,-7.716727,-5.402583,-8.628624,4.085990,5.958483,-2.188530,0.837819,-1.975364,3.542804,9.028006,-0.924064,-1.492104,0.610459,-2.248821,8.682061,1.380261,-5.515385,-3.479365,-7.143486,3.329605,-7.379382,2.391592,8.542700,-3.045521,-6.440973,-1.560104,2.102296,-8.301154,-8.881620,1.745181,1.807728,1.977253,-4.137633,2.632344,5.443068,-7.081763,-8.864239,3.703621,2.595000,-9.628097,1.703631,6.146131,2.060090,4.229056,-1.916749,-1.509109,-5.128447,4.770068,3.213051,5.941827,0.158428,-4.464702,-5.289658], dtype = "float32")#candidate|8891|(240,)|const|float32
call_8889 = relay.TupleGetItem(func_3055_call(relay.reshape(const_8890.astype('float32'), []), relay.reshape(const_8891.astype('float32'), [2, 8, 15]), relay.reshape(const_8867.astype('bool'), [2, 104]), ), 4)
call_8892 = relay.TupleGetItem(func_3059_call(relay.reshape(const_8890.astype('float32'), []), relay.reshape(const_8891.astype('float32'), [2, 8, 15]), relay.reshape(const_8867.astype('bool'), [2, 104]), ), 4)
uop_8898 = relay.sinh(uop_8883.astype('float64')) # shape=(18, 2)
uop_8900 = relay.sinh(uop_8885.astype('float64')) # shape=(18, 2)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_8901 = relay.TupleGetItem(func_7501_call(), 0)
call_8902 = relay.TupleGetItem(func_7502_call(), 0)
output = relay.Tuple([call_8862,const_8867,const_8868,const_8869,const_8870,call_8886,const_8887,call_8889,const_8890,const_8891,uop_8898,call_8901,])
output2 = relay.Tuple([call_8863,const_8867,const_8868,const_8869,const_8870,call_8888,const_8887,call_8892,const_8890,const_8891,uop_8900,call_8902,])
func_8904 = relay.Function([], output)
mod['func_8904'] = func_8904
mod = relay.transform.InferType()(mod)
mutated_mod['func_8904'] = func_8904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8904_call = mutated_mod.get_global_var('func_8904')
call_8905 = func_8904_call()
output = call_8905
func_8906 = relay.Function([], output)
mutated_mod['func_8906'] = func_8906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7729_call = mod.get_global_var('func_7729')
func_7730_call = mutated_mod.get_global_var('func_7730')
call_8907 = relay.TupleGetItem(func_7729_call(), 0)
call_8908 = relay.TupleGetItem(func_7730_call(), 0)
func_3055_call = mod.get_global_var('func_3055')
func_3059_call = mutated_mod.get_global_var('func_3059')
var_8921 = relay.var("var_8921", dtype = "float32", shape = ())#candidate|8921|()|var|float32
var_8922 = relay.var("var_8922", dtype = "float32", shape = (240,))#candidate|8922|(240,)|var|float32
var_8923 = relay.var("var_8923", dtype = "bool", shape = (1, 208))#candidate|8923|(1, 208)|var|bool
call_8920 = relay.TupleGetItem(func_3055_call(relay.reshape(var_8921.astype('float32'), []), relay.reshape(var_8922.astype('float32'), [2, 8, 15]), relay.reshape(var_8923.astype('bool'), [2, 104]), ), 6)
call_8924 = relay.TupleGetItem(func_3059_call(relay.reshape(var_8921.astype('float32'), []), relay.reshape(var_8922.astype('float32'), [2, 8, 15]), relay.reshape(var_8923.astype('bool'), [2, 104]), ), 6)
output = relay.Tuple([call_8907,call_8920,var_8921,var_8922,var_8923,])
output2 = relay.Tuple([call_8908,call_8924,var_8921,var_8922,var_8923,])
func_8931 = relay.Function([var_8921,var_8922,var_8923,], output)
mod['func_8931'] = func_8931
mod = relay.transform.InferType()(mod)
mutated_mod['func_8931'] = func_8931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8931_call = mutated_mod.get_global_var('func_8931')
var_8933 = relay.var("var_8933", dtype = "float32", shape = ())#candidate|8933|()|var|float32
var_8934 = relay.var("var_8934", dtype = "float32", shape = (240,))#candidate|8934|(240,)|var|float32
var_8935 = relay.var("var_8935", dtype = "bool", shape = (1, 208))#candidate|8935|(1, 208)|var|bool
call_8932 = func_8931_call(var_8933,var_8934,var_8935,)
output = call_8932
func_8936 = relay.Function([var_8933,var_8934,var_8935,], output)
mutated_mod['func_8936'] = func_8936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8089_call = mod.get_global_var('func_8089')
func_8090_call = mutated_mod.get_global_var('func_8090')
call_8944 = func_8089_call()
call_8945 = func_8089_call()
output = relay.Tuple([call_8944,])
output2 = relay.Tuple([call_8945,])
func_8947 = relay.Function([], output)
mod['func_8947'] = func_8947
mod = relay.transform.InferType()(mod)
mutated_mod['func_8947'] = func_8947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8947_call = mutated_mod.get_global_var('func_8947')
call_8948 = func_8947_call()
output = call_8948
func_8949 = relay.Function([], output)
mutated_mod['func_8949'] = func_8949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_8965 = relay.TupleGetItem(func_7413_call(), 1)
call_8966 = relay.TupleGetItem(func_7415_call(), 1)
func_579_call = mod.get_global_var('func_579')
func_582_call = mutated_mod.get_global_var('func_582')
var_8971 = relay.var("var_8971", dtype = "float32", shape = (150,))#candidate|8971|(150,)|var|float32
call_8970 = func_579_call(relay.reshape(var_8971.astype('float32'), [10, 15, 1]))
call_8972 = func_579_call(relay.reshape(var_8971.astype('float32'), [10, 15, 1]))
output = relay.Tuple([call_8965,call_8970,var_8971,])
output2 = relay.Tuple([call_8966,call_8972,var_8971,])
func_8984 = relay.Function([var_8971,], output)
mod['func_8984'] = func_8984
mod = relay.transform.InferType()(mod)
var_8985 = relay.var("var_8985", dtype = "float32", shape = (150,))#candidate|8985|(150,)|var|float32
output = func_8984(var_8985)
func_8986 = relay.Function([var_8985], output)
mutated_mod['func_8986'] = func_8986
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9010 = relay.var("var_9010", dtype = "float64", shape = (8, 12, 10))#candidate|9010|(8, 12, 10)|var|float64
uop_9011 = relay.atanh(var_9010.astype('float64')) # shape=(8, 12, 10)
uop_9054 = relay.sin(var_9010.astype('float32')) # shape=(8, 12, 10)
uop_9060 = relay.asin(uop_9011.astype('float32')) # shape=(8, 12, 10)
func_7579_call = mod.get_global_var('func_7579')
func_7585_call = mutated_mod.get_global_var('func_7585')
var_9068 = relay.var("var_9068", dtype = "bool", shape = (208,))#candidate|9068|(208,)|var|bool
var_9069 = relay.var("var_9069", dtype = "float32", shape = (2, 300))#candidate|9069|(2, 300)|var|float32
const_9070 = relay.const([[8,-9,-10,-2,-7,5,-5,9,-4,3,-3,2,5,-4,2,8,3,-4,8,3,-8,-3,7,-6,-10,3,-5,-1,-6,3],[6,7,-9,-2,8,-2,-8,-1,5,-6,-6,8,-5,-10,-5,1,4,-1,-1,-10,10,7,-5,3,-6,6,-9,3,-5,-4],[-8,2,-3,5,-7,2,6,-5,8,2,-8,-7,-7,10,-5,-4,1,5,10,7,6,3,9,-5,-6,10,-7,1,-7,-6],[7,-5,6,10,3,-3,7,3,6,2,6,5,8,9,-9,8,-7,-2,-5,10,2,-9,9,-4,1,-6,7,-2,9,10],[10,-6,3,1,2,7,5,4,9,1,-5,9,-10,9,-4,-9,-9,3,-3,-1,6,-3,-4,-6,-5,5,4,4,-4,-3],[-1,5,9,9,2,9,8,10,-8,-6,-3,-5,-4,-1,9,1,10,8,-3,3,9,-3,3,10,10,-6,-9,-10,-7,5],[6,-6,1,-6,-2,-8,-1,9,-4,7,7,5,-2,2,7,-5,-3,-1,-4,-7,-8,-7,-7,4,5,3,7,-9,4,-10],[9,6,-8,-4,-8,9,7,-6,4,4,-3,1,-5,-9,-2,-10,4,-10,-4,5,5,-7,-1,7,-5,5,5,8,-6,9],[-5,8,-8,4,-5,4,-4,-4,-6,-2,-9,-8,3,-6,-2,9,-7,-1,-7,7,-5,-6,3,-7,1,7,4,-8,-1,8],[-1,-3,5,-1,8,-6,10,5,2,-2,9,4,-5,2,7,1,8,6,7,-8,7,9,8,1,-6,-4,2,-10,-2,-5]], dtype = "uint16")#candidate|9070|(10, 30)|const|uint16
var_9071 = relay.var("var_9071", dtype = "bool", shape = (624,))#candidate|9071|(624,)|var|bool
const_9072 = relay.const([-1.984124,-2.434855,-5.631728,-8.905331,-6.471439,8.933937,-2.752072,9.662095,5.303041,-9.212953,1.901581,-7.226772,6.238437,3.767591,-9.027021,-7.457330,-5.605606,2.135156,2.393427,-7.704390,-0.918004,2.527452,9.913518,4.237262,-6.345501,5.230134,8.262441,6.510538,-5.854746,1.273385,-4.625311,3.167914,-2.032539,2.696866,-0.163457,-0.089592,5.876316,9.821312,-4.699528,-1.299153,2.446830,-0.927097,9.659920,2.159350,-4.520313,2.529744,-5.387637,8.921553,4.630594,-4.254459,-9.946528,-3.173079,-6.671532,4.316741,5.482203,3.079955,9.676232,8.873685,-1.329326,-7.432657,0.924697,7.316458,-1.305866,-9.417554,-2.251476,-3.736027,3.391568,-2.334534,-7.182525,-8.678722,7.934628,-6.196030,2.496961,-8.360343,-4.782423,-1.363783,-5.610245,3.327384,3.382949,-5.785125,4.860068,-2.856165,-8.054471,-2.706938,-6.837553,-2.597314,1.573354,9.092660,-9.488514,-0.116371,-0.850582,-6.836897,-7.417816,-8.691946,1.160327,4.063554,5.997740,-6.434623,4.136245,-4.297086,8.357271,4.277011,-7.023742,-4.035949,-2.721211,8.317880,2.073836,5.552226,-2.655442,8.013658,7.758092,-9.573321,0.152460,-9.540838,3.181601,-2.619200,7.934226,4.920472,-2.582644,-6.626922,-5.902664,-8.118233,7.787325,-4.412651,4.717617,0.978292,-6.810092,3.550376,-5.778803,-1.172243,-7.831131,3.857141,8.350158,2.228116,-2.122583,-3.822551,-8.013722,-8.760429,9.099642,1.640202,6.824170,7.632188,-4.095968,4.501930,-4.295774,-3.544876,-1.016199,-0.429339,6.565992,-3.497690,1.490386,-7.584359,9.715201,7.384498,9.053671,4.882760,4.087811,5.038410,9.249126,2.501145,-1.460189,-2.302069,8.505963,-1.717096,3.529885,-6.630944,-5.667647,-8.602842,0.324435,-6.290915,-2.563065,0.069796,-4.237006,3.575352,9.381010,8.030906,-7.685961,5.386693,-4.639027,-8.173139,-6.919041,-0.468309,-7.508715,-6.152393,-4.832604,-9.374758,-7.179164,-0.023293,-0.362176,-2.399244,-1.472775,-7.676233,6.646086,-4.899432,5.941503,2.616610,4.934269,-3.591313,-9.593809,-1.853013,4.222058,1.996082,-9.620578,-4.247954,0.369954,9.807805,-5.178679,9.229280,0.719281,6.650519,-6.985611,-4.850606,-6.495361,2.505825,9.954025,8.421171,5.897878,-7.743357,1.858025,-9.325029,8.827316,-1.789601,3.494818,0.533669,-6.114329,-9.884948,-0.315322,-2.967587,0.095826,9.681931,1.408912,-1.836572,-9.884522,6.043600,8.833853,-4.288080,7.990326,1.506298,-0.164832,0.780671,0.804243,-3.049582,-5.976806,7.636257,-7.802508,-9.462458,7.210666,-5.386199,6.326642,0.778545,-0.836005,0.886681,2.013056,-3.058453,0.348483,-1.461060,7.641438,-8.272285,2.765522,-8.483145,7.284578,-8.872674,7.505005,-9.595944,-1.918942,7.385102,3.026954,-1.269791,1.764836,0.022207,-0.958267,-1.773367,-3.620864,5.463936,-5.582409,2.237887,-4.417786,-5.054012,3.871252,-5.409203,5.347475,-2.970228,-2.252992,0.555231,8.123599,-2.921439,-5.000940,-1.639515,-8.738957,-6.466293,8.830085,-0.016012,3.870578,7.047259,1.474545,-8.808628,7.552066,4.270400,4.297607,-1.379301,9.790731,-8.009817,6.921225,-4.957085,-0.520803,-0.968015,2.821180,9.205448,3.415762,4.971856,-4.538397,9.459998,-6.239471,9.498430,8.485142,-7.605860,4.432728,-1.898740,0.574041,-9.274902,-8.592298,0.428381,8.769139,-9.417750,4.395473,7.531787,-9.241208,-3.855425,3.592943,-8.560868,2.857056,-2.277441,-3.987040,3.253672,3.724192,5.446869,-1.496003,4.053886,-6.601847,-6.574564,1.374603,8.135205,6.933137,-6.056552,-7.520411,0.972905,-9.381063,-9.415870,5.965177,-3.703589,1.946361,-9.715922,7.836255,1.734220,8.645643,2.163230,4.226465,-0.855312,-8.494560,3.501630,-5.719996,-1.352078,-6.634085,5.559293,-5.831993,8.627066,3.287656,9.200730,8.580680,-1.055442,9.958016,-1.258142,8.904368,5.434231,4.639960,-1.206807,1.154398,-5.148640,3.582264,7.139894,-6.893657,7.515586,-3.097582,-7.912459,8.304873,1.519959,-0.979050,6.700989,-8.772616,-0.168008,0.341379,6.310729,6.377107,7.845124,0.890271,7.602186,6.018547,-9.162413,5.317621,8.980428,1.184541,7.790584,-7.176481,1.734716,7.900296,9.054714,-5.930026,-7.907768,-9.314269,-9.501223,-6.350375,6.184086,-1.668647,-9.842358,-8.251013,-9.730364,-5.281816,-8.737491,-3.753123,9.738422,7.002700,9.447918,-0.139182,5.728837,9.841404,-3.198992,9.810509,0.775391,4.475912,-8.592507,9.658984,-9.815710,-7.624437,5.551613,-3.147269,1.648171,9.605731,-7.298754,-8.159566,-1.967471,0.903312,2.756756,0.118270,3.207138,-2.829827,-6.668667,-6.922876,7.159033,6.596538,-1.843985,-8.179876,0.330195,-9.891462,3.744301,-0.005222,-5.346549,-5.606716,-7.210981,-6.533674,9.438295,2.618654,-8.519832,-5.521217,0.948633,-7.255151,0.302630,8.188689,-4.538168,-4.600560,-6.909809,-9.649594,6.287599,-6.272149,-9.678877,6.892477,-8.965326,9.764392,-6.479754,-0.111808,-9.793560,7.775699,5.414659,-2.128399,-8.450891,1.984914,6.341666,3.280322,9.138752,7.954026,-4.650984,2.546382,8.753344,-4.012198,-5.410240,2.776119,5.530964,-1.143194,2.019595,0.835486,-2.783531,-5.476299,-1.331586,-6.169656,-9.619389,0.359490,-4.411896,2.266237,7.069161,8.576258,-9.497116,-6.700255,-8.973123,4.582089,-1.815914,5.015909,3.890824,-1.814925,-0.345521,0.912377,-3.002317,1.591070,1.392010,5.693750,-0.032441,-3.105893,8.358133,1.323270,-9.916297,-2.561104,4.116260,5.750485,3.978552,-9.385291,-4.737517,-4.527219,-5.251706,0.985287,-0.322797,-6.415691,7.548795,-4.893273,-9.730054,-6.369630,-4.383061,6.215836,3.085198,-1.992542,-4.323853,-4.411132,8.655935,-5.390960,-6.745671,0.925209,-3.698321,-9.634736,4.074105,-5.238621,-6.053270,-6.627939,3.842803,-2.972876,-8.321689,-6.453802,8.242233,7.871357,4.214464,-8.209796,2.549919,7.013804,4.141202,2.891684,-9.665630,-0.338788,3.004555,9.443332,-6.691565,5.405026,-5.792291,-9.565064,-2.727431,-5.483192,7.105838,9.264614,7.371872,-0.234851,-5.169526,6.131881,7.025612,0.463835,-3.193049,-8.877824,-8.788327,8.462469,4.655332,-1.715508,6.530798,2.371833,4.147513,4.092338,0.611477,-4.555770,5.520387,-0.736868,2.464030,9.928759,-6.309853,7.013100,4.945590,-2.216290,-9.785567,-5.591921,0.244913,-4.886314,4.845811,8.191797,1.582945,-9.172613,4.047352,1.365526,7.052217,-2.477759,-5.232290,-2.132142,-7.814652,-1.072473,-7.937857,-2.060092,7.719019,-2.093745,-1.213066,9.584840,7.514270,1.795890,7.488311,-3.167948,5.587719,-6.171883,-4.463560,-5.914985,8.044140,3.199103,9.427653,-8.077366,-8.209274,3.772282,-9.897645,-2.088734,3.902802,1.420876,-0.035073,8.760428,-7.417845,-2.196271,-1.788072,-3.765155,2.914535,3.455898,3.646045,3.997647,1.846786,2.687445,-1.908607,6.447692,6.712384,-7.504444,-9.872891,8.340101,4.678420,3.515436,-2.752425,-0.465412,9.952149,6.392528,5.010892,-6.074997,8.702964,-6.737366,2.930805,5.818026,-7.688943,3.042410,2.523232,-4.894962,-1.852631,8.047907,7.275354,-1.502604,8.822709,0.524135,4.912344,1.776630,5.501141,-4.514640,-5.538511,4.891856,3.162038,9.676804,-7.310051,5.416560,-7.560044,7.863018,-3.129022,-7.709356,1.454393,-3.210572,-4.906413,-9.258495,-9.222711,-0.479443,-1.009658,8.262100,-0.085567,9.127076,-9.230194,1.008688,4.901288,-7.516323,9.725800,4.423196,9.103791], dtype = "float32")#candidate|9072|(720,)|const|float32
call_9067 = relay.TupleGetItem(func_7579_call(relay.reshape(var_9068.astype('bool'), [208,]), relay.reshape(var_9069.astype('float32'), [2, 300]), relay.reshape(const_9070.astype('uint16'), [300,]), relay.reshape(var_9071.astype('bool'), [624,]), relay.reshape(const_9072.astype('float32'), [720,]), ), 9)
call_9073 = relay.TupleGetItem(func_7585_call(relay.reshape(var_9068.astype('bool'), [208,]), relay.reshape(var_9069.astype('float32'), [2, 300]), relay.reshape(const_9070.astype('uint16'), [300,]), relay.reshape(var_9071.astype('bool'), [624,]), relay.reshape(const_9072.astype('float32'), [720,]), ), 9)
func_2381_call = mod.get_global_var('func_2381')
func_2384_call = mutated_mod.get_global_var('func_2384')
const_9076 = relay.const([-6,7,-1,-2,-3,-10,-8,-4,-7,-8,8,4,-10,-7,-4,1,7,7,-5,10,-9,2,3,8,-10,-8,6,-6,5,-3,4,-8,-1,2,3,-5,2,2,5,7,10,-6,7,3,5,-2,9,3,-4,8,-5,-10,10,6,3,1,-9,8,-8,2,4,-2,2,4,10,-3,-3,-4,4,6,-3,1], dtype = "uint8")#candidate|9076|(72,)|const|uint8
call_9075 = relay.TupleGetItem(func_2381_call(relay.reshape(var_9068.astype('bool'), [8, 13, 2]), relay.reshape(const_9076.astype('uint8'), [72,]), ), 6)
call_9077 = relay.TupleGetItem(func_2384_call(relay.reshape(var_9068.astype('bool'), [8, 13, 2]), relay.reshape(const_9076.astype('uint8'), [72,]), ), 6)
output = relay.Tuple([uop_9054,uop_9060,call_9067,var_9068,var_9069,const_9070,var_9071,const_9072,call_9075,const_9076,])
output2 = relay.Tuple([uop_9054,uop_9060,call_9073,var_9068,var_9069,const_9070,var_9071,const_9072,call_9077,const_9076,])
func_9083 = relay.Function([var_9010,var_9068,var_9069,var_9071,], output)
mod['func_9083'] = func_9083
mod = relay.transform.InferType()(mod)
var_9084 = relay.var("var_9084", dtype = "float64", shape = (8, 12, 10))#candidate|9084|(8, 12, 10)|var|float64
var_9085 = relay.var("var_9085", dtype = "bool", shape = (208,))#candidate|9085|(208,)|var|bool
var_9086 = relay.var("var_9086", dtype = "float32", shape = (2, 300))#candidate|9086|(2, 300)|var|float32
var_9087 = relay.var("var_9087", dtype = "bool", shape = (624,))#candidate|9087|(624,)|var|bool
output = func_9083(var_9084,var_9085,var_9086,var_9087,)
func_9088 = relay.Function([var_9084,var_9085,var_9086,var_9087,], output)
mutated_mod['func_9088'] = func_9088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8292_call = mod.get_global_var('func_8292')
func_8293_call = mutated_mod.get_global_var('func_8293')
call_9111 = func_8292_call()
call_9112 = func_8292_call()
func_2381_call = mod.get_global_var('func_2381')
func_2384_call = mutated_mod.get_global_var('func_2384')
const_9121 = relay.const([True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False], dtype = "bool")#candidate|9121|(208,)|const|bool
var_9122 = relay.var("var_9122", dtype = "uint8", shape = (72,))#candidate|9122|(72,)|var|uint8
call_9120 = relay.TupleGetItem(func_2381_call(relay.reshape(const_9121.astype('bool'), [8, 13, 2]), relay.reshape(var_9122.astype('uint8'), [72,]), ), 0)
call_9123 = relay.TupleGetItem(func_2384_call(relay.reshape(const_9121.astype('bool'), [8, 13, 2]), relay.reshape(var_9122.astype('uint8'), [72,]), ), 0)
func_2982_call = mod.get_global_var('func_2982')
func_2988_call = mutated_mod.get_global_var('func_2988')
const_9125 = relay.const([-3.147387,-3.437584,-8.666673,8.437293,9.361142,3.058628,-3.361879,-0.913128,-3.241388,0.993162,0.387505,-0.018376,4.676266,3.374053,9.748480,1.502987,-2.319434,1.057860,5.690550,9.548928,4.970872,5.894771,1.871073,5.952019,-9.431608,2.032916,-7.424285,-5.603451,5.595473,-3.514796,-6.137476,-0.734207,9.334981,-8.924815,6.161090,4.728046], dtype = "float32")#candidate|9125|(36,)|const|float32
const_9126 = relay.const(8, dtype = "uint8")#candidate|9126|()|const|uint8
call_9124 = relay.TupleGetItem(func_2982_call(relay.reshape(const_9125.astype('float32'), [2, 9, 2]), relay.reshape(const_9125.astype('float32'), [2, 9, 2]), relay.reshape(call_9120.astype('bool'), [208,]), relay.reshape(var_9122.astype('uint8'), [36, 2]), relay.reshape(const_9126.astype('uint8'), []), ), 7)
call_9127 = relay.TupleGetItem(func_2988_call(relay.reshape(const_9125.astype('float32'), [2, 9, 2]), relay.reshape(const_9125.astype('float32'), [2, 9, 2]), relay.reshape(call_9120.astype('bool'), [208,]), relay.reshape(var_9122.astype('uint8'), [36, 2]), relay.reshape(const_9126.astype('uint8'), []), ), 7)
func_7729_call = mod.get_global_var('func_7729')
func_7730_call = mutated_mod.get_global_var('func_7730')
call_9129 = relay.TupleGetItem(func_7729_call(), 0)
call_9130 = relay.TupleGetItem(func_7730_call(), 0)
output = relay.Tuple([call_9111,call_9120,const_9121,var_9122,call_9124,const_9125,const_9126,call_9129,])
output2 = relay.Tuple([call_9112,call_9123,const_9121,var_9122,call_9127,const_9125,const_9126,call_9130,])
func_9134 = relay.Function([var_9122,], output)
mod['func_9134'] = func_9134
mod = relay.transform.InferType()(mod)
mutated_mod['func_9134'] = func_9134
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9135 = relay.var("var_9135", dtype = "uint8", shape = (72,))#candidate|9135|(72,)|var|uint8
func_9134_call = mutated_mod.get_global_var('func_9134')
call_9136 = func_9134_call(var_9135)
output = call_9136
func_9137 = relay.Function([var_9135], output)
mutated_mod['func_9137'] = func_9137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8089_call = mod.get_global_var('func_8089')
func_8090_call = mutated_mod.get_global_var('func_8090')
call_9175 = func_8089_call()
call_9176 = func_8089_call()
output = relay.Tuple([call_9175,])
output2 = relay.Tuple([call_9176,])
func_9184 = relay.Function([], output)
mod['func_9184'] = func_9184
mod = relay.transform.InferType()(mod)
output = func_9184()
func_9185 = relay.Function([], output)
mutated_mod['func_9185'] = func_9185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_9203 = relay.TupleGetItem(func_7172_call(), 2)
call_9204 = relay.TupleGetItem(func_7173_call(), 2)
func_5133_call = mod.get_global_var('func_5133')
func_5137_call = mutated_mod.get_global_var('func_5137')
const_9206 = relay.const([[4,10,-5,-4,6,1,8,5,8,9,1,7,6,3,-8,5,-10,-1,-9,-1,-10,-3,8,8,-9,8,-4,-1,9,-10,-8,-10,-2,-3,-7,-6,-9,-5,-8,3,-2,9,-7,8,-4,-4,3,-3,8,-6,2,-2,-10,8,-2,7,-3,9,9,-8,8,-7,8,8,6,1,-5,-7,-1,-4,7,6,10,-1,-7,-1,-3,-7,-8,4,-8,-10,-9,-7,3,3,5,-1,7,1,3,8,-10,-4,10,10,5,1,8,-6,1,4,-9,10],[-9,9,-3,-5,-1,-9,8,-1,1,9,-1,-4,-4,-10,-3,10,-1,3,7,-7,10,-9,7,-3,3,-2,9,-9,-4,10,9,-1,-1,2,-6,-4,5,5,7,-4,2,-5,2,7,-4,5,-5,2,5,-3,5,5,5,5,8,2,-5,-4,-2,-3,6,-8,8,-8,-7,2,-8,-3,-7,-5,-8,-8,4,10,-10,10,2,-8,1,-3,-5,-10,2,-8,-4,7,-7,-6,6,5,-10,-2,5,5,6,-4,-3,-5,-10,5,5,-7,-8,5],[1,-1,-7,5,3,-9,8,-9,8,7,9,1,5,-8,10,-6,-3,2,-10,-1,-7,-3,4,5,7,9,3,10,7,-2,1,-10,4,2,8,-8,-6,1,2,1,9,7,-9,1,-5,6,10,-8,-9,10,-8,4,7,5,3,-1,5,6,5,1,-2,-5,5,7,-8,1,5,-1,1,4,-1,6,-4,-1,10,10,10,-4,-3,-7,8,-6,-3,5,-10,-8,7,6,-6,10,-10,10,8,-3,7,-1,-9,-7,-3,-6,5,-5,-10,4],[9,-4,6,6,-9,4,-2,10,1,4,4,-6,-6,1,-1,1,-9,-6,-2,9,-3,7,8,-7,-9,-3,-10,3,-10,-1,-9,1,-1,1,1,-3,4,10,-9,3,7,-2,6,5,10,-9,10,5,6,5,7,-4,1,-5,10,-10,-5,-5,8,7,6,4,-5,-9,6,-10,3,-4,-7,-5,-6,-3,-7,-1,8,2,-5,2,-3,3,-7,2,7,6,-6,1,8,-2,2,-2,3,-4,8,8,-7,3,-4,-5,3,-4,-4,3,-7,-9],[-10,1,4,-2,9,8,-3,-1,-7,9,-8,3,6,-4,-10,-3,-3,-4,10,-1,-7,7,9,-8,-4,10,-8,6,6,-8,-2,-7,-7,-1,-8,-6,-1,-5,-2,-1,-10,10,4,3,-5,-8,-3,-1,-7,-7,-7,10,-7,2,-9,-8,6,8,-6,-1,3,-8,-6,7,3,10,7,2,6,5,-9,-8,-1,-4,-7,-7,-6,-9,4,-8,9,9,-8,2,-4,-3,8,-7,-8,-5,8,7,7,-8,1,-7,4,6,6,-9,-5,-3,-4,3],[5,-6,1,9,-9,-8,3,-1,-9,2,-7,8,-3,-6,-3,-6,-10,-1,8,-9,-7,7,10,6,7,7,-8,7,-5,-6,-3,-9,7,-3,10,-1,-7,-6,8,-10,-1,-10,-1,-8,-3,9,9,8,7,-10,-5,5,-1,1,-4,-8,-8,-2,7,-7,8,-6,-3,-4,10,-1,-7,7,7,1,8,6,8,-5,10,7,10,-5,-2,7,-5,4,-7,3,-8,-5,4,2,-9,-10,1,-7,3,-5,-2,-4,3,2,9,-3,-10,3,10,-9],[-2,-10,-6,-3,-10,3,-5,3,-7,9,10,2,2,5,1,-3,-3,-4,-1,-8,-9,4,-10,-1,2,2,4,2,-1,8,-1,3,-5,2,5,-6,3,-8,9,-9,-1,-2,6,1,-3,7,1,7,-6,1,-1,8,8,-6,-5,-9,5,-1,9,8,10,-5,7,8,-1,7,-7,5,-10,6,7,4,-9,4,-9,-10,-10,-2,7,10,-9,1,1,5,6,-9,-7,4,7,3,-10,5,-6,-9,-4,-10,-8,-1,6,2,-7,4,1,-9]], dtype = "int32")#candidate|9206|(7, 104)|const|int32
const_9207 = relay.const([[7.582788,9.337159],[-0.920841,2.134420],[-9.987947,3.669709],[6.399237,1.525745],[0.273200,7.955694],[-6.626069,-6.623535],[-4.850508,3.517078],[-7.884573,1.339146],[-4.551919,3.616892],[7.967630,-7.061203],[3.509665,-9.742325],[0.992204,-6.821960],[2.749065,7.890282],[-9.709805,-7.838189],[-6.005863,2.111031],[9.684888,-8.773834],[-0.094650,2.825159],[-7.359170,8.622797],[7.732739,9.410259],[-7.341986,9.728085],[9.831147,2.460020],[0.889460,-2.943220],[-3.536764,-5.767903],[-8.759309,4.242374],[-1.012555,-3.475238],[5.481013,7.241278],[-1.877683,9.799379],[-9.173565,-4.399726],[-0.641074,2.751373],[6.823128,3.591386],[-7.912501,5.230930],[-6.692498,0.413304],[1.144856,4.243819],[0.840200,-2.333473],[2.744821,-7.890921],[-6.642800,9.265321],[4.962741,-0.450354],[-1.714613,-9.604534],[-1.523633,-7.516734],[-0.655621,5.780569],[0.739160,-8.486599],[6.855112,-2.632392],[1.089452,-6.642150],[9.412549,-2.472052],[9.944272,3.413612],[-4.109438,-3.533028],[-8.058959,7.895803],[-6.387530,-4.902800],[2.863457,-5.300459],[9.691241,-1.110733],[-6.827305,5.150277],[-3.210467,-3.967745],[-2.367233,-3.387216],[1.004721,9.877650],[2.083957,-6.812145],[-0.516229,2.387631],[-9.182105,-1.834727],[8.101408,-4.412697],[-1.666453,4.906998],[8.787422,-0.183470],[-0.125989,-4.105942],[5.973000,0.637343],[-7.211783,-9.535545],[-7.156849,-2.959993],[9.238750,7.388316],[0.475988,-6.691230],[4.201560,4.698259],[4.534829,-2.993250],[-0.189483,6.618072],[9.414651,-1.568353],[7.305072,-7.864349],[-0.833223,-5.181350],[2.427762,-2.399557],[5.249187,-5.392013],[2.666305,0.938390]], dtype = "float32")#candidate|9207|(75, 2)|const|float32
call_9205 = relay.TupleGetItem(func_5133_call(relay.reshape(const_9206.astype('int32'), [4, 14, 13]), relay.reshape(const_9207.astype('float32'), [25, 6]), ), 1)
call_9208 = relay.TupleGetItem(func_5137_call(relay.reshape(const_9206.astype('int32'), [4, 14, 13]), relay.reshape(const_9207.astype('float32'), [25, 6]), ), 1)
uop_9210 = relay.atan(const_9207.astype('float32')) # shape=(75, 2)
uop_9215 = relay.rsqrt(uop_9210.astype('float32')) # shape=(75, 2)
output = relay.Tuple([call_9203,call_9205,const_9206,uop_9215,])
output2 = relay.Tuple([call_9204,call_9208,const_9206,uop_9215,])
func_9218 = relay.Function([], output)
mod['func_9218'] = func_9218
mod = relay.transform.InferType()(mod)
mutated_mod['func_9218'] = func_9218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9218_call = mutated_mod.get_global_var('func_9218')
call_9219 = func_9218_call()
output = call_9219
func_9220 = relay.Function([], output)
mutated_mod['func_9220'] = func_9220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8047_call = mod.get_global_var('func_8047')
func_8048_call = mutated_mod.get_global_var('func_8048')
call_9358 = relay.TupleGetItem(func_8047_call(), 0)
call_9359 = relay.TupleGetItem(func_8048_call(), 0)
output = relay.Tuple([call_9358,])
output2 = relay.Tuple([call_9359,])
func_9363 = relay.Function([], output)
mod['func_9363'] = func_9363
mod = relay.transform.InferType()(mod)
mutated_mod['func_9363'] = func_9363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9363_call = mutated_mod.get_global_var('func_9363')
call_9364 = func_9363_call()
output = call_9364
func_9365 = relay.Function([], output)
mutated_mod['func_9365'] = func_9365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_9445 = relay.TupleGetItem(func_7501_call(), 0)
call_9446 = relay.TupleGetItem(func_7502_call(), 0)
func_5731_call = mod.get_global_var('func_5731')
func_5736_call = mutated_mod.get_global_var('func_5736')
var_9457 = relay.var("var_9457", dtype = "float64", shape = (10, 44))#candidate|9457|(10, 44)|var|float64
const_9458 = relay.const([9.790385,-8.146049,6.429755,6.915678,6.461042,1.963305,2.019095,-6.010450,-7.216355,8.435699,-5.797454,-6.832244,8.448029,3.362553,-4.112481,2.130224,-4.484402,6.023878,7.413039,2.270000,-7.202044,2.285467,7.360873,0.248062,8.943793,5.231845,6.229682,-0.764757,3.196156,0.657569,3.999312,-6.365485,-7.241845,3.198423,-8.555057,3.032122,2.180865,-0.530112,-7.383541,-6.706272,3.382247,7.302459,4.064910,6.346371,-6.727082,6.415023,4.126221,2.132953,0.088313,-0.376504,7.331090,-0.365836,-9.820227,5.256524,4.255789,-9.828207,4.062148,4.817619,6.011425,-1.853663,5.400558,1.997023,3.751876,-2.882676,-4.389912,-2.516126,-4.979841,-2.300034,-8.019034,3.216839,-6.295339,-1.242055,-3.182444,-2.598978,-8.705501,9.537780,-7.037896,-4.942324,9.361004,3.177329,9.607766,-3.772213,-9.212871,-8.723384,-1.529535,-7.036927,6.540232,3.453073,-1.424641,-7.590025,-5.141822,-1.606837,-4.127892,-6.534471,-8.552432,7.015588,4.462609,7.991222,0.681550,-8.361846,-6.345796,-6.717542,1.203530,1.347094,7.931749,-0.986853,5.865824,4.713140,-2.154607,7.828552,7.895954,-9.218179,-2.296901,-4.873560,-9.865351,-9.960287,-6.330146,-7.831771,-9.431854,8.307609,5.118073,4.648303,7.831011,0.446642,-1.658251,-3.192016,4.744574,-3.993170,-2.384838,6.192630,-1.475194,4.814141,-1.211139,-9.974845,5.786477,2.497092,-9.294673,3.279042,8.386574,7.790542,-2.990460,4.004860,-8.986872,6.096326,-9.284911,8.450323,-7.333993,1.505710,1.399707,6.569719,-6.273609,8.767122,1.815762,-9.548005,2.676819,-6.490246,9.104475,-1.051982,-4.236488,-7.860983,-3.875015,4.659957,1.328536,-0.122604,-0.730391,5.780382,-0.820268,6.155821,-6.841652,-8.172996,3.474867,7.970917,-4.444553,6.077066,9.845435,7.202900,2.437804,2.916758,-7.080592,7.417197,9.422552,5.025181,-9.792169,-8.749520,-0.925332,-1.162473,8.082061,-4.599288,3.465200,-0.550942,6.944570,6.924571,-5.669152,2.152460,-7.732227,-8.849575,-0.786246,2.785902,-9.339635,7.207230,-1.163417,1.033904,6.794351,9.661421,0.671973,3.034152,9.891791,2.240089,6.660130,-1.700165,-1.056147,-2.717175,-7.772112,6.128024,0.237875,0.898260,-8.942306,7.822733,-2.554279,8.275065,4.428307,4.450217,1.674149,-3.058375,8.391485,-4.021005,9.657646,-1.410398,-6.617217,6.337214,-4.301077,8.447905,4.075482,-3.404963,1.698102,9.342886,0.367296,7.095074,9.926251,2.631722,6.210578,-3.475252,-3.496141,-5.587964,-5.072989,-5.169486,7.162560,-0.878795,2.931450,-4.348407,-9.923054,8.050683,-8.658882,-8.649234,-4.162148,7.546815,4.115059,3.759462,-6.912293,-2.681059,5.536933,-2.724485,-0.910100,6.956893,9.609166,-7.452611,2.483332,0.205115,-0.256059,1.431079,-2.190693,-3.349480,4.958292,1.852327,-1.087211,-6.220490,8.370176,-5.380668,1.700086,8.716041,9.373791,-4.036910,1.302128,0.734569,3.373323,-3.489384,4.309732,6.453909,-5.400683,-3.469314,-2.073952,-4.173347,8.285402,3.459941,-9.613924,-3.983698,-6.562271,-9.951440,-2.639887,-3.579586,3.409939,1.494635,3.219313,9.551918,-1.781718,-4.291185,-5.779146,-0.354849,4.399757,3.168783,-7.156553,-9.363672,-2.688131,-6.942014,-3.653344,8.639168,5.034861,-6.703225,7.766777,3.839599,0.542812,1.343438,-1.645258,-3.050306,2.372697,-2.774477,6.183364,4.906767,2.894894,-0.581456,-9.579916,5.954338,0.176893,-8.401456,0.363222,-6.716880,-0.987098,3.344214,2.080045,-5.751033,2.772404,-8.501113,9.480837,-8.088792,2.349980,-3.673664,-1.477582,8.717505,4.884660,5.016071,0.444567,-7.768423,8.537701,2.106629,6.351563,7.141672,-1.173362,5.819666,3.089858,-9.321261,-0.881152,-1.368042,0.631272,-3.930373,-6.592002,3.988419,0.935830,9.233748,2.438071,6.087569,-5.834899,9.269049,-4.683227,1.781459,4.356357,-0.033617,-9.294527,-7.428213,9.590735,5.888129,-2.533435,8.815170,-9.595832,-2.118567,0.274877,-5.555710,2.489645,-4.135290,-2.333188,5.192822,-6.410676,1.002061,1.385112,-6.880064,3.845659,-3.837324,-1.498468,5.096339,-5.989331,5.118766,-3.649367,7.916446,0.757562,4.836192,2.353207,5.216667,5.078208,0.309636,8.180134,5.967897,5.969927,-0.846986,2.263896,-7.835230,-9.558748,-9.677980,7.127089,-1.135118,6.607697,-5.407613,-1.614513,-5.864272,-8.152957,-0.080215,7.800753,-7.432563,9.125010,3.989185,8.995693,-2.932798,5.376305,-3.509173,6.348320,8.625643,-9.929225,1.966262,-5.768364,-9.174477,6.838598,-8.134662,-2.730209,8.840109,6.920819,7.413625,-8.905943,-6.617404,-6.847112,-1.480330,9.672791,-9.305382,1.076643,2.361381,-1.482021,3.041627,-0.289810,-8.690100,-0.085262,4.480302,-1.685252,-8.557635,-0.147903,-3.624956,2.360904,-6.717199,0.603439,5.857275,5.948696,-7.956462,-1.351570,6.400757,5.769664,-0.565858,-9.127242,5.287968,-6.449961,3.716274,5.079050,5.695037,4.261914,3.631716,-6.912008,3.286470,8.566623,2.123773,8.889015,7.599819,0.210267,6.565306,7.696300,-9.279329,-0.367589,-7.956265,-7.430815,6.318521,-9.326434,-9.046736,3.259196,-8.879142,1.360159,-2.665289,-6.011952,3.962495,6.123483,9.970929,4.660878,-0.878762,-8.609835,8.369354,-0.528038,-0.466304,-1.324900,-9.133233,-2.196890,-1.506191,-2.795491,7.551690,-1.934799,-9.082084,4.136226,-6.208710,-2.732534,-1.150145,-9.223331,5.414451,-5.497471,7.804747,-7.848068,-3.386452,-1.125131,-9.270861,-8.697177,6.255888,-0.203927,-3.232993,-8.951834,-5.871668,-9.308597,7.006718,1.365138,6.451012,-8.292236,-3.640217,-1.086830,4.911984,9.366346,-3.098277,2.958280,1.441295,1.795709,8.339004,-1.191099,-7.274340,5.530939,5.555523,-1.249776,-3.664906,7.112165,6.501174,-5.374805,-9.248562,-4.250244,6.041836,2.567847,0.482520,-0.173736,-7.892343,1.928269,0.222662,-4.623141,9.473247,-4.650936,0.400256,-3.377233,4.369577,7.832941,-7.345903,-2.457480,-0.114774,-2.237968,8.034658,-2.445027,-7.507547,-0.472192,-5.197667,-7.694990,-2.712394,-2.481487,6.379792,-4.505188,9.668904,-6.950166,-2.021296,4.122944,-9.758839,-1.409270,-3.471019,1.958922,-4.438888,7.442306,-1.884103,-7.818042,-0.002962,-9.333657,0.405984,-1.179610,0.906723,2.092075,-5.404705,-6.713524,-1.095339,-8.583335,5.103482,9.095411,7.917995,7.850514,5.553029,-1.248420,-1.785610,3.268789,-1.054036,-5.627369,-9.973435,5.147602,-7.363355,-4.587968,-8.715406,4.320943,-9.440321,-2.857718,7.936750,-4.691061,0.087018,-5.911064,2.535619,-8.622394,-1.222131,0.644998,-2.999525,6.874682,-9.695588,3.602629,-2.090044,8.756692,-4.758183,-7.140840,3.019018,-6.997952,-9.979795,-7.881941,-4.936456,7.621581,0.098517,8.692945,6.585234,-4.277186,-6.300365,-5.029049,-8.513474,-4.561168,9.288817,9.902008,2.422124,-5.337750,-7.259361,7.313316,0.970291,0.165441,-1.469810,-6.849391,2.325368,6.807688,-2.667676,-8.941685,5.711783,6.686110,-2.406524,5.750579,-8.325981,2.603261,-2.851607,6.386348,5.057389,-1.797903,-2.422983,1.112501,9.448845,2.310573,-2.393979,7.336701,-0.741329,1.126597,0.690213,-4.831593,-9.394399,-0.821076,7.343280,-1.662908,4.777736,-8.671646,9.216167,1.482528,-1.031249,-1.946440,5.313744,4.261673,3.255943,-0.373509,9.992394,-4.355247,-9.266617,1.869831,6.347761,-8.162969,-5.511584,-1.193647,-0.693594,5.918279,-9.270408,0.446586,0.869201], dtype = "float32")#candidate|9458|(720,)|const|float32
var_9459 = relay.var("var_9459", dtype = "uint8", shape = ())#candidate|9459|()|var|uint8
const_9460 = relay.const([8.351299,-8.513291,-2.398139,0.920829,2.570661,-3.113205,-8.079539,8.108073,6.799058,-7.376478,1.919165,0.434882,-1.933853,1.074478,-7.860831,-7.307431,-3.847887,8.055154,-3.088715,-3.517485,-4.549519,-4.488638,5.446474,7.943721,-7.111711,0.515205,3.312933,-5.407909,-6.392510,-6.613945,-9.209841,-8.175210,6.630916,3.898686,8.701070,-2.886515,9.696549,-5.940102,-3.266879,1.217808,6.605533,-8.470596,4.442661,-8.739093,-3.278968,-7.715499,-0.687315,-5.466167,-2.055875,8.237463,0.002509,4.461553,-9.246017,-0.949700,9.425430,1.019426,-3.433644,0.622171,-8.812286,3.443600,-4.332292,3.214649,-4.241439,8.418277,-2.228524,-8.480595,-6.964827,-4.191484,-1.203597,5.515574,-7.467364,-1.295413,0.392898,-0.031480,-4.037450,-5.532764,9.315270,2.662135,3.960303,-0.465078,5.361266,-9.317167,-2.805790,3.739241,9.037322,-3.672138,8.178518,-8.286568,-3.541675,6.276786,-0.889818,-1.841180,3.358760,2.060669,-9.233443,-3.208962,3.624409,8.670193,1.968155,-5.475674,2.138350,-5.299679,4.377535,5.447314,1.628871,-3.765286,1.322171,8.214475,-2.226458,2.158692,-0.371982,4.606183,-2.011370,6.444890,7.378624,-8.962235,-5.589238,6.512615,2.824760,-2.044260,8.045136,-7.681885,9.926130,-7.951895,0.995320,-8.784469,5.252667,5.340286,-9.647324,-4.507285,-6.856296,-7.731225,0.047283,-0.430914,6.121404,-1.339423,-9.465122,1.276752,-2.574077,8.832810,4.064221,-3.307757,2.544334,1.187868,-5.502736,4.847245,-9.569486,-2.281943,-8.722828,8.237929,4.633940,-8.477778,-6.160620,7.174406,3.683376,-5.958794,-7.115094,-6.101968,-6.214620,6.651203,5.024191,2.006473,-5.411992,6.894378,4.526378,-9.777307,-6.839548,-3.195500,-9.639618,-7.664055,-9.240464,3.739679,4.389175,0.270464,6.916266,-0.607989,3.486571,-7.300722,9.652885,-8.999183,-3.438773,7.360629,-9.272613,-1.091798,7.079651,-2.557201,9.026505,-1.772289,9.443346,7.654884,-9.893924,7.881141,9.970158,-0.254676,-5.422953,8.758561,2.246689,9.026660,-9.515764,0.781243,-7.535470,-5.203982,3.369258,-0.712418,-5.665978,0.652361,-1.056559,-8.015696,-5.117429,-8.449904,-3.076950,-3.708526,8.303356,6.981492,1.268465,5.917299,-4.391698,1.513475,7.385337,9.092337,5.618679,-8.742113,7.081356,-8.258840,6.663377,-1.332291,-6.604408,-7.739762,4.887206,-1.289328,-2.999795,-8.864761,5.181656,-1.645418,-8.462014,-9.472701,-1.719309,6.306518,5.360538,2.729067,-1.809428,-8.831373,-1.471446,-4.875460,-7.925389], dtype = "float32")#candidate|9460|(245,)|const|float32
call_9456 = relay.TupleGetItem(func_5731_call(relay.reshape(var_9457.astype('float64'), [11, 8, 5]), relay.reshape(const_9458.astype('float32'), [720,]), relay.reshape(var_9459.astype('uint8'), []), relay.reshape(const_9460.astype('float32'), [245,]), ), 8)
call_9461 = relay.TupleGetItem(func_5736_call(relay.reshape(var_9457.astype('float64'), [11, 8, 5]), relay.reshape(const_9458.astype('float32'), [720,]), relay.reshape(var_9459.astype('uint8'), []), relay.reshape(const_9460.astype('float32'), [245,]), ), 8)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_9464 = func_7228_call()
call_9465 = func_7228_call()
output = relay.Tuple([call_9445,call_9456,var_9457,const_9458,var_9459,const_9460,call_9464,])
output2 = relay.Tuple([call_9446,call_9461,var_9457,const_9458,var_9459,const_9460,call_9465,])
func_9469 = relay.Function([var_9457,var_9459,], output)
mod['func_9469'] = func_9469
mod = relay.transform.InferType()(mod)
var_9470 = relay.var("var_9470", dtype = "float64", shape = (10, 44))#candidate|9470|(10, 44)|var|float64
var_9471 = relay.var("var_9471", dtype = "uint8", shape = ())#candidate|9471|()|var|uint8
output = func_9469(var_9470,var_9471,)
func_9472 = relay.Function([var_9470,var_9471,], output)
mutated_mod['func_9472'] = func_9472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8947_call = mod.get_global_var('func_8947')
func_8949_call = mutated_mod.get_global_var('func_8949')
call_9485 = relay.TupleGetItem(func_8947_call(), 0)
call_9486 = relay.TupleGetItem(func_8949_call(), 0)
output = relay.Tuple([call_9485,])
output2 = relay.Tuple([call_9486,])
func_9488 = relay.Function([], output)
mod['func_9488'] = func_9488
mod = relay.transform.InferType()(mod)
output = func_9488()
func_9489 = relay.Function([], output)
mutated_mod['func_9489'] = func_9489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8904_call = mod.get_global_var('func_8904')
func_8906_call = mutated_mod.get_global_var('func_8906')
call_9517 = relay.TupleGetItem(func_8904_call(), 4)
call_9518 = relay.TupleGetItem(func_8906_call(), 4)
func_2381_call = mod.get_global_var('func_2381')
func_2384_call = mutated_mod.get_global_var('func_2384')
const_9532 = relay.const([[False,False],[False,False],[True,True],[False,False],[False,True],[True,False],[True,True],[True,True],[True,False],[True,True],[False,True],[True,False],[False,False],[True,False],[False,False],[True,False],[False,True],[True,False],[False,True],[False,False],[False,False],[True,True],[True,False],[False,False],[True,False],[False,True],[True,True],[False,False],[True,True],[False,True],[True,True],[False,True],[False,True],[True,False],[False,False],[True,False],[False,False],[True,True],[False,True],[False,True],[True,False],[True,True],[True,True],[True,True],[False,True],[False,True],[True,False],[False,True],[True,False],[False,True],[False,True],[True,False],[True,False],[True,True],[False,True],[True,True],[True,False],[False,True],[True,True],[False,True],[True,False],[False,False],[True,False],[True,False],[False,True],[False,False],[False,True],[False,True],[False,False],[True,False],[True,False],[True,True],[False,False],[False,True],[True,False],[False,False],[False,False],[False,True],[False,False],[False,True],[True,False],[True,False],[True,False],[True,True],[False,False],[True,True],[False,True],[False,False],[True,False],[True,False],[False,True],[True,True],[True,True],[False,False],[True,False],[True,True],[False,False],[True,False],[False,False],[True,False],[True,True],[False,True],[False,False],[False,True]], dtype = "bool")#candidate|9532|(104, 2)|const|bool
var_9533 = relay.var("var_9533", dtype = "uint8", shape = (72,))#candidate|9533|(72,)|var|uint8
call_9531 = relay.TupleGetItem(func_2381_call(relay.reshape(const_9532.astype('bool'), [8, 13, 2]), relay.reshape(var_9533.astype('uint8'), [72,]), ), 4)
call_9534 = relay.TupleGetItem(func_2384_call(relay.reshape(const_9532.astype('bool'), [8, 13, 2]), relay.reshape(var_9533.astype('uint8'), [72,]), ), 4)
output = relay.Tuple([call_9517,call_9531,const_9532,var_9533,])
output2 = relay.Tuple([call_9518,call_9534,const_9532,var_9533,])
func_9541 = relay.Function([var_9533,], output)
mod['func_9541'] = func_9541
mod = relay.transform.InferType()(mod)
mutated_mod['func_9541'] = func_9541
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9542 = relay.var("var_9542", dtype = "uint8", shape = (72,))#candidate|9542|(72,)|var|uint8
func_9541_call = mutated_mod.get_global_var('func_9541')
call_9543 = func_9541_call(var_9542)
output = call_9543
func_9544 = relay.Function([var_9542], output)
mutated_mod['func_9544'] = func_9544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8089_call = mod.get_global_var('func_8089')
func_8090_call = mutated_mod.get_global_var('func_8090')
call_9553 = func_8089_call()
call_9554 = func_8089_call()
output = call_9553
output2 = call_9554
func_9575 = relay.Function([], output)
mod['func_9575'] = func_9575
mod = relay.transform.InferType()(mod)
output = func_9575()
func_9576 = relay.Function([], output)
mutated_mod['func_9576'] = func_9576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8292_call = mod.get_global_var('func_8292')
func_8293_call = mutated_mod.get_global_var('func_8293')
call_9577 = func_8292_call()
call_9578 = func_8292_call()
output = relay.Tuple([call_9577,])
output2 = relay.Tuple([call_9578,])
func_9600 = relay.Function([], output)
mod['func_9600'] = func_9600
mod = relay.transform.InferType()(mod)
mutated_mod['func_9600'] = func_9600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9600_call = mutated_mod.get_global_var('func_9600')
call_9601 = func_9600_call()
output = call_9601
func_9602 = relay.Function([], output)
mutated_mod['func_9602'] = func_9602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_9603 = relay.TupleGetItem(func_7172_call(), 2)
call_9604 = relay.TupleGetItem(func_7173_call(), 2)
output = call_9603
output2 = call_9604
func_9608 = relay.Function([], output)
mod['func_9608'] = func_9608
mod = relay.transform.InferType()(mod)
mutated_mod['func_9608'] = func_9608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9608_call = mutated_mod.get_global_var('func_9608')
call_9609 = func_9608_call()
output = call_9609
func_9610 = relay.Function([], output)
mutated_mod['func_9610'] = func_9610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9363_call = mod.get_global_var('func_9363')
func_9365_call = mutated_mod.get_global_var('func_9365')
call_9615 = relay.TupleGetItem(func_9363_call(), 0)
call_9616 = relay.TupleGetItem(func_9365_call(), 0)
output = relay.Tuple([call_9615,])
output2 = relay.Tuple([call_9616,])
func_9620 = relay.Function([], output)
mod['func_9620'] = func_9620
mod = relay.transform.InferType()(mod)
mutated_mod['func_9620'] = func_9620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9620_call = mutated_mod.get_global_var('func_9620')
call_9621 = func_9620_call()
output = call_9621
func_9622 = relay.Function([], output)
mutated_mod['func_9622'] = func_9622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9575_call = mod.get_global_var('func_9575')
func_9576_call = mutated_mod.get_global_var('func_9576')
call_9633 = func_9575_call()
call_9634 = func_9575_call()
output = call_9633
output2 = call_9634
func_9651 = relay.Function([], output)
mod['func_9651'] = func_9651
mod = relay.transform.InferType()(mod)
mutated_mod['func_9651'] = func_9651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9651_call = mutated_mod.get_global_var('func_9651')
call_9652 = func_9651_call()
output = call_9652
func_9653 = relay.Function([], output)
mutated_mod['func_9653'] = func_9653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9488_call = mod.get_global_var('func_9488')
func_9489_call = mutated_mod.get_global_var('func_9489')
call_9675 = relay.TupleGetItem(func_9488_call(), 0)
call_9676 = relay.TupleGetItem(func_9489_call(), 0)
output = call_9675
output2 = call_9676
func_9677 = relay.Function([], output)
mod['func_9677'] = func_9677
mod = relay.transform.InferType()(mod)
mutated_mod['func_9677'] = func_9677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9677_call = mutated_mod.get_global_var('func_9677')
call_9678 = func_9677_call()
output = call_9678
func_9679 = relay.Function([], output)
mutated_mod['func_9679'] = func_9679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7845_call = mod.get_global_var('func_7845')
func_7847_call = mutated_mod.get_global_var('func_7847')
call_9705 = relay.TupleGetItem(func_7845_call(), 0)
call_9706 = relay.TupleGetItem(func_7847_call(), 0)
output = relay.Tuple([call_9705,])
output2 = relay.Tuple([call_9706,])
func_9726 = relay.Function([], output)
mod['func_9726'] = func_9726
mod = relay.transform.InferType()(mod)
mutated_mod['func_9726'] = func_9726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mutated_mod.get_global_var('func_9726')
call_9727 = func_9726_call()
output = call_9727
func_9728 = relay.Function([], output)
mutated_mod['func_9728'] = func_9728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9600_call = mod.get_global_var('func_9600')
func_9602_call = mutated_mod.get_global_var('func_9602')
call_9737 = relay.TupleGetItem(func_9600_call(), 0)
call_9738 = relay.TupleGetItem(func_9602_call(), 0)
output = call_9737
output2 = call_9738
func_9773 = relay.Function([], output)
mod['func_9773'] = func_9773
mod = relay.transform.InferType()(mod)
mutated_mod['func_9773'] = func_9773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9773_call = mutated_mod.get_global_var('func_9773')
call_9774 = func_9773_call()
output = call_9774
func_9775 = relay.Function([], output)
mutated_mod['func_9775'] = func_9775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8089_call = mod.get_global_var('func_8089')
func_8090_call = mutated_mod.get_global_var('func_8090')
call_9783 = func_8089_call()
call_9784 = func_8089_call()
func_8931_call = mod.get_global_var('func_8931')
func_8936_call = mutated_mod.get_global_var('func_8936')
const_9798 = relay.const(5.711527, dtype = "float32")#candidate|9798|()|const|float32
const_9799 = relay.const([[8.989009,-9.694497,-8.378305,7.723465,-5.999334,3.462596,5.185046,7.731943,7.446879,-3.135578],[-1.647888,8.073940,2.063547,5.481109,9.930441,-8.125255,-5.541412,-5.910682,4.903262,5.744661],[0.942534,-3.839684,5.765678,-3.886150,3.273417,0.555483,-8.035833,-6.683299,3.252658,1.525756],[0.472285,-8.296733,-9.639913,1.480925,-1.522383,3.268523,9.236910,-7.009750,-1.474646,2.061541],[2.673109,2.969297,-3.502674,5.016723,8.315149,-2.544842,8.074964,5.318559,1.343771,5.520107],[5.517057,-5.875676,-6.456019,9.555565,1.680485,7.130659,-1.101612,-3.903736,-1.817812,-1.502890],[-2.638840,-1.618642,7.076306,1.555809,-1.796109,-5.928440,-3.409881,3.635761,5.820430,3.980341],[4.084904,4.432868,9.030749,-0.323303,-2.581175,0.754135,-7.767684,-5.591099,0.953545,-3.087319],[-3.804396,7.108051,7.747621,5.651741,-1.425755,4.834986,6.313135,6.308751,-7.286985,-8.894952],[-2.540970,6.235511,-7.215280,6.506312,-9.525866,6.108453,-6.977136,3.266859,8.249888,1.005199],[6.960242,-0.990616,5.773553,5.301266,1.650993,-1.173790,3.363022,-0.090990,9.026142,-5.242946],[-2.954836,-7.594655,-9.849997,-2.607619,6.200899,2.365177,6.711731,4.825263,0.769204,-5.651689],[0.500295,6.976689,1.478532,-6.731846,6.601477,-6.151917,-4.678685,-7.450759,-9.893582,9.301735],[-7.586812,-3.432280,-3.238704,9.095091,-5.718148,-4.751848,-4.541503,-8.771503,-5.038806,1.357490],[3.396795,7.882677,-5.572678,8.435462,-4.776630,-3.755183,0.306751,-2.948259,7.758254,-4.082830],[-0.290528,5.556740,-0.605907,-9.918076,-9.764003,-8.509420,4.361565,2.169822,9.539950,-7.847292],[3.740721,5.746468,7.074878,-9.761321,4.456116,-4.737826,-1.028003,-1.837207,2.241177,9.466666],[-3.797182,-2.537170,0.551084,-3.328725,-2.356348,-3.462999,3.922252,-3.070083,-6.644831,7.865430],[6.525759,8.837255,8.836959,-9.926230,-2.762410,-8.370189,7.334167,-2.551208,5.863078,-1.398270],[0.189373,9.612607,-7.066861,7.168859,7.630250,-4.582017,-6.642107,-0.747752,7.065505,-8.079014],[-1.371430,5.913626,8.358862,-9.345387,-5.025667,-7.043756,1.340988,-3.079098,-5.528011,-5.263849],[4.737312,-5.840144,-1.363961,7.687426,-2.810596,8.013490,1.003225,-4.832956,-8.476550,2.867829],[7.409913,-5.941251,2.552634,-6.549625,-6.843072,2.553122,4.531494,8.473771,-6.602063,-1.233860],[7.337527,3.808512,-6.442408,5.334178,-2.307534,3.115879,3.736586,9.885447,-6.344903,-5.347050]], dtype = "float32")#candidate|9799|(24, 10)|const|float32
var_9800 = relay.var("var_9800", dtype = "bool", shape = (208,))#candidate|9800|(208,)|var|bool
call_9797 = relay.TupleGetItem(func_8931_call(relay.reshape(const_9798.astype('float32'), []), relay.reshape(const_9799.astype('float32'), [240,]), relay.reshape(var_9800.astype('bool'), [1, 208]), ), 0)
call_9801 = relay.TupleGetItem(func_8936_call(relay.reshape(const_9798.astype('float32'), []), relay.reshape(const_9799.astype('float32'), [240,]), relay.reshape(var_9800.astype('bool'), [1, 208]), ), 0)
output = relay.Tuple([call_9783,call_9797,const_9798,const_9799,var_9800,])
output2 = relay.Tuple([call_9784,call_9801,const_9798,const_9799,var_9800,])
func_9802 = relay.Function([var_9800,], output)
mod['func_9802'] = func_9802
mod = relay.transform.InferType()(mod)
var_9803 = relay.var("var_9803", dtype = "bool", shape = (208,))#candidate|9803|(208,)|var|bool
output = func_9802(var_9803)
func_9804 = relay.Function([var_9803], output)
mutated_mod['func_9804'] = func_9804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_9820 = relay.TupleGetItem(func_7172_call(), 1)
call_9821 = relay.TupleGetItem(func_7173_call(), 1)
output = call_9820
output2 = call_9821
func_9827 = relay.Function([], output)
mod['func_9827'] = func_9827
mod = relay.transform.InferType()(mod)
output = func_9827()
func_9828 = relay.Function([], output)
mutated_mod['func_9828'] = func_9828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_9945 = func_7228_call()
call_9946 = func_7228_call()
output = relay.Tuple([call_9945,])
output2 = relay.Tuple([call_9946,])
func_9961 = relay.Function([], output)
mod['func_9961'] = func_9961
mod = relay.transform.InferType()(mod)
output = func_9961()
func_9962 = relay.Function([], output)
mutated_mod['func_9962'] = func_9962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8065_call = mod.get_global_var('func_8065')
func_8067_call = mutated_mod.get_global_var('func_8067')
call_9988 = relay.TupleGetItem(func_8065_call(), 0)
call_9989 = relay.TupleGetItem(func_8067_call(), 0)
output = call_9988
output2 = call_9989
func_9994 = relay.Function([], output)
mod['func_9994'] = func_9994
mod = relay.transform.InferType()(mod)
mutated_mod['func_9994'] = func_9994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9994_call = mutated_mod.get_global_var('func_9994')
call_9995 = func_9994_call()
output = call_9995
func_9996 = relay.Function([], output)
mutated_mod['func_9996'] = func_9996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9773_call = mod.get_global_var('func_9773')
func_9775_call = mutated_mod.get_global_var('func_9775')
call_10018 = func_9773_call()
call_10019 = func_9773_call()
func_9488_call = mod.get_global_var('func_9488')
func_9489_call = mutated_mod.get_global_var('func_9489')
call_10031 = relay.TupleGetItem(func_9488_call(), 0)
call_10032 = relay.TupleGetItem(func_9489_call(), 0)
func_5731_call = mod.get_global_var('func_5731')
func_5736_call = mutated_mod.get_global_var('func_5736')
const_10045 = relay.const([[-1.379650,-7.093806],[-0.841571,3.121700],[7.442334,7.294779],[7.802113,-6.980290],[-7.732221,4.593341],[-0.587221,-7.406817],[8.771573,-8.471597],[-2.834301,3.556084],[-3.398347,-9.457099],[7.062798,-5.584802],[-4.316944,6.198914],[-7.448125,2.208845],[-1.186646,8.666691],[-6.322979,9.594757],[5.387058,-6.820075],[2.155491,-6.511306],[4.359493,-0.780094],[-6.570422,7.455108],[6.515418,-8.751703],[-1.199227,-6.043038],[5.573424,1.182345],[2.396701,4.605589],[-5.614640,3.605743],[8.680627,1.523367],[-1.852765,4.085805],[-9.515756,-4.643503],[7.391117,-9.528466],[-9.804338,-4.088470],[-8.906030,-6.553637],[-0.645555,-1.087445],[2.058002,-8.526967],[4.146555,0.286892],[-6.979939,-7.713738],[1.292503,-7.187906],[-2.460568,0.503831],[0.315029,-6.786306],[5.943728,-7.557568],[-7.961058,1.422059],[-7.094415,-2.385536],[4.079582,8.463489],[5.562322,0.226276],[-0.599762,4.869217],[-8.178456,-1.747519],[7.526820,4.640858],[1.051940,-5.387026],[-7.073199,1.266011],[-8.218654,-1.549400],[3.169654,9.327246],[8.865042,3.250038],[-9.260018,-3.271683],[5.988409,-2.969929],[4.195839,-8.951924],[1.199250,-6.453333],[-6.361905,-9.949328],[-5.862093,-5.513863],[5.431349,-0.399993],[-4.699094,-2.601649],[-6.376390,9.116033],[2.788282,-4.363150],[1.181347,4.227867],[-6.383284,-9.793596],[9.132582,5.704299],[8.088239,7.418973],[4.714511,-0.014406],[-9.209094,-0.136684],[1.323033,-9.522143],[9.169895,-8.758123],[1.070210,-4.885038],[0.842220,-3.906408],[1.368260,-3.149511],[-8.716943,3.134674],[3.371100,1.443760],[4.013842,3.275534],[-6.761728,0.565201],[-9.822805,-9.750695],[-9.490862,2.757552],[-3.540069,-2.722133],[2.778128,-4.281195],[4.633864,3.440735],[2.110686,-7.971249],[-8.687242,-1.207071],[4.849084,5.788322],[1.270184,-5.785729],[-0.303850,3.915591],[0.029237,-7.956426],[7.603479,-9.478590],[3.907081,6.472293],[4.316458,6.704077],[7.069373,-3.675751],[8.642169,3.190434],[4.672614,-6.837698],[2.462128,-6.073354],[-8.632882,-5.857325],[-0.952567,-2.636546],[-8.563311,-6.995849],[6.609117,-2.545612],[5.979430,7.489175],[-1.054889,4.112032],[-8.482039,5.325359],[-9.637669,2.462359],[-0.463799,-6.605592],[-6.811691,-3.296993],[-6.073933,-8.619912],[-9.331016,9.125078],[4.563890,6.720739],[4.754810,-7.395101],[-7.040463,6.078767],[6.717917,9.443108],[-5.254843,-2.724503],[-1.083221,-0.230607],[-5.805457,-3.581717],[3.920053,-7.493248],[6.797618,-2.255792],[9.682843,-9.083837],[-9.219135,-9.912217],[-4.849415,8.291983],[1.408512,-9.653366],[5.369728,-0.796091],[1.281660,-0.571781],[-9.347040,-1.579965],[-3.754640,-6.596226],[4.746566,-9.492489],[3.908798,4.116073],[-5.843411,-7.479054],[6.144366,-4.199726],[4.742753,-1.227730],[1.762699,2.569135],[7.503675,2.318247],[-1.073295,6.266465],[0.650730,5.213653],[-7.253026,-2.256668],[-8.877911,-0.618170],[8.327111,-7.973069],[-7.120650,-4.870439],[1.865658,4.666320],[7.855173,6.970982],[0.598286,1.950810],[-0.700736,4.164689],[8.922520,8.261523],[-2.356041,1.535412],[-2.558184,5.070896],[-0.510260,3.556995],[1.087721,8.257974],[4.746139,3.040590],[4.851987,9.710870],[2.075837,7.170034],[8.333855,-0.501876],[-5.062069,8.743204],[9.969616,5.473083],[-1.740069,-2.379569],[-8.201268,-6.948732],[-7.799214,-4.637985],[-7.366730,8.162331],[-5.012622,8.535488],[8.973275,8.859176],[0.065432,9.810242],[9.500621,8.709451],[5.687406,-5.580257],[3.330252,0.998463],[-9.851340,0.296644],[-6.572314,-4.583791],[8.986193,-8.350400],[-6.404899,9.200951],[-5.644401,-9.511275],[6.380091,-5.299866],[5.697292,-0.376301],[8.543307,-7.384728],[2.261350,9.485574],[-6.629759,-8.449898],[7.943889,2.352377],[4.215285,9.070369],[3.566126,4.814942],[7.663530,9.355031],[-5.540092,8.206476],[2.654836,8.280496],[-3.189880,-8.047569],[6.516766,-0.658372],[8.847502,-0.864378],[-0.514240,1.301043],[1.362861,0.056081],[-0.690573,-7.282591],[-2.272024,-2.319593],[6.820040,2.970634],[-0.798856,0.938733],[-8.852268,-3.930398],[9.786332,-8.959659],[3.775827,2.164425],[1.033877,7.983151],[8.921835,-7.788641],[-0.930217,3.357836],[9.178504,8.226896],[0.709627,7.966464],[-1.380631,6.318306],[-1.197593,-9.558174],[7.658307,-6.074404],[-0.128646,-8.451899],[8.007398,4.801116],[-0.930281,-8.399482],[6.582656,9.092971],[-5.166669,0.221724],[2.380779,-9.076253],[-6.562217,5.112261],[-5.282320,-2.900248],[3.922771,-4.622137],[-4.043459,-0.808131],[-3.306342,-7.798037],[-2.269479,-7.885118],[-2.949510,-9.941018],[5.170891,2.929914],[1.503098,3.744772],[-3.872387,-7.081917],[4.308541,5.828593],[-0.618094,-8.487084],[-4.712852,3.035752],[-8.342438,5.071245],[0.865071,-3.512001],[-0.066928,-6.071733],[-3.274491,6.809867],[-5.027445,4.488498],[-4.777444,3.644786]], dtype = "float64")#candidate|10045|(220, 2)|const|float64
var_10046 = relay.var("var_10046", dtype = "float32", shape = (720,))#candidate|10046|(720,)|var|float32
var_10047 = relay.var("var_10047", dtype = "uint8", shape = ())#candidate|10047|()|var|uint8
var_10048 = relay.var("var_10048", dtype = "float32", shape = (245,))#candidate|10048|(245,)|var|float32
call_10044 = relay.TupleGetItem(func_5731_call(relay.reshape(const_10045.astype('float64'), [11, 8, 5]), relay.reshape(var_10046.astype('float32'), [720,]), relay.reshape(var_10047.astype('uint8'), []), relay.reshape(var_10048.astype('float32'), [245,]), ), 8)
call_10049 = relay.TupleGetItem(func_5736_call(relay.reshape(const_10045.astype('float64'), [11, 8, 5]), relay.reshape(var_10046.astype('float32'), [720,]), relay.reshape(var_10047.astype('uint8'), []), relay.reshape(var_10048.astype('float32'), [245,]), ), 8)
func_8292_call = mod.get_global_var('func_8292')
func_8293_call = mutated_mod.get_global_var('func_8293')
call_10050 = func_8292_call()
call_10051 = func_8292_call()
var_10053 = relay.var("var_10053", dtype = "float32", shape = (245,))#candidate|10053|(245,)|var|float32
bop_10054 = relay.right_shift(var_10048.astype('uint16'), relay.reshape(var_10053.astype('uint16'), relay.shape_of(var_10048))) # shape=(245,)
output = relay.Tuple([call_10018,call_10031,call_10044,const_10045,var_10046,var_10047,call_10050,bop_10054,])
output2 = relay.Tuple([call_10019,call_10032,call_10049,const_10045,var_10046,var_10047,call_10051,bop_10054,])
func_10057 = relay.Function([var_10046,var_10047,var_10048,var_10053,], output)
mod['func_10057'] = func_10057
mod = relay.transform.InferType()(mod)
var_10058 = relay.var("var_10058", dtype = "float32", shape = (720,))#candidate|10058|(720,)|var|float32
var_10059 = relay.var("var_10059", dtype = "uint8", shape = ())#candidate|10059|()|var|uint8
var_10060 = relay.var("var_10060", dtype = "float32", shape = (245,))#candidate|10060|(245,)|var|float32
var_10061 = relay.var("var_10061", dtype = "float32", shape = (245,))#candidate|10061|(245,)|var|float32
output = func_10057(var_10058,var_10059,var_10060,var_10061,)
func_10062 = relay.Function([var_10058,var_10059,var_10060,var_10061,], output)
mutated_mod['func_10062'] = func_10062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9677_call = mod.get_global_var('func_9677')
func_9679_call = mutated_mod.get_global_var('func_9679')
call_10072 = func_9677_call()
call_10073 = func_9677_call()
output = call_10072
output2 = call_10073
func_10082 = relay.Function([], output)
mod['func_10082'] = func_10082
mod = relay.transform.InferType()(mod)
mutated_mod['func_10082'] = func_10082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10082_call = mutated_mod.get_global_var('func_10082')
call_10083 = func_10082_call()
output = call_10083
func_10084 = relay.Function([], output)
mutated_mod['func_10084'] = func_10084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10146 = relay.var("var_10146", dtype = "float32", shape = ())#candidate|10146|()|var|float32
const_10147 = relay.const([[[7.682736,-9.886663,-5.272322,7.764762,-6.479507],[1.253995,-7.810331,3.626699,-2.190119,9.272277],[7.742537,5.912123,-2.454999,7.556528,-5.720177],[8.747710,4.057045,-5.902755,0.942138,5.973028],[-4.386501,9.479299,-7.659772,1.527118,6.212676],[0.567645,1.879349,2.043349,2.094894,1.649623],[8.671754,1.995817,-9.076307,-7.373060,-9.426438],[6.211734,-4.607239,0.928841,2.863531,6.406931],[-9.747658,-0.446631,-0.025331,4.508272,-4.168874]],[[9.558499,-9.226524,-9.401243,-1.063273,-0.185198],[-2.155407,-0.479328,-7.601719,-5.132370,-5.520889],[-7.218797,-1.674371,-7.123726,-0.667912,9.120833],[-0.886669,-9.521180,9.240574,9.092408,1.675123],[-5.344243,7.801989,-3.070347,7.807878,-9.460938],[7.464662,-5.993761,1.833506,-9.964281,-7.314671],[-6.452066,-8.109602,3.214756,-3.950326,7.070829],[-8.791278,1.949577,-8.580681,4.409517,-1.475023],[-6.072588,7.103396,-1.710559,2.926491,-2.301165]],[[-4.273896,3.708442,-8.321263,-3.852818,6.235993],[-7.423486,-6.065654,-5.998204,-3.499497,-2.197215],[5.395325,-2.904794,8.373835,5.698890,5.486711],[-2.702529,-0.231005,-2.943721,7.359418,1.867155],[-4.325266,-0.508653,-6.772610,-5.719110,5.214556],[4.666532,4.413659,7.387931,-4.314635,5.416222],[-9.337189,3.019310,9.136397,6.628068,6.109639],[-0.068637,3.429951,-3.245180,9.281006,-9.325819],[4.192387,0.507222,1.759255,4.599587,9.384351]],[[4.364850,-0.182831,-4.632824,-1.431419,-5.111693],[1.480674,6.073675,-4.523561,-8.957310,-7.250107],[-7.245716,-2.196332,-9.246102,-4.561886,-2.906553],[0.501870,8.679993,-4.400789,6.190638,-9.936434],[-3.449879,-6.584499,-4.597394,9.088351,-1.186554],[2.392703,1.448880,-7.820020,6.626704,2.946722],[-9.491878,3.797025,0.792379,-0.538532,-0.024570],[-2.481490,-0.069121,-2.448546,8.889520,9.272935],[-7.013800,-1.680174,-8.334187,9.001728,5.205082]]], dtype = "float32")#candidate|10147|(4, 9, 5)|const|float32
bop_10148 = relay.mod(var_10146.astype('float32'), const_10147.astype('float32')) # shape=(4, 9, 5)
output = bop_10148
output2 = bop_10148
func_10168 = relay.Function([var_10146,], output)
mod['func_10168'] = func_10168
mod = relay.transform.InferType()(mod)
mutated_mod['func_10168'] = func_10168
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10169 = relay.var("var_10169", dtype = "float32", shape = ())#candidate|10169|()|var|float32
func_10168_call = mutated_mod.get_global_var('func_10168')
call_10170 = func_10168_call(var_10169)
output = call_10170
func_10171 = relay.Function([var_10169], output)
mutated_mod['func_10171'] = func_10171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9608_call = mod.get_global_var('func_9608')
func_9610_call = mutated_mod.get_global_var('func_9610')
call_10181 = func_9608_call()
call_10182 = func_9608_call()
output = relay.Tuple([call_10181,])
output2 = relay.Tuple([call_10182,])
func_10191 = relay.Function([], output)
mod['func_10191'] = func_10191
mod = relay.transform.InferType()(mod)
mutated_mod['func_10191'] = func_10191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10191_call = mutated_mod.get_global_var('func_10191')
call_10192 = func_10191_call()
output = call_10192
func_10193 = relay.Function([], output)
mutated_mod['func_10193'] = func_10193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7845_call = mod.get_global_var('func_7845')
func_7847_call = mutated_mod.get_global_var('func_7847')
call_10210 = relay.TupleGetItem(func_7845_call(), 0)
call_10211 = relay.TupleGetItem(func_7847_call(), 0)
output = call_10210
output2 = call_10211
func_10239 = relay.Function([], output)
mod['func_10239'] = func_10239
mod = relay.transform.InferType()(mod)
output = func_10239()
func_10240 = relay.Function([], output)
mutated_mod['func_10240'] = func_10240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7729_call = mod.get_global_var('func_7729')
func_7730_call = mutated_mod.get_global_var('func_7730')
call_10297 = relay.TupleGetItem(func_7729_call(), 0)
call_10298 = relay.TupleGetItem(func_7730_call(), 0)
output = call_10297
output2 = call_10298
func_10301 = relay.Function([], output)
mod['func_10301'] = func_10301
mod = relay.transform.InferType()(mod)
mutated_mod['func_10301'] = func_10301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10301_call = mutated_mod.get_global_var('func_10301')
call_10302 = func_10301_call()
output = call_10302
func_10303 = relay.Function([], output)
mutated_mod['func_10303'] = func_10303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10239_call = mod.get_global_var('func_10239')
func_10240_call = mutated_mod.get_global_var('func_10240')
call_10335 = func_10239_call()
call_10336 = func_10239_call()
output = relay.Tuple([call_10335,])
output2 = relay.Tuple([call_10336,])
func_10338 = relay.Function([], output)
mod['func_10338'] = func_10338
mod = relay.transform.InferType()(mod)
output = func_10338()
func_10339 = relay.Function([], output)
mutated_mod['func_10339'] = func_10339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mod.get_global_var('func_9726')
func_9728_call = mutated_mod.get_global_var('func_9728')
call_10343 = relay.TupleGetItem(func_9726_call(), 0)
call_10344 = relay.TupleGetItem(func_9728_call(), 0)
func_579_call = mod.get_global_var('func_579')
func_582_call = mutated_mod.get_global_var('func_582')
const_10363 = relay.const([[-4.456567,-2.128021,-4.641815,8.939526,0.323060,2.158189,8.038444,5.881819,-0.047412,-1.416738,4.187669,-4.219913,-4.547378,4.349099,-3.086318,-3.394859,8.837552,-8.125666,-5.061477,6.764414,2.223997,9.275015,2.401111,7.453933,3.738915,6.753412,-3.569691,6.492020,-6.279142,7.840048,-7.452126,2.571657,2.459187,0.277271,9.005555,1.786556,8.662432,6.325120,7.129141,-2.163762,2.145400,-4.133539,-0.511759,-9.074622,-5.094935,9.706374,0.957955,-7.828606,-8.684792,3.753451,-2.667917,0.009296,5.371567,2.940777,0.044310,-9.580886,7.891009,7.799941,-2.264291,-3.254916,6.519170,4.627279,-9.036938,3.831430,-3.992678,-6.831320,-0.268735,-6.805273,1.679278,-9.472344,-5.334773,8.415765,0.220191,9.745853,-2.994691,-4.310506,4.650874,-7.775645,5.868196,-9.711071,-1.830593,9.636210,-2.692507,2.602474,8.635264,8.265615,-5.068389,3.089849,3.425373,4.539364,4.421723,6.189033,-5.577719,-5.878477,-8.691637,1.390253,-4.533820,1.776573,-1.304555,-9.038574,-3.849322,5.420707,-5.262008,7.098793,8.005857,7.177230,-4.238650,8.781585,-2.519349,7.125045,6.214923,-6.467144,0.942912,-6.010488,-9.244126,2.551376,-8.596970,0.078182,5.494302,-2.235951,2.442390,8.587477,2.298960,-5.829301,0.450415,-4.435796,-5.708261,-1.742433,-9.797470,-4.360375,5.599411,2.026916,-1.523473,-7.914306,4.946037,8.539837,-9.141871,0.217098,4.551241,4.354453,3.751382,6.156080,-3.193700,6.749732,5.816006,8.067865,0.113319,-5.649962,2.824354,6.185973]], dtype = "float32")#candidate|10363|(1, 150)|const|float32
call_10362 = func_579_call(relay.reshape(const_10363.astype('float32'), [10, 15, 1]))
call_10364 = func_579_call(relay.reshape(const_10363.astype('float32'), [10, 15, 1]))
func_10239_call = mod.get_global_var('func_10239')
func_10240_call = mutated_mod.get_global_var('func_10240')
call_10374 = func_10239_call()
call_10375 = func_10239_call()
var_10392 = relay.var("var_10392", dtype = "float32", shape = (11, 150))#candidate|10392|(11, 150)|var|float32
bop_10393 = relay.logical_xor(const_10363.astype('uint16'), var_10392.astype('uint16')) # shape=(11, 150)
output = relay.Tuple([call_10343,call_10362,call_10374,bop_10393,])
output2 = relay.Tuple([call_10344,call_10364,call_10375,bop_10393,])
func_10400 = relay.Function([var_10392,], output)
mod['func_10400'] = func_10400
mod = relay.transform.InferType()(mod)
mutated_mod['func_10400'] = func_10400
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10401 = relay.var("var_10401", dtype = "float32", shape = (11, 150))#candidate|10401|(11, 150)|var|float32
func_10400_call = mutated_mod.get_global_var('func_10400')
call_10402 = func_10400_call(var_10401)
output = call_10402
func_10403 = relay.Function([var_10401], output)
mutated_mod['func_10403'] = func_10403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9677_call = mod.get_global_var('func_9677')
func_9679_call = mutated_mod.get_global_var('func_9679')
call_10435 = func_9677_call()
call_10436 = func_9677_call()
output = call_10435
output2 = call_10436
func_10437 = relay.Function([], output)
mod['func_10437'] = func_10437
mod = relay.transform.InferType()(mod)
mutated_mod['func_10437'] = func_10437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10437_call = mutated_mod.get_global_var('func_10437')
call_10438 = func_10437_call()
output = call_10438
func_10439 = relay.Function([], output)
mutated_mod['func_10439'] = func_10439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10191_call = mod.get_global_var('func_10191')
func_10193_call = mutated_mod.get_global_var('func_10193')
call_10454 = relay.TupleGetItem(func_10191_call(), 0)
call_10455 = relay.TupleGetItem(func_10193_call(), 0)
output = call_10454
output2 = call_10455
func_10462 = relay.Function([], output)
mod['func_10462'] = func_10462
mod = relay.transform.InferType()(mod)
mutated_mod['func_10462'] = func_10462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10462_call = mutated_mod.get_global_var('func_10462')
call_10463 = func_10462_call()
output = call_10463
func_10464 = relay.Function([], output)
mutated_mod['func_10464'] = func_10464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_10468 = relay.TupleGetItem(func_7413_call(), 2)
call_10469 = relay.TupleGetItem(func_7415_call(), 2)
func_10239_call = mod.get_global_var('func_10239')
func_10240_call = mutated_mod.get_global_var('func_10240')
call_10524 = func_10239_call()
call_10525 = func_10239_call()
func_7917_call = mod.get_global_var('func_7917')
func_7923_call = mutated_mod.get_global_var('func_7923')
var_10529 = relay.var("var_10529", dtype = "float32", shape = ())#candidate|10529|()|var|float32
const_10530 = relay.const([4.986347,-3.362616,1.017790,-1.633110,-8.028877,2.394045,2.244091,5.593384,-5.983543,-6.119296,3.619451,1.547725,-0.956237,-5.427170,-6.269803,4.039105,2.895781,-5.119717,4.971365,-1.782776,6.087353,-0.958097,8.824760,-3.318687,5.128104,3.749586,-1.978115,1.085317,-0.532571,-8.537485,2.886812,-0.957253,0.741121,2.209630,-7.195132,-0.778162,-9.343697,-6.311404,-4.561564,3.007272,4.053302,5.517889,4.810904,-1.456630,-4.163229,3.690123,7.984978,-9.742378,-0.184970,1.361279,8.396959,-5.523771,-5.458400,0.098837,-5.724725,8.942317,-2.098712,7.103076,3.573460,0.598729,-4.376410,2.927692,4.646046,7.860643,-7.685499,-9.006770,-5.893418,4.311788,2.779207,-2.941339,5.153000,-3.580741,-5.356139,4.588709,6.722362,7.932017,1.888705,3.698674,-3.173432,-6.892401,-3.407346,-6.832366,-4.654553,5.086677,-1.380112,8.276146,5.472711,8.943591,3.450692,2.858319,-7.644451,-6.899106,-9.676775,-1.949384,-2.971388,5.077465,8.712280,-1.867181,0.981856,1.819134,6.786054,9.388824,-5.559389,-8.877771,6.256725,0.159323,-5.112660,-1.149792,4.562836,7.419529,6.350903,-9.632633,-1.215599,-5.561745,6.606973,8.192827,-5.893718,2.841740,-1.253465,-4.881144,-5.467297,0.643859,-0.027146,3.614320,-8.183842,7.823365,2.894484,-2.009873,-6.564491,0.089619,-2.360979,-8.139052,3.867658,-1.234279,3.517485,3.797467,-0.823275,-8.426297,-4.030699,-9.140483,-0.735049,9.545829,-9.146193,2.011969,-3.947623,-3.027819,-5.679460,-0.657549,-0.259060,4.126364,4.123834,0.545899,8.711966,-0.140530,0.572864,-0.308654,8.920218,7.692325,1.252380,-7.779258,6.868886,-9.448285,-3.797320,9.071796,8.548651,-6.718745,-1.527333,-4.694739,-3.512422,4.355644,-1.462112,7.498703,0.773099,8.689703,-0.802714,4.208452,-9.221498,5.824464,-3.229653,1.908406,9.551047,-5.027473,-9.814360,8.346461,-1.486903,-1.603667,-7.089088,-1.860212,3.688690,-0.906210,1.321350,1.556550,1.129047,-1.243739,-3.915606,-3.397836,-2.988481,8.117063,5.492688,5.374166,5.673523,-9.282947,8.679843,-6.704090,-1.634401,-0.389701,-2.124920,0.951491,-2.735964,6.628109,-5.533892,-3.462127,-5.579702,2.007389,-1.329741,4.400238,-4.075358,1.184377,-4.060643,-0.903658,-8.676224,0.970312,4.384191,6.517671,-8.331025,-2.777665,-8.319337,3.910311,-3.445451,-0.133257,3.446645,-8.625853,-1.118723,-1.562373,5.689916,1.436629,5.458384,-7.011262,-3.141848,5.021815,-9.745799,3.679402,-3.057991,-5.788108,4.676000,-0.404529,-8.439436,-6.680738,-0.317681,-6.707407,-9.724410,-5.372439,-5.112018,-5.307608,-3.655389,5.894929,5.487699,1.319266,-5.499325,-2.954608,-5.530362,-3.510462,6.425747,5.332824,3.183822,-3.774313,-3.832468,-7.758591,1.701637,2.768096,-5.569374,7.807780,7.417328,9.406564,-9.185755,8.274487,-6.067843,9.567488,-2.344054,-2.533661,-0.780413,6.734753,9.638499,3.304935,-3.665382,-5.371638,-3.545740,-5.455169,-3.618479,3.569449,9.399948,8.604085,-9.512744,-6.579160,-4.421826,2.678247,7.593162,0.002767,-6.827286,7.252630,9.650753,6.915160,3.752697,6.693625,3.469949,-6.686297,5.358287,2.574223,5.756354,-2.304770,-6.862756,-3.734078,1.247472,-8.114619,4.336004,-2.442960,7.095805,-2.535643,-4.289895,-9.590409,-6.414999,-0.431877,-1.559216,7.165125,2.187708,5.789728,1.895019,0.566446,5.905941,-9.268577,-2.446239,4.459477,-4.619271,-8.142342,2.833878,5.153900,-2.005798,2.490932,5.024326,-4.899078,8.974903,-8.317380,9.475004,6.377072,7.022162,3.356466,-7.984456,3.125830,-0.445817,9.675624,-3.587725,4.960740,2.479850,8.674019,-9.162584,9.684097,-4.218763,-8.801673,-9.600524,-3.750797,-8.444836,2.002281,7.836491,4.292033,-2.456240,4.650630,9.239435,8.394034,-9.601866,5.368493,-1.376653,-6.246187,-1.390652,0.719131,-9.770240,-1.720716,7.637516,4.000949,-3.939124,0.767878,-6.238548,6.671172,0.119301,-2.954394,-4.020446,-1.562931,-7.181030,7.091966,-6.300297,8.656261,-4.216101,6.438133,3.809316,-9.137608,6.745795,8.726413,5.059150,-2.359081,7.591804,-7.295166,-4.041754,4.260066,0.097715,-1.006214,0.209312,-7.731370,4.501952,4.024189,-3.993442,9.599913,2.001078,5.885159,1.430614,-1.793053,-9.737094,-0.587349,9.638405,-2.782598,-6.610394,-0.622442,-1.042979,-0.606033,-0.828409,0.790832,8.082108,1.954242,5.286600,3.230124,-9.310730,3.015115,-8.869304,6.007233,7.356077,-6.879913,-2.897342,4.151745,1.017484,1.556221,-4.451390,4.012943,6.703101,-0.390005,4.353799,7.294042,9.523166,5.382665,0.098507,-4.369114,-0.692858,-3.876606,7.740904,1.292765,2.821920,7.230508,5.276117,-4.723405,3.278671,2.772043,-9.521233,-7.550463,-6.207386,-5.965276,-4.468525,-6.759819,2.373242,-9.162635,1.234797,-3.913829,-1.922910,-6.512295,-2.317806,-3.417270,9.563539,-9.320928,-8.490250,-3.740878,-7.411677,-4.368666,1.286876,6.974784,-2.041432,3.224014,-3.785904,-2.446613,4.325606,-2.674692,8.503928,7.291210,9.143883,1.582370,-8.753390,-2.276145,-8.211946,-9.028656,2.978513,-9.835265,5.179164,9.013597,4.812142,-1.332925,-5.775670,-3.960330,6.183260,6.217961,-1.061636,-1.749429,-1.997805,7.984688,-5.853907,-3.254398,-0.239283,1.926542,-7.591182,1.195387,-4.996590,9.930470,-5.805079,7.140149,2.801227,-4.071050,3.431739,3.521192,9.654480,-2.620589,-3.793268,-2.068176,1.955524,-7.769703,-3.423173,-4.458571,4.582558,-6.259117,7.964678,2.058914,-4.681943,-5.581896,-9.748609,2.378257,8.057167,9.517584,-4.691424,-9.269317,7.279542,0.111795,-5.281401,9.883224,9.434190,6.175918,8.476845,-3.271909,2.082082,0.789962,-8.314520,9.254289,-9.389195,2.932418,-8.741865,-8.257293,-2.484745,-7.526031,7.632246,-7.648282,5.998773,-9.919495,-3.078680,-8.786669,2.215273,5.669251,-2.506770,4.161553,-3.692958,0.364128,-2.204673,-3.557743,9.774857,1.363628,-7.123690,-5.484036,-9.284387,-7.960715,2.345908,-3.642593,-2.854644,-8.553025,-6.302105,5.064801,-1.334866,-3.719891,4.251280,6.960622,0.683700,8.230719,-4.916377,8.214121,-5.761707,3.447464,-6.512138,7.877022,2.447992,9.574035], dtype = "float32")#candidate|10530|(600,)|const|float32
const_10531 = relay.const([[False,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True],[False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,True,False],[False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True],[True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True]], dtype = "bool")#candidate|10531|(4, 52)|const|bool
const_10532 = relay.const([[0.315950,-3.873974,-2.476715,-1.318349,2.479214,-6.383660,-3.390565,5.612648,-0.779163,9.130590,-5.473369,-0.108768,-9.342378,1.394684,1.478222,-8.287482,-7.672872,6.705314,0.308649,7.979895,4.654162,-4.192928,8.911773,-7.270988,-8.099332,-9.239038,-7.379936,-9.987125,-3.876822,9.041343,-5.570764,0.174545,4.382183,8.616640,-8.326517,7.556794,7.072329,1.435910,4.654505,-0.767637,4.785886,-5.819551,-9.191788,-5.955802,-4.186505,-6.579563,5.514507,6.085872,-1.125808,-8.091199,1.019371,-6.775732,5.076351,2.044588,1.848553,9.052737,-3.330880,3.321109,-4.935893,-5.959704,7.880646,7.591342,-4.504770,7.036072,3.868495,2.356574,6.057767,2.522002,6.142265,0.139973,1.573959,5.672188,2.951591,-3.554101,7.888053,-8.365358,3.470267,1.686292,6.820627,-3.035827,-4.857177,6.322951,6.890387,9.791109,-1.295043,-7.624850,0.355837,6.552628,-9.770770,-1.702460,-0.463559,-1.931996,-1.535848,9.641060,4.086080,-7.738334,2.062387,3.153958,7.454710,6.148315,-0.890861,8.714425,-8.909338,-5.886253,-8.358569,-8.501899,2.334578,-6.240757,-8.755693,5.230093,8.347643,-6.418607,-9.308910,4.413913,-0.443642,3.951055,-6.845359,-5.588979,6.056933,0.184078,2.448043,3.723343,9.015699,-7.665992,1.929122,2.596693,4.829306,-9.580127,8.372790,5.113952,-9.825074,-6.659510,5.472813,7.379190,9.093471,-8.926071,-5.613543,-1.987283,1.434938,-5.220059,-8.186371,2.355495,4.203619,6.593049,-3.133306,-3.099989,1.801344,5.353422,9.166734,-7.711225,-6.306615,3.499117,-8.370370,-8.303611,-5.738564,-7.739100,-7.170941,-4.692349,7.219824,-8.350163,7.892005,9.240149,-7.837262,6.923506,7.890287,-5.840931,7.477997,7.246578,1.991007,7.894008,-0.823407,9.567643,-2.569206,-6.689159,3.528226,7.322686,0.792623,-1.227131,1.998800,0.137594],[6.421135,-3.985748,3.733113,-5.804748,9.666540,-2.008289,7.895992,-7.551770,2.404989,-0.445123,-5.947082,1.722845,-7.221862,2.059811,-3.213148,-5.554500,-5.415274,-5.653688,-7.680181,7.462872,-5.927300,2.178790,3.518880,9.144754,-2.655567,6.874773,2.689729,-3.812031,-0.082349,-9.581696,-8.942128,-3.001400,2.170703,-4.842738,2.207614,-9.726008,2.469767,-0.828469,3.213280,-8.022388,1.963605,-6.242928,-8.042570,-7.898889,-2.844761,1.219092,7.025279,-9.642999,-7.671212,4.364880,-0.818736,-2.737491,4.185912,-0.676482,-9.477412,1.390887,-2.915222,9.101734,-1.913250,-0.604260,-8.486561,-2.926545,0.066847,-8.900334,1.084318,-6.829728,2.529024,-3.340988,6.154246,-9.657017,8.658174,1.667376,3.444128,-0.566942,-2.937098,1.097181,0.028683,-1.204138,-8.978303,-2.440085,-9.023881,0.926478,3.752950,2.512128,-4.597404,5.814884,2.946370,5.633337,6.783544,-6.472505,-2.327074,-4.340322,9.798446,7.889170,6.520394,-9.172663,-8.290681,-7.430873,6.938863,-6.401160,0.102872,0.093398,-1.661736,6.642087,-6.792156,9.202674,2.567815,-6.163266,-7.465196,-0.868172,-6.569057,-0.766334,-8.007308,-9.294807,-9.733848,3.468336,-2.970544,-9.738272,-9.900454,-8.526161,4.819790,6.920425,8.007566,-5.533012,2.271818,-6.893297,7.974528,-2.742345,4.634222,0.176894,4.781161,9.459394,0.972199,-9.146374,6.186858,-2.300074,-2.534486,-6.244044,-7.049034,-2.163795,4.778838,8.558754,5.522787,2.401506,-6.586240,-3.185225,0.665924,-4.677385,8.456655,-2.831020,4.262883,3.369729,8.811655,-2.323100,-4.466271,3.297489,2.884824,-0.804197,8.508386,3.998337,-2.398218,1.454938,4.418389,-1.867307,9.421383,2.063327,-5.636614,-3.786845,-2.433879,3.498034,9.823323,5.944612,3.677695,4.217986,9.778902,-7.966551,-9.009693,3.220820,4.931590,-9.856154],[1.746796,-5.827536,6.164575,5.066937,8.409597,-8.920095,1.582580,4.467280,-0.683512,9.581627,7.168013,6.205794,-7.909464,4.650921,2.930008,-4.453774,3.659825,-3.662347,3.527434,5.471530,-9.781669,-4.814631,0.772406,-2.713670,-9.792238,3.607571,7.239247,-9.047866,0.273278,-6.755562,4.218947,7.727104,2.641929,2.088906,3.275126,4.871764,2.239713,-1.739943,4.919528,-6.949902,-8.321572,3.173801,-5.925651,2.434958,3.385247,-6.679909,-0.675880,2.116067,6.702250,3.172153,7.020514,-8.362628,-1.527970,2.333240,5.505689,2.473692,3.233368,-4.582495,-2.508015,-9.694284,4.433895,5.042397,-3.123091,3.404016,9.138511,3.250606,6.680678,9.472624,-8.230183,6.257337,-3.472637,1.937081,6.527691,-7.828029,-1.230033,0.268736,3.359409,4.419458,1.420582,-5.971517,8.986392,-8.327230,2.876848,-2.811022,-5.018379,-0.762803,0.282555,6.294878,2.488638,-1.268380,-2.352920,6.148615,-8.393148,8.950977,6.055732,3.061331,8.141128,8.162748,0.171933,-5.135192,5.230638,6.219122,3.328657,9.151315,-3.151408,-4.321653,6.199544,-2.278486,-9.974462,1.350041,7.348892,8.326245,-6.655033,-7.058053,-3.519016,-9.537372,1.025874,-7.637155,-1.079200,6.790115,-6.044065,3.612815,9.587793,9.485654,4.577532,5.913662,8.251386,-8.440097,2.918101,-4.082067,4.801269,3.099038,-0.552604,5.833953,9.501636,8.298881,-8.738597,5.729717,-3.914879,-0.896812,8.328014,3.859922,-4.631737,3.797330,-5.180081,4.764227,-4.943143,-8.185787,5.382140,1.684497,-5.005854,-7.388158,7.462251,-8.232887,-1.955109,8.891012,-2.414170,4.343821,-2.194353,-3.136932,-5.305140,5.867750,-6.150733,0.875851,6.705274,-9.363022,8.745536,6.591574,-7.432307,-8.068763,-6.380169,-7.573000,-1.375874,9.975634,-7.858692,4.462917,1.847023,6.153784,-5.093010,6.496926],[3.984761,4.681930,-6.309510,4.119262,-5.228017,-5.993145,-4.402269,6.735437,-6.750726,9.093128,-9.622911,7.126410,0.586995,1.831838,8.976118,-7.068387,-1.394154,6.665393,-0.784904,3.433183,-8.193421,6.280487,6.087215,-4.463619,3.844615,-1.387548,-9.735656,2.418822,1.744806,-2.809698,-2.131426,9.993380,-7.572242,8.066327,-2.626146,-8.079879,-6.841994,0.807954,-0.901990,1.509033,9.522822,-1.936871,7.025392,-7.644304,-5.502357,3.000655,0.721423,-8.350959,3.118875,-6.292868,-3.372506,9.510000,-4.361414,-4.304391,-6.563708,-6.629205,-3.832340,9.086479,-6.143555,-6.345993,-2.804534,9.756796,-6.971903,-2.906629,-1.166199,6.698272,7.874177,5.353142,2.216189,-3.910709,-7.555965,-6.844748,6.238445,-6.196926,4.120648,9.399794,6.714407,2.884414,-5.851204,7.807831,-7.828819,9.981258,6.227878,1.984890,7.618762,-1.428346,-5.868917,-4.499421,3.800716,4.224404,4.375746,-4.779491,-8.991924,-2.902456,1.416497,8.062573,9.035110,0.231145,3.549126,0.168413,7.326890,-4.868794,-8.322175,3.518857,-2.635327,-9.500002,1.830282,-8.898056,-8.208442,-9.181006,-5.151213,7.759193,7.813626,2.889230,1.920296,0.322203,-5.466436,-9.751550,-7.776146,-9.503874,0.353446,-8.200830,-9.703933,-5.714607,8.590663,-0.097026,-9.635100,7.871865,5.671630,-4.901617,-9.877357,6.004157,-6.293117,8.470642,6.021697,8.682717,6.992560,-7.793987,-1.754258,-9.124985,7.443961,3.784750,0.001068,2.138531,1.802116,3.833315,7.928703,1.181478,0.406531,-3.665808,-9.637050,8.178044,7.076126,7.094108,-1.384974,-6.069198,2.560937,3.711668,-8.131093,6.413989,-6.748429,8.580324,8.529083,0.013812,-4.474843,6.005018,1.279099,-6.951807,-4.768774,-3.662869,5.023982,6.440699,8.728971,3.640559,4.925525,3.257682,-4.833829,-2.822591,8.527919,-1.384513]], dtype = "float32")#candidate|10532|(4, 180)|const|float32
call_10528 = relay.TupleGetItem(func_7917_call(relay.reshape(var_10529.astype('float32'), []), relay.reshape(const_10530.astype('float32'), [300, 2]), relay.reshape(const_10531.astype('bool'), [208,]), relay.reshape(const_10532.astype('float32'), [720,]), ), 1)
call_10533 = relay.TupleGetItem(func_7923_call(relay.reshape(var_10529.astype('float32'), []), relay.reshape(const_10530.astype('float32'), [300, 2]), relay.reshape(const_10531.astype('bool'), [208,]), relay.reshape(const_10532.astype('float32'), [720,]), ), 1)
bop_10535 = relay.logical_xor(var_10529.astype('int16'), const_10531.astype('int16')) # shape=(4, 52)
func_10057_call = mod.get_global_var('func_10057')
func_10062_call = mutated_mod.get_global_var('func_10062')
var_10563 = relay.var("var_10563", dtype = "float32", shape = (245,))#candidate|10563|(245,)|var|float32
call_10562 = relay.TupleGetItem(func_10057_call(relay.reshape(const_10532.astype('float32'), [720,]), relay.reshape(var_10529.astype('uint8'), []), relay.reshape(var_10563.astype('float32'), [245,]), relay.reshape(var_10563.astype('float32'), [245,]), ), 0)
call_10564 = relay.TupleGetItem(func_10062_call(relay.reshape(const_10532.astype('float32'), [720,]), relay.reshape(var_10529.astype('uint8'), []), relay.reshape(var_10563.astype('float32'), [245,]), relay.reshape(var_10563.astype('float32'), [245,]), ), 0)
func_9726_call = mod.get_global_var('func_9726')
func_9728_call = mutated_mod.get_global_var('func_9728')
call_10567 = relay.TupleGetItem(func_9726_call(), 0)
call_10568 = relay.TupleGetItem(func_9728_call(), 0)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_10570 = func_7228_call()
call_10571 = func_7228_call()
func_3812_call = mod.get_global_var('func_3812')
func_3820_call = mutated_mod.get_global_var('func_3820')
const_10573 = relay.const([False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,False], dtype = "bool")#candidate|10573|(624,)|const|bool
call_10572 = relay.TupleGetItem(func_3812_call(relay.reshape(var_10529.astype('float32'), []), relay.reshape(const_10530.astype('float32'), [10, 6, 10]), relay.reshape(call_10570.astype('uint16'), [300,]), relay.reshape(call_10528.astype('float32'), [18, 2]), relay.reshape(const_10531.astype('bool'), [1, 208]), relay.reshape(const_10573.astype('bool'), [3, 208]), relay.reshape(const_10532.astype('float32'), [60, 12]), ), 6)
call_10574 = relay.TupleGetItem(func_3820_call(relay.reshape(var_10529.astype('float32'), []), relay.reshape(const_10530.astype('float32'), [10, 6, 10]), relay.reshape(call_10570.astype('uint16'), [300,]), relay.reshape(call_10528.astype('float32'), [18, 2]), relay.reshape(const_10531.astype('bool'), [1, 208]), relay.reshape(const_10573.astype('bool'), [3, 208]), relay.reshape(const_10532.astype('float32'), [60, 12]), ), 6)
output = relay.Tuple([call_10468,call_10524,call_10528,const_10530,const_10532,bop_10535,call_10562,var_10563,call_10567,call_10570,call_10572,const_10573,])
output2 = relay.Tuple([call_10469,call_10525,call_10533,const_10530,const_10532,bop_10535,call_10564,var_10563,call_10568,call_10571,call_10574,const_10573,])
func_10576 = relay.Function([var_10529,var_10563,], output)
mod['func_10576'] = func_10576
mod = relay.transform.InferType()(mod)
mutated_mod['func_10576'] = func_10576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10576_call = mutated_mod.get_global_var('func_10576')
var_10578 = relay.var("var_10578", dtype = "float32", shape = ())#candidate|10578|()|var|float32
var_10579 = relay.var("var_10579", dtype = "float32", shape = (245,))#candidate|10579|(245,)|var|float32
call_10577 = func_10576_call(var_10578,var_10579,)
output = call_10577
func_10580 = relay.Function([var_10578,var_10579,], output)
mutated_mod['func_10580'] = func_10580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9363_call = mod.get_global_var('func_9363')
func_9365_call = mutated_mod.get_global_var('func_9365')
call_10589 = relay.TupleGetItem(func_9363_call(), 0)
call_10590 = relay.TupleGetItem(func_9365_call(), 0)
output = relay.Tuple([call_10589,])
output2 = relay.Tuple([call_10590,])
func_10612 = relay.Function([], output)
mod['func_10612'] = func_10612
mod = relay.transform.InferType()(mod)
mutated_mod['func_10612'] = func_10612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10612_call = mutated_mod.get_global_var('func_10612')
call_10613 = func_10612_call()
output = call_10613
func_10614 = relay.Function([], output)
mutated_mod['func_10614'] = func_10614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8065_call = mod.get_global_var('func_8065')
func_8067_call = mutated_mod.get_global_var('func_8067')
call_10636 = relay.TupleGetItem(func_8065_call(), 0)
call_10637 = relay.TupleGetItem(func_8067_call(), 0)
func_9726_call = mod.get_global_var('func_9726')
func_9728_call = mutated_mod.get_global_var('func_9728')
call_10642 = relay.TupleGetItem(func_9726_call(), 0)
call_10643 = relay.TupleGetItem(func_9728_call(), 0)
output = relay.Tuple([call_10636,call_10642,])
output2 = relay.Tuple([call_10637,call_10643,])
func_10690 = relay.Function([], output)
mod['func_10690'] = func_10690
mod = relay.transform.InferType()(mod)
mutated_mod['func_10690'] = func_10690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10690_call = mutated_mod.get_global_var('func_10690')
call_10691 = func_10690_call()
output = call_10691
func_10692 = relay.Function([], output)
mutated_mod['func_10692'] = func_10692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9994_call = mod.get_global_var('func_9994')
func_9996_call = mutated_mod.get_global_var('func_9996')
call_10693 = func_9994_call()
call_10694 = func_9994_call()
output = relay.Tuple([call_10693,])
output2 = relay.Tuple([call_10694,])
func_10699 = relay.Function([], output)
mod['func_10699'] = func_10699
mod = relay.transform.InferType()(mod)
output = func_10699()
func_10700 = relay.Function([], output)
mutated_mod['func_10700'] = func_10700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_10780 = relay.TupleGetItem(func_7501_call(), 0)
call_10781 = relay.TupleGetItem(func_7502_call(), 0)
output = relay.Tuple([call_10780,])
output2 = relay.Tuple([call_10781,])
func_10788 = relay.Function([], output)
mod['func_10788'] = func_10788
mod = relay.transform.InferType()(mod)
mutated_mod['func_10788'] = func_10788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10788_call = mutated_mod.get_global_var('func_10788')
call_10789 = func_10788_call()
output = call_10789
func_10790 = relay.Function([], output)
mutated_mod['func_10790'] = func_10790
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10809 = relay.var("var_10809", dtype = "uint32", shape = (3, 7, 3))#candidate|10809|(3, 7, 3)|var|uint32
var_10810 = relay.var("var_10810", dtype = "uint32", shape = (3, 7, 3))#candidate|10810|(3, 7, 3)|var|uint32
bop_10811 = relay.left_shift(var_10809.astype('uint32'), relay.reshape(var_10810.astype('uint32'), relay.shape_of(var_10809))) # shape=(3, 7, 3)
output = relay.Tuple([bop_10811,])
output2 = relay.Tuple([bop_10811,])
func_10814 = relay.Function([var_10809,var_10810,], output)
mod['func_10814'] = func_10814
mod = relay.transform.InferType()(mod)
mutated_mod['func_10814'] = func_10814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10814_call = mutated_mod.get_global_var('func_10814')
var_10816 = relay.var("var_10816", dtype = "uint32", shape = (3, 7, 3))#candidate|10816|(3, 7, 3)|var|uint32
var_10817 = relay.var("var_10817", dtype = "uint32", shape = (3, 7, 3))#candidate|10817|(3, 7, 3)|var|uint32
call_10815 = func_10814_call(var_10816,var_10817,)
output = call_10815
func_10818 = relay.Function([var_10816,var_10817,], output)
mutated_mod['func_10818'] = func_10818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9827_call = mod.get_global_var('func_9827')
func_9828_call = mutated_mod.get_global_var('func_9828')
call_10838 = func_9827_call()
call_10839 = func_9827_call()
func_8065_call = mod.get_global_var('func_8065')
func_8067_call = mutated_mod.get_global_var('func_8067')
call_10847 = relay.TupleGetItem(func_8065_call(), 0)
call_10848 = relay.TupleGetItem(func_8067_call(), 0)
output = relay.Tuple([call_10838,call_10847,])
output2 = relay.Tuple([call_10839,call_10848,])
func_10872 = relay.Function([], output)
mod['func_10872'] = func_10872
mod = relay.transform.InferType()(mod)
output = func_10872()
func_10873 = relay.Function([], output)
mutated_mod['func_10873'] = func_10873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8849_call = mod.get_global_var('func_8849')
func_8850_call = mutated_mod.get_global_var('func_8850')
call_10890 = func_8849_call()
call_10891 = func_8849_call()
func_6693_call = mod.get_global_var('func_6693')
func_6697_call = mutated_mod.get_global_var('func_6697')
var_10895 = relay.var("var_10895", dtype = "uint32", shape = ())#candidate|10895|()|var|uint32
var_10896 = relay.var("var_10896", dtype = "uint32", shape = (728,))#candidate|10896|(728,)|var|uint32
var_10897 = relay.var("var_10897", dtype = "float64", shape = (8, 66))#candidate|10897|(8, 66)|var|float64
call_10894 = relay.TupleGetItem(func_6693_call(relay.reshape(var_10895.astype('uint32'), []), relay.reshape(var_10896.astype('uint32'), [8, 13, 7]), relay.reshape(var_10897.astype('float64'), [528,]), ), 0)
call_10898 = relay.TupleGetItem(func_6697_call(relay.reshape(var_10895.astype('uint32'), []), relay.reshape(var_10896.astype('uint32'), [8, 13, 7]), relay.reshape(var_10897.astype('float64'), [528,]), ), 0)
func_9134_call = mod.get_global_var('func_9134')
func_9137_call = mutated_mod.get_global_var('func_9137')
const_10900 = relay.const([5,1,-1,-1,-3,-10,6,-5,10,-4,1,-4,4,9,5,9,-2,-8,-1,7,1,-2,-7,9,-1,8,-3,-8,6,-2,7,-8,2,-4,-6,-6,-10,3,-7,7,-5,7,5,-7,-3,1,10,1,-9,4,-7,10,1,7,8,-6,-8,3,8,-6,10,-5,1,4,-2,-3,1,8,-9,-9,-8,-9], dtype = "uint8")#candidate|10900|(72,)|const|uint8
call_10899 = relay.TupleGetItem(func_9134_call(relay.reshape(const_10900.astype('uint8'), [72,])), 0)
call_10901 = relay.TupleGetItem(func_9137_call(relay.reshape(const_10900.astype('uint8'), [72,])), 0)
func_10057_call = mod.get_global_var('func_10057')
func_10062_call = mutated_mod.get_global_var('func_10062')
var_10921 = relay.var("var_10921", dtype = "float32", shape = (720,))#candidate|10921|(720,)|var|float32
var_10922 = relay.var("var_10922", dtype = "float32", shape = (35, 7))#candidate|10922|(35, 7)|var|float32
call_10920 = relay.TupleGetItem(func_10057_call(relay.reshape(var_10921.astype('float32'), [720,]), relay.reshape(var_10895.astype('uint8'), []), relay.reshape(var_10922.astype('float32'), [245,]), relay.reshape(var_10922.astype('float32'), [245,]), ), 3)
call_10923 = relay.TupleGetItem(func_10062_call(relay.reshape(var_10921.astype('float32'), [720,]), relay.reshape(var_10895.astype('uint8'), []), relay.reshape(var_10922.astype('float32'), [245,]), relay.reshape(var_10922.astype('float32'), [245,]), ), 3)
output = relay.Tuple([call_10890,call_10894,var_10895,var_10896,var_10897,call_10899,const_10900,call_10920,var_10921,var_10922,])
output2 = relay.Tuple([call_10891,call_10898,var_10895,var_10896,var_10897,call_10901,const_10900,call_10923,var_10921,var_10922,])
func_10926 = relay.Function([var_10895,var_10896,var_10897,var_10921,var_10922,], output)
mod['func_10926'] = func_10926
mod = relay.transform.InferType()(mod)
var_10927 = relay.var("var_10927", dtype = "uint32", shape = ())#candidate|10927|()|var|uint32
var_10928 = relay.var("var_10928", dtype = "uint32", shape = (728,))#candidate|10928|(728,)|var|uint32
var_10929 = relay.var("var_10929", dtype = "float64", shape = (8, 66))#candidate|10929|(8, 66)|var|float64
var_10930 = relay.var("var_10930", dtype = "float32", shape = (720,))#candidate|10930|(720,)|var|float32
var_10931 = relay.var("var_10931", dtype = "float32", shape = (35, 7))#candidate|10931|(35, 7)|var|float32
output = func_10926(var_10927,var_10928,var_10929,var_10930,var_10931,)
func_10932 = relay.Function([var_10927,var_10928,var_10929,var_10930,var_10931,], output)
mutated_mod['func_10932'] = func_10932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_10944 = relay.TupleGetItem(func_7413_call(), 0)
call_10945 = relay.TupleGetItem(func_7415_call(), 0)
output = call_10944
output2 = call_10945
func_10961 = relay.Function([], output)
mod['func_10961'] = func_10961
mod = relay.transform.InferType()(mod)
mutated_mod['func_10961'] = func_10961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10961_call = mutated_mod.get_global_var('func_10961')
call_10962 = func_10961_call()
output = call_10962
func_10963 = relay.Function([], output)
mutated_mod['func_10963'] = func_10963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8849_call = mod.get_global_var('func_8849')
func_8850_call = mutated_mod.get_global_var('func_8850')
call_11007 = func_8849_call()
call_11008 = func_8849_call()
func_10788_call = mod.get_global_var('func_10788')
func_10790_call = mutated_mod.get_global_var('func_10790')
call_11045 = relay.TupleGetItem(func_10788_call(), 0)
call_11046 = relay.TupleGetItem(func_10790_call(), 0)
func_10814_call = mod.get_global_var('func_10814')
func_10818_call = mutated_mod.get_global_var('func_10818')
var_11085 = relay.var("var_11085", dtype = "uint32", shape = (63,))#candidate|11085|(63,)|var|uint32
call_11084 = relay.TupleGetItem(func_10814_call(relay.reshape(var_11085.astype('uint32'), [3, 7, 3]), relay.reshape(var_11085.astype('uint32'), [3, 7, 3]), ), 0)
call_11086 = relay.TupleGetItem(func_10818_call(relay.reshape(var_11085.astype('uint32'), [3, 7, 3]), relay.reshape(var_11085.astype('uint32'), [3, 7, 3]), ), 0)
func_8089_call = mod.get_global_var('func_8089')
func_8090_call = mutated_mod.get_global_var('func_8090')
call_11088 = func_8089_call()
call_11089 = func_8089_call()
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
const_11093 = relay.const(-9, dtype = "uint8")#candidate|11093|()|const|uint8
var_11094 = relay.var("var_11094", dtype = "uint8", shape = (72,))#candidate|11094|(72,)|var|uint8
var_11095 = relay.var("var_11095", dtype = "float32", shape = (75, 2))#candidate|11095|(75, 2)|var|float32
call_11092 = relay.TupleGetItem(func_1678_call(relay.reshape(const_11093.astype('uint8'), []), relay.reshape(var_11094.astype('uint8'), [6, 2, 6]), relay.reshape(var_11095.astype('float32'), [150,]), ), 5)
call_11096 = relay.TupleGetItem(func_1682_call(relay.reshape(const_11093.astype('uint8'), []), relay.reshape(var_11094.astype('uint8'), [6, 2, 6]), relay.reshape(var_11095.astype('float32'), [150,]), ), 5)
func_10690_call = mod.get_global_var('func_10690')
func_10692_call = mutated_mod.get_global_var('func_10692')
call_11118 = relay.TupleGetItem(func_10690_call(), 1)
call_11119 = relay.TupleGetItem(func_10692_call(), 1)
output = relay.Tuple([call_11007,call_11045,call_11084,var_11085,call_11088,call_11092,const_11093,var_11094,var_11095,call_11118,])
output2 = relay.Tuple([call_11008,call_11046,call_11086,var_11085,call_11089,call_11096,const_11093,var_11094,var_11095,call_11119,])
func_11122 = relay.Function([var_11085,var_11094,var_11095,], output)
mod['func_11122'] = func_11122
mod = relay.transform.InferType()(mod)
var_11123 = relay.var("var_11123", dtype = "uint32", shape = (63,))#candidate|11123|(63,)|var|uint32
var_11124 = relay.var("var_11124", dtype = "uint8", shape = (72,))#candidate|11124|(72,)|var|uint8
var_11125 = relay.var("var_11125", dtype = "float32", shape = (75, 2))#candidate|11125|(75, 2)|var|float32
output = func_11122(var_11123,var_11124,var_11125,)
func_11126 = relay.Function([var_11123,var_11124,var_11125,], output)
mutated_mod['func_11126'] = func_11126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8849_call = mod.get_global_var('func_8849')
func_8850_call = mutated_mod.get_global_var('func_8850')
call_11257 = func_8849_call()
call_11258 = func_8849_call()
output = relay.Tuple([call_11257,])
output2 = relay.Tuple([call_11258,])
func_11259 = relay.Function([], output)
mod['func_11259'] = func_11259
mod = relay.transform.InferType()(mod)
mutated_mod['func_11259'] = func_11259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11259_call = mutated_mod.get_global_var('func_11259')
call_11260 = func_11259_call()
output = call_11260
func_11261 = relay.Function([], output)
mutated_mod['func_11261'] = func_11261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9600_call = mod.get_global_var('func_9600')
func_9602_call = mutated_mod.get_global_var('func_9602')
call_11276 = relay.TupleGetItem(func_9600_call(), 0)
call_11277 = relay.TupleGetItem(func_9602_call(), 0)
output = call_11276
output2 = call_11277
func_11287 = relay.Function([], output)
mod['func_11287'] = func_11287
mod = relay.transform.InferType()(mod)
mutated_mod['func_11287'] = func_11287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11287_call = mutated_mod.get_global_var('func_11287')
call_11288 = func_11287_call()
output = call_11288
func_11289 = relay.Function([], output)
mutated_mod['func_11289'] = func_11289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10690_call = mod.get_global_var('func_10690')
func_10692_call = mutated_mod.get_global_var('func_10692')
call_11311 = relay.TupleGetItem(func_10690_call(), 1)
call_11312 = relay.TupleGetItem(func_10692_call(), 1)
output = call_11311
output2 = call_11312
func_11336 = relay.Function([], output)
mod['func_11336'] = func_11336
mod = relay.transform.InferType()(mod)
output = func_11336()
func_11337 = relay.Function([], output)
mutated_mod['func_11337'] = func_11337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10437_call = mod.get_global_var('func_10437')
func_10439_call = mutated_mod.get_global_var('func_10439')
call_11364 = func_10437_call()
call_11365 = func_10437_call()
output = relay.Tuple([call_11364,])
output2 = relay.Tuple([call_11365,])
func_11367 = relay.Function([], output)
mod['func_11367'] = func_11367
mod = relay.transform.InferType()(mod)
output = func_11367()
func_11368 = relay.Function([], output)
mutated_mod['func_11368'] = func_11368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10690_call = mod.get_global_var('func_10690')
func_10692_call = mutated_mod.get_global_var('func_10692')
call_11379 = relay.TupleGetItem(func_10690_call(), 0)
call_11380 = relay.TupleGetItem(func_10692_call(), 0)
output = call_11379
output2 = call_11380
func_11381 = relay.Function([], output)
mod['func_11381'] = func_11381
mod = relay.transform.InferType()(mod)
mutated_mod['func_11381'] = func_11381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11381_call = mutated_mod.get_global_var('func_11381')
call_11382 = func_11381_call()
output = call_11382
func_11383 = relay.Function([], output)
mutated_mod['func_11383'] = func_11383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10191_call = mod.get_global_var('func_10191')
func_10193_call = mutated_mod.get_global_var('func_10193')
call_11411 = relay.TupleGetItem(func_10191_call(), 0)
call_11412 = relay.TupleGetItem(func_10193_call(), 0)
output = relay.Tuple([call_11411,])
output2 = relay.Tuple([call_11412,])
func_11415 = relay.Function([], output)
mod['func_11415'] = func_11415
mod = relay.transform.InferType()(mod)
output = func_11415()
func_11416 = relay.Function([], output)
mutated_mod['func_11416'] = func_11416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_11468 = func_7228_call()
call_11469 = func_7228_call()
output = relay.Tuple([call_11468,])
output2 = relay.Tuple([call_11469,])
func_11473 = relay.Function([], output)
mod['func_11473'] = func_11473
mod = relay.transform.InferType()(mod)
mutated_mod['func_11473'] = func_11473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11473_call = mutated_mod.get_global_var('func_11473')
call_11474 = func_11473_call()
output = call_11474
func_11475 = relay.Function([], output)
mutated_mod['func_11475'] = func_11475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mod.get_global_var('func_9726')
func_9728_call = mutated_mod.get_global_var('func_9728')
call_11513 = relay.TupleGetItem(func_9726_call(), 0)
call_11514 = relay.TupleGetItem(func_9728_call(), 0)
output = call_11513
output2 = call_11514
func_11517 = relay.Function([], output)
mod['func_11517'] = func_11517
mod = relay.transform.InferType()(mod)
output = func_11517()
func_11518 = relay.Function([], output)
mutated_mod['func_11518'] = func_11518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9363_call = mod.get_global_var('func_9363')
func_9365_call = mutated_mod.get_global_var('func_9365')
call_11519 = relay.TupleGetItem(func_9363_call(), 0)
call_11520 = relay.TupleGetItem(func_9365_call(), 0)
func_4176_call = mod.get_global_var('func_4176')
func_4179_call = mutated_mod.get_global_var('func_4179')
const_11532 = relay.const([False,True,True,False,False,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,True,False,False,True,True], dtype = "bool")#candidate|11532|(208,)|const|bool
call_11531 = relay.TupleGetItem(func_4176_call(relay.reshape(const_11532.astype('bool'), [1, 208])), 6)
call_11533 = relay.TupleGetItem(func_4179_call(relay.reshape(const_11532.astype('bool'), [1, 208])), 6)
uop_11539 = relay.log10(call_11531.astype('float32')) # shape=(1, 208)
uop_11541 = relay.log10(call_11533.astype('float32')) # shape=(1, 208)
output = relay.Tuple([call_11519,const_11532,uop_11539,])
output2 = relay.Tuple([call_11520,const_11532,uop_11541,])
func_11569 = relay.Function([], output)
mod['func_11569'] = func_11569
mod = relay.transform.InferType()(mod)
output = func_11569()
func_11570 = relay.Function([], output)
mutated_mod['func_11570'] = func_11570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9363_call = mod.get_global_var('func_9363')
func_9365_call = mutated_mod.get_global_var('func_9365')
call_11608 = relay.TupleGetItem(func_9363_call(), 0)
call_11609 = relay.TupleGetItem(func_9365_call(), 0)
output = relay.Tuple([call_11608,])
output2 = relay.Tuple([call_11609,])
func_11614 = relay.Function([], output)
mod['func_11614'] = func_11614
mod = relay.transform.InferType()(mod)
output = func_11614()
func_11615 = relay.Function([], output)
mutated_mod['func_11615'] = func_11615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8711_call = mod.get_global_var('func_8711')
func_8713_call = mutated_mod.get_global_var('func_8713')
call_11647 = relay.TupleGetItem(func_8711_call(), 0)
call_11648 = relay.TupleGetItem(func_8713_call(), 0)
output = call_11647
output2 = call_11648
func_11664 = relay.Function([], output)
mod['func_11664'] = func_11664
mod = relay.transform.InferType()(mod)
mutated_mod['func_11664'] = func_11664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11664_call = mutated_mod.get_global_var('func_11664')
call_11665 = func_11664_call()
output = call_11665
func_11666 = relay.Function([], output)
mutated_mod['func_11666'] = func_11666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10612_call = mod.get_global_var('func_10612')
func_10614_call = mutated_mod.get_global_var('func_10614')
call_11672 = relay.TupleGetItem(func_10612_call(), 0)
call_11673 = relay.TupleGetItem(func_10614_call(), 0)
func_11381_call = mod.get_global_var('func_11381')
func_11383_call = mutated_mod.get_global_var('func_11383')
call_11679 = func_11381_call()
call_11680 = func_11381_call()
func_8065_call = mod.get_global_var('func_8065')
func_8067_call = mutated_mod.get_global_var('func_8067')
call_11693 = relay.TupleGetItem(func_8065_call(), 0)
call_11694 = relay.TupleGetItem(func_8067_call(), 0)
output = relay.Tuple([call_11672,call_11679,call_11693,])
output2 = relay.Tuple([call_11673,call_11680,call_11694,])
func_11701 = relay.Function([], output)
mod['func_11701'] = func_11701
mod = relay.transform.InferType()(mod)
mutated_mod['func_11701'] = func_11701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11701_call = mutated_mod.get_global_var('func_11701')
call_11702 = func_11701_call()
output = call_11702
func_11703 = relay.Function([], output)
mutated_mod['func_11703'] = func_11703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7845_call = mod.get_global_var('func_7845')
func_7847_call = mutated_mod.get_global_var('func_7847')
call_11759 = relay.TupleGetItem(func_7845_call(), 0)
call_11760 = relay.TupleGetItem(func_7847_call(), 0)
output = relay.Tuple([call_11759,])
output2 = relay.Tuple([call_11760,])
func_11807 = relay.Function([], output)
mod['func_11807'] = func_11807
mod = relay.transform.InferType()(mod)
output = func_11807()
func_11808 = relay.Function([], output)
mutated_mod['func_11808'] = func_11808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_11832 = relay.TupleGetItem(func_7172_call(), 3)
call_11833 = relay.TupleGetItem(func_7173_call(), 3)
func_11701_call = mod.get_global_var('func_11701')
func_11703_call = mutated_mod.get_global_var('func_11703')
call_11858 = relay.TupleGetItem(func_11701_call(), 1)
call_11859 = relay.TupleGetItem(func_11703_call(), 1)
func_11367_call = mod.get_global_var('func_11367')
func_11368_call = mutated_mod.get_global_var('func_11368')
call_11882 = relay.TupleGetItem(func_11367_call(), 0)
call_11883 = relay.TupleGetItem(func_11368_call(), 0)
output = relay.Tuple([call_11832,call_11858,call_11882,])
output2 = relay.Tuple([call_11833,call_11859,call_11883,])
func_11888 = relay.Function([], output)
mod['func_11888'] = func_11888
mod = relay.transform.InferType()(mod)
mutated_mod['func_11888'] = func_11888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11888_call = mutated_mod.get_global_var('func_11888')
call_11889 = func_11888_call()
output = call_11889
func_11890 = relay.Function([], output)
mutated_mod['func_11890'] = func_11890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9773_call = mod.get_global_var('func_9773')
func_9775_call = mutated_mod.get_global_var('func_9775')
call_12084 = func_9773_call()
call_12085 = func_9773_call()
output = relay.Tuple([call_12084,])
output2 = relay.Tuple([call_12085,])
func_12095 = relay.Function([], output)
mod['func_12095'] = func_12095
mod = relay.transform.InferType()(mod)
mutated_mod['func_12095'] = func_12095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12095_call = mutated_mod.get_global_var('func_12095')
call_12096 = func_12095_call()
output = call_12096
func_12097 = relay.Function([], output)
mutated_mod['func_12097'] = func_12097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_12129 = relay.TupleGetItem(func_7413_call(), 1)
call_12130 = relay.TupleGetItem(func_7415_call(), 1)
output = relay.Tuple([call_12129,])
output2 = relay.Tuple([call_12130,])
func_12151 = relay.Function([], output)
mod['func_12151'] = func_12151
mod = relay.transform.InferType()(mod)
output = func_12151()
func_12152 = relay.Function([], output)
mutated_mod['func_12152'] = func_12152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8292_call = mod.get_global_var('func_8292')
func_8293_call = mutated_mod.get_global_var('func_8293')
call_12181 = func_8292_call()
call_12182 = func_8292_call()
func_10338_call = mod.get_global_var('func_10338')
func_10339_call = mutated_mod.get_global_var('func_10339')
call_12211 = relay.TupleGetItem(func_10338_call(), 0)
call_12212 = relay.TupleGetItem(func_10339_call(), 0)
func_2525_call = mod.get_global_var('func_2525')
func_2528_call = mutated_mod.get_global_var('func_2528')
const_12217 = relay.const([-9.552401,-0.159577,-9.662160,6.985244,1.203477,5.513282,0.034589,-2.933910,8.312754,-4.897152,-3.102789,5.898615,-3.117595,8.721276,5.650904,-8.696183,1.682660,7.898312,-6.858191,-4.137251,7.839066,-6.750965,7.961415,8.910674,-1.759086,-0.189126,-0.661807,0.392256,6.882912,-1.303032,-8.503386,-6.550341,4.414389,1.117727,-6.794493,8.567218,2.914668,-3.862154,7.619116,9.087880,-5.980890,-5.135135,9.122112,5.376766,-3.690794,-6.674226,-7.515303,-5.941140,-6.475686,3.831773,1.574302,-7.118560,-4.948921,-4.589682,-7.023729,-7.347879,5.828126,8.546683,-2.846064,1.905382,-6.980049,1.018737,-9.825376,6.882716,1.293252,7.900616,7.564236,0.747486,-6.407354,6.970352,-6.629887,1.321585,-8.276739,-8.817511,7.622451,6.742203,9.585484,3.654798,8.549338,-8.706086,1.591642,2.705610,-3.966180,6.197623,-5.276179,0.052387,-4.081633,-0.430410,-0.378210,5.458624,-3.772922,5.642267,-3.089796,4.936548,9.752686,-2.230847,0.374222,-4.989637,4.444564,0.034658,-8.414691,-6.897907,5.463239,-8.500226,1.325890,-2.700599,-6.199565,-1.233719,-1.253708,-4.820623,8.534286,-4.674406,8.393875,-8.732336,-3.014298,-7.494812,4.400207,7.545584,-5.149440,-5.365421,-1.762394,8.327163,-2.135153,9.830885,-7.151942,2.794832,-3.104855,-3.717004,-0.132853,-6.956060,-6.708404,7.553798,7.307494,9.926780,-8.597396,-5.689620,-9.563148,-7.057322,7.222492,3.292421,1.461522,4.490276,-4.185838,5.902439,2.609171,-2.996305,8.561829,8.013746,-0.225375,-2.553734,-7.798377,7.888711,-5.875393,6.967431,9.457232,7.199027,1.148736,6.696787,7.990550,-0.664387,-9.914072,-7.517449,7.600653,0.008504,-7.866975,-3.557308,-8.509413,5.062367,3.860937,-2.057118,7.390383,-0.024543,-0.535733,5.507504,-9.683265,-5.933645,-9.437264,-3.024992,-6.523559,9.712994,8.613385,5.979979,-7.335892,8.532821,-5.205410,-5.478507,5.721132,-5.809254,-7.697678,4.947634,-1.642459,-4.669406,5.301357,-2.769417,-7.086579,-7.553308,8.943910,4.139047,3.563127,-9.891010,-7.488497,0.554776,1.006050,6.945272,0.587136,-8.503075,7.848077,-0.806803,-6.479131,-7.267160,1.176075,-7.276583,0.882128,-9.380834,-2.356035,-1.162110,7.827540,4.206980,4.435935,3.198949,0.683677,-9.596621,-8.429592,6.053654,8.221799,3.763787,4.963984,-0.912291,7.963641,0.228852,0.621587,-3.748709,9.876399,0.038727,-1.316426,-3.448749,-0.995381,-2.134656,0.870074,5.300823,-6.337492,2.447554,6.104282,-3.699570,-5.823281], dtype = "float32")#candidate|12217|(245,)|const|float32
call_12216 = relay.TupleGetItem(func_2525_call(relay.reshape(const_12217.astype('float32'), [5, 7, 7])), 0)
call_12218 = relay.TupleGetItem(func_2528_call(relay.reshape(const_12217.astype('float32'), [5, 7, 7])), 0)
output = relay.Tuple([call_12181,call_12211,call_12216,const_12217,])
output2 = relay.Tuple([call_12182,call_12212,call_12218,const_12217,])
func_12235 = relay.Function([], output)
mod['func_12235'] = func_12235
mod = relay.transform.InferType()(mod)
mutated_mod['func_12235'] = func_12235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12235_call = mutated_mod.get_global_var('func_12235')
call_12236 = func_12235_call()
output = call_12236
func_12237 = relay.Function([], output)
mutated_mod['func_12237'] = func_12237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10612_call = mod.get_global_var('func_10612')
func_10614_call = mutated_mod.get_global_var('func_10614')
call_12240 = relay.TupleGetItem(func_10612_call(), 0)
call_12241 = relay.TupleGetItem(func_10614_call(), 0)
output = call_12240
output2 = call_12241
func_12242 = relay.Function([], output)
mod['func_12242'] = func_12242
mod = relay.transform.InferType()(mod)
output = func_12242()
func_12243 = relay.Function([], output)
mutated_mod['func_12243'] = func_12243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10788_call = mod.get_global_var('func_10788')
func_10790_call = mutated_mod.get_global_var('func_10790')
call_12252 = relay.TupleGetItem(func_10788_call(), 0)
call_12253 = relay.TupleGetItem(func_10790_call(), 0)
output = call_12252
output2 = call_12253
func_12265 = relay.Function([], output)
mod['func_12265'] = func_12265
mod = relay.transform.InferType()(mod)
output = func_12265()
func_12266 = relay.Function([], output)
mutated_mod['func_12266'] = func_12266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8065_call = mod.get_global_var('func_8065')
func_8067_call = mutated_mod.get_global_var('func_8067')
call_12276 = relay.TupleGetItem(func_8065_call(), 0)
call_12277 = relay.TupleGetItem(func_8067_call(), 0)
output = relay.Tuple([call_12276,])
output2 = relay.Tuple([call_12277,])
func_12294 = relay.Function([], output)
mod['func_12294'] = func_12294
mod = relay.transform.InferType()(mod)
output = func_12294()
func_12295 = relay.Function([], output)
mutated_mod['func_12295'] = func_12295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12327 = relay.var("var_12327", dtype = "bool", shape = ())#candidate|12327|()|var|bool
var_12328 = relay.var("var_12328", dtype = "bool", shape = (6, 10, 9))#candidate|12328|(6, 10, 9)|var|bool
bop_12329 = relay.logical_or(var_12327.astype('bool'), var_12328.astype('bool')) # shape=(6, 10, 9)
func_9773_call = mod.get_global_var('func_9773')
func_9775_call = mutated_mod.get_global_var('func_9775')
call_12343 = func_9773_call()
call_12344 = func_9773_call()
func_7816_call = mod.get_global_var('func_7816')
func_7818_call = mutated_mod.get_global_var('func_7818')
const_12356 = relay.const([False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False], dtype = "bool")#candidate|12356|(208,)|const|bool
call_12355 = relay.TupleGetItem(func_7816_call(relay.reshape(const_12356.astype('bool'), [52, 4])), 1)
call_12357 = relay.TupleGetItem(func_7818_call(relay.reshape(const_12356.astype('bool'), [52, 4])), 1)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_12366 = func_7228_call()
call_12367 = func_7228_call()
func_12095_call = mod.get_global_var('func_12095')
func_12097_call = mutated_mod.get_global_var('func_12097')
call_12390 = relay.TupleGetItem(func_12095_call(), 0)
call_12391 = relay.TupleGetItem(func_12097_call(), 0)
output = relay.Tuple([bop_12329,call_12343,call_12355,const_12356,call_12366,call_12390,])
output2 = relay.Tuple([bop_12329,call_12344,call_12357,const_12356,call_12367,call_12391,])
func_12394 = relay.Function([var_12327,var_12328,], output)
mod['func_12394'] = func_12394
mod = relay.transform.InferType()(mod)
var_12395 = relay.var("var_12395", dtype = "bool", shape = ())#candidate|12395|()|var|bool
var_12396 = relay.var("var_12396", dtype = "bool", shape = (6, 10, 9))#candidate|12396|(6, 10, 9)|var|bool
output = func_12394(var_12395,var_12396,)
func_12397 = relay.Function([var_12395,var_12396,], output)
mutated_mod['func_12397'] = func_12397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11259_call = mod.get_global_var('func_11259')
func_11261_call = mutated_mod.get_global_var('func_11261')
call_12469 = relay.TupleGetItem(func_11259_call(), 0)
call_12470 = relay.TupleGetItem(func_11261_call(), 0)
output = relay.Tuple([call_12469,])
output2 = relay.Tuple([call_12470,])
func_12479 = relay.Function([], output)
mod['func_12479'] = func_12479
mod = relay.transform.InferType()(mod)
mutated_mod['func_12479'] = func_12479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12479_call = mutated_mod.get_global_var('func_12479')
call_12480 = func_12479_call()
output = call_12480
func_12481 = relay.Function([], output)
mutated_mod['func_12481'] = func_12481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12235_call = mod.get_global_var('func_12235')
func_12237_call = mutated_mod.get_global_var('func_12237')
call_12517 = relay.TupleGetItem(func_12235_call(), 1)
call_12518 = relay.TupleGetItem(func_12237_call(), 1)
output = relay.Tuple([call_12517,])
output2 = relay.Tuple([call_12518,])
func_12520 = relay.Function([], output)
mod['func_12520'] = func_12520
mod = relay.transform.InferType()(mod)
mutated_mod['func_12520'] = func_12520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12520_call = mutated_mod.get_global_var('func_12520')
call_12521 = func_12520_call()
output = call_12521
func_12522 = relay.Function([], output)
mutated_mod['func_12522'] = func_12522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11381_call = mod.get_global_var('func_11381')
func_11383_call = mutated_mod.get_global_var('func_11383')
call_12548 = func_11381_call()
call_12549 = func_11381_call()
func_11807_call = mod.get_global_var('func_11807')
func_11808_call = mutated_mod.get_global_var('func_11808')
call_12578 = relay.TupleGetItem(func_11807_call(), 0)
call_12579 = relay.TupleGetItem(func_11808_call(), 0)
output = relay.Tuple([call_12548,call_12578,])
output2 = relay.Tuple([call_12549,call_12579,])
func_12591 = relay.Function([], output)
mod['func_12591'] = func_12591
mod = relay.transform.InferType()(mod)
mutated_mod['func_12591'] = func_12591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12591_call = mutated_mod.get_global_var('func_12591')
call_12592 = func_12591_call()
output = call_12592
func_12593 = relay.Function([], output)
mutated_mod['func_12593'] = func_12593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_12618 = relay.TupleGetItem(func_7172_call(), 2)
call_12619 = relay.TupleGetItem(func_7173_call(), 2)
output = call_12618
output2 = call_12619
func_12631 = relay.Function([], output)
mod['func_12631'] = func_12631
mod = relay.transform.InferType()(mod)
mutated_mod['func_12631'] = func_12631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12631_call = mutated_mod.get_global_var('func_12631')
call_12632 = func_12631_call()
output = call_12632
func_12633 = relay.Function([], output)
mutated_mod['func_12633'] = func_12633
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12654 = relay.var("var_12654", dtype = "float64", shape = (14, 16, 2))#candidate|12654|(14, 16, 2)|var|float64
uop_12655 = relay.acos(var_12654.astype('float64')) # shape=(14, 16, 2)
func_5331_call = mod.get_global_var('func_5331')
func_5337_call = mutated_mod.get_global_var('func_5337')
var_12664 = relay.var("var_12664", dtype = "float64", shape = (216,))#candidate|12664|(216,)|var|float64
const_12665 = relay.const([-5.973637,-1.674422,1.539936,-4.538915,-1.634902,6.304703,4.307932,7.696230,-5.989176,2.044238,4.126754,9.977971,0.941000,7.586293,5.952885,-7.638507,2.690486,-2.777971,7.935845,-2.433337,7.172656,8.372053,-2.332951,5.137841,7.910099,-3.430777,-7.772606,2.515564,-8.934597,-6.869370,7.746983,-7.006314,8.673262,-8.494260,6.699514,0.965933], dtype = "float32")#candidate|12665|(36,)|const|float32
var_12666 = relay.var("var_12666", dtype = "bool", shape = (4, 52))#candidate|12666|(4, 52)|var|bool
const_12667 = relay.const(8, dtype = "uint8")#candidate|12667|()|const|uint8
call_12663 = relay.TupleGetItem(func_5331_call(relay.reshape(var_12664.astype('float64'), [9, 3, 8]), relay.reshape(const_12665.astype('float32'), [36,]), relay.reshape(var_12666.astype('bool'), [208,]), relay.reshape(const_12667.astype('uint8'), []), ), 2)
call_12668 = relay.TupleGetItem(func_5337_call(relay.reshape(var_12664.astype('float64'), [9, 3, 8]), relay.reshape(const_12665.astype('float32'), [36,]), relay.reshape(var_12666.astype('bool'), [208,]), relay.reshape(const_12667.astype('uint8'), []), ), 2)
output = relay.Tuple([uop_12655,call_12663,var_12664,const_12665,var_12666,const_12667,])
output2 = relay.Tuple([uop_12655,call_12668,var_12664,const_12665,var_12666,const_12667,])
func_12669 = relay.Function([var_12654,var_12664,var_12666,], output)
mod['func_12669'] = func_12669
mod = relay.transform.InferType()(mod)
mutated_mod['func_12669'] = func_12669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12669_call = mutated_mod.get_global_var('func_12669')
var_12671 = relay.var("var_12671", dtype = "float64", shape = (14, 16, 2))#candidate|12671|(14, 16, 2)|var|float64
var_12672 = relay.var("var_12672", dtype = "float64", shape = (216,))#candidate|12672|(216,)|var|float64
var_12673 = relay.var("var_12673", dtype = "bool", shape = (4, 52))#candidate|12673|(4, 52)|var|bool
call_12670 = func_12669_call(var_12671,var_12672,var_12673,)
output = call_12670
func_12674 = relay.Function([var_12671,var_12672,var_12673,], output)
mutated_mod['func_12674'] = func_12674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11614_call = mod.get_global_var('func_11614')
func_11615_call = mutated_mod.get_global_var('func_11615')
call_12822 = relay.TupleGetItem(func_11614_call(), 0)
call_12823 = relay.TupleGetItem(func_11615_call(), 0)
func_9677_call = mod.get_global_var('func_9677')
func_9679_call = mutated_mod.get_global_var('func_9679')
call_12839 = func_9677_call()
call_12840 = func_9677_call()
func_11336_call = mod.get_global_var('func_11336')
func_11337_call = mutated_mod.get_global_var('func_11337')
call_12873 = func_11336_call()
call_12874 = func_11336_call()
func_10239_call = mod.get_global_var('func_10239')
func_10240_call = mutated_mod.get_global_var('func_10240')
call_12887 = func_10239_call()
call_12888 = func_10239_call()
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_12907 = relay.TupleGetItem(func_7413_call(), 0)
call_12908 = relay.TupleGetItem(func_7415_call(), 0)
output = relay.Tuple([call_12822,call_12839,call_12873,call_12887,call_12907,])
output2 = relay.Tuple([call_12823,call_12840,call_12874,call_12888,call_12908,])
func_12910 = relay.Function([], output)
mod['func_12910'] = func_12910
mod = relay.transform.InferType()(mod)
mutated_mod['func_12910'] = func_12910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12910_call = mutated_mod.get_global_var('func_12910')
call_12911 = func_12910_call()
output = call_12911
func_12912 = relay.Function([], output)
mutated_mod['func_12912'] = func_12912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9961_call = mod.get_global_var('func_9961')
func_9962_call = mutated_mod.get_global_var('func_9962')
call_12921 = relay.TupleGetItem(func_9961_call(), 0)
call_12922 = relay.TupleGetItem(func_9962_call(), 0)
func_9541_call = mod.get_global_var('func_9541')
func_9544_call = mutated_mod.get_global_var('func_9544')
var_12999 = relay.var("var_12999", dtype = "uint8", shape = (6, 12))#candidate|12999|(6, 12)|var|uint8
call_12998 = relay.TupleGetItem(func_9541_call(relay.reshape(var_12999.astype('uint8'), [72,])), 2)
call_13000 = relay.TupleGetItem(func_9544_call(relay.reshape(var_12999.astype('uint8'), [72,])), 2)
func_8904_call = mod.get_global_var('func_8904')
func_8906_call = mutated_mod.get_global_var('func_8906')
call_13049 = relay.TupleGetItem(func_8904_call(), 1)
call_13050 = relay.TupleGetItem(func_8906_call(), 1)
func_10788_call = mod.get_global_var('func_10788')
func_10790_call = mutated_mod.get_global_var('func_10790')
call_13053 = relay.TupleGetItem(func_10788_call(), 0)
call_13054 = relay.TupleGetItem(func_10790_call(), 0)
output = relay.Tuple([call_12921,call_12998,var_12999,call_13049,call_13053,])
output2 = relay.Tuple([call_12922,call_13000,var_12999,call_13050,call_13054,])
func_13059 = relay.Function([var_12999,], output)
mod['func_13059'] = func_13059
mod = relay.transform.InferType()(mod)
var_13060 = relay.var("var_13060", dtype = "uint8", shape = (6, 12))#candidate|13060|(6, 12)|var|uint8
output = func_13059(var_13060)
func_13061 = relay.Function([var_13060], output)
mutated_mod['func_13061'] = func_13061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11569_call = mod.get_global_var('func_11569')
func_11570_call = mutated_mod.get_global_var('func_11570')
call_13116 = relay.TupleGetItem(func_11569_call(), 1)
call_13117 = relay.TupleGetItem(func_11570_call(), 1)
func_5100_call = mod.get_global_var('func_5100')
func_5104_call = mutated_mod.get_global_var('func_5104')
var_13123 = relay.var("var_13123", dtype = "float32", shape = (5, 30))#candidate|13123|(5, 30)|var|float32
var_13124 = relay.var("var_13124", dtype = "uint8", shape = (1, 72))#candidate|13124|(1, 72)|var|uint8
var_13125 = relay.var("var_13125", dtype = "float32", shape = (245,))#candidate|13125|(245,)|var|float32
call_13122 = relay.TupleGetItem(func_5100_call(relay.reshape(var_13123.astype('float32'), [1, 150]), relay.reshape(var_13124.astype('uint8'), [18, 4]), relay.reshape(var_13125.astype('float32'), [245,]), ), 1)
call_13126 = relay.TupleGetItem(func_5104_call(relay.reshape(var_13123.astype('float32'), [1, 150]), relay.reshape(var_13124.astype('uint8'), [18, 4]), relay.reshape(var_13125.astype('float32'), [245,]), ), 1)
func_12394_call = mod.get_global_var('func_12394')
func_12397_call = mutated_mod.get_global_var('func_12397')
const_13131 = relay.const(False, dtype = "bool")#candidate|13131|()|const|bool
const_13132 = relay.const([[False,True,True,True,False,False,False,False,True,True],[True,True,True,True,True,False,False,True,True,False],[True,True,True,False,False,False,True,True,True,False],[False,True,True,True,False,False,True,False,False,True],[True,False,False,True,True,True,True,True,False,True],[True,True,False,True,False,False,True,True,True,False],[True,False,True,True,True,True,True,True,True,True],[False,True,True,False,False,False,True,True,True,True],[False,True,False,False,False,False,True,True,True,False],[False,True,False,True,False,False,True,True,True,False],[False,True,True,False,True,True,False,False,True,False],[True,True,True,True,False,True,False,True,False,True],[True,False,False,False,False,False,False,True,True,True],[True,False,False,True,False,True,False,False,True,True],[False,False,True,True,True,True,False,True,False,True],[True,True,True,True,True,True,False,True,False,True],[False,False,True,False,True,True,True,True,False,False],[True,False,False,False,False,False,True,False,True,True],[True,False,False,True,False,False,False,False,True,True],[True,False,True,True,False,False,False,False,True,False],[False,False,True,True,False,True,True,True,True,False],[False,True,True,True,False,True,True,False,True,False],[True,False,False,False,True,True,False,False,True,False],[False,True,False,True,False,True,False,True,False,False],[False,True,True,True,False,True,False,True,True,True],[True,True,True,False,True,True,True,False,True,False],[False,True,True,False,True,False,True,True,True,False],[True,True,True,False,False,True,True,False,False,True],[True,True,False,True,True,True,False,False,True,True],[False,True,False,False,False,True,False,True,True,True],[True,False,True,False,True,True,True,False,False,True],[True,True,True,True,False,False,True,False,True,False],[True,True,False,False,True,False,True,True,True,False],[True,True,True,False,True,False,True,True,False,True],[False,False,True,True,True,True,False,False,False,True],[True,True,False,True,True,False,True,True,True,False],[True,False,True,False,False,True,False,False,False,True],[True,False,True,False,False,False,False,False,True,False],[True,False,True,True,True,True,True,False,False,True],[False,True,True,False,False,False,True,False,False,True],[True,True,True,False,False,True,True,False,True,False],[False,False,False,True,False,True,False,True,True,False],[False,True,False,False,True,False,False,False,False,False],[True,False,True,True,False,True,False,True,True,False],[True,True,False,True,True,False,False,True,False,True],[False,False,True,False,False,False,False,False,True,False],[False,False,False,False,True,True,True,False,False,True],[False,False,False,False,True,True,True,False,True,True],[True,True,True,False,True,False,True,True,False,False],[True,True,False,False,True,False,True,False,False,True],[True,False,True,False,False,True,True,True,True,False],[False,False,True,False,True,False,False,False,True,False],[False,True,True,False,True,False,False,False,True,False],[True,False,False,True,False,True,False,False,False,True]], dtype = "bool")#candidate|13132|(54, 10)|const|bool
call_13130 = relay.TupleGetItem(func_12394_call(relay.reshape(const_13131.astype('bool'), []), relay.reshape(const_13132.astype('bool'), [6, 10, 9]), ), 3)
call_13133 = relay.TupleGetItem(func_12397_call(relay.reshape(const_13131.astype('bool'), []), relay.reshape(const_13132.astype('bool'), [6, 10, 9]), ), 3)
output = relay.Tuple([call_13116,call_13122,var_13123,var_13124,var_13125,call_13130,const_13131,const_13132,])
output2 = relay.Tuple([call_13117,call_13126,var_13123,var_13124,var_13125,call_13133,const_13131,const_13132,])
func_13138 = relay.Function([var_13123,var_13124,var_13125,], output)
mod['func_13138'] = func_13138
mod = relay.transform.InferType()(mod)
var_13139 = relay.var("var_13139", dtype = "float32", shape = (5, 30))#candidate|13139|(5, 30)|var|float32
var_13140 = relay.var("var_13140", dtype = "uint8", shape = (1, 72))#candidate|13140|(1, 72)|var|uint8
var_13141 = relay.var("var_13141", dtype = "float32", shape = (245,))#candidate|13141|(245,)|var|float32
output = func_13138(var_13139,var_13140,var_13141,)
func_13142 = relay.Function([var_13139,var_13140,var_13141,], output)
mutated_mod['func_13142'] = func_13142
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13160 = relay.var("var_13160", dtype = "uint64", shape = (8, 3, 12))#candidate|13160|(8, 3, 12)|var|uint64
var_13161 = relay.var("var_13161", dtype = "uint64", shape = (8, 3, 12))#candidate|13161|(8, 3, 12)|var|uint64
bop_13162 = relay.add(var_13160.astype('uint64'), relay.reshape(var_13161.astype('uint64'), relay.shape_of(var_13160))) # shape=(8, 3, 12)
func_10082_call = mod.get_global_var('func_10082')
func_10084_call = mutated_mod.get_global_var('func_10084')
call_13176 = func_10082_call()
call_13177 = func_10082_call()
func_11367_call = mod.get_global_var('func_11367')
func_11368_call = mutated_mod.get_global_var('func_11368')
call_13179 = relay.TupleGetItem(func_11367_call(), 0)
call_13180 = relay.TupleGetItem(func_11368_call(), 0)
func_10462_call = mod.get_global_var('func_10462')
func_10464_call = mutated_mod.get_global_var('func_10464')
call_13181 = func_10462_call()
call_13182 = func_10462_call()
uop_13185 = relay.sigmoid(bop_13162.astype('float32')) # shape=(8, 3, 12)
output = relay.Tuple([call_13176,call_13179,call_13181,uop_13185,])
output2 = relay.Tuple([call_13177,call_13180,call_13182,uop_13185,])
func_13188 = relay.Function([var_13160,var_13161,], output)
mod['func_13188'] = func_13188
mod = relay.transform.InferType()(mod)
var_13189 = relay.var("var_13189", dtype = "uint64", shape = (8, 3, 12))#candidate|13189|(8, 3, 12)|var|uint64
var_13190 = relay.var("var_13190", dtype = "uint64", shape = (8, 3, 12))#candidate|13190|(8, 3, 12)|var|uint64
output = func_13188(var_13189,var_13190,)
func_13191 = relay.Function([var_13189,var_13190,], output)
mutated_mod['func_13191'] = func_13191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10788_call = mod.get_global_var('func_10788')
func_10790_call = mutated_mod.get_global_var('func_10790')
call_13230 = relay.TupleGetItem(func_10788_call(), 0)
call_13231 = relay.TupleGetItem(func_10790_call(), 0)
func_10612_call = mod.get_global_var('func_10612')
func_10614_call = mutated_mod.get_global_var('func_10614')
call_13232 = relay.TupleGetItem(func_10612_call(), 0)
call_13233 = relay.TupleGetItem(func_10614_call(), 0)
func_11336_call = mod.get_global_var('func_11336')
func_11337_call = mutated_mod.get_global_var('func_11337')
call_13237 = func_11336_call()
call_13238 = func_11336_call()
output = relay.Tuple([call_13230,call_13232,call_13237,])
output2 = relay.Tuple([call_13231,call_13233,call_13238,])
func_13277 = relay.Function([], output)
mod['func_13277'] = func_13277
mod = relay.transform.InferType()(mod)
mutated_mod['func_13277'] = func_13277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13277_call = mutated_mod.get_global_var('func_13277')
call_13278 = func_13277_call()
output = call_13278
func_13279 = relay.Function([], output)
mutated_mod['func_13279'] = func_13279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11287_call = mod.get_global_var('func_11287')
func_11289_call = mutated_mod.get_global_var('func_11289')
call_13298 = func_11287_call()
call_13299 = func_11287_call()
output = relay.Tuple([call_13298,])
output2 = relay.Tuple([call_13299,])
func_13303 = relay.Function([], output)
mod['func_13303'] = func_13303
mod = relay.transform.InferType()(mod)
output = func_13303()
func_13304 = relay.Function([], output)
mutated_mod['func_13304'] = func_13304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8947_call = mod.get_global_var('func_8947')
func_8949_call = mutated_mod.get_global_var('func_8949')
call_13417 = relay.TupleGetItem(func_8947_call(), 0)
call_13418 = relay.TupleGetItem(func_8949_call(), 0)
func_12235_call = mod.get_global_var('func_12235')
func_12237_call = mutated_mod.get_global_var('func_12237')
call_13434 = relay.TupleGetItem(func_12235_call(), 1)
call_13435 = relay.TupleGetItem(func_12237_call(), 1)
func_9541_call = mod.get_global_var('func_9541')
func_9544_call = mutated_mod.get_global_var('func_9544')
const_13437 = relay.const([-6,-4,10,-4,-6,7,-7,3,-9,1,-5,-5,-6,-8,-10,10,2,7,-7,-6,6,-2,-4,-4,-3,6,-9,5,-1,-4,3,-1,7,8,-10,6,8,1,-2,6,2,-3,6,-8,-2,10,-4,2,-8,5,7,-4,-1,8,1,-1,9,-4,2,1,-4,-1,9,-10,-6,-5,-10,7,-5,7,10,-9], dtype = "uint8")#candidate|13437|(72,)|const|uint8
call_13436 = relay.TupleGetItem(func_9541_call(relay.reshape(const_13437.astype('uint8'), [72,])), 1)
call_13438 = relay.TupleGetItem(func_9544_call(relay.reshape(const_13437.astype('uint8'), [72,])), 1)
func_8931_call = mod.get_global_var('func_8931')
func_8936_call = mutated_mod.get_global_var('func_8936')
const_13441 = relay.const(0.272943, dtype = "float32")#candidate|13441|()|const|float32
const_13442 = relay.const([-8.419211,9.353645,-2.311497,4.262697,6.791249,7.454429,7.794831,-1.742661,7.194485,1.277760,-8.699375,-4.258811,1.746492,-6.433334,1.439594,2.971769,-2.275822,-7.727318,6.984700,9.839338,-6.221704,6.747156,4.666061,1.301094,0.077919,-0.158858,1.460985,3.350024,-8.141131,5.829344,-0.683615,3.195355,6.124415,2.881253,2.313199,8.901765,-1.063061,1.018264,-0.123482,-5.446043,3.820514,9.889947,-2.794788,1.597528,3.550159,-8.159544,0.455122,-3.619550,-5.269327,-9.724195,3.061926,7.470628,-5.495192,1.121301,0.680821,-9.623623,-8.088470,2.743210,-2.057146,1.995259,-5.097713,8.868425,8.084269,-7.619582,-1.568660,8.650167,9.589304,9.291237,-5.522115,-5.101743,-6.807221,-2.496278,9.199138,3.104929,6.245132,8.370789,9.188849,1.992932,-2.932108,-3.085396,-3.261876,-3.486615,-3.385854,7.694192,-0.268862,9.360901,-0.984799,4.371634,7.471513,-9.211576,9.988003,-1.699712,-2.949736,8.106407,-0.985928,1.728984,-3.229897,-7.745374,1.779792,8.629316,2.846516,3.912762,-8.378518,2.454786,0.884007,-4.640296,4.494369,6.289488,3.006928,2.191874,-7.996245,-9.839687,-5.017571,-6.510086,1.054596,-3.072085,-3.900303,-2.279552,-1.516580,-0.057162,5.998160,7.757105,-2.431262,5.422404,4.584762,0.485223,5.096937,-5.790305,-9.868839,-5.796511,-6.327827,-7.825273,-4.315926,-6.703114,4.706050,-5.010404,2.906601,0.582153,0.468574,8.905487,2.369331,-9.294400,1.852840,8.037136,0.481074,9.175500,-9.072878,-6.398717,-9.400285,0.216045,-5.267147,7.808626,8.184651,5.554042,4.054595,-6.155338,3.839379,1.447237,2.938811,-3.064638,-1.669873,7.305810,8.232806,1.272603,-0.146519,7.375404,5.374159,-6.379211,-9.240888,6.862587,3.578153,-8.343782,-9.383360,0.397150,-2.592311,4.675392,4.805302,6.369751,-2.844364,-9.827711,-7.254222,9.829432,-7.485143,-3.950453,9.414812,-8.944055,2.255094,4.111684,4.853419,-4.611136,-1.655980,-4.079808,-7.531398,8.467642,8.183031,6.672452,6.701031,9.044433,-0.513140,-1.292431,5.256481,-7.099944,-5.759639,-5.700563,-2.356340,6.325371,-5.095100,-9.723593,-1.694854,-0.673184,-7.863384,1.159539,-4.415925,2.654294,-1.544045,3.129280,3.128406,9.446328,8.161750,4.404953,-1.410582,2.690140,-2.917776,3.597184,1.998392,-1.176426,0.784131,1.344594,-7.113623,-1.498341,7.534471,-3.463155,-9.872034,-9.380586,-6.082742,9.008457,-5.733759,1.276891,0.902371,1.274326], dtype = "float32")#candidate|13442|(240,)|const|float32
var_13443 = relay.var("var_13443", dtype = "bool", shape = (208,))#candidate|13443|(208,)|var|bool
call_13440 = relay.TupleGetItem(func_8931_call(relay.reshape(const_13441.astype('float32'), []), relay.reshape(const_13442.astype('float32'), [240,]), relay.reshape(var_13443.astype('bool'), [1, 208]), ), 2)
call_13444 = relay.TupleGetItem(func_8936_call(relay.reshape(const_13441.astype('float32'), []), relay.reshape(const_13442.astype('float32'), [240,]), relay.reshape(var_13443.astype('bool'), [1, 208]), ), 2)
func_10400_call = mod.get_global_var('func_10400')
func_10403_call = mutated_mod.get_global_var('func_10403')
var_13454 = relay.var("var_13454", dtype = "float32", shape = (550, 3))#candidate|13454|(550, 3)|var|float32
call_13453 = relay.TupleGetItem(func_10400_call(relay.reshape(var_13454.astype('float32'), [11, 150])), 1)
call_13455 = relay.TupleGetItem(func_10403_call(relay.reshape(var_13454.astype('float32'), [11, 150])), 1)
output = relay.Tuple([call_13417,call_13434,call_13436,const_13437,call_13440,const_13441,const_13442,var_13443,call_13453,var_13454,])
output2 = relay.Tuple([call_13418,call_13435,call_13438,const_13437,call_13444,const_13441,const_13442,var_13443,call_13455,var_13454,])
func_13458 = relay.Function([var_13443,var_13454,], output)
mod['func_13458'] = func_13458
mod = relay.transform.InferType()(mod)
var_13459 = relay.var("var_13459", dtype = "bool", shape = (208,))#candidate|13459|(208,)|var|bool
var_13460 = relay.var("var_13460", dtype = "float32", shape = (550, 3))#candidate|13460|(550, 3)|var|float32
output = func_13458(var_13459,var_13460,)
func_13461 = relay.Function([var_13459,var_13460,], output)
mutated_mod['func_13461'] = func_13461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9651_call = mod.get_global_var('func_9651')
func_9653_call = mutated_mod.get_global_var('func_9653')
call_13499 = func_9651_call()
call_13500 = func_9651_call()
func_10191_call = mod.get_global_var('func_10191')
func_10193_call = mutated_mod.get_global_var('func_10193')
call_13506 = relay.TupleGetItem(func_10191_call(), 0)
call_13507 = relay.TupleGetItem(func_10193_call(), 0)
func_11614_call = mod.get_global_var('func_11614')
func_11615_call = mutated_mod.get_global_var('func_11615')
call_13512 = relay.TupleGetItem(func_11614_call(), 0)
call_13513 = relay.TupleGetItem(func_11615_call(), 0)
output = relay.Tuple([call_13499,call_13506,call_13512,])
output2 = relay.Tuple([call_13500,call_13507,call_13513,])
func_13518 = relay.Function([], output)
mod['func_13518'] = func_13518
mod = relay.transform.InferType()(mod)
mutated_mod['func_13518'] = func_13518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13518_call = mutated_mod.get_global_var('func_13518')
call_13519 = func_13518_call()
output = call_13519
func_13520 = relay.Function([], output)
mutated_mod['func_13520'] = func_13520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10961_call = mod.get_global_var('func_10961')
func_10963_call = mutated_mod.get_global_var('func_10963')
call_13524 = func_10961_call()
call_13525 = func_10961_call()
output = call_13524
output2 = call_13525
func_13531 = relay.Function([], output)
mod['func_13531'] = func_13531
mod = relay.transform.InferType()(mod)
mutated_mod['func_13531'] = func_13531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13531_call = mutated_mod.get_global_var('func_13531')
call_13532 = func_13531_call()
output = call_13532
func_13533 = relay.Function([], output)
mutated_mod['func_13533'] = func_13533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12095_call = mod.get_global_var('func_12095')
func_12097_call = mutated_mod.get_global_var('func_12097')
call_13536 = relay.TupleGetItem(func_12095_call(), 0)
call_13537 = relay.TupleGetItem(func_12097_call(), 0)
func_10057_call = mod.get_global_var('func_10057')
func_10062_call = mutated_mod.get_global_var('func_10062')
const_13542 = relay.const([1.576136,-8.588353,-7.045910,-2.279613,0.446279,-0.111040,-9.004719,9.789527,0.684461,2.375043,1.777188,4.275857,0.266466,-8.471005,-4.596942,6.411931,5.754456,0.304065,3.024081,-8.065057,-5.838802,-9.471917,-1.223355,-6.882117,-6.887872,-7.457372,-6.890376,6.670757,1.985252,-2.558018,6.392188,7.948678,9.018623,-6.433656,-1.975757,9.804133,-5.974486,-5.642236,6.087995,-4.585768,-3.352774,-5.023664,-8.111999,-3.960822,6.637371,-6.177555,-8.362608,0.945711,-0.021725,-6.152057,-4.593779,4.578388,9.832874,2.550424,-9.162210,-0.945316,-5.014697,8.208546,8.282944,-4.324511,-4.308614,6.446074,4.782109,-3.849469,0.177601,-8.491724,1.242380,-4.849569,4.105042,2.543974,9.358932,-8.704967,-8.013612,-1.855325,-1.204965,-1.320534,5.967943,8.024835,8.194738,-2.187068,4.066551,-6.193935,2.378944,2.955969,8.185789,-2.446770,5.231591,-2.241116,4.273313,7.154081,-4.009050,-8.122601,2.519733,-2.216146,-0.082812,7.056382,6.687500,-9.500245,-7.293218,-9.986103,-3.866188,-1.531320,5.487422,-7.488688,-0.305140,-3.863873,6.641081,-2.176110,3.167549,2.448305,-7.898048,2.756433,9.789090,-2.990489,6.994357,9.435802,9.726561,6.404533,-0.949348,5.456557,1.279232,5.789396,4.081817,-3.328432,-7.934166,-9.722440,-5.023047,9.161318,8.553976,-7.576025,-0.030787,-6.476444,4.507797,-3.301615,9.157513,-1.081870,-8.165818,-5.245975,-6.651125,-2.335802,-0.932954,0.404980,-9.580442,-0.532685,-0.398691,-7.258581,-7.323291,-6.908485,5.144998,-0.256827,6.591587,2.097007,-4.644453,9.032553,-7.635760,-0.427190,-1.552272,-7.445389,-9.662745,-7.277198,4.353662,3.968907,3.928476,1.483802,-5.407496,-9.528479,2.222281,2.888941,7.330490,-8.805907,-6.311401,-3.229500,-8.938512,8.254046,-2.442120,9.525101,5.246351,6.546700,-6.308140,4.664202,-6.116006,-5.359971,0.978078,-8.736731,-7.364370,2.314641,2.429464,6.405433,-4.221978,-7.260870,-2.353714,-2.875466,-0.672581,5.133080,-3.940171,1.417539,-8.966337,-8.821828,-2.823813,-0.173632,5.286843,5.358046,1.631755,-7.672700,-3.162992,-8.915600,-9.256415,-6.564497,4.923029,-1.002559,-9.884376,-5.101424,3.924109,-4.417097,4.272563,6.072023,-7.393836,2.739584,8.881008,5.620405,-2.630530,6.259246,-8.695272,6.280127,5.259851,-9.190979,-6.053533,-2.853032,2.673262,6.513531,9.922188,-6.209410,0.496801,8.571188,3.049929,-8.090600,7.796547,8.313136,8.193462,9.387449,-7.413884,-8.094628,-5.525131,-9.377805,-5.610146,8.385842,-2.013217,4.250292,7.295390,1.911800,-7.879453,0.676240,4.347967,4.705475,3.412076,5.174408,-0.859420,-6.180005,-4.942496,6.948558,-6.066731,-3.053047,-7.460751,4.250419,-0.128617,-6.144528,-2.923449,-3.055962,-1.106515,5.367678,-3.106551,2.283769,-9.241606,-7.743631,4.550464,0.050354,-4.073467,-8.652430,-6.899783,-6.246100,-4.767523,6.421471,-1.355630,-9.898620,2.815080,9.100721,-7.181041,9.982220,-1.184805,5.165437,0.074697,-5.230040,-4.301893,-1.207405,-9.070375,-2.818620,2.444425,5.685336,5.537340,6.738164,7.870449,3.632271,7.406283,8.073990,-9.332665,0.701826,5.108318,0.549866,9.788338,-0.871026,-7.985398,-3.773751,-5.430593,-3.175412,-5.971739,2.171113,-2.952732,3.503993,6.369298,1.237949,-5.786065,9.688738,-4.313493,2.835012,-8.916332,4.927322,-0.200642,-7.074294,-3.156852,7.089501,-2.569503,-0.009824,1.635722,7.996782,-5.630916,-4.471544,5.840934,1.122244,-8.273338,2.387975,-6.426855,3.590570,8.915727,-2.704161,-5.510569,-1.178654,-2.537924,4.038118,-8.909006,-3.345592,-8.127893,5.247500,-9.425308,5.238611,-0.142294,5.848092,-3.188673,2.047755,-1.938643,8.881650,7.166339,-8.016148,-0.142044,6.823313,-9.318759,-9.622776,-2.878080,-0.269013,-8.625325,5.545746,4.019326,1.988217,-9.994872,1.429953,-0.144954,7.623940,-8.958959,8.349799,-1.159183,8.739647,-0.725579,6.046656,-4.495807,0.933462,2.136160,5.096961,4.739974,-4.950454,7.619742,2.535623,-1.962506,-3.950404,-2.280326,-0.342876,-8.222369,0.636802,0.479438,-1.135202,-4.339782,-5.564779,-4.386689,-6.268496,-6.952571,0.601493,-2.127271,-5.633703,-7.566250,5.964711,-2.138724,5.499560,-4.993633,-5.934491,1.577625,7.829224,-4.646471,1.755342,9.530448,9.550258,3.338421,4.254559,5.869426,-7.391961,-3.644675,-9.753326,9.287227,-0.238823,-8.032652,3.173108,8.302166,9.069895,-5.421657,-3.554839,5.803746,-1.088220,0.965433,-4.650879,5.411332,-7.343452,5.386093,-1.255953,-8.300785,-2.238389,4.137537,-2.272936,-9.950387,0.342409,-1.245233,-3.583657,5.353250,-4.792739,-7.440760,5.256474,-3.477665,-7.986733,-5.971697,-5.081370,6.511097,5.069451,6.406003,4.059755,2.501433,-7.341965,-6.175538,3.380712,0.390182,-3.693214,5.345819,3.280612,9.466466,8.004627,1.246692,-5.552128,-2.573484,4.984179,2.848074,1.961218,2.041370,1.755063,-7.656739,5.494937,-0.979304,2.348153,4.238110,2.989300,-0.252309,-3.068547,4.968642,-9.884531,-5.538828,0.383388,-3.721254,6.582190,-3.302710,-8.603088,4.902775,9.332475,1.928213,7.523022,2.607636,-5.393282,5.181322,2.053595,6.647202,-3.921295,-7.837309,-9.063408,-8.912005,-9.909492,-3.369772,2.590983,6.538142,3.577803,-8.864982,6.838421,-4.621465,0.932759,7.791622,-1.924989,8.931281,-8.127642,-7.287100,-3.361135,-3.845000,8.215165,9.472600,0.413309,5.868973,-6.875970,5.870758,-9.651958,1.937709,-7.384614,-6.296649,4.644441,8.089685,2.534151,-6.875564,8.498205,2.292374,8.462489,6.079465,2.085735,-9.543420,-7.011903,6.656481,8.877677,7.993436,5.460539,-7.672498,1.795532,2.239712,8.413834,-8.256586,-6.829305,8.826942,1.281177,-2.030563,-5.670039,-3.916064,6.723428,8.516169,-7.319315,-5.825298,-4.587566,-4.812799,-0.606958,5.155335,-4.747549,-1.169044,9.355275,-9.584694,4.357645,9.708140,1.339380,-1.605422,5.493864,6.332808,-0.821556,-2.230595,-1.540969,-1.597933,-4.577893,-6.555304,-5.567723,0.853758,2.919002,-2.159203,4.348761,-1.812124,5.570308,0.843313,-6.412956,-7.695805,-9.259742,2.588504,8.174630,5.256336,4.383197,-4.779276,6.680753,6.095835,-6.463790,5.337928,5.870931,-5.447316,-9.208067,-8.772415,3.606592,-4.086712,0.034109,-5.074111,4.115030,-0.849801,-1.529051,-9.550926,-6.238552,-0.617155,0.483797,-7.910320,3.368884,1.607359,-9.340767,-5.314154,-0.297781,4.101563,-7.788766,8.601495,-2.266890,2.452665,-0.847257,-4.557588,2.266647,6.382666,-9.835594,-9.871329,8.122970,8.816527,8.011856,1.586059,-1.089627,8.912994,-3.541934,6.884789,-4.147182,4.435646,-3.168744,6.981247,-7.421854,3.512176,2.073578,-2.573971,8.360249,-6.769533,7.822695,9.963696,1.203755,5.749698,9.409005,-9.004897,2.149051,-0.634884,8.143395,5.520327,8.151924,-2.741003,-0.187487,8.144727,-8.871163,-2.122814,0.708157,-0.511655,-3.261742,-1.962276,-3.920737,7.909552,7.125207,6.668805,-0.168494,-6.128906,9.354337,-4.133550,-6.095902,-6.227783,8.576104,-6.630429,-8.770384,0.767517,-5.957987,-0.880584,-4.985035,-7.513322,5.662465,-2.626758,8.558623,5.499597,1.479040,-6.576790,2.302821,4.200677,-1.924752,4.371245,-6.765146,4.649059,7.324267,5.213077,-6.935708,8.988060,3.404206,0.921355,-8.365916,-8.557090,-5.190386,9.618056,3.859402,-6.678722,3.536311,-7.514642,3.009369,-0.802605,3.657782], dtype = "float32")#candidate|13542|(720,)|const|float32
var_13543 = relay.var("var_13543", dtype = "uint8", shape = ())#candidate|13543|()|var|uint8
var_13544 = relay.var("var_13544", dtype = "float32", shape = (245,))#candidate|13544|(245,)|var|float32
call_13541 = relay.TupleGetItem(func_10057_call(relay.reshape(const_13542.astype('float32'), [720,]), relay.reshape(var_13543.astype('uint8'), []), relay.reshape(var_13544.astype('float32'), [245,]), relay.reshape(var_13544.astype('float32'), [245,]), ), 3)
call_13545 = relay.TupleGetItem(func_10062_call(relay.reshape(const_13542.astype('float32'), [720,]), relay.reshape(var_13543.astype('uint8'), []), relay.reshape(var_13544.astype('float32'), [245,]), relay.reshape(var_13544.astype('float32'), [245,]), ), 3)
output = relay.Tuple([call_13536,call_13541,const_13542,var_13543,var_13544,])
output2 = relay.Tuple([call_13537,call_13545,const_13542,var_13543,var_13544,])
func_13549 = relay.Function([var_13543,var_13544,], output)
mod['func_13549'] = func_13549
mod = relay.transform.InferType()(mod)
mutated_mod['func_13549'] = func_13549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13549_call = mutated_mod.get_global_var('func_13549')
var_13551 = relay.var("var_13551", dtype = "uint8", shape = ())#candidate|13551|()|var|uint8
var_13552 = relay.var("var_13552", dtype = "float32", shape = (245,))#candidate|13552|(245,)|var|float32
call_13550 = func_13549_call(var_13551,var_13552,)
output = call_13550
func_13553 = relay.Function([var_13551,var_13552,], output)
mutated_mod['func_13553'] = func_13553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8849_call = mod.get_global_var('func_8849')
func_8850_call = mutated_mod.get_global_var('func_8850')
call_13579 = func_8849_call()
call_13580 = func_8849_call()
func_11336_call = mod.get_global_var('func_11336')
func_11337_call = mutated_mod.get_global_var('func_11337')
call_13592 = func_11336_call()
call_13593 = func_11336_call()
output = relay.Tuple([call_13579,call_13592,])
output2 = relay.Tuple([call_13580,call_13593,])
func_13621 = relay.Function([], output)
mod['func_13621'] = func_13621
mod = relay.transform.InferType()(mod)
output = func_13621()
func_13622 = relay.Function([], output)
mutated_mod['func_13622'] = func_13622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8711_call = mod.get_global_var('func_8711')
func_8713_call = mutated_mod.get_global_var('func_8713')
call_13623 = relay.TupleGetItem(func_8711_call(), 2)
call_13624 = relay.TupleGetItem(func_8713_call(), 2)
var_13633 = relay.var("var_13633", dtype = "float32", shape = (25, 6))#candidate|13633|(25, 6)|var|float32
bop_13634 = relay.greater(call_13623.astype('bool'), relay.reshape(var_13633.astype('bool'), relay.shape_of(call_13623))) # shape=(25, 6)
bop_13637 = relay.greater(call_13624.astype('bool'), relay.reshape(var_13633.astype('bool'), relay.shape_of(call_13624))) # shape=(25, 6)
output = relay.Tuple([bop_13634,])
output2 = relay.Tuple([bop_13637,])
func_13645 = relay.Function([var_13633,], output)
mod['func_13645'] = func_13645
mod = relay.transform.InferType()(mod)
mutated_mod['func_13645'] = func_13645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13646 = relay.var("var_13646", dtype = "float32", shape = (25, 6))#candidate|13646|(25, 6)|var|float32
func_13645_call = mutated_mod.get_global_var('func_13645')
call_13647 = func_13645_call(var_13646)
output = call_13647
func_13648 = relay.Function([var_13646], output)
mutated_mod['func_13648'] = func_13648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12151_call = mod.get_global_var('func_12151')
func_12152_call = mutated_mod.get_global_var('func_12152')
call_13766 = relay.TupleGetItem(func_12151_call(), 0)
call_13767 = relay.TupleGetItem(func_12152_call(), 0)
func_5331_call = mod.get_global_var('func_5331')
func_5337_call = mutated_mod.get_global_var('func_5337')
var_13784 = relay.var("var_13784", dtype = "float64", shape = (216,))#candidate|13784|(216,)|var|float64
const_13785 = relay.const([3.031914,-2.124462,0.464429,6.491718,6.648852,-7.000418,-4.285224,4.664545,-1.252995,-9.589108,1.219674,2.328192,6.682688,-7.377000,-1.484322,-2.724019,-8.157905,2.361695,0.285218,-9.957703,4.984647,0.253677,-1.883906,1.929842,3.898269,9.246167,2.342010,-1.186852,1.563036,2.956826,-1.688773,1.605845,2.978794,-2.166771,9.311279,0.495896], dtype = "float32")#candidate|13785|(36,)|const|float32
var_13786 = relay.var("var_13786", dtype = "bool", shape = (208,))#candidate|13786|(208,)|var|bool
const_13787 = relay.const(9, dtype = "uint8")#candidate|13787|()|const|uint8
call_13783 = relay.TupleGetItem(func_5331_call(relay.reshape(var_13784.astype('float64'), [9, 3, 8]), relay.reshape(const_13785.astype('float32'), [36,]), relay.reshape(var_13786.astype('bool'), [208,]), relay.reshape(const_13787.astype('uint8'), []), ), 4)
call_13788 = relay.TupleGetItem(func_5337_call(relay.reshape(var_13784.astype('float64'), [9, 3, 8]), relay.reshape(const_13785.astype('float32'), [36,]), relay.reshape(var_13786.astype('bool'), [208,]), relay.reshape(const_13787.astype('uint8'), []), ), 4)
func_13531_call = mod.get_global_var('func_13531')
func_13533_call = mutated_mod.get_global_var('func_13533')
call_13789 = func_13531_call()
call_13790 = func_13531_call()
func_10168_call = mod.get_global_var('func_10168')
func_10171_call = mutated_mod.get_global_var('func_10171')
call_13791 = func_10168_call(relay.reshape(const_13787.astype('float32'), []))
call_13792 = func_10168_call(relay.reshape(const_13787.astype('float32'), []))
output = relay.Tuple([call_13766,call_13783,var_13784,const_13785,var_13786,const_13787,call_13789,call_13791,])
output2 = relay.Tuple([call_13767,call_13788,var_13784,const_13785,var_13786,const_13787,call_13790,call_13792,])
func_13797 = relay.Function([var_13784,var_13786,], output)
mod['func_13797'] = func_13797
mod = relay.transform.InferType()(mod)
var_13798 = relay.var("var_13798", dtype = "float64", shape = (216,))#candidate|13798|(216,)|var|float64
var_13799 = relay.var("var_13799", dtype = "bool", shape = (208,))#candidate|13799|(208,)|var|bool
output = func_13797(var_13798,var_13799,)
func_13800 = relay.Function([var_13798,var_13799,], output)
mutated_mod['func_13800'] = func_13800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9184_call = mod.get_global_var('func_9184')
func_9185_call = mutated_mod.get_global_var('func_9185')
call_13966 = relay.TupleGetItem(func_9184_call(), 0)
call_13967 = relay.TupleGetItem(func_9185_call(), 0)
func_10168_call = mod.get_global_var('func_10168')
func_10171_call = mutated_mod.get_global_var('func_10171')
const_13978 = relay.const(7.751675, dtype = "float32")#candidate|13978|()|const|float32
call_13977 = func_10168_call(relay.reshape(const_13978.astype('float32'), []))
call_13979 = func_10168_call(relay.reshape(const_13978.astype('float32'), []))
output = relay.Tuple([call_13966,call_13977,const_13978,])
output2 = relay.Tuple([call_13967,call_13979,const_13978,])
func_13980 = relay.Function([], output)
mod['func_13980'] = func_13980
mod = relay.transform.InferType()(mod)
mutated_mod['func_13980'] = func_13980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13980_call = mutated_mod.get_global_var('func_13980')
call_13981 = func_13980_call()
output = call_13981
func_13982 = relay.Function([], output)
mutated_mod['func_13982'] = func_13982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12910_call = mod.get_global_var('func_12910')
func_12912_call = mutated_mod.get_global_var('func_12912')
call_14000 = relay.TupleGetItem(func_12910_call(), 4)
call_14001 = relay.TupleGetItem(func_12912_call(), 4)
func_12591_call = mod.get_global_var('func_12591')
func_12593_call = mutated_mod.get_global_var('func_12593')
call_14034 = relay.TupleGetItem(func_12591_call(), 1)
call_14035 = relay.TupleGetItem(func_12593_call(), 1)
func_12294_call = mod.get_global_var('func_12294')
func_12295_call = mutated_mod.get_global_var('func_12295')
call_14042 = relay.TupleGetItem(func_12294_call(), 0)
call_14043 = relay.TupleGetItem(func_12295_call(), 0)
func_11381_call = mod.get_global_var('func_11381')
func_11383_call = mutated_mod.get_global_var('func_11383')
call_14063 = func_11381_call()
call_14064 = func_11381_call()
func_13531_call = mod.get_global_var('func_13531')
func_13533_call = mutated_mod.get_global_var('func_13533')
call_14066 = func_13531_call()
call_14067 = func_13531_call()
output = relay.Tuple([call_14000,call_14034,call_14042,call_14063,call_14066,])
output2 = relay.Tuple([call_14001,call_14035,call_14043,call_14064,call_14067,])
func_14074 = relay.Function([], output)
mod['func_14074'] = func_14074
mod = relay.transform.InferType()(mod)
mutated_mod['func_14074'] = func_14074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14074_call = mutated_mod.get_global_var('func_14074')
call_14075 = func_14074_call()
output = call_14075
func_14076 = relay.Function([], output)
mutated_mod['func_14076'] = func_14076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9363_call = mod.get_global_var('func_9363')
func_9365_call = mutated_mod.get_global_var('func_9365')
call_14077 = relay.TupleGetItem(func_9363_call(), 0)
call_14078 = relay.TupleGetItem(func_9365_call(), 0)
func_10239_call = mod.get_global_var('func_10239')
func_10240_call = mutated_mod.get_global_var('func_10240')
call_14081 = func_10239_call()
call_14082 = func_10239_call()
func_12520_call = mod.get_global_var('func_12520')
func_12522_call = mutated_mod.get_global_var('func_12522')
call_14085 = relay.TupleGetItem(func_12520_call(), 0)
call_14086 = relay.TupleGetItem(func_12522_call(), 0)
func_2800_call = mod.get_global_var('func_2800')
func_2805_call = mutated_mod.get_global_var('func_2805')
var_14091 = relay.var("var_14091", dtype = "uint8", shape = ())#candidate|14091|()|var|uint8
var_14092 = relay.var("var_14092", dtype = "float32", shape = (150,))#candidate|14092|(150,)|var|float32
call_14090 = relay.TupleGetItem(func_2800_call(relay.reshape(call_14081.astype('uint16'), [15, 2, 10]), relay.reshape(var_14091.astype('uint8'), []), relay.reshape(var_14092.astype('float32'), [75, 2]), ), 2)
call_14093 = relay.TupleGetItem(func_2805_call(relay.reshape(call_14081.astype('uint16'), [15, 2, 10]), relay.reshape(var_14091.astype('uint8'), []), relay.reshape(var_14092.astype('float32'), [75, 2]), ), 2)
func_1678_call = mod.get_global_var('func_1678')
func_1682_call = mutated_mod.get_global_var('func_1682')
var_14114 = relay.var("var_14114", dtype = "uint8", shape = (72,))#candidate|14114|(72,)|var|uint8
call_14113 = relay.TupleGetItem(func_1678_call(relay.reshape(var_14091.astype('uint8'), []), relay.reshape(var_14114.astype('uint8'), [6, 2, 6]), relay.reshape(var_14092.astype('float32'), [150,]), ), 2)
call_14115 = relay.TupleGetItem(func_1682_call(relay.reshape(var_14091.astype('uint8'), []), relay.reshape(var_14114.astype('uint8'), [6, 2, 6]), relay.reshape(var_14092.astype('float32'), [150,]), ), 2)
output = relay.Tuple([call_14077,call_14081,call_14085,call_14090,var_14091,var_14092,call_14113,var_14114,])
output2 = relay.Tuple([call_14078,call_14082,call_14086,call_14093,var_14091,var_14092,call_14115,var_14114,])
func_14116 = relay.Function([var_14091,var_14092,var_14114,], output)
mod['func_14116'] = func_14116
mod = relay.transform.InferType()(mod)
var_14117 = relay.var("var_14117", dtype = "uint8", shape = ())#candidate|14117|()|var|uint8
var_14118 = relay.var("var_14118", dtype = "float32", shape = (150,))#candidate|14118|(150,)|var|float32
var_14119 = relay.var("var_14119", dtype = "uint8", shape = (72,))#candidate|14119|(72,)|var|uint8
output = func_14116(var_14117,var_14118,var_14119,)
func_14120 = relay.Function([var_14117,var_14118,var_14119,], output)
mutated_mod['func_14120'] = func_14120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12151_call = mod.get_global_var('func_12151')
func_12152_call = mutated_mod.get_global_var('func_12152')
call_14172 = relay.TupleGetItem(func_12151_call(), 0)
call_14173 = relay.TupleGetItem(func_12152_call(), 0)
func_14074_call = mod.get_global_var('func_14074')
func_14076_call = mutated_mod.get_global_var('func_14076')
call_14174 = relay.TupleGetItem(func_14074_call(), 4)
call_14175 = relay.TupleGetItem(func_14076_call(), 4)
func_11517_call = mod.get_global_var('func_11517')
func_11518_call = mutated_mod.get_global_var('func_11518')
call_14185 = func_11517_call()
call_14186 = func_11517_call()
output = relay.Tuple([call_14172,call_14174,call_14185,])
output2 = relay.Tuple([call_14173,call_14175,call_14186,])
func_14192 = relay.Function([], output)
mod['func_14192'] = func_14192
mod = relay.transform.InferType()(mod)
mutated_mod['func_14192'] = func_14192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14192_call = mutated_mod.get_global_var('func_14192')
call_14193 = func_14192_call()
output = call_14193
func_14194 = relay.Function([], output)
mutated_mod['func_14194'] = func_14194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8947_call = mod.get_global_var('func_8947')
func_8949_call = mutated_mod.get_global_var('func_8949')
call_14294 = relay.TupleGetItem(func_8947_call(), 0)
call_14295 = relay.TupleGetItem(func_8949_call(), 0)
func_10699_call = mod.get_global_var('func_10699')
func_10700_call = mutated_mod.get_global_var('func_10700')
call_14321 = relay.TupleGetItem(func_10699_call(), 0)
call_14322 = relay.TupleGetItem(func_10700_call(), 0)
func_7172_call = mod.get_global_var('func_7172')
func_7173_call = mutated_mod.get_global_var('func_7173')
call_14373 = relay.TupleGetItem(func_7172_call(), 2)
call_14374 = relay.TupleGetItem(func_7173_call(), 2)
output = relay.Tuple([call_14294,call_14321,call_14373,])
output2 = relay.Tuple([call_14295,call_14322,call_14374,])
func_14375 = relay.Function([], output)
mod['func_14375'] = func_14375
mod = relay.transform.InferType()(mod)
mutated_mod['func_14375'] = func_14375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14375_call = mutated_mod.get_global_var('func_14375')
call_14376 = func_14375_call()
output = call_14376
func_14377 = relay.Function([], output)
mutated_mod['func_14377'] = func_14377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13621_call = mod.get_global_var('func_13621')
func_13622_call = mutated_mod.get_global_var('func_13622')
call_14424 = relay.TupleGetItem(func_13621_call(), 1)
call_14425 = relay.TupleGetItem(func_13622_call(), 1)
output = call_14424
output2 = call_14425
func_14446 = relay.Function([], output)
mod['func_14446'] = func_14446
mod = relay.transform.InferType()(mod)
mutated_mod['func_14446'] = func_14446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14446_call = mutated_mod.get_global_var('func_14446')
call_14447 = func_14446_call()
output = call_14447
func_14448 = relay.Function([], output)
mutated_mod['func_14448'] = func_14448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8849_call = mod.get_global_var('func_8849')
func_8850_call = mutated_mod.get_global_var('func_8850')
call_14486 = func_8849_call()
call_14487 = func_8849_call()
output = call_14486
output2 = call_14487
func_14522 = relay.Function([], output)
mod['func_14522'] = func_14522
mod = relay.transform.InferType()(mod)
output = func_14522()
func_14523 = relay.Function([], output)
mutated_mod['func_14523'] = func_14523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12151_call = mod.get_global_var('func_12151')
func_12152_call = mutated_mod.get_global_var('func_12152')
call_14529 = relay.TupleGetItem(func_12151_call(), 0)
call_14530 = relay.TupleGetItem(func_12152_call(), 0)
output = relay.Tuple([call_14529,])
output2 = relay.Tuple([call_14530,])
func_14533 = relay.Function([], output)
mod['func_14533'] = func_14533
mod = relay.transform.InferType()(mod)
mutated_mod['func_14533'] = func_14533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14533_call = mutated_mod.get_global_var('func_14533')
call_14534 = func_14533_call()
output = call_14534
func_14535 = relay.Function([], output)
mutated_mod['func_14535'] = func_14535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9677_call = mod.get_global_var('func_9677')
func_9679_call = mutated_mod.get_global_var('func_9679')
call_14577 = func_9677_call()
call_14578 = func_9677_call()
output = relay.Tuple([call_14577,])
output2 = relay.Tuple([call_14578,])
func_14587 = relay.Function([], output)
mod['func_14587'] = func_14587
mod = relay.transform.InferType()(mod)
mutated_mod['func_14587'] = func_14587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14587_call = mutated_mod.get_global_var('func_14587')
call_14588 = func_14587_call()
output = call_14588
func_14589 = relay.Function([], output)
mutated_mod['func_14589'] = func_14589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9961_call = mod.get_global_var('func_9961')
func_9962_call = mutated_mod.get_global_var('func_9962')
call_14593 = relay.TupleGetItem(func_9961_call(), 0)
call_14594 = relay.TupleGetItem(func_9962_call(), 0)
output = call_14593
output2 = call_14594
func_14598 = relay.Function([], output)
mod['func_14598'] = func_14598
mod = relay.transform.InferType()(mod)
mutated_mod['func_14598'] = func_14598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14598_call = mutated_mod.get_global_var('func_14598')
call_14599 = func_14598_call()
output = call_14599
func_14600 = relay.Function([], output)
mutated_mod['func_14600'] = func_14600
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14615 = relay.var("var_14615", dtype = "float64", shape = (4, 11, 4))#candidate|14615|(4, 11, 4)|var|float64
uop_14616 = relay.asin(var_14615.astype('float64')) # shape=(4, 11, 4)
output = uop_14616
output2 = uop_14616
func_14625 = relay.Function([var_14615,], output)
mod['func_14625'] = func_14625
mod = relay.transform.InferType()(mod)
var_14626 = relay.var("var_14626", dtype = "float64", shape = (4, 11, 4))#candidate|14626|(4, 11, 4)|var|float64
output = func_14625(var_14626)
func_14627 = relay.Function([var_14626], output)
mutated_mod['func_14627'] = func_14627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8065_call = mod.get_global_var('func_8065')
func_8067_call = mutated_mod.get_global_var('func_8067')
call_14632 = relay.TupleGetItem(func_8065_call(), 0)
call_14633 = relay.TupleGetItem(func_8067_call(), 0)
output = relay.Tuple([call_14632,])
output2 = relay.Tuple([call_14633,])
func_14641 = relay.Function([], output)
mod['func_14641'] = func_14641
mod = relay.transform.InferType()(mod)
output = func_14641()
func_14642 = relay.Function([], output)
mutated_mod['func_14642'] = func_14642
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14649 = relay.var("var_14649", dtype = "float64", shape = (12, 15, 1))#candidate|14649|(12, 15, 1)|var|float64
var_14650 = relay.var("var_14650", dtype = "float64", shape = (12, 15, 10))#candidate|14650|(12, 15, 10)|var|float64
bop_14651 = relay.mod(var_14649.astype('float64'), var_14650.astype('float64')) # shape=(12, 15, 10)
func_10191_call = mod.get_global_var('func_10191')
func_10193_call = mutated_mod.get_global_var('func_10193')
call_14658 = relay.TupleGetItem(func_10191_call(), 0)
call_14659 = relay.TupleGetItem(func_10193_call(), 0)
output = relay.Tuple([bop_14651,call_14658,])
output2 = relay.Tuple([bop_14651,call_14659,])
func_14664 = relay.Function([var_14649,var_14650,], output)
mod['func_14664'] = func_14664
mod = relay.transform.InferType()(mod)
var_14665 = relay.var("var_14665", dtype = "float64", shape = (12, 15, 1))#candidate|14665|(12, 15, 1)|var|float64
var_14666 = relay.var("var_14666", dtype = "float64", shape = (12, 15, 10))#candidate|14666|(12, 15, 10)|var|float64
output = func_14664(var_14665,var_14666,)
func_14667 = relay.Function([var_14665,var_14666,], output)
mutated_mod['func_14667'] = func_14667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_14713 = relay.TupleGetItem(func_7413_call(), 1)
call_14714 = relay.TupleGetItem(func_7415_call(), 1)
func_4176_call = mod.get_global_var('func_4176')
func_4179_call = mutated_mod.get_global_var('func_4179')
var_14748 = relay.var("var_14748", dtype = "bool", shape = (208,))#candidate|14748|(208,)|var|bool
call_14747 = relay.TupleGetItem(func_4176_call(relay.reshape(var_14748.astype('bool'), [1, 208])), 1)
call_14749 = relay.TupleGetItem(func_4179_call(relay.reshape(var_14748.astype('bool'), [1, 208])), 1)
output = relay.Tuple([call_14713,call_14747,var_14748,])
output2 = relay.Tuple([call_14714,call_14749,var_14748,])
func_14752 = relay.Function([var_14748,], output)
mod['func_14752'] = func_14752
mod = relay.transform.InferType()(mod)
mutated_mod['func_14752'] = func_14752
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14753 = relay.var("var_14753", dtype = "bool", shape = (208,))#candidate|14753|(208,)|var|bool
func_14752_call = mutated_mod.get_global_var('func_14752')
call_14754 = func_14752_call(var_14753)
output = call_14754
func_14755 = relay.Function([var_14753], output)
mutated_mod['func_14755'] = func_14755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10872_call = mod.get_global_var('func_10872')
func_10873_call = mutated_mod.get_global_var('func_10873')
call_14767 = relay.TupleGetItem(func_10872_call(), 1)
call_14768 = relay.TupleGetItem(func_10873_call(), 1)
func_9184_call = mod.get_global_var('func_9184')
func_9185_call = mutated_mod.get_global_var('func_9185')
call_14775 = relay.TupleGetItem(func_9184_call(), 0)
call_14776 = relay.TupleGetItem(func_9185_call(), 0)
output = relay.Tuple([call_14767,call_14775,])
output2 = relay.Tuple([call_14768,call_14776,])
func_14778 = relay.Function([], output)
mod['func_14778'] = func_14778
mod = relay.transform.InferType()(mod)
output = func_14778()
func_14779 = relay.Function([], output)
mutated_mod['func_14779'] = func_14779
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14785 = relay.const([[[2.511395,-2.142970,-7.448738,2.646331,0.135261,-9.018035,-0.463720,-6.483687,-6.763570,1.075491],[2.706095,9.156281,8.954264,-6.783139,7.184626,4.113171,-3.191711,-0.715328,2.083379,6.137737],[-7.228743,-3.691885,-0.714984,8.302146,-1.795838,-0.446681,-2.210261,5.924262,4.672590,2.372642],[0.469305,6.711684,-1.671688,-2.997990,-3.154730,-7.234295,7.723080,8.478678,-4.357468,-5.363467],[1.034131,-7.733844,0.161555,3.233907,1.530666,7.811937,6.512384,4.444910,-3.626975,-5.738769],[2.817157,8.571980,9.583784,-8.752316,4.847998,-6.411521,-5.944106,-6.442815,-4.430659,-5.234665],[4.935144,1.857170,1.193977,-8.351454,-7.703954,-5.562898,-9.879379,4.064151,-9.255734,5.153393],[-4.473705,-7.322668,-9.830847,-3.532382,1.447958,-3.073709,-9.185789,4.668228,-0.437451,9.833397],[-3.975352,-3.960815,2.165193,0.765036,-0.472550,4.312175,-3.271817,9.727876,2.773709,-5.576858],[-1.924465,7.805603,-6.960891,-4.672800,-6.220075,2.741787,4.925281,9.900985,9.240996,-0.034030]],[[3.311859,0.505351,-0.887113,-5.862348,-0.201396,-4.484413,-8.806669,-1.446162,-5.373628,3.333413],[-6.382569,-7.906888,2.522309,8.285697,-0.541532,-4.966174,5.957686,9.417961,-2.164018,4.548869],[-3.494623,4.494087,1.936404,8.709074,8.334977,0.555129,-4.325700,9.909943,1.418249,-7.699321],[9.569801,-3.603070,-7.581469,-3.284362,5.898810,-5.473118,8.522338,-6.195269,5.083965,-6.634470],[0.869734,-5.557710,8.943716,0.405636,-1.210488,-9.402437,-2.911882,7.784753,8.168128,2.831738],[5.355142,-8.169173,4.334121,-1.927090,5.515676,1.477050,-1.539754,-0.477592,-8.701944,-5.491800],[0.405816,-2.990590,0.852662,0.881133,7.076383,-8.254580,-3.252691,0.209613,1.513667,-6.801963],[-0.068426,2.912999,0.774661,7.944217,1.345589,4.666449,-1.957698,-2.956127,9.421884,-9.732835],[-5.791510,0.936244,-6.648991,0.376303,-9.208395,-6.000421,3.214534,7.570930,4.125048,-8.113114],[6.852418,5.587380,4.630702,1.655560,2.738663,7.825615,-4.001253,-1.558405,9.381308,0.795744]]], dtype = "float64")#candidate|14785|(2, 10, 10)|const|float64
var_14786 = relay.var("var_14786", dtype = "float64", shape = (2, 10, 10))#candidate|14786|(2, 10, 10)|var|float64
bop_14787 = relay.floor_mod(const_14785.astype('float64'), relay.reshape(var_14786.astype('float64'), relay.shape_of(const_14785))) # shape=(2, 10, 10)
output = relay.Tuple([bop_14787,])
output2 = relay.Tuple([bop_14787,])
func_14792 = relay.Function([var_14786,], output)
mod['func_14792'] = func_14792
mod = relay.transform.InferType()(mod)
var_14793 = relay.var("var_14793", dtype = "float64", shape = (2, 10, 10))#candidate|14793|(2, 10, 10)|var|float64
output = func_14792(var_14793)
func_14794 = relay.Function([var_14793], output)
mutated_mod['func_14794'] = func_14794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10872_call = mod.get_global_var('func_10872')
func_10873_call = mutated_mod.get_global_var('func_10873')
call_14810 = relay.TupleGetItem(func_10872_call(), 0)
call_14811 = relay.TupleGetItem(func_10873_call(), 0)
output = call_14810
output2 = call_14811
func_14845 = relay.Function([], output)
mod['func_14845'] = func_14845
mod = relay.transform.InferType()(mod)
output = func_14845()
func_14846 = relay.Function([], output)
mutated_mod['func_14846'] = func_14846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14522_call = mod.get_global_var('func_14522')
func_14523_call = mutated_mod.get_global_var('func_14523')
call_14859 = func_14522_call()
call_14860 = func_14522_call()
output = relay.Tuple([call_14859,])
output2 = relay.Tuple([call_14860,])
func_14874 = relay.Function([], output)
mod['func_14874'] = func_14874
mod = relay.transform.InferType()(mod)
output = func_14874()
func_14875 = relay.Function([], output)
mutated_mod['func_14875'] = func_14875
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14878 = relay.const([[[9,9,6,7,-3,-3,9,5,-6,-6,-4,4,3,6],[-10,-9,8,-3,5,-8,6,-3,5,3,-4,10,1,-7],[9,-6,-8,6,-2,-10,-8,7,-2,-9,10,-8,2,2],[5,10,5,-3,-10,10,-9,-10,9,-2,-8,9,4,-4],[-7,-2,8,-6,-7,-5,-9,10,5,4,-7,-6,9,5],[-3,10,5,-4,-3,3,9,-8,5,4,-9,-6,9,3]],[[9,9,-7,4,10,-5,8,4,8,-6,1,-4,10,-9],[6,-5,10,-9,-3,-6,-10,-8,1,-8,6,-3,-3,9],[1,-2,-10,1,3,4,2,-10,3,3,-2,2,-4,-6],[3,8,-5,-8,9,4,9,1,10,-4,-9,-6,7,-10],[-2,-5,4,-7,-8,-4,4,3,6,3,-3,-8,5,7],[1,-2,-4,7,4,6,9,-1,10,8,-5,-3,-9,5]],[[6,-5,-9,-9,6,10,-10,-4,-8,5,10,-5,4,7],[10,7,-4,-2,-1,-6,7,-1,-4,-9,1,-2,5,5],[-7,5,4,3,8,3,-8,-8,-6,-3,3,3,-6,-4],[4,2,-10,1,3,-2,-1,10,-3,-4,7,-9,1,-6],[-7,-8,8,2,-9,3,-9,2,-1,9,1,5,3,10],[-6,-1,-7,-5,10,-4,-2,-2,-6,-1,7,3,3,5]],[[3,-10,-2,-3,-1,-5,-4,2,7,-7,10,-10,-7,-4],[10,-8,7,-2,-10,-9,1,-4,2,-3,1,4,7,8],[-6,8,-2,-10,6,-9,7,9,-1,-5,8,3,-9,3],[-10,1,3,-3,6,5,5,10,9,2,-4,-2,6,-4],[-4,-10,-7,-2,2,7,-9,2,4,6,3,3,4,2],[3,-4,4,-3,6,-3,-1,4,1,-3,-8,-8,6,10]],[[9,9,-1,-8,4,-10,-7,9,-3,9,9,-9,-1,-1],[10,-7,5,-10,-9,-5,-2,-5,6,-8,-7,3,8,-4],[-10,-6,-6,1,10,-2,-2,2,-2,4,9,6,-10,1],[-4,-7,-9,7,7,-1,-9,-4,9,-6,10,-8,-1,-4],[-5,9,9,-4,-8,-6,-10,9,-9,2,-8,-9,-6,9],[3,-10,-10,8,4,10,6,4,4,-5,8,-2,-6,9]],[[10,-1,1,1,-10,-1,-4,6,-6,6,-6,4,10,4],[-7,-10,-1,1,-4,-5,3,9,-6,7,-5,-3,-8,9],[-3,4,6,-8,-6,-10,1,-5,1,2,-8,3,-6,6],[-3,1,-8,7,-8,-10,2,-5,5,-7,-3,-6,-10,4],[-5,-9,5,-6,5,-4,8,9,4,-3,1,7,-1,-5],[-2,-8,-9,-7,6,-7,9,-6,-7,-5,9,2,-9,6]],[[-10,10,9,-10,4,-3,3,3,-1,-8,-6,-1,-2,6],[10,1,2,3,-9,10,-2,-6,-2,8,-8,2,-9,10],[4,3,8,7,5,-1,-4,-8,5,3,2,9,-8,-7],[-3,-8,-1,-4,-5,10,2,-4,4,5,5,5,1,-1],[-8,-6,3,10,5,6,-7,-9,10,7,5,-3,2,-2],[-5,-4,1,-4,3,10,-9,9,-3,-7,2,-6,8,1]],[[-9,-4,6,-7,-9,-1,6,2,8,-3,10,3,-6,10],[8,3,-4,4,-9,9,4,2,-3,-7,-8,3,2,1],[-5,-1,4,-2,5,10,-9,-1,9,2,10,5,2,5],[2,-4,-8,-1,1,1,-9,1,10,-10,-5,-2,-4,2],[-3,-1,-2,-3,10,-3,5,-10,-6,4,-2,6,-1,-4],[-5,2,-3,6,-8,8,-1,10,4,4,-10,6,5,3]]], dtype = "uint8")#candidate|14878|(8, 6, 14)|const|uint8
var_14879 = relay.var("var_14879", dtype = "uint8", shape = (8, 6, 14))#candidate|14879|(8, 6, 14)|var|uint8
bop_14880 = relay.greater(const_14878.astype('bool'), relay.reshape(var_14879.astype('bool'), relay.shape_of(const_14878))) # shape=(8, 6, 14)
output = relay.Tuple([bop_14880,])
output2 = relay.Tuple([bop_14880,])
func_14884 = relay.Function([var_14879,], output)
mod['func_14884'] = func_14884
mod = relay.transform.InferType()(mod)
var_14885 = relay.var("var_14885", dtype = "uint8", shape = (8, 6, 14))#candidate|14885|(8, 6, 14)|var|uint8
output = func_14884(var_14885)
func_14886 = relay.Function([var_14885], output)
mutated_mod['func_14886'] = func_14886
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14898 = relay.var("var_14898", dtype = "float32", shape = (4, 10, 3))#candidate|14898|(4, 10, 3)|var|float32
uop_14899 = relay.sinh(var_14898.astype('float32')) # shape=(4, 10, 3)
output = uop_14899
output2 = uop_14899
func_14908 = relay.Function([var_14898,], output)
mod['func_14908'] = func_14908
mod = relay.transform.InferType()(mod)
mutated_mod['func_14908'] = func_14908
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14909 = relay.var("var_14909", dtype = "float32", shape = (4, 10, 3))#candidate|14909|(4, 10, 3)|var|float32
func_14908_call = mutated_mod.get_global_var('func_14908')
call_14910 = func_14908_call(var_14909)
output = call_14910
func_14911 = relay.Function([var_14909], output)
mutated_mod['func_14911'] = func_14911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8292_call = mod.get_global_var('func_8292')
func_8293_call = mutated_mod.get_global_var('func_8293')
call_14916 = func_8292_call()
call_14917 = func_8292_call()
output = relay.Tuple([call_14916,])
output2 = relay.Tuple([call_14917,])
func_14930 = relay.Function([], output)
mod['func_14930'] = func_14930
mod = relay.transform.InferType()(mod)
mutated_mod['func_14930'] = func_14930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14930_call = mutated_mod.get_global_var('func_14930')
call_14931 = func_14930_call()
output = call_14931
func_14932 = relay.Function([], output)
mutated_mod['func_14932'] = func_14932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9600_call = mod.get_global_var('func_9600')
func_9602_call = mutated_mod.get_global_var('func_9602')
call_14971 = relay.TupleGetItem(func_9600_call(), 0)
call_14972 = relay.TupleGetItem(func_9602_call(), 0)
func_13621_call = mod.get_global_var('func_13621')
func_13622_call = mutated_mod.get_global_var('func_13622')
call_14973 = relay.TupleGetItem(func_13621_call(), 0)
call_14974 = relay.TupleGetItem(func_13622_call(), 0)
output = relay.Tuple([call_14971,call_14973,])
output2 = relay.Tuple([call_14972,call_14974,])
func_14980 = relay.Function([], output)
mod['func_14980'] = func_14980
mod = relay.transform.InferType()(mod)
output = func_14980()
func_14981 = relay.Function([], output)
mutated_mod['func_14981'] = func_14981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12242_call = mod.get_global_var('func_12242')
func_12243_call = mutated_mod.get_global_var('func_12243')
call_15048 = func_12242_call()
call_15049 = func_12242_call()
func_14116_call = mod.get_global_var('func_14116')
func_14120_call = mutated_mod.get_global_var('func_14120')
const_15091 = relay.const(-8, dtype = "uint8")#candidate|15091|()|const|uint8
var_15092 = relay.var("var_15092", dtype = "float32", shape = (150,))#candidate|15092|(150,)|var|float32
var_15093 = relay.var("var_15093", dtype = "uint8", shape = (72,))#candidate|15093|(72,)|var|uint8
call_15090 = relay.TupleGetItem(func_14116_call(relay.reshape(const_15091.astype('uint8'), []), relay.reshape(var_15092.astype('float32'), [150,]), relay.reshape(var_15093.astype('uint8'), [72,]), ), 5)
call_15094 = relay.TupleGetItem(func_14120_call(relay.reshape(const_15091.astype('uint8'), []), relay.reshape(var_15092.astype('float32'), [150,]), relay.reshape(var_15093.astype('uint8'), [72,]), ), 5)
func_12394_call = mod.get_global_var('func_12394')
func_12397_call = mutated_mod.get_global_var('func_12397')
var_15114 = relay.var("var_15114", dtype = "bool", shape = (540,))#candidate|15114|(540,)|var|bool
call_15113 = relay.TupleGetItem(func_12394_call(relay.reshape(const_15091.astype('bool'), []), relay.reshape(var_15114.astype('bool'), [6, 10, 9]), ), 2)
call_15115 = relay.TupleGetItem(func_12397_call(relay.reshape(const_15091.astype('bool'), []), relay.reshape(var_15114.astype('bool'), [6, 10, 9]), ), 2)
func_12394_call = mod.get_global_var('func_12394')
func_12397_call = mutated_mod.get_global_var('func_12397')
call_15119 = relay.TupleGetItem(func_12394_call(relay.reshape(const_15091.astype('bool'), []), relay.reshape(var_15114.astype('bool'), [6, 10, 9]), ), 1)
call_15120 = relay.TupleGetItem(func_12397_call(relay.reshape(const_15091.astype('bool'), []), relay.reshape(var_15114.astype('bool'), [6, 10, 9]), ), 1)
output = relay.Tuple([call_15048,call_15090,const_15091,var_15092,var_15093,call_15113,var_15114,call_15119,])
output2 = relay.Tuple([call_15049,call_15094,const_15091,var_15092,var_15093,call_15115,var_15114,call_15120,])
func_15123 = relay.Function([var_15092,var_15093,var_15114,], output)
mod['func_15123'] = func_15123
mod = relay.transform.InferType()(mod)
var_15124 = relay.var("var_15124", dtype = "float32", shape = (150,))#candidate|15124|(150,)|var|float32
var_15125 = relay.var("var_15125", dtype = "uint8", shape = (72,))#candidate|15125|(72,)|var|uint8
var_15126 = relay.var("var_15126", dtype = "bool", shape = (540,))#candidate|15126|(540,)|var|bool
output = func_15123(var_15124,var_15125,var_15126,)
func_15127 = relay.Function([var_15124,var_15125,var_15126,], output)
mutated_mod['func_15127'] = func_15127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14446_call = mod.get_global_var('func_14446')
func_14448_call = mutated_mod.get_global_var('func_14448')
call_15148 = func_14446_call()
call_15149 = func_14446_call()
func_9994_call = mod.get_global_var('func_9994')
func_9996_call = mutated_mod.get_global_var('func_9996')
call_15160 = func_9994_call()
call_15161 = func_9994_call()
output = relay.Tuple([call_15148,call_15160,])
output2 = relay.Tuple([call_15149,call_15161,])
func_15163 = relay.Function([], output)
mod['func_15163'] = func_15163
mod = relay.transform.InferType()(mod)
mutated_mod['func_15163'] = func_15163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15163_call = mutated_mod.get_global_var('func_15163')
call_15164 = func_15163_call()
output = call_15164
func_15165 = relay.Function([], output)
mutated_mod['func_15165'] = func_15165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14874_call = mod.get_global_var('func_14874')
func_14875_call = mutated_mod.get_global_var('func_14875')
call_15166 = relay.TupleGetItem(func_14874_call(), 0)
call_15167 = relay.TupleGetItem(func_14875_call(), 0)
output = relay.Tuple([call_15166,])
output2 = relay.Tuple([call_15167,])
func_15168 = relay.Function([], output)
mod['func_15168'] = func_15168
mod = relay.transform.InferType()(mod)
output = func_15168()
func_15169 = relay.Function([], output)
mutated_mod['func_15169'] = func_15169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9363_call = mod.get_global_var('func_9363')
func_9365_call = mutated_mod.get_global_var('func_9365')
call_15249 = relay.TupleGetItem(func_9363_call(), 0)
call_15250 = relay.TupleGetItem(func_9365_call(), 0)
output = call_15249
output2 = call_15250
func_15253 = relay.Function([], output)
mod['func_15253'] = func_15253
mod = relay.transform.InferType()(mod)
mutated_mod['func_15253'] = func_15253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15253_call = mutated_mod.get_global_var('func_15253')
call_15254 = func_15253_call()
output = call_15254
func_15255 = relay.Function([], output)
mutated_mod['func_15255'] = func_15255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mod.get_global_var('func_9726')
func_9728_call = mutated_mod.get_global_var('func_9728')
call_15281 = relay.TupleGetItem(func_9726_call(), 0)
call_15282 = relay.TupleGetItem(func_9728_call(), 0)
func_9218_call = mod.get_global_var('func_9218')
func_9220_call = mutated_mod.get_global_var('func_9220')
call_15307 = relay.TupleGetItem(func_9218_call(), 0)
call_15308 = relay.TupleGetItem(func_9220_call(), 0)
output = relay.Tuple([call_15281,call_15307,])
output2 = relay.Tuple([call_15282,call_15308,])
func_15310 = relay.Function([], output)
mod['func_15310'] = func_15310
mod = relay.transform.InferType()(mod)
mutated_mod['func_15310'] = func_15310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15310_call = mutated_mod.get_global_var('func_15310')
call_15311 = func_15310_call()
output = call_15311
func_15312 = relay.Function([], output)
mutated_mod['func_15312'] = func_15312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10239_call = mod.get_global_var('func_10239')
func_10240_call = mutated_mod.get_global_var('func_10240')
call_15346 = func_10239_call()
call_15347 = func_10239_call()
output = call_15346
output2 = call_15347
func_15369 = relay.Function([], output)
mod['func_15369'] = func_15369
mod = relay.transform.InferType()(mod)
output = func_15369()
func_15370 = relay.Function([], output)
mutated_mod['func_15370'] = func_15370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11664_call = mod.get_global_var('func_11664')
func_11666_call = mutated_mod.get_global_var('func_11666')
call_15475 = func_11664_call()
call_15476 = func_11664_call()
func_12095_call = mod.get_global_var('func_12095')
func_12097_call = mutated_mod.get_global_var('func_12097')
call_15488 = relay.TupleGetItem(func_12095_call(), 0)
call_15489 = relay.TupleGetItem(func_12097_call(), 0)
output = relay.Tuple([call_15475,call_15488,])
output2 = relay.Tuple([call_15476,call_15489,])
func_15511 = relay.Function([], output)
mod['func_15511'] = func_15511
mod = relay.transform.InferType()(mod)
mutated_mod['func_15511'] = func_15511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15511_call = mutated_mod.get_global_var('func_15511')
call_15512 = func_15511_call()
output = call_15512
func_15513 = relay.Function([], output)
mutated_mod['func_15513'] = func_15513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10338_call = mod.get_global_var('func_10338')
func_10339_call = mutated_mod.get_global_var('func_10339')
call_15517 = relay.TupleGetItem(func_10338_call(), 0)
call_15518 = relay.TupleGetItem(func_10339_call(), 0)
output = relay.Tuple([call_15517,])
output2 = relay.Tuple([call_15518,])
func_15524 = relay.Function([], output)
mod['func_15524'] = func_15524
mod = relay.transform.InferType()(mod)
output = func_15524()
func_15525 = relay.Function([], output)
mutated_mod['func_15525'] = func_15525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15526 = relay.var("var_15526", dtype = "uint32", shape = (12, 11, 16))#candidate|15526|(12, 11, 16)|var|uint32
var_15527 = relay.var("var_15527", dtype = "uint32", shape = (12, 11, 16))#candidate|15527|(12, 11, 16)|var|uint32
bop_15528 = relay.right_shift(var_15526.astype('uint32'), relay.reshape(var_15527.astype('uint32'), relay.shape_of(var_15526))) # shape=(12, 11, 16)
output = bop_15528
output2 = bop_15528
func_15534 = relay.Function([var_15526,var_15527,], output)
mod['func_15534'] = func_15534
mod = relay.transform.InferType()(mod)
mutated_mod['func_15534'] = func_15534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15534_call = mutated_mod.get_global_var('func_15534')
var_15536 = relay.var("var_15536", dtype = "uint32", shape = (12, 11, 16))#candidate|15536|(12, 11, 16)|var|uint32
var_15537 = relay.var("var_15537", dtype = "uint32", shape = (12, 11, 16))#candidate|15537|(12, 11, 16)|var|uint32
call_15535 = func_15534_call(var_15536,var_15537,)
output = call_15535
func_15538 = relay.Function([var_15536,var_15537,], output)
mutated_mod['func_15538'] = func_15538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15524_call = mod.get_global_var('func_15524')
func_15525_call = mutated_mod.get_global_var('func_15525')
call_15546 = relay.TupleGetItem(func_15524_call(), 0)
call_15547 = relay.TupleGetItem(func_15525_call(), 0)
func_13277_call = mod.get_global_var('func_13277')
func_13279_call = mutated_mod.get_global_var('func_13279')
call_15579 = relay.TupleGetItem(func_13277_call(), 0)
call_15580 = relay.TupleGetItem(func_13279_call(), 0)
func_12520_call = mod.get_global_var('func_12520')
func_12522_call = mutated_mod.get_global_var('func_12522')
call_15584 = relay.TupleGetItem(func_12520_call(), 0)
call_15585 = relay.TupleGetItem(func_12522_call(), 0)
func_8711_call = mod.get_global_var('func_8711')
func_8713_call = mutated_mod.get_global_var('func_8713')
call_15589 = relay.TupleGetItem(func_8711_call(), 1)
call_15590 = relay.TupleGetItem(func_8713_call(), 1)
func_11336_call = mod.get_global_var('func_11336')
func_11337_call = mutated_mod.get_global_var('func_11337')
call_15615 = func_11336_call()
call_15616 = func_11336_call()
func_9802_call = mod.get_global_var('func_9802')
func_9804_call = mutated_mod.get_global_var('func_9804')
var_15633 = relay.var("var_15633", dtype = "bool", shape = (52, 4))#candidate|15633|(52, 4)|var|bool
call_15632 = relay.TupleGetItem(func_9802_call(relay.reshape(var_15633.astype('bool'), [208,])), 4)
call_15634 = relay.TupleGetItem(func_9804_call(relay.reshape(var_15633.astype('bool'), [208,])), 4)
func_10239_call = mod.get_global_var('func_10239')
func_10240_call = mutated_mod.get_global_var('func_10240')
call_15640 = func_10239_call()
call_15641 = func_10239_call()
output = relay.Tuple([call_15546,call_15579,call_15584,call_15589,call_15615,call_15632,var_15633,call_15640,])
output2 = relay.Tuple([call_15547,call_15580,call_15585,call_15590,call_15616,call_15634,var_15633,call_15641,])
func_15655 = relay.Function([var_15633,], output)
mod['func_15655'] = func_15655
mod = relay.transform.InferType()(mod)
mutated_mod['func_15655'] = func_15655
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15656 = relay.var("var_15656", dtype = "bool", shape = (52, 4))#candidate|15656|(52, 4)|var|bool
func_15655_call = mutated_mod.get_global_var('func_15655')
call_15657 = func_15655_call(var_15656)
output = call_15657
func_15658 = relay.Function([var_15656], output)
mutated_mod['func_15658'] = func_15658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14074_call = mod.get_global_var('func_14074')
func_14076_call = mutated_mod.get_global_var('func_14076')
call_15728 = relay.TupleGetItem(func_14074_call(), 3)
call_15729 = relay.TupleGetItem(func_14076_call(), 3)
func_14116_call = mod.get_global_var('func_14116')
func_14120_call = mutated_mod.get_global_var('func_14120')
var_15732 = relay.var("var_15732", dtype = "uint8", shape = ())#candidate|15732|()|var|uint8
const_15733 = relay.const([6.472655,7.880944,-2.808162,3.532102,7.927088,0.899337,-0.299168,7.988249,-7.415129,6.032263,2.816564,6.031317,-5.094761,-0.044765,-7.015975,-3.849458,-3.556683,7.852996,-8.735943,2.289273,-3.303815,2.590042,9.765157,-9.524946,6.907450,-1.213623,6.478194,9.872939,2.773622,4.173624,0.029344,9.972894,-8.924389,-8.114382,-8.553490,-1.867087,0.871310,9.142972,-4.299449,-1.881927,-3.980545,-5.573456,7.972374,6.325088,-6.410033,-2.699964,-5.716786,6.104401,-2.840399,6.567455,0.968997,8.248983,-3.401820,1.249689,-7.836696,-2.786017,-2.936043,-4.108149,-7.162054,-4.151609,4.325239,-3.451570,3.531551,-0.103101,-5.453813,-6.738596,0.567538,-6.850599,-5.407747,-7.605999,3.660594,1.117108,8.461822,0.990882,2.845871,-2.977952,-2.432399,-8.092271,5.269078,6.872049,7.573188,6.156517,2.107839,-1.572824,-5.001434,6.899424,8.288687,5.180341,-8.208491,-9.536365,9.363181,-8.148669,1.931781,3.465384,0.496570,-9.783940,-7.492355,7.493466,5.128751,4.638897,-0.968411,-6.108722,-8.960506,9.936482,-7.049512,-1.732232,-0.173103,-4.849721,-8.225306,-7.833574,-9.187445,-5.014870,5.851151,5.992783,4.435751,-8.196099,2.051855,6.306547,-5.580821,-4.635297,-0.486733,-3.399847,-6.476482,-9.213042,-8.327047,-3.468414,-3.096882,1.407460,3.051111,-5.743152,-0.311000,-8.092247,8.584129,6.341772,-1.269101,3.393165,-3.834834,-8.758450,-3.290645,9.578559,7.230548,0.244079,-9.205880,5.616728,7.369131,-4.372626,-3.020783,5.802218,-1.678103,-5.076575], dtype = "float32")#candidate|15733|(150,)|const|float32
const_15734 = relay.const([-7,7,-3,5,-7,-7,-6,-8,5,-4,-5,-4,-9,4,-9,9,9,-3,-8,6,-3,2,6,-8,5,9,6,4,-4,-3,9,-8,6,3,-2,-9,-4,4,10,-10,6,5,-3,-7,9,-9,-2,9,10,3,-2,7,-5,5,5,-10,-7,2,6,-4,-1,-5,9,2,5,3,8,-3,-3,8,-4,-8], dtype = "uint8")#candidate|15734|(72,)|const|uint8
call_15731 = relay.TupleGetItem(func_14116_call(relay.reshape(var_15732.astype('uint8'), []), relay.reshape(const_15733.astype('float32'), [150,]), relay.reshape(const_15734.astype('uint8'), [72,]), ), 4)
call_15735 = relay.TupleGetItem(func_14120_call(relay.reshape(var_15732.astype('uint8'), []), relay.reshape(const_15733.astype('float32'), [150,]), relay.reshape(const_15734.astype('uint8'), [72,]), ), 4)
func_2800_call = mod.get_global_var('func_2800')
func_2805_call = mutated_mod.get_global_var('func_2805')
call_15742 = relay.TupleGetItem(func_2800_call(relay.reshape(call_15728.astype('uint16'), [15, 2, 10]), relay.reshape(var_15732.astype('uint8'), []), relay.reshape(const_15733.astype('float32'), [75, 2]), ), 1)
call_15743 = relay.TupleGetItem(func_2805_call(relay.reshape(call_15728.astype('uint16'), [15, 2, 10]), relay.reshape(var_15732.astype('uint8'), []), relay.reshape(const_15733.astype('float32'), [75, 2]), ), 1)
func_9651_call = mod.get_global_var('func_9651')
func_9653_call = mutated_mod.get_global_var('func_9653')
call_15744 = func_9651_call()
call_15745 = func_9651_call()
output = relay.Tuple([call_15728,call_15731,var_15732,const_15733,const_15734,call_15742,call_15744,])
output2 = relay.Tuple([call_15729,call_15735,var_15732,const_15733,const_15734,call_15743,call_15745,])
func_15746 = relay.Function([var_15732,], output)
mod['func_15746'] = func_15746
mod = relay.transform.InferType()(mod)
mutated_mod['func_15746'] = func_15746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15747 = relay.var("var_15747", dtype = "uint8", shape = ())#candidate|15747|()|var|uint8
func_15746_call = mutated_mod.get_global_var('func_15746')
call_15748 = func_15746_call(var_15747)
output = call_15748
func_15749 = relay.Function([var_15747], output)
mutated_mod['func_15749'] = func_15749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8849_call = mod.get_global_var('func_8849')
func_8850_call = mutated_mod.get_global_var('func_8850')
call_15791 = func_8849_call()
call_15792 = func_8849_call()
output = relay.Tuple([call_15791,])
output2 = relay.Tuple([call_15792,])
func_15877 = relay.Function([], output)
mod['func_15877'] = func_15877
mod = relay.transform.InferType()(mod)
output = func_15877()
func_15878 = relay.Function([], output)
mutated_mod['func_15878'] = func_15878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11664_call = mod.get_global_var('func_11664')
func_11666_call = mutated_mod.get_global_var('func_11666')
call_15894 = func_11664_call()
call_15895 = func_11664_call()
output = relay.Tuple([call_15894,])
output2 = relay.Tuple([call_15895,])
func_15919 = relay.Function([], output)
mod['func_15919'] = func_15919
mod = relay.transform.InferType()(mod)
mutated_mod['func_15919'] = func_15919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15919_call = mutated_mod.get_global_var('func_15919')
call_15920 = func_15919_call()
output = call_15920
func_15921 = relay.Function([], output)
mutated_mod['func_15921'] = func_15921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13621_call = mod.get_global_var('func_13621')
func_13622_call = mutated_mod.get_global_var('func_13622')
call_15928 = relay.TupleGetItem(func_13621_call(), 1)
call_15929 = relay.TupleGetItem(func_13622_call(), 1)
func_8089_call = mod.get_global_var('func_8089')
func_8090_call = mutated_mod.get_global_var('func_8090')
call_15932 = func_8089_call()
call_15933 = func_8089_call()
output = relay.Tuple([call_15928,call_15932,])
output2 = relay.Tuple([call_15929,call_15933,])
func_15953 = relay.Function([], output)
mod['func_15953'] = func_15953
mod = relay.transform.InferType()(mod)
output = func_15953()
func_15954 = relay.Function([], output)
mutated_mod['func_15954'] = func_15954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12479_call = mod.get_global_var('func_12479')
func_12481_call = mutated_mod.get_global_var('func_12481')
call_15981 = relay.TupleGetItem(func_12479_call(), 0)
call_15982 = relay.TupleGetItem(func_12481_call(), 0)
output = relay.Tuple([call_15981,])
output2 = relay.Tuple([call_15982,])
func_15987 = relay.Function([], output)
mod['func_15987'] = func_15987
mod = relay.transform.InferType()(mod)
output = func_15987()
func_15988 = relay.Function([], output)
mutated_mod['func_15988'] = func_15988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7325_call = mod.get_global_var('func_7325')
func_7327_call = mutated_mod.get_global_var('func_7327')
call_16026 = relay.TupleGetItem(func_7325_call(), 1)
call_16027 = relay.TupleGetItem(func_7327_call(), 1)
output = call_16026
output2 = call_16027
func_16059 = relay.Function([], output)
mod['func_16059'] = func_16059
mod = relay.transform.InferType()(mod)
output = func_16059()
func_16060 = relay.Function([], output)
mutated_mod['func_16060'] = func_16060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14375_call = mod.get_global_var('func_14375')
func_14377_call = mutated_mod.get_global_var('func_14377')
call_16085 = relay.TupleGetItem(func_14375_call(), 0)
call_16086 = relay.TupleGetItem(func_14377_call(), 0)
output = call_16085
output2 = call_16086
func_16127 = relay.Function([], output)
mod['func_16127'] = func_16127
mod = relay.transform.InferType()(mod)
mutated_mod['func_16127'] = func_16127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16127_call = mutated_mod.get_global_var('func_16127')
call_16128 = func_16127_call()
output = call_16128
func_16129 = relay.Function([], output)
mutated_mod['func_16129'] = func_16129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11473_call = mod.get_global_var('func_11473')
func_11475_call = mutated_mod.get_global_var('func_11475')
call_16204 = relay.TupleGetItem(func_11473_call(), 0)
call_16205 = relay.TupleGetItem(func_11475_call(), 0)
func_14192_call = mod.get_global_var('func_14192')
func_14194_call = mutated_mod.get_global_var('func_14194')
call_16222 = relay.TupleGetItem(func_14192_call(), 0)
call_16223 = relay.TupleGetItem(func_14194_call(), 0)
output = relay.Tuple([call_16204,call_16222,])
output2 = relay.Tuple([call_16205,call_16223,])
func_16232 = relay.Function([], output)
mod['func_16232'] = func_16232
mod = relay.transform.InferType()(mod)
output = func_16232()
func_16233 = relay.Function([], output)
mutated_mod['func_16233'] = func_16233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10338_call = mod.get_global_var('func_10338')
func_10339_call = mutated_mod.get_global_var('func_10339')
call_16243 = relay.TupleGetItem(func_10338_call(), 0)
call_16244 = relay.TupleGetItem(func_10339_call(), 0)
output = relay.Tuple([call_16243,])
output2 = relay.Tuple([call_16244,])
func_16257 = relay.Function([], output)
mod['func_16257'] = func_16257
mod = relay.transform.InferType()(mod)
mutated_mod['func_16257'] = func_16257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16257_call = mutated_mod.get_global_var('func_16257')
call_16258 = func_16257_call()
output = call_16258
func_16259 = relay.Function([], output)
mutated_mod['func_16259'] = func_16259
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16278 = relay.var("var_16278", dtype = "float32", shape = (15, 3, 7))#candidate|16278|(15, 3, 7)|var|float32
var_16279 = relay.var("var_16279", dtype = "float32", shape = (15, 3, 7))#candidate|16279|(15, 3, 7)|var|float32
bop_16280 = relay.floor_divide(var_16278.astype('float32'), relay.reshape(var_16279.astype('float32'), relay.shape_of(var_16278))) # shape=(15, 3, 7)
func_15163_call = mod.get_global_var('func_15163')
func_15165_call = mutated_mod.get_global_var('func_15165')
call_16290 = relay.TupleGetItem(func_15163_call(), 0)
call_16291 = relay.TupleGetItem(func_15165_call(), 0)
uop_16295 = relay.log(bop_16280.astype('float64')) # shape=(15, 3, 7)
output = relay.Tuple([call_16290,uop_16295,])
output2 = relay.Tuple([call_16291,uop_16295,])
func_16301 = relay.Function([var_16278,var_16279,], output)
mod['func_16301'] = func_16301
mod = relay.transform.InferType()(mod)
var_16302 = relay.var("var_16302", dtype = "float32", shape = (15, 3, 7))#candidate|16302|(15, 3, 7)|var|float32
var_16303 = relay.var("var_16303", dtype = "float32", shape = (15, 3, 7))#candidate|16303|(15, 3, 7)|var|float32
output = func_16301(var_16302,var_16303,)
func_16304 = relay.Function([var_16302,var_16303,], output)
mutated_mod['func_16304'] = func_16304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14375_call = mod.get_global_var('func_14375')
func_14377_call = mutated_mod.get_global_var('func_14377')
call_16345 = relay.TupleGetItem(func_14375_call(), 0)
call_16346 = relay.TupleGetItem(func_14377_call(), 0)
func_8947_call = mod.get_global_var('func_8947')
func_8949_call = mutated_mod.get_global_var('func_8949')
call_16370 = relay.TupleGetItem(func_8947_call(), 0)
call_16371 = relay.TupleGetItem(func_8949_call(), 0)
output = relay.Tuple([call_16345,call_16370,])
output2 = relay.Tuple([call_16346,call_16371,])
func_16378 = relay.Function([], output)
mod['func_16378'] = func_16378
mod = relay.transform.InferType()(mod)
output = func_16378()
func_16379 = relay.Function([], output)
mutated_mod['func_16379'] = func_16379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15253_call = mod.get_global_var('func_15253')
func_15255_call = mutated_mod.get_global_var('func_15255')
call_16444 = func_15253_call()
call_16445 = func_15253_call()
func_15524_call = mod.get_global_var('func_15524')
func_15525_call = mutated_mod.get_global_var('func_15525')
call_16462 = relay.TupleGetItem(func_15524_call(), 0)
call_16463 = relay.TupleGetItem(func_15525_call(), 0)
output = relay.Tuple([call_16444,call_16462,])
output2 = relay.Tuple([call_16445,call_16463,])
func_16476 = relay.Function([], output)
mod['func_16476'] = func_16476
mod = relay.transform.InferType()(mod)
mutated_mod['func_16476'] = func_16476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16476_call = mutated_mod.get_global_var('func_16476')
call_16477 = func_16476_call()
output = call_16477
func_16478 = relay.Function([], output)
mutated_mod['func_16478'] = func_16478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11569_call = mod.get_global_var('func_11569')
func_11570_call = mutated_mod.get_global_var('func_11570')
call_16517 = relay.TupleGetItem(func_11569_call(), 0)
call_16518 = relay.TupleGetItem(func_11570_call(), 0)
func_2982_call = mod.get_global_var('func_2982')
func_2988_call = mutated_mod.get_global_var('func_2988')
const_16539 = relay.const([5.353886,3.274656,7.442182,-8.209450,-7.397705,7.481593,5.980943,0.568945,0.455821,5.038670,9.177985,7.444448,0.259508,-6.213538,6.548728,-7.973265,-0.589157,8.098449,-2.820750,5.691030,-6.162448,9.464141,-9.355145,-1.385036,6.178693,4.059719,3.617806,7.909405,-7.490578,9.626621,-0.678799,-6.953369,8.898336,-2.025048,-7.071540,0.856164], dtype = "float32")#candidate|16539|(36,)|const|float32
var_16540 = relay.var("var_16540", dtype = "bool", shape = (208,))#candidate|16540|(208,)|var|bool
var_16541 = relay.var("var_16541", dtype = "uint8", shape = (72,))#candidate|16541|(72,)|var|uint8
const_16542 = relay.const(9, dtype = "uint8")#candidate|16542|()|const|uint8
call_16538 = relay.TupleGetItem(func_2982_call(relay.reshape(const_16539.astype('float32'), [2, 9, 2]), relay.reshape(const_16539.astype('float32'), [2, 9, 2]), relay.reshape(var_16540.astype('bool'), [208,]), relay.reshape(var_16541.astype('uint8'), [36, 2]), relay.reshape(const_16542.astype('uint8'), []), ), 5)
call_16543 = relay.TupleGetItem(func_2988_call(relay.reshape(const_16539.astype('float32'), [2, 9, 2]), relay.reshape(const_16539.astype('float32'), [2, 9, 2]), relay.reshape(var_16540.astype('bool'), [208,]), relay.reshape(var_16541.astype('uint8'), [36, 2]), relay.reshape(const_16542.astype('uint8'), []), ), 5)
output = relay.Tuple([call_16517,call_16538,const_16539,var_16540,var_16541,const_16542,])
output2 = relay.Tuple([call_16518,call_16543,const_16539,var_16540,var_16541,const_16542,])
func_16553 = relay.Function([var_16540,var_16541,], output)
mod['func_16553'] = func_16553
mod = relay.transform.InferType()(mod)
mutated_mod['func_16553'] = func_16553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16553_call = mutated_mod.get_global_var('func_16553')
var_16555 = relay.var("var_16555", dtype = "bool", shape = (208,))#candidate|16555|(208,)|var|bool
var_16556 = relay.var("var_16556", dtype = "uint8", shape = (72,))#candidate|16556|(72,)|var|uint8
call_16554 = func_16553_call(var_16555,var_16556,)
output = call_16554
func_16557 = relay.Function([var_16555,var_16556,], output)
mutated_mod['func_16557'] = func_16557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16127_call = mod.get_global_var('func_16127')
func_16129_call = mutated_mod.get_global_var('func_16129')
call_16574 = func_16127_call()
call_16575 = func_16127_call()
func_14845_call = mod.get_global_var('func_14845')
func_14846_call = mutated_mod.get_global_var('func_14846')
call_16585 = func_14845_call()
call_16586 = func_14845_call()
func_5100_call = mod.get_global_var('func_5100')
func_5104_call = mutated_mod.get_global_var('func_5104')
const_16589 = relay.const([-0.594859,4.613440,7.530546,5.049679,4.982521,-6.863192,6.727548,2.308656,-8.638440,9.179001,8.192343,-7.144343,-5.590326,2.860618,-7.908824,8.078523,-9.065316,2.871712,-7.599654,-7.858102,-3.173119,-7.453360,-4.823873,-9.623972,5.938821,4.485774,-8.618220,8.519500,2.910897,-1.298373,5.486383,-8.338502,-4.581022,5.039431,-3.577724,9.007341,-1.324564,-1.699818,5.185096,6.943183,-7.634284,9.626048,-6.001168,6.779719,8.610268,-1.238286,-5.058154,-2.478901,-5.416758,3.525912,-8.507851,3.086383,-5.739412,0.134217,-9.583283,9.497531,4.546612,3.307176,3.642110,7.300786,-8.591621,7.696582,-6.963945,-8.006472,1.591839,4.632729,-0.995961,-4.493002,-9.808740,-7.686243,7.415211,3.482699,8.973890,-4.543992,-9.204884,8.505194,3.302441,0.508152,4.074514,3.516510,3.914731,-2.408900,2.994292,-7.964120,-0.119708,1.494721,-4.111064,1.517926,3.898223,-8.650368,1.359904,5.982089,-0.049322,9.833449,-3.563982,-8.764818,7.530470,0.087315,-9.843800,8.861858,-4.614946,-2.254940,9.928405,-7.911303,6.447999,-1.521554,5.601378,-3.180992,-8.179037,5.011600,-3.399628,-8.305420,-2.088319,-0.274742,-1.712808,1.247178,-4.370966,5.886385,7.870502,2.481467,2.414132,-1.806408,1.530713,-0.090405,-8.065878,-7.974975,-1.883945,-8.204037,-4.904558,0.541667,-8.293926,5.755443,-5.611300,2.946865,3.059901,-3.590409,-7.126389,4.218577,6.806864,-3.006028,1.736319,-5.179531,3.891718,-3.657853,-4.485718,-0.037255,-9.221612,0.487938,0.452965,4.962364], dtype = "float32")#candidate|16589|(150,)|const|float32
const_16590 = relay.const([2,4,2,2,-1,-6,-6,2,-2,-4,8,9,-8,-9,-10,6,-8,-1,2,4,6,10,10,5,5,-4,-1,-10,-2,6,1,4,-10,-10,8,8,2,7,-10,-4,2,-7,-9,-1,-7,-4,9,-8,1,-1,-9,-5,7,-3,-4,1,4,-10,4,-7,8,-9,-7,6,-4,9,8,-6,-5,1,7,7], dtype = "uint8")#candidate|16590|(72,)|const|uint8
const_16591 = relay.const([-4.005640,-8.647938,3.191663,2.998341,5.373255,-8.374071,5.172866,-2.795309,-1.369157,0.389562,4.442937,0.515637,-4.737501,9.671107,-4.316557,-0.543004,1.589002,6.320996,-3.225249,-3.630471,-1.089026,-8.080853,-8.866487,-0.917714,-1.728604,-4.878417,-5.198954,8.161856,-8.843707,-1.043285,0.601418,-6.970703,0.166489,6.855943,-7.126404,-0.855172,-9.398697,-7.725534,7.666267,0.531696,-5.266347,1.005224,0.299998,4.609067,1.200210,0.641294,-8.394776,4.514325,4.086894,0.135796,0.542080,6.978051,4.323242,-9.913124,-2.672500,-3.753399,0.824190,-9.588868,-2.164603,7.691137,7.420903,-5.686073,-3.922344,-0.202003,-1.173567,1.889776,2.080185,-2.759118,-1.736420,5.798084,-9.915674,5.961029,6.063750,7.578433,-9.888755,-1.442698,6.360540,8.747571,-0.420194,3.949010,-4.550352,-6.805939,3.931863,-8.827301,0.631273,7.594878,7.265536,-4.342227,-7.488002,9.263403,-9.851646,-5.367051,-2.201019,3.826552,4.714748,-3.738346,9.552901,9.996599,3.086722,-5.975141,3.172786,-2.104236,-8.290605,-3.994933,-9.519536,0.740093,8.605459,-8.148901,-4.781501,-7.589477,1.273454,3.115199,-4.298637,6.797235,-6.495547,-8.767405,2.032023,-6.472559,0.758292,-5.990220,-9.717751,-9.743210,-6.880956,-7.174033,-5.030781,-1.549155,1.364201,-4.781733,4.073560,5.603804,8.178189,6.539232,-8.761949,8.222062,-0.502691,-3.301620,6.874713,-0.489759,8.502499,-2.308636,-7.970067,5.958294,-8.539924,2.434693,-2.878967,5.269895,-2.355996,-2.717487,6.641439,7.634079,-4.137678,-4.299555,-8.491858,8.767016,8.721629,-7.880992,-6.523175,3.303621,9.760586,-2.173308,0.094558,-3.807566,4.972667,0.857698,-3.802690,-3.951222,-9.694533,-0.816446,-5.522182,-0.600013,-3.416238,8.972799,7.541012,6.491712,3.692035,-0.296967,-1.931270,-6.453042,6.901864,-9.428239,-7.639220,-8.141870,8.266937,-4.191617,-6.524423,-5.847969,6.007664,-2.421626,-5.112603,3.429563,0.957463,8.858236,-5.081188,6.932014,7.141924,5.457498,2.845791,-2.162666,0.086093,-3.998523,1.099340,-9.886208,-3.920227,1.356121,-1.942444,-7.964612,-8.686039,8.253858,3.812826,5.892459,-0.490994,8.962274,-5.608322,6.168005,-6.546947,-6.245475,-4.898148,-3.376696,8.624593,2.339514,-2.470992,9.249266,8.257678,-6.129837,-0.444391,9.143528,-5.355206,-6.026684,-5.230513,-5.254297,2.318707,9.138218,3.347563,-0.545207,9.571174,7.042692,8.658185,2.013768,3.641232,6.406482,2.213243,5.169629,5.879673,-2.047969,9.423389], dtype = "float32")#candidate|16591|(245,)|const|float32
call_16588 = relay.TupleGetItem(func_5100_call(relay.reshape(const_16589.astype('float32'), [1, 150]), relay.reshape(const_16590.astype('uint8'), [18, 4]), relay.reshape(const_16591.astype('float32'), [245,]), ), 6)
call_16592 = relay.TupleGetItem(func_5104_call(relay.reshape(const_16589.astype('float32'), [1, 150]), relay.reshape(const_16590.astype('uint8'), [18, 4]), relay.reshape(const_16591.astype('float32'), [245,]), ), 6)
bop_16593 = relay.multiply(call_16574.astype('int16'), call_16588.astype('int16')) # shape=(10, 15, 300)
bop_16596 = relay.multiply(call_16575.astype('int16'), call_16592.astype('int16')) # shape=(10, 15, 300)
uop_16597 = relay.rsqrt(bop_16593.astype('float64')) # shape=(10, 15, 300)
uop_16599 = relay.rsqrt(bop_16596.astype('float64')) # shape=(10, 15, 300)
output = relay.Tuple([call_16585,const_16589,const_16590,const_16591,uop_16597,])
output2 = relay.Tuple([call_16586,const_16589,const_16590,const_16591,uop_16599,])
func_16601 = relay.Function([], output)
mod['func_16601'] = func_16601
mod = relay.transform.InferType()(mod)
mutated_mod['func_16601'] = func_16601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16601_call = mutated_mod.get_global_var('func_16601')
call_16602 = func_16601_call()
output = call_16602
func_16603 = relay.Function([], output)
mutated_mod['func_16603'] = func_16603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13277_call = mod.get_global_var('func_13277')
func_13279_call = mutated_mod.get_global_var('func_13279')
call_16607 = relay.TupleGetItem(func_13277_call(), 2)
call_16608 = relay.TupleGetItem(func_13279_call(), 2)
output = call_16607
output2 = call_16608
func_16630 = relay.Function([], output)
mod['func_16630'] = func_16630
mod = relay.transform.InferType()(mod)
output = func_16630()
func_16631 = relay.Function([], output)
mutated_mod['func_16631'] = func_16631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16059_call = mod.get_global_var('func_16059')
func_16060_call = mutated_mod.get_global_var('func_16060')
call_16644 = func_16059_call()
call_16645 = func_16059_call()
output = relay.Tuple([call_16644,])
output2 = relay.Tuple([call_16645,])
func_16681 = relay.Function([], output)
mod['func_16681'] = func_16681
mod = relay.transform.InferType()(mod)
mutated_mod['func_16681'] = func_16681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16681_call = mutated_mod.get_global_var('func_16681')
call_16682 = func_16681_call()
output = call_16682
func_16683 = relay.Function([], output)
mutated_mod['func_16683'] = func_16683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15511_call = mod.get_global_var('func_15511')
func_15513_call = mutated_mod.get_global_var('func_15513')
call_16729 = relay.TupleGetItem(func_15511_call(), 0)
call_16730 = relay.TupleGetItem(func_15513_call(), 0)
output = call_16729
output2 = call_16730
func_16733 = relay.Function([], output)
mod['func_16733'] = func_16733
mod = relay.transform.InferType()(mod)
mutated_mod['func_16733'] = func_16733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16733_call = mutated_mod.get_global_var('func_16733')
call_16734 = func_16733_call()
output = call_16734
func_16735 = relay.Function([], output)
mutated_mod['func_16735'] = func_16735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16059_call = mod.get_global_var('func_16059')
func_16060_call = mutated_mod.get_global_var('func_16060')
call_16765 = func_16059_call()
call_16766 = func_16059_call()
output = relay.Tuple([call_16765,])
output2 = relay.Tuple([call_16766,])
func_16778 = relay.Function([], output)
mod['func_16778'] = func_16778
mod = relay.transform.InferType()(mod)
mutated_mod['func_16778'] = func_16778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16778_call = mutated_mod.get_global_var('func_16778')
call_16779 = func_16778_call()
output = call_16779
func_16780 = relay.Function([], output)
mutated_mod['func_16780'] = func_16780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mod.get_global_var('func_9726')
func_9728_call = mutated_mod.get_global_var('func_9728')
call_16857 = relay.TupleGetItem(func_9726_call(), 0)
call_16858 = relay.TupleGetItem(func_9728_call(), 0)
output = relay.Tuple([call_16857,])
output2 = relay.Tuple([call_16858,])
func_16872 = relay.Function([], output)
mod['func_16872'] = func_16872
mod = relay.transform.InferType()(mod)
output = func_16872()
func_16873 = relay.Function([], output)
mutated_mod['func_16873'] = func_16873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14587_call = mod.get_global_var('func_14587')
func_14589_call = mutated_mod.get_global_var('func_14589')
call_16881 = relay.TupleGetItem(func_14587_call(), 0)
call_16882 = relay.TupleGetItem(func_14589_call(), 0)
func_12479_call = mod.get_global_var('func_12479')
func_12481_call = mutated_mod.get_global_var('func_12481')
call_16887 = relay.TupleGetItem(func_12479_call(), 0)
call_16888 = relay.TupleGetItem(func_12481_call(), 0)
func_11569_call = mod.get_global_var('func_11569')
func_11570_call = mutated_mod.get_global_var('func_11570')
call_16900 = relay.TupleGetItem(func_11569_call(), 1)
call_16901 = relay.TupleGetItem(func_11570_call(), 1)
func_14792_call = mod.get_global_var('func_14792')
func_14794_call = mutated_mod.get_global_var('func_14794')
var_16912 = relay.var("var_16912", dtype = "float64", shape = (100, 2))#candidate|16912|(100, 2)|var|float64
call_16911 = relay.TupleGetItem(func_14792_call(relay.reshape(var_16912.astype('float64'), [2, 10, 10])), 0)
call_16913 = relay.TupleGetItem(func_14794_call(relay.reshape(var_16912.astype('float64'), [2, 10, 10])), 0)
uop_16931 = relay.acos(call_16911.astype('float64')) # shape=(2, 10, 10)
uop_16933 = relay.acos(call_16913.astype('float64')) # shape=(2, 10, 10)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_16948 = func_7228_call()
call_16949 = func_7228_call()
bop_16950 = relay.multiply(uop_16931.astype('uint16'), relay.reshape(call_16911.astype('uint16'), relay.shape_of(uop_16931))) # shape=(2, 10, 10)
bop_16953 = relay.multiply(uop_16933.astype('uint16'), relay.reshape(call_16913.astype('uint16'), relay.shape_of(uop_16933))) # shape=(2, 10, 10)
func_7489_call = mod.get_global_var('func_7489')
func_7495_call = mutated_mod.get_global_var('func_7495')
var_16955 = relay.var("var_16955", dtype = "float32", shape = (36,))#candidate|16955|(36,)|var|float32
const_16956 = relay.const([5,10,6,4,3,4,-5,4,-10,-6,-9,10,-8,3,6,7,-2,5,-8,10,1,3,-8,3,-2,-4,9,-10,-10,-10,-1,-10,-3,-2,6,-4,7,-2,-2,4,-3,4,4,-10,9,1,-8,-2,7,-3,8,-9,-3,-10,7,1,-4,-3,-9,3,4,7,-6,-4,4,6,-7,7,-8,-6,-2,-7], dtype = "uint8")#candidate|16956|(72,)|const|uint8
var_16957 = relay.var("var_16957", dtype = "uint8", shape = ())#candidate|16957|()|var|uint8
const_16958 = relay.const([2,-9,10,6,8,8,-10,8,-2,-7,-3,-8,7,-8,6,10,-5,-8,2,8,-9,4,1,1,6,-6,4,-8,10,6,5,6,7,-5,-8,-3,-9,-6,-8,-6,6,3,-8,3,-9,5,-6,-4,-5,-6,-3,-9,7,-5,-4,-1,-4,2,-7,1,-5,2,9,8,6,-10,6,-3,7,-10,-8,-3,7,-4,4,2,6,-3,-9,-1,-7,-6,-2,-6,7,-10,-6,7,2,-10,9,-6,-6,-9,1,2,3,-3,-6,-4,6,8,-10,-7,-8,-9,-9,-1,-7,1,-4,-8,-2,-4,1,-1,-3,-10,6,5,4,-9,10,-7,-4,-5,-1,7,-5,2,-8,-2,4,4,-9,1,1,-6,4,8,-2,-6,7,6,4,-7,-1,-5,-2,6,-6,-5,-9,-9,-4,10,-1,9,-2,9,1,10,6,-10,2,2,-10,-6,7,1,2,7,10,1,-1,7,8,-5,-3,-5,-10,7,-3,1,8,-3,-5,-4,-8,-6,5,2,-3,10,-1,-4,-1,3,2,5,-5,-10,1,-7,1,8,9,1,-7,9,-3,1,4,7,-7,5,3,4,1,2,7,8,-2,-7,8,-10,-10,5,6,-7,-8,-7,-10,-4,-2,-1,-10,4,-5,-2,-8,-6,-3,10,6,-2,-2,5,10,2,-8,1,-3,-10,6,3,-4,2,-1,7,-2,10,-8,7,-4,9,4,-10,5,-7,-1,6,-1,-1,3,-8,6,10,-2,-9,-7,-8,8,-10,-5,-5,9,-2,-2,-1,-2,9,-6,2,-3,4,-1,1,-10,4,9,-4,1,-9,8,7,8,9,-2,-3,2,-4,-2,4,-7,-7,-6,-5,6,1,3,-5,-3,-6,-3,-9,-8,10,2,-2,-10,7,2,6,-7,2,-4,-2,9,-1,9,-9,-5,-9,-3,-7,-3,-1,-8,3,-4,7,1,-5,9,5,6,-9,5,1,10,-2,-4,-10,-10,10,-9,1,8,4,-4,9,5,2,-5,-9,-10,-10,4,9,-4,-9,5,4,-8,3,9,1,-10,-5,9,-2,5,-5,3,-6,-10,1,-4,3,5,-3,9,-8,10,-4,7,8,-9,4,5,-10,-2,-4,-7,-10,2,5,-9,10,6,8,3,7,9,5,-1,2,-7,-2,1,7,5,-7,-4,-4,3,6,-10,-8,-6,6,10,-3,-2,1,6,1,9,6,4,-6,3,-5,-4,-3,-7,-8,-7,-4,-7,-4,-3,6,2,-7,-3,-5,4,-1,-4,1,-5,8,1,3,-7,10,-4,3,-8,2,3,10,-9,8,-9,-7,-7,8,-7,5,-10,3,1,9,6,1,-1,7], dtype = "uint8")#candidate|16958|(500,)|const|uint8
call_16954 = relay.TupleGetItem(func_7489_call(relay.reshape(var_16955.astype('float32'), [36,]), relay.reshape(const_16956.astype('uint8'), [72,]), relay.reshape(var_16957.astype('uint8'), []), relay.reshape(const_16958.astype('uint8'), [10, 5, 10]), ), 5)
call_16959 = relay.TupleGetItem(func_7495_call(relay.reshape(var_16955.astype('float32'), [36,]), relay.reshape(const_16956.astype('uint8'), [72,]), relay.reshape(var_16957.astype('uint8'), []), relay.reshape(const_16958.astype('uint8'), [10, 5, 10]), ), 5)
uop_16964 = relay.cosh(bop_16950.astype('float32')) # shape=(2, 10, 10)
uop_16966 = relay.cosh(bop_16953.astype('float32')) # shape=(2, 10, 10)
output = relay.Tuple([call_16881,call_16887,call_16900,var_16912,call_16948,call_16954,var_16955,const_16956,var_16957,const_16958,uop_16964,])
output2 = relay.Tuple([call_16882,call_16888,call_16901,var_16912,call_16949,call_16959,var_16955,const_16956,var_16957,const_16958,uop_16966,])
func_16980 = relay.Function([var_16912,var_16955,var_16957,], output)
mod['func_16980'] = func_16980
mod = relay.transform.InferType()(mod)
var_16981 = relay.var("var_16981", dtype = "float64", shape = (100, 2))#candidate|16981|(100, 2)|var|float64
var_16982 = relay.var("var_16982", dtype = "float32", shape = (36,))#candidate|16982|(36,)|var|float32
var_16983 = relay.var("var_16983", dtype = "uint8", shape = ())#candidate|16983|()|var|uint8
output = func_16980(var_16981,var_16982,var_16983,)
func_16984 = relay.Function([var_16981,var_16982,var_16983,], output)
mutated_mod['func_16984'] = func_16984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9608_call = mod.get_global_var('func_9608')
func_9610_call = mutated_mod.get_global_var('func_9610')
call_16995 = func_9608_call()
call_16996 = func_9608_call()
output = relay.Tuple([call_16995,])
output2 = relay.Tuple([call_16996,])
func_17041 = relay.Function([], output)
mod['func_17041'] = func_17041
mod = relay.transform.InferType()(mod)
output = func_17041()
func_17042 = relay.Function([], output)
mutated_mod['func_17042'] = func_17042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16476_call = mod.get_global_var('func_16476')
func_16478_call = mutated_mod.get_global_var('func_16478')
call_17093 = relay.TupleGetItem(func_16476_call(), 1)
call_17094 = relay.TupleGetItem(func_16478_call(), 1)
output = relay.Tuple([call_17093,])
output2 = relay.Tuple([call_17094,])
func_17104 = relay.Function([], output)
mod['func_17104'] = func_17104
mod = relay.transform.InferType()(mod)
mutated_mod['func_17104'] = func_17104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17104_call = mutated_mod.get_global_var('func_17104')
call_17105 = func_17104_call()
output = call_17105
func_17106 = relay.Function([], output)
mutated_mod['func_17106'] = func_17106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10788_call = mod.get_global_var('func_10788')
func_10790_call = mutated_mod.get_global_var('func_10790')
call_17118 = relay.TupleGetItem(func_10788_call(), 0)
call_17119 = relay.TupleGetItem(func_10790_call(), 0)
output = call_17118
output2 = call_17119
func_17123 = relay.Function([], output)
mod['func_17123'] = func_17123
mod = relay.transform.InferType()(mod)
mutated_mod['func_17123'] = func_17123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17123_call = mutated_mod.get_global_var('func_17123')
call_17124 = func_17123_call()
output = call_17124
func_17125 = relay.Function([], output)
mutated_mod['func_17125'] = func_17125
mutated_mod = relay.transform.InferType()(mutated_mod)
const_17161 = relay.const(4.455382, dtype = "float32")#candidate|17161|()|const|float32
var_17162 = relay.var("var_17162", dtype = "float32", shape = (14, 7, 4))#candidate|17162|(14, 7, 4)|var|float32
bop_17163 = relay.subtract(const_17161.astype('float32'), var_17162.astype('float32')) # shape=(14, 7, 4)
func_7579_call = mod.get_global_var('func_7579')
func_7585_call = mutated_mod.get_global_var('func_7585')
const_17169 = relay.const([[True,True],[True,True],[True,True],[True,True],[True,False],[True,False],[False,True],[True,True],[True,True],[True,False],[True,False],[False,False],[False,True],[True,False],[True,True],[False,True],[False,False],[False,True],[True,False],[False,False],[False,False],[True,False],[True,False],[False,False],[False,True],[True,True],[True,True],[False,True],[False,True],[False,False],[False,False],[True,True],[False,True],[False,False],[True,True],[False,False],[True,True],[False,False],[False,False],[False,False],[False,True],[True,True],[True,True],[True,True],[True,True],[True,True],[True,False],[False,False],[False,True],[False,True],[False,False],[True,True],[False,False],[True,False],[False,True],[False,False],[True,True],[False,False],[True,True],[True,False],[False,True],[True,True],[True,False],[True,True],[True,True],[True,True],[False,False],[False,False],[False,True],[False,True],[False,False],[True,True],[True,True],[True,False],[False,True],[False,False],[False,False],[False,True],[False,True],[True,True],[True,False],[False,True],[False,False],[True,True],[True,True],[False,True],[True,True],[True,False],[True,False],[True,True],[True,True],[False,True],[True,False],[True,True],[True,False],[False,False],[False,False],[True,False],[False,False],[True,True],[True,True],[True,False],[True,False],[True,False]], dtype = "bool")#candidate|17169|(104, 2)|const|bool
const_17170 = relay.const([-0.895526,0.958154,-9.933333,-0.502346,-6.690425,-7.190289,-5.573986,2.868150,7.207194,-6.894468,3.455355,-5.760559,-0.840894,8.620698,-2.559393,-2.246797,-7.710768,9.452079,-2.253609,4.728579,-9.622612,-1.637879,6.622735,3.102486,-3.123192,-9.520586,3.797926,8.892550,-5.540204,-8.669034,4.366260,7.865835,-6.236566,9.357143,0.259324,2.089463,-3.628867,-3.973149,-7.172688,-2.841090,3.320453,-7.002723,5.801456,4.797122,2.430845,9.839359,-5.452771,-4.893953,3.521946,3.654817,-4.537763,-8.885721,-0.775897,-6.559005,0.817930,-1.528871,3.145365,3.335862,-2.204728,-3.380377,-7.456141,9.487610,3.037670,8.755595,8.131816,8.065056,-5.996495,-3.931658,-7.731796,7.120826,1.636627,8.529389,-9.030864,-8.433121,1.528081,-3.512526,-5.233373,-2.156144,1.456700,-0.283287,-3.201258,3.327930,6.938046,-5.812511,-6.469864,6.598632,5.482969,6.618116,-1.369273,-6.121012,-2.770608,8.410396,-1.750385,-0.177576,-9.538694,-8.062027,-3.828430,3.530562,4.315692,-6.241400,9.712551,-4.356258,-8.066822,-2.282879,3.604363,-6.074581,-1.968258,-6.865427,1.317673,-5.545625,3.723055,-4.652762,-2.534077,4.209582,9.840574,-7.509579,-0.935137,7.472878,-3.672800,2.635506,3.049862,1.726934,9.055283,-5.840745,9.279004,-9.128031,-8.729603,-4.538794,-4.850783,-3.447505,0.666896,-5.953028,2.703869,-4.390289,-8.559682,1.851742,3.813762,0.902480,-3.575383,5.623533,-6.389935,-9.916927,5.699758,-9.277618,7.683210,9.167193,9.131500,-0.993719,-0.270962,-4.377819,-7.654700,-1.974162,-5.778910,-2.960124,0.364358,-4.280642,-5.514972,-9.929761,-5.608918,1.339062,-7.430070,-3.412226,5.176449,-5.475338,-4.049074,-4.815782,4.368527,-1.306220,-6.210685,-8.703732,5.914697,0.069170,-8.448843,3.782104,-9.710060,-2.549444,8.326335,-4.195083,7.172376,-2.648104,3.666285,-1.076202,1.568568,3.113432,2.854944,-1.152485,-8.252378,-2.245051,6.473771,7.599615,2.273646,-2.272337,9.614211,1.208767,-2.064988,-5.292618,-0.363856,-4.993532,7.130606,9.854271,9.385914,2.395694,4.533688,-8.433609,2.547491,9.544660,1.014902,-8.925528,-7.291679,0.788057,0.212538,9.419414,-6.728125,-0.673531,6.717602,9.610493,0.722334,-7.347796,-0.266188,7.012012,1.089714,-4.903256,8.177327,9.825062,-6.922725,-2.717688,-8.352130,8.236707,8.768330,-9.204776,1.857449,5.523845,6.050250,-7.861126,4.075618,2.768461,-1.637813,3.601924,-6.650315,4.581073,-7.920157,5.996546,4.063533,0.787757,-9.068638,3.220452,7.245607,-0.961266,5.684195,8.174898,-5.181689,0.947179,-6.630342,-7.360517,6.616691,-4.207436,0.537574,-6.187547,-3.041071,7.135396,8.818487,5.365608,-4.913232,5.024136,-7.255974,-2.507990,-9.114133,6.823544,-3.952190,7.659355,1.333668,7.056313,4.045663,-1.570076,-6.494427,-3.382069,-0.212099,-7.649401,9.793981,-8.655104,-9.366698,3.732914,-0.283117,-2.807751,-3.483606,-5.471906,0.434504,4.165120,2.004600,-3.830158,6.389248,-8.632798,-5.324093,-2.334702,-8.752118,1.494869,3.929317,3.599840,6.851820,5.604974,-6.160242,-6.593060,3.340406,-8.624997,5.703205,-8.200863,-8.895900,-2.481248,-9.270479,-9.347661,-6.082883,8.522103,-2.861682,0.258029,-9.314200,-7.342740,9.868045,-1.880848,-3.779945,1.791732,-3.569544,-7.809741,-1.667660,3.156309,-4.725068,-7.709885,-9.763181,-0.796258,-3.241859,-6.980939,-4.409696,0.094474,6.172266,7.371483,6.449701,0.402300,-1.992064,-9.970674,8.257910,5.590594,9.618431,-3.576892,-8.940794,3.726577,-3.028930,4.804274,-4.946958,-5.349708,6.734222,9.650419,5.981354,-5.027609,-6.692521,-8.560976,-9.696835,1.042051,6.166197,0.256618,4.969582,4.791892,4.361572,-2.208594,6.981433,3.012459,-3.363833,4.585630,-8.948033,-5.045196,-1.008575,-3.393065,-4.204476,2.564001,9.757875,3.681040,5.228970,-8.634292,-9.771550,-8.722434,-8.188034,-1.621110,-5.136360,-8.128497,8.516412,4.837162,3.140343,-1.933979,-4.161134,-7.510897,1.020033,-0.349955,-3.002592,1.415641,8.666570,-1.455621,8.300201,5.273664,4.472808,-7.443741,-2.394402,-0.792089,7.315163,7.368661,-3.878676,3.689150,-2.005784,-2.504892,6.730367,0.496741,6.694469,-8.730593,-0.592425,-8.916513,8.364434,-9.897275,2.015251,8.405746,5.756468,-4.710776,-9.981606,6.555912,2.929107,9.216741,8.548368,8.029980,8.129156,-1.084295,0.129453,8.746261,0.217529,-3.977445,-9.779433,-9.898510,4.901464,-5.662959,-0.786951,-6.747188,3.159659,-9.164387,-7.985523,-3.342646,2.893272,6.866015,9.801816,1.618938,-2.736550,9.092700,-2.949999,-2.870785,-6.899945,9.862019,0.046514,-3.089129,-0.814201,1.545348,1.921074,-9.580573,-3.557432,3.798044,-4.670746,0.784032,0.328495,6.708280,-1.552291,2.149086,-9.083932,8.447645,-9.181821,4.752130,4.593683,0.192915,-7.595568,6.068670,2.851436,-4.201306,-3.063333,-9.428472,4.618931,3.490682,3.889244,-2.916404,0.516279,2.643333,-6.476682,-8.440039,-3.132999,-0.429534,7.371547,1.847684,-3.247856,-7.389027,9.090197,-6.813794,9.880802,-9.458641,-1.846598,-3.570319,6.965197,6.991659,-8.650243,5.778323,3.407846,7.026283,4.277653,5.124349,7.944445,-7.383183,-6.578323,6.915707,-9.214036,1.787559,-2.892815,8.231658,4.590012,7.735596,-7.535000,-1.731140,-9.475012,7.999222,5.130171,-4.405282,-2.117209,9.161498,8.836026,-2.511242,7.522660,3.921502,-5.940448,0.232821,0.279769,7.424456,4.373543,-4.509650,-1.968770,1.378087,-9.636374,-9.932493,8.029872,-4.620515,-5.693018,-1.661440,-0.896919,8.289367,-3.245575,-0.915652,-4.027374,-2.372903,-4.298061,0.169211,-5.759118,-4.763953,-0.508840,5.913852,-1.903543,6.194176,7.622849,-9.221682,4.275858,-8.362512,-3.188912,6.225148,-1.017211,-9.383450,-4.393225,1.183154,8.673541,-3.939122,-1.037604,4.220797,7.668517,8.248967,-8.658037,-3.291922,-6.347428,-8.374367,5.176542,1.188816,9.255795,-5.770920,2.570822,-7.791498,0.011341,1.094802,-5.459371,3.982030,8.738202,-0.881573,-5.248704,5.370521,4.028510,-9.846088,8.737519,1.977839,7.167367,3.313939,1.462513,2.956391,-5.833897,3.434382,3.887112,-3.486490], dtype = "float32")#candidate|17170|(600,)|const|float32
const_17171 = relay.const([-3,2,-2,5,3,-7,3,6,-7,4,-6,1,-3,3,9,3,-5,-2,-9,6,-8,3,-8,-7,-9,3,1,1,9,8,-3,2,6,-5,-10,1,6,1,6,-1,8,10,-7,5,-4,6,4,7,9,-8,-5,-8,4,6,-9,3,-8,7,6,3,-5,-9,-6,-8,8,-5,5,-3,5,9,4,-1,8,2,-10,-4,-4,3,-9,5,6,-10,5,2,-3,-2,-4,1,-1,-6,8,9,2,3,4,9,-10,-3,-10,-3,-5,-2,-1,10,8,4,-5,9,4,9,2,8,-4,-4,-7,1,-5,-2,8,8,-8,-5,7,10,-5,-9,-8,-8,-9,9,3,-9,-5,-5,-3,-10,-9,-3,8,-10,-4,-2,8,-7,2,5,7,4,-5,4,5,-8,-8,1,-6,-9,-9,-5,10,-6,-9,10,6,-6,4,-8,4,3,9,-8,-4,9,9,-2,7,3,-10,-10,10,7,9,-5,1,5,-2,7,1,1,10,-10,5,1,-8,-4,-10,-2,-6,2,-5,-9,3,4,2,3,-3,8,-6,-5,-3,-5,-10,2,4,-5,-4,-7,-2,8,-10,-3,5,3,2,8,-7,-8,9,-2,5,-3,4,3,-3,-10,-5,-8,-6,-4,6,-2,4,-9,10,-8,-3,-4,-3,4,2,-10,7,-9,-6,-1,-4,9,-5,-3,-2,-1,-3,3,-6,3,1,6,1,10,6,-2,-6,-8,-9,-7,-1,-7,5,-2,7,8,-9,5,-8,7,-10,-6,-10,-9,-5,-4,-5,3,-1,9,-10,-7,1,-7,8,-7], dtype = "uint16")#candidate|17171|(300,)|const|uint16
const_17172 = relay.const([False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,False], dtype = "bool")#candidate|17172|(624,)|const|bool
const_17173 = relay.const([9.776012,2.463953,-7.417096,-7.788773,3.078727,1.424681,-4.884954,-1.015838,1.161732,-5.672971,0.871203,-2.475784,-3.927623,-3.541604,-3.821696,4.250186,9.063351,-4.076430,3.731200,-2.570350,4.916318,5.475748,0.239230,6.640903,0.554658,6.472602,4.038078,-6.615981,-2.391973,7.017020,5.491505,-6.262408,-7.174241,4.938037,-3.744773,-1.766292,2.335383,0.151890,3.484782,1.987797,-3.328701,4.264818,-3.951303,7.649965,2.349313,-0.708861,-7.529541,3.413660,3.725652,-0.673225,-9.966034,-8.429477,7.389477,-6.060153,-8.822335,0.229444,6.079918,-7.369528,-6.808657,-3.255839,-9.446086,2.133625,2.837418,7.324281,7.500530,-4.473542,7.707044,7.648316,-9.906466,2.482588,-0.515760,-0.566503,-2.105154,9.496844,-0.492519,-8.253936,-1.510123,5.387635,-7.020219,9.730355,0.030820,-4.315067,-6.373226,3.576748,6.964569,2.734189,1.201801,5.177641,-6.293051,-9.931441,-4.161232,5.288460,-5.363306,5.926311,-8.457986,-1.081438,-2.368317,-1.183546,6.513895,-0.795748,-3.963029,-1.342787,1.768122,0.431751,-7.277357,-1.235058,-9.703751,-8.725348,5.739447,-0.110287,-1.826041,9.549777,8.193394,5.796330,5.123587,7.498094,4.826639,3.985665,-7.085774,-3.893726,-4.527377,5.224572,-1.274084,-4.315168,6.215946,9.644118,8.263635,3.454006,-2.269657,5.685707,-0.993901,-3.945750,-1.713243,-7.364869,-7.862746,-6.550167,2.816784,-7.936695,0.239703,3.797524,3.437239,-2.911365,7.380892,0.779166,-3.889936,7.257395,5.346821,-1.948158,6.614632,-1.697730,6.495974,5.046117,5.033004,-2.702756,-5.207345,0.664521,6.840352,-6.680013,2.925857,-6.178244,8.551693,-5.753715,7.852283,-0.553338,1.990240,3.083427,3.723826,-0.877536,-6.077242,5.778074,-2.973631,-9.268297,-7.877885,8.629751,-0.543657,4.207141,4.664826,-7.575285,-5.999950,-3.596161,-4.584444,-2.766458,-2.308207,-0.285359,-6.108164,5.548609,-1.816574,-9.945332,-1.117733,2.976614,0.224615,-1.516180,-7.446863,-9.680515,-7.764364,0.600773,-1.751006,-4.205571,-1.377236,1.611469,5.575066,9.355773,-5.519852,-4.275765,2.281951,4.790152,1.856081,-7.396948,-2.792188,-1.035060,0.896948,2.406615,-2.362612,-6.394115,-6.424122,6.441742,-3.135005,-3.892281,-2.698878,4.484692,-2.077291,-2.497174,1.845194,3.934162,6.159074,-9.062485,5.677847,-7.348261,9.915779,-8.203735,-7.145101,1.365759,5.099877,4.714432,5.939566,5.673343,0.026278,2.539728,-5.250376,2.638188,-7.054269,-4.537073,1.936341,5.001595,3.941615,2.192692,8.774331,-2.906519,-6.982159,-0.285867,4.686519,6.988654,-6.491063,8.034754,7.355964,-4.904795,-4.293729,-9.947387,-0.589010,-7.221837,0.893128,5.224513,3.770972,4.963042,-4.389647,1.386923,-4.395018,-5.745821,0.389601,0.308822,-3.085968,-1.227697,0.881752,3.867442,9.570389,8.766434,7.866678,1.889200,9.906778,-5.963312,3.594376,9.251088,-4.667081,-1.582978,7.897400,-4.639454,4.301427,-3.666118,9.788856,-2.311276,7.062746,-1.735257,2.335915,0.482576,-5.003613,-9.366065,6.473077,3.060901,7.927227,4.489091,-9.541088,8.755631,6.660586,-8.114486,8.021661,3.358400,-5.033870,4.484111,2.598028,-4.720479,-9.870521,0.198822,-6.737349,2.573614,-2.906507,-6.249985,-8.123904,1.284654,0.219811,2.306797,-7.053352,-9.377692,-2.498620,-9.093989,-1.044464,8.790895,3.914467,7.566566,-5.294629,-9.634849,2.444978,8.413069,-7.596380,8.900406,-1.400560,-4.741381,1.415202,7.904515,-3.926519,-2.670858,6.132934,7.946055,-5.698220,-3.883898,9.528953,-3.821333,-5.837615,-2.344832,-0.687776,-0.091844,-4.253391,9.018947,4.659113,7.442519,4.276089,2.138297,-9.610291,2.448182,5.310350,5.797668,-6.208668,5.822775,6.471386,4.036398,-5.807783,-4.274910,-4.630325,-6.691164,-0.966825,5.152385,7.000616,-4.503300,3.112726,2.962346,-5.011083,0.524978,-9.604124,2.045515,0.766501,2.046724,-8.082016,-0.524814,9.578928,5.091284,0.070896,1.958783,7.429786,-6.185493,-5.889488,2.751479,-0.587476,4.819195,3.892921,-5.536170,-0.277464,-2.500570,0.154701,9.434913,-7.901779,-0.426989,-5.670106,-3.258696,-6.172045,-8.675107,-5.504249,0.727726,6.159988,5.085368,2.814444,7.778874,7.210391,-8.649816,-1.351825,-3.881317,-6.505958,-4.871902,-0.687310,-7.407949,7.864789,2.263019,-5.759792,-2.226783,-6.593689,1.601088,5.453569,8.748215,-6.610850,1.400194,4.868102,0.415567,6.759368,-5.892648,8.580999,-3.225231,-2.169220,-3.948910,-1.709511,-1.826769,2.560242,-0.255755,-8.991711,6.684282,5.375137,6.290954,-5.910453,9.266513,0.416086,-8.779488,-7.241496,7.055773,-4.834073,-5.909927,3.747644,8.588808,-7.414944,6.654479,1.152715,7.752657,-4.208960,-1.730146,-7.212094,-5.507068,6.675363,-2.570230,3.708270,-1.610386,2.386350,-9.692813,8.010082,3.766804,8.354277,-0.921037,-7.121855,9.929499,4.033600,6.625181,0.830023,6.404635,-0.608799,1.923629,0.231292,-9.144740,-1.616200,5.911301,-6.117427,3.788393,-9.459415,6.091659,1.368586,7.015052,-3.558815,-4.771385,-6.448430,-3.707443,2.016083,-9.749237,-1.988239,-7.228105,0.829574,-7.994738,-9.381959,0.540148,-8.171965,4.885203,8.824658,-2.739484,-8.842070,-4.698473,-6.987974,7.674426,-0.527465,-2.240760,-9.305709,2.781703,6.879673,-8.479018,6.217194,-9.600126,-9.029582,3.846743,-9.931668,3.878030,9.930569,8.075408,-9.623243,2.465986,-8.324566,1.970219,-6.236471,-9.368551,3.890710,-3.059369,-4.822354,-4.024773,-0.222196,-9.189201,7.106699,0.481410,2.654459,-2.362038,-3.741131,-3.158504,6.265390,0.912441,-1.755035,4.549964,-4.706239,-2.283144,-0.541136,4.773806,1.842368,2.852511,1.216040,0.398716,2.319408,6.359103,0.844431,-9.123704,3.140306,4.991278,8.140617,0.317139,-3.746546,-0.876311,-8.167429,5.011009,-0.853815,-7.282512,-3.172470,-2.658414,1.651338,5.053847,-6.805416,-7.262312,5.344431,4.876033,-6.675475,7.657111,6.757231,-2.217456,4.723661,9.063926,-5.822810,-2.191794,8.511098,8.153110,-0.787081,2.988451,-4.324229,-8.137120,7.982799,3.909481,5.250246,-2.943875,-7.612188,-5.185661,2.272466,2.706487,-9.396863,-6.879048,1.885754,-5.016401,-6.751176,-9.241255,2.001910,-3.329249,-6.146236,9.032285,-0.236749,-9.776419,-7.077457,2.662263,-9.092152,7.771813,-8.986955,-6.289480,6.697478,2.577001,7.809831,7.638978,-7.681309,4.261383,6.442468,-6.600684,5.625530,-4.618913,-2.165975,3.862261,9.762839,3.838605,-0.623071,4.708007,-3.949541,1.291461,-9.701199,4.997183,-8.016663,3.196228,0.650596,-1.566881,4.486383,-1.059168,-9.090232,-0.836611,-6.383404,6.877189,-2.515875,3.371900,3.284396,-4.290018,3.464227,-6.390367,-2.725304,6.587001,-5.571011,-8.503448,-4.751126,0.142275,-8.894244,-5.579239,5.700626,8.886029,-5.864369,-4.328786,1.041848,8.190738,-6.715642,6.348023,-5.119351,-8.821383,-5.740826,-2.121437,6.932523,8.975130,9.003735,1.717807,8.655576,-9.280952,5.168844,9.744899,5.362615,1.573864,-4.468079,6.658112,3.152671,0.499432,-1.086856,-6.772783,9.185300,-6.421506,-7.447436,3.493832,-4.830155,9.450369,5.265423,1.622940,-6.860807,-2.397462,4.397682,0.618996,-8.183615,-3.108873,-0.647239,-4.586306,-4.495652,-9.426993,-9.125562,-8.663099,-8.840492,-0.031234,-0.541143,-2.155616,-8.431585,0.884838,-5.737497,-5.533578,-1.359445,-3.931736,-3.072240,-3.693756], dtype = "float32")#candidate|17173|(720,)|const|float32
call_17168 = relay.TupleGetItem(func_7579_call(relay.reshape(const_17169.astype('bool'), [208,]), relay.reshape(const_17170.astype('float32'), [2, 300]), relay.reshape(const_17171.astype('uint16'), [300,]), relay.reshape(const_17172.astype('bool'), [624,]), relay.reshape(const_17173.astype('float32'), [720,]), ), 4)
call_17174 = relay.TupleGetItem(func_7585_call(relay.reshape(const_17169.astype('bool'), [208,]), relay.reshape(const_17170.astype('float32'), [2, 300]), relay.reshape(const_17171.astype('uint16'), [300,]), relay.reshape(const_17172.astype('bool'), [624,]), relay.reshape(const_17173.astype('float32'), [720,]), ), 4)
func_2800_call = mod.get_global_var('func_2800')
func_2805_call = mutated_mod.get_global_var('func_2805')
const_17180 = relay.const([[-2.950427,4.968298,-9.406413,-1.102562,5.995478,2.376434,-9.622530,9.095830,7.187374,-4.684805,7.264482,-5.225041,4.195923,2.138513,4.152306,-4.704403,7.687647,-8.652802,-4.250712,9.235469,4.381548,7.204936,-2.925478,-0.156155,0.053354,-3.958044,-2.075006,8.673174,-3.304014,4.484440,-0.121489,6.310782,-2.509128,6.196110,-1.231471,-4.884665,-3.174970,-9.529736,7.129827,-3.050081,5.565827,0.298733,2.039535,5.083975,2.438895,0.247754,-1.767032,-5.510013,1.068763,7.366726,-6.929707,0.983894,3.641441,5.042965,-5.991780,-0.602688,-8.069608,-2.747672,-7.885954,-0.845780,-8.991261,-6.564642,-2.445716,0.218659,-9.076494,-7.971745,7.252592,8.217662,8.905294,3.065521,-6.292737,4.825101,9.942156,5.276912,7.387365,3.326344,2.726829,8.111003,-1.964704,5.863666,2.219090,9.893831,4.950755,-2.229213,6.103971,4.338131,6.837069,5.658379,-0.433432,-7.612922,-9.938252,9.649718,4.141082,2.501752,-1.289470,5.915984,-4.710302,-0.409007,8.934493,-3.939175,-3.349410,9.933510,-2.040911,-5.127491,8.405961,0.502480,-7.539459,7.524800,7.243736,-2.675553,-7.416050,2.647925,-8.971713,-3.737987,-0.960273,9.440325,-0.987250,-8.385665,0.074301,1.052796,-5.811538,-9.379142,-4.970258,-7.657402,-2.439384,9.385311,-3.814547,-6.765132,-5.740431,1.312001,9.987809,2.222256,5.029027,3.461648,-5.628509,5.722404,0.194831,7.791365,1.433133,9.827467,-7.715791,-6.953070,2.665676,-8.104266,-6.078742,1.188158,-1.537655,7.956147,-2.822142,-6.391349]], dtype = "float32")#candidate|17180|(1, 150)|const|float32
call_17179 = relay.TupleGetItem(func_2800_call(relay.reshape(const_17171.astype('uint16'), [15, 2, 10]), relay.reshape(const_17161.astype('uint8'), []), relay.reshape(const_17180.astype('float32'), [75, 2]), ), 3)
call_17181 = relay.TupleGetItem(func_2805_call(relay.reshape(const_17171.astype('uint16'), [15, 2, 10]), relay.reshape(const_17161.astype('uint8'), []), relay.reshape(const_17180.astype('float32'), [75, 2]), ), 3)
output = relay.Tuple([bop_17163,call_17168,const_17169,const_17170,const_17171,const_17172,const_17173,call_17179,const_17180,])
output2 = relay.Tuple([bop_17163,call_17174,const_17169,const_17170,const_17171,const_17172,const_17173,call_17181,const_17180,])
func_17182 = relay.Function([var_17162,], output)
mod['func_17182'] = func_17182
mod = relay.transform.InferType()(mod)
mutated_mod['func_17182'] = func_17182
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17183 = relay.var("var_17183", dtype = "float32", shape = (14, 7, 4))#candidate|17183|(14, 7, 4)|var|float32
func_17182_call = mutated_mod.get_global_var('func_17182')
call_17184 = func_17182_call(var_17183)
output = call_17184
func_17185 = relay.Function([var_17183], output)
mutated_mod['func_17185'] = func_17185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11888_call = mod.get_global_var('func_11888')
func_11890_call = mutated_mod.get_global_var('func_11890')
call_17268 = relay.TupleGetItem(func_11888_call(), 1)
call_17269 = relay.TupleGetItem(func_11890_call(), 1)
output = call_17268
output2 = call_17269
func_17286 = relay.Function([], output)
mod['func_17286'] = func_17286
mod = relay.transform.InferType()(mod)
mutated_mod['func_17286'] = func_17286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17286_call = mutated_mod.get_global_var('func_17286')
call_17287 = func_17286_call()
output = call_17287
func_17288 = relay.Function([], output)
mutated_mod['func_17288'] = func_17288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7230_call = mutated_mod.get_global_var('func_7230')
call_17299 = func_7228_call()
call_17300 = func_7228_call()
output = call_17299
output2 = call_17300
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
var_17321 = relay.var("var_17321", dtype = "int32", shape = ())#candidate|17321|()|var|int32
var_17322 = relay.var("var_17322", dtype = "int32", shape = (16, 7, 2))#candidate|17322|(16, 7, 2)|var|int32
bop_17323 = relay.multiply(var_17321.astype('int32'), var_17322.astype('int32')) # shape=(16, 7, 2)
func_10168_call = mod.get_global_var('func_10168')
func_10171_call = mutated_mod.get_global_var('func_10171')
call_17326 = func_10168_call(relay.reshape(var_17321.astype('float32'), []))
call_17327 = func_10168_call(relay.reshape(var_17321.astype('float32'), []))
uop_17346 = relay.sinh(var_17322.astype('float32')) # shape=(16, 7, 2)
output = relay.Tuple([bop_17323,call_17326,uop_17346,])
output2 = relay.Tuple([bop_17323,call_17327,uop_17346,])
func_17363 = relay.Function([var_17321,var_17322,], output)
mod['func_17363'] = func_17363
mod = relay.transform.InferType()(mod)
mutated_mod['func_17363'] = func_17363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17363_call = mutated_mod.get_global_var('func_17363')
var_17365 = relay.var("var_17365", dtype = "int32", shape = ())#candidate|17365|()|var|int32
var_17366 = relay.var("var_17366", dtype = "int32", shape = (16, 7, 2))#candidate|17366|(16, 7, 2)|var|int32
call_17364 = func_17363_call(var_17365,var_17366,)
output = call_17364
func_17367 = relay.Function([var_17365,var_17366,], output)
mutated_mod['func_17367'] = func_17367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9184_call = mod.get_global_var('func_9184')
func_9185_call = mutated_mod.get_global_var('func_9185')
call_17394 = relay.TupleGetItem(func_9184_call(), 0)
call_17395 = relay.TupleGetItem(func_9185_call(), 0)
func_9773_call = mod.get_global_var('func_9773')
func_9775_call = mutated_mod.get_global_var('func_9775')
call_17401 = func_9773_call()
call_17402 = func_9773_call()
output = relay.Tuple([call_17394,call_17401,])
output2 = relay.Tuple([call_17395,call_17402,])
func_17412 = relay.Function([], output)
mod['func_17412'] = func_17412
mod = relay.transform.InferType()(mod)
mutated_mod['func_17412'] = func_17412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17412_call = mutated_mod.get_global_var('func_17412')
call_17413 = func_17412_call()
output = call_17413
func_17414 = relay.Function([], output)
mutated_mod['func_17414'] = func_17414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16059_call = mod.get_global_var('func_16059')
func_16060_call = mutated_mod.get_global_var('func_16060')
call_17425 = func_16059_call()
call_17426 = func_16059_call()
output = relay.Tuple([call_17425,])
output2 = relay.Tuple([call_17426,])
func_17456 = relay.Function([], output)
mod['func_17456'] = func_17456
mod = relay.transform.InferType()(mod)
mutated_mod['func_17456'] = func_17456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17456_call = mutated_mod.get_global_var('func_17456')
call_17457 = func_17456_call()
output = call_17457
func_17458 = relay.Function([], output)
mutated_mod['func_17458'] = func_17458
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17461 = relay.var("var_17461", dtype = "float32", shape = (15, 16, 6))#candidate|17461|(15, 16, 6)|var|float32
uop_17462 = relay.sqrt(var_17461.astype('float32')) # shape=(15, 16, 6)
func_9469_call = mod.get_global_var('func_9469')
func_9472_call = mutated_mod.get_global_var('func_9472')
var_17469 = relay.var("var_17469", dtype = "float64", shape = (440,))#candidate|17469|(440,)|var|float64
const_17470 = relay.const(-6, dtype = "uint8")#candidate|17470|()|const|uint8
call_17468 = relay.TupleGetItem(func_9469_call(relay.reshape(var_17469.astype('float64'), [10, 44]), relay.reshape(const_17470.astype('uint8'), []), ), 0)
call_17471 = relay.TupleGetItem(func_9472_call(relay.reshape(var_17469.astype('float64'), [10, 44]), relay.reshape(const_17470.astype('uint8'), []), ), 0)
uop_17472 = relay.acos(uop_17462.astype('float32')) # shape=(15, 16, 6)
uop_17475 = relay.exp(uop_17472.astype('float64')) # shape=(15, 16, 6)
output = relay.Tuple([call_17468,var_17469,const_17470,uop_17475,])
output2 = relay.Tuple([call_17471,var_17469,const_17470,uop_17475,])
func_17480 = relay.Function([var_17461,var_17469,], output)
mod['func_17480'] = func_17480
mod = relay.transform.InferType()(mod)
var_17481 = relay.var("var_17481", dtype = "float32", shape = (15, 16, 6))#candidate|17481|(15, 16, 6)|var|float32
var_17482 = relay.var("var_17482", dtype = "float64", shape = (440,))#candidate|17482|(440,)|var|float64
output = func_17480(var_17481,var_17482,)
func_17483 = relay.Function([var_17481,var_17482,], output)
mutated_mod['func_17483'] = func_17483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16127_call = mod.get_global_var('func_16127')
func_16129_call = mutated_mod.get_global_var('func_16129')
call_17512 = func_16127_call()
call_17513 = func_16127_call()
func_6087_call = mod.get_global_var('func_6087')
func_6090_call = mutated_mod.get_global_var('func_6090')
const_17515 = relay.const([4.649359,-9.567486,-1.948485,5.876535,8.541804,8.098389,-4.239928,-5.662396,-8.280373,-3.043646,9.436010,-0.393748,6.402469,-9.013903,-0.839555,-9.154039,1.889078,3.705200,-1.005934,2.448987,6.014672,-5.658707,-5.512080,-8.929282,4.423045,-0.573061,-6.054748,8.241902,7.694273,-5.900889,-6.962411,5.881544,-5.444290,1.822641,2.106383,-8.458151,1.808095,-6.129539,-0.655552,-5.716030,1.467626,-9.794267,7.603019,7.105734,5.541239,-6.778627,1.685984,2.304074,-4.802816,-1.855660,1.742657,0.690466,5.639293,0.966128,-8.669727,1.469266,-6.964923,6.147312,9.301090,-0.630629,3.301124,-8.977847,-9.666935,-6.066346,-6.827663,-1.440999], dtype = "float32")#candidate|17515|(66,)|const|float32
call_17514 = relay.TupleGetItem(func_6087_call(relay.reshape(const_17515.astype('float32'), [1, 11, 6])), 0)
call_17516 = relay.TupleGetItem(func_6090_call(relay.reshape(const_17515.astype('float32'), [1, 11, 6])), 0)
bop_17565 = relay.maximum(call_17514.astype('uint16'), relay.reshape(const_17515.astype('uint16'), relay.shape_of(call_17514))) # shape=(1, 11, 6)
bop_17568 = relay.maximum(call_17516.astype('uint16'), relay.reshape(const_17515.astype('uint16'), relay.shape_of(call_17516))) # shape=(1, 11, 6)
func_9608_call = mod.get_global_var('func_9608')
func_9610_call = mutated_mod.get_global_var('func_9610')
call_17573 = func_9608_call()
call_17574 = func_9608_call()
bop_17581 = relay.bitwise_xor(call_17514.astype('uint64'), relay.reshape(const_17515.astype('uint64'), relay.shape_of(call_17514))) # shape=(1, 11, 6)
bop_17584 = relay.bitwise_xor(call_17516.astype('uint64'), relay.reshape(const_17515.astype('uint64'), relay.shape_of(call_17516))) # shape=(1, 11, 6)
output = relay.Tuple([call_17512,bop_17565,call_17573,bop_17581,])
output2 = relay.Tuple([call_17513,bop_17568,call_17574,bop_17584,])
func_17586 = relay.Function([], output)
mod['func_17586'] = func_17586
mod = relay.transform.InferType()(mod)
output = func_17586()
func_17587 = relay.Function([], output)
mutated_mod['func_17587'] = func_17587
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17608 = relay.var("var_17608", dtype = "int64", shape = (13, 11, 2))#candidate|17608|(13, 11, 2)|var|int64
var_17609 = relay.var("var_17609", dtype = "int64", shape = (13, 11, 2))#candidate|17609|(13, 11, 2)|var|int64
bop_17610 = relay.subtract(var_17608.astype('int64'), relay.reshape(var_17609.astype('int64'), relay.shape_of(var_17608))) # shape=(13, 11, 2)
func_10690_call = mod.get_global_var('func_10690')
func_10692_call = mutated_mod.get_global_var('func_10692')
call_17617 = relay.TupleGetItem(func_10690_call(), 1)
call_17618 = relay.TupleGetItem(func_10692_call(), 1)
output = relay.Tuple([bop_17610,call_17617,])
output2 = relay.Tuple([bop_17610,call_17618,])
func_17628 = relay.Function([var_17608,var_17609,], output)
mod['func_17628'] = func_17628
mod = relay.transform.InferType()(mod)
var_17629 = relay.var("var_17629", dtype = "int64", shape = (13, 11, 2))#candidate|17629|(13, 11, 2)|var|int64
var_17630 = relay.var("var_17630", dtype = "int64", shape = (13, 11, 2))#candidate|17630|(13, 11, 2)|var|int64
output = func_17628(var_17629,var_17630,)
func_17631 = relay.Function([var_17629,var_17630,], output)
mutated_mod['func_17631'] = func_17631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17456_call = mod.get_global_var('func_17456')
func_17458_call = mutated_mod.get_global_var('func_17458')
call_17633 = relay.TupleGetItem(func_17456_call(), 0)
call_17634 = relay.TupleGetItem(func_17458_call(), 0)
func_11701_call = mod.get_global_var('func_11701')
func_11703_call = mutated_mod.get_global_var('func_11703')
call_17642 = relay.TupleGetItem(func_11701_call(), 2)
call_17643 = relay.TupleGetItem(func_11703_call(), 2)
output = relay.Tuple([call_17633,call_17642,])
output2 = relay.Tuple([call_17634,call_17643,])
func_17650 = relay.Function([], output)
mod['func_17650'] = func_17650
mod = relay.transform.InferType()(mod)
mutated_mod['func_17650'] = func_17650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17650_call = mutated_mod.get_global_var('func_17650')
call_17651 = func_17650_call()
output = call_17651
func_17652 = relay.Function([], output)
mutated_mod['func_17652'] = func_17652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16059_call = mod.get_global_var('func_16059')
func_16060_call = mutated_mod.get_global_var('func_16060')
call_17738 = func_16059_call()
call_17739 = func_16059_call()
func_17412_call = mod.get_global_var('func_17412')
func_17414_call = mutated_mod.get_global_var('func_17414')
call_17746 = relay.TupleGetItem(func_17412_call(), 1)
call_17747 = relay.TupleGetItem(func_17414_call(), 1)
func_15919_call = mod.get_global_var('func_15919')
func_15921_call = mutated_mod.get_global_var('func_15921')
call_17754 = relay.TupleGetItem(func_15919_call(), 0)
call_17755 = relay.TupleGetItem(func_15921_call(), 0)
output = relay.Tuple([call_17738,call_17746,call_17754,])
output2 = relay.Tuple([call_17739,call_17747,call_17755,])
func_17758 = relay.Function([], output)
mod['func_17758'] = func_17758
mod = relay.transform.InferType()(mod)
output = func_17758()
func_17759 = relay.Function([], output)
mutated_mod['func_17759'] = func_17759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11367_call = mod.get_global_var('func_11367')
func_11368_call = mutated_mod.get_global_var('func_11368')
call_17774 = relay.TupleGetItem(func_11367_call(), 0)
call_17775 = relay.TupleGetItem(func_11368_call(), 0)
func_4176_call = mod.get_global_var('func_4176')
func_4179_call = mutated_mod.get_global_var('func_4179')
const_17778 = relay.const([False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,False], dtype = "bool")#candidate|17778|(208,)|const|bool
call_17777 = relay.TupleGetItem(func_4176_call(relay.reshape(const_17778.astype('bool'), [1, 208])), 2)
call_17779 = relay.TupleGetItem(func_4179_call(relay.reshape(const_17778.astype('bool'), [1, 208])), 2)
output = relay.Tuple([call_17774,call_17777,const_17778,])
output2 = relay.Tuple([call_17775,call_17779,const_17778,])
func_17796 = relay.Function([], output)
mod['func_17796'] = func_17796
mod = relay.transform.InferType()(mod)
output = func_17796()
func_17797 = relay.Function([], output)
mutated_mod['func_17797'] = func_17797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11888_call = mod.get_global_var('func_11888')
func_11890_call = mutated_mod.get_global_var('func_11890')
call_17798 = relay.TupleGetItem(func_11888_call(), 0)
call_17799 = relay.TupleGetItem(func_11890_call(), 0)
output = relay.Tuple([call_17798,])
output2 = relay.Tuple([call_17799,])
func_17813 = relay.Function([], output)
mod['func_17813'] = func_17813
mod = relay.transform.InferType()(mod)
output = func_17813()
func_17814 = relay.Function([], output)
mutated_mod['func_17814'] = func_17814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14874_call = mod.get_global_var('func_14874')
func_14875_call = mutated_mod.get_global_var('func_14875')
call_17818 = relay.TupleGetItem(func_14874_call(), 0)
call_17819 = relay.TupleGetItem(func_14875_call(), 0)
func_12394_call = mod.get_global_var('func_12394')
func_12397_call = mutated_mod.get_global_var('func_12397')
const_17838 = relay.const(True, dtype = "bool")#candidate|17838|()|const|bool
var_17839 = relay.var("var_17839", dtype = "bool", shape = (540,))#candidate|17839|(540,)|var|bool
call_17837 = relay.TupleGetItem(func_12394_call(relay.reshape(const_17838.astype('bool'), []), relay.reshape(var_17839.astype('bool'), [6, 10, 9]), ), 5)
call_17840 = relay.TupleGetItem(func_12397_call(relay.reshape(const_17838.astype('bool'), []), relay.reshape(var_17839.astype('bool'), [6, 10, 9]), ), 5)
func_5133_call = mod.get_global_var('func_5133')
func_5137_call = mutated_mod.get_global_var('func_5137')
const_17844 = relay.const([9,-1,-6,-1,9,-5,6,1,-8,7,3,8,-2,-7,1,8,5,-3,2,10,-1,-6,-4,6,-1,-2,6,-10,-8,-1,10,-1,9,-5,-9,-2,-1,-7,7,-5,-6,-3,-8,-9,7,-9,9,1,3,-1,-1,5,1,-5,5,7,8,2,-10,-6,2,5,5,-3,1,3,5,2,-9,-4,-8,6,10,5,10,8,-5,7,-10,10,-2,-3,-8,3,-3,-2,6,10,7,-6,5,10,9,-1,6,10,4,-5,10,2,4,6,-3,6,2,-6,7,8,-3,-7,-2,-9,4,-1,-3,-8,8,-7,-10,10,4,-8,1,-1,9,-5,6,-9,1,5,-2,3,8,-10,2,2,-5,-8,-8,-1,6,-10,-4,-5,9,-9,2,1,-1,-10,-1,8,3,-2,-5,-2,1,-7,10,-7,1,-10,-9,5,-3,10,9,10,6,-5,-7,5,-6,2,-4,5,-9,2,-7,6,4,-6,6,5,9,4,-6,3,-1,9,6,-3,-10,-10,2,9,-4,8,-10,-3,-2,5,5,-9,-3,-2,-4,-3,-7,-1,3,-4,-2,8,-5,1,9,5,-3,10,3,-6,-8,1,-6,-6,-2,-5,-5,8,-5,9,-6,9,9,7,5,10,4,9,-4,6,-7,2,-5,4,-3,5,-7,9,6,-9,9,4,-9,-3,8,-10,-4,9,-7,1,-5,-9,3,-8,4,-9,7,8,6,10,5,-1,6,-8,4,-3,6,-3,10,7,1,6,-9,3,-6,-7,4,-7,9,-5,5,-2,-10,9,6,-3,-1,-2,-1,-4,-9,5,-3,6,-8,-3,-9,-5,9,8,-9,2,-7,-2,1,-5,-1,6,3,-5,10,-3,4,9,-1,9,-9,-3,5,-7,3,7,-2,-7,-4,5,2,-5,7,10,-3,9,-9,-8,-10,-1,5,-7,2,2,-10,-1,5,9,-2,-10,-7,4,-3,-8,-7,6,-10,1,-10,-7,-9,3,6,6,10,-2,-8,10,-1,4,9,2,-6,-1,-5,7,1,-8,1,-7,-1,-7,-7,10,-7,-6,6,-6,-10,-1,7,8,9,5,1,2,-2,1,-5,-7,-7,9,-2,8,-3,-6,-6,-8,-2,6,6,-5,6,-6,-7,5,10,9,-10,4,7,-6,6,-9,-9,-2,-2,3,-1,1,6,5,-10,5,-3,-5,-3,-5,-7,9,-1,2,6,-3,8,8,-2,7,-7,-3,-5,5,1,7,6,5,7,-3,5,-9,-4,7,9,-5,10,9,6,3,3,5,-8,-1,10,-7,1,-9,2,-10,-4,7,5,-9,-1,-10,6,6,-8,8,-10,-2,-10,8,9,-3,3,6,8,-8,-10,3,-4,10,7,-9,-3,-10,3,5,7,2,-9,-7,6,8,-6,1,-2,-1,1,6,10,-8,-7,5,-2,2,-7,-10,6,6,9,-3,10,-9,-5,-6,-4,-8,-9,3,-1,-3,-7,1,9,7,-7,-8,-6,10,6,6,2,1,8,3,10,-10,-8,-2,8,-4,10,2,3,-7,1,8,-9,5,4,9,-1,-1,-7,6,4,10,6,-2,-7,-7,-2,2,-6,9,2,-4,-8,-3,-9,2,-3,-9,-8,9,8,4,2,3,10,10,1,-6,-10,-6,2,-6,10,-3,4,4,9,-4,-3,-1,-1,4,6,1,-10,8,-4,-6,-10,5,-2,-8,8,-2,-10,-1,-5,-3,6,10,10,8,2,10,-3,-6,5,-6,7,-1,2,-8,-8,9,-4,10,8,-9,1,2,4,9,-1,2,2,5,-7,10,-1,-9,-9,-10,-8,7,8,-3,7,-2,6,6,-7,-1,-1,10,-1,8,10,9,9,-7,-5,-1,-2,-1,-9,6,8,-2,8,1,-5,-9,1,4,4,-8,2,3,4,-2,-3,-3,-6,7,9,3,-1,10,10,1,-3,-7,10,-9], dtype = "int32")#candidate|17844|(728,)|const|int32
var_17845 = relay.var("var_17845", dtype = "float32", shape = (1, 150))#candidate|17845|(1, 150)|var|float32
call_17843 = relay.TupleGetItem(func_5133_call(relay.reshape(const_17844.astype('int32'), [4, 14, 13]), relay.reshape(var_17845.astype('float32'), [25, 6]), ), 2)
call_17846 = relay.TupleGetItem(func_5137_call(relay.reshape(const_17844.astype('int32'), [4, 14, 13]), relay.reshape(var_17845.astype('float32'), [25, 6]), ), 2)
output = relay.Tuple([call_17818,call_17837,const_17838,var_17839,call_17843,const_17844,var_17845,])
output2 = relay.Tuple([call_17819,call_17840,const_17838,var_17839,call_17846,const_17844,var_17845,])
func_17849 = relay.Function([var_17839,var_17845,], output)
mod['func_17849'] = func_17849
mod = relay.transform.InferType()(mod)
mutated_mod['func_17849'] = func_17849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17849_call = mutated_mod.get_global_var('func_17849')
var_17851 = relay.var("var_17851", dtype = "bool", shape = (540,))#candidate|17851|(540,)|var|bool
var_17852 = relay.var("var_17852", dtype = "float32", shape = (1, 150))#candidate|17852|(1, 150)|var|float32
call_17850 = func_17849_call(var_17851,var_17852,)
output = call_17850
func_17853 = relay.Function([var_17851,var_17852,], output)
mutated_mod['func_17853'] = func_17853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11287_call = mod.get_global_var('func_11287')
func_11289_call = mutated_mod.get_global_var('func_11289')
call_17873 = func_11287_call()
call_17874 = func_11287_call()
output = relay.Tuple([call_17873,])
output2 = relay.Tuple([call_17874,])
func_17924 = relay.Function([], output)
mod['func_17924'] = func_17924
mod = relay.transform.InferType()(mod)
output = func_17924()
func_17925 = relay.Function([], output)
mutated_mod['func_17925'] = func_17925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7729_call = mod.get_global_var('func_7729')
func_7730_call = mutated_mod.get_global_var('func_7730')
call_17933 = relay.TupleGetItem(func_7729_call(), 0)
call_17934 = relay.TupleGetItem(func_7730_call(), 0)
output = call_17933
output2 = call_17934
func_17955 = relay.Function([], output)
mod['func_17955'] = func_17955
mod = relay.transform.InferType()(mod)
output = func_17955()
func_17956 = relay.Function([], output)
mutated_mod['func_17956'] = func_17956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11614_call = mod.get_global_var('func_11614')
func_11615_call = mutated_mod.get_global_var('func_11615')
call_17964 = relay.TupleGetItem(func_11614_call(), 0)
call_17965 = relay.TupleGetItem(func_11615_call(), 0)
func_14908_call = mod.get_global_var('func_14908')
func_14911_call = mutated_mod.get_global_var('func_14911')
const_17970 = relay.const([-3.601754,8.181875,-9.554320,7.684040,3.591550,-8.252309,-1.599816,8.571669,-4.937886,7.788498,-5.616611,-7.483271,-7.551360,-7.331521,-6.094321,0.841221,-2.230593,-0.709508,6.923589,2.658945,-9.449095,5.786640,-5.792350,4.446678,2.097391,-0.362683,8.769692,-5.080584,5.969965,1.560349,8.876831,-1.500821,0.878916,-9.526321,5.834460,9.382738,-9.531917,-5.962788,1.069775,4.242159,-4.089595,2.129371,-0.719293,6.851844,-7.535539,9.473535,2.342781,1.137105,-2.129606,0.327944,-8.995062,3.960037,-8.540253,5.728226,0.788135,-2.735363,-3.171583,0.547208,-3.569834,-3.400365,0.448660,-1.399196,-4.523541,5.828598,0.942188,-6.390453,9.065805,-1.882415,9.164929,-4.395690,-5.741743,5.762938,-1.431718,1.207316,2.730559,4.209981,2.429187,-2.541767,-1.353733,4.856347,-8.935402,7.472849,2.406696,5.886807,6.092566,-1.086412,7.609807,-3.814285,-7.697606,-0.327819,7.666506,3.995135,3.895540,-1.716393,2.782353,6.483138,4.480193,-0.356797,8.452284,-1.936370,3.390447,-8.916471,-7.889109,-5.313377,1.404307,-8.446966,-6.451905,5.286414,5.761684,8.201301,7.160556,7.960140,7.232999,-2.699706,4.803483,5.364807,9.571820,2.588651,-1.547813,-9.980437], dtype = "float32")#candidate|17970|(120,)|const|float32
call_17969 = func_14908_call(relay.reshape(const_17970.astype('float32'), [4, 10, 3]))
call_17971 = func_14908_call(relay.reshape(const_17970.astype('float32'), [4, 10, 3]))
func_11122_call = mod.get_global_var('func_11122')
func_11126_call = mutated_mod.get_global_var('func_11126')
const_17982 = relay.const([8,-1,-9,3,-6,-7,-9,4,-6,-6,1,-1,10,10,-5,-3,6,-9,5,-1,8,-1,-1,-2,5,6,-2,4,-2,-8,-7,1,5,10,-1,-4,1,3,2,8,1,-5,3,-7,-6,-2,-5,6,-3,3,9,1,3,-1,1,-2,5,7,9,-3,-10,5,7], dtype = "uint32")#candidate|17982|(63,)|const|uint32
const_17983 = relay.const([-10,-4,-8,-7,2,7,1,-8,-9,6,-1,-2,-3,-6,10,2,2,7,4,-2,-5,-10,8,-3,-2,-4,8,-4,5,-5,1,-3,5,4,7,6,3,-10,-3,-10,2,10,2,-4,3,-1,7,9,7,1,-9,6,2,-7,-9,-10,4,4,5,2,5,4,9,-4,-9,10,2,2,-2,-7,-7,-5], dtype = "uint8")#candidate|17983|(72,)|const|uint8
var_17984 = relay.var("var_17984", dtype = "float32", shape = (150,))#candidate|17984|(150,)|var|float32
call_17981 = relay.TupleGetItem(func_11122_call(relay.reshape(const_17982.astype('uint32'), [63,]), relay.reshape(const_17983.astype('uint8'), [72,]), relay.reshape(var_17984.astype('float32'), [75, 2]), ), 0)
call_17985 = relay.TupleGetItem(func_11126_call(relay.reshape(const_17982.astype('uint32'), [63,]), relay.reshape(const_17983.astype('uint8'), [72,]), relay.reshape(var_17984.astype('float32'), [75, 2]), ), 0)
output = relay.Tuple([call_17964,call_17969,const_17970,call_17981,const_17982,const_17983,var_17984,])
output2 = relay.Tuple([call_17965,call_17971,const_17970,call_17985,const_17982,const_17983,var_17984,])
func_17987 = relay.Function([var_17984,], output)
mod['func_17987'] = func_17987
mod = relay.transform.InferType()(mod)
mutated_mod['func_17987'] = func_17987
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17988 = relay.var("var_17988", dtype = "float32", shape = (150,))#candidate|17988|(150,)|var|float32
func_17987_call = mutated_mod.get_global_var('func_17987')
call_17989 = func_17987_call(var_17988)
output = call_17989
func_17990 = relay.Function([var_17988], output)
mutated_mod['func_17990'] = func_17990
mutated_mod = relay.transform.InferType()(mutated_mod)
const_18051 = relay.const([[[3.050189,-5.368262,-2.935816,-5.348763,-4.300194,8.637817,-0.302149]],[[8.694397,4.523176,1.829617,-2.559133,7.503736,1.102876,6.029220]],[[-6.115443,-6.257651,6.859901,-2.472523,-1.713708,-1.270790,-7.180952]],[[-7.604468,-8.311813,-7.323458,-3.067340,1.733899,7.793201,-2.979154]],[[6.923193,6.102647,-4.765396,0.004965,-3.009009,4.088602,9.004152]],[[0.745692,1.949749,-0.328231,3.855777,-3.015277,-6.863786,-4.325138]],[[-1.330621,-4.858246,-9.962570,8.474468,8.942333,0.266486,-9.545741]],[[4.824879,-1.968152,-9.752873,-0.868012,2.347581,5.614724,8.238126]],[[7.721333,9.256861,1.391365,-6.392359,6.868709,-8.722590,-4.606688]],[[-8.515876,6.454452,-8.669710,-8.352294,5.684926,8.067322,-2.417052]],[[-6.150322,-6.814303,1.415636,-4.487221,6.420144,-1.195835,-2.002272]]], dtype = "float32")#candidate|18051|(11, 1, 7)|const|float32
uop_18052 = relay.asin(const_18051.astype('float32')) # shape=(11, 1, 7)
bop_18054 = relay.maximum(const_18051.astype('uint64'), relay.reshape(uop_18052.astype('uint64'), relay.shape_of(const_18051))) # shape=(11, 1, 7)
func_14908_call = mod.get_global_var('func_14908')
func_14911_call = mutated_mod.get_global_var('func_14911')
var_18062 = relay.var("var_18062", dtype = "float32", shape = (120,))#candidate|18062|(120,)|var|float32
call_18061 = func_14908_call(relay.reshape(var_18062.astype('float32'), [4, 10, 3]))
call_18063 = func_14908_call(relay.reshape(var_18062.astype('float32'), [4, 10, 3]))
output = relay.Tuple([bop_18054,call_18061,var_18062,])
output2 = relay.Tuple([bop_18054,call_18063,var_18062,])
func_18079 = relay.Function([var_18062,], output)
mod['func_18079'] = func_18079
mod = relay.transform.InferType()(mod)
mutated_mod['func_18079'] = func_18079
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18080 = relay.var("var_18080", dtype = "float32", shape = (120,))#candidate|18080|(120,)|var|float32
func_18079_call = mutated_mod.get_global_var('func_18079')
call_18081 = func_18079_call(var_18080)
output = call_18081
func_18082 = relay.Function([var_18080], output)
mutated_mod['func_18082'] = func_18082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16476_call = mod.get_global_var('func_16476')
func_16478_call = mutated_mod.get_global_var('func_16478')
call_18091 = relay.TupleGetItem(func_16476_call(), 1)
call_18092 = relay.TupleGetItem(func_16478_call(), 1)
output = relay.Tuple([call_18091,])
output2 = relay.Tuple([call_18092,])
func_18115 = relay.Function([], output)
mod['func_18115'] = func_18115
mod = relay.transform.InferType()(mod)
mutated_mod['func_18115'] = func_18115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18115_call = mutated_mod.get_global_var('func_18115')
call_18116 = func_18115_call()
output = call_18116
func_18117 = relay.Function([], output)
mutated_mod['func_18117'] = func_18117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14375_call = mod.get_global_var('func_14375')
func_14377_call = mutated_mod.get_global_var('func_14377')
call_18167 = relay.TupleGetItem(func_14375_call(), 0)
call_18168 = relay.TupleGetItem(func_14377_call(), 0)
func_13458_call = mod.get_global_var('func_13458')
func_13461_call = mutated_mod.get_global_var('func_13461')
const_18170 = relay.const([False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True], dtype = "bool")#candidate|18170|(208,)|const|bool
const_18171 = relay.const([-4.503542,2.891232,0.450957,9.215115,0.465413,-2.010824,-0.113603,8.197017,-6.989749,0.799533,-0.709895,7.045757,-8.851429,2.451158,1.637618,-1.670362,9.891207,2.680812,8.414328,6.451801,-1.885901,-3.567071,-1.825988,5.075625,-7.036523,5.349915,1.313190,-6.427222,-5.310221,3.014467,-3.990417,2.867785,2.720882,-0.826646,-0.146789,0.886945,9.716304,9.647883,-2.047770,-6.977701,2.559211,2.497716,4.219360,6.124579,3.404161,4.461031,-0.795491,8.964327,1.954577,-1.637938,-5.052694,-8.157967,7.529743,9.423660,8.011044,-1.650030,8.531463,7.532913,3.582879,4.907365,-3.908075,-1.657183,8.711336,-3.681414,7.531281,-3.661643,1.765708,-3.863255,-8.424236,-3.215220,4.727014,5.834363,-4.640053,7.709230,9.316783,1.451103,8.705667,-5.216493,1.909673,5.221298,1.969651,-2.359841,5.384169,1.648438,9.391640,3.163342,-0.459933,9.759636,9.009494,-4.611222,3.372096,-7.843011,-5.781191,-2.964491,-4.770439,-5.853405,4.648623,-3.085409,7.892371,3.360100,1.213466,-6.934855,8.314682,-2.136396,-6.950890,4.485068,-8.060736,0.093280,-5.964850,3.973180,7.759194,-2.927619,-9.531263,8.086341,-9.936983,-1.394413,3.077346,1.009725,1.195747,-0.042180,-2.744838,4.018744,3.184393,3.499659,-2.741757,-4.240025,0.222511,0.852565,1.957901,5.583336,9.293255,5.767335,-2.001241,0.569624,8.579176,-9.705118,8.476459,-2.930134,-6.760811,-9.411773,-4.724288,-5.931285,5.313324,-8.555039,3.790760,-2.537740,7.482213,9.613293,-3.452396,4.223448,-5.874793,0.009454,-8.292019,0.831863,-1.806682,8.315971,-0.651213,-3.749523,5.598958,4.062212,-8.237998,0.654268,3.614819,-3.479900,9.350253,9.542812,8.563542,0.066936,7.563428,-3.436755,-8.717022,-3.332439,3.205412,-6.851270,4.591600,9.388796,3.736418,-2.178922,-9.985285,-6.649520,-5.832780,8.646967,1.243972,2.733818,4.677352,-0.124022,-1.358866,8.863635,0.504066,-0.593473,0.305833,-1.661737,7.585908,5.719468,2.793532,6.620651,-8.878498,3.270270,-1.569093,-8.919181,-6.924542,9.960662,4.850109,8.979403,2.913618,-3.020955,6.017578,3.410331,7.251417,-6.957681,5.073919,-3.067147,2.211386,1.918340,2.117802,7.669614,-3.949354,-6.022367,9.067458,-8.349617,8.140502,5.716930,3.937635,2.763014,-5.500978,-3.498133,-4.012251,8.348687,-9.320613,2.520676,-6.973763,-0.143022,3.631353,-0.003103,-7.765366,0.088877,5.862619,-5.343336,-1.460386,9.025135,-2.395048,-4.439315,8.672391,-7.423269,-4.205734,5.496412,-7.704063,7.105676,-7.582354,1.286171,-9.271845,-2.035438,8.998951,-6.156232,2.430922,-8.225608,7.156166,-7.168026,-8.336956,6.116929,-6.198611,1.810098,-3.686664,-9.976573,0.983545,7.472991,0.320596,6.812276,-3.186706,-9.461308,-3.434339,7.611796,7.028015,-0.095340,-8.547413,-2.664431,-5.014819,-9.007060,-1.838451,9.970836,-4.367785,7.195074,-8.096144,-6.413990,-9.011461,-6.269078,-5.903289,7.841082,0.748061,7.035169,9.273258,-3.018536,-0.651116,-7.405510,-0.031885,-1.093334,-6.801571,-4.332619,-2.723766,1.635624,8.437654,9.317354,-1.512971,7.252809,-2.261096,2.001887,-6.140016,5.605989,-0.539481,7.106594,7.658385,1.699958,1.344041,0.440828,6.329595,-9.352422,-7.502868,-2.173678,-2.559877,5.168176,-9.846593,-4.451042,-8.869335,8.995195,8.367952,1.033673,-9.736103,-8.526321,-8.594854,-0.203750,1.279775,-5.641231,-5.437237,-7.706345,-8.499705,-9.167433,-1.632325,1.956429,-1.368706,-2.095297,8.872861,0.882561,-4.791118,2.142028,7.018709,-7.593907,9.870330,-4.041271,6.900878,-6.549440,-7.698455,8.169914,-0.733750,-7.185985,5.456585,-8.533407,-7.409908,9.036988,-9.868805,-1.772486,-5.793468,-2.889572,9.952449,8.998285,6.035221,8.258141,-0.677749,-3.577337,1.795150,-0.234245,8.547446,-2.674385,-1.007516,0.603903,-1.160412,-5.734893,-5.138562,-0.164539,0.293442,8.674690,-7.723141,8.692228,3.248879,8.598271,-3.395211,8.862265,-6.462779,5.410674,1.334435,3.842419,-3.881585,-1.961314,-4.193779,1.666883,3.314148,-6.890924,1.654416,-2.615880,-5.664894,0.077570,1.856501,-6.902532,-8.547083,-2.751453,-9.530367,-5.880954,8.691776,-3.887674,2.577920,-1.856246,-4.863956,-0.149009,-5.210864,-2.374365,-5.824685,7.589055,-6.118451,-8.030798,6.396403,4.572323,-8.513952,0.089116,-3.916828,-8.147060,3.034566,-1.581068,6.616405,1.595678,-3.219834,-2.265110,0.742221,-1.409284,-2.899766,6.839246,-8.561940,8.137232,-2.428675,-1.190652,-5.750798,-6.962557,9.774768,1.043460,-9.122209,-5.081601,-8.761058,3.288641,-5.153137,-0.189226,-7.742274,6.249762,-8.103546,-1.966666,2.929590,4.160849,2.184339,4.023795,7.234162,2.210107,4.832209,-2.760840,7.172050,1.773585,1.865434,-7.283219,3.128964,-1.093066,-9.289542,-6.652300,-2.241304,-2.009605,-5.585350,-6.564967,-9.258175,3.133090,-2.396217,-6.178547,5.309425,6.297847,0.065753,2.388272,2.869115,-5.855344,-9.940151,7.599312,-6.961573,-3.046406,7.977799,-3.202614,-3.768884,9.410585,1.766589,-0.888630,-7.242423,-2.067736,6.881701,-9.339134,7.211209,1.973238,-7.446643,-9.961107,-6.588873,5.168274,-9.257098,8.367480,5.772921,0.944169,-2.359440,2.723018,6.637847,-0.112820,7.986589,-9.154548,2.995520,-0.718709,-6.276068,9.266558,9.188777,5.817067,-8.339161,9.728268,3.955913,4.799995,-3.338681,-2.633663,-3.047882,1.867453,-9.886678,-5.299319,5.218820,8.569813,-3.126246,-9.940984,8.950793,3.195083,-6.802348,4.992667,7.046223,-0.270923,1.450537,4.440810,0.577973,-0.229754,-7.332827,-2.850835,9.967630,-9.950128,-9.903353,-4.623421,-6.052588,5.285769,-0.680148,-6.326319,5.173339,7.765210,-1.423609,-5.862019,8.332641,5.935906,-8.397551,4.965490,6.752045,7.270373,-8.286775,6.334181,5.758593,-1.025350,3.914142,4.861559,5.292816,1.677343,3.134150,7.079243,-0.894676,6.482182,-5.395141,2.705552,-5.665678,9.089027,-2.149426,9.202484,-6.695142,1.847996,-9.630816,-2.383487,6.025938,6.035818,-5.100833,-6.875225,4.407050,6.136828,-2.926574,8.830748,8.863628,-8.462767,9.912466,0.255767,9.951483,8.840296,9.621754,5.313165,-6.131688,1.111068,0.295003,0.652693,8.862286,5.218847,9.376874,-2.080937,5.393173,-2.049441,-1.219843,-8.915328,-9.958537,-3.128228,-5.752354,4.454766,-8.912441,5.992029,-8.204735,8.227316,7.175557,9.837347,3.593708,4.607939,-4.593605,-2.736706,4.177812,-1.100820,-3.500722,0.019887,-9.251058,3.306282,0.175633,9.742487,-2.224457,-3.501642,5.272826,-1.625688,6.502550,6.441622,-0.389565,8.389619,3.040075,6.961089,-6.796473,-7.077587,1.264494,9.954007,-0.093185,-8.983960,3.110518,-2.214527,5.855739,-6.206001,-9.392620,-1.707889,7.436033,-0.497634,-9.968320,-2.967846,-1.239013,6.751883,4.029710,-0.584125,8.936974,-1.794391,6.547556,3.632299,3.879943,-3.018350,-6.950383,-8.403016,-9.275554,-1.797693,5.655492,7.352751,9.493129,3.807233,0.491788,-9.168388,1.848980,-6.926792,4.000121,2.514812,7.427420,-6.697234,-0.068139,8.613282,3.794571,1.390393,-0.786685,-2.947830,-4.413160,-1.140416,4.758331,-3.375816,9.522475,-8.846645,1.511924,-6.812491,8.356400,-4.094083,7.971509,-1.887003,5.116122,6.111400,-2.049483,0.754650,-0.284576,-1.339956,-6.507149,-5.110062,1.096770,-5.383675,-8.638613,6.184703,6.638844,1.171352,9.538095,6.312996,-0.195525,2.379094,-1.683482,8.340989,-2.337594,-3.321674,-6.916560,1.642761,5.789774,-5.608229,-7.717489,4.170957,4.677816,-7.471742,-1.557159,4.687164,1.106907,2.615028,2.017368,-2.180517,5.245631,-7.472180,0.009711,6.746662,9.323542,-7.217821,-0.819220,1.908131,-8.672401,-7.412459,7.868255,1.329763,-1.656985,-4.869678,7.967136,-3.764009,-5.044665,6.574846,-0.510630,-9.391479,-0.626983,7.328282,1.104313,5.659708,-4.280139,-2.449841,9.441855,-6.832135,1.044675,-8.322501,4.723021,6.431497,5.754083,5.167510,1.166881,-1.290618,-8.464135,-0.264909,-1.477927,-9.635432,-7.212418,0.373671,-9.604274,3.366016,-4.318515,8.642631,-4.802594,7.060779,4.285486,1.883423,2.504527,-7.870760,6.280651,3.268938,-9.591966,5.246388,-6.377302,8.749991,-9.091631,-7.128951,-0.594448,9.328768,-7.278992,-7.291232,7.402282,7.986489,6.104083,3.437201,-2.141153,8.350866,-6.257048,3.865504,3.795811,4.017796,-9.600514,-7.587669,5.532458,7.968886,6.146354,4.599300,-3.633436,4.626255,1.221098,-6.097257,6.843440,-7.384599,-0.091819,-4.111578,-7.014379,-3.427821,-3.247629,1.543816,-0.623341,7.035083,3.157717,-1.702711,9.194798,1.728622,-1.878347,9.043148,2.022078,3.897621,9.492723,4.478457,-0.999462,-7.568838,6.621644,-3.982213,7.912129,4.161890,4.155045,-2.656900,4.356104,5.222995,6.066379,8.997524,-1.707080,2.503418,-2.965428,-8.180411,-6.613676,5.138140,-0.696603,4.810106,-1.397377,-9.210837,-9.713315,-0.057725,7.587305,-0.854539,-3.685643,7.317450,-0.644006,1.916821,-6.444642,9.319209,-9.976466,-2.977211,5.368140,-3.760908,-9.033900,4.293171,5.974546,-2.864870,2.077485,-1.965026,-3.452687,-9.269054,-1.566226,4.414534,2.758043,3.902635,-9.581444,5.513983,9.449579,1.886973,-0.696251,-1.962946,-3.542432,-2.790615,5.463692,-1.404200,7.292444,7.879904,-1.157739,-7.342419,7.471345,8.386757,9.950269,0.342630,4.324943,-4.477877,1.014085,0.965227,7.333587,3.093614,-0.433654,-5.826080,0.420562,4.757104,-4.385685,8.182048,5.621625,7.806875,2.659287,3.283259,1.765936,1.340553,1.950028,8.282295,-3.797613,0.939347,-3.701940,-5.684717,4.112868,5.851600,1.537506,-5.937859,9.549447,3.885141,-3.455905,5.518613,-7.793699,3.137270,-5.148174,-9.466021,9.106629,7.917353,2.549209,5.995902,-6.288348,9.681926,-8.953818,-9.950600,5.669950,-0.629028,9.125315,-5.452458,-9.018965,4.265770,-2.790231,-6.620689,6.289850,2.659412,3.071036,-8.038514,9.552807,-4.840332,5.784315,1.467708,-5.993061,-1.068948,-0.412258,-3.578480,-7.513031,4.549621,4.676593,1.848154,2.920085,-7.446589,4.792122,-3.821819,-9.741542,-1.672756,-4.757462,-1.459424,-0.132222,-5.200220,0.583063,7.231392,-3.101683,-7.902402,-3.893964,-0.970790,-7.362918,3.786620,2.766098,-1.769684,-0.206183,6.413403,8.000678,3.591173,2.448950,-5.597955,-2.153541,-5.320560,-9.461744,6.514390,-2.577202,-9.450383,-1.573385,4.686987,-9.663574,5.870294,-9.029683,7.513646,-3.912871,9.170716,-3.056693,3.434690,-3.300139,6.408253,-1.391002,2.766400,-6.669203,-0.425934,1.522848,2.632544,6.013111,-3.291344,2.611968,3.628640,1.234944,8.265957,-7.456342,-1.745487,9.741264,2.412028,-1.277697,-5.280376,6.433078,8.196221,-3.484720,-2.314914,6.410516,-6.937512,-6.265926,1.053494,-5.989671,2.613025,7.109093,1.077793,1.270063,-0.388832,-4.205442,-9.395477,1.638534,-6.369718,-5.406628,-4.170975,-2.784936,3.835072,-6.082017,-4.586041,1.257741,-9.130664,6.299878,7.485657,-0.631644,7.399534,9.730891,-5.871376,9.190305,-3.627248,8.799782,-4.532317,1.136376,-1.151922,-1.827563,2.173531,-5.558116,-3.520826,0.529857,-8.510711,5.988585,-6.421001,-6.061814,-3.843689,-6.952798,9.079603,7.418822,0.100802,9.935133,-8.471765,-8.789235,-2.129885,4.276169,-3.188108,-5.937225,8.472012,-8.721617,-5.206300,-5.752409,5.098988,-3.212741,5.166693,-6.517387,-9.622419,-4.843834,7.620882,-2.765538,-6.496850,-9.795945,6.323462,1.003074,-7.881782,-7.377253,-6.628179,6.228120,7.412974,0.012738,2.513097,1.258561,0.592876,2.912565,-9.429969,-0.454774,4.730998,-3.518873,-8.931489,1.320667,4.800227,6.802322,8.019917,2.456062,-2.712110,2.661821,-1.983752,-9.648783,-5.935265,-7.194405,8.001785,7.916186,8.163088,6.131009,-8.965748,8.742207,8.195898,8.163347,2.458323,4.905616,9.618560,-2.640783,-4.191644,-6.997943,-8.847063,8.407938,1.466346,-2.069183,-9.999826,-3.297851,9.621438,5.928532,8.615248,6.982563,0.348222,-3.837106,3.186117,3.903415,1.709660,-6.008144,-4.672599,-3.874981,9.652851,3.754542,-9.899296,-7.686024,6.606975,-2.591383,-2.332104,2.694275,4.867814,9.426695,-2.746175,-6.443649,-9.597008,4.454195,-4.144391,-2.200735,2.706723,-7.641261,-4.615008,0.645454,-6.955174,-8.709443,8.882890,-2.103821,9.810971,4.509881,-9.894647,-5.861960,-7.980617,-2.318749,1.895016,-8.593973,-4.254020,-2.237420,3.157059,-5.881821,-5.907055,8.515235,-8.752422,-1.554533,3.986078,-2.398949,2.539498,-7.223108,-1.651014,-1.277445,7.844613,-4.001776,7.735765,-1.175465,-5.045881,-1.538936,1.277746,-7.260308,-9.290318,-6.145005,-9.175705,3.157131,1.461069,-3.125804,-1.074284,7.842887,4.599437,4.556828,-1.682806,-7.707034,-4.858670,3.934235,-2.181981,-5.933139,-4.612935,-6.123265,2.625944,-3.914787,6.897989,-0.308685,-3.397479,5.393574,-8.673886,-5.206995,8.051392,8.874230,-8.971864,5.691750,8.713939,4.114126,-2.123152,-6.058259,9.061516,-8.152617,0.934799,1.034213,-7.123957,-4.385277,0.271696,-7.296874,8.921342,6.226824,-6.177703,-9.676098,-6.475387,-6.658945,6.824081,-6.654687,8.038731,8.740263,0.755939,-8.290093,5.807764,-5.485675,-2.503621,7.280293,9.893062,6.175498,-0.150491,6.737970,9.163694,4.010388,-8.821650,2.542759,0.894097,3.063440,3.715649,-5.156978,-9.763629,-5.306566,9.364580,-2.569302,-2.423391,0.416333,3.097708,5.373330,-5.719951,0.973032,-4.197797,-2.876548,1.672154,-6.932594,-2.891200,4.512488,-6.039873,9.185137,-9.346895,-0.620987,5.090592,5.548521,-5.302068,3.957804,1.075626,4.094672,4.411452,0.227390,1.487269,-1.770134,8.007991,-8.449751,2.426006,2.849904,3.542635,-6.720637,0.693099,1.304653,-7.511741,-2.012977,0.957320,2.700510,-6.314190,2.765319,-2.234094,8.807921,-6.551685,8.715121,0.439262,4.421854,-5.418847,5.735276,6.520055,2.323127,8.924609,5.103446,-1.115626,9.498484,-6.106151,-7.589449,-5.733815,-4.458832,-2.543099,-3.266624,-0.655296,-6.073893,4.533525,1.857933,3.509411,-8.953650,-6.845259,4.008994,-3.247129,0.853236,-0.862953,-8.968411,1.265624,0.530480,-8.334997,5.001338,7.873084,-1.636052,0.867048,0.524214,-5.347659,0.265632,1.754091,5.880401,-1.867187,-3.743654,3.363390,0.270130,2.833764,-2.794462,9.948308,1.025885,6.808652,2.619872,6.225485,9.136777,8.192646,-2.036384,-7.753349,-2.502178,1.121587,9.290193,8.793552,4.342763,6.148962,2.065372,-3.279754,3.386899,-1.113546,-2.382248,7.936310,9.596768,2.835603,3.718311,-0.290237,-1.801383,7.521511,-4.446307,-9.091285,5.567865,2.155385,-5.499536,9.983423,1.600186,5.229890,9.835225,-6.684390,9.342750,5.060269,4.645135,-3.668336,2.206571,3.627883,6.671698,1.867766,2.867502,6.931539,-7.869920,7.204063,-7.695195,-9.587904,0.497885,-3.599194,-7.576642,9.672178,1.750355,4.863309,3.776430,-8.071602,-4.824788,-1.096134,-1.551155,-3.877427,-1.334096,2.994360,-4.391564,5.294392,-1.825090,-1.418882,0.283527,-2.487799,4.867682,8.185956,-1.678487,4.096059,1.219032,-0.980423,4.985083,1.795786,-3.340815,-0.817116,-3.830129,-8.665338,-6.838214,9.412502,-9.169150,-6.358640,7.157951,4.754565,-1.915316,-2.747090,-1.892428,4.595843,1.126296,2.166415,9.410359,-8.338964,8.509657,-9.309399,7.769851,8.980924,1.780096,-4.128398,9.794915,-4.220783,-6.461586,-9.683038,2.903564,0.845770,-6.394380,-9.988476,-5.483181,5.603109,6.954351,3.778660,5.397058,8.703465,4.719822,2.789531,7.418134,-4.948555,-7.681070,-7.433907,-9.166751,4.530805,-1.830551,4.699522,-2.915780,8.225192,-2.195715,0.619551,3.677499,6.537787,-5.877805,-1.593773,-9.245345,8.053273,2.384364,7.422354,9.975269,-9.772868,-8.470519,7.195079,-9.387383,9.390384,1.131121,-2.836482,5.958163,0.726390,-1.567927,0.413029,-6.761577,1.144652,-5.131897,-4.712799,6.947213,1.265574,-7.973716,1.052287,1.590948,5.712420,9.042711,-0.839223,0.193051,-2.960432,8.016553,5.594409,-6.858927,2.954257,2.058011,5.037198,-8.310134,-7.226003,4.752301,4.704511,-2.593030,8.585919,-5.356253,-2.833732,-8.897505,3.739538,-6.997789,7.739545,0.237889,9.907854,-6.157863,-3.578644,-1.465889,8.943038,-4.090725,-1.629564,-1.105409,-9.112532,3.936184,-6.590116,6.531240,1.238431,-3.678899,-4.776396,2.426330,-5.796764,-3.545874,-3.903894,-3.678020,-3.497897,-2.353151,2.285276,7.321602,1.867050,4.708824,-5.134386,3.257660,-1.396218,-1.088733,-8.237846,8.334160,-2.792201,3.250083,-8.740583,-4.957832,-5.541149,6.288369,3.960805,4.395564,-5.709680,3.338052,3.107739,-1.858507,-1.118121,-8.641567,3.693071,-9.858485,-4.464466,-8.898926,4.977032,3.303729,-0.717516,3.404202,6.845449,-2.081688,7.269211,-5.471105,9.118016,2.817739,-8.094591,-4.979366,9.105734,5.317782,-4.329648,-2.810326,-6.528250,1.599286,-5.696036,8.228635,3.494854,4.446590,0.986091,3.234836,4.149177], dtype = "float32")#candidate|18171|(1650,)|const|float32
call_18169 = relay.TupleGetItem(func_13458_call(relay.reshape(const_18170.astype('bool'), [208,]), relay.reshape(const_18171.astype('float32'), [550, 3]), ), 0)
call_18172 = relay.TupleGetItem(func_13461_call(relay.reshape(const_18170.astype('bool'), [208,]), relay.reshape(const_18171.astype('float32'), [550, 3]), ), 0)
var_18186 = relay.var("var_18186", dtype = "bool", shape = (208,))#candidate|18186|(208,)|var|bool
bop_18187 = relay.mod(const_18170.astype('float64'), relay.reshape(var_18186.astype('float64'), relay.shape_of(const_18170))) # shape=(208,)
output = relay.Tuple([call_18167,call_18169,const_18171,bop_18187,])
output2 = relay.Tuple([call_18168,call_18172,const_18171,bop_18187,])
func_18190 = relay.Function([var_18186,], output)
mod['func_18190'] = func_18190
mod = relay.transform.InferType()(mod)
var_18191 = relay.var("var_18191", dtype = "bool", shape = (208,))#candidate|18191|(208,)|var|bool
output = func_18190(var_18191)
func_18192 = relay.Function([var_18191], output)
mutated_mod['func_18192'] = func_18192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17123_call = mod.get_global_var('func_17123')
func_17125_call = mutated_mod.get_global_var('func_17125')
call_18255 = func_17123_call()
call_18256 = func_17123_call()
output = relay.Tuple([call_18255,])
output2 = relay.Tuple([call_18256,])
func_18257 = relay.Function([], output)
mod['func_18257'] = func_18257
mod = relay.transform.InferType()(mod)
output = func_18257()
func_18258 = relay.Function([], output)
mutated_mod['func_18258'] = func_18258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12265_call = mod.get_global_var('func_12265')
func_12266_call = mutated_mod.get_global_var('func_12266')
call_18282 = func_12265_call()
call_18283 = func_12265_call()
output = call_18282
output2 = call_18283
func_18292 = relay.Function([], output)
mod['func_18292'] = func_18292
mod = relay.transform.InferType()(mod)
output = func_18292()
func_18293 = relay.Function([], output)
mutated_mod['func_18293'] = func_18293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11517_call = mod.get_global_var('func_11517')
func_11518_call = mutated_mod.get_global_var('func_11518')
call_18294 = func_11517_call()
call_18295 = func_11517_call()
func_10400_call = mod.get_global_var('func_10400')
func_10403_call = mutated_mod.get_global_var('func_10403')
var_18318 = relay.var("var_18318", dtype = "float32", shape = (1650,))#candidate|18318|(1650,)|var|float32
call_18317 = relay.TupleGetItem(func_10400_call(relay.reshape(var_18318.astype('float32'), [11, 150])), 0)
call_18319 = relay.TupleGetItem(func_10403_call(relay.reshape(var_18318.astype('float32'), [11, 150])), 0)
output = relay.Tuple([call_18294,call_18317,var_18318,])
output2 = relay.Tuple([call_18295,call_18319,var_18318,])
func_18336 = relay.Function([var_18318,], output)
mod['func_18336'] = func_18336
mod = relay.transform.InferType()(mod)
mutated_mod['func_18336'] = func_18336
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18337 = relay.var("var_18337", dtype = "float32", shape = (1650,))#candidate|18337|(1650,)|var|float32
func_18336_call = mutated_mod.get_global_var('func_18336')
call_18338 = func_18336_call(var_18337)
output = call_18338
func_18339 = relay.Function([var_18337], output)
mutated_mod['func_18339'] = func_18339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12479_call = mod.get_global_var('func_12479')
func_12481_call = mutated_mod.get_global_var('func_12481')
call_18346 = relay.TupleGetItem(func_12479_call(), 0)
call_18347 = relay.TupleGetItem(func_12481_call(), 0)
output = relay.Tuple([call_18346,])
output2 = relay.Tuple([call_18347,])
func_18352 = relay.Function([], output)
mod['func_18352'] = func_18352
mod = relay.transform.InferType()(mod)
output = func_18352()
func_18353 = relay.Function([], output)
mutated_mod['func_18353'] = func_18353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8065_call = mod.get_global_var('func_8065')
func_8067_call = mutated_mod.get_global_var('func_8067')
call_18354 = relay.TupleGetItem(func_8065_call(), 0)
call_18355 = relay.TupleGetItem(func_8067_call(), 0)
output = call_18354
output2 = call_18355
func_18385 = relay.Function([], output)
mod['func_18385'] = func_18385
mod = relay.transform.InferType()(mod)
mutated_mod['func_18385'] = func_18385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18385_call = mutated_mod.get_global_var('func_18385')
call_18386 = func_18385_call()
output = call_18386
func_18387 = relay.Function([], output)
mutated_mod['func_18387'] = func_18387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mod.get_global_var('func_9726')
func_9728_call = mutated_mod.get_global_var('func_9728')
call_18475 = relay.TupleGetItem(func_9726_call(), 0)
call_18476 = relay.TupleGetItem(func_9728_call(), 0)
output = relay.Tuple([call_18475,])
output2 = relay.Tuple([call_18476,])
func_18480 = relay.Function([], output)
mod['func_18480'] = func_18480
mod = relay.transform.InferType()(mod)
mutated_mod['func_18480'] = func_18480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18480_call = mutated_mod.get_global_var('func_18480')
call_18481 = func_18480_call()
output = call_18481
func_18482 = relay.Function([], output)
mutated_mod['func_18482'] = func_18482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10612_call = mod.get_global_var('func_10612')
func_10614_call = mutated_mod.get_global_var('func_10614')
call_18503 = relay.TupleGetItem(func_10612_call(), 0)
call_18504 = relay.TupleGetItem(func_10614_call(), 0)
func_9608_call = mod.get_global_var('func_9608')
func_9610_call = mutated_mod.get_global_var('func_9610')
call_18547 = func_9608_call()
call_18548 = func_9608_call()
output = relay.Tuple([call_18503,call_18547,])
output2 = relay.Tuple([call_18504,call_18548,])
func_18550 = relay.Function([], output)
mod['func_18550'] = func_18550
mod = relay.transform.InferType()(mod)
mutated_mod['func_18550'] = func_18550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18550_call = mutated_mod.get_global_var('func_18550')
call_18551 = func_18550_call()
output = call_18551
func_18552 = relay.Function([], output)
mutated_mod['func_18552'] = func_18552
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18619 = relay.var("var_18619", dtype = "float64", shape = (13, 12, 1))#candidate|18619|(13, 12, 1)|var|float64
uop_18620 = relay.sinh(var_18619.astype('float64')) # shape=(13, 12, 1)
output = relay.Tuple([uop_18620,])
output2 = relay.Tuple([uop_18620,])
func_18630 = relay.Function([var_18619,], output)
mod['func_18630'] = func_18630
mod = relay.transform.InferType()(mod)
var_18631 = relay.var("var_18631", dtype = "float64", shape = (13, 12, 1))#candidate|18631|(13, 12, 1)|var|float64
output = func_18630(var_18631)
func_18632 = relay.Function([var_18631], output)
mutated_mod['func_18632'] = func_18632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17412_call = mod.get_global_var('func_17412')
func_17414_call = mutated_mod.get_global_var('func_17414')
call_18636 = relay.TupleGetItem(func_17412_call(), 0)
call_18637 = relay.TupleGetItem(func_17414_call(), 0)
func_16059_call = mod.get_global_var('func_16059')
func_16060_call = mutated_mod.get_global_var('func_16060')
call_18643 = func_16059_call()
call_18644 = func_16059_call()
func_12095_call = mod.get_global_var('func_12095')
func_12097_call = mutated_mod.get_global_var('func_12097')
call_18648 = relay.TupleGetItem(func_12095_call(), 0)
call_18649 = relay.TupleGetItem(func_12097_call(), 0)
output = relay.Tuple([call_18636,call_18643,call_18648,])
output2 = relay.Tuple([call_18637,call_18644,call_18649,])
func_18657 = relay.Function([], output)
mod['func_18657'] = func_18657
mod = relay.transform.InferType()(mod)
mutated_mod['func_18657'] = func_18657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18657_call = mutated_mod.get_global_var('func_18657')
call_18658 = func_18657_call()
output = call_18658
func_18659 = relay.Function([], output)
mutated_mod['func_18659'] = func_18659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11569_call = mod.get_global_var('func_11569')
func_11570_call = mutated_mod.get_global_var('func_11570')
call_18700 = relay.TupleGetItem(func_11569_call(), 0)
call_18701 = relay.TupleGetItem(func_11570_call(), 0)
func_5100_call = mod.get_global_var('func_5100')
func_5104_call = mutated_mod.get_global_var('func_5104')
const_18714 = relay.const([[-7.193500,4.700577,-1.557918,-7.814958,6.318683,-5.764098,-9.534834,-4.743249,3.174034,9.789012,-4.139934,-6.388966,-9.375652,-5.221796,-1.254911,6.801180,-9.529546,-4.464442,-4.288302,-9.451491,5.363916,-9.608075,1.423664,-9.292909,-5.367146,8.999413,7.452191,2.689032,-7.241437,-9.307851],[1.569023,4.537981,-8.724940,-8.435351,-4.958063,1.056985,2.405070,-4.665944,-9.577271,7.227117,-9.786712,8.493780,-3.659044,2.132555,5.259611,-0.507177,8.231758,-5.710530,8.372647,-6.328942,-8.421566,5.006025,-7.889568,-2.397722,-3.810844,7.185503,8.521385,2.525558,5.136457,-0.660653],[-1.506103,-3.389012,-1.733830,-7.394828,0.484279,-9.101575,-6.882432,-2.175802,2.439989,8.504806,-4.318288,-9.652865,0.726912,-1.946670,7.302631,3.511632,0.514027,0.458154,4.685238,0.448641,2.266768,-3.314714,1.842670,-7.815547,8.035494,5.081970,-8.871764,8.981174,1.739324,9.728876],[-1.761379,-3.127059,-1.581605,-3.484102,6.555164,-3.511150,5.525350,-1.186268,0.986220,1.839482,-8.249382,4.509386,-2.556501,3.168698,-9.808364,-7.493042,1.302784,-2.262822,8.478753,8.328901,-8.453386,5.511111,-5.336702,-8.092907,-1.846713,0.934622,-5.626406,1.814179,8.433542,-9.169043],[8.219125,5.645604,-1.051534,-8.521889,-2.977134,-2.712126,-9.010146,-2.854692,-5.683569,-5.295842,-8.582180,3.895584,-6.492481,9.946481,4.871695,9.157901,8.399711,-6.241182,-9.275010,3.794604,-4.023714,6.413623,5.980391,-7.432544,8.994644,-0.019186,-5.623934,-0.741076,-7.601424,-0.774790]], dtype = "float32")#candidate|18714|(5, 30)|const|float32
var_18715 = relay.var("var_18715", dtype = "uint8", shape = (72,))#candidate|18715|(72,)|var|uint8
var_18716 = relay.var("var_18716", dtype = "float32", shape = (245,))#candidate|18716|(245,)|var|float32
call_18713 = relay.TupleGetItem(func_5100_call(relay.reshape(const_18714.astype('float32'), [1, 150]), relay.reshape(var_18715.astype('uint8'), [18, 4]), relay.reshape(var_18716.astype('float32'), [245,]), ), 0)
call_18717 = relay.TupleGetItem(func_5104_call(relay.reshape(const_18714.astype('float32'), [1, 150]), relay.reshape(var_18715.astype('uint8'), [18, 4]), relay.reshape(var_18716.astype('float32'), [245,]), ), 0)
func_18336_call = mod.get_global_var('func_18336')
func_18339_call = mutated_mod.get_global_var('func_18339')
const_18725 = relay.const([9.249525,-2.872162,-7.079958,-5.040818,4.249870,-6.309882,-0.797877,2.174442,-0.619010,-1.544474,2.657023,-7.545721,-8.994995,0.250637,-2.656573,-0.693577,-5.171815,-4.513895,2.334276,-0.734619,-0.853075,-3.388956,-9.999303,4.807392,7.477426,-7.556845,0.888315,-3.598621,2.673897,3.968304,-8.822855,7.408562,9.030565,-9.204828,0.724461,7.407948,7.114549,-2.795831,-6.398208,-2.415050,5.508574,-7.941411,-8.024756,-4.393177,-3.814480,9.387029,-6.054104,-2.842065,-7.703547,-3.323107,4.199348,9.447434,-6.163956,-5.734286,-0.248322,-0.386073,-2.311708,-7.020703,-4.330428,-0.564747,0.939190,9.912117,2.150176,6.806316,-0.279555,7.550539,1.993096,6.876928,-9.796168,-2.560599,-6.592549,-4.193487,0.482305,4.011931,-0.715495,0.578858,-4.428422,4.184468,-3.256735,2.028502,-7.183872,-8.479730,-4.749298,9.007800,6.927129,4.237753,3.417247,-8.673254,-1.408775,-3.286587,-4.145635,-1.505062,-2.191214,-8.008490,-9.153227,-2.157118,-8.237177,2.464021,-4.639539,1.890879,-9.013433,2.494422,-8.761184,3.837080,-8.395074,5.664712,2.475237,4.413828,6.888948,-7.346440,3.465060,2.547360,6.573500,-1.178823,0.890032,6.867165,-3.388277,3.190303,6.683107,-8.470204,-2.676920,-2.341029,7.617366,-0.903952,4.096366,3.472211,5.825628,-7.459329,2.026727,-5.010921,-4.968242,-8.886659,-6.148252,8.988272,-3.553402,2.721339,-7.393713,-6.521450,1.348647,-0.158423,6.851225,-2.925146,-4.719309,1.551715,3.138309,9.757581,-3.341603,2.671560,0.079776,-4.099820,-1.963424,1.030214,8.833313,-9.530914,-1.402655,2.300821,-7.320780,-6.362242,-5.474708,-5.931912,0.392325,3.303259,-1.138199,-0.195809,1.137950,9.530936,9.339297,-0.946067,0.491400,5.562207,-3.682059,1.910902,-1.025392,0.672434,-5.804289,7.845288,5.694983,4.139213,0.767317,-8.263432,-7.919206,-4.572124,-6.765473,-7.062628,5.341288,7.024830,-4.856901,1.988283,-4.300048,2.614359,-0.639600,-2.784766,0.146988,0.364234,6.038386,8.674751,-0.577833,3.438315,7.691803,-8.844922,-6.041267,-3.616774,-3.583508,2.558093,-1.481530,9.422492,4.418050,1.832635,2.306817,3.692316,-6.578381,-6.147731,-5.608792,2.347016,9.419557,9.631573,8.286878,-6.352451,3.313313,-0.739272,-7.344119,-7.062717,2.058165,-2.013572,5.850260,6.699414,9.240862,-0.382577,-8.802999,8.525614,5.888970,7.333233,-3.942543,-7.049665,8.300119,5.224772,3.428197,-0.551406,0.247292,4.763688,-7.459529,-6.849936,3.436133,-9.896461,-2.086432,0.670000,-1.093880,-0.285403,6.804299,-0.606966,6.652367,-9.027518,6.160995,5.882499,-4.906562,2.803342,-9.012313,-0.465534,-3.650555,7.678243,-1.437150,-5.320278,4.777600,3.479620,-7.543479,3.874184,4.669179,-2.745572,-7.580818,-2.788810,-2.251880,-5.391287,4.191776,-9.460740,6.729805,5.538996,2.825888,-1.961158,-9.969399,1.748921,6.453207,5.903297,-9.096591,4.660131,6.522109,4.700796,-8.460419,-2.410346,-5.162713,1.852823,-0.531113,3.438250,9.997033,-8.074381,7.971521,-7.467487,8.196390,-1.495219,9.284355,-5.951340,0.661745,-1.654867,9.416798,0.509966,-0.480562,7.300100,8.669325,-7.372370,-6.928457,8.560690,-6.716666,-7.434603,8.951965,1.027254,9.968349,1.086607,-8.146365,-8.610617,4.395579,2.489184,-7.509868,-5.975273,-4.814031,-0.274408,-4.279828,-3.872872,9.244185,-9.112071,9.685194,9.021804,1.019255,3.281945,8.329851,-0.337879,-2.911123,-6.947898,-8.790348,-1.759616,6.789040,-6.045610,-8.632538,-2.118245,9.176167,-8.753911,-4.305041,2.459172,7.851531,1.610538,-3.419488,2.505395,-4.482842,-1.235287,-4.742224,0.340745,7.364132,8.660811,-8.253416,-7.492148,-9.164735,8.081850,-7.866697,4.045544,7.040931,-5.214886,-1.390902,-6.781156,8.861649,8.318720,-1.466163,9.623300,-8.079446,2.845793,-8.985079,3.114648,9.596127,-3.820125,8.416068,1.818756,-9.877013,9.603248,3.031825,2.323159,-4.679199,-3.763517,1.031188,-9.320689,2.759894,9.007947,9.742791,-7.629833,8.252335,2.113473,-7.881956,5.945668,-8.144723,1.296999,4.715315,4.763044,-9.499921,-3.586258,8.855737,2.552851,-6.257752,1.785436,1.505739,-4.577322,-4.895224,-1.181755,-5.254986,8.524827,-4.116206,-7.306837,-9.502325,2.795177,-9.206400,-8.910170,-5.036417,-0.325354,-7.462162,3.982646,2.678280,-0.071713,3.242439,4.005232,3.337459,-1.657127,1.949620,8.832416,-5.696162,-9.736982,-4.153649,7.302575,5.114304,8.710229,1.713133,9.104157,9.527395,-5.492240,-7.213197,-8.112406,-4.544958,2.735207,-4.932359,3.914910,8.458217,9.432912,4.380612,7.852026,-3.976627,-3.699136,1.866956,-9.315819,-8.597624,2.862988,-3.496623,-0.323462,-7.872847,2.222253,-6.328776,-1.819619,-4.103296,7.320204,-7.522239,-7.869950,8.784750,-1.141835,1.566582,8.562002,1.924718,-6.864796,6.280916,-2.559014,7.548620,-6.097203,1.681923,7.361927,-7.515457,0.022188,1.123935,5.094444,-1.325165,4.340167,-0.096202,0.205263,8.770917,-6.932287,-4.743065,5.719269,-0.012931,7.933210,-9.166562,3.913969,2.934867,0.387577,9.502749,-5.921800,-0.044583,2.510649,-8.852301,-4.697963,-3.768777,-3.933936,8.544226,-0.825549,6.763435,6.480526,5.846078,-0.545743,1.345177,1.243851,-9.261582,0.138707,-1.328570,-2.040857,7.617126,-0.028017,3.396690,2.559292,-5.158733,-4.329937,5.052510,1.971767,-7.025386,-5.667354,8.708549,-5.790500,1.031930,-1.403989,-4.572364,-5.109115,2.794642,-0.404697,-5.363309,-2.975139,4.352515,-6.710249,-4.674646,1.964123,-1.975183,2.576558,-4.263446,9.545054,4.755631,9.452869,-7.307442,4.245308,-7.743838,-8.497930,4.935098,-7.214851,7.197971,-5.836572,-3.758094,7.694564,8.105662,5.625899,-7.345198,0.692751,-9.336286,-8.503462,-5.883265,0.940298,7.544059,0.160018,-4.679862,0.588308,4.063958,1.648959,-1.843063,-6.155149,4.404938,2.288497,-5.532569,5.453813,3.300341,-7.118723,-6.041551,-2.341444,7.331299,-0.895729,1.641777,-4.253207,3.412160,7.738515,-9.858949,8.855052,8.426683,7.548654,8.607853,-6.182294,-6.391812,0.546880,-9.736512,-4.826079,2.475336,1.068762,3.956892,8.838961,-4.736982,-1.506694,-0.689566,-6.153709,-5.291801,-5.822899,7.550698,-5.192993,5.998489,-7.154342,1.383383,9.003934,2.054915,-3.061926,-7.701879,-1.056757,-3.871480,1.927853,-6.463170,-9.676287,-1.808923,0.702915,0.354139,7.621003,2.216638,2.470938,4.342417,5.596715,5.775978,2.709339,-9.200609,-1.224433,-9.947520,7.581672,-1.372135,1.649684,-0.759944,-0.849687,-1.773516,-6.661052,7.400744,-6.693704,3.515482,3.725435,0.713071,-1.450609,-4.348578,-1.974978,1.220055,-9.635775,6.695503,-4.919243,-3.447697,-4.376442,-6.376976,-9.926356,-1.996869,-5.553472,-4.280093,-2.448421,-7.183835,1.960692,-4.693652,4.602004,-1.905558,0.762698,0.005912,3.466232,-5.563587,-5.761789,6.863534,-8.310724,-5.609744,1.137810,-8.296356,-2.445125,-4.726105,-8.917131,-7.735229,-0.490247,0.324621,-8.529949,6.543240,-1.625546,5.296182,9.673825,2.073830,-4.829781,-1.952393,-0.936602,-4.588928,-0.208672,5.024847,8.735497,-9.648226,-0.713919,0.717163,6.328047,-8.685936,-5.734509,-1.715181,-6.184499,4.394042,2.076743,-7.612577,-5.536158,0.732303,-9.153516,2.268173,-0.887982,8.156501,1.621376,7.195338,-4.461281,-2.000446,-6.056427,-0.827455,-3.585611,6.551870,9.806873,-6.280320,-6.548938,-6.184918,-6.952258,-3.802013,-5.263920,7.714680,-5.472977,-4.348443,-3.590628,0.452279,2.262977,-2.016536,1.606022,-3.477745,8.563605,0.177256,-9.828624,-0.472355,6.548937,4.715628,3.611893,-3.160223,6.527704,-6.005674,0.346849,-4.506440,5.061781,0.147632,3.576408,0.494319,-8.041489,-7.928799,8.127198,4.655126,-1.596126,-7.458577,4.407190,7.588001,6.019472,-9.676234,-9.973409,9.714284,0.910780,-7.747265,-0.442772,-8.110023,-4.564685,4.687415,6.251072,0.466397,9.243308,5.955216,-0.584736,-1.518590,-7.901144,-1.897388,7.532174,-3.360035,-5.715191,0.979782,5.733645,9.518377,0.506768,5.454004,8.584280,-9.534025,-5.091275,4.735452,-8.233638,-0.493800,1.386279,2.100003,-5.016089,6.569223,0.166287,-6.743716,-5.235950,-4.447322,-6.497970,8.010882,-1.102849,0.480335,3.920314,7.498184,-0.220853,6.842347,4.990575,-2.150151,-1.749908,-4.147337,6.640727,-5.209124,7.728107,8.429359,-1.479939,4.547654,-5.276954,2.054663,-8.636588,5.105947,-0.257983,-4.996792,-3.674407,-1.454007,-9.289586,-7.447460,0.024901,-9.117361,1.160912,-8.728641,-5.443300,1.065156,-6.844588,-2.170742,1.402142,7.656965,-1.558089,0.914804,4.829523,-3.675010,5.558318,1.986776,3.213524,1.844802,5.706326,0.799562,1.405545,-1.575416,2.088306,-3.713235,-0.908320,9.880921,9.559467,9.021943,-2.020362,3.638826,-2.698211,-3.721936,-4.489320,8.621040,5.913578,8.057922,0.183977,5.401016,-6.759886,4.318200,9.670372,-4.299047,-4.886869,6.012769,8.895741,-4.635540,4.023500,1.823229,-5.029160,9.003574,8.782685,-7.066475,-3.658311,-0.787432,-1.236129,-8.389927,-3.650664,-0.699272,-9.661191,4.669728,-0.779055,-6.744368,-0.055359,6.386255,-5.311722,-3.183076,0.695397,-1.624824,-5.216665,5.402531,-7.589295,5.320853,-8.398103,9.147807,3.270599,-8.150281,-9.739040,-0.532493,-7.564667,9.555108,-7.290431,9.698733,4.512191,-8.613556,-4.267905,-1.499124,9.875397,9.042558,7.616176,-4.802154,7.618690,8.522654,9.107044,-4.252148,2.835498,-8.396250,8.273727,-4.785206,4.755988,2.443909,-1.552620,2.423541,0.190056,4.320672,2.191319,6.467723,-0.361403,1.156801,-0.888825,8.547321,4.522009,-2.607333,0.672128,1.269334,4.170951,-1.000668,-8.560215,8.654714,-0.608673,2.650133,-5.676654,-5.510235,3.018109,9.537145,4.832346,5.971437,-2.021906,-6.207161,-6.498659,5.530282,-5.138460,2.547143,7.755126,-9.480497,8.165013,7.616571,-2.707465,-9.612903,9.204015,-4.417322,7.142232,-6.164161,7.117963,5.093065,-2.986158,0.530461,6.466555,-3.727561,4.807795,-3.808056,-7.480868,-1.791954,-7.956622,-2.305224,-6.515620,-6.289392,-6.775954,-0.300069,1.613933,-6.715167,-0.951025,-3.527494,-7.503034,-1.405204,5.302147,6.058834,-4.155354,2.049257,-7.527649,3.072459,-1.954983,-7.770317,-2.838832,-7.030009,8.220642,7.906608,-7.447969,0.888320,-5.401528,-9.394620,-3.608625,6.233423,5.131107,5.730114,-3.812626,5.489264,1.436752,-6.695480,-4.512624,0.544485,3.683028,9.498544,4.562572,-5.542578,-9.696819,1.687944,-5.621775,9.604653,0.978126,-2.774873,8.378050,-9.039741,7.198290,-1.112911,2.566326,3.579872,3.558262,-9.623233,7.058915,-0.745959,9.364075,5.887808,2.288702,-7.037037,0.145809,-2.686607,-8.007501,2.138955,0.860052,8.070393,-1.853599,4.643719,7.835233,-6.981096,3.576479,-7.735809,-7.643031,-4.010305,-0.774561,5.378723,3.318043,7.735091,-4.619963,-3.347535,-3.855936,1.139210,-7.819913,-5.791338,-2.659526,8.594988,-5.181880,2.093001,8.969868,-2.223709,-6.163608,1.537369,4.595960,0.453150,-0.825873,-0.221223,2.182577,5.334093,-5.889688,8.846828,-6.221824,-2.596446,-8.041267,4.707374,-1.365181,4.705889,4.698520,-8.597144,2.016234,6.344928,1.225972,9.537709,1.270681,4.992443,-8.828314,-7.698027,3.468105,8.469562,-7.901143,4.064168,-5.182091,9.761821,2.556249,8.122438,5.591818,-6.157040,-1.796526,9.863346,-0.730973,3.549562,4.826305,0.810938,3.952126,-5.713463,-3.231506,-8.309267,0.015278,-0.104538,5.950562,3.609160,-2.146273,-6.428569,4.890969,-8.201345,-7.737625,7.447086,-9.235163,-9.039182,5.323047,0.849081,-8.831808,1.723334,-4.584794,-3.488765,9.443111,-1.328651,-8.965732,-8.751080,1.096879,3.375199,-3.805929,0.070279,-1.049242,-4.873461,2.142784,5.550853,3.727458,8.807801,-0.312742,-0.421670,8.435636,-6.470928,9.488955,-1.042682,5.884705,-1.702676,-5.022267,-3.922317,2.576443,-8.420622,7.654502,-3.421508,-7.130223,-2.225459,8.588371,-0.539928,9.029825,-3.481090,7.364090,3.182712,8.659226,4.174860,-8.828605,-2.151459,-7.271653,-5.365565,-7.062107,6.399289,-5.301698,1.316977,-5.125795,-3.397480,-4.890171,-2.582614,6.088683,8.229004,4.573661,-7.126342,-4.026747,7.736029,-2.467467,-1.963505,-9.955243,7.046556,0.670051,-5.250553,3.098867,-3.541256,-7.633126,7.271944,-9.688916,-5.978768,8.278070,3.593320,9.340095,8.796879,-7.573452,-5.424623,1.533458,9.764222,-8.717094,-2.437002,8.128951,-0.534028,6.681268,9.198095,-1.244531,4.256612,4.758587,4.913822,7.823212,-5.231584,2.364119,-6.403809,-3.043062,9.576887,9.509956,-6.594640,-9.119925,-1.065646,6.578825,-3.402440,6.918424,2.942880,-8.483833,1.635349,2.057409,-5.551312,-2.153391,7.045255,-2.940673,-6.097053,-6.694767,-5.357324,1.315075,-7.371458,2.971079,-6.622814,-4.880000,3.566073,-7.717363,-0.120688,-8.165689,-5.772281,6.882832,7.753977,6.179901,-3.063656,6.080008,-8.506642,0.388178,6.862018,4.110029,-2.479798,4.118879,1.160251,-7.016156,-1.906591,-8.668878,-4.703855,-9.740820,3.711344,6.481539,-1.900482,1.162914,0.325015,6.671815,5.958346,-6.969476,3.452853,4.211631,7.011841,-4.990691,-2.363497,5.643046,9.034926,-8.617110,0.564936,-3.696104,-2.666766,-2.158881,-7.331857,-6.065514,1.261290,2.334796,5.771033,9.906511,4.538000,-3.732639,-6.192020,-4.736125,3.685221,-6.197467,-1.205393,-9.487421,-4.843414,-9.270224,8.497054,-4.071940,5.667943,8.311505,-5.482509,5.628367,-0.175767,8.070077,3.160912,-0.595002,9.586710,9.502640,4.805587,-4.253380,5.569350,7.393594,-5.675381,5.252104,0.715847,-4.315572,1.316200,1.929044,5.585501,-4.452942,-9.763862,6.519034,3.750025,0.090322,5.166750,4.319127,-3.783215,0.205715,-3.840338,-8.036051,7.930036,-5.671719,8.442038,-3.888239,-3.683808,7.263069,-6.531505,-2.373324,-3.811787,-0.318438,-0.228947,-7.535583,-7.017736,4.216955,-8.326869,2.455109,-6.058560,-1.202615,5.016055,-0.743992,8.716640,6.071139,-2.159130,5.823642,2.409995,-3.854930,0.598296,8.249802,-6.353307,5.579408,-3.748949,-9.403141,-6.722462,-7.111484,-9.232275,2.890451,3.156021,8.980432,1.542806,-5.712464,-2.143192,-6.979491,8.742260,-6.681775,-9.855736,-7.522685,-3.988667,4.994035,9.166988,-7.337304,-9.072733,4.490363,-2.898113,9.337317,7.126807,6.633162,9.407162,-6.626966,8.322339,-4.815303,-8.607786,-9.604858,-2.654855,1.557595,-9.735563,7.979974,6.050600,-3.254749,6.520057,3.075095,3.480996,-0.400762,-2.090672,2.588427,0.780112,0.409124,-0.853390,-4.617290,9.317359,-6.057985,-8.311341,-7.130843,-4.364492,6.832394,8.725008,-9.294990,0.393468,7.516819,5.200847,5.846804,-9.204936,-8.908935,9.348274,2.823839,-9.305532,-3.699964,9.077081,7.204011,0.043605,0.453606,9.650379,0.802216,5.943009,4.701610,1.276580,3.538414,6.919157,-8.140651,6.895303,-1.484555,6.312078,-8.822755,1.020976,-4.429211,-0.391543,2.139479,6.118510,8.862223,7.504333,-7.805353,3.026108,5.333325,1.085945,4.379352,4.276592,4.857639,-1.427654,-4.637534,3.339853,-3.681247,-6.161531,5.090196,-3.460916,-3.062806,3.075428,-5.871149,7.717198,-7.593760,6.628155,7.107020,1.393253,4.254474,-4.977221,2.735345,-6.497741,9.915700,-5.254840,3.386864,1.728756,-9.347850,-2.776447,-0.398225,-3.440044,-9.984800,-1.226164,4.584901,-1.596601,-7.195696,-0.097770,-9.085758,0.220053,5.871615,4.690212,8.969802,3.072702,4.304421,-1.374749,1.909628,-5.876313,7.894578,2.070581,-2.286704,2.424693,-9.005998,4.642631,6.652447,-3.523787,-3.426300,9.428500,0.385329,3.205394,-0.472224,-3.069206,8.675516,4.946617,6.070382,5.436411,4.738285,-0.858215,-0.967721,-7.328771,2.042567,-0.144848,-0.570260,1.532514,-4.412701,1.934901,-5.868094,-1.847274,-0.827898,-3.601154,-4.062069,-4.840080,2.670398,0.630416,-0.390045,7.449934,9.440090,1.125972,2.439075,3.732893,9.082495,-8.822144,-6.021983,3.336660,-1.650235,-5.406661,8.295902,-7.928440,-4.548029,-3.114338,-1.348748,-5.880440,-4.106772,1.796684,-4.272887,4.972893,6.413570,1.257582,7.977707,4.174003,7.357430,-9.667606,-2.607880,3.442667,0.634570,8.527272,9.765345,4.051633,7.450319,2.138116,2.692723,6.690046,-5.072594,-8.029476,-0.251569,0.365300,8.342839,-0.833918,5.084317,-7.211264,-3.204516,-2.707909,2.194207,5.579506,-5.896466,-9.155869,9.749938,4.533001,2.389126,2.856097,5.316838,0.447853,4.689824,-5.566272,4.699633,4.021227,-0.547809,8.449758,3.045245,-9.775034,4.257828,6.047848,-4.564717,-4.217223,-4.750851,0.327920,-6.172601,-3.702363,6.131948,-1.308726,-7.628930,-4.828197,1.139850,-5.134053,-1.578793,2.025414,-3.904301,-0.427009,3.475146,-4.196966,8.754077,1.416058,-3.790163,4.289636,-9.037870,-9.076343,7.533830,7.086818,-2.468569,3.959987,-8.439177,-9.174714,2.547244,9.888078,2.217197,-3.937574,-9.282719,-8.666663,4.161499], dtype = "float32")#candidate|18725|(1650,)|const|float32
call_18724 = relay.TupleGetItem(func_18336_call(relay.reshape(const_18725.astype('float32'), [1650,])), 0)
call_18726 = relay.TupleGetItem(func_18339_call(relay.reshape(const_18725.astype('float32'), [1650,])), 0)
func_11614_call = mod.get_global_var('func_11614')
func_11615_call = mutated_mod.get_global_var('func_11615')
call_18735 = relay.TupleGetItem(func_11614_call(), 0)
call_18736 = relay.TupleGetItem(func_11615_call(), 0)
output = relay.Tuple([call_18700,call_18713,const_18714,var_18715,var_18716,call_18724,const_18725,call_18735,])
output2 = relay.Tuple([call_18701,call_18717,const_18714,var_18715,var_18716,call_18726,const_18725,call_18736,])
func_18741 = relay.Function([var_18715,var_18716,], output)
mod['func_18741'] = func_18741
mod = relay.transform.InferType()(mod)
mutated_mod['func_18741'] = func_18741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18741_call = mutated_mod.get_global_var('func_18741')
var_18743 = relay.var("var_18743", dtype = "uint8", shape = (72,))#candidate|18743|(72,)|var|uint8
var_18744 = relay.var("var_18744", dtype = "float32", shape = (245,))#candidate|18744|(245,)|var|float32
call_18742 = func_18741_call(var_18743,var_18744,)
output = call_18742
func_18745 = relay.Function([var_18743,var_18744,], output)
mutated_mod['func_18745'] = func_18745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16378_call = mod.get_global_var('func_16378')
func_16379_call = mutated_mod.get_global_var('func_16379')
call_18789 = relay.TupleGetItem(func_16378_call(), 0)
call_18790 = relay.TupleGetItem(func_16379_call(), 0)
output = call_18789
output2 = call_18790
func_18795 = relay.Function([], output)
mod['func_18795'] = func_18795
mod = relay.transform.InferType()(mod)
mutated_mod['func_18795'] = func_18795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18795_call = mutated_mod.get_global_var('func_18795')
call_18796 = func_18795_call()
output = call_18796
func_18797 = relay.Function([], output)
mutated_mod['func_18797'] = func_18797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10239_call = mod.get_global_var('func_10239')
func_10240_call = mutated_mod.get_global_var('func_10240')
call_18809 = func_10239_call()
call_18810 = func_10239_call()
func_15953_call = mod.get_global_var('func_15953')
func_15954_call = mutated_mod.get_global_var('func_15954')
call_18815 = relay.TupleGetItem(func_15953_call(), 0)
call_18816 = relay.TupleGetItem(func_15954_call(), 0)
func_14908_call = mod.get_global_var('func_14908')
func_14911_call = mutated_mod.get_global_var('func_14911')
const_18820 = relay.const([5.653586,7.525383,-9.250503,-7.189426,-8.226216,6.657725,-3.902616,4.607373,-4.871822,7.726360,6.492287,-1.442055,-9.196775,4.421958,7.628912,-7.296667,-4.012766,-3.271999,-1.807850,0.165098,-0.654894,6.896839,5.096159,8.952449,6.151079,4.662500,-3.503438,6.667350,-8.165885,6.455234,6.042316,8.756868,3.267087,-9.080893,-2.480618,-2.909572,3.273607,8.318311,-4.091893,-6.547290,9.048736,-0.564733,0.136848,-7.350894,-6.820860,-9.473658,1.261167,2.706657,3.956401,5.869335,6.222896,1.184043,8.616493,-9.915978,2.805200,-1.249044,-4.396111,-5.112028,-2.851711,-5.099982,-6.672694,-2.355007,-1.168852,-5.766803,-8.577981,8.260528,6.063731,-0.322436,8.957171,-1.341177,3.379911,8.370368,2.162208,-7.795495,-6.087757,6.806100,9.637732,-6.761741,2.294113,0.610456,-4.705478,-5.997615,1.711028,6.704945,9.308823,3.525147,-9.249926,-1.905012,2.230216,8.772318,3.096900,-2.306174,-3.316936,-3.430028,-8.862415,2.285114,-6.154282,-4.819430,-7.228125,-3.582503,-1.315306,4.538949,-1.849360,-4.748643,-2.220677,2.376744,-7.049678,-2.219194,9.994723,8.403724,-0.144406,-4.012672,-0.136152,0.450775,-1.520318,-3.649277,2.693745,3.323802,6.115879,9.414080], dtype = "float32")#candidate|18820|(120,)|const|float32
call_18819 = func_14908_call(relay.reshape(const_18820.astype('float32'), [4, 10, 3]))
call_18821 = func_14908_call(relay.reshape(const_18820.astype('float32'), [4, 10, 3]))
output = relay.Tuple([call_18809,call_18815,call_18819,const_18820,])
output2 = relay.Tuple([call_18810,call_18816,call_18821,const_18820,])
func_18824 = relay.Function([], output)
mod['func_18824'] = func_18824
mod = relay.transform.InferType()(mod)
mutated_mod['func_18824'] = func_18824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18824_call = mutated_mod.get_global_var('func_18824')
call_18825 = func_18824_call()
output = call_18825
func_18826 = relay.Function([], output)
mutated_mod['func_18826'] = func_18826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14874_call = mod.get_global_var('func_14874')
func_14875_call = mutated_mod.get_global_var('func_14875')
call_18833 = relay.TupleGetItem(func_14874_call(), 0)
call_18834 = relay.TupleGetItem(func_14875_call(), 0)
func_8849_call = mod.get_global_var('func_8849')
func_8850_call = mutated_mod.get_global_var('func_8850')
call_18876 = func_8849_call()
call_18877 = func_8849_call()
func_17182_call = mod.get_global_var('func_17182')
func_17185_call = mutated_mod.get_global_var('func_17185')
var_18890 = relay.var("var_18890", dtype = "float32", shape = (98, 4))#candidate|18890|(98, 4)|var|float32
call_18889 = relay.TupleGetItem(func_17182_call(relay.reshape(var_18890.astype('float32'), [14, 7, 4])), 0)
call_18891 = relay.TupleGetItem(func_17185_call(relay.reshape(var_18890.astype('float32'), [14, 7, 4])), 0)
func_14874_call = mod.get_global_var('func_14874')
func_14875_call = mutated_mod.get_global_var('func_14875')
call_18895 = relay.TupleGetItem(func_14874_call(), 0)
call_18896 = relay.TupleGetItem(func_14875_call(), 0)
output = relay.Tuple([call_18833,call_18876,call_18889,var_18890,call_18895,])
output2 = relay.Tuple([call_18834,call_18877,call_18891,var_18890,call_18896,])
func_18924 = relay.Function([var_18890,], output)
mod['func_18924'] = func_18924
mod = relay.transform.InferType()(mod)
var_18925 = relay.var("var_18925", dtype = "float32", shape = (98, 4))#candidate|18925|(98, 4)|var|float32
output = func_18924(var_18925)
func_18926 = relay.Function([var_18925], output)
mutated_mod['func_18926'] = func_18926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16059_call = mod.get_global_var('func_16059')
func_16060_call = mutated_mod.get_global_var('func_16060')
call_19015 = func_16059_call()
call_19016 = func_16059_call()
output = relay.Tuple([call_19015,])
output2 = relay.Tuple([call_19016,])
func_19021 = relay.Function([], output)
mod['func_19021'] = func_19021
mod = relay.transform.InferType()(mod)
output = func_19021()
func_19022 = relay.Function([], output)
mutated_mod['func_19022'] = func_19022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10437_call = mod.get_global_var('func_10437')
func_10439_call = mutated_mod.get_global_var('func_10439')
call_19064 = func_10437_call()
call_19065 = func_10437_call()
func_17456_call = mod.get_global_var('func_17456')
func_17458_call = mutated_mod.get_global_var('func_17458')
call_19074 = relay.TupleGetItem(func_17456_call(), 0)
call_19075 = relay.TupleGetItem(func_17458_call(), 0)
output = relay.Tuple([call_19064,call_19074,])
output2 = relay.Tuple([call_19065,call_19075,])
func_19077 = relay.Function([], output)
mod['func_19077'] = func_19077
mod = relay.transform.InferType()(mod)
output = func_19077()
func_19078 = relay.Function([], output)
mutated_mod['func_19078'] = func_19078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18257_call = mod.get_global_var('func_18257')
func_18258_call = mutated_mod.get_global_var('func_18258')
call_19108 = relay.TupleGetItem(func_18257_call(), 0)
call_19109 = relay.TupleGetItem(func_18258_call(), 0)
output = relay.Tuple([call_19108,])
output2 = relay.Tuple([call_19109,])
func_19130 = relay.Function([], output)
mod['func_19130'] = func_19130
mod = relay.transform.InferType()(mod)
mutated_mod['func_19130'] = func_19130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19130_call = mutated_mod.get_global_var('func_19130')
call_19131 = func_19130_call()
output = call_19131
func_19132 = relay.Function([], output)
mutated_mod['func_19132'] = func_19132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14980_call = mod.get_global_var('func_14980')
func_14981_call = mutated_mod.get_global_var('func_14981')
call_19182 = relay.TupleGetItem(func_14980_call(), 1)
call_19183 = relay.TupleGetItem(func_14981_call(), 1)
func_11367_call = mod.get_global_var('func_11367')
func_11368_call = mutated_mod.get_global_var('func_11368')
call_19185 = relay.TupleGetItem(func_11367_call(), 0)
call_19186 = relay.TupleGetItem(func_11368_call(), 0)
output = relay.Tuple([call_19182,call_19185,])
output2 = relay.Tuple([call_19183,call_19186,])
func_19194 = relay.Function([], output)
mod['func_19194'] = func_19194
mod = relay.transform.InferType()(mod)
output = func_19194()
func_19195 = relay.Function([], output)
mutated_mod['func_19195'] = func_19195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14522_call = mod.get_global_var('func_14522')
func_14523_call = mutated_mod.get_global_var('func_14523')
call_19199 = func_14522_call()
call_19200 = func_14522_call()
output = relay.Tuple([call_19199,])
output2 = relay.Tuple([call_19200,])
func_19213 = relay.Function([], output)
mod['func_19213'] = func_19213
mod = relay.transform.InferType()(mod)
output = func_19213()
func_19214 = relay.Function([], output)
mutated_mod['func_19214'] = func_19214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17314_call = mod.get_global_var('func_17314')
func_17316_call = mutated_mod.get_global_var('func_17316')
call_19269 = func_17314_call()
call_19270 = func_17314_call()
output = relay.Tuple([call_19269,])
output2 = relay.Tuple([call_19270,])
func_19295 = relay.Function([], output)
mod['func_19295'] = func_19295
mod = relay.transform.InferType()(mod)
output = func_19295()
func_19296 = relay.Function([], output)
mutated_mod['func_19296'] = func_19296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15919_call = mod.get_global_var('func_15919')
func_15921_call = mutated_mod.get_global_var('func_15921')
call_19387 = relay.TupleGetItem(func_15919_call(), 0)
call_19388 = relay.TupleGetItem(func_15921_call(), 0)
output = relay.Tuple([call_19387,])
output2 = relay.Tuple([call_19388,])
func_19405 = relay.Function([], output)
mod['func_19405'] = func_19405
mod = relay.transform.InferType()(mod)
mutated_mod['func_19405'] = func_19405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19405_call = mutated_mod.get_global_var('func_19405')
call_19406 = func_19405_call()
output = call_19406
func_19407 = relay.Function([], output)
mutated_mod['func_19407'] = func_19407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15524_call = mod.get_global_var('func_15524')
func_15525_call = mutated_mod.get_global_var('func_15525')
call_19418 = relay.TupleGetItem(func_15524_call(), 0)
call_19419 = relay.TupleGetItem(func_15525_call(), 0)
output = relay.Tuple([call_19418,])
output2 = relay.Tuple([call_19419,])
func_19427 = relay.Function([], output)
mod['func_19427'] = func_19427
mod = relay.transform.InferType()(mod)
mutated_mod['func_19427'] = func_19427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19427_call = mutated_mod.get_global_var('func_19427')
call_19428 = func_19427_call()
output = call_19428
func_19429 = relay.Function([], output)
mutated_mod['func_19429'] = func_19429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19443 = relay.var("var_19443", dtype = "float64", shape = (3, 6, 2))#candidate|19443|(3, 6, 2)|var|float64
uop_19444 = relay.erf(var_19443.astype('float64')) # shape=(3, 6, 2)
output = uop_19444
output2 = uop_19444
func_19478 = relay.Function([var_19443,], output)
mod['func_19478'] = func_19478
mod = relay.transform.InferType()(mod)
mutated_mod['func_19478'] = func_19478
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19479 = relay.var("var_19479", dtype = "float64", shape = (3, 6, 2))#candidate|19479|(3, 6, 2)|var|float64
func_19478_call = mutated_mod.get_global_var('func_19478')
call_19480 = func_19478_call(var_19479)
output = call_19480
func_19481 = relay.Function([var_19479], output)
mutated_mod['func_19481'] = func_19481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15369_call = mod.get_global_var('func_15369')
func_15370_call = mutated_mod.get_global_var('func_15370')
call_19514 = func_15369_call()
call_19515 = func_15369_call()
output = call_19514
output2 = call_19515
func_19535 = relay.Function([], output)
mod['func_19535'] = func_19535
mod = relay.transform.InferType()(mod)
mutated_mod['func_19535'] = func_19535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19535_call = mutated_mod.get_global_var('func_19535')
call_19536 = func_19535_call()
output = call_19536
func_19537 = relay.Function([], output)
mutated_mod['func_19537'] = func_19537
mutated_mod = relay.transform.InferType()(mutated_mod)
const_19577 = relay.const(8.193201, dtype = "float64")#candidate|19577|()|const|float64
var_19578 = relay.var("var_19578", dtype = "float64", shape = (7, 11, 7))#candidate|19578|(7, 11, 7)|var|float64
bop_19579 = relay.power(const_19577.astype('float64'), var_19578.astype('float64')) # shape=(7, 11, 7)
func_12235_call = mod.get_global_var('func_12235')
func_12237_call = mutated_mod.get_global_var('func_12237')
call_19591 = relay.TupleGetItem(func_12235_call(), 2)
call_19592 = relay.TupleGetItem(func_12237_call(), 2)
output = relay.Tuple([bop_19579,call_19591,])
output2 = relay.Tuple([bop_19579,call_19592,])
func_19593 = relay.Function([var_19578,], output)
mod['func_19593'] = func_19593
mod = relay.transform.InferType()(mod)
mutated_mod['func_19593'] = func_19593
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19594 = relay.var("var_19594", dtype = "float64", shape = (7, 11, 7))#candidate|19594|(7, 11, 7)|var|float64
func_19593_call = mutated_mod.get_global_var('func_19593')
call_19595 = func_19593_call(var_19594)
output = call_19595
func_19596 = relay.Function([var_19594], output)
mutated_mod['func_19596'] = func_19596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14598_call = mod.get_global_var('func_14598')
func_14600_call = mutated_mod.get_global_var('func_14600')
call_19652 = func_14598_call()
call_19653 = func_14598_call()
func_9134_call = mod.get_global_var('func_9134')
func_9137_call = mutated_mod.get_global_var('func_9137')
var_19657 = relay.var("var_19657", dtype = "uint8", shape = (18, 4))#candidate|19657|(18, 4)|var|uint8
call_19656 = relay.TupleGetItem(func_9134_call(relay.reshape(var_19657.astype('uint8'), [72,])), 4)
call_19658 = relay.TupleGetItem(func_9137_call(relay.reshape(var_19657.astype('uint8'), [72,])), 4)
output = relay.Tuple([call_19652,call_19656,var_19657,])
output2 = relay.Tuple([call_19653,call_19658,var_19657,])
func_19663 = relay.Function([var_19657,], output)
mod['func_19663'] = func_19663
mod = relay.transform.InferType()(mod)
var_19664 = relay.var("var_19664", dtype = "uint8", shape = (18, 4))#candidate|19664|(18, 4)|var|uint8
output = func_19663(var_19664)
func_19665 = relay.Function([var_19664], output)
mutated_mod['func_19665'] = func_19665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10437_call = mod.get_global_var('func_10437')
func_10439_call = mutated_mod.get_global_var('func_10439')
call_19689 = func_10437_call()
call_19690 = func_10437_call()
output = relay.Tuple([call_19689,])
output2 = relay.Tuple([call_19690,])
func_19699 = relay.Function([], output)
mod['func_19699'] = func_19699
mod = relay.transform.InferType()(mod)
output = func_19699()
func_19700 = relay.Function([], output)
mutated_mod['func_19700'] = func_19700
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19756 = relay.var("var_19756", dtype = "float64", shape = (1, 10, 6))#candidate|19756|(1, 10, 6)|var|float64
uop_19757 = relay.atanh(var_19756.astype('float64')) # shape=(1, 10, 6)
uop_19759 = relay.exp(uop_19757.astype('float32')) # shape=(1, 10, 6)
output = uop_19759
output2 = uop_19759
func_19797 = relay.Function([var_19756,], output)
mod['func_19797'] = func_19797
mod = relay.transform.InferType()(mod)
mutated_mod['func_19797'] = func_19797
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19798 = relay.var("var_19798", dtype = "float64", shape = (1, 10, 6))#candidate|19798|(1, 10, 6)|var|float64
func_19797_call = mutated_mod.get_global_var('func_19797')
call_19799 = func_19797_call(var_19798)
output = call_19799
func_19800 = relay.Function([var_19798], output)
mutated_mod['func_19800'] = func_19800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17104_call = mod.get_global_var('func_17104')
func_17106_call = mutated_mod.get_global_var('func_17106')
call_19807 = relay.TupleGetItem(func_17104_call(), 0)
call_19808 = relay.TupleGetItem(func_17106_call(), 0)
func_8065_call = mod.get_global_var('func_8065')
func_8067_call = mutated_mod.get_global_var('func_8067')
call_19830 = relay.TupleGetItem(func_8065_call(), 0)
call_19831 = relay.TupleGetItem(func_8067_call(), 0)
func_17480_call = mod.get_global_var('func_17480')
func_17483_call = mutated_mod.get_global_var('func_17483')
const_19847 = relay.const([-4.103183,-9.389510,-4.332930,7.233283,-9.447343,6.997231,-4.775060,6.951055,3.660352,-0.188753,-0.069716,-7.586850,-4.525599,3.286140,8.151334,-8.505555,9.009239,-8.421727,8.397868,6.091939,-4.856473,-3.210275,9.910564,-9.223380,-3.121393,3.421551,-4.866248,1.965760,-3.976169,-3.744735,6.932389,-6.220822,8.007330,-8.490248,-6.036761,0.842130,-8.901355,6.239220,0.610956,-6.393415,3.282116,-7.229274,9.243397,-7.205788,-7.719764,6.154739,-8.431825,-5.576130,0.850303,-8.187310,-6.908443,-9.017094,-5.895655,-2.913845,4.442154,9.706226,0.669334,-1.414428,9.092687,-6.296111,6.081616,3.672762,4.437311,2.780648,-6.968733,-8.539707,6.388415,5.909378,4.538127,5.105411,-1.182878,3.894971,-7.369775,-4.130814,-1.263916,4.348046,9.260289,4.913685,-1.922608,9.975275,8.459070,-1.373362,-9.820376,-2.064954,4.570196,-3.770854,-3.638526,9.934501,5.105572,-4.185570,6.418503,8.691249,-0.292598,0.952248,8.718900,6.679041,3.297498,-9.116479,7.221575,5.974233,-7.367337,-3.229960,7.565107,-8.823468,1.673355,-5.038741,-0.062741,3.030445,2.828701,-2.365686,9.626009,7.455476,5.195739,-5.716867,-6.281765,8.167481,5.081931,6.296013,-1.177688,9.786954,-3.916598,-8.467210,3.874939,4.942957,-3.356087,-4.161655,0.186658,-1.206050,1.218626,0.190518,-5.768053,-0.763344,-0.868292,-7.618720,7.039202,-0.846757,-2.128596,3.539970,8.009866,-3.508989,-2.195254,4.385810,-1.457449,-4.723615,9.106534,3.344142,-8.544334,4.619904,9.660809,6.339518,-0.780273,-2.241396,-5.966965,-3.917627,-8.139300,-8.708207,8.309361,-2.733397,1.012628,6.049846,-2.528477,6.603945,8.534908,2.320597,-3.122900,4.433037,-9.459596,7.682714,2.965929,-9.033315,-2.251744,-3.730259,0.773440,1.074170,6.080136,7.661381,3.164422,1.406426,9.276839,9.963086,2.748128,-2.363951,-7.316500,1.273258,-8.572366,0.779359,-9.584849,-2.090398,-5.078315,-4.022086,5.835939,4.389282,-1.983446,2.597032,8.752107,-1.319253,1.501916,2.292107,-7.214306,-0.989448,-1.841564,-3.477840,4.805776,-9.076199,-1.087850,-0.728950,-1.475229,5.882001,-7.497175,1.084194,2.494252,-4.569768,-6.689321,5.416158,-6.672612,6.318912,0.829599,0.045896,0.979860,7.899054,0.456867,7.064268,1.381013,-2.743061,8.947915,-2.096474,8.770398,5.795921,-8.966162,9.835814,-8.471747,8.753492,-8.272796,9.281323,0.537175,9.892184,-4.234335,-0.307631,5.143996,5.935490,-1.895096,-7.596236,-5.808792,-8.166584,-6.042178,-0.860421,-8.071830,-9.476867,-8.953009,-7.329702,-7.971709,-5.849743,-2.672536,5.991461,-7.969024,-8.378627,-8.101957,-1.985733,9.427966,2.068178,-4.556814,-3.511578,8.820586,4.402702,-9.540709,9.783819,-2.072139,0.984926,3.773159,-0.812314,1.958787,-7.296065,0.144308,1.292763,4.713547,-7.853775,-4.019840,6.717012,-5.577047,6.059426,-2.936515,2.313859,0.919484,-3.948372,1.521711,-5.720029,2.768040,-5.686370,1.656550,0.445429,-9.375918,3.203956,8.061768,9.680994,2.747991,-3.220125,5.989585,-2.235148,5.661164,1.929930,-8.834389,2.306011,0.268847,-2.359783,6.224440,0.131359,-4.155312,-0.836180,2.533836,5.167954,3.244713,1.472501,4.633308,3.767230,-3.911463,-0.278664,-8.154315,-4.891228,4.925635,-6.641315,8.433617,8.103372,-0.198768,0.859162,2.795967,0.501925,-9.282906,4.360251,-9.603423,-5.076483,-3.288315,7.524747,6.697061,-4.682373,1.949485,9.486593,-0.085779,-5.666630,4.851167,4.933254,-4.409951,8.758275,1.786243,-8.887431,2.209020,-2.310875,4.244571,-6.012384,2.072089,-9.870687,9.297178,0.468565,-7.597715,3.969191,1.091169,-8.764322,7.230892,4.333335,-0.703129,-4.596522,-4.358865,3.690037,2.138037,-9.889321,-5.928180,8.206470,1.483373,-0.776821,-1.316336,7.880053,-9.544689,7.127179,3.196628,-5.674790,-9.903992,1.790335,2.239652,1.305803,-2.338526,0.713125,-9.114982,-8.573740,-6.816798,7.704468,-5.425338,-8.652101,-7.415115,-1.343635,-1.982575,8.652557,-8.725810,-5.532560,-2.129878,-0.749934,8.362125,2.539343,-3.461466,9.068286,-2.994833,5.826908,1.944429,5.097334,5.652622,8.343717,-2.291302,-7.513643,4.343882,-3.691656,-7.542322,-1.554920,9.575053,1.332111,-6.122304,-9.129176,7.287844,4.024441,0.265619,-9.468439,4.735051,5.318345,7.207408,-3.406695,-8.729179,-2.652614,8.075035,-0.208955,-3.446934,-8.035208,0.844510,-1.415509,-3.662211,2.344167,-9.306008,-2.769417,-6.435137,-5.299377,9.939795,-6.414780,8.336844,1.891183,-5.423120,7.666546,9.275218,3.715404,-7.849265,-4.261816,2.881591,6.106814,1.970179,4.638925,9.242438,3.685909,-5.731178,-2.332031,-2.201751,-4.807816,0.792298,-5.643042,4.437137,1.727349,4.084114,-3.190248,-5.545227,-0.800577,7.697154,8.837337,1.751855,-2.602131,-1.310235,-3.888348,-3.490101,8.361488,-3.885505,-1.810440,9.583602,-1.068119,7.509426,-5.116021,-1.838664,-2.333698,-6.482151,-6.013455,-4.814395,-0.245365,0.119746,-0.980436,8.058818,5.224438,5.105526,-5.230059,-8.267866,1.702209,5.684801,9.902672,-4.849476,-4.075204,8.335501,0.928552,6.720911,-0.869398,-9.856051,-6.837081,7.191027,3.956376,0.913556,0.710598,-8.705424,-5.860767,-8.968736,5.167902,6.515734,-6.568750,-7.221258,-4.025793,4.145623,-5.921009,3.875349,8.162662,6.961922,0.814457,-5.044130,-0.466986,2.388746,5.292776,-4.859249,4.027524,-3.820728,-1.104342,3.203465,-3.121838,9.058553,-1.932517,7.785771,7.643389,-8.232944,6.945238,-3.155297,-6.924564,-5.036922,4.049610,-6.264899,-2.678991,-0.636410,-1.543190,-9.652200,-8.451181,6.555502,-6.442820,0.328856,5.813988,0.469753,-2.305823,-1.429355,0.082739,-0.664125,3.047019,0.672998,0.221287,-7.555863,0.707403,-8.593777,8.830618,-8.599803,-6.883075,8.928664,-4.283929,2.343328,-2.189953,9.100260,-6.520192,8.944432,-4.109987,-2.686805,-5.567602,0.457618,3.278670,-2.704088,-2.358809,-8.540499,-0.351988,-6.389415,-6.988981,7.593401,-7.271527,8.184672,5.488322,-9.816414,2.304396,7.816606,-1.102015,-9.949204,8.877675,-4.894893,7.500940,-7.793141,-8.867371,-3.592582,-4.081950,-5.697023,-1.832835,-2.494286,-2.579120,-0.563331,0.902236,4.322367,-3.065490,4.338508,-5.760744,0.341562,-6.999085,3.813085,5.263664,-0.533612,-1.794579,-3.234801,-3.217602,-7.052984,6.112934,-5.435235,-4.219364,-3.968962,8.277205,-9.875743,7.128219,-2.512900,-6.577921,8.333931,6.648604,6.958383,-4.423108,2.197676,-6.160755,0.742682,-5.614124,-2.373840,9.316034,4.514361,-9.953807,4.809419,-4.180944,-4.545259,3.020781,-1.977740,5.478975,-6.656547,1.526473,-2.125960,6.876373,5.976820,8.863864,5.574612,6.852471,-5.771666,-5.496457,0.016561,6.827154,5.701663,3.424242,6.239148,-0.922107,-3.984614,4.690736,3.341016,-9.838450,-8.028478,7.361829,9.159472,6.299938,-7.607513,2.088268,-9.613179,2.222276,6.928308,9.180177,5.907294,8.891256,7.377552,-8.151189,2.415381,5.350515,8.078896,9.011055,5.804964,-8.698052,1.131225,-0.724388,-6.983950,0.064532,-0.461562,-9.087862,-7.647823,-0.499237,9.404087,0.605704,4.500452,-3.567285,7.352080,6.110185,-0.482162,-7.044670,0.547160,6.558831,4.163699,-2.799563,0.419336,5.562556,-2.536077,2.349651,5.882085,-8.207589,-6.976684,8.592178,6.011119,-7.212589,-3.309671,0.997230,2.905045,6.346828,6.698438,9.766304,-2.032575,6.926725,-4.492653,-7.499014,1.375016,-5.287612,-6.068965,3.361901,1.016218,6.938455,-0.772642,8.259816,-5.875029,-5.376232,-8.395349,-1.265383,6.049015,4.089545,0.300688,2.069439,1.265389,-9.853373,8.497257,9.199327,4.217470,-8.940204,4.210595,-4.257427,-3.233463,0.968173,-9.244291,7.821284,5.125806,2.385842,3.174929,6.334943,-8.193713,-3.188070,7.598294,-9.862165,-6.231231,1.593654,8.554772,3.387803,-0.512308,-3.382269,9.120805,-4.833709,3.802463,6.677265,-4.472576,3.400008,-3.087927,-7.408281,1.326727,-4.783323,3.976109,0.856818,5.919174,-0.320049,9.641432,-3.912561,5.441810,-2.757113,-3.670356,0.912876,-9.781491,-7.440026,-1.931436,3.712070,9.074794,4.406700,2.523803,5.746992,-6.552558,-3.231281,2.415641,-7.608478,-0.127913,2.983287,-2.422067,4.676448,7.395181,4.098392,2.053849,1.889104,-9.513806,0.396006,9.092080,6.422560,5.649628,1.883634,-4.933477,9.093030,-4.084343,-5.807713,6.662816,-3.896873,6.758194,-4.015775,-5.334404,2.119485,-1.661419,-0.571174,-0.180362,9.682879,3.117601,-3.258343,-1.709535,-6.399595,-5.921318,4.477994,4.509388,-6.387556,6.619782,2.308611,-7.559175,4.292641,6.962483,-2.506095,8.195595,3.155618,-6.143331,-8.826791,7.079569,-6.124602,1.206294,2.289088,1.806750,9.375378,-9.940426,-6.468415,-1.622250,-3.442383,6.979138,8.176712,-7.296632,8.182297,-5.502929,-1.528036,3.982504,2.153207,-0.052304,1.060672,-4.629780,8.181807,7.344469,4.985398,5.542006,4.408115,-7.546429,1.898077,-5.855597,3.400263,-6.281911,-0.674698,-3.533218,9.941387,9.677937,-6.165497,7.889881,-2.947457,7.647816,-1.385262,5.817920,8.418242,-3.963703,5.067721,-2.295712,4.571044,-3.093835,-9.417056,2.091371,0.136201,-2.209925,-8.392015,8.893908,-6.243101,-6.910554,3.113117,-1.907597,3.794236,3.258000,5.276058,-4.246756,4.129789,8.849891,8.796619,0.386034,3.012647,8.851449,2.511003,-4.596075,7.086676,8.848310,6.986345,-7.037930,-1.084679,9.765089,1.595401,2.209327,-0.520413,-1.768128,8.508523,-2.626075,1.955990,2.912699,1.403620,-3.484197,-8.808251,6.225753,0.924632,2.455755,-4.790871,-0.679442,-1.227499,-9.852906,-1.528882,-2.477567,-0.140956,-8.858226,-4.122172,-1.455528,2.066411,6.551254,-8.813055,8.345911,-9.978511,-2.414970,6.595870,-2.286141,-0.430794,-3.582067,6.966547,-1.192210,-5.060232,1.007229,-6.504827,-8.910597,-9.224773,-1.222809,-0.572209,-2.387660,-7.235407,5.728535,6.744037,4.884532,-6.676267,-0.798418,-2.541194,9.182437,9.871344,-5.348299,8.986390,-4.375866,-9.866397,-3.746852,-3.757237,0.970927,0.448478,5.679364,-8.405705,-7.476472,-8.933790,-9.120328,-1.694408,7.047842,-6.476546,7.750276,-2.596286,7.260470,-1.111509,-6.065564,-5.271567,2.591284,-1.979527,2.576714,9.839076,-6.596966,-0.549658,7.870452,-8.538795,4.208603,-0.592981,-9.323564,-9.363562,1.524159,-8.574634,8.510658,3.416951,-3.871595,5.392506,-8.843226,-4.707167,3.358233,2.327758,7.757922,6.464846,-1.323658,4.151415,5.327298,-1.847727,5.419484,-6.232428,2.479851,8.874170,6.703698,1.019613,-5.488447,-7.950162,8.170801,-0.875645,-3.430403,0.544229,1.738473,4.576304,-1.745875,9.752757,-4.408612,-5.760239,6.978311,-3.822933,5.787985,-2.155232,2.771259,3.954444,-8.168416,6.795140,6.347707,9.389514,9.416928,3.188255,-4.995119,9.560110,-9.324696,-5.816922,-2.106053,8.532822,0.200606,8.328927,-9.333428,2.118769,-1.453425,8.962491,5.583641,-6.621530,-4.891672,-4.077240,-6.189503,1.090124,1.777525,-5.033302,-5.134025,4.326708,8.065755,-3.223159,0.141637,-3.380510,-8.777061,-5.873677,-6.172851,5.113358,-1.617874,2.927098,5.023514,-5.134607,-4.396721,-5.871460,-3.021158,-1.595130,-4.255018,9.371280,-1.622165,4.947661,-7.101143,-2.742492,-6.823503,3.906548,8.568891,8.455849,8.910022,-8.957185,-4.958287,7.991041,-8.164042,-2.934826,-8.875589,8.056628,7.854595,-2.035235,-9.636703,-6.564517,-8.560505,0.464651,-6.080583,-1.389807,-6.858614,-7.729572,-6.214829,3.992583,5.455711,3.867467,-1.362878,2.478430,-2.916625,7.170070,-6.931511,5.850323,8.007208,1.499160,-9.624259,5.850144,-9.070568,9.778002,7.766515,1.721763,7.500685,7.995677,6.776842,6.111915,-0.245769,-9.998643,3.165861,1.376028,4.501714,-8.930986,-7.836310,-6.906523,7.376453,3.671851,4.947438,-7.726960,-4.983498,-0.704315,-3.398918,5.242938,-9.049195,4.594177,4.947707,-5.981752,6.049744,-6.334030,-8.404528,-8.784528,4.813976,7.593790,5.892750,3.961260,0.127152,7.956988,3.244153,-9.250328,3.156415,8.516875,-4.601334,7.111636,7.447632,6.819946,-1.166579,9.373410,-1.297874,-3.803908,-7.727506,0.774701,3.412042,4.525454,4.850515,-5.531801,-2.806892,1.492187,1.514630,-0.400503,7.884498,6.266430,-4.931173,9.925028,4.647944,-3.658101,9.587839,3.773535,-7.878054,1.075892,-5.258058,-6.698001,-0.187055,4.544571,-0.356015,-9.019621,3.499402,-0.244223,-2.569187,-1.020253,1.096904,-3.472706,-7.217293,-9.871581,-3.108149,-8.217293,1.589994,7.768642,1.908569,-6.401013,7.315070,0.998409,-2.639864,-6.385078,8.132567,-4.439812,3.253690,5.015866,-7.739700,-1.417467,6.313663,7.988155,-2.719647,-8.291351,8.424800,3.823327,8.861347,9.947385,-3.465924,9.059985,9.934606,2.915723,-3.409709,-8.452747,-5.310400,9.523707,-1.372747,-6.825802,-1.468308,-6.802750,8.469394,-8.277391,-9.320247,-7.463970,7.627199,-8.602392,8.287552,2.709902,-9.223545,-5.818414,-0.022382,-8.169547,-2.035551,4.029708,-3.170129,-4.298379,-9.803730,-2.122897,4.849290,4.506921,-5.166164,7.569542,0.444816,7.239819,-4.412924,-4.781914,-3.946411,4.264347,-2.169959,1.751738,-8.356905,-2.381910,-1.476321,8.843258,-0.076127,-2.180520,-2.255916,-4.329762,-5.240707,5.205556,-9.903415,1.904754,5.349009,2.695553,-7.054076,-7.658478,1.005364,8.235191,7.808795,2.605680,9.419582,2.597063,4.119889,-5.443201,6.586842,-2.003738,7.968601,-3.361170,3.158958,-7.565235,-8.572101,-5.789248,-4.261972,6.718151,7.438022,9.899047,-9.379391,-0.613430,-0.835157,1.342930,3.740981,1.526204,-6.683917,3.435273,-1.421458,1.015351,-5.260086,-9.675542,1.064797,-1.232504,-7.692440,3.079801,-3.108328,-1.011085,-6.355214,8.105439,8.938851,0.248246,-9.775136,3.825329,-0.090891,-0.449717,4.247506,7.250277,-6.172439,2.755005,4.255875,-0.522094,-8.238563,4.088134,-1.386193,-7.888917,2.462438,9.172898,-1.855494,-9.272492,7.628687,5.021313,7.090999,1.145489,2.763390,-0.750166,-7.031654,-4.099947,5.874287,1.654579,-4.353799,-8.116224,6.990559,-0.384451,-1.937618,8.482479,6.383170,-3.094869,6.024050,-6.891335,-9.067545,-6.704893,6.094352,-0.049967,-5.871939,9.785773,4.482548,-0.510252,5.603246,8.140464,-1.792297,-9.338925,7.849867,-9.926311,-1.844584,0.649864,-5.456578,8.333313,6.452399,-0.657132,-7.042013,-3.294417,3.445567,-5.935589,1.591219,0.920878,-5.171634,9.230305,-4.565081,6.134166,7.773330,-0.197266,-3.421393,9.701342,9.817697,1.676482,3.415753,2.482159,-1.371156,-8.570151,6.467473,0.028048,7.945800,-8.573754,3.585807,-5.698751,-2.706191,-7.014792,4.064164,-9.357205,1.216379,-5.270849,-3.816570,-9.388628,8.099281,-3.020805,-8.059360,3.219173,9.014591,4.620759,7.013255,1.827379], dtype = "float32")#candidate|19847|(1440,)|const|float32
var_19848 = relay.var("var_19848", dtype = "float64", shape = (220, 2))#candidate|19848|(220, 2)|var|float64
call_19846 = relay.TupleGetItem(func_17480_call(relay.reshape(const_19847.astype('float32'), [15, 16, 6]), relay.reshape(var_19848.astype('float64'), [440,]), ), 3)
call_19849 = relay.TupleGetItem(func_17483_call(relay.reshape(const_19847.astype('float32'), [15, 16, 6]), relay.reshape(var_19848.astype('float64'), [440,]), ), 3)
output = relay.Tuple([call_19807,call_19830,call_19846,const_19847,var_19848,])
output2 = relay.Tuple([call_19808,call_19831,call_19849,const_19847,var_19848,])
func_19859 = relay.Function([var_19848,], output)
mod['func_19859'] = func_19859
mod = relay.transform.InferType()(mod)
mutated_mod['func_19859'] = func_19859
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19860 = relay.var("var_19860", dtype = "float64", shape = (220, 2))#candidate|19860|(220, 2)|var|float64
func_19859_call = mutated_mod.get_global_var('func_19859')
call_19861 = func_19859_call(var_19860)
output = call_19861
func_19862 = relay.Function([var_19860], output)
mutated_mod['func_19862'] = func_19862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17586_call = mod.get_global_var('func_17586')
func_17587_call = mutated_mod.get_global_var('func_17587')
call_19910 = relay.TupleGetItem(func_17586_call(), 1)
call_19911 = relay.TupleGetItem(func_17587_call(), 1)
func_13518_call = mod.get_global_var('func_13518')
func_13520_call = mutated_mod.get_global_var('func_13520')
call_19917 = relay.TupleGetItem(func_13518_call(), 2)
call_19918 = relay.TupleGetItem(func_13520_call(), 2)
uop_19922 = relay.sigmoid(call_19910.astype('float32')) # shape=(1, 11, 6)
uop_19924 = relay.sigmoid(call_19911.astype('float32')) # shape=(1, 11, 6)
func_17955_call = mod.get_global_var('func_17955')
func_17956_call = mutated_mod.get_global_var('func_17956')
call_19934 = func_17955_call()
call_19935 = func_17955_call()
bop_19948 = relay.multiply(uop_19922.astype('uint64'), relay.reshape(call_19910.astype('uint64'), relay.shape_of(uop_19922))) # shape=(1, 11, 6)
bop_19951 = relay.multiply(uop_19924.astype('uint64'), relay.reshape(call_19911.astype('uint64'), relay.shape_of(uop_19924))) # shape=(1, 11, 6)
output = relay.Tuple([call_19917,call_19934,bop_19948,])
output2 = relay.Tuple([call_19918,call_19935,bop_19951,])
func_19958 = relay.Function([], output)
mod['func_19958'] = func_19958
mod = relay.transform.InferType()(mod)
mutated_mod['func_19958'] = func_19958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19958_call = mutated_mod.get_global_var('func_19958')
call_19959 = func_19958_call()
output = call_19959
func_19960 = relay.Function([], output)
mutated_mod['func_19960'] = func_19960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8065_call = mod.get_global_var('func_8065')
func_8067_call = mutated_mod.get_global_var('func_8067')
call_20021 = relay.TupleGetItem(func_8065_call(), 0)
call_20022 = relay.TupleGetItem(func_8067_call(), 0)
func_18795_call = mod.get_global_var('func_18795')
func_18797_call = mutated_mod.get_global_var('func_18797')
call_20023 = func_18795_call()
call_20024 = func_18795_call()
output = relay.Tuple([call_20021,call_20023,])
output2 = relay.Tuple([call_20022,call_20024,])
func_20028 = relay.Function([], output)
mod['func_20028'] = func_20028
mod = relay.transform.InferType()(mod)
output = func_20028()
func_20029 = relay.Function([], output)
mutated_mod['func_20029'] = func_20029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mod.get_global_var('func_9726')
func_9728_call = mutated_mod.get_global_var('func_9728')
call_20052 = relay.TupleGetItem(func_9726_call(), 0)
call_20053 = relay.TupleGetItem(func_9728_call(), 0)
func_5133_call = mod.get_global_var('func_5133')
func_5137_call = mutated_mod.get_global_var('func_5137')
const_20073 = relay.const([-6,-7,8,-8,3,-6,10,-2,3,-6,2,-7,-9,1,-1,-3,5,7,4,-6,3,-8,4,-10,7,7,5,-10,-10,-8,-7,-1,-3,-6,6,-5,-3,-1,-5,3,-9,1,-4,-8,2,-9,-7,9,-9,-8,-6,5,10,-6,9,4,2,1,6,2,5,5,10,-5,-1,-3,8,6,-5,10,2,1,-9,9,2,-3,3,-3,6,-3,1,-3,5,6,4,2,-9,-9,7,-6,-9,8,-9,-6,-8,-1,4,-7,-5,-9,-8,4,-5,-10,1,1,-4,-6,1,7,1,-6,2,-6,-6,-6,5,4,3,2,9,-7,-4,6,-3,3,-1,-10,4,-9,-10,-7,-5,5,-6,-3,2,-7,-1,10,-8,-9,-3,1,5,-2,-7,10,-3,-9,3,3,1,2,5,-7,8,-1,7,10,3,6,2,-3,2,3,3,-3,-6,-6,10,3,9,8,-7,7,2,-4,-1,1,-9,3,10,6,-2,6,-6,-1,-4,-1,9,3,-3,-8,-3,10,-3,4,8,7,4,3,2,-7,2,9,7,-5,-10,7,-1,-7,-9,-8,-3,-8,-8,-1,6,9,7,9,10,6,-6,5,-9,2,3,6,4,-7,4,7,5,8,-3,-7,3,-7,6,8,4,5,1,5,5,10,-7,1,-2,-5,-8,-2,-4,3,10,-7,-3,-10,-4,-2,7,10,10,8,-10,10,5,-2,8,-1,7,3,-10,4,9,5,-9,-2,4,-2,-4,4,-2,-8,-10,-1,7,-6,-6,-3,8,3,-2,-6,-6,3,-9,-7,5,-3,4,-3,5,-8,-10,8,-8,5,5,-8,-10,-8,10,-1,-3,-10,-6,8,2,6,6,2,-4,-5,10,7,6,10,5,1,-6,4,5,7,7,-1,-7,6,2,10,7,-6,5,9,9,-7,-2,-7,5,4,7,-5,-8,6,4,-6,3,6,-9,-7,4,3,7,10,-6,-3,10,7,-1,-10,7,10,9,10,-8,6,3,7,-1,-3,3,-10,-6,-3,-10,-5,-10,-8,8,4,-5,9,2,-7,7,10,5,-5,6,9,-10,2,-7,6,8,-3,-4,10,-10,-9,-6,7,10,4,9,-2,6,-6,4,-8,5,7,6,3,4,-5,2,4,5,8,9,-2,5,8,1,4,-1,-3,-6,-5,10,-1,-3,6,2,1,-5,-6,8,-10,4,-4,4,-2,-6,1,8,-10,-8,8,-2,3,9,-10,7,-7,-3,-4,2,7,4,6,1,-4,4,-1,10,-8,5,-7,7,1,-6,-6,4,8,1,-1,-10,1,4,4,6,-2,-9,3,-2,-5,1,9,-3,3,-1,-6,9,6,-1,-7,2,10,-8,-7,-9,-3,2,-8,-10,-10,-7,-1,8,-10,-10,6,8,-5,-10,9,3,-10,5,-3,-8,6,-1,-2,4,6,6,-8,-9,-3,3,8,5,2,-5,6,8,-9,-7,-8,2,9,-9,4,-9,-6,-8,-10,-2,2,-9,-3,10,-8,4,2,-1,3,5,9,-2,-6,-1,3,1,3,6,7,-9,-5,-2,-6,-5,4,-6,-5,7,-1,8,-4,-1,-8,-2,-5,1,-1,-6,-7,-7,2,-5,-4,-6,3,-10,4,-3,-2,-1,-3,6,7,-2,-2,7,-4,9,-7,4,-1,-6,-8,1,-1,7,-5,7,-5,-8,9,9,10,-3,4,-6,4,4,-8,-1,5,2,-9,4,1,10,-7,-5,-8,-3,-10,9,-10,5,8,-8,2,-5,-10,-4,10,3,5,-6,8,5,-10,-1,9,-10,-10,10,-8,-2,3,-1,1,2,-2,9,10,8,-10,2,-5,-6,1,-6,2,-9,-7,10,4,4,-10,8,4,-2,8,-4,6,-7,-6,10,-4,-3,-1,9,-2,-5,-3,-4,2,-3,-8,1,-5,-5,-3,8,-5,-8,-1,4,-7], dtype = "int32")#candidate|20073|(728,)|const|int32
var_20074 = relay.var("var_20074", dtype = "float32", shape = (150,))#candidate|20074|(150,)|var|float32
call_20072 = relay.TupleGetItem(func_5133_call(relay.reshape(const_20073.astype('int32'), [4, 14, 13]), relay.reshape(var_20074.astype('float32'), [25, 6]), ), 1)
call_20075 = relay.TupleGetItem(func_5137_call(relay.reshape(const_20073.astype('int32'), [4, 14, 13]), relay.reshape(var_20074.astype('float32'), [25, 6]), ), 1)
output = relay.Tuple([call_20052,call_20072,const_20073,var_20074,])
output2 = relay.Tuple([call_20053,call_20075,const_20073,var_20074,])
func_20081 = relay.Function([var_20074,], output)
mod['func_20081'] = func_20081
mod = relay.transform.InferType()(mod)
mutated_mod['func_20081'] = func_20081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20082 = relay.var("var_20082", dtype = "float32", shape = (150,))#candidate|20082|(150,)|var|float32
func_20081_call = mutated_mod.get_global_var('func_20081')
call_20083 = func_20081_call(var_20082)
output = call_20083
func_20084 = relay.Function([var_20082], output)
mutated_mod['func_20084'] = func_20084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18795_call = mod.get_global_var('func_18795')
func_18797_call = mutated_mod.get_global_var('func_18797')
call_20114 = func_18795_call()
call_20115 = func_18795_call()
func_9541_call = mod.get_global_var('func_9541')
func_9544_call = mutated_mod.get_global_var('func_9544')
const_20129 = relay.const([2,7,6,8,-5,-10,3,1,-10,-8,-1,7,4,9,4,7,-7,-3,-6,-8,9,3,-5,-1,7,-7,10,6,-6,7,-2,-5,9,-3,-8,-3,-10,1,3,10,3,-8,1,-9,10,6,-8,-2,-10,1,-7,7,3,5,-1,-7,2,7,1,8,-2,5,7,7,2,7,2,-9,3,-2,8,-1], dtype = "uint8")#candidate|20129|(72,)|const|uint8
call_20128 = relay.TupleGetItem(func_9541_call(relay.reshape(const_20129.astype('uint8'), [72,])), 2)
call_20130 = relay.TupleGetItem(func_9544_call(relay.reshape(const_20129.astype('uint8'), [72,])), 2)
func_12479_call = mod.get_global_var('func_12479')
func_12481_call = mutated_mod.get_global_var('func_12481')
call_20154 = relay.TupleGetItem(func_12479_call(), 0)
call_20155 = relay.TupleGetItem(func_12481_call(), 0)
output = relay.Tuple([call_20114,call_20128,const_20129,call_20154,])
output2 = relay.Tuple([call_20115,call_20130,const_20129,call_20155,])
func_20157 = relay.Function([], output)
mod['func_20157'] = func_20157
mod = relay.transform.InferType()(mod)
mutated_mod['func_20157'] = func_20157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20157_call = mutated_mod.get_global_var('func_20157')
call_20158 = func_20157_call()
output = call_20158
func_20159 = relay.Function([], output)
mutated_mod['func_20159'] = func_20159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19295_call = mod.get_global_var('func_19295')
func_19296_call = mutated_mod.get_global_var('func_19296')
call_20216 = relay.TupleGetItem(func_19295_call(), 0)
call_20217 = relay.TupleGetItem(func_19296_call(), 0)
func_11807_call = mod.get_global_var('func_11807')
func_11808_call = mutated_mod.get_global_var('func_11808')
call_20219 = relay.TupleGetItem(func_11807_call(), 0)
call_20220 = relay.TupleGetItem(func_11808_call(), 0)
output = relay.Tuple([call_20216,call_20219,])
output2 = relay.Tuple([call_20217,call_20220,])
func_20221 = relay.Function([], output)
mod['func_20221'] = func_20221
mod = relay.transform.InferType()(mod)
output = func_20221()
func_20222 = relay.Function([], output)
mutated_mod['func_20222'] = func_20222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12479_call = mod.get_global_var('func_12479')
func_12481_call = mutated_mod.get_global_var('func_12481')
call_20228 = relay.TupleGetItem(func_12479_call(), 0)
call_20229 = relay.TupleGetItem(func_12481_call(), 0)
output = relay.Tuple([call_20228,])
output2 = relay.Tuple([call_20229,])
func_20251 = relay.Function([], output)
mod['func_20251'] = func_20251
mod = relay.transform.InferType()(mod)
mutated_mod['func_20251'] = func_20251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20251_call = mutated_mod.get_global_var('func_20251')
call_20252 = func_20251_call()
output = call_20252
func_20253 = relay.Function([], output)
mutated_mod['func_20253'] = func_20253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7325_call = mod.get_global_var('func_7325')
func_7327_call = mutated_mod.get_global_var('func_7327')
call_20299 = relay.TupleGetItem(func_7325_call(), 1)
call_20300 = relay.TupleGetItem(func_7327_call(), 1)
func_10301_call = mod.get_global_var('func_10301')
func_10303_call = mutated_mod.get_global_var('func_10303')
call_20305 = func_10301_call()
call_20306 = func_10301_call()
func_18190_call = mod.get_global_var('func_18190')
func_18192_call = mutated_mod.get_global_var('func_18192')
var_20313 = relay.var("var_20313", dtype = "bool", shape = (208,))#candidate|20313|(208,)|var|bool
call_20312 = relay.TupleGetItem(func_18190_call(relay.reshape(var_20313.astype('bool'), [208,])), 1)
call_20314 = relay.TupleGetItem(func_18192_call(relay.reshape(var_20313.astype('bool'), [208,])), 1)
func_16630_call = mod.get_global_var('func_16630')
func_16631_call = mutated_mod.get_global_var('func_16631')
call_20326 = func_16630_call()
call_20327 = func_16630_call()
func_17182_call = mod.get_global_var('func_17182')
func_17185_call = mutated_mod.get_global_var('func_17185')
const_20344 = relay.const([-8.471160,-3.318034,-1.460721,5.716757,2.879935,0.465188,-1.653729,-4.545845,7.266885,2.158903,-1.403620,9.490818,-8.302616,5.299250,-8.294737,-4.671010,-3.834216,4.157910,9.502162,3.065285,3.896995,-5.723179,-8.664775,0.032629,-5.389521,0.206720,-2.168524,-5.091945,-6.947196,-1.207777,0.691669,1.287781,0.534114,-3.374341,-7.174669,4.558001,3.031139,3.595276,8.357988,2.971492,1.204762,-3.370239,1.164918,-0.493745,-1.929735,-6.669752,-2.894750,9.342211,0.456325,-1.276283,-9.457861,8.573980,9.312058,6.778651,7.929655,-3.084632,1.476270,9.492108,1.534871,7.078946,-7.188090,-9.553446,3.026469,8.544216,0.870808,-0.418953,1.436933,5.592432,1.842864,6.215264,-0.448095,3.736847,4.045472,-9.527051,4.926811,-0.513334,-8.487095,-1.169113,8.190978,-3.327427,4.524744,-2.313884,-4.450444,5.370545,-1.304301,8.808256,-5.133807,-6.992101,2.234412,-3.476611,-1.514413,-1.557151,0.919423,8.368152,-3.921108,-3.475410,-8.376305,7.908606,-3.378863,-9.628583,1.774570,4.628667,2.919804,9.739532,9.253399,7.052475,8.155675,-7.491871,-3.329565,1.534285,3.565121,-6.558901,-7.196597,-6.829792,-8.645157,7.792106,-7.358051,8.380715,-7.270732,-2.514627,-0.581712,-5.900408,-9.998637,1.976291,-0.403603,8.538068,-4.740770,5.627578,9.959028,8.477648,8.271293,-2.457111,-9.924541,0.859367,-1.144526,-2.370153,3.026393,-3.258964,0.518563,-5.286482,-4.266396,6.848674,6.653738,7.022249,-6.132360,-8.671699,6.737333,-2.324069,-7.956051,8.467013,6.801443,9.952612,-3.798261,-1.422518,5.153974,7.507202,8.527960,-0.273038,8.311245,7.766558,8.281389,7.632850,-7.803492,-1.168230,1.178020,-4.302600,9.282032,3.697679,9.507693,1.090322,-8.965509,3.261633,6.476217,-7.803823,6.699663,-6.035499,5.451323,-2.437366,7.256392,-7.478965,-4.882147,-1.245142,2.487869,6.588997,2.826528,4.653276,2.476325,4.848943,0.014361,8.717797,-5.678360,0.496742,-4.672951,5.708550,-0.518523,-2.293306,-3.282806,-2.290979,9.565245,1.590585,-6.531930,-3.345758,0.633546,-2.204092,-9.605580,0.399218,8.724558,-2.598535,-0.343829,-4.947413,-7.668579,3.859060,1.907373,-7.575186,9.398255,9.952988,-4.325333,5.440026,-7.466107,-3.951409,-1.824359,9.106799,-1.331678,1.748900,8.629884,2.482516,-1.515159,1.189271,-0.358041,-1.649027,4.611261,3.327681,-7.202367,5.339354,-2.418871,1.376706,0.742357,6.119402,-5.674492,8.086319,-9.847378,8.340300,0.125382,-7.045605,-5.929249,-2.920555,-4.514289,-4.194067,-4.078535,6.070662,1.281354,8.179335,6.506461,6.199683,5.776423,-6.726163,0.455052,5.766122,-5.958699,4.243917,-6.743235,-7.235369,5.847885,3.038484,-1.938942,4.257123,9.128594,-5.734397,2.036270,1.658705,-5.230183,-3.875768,5.229504,8.945267,8.200840,1.409670,-4.709649,-3.535574,-5.756081,9.178789,2.081661,-1.416151,-4.803958,4.962452,-2.104613,-1.090660,-8.114381,4.896728,-7.177453,4.296969,1.294920,-4.366112,-5.874670,7.891332,-3.333184,3.764215,1.990154,2.799006,8.197995,3.238495,0.528078,-4.215760,-1.111208,7.618741,-3.048784,-9.510806,1.321013,6.859592,-0.946731,-8.791427,-3.986778,-4.731618,-8.757760,6.895724,-0.353610,3.704685,-6.259149,-6.900313,2.888806,-3.272121,-5.364859,6.033411,3.935338,-9.503951,-8.758235,-6.789024,-7.310481,-6.268389,-7.644686,-9.151377,6.013735,-2.566662,-5.233000,-8.365653,2.449936,6.717081,-5.807540,9.024580,-4.429870,0.427166,0.258304,8.609835,-8.747640,-5.692647,7.511250,9.528402,-7.213805,-7.699255,-0.228999,0.219688,1.319812,-6.324488,1.046152,2.783725,2.688308,-0.415162,8.706205,-1.059627,-9.924299,-3.276703,-8.579032,-3.882459,-7.403623,8.291042,2.372130,-5.689607,4.298112,-0.389207,-7.289727,-1.933024,-8.302566,-1.527093,-8.596785,5.783312,6.982422,-9.513925,-9.794625,3.252528,-7.229748,0.380589,4.701272,-8.876069,-1.011927,8.241763,5.926542,-8.815485,6.000345,9.599276,-0.335987,-2.482979,-6.267234,6.174885], dtype = "float32")#candidate|20344|(392,)|const|float32
call_20343 = relay.TupleGetItem(func_17182_call(relay.reshape(const_20344.astype('float32'), [14, 7, 4])), 1)
call_20345 = relay.TupleGetItem(func_17185_call(relay.reshape(const_20344.astype('float32'), [14, 7, 4])), 1)
func_11569_call = mod.get_global_var('func_11569')
func_11570_call = mutated_mod.get_global_var('func_11570')
call_20364 = relay.TupleGetItem(func_11569_call(), 2)
call_20365 = relay.TupleGetItem(func_11570_call(), 2)
output = relay.Tuple([call_20299,call_20305,call_20312,var_20313,call_20326,call_20343,const_20344,call_20364,])
output2 = relay.Tuple([call_20300,call_20306,call_20314,var_20313,call_20327,call_20345,const_20344,call_20365,])
func_20384 = relay.Function([var_20313,], output)
mod['func_20384'] = func_20384
mod = relay.transform.InferType()(mod)
mutated_mod['func_20384'] = func_20384
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20385 = relay.var("var_20385", dtype = "bool", shape = (208,))#candidate|20385|(208,)|var|bool
func_20384_call = mutated_mod.get_global_var('func_20384')
call_20386 = func_20384_call(var_20385)
output = call_20386
func_20387 = relay.Function([var_20385], output)
mutated_mod['func_20387'] = func_20387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8947_call = mod.get_global_var('func_8947')
func_8949_call = mutated_mod.get_global_var('func_8949')
call_20450 = relay.TupleGetItem(func_8947_call(), 0)
call_20451 = relay.TupleGetItem(func_8949_call(), 0)
func_7975_call = mod.get_global_var('func_7975')
func_7979_call = mutated_mod.get_global_var('func_7979')
var_20504 = relay.var("var_20504", dtype = "float32", shape = (300, 2))#candidate|20504|(300, 2)|var|float32
const_20505 = relay.const([False,False,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False], dtype = "bool")#candidate|20505|(208,)|const|bool
call_20503 = relay.TupleGetItem(func_7975_call(relay.reshape(var_20504.astype('float32'), [1, 600]), relay.reshape(const_20505.astype('bool'), [208,]), ), 3)
call_20506 = relay.TupleGetItem(func_7979_call(relay.reshape(var_20504.astype('float32'), [1, 600]), relay.reshape(const_20505.astype('bool'), [208,]), ), 3)
output = relay.Tuple([call_20450,call_20503,var_20504,const_20505,])
output2 = relay.Tuple([call_20451,call_20506,var_20504,const_20505,])
func_20507 = relay.Function([var_20504,], output)
mod['func_20507'] = func_20507
mod = relay.transform.InferType()(mod)
var_20508 = relay.var("var_20508", dtype = "float32", shape = (300, 2))#candidate|20508|(300, 2)|var|float32
output = func_20507(var_20508)
func_20509 = relay.Function([var_20508], output)
mutated_mod['func_20509'] = func_20509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8292_call = mod.get_global_var('func_8292')
func_8293_call = mutated_mod.get_global_var('func_8293')
call_20555 = func_8292_call()
call_20556 = func_8292_call()
output = call_20555
output2 = call_20556
func_20582 = relay.Function([], output)
mod['func_20582'] = func_20582
mod = relay.transform.InferType()(mod)
mutated_mod['func_20582'] = func_20582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20582_call = mutated_mod.get_global_var('func_20582')
call_20583 = func_20582_call()
output = call_20583
func_20584 = relay.Function([], output)
mutated_mod['func_20584'] = func_20584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10872_call = mod.get_global_var('func_10872')
func_10873_call = mutated_mod.get_global_var('func_10873')
call_20735 = relay.TupleGetItem(func_10872_call(), 0)
call_20736 = relay.TupleGetItem(func_10873_call(), 0)
func_10462_call = mod.get_global_var('func_10462')
func_10464_call = mutated_mod.get_global_var('func_10464')
call_20744 = func_10462_call()
call_20745 = func_10462_call()
output = relay.Tuple([call_20735,call_20744,])
output2 = relay.Tuple([call_20736,call_20745,])
func_20764 = relay.Function([], output)
mod['func_20764'] = func_20764
mod = relay.transform.InferType()(mod)
output = func_20764()
func_20765 = relay.Function([], output)
mutated_mod['func_20765'] = func_20765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_20773 = relay.TupleGetItem(func_7413_call(), 0)
call_20774 = relay.TupleGetItem(func_7415_call(), 0)
func_17041_call = mod.get_global_var('func_17041')
func_17042_call = mutated_mod.get_global_var('func_17042')
call_20779 = relay.TupleGetItem(func_17041_call(), 0)
call_20780 = relay.TupleGetItem(func_17042_call(), 0)
output = relay.Tuple([call_20773,call_20779,])
output2 = relay.Tuple([call_20774,call_20780,])
func_20781 = relay.Function([], output)
mod['func_20781'] = func_20781
mod = relay.transform.InferType()(mod)
output = func_20781()
func_20782 = relay.Function([], output)
mutated_mod['func_20782'] = func_20782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18385_call = mod.get_global_var('func_18385')
func_18387_call = mutated_mod.get_global_var('func_18387')
call_20816 = func_18385_call()
call_20817 = func_18385_call()
output = call_20816
output2 = call_20817
func_20836 = relay.Function([], output)
mod['func_20836'] = func_20836
mod = relay.transform.InferType()(mod)
mutated_mod['func_20836'] = func_20836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20836_call = mutated_mod.get_global_var('func_20836')
call_20837 = func_20836_call()
output = call_20837
func_20838 = relay.Function([], output)
mutated_mod['func_20838'] = func_20838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18657_call = mod.get_global_var('func_18657')
func_18659_call = mutated_mod.get_global_var('func_18659')
call_20841 = relay.TupleGetItem(func_18657_call(), 1)
call_20842 = relay.TupleGetItem(func_18659_call(), 1)
func_6087_call = mod.get_global_var('func_6087')
func_6090_call = mutated_mod.get_global_var('func_6090')
var_20847 = relay.var("var_20847", dtype = "float32", shape = (66,))#candidate|20847|(66,)|var|float32
call_20846 = relay.TupleGetItem(func_6087_call(relay.reshape(var_20847.astype('float32'), [1, 11, 6])), 0)
call_20848 = relay.TupleGetItem(func_6090_call(relay.reshape(var_20847.astype('float32'), [1, 11, 6])), 0)
bop_20860 = relay.bitwise_or(call_20846.astype('uint32'), relay.reshape(var_20847.astype('uint32'), relay.shape_of(call_20846))) # shape=(1, 11, 6)
bop_20863 = relay.bitwise_or(call_20848.astype('uint32'), relay.reshape(var_20847.astype('uint32'), relay.shape_of(call_20848))) # shape=(1, 11, 6)
bop_20865 = relay.logical_xor(bop_20860.astype('uint16'), relay.reshape(call_20846.astype('uint16'), relay.shape_of(bop_20860))) # shape=(1, 11, 6)
bop_20868 = relay.logical_xor(bop_20863.astype('uint16'), relay.reshape(call_20848.astype('uint16'), relay.shape_of(bop_20863))) # shape=(1, 11, 6)
output = relay.Tuple([call_20841,bop_20865,])
output2 = relay.Tuple([call_20842,bop_20868,])
func_20871 = relay.Function([var_20847,], output)
mod['func_20871'] = func_20871
mod = relay.transform.InferType()(mod)
mutated_mod['func_20871'] = func_20871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20872 = relay.var("var_20872", dtype = "float32", shape = (66,))#candidate|20872|(66,)|var|float32
func_20871_call = mutated_mod.get_global_var('func_20871')
call_20873 = func_20871_call(var_20872)
output = call_20873
func_20874 = relay.Function([var_20872], output)
mutated_mod['func_20874'] = func_20874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19699_call = mod.get_global_var('func_19699')
func_19700_call = mutated_mod.get_global_var('func_19700')
call_20899 = relay.TupleGetItem(func_19699_call(), 0)
call_20900 = relay.TupleGetItem(func_19700_call(), 0)
func_11367_call = mod.get_global_var('func_11367')
func_11368_call = mutated_mod.get_global_var('func_11368')
call_20912 = relay.TupleGetItem(func_11367_call(), 0)
call_20913 = relay.TupleGetItem(func_11368_call(), 0)
func_19958_call = mod.get_global_var('func_19958')
func_19960_call = mutated_mod.get_global_var('func_19960')
call_20914 = relay.TupleGetItem(func_19958_call(), 2)
call_20915 = relay.TupleGetItem(func_19960_call(), 2)
output = relay.Tuple([call_20899,call_20912,call_20914,])
output2 = relay.Tuple([call_20900,call_20913,call_20915,])
func_20929 = relay.Function([], output)
mod['func_20929'] = func_20929
mod = relay.transform.InferType()(mod)
mutated_mod['func_20929'] = func_20929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20929_call = mutated_mod.get_global_var('func_20929')
call_20930 = func_20929_call()
output = call_20930
func_20931 = relay.Function([], output)
mutated_mod['func_20931'] = func_20931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20157_call = mod.get_global_var('func_20157')
func_20159_call = mutated_mod.get_global_var('func_20159')
call_20937 = relay.TupleGetItem(func_20157_call(), 3)
call_20938 = relay.TupleGetItem(func_20159_call(), 3)
output = relay.Tuple([call_20937,])
output2 = relay.Tuple([call_20938,])
func_20950 = relay.Function([], output)
mod['func_20950'] = func_20950
mod = relay.transform.InferType()(mod)
mutated_mod['func_20950'] = func_20950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20950_call = mutated_mod.get_global_var('func_20950')
call_20951 = func_20950_call()
output = call_20951
func_20952 = relay.Function([], output)
mutated_mod['func_20952'] = func_20952
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20953 = relay.var("var_20953", dtype = "uint8", shape = (12, 15, 8))#candidate|20953|(12, 15, 8)|var|uint8
var_20954 = relay.var("var_20954", dtype = "uint8", shape = (12, 15, 8))#candidate|20954|(12, 15, 8)|var|uint8
bop_20955 = relay.bitwise_xor(var_20953.astype('uint8'), relay.reshape(var_20954.astype('uint8'), relay.shape_of(var_20953))) # shape=(12, 15, 8)
uop_20961 = relay.sigmoid(var_20954.astype('float64')) # shape=(12, 15, 8)
func_14533_call = mod.get_global_var('func_14533')
func_14535_call = mutated_mod.get_global_var('func_14535')
call_20963 = relay.TupleGetItem(func_14533_call(), 0)
call_20964 = relay.TupleGetItem(func_14535_call(), 0)
func_20221_call = mod.get_global_var('func_20221')
func_20222_call = mutated_mod.get_global_var('func_20222')
call_20985 = relay.TupleGetItem(func_20221_call(), 0)
call_20986 = relay.TupleGetItem(func_20222_call(), 0)
output = relay.Tuple([bop_20955,uop_20961,call_20963,call_20985,])
output2 = relay.Tuple([bop_20955,uop_20961,call_20964,call_20986,])
func_20990 = relay.Function([var_20953,var_20954,], output)
mod['func_20990'] = func_20990
mod = relay.transform.InferType()(mod)
mutated_mod['func_20990'] = func_20990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20990_call = mutated_mod.get_global_var('func_20990')
var_20992 = relay.var("var_20992", dtype = "uint8", shape = (12, 15, 8))#candidate|20992|(12, 15, 8)|var|uint8
var_20993 = relay.var("var_20993", dtype = "uint8", shape = (12, 15, 8))#candidate|20993|(12, 15, 8)|var|uint8
call_20991 = func_20990_call(var_20992,var_20993,)
output = call_20991
func_20994 = relay.Function([var_20992,var_20993,], output)
mutated_mod['func_20994'] = func_20994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9363_call = mod.get_global_var('func_9363')
func_9365_call = mutated_mod.get_global_var('func_9365')
call_21003 = relay.TupleGetItem(func_9363_call(), 0)
call_21004 = relay.TupleGetItem(func_9365_call(), 0)
func_14664_call = mod.get_global_var('func_14664')
func_14667_call = mutated_mod.get_global_var('func_14667')
const_21006 = relay.const([[0.439016,-2.485938,-6.049461,-0.052258,-4.428743,3.140857,-9.393593,3.926350,-6.938774,-5.330192,-7.933960,-1.858524,3.045375,5.466521,-2.499740,2.224023,-7.724951,-2.790643,2.502789,-0.513228,-2.953560,-1.620238,8.633260,6.105901,4.759084,4.714665,4.852406,3.994614,2.584036,-5.849226],[-7.263875,2.683737,7.503662,8.472047,-5.135542,3.637632,3.857275,9.926526,3.212490,5.190764,-5.610465,-7.022660,-7.376784,9.124086,5.962746,0.800966,5.212153,-0.334501,-7.637368,8.489250,1.767914,4.501426,6.956329,9.803012,-2.758119,8.772580,6.665381,-4.496894,-9.514733,8.198186],[1.099461,7.312501,2.576349,2.436415,8.977373,-1.111492,2.853991,1.784069,-6.849000,-1.848061,4.681013,-6.876698,0.562088,0.630802,-7.392115,4.760668,8.112942,-6.342973,0.533169,8.529015,5.277945,9.520681,7.349190,8.835758,-1.819204,-2.951904,0.438368,-8.755660,7.800120,-1.099117],[7.780102,7.017125,-1.160080,9.657633,-8.778316,-6.002213,0.169350,-4.196411,3.735966,-8.991545,8.345541,5.058109,1.696286,-4.534557,7.704293,-3.487273,-9.835060,-6.751715,-0.443763,-0.485924,-7.920193,-2.133091,7.494726,-0.518237,-4.895617,-6.890078,-7.664668,-9.398419,7.033239,-4.142859],[-5.618655,1.445785,0.344581,2.348633,-8.192334,-5.045673,4.153665,-4.275695,2.934543,8.910845,6.427270,-9.926883,4.127053,-0.541440,3.729121,-5.144531,1.202821,-6.360341,8.318699,-5.047515,-8.555806,-4.929700,9.700868,-4.118828,4.714190,-7.512660,1.998002,-1.592978,-6.115388,4.793321],[-7.139452,4.103749,-6.152752,-5.163399,4.512021,0.475228,9.760766,4.400384,-6.896815,1.415385,5.101848,-0.081696,-7.903649,-6.607347,7.618384,-1.144046,3.370791,-6.455857,-2.590255,1.865988,8.350315,6.100812,-4.958777,-7.477241,-7.238998,-7.027471,5.641643,-1.188088,-4.246648,-5.178501]], dtype = "float64")#candidate|21006|(6, 30)|const|float64
var_21007 = relay.var("var_21007", dtype = "float64", shape = (1800,))#candidate|21007|(1800,)|var|float64
call_21005 = relay.TupleGetItem(func_14664_call(relay.reshape(const_21006.astype('float64'), [12, 15, 1]), relay.reshape(var_21007.astype('float64'), [12, 15, 10]), ), 0)
call_21008 = relay.TupleGetItem(func_14667_call(relay.reshape(const_21006.astype('float64'), [12, 15, 1]), relay.reshape(var_21007.astype('float64'), [12, 15, 10]), ), 0)
func_14980_call = mod.get_global_var('func_14980')
func_14981_call = mutated_mod.get_global_var('func_14981')
call_21009 = relay.TupleGetItem(func_14980_call(), 1)
call_21010 = relay.TupleGetItem(func_14981_call(), 1)
func_9363_call = mod.get_global_var('func_9363')
func_9365_call = mutated_mod.get_global_var('func_9365')
call_21018 = relay.TupleGetItem(func_9363_call(), 0)
call_21019 = relay.TupleGetItem(func_9365_call(), 0)
func_15746_call = mod.get_global_var('func_15746')
func_15749_call = mutated_mod.get_global_var('func_15749')
var_21021 = relay.var("var_21021", dtype = "uint8", shape = ())#candidate|21021|()|var|uint8
call_21020 = relay.TupleGetItem(func_15746_call(relay.reshape(var_21021.astype('uint8'), [])), 4)
call_21022 = relay.TupleGetItem(func_15749_call(relay.reshape(var_21021.astype('uint8'), [])), 4)
output = relay.Tuple([call_21003,call_21005,const_21006,var_21007,call_21009,call_21018,call_21020,var_21021,])
output2 = relay.Tuple([call_21004,call_21008,const_21006,var_21007,call_21010,call_21019,call_21022,var_21021,])
func_21023 = relay.Function([var_21007,var_21021,], output)
mod['func_21023'] = func_21023
mod = relay.transform.InferType()(mod)
mutated_mod['func_21023'] = func_21023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21023_call = mutated_mod.get_global_var('func_21023')
var_21025 = relay.var("var_21025", dtype = "float64", shape = (1800,))#candidate|21025|(1800,)|var|float64
var_21026 = relay.var("var_21026", dtype = "uint8", shape = ())#candidate|21026|()|var|uint8
call_21024 = func_21023_call(var_21025,var_21026,)
output = call_21024
func_21027 = relay.Function([var_21025,var_21026,], output)
mutated_mod['func_21027'] = func_21027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20582_call = mod.get_global_var('func_20582')
func_20584_call = mutated_mod.get_global_var('func_20584')
call_21058 = func_20582_call()
call_21059 = func_20582_call()
func_6087_call = mod.get_global_var('func_6087')
func_6090_call = mutated_mod.get_global_var('func_6090')
var_21069 = relay.var("var_21069", dtype = "float32", shape = (66,))#candidate|21069|(66,)|var|float32
call_21068 = relay.TupleGetItem(func_6087_call(relay.reshape(var_21069.astype('float32'), [1, 11, 6])), 0)
call_21070 = relay.TupleGetItem(func_6090_call(relay.reshape(var_21069.astype('float32'), [1, 11, 6])), 0)
output = relay.Tuple([call_21058,call_21068,var_21069,])
output2 = relay.Tuple([call_21059,call_21070,var_21069,])
func_21076 = relay.Function([var_21069,], output)
mod['func_21076'] = func_21076
mod = relay.transform.InferType()(mod)
mutated_mod['func_21076'] = func_21076
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21077 = relay.var("var_21077", dtype = "float32", shape = (66,))#candidate|21077|(66,)|var|float32
func_21076_call = mutated_mod.get_global_var('func_21076')
call_21078 = func_21076_call(var_21077)
output = call_21078
func_21079 = relay.Function([var_21077], output)
mutated_mod['func_21079'] = func_21079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16778_call = mod.get_global_var('func_16778')
func_16780_call = mutated_mod.get_global_var('func_16780')
call_21094 = relay.TupleGetItem(func_16778_call(), 0)
call_21095 = relay.TupleGetItem(func_16780_call(), 0)
output = relay.Tuple([call_21094,])
output2 = relay.Tuple([call_21095,])
func_21096 = relay.Function([], output)
mod['func_21096'] = func_21096
mod = relay.transform.InferType()(mod)
mutated_mod['func_21096'] = func_21096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21096_call = mutated_mod.get_global_var('func_21096')
call_21097 = func_21096_call()
output = call_21097
func_21098 = relay.Function([], output)
mutated_mod['func_21098'] = func_21098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12631_call = mod.get_global_var('func_12631')
func_12633_call = mutated_mod.get_global_var('func_12633')
call_21142 = func_12631_call()
call_21143 = func_12631_call()
output = relay.Tuple([call_21142,])
output2 = relay.Tuple([call_21143,])
func_21186 = relay.Function([], output)
mod['func_21186'] = func_21186
mod = relay.transform.InferType()(mod)
output = func_21186()
func_21187 = relay.Function([], output)
mutated_mod['func_21187'] = func_21187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11287_call = mod.get_global_var('func_11287')
func_11289_call = mutated_mod.get_global_var('func_11289')
call_21251 = func_11287_call()
call_21252 = func_11287_call()
func_19427_call = mod.get_global_var('func_19427')
func_19429_call = mutated_mod.get_global_var('func_19429')
call_21255 = relay.TupleGetItem(func_19427_call(), 0)
call_21256 = relay.TupleGetItem(func_19429_call(), 0)
func_9575_call = mod.get_global_var('func_9575')
func_9576_call = mutated_mod.get_global_var('func_9576')
call_21257 = func_9575_call()
call_21258 = func_9575_call()
func_9827_call = mod.get_global_var('func_9827')
func_9828_call = mutated_mod.get_global_var('func_9828')
call_21264 = func_9827_call()
call_21265 = func_9827_call()
func_14930_call = mod.get_global_var('func_14930')
func_14932_call = mutated_mod.get_global_var('func_14932')
call_21267 = relay.TupleGetItem(func_14930_call(), 0)
call_21268 = relay.TupleGetItem(func_14932_call(), 0)
func_17412_call = mod.get_global_var('func_17412')
func_17414_call = mutated_mod.get_global_var('func_17414')
call_21283 = relay.TupleGetItem(func_17412_call(), 0)
call_21284 = relay.TupleGetItem(func_17414_call(), 0)
func_19130_call = mod.get_global_var('func_19130')
func_19132_call = mutated_mod.get_global_var('func_19132')
call_21290 = relay.TupleGetItem(func_19130_call(), 0)
call_21291 = relay.TupleGetItem(func_19132_call(), 0)
func_17041_call = mod.get_global_var('func_17041')
func_17042_call = mutated_mod.get_global_var('func_17042')
call_21310 = relay.TupleGetItem(func_17041_call(), 0)
call_21311 = relay.TupleGetItem(func_17042_call(), 0)
func_10612_call = mod.get_global_var('func_10612')
func_10614_call = mutated_mod.get_global_var('func_10614')
call_21314 = relay.TupleGetItem(func_10612_call(), 0)
call_21315 = relay.TupleGetItem(func_10614_call(), 0)
output = relay.Tuple([call_21251,call_21255,call_21257,call_21264,call_21267,call_21283,call_21290,call_21310,call_21314,])
output2 = relay.Tuple([call_21252,call_21256,call_21258,call_21265,call_21268,call_21284,call_21291,call_21311,call_21315,])
func_21316 = relay.Function([], output)
mod['func_21316'] = func_21316
mod = relay.transform.InferType()(mod)
mutated_mod['func_21316'] = func_21316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21316_call = mutated_mod.get_global_var('func_21316')
call_21317 = func_21316_call()
output = call_21317
func_21318 = relay.Function([], output)
mutated_mod['func_21318'] = func_21318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10961_call = mod.get_global_var('func_10961')
func_10963_call = mutated_mod.get_global_var('func_10963')
call_21429 = func_10961_call()
call_21430 = func_10961_call()
output = relay.Tuple([call_21429,])
output2 = relay.Tuple([call_21430,])
func_21436 = relay.Function([], output)
mod['func_21436'] = func_21436
mod = relay.transform.InferType()(mod)
mutated_mod['func_21436'] = func_21436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21436_call = mutated_mod.get_global_var('func_21436')
call_21437 = func_21436_call()
output = call_21437
func_21438 = relay.Function([], output)
mutated_mod['func_21438'] = func_21438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16378_call = mod.get_global_var('func_16378')
func_16379_call = mutated_mod.get_global_var('func_16379')
call_21463 = relay.TupleGetItem(func_16378_call(), 0)
call_21464 = relay.TupleGetItem(func_16379_call(), 0)
output = call_21463
output2 = call_21464
func_21466 = relay.Function([], output)
mod['func_21466'] = func_21466
mod = relay.transform.InferType()(mod)
output = func_21466()
func_21467 = relay.Function([], output)
mutated_mod['func_21467'] = func_21467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19077_call = mod.get_global_var('func_19077')
func_19078_call = mutated_mod.get_global_var('func_19078')
call_21496 = relay.TupleGetItem(func_19077_call(), 1)
call_21497 = relay.TupleGetItem(func_19078_call(), 1)
func_11569_call = mod.get_global_var('func_11569')
func_11570_call = mutated_mod.get_global_var('func_11570')
call_21499 = relay.TupleGetItem(func_11569_call(), 0)
call_21500 = relay.TupleGetItem(func_11570_call(), 0)
output = relay.Tuple([call_21496,call_21499,])
output2 = relay.Tuple([call_21497,call_21500,])
func_21516 = relay.Function([], output)
mod['func_21516'] = func_21516
mod = relay.transform.InferType()(mod)
output = func_21516()
func_21517 = relay.Function([], output)
mutated_mod['func_21517'] = func_21517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9620_call = mod.get_global_var('func_9620')
func_9622_call = mutated_mod.get_global_var('func_9622')
call_21557 = relay.TupleGetItem(func_9620_call(), 0)
call_21558 = relay.TupleGetItem(func_9622_call(), 0)
output = relay.Tuple([call_21557,])
output2 = relay.Tuple([call_21558,])
func_21569 = relay.Function([], output)
mod['func_21569'] = func_21569
mod = relay.transform.InferType()(mod)
output = func_21569()
func_21570 = relay.Function([], output)
mutated_mod['func_21570'] = func_21570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21574 = relay.var("var_21574", dtype = "float64", shape = (10, 15, 6))#candidate|21574|(10, 15, 6)|var|float64
uop_21575 = relay.cos(var_21574.astype('float64')) # shape=(10, 15, 6)
output = uop_21575
output2 = uop_21575
func_21584 = relay.Function([var_21574,], output)
mod['func_21584'] = func_21584
mod = relay.transform.InferType()(mod)
var_21585 = relay.var("var_21585", dtype = "float64", shape = (10, 15, 6))#candidate|21585|(10, 15, 6)|var|float64
output = func_21584(var_21585)
func_21586 = relay.Function([var_21585], output)
mutated_mod['func_21586'] = func_21586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17286_call = mod.get_global_var('func_17286')
func_17288_call = mutated_mod.get_global_var('func_17288')
call_21588 = func_17286_call()
call_21589 = func_17286_call()
output = call_21588
output2 = call_21589
func_21602 = relay.Function([], output)
mod['func_21602'] = func_21602
mod = relay.transform.InferType()(mod)
output = func_21602()
func_21603 = relay.Function([], output)
mutated_mod['func_21603'] = func_21603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14375_call = mod.get_global_var('func_14375')
func_14377_call = mutated_mod.get_global_var('func_14377')
call_21652 = relay.TupleGetItem(func_14375_call(), 0)
call_21653 = relay.TupleGetItem(func_14377_call(), 0)
func_10168_call = mod.get_global_var('func_10168')
func_10171_call = mutated_mod.get_global_var('func_10171')
var_21658 = relay.var("var_21658", dtype = "float32", shape = ())#candidate|21658|()|var|float32
call_21657 = func_10168_call(relay.reshape(var_21658.astype('float32'), []))
call_21659 = func_10168_call(relay.reshape(var_21658.astype('float32'), []))
func_8984_call = mod.get_global_var('func_8984')
func_8986_call = mutated_mod.get_global_var('func_8986')
var_21668 = relay.var("var_21668", dtype = "float32", shape = (150,))#candidate|21668|(150,)|var|float32
call_21667 = relay.TupleGetItem(func_8984_call(relay.reshape(var_21668.astype('float32'), [150,])), 2)
call_21669 = relay.TupleGetItem(func_8986_call(relay.reshape(var_21668.astype('float32'), [150,])), 2)
output = relay.Tuple([call_21652,call_21657,var_21658,call_21667,var_21668,])
output2 = relay.Tuple([call_21653,call_21659,var_21658,call_21669,var_21668,])
func_21690 = relay.Function([var_21658,var_21668,], output)
mod['func_21690'] = func_21690
mod = relay.transform.InferType()(mod)
mutated_mod['func_21690'] = func_21690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21690_call = mutated_mod.get_global_var('func_21690')
var_21692 = relay.var("var_21692", dtype = "float32", shape = ())#candidate|21692|()|var|float32
var_21693 = relay.var("var_21693", dtype = "float32", shape = (150,))#candidate|21693|(150,)|var|float32
call_21691 = func_21690_call(var_21692,var_21693,)
output = call_21691
func_21694 = relay.Function([var_21692,var_21693,], output)
mutated_mod['func_21694'] = func_21694
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21696 = relay.var("var_21696", dtype = "float32", shape = (11, 3, 6))#candidate|21696|(11, 3, 6)|var|float32
uop_21697 = relay.acos(var_21696.astype('float32')) # shape=(11, 3, 6)
output = uop_21697
output2 = uop_21697
func_21701 = relay.Function([var_21696,], output)
mod['func_21701'] = func_21701
mod = relay.transform.InferType()(mod)
mutated_mod['func_21701'] = func_21701
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21702 = relay.var("var_21702", dtype = "float32", shape = (11, 3, 6))#candidate|21702|(11, 3, 6)|var|float32
func_21701_call = mutated_mod.get_global_var('func_21701')
call_21703 = func_21701_call(var_21702)
output = call_21703
func_21704 = relay.Function([var_21702], output)
mutated_mod['func_21704'] = func_21704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20582_call = mod.get_global_var('func_20582')
func_20584_call = mutated_mod.get_global_var('func_20584')
call_21711 = func_20582_call()
call_21712 = func_20582_call()
output = call_21711
output2 = call_21712
func_21720 = relay.Function([], output)
mod['func_21720'] = func_21720
mod = relay.transform.InferType()(mod)
mutated_mod['func_21720'] = func_21720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21720_call = mutated_mod.get_global_var('func_21720')
call_21721 = func_21720_call()
output = call_21721
func_21722 = relay.Function([], output)
mutated_mod['func_21722'] = func_21722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14192_call = mod.get_global_var('func_14192')
func_14194_call = mutated_mod.get_global_var('func_14194')
call_21729 = relay.TupleGetItem(func_14192_call(), 1)
call_21730 = relay.TupleGetItem(func_14194_call(), 1)
output = call_21729
output2 = call_21730
func_21731 = relay.Function([], output)
mod['func_21731'] = func_21731
mod = relay.transform.InferType()(mod)
mutated_mod['func_21731'] = func_21731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21731_call = mutated_mod.get_global_var('func_21731')
call_21732 = func_21731_call()
output = call_21732
func_21733 = relay.Function([], output)
mutated_mod['func_21733'] = func_21733
mutated_mod = relay.transform.InferType()(mutated_mod)
const_21756 = relay.const([[[True,True,False,True,True,False],[True,False,True,False,False,False],[False,False,True,False,True,True],[True,False,False,False,False,True],[True,True,False,False,True,True],[True,False,False,True,True,True],[False,True,False,True,True,False],[True,True,True,False,True,False],[False,False,True,False,True,True],[True,False,False,False,True,True],[True,False,True,False,True,False],[True,True,True,True,True,False],[False,False,False,True,True,True]],[[True,True,False,False,True,True],[True,False,True,True,False,False],[False,False,False,True,False,False],[False,True,True,True,True,False],[False,True,True,False,False,False],[True,True,True,True,False,False],[False,True,False,False,True,True],[False,True,True,True,True,True],[True,True,False,False,False,True],[True,False,False,False,False,False],[False,False,False,True,True,False],[True,False,True,True,False,False],[False,False,False,True,True,True]],[[False,False,False,True,True,False],[False,False,True,True,False,True],[True,False,True,True,True,True],[True,False,True,True,True,True],[True,False,True,True,True,True],[False,False,True,False,True,False],[True,True,False,False,False,False],[True,False,False,True,True,True],[False,True,True,True,False,True],[False,True,True,True,True,False],[False,True,False,False,False,True],[False,True,True,True,True,True],[True,False,True,False,True,True]],[[True,True,False,True,False,False],[False,False,True,True,False,False],[True,False,False,False,False,False],[True,True,True,False,False,False],[False,True,False,True,True,False],[False,True,True,False,False,False],[False,False,False,False,True,False],[False,False,True,False,False,True],[False,False,False,True,False,False],[True,False,False,False,False,True],[False,False,False,True,True,False],[True,True,False,False,True,True],[False,False,False,True,False,False]],[[True,True,False,True,False,True],[False,False,True,False,False,True],[True,False,False,False,True,True],[False,True,False,True,True,False],[False,True,False,False,True,False],[True,False,True,True,True,False],[False,True,False,False,True,False],[True,True,False,True,True,True],[False,True,False,True,False,True],[True,True,True,True,True,False],[True,False,False,True,False,True],[True,False,True,True,False,False],[True,False,True,True,True,False]],[[False,False,False,True,True,False],[False,False,True,True,True,True],[True,False,True,True,True,True],[True,False,False,False,True,False],[False,False,False,False,True,False],[False,False,False,False,True,True],[True,True,True,False,True,False],[True,False,False,True,False,False],[False,True,False,False,True,False],[True,True,False,True,True,False],[True,False,False,True,False,True],[False,True,False,True,False,True],[True,True,False,False,False,False]],[[False,True,True,False,True,False],[False,False,True,True,False,True],[True,True,True,True,True,True],[False,True,True,False,True,True],[False,False,False,False,False,True],[False,False,False,True,True,True],[True,True,False,False,False,False],[True,True,True,False,False,False],[False,False,False,True,True,True],[False,True,True,False,True,False],[True,True,False,True,False,True],[True,True,True,True,True,True],[True,True,True,False,True,True]],[[True,True,False,True,False,True],[False,False,False,True,True,True],[True,False,False,False,False,False],[True,True,True,False,False,False],[False,True,True,True,True,True],[False,False,False,False,True,True],[True,True,True,True,True,False],[False,False,True,False,False,True],[False,False,False,True,False,False],[False,False,True,True,True,False],[False,False,True,True,False,False],[False,False,False,True,True,True],[False,False,True,True,False,False]]], dtype = "bool")#candidate|21756|(8, 13, 6)|const|bool
var_21757 = relay.var("var_21757", dtype = "bool", shape = (8, 13, 6))#candidate|21757|(8, 13, 6)|var|bool
bop_21758 = relay.logical_and(const_21756.astype('bool'), relay.reshape(var_21757.astype('bool'), relay.shape_of(const_21756))) # shape=(8, 13, 6)
output = relay.Tuple([bop_21758,])
output2 = relay.Tuple([bop_21758,])
func_21775 = relay.Function([var_21757,], output)
mod['func_21775'] = func_21775
mod = relay.transform.InferType()(mod)
mutated_mod['func_21775'] = func_21775
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21776 = relay.var("var_21776", dtype = "bool", shape = (8, 13, 6))#candidate|21776|(8, 13, 6)|var|bool
func_21775_call = mutated_mod.get_global_var('func_21775')
call_21777 = func_21775_call(var_21776)
output = call_21777
func_21778 = relay.Function([var_21776], output)
mutated_mod['func_21778'] = func_21778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11701_call = mod.get_global_var('func_11701')
func_11703_call = mutated_mod.get_global_var('func_11703')
call_21814 = relay.TupleGetItem(func_11701_call(), 0)
call_21815 = relay.TupleGetItem(func_11703_call(), 0)
func_19077_call = mod.get_global_var('func_19077')
func_19078_call = mutated_mod.get_global_var('func_19078')
call_21816 = relay.TupleGetItem(func_19077_call(), 1)
call_21817 = relay.TupleGetItem(func_19078_call(), 1)
func_18741_call = mod.get_global_var('func_18741')
func_18745_call = mutated_mod.get_global_var('func_18745')
const_21835 = relay.const([6,10,4,4,-1,-4,8,8,-2,-3,-2,3,-10,10,-9,5,-9,-9,8,8,-8,-4,-6,6,-9,-4,-9,-1,-8,-4,5,2,8,-7,-5,-6,7,-9,-2,1,-6,-6,-4,6,5,-8,-3,6,-6,-8,8,-3,-3,8,-9,-1,-3,-4,2,-10,-1,-9,1,-6,8,7,7,3,-4,7,9,10], dtype = "uint8")#candidate|21835|(72,)|const|uint8
const_21836 = relay.const([3.402381,-8.375164,1.005470,-1.558942,0.654341,-6.272412,7.297605,-4.468355,4.644182,2.912442,-7.885288,-0.327524,-6.170444,5.051005,-0.604227,-5.047510,-0.988062,-2.456630,9.816340,-4.431439,-2.639714,-0.098532,3.565120,2.284685,-7.116043,3.138981,2.378982,-3.224254,5.700869,7.384799,-8.019410,2.200513,-5.920892,2.549935,0.399162,2.418337,-9.512151,5.664225,-3.307615,-8.706071,-2.668569,7.504865,7.483184,7.064904,1.695739,-2.926962,6.081132,-9.325459,6.540509,7.454903,7.613059,-0.114977,-4.684918,1.465691,-5.992614,-8.897880,8.059396,2.536423,2.856451,-1.180806,4.712148,-6.520209,-3.258502,5.251510,-9.788315,-9.274994,2.230181,5.582234,9.733845,-7.251402,-7.804582,-7.253626,-6.214329,-3.687198,-0.920657,-2.112518,5.488550,-2.088477,-7.816115,8.004571,-2.988586,-5.214701,1.136367,-3.366703,9.526621,-8.340262,2.710563,3.246087,-1.642769,8.598869,-7.557323,0.622492,-5.176839,-0.911946,8.717176,-7.520255,2.845306,0.194012,-4.881496,1.195423,-5.832116,-2.737554,-0.539667,8.396206,3.963921,-9.147680,-0.091801,-6.780719,1.054290,8.599911,-2.261496,4.999350,7.708196,-3.923924,-1.041544,9.808871,-0.776190,-4.992863,9.555267,9.146738,-3.631868,8.727265,3.985519,9.577894,-0.622179,6.629686,-6.900877,-7.788733,8.963262,-7.204597,8.177991,-7.808587,2.529131,-5.145844,-0.095247,7.406362,8.726794,-6.635858,-5.052770,-2.939672,-5.113481,-3.079535,-3.321334,-2.772247,3.060897,2.148091,-0.523498,-2.580966,-4.935490,7.150900,6.337295,4.564567,9.971384,0.869138,9.120946,-0.011636,-3.004897,3.197145,5.555556,-8.742722,-9.247434,0.560194,-1.696920,-2.830477,5.740385,4.384849,-1.040716,6.097998,-6.552079,-8.470960,-9.162157,-7.730510,1.339869,7.983844,8.219023,8.187709,8.199652,3.871000,6.732324,-3.614061,0.785488,2.940120,-4.840861,4.481668,1.957801,6.430565,-1.004359,-1.429520,1.516668,-0.881832,-2.304613,-6.317667,8.976052,0.050844,4.046663,5.535371,2.247280,-7.687296,0.045624,7.901399,4.328342,7.222918,-1.060071,0.600811,2.288941,-8.503890,-7.081408,-2.859919,-5.554588,-4.608291,2.394433,-7.941768,-7.840648,3.434371,-6.400558,-5.688791,0.368089,2.522817,-1.411123,0.736504,1.464203,0.304165,-7.766090,6.745776,6.724334,-6.138776,6.291280,8.968530,1.041324,7.539048,1.404732,-1.072546,2.214387,-3.720484,-5.968941,-7.666406,-0.540017,8.911483,7.004041,1.156478,-0.523827,5.721564,7.640487,1.923418,2.460287], dtype = "float32")#candidate|21836|(245,)|const|float32
call_21834 = relay.TupleGetItem(func_18741_call(relay.reshape(const_21835.astype('uint8'), [72,]), relay.reshape(const_21836.astype('float32'), [245,]), ), 7)
call_21837 = relay.TupleGetItem(func_18745_call(relay.reshape(const_21835.astype('uint8'), [72,]), relay.reshape(const_21836.astype('float32'), [245,]), ), 7)
func_11807_call = mod.get_global_var('func_11807')
func_11808_call = mutated_mod.get_global_var('func_11808')
call_21852 = relay.TupleGetItem(func_11807_call(), 0)
call_21853 = relay.TupleGetItem(func_11808_call(), 0)
output = relay.Tuple([call_21814,call_21816,call_21834,const_21835,const_21836,call_21852,])
output2 = relay.Tuple([call_21815,call_21817,call_21837,const_21835,const_21836,call_21853,])
func_21860 = relay.Function([], output)
mod['func_21860'] = func_21860
mod = relay.transform.InferType()(mod)
mutated_mod['func_21860'] = func_21860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21860_call = mutated_mod.get_global_var('func_21860')
call_21861 = func_21860_call()
output = call_21861
func_21862 = relay.Function([], output)
mutated_mod['func_21862'] = func_21862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9600_call = mod.get_global_var('func_9600')
func_9602_call = mutated_mod.get_global_var('func_9602')
call_21881 = relay.TupleGetItem(func_9600_call(), 0)
call_21882 = relay.TupleGetItem(func_9602_call(), 0)
func_18336_call = mod.get_global_var('func_18336')
func_18339_call = mutated_mod.get_global_var('func_18339')
var_21890 = relay.var("var_21890", dtype = "float32", shape = (1650,))#candidate|21890|(1650,)|var|float32
call_21889 = relay.TupleGetItem(func_18336_call(relay.reshape(var_21890.astype('float32'), [1650,])), 0)
call_21891 = relay.TupleGetItem(func_18339_call(relay.reshape(var_21890.astype('float32'), [1650,])), 0)
func_18741_call = mod.get_global_var('func_18741')
func_18745_call = mutated_mod.get_global_var('func_18745')
var_21905 = relay.var("var_21905", dtype = "uint8", shape = (72,))#candidate|21905|(72,)|var|uint8
var_21906 = relay.var("var_21906", dtype = "float32", shape = (245,))#candidate|21906|(245,)|var|float32
call_21904 = relay.TupleGetItem(func_18741_call(relay.reshape(var_21905.astype('uint8'), [72,]), relay.reshape(var_21906.astype('float32'), [245,]), ), 0)
call_21907 = relay.TupleGetItem(func_18745_call(relay.reshape(var_21905.astype('uint8'), [72,]), relay.reshape(var_21906.astype('float32'), [245,]), ), 0)
var_21917 = relay.var("var_21917", dtype = "float32", shape = (245,))#candidate|21917|(245,)|var|float32
bop_21918 = relay.logical_and(var_21906.astype('bool'), relay.reshape(var_21917.astype('bool'), relay.shape_of(var_21906))) # shape=(245,)
output = relay.Tuple([call_21881,call_21889,var_21890,call_21904,var_21905,bop_21918,])
output2 = relay.Tuple([call_21882,call_21891,var_21890,call_21907,var_21905,bop_21918,])
F = relay.Function([var_21890,var_21905,var_21906,var_21917,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_21890,var_21905,var_21906,var_21917,], output2)
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
