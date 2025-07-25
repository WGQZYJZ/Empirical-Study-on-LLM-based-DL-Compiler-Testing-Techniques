import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_262 = relay.var("var_262", dtype = "float32", shape = (12, 7, 2))#candidate|262|(12, 7, 2)|var|float32
var_263 = relay.var("var_263", dtype = "float32", shape = (12, 7, 2))#candidate|263|(12, 7, 2)|var|float32
bop_264 = relay.greater_equal(var_262.astype('bool'), relay.reshape(var_263.astype('bool'), relay.shape_of(var_262))) # shape=(12, 7, 2)
output = bop_264
output2 = bop_264
func_271 = relay.Function([var_262,var_263,], output)
mod['func_271'] = func_271
mod = relay.transform.InferType()(mod)
mutated_mod['func_271'] = func_271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_271_call = mutated_mod.get_global_var('func_271')
var_273 = relay.var("var_273", dtype = "float32", shape = (12, 7, 2))#candidate|273|(12, 7, 2)|var|float32
var_274 = relay.var("var_274", dtype = "float32", shape = (12, 7, 2))#candidate|274|(12, 7, 2)|var|float32
call_272 = func_271_call(var_273,var_274,)
output = call_272
func_275 = relay.Function([var_273,var_274,], output)
mutated_mod['func_275'] = func_275
mutated_mod = relay.transform.InferType()(mutated_mod)
const_713 = relay.const([[[-9.612611,-3.291084,4.557908,-6.116223],[5.830840,-1.472287,0.421551,4.930046],[0.402665,-3.272472,1.171378,-8.328063],[8.543951,-9.402381,-6.064895,-1.648989],[-3.587414,-1.583357,-6.520362,-8.106335],[8.072186,1.051864,0.098812,-8.807882],[-5.748054,-8.798547,2.028186,1.121845],[-0.143509,6.270477,2.938630,3.974665],[-0.661980,-3.048664,-8.990912,-7.243874],[3.071357,-8.086112,-9.262502,9.398704]],[[-0.880076,-5.347247,-3.880876,-7.987832],[6.648202,8.942710,-6.642262,1.156997],[-3.153347,1.947699,-3.010114,7.908077],[-9.511435,-3.321281,-5.956687,6.379034],[-2.791401,-7.207024,-7.485270,3.482096],[-0.374476,-3.456314,7.712962,2.426282],[7.642247,-6.527343,-3.942059,8.167907],[-4.121981,5.190272,-9.142816,4.533155],[1.538899,3.929759,-2.715473,8.690787],[-1.805430,0.341227,6.408196,5.332332]],[[-8.907628,7.974822,8.626812,2.390824],[-8.117193,-2.828553,3.972357,6.575964],[-3.327157,-8.695110,1.898427,8.960593],[-6.252628,6.828141,-3.986921,-9.429005],[4.674545,3.634884,0.246110,-1.353244],[-6.165767,-6.960202,-7.999496,-3.068667],[-7.994933,3.889069,-1.954859,4.356538],[-2.953033,8.633492,-1.026377,6.517679],[6.008700,-2.033106,7.815067,-3.847824],[-3.922758,1.418757,5.228163,6.303447]],[[1.319832,0.707968,2.198552,-4.967764],[-3.927290,-9.120678,3.071283,-4.940142],[9.573008,9.031107,8.298042,-8.850129],[-1.883100,-0.399179,3.373565,-0.855541],[-1.989658,-0.947020,-7.680190,3.281345],[-4.197440,6.964992,8.533351,-1.425624],[9.660091,2.343943,-7.713502,-6.604997],[-3.846633,-3.470306,-5.840233,-8.857758],[-1.056452,-5.415820,0.088391,2.966879],[-2.545251,7.083932,-3.819653,-2.143485]]], dtype = "float32")#candidate|713|(4, 10, 4)|const|float32
uop_714 = relay.rsqrt(const_713.astype('float32')) # shape=(4, 10, 4)
bop_719 = relay.greater_equal(uop_714.astype('bool'), relay.reshape(const_713.astype('bool'), relay.shape_of(uop_714))) # shape=(4, 10, 4)
func_271_call = mod.get_global_var('func_271')
func_275_call = mutated_mod.get_global_var('func_275')
var_723 = relay.var("var_723", dtype = "float32", shape = (168,))#candidate|723|(168,)|var|float32
call_722 = func_271_call(relay.reshape(var_723.astype('float32'), [12, 7, 2]), relay.reshape(var_723.astype('float32'), [12, 7, 2]), )
call_724 = func_271_call(relay.reshape(var_723.astype('float32'), [12, 7, 2]), relay.reshape(var_723.astype('float32'), [12, 7, 2]), )
output = relay.Tuple([bop_719,call_722,var_723,])
output2 = relay.Tuple([bop_719,call_724,var_723,])
func_732 = relay.Function([var_723,], output)
mod['func_732'] = func_732
mod = relay.transform.InferType()(mod)
mutated_mod['func_732'] = func_732
mutated_mod = relay.transform.InferType()(mutated_mod)
var_733 = relay.var("var_733", dtype = "float32", shape = (168,))#candidate|733|(168,)|var|float32
func_732_call = mutated_mod.get_global_var('func_732')
call_734 = func_732_call(var_733)
output = call_734
func_735 = relay.Function([var_733], output)
mutated_mod['func_735'] = func_735
mutated_mod = relay.transform.InferType()(mutated_mod)
const_864 = relay.const([[[-2,-2],[5,10],[-6,-10],[-6,2],[-6,9],[-2,2],[-3,-7],[-10,2],[-10,-10],[8,-1],[-10,9],[-9,1],[5,3],[-6,7]],[[9,-2],[5,-2],[8,-1],[4,3],[3,2],[-2,9],[1,-7],[8,8],[8,-8],[-4,9],[2,10],[-2,-4],[4,-8],[8,-6]],[[-9,8],[8,7],[-6,8],[-5,3],[9,-5],[-6,-7],[-4,-7],[-2,1],[-7,-1],[5,-1],[-10,10],[-6,-3],[6,-7],[9,-3]],[[10,-5],[-4,-6],[-5,5],[2,10],[5,-9],[5,-5],[2,-5],[7,-3],[-9,-9],[-5,5],[-1,-10],[6,-7],[2,-1],[10,1]],[[-9,2],[-6,3],[3,10],[7,8],[8,1],[9,-7],[5,-9],[-8,-8],[5,-3],[7,8],[-7,8],[4,2],[-5,7],[10,-3]]], dtype = "int64")#candidate|864|(5, 14, 2)|const|int64
var_865 = relay.var("var_865", dtype = "int64", shape = (5, 14, 2))#candidate|865|(5, 14, 2)|var|int64
bop_866 = relay.equal(const_864.astype('bool'), relay.reshape(var_865.astype('bool'), relay.shape_of(const_864))) # shape=(5, 14, 2)
func_271_call = mod.get_global_var('func_271')
func_275_call = mutated_mod.get_global_var('func_275')
const_882 = relay.const([-6.403392,-3.784794,4.474990,1.386249,-9.428472,-9.170888,7.065840,0.280379,-9.081019,3.119872,3.923771,-5.442523,3.552011,-6.122682,6.515020,3.472052,-3.190847,-4.443709,5.338105,-5.037277,-5.580524,7.154071,5.529795,7.260906,2.518990,-9.971384,-8.179401,1.390438,-4.854194,-3.953502,-0.578245,5.703699,6.143090,-5.774901,-9.191717,-1.069904,0.188461,-6.941619,-6.276844,-5.711609,3.246983,-9.600626,7.861236,8.768986,-5.017758,-7.593045,-4.084347,7.494202,7.113056,-5.237680,-3.293529,-2.903026,7.413102,-6.343812,-2.469354,5.299459,-3.443941,8.825119,9.276903,9.250106,-6.299973,-5.471381,-6.361749,-9.238518,3.597888,5.000076,0.879574,-2.496803,-7.063888,-6.256595,3.935102,-5.851941,-7.794009,-4.560791,8.672352,3.899330,8.540451,-7.367597,9.606095,1.632766,2.510032,8.221250,-8.826013,7.717676,-0.333382,6.676589,4.903364,9.690528,5.844304,-5.760793,-0.341842,-9.465393,5.917360,6.381301,1.493135,-1.807283,6.532466,1.182303,0.836587,-6.154872,-1.582633,8.351802,-6.538880,4.790041,-4.693589,-0.328020,7.424841,-0.423234,9.027151,-2.882476,-5.899721,8.266844,-8.809640,5.710050,-6.968963,2.612681,5.278266,-9.702579,-6.733044,6.373951,3.274968,8.945730,-4.360269,-2.529297,7.547339,-2.200353,3.235197,8.151465,-0.698590,6.801838,-7.017247,-0.453205,2.264539,3.140841,-0.307735,3.886431,-0.232327,2.979936,-7.436987,-1.413909,-7.926646,-2.503295,8.707270,5.239119,-8.889601,-7.951473,3.803205,4.864703,4.976778,-8.030028,3.415085,-2.402454,-3.053898,9.881807,7.192618,-7.451670,-5.414734,2.803338,-6.786252,-2.284432,0.227035,-3.288491,7.238872,2.201605,-5.353936,-6.075942,8.992266,-3.354433], dtype = "float32")#candidate|882|(168,)|const|float32
call_881 = func_271_call(relay.reshape(const_882.astype('float32'), [12, 7, 2]), relay.reshape(const_882.astype('float32'), [12, 7, 2]), )
call_883 = func_271_call(relay.reshape(const_882.astype('float32'), [12, 7, 2]), relay.reshape(const_882.astype('float32'), [12, 7, 2]), )
output = relay.Tuple([bop_866,call_881,const_882,])
output2 = relay.Tuple([bop_866,call_883,const_882,])
func_884 = relay.Function([var_865,], output)
mod['func_884'] = func_884
mod = relay.transform.InferType()(mod)
mutated_mod['func_884'] = func_884
mutated_mod = relay.transform.InferType()(mutated_mod)
var_885 = relay.var("var_885", dtype = "int64", shape = (5, 14, 2))#candidate|885|(5, 14, 2)|var|int64
func_884_call = mutated_mod.get_global_var('func_884')
call_886 = func_884_call(var_885)
output = call_886
func_887 = relay.Function([var_885], output)
mutated_mod['func_887'] = func_887
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1260 = relay.const(5, dtype = "uint8")#candidate|1260|()|const|uint8
var_1261 = relay.var("var_1261", dtype = "uint8", shape = (15, 11, 1))#candidate|1261|(15, 11, 1)|var|uint8
bop_1262 = relay.left_shift(const_1260.astype('uint8'), var_1261.astype('uint8')) # shape=(15, 11, 1)
output = bop_1262
output2 = bop_1262
func_1272 = relay.Function([var_1261,], output)
mod['func_1272'] = func_1272
mod = relay.transform.InferType()(mod)
mutated_mod['func_1272'] = func_1272
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1273 = relay.var("var_1273", dtype = "uint8", shape = (15, 11, 1))#candidate|1273|(15, 11, 1)|var|uint8
func_1272_call = mutated_mod.get_global_var('func_1272')
call_1274 = func_1272_call(var_1273)
output = call_1274
func_1275 = relay.Function([var_1273], output)
mutated_mod['func_1275'] = func_1275
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1627 = relay.var("var_1627", dtype = "float32", shape = (6, 4, 13))#candidate|1627|(6, 4, 13)|var|float32
uop_1628 = relay.log2(var_1627.astype('float32')) # shape=(6, 4, 13)
var_1640 = relay.var("var_1640", dtype = "float32", shape = (6, 4, 13))#candidate|1640|(6, 4, 13)|var|float32
bop_1641 = relay.power(uop_1628.astype('float64'), relay.reshape(var_1640.astype('float64'), relay.shape_of(uop_1628))) # shape=(6, 4, 13)
uop_1646 = relay.exp(uop_1628.astype('float64')) # shape=(6, 4, 13)
output = relay.Tuple([bop_1641,uop_1646,])
output2 = relay.Tuple([bop_1641,uop_1646,])
func_1649 = relay.Function([var_1627,var_1640,], output)
mod['func_1649'] = func_1649
mod = relay.transform.InferType()(mod)
var_1650 = relay.var("var_1650", dtype = "float32", shape = (6, 4, 13))#candidate|1650|(6, 4, 13)|var|float32
var_1651 = relay.var("var_1651", dtype = "float32", shape = (6, 4, 13))#candidate|1651|(6, 4, 13)|var|float32
output = func_1649(var_1650,var_1651,)
func_1652 = relay.Function([var_1650,var_1651,], output)
mutated_mod['func_1652'] = func_1652
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2026 = relay.var("var_2026", dtype = "uint32", shape = (4, 2, 16))#candidate|2026|(4, 2, 16)|var|uint32
var_2027 = relay.var("var_2027", dtype = "uint32", shape = (4, 2, 16))#candidate|2027|(4, 2, 16)|var|uint32
bop_2028 = relay.less(var_2026.astype('bool'), relay.reshape(var_2027.astype('bool'), relay.shape_of(var_2026))) # shape=(4, 2, 16)
uop_2054 = relay.sigmoid(bop_2028.astype('float64')) # shape=(4, 2, 16)
output = uop_2054
output2 = uop_2054
func_2064 = relay.Function([var_2026,var_2027,], output)
mod['func_2064'] = func_2064
mod = relay.transform.InferType()(mod)
mutated_mod['func_2064'] = func_2064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2064_call = mutated_mod.get_global_var('func_2064')
var_2066 = relay.var("var_2066", dtype = "uint32", shape = (4, 2, 16))#candidate|2066|(4, 2, 16)|var|uint32
var_2067 = relay.var("var_2067", dtype = "uint32", shape = (4, 2, 16))#candidate|2067|(4, 2, 16)|var|uint32
call_2065 = func_2064_call(var_2066,var_2067,)
output = call_2065
func_2068 = relay.Function([var_2066,var_2067,], output)
mutated_mod['func_2068'] = func_2068
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2286 = relay.var("var_2286", dtype = "uint16", shape = (1, 9, 10))#candidate|2286|(1, 9, 10)|var|uint16
var_2287 = relay.var("var_2287", dtype = "uint16", shape = (2, 9, 10))#candidate|2287|(2, 9, 10)|var|uint16
bop_2288 = relay.logical_xor(var_2286.astype('uint16'), var_2287.astype('uint16')) # shape=(2, 9, 10)
func_884_call = mod.get_global_var('func_884')
func_887_call = mutated_mod.get_global_var('func_887')
const_2306 = relay.const([4,3,-2,-6,-8,-5,-2,6,-7,8,-1,8,-2,9,1,-9,5,-3,-4,8,-8,4,-7,-4,3,8,6,-3,-8,-2,-6,2,-2,8,5,-9,8,1,-4,-2,6,-3,5,-1,-8,-2,3,-4,10,-2,-8,8,-6,3,-3,-9,6,-1,5,6,4,-8,1,-3,-5,-5,-10,1,9,6,-3,-1,6,-2,4,6,3,7,7,-4,-9,-7,2,-2,6,-5,4,7,-9,-3,-6,-3,5,4,1,4,9,-8,-1,-3,10,-3,-5,-8,-9,7,2,-6,-1,-6,-10,-4,-2,-1,-3,-10,-4,1,3,-4,-10,8,1,8,-4,-8,-7,-5,-5,1,-3,-4,4,-6,5,-9,-1,7,-1,-5], dtype = "int64")#candidate|2306|(140,)|const|int64
call_2305 = relay.TupleGetItem(func_884_call(relay.reshape(const_2306.astype('int64'), [5, 14, 2])), 1)
call_2307 = relay.TupleGetItem(func_887_call(relay.reshape(const_2306.astype('int64'), [5, 14, 2])), 1)
func_1272_call = mod.get_global_var('func_1272')
func_1275_call = mutated_mod.get_global_var('func_1275')
const_2312 = relay.const([10,-1,7,10,-5,-7,-9,9,9,-8,9,4,-8,-6,5,-9,7,6,7,1,7,1,5,9,-3,10,4,1,6,-2,-5,8,1,7,-7,8,-8,-1,8,-6,6,7,1,-3,5,8,6,-3,-7,5,-1,-2,-3,-4,5,-5,8,-3,10,-6,3,7,7,8,-10,-1,-7,2,6,-2,5,-3,1,-4,4,-8,-3,6,-4,-5,7,-7,-9,-6,-4,7,8,-2,8,2,5,8,-6,7,1,6,10,-2,-2,-3,9,-4,1,-5,-4,-8,-6,7,3,2,8,1,1,4,-2,-8,10,-7,9,-10,1,-4,-6,-1,-4,10,2,7,-5,-9,-1,-9,10,-2,1,4,9,1,8,4,-8,2,-8,-7,2,-1,2,2,9,3,-5,4,-4,7,8,3,-8,7,-4,8,-10,-8,10,-4,-5], dtype = "uint8")#candidate|2312|(165,)|const|uint8
call_2311 = func_1272_call(relay.reshape(const_2312.astype('uint8'), [15, 11, 1]))
call_2313 = func_1272_call(relay.reshape(const_2312.astype('uint8'), [15, 11, 1]))
output = relay.Tuple([bop_2288,call_2305,const_2306,call_2311,const_2312,])
output2 = relay.Tuple([bop_2288,call_2307,const_2306,call_2313,const_2312,])
func_2320 = relay.Function([var_2286,var_2287,], output)
mod['func_2320'] = func_2320
mod = relay.transform.InferType()(mod)
mutated_mod['func_2320'] = func_2320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2320_call = mutated_mod.get_global_var('func_2320')
var_2322 = relay.var("var_2322", dtype = "uint16", shape = (1, 9, 10))#candidate|2322|(1, 9, 10)|var|uint16
var_2323 = relay.var("var_2323", dtype = "uint16", shape = (2, 9, 10))#candidate|2323|(2, 9, 10)|var|uint16
call_2321 = func_2320_call(var_2322,var_2323,)
output = call_2321
func_2324 = relay.Function([var_2322,var_2323,], output)
mutated_mod['func_2324'] = func_2324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2591 = relay.var("var_2591", dtype = "int64", shape = (3, 13, 8))#candidate|2591|(3, 13, 8)|var|int64
var_2592 = relay.var("var_2592", dtype = "int64", shape = (3, 13, 8))#candidate|2592|(3, 13, 8)|var|int64
bop_2593 = relay.less(var_2591.astype('bool'), relay.reshape(var_2592.astype('bool'), relay.shape_of(var_2591))) # shape=(3, 13, 8)
uop_2596 = relay.erf(bop_2593.astype('float32')) # shape=(3, 13, 8)
output = uop_2596
output2 = uop_2596
func_2606 = relay.Function([var_2591,var_2592,], output)
mod['func_2606'] = func_2606
mod = relay.transform.InferType()(mod)
mutated_mod['func_2606'] = func_2606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2606_call = mutated_mod.get_global_var('func_2606')
var_2608 = relay.var("var_2608", dtype = "int64", shape = (3, 13, 8))#candidate|2608|(3, 13, 8)|var|int64
var_2609 = relay.var("var_2609", dtype = "int64", shape = (3, 13, 8))#candidate|2609|(3, 13, 8)|var|int64
call_2607 = func_2606_call(var_2608,var_2609,)
output = call_2607
func_2610 = relay.Function([var_2608,var_2609,], output)
mutated_mod['func_2610'] = func_2610
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2711 = relay.var("var_2711", dtype = "float32", shape = (12, 5, 15))#candidate|2711|(12, 5, 15)|var|float32
uop_2712 = relay.log10(var_2711.astype('float32')) # shape=(12, 5, 15)
output = uop_2712
output2 = uop_2712
func_2726 = relay.Function([var_2711,], output)
mod['func_2726'] = func_2726
mod = relay.transform.InferType()(mod)
var_2727 = relay.var("var_2727", dtype = "float32", shape = (12, 5, 15))#candidate|2727|(12, 5, 15)|var|float32
output = func_2726(var_2727)
func_2728 = relay.Function([var_2727], output)
mutated_mod['func_2728'] = func_2728
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2882 = relay.var("var_2882", dtype = "float64", shape = (10, 15, 1))#candidate|2882|(10, 15, 1)|var|float64
uop_2883 = relay.acos(var_2882.astype('float64')) # shape=(10, 15, 1)
bop_2887 = relay.floor_divide(uop_2883.astype('float64'), relay.reshape(var_2882.astype('float64'), relay.shape_of(uop_2883))) # shape=(10, 15, 1)
bop_2890 = relay.floor_mod(bop_2887.astype('float64'), relay.reshape(uop_2883.astype('float64'), relay.shape_of(bop_2887))) # shape=(10, 15, 1)
var_2893 = relay.var("var_2893", dtype = "float64", shape = (10, 15, 10))#candidate|2893|(10, 15, 10)|var|float64
bop_2894 = relay.floor_mod(var_2882.astype('float32'), var_2893.astype('float32')) # shape=(10, 15, 10)
output = relay.Tuple([bop_2890,bop_2894,])
output2 = relay.Tuple([bop_2890,bop_2894,])
func_2897 = relay.Function([var_2882,var_2893,], output)
mod['func_2897'] = func_2897
mod = relay.transform.InferType()(mod)
var_2898 = relay.var("var_2898", dtype = "float64", shape = (10, 15, 1))#candidate|2898|(10, 15, 1)|var|float64
var_2899 = relay.var("var_2899", dtype = "float64", shape = (10, 15, 10))#candidate|2899|(10, 15, 10)|var|float64
output = func_2897(var_2898,var_2899,)
func_2900 = relay.Function([var_2898,var_2899,], output)
mutated_mod['func_2900'] = func_2900
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3203 = relay.var("var_3203", dtype = "float64", shape = (10, 16, 5))#candidate|3203|(10, 16, 5)|var|float64
uop_3204 = relay.tan(var_3203.astype('float64')) # shape=(10, 16, 5)
output = relay.Tuple([uop_3204,])
output2 = relay.Tuple([uop_3204,])
func_3212 = relay.Function([var_3203,], output)
mod['func_3212'] = func_3212
mod = relay.transform.InferType()(mod)
mutated_mod['func_3212'] = func_3212
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3213 = relay.var("var_3213", dtype = "float64", shape = (10, 16, 5))#candidate|3213|(10, 16, 5)|var|float64
func_3212_call = mutated_mod.get_global_var('func_3212')
call_3214 = func_3212_call(var_3213)
output = call_3214
func_3215 = relay.Function([var_3213], output)
mutated_mod['func_3215'] = func_3215
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3824 = relay.var("var_3824", dtype = "float64", shape = (15, 16, 14))#candidate|3824|(15, 16, 14)|var|float64
uop_3825 = relay.rsqrt(var_3824.astype('float64')) # shape=(15, 16, 14)
output = uop_3825
output2 = uop_3825
func_3835 = relay.Function([var_3824,], output)
mod['func_3835'] = func_3835
mod = relay.transform.InferType()(mod)
var_3836 = relay.var("var_3836", dtype = "float64", shape = (15, 16, 14))#candidate|3836|(15, 16, 14)|var|float64
output = func_3835(var_3836)
func_3837 = relay.Function([var_3836], output)
mutated_mod['func_3837'] = func_3837
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3886 = relay.var("var_3886", dtype = "float64", shape = (2, 2, 13))#candidate|3886|(2, 2, 13)|var|float64
uop_3887 = relay.asinh(var_3886.astype('float64')) # shape=(2, 2, 13)
func_2726_call = mod.get_global_var('func_2726')
func_2728_call = mutated_mod.get_global_var('func_2728')
const_3900 = relay.const([9.045100,-1.468054,-0.996503,1.600995,4.672515,0.251951,-9.534388,-2.801630,8.134419,0.550069,7.915362,8.651532,7.309207,-3.039097,-6.488999,5.501925,4.107163,-3.583774,0.320059,3.441999,-2.181036,-4.050586,6.072559,-3.742914,-1.446165,4.479435,7.298035,-9.840772,8.448800,0.892197,-5.682627,-3.839211,-6.871615,4.966968,-9.932776,7.880145,7.129725,7.214229,-1.949978,4.257950,2.135533,-1.850203,-2.917086,-4.609548,5.668974,6.516904,-4.386520,-1.788526,-7.734537,-1.898073,-9.338281,-7.670659,7.570877,-8.450594,9.059038,5.589594,-4.743433,5.950805,-4.424777,1.431084,-3.435596,4.199418,-0.567405,0.356304,3.518287,5.780361,4.408500,1.929989,-7.530692,-3.420772,0.599494,-7.726082,7.809622,-5.499344,2.003105,-7.139960,7.556232,-5.524792,8.929880,-9.206607,0.536443,-9.442698,9.076261,-1.773060,-6.470286,-7.571594,-7.747405,8.236648,-4.605115,3.915964,3.492988,2.223289,3.764083,-7.168525,-2.811379,6.503178,9.795609,-1.590766,2.285068,-6.684836,-2.726078,8.543972,3.851979,-6.228738,5.848480,-2.555094,0.096598,5.276210,0.887349,2.875801,-6.462300,-8.081366,4.358133,5.982059,1.540446,-9.455628,-3.737418,-9.275259,-3.940086,2.926987,-8.603515,9.658994,-5.406573,-8.674288,-0.503798,0.799411,-6.293232,-7.697604,-4.931648,-8.010470,6.902122,8.412173,-4.505027,-4.577050,7.222646,-5.544297,1.526169,7.217164,-5.050234,9.454192,-6.659009,-5.309757,-3.872624,-0.598239,-3.193566,-7.517181,1.548640,9.943776,0.480738,-2.900361,4.240188,-1.551700,-2.760037,-9.941831,8.493226,-9.312354,-1.587595,-0.494452,6.379022,-5.591824,7.708376,-8.808926,-2.362658,3.427644,6.757007,-9.288919,-3.863098,6.586407,0.568006,-6.118323,4.410776,-7.850509,9.804092,3.053282,0.019517,-1.660110,-9.527891,7.915422,-2.036442,2.872016,-7.911469,-3.661433,-3.301220,-4.432318,-2.015759,0.070586,0.083852,5.112121,-2.822989,4.684941,-5.452452,7.201752,-2.654426,-3.330555,6.251211,-4.836253,3.456414,-5.854758,-7.855182,9.567238,8.247649,4.008006,-4.431776,8.832487,4.703049,-3.360022,-5.249767,-8.182967,-4.934422,2.173493,-2.406400,-7.537020,2.513322,-8.608731,2.814737,-9.503893,-0.223145,1.293222,-6.558861,1.598746,3.410626,-1.039271,1.825633,7.105511,6.724251,5.618413,-2.710363,4.249236,5.901656,-0.818548,-8.531845,0.918798,-9.117790,7.270498,-7.688768,-1.041065,5.439399,7.881011,8.386872,-5.504345,-2.052262,6.572931,3.567200,-8.901432,-8.615954,2.868590,8.236895,0.895746,5.263778,-2.482131,7.567760,-8.075286,5.949283,-8.973547,-9.707334,4.107756,-0.557438,5.108875,-0.890009,-6.712980,-3.956915,8.672189,7.830770,7.027639,5.240616,-2.878298,-5.661847,7.808861,-0.311921,9.050567,1.319929,0.293984,3.243143,9.241261,-5.397242,-3.311972,-0.886725,-9.216934,-9.379369,-1.604885,-0.243966,-7.417169,0.171900,-4.153218,5.323420,-2.741246,1.220951,1.539177,4.864307,-0.894460,-8.180220,-0.026256,-2.903337,-8.900873,5.256440,-6.933021,5.500300,-4.080108,4.776539,0.034147,-3.480959,6.125510,7.079427,-0.824097,7.855213,3.888294,9.243886,-4.633199,-6.977198,-4.400926,-8.799185,9.540291,-0.598249,-1.730882,3.189785,-6.611144,-2.329361,1.830316,-8.548148,-1.112711,-1.496867,-5.466805,2.420539,5.129379,4.443251,6.845916,-8.196058,-0.684646,8.570367,-3.345234,-3.906701,-9.227643,-3.749055,-6.919312,-8.013778,2.494939,-6.519129,-9.140915,-9.463685,-1.293734,-1.431057,9.962500,-2.378598,1.985758,6.012797,-5.501438,-6.778621,-9.213914,-1.474440,-9.300540,6.077055,8.963758,3.036768,9.835604,0.147577,2.689969,-1.493586,4.732941,-8.311999,-6.898039,-3.669050,0.354047,6.953255,-7.062415,3.544473,-0.959788,-0.331887,-8.408812,-1.189987,2.362163,7.688177,7.276836,-3.797203,7.330199,1.319849,-5.151448,-5.648859,-1.815390,8.599994,-0.021489,0.722259,8.906372,-4.510223,0.781882,7.021619,5.504325,-4.736687,-3.105310,9.722854,5.812105,1.017553,-2.302563,-9.122529,-9.633491,8.473761,-2.722777,1.117703,-4.483835,0.388081,-8.461447,3.235650,-9.582691,-3.212590,-4.785230,-2.347545,-0.998063,4.013759,2.148696,-7.166895,3.874842,-0.331202,-3.747569,4.798130,-6.836092,4.694754,8.146727,-1.226459,-1.213153,8.253740,-6.992976,-7.697414,3.580207,2.609260,7.879869,-1.046872,-1.949731,-9.512048,0.771333,4.392692,4.364174,-2.415990,3.377570,-3.036704,-7.936851,-4.396030,2.105689,7.495828,-7.826026,2.438136,-2.971669,-4.838561,0.140942,-8.510177,-5.874015,-3.325140,-7.576174,9.866078,7.456808,1.221711,0.073250,-6.737736,-9.798939,0.494671,-3.792457,0.282392,7.900160,7.537840,-5.192067,8.335326,-2.057338,-9.368118,-8.321183,-0.335746,7.409299,9.836855,-7.131787,2.736993,-6.184592,0.401281,-5.947650,1.363607,3.610145,-4.077577,-4.859538,-2.210490,5.556907,9.920389,-3.666647,6.047579,7.552083,-5.984823,-7.854509,1.603007,9.988341,1.546397,1.710771,2.965065,-5.619868,-8.372594,5.565508,9.549790,-0.211744,-3.732320,-2.594610,-7.667263,2.814651,9.290530,9.906595,-0.617902,-9.634819,-0.016774,-8.834907,-1.916509,9.348088,-5.819851,7.558197,5.743386,-3.841086,6.316601,1.821482,9.591506,-4.780052,-0.662365,3.229635,-2.763688,-7.085985,5.682828,-0.830845,2.666090,-8.537856,-5.705113,3.835389,9.066156,-1.741316,1.150230,2.439996,-1.440051,8.140148,5.354061,8.457951,-2.030138,-2.181944,-5.758658,4.847822,-7.587337,1.750482,-6.543691,-9.880537,5.943709,-6.997120,-4.352864,8.830288,2.475922,4.423938,5.375170,5.395166,-5.777531,2.802690,-7.927298,1.753753,-3.779313,-9.817854,9.776020,9.244551,0.820048,4.539400,5.189266,-6.807760,-8.519001,0.160149,-4.401598,9.162453,-8.379819,6.021114,-4.393240,0.892579,-1.700362,9.867858,-0.881544,-3.169253,-4.818735,8.492716,-8.876931,-8.753811,6.227976,-0.257899,-6.373861,-8.679144,-7.389412,-2.165764,-7.134787,2.807437,8.366455,4.891771,3.654145,7.333908,2.641616,5.329866,-5.802090,-6.208359,5.825417,1.504884,0.308885,-8.763300,9.409817,-5.725818,-7.593737,-2.306827,-5.874286,5.326923,5.625648,7.804108,1.424963,-1.577721,-0.245405,1.381111,9.982390,-3.656040,0.394506,-1.901263,3.638344,-4.801505,2.422905,6.371643,-0.515621,9.732937,5.312597,7.524763,-2.858502,-0.212587,-9.185666,-2.917308,-9.707623,-1.436225,-3.878178,-2.359861,1.501995,8.965662,-4.985162,-8.900051,-1.770874,-1.546841,-1.029659,-3.880895,-1.234457,-1.340408,8.566880,-7.000027,6.743579,8.472206,-2.076661,2.595345,-3.103159,-3.777966,2.403362,-5.515740,-2.072751,9.190423,-0.719425,6.304345,-8.853125,6.535687,9.968043,4.470613,5.351138,-8.072349,-9.250766,2.773635,-3.159368,5.537634,6.379746,9.725797,9.836360,-0.294853,9.104340,-7.116124,2.304481,8.888909,3.914808,0.961561,9.001179,-0.244438,6.060111,-9.882431,4.148646,5.298200,9.552112,9.743406,6.354762,-7.673694,5.846681,-3.475599,7.898744,1.373078,-4.769436,9.075188,-5.839639,-9.430508,3.784372,-9.983712,-7.942550,1.936192,-1.902315,-0.797582,9.301914,-9.903072,9.904859,6.707217,-5.519023,-1.800840,-9.668190,-4.730088,0.678232,-5.399863,-7.527378,-7.412083,2.926795,-6.404896,-7.839936,4.460481,-6.279247,-6.048218,6.528338,-2.584537,1.480103,-3.347755,-8.449164,-6.481178,9.359798,-2.346094,8.750287,5.569659,4.402504,2.842811,-9.872868,4.357024,-9.132618,6.827346,4.340076,-9.456933,-7.299988,-0.996759,9.417682,-0.015887,-1.179818,-2.382682,8.640079,-7.744821,-6.446217,-8.376769,-0.659124,8.523314,-0.036630,-4.455636,-6.355182,-7.731033,-5.784990,4.235847,0.781108,-4.064078,-4.656890,-7.922711,-2.296734,-8.487652,-1.945398,-1.237698,-6.602660,4.409398,-0.782150,7.587045,-0.060889,1.332525,-7.181227,1.556263,-7.330323,4.687526,-3.161333,8.103345,-0.363770,1.066697,-3.364962,-6.227927,8.099518,9.131071,8.985599,-8.666309,-7.893529,-0.288062,-7.398300,0.322539,-6.729470,-8.600002,-9.364092,5.105676,4.077522,1.971909,-0.227737,9.470361,4.983005,0.551607,3.143388,1.721433,5.848448,-2.762226,0.631254,4.312008,1.465130,-8.022193,2.608183,-6.264237,9.298886,-1.646490,4.813470,7.304132,5.611985,-4.434626,1.723355,-8.504277,5.904557,-3.569092,-4.366150,-4.928091,3.520931,3.947735,5.865338,-7.681743,8.564791,-6.227325,-9.489181,-2.759128,8.683859,-2.174590,-3.070222,9.848281,5.267885,-4.676418,0.666479,9.412744,0.191623,3.661758,6.116618,0.875563,3.932149,7.490344,-8.159499,4.733945,-3.483300,-3.614463,-9.607746,6.490132,9.257111,-4.537568,-2.246166,-6.887841,-1.811841,-5.789049,0.956615,5.249126,-7.334786,-3.299539,-4.878191,-5.497004,1.623230,6.112930,-4.252508,2.188889,-7.134538,4.716200,-1.857114,-0.613779,8.884244,-2.270564,8.839242,8.799564,-3.754066,-5.780873,2.183618,-3.508350,0.981498,5.197701,-5.334360,7.991860,-8.629612,1.543354,-3.155621,3.045748,3.211433,-1.586873,9.544454,-7.433175,5.775092,-9.152975,7.798540,6.396682,-3.255534,-2.781943,-0.095138,7.093725,-6.463566,3.612255,8.138421,4.101785,-6.068100,9.336812,5.861323,2.949409,-1.187864,-4.534845,-2.659130,-2.386598], dtype = "float32")#candidate|3900|(900,)|const|float32
call_3899 = func_2726_call(relay.reshape(const_3900.astype('float32'), [12, 5, 15]))
call_3901 = func_2726_call(relay.reshape(const_3900.astype('float32'), [12, 5, 15]))
func_2606_call = mod.get_global_var('func_2606')
func_2610_call = mutated_mod.get_global_var('func_2610')
const_3910 = relay.const([-10,6,-5,6,-9,1,-2,5,-7,-3,-7,8,-3,-3,8,8,6,-9,-10,10,-10,5,1,-3,-10,5,-5,9,4,10,5,-7,-3,3,-3,-5,3,-3,9,5,2,-5,3,-7,-6,-6,-5,2,-1,-1,10,-7,5,-9,8,4,-4,-9,2,3,-2,-9,-3,-5,9,-1,2,-6,-10,3,-9,-9,3,9,5,5,10,-4,-8,9,5,-8,8,7,-9,7,5,-10,-6,-8,-2,10,-9,-4,5,6,-1,-8,8,-8,-6,-4,3,-1,-4,3,2,-7,10,-7,3,5,-8,5,-8,3,-10,-5,1,-3,5,-3,9,-7,9,4,-9,-8,-1,3,5,-5,2,-7,8,-8,-8,-7,10,6,9,-1,-6,-5,1,-10,5,3,-7,-8,4,7,8,-7,-9,-8,-2,5,10,-6,-10,-9,-4,-2,-5,-8,-10,-1,1,9,-2,6,-7,-1,-5,-10,-5,-1,3,4,6,9,6,-4,-7,-7,-1,-2,-8,-5,-1,-9,4,-9,-5,-5,4,-7,-1,9,6,-6,1,-3,-2,-3,3,-1,-3,-2,-3,9,8,-8,-9,-8,5,1,-1,-6,-3,5,-2,-3,-7,1,-1,-7,-8,-1,-4,-9,-2,-6,5,7,10,5,10,-6,4,-9,10,7,3,-3,6,7,-2,-2,-4,6,1,-7,-3,8,-10,4,2,-8,-9,3,2,-3,4,3,4,-5,5,6,5,-5,10,7,-3,9,5,-9,-4,3,-10,8,-8,-9,-7,10,10,8,-7,3,9,5,-8,1,1,-1,-10,4,-4,-8,-1,-4,6,-10,7,2,-9,-10,-3,8,4,-4], dtype = "int64")#candidate|3910|(312,)|const|int64
call_3909 = func_2606_call(relay.reshape(const_3910.astype('int64'), [3, 13, 8]), relay.reshape(const_3910.astype('int64'), [3, 13, 8]), )
call_3911 = func_2606_call(relay.reshape(const_3910.astype('int64'), [3, 13, 8]), relay.reshape(const_3910.astype('int64'), [3, 13, 8]), )
func_271_call = mod.get_global_var('func_271')
func_275_call = mutated_mod.get_global_var('func_275')
const_3915 = relay.const([[-1.148767,-2.573006,2.229495,3.203707,9.987664,8.044370,-0.135223,-6.574033,-7.742725,-5.119294,-3.043679,-5.432618,-8.932330,8.609293,-7.763875,1.718486,-9.894566,-9.615408,7.845468,3.104197,-1.370272,-5.383914,5.931117,-6.889892,0.716970,-2.498843,8.413783,8.835635],[-0.360918,-4.914305,5.858836,8.191613,-0.724895,4.763547,-3.944840,-2.420095,7.773285,1.734830,-8.583292,0.934674,-1.723857,3.608885,-0.826314,6.826978,9.909231,4.324634,1.603793,-2.459006,5.122288,-6.087165,7.694134,-2.572615,5.566734,0.796512,0.695993,8.842163],[1.926425,-1.130633,9.344698,-3.180216,7.056790,0.418426,5.691895,-7.064110,-7.727317,-4.764634,-3.704155,-7.570309,-4.182477,4.485303,-8.413466,4.488681,7.239965,-4.367270,-6.546722,6.708718,-7.815603,-6.592957,-5.721718,-9.189070,8.987756,-5.777751,4.338782,-4.783942],[2.054139,-4.804017,-3.975749,7.301913,2.014576,4.662796,-4.532606,3.731430,3.500152,-3.342182,0.401547,-7.291239,0.904533,-5.365733,-1.932927,-9.272264,-1.852551,8.277940,4.149298,-1.291927,-0.670358,-4.354731,-6.689557,-0.401535,3.902267,3.624110,2.545824,-4.318065],[8.557692,-7.246611,0.795666,7.250410,7.637988,-9.795478,1.535934,9.037215,-1.280040,-5.985782,0.846402,6.531074,-8.886758,0.169507,-5.693450,-5.432276,-4.414966,0.379332,-0.690426,3.310305,-1.616884,-5.355642,-9.323872,8.799301,7.142026,0.623774,-1.567387,5.031003],[-0.642260,8.251250,-7.225365,-6.730352,-6.421672,-6.735213,-8.429513,-1.344575,-3.503140,-8.240899,-0.319265,2.131886,5.957267,-2.977760,6.891197,-4.443464,9.330601,5.765712,-0.879080,-5.912545,1.042301,7.534934,1.331573,-7.193601,-5.352148,-8.641444,7.969563,-1.371826]], dtype = "float32")#candidate|3915|(6, 28)|const|float32
call_3914 = func_271_call(relay.reshape(const_3915.astype('float32'), [12, 7, 2]), relay.reshape(const_3915.astype('float32'), [12, 7, 2]), )
call_3916 = func_271_call(relay.reshape(const_3915.astype('float32'), [12, 7, 2]), relay.reshape(const_3915.astype('float32'), [12, 7, 2]), )
output = relay.Tuple([uop_3887,call_3899,const_3900,call_3909,const_3910,call_3914,const_3915,])
output2 = relay.Tuple([uop_3887,call_3901,const_3900,call_3911,const_3910,call_3916,const_3915,])
func_3926 = relay.Function([var_3886,], output)
mod['func_3926'] = func_3926
mod = relay.transform.InferType()(mod)
mutated_mod['func_3926'] = func_3926
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3927 = relay.var("var_3927", dtype = "float64", shape = (2, 2, 13))#candidate|3927|(2, 2, 13)|var|float64
func_3926_call = mutated_mod.get_global_var('func_3926')
call_3928 = func_3926_call(var_3927)
output = call_3928
func_3929 = relay.Function([var_3927], output)
mutated_mod['func_3929'] = func_3929
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4027 = relay.var("var_4027", dtype = "uint32", shape = (1, 9, 14))#candidate|4027|(1, 9, 14)|var|uint32
var_4028 = relay.var("var_4028", dtype = "uint32", shape = (8, 9, 14))#candidate|4028|(8, 9, 14)|var|uint32
bop_4029 = relay.maximum(var_4027.astype('uint32'), var_4028.astype('uint32')) # shape=(8, 9, 14)
func_2606_call = mod.get_global_var('func_2606')
func_2610_call = mutated_mod.get_global_var('func_2610')
const_4033 = relay.const([[6],[2],[10],[5],[8],[8],[1],[4],[-5],[6],[4],[-10],[-8],[2],[2],[8],[-5],[4],[-4],[5],[-4],[-8],[8],[-4],[10],[-8],[8],[3],[-1],[-1],[10],[-5],[-2],[8],[9],[-10],[10],[-8],[9],[-1],[4],[5],[9],[7],[-4],[5],[10],[9],[-8],[-9],[-2],[-1],[-8],[-3],[3],[-8],[-5],[-8],[-1],[-4],[-3],[-1],[8],[4],[8],[-6],[6],[-7],[6],[-1],[-3],[-5],[-4],[-3],[-8],[-1],[8],[4],[3],[4],[3],[6],[-7],[4],[-10],[-4],[6],[1],[2],[4],[-1],[-9],[-1],[4],[2],[9],[-10],[-3],[-5],[-2],[-1],[-8],[-6],[6],[3],[8],[-9],[10],[3],[-5],[-4],[8],[-7],[-2],[-7],[-7],[-1],[-7],[4],[-8],[7],[10],[4],[-7],[-5],[-10],[9],[4],[-1],[10],[1],[10],[4],[10],[3],[4],[4],[10],[-5],[-5],[-1],[1],[6],[-8],[2],[-5],[-5],[2],[2],[-7],[9],[-9],[-9],[-3],[5],[-7],[6],[6],[3],[-7],[2],[-5],[-8],[-6],[2],[9],[9],[6],[-6],[2],[-8],[10],[7],[6],[-10],[7],[8],[10],[-3],[-8],[2],[-6],[-7],[6],[-1],[7],[-7],[3],[-2],[8],[-3],[-5],[8],[-7],[-2],[4],[4],[2],[10],[7],[8],[3],[8],[3],[-5],[2],[-5],[9],[2],[4],[10],[-5],[-8],[8],[-9],[-1],[6],[4],[10],[-3],[-8],[4],[-2],[7],[-8],[-8],[-9],[-5],[-2],[-4],[7],[-7],[9],[-8],[-9],[-5],[8],[2],[-10],[-3],[-2],[-7],[4],[7],[-6],[-6],[-8],[7],[-6],[-6],[7],[-4],[1],[-2],[7],[-9],[6],[1],[7],[-7],[-10],[-7],[6],[6],[8],[9],[-5],[10],[-10],[-7],[10],[7],[2],[-8],[-7],[4],[-8],[6],[5],[-7],[7],[-10],[-8],[-10],[-5],[-5],[-3],[-4],[2],[5],[-9],[-7],[-8],[-2],[-8],[-7],[5],[-9],[8],[-1],[-6],[-9],[-1],[-3],[-5],[4],[-7],[-10],[5],[-9],[-10],[-8]], dtype = "int64")#candidate|4033|(312, 1)|const|int64
call_4032 = func_2606_call(relay.reshape(const_4033.astype('int64'), [3, 13, 8]), relay.reshape(const_4033.astype('int64'), [3, 13, 8]), )
call_4034 = func_2606_call(relay.reshape(const_4033.astype('int64'), [3, 13, 8]), relay.reshape(const_4033.astype('int64'), [3, 13, 8]), )
output = relay.Tuple([bop_4029,call_4032,const_4033,])
output2 = relay.Tuple([bop_4029,call_4034,const_4033,])
func_4041 = relay.Function([var_4027,var_4028,], output)
mod['func_4041'] = func_4041
mod = relay.transform.InferType()(mod)
mutated_mod['func_4041'] = func_4041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4041_call = mutated_mod.get_global_var('func_4041')
var_4043 = relay.var("var_4043", dtype = "uint32", shape = (1, 9, 14))#candidate|4043|(1, 9, 14)|var|uint32
var_4044 = relay.var("var_4044", dtype = "uint32", shape = (8, 9, 14))#candidate|4044|(8, 9, 14)|var|uint32
call_4042 = func_4041_call(var_4043,var_4044,)
output = call_4042
func_4045 = relay.Function([var_4043,var_4044,], output)
mutated_mod['func_4045'] = func_4045
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4102 = relay.var("var_4102", dtype = "float32", shape = (2, 9, 1))#candidate|4102|(2, 9, 1)|var|float32
uop_4103 = relay.acosh(var_4102.astype('float32')) # shape=(2, 9, 1)
func_3926_call = mod.get_global_var('func_3926')
func_3929_call = mutated_mod.get_global_var('func_3929')
const_4106 = relay.const([[2.549290,3.412322],[0.178325,6.089818],[7.451463,-2.567883],[-1.186973,5.219646],[-4.755646,9.533147],[-6.985057,-5.962676],[1.330701,-6.585795],[-7.517767,-9.304541],[-8.666210,3.504497],[3.576149,7.487950],[-7.372372,4.664833],[4.458182,-2.799943],[7.405280,-6.928035],[-8.702989,8.140256],[-4.836648,3.675856],[5.185045,-8.927780],[-6.397164,0.472718],[-2.894731,-3.582779],[-5.380724,8.554517],[9.759700,0.579217],[-7.325485,-1.634897],[-2.116235,-0.374966],[4.793634,-3.709119],[6.187614,-3.563835],[-6.109418,4.106095],[-0.723025,4.834354]], dtype = "float64")#candidate|4106|(26, 2)|const|float64
call_4105 = relay.TupleGetItem(func_3926_call(relay.reshape(const_4106.astype('float64'), [2, 2, 13])), 0)
call_4107 = relay.TupleGetItem(func_3929_call(relay.reshape(const_4106.astype('float64'), [2, 2, 13])), 0)
output = relay.Tuple([uop_4103,call_4105,const_4106,])
output2 = relay.Tuple([uop_4103,call_4107,const_4106,])
func_4118 = relay.Function([var_4102,], output)
mod['func_4118'] = func_4118
mod = relay.transform.InferType()(mod)
var_4119 = relay.var("var_4119", dtype = "float32", shape = (2, 9, 1))#candidate|4119|(2, 9, 1)|var|float32
output = func_4118(var_4119)
func_4120 = relay.Function([var_4119], output)
mutated_mod['func_4120'] = func_4120
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4510 = relay.var("var_4510", dtype = "float32", shape = (13, 1, 5))#candidate|4510|(13, 1, 5)|var|float32
uop_4511 = relay.atanh(var_4510.astype('float32')) # shape=(13, 1, 5)
output = relay.Tuple([uop_4511,])
output2 = relay.Tuple([uop_4511,])
func_4518 = relay.Function([var_4510,], output)
mod['func_4518'] = func_4518
mod = relay.transform.InferType()(mod)
mutated_mod['func_4518'] = func_4518
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4519 = relay.var("var_4519", dtype = "float32", shape = (13, 1, 5))#candidate|4519|(13, 1, 5)|var|float32
func_4518_call = mutated_mod.get_global_var('func_4518')
call_4520 = func_4518_call(var_4519)
output = call_4520
func_4521 = relay.Function([var_4519], output)
mutated_mod['func_4521'] = func_4521
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4670 = relay.var("var_4670", dtype = "uint32", shape = ())#candidate|4670|()|var|uint32
var_4671 = relay.var("var_4671", dtype = "uint32", shape = (3, 2, 11))#candidate|4671|(3, 2, 11)|var|uint32
bop_4672 = relay.bitwise_xor(var_4670.astype('uint32'), var_4671.astype('uint32')) # shape=(3, 2, 11)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
const_4683 = relay.const([7.781733,0.780328,-8.760645,-4.908776,-0.220870,5.472579,9.105220,-3.603512,5.390981,2.060694,-7.398171,-6.685404,-9.987504,6.234367,1.611515,5.317962,2.186763,-9.798515], dtype = "float32")#candidate|4683|(18,)|const|float32
call_4682 = relay.TupleGetItem(func_4118_call(relay.reshape(const_4683.astype('float32'), [2, 9, 1])), 1)
call_4684 = relay.TupleGetItem(func_4120_call(relay.reshape(const_4683.astype('float32'), [2, 9, 1])), 1)
output = relay.Tuple([bop_4672,call_4682,const_4683,])
output2 = relay.Tuple([bop_4672,call_4684,const_4683,])
func_4689 = relay.Function([var_4670,var_4671,], output)
mod['func_4689'] = func_4689
mod = relay.transform.InferType()(mod)
mutated_mod['func_4689'] = func_4689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mutated_mod.get_global_var('func_4689')
var_4691 = relay.var("var_4691", dtype = "uint32", shape = ())#candidate|4691|()|var|uint32
var_4692 = relay.var("var_4692", dtype = "uint32", shape = (3, 2, 11))#candidate|4692|(3, 2, 11)|var|uint32
call_4690 = func_4689_call(var_4691,var_4692,)
output = call_4690
func_4693 = relay.Function([var_4691,var_4692,], output)
mutated_mod['func_4693'] = func_4693
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4698 = relay.var("var_4698", dtype = "float32", shape = (8, 1, 15))#candidate|4698|(8, 1, 15)|var|float32
uop_4699 = relay.sqrt(var_4698.astype('float32')) # shape=(8, 1, 15)
output = relay.Tuple([uop_4699,])
output2 = relay.Tuple([uop_4699,])
func_4718 = relay.Function([var_4698,], output)
mod['func_4718'] = func_4718
mod = relay.transform.InferType()(mod)
var_4719 = relay.var("var_4719", dtype = "float32", shape = (8, 1, 15))#candidate|4719|(8, 1, 15)|var|float32
output = func_4718(var_4719)
func_4720 = relay.Function([var_4719], output)
mutated_mod['func_4720'] = func_4720
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4784 = relay.var("var_4784", dtype = "float64", shape = (4, 3, 14))#candidate|4784|(4, 3, 14)|var|float64
uop_4785 = relay.sqrt(var_4784.astype('float64')) # shape=(4, 3, 14)
func_271_call = mod.get_global_var('func_271')
func_275_call = mutated_mod.get_global_var('func_275')
call_4819 = func_271_call(relay.reshape(var_4784.astype('float32'), [12, 7, 2]), relay.reshape(var_4784.astype('float32'), [12, 7, 2]), )
call_4820 = func_271_call(relay.reshape(var_4784.astype('float32'), [12, 7, 2]), relay.reshape(var_4784.astype('float32'), [12, 7, 2]), )
bop_4821 = relay.multiply(uop_4785.astype('int16'), relay.reshape(call_4819.astype('int16'), relay.shape_of(uop_4785))) # shape=(4, 3, 14)
bop_4824 = relay.multiply(uop_4785.astype('int16'), relay.reshape(call_4820.astype('int16'), relay.shape_of(uop_4785))) # shape=(4, 3, 14)
output = relay.Tuple([bop_4821,])
output2 = relay.Tuple([bop_4824,])
func_4834 = relay.Function([var_4784,], output)
mod['func_4834'] = func_4834
mod = relay.transform.InferType()(mod)
mutated_mod['func_4834'] = func_4834
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4835 = relay.var("var_4835", dtype = "float64", shape = (4, 3, 14))#candidate|4835|(4, 3, 14)|var|float64
func_4834_call = mutated_mod.get_global_var('func_4834')
call_4836 = func_4834_call(var_4835)
output = call_4836
func_4837 = relay.Function([var_4835], output)
mutated_mod['func_4837'] = func_4837
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5124 = relay.var("var_5124", dtype = "float64", shape = (1, 2, 12))#candidate|5124|(1, 2, 12)|var|float64
uop_5125 = relay.cosh(var_5124.astype('float64')) # shape=(1, 2, 12)
bop_5127 = relay.multiply(uop_5125.astype('int32'), relay.reshape(var_5124.astype('int32'), relay.shape_of(uop_5125))) # shape=(1, 2, 12)
bop_5143 = relay.mod(bop_5127.astype('float64'), relay.reshape(var_5124.astype('float64'), relay.shape_of(bop_5127))) # shape=(1, 2, 12)
bop_5150 = relay.floor_mod(bop_5143.astype('float32'), relay.reshape(var_5124.astype('float32'), relay.shape_of(bop_5143))) # shape=(1, 2, 12)
output = bop_5150
output2 = bop_5150
func_5153 = relay.Function([var_5124,], output)
mod['func_5153'] = func_5153
mod = relay.transform.InferType()(mod)
var_5154 = relay.var("var_5154", dtype = "float64", shape = (1, 2, 12))#candidate|5154|(1, 2, 12)|var|float64
output = func_5153(var_5154)
func_5155 = relay.Function([var_5154], output)
mutated_mod['func_5155'] = func_5155
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5498 = relay.var("var_5498", dtype = "uint8", shape = (10, 6))#candidate|5498|(10, 6)|var|uint8
const_5499 = relay.const([[10,-1,4,-9,-6,-10],[-7,-3,-3,-2,-2,2],[7,-2,6,5,3,-3],[7,7,-8,10,-9,6],[-6,6,-3,6,10,-9],[1,4,-7,2,-1,-1],[5,4,-4,5,-7,6],[1,4,-9,10,4,-5],[-3,6,7,4,-7,-5],[7,1,-2,7,-8,-5]], dtype = "uint8")#candidate|5499|(10, 6)|const|uint8
bop_5500 = relay.not_equal(var_5498.astype('bool'), relay.reshape(const_5499.astype('bool'), relay.shape_of(var_5498))) # shape=(10, 6)
output = relay.Tuple([bop_5500,])
output2 = relay.Tuple([bop_5500,])
func_5503 = relay.Function([var_5498,], output)
mod['func_5503'] = func_5503
mod = relay.transform.InferType()(mod)
var_5504 = relay.var("var_5504", dtype = "uint8", shape = (10, 6))#candidate|5504|(10, 6)|var|uint8
output = func_5503(var_5504)
func_5505 = relay.Function([var_5504], output)
mutated_mod['func_5505'] = func_5505
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5587 = relay.const([[[-0.347282,7.017648,7.437318,1.018231,8.140328,9.168572,-2.116770,8.364687,9.286996,-1.820050,-2.820708,-9.550115,-4.897623],[1.795496,-0.088190,1.964672,3.957886,4.834415,-8.482829,-5.080240,7.720992,4.673139,-0.525169,-2.906026,0.988374,-2.836220]],[[8.718582,-8.273185,7.356256,-9.571917,-6.557106,-0.277591,-4.271818,-9.973051,-0.312024,-5.245701,-1.996149,-6.623050,-5.616470],[2.071109,9.618404,9.609522,-4.910126,3.764564,-4.926132,9.838689,9.386186,-7.549074,8.320130,-7.460465,1.972722,3.873753]],[[-7.295941,-2.873515,-0.257155,1.464245,-3.468021,2.412416,-1.874115,-0.283565,-1.206434,9.935970,-1.019733,7.288403,-3.716234],[0.102511,-0.058778,4.070942,-3.671576,7.927024,0.335860,5.897088,-0.497679,7.983038,4.012276,5.089056,6.313346,6.200916]],[[-4.926066,-0.643915,-4.884507,8.975014,-4.725764,-1.184088,-0.535624,-0.137472,-8.765962,7.603037,-6.002877,8.863486,2.297259],[0.796944,6.590585,-6.904206,0.041904,-3.334052,-4.304566,-2.549502,-6.581274,-2.211179,-0.696556,3.140611,-1.930892,3.129426]],[[3.896492,-2.538210,6.901083,6.936895,-4.179854,3.572243,-7.535281,9.679401,5.058166,-3.657522,-9.816389,-0.624242,0.544304],[1.104786,7.742189,-2.842637,6.586257,8.076171,-0.928025,6.062754,-3.354824,-6.606669,-5.474690,5.307491,5.466348,-2.351237]],[[-6.198365,-9.486436,-3.495134,3.774227,1.066894,-8.508922,-5.713070,8.890649,-7.583610,0.162885,0.925390,-0.193743,-9.000772],[8.955148,4.129922,9.472806,3.603306,1.237517,-0.773615,6.728902,-3.622797,-7.321737,7.717142,2.643854,0.701473,-8.286884]],[[-0.363477,-0.813976,-8.312732,-5.074908,2.431824,-0.599426,2.749808,-4.850348,-1.920699,0.253317,4.145617,-4.975647,-3.644553],[7.799889,-3.474253,-8.439157,-5.573925,6.827598,6.657980,-4.318617,-2.877749,1.911554,-8.044448,5.099560,9.876440,9.357819]],[[-0.572315,4.588536,1.684441,-4.179148,-5.869611,-0.028032,-3.263066,4.344072,0.694827,-2.912385,-6.806366,9.660139,-0.426205],[-9.214967,-7.606487,-8.293799,0.705319,0.509580,-6.240258,-6.864839,-2.071219,6.116709,6.096671,-7.521684,-2.078698,-0.016235]],[[-0.103051,4.090962,-2.928033,-7.368246,7.583486,5.573069,-6.231170,5.748726,7.650474,7.754770,-4.215081,-6.326904,-1.059269],[-6.944218,9.005307,5.508805,2.949669,-9.195843,-2.661543,-5.425376,-9.522095,-2.276387,-3.052360,6.899078,-9.872972,0.495987]],[[-5.812227,-5.851631,2.763044,7.570669,4.531355,-2.495400,-0.117132,-9.271409,-4.748119,-5.836651,-0.176302,5.043711,3.673909],[-0.297513,-1.211825,-9.262113,0.414289,9.564220,-9.263523,-8.155272,6.571515,-6.660790,8.473728,4.987788,9.483238,-1.739882]],[[-8.620975,-6.144625,4.435852,0.294780,-2.066814,-2.136762,-5.612304,-2.998104,-4.941501,-9.981016,-0.547745,9.524780,6.092114],[2.155981,5.693186,8.721161,4.669756,1.484689,-9.044104,-4.412858,-9.278178,8.318599,-2.176393,2.186904,-4.993843,1.901072]],[[-9.556752,-2.478736,2.664854,-3.731673,-5.297533,-5.361649,6.358740,-9.615691,6.693314,8.164550,2.532604,-8.635674,-4.965084],[-6.823530,-9.616140,7.031749,8.030827,-3.549991,2.993842,5.306941,-8.379836,-5.507323,7.872874,-0.928145,7.430341,-2.263825]],[[-8.791221,5.445409,1.597521,7.722845,3.698505,-7.053418,-7.127678,9.941573,-9.186949,1.635337,-9.074754,-3.373643,-6.989161],[-8.956745,-3.104633,-8.684735,-7.365618,-2.210286,-1.515212,1.803331,-7.505032,-9.580184,-7.236363,0.779467,-3.072029,-3.598668]],[[-0.465914,-1.409185,2.610336,-8.414258,0.104221,-1.028860,-1.921405,7.882340,-7.834636,-0.539062,1.894963,9.062128,-1.415794],[-5.698213,-9.754430,-2.788125,9.591061,2.780590,9.775350,0.774463,9.723066,-7.421726,-1.249821,-9.521334,-7.338110,0.140423]],[[0.791316,-3.573361,7.659674,-2.703326,8.421671,-1.500207,1.943541,7.249570,-2.923359,3.591987,-5.374792,5.084988,-8.066432],[8.364085,3.516703,-1.775031,2.128431,-0.045274,6.131807,-8.651948,3.910627,6.070955,0.957334,-0.353739,3.685717,5.189214]]], dtype = "float64")#candidate|5587|(15, 2, 13)|const|float64
uop_5588 = relay.sin(const_5587.astype('float64')) # shape=(15, 2, 13)
output = relay.Tuple([uop_5588,])
output2 = relay.Tuple([uop_5588,])
func_5615 = relay.Function([], output)
mod['func_5615'] = func_5615
mod = relay.transform.InferType()(mod)
mutated_mod['func_5615'] = func_5615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mutated_mod.get_global_var('func_5615')
call_5616 = func_5615_call()
output = call_5616
func_5617 = relay.Function([], output)
mutated_mod['func_5617'] = func_5617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_5644 = relay.TupleGetItem(func_5615_call(), 0)
call_5645 = relay.TupleGetItem(func_5617_call(), 0)
func_2320_call = mod.get_global_var('func_2320')
func_2324_call = mutated_mod.get_global_var('func_2324')
const_5659 = relay.const([-10,9,-5,2,-10,4,8,-3,4,-1,-4,-9,6,-10,2,-6,-8,8,1,-3,9,-10,-3,-7,10,-8,-7,-1,4,3,-9,-10,-6,-2,2,-10,5,7,5,-6,6,-9,-2,5,4,-2,8,9,4,-1,-9,7,-10,-3,-10,10,-3,-8,-1,-9,-2,-7,-4,-2,-8,-7,3,10,-10,-8,9,8,-9,7,1,5,8,2,8,2,-9,2,3,-5,2,5,3,5,10,-10], dtype = "uint16")#candidate|5659|(90,)|const|uint16
const_5660 = relay.const([-4,6,-1,-2,-10,-2,-4,4,-1,-5,2,-10,10,7,2,-4,3,2,6,-6,8,-1,-6,4,-5,-2,8,2,-3,-7,-6,-1,5,-2,-9,9,8,-2,9,10,6,1,-5,4,-3,-4,4,-8,9,9,-8,-7,-2,-9,-4,5,10,-8,10,-4,2,1,-3,6,9,-2,-6,1,10,9,8,6,1,-4,5,-3,4,-5,-3,1,-6,8,3,-2,-1,9,-6,-9,8,-7,9,-7,1,2,-3,-7,7,5,-5,5,7,-7,-6,9,8,-6,-5,2,7,2,-6,-10,-4,-2,-1,9,8,10,-10,9,-6,-5,-8,-9,-10,4,9,8,9,6,-7,-8,1,-1,9,-9,5,-8,-10,7,-7,7,-4,-3,6,-3,-6,-10,-8,-6,-4,-6,8,1,2,-1,8,-6,4,7,1,-5,-10,-2,7,-9,-4,10,-10,1,1,-10,-1,-5,-8,-4,-2,-5,-5,3], dtype = "uint16")#candidate|5660|(180,)|const|uint16
call_5658 = relay.TupleGetItem(func_2320_call(relay.reshape(const_5659.astype('uint16'), [1, 9, 10]), relay.reshape(const_5660.astype('uint16'), [2, 9, 10]), ), 0)
call_5661 = relay.TupleGetItem(func_2324_call(relay.reshape(const_5659.astype('uint16'), [1, 9, 10]), relay.reshape(const_5660.astype('uint16'), [2, 9, 10]), ), 0)
var_5686 = relay.var("var_5686", dtype = "float64", shape = (15, 2, 13))#candidate|5686|(15, 2, 13)|var|float64
bop_5687 = relay.greater_equal(call_5644.astype('bool'), relay.reshape(var_5686.astype('bool'), relay.shape_of(call_5644))) # shape=(15, 2, 13)
bop_5690 = relay.greater_equal(call_5645.astype('bool'), relay.reshape(var_5686.astype('bool'), relay.shape_of(call_5645))) # shape=(15, 2, 13)
output = relay.Tuple([call_5658,const_5659,const_5660,bop_5687,])
output2 = relay.Tuple([call_5661,const_5659,const_5660,bop_5690,])
func_5691 = relay.Function([var_5686,], output)
mod['func_5691'] = func_5691
mod = relay.transform.InferType()(mod)
var_5692 = relay.var("var_5692", dtype = "float64", shape = (15, 2, 13))#candidate|5692|(15, 2, 13)|var|float64
output = func_5691(var_5692)
func_5693 = relay.Function([var_5692], output)
mutated_mod['func_5693'] = func_5693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_5695 = relay.TupleGetItem(func_5615_call(), 0)
call_5696 = relay.TupleGetItem(func_5617_call(), 0)
var_5697 = relay.var("var_5697", dtype = "float64", shape = (15, 2, 13))#candidate|5697|(15, 2, 13)|var|float64
bop_5698 = relay.multiply(call_5695.astype('int16'), relay.reshape(var_5697.astype('int16'), relay.shape_of(call_5695))) # shape=(15, 2, 13)
bop_5701 = relay.multiply(call_5696.astype('int16'), relay.reshape(var_5697.astype('int16'), relay.shape_of(call_5696))) # shape=(15, 2, 13)
uop_5705 = relay.sigmoid(bop_5698.astype('float64')) # shape=(15, 2, 13)
uop_5707 = relay.sigmoid(bop_5701.astype('float64')) # shape=(15, 2, 13)
func_3835_call = mod.get_global_var('func_3835')
func_3837_call = mutated_mod.get_global_var('func_3837')
const_5711 = relay.const([[0.975975,-2.994014,-8.491401,-7.792700,-4.235587,5.652178,-7.060864,4.184514,-6.985077,-8.243071,-4.481088,0.203841,-5.643674,-7.895521,-5.516556,-4.237895,0.643428,-3.672737,-1.232248,-7.552510,2.326751,-7.242727,-4.979570,-1.238507,-3.319967,9.422637,1.062417,-4.357102,9.155185,-5.923637,7.082582,-2.056482,5.310937,7.928939,5.804080,-9.113079,6.848867,-8.273038,8.567541,-5.418019,-2.153115,-1.939094,-6.585084,1.364025,-4.148992,9.968535,2.181018,-4.417082,1.150986,-4.858589,0.228143,8.987284,-8.476016,6.212502,-3.879342,8.635989,9.697927,-3.436186,-8.120145,-5.749511,-7.341812,6.473915,5.931363,-1.349393,0.107920,5.264948,-5.420877,9.367136,-6.284184,-2.996928,-7.503913,6.838511,5.444084,-1.176146,-3.699500,-9.896007,-3.277721,-1.601674,7.161743,-6.839179,4.162209,-3.722490,1.757325,-9.348175,-9.282491,-2.689957,8.829335,-1.476343,-9.766674,-9.943700,8.102869,9.472184,-2.050206,7.476040,-6.914866,-7.973215,4.691186,7.326248,-5.845608,4.410002,-8.515070,-2.082915,5.364349,8.234950,2.274379,-7.494356,-6.468431,-8.862128,0.646039,8.603323,-1.845892,-8.926218,-8.535525,-8.867340,0.970600,8.924791,7.842990,2.112527,-6.339102,-1.735335,0.930286,6.902941,-4.651062,-4.959028,2.346713,-4.108900,-8.408508,-2.308504,-7.328312,5.801034,-0.372827,-0.980928,-0.777827,-0.214875,-6.526928,-5.511048,-6.567234,0.535352,-8.977492,-7.920015,0.473467,7.839392,0.510713,-8.829214,-5.907361,-0.124797,-1.651374,-1.816448,-4.996610,-1.052681,-6.937461,-4.130343,-4.850964,5.293250,-8.914130,-6.738280,-7.663894,7.094914,4.979773,-9.485003,8.636537,-3.529556,0.338816,3.696714,-1.554744,-4.162114,-9.316149,6.467023,-4.255650,4.727635,-6.015573,1.269961,0.364032,5.265340,-2.863827,-8.225262,-5.444684,-3.599095,-7.973760,9.928948,6.016594,4.014334,6.576281,-8.165615,4.058985,-5.502320,3.004088,9.587477,-7.239337,-0.161181,-7.609666,-4.430333,5.663718,-9.623185,-7.416167,-3.437704,7.245141,-7.023344,-4.160496,-1.329880,-7.591958,-5.799911,-8.260380,2.205108,-4.254566,-5.784579,-9.926228,7.528787,2.852696,9.853436,6.689784,3.098651,3.290731,8.265206,-2.581279,-6.016707,-0.979333,-3.744582,-0.818541,6.766804,8.081633,0.976810,6.702449,-4.933195,-2.917581,-5.327248,2.395096,-7.222857,7.804026,9.350480,3.149808,4.590319,-2.271616,1.254920,8.173164,5.000289,-1.065077,-8.146491,7.916623,-2.712646,7.055134,4.680447,-7.137105,9.334567,-7.203670,6.650068,-3.532279,4.887753,-9.060625,6.932425,-5.983948,8.513339,3.612465,-8.166604,-4.294742,-1.933302,4.342519,-0.053689,0.241141,-8.215107,-9.755334,-4.786074,-6.310091,0.208842,-3.950360,-6.396543,7.927027,1.257586,3.519462,4.717285,-1.905611,1.426149,-7.068420,1.003022,-2.457409,0.158799,7.499594,8.643991,1.583316,-3.543719,-5.174077,-9.661199,-6.082610,-5.570766,9.540218,0.867536,-9.995104,-6.786312,4.520390,-4.937895,7.106491,-2.491074,5.429907,-0.610373,7.005036,-4.714031,1.766747,1.553660,-7.389977,3.368038,-5.849790,5.007845,-4.214607,9.737250,3.878895,0.697089,7.883449,2.251164,8.487882,9.619328,8.813175,-1.466312,7.612940,-5.070097,-3.207732,3.460048,2.384293,6.775825,-6.011201,4.929379,-7.807200,-3.112956,-3.296675,3.887779,8.827408,-7.865287,-3.463971,5.554704,5.335861,-0.334442,-1.294497,-1.880907,-4.840977,9.271101,-5.653143,0.354128,2.217256,-7.413071,2.339418,9.515582,-9.675681,8.564846,0.685490,-4.615185,3.481257,-8.064714,3.425162,1.536606,-2.022743,-3.341126,0.720772,8.992429,-4.056745,-9.564113,9.137713,-7.786598,-7.076287,8.700430,2.322317,-9.307723,-5.137166,-5.859569,9.637262,3.801014,-2.152123,-5.922835,6.062310,-6.899732,7.623490,-6.017763,-3.992639,-2.227769,-7.048909,-7.846925,-2.111912,-5.053390,3.053149,-1.051721,-4.866876,-0.816465,8.398489,-4.822973,0.229169,-6.124589,-8.423897,3.120185,-8.723404,3.033070,4.492294,-8.991731,-4.158171,-6.017673,8.514320,-9.177649,3.049919,-1.835838,0.425268,9.048243,7.729867,8.571771,-4.320316,-1.525070,-7.171466,-6.628497,-5.510620,2.476250,8.113221,-4.081587,-2.694000,2.062684,-7.967101,3.387062,-8.041449,-5.533684,-6.130456,9.083313,-0.761145,1.518661,8.138118,0.403418,-0.027973,-0.153307,-4.122326,-7.366838,2.703220,-4.392754,3.783181,4.303251,8.649819,3.598622,1.108204,-8.695605,6.870955,7.618333,7.276049,-9.785335,6.649045,-5.324241,4.946769,3.681310,-2.669276,-8.420850,2.762519,6.098422,5.858104,-5.546449,-4.366082,3.645815,2.683995,-5.117938,1.818532,-6.697060,-7.274042,-3.795156,-5.269575,-8.814759,-4.546171,-2.914597,6.687064,-6.591874,0.444345,1.700265,4.792499,0.850173,8.969290,-1.818414,-2.170513,-8.058566,1.083856,-9.717675,-5.123853,-5.540667,-8.837932,-1.686322,-8.414464,-9.309059,4.266365,3.388205,-0.271047,5.092746,3.072674,-7.333309,3.191998,-6.313902,-7.174414,-0.654850,7.537236,7.785107,5.584467,5.172446,-8.994485,9.781142,-4.460624,-0.133540,8.374498,-6.420143,2.826000,-0.941701,6.317695,5.636824,-3.329646,-1.455721,-1.265831,2.186738,7.004617,-6.004957,-0.410336,-5.148465,-6.678944,-9.835488,-7.085247,-5.149423,8.747230,-0.217051,0.472139,-8.780088,3.760628,-2.789581,-9.178732,-8.990728,-3.567367,7.606008,-2.858402,4.049989,5.663425,1.516825,4.205566,0.118843,-0.395526,7.242259,-0.801186,8.970412,6.482294,1.234236,3.537114,4.789223,-8.293780,9.306809,-9.451569,-9.823390,-9.067163,-3.737190,4.942893,-3.635930,9.277368,-1.810808,-7.072864,-1.494994,0.467372,8.175966,3.552924,-4.122013,-6.961999,-4.027589,9.756962,-3.364759,-0.213480,0.484866,-6.363226,-6.619549,9.306811,2.651884,-8.402859,6.556240,-3.629071,6.806659,-0.671051,0.263034,8.778164,8.272017,-7.606862,-2.759711,-2.600380,6.200704,4.785877,9.868661,-6.584111,-7.524524,-5.628375,-7.625560,5.197384,-1.542258,2.983359,-7.262313,3.778341,2.139714,2.237909,8.777119,1.466419,-7.669905,-5.559227,-3.056328,6.136388,5.641542,-3.662065,-2.930487,8.565882,6.516407,-8.466907,9.396291,-1.261825,-5.370760,-6.420910,4.200971,-0.150314,2.320315,2.086203,1.973016,-5.688337,-8.746716,-0.277215,-5.608192,9.279695,-1.754992,7.384214,-3.173612,7.665649,4.485506,-3.191572,9.321268,1.889049,4.046961,-4.366382,0.783879,6.721815,-5.687860,-2.985932,-7.001658,-9.905639,2.543728,-4.164674,0.184237,-2.240932,-0.004859,-4.839044,6.986463,-8.931761,-5.133881,5.138769,7.134199,-6.483079,-3.994637,5.410044,-7.228063,-4.553972,3.091327,7.156806,-7.296239,-8.422006,-2.601682,-8.189479,-1.158882,-0.063635,-2.561896,-3.787075,6.581767,1.761600,3.158977,-5.591691,-5.457944,3.616450,8.362726,4.855851,0.030936,-8.809286,-0.568088,6.118686,2.046545,6.277567,-7.040824,-2.105141,-9.869908,6.770516,-6.483097,-8.661918,-9.461925,-0.691970,-7.069046,8.797196,4.348105,-1.469902,5.003544,-4.425514,8.696286,-5.785552,0.243387,3.927619,-9.196952,6.376591,-3.565386,0.069519,-1.038947,7.339694,8.766388,-7.953012,-9.816912,-4.402793,-4.430186,6.645555,4.935212,2.747658,-8.763547,-1.213933,-9.521483,1.783247,9.514014,1.753593,-8.605157,4.726078,-6.420206,8.888354,-1.059786,-1.518280,-9.699981,-8.959997,3.160325,2.339408,5.879744,-5.614036,1.250683,-4.585320,-1.859515,-1.239517,-5.809337,9.826135,0.543172,-4.336370,-0.514407,4.851685,-2.604253,-1.029078,3.648202,1.738372,-0.196282,-7.062715,1.083531,-6.496875,8.637368,-2.315653,-9.958893,-8.007339,-4.123760,9.327536,2.152708,-9.835731,2.196355,2.863190,-8.777133,8.097732,-2.482107,-5.893401,-1.694070,2.166125,-8.697376,-1.085683,6.086442,-8.872373,5.469211,4.069640,-8.461367,-6.703644,-1.348656,0.990163,-0.259008,0.031682,-3.899830,-6.139481,5.975885,-8.069412,0.322155,-5.079685,1.484528,1.899209,1.259275,1.096797,-3.694254,7.344321,0.600301,8.594768,2.996449,-8.833768,-6.362937,-0.588830,8.492190,8.252145,0.006554,1.878886,8.637098,2.089597,2.380727,-0.811455,-4.602291,1.185504,-4.292469,9.769024,5.368513,-9.570587,-6.511989,8.907901,6.288101,5.970275,3.103162,-5.452343,4.770469,9.093682,-4.296440,-9.800946,9.461308,5.481991,-8.194431,6.988274,-3.093307,6.780063,-4.774892,-7.542914,-5.424135,4.435048,9.071566,-8.922780,3.149896,6.919893,7.782099,5.240371,9.933233,4.353262,6.465233,-3.597376,-6.031870,4.457903,-5.184700,-0.801767,8.344886,-6.466835,9.953190,2.428314,-8.378964,7.025343,-9.667542,-5.038588,3.205162,7.089691,-2.927354,-4.870966,9.598861,-1.247736,-0.618751,-2.786928,-7.154172,-6.023000,9.627354,-5.463559,-2.553414,-1.612049,-2.655695,1.199786,-9.153411,9.823807,-2.792938,0.402797,7.321404,6.077883,-8.361893,0.606161,1.744483,6.482601,5.960240,-0.034641,3.282271,-8.305298,-5.170801,8.627350,-7.718324,6.241880,-6.369512,-8.578431,-9.354182,5.217126,-6.425751,9.916226,-5.391172,-0.387382,8.721269,-1.984313,2.626461,-5.008447,-5.384928,-3.495143,-6.103303,2.398196,-4.356509,-8.661262,5.704804,-3.057498,-0.574670,1.933804,-6.090284,-4.083144,6.697909,-5.842080,0.288770,-5.507025,-9.808059,-4.894942,-9.275747,7.704306,-8.552993,-8.341680,-6.134522,3.034569,-0.077881,4.297420,-3.459376,-4.512465,-2.230417,7.238844,-4.029008,4.163208,-7.500765,2.673652,3.549193,-8.870175,4.284029,-7.346227,8.943615,-6.563154,-3.320942,-5.977809,-4.090079,-0.259764,1.036128,-0.194450,7.977113,-0.048433,-7.772610,6.664918,-9.478028,3.966602,-0.788117,4.073346,5.066751,3.868034,-5.719942,-6.369998,7.667768,3.582473,-8.295822,-6.709122,-9.103880,-7.175582,-4.166150,-4.394552,6.225144,-6.240791,5.288501,4.554540,-4.256590,3.265103,-3.817245,6.300779,-1.204292,-7.840274,-9.375909,5.572056,6.092060,4.245210,7.641087,-2.394317,4.671715,-7.068011,8.761076,0.037272,-3.423750,-4.882908,3.016844,-4.765106,-9.498857,-8.387290,7.191003,7.204829,9.088816,4.259726,6.227613,6.514413,-8.526887,5.780040,2.117454,7.221092,8.779440,-1.780873,4.911776,1.673512,2.941746,0.814152,8.881546,6.998116,6.967301,4.420925,4.826659,-9.498972,-1.781014,5.164155,-7.350577,3.903591,-7.728036,-4.774571,1.062585,6.571311,-8.160968,8.379277,-4.755712,-8.989909,3.300390,-6.158908,6.647844,1.370478,-8.601997,4.545012,9.552118,4.006148,4.543036,-6.107367,8.067842,2.032826,-5.525818,2.652659,-2.086227,-1.981920,0.550379,-4.264835,1.381137,-9.720492,-6.716321,5.996064,-1.889812,0.436098,-9.661617,-6.731003,3.793244,8.239717,8.643122,-8.810748,5.038359,2.713672,0.708268,8.690143,8.589675,9.228794,1.929467,-8.484225,2.783197,7.814543,9.546284,9.619770,-1.383233,-1.587331,5.582232,5.660938,6.283358,5.416611,-3.148383,-2.184674,-5.884520,5.642462,-6.494216,6.627241,3.857558,5.783579,5.941085,7.791567,-5.273835,0.164251,1.817244,-8.982833,3.531195,7.317533,-7.358887,-0.712237,9.882922,-1.918307,4.935795,7.570450,8.469977,1.932649,2.492222,-7.562441,-3.245357,4.086241,-1.283423,-9.618705,4.976888,5.877098,1.784438,-7.530501,4.000915,-4.451594,0.609349,8.575649,1.986756,5.672773,3.451766,-8.356971,2.438691,8.748024,1.878069,0.667669,-2.165272,-9.643975,-2.100186,-6.390053,4.073354,-9.277934,4.899921,7.126254,-3.435313,7.348347,-2.672795,8.245696,-0.064759,5.131906,6.731042,-3.883217,8.803310,4.145636,-2.038321,6.424999,3.831887,-6.033165,3.946988,1.625614,-1.586982,-2.160984,-9.611851,-6.771073,-2.848864,-9.588995,-6.727655,5.918593,3.206864,-6.721812,6.974159,8.116249,7.036008,2.817363,-4.913266,8.154567,6.724377,5.736011,7.855131,-0.723608,-9.638348,0.124312,-6.942760,-7.669903,-9.148787,1.416864,4.833569,-6.782501,-5.125649,1.008719,-1.286417,1.145892,-3.537601,4.418825,-0.781832,-8.485947,-9.971169,1.374634,-4.365813,-0.533782,-3.136929,-6.236312,-8.080835,4.455689,-4.729427,7.301746,6.402506,6.555113,-2.393746,8.031949,-6.050364,1.894026,-4.005363,6.274514,-3.560628,3.277861,4.762146,-5.683328,-1.756676,-2.379875,3.301387,0.193753,-4.500825,-1.328176,0.094688,9.843379,6.348857,-1.150976,-0.645602,7.046823,6.882916,3.276256,-5.596892,-8.488565,9.859261,-3.722180,8.290216,8.753091,-5.696541,-1.141347,-6.389966,6.769344,-4.326317,2.475011,-2.502396,3.118958,1.510488,-5.325417,1.168556,-4.797508,-4.575173,9.494052,-5.200599,0.557489,-0.575213,-4.036448,-6.990644,3.473612,7.388130,6.223099,4.201137,0.939796,7.514065,-0.824406,-8.954835,-6.959759,2.291947,-6.916224,-4.714323,-6.241433,9.751532,5.086277,6.034883,-4.039979,5.925378,-0.843946,6.405085,0.969102,3.520684,0.194600,-3.343749,-3.562092,3.287408,4.103346,4.619206,-9.062507,-7.653098,-0.728148,-0.990172,-5.020478,-2.537812,-7.423998,-5.981821,-8.940186,-5.006443,-8.878385,6.087873,-5.146298,4.951640,1.070457,-9.933098,-1.663618,0.830141,-3.774096,1.953612,-3.726436,5.231431,9.760881,-0.437977,1.182371,7.164417,-9.341095,0.375951,2.134009,-7.166615,0.090704,6.510518,-9.195263,-8.807526,-7.313675,9.533429,0.108844,-2.531956,9.711706,-5.471733,1.898715,-6.428199,6.405432,-0.616648,-9.747308,2.122400,5.152916,7.368018,4.230836,-6.856793,-3.617968,-6.646483,-7.513250,-0.636115,-0.040555,5.876123,8.597661,0.923034,6.258791,8.788977,-1.521307,5.275766,5.438781,3.544741,-5.567661,8.982472,-7.592427,-3.385540,-8.724950,-0.923423,6.478698,-6.029388,8.568639,0.580189,1.958288,-1.771399,8.084576,-8.244147,8.266622,-0.301461,0.891579,-6.894801,2.897838,5.176596,0.465130,-5.017204,2.152885,3.488350,-4.132853,1.877539,-3.602513,-3.124194,5.429342,-9.369474,-0.698208,-5.410353,-0.731459,4.838779,2.785123,3.734880,-9.636566,4.793334,-8.489842,-0.819188,-5.050007,8.942804,-3.665436,-3.247802,-4.663181,-7.495113,9.649125,-8.233347,9.396860,-4.157862,-8.785254,3.983088,7.700457,-9.693036,-8.230717,2.606619,-1.048902,7.072538,-5.556046,-2.773968,-2.921560,2.363360,5.115032,-2.535717,-1.179679,5.249592,-0.637062,0.007711,-1.403162,-0.260992,1.822396,5.664283,-6.090447,-8.397780,-5.806211,4.069602,6.020106,4.109165,-8.513369,1.651287,-2.250591,-5.743635,4.954693,-4.553395,8.078390,-8.052749,-2.352328,7.047447,-6.618462,0.505030,-5.661005,-7.889561,-0.662383,8.923738,4.320271,8.583715,0.680673,-1.094029,0.940383,-3.563150,5.273938,3.371701,-6.617844,-8.580991,-7.960558,-9.935003,-7.383374,-3.882211,-0.033632,-2.626508,-1.294033,4.391368,2.963550,7.079459,-9.435311,1.331192,-6.522457,-3.424581,1.794066,-0.188297,-3.112752,2.071109,4.297178,9.205000,1.011866,0.563616,5.571400,6.457766,-0.076896,-5.262519,1.265399,2.634180,-7.248910,-8.414436,-7.206584,-1.300147,3.435246,-9.545961,7.006244,-1.518868,2.105884,4.654544,-6.286812,6.823536,6.021203,-8.090154,0.449493,-9.733736,9.846938,-5.340713,6.507599,-9.940363,-7.223763,9.968925,7.176430,-8.087251,0.965507,2.551833,-7.716697,2.762997,-1.219575,-2.722763,1.224039,-1.579841,-3.376152,-6.354676,8.733443,-4.407291,3.327881,9.732327,-5.704754,2.168841,6.559005,6.944251,8.228717,8.135019,-8.211351,-0.141818,2.180184,-9.244745,5.023994,5.436382,-4.631365,-7.456019,-6.326173,-8.585565,1.126523,-8.756776,-2.262292,-8.063354,-3.450594,-6.564911,-5.826516,-2.035784,1.914778,5.613138,-1.438261,8.082961,-0.125491,-8.559453,5.422409,9.671179,5.196758,-5.018460,-3.237427,2.896280,-2.562086,9.183572,-7.808116,-7.824235,7.987527,-3.977968,8.643043,-5.362397,9.032942,-3.468757,9.493503,5.780256,5.047260,-3.595292,0.357644,6.498053,6.298659,-9.567072,-7.263658,3.472012,-5.792785,2.853740,2.452948,6.032930,1.638907,-2.426349,-2.408970,4.070291,9.977988,1.347412,5.873450,-7.034648,8.170481,8.082744,-5.404390,7.863705,-8.564626,-1.637385,-2.517963,7.485948,2.619186,-9.983333,3.962325,4.589668,-8.112985,2.114816,7.129702,-9.688223,-2.334293,9.386693,2.824498,1.670478,5.956675,1.683919,-5.384768,7.250071,-2.552651,9.334993,8.918892,-8.597648,3.785457,-8.320233,-8.285679,0.073904,-0.741373,1.837513,-5.904730,4.171781,-2.726873,2.021787,1.510695,-3.500866,1.885821,-0.265833,-5.559193,-0.124333,-2.094200,7.419026,6.066451,-3.457949,1.160618,6.252356,-5.923953,3.546021,-5.220871,1.446790,-2.614486,4.847096,4.549273,-8.955889,7.816934,4.777227,1.642108,-7.824750,-7.448094,-4.496084,-6.830839,3.879269,8.974909,5.116879,8.775983,1.720377,-5.926789,4.313506,-1.740733,2.895226,-3.535726,-4.404078,9.422560,8.166438,2.744618,6.238695,7.875345,-0.213455,-8.938226,-7.455722,6.767156,8.288941,0.376950,4.814440,-7.809021,6.287360,-7.660247,6.664925,-5.365479,7.302884,-7.170532,7.770796,2.919835,-0.097129,1.439739,2.098715,1.283924,-1.838682,-9.493444,-3.305582,-5.903915,3.903170,0.326625,0.474874,2.831029,1.960073,6.258672,-2.274817,7.754724,-0.838856,5.019860,8.172894,-2.909883,8.598845,4.655217,-1.955762,0.589669,-9.196634,-6.773113,-6.804403],[-3.865616,4.495245,-9.647155,-8.914387,2.857245,-3.025989,0.790409,3.107988,3.629317,-7.883255,-8.794730,0.722141,-8.587137,2.004960,7.237661,0.086894,9.147627,4.743860,-6.945193,8.734211,1.888077,-2.911363,5.590266,-1.081740,0.928360,-5.809167,2.859628,1.659991,1.186615,-3.744401,0.630161,2.029407,2.775808,-8.186176,-4.789583,1.579491,-0.521068,-1.756635,8.796089,-1.335774,2.539063,-1.057659,-9.231923,0.791418,-1.202124,-0.543059,7.712485,1.863807,9.963310,-2.720428,7.914119,8.807931,3.413992,-0.526619,-3.367694,6.261519,6.961362,4.403711,-4.707210,9.628371,-5.084177,-6.897536,1.864201,-2.305035,5.724008,3.702595,-9.929721,-9.654582,-0.338988,-6.014869,-5.511526,3.012377,-0.131650,8.715005,4.201032,0.193162,4.535793,6.174215,3.849126,0.855765,-9.072914,-5.436989,4.204269,-1.997995,4.643271,-1.179967,5.967859,2.026178,-7.633617,-1.281895,6.950074,-4.212130,1.020895,-5.468414,7.748042,3.355481,-5.397286,2.695575,9.020053,3.043919,-5.287976,-3.228878,9.941476,6.264301,-8.462655,7.219716,-9.035139,-6.584261,8.374667,-7.012176,-0.691556,-1.826098,4.303073,-0.322119,-9.512112,7.058879,-0.386081,-1.990197,9.851813,1.690185,4.459784,-5.123265,-4.351416,5.514773,0.469574,2.580559,4.942334,-7.696257,7.365351,8.998947,-8.291336,-2.509719,-2.030819,5.654281,6.536271,-9.234977,0.677476,-2.207170,3.210079,-8.121333,9.932717,3.960874,8.084013,-2.247531,-2.844749,-2.784236,-5.736943,6.754574,0.846807,1.331556,-6.963327,0.576438,-4.402969,5.356055,6.659525,-5.887732,3.988959,-6.887081,1.207658,8.837952,-7.380798,-9.892495,1.554538,-5.242797,-5.147842,1.395975,4.317920,3.324317,-0.313470,1.992827,-2.681523,-9.123003,9.152579,-8.613838,8.778683,2.699803,-7.231336,0.206075,5.625248,-7.371272,9.494514,-5.156279,6.554554,-2.612960,6.511889,9.547985,6.602528,5.216233,-7.046967,0.857510,-8.874014,-0.955769,-7.517920,-5.504738,1.881406,-7.422032,-6.270489,0.784997,-2.947816,5.206187,5.982202,6.437150,-7.221244,-7.901359,-2.678517,5.786713,-7.946514,5.519596,6.759853,-8.271867,2.244510,8.430370,-1.434571,9.491475,-0.605897,-0.783054,4.549437,-4.433826,-1.226158,6.421762,-6.878881,2.575157,-0.440279,4.480719,-4.183789,-7.827383,-2.353465,4.274262,-6.404593,2.636723,0.167350,-6.949988,0.277622,1.660974,5.221037,4.015231,3.229719,-9.941260,3.362330,3.481837,-0.195894,1.694540,8.331953,1.243087,9.950893,-9.444512,-2.952910,-2.935862,4.440344,7.423561,-0.665667,-7.335358,-3.508811,5.107712,-8.419050,4.008230,-4.338694,-9.618422,-0.708931,7.129280,-3.629276,-9.579363,-4.652108,2.368510,-6.605816,1.273288,5.064192,-6.719401,-2.526634,7.336213,-3.976788,3.609575,-8.100842,-8.430849,3.378707,-9.341399,8.061058,-7.346903,7.535498,4.610079,7.376351,-5.792285,-9.694043,-3.621468,-5.888875,-6.271253,-4.753822,7.146773,9.601946,9.410544,6.684612,-3.166752,0.946594,5.164201,-2.726753,-1.711012,8.566787,-7.871490,-3.585116,-6.407939,8.214218,3.633354,5.103468,-7.544910,3.971015,4.987155,9.531755,2.281211,2.885001,-7.696468,-6.716232,8.593147,4.037719,5.903643,-4.377032,3.212071,-3.448717,8.347415,8.735781,-1.890003,-8.338845,-2.840945,-1.397486,-4.371735,-8.437388,2.084434,2.355972,-8.193422,4.094921,-0.424799,0.657407,7.831538,9.373293,9.051918,-0.798716,1.247928,-4.393263,-2.832964,3.998446,-2.505773,9.994830,-2.072621,-9.964419,-1.844978,8.142532,3.551324,-7.277873,-2.852850,3.121494,-6.873671,-2.690639,-6.252306,7.748986,9.270690,1.527119,-5.785436,0.064550,-0.895600,4.559297,4.829965,6.432756,-6.610602,4.418519,4.192129,-8.422761,-6.823164,7.498871,7.605964,-2.169262,-7.653668,-5.766513,-6.456697,5.285947,9.957855,4.544347,0.296081,6.256136,-0.548627,1.416565,-0.899493,-4.119642,-8.097638,6.034607,-3.038974,-5.394989,-0.458697,-8.709170,-2.019864,9.147790,-7.355668,0.795879,2.175856,7.528434,4.130402,-8.181815,8.023853,2.697280,-2.920942,5.531358,-9.474215,7.182606,6.635637,7.248280,-7.043402,1.826657,-3.037747,-8.586136,-9.798472,7.601715,-0.241538,0.249589,-1.034180,8.121370,8.840493,-8.187512,-1.732835,-5.495672,9.895694,-8.597375,-8.024026,-6.688680,-8.818013,8.977680,7.993580,-1.661021,-4.865051,2.448361,-8.177385,8.626913,5.082461,6.493844,-8.047854,4.821925,-3.967435,3.719384,-2.240307,7.412597,-8.580532,9.658051,0.637173,-6.384860,9.326416,3.204349,-4.235877,4.157058,-2.967281,-1.058483,2.017926,-6.422205,9.636224,-4.856850,0.330012,-8.135416,-4.451638,7.614618,0.962537,6.555215,7.432965,8.278595,-8.723525,-1.816373,9.685892,1.994728,-8.476024,-0.740889,0.344388,3.316741,-1.042312,-5.974930,5.955528,9.576779,3.802347,7.334436,1.347403,6.301176,-7.852907,-1.877159,-2.493857,-8.016209,6.970545,-3.741836,2.635788,7.174488,7.290026,2.200768,-7.623403,8.108888,4.287416,-6.165608,8.288356,-2.324184,2.473284,-2.474489,-7.175262,8.685502,6.274654,-5.340631,4.194859,0.806922,-4.793518,-0.242556,2.488534,-8.351010,-4.350059,5.567663,-8.910747,1.940107,-4.301620,5.163234,-7.056333,-7.672271,-5.915120,6.074276,-7.426408,-8.991352,5.676841,8.534614,5.199961,8.703429,3.518364,4.430105,6.478660,9.008733,-7.122771,-1.796900,6.872860,5.239199,-5.462017,-4.452985,2.687190,3.207891,6.441491,0.575177,-9.725425,-9.005502,7.935712,-4.318673,2.860870,-6.279136,-4.209842,-7.592780,6.030284,-4.433639,-2.039325,-0.205901,2.113458,-7.160043,4.901325,5.071202,8.314090,2.334001,-0.617430,5.160947,6.069560,3.240350,-5.301379,-8.496370,0.944026,3.774715,0.141657,7.773307,3.057628,1.302867,1.685704,4.288374,-7.576389,0.893568,-4.800034,-2.957885,-2.606732,1.633305,-9.238821,-9.979155,-9.453967,5.445387,-8.259048,4.927999,6.425279,-2.467259,3.738630,7.337561,-5.849330,-1.637718,9.885155,-6.086201,2.753191,-5.164315,6.438320,5.849101,1.201975,7.133211,-0.652809,4.754907,9.016534,-0.943878,6.631573,4.763377,3.311472,-2.968342,-1.639810,-8.594985,9.972735,6.067235,-2.089030,-7.082744,-2.475845,4.901264,-8.667188,-1.335207,-8.713444,6.294655,-3.441654,5.797971,-6.045444,-4.551900,-7.533738,-6.682858,1.547907,4.327565,2.807961,1.924804,9.854034,-7.627991,-2.352207,-5.988885,1.864906,-3.745295,-9.874122,0.226783,-5.189032,0.184294,7.318964,-3.553592,-5.443703,-1.704661,6.914806,3.464135,-4.362884,0.115202,-0.785333,2.177344,6.060288,4.590072,2.244509,-7.811071,-8.384892,-4.438828,-7.659392,-4.731258,-3.307149,-8.189018,2.837100,6.348935,2.214359,-4.265563,-1.596816,6.391777,2.833276,0.918753,-6.001204,-3.319886,0.493008,-1.400418,1.347591,-3.886215,9.072888,-0.381435,-5.281847,-2.976388,-5.971744,4.348126,-0.032262,-8.404764,3.848118,-7.147728,0.101143,-5.150086,6.601506,-2.153612,-3.642011,5.979149,7.657043,-7.816134,9.214948,1.185954,2.861141,-9.757428,-5.599307,2.721663,-7.378798,4.102364,6.825565,-1.739213,-7.431556,7.041002,-5.853067,-3.499690,-3.497266,9.250085,8.546028,1.832190,-3.620005,-7.305653,-6.536987,-6.220111,5.618242,1.404096,-2.034093,9.999449,-3.307325,0.983296,0.042334,8.919610,-4.918716,9.366465,7.981321,-3.508766,-1.453984,-6.489423,-5.150449,5.180322,-8.576940,-1.675016,1.137986,0.520661,2.318239,-0.359881,-2.082239,-2.382403,-0.695411,-3.023916,1.284845,5.960618,1.900127,-5.533096,2.894111,2.759212,-6.376763,-4.824763,-7.232195,-5.696141,-7.130089,-7.440077,-8.488698,1.427361,9.929036,-1.056376,-3.338005,-0.597485,-7.915877,9.632845,1.506965,4.777012,9.629172,7.961474,-1.779583,7.962674,-8.438064,7.408224,-5.175360,0.321658,3.206378,-3.181061,-1.743964,7.970274,-7.570952,-4.673873,-8.554855,1.544014,3.548894,5.712202,-7.579711,-6.409071,-5.695985,4.967040,-2.200712,-5.657369,6.579919,8.901807,-9.556917,-6.390112,2.279304,-3.670988,-5.484212,6.747208,-9.737564,8.994086,0.383407,4.544259,-5.201507,4.952112,5.113286,-7.901531,-0.470599,-3.454563,-8.511288,9.692798,5.278232,3.733324,-3.370781,3.817574,4.472332,1.269477,-0.189200,0.875888,-7.996082,9.278159,-7.976805,-1.506865,6.513178,3.875938,5.835097,-1.560435,-4.898213,-8.158619,-8.806042,9.377428,0.228069,5.977699,1.849615,-8.820318,1.867300,-6.940952,0.162067,-4.398934,9.083985,-6.028754,5.821554,-8.864120,2.107127,-6.379577,-2.914950,0.495439,-9.249251,-4.437348,4.487117,3.911386,-1.544440,0.663801,-4.864029,0.900947,5.956728,-3.355508,-8.097568,3.627455,-8.146546,5.347852,3.693964,-2.667894,8.270653,-5.839271,9.408828,7.584044,0.827141,2.224246,5.881453,8.676468,-8.441904,1.888430,-7.025908,-6.399783,-4.778599,-9.297925,4.382958,6.099020,2.990530,3.488786,-6.120010,-5.019946,5.495905,3.814701,-5.263817,-1.143922,2.028855,1.445100,-9.791483,-7.773195,-6.608843,-1.236040,4.857819,-8.450985,1.286704,7.816460,7.448219,4.821642,7.606015,6.215676,-2.183624,-5.895753,4.590163,8.063237,-5.216609,-6.730419,-3.945197,-0.844179,-6.135484,-3.039545,-8.484326,7.435012,-3.867268,0.458744,-4.694209,8.198773,-9.628735,-2.852139,-3.116830,1.546802,3.978552,6.709120,-8.664641,8.514544,-8.374087,9.488193,3.636260,-6.263321,3.309340,7.627456,-0.456648,-4.806862,-1.568724,-2.855825,1.930122,3.639029,0.313714,-0.245438,-4.741462,7.276354,-8.295065,-7.013836,2.388107,0.374897,-4.472397,-5.998992,8.777329,8.069901,4.435729,-1.869124,7.032542,6.359816,-1.395825,-2.550524,3.564396,-2.627461,-0.127046,8.249791,2.765527,8.574368,0.024582,9.913695,-7.506456,8.434931,-8.751486,-6.973797,0.972072,4.135298,-3.533344,0.167000,3.955062,4.287630,-0.777236,9.293270,6.688006,2.576743,1.983753,9.528425,4.216420,7.048082,2.696999,8.602637,-5.954950,-7.524807,-0.145926,-4.066301,9.225289,-9.120276,9.541594,-6.938918,-7.926494,2.346491,-6.161515,6.518326,3.522306,5.160273,6.716770,-3.429871,9.870307,-9.190493,-3.366140,0.663975,-6.545793,4.452691,-0.837816,-4.269740,9.587376,-1.399103,-2.194197,2.742740,-2.888558,-4.642650,2.796025,9.788667,-6.356046,-8.692370,6.480597,-7.684932,8.135816,7.535718,6.465513,-0.287334,7.837110,-9.234358,6.844255,-2.423611,6.632988,9.970892,0.891955,5.505878,-1.963112,-4.313257,-9.621613,8.070210,-4.076641,9.076927,-5.869530,-7.763860,-0.049659,0.071268,-7.331710,0.209801,1.817415,-8.603856,-1.105076,-6.589637,3.334387,-4.368738,9.369157,-9.736474,-3.070287,-5.345715,6.446090,-7.520262,4.569257,1.954399,8.676775,4.330521,5.692410,0.867539,-0.414072,-3.995417,-9.629184,2.405360,-4.052595,6.484715,2.020167,8.439759,-2.564123,-0.744515,-0.288696,7.081931,-0.820912,-7.925887,-1.473403,3.258054,1.430897,1.636437,-4.391388,5.994597,-2.310539,7.612574,-9.733540,-9.067123,3.810634,3.267729,5.488472,2.976865,2.505089,1.288033,-9.852731,-1.374570,4.906030,5.196591,-8.312579,-9.492290,-1.287715,-1.176078,8.900119,6.434516,2.758850,-7.129459,-9.922803,7.125427,9.383377,6.639788,5.925816,1.282013,1.487553,1.527265,8.453641,-7.621254,0.048752,7.477186,-9.775910,7.712884,2.916362,-8.729742,-2.954795,2.485554,-5.095824,7.891108,6.243340,-6.116484,4.868591,-0.443002,-6.551387,-6.665720,-6.557121,-8.154095,9.506073,-8.459889,9.150740,-8.754499,-9.322082,4.995743,-8.607285,6.195994,2.015226,8.930304,2.283429,7.965430,-4.483073,6.014917,9.364137,7.829118,-5.000138,2.506954,-7.512435,3.838988,-6.898604,-4.869414,3.978241,-9.906960,4.213616,5.159596,7.542470,-7.707309,5.056613,-5.217254,5.010557,1.016948,-5.068907,4.856040,-4.955941,7.357174,1.365436,6.093046,2.260583,6.265120,2.552507,5.340652,-2.053359,2.746651,-6.036900,-1.290090,0.844651,4.716717,7.709889,3.327109,7.241290,-8.622247,-0.511620,9.733299,3.817454,-9.297313,5.319394,8.680298,-9.833796,0.808892,8.325011,-5.911307,6.075667,-0.653164,8.847471,-1.471459,-6.979888,6.695757,8.093304,5.548700,-8.677267,8.671525,8.094825,9.194119,0.238936,-2.209444,-7.928265,-5.953753,-4.914942,-7.886196,-4.509020,-5.979210,3.107506,8.006745,-3.663886,1.115603,-3.881606,2.218197,-2.228230,0.222859,4.287149,-4.491814,3.719188,-9.536851,0.670258,8.320171,8.096135,-8.680562,7.833993,0.633268,-6.937892,-7.116434,-1.348017,3.860285,-0.591099,-1.570135,-5.760300,-2.209347,1.683366,-7.022670,9.273470,-2.905894,9.826989,-7.513491,-2.750553,8.933478,-8.466427,-1.264002,3.543668,2.382054,-5.556913,0.285411,-0.331538,-4.344272,-5.714348,-6.341756,-5.997131,6.369062,-9.611166,3.343359,5.602726,5.123622,-9.816900,-6.551556,1.951315,-4.058049,-5.673717,8.440791,7.704127,-3.739991,-9.719293,9.316195,-0.001807,-5.532179,-8.818402,2.352312,-4.719695,-7.967586,-2.868166,-7.701122,-5.020252,-4.700477,3.626719,-4.540715,8.779010,-1.981932,8.545540,2.654892,-3.478053,-7.928794,5.284800,9.152027,8.573144,-6.028255,-5.767587,8.306646,1.549589,5.819468,8.612787,2.999251,2.748576,-0.044541,-5.064457,-4.071046,-1.827195,7.023002,-1.442027,1.724413,-4.455024,-2.384978,0.685160,-6.271478,8.648507,2.202193,3.011117,9.550097,-8.609340,8.237174,1.330250,-8.052935,7.698829,3.700162,-1.820242,7.577751,8.174306,0.824002,7.752843,5.804230,-8.443288,-8.717644,-7.166204,-8.569047,0.519945,5.169448,4.658981,-3.656455,5.315790,-1.434875,1.438794,6.486342,1.592158,2.690377,-1.756879,7.555043,1.274756,-2.186366,-7.432490,-6.276403,-1.848253,-3.555764,7.345606,-1.740362,3.287230,-8.497527,-0.071799,0.511784,6.821212,5.134337,2.955976,-2.058926,-0.505398,-4.273093,5.359926,-2.448245,-4.710896,0.638695,-2.659248,8.091978,-4.869127,-1.342254,9.375497,4.067239,-9.098858,-8.664990,9.976111,-0.228739,1.851361,-3.293052,9.693664,-2.072535,-2.178294,-1.212461,-2.797257,-9.643074,5.882008,2.989289,-1.884019,4.152524,5.017987,-3.874691,-6.848301,-0.126660,-1.599025,-4.792633,-2.291243,5.699340,-4.803585,9.613887,9.166632,-3.157734,-5.394831,0.141898,-5.669769,3.183067,-4.113617,-1.545471,-1.259432,-1.008314,-2.190067,-7.198355,-1.266359,5.439343,5.473658,4.673871,-4.685224,-9.533049,7.886286,8.931713,-8.931603,-0.387234,-0.684500,-4.253853,7.539053,8.607351,1.645241,-8.156937,-7.713015,3.438520,-9.112296,-5.457765,-7.600309,0.054768,4.229959,7.118601,7.452275,-4.639837,-5.754349,-9.812066,-8.138729,8.875290,-1.291808,1.103536,1.774920,-7.487994,1.162287,-2.754469,1.390525,4.654722,-3.145477,4.782776,-7.899723,-7.312641,-3.483514,4.425465,-3.034642,-3.473998,-8.834103,4.436901,-7.616244,-2.828104,8.504091,5.425385,-5.382698,0.289922,1.336866,4.104740,-7.915399,7.595589,-6.417401,8.494108,9.615615,7.513297,2.560408,-7.993409,2.640328,5.260207,6.448935,8.645128,-2.935384,8.205275,7.972092,9.840840,-5.503799,-1.174419,0.189983,0.171053,-4.860180,2.996545,-7.390368,1.986063,-4.669131,-8.605083,-3.419923,1.166480,-8.654254,-0.978209,2.405789,1.080385,-3.027247,9.379585,-1.550637,5.731671,0.052598,-0.437508,-6.083156,0.715631,0.127857,-6.829761,-1.907085,-8.871005,-6.259538,-4.169189,-7.307613,2.512931,-8.049551,6.591160,-6.663186,2.779184,5.080126,2.683395,6.148498,-2.562240,-8.251101,-2.781778,-4.222075,4.516506,-8.348383,7.632114,4.279052,8.380188,3.260236,-0.008499,3.129580,2.345981,-0.900036,-1.282845,-3.366520,-5.661803,-8.012450,6.042631,9.727650,8.662429,-3.807924,-9.258808,-9.823172,1.082580,-7.818178,3.856275,6.265181,-7.110840,9.825661,-3.390644,0.378721,-0.884657,8.666230,3.952198,-2.428992,-5.659972,0.079761,-1.518948,3.553438,3.322691,-4.300086,2.260332,0.046546,3.930034,5.222120,-0.370988,-3.543513,-4.561468,-4.131065,-1.820242,-1.114569,-8.789411,8.867819,3.909934,-0.473224,6.756522,3.058404,5.456589,-5.354646,8.618487,-3.731195,9.787661,-5.057988,-8.885599,4.058221,8.017441,-5.754158,2.237694,2.975513,-1.264019,8.607239,-1.181229,-0.787108,1.848688,-4.045001,-1.771973,0.109563,2.429499,3.903269,-9.984450,-9.245836,6.419319,3.982990,-7.029124,1.577196,4.202742,-1.696892,-2.788376,2.892988,-7.682776,-8.615114,-8.744584,-1.386769,-9.192331,2.822640,-9.041482,-4.034967,-3.603122,-7.561039,-9.267653,9.896969,-4.460735,4.777217,0.081915,-8.763777,-6.853354,-0.813912,-6.260949,-0.990912,6.588415,-2.558529,4.305748,6.964476,-7.834240,5.282653,4.322433,-0.174720,-0.643963,-9.264991,-7.084656,1.531925,-0.895735,8.247445,-2.228729,3.196460,-7.818415,6.385646,-9.072766,8.860413,-5.867200,-8.512975,-4.497421,8.241127,-2.445342,-2.107735,9.071512,-7.595257,1.383060,-4.266077,3.890493,6.584880,3.161255,-5.679407,9.676952,8.087707,-8.937343,-4.892994,-6.546505,9.525922,6.945981,-3.479511,-4.483125,-5.973572,-4.841392,5.427489,-8.654936,6.361161,-7.511434,-0.863666,-8.822760,4.753604,7.870194,2.889363,-7.972347,-9.478280,-2.954690,-2.960203,3.353643,-4.807189,1.217428,-4.644601]], dtype = "float64")#candidate|5711|(2, 1680)|const|float64
call_5710 = func_3835_call(relay.reshape(const_5711.astype('float64'), [15, 16, 14]))
call_5712 = func_3835_call(relay.reshape(const_5711.astype('float64'), [15, 16, 14]))
func_2897_call = mod.get_global_var('func_2897')
func_2900_call = mutated_mod.get_global_var('func_2900')
var_5717 = relay.var("var_5717", dtype = "float64", shape = (150,))#candidate|5717|(150,)|var|float64
var_5718 = relay.var("var_5718", dtype = "float64", shape = (1500,))#candidate|5718|(1500,)|var|float64
call_5716 = relay.TupleGetItem(func_2897_call(relay.reshape(var_5717.astype('float64'), [10, 15, 1]), relay.reshape(var_5718.astype('float64'), [10, 15, 10]), ), 1)
call_5719 = relay.TupleGetItem(func_2900_call(relay.reshape(var_5717.astype('float64'), [10, 15, 1]), relay.reshape(var_5718.astype('float64'), [10, 15, 10]), ), 1)
func_2606_call = mod.get_global_var('func_2606')
func_2610_call = mutated_mod.get_global_var('func_2610')
var_5722 = relay.var("var_5722", dtype = "int64", shape = (312,))#candidate|5722|(312,)|var|int64
call_5721 = func_2606_call(relay.reshape(var_5722.astype('int64'), [3, 13, 8]), relay.reshape(var_5722.astype('int64'), [3, 13, 8]), )
call_5723 = func_2606_call(relay.reshape(var_5722.astype('int64'), [3, 13, 8]), relay.reshape(var_5722.astype('int64'), [3, 13, 8]), )
uop_5731 = relay.log(call_5721.astype('float32')) # shape=(3, 13, 8)
uop_5733 = relay.log(call_5723.astype('float32')) # shape=(3, 13, 8)
output = relay.Tuple([uop_5705,call_5710,const_5711,call_5716,var_5717,var_5718,var_5722,uop_5731,])
output2 = relay.Tuple([uop_5707,call_5712,const_5711,call_5719,var_5717,var_5718,var_5722,uop_5733,])
func_5745 = relay.Function([var_5697,var_5717,var_5718,var_5722,], output)
mod['func_5745'] = func_5745
mod = relay.transform.InferType()(mod)
var_5746 = relay.var("var_5746", dtype = "float64", shape = (15, 2, 13))#candidate|5746|(15, 2, 13)|var|float64
var_5747 = relay.var("var_5747", dtype = "float64", shape = (150,))#candidate|5747|(150,)|var|float64
var_5748 = relay.var("var_5748", dtype = "float64", shape = (1500,))#candidate|5748|(1500,)|var|float64
var_5749 = relay.var("var_5749", dtype = "int64", shape = (312,))#candidate|5749|(312,)|var|int64
output = func_5745(var_5746,var_5747,var_5748,var_5749,)
func_5750 = relay.Function([var_5746,var_5747,var_5748,var_5749,], output)
mutated_mod['func_5750'] = func_5750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_5757 = relay.TupleGetItem(func_5615_call(), 0)
call_5758 = relay.TupleGetItem(func_5617_call(), 0)
func_4518_call = mod.get_global_var('func_4518')
func_4521_call = mutated_mod.get_global_var('func_4521')
var_5771 = relay.var("var_5771", dtype = "float32", shape = (65,))#candidate|5771|(65,)|var|float32
call_5770 = relay.TupleGetItem(func_4518_call(relay.reshape(var_5771.astype('float32'), [13, 1, 5])), 0)
call_5772 = relay.TupleGetItem(func_4521_call(relay.reshape(var_5771.astype('float32'), [13, 1, 5])), 0)
output = relay.Tuple([call_5757,call_5770,var_5771,])
output2 = relay.Tuple([call_5758,call_5772,var_5771,])
func_5784 = relay.Function([var_5771,], output)
mod['func_5784'] = func_5784
mod = relay.transform.InferType()(mod)
mutated_mod['func_5784'] = func_5784
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5785 = relay.var("var_5785", dtype = "float32", shape = (65,))#candidate|5785|(65,)|var|float32
func_5784_call = mutated_mod.get_global_var('func_5784')
call_5786 = func_5784_call(var_5785)
output = call_5786
func_5787 = relay.Function([var_5785], output)
mutated_mod['func_5787'] = func_5787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_5870 = relay.TupleGetItem(func_5615_call(), 0)
call_5871 = relay.TupleGetItem(func_5617_call(), 0)
func_2897_call = mod.get_global_var('func_2897')
func_2900_call = mutated_mod.get_global_var('func_2900')
var_5882 = relay.var("var_5882", dtype = "float64", shape = (150,))#candidate|5882|(150,)|var|float64
const_5883 = relay.const([7.589553,4.886103,8.019000,2.775983,8.841418,-8.755137,9.951332,0.411201,-4.046955,-5.998612,2.358175,-5.455620,-6.306836,-2.092134,9.604106,8.954789,-0.891245,3.894528,-0.592815,-6.344791,-1.229434,-9.223555,6.905870,6.285041,-5.469453,9.016434,-8.071124,7.070541,4.048248,-4.768979,5.426641,9.784776,-8.972972,9.896496,-1.391823,-1.962723,7.605653,-0.483122,7.782958,-7.019997,6.744734,5.735310,-1.995458,-3.405492,3.393248,-9.144050,4.341680,-2.433209,-0.802176,-9.476564,7.817020,1.142186,6.682264,-5.991634,1.519889,-8.864254,-3.058264,-6.887468,2.207037,-9.079717,8.281485,9.755323,-4.433680,9.978553,-5.641150,8.763418,-1.180469,-1.318015,4.370581,-1.412902,5.860641,4.819244,9.618890,-4.663629,9.939318,6.715761,3.629896,2.104088,-9.859343,-6.303077,-0.051205,-3.262265,9.197965,2.207502,3.295276,7.345492,-0.919664,-9.004153,3.315459,-4.446479,8.199461,1.943411,4.201005,0.266285,2.454170,-8.059767,1.635016,7.385675,1.109699,1.653719,-5.827330,5.833899,-8.142529,-7.682587,8.209505,-3.937624,-2.344419,0.138304,-4.664334,7.409396,1.805928,3.527347,0.031598,6.932919,3.153191,0.333628,3.299487,5.912496,9.212551,9.634699,-8.240795,9.660437,-7.208333,-2.184137,7.615797,-0.275304,4.151482,-0.087493,-1.792509,0.216531,-9.263282,-3.368799,-2.227461,8.422839,7.627333,-8.013152,-7.971303,2.699680,-8.100103,6.405355,0.153916,-3.360278,-5.131455,6.405635,-5.237280,-6.899802,-4.671476,2.239395,-4.108538,-1.491913,4.481128,-9.825037,-0.028153,-6.709533,6.998861,7.276991,-0.344644,-4.695093,-9.935631,6.542831,-3.136146,4.630052,-5.932278,7.271723,-5.467521,5.315103,-1.027556,7.703823,9.635006,-6.911792,-4.309135,2.417359,2.810411,9.445111,-8.842655,7.639087,-0.411060,7.164728,8.126255,-5.122133,-8.853523,8.396175,3.249118,6.196100,8.864607,6.095752,7.890398,-0.437483,-1.103605,-8.061558,-4.859583,-3.042695,9.629016,-1.387893,-1.840700,-0.558410,-5.087467,-1.949449,-3.305961,-1.799370,3.065935,4.403006,-0.453200,4.125529,6.662518,1.470899,7.347825,3.341764,4.009668,2.157067,-2.832933,-4.199040,-6.958408,-9.415051,9.967579,-7.690450,-7.383851,4.432999,0.341778,-8.670885,0.428893,-0.496796,0.756840,4.046447,2.683662,-4.796351,-7.289183,-6.189190,4.985330,0.718618,6.637826,2.146740,-5.781268,0.219872,-0.232884,-5.435232,3.394121,-7.610128,-7.864239,-3.330232,1.209457,0.046315,8.857514,-4.493741,-7.502160,8.946801,5.908880,-3.772598,-0.862152,9.362753,7.853144,-6.106369,-3.023480,7.853792,-3.456833,6.894460,-1.603566,9.975993,-0.741082,2.827799,9.933562,2.081394,6.075742,-7.024481,3.638353,-0.466636,-9.614425,2.330481,-3.947498,1.290155,-8.273614,-8.532172,-2.446086,7.819473,7.501665,4.071547,2.600850,8.716523,-6.221079,-7.957046,4.148404,-7.308691,2.893117,-8.457930,-3.073136,-9.774855,-3.298355,-8.348929,-7.830361,-8.635828,-7.998405,9.372689,-0.499787,-0.549606,-2.332222,-9.415504,-0.923317,9.783645,-4.861158,8.812402,-3.883547,-2.632467,-2.686933,1.048153,-0.505615,-1.857048,0.196562,-7.630131,-1.548636,0.563774,-0.723795,-2.990499,-7.125137,-3.060677,6.253932,-4.101628,-0.735708,9.766962,1.230598,0.767183,-1.014151,-5.347587,1.368591,5.799715,6.714770,0.013955,-6.703253,-2.041568,6.283108,0.278403,-5.242807,-8.588668,-7.998042,1.715597,-3.393797,5.515920,-3.829132,8.721584,6.437382,6.875464,3.785399,-5.524457,-1.645942,-8.360708,5.583573,9.612147,9.981666,-4.014589,9.465640,6.538963,0.363655,-0.547978,-2.065523,0.095533,-6.082871,5.909439,7.945705,8.776515,-3.725646,-9.455814,6.757789,-1.606096,6.401710,5.041486,-8.200579,4.252642,0.630833,-6.786776,5.528839,0.109711,-2.384698,4.032153,-4.092934,-8.054218,-8.135235,2.314941,-5.649080,6.120285,-1.656095,-1.284881,1.973375,-8.230126,9.795468,5.908864,6.611757,-5.015914,6.534115,5.716550,-7.275829,-7.420802,-7.557118,-2.045003,3.317966,1.736261,-5.228365,3.643667,5.013193,0.629005,-7.096517,1.170908,1.957470,0.675304,4.284977,5.699853,-8.224383,-0.651553,4.226372,1.965603,-3.130647,-2.410044,-8.199884,7.540048,-6.985808,-9.666728,6.152357,-3.487981,1.007441,8.922562,-8.995997,-5.622679,-3.405643,-4.264715,-1.136104,0.078955,-5.262616,4.818019,2.318880,-6.258557,9.497940,-0.209939,-7.530063,-5.859899,-6.097113,-6.276366,-6.931103,-6.704545,2.150324,-9.508058,-4.133108,7.043355,6.040827,-1.402515,7.700832,-9.098988,4.650906,0.848215,2.208868,-6.844574,9.292662,9.596570,1.623390,-6.484688,-5.314257,-1.337923,-0.771147,2.155464,1.295783,-2.846756,-4.740878,9.960120,3.000331,3.872162,-7.968492,5.985604,-3.592739,7.219885,-0.753831,-5.284839,-1.359620,6.239654,-8.504297,1.887742,-0.319127,-7.892883,-4.149973,4.552828,-4.444185,7.070425,-6.153586,-2.358006,1.160044,-1.917135,-6.222152,-1.807020,-7.023412,8.097827,-7.622344,-8.932292,5.722003,8.222010,-4.577252,0.202494,5.341038,-3.397244,2.189366,-6.020029,-4.105243,-5.055106,5.181850,-3.262068,3.630403,8.019278,-7.254148,-8.000421,-3.174080,0.970891,-1.832047,-8.059575,9.194566,8.492824,5.312109,6.054483,0.924155,-2.881582,-9.205602,-3.434549,6.298014,3.697766,1.484613,6.403657,0.647520,-6.770215,9.612364,3.752286,6.240642,-1.395404,-6.063198,4.850015,7.383501,4.278939,-4.673846,3.241186,9.277323,2.290018,9.423209,-5.645989,3.751938,-3.544619,0.808461,-8.793464,5.955359,-5.155287,-8.915834,3.933189,6.782779,-7.364865,-8.832586,0.579468,-1.196768,-1.225337,5.224215,3.954691,4.346993,-3.546173,8.065949,-5.049905,5.622245,2.259443,-3.755699,2.233561,9.117375,7.550144,-9.849990,9.568328,7.801697,-2.714861,-9.905746,4.783001,5.941289,2.656577,-5.446707,3.180677,-6.984858,-7.997595,8.202762,-6.952082,7.032170,-9.108000,0.691407,-2.055387,0.816384,1.787026,-9.759748,-3.286690,-8.299563,4.185702,4.518109,-5.964366,5.922929,-5.709823,5.284885,2.079667,-1.590006,-0.124482,8.424576,-4.953630,6.389713,-5.707530,-2.423091,7.538805,-2.849103,-1.964724,-5.323281,1.304551,0.960559,-7.517070,3.661406,2.008823,-3.363390,0.908549,-9.685246,-2.786503,4.786144,-2.617782,8.067989,5.437757,-5.415302,4.273038,-4.776446,-0.680760,-9.028738,-9.193062,-4.458652,8.650601,4.050500,-7.067334,-1.398366,9.660779,2.167984,-2.253243,-2.173390,2.241009,7.668101,0.775990,8.502174,1.775552,-6.633558,3.859017,2.405827,4.720954,8.488175,-5.506498,0.113147,-7.631986,8.953146,0.780378,-4.777387,-6.891848,-6.817107,6.823547,8.439932,8.564975,9.626102,-3.522931,-5.480326,3.572010,6.953187,6.813183,-6.495431,-4.273248,-3.189914,3.536657,-9.079579,-7.666953,1.413169,-6.441502,-5.559790,-1.466311,7.165294,-2.605264,2.043349,4.340641,-5.339404,0.787171,-3.438726,-7.050548,7.251439,2.510888,-5.615704,-8.871914,-5.073523,-4.304061,3.410410,-3.537259,-8.356998,-3.744820,-9.348132,-3.519770,-2.385703,9.722192,9.736193,-3.228115,5.075584,-0.800268,9.809379,1.973462,-4.118992,7.600875,1.244636,-5.098516,-6.541670,0.564681,-5.530575,5.110945,9.819718,-2.831812,2.104712,0.799758,-1.117073,-2.846213,5.778890,3.071270,9.600455,0.431282,-5.470945,-9.151531,-6.275106,-5.316961,-7.500633,2.068998,-1.846051,-7.493406,-9.213849,4.773457,-8.809863,7.972159,9.975948,2.315770,0.488669,2.911212,-2.343845,-0.897831,7.083342,5.843048,0.828951,3.867217,-0.028781,2.733582,-9.724406,-2.364787,-7.390993,-6.409641,-5.512013,-8.737650,-9.446222,-8.709953,-3.342738,3.842136,1.502961,7.160415,5.370898,-5.169108,-5.461433,4.245195,-9.918817,0.696951,5.746963,7.162583,0.852628,8.292004,1.200205,-9.838958,-0.389121,-1.832569,5.920664,-5.825435,-7.814941,-8.522015,-8.887347,4.002323,8.888905,6.606743,-2.393766,8.533952,4.867446,3.052123,-0.862474,-2.771025,8.587382,-9.984923,-0.158240,-0.967765,9.885041,9.005574,-4.867887,9.551870,-6.384700,-1.466244,9.188122,-2.639953,-8.177722,0.373339,-9.057691,2.440182,-1.828313,-8.565758,3.824557,-2.026167,1.230505,-0.598792,-9.507126,-3.359534,5.814434,-3.505169,-6.396119,6.882925,-1.541130,7.557761,-4.980059,7.673412,-2.167724,4.621131,-1.750892,-8.371499,6.289351,9.712154,-4.998941,-3.157818,-4.271264,-8.818458,-8.683601,6.781864,2.812380,9.220327,6.160469,-7.135379,-5.151189,0.939360,5.571972,-5.820179,0.471126,4.118358,9.059216,9.735540,-8.318513,-1.111268,4.051674,3.274619,-7.955633,-9.434860,7.630395,7.770009,-5.939624,-7.728717,7.538083,-4.063449,-6.452580,-0.011145,-0.324065,1.413863,-1.289144,2.156645,7.262462,-1.807146,7.940168,-8.601686,4.977497,-5.096555,-7.175917,-5.394283,7.996881,-0.127169,-9.771284,-6.215502,-5.418182,4.408565,0.292955,-1.984553,9.945432,0.767042,7.303407,-8.683961,9.628080,-9.159948,5.945152,0.529719,-3.671707,3.651567,3.157936,2.521682,3.466479,-1.200397,8.774730,-0.733070,8.573149,0.570161,6.461934,6.423718,-3.006829,-1.288363,-6.189678,-1.147933,-8.016736,9.639652,4.421435,3.243073,2.025286,-4.300555,4.590631,-6.401917,-5.341023,0.486171,1.903655,-3.476929,7.817626,0.549364,1.006003,-6.419367,3.394175,9.531001,-7.405892,-1.051036,-7.602599,-5.190263,4.874182,-5.452991,-1.507325,7.939619,-5.784110,9.982020,-8.446031,-7.702304,-1.747630,6.992842,-8.120535,7.710900,-5.051694,6.000176,-1.531214,-4.123466,-5.804794,3.709203,-3.763544,-9.173971,-3.280600,-9.411085,-5.038023,-1.271551,3.007153,5.888444,-2.678502,-7.672465,-4.805933,1.310257,1.633614,-6.944119,-5.371057,-2.785820,-9.657140,-7.551142,-5.940391,8.924944,9.259599,-9.466310,-2.538756,-3.227817,-1.125147,7.035421,-7.826918,6.549954,-8.088305,6.821883,9.794762,1.443834,-1.130103,-2.520586,7.335680,-8.296304,-8.690625,9.740191,-4.896653,4.435907,7.185143,2.592060,-7.642276,7.530105,-4.615103,8.155985,2.811054,0.386543,-7.169150,-5.014706,3.111834,-8.433978,1.576521,-1.152583,-4.101248,-0.636862,-0.755948,2.180304,-8.550668,0.611985,-5.419594,-3.731848,-8.388549,1.207829,-2.323207,-7.131288,-9.117102,9.710595,-2.846081,2.741542,9.693005,-5.934614,3.271454,-0.677916,9.048065,-0.561792,4.851133,9.444907,-3.570610,-2.208961,-3.001150,9.332696,-0.981093,6.874040,-9.824189,2.606656,-8.088297,-9.106675,5.807155,-1.774039,-2.777415,-2.301895,7.775191,0.469364,5.544990,-5.827090,-7.624447,-8.067143,-6.530836,-0.290766,6.205535,2.494062,5.653299,4.679776,-5.688144,7.398489,7.655204,-6.159737,9.945132,-1.109569,-9.175719,7.225816,-1.516793,6.197225,6.168130,-5.496010,9.730992,-4.362945,2.651964,0.186257,5.009184,-5.011601,7.199054,-6.120179,7.480399,4.098304,6.857246,-0.525667,-5.287160,6.790815,9.069404,-9.105103,9.161220,-0.478893,5.346711,-8.221512,-3.132233,2.007420,-6.808900,6.615604,-0.510678,4.042453,7.055687,-4.738086,0.251301,5.996065,5.064185,9.606162,-4.870507,0.946957,7.173889,9.892409,-0.117004,3.132680,-3.098078,-4.113635,1.749152,-0.724838,-4.145103,1.252013,-5.309328,-1.449641,-3.231961,-5.368461,5.427055,-3.433665,-7.509357,4.712726,-0.352609,6.011434,8.856134,-1.238063,9.413554,2.748269,6.223097,9.992069,2.027583,1.360515,7.985642,-6.331896,5.032635,6.113763,-1.281351,-2.049587,-7.766257,0.529140,-4.968309,-2.781738,6.761832,4.844073,-6.670340,-6.604092,-9.815259,-4.571094,-8.122115,8.796905,4.624903,4.731783,4.852498,2.109811,2.981292,3.287851,-0.441212,3.120619,3.317585,-8.550787,4.686441,5.930671,-8.721410,7.797364,-8.587992,-1.773184,5.141954,-0.968998,0.569226,-0.029995,-4.388154,-5.347083,-8.268107,-9.541367,-8.253936,1.163265,-2.427641,-3.988659,-3.177668,9.069729,-0.001555,3.994419,3.948927,-3.313818,2.367727,8.845645,-5.544937,-6.878778,6.094519,-8.500282,7.029266,6.183408,-5.799965,-4.608530,0.994844,3.477026,2.020241,4.296236,-3.648108,3.087234,0.215609,-6.588725,7.143999,-7.764340,5.339292,-6.841457,-0.064270,-9.604007,5.911866,-3.415222,-4.838726,-8.440699,-4.055377,-5.588547,2.319834,-1.740016,-8.081122,-0.555188,1.640213,-4.350085,7.605428,1.947172,-0.689485,-9.432494,-3.616465,-0.547179,0.258872,-0.537021,0.555107,-5.851645,-0.246183,2.224277,6.764129,-4.603257,-3.489273,-9.576307,-6.382013,7.521749,7.370579,-8.958614,-9.763811,7.308039,-0.532768,4.202040,-3.127913,-9.095646,-2.202870,-2.543222,-0.740655,-0.788621,5.324238,-2.709155,-5.742393,3.631381,-6.203854,4.293013,-1.597481,-3.113641,-1.149851,-4.026635,4.683568,-0.534966,-0.755028,-7.283644,3.014709,6.242817,9.163365,-1.799082,-7.842171,8.867192,-6.794731,1.158491,8.282904,5.265789,-4.407659,7.105907,-8.801534,1.377570,-5.593376,8.128803,2.897051,-1.501858,2.812744,-1.458457,-1.062779,-9.866123,8.266633,-3.464338,2.728745,-2.406953,5.177505,5.013606,2.539910,5.997348,-8.871963,-0.501487,9.600083,-1.593385,7.924093,-3.880905,8.189061,-7.416854,1.696157,9.113714,-3.406667,-2.369279,5.927691,-4.180705,-8.732699,-0.612788,-0.415988,-1.723140,-3.046485,-4.051488,-2.950947,9.444170,2.560354,-5.774800,-8.029722,8.473186,4.009829,4.625670,-5.424326,-0.621677,7.622340,7.105858,1.787822,3.529265,6.554543,2.390188,5.763097,0.708032,1.642044,2.621165,2.580642,-3.104831,-9.851275,-7.819033,0.267655,1.645248,1.239617,5.349429,5.423637,-9.265840,-3.514299,-4.935288,3.630973,5.325271,2.313195,-4.782557,9.463380,5.953388,-9.633838,-9.943974,-2.551719,-5.176467,0.098460,-0.472124,8.122717,7.739916,6.360063,1.925247,7.833754,0.684318,2.277622,0.717663,-5.784728,-4.657777,-0.910640,5.220264,-7.881593,1.265489,9.614537,-4.209351,-6.817942,-1.264868,3.019836,-4.632505,-0.842595,0.161121,-4.729296,3.968471,-7.388406,5.573159,-9.808087,5.694268,9.933071,-5.179303,7.554142,1.063840,-8.051085,8.643737,5.741705,-6.557222,9.764518,6.939402,1.781597,-9.193253,-1.568922,-9.791426,-1.949204,6.310592,-5.000010,-9.862981,4.586305,-1.695726,-5.787600,4.098563,0.113158,9.831712,-4.670400,-2.443881,2.679912,3.560684,2.363319,6.309128,4.402525,6.426775,-5.358837,2.529947,8.963116,-6.963323,8.816986,1.224151,8.489296,7.227464,1.725212,9.086544,8.921032,-8.213302,3.880564,-8.528548,-4.238026,-9.223181,-7.468882,-4.075600,8.232917,8.809389,6.718602,-4.013628,2.481012,-3.787288,0.653746,-7.471490,-9.794871,4.299435,-3.571605,-4.778111,5.835906,4.004896,6.868300,1.826863,-7.165594,2.523352,2.165231,2.509954,-4.443990,4.295479,3.575516,-8.314161,-2.203933,8.349672,9.512764,-9.399010,2.840845,-6.882046,2.368224,8.570173,-2.696232,0.963948,-3.714140,8.962959,-2.742535,4.080214,-2.351804,4.358828,5.755981,4.623241,3.599806,-5.845433,8.421215,0.016925,-3.487554,8.653919,0.615287,5.917763,6.471372,-3.886369,0.002727,4.512167,2.167887,4.439140,-9.779239,-3.069160,-7.086086,-8.801323,0.590819,-3.710602,-3.905103,7.043287,6.651388,-4.276629,6.355619,-5.914070,-6.501244,-1.835233,2.273382,-3.638923,-3.595660,1.079666,5.816940,-6.182537,3.052150,0.050415,-8.980884,8.770129,0.606983,-3.292536,5.950452,2.481236,0.710222,9.257075], dtype = "float64")#candidate|5883|(1500,)|const|float64
call_5881 = relay.TupleGetItem(func_2897_call(relay.reshape(var_5882.astype('float64'), [10, 15, 1]), relay.reshape(const_5883.astype('float64'), [10, 15, 10]), ), 1)
call_5884 = relay.TupleGetItem(func_2900_call(relay.reshape(var_5882.astype('float64'), [10, 15, 1]), relay.reshape(const_5883.astype('float64'), [10, 15, 10]), ), 1)
output = relay.Tuple([call_5870,call_5881,var_5882,const_5883,])
output2 = relay.Tuple([call_5871,call_5884,var_5882,const_5883,])
func_5885 = relay.Function([var_5882,], output)
mod['func_5885'] = func_5885
mod = relay.transform.InferType()(mod)
var_5886 = relay.var("var_5886", dtype = "float64", shape = (150,))#candidate|5886|(150,)|var|float64
output = func_5885(var_5886)
func_5887 = relay.Function([var_5886], output)
mutated_mod['func_5887'] = func_5887
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5900 = relay.var("var_5900", dtype = "float32", shape = (15, 4, 15))#candidate|5900|(15, 4, 15)|var|float32
var_5901 = relay.var("var_5901", dtype = "float32", shape = (15, 4, 15))#candidate|5901|(15, 4, 15)|var|float32
bop_5902 = relay.multiply(var_5900.astype('float32'), relay.reshape(var_5901.astype('float32'), relay.shape_of(var_5900))) # shape=(15, 4, 15)
func_5503_call = mod.get_global_var('func_5503')
func_5505_call = mutated_mod.get_global_var('func_5505')
const_5906 = relay.const([4,8,-9,-5,2,-3,9,-7,-10,7,-8,-7,1,-6,-3,8,2,-7,8,-10,-3,-7,3,-3,8,5,6,6,5,-2,4,-6,-6,7,-6,-6,-2,-1,6,9,1,1,6,-5,-1,9,-8,2,-1,-10,6,4,-9,-2,-7,7,5,-5,7,-3], dtype = "uint8")#candidate|5906|(60,)|const|uint8
call_5905 = relay.TupleGetItem(func_5503_call(relay.reshape(const_5906.astype('uint8'), [10, 6])), 0)
call_5907 = relay.TupleGetItem(func_5505_call(relay.reshape(const_5906.astype('uint8'), [10, 6])), 0)
func_3835_call = mod.get_global_var('func_3835')
func_3837_call = mutated_mod.get_global_var('func_3837')
var_5909 = relay.var("var_5909", dtype = "float64", shape = (3360,))#candidate|5909|(3360,)|var|float64
call_5908 = func_3835_call(relay.reshape(var_5909.astype('float64'), [15, 16, 14]))
call_5910 = func_3835_call(relay.reshape(var_5909.astype('float64'), [15, 16, 14]))
output = relay.Tuple([bop_5902,call_5905,const_5906,call_5908,var_5909,])
output2 = relay.Tuple([bop_5902,call_5907,const_5906,call_5910,var_5909,])
func_5919 = relay.Function([var_5900,var_5901,var_5909,], output)
mod['func_5919'] = func_5919
mod = relay.transform.InferType()(mod)
var_5920 = relay.var("var_5920", dtype = "float32", shape = (15, 4, 15))#candidate|5920|(15, 4, 15)|var|float32
var_5921 = relay.var("var_5921", dtype = "float32", shape = (15, 4, 15))#candidate|5921|(15, 4, 15)|var|float32
var_5922 = relay.var("var_5922", dtype = "float64", shape = (3360,))#candidate|5922|(3360,)|var|float64
output = func_5919(var_5920,var_5921,var_5922,)
func_5923 = relay.Function([var_5920,var_5921,var_5922,], output)
mutated_mod['func_5923'] = func_5923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_5958 = relay.TupleGetItem(func_5615_call(), 0)
call_5959 = relay.TupleGetItem(func_5617_call(), 0)
func_4041_call = mod.get_global_var('func_4041')
func_4045_call = mutated_mod.get_global_var('func_4045')
var_5969 = relay.var("var_5969", dtype = "uint32", shape = (126, 1))#candidate|5969|(126, 1)|var|uint32
const_5970 = relay.const([7,4,6,4,-8,10,-5,-3,-4,-9,-6,-4,-10,3,1,5,-3,8,6,-9,-2,-4,-7,-7,-4,4,3,-4,10,-4,-9,-1,-8,2,-10,8,-8,-8,-1,-8,1,5,-9,-6,8,1,9,-10,10,10,-2,1,-3,7,-4,-9,6,-9,-4,-5,5,2,8,10,3,-8,-8,-5,8,5,6,6,-9,-6,-2,-7,-8,10,2,-4,9,10,-10,6,-8,3,6,-7,-6,10,-5,-4,8,7,-3,-5,-4,10,3,-4,-9,-6,-8,-2,5,2,-10,2,-10,10,-1,-8,3,1,-3,6,3,7,-6,-6,10,2,4,-10,5,10,6,-3,3,2,8,-8,-3,-2,3,-9,-6,2,4,-4,1,-7,1,3,-3,-2,6,-1,4,-5,1,-9,-2,-7,-1,5,7,9,1,4,7,-2,5,-10,-9,3,9,-9,2,-9,-8,-7,6,5,-5,1,6,-5,-9,9,1,9,3,-5,3,10,-8,-6,-10,-2,-1,-9,8,-7,10,-6,7,5,1,-7,-1,6,1,-6,5,7,2,-3,9,-7,6,-2,-7,7,6,-4,10,-8,2,-3,3,10,-4,-6,-5,-4,4,-7,4,1,-5,-8,-3,-7,2,1,-10,1,-6,-8,7,3,7,-4,-4,-10,-2,-6,-5,-1,3,-2,-4,8,9,-2,-8,-10,7,-8,1,-9,-6,-9,8,-8,3,-5,-5,7,-10,10,6,-5,-4,-5,10,-9,9,-7,-9,7,7,6,-4,5,4,4,-5,-6,-1,-7,4,-5,-7,9,7,7,9,-7,-8,9,-10,-5,-9,8,-1,10,3,8,8,-6,-7,-1,8,-1,2,10,10,-9,-6,10,-3,3,-8,6,10,4,-6,-4,-5,-1,-5,-1,6,-6,8,-2,-10,7,-5,5,8,5,-4,-6,-5,8,-8,7,-10,8,10,-10,-6,8,1,-9,5,-3,-4,-8,6,9,6,9,8,5,-9,10,-2,-7,4,-4,-9,-7,-5,-1,4,4,5,-5,3,1,-5,-9,1,-1,-3,5,-9,-6,9,5,7,-3,-5,5,8,-3,-9,9,-10,7,3,-5,2,7,9,7,3,8,6,-9,-1,7,-5,-10,-5,8,6,-2,-5,4,-3,1,8,-6,-5,9,7,8,2,-7,-4,5,-8,-2,6,-8,6,-6,9,1,7,1,-7,6,-6,6,-7,2,6,8,-2,2,4,-4,-10,-10,-6,8,10,3,-6,8,10,7,-5,-9,-1,-7,-8,9,-6,4,-2,7,6,-9,-9,-4,-8,4,-7,-2,-5,-5,-2,3,-5,-9,-9,8,6,-6,4,-3,-2,-6,1,9,-9,-1,9,8,-10,1,-3,5,-4,-6,4,9,-6,6,4,-1,2,-3,-7,4,-6,-9,4,2,-6,8,-6,7,-3,7,-10,10,2,2,-4,7,3,-1,-9,-7,-1,-6,-2,-9,5,2,-8,-7,8,10,-8,-2,-4,-8,-7,-9,-9,-3,9,8,10,1,-6,8,8,6,6,6,2,-2,-10,7,-9,2,4,4,-2,2,1,-2,10,6,-9,-6,6,-9,-3,8,9,-10,2,7,-8,3,-8,10,-6,-4,7,-5,-9,1,-1,4,1,-2,-9,-8,-7,8,-8,5,-5,9,10,6,8,-1,-6,-10,-2,-1,-1,-8,2,8,-4,-5,4,10,-6,3,-6,3,-3,1,5,-6,1,-7,-2,4,-9,-7,-1,-5,5,-2,-6,5,8,-5,-7,1,9,-2,4,8,-3,6,-2,-2,1,-8,-9,-6,-10,-3,-4,-5,-4,-5,-3,4,6,1,-1,4,6,-8,-6,5,-7,-3,3,-5,6,-9,-1,-4,-1,6,7,5,-4,8,9,-8,-2,-1,-10,3,-4,-5,-3,5,-4,-7,1,-4,-7,8,6,4,8,2,-2,6,-5,-3,1,-4,9,8,5,6,2,8,10,7,-9,-10,4,-7,8,-9,1,8,7,9,-5,4,9,-9,-5,-10,5,-5,5,-8,-5,-4,2,-6,7,9,-2,-1,-4,-1,5,5,-1,-9,-4,9,-5,6,4,-6,-7,3,9,-10,2,-4,-5,7,9,2,6,-1,-4,-10,-8,9,1,-3,-4,5,-6,-3,10,-9,-9,-10,-10,-5,9,3,2,-3,2,5,-10,-1,1,-9,5,10,9,-8,3,5,1,-9,10,5,-9,9,3,8,-6,-7,-7,7,-8,-6,10,-3,9,-1,-6,-2,-9,4,1,-9,9,7,4,-3,-9,-1,10,10,-8,10,-9,8,-3,3,-4,-10,10,-8,-1,5,10,9,-2,1,9,-7,-6,-8,7,5,-6,6,-10,8,-7,-1,3,-9,8,6,-5,-8,7,-2,-9,-10,9,1,-10,3,4,-6,-4,3,-7,9,-1,3,-3,6,1,7,2,1,6,1,10,8,-2,-3,-9,1,9,2,10,-2,-6,2,6,9,-9,-4,8,2,5,1,10,-6,7,-9,-7,-9,-1,-8,4,10,10,4,-10,-9,2,8,3,8,-3,-8,-1,3,6,10,-1,-7,8,10,-6,2,-1,7,-8,6,4,-2,-9,-7,-6,-8,1,7,-5,-7,8,-10,-4,4,3,-3,-4,-2,-2,9,-9,-5,2,-8,-1,-9,-8,9,-5,-2,-3,-7,-2,9,9,-1,6,-9,-10,-5,-3,1,5,-1,-2,-1,10,3], dtype = "uint32")#candidate|5970|(1008,)|const|uint32
call_5968 = relay.TupleGetItem(func_4041_call(relay.reshape(var_5969.astype('uint32'), [1, 9, 14]), relay.reshape(const_5970.astype('uint32'), [8, 9, 14]), ), 0)
call_5971 = relay.TupleGetItem(func_4045_call(relay.reshape(var_5969.astype('uint32'), [1, 9, 14]), relay.reshape(const_5970.astype('uint32'), [8, 9, 14]), ), 0)
func_5691_call = mod.get_global_var('func_5691')
func_5693_call = mutated_mod.get_global_var('func_5693')
call_5981 = relay.TupleGetItem(func_5691_call(relay.reshape(call_5958.astype('float64'), [15, 2, 13])), 0)
call_5982 = relay.TupleGetItem(func_5693_call(relay.reshape(call_5958.astype('float64'), [15, 2, 13])), 0)
func_732_call = mod.get_global_var('func_732')
func_735_call = mutated_mod.get_global_var('func_735')
const_6001 = relay.const([[-3.531951,5.945422,-9.943859,5.422726,1.068095,7.640938,7.896100,5.837397,-6.369287,-7.655928,9.829475,9.154558,-2.143674,1.272668,9.436449,5.845470,3.059390,-7.716316,-1.317375,3.976436,2.779377,7.361805,-7.019867,-5.682444,7.625043,-2.662058,7.078390,-1.213804,-2.126219,2.044104,2.325425,8.384931,5.300284,-4.468926,7.003589,1.174153,-0.861849,2.943560,8.478775,-0.913053,-6.550097,-3.758434,-4.698628,-6.965163,-7.486315,-3.488295,-1.419849,-1.658863,0.010858,-5.695254,1.957508,1.722615,-6.054789,-9.649872,-3.317796,-0.213281],[7.522407,2.137941,7.731552,0.445548,2.807848,4.971551,1.816443,5.068720,-7.550602,-0.947330,5.704425,-0.457701,-9.788150,-7.158824,4.287387,-8.553916,9.622900,-1.389539,2.155275,-1.894296,-9.727086,-4.615828,3.024261,-1.689737,9.146703,6.100740,8.131962,-9.521324,8.489037,-6.104729,-5.956043,7.283402,-4.944004,-8.109025,4.751680,-4.284418,7.903556,-0.227541,-0.907875,-7.798999,7.472062,7.553912,3.574063,-1.344332,-4.292286,8.115455,3.470681,-8.453219,1.821040,6.439691,8.788460,-2.135334,9.546814,9.768475,8.235901,2.664383],[-7.166811,8.553214,4.218679,-6.492177,1.558231,-5.918855,-1.307482,-7.866128,7.614833,8.871298,-6.344725,2.813124,-0.034006,0.261905,9.562258,-3.323597,7.045071,9.973242,4.375061,-7.845695,-1.076918,-7.261753,3.356281,-5.005047,-6.562365,2.910011,5.195981,-7.298785,-5.460738,9.215258,0.338475,4.439461,-0.527694,8.184823,-3.870559,-3.054952,-8.638605,9.911789,3.647531,-6.038131,9.878863,-5.942721,5.455686,-1.235994,0.039368,2.914260,6.532711,3.329293,5.980154,-1.567725,7.814318,-6.739997,7.246299,2.448794,5.019724,-0.949456]], dtype = "float32")#candidate|6001|(3, 56)|const|float32
call_6000 = relay.TupleGetItem(func_732_call(relay.reshape(const_6001.astype('float32'), [168,])), 0)
call_6002 = relay.TupleGetItem(func_735_call(relay.reshape(const_6001.astype('float32'), [168,])), 0)
output = relay.Tuple([call_5958,call_5968,var_5969,const_5970,call_5981,call_6000,const_6001,])
output2 = relay.Tuple([call_5959,call_5971,var_5969,const_5970,call_5982,call_6002,const_6001,])
func_6008 = relay.Function([var_5969,], output)
mod['func_6008'] = func_6008
mod = relay.transform.InferType()(mod)
var_6009 = relay.var("var_6009", dtype = "uint32", shape = (126, 1))#candidate|6009|(126, 1)|var|uint32
output = func_6008(var_6009)
func_6010 = relay.Function([var_6009], output)
mutated_mod['func_6010'] = func_6010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_6113 = relay.TupleGetItem(func_5615_call(), 0)
call_6114 = relay.TupleGetItem(func_5617_call(), 0)
output = call_6113
output2 = call_6114
func_6121 = relay.Function([], output)
mod['func_6121'] = func_6121
mod = relay.transform.InferType()(mod)
mutated_mod['func_6121'] = func_6121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6121_call = mutated_mod.get_global_var('func_6121')
call_6122 = func_6121_call()
output = call_6122
func_6123 = relay.Function([], output)
mutated_mod['func_6123'] = func_6123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_6134 = relay.TupleGetItem(func_5615_call(), 0)
call_6135 = relay.TupleGetItem(func_5617_call(), 0)
func_4689_call = mod.get_global_var('func_4689')
func_4693_call = mutated_mod.get_global_var('func_4693')
var_6137 = relay.var("var_6137", dtype = "uint32", shape = ())#candidate|6137|()|var|uint32
var_6138 = relay.var("var_6138", dtype = "uint32", shape = (66,))#candidate|6138|(66,)|var|uint32
call_6136 = relay.TupleGetItem(func_4689_call(relay.reshape(var_6137.astype('uint32'), []), relay.reshape(var_6138.astype('uint32'), [3, 2, 11]), ), 0)
call_6139 = relay.TupleGetItem(func_4693_call(relay.reshape(var_6137.astype('uint32'), []), relay.reshape(var_6138.astype('uint32'), [3, 2, 11]), ), 0)
bop_6146 = relay.subtract(call_6134.astype('int64'), var_6137.astype('int64')) # shape=(15, 2, 13)
bop_6149 = relay.subtract(call_6135.astype('int64'), var_6137.astype('int64')) # shape=(15, 2, 13)
func_5745_call = mod.get_global_var('func_5745')
func_5750_call = mutated_mod.get_global_var('func_5750')
const_6155 = relay.const([3.653966,9.873502,2.669975,3.940471,0.641453,6.449024,-2.502829,-6.681794,-7.184714,-4.948354,-6.691954,1.496700,-8.219112,2.085071,-5.621440,-8.752381,-9.072521,8.892095,2.258465,-7.743779,-9.689941,9.433126,6.232527,-9.332149,-9.394076,1.556799,9.089817,-2.543425,0.041556,6.855430,-6.310056,-3.870992,7.545874,4.242952,-3.041914,-4.694089,8.806180,0.573698,9.705757,8.330861,-0.542951,7.997646,5.676921,8.579385,1.360210,6.634028,-6.289561,-3.791114,1.906753,2.974062,9.539474,-5.989620,4.022143,0.090150,-5.250037,4.516852,6.455822,-8.382733,-4.032886,-7.789369,7.078239,7.668499,6.312931,4.331135,8.817617,-1.952538,-9.435374,-3.757472,-5.657585,5.650812,-8.002165,-2.231710,8.541698,-4.241042,-8.803279,6.327006,-9.243330,-5.795482,-3.825694,-3.167569,-5.380036,-9.257802,-6.972182,-0.958528,-3.155889,9.551043,-4.302586,4.196943,-3.065025,3.382349,-8.614207,-6.433607,-9.220578,-2.753849,3.765728,-1.111434,4.299745,-4.336638,0.157180,-6.946759,-9.741437,-5.587458,4.502951,-6.930302,-4.106771,8.944172,-9.473105,0.157162,-7.382601,5.289879,3.466993,2.249345,-7.435128,-4.510355,-7.361366,-1.869330,-9.094570,-2.324751,-1.583104,1.980100,-0.475289,5.203196,0.735582,8.019818,-8.049211,8.115302,2.102315,-5.025294,-6.862361,3.236698,8.659704,-3.550995,1.194820,-8.541765,0.699648,-5.621257,-7.039823,3.131397,-7.299755,3.819567,2.647258,-9.999349,1.900805,7.796507,0.497585,-2.297511,-1.410083,-1.850680,1.426520,7.923675], dtype = "float64")#candidate|6155|(150,)|const|float64
const_6156 = relay.const([4.783092,1.718852,2.704390,-7.587661,1.229687,9.872777,7.179630,-4.412641,-5.639130,0.967437,3.111060,-3.191380,-3.756320,-8.209041,1.405128,2.741557,-9.940105,-3.780865,5.028745,-8.830510,-7.229207,2.084715,-0.511100,-9.872921,2.661999,4.036215,-5.696781,8.903645,0.214791,-4.902653,5.488715,1.557763,-0.390163,-5.202942,-0.868140,-8.608316,-3.953228,-5.186046,6.229349,8.518894,4.651538,-3.945484,-4.905256,-1.405431,4.278668,-1.475299,0.126940,-6.787856,-2.488636,1.444803,8.157631,6.883449,-1.993044,4.233322,-5.590814,-5.795399,3.530230,1.063910,-7.130875,-8.792956,-9.256687,5.413250,-5.168087,4.454142,-5.877226,-3.315799,-4.375405,2.324352,2.518180,4.169504,-6.056172,9.927247,-7.446443,9.327701,1.676772,-1.421144,2.433053,3.827620,1.334254,-2.047109,3.999428,6.847623,-4.850893,-8.853829,7.628519,3.041215,7.738269,-9.754118,-4.292513,0.289126,1.727151,8.604092,9.293486,-4.022662,-1.633301,-0.140494,4.251191,6.470262,-5.518693,-1.906733,8.706709,8.682043,-3.629769,-2.789188,-0.517234,-7.078904,7.573222,-9.723640,-7.075001,0.726252,7.234918,3.570399,-7.724375,-0.307624,-5.881228,-6.304448,-6.760671,2.982764,2.031433,9.360777,0.797105,2.773952,-6.200798,5.125723,9.490623,4.881021,-4.945802,8.727243,4.961258,5.339361,-0.261408,-2.721937,-7.554716,-3.714022,8.194476,6.461858,3.676136,-3.172225,-9.520849,7.967283,-1.654071,-1.375391,8.068943,2.689427,2.399181,-4.689163,8.378107,-3.821032,-1.437314,3.966311,4.348180,-4.148419,-1.574425,-5.714790,-8.289554,-2.030973,-6.607318,1.068098,-8.507095,-2.066889,-4.644007,-4.607153,5.744393,3.184246,4.043265,-9.678328,3.758313,9.754684,2.486438,-7.269951,9.511497,-2.488737,1.660920,5.187005,9.699484,7.960269,5.463116,5.074308,-4.839631,-1.670755,2.046696,-9.919091,-2.044673,-5.374853,9.630055,2.058746,0.563308,-9.956337,-9.137665,0.140047,-2.235889,6.475043,-5.253700,-9.274118,8.195663,-7.628833,9.640103,6.530281,-0.748528,6.003954,-9.797426,1.435280,5.661246,-9.434046,5.469780,9.447822,-9.532601,9.251775,4.786534,7.603647,4.804739,2.103902,2.970169,-4.629341,7.931886,8.574450,-7.438683,8.632871,8.505653,8.177818,2.124144,-3.485319,3.069205,-8.047575,3.067475,7.660377,7.956847,-0.935971,2.391360,6.127584,-0.694744,-1.662109,4.808493,-6.144767,9.152133,1.493428,-4.993000,-0.413253,-9.431540,-2.674335,7.438435,-6.531456,0.538782,9.822954,3.234069,1.562924,5.982963,-5.170361,4.029220,9.272099,5.079268,-2.408298,-4.367365,7.864244,2.902256,5.486399,-6.608759,-6.634899,-8.130813,-5.595954,-0.655819,7.048971,-1.021793,-3.895671,2.667942,-4.625777,-8.607980,-2.492646,-0.593627,2.005495,-7.115733,-0.763302,-1.522968,-1.140183,-6.418030,-9.092468,-2.422210,-0.628160,-5.929638,-4.430841,3.194480,-9.480567,7.633407,-2.916941,-6.557663,-8.280228,-6.970170,2.096048,9.011933,0.057078,6.003241,-4.282978,-4.468778,-4.065917,6.649417,-6.068121,3.025327,-8.980390,3.690493,-0.089883,9.260714,-7.935184,2.765545,-2.675589,4.912334,-0.445346,-9.530316,-9.189047,-0.388293,6.462612,-9.651635,-3.408713,-6.146696,-7.417273,0.510192,2.158775,1.478815,5.460738,-0.669655,3.625362,5.756315,-5.122430,-4.725515,-8.042964,5.761713,-6.031283,6.722744,9.506651,-7.947282,-2.681328,0.144035,-8.129348,6.924024,3.691342,4.068118,-7.358376,6.501924,-6.665492,8.635226,-4.619509,-6.113221,-2.121510,8.682871,4.516452,-5.910420,8.561849,-9.939317,-5.816615,6.980252,8.996518,5.143634,-7.459720,-8.147942,-2.818995,4.854840,-1.170145,-4.443855,-4.718354,-2.291243,5.021702,9.284754,-9.780938,-9.851140,6.834140,0.362759,-7.015677,-6.229516,8.961431,-4.627473,2.130777,-1.115081,9.787526,-0.422019,-2.783343,-9.690898,0.791117,-8.806385,0.589857,2.174844,5.737559,3.010905,5.596119,-8.046703,-0.436585,-9.127764,-0.995209,9.483069,4.676165,1.925065,-7.934758,9.622043,1.242684,-3.892659,-2.809900,-0.973223,-4.620257,-1.373774,5.686244,-6.311103,2.512539,6.651333,9.657021,3.900264,3.715315,-6.549747,-9.894780,9.135420,2.003841,-8.022113,8.240524,1.711165,-2.359199,0.624870,-3.366195,9.863619,1.283775,-6.688124,8.628056,6.718660,-7.322470,3.316776,-1.860286,3.682556,-2.050975,4.553787,-9.123535,4.252916,-3.251170,-6.624055,-7.438450,-9.885565,6.822930,-2.000926,4.730389,9.588766,6.186901,-9.066478,1.667215,3.683483,-9.223116,-4.427212,-1.922925,6.096051,-7.005093,4.470055,-9.799356,-4.346989,-5.720713,-7.540503,2.010452,-1.413864,-5.486009,-2.797685,-9.103071,8.731272,-3.246708,8.157737,1.931656,-5.107393,-6.516114,-1.049009,4.294277,-9.275529,7.616444,4.489347,-5.109584,2.743847,5.448407,9.927183,-9.923070,-3.824025,-7.550436,8.779927,-9.182895,5.545294,9.036749,1.346690,6.715029,6.181244,2.807213,1.693227,-3.513011,-1.076040,-4.674108,8.785812,4.428781,5.290128,3.542634,2.173910,-4.567606,-7.578674,1.572891,7.066905,-0.451477,4.249478,1.011193,5.552891,-7.200671,1.103987,4.316497,9.812175,-7.772004,-1.250926,2.145552,-8.888375,1.393562,0.112023,-8.792214,1.012288,5.803430,-2.993106,8.226590,-6.243236,-8.046860,-1.983449,-4.138622,-1.932611,-4.368953,-8.533827,-5.392972,-0.795292,-5.286027,-8.016937,-9.458650,5.925864,1.399392,-4.580968,7.580401,-5.146876,4.052530,-9.336273,-1.505016,-2.400715,0.262159,-5.650875,0.278932,1.174273,-0.400348,9.368760,5.381157,0.915498,-9.480194,7.315180,-9.757698,2.455345,-5.732649,-1.341377,-4.752899,-8.310252,9.302176,-5.053643,9.503652,-7.247667,5.969211,-9.029346,-1.228517,7.595740,5.112589,1.836487,-2.316466,6.074115,-9.000020,6.177747,6.101029,-9.052901,-2.995263,4.752196,0.400252,-2.483809,0.600506,8.374319,-8.778047,7.674825,-4.303846,0.020769,1.047757,9.868332,-9.888237,3.485845,-8.770411,9.750585,-8.589165,-5.302357,-9.769724,-5.231086,1.944879,-6.287579,7.510463,-2.955298,-7.629567,-4.386388,-9.343047,7.779727,3.843017,-0.194201,-7.494699,-0.142789,8.665753,-3.068965,8.183802,1.047858,2.388621,-0.992242,8.544392,-1.252853,5.383592,-4.236933,-7.851785,-0.008929,-7.400821,-4.718836,-5.051792,5.504630,7.442903,-4.834104,-7.067051,-0.720320,7.477680,-7.074489,1.939706,-8.063632,-4.422812,-3.049712,-7.311417,-6.792102,-9.408069,9.238209,8.852423,-0.884770,0.900078,-8.811224,-9.858934,6.391591,4.832825,9.301753,-7.663645,4.132853,-4.151724,7.392048,3.260149,9.131302,-6.896511,-4.434440,9.868515,2.192826,9.448470,-7.653557,-1.545581,6.643066,-8.208999,-7.147706,-2.802223,5.450013,0.621803,1.960077,-5.692740,-2.243310,-8.854575,-5.443716,6.727254,-7.421890,6.095199,2.626819,-2.010869,-1.650402,6.017421,2.204756,-7.237137,-9.115261,2.855039,-4.790616,-6.145647,6.022881,-7.072092,-4.990509,9.010977,-4.694485,9.165224,-9.215510,5.649066,-5.402566,0.421227,-3.878631,-4.057773,9.545001,9.295405,0.114025,2.632166,-3.696200,4.000054,7.187301,2.894431,3.534904,3.125390,-9.378205,-8.092324,0.534806,-8.808895,-0.689759,-2.153984,-5.295021,8.129161,5.729498,-7.213966,-4.529067,-5.326116,-4.851063,-3.879710,3.584544,6.147248,-4.903534,-6.691006,0.964476,1.483027,-1.419528,-0.056145,5.790482,-7.152127,-3.792298,-1.545049,-1.422249,-3.973713,-7.178015,2.581208,2.558773,9.912816,-9.896339,3.921771,-9.362603,6.690315,1.875483,-6.657792,-7.946618,5.349870,7.386916,0.709196,8.613381,4.975923,-7.690396,8.206321,2.873734,8.358641,-0.493437,-5.767159,-2.211755,3.219479,0.607274,-0.313178,5.328893,-8.047204,-8.107115,-8.418649,6.205365,5.381323,-5.760675,6.296296,-4.114471,-9.529862,-0.360115,6.959534,-9.791958,-2.439935,-2.421625,6.186851,-7.294625,3.501584,-6.844323,-2.118534,0.277993,4.527395,-5.949445,3.181424,-4.797181,-1.791073,-8.418445,1.347085,-4.205613,-8.893212,-4.293022,-4.060873,3.744485,0.704479,-2.925023,-7.660021,-5.480396,1.503619,-5.388917,3.453732,-6.723697,6.720174,5.090863,-2.640403,-5.757603,9.735424,-5.702937,-6.350925,1.985729,6.526475,9.444886,3.713856,-0.348626,9.966510,6.307757,2.987234,-5.647921,9.306195,9.385446,0.649665,-4.427459,-3.082618,0.516439,0.303342,9.887331,-7.464906,-3.626838,-4.272135,-0.600145,8.110170,-3.605609,-6.447093,-6.054679,-5.674873,0.552609,2.408154,-0.574462,-3.044626,-0.223464,-3.993515,3.244480,9.522570,-9.689816,-4.827796,3.833554,2.945007,-9.815404,-6.909574,7.845348,-7.238223,-9.032125,-7.369335,9.400058,-0.890824,-7.309505,6.469997,3.200239,5.819089,-5.049396,7.315715,-4.975736,3.797229,-3.050290,1.300789,6.158789,-2.283810,8.184255,-9.546163,1.963371,0.040119,-6.988068,1.641979,0.866133,9.958167,-0.366669,4.234161,5.107517,7.639923,-2.255324,3.761659,-5.442672,7.100708,3.958977,5.358861,2.093851,-4.254033,3.493622,4.751748,2.082704,6.822598,3.837255,-1.917919,9.671643,-4.658509,-3.854798,2.101396,9.561774,-5.218069,6.029668,-7.276352,-8.960188,-1.016535,-2.753480,-7.611415,-8.078744,-8.436750,-3.926008,5.208535,-9.739828,8.183921,4.879735,-8.827788,-1.811313,4.622353,-0.215988,-4.959322,5.171758,-5.702046,-7.883188,4.354726,-6.663590,0.594789,-1.648974,5.105703,-5.543570,0.708829,2.716794,3.338675,-1.061590,7.219942,-5.597076,-0.415654,-1.424494,9.435738,0.095896,-7.113179,-7.265352,9.925901,-5.787441,-7.193013,8.884619,-4.423913,3.079754,-1.661932,5.772995,-1.818049,0.666487,0.298338,1.470685,4.097869,5.549641,9.488922,9.991374,-0.076087,6.046354,-8.348073,-5.655739,4.783200,-2.972136,7.074464,-6.767014,9.288711,-7.094421,9.808296,-6.771185,9.130356,-9.603119,7.051187,2.006963,2.632131,-0.086414,4.055686,4.206563,-2.011583,1.177307,8.616576,3.270512,7.490362,1.141076,-5.351413,3.590284,5.922015,-6.230820,5.438653,-2.876585,-7.110755,9.733276,1.644098,-3.669985,-2.720114,5.087357,3.756954,1.346544,5.931050,-8.910488,-4.189546,3.127430,3.849392,-3.785853,5.355331,-7.271289,-0.789751,8.502030,-2.088466,8.124423,5.246538,-6.628453,-3.167307,-5.973415,-2.213896,8.112176,-7.587943,-1.774836,-0.645003,5.678937,1.291816,1.277513,2.667039,1.369647,-4.229482,-7.183617,2.622975,7.086853,-8.281767,3.352661,-9.879751,8.412969,4.823896,-5.233537,6.469226,1.198562,2.446744,-6.087374,-8.056316,-9.857569,-7.918482,-2.988257,7.012009,5.298576,8.836773,-1.368342,6.303255,4.307222,5.965516,-8.672198,9.941397,8.657931,-4.413588,4.026593,6.858984,-8.215523,-2.110242,-8.046782,-4.197860,-9.878865,-3.995168,1.281604,-5.860886,7.887879,-2.301685,-7.984882,1.591060,4.466856,1.868989,-3.348453,-4.237056,3.540335,-2.228904,3.135813,0.711409,-5.070670,-3.005256,-5.081645,-8.514735,4.228890,9.619023,-4.790454,2.827154,3.224126,-6.807723,-7.066720,-9.575995,-3.309334,1.973389,9.326702,5.385837,-2.249764,7.557236,-5.432820,-2.566907,-3.789287,-7.020532,5.025237,-9.577324,-1.592005,-2.311385,-3.602135,-2.679026,8.992061,-8.534024,6.949660,3.809258,0.040475,-7.577872,-2.503901,1.838177,-6.435914,-9.289988,-5.340253,-8.480897,6.164742,6.501375,2.668324,-0.122824,6.780019,4.472142,-9.944954,-7.740084,7.922419,-9.197440,-5.304103,4.726438,5.237463,-3.593554,-0.893705,-1.559290,6.705396,1.739386,-1.038717,-7.714926,-8.863607,-7.876905,-4.967668,5.611968,5.683149,2.546280,7.277560,-4.578680,-1.530278,-4.333686,-1.210105,4.811066,-3.606384,-7.644386,-1.536100,-3.604871,2.428573,-3.240593,-6.468196,0.825615,1.709050,6.887051,2.072605,1.504492,-8.655826,4.264349,-7.756178,-7.334896,7.077724,4.096301,8.631256,3.961765,-8.408182,-9.538703,5.850360,-9.099837,2.042266,0.845275,-1.314604,-5.801404,9.357770,5.121213,-3.725779,-3.899506,-0.928515,-8.129508,-9.687962,-7.198889,4.201202,5.512432,3.723792,4.857741,2.204052,6.871821,7.214537,-9.090626,7.503698,-7.585916,1.792265,-7.992472,2.051699,-8.469365,-5.136851,-8.987884,7.340208,-5.704990,-3.903668,6.226566,-3.650260,7.729956,5.248759,-1.958529,0.390107,-7.923096,-7.830905,-7.344060,3.235158,7.226217,-7.774332,1.478948,9.150756,-0.110775,3.751599,1.162539,-8.448569,7.471578,-0.409780,8.741880,2.987685,-5.430572,-2.365164,5.707957,9.791234,3.364752,-5.355740,-8.897812,-6.308293,4.581434,-1.587024,6.971366,6.141629,-7.515181,7.437606,0.317745,-1.481765,-4.512709,7.708983,-7.943721,-8.695382,-5.427968,8.376321,-0.607810,8.503437,2.478647,-0.669568,-8.484581,-1.271310,4.764347,-3.285183,-7.293949,-0.697121,0.932154,-8.205687,7.701427,6.441401,3.449992,-6.697235,-5.397514,-0.384536,8.740369,5.115557,-6.662294,8.422347,3.114290,6.071425,-8.709868,-8.875211,6.795632,4.124299,9.347353,-0.837962,1.969838,-1.311988,-7.369456,-2.447341,7.736013,7.501048,9.167987,5.559042,1.073034,-7.731775,-7.815322,0.554519,0.967568,-9.589997,-2.350937,6.144938,2.096080,4.838107,-9.738190,-8.063800,0.653929,-1.579845,-4.402056,1.533272,-1.637719,9.308985,-1.691590,-8.952048,0.077020,-4.350428,9.209456,-4.828336,6.636972,-9.293315,8.320551,2.099139,-5.521692,2.477048,9.824076,-6.132203,-9.677843,6.087933,3.084589,-5.863073,-0.518787,-6.446960,-5.978172,5.604110,-7.476667,-7.729021,-3.339930,8.123997,0.382238,6.629537,4.638202,-6.362782,3.189013,9.741800,6.994932,7.044246,-2.130011,9.225944,-4.549769,9.365588,-3.762130,-5.225784,5.980622,0.138928,-1.523628,-1.972839,2.110377,6.089809,-2.543275,2.140365,-1.185990,9.989597,-7.207464,-6.350995,6.636801,8.738401,5.975162,-0.076605,0.004721,7.821346,-9.876284,-2.207728,-2.640951,-9.629883,-4.149738,-6.291253,0.742829,8.779480,-3.601171,-7.367739,5.664646,0.751455,-6.034763,-7.562269,7.508760,4.027226,7.642697,0.455699,-8.611761,-3.468534,0.912699,6.531505,-6.191453,-7.631296,-8.551759,5.903603,1.848467,-2.224467,-1.706186,8.958066,-0.331582,-8.599577,-4.946059,9.393982,7.035926,7.461333,-1.489540,7.227343,-1.925362,8.184177,2.936079,-5.210807,4.849716,-9.099518,8.383692,-2.644631,-4.513156,3.296933,-4.926342,9.317072,-4.393396,3.226837,-5.946749,-9.223468,-2.215346,5.207295,-4.255896,-3.385517,7.128587,5.117597,0.218537,-8.528192,-7.896554,-3.495755,1.040855,7.333177,9.042580,-3.784985,6.841147,-0.334382,8.720955,4.294428,3.827997,1.556018,-7.763227,-6.655389,-3.302875,-3.674308,-0.342805,-6.758529,-5.100938,-8.782124,-3.487026,2.272251,1.612252,9.451628,-9.580255,-0.043893,8.624445,-8.253335,-9.137511,0.263488,1.546803,-6.368408,-9.771523,7.272215,-2.014606,-5.877508,7.301370,-6.235706,2.775546,9.873690,6.858190,-2.264662,7.482001,-6.653884,7.640887,6.514836,6.319917,-7.072098,-6.902031,7.280775,5.294957,8.584204,0.701648,7.586770,7.792058,-4.246065,-5.361292,9.032733,4.607877,-5.863860,4.660259,-8.796136,8.436642,1.346184,-5.025176,-4.689720,-2.736460,-4.731522,5.993162,9.473004,-5.788649,2.740071,-2.936003,6.686944,1.008237,-7.526010,7.934897,1.126549,7.070408,-2.815899,8.280226,-6.371449,-5.957768,-8.643548,-1.295135,-7.936972,5.568318,-5.607392,8.069103,-4.814733,8.928658,1.831045,9.126932,4.757772,2.101114], dtype = "float64")#candidate|6156|(1500,)|const|float64
var_6157 = relay.var("var_6157", dtype = "int64", shape = (156, 2))#candidate|6157|(156, 2)|var|int64
call_6154 = relay.TupleGetItem(func_5745_call(relay.reshape(call_6134.astype('float64'), [15, 2, 13]), relay.reshape(const_6155.astype('float64'), [150,]), relay.reshape(const_6156.astype('float64'), [1500,]), relay.reshape(var_6157.astype('int64'), [312,]), ), 5)
call_6158 = relay.TupleGetItem(func_5750_call(relay.reshape(call_6134.astype('float64'), [15, 2, 13]), relay.reshape(const_6155.astype('float64'), [150,]), relay.reshape(const_6156.astype('float64'), [1500,]), relay.reshape(var_6157.astype('int64'), [312,]), ), 5)
func_2897_call = mod.get_global_var('func_2897')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_6162 = relay.TupleGetItem(func_2897_call(relay.reshape(const_6155.astype('float64'), [10, 15, 1]), relay.reshape(call_6154.astype('float64'), [10, 15, 10]), ), 0)
call_6163 = relay.TupleGetItem(func_2900_call(relay.reshape(const_6155.astype('float64'), [10, 15, 1]), relay.reshape(call_6154.astype('float64'), [10, 15, 10]), ), 0)
output = relay.Tuple([call_6136,var_6138,bop_6146,call_6154,const_6155,const_6156,var_6157,call_6162,])
output2 = relay.Tuple([call_6139,var_6138,bop_6149,call_6158,const_6155,const_6156,var_6157,call_6163,])
func_6176 = relay.Function([var_6137,var_6138,var_6157,], output)
mod['func_6176'] = func_6176
mod = relay.transform.InferType()(mod)
mutated_mod['func_6176'] = func_6176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6176_call = mutated_mod.get_global_var('func_6176')
var_6178 = relay.var("var_6178", dtype = "uint32", shape = ())#candidate|6178|()|var|uint32
var_6179 = relay.var("var_6179", dtype = "uint32", shape = (66,))#candidate|6179|(66,)|var|uint32
var_6180 = relay.var("var_6180", dtype = "int64", shape = (156, 2))#candidate|6180|(156, 2)|var|int64
call_6177 = func_6176_call(var_6178,var_6179,var_6180,)
output = call_6177
func_6181 = relay.Function([var_6178,var_6179,var_6180,], output)
mutated_mod['func_6181'] = func_6181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6121_call = mod.get_global_var('func_6121')
func_6123_call = mutated_mod.get_global_var('func_6123')
call_6198 = func_6121_call()
call_6199 = func_6121_call()
output = call_6198
output2 = call_6199
func_6207 = relay.Function([], output)
mod['func_6207'] = func_6207
mod = relay.transform.InferType()(mod)
output = func_6207()
func_6208 = relay.Function([], output)
mutated_mod['func_6208'] = func_6208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6207_call = mod.get_global_var('func_6207')
func_6208_call = mutated_mod.get_global_var('func_6208')
call_6264 = func_6207_call()
call_6265 = func_6207_call()
uop_6276 = relay.rsqrt(call_6264.astype('float64')) # shape=(15, 2, 13)
uop_6278 = relay.rsqrt(call_6265.astype('float64')) # shape=(15, 2, 13)
func_4041_call = mod.get_global_var('func_4041')
func_4045_call = mutated_mod.get_global_var('func_4045')
var_6281 = relay.var("var_6281", dtype = "uint32", shape = (126,))#candidate|6281|(126,)|var|uint32
var_6282 = relay.var("var_6282", dtype = "uint32", shape = (1008,))#candidate|6282|(1008,)|var|uint32
call_6280 = relay.TupleGetItem(func_4041_call(relay.reshape(var_6281.astype('uint32'), [1, 9, 14]), relay.reshape(var_6282.astype('uint32'), [8, 9, 14]), ), 0)
call_6283 = relay.TupleGetItem(func_4045_call(relay.reshape(var_6281.astype('uint32'), [1, 9, 14]), relay.reshape(var_6282.astype('uint32'), [8, 9, 14]), ), 0)
output = relay.Tuple([uop_6276,call_6280,var_6281,var_6282,])
output2 = relay.Tuple([uop_6278,call_6283,var_6281,var_6282,])
func_6284 = relay.Function([var_6281,var_6282,], output)
mod['func_6284'] = func_6284
mod = relay.transform.InferType()(mod)
var_6285 = relay.var("var_6285", dtype = "uint32", shape = (126,))#candidate|6285|(126,)|var|uint32
var_6286 = relay.var("var_6286", dtype = "uint32", shape = (1008,))#candidate|6286|(1008,)|var|uint32
output = func_6284(var_6285,var_6286,)
func_6287 = relay.Function([var_6285,var_6286,], output)
mutated_mod['func_6287'] = func_6287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6207_call = mod.get_global_var('func_6207')
func_6208_call = mutated_mod.get_global_var('func_6208')
call_6291 = func_6207_call()
call_6292 = func_6207_call()
output = relay.Tuple([call_6291,])
output2 = relay.Tuple([call_6292,])
func_6295 = relay.Function([], output)
mod['func_6295'] = func_6295
mod = relay.transform.InferType()(mod)
output = func_6295()
func_6296 = relay.Function([], output)
mutated_mod['func_6296'] = func_6296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6121_call = mod.get_global_var('func_6121')
func_6123_call = mutated_mod.get_global_var('func_6123')
call_6404 = func_6121_call()
call_6405 = func_6121_call()
func_6284_call = mod.get_global_var('func_6284')
func_6287_call = mutated_mod.get_global_var('func_6287')
const_6407 = relay.const([-8,-2,1,5,-9,-5,1,4,-6,-10,-9,6,10,9,1,-6,6,-5,9,-5,7,5,-3,-6,4,-3,-4,8,10,-9,3,4,-7,-6,-1,7,10,-7,-3,-1,10,7,2,-10,-5,7,-8,7,2,-2,-4,-10,-10,-7,-2,9,-2,-8,2,-9,8,-6,7,-4,7,-1,-6,5,-9,-1,1,-3,-4,7,8,4,-2,-2,6,-7,3,-3,-10,-5,1,10,-5,4,3,-7,7,-6,-4,7,6,2,-3,-6,-5,4,6,9,6,-1,5,9,-3,-9,5,8,2,-1,-5,8,8,6,-5,-7,8,-1,10,-3,4,2,9,-1], dtype = "uint32")#candidate|6407|(126,)|const|uint32
var_6408 = relay.var("var_6408", dtype = "uint32", shape = (1008,))#candidate|6408|(1008,)|var|uint32
call_6406 = relay.TupleGetItem(func_6284_call(relay.reshape(const_6407.astype('uint32'), [126,]), relay.reshape(var_6408.astype('uint32'), [1008,]), ), 1)
call_6409 = relay.TupleGetItem(func_6287_call(relay.reshape(const_6407.astype('uint32'), [126,]), relay.reshape(var_6408.astype('uint32'), [1008,]), ), 1)
output = relay.Tuple([call_6404,call_6406,const_6407,var_6408,])
output2 = relay.Tuple([call_6405,call_6409,const_6407,var_6408,])
func_6413 = relay.Function([var_6408,], output)
mod['func_6413'] = func_6413
mod = relay.transform.InferType()(mod)
var_6414 = relay.var("var_6414", dtype = "uint32", shape = (1008,))#candidate|6414|(1008,)|var|uint32
output = func_6413(var_6414)
func_6415 = relay.Function([var_6414], output)
mutated_mod['func_6415'] = func_6415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_6452 = relay.TupleGetItem(func_5615_call(), 0)
call_6453 = relay.TupleGetItem(func_5617_call(), 0)
const_6454 = relay.const([[[-4.585060,-0.760205,1.518876,-6.324100,2.545304,9.882285,-1.248377,-9.260007,-9.707589,-4.255612,-7.013505,4.802852,-6.557851],[8.188987,-1.576210,2.405448,-4.143728,3.051983,-6.581213,-7.302911,-6.523613,9.894698,8.868853,-6.934713,-6.159442,-7.429661]],[[3.544723,-6.547440,4.115385,-4.714578,-5.253164,-2.869981,0.950981,-0.868371,4.921027,5.028018,1.700581,-7.773470,-4.180666],[-8.453707,-3.131283,7.269869,-5.913787,5.500625,-9.237386,3.995873,7.291390,1.901486,-2.793304,-6.464330,-7.021308,6.430182]],[[-4.611863,-0.254564,-1.622862,5.263403,-5.803899,3.369830,6.994156,-0.714499,-1.166665,-9.077544,8.054122,-6.452150,-8.367549],[3.342709,-2.002912,-3.542759,2.135256,5.689040,4.090423,-9.220453,-7.866812,-4.825626,-2.106127,9.230026,1.674079,9.905344]],[[7.965504,-5.457951,-0.399828,-3.167778,-9.892814,-8.626507,9.485605,9.466668,-3.602325,-6.525493,5.041064,-0.562381,0.438304],[-3.605874,-5.490746,9.499975,4.279418,0.213524,-1.250068,-2.012498,-5.221886,-1.071146,5.614018,-0.842804,9.895107,-1.918855]],[[2.278766,-2.059276,-7.634204,8.476101,-0.224791,-1.344492,-7.545265,-6.380656,7.814258,2.540922,9.000802,0.438544,-1.774892],[-4.561932,5.856709,-6.040050,-1.587169,3.514042,-8.384644,4.354034,-8.782833,-2.748904,2.842790,7.780103,-8.312028,-6.993600]],[[-9.235167,-2.767252,8.019772,-2.813393,9.916656,4.279521,9.228581,-3.660378,-9.030151,7.178700,3.533760,1.079804,-6.809920],[0.723640,-0.525600,-5.783182,5.331211,0.371102,7.393428,4.434464,-7.976240,-2.256197,-8.157356,5.049404,-0.300751,6.882048]],[[3.806122,-2.831082,3.650208,-0.805049,6.892211,-0.299452,4.881045,7.514108,8.490471,4.988055,-6.523101,5.743554,-2.369697],[7.058311,8.830824,-1.110675,8.433516,-4.024011,-0.535612,-5.656381,0.492827,-2.317338,-4.834440,-8.071794,4.671849,-2.309709]],[[0.860346,-0.165745,-8.632805,0.923097,-1.403541,-9.070367,-8.395118,-1.121694,7.268977,2.523754,5.212522,0.533741,7.823319],[4.541001,1.451572,-0.042794,6.524769,-0.723689,-7.209624,-8.959445,4.113042,1.546920,7.484073,-9.449076,-5.113675,-5.856784]],[[-1.161603,-7.328472,1.520299,-2.894491,7.683651,0.009498,1.169908,-0.627535,4.534108,-0.243456,-0.695516,2.831648,9.840883],[-1.660860,9.904339,0.237016,0.161092,6.595293,8.017782,2.405827,3.462509,7.321594,9.878556,-8.100487,-3.204911,9.154356]],[[-7.341232,1.551095,1.805504,-2.335955,-7.214626,-8.011124,0.871497,-8.695158,2.272070,8.848663,-5.380194,4.622843,-5.715680],[4.320922,-5.371724,2.074823,6.729052,-7.694406,6.997908,9.810050,-4.338687,3.173701,7.495714,-4.356845,3.663479,8.577143]],[[-6.488208,1.145920,9.883778,-0.774024,-5.114679,-3.406372,-9.988097,-5.674159,4.913747,5.946685,5.067539,4.361275,-6.270950],[4.609323,2.155420,0.570465,0.214007,4.584826,3.796909,-4.248305,3.290925,1.210473,2.251309,0.268238,1.008367,-7.357152]],[[4.591745,-9.641313,2.131774,-5.048847,-6.894204,-2.041819,-1.592912,-9.938481,9.948594,9.758126,-4.753323,-2.091919,-5.302671],[-9.249790,-5.060366,-1.489481,9.512112,4.484546,-0.643907,4.358363,-4.746714,-1.198904,9.401452,-5.048693,0.818702,-1.644063]],[[6.276801,2.375128,-8.507318,6.873053,-5.825426,8.788823,-5.030290,-1.180634,-8.883173,-2.112507,-5.289407,1.838427,5.187991],[-9.084817,-6.984116,-6.584266,-3.339718,4.761337,-3.953740,2.939209,1.289885,-3.111156,-4.336021,-8.457882,-3.581645,1.651816]],[[-9.439968,1.209644,-4.211341,-2.712813,-6.847210,-6.736901,4.933959,5.143119,2.138531,-9.946170,2.911275,-0.776986,-7.703670],[-7.610051,4.364889,5.827952,9.839585,-4.054861,-9.716558,-4.374464,5.777531,5.284204,-1.418749,-4.960934,-2.356932,-0.754905]],[[1.064848,8.541363,-8.348292,1.090052,9.521264,4.728612,4.992047,-0.905452,-9.929921,-1.439143,-5.273089,-0.827719,-3.238649],[-4.582578,-2.929466,5.080371,8.441684,4.330218,-5.307094,-0.718630,7.504454,-7.132456,9.389678,-7.285518,8.289377,0.686563]]], dtype = "float64")#candidate|6454|(15, 2, 13)|const|float64
bop_6455 = relay.left_shift(call_6452.astype('uint64'), relay.reshape(const_6454.astype('uint64'), relay.shape_of(call_6452))) # shape=(15, 2, 13)
bop_6458 = relay.left_shift(call_6453.astype('uint64'), relay.reshape(const_6454.astype('uint64'), relay.shape_of(call_6453))) # shape=(15, 2, 13)
func_5503_call = mod.get_global_var('func_5503')
func_5505_call = mutated_mod.get_global_var('func_5505')
const_6475 = relay.const([5,-4,8,10,-8,6,-1,-6,3,-4,-4,-2,10,-4,-5,10,-7,-10,10,10,-6,-2,9,-7,1,1,-6,4,2,-9,-7,10,3,-8,1,-1,-8,6,-10,-10,-4,8,5,-10,-10,-5,-7,-10,6,-3,7,5,-4,5,-4,7,-7,2,7,-10], dtype = "uint8")#candidate|6475|(60,)|const|uint8
call_6474 = relay.TupleGetItem(func_5503_call(relay.reshape(const_6475.astype('uint8'), [10, 6])), 0)
call_6476 = relay.TupleGetItem(func_5505_call(relay.reshape(const_6475.astype('uint8'), [10, 6])), 0)
uop_6481 = relay.atanh(call_6452.astype('float32')) # shape=(15, 2, 13)
uop_6483 = relay.atanh(call_6453.astype('float32')) # shape=(15, 2, 13)
output = relay.Tuple([bop_6455,call_6474,const_6475,uop_6481,])
output2 = relay.Tuple([bop_6458,call_6476,const_6475,uop_6483,])
func_6512 = relay.Function([], output)
mod['func_6512'] = func_6512
mod = relay.transform.InferType()(mod)
mutated_mod['func_6512'] = func_6512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6512_call = mutated_mod.get_global_var('func_6512')
call_6513 = func_6512_call()
output = call_6513
func_6514 = relay.Function([], output)
mutated_mod['func_6514'] = func_6514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6295_call = mod.get_global_var('func_6295')
func_6296_call = mutated_mod.get_global_var('func_6296')
call_6541 = relay.TupleGetItem(func_6295_call(), 0)
call_6542 = relay.TupleGetItem(func_6296_call(), 0)
func_5503_call = mod.get_global_var('func_5503')
func_5505_call = mutated_mod.get_global_var('func_5505')
var_6558 = relay.var("var_6558", dtype = "uint8", shape = (15, 4))#candidate|6558|(15, 4)|var|uint8
call_6557 = relay.TupleGetItem(func_5503_call(relay.reshape(var_6558.astype('uint8'), [10, 6])), 0)
call_6559 = relay.TupleGetItem(func_5505_call(relay.reshape(var_6558.astype('uint8'), [10, 6])), 0)
func_5503_call = mod.get_global_var('func_5503')
func_5505_call = mutated_mod.get_global_var('func_5505')
call_6561 = relay.TupleGetItem(func_5503_call(relay.reshape(call_6557.astype('uint8'), [10, 6])), 0)
call_6562 = relay.TupleGetItem(func_5505_call(relay.reshape(call_6557.astype('uint8'), [10, 6])), 0)
var_6569 = relay.var("var_6569", dtype = "float64", shape = (15, 2, 13))#candidate|6569|(15, 2, 13)|var|float64
bop_6570 = relay.mod(call_6541.astype('float64'), relay.reshape(var_6569.astype('float64'), relay.shape_of(call_6541))) # shape=(15, 2, 13)
bop_6573 = relay.mod(call_6542.astype('float64'), relay.reshape(var_6569.astype('float64'), relay.shape_of(call_6542))) # shape=(15, 2, 13)
output = relay.Tuple([call_6557,var_6558,call_6561,bop_6570,])
output2 = relay.Tuple([call_6559,var_6558,call_6562,bop_6573,])
func_6574 = relay.Function([var_6558,var_6569,], output)
mod['func_6574'] = func_6574
mod = relay.transform.InferType()(mod)
mutated_mod['func_6574'] = func_6574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6574_call = mutated_mod.get_global_var('func_6574')
var_6576 = relay.var("var_6576", dtype = "uint8", shape = (15, 4))#candidate|6576|(15, 4)|var|uint8
var_6577 = relay.var("var_6577", dtype = "float64", shape = (15, 2, 13))#candidate|6577|(15, 2, 13)|var|float64
call_6575 = func_6574_call(var_6576,var_6577,)
output = call_6575
func_6578 = relay.Function([var_6576,var_6577,], output)
mutated_mod['func_6578'] = func_6578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6512_call = mod.get_global_var('func_6512')
func_6514_call = mutated_mod.get_global_var('func_6514')
call_6600 = relay.TupleGetItem(func_6512_call(), 2)
call_6601 = relay.TupleGetItem(func_6514_call(), 2)
func_5745_call = mod.get_global_var('func_5745')
func_5750_call = mutated_mod.get_global_var('func_5750')
const_6605 = relay.const([-8.776346,-1.202970,7.908712,-2.475249,6.982523,-6.321917,5.155406,-4.486609,-5.848003,0.983651,4.344755,-1.130664,-6.430153,-2.709660,-8.170883,-9.138932,4.266406,-3.292891,-6.892065,5.655894,-7.393101,-4.702248,-1.275711,-5.771441,-7.790757,2.722728,5.536256,8.266208,7.049961,3.416142,1.952190,-1.102942,-1.844333,8.268135,5.745125,-0.519357,-5.745899,-4.180837,3.033195,5.134637,-7.088935,8.429772,-8.872026,7.888916,-5.384633,-0.732631,0.133277,-4.115005,5.772476,-3.322366,5.409335,-7.525621,5.937043,-0.021492,6.896677,-3.858720,-6.876122,8.001462,-9.379563,-0.398305,6.846398,-8.947742,-8.649419,-0.153688,3.388911,-2.536650,5.732521,-2.326143,5.445918,7.408017,8.252441,2.382634,-2.494646,-2.620665,8.680876,9.115537,7.621859,6.853504,2.533202,6.560499,-1.856410,8.902604,-8.946950,9.188658,-0.399489,-3.611667,-0.745543,7.251497,-4.761353,-7.444566,1.628121,-4.645832,5.148754,-7.316799,7.593396,3.257759,3.236410,3.070589,3.425926,-9.996377,-3.191721,9.363931,-9.150448,1.992551,-0.221118,-6.585334,2.546469,5.530567,1.608180,1.887289,2.256043,-8.922831,2.394714,2.209509,-9.188612,-3.917468,-9.621647,-3.611474,1.152733,-9.833243,7.613080,8.302399,0.170908,8.171750,-9.796289,-6.889943,-8.142704,-0.550950,-5.909782,-3.490439,7.471765,8.084932,-8.772007,-4.047074,5.290774,0.394402,-5.854487,-1.492944,2.483430,-2.926142,-6.574710,-0.167780,9.247709,4.172851,-0.535101,2.846047,-3.521377,2.114499,-3.530111,-7.630928,-8.269109,-8.156282,-1.408045,5.575331,-6.562239,7.362857,-3.232368,4.363467,0.661851,0.770002,-8.151099,7.352000,-3.888431,5.137792,9.119900,-1.186430,-6.456059,-9.734781,5.373417,-1.442789,3.958481,5.942810,9.484503,5.076990,1.890159,-1.060911,0.210609,-8.289079,9.617470,-7.794784,-6.247931,-1.638161,0.287716,5.918451,-4.577664,5.316366,-1.975934,3.687843,1.303788,-9.582133,-9.069936,4.832888,-9.857597,9.010735,4.757854,-0.459060,-7.958019,-2.594358,2.917758,8.176664,-7.748724,7.447063,4.893444,-5.749244,-2.565048,6.551573,-6.538499,-4.064252,-2.412053,-5.001703,-4.032095,2.073555,0.288115,-5.195637,-2.611842,2.811193,-9.171595,9.136652,2.410243,0.334880,-3.719253,-5.105341,6.112586,6.348372,-8.346378,7.251120,9.737741,-3.602966,7.546292,8.377236,-5.974614,-3.377789,-8.066785,-2.005416,8.172012,8.722212,-1.595274,-6.753536,-9.437583,2.588739,4.530856,5.472574,-4.615436,-7.004366,6.966584,9.410880,-2.957461,-8.587436,8.702120,-1.013405,-6.410108,-2.997033,-7.576847,-3.934896,-6.854911,8.344847,2.369904,-5.191759,-5.818150,1.041974,2.788339,2.853489,-0.328818,-9.812887,-3.287144,-6.321820,-6.254094,9.134205,-3.600849,2.003399,-0.297078,-7.268046,-0.698279,4.157982,2.393846,-1.237172,0.494411,-8.540737,4.296586,9.778413,-9.462676,8.961278,-7.889723,5.260777,-1.713074,4.190734,1.952045,-5.654139,3.001289,5.870371,-7.036331,2.061302,9.578556,2.587521,-5.195922,3.060527,2.101585,3.228190,9.846668,-6.113816,6.232719,-5.814515,3.793416,-1.681665,-8.441998,-6.519907,8.314469,-0.393570,1.704830,-5.301055,-2.978350,-3.843386,-2.767950,8.174118,-6.247945,2.825749,-4.511810,4.491489,1.542387,-7.970538,6.639687,-1.585016,-2.095733,4.828987,5.434328,7.630525,2.330206,6.000481,2.969391,-6.760716,-2.526764,0.658493,9.317650,-8.797276,9.664806,3.342878,0.544269,5.373985,-2.485092,-8.633414,-1.274749,-8.986539,5.356907,9.179816,-3.498701,4.261019,-9.216528,4.536826,6.273792,-7.246403,-8.415178,4.419065,0.996862,0.007502,1.932855,2.217484,4.979457,-1.640378,5.038841,1.868548,3.376277,-6.154588,-2.774503,1.484814,-8.232949,-2.251548,8.382982,-2.447765,-4.898829,3.885221,6.379113,-3.225251,-6.646591,-9.250447,-0.193271,1.781247,-9.674486,6.219935,-8.646788,-3.695047,-1.758660,1.607937,-4.115691,2.948329,-4.973997,-6.234293,2.727266,-0.716090,8.945921,-7.179218], dtype = "float64")#candidate|6605|(390,)|const|float64
const_6606 = relay.const([2.613119,-3.267830,-3.069314,-6.547666,5.240401,-2.559578,-1.122576,-4.177935,-7.744918,-2.501046,4.388826,3.610388,8.094591,3.100785,-9.808036,-3.753542,9.714498,7.298064,6.274834,1.234447,3.410702,-7.190660,6.134954,-4.430474,-4.189122,6.328878,-4.901365,-9.801281,-1.380064,-3.819025,9.225112,0.393155,1.887593,-9.225527,-8.358054,0.822008,6.247604,8.764295,-1.707793,0.566739,9.408657,9.857152,9.229829,6.532934,4.908512,-7.273677,9.460337,0.581160,-6.829150,9.474493,3.201589,5.121575,1.243107,4.613443,-1.771878,-5.507469,-1.705712,1.175800,6.404809,9.422281,-0.875627,2.866357,9.401143,-1.623124,-4.465108,5.504106,-7.543275,8.821555,3.841844,-1.947499,4.518686,5.960112,-9.908412,3.366739,-7.403547,-7.647467,9.724498,-4.641291,-7.937372,-2.673870,-1.150865,3.719431,-2.440302,-2.679373,7.287670,-1.062000,2.154701,-2.183224,-1.094686,-0.516466,3.917451,-3.936587,-5.690974,2.088352,0.820926,-6.673655,7.064621,1.826303,-7.281373,-4.644032,-7.655984,-1.507886,-4.583855,5.728154,-4.867281,1.676901,-1.763077,-9.602701,-2.082995,1.447252,-3.489244,-7.192170,5.318592,5.674742,5.301927,-0.806366,-8.303089,-1.455488,8.613556,-7.971921,7.650019,1.457637,0.665523,-7.297078,-8.229734,6.607678,4.144186,-4.857200,5.942424,-7.080945,7.033091,-0.833071,7.524390,7.144142,-7.660630,4.025349,8.788684,9.987498,-4.157327,9.134904,-8.518350,0.252774,-5.639688,-8.563941,-4.198137,-7.700754,7.767597,0.907655,6.341766,-0.790012], dtype = "float64")#candidate|6606|(150,)|const|float64
var_6607 = relay.var("var_6607", dtype = "float64", shape = (1500,))#candidate|6607|(1500,)|var|float64
var_6608 = relay.var("var_6608", dtype = "int64", shape = (312,))#candidate|6608|(312,)|var|int64
call_6604 = relay.TupleGetItem(func_5745_call(relay.reshape(const_6605.astype('float64'), [15, 2, 13]), relay.reshape(const_6606.astype('float64'), [150,]), relay.reshape(var_6607.astype('float64'), [1500,]), relay.reshape(var_6608.astype('int64'), [312,]), ), 3)
call_6609 = relay.TupleGetItem(func_5750_call(relay.reshape(const_6605.astype('float64'), [15, 2, 13]), relay.reshape(const_6606.astype('float64'), [150,]), relay.reshape(var_6607.astype('float64'), [1500,]), relay.reshape(var_6608.astype('int64'), [312,]), ), 3)
output = relay.Tuple([call_6600,call_6604,const_6605,const_6606,var_6607,var_6608,])
output2 = relay.Tuple([call_6601,call_6609,const_6605,const_6606,var_6607,var_6608,])
func_6622 = relay.Function([var_6607,var_6608,], output)
mod['func_6622'] = func_6622
mod = relay.transform.InferType()(mod)
var_6623 = relay.var("var_6623", dtype = "float64", shape = (1500,))#candidate|6623|(1500,)|var|float64
var_6624 = relay.var("var_6624", dtype = "int64", shape = (312,))#candidate|6624|(312,)|var|int64
output = func_6622(var_6623,var_6624,)
func_6625 = relay.Function([var_6623,var_6624,], output)
mutated_mod['func_6625'] = func_6625
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6676 = relay.var("var_6676", dtype = "float32", shape = (9, 14, 3))#candidate|6676|(9, 14, 3)|var|float32
uop_6677 = relay.log(var_6676.astype('float32')) # shape=(9, 14, 3)
output = relay.Tuple([uop_6677,])
output2 = relay.Tuple([uop_6677,])
func_6692 = relay.Function([var_6676,], output)
mod['func_6692'] = func_6692
mod = relay.transform.InferType()(mod)
mutated_mod['func_6692'] = func_6692
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6693 = relay.var("var_6693", dtype = "float32", shape = (9, 14, 3))#candidate|6693|(9, 14, 3)|var|float32
func_6692_call = mutated_mod.get_global_var('func_6692')
call_6694 = func_6692_call(var_6693)
output = call_6694
func_6695 = relay.Function([var_6693], output)
mutated_mod['func_6695'] = func_6695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6121_call = mod.get_global_var('func_6121')
func_6123_call = mutated_mod.get_global_var('func_6123')
call_6789 = func_6121_call()
call_6790 = func_6121_call()
func_5503_call = mod.get_global_var('func_5503')
func_5505_call = mutated_mod.get_global_var('func_5505')
const_6792 = relay.const([1,2,7,2,-10,9,1,-4,-9,7,7,6,-2,-6,-7,-1,-9,8,9,-9,4,-1,-7,7,6,-2,1,7,-8,2,4,-6,6,-8,3,-2,-3,-4,-7,-6,9,8,-8,5,7,-5,-3,-3,6,-4,9,8,10,-2,-4,-2,8,3,4,-4], dtype = "uint8")#candidate|6792|(60,)|const|uint8
call_6791 = relay.TupleGetItem(func_5503_call(relay.reshape(const_6792.astype('uint8'), [10, 6])), 0)
call_6793 = relay.TupleGetItem(func_5505_call(relay.reshape(const_6792.astype('uint8'), [10, 6])), 0)
func_6692_call = mod.get_global_var('func_6692')
func_6695_call = mutated_mod.get_global_var('func_6695')
const_6798 = relay.const([-3.511688,-8.236843,6.018796,6.027583,5.211980,3.390279,2.291383,6.332883,6.365193,0.116428,-8.653008,2.467245,-2.390599,-0.932292,-4.459922,-8.834422,4.346901,-5.301856,2.618074,-2.198298,-1.293534,7.984338,-9.803265,0.451219,8.516766,5.397826,-9.809718,-2.116846,0.126500,-7.189649,2.569143,8.420145,-6.594504,-6.705965,2.780762,-7.723495,-3.698018,0.782347,6.445520,-7.083662,-8.043936,-8.349112,-5.844538,3.378561,8.686889,5.550684,-8.019091,5.365887,9.120911,-9.946912,7.538859,-3.420269,1.234618,-6.858650,1.477354,8.738623,-4.414550,-9.660342,4.646142,7.041823,-6.186904,9.071405,0.871271,8.397144,-6.744248,1.389027,-5.246819,8.025198,-0.986400,-3.161944,-5.255390,7.231567,-9.981357,-0.723395,4.718612,-5.698989,-7.236489,1.588935,9.692160,-3.477947,-3.265853,7.758597,-4.342900,-6.626014,-0.886259,-5.756018,1.694655,7.723648,0.814305,9.120924,0.899918,-2.455109,5.046685,0.867169,-0.249198,3.202221,-9.245315,-8.539026,4.680292,6.913846,1.864761,7.786610,6.471712,-1.482695,-0.590004,3.196414,-2.216574,1.581443,6.182078,-0.516673,9.565183,4.652326,-1.158776,-0.045005,-2.323281,6.454096,2.492730,-3.813980,7.584186,2.434678,-5.148760,-1.481995,7.378162,2.704047,-2.999939,-0.277851,9.454594,6.315616,8.229065,9.845337,4.668675,-3.364554,9.674096,3.981805,7.239116,-3.558866,-5.073181,-1.003075,5.100791,-0.855999,3.049170,2.532430,-6.706890,-9.947757,-9.743132,-0.254767,-4.150194,-4.393785,5.496251,0.111022,-7.876915,6.718065,-0.909648,-6.031265,1.558520,8.969119,-9.509283,3.048434,-0.147238,-2.985019,6.154826,-5.199079,5.146363,-8.354831,2.247293,-6.805248,0.626252,-9.618750,6.569139,7.687394,7.720704,-4.245418,0.969267,7.127582,9.572648,-3.119920,-2.621695,6.601710,2.813493,-6.906430,9.968043,8.783728,-4.351221,-9.998733,-8.656297,-9.817063,-0.725139,3.508064,-9.720996,2.536053,0.158671,6.719749,2.007234,3.373826,-0.343400,7.369258,-9.786934,-5.260034,-4.702815,7.523002,7.077335,-4.713429,-3.187852,2.508522,-8.453533,-7.198978,6.670149,8.620609,-7.959152,7.254844,8.265595,-7.880856,9.504501,-4.730458,5.394985,0.411494,-0.015241,2.633173,9.440557,7.204627,0.884533,7.562393,6.636008,9.446227,-2.152823,-0.698522,2.285341,7.675398,-5.814130,-9.032519,5.017349,-6.886009,-9.714657,-7.986446,-0.773828,9.216845,-3.119217,-0.756643,-3.550610,9.104701,5.453389,-8.130896,0.666772,1.628346,1.188134,4.486531,1.080578,-5.376470,9.864301,-5.633229,8.627563,-8.821703,-3.938094,0.879636,-5.582424,5.250660,4.018022,4.247204,-2.218110,-7.284643,-7.331958,-5.050594,1.063050,7.962503,-0.506679,-9.181189,-2.560321,3.463566,-5.687881,7.129444,7.408431,-8.804019,-3.869220,9.507912,-4.627325,-5.221491,-4.911702,2.067669,-7.209819,-9.060180,-3.199612,-1.634262,8.831365,1.914399,-1.402693,4.322403,-0.230421,-9.830775,2.396316,8.564011,8.630971,-5.723430,-1.281572,9.877777,3.099089,6.575108,7.406197,-3.201244,5.523303,-0.326354,-4.111743,-6.835141,7.272237,7.226310,-2.347876,-9.350240,-2.274295,2.145865,-8.473086,4.708797,5.401856,3.696101,-7.726301,2.940398,-5.651592,-4.346390,7.532481,7.670157,1.125988,0.582564,1.853152,-3.972591,1.668183,-0.650853,-0.545607,7.225274,0.489456,-3.022625,-0.543574,9.137993,0.128059,2.725414,-8.192696,5.882686,3.615354,-6.610615,4.387320,-0.781649,-2.579675,-7.316734,6.553684,-1.838252,7.424113,-4.436792,5.391610,-0.827248,5.617271,0.515649,-1.681248,-5.150934,-5.344445,-9.384603,1.589423,-6.544612,5.281305,-0.539423,-2.825657,5.478374,-6.185811,3.319882,-7.659254,-9.816798,4.921118,2.087195,4.518904,8.390104,-2.897184,5.715341,-1.237422,-3.468413,-6.996744,-4.697758,9.792919,-1.575941,-6.147156,8.847164,6.613072,-6.838905], dtype = "float32")#candidate|6798|(378,)|const|float32
call_6797 = relay.TupleGetItem(func_6692_call(relay.reshape(const_6798.astype('float32'), [9, 14, 3])), 0)
call_6799 = relay.TupleGetItem(func_6695_call(relay.reshape(const_6798.astype('float32'), [9, 14, 3])), 0)
func_6121_call = mod.get_global_var('func_6121')
func_6123_call = mutated_mod.get_global_var('func_6123')
call_6803 = func_6121_call()
call_6804 = func_6121_call()
output = relay.Tuple([call_6789,call_6791,const_6792,call_6797,const_6798,call_6803,])
output2 = relay.Tuple([call_6790,call_6793,const_6792,call_6799,const_6798,call_6804,])
func_6809 = relay.Function([], output)
mod['func_6809'] = func_6809
mod = relay.transform.InferType()(mod)
output = func_6809()
func_6810 = relay.Function([], output)
mutated_mod['func_6810'] = func_6810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_6817 = relay.TupleGetItem(func_5615_call(), 0)
call_6818 = relay.TupleGetItem(func_5617_call(), 0)
output = call_6817
output2 = call_6818
func_6855 = relay.Function([], output)
mod['func_6855'] = func_6855
mod = relay.transform.InferType()(mod)
mutated_mod['func_6855'] = func_6855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6855_call = mutated_mod.get_global_var('func_6855')
call_6856 = func_6855_call()
output = call_6856
func_6857 = relay.Function([], output)
mutated_mod['func_6857'] = func_6857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6295_call = mod.get_global_var('func_6295')
func_6296_call = mutated_mod.get_global_var('func_6296')
call_6880 = relay.TupleGetItem(func_6295_call(), 0)
call_6881 = relay.TupleGetItem(func_6296_call(), 0)
func_6284_call = mod.get_global_var('func_6284')
func_6287_call = mutated_mod.get_global_var('func_6287')
var_6898 = relay.var("var_6898", dtype = "uint32", shape = (126,))#candidate|6898|(126,)|var|uint32
var_6899 = relay.var("var_6899", dtype = "uint32", shape = (1008,))#candidate|6899|(1008,)|var|uint32
call_6897 = relay.TupleGetItem(func_6284_call(relay.reshape(var_6898.astype('uint32'), [126,]), relay.reshape(var_6899.astype('uint32'), [1008,]), ), 2)
call_6900 = relay.TupleGetItem(func_6287_call(relay.reshape(var_6898.astype('uint32'), [126,]), relay.reshape(var_6899.astype('uint32'), [1008,]), ), 2)
output = relay.Tuple([call_6880,call_6897,var_6898,var_6899,])
output2 = relay.Tuple([call_6881,call_6900,var_6898,var_6899,])
func_6903 = relay.Function([var_6898,var_6899,], output)
mod['func_6903'] = func_6903
mod = relay.transform.InferType()(mod)
mutated_mod['func_6903'] = func_6903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6903_call = mutated_mod.get_global_var('func_6903')
var_6905 = relay.var("var_6905", dtype = "uint32", shape = (126,))#candidate|6905|(126,)|var|uint32
var_6906 = relay.var("var_6906", dtype = "uint32", shape = (1008,))#candidate|6906|(1008,)|var|uint32
call_6904 = func_6903_call(var_6905,var_6906,)
output = call_6904
func_6907 = relay.Function([var_6905,var_6906,], output)
mutated_mod['func_6907'] = func_6907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_6955 = relay.TupleGetItem(func_5615_call(), 0)
call_6956 = relay.TupleGetItem(func_5617_call(), 0)
output = call_6955
output2 = call_6956
func_6963 = relay.Function([], output)
mod['func_6963'] = func_6963
mod = relay.transform.InferType()(mod)
output = func_6963()
func_6964 = relay.Function([], output)
mutated_mod['func_6964'] = func_6964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6295_call = mod.get_global_var('func_6295')
func_6296_call = mutated_mod.get_global_var('func_6296')
call_6965 = relay.TupleGetItem(func_6295_call(), 0)
call_6966 = relay.TupleGetItem(func_6296_call(), 0)
output = relay.Tuple([call_6965,])
output2 = relay.Tuple([call_6966,])
func_6967 = relay.Function([], output)
mod['func_6967'] = func_6967
mod = relay.transform.InferType()(mod)
output = func_6967()
func_6968 = relay.Function([], output)
mutated_mod['func_6968'] = func_6968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6512_call = mod.get_global_var('func_6512')
func_6514_call = mutated_mod.get_global_var('func_6514')
call_6999 = relay.TupleGetItem(func_6512_call(), 1)
call_7000 = relay.TupleGetItem(func_6514_call(), 1)
output = call_6999
output2 = call_7000
func_7007 = relay.Function([], output)
mod['func_7007'] = func_7007
mod = relay.transform.InferType()(mod)
mutated_mod['func_7007'] = func_7007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7007_call = mutated_mod.get_global_var('func_7007')
call_7008 = func_7007_call()
output = call_7008
func_7009 = relay.Function([], output)
mutated_mod['func_7009'] = func_7009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6967_call = mod.get_global_var('func_6967')
func_6968_call = mutated_mod.get_global_var('func_6968')
call_7022 = relay.TupleGetItem(func_6967_call(), 0)
call_7023 = relay.TupleGetItem(func_6968_call(), 0)
output = relay.Tuple([call_7022,])
output2 = relay.Tuple([call_7023,])
func_7037 = relay.Function([], output)
mod['func_7037'] = func_7037
mod = relay.transform.InferType()(mod)
mutated_mod['func_7037'] = func_7037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mutated_mod.get_global_var('func_7037')
call_7038 = func_7037_call()
output = call_7038
func_7039 = relay.Function([], output)
mutated_mod['func_7039'] = func_7039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mod.get_global_var('func_7037')
func_7039_call = mutated_mod.get_global_var('func_7039')
call_7155 = relay.TupleGetItem(func_7037_call(), 0)
call_7156 = relay.TupleGetItem(func_7039_call(), 0)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
const_7161 = relay.const([[-3.043301],[3.582819],[6.324198],[9.891230],[-6.570031],[-1.513100],[8.805840],[9.667159],[-4.199622],[8.366496],[-0.150455],[-1.236094],[-6.602489],[-6.326099],[9.203743],[-5.826577],[-2.317099],[-5.488718]], dtype = "float32")#candidate|7161|(18, 1)|const|float32
call_7160 = relay.TupleGetItem(func_4118_call(relay.reshape(const_7161.astype('float32'), [2, 9, 1])), 1)
call_7162 = relay.TupleGetItem(func_4120_call(relay.reshape(const_7161.astype('float32'), [2, 9, 1])), 1)
uop_7173 = relay.sqrt(const_7161.astype('float32')) # shape=(18, 1)
const_7175 = relay.const([[4.689645,9.123103,5.270368,-2.547275],[6.214123,-9.884716,0.587256,7.958453],[-6.813283,6.224453,-0.051320,-2.876789],[2.859632,9.956717,-4.809500,-0.693477],[-7.624555,4.430300,-7.415310,-4.991962],[0.185377,-8.167404,-6.202934,8.731014],[-0.338401,2.074571,-5.208548,7.035075],[3.690654,7.621271,9.275086,2.950830],[-5.647833,6.939799,1.425380,-2.210627],[-9.593487,5.356735,1.126971,-0.608249],[9.078196,-1.918818,4.823775,-8.506215],[-6.992401,-3.922181,8.843310,1.074535],[1.076768,-0.064911,8.446111,8.103895],[9.553177,-1.962829,7.950348,0.647545],[1.434150,-9.231009,7.445902,1.864016],[0.923537,4.282740,7.114444,-0.584443],[0.120873,7.094601,6.335872,-2.547995],[9.214365,3.632784,0.234733,-7.581651]], dtype = "float32")#candidate|7175|(18, 4)|const|float32
bop_7176 = relay.bitwise_and(uop_7173.astype('uint32'), const_7175.astype('uint32')) # shape=(18, 4)
func_5691_call = mod.get_global_var('func_5691')
func_5693_call = mutated_mod.get_global_var('func_5693')
call_7187 = relay.TupleGetItem(func_5691_call(relay.reshape(call_7155.astype('float64'), [15, 2, 13])), 2)
call_7188 = relay.TupleGetItem(func_5693_call(relay.reshape(call_7155.astype('float64'), [15, 2, 13])), 2)
bop_7192 = relay.minimum(bop_7176.astype('float32'), uop_7173.astype('float32')) # shape=(18, 4)
func_6512_call = mod.get_global_var('func_6512')
func_6514_call = mutated_mod.get_global_var('func_6514')
call_7198 = relay.TupleGetItem(func_6512_call(), 2)
call_7199 = relay.TupleGetItem(func_6514_call(), 2)
uop_7200 = relay.acosh(uop_7173.astype('float64')) # shape=(18, 1)
var_7202 = relay.var("var_7202", dtype = "float32", shape = (18, 1))#candidate|7202|(18, 1)|var|float32
bop_7203 = relay.bitwise_xor(uop_7173.astype('int16'), relay.reshape(var_7202.astype('int16'), relay.shape_of(uop_7173))) # shape=(18, 1)
uop_7213 = relay.cosh(uop_7200.astype('float64')) # shape=(18, 1)
uop_7217 = relay.sigmoid(uop_7213.astype('float32')) # shape=(18, 1)
uop_7223 = relay.asin(uop_7213.astype('float32')) # shape=(18, 1)
output = relay.Tuple([call_7155,call_7160,call_7187,bop_7192,call_7198,bop_7203,uop_7217,uop_7223,])
output2 = relay.Tuple([call_7156,call_7162,call_7188,bop_7192,call_7199,bop_7203,uop_7217,uop_7223,])
func_7225 = relay.Function([var_7202,], output)
mod['func_7225'] = func_7225
mod = relay.transform.InferType()(mod)
mutated_mod['func_7225'] = func_7225
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7226 = relay.var("var_7226", dtype = "float32", shape = (18, 1))#candidate|7226|(18, 1)|var|float32
func_7225_call = mutated_mod.get_global_var('func_7225')
call_7227 = func_7225_call(var_7226)
output = call_7227
func_7228 = relay.Function([var_7226], output)
mutated_mod['func_7228'] = func_7228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6967_call = mod.get_global_var('func_6967')
func_6968_call = mutated_mod.get_global_var('func_6968')
call_7296 = relay.TupleGetItem(func_6967_call(), 0)
call_7297 = relay.TupleGetItem(func_6968_call(), 0)
func_6903_call = mod.get_global_var('func_6903')
func_6907_call = mutated_mod.get_global_var('func_6907')
var_7299 = relay.var("var_7299", dtype = "uint32", shape = (63, 2))#candidate|7299|(63, 2)|var|uint32
const_7300 = relay.const([5,-9,-5,-3,6,5,-9,-8,2,9,-3,-7,-3,-9,-2,-9,6,-4,-8,3,7,5,10,-2,-1,-10,9,5,-10,9,1,-1,-6,9,1,8,-1,5,-8,6,9,-6,-1,-2,-7,7,1,-4,-2,-8,4,3,1,-9,-7,8,8,6,-5,4,-1,10,8,6,-7,-5,2,-8,-7,4,1,2,8,-3,-6,4,6,7,8,-4,-10,5,6,-7,-2,9,-2,5,8,-4,-4,4,-4,4,6,6,8,8,-7,-8,-5,-2,-7,9,-4,-2,1,8,6,-7,3,-6,7,6,-10,-4,-3,-4,-5,6,5,-10,3,-2,-4,-1,4,-10,3,6,-2,8,9,6,4,7,-1,8,9,-2,8,-1,-1,5,7,-7,4,-6,7,8,3,1,-4,-7,8,5,-1,10,5,5,-7,-5,-8,-5,-1,6,-8,-10,-5,-3,-6,-1,-3,10,8,-4,-10,7,7,2,-5,-6,7,-5,-2,-7,7,9,1,-1,-7,-6,-1,-6,7,8,8,4,9,8,-8,-2,-3,6,-10,-4,2,-3,-7,1,7,-5,-3,-8,10,4,1,2,6,-1,-7,-3,-7,1,-5,9,4,-7,-6,-9,-3,2,-10,-9,6,-3,4,-3,-2,8,-9,-9,2,-1,-3,3,-5,9,3,2,-9,-2,10,-6,2,-10,-1,-5,5,1,8,3,1,7,-3,3,3,-4,3,-5,-6,-7,6,-1,-9,10,-6,-9,6,-1,6,-10,9,1,-8,6,-5,-2,-6,3,-5,1,5,-10,-7,-1,-5,1,9,-8,10,10,9,-6,4,8,-2,5,-10,-10,6,-9,4,-6,2,9,-10,-7,2,-3,3,-8,-2,-2,-7,-1,-6,5,2,5,7,-8,-5,-5,-8,-5,-2,4,7,-8,10,9,-4,10,-8,-2,8,-2,-4,-2,-5,-5,-10,-1,-7,-1,-2,5,-5,-2,9,-7,-3,-2,6,-1,-8,8,-5,5,9,9,8,-5,-8,-5,-8,-3,-1,-10,-6,-6,7,-4,-2,-6,-9,-2,10,10,-4,-4,7,-5,-2,-3,-6,-5,-2,7,10,-7,-10,-5,-4,-8,-2,-1,10,5,-1,-2,-9,1,-8,9,6,8,-5,-6,-10,7,9,-10,8,-2,-6,-7,1,-10,10,8,5,2,1,-9,4,-2,8,1,9,-4,-6,-2,10,-8,1,-6,10,-4,-6,1,-9,-1,6,10,5,-2,4,2,6,-4,-3,-3,8,3,10,-2,-10,-5,-8,2,10,6,10,10,7,-2,4,-3,-3,-4,2,-2,-2,-9,-4,4,6,10,10,-1,1,5,-1,8,7,-8,10,3,9,-2,4,-6,8,8,3,-6,7,2,2,-3,-3,-7,-3,5,-2,-4,3,-1,-6,-2,10,-7,-1,-6,-10,1,-10,-4,-9,-4,6,-9,7,-1,-1,-4,-10,8,2,4,3,-3,2,-7,-6,3,-8,-2,-4,-10,5,6,6,9,-7,10,-6,4,-2,-10,9,-2,-10,4,7,-9,-7,-10,-10,-3,-1,7,-5,7,2,-8,5,-8,4,8,-5,6,3,-6,-6,-10,-3,-6,9,-8,3,2,5,2,3,1,-7,9,-2,3,-8,-4,-9,1,-4,-9,-4,6,2,-7,7,2,-4,4,-9,-5,-1,8,-1,-9,8,3,-10,1,6,8,7,-5,-4,8,-9,10,2,-9,-9,-8,-6,-10,2,2,-9,-9,-2,-9,7,-10,8,4,10,-3,-2,9,-5,-6,-10,3,9,-8,-8,7,-2,-2,7,-10,-1,-9,7,-3,-4,-7,9,4,4,9,6,-7,-5,9,-5,10,-6,-9,4,3,-10,2,2,7,7,8,-4,-2,-6,-10,3,-6,-6,10,-8,-7,3,8,-5,-1,-1,-6,8,3,-2,-4,2,4,7,-9,6,3,-7,-7,6,-5,-1,-3,10,10,10,6,5,1,1,9,7,-9,3,-9,5,3,4,2,1,-5,-5,-4,-9,4,-6,-9,3,9,5,-4,-1,-4,-4,-8,-8,7,-4,-6,7,-4,3,7,-5,-3,-6,9,-5,-4,-1,3,7,-5,-2,-5,2,-3,7,10,-10,-10,-9,6,4,-10,-4,6,-6,4,3,8,-1,10,-1,-7,3,-7,-8,4,-5,-9,-1,10,-8,-5,2,-8,-4,-10,-9,6,-4,-4,-10,-4,-5,1,8,1,-4,6,-10,10,3,9,-4,-3,9,-1,-6,-3,-8,4,4,1,-2,5,-5,5,4,1,-8,8,-4,8,6,10,6,9,3,-9,10,8,10,3,-5,3,1,-3,-10,6,2,9,1,-7,1,9,1,-7,1,6,4,-1,9,-1,-7,-5,2,7,4,-8,-2,-6,-6,-6,3,-3,1,4,-8,-9,2,3,9,-7,-6,8,6,4,7,9,4,-6,5,-5,7,-7,-9,2,10,1,-6,5,2,-4,-1,-8,-4,-8,-6,-2,-6,-1,9,2,-3,-7,-3,3,-2,-6,-9,-8,7,-9,-8,6,-2,-10,10,-2,7,6,-2,7,3,8,8,-4,-1,-9,-6,4,2,8,-8,-7,-10,6,9,7,-9,-5,-1,3,1,-3,-5,-6,-3,-8,-7,-5,-7,8,-6,-9,1,1,4,8,-6,-4,-9,7,-7,2,-2,-10,10,7,4,-1,2,1,-8,1,9,4,-8,-2,7,-8,3,-10,-5,-8], dtype = "uint32")#candidate|7300|(1008,)|const|uint32
call_7298 = relay.TupleGetItem(func_6903_call(relay.reshape(var_7299.astype('uint32'), [126,]), relay.reshape(const_7300.astype('uint32'), [1008,]), ), 2)
call_7301 = relay.TupleGetItem(func_6907_call(relay.reshape(var_7299.astype('uint32'), [126,]), relay.reshape(const_7300.astype('uint32'), [1008,]), ), 2)
func_6176_call = mod.get_global_var('func_6176')
func_6181_call = mutated_mod.get_global_var('func_6181')
const_7312 = relay.const(8, dtype = "uint32")#candidate|7312|()|const|uint32
const_7313 = relay.const([-3,-3,-9,10,2,-1,-3,-5,5,-10,6,-5,-8,8,-8,8,9,2,-2,5,-6,8,9,10,1,-10,2,3,-10,6,3,9,5,1,4,1,4,1,-3,7,3,-10,-3,-6,7,2,6,-1,3,-10,9,8,1,7,2,-7,-1,9,1,10,-7,-7,4,-6,1,7], dtype = "uint32")#candidate|7313|(66,)|const|uint32
const_7314 = relay.const([[-7,1,-8,7,-8,2,-6,-2,2,-10,-8,1,6,3,4,-1,-4,3,7,-6,7,-8,-2,6,6,-10,-3,-4,1,-8,7,-7,10,-5,-2,-3,6,1,-4,3,3,6,-4,-6,-8,-9,-2,7,8,2,-2,8,8,9,-8,-2,4,8,-8,5,9,-10,2,-6,9,10,-4,-1,-2,6,1,-1,-8,4,-3,10,5,-2,7,-7,5,8,-10,2,9,9,6,8,-9,9,-3,2,1,5,2,-2,1,-6,1,10,6,4,9,7,6,8,7,7,5,-3,6,-4,9,8,6,2,7,-5,9,4,5,5,3,-9,-6,5,-2,-8,7,-1,-4,-6,-10,-7,2,-4,-3,-1,3,-5,4,2,9,7,6,2,2,8,10,10,-9,8,-5,10,-9,-6,7,9,8,3,-3,-3,-4,6,8,-7,-2,9,-6,-5,6,-9,9,-8,-1,2,-7,-8,8,8,-2,3,9,-1,-2,9,-10,-10,6,6,2,-3,3,-3,-7,-6,-3,-5,2,-7,-2,4,-7,-1,-6,-10,6,-7,-5,1,1,-3,8,-7,3,7,-2,-9,7,10,8,-10,-3,5,-9,-2,-4,5,2,-2,-5,2,10,-4,1,8,6,-6,-9,7,-7,-10,-5,-5,-6,3,6,9,-7,2,-9,-9,-2,-3,6,-1,-10,-6,-6,3,-7,-3,4,-8,-7,10,5,-2,-4,8,-7,-5,-1,-4,-1,9,5,-3,-4,-9,3,8,1,-5,-6,-7,3,2,2,-1,4,2,-1,-8,6,-7,-1,7,8,-6,-4,-9,-4,8,-6,-2,-8,10,9,-6,9,4]], dtype = "int64")#candidate|7314|(1, 312)|const|int64
call_7311 = relay.TupleGetItem(func_6176_call(relay.reshape(const_7312.astype('uint32'), []), relay.reshape(const_7313.astype('uint32'), [66,]), relay.reshape(const_7314.astype('int64'), [156, 2]), ), 0)
call_7315 = relay.TupleGetItem(func_6181_call(relay.reshape(const_7312.astype('uint32'), []), relay.reshape(const_7313.astype('uint32'), [66,]), relay.reshape(const_7314.astype('int64'), [156, 2]), ), 0)
output = relay.Tuple([call_7296,call_7298,var_7299,const_7300,call_7311,const_7312,const_7313,const_7314,])
output2 = relay.Tuple([call_7297,call_7301,var_7299,const_7300,call_7315,const_7312,const_7313,const_7314,])
func_7328 = relay.Function([var_7299,], output)
mod['func_7328'] = func_7328
mod = relay.transform.InferType()(mod)
mutated_mod['func_7328'] = func_7328
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7329 = relay.var("var_7329", dtype = "uint32", shape = (63, 2))#candidate|7329|(63, 2)|var|uint32
func_7328_call = mutated_mod.get_global_var('func_7328')
call_7330 = func_7328_call(var_7329)
output = call_7330
func_7331 = relay.Function([var_7329], output)
mutated_mod['func_7331'] = func_7331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7007_call = mod.get_global_var('func_7007')
func_7009_call = mutated_mod.get_global_var('func_7009')
call_7408 = func_7007_call()
call_7409 = func_7007_call()
output = call_7408
output2 = call_7409
func_7440 = relay.Function([], output)
mod['func_7440'] = func_7440
mod = relay.transform.InferType()(mod)
output = func_7440()
func_7441 = relay.Function([], output)
mutated_mod['func_7441'] = func_7441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6512_call = mod.get_global_var('func_6512')
func_6514_call = mutated_mod.get_global_var('func_6514')
call_7442 = relay.TupleGetItem(func_6512_call(), 0)
call_7443 = relay.TupleGetItem(func_6514_call(), 0)
output = relay.Tuple([call_7442,])
output2 = relay.Tuple([call_7443,])
func_7445 = relay.Function([], output)
mod['func_7445'] = func_7445
mod = relay.transform.InferType()(mod)
mutated_mod['func_7445'] = func_7445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7445_call = mutated_mod.get_global_var('func_7445')
call_7446 = func_7445_call()
output = call_7446
func_7447 = relay.Function([], output)
mutated_mod['func_7447'] = func_7447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6967_call = mod.get_global_var('func_6967')
func_6968_call = mutated_mod.get_global_var('func_6968')
call_7537 = relay.TupleGetItem(func_6967_call(), 0)
call_7538 = relay.TupleGetItem(func_6968_call(), 0)
output = call_7537
output2 = call_7538
func_7553 = relay.Function([], output)
mod['func_7553'] = func_7553
mod = relay.transform.InferType()(mod)
output = func_7553()
func_7554 = relay.Function([], output)
mutated_mod['func_7554'] = func_7554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6295_call = mod.get_global_var('func_6295')
func_6296_call = mutated_mod.get_global_var('func_6296')
call_7558 = relay.TupleGetItem(func_6295_call(), 0)
call_7559 = relay.TupleGetItem(func_6296_call(), 0)
output = call_7558
output2 = call_7559
func_7588 = relay.Function([], output)
mod['func_7588'] = func_7588
mod = relay.transform.InferType()(mod)
mutated_mod['func_7588'] = func_7588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7588_call = mutated_mod.get_global_var('func_7588')
call_7589 = func_7588_call()
output = call_7589
func_7590 = relay.Function([], output)
mutated_mod['func_7590'] = func_7590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6809_call = mod.get_global_var('func_6809')
func_6810_call = mutated_mod.get_global_var('func_6810')
call_7600 = relay.TupleGetItem(func_6809_call(), 5)
call_7601 = relay.TupleGetItem(func_6810_call(), 5)
uop_7602 = relay.sqrt(call_7600.astype('float32')) # shape=(15, 2, 13)
uop_7604 = relay.sqrt(call_7601.astype('float32')) # shape=(15, 2, 13)
func_5745_call = mod.get_global_var('func_5745')
func_5750_call = mutated_mod.get_global_var('func_5750')
const_7611 = relay.const([9.530631,-0.231144,-9.044265,1.983575,9.568309,-2.111203,-5.078358,7.525095,-6.715447,-4.240396,9.963118,-8.664721,8.697324,7.820434,7.831196,5.173134,4.063413,7.783135,3.791941,3.352590,2.642277,3.377391,7.866518,-7.998101,-1.389846,-4.062444,-4.937761,-3.475714,3.180623,-4.051063,8.166789,5.186702,2.278967,-9.397209,5.541732,-7.597465,5.404499,8.743434,-3.113594,2.580454,-3.325209,-2.895898,-7.018190,1.961725,-0.744444,-3.461628,1.772889,-9.297867,-4.837463,3.370976,3.351022,-4.618044,3.620833,3.957809,4.625311,7.829151,-4.047340,-7.855291,-6.724493,1.075163,-0.439141,-2.408905,5.112789,-3.915646,-0.420837,-1.699039,4.823603,-0.427799,-7.845173,-2.866922,-8.310287,5.593334,8.931100,3.294502,5.875610,4.950633,-7.802057,6.480643,-1.963150,-3.130577,-6.526824,-1.423620,4.601241,-5.276040,-7.625725,-9.173771,-3.858264,-7.598203,3.083571,8.004689,-6.829213,-9.194647,9.491350,-2.796587,-9.884415,-6.730625,3.042274,-8.478580,6.062780,-8.246175,-6.229878,9.340096,0.241451,-2.180024,0.743392,7.487163,-3.599606,8.020390,-1.979165,-4.177131,-6.253561,9.366616,7.933383,-0.543552,-0.105792,2.484023,0.549493,-7.748529,-7.026473,-6.960783,-1.984790,7.173167,5.216191,-8.853642,-9.151904,-4.483647,9.051134,8.257994,-0.932394,-8.781753,-8.445462,0.672548,-5.818149,-1.112357,-3.565707,-6.820106,6.491881,-0.754131,-0.579899,-7.193840,6.684924,5.226463,-9.759069,2.594539,3.845820,3.023785,8.872492,1.982369,-9.852005,-8.548506], dtype = "float64")#candidate|7611|(150,)|const|float64
var_7612 = relay.var("var_7612", dtype = "float64", shape = (1500,))#candidate|7612|(1500,)|var|float64
var_7613 = relay.var("var_7613", dtype = "int64", shape = (312,))#candidate|7613|(312,)|var|int64
call_7610 = relay.TupleGetItem(func_5745_call(relay.reshape(uop_7602.astype('float64'), [15, 2, 13]), relay.reshape(const_7611.astype('float64'), [150,]), relay.reshape(var_7612.astype('float64'), [1500,]), relay.reshape(var_7613.astype('int64'), [312,]), ), 7)
call_7614 = relay.TupleGetItem(func_5750_call(relay.reshape(uop_7602.astype('float64'), [15, 2, 13]), relay.reshape(const_7611.astype('float64'), [150,]), relay.reshape(var_7612.astype('float64'), [1500,]), relay.reshape(var_7613.astype('int64'), [312,]), ), 7)
func_6512_call = mod.get_global_var('func_6512')
func_6514_call = mutated_mod.get_global_var('func_6514')
call_7619 = relay.TupleGetItem(func_6512_call(), 3)
call_7620 = relay.TupleGetItem(func_6514_call(), 3)
func_732_call = mod.get_global_var('func_732')
func_735_call = mutated_mod.get_global_var('func_735')
var_7625 = relay.var("var_7625", dtype = "float32", shape = (168,))#candidate|7625|(168,)|var|float32
call_7624 = relay.TupleGetItem(func_732_call(relay.reshape(var_7625.astype('float32'), [168,])), 0)
call_7626 = relay.TupleGetItem(func_735_call(relay.reshape(var_7625.astype('float32'), [168,])), 0)
output = relay.Tuple([uop_7602,call_7610,const_7611,var_7612,var_7613,call_7619,call_7624,var_7625,])
output2 = relay.Tuple([uop_7604,call_7614,const_7611,var_7612,var_7613,call_7620,call_7626,var_7625,])
func_7630 = relay.Function([var_7612,var_7613,var_7625,], output)
mod['func_7630'] = func_7630
mod = relay.transform.InferType()(mod)
mutated_mod['func_7630'] = func_7630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7630_call = mutated_mod.get_global_var('func_7630')
var_7632 = relay.var("var_7632", dtype = "float64", shape = (1500,))#candidate|7632|(1500,)|var|float64
var_7633 = relay.var("var_7633", dtype = "int64", shape = (312,))#candidate|7633|(312,)|var|int64
var_7634 = relay.var("var_7634", dtype = "float32", shape = (168,))#candidate|7634|(168,)|var|float32
call_7631 = func_7630_call(var_7632,var_7633,var_7634,)
output = call_7631
func_7635 = relay.Function([var_7632,var_7633,var_7634,], output)
mutated_mod['func_7635'] = func_7635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mod.get_global_var('func_7037')
func_7039_call = mutated_mod.get_global_var('func_7039')
call_7670 = relay.TupleGetItem(func_7037_call(), 0)
call_7671 = relay.TupleGetItem(func_7039_call(), 0)
output = relay.Tuple([call_7670,])
output2 = relay.Tuple([call_7671,])
func_7674 = relay.Function([], output)
mod['func_7674'] = func_7674
mod = relay.transform.InferType()(mod)
output = func_7674()
func_7675 = relay.Function([], output)
mutated_mod['func_7675'] = func_7675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_7839 = relay.TupleGetItem(func_5615_call(), 0)
call_7840 = relay.TupleGetItem(func_5617_call(), 0)
func_5919_call = mod.get_global_var('func_5919')
func_5923_call = mutated_mod.get_global_var('func_5923')
const_7861 = relay.const([7.016898,-1.188865,7.379856,-7.643819,-8.058681,5.247122,7.871775,-7.464355,6.955988,-9.295530,1.259303,4.367880,4.928947,1.086294,3.620496,-0.963041,4.606090,-5.059719,-1.306724,-8.995094,3.609381,-7.841163,8.540845,-1.831397,9.078387,-0.884067,5.406225,-5.865638,9.678029,0.921518,9.427695,5.254973,-7.208282,1.810165,-9.976775,-6.963248,4.134047,7.726872,5.654279,-2.797252,-8.076988,3.835174,-2.470784,-5.690130,6.921475,-8.118437,2.340389,5.539004,0.565990,-1.939079,-3.820288,8.930151,1.923416,3.963694,-6.630340,1.236263,-4.522296,4.650141,9.400264,-5.970234,1.731555,9.110416,-8.987834,0.397602,9.851677,-1.497904,-1.892237,-6.239027,-5.356693,-3.432055,4.498139,8.195574,1.954709,-0.792766,-0.061596,8.473318,2.106319,-2.604912,-6.053405,-0.508914,-1.255493,6.680501,-4.692620,-0.523046,6.820288,-1.126962,7.597340,7.943885,-5.975714,5.715443,-3.318678,-4.898767,0.669397,-7.519852,-3.229939,5.787670,7.406746,5.208334,-0.253712,-8.725160,4.433196,-8.390394,-4.947261,9.466414,9.299671,1.798590,3.697136,-5.163438,-9.768785,-0.588324,9.452025,1.467016,3.784113,-7.199239,9.982857,9.885378,4.109093,3.242839,9.399924,-8.998680,8.015815,8.502031,-2.328367,0.513458,-9.258635,5.691331,3.239287,-7.877954,-8.402954,9.214389,1.811749,-5.492653,-5.635208,-3.740490,-8.241086,8.983994,-2.227640,-7.581434,-0.402351,4.507553,-5.047737,-6.106268,-9.218318,-2.544040,2.413571,-6.933188,-8.159281,-4.260351,-2.630972,4.988297,3.768997,-8.788979,3.672606,-3.324145,-8.368232,-5.013492,2.344748,-6.985026,6.019506,-0.914192,-6.751910,6.986171,7.513392,-5.528699,-2.215244,-7.535049,-0.311641,8.902701,5.624966,3.436481,9.538437,-9.502442,-9.760412,-3.916050,9.158175,-3.778415,1.208915,3.578237,8.647522,-9.741603,2.577471,-5.239570,7.427350,7.528119,3.073062,-6.597122,-4.616941,8.071921,-2.229104,-2.993496,-4.511188,9.093780,-1.242615,-4.732371,-1.431779,3.455905,7.860150,9.963610,3.029949,-3.513025,8.890582,8.006203,7.105001,-3.025504,9.683700,-7.461893,-1.010381,5.717022,-5.215389,-5.402057,1.979561,-6.637094,3.161210,0.470425,-7.546319,-8.993915,7.204251,6.749546,-2.971976,-7.654726,-7.661187,-5.679129,-5.430009,2.469633,7.257821,-6.566516,6.872317,-9.665745,-2.518000,1.044907,2.994314,6.452727,0.289249,5.714284,-4.008920,9.572568,-3.474235,9.683736,-4.777007,9.675026,7.873158,-0.112519,-5.479158,9.843347,-2.351425,2.728800,-3.829818,-6.199370,9.797422,-9.747185,9.539443,-0.044555,9.950367,2.766454,-5.530996,1.458450,-6.181847,-4.570209,-7.960627,2.049999,-3.587001,-4.366252,5.851820,4.510008,7.325624,5.329116,4.034898,-0.078307,0.877287,-6.222139,7.772516,6.471622,5.184765,-2.938421,-5.721437,3.240157,7.382102,5.332388,-5.346789,3.570439,-4.323615,5.144724,4.013028,-4.232750,0.435783,-6.176853,4.375239,-4.399638,-6.157563,-9.961398,-1.143046,5.394894,-2.683517,2.815223,9.394553,-7.443384,2.613273,-7.035413,3.902311,9.166907,2.649848,8.014239,-3.733718,-5.083709,9.204179,7.815487,-2.076412,4.395128,3.845153,5.788956,2.581497,4.788815,3.734135,1.809757,-5.035383,1.720835,0.496244,-0.802041,-8.031387,-0.226303,-7.437956,-7.911455,-9.628675,1.464303,-3.802220,4.299658,-9.795929,-2.579268,-2.716949,-1.515845,-2.098109,-4.416418,7.601777,3.380358,2.498099,0.724365,5.787425,-7.994885,7.039333,-2.174047,2.238523,9.347493,-1.342516,5.548197,-6.902684,2.186624,-7.134355,-3.772682,9.060534,4.073820,0.619649,-8.617589,-4.179734,-5.018363,-6.111142,4.247102,-0.780465,8.726440,-9.867602,3.154907,-3.116975,-7.593260,5.299341,-0.156517,-2.529796,2.083410,-1.731263,6.007659,0.537168,-9.525724,-6.049542,0.660391,1.647121,0.836689,4.376913,-7.995416,4.646682,-8.258143,9.344535,6.302720,0.310339,6.282450,-2.412035,-2.155877,-9.783439,4.787846,8.592090,-0.353013,1.818064,-1.828065,-6.130938,3.747501,0.411032,-5.200199,-6.611187,4.535965,5.816122,-6.729909,3.495108,8.771553,9.571051,-2.694807,4.979492,4.503512,-3.752583,1.559974,-9.059335,-0.255983,0.702942,-8.175855,6.473583,8.185788,-2.687946,-5.293001,-0.430391,-0.223910,3.842604,-3.580029,9.183490,2.276362,-2.121761,-9.227885,8.605018,-9.439273,-1.454438,0.176500,-1.386502,-3.956916,-7.036905,-1.335533,-2.150061,-6.426779,6.070976,-8.426263,2.463783,-5.375307,-3.485296,-8.453038,-1.441587,-9.634860,-9.703886,-3.675194,-2.661565,5.597438,1.323652,-1.013046,-9.532753,3.613480,0.540575,-9.267900,-7.129103,-6.489553,-7.854290,-9.784053,-8.196214,6.443318,-3.948800,4.163550,-4.446489,4.463012,8.226668,3.104946,1.862199,3.267617,-8.848464,5.653746,5.597569,5.485180,-3.113187,-7.682748,3.354537,9.471290,4.052677,-7.983830,-2.457867,7.319242,3.530096,2.856900,-6.301603,-7.774452,3.948467,8.564825,2.941884,-4.964638,-6.307772,-1.774885,-4.840386,-3.181680,3.415060,5.715513,-3.881511,2.002041,4.294803,-3.731428,0.146084,-2.660158,-4.447895,9.433527,-2.245809,-3.729773,-9.683751,-5.085651,-4.577830,-9.648664,-9.469862,8.843619,7.613516,-5.482436,-9.067110,-1.791336,4.422099,-2.037222,-1.907869,-6.191298,5.500319,4.373650,3.833196,-6.886400,-1.568107,9.571192,-4.651710,-3.477319,3.804419,-4.136023,3.502036,-2.947019,9.152012,0.173052,-6.210597,-2.343179,-5.036482,-0.977669,-8.345225,5.217137,6.926151,5.736754,-1.049393,1.945334,-8.495234,5.753441,-0.219579,9.398608,-6.018687,9.361388,-7.640047,-9.746936,-1.577238,-2.855477,6.870363,4.904939,0.366902,-2.222709,-1.553915,0.518318,4.105991,1.473994,-8.582593,8.194338,5.874654,-6.192984,-2.967606,-7.242115,6.030692,4.409746,-5.678370,7.645156,2.497133,9.826246,-6.105322,3.592333,5.149252,2.124882,2.498835,-9.916649,-1.371753,-2.370348,8.642637,5.395742,1.798286,6.003924,6.273908,9.749189,-1.072000,6.831764,-2.466770,-1.061225,7.278685,0.828729,-2.861057,6.041280,-9.435799,-6.451473,-8.291593,-9.347084,-7.015852,2.265065,9.023184,2.642681,-6.754884,-6.572535,9.861551,-8.770860,-1.770785,6.268760,-4.706433,2.998185,-4.069397,-3.103994,4.562261,-8.465368,5.444686,-1.925369,4.092228,-9.060119,-4.817676,-2.451643,-0.047669,-0.597602,-9.479105,1.384424,-8.122763,-9.578154,-8.734639,5.790464,7.708998,-1.039084,1.733771,8.893798,-0.273698,-8.712220,-7.054602,-6.799645,-8.072573,-2.763513,-8.176116,8.919913,-0.642829,8.603084,-5.284784,1.087076,-6.191909,-2.969379,-8.897000,-3.730221,-2.807404,3.250916,4.752470,9.896940,-6.285995,1.747825,5.183302,0.902519,-4.084024,6.932553,0.711670,-2.784597,-2.601885,4.172204,3.468350,1.040961,1.753349,-9.902885,-1.853322,-3.963610,1.574675,9.616030,-2.532262,2.959224,2.353481,4.578732,9.203523,-1.827248,3.773801,-2.822406,-1.476065,-2.309334,-2.230142,-8.740290,-9.982639,1.664163,-5.839335,-5.851486,6.583239,6.254615,-4.222430,8.837049,0.895511,0.903789,2.267262,9.254743,5.183266,3.407358,-7.946653,-1.692507,-9.126883,5.929787,-1.999125,8.972622,6.441977,-1.838808,-6.365560,2.331471,-7.860229,-6.887292,-3.856323,4.014451,5.790044,8.775422,-7.120889,-1.002660,9.225641,-2.081458,2.871609,8.134307,-9.231619,1.973913,1.114284,-0.649415,1.808962,7.293554,-9.704637,-4.075962,-5.518873,-4.860236,3.249776,7.083914,-1.305123,5.997074,-8.057610,-6.204986,-8.978354,7.378372,-4.817921,0.978578,-2.296907,0.179747,1.907022,-1.308466,1.045071,8.493124,2.112148,8.680813,-0.429930,5.587688,5.421146,0.816349,7.228093,0.328632,8.827683,-6.292701,4.649418,-3.654744,0.867724,-8.264363,1.054943,9.962942,9.421200,-8.195901,9.918459,-0.963637,2.411951,9.447849,-4.249290,-9.849713,3.348315,8.584776,-8.404385,-8.967780,-5.270244,-2.035200,-3.530668,-7.298869,-5.100171,0.284933,-8.897100,-3.980551,3.049919,1.340482,-9.938072,7.541074,-8.653293,6.817469,2.589466,-7.806516,-1.193620,3.489797,-3.377903,-3.268558,1.673216,0.176517,8.053019,2.588782,6.748236,-2.917646,6.143841,6.957783,-1.678733,-5.410772,-7.303564,9.813828,-1.346518,0.621120,-1.093474,2.127633,7.104134,-6.549749,7.052290,-9.389937,-1.156586,-2.012644,-8.529189,7.969864,-8.103042,-7.827136,-2.117439,-5.595799,4.516784,2.174477,2.328815,7.452518,3.739410,-9.430234,1.064945,5.242901,7.074484,5.690540,-4.744307,6.766822,5.925142,0.271556,7.159750,-1.385030,-6.053352,9.779194,-2.422057,-3.393117,-6.077157,-3.726601,6.208904,3.157937,-9.899988,0.914744,1.133146,5.950816,-4.504609,-9.082214,-9.437604,-3.467802,-8.507226,6.774171,-5.411309,2.322234,-1.445655,3.439451,9.125643,-7.917451,9.975159,-6.250763,-7.889642,3.128307,7.733745,4.439269,-2.600055,-8.253735,7.742211,-7.537435,5.832516,-5.885331,4.335253,-4.021149,-5.627713,-0.899298,-9.096140,-2.264480,9.778165,9.480671,2.566181,-9.986219,6.333096,-8.472840,-0.555922,-0.166321,-3.276236,1.909315,-8.571563,7.189354,6.493425,5.292071,-0.873682,-8.455757,2.149274,-7.479450,-1.881278,9.827231,3.506581,-5.290463,-7.677395,-1.234313,9.910029,-2.604619], dtype = "float32")#candidate|7861|(900,)|const|float32
var_7862 = relay.var("var_7862", dtype = "float64", shape = (140, 24))#candidate|7862|(140, 24)|var|float64
call_7860 = relay.TupleGetItem(func_5919_call(relay.reshape(const_7861.astype('float32'), [15, 4, 15]), relay.reshape(const_7861.astype('float32'), [15, 4, 15]), relay.reshape(var_7862.astype('float64'), [3360,]), ), 0)
call_7863 = relay.TupleGetItem(func_5923_call(relay.reshape(const_7861.astype('float32'), [15, 4, 15]), relay.reshape(const_7861.astype('float32'), [15, 4, 15]), relay.reshape(var_7862.astype('float64'), [3360,]), ), 0)
func_6207_call = mod.get_global_var('func_6207')
func_6208_call = mutated_mod.get_global_var('func_6208')
call_7874 = func_6207_call()
call_7875 = func_6207_call()
output = relay.Tuple([call_7839,call_7860,const_7861,var_7862,call_7874,])
output2 = relay.Tuple([call_7840,call_7863,const_7861,var_7862,call_7875,])
func_7884 = relay.Function([var_7862,], output)
mod['func_7884'] = func_7884
mod = relay.transform.InferType()(mod)
var_7885 = relay.var("var_7885", dtype = "float64", shape = (140, 24))#candidate|7885|(140, 24)|var|float64
output = func_7884(var_7885)
func_7886 = relay.Function([var_7885], output)
mutated_mod['func_7886'] = func_7886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7445_call = mod.get_global_var('func_7445')
func_7447_call = mutated_mod.get_global_var('func_7447')
call_7941 = relay.TupleGetItem(func_7445_call(), 0)
call_7942 = relay.TupleGetItem(func_7447_call(), 0)
uop_7944 = relay.log10(call_7941.astype('float64')) # shape=(15, 2, 13)
uop_7946 = relay.log10(call_7942.astype('float64')) # shape=(15, 2, 13)
output = uop_7944
output2 = uop_7946
func_7965 = relay.Function([], output)
mod['func_7965'] = func_7965
mod = relay.transform.InferType()(mod)
output = func_7965()
func_7966 = relay.Function([], output)
mutated_mod['func_7966'] = func_7966
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8002 = relay.var("var_8002", dtype = "float32", shape = (16, 14, 3))#candidate|8002|(16, 14, 3)|var|float32
var_8003 = relay.var("var_8003", dtype = "float32", shape = (16, 14, 3))#candidate|8003|(16, 14, 3)|var|float32
bop_8004 = relay.less(var_8002.astype('bool'), relay.reshape(var_8003.astype('bool'), relay.shape_of(var_8002))) # shape=(16, 14, 3)
func_6574_call = mod.get_global_var('func_6574')
func_6578_call = mutated_mod.get_global_var('func_6578')
var_8014 = relay.var("var_8014", dtype = "uint8", shape = (60,))#candidate|8014|(60,)|var|uint8
const_8015 = relay.const([-4.030630,-0.572807,5.524489,3.555913,-3.094821,-7.461714,6.751629,-0.102547,1.532898,4.019781,-3.684585,-0.430911,4.858082,7.820351,-3.981745,8.341958,-1.478653,-6.505654,8.040873,3.688919,-0.667790,3.694417,5.282757,-9.374101,-1.808385,4.445249,-8.224614,-7.577397,-6.598618,-2.215465,7.295089,-6.610181,3.605175,8.256079,-8.151385,0.721242,-7.565382,-9.788333,-6.382035,-6.938420,-5.419694,2.750984,-5.523723,1.930703,6.734357,5.595114,6.112633,7.828546,3.010878,3.489792,5.999852,-1.978247,8.149561,4.165169,6.309035,5.585113,1.950981,-4.615159,-7.395061,8.343872,-6.519842,-4.262617,-0.532033,-1.039884,-9.246089,4.283324,-2.921789,1.313755,-4.287224,6.834526,7.317855,0.699162,7.108113,-4.833162,4.563142,-9.290421,-8.149290,1.098398,-9.632395,-7.093063,-4.824001,-7.704999,6.320499,-4.935445,-9.259504,-5.351480,-5.962587,6.512052,9.332689,2.386043,3.718239,-3.604762,-0.783871,-4.983911,-5.537707,2.013812,-2.803074,3.396275,-0.005187,1.148300,-6.554329,-1.477179,7.540196,-8.056730,8.819160,-1.454350,8.600176,-7.641742,-9.090819,-3.177260,-8.811346,1.916885,0.082890,-9.728639,4.247613,5.758820,4.074947,-0.408576,4.230728,-8.972259,0.345054,4.618815,6.624038,-3.958153,-9.733650,-7.534167,5.003464,1.403142,4.488302,-5.142773,5.683251,-5.067389,6.367816,3.863585,3.724810,1.595700,-5.891275,-2.436208,-0.085481,-8.201586,7.447003,6.753958,-3.111555,-6.925776,7.085746,-1.722470,-3.795323,8.627183,-2.228915,-9.667735,-5.644867,-7.948644,-8.443396,9.622359,0.677148,0.343183,-0.538228,3.568829,6.853262,-4.003732,-3.623909,8.542378,2.969333,-7.646501,1.746360,-1.628105,-1.203761,8.782536,8.787441,-8.921256,-4.441347,6.539200,-9.588798,9.656836,-3.509479,-7.227336,5.484696,8.770717,8.346580,-6.794587,-9.332002,-5.892095,7.435647,3.178249,-4.053268,3.549226,5.242348,-8.653473,-4.607918,9.255408,5.487227,1.489417,9.711461,-8.698107,1.783307,-0.235906,9.230491,-1.324747,-1.238154,7.815272,6.813406,2.088978,2.535296,0.386405,4.144505,8.198379,-8.769232,7.082582,9.963115,-3.098892,-1.681234,3.386894,-2.517213,-0.658098,2.650599,0.627224,4.665349,-0.826635,-7.139508,-4.039786,-9.552852,0.479448,-4.402414,1.804487,-9.814809,-3.512068,-2.413590,-2.707704,-2.726823,0.455772,-8.038501,-9.110052,5.239591,-1.631486,-2.249145,8.271926,-5.320090,-6.630749,-7.520969,7.546559,4.781105,8.337740,7.309307,-1.658033,0.497587,1.110812,0.280242,9.662802,-1.021811,-2.026681,-9.854408,-1.574025,-9.915114,7.723976,-5.125270,1.750521,9.088715,3.702390,-3.158583,-7.056214,9.736300,1.878873,2.690779,8.599988,6.710777,9.680116,8.766054,-0.873337,-8.594511,-9.335305,-6.692387,-8.551532,6.126776,-0.179788,-9.364250,5.344411,1.264382,-4.915763,5.064495,-8.972735,7.223990,-2.436995,6.456774,1.900858,-0.199321,-0.765136,3.315171,-0.318797,-6.614640,9.274110,4.406288,-7.817599,2.227012,-7.722564,-9.505028,4.530436,-7.838520,4.777363,0.374684,8.889294,-1.784509,-0.254950,-9.435257,-5.901586,-1.689670,9.838128,-6.771741,-5.162228,-9.207907,-0.044608,8.220064,4.047589,2.383304,-5.641181,3.695094,2.156866,1.854666,8.625491,-0.892358,1.355295,3.235578,0.731627,-2.516730,-6.005973,-5.703193,-1.058285,-5.059157,7.328095,-4.536716,-2.931647,4.553082,3.513837,-7.165804,-0.470208,5.374479,2.172544,9.718287,-4.846965,-7.675997,-5.090276,-6.946812,-6.011755,-6.761590,-0.337010,9.799151,-2.633060,-7.921288,-9.623434,9.795095,-8.463595,-1.759324,3.796006,-5.428920,6.614818,-3.900151,5.644288,-2.346050,-9.579135,0.919292,2.464607,1.992444,3.002140,-6.737181,-3.312209,-5.108787,-5.883840,-9.834715,-7.758761,9.323844,9.008083,-5.703849,-8.329989,3.561912,4.222288,-3.157061,8.658976,5.922369,4.932320,-4.014438,0.022656,-1.017765,5.813325,2.324903,5.813092,-0.758242,3.623565,4.699748,2.787808,-2.076985,4.661828], dtype = "float64")#candidate|8015|(390,)|const|float64
call_8013 = relay.TupleGetItem(func_6574_call(relay.reshape(var_8014.astype('uint8'), [15, 4]), relay.reshape(const_8015.astype('float64'), [15, 2, 13]), ), 1)
call_8016 = relay.TupleGetItem(func_6578_call(relay.reshape(var_8014.astype('uint8'), [15, 4]), relay.reshape(const_8015.astype('float64'), [15, 2, 13]), ), 1)
func_7007_call = mod.get_global_var('func_7007')
func_7009_call = mutated_mod.get_global_var('func_7009')
call_8021 = func_7007_call()
call_8022 = func_7007_call()
func_6121_call = mod.get_global_var('func_6121')
func_6123_call = mutated_mod.get_global_var('func_6123')
call_8035 = func_6121_call()
call_8036 = func_6121_call()
output = relay.Tuple([bop_8004,call_8013,var_8014,const_8015,call_8021,call_8035,])
output2 = relay.Tuple([bop_8004,call_8016,var_8014,const_8015,call_8022,call_8036,])
func_8045 = relay.Function([var_8002,var_8003,var_8014,], output)
mod['func_8045'] = func_8045
mod = relay.transform.InferType()(mod)
var_8046 = relay.var("var_8046", dtype = "float32", shape = (16, 14, 3))#candidate|8046|(16, 14, 3)|var|float32
var_8047 = relay.var("var_8047", dtype = "float32", shape = (16, 14, 3))#candidate|8047|(16, 14, 3)|var|float32
var_8048 = relay.var("var_8048", dtype = "uint8", shape = (60,))#candidate|8048|(60,)|var|uint8
output = func_8045(var_8046,var_8047,var_8048,)
func_8049 = relay.Function([var_8046,var_8047,var_8048,], output)
mutated_mod['func_8049'] = func_8049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7553_call = mod.get_global_var('func_7553')
func_7554_call = mutated_mod.get_global_var('func_7554')
call_8072 = func_7553_call()
call_8073 = func_7553_call()
func_7674_call = mod.get_global_var('func_7674')
func_7675_call = mutated_mod.get_global_var('func_7675')
call_8076 = relay.TupleGetItem(func_7674_call(), 0)
call_8077 = relay.TupleGetItem(func_7675_call(), 0)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
const_8083 = relay.const([-3.511441,0.435707,0.684925,-1.070448,-0.373500,-9.013737,-5.365347,3.849730,-8.477409,-8.585596,-2.335331,-1.207190,-7.234137,2.141315,-4.756618,-6.715073,-5.357091,-4.391419], dtype = "float32")#candidate|8083|(18,)|const|float32
call_8082 = relay.TupleGetItem(func_4118_call(relay.reshape(const_8083.astype('float32'), [2, 9, 1])), 0)
call_8084 = relay.TupleGetItem(func_4120_call(relay.reshape(const_8083.astype('float32'), [2, 9, 1])), 0)
func_6963_call = mod.get_global_var('func_6963')
func_6964_call = mutated_mod.get_global_var('func_6964')
call_8087 = func_6963_call()
call_8088 = func_6963_call()
func_7445_call = mod.get_global_var('func_7445')
func_7447_call = mutated_mod.get_global_var('func_7447')
call_8097 = relay.TupleGetItem(func_7445_call(), 0)
call_8098 = relay.TupleGetItem(func_7447_call(), 0)
uop_8132 = relay.asinh(call_8097.astype('float32')) # shape=(15, 2, 13)
uop_8134 = relay.asinh(call_8098.astype('float32')) # shape=(15, 2, 13)
func_6284_call = mod.get_global_var('func_6284')
func_6287_call = mutated_mod.get_global_var('func_6287')
const_8137 = relay.const([2,5,-4,7,4,-8,6,-4,5,-7,-7,1,2,3,-9,5,-6,-9,-1,-6,6,7,-8,-6,-3,8,-3,-9,-10,2,5,-1,6,-3,6,6,-7,-5,-4,-6,5,-6,6,3,6,-5,1,-3,-8,7,-8,-8,-6,10,4,-8,1,-7,-7,-10,6,-5,-1,-7,5,-3,-5,-7,-3,-10,2,-8,-1,-9,7,-1,-5,1,5,5,10,-2,-8,-7,-8,10,4,-5,4,3,-5,4,3,8,-3,-7,-10,9,7,-10,2,7,9,3,5,-7,-10,-10,8,10,-10,6,5,-9,3,7,3,-5,5,-8,-2,1,-7,9,-9,-1], dtype = "uint32")#candidate|8137|(126,)|const|uint32
var_8138 = relay.var("var_8138", dtype = "uint32", shape = (504, 2))#candidate|8138|(504, 2)|var|uint32
call_8136 = relay.TupleGetItem(func_6284_call(relay.reshape(const_8137.astype('uint32'), [126,]), relay.reshape(var_8138.astype('uint32'), [1008,]), ), 0)
call_8139 = relay.TupleGetItem(func_6287_call(relay.reshape(const_8137.astype('uint32'), [126,]), relay.reshape(var_8138.astype('uint32'), [1008,]), ), 0)
func_7553_call = mod.get_global_var('func_7553')
func_7554_call = mutated_mod.get_global_var('func_7554')
call_8140 = func_7553_call()
call_8141 = func_7553_call()
func_7965_call = mod.get_global_var('func_7965')
func_7966_call = mutated_mod.get_global_var('func_7966')
call_8142 = func_7965_call()
call_8143 = func_7965_call()
bop_8144 = relay.less_equal(call_8097.astype('bool'), relay.reshape(call_8140.astype('bool'), relay.shape_of(call_8097))) # shape=(15, 2, 13)
bop_8147 = relay.less_equal(call_8098.astype('bool'), relay.reshape(call_8141.astype('bool'), relay.shape_of(call_8098))) # shape=(15, 2, 13)
output = relay.Tuple([call_8072,call_8076,call_8082,const_8083,call_8087,uop_8132,call_8136,const_8137,var_8138,call_8142,bop_8144,])
output2 = relay.Tuple([call_8073,call_8077,call_8084,const_8083,call_8088,uop_8134,call_8139,const_8137,var_8138,call_8143,bop_8147,])
func_8149 = relay.Function([var_8138,], output)
mod['func_8149'] = func_8149
mod = relay.transform.InferType()(mod)
var_8150 = relay.var("var_8150", dtype = "uint32", shape = (504, 2))#candidate|8150|(504, 2)|var|uint32
output = func_8149(var_8150)
func_8151 = relay.Function([var_8150], output)
mutated_mod['func_8151'] = func_8151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6207_call = mod.get_global_var('func_6207')
func_6208_call = mutated_mod.get_global_var('func_6208')
call_8162 = func_6207_call()
call_8163 = func_6207_call()
output = call_8162
output2 = call_8163
func_8197 = relay.Function([], output)
mod['func_8197'] = func_8197
mod = relay.transform.InferType()(mod)
output = func_8197()
func_8198 = relay.Function([], output)
mutated_mod['func_8198'] = func_8198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mod.get_global_var('func_7037')
func_7039_call = mutated_mod.get_global_var('func_7039')
call_8221 = relay.TupleGetItem(func_7037_call(), 0)
call_8222 = relay.TupleGetItem(func_7039_call(), 0)
output = relay.Tuple([call_8221,])
output2 = relay.Tuple([call_8222,])
func_8251 = relay.Function([], output)
mod['func_8251'] = func_8251
mod = relay.transform.InferType()(mod)
mutated_mod['func_8251'] = func_8251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8251_call = mutated_mod.get_global_var('func_8251')
call_8252 = func_8251_call()
output = call_8252
func_8253 = relay.Function([], output)
mutated_mod['func_8253'] = func_8253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7007_call = mod.get_global_var('func_7007')
func_7009_call = mutated_mod.get_global_var('func_7009')
call_8278 = func_7007_call()
call_8279 = func_7007_call()
func_6176_call = mod.get_global_var('func_6176')
func_6181_call = mutated_mod.get_global_var('func_6181')
const_8285 = relay.const(4, dtype = "uint32")#candidate|8285|()|const|uint32
const_8286 = relay.const([6,10,-3,4,-3,10,-3,-10,-4,2,3,-9,1,-5,1,-9,-2,-6,-10,-4,-7,6,9,10,-7,9,6,-9,1,1,5,-1,-3,-2,9,5,-2,5,8,-3,8,7,3,2,-1,7,6,-5,-5,1,4,-10,-8,-8,-10,5,4,-3,-9,2,-7,6,-5,2,7,-3], dtype = "uint32")#candidate|8286|(66,)|const|uint32
const_8287 = relay.const([7,-6,10,-5,-4,-7,7,-2,-6,6,-4,-2,-2,-4,-1,-6,6,3,-7,-3,9,-10,5,-5,-4,-4,3,-9,-6,10,7,6,-7,9,9,-7,-1,-5,2,9,3,6,-9,1,-7,-3,-6,-8,-9,-6,-9,5,1,-8,1,9,-3,10,-10,-7,1,-9,-10,7,-4,-6,-8,-4,-2,-10,-2,-5,-1,-4,5,6,-3,2,-2,1,-3,-8,9,-8,4,5,6,-10,-6,-10,8,-8,2,4,-10,1,-3,4,1,-6,3,-5,-1,8,1,-10,-3,-2,6,-9,3,10,9,10,8,-8,-7,-10,8,-6,5,10,4,-2,-9,7,-3,10,2,5,-5,-3,-8,1,-2,-4,4,-4,7,-9,1,8,4,7,7,-8,-6,5,3,-9,2,1,-9,-4,-2,-3,-8,6,-1,8,4,-2,-6,-4,2,5,7,2,2,2,-9,-7,-8,-9,-8,6,-2,4,-5,8,-2,-1,-10,4,-9,5,1,-2,-9,-7,7,-10,-2,-6,5,-2,6,7,-8,-5,-7,-2,-6,-7,-5,-1,8,1,10,-6,-1,3,4,3,-10,9,-1,-6,-5,-2,-7,-5,6,4,-5,-10,-9,-6,-4,-6,-9,10,6,-7,-8,3,1,10,-8,-1,5,3,-6,-10,10,-5,-1,-9,10,9,-4,-5,4,2,2,-9,7,-2,1,-5,9,9,6,8,1,-6,-2,2,8,10,-7,6,8,-1,1,-1,-10,2,-6,2,10,4,10,-7,-10,-8,-5,5,2,6,3,-6,6,9,-8,1,8,9,-1,-8,-5,-10,-9,-8,10,-8,9,-8,-10,7,7,-8], dtype = "int64")#candidate|8287|(312,)|const|int64
call_8284 = relay.TupleGetItem(func_6176_call(relay.reshape(const_8285.astype('uint32'), []), relay.reshape(const_8286.astype('uint32'), [66,]), relay.reshape(const_8287.astype('int64'), [156, 2]), ), 4)
call_8288 = relay.TupleGetItem(func_6181_call(relay.reshape(const_8285.astype('uint32'), []), relay.reshape(const_8286.astype('uint32'), [66,]), relay.reshape(const_8287.astype('int64'), [156, 2]), ), 4)
output = relay.Tuple([call_8278,call_8284,const_8285,const_8286,const_8287,])
output2 = relay.Tuple([call_8279,call_8288,const_8285,const_8286,const_8287,])
func_8289 = relay.Function([], output)
mod['func_8289'] = func_8289
mod = relay.transform.InferType()(mod)
output = func_8289()
func_8290 = relay.Function([], output)
mutated_mod['func_8290'] = func_8290
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8312 = relay.var("var_8312", dtype = "float64", shape = (10, 1, 12))#candidate|8312|(10, 1, 12)|var|float64
uop_8313 = relay.log(var_8312.astype('float64')) # shape=(10, 1, 12)
func_6008_call = mod.get_global_var('func_6008')
func_6010_call = mutated_mod.get_global_var('func_6010')
const_8328 = relay.const([-4,-3,3,-3,5,-5,-7,-6,2,8,-10,-1,1,-4,7,-1,8,5,6,-2,-3,5,5,4,-9,5,7,4,5,9,5,2,-6,7,-6,-10,-7,-9,-6,10,-7,7,-2,2,-6,9,2,7,10,-7,-2,-5,6,3,-9,9,9,10,4,-9,4,4,-1,4,-4,10,-2,6,1,9,-2,7,-4,-3,2,3,-9,-4,9,-4,8,10,8,-7,-7,10,5,-1,6,-9,5,6,8,-6,7,1,-3,7,-9,2,-1,5,2,4,1,8,-7,2,4,4,8,-9,6,-4,-8,-3,1,-4,-6,-10,-4,-3,-3,-6,-2,10], dtype = "uint32")#candidate|8328|(126,)|const|uint32
call_8327 = relay.TupleGetItem(func_6008_call(relay.reshape(const_8328.astype('uint32'), [126, 1])), 0)
call_8329 = relay.TupleGetItem(func_6010_call(relay.reshape(const_8328.astype('uint32'), [126, 1])), 0)
output = relay.Tuple([uop_8313,call_8327,const_8328,])
output2 = relay.Tuple([uop_8313,call_8329,const_8328,])
func_8333 = relay.Function([var_8312,], output)
mod['func_8333'] = func_8333
mod = relay.transform.InferType()(mod)
mutated_mod['func_8333'] = func_8333
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8334 = relay.var("var_8334", dtype = "float64", shape = (10, 1, 12))#candidate|8334|(10, 1, 12)|var|float64
func_8333_call = mutated_mod.get_global_var('func_8333')
call_8335 = func_8333_call(var_8334)
output = call_8335
func_8336 = relay.Function([var_8334], output)
mutated_mod['func_8336'] = func_8336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6295_call = mod.get_global_var('func_6295')
func_6296_call = mutated_mod.get_global_var('func_6296')
call_8341 = relay.TupleGetItem(func_6295_call(), 0)
call_8342 = relay.TupleGetItem(func_6296_call(), 0)
var_8350 = relay.var("var_8350", dtype = "float64", shape = (15, 2, 13))#candidate|8350|(15, 2, 13)|var|float64
bop_8351 = relay.greater(call_8341.astype('bool'), relay.reshape(var_8350.astype('bool'), relay.shape_of(call_8341))) # shape=(15, 2, 13)
bop_8354 = relay.greater(call_8342.astype('bool'), relay.reshape(var_8350.astype('bool'), relay.shape_of(call_8342))) # shape=(15, 2, 13)
output = relay.Tuple([bop_8351,])
output2 = relay.Tuple([bop_8354,])
func_8359 = relay.Function([var_8350,], output)
mod['func_8359'] = func_8359
mod = relay.transform.InferType()(mod)
var_8360 = relay.var("var_8360", dtype = "float64", shape = (15, 2, 13))#candidate|8360|(15, 2, 13)|var|float64
output = func_8359(var_8360)
func_8361 = relay.Function([var_8360], output)
mutated_mod['func_8361'] = func_8361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6855_call = mod.get_global_var('func_6855')
func_6857_call = mutated_mod.get_global_var('func_6857')
call_8413 = func_6855_call()
call_8414 = func_6855_call()
func_5153_call = mod.get_global_var('func_5153')
func_5155_call = mutated_mod.get_global_var('func_5155')
var_8420 = relay.var("var_8420", dtype = "float64", shape = (24,))#candidate|8420|(24,)|var|float64
call_8419 = func_5153_call(relay.reshape(var_8420.astype('float64'), [1, 2, 12]))
call_8421 = func_5153_call(relay.reshape(var_8420.astype('float64'), [1, 2, 12]))
func_6622_call = mod.get_global_var('func_6622')
func_6625_call = mutated_mod.get_global_var('func_6625')
const_8428 = relay.const([2.253991,-9.908071,4.345549,8.478695,1.828138,-4.300402,-9.350338,-7.853329,-3.349691,-3.164817,2.335027,-3.408687,1.702855,-4.028694,8.218417,-7.590099,-7.592022,3.340656,-9.496641,2.596477,-8.854272,2.917444,5.518574,1.369832,-5.720438,-3.362410,-2.711801,-5.861896,1.514053,-9.383778,-9.783377,-9.158267,-7.632937,-3.374294,-9.743697,-7.036201,9.286156,6.516397,1.424794,-0.935693,-3.158705,5.106162,4.840999,-4.331048,2.084084,5.588592,8.111201,-5.145218,-3.340845,7.691960,7.482482,5.317286,8.006739,6.891008,7.677545,-7.611543,-6.193169,-8.460416,9.745192,-8.661151,2.004864,-6.420413,3.102867,-6.440608,3.706613,-8.497926,6.920807,-3.696358,9.168632,0.587434,2.217849,-8.382979,-5.271422,-3.583898,-6.061471,-6.015523,-0.756135,-4.220809,0.056918,0.912615,-0.711897,9.694244,1.472422,-0.451728,3.544487,3.357949,3.440698,-0.577592,-9.431244,-8.813172,-5.320447,9.997945,9.712971,-9.978859,-9.244309,-1.064815,-9.197717,4.383132,3.240640,-3.347317,7.915703,5.534377,2.082637,-4.590448,-7.591935,-9.056780,5.724405,-6.747965,-1.042910,-2.706816,-2.549154,6.624601,-8.605327,6.640116,2.137650,5.605766,4.582901,8.297136,-2.343584,6.885134,-1.052071,0.402724,5.415210,2.513449,9.707773,-1.989300,-1.385527,-0.198305,-3.493560,-6.088974,3.856027,3.396639,-2.087943,8.379449,-3.208224,-5.026442,8.136863,6.238458,2.567387,-9.524507,-8.821749,-7.897331,-7.095641,2.179532,-5.000452,-7.497993,7.565637,6.818801,2.720935,4.219781,3.097406,-9.798581,9.540462,2.625617,-1.201995,5.307053,-6.614042,4.889501,-5.897585,-4.942409,-3.387231,-7.310798,-8.054771,-6.942827,7.770734,0.758034,2.713851,4.224987,9.105188,5.473408,-3.507340,-6.291295,-7.040648,5.662566,2.313831,-9.868409,3.862896,9.837709,-9.369052,9.849797,9.952605,-2.728924,-2.977406,-7.417529,-7.581111,-1.635620,-2.335423,6.946093,-5.019060,-2.139997,-6.624264,-0.018513,2.746161,9.463031,9.488475,4.910481,-4.183884,6.678887,4.634541,-4.419296,2.706534,-3.650457,-2.893906,-5.182470,2.414474,-4.301645,4.722066,3.822835,-8.917113,-9.583214,0.959867,2.699813,4.441140,-8.975334,-6.199734,-5.248583,8.362460,9.287101,6.734557,1.294289,-3.516163,-7.993467,-0.415362,6.667606,2.708932,-9.245568,5.159876,-2.038614,-1.932013,-6.287287,2.325960,-9.551738,3.008679,-6.773316,8.956463,8.163826,2.223561,-8.912645,8.067130,8.587924,6.482061,6.482479,3.323531,-9.341619,4.422445,-1.893623,3.276101,7.259193,-3.131478,1.618324,2.272482,-0.673226,3.654232,-7.818736,-5.419566,3.786091,6.057795,-6.906920,-7.281943,-6.366866,6.102633,-4.325320,3.623810,-9.672805,-6.509177,-7.253758,-2.609426,-2.318672,8.874200,9.045715,-3.711876,8.877182,2.936039,-3.534156,-7.688463,4.956922,2.608675,7.098522,-3.286494,2.197917,6.547448,-0.498242,-4.040268,2.781655,-9.852215,6.134868,8.194755,-4.382688,-7.663291,-9.595249,-8.582751,9.460406,-6.859946,-2.434297,-8.707265,6.503209,9.389142,5.544472,-2.097885,2.334810,7.889275,-9.058506,-1.431796,-7.330028,2.934014,6.098397,-1.916816,-4.332153,4.849103,6.089866,-6.233541,-9.180630,7.034793,2.439590,-2.493888,-8.223303,8.614373,6.501634,6.714216,-1.574007,-1.934011,-4.502042,-8.521833,0.131812,-7.017708,6.168810,2.456448,-6.420405,-7.921626,2.771625,0.289571,-6.217508,-1.311526,-9.305280,3.025995,-1.739277,-2.300988,3.982353,6.864078,0.180841,8.194354,-2.541095,-2.805615,9.945863,-2.790718,9.943762,-3.455227,-7.348524,8.615731,4.130047,-2.990970,6.618893,-3.364998,8.552097,5.219461,8.693288,-6.015308,-9.263470,7.841976,2.104793,-5.949214,6.743760,-8.370055,3.681728,-9.854907,8.611283,-4.722008,9.636094,1.224551,1.588638,8.076971,5.908328,-1.730635,-0.740691,-5.011413,-1.924993,4.604483,2.030055,0.432269,0.923423,8.280443,-5.717389,0.448723,8.724338,4.327501,-6.762324,1.108951,-5.882062,3.975716,0.255863,-1.474201,-0.608780,5.781567,2.182415,-2.315772,-2.776714,6.478520,8.755217,8.059123,6.591801,1.423745,4.863474,-5.334991,6.558563,3.280800,1.995434,-6.068727,8.365689,4.788048,-8.194019,5.435192,-1.763165,-1.350610,-6.886173,-2.375945,-8.587637,8.316448,-1.851687,8.188634,9.407836,4.894302,-8.460347,-9.124262,4.532685,-1.939636,9.934105,2.816423,0.735588,3.479620,3.005770,8.881614,-1.535825,7.768662,-6.227125,-9.157964,0.822536,-3.437706,6.777534,8.022951,4.460549,-4.350482,-0.407531,-6.602436,6.214513,4.901299,7.380923,-6.779972,5.797229,-3.054752,-7.542481,1.766335,-5.443234,7.076562,-2.031679,3.637709,3.125267,-3.835399,9.070278,4.392433,-2.933295,3.333891,2.054573,8.997878,4.293621,1.955762,-4.285408,-4.585738,-5.861960,-7.827993,-8.232469,-7.255837,-5.369293,8.168630,4.021784,-6.287816,4.259486,8.143835,-0.639571,3.996053,2.875513,0.503697,1.697840,-6.632532,-1.876081,-6.204390,-1.534790,-8.350690,8.264470,-9.282911,-5.784186,1.925624,-9.447803,-4.272144,6.403852,6.296844,-5.180882,3.176744,-6.333443,-9.672188,-5.002584,3.202853,5.373341,9.589404,-8.507653,-6.738083,1.589346,-6.955989,-3.405687,-1.938089,5.506116,-0.316805,-4.254284,0.088940,-2.169344,6.007294,9.835956,8.735444,-2.760040,1.984822,0.274375,5.440638,7.532412,-3.155171,3.478285,-4.384485,-5.271149,-9.617274,-3.190211,9.972443,1.187772,0.844727,-4.039990,-2.132369,-4.655728,5.577240,8.974505,-1.335365,-7.579659,-7.867760,8.841731,-3.478963,-9.473045,-5.814848,9.172743,8.367950,9.648399,7.562208,5.503469,-8.149359,7.001283,2.857922,5.622443,-0.860649,0.154775,1.123269,5.238349,-0.612501,-3.716035,-7.524948,1.607811,6.893673,-0.695795,-4.041598,-7.954706,6.422866,-6.065500,-9.620179,-1.848298,9.296217,7.399441,-9.855100,5.644441,-8.352091,-2.521350,5.309974,-6.325887,-0.140361,1.382994,5.425949,6.256680,8.671900,1.444576,2.073371,-5.000928,1.706239,2.441776,-6.316585,4.594773,7.191829,4.915938,9.681877,6.280067,1.883499,-9.421255,-3.602193,0.316930,1.227982,6.146719,4.282668,8.307948,5.360210,-0.474256,6.510891,2.884410,1.529869,9.352330,-7.946194,-8.932939,4.726553,-8.309723,4.300784,-7.037510,6.456367,7.984830,5.104233,6.762114,-9.085977,4.806128,7.515741,-9.679309,2.968950,6.060279,-9.392350,9.108286,-0.258250,5.665626,-7.343873,-4.804615,9.705958,-5.684319,0.700394,7.825067,6.169289,7.616770,8.444739,-2.701275,-6.034936,9.783248,6.048026,-1.983109,-9.631531,9.694910,8.027638,-3.468413,-9.464160,-8.151908,6.217529,4.328600,-9.818145,7.763528,-1.690424,-4.363698,-0.263321,0.356150,2.816760,8.796071,0.973557,-0.200781,7.891526,3.908533,8.025749,9.639034,6.171454,5.435588,9.865818,-7.313314,-3.581806,-4.383795,-7.313966,5.555625,-9.541078,0.675745,8.515847,-7.495791,2.942259,-2.446562,8.461397,8.738716,-8.532744,-5.679812,8.792595,4.684773,-1.294521,-2.267150,5.240864,-1.767156,6.159788,5.040663,1.660317,6.532213,2.699580,2.716643,6.533601,-1.694596,3.359005,0.103575,7.364610,8.377254,2.898400,-6.166289,3.703203,-9.294859,-8.478948,0.144254,4.707810,-7.987600,6.638680,-7.427443,-9.202943,-3.646274,9.972535,4.665711,6.508658,-3.120848,-4.032251,0.914418,1.392828,-5.637488,-8.189774,9.084428,-8.008417,-6.123768,6.499663,-8.372339,8.798410,-2.785688,3.572644,0.554115,-4.453586,5.804799,-8.974746,-0.685443,-6.250496,-4.855399,-5.634182,-5.528889,3.216495,-3.635049,2.445872,7.028010,-1.882120,-9.359839,9.278396,-7.793042,2.724076,-3.017878,-0.429876,-8.964084,-1.129006,6.601922,-5.220740,5.555073,7.034813,7.352648,7.350216,1.411867,-1.131393,3.947925,-7.679217,5.099844,5.874753,2.763864,-4.041432,-1.541594,-4.069013,4.415392,2.065560,1.008657,0.081288,-4.428038,9.107683,-5.300236,8.680596,8.063793,2.570339,1.545815,-7.498504,-9.488290,-9.869734,2.053595,9.854752,-5.886703,-2.079863,2.234287,-1.146840,-2.631793,0.917452,5.318497,-8.469191,-3.948387,7.498808,-7.579579,4.838837,-6.257608,2.950163,-1.051382,-7.302952,2.037721,-2.363812,-7.029292,-1.019502,-1.209969,1.537905,-1.330514,-9.339970,1.427805,0.615008,-8.453537,6.597604,-5.660568,-6.682319,8.690995,1.695694,0.341403,3.718721,-5.764270,-5.738459,9.404863,-3.209147,2.323571,0.700551,-9.598507,-8.231358,7.022076,3.246157,-3.162071,-6.751189,4.373049,0.448869,-1.970311,-8.567067,-3.360667,3.778001,8.961419,-1.701995,3.843198,9.094083,-1.109002,-0.834456,2.481680,2.788481,2.062736,0.543469,-1.693449,-7.645824,6.423556,5.022377,0.083236,-5.003847,1.889987,-3.931395,-1.658781,-3.050761,0.198768,-9.171352,9.017553,1.683416,4.497458,6.864999,8.329260,-4.049344,-2.858611,-3.795361,5.620080,-6.788643,3.237316,7.912971,6.329006,-8.735395,-4.172775,5.591045,6.696439,-6.692366,-6.080664,-3.043435,2.479189,-1.687521,-1.502527,-3.544258,3.911912,-9.211870,8.210055,-5.027030,-8.097426,2.612551,7.822956,-5.482391,3.117677,-9.052775,-2.544378,5.135692,1.043589,0.257756,1.930702,7.595716,5.364708,6.037089,3.947574,2.368298,3.884758,-3.846000,5.455757,8.632292,-2.087875,-2.277282,-5.124428,-5.372079,-0.245823,9.445989,5.933388,-0.775113,0.648977,2.674194,-9.593680,-8.384992,-7.592406,-6.331814,4.930548,-9.417759,3.599719,-5.862872,6.676149,-8.900152,-3.819661,5.569949,-1.985439,-6.891698,6.077893,7.817201,-8.456140,1.416272,-4.583746,7.042973,6.637220,9.169475,-7.901599,-9.989093,8.380752,6.996277,3.185614,2.985837,7.163365,6.908717,-4.771048,-6.041864,-1.598029,3.762811,0.998180,-7.893881,-8.813446,-2.187038,1.315563,-0.133549,3.961331,-4.172196,-3.934992,-6.200958,-3.036068,6.735600,-4.772607,2.775923,2.895626,-3.922559,7.576076,-3.469987,-4.249220,6.454892,0.121989,-0.972488,7.696678,7.626667,8.374567,8.240299,7.269556,-5.802041,-7.173052,-1.255008,-0.397723,3.224968,8.339023,4.288334,-4.335285,0.837001,2.407001,-4.620301,1.560604,-2.181721,5.982244,-2.535770,-7.726036,1.495479,-5.394342,8.113523,-2.874190,3.364171,-1.119376,0.725904,6.071278,-3.313682,4.158837,4.098090,7.870959,4.207166,-7.713075,0.156550,-3.201877,8.461013,6.104357,6.421000,7.409791,4.796156,2.975121,-9.284065,-7.905697,8.319677,9.494890,-9.999465,8.260648,-1.075054,0.528433,-2.330401,-6.024690,-9.252147,-3.386107,3.158558,-5.211545,3.925377,4.181749,-4.799855,1.822312,5.355498,0.164903,6.281897,6.111184,-6.169605,3.878580,-5.550078,-2.568800,4.236184,-0.483109,4.503617,-6.130999,7.482940,-1.937635,7.463988,2.389578,4.084047,-9.236350,4.735247,-0.824128,-5.090810,0.208387,5.626762,2.630921,-4.916449,2.640222,2.346971,3.135059,0.754525,-0.658550,2.040621,-9.933860,-7.360345,5.388516,-6.287231,4.360692,4.169931,-5.994356,0.368843,-5.906481,2.199626,4.097433,1.291903,6.520697,-0.618670,6.803321,-6.574198,-2.920288,-2.319672,-5.546326,5.055182,0.085682,-2.720983,0.914278,1.208181,-4.455659,2.313730,0.227038,-6.787722,-0.132041,9.502346,-1.618204,6.307513,-5.367209,-7.613552,-7.890051,2.994535,-5.256006,9.692585,3.646592,3.527757,-7.781828,4.582964,0.891746,-2.110667,-3.465667,8.192387,0.235997,-1.221800,-2.606047,2.322400,-4.170187,-5.466850,-2.675441,8.498854,9.705641,9.205448,4.226970,1.782196,-2.611427,-5.592889,2.980321,7.118538,-6.524299,4.162139,-0.106033,-6.516033,9.174199,-6.272911,-2.039559,1.679166,-3.969531,0.043296,0.092362,9.611225,2.888868,-7.186203,1.581818,4.332675,8.074062,4.256104,3.435661,6.561282,-6.640556,3.446833,8.588004,-9.960211,8.291232,7.688597,0.411995,1.710639,9.023721,5.246645,5.796700,-5.417609,2.807613,1.834258,3.080039,1.172542,-3.824427,5.501615,6.188327,3.092274,4.201522,7.539592,5.964325,2.542622,3.595100,-6.440158,-6.516355,1.694021,-6.296488,-6.414335,3.518805,9.970762,-3.087066,9.429437,4.409610,8.305808,-6.970222,5.142969,3.763985,-5.298945,4.543873,9.548810,1.290844,-0.307729,0.614697,-4.591251,-0.619057,-7.087954,-2.216624,6.727003,9.287370,-0.719783,4.738233,9.942996,3.655917,7.003344,-0.374133,-3.737950,-0.527939,1.941144,9.960976,-4.468066,-6.216130,5.076159,0.636487,-0.641285,2.338621,-5.705435,-0.890124,0.908105,7.075609,-2.849408,4.194239,5.267117,7.878430,-7.429047,-2.559689,4.966425,3.384304,3.794279,6.003967,1.809357,1.490211,8.513102,-9.141463,8.926959,-7.717021,4.777418,-1.409522,4.809581,-6.787289,-1.860361,-9.237986,8.079750,-0.951612,-5.688440,-6.725028,-9.709738,9.259606,8.667375,-1.533085,3.919970,-2.896600,8.836769,-4.231034,1.082171,-0.368799,5.352973,9.939141,-2.861551,-6.206911,7.492682,1.615073,-7.785138,6.298200,-2.432245,-7.264470,-3.261863,-9.823597,4.093345,-9.926553,4.747381,-8.702457,-7.436397,1.389453,-8.073660,0.179567,-1.691148,5.080528,-8.857872,-4.925845,1.009262,-4.214345,-8.392772,3.978469,8.214330,-7.152564,-3.767243,-8.721431,-8.264966,2.262829,9.500820,-4.890316,7.001787,-7.209456,-5.408152,-8.676060,4.601753,-2.235393,-7.434637,0.342030,2.142147,-8.860117,-9.961683,-5.916977,8.877810,9.170503,1.202461,-2.886537,-2.180599,-9.089147,-0.517394,-7.776800,3.366085,4.719010,-3.343136,-4.996618,-9.136139,7.117508,1.680161,8.465687,2.176506,7.236410,-0.593877,-9.889200,-8.281237,8.508709,2.008876,-9.264433,-0.982036,-2.085910,-6.030164,2.361841,-2.545957,1.348453,-4.049966,-9.308868,-0.280881,-1.026795,5.825952,2.926595,9.775495,-9.244279,-1.329815,-0.345097,-6.166894,2.310210,8.709592,9.112408,0.062984,6.527339,6.344822,3.400161,6.601774,-4.508242,-2.418363,-6.525493,8.035840,7.144601,9.661857,-7.550192,-2.842951,-6.215487,-9.334601,2.730890,-6.839966,-0.872984,-2.513301,2.864077,7.730584,3.378737,6.779606,-3.013417,-7.532078,-1.501128,6.478898,-1.539697,-6.012909,6.525738,-4.986975,-2.383836,3.020317,0.402754,1.247406,6.502653,-7.772234,-5.428137,-4.406532,-2.109322,-3.242264,-7.921543,-0.728024,-4.712896,3.828827,8.449892,-3.676199,-7.358593,-4.083557,-4.905325,6.579659,3.904895,-3.204349,9.088245,-4.319016,2.256864,5.092779,-6.322556,-4.462277,-5.597204,-9.262572,-0.543409,-6.798845,-5.658669,-8.357958,-6.606254,-4.509018,5.582962,1.676892,9.303850,3.759191,5.002769,-6.276624,-9.050601,-4.474123,-4.815377,-8.060453,0.050242,9.368828,-3.523324,-1.394218,0.073487,-4.307142,9.239513,-9.555576,0.502534,-6.133347,-9.875076,-8.287828,8.091492,9.045091,3.733645,-0.840219,-9.921968,-7.328856,7.752704,7.017968,3.020428,-5.872837,-4.871474,7.770246,-0.384227,-8.032388,-1.389402,7.793535,1.467941,7.882692,-9.169870,3.189466,7.951238,6.574992,9.451627,-1.327627,-3.703488,9.896035,2.623283,-1.099127,-2.857727,-0.201309,0.921698,0.039145,-0.248237,7.884450,-6.450459,-4.623783,-0.634089,8.660016,-2.396654,-5.362551,-1.715808,0.309251,-5.136200,7.836925,-7.750766,5.532742,9.208095,-4.051401,2.390085,-5.703461,0.709877,-3.224076,4.106035,3.876491,1.790471,-0.797184,0.416121,4.477934,-0.077067,7.553281,-0.638351,-5.259449,6.621690,6.519667,2.442444,-7.501800,-1.725116,-0.663506,-8.788555], dtype = "float64")#candidate|8428|(1500,)|const|float64
var_8429 = relay.var("var_8429", dtype = "int64", shape = (6, 52))#candidate|8429|(6, 52)|var|int64
call_8427 = relay.TupleGetItem(func_6622_call(relay.reshape(const_8428.astype('float64'), [1500,]), relay.reshape(var_8429.astype('int64'), [312,]), ), 1)
call_8430 = relay.TupleGetItem(func_6625_call(relay.reshape(const_8428.astype('float64'), [1500,]), relay.reshape(var_8429.astype('int64'), [312,]), ), 1)
uop_8438 = relay.exp(call_8413.astype('float64')) # shape=(15, 2, 13)
uop_8440 = relay.exp(call_8414.astype('float64')) # shape=(15, 2, 13)
output = relay.Tuple([call_8419,var_8420,call_8427,const_8428,var_8429,uop_8438,])
output2 = relay.Tuple([call_8421,var_8420,call_8430,const_8428,var_8429,uop_8440,])
func_8444 = relay.Function([var_8420,var_8429,], output)
mod['func_8444'] = func_8444
mod = relay.transform.InferType()(mod)
mutated_mod['func_8444'] = func_8444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8444_call = mutated_mod.get_global_var('func_8444')
var_8446 = relay.var("var_8446", dtype = "float64", shape = (24,))#candidate|8446|(24,)|var|float64
var_8447 = relay.var("var_8447", dtype = "int64", shape = (6, 52))#candidate|8447|(6, 52)|var|int64
call_8445 = func_8444_call(var_8446,var_8447,)
output = call_8445
func_8448 = relay.Function([var_8446,var_8447,], output)
mutated_mod['func_8448'] = func_8448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8600 = relay.var("var_8600", dtype = "float64", shape = (14, 14, 9))#candidate|8600|(14, 14, 9)|var|float64
uop_8601 = relay.atan(var_8600.astype('float64')) # shape=(14, 14, 9)
uop_8603 = relay.cosh(var_8600.astype('float64')) # shape=(14, 14, 9)
output = relay.Tuple([uop_8601,uop_8603,])
output2 = relay.Tuple([uop_8601,uop_8603,])
func_8605 = relay.Function([var_8600,], output)
mod['func_8605'] = func_8605
mod = relay.transform.InferType()(mod)
var_8606 = relay.var("var_8606", dtype = "float64", shape = (14, 14, 9))#candidate|8606|(14, 14, 9)|var|float64
output = func_8605(var_8606)
func_8607 = relay.Function([var_8606], output)
mutated_mod['func_8607'] = func_8607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_8635 = relay.TupleGetItem(func_5615_call(), 0)
call_8636 = relay.TupleGetItem(func_5617_call(), 0)
func_7440_call = mod.get_global_var('func_7440')
func_7441_call = mutated_mod.get_global_var('func_7441')
call_8658 = func_7440_call()
call_8659 = func_7440_call()
func_5919_call = mod.get_global_var('func_5919')
func_5923_call = mutated_mod.get_global_var('func_5923')
const_8674 = relay.const([6.691191,-7.856758,-2.788098,-3.078314,2.377729,5.921163,1.199421,-6.352552,-9.476502,6.661519,-7.571052,-7.275850,9.661300,-5.698820,-0.356798,0.898512,2.517311,-8.091501,7.525385,-0.839220,4.066681,9.178831,-3.128703,2.289962,3.683332,0.944034,9.454799,2.395713,7.450042,6.293232,4.575697,5.367537,6.842920,-7.883777,-8.376768,3.852476,-5.232755,-5.673362,-9.624173,-8.621578,-3.769735,-5.605854,5.826520,-3.977725,0.673486,1.077607,0.825636,-3.569094,-7.040818,4.495643,5.462043,-0.632994,3.541766,-9.629945,-9.082616,5.321011,1.697338,6.532069,3.030213,4.319794,8.732836,2.195767,9.422838,1.383509,-4.938393,-5.169927,-7.367863,-9.117328,-3.730350,1.143503,6.248833,4.763725,-1.312369,7.880352,6.031506,0.667220,4.027069,4.593007,-5.150347,-2.761639,4.516969,-9.413667,-3.936898,0.814631,-8.733261,4.720895,-9.780528,-3.005477,3.886382,-4.748481,-2.562176,-3.709149,5.935641,-9.427159,-2.376090,-7.129480,7.167602,8.477486,9.494034,-2.876967,-5.876493,6.845209,6.775715,5.964637,-9.490109,3.060018,5.002506,-6.049195,7.318442,-4.053270,-0.797378,2.211276,-4.095460,4.473366,4.115959,9.980729,7.396957,-7.229512,-4.890144,-0.174302,-1.383857,9.148458,9.657351,-2.058542,-5.714180,-2.079793,9.421067,-4.987051,8.389604,-4.909310,-3.256638,-1.480287,-4.981810,-3.460767,-2.045886,5.294597,-0.039751,3.341761,2.194655,-4.282682,-0.691283,-7.584911,-7.028515,9.078563,-0.389885,-2.556738,9.271525,-7.734199,-6.194674,-9.964701,6.771701,3.819026,-5.323329,7.632826,-4.835760,0.126133,8.117522,-3.675708,1.733538,5.218388,7.692807,-4.629498,-2.044195,8.057210,5.789890,6.763223,8.712773,-1.749690,9.313516,8.877780,2.688724,2.586674,-9.484991,-1.448707,8.882896,4.225252,8.506706,-8.511399,0.446602,-2.339967,9.538644,8.375777,-8.553712,4.561337,-2.542557,6.738287,3.200151,-8.978969,3.027107,4.428538,-1.507760,9.518374,-7.357511,3.421499,2.851457,-5.384619,4.180641,-4.159422,3.422011,-5.488710,-4.536668,0.358314,-9.664829,-0.904888,-2.567281,-9.108707,-8.205275,3.326952,4.826454,-2.835862,-0.285175,-6.138875,2.944444,-5.183158,-5.847400,-7.522749,-2.194224,-3.597679,9.106542,-1.376136,4.115400,-3.388637,3.687403,-5.181535,-3.240695,5.305372,-9.951849,-6.935855,-0.535114,-8.833489,5.883084,-3.314764,7.057619,-6.526402,8.034153,-4.004027,-8.750877,-3.454735,-1.398952,-0.099775,-5.693198,-0.706848,6.990735,-2.129106,4.816143,-2.877537,9.031214,-6.680914,-6.379375,3.046194,-5.507194,-6.181073,-8.924128,-0.929459,4.269891,4.750222,-6.992272,-9.688950,-7.002580,-5.383919,-4.363817,1.915462,9.245703,-2.308115,-0.815552,0.629726,3.921901,8.996668,-9.192621,2.470040,2.379103,4.765422,-8.992654,9.101836,-9.734890,-3.560279,9.731108,-0.528638,0.506320,-1.378932,-6.756072,-7.721721,8.730059,7.072096,2.602571,0.726486,0.431981,5.590416,1.420369,3.777357,-8.861384,-4.873534,6.130287,-5.365299,5.494626,-7.814123,-9.576788,0.152511,0.023695,1.977431,7.659202,1.166460,-4.534572,-4.418839,1.474719,8.613953,6.149436,2.822300,3.909824,-3.213751,-6.148070,-9.206266,6.243887,-8.608456,5.615416,-4.235096,2.497218,2.873913,-9.193462,8.702021,2.114859,9.711337,-8.475761,5.376602,-9.786229,-2.065007,1.867246,2.849520,-4.842015,3.158557,4.140116,4.252163,5.332051,-0.700323,-4.560402,4.922636,2.185735,7.607591,-7.291268,7.977692,-6.671717,1.685360,-1.525555,-7.817897,9.200963,-7.974110,7.759804,4.872227,4.787509,-4.491040,9.232639,4.991882,-8.554938,-8.830970,-1.251827,1.461115,5.398417,-5.409972,6.248650,-0.448875,-0.966055,-4.117032,-4.696391,-5.262163,5.939766,-2.399855,-4.877905,6.022876,-2.981712,8.338575,2.929169,2.407648,-8.646122,1.720131,-0.030154,-9.688534,-1.211447,0.810613,-3.949076,-0.315742,-9.996000,-0.158334,4.648668,-8.726158,7.748674,-4.401891,-3.626618,9.864904,7.042596,1.831595,-2.658031,-3.880648,-3.077068,-6.262333,5.584476,-0.667558,2.446391,-8.395835,2.316885,-1.582573,1.748029,0.578189,-5.790794,-9.691448,5.924395,3.991852,9.664841,0.256156,9.306797,-6.290968,-6.751019,4.814777,2.887666,-9.418605,-3.434363,1.468976,8.474531,1.462307,6.629172,3.852342,5.559552,-4.766365,-8.154652,-0.364066,3.787831,-8.778362,-2.877042,6.551685,-8.938732,-9.996793,-7.451996,-5.887128,-7.518209,8.126921,9.457019,4.291124,-4.341410,1.938425,1.200459,-8.702639,-6.459598,-6.077387,-3.033578,-1.824697,-2.199426,6.343973,-9.974907,-1.770795,-3.507369,-3.259542,0.515535,-4.203341,6.843015,-0.718169,-9.969219,-8.009235,-6.212501,0.896749,-2.342916,3.149519,-3.507846,-5.233511,-8.023538,4.633619,-8.987081,-7.363719,0.976824,0.001198,-5.861070,9.843638,5.367131,2.238407,7.396708,-5.646798,-6.795784,-0.550487,1.771148,4.005526,4.246958,-3.277950,-1.570605,5.201185,0.919014,-7.716219,8.482984,-9.567854,0.262124,-6.011228,-6.063861,7.459869,-9.875548,8.844457,-5.288648,6.735983,-8.114319,3.815870,-0.881265,-0.026616,-0.118930,5.012817,8.648883,-9.585161,3.961280,9.360919,4.969414,-3.601160,-4.207978,9.712912,-0.054427,-6.114110,-2.103799,5.224844,8.041960,4.161489,-8.817987,9.264578,-9.223047,1.752741,-3.750024,-5.883711,5.227507,1.266465,-6.357836,-4.306803,4.062418,6.799619,-3.610893,-0.351185,9.862095,7.378654,-1.897992,1.611792,-8.322675,-8.441323,8.931811,8.624921,1.950126,-9.820999,0.840992,-9.219913,4.552612,4.099546,-9.544763,6.002335,4.757232,7.391345,6.187052,-0.154649,0.971123,-7.277415,0.584134,6.285724,-1.066621,1.600521,-3.449106,-6.100093,0.939969,-9.900990,0.903345,3.607959,-9.156051,-2.805372,0.607313,-8.821271,8.600695,3.586436,-6.452612,8.366301,-0.305701,-5.006568,-8.015137,4.510512,-0.788919,6.522173,7.332473,-0.835726,-5.214011,-8.230174,-1.602752,-7.925523,4.721807,-7.750759,4.579865,8.262142,-2.998577,-0.413148,-2.278588,3.199406,1.690648,8.042733,1.815939,4.980485,-2.044629,-5.461555,-2.697940,1.069911,-0.753250,2.054569,6.420134,-3.206594,-5.654620,6.609289,-1.046079,-2.489004,5.840187,-1.132003,5.063259,-1.075747,8.892169,-1.778589,-8.438369,-8.113520,-2.354877,-5.517910,-2.190933,4.188313,9.431195,4.647472,1.543932,-2.563839,3.846920,-6.407240,-5.196274,1.898175,4.866315,1.234497,8.801827,-4.970024,7.046973,8.722250,8.710922,-5.547444,9.693071,-5.458567,3.291766,-1.361164,-5.152009,-4.887968,3.498895,-6.645464,7.148642,-5.963395,6.147243,-0.888983,7.087499,-2.263958,7.502487,-2.060902,9.983061,6.350631,0.133471,8.455579,-1.474740,-2.459529,9.452912,-1.330969,-6.009078,0.690753,-4.889749,-1.289445,-9.422058,-9.891230,4.932196,-2.091700,-8.970230,-8.038578,2.524904,8.228269,2.238008,-1.461910,-0.528982,0.052614,3.103934,3.823420,0.893656,-0.401016,-1.679751,3.140981,1.894880,-4.767135,6.030991,7.388566,4.399724,7.383802,-3.845146,6.507910,-5.939062,1.573271,-3.138120,4.108690,-8.424150,8.487673,3.164854,-7.876211,-4.746980,-9.175001,5.566303,5.509741,-1.430746,6.694816,-8.745934,9.489234,-3.122137,-7.040391,8.464837,-0.412277,0.283340,9.265514,-6.418644,5.485661,-1.730178,-6.147165,5.420256,-7.814765,-1.440289,-0.227835,2.398664,-1.699084,-6.981199,-3.586398,-9.790423,1.771608,-9.778711,-6.481105,4.805742,1.186282,5.189083,7.077234,7.351118,-0.688183,-0.597560,-8.677569,0.583475,8.139610,-4.651536,8.171428,-8.787905,-1.943788,0.686350,9.661866,2.894934,0.704101,-4.273806,1.410174,-4.072782,-6.145528,7.957308,-6.861499,1.770213,-6.573828,0.686430,-3.172966,5.532236,-4.227791,-1.727975,0.932752,3.368645,-8.944884,4.462320,8.893486,-4.530501,-4.686376,9.269564,-5.783532,-1.058156,-4.060243,-7.272808,2.144099,9.163622,9.661854,1.532083,2.380564,6.508215,1.843714,-4.048017,-5.249023,-3.093209,-7.992841,-2.436916,-8.610087,1.173826,-4.964265,8.852873,7.263751,-1.732254,-7.967744,0.898395,-3.722751,-3.108336,-8.034832,-7.292028,2.854665,9.614276,-3.181279,-7.246612,1.773479,4.465106,5.819528,3.529671,-9.521545,9.272527,-7.101467,-0.830496,4.679972,-0.585724,7.350377,5.476849,5.057968,-1.607703,-1.786975,-2.467269,1.772110,5.214890,-3.382625,6.658256,-9.858901,-1.495632,-7.339708,3.345754,4.984847,8.828830,8.673082,8.166498,2.740449,-4.095171,-9.389069,0.901363,3.479459,-4.262168,-6.729858,-4.162884,6.948939,3.314307,1.815716,0.370111,-8.466049,-3.084201,1.549592,-4.258017,9.107271,-5.830909,7.605590,6.752140,3.926750,-2.223093,-4.365219,-8.586553,2.422297,2.786685,4.438665,2.414625,7.251529,2.287722,0.921830,2.248814,-1.200473,-2.901079,-6.087291,-8.385947,-6.448417,7.731498,1.376277,-8.990691,0.710173,-2.187352,-0.816967,-0.444571,4.227834,6.375364,3.154395,0.592034,-0.964582,9.004949,-0.905984,-0.590453,-7.407282,8.812132,-3.451196,6.635333,0.324361,-8.096193,3.897444,0.591259,-3.639947,-8.097992,4.992808,1.145414,8.868753,-5.697997,1.864384,-1.681040,-3.835876,5.532234,4.064342,-1.621419,-5.671117,3.164946,7.025002,-8.567160,1.643459], dtype = "float32")#candidate|8674|(900,)|const|float32
const_8675 = relay.const([4.120774,-9.517922,-8.077029,5.758656,-5.424246,8.522268,1.207781,-9.206617,-1.490675,9.058898,-4.978757,0.890168,-0.215766,-1.541477,2.744142,1.551380,-0.001390,4.615707,-7.641299,6.312549,-8.310543,9.554047,1.395801,6.651103,1.370975,3.066568,8.095463,0.934018,-6.531933,4.508723,-1.143823,-9.292239,-4.075356,0.222518,-0.270196,1.114459,0.656328,-6.308274,-4.760133,-2.701740,2.729581,1.499105,-0.858330,-1.680446,-8.576206,2.513768,-1.492755,2.361275,6.210427,-8.225425,-5.082968,-6.389996,-5.389018,-6.378677,0.352247,-8.221545,-2.744102,6.241075,-0.878769,7.168790,9.117395,0.887628,6.569283,-6.659091,-9.029694,-0.508995,-8.031074,-7.788958,-6.403557,2.688932,-5.492486,-4.102844,8.970900,7.442783,0.372295,-4.765675,3.359144,2.490772,0.186985,-9.794511,-1.791579,-5.749823,0.430105,9.830220,2.125978,9.263795,-8.075785,-2.312072,4.184071,5.575201,9.158350,4.444472,9.498556,2.512994,-3.677503,-9.213379,-5.238866,2.615798,-4.673484,2.870640,6.755604,7.315304,-0.362400,8.240349,5.018644,8.494224,4.097373,-0.089187,6.821569,2.987628,9.767764,-3.354510,-1.086351,7.643516,-6.218124,-9.603945,-8.584925,3.362764,7.223235,-8.090652,4.217876,4.481991,6.406140,6.440334,7.133914,-9.590353,4.332739,6.864152,8.852772,-2.370315,7.481391,2.503491,-7.392776,9.761927,-5.091224,-2.280791,3.068947,-9.417112,6.712987,0.574454,-7.209709,3.510763,-6.485163,3.950296,-8.347546,7.178253,-0.177341,5.568929,3.968183,-9.709673,-3.264175,7.949165,6.365537,-0.181953,5.538199,1.306543,-8.982068,0.220112,8.161086,-0.547992,-7.724695,-9.500845,-1.754125,3.732721,-4.562441,4.636615,3.651566,-6.441720,-7.481981,0.423709,-5.359120,6.471999,-1.473374,6.266233,7.951661,6.186238,4.359526,-9.119398,4.512018,2.566560,-6.893679,-5.762893,6.244571,-8.257254,-8.853367,4.069046,-0.665552,7.648770,-7.466766,3.332363,-5.471789,0.878467,-1.498955,1.090962,-0.131049,6.938727,-4.373831,-5.359853,-7.877126,8.271646,-8.260545,8.387462,-1.132901,8.302047,6.656068,-3.635371,6.353934,8.077405,-0.975280,7.298288,0.383487,7.387112,4.920723,8.323379,-3.923030,-0.879437,5.303994,0.032553,-6.889284,-4.835564,2.062890,6.321863,6.091144,-6.760750,0.557032,-1.777781,-6.596721,-6.497186,4.998181,4.870003,4.490013,-8.355377,3.507027,-9.467106,3.226229,1.984511,3.380523,4.405301,9.928438,-9.008461,-4.288565,0.817144,-6.807311,-3.564034,2.301449,4.322546,9.488486,-6.294022,-9.810818,-7.578744,2.844617,-8.303927,-6.139375,8.115616,-4.631294,-2.295386,-5.480252,0.080857,-4.981598,-1.111796,-9.615326,-2.429959,-4.131817,-8.659991,0.340160,-5.100817,7.751992,6.263105,-3.259015,6.385148,0.748409,4.416450,-6.579639,-0.962492,-8.278654,-8.249524,0.862364,-7.895057,9.033491,-0.582852,0.629939,-5.000124,0.289194,-7.244725,-4.264695,-6.938952,-0.154359,-2.576494,6.702242,3.138185,3.453729,-2.863599,-0.651394,-4.735416,5.866901,-3.201248,0.002149,1.934013,-2.252751,0.408809,-2.282847,-0.109792,0.744345,5.815401,-8.777955,5.584468,-2.762399,-9.385394,-4.029238,4.189415,0.307719,1.622362,-1.758465,9.064116,-6.240293,4.947571,0.143981,3.409175,-3.255574,6.580735,6.868702,5.024813,-7.414075,-7.207812,-4.869120,-2.556303,2.248024,0.216359,7.088141,8.617275,7.033737,-7.839454,-0.620519,9.512328,-7.847252,7.995889,8.471597,7.951306,-7.219532,8.247350,5.780714,-5.898813,8.180726,-1.043917,3.428175,-5.086253,1.734650,3.712769,6.181075,-0.989229,5.572060,2.212862,-2.479562,-8.558498,7.836192,-1.934068,5.022020,9.792815,-6.231594,1.275390,0.550378,-0.450626,-7.622379,9.752313,-1.909971,7.515610,7.915793,2.547594,-9.612966,2.597425,5.973751,-1.586749,-2.026230,3.301338,-1.867737,-6.693706,-2.452241,-1.335239,-4.035420,-8.089399,6.847741,-0.483505,4.872978,9.631798,8.631129,5.478398,-9.550732,-2.894365,8.965120,5.439697,-3.480899,-2.155331,-0.047852,-8.683176,-8.497510,9.387043,-9.899246,-1.635991,7.551451,5.594864,-7.147517,0.724936,4.121763,-2.166473,0.719638,-8.179540,3.602351,8.734257,8.401024,5.507027,-8.037903,2.046432,-5.305829,-2.920962,9.656739,6.158778,-5.944559,-1.418872,-3.112902,8.794468,-7.563961,1.422572,-4.532478,2.266801,-9.848425,8.676858,-7.398053,-0.198442,-6.363232,-5.535814,-7.975926,-6.575597,4.294373,-2.046415,9.657294,6.563385,9.290660,6.511685,1.681557,1.016546,5.844088,9.750105,-8.005544,6.017456,-1.754974,-0.801826,3.226862,-2.538445,-3.028955,-7.921202,-8.928878,2.477754,-2.971854,6.399050,-5.747449,-7.927039,6.630250,4.503352,9.290985,-5.022244,-2.823019,-5.956453,5.250204,-8.541134,-9.077659,3.079059,2.756823,-0.964324,-0.233544,3.483003,1.444974,-1.961141,4.544110,-2.374009,-7.584424,7.203453,0.819578,-6.119715,-7.458295,-4.069132,6.574944,4.763166,3.913828,5.477001,5.795885,-5.525055,-3.780936,7.552242,-8.855409,-6.163665,-1.157351,7.317026,2.659948,3.984744,2.315923,-0.633886,6.284381,6.203329,-8.871390,-3.218203,6.540999,-2.066839,-0.882916,-4.380934,7.072268,0.899829,-4.056043,5.981660,5.014758,9.256632,3.099740,3.318560,3.494419,7.384271,4.852023,4.372740,-9.948092,-3.332470,9.103108,9.540152,9.613088,-4.026594,2.187290,-0.403269,-9.798528,5.810158,8.435751,0.727349,0.186793,-4.397442,-3.306242,-0.681388,0.110952,6.084827,8.489455,7.004105,-0.003009,-2.891463,-3.658482,-5.368225,-8.906056,-1.302004,-7.401748,-1.754320,-7.437948,6.947604,-0.702435,1.374596,-9.260807,-9.823950,2.375044,0.583882,4.901053,8.565378,-3.735956,9.233050,-3.057569,-0.805012,0.605255,-4.825482,-0.537782,-8.821861,0.623996,-2.217154,2.399893,6.613935,4.289667,-0.564987,-7.203812,-6.117765,3.429462,0.281264,6.331403,-9.984927,-9.091494,-5.187866,-8.860864,2.203894,-3.378028,-8.299685,-9.246083,-7.707466,-6.311614,2.261530,-8.864829,3.098237,1.008126,4.523517,-1.923016,9.040222,3.530057,1.675220,-3.409593,5.901640,8.779134,-0.066044,-4.762752,3.437385,7.826957,3.266581,-0.637418,1.666561,-0.225393,-5.090148,4.896557,1.023133,5.210515,-8.218078,-7.118936,-2.585026,2.069452,8.229062,5.706068,-1.638737,8.802833,-4.181035,-8.054469,7.998706,0.293649,-5.353163,1.662092,9.501205,-8.520638,9.717191,7.512477,-2.906344,-3.142666,-4.144551,-8.066764,6.132849,5.368836,1.355352,3.404160,-7.646715,-7.734813,5.948466,-1.674111,-9.054493,6.583915,0.122827,4.195015,5.907840,-9.248528,8.483665,1.020441,-9.448079,9.842134,-7.831353,9.796797,0.122095,9.807708,0.758762,1.799925,9.710327,4.702062,1.146397,-5.967835,6.781229,7.453961,-7.992165,5.039190,4.076758,-3.719217,2.759519,-2.175795,-7.001004,-0.237202,7.455540,8.112340,-5.239238,-9.879331,-0.043119,-3.005852,7.101180,-9.772796,-5.358678,-3.665073,-9.526560,-7.886534,-8.475500,-6.719812,-2.108220,1.859589,-5.609064,-2.814376,1.149328,9.188856,-9.612877,4.163755,9.503900,2.585363,7.854795,9.460338,-9.917644,-4.036740,-8.655464,8.218885,7.907447,-2.925495,-8.331281,-3.112524,9.985934,3.639159,0.552460,0.204210,-0.397773,6.632269,7.759148,-5.170468,-8.547298,-1.296169,4.650543,8.067628,-8.148679,6.116955,2.299556,0.380104,5.721406,-5.283742,1.853877,7.669781,-9.933611,-8.079539,1.381581,0.692071,2.961801,-0.645697,-6.904684,3.168554,9.040653,0.930589,-3.379142,-1.545315,0.586865,-5.755139,-9.548275,-5.205737,-6.899142,-8.919011,0.023289,2.254355,-5.465738,-3.336748,-3.898506,7.647346,-7.171810,-3.515675,1.172906,-9.759678,7.521106,-0.982323,-9.847509,-7.227843,0.041467,-3.980485,-1.845184,2.197531,3.614270,0.667077,5.664119,4.176042,8.137971,-7.423089,-3.233519,0.750620,7.700530,-7.237837,9.190445,6.966208,3.278079,8.092330,2.308770,-7.722889,-8.980712,-8.615673,6.839934,8.826726,6.104275,9.590295,-3.174409,1.620861,-1.118250,8.698734,-3.011629,-1.039931,-9.755809,-5.303156,-6.542827,-6.056360,-7.169868,-6.220240,0.690579,1.063502,6.803342,-1.885330,2.264465,-3.199443,9.252793,1.377407,-8.905069,-7.726059,-3.745801,-2.274970,5.126386,1.867704,-3.500036,2.347731,-3.575409,-3.178760,-6.672651,5.667941,3.177972,6.251659,-4.039072,-3.156304,1.591063,6.169468,1.539733,-8.889557,1.005395,5.210142,-3.257591,6.396391,3.420595,-1.064865,-6.658027,3.116001,6.660759,1.062838,-1.639955,-1.430071,-8.583599,9.956831,-7.342096,-3.845616,0.105359,3.737846,6.241766,-0.125708,-1.624079,-9.425788,9.955288,-8.412728,-4.467632,-5.237006,-7.244305,-1.847607,-9.516745,-2.922545,-8.001911,-3.957846,-9.826488,1.636625,-5.138795,-0.640173,-1.524498,-4.621247,7.238449,9.032545,-4.578247,-4.012962,-8.581391,8.512714,-7.341997,8.690839,-3.055284,-6.845860,5.823738,-9.821863,-4.702821,2.425632,3.201076,-3.961931,-8.801807,4.192107,7.212597,2.942395,-8.453601,-3.673653,2.040324,4.470338,-5.359210,-3.422396,9.557050,7.306908,-7.882321,7.504113,-1.082171,-7.816924,6.534738,4.803871,9.085858,-4.147528,4.406398,-4.879340,1.103669,4.883394,1.378327,8.512276,-4.320310,-0.030977,6.972772,1.779716,8.794139,4.844716,1.032498,6.092709,8.533708,-4.125567,6.660278,9.723338,9.162164,-5.141795,2.995984,5.944316,-1.457601,-5.022001,3.894270,-5.993251,4.645662,4.936043,-5.676249,6.682856,9.417712,6.081601,-3.342133,6.501391,5.444345,-0.816392,0.276611,-9.569724,-6.934499,-8.521694,-1.149998,-8.859082,-3.749318,-3.807366,5.972204,-6.586259,-6.126738,9.805722,8.703639,-9.696281,-9.569629,4.628437,-8.510494,5.590393,-1.338421,4.185635,-2.806037,-2.962002,1.923157,-4.445566,-2.651125,6.960693,-2.812786,9.845378,4.185773,-7.258200,-9.450345,-6.947824,7.849218,2.751355,2.809449,8.179875,4.363115,-2.264979,-1.221457,8.541870,4.566891,9.092020,4.098829,3.377653,-3.524722,-4.243739,8.843672,-7.097051,-3.865617,-2.343659,-5.033683,-7.088048,8.899795,-2.408296,3.146183,-3.156997,3.417157,-8.968037,-6.925053,1.492365,7.380757,-9.453351,-9.785151,6.263895,-8.493354,-4.533582,0.443058,-2.004440,1.325244,4.246797,-5.670563,-9.100330,3.082733,-2.674748,-8.660378,2.003429,7.867758,0.516967,-7.003602,7.490121,-9.261192,4.509431,-2.638457,6.548168,-8.705650,-7.919504,-3.573638,-5.949578,9.624473,-6.300784,1.736569,2.672323,6.176570,-3.419145,5.740483,-1.288051,-9.184618,-3.056790,-9.910039,-5.551176,-7.606361,5.052311,5.270923,-2.188164,7.043870,3.138279,-7.290815,0.231988,4.328458,4.514611,2.716971,-1.967374,9.842109,-4.672540,-2.286897,7.138326,0.986968,-6.241414,-8.984108,9.388889,3.122570,-6.418710,1.307933,6.316919,-7.107101,-5.677574,-9.421693,1.807130,4.228872,8.052604,-3.851407,-6.176460,-4.338195,9.718924,2.280839,-2.497243,8.321642,2.918261,-2.182152,4.076371,1.382225,9.876662,-9.362438,-1.600491,-0.571279,-6.768975,-0.408058,1.865427,6.774182,5.350510,5.267464,0.099241,3.450858,-0.770249,5.535529,-3.320688,0.014799,-3.126785,-9.316691,8.219952,0.244361,5.363368,-3.320558,-1.027999,9.657006,-1.967467,5.268478,1.240953,-8.355907,-4.405052,9.588550,3.696503,-0.619177,6.665392,-3.196434,-4.290115,-8.818172,2.323876,-2.755798,-7.505891,1.599590,-1.351266,-3.701439,2.407542,7.431990,-8.403415,-9.465972,0.408076,9.653325,7.149166,6.298935,6.928590,-7.454577,-4.716801,-6.381034,-3.232521,-9.434270,-5.364859,7.895041,6.083762,-1.627790,2.251463,8.664195,6.072422,1.280378,-8.999424,-7.024280,-4.869782,-5.100328,3.668732,2.354333,8.254940,4.205820,-7.649034,7.908005,6.198164,6.415626,5.015537,-0.379914,-8.342632,8.229218,-5.479416,-1.767071,-8.006760,-0.195082,-3.042987,-0.489515,5.214602,9.822179,-5.342050,0.921571,-1.149610,-0.270561,-7.403412,4.231610,8.878381,0.204921,-3.226869,-8.637372,6.283413,5.532693,8.821317,8.723432,3.733623,-9.426065,9.936544,6.009448,9.623354,5.756790,-4.924899,-5.372855,-4.465003,-0.730438,1.032260,0.391043,9.704294,-1.832328,-2.274814,2.852006,7.393533,4.193154,8.214210,-3.071147,5.539569,-5.411387,-8.866872,7.133850,1.569521,-0.083164,-0.181799,1.942605,-4.234438,-6.836653,0.719900,-3.399524,-4.110515,2.030268,-7.830107,-2.045038,-6.696111,-9.805923,4.990700,3.411109,2.488397,6.424150,7.004572,0.624879,7.473718,5.716222,2.661892,1.555870,8.354221,6.487279,-2.573721,5.579787,7.824082,-7.751796,8.194941,1.872454,1.904133,9.981096,5.380492,-6.463218,-3.737564,6.888725,2.574527,3.493180,6.296628,-8.499747,-3.790716,-9.544511,1.084453,-6.668576,-8.933558,0.680277,6.270777,3.607287,7.490207,4.493933,6.446515,6.069345,6.099355,8.590372,-3.293992,-3.919853,-0.429334,-9.151974,7.107520,-3.830198,-2.765768,4.777844,-0.481699,-3.122649,-7.570214,-9.368849,-3.707062,-4.251941,-4.803352,-6.022776,-3.309245,-8.862595,-9.478907,-3.534139,3.157042,4.192890,0.022642,7.138385,3.839847,0.514743,8.318455,6.345919,-5.616187,0.512576,-3.689790,7.571299,4.394855,8.644976,-4.391676,3.238742,-7.599036,4.963975,-1.508345,-9.769346,-6.232302,8.729314,5.118330,0.274623,1.680898,-2.951500,-9.204693,-0.064865,6.589781,4.324305,5.423709,-0.330531,-2.904340,8.937873,-4.259140,-9.009304,-9.335306,0.447462,7.166748,2.691986,1.664545,-0.398212,1.955742,0.143391,-1.172530,-1.547499,-5.942027,8.072453,-0.256338,8.170218,-9.004328,4.079896,8.238884,-7.879509,7.382810,5.735841,-9.202675,-8.176119,-5.832461,-2.435553,4.420703,2.221904,0.180635,-1.826214,0.324034,8.945295,3.717470,-5.690986,6.125365,9.607441,-1.880810,8.282964,-8.314532,-1.009260,-4.760841,4.685842,4.321420,4.445764,-9.216935,-4.623799,3.888959,5.249632,-4.473705,0.732242,3.118782,-8.453302,-6.019983,-1.064545,-1.009172,9.688343,7.068204,-1.897753,1.315857,-4.790443,5.914788,-5.306730,-0.603919,7.563032,3.632165,-1.616398,-5.274073,2.418873,-7.571611,9.248454,-2.081196,0.005405,-1.300077,9.889063,5.333424,7.828639,-7.934570,7.418494,0.930905,-6.595679,-6.092611,1.798511,3.927626,9.803152,-2.276805,-4.486351,3.798945,3.197950,2.873444,-8.299719,-3.943145,4.315173,8.874809,4.257007,-6.066728,1.798888,-5.443089,0.206080,7.080778,5.349255,1.657929,5.538374,-2.417344,-8.656563,1.762151,-6.769611,-5.031554,-7.059950,9.916983,8.731556,9.536883,-6.932966,9.807227,-4.182576,-7.876999,8.541732,9.457310,-2.457861,3.001333,-2.584446,4.745324,-8.401192,-7.331069,3.894422,-2.626882,2.240552,-6.941367,0.487862,8.931865,-0.341194,7.609981,-5.655417,-8.578837,-9.877216,7.724129,-4.188037,-7.658560,7.368543,-4.510742,-7.756132,1.741343,-2.216766,2.285817,0.556276,5.382117,-6.160217,0.774989,-7.453181,5.208790,0.835985,2.276865,-6.855002,-5.491595,-1.242316,-1.026533,3.188880,1.517965,6.611854,8.927856,8.942727,9.858580,-3.973900,-6.708870,-3.965750,8.349216,2.353963,-3.366427,-8.046639,0.127922,7.567268,2.245857,1.123142,-3.559201,9.217900,0.259638,5.712278,-1.334127,-7.506989,-6.781395,5.305352,-8.796971,-1.615785,-3.721107,-0.184998,4.459493,7.753006,-3.223747,5.390698,-4.666633,4.736019,-5.890471,-7.152640,-8.555007,1.027549,9.701748,-8.634075,3.306332,-5.895129,-9.714514,8.108928,-5.420132,-1.613136,4.182917,-7.423182,7.960018,-5.243744,-1.849773,-7.522491,7.038769,5.524638,-3.515822,-5.329228,-6.302354,5.279713,5.688237,-9.384297,-8.522867,9.004701,0.864033,4.935977,6.206635,-0.619053,-6.966254,-5.093525,-9.194375,-0.327319,3.295321,3.462865,-6.768955,-4.524321,0.879314,9.494645,-1.670416,-6.645645,-7.545952,-3.144005,6.628353,3.175872,7.329061,0.035777,0.805771,3.178872,-6.679517,-9.695164,7.258108,0.372776,-5.099803,-0.702165,7.422196,-8.364045,-2.723320,9.260654,4.892995,9.513417,-4.961717,-0.915629,8.974933,-6.406417,-8.106579,-2.712423,-8.427575,0.621541,-3.070384,6.059720,-2.965587,-9.099844,-3.375730,-4.095785,-0.151818,-0.056182,-8.493425,1.622549,-0.794095,8.221172,-7.495281,1.559541,5.488053,6.660814,-0.945675,5.997739,-1.292754,-5.060059,3.417125,-2.008276,-0.001329,-5.042019,-3.852119,-7.798618,-1.568870,0.806388,7.952211,7.150511,5.651892,3.192231,8.538747,-8.285619,-7.020178,-0.528365,5.710691,6.945382,8.350066,-4.787032,9.307636,4.567153,7.518709,5.172188,9.702223,8.264031,2.163051,-4.361503,-0.437022,3.510697,4.749677,-8.633519,-4.097236,3.589845,-7.169814,4.990328,-0.388584,4.562274,-2.524764,9.909179,8.446132,-0.254553,3.355853,0.116565,-7.476930,-0.291708,-2.364283,-7.550029,-5.909317,-7.702858,-9.072553,9.633478,-3.335571,-4.600567,3.298467,-2.515331,-4.519118,2.979487,-3.491662,4.093492,0.864273,-1.950067,5.933073,1.740614,-3.262342,-8.238506,2.994799,-2.177080,-9.532818,-1.346217,-9.863582,-4.125096,-9.360830,-6.866996,-9.066827,9.444034,3.909540,8.071526,-2.828331,-5.660778,-8.226463,6.114614,-1.405681,-8.893984,-2.824431,-1.496557,7.309614,-6.085907,4.872229,-4.935924,-8.463378,1.490923,-7.735250,-0.748438,9.103647,5.636915,8.756427,-5.425464,-9.066107,-3.917584,0.407554,6.166639,3.116648,-4.392033,-8.465220,-2.906766,-5.585870,-7.425141,-5.809522,-8.199959,-8.110568,-2.417483,-8.473030,1.286981,4.651854,-4.728622,4.660397,4.202870,3.144335,2.758308,0.700811,-6.596132,5.417562,-8.072380,-3.094481,-5.412688,-4.299531,-6.520225,5.459928,-0.047187,-1.263103,5.120495,-7.705231,-8.113144,1.700703,-3.918102,-7.273955,-6.108932,7.603762,5.278177,5.077847,-4.342422,-3.636710,7.534289,4.101485,-7.364031,-3.723396,7.672402,8.413271,-9.471498,0.479009,1.103737,4.898354,5.211311,-8.359810,-0.346333,-4.153613,3.687458,-0.797660,-3.381163,-2.953191,4.248004,7.645930,-9.659477,-2.825419,9.300011,7.663563,3.822341,-0.134063,6.443042,-5.043957,3.064024,3.222510,2.789953,2.719056,2.696265,7.920802,-7.613286,6.098620,9.362717,2.209270,1.820579,3.063853,0.225389,6.252309,-8.967593,3.098756,4.126123,-1.248943,-3.445917,-8.919803,-3.628847,-5.937784,-9.579583,1.514898,9.718929,-8.652187,9.565845,-9.735466,-1.754510,4.174167,8.823719,-6.401925,6.854556,3.184105,-0.378663,9.755301,7.963529,7.867968,8.816195,1.011367,6.617111,2.843872,4.391892,2.798343,-8.015635,-5.596422,1.142930,-8.178945,-2.872456,-7.054378,9.651487,0.196930,4.908638,3.438331,4.035550,-6.882509,-1.430453,4.450366,9.751390,0.370123,8.690314,7.545248,-2.912232,-8.292272,1.813823,2.323091,-1.876416,-6.963139,9.759518,0.140687,-5.869947,2.665856,1.664323,0.427459,-6.718523,-3.104044,-1.590843,-0.800443,0.551648,1.569917,-5.170397,-0.477237,7.500670,-8.797383,-3.756461,7.902383,8.305855,9.591655,3.199077,3.525295,-8.564188,-0.432375,0.631521,5.162240,0.325084,-6.154583,-3.565263,-7.996812,9.059128,-1.046664,-3.720240,-5.930175,9.535362,4.763157,-7.930126,-0.585390,-8.776865,-1.176515,5.614227,5.848495,-3.537471,-4.975210,-4.790268,7.297900,-8.083312,7.592060,5.646758,-0.995442,1.763581,-6.380854,0.545672,-6.694519,2.711070,9.426258,5.402529,8.430296,-0.776478,-5.392556,-5.756130,-8.361615,2.500200,-4.728805,-8.204591,1.547340,-5.984749,2.565088,-2.592377,3.075551,-8.890566,8.988246,0.721949,-0.773976,-9.789450,-6.533845,-3.896296,7.131110,-1.474588,-8.126638,7.363960,8.901320,0.538315,9.679175,-6.704595,7.918901,8.730498,-2.979541,6.630451,6.310259,0.371690,3.504802,-5.864759,-4.188237,-9.159132,3.896616,-7.190347,8.370451,-9.698336,-4.882191,4.691153,7.820115,-5.729143,-7.755355,-2.335554,9.903428,8.378297,0.229845,-9.093378,5.636341,1.213485,-1.244406,7.526688,8.514254,-9.756017,-2.974519,-1.875554,-7.974536,-3.627109,-3.712522,-6.063354,-7.816796,-3.535186,-4.522112,7.842154,8.344462,-5.475257,6.726093,0.109464,6.810390,-2.876790,-2.858197,-6.012123,7.793321,9.893616,9.891266,7.584635,7.144881,-3.567065,-5.504812,9.015636,-7.192091,3.787782,9.106764,-1.974823,-6.831053,4.727801,6.847757,-4.845281,-0.206560,6.361989,2.107325,6.185489,-8.055459,-7.029688,-4.885501,1.088818,-5.354741,-9.455552,6.499707,-3.100357,4.531511,-6.762474,6.139483,5.144878,-5.868193,-8.251579,8.857956,6.426334,7.476687,2.327809,9.833946,-1.366104,7.424361,-5.167504,3.390586,6.677666,-3.844887,-3.516350,-7.157407,6.635113,-9.859226,-6.492329,2.583577,9.919549,-3.113832,-9.556647,5.746951,8.917307,4.224168,-9.488962,-5.840312,5.084184,2.649867,2.489558,2.031785,8.614090,-0.649462,-9.281405,1.675574,-6.102928,-3.255796,1.883529,3.974111,-8.300384,-6.225093,7.075081,-6.920738,2.719709,-5.344207,4.603571,5.168565,8.320103,7.532779,-1.886957,-0.529890,-6.008022,0.879150,-3.181576,-9.455386,-6.902380,8.894940,8.224676,-2.309918,-1.535322,9.572107,9.533878,-3.157574,-1.682534,-9.718128,-3.190590,0.720926,0.699873,-7.764649,1.004656,-8.268951,-0.354738,-3.203575,-3.847192,-8.321126,3.831827,-9.595839,3.616244,-3.342349,-2.623588,-0.172623,5.540918,9.348408,-1.903927,-6.159595,-2.780919,4.645840,0.042134,5.242935,2.936389,-4.967796,8.200527,3.228673,4.687696,7.911781,-5.417491,-0.956845,4.616135,-1.433969,0.729363,-3.829608,4.915563,-5.493473,1.022009,-6.862513,-4.086532,7.024528,-4.609330,-6.829738,-3.312998,0.955808,1.854195,-1.035447,-9.543322,-1.376353,-9.347021,0.325222,9.893415,-7.991358,2.581645,2.957780,7.579409,-5.564353,9.866239,0.743922,-4.988854,-7.850268,-0.904041,-8.825745,3.309363,-2.936214,8.103901,2.050525,-0.168367,9.803292,8.786168,9.537155,-4.601896,-9.858355,-5.165634,5.973922,-2.454465,-2.649913,5.274544,0.165448,9.276745,-9.570013,-0.327284,4.892053,6.582479,-3.013520,4.566458,3.994144,6.331444,5.022136,8.819954,-0.459499,-3.822400,-9.764298,-1.939822,-6.384078,8.784402,-6.441389,7.564044,-0.459481,6.394149,2.377649,-3.403360,-8.966822,-1.563670,5.272971,-9.918620,0.501442,-3.384671,-1.167294,-6.431683,9.389686,8.895296,6.735057,3.797705,8.859256,-0.348416,-3.693194,4.527487,0.095177,-2.380432,0.758896,-6.368168,-2.948602,-9.791747,5.498469,5.266655,2.610196,6.493710,8.722957,-9.453439,6.471942,4.177068,-4.144392,-2.589753,-0.149966,-7.742037,1.547531,7.473175,-5.935608,7.771547,-9.855963,-6.008169,4.899303,-8.517144,-0.654645,-6.131235,1.956225,1.801674,-0.726262,0.356237,5.844856,4.001568,8.983291,-1.318639,-6.682298,4.626551,-2.548231,-1.587387,2.353406,3.227546,-9.115917,6.221936,5.225817,5.142436,-0.176281,1.475768,-7.779510,2.258256,0.126109,2.177135,4.293986,-5.177700,-5.158646,8.791692,8.220593,-0.534026,-5.121093,6.703080,-2.810594,-2.553989,-1.965769,-4.546876,-2.101158,-8.937973,0.064165,8.233208,-6.342249,2.375571,0.153170,2.890964,8.243715,-2.944081,1.837462,3.499220,-0.314031,0.330808,1.180893,3.911049,7.152751,9.653758,-3.097263,6.034811,-7.167256,9.812798,4.641201,-0.688375,-3.440659,4.324478,7.024490,-8.114191,-4.295382,-1.463682,5.569773,6.295447,2.531479,-6.359102,0.658590,-6.197037,-3.202103,1.104963,-7.164589,-0.743190,-5.517371,4.104291,-2.873432,2.456930,7.938357,7.351055,-6.301123,2.793643,4.770748,0.244735,4.408916,2.490479,7.418490,4.499883,-6.041480,0.333348,1.006316,-0.286600,-0.242811,-7.610543,7.886182,-5.791124,-2.290547,5.148814,8.333967,2.554405,4.048581,-8.304793,4.864063,-0.520860,8.630880,1.549685,-9.271459,6.437473,6.489770,-2.373244,7.651300,-1.952289,-3.514640,0.380331,-5.051702,-7.557401,7.627025,2.592236,1.629237,3.276740,8.007163,5.435292,-7.778135,-4.873357,9.682895,8.036303,0.492210,-6.066888,0.962033,-2.049652,-5.106768,3.459484,1.045413,7.540993,5.223376,-5.438553,5.128607,-1.560686,-6.601572,3.374871,-8.742575,-7.295686,9.879314,1.640640,-3.572625,-5.918936,2.540722,6.521888,-8.478252,8.231177,9.142332,-0.651341,8.447690,-9.232173,7.828206,8.060332,-9.553889,-1.267152,7.295159,3.930587,3.758677,-3.550480,9.177224,8.746375,-2.338364,6.564132,-5.092908,-6.162786,0.963793,5.768573,8.936293,-1.605668,-9.743004,7.804035,-0.994002,-0.056637,-6.231001,-7.897737,-0.993080,-3.429896,-5.536488,-8.193680,9.187668,1.041900,3.809481,-0.072465,8.665116,1.354750,1.533507,8.088240,9.532537,2.007001,9.227599,4.686725,2.503414,-3.942902,-8.035300,7.613987,-0.553624,-0.859406,1.281741,-9.979358,4.176797,0.537519,-8.651197,-1.343497,-3.551774,0.378921,-6.306217,9.033935,-5.039379,6.768307,-0.164558,2.161243,0.809974,-7.030597,-8.419333,-5.047251,-7.166326,-9.031918,-4.716536,-0.223945,-3.117983,-7.976408,8.843288,-5.351254,-8.237288,-8.167823,-7.040011,9.128287,7.878543,7.638748,-9.528964,4.253025,6.056964,4.336330,-3.849399,-8.305568,1.248660,8.352665,-2.730845,0.518971,-5.240869,9.837669,2.033901,-3.882812,-0.441556,-5.507278,7.702512,-0.436115,4.558077,8.995141,4.416897,-4.619486,-1.086140,8.455634,4.467399,5.505086,-3.029047,5.106447,4.650982,-0.355487,9.812850,-1.801560,-8.564563,9.145378,-7.717630,-5.742644,-6.810219,0.551999,-9.873872,8.640336,6.615650,0.806664,6.909741,1.746241,1.599696,-6.685514,-6.323363,2.738147,1.886987,-5.602504,3.052897,-9.751789,9.029998,6.019372,-4.618311,9.169212,8.367980,-8.963287,6.127891,-0.002736,4.082500,1.667560,9.140465,5.608081,6.003040,1.985358,-8.381846,-8.962103,2.620531,0.792475,-2.162121,9.823198,-2.354339,-2.665553,3.041802,-1.093810,-6.663456,-2.228697,-0.616725,-9.650998,6.082956,9.495955,9.892741,8.879690,5.282645,0.112558,4.121930,1.972215,-9.372960,-0.853957,-5.533009,-2.178015,-5.363617,8.075585,-5.915444,7.724553,4.366760,0.503590,-8.178004,9.064472,-0.996157,-7.170895,4.909086,8.263670,8.163038,8.637724,-1.499833,-4.291388,-8.763834,4.570396,-7.776703,-7.103564,5.889838,-6.344167,-9.030506,3.517161,-0.337518,-3.016805,-4.053834,5.326399,3.211670,0.279627,4.691256,1.509164,3.764754,-3.689588,8.179532,8.105807,2.854596,-9.312128,3.544777,-2.489608,7.437502,2.739661,-9.121945,-7.915132,1.816861,2.647094,4.575944,-2.169305,3.841303,-5.183167,1.220638,-5.379325,-2.515031,-1.377019,-8.980592,1.030433,-6.850114,0.843900,-5.057062,-5.060735,-2.423687,-6.272925,-5.388776,-3.175543,0.167040,-2.156010,4.194224,9.787879,-5.091723,2.369035,-9.456301,-9.133951,-6.481590,3.168923,2.729429,-5.254333,1.762990,-9.093570,-9.303719,-6.750679,6.297927,-7.320240,1.852189,-5.630344,-7.203037,-8.565231,1.216243,0.568605,4.499644,-7.926878,-8.721129,-4.885375,0.462802,-9.694898,3.758490,2.396317,6.254031,0.979771,-0.028531,-0.738642,-9.362059,1.553058,-1.481119,4.743333,-8.541546,-4.188709,-6.274272,-7.730369,7.416391,2.483546,5.396899,-5.694601,1.689373,9.567560,5.956069,-9.360369,7.681077,4.945287,-6.122918,4.920624,-5.225368,6.691044,-3.319852,-7.897917,-1.610784,-7.011467,3.110428,9.747934,9.293114,-1.942676,-3.261891,-4.852916,-5.051782,4.842557,-5.753863,0.885275,5.746761,1.542148,2.446479,5.779142,-0.871121,2.322329,-7.193234,-2.942898,-8.129730,8.429609,7.590913,-7.569046,6.427590,-2.415901,-6.039088,7.167781,-4.299120,0.684504,-2.998196,-5.762079,-6.092830,-5.531512,-1.530668,-9.348910,3.536249,9.904678,4.418123,6.959794,-7.899962,-9.188980,7.374966,-3.959243,8.900769,9.831471,-4.522628,-9.551206,-6.883871,-2.427200,4.398341,1.979639,-0.451681,0.943500,-6.005151,-7.043723,-5.941156,3.872029,-2.951619,5.582675,0.870469,-7.484476,-6.183415,-9.217878,4.359296,2.627920,-0.678026,-8.614174,-4.086915,-4.703362,-5.153941,0.023631,-2.686157,-5.264759,-2.674282,-7.992535,2.987323,2.276091,1.663997,-2.085723,-0.940228,5.635695,-6.058988,6.079741,2.322987,3.903962,5.378012,-0.748439,7.563139,-8.004922,-1.044226,0.619469,0.064751,-0.715957,-5.209626,-0.624720,-2.824580,0.718232,1.111586,7.453934,2.475369,-0.299537,9.360604,-8.916127,6.153718,-5.785180,2.209350,4.472041,9.694946,6.139034,-5.512328,-4.448066,8.753091,3.551494,6.475608,6.216188,1.512373,0.247043,-2.116171,1.953569,-4.594248,5.506937,2.879334,0.570155,-2.062619,4.727163,-4.668646,-3.165559,5.428253,-7.176839,-1.687034,0.348722,0.624999,4.788427,-2.277591,0.086073,-4.218261,-8.535815,-2.111886,-5.518241,-7.406876,3.512896,-1.322031,-2.933675,-4.063424,-4.642106,-3.678746,-5.535789,-0.996581,9.727707,1.855021,0.834626,-1.952610,6.846987,9.761641,8.691339,5.195827,-0.059980,-3.133020,-8.890673,0.229964,-7.092959,-2.317544,3.290997,-6.094049,-9.768376,-2.582546,3.138986,9.067781,2.700425,5.581252,0.729837,4.703534,-0.019684,-7.085300,-0.046342,7.599403,-6.932934,-1.981220,-3.182383,-9.834751,-9.635405,-7.297396,7.942816,-5.170609,0.643232,-4.231668,2.780107,-6.134054,8.514308,-9.088212,5.956769,-5.487816,1.481806,2.890321,4.028066,-5.126897,-7.990101,-3.107804,9.670928,-1.964473,-1.482400,8.312928,9.343616,2.612554,-4.908269,-1.787747,9.773267,4.446841,6.181887,-1.443604,7.396248,-5.937563,7.888743,0.596058,-1.969335,6.628962,-8.327283,-1.456431,8.405379,7.142171,0.918298,0.855378,-8.557746,3.219761,0.423681,3.567729,2.668511,6.261721,-0.648209,0.412294,-8.233893,3.790811,5.521323,-7.331799,2.501566,-1.553095,-4.565788,5.118882,6.187145,-3.271454,-5.529809,1.592652,-7.532026,-2.680835,9.355813,2.448367,2.298215,6.305677,-8.750324,3.216613,6.825438,-9.202715,1.389991,-0.072885,-3.201499,3.168256,-6.339316,-5.330703,9.559597,0.245170,-3.871455,1.477971,5.603977,-4.742625,-5.021723,3.972123,-4.341112,4.980509,2.672442,-7.362462,9.600226,-0.966914,-5.941131,-9.795562,-4.665527,-9.441135,-8.494579,-2.524978,-1.222118,5.327943,-7.924919,-4.772948,-4.760068,-3.452840,-7.144764,1.108920,-3.844507,5.366302,6.655460,6.621021,-8.235251,-6.616575,5.310662,-3.625929,-0.600055,-6.989717,4.270829,0.602607,4.304999,6.772005,-5.204033,4.661085,6.424478,3.899020,-3.615216,-1.288664,-3.592310,6.403026,7.365520,-4.015676,8.771103,-9.870834,5.342336,-6.549634,9.204070,-3.474164,-7.199071,-2.255762,3.260930,-8.668509,-4.916852,-3.506457,-5.721800,-2.243889,6.661804,1.540804,-6.829465,0.652051,9.763065,-2.299372,-6.898509,-7.545245,-4.366713,-6.381283,-8.053730,8.241811,0.119707,1.097618,3.948440,1.939404,-5.685663,6.210973,-0.225191,2.760865,-6.376770,-5.379157,-8.026852,7.168233,6.481199,-7.841167,6.789523,6.273498,8.082637,-6.171184,-5.282012,-8.137853,-4.068226,8.884369,-2.980353,-5.407324,-7.757788,4.283795,5.394318,2.688745,-9.306259,-6.347271,7.358781,-0.508800,-9.537038,1.291407,-7.979153,-0.473484,0.288737,4.593086,-0.017122,-7.575722,-1.139647,3.403969,3.814161,0.285899,5.479573,3.084618,9.321700,7.094443,-6.015238,-3.029068,-3.437488,2.926353,0.810905,-4.899120,-2.802323,-2.201877,-7.207340,-8.875131,3.879609,-6.096137,6.883051,6.658910,5.726947,-5.160652,-5.584415,6.493424,5.398971,-9.898515,2.388833,-5.291530,-5.938019,3.352315,0.953926,-9.192176,6.218931,3.226364,-6.207085,6.437432,1.255962,6.596867,-2.673702,8.189559,9.769169,-8.178321,-3.181238,-3.990979,-0.762622,2.547689,6.738349,-5.771786,-3.226730,3.851913,-6.190061,4.378088,-1.986574,0.630732,2.236311,7.729970,2.949727,9.286043,-4.732786,-0.314315,1.017606,-4.295527,9.769829,0.249473,-9.093211,-5.179836,2.689866,4.169125,-3.598854,2.147032,8.224353,-0.511885,-2.475454,-1.436638,8.647712,9.458176,-3.215874,6.616526,-9.768031,-1.683104,8.042555,-7.269191,-0.571584,-0.660475,-9.468158,-5.069308,-6.928796,-0.776085,-9.825524,-4.714923,1.087162,9.144132,8.145119,7.806029,4.055063,0.716182,-5.033313,-1.084029,6.681450,7.093046,-9.783214,1.920821,-5.983174,3.150373,-7.134062,-5.423893,-6.946775,6.438580,-1.885204,9.364339,-6.257942,-6.596891,-1.628025,3.180891,-2.793345,-7.140038,-0.721893,0.767876,0.338171,-5.229486,-6.991084,-7.300632,-4.375614,7.757975,-9.630293,-3.020256,9.199415,-8.104323,3.895102,5.624763,-9.790496,-2.985673,6.885534,-6.370898,7.746269,-1.477729,3.548345,-2.034840,-7.129704,2.929458,-9.390504,-4.014590,-7.828516,-2.275870,-1.558428,9.937049,0.565890,-5.658871,-7.071221,4.011430,7.971278,6.179844,-4.132574,-9.226637,7.224094,-8.139223,5.332228,5.004389,6.105975,-4.661416,9.973858,-3.510871,9.673125,9.987155,4.988918,9.656013,-7.768531,-2.283761,-7.683399,-9.132119,-3.492448,-5.603366,5.073228,8.607645,4.538030,-9.464295,-9.324751,4.159808,5.285341,9.614534,2.581140,0.565476,0.958031,0.868827,-7.751449,-8.790109,-3.192940,1.176567,-0.027293,-1.026666,-9.256924,6.440701,3.773730,-1.987487,8.255754,-2.194338,8.436372,3.744900,7.824539,-7.462588,-1.457522,-7.730211,3.101270,-8.773935,-6.997755,9.806507,7.118609,4.815591,3.049302,-6.229092,0.432859,-5.245433,-0.321634,-2.775337,-3.470407,-1.195398,8.946652,1.399266,-5.987973,-9.822235,-0.548682,1.134826,-6.306016,-8.084472,-1.063758,3.991330,7.286276,-3.448981,5.028325,1.537081,-7.585851,-9.580668,-8.284140,-2.606280,9.002611,-7.426456,6.307434,3.729248,-6.872638,9.972195,-9.085189,1.691153,-2.534577,-2.478002,-2.163880,3.146003,2.723505,-8.730885,8.438715,-2.113712,4.267501,-1.253873,-7.852898,8.320009,-8.458809,9.701265,7.356694,-6.335741,1.338679,1.258619,2.858899,-2.029045,-8.119904,-9.091432,4.711592,-4.186366,4.211379,5.572620,-0.856141,8.435041,-6.947933,-3.409303,7.260874,1.148661,1.656573,-0.713531,-3.202846,0.521510,9.626021,-5.671652,-8.471434,8.026168,-5.260257,7.904278,5.313592,4.853848,5.756176,9.896233,-5.576464,3.339874,9.245967,-1.431759,-5.318978,-5.940947,-2.772925,2.391986,2.784318,-1.737375,8.415925,8.292880,-9.620985,-3.334239,-3.741994,-8.081760,3.114232,-8.631088,3.913546,-2.801095,-6.662822,7.961410,3.013792,3.180686,-2.048921,-7.782558,0.948181,-2.934416,-1.891553,5.288075,9.539386,-4.733805,-2.168333,7.801141,0.413041,7.455926,7.870197,-2.087897,1.989847], dtype = "float64")#candidate|8675|(3360,)|const|float64
call_8673 = relay.TupleGetItem(func_5919_call(relay.reshape(const_8674.astype('float32'), [15, 4, 15]), relay.reshape(const_8674.astype('float32'), [15, 4, 15]), relay.reshape(const_8675.astype('float64'), [3360,]), ), 0)
call_8676 = relay.TupleGetItem(func_5923_call(relay.reshape(const_8674.astype('float32'), [15, 4, 15]), relay.reshape(const_8674.astype('float32'), [15, 4, 15]), relay.reshape(const_8675.astype('float64'), [3360,]), ), 0)
func_6692_call = mod.get_global_var('func_6692')
func_6695_call = mutated_mod.get_global_var('func_6695')
const_8679 = relay.const([8.947579,-1.121039,-6.368637,-0.525499,6.607647,-7.991923,3.519936,-1.911531,-0.863631,-7.779506,-3.359470,3.535889,-6.914157,0.855146,-6.747735,1.680754,8.002284,-8.602179,7.429649,9.547289,6.677037,4.579540,-1.061107,-4.171865,-3.149604,-0.484826,-0.293494,7.178887,-0.193778,6.821649,-2.850351,3.861146,-0.516026,9.124149,-6.216687,-5.896082,1.757024,-2.321983,-1.949143,-4.579844,0.614397,3.916097,-2.314246,0.958269,1.070723,0.514667,3.541066,2.089434,8.699877,1.391624,1.565141,2.799573,7.776749,-5.305865,-9.127847,-1.199873,-5.023804,4.559353,0.895609,6.113522,6.078890,-6.432732,6.597519,7.010361,-1.185879,-6.016250,-3.236760,-1.310005,0.450084,8.763600,-2.231775,-0.897732,4.355081,6.330478,-7.731036,4.825265,-5.954801,-3.193372,-9.681485,-4.879822,-2.611668,-3.796741,-6.631587,-4.060519,-0.245704,9.304483,-5.465584,4.679672,8.220142,-0.280574,6.061764,-7.915499,6.406987,-2.406646,-8.770271,-6.829919,8.550610,9.718273,-9.960815,-0.676811,-3.349002,5.693071,1.268846,-2.449053,7.224829,-0.549195,8.852677,-0.538790,2.924038,-2.873768,6.567185,-8.071899,4.713508,-8.505643,8.050913,-3.307438,-3.619051,-2.104766,-0.017909,0.220626,8.235906,3.099634,-2.002943,5.256448,-4.102734,6.517768,4.261725,-9.444292,9.322031,-3.352727,1.130944,-1.008875,-3.677262,6.772531,-5.443533,-9.657054,-4.273418,-9.298584,-2.973300,-1.616162,5.252054,-5.799367,0.016089,2.376982,-7.016294,-8.977199,2.754202,3.367916,8.879854,-5.889558,5.416264,-4.587344,-2.336705,-6.819639,-6.381307,4.864442,-6.360780,-5.078847,2.109777,1.920318,5.945928,2.875936,-9.915675,-8.086230,-7.499001,8.668632,-6.186041,6.284542,-7.728482,3.754918,7.031608,-7.801638,-5.390550,8.896840,5.511853,1.417779,-1.817564,8.888970,-1.093227,9.542690,-2.900149,-5.948667,-0.518263,-4.634925,-7.349044,4.242959,-7.102242,4.447867,8.357852,-3.514675,7.175139,1.216454,3.905786,6.244765,0.708270,-3.449455,9.670143,-4.789456,-1.648218,6.683254,-9.077207,-8.272364,-9.335333,1.992595,1.598958,-8.186847,-0.020408,-0.365059,-2.148235,4.145164,-7.922335,-4.493505,-1.722257,6.691427,5.662927,7.501453,-1.345058,-7.556618,-3.225867,-1.991098,-9.944497,-4.737542,-0.651211,-9.665510,-2.391412,-4.375853,4.588512,4.555688,9.081288,-8.029913,4.713693,-8.259201,-7.259677,-6.001658,7.241670,-7.862226,-6.312238,-3.421566,5.011062,7.016482,-8.208442,4.778649,-6.574220,3.465123,2.255108,-8.189191,-4.068296,-6.217538,-6.401025,2.917898,6.960193,1.697421,-1.806696,5.771396,-3.681017,-5.411858,-6.985762,-0.727526,-7.618066,5.452211,4.166376,-3.053055,-5.327741,-5.998382,7.467555,-6.280704,2.085898,-3.767457,6.422421,-6.564615,6.510792,-1.121023,-8.456514,-5.393139,6.669700,-7.149730,-3.795215,-7.985928,-7.680599,8.406520,-5.885108,-9.094161,2.478408,2.863997,-9.986802,-1.674961,-2.156292,-3.323506,5.759122,5.531900,-9.851093,2.039418,-0.750044,9.046807,1.399729,8.485817,2.766688,5.669177,-6.077849,8.102952,-3.742115,-1.422767,4.103463,1.709899,-8.398315,2.336879,6.441838,2.353243,-7.237653,-7.616568,9.875045,7.405832,8.350334,1.915349,6.100513,9.721929,-0.344201,8.739932,-7.684091,-6.435748,8.952524,9.449672,-1.181586,8.897667,2.168179,-2.748444,8.929287,2.049824,1.156877,-3.165397,-1.349610,-6.676908,-6.289096,-3.909902,3.897265,7.094400,-6.043159,5.288515,9.133960,5.598385,-5.125484,5.734855,7.063857,-7.541112,6.919838,0.599059,-6.673726,-9.288702,0.724812,1.417370,7.163792,-8.889937,3.402940,-7.582288,-7.610103,-6.510219,-5.111766,-7.230128,-9.500654,-4.394506,5.292327,7.626950,8.004492,-0.268929,-1.738360,6.590232,-8.303334,1.454629,9.147004,-6.409940,8.444874,-4.065420,-3.267605,5.103693,-4.847553,-3.320974,-0.902312,1.761841], dtype = "float32")#candidate|8679|(378,)|const|float32
call_8678 = relay.TupleGetItem(func_6692_call(relay.reshape(const_8679.astype('float32'), [9, 14, 3])), 0)
call_8680 = relay.TupleGetItem(func_6695_call(relay.reshape(const_8679.astype('float32'), [9, 14, 3])), 0)
func_6176_call = mod.get_global_var('func_6176')
func_6181_call = mutated_mod.get_global_var('func_6181')
var_8683 = relay.var("var_8683", dtype = "uint32", shape = ())#candidate|8683|()|var|uint32
const_8684 = relay.const([1,-1,7,7,2,-7,-6,-10,4,7,-7,-9,4,-8,-1,9,4,6,10,3,7,-6,8,-1,-3,-10,-9,-3,-5,4,-4,1,3,-3,9,4,6,10,6,-6,-2,-1,-7,5,-5,-9,-4,-9,6,-1,-6,2,6,5,5,-3,10,-9,-10,9,5,-4,-6,7,5,-8], dtype = "uint32")#candidate|8684|(66,)|const|uint32
var_8685 = relay.var("var_8685", dtype = "int64", shape = (312,))#candidate|8685|(312,)|var|int64
call_8682 = relay.TupleGetItem(func_6176_call(relay.reshape(var_8683.astype('uint32'), []), relay.reshape(const_8684.astype('uint32'), [66,]), relay.reshape(var_8685.astype('int64'), [156, 2]), ), 4)
call_8686 = relay.TupleGetItem(func_6181_call(relay.reshape(var_8683.astype('uint32'), []), relay.reshape(const_8684.astype('uint32'), [66,]), relay.reshape(var_8685.astype('int64'), [156, 2]), ), 4)
output = relay.Tuple([call_8635,call_8658,call_8673,const_8674,const_8675,call_8678,const_8679,call_8682,var_8683,const_8684,var_8685,])
output2 = relay.Tuple([call_8636,call_8659,call_8676,const_8674,const_8675,call_8680,const_8679,call_8686,var_8683,const_8684,var_8685,])
func_8699 = relay.Function([var_8683,var_8685,], output)
mod['func_8699'] = func_8699
mod = relay.transform.InferType()(mod)
mutated_mod['func_8699'] = func_8699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8699_call = mutated_mod.get_global_var('func_8699')
var_8701 = relay.var("var_8701", dtype = "uint32", shape = ())#candidate|8701|()|var|uint32
var_8702 = relay.var("var_8702", dtype = "int64", shape = (312,))#candidate|8702|(312,)|var|int64
call_8700 = func_8699_call(var_8701,var_8702,)
output = call_8700
func_8703 = relay.Function([var_8701,var_8702,], output)
mutated_mod['func_8703'] = func_8703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7445_call = mod.get_global_var('func_7445')
func_7447_call = mutated_mod.get_global_var('func_7447')
call_8749 = relay.TupleGetItem(func_7445_call(), 0)
call_8750 = relay.TupleGetItem(func_7447_call(), 0)
func_8444_call = mod.get_global_var('func_8444')
func_8448_call = mutated_mod.get_global_var('func_8448')
var_8754 = relay.var("var_8754", dtype = "float64", shape = (24,))#candidate|8754|(24,)|var|float64
const_8755 = relay.const([10,-10,1,-3,-9,-4,8,-1,3,-5,-8,-8,3,-1,-3,-6,4,-9,-6,-6,7,-9,1,-8,-5,3,-1,2,-2,10,9,-10,2,10,4,-10,-7,-6,10,-5,8,-10,10,-2,5,10,9,-9,-9,-8,4,-4,8,9,5,-7,-1,1,-9,4,6,-9,1,-6,6,5,-4,1,8,-4,-4,-7,7,8,2,3,-5,-3,-2,-9,4,8,-3,-4,9,-6,-8,-9,1,-3,9,-3,8,-3,6,7,-7,10,6,-3,-1,-9,1,5,5,-9,2,9,7,-10,-3,4,4,10,-9,4,-1,10,10,8,-3,-10,-6,-7,-10,-7,-6,2,7,1,-6,-10,9,-1,-7,-6,3,-7,4,3,3,-6,-2,-2,-2,-7,-9,5,8,10,-4,-6,-2,-7,1,10,-9,4,5,-2,-10,-3,-7,10,4,-1,-4,-7,-1,3,-2,5,-7,7,-8,9,10,-8,2,-2,-6,7,1,-8,-8,-4,2,-4,-2,-1,1,-8,-3,8,4,4,-7,2,4,-10,-1,-3,-6,1,9,10,-3,-1,-7,-2,2,-5,-6,5,-8,-2,-1,-1,-5,7,-4,4,-7,4,5,-7,1,-6,-10,6,-5,-5,7,-5,8,-6,1,2,6,-6,-1,10,4,8,6,-1,6,9,-2,4,8,-2,10,1,-9,9,-9,-1,-4,8,-7,-4,5,-4,10,4,-8,1,10,5,8,-7,-4,1,-1,1,7,9,-9,-8,-1,-8,-9,-10,-10,6,1,-4,-6,-5,5,-3,9,6,-4,-6,-7,7,-1,4,-2,-9,6,7,10,8,-6,-10,2,-3,-10,-3], dtype = "int64")#candidate|8755|(312,)|const|int64
call_8753 = relay.TupleGetItem(func_8444_call(relay.reshape(var_8754.astype('float64'), [24,]), relay.reshape(const_8755.astype('int64'), [6, 52]), ), 5)
call_8756 = relay.TupleGetItem(func_8448_call(relay.reshape(var_8754.astype('float64'), [24,]), relay.reshape(const_8755.astype('int64'), [6, 52]), ), 5)
output = relay.Tuple([call_8749,call_8753,var_8754,const_8755,])
output2 = relay.Tuple([call_8750,call_8756,var_8754,const_8755,])
func_8757 = relay.Function([var_8754,], output)
mod['func_8757'] = func_8757
mod = relay.transform.InferType()(mod)
var_8758 = relay.var("var_8758", dtype = "float64", shape = (24,))#candidate|8758|(24,)|var|float64
output = func_8757(var_8758)
func_8759 = relay.Function([var_8758], output)
mutated_mod['func_8759'] = func_8759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8289_call = mod.get_global_var('func_8289')
func_8290_call = mutated_mod.get_global_var('func_8290')
call_8805 = relay.TupleGetItem(func_8289_call(), 0)
call_8806 = relay.TupleGetItem(func_8290_call(), 0)
output = relay.Tuple([call_8805,])
output2 = relay.Tuple([call_8806,])
func_8834 = relay.Function([], output)
mod['func_8834'] = func_8834
mod = relay.transform.InferType()(mod)
output = func_8834()
func_8835 = relay.Function([], output)
mutated_mod['func_8835'] = func_8835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6967_call = mod.get_global_var('func_6967')
func_6968_call = mutated_mod.get_global_var('func_6968')
call_8847 = relay.TupleGetItem(func_6967_call(), 0)
call_8848 = relay.TupleGetItem(func_6968_call(), 0)
output = relay.Tuple([call_8847,])
output2 = relay.Tuple([call_8848,])
func_8850 = relay.Function([], output)
mod['func_8850'] = func_8850
mod = relay.transform.InferType()(mod)
output = func_8850()
func_8851 = relay.Function([], output)
mutated_mod['func_8851'] = func_8851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6512_call = mod.get_global_var('func_6512')
func_6514_call = mutated_mod.get_global_var('func_6514')
call_8872 = relay.TupleGetItem(func_6512_call(), 1)
call_8873 = relay.TupleGetItem(func_6514_call(), 1)
output = call_8872
output2 = call_8873
func_8874 = relay.Function([], output)
mod['func_8874'] = func_8874
mod = relay.transform.InferType()(mod)
output = func_8874()
func_8875 = relay.Function([], output)
mutated_mod['func_8875'] = func_8875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7445_call = mod.get_global_var('func_7445')
func_7447_call = mutated_mod.get_global_var('func_7447')
call_8939 = relay.TupleGetItem(func_7445_call(), 0)
call_8940 = relay.TupleGetItem(func_7447_call(), 0)
output = relay.Tuple([call_8939,])
output2 = relay.Tuple([call_8940,])
func_8942 = relay.Function([], output)
mod['func_8942'] = func_8942
mod = relay.transform.InferType()(mod)
output = func_8942()
func_8943 = relay.Function([], output)
mutated_mod['func_8943'] = func_8943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6295_call = mod.get_global_var('func_6295')
func_6296_call = mutated_mod.get_global_var('func_6296')
call_8972 = relay.TupleGetItem(func_6295_call(), 0)
call_8973 = relay.TupleGetItem(func_6296_call(), 0)
func_7630_call = mod.get_global_var('func_7630')
func_7635_call = mutated_mod.get_global_var('func_7635')
const_8977 = relay.const([-0.677625,3.609175,5.099917,0.002383,-8.943880,3.605217,7.538541,0.659924,-8.085183,6.848888,-5.243550,-8.912207,1.515857,5.534743,3.414474,-0.317115,8.297269,-6.359258,8.738287,8.970175,7.972107,0.229340,1.768559,-4.512121,0.733780,5.388061,4.755568,-0.512502,-9.328696,1.930409,-0.712162,-1.725581,8.068896,-7.389039,-3.748605,4.934041,-4.700261,-7.452206,8.196529,-9.477824,-7.858961,-8.778886,0.046909,6.301212,2.548199,4.766238,-9.914207,3.251091,-4.500546,-2.714927,2.520629,7.850862,4.538852,7.259068,-5.491693,7.448439,4.404952,-6.731440,-1.359376,3.199361,3.986845,6.668565,-2.579138,6.130344,-7.522231,2.740625,5.384986,1.149671,-7.274306,8.933729,-2.620735,-7.812522,9.500990,-5.901170,-0.001228,1.108373,2.662080,4.966869,1.347847,-7.646048,-8.988159,-3.508549,-1.886977,-2.431078,-3.084061,-6.100127,-3.011007,0.547332,4.787158,0.080831,2.586909,7.401275,9.690853,-9.070617,-6.429349,-3.117082,-1.700261,-4.617594,6.463422,3.521862,6.192881,-0.421218,-9.577204,3.022231,-5.790109,4.587673,2.691775,-8.873419,5.110628,0.511725,7.241218,2.427928,-3.895047,4.095783,-2.781402,-5.189876,-6.761421,-0.027941,-0.060157,-2.665369,-6.355157,-8.220207,8.226971,1.936919,3.875519,-7.439104,-1.867946,-2.148090,1.145028,-8.831139,-6.981441,6.873502,-1.496771,-5.699815,2.901078,0.674469,-3.856023,3.309567,-6.000645,8.342050,-3.173303,-5.461635,5.904413,5.862277,-1.354210,-1.878821,-9.713786,9.459064,2.891724,8.535942,9.058928,6.507477,-3.351859,7.969252,8.126030,-3.074915,-3.434708,-1.904742,2.872018,-6.667524,-6.736889,0.638346,6.638727,8.490695,-1.264272,4.633604,4.415491,4.401136,-9.562771,-4.053226,4.784038,6.005103,2.231806,6.241172,0.573764,0.302079,4.095090,7.139325,6.955256,0.288215,5.206184,7.107185,5.108236,8.588654,3.105344,7.949251,-6.025721,-6.655247,4.149329,3.667153,-7.604842,-8.120745,8.579081,-9.781178,-8.745574,-7.729141,-2.896264,-9.794832,-3.871934,8.496378,2.972263,8.251934,2.699683,8.799322,5.638819,-8.303760,0.645527,8.852841,-1.116903,-9.781673,-5.065016,-9.688111,-4.905738,-4.468532,-2.529389,0.639999,4.087942,-6.803587,-7.396268,5.051369,-0.136707,2.920083,-3.201349,-3.447008,-8.409877,0.626904,6.747394,-8.290803,-3.070624,-4.289118,-3.005590,-4.330982,-9.690966,7.635352,-8.804213,2.220074,-5.952269,7.900230,3.923262,2.252491,-4.158557,-5.984476,-2.963238,7.875746,-0.337964,-8.919251,8.307832,-6.143798,8.228077,2.617140,-7.554076,-5.395348,1.369205,6.778109,5.190436,4.662587,1.847910,6.495696,-1.093221,-3.977229,-6.115848,3.762785,5.859155,-2.407660,7.517083,-3.007642,-2.355224,-8.326545,-7.141875,-6.959593,-2.737542,1.018126,-3.835714,-3.703120,-4.469551,9.624980,5.220081,-7.555721,-2.003334,5.221240,-2.962415,0.381240,-4.049269,2.434495,6.421389,-2.606638,2.401325,7.106366,-2.858149,-6.094045,-9.988106,6.399722,-0.623836,-6.374520,-9.558853,5.147786,6.597557,9.161303,-4.847224,4.630606,9.959163,-8.882190,5.027732,-5.887113,8.369071,-1.841103,-5.686947,7.273870,-1.951900,3.005557,1.830951,6.309085,7.488647,-9.364294,6.302543,1.619930,4.119517,8.956249,9.845284,-6.353056,-9.168374,-3.641886,-9.110715,-1.933113,8.669360,-6.746049,-8.218180,3.061776,-2.351587,4.699937,2.553981,-9.444593,-5.667730,-4.545489,4.389452,-7.365193,8.183734,-0.128898,-8.584716,-7.815260,-2.535596,-0.111262,7.669142,-0.979922,9.873953,1.441944,-2.968461,3.789067,-1.664115,-2.459579,-9.610774,4.188434,8.824078,-0.879788,-5.300757,9.946162,9.356403,6.467173,-9.164988,-4.409505,-5.819412,-3.015923,-6.899143,3.390170,0.383567,-5.258576,5.447449,-1.868124,-5.493344,-5.751170,3.177475,6.983411,-2.661595,1.570816,0.023204,-2.552571,-9.545124,-1.238719,6.139084,0.731017,-9.107667,-1.173766,4.995735,-7.626575,6.555896,9.404735,2.273767,6.913105,4.523407,-1.010740,8.282195,-6.871193,9.221353,-4.727222,4.305028,-7.858063,1.931912,7.271743,3.225814,-5.857070,-8.983767,8.951119,6.422313,0.339003,-3.283057,2.912234,6.948707,4.005206,-3.215416,9.603651,9.070963,0.891010,-9.580512,8.010721,4.773726,8.076281,4.713649,3.973030,0.643840,-5.568893,-7.123715,2.291063,9.022414,-6.400652,-8.230913,1.702925,8.645084,5.047108,1.464110,3.960206,-7.850876,9.397767,-8.799178,-7.007102,3.637421,2.135098,-3.947794,9.868471,4.044122,-2.917497,7.602295,4.634788,-9.706679,7.891059,1.242897,-9.930308,9.286316,-6.429716,-6.852341,3.013439,2.233161,4.916274,-7.953814,2.545520,7.734541,1.568349,-5.211403,9.184115,9.838293,-7.701765,-4.783256,5.888995,-3.515980,0.780082,-0.221862,5.745009,2.800623,-5.162018,8.803345,4.438080,5.992294,-2.523655,2.317984,-6.325032,-2.288265,5.250844,-5.385004,-3.654121,-4.808434,4.847162,-7.010842,-5.978912,-5.080022,2.386139,2.775226,-8.699180,-8.148132,-2.719360,-9.027779,-1.544966,1.768019,8.627788,-0.119877,1.936340,2.363659,-3.237423,3.193164,5.832676,4.284638,0.492595,1.766140,3.868580,-2.050467,9.768538,-3.685641,0.724959,-2.477118,7.015288,-2.825842,3.888661,-5.991953,-0.421696,1.861353,9.093621,-6.298347,3.742881,-5.686033,8.397959,-2.841482,3.117684,2.881882,-3.464144,-9.528680,-0.132865,-6.943242,-6.092784,6.127798,-0.985369,6.939073,2.971587,0.956201,8.397541,9.144939,-4.945886,-0.747703,0.060305,2.682545,6.255093,3.116570,-5.835264,6.856623,-7.515887,1.875125,2.133683,-0.756431,0.439258,7.646706,1.503226,4.686493,-7.460825,-6.082725,0.252667,-7.719018,6.601245,4.791072,3.171319,-5.570448,7.429845,3.852336,-8.072453,-1.364249,7.364283,2.936983,-6.536895,-3.689657,-7.940952,-3.046060,-6.557019,-7.352158,3.259568,-0.899449,-9.865088,-6.261635,-1.434875,0.482529,-5.549886,-0.433113,1.544691,-4.808238,6.339549,3.000913,5.012395,2.925495,-2.491419,5.051198,3.792434,-9.658843,3.201761,-3.345678,-4.174414,-7.539274,0.788519,-2.603453,-1.538005,-7.944576,-6.493057,3.022939,-7.711936,8.618656,-9.821801,-2.569762,-0.637242,-2.709967,0.871850,-7.969403,-0.747486,-8.622964,6.481673,-9.182220,-6.124143,4.578950,-8.083418,-5.854181,-6.243633,7.987887,3.116158,-1.432069,2.488961,1.534426,5.064728,-0.459205,-2.127921,6.463639,-7.038549,-8.596714,3.209068,9.122944,-8.088663,-1.262741,0.601355,-9.604403,9.404909,7.632598,0.608776,0.714336,-8.777889,-0.638330,4.436597,-3.273076,9.787618,-8.081403,6.051124,8.922729,6.616705,-3.946172,1.196973,4.063762,6.436509,1.695436,3.036398,-8.328949,9.052311,1.427924,-8.954775,-2.653026,-4.309797,-2.730927,-1.246229,4.607760,2.809720,-1.699975,-7.959874,0.556150,-2.603415,-5.216035,-6.289969,5.920192,8.949021,-1.059593,9.549465,-8.622917,4.379400,4.985689,-8.970938,2.494371,-2.724485,-1.236667,-5.402015,-4.791343,8.645723,-9.206011,5.063263,8.703052,-2.186092,2.656396,-6.594357,2.054038,-3.543782,3.449098,-7.922963,0.589309,-4.198679,5.953922,4.477015,-6.172343,1.367878,-0.766752,-3.154142,7.140783,9.252993,-8.032603,-5.605729,8.244600,-9.934477,5.861951,-6.660221,5.113962,0.019530,0.948793,6.196461,8.097434,-9.993161,0.351883,0.066617,-9.712170,5.699720,-9.545234,-0.418575,6.940531,-0.232517,1.633092,7.265090,6.554592,-9.140382,6.455031,-3.512957,-5.265770,2.228643,-2.567945,-1.247144,7.438899,4.481705,-6.544122,-1.387828,4.544819,-7.151180,5.961689,1.344684,-1.246282,6.079277,6.135240,-9.028553,-7.864030,-7.835239,-0.325200,0.649224,-3.070163,8.898982,8.379734,-9.943238,-8.151061,8.402052,-5.086757,5.778863,-2.741334,5.947738,-3.689266,2.019492,3.318867,1.897111,0.162359,5.613916,-8.783448,-0.499717,-7.116203,-2.199829,8.714064,-3.963968,-5.525634,5.889932,-2.141099,3.284750,-2.742953,-8.861705,-3.632051,-0.475236,-2.789195,3.810884,-8.500606,-8.520338,4.250782,-8.506507,8.380986,-3.951765,-3.386903,-5.483970,-4.122360,3.932416,6.854018,-4.444429,-3.900700,0.576774,8.031941,5.367424,-3.086869,-2.955250,-9.696052,-6.641856,-7.874512,2.137300,-5.729864,0.385377,3.316949,-7.579293,-5.527537,-4.896758,9.664781,-8.758852,3.125555,-2.492887,0.705025,8.818429,7.295343,0.360207,-1.673359,-6.621878,5.581122,-4.222458,9.302513,7.804379,6.159676,-3.618628,8.836649,8.066914,-3.484753,-5.454453,6.790940,0.937290,1.093922,-8.151286,9.493287,2.562563,-2.832840,-4.369909,-3.050542,-7.149393,7.228442,-9.389052,2.259686,3.011774,5.710346,1.563161,6.952716,-1.124790,-3.314132,7.056057,9.178453,-7.332500,-1.371092,2.354401,-5.307716,-2.082130,-2.198400,-7.210291,6.028190,4.459321,8.804902,4.096914,4.474420,3.433581,-4.475728,-4.006484,7.755182,7.409875,4.550160,-6.368739,-9.611729,3.138503,3.905003,-2.896779,-5.963996,-8.897108,4.035041,-8.147509,8.618820,-6.003586,-1.828496,4.224443,6.531044,1.156916,-1.793395,-2.110049,0.712847,7.175038,2.153423,9.837472,-0.718960,2.402144,5.109180,-6.318171,3.553339,-4.103134,1.099816,-5.527980,-9.079571,8.392187,8.752359,-4.642829,-3.818659,-1.418817,9.985170,8.727219,4.707309,0.936209,-2.636730,6.017087,-3.274902,-4.600788,5.477083,-5.561216,-5.036008,-9.245089,5.856125,-1.496243,0.024831,6.968507,-5.149371,-0.242525,9.514348,-2.549819,8.719585,-6.834024,0.839519,-7.340620,3.489431,4.874809,-2.266377,8.286625,-2.121862,1.064023,-7.821229,-7.853342,7.542383,-4.298528,4.199229,0.322518,-9.258048,-7.788099,-3.224002,1.315692,-9.495523,2.416213,-9.954984,-1.217789,9.976975,-7.882158,7.581663,-8.253933,5.005024,7.512104,-0.418254,-9.098854,-4.426716,-5.405853,8.991389,-0.969913,-3.028868,-1.120689,7.089758,7.471525,6.780834,-2.799144,0.067047,1.134248,-2.271543,6.023583,1.945617,7.460496,-5.972485,-8.810196,5.749587,9.042089,7.314140,3.335412,6.976142,8.576091,-5.170299,9.052171,-2.527973,4.825732,6.278289,5.214683,-2.722836,9.595151,6.967223,-7.980492,-3.508119,-0.584725,2.016722,-0.884045,4.317168,0.782662,-6.682666,3.283018,-1.790863,3.582183,2.864777,-8.220964,1.881401,-1.111134,-8.408333,-9.701005,3.900984,-2.240798,-1.320409,7.578121,-6.693400,6.981416,4.597086,9.718621,1.895487,4.131716,-8.360837,-4.733412,8.318902,-9.460270,6.845772,2.499774,2.427948,-2.947521,-7.743063,2.554143,-9.755985,2.686229,2.088116,8.407849,6.008207,1.896329,9.073241,-5.293066,1.632937,-1.704571,8.287068,1.270346,1.886309,-2.434818,3.770297,-5.365769,-7.462026,2.710452,-0.774505,7.510028,6.084111,9.176920,-3.092858,-4.616549,-1.157948,8.254505,-9.911464,5.585677,-2.874239,6.327093,6.464700,7.970726,-5.567948,-8.645979,-0.811730,-1.103030,-3.512978,-3.701664,9.535158,-7.123321,0.025378,2.854420,-4.306286,2.566505,-4.816435,-0.438719,-8.788877,-6.889129,-8.517255,1.090768,-7.022266,8.447688,-8.064835,9.159781,-2.477953,7.591168,9.914065,8.287627,1.347093,-8.173398,9.758293,-6.016559,4.518087,-9.095978,1.124119,-2.882447,-3.931858,-2.402022,2.083057,-3.872143,-1.673103,6.914813,3.544887,1.373201,9.420961,-2.471956,1.518061,-3.768326,3.235745,-2.687029,-4.647575,-0.862836,-1.299581,6.164853,3.074159,7.156136,-6.428797,0.741589,3.830914,-6.727633,6.327780,-0.417760,8.352992,7.657505,3.032944,7.285031,-5.782354,-4.240662,5.669817,-7.495082,-4.536037,-0.780400,-0.775707,-9.871463,-6.944979,-9.963568,1.528736,-9.184889,5.916322,-2.364507,-1.062677,-3.818261,3.047141,1.892504,0.403033,7.681364,-3.807907,-0.563298,-0.086438,-0.260227,8.481414,-6.877402,2.462415,-2.086547,-1.938183,-5.512840,-8.993251,4.363585,7.926327,-8.810984,-6.417610,-5.758402,1.017148,7.606576,4.071343,5.517557,-7.833395,-6.619503,-2.952074,-6.582372,9.376352,8.596939,1.671742,2.710018,-8.426470,1.859352,-7.250288,8.488726,-1.591726,7.249042,-0.982936,6.355182,-3.272185,5.497381,-2.149265,4.558639,-6.975781,0.172815,9.981785,-9.353248,2.464542,-2.028405,-5.185498,0.957652,-4.366640,-4.899111,7.856323,4.732400,7.495012,3.497674,-3.306401,4.037312,5.619221,-5.839632,-0.227738,-4.633852,0.432545,8.932763,-2.292146,-2.598503,2.305073,-2.291517,-5.625309,-3.727556,-4.265229,0.320414,-1.563627,4.782863,-0.247710,-8.868308,-5.537308,-5.881893,5.641006,3.792207,-0.618935,-1.098306,2.845560,6.417538,-3.989792,3.064343,8.527694,0.835719,-4.329400,5.643689,-0.150683,6.239619,2.388462,-4.832908,3.630598,-5.838036,-2.209310,7.418711,9.457171,9.070617,-0.239957,-6.091502,-4.019676,0.084980,-3.422577,9.849823,-3.926296,-9.410132,-7.977497,-1.063118,-7.548273,5.058374,5.044951,-2.527621,5.847029,-1.091290,8.987838,5.496179,-1.568745,-4.518014,-1.290708,5.455268,-0.484294,-8.164049,0.610978,-6.377271,7.980549,-6.132882,-9.253518,-1.725155,-9.725027,7.380661,3.280549,4.179946,4.125276,6.995424,5.778024,-8.941960,-1.408882,-5.355016,9.004216,8.170890,2.099214,4.940691,0.241207,3.600718,-2.006836,0.334363,-7.341787,5.856563,-6.421932,8.714320,7.404093,4.149009,-3.987349,0.155479,-9.789565,-4.021249,-3.819651,8.187500,9.246898,-5.555454,1.750117,-6.233256,-7.906292,5.449067,-8.344618,8.785132,-6.191184,2.817973,-4.771555,-5.636494,0.743679,-7.179478,-4.859481,9.958511,1.489115,2.057345,7.860454,-8.894168,6.467510,-9.176656,-8.811658,8.533603,-1.515487,8.287858,-6.153335,5.921287,-6.302372,7.634640,8.674267,8.945161,-1.761064,9.167458,-7.174837,-7.467374,6.355846,6.962122,-0.187242,-8.562451,5.069353,2.230176,9.193267,7.851745,5.223632,-8.971857,-1.599078,1.130292,-6.579204,-7.785654,-9.204666,-7.770465,-1.196509,1.741889,7.061494,7.764747,6.374920,-7.617774,-5.623902,-0.497110,-0.864055,-9.253590,-0.186902,-7.444898,2.701964,9.017288,6.157489,5.525088,4.147330,-1.520738,8.281297,7.391529,-5.655231,7.882699,-1.527232,-7.921439,5.878725,7.913760,-6.061698,-2.635874,-3.623699,8.367641,-3.854203,8.853461,4.231288,-2.568499,-7.709945,0.740557,2.165592,2.976042,9.037944,-3.422831,-8.668409,-7.462213,4.321559,-3.814308,2.945673,8.469154,1.572428,1.871420,-1.078672,0.321823,-5.430450,-9.805088,4.235349,5.211519,0.309088,9.863766,1.180451,6.241419,8.370311,-0.271286,0.964859,-4.950825,7.165667,-1.598278,2.320083,-0.687355,-2.241420,6.274848,-9.252615,-5.890269,-6.372247,9.256695,-7.657257,2.011533,2.466182,-9.363883,3.513062,5.868023,-5.179984,1.198840,7.098890,9.597924,-4.516226,3.862559,8.732551,-6.971237,-6.378426,4.423442,-0.563450,-2.307934,3.515607,8.305887,5.472393,1.407986,-1.636713,7.244743,-6.538374,3.653870,2.105796,4.173193,1.915236,-9.322888,9.810707,-8.129520,-9.342272,0.173869,1.585483,5.919952,4.600994,-1.085381,9.239980,0.489745,3.164971,-7.180214,-3.908190,5.769018,5.723196,9.843539,-2.140188,7.107571,-1.753366,-4.898475,5.615231,-4.124937,-0.625312,-4.601760,-0.913387,3.498050,-3.747081,-7.794672,9.777808,-4.639510,8.561264,0.677989,8.089444,5.802494,-2.668498,2.245061,9.015821,-4.785526,7.422702,2.145750,4.552433,3.178445,-9.247003,-1.877844,3.393843,-8.473864,-8.627179,-9.358008,-8.456578,0.390182], dtype = "float64")#candidate|8977|(1500,)|const|float64
const_8978 = relay.const([-4,1,8,-10,-4,9,-4,-7,1,10,5,-10,5,-5,-7,-10,-9,2,4,-8,-5,-2,-5,-2,7,8,-2,-6,2,3,-2,-2,-6,8,-8,-8,3,-6,1,5,-7,-1,1,9,-9,-5,-7,-9,3,3,-4,-6,1,7,9,-3,7,9,-9,3,1,8,7,9,7,-3,2,-1,-3,-8,-2,-1,3,9,8,-4,2,-7,1,10,9,-2,5,6,2,4,-3,5,7,-1,-7,-4,-7,9,6,-8,5,5,-1,-1,5,9,10,-5,9,2,1,5,6,5,-5,8,-3,1,-6,-9,8,8,-3,5,-10,-7,2,8,6,-1,-8,-3,3,-9,8,9,-7,6,-1,3,7,-4,-2,8,-8,10,-9,1,7,-1,7,1,-7,5,7,1,7,-4,8,8,-2,-3,9,2,-3,1,3,3,6,-9,-7,-6,6,5,3,-1,4,-7,-10,-1,2,-3,1,-6,-6,-1,-7,-9,-8,-8,-10,7,7,-6,-2,7,8,-8,6,7,1,6,6,3,-10,6,-4,-3,-6,-5,6,10,-4,3,4,-3,-10,7,4,10,2,3,7,-6,-3,-9,7,-2,-10,4,-7,-3,5,2,9,-3,-8,-9,-2,-9,-8,-5,10,7,-4,-5,9,9,5,5,-5,-5,5,-9,-10,2,-7,-4,-6,-8,-3,3,-3,8,-6,-4,-1,4,-4,5,-9,4,3,2,1,10,-5,8,5,-7,-6,2,1,-5,8,9,-6,3,10,-1,-7,7,-5,-1,-10,3,-1,-5,-10,-7,2,-6,-10,-10,-6,3,5,7,-6,2,9,2,-2,-10,9,3], dtype = "int64")#candidate|8978|(312,)|const|int64
const_8979 = relay.const([-9.751044,0.632249,8.483206,0.394387,-0.456379,8.588703,-4.914376,-0.587573,7.390575,-2.875015,2.636572,9.905908,-1.457485,-1.395832,-4.751809,-5.428804,1.580925,-9.005594,-9.572124,-1.485782,0.216236,4.390947,8.601171,-9.048929,-1.394225,-9.307385,-8.486622,-1.733877,-8.598183,5.632156,7.974879,8.370182,1.933174,-4.003043,5.303873,-7.389496,-4.191282,-5.909147,9.891891,-0.456591,8.057532,6.759413,-2.038979,-4.156043,0.112147,-2.891158,8.723888,5.409495,2.257822,-9.805157,-7.192528,7.575142,3.054317,-6.768084,8.713942,-7.521816,3.947681,-0.933064,-9.973207,-6.687408,-4.957364,-5.534877,-9.070355,-1.724089,3.408264,-4.326809,2.779519,-0.457077,7.408216,-8.209317,0.582906,5.581406,-8.529216,7.350215,6.319859,-9.717398,-3.780293,3.850562,-6.443617,-7.806770,1.017901,5.181863,4.168766,7.260666,3.587706,6.213415,-7.995804,8.885376,-1.431890,0.695091,9.370444,-3.553323,8.560914,-6.707642,5.706124,5.322971,-2.903495,-8.440460,3.523054,-8.385259,7.460023,2.249671,6.434879,-7.661692,1.200029,3.634942,-0.970964,-8.910374,7.742875,9.812544,-4.231323,7.464376,-7.499744,-3.255876,9.109513,-9.192471,-3.944307,7.686211,-1.230409,6.170434,5.187871,-5.941318,-6.048400,9.889646,-7.128013,5.209946,-4.649141,2.222189,-9.804743,-4.967728,-4.138532,-5.407199,-3.756953,-3.536327,1.962925,1.217448,-4.087586,-3.340454,-0.525613,3.951122,3.529447,9.777228,6.657390,-7.209992,-4.285223,-5.813352,0.922517,0.545608,-4.277666,-8.890015,-4.508053,-4.657391,-0.103005,9.738537,9.642183,7.284450,8.634470,-3.685800,0.479903,-7.802717,3.138722,-3.281485,4.944577,-0.848385,-2.279294,-9.568201,-0.308587,1.703257], dtype = "float32")#candidate|8979|(168,)|const|float32
call_8976 = relay.TupleGetItem(func_7630_call(relay.reshape(const_8977.astype('float64'), [1500,]), relay.reshape(const_8978.astype('int64'), [312,]), relay.reshape(const_8979.astype('float32'), [168,]), ), 7)
call_8980 = relay.TupleGetItem(func_7635_call(relay.reshape(const_8977.astype('float64'), [1500,]), relay.reshape(const_8978.astype('int64'), [312,]), relay.reshape(const_8979.astype('float32'), [168,]), ), 7)
func_1272_call = mod.get_global_var('func_1272')
func_1275_call = mutated_mod.get_global_var('func_1275')
var_8988 = relay.var("var_8988", dtype = "uint8", shape = (165,))#candidate|8988|(165,)|var|uint8
call_8987 = func_1272_call(relay.reshape(var_8988.astype('uint8'), [15, 11, 1]))
call_8989 = func_1272_call(relay.reshape(var_8988.astype('uint8'), [15, 11, 1]))
output = relay.Tuple([call_8972,call_8976,const_8977,const_8978,const_8979,call_8987,var_8988,])
output2 = relay.Tuple([call_8973,call_8980,const_8977,const_8978,const_8979,call_8989,var_8988,])
func_8994 = relay.Function([var_8988,], output)
mod['func_8994'] = func_8994
mod = relay.transform.InferType()(mod)
var_8995 = relay.var("var_8995", dtype = "uint8", shape = (165,))#candidate|8995|(165,)|var|uint8
output = func_8994(var_8995)
func_8996 = relay.Function([var_8995], output)
mutated_mod['func_8996'] = func_8996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8850_call = mod.get_global_var('func_8850')
func_8851_call = mutated_mod.get_global_var('func_8851')
call_9001 = relay.TupleGetItem(func_8850_call(), 0)
call_9002 = relay.TupleGetItem(func_8851_call(), 0)
func_7007_call = mod.get_global_var('func_7007')
func_7009_call = mutated_mod.get_global_var('func_7009')
call_9022 = func_7007_call()
call_9023 = func_7007_call()
func_8045_call = mod.get_global_var('func_8045')
func_8049_call = mutated_mod.get_global_var('func_8049')
var_9056 = relay.var("var_9056", dtype = "float32", shape = (672,))#candidate|9056|(672,)|var|float32
call_9055 = relay.TupleGetItem(func_8045_call(relay.reshape(var_9056.astype('float32'), [16, 14, 3]), relay.reshape(var_9056.astype('float32'), [16, 14, 3]), relay.reshape(call_9022.astype('uint8'), [60,]), ), 5)
call_9057 = relay.TupleGetItem(func_8049_call(relay.reshape(var_9056.astype('float32'), [16, 14, 3]), relay.reshape(var_9056.astype('float32'), [16, 14, 3]), relay.reshape(call_9022.astype('uint8'), [60,]), ), 5)
func_8757_call = mod.get_global_var('func_8757')
func_8759_call = mutated_mod.get_global_var('func_8759')
var_9067 = relay.var("var_9067", dtype = "float64", shape = (24,))#candidate|9067|(24,)|var|float64
call_9066 = relay.TupleGetItem(func_8757_call(relay.reshape(var_9067.astype('float64'), [24,])), 1)
call_9068 = relay.TupleGetItem(func_8759_call(relay.reshape(var_9067.astype('float64'), [24,])), 1)
output = relay.Tuple([call_9001,call_9022,call_9055,var_9056,call_9066,var_9067,])
output2 = relay.Tuple([call_9002,call_9023,call_9057,var_9056,call_9068,var_9067,])
func_9069 = relay.Function([var_9056,var_9067,], output)
mod['func_9069'] = func_9069
mod = relay.transform.InferType()(mod)
var_9070 = relay.var("var_9070", dtype = "float32", shape = (672,))#candidate|9070|(672,)|var|float32
var_9071 = relay.var("var_9071", dtype = "float64", shape = (24,))#candidate|9071|(24,)|var|float64
output = func_9069(var_9070,var_9071,)
func_9072 = relay.Function([var_9070,var_9071,], output)
mutated_mod['func_9072'] = func_9072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6967_call = mod.get_global_var('func_6967')
func_6968_call = mutated_mod.get_global_var('func_6968')
call_9096 = relay.TupleGetItem(func_6967_call(), 0)
call_9097 = relay.TupleGetItem(func_6968_call(), 0)
func_6413_call = mod.get_global_var('func_6413')
func_6415_call = mutated_mod.get_global_var('func_6415')
const_9126 = relay.const([9,-1,-6,9,-9,-8,-10,9,4,-6,5,3,10,10,9,-7,7,-3,-8,-8,7,-4,-4,6,-6,-5,10,3,-9,-8,-10,-1,10,-7,-6,-7,-10,7,5,2,-8,2,-6,10,10,4,-2,5,8,-10,9,-5,-10,5,-8,5,-5,-5,-2,6,2,3,4,-6,2,-5,7,9,4,1,2,-7,-4,8,7,9,-4,5,-10,10,-1,2,7,-3,7,1,3,4,2,5,-6,1,7,-7,1,1,-2,-9,-4,8,-10,9,-10,-1,7,-2,-10,-2,-2,-8,-4,-4,1,5,-6,5,5,9,8,-8,6,7,-4,5,-6,9,-1,8,6,7,8,10,-5,7,-7,-10,4,10,-6,5,9,4,9,-2,-5,1,-1,7,7,1,8,10,-9,-1,5,-9,-2,-4,6,9,7,5,10,5,-5,-3,10,-4,-4,-7,10,3,10,-6,5,8,-5,1,-6,-3,5,-3,-9,-7,3,-2,-10,7,-2,6,6,3,-10,7,1,8,-5,-4,-9,7,-2,5,4,2,4,-5,-4,4,-3,2,10,-1,-1,1,-3,-4,-7,-9,-2,7,8,10,2,-8,6,8,-9,3,5,2,2,5,6,8,-4,5,1,-8,1,8,5,5,9,6,2,2,-3,-1,2,6,-8,-9,-8,2,2,-7,7,3,-10,10,6,-3,-2,9,-6,1,7,3,-7,-5,6,-8,-1,-9,-1,-2,2,7,10,7,10,-1,5,2,-2,3,-6,1,5,10,-10,2,-8,5,2,7,7,8,-4,8,-7,4,-3,5,-6,3,-7,-9,3,-4,-5,6,9,-5,-6,10,3,9,10,5,8,3,2,-10,-5,9,-5,1,-1,-6,-9,-2,-10,-2,6,-8,5,10,5,-10,6,2,6,-5,2,-6,8,7,1,-10,-7,9,-2,-1,1,-1,3,-10,9,-6,9,-5,-9,6,-4,-5,9,-4,5,9,-7,4,-4,-6,2,-7,3,-9,-4,10,-3,8,-1,4,8,-3,-4,4,3,-4,-2,-5,2,-7,1,4,-2,-8,7,-8,-5,-1,-8,-10,6,6,-2,-5,7,1,-9,1,-1,4,-1,4,-1,-5,-1,10,9,-5,6,-7,10,-10,5,10,-8,-6,7,5,5,9,-6,-1,-4,8,-6,5,-5,7,-4,-7,-3,3,1,10,-9,3,-7,-2,3,-2,-5,7,10,9,4,10,9,7,-5,-7,5,2,6,-2,-2,-10,-9,-6,-4,7,-2,-3,-4,10,-7,-2,9,-4,-7,-4,9,7,-2,1,9,3,-6,-2,-7,8,9,8,-5,1,-9,3,2,7,3,1,5,5,10,-2,8,-3,-9,5,3,5,2,1,-8,-9,6,4,3,5,-7,-10,-4,-1,4,-8,-1,-1,1,-8,-10,-9,-8,2,-4,-5,-3,-3,-10,1,-2,2,-1,8,-5,-2,-7,3,-6,7,1,1,6,2,-10,-9,1,-6,4,-8,-2,6,-3,-5,6,-1,1,-3,-5,3,8,-6,3,5,7,8,4,-9,7,-8,-5,1,10,-4,-1,-10,7,9,-9,-7,8,6,-1,10,10,-10,6,2,9,3,-3,8,9,1,-4,4,6,-5,-6,7,-3,-2,10,7,4,-9,2,-8,-9,-1,-1,-6,-9,-6,-5,3,-9,7,3,-1,5,-3,-9,10,-1,-10,7,9,-6,1,7,-9,10,-8,-1,7,10,3,-2,9,3,6,-7,6,-2,-7,10,5,-4,-3,5,1,10,7,6,-5,-5,-10,8,6,-4,6,8,6,-8,7,8,9,3,-10,-9,-9,-6,5,-7,-1,-3,-5,-10,-3,9,-10,-7,5,-2,-10,-9,-5,9,8,-2,-7,6,8,-2,-4,10,-9,4,8,8,9,8,-10,-6,3,7,-5,-1,-1,-3,-5,1,-9,-8,3,4,1,5,-10,-2,-1,10,-2,-8,-5,9,3,6,5,8,1,-9,5,-6,5,8,6,3,-1,2,3,8,3,9,-1,7,10,-4,10,-9,-7,4,-5,3,9,1,-9,9,6,-2,-4,7,-5,-8,-1,1,-2,-1,-1,2,-10,-1,4,10,9,-7,1,6,6,-10,-10,5,5,10,10,5,7,-10,-7,2,-4,-10,4,-10,1,-9,4,-5,-10,4,-7,2,6,-6,2,-2,9,-1,7,5,-5,9,6,8,-8,-8,3,10,1,6,-4,-2,-10,5,-8,5,5,-3,-9,9,-3,-6,-8,-10,4,6,4,-2,3,-2,-8,-2,-3,5,6,-1,2,7,-4,3,-1,-6,7,9,-5,-10,-10,-7,-9,-4,8,-4,-3,-2,-8,-2,6,-5,-6,-4,7,-4,-8,9,3,10,9,2,7,-8,3,-5,8,3,-6,4,2,-10,9,6,5,5,-4,-7,-3,5,4,4,-9,5,5,-1,-7,7,-2,-10,-1,-2,-4,-5,1,4,7,7,-4,-3,4,-5,-5,-9,-5,6,5,-2,-7,7,-4,-3,-8,9,5,-10,8,-1,8,-1,-8,1,-5,4,8,9,-2,-5,3,2,-7,-8,-2,7,-7,-4,-7,2,-8,3,-10,9,5,4,-9,-7,-1,-3,-1,4,1,7,-3,-10,-5,-8,-7,9,-3,1,9,10,2,4,6,-5,6,-4,9,3,-9,3,7,10,-2,4,9,-3,7], dtype = "uint32")#candidate|9126|(1008,)|const|uint32
call_9125 = relay.TupleGetItem(func_6413_call(relay.reshape(const_9126.astype('uint32'), [1008,])), 2)
call_9127 = relay.TupleGetItem(func_6415_call(relay.reshape(const_9126.astype('uint32'), [1008,])), 2)
output = relay.Tuple([call_9096,call_9125,const_9126,])
output2 = relay.Tuple([call_9097,call_9127,const_9126,])
func_9130 = relay.Function([], output)
mod['func_9130'] = func_9130
mod = relay.transform.InferType()(mod)
mutated_mod['func_9130'] = func_9130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9130_call = mutated_mod.get_global_var('func_9130')
call_9131 = func_9130_call()
output = call_9131
func_9132 = relay.Function([], output)
mutated_mod['func_9132'] = func_9132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7965_call = mod.get_global_var('func_7965')
func_7966_call = mutated_mod.get_global_var('func_7966')
call_9226 = func_7965_call()
call_9227 = func_7965_call()
output = call_9226
output2 = call_9227
func_9236 = relay.Function([], output)
mod['func_9236'] = func_9236
mod = relay.transform.InferType()(mod)
output = func_9236()
func_9237 = relay.Function([], output)
mutated_mod['func_9237'] = func_9237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mod.get_global_var('func_7037')
func_7039_call = mutated_mod.get_global_var('func_7039')
call_9331 = relay.TupleGetItem(func_7037_call(), 0)
call_9332 = relay.TupleGetItem(func_7039_call(), 0)
func_4834_call = mod.get_global_var('func_4834')
func_4837_call = mutated_mod.get_global_var('func_4837')
const_9358 = relay.const([-5.188742,-7.747885,5.208181,-1.853069,-9.370684,9.698430,-8.402850,8.239958,-4.977601,-7.751324,5.948917,-9.371114,2.109262,-0.398034,-9.793434,6.604499,9.499728,8.572898,0.616341,-2.291081,-2.771613,-1.284844,-6.215477,6.604600,-6.317544,9.255688,-5.074084,-6.316958,1.508283,-2.835056,7.377672,-5.459756,7.289978,4.804237,-8.339892,3.496825,-0.262073,2.709327,2.392815,2.574549,-2.061394,-3.462462,-5.637800,-8.549193,5.478001,6.849327,-9.015990,7.787815,-1.481354,1.170236,2.928596,4.728791,-8.550005,-4.083785,8.752153,0.009101,8.937705,-7.896394,-0.962322,3.782038,8.675849,-5.243486,-0.295045,0.009835,6.777168,1.350905,3.959451,-5.616947,8.247078,-5.946761,-8.270302,-0.527308,7.331180,0.054142,-0.384900,6.051072,7.123108,7.508733,1.236510,-3.994194,7.475169,7.940895,-8.609518,-9.652665,8.849347,-9.022606,-0.381002,5.389608,8.181789,7.936275,4.352583,1.300146,1.720993,-8.097931,-3.452998,9.302744,6.758400,-1.743415,-1.746564,1.182198,0.976262,6.843359,5.314307,1.743397,3.510799,-4.924621,8.508118,3.993480,-4.554817,-8.319546,3.776499,6.342978,-6.769512,-6.447484,-0.325903,-9.944214,-2.345499,-1.835569,-2.979678,-0.857097,-6.266378,-8.391128,4.917080,-0.778754,-7.880915,-3.679268,-3.259417,-9.082104,8.972250,1.831157,-1.375033,-3.679158,4.806039,-5.560576,-7.619954,4.816469,9.150428,7.782567,-2.663951,9.270243,-0.215952,-1.564568,3.756402,5.256279,6.756624,-5.323749,8.112405,-9.909157,4.730117,-6.513779,-7.419451,3.048380,-8.168122,-1.319487,-3.830229,0.509953,2.612102,-5.346393,-0.884970,3.420994,-7.908702,8.341678,-5.101717,1.689928,3.255671,-9.195058,8.255351,7.500421], dtype = "float64")#candidate|9358|(168,)|const|float64
call_9357 = relay.TupleGetItem(func_4834_call(relay.reshape(const_9358.astype('float64'), [4, 3, 14])), 0)
call_9359 = relay.TupleGetItem(func_4837_call(relay.reshape(const_9358.astype('float64'), [4, 3, 14])), 0)
func_6413_call = mod.get_global_var('func_6413')
func_6415_call = mutated_mod.get_global_var('func_6415')
const_9380 = relay.const([-4,-3,-1,2,-9,4,-9,-2,-9,-9,6,10,-2,6,-6,4,-1,3,-1,-7,2,-10,2,-5,-8,6,4,3,-8,-7,-3,-6,-10,-6,4,1,-7,-8,-2,-9,-7,-6,10,-6,10,5,-6,10,2,7,1,5,-1,-6,7,-5,10,-5,3,-3,7,-8,2,9,4,-1,3,3,-10,9,4,-4,-7,9,2,-1,-1,-10,-7,-7,4,-5,6,5,9,-5,-7,-9,8,2,-1,9,-4,-5,9,-3,1,-1,8,-7,9,-9,-1,-1,-10,10,-10,5,9,6,-3,-10,6,5,9,-2,4,-7,2,7,-4,5,-8,-9,-10,5,-3,2,-10,5,7,-10,-9,-7,8,2,10,8,-8,5,2,-3,-6,-4,2,-8,7,1,6,8,1,-7,-9,-1,4,7,7,-10,-5,-9,-6,-5,4,2,3,7,-9,-4,-1,-7,10,-10,-4,-10,-7,-7,8,7,-7,4,-8,-3,-5,-7,-2,1,6,1,-2,-10,-1,-1,8,-3,-8,6,-7,-2,8,1,4,3,5,-2,4,5,1,-4,-3,-4,3,-6,-1,-7,10,8,-1,-7,-5,-3,-3,6,-4,2,9,-10,-8,-7,7,-7,-1,2,-7,10,8,-5,-4,4,1,-7,4,5,6,-2,-5,9,-5,9,9,-8,-5,-9,-1,-6,1,-5,1,-8,1,9,10,-3,10,-8,3,8,-6,6,-2,-4,-6,-1,-10,-5,10,8,-3,-4,10,3,-10,1,8,5,-10,6,-7,-2,-5,-7,-10,-2,3,5,9,-9,9,-5,7,-10,9,10,10,-3,10,9,-5,2,-8,-3,7,8,-2,-4,4,-6,9,-1,10,5,5,10,4,10,-3,2,7,-5,-4,-9,-2,-3,3,-1,9,-4,9,-4,8,-8,7,2,-10,4,-7,-2,8,-1,1,-3,-7,5,-1,-10,3,3,-5,-5,-1,9,-1,-10,-8,9,4,-2,-1,6,5,4,-3,1,1,5,4,1,-6,-4,3,-4,9,5,-2,-3,-10,-9,5,2,-6,9,10,-5,10,-1,-5,9,2,4,-6,4,-8,-8,-3,-9,9,8,8,8,-5,3,5,-3,-6,4,8,8,3,8,-8,4,3,-7,-5,8,-3,1,-3,-8,3,-10,9,6,-4,7,-9,9,3,2,-2,-10,-3,4,5,-4,-3,-9,10,6,10,-8,-4,-1,-7,-7,-7,-4,7,-8,-10,-1,7,-7,7,-3,-7,-4,-1,8,-1,-7,-1,1,-10,2,-1,5,5,7,7,7,-2,-5,-7,3,9,8,-10,9,8,-10,-4,-9,6,1,5,-7,10,-3,8,-8,-5,-8,3,-7,-1,-2,-1,-6,-6,-2,6,1,5,6,10,-2,-10,2,-10,-8,5,5,-10,6,-9,-10,-2,-4,5,-10,-6,9,-5,-3,9,7,9,3,5,9,8,3,-10,-6,-9,-9,-1,2,1,-2,-5,6,2,-7,-9,-3,8,8,2,-3,2,-7,10,2,7,4,2,-9,-9,1,5,-4,9,10,-6,2,5,-5,-1,8,1,-9,10,-9,-6,-7,-4,1,5,-3,-4,-10,-6,-6,2,-4,-4,7,-3,-4,-7,-8,-4,-4,-2,-9,-4,7,-6,7,-7,-10,-4,-8,3,3,-5,-1,-2,7,4,2,6,9,10,-9,-7,-9,-6,-9,9,9,5,-2,-4,10,-6,5,-2,4,-10,-1,4,9,5,8,-2,-7,-4,-3,-9,-6,7,-6,8,3,5,-7,3,8,6,3,3,-4,-10,-7,1,-3,7,-9,9,2,-3,-2,9,-6,6,-4,1,7,-6,-10,10,-7,-1,1,-8,4,4,-10,4,9,-7,-10,-10,8,3,-4,1,9,10,4,5,-1,-1,-5,9,6,6,2,5,3,-10,-3,10,5,-4,-10,-4,-1,2,-4,9,-4,-8,-10,-8,4,-9,9,1,-1,-2,7,2,2,3,4,6,6,4,-8,8,-10,-9,10,2,6,-2,9,10,-7,-9,-6,9,-10,7,-5,2,-3,4,-2,5,-10,8,3,5,10,3,9,-7,4,7,-8,-5,-9,-6,-5,8,2,-7,3,-4,-5,8,-8,-3,8,2,-8,-10,-3,-9,-9,-4,-2,-5,4,-7,-8,-3,9,-9,-5,-2,7,9,8,8,4,8,6,2,-5,-9,3,7,7,8,6,-4,-3,5,-2,1,-7,-3,-4,-3,3,10,-5,7,-5,-3,-6,-6,-9,-2,-3,6,-4,5,3,9,-1,1,7,5,4,7,-4,-10,-5,1,-7,-10,-7,1,4,-7,8,-8,-5,-9,2,10,8,-6,-2,10,5,10,-6,1,8,4,5,1,6,10,5,-3,-9,5,-7,9,-7,-3,10,5,-1,4,-3,-9,-6,-9,8,3,1,9,2,-10,-6,6,-7,4,9,6,-4,3,4,10,-3,1,8,2,9,3,-4,-1,-9,9,-4,2,-1,-7,-6,-9,7,-3,-2,-9,8,6,8,-1,4,-4,6,-6,10,2,-10,5,2,4,-4,7,-4,3,2,-8,-3,-3,-10,-6,2,-8,-10,10,2,8,-9,-9,-9,5,-6,6,-7,10,7,8,5,-10,1,-9,-7,1,3,1,10,-3,-10,6,7,-5,-2,-4,8,-2,-7,2,-7,10,-10,-1,-8,7,-5,-5,8,9,-10,-9,-8,-9,-1], dtype = "uint32")#candidate|9380|(1008,)|const|uint32
call_9379 = relay.TupleGetItem(func_6413_call(relay.reshape(const_9380.astype('uint32'), [1008,])), 2)
call_9381 = relay.TupleGetItem(func_6415_call(relay.reshape(const_9380.astype('uint32'), [1008,])), 2)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
const_9385 = relay.const([[-1.686744,6.871790,1.296402,-2.042882,-1.278076,-8.595818],[5.634040,-8.461138,9.934339,-7.383187,5.888152,5.288632],[0.877734,-7.162724,-2.097068,-6.767531,5.543395,-2.239574]], dtype = "float32")#candidate|9385|(3, 6)|const|float32
call_9384 = relay.TupleGetItem(func_4118_call(relay.reshape(const_9385.astype('float32'), [2, 9, 1])), 2)
call_9386 = relay.TupleGetItem(func_4120_call(relay.reshape(const_9385.astype('float32'), [2, 9, 1])), 2)
func_6963_call = mod.get_global_var('func_6963')
func_6964_call = mutated_mod.get_global_var('func_6964')
call_9393 = func_6963_call()
call_9394 = func_6963_call()
func_6207_call = mod.get_global_var('func_6207')
func_6208_call = mutated_mod.get_global_var('func_6208')
call_9419 = func_6207_call()
call_9420 = func_6207_call()
output = relay.Tuple([call_9331,call_9357,const_9358,call_9379,const_9380,call_9384,const_9385,call_9393,call_9419,])
output2 = relay.Tuple([call_9332,call_9359,const_9358,call_9381,const_9380,call_9386,const_9385,call_9394,call_9420,])
func_9422 = relay.Function([], output)
mod['func_9422'] = func_9422
mod = relay.transform.InferType()(mod)
output = func_9422()
func_9423 = relay.Function([], output)
mutated_mod['func_9423'] = func_9423
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9465 = relay.var("var_9465", dtype = "float32", shape = (12, 1, 13))#candidate|9465|(12, 1, 13)|var|float32
var_9466 = relay.var("var_9466", dtype = "float32", shape = (12, 10, 13))#candidate|9466|(12, 10, 13)|var|float32
bop_9467 = relay.less_equal(var_9465.astype('bool'), var_9466.astype('bool')) # shape=(12, 10, 13)
uop_9499 = relay.asinh(var_9466.astype('float32')) # shape=(12, 10, 13)
func_5745_call = mod.get_global_var('func_5745')
func_5750_call = mutated_mod.get_global_var('func_5750')
var_9510 = relay.var("var_9510", dtype = "float64", shape = (390,))#candidate|9510|(390,)|var|float64
const_9511 = relay.const([[-8.181946,-3.015589,9.412759,-7.423632,9.670362,-8.205522,-6.135918,7.963034,4.661144,4.016263,7.528477,1.721757,-4.717828,5.386788,8.120187,0.045281,-8.092444,0.784374,-8.327939,4.203186,4.691237,-3.777501,-3.601648,8.549064,6.817923,3.888285,-3.466763,2.843924,1.304090,-6.793599,-4.558206,-2.071053,0.205384,-0.437931,-0.740766,5.042725,8.729118,0.548730,-5.750847,1.664983,-7.907347,-9.180669,-1.793982,6.460053,-5.057650,-7.202874,8.474968,1.935768,-2.101446,5.659759,8.263520,0.773069,-2.616868,-1.508006,1.769499,-5.325676,-4.095884,6.973741,-8.380893,8.656292,-8.625191,9.804867,-5.328439,-9.010981,7.325046,2.844200,9.057541,1.341755,-0.029539,-3.770518,-0.029495,6.798670,1.833928,7.380479,0.479345,-6.676902,-6.757964,0.524415,-9.911848,4.513267,3.447886,0.860022,0.778651,-2.241780,-7.776878,-5.759575,3.876490,-3.601765,-0.675099,7.265596,-9.438948,2.153729,6.053473,9.032664,-4.996389,3.371527,-5.634263,-6.507882,-7.430034,8.722599,1.858365,0.635585,8.344255,2.834738,2.666831,4.150658,-1.990770,-3.374259,1.747863,-6.900111,-1.211430,-6.961211,-0.511947,2.257868,3.774715,6.999655,-6.521631,-9.935847,-5.774020,5.938775,-7.664717,8.407056,4.168463,-3.931656,-4.548170,-5.054132,9.721929,0.590687,-0.294317,-7.802894,4.990749,-2.547088,-6.710573,1.248005,9.069065,-5.891097,7.258300,-0.595829,4.594618,2.618405,4.739225,-7.498246,-5.411052,-6.792093,-0.075315,8.580746,4.502327,1.933109,-7.177080,-9.010892]], dtype = "float64")#candidate|9511|(1, 150)|const|float64
const_9512 = relay.const([2.728428,5.882170,-9.819113,-7.822935,4.941488,-1.372233,-0.499696,-2.476719,8.979433,-3.887365,2.385339,-6.550315,-4.371235,5.057641,8.420143,-8.438247,2.592392,0.467452,-3.820756,0.822187,4.761156,-9.988209,1.792672,-4.497628,-9.502222,0.087182,7.207558,3.404953,-0.271523,0.776291,0.119711,-6.450505,-2.755934,-0.087427,4.310992,-2.831231,-8.464614,-3.557525,5.576506,-0.519108,8.682058,1.967192,-4.508655,-8.621056,-8.615967,-3.601262,5.754864,-3.336286,4.271209,1.508827,-5.206581,3.038198,-9.051063,-7.487273,-1.722506,6.831876,-9.011469,-1.943233,4.966360,-4.740973,4.737539,9.023554,3.331160,-8.371684,-3.972970,-6.937000,7.563101,1.332606,9.829513,4.769738,2.720314,-5.175096,1.510713,-8.333646,8.848171,-6.188481,9.684898,-7.737566,3.299544,4.854194,-7.512382,7.402614,4.256601,1.678623,-5.307952,4.726771,9.895432,-4.447508,-1.922052,9.149631,8.857647,-4.840734,0.891545,2.193549,7.342568,-0.124796,-4.384422,9.809019,4.236781,9.776413,0.031828,7.318815,-5.065909,-7.477380,-6.272536,-1.824842,5.692692,-2.985911,9.926028,-6.382119,4.118987,-8.399701,-7.222687,8.565902,-3.880933,8.972485,0.005206,-9.046083,-6.588504,7.217864,-7.283023,-4.772058,-2.890022,-9.799716,2.681787,2.696628,-7.737904,-4.091109,8.837220,-6.391236,-3.170414,-5.455433,-6.777706,2.871221,2.813847,2.820005,6.998710,1.117513,-1.995747,9.222342,-9.623450,-3.763001,3.680233,9.608615,5.042421,-3.042291,-9.743190,3.669066,-1.092320,4.160200,8.337794,5.156060,4.863698,6.312109,3.419878,5.145516,6.004377,-6.774508,-9.159418,2.810074,5.221798,-7.043510,-3.837138,-0.610708,-9.303226,-3.521963,-8.736734,-5.578369,9.067427,0.485894,2.090616,-8.945677,4.711183,2.203755,1.734878,1.570161,-6.885725,-3.769128,1.680014,5.849212,-4.798126,-5.651119,-9.557560,-5.749071,-9.553338,-1.020577,-4.892743,-6.370830,1.754917,-5.766324,-6.630454,1.920208,6.788596,-7.643840,-0.108802,-8.096594,5.150689,6.130467,-1.002648,3.835956,3.459284,-3.907904,9.555008,0.068559,-3.846583,1.866813,0.066663,0.060232,-6.697732,-3.364659,-0.462772,2.379447,6.432794,6.155290,1.370347,-1.743275,-4.272327,-4.772195,5.462989,-7.582153,4.781970,-6.329778,-4.142118,2.318262,4.221119,0.877631,6.014371,-3.062688,6.709558,-1.410947,-8.920889,7.232113,5.199273,-7.333450,-0.900150,-4.881773,-6.860592,-0.910255,-0.441101,5.830074,5.530694,2.185819,-9.635876,9.444623,7.917402,-8.746899,-2.328138,-2.699091,3.144963,-4.867483,9.148254,-4.577335,-8.514865,-3.172623,-4.740914,-7.889601,-5.451380,-8.114764,1.250418,-4.696261,9.010515,4.029554,6.908910,3.594715,-9.382820,-1.846379,-6.805844,-8.386389,5.502537,-4.059635,-7.858349,-4.941475,-5.433155,7.164619,-4.930360,4.430310,-7.400783,-7.676719,-1.643794,6.663174,0.529341,7.881666,-6.658488,-3.386959,-3.516126,3.973367,-6.384298,-6.308947,2.205803,-4.157115,2.819484,5.088415,-8.959162,2.874692,-4.931413,-5.172426,-3.805161,2.230855,1.505074,9.234310,-1.626324,-8.614954,-9.398653,-1.355130,3.608172,2.510219,-3.747362,-6.679507,-2.462595,0.524307,-8.384366,2.843056,4.635439,4.554212,-0.129889,3.401114,-3.104373,7.461074,-7.700136,-8.550382,8.704603,-5.819439,-6.662358,-6.088004,1.666440,0.752250,3.995107,-2.257243,-3.729915,8.534343,-7.532591,4.629607,8.050544,5.602727,-6.647678,4.638569,-1.971603,5.809211,-8.454164,9.358973,-8.291962,-5.025648,9.242884,-1.518301,-5.926126,3.155752,-7.528754,4.399322,0.409027,4.614198,-3.060485,4.022535,0.100201,-7.181541,9.157451,4.216183,-7.847446,9.641423,-1.404318,8.785596,-7.899743,-2.620678,-4.965355,-3.892076,-1.062642,0.323096,-4.692762,1.813163,-3.335025,8.373323,-3.197171,2.689847,-8.278672,-2.367563,-2.463353,-3.703036,-1.237811,-9.167568,-8.374064,4.987457,-5.361055,-3.861996,0.738977,-0.794012,3.339566,4.431436,-4.548384,-1.148115,-0.769355,-1.499707,4.471475,0.506830,4.912066,-9.499702,-3.499941,-1.149952,-3.805664,1.701625,8.320728,2.214014,1.595959,-8.380857,8.737783,2.931904,7.203541,0.562656,-6.955635,4.649329,-6.788245,4.140727,1.531522,0.424461,-4.113248,3.046351,6.263641,-7.231756,-8.107871,-6.919992,-6.047860,8.353061,3.123680,-0.362681,3.735450,9.195087,5.712281,-9.277299,6.426140,-0.940481,-2.870307,1.393767,1.637080,-4.547490,-1.792777,5.610361,-5.017175,-4.318918,9.729907,0.910189,-9.278781,-7.653765,-1.884269,-8.847537,6.587623,6.656752,7.641354,7.418451,2.030786,-5.313915,-3.337612,-9.480580,-3.808706,8.270543,2.875288,-4.354575,8.247244,1.148197,8.829744,8.098808,-5.007201,-3.864163,7.749203,-4.120129,6.689392,-3.602199,0.372839,6.578347,-1.348881,9.319811,0.261922,8.145918,5.783925,-2.193972,1.215399,5.095378,1.527434,4.954125,6.857952,9.860797,-0.863055,-1.040589,-1.914120,1.558035,-1.745057,-9.318619,-7.570341,3.033664,-9.135656,-9.669531,0.609302,2.036287,9.988820,-0.352033,3.154024,3.554202,0.025385,7.278916,3.902578,-9.005829,0.806779,-6.412354,5.568070,8.839301,5.963072,4.620907,3.340633,4.451616,8.452934,1.462303,2.087269,-6.703470,4.625127,-5.423934,-9.228634,-8.897128,9.004717,5.891709,-3.016501,-6.597327,-7.563916,7.653098,7.557786,-7.778854,-0.720002,1.791673,-3.770657,-5.529097,1.478280,9.060963,-8.561213,9.795538,-5.322053,-8.931851,-3.421178,-5.267581,-9.675661,-4.138338,6.500392,-1.263159,4.250885,0.777569,2.952330,8.088988,3.212548,-0.950613,-8.812799,8.457131,-7.513880,-0.768729,4.854762,6.624856,-1.753209,2.476527,-1.827139,1.913204,4.067287,0.412953,-3.997873,7.476531,7.358320,8.657885,4.559779,-4.830293,-7.048427,-7.708377,-3.061722,8.523018,-8.837722,-1.047206,-5.535284,-8.623917,-5.890112,-5.538245,-0.477600,-7.087737,3.507441,4.898631,4.687655,-4.002746,-4.233546,0.066243,-8.270865,0.913944,1.223929,3.157729,4.007573,4.536685,-7.290567,9.831441,5.590318,-4.151132,5.745953,9.932507,-7.395118,8.559023,8.252922,7.948059,4.851517,-0.226152,-2.165973,0.985764,3.660897,2.473832,-9.168691,-1.826337,7.421825,3.350592,-3.342994,4.033840,-0.633525,-4.258109,3.201975,-0.928035,-8.327786,1.306013,-0.939683,4.198590,0.757636,8.148045,9.509920,6.422024,6.569704,0.170091,0.315451,-5.278579,7.531820,3.517897,-6.812048,-7.866284,-1.971107,7.909759,-6.758273,-0.940074,9.468964,3.756050,7.373835,5.294024,1.120277,3.245308,5.524292,2.399820,-5.262970,2.508071,-0.709522,3.470929,8.049036,4.565371,6.507993,1.413050,-4.000689,0.460960,1.036889,-3.007576,-7.564901,-5.695327,5.617721,-1.031403,-0.971358,-3.053857,1.186141,-7.983725,-9.050724,-5.630176,9.006394,-4.227245,5.729325,-5.572422,1.037299,3.352061,-0.846120,2.080347,8.472767,3.680056,-0.705577,-2.364719,8.625885,-5.451932,7.234532,-2.776232,2.906072,-9.948959,-5.591722,3.440489,7.385617,7.366038,-0.009589,5.472349,1.623734,-4.589607,-0.975681,1.902945,5.512741,3.630094,9.314946,7.437285,-9.745976,1.900611,-1.464581,-7.622148,6.781228,2.789531,4.693469,-9.608935,5.941084,-1.489173,0.751820,-6.918402,4.490621,3.513621,0.032017,3.669991,-3.651744,-1.565295,-0.660980,-7.273174,0.638907,8.622033,-2.063969,1.669658,-5.427218,1.370722,3.373122,-4.702203,9.208151,6.452867,9.319841,7.388469,5.918172,-7.908567,-2.201857,-3.546568,4.206439,-3.309894,7.530120,9.225448,6.046854,5.947530,-8.758156,-8.860875,-5.242885,-3.565749,-2.381006,7.374132,-4.607427,7.035654,1.321706,-1.151277,-2.883323,-6.378972,-9.097591,5.764818,8.576688,-9.077675,0.991696,3.150994,5.938745,7.576436,6.474626,3.966955,-2.453735,6.390659,-0.650427,-8.616718,-6.927964,-4.739730,8.200256,3.538318,7.203901,-0.856164,-0.273597,-3.344604,-3.665950,0.110949,-0.408961,0.657433,-0.152512,-2.879156,-6.615412,9.396304,-0.802852,1.308116,0.943017,-9.514264,-3.299954,6.524365,-7.975519,-7.784418,0.774733,8.141886,9.500153,6.705305,1.991353,-9.196675,-3.690464,-0.205680,-6.198101,-7.103723,-5.062086,-5.117394,-0.481791,8.499651,2.382862,0.720092,-0.962155,-3.604465,9.550959,7.991089,-1.328395,-3.672196,2.858535,6.240903,-8.612606,4.377737,-2.141732,1.291234,-6.184014,4.958956,8.046927,-5.759563,0.337932,6.505804,-7.372502,5.981109,-4.085545,-1.639142,3.174834,6.607294,0.799942,-3.167599,-1.385715,-3.159861,0.552670,-8.577879,-3.345925,-4.739489,-4.800111,-0.135613,-0.292681,1.300336,4.287903,-3.345260,2.257293,-8.507027,-4.004418,-8.191314,5.851142,6.370967,-4.590492,2.418243,7.398860,4.956299,1.284017,-2.846558,8.807803,-1.036139,3.838103,9.509756,9.919058,-6.032327,9.642684,-2.547238,2.115175,7.485692,-3.021641,8.968622,-2.111382,2.850974,-1.071810,2.638818,3.344142,3.194374,-4.761455,2.857330,-8.537735,4.449091,-2.843079,-1.721586,-1.406132,5.419307,-8.788214,-4.691688,8.478062,-1.144996,2.794356,-2.906298,-4.707967,-1.113045,-2.375669,-7.134970,1.273760,-6.013218,1.940028,8.134799,-0.676084,-5.807880,6.411563,8.553359,-6.008940,3.554301,0.330321,-1.338127,9.582950,-8.948735,-0.920811,-8.412524,7.587161,7.233346,-5.182497,-3.937568,-4.468912,1.726850,5.436066,-8.280530,2.121161,2.863892,2.043412,-5.058628,-2.244628,4.135370,9.979611,-9.103436,-1.411533,0.028659,5.138708,-5.111962,8.061368,7.708810,-6.598855,-5.291511,6.661682,6.463617,-7.956850,9.721502,-6.031054,9.151246,5.893435,-2.446379,-5.396523,-4.729563,0.104706,3.329512,-9.859318,3.619134,-1.539577,-4.161107,-3.535792,7.926103,0.994078,6.334992,5.551499,8.286529,4.193772,-7.487802,-2.624142,6.252771,7.974333,-5.680521,1.622129,2.854522,0.615449,-6.998592,7.925821,-4.548741,-5.552795,-7.850635,2.263198,-6.643468,-6.332813,-5.110192,1.096088,-9.086603,-8.899136,3.117486,5.393773,0.684873,-6.663651,-4.224312,3.666218,4.385040,-0.789567,5.066954,2.898606,-0.481265,0.197617,-3.712929,-6.494869,3.860136,0.048834,4.314237,3.129073,-1.934675,-6.484776,8.488317,2.367856,3.476075,2.158589,6.778675,5.373879,-0.387889,-9.302098,8.954592,3.553863,8.326274,9.538232,3.834465,-1.652261,8.157075,-5.637138,-0.570733,8.164480,-6.940058,9.473838,5.136055,4.544714,4.464594,0.186485,9.677387,5.298213,1.310189,2.183149,-3.607102,-7.798040,-7.032368,-8.713969,3.505108,-1.945279,-8.319309,1.443432,-0.849300,7.012423,6.237124,5.178349,-4.092219,3.909849,7.132693,-2.029800,-2.500506,2.496924,-2.707389,-5.529623,1.940881,1.226064,-5.082879,-5.353515,9.169724,-0.484663,-0.245082,5.937499,-8.201636,-7.592388,7.668808,1.260962,-6.201252,-3.764855,1.113139,-8.398205,-5.420783,-7.113683,-0.911271,3.591535,9.676758,-0.210063,6.462856,-0.746641,7.451172,-1.964536,4.363993,-8.359105,-8.889087,-8.570158,2.216027,7.198288,-4.925151,-6.343398,-2.937589,7.177377,3.605997,2.698610,7.758996,4.181740,-5.993882,-5.130665,1.147950,3.623921,2.466279,7.681592,-0.891882,-8.975300,3.015678,-3.259733,0.019907,5.639994,7.274829,7.837649,-3.178459,2.657384,-9.631923,-1.328841,9.448849,-8.872583,-6.685897,2.395189,-1.344334,4.852262,0.483299,9.280791,5.920759,0.977215,7.262964,-0.098939,2.800371,-7.028571,1.556344,-0.256137,9.594762,2.567137,-2.747020,-8.675752,6.564582,-2.298868,6.927461,6.296419,-6.781517,-0.907093,1.039949,7.722581,-7.317257,1.026377,9.873297,-1.134741,-4.762628,-2.486766,9.591331,7.896824,-3.936850,2.320891,8.667143,9.482568,6.911733,9.338124,-5.543419,-2.949683,-3.855257,-9.959495,6.964482,-0.980857,-5.426229,-4.669050,-4.651394,-0.385133,-2.287540,-6.710174,-0.943648,1.857203,7.633690,4.701292,-0.048295,1.867729,1.346271,-1.867761,-8.370877,-1.340464,7.042892,-8.942993,-1.777167,-8.893502,-9.600957,-5.077093,-6.593006,3.034607,-0.829282,0.969221,-7.189189,5.339299,-7.689519,-4.495174,1.020008,-1.614256,7.436854,-2.157571,4.860090,-2.282514,3.978716,0.220752,6.932252,-0.484778,4.549977,-1.471917,-3.944054,0.286522,6.720181,1.174559,-3.164064,4.086944,5.548815,0.445425,-0.636449,-3.855090,-4.063561,-0.141202,-5.932304,2.343088,-9.947540,2.795268,8.575350,-0.692961,-5.534169,0.153681,0.498112,4.651985,-6.197268,7.672918,-4.142024,7.779369,2.540940,-6.043959,-0.006549,5.803134,9.842050,7.648957,4.320057,5.071439,8.028207,-0.801002,4.841562,9.528568,-9.172039,4.829516,6.108475,7.077124,-9.632573,-6.437964,4.841675,2.588922,8.434611,-5.302853,-2.963583,-6.640124,-4.977477,-5.939703,-5.507361,-4.538800,4.059561,-7.352670,-2.252304,2.654846,4.037543,6.665581,-8.696052,-1.169504,5.038509,-9.338918,-6.539189,0.128688,-8.629879,7.046057,-9.091004,1.980552,9.029496,-1.210845,-1.665345,-7.992970,3.504597,-7.910354,-2.608619,8.650698,8.290659,-0.988673,7.780820,7.517621,4.415014,-1.835789,-0.874513,1.256396,1.108406,0.486729,-9.487007,-3.888556,8.383558,7.958451,7.204714,8.996584,-8.699865,-4.976483,4.193558,5.574521,-5.292179,-8.980750,-4.320200,-0.590388,1.246383,6.820815,5.169790,-3.319332,-5.378875,2.995774,-4.943641,0.933936,-7.998565,-8.569371,0.110176,-0.792019,-1.994578,-0.838181,7.562808,-5.402971,-3.582498,-9.742697,6.796286,-0.488684,-6.040415,4.209507,-1.217707,1.533390,0.572349,-2.987010,-2.087223,-3.915179,-1.861874,0.093106,-5.980900,-8.935797,7.214851,-4.582466,7.263889,-0.596223,-2.633308,1.491443,-0.923245,8.051174,-9.751231,-0.768455,2.654921,1.812696,5.739668,8.882424,0.019129,-5.318482,-7.995406,0.293196,2.490067,0.427935,-9.046448,-8.962423,6.650548,-5.353815,-2.869235,-1.553077,9.894418,5.096336,-4.588784,-5.809167,-3.916957,-4.335026,-4.631704,8.534818,-4.089354,5.662629,9.651802,4.369640,-6.029796,-6.698757,5.879985,-0.364513,2.673315,7.889005,-4.590631,4.083141,6.128761,4.690438,4.971087,2.347814,8.806463,-6.988100,4.936412,0.977119,1.447423,-6.261690,2.138015,-3.277360,-2.251183,-5.258334,0.837310,0.144712,-0.984020,-1.369085,6.628131,9.137468,0.693754,0.277411,6.673750,-2.879080,9.179432,6.776023,0.229684,5.055814,-6.703188,-9.792580,2.177009,-6.720054,-7.365105,5.730244,-5.450028,-6.921575,4.082101,-1.078124,-0.389946,1.585370,8.049475,-6.990831,-9.590129,-9.155334,-4.480378,9.549961,5.460304,5.551877,-9.501258,4.348062,2.862887,-6.083858,-8.072697,7.757791,4.096096,-1.539130,-2.667756,7.838456,-2.556465,3.958029,-2.697316,-9.553046,-1.254373,7.920521,-2.484514,1.471222,-9.859827,-8.207130,2.260570,-5.552685,5.579879,4.727679,5.425768,-1.235470,8.797552,-2.581015,-6.034073,3.843724,-9.445338,-6.764480,9.533439,-7.406087,2.763745,-4.221239,0.782775,-6.865148,7.147990,-7.753940,-7.861499,-8.103044,-6.244022,-2.346516,8.321549,8.694314,-6.727154,1.297037,1.421688,-5.643181,-9.963073,6.027701,8.338223,-2.410431,-5.318592,8.437672,-8.434799,-1.731817,8.677221,3.359528,-6.654256,-2.157050,-0.943607,-1.414904,-5.684638,8.786331,-8.873566,-9.295454,-1.453810,-6.829905,0.634625,0.833692,-4.277170,-1.976564,-1.214961,-7.708748,-3.082325,-0.232767,-2.636659,-9.065910,6.054276,-6.319377,5.935754,1.113528,5.323521], dtype = "float64")#candidate|9512|(1500,)|const|float64
var_9513 = relay.var("var_9513", dtype = "int64", shape = (312,))#candidate|9513|(312,)|var|int64
call_9509 = relay.TupleGetItem(func_5745_call(relay.reshape(var_9510.astype('float64'), [15, 2, 13]), relay.reshape(const_9511.astype('float64'), [150,]), relay.reshape(const_9512.astype('float64'), [1500,]), relay.reshape(var_9513.astype('int64'), [312,]), ), 5)
call_9514 = relay.TupleGetItem(func_5750_call(relay.reshape(var_9510.astype('float64'), [15, 2, 13]), relay.reshape(const_9511.astype('float64'), [150,]), relay.reshape(const_9512.astype('float64'), [1500,]), relay.reshape(var_9513.astype('int64'), [312,]), ), 5)
func_6622_call = mod.get_global_var('func_6622')
func_6625_call = mutated_mod.get_global_var('func_6625')
call_9516 = relay.TupleGetItem(func_6622_call(relay.reshape(call_9509.astype('float64'), [1500,]), relay.reshape(var_9513.astype('int64'), [312,]), ), 0)
call_9517 = relay.TupleGetItem(func_6625_call(relay.reshape(call_9509.astype('float64'), [1500,]), relay.reshape(var_9513.astype('int64'), [312,]), ), 0)
bop_9521 = relay.bitwise_and(uop_9499.astype('int8'), relay.reshape(bop_9467.astype('int8'), relay.shape_of(uop_9499))) # shape=(12, 10, 13)
output = relay.Tuple([call_9509,var_9510,const_9511,const_9512,var_9513,call_9516,bop_9521,])
output2 = relay.Tuple([call_9514,var_9510,const_9511,const_9512,var_9513,call_9517,bop_9521,])
func_9533 = relay.Function([var_9465,var_9466,var_9510,var_9513,], output)
mod['func_9533'] = func_9533
mod = relay.transform.InferType()(mod)
mutated_mod['func_9533'] = func_9533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9533_call = mutated_mod.get_global_var('func_9533')
var_9535 = relay.var("var_9535", dtype = "float32", shape = (12, 1, 13))#candidate|9535|(12, 1, 13)|var|float32
var_9536 = relay.var("var_9536", dtype = "float32", shape = (12, 10, 13))#candidate|9536|(12, 10, 13)|var|float32
var_9537 = relay.var("var_9537", dtype = "float64", shape = (390,))#candidate|9537|(390,)|var|float64
var_9538 = relay.var("var_9538", dtype = "int64", shape = (312,))#candidate|9538|(312,)|var|int64
call_9534 = func_9533_call(var_9535,var_9536,var_9537,var_9538,)
output = call_9534
func_9539 = relay.Function([var_9535,var_9536,var_9537,var_9538,], output)
mutated_mod['func_9539'] = func_9539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7588_call = mod.get_global_var('func_7588')
func_7590_call = mutated_mod.get_global_var('func_7590')
call_9541 = func_7588_call()
call_9542 = func_7588_call()
uop_9546 = relay.log2(call_9541.astype('float64')) # shape=(15, 2, 13)
uop_9548 = relay.log2(call_9542.astype('float64')) # shape=(15, 2, 13)
func_2320_call = mod.get_global_var('func_2320')
func_2324_call = mutated_mod.get_global_var('func_2324')
var_9553 = relay.var("var_9553", dtype = "uint16", shape = (90,))#candidate|9553|(90,)|var|uint16
var_9554 = relay.var("var_9554", dtype = "uint16", shape = (180,))#candidate|9554|(180,)|var|uint16
call_9552 = relay.TupleGetItem(func_2320_call(relay.reshape(var_9553.astype('uint16'), [1, 9, 10]), relay.reshape(var_9554.astype('uint16'), [2, 9, 10]), ), 4)
call_9555 = relay.TupleGetItem(func_2324_call(relay.reshape(var_9553.astype('uint16'), [1, 9, 10]), relay.reshape(var_9554.astype('uint16'), [2, 9, 10]), ), 4)
output = relay.Tuple([uop_9546,call_9552,var_9553,var_9554,])
output2 = relay.Tuple([uop_9548,call_9555,var_9553,var_9554,])
func_9556 = relay.Function([var_9553,var_9554,], output)
mod['func_9556'] = func_9556
mod = relay.transform.InferType()(mod)
mutated_mod['func_9556'] = func_9556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9556_call = mutated_mod.get_global_var('func_9556')
var_9558 = relay.var("var_9558", dtype = "uint16", shape = (90,))#candidate|9558|(90,)|var|uint16
var_9559 = relay.var("var_9559", dtype = "uint16", shape = (180,))#candidate|9559|(180,)|var|uint16
call_9557 = func_9556_call(var_9558,var_9559,)
output = call_9557
func_9560 = relay.Function([var_9558,var_9559,], output)
mutated_mod['func_9560'] = func_9560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7445_call = mod.get_global_var('func_7445')
func_7447_call = mutated_mod.get_global_var('func_7447')
call_9635 = relay.TupleGetItem(func_7445_call(), 0)
call_9636 = relay.TupleGetItem(func_7447_call(), 0)
func_6121_call = mod.get_global_var('func_6121')
func_6123_call = mutated_mod.get_global_var('func_6123')
call_9642 = func_6121_call()
call_9643 = func_6121_call()
func_8874_call = mod.get_global_var('func_8874')
func_8875_call = mutated_mod.get_global_var('func_8875')
call_9656 = func_8874_call()
call_9657 = func_8874_call()
func_6207_call = mod.get_global_var('func_6207')
func_6208_call = mutated_mod.get_global_var('func_6208')
call_9665 = func_6207_call()
call_9666 = func_6207_call()
output = relay.Tuple([call_9635,call_9642,call_9656,call_9665,])
output2 = relay.Tuple([call_9636,call_9643,call_9657,call_9666,])
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
func_7965_call = mod.get_global_var('func_7965')
func_7966_call = mutated_mod.get_global_var('func_7966')
call_9698 = func_7965_call()
call_9699 = func_7965_call()
func_2064_call = mod.get_global_var('func_2064')
func_2068_call = mutated_mod.get_global_var('func_2068')
var_9705 = relay.var("var_9705", dtype = "uint32", shape = (128,))#candidate|9705|(128,)|var|uint32
call_9704 = func_2064_call(relay.reshape(var_9705.astype('uint32'), [4, 2, 16]), relay.reshape(var_9705.astype('uint32'), [4, 2, 16]), )
call_9706 = func_2064_call(relay.reshape(var_9705.astype('uint32'), [4, 2, 16]), relay.reshape(var_9705.astype('uint32'), [4, 2, 16]), )
func_5919_call = mod.get_global_var('func_5919')
func_5923_call = mutated_mod.get_global_var('func_5923')
var_9709 = relay.var("var_9709", dtype = "float32", shape = (900,))#candidate|9709|(900,)|var|float32
const_9710 = relay.const([7.040240,-3.485444,4.944425,-2.315529,-3.452432,-3.877314,4.064387,-7.239784,-9.767147,3.632882,0.668659,1.242943,5.609998,-3.327089,8.767825,-5.885848,-6.043335,3.764105,1.589852,-3.951197,5.061031,-0.750051,8.146281,7.486526,2.788632,3.950971,8.007203,6.987620,2.130509,0.877754,9.710035,1.298568,-3.512971,9.121953,8.968714,-8.762517,5.626754,6.767570,4.353860,-9.574280,3.878162,1.966568,-4.468044,-9.516637,-6.318179,-9.152322,5.929973,-2.920450,-2.003349,-8.991560,7.037923,-8.683409,3.601597,-2.755581,5.033676,2.832042,-4.732090,9.484611,8.608230,-3.489588,8.923479,7.653846,2.310708,2.502406,-9.481903,6.106735,-3.607834,-9.127492,4.979306,-4.227758,4.200165,9.908076,3.959017,-0.202196,-4.472984,-4.608074,-5.040020,6.586301,9.099308,7.653012,-7.881730,-4.816791,8.871508,-1.186168,8.874314,4.828539,5.444162,-0.979298,2.220943,9.104084,-7.287804,3.345726,-5.283785,-0.364725,0.478782,7.291547,-1.817775,-3.197377,-0.530389,-2.570848,-2.427289,-7.714672,-3.167890,-0.606540,6.226262,-2.708399,1.990817,-1.994743,-9.066594,-4.999018,0.705391,8.168549,3.061686,0.475943,-0.956735,1.128022,4.257042,-8.628461,-8.106606,4.524539,6.770176,4.509529,3.389292,-2.447961,-3.690518,-4.923399,-9.250883,3.877423,6.860659,7.517159,-2.073541,-2.821826,-1.516530,-3.236848,1.642630,-6.418128,7.916655,-4.218563,-8.061617,-7.143453,3.419874,-0.297589,-1.683332,6.355753,-5.987099,2.380789,7.738940,-4.713858,7.206922,-2.535113,-6.246844,1.646848,6.432515,-4.964830,-8.338765,-1.229727,2.456058,3.142887,0.350935,-3.488964,7.629585,-3.319029,0.581763,-9.288499,8.127173,-9.124487,5.003858,0.947693,1.776079,-5.428743,-7.843305,5.349817,7.413091,6.135551,5.466371,-9.524245,-8.037320,0.705239,6.433636,-2.667688,-3.693502,-4.622957,-2.994210,-1.479511,-6.030288,6.056318,-0.305420,-6.377090,3.391373,-3.816256,5.557586,8.360538,6.249899,-4.473023,-1.844246,-8.825340,1.608209,-1.440274,-6.585090,1.820830,-4.787992,-0.421198,1.139166,-5.865423,-7.815917,5.137332,-1.695331,6.211198,5.307995,-2.912158,-5.941769,-7.372499,-6.160400,0.069997,-2.644798,5.875069,5.095264,9.921952,-1.920994,7.397452,-6.233762,2.175197,9.558655,-2.669662,-0.167975,-3.310552,8.817001,-1.597186,-5.313280,8.143471,-2.911823,9.779879,-6.294277,-4.482783,-5.248267,7.465905,-3.242993,5.020758,-5.647885,-5.815154,9.121778,4.293850,3.342709,-2.832555,-4.369554,-6.038796,-0.877848,-4.820752,-3.699725,3.876380,8.467473,5.893102,5.428727,1.820640,0.427675,-8.201576,2.020150,6.066078,3.949004,-0.616115,1.980821,-4.566797,-8.513820,-3.527582,0.170270,1.094893,6.091990,-1.661845,-6.800206,-0.657374,7.463982,-0.885135,-2.323575,-8.285813,9.896914,6.542136,7.707099,-0.826220,1.294451,9.768360,-5.057960,1.944004,6.025078,1.923849,6.288310,1.897259,-0.838581,9.550727,-9.284518,8.974596,-4.321403,-6.514798,-7.284386,0.161922,-6.947720,2.205617,-6.967790,-9.257879,-5.461866,0.787988,7.626375,0.254651,-0.898070,-0.497919,-9.537077,-0.511108,5.009171,-2.702031,5.610765,7.480625,-2.527054,-5.075789,3.205726,8.718502,-9.257022,6.901394,8.791085,-0.120715,-9.760483,-0.659389,-2.578539,4.660757,-8.692231,1.150049,-4.457659,6.141586,2.284446,8.615976,-0.596059,8.238101,9.801321,-2.102007,9.195225,-7.370211,2.568818,-4.730280,4.071907,0.581436,8.927374,7.172062,2.700966,5.719922,-0.244543,0.073935,3.774715,-5.499307,-1.765301,6.907318,2.923926,1.664266,9.130994,-2.047566,0.626726,-8.280363,-1.368802,-6.226983,-2.331049,4.587708,-0.696613,3.637519,4.950134,-1.240506,-9.277273,8.276172,1.996460,-8.171617,-5.275057,2.174245,8.839092,-5.485110,8.175383,2.749452,-4.220944,0.251412,-0.191700,-2.720498,-4.994226,8.663271,6.697855,-7.517622,5.174767,0.184198,3.218428,5.693879,-1.279082,-6.352501,1.318540,7.209292,-3.133015,-5.227964,8.653570,-8.819862,-3.802451,-4.340964,-8.831156,-5.085964,3.599201,9.230614,1.409305,6.124295,8.971434,3.318539,-8.945472,-9.392487,8.122998,2.319318,-8.232879,-6.215619,2.296274,-2.871338,0.763320,2.008447,-5.021300,6.076558,3.505492,2.431746,7.231971,9.779693,7.619168,-9.453508,7.972888,2.986641,-0.125721,-1.548180,-8.696245,6.805823,3.169973,-0.428702,-3.767931,6.250581,7.077106,-0.838140,-3.546522,-2.967450,1.182489,-5.122355,-5.138034,-8.840045,-0.030101,-9.795236,5.139640,-3.836715,-9.953375,-4.731186,0.899492,-8.725901,-7.994658,7.730537,3.380889,-9.362251,-8.511045,3.652081,-6.739423,9.503800,-7.173678,6.390876,-4.594335,-1.964082,9.096387,0.561909,8.133219,7.134694,-7.572207,-6.535404,-0.449041,-1.426314,2.820928,3.084074,-7.364738,-4.936528,-4.968674,-6.987819,-5.302367,9.494408,-1.424346,-0.410784,-7.263178,6.623466,-9.123389,-8.476091,4.931216,1.870482,-0.532269,-9.365960,-1.018255,6.600051,9.129785,6.448922,7.900635,0.572537,5.138197,4.868330,8.212055,-6.145241,-9.730197,-8.230002,7.845277,-8.753356,-4.192467,-4.498145,-2.656928,6.773260,-8.279109,0.969504,6.227477,9.820922,-1.871652,-4.506851,9.472227,8.056796,-5.349454,0.290761,2.674779,1.553601,4.848781,-8.438641,-4.153214,1.644009,-6.058500,-7.742461,3.548565,-6.973215,-5.053083,1.842616,3.526128,2.694009,-4.260885,-5.280338,-6.789606,8.452822,9.065933,4.147091,7.325258,-4.530474,3.089569,7.471203,-7.215691,-9.377596,-5.310138,6.510482,-4.168153,2.702381,8.949251,0.799990,-6.168646,1.852045,-0.667578,0.965634,2.592001,-7.024952,-2.303330,5.161809,6.482595,7.591959,8.920126,-6.999268,8.060059,-7.520254,4.406243,-6.331531,-4.908540,4.703681,3.972738,-3.094090,3.262444,6.581217,-4.319768,-6.719803,0.518719,-9.656929,-2.072843,-1.451866,-0.693064,8.141833,-5.288101,3.646579,5.012893,-1.840838,3.953546,-0.194592,2.756033,-3.322772,-4.833479,0.063854,-6.812029,9.846300,-6.800407,-7.438624,-2.594945,-6.782001,-3.413420,-5.353822,5.055421,-3.752482,1.393677,9.664921,-1.718263,9.726935,-0.239037,-6.520353,-3.635636,-9.425784,-9.320551,8.598382,-1.101739,9.467393,-8.778871,-7.017945,-7.484818,-0.966675,2.177278,-3.862824,-8.661895,2.624174,1.788224,0.235505,3.476495,-9.705961,1.513593,-9.702276,-7.423101,-6.178660,7.772313,-5.146724,5.225029,-4.113806,-1.970757,-2.182936,-8.989400,2.503163,-5.585712,4.307356,-2.476824,7.566368,6.101979,6.721254,8.412284,-3.280300,4.863054,3.543205,-2.965452,4.311618,-7.939153,6.662599,1.913069,-9.011955,9.936749,2.503116,-1.617391,4.933143,8.872324,8.408330,-4.482288,0.280887,-8.163495,-0.659072,-8.575494,5.738431,-0.449200,8.293453,4.632889,3.072805,6.068254,9.485595,5.435975,-8.276975,5.623594,8.755662,7.351577,3.509981,7.607748,-5.928559,-8.012293,3.342573,-2.337681,-5.880474,-9.691508,4.397023,8.259597,0.567066,0.047490,6.633601,9.712264,1.910303,1.048973,-5.560238,-3.263624,5.248215,-8.883597,4.220372,1.519292,1.229582,5.108440,-8.663988,8.136130,4.734966,4.008451,7.762351,-6.029773,5.858059,-6.022171,-8.640075,9.803008,6.030618,-8.702303,-3.228944,-6.251965,-9.232757,-2.425916,-1.016288,-5.949492,9.768450,-1.703774,2.307343,4.934511,9.787148,-0.876907,-3.824625,3.382365,-9.943866,3.585180,1.651573,-5.969989,7.055481,-0.111847,-5.571011,-0.463216,-5.044275,-4.395795,1.186074,3.694315,8.751949,-9.929731,6.891624,1.153977,-2.905996,-5.048251,2.294597,9.266232,-2.239279,-5.931030,-3.065005,-6.713526,-7.345778,-9.102176,-1.032777,-9.880825,-6.709038,7.630501,-5.217116,5.305170,0.734952,-2.576319,-2.256186,-3.978655,-2.517319,4.654634,7.765861,0.069961,-2.077322,4.609859,5.515396,3.494633,-4.814418,8.701548,5.115118,7.500734,7.794478,1.930338,3.118457,-9.294209,2.288031,6.689904,3.265579,-7.984296,-8.884215,-9.508735,3.277786,0.226684,-6.963459,-3.286243,8.344863,0.079726,2.521580,-0.405477,-9.762411,-3.984881,-1.075885,-8.529622,5.200837,-1.914868,-7.026070,0.603347,-0.481897,0.756770,-1.592047,-6.398752,-8.731360,-4.172848,0.741439,-4.983328,1.348112,9.310693,-1.532619,0.694098,-9.429594,-7.813415,-4.771773,-3.080272,-2.024376,7.649062,1.330309,9.190759,8.025492,6.514520,-8.379558,-2.837565,1.888873,-0.515027,1.030038,6.481492,1.295178,-8.760780,0.079867,-8.197385,1.417835,-7.995892,8.434174,-7.345702,0.408770,8.046783,2.306444,4.195471,7.079191,0.304364,2.330620,-1.418366,-5.066210,-1.403448,9.517446,2.833862,3.859927,9.189983,2.949620,1.053552,-9.446864,9.127208,6.481318,-4.870234,-1.600571,5.715516,-1.278611,-6.496223,2.124457,-9.148502,9.385877,6.121410,-3.923881,6.998409,-5.589429,-2.992889,-1.022757,-2.070773,4.214915,-4.115499,-9.452172,9.000253,-7.405996,0.772201,7.257384,-6.110183,-3.405933,6.227804,5.138479,-1.965709,5.123431,-2.273773,-2.231462,7.601577,7.111162,5.310955,-4.529706,-8.338533,-6.406218,-7.130995,3.873300,-6.872318,-7.020683,-0.652395,9.434746,2.569772,-6.426523,-1.613606,-0.728061,-9.488900,4.489140,-1.295960,-4.807551,-0.761303,-6.495294,-8.665154,-6.688154,0.229124,-4.080082,-2.123218,0.266436,6.569278,1.008193,-3.374385,8.630991,0.097248,5.314032,-9.969138,-0.094268,-9.584847,1.555309,-0.918102,-1.135487,-0.556591,-9.086354,-0.120099,-2.205047,1.730000,6.951607,-6.558117,-2.657952,0.654248,8.777424,5.558315,5.310664,-3.304547,7.387511,-0.630267,6.764056,-5.153335,1.310320,7.406110,-9.345464,5.293301,-5.007016,2.382554,3.475709,-3.053973,-8.809671,-9.594612,-0.617205,9.904495,6.424781,4.937375,-3.376598,-5.355342,-4.709092,-4.612179,-0.613214,-1.609898,7.847272,4.156166,-6.501955,9.130084,-3.781122,-9.371152,-5.508963,-9.658313,3.115021,-5.672435,1.847549,0.564532,-5.493949,7.103008,5.215181,-9.442142,2.840343,9.253668,9.265538,-7.838135,-3.114612,-6.858470,-4.525304,7.446848,-1.334164,-0.570326,-3.148805,4.321350,4.153272,-4.187094,-5.816132,3.247339,-9.102799,-6.889625,7.500372,6.641608,7.780198,-3.615045,-0.055837,-0.438768,-7.324818,5.455555,-4.484047,7.246333,7.946950,6.114489,-4.071268,9.227936,6.660184,0.688965,-3.469160,2.005073,-7.592749,-3.084549,3.303065,-6.840667,9.140941,-5.582507,-2.441715,3.859008,6.564019,-4.363203,0.846861,3.650752,0.240143,3.379765,0.155644,0.898763,-3.394319,3.019883,-8.956368,3.802592,8.273086,-8.059079,-5.275929,2.430492,-7.617979,6.385272,8.748912,-6.651270,7.750787,-2.744543,-9.154229,0.664909,4.337599,-3.631726,-7.142083,9.674293,-9.043401,4.211970,2.488670,-5.650142,-8.290440,5.606751,-3.673968,-8.167089,7.445190,1.638691,3.732368,3.255752,2.824583,-5.561994,7.704761,5.038498,4.396727,-7.108553,3.911181,-3.901000,0.485165,6.030816,-0.080354,9.683123,-9.763071,1.681022,2.130006,8.133934,7.125778,-8.059446,1.948981,-8.080015,8.025610,-4.451945,7.874113,-3.126096,-4.874900,8.757930,-5.482234,6.740258,7.654805,-5.492595,5.264132,2.744677,0.229238,0.368083,8.637399,-9.884061,3.398564,5.190391,2.566274,5.648411,6.541075,-1.099278,3.670651,-5.445870,1.469088,-3.575507,-4.429580,1.501825,8.076700,8.697351,-1.584664,6.963021,-1.865055,-5.700029,1.307367,3.232239,-7.427155,-9.074319,9.089092,-5.961299,3.059307,3.838268,-0.455949,3.976238,-6.051117,-9.325783,-1.886845,-9.623643,-2.422364,5.272900,-8.011449,-6.176081,-4.068049,-6.769409,-5.733047,-0.206534,0.126047,8.896015,-8.028238,-9.345660,3.624467,7.245518,-8.821953,-7.271525,7.147662,-3.945669,2.435607,-0.939015,5.485181,0.041514,-2.237092,9.968244,-3.837415,3.978352,-4.227825,6.604626,7.267825,6.602841,-2.532852,-7.306931,0.971665,8.304131,-4.305915,7.569789,-5.815610,9.970611,-7.410545,6.514006,5.616650,-9.890934,-4.032704,-6.478955,-8.698676,0.266273,7.096181,-8.348307,2.782775,8.073770,-4.743438,6.420988,-7.242727,5.646514,-1.416745,8.928329,2.526803,4.695626,9.273957,5.301303,3.853044,-3.733447,7.869468,-4.800127,-9.020709,-8.464990,-8.326028,6.323684,-0.618215,4.240847,9.878793,-8.268732,-0.697016,-8.851904,4.052835,-8.113782,8.222110,-1.278909,0.555102,9.814696,-0.434126,-9.536177,7.812183,4.246535,-5.033090,-5.048029,4.101941,4.794808,-7.215311,0.880825,0.035989,0.883840,-9.270326,6.444718,-1.950057,8.477628,-6.575349,4.054636,-4.264207,9.127653,9.815712,-0.730796,3.871123,8.354700,-3.661623,5.025627,-3.113562,-1.045878,-5.523524,-6.927598,-3.600439,-2.921816,-2.985829,-9.133963,-7.853005,5.331006,-2.461933,6.402884,3.957852,1.741595,9.474160,-1.024277,2.685877,6.068070,-1.174842,-6.618594,0.900731,-2.532214,-3.846942,-3.413178,-8.578982,7.935760,-0.173535,-8.730460,7.527953,9.684199,4.798977,-5.174118,-4.540170,-7.301265,7.597319,9.096757,4.847131,-9.760358,-0.381210,5.055229,9.244196,7.517719,5.627862,8.741770,-4.565012,5.932349,-4.476880,-8.990815,5.023425,-5.084343,-6.557391,-9.365301,1.190079,4.451338,0.837111,-0.712558,7.108602,-2.774453,-2.932643,6.497973,-9.855888,-4.594989,-4.706203,5.025104,1.489146,7.070449,5.165974,-6.878773,-8.782590,2.686504,-5.326717,-0.900605,6.105530,-1.434332,3.582779,-5.715353,-6.037050,-1.795446,-6.220260,8.800710,4.195477,5.777577,-3.181498,1.066789,3.533922,-0.197182,5.861121,-1.776917,-6.828489,-8.963913,-5.412389,0.862704,1.191142,-6.056213,-1.067455,2.428417,-8.142932,-0.710141,-3.210225,9.228529,-5.941948,1.750850,9.294415,2.541578,-1.417323,5.204971,-0.663600,-4.791587,-8.632201,8.817397,-6.879170,9.922994,8.856742,1.501459,9.443774,-3.917974,-0.689061,5.398801,1.257741,7.526680,-4.118813,-5.147463,-7.216816,-2.507126,2.427920,7.767227,4.438518,-4.121683,-7.175343,-4.214488,5.325061,-3.029446,5.797774,5.874659,-3.112782,-6.323662,3.313810,5.750802,3.915469,-5.245985,-9.506477,-0.550468,-1.864055,-0.662752,-1.293740,3.606731,4.500371,-1.847346,3.027380,1.431859,-9.848445,9.609838,0.410738,2.459774,-3.405947,3.145694,7.264249,-0.318049,1.398058,9.164285,-9.319036,7.997398,-0.247075,-4.281768,7.747391,2.204735,4.232237,8.041664,8.282905,-4.141571,-1.131338,-4.514824,4.914229,-8.585385,-4.415459,5.826743,-6.762573,-1.123207,-4.860480,-7.000273,4.615310,9.853379,-2.738563,5.781563,-8.659399,-9.187902,9.728352,-2.879352,5.858147,4.934205,-8.870105,-4.749038,6.134375,8.699887,2.028635,0.409523,0.107609,-1.870012,5.606814,-7.131618,4.102658,8.526895,8.648493,8.897319,-0.867233,-4.975309,8.091403,0.702016,-7.902702,-8.611515,-0.761724,-9.179145,2.770650,-5.300290,-8.432210,-1.307392,1.183795,-1.740655,5.860423,7.805923,8.208942,5.442222,1.374364,9.045781,8.060032,4.534969,-9.054603,-0.362832,-8.094996,-4.398487,7.773998,-0.797273,-2.614439,7.339782,7.365020,9.044229,5.774683,9.532003,8.636854,-6.688185,7.442604,1.414627,4.463236,8.707401,-1.367031,-2.527216,-9.142183,-0.441854,3.975472,-8.756876,-4.774303,0.816273,-5.881800,-6.990215,-8.207586,8.152235,9.359114,7.784535,-2.819784,-5.458272,-3.479761,-1.394084,-0.592270,-3.844362,-6.544344,-6.627108,-6.373561,-6.513269,-1.891374,8.832940,2.138917,-6.844745,4.075306,4.662877,-9.310996,-7.479617,-2.002917,3.862237,8.357369,0.717981,6.803521,-2.826748,9.196742,-3.067118,-4.693760,-7.740931,-6.057899,-4.595982,-3.195526,5.341006,5.882319,-6.077385,-9.147668,-4.233292,5.663066,-7.239754,6.753447,-8.786667,9.026536,7.949333,-1.858291,-0.892254,-7.841232,-3.895300,-3.866582,-3.875554,4.367700,-9.389889,-0.093796,3.698255,-4.881635,-1.791723,3.555920,-2.636903,-7.284733,-8.831579,-6.417680,0.673226,0.389357,7.398271,-0.284779,4.843709,-1.217818,1.341196,4.915873,-8.874419,-2.571550,7.053492,-4.678601,2.172652,1.940963,8.782897,-9.135678,0.098313,6.530117,5.924726,-1.302987,2.496677,-3.806357,3.589198,-7.816118,2.958559,6.890960,-6.837665,6.203774,-5.965094,2.642992,-8.767594,-4.274587,4.795328,-0.629887,3.388690,7.253096,-2.676538,-7.586991,0.715909,2.324692,4.985714,-4.526480,-0.170693,0.967619,-3.988236,2.742643,-3.127435,-8.870834,8.405668,1.249537,2.850193,4.763415,-6.724240,-5.810227,-3.894736,5.010258,-1.318098,1.970859,3.626800,2.577578,1.305948,-1.097864,-4.041880,8.350055,0.500172,6.708678,-3.619454,-3.691623,-0.657425,-8.682120,0.989254,-6.592196,0.115115,-5.258215,3.748748,5.613005,-4.013750,-8.752970,-1.516048,-9.303308,-8.047456,8.896201,5.137584,-2.103976,-5.773629,-3.206905,-4.952288,4.245778,6.828266,-6.180648,5.811100,1.387706,6.032120,-0.785928,-2.079985,4.196040,-0.129416,2.670969,1.980030,6.817692,-0.024024,7.147192,5.792724,0.915039,-3.193448,5.604442,7.863608,-3.092899,-2.325538,-0.215662,7.668654,-4.144512,-2.296644,7.670392,5.067782,0.153081,5.195751,-4.281280,6.408633,3.096404,4.192380,4.574239,6.025983,1.281795,8.287311,-2.021638,6.964345,-9.473139,-5.798381,6.523508,9.249761,-9.253458,2.994064,8.522104,-0.968934,9.337059,4.770527,-5.089362,-6.139969,-3.825709,8.313994,-7.155536,4.575069,9.815892,6.603822,7.215314,5.606009,5.709458,-9.508662,-8.714575,3.863710,-1.088631,-7.403651,5.655098,-8.718880,-1.955049,9.841505,5.643136,-2.545263,-0.174897,8.030603,-2.121712,7.122633,-9.435643,-6.405483,-2.729503,-9.369791,-7.774052,0.343676,2.663108,2.482333,-4.873330,-6.529244,-3.101984,-1.533814,-4.811766,-6.498467,-3.652613,-1.922519,-2.289956,8.998761,-5.097614,3.677115,3.197411,0.170084,6.662749,-9.900791,1.285881,1.056223,5.775405,-3.808808,3.854434,-6.842512,0.794610,-6.652838,5.189674,-0.306022,1.233668,-1.154824,7.640483,2.206642,7.268994,-6.210474,1.445216,-9.217885,6.643689,-1.694418,4.585735,-2.175145,-3.388731,-2.377867,0.967581,0.273088,0.361944,5.869867,8.435262,9.709335,-7.294155,5.764843,3.875424,0.579529,0.662621,7.622147,-6.513734,3.926811,4.305588,0.568823,-7.007697,1.413782,-1.108955,-7.593589,-1.292527,-6.482676,9.781437,-0.060948,1.188092,6.296678,2.040016,-1.661664,0.221813,-1.800385,8.310299,6.127559,3.252362,3.768153,4.740153,2.796451,4.908681,-3.071585,-9.055822,7.732582,-6.446836,-1.100797,-3.992423,-1.997296,-5.773681,-7.696715,-9.256547,9.262422,-9.395241,9.187832,4.388038,5.087021,8.442703,3.421167,-0.291611,0.412112,-7.548221,3.167513,-1.320792,-8.559485,-9.799632,0.741079,-9.992423,-2.770729,2.956199,-6.396484,4.483313,-2.676147,3.312231,-3.955406,-0.038812,2.880430,7.597590,7.363884,-9.962656,-5.773500,-9.034194,4.719518,-5.788594,-0.494745,5.407494,-7.304873,-3.340416,6.532600,5.073963,-9.623507,-2.996087,-3.139495,-7.669584,8.252159,3.557262,2.351333,3.013235,-5.356841,6.088858,-5.947177,1.768971,6.531831,0.291861,2.564844,-0.726051,-4.116413,3.261857,-7.770179,9.578272,-6.494624,9.756341,-8.936779,-7.560456,-1.262756,8.678409,3.912768,-8.290593,2.293478,4.677025,-9.542757,-5.130334,-0.852030,9.480450,4.916570,0.132324,0.260047,4.507721,3.782062,-4.890726,9.077981,-0.323151,-9.233869,7.224473,-5.625176,-8.828057,-4.329872,-1.091363,3.202765,5.479898,-3.303129,-0.209086,9.880827,0.265923,-0.942508,2.346191,-9.054567,-4.214314,-1.697555,-6.467834,-0.314033,3.376749,2.209304,-6.696312,3.058376,7.987457,-5.043632,8.247227,1.685735,-8.016693,-7.665102,-6.594682,-7.224503,6.798092,-9.767352,6.132110,-6.365002,-3.643718,-5.915455,-6.038307,-9.277504,7.480969,-3.430369,7.656865,-6.282636,1.232220,8.977663,4.113462,-6.851182,-4.907189,-9.947528,7.932128,-1.734238,-6.230493,-6.913890,-3.560161,-0.016468,1.375996,-6.676196,-3.338363,3.176929,9.487388,5.922254,-8.152817,9.186129,7.294448,-4.105925,-6.138377,-7.693341,-0.250805,-5.970199,6.595614,-7.239311,3.674651,9.591225,7.148292,9.498006,8.359587,3.036620,-0.492181,-4.973366,-5.603037,-0.174136,1.608220,9.764866,-7.114607,-1.744260,-5.277218,-4.893313,5.176397,-6.666665,-4.534228,5.625677,-5.589637,3.122504,2.478259,-0.291348,2.350033,0.530797,9.377008,-8.331777,-6.063788,-5.574915,6.137636,-3.896688,-4.045338,-9.392894,-9.190509,0.089267,-3.143766,9.260514,-0.095610,-6.132565,-6.595228,1.853732,-7.255372,4.268121,-5.657521,-0.125693,0.912498,9.680842,2.916203,-3.829044,2.169374,-4.199686,0.090810,-2.224068,-9.377094,9.221238,-8.653551,-7.389165,-1.586544,1.807446,5.104694,-2.418591,-0.873290,6.359082,0.612331,2.087399,4.746755,5.724479,2.202337,-2.445718,-3.692474,-3.970315,-6.164851,8.723435,7.286894,-0.165951,-7.294405,2.204939,-8.007819,-0.237840,-4.728375,-9.302886,-4.315620,-8.068454,5.605901,6.628416,-0.205503,-6.241413,-4.970675,9.134471,-3.587032,9.013379,0.612513,8.570540,0.936149,4.840021,3.410144,7.239484,4.383942,6.641665,-6.116606,-1.839600,7.942089,-4.009180,5.952028,3.326997,5.747097,-7.536632,9.273406,-2.878063,-3.669561,-1.356919,9.538601,7.106873,-8.515865,-7.344954,3.228455,0.428875,2.989607,-1.866393,-7.447803,6.057407,-6.694880,-7.179480,0.498380,-1.334886,-5.836988,-3.967347,-5.635960,9.098926,-6.742235,-3.723276,-0.073805,-7.262335,5.429070,-7.338149,-0.623635,7.703816,-9.159133,-9.970015,-7.968221,4.945609,-3.443190,-5.892524,9.067836,2.496957,1.670191,8.485387,0.167780,-9.337817,-9.864204,-3.808660,-0.480136,-6.805430,1.907036,-4.550573,0.451062,2.570649,8.685347,9.343101,1.616965,9.912891,-2.627454,-5.662078,-5.156510,-0.656829,-6.026062,-2.450201,-1.684189,0.756874,2.384473,7.156500,6.887231,-2.352873,-2.870099,6.806125,-0.949609,8.058634,5.218348,5.225281,-2.117896,-7.122332,-6.330606,4.157854,6.869859,5.454308,-4.186184,-5.186443,3.276112,5.070913,-9.813369,4.918855,1.045854,5.243625,-0.740918,-3.999275,-6.067456,7.187659,1.964809,1.448100,2.996320,-4.863844,0.020362,1.446000,3.767583,-5.771638,1.310024,2.729533,-8.984851,5.664661,9.855952,9.009193,5.172287,-8.629653,6.069855,7.729599,-2.333536,8.814669,-9.735204,-0.836528,6.677247,1.836482,-9.786094,6.529444,5.226696,-5.961221,-6.101637,-4.065247,-7.788479,2.971944,-1.140657,8.009720,-4.722983,-7.316552,4.371317,-4.839039,-2.882493,-2.206148,-5.421152,0.578654,-9.131858,-4.300732,-8.932847,-6.682126,-0.701890,-8.486640,4.285341,4.810875,-3.391324,-9.735384,6.011802,-3.568705,6.805502,-3.160950,-8.017306,4.695390,3.880007,-6.988859,5.185701,1.144418,-4.101822,-1.010294,4.216055,3.729847,-5.484294,8.395335,-6.358145,4.573778,-2.615016,-8.026755,7.694813,-8.128192,8.907604,-9.692488,4.939779,-5.866726,-4.621927,0.773883,2.739551,4.264488,2.531508,5.645323,3.294558,3.316507,-8.189803,-6.583270,2.140015,5.559319,1.446744,6.524008,9.434605,-4.856597,5.894947,9.175174,-2.551325,-4.317160,3.939792,-2.801423,-5.162941,7.693864,1.382759,-8.142384,-2.691656,9.201903,-7.594380,-1.444392,5.612514,5.039013,2.257172,4.531529,1.077250,4.271771,1.889791,8.291020,5.204734,-7.326594,3.472938,0.500555,-3.765151,5.698400,-3.979495,-2.933864,4.933218,-0.287468,-9.811801,-9.270149,0.981925,5.254893,5.572317,-6.965117,9.857017,2.120672,7.364066,-0.150824,-1.879358,-7.430307,9.631071,-9.434422,-3.425676,7.504182,-1.387334,5.077600,4.928523,-1.602544,2.815333,9.525361,3.345215,8.907248,-7.192899,8.394653,-7.249630,4.880986,-2.570481,-5.754655,-6.506004,-5.952450,1.197541,-2.617491,-0.469007,-9.972343,9.519406,-8.725582,-3.138720,2.181999,9.629506,3.073574,7.374889,7.327674,-0.604578,-7.932579,-1.173243,5.401304,-4.271822,-7.325171,-1.431232,5.404303,1.194070,8.179396,8.475634,-5.237958,0.813944,-8.306518,-6.779276,-6.314164,8.815789,5.679016,5.315988,-6.278503,-4.098088,-7.367966,9.440916,-2.708348,3.770813,-1.230761,-9.307186,9.233778,7.579425,-6.614747,-5.623567,-0.389202,-7.863997,0.865184,9.800053,5.870846,-3.677064,-0.866859,7.668151,-4.220860,-4.388307,-2.868187,5.927629,-5.153082,2.000483,-4.142664,-6.102395,-6.310942,-2.743979,-8.955947,1.287557,4.795919,-1.790748,9.550111,-1.913886,-8.836312,-4.783534,-0.849718,7.963854,-7.652095,7.160602,-3.782324,-9.677056,-0.663704,-0.612053,-1.687684,0.384843,2.600424,5.147313,7.653382,3.454141,4.814208,-2.443667,1.668285,-7.267499,6.543732,2.604249,6.840643,-2.363526,-9.702597,6.146497,-9.872773,7.533703,-8.328599,-7.707655,-8.267572,0.448731,3.710912,9.235947,8.496570,3.835658,-9.688932,-0.765955,-0.247913,1.471343,8.742336,5.566659,0.200397,-8.375923,5.072731,-9.294897,-2.130541,9.993789,3.809661,-8.283100,6.187661,4.226168,-6.291306,2.973817,-3.111717,-9.606110,9.077832,6.928225,-5.907245,-2.884911,-6.575486,5.875686,3.325393,0.281017,-8.472531,2.512535,7.690695,6.528024,4.973049,-7.270178,2.521282,3.451009,-9.653787,-3.906789,-3.202047,-5.405527,5.965886,7.663474,8.085318,3.811410,0.057862,9.436440,-8.424905,-3.414063,1.393919,5.735101,1.111386,-1.476106,-3.275368,-6.534712,4.430179,0.122667,6.104992,9.584130,3.603216,-4.389607,-8.026641,9.632912,-2.458151,-4.965546,-5.117006,-2.449635,-0.490290,2.183464,2.564750,-5.731603,8.719425,1.633906,-9.623493,3.248091,-1.042818,-2.031289,1.051925,4.027003,-8.580171,8.861876,6.316437,-0.791801,-5.431264,-4.489022,-6.900824,1.273799,6.640109,-4.554407,9.142862,2.140409,3.814458,-7.656616,-4.132749,-1.355070,3.239664,2.472102,6.179622,5.855142,-7.634663,-6.370460,-8.543629,-1.325517,-4.466958,7.989686,-2.996922,5.561044,4.232735,-2.248524,8.872909,-3.505030,-0.728072,-2.229424,7.692109,-3.991282,2.905157,-9.291994,-9.449892,8.021023,0.546298,-1.559593,-6.968668,0.588956,-3.808901,6.103602,-8.854149,-7.590699,4.983772,6.284937,-9.718452,-8.163315,-8.567728,2.764802,0.713286,4.862015,-5.940087,-0.739645,-9.232104,-1.892652,0.491386,-6.228831,5.834398,4.464609,7.139000,4.562537,-8.007825,-7.712353,8.673877,2.725790,-1.968489,9.240540,-3.542528,0.842914,-2.405339,5.476201,2.766846,9.867647,7.876496,-6.321558,6.906087,-9.951500,0.932094,-7.448547,2.286933,-9.506908,6.426529,-6.662342,5.508917,-4.737069,6.670196,-2.444150,3.023062,0.581748,-1.940269,-7.228775,3.951253,5.518363,0.595146,6.229844,1.662130,-3.552434,-6.739904,-1.884951,4.465682,9.228400,9.789502,4.263150,1.140377,3.415402,-3.210935,-7.191933,-5.246059,1.113555,3.047068,-0.253708,-5.467295,3.808056,4.650179,-8.963960,-5.482849,4.854964,4.503701,0.243211,1.242510,-3.706143,-5.765729,-1.441487,-7.760749,-3.642013,-2.811671,-8.316661,9.764773,8.963319,-3.944063,2.996406,6.954060,-0.135118,-0.919058,-6.179422,-2.673466,0.833386,5.963620,2.610151,0.164966,9.565509,9.826045,-0.187908,-2.817498,0.973209,-0.028378,9.800880,-4.928187,-0.677175,8.811045,-9.537107,-0.428188,-0.763093,6.216754,1.358422,4.448304,8.676661,1.542052,-6.549680,4.126071,-2.828088,-0.029765,-6.721919,5.947004,6.502554,8.122581,-3.458261,-6.140549,7.278840,-5.582625,-5.848772,7.528532,-2.636408,-8.727438,-3.305731,8.820528,8.456193,1.254416,-0.323187,-8.209520,5.702779,0.228035,6.247773,2.765473,-8.372337,-1.741231,1.384749,-3.793766,-8.254954,-5.331995,-8.447804,6.360298,-0.836938,9.256977,5.115310,-6.798611,0.351807,-7.527362,4.771597,8.480757,8.571472,0.710469,-9.522704,6.562114,-4.359312,6.370035,8.179836,-0.545943,6.794226,-9.382157,8.411907,-5.112174,-0.194146,-3.082096,-5.401919,0.008935,7.511524,-6.010422,-3.327671,-4.470516,-5.917858,-3.716019,-7.847505,3.206596,-0.289698,-0.712830,-7.256969,1.625551,3.179219,9.354486,8.464015,4.915127,1.098191,-9.312683,2.242288,-5.549020,3.453023,2.482970,8.744859,4.700635,-1.743117,0.980306,-5.874839,-8.328736,-3.661868,3.047629,-3.169728,-9.482518,4.556279,-0.128243,6.591663,-7.225310,2.684585,-8.110488,-8.477478,-5.313857,6.051001,9.913601,-0.335275,7.164828,9.656541,8.816845,-6.268334,3.666412,-8.059492,-0.760738,-1.488637,-6.211367,5.310399,-7.632406,3.796720,-0.986542,4.485601,-2.196757,1.054208,-4.373509,8.115274,6.175756,-7.493782,2.089861,-7.429062,-5.408084,-5.425456,-1.482569,-0.076377,6.636437,7.807821,-4.916848,8.181348,0.470631,7.331427,-6.244740,1.505828,-5.405015,-0.039259,-7.020880,0.531278,-9.407902,-5.635352,0.905483,3.544730,-7.006621,9.550610,7.150335,8.384557,9.183880,9.236583,6.448713,0.053853,-1.207830,9.387578,-0.432109,2.939909,-8.858091,6.030107,-8.015442,-2.550155,-4.756883,-9.233529,3.469274,-9.992502,-6.458358,-5.488135,-7.943191,9.425359,9.924775,3.681692,8.322339,-9.813802,-5.559817,-5.771345,6.323055,4.037434,-7.572567,5.531455,-1.378770,-3.563121,3.484961,-8.723577,4.853534,-2.846130,2.072149,-6.487005,1.210266,-0.908936,1.912661,-0.794289,-4.528646,-2.591626,5.538268,-5.436518,8.345581,-3.146414,0.764781,-8.229594,-6.867846,7.423198,-7.039658,4.363327,5.397955,-4.021209,-8.116838,3.552508,-7.954781,4.072761,9.265158,8.483811,-3.975022,-0.381874,8.977941,-2.026544,9.037997,9.377804,-0.123888,2.084766,-1.534982,-5.644840,7.153800,9.237329,0.565896,1.787279,-8.255947,1.675255,3.394579,-0.350986,-0.811464,-3.153804,1.528956,0.853780,-3.573572,4.908823,-6.542800,7.931797,6.752699,-2.188652,6.093683,7.404212,-0.186209,0.164529,-7.532515,-6.726651,-4.155746,2.144822,-3.398888,8.396964,4.910644,-9.095446,-4.332397,2.043811,-7.314393,-6.615618,-0.144325,-3.159796,-7.185166,-5.333947,6.112575,5.985490,6.348836,0.700198,-4.698049,6.986275,2.865012,0.701144,2.626042,4.725344,-0.429516,-0.805660,-7.921720,-4.387206,-4.693029,5.971141,4.537633,7.757432,3.493535,6.707798,-9.019377,-4.149642,-2.034132,7.550783,-5.488517,6.995240,4.486154,3.400648,-2.032147,-8.899171,-8.678176,8.812544,5.496628,1.768718,5.883299,-6.423129,0.994155,-4.789998,-2.394452,2.714617,-8.156599,-5.397643,-6.911843,8.530897,2.384832,1.561972,-3.984105,1.954716,-5.555963,-4.778861,7.130754,5.357201,6.640542,-8.066993,9.287298,2.525782,8.369919,9.870467,6.099067,-8.069881,8.619498,0.044248,-9.644177,1.542942,3.646525,0.288341,-8.016533,4.910617,-9.625777,4.403664,8.887411,1.792671,-4.020636,4.417559,-5.132704,-5.742784,7.994208,2.800464,5.992406,-5.805587,-8.997486,5.412115,-5.599311,8.345581,3.237999,4.440389,2.259796,5.159784,8.009011,9.290706,-7.942161,0.700665,4.338278,-0.479799,2.769944,7.145927,-0.294986,-2.508158,0.191763,9.232104,2.550318,-9.444361,8.776624,-6.002466,-0.097638,-6.481633,-9.027733,-8.299850,-6.519807,-6.971050,-1.398074,-4.299413,-3.443022,3.449277,-5.986644,-5.707627,3.188210,-4.364988,-2.775678,-9.005162,-9.437927,-4.788171,-1.514529,7.192968,3.567201,6.511416,5.076731,-4.362469,-4.870610,-2.745770,-8.150159,-6.983147,2.442272,-4.254852,-1.720637,-8.210276,-4.363054,7.372786,0.864635,0.786757,-0.910407,-5.398972,-8.645721,5.386485,8.169921,2.407336,3.873620,6.212302,-4.320481,-2.001957,-3.847936,-8.892384,2.463660,-6.649643,-6.397618,7.757520,-1.689515,-1.443822,-2.745689,0.289643,2.114442,2.658295,0.153529,4.999333,7.018316,-4.227262,-1.905274,-1.621785,-7.902768,2.548541,-5.253572,3.423278,-1.803735,-2.039374,3.404789,-3.245301,-8.496328,4.665848,6.951631,-5.212535,5.289355,-7.959117,6.014017,5.139600,5.877182,-2.579358,-7.409851,-5.162801,7.422307,5.474827,5.259218,-9.197501,-9.693804,6.768726,-1.893302,-1.933882,-7.949039,-9.309844,6.121188,9.605489,-3.668006,-2.644500,0.703688,2.876176,6.849740,2.365585,6.491692,9.204878,-7.393916,8.900096,-4.531864,-2.509358,-0.248506,-8.648142,-2.150192,8.995268,1.712570,2.542519,-6.336416,7.312212,-6.800180,-5.034713,-7.490944,7.673544,-7.444562,-5.057225,-5.601778,4.471307,2.336002,-7.251121,5.348390,-7.457281,1.467990,3.120573,-6.127244,-7.604857,-3.839748,-4.181419,-2.638531,6.017635,-8.318732,2.536903,-1.410798,-3.797800,-9.423363,9.698426,-9.878460,-0.488895,-3.779469,3.461634,-8.113438,4.438683,3.726091,-3.044040,7.071514,-8.539244,0.877711,-8.576672,6.110368,8.027937,5.067543,6.126861,-7.163262,0.335147,-9.839185,7.824536,-1.539904,2.335689,0.921868,8.836969,7.491029,-6.065706,8.445265,-4.319318,9.806480,-0.968943,-3.333423,-7.554648,7.786928,0.202386,9.254893,8.612575,3.825432,4.598041,-2.904024,1.994737,-7.334181,-2.603113,-2.018333,-3.544977,-0.364831,-3.183636,3.764816,4.549673,8.313439,-4.899461,2.647465,-0.266814,-5.338043,4.997589,9.131452,-3.738704,1.432168,1.879994,0.661589,9.152504,0.543825,-3.386474,0.612097,9.352436,6.984185,8.095061,9.298430,2.347293,9.178189,-4.948108,-3.614251,-2.982256,0.958817,0.547496,-8.669430,-1.084787,0.522521,-1.414950,-6.650149,3.221876,7.531918,1.132891,-9.622590,-6.938391,8.929581,-0.231574,1.606253,5.727684,9.328927,2.859889,-8.252662,6.595161,-2.531310,-8.669874,5.828227,-4.061145,-3.903361,-8.832276,0.529102,-7.166537,3.044653,-2.857510,7.023580,-6.353882,-0.107055,-5.245956,1.448984,-9.404806,7.379212,4.479777,-4.209895,2.309621,9.626805,-6.711330,-6.212060,1.773378,3.659944,-1.397815,-4.109644,3.212948,-0.631896,0.576550,4.290266,-4.140761,-1.694615,-6.299272,8.005892,2.493598,3.412482,2.769513,-2.874574,9.981904,-8.519622,-6.085131,-4.717658,-3.062606,-0.289711,3.580179,4.657567,-0.682409,1.667178,4.280970,5.045228,8.246322,-3.667466,-7.330311,5.268976,-4.014394,-4.085602,-9.018598,1.090199,6.870382,-8.839079,3.328636,-4.739043,1.821762,-0.076247,8.001121,8.480479,-5.626340,9.937632,-4.016285,5.832751,8.890051,-9.204565,-5.151611,-8.871099,1.506288,-1.317503,-7.401505,-4.157633,-7.795080,-4.847882,-1.942101,-4.836322,8.218790,-8.058451,6.011529,6.335551,7.052528,-4.064194,6.571254,7.758855,-0.242847,0.862139,8.606128,-8.722008,3.308670,2.917840,8.725540,-6.278273,2.461721,-5.756691,-5.040530,8.227522,6.774189,-2.759123,-0.917493,7.164858,3.659027,-3.215600,7.375291], dtype = "float64")#candidate|9710|(3360,)|const|float64
call_9708 = relay.TupleGetItem(func_5919_call(relay.reshape(var_9709.astype('float32'), [15, 4, 15]), relay.reshape(var_9709.astype('float32'), [15, 4, 15]), relay.reshape(const_9710.astype('float64'), [3360,]), ), 3)
call_9711 = relay.TupleGetItem(func_5923_call(relay.reshape(var_9709.astype('float32'), [15, 4, 15]), relay.reshape(var_9709.astype('float32'), [15, 4, 15]), relay.reshape(const_9710.astype('float64'), [3360,]), ), 3)
output = relay.Tuple([call_9698,call_9704,var_9705,call_9708,var_9709,const_9710,])
output2 = relay.Tuple([call_9699,call_9706,var_9705,call_9711,var_9709,const_9710,])
func_9715 = relay.Function([var_9705,var_9709,], output)
mod['func_9715'] = func_9715
mod = relay.transform.InferType()(mod)
mutated_mod['func_9715'] = func_9715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9715_call = mutated_mod.get_global_var('func_9715')
var_9717 = relay.var("var_9717", dtype = "uint32", shape = (128,))#candidate|9717|(128,)|var|uint32
var_9718 = relay.var("var_9718", dtype = "float32", shape = (900,))#candidate|9718|(900,)|var|float32
call_9716 = func_9715_call(var_9717,var_9718,)
output = call_9716
func_9719 = relay.Function([var_9717,var_9718,], output)
mutated_mod['func_9719'] = func_9719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6207_call = mod.get_global_var('func_6207')
func_6208_call = mutated_mod.get_global_var('func_6208')
call_9730 = func_6207_call()
call_9731 = func_6207_call()
output = call_9730
output2 = call_9731
func_9746 = relay.Function([], output)
mod['func_9746'] = func_9746
mod = relay.transform.InferType()(mod)
mutated_mod['func_9746'] = func_9746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9746_call = mutated_mod.get_global_var('func_9746')
call_9747 = func_9746_call()
output = call_9747
func_9748 = relay.Function([], output)
mutated_mod['func_9748'] = func_9748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8197_call = mod.get_global_var('func_8197')
func_8198_call = mutated_mod.get_global_var('func_8198')
call_9785 = func_8197_call()
call_9786 = func_8197_call()
func_5503_call = mod.get_global_var('func_5503')
func_5505_call = mutated_mod.get_global_var('func_5505')
var_9789 = relay.var("var_9789", dtype = "uint8", shape = (60,))#candidate|9789|(60,)|var|uint8
call_9788 = relay.TupleGetItem(func_5503_call(relay.reshape(var_9789.astype('uint8'), [10, 6])), 0)
call_9790 = relay.TupleGetItem(func_5505_call(relay.reshape(var_9789.astype('uint8'), [10, 6])), 0)
func_4518_call = mod.get_global_var('func_4518')
func_4521_call = mutated_mod.get_global_var('func_4521')
const_9792 = relay.const([-9.133506,-8.044955,-1.778815,2.075430,5.521237,7.196982,3.158216,7.295309,-9.915815,2.829499,-2.805697,-7.484576,-5.286195,-8.117295,-3.907285,8.305795,3.473078,6.425916,0.199310,4.091408,0.765281,2.288213,0.370784,-4.085204,-1.193402,0.772035,-7.338951,-2.997265,-2.542521,-1.021512,-8.636470,8.162343,6.951472,6.736019,-0.908594,-8.628922,8.516330,-1.023904,-2.062666,0.238758,-0.678030,6.801653,-9.806867,-1.789629,3.690018,9.318887,-0.257307,7.565257,1.802858,8.342348,5.716611,6.799279,6.742652,9.469043,2.134166,5.959768,-7.775780,-4.751287,-4.806009,4.648854,0.503359,8.927501,-8.339903,5.295781,-4.965196], dtype = "float32")#candidate|9792|(65,)|const|float32
call_9791 = relay.TupleGetItem(func_4518_call(relay.reshape(const_9792.astype('float32'), [13, 1, 5])), 0)
call_9793 = relay.TupleGetItem(func_4521_call(relay.reshape(const_9792.astype('float32'), [13, 1, 5])), 0)
func_7225_call = mod.get_global_var('func_7225')
func_7228_call = mutated_mod.get_global_var('func_7228')
var_9807 = relay.var("var_9807", dtype = "float32", shape = (18,))#candidate|9807|(18,)|var|float32
call_9806 = relay.TupleGetItem(func_7225_call(relay.reshape(var_9807.astype('float32'), [18, 1])), 5)
call_9808 = relay.TupleGetItem(func_7228_call(relay.reshape(var_9807.astype('float32'), [18, 1])), 5)
output = relay.Tuple([call_9785,call_9788,var_9789,call_9791,const_9792,call_9806,var_9807,])
output2 = relay.Tuple([call_9786,call_9790,var_9789,call_9793,const_9792,call_9808,var_9807,])
func_9810 = relay.Function([var_9789,var_9807,], output)
mod['func_9810'] = func_9810
mod = relay.transform.InferType()(mod)
mutated_mod['func_9810'] = func_9810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9810_call = mutated_mod.get_global_var('func_9810')
var_9812 = relay.var("var_9812", dtype = "uint8", shape = (60,))#candidate|9812|(60,)|var|uint8
var_9813 = relay.var("var_9813", dtype = "float32", shape = (18,))#candidate|9813|(18,)|var|float32
call_9811 = func_9810_call(var_9812,var_9813,)
output = call_9811
func_9814 = relay.Function([var_9812,var_9813,], output)
mutated_mod['func_9814'] = func_9814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8251_call = mod.get_global_var('func_8251')
func_8253_call = mutated_mod.get_global_var('func_8253')
call_9823 = relay.TupleGetItem(func_8251_call(), 0)
call_9824 = relay.TupleGetItem(func_8253_call(), 0)
func_271_call = mod.get_global_var('func_271')
func_275_call = mutated_mod.get_global_var('func_275')
const_9834 = relay.const([9.181228,7.866392,8.704969,8.466727,8.203103,0.536016,0.964917,-8.730242,-2.354983,2.392923,3.057794,-4.508360,1.348428,9.569551,-6.917320,5.863381,-7.291044,5.903350,7.715095,-3.915138,7.966684,4.335889,-3.519939,3.929324,8.903626,-5.225472,-8.329922,-3.425824,-9.478339,-8.970025,2.905772,-6.354278,4.408665,8.650898,3.976861,1.250168,-2.404842,2.405486,2.822721,9.207070,3.096284,2.330691,-0.830961,-4.593652,8.426688,4.096096,-2.586525,-1.608897,0.460082,-3.964913,-8.131419,2.105132,-9.140881,8.151751,-2.247838,-6.861975,-3.069295,2.278524,-1.956835,7.954332,6.506827,-7.461307,0.914589,1.271732,-0.617513,0.208030,2.316347,8.287473,0.985772,9.362584,2.694845,1.873197,-4.695536,4.576531,-9.477094,-3.463629,5.806166,8.336013,-3.050384,-5.451825,-4.783205,2.431212,-1.558546,2.963275,7.906802,9.802473,3.819595,-8.841395,-2.823476,-9.969505,-1.094374,-3.922718,1.586773,-6.005042,-8.608510,-9.410241,-0.083278,-3.500942,6.142692,-7.352120,4.018299,7.974237,1.405497,-6.657614,7.753597,-1.791800,7.899456,-4.233401,9.443292,-9.086929,7.665021,-7.099852,-9.464419,-7.380014,7.246021,-2.871510,2.062308,5.434587,4.392784,-2.212346,-4.498716,8.627830,4.984025,-7.432340,-9.099754,-7.840986,6.921842,-5.808065,0.059863,1.952114,4.447254,4.498531,-7.481707,3.465698,-0.060735,-2.036383,9.389426,7.122717,3.735853,1.234622,-6.215780,5.322987,-0.729771,-3.682456,2.453169,-5.855010,3.347317,5.992776,-6.550139,-4.696641,-6.329743,4.089431,-5.618793,-0.192410,-1.863139,7.420687,1.658822,4.519145,-0.903426,2.590510,0.260911,0.237730,-0.052088,-3.583381,2.761251,0.721085,-3.048842,6.565422], dtype = "float32")#candidate|9834|(168,)|const|float32
call_9833 = func_271_call(relay.reshape(const_9834.astype('float32'), [12, 7, 2]), relay.reshape(const_9834.astype('float32'), [12, 7, 2]), )
call_9835 = func_271_call(relay.reshape(const_9834.astype('float32'), [12, 7, 2]), relay.reshape(const_9834.astype('float32'), [12, 7, 2]), )
output = relay.Tuple([call_9823,call_9833,const_9834,])
output2 = relay.Tuple([call_9824,call_9835,const_9834,])
func_9836 = relay.Function([], output)
mod['func_9836'] = func_9836
mod = relay.transform.InferType()(mod)
mutated_mod['func_9836'] = func_9836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9836_call = mutated_mod.get_global_var('func_9836')
call_9837 = func_9836_call()
output = call_9837
func_9838 = relay.Function([], output)
mutated_mod['func_9838'] = func_9838
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9926 = relay.var("var_9926", dtype = "uint8", shape = (4, 5, 7))#candidate|9926|(4, 5, 7)|var|uint8
const_9927 = relay.const([[[1,-1,7,-4,3,6,-1],[7,-7,-5,-3,-1,-1,-5],[-1,8,-10,-8,5,5,-3],[-1,1,2,-2,-7,9,-7],[9,5,-4,3,-2,-5,4]],[[6,-3,2,7,-2,-1,6],[-8,-10,-7,-8,-8,9,3],[6,3,7,-8,-10,10,-6],[2,1,-6,-7,-4,6,-10],[-1,-8,-2,-6,9,-7,1]],[[-2,10,-10,3,10,1,-9],[-7,3,-1,2,5,4,5],[4,1,-4,9,-10,10,-4],[-7,7,1,-1,-2,-6,4],[-1,-1,5,-1,1,-3,-2]],[[-4,-3,1,-6,-1,-3,-1],[-1,10,3,7,3,7,9],[6,10,-10,-2,2,-3,6],[-5,6,-1,-8,-8,-2,-4],[-5,-6,6,3,-10,7,5]]], dtype = "uint8")#candidate|9927|(4, 5, 7)|const|uint8
bop_9928 = relay.equal(var_9926.astype('bool'), relay.reshape(const_9927.astype('bool'), relay.shape_of(var_9926))) # shape=(4, 5, 7)
func_7630_call = mod.get_global_var('func_7630')
func_7635_call = mutated_mod.get_global_var('func_7635')
const_9933 = relay.const([8.362780,3.180821,7.650365,-8.091593,-9.464749,9.095864,6.819727,-3.561154,-3.525578,5.721228,-5.177528,-3.566268,4.054634,-0.968059,-7.519622,9.100779,-9.098961,-2.450893,-9.237207,-1.658635,5.086724,1.792412,8.073292,-8.305682,4.000979,1.208438,-8.754542,2.399208,-7.492225,-3.393254,2.630579,-1.462200,-1.570744,5.661480,4.325686,-9.567200,5.943814,-5.309754,0.880493,7.666854,-6.905838,-3.382529,-5.656149,-5.384188,0.919282,3.910127,3.636034,1.946835,-4.548935,-2.921383,-3.330652,3.382361,-6.059092,-6.595681,-5.519715,-6.429910,8.772112,9.358289,-9.329115,-3.062967,4.917322,4.612675,-5.987952,-2.192815,1.504643,-3.312409,7.438665,-8.313443,8.183120,2.032849,-8.008654,-9.488655,3.852009,5.228887,-2.131015,5.656934,-3.947794,-9.600475,1.499778,2.160042,1.211564,-6.033327,0.355311,-8.995422,-1.366720,0.046856,7.444335,-8.261446,6.621691,9.340826,2.951761,5.295911,2.758388,-7.677442,0.128828,4.203338,-5.188671,2.192407,-7.385963,-3.186132,-5.723712,9.567198,-3.319681,-4.354191,-5.916680,1.472300,-9.743504,5.618667,-7.521110,8.911491,5.991285,-0.041921,-2.915703,-0.693160,2.897950,4.412390,-8.500262,1.829766,-5.748098,-9.294038,4.493660,1.630040,9.440402,6.732001,-7.242101,8.449417,-3.327002,2.023861,7.045860,5.497226,2.470951,-3.503490,-0.780860,-1.970806,2.603139,7.474819,-5.180162,2.911905,5.585335,2.271986,9.950047,1.117056,-5.545859,-0.942343,-1.954819,-2.682037,3.986038,1.162750,-3.517344,-7.952560,8.581035,5.442397,-9.484502,5.226379,1.166046,-9.088973,4.399137,-1.517185,-4.183461,2.447661,7.446246,-9.594061,3.928479,-4.256349,6.222056,7.055196,-4.918933,-3.368815,8.016290,-4.853508,-7.577570,0.838692,-6.173387,0.025347,1.045078,-9.129580,-2.759726,5.828512,-3.634652,-0.520731,-4.799846,-6.797341,-8.103729,-0.470308,-7.902902,-4.102716,5.810197,-5.072667,-0.249263,-4.081771,1.806115,-6.897097,-8.161791,3.811329,7.492252,-3.681554,6.422511,-0.479351,-9.540969,-4.740591,1.166596,6.244427,-4.112493,-7.031642,-5.224914,-4.381756,1.573296,0.702367,-9.763484,7.688366,-0.202821,-7.650462,-5.338326,3.319179,0.368116,-3.355323,7.509668,3.887872,4.849845,-6.987418,-7.553421,3.199795,3.960810,8.859929,2.405213,9.974949,0.413264,-9.184502,-7.321145,-7.245370,9.205996,-8.408765,-4.762552,-1.045329,6.300837,1.721298,-7.399701,-0.092813,-9.775539,8.949093,-2.343088,5.115007,-8.346438,1.720572,-0.846990,-3.793304,-0.568625,-6.162976,-4.016382,9.031785,2.432178,-8.880202,4.499445,6.394320,-8.564743,-4.130210,2.212929,-5.977083,5.336936,-7.923038,4.024210,0.192556,8.753173,5.756146,-2.054789,5.304465,4.651565,0.963493,-0.069593,-3.213795,-4.955820,0.220400,9.298076,9.278034,-0.391811,-9.606036,5.712048,1.276574,3.979037,-2.856587,3.369596,0.608898,1.799498,-2.097266,9.617313,6.313955,3.793335,9.241858,-7.013778,3.671549,-5.317153,0.043746,3.996690,-3.011012,9.976303,-5.151609,-6.950055,6.470566,8.158092,-1.152158,8.065718,-5.977935,-2.113143,5.900721,-2.720817,7.770248,-9.701812,-2.444036,-4.511722,-5.147982,-3.663094,-6.879636,-7.381917,-7.251902,9.734830,-5.338093,-5.758360,4.178358,-0.307493,-7.147919,4.870713,6.530493,-2.401992,8.968227,-3.665754,-2.677436,7.958857,9.807192,-4.745931,5.326324,-0.594651,-4.682776,-0.017198,-8.307553,-7.757662,3.211462,-7.625113,6.560960,8.701096,7.555315,-1.485575,-6.725248,3.962080,1.106402,0.249580,7.996299,-7.517561,5.278425,-4.742271,7.445384,-8.368935,-1.147495,6.574253,3.937118,9.634001,-5.287325,-5.890053,9.645037,6.655057,0.749268,9.127794,-9.270911,9.894788,-9.924124,6.487160,-7.373902,-1.440633,3.574348,7.366556,-9.452421,9.963268,-0.425908,5.288701,2.175974,3.252693,-2.678825,-9.789636,-6.669672,-5.772677,0.071126,9.105375,0.994107,-4.856201,8.664325,1.197677,-0.145725,7.475006,-0.179434,-2.230455,7.458778,-9.372125,-9.291317,-8.764458,-0.940332,1.368974,8.212840,-7.509574,8.916350,1.379568,-9.256496,-5.658831,4.666036,6.463478,2.459384,-3.112037,2.850944,-0.264869,8.956071,9.987863,2.009366,1.258990,6.474113,4.247922,-4.421110,5.201803,7.712196,-4.822759,0.967131,-9.002473,1.183058,4.201964,5.746767,0.661757,3.920786,5.455410,4.303623,1.396469,-3.843616,0.767951,4.127718,8.946421,5.623782,5.411758,3.663414,5.320969,-5.748927,-1.714820,-1.823938,-1.179656,-7.277084,-1.088367,-3.027299,-1.987890,-9.334448,-8.224320,-6.369694,-4.222537,1.047837,6.408401,8.267127,7.594244,1.031747,5.718513,9.238089,6.929701,3.797351,-3.216120,6.981961,-6.787721,-0.597772,4.234613,-6.195428,-4.234956,-1.883346,1.316015,-4.495688,6.467038,-5.208485,7.584772,2.580144,4.923837,-0.133603,-0.952297,-1.185265,9.487026,4.164311,3.585678,-2.434390,0.093225,6.373626,-7.021254,-6.991372,-5.827841,5.286922,-6.373419,-5.839717,8.866071,9.516177,7.867869,3.799624,8.709806,6.664357,-9.251270,-4.079881,-9.555683,-9.376787,-4.719118,8.464114,7.236451,-6.494969,8.669845,3.990215,-0.976922,-0.142899,-8.619088,-1.587690,2.230478,4.921717,-6.673200,4.404476,1.241979,3.510780,-6.544259,-5.095625,7.474959,-9.582380,-1.175092,-1.440765,-1.304905,-0.557357,-2.176221,-5.015260,-3.202551,3.452331,-0.680410,-8.696569,6.312912,6.940629,-5.087709,9.646591,-1.514952,-2.224942,-6.233155,6.937468,9.704071,8.399609,8.050127,3.509064,9.931295,-8.694584,-7.276125,-5.348508,-5.687471,2.942813,9.607564,1.077414,-1.437653,-7.435002,-8.014295,-2.128659,9.593234,5.093363,8.302072,0.784239,2.081621,-2.181674,-3.577866,1.033685,-9.242820,4.626567,-6.616815,-6.502222,-6.892406,2.183723,-3.953439,-4.887722,1.643897,-2.030754,5.735005,-4.017653,2.196575,-7.907143,7.396441,8.151310,-1.652236,8.548021,9.215428,-2.751931,8.513099,-2.793349,8.205469,6.569024,-0.574879,0.307872,4.158275,-7.244173,2.740494,-6.613788,4.631083,-1.624774,-0.292034,-4.874257,7.329299,9.293171,-5.278240,8.710285,8.872431,-3.310494,-8.614352,7.939594,0.858356,0.011584,-0.406956,1.879929,9.210937,2.861346,-8.440867,4.815721,-3.496045,-3.381108,-6.533408,-4.294996,-2.757973,6.154238,2.870062,4.519824,-0.910199,9.515105,-9.842775,-4.890713,-6.090984,-1.520829,2.999343,7.877177,-8.277511,-1.133905,3.800908,-2.982875,-3.698916,-7.891667,-6.398730,-1.170919,-3.946461,2.424272,2.288998,-1.133830,-8.667532,-4.522520,-8.860223,7.215668,5.910033,6.807921,0.554621,-3.118766,9.586783,8.399151,-5.463321,9.696239,3.619992,-7.462881,-8.758543,-9.797629,3.646649,0.111359,-4.180358,-3.746968,-4.558652,-9.172906,-0.843010,9.295078,-2.063059,6.566317,8.152224,5.453230,-9.443687,5.612423,3.363245,5.501109,-8.475704,-2.527587,6.363634,-3.728821,5.051210,4.849370,0.443850,8.991298,7.637681,3.830011,4.745011,8.901584,-1.891258,7.197285,2.924854,-8.139194,0.639639,-4.578796,7.175979,-5.721373,-5.653785,-2.559964,5.316338,1.027794,1.059305,8.555593,0.899754,-6.340563,8.833792,9.781785,-6.967434,-9.521630,7.477863,-5.117505,7.112312,7.388232,4.173659,7.431424,0.433323,9.853237,1.630160,-4.478271,-3.595804,-5.683777,-5.302205,-6.196373,9.798426,-4.616593,3.245297,-0.433890,5.457018,-4.740255,1.814446,2.204825,-0.696512,6.412665,1.443023,6.468757,-6.537031,8.188351,9.422132,6.943146,-6.564407,9.732012,4.105529,-4.373986,1.571388,7.585316,4.130809,-7.624169,6.998508,3.710814,1.042532,-7.531604,7.130554,-9.930712,9.428245,7.135003,0.726458,-7.031408,-1.307849,3.437611,0.124248,4.952317,-5.275693,7.037517,1.902066,-4.302975,0.438438,0.204491,8.643129,1.576064,5.881146,-3.761481,-1.333651,7.572838,-1.046266,-3.256192,2.871293,-0.926075,1.176371,-7.284368,-5.274664,2.416568,4.481836,-4.151848,-3.516248,-2.958562,9.490590,-8.669403,9.610584,-4.135514,4.904384,8.452290,-4.101869,-8.347601,6.675752,2.549126,4.959985,7.327095,5.329997,6.381805,-6.505085,7.963382,9.094952,1.309565,-9.096873,-8.429141,-2.835251,-4.268957,0.572120,6.996759,1.004927,-3.369101,2.122218,-4.124516,-4.750255,7.644425,3.736301,-6.927578,-5.587032,5.482874,0.264337,-0.716330,8.010749,8.930708,6.982939,-3.536790,2.832596,-6.033179,-4.887573,8.308064,-5.985113,5.197213,8.808137,-1.696286,5.956696,-6.057728,7.066882,2.195842,-0.116438,7.431222,5.234626,-2.161867,0.854623,2.760532,0.320122,-5.519046,0.369379,4.734129,4.728383,2.248988,8.759911,0.254168,-9.662314,-2.903621,5.104046,0.262492,3.657195,3.919366,-2.400327,-4.422715,7.905248,0.983173,3.782816,-6.426566,6.044173,3.522802,6.119490,4.681197,8.209829,-5.256865,-0.515130,4.537649,-6.866656,-3.609040,-4.042102,-0.456721,7.775583,-7.552651,3.829221,8.096162,-9.374185,8.784430,0.984094,-8.449549,-3.554552,-5.532513,-3.970720,-1.540243,-5.685893,4.860828,-0.068553,6.611425,6.218197,-8.141295,-0.542962,1.384465,-7.007527,-1.841134,-5.449204,5.509920,-7.376161,1.578616,1.688047,8.375960,-4.819501,-2.042194,-8.888983,-8.828673,-3.045050,-0.520928,-9.367244,8.407808,3.820520,-4.467219,-3.978202,-4.990963,2.148285,2.589381,-9.993721,5.665704,8.754913,8.220614,3.275245,-6.596102,-0.386201,-0.162198,-3.383155,9.253945,3.779268,9.986828,9.835070,-4.491738,0.122758,-3.179476,-6.276710,-2.921998,5.657329,-4.182662,1.731065,-1.780947,8.018396,-0.682651,4.301068,2.739584,-1.336833,-0.582696,5.820447,-9.552938,3.226836,-2.107719,-3.681946,1.533468,-9.823970,-7.509291,-7.675199,5.355854,6.088175,-2.954409,3.381771,-6.195036,-6.431403,-7.953243,9.478009,1.431930,4.987862,6.832916,-7.260373,2.650283,-3.295273,7.749808,7.791244,-1.552397,-7.280283,5.500807,6.687195,2.527436,-1.650185,2.454272,5.825439,-8.084376,-5.979352,-7.919843,2.597352,6.972668,-5.473970,-9.108480,2.971336,-3.288588,1.209240,0.518336,2.113062,2.988205,-8.742155,-9.023098,7.305542,-6.620470,-9.560578,-7.437224,3.862957,3.635080,-0.389624,8.902643,-1.772621,-1.620283,2.330654,-5.425022,-0.824663,-5.309314,-6.908720,-0.972549,-4.650503,4.433259,-0.194166,-4.206448,6.308038,9.705590,1.929735,9.252917,-2.593894,-9.886724,-7.973744,0.369252,-2.480553,1.109866,-1.146891,-8.588942,8.502270,4.032391,4.476207,3.351055,1.586873,8.704390,0.526010,-5.043927,-0.279991,3.191141,-6.491786,0.737190,-4.384847,1.193301,7.568787,8.582149,-9.533259,-8.257788,-0.763227,-8.994993,-3.740400,1.749287,9.124249,4.557874,-3.494217,-0.645914,6.823059,5.275836,-9.552755,-6.723573,-6.558399,-4.621424,-9.115236,-9.908787,-3.315817,-0.176893,-0.326877,-2.408417,-2.642164,8.249880,-3.090165,1.845519,-8.746036,-9.742920,6.109904,-6.392453,-5.556973,-0.192162,2.093407,-8.974921,-0.389141,-5.207632,-2.734244,-1.997040,-4.381246,1.910552,2.413651,2.820302,2.384092,-2.328980,-7.623145,-8.585660,-2.518642,-2.846010,2.209101,2.360521,2.102673,5.728215,9.441723,-9.806303,9.037175,-3.864826,-3.642984,-3.604696,9.703962,8.820075,2.130883,6.335852,-5.955785,7.990422,-0.676141,6.071188,-4.632373,3.144237,-6.510601,-3.661411,1.075037,-2.947719,-6.928201,3.003407,-2.484431,0.934130,-9.020483,9.617240,-4.084129,-5.029808,1.379991,9.270139,-2.654421,6.235854,-2.910380,8.482800,6.408852,-9.130991,-9.647486,4.849630,-9.387927,1.627200,6.894488,1.330692,6.605218,-7.779168,-3.826025,9.744016,-8.364061,4.938785,-5.573308,-4.398767,9.509119,6.154578,-0.296744,-2.022176,8.145266,8.766458,-8.223559,9.128157,5.660053,-7.590889,8.102112,-5.435055,4.519951,-1.794088,-7.936259,9.213297,2.837641,-8.255880,5.961655,-5.035868,-0.321533,-8.115559,0.119326,-3.533779,3.609843,-1.630133,-5.203988,5.901610,-0.576099,7.759312,-0.026675,-7.154635,7.964797,-0.522611,9.488842,-6.974347,-2.595932,-4.684755,-7.824771,-5.506562,-9.177705,-9.948318,-7.022235,-9.827579,1.229581,4.096264,-4.876830,-2.631929,-3.185907,-9.685972,8.184166,8.018993,4.083616,9.643616,6.916164,-6.678746,-2.205800,-3.829524,-7.004711,-9.463029,6.027244,8.298094,7.254441,0.434186,-5.886432,-8.525280,-4.441290,-5.193716,2.418203,4.625149,3.669193,-5.018998,-6.918100,-5.120497,1.700380,0.030772,9.537020,-9.323251,-7.414415,-7.377706,-5.925086,-1.401830,1.270886,-9.066323,6.636737,5.647282,0.713927,-9.476069,-7.878519,-5.950324,9.962986,-4.900492,3.452512,-5.118355,4.657079,-5.318273,1.891206,-6.237756,5.428738,4.125621,0.912374,-0.407224,5.307248,-5.838854,8.733075,8.311370,-1.266186,0.568456,5.927538,2.215004,6.689380,-4.500409,9.055920,0.078769,6.286237,0.705402,7.310963,-4.003429,-0.047672,-7.144618,8.490855,7.566472,-6.104465,1.605165,-1.525054,-6.894328,8.749205,-3.165965,5.690264,0.602210,-4.874506,8.229126,-5.946853,-9.482085,5.627199,3.137142,8.071025,-6.333472,9.252658,8.162856,6.980165,3.342280,-5.418558,0.750755,4.299211,-7.333025,6.788014,8.935676,2.781017,-3.337054,5.786074,-6.426201,-6.950090,-0.775186,-1.895651,4.987170,1.086681,-0.415632,-1.053454,7.951554,3.371948,-2.404715,-0.861119,-9.710648,5.325254,-5.390752,-2.547013,9.218533,7.104872,7.494922,8.995737,0.016302,2.485499,-3.339214,7.755994,-4.650567,-4.716809,9.699136,-2.812827,-9.730800,2.797668,-6.345145,8.052168,-5.640162,9.714003,6.372550,6.079055,5.309286,-5.107544,-9.786551,-4.569393,-9.895629,6.971743,0.002407,-1.323306,-9.106720,-9.479323,3.427071,-7.611421,-5.293781,8.202453,9.625253,2.896550,-0.523427,-3.805160,3.945960,6.655113,6.881718,-8.107183,-8.675875,2.870520,-4.432898,-9.180999,6.819474,6.008494,-3.618201,3.063319,4.755188,4.574951,4.666330,4.455724,-6.821243,-2.502449,5.441380,-0.451461,7.938421,-5.921120,5.305370,-4.952942,-0.921971,-6.534398,-7.533722,-7.185365,-2.454012,2.778537,5.327041,2.255665,0.162231,-9.603766,-0.341430,4.531290,-2.194643,2.966621,-8.157304,-1.622532,3.155831,2.049744,7.282196,-3.220613,8.497095,9.675131,-3.943976,-1.530423,-5.742193,-4.974487,5.719225,0.273555,-8.950580,8.180052,-4.797940,3.584976,7.520606,9.946560,-3.325851,-9.352319,-5.536805,-1.653185,-5.011110,-0.244691,6.455495,8.165310,-8.485951,-7.449912,2.811251,2.021100,-7.188525,-4.085357,-6.606652,-4.221427,0.607327,-1.726004,-3.859023,-9.357490,-5.323163,2.714905,9.916333,-0.255135,5.423488,-9.690415,9.463787,-7.579779,-6.447420,1.792899,7.174971,1.602464,-8.982350,-2.793155,2.060869,-4.403864,8.775544,3.413874,-6.504761,2.060333,4.134598,5.358867,3.775577,-3.500979,-3.977783,-2.869742,2.035083,-7.180772,-4.048231,-5.818113,6.778351,0.560537,-2.106325,7.359172,-2.199899,3.863720,8.835140,-9.479759,-9.694720,-1.965124,-8.723419,-2.982430,5.053400,-4.109594,5.286477,7.954626,8.946745,-6.632542,1.878848,-4.577628,-0.760743,4.489370,-4.517550,-2.127532,-3.566411,6.902362,-4.377413,-3.246265,-1.882761,5.912263,0.864016,-3.286459,7.221781,9.817045,2.957142,-3.970471,3.766053,3.528820,-0.101597,-7.910337,-7.145267,4.086766,-7.411987,-0.376871,-5.808604,-1.269103,-2.021775,-2.976632,4.883045,9.234476,-3.018808,-5.136343,8.173250], dtype = "float64")#candidate|9933|(1500,)|const|float64
const_9934 = relay.const([-1,-3,1,7,1,-7,5,-7,-10,-7,7,5,9,6,-10,-4,-5,-7,10,-8,-5,9,-8,7,3,10,3,-1,-1,-2,4,-3,-4,5,-6,4,-9,-1,3,5,-10,-8,-2,7,-8,6,6,10,2,3,-10,9,-2,-4,-8,3,-4,3,1,-9,1,-10,-7,-7,8,6,7,-7,8,5,10,4,-2,2,-10,-4,-8,-8,-7,-3,4,-4,5,-1,-5,-8,8,-1,-10,-4,3,1,-4,-4,5,7,7,4,5,6,2,6,-8,10,9,-8,4,4,10,1,7,9,-1,7,-6,7,9,-10,8,4,-8,10,2,1,1,-9,10,-2,9,-7,4,-7,-5,9,8,3,-8,7,-6,-3,-10,7,2,-9,1,-8,-7,-8,-1,-6,-4,5,1,-1,-10,-5,-9,-8,-2,-2,10,7,-4,-10,4,5,6,-10,-2,5,5,2,-2,3,-7,4,4,9,-6,4,-6,10,9,-2,-8,2,-8,-7,5,2,-6,3,8,9,-10,8,4,-1,-5,-3,-9,8,9,8,7,8,-8,5,-3,-2,9,-1,7,5,5,4,-3,3,-8,-8,1,-8,8,-7,-8,-6,-8,-10,-10,-6,3,1,4,7,-5,9,-10,-6,-2,9,-9,-9,-5,3,-5,10,-1,-3,-7,7,3,7,-2,-4,-6,-4,-10,-4,-1,-10,-8,-4,3,1,8,-1,3,6,1,-10,3,-1,-7,9,4,6,-10,-8,-8,3,7,8,-2,-5,-6,-1,1,3,-9,-7,2,4,6,6,-2,-1,-5,-1,5,1,3,2,3,1,10,4,1,-5,-1,10,-2,-4], dtype = "int64")#candidate|9934|(312,)|const|int64
var_9935 = relay.var("var_9935", dtype = "float32", shape = (168,))#candidate|9935|(168,)|var|float32
call_9932 = relay.TupleGetItem(func_7630_call(relay.reshape(const_9933.astype('float64'), [1500,]), relay.reshape(const_9934.astype('int64'), [312,]), relay.reshape(var_9935.astype('float32'), [168,]), ), 3)
call_9936 = relay.TupleGetItem(func_7635_call(relay.reshape(const_9933.astype('float64'), [1500,]), relay.reshape(const_9934.astype('int64'), [312,]), relay.reshape(var_9935.astype('float32'), [168,]), ), 3)
func_8605_call = mod.get_global_var('func_8605')
func_8607_call = mutated_mod.get_global_var('func_8607')
var_9944 = relay.var("var_9944", dtype = "float64", shape = (1764,))#candidate|9944|(1764,)|var|float64
call_9943 = relay.TupleGetItem(func_8605_call(relay.reshape(var_9944.astype('float64'), [14, 14, 9])), 1)
call_9945 = relay.TupleGetItem(func_8607_call(relay.reshape(var_9944.astype('float64'), [14, 14, 9])), 1)
var_9953 = relay.var("var_9953", dtype = "int64", shape = (312,))#candidate|9953|(312,)|var|int64
bop_9954 = relay.less_equal(const_9934.astype('bool'), relay.reshape(var_9953.astype('bool'), relay.shape_of(const_9934))) # shape=(312,)
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
const_9961 = relay.const([-2.955779,-0.820130,-6.702150,-4.921886,2.974024,8.387476,-4.765463,1.842833,-5.862641,5.333861,-2.645996,-6.239629,8.625836,-8.843605,-6.684431,-9.523216,9.548351,8.851439,-0.017966,-2.940938,-5.436542,-1.219354,-1.837776,5.292340,1.249141,-7.787909,-2.554623,-8.759160,4.079859,-6.034441,-1.297441,-7.700962,9.407386,-6.263721,0.226854,9.132769,-4.819774,8.966884,2.272796,0.220492,7.410624,7.845192,9.089621,7.786575,-9.035569,-6.176671,-0.023745,-2.736196,-7.174362,2.265345,0.595454,3.098679,8.897536,-3.707325,2.563509,7.691258,5.270369,-7.430361,4.368987,8.216619,8.495575,-1.725992,5.986596,2.630532,0.440308,2.726304,-4.396686,-5.350117,8.672165,-5.574414,4.005211,1.506222,-9.930863,8.605214,-1.260486,4.317078,-2.567711,7.599732,-5.497616,2.491755,-3.501400,5.357690,4.801699,-9.323368,-7.002149,7.416667,-2.124773,2.049435,-3.468513,-7.929441,3.598002,-5.375649,-2.547469,2.141335,-0.295801,-2.796983,-2.927700,2.864036,-2.143957,-3.975463,8.404639,-6.445953,8.839772,-7.908052,-0.616311,-7.873055,8.638019,1.516628,-2.700113,-4.183052,8.414341,2.296043,-9.496061,5.743901,-4.924554,-2.124407,2.029778,-2.448600,-2.249483,-4.401715,3.341189,-3.507457,2.122746,-0.694484,4.745063,-4.874259,-2.287498,-0.496943,2.245080,1.816889,0.123265,4.225313,-5.484651,8.026140,-4.112184,0.292949,-9.202327,-9.059926,8.310152,-8.020130,-8.968512,9.439500,-3.294535,7.620063,6.310484,-4.340941,-3.742296,5.803964,8.337654,6.180244], dtype = "float64")#candidate|9961|(150,)|const|float64
call_9960 = relay.TupleGetItem(func_5885_call(relay.reshape(const_9961.astype('float64'), [150,])), 3)
call_9962 = relay.TupleGetItem(func_5887_call(relay.reshape(const_9961.astype('float64'), [150,])), 3)
var_9963 = relay.var("var_9963", dtype = "float64", shape = (1500,))#candidate|9963|(1500,)|var|float64
bop_9964 = relay.bitwise_and(const_9933.astype('int32'), relay.reshape(var_9963.astype('int32'), relay.shape_of(const_9933))) # shape=(1500,)
func_9746_call = mod.get_global_var('func_9746')
func_9748_call = mutated_mod.get_global_var('func_9748')
call_9972 = func_9746_call()
call_9973 = func_9746_call()
func_7328_call = mod.get_global_var('func_7328')
func_7331_call = mutated_mod.get_global_var('func_7331')
const_9986 = relay.const([-6,-8,4,9,7,-3,2,4,-2,1,-1,7,1,-4,-10,6,3,-10,-5,-10,-9,-1,4,-8,-8,-8,8,-8,5,-9,-7,2,-9,9,-3,6,4,3,-5,-6,-2,3,-10,-6,2,-1,-2,-1,7,-7,-8,2,-2,-10,4,9,10,3,-10,-6,-6,-3,4,-9,3,1,1,-3,-8,10,-9,-7,1,-9,-3,-5,-4,7,-4,6,4,-9,3,-8,5,5,6,-2,-6,-8,-8,5,-3,7,-1,-7,4,-10,7,10,-5,-3,6,8,8,8,10,7,10,-3,7,-3,-3,10,10,-10,-2,6,2,-2,9,-6,5,-2,-5,5], dtype = "uint32")#candidate|9986|(126,)|const|uint32
call_9985 = relay.TupleGetItem(func_7328_call(relay.reshape(const_9986.astype('uint32'), [63, 2])), 7)
call_9987 = relay.TupleGetItem(func_7331_call(relay.reshape(const_9986.astype('uint32'), [63, 2])), 7)
func_8699_call = mod.get_global_var('func_8699')
func_8703_call = mutated_mod.get_global_var('func_8703')
var_9996 = relay.var("var_9996", dtype = "uint32", shape = ())#candidate|9996|()|var|uint32
call_9995 = relay.TupleGetItem(func_8699_call(relay.reshape(var_9996.astype('uint32'), []), relay.reshape(bop_9954.astype('int64'), [312,]), ), 3)
call_9997 = relay.TupleGetItem(func_8703_call(relay.reshape(var_9996.astype('uint32'), []), relay.reshape(bop_9954.astype('int64'), [312,]), ), 3)
output = relay.Tuple([bop_9928,call_9932,var_9935,call_9943,var_9944,bop_9954,call_9960,const_9961,bop_9964,call_9972,call_9985,const_9986,call_9995,var_9996,])
output2 = relay.Tuple([bop_9928,call_9936,var_9935,call_9945,var_9944,bop_9954,call_9962,const_9961,bop_9964,call_9973,call_9987,const_9986,call_9997,var_9996,])
func_9999 = relay.Function([var_9926,var_9935,var_9944,var_9953,var_9963,var_9996,], output)
mod['func_9999'] = func_9999
mod = relay.transform.InferType()(mod)
var_10000 = relay.var("var_10000", dtype = "uint8", shape = (4, 5, 7))#candidate|10000|(4, 5, 7)|var|uint8
var_10001 = relay.var("var_10001", dtype = "float32", shape = (168,))#candidate|10001|(168,)|var|float32
var_10002 = relay.var("var_10002", dtype = "float64", shape = (1764,))#candidate|10002|(1764,)|var|float64
var_10003 = relay.var("var_10003", dtype = "int64", shape = (312,))#candidate|10003|(312,)|var|int64
var_10004 = relay.var("var_10004", dtype = "float64", shape = (1500,))#candidate|10004|(1500,)|var|float64
var_10005 = relay.var("var_10005", dtype = "uint32", shape = ())#candidate|10005|()|var|uint32
output = func_9999(var_10000,var_10001,var_10002,var_10003,var_10004,var_10005,)
func_10006 = relay.Function([var_10000,var_10001,var_10002,var_10003,var_10004,var_10005,], output)
mutated_mod['func_10006'] = func_10006
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10036 = relay.var("var_10036", dtype = "int32", shape = (11, 2, 12))#candidate|10036|(11, 2, 12)|var|int32
var_10037 = relay.var("var_10037", dtype = "int32", shape = (11, 2, 12))#candidate|10037|(11, 2, 12)|var|int32
bop_10038 = relay.maximum(var_10036.astype('int32'), relay.reshape(var_10037.astype('int32'), relay.shape_of(var_10036))) # shape=(11, 2, 12)
var_10041 = relay.var("var_10041", dtype = "int32", shape = (11, 2, 12))#candidate|10041|(11, 2, 12)|var|int32
bop_10042 = relay.divide(bop_10038.astype('float64'), relay.reshape(var_10041.astype('float64'), relay.shape_of(bop_10038))) # shape=(11, 2, 12)
output = relay.Tuple([bop_10042,])
output2 = relay.Tuple([bop_10042,])
func_10047 = relay.Function([var_10036,var_10037,var_10041,], output)
mod['func_10047'] = func_10047
mod = relay.transform.InferType()(mod)
mutated_mod['func_10047'] = func_10047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10047_call = mutated_mod.get_global_var('func_10047')
var_10049 = relay.var("var_10049", dtype = "int32", shape = (11, 2, 12))#candidate|10049|(11, 2, 12)|var|int32
var_10050 = relay.var("var_10050", dtype = "int32", shape = (11, 2, 12))#candidate|10050|(11, 2, 12)|var|int32
var_10051 = relay.var("var_10051", dtype = "int32", shape = (11, 2, 12))#candidate|10051|(11, 2, 12)|var|int32
call_10048 = func_10047_call(var_10049,var_10050,var_10051,)
output = call_10048
func_10052 = relay.Function([var_10049,var_10050,var_10051,], output)
mutated_mod['func_10052'] = func_10052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8197_call = mod.get_global_var('func_8197')
func_8198_call = mutated_mod.get_global_var('func_8198')
call_10067 = func_8197_call()
call_10068 = func_8197_call()
output = relay.Tuple([call_10067,])
output2 = relay.Tuple([call_10068,])
func_10098 = relay.Function([], output)
mod['func_10098'] = func_10098
mod = relay.transform.InferType()(mod)
mutated_mod['func_10098'] = func_10098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10098_call = mutated_mod.get_global_var('func_10098')
call_10099 = func_10098_call()
output = call_10099
func_10100 = relay.Function([], output)
mutated_mod['func_10100'] = func_10100
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10105 = relay.var("var_10105", dtype = "int8", shape = (3, 8, 10))#candidate|10105|(3, 8, 10)|var|int8
var_10106 = relay.var("var_10106", dtype = "int8", shape = (3, 8, 10))#candidate|10106|(3, 8, 10)|var|int8
bop_10107 = relay.right_shift(var_10105.astype('int8'), relay.reshape(var_10106.astype('int8'), relay.shape_of(var_10105))) # shape=(3, 8, 10)
func_7553_call = mod.get_global_var('func_7553')
func_7554_call = mutated_mod.get_global_var('func_7554')
call_10114 = func_7553_call()
call_10115 = func_7553_call()
uop_10116 = relay.sqrt(var_10105.astype('float64')) # shape=(3, 8, 10)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_10123 = relay.TupleGetItem(func_5615_call(), 0)
call_10124 = relay.TupleGetItem(func_5617_call(), 0)
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
var_10137 = relay.var("var_10137", dtype = "float64", shape = (150,))#candidate|10137|(150,)|var|float64
call_10136 = relay.TupleGetItem(func_5885_call(relay.reshape(var_10137.astype('float64'), [150,])), 0)
call_10138 = relay.TupleGetItem(func_5887_call(relay.reshape(var_10137.astype('float64'), [150,])), 0)
output = relay.Tuple([bop_10107,call_10114,uop_10116,call_10123,call_10136,var_10137,])
output2 = relay.Tuple([bop_10107,call_10115,uop_10116,call_10124,call_10138,var_10137,])
func_10139 = relay.Function([var_10105,var_10106,var_10137,], output)
mod['func_10139'] = func_10139
mod = relay.transform.InferType()(mod)
var_10140 = relay.var("var_10140", dtype = "int8", shape = (3, 8, 10))#candidate|10140|(3, 8, 10)|var|int8
var_10141 = relay.var("var_10141", dtype = "int8", shape = (3, 8, 10))#candidate|10141|(3, 8, 10)|var|int8
var_10142 = relay.var("var_10142", dtype = "float64", shape = (150,))#candidate|10142|(150,)|var|float64
output = func_10139(var_10140,var_10141,var_10142,)
func_10143 = relay.Function([var_10140,var_10141,var_10142,], output)
mutated_mod['func_10143'] = func_10143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8874_call = mod.get_global_var('func_8874')
func_8875_call = mutated_mod.get_global_var('func_8875')
call_10203 = func_8874_call()
call_10204 = func_8874_call()
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_10214 = relay.TupleGetItem(func_5615_call(), 0)
call_10215 = relay.TupleGetItem(func_5617_call(), 0)
func_7588_call = mod.get_global_var('func_7588')
func_7590_call = mutated_mod.get_global_var('func_7590')
call_10220 = func_7588_call()
call_10221 = func_7588_call()
output = relay.Tuple([call_10203,call_10214,call_10220,])
output2 = relay.Tuple([call_10204,call_10215,call_10221,])
func_10222 = relay.Function([], output)
mod['func_10222'] = func_10222
mod = relay.transform.InferType()(mod)
output = func_10222()
func_10223 = relay.Function([], output)
mutated_mod['func_10223'] = func_10223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9746_call = mod.get_global_var('func_9746')
func_9748_call = mutated_mod.get_global_var('func_9748')
call_10262 = func_9746_call()
call_10263 = func_9746_call()
output = relay.Tuple([call_10262,])
output2 = relay.Tuple([call_10263,])
func_10292 = relay.Function([], output)
mod['func_10292'] = func_10292
mod = relay.transform.InferType()(mod)
output = func_10292()
func_10293 = relay.Function([], output)
mutated_mod['func_10293'] = func_10293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9422_call = mod.get_global_var('func_9422')
func_9423_call = mutated_mod.get_global_var('func_9423')
call_10368 = relay.TupleGetItem(func_9422_call(), 7)
call_10369 = relay.TupleGetItem(func_9423_call(), 7)
func_8444_call = mod.get_global_var('func_8444')
func_8448_call = mutated_mod.get_global_var('func_8448')
const_10371 = relay.const([6.994646,-1.876035,-6.671670,-8.670877,-4.711928,5.400836,3.106502,-5.547440,-5.517200,2.584968,-3.153597,7.070163,-5.400833,-9.393435,-5.736791,9.995074,-3.165959,2.809649,8.735564,-2.885112,-3.600557,9.166291,-6.907453,-5.432402], dtype = "float64")#candidate|10371|(24,)|const|float64
const_10372 = relay.const([3,3,2,8,6,-5,-7,-5,-9,-7,2,-4,8,10,10,-4,-1,-4,-8,7,2,-3,9,7,-6,6,8,6,6,3,7,-9,-4,-1,5,8,-10,-8,2,10,8,7,-5,-1,9,7,3,4,8,2,3,-3,-3,-5,-4,3,8,9,3,6,-6,-7,8,-8,9,10,-2,-7,3,7,5,-1,-2,-10,-10,8,-9,7,-8,-6,7,-9,10,-3,7,2,2,5,-2,10,1,-10,-4,-2,3,9,3,-8,-3,-7,1,-2,-1,-8,4,-8,7,-9,-4,1,-8,-7,8,5,-4,-4,2,-9,-5,-7,-6,-3,-5,-4,-3,6,7,4,9,-9,-4,10,-8,-8,-8,1,-1,9,-9,5,-1,-5,6,-6,-1,-8,9,-8,8,10,-2,-10,-7,9,3,10,-4,-2,6,-5,-4,-1,-2,-10,6,4,2,3,4,-5,-5,-1,-10,9,-1,-3,9,8,5,-10,1,-9,10,2,3,1,10,6,2,-4,-4,-10,10,-2,9,6,-6,2,-8,-7,10,8,9,2,3,-6,4,8,5,9,-2,3,1,-3,10,9,-10,-1,-2,10,-10,2,4,10,-2,3,-3,3,4,2,-7,-5,5,-6,1,-4,-4,-7,-8,8,-5,5,1,-1,-3,-8,-1,9,-9,6,-3,-2,-9,-3,-5,7,4,-7,8,-10,2,-1,-1,10,-5,9,-9,5,10,-2,-1,-5,1,-1,-2,1,-9,7,-5,9,5,10,-2,1,10,-9,4,-7,-5,-7,-9,1,3,7,6,9,-7,7,-1,1,2,4,3,-3,2,-7,8,-9,5,8,6,-5], dtype = "int64")#candidate|10372|(312,)|const|int64
call_10370 = relay.TupleGetItem(func_8444_call(relay.reshape(const_10371.astype('float64'), [24,]), relay.reshape(const_10372.astype('int64'), [6, 52]), ), 1)
call_10373 = relay.TupleGetItem(func_8448_call(relay.reshape(const_10371.astype('float64'), [24,]), relay.reshape(const_10372.astype('int64'), [6, 52]), ), 1)
output = relay.Tuple([call_10368,call_10370,const_10371,const_10372,])
output2 = relay.Tuple([call_10369,call_10373,const_10371,const_10372,])
func_10381 = relay.Function([], output)
mod['func_10381'] = func_10381
mod = relay.transform.InferType()(mod)
output = func_10381()
func_10382 = relay.Function([], output)
mutated_mod['func_10382'] = func_10382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8197_call = mod.get_global_var('func_8197')
func_8198_call = mutated_mod.get_global_var('func_8198')
call_10386 = func_8197_call()
call_10387 = func_8197_call()
func_884_call = mod.get_global_var('func_884')
func_887_call = mutated_mod.get_global_var('func_887')
const_10405 = relay.const([2,1,-2,-5,5,-4,2,9,10,10,9,-4,-6,-10,-7,-10,10,1,8,-9,-4,3,-8,7,-2,6,8,-10,7,7,-8,3,10,4,-9,-9,7,-1,4,-3,-5,-10,8,-7,7,-1,3,-4,9,1,10,-5,3,10,-3,6,3,-5,3,6,-8,-6,10,-3,8,10,-7,-7,-10,8,1,3,9,4,10,3,-6,10,-8,6,-9,6,-1,6,9,5,9,5,-8,1,9,-7,-4,-1,-1,10,5,-6,10,-6,-6,-10,-10,5,4,-5,2,5,8,6,-5,9,-4,-6,7,-3,4,-9,10,2,10,4,9,7,9,9,2,6,5,10,6,6,-9,-4,-3,-3,-4,-6,-10,2], dtype = "int64")#candidate|10405|(140,)|const|int64
call_10404 = relay.TupleGetItem(func_884_call(relay.reshape(const_10405.astype('int64'), [5, 14, 2])), 2)
call_10406 = relay.TupleGetItem(func_887_call(relay.reshape(const_10405.astype('int64'), [5, 14, 2])), 2)
output = relay.Tuple([call_10386,call_10404,const_10405,])
output2 = relay.Tuple([call_10387,call_10406,const_10405,])
func_10412 = relay.Function([], output)
mod['func_10412'] = func_10412
mod = relay.transform.InferType()(mod)
mutated_mod['func_10412'] = func_10412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10412_call = mutated_mod.get_global_var('func_10412')
call_10413 = func_10412_call()
output = call_10413
func_10414 = relay.Function([], output)
mutated_mod['func_10414'] = func_10414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8251_call = mod.get_global_var('func_8251')
func_8253_call = mutated_mod.get_global_var('func_8253')
call_10430 = relay.TupleGetItem(func_8251_call(), 0)
call_10431 = relay.TupleGetItem(func_8253_call(), 0)
func_9810_call = mod.get_global_var('func_9810')
func_9814_call = mutated_mod.get_global_var('func_9814')
const_10442 = relay.const([-2,6,-10,-4,1,1,-3,-6,-8,10,-9,10,4,10,-5,-7,4,6,4,-2,1,10,10,-1,-6,-6,-9,-10,-2,-8,3,-3,-1,-10,-8,3,-8,5,1,-8,-6,-4,1,-6,6,2,-1,6,-4,8,-9,-5,-4,-8,-6,-3,-3,7,-3,-8], dtype = "uint8")#candidate|10442|(60,)|const|uint8
const_10443 = relay.const([-9.786573,7.539762,7.617344,-4.267518,-7.123548,-5.429931,7.130631,2.037267,-3.828421,9.736133,9.747215,1.982865,-1.058090,-4.029403,-3.890217,6.923628,3.065944,3.729162], dtype = "float32")#candidate|10443|(18,)|const|float32
call_10441 = relay.TupleGetItem(func_9810_call(relay.reshape(const_10442.astype('uint8'), [60,]), relay.reshape(const_10443.astype('float32'), [18,]), ), 0)
call_10444 = relay.TupleGetItem(func_9814_call(relay.reshape(const_10442.astype('uint8'), [60,]), relay.reshape(const_10443.astype('float32'), [18,]), ), 0)
func_8444_call = mod.get_global_var('func_8444')
func_8448_call = mutated_mod.get_global_var('func_8448')
const_10451 = relay.const([[7.295700,-6.300271,-5.354948,-0.345012],[3.472202,8.945670,-1.459273,-2.139399],[1.597631,1.403559,8.663737,7.770634],[-3.944676,-6.015335,6.096978,5.083059],[3.223167,-8.452848,-3.468866,-4.753397],[8.606907,0.952466,-6.950086,3.486851]], dtype = "float64")#candidate|10451|(6, 4)|const|float64
const_10452 = relay.const([-8,3,8,1,1,-1,8,-1,-6,-6,-8,-1,-7,2,-6,1,3,-2,-9,2,2,-1,3,-7,-8,-1,-4,-1,-5,-4,-4,-9,-8,10,1,-7,3,-3,-3,7,-3,-8,-3,10,3,-10,-9,-6,7,4,7,-3,3,-9,8,6,6,-10,4,-8,-4,-4,7,-9,5,4,-7,2,-3,-4,9,-2,-5,-6,2,4,4,8,7,8,3,3,1,9,8,-6,-5,-4,3,-9,-5,3,-2,-1,-10,-10,2,-2,1,-6,-7,8,1,4,3,10,-6,-7,4,7,6,-7,-3,1,2,-4,10,-5,-7,4,2,-8,-7,-9,3,-8,-7,7,-6,5,6,9,3,-6,2,-2,5,7,7,6,-3,-8,9,-2,4,3,9,5,-5,-4,-10,-3,6,-9,-5,-4,-9,-1,-10,3,10,-5,9,3,-10,3,3,6,-8,-4,-2,-5,3,-9,-9,-6,-10,10,-10,5,9,-9,-6,4,10,8,6,-4,9,1,-8,9,-7,-9,-3,6,-2,4,2,3,6,5,-5,3,2,4,-3,2,-3,9,-5,5,2,7,-9,-5,2,-1,8,-2,9,10,8,-2,-3,6,5,-9,-3,10,-7,-9,4,-7,-5,3,-5,-4,7,6,6,-1,-3,10,7,2,-7,-4,-2,-5,9,8,1,9,-7,-9,6,4,10,-7,-3,10,9,-3,6,7,4,-1,7,-6,-4,-7,-4,-2,-6,1,10,-1,7,2,-10,9,4,2,8,10,-2,4,10,2,7,-5,-7,7,-10,7,8,5,-4,7,-6,7,4,8,9,9,-5,4,1,-6,-10,1], dtype = "int64")#candidate|10452|(312,)|const|int64
call_10450 = relay.TupleGetItem(func_8444_call(relay.reshape(const_10451.astype('float64'), [24,]), relay.reshape(const_10452.astype('int64'), [6, 52]), ), 5)
call_10453 = relay.TupleGetItem(func_8448_call(relay.reshape(const_10451.astype('float64'), [24,]), relay.reshape(const_10452.astype('int64'), [6, 52]), ), 5)
func_7630_call = mod.get_global_var('func_7630')
func_7635_call = mutated_mod.get_global_var('func_7635')
var_10457 = relay.var("var_10457", dtype = "float64", shape = (1500,))#candidate|10457|(1500,)|var|float64
var_10458 = relay.var("var_10458", dtype = "float32", shape = (168,))#candidate|10458|(168,)|var|float32
call_10456 = relay.TupleGetItem(func_7630_call(relay.reshape(var_10457.astype('float64'), [1500,]), relay.reshape(const_10452.astype('int64'), [312,]), relay.reshape(var_10458.astype('float32'), [168,]), ), 5)
call_10459 = relay.TupleGetItem(func_7635_call(relay.reshape(var_10457.astype('float64'), [1500,]), relay.reshape(const_10452.astype('int64'), [312,]), relay.reshape(var_10458.astype('float32'), [168,]), ), 5)
output = relay.Tuple([call_10430,call_10441,const_10442,const_10443,call_10450,const_10451,const_10452,call_10456,var_10457,var_10458,])
output2 = relay.Tuple([call_10431,call_10444,const_10442,const_10443,call_10453,const_10451,const_10452,call_10459,var_10457,var_10458,])
func_10460 = relay.Function([var_10457,var_10458,], output)
mod['func_10460'] = func_10460
mod = relay.transform.InferType()(mod)
mutated_mod['func_10460'] = func_10460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10460_call = mutated_mod.get_global_var('func_10460')
var_10462 = relay.var("var_10462", dtype = "float64", shape = (1500,))#candidate|10462|(1500,)|var|float64
var_10463 = relay.var("var_10463", dtype = "float32", shape = (168,))#candidate|10463|(168,)|var|float32
call_10461 = func_10460_call(var_10462,var_10463,)
output = call_10461
func_10464 = relay.Function([var_10462,var_10463,], output)
mutated_mod['func_10464'] = func_10464
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10472 = relay.var("var_10472", dtype = "float64", shape = (8, 2, 1))#candidate|10472|(8, 2, 1)|var|float64
var_10473 = relay.var("var_10473", dtype = "float64", shape = (8, 2, 1))#candidate|10473|(8, 2, 1)|var|float64
bop_10474 = relay.divide(var_10472.astype('float64'), relay.reshape(var_10473.astype('float64'), relay.shape_of(var_10472))) # shape=(8, 2, 1)
output = bop_10474
output2 = bop_10474
func_10480 = relay.Function([var_10472,var_10473,], output)
mod['func_10480'] = func_10480
mod = relay.transform.InferType()(mod)
mutated_mod['func_10480'] = func_10480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10480_call = mutated_mod.get_global_var('func_10480')
var_10482 = relay.var("var_10482", dtype = "float64", shape = (8, 2, 1))#candidate|10482|(8, 2, 1)|var|float64
var_10483 = relay.var("var_10483", dtype = "float64", shape = (8, 2, 1))#candidate|10483|(8, 2, 1)|var|float64
call_10481 = func_10480_call(var_10482,var_10483,)
output = call_10481
func_10484 = relay.Function([var_10482,var_10483,], output)
mutated_mod['func_10484'] = func_10484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7553_call = mod.get_global_var('func_7553')
func_7554_call = mutated_mod.get_global_var('func_7554')
call_10488 = func_7553_call()
call_10489 = func_7553_call()
output = call_10488
output2 = call_10489
func_10496 = relay.Function([], output)
mod['func_10496'] = func_10496
mod = relay.transform.InferType()(mod)
mutated_mod['func_10496'] = func_10496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10496_call = mutated_mod.get_global_var('func_10496')
call_10497 = func_10496_call()
output = call_10497
func_10498 = relay.Function([], output)
mutated_mod['func_10498'] = func_10498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10381_call = mod.get_global_var('func_10381')
func_10382_call = mutated_mod.get_global_var('func_10382')
call_10519 = relay.TupleGetItem(func_10381_call(), 1)
call_10520 = relay.TupleGetItem(func_10382_call(), 1)
output = relay.Tuple([call_10519,])
output2 = relay.Tuple([call_10520,])
func_10525 = relay.Function([], output)
mod['func_10525'] = func_10525
mod = relay.transform.InferType()(mod)
mutated_mod['func_10525'] = func_10525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10525_call = mutated_mod.get_global_var('func_10525')
call_10526 = func_10525_call()
output = call_10526
func_10527 = relay.Function([], output)
mutated_mod['func_10527'] = func_10527
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10636 = relay.var("var_10636", dtype = "float64", shape = (10, 7, 10))#candidate|10636|(10, 7, 10)|var|float64
uop_10637 = relay.exp(var_10636.astype('float64')) # shape=(10, 7, 10)
output = relay.Tuple([uop_10637,])
output2 = relay.Tuple([uop_10637,])
func_10644 = relay.Function([var_10636,], output)
mod['func_10644'] = func_10644
mod = relay.transform.InferType()(mod)
var_10645 = relay.var("var_10645", dtype = "float64", shape = (10, 7, 10))#candidate|10645|(10, 7, 10)|var|float64
output = func_10644(var_10645)
func_10646 = relay.Function([var_10645], output)
mutated_mod['func_10646'] = func_10646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6121_call = mod.get_global_var('func_6121')
func_6123_call = mutated_mod.get_global_var('func_6123')
call_10683 = func_6121_call()
call_10684 = func_6121_call()
output = relay.Tuple([call_10683,])
output2 = relay.Tuple([call_10684,])
func_10702 = relay.Function([], output)
mod['func_10702'] = func_10702
mod = relay.transform.InferType()(mod)
output = func_10702()
func_10703 = relay.Function([], output)
mutated_mod['func_10703'] = func_10703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6963_call = mod.get_global_var('func_6963')
func_6964_call = mutated_mod.get_global_var('func_6964')
call_10732 = func_6963_call()
call_10733 = func_6963_call()
output = call_10732
output2 = call_10733
func_10754 = relay.Function([], output)
mod['func_10754'] = func_10754
mod = relay.transform.InferType()(mod)
mutated_mod['func_10754'] = func_10754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10754_call = mutated_mod.get_global_var('func_10754')
call_10755 = func_10754_call()
output = call_10755
func_10756 = relay.Function([], output)
mutated_mod['func_10756'] = func_10756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_10838 = relay.TupleGetItem(func_5615_call(), 0)
call_10839 = relay.TupleGetItem(func_5617_call(), 0)
var_10861 = relay.var("var_10861", dtype = "float64", shape = (15, 2, 13))#candidate|10861|(15, 2, 13)|var|float64
bop_10862 = relay.equal(call_10838.astype('bool'), relay.reshape(var_10861.astype('bool'), relay.shape_of(call_10838))) # shape=(15, 2, 13)
bop_10865 = relay.equal(call_10839.astype('bool'), relay.reshape(var_10861.astype('bool'), relay.shape_of(call_10839))) # shape=(15, 2, 13)
func_1272_call = mod.get_global_var('func_1272')
func_1275_call = mutated_mod.get_global_var('func_1275')
const_10867 = relay.const([[-5],[-10],[-1],[7],[2],[-5],[8],[-3],[-7],[1],[5],[-8],[9],[3],[-9],[4],[7],[10],[-4],[7],[5],[-7],[9],[-9],[-9],[8],[-8],[-7],[2],[-6],[-2],[-9],[-4],[-4],[-6],[-4],[-2],[5],[-3],[10],[5],[-5],[4],[1],[-3],[-9],[7],[1],[-6],[2],[7],[4],[1],[1],[-6],[-7],[8],[-5],[4],[-10],[-2],[2],[-6],[-5],[-2],[-4],[-6],[-8],[-10],[2],[-9],[6],[-1],[-2],[6],[3],[-3],[-9],[10],[1],[2],[-8],[-4],[5],[5],[-9],[-6],[-6],[5],[-1],[-1],[8],[9],[-3],[3],[10],[-9],[-4],[-7],[8],[-6],[-8],[1],[9],[-1],[-6],[-7],[6],[-4],[-7],[-3],[10],[7],[7],[-3],[-8],[2],[-3],[-10],[-9],[-5],[5],[9],[-1],[2],[-10],[7],[9],[6],[-8],[2],[9],[-1],[-7],[5],[4],[-2],[3],[2],[-6],[4],[-9],[6],[2],[7],[10],[-5],[-1],[9],[7],[-7],[3],[2],[1],[-10],[6],[3],[-4],[7],[-8],[8],[-2],[-6],[1],[-5]], dtype = "uint8")#candidate|10867|(165, 1)|const|uint8
call_10866 = func_1272_call(relay.reshape(const_10867.astype('uint8'), [15, 11, 1]))
call_10868 = func_1272_call(relay.reshape(const_10867.astype('uint8'), [15, 11, 1]))
output = relay.Tuple([bop_10862,call_10866,const_10867,])
output2 = relay.Tuple([bop_10865,call_10868,const_10867,])
func_10874 = relay.Function([var_10861,], output)
mod['func_10874'] = func_10874
mod = relay.transform.InferType()(mod)
mutated_mod['func_10874'] = func_10874
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10875 = relay.var("var_10875", dtype = "float64", shape = (15, 2, 13))#candidate|10875|(15, 2, 13)|var|float64
func_10874_call = mutated_mod.get_global_var('func_10874')
call_10876 = func_10874_call(var_10875)
output = call_10876
func_10877 = relay.Function([var_10875], output)
mutated_mod['func_10877'] = func_10877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7674_call = mod.get_global_var('func_7674')
func_7675_call = mutated_mod.get_global_var('func_7675')
call_10901 = relay.TupleGetItem(func_7674_call(), 0)
call_10902 = relay.TupleGetItem(func_7675_call(), 0)
output = call_10901
output2 = call_10902
func_10909 = relay.Function([], output)
mod['func_10909'] = func_10909
mod = relay.transform.InferType()(mod)
mutated_mod['func_10909'] = func_10909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10909_call = mutated_mod.get_global_var('func_10909')
call_10910 = func_10909_call()
output = call_10910
func_10911 = relay.Function([], output)
mutated_mod['func_10911'] = func_10911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6512_call = mod.get_global_var('func_6512')
func_6514_call = mutated_mod.get_global_var('func_6514')
call_10953 = relay.TupleGetItem(func_6512_call(), 1)
call_10954 = relay.TupleGetItem(func_6514_call(), 1)
output = relay.Tuple([call_10953,])
output2 = relay.Tuple([call_10954,])
func_10957 = relay.Function([], output)
mod['func_10957'] = func_10957
mod = relay.transform.InferType()(mod)
mutated_mod['func_10957'] = func_10957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10957_call = mutated_mod.get_global_var('func_10957')
call_10958 = func_10957_call()
output = call_10958
func_10959 = relay.Function([], output)
mutated_mod['func_10959'] = func_10959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8197_call = mod.get_global_var('func_8197')
func_8198_call = mutated_mod.get_global_var('func_8198')
call_11032 = func_8197_call()
call_11033 = func_8197_call()
output = call_11032
output2 = call_11033
func_11037 = relay.Function([], output)
mod['func_11037'] = func_11037
mod = relay.transform.InferType()(mod)
output = func_11037()
func_11038 = relay.Function([], output)
mutated_mod['func_11038'] = func_11038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11037_call = mod.get_global_var('func_11037')
func_11038_call = mutated_mod.get_global_var('func_11038')
call_11061 = func_11037_call()
call_11062 = func_11037_call()
func_10098_call = mod.get_global_var('func_10098')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_11068 = relay.TupleGetItem(func_10098_call(), 0)
call_11069 = relay.TupleGetItem(func_10100_call(), 0)
output = relay.Tuple([call_11061,call_11068,])
output2 = relay.Tuple([call_11062,call_11069,])
func_11075 = relay.Function([], output)
mod['func_11075'] = func_11075
mod = relay.transform.InferType()(mod)
output = func_11075()
func_11076 = relay.Function([], output)
mutated_mod['func_11076'] = func_11076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10381_call = mod.get_global_var('func_10381')
func_10382_call = mutated_mod.get_global_var('func_10382')
call_11089 = relay.TupleGetItem(func_10381_call(), 0)
call_11090 = relay.TupleGetItem(func_10382_call(), 0)
output = call_11089
output2 = call_11090
func_11112 = relay.Function([], output)
mod['func_11112'] = func_11112
mod = relay.transform.InferType()(mod)
output = func_11112()
func_11113 = relay.Function([], output)
mutated_mod['func_11113'] = func_11113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10412_call = mod.get_global_var('func_10412')
func_10414_call = mutated_mod.get_global_var('func_10414')
call_11152 = relay.TupleGetItem(func_10412_call(), 0)
call_11153 = relay.TupleGetItem(func_10414_call(), 0)
output = call_11152
output2 = call_11153
func_11156 = relay.Function([], output)
mod['func_11156'] = func_11156
mod = relay.transform.InferType()(mod)
output = func_11156()
func_11157 = relay.Function([], output)
mutated_mod['func_11157'] = func_11157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7588_call = mod.get_global_var('func_7588')
func_7590_call = mutated_mod.get_global_var('func_7590')
call_11185 = func_7588_call()
call_11186 = func_7588_call()
output = relay.Tuple([call_11185,])
output2 = relay.Tuple([call_11186,])
func_11208 = relay.Function([], output)
mod['func_11208'] = func_11208
mod = relay.transform.InferType()(mod)
output = func_11208()
func_11209 = relay.Function([], output)
mutated_mod['func_11209'] = func_11209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8834_call = mod.get_global_var('func_8834')
func_8835_call = mutated_mod.get_global_var('func_8835')
call_11219 = relay.TupleGetItem(func_8834_call(), 0)
call_11220 = relay.TupleGetItem(func_8835_call(), 0)
output = relay.Tuple([call_11219,])
output2 = relay.Tuple([call_11220,])
func_11221 = relay.Function([], output)
mod['func_11221'] = func_11221
mod = relay.transform.InferType()(mod)
mutated_mod['func_11221'] = func_11221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11221_call = mutated_mod.get_global_var('func_11221')
call_11222 = func_11221_call()
output = call_11222
func_11223 = relay.Function([], output)
mutated_mod['func_11223'] = func_11223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10381_call = mod.get_global_var('func_10381')
func_10382_call = mutated_mod.get_global_var('func_10382')
call_11257 = relay.TupleGetItem(func_10381_call(), 3)
call_11258 = relay.TupleGetItem(func_10382_call(), 3)
output = relay.Tuple([call_11257,])
output2 = relay.Tuple([call_11258,])
func_11266 = relay.Function([], output)
mod['func_11266'] = func_11266
mod = relay.transform.InferType()(mod)
output = func_11266()
func_11267 = relay.Function([], output)
mutated_mod['func_11267'] = func_11267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9130_call = mod.get_global_var('func_9130')
func_9132_call = mutated_mod.get_global_var('func_9132')
call_11404 = relay.TupleGetItem(func_9130_call(), 1)
call_11405 = relay.TupleGetItem(func_9132_call(), 1)
output = relay.Tuple([call_11404,])
output2 = relay.Tuple([call_11405,])
func_11413 = relay.Function([], output)
mod['func_11413'] = func_11413
mod = relay.transform.InferType()(mod)
mutated_mod['func_11413'] = func_11413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11413_call = mutated_mod.get_global_var('func_11413')
call_11414 = func_11413_call()
output = call_11414
func_11415 = relay.Function([], output)
mutated_mod['func_11415'] = func_11415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7674_call = mod.get_global_var('func_7674')
func_7675_call = mutated_mod.get_global_var('func_7675')
call_11426 = relay.TupleGetItem(func_7674_call(), 0)
call_11427 = relay.TupleGetItem(func_7675_call(), 0)
func_6574_call = mod.get_global_var('func_6574')
func_6578_call = mutated_mod.get_global_var('func_6578')
const_11429 = relay.const([-7,-1,-2,-6,-8,-6,-8,-3,1,3,5,-1,6,1,6,10,-8,2,5,-10,5,-1,7,6,-7,7,2,-1,6,10,5,-7,1,2,5,9,5,3,-4,-7,-9,3,6,2,5,4,-2,-4,8,10,-7,5,1,-2,-10,7,7,3,-5,5], dtype = "uint8")#candidate|11429|(60,)|const|uint8
call_11428 = relay.TupleGetItem(func_6574_call(relay.reshape(const_11429.astype('uint8'), [15, 4]), relay.reshape(call_11426.astype('float64'), [15, 2, 13]), ), 3)
call_11430 = relay.TupleGetItem(func_6578_call(relay.reshape(const_11429.astype('uint8'), [15, 4]), relay.reshape(call_11426.astype('float64'), [15, 2, 13]), ), 3)
output = relay.Tuple([call_11426,call_11428,const_11429,])
output2 = relay.Tuple([call_11427,call_11430,const_11429,])
func_11438 = relay.Function([], output)
mod['func_11438'] = func_11438
mod = relay.transform.InferType()(mod)
output = func_11438()
func_11439 = relay.Function([], output)
mutated_mod['func_11439'] = func_11439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11469 = relay.var("var_11469", dtype = "float32", shape = (15, 15, 6))#candidate|11469|(15, 15, 6)|var|float32
uop_11470 = relay.sigmoid(var_11469.astype('float32')) # shape=(15, 15, 6)
uop_11480 = relay.atan(var_11469.astype('float64')) # shape=(15, 15, 6)
func_11266_call = mod.get_global_var('func_11266')
func_11267_call = mutated_mod.get_global_var('func_11267')
call_11484 = relay.TupleGetItem(func_11266_call(), 0)
call_11485 = relay.TupleGetItem(func_11267_call(), 0)
bop_11493 = relay.greater(uop_11480.astype('bool'), relay.reshape(var_11469.astype('bool'), relay.shape_of(uop_11480))) # shape=(15, 15, 6)
uop_11499 = relay.asinh(var_11469.astype('float64')) # shape=(15, 15, 6)
func_5919_call = mod.get_global_var('func_5919')
func_5923_call = mutated_mod.get_global_var('func_5923')
const_11519 = relay.const([-9.292423,2.554935,-6.041575,1.197198,0.591120,-3.871711,-3.212212,-4.664012,-2.578530,-3.980706,2.978971,-7.030156,0.305255,-9.297703,-0.204098,6.332538,9.404943,9.229963,7.759312,-9.045375,-7.580018,-2.920769,5.934461,-6.728816,-8.296547,6.502408,-5.068544,1.142268,-3.016268,-1.477708,8.926979,5.529259,-9.175066,8.342284,2.962012,-5.655756,-2.329551,-9.328009,0.553436,4.238529,9.187038,0.835729,-6.459816,8.208840,-7.318421,6.509391,3.782580,8.269307,-0.908439,5.696661,-7.952941,0.509311,9.027142,9.883798,-3.596148,-7.973016,5.671001,4.830614,-7.628082,-8.477276,1.328544,5.722899,-7.016468,-1.620831,9.745891,6.053218,-0.653742,-0.251291,-9.525684,-5.732056,-6.870442,3.158067,4.092271,0.509740,3.447939,-7.811425,4.115144,-7.980057,-9.619054,-0.901731,-9.381272,-1.391132,-8.449748,-5.708950,-2.351372,5.288592,-8.136832,-0.878102,-2.610379,3.201770,6.879235,-2.940001,5.548818,-3.156450,3.090828,3.891517,-4.137365,-1.553568,-3.644235,-3.562240,-2.795502,1.788890,-0.079451,-6.781203,5.035366,-5.199586,6.617851,-1.693813,8.270308,2.613453,9.411698,9.553982,-4.835921,2.348978,-8.366297,7.208775,3.084963,0.822969,-2.727981,-1.936766,-1.455992,-8.763121,2.258284,-8.039163,7.602373,-3.175222,4.425751,8.475968,0.360843,-4.608924,-8.404243,-4.005315,7.787915,1.736465,4.327341,6.022384,-6.730196,-1.924438,-3.277142,2.748046,-9.887229,0.759563,0.371436,5.443635,9.282326,-0.482530,6.004179,7.152243,2.484949,-8.291861,3.278193,-8.562779,7.000623,5.449345,3.493031,8.545927,-9.531642,3.683454,2.446745,0.747356,8.765051,-5.771164,-2.703788,5.508165,-0.721383,5.547801,8.537789,-6.321648,-0.820751,8.904015,-0.743355,7.340858,7.112772,-0.229247,3.859671,8.446980,0.211549,2.076840,5.394635,6.927781,-3.631852,2.146564,-3.006685,-8.948330,-9.939009,8.918591,-0.022118,9.160925,1.958736,9.877936,7.473546,5.475054,-1.173114,4.794324,6.361755,-8.520463,7.129459,-9.545470,2.851965,-3.778473,-0.250107,-6.861682,-6.956293,-3.209841,9.787356,-2.045639,-0.659038,5.671193,-0.556477,-9.597938,-0.837448,1.280907,1.107727,5.973779,-7.237054,-0.350152,8.593206,7.891335,-2.073884,-8.293652,0.842658,4.133243,-2.624109,4.769646,7.088179,0.801157,-2.396247,8.188005,-9.812657,-6.949810,-6.246796,6.184934,7.793804,4.582630,-7.213442,7.422514,-9.897705,0.638036,6.996898,9.696529,-2.778996,-4.838997,2.756849,-0.160271,0.473667,-9.766407,3.180122,4.221414,-3.652626,8.983027,-0.989916,9.960438,3.551178,-3.468285,2.962796,1.365025,-0.654817,-4.072107,8.054677,3.882472,0.529743,-2.913668,5.900803,1.621149,-0.395529,-8.290963,3.927078,8.891410,-1.786042,4.279059,7.623695,3.608508,6.926298,7.991703,1.234399,1.148477,-4.268221,8.131884,0.054208,9.206420,3.257014,3.786400,7.745307,3.264156,-3.161240,1.397282,9.178655,7.197514,-5.884933,0.301655,6.259111,-1.044800,-0.126441,2.455967,-5.136378,7.340913,-2.509184,-8.257068,0.737127,2.555098,2.805455,3.328309,2.297313,0.299899,9.028663,2.174290,9.387314,-7.869792,-5.901002,9.364475,3.646947,-1.073846,2.643001,7.184460,5.595267,-4.136714,-6.614371,0.627971,-7.054754,2.531673,-9.331732,-5.337004,7.768018,5.594878,-3.986575,-7.377276,-9.300581,8.658936,-5.877560,-2.075831,2.555323,-3.407590,0.286062,-1.976287,-4.437854,7.251573,-0.870583,-5.597075,5.589176,9.705910,-4.361724,7.381826,7.109550,5.584791,3.523019,2.522023,-5.391987,-7.631240,6.763662,-5.069580,5.316471,-3.610098,6.964356,3.692675,5.671048,3.787399,-6.739958,-7.345755,4.719898,9.904749,0.466206,-3.999003,-0.276538,5.260612,9.464293,2.241050,-5.544971,-8.179447,-4.058913,-0.490633,0.512715,-7.823059,-6.904945,1.467404,-6.676697,-3.808710,7.766683,8.139571,-8.320766,7.931988,-4.821471,-5.933118,3.403680,1.710604,-5.552257,0.029350,2.404155,3.315332,-0.221805,4.615029,-9.915314,-8.379169,-8.668421,7.010451,7.646341,-9.916484,-1.835186,-4.960045,-0.621306,5.210180,8.446811,-9.903090,-6.367018,-0.437632,-0.826491,4.711544,4.145298,-5.283186,-6.637219,-0.206123,-8.785909,1.116929,0.186003,-8.383947,3.010981,-8.531607,-5.667329,2.100310,6.451528,2.010576,-1.068241,-5.215610,8.284490,4.191431,-2.364462,4.360410,7.328570,7.963340,-0.864362,-5.573522,-0.466864,-4.539363,0.299333,7.721862,6.924079,-7.821915,-0.891585,6.407953,8.492777,6.354054,1.217461,-0.142371,1.294775,9.403287,-0.812290,-8.043600,0.982271,4.875119,-1.321703,1.288553,-0.304039,7.619502,-5.271598,-7.695281,-6.793492,1.419058,-7.891665,-9.510246,-5.607072,1.280887,4.599083,0.284257,-2.719101,4.519109,0.045024,-8.840928,-5.133921,-5.990963,-7.749529,-6.962775,-0.654192,-8.975602,5.766099,6.446401,7.794598,-0.287507,-6.267299,4.533952,8.498764,9.375954,9.614204,-0.229648,-7.892967,-1.184097,9.926452,3.165664,-5.950494,-3.167516,-4.965853,7.198544,-3.795885,-2.347694,8.122807,0.696202,-0.077574,-7.926722,-6.352245,2.886770,3.769630,9.197700,-0.542184,5.188707,1.277615,-3.996657,4.118216,5.589986,-5.583549,-8.109604,6.559789,-7.363224,-3.973635,2.193356,5.687286,3.332204,-2.212931,0.993901,3.796267,9.518414,-6.014034,-8.378596,-4.637481,2.716100,4.629229,-9.781762,4.988806,-6.454402,0.755138,-3.428579,-3.458325,-2.987705,-3.804028,9.429395,-2.551066,-1.111810,0.804981,-1.977744,-9.934381,-8.354872,6.097657,-6.678899,1.411873,-4.825053,-2.088004,6.298772,0.214930,8.650416,4.640390,8.013214,-3.106030,-1.433271,2.598321,2.213497,-8.171443,9.287567,-4.706779,-2.037263,6.100583,1.135271,9.003219,-9.895784,-8.843845,-5.645713,9.487412,2.892118,-3.062371,9.018991,-4.349087,9.289324,-7.685845,-4.634686,3.015605,-5.565141,1.638293,-1.675160,-1.563158,3.559838,8.169310,-1.051631,-5.355779,-4.455368,4.924962,-0.172325,-5.055315,-9.523534,-8.895173,2.245904,3.116954,-6.162627,2.127158,8.113220,-1.299092,-6.407565,-3.682434,-3.390380,-3.083953,2.304649,-8.294091,9.726514,-0.575458,7.763834,-7.986457,-7.093282,-7.468668,7.697587,3.263406,7.278766,4.942494,2.717826,-8.541071,-1.442751,-5.111125,-1.997738,3.194148,8.351248,3.995914,8.300492,-7.486127,9.153385,-0.394222,-3.242879,1.725686,5.524860,-2.486862,-3.406252,-7.739873,4.558536,3.278380,6.553194,-6.611114,-5.865312,4.032554,6.490763,7.915403,-1.904559,0.654700,4.824854,-0.997480,-7.095732,-4.504187,6.372147,5.167593,1.009921,-2.892916,-9.380378,-1.894812,-1.972506,-5.382255,0.160095,-0.573260,4.671829,-2.717770,-2.731661,-5.570846,1.100136,-7.148996,3.235886,-0.388452,-6.319851,-4.000336,0.371862,0.328302,-7.722000,1.038372,0.980687,-8.284786,-6.610373,3.995574,0.985648,3.584172,-6.982898,-6.693021,9.385509,6.734727,3.644925,-0.862031,-5.146905,3.696426,9.604411,-4.870472,-2.614224,-3.804141,2.576144,-8.314466,2.381623,-8.201321,7.960371,8.732424,0.941244,-4.135744,-2.315777,7.947428,-5.617919,-0.398764,3.035675,-6.580693,1.204894,-2.396996,-3.681196,9.757097,-3.362888,-3.929081,-7.282459,1.663704,-7.179024,9.105587,-1.098668,8.151579,9.214565,3.048224,-9.525089,-6.735267,-9.183235,-3.217892,6.433269,-4.897156,9.794225,5.196060,-9.364535,7.330975,-6.814094,-8.928052,0.911932,0.642113,0.106089,-2.458696,-4.938462,3.985524,2.082717,-3.048766,5.802062,3.043389,4.541096,6.935001,6.058996,-7.291273,8.958952,-1.575817,-5.997808,6.937466,-8.583017,9.925404,-6.819852,4.885094,-2.107786,8.151714,-4.391434,7.271954,8.946495,-7.729120,6.110298,1.321927,7.219099,-6.923239,9.679062,6.429159,8.175378,6.202646,4.531382,5.113490,-4.379211,8.094672,7.500056,-8.236083,5.710105,3.863534,0.870460,9.453894,7.796434,-1.417723,3.059994,-8.098365,-6.663400,5.199047,2.929701,9.624090,4.447698,-7.759013,5.906586,5.445956,4.539675,-8.501261,0.740119,4.611217,5.121165,-9.416470,3.628947,2.815067,-8.076734,2.048328,9.693057,9.022500,-7.812233,-5.027971,-1.602478,-0.208560,-0.174330,-4.651296,5.069343,-1.478217,1.311742,0.016390,-9.012883,-2.586363,5.571574,-2.439285,-8.440204,0.112145,6.871555,6.700515,-2.929390,-1.344719,-0.527448,-6.187922,-5.716375,-5.162862,1.983407,3.129382,-0.403313,-3.350191,8.693215,-4.576896,-0.933185,-1.366371,2.060816,4.988097,-9.343117,5.277985,-5.554277,-4.733082,-1.495961,-7.715486,-8.125915,2.833038,8.479929,2.114080,-5.119490,8.589445,5.939470,0.999601,3.984536,-6.525752,-1.562198,-1.416576,-6.024837,7.873120,1.771651,-1.001746,5.238893,-2.266204,-4.506717,-3.596672,0.560954,7.651542,8.933403,-5.838363,-1.341443,-2.906956,-3.458172,8.950892,9.427485,9.460453,2.107719,1.567999,-1.744120,9.286575,4.197226,5.088322,2.183432,5.623836,5.189692,5.469901,7.203666,-1.118505,-1.566563,-3.227293,6.861708,-8.644467,8.039772,2.756452,4.872215,-7.231478,-0.488318,-2.406978,3.679454,5.005720,7.891954,-7.271082,-7.054449,-8.416482,-9.220044,9.596542,-4.709316,-9.250566,5.096993,6.744634,9.989662,9.166392,-1.739784,2.941864,6.917647], dtype = "float32")#candidate|11519|(900,)|const|float32
var_11520 = relay.var("var_11520", dtype = "float64", shape = (3360,))#candidate|11520|(3360,)|var|float64
call_11518 = relay.TupleGetItem(func_5919_call(relay.reshape(const_11519.astype('float32'), [15, 4, 15]), relay.reshape(const_11519.astype('float32'), [15, 4, 15]), relay.reshape(var_11520.astype('float64'), [3360,]), ), 4)
call_11521 = relay.TupleGetItem(func_5923_call(relay.reshape(const_11519.astype('float32'), [15, 4, 15]), relay.reshape(const_11519.astype('float32'), [15, 4, 15]), relay.reshape(var_11520.astype('float64'), [3360,]), ), 4)
output = relay.Tuple([uop_11470,call_11484,bop_11493,uop_11499,call_11518,const_11519,var_11520,])
output2 = relay.Tuple([uop_11470,call_11485,bop_11493,uop_11499,call_11521,const_11519,var_11520,])
func_11524 = relay.Function([var_11469,var_11520,], output)
mod['func_11524'] = func_11524
mod = relay.transform.InferType()(mod)
var_11525 = relay.var("var_11525", dtype = "float32", shape = (15, 15, 6))#candidate|11525|(15, 15, 6)|var|float32
var_11526 = relay.var("var_11526", dtype = "float64", shape = (3360,))#candidate|11526|(3360,)|var|float64
output = func_11524(var_11525,var_11526,)
func_11527 = relay.Function([var_11525,var_11526,], output)
mutated_mod['func_11527'] = func_11527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10292_call = mod.get_global_var('func_10292')
func_10293_call = mutated_mod.get_global_var('func_10293')
call_11590 = relay.TupleGetItem(func_10292_call(), 0)
call_11591 = relay.TupleGetItem(func_10293_call(), 0)
output = relay.Tuple([call_11590,])
output2 = relay.Tuple([call_11591,])
func_11605 = relay.Function([], output)
mod['func_11605'] = func_11605
mod = relay.transform.InferType()(mod)
mutated_mod['func_11605'] = func_11605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11605_call = mutated_mod.get_global_var('func_11605')
call_11606 = func_11605_call()
output = call_11606
func_11607 = relay.Function([], output)
mutated_mod['func_11607'] = func_11607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6855_call = mod.get_global_var('func_6855')
func_6857_call = mutated_mod.get_global_var('func_6857')
call_11610 = func_6855_call()
call_11611 = func_6855_call()
output = call_11610
output2 = call_11611
func_11616 = relay.Function([], output)
mod['func_11616'] = func_11616
mod = relay.transform.InferType()(mod)
output = func_11616()
func_11617 = relay.Function([], output)
mutated_mod['func_11617'] = func_11617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7965_call = mod.get_global_var('func_7965')
func_7966_call = mutated_mod.get_global_var('func_7966')
call_11648 = func_7965_call()
call_11649 = func_7965_call()
output = relay.Tuple([call_11648,])
output2 = relay.Tuple([call_11649,])
func_11656 = relay.Function([], output)
mod['func_11656'] = func_11656
mod = relay.transform.InferType()(mod)
mutated_mod['func_11656'] = func_11656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11656_call = mutated_mod.get_global_var('func_11656')
call_11657 = func_11656_call()
output = call_11657
func_11658 = relay.Function([], output)
mutated_mod['func_11658'] = func_11658
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11699 = relay.const([[[7.810032,-4.962309,-5.604893,-6.616995,-7.763918,2.505486,-6.855392,-6.722014,-6.942605],[-3.942517,-3.701902,5.021158,7.707402,-4.523487,4.634647,2.149004,-2.202559,-3.256605],[2.309865,-0.021152,0.347766,7.119439,1.584479,4.684120,6.004801,-6.429530,6.411727],[1.399035,9.623584,2.856768,4.436863,5.968814,-6.373848,9.988891,-2.299781,9.129136],[9.983040,9.512108,-4.627694,2.571016,-8.823276,9.393728,5.952623,8.358831,3.682318],[7.139136,2.859615,-3.265985,-7.152497,7.970584,1.952346,-4.851368,7.305762,-9.555312],[4.412083,-8.885019,4.220146,1.556186,-3.233294,1.752117,1.848480,7.477830,1.393962],[8.979902,0.731089,-9.729706,1.038592,1.739387,7.118339,9.871775,4.074205,-4.409550],[5.736790,1.985329,-9.873187,5.813850,-8.716575,-0.501800,-1.771482,9.700027,5.007439],[3.469476,3.603235,3.999117,-9.591985,4.366598,-3.542342,-4.085993,5.968028,-5.605108],[-8.137065,2.510810,-8.633409,-6.192909,2.556443,-1.759073,5.580440,-9.702232,-2.825060],[9.114819,-6.642446,8.561894,4.640708,-3.481576,2.022584,-9.959452,2.877155,-6.190663]],[[-0.904049,-6.001305,2.827343,-5.117646,-4.169323,6.460155,-2.570138,2.465838,2.766873],[-6.966497,-3.042752,0.943426,5.016591,0.288786,5.601600,-1.321705,-1.783754,-7.722934],[2.989368,9.345196,8.801749,-4.436219,2.065385,-2.803135,-0.009966,2.442313,0.189603],[9.167381,3.606695,8.522334,-0.603018,-7.312824,2.371304,-3.349582,8.432430,-7.329544],[-2.546122,-9.295039,4.263101,-3.766456,2.112420,-8.541381,-8.298931,9.199315,4.083649],[9.148910,-9.928681,-3.684552,-2.277875,-3.996770,-9.966067,-9.382357,-4.783161,7.366375],[7.066823,2.378358,9.141389,5.481039,5.319673,3.196193,-3.868397,4.728422,-2.952820],[-0.419978,-8.169998,-6.827886,6.995467,-1.524542,-1.462089,1.034742,6.224375,-3.458001],[4.994281,7.924857,9.459894,8.813768,3.079675,-6.132828,-8.742970,-4.452226,-8.473423],[-1.543855,7.341397,1.302634,-7.775966,0.122904,4.078659,-6.428411,4.711018,-8.152131],[0.437136,-2.508218,-1.168336,-6.685098,9.644688,2.360788,-6.761324,-2.854645,-1.688014],[1.034954,-2.972304,3.447991,-2.770882,-3.682722,2.978813,-4.027646,-9.745530,3.458524]],[[-4.486787,-1.703606,-5.874457,3.426126,5.188926,-5.123230,2.996986,-1.302048,-9.334690],[5.544648,0.542031,-0.473201,-9.439397,8.104058,-9.740304,4.669798,8.647101,-7.538870],[-0.299249,-2.680376,3.080718,0.425980,-4.262455,2.425231,1.007052,0.489309,-8.567594],[8.813560,3.689097,-5.227433,4.926974,-8.195415,7.949893,-1.744125,-7.062479,0.099819],[9.533531,-7.469712,-7.748366,-4.537172,-4.102040,-4.226921,-7.324262,-1.636355,8.661742],[1.828135,-2.960201,5.761338,-2.030632,6.162860,-9.930953,6.710851,-8.778598,2.567649],[9.947886,-3.128045,3.046394,-0.795288,2.042512,4.170979,2.867297,2.297083,-0.560255],[5.608657,8.091220,5.085147,2.214888,9.541442,-8.208228,-3.078249,2.207956,-7.746768],[-7.317421,-7.763652,0.776735,-9.631848,-2.651390,-8.174869,-0.563889,6.420516,5.935221],[8.356061,9.772604,-9.648401,2.953033,0.369394,0.860477,2.836269,7.778290,3.463080],[-2.006228,9.939252,-5.445648,0.273893,-8.196720,-1.483221,-3.706260,-2.040102,-6.448571],[6.263903,-9.089043,-9.913042,-2.719260,4.744466,4.800959,-4.574578,-6.592595,-0.486982]]], dtype = "float64")#candidate|11699|(3, 12, 9)|const|float64
var_11700 = relay.var("var_11700", dtype = "float64", shape = (3, 12, 9))#candidate|11700|(3, 12, 9)|var|float64
bop_11701 = relay.floor_divide(const_11699.astype('float64'), relay.reshape(var_11700.astype('float64'), relay.shape_of(const_11699))) # shape=(3, 12, 9)
uop_11718 = relay.acosh(bop_11701.astype('float32')) # shape=(3, 12, 9)
const_11723 = relay.const([[[-1.960708,7.293481,2.403712,-5.671017,-2.200437,7.303854,-3.631479,2.573444,7.396665],[-9.663480,-3.600947,7.698650,6.884014,-2.170183,-1.097908,-5.892672,-4.801031,-7.490932],[-8.009909,4.777120,-6.639270,-3.449845,-7.543311,-6.957752,-3.563998,6.575439,-5.699929],[5.402963,1.298355,-9.957377,4.769986,-9.704095,-5.546865,7.897206,-9.032220,9.013198],[2.239521,6.118105,8.920787,-7.298948,-9.904039,-3.663991,-9.662339,-4.668037,1.282956],[5.365269,7.204648,-6.713354,-2.549317,-5.757084,7.203872,8.839688,-3.024895,-4.189110],[-2.007479,2.096937,-5.405832,-9.659673,2.465841,-1.766686,1.241556,1.826597,-3.530861],[-7.442712,8.780932,5.364084,-5.996091,-8.275716,5.113307,-7.086349,0.406021,5.538435],[8.155719,-6.426702,-9.382191,4.730214,-9.620039,5.862841,1.838453,9.284805,-5.860905],[1.755817,2.069887,3.253982,-6.405594,-5.225292,7.938184,8.688661,7.389582,4.702728],[2.238030,0.437675,9.247193,-2.743875,-6.374243,-6.652975,-5.949614,5.475197,6.154271],[-3.382720,-3.965037,2.727981,-9.989378,-3.346173,-9.877999,-7.649070,3.464143,9.887690]],[[-3.683686,4.250059,2.301112,4.335449,5.145997,3.043122,-6.323911,-8.584136,-8.558555],[-2.698175,-3.590113,2.438909,3.698878,-0.057435,9.984944,3.400642,0.204874,4.771872],[-1.928571,-5.578646,4.536083,-3.518027,-4.112973,4.642628,-7.702521,2.784279,-9.959557],[6.345857,-3.329012,-3.286912,8.716605,9.910866,-1.332746,9.426782,-3.478545,-2.258394],[6.696282,1.173878,4.965289,2.121148,-6.739086,2.385897,7.035348,-5.782175,-7.727904],[0.084193,8.292983,3.495291,9.811202,-3.447658,-4.372028,-1.738830,-2.273214,0.830870],[-1.160006,4.272454,-5.162931,2.567287,-8.311755,3.515954,8.918552,-9.278806,-3.769071],[-3.722877,6.221293,5.100692,-3.359779,4.187698,8.934492,-3.634490,5.934167,-0.940116],[-4.820659,6.002985,-5.758633,-4.834770,-9.376996,-1.378110,-7.882150,-8.221504,6.587279],[2.567356,0.734687,-6.216226,-7.305768,-5.881308,9.343488,0.464780,3.783779,-7.732637],[5.179664,6.672815,1.964699,-8.631618,-4.972836,7.075679,-3.323769,5.591368,-0.356730],[-6.554862,2.836445,-6.067892,-9.185456,-8.684425,7.708169,6.784383,5.176524,-5.777225]],[[-4.944484,-7.205675,0.742639,-4.890270,5.834958,-3.550605,-1.137607,-0.663883,3.349551],[-9.429393,-2.629987,8.052643,5.593174,-3.861252,7.241846,3.428095,-1.313153,1.314476],[-4.728642,1.717313,1.043489,4.778445,1.950899,4.358111,-3.356495,-3.217528,8.256570],[-7.016706,-7.883159,4.088304,7.555843,8.899113,6.049011,-7.624095,-3.109208,9.016087],[4.398693,2.139760,-7.253548,3.788680,-8.225463,5.867582,-3.888983,-5.362951,-9.170303],[-5.804726,2.012624,2.085120,-1.673246,-4.544791,-1.968276,6.557570,-0.581036,-3.302497],[2.939159,4.705548,2.452187,1.222387,6.136556,-5.066488,-2.632318,4.318254,-2.252460],[-7.351849,-8.927099,3.125398,-2.224377,-7.882135,-7.477399,9.849057,0.447067,5.450877],[5.963968,-1.478419,7.418149,-7.645207,0.066213,4.636501,7.488034,6.974352,-9.214757],[-8.004442,5.182652,9.303998,7.240523,3.818111,0.912583,5.511985,-3.446350,3.449002],[-2.680521,9.381759,-3.625090,8.722504,-3.061052,2.803939,5.894931,6.188309,0.226993],[-5.037671,6.121058,4.055243,0.757271,6.764243,-3.003176,0.540078,-2.353541,-1.924286]]], dtype = "float64")#candidate|11723|(3, 12, 9)|const|float64
bop_11724 = relay.maximum(const_11699.astype('int16'), relay.reshape(const_11723.astype('int16'), relay.shape_of(const_11699))) # shape=(3, 12, 9)
const_11744 = relay.const([[[-9.803517,7.888697,3.047914,6.969698,-2.560463,-1.101132,1.463462,7.861125,2.954961],[-4.844727,-7.631200,-1.630602,-6.669969,5.026793,5.429767,-1.018000,-5.832567,-1.253519],[-4.888749,-4.258721,-2.989226,-0.697409,6.402480,-9.799008,4.791238,-0.554652,-2.439437],[-9.938017,7.459526,-2.863853,-0.121279,-1.151078,-3.838912,5.982739,-1.907198,-0.165213],[-3.778749,-7.091163,-8.442996,5.915575,-7.810213,1.554550,-3.142306,1.634363,-9.097124],[-0.453227,-5.118971,0.789816,1.224228,-8.837381,-9.268435,1.939165,7.442753,1.688126],[-3.512138,4.138516,-3.282741,8.259404,8.270514,-1.383605,-6.449245,-9.266240,-5.113364],[-3.237783,-2.407469,2.461083,1.072095,-2.359043,3.647243,-4.585196,-9.263552,-5.284717],[-7.017165,9.004480,-3.428125,3.634169,-8.998130,-7.703889,-2.157023,5.134962,4.154019],[9.141039,9.263884,1.220652,7.915679,-4.080910,8.119616,7.120584,-2.993142,2.404265],[-5.577914,-1.271321,7.975878,9.118024,2.004177,-2.564164,-7.756882,0.653914,6.715119],[-5.177854,-0.743859,-0.445429,5.049708,8.803237,-6.691369,-1.322198,-5.255292,-9.573416]],[[0.626523,9.735241,-1.387866,0.392355,7.150867,-6.176437,6.724131,-0.334354,1.516483],[-9.971398,-9.774220,-7.762001,-4.167063,6.897344,8.977299,-5.024135,-4.106229,7.431654],[-5.139928,7.447185,8.561906,-5.669501,-5.189654,-2.215096,-0.776482,-2.305247,1.257002],[8.958253,0.735098,-3.064058,-9.491798,-5.913052,-8.929413,0.298040,-1.974407,-5.636984],[-3.532367,5.018865,8.166882,-9.195602,-4.844162,-6.796721,-8.715992,0.493332,8.573690],[-7.006837,4.631119,-7.487568,2.763606,-7.436377,-5.759639,8.806471,6.450153,0.930381],[6.700899,-7.750639,-6.869066,8.414244,5.264462,-2.522357,-0.738499,-6.590454,0.606481],[4.612136,9.754393,0.494812,-2.079323,-3.182521,4.949561,5.092744,-1.792578,-7.111714],[-2.581908,1.254259,-6.973277,-0.204503,-7.630081,-5.555483,9.541036,-6.895210,0.689085],[-9.327222,3.950598,-5.930020,-4.938264,9.350370,8.693625,5.175937,2.815662,6.676379],[0.659398,-8.386161,6.071425,2.744420,-6.233522,4.971568,1.306122,4.376022,-8.709520],[1.067939,3.845813,2.871385,-7.520919,5.346122,9.735324,-6.781138,-4.020004,7.275796]],[[1.135831,7.317772,-7.674002,-2.040991,-7.272106,-7.543937,1.921819,-0.902851,-3.537501],[5.691133,-5.820102,-0.892642,-0.678936,-8.613321,4.056824,-7.912706,0.627486,-8.921025],[-3.480564,7.431830,9.466037,6.206632,-6.656188,5.045582,-8.450855,4.511523,4.765988],[-7.389728,-3.696149,1.832809,-3.761528,5.891813,7.066367,-0.783661,-8.409913,-3.568749],[0.704042,-4.470886,4.202360,2.529450,-6.638494,6.236699,-3.643373,3.631282,-5.326679],[0.119817,-4.457509,-6.376819,-3.351271,3.091717,7.274119,-1.268635,-3.618687,-1.978079],[0.675672,4.158295,-7.745230,3.574822,-3.811299,-3.182971,3.908334,-2.773028,-8.647157],[8.720826,5.502847,1.206439,3.900039,9.558242,-6.591713,8.081103,6.641598,6.865265],[0.018684,5.306587,-9.623626,7.546294,9.529361,2.495861,-6.354555,-2.923520,-4.717169],[-7.258671,-2.629440,1.305935,4.625073,-5.785500,0.433263,6.355323,-5.347029,-5.741527],[-2.005071,4.168288,4.279302,8.163538,1.497450,2.163114,1.117194,1.009533,-3.555227],[-1.075361,-3.392935,-5.918770,-0.799179,-9.524186,-8.737640,1.298899,-6.199617,-5.388953]]], dtype = "float32")#candidate|11744|(3, 12, 9)|const|float32
bop_11745 = relay.not_equal(uop_11718.astype('bool'), relay.reshape(const_11744.astype('bool'), relay.shape_of(uop_11718))) # shape=(3, 12, 9)
output = relay.Tuple([bop_11724,bop_11745,])
output2 = relay.Tuple([bop_11724,bop_11745,])
func_11749 = relay.Function([var_11700,], output)
mod['func_11749'] = func_11749
mod = relay.transform.InferType()(mod)
mutated_mod['func_11749'] = func_11749
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11750 = relay.var("var_11750", dtype = "float64", shape = (3, 12, 9))#candidate|11750|(3, 12, 9)|var|float64
func_11749_call = mutated_mod.get_global_var('func_11749')
call_11751 = func_11749_call(var_11750)
output = call_11751
func_11752 = relay.Function([var_11750], output)
mutated_mod['func_11752'] = func_11752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10496_call = mod.get_global_var('func_10496')
func_10498_call = mutated_mod.get_global_var('func_10498')
call_11762 = func_10496_call()
call_11763 = func_10496_call()
output = relay.Tuple([call_11762,])
output2 = relay.Tuple([call_11763,])
func_11809 = relay.Function([], output)
mod['func_11809'] = func_11809
mod = relay.transform.InferType()(mod)
mutated_mod['func_11809'] = func_11809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11809_call = mutated_mod.get_global_var('func_11809')
call_11810 = func_11809_call()
output = call_11810
func_11811 = relay.Function([], output)
mutated_mod['func_11811'] = func_11811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11413_call = mod.get_global_var('func_11413')
func_11415_call = mutated_mod.get_global_var('func_11415')
call_11837 = relay.TupleGetItem(func_11413_call(), 0)
call_11838 = relay.TupleGetItem(func_11415_call(), 0)
output = call_11837
output2 = call_11838
func_11869 = relay.Function([], output)
mod['func_11869'] = func_11869
mod = relay.transform.InferType()(mod)
mutated_mod['func_11869'] = func_11869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11869_call = mutated_mod.get_global_var('func_11869')
call_11870 = func_11869_call()
output = call_11870
func_11871 = relay.Function([], output)
mutated_mod['func_11871'] = func_11871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7007_call = mod.get_global_var('func_7007')
func_7009_call = mutated_mod.get_global_var('func_7009')
call_11878 = func_7007_call()
call_11879 = func_7007_call()
func_10480_call = mod.get_global_var('func_10480')
func_10484_call = mutated_mod.get_global_var('func_10484')
var_11893 = relay.var("var_11893", dtype = "float64", shape = (2, 8))#candidate|11893|(2, 8)|var|float64
call_11892 = func_10480_call(relay.reshape(var_11893.astype('float64'), [8, 2, 1]), relay.reshape(var_11893.astype('float64'), [8, 2, 1]), )
call_11894 = func_10480_call(relay.reshape(var_11893.astype('float64'), [8, 2, 1]), relay.reshape(var_11893.astype('float64'), [8, 2, 1]), )
func_10874_call = mod.get_global_var('func_10874')
func_10877_call = mutated_mod.get_global_var('func_10877')
var_11906 = relay.var("var_11906", dtype = "float64", shape = (390,))#candidate|11906|(390,)|var|float64
call_11905 = relay.TupleGetItem(func_10874_call(relay.reshape(var_11906.astype('float64'), [15, 2, 13])), 1)
call_11907 = relay.TupleGetItem(func_10877_call(relay.reshape(var_11906.astype('float64'), [15, 2, 13])), 1)
output = relay.Tuple([call_11878,call_11892,var_11893,call_11905,var_11906,])
output2 = relay.Tuple([call_11879,call_11894,var_11893,call_11907,var_11906,])
func_11914 = relay.Function([var_11893,var_11906,], output)
mod['func_11914'] = func_11914
mod = relay.transform.InferType()(mod)
mutated_mod['func_11914'] = func_11914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11914_call = mutated_mod.get_global_var('func_11914')
var_11916 = relay.var("var_11916", dtype = "float64", shape = (2, 8))#candidate|11916|(2, 8)|var|float64
var_11917 = relay.var("var_11917", dtype = "float64", shape = (390,))#candidate|11917|(390,)|var|float64
call_11915 = func_11914_call(var_11916,var_11917,)
output = call_11915
func_11918 = relay.Function([var_11916,var_11917,], output)
mutated_mod['func_11918'] = func_11918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11869_call = mod.get_global_var('func_11869')
func_11871_call = mutated_mod.get_global_var('func_11871')
call_11961 = func_11869_call()
call_11962 = func_11869_call()
func_8994_call = mod.get_global_var('func_8994')
func_8996_call = mutated_mod.get_global_var('func_8996')
const_11975 = relay.const([-1,-10,-1,1,2,-8,4,-5,7,-2,-6,-5,4,-5,5,6,6,-10,-9,-9,-9,-2,-8,9,-9,-2,9,7,-7,4,10,-8,5,3,3,7,-8,-4,-3,2,6,-6,3,-10,8,2,3,-4,10,-4,-9,4,1,-4,2,8,-1,-5,-10,5,-9,7,9,-4,-1,1,-1,-9,-4,7,-10,8,-9,-6,-7,8,9,10,7,8,-2,7,-5,-4,-1,9,-5,-5,-7,3,3,2,5,4,5,9,1,1,-4,7,7,9,2,-6,4,-4,1,2,7,-9,6,-2,-7,4,-1,9,8,1,1,-8,-9,1,-8,7,9,-8,5,3,-6,-3,10,4,-9,8,2,-4,-6,-2,-8,-10,6,-3,1,-3,2,1,-8,-10,1,7,-1,4,-6,4,5,2,-3,2,-10,10,-3,-4,7,9,1], dtype = "uint8")#candidate|11975|(165,)|const|uint8
call_11974 = relay.TupleGetItem(func_8994_call(relay.reshape(const_11975.astype('uint8'), [165,])), 4)
call_11976 = relay.TupleGetItem(func_8996_call(relay.reshape(const_11975.astype('uint8'), [165,])), 4)
func_10292_call = mod.get_global_var('func_10292')
func_10293_call = mutated_mod.get_global_var('func_10293')
call_11977 = relay.TupleGetItem(func_10292_call(), 0)
call_11978 = relay.TupleGetItem(func_10293_call(), 0)
output = relay.Tuple([call_11961,call_11974,const_11975,call_11977,])
output2 = relay.Tuple([call_11962,call_11976,const_11975,call_11978,])
func_11989 = relay.Function([], output)
mod['func_11989'] = func_11989
mod = relay.transform.InferType()(mod)
mutated_mod['func_11989'] = func_11989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11989_call = mutated_mod.get_global_var('func_11989')
call_11990 = func_11989_call()
output = call_11990
func_11991 = relay.Function([], output)
mutated_mod['func_11991'] = func_11991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11438_call = mod.get_global_var('func_11438')
func_11439_call = mutated_mod.get_global_var('func_11439')
call_12069 = relay.TupleGetItem(func_11438_call(), 1)
call_12070 = relay.TupleGetItem(func_11439_call(), 1)
uop_12077 = relay.asin(call_12069.astype('float64')) # shape=(15, 2, 13)
uop_12079 = relay.asin(call_12070.astype('float64')) # shape=(15, 2, 13)
output = relay.Tuple([uop_12077,])
output2 = relay.Tuple([uop_12079,])
func_12089 = relay.Function([], output)
mod['func_12089'] = func_12089
mod = relay.transform.InferType()(mod)
mutated_mod['func_12089'] = func_12089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12089_call = mutated_mod.get_global_var('func_12089')
call_12090 = func_12089_call()
output = call_12090
func_12091 = relay.Function([], output)
mutated_mod['func_12091'] = func_12091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9236_call = mod.get_global_var('func_9236')
func_9237_call = mutated_mod.get_global_var('func_9237')
call_12099 = func_9236_call()
call_12100 = func_9236_call()
func_11605_call = mod.get_global_var('func_11605')
func_11607_call = mutated_mod.get_global_var('func_11607')
call_12106 = relay.TupleGetItem(func_11605_call(), 0)
call_12107 = relay.TupleGetItem(func_11607_call(), 0)
output = relay.Tuple([call_12099,call_12106,])
output2 = relay.Tuple([call_12100,call_12107,])
func_12129 = relay.Function([], output)
mod['func_12129'] = func_12129
mod = relay.transform.InferType()(mod)
mutated_mod['func_12129'] = func_12129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12129_call = mutated_mod.get_global_var('func_12129')
call_12130 = func_12129_call()
output = call_12130
func_12131 = relay.Function([], output)
mutated_mod['func_12131'] = func_12131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10957_call = mod.get_global_var('func_10957')
func_10959_call = mutated_mod.get_global_var('func_10959')
call_12199 = relay.TupleGetItem(func_10957_call(), 0)
call_12200 = relay.TupleGetItem(func_10959_call(), 0)
func_6903_call = mod.get_global_var('func_6903')
func_6907_call = mutated_mod.get_global_var('func_6907')
const_12209 = relay.const([1,9,4,-6,9,-7,-4,-5,3,6,6,2,-8,-4,8,-10,1,1,-7,10,-4,-3,9,1,-1,-3,-9,-3,-6,6,4,5,7,3,-2,-10,-1,7,10,4,-5,6,-10,10,6,1,4,-7,1,5,-2,-2,-9,-3,-8,-8,-1,-8,-5,-8,8,3,9,-3,8,6,4,-3,8,1,10,-3,-6,-4,1,2,-5,-1,4,3,-3,-2,-8,1,-10,3,2,10,7,8,8,-9,-6,-7,6,2,10,8,10,3,-2,9,2,-3,-5,-1,5,-6,-2,-1,3,-10,1,1,9,-1,-10,-6,-10,-3,4,-8,4,9,-8,-4], dtype = "uint32")#candidate|12209|(126,)|const|uint32
var_12210 = relay.var("var_12210", dtype = "uint32", shape = (1008,))#candidate|12210|(1008,)|var|uint32
call_12208 = relay.TupleGetItem(func_6903_call(relay.reshape(const_12209.astype('uint32'), [126,]), relay.reshape(var_12210.astype('uint32'), [1008,]), ), 2)
call_12211 = relay.TupleGetItem(func_6907_call(relay.reshape(const_12209.astype('uint32'), [126,]), relay.reshape(var_12210.astype('uint32'), [1008,]), ), 2)
func_11413_call = mod.get_global_var('func_11413')
func_11415_call = mutated_mod.get_global_var('func_11415')
call_12212 = relay.TupleGetItem(func_11413_call(), 0)
call_12213 = relay.TupleGetItem(func_11415_call(), 0)
output = relay.Tuple([call_12199,call_12208,const_12209,var_12210,call_12212,])
output2 = relay.Tuple([call_12200,call_12211,const_12209,var_12210,call_12213,])
func_12231 = relay.Function([var_12210,], output)
mod['func_12231'] = func_12231
mod = relay.transform.InferType()(mod)
var_12232 = relay.var("var_12232", dtype = "uint32", shape = (1008,))#candidate|12232|(1008,)|var|uint32
output = func_12231(var_12232)
func_12233 = relay.Function([var_12232], output)
mutated_mod['func_12233'] = func_12233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9836_call = mod.get_global_var('func_9836')
func_9838_call = mutated_mod.get_global_var('func_9838')
call_12245 = relay.TupleGetItem(func_9836_call(), 0)
call_12246 = relay.TupleGetItem(func_9838_call(), 0)
func_2897_call = mod.get_global_var('func_2897')
func_2900_call = mutated_mod.get_global_var('func_2900')
var_12253 = relay.var("var_12253", dtype = "float64", shape = (150, 1))#candidate|12253|(150, 1)|var|float64
var_12254 = relay.var("var_12254", dtype = "float64", shape = (750, 2))#candidate|12254|(750, 2)|var|float64
call_12252 = relay.TupleGetItem(func_2897_call(relay.reshape(var_12253.astype('float64'), [10, 15, 1]), relay.reshape(var_12254.astype('float64'), [10, 15, 10]), ), 0)
call_12255 = relay.TupleGetItem(func_2900_call(relay.reshape(var_12253.astype('float64'), [10, 15, 1]), relay.reshape(var_12254.astype('float64'), [10, 15, 10]), ), 0)
func_3212_call = mod.get_global_var('func_3212')
func_3215_call = mutated_mod.get_global_var('func_3215')
const_12271 = relay.const([0.983613,-2.023003,7.604715,-2.695141,-2.438781,4.761304,3.840715,1.465189,-9.181556,9.788993,6.265636,-4.021422,0.830756,0.646002,1.300108,3.764317,2.788769,-0.295631,-7.407031,1.571910,4.620758,-2.795382,6.726210,-5.711103,-7.189575,-4.267892,-0.218421,0.420119,-6.499651,-5.797044,8.118714,-9.793818,3.763863,7.154082,7.420065,-9.997206,-3.655301,0.243435,-1.696725,7.604546,9.439872,4.878048,-1.755209,-3.927728,8.581427,-1.862016,-3.204319,4.884392,3.735764,8.791491,-5.860103,7.706749,4.180415,-1.934645,-8.362356,-5.562101,5.536013,8.006296,-6.322573,-1.808141,-2.091218,-8.992482,-2.738933,-9.946732,-2.947990,-2.916576,-2.407549,0.155618,4.838977,9.447433,0.173251,6.547382,6.625337,1.565758,-4.261838,8.428244,-9.229098,3.746110,-5.055194,5.108284,-5.526326,0.581400,9.361236,-4.097328,-2.802177,1.567521,0.975214,-8.513919,1.032039,-0.495963,-2.194817,0.046079,3.096439,1.716380,-0.477800,-2.598639,-1.224118,6.429604,6.860975,-6.649171,-1.791344,6.981794,5.535923,-0.055918,3.378152,-9.871734,8.216522,1.253592,6.217743,-2.958478,2.525995,-4.605199,-3.809245,8.057686,7.585714,6.476209,9.403776,5.971532,-7.129504,-4.603784,-4.126425,7.033164,-2.094811,-1.571597,4.956241,7.810917,6.688749,2.069765,-5.671725,7.926374,-3.592669,3.597155,-0.220207,-6.003558,-3.108318,-5.427634,-8.933401,-5.105093,-8.617565,-3.205954,0.797874,-9.321654,1.036805,-1.404679,6.675283,3.217886,-0.613328,8.553750,6.937506,-3.681988,-0.148195,-7.319940,-1.020413,4.792553,0.038927,9.826244,-1.216906,5.086666,7.683874,6.206427,-1.527601,-4.989514,0.559628,7.760660,-4.700009,-9.610981,-2.220303,2.195860,-7.712188,-8.216896,-0.942931,-9.966511,8.790152,-1.833999,-7.629895,2.256379,-3.273873,9.854833,-4.229894,-4.811505,-7.505099,6.690235,5.449032,-3.080471,-3.977177,4.829673,-1.237178,8.195977,1.658233,-6.948891,0.540218,-5.713681,2.964232,8.326278,-7.356385,-1.181618,-2.460593,-0.070589,-3.061639,6.579662,9.673896,6.422181,9.591460,4.079326,-6.368537,-9.597259,-7.318804,5.733867,-5.889553,6.494174,-8.169939,-8.402351,4.416225,-6.048280,5.876984,-5.268633,-7.646233,-9.428867,-6.220449,3.200342,1.492173,-5.735135,-3.920207,2.648882,-9.792397,-8.833556,9.135063,-7.151768,2.073748,-2.504780,-6.425356,4.508049,4.632388,-1.971364,1.594650,-0.474565,9.457582,-8.980994,9.528304,8.432913,-8.728780,-5.146513,-9.591787,5.086406,-6.039472,-4.855570,-4.822730,9.266596,2.413263,-2.614389,7.832120,0.501037,5.617564,6.483952,6.273434,5.298457,-2.606735,7.399294,-6.870277,-9.839778,0.283713,3.158538,-4.428625,3.238071,5.207987,-4.719429,-3.824971,4.870327,-4.585716,-7.263154,3.993179,1.845076,-1.898675,-5.483243,1.145298,9.887707,9.543226,8.922750,5.249629,1.411778,-8.698722,-4.299043,0.069551,-0.827653,-9.071536,-1.094148,-0.936813,7.645638,-3.388257,5.022869,-9.101442,-4.093100,-8.864464,9.413343,-9.315078,-3.896367,-7.117751,-2.563320,-4.566900,1.975047,3.803327,6.600760,-4.298365,-5.295815,-3.561621,-9.843692,-3.341809,8.490872,-3.299587,3.772491,9.182271,7.203921,-4.162698,-2.221825,6.523427,3.980285,4.834237,-1.636132,0.815544,-6.441198,2.961588,-4.677645,-5.239537,-2.176138,-7.381098,8.750420,6.085591,3.558463,-6.749059,-4.421175,-6.115768,6.432472,-1.196980,0.644210,-1.766616,-6.172117,-6.624662,-4.570905,-8.220364,-0.360045,-6.062329,-1.135891,-5.328831,2.396965,3.143222,-3.895007,4.968851,3.094795,-9.740329,7.729218,8.465868,-7.611652,-7.914415,-8.574020,3.965559,6.322495,-9.442859,8.332666,2.203515,-9.839144,-4.914243,-0.633418,-9.211356,-4.051577,-2.284402,7.989062,0.935809,-5.105403,-2.834733,-6.162171,1.478140,5.916207,2.696730,-7.126681,8.015834,-8.422877,-5.065943,2.057189,-3.958474,6.718564,5.561993,-1.877701,-7.535663,-9.850098,3.573581,-5.886859,-2.489597,9.133266,-4.907884,4.220005,-6.333454,9.082750,-1.908320,7.529394,-6.364087,-2.254256,1.789219,-7.672584,4.799981,1.239545,7.804592,5.005373,8.495935,-2.302033,-5.206661,-2.438810,2.785227,6.394060,-0.065623,-8.176026,9.784447,1.208743,-2.124345,-9.414005,-4.159812,-3.139012,4.503949,-3.673104,-2.786291,-0.543115,-6.529166,2.062011,0.417614,6.686276,6.654499,-1.015497,-6.188092,-2.995150,-3.028840,-6.174668,-8.564780,-5.809259,-9.636568,-6.117690,7.347136,-6.949660,0.366877,9.754936,-0.425832,4.336150,4.128596,6.053375,3.173447,-7.441583,-0.392126,-6.221692,0.048162,4.077577,0.674268,6.707931,-8.743845,-6.863853,8.160413,-6.806675,8.291290,-0.452149,-0.423407,-6.323257,9.744834,4.005270,-6.233628,-6.458375,-8.762360,6.460052,5.212648,8.648654,-3.267495,-8.058915,5.866788,-7.315727,-1.769026,7.047602,-8.786207,-1.646626,-0.524412,5.120648,9.621880,7.097888,4.811442,-4.511797,5.906149,4.947627,4.663249,4.446232,-7.556638,8.627349,-9.631165,8.911067,6.958843,-2.995892,1.865664,-9.752627,5.043281,5.514005,-9.227067,-4.248724,8.754689,-6.641749,6.505003,8.170389,6.202649,-1.790256,-3.231486,-8.859378,7.618510,0.205679,-0.720608,7.306108,2.559387,0.220835,-6.996056,6.134882,8.869113,6.192751,-3.019503,-7.621612,3.599127,8.220444,5.134180,7.611981,3.635864,4.297277,-5.481852,0.009884,4.623899,-0.134151,-3.477513,0.956428,1.561663,-9.629829,-6.995000,7.779385,8.718101,6.839525,-8.905791,0.109810,8.907641,5.815510,-2.592903,-4.430042,1.783980,5.290190,-8.391499,2.725809,0.229374,1.808900,6.096309,-6.089755,-1.128061,0.401517,-6.828181,-2.067416,2.994325,-6.192026,-9.052161,-5.879817,9.228115,-7.840217,-5.089848,3.555231,4.033188,0.272431,4.793132,-3.173433,9.999601,-5.467076,-0.762334,-4.432777,-0.175047,1.424680,5.998079,7.339380,-4.536151,-2.915866,5.313000,-8.828304,8.239527,6.971881,3.146178,-6.269047,5.843217,4.119823,1.369600,-7.977806,-8.520815,-1.070923,4.898046,-9.775644,0.693084,-7.196823,-3.536031,-0.652538,9.472068,-8.944715,1.662265,5.392029,0.189795,-0.430884,-2.555700,-8.066807,5.052791,-7.242768,-2.228695,-1.250811,-4.154523,9.381463,5.921156,-1.135475,9.160352,-4.908217,5.327633,-3.244694,-7.873196,9.581779,0.067014,3.053460,-2.835615,8.485631,-0.381075,9.910906,-0.287934,3.106363,-0.023959,-8.226042,-3.271098,-8.113470,6.609148,-6.583558,6.348319,-2.778284,6.638687,9.081394,-0.489248,9.085448,-1.363279,7.610468,5.063922,8.665616,-0.146687,0.900840,-6.845249,-4.399549,-5.620464,3.427106,-5.098896,-5.573265,0.786228,1.900003,-0.898266,-2.479273,3.065988,-7.933011,-2.890170,-6.557557,8.405106,1.768439,4.146589,9.736179,-0.517595,-5.184258,4.343495,-6.027872,-9.294607,-7.414785,-8.418903,-4.871571,-0.380893,-1.944846,-8.261808,6.730871,0.464372,4.107985,-8.943781,-4.857659,4.274890,7.631878,-5.927929,0.259919,0.116235,6.511070,-1.239996,-5.130698,-1.795370,1.987327,5.752918,0.122142,3.067744,-7.418861,2.915168,-7.513675,1.068109,6.123701,6.225978,-7.614103,-3.135565,7.066238,2.353050,6.171076,-9.480469,-3.611997,1.121497,-4.540047,-9.524564,-0.452348,-7.537203,-9.738523,-6.322671,1.095690,-2.619029,4.929557,3.340328,7.172211,-3.718620,4.260775,3.528068,-9.135934,5.760612,1.284583,1.864728,6.181257,-7.265681,9.551209,-9.962267,3.955944,5.394606,3.472768,7.466622,5.981938,-1.744513,-2.044801,4.230003,-5.680893,-3.277459,-7.463661,-0.147999,8.196134,-4.435325,8.198054,4.690416,7.234930,3.390100,7.894903,-0.236431,-6.532848,5.594088,-9.915065,-2.308852,4.410135,1.232174,-5.245485,-7.828968,-1.196922,5.188598,4.009941,-1.762440,5.270193,6.719548,-8.682432,2.836285,-4.160606,-7.169843,2.161702,-8.325817,1.864645,8.025027,0.045995,3.722867,-6.618369,3.687638,5.303786,-9.060753,-8.694213,0.886550,3.195057,9.261506,-1.987015,2.553692,-3.804320,-1.497937,2.876709,-5.839297,3.597240,-5.403117,-4.290634,9.119929,-9.776966,-4.129423,-8.079496,4.044742,-5.212711,1.432528,-2.935471,5.648965,-3.183138,-5.385323,9.522451,-1.018834,-9.414160,-4.422947,6.804512], dtype = "float64")#candidate|12271|(800,)|const|float64
call_12270 = relay.TupleGetItem(func_3212_call(relay.reshape(const_12271.astype('float64'), [10, 16, 5])), 0)
call_12272 = relay.TupleGetItem(func_3215_call(relay.reshape(const_12271.astype('float64'), [10, 16, 5])), 0)
uop_12278 = relay.atan(const_12271.astype('float32')) # shape=(800,)
func_8605_call = mod.get_global_var('func_8605')
func_8607_call = mutated_mod.get_global_var('func_8607')
const_12334 = relay.const([6.063253,-7.139739,-4.164614,-2.086704,-6.043454,-3.864117,-3.715903,7.499798,3.662726,6.268765,-6.374857,2.669064,8.875548,2.081001,-2.049346,4.351722,-8.335311,-0.572577,9.506795,-5.191688,-6.606530,6.095402,-2.026284,9.393976,7.021162,-2.531234,-2.331190,3.089761,8.275109,-8.206621,5.100053,2.849556,4.231423,-2.516551,-3.902317,-3.263669,-6.523553,3.942088,0.224067,-0.127945,-3.857083,-1.752366,-4.672486,-4.727899,-3.814026,7.794534,2.677137,8.597119,1.424778,3.964418,-8.837626,-3.125209,2.980002,-0.603216,-0.526651,8.890462,6.350956,-7.426111,1.843616,2.128039,9.253318,-4.479644,-3.175044,-5.964238,6.661448,5.575734,4.286968,-9.996324,-6.751517,3.846182,4.600638,3.938443,-3.782739,2.699081,-3.669908,6.683588,2.341321,-8.246172,0.409388,1.138203,7.768637,4.759866,-6.263000,2.675331,-4.039335,-1.366176,-6.722111,-2.090798,7.760750,-5.000592,-2.147680,1.669324,7.680639,6.934429,-6.452856,-1.306923,-9.167978,2.686617,6.118298,5.127585,2.689549,-6.156823,7.661230,2.541586,-6.214552,-4.790346,0.586172,-1.044079,-1.903592,-4.393429,4.765593,-7.698369,-7.092500,-7.653123,-5.565760,2.345587,1.396604,6.714961,-1.209855,8.311017,4.291696,3.171395,-0.322899,6.190829,-0.580967,9.315465,-0.490151,1.902853,5.234828,1.566610,3.182617,-8.808911,-3.572349,6.539092,-6.705056,5.421545,-3.271157,-6.327454,-4.172715,6.308836,3.408393,-7.430111,-2.742143,-2.056778,-6.405400,-4.297443,-4.067800,-7.911680,-6.752098,8.192906,7.124567,-1.175644,-9.161772,-5.387568,7.206285,0.928192,-1.188498,-8.631539,3.134639,9.824240,-8.796279,5.274051,-0.134497,2.356786,2.339405,5.001507,0.987914,-2.234340,-8.546064,5.950163,0.211460,9.736830,-6.785373,-8.867277,-6.813818,0.663495,4.666360,-8.422198,1.164261,9.153647,-0.761854,4.905564,-1.836703,2.775357,-4.739874,-8.908810,5.505261,1.632081,-7.494949,4.757797,1.336639,5.851282,0.997506,-2.795524,-3.820524,4.069476,-6.769975,-7.596320,5.039270,-3.713462,-1.349244,3.239723,-2.293764,-3.102749,-4.561128,2.529142,-0.753513,7.286877,-6.145545,-8.123837,6.351570,-4.244665,-8.971740,-6.099531,-0.303895,8.616425,-3.068928,5.745202,-9.104165,5.808662,7.630964,-9.386355,0.747600,-0.201287,-3.949398,-0.284067,-1.891589,1.676664,-6.735545,-7.984191,-1.943727,8.938371,-4.408371,3.936897,-9.054763,-2.584588,-7.308155,-3.603122,-8.262542,6.230214,4.894577,-2.718801,-3.442086,4.834940,4.145199,-2.461790,5.800276,-1.526715,-9.157867,-1.741053,-0.985927,-7.167475,-0.261266,8.944648,6.104288,1.367335,-0.842794,4.198497,6.996812,3.549298,-3.952866,7.968191,-1.238996,-9.101978,8.856638,8.658808,8.791522,-4.919658,-9.251962,-0.475275,8.166268,8.689014,8.116691,-5.469860,9.508187,8.640448,7.956639,2.820347,9.768166,-6.629629,3.331690,-5.899702,-3.620346,-3.010690,-0.889482,-6.335978,-6.062585,-7.408050,-9.373059,-8.537523,-8.696578,-5.403321,-7.332256,7.837817,4.274878,5.366224,-4.913796,4.675352,-3.293914,2.362959,-3.840786,-8.079424,0.323227,-7.545706,-9.052128,0.523074,-1.157088,-2.973297,-7.400506,-0.301975,-8.965182,-6.843410,-7.891012,7.580619,1.265711,9.193996,-6.874371,-4.060449,-9.322022,-6.902961,6.110469,-1.603711,8.719617,8.970407,-8.064480,5.696937,5.833017,0.385104,7.337465,-0.193144,-7.814402,-0.716169,-7.104014,-6.027704,6.860680,2.896086,4.840097,-0.640660,-7.213127,-4.619024,-6.313984,1.814419,7.643787,0.827332,6.773856,0.715611,9.012796,5.296028,-8.395382,4.389328,-4.217583,-9.154518,-2.269833,-1.752110,-0.473913,0.614275,-8.803262,-2.351746,-6.725953,-6.638084,-9.933086,0.765935,2.689112,1.121837,-8.995495,9.095202,7.190329,-4.401594,-0.020444,-5.141799,2.196274,7.052634,0.136005,6.082600,9.011931,5.582976,9.337322,-2.685573,9.379262,-7.919130,-4.356160,-7.646527,-3.217565,0.959113,2.049534,6.846079,1.035480,-9.431669,6.744449,-1.770394,8.117645,-8.348883,-9.564987,5.755832,-1.614053,-4.259257,1.454699,-1.451215,5.846372,3.656486,8.306918,-7.934917,3.978068,0.887120,-4.482948,-3.693147,-6.764453,0.873942,3.500969,-4.149371,-1.728524,-9.899247,-6.795703,0.128652,-2.063226,-6.800742,-4.069501,-5.323268,-0.066916,-0.154481,-6.735097,-0.682268,5.197417,9.715645,6.666374,-8.267456,-1.416973,0.586916,3.347593,7.737222,4.830508,4.604363,-6.402282,-0.204945,-5.716182,6.909897,0.925031,5.716440,7.442167,2.986594,-2.282863,3.670556,-3.864421,7.632395,7.412827,7.219728,7.363596,-9.895882,-4.957249,-4.292125,0.482493,2.000906,7.494609,8.172751,-2.303749,5.306780,-1.539940,8.062926,-7.445300,-1.563012,3.172374,-2.094027,1.101900,-8.793471,7.764333,-5.737971,1.125644,5.976626,-2.680035,2.512568,8.002405,2.870941,3.523046,-9.375581,-6.730031,-3.601534,-2.320049,-3.602596,9.818067,-5.398534,2.643057,-2.990126,-3.641923,1.445768,-6.585845,2.818613,-5.154515,-4.458219,-4.180035,4.931159,5.719899,-2.361161,-3.652796,1.896226,-1.796047,1.623690,-4.321616,-1.417171,9.151637,2.689154,-8.933041,-4.305136,-6.466083,7.286561,2.794446,2.989958,-4.138134,9.575055,-5.772532,-5.191095,-3.054533,-6.047303,9.404150,4.307101,-0.428954,7.092942,-7.532197,4.865683,-5.095852,1.838870,2.547411,-0.330614,-0.972614,3.221961,1.367145,2.397238,4.874143,-6.473283,-2.955155,7.481621,1.563040,-2.536887,-9.530129,-2.133750,-6.181174,0.455797,-0.228813,4.271322,2.025000,9.228816,-3.702070,-0.885080,-4.410061,0.334889,-0.605955,2.868589,4.261473,0.726231,-1.308340,-5.808364,5.228379,-8.253521,5.857249,1.608779,-8.027071,5.861602,4.720288,-2.461366,5.260262,6.478726,3.452359,1.644000,-3.116822,-5.635019,-5.738455,1.807767,-3.246172,0.031162,8.605091,-5.726319,8.699745,-0.974041,5.450473,-5.615502,-9.545943,4.335433,-2.158879,-4.345867,1.307138,4.606605,5.320005,-7.712364,4.221684,-2.971506,-1.600689,-2.805923,-6.312837,-1.828566,-4.418697,-0.756111,-7.711998,-7.156530,-1.716173,6.909137,1.222915,4.378296,5.384201,8.925690,0.843717,6.655275,-0.768457,1.980794,5.409068,3.425358,-2.107079,-6.456792,2.120114,-1.358555,-7.746904,9.273934,-0.340279,-7.949996,-5.684816,-1.006307,3.771429,2.589474,-8.484777,6.482846,7.011912,0.584112,-5.305009,-1.988344,-3.903528,-6.619927,5.000527,-5.296519,-0.759388,4.521401,-7.991028,3.688572,-4.532312,-6.460747,0.607414,-3.489750,-8.645932,1.362443,8.086005,-2.658870,-6.458766,-8.777725,-5.805594,1.446270,-4.590448,-2.204419,8.677798,-8.983553,-3.473044,-7.439233,-8.244951,-3.770204,-9.162292,-0.436411,-5.985007,4.309393,7.429646,-2.014832,-2.138303,-8.877380,-8.737648,-7.856759,-5.713827,7.016337,8.354226,6.433056,-8.316334,-1.589372,5.478403,9.923855,2.929286,-5.158724,-9.067371,-6.265131,-8.917412,7.214250,2.995847,-4.085586,1.843949,8.534345,1.980402,-7.559983,-1.741995,-7.543561,8.731679,7.644864,-6.249616,4.013773,-8.727070,-8.779595,0.571419,-5.205986,6.037594,-6.236740,-9.518150,1.886888,-4.804128,-6.922015,-1.151463,-6.871967,-1.447234,-0.594092,5.276837,8.761309,2.527490,3.799362,-8.363754,-0.162407,-2.525265,-4.221342,-5.564487,8.418791,4.449436,9.980984,-4.118335,-4.764894,-1.960147,-7.388382,-9.143508,4.227571,1.226819,-7.072395,-4.680292,3.735895,-0.802294,-3.005424,5.258304,0.684909,8.247247,-2.185342,9.070001,-5.541971,9.044788,6.567131,-4.736258,0.515300,7.052453,0.596164,-2.063889,5.953249,-5.231140,2.229734,0.021428,4.653192,-8.644108,-5.641759,-9.026682,7.251899,2.444178,8.630757,9.768329,8.883927,8.111025,0.618195,6.373606,-5.119180,-7.979959,0.468540,-5.937841,-6.698076,-9.024167,-4.743221,4.160163,-7.418844,4.237536,-2.764608,2.169450,1.143370,0.733440,-6.297805,7.919571,-6.047335,2.864034,6.463813,-2.948745,-3.550435,0.518373,4.924802,-4.563604,8.612164,-2.857529,-6.763011,-5.206739,-9.762766,-5.663427,-6.878902,4.349841,2.598683,0.356340,-8.054126,-2.203401,-9.007352,-1.270995,-7.542590,-2.095034,-5.948152,-6.473430,-7.719536,-4.343702,-5.548889,0.003440,2.050618,1.596117,9.748992,6.186612,9.867314,-8.695761,4.079520,6.007491,7.268323,-2.415845,-8.633522,3.708732,6.826845,6.073828,-9.258541,-6.797411,7.035950,7.324103,-4.465517,4.515908,-4.487758,-4.389924,-5.023750,-2.579619,8.295181,0.575151,7.947730,-9.980989,-3.462760,-7.119813,-0.999705,-4.143013,-1.780942,7.609165,1.873799,-1.898823,-8.415710,4.473076,7.071443,9.189347,-0.050019,-3.608814,2.051545,-2.083018,2.302127,-5.513683,-9.129787,2.325095,-8.698373,7.200547,7.027709,-4.372106,-6.121522,-8.259022,3.604900,-0.693840,-0.124737,1.491028,9.072050,-6.535816,-3.712523,2.581068,4.434786,7.386105,9.676696,5.734484,2.589844,-0.797177,-1.144370,7.670102,-0.121476,5.257137,-4.746163,-2.493819,2.401060,-2.158471,-9.272726,-1.076143,9.637509,3.973231,-0.210607,2.195924,-0.187280,-4.772459,0.676131,-0.277580,7.578087,-3.869022,-0.452415,-9.503966,4.216833,4.281398,-7.347688,-0.085888,-0.237465,-4.751859,-3.788000,-9.514693,9.717030,5.426596,-1.132867,9.455094,-5.106310,4.795648,-8.164925,-1.932896,8.564427,9.136160,8.051266,2.134816,-5.562632,-0.245357,8.189053,7.709532,7.726591,3.197258,2.859325,-2.545366,2.509167,-4.385928,9.679786,5.817199,2.169924,-0.697073,-3.137909,-4.831786,3.051392,-3.608407,0.361622,1.234762,-5.028117,-6.987917,8.565251,9.744178,-5.947298,0.096210,-2.720310,-2.464278,9.538512,-3.001622,-2.463948,-5.558099,-4.420321,2.317263,7.843678,-3.429989,5.751254,3.550367,0.493995,8.729401,-3.525965,3.648985,-4.700626,-6.894855,-8.721511,5.540771,4.123956,-7.341310,-5.533377,9.942720,3.563801,-3.779696,-6.815229,4.707783,-9.104709,-6.240876,1.607843,-2.362766,6.868829,-7.326762,4.218975,1.811142,8.660552,-3.778714,5.411910,8.672209,-6.168245,3.687502,5.429282,-5.650034,-9.191913,6.211279,8.683158,5.877863,-9.790612,-9.893389,9.702414,1.536270,-4.398682,2.674961,8.791230,-3.925485,-4.376709,9.257380,-5.164834,4.042288,-5.635836,5.116665,-1.647078,-2.322424,-0.358024,6.011550,-8.329444,-7.902810,-3.666591,-1.506601,0.912174,3.008096,2.501765,9.867754,1.065963,-5.259200,8.984468,4.281520,-1.363825,1.822672,-9.234906,-5.769795,0.601672,9.586595,-8.576272,7.590846,-3.756390,0.849779,8.921519,-4.705761,-9.038480,-8.379706,-5.262489,4.900575,-7.388722,9.028696,4.867631,2.595590,-4.170991,7.811494,8.739192,-2.573291,2.883916,2.562163,1.142530,3.505986,-7.745331,8.312908,4.317751,4.428148,1.864028,5.088088,-0.834902,6.959387,6.738863,-2.583827,-2.917656,1.618036,-9.875069,-5.532197,-5.021360,8.409288,-9.079790,5.357805,-7.005235,4.991076,3.595503,-1.393312,1.374257,-6.158076,-9.784518,9.131664,-9.491781,8.162013,2.866501,-7.890252,6.552747,-3.869962,-0.408980,-4.218495,-0.216861,2.366491,-7.269530,-0.726096,6.996781,-5.192655,4.100789,-6.406155,-4.763275,-3.737352,-6.311217,5.358982,4.109451,5.776119,0.292991,-3.630766,6.526486,8.873147,7.481010,2.872149,5.152901,6.909871,-3.907520,-6.228350,3.007793,-8.552083,2.802387,4.124385,-3.535171,-0.963562,-0.466587,0.018457,-1.618839,0.807221,-2.847865,5.385257,1.945336,-5.715726,-5.062083,-7.175668,-6.484341,7.986218,9.518010,-1.982177,0.871658,0.857825,9.368746,3.567365,-6.759034,9.803894,-8.990755,-4.138528,2.987573,7.592467,5.040382,2.474084,-2.535681,5.074338,-5.058262,9.471853,-2.743313,8.186445,-8.178207,-2.087227,-6.206993,2.696873,-3.296215,-7.752291,6.415353,6.096186,0.233208,-2.997944,-4.381114,3.554001,6.676661,-4.748033,-8.560120,2.144181,8.764969,6.844097,7.150080,-2.938410,-4.413778,-7.446716,-3.673844,-0.897216,-1.048199,1.751500,-1.140275,6.954654,-3.143006,9.142783,-9.813947,8.344661,-6.964453,9.385629,4.944978,7.961005,-1.943543,4.290794,-6.888163,-6.820347,-6.920946,3.932543,0.795049,-8.127559,-3.971165,-7.696555,-1.640220,-7.025268,-0.177342,6.510968,9.891478,7.838556,-4.028728,-7.057882,-0.455966,9.721511,0.655824,8.270846,-9.282937,-3.959382,1.331362,9.151149,-1.669453,9.694671,3.902720,-7.722412,7.228682,-4.747814,0.361453,-4.708825,4.688814,-9.649025,-4.253606,2.455437,-3.979103,-3.733817,-5.688795,1.813456,9.516864,7.496424,3.994707,-0.582758,2.325018,-5.328589,6.732952,-8.380272,8.479489,2.702073,-3.899689,-2.196121,-8.169922,5.475393,-3.241048,2.600471,5.580736,-7.998657,6.122744,7.506560,2.143089,4.849186,0.821521,8.620928,-6.923500,-7.222483,-6.056744,2.708583,5.531760,8.429253,-0.627590,-3.814711,-0.835911,-8.565504,0.934853,-6.017118,-8.449977,6.295537,-6.916862,-1.825320,-5.515460,1.666742,6.324811,1.384159,2.123062,-5.027762,-7.018764,2.171466,7.466588,-8.592016,-8.340584,7.468534,-4.507181,-4.750192,2.559282,3.587979,3.285971,-8.443275,-1.878468,-9.119470,2.497346,7.868945,4.415369,-4.085175,-2.277103,3.103560,4.157525,0.235136,5.518887,-4.521699,-7.153900,-8.768806,5.159867,-2.312413,8.398067,7.518407,0.549203,-8.500583,-6.726805,9.882591,8.483058,1.355695,7.116209,-4.921473,-2.059687,-9.913749,-2.029726,-4.733742,2.427995,9.038703,7.414349,4.911375,6.554882,7.705070,-5.294285,1.028290,4.847737,3.709868,5.288444,-2.550457,-8.695108,3.940057,3.249768,-2.918439,-1.612157,5.043133,1.348250,5.732798,-2.786656,-1.887512,3.098746,-3.260416,-1.258469,-2.560918,9.902533,1.298700,9.980650,8.398297,-9.001172,3.089492,6.107070,5.962725,-8.392514,-9.642250,1.500424,7.855835,-7.445591,-0.369787,1.775740,-8.795858,4.615938,5.632390,-9.908022,8.779760,-1.059691,-1.298328,-7.739810,-1.543515,-1.784452,8.230902,4.439858,-5.138354,0.073511,-9.178632,5.689223,8.504441,-9.637726,0.442476,6.909101,-4.839643,-2.689256,-8.062520,-3.678518,9.684848,2.552227,-0.936008,5.222108,-5.107401,8.568467,-6.627363,1.308531,0.267695,-9.760552,8.181758,-9.523220,9.449275,-7.288830,7.700269,2.302801,7.837217,3.734074,1.519253,-4.531237,8.724669,9.651455,7.063983,-8.311789,-4.947330,1.911589,-4.684939,2.825750,-3.206837,7.234991,-0.482868,-6.083328,3.069498,-7.189931,4.374363,-1.670507,-3.653399,-0.463361,1.169240,4.397972,3.851320,0.247099,-2.326337,4.880075,-2.622109,-9.920873,0.872609,-1.980438,-5.486030,-3.244249,9.848183,9.684602,-4.636791,1.018009,-9.208375,9.482615,-4.541123,0.224996,-4.539472,4.766906,-9.128555,9.110934,3.524322,-7.259781,-0.600142,7.670462,-3.509927,-3.836820,-1.899051,-6.667509,-6.612343,-8.427105,-3.374191,7.782538,-3.445350,9.442998,-4.570679,2.645442,-1.217141,7.686485,-2.924541,-8.263314,3.572297,7.261776,4.909575,-7.211171,9.062843,-7.503927,9.613411,-2.254767,-2.445641,-2.234760,0.751736,-9.406222,0.425452,-1.245792,-7.059399,-3.220465,3.974509,8.693833,6.156247,-7.648488,-7.224238,-0.998828,-9.685914,-9.452025,-3.722478,0.032043,-0.952084,6.633537,-1.519148,3.283969,3.338095,-9.561034,8.034163,2.953738,-0.281255,0.245442,-1.106430,-7.977973,8.506585,2.468718,8.857589,0.873720,1.026442,5.985302,-9.605489,-4.049608,1.831056,3.210601,2.818265,3.763018,-9.473710,-4.129298,7.022829,-0.527282,7.324534,-1.152208,-9.277919,-9.640736,6.744282,8.221009,-1.528651,7.314180,8.255344,-3.012686,5.091006,-5.208200,5.461873,-1.237093,6.978277,0.953172,-8.803228,9.158937,9.629809,-6.148624,5.315619,-8.472734,-9.039390,4.196737,-8.169136,-6.062482,-2.088675,-1.240236,2.794970,-2.813945,5.643768,-3.745273,7.643301,-1.009765,5.559943,5.012178,1.793378,1.177210,9.766966,5.380453,-3.012782,7.899951,-7.581785,-5.009812,-0.167051,-1.339063,-6.994297,-1.708238,-9.722889,-9.573015,2.714614,-2.938657,-2.105900,-4.524236,4.421151,0.725400,5.646605,-1.109817,-6.287068,-6.483741,2.610712,-3.570416,9.262903,2.356362,-9.393665,3.654127,-7.165387,-4.246688,6.151644,-6.667165,-7.101044,0.239054,0.673002,8.014489,-3.582194,-8.918491,-7.653601,-5.048570,2.501097,9.174475,4.158529,-6.769287,-6.228709,-8.556116,8.478596,-8.763607,8.621392,-3.918977,3.838261,-4.841162,1.690645,3.134445,-3.321834,4.722632,-4.118694,8.588955,1.300537,1.338591,-2.993491,-6.799619,-2.707852,2.653254,-3.546412,-3.667161,8.388835,1.419018,-1.306637,-0.294533,-0.170132,-7.475471,-1.540136,1.823344,3.725653,9.850814,-8.571414,-5.636233,3.034984,-2.357609,3.330722,1.056961,-4.448280,6.246107,-4.828626,3.703198,7.907414,7.245179,8.152951,2.314854,2.405324,-3.287634,-6.160647,-3.115017,-9.931644,9.088895,-7.244173,-4.040487,-4.250664,9.797884,8.716118,7.806947,-8.790835,-2.012507,5.780376,7.642053,-1.212977,8.369493,-0.554479,-8.469467,-1.602567,-0.304791,8.431136,8.188935,-7.875712,-6.579073,6.140704,-9.271864,-2.081929,4.937923,-6.580725,-6.331420,-2.881504,-7.620097,0.599182,0.188037,-4.183761,-7.436079,-1.629360,3.332134,-1.756405,-6.717170,-6.999372,-4.846103,6.310676,-0.039854,-8.924819,8.765017,-2.850875,0.363232,-6.462231,-6.480956,-5.596896,-1.766932,-8.680583,5.767013,2.216908,5.804571,-9.398446,-7.876762,5.601202,2.661404,8.808936,2.982888,-8.334392,-2.160359,2.921571,-4.840157,0.497173,4.878082,-1.399043,5.932423,-6.563646,6.634348,-1.622488,3.448682,6.252228,8.949612,3.029166,-4.607054,8.931077,-2.864408,1.771368,-1.096743,-9.230540,6.185554,-4.467594,-1.652607,0.453249,8.203582,-5.078899,6.804650,6.819859,-2.033199,5.990137,6.578077,8.463484,-0.135351,-5.188335,-8.552758,-0.930926,5.612230,-5.691993,4.464002,-2.927336,5.526452,9.857861,-2.947256,9.538690,9.039760,5.472593,6.519332,0.804542,-5.599059,-8.439869,-3.103137,-2.653565,4.805206,7.182232,-3.809851,8.860637,-5.115161,-5.911890,7.356557,-6.051656,8.130508,4.105968,-5.195538,-6.372100,-2.109636,0.541583,6.427441], dtype = "float64")#candidate|12334|(1764,)|const|float64
call_12333 = relay.TupleGetItem(func_8605_call(relay.reshape(const_12334.astype('float64'), [14, 14, 9])), 1)
call_12335 = relay.TupleGetItem(func_8607_call(relay.reshape(const_12334.astype('float64'), [14, 14, 9])), 1)
func_7965_call = mod.get_global_var('func_7965')
func_7966_call = mutated_mod.get_global_var('func_7966')
call_12338 = func_7965_call()
call_12339 = func_7965_call()
bop_12353 = relay.equal(uop_12278.astype('bool'), call_12252.astype('bool')) # shape=(10, 15, 800)
bop_12356 = relay.equal(uop_12278.astype('bool'), call_12255.astype('bool')) # shape=(10, 15, 800)
uop_12358 = relay.atanh(uop_12278.astype('float64')) # shape=(800,)
bop_12365 = relay.right_shift(uop_12358.astype('uint8'), bop_12353.astype('uint8')) # shape=(10, 15, 800)
bop_12368 = relay.right_shift(uop_12358.astype('uint8'), bop_12356.astype('uint8')) # shape=(10, 15, 800)
output = relay.Tuple([call_12245,var_12253,var_12254,call_12270,call_12333,const_12334,call_12338,bop_12365,])
output2 = relay.Tuple([call_12246,var_12253,var_12254,call_12272,call_12335,const_12334,call_12339,bop_12368,])
func_12371 = relay.Function([var_12253,var_12254,], output)
mod['func_12371'] = func_12371
mod = relay.transform.InferType()(mod)
var_12372 = relay.var("var_12372", dtype = "float64", shape = (150, 1))#candidate|12372|(150, 1)|var|float64
var_12373 = relay.var("var_12373", dtype = "float64", shape = (750, 2))#candidate|12373|(750, 2)|var|float64
output = func_12371(var_12372,var_12373,)
func_12374 = relay.Function([var_12372,var_12373,], output)
mutated_mod['func_12374'] = func_12374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9130_call = mod.get_global_var('func_9130')
func_9132_call = mutated_mod.get_global_var('func_9132')
call_12430 = relay.TupleGetItem(func_9130_call(), 0)
call_12431 = relay.TupleGetItem(func_9132_call(), 0)
func_7007_call = mod.get_global_var('func_7007')
func_7009_call = mutated_mod.get_global_var('func_7009')
call_12467 = func_7007_call()
call_12468 = func_7007_call()
output = relay.Tuple([call_12430,call_12467,])
output2 = relay.Tuple([call_12431,call_12468,])
func_12473 = relay.Function([], output)
mod['func_12473'] = func_12473
mod = relay.transform.InferType()(mod)
mutated_mod['func_12473'] = func_12473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12473_call = mutated_mod.get_global_var('func_12473')
call_12474 = func_12473_call()
output = call_12474
func_12475 = relay.Function([], output)
mutated_mod['func_12475'] = func_12475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11989_call = mod.get_global_var('func_11989')
func_11991_call = mutated_mod.get_global_var('func_11991')
call_12524 = relay.TupleGetItem(func_11989_call(), 0)
call_12525 = relay.TupleGetItem(func_11991_call(), 0)
output = relay.Tuple([call_12524,])
output2 = relay.Tuple([call_12525,])
func_12540 = relay.Function([], output)
mod['func_12540'] = func_12540
mod = relay.transform.InferType()(mod)
output = func_12540()
func_12541 = relay.Function([], output)
mutated_mod['func_12541'] = func_12541
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12617 = relay.var("var_12617", dtype = "uint16", shape = (4, 10, 16))#candidate|12617|(4, 10, 16)|var|uint16
var_12618 = relay.var("var_12618", dtype = "uint16", shape = (4, 10, 16))#candidate|12618|(4, 10, 16)|var|uint16
bop_12619 = relay.add(var_12617.astype('uint16'), relay.reshape(var_12618.astype('uint16'), relay.shape_of(var_12617))) # shape=(4, 10, 16)
output = relay.Tuple([bop_12619,])
output2 = relay.Tuple([bop_12619,])
func_12624 = relay.Function([var_12617,var_12618,], output)
mod['func_12624'] = func_12624
mod = relay.transform.InferType()(mod)
mutated_mod['func_12624'] = func_12624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12624_call = mutated_mod.get_global_var('func_12624')
var_12626 = relay.var("var_12626", dtype = "uint16", shape = (4, 10, 16))#candidate|12626|(4, 10, 16)|var|uint16
var_12627 = relay.var("var_12627", dtype = "uint16", shape = (4, 10, 16))#candidate|12627|(4, 10, 16)|var|uint16
call_12625 = func_12624_call(var_12626,var_12627,)
output = call_12625
func_12628 = relay.Function([var_12626,var_12627,], output)
mutated_mod['func_12628'] = func_12628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11413_call = mod.get_global_var('func_11413')
func_11415_call = mutated_mod.get_global_var('func_11415')
call_12630 = relay.TupleGetItem(func_11413_call(), 0)
call_12631 = relay.TupleGetItem(func_11415_call(), 0)
func_6967_call = mod.get_global_var('func_6967')
func_6968_call = mutated_mod.get_global_var('func_6968')
call_12637 = relay.TupleGetItem(func_6967_call(), 0)
call_12638 = relay.TupleGetItem(func_6968_call(), 0)
func_7328_call = mod.get_global_var('func_7328')
func_7331_call = mutated_mod.get_global_var('func_7331')
call_12652 = relay.TupleGetItem(func_7328_call(relay.reshape(call_12630.astype('uint32'), [63, 2])), 2)
call_12653 = relay.TupleGetItem(func_7331_call(relay.reshape(call_12630.astype('uint32'), [63, 2])), 2)
bop_12665 = relay.left_shift(call_12652.astype('uint16'), relay.reshape(call_12630.astype('uint16'), relay.shape_of(call_12652))) # shape=(63, 2)
bop_12668 = relay.left_shift(call_12653.astype('uint16'), relay.reshape(call_12631.astype('uint16'), relay.shape_of(call_12653))) # shape=(63, 2)
output = relay.Tuple([call_12637,bop_12665,])
output2 = relay.Tuple([call_12638,bop_12668,])
func_12671 = relay.Function([], output)
mod['func_12671'] = func_12671
mod = relay.transform.InferType()(mod)
mutated_mod['func_12671'] = func_12671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12671_call = mutated_mod.get_global_var('func_12671')
call_12672 = func_12671_call()
output = call_12672
func_12673 = relay.Function([], output)
mutated_mod['func_12673'] = func_12673
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12696 = relay.var("var_12696", dtype = "int64", shape = ())#candidate|12696|()|var|int64
var_12697 = relay.var("var_12697", dtype = "int64", shape = (13, 13, 12))#candidate|12697|(13, 13, 12)|var|int64
bop_12698 = relay.greater(var_12696.astype('bool'), var_12697.astype('bool')) # shape=(13, 13, 12)
output = relay.Tuple([bop_12698,])
output2 = relay.Tuple([bop_12698,])
func_12708 = relay.Function([var_12696,var_12697,], output)
mod['func_12708'] = func_12708
mod = relay.transform.InferType()(mod)
var_12709 = relay.var("var_12709", dtype = "int64", shape = ())#candidate|12709|()|var|int64
var_12710 = relay.var("var_12710", dtype = "int64", shape = (13, 13, 12))#candidate|12710|(13, 13, 12)|var|int64
output = func_12708(var_12709,var_12710,)
func_12711 = relay.Function([var_12709,var_12710,], output)
mutated_mod['func_12711'] = func_12711
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12741 = relay.var("var_12741", dtype = "float32", shape = (10, 6, 14))#candidate|12741|(10, 6, 14)|var|float32
var_12742 = relay.var("var_12742", dtype = "float32", shape = (10, 6, 14))#candidate|12742|(10, 6, 14)|var|float32
bop_12743 = relay.not_equal(var_12741.astype('bool'), relay.reshape(var_12742.astype('bool'), relay.shape_of(var_12741))) # shape=(10, 6, 14)
output = bop_12743
output2 = bop_12743
func_12751 = relay.Function([var_12741,var_12742,], output)
mod['func_12751'] = func_12751
mod = relay.transform.InferType()(mod)
mutated_mod['func_12751'] = func_12751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12751_call = mutated_mod.get_global_var('func_12751')
var_12753 = relay.var("var_12753", dtype = "float32", shape = (10, 6, 14))#candidate|12753|(10, 6, 14)|var|float32
var_12754 = relay.var("var_12754", dtype = "float32", shape = (10, 6, 14))#candidate|12754|(10, 6, 14)|var|float32
call_12752 = func_12751_call(var_12753,var_12754,)
output = call_12752
func_12755 = relay.Function([var_12753,var_12754,], output)
mutated_mod['func_12755'] = func_12755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11605_call = mod.get_global_var('func_11605')
func_11607_call = mutated_mod.get_global_var('func_11607')
call_12773 = relay.TupleGetItem(func_11605_call(), 0)
call_12774 = relay.TupleGetItem(func_11607_call(), 0)
output = relay.Tuple([call_12773,])
output2 = relay.Tuple([call_12774,])
func_12778 = relay.Function([], output)
mod['func_12778'] = func_12778
mod = relay.transform.InferType()(mod)
output = func_12778()
func_12779 = relay.Function([], output)
mutated_mod['func_12779'] = func_12779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7007_call = mod.get_global_var('func_7007')
func_7009_call = mutated_mod.get_global_var('func_7009')
call_12780 = func_7007_call()
call_12781 = func_7007_call()
output = call_12780
output2 = call_12781
func_12796 = relay.Function([], output)
mod['func_12796'] = func_12796
mod = relay.transform.InferType()(mod)
output = func_12796()
func_12797 = relay.Function([], output)
mutated_mod['func_12797'] = func_12797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11616_call = mod.get_global_var('func_11616')
func_11617_call = mutated_mod.get_global_var('func_11617')
call_12814 = func_11616_call()
call_12815 = func_11616_call()
uop_12821 = relay.tan(call_12814.astype('float64')) # shape=(15, 2, 13)
uop_12823 = relay.tan(call_12815.astype('float64')) # shape=(15, 2, 13)
output = uop_12821
output2 = uop_12823
func_12828 = relay.Function([], output)
mod['func_12828'] = func_12828
mod = relay.transform.InferType()(mod)
output = func_12828()
func_12829 = relay.Function([], output)
mutated_mod['func_12829'] = func_12829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10381_call = mod.get_global_var('func_10381')
func_10382_call = mutated_mod.get_global_var('func_10382')
call_12857 = relay.TupleGetItem(func_10381_call(), 0)
call_12858 = relay.TupleGetItem(func_10382_call(), 0)
output = relay.Tuple([call_12857,])
output2 = relay.Tuple([call_12858,])
func_12873 = relay.Function([], output)
mod['func_12873'] = func_12873
mod = relay.transform.InferType()(mod)
mutated_mod['func_12873'] = func_12873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12873_call = mutated_mod.get_global_var('func_12873')
call_12874 = func_12873_call()
output = call_12874
func_12875 = relay.Function([], output)
mutated_mod['func_12875'] = func_12875
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12885 = relay.const(9, dtype = "uint64")#candidate|12885|()|const|uint64
var_12886 = relay.var("var_12886", dtype = "uint64", shape = (4, 14, 2))#candidate|12886|(4, 14, 2)|var|uint64
bop_12887 = relay.greater(const_12885.astype('bool'), var_12886.astype('bool')) # shape=(4, 14, 2)
output = bop_12887
output2 = bop_12887
func_12895 = relay.Function([var_12886,], output)
mod['func_12895'] = func_12895
mod = relay.transform.InferType()(mod)
var_12896 = relay.var("var_12896", dtype = "uint64", shape = (4, 14, 2))#candidate|12896|(4, 14, 2)|var|uint64
output = func_12895(var_12896)
func_12897 = relay.Function([var_12896], output)
mutated_mod['func_12897'] = func_12897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11605_call = mod.get_global_var('func_11605')
func_11607_call = mutated_mod.get_global_var('func_11607')
call_12899 = relay.TupleGetItem(func_11605_call(), 0)
call_12900 = relay.TupleGetItem(func_11607_call(), 0)
func_6692_call = mod.get_global_var('func_6692')
func_6695_call = mutated_mod.get_global_var('func_6695')
const_12926 = relay.const([6.712998,-1.555009,6.033671,-3.319126,-6.766437,2.587240,-2.987459,-7.272584,4.189123,6.692896,8.389411,-7.963097,-2.884051,-5.471710,-9.913112,4.949056,2.439987,8.275856,5.211249,1.462408,4.326130,5.177072,9.922175,-3.796900,-0.746049,5.199959,-1.068714,-6.161541,-2.134837,-3.391862,-8.464754,-1.646693,3.238546,3.950321,6.032519,5.357810,0.524996,-4.605827,-0.700236,8.365079,-2.367354,-4.259055,7.124272,9.201309,0.414915,-2.373232,-7.475122,3.726643,1.498526,-2.718513,7.514905,7.491201,4.488845,2.542626,-7.252643,-1.629097,2.254654,7.224737,5.875427,0.469312,-8.914553,6.491525,-4.372294,-2.713945,8.165359,8.509605,-6.700078,3.530525,-7.641042,6.473382,-9.479596,-2.598382,-3.701259,-8.906022,-6.616597,-7.263674,9.411165,7.343122,-4.237089,3.581649,4.339588,2.321863,2.008286,0.350614,7.746073,-5.685200,-6.115475,-6.458689,-4.957349,9.082347,-7.316306,9.059202,3.603563,3.673555,6.367856,0.608053,3.564441,-2.635119,7.846030,1.030157,2.540832,-3.242576,-5.874494,-1.662081,8.487122,3.232000,-6.734770,-6.529628,-7.876808,6.543393,-0.768388,-3.008492,4.590387,2.151164,-7.851019,-3.622657,-9.625007,3.725840,1.176036,-7.447350,0.304970,-8.899189,-3.725633,5.482061,-8.357675,-7.503223,4.363311,2.177790,-6.523220,-7.671540,0.103464,-4.803618,0.274799,-0.936867,7.383556,-4.411132,-5.173967,-9.854479,1.431171,6.681961,1.142984,-9.325048,-1.202811,3.190031,-4.664228,1.840274,-2.917955,-6.920460,-0.308900,-4.268955,7.236065,-6.196335,8.042588,-6.761067,3.624016,7.624168,-3.370254,0.616581,9.657491,9.797936,-9.086302,8.019660,-1.508126,0.468250,-3.174640,-2.638429,-6.439211,7.131960,-7.418550,-8.321770,-2.683482,-7.217743,3.371798,8.829238,-8.371676,7.468448,-4.049194,-1.160929,-3.603049,5.632354,6.579414,-5.917330,-3.710614,-3.961469,3.122434,-6.224188,-3.168817,-6.746835,9.022542,-0.312411,-2.499275,-7.758520,-0.537444,2.309584,-2.223427,9.872471,7.137048,7.997137,5.595563,-4.103304,-0.509883,-6.956495,8.555583,8.320312,7.176241,-1.513099,6.819542,-8.208900,0.458717,-4.881675,-0.800767,-9.953068,7.254750,3.247177,7.061053,8.769216,3.733844,-5.714723,0.904138,5.584574,1.312231,-5.717531,-9.144696,-2.784952,7.308280,-6.580632,-1.060290,4.685155,-1.546131,-3.885759,-8.089703,-5.471564,-4.160438,-0.992522,-9.954118,-5.011431,3.979886,-7.727490,5.315980,-6.031153,1.071964,-4.780527,9.689055,0.118016,-5.763524,4.748064,5.360631,-2.721974,-5.429795,0.620253,-0.954601,-6.809147,9.096090,-0.394723,8.156919,9.041412,8.360636,-3.249419,6.293046,-6.145856,8.719966,-9.274756,0.596969,-6.421331,3.711098,-3.970259,3.463496,0.158293,7.074970,8.508598,-6.991433,7.965564,-4.867818,-0.686576,1.569985,-6.796971,-7.029582,-6.312917,9.837752,4.504002,-4.607412,6.720685,-0.421802,-8.028922,-9.494120,-0.373607,-4.347369,-0.783241,9.079082,-8.417579,9.383746,-7.043641,1.109076,-8.443319,7.373630,5.323156,2.295324,-7.905676,-2.887637,-6.428574,-6.186876,3.716942,-0.073658,-6.390200,9.007813,7.669958,3.831938,-4.350096,-2.376861,6.559927,2.209103,6.841052,7.029096,-1.422683,6.473717,-9.362147,-1.584330,-2.623344,9.625585,-9.990052,-5.926543,-7.793238,8.477716,-5.361992,3.787179,-8.399709,5.616015,2.012097,0.062816,-6.024315,-0.066619,-9.190195,-2.224125,-1.396260,9.197962,-9.753918,-8.611151,6.503124,-2.307725,8.522013,-5.999093,-4.814267,9.410848,-5.191201,1.510295,7.356436,-1.631747,-2.724546,3.630823,-6.876301,-3.535387,-4.478532,1.580040,-3.451948,7.393927,6.682609,9.130059,6.142312,-0.509142,3.300065,-3.820182,1.487519,5.595124,-1.604126,-8.057615,4.840580,1.258856,2.375252,-5.404208,-6.866014,6.580670,8.766048,5.804871,-4.040137,-8.772227,-1.373425,-7.696354,1.253070], dtype = "float32")#candidate|12926|(378,)|const|float32
call_12925 = relay.TupleGetItem(func_6692_call(relay.reshape(const_12926.astype('float32'), [9, 14, 3])), 0)
call_12927 = relay.TupleGetItem(func_6695_call(relay.reshape(const_12926.astype('float32'), [9, 14, 3])), 0)
output = relay.Tuple([call_12899,call_12925,const_12926,])
output2 = relay.Tuple([call_12900,call_12927,const_12926,])
func_12928 = relay.Function([], output)
mod['func_12928'] = func_12928
mod = relay.transform.InferType()(mod)
output = func_12928()
func_12929 = relay.Function([], output)
mutated_mod['func_12929'] = func_12929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mod.get_global_var('func_7037')
func_7039_call = mutated_mod.get_global_var('func_7039')
call_12976 = relay.TupleGetItem(func_7037_call(), 0)
call_12977 = relay.TupleGetItem(func_7039_call(), 0)
output = call_12976
output2 = call_12977
func_12993 = relay.Function([], output)
mod['func_12993'] = func_12993
mod = relay.transform.InferType()(mod)
output = func_12993()
func_12994 = relay.Function([], output)
mutated_mod['func_12994'] = func_12994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10702_call = mod.get_global_var('func_10702')
func_10703_call = mutated_mod.get_global_var('func_10703')
call_13001 = relay.TupleGetItem(func_10702_call(), 0)
call_13002 = relay.TupleGetItem(func_10703_call(), 0)
func_6295_call = mod.get_global_var('func_6295')
func_6296_call = mutated_mod.get_global_var('func_6296')
call_13003 = relay.TupleGetItem(func_6295_call(), 0)
call_13004 = relay.TupleGetItem(func_6296_call(), 0)
output = relay.Tuple([call_13001,call_13003,])
output2 = relay.Tuple([call_13002,call_13004,])
func_13010 = relay.Function([], output)
mod['func_13010'] = func_13010
mod = relay.transform.InferType()(mod)
output = func_13010()
func_13011 = relay.Function([], output)
mutated_mod['func_13011'] = func_13011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11156_call = mod.get_global_var('func_11156')
func_11157_call = mutated_mod.get_global_var('func_11157')
call_13023 = func_11156_call()
call_13024 = func_11156_call()
output = call_13023
output2 = call_13024
func_13029 = relay.Function([], output)
mod['func_13029'] = func_13029
mod = relay.transform.InferType()(mod)
mutated_mod['func_13029'] = func_13029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13029_call = mutated_mod.get_global_var('func_13029')
call_13030 = func_13029_call()
output = call_13030
func_13031 = relay.Function([], output)
mutated_mod['func_13031'] = func_13031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7007_call = mod.get_global_var('func_7007')
func_7009_call = mutated_mod.get_global_var('func_7009')
call_13114 = func_7007_call()
call_13115 = func_7007_call()
output = call_13114
output2 = call_13115
func_13116 = relay.Function([], output)
mod['func_13116'] = func_13116
mod = relay.transform.InferType()(mod)
mutated_mod['func_13116'] = func_13116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13116_call = mutated_mod.get_global_var('func_13116')
call_13117 = func_13116_call()
output = call_13117
func_13118 = relay.Function([], output)
mutated_mod['func_13118'] = func_13118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9422_call = mod.get_global_var('func_9422')
func_9423_call = mutated_mod.get_global_var('func_9423')
call_13143 = relay.TupleGetItem(func_9422_call(), 3)
call_13144 = relay.TupleGetItem(func_9423_call(), 3)
uop_13146 = relay.sinh(call_13143.astype('float64')) # shape=(126,)
uop_13148 = relay.sinh(call_13144.astype('float64')) # shape=(126,)
output = uop_13146
output2 = uop_13148
func_13155 = relay.Function([], output)
mod['func_13155'] = func_13155
mod = relay.transform.InferType()(mod)
mutated_mod['func_13155'] = func_13155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13155_call = mutated_mod.get_global_var('func_13155')
call_13156 = func_13155_call()
output = call_13156
func_13157 = relay.Function([], output)
mutated_mod['func_13157'] = func_13157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11616_call = mod.get_global_var('func_11616')
func_11617_call = mutated_mod.get_global_var('func_11617')
call_13175 = func_11616_call()
call_13176 = func_11616_call()
output = call_13175
output2 = call_13176
func_13183 = relay.Function([], output)
mod['func_13183'] = func_13183
mod = relay.transform.InferType()(mod)
mutated_mod['func_13183'] = func_13183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13183_call = mutated_mod.get_global_var('func_13183')
call_13184 = func_13183_call()
output = call_13184
func_13185 = relay.Function([], output)
mutated_mod['func_13185'] = func_13185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12540_call = mod.get_global_var('func_12540')
func_12541_call = mutated_mod.get_global_var('func_12541')
call_13198 = relay.TupleGetItem(func_12540_call(), 0)
call_13199 = relay.TupleGetItem(func_12541_call(), 0)
output = relay.Tuple([call_13198,])
output2 = relay.Tuple([call_13199,])
func_13202 = relay.Function([], output)
mod['func_13202'] = func_13202
mod = relay.transform.InferType()(mod)
output = func_13202()
func_13203 = relay.Function([], output)
mutated_mod['func_13203'] = func_13203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9422_call = mod.get_global_var('func_9422')
func_9423_call = mutated_mod.get_global_var('func_9423')
call_13217 = relay.TupleGetItem(func_9422_call(), 4)
call_13218 = relay.TupleGetItem(func_9423_call(), 4)
output = relay.Tuple([call_13217,])
output2 = relay.Tuple([call_13218,])
func_13219 = relay.Function([], output)
mod['func_13219'] = func_13219
mod = relay.transform.InferType()(mod)
mutated_mod['func_13219'] = func_13219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13219_call = mutated_mod.get_global_var('func_13219')
call_13220 = func_13219_call()
output = call_13220
func_13221 = relay.Function([], output)
mutated_mod['func_13221'] = func_13221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mod.get_global_var('func_7037')
func_7039_call = mutated_mod.get_global_var('func_7039')
call_13241 = relay.TupleGetItem(func_7037_call(), 0)
call_13242 = relay.TupleGetItem(func_7039_call(), 0)
output = call_13241
output2 = call_13242
func_13251 = relay.Function([], output)
mod['func_13251'] = func_13251
mod = relay.transform.InferType()(mod)
output = func_13251()
func_13252 = relay.Function([], output)
mutated_mod['func_13252'] = func_13252
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13302 = relay.const([[[3.522857,-8.845197,-4.429184,-8.812518,-9.024203,-3.256028,-2.518274,-5.943288],[2.376013,-9.903171,-1.856955,-4.955339,-6.637549,-2.919582,2.700020,-5.371014],[-7.765022,-4.681743,-8.434340,-6.967014,-3.658355,2.890271,-4.725509,-5.078611],[-2.767224,2.508606,-5.658790,-5.504252,-2.802046,3.629114,-2.698783,-2.252239],[-3.220832,3.949869,4.375070,6.353343,-5.630977,3.916561,2.283137,9.527608],[-1.391318,-0.499310,-0.281555,-7.224722,9.834644,8.849702,7.641434,-0.188409],[-9.524688,8.289069,0.025042,7.935666,0.361340,-1.762084,8.266798,-6.150347],[-6.565781,-2.232112,7.404139,0.198666,-7.385937,-1.770991,-7.648490,-3.843981],[-5.639439,1.511211,-2.267686,7.563745,6.702191,-5.761323,2.024859,-7.974750],[5.188107,6.569265,0.773312,3.867752,9.408980,-9.145658,2.485593,-4.669377],[-1.764054,5.934817,-5.049822,-0.228041,8.280585,-1.519925,7.444093,-5.167180],[8.447576,4.046208,4.651730,3.241599,-1.620539,-6.105175,-3.866432,5.604819],[-9.663950,2.285542,7.143577,-3.694215,5.802486,-0.091067,-1.028385,1.003930],[-7.803874,-9.249255,-3.386865,-1.989021,4.354633,-5.611279,6.539336,-7.196936]],[[-5.023910,-2.613357,1.223280,-3.325587,-0.166597,4.556002,-3.689892,-1.247099],[3.302328,-0.338404,-1.946851,-3.077184,0.805513,3.854924,-6.617863,4.203563],[-4.253600,3.458030,-7.992913,-8.946613,-7.059776,3.089298,-8.514880,6.733791],[7.766476,4.653843,-4.455746,1.033959,-5.952395,-7.967333,1.891569,-7.473682],[3.519381,5.706039,5.256190,-0.496591,-2.525822,-2.602523,-8.549935,-3.229570],[5.341107,7.867417,-9.775237,-1.796903,-8.680495,7.478556,-5.234098,9.879427],[7.735406,7.833231,-8.677463,-4.822549,-2.792607,2.201578,-7.243334,-3.765485],[-2.053830,3.758533,-1.113794,6.393060,-0.147966,-8.909750,-2.071277,1.403610],[3.398492,9.840627,-5.468068,-6.035048,-4.909629,0.325208,3.094873,3.167914],[-3.790702,-3.271745,-0.099404,4.276452,5.391309,4.954355,2.402906,2.691825],[1.066640,-6.252098,4.038030,-8.451995,-5.602122,-1.926048,0.534100,9.010119],[7.080028,9.622068,-7.331307,-4.556438,-1.195777,8.142446,-2.590477,-6.435368],[2.234747,-6.413783,0.643867,2.911560,-1.226382,-4.699286,6.260417,4.889388],[4.688164,-5.521961,0.489104,4.199772,-5.830618,9.600873,-9.109427,-2.968413]],[[-8.864907,-2.490482,-3.005266,-8.279858,7.720104,-0.065727,-0.612925,9.357362],[-1.100346,0.706789,5.055955,-5.502692,-7.214339,-9.709709,6.606995,-0.990410],[5.786319,-8.777851,-2.137956,5.362928,2.332792,-9.167899,7.420290,3.353763],[9.214336,-0.641974,-9.554907,-3.271788,-9.170537,4.100479,-3.257405,-9.951892],[-0.580968,8.067598,7.655204,-1.469964,-1.620421,-7.834853,2.224592,-6.509144],[6.232358,1.845130,7.624971,-9.740527,-1.696970,5.375023,2.432062,4.038144],[-9.845771,6.075818,4.335033,-9.806239,-1.107443,4.258381,0.822893,3.843879],[-7.359415,-9.447784,-2.292110,-7.131867,-2.962325,6.394991,5.735670,3.364146],[5.487815,2.185327,-6.816594,2.043411,-4.359018,-2.930871,-4.943280,-7.828242],[-0.041525,-9.685564,2.368582,-3.840784,-9.277487,-1.589099,-6.791079,-9.121413],[-6.393901,-2.802589,9.940460,5.764345,-6.135305,1.603557,4.035976,-4.098924],[-6.755375,9.053624,9.484523,8.855438,2.185093,0.028464,7.719384,-8.040012],[3.286150,1.676164,-0.137546,-3.056236,-6.232371,7.226648,-7.260356,-4.355130],[-9.284619,-7.047721,7.625903,7.659720,1.492265,-4.509859,-3.134014,-8.207771]],[[7.415801,4.929279,1.808919,-7.091832,2.175902,5.019876,1.278587,5.790909],[6.449786,1.750339,6.681136,-6.158821,8.913151,-7.559447,1.746620,5.424278],[-5.073200,-6.693688,7.673400,1.188354,-7.501193,-7.319633,-0.896288,3.388929],[2.403507,-4.239280,1.709652,-1.125663,8.940779,7.957553,9.193141,9.015472],[1.198410,9.949383,3.375235,3.898534,-4.754104,4.005026,2.595909,-8.799109],[-8.459769,-0.342092,4.274217,-1.841073,2.005557,7.408908,5.072154,-6.287390],[-7.321424,1.622015,-8.075820,7.935017,-9.165631,-8.847134,6.025334,-8.865167],[5.476766,-4.034107,7.871191,-2.178519,-4.570629,-3.221140,-3.492063,-4.891792],[-8.618691,-2.660308,-4.535003,3.092189,7.738824,0.664221,6.850244,-5.211269],[-4.403457,0.798664,8.013484,-2.070651,-2.820031,8.349279,7.582730,5.133293],[8.559765,-9.810550,-4.459272,-0.019674,9.750869,-3.750650,-2.869345,-1.718053],[8.818638,-3.002797,0.723358,-3.285187,5.961027,-8.395569,2.455903,5.597338],[-5.108185,1.593524,2.360721,-4.037491,3.613154,2.925332,3.558723,-8.683507],[-9.956973,0.938654,9.463592,9.559579,-8.024369,9.808764,4.911050,-2.552282]],[[-0.123965,-7.248904,-5.603335,7.983529,-3.887703,3.933852,-7.190412,-4.848767],[-6.672535,-0.989080,-9.151706,6.246074,4.907189,-9.951293,8.116411,-6.312210],[-4.252383,2.712047,1.216866,-7.819407,-7.023865,1.364030,5.712275,6.056238],[-1.134010,0.774537,6.688326,5.649334,4.972241,5.375109,-3.648511,4.854197],[3.923257,7.551631,9.546642,-7.629450,2.449974,-5.251430,6.799611,4.070988],[3.462572,-5.730063,5.250698,0.093042,-7.809300,3.378046,8.009165,1.993967],[1.590545,8.502397,3.182000,-3.137396,-7.414078,2.763578,-2.494637,4.222732],[-3.006239,-6.397653,0.643913,-3.873030,5.839469,-9.307539,-2.824854,2.932768],[7.032373,-1.438465,-0.374281,5.666638,7.327451,-4.713868,0.140113,2.616155],[-3.651301,6.647760,-4.724861,2.178255,9.644366,-2.461479,4.846831,-5.564964],[-8.745468,7.058875,6.106951,5.780506,-6.879875,7.999427,4.122223,8.546903],[-9.562300,4.480657,-4.635657,-1.855248,9.926554,-3.477337,-6.227656,2.958976],[0.033892,5.295759,6.657341,-9.348202,5.023140,-1.416432,-3.338096,-6.124666],[-2.942428,7.211268,-5.590224,0.690528,-5.194522,-8.873955,-4.119905,-0.264066]]], dtype = "float32")#candidate|13302|(5, 14, 8)|const|float32
uop_13303 = relay.log(const_13302.astype('float32')) # shape=(5, 14, 8)
func_6284_call = mod.get_global_var('func_6284')
func_6287_call = mutated_mod.get_global_var('func_6287')
const_13337 = relay.const([-7,-6,6,-4,-5,-9,-4,-7,-1,-7,-9,-1,1,-2,-4,-9,3,-9,-9,1,10,1,4,-2,-3,9,-4,-2,6,3,-2,-10,-10,-5,2,5,8,5,-5,7,5,-1,6,-3,-7,2,-3,-4,9,-3,7,-2,-3,-7,3,-8,1,1,-3,2,3,9,4,8,-5,6,-9,7,7,-2,-9,1,2,-7,-6,-6,1,-6,1,10,-5,7,7,5,9,6,-8,6,-9,-4,2,-8,7,9,8,-5,-10,-4,-8,10,-6,5,-3,5,-4,1,-1,2,-2,8,-2,10,7,8,-5,-3,7,7,9,-4,-3,2,5,-3,-4,-5], dtype = "uint32")#candidate|13337|(126,)|const|uint32
var_13338 = relay.var("var_13338", dtype = "uint32", shape = (252, 4))#candidate|13338|(252, 4)|var|uint32
call_13336 = relay.TupleGetItem(func_6284_call(relay.reshape(const_13337.astype('uint32'), [126,]), relay.reshape(var_13338.astype('uint32'), [1008,]), ), 2)
call_13339 = relay.TupleGetItem(func_6287_call(relay.reshape(const_13337.astype('uint32'), [126,]), relay.reshape(var_13338.astype('uint32'), [1008,]), ), 2)
output = relay.Tuple([uop_13303,call_13336,const_13337,var_13338,])
output2 = relay.Tuple([uop_13303,call_13339,const_13337,var_13338,])
func_13342 = relay.Function([var_13338,], output)
mod['func_13342'] = func_13342
mod = relay.transform.InferType()(mod)
mutated_mod['func_13342'] = func_13342
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13343 = relay.var("var_13343", dtype = "uint32", shape = (252, 4))#candidate|13343|(252, 4)|var|uint32
func_13342_call = mutated_mod.get_global_var('func_13342')
call_13344 = func_13342_call(var_13343)
output = call_13344
func_13345 = relay.Function([var_13343], output)
mutated_mod['func_13345'] = func_13345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13116_call = mod.get_global_var('func_13116')
func_13118_call = mutated_mod.get_global_var('func_13118')
call_13463 = func_13116_call()
call_13464 = func_13116_call()
output = call_13463
output2 = call_13464
func_13465 = relay.Function([], output)
mod['func_13465'] = func_13465
mod = relay.transform.InferType()(mod)
output = func_13465()
func_13466 = relay.Function([], output)
mutated_mod['func_13466'] = func_13466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7674_call = mod.get_global_var('func_7674')
func_7675_call = mutated_mod.get_global_var('func_7675')
call_13467 = relay.TupleGetItem(func_7674_call(), 0)
call_13468 = relay.TupleGetItem(func_7675_call(), 0)
output = relay.Tuple([call_13467,])
output2 = relay.Tuple([call_13468,])
func_13480 = relay.Function([], output)
mod['func_13480'] = func_13480
mod = relay.transform.InferType()(mod)
output = func_13480()
func_13481 = relay.Function([], output)
mutated_mod['func_13481'] = func_13481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10957_call = mod.get_global_var('func_10957')
func_10959_call = mutated_mod.get_global_var('func_10959')
call_13485 = relay.TupleGetItem(func_10957_call(), 0)
call_13486 = relay.TupleGetItem(func_10959_call(), 0)
output = relay.Tuple([call_13485,])
output2 = relay.Tuple([call_13486,])
func_13498 = relay.Function([], output)
mod['func_13498'] = func_13498
mod = relay.transform.InferType()(mod)
output = func_13498()
func_13499 = relay.Function([], output)
mutated_mod['func_13499'] = func_13499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11656_call = mod.get_global_var('func_11656')
func_11658_call = mutated_mod.get_global_var('func_11658')
call_13502 = relay.TupleGetItem(func_11656_call(), 0)
call_13503 = relay.TupleGetItem(func_11658_call(), 0)
func_10460_call = mod.get_global_var('func_10460')
func_10464_call = mutated_mod.get_global_var('func_10464')
const_13519 = relay.const([5.560275,-4.109479,-9.301536,6.639575,6.766529,-9.984807,8.268812,-7.216008,-2.103940,2.681417,3.081635,2.545487,9.360276,-1.371383,4.114501,-2.412795,5.699678,1.786037,-2.714366,5.607503,-6.566091,-9.917977,-1.825436,6.898391,2.503317,-6.148238,-4.793673,9.673436,-4.233213,-6.302512,0.961600,2.633972,-9.242292,-1.289558,0.531285,-1.624179,-7.307957,-6.960405,0.970351,0.080102,-5.319562,-5.050735,8.017152,-3.657286,8.174183,9.817073,9.522008,-4.432987,-2.051728,-6.387285,-1.039104,6.342653,7.483348,8.602381,6.147577,1.130306,1.508188,-3.207277,1.127374,-6.373551,-5.368300,1.059716,-6.364839,9.230905,7.428701,5.086662,-3.990577,-3.941903,-6.937017,-5.635557,-2.311202,2.936930,7.604981,2.376123,-0.847954,-3.608739,9.838350,-7.150791,0.191142,-9.327024,8.672350,-7.947083,-2.891749,6.206133,-0.452875,6.746359,9.224434,-2.223242,-1.336881,9.490137,-3.492479,5.728453,5.818139,4.769863,5.553619,9.948168,2.900880,-0.409945,-1.565443,-8.517276,-0.445783,-1.875974,-3.224998,-2.661948,-2.153120,0.288894,5.656683,-4.186397,-7.075596,6.407454,-6.587517,-8.561547,-7.084074,2.126927,-9.254051,-5.117026,5.604086,-6.950898,3.923383,4.829639,-4.473525,-5.273972,6.469763,6.796260,0.933338,-0.166216,6.187484,6.132295,4.968286,2.210799,4.688611,-1.665465,-8.280977,-0.530790,-0.161209,5.056477,0.136492,-5.162607,-1.788057,-8.167578,9.281478,7.814865,-5.440570,-5.800794,-1.372508,2.041624,2.672581,-6.402773,9.563881,-6.950162,-6.780094,-7.231382,9.201464,4.560723,-2.191543,3.889863,-2.077725,7.495336,-7.753671,-7.465074,9.356142,-0.970160,-3.152804,-4.306151,5.116331,8.830558,-8.604554,1.474843,-2.635443,8.528232,0.985127,-0.071727,-7.751133,-0.283181,-2.663250,7.835620,-3.084037,-8.576969,-1.134708,-4.360960,7.506394,-6.794585,-6.827742,-6.500383,-8.111716,0.942960,-9.056120,3.206828,9.377008,7.931035,-0.094184,5.413987,-7.572145,3.435330,-2.134054,2.211956,2.274456,8.953580,0.128345,2.793465,-3.701426,1.193493,-5.701824,0.432997,-8.732157,3.315187,5.295212,-7.357843,4.056558,-6.147026,1.002447,1.320006,0.249524,-7.930435,-6.042304,-3.214875,4.613050,-5.492480,-3.847858,1.235223,-4.785723,-4.663559,-3.000866,-2.886967,-5.247714,8.856359,-2.220459,8.048917,-3.688239,-1.159147,5.848793,8.850046,4.560932,-6.731940,2.213989,-9.798034,4.622605,1.978321,9.809639,0.357049,-9.713231,-4.156170,1.269992,0.830873,8.398441,4.443356,-6.600253,7.039387,-6.995159,-8.876700,-7.342498,3.274654,8.016371,9.815433,-5.488031,-5.246124,7.078249,2.174031,-9.588849,-9.928647,8.062590,-1.504205,-6.781987,9.044584,-7.971044,-5.696405,-6.372626,-3.381491,-4.440286,2.209896,-0.756708,-3.680877,-7.723408,-4.632119,-7.500632,-0.821188,-0.062056,6.899552,4.531816,2.484549,-5.731642,-8.037153,-6.594945,-2.800290,-0.903245,8.001002,-4.962833,-0.213573,-9.791483,9.152339,-9.248286,-1.868457,4.100485,7.259547,-7.502277,-2.665009,3.320711,1.372603,9.244637,-8.504451,1.689854,-7.470824,5.062254,-7.180031,0.827433,-9.029861,-1.081571,7.230131,2.121204,-5.115207,0.045625,-5.572177,7.509803,-9.178831,-8.555640,-7.143437,5.673522,0.218313,1.721637,-2.999869,9.278524,-7.779370,4.263874,3.376835,6.493605,-0.415695,-6.280526,4.075341,-7.483058,-9.329721,-5.211273,8.355655,4.545594,5.259318,-6.727766,-4.695813,-3.411941,2.530839,-1.711811,-5.676529,-7.413672,-2.781226,-2.928742,-4.968312,-8.285313,1.613039,9.780809,-2.884144,4.107732,-2.858173,0.593846,4.563379,8.057794,9.097125,-8.605648,9.069765,-5.749529,8.077965,2.264616,7.744801,9.265008,8.437064,0.614583,0.251784,0.697565,7.572763,-9.011525,-5.155724,8.682107,8.680263,-2.351628,8.957867,5.679495,3.935431,-1.307507,-8.917291,8.395416,5.460527,8.414378,5.488504,-3.098085,7.111292,1.478881,-8.541548,5.195065,-3.753215,6.532130,-6.978631,4.571656,6.723962,-6.218145,2.855041,1.761068,5.423323,5.021675,4.826896,8.102900,1.853361,9.861385,7.696027,2.769395,-3.334906,3.722096,4.460438,-4.648455,8.291594,-8.879523,-1.165138,7.928504,-1.119628,-2.528673,-8.737261,-5.205529,-4.722562,3.626878,-8.026949,-1.007136,5.350712,6.238814,-7.215790,-4.113547,1.784860,-5.964749,-0.115676,7.742946,-9.285114,6.961924,7.486820,-7.744783,2.723514,0.532472,0.758739,-2.226333,-2.964139,7.797046,0.686571,-1.559520,3.774498,-2.183562,-7.461845,-4.802033,8.112679,3.917791,-3.312596,-3.383389,8.016579,9.454878,2.289660,-9.082432,-1.520008,-1.714320,1.139184,-7.333810,2.814575,-3.402147,-4.390613,7.412496,-2.677905,-0.645370,-1.074831,-5.504562,-7.779414,-6.850329,8.166306,6.751145,1.161864,1.242419,-6.502241,5.256310,-0.643146,4.798348,-7.465221,-2.120787,0.659725,8.586712,-8.629644,-6.873089,-4.770479,-8.649209,6.098965,8.755519,-1.320853,6.499996,-6.365851,-7.453758,-1.772924,0.627316,-8.607965,-9.525188,-9.960984,-3.526625,9.106950,5.504223,3.822527,-5.235559,-1.507543,4.000239,-1.699038,8.377424,6.050117,-9.370301,-0.468377,5.014764,8.365584,-4.221030,2.007432,-3.601993,9.907731,-4.341919,-8.767527,6.596344,-0.956592,8.945279,9.394636,9.446246,-2.221077,2.655493,5.279923,-1.931779,-1.225759,-6.270705,6.157574,-1.021314,5.834135,6.866502,9.754773,-1.244898,-2.881231,1.990929,-2.557458,-1.679847,-2.808793,5.180275,-5.200203,-0.123060,9.001474,9.946795,-4.380411,8.793339,-4.107706,0.406681,-1.271948,-2.798312,5.230402,-7.922544,-7.944727,-9.820764,-6.983490,0.693669,4.161761,1.321379,-9.658472,7.224305,3.517603,-4.324309,-7.519871,7.519497,9.794187,8.588678,8.723592,1.394133,-6.117931,-0.084856,6.854165,-1.777825,-8.560484,7.137983,-9.908409,1.995703,-2.823490,7.769762,8.496492,8.698313,-5.457076,3.694677,-0.264257,-5.342478,-1.843172,-1.389539,-9.460785,7.332374,-2.034641,3.983926,4.006377,-0.819428,8.361271,-8.770983,2.755856,2.984395,-8.607671,4.868640,5.676503,-9.585853,5.446947,-9.066635,1.965227,-1.054060,-5.129153,-9.837985,-7.127642,8.591978,-0.215384,-7.297559,9.224009,-2.836878,-1.168342,1.326994,2.449134,9.277444,-7.950821,-6.084493,4.124258,8.350274,-9.643375,-4.296124,7.590001,-6.963884,8.092771,5.300313,0.799798,0.663021,3.705170,1.404073,-3.587371,0.247221,-9.766738,-1.008399,-8.436143,-6.155875,0.340314,9.561927,-7.210872,-2.489377,-8.903748,1.216920,2.836682,9.817654,6.012227,8.609750,-7.321277,-7.353566,-7.410515,-3.319707,-0.726516,-7.345453,8.064767,-9.396799,1.050218,-5.451804,-0.434672,1.316865,-8.249377,6.672370,-0.321150,4.176398,2.611127,6.394455,-9.927136,9.734313,-3.735720,-3.302462,7.714691,-4.828730,6.011161,2.899074,-6.484008,-2.661041,4.744951,-3.563573,-7.542073,-4.235350,0.905868,-8.943064,-1.224011,-8.805853,9.701438,-3.788638,-7.105250,1.894876,5.806745,8.466138,-6.121296,-3.517382,2.909011,7.028533,-7.109606,-0.184698,5.737109,9.004083,-0.154519,0.545900,-0.934752,-6.396962,-5.478833,4.149690,-5.832969,1.072145,-3.250891,1.298565,-4.457947,1.965554,-0.857152,-7.862577,-7.179047,2.390072,6.585753,-1.517247,4.799337,-0.803688,9.122444,2.551783,7.750252,-1.099273,1.377565,9.869724,-7.820524,-7.853691,-1.575763,-2.680187,9.713569,4.189764,-4.660238,-0.128005,8.502039,7.843680,-4.878828,-8.759250,7.363650,8.356669,-8.792485,-2.556602,-3.505577,-1.716569,9.939244,1.782083,-2.924511,-4.195246,6.110092,-3.806178,8.440253,6.928083,7.163687,6.857399,-1.727272,5.563550,-4.477742,7.664314,-1.812757,9.432767,-2.086243,-9.100528,-2.082015,-4.552956,-6.400108,-8.382009,-7.108575,9.753161,0.740995,2.840415,-5.943682,8.379695,-9.522956,7.200435,-0.030253,4.074607,0.295467,5.751023,-1.448987,9.173990,6.327559,-7.110583,8.282880,1.996923,1.385038,-1.832184,1.633246,-1.085138,-6.036595,-5.253145,-0.623920,-8.340688,-3.518685,2.557823,2.507758,3.853303,-3.942685,-8.166148,6.073889,5.510579,-2.375830,-7.409507,7.321747,-8.056158,-6.801322,-9.990466,-1.120610,7.097715,-8.329111,7.194833,3.588779,-1.751328,-8.286147,-9.932791,-6.393535,-8.613101,8.201546,-9.392238,6.960613,0.557086,-3.859061,4.514950,-8.068679,6.634313,2.839412,-5.474056,7.951135,2.569588,5.019916,2.783271,5.198206,1.473205,4.035719,3.682953,-5.624910,-4.082844,-9.803932,3.059983,-2.081770,1.198964,6.705337,0.985324,8.064621,-4.402574,-5.210348,-1.816384,-5.080104,-3.917629,-2.042511,-7.167926,-7.702687,3.348146,-7.264228,8.349934,3.710715,2.043800,-9.225546,0.864358,6.842766,3.634097,0.669804,9.798080,0.372879,1.107017,5.675910,-4.756428,8.549786,-4.391426,-0.452495,-4.253352,-4.446177,-3.264720,-3.525635,-4.234171,7.539972,6.104759,-1.374551,-0.709252,9.397735,5.153804,-9.642950,-4.420885,9.584154,4.276707,5.309923,3.269623,6.800298,-8.040266,6.700568,2.653752,-4.500864,5.765109,1.615921,-0.874695,-2.167262,4.141842,8.960399,-3.142311,-8.801074,-7.322601,8.802217,-6.160779,5.661577,8.460086,4.952157,-9.149853,6.661596,-0.035439,9.788118,9.377771,-4.914806,-8.840425,3.647947,-4.816069,1.178104,0.971805,-8.888870,6.895925,-7.816127,-7.287225,-5.245727,-4.786008,3.135056,-0.649450,4.336680,-4.473190,5.987415,-4.113594,5.601012,-3.175290,9.375012,1.062748,7.942308,-6.505793,2.702209,-8.119735,2.586976,-2.813924,6.579731,5.509054,-2.418595,7.861656,6.325324,-0.307108,-1.296266,0.664001,-2.661358,-7.644509,2.233234,-0.355410,1.815116,-4.672683,5.035869,1.210019,-7.289138,4.646204,-6.300128,-2.832868,-1.074010,-2.728299,9.690981,5.438349,2.908938,-9.433810,-6.030668,6.419670,4.731935,-0.106999,-5.465851,3.158574,-0.641557,-8.782061,4.966868,-2.382669,4.569564,8.452619,-2.229308,2.323160,-9.083192,6.346519,-8.165491,-4.128232,-0.366993,-9.369952,8.848559,5.073485,-4.084549,-7.472226,-4.322872,-1.321182,-9.685924,5.559518,-0.400846,-8.126666,-7.890561,8.297679,-2.914731,-1.299894,-6.239871,-6.126105,-6.270779,5.995622,0.546185,8.799129,4.067714,7.656541,8.156194,-6.604174,1.665939,-3.410040,-5.989896,-4.829599,3.555954,-2.130785,0.533634,5.334062,-3.031622,5.775920,2.121942,-0.004399,-8.304807,-2.024255,-6.711036,8.232022,3.158628,8.507679,9.680881,-5.268188,-5.516076,-9.661184,4.522481,7.792910,-9.291160,5.066370,5.930540,-7.169129,-1.627441,8.962193,-9.395139,-3.494039,-2.985718,9.383576,-3.652755,0.315028,-7.412247,-9.037900,5.971798,-8.745820,-3.478485,7.799658,0.254062,0.521534,-0.472548,-3.750521,7.356605,-4.405700,-1.108916,0.712971,-7.952855,0.728064,-1.293317,-5.496062,1.168035,-8.613031,6.987695,-0.573007,5.857843,-1.421435,-6.960557,-7.882496,6.921772,-4.216723,4.271854,-4.766483,-4.919191,-8.820892,-3.321207,-4.912461,9.971079,1.596244,0.171576,4.182343,-7.283300,-5.933703,-5.384727,-6.288327,-8.491338,7.008269,7.765528,0.357542,2.774990,-2.830006,-7.907800,-9.819404,5.083806,-2.960188,4.818375,-2.829753,3.391796,-5.568374,8.814492,-0.288499,7.899835,4.067105,3.685544,-8.701926,6.464743,-1.133290,-1.943361,6.860970,2.586947,-0.837942,-8.678459,-4.489140,5.321576,5.231546,2.292989,-6.824376,-5.258541,9.968631,-0.769486,-2.205300,8.358886,-3.364433,7.284609,5.363934,6.741478,0.455294,-9.289810,-6.786398,7.631612,0.595337,5.299570,6.722706,5.682959,8.215429,2.941371,9.180369,5.483470,-8.287696,-5.571872,5.298668,9.477401,3.833296,-3.924983,2.265121,2.326473,-3.127562,9.571820,-9.045878,1.611371,-5.464122,-5.650180,5.267919,6.598919,-0.619019,0.218904,-5.848814,3.253965,5.604048,6.310546,3.953492,2.538899,4.132889,4.173744,4.825555,8.858288,8.212461,-8.070787,5.828292,-9.425645,0.609471,5.273444,-3.361953,9.858759,-9.670436,4.786123,5.253357,-0.894375,9.977346,7.181273,-9.310659,-6.107973,-3.769075,-7.977911,4.351886,9.395057,-3.511751,-2.972114,5.367199,-2.408085,-8.437515,3.985098,-5.232299,-6.214866,-1.824802,0.683318,-2.486002,-1.574732,-5.833215,9.768410,-6.614880,-5.706638,8.598804,6.710043,-5.084867,5.447920,9.175349,-3.769645,-0.883457,2.456869,-9.617789,4.369724,3.192816,8.306555,-4.802774,7.946226,-2.273182,8.243618,-9.154340,-1.666682,0.040712,5.653324,8.821994,-5.538020,-6.380501,-6.735849,-5.197721,0.938871,6.786222,0.961186,9.061218,-4.208664,-3.478581,-6.929519,8.446153,5.593491,-4.462370,2.595384,8.942403,6.643164,-8.868460,-8.162375,0.432629,-5.987711,8.058761,-9.132212,-8.741900,-0.271734,-0.796217,2.406568,9.200133,-5.460349,1.820280,1.062410,-8.759762,-2.632156,-6.883978,1.427108,-0.703306,4.751698,-2.925220,2.825584,-2.788571,2.926864,-9.368352,-0.725439,-9.050044,6.150636,7.439845,-6.026698,5.063221,-6.607420,7.950802,0.519612,0.716106,2.689000,-2.794851,-1.170305,-0.405060,7.187445,-2.977392,5.168684,9.211309,-5.585091,3.028214,-3.616852,4.653294,1.731277,-6.357440,-1.624157,0.991838,8.945601,-4.664954,-0.149844,-8.137181,0.177747,-2.788608,8.826488,8.925601,-2.492406,-9.596005,0.589235,2.816218,-7.747175,8.839592,9.691472,6.682143,-0.348709,-3.354181,-9.617364,5.680262,3.479930,-8.916399,8.576415,-2.362491,1.356208,-0.491437,-7.176915,8.145027,2.106146,0.438604,7.521347,-1.793285,4.600166,-7.792370,1.050301,8.055224,5.497887,2.740021,-3.079488,-9.595864,-3.890923,-3.539575,-3.592066,4.439061,3.246558,-6.989867,3.727252,-7.613655,2.601578,5.841498,-6.999888,1.586404,-8.026478,-9.705556,-7.816614,-1.552562,9.150176,7.532236,-5.087629,-3.904045,-1.154001,-1.450781,4.118701,-8.202063,-9.097240,0.064395,-8.080137,-1.177726,4.635908,2.145210,-3.817949,-4.316978,9.678112,6.040365,-1.958281,9.913396,0.503334,4.723099,-9.454167,8.606504,9.282594,-2.980126,-2.421322,-8.996946,9.650125,6.756511,-7.698339,-8.854686,-1.410390,9.549925,8.406068,3.540834,9.859874,4.846974,-3.339087,-1.190042,5.467046,9.087539,4.534206,4.991436,-8.071508,-8.671460,-9.364920,-8.007455,6.212658,2.827036,-4.762373,9.690466,4.625808,5.511015,4.145241,9.002281,-9.624937,-8.880025,4.135264,9.811682,0.466996,-2.275156,-2.920880,-5.784586,-9.780912,-0.728149,-8.821729,-8.744977,-6.555441,0.948570,4.666462,-4.010899,0.960194,-5.292332,-2.184161,-9.452383,8.378328,3.701165,6.034109,8.974288,8.551582,-9.161057,3.572501,-2.859675,9.688136,-5.512844,-4.446400,-0.787281,7.782353,-9.349851,-5.161022,5.784611,8.051475,7.033166,-7.511482,5.403276,-4.654743,8.215570,-1.899878,7.067772,9.429444,6.993924,-7.933007,-1.654364,-7.056078,4.736237,9.933845,-1.413170,1.382285,-3.471583,5.177169,-2.441391,7.158497,4.863576,4.690873,8.089012,-5.050038,-2.856729,9.197903,1.008869,-7.810817,-1.180568,4.231622,-0.570476,4.353650,9.142835,-7.798027,-3.723411,0.898462,-6.558939,6.945741,-8.467754,-9.791807,-5.301998,4.869653,3.837145,6.593984,2.641491,-4.286813,3.876126,-7.406208,-6.858829,-5.906900,8.488162,7.872928,-3.514312,1.747185,-0.547837,-0.148368,6.774570,-3.391317,4.670576,1.224183,9.870255,-7.938875,0.788364,6.920549,-6.331422,-3.588336,6.869932,6.715635,-5.768549,-1.405086], dtype = "float64")#candidate|13519|(1500,)|const|float64
var_13520 = relay.var("var_13520", dtype = "float32", shape = (168,))#candidate|13520|(168,)|var|float32
call_13518 = relay.TupleGetItem(func_10460_call(relay.reshape(const_13519.astype('float64'), [1500,]), relay.reshape(var_13520.astype('float32'), [168,]), ), 6)
call_13521 = relay.TupleGetItem(func_10464_call(relay.reshape(const_13519.astype('float64'), [1500,]), relay.reshape(var_13520.astype('float32'), [168,]), ), 6)
output = relay.Tuple([call_13502,call_13518,const_13519,var_13520,])
output2 = relay.Tuple([call_13503,call_13521,const_13519,var_13520,])
func_13523 = relay.Function([var_13520,], output)
mod['func_13523'] = func_13523
mod = relay.transform.InferType()(mod)
var_13524 = relay.var("var_13524", dtype = "float32", shape = (168,))#candidate|13524|(168,)|var|float32
output = func_13523(var_13524)
func_13525 = relay.Function([var_13524], output)
mutated_mod['func_13525'] = func_13525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11438_call = mod.get_global_var('func_11438')
func_11439_call = mutated_mod.get_global_var('func_11439')
call_13553 = relay.TupleGetItem(func_11438_call(), 0)
call_13554 = relay.TupleGetItem(func_11439_call(), 0)
func_6008_call = mod.get_global_var('func_6008')
func_6010_call = mutated_mod.get_global_var('func_6010')
const_13558 = relay.const([9,8,-6,2,4,-2,-7,5,-6,-10,1,8,-5,-6,-7,-7,-5,-4,-4,6,6,-1,2,10,2,-4,-8,-1,-5,-9,-9,1,-1,-2,3,-3,6,4,9,-8,6,4,-6,6,-3,6,-1,-4,3,-9,6,9,-3,1,-9,-3,-1,-8,3,8,6,7,-2,2,-9,-4,-1,6,-6,-10,-6,-1,-9,3,2,7,5,7,-5,3,-8,-8,9,-6,10,1,8,-4,10,10,-7,10,-1,7,8,9,-6,6,10,2,8,8,5,5,-9,5,-4,-8,-6,10,-7,-9,-5,-8,-8,4,4,-4,-6,-4,5,-9,-6,3,-3,3], dtype = "uint32")#candidate|13558|(126,)|const|uint32
call_13557 = relay.TupleGetItem(func_6008_call(relay.reshape(const_13558.astype('uint32'), [126, 1])), 2)
call_13559 = relay.TupleGetItem(func_6010_call(relay.reshape(const_13558.astype('uint32'), [126, 1])), 2)
bop_13564 = relay.bitwise_or(call_13557.astype('int8'), relay.reshape(const_13558.astype('int8'), relay.shape_of(call_13557))) # shape=(126, 1)
bop_13567 = relay.bitwise_or(call_13559.astype('int8'), relay.reshape(const_13558.astype('int8'), relay.shape_of(call_13559))) # shape=(126, 1)
func_7553_call = mod.get_global_var('func_7553')
func_7554_call = mutated_mod.get_global_var('func_7554')
call_13568 = func_7553_call()
call_13569 = func_7553_call()
func_10412_call = mod.get_global_var('func_10412')
func_10414_call = mutated_mod.get_global_var('func_10414')
call_13576 = relay.TupleGetItem(func_10412_call(), 1)
call_13577 = relay.TupleGetItem(func_10414_call(), 1)
func_6176_call = mod.get_global_var('func_6176')
func_6181_call = mutated_mod.get_global_var('func_6181')
var_13579 = relay.var("var_13579", dtype = "uint32", shape = ())#candidate|13579|()|var|uint32
const_13580 = relay.const([[3,-2,-6,-2,6,2],[-5,-8,3,9,-4,-4],[8,-10,7,-3,3,3],[-2,6,4,-3,-4,8],[-6,-7,-6,3,-4,-10],[4,-1,9,-4,-8,10],[-2,-1,-4,4,-3,-2],[-9,-5,-5,-5,-8,-6],[10,-9,-2,-8,-2,1],[-5,-7,5,1,4,10],[-1,-10,1,8,-6,10]], dtype = "uint32")#candidate|13580|(11, 6)|const|uint32
var_13581 = relay.var("var_13581", dtype = "int64", shape = (312,))#candidate|13581|(312,)|var|int64
call_13578 = relay.TupleGetItem(func_6176_call(relay.reshape(var_13579.astype('uint32'), []), relay.reshape(const_13580.astype('uint32'), [66,]), relay.reshape(var_13581.astype('int64'), [156, 2]), ), 4)
call_13582 = relay.TupleGetItem(func_6181_call(relay.reshape(var_13579.astype('uint32'), []), relay.reshape(const_13580.astype('uint32'), [66,]), relay.reshape(var_13581.astype('int64'), [156, 2]), ), 4)
output = relay.Tuple([call_13553,bop_13564,call_13568,call_13576,call_13578,var_13579,const_13580,var_13581,])
output2 = relay.Tuple([call_13554,bop_13567,call_13569,call_13577,call_13582,var_13579,const_13580,var_13581,])
func_13591 = relay.Function([var_13579,var_13581,], output)
mod['func_13591'] = func_13591
mod = relay.transform.InferType()(mod)
var_13592 = relay.var("var_13592", dtype = "uint32", shape = ())#candidate|13592|()|var|uint32
var_13593 = relay.var("var_13593", dtype = "int64", shape = (312,))#candidate|13593|(312,)|var|int64
output = func_13591(var_13592,var_13593,)
func_13594 = relay.Function([var_13592,var_13593,], output)
mutated_mod['func_13594'] = func_13594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9236_call = mod.get_global_var('func_9236')
func_9237_call = mutated_mod.get_global_var('func_9237')
call_13604 = func_9236_call()
call_13605 = func_9236_call()
func_12371_call = mod.get_global_var('func_12371')
func_12374_call = mutated_mod.get_global_var('func_12374')
const_13607 = relay.const([[-3.986776,-7.870408,0.926989,-7.138646,1.765657,8.130690],[-8.257880,0.636769,-2.310617,9.263902,4.884018,1.938644],[-2.784480,7.644450,7.415866,-6.471988,1.825415,8.750402],[8.878595,4.218133,5.098601,-3.253016,-1.560445,-1.188909],[3.261699,8.879404,7.671375,4.198750,8.674636,-6.792894],[0.649695,-5.870474,-7.647547,0.076655,-8.304803,-5.021235],[7.202414,6.167861,0.122752,-6.585735,8.283081,7.332901],[-2.297619,3.246577,-5.922976,-5.954409,-0.572874,-0.335210],[-8.181452,-6.346396,-9.526214,4.344780,2.728294,5.164378],[-0.353493,5.184624,8.968270,9.486738,-0.027101,1.670149],[-0.223138,-3.401214,5.705594,7.152068,-6.370288,-4.166157],[8.851991,-9.341250,-1.946787,6.329659,3.451164,7.081556],[9.468695,-2.886733,6.988053,-6.532661,-6.407638,-7.632509],[5.553509,3.406346,8.709166,-2.719217,9.811911,-8.553645],[7.463212,1.676049,-2.123175,8.175486,8.636904,3.014396],[-9.712878,-2.955718,-5.358147,-8.066616,2.707918,4.740850],[9.445809,3.534390,-1.132662,-1.098260,3.116377,-5.826515],[-3.643111,4.363340,-3.930632,-2.442810,2.104190,4.728002],[1.650584,1.880925,7.195821,-8.695998,0.615653,-1.142287],[1.622991,2.489225,-2.580233,-6.696170,5.266667,-9.696338],[5.081763,-8.498766,9.776923,-5.049097,3.390741,0.133953],[6.058787,7.650706,9.307300,-2.105298,2.317439,9.237784],[-8.470513,-0.786581,-7.732010,4.799773,-6.484547,-1.762228],[3.389297,-7.830454,-6.314801,2.636877,5.017679,-9.276361],[-4.803745,5.781485,-6.095273,0.393605,1.758295,1.720849]], dtype = "float64")#candidate|13607|(25, 6)|const|float64
var_13608 = relay.var("var_13608", dtype = "float64", shape = (1500,))#candidate|13608|(1500,)|var|float64
call_13606 = relay.TupleGetItem(func_12371_call(relay.reshape(const_13607.astype('float64'), [150, 1]), relay.reshape(var_13608.astype('float64'), [750, 2]), ), 6)
call_13609 = relay.TupleGetItem(func_12374_call(relay.reshape(const_13607.astype('float64'), [150, 1]), relay.reshape(var_13608.astype('float64'), [750, 2]), ), 6)
func_7588_call = mod.get_global_var('func_7588')
func_7590_call = mutated_mod.get_global_var('func_7590')
call_13616 = func_7588_call()
call_13617 = func_7588_call()
output = relay.Tuple([call_13604,call_13606,const_13607,var_13608,call_13616,])
output2 = relay.Tuple([call_13605,call_13609,const_13607,var_13608,call_13617,])
func_13619 = relay.Function([var_13608,], output)
mod['func_13619'] = func_13619
mod = relay.transform.InferType()(mod)
mutated_mod['func_13619'] = func_13619
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13620 = relay.var("var_13620", dtype = "float64", shape = (1500,))#candidate|13620|(1500,)|var|float64
func_13619_call = mutated_mod.get_global_var('func_13619')
call_13621 = func_13619_call(var_13620)
output = call_13621
func_13622 = relay.Function([var_13620], output)
mutated_mod['func_13622'] = func_13622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11156_call = mod.get_global_var('func_11156')
func_11157_call = mutated_mod.get_global_var('func_11157')
call_13643 = func_11156_call()
call_13644 = func_11156_call()
func_4718_call = mod.get_global_var('func_4718')
func_4720_call = mutated_mod.get_global_var('func_4720')
var_13646 = relay.var("var_13646", dtype = "float32", shape = (60, 2))#candidate|13646|(60, 2)|var|float32
call_13645 = relay.TupleGetItem(func_4718_call(relay.reshape(var_13646.astype('float32'), [8, 1, 15])), 0)
call_13647 = relay.TupleGetItem(func_4720_call(relay.reshape(var_13646.astype('float32'), [8, 1, 15])), 0)
func_10292_call = mod.get_global_var('func_10292')
func_10293_call = mutated_mod.get_global_var('func_10293')
call_13648 = relay.TupleGetItem(func_10292_call(), 0)
call_13649 = relay.TupleGetItem(func_10293_call(), 0)
output = relay.Tuple([call_13643,call_13645,var_13646,call_13648,])
output2 = relay.Tuple([call_13644,call_13647,var_13646,call_13649,])
func_13653 = relay.Function([var_13646,], output)
mod['func_13653'] = func_13653
mod = relay.transform.InferType()(mod)
var_13654 = relay.var("var_13654", dtype = "float32", shape = (60, 2))#candidate|13654|(60, 2)|var|float32
output = func_13653(var_13654)
func_13655 = relay.Function([var_13654], output)
mutated_mod['func_13655'] = func_13655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11156_call = mod.get_global_var('func_11156')
func_11157_call = mutated_mod.get_global_var('func_11157')
call_13669 = func_11156_call()
call_13670 = func_11156_call()
func_1272_call = mod.get_global_var('func_1272')
func_1275_call = mutated_mod.get_global_var('func_1275')
var_13684 = relay.var("var_13684", dtype = "uint8", shape = (11, 15))#candidate|13684|(11, 15)|var|uint8
call_13683 = func_1272_call(relay.reshape(var_13684.astype('uint8'), [15, 11, 1]))
call_13685 = func_1272_call(relay.reshape(var_13684.astype('uint8'), [15, 11, 1]))
output = relay.Tuple([call_13669,call_13683,var_13684,])
output2 = relay.Tuple([call_13670,call_13685,var_13684,])
func_13686 = relay.Function([var_13684,], output)
mod['func_13686'] = func_13686
mod = relay.transform.InferType()(mod)
mutated_mod['func_13686'] = func_13686
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13687 = relay.var("var_13687", dtype = "uint8", shape = (11, 15))#candidate|13687|(11, 15)|var|uint8
func_13686_call = mutated_mod.get_global_var('func_13686')
call_13688 = func_13686_call(var_13687)
output = call_13688
func_13689 = relay.Function([var_13687], output)
mutated_mod['func_13689'] = func_13689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12671_call = mod.get_global_var('func_12671')
func_12673_call = mutated_mod.get_global_var('func_12673')
call_13694 = relay.TupleGetItem(func_12671_call(), 0)
call_13695 = relay.TupleGetItem(func_12673_call(), 0)
output = relay.Tuple([call_13694,])
output2 = relay.Tuple([call_13695,])
func_13711 = relay.Function([], output)
mod['func_13711'] = func_13711
mod = relay.transform.InferType()(mod)
mutated_mod['func_13711'] = func_13711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13711_call = mutated_mod.get_global_var('func_13711')
call_13712 = func_13711_call()
output = call_13712
func_13713 = relay.Function([], output)
mutated_mod['func_13713'] = func_13713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11869_call = mod.get_global_var('func_11869')
func_11871_call = mutated_mod.get_global_var('func_11871')
call_13739 = func_11869_call()
call_13740 = func_11869_call()
output = call_13739
output2 = call_13740
func_13741 = relay.Function([], output)
mod['func_13741'] = func_13741
mod = relay.transform.InferType()(mod)
mutated_mod['func_13741'] = func_13741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13741_call = mutated_mod.get_global_var('func_13741')
call_13742 = func_13741_call()
output = call_13742
func_13743 = relay.Function([], output)
mutated_mod['func_13743'] = func_13743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8942_call = mod.get_global_var('func_8942')
func_8943_call = mutated_mod.get_global_var('func_8943')
call_13765 = relay.TupleGetItem(func_8942_call(), 0)
call_13766 = relay.TupleGetItem(func_8943_call(), 0)
output = call_13765
output2 = call_13766
func_13782 = relay.Function([], output)
mod['func_13782'] = func_13782
mod = relay.transform.InferType()(mod)
mutated_mod['func_13782'] = func_13782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13782_call = mutated_mod.get_global_var('func_13782')
call_13783 = func_13782_call()
output = call_13783
func_13784 = relay.Function([], output)
mutated_mod['func_13784'] = func_13784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mod.get_global_var('func_7037')
func_7039_call = mutated_mod.get_global_var('func_7039')
call_13819 = relay.TupleGetItem(func_7037_call(), 0)
call_13820 = relay.TupleGetItem(func_7039_call(), 0)
output = relay.Tuple([call_13819,])
output2 = relay.Tuple([call_13820,])
func_13827 = relay.Function([], output)
mod['func_13827'] = func_13827
mod = relay.transform.InferType()(mod)
mutated_mod['func_13827'] = func_13827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13827_call = mutated_mod.get_global_var('func_13827')
call_13828 = func_13827_call()
output = call_13828
func_13829 = relay.Function([], output)
mutated_mod['func_13829'] = func_13829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9677_call = mod.get_global_var('func_9677')
func_9679_call = mutated_mod.get_global_var('func_9679')
call_13903 = relay.TupleGetItem(func_9677_call(), 1)
call_13904 = relay.TupleGetItem(func_9679_call(), 1)
func_12371_call = mod.get_global_var('func_12371')
func_12374_call = mutated_mod.get_global_var('func_12374')
var_13914 = relay.var("var_13914", dtype = "float64", shape = (150,))#candidate|13914|(150,)|var|float64
const_13915 = relay.const([-7.304308,2.153982,6.432074,1.649912,9.282717,7.233142,-1.034742,-2.022677,8.114367,6.568798,-8.706831,5.929158,-6.975491,-6.449819,2.450127,-9.788345,-5.845616,-3.810339,6.881279,3.180673,-8.581582,3.045709,-6.243175,-9.171001,7.557905,-8.708205,9.931502,-6.374081,7.708716,8.812340,5.401173,3.668810,1.638218,1.508678,0.083593,1.605648,1.127832,-6.951491,1.505477,7.283793,-7.078294,-2.332090,0.067453,-4.907711,6.126842,3.792795,4.401416,-2.570606,-9.483488,9.466276,-4.134340,9.020752,8.417097,-6.547048,-5.125316,-5.061752,6.372191,-4.032283,0.213632,4.525751,-7.238432,7.187988,5.336089,5.872548,1.231802,-4.041386,0.018553,2.590170,7.102096,9.269810,-9.538643,8.173974,-9.467819,-4.042580,-7.776895,-2.964722,6.796161,-3.077423,3.365449,-2.794011,-3.885978,2.067536,5.455760,2.247299,-2.838033,-2.842783,-4.436456,-8.263860,-2.261627,-9.871114,-7.248916,3.614862,5.659802,8.683764,3.022695,6.086713,-1.643422,-4.611513,-0.591329,-7.070765,-7.894738,0.237551,-0.044775,-7.411476,-4.756335,0.966303,2.745391,-2.660783,-6.107556,-5.587820,-3.703486,-3.250236,-5.429118,-1.093493,-2.701548,4.741253,8.182350,1.250058,-5.223376,-6.950589,-1.823713,8.948704,7.972002,-9.854351,7.283547,6.275667,3.272048,-0.966479,-0.995718,-5.140512,-9.177252,-5.371265,-5.092979,1.623598,1.896082,8.967406,-3.898432,4.386955,9.263156,1.578491,-9.428313,-0.591245,-8.404164,8.205909,9.792354,2.289301,5.156713,6.395057,6.851028,-1.738305,3.157197,6.264126,2.694663,0.125547,-0.701534,2.042669,3.532295,-2.196337,5.796070,1.438673,4.102973,-1.756378,-7.516455,-3.192688,-3.798460,-1.031926,6.889920,6.446857,-6.308297,6.784976,-4.090465,-8.877902,-3.595917,9.852441,-0.482437,-8.170806,-5.850129,5.680685,-5.887541,-9.493399,-9.530876,-8.379186,-1.148177,-3.993307,-4.630510,-0.655727,0.178811,7.323625,8.163701,5.023558,3.609587,-0.573061,-6.696179,-9.735159,5.539928,0.720389,9.588359,2.362021,-7.603736,-1.382788,5.585045,4.091244,7.231565,-3.386816,4.879981,0.321939,1.038268,-3.840474,5.684444,1.882922,-1.858465,-0.890810,-0.637086,2.943196,-0.502728,-1.721624,-1.339397,-1.024288,-0.105036,9.476725,-3.980327,-4.405487,-1.353264,0.125679,3.599221,-1.604900,7.316305,3.591573,2.679008,-0.903162,-1.701505,1.246675,-0.562143,7.032398,3.101860,6.389303,4.553761,6.114209,-5.498232,1.641991,1.927962,2.889139,-5.308502,6.851881,-7.581329,7.488495,-4.224523,9.718114,-5.268557,6.130299,3.235204,6.721220,-6.028379,-1.939800,2.096871,-6.037341,-5.668817,-9.071096,-0.857063,-3.753305,8.322408,7.275887,-7.106074,9.025782,8.039742,-5.776946,5.483617,3.649519,2.734072,-1.041018,9.435738,8.855944,7.479140,1.350329,5.148551,-5.492814,4.081726,-5.079171,-7.238773,9.535257,-2.677187,5.719270,1.427099,3.287756,-7.790197,-8.644388,-6.877768,7.085241,7.737452,4.692795,-0.655997,2.456582,-6.224636,-4.205033,8.516305,-9.284583,5.585184,5.858593,5.505906,7.379637,9.956341,9.510031,-9.581063,1.761066,7.933954,-9.592769,-9.980073,-9.956300,-6.676030,9.449643,-1.494575,4.509712,8.861255,-1.278369,-5.523452,5.729703,0.109675,3.922483,3.993047,1.548475,-1.187551,2.449619,-2.156148,6.021685,-1.497274,-6.068527,-9.287675,-2.134559,0.500276,-6.903621,5.891967,5.328332,0.489134,-4.787905,3.998911,2.391435,0.529836,-5.382384,-3.964766,-1.490601,-1.715313,5.942761,1.292493,0.354836,6.717393,-8.053888,2.359161,7.217610,-4.777261,6.571578,-4.867380,9.237622,7.882849,6.831620,6.019549,-1.908559,-6.714713,5.735924,-9.486033,-9.771151,-7.419329,-1.003917,-4.656524,-3.494546,0.540838,-3.357875,4.845270,9.796726,6.807599,-8.210817,3.175426,5.797751,9.867209,9.510014,9.249594,7.107839,-4.282334,8.348380,7.808592,3.148281,4.282138,-0.103272,-7.444888,-4.876880,-8.728975,-1.301368,6.477532,-0.466244,-7.079064,-6.981535,5.351913,-1.851880,7.420378,6.965794,5.480042,4.033625,-9.446118,3.718422,-2.487870,6.746869,1.767199,-4.660679,0.123846,1.264680,-1.830697,0.943566,5.749313,2.653254,7.381806,5.931987,2.048190,0.057452,3.167450,-3.784223,-9.291778,-7.454977,-5.694670,9.294892,5.904934,9.279276,-0.572147,-9.208250,-5.772175,2.915808,-6.277895,2.311577,7.925505,7.883750,2.889710,-8.037273,4.696734,4.456027,8.769622,1.603139,8.657905,-8.366408,6.733917,3.030257,-9.431410,9.137389,-1.221781,2.671947,-8.684119,-0.123240,-1.112440,2.790822,5.066598,3.296132,6.093379,-0.608755,-5.905690,6.096898,8.548222,8.562185,8.622447,-8.679136,0.966518,3.098648,-7.913145,-1.406005,5.008940,3.765773,-0.435238,2.185593,8.961995,8.895088,7.872084,-2.104752,1.243539,-2.537145,-1.650147,-0.817898,-4.318455,9.559865,5.133414,-2.337350,-8.104814,-7.507677,-8.498614,-2.645319,1.570727,8.913625,-7.551495,0.357946,-9.482670,-7.453290,-3.976930,-7.657445,5.091394,4.425889,0.651065,6.334925,9.095316,1.656479,8.898546,-0.887924,6.908595,9.838822,9.553814,4.514145,0.704298,-0.784872,5.166078,-2.200913,0.192587,0.837064,3.874114,-1.484673,-9.993786,3.532530,4.829061,-3.212959,0.458352,6.385478,-0.606389,-8.088652,-3.946939,9.953431,-9.492920,-4.625161,-6.365530,-7.029459,-7.307905,-1.201975,-0.175335,2.373220,6.567072,-9.158190,3.394263,6.918780,6.387967,8.290582,0.793232,3.723267,3.976486,6.468058,5.201906,8.096666,-1.894637,9.437061,5.167907,-7.537234,-8.864686,-4.584005,-3.070524,-6.429832,0.805762,-9.763250,-9.108813,-2.065324,0.231005,4.427692,-6.126654,6.457678,3.188218,2.589710,5.904508,6.520571,0.014101,6.730866,-8.670365,9.575610,-9.240436,-5.343745,7.918649,-9.305201,-1.233153,6.889850,-1.894425,0.366322,9.986316,7.486946,-0.908811,1.943996,-7.126111,-4.953300,-4.167393,-7.621207,6.899201,7.862234,-8.437374,4.879708,-7.423568,2.794405,8.646200,-6.488930,7.702319,8.519127,-5.900617,1.575875,-3.692266,4.388608,3.193009,2.535564,-9.909753,2.447423,-2.237613,4.007671,-6.339268,9.350087,1.219727,-5.383491,0.875170,9.703579,-8.922990,-1.857942,-5.281538,6.584023,-8.457971,-3.808654,-2.111860,7.812403,-3.267820,0.380041,1.843743,6.680613,-0.611700,0.819909,6.358894,3.898403,-3.412586,-4.554004,-2.764366,-6.401205,-3.470975,7.838877,1.179910,4.873926,-2.642841,-9.898290,-7.390568,-5.276053,4.444257,-1.988673,-1.765747,5.027372,-6.919967,1.886849,9.701125,1.472740,-9.994164,-6.784813,0.545235,-7.670927,-8.063242,4.337840,-2.079345,1.541153,9.783057,-5.789094,-4.992396,-2.267100,-0.801539,1.442435,-1.130237,3.178934,9.509014,-1.698282,-8.852470,-1.557391,7.186958,2.113458,-5.994911,1.054390,-6.214716,9.867105,1.353541,7.123453,-8.910600,-4.300033,5.875254,3.068901,8.733290,0.648091,-5.048718,1.444669,5.030670,7.105376,5.446900,-2.146920,5.600277,-8.450686,2.161705,-1.862400,-0.449639,-2.353477,-0.333608,6.266017,3.151205,0.166159,-1.716571,9.556418,5.772525,5.889143,-8.460300,2.265107,-7.279506,-9.715717,9.264052,9.568878,2.960375,-1.150989,6.654573,-8.417998,-3.071113,4.015106,-1.198611,5.559685,1.499755,-6.886296,-4.914796,4.777798,-4.667057,-6.407442,-3.773869,7.894005,-9.336073,-3.062011,2.302002,-2.094779,-9.504451,2.759609,3.229620,5.525264,4.279141,-2.718698,8.211908,-2.001114,3.039134,0.841458,-5.322061,-2.781884,-9.481215,6.839244,4.748448,-2.064463,7.516688,-1.844742,-2.871290,1.879003,1.466990,0.107920,-3.193330,-5.295267,-8.676910,5.874857,6.085669,3.321232,-7.571175,8.346470,8.691892,-3.159353,4.375067,9.945714,-6.062302,-8.185484,-6.745931,-5.890687,4.653686,-2.123320,-6.134628,6.440813,6.828956,-1.701619,2.373962,0.926390,7.382114,6.349327,-7.290477,-4.208270,0.177852,4.552368,-9.566498,-9.926956,-5.058994,1.941320,0.730052,-2.869733,-4.940939,-5.599218,1.658147,-3.712354,8.201887,3.304308,-6.845764,-4.498127,-0.771727,3.974911,6.556722,7.261160,-9.010961,2.040242,1.095261,8.821545,-8.295828,5.277379,6.038413,-3.377309,3.496503,5.972404,7.626528,9.752217,3.614370,-0.641373,5.388417,-0.877521,-1.879847,1.618656,-2.500288,0.519239,-4.788467,-2.300339,-2.958575,5.436160,-3.292687,9.848012,-0.627432,-2.103420,3.671819,7.724602,-8.574280,3.341548,0.274801,-2.125763,5.585314,-5.193167,-3.137308,0.811691,3.554630,-6.797783,8.057012,5.407874,-6.373562,7.875350,-7.077027,-3.417559,8.246787,5.764202,-4.492477,-6.884859,-6.469794,-7.065731,9.969327,9.184901,-3.033764,-5.604927,-2.801720,7.391230,4.520442,-4.599466,7.456571,-2.120730,-8.078420,6.199817,4.708094,-9.738150,-3.274217,-5.241863,5.084786,-2.953670,5.785560,2.959260,-5.906163,4.748190,-6.021367,8.762121,-9.019256,-4.074839,-7.278504,-5.798511,2.239211,9.415813,7.464344,7.529069,1.501423,-4.136463,-5.599747,-3.191547,-2.784622,0.407985,-6.775134,8.950624,-2.139663,9.186972,1.812109,1.765601,2.418546,2.225207,-5.943780,9.588502,-5.828698,8.958644,5.836860,-1.837398,6.126770,-3.027214,-1.280845,-8.157621,5.624794,5.872077,1.435556,6.634499,1.931151,7.691767,1.240619,-0.547026,-7.516883,6.938001,8.558265,-8.668436,1.276932,-0.366797,-5.294997,-3.435070,6.633843,-4.754852,-7.201446,1.460219,-3.745804,-5.928823,1.349810,-5.031700,-7.702453,5.343403,8.110441,-9.614425,7.036700,-4.964002,4.298110,9.147010,4.867918,-8.326632,-2.337382,4.204976,-1.858882,-9.673947,-7.075575,-0.749272,-8.732102,8.671432,2.249166,-8.293829,-0.955043,-8.419270,-3.991847,-5.253953,7.240966,2.693237,-9.346680,8.067609,-3.959449,-7.379057,-3.073821,2.107542,5.175262,-0.664740,-0.356992,6.736799,8.283272,2.451079,1.295521,2.569032,-5.478906,-9.725611,-8.167847,1.131217,-3.783556,2.077550,-8.564043,0.881747,7.830445,-8.220608,4.737679,0.786635,7.951446,-2.103963,-8.932937,-2.429843,-8.212230,-1.601488,-0.141607,-2.142092,8.411734,1.453138,-8.806064,0.540854,-7.955516,-6.686608,2.834798,-7.452377,-8.773556,-5.389133,5.184785,0.625208,4.104566,-3.610633,8.255200,-3.956073,-0.494748,0.119610,0.036469,8.956220,-9.847698,7.595415,6.544769,9.440195,-3.541390,-8.090936,-7.846835,4.562336,1.943627,6.718106,-3.505883,-0.030894,7.964358,-8.487252,-4.535581,-1.768665,9.774855,6.903980,3.091320,-2.359334,-2.396739,5.897170,-1.818287,-2.198431,-1.862040,-0.756051,-1.889438,-3.555524,-3.893882,-7.755619,-1.024052,-3.697702,-2.568036,-8.322861,-8.471914,5.471509,0.922978,9.987866,6.229421,-3.547509,9.904440,8.611959,9.621759,6.961527,-3.150278,-4.053114,-3.581469,-3.610017,-6.512890,-8.217780,7.576304,2.576298,7.876843,-2.514083,2.289557,-1.923895,5.217040,-6.042712,8.424630,2.767947,2.779775,-4.719173,-8.053549,-2.856309,8.646441,9.281452,-8.868380,-2.865289,6.570569,-3.880151,8.441449,8.725148,-5.894925,7.017910,6.625611,9.782841,-8.993215,-3.543995,-5.361322,-0.684349,0.711528,-7.313252,-0.973360,9.736768,1.275599,-0.070280,6.391188,-9.004806,6.591095,3.532461,-7.609119,6.704952,5.003418,3.560341,-3.911322,1.330917,3.657851,2.695834,-9.527744,1.723846,2.482860,-5.302540,4.705605,-7.093787,-7.304982,8.206116,6.907216,-5.798750,-0.167502,-9.039169,5.604800,-3.767099,-1.221033,-1.585519,2.363184,-4.764043,-3.109078,7.403589,9.394607,-2.128557,0.521985,-3.917800,1.700638,9.419834,-1.624959,-9.089471,-4.372505,-8.200909,0.349611,8.062047,-8.647362,3.190214,6.360487,-7.545350,-8.199230,-1.580071,-0.020848,-0.653267,1.849290,9.660337,-9.635924,1.601829,7.741795,0.358074,7.418625,3.841352,-6.524730,-2.350055,2.866376,5.475835,1.491436,9.208542,-5.866869,7.631749,-6.538377,-6.376917,1.350568,9.425768,0.241444,6.002254,4.110817,2.813228,0.756032,7.885805,-2.781025,-3.612973,0.525197,-8.754875,-3.910865,1.058310,-7.137008,1.814684,-5.410686,-6.251966,8.752985,-3.751704,-7.481837,-2.670750,5.995840,-3.454024,-5.256333,9.555717,9.904448,-4.747853,-9.497530,-7.061592,2.702414,-0.743915,-2.755515,1.252251,-8.805083,-8.137689,8.553156,-3.418577,2.378782,2.701817,5.036399,6.785372,-3.321567,-8.203786,9.978594,4.740550,-8.149093,-0.755885,0.179224,-5.132924,4.166428,-2.906757,-6.207179,4.243611,-8.249897,8.537191,-4.762098,-4.502828,-8.671164,2.383080,3.179720,-2.517373,-5.981813,-1.759526,0.621595,3.508999,7.744638,2.499697,-5.828385,3.741614,4.252264,-6.728781,4.745827,-6.696332,-9.271304,-1.700887,9.986369,1.292483,9.299884,9.045413,0.207734,-1.891365,-4.933135,-6.371009,-7.658427,4.305651,-4.076557,0.776414,-2.085275,-9.742021,7.191752,-9.562219,9.201887,-4.403309,0.114573,4.979768,-2.384369,-6.691926,-6.768911,0.321614,-5.488820,-5.847963,1.593649,6.528735,-6.527057,-8.808619,-9.008126,-3.692026,-0.325159,-5.052779,-9.857392,-7.432441,9.190661,6.213756,0.669283,8.047615,-3.545308,2.875058,0.391640,3.946872,-7.605749,-8.114595,1.243109,-0.005590,6.640194,7.197100,4.682531,5.002090,-8.445869,-1.459707,9.898012,-5.585058,4.344196,8.268523,-3.885768,-6.390470,-4.763069,7.277660,8.502551,-9.980037,-6.349042,-9.673096,7.869654,6.983512,6.871797,-3.373045,5.755695,-8.007022,-8.346169,9.032577,-9.111843,1.231223,-0.292959,-3.603263,-1.701538,7.575210,5.682094,-6.775665,2.490714,-2.673234,3.177264,9.209024,2.913337,-8.173752,-2.714216,-5.593756,1.454437,0.888036,-8.436544,-4.751146,-5.791823,-5.163440,5.727027,5.651778,-6.497897,9.387269,-3.207407,-9.260607,-4.161476,7.464258,-3.757887,-0.303101,4.706308,-9.325086,6.535797,-9.814579,-1.099143,1.459753,-7.614476,-8.647234,1.222619,-1.098572,-4.653209,7.505712,0.082433,5.676069,5.362736,-3.569639,-8.482881,-6.618490,6.199439,8.055297,7.386884,2.902303,0.596385,-5.720873,-0.745148,-6.457474,6.140071,4.300477,-6.015329,2.967108,-6.540547,-8.150699,-7.460647,7.471725,-0.211863,4.026684,9.370422,2.778335,-4.615021,1.040162,-3.559409,0.285432,-3.139455,5.365130,-5.280050,-7.737455,-5.588058,4.623932,0.243903,-1.400681,1.928090,-5.455530,-3.065179,-4.667226,2.587631,6.624541,6.248394,-7.254371,-7.457025,7.474906,-6.516641,2.536456,-9.399732,6.163356,7.314956,9.758136,0.381205,-3.855170,8.583935,-4.988640,-3.132730,1.707511,-4.726128,0.929755,0.120405,6.373488,-7.126057,-2.327676,5.276014,0.340414,8.246028,-0.279502,-4.552839,-8.741783,5.871815,-0.200426,7.901514,1.719930,9.410403,-3.720933,9.622092,-6.127667,-4.042591,0.181428,-9.861235,3.579322,5.347785,-9.769681,-3.306583,-0.577643,0.486104,4.588165,-0.852386,7.306042,-0.272017,-6.334786,0.989933,3.194580,9.345659,-4.801612,3.930288,6.458864,2.572837,-9.437427,-4.736108,6.158798,-1.746973,-3.132308,8.796317,-8.620802,5.182616,-2.899292,-6.838553,1.636822,-3.514968,3.156515,2.477737,-8.611377,0.435257,-6.305565,4.833710,8.116201,-3.480040,-7.835036,5.710614,9.115412,1.103086,-5.033801,-5.410404,7.219238,7.331994,-9.019523,7.368072,9.000130,-8.036312,1.285538,2.889640,9.640762,-3.330601,6.227278,-7.102462,5.950675,-2.299761,1.730434,0.942769,5.149191,-1.528101,9.934068,5.583819,-0.015738], dtype = "float64")#candidate|13915|(1500,)|const|float64
call_13913 = relay.TupleGetItem(func_12371_call(relay.reshape(var_13914.astype('float64'), [150, 1]), relay.reshape(const_13915.astype('float64'), [750, 2]), ), 5)
call_13916 = relay.TupleGetItem(func_12374_call(relay.reshape(var_13914.astype('float64'), [150, 1]), relay.reshape(const_13915.astype('float64'), [750, 2]), ), 5)
var_13930 = relay.var("var_13930", dtype = "float64", shape = (1500,))#candidate|13930|(1500,)|var|float64
bop_13931 = relay.floor_mod(const_13915.astype('float64'), relay.reshape(var_13930.astype('float64'), relay.shape_of(const_13915))) # shape=(1500,)
output = relay.Tuple([call_13903,call_13913,var_13914,bop_13931,])
output2 = relay.Tuple([call_13904,call_13916,var_13914,bop_13931,])
F = relay.Function([var_13914,var_13930,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_13914,var_13930,], output2)
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
