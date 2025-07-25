import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_565 = relay.var("var_565", dtype = "int64", shape = (14, 6, 6))#candidate|565|(14, 6, 6)|var|int64
var_566 = relay.var("var_566", dtype = "int64", shape = (14, 6, 6))#candidate|566|(14, 6, 6)|var|int64
bop_567 = relay.add(var_565.astype('int64'), relay.reshape(var_566.astype('int64'), relay.shape_of(var_565))) # shape=(14, 6, 6)
uop_571 = relay.log10(bop_567.astype('float32')) # shape=(14, 6, 6)
output = relay.Tuple([uop_571,])
output2 = relay.Tuple([uop_571,])
func_575 = relay.Function([var_565,var_566,], output)
mod['func_575'] = func_575
mod = relay.transform.InferType()(mod)
mutated_mod['func_575'] = func_575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mutated_mod.get_global_var('func_575')
var_577 = relay.var("var_577", dtype = "int64", shape = (14, 6, 6))#candidate|577|(14, 6, 6)|var|int64
var_578 = relay.var("var_578", dtype = "int64", shape = (14, 6, 6))#candidate|578|(14, 6, 6)|var|int64
call_576 = func_575_call(var_577,var_578,)
output = call_576
func_579 = relay.Function([var_577,var_578,], output)
mutated_mod['func_579'] = func_579
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1208 = relay.var("var_1208", dtype = "bool", shape = ())#candidate|1208|()|var|bool
var_1209 = relay.var("var_1209", dtype = "bool", shape = (4, 10, 14))#candidate|1209|(4, 10, 14)|var|bool
bop_1210 = relay.logical_and(var_1208.astype('bool'), var_1209.astype('bool')) # shape=(4, 10, 14)
func_575_call = mod.get_global_var('func_575')
func_579_call = mutated_mod.get_global_var('func_579')
var_1226 = relay.var("var_1226", dtype = "int64", shape = (504,))#candidate|1226|(504,)|var|int64
call_1225 = relay.TupleGetItem(func_575_call(relay.reshape(var_1226.astype('int64'), [14, 6, 6]), relay.reshape(var_1226.astype('int64'), [14, 6, 6]), ), 0)
call_1227 = relay.TupleGetItem(func_579_call(relay.reshape(var_1226.astype('int64'), [14, 6, 6]), relay.reshape(var_1226.astype('int64'), [14, 6, 6]), ), 0)
uop_1230 = relay.atan(bop_1210.astype('float32')) # shape=(4, 10, 14)
uop_1233 = relay.acosh(uop_1230.astype('float64')) # shape=(4, 10, 14)
output = relay.Tuple([call_1225,var_1226,uop_1233,])
output2 = relay.Tuple([call_1227,var_1226,uop_1233,])
func_1241 = relay.Function([var_1208,var_1209,var_1226,], output)
mod['func_1241'] = func_1241
mod = relay.transform.InferType()(mod)
mutated_mod['func_1241'] = func_1241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1241_call = mutated_mod.get_global_var('func_1241')
var_1243 = relay.var("var_1243", dtype = "bool", shape = ())#candidate|1243|()|var|bool
var_1244 = relay.var("var_1244", dtype = "bool", shape = (4, 10, 14))#candidate|1244|(4, 10, 14)|var|bool
var_1245 = relay.var("var_1245", dtype = "int64", shape = (504,))#candidate|1245|(504,)|var|int64
call_1242 = func_1241_call(var_1243,var_1244,var_1245,)
output = call_1242
func_1246 = relay.Function([var_1243,var_1244,var_1245,], output)
mutated_mod['func_1246'] = func_1246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1414 = relay.var("var_1414", dtype = "float64", shape = (1, 8, 11))#candidate|1414|(1, 8, 11)|var|float64
uop_1415 = relay.sinh(var_1414.astype('float64')) # shape=(1, 8, 11)
func_575_call = mod.get_global_var('func_575')
func_579_call = mutated_mod.get_global_var('func_579')
var_1418 = relay.var("var_1418", dtype = "int64", shape = (504,))#candidate|1418|(504,)|var|int64
call_1417 = relay.TupleGetItem(func_575_call(relay.reshape(var_1418.astype('int64'), [14, 6, 6]), relay.reshape(var_1418.astype('int64'), [14, 6, 6]), ), 0)
call_1419 = relay.TupleGetItem(func_579_call(relay.reshape(var_1418.astype('int64'), [14, 6, 6]), relay.reshape(var_1418.astype('int64'), [14, 6, 6]), ), 0)
output = relay.Tuple([uop_1415,call_1417,var_1418,])
output2 = relay.Tuple([uop_1415,call_1419,var_1418,])
func_1420 = relay.Function([var_1414,var_1418,], output)
mod['func_1420'] = func_1420
mod = relay.transform.InferType()(mod)
mutated_mod['func_1420'] = func_1420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1420_call = mutated_mod.get_global_var('func_1420')
var_1422 = relay.var("var_1422", dtype = "float64", shape = (1, 8, 11))#candidate|1422|(1, 8, 11)|var|float64
var_1423 = relay.var("var_1423", dtype = "int64", shape = (504,))#candidate|1423|(504,)|var|int64
call_1421 = func_1420_call(var_1422,var_1423,)
output = call_1421
func_1424 = relay.Function([var_1422,var_1423,], output)
mutated_mod['func_1424'] = func_1424
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1710 = relay.var("var_1710", dtype = "float32", shape = (9, 14, 9))#candidate|1710|(9, 14, 9)|var|float32
uop_1711 = relay.asin(var_1710.astype('float32')) # shape=(9, 14, 9)
bop_1713 = relay.logical_xor(var_1710.astype('uint64'), relay.reshape(uop_1711.astype('uint64'), relay.shape_of(var_1710))) # shape=(9, 14, 9)
output = relay.Tuple([bop_1713,])
output2 = relay.Tuple([bop_1713,])
func_1716 = relay.Function([var_1710,], output)
mod['func_1716'] = func_1716
mod = relay.transform.InferType()(mod)
var_1717 = relay.var("var_1717", dtype = "float32", shape = (9, 14, 9))#candidate|1717|(9, 14, 9)|var|float32
output = func_1716(var_1717)
func_1718 = relay.Function([var_1717], output)
mutated_mod['func_1718'] = func_1718
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2013 = relay.var("var_2013", dtype = "float32", shape = (10, 10, 14))#candidate|2013|(10, 10, 14)|var|float32
uop_2014 = relay.sqrt(var_2013.astype('float32')) # shape=(10, 10, 14)
output = uop_2014
output2 = uop_2014
func_2019 = relay.Function([var_2013,], output)
mod['func_2019'] = func_2019
mod = relay.transform.InferType()(mod)
mutated_mod['func_2019'] = func_2019
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2020 = relay.var("var_2020", dtype = "float32", shape = (10, 10, 14))#candidate|2020|(10, 10, 14)|var|float32
func_2019_call = mutated_mod.get_global_var('func_2019')
call_2021 = func_2019_call(var_2020)
output = call_2021
func_2022 = relay.Function([var_2020], output)
mutated_mod['func_2022'] = func_2022
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2094 = relay.var("var_2094", dtype = "uint16", shape = ())#candidate|2094|()|var|uint16
var_2095 = relay.var("var_2095", dtype = "uint16", shape = (6, 16, 12))#candidate|2095|(6, 16, 12)|var|uint16
bop_2096 = relay.minimum(var_2094.astype('uint16'), var_2095.astype('uint16')) # shape=(6, 16, 12)
func_575_call = mod.get_global_var('func_575')
func_579_call = mutated_mod.get_global_var('func_579')
var_2128 = relay.var("var_2128", dtype = "int64", shape = (504,))#candidate|2128|(504,)|var|int64
call_2127 = relay.TupleGetItem(func_575_call(relay.reshape(var_2128.astype('int64'), [14, 6, 6]), relay.reshape(var_2128.astype('int64'), [14, 6, 6]), ), 0)
call_2129 = relay.TupleGetItem(func_579_call(relay.reshape(var_2128.astype('int64'), [14, 6, 6]), relay.reshape(var_2128.astype('int64'), [14, 6, 6]), ), 0)
func_575_call = mod.get_global_var('func_575')
func_579_call = mutated_mod.get_global_var('func_579')
call_2130 = relay.TupleGetItem(func_575_call(relay.reshape(var_2128.astype('int64'), [14, 6, 6]), relay.reshape(call_2127.astype('int64'), [14, 6, 6]), ), 0)
call_2131 = relay.TupleGetItem(func_579_call(relay.reshape(var_2128.astype('int64'), [14, 6, 6]), relay.reshape(call_2127.astype('int64'), [14, 6, 6]), ), 0)
output = relay.Tuple([bop_2096,call_2127,var_2128,call_2130,])
output2 = relay.Tuple([bop_2096,call_2129,var_2128,call_2131,])
func_2135 = relay.Function([var_2094,var_2095,var_2128,], output)
mod['func_2135'] = func_2135
mod = relay.transform.InferType()(mod)
var_2136 = relay.var("var_2136", dtype = "uint16", shape = ())#candidate|2136|()|var|uint16
var_2137 = relay.var("var_2137", dtype = "uint16", shape = (6, 16, 12))#candidate|2137|(6, 16, 12)|var|uint16
var_2138 = relay.var("var_2138", dtype = "int64", shape = (504,))#candidate|2138|(504,)|var|int64
output = func_2135(var_2136,var_2137,var_2138,)
func_2139 = relay.Function([var_2136,var_2137,var_2138,], output)
mutated_mod['func_2139'] = func_2139
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2300 = relay.const(-2.488142, dtype = "float32")#candidate|2300|()|const|float32
const_2301 = relay.const([[[8.682132,6.530042,-9.849873,4.352392,4.183833]],[[-8.104074,-7.714047,-8.265452,-1.852409,5.325845]],[[-8.288441,-0.366169,-3.760033,-9.886835,-4.087866]],[[1.852914,-2.915820,9.014011,7.478476,-5.192641]],[[-6.900502,-3.654908,8.543565,5.876622,3.403124]],[[-0.448931,-4.833769,-8.246585,-3.815261,5.922733]],[[-3.862843,-1.338085,8.163025,3.982794,4.347494]],[[9.197380,-9.508428,-5.066318,5.503148,0.495556]]], dtype = "float32")#candidate|2301|(8, 1, 5)|const|float32
bop_2302 = relay.maximum(const_2300.astype('float32'), const_2301.astype('float32')) # shape=(8, 1, 5)
output = relay.Tuple([bop_2302,])
output2 = relay.Tuple([bop_2302,])
func_2305 = relay.Function([], output)
mod['func_2305'] = func_2305
mod = relay.transform.InferType()(mod)
mutated_mod['func_2305'] = func_2305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mutated_mod.get_global_var('func_2305')
call_2306 = func_2305_call()
output = call_2306
func_2307 = relay.Function([], output)
mutated_mod['func_2307'] = func_2307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2329 = relay.TupleGetItem(func_2305_call(), 0)
call_2330 = relay.TupleGetItem(func_2307_call(), 0)
output = relay.Tuple([call_2329,])
output2 = relay.Tuple([call_2330,])
func_2336 = relay.Function([], output)
mod['func_2336'] = func_2336
mod = relay.transform.InferType()(mod)
output = func_2336()
func_2337 = relay.Function([], output)
mutated_mod['func_2337'] = func_2337
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2373 = relay.var("var_2373", dtype = "float32", shape = (8, 1, 16))#candidate|2373|(8, 1, 16)|var|float32
const_2374 = relay.const([[[-9.536127,-3.214123,-9.380492,-3.222031,6.475213,7.527301,9.069708,-1.905299,0.821261,3.391929,3.396158,-8.176359,3.277416,-2.566158,9.065593,8.205338],[5.284446,-2.510807,8.916639,-4.177685,9.864145,8.081412,5.510729,9.543751,-3.481784,-8.356469,4.431274,-4.106727,-1.855532,-2.287599,-2.645505,2.114945],[8.494613,0.462450,-6.243798,-8.653149,-7.104986,-6.999872,9.640602,-0.355608,-3.507751,7.375430,5.718195,-4.377376,-7.680518,-7.692062,-3.085994,-2.918485],[3.931405,1.578991,1.541544,6.924938,0.831134,3.012969,2.223385,0.441515,-1.844349,5.119726,-3.525518,-6.276733,-6.775682,4.361901,-8.237120,2.506738]],[[5.428068,-4.329013,-8.576918,-8.789071,9.016917,-1.266938,-1.611301,9.743293,1.297896,-5.797042,-0.526664,-0.140888,7.894709,-7.691345,-1.037350,4.339525],[-5.495384,-8.542672,-8.736692,-6.143192,6.461943,-9.037630,-7.114564,-1.752149,7.060784,9.807472,1.805966,-7.031602,0.175709,6.010686,-2.093099,-6.286021],[-7.252351,0.917996,3.291922,-4.658838,7.054256,-4.402305,-4.738069,3.908025,-6.908354,-6.790761,-9.259380,-9.822120,5.383958,5.789601,0.482076,-1.292193],[8.257164,-3.985816,5.352125,2.287424,9.284500,7.214847,-7.501488,7.243031,2.869333,6.359209,3.484404,-9.318393,3.473196,-4.668061,2.439985,-8.589745]],[[9.623719,8.906919,3.030813,2.290064,3.767476,7.553448,9.211633,-5.474578,-4.999648,-6.816404,0.341816,-7.962729,7.010273,5.126193,8.698168,9.964969],[-7.446606,1.294903,6.089858,7.142339,2.636900,-1.158991,8.452353,-4.368265,-2.882785,1.427915,7.989548,-8.940499,2.036216,5.558957,0.801596,7.956297],[0.962618,-9.942938,2.031201,3.478852,-9.144412,9.080170,-8.627438,8.796688,-9.707275,3.579723,-8.600491,-9.298943,1.691894,-6.945710,-1.558865,7.560889],[-5.257523,-6.879174,0.022542,4.306446,-4.833344,3.075276,-3.493290,8.118416,-8.001374,-9.806108,3.480270,-0.498055,-9.982162,8.681580,-4.757552,-9.326351]],[[-5.773683,-4.030503,5.883815,7.301895,-1.779277,-4.409582,4.142519,5.674452,-4.792287,-0.139494,9.488554,6.066919,2.562796,-6.826748,7.889389,5.484277],[-9.189044,1.611313,5.983779,5.048479,5.570304,-9.887098,4.086199,-6.219797,3.431584,1.831836,3.358273,-1.494660,-0.025508,-8.302112,6.252552,9.442862],[5.559848,4.747530,-4.021106,-9.350096,4.343978,-6.834102,0.433785,-1.782007,-4.930660,8.197090,-0.476016,-9.200855,-0.083459,-4.363818,-2.836751,8.256337],[-2.254398,-9.386448,5.803977,0.245560,0.588625,-6.902946,-1.727282,7.628087,-6.510769,0.776231,-9.434948,1.187692,-4.683112,9.105537,-0.707095,6.713983]],[[0.031807,4.611520,-8.225392,5.349138,-8.025391,-7.827624,3.521260,4.351443,-6.143888,-9.889508,6.571062,-4.300292,-5.999861,-7.559711,-5.347880,7.666736],[-8.591842,4.483751,1.536047,-0.502432,-8.826239,6.056682,9.117882,5.035772,9.140782,-7.973559,-2.027584,-0.706304,-6.149352,4.928578,-6.739878,2.124439],[7.565491,-6.124430,3.110155,-9.066951,1.741250,2.198390,3.187508,3.585929,9.900051,9.361028,-1.748569,-9.450003,-0.391003,0.745540,-7.649579,4.457821],[0.395893,2.350572,2.835205,-1.439208,7.750467,6.881549,9.447618,8.871259,-8.414509,-7.327822,-8.991352,-2.955598,-9.810326,-1.149561,-1.197052,-3.810627]],[[1.617175,-8.077194,5.641196,8.006983,5.389182,0.660881,3.524321,7.090552,7.358360,-4.878527,-6.878066,6.632348,7.648173,7.777058,1.900212,7.147527],[2.019439,6.187567,3.441179,7.482043,0.541135,9.300857,1.928399,8.518959,-8.816014,1.463611,-7.794374,3.609492,-5.388735,3.024702,-3.204443,-1.124670],[-0.619180,-2.982199,-4.035259,-8.612492,6.298484,8.848199,-5.802856,2.081445,-9.300842,4.839542,2.278134,-3.899752,-4.830509,-1.027163,1.079015,-8.970516],[-3.841168,6.554377,1.209208,1.256396,8.050183,5.840337,2.288323,-7.340500,7.729613,-1.704534,-4.742045,-7.097581,-8.062846,6.286311,6.740406,4.358565]],[[-0.937596,5.491037,5.702032,-1.390293,2.671833,-6.447155,2.496260,-7.760060,5.614563,7.776656,-4.653735,-6.224050,-0.258397,-2.298952,2.308989,-0.373550],[-6.192811,9.756547,-0.571018,-4.340053,-3.456442,-7.038636,5.970451,-2.815944,2.412190,-5.568883,-9.917890,-0.567145,-0.157439,-4.892346,-9.877599,0.532939],[-4.571914,-4.305665,4.580013,-9.881940,-3.855720,4.869691,-6.929675,-8.841267,7.900927,8.855135,3.696574,1.309873,-6.780135,9.476254,-5.023258,1.142324],[-0.759572,8.800393,-1.841513,5.454428,-5.516831,-5.969976,-0.181516,-9.211284,7.149705,8.655201,6.222498,-5.770439,9.119012,-6.841979,-3.539657,-8.559522]],[[-0.543358,-3.545053,-8.916584,9.474381,-7.271232,4.244319,-7.261844,8.539750,3.360936,-2.591991,3.927220,-0.672682,-0.887367,-1.170285,-2.181908,6.961589],[-5.472063,1.268456,7.322449,7.042568,-2.414242,5.137675,-0.317752,-0.260477,6.689895,-2.491181,2.016760,0.025876,2.535277,-1.035054,5.946014,-6.336509],[-2.977804,-3.094208,-7.185098,2.685654,-0.770927,7.993546,3.525203,-3.934019,-1.990533,4.914828,6.174162,-3.201404,-3.109766,-5.236065,-6.216731,9.398583],[-0.287150,6.904897,5.083348,9.584653,0.062056,-8.681276,-4.811272,3.663787,7.905357,-9.501257,-7.049603,-5.891688,3.960442,-1.455164,6.073320,-1.446111]]], dtype = "float32")#candidate|2374|(8, 4, 16)|const|float32
bop_2375 = relay.divide(var_2373.astype('float32'), const_2374.astype('float32')) # shape=(8, 4, 16)
output = bop_2375
output2 = bop_2375
func_2378 = relay.Function([var_2373,], output)
mod['func_2378'] = func_2378
mod = relay.transform.InferType()(mod)
var_2379 = relay.var("var_2379", dtype = "float32", shape = (8, 1, 16))#candidate|2379|(8, 1, 16)|var|float32
output = func_2378(var_2379)
func_2380 = relay.Function([var_2379], output)
mutated_mod['func_2380'] = func_2380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2400 = relay.TupleGetItem(func_2305_call(), 0)
call_2401 = relay.TupleGetItem(func_2307_call(), 0)
uop_2404 = relay.atan(call_2400.astype('float64')) # shape=(8, 1, 5)
uop_2406 = relay.atan(call_2401.astype('float64')) # shape=(8, 1, 5)
func_1716_call = mod.get_global_var('func_1716')
func_1718_call = mutated_mod.get_global_var('func_1718')
var_2408 = relay.var("var_2408", dtype = "float32", shape = (1134,))#candidate|2408|(1134,)|var|float32
call_2407 = relay.TupleGetItem(func_1716_call(relay.reshape(var_2408.astype('float32'), [9, 14, 9])), 0)
call_2409 = relay.TupleGetItem(func_1718_call(relay.reshape(var_2408.astype('float32'), [9, 14, 9])), 0)
bop_2418 = relay.greater(call_2400.astype('bool'), relay.reshape(uop_2404.astype('bool'), relay.shape_of(call_2400))) # shape=(8, 1, 5)
bop_2421 = relay.greater(call_2401.astype('bool'), relay.reshape(uop_2406.astype('bool'), relay.shape_of(call_2401))) # shape=(8, 1, 5)
bop_2425 = relay.floor_divide(bop_2418.astype('float64'), relay.reshape(uop_2404.astype('float64'), relay.shape_of(bop_2418))) # shape=(8, 1, 5)
bop_2428 = relay.floor_divide(bop_2421.astype('float64'), relay.reshape(uop_2406.astype('float64'), relay.shape_of(bop_2421))) # shape=(8, 1, 5)
bop_2430 = relay.mod(var_2408.astype('float64'), relay.reshape(call_2407.astype('float64'), relay.shape_of(var_2408))) # shape=(1134,)
bop_2433 = relay.mod(var_2408.astype('float64'), relay.reshape(call_2409.astype('float64'), relay.shape_of(var_2408))) # shape=(1134,)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2434 = relay.TupleGetItem(func_2305_call(), 0)
call_2435 = relay.TupleGetItem(func_2307_call(), 0)
output = relay.Tuple([bop_2425,bop_2430,call_2434,])
output2 = relay.Tuple([bop_2428,bop_2433,call_2435,])
func_2442 = relay.Function([var_2408,], output)
mod['func_2442'] = func_2442
mod = relay.transform.InferType()(mod)
mutated_mod['func_2442'] = func_2442
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2443 = relay.var("var_2443", dtype = "float32", shape = (1134,))#candidate|2443|(1134,)|var|float32
func_2442_call = mutated_mod.get_global_var('func_2442')
call_2444 = func_2442_call(var_2443)
output = call_2444
func_2445 = relay.Function([var_2443], output)
mutated_mod['func_2445'] = func_2445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2337_call = mutated_mod.get_global_var('func_2337')
call_2508 = relay.TupleGetItem(func_2336_call(), 0)
call_2509 = relay.TupleGetItem(func_2337_call(), 0)
output = call_2508
output2 = call_2509
func_2513 = relay.Function([], output)
mod['func_2513'] = func_2513
mod = relay.transform.InferType()(mod)
mutated_mod['func_2513'] = func_2513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2513_call = mutated_mod.get_global_var('func_2513')
call_2514 = func_2513_call()
output = call_2514
func_2515 = relay.Function([], output)
mutated_mod['func_2515'] = func_2515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2565 = relay.TupleGetItem(func_2305_call(), 0)
call_2566 = relay.TupleGetItem(func_2307_call(), 0)
output = relay.Tuple([call_2565,])
output2 = relay.Tuple([call_2566,])
func_2571 = relay.Function([], output)
mod['func_2571'] = func_2571
mod = relay.transform.InferType()(mod)
output = func_2571()
func_2572 = relay.Function([], output)
mutated_mod['func_2572'] = func_2572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2571_call = mod.get_global_var('func_2571')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_2578 = relay.TupleGetItem(func_2571_call(), 0)
call_2579 = relay.TupleGetItem(func_2572_call(), 0)
uop_2581 = relay.log10(call_2578.astype('float32')) # shape=(8, 1, 5)
uop_2583 = relay.log10(call_2579.astype('float32')) # shape=(8, 1, 5)
func_1241_call = mod.get_global_var('func_1241')
func_1246_call = mutated_mod.get_global_var('func_1246')
var_2587 = relay.var("var_2587", dtype = "bool", shape = ())#candidate|2587|()|var|bool
const_2588 = relay.const([True,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False], dtype = "bool")#candidate|2588|(560,)|const|bool
const_2589 = relay.const([-9,-1,7,2,3,6,-2,7,4,4,-8,-10,-4,-5,-10,-1,7,3,-3,7,-1,-10,-9,-1,-2,-3,-1,3,-9,-4,-1,5,7,4,-5,8,4,-8,-4,-8,-2,-9,3,-10,-10,-1,-9,1,-6,-10,5,-6,-7,-4,3,-9,4,-10,10,1,-4,3,1,-3,-10,-10,10,-6,10,8,-3,-8,5,-5,-8,4,-1,7,-2,8,3,9,-4,10,4,-7,5,7,3,-4,10,-3,7,-10,-10,1,8,7,-4,6,-5,8,-8,9,-6,-2,-10,-5,5,-6,-6,10,-8,6,4,-9,-4,-8,-1,-4,1,-1,-1,2,4,4,-6,5,-1,-3,2,-5,-8,-9,-1,5,-8,-7,-5,-8,-6,10,-7,3,6,5,9,-4,-3,5,5,10,-6,-6,-5,-9,-7,4,-4,1,4,-9,6,-9,8,4,3,9,-10,-8,9,9,-6,9,-9,-9,-8,3,2,2,-5,-3,8,-8,7,5,-3,2,-7,-9,-3,7,-7,-5,4,6,2,8,3,2,3,-6,4,-6,-10,5,-3,5,7,-8,-5,-2,6,-1,-7,-9,-2,7,-6,5,9,-9,4,-2,-4,-2,5,-10,-6,-9,3,3,6,9,4,6,-6,6,1,-1,-10,-5,-8,7,-5,-7,8,-4,-10,4,9,-7,-9,4,-3,-6,-9,2,-6,-3,9,9,-10,2,8,-1,-8,-1,-1,6,10,-1,-2,8,1,-7,1,-8,9,-10,5,-5,10,-9,-10,9,6,-1,-10,-6,-2,3,-1,4,-10,8,-6,6,8,6,-2,-10,-4,9,-9,7,10,-5,-1,-10,3,-4,-10,4,-10,7,-7,10,-7,-5,6,8,-2,-6,3,-3,3,-5,2,2,-2,-3,6,-10,6,9,-9,-7,-1,-5,-8,-3,10,7,-7,-5,8,8,3,6,5,-1,-2,5,-1,10,-1,-2,10,4,-8,8,6,9,6,-1,1,-5,-10,8,1,1,-10,-4,10,-10,4,4,4,3,1,2,6,4,-6,-5,10,-10,9,-3,-9,-9,8,6,7,3,3,-9,-3,-3,5,7,-4,-8,-2,-3,-1,-7,-6,-3,2,2,-3,2,-3,-4,-5,-6,1,-3,6,-3,8,9,3,-8,10,-10,-8,9,-9,2,6,-4,-3,-10,-7,-7,3,1,-8,10,-7,-10,-3,6,2,8,5,4,3,8,-9,4,-3,-7,-2,-8,7,3,7,-6,9,-6,7,4,-8,-1,9,8,-10,2,1,-2,10,-10,7,7,-1,-10,-6,10,9,8,7,-10,10,1,-6,2,2,-4,-10,-5,-5,-1,1,5,-3,8,1,-6,-1,-4], dtype = "int64")#candidate|2589|(504,)|const|int64
call_2586 = relay.TupleGetItem(func_1241_call(relay.reshape(var_2587.astype('bool'), []), relay.reshape(const_2588.astype('bool'), [4, 10, 14]), relay.reshape(const_2589.astype('int64'), [504,]), ), 0)
call_2590 = relay.TupleGetItem(func_1246_call(relay.reshape(var_2587.astype('bool'), []), relay.reshape(const_2588.astype('bool'), [4, 10, 14]), relay.reshape(const_2589.astype('int64'), [504,]), ), 0)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2597 = relay.TupleGetItem(func_2305_call(), 0)
call_2598 = relay.TupleGetItem(func_2307_call(), 0)
bop_2600 = relay.subtract(uop_2581.astype('uint64'), var_2587.astype('uint64')) # shape=(8, 1, 5)
bop_2603 = relay.subtract(uop_2583.astype('uint64'), var_2587.astype('uint64')) # shape=(8, 1, 5)
func_2571_call = mod.get_global_var('func_2571')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_2605 = relay.TupleGetItem(func_2571_call(), 0)
call_2606 = relay.TupleGetItem(func_2572_call(), 0)
output = relay.Tuple([call_2586,const_2588,const_2589,call_2597,bop_2600,call_2605,])
output2 = relay.Tuple([call_2590,const_2588,const_2589,call_2598,bop_2603,call_2606,])
func_2637 = relay.Function([var_2587,], output)
mod['func_2637'] = func_2637
mod = relay.transform.InferType()(mod)
mutated_mod['func_2637'] = func_2637
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2638 = relay.var("var_2638", dtype = "bool", shape = ())#candidate|2638|()|var|bool
func_2637_call = mutated_mod.get_global_var('func_2637')
call_2639 = func_2637_call(var_2638)
output = call_2639
func_2640 = relay.Function([var_2638], output)
mutated_mod['func_2640'] = func_2640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2664 = relay.TupleGetItem(func_2305_call(), 0)
call_2665 = relay.TupleGetItem(func_2307_call(), 0)
func_2442_call = mod.get_global_var('func_2442')
func_2445_call = mutated_mod.get_global_var('func_2445')
var_2667 = relay.var("var_2667", dtype = "float32", shape = (1134,))#candidate|2667|(1134,)|var|float32
call_2666 = relay.TupleGetItem(func_2442_call(relay.reshape(var_2667.astype('float32'), [1134,])), 0)
call_2668 = relay.TupleGetItem(func_2445_call(relay.reshape(var_2667.astype('float32'), [1134,])), 0)
const_2676 = relay.const([[[7.870174,-0.154434,-5.727025,-3.636192,5.936097],[-2.366047,-2.691018,9.977091,-0.205386,0.734727],[-9.015070,8.794114,-9.847845,-2.695568,-1.453180],[3.334918,-0.059717,4.682821,-3.335000,-5.890126],[1.261689,-7.542562,-9.901783,-7.855064,-3.470942],[-2.623341,6.384056,1.536209,-1.793590,-4.830604],[2.064354,-4.641265,1.616980,9.236613,-4.471225]],[[6.935062,-2.293058,5.077835,6.292563,0.826635],[2.953252,8.143752,7.149446,-5.352850,-2.100612],[-6.029885,-2.457212,5.019519,-4.168676,1.520222],[5.857996,-1.907681,-6.211598,-4.168631,-7.608558],[-2.365487,2.135369,-7.360280,-9.917308,-2.067501],[9.849739,8.536310,-5.176047,0.941434,0.896595],[5.803362,8.185073,-1.670701,7.362612,-5.589363]],[[-3.476742,4.244953,-2.460867,-6.485064,-6.814179],[0.590020,4.938245,6.411677,-2.852065,-8.798141],[8.011930,-4.850949,-8.027725,2.561723,7.511305],[3.589980,-9.931256,7.683186,-5.340775,9.954537],[0.646609,0.016792,9.094967,-8.380897,5.113496],[2.371626,-5.025798,-8.416868,-6.543806,-2.145919],[4.210309,8.562657,-3.666031,-4.287137,-2.619479]],[[7.321587,-2.195195,-9.467637,6.375172,5.236067],[-8.665479,6.306368,-7.712942,2.211112,2.810938],[-2.197280,2.004468,-1.969576,1.747022,-3.844141],[6.734487,6.038227,-4.848780,5.183617,-6.197984],[4.081228,-9.043110,5.212743,-2.649071,9.296231],[-3.179222,-8.480355,-6.118744,9.585673,6.632071],[9.168939,9.377059,-7.514460,9.730265,3.456057]],[[5.102688,-5.009847,1.529619,-0.754400,-1.047635],[-1.845308,-7.560336,-1.260981,7.614709,-7.127000],[0.353404,5.255345,-9.060385,8.516220,-6.254751],[6.256414,4.656237,4.634041,5.452148,-4.332118],[1.639501,-2.500295,5.933077,-2.096343,-9.886702],[0.613245,7.213813,-3.179645,-7.395417,9.765454],[-9.291812,-0.044724,-4.835132,-7.580824,-9.952942]],[[6.103801,4.634874,5.242620,-3.128986,-7.271696],[-3.106883,-4.837271,-9.539599,4.700045,-5.075473],[6.671555,1.335813,-1.355474,2.312344,0.697226],[3.678690,-3.585572,-4.010714,7.157314,7.241714],[9.370053,8.688886,1.598669,-9.219465,9.251192],[3.376020,7.303869,-0.019947,-1.599289,-3.872511],[6.498892,-7.034269,2.434004,7.383294,1.672063]],[[-7.486101,-2.111466,9.976848,7.186340,-3.007815],[-3.467748,-9.049135,-3.668577,-2.761627,-3.867508],[-6.550461,-3.637000,9.753939,8.824932,2.694446],[-8.566652,5.386769,4.237821,-6.131335,-2.532014],[9.391149,4.421416,-2.461051,9.026538,-1.723613],[-5.393197,0.567102,-1.932174,-9.007414,-3.419830],[-1.227201,4.622599,5.069010,-4.896979,1.769732]],[[7.664928,-6.334896,-5.168015,-7.974842,8.071143],[-8.768633,-9.632242,-9.306608,-5.674681,-2.305214],[-3.504833,4.095252,0.818042,3.652345,9.685697],[-0.032580,5.981897,7.155308,-1.772862,3.167803],[-8.792258,4.278924,-2.732635,8.337617,-4.817175],[4.165819,4.715653,-4.870238,0.462954,-8.439396],[-6.489873,7.267954,3.398280,-8.502560,5.689795]]], dtype = "float64")#candidate|2676|(8, 7, 5)|const|float64
bop_2677 = relay.equal(call_2666.astype('bool'), const_2676.astype('bool')) # shape=(8, 7, 5)
bop_2680 = relay.equal(call_2668.astype('bool'), const_2676.astype('bool')) # shape=(8, 7, 5)
const_2687 = relay.const([[[True,True,False,True,True],[True,False,False,False,True],[False,False,True,False,True],[True,False,False,True,False],[True,False,False,True,True],[True,False,True,True,True],[False,False,False,False,False]],[[True,False,False,True,False],[True,False,True,False,False],[False,True,False,False,True],[False,False,True,True,True],[False,False,True,False,True],[False,False,True,False,False],[True,True,False,True,False]],[[True,True,False,False,True],[True,False,True,True,True],[False,False,True,True,True],[False,True,True,True,True],[False,True,True,True,True],[False,True,False,False,False],[False,True,True,True,True]],[[True,False,False,False,True],[True,False,True,False,True],[False,False,False,True,True],[False,True,False,True,True],[True,True,False,True,False],[False,True,True,False,False],[True,True,False,True,True]],[[False,False,True,True,False],[False,False,False,False,True],[True,False,True,True,False],[False,False,True,False,True],[True,False,False,True,False],[True,False,True,True,True],[False,True,True,True,True]],[[True,True,True,True,False],[False,False,False,True,True],[False,True,True,False,True],[False,True,False,False,False],[False,True,False,False,True],[True,False,False,False,False],[True,True,True,False,False]],[[True,True,False,False,False],[True,False,False,False,False],[True,False,False,True,True],[False,False,False,True,False],[True,False,False,False,True],[False,True,False,False,False],[True,True,True,True,True]],[[True,True,False,True,True],[False,True,False,False,False],[True,True,False,True,False],[False,True,False,True,True],[True,True,False,False,True],[False,True,True,True,False],[False,True,True,False,False]]], dtype = "bool")#candidate|2687|(8, 7, 5)|const|bool
bop_2688 = relay.less(bop_2677.astype('bool'), relay.reshape(const_2687.astype('bool'), relay.shape_of(bop_2677))) # shape=(8, 7, 5)
bop_2691 = relay.less(bop_2680.astype('bool'), relay.reshape(const_2687.astype('bool'), relay.shape_of(bop_2680))) # shape=(8, 7, 5)
output = relay.Tuple([call_2664,var_2667,bop_2688,])
output2 = relay.Tuple([call_2665,var_2667,bop_2691,])
func_2694 = relay.Function([var_2667,], output)
mod['func_2694'] = func_2694
mod = relay.transform.InferType()(mod)
mutated_mod['func_2694'] = func_2694
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2695 = relay.var("var_2695", dtype = "float32", shape = (1134,))#candidate|2695|(1134,)|var|float32
func_2694_call = mutated_mod.get_global_var('func_2694')
call_2696 = func_2694_call(var_2695)
output = call_2696
func_2697 = relay.Function([var_2695], output)
mutated_mod['func_2697'] = func_2697
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2699 = relay.const([[[8,7,-1,-6,6,-7,-2,-2,-1,2,-5,8,6,-7]],[[-3,6,-8,-3,-9,5,1,-4,5,10,6,1,6,5]],[[3,4,-4,9,5,-5,1,10,2,-6,1,-4,-9,10]],[[2,-7,7,3,4,-7,6,-3,-2,10,6,-2,4,-6]],[[2,-10,1,-1,1,-4,-10,5,-3,-2,1,10,9,-4]],[[9,-10,8,-5,-9,1,-4,6,6,-9,-10,-3,-4,8]],[[-4,-8,6,3,-8,-5,9,-7,-1,-9,4,3,9,-7]]], dtype = "int16")#candidate|2699|(7, 1, 14)|const|int16
var_2700 = relay.var("var_2700", dtype = "int16", shape = (7, 10, 14))#candidate|2700|(7, 10, 14)|var|int16
bop_2701 = relay.greater_equal(const_2699.astype('bool'), var_2700.astype('bool')) # shape=(7, 10, 14)
output = relay.Tuple([bop_2701,])
output2 = relay.Tuple([bop_2701,])
func_2743 = relay.Function([var_2700,], output)
mod['func_2743'] = func_2743
mod = relay.transform.InferType()(mod)
mutated_mod['func_2743'] = func_2743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2744 = relay.var("var_2744", dtype = "int16", shape = (7, 10, 14))#candidate|2744|(7, 10, 14)|var|int16
func_2743_call = mutated_mod.get_global_var('func_2743')
call_2745 = func_2743_call(var_2744)
output = call_2745
func_2746 = relay.Function([var_2744], output)
mutated_mod['func_2746'] = func_2746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2788 = relay.TupleGetItem(func_2305_call(), 0)
call_2789 = relay.TupleGetItem(func_2307_call(), 0)
func_2336_call = mod.get_global_var('func_2336')
func_2337_call = mutated_mod.get_global_var('func_2337')
call_2790 = relay.TupleGetItem(func_2336_call(), 0)
call_2791 = relay.TupleGetItem(func_2337_call(), 0)
func_2571_call = mod.get_global_var('func_2571')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_2794 = relay.TupleGetItem(func_2571_call(), 0)
call_2795 = relay.TupleGetItem(func_2572_call(), 0)
uop_2796 = relay.rsqrt(call_2794.astype('float64')) # shape=(8, 1, 5)
uop_2798 = relay.rsqrt(call_2795.astype('float64')) # shape=(8, 1, 5)
func_2019_call = mod.get_global_var('func_2019')
func_2022_call = mutated_mod.get_global_var('func_2022')
const_2802 = relay.const([3.661547,7.508027,7.529119,6.235657,-7.118493,-2.589383,8.482336,-2.333060,1.828178,4.849366,-6.307658,7.346589,-4.419935,-3.503010,-7.554621,-8.613020,5.449100,-9.931736,-5.835956,-1.505486,-9.823885,5.377836,-3.628722,-9.033092,5.079767,-5.413522,-6.334233,-8.022859,3.010015,-0.141415,-4.899948,3.103053,8.454860,-0.194517,-5.325316,-6.011994,4.881284,-2.704304,0.020643,-4.475026,-5.874825,6.872269,-6.022264,8.625855,-6.361921,8.452363,-3.733417,-0.132225,0.437237,9.025317,1.897650,-0.596170,0.516759,-8.767201,-9.055340,2.852701,-2.181559,0.905398,3.546487,-9.330050,9.815916,-1.963864,4.721967,6.551843,-3.044554,-4.901016,-8.269511,-3.974086,5.592065,4.817213,8.914213,7.622138,3.410602,3.802126,7.898178,-1.365255,6.837561,3.013805,-0.793051,1.178077,2.962322,-0.847298,5.677994,-6.664822,-4.910534,-7.041701,-1.069905,0.912308,-2.196685,-6.687115,-9.898341,-4.477845,-5.249661,-5.056937,-0.941524,4.483956,0.369974,-2.520451,-0.328950,-9.694723,-5.375876,7.070985,-1.471702,-9.590612,9.884311,-7.194236,4.242296,5.533429,-6.197287,-3.345530,-3.049496,4.607976,-0.452256,-3.899415,-2.698737,7.162712,9.078011,3.445872,4.352765,-1.706053,0.423959,-0.298551,-7.644558,-1.853258,-2.386921,1.929062,-3.056922,-1.223525,-9.583753,7.820894,2.709171,3.339720,5.210728,-6.331333,-8.142874,0.993997,-1.350962,7.829533,-8.846449,5.152406,-5.508407,5.139089,1.817428,7.092731,-2.962423,-8.719989,8.734179,-2.045750,0.302267,2.374395,7.868124,8.307607,8.379004,-9.698963,-5.544177,-7.300496,1.529105,5.027213,2.614775,-5.909744,4.028288,-6.549341,3.541576,-0.446809,0.705931,-5.491025,-6.753714,-8.175269,-8.213199,6.321505,1.494629,-2.213587,3.607937,2.289862,-6.601489,-0.190544,4.721524,2.473088,6.237270,6.674737,3.567412,-8.217288,9.524087,9.379142,3.655093,-9.140043,-4.062651,8.431726,-5.052374,7.032847,0.638117,-2.992348,-8.181051,3.758099,7.159654,-7.554511,-8.254688,4.860509,-1.989621,-8.113420,2.714537,-1.335179,6.831770,-0.010328,-6.042687,-9.902661,0.834851,-5.631270,-5.090468,-1.040537,-8.231261,2.990722,5.309163,-9.960030,5.916786,0.218692,9.538130,7.735542,-2.219554,-9.201249,6.573273,-3.252770,-4.356371,-7.200642,-7.972320,-3.379440,7.216339,8.699611,-7.799642,-4.572570,-7.024059,9.134857,0.511423,-8.311587,-8.463503,5.226245,-7.774249,-5.171868,-8.832387,6.500013,2.493451,-2.436555,5.904804,4.373280,8.546815,-0.408768,-9.853789,-6.953618,-1.070846,8.764528,6.735999,-6.285979,-6.750824,-4.999594,0.799991,3.279380,-8.018569,2.760650,2.090515,2.268268,0.494713,8.972474,9.320716,6.379093,-9.701041,-5.908640,6.124213,5.755787,-7.342441,8.487263,-8.508827,-5.534259,-7.621479,-3.164509,9.505613,-7.998067,4.580752,-4.905615,2.107115,-1.747788,-5.837678,-6.670432,9.119937,2.071483,8.037516,9.545677,3.434976,-8.302331,-5.571077,0.970872,3.888633,-0.110840,2.149826,7.538925,-3.493011,0.307532,0.477882,0.604158,2.233508,-0.921851,6.618434,-5.321910,0.680916,-7.658905,-9.710089,0.619197,2.318486,-1.924950,-4.243360,-6.579060,-9.212993,8.693503,3.785539,-6.180626,9.024986,4.500999,6.514937,7.981504,0.344981,-3.344587,-7.773933,6.241510,9.371232,-2.804247,8.535686,-7.238493,-0.954303,1.814896,-1.623831,4.431382,-2.259950,-8.352343,-2.625492,6.226710,0.734100,0.950707,4.189422,-7.621849,1.929528,2.366698,8.493376,-4.210076,2.742413,2.756187,4.983388,-1.092624,9.836088,3.553561,-3.457315,2.857747,-0.424757,9.137679,1.793501,-2.850780,9.946702,-0.237527,-5.040553,-2.111836,-4.999867,3.393787,-3.575131,-5.376530,9.260777,-6.963473,-5.765481,7.769008,-1.381074,-0.968341,-7.992306,-4.644544,-1.859551,-3.381691,4.313165,9.897344,-7.502097,-8.281633,-5.318807,4.423338,-4.493696,4.283394,0.629876,-8.080800,-4.498494,-8.684986,8.475840,-4.941290,2.102949,-5.666276,1.017003,-5.680148,3.370529,1.442703,5.140832,7.211855,-0.150778,-4.166832,2.754852,2.077051,-9.922003,8.306797,3.348302,5.598712,-0.685332,5.258945,3.681733,-2.415298,-4.408639,-2.258888,-4.196855,-0.770627,8.806561,-6.152929,6.731642,-5.675002,8.840707,3.491745,3.649261,4.055289,3.115750,5.040042,6.772016,5.839391,5.427823,7.810538,7.207969,-2.501464,1.309029,5.640951,1.368305,-2.037370,6.566833,8.164708,-2.361357,3.429110,8.497448,8.663583,-0.250165,5.196859,-0.957666,1.962246,-3.046497,-5.867052,-9.777419,-3.702636,5.398068,5.959946,-2.319301,7.611480,7.980710,-6.304415,-4.113451,1.403868,-0.677190,-0.142014,-1.403702,-0.896160,-2.711720,-3.267376,7.852310,-3.687223,4.264597,2.318477,-2.016828,-2.922737,9.550213,-0.572640,-4.537502,-7.314980,-0.350011,-7.961885,-0.089294,3.754252,4.540457,-3.567274,-6.354927,-1.983063,-1.823829,-6.888314,-5.277546,-4.282750,6.427799,0.880953,1.193326,0.958334,0.467882,-0.739394,-3.559463,-8.268665,3.421466,-8.073486,6.032416,4.844190,1.794405,-1.219874,-9.174297,2.793575,3.996246,-1.878128,9.166494,1.245185,7.785638,-9.607927,5.685110,5.290650,4.622528,4.448488,-9.551176,-7.605345,-8.330692,-5.997121,-1.533491,-4.719319,-4.182825,-5.524159,-8.135137,-8.897268,7.914397,-2.120185,2.573842,2.998040,1.241022,9.348537,9.214349,0.915322,-3.801044,-3.752967,-5.553246,8.504583,8.611969,-9.476892,5.223630,7.797013,9.700597,1.617728,-8.146481,-9.164382,9.593018,3.620101,6.739592,-3.908557,-2.270585,-3.855997,-6.501482,-3.388385,6.412944,9.355234,5.981536,5.606024,-5.866896,-7.898281,5.423502,4.998500,-8.588660,2.669800,0.735972,-5.806669,2.691106,-6.285120,-1.450417,9.142342,4.562227,-0.978626,-0.004193,-9.582561,-2.896320,4.580859,9.949832,5.676443,5.979681,1.664426,-6.241856,9.784665,6.679017,4.394186,-3.111998,3.375321,-9.541527,-0.387661,-5.635939,0.263670,2.079166,-1.417779,1.394735,0.188506,3.778427,-0.171848,-0.909719,5.023328,7.626594,1.076322,8.220382,-0.204511,-4.297740,-6.318292,2.795816,2.752502,-8.729091,0.702952,5.911828,3.847234,8.781477,4.275540,6.787896,5.357477,9.109126,-1.713099,-1.917299,-2.135793,3.727659,7.910340,2.832452,-3.916385,-4.656698,5.859349,-3.803313,-5.274608,-0.716721,1.270987,-3.296411,8.868338,7.531198,2.596044,-5.848299,-0.901246,-6.472239,-9.471701,-4.952419,-1.716475,-7.769583,3.539921,-9.478656,-0.805960,2.481397,-7.455893,1.927539,8.887685,6.790363,-3.868954,6.157977,2.979317,-5.828696,4.750880,-8.334029,5.289556,2.402598,1.044247,0.213096,7.530507,1.018298,-2.746064,4.372266,4.182515,-0.977267,-9.534415,-0.635446,-1.288231,9.526654,-4.987308,0.343368,-4.376729,-7.444572,-8.180069,6.381270,-8.722435,4.306257,3.056572,-4.626445,1.018775,-0.507554,-1.999826,4.760135,8.052856,-1.783118,7.979034,-9.817073,6.072965,5.987999,-3.284239,1.989965,-0.408681,7.529236,9.943828,-7.197613,4.837320,-6.647369,-8.667987,-0.005391,-5.972943,6.151447,-7.893025,1.181919,-3.699868,8.696461,9.092101,4.081680,0.550080,-4.803167,-5.045054,1.992784,6.448675,-6.770858,1.041924,-5.013007,7.170003,2.671889,8.828441,1.026165,-9.040824,-5.021020,4.132168,5.970423,-1.052698,7.911104,-9.394840,-5.225025,-7.787642,4.484149,4.633190,7.311927,8.402466,-8.134531,9.607298,-0.952402,-6.529911,-6.341611,-4.806857,-8.117212,5.590073,-6.435351,-7.701631,6.033538,0.789004,6.350341,-2.177247,9.150256,6.012364,-8.705976,-8.658440,-3.142403,6.787158,-1.211753,-0.857503,6.105778,1.423350,-2.375313,-3.179323,-3.510745,-9.193397,2.744288,3.086364,8.415609,-6.304046,0.341037,-5.425265,-7.095489,-7.238983,-9.598414,9.649082,-3.239220,1.238645,3.817690,6.895775,7.016390,0.694551,-9.940026,8.773677,0.276719,-9.231074,-9.044415,9.177516,-2.511822,-3.665993,-2.943974,-3.275743,-4.453291,9.273161,-4.585906,2.702108,7.682123,-3.609051,0.440803,0.685782,0.133615,-6.383271,-1.599667,-1.700696,6.857076,8.574427,9.118005,2.894887,4.087482,6.951130,5.271141,9.501543,1.753422,-3.228040,-2.727329,0.477171,8.870464,9.135144,2.220404,7.945720,-3.070727,7.744563,-0.861641,3.303023,3.867457,5.542963,-2.942415,8.851535,-8.859590,-6.233223,3.003390,8.770943,9.031616,7.808535,-1.237525,-6.342406,7.183206,-8.325353,-1.664402,-4.115711,-3.665604,-6.462248,-2.319189,-4.316123,9.583981,3.170891,7.658713,-7.077521,-1.148962,0.122804,-7.170283,7.201264,8.683240,0.222228,-1.246184,-4.346947,-6.839085,7.045795,-0.778009,7.858286,-0.073939,6.045974,8.319831,0.237275,6.858386,4.869070,-2.138377,7.679694,-6.658532,1.598416,-2.027047,-0.367415,-0.059356,-0.995588,3.837855,-8.166555,-4.413184,2.762025,1.302779,2.039573,-9.540736,-1.974766,-4.796170,-7.834161,1.279251,1.288038,5.954882,-0.476814,4.921904,8.931487,-6.582658,-2.448862,7.743347,8.719793,-3.108650,0.493144,3.887651,4.553222,4.312166,-7.452264,5.238089,4.402291,6.168526,-1.861328,-8.263491,-7.164213,-5.261716,1.409382,-4.081112,-4.303081,-8.639479,8.618336,-8.770874,7.374147,9.914041,-1.981776,0.459669,7.784832,4.543900,1.579804,1.122419,-1.385430,-5.704324,4.467978,-2.127130,-1.826537,2.545378,-8.835972,-0.890627,-0.198324,-6.658928,5.548488,-1.182727,-7.636737,-0.304294,2.785282,6.463617,1.456359,5.295152,0.311629,8.726634,-8.405629,3.240030,-5.808668,-2.766172,1.352429,6.924220,-6.666625,-1.792637,4.394003,-2.884001,-2.081685,-8.545168,-4.539136,6.758206,-3.640579,7.931644,9.295721,2.037436,-3.374721,-6.764907,-3.250618,-1.369481,6.557068,-0.014283,-3.805955,1.188982,-6.761963,-0.491218,-6.871811,-0.329692,-9.091785,4.724102,5.638047,1.417768,2.842521,6.316117,8.965318,-5.025082,-6.408779,0.837561,-1.193802,-8.358405,7.125647,1.401195,-9.364003,-6.385249,5.931554,-8.252327,-1.566847,-9.843039,-5.584422,-2.064455,-9.274062,-9.786294,4.766540,9.896468,5.619024,-9.587903,-7.081381,-0.593727,-4.240464,-9.030913,-9.309670,-1.689779,-3.057259,-2.895724,-5.365106,1.565505,-7.618105,-6.232605,5.041647,6.596742,9.951289,6.028357,5.238069,-3.141669,-1.779520,9.367080,3.818292,-0.762010,-1.247976,-9.526746,8.803438,1.713310,-5.530321,6.224563,5.447578,-5.807998,-2.845264,8.967969,1.288546,7.777534,-3.316447,-3.602833,-6.770569,8.703141,-4.006480,-3.875027,3.266373,1.920451,5.305066,-6.466968,0.955248,8.366134,-6.701862,1.237326,-5.932788,-7.418719,3.289286,-3.052278,0.512692,-8.433662,-9.700511,3.821829,3.937173,5.685558,3.701083,0.216602,-2.035978,-3.948327,0.486178,-9.571209,6.388172,-0.401825,7.708174,-6.016212,6.139071,-0.363132,4.595424,5.219087,-3.393154,1.751505,-7.657126,-6.930060,4.893941,-5.258966,-5.183226,-5.496527,3.332635,-5.329462,-2.495768,5.954093,-3.801715,7.267972,5.195359,-2.759877,2.411320,3.630495,-3.167006,-2.626725,-2.662414,8.411723,2.783592,-6.637002,-5.725669,9.696020,-1.833632,-7.141524,1.255516,-7.378386,2.556558,-0.537778,3.134517,-6.469116,-5.059776,0.444840,8.910834,5.632063,7.148810,3.684292,3.231520,-3.955112,3.628436,-2.455996,-0.178842,2.702784,6.548905,-6.065605,3.210975,-2.919066,7.808627,1.215824,-6.714549,0.527175,-4.316082,-6.824995,4.425760,5.670195,1.843855,8.592729,6.894969,1.348083,5.481731,9.540476,4.846597,-1.018312,6.262184,2.769857,-8.339002,6.993594,-0.627518,-5.193647,-9.005066,-3.847799,4.521125,1.465727,9.957468,6.764511,-1.854487,4.028640,9.245310,-7.045137,8.465115,-1.636248,-0.948410,2.128814,8.693118,7.873088,6.714276,-3.718743,1.207999,7.020975,-3.232073,0.681142,7.349389,-8.401955,-2.663736,-0.464024,4.601080,-0.858649,-2.416031,-9.489857,3.477246,-0.653041,6.722498,-3.457600,-4.674274,5.414179,-3.413474,-6.895419,-9.451903,-5.628355,6.617691,-6.403963,-6.267159,0.394228,-0.300821,-5.141542,7.398807,0.239305,8.375313,0.788950,1.197263,5.744011,-8.552341,-0.451282,-9.047624,2.745758,5.497301,-5.964967,-6.359843,-8.283860,2.858435,9.445192,5.524150,-4.033955,-4.034749,5.616287,-6.488715,2.725367,-6.958850,9.776021,0.940753,-2.349726,2.976850,-8.475222,-4.565065,-7.814291,8.127012,-7.265484,-7.913789,-0.120060,2.216105,4.683436,-7.437385,-5.906504,-0.781183,9.954485,-8.557526,-9.263668,9.055237,-2.116844,2.642310,5.388142,-1.973951,-4.035819,-9.663240,1.628547,-2.904845,-8.982843,7.266307,6.244615,-3.574776,4.885295,-9.491131,-1.856528,-6.392802,-5.555450,-1.383810,0.401773,8.502788,2.781245,-8.703841,2.543331,5.841774,8.912286,-3.067180,-2.630437,0.293975,-8.498789,6.025436,1.033473,2.610090,-3.053286,-9.605895,-6.547017,2.874053,4.855450,-9.718478,-8.502668,-9.652752,-2.075561,-8.570685,-7.079730,0.119687,2.287081,3.978693,-5.454428,-3.621839,-8.789407,-3.287681,3.170123,2.165260,8.942335,1.565921,3.193032,5.274429,6.585448,3.083288,-3.130100,-3.115481,1.965171,-6.816084,-6.877357,-6.853424,1.277527,8.873866,-5.814234,-9.474720,-8.472091,9.863187,5.044689,1.229608,-7.864475,-3.508206,5.166444,7.103014,9.751432,5.342305,-9.221296,-7.832397,-2.712207,-2.068903,-4.955159,7.776989,0.232889,1.498791,2.056533,1.599968,0.061184,-0.275345,-0.675275,8.998498,-8.435397,0.703801,9.398866,-8.634278,6.542787,-9.340349,8.609999,-6.700172,7.408560,-4.356748,-0.917737,-5.017296,3.798082,6.821132,-2.370107,2.931497,0.920303,-3.094395,5.161233,-3.714630,4.320477,-3.706765,-7.144385,3.033947,-4.723532,6.646602,4.500507,-2.037413,-2.468353,-4.757597,9.718618,9.126657,-5.871878,6.974742,6.423733,-0.351660,-0.771169,2.045651,8.485612,-4.776975,-5.193488,8.403978,-8.503927,5.414683,0.054173,3.625031,0.471507,1.674951,-9.470451,5.327348,-8.531973,5.049015,2.993594,-7.723341,0.097794,-8.111417,-6.831752,-1.432620,-6.414423,4.579385,1.225071,-0.759414,-0.503926,1.120812,-2.631491,-9.141348,-1.873478,7.336547,-5.922174,7.795873,1.566291,-3.895498,6.631143,-1.319423,-9.315228,8.477995,-1.705505,-9.243106,6.391224,-6.121315,0.066073,-7.732543,-3.633028,7.749564,4.611119,-4.880173,-9.358580,-7.359564,3.500406,8.133645,3.445033,-4.630813,-7.867499,-7.121823], dtype = "float32")#candidate|2802|(1400,)|const|float32
call_2801 = func_2019_call(relay.reshape(const_2802.astype('float32'), [10, 10, 14]))
call_2803 = func_2019_call(relay.reshape(const_2802.astype('float32'), [10, 10, 14]))
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_2805 = func_2513_call()
call_2806 = func_2513_call()
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2811 = relay.TupleGetItem(func_2305_call(), 0)
call_2812 = relay.TupleGetItem(func_2307_call(), 0)
output = relay.Tuple([call_2788,call_2790,uop_2796,call_2801,const_2802,call_2805,call_2811,])
output2 = relay.Tuple([call_2789,call_2791,uop_2798,call_2803,const_2802,call_2806,call_2812,])
func_2813 = relay.Function([], output)
mod['func_2813'] = func_2813
mod = relay.transform.InferType()(mod)
output = func_2813()
func_2814 = relay.Function([], output)
mutated_mod['func_2814'] = func_2814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2337_call = mutated_mod.get_global_var('func_2337')
call_2818 = relay.TupleGetItem(func_2336_call(), 0)
call_2819 = relay.TupleGetItem(func_2337_call(), 0)
func_2378_call = mod.get_global_var('func_2378')
func_2380_call = mutated_mod.get_global_var('func_2380')
var_2863 = relay.var("var_2863", dtype = "float32", shape = (128,))#candidate|2863|(128,)|var|float32
call_2862 = func_2378_call(relay.reshape(var_2863.astype('float32'), [8, 1, 16]))
call_2864 = func_2378_call(relay.reshape(var_2863.astype('float32'), [8, 1, 16]))
output = relay.Tuple([call_2818,call_2862,var_2863,])
output2 = relay.Tuple([call_2819,call_2864,var_2863,])
func_2868 = relay.Function([var_2863,], output)
mod['func_2868'] = func_2868
mod = relay.transform.InferType()(mod)
var_2869 = relay.var("var_2869", dtype = "float32", shape = (128,))#candidate|2869|(128,)|var|float32
output = func_2868(var_2869)
func_2870 = relay.Function([var_2869], output)
mutated_mod['func_2870'] = func_2870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2883 = relay.TupleGetItem(func_2305_call(), 0)
call_2884 = relay.TupleGetItem(func_2307_call(), 0)
func_2135_call = mod.get_global_var('func_2135')
func_2139_call = mutated_mod.get_global_var('func_2139')
var_2886 = relay.var("var_2886", dtype = "uint16", shape = ())#candidate|2886|()|var|uint16
const_2887 = relay.const([5,-3,5,-6,-5,-3,3,-8,-5,-6,-2,-9,-8,10,2,-8,1,8,9,-2,-4,-9,5,6,6,10,-2,6,-4,4,2,-6,5,-8,7,9,7,6,5,-3,5,-9,-2,5,-1,-5,2,5,-5,-2,-5,4,6,5,4,-2,-1,6,-8,-3,-1,-2,-10,-10,10,-9,-10,-8,-5,-10,2,9,-7,-1,5,1,-2,9,-10,9,3,-6,1,1,-10,6,-7,5,8,-8,-10,1,4,6,-10,-5,-2,-6,-6,10,2,-7,-9,-2,10,1,8,4,1,5,6,4,10,1,-9,-3,-7,9,-5,-6,-10,7,-9,2,-2,1,7,-3,5,5,7,4,-8,-3,-3,-8,-5,3,-5,-2,-3,2,-8,9,3,9,1,5,6,4,6,-4,-6,-5,-3,-7,-9,8,-8,-3,10,10,-5,5,-4,3,-1,-10,-6,-8,-1,-5,6,10,-10,-2,4,6,-8,1,7,1,-10,5,-8,-5,7,-1,-3,6,3,6,1,-7,2,-2,-1,-9,6,7,6,-2,1,-6,2,10,4,-5,9,-6,1,1,1,-2,-3,-10,10,2,3,6,3,-5,1,4,3,2,-7,7,-3,6,10,7,-8,-1,-10,-8,-10,-10,4,-2,3,10,-7,10,8,7,2,5,-6,10,-3,9,-3,6,-4,-6,-10,-8,5,-8,6,8,1,7,-2,-5,7,-8,-4,8,3,-6,-2,2,4,8,-5,-9,2,6,-3,8,-7,-10,1,1,-4,8,1,1,10,-9,-6,3,-4,-1,-2,-9,-7,9,9,-1,7,8,9,-7,-9,-4,-5,-6,-8,10,-7,-10,-7,2,1,8,-5,7,-6,-3,-1,1,-3,-6,3,4,4,4,-5,7,4,-3,10,2,-2,-10,-1,-8,-9,9,2,-3,7,8,-6,5,8,8,8,3,-5,5,-5,2,9,5,-5,8,6,4,-8,-1,-9,-6,8,-8,-6,9,-8,-5,-4,-10,1,-1,-3,10,-3,10,1,-8,-9,2,-9,-5,3,8,4,-6,-6,-3,-1,-10,5,6,-10,-7,-1,2,-1,1,-1,-1,4,10,-4,1,-6,-10,3,-9,2,-1,4,-5,10,-10,2,6,1,-8,-6,2,9,3,10,6,7,-5,1,-7,-3,-4,10,-2,3,-8,8,1,2,1,5,5,5,4,-7,8,7,6,-1,10,8,-5,6,4,-1,3,2,-7,-6,-6,-1,7,-6,7,1,1,3,-4,1,8,-2,-7,9,-5,6,-9,4,7,9,9,-9,-9,-6,3,2,-1,-4,-1,4,-7,-5,-7,2,-1,8,-3,2,-1,-7,-8,-8,5,7,5,10,-2,-8,-6,-3,-3,10,-7,-2,-1,-3,-9,-9,-2,-10,8,9,-7,-6,-9,-1,-9,-10,3,7,10,4,2,6,10,3,6,-7,-10,5,4,-4,6,1,8,3,7,-9,-1,-5,9,-10,-9,-7,9,-8,7,-8,-8,10,9,3,-1,7,5,4,9,10,-10,-6,-6,-4,8,6,2,-1,-9,7,7,3,-5,8,2,1,-5,-1,-5,4,8,1,-5,-1,7,6,3,5,-10,-1,3,4,-10,10,1,-1,3,-9,6,-7,-9,6,4,-7,6,-7,-1,-8,-6,-8,-2,6,-3,-8,-6,-2,7,4,-9,8,-8,-8,-5,-1,5,-10,6,-4,2,8,6,10,5,-7,-4,4,9,2,-10,-9,-10,-2,6,7,-8,3,-2,7,6,6,8,-3,-3,5,7,6,4,6,-6,7,8,9,-2,9,-2,-9,4,9,6,-9,-9,-10,7,-10,-9,-8,-6,6,7,9,8,-10,-9,-10,-3,8,7,3,-4,-6,2,9,-5,10,-8,-9,-5,1,-8,-9,-9,2,-4,10,2,10,-2,-3,-4,8,2,-10,-6,2,-1,6,-7,8,5,-1,5,-2,2,3,10,10,9,-8,-1,1,-3,-4,5,-4,-1,7,8,-3,7,-6,7,7,-6,-3,7,-10,10,1,-9,4,-9,6,-4,-6,6,6,-10,1,9,-4,9,7,2,-3,-2,-1,-1,6,5,-4,8,4,4,5,-1,-2,-4,8,-6,9,9,6,-6,-5,8,3,9,3,5,9,-6,-6,1,-10,-8,-2,8,7,4,-6,1,-8,9,6,-1,1,7,10,5,4,9,-8,-5,1,-7,4,8,-10,5,-10,2,-4,1,8,3,7,9,-9,2,-6,8,-9,-1,-3,5,-1,-7,8,8,-3,-8,-1,8,1,-9,-1,6,3,-8,-2,-4,-2,9,-10,-7,-5,3,-4,-5,1,4,3,1,-7,-4,6,3,10,9,6,1,3,-9,-5,1,-10,-5,5,1,-8,1,5,-1,6,3,6,-5,-7,3,1,-7,1,6,-9,9,3,1,-6,3,4,7,-1,8,-7,10,-9,10,1,7,2,7,-8,3,5,-7,1,9,-6,-10,10,-2,-8,-10,-10,-9,2,8,-8,-3,7,2,-4,10,7,-7,-9,-7,-3,6,-3,6,2,-5,-6,-3,-10,3,-3,-6,-10,-1,-3,-7,-5,-2,9,4,-5,-2,-7,6,-8,-3,-9,-3,-3,-9,5,7,-9,10,8,-9,-3,3,-4,9,-7,4,3,-6,-4,-3,3,10,-8,1,-4,-10,-1,-1,4,-8,-4,9,-2,2,-4,-4,6,10,-4,-3,-1,-7,5,-1,8,2,-4,7,-9,-1,-7,-9,-10,-10,-10,-5,3,-5,-8,9,-6,9,-3,-3,7,-5,-10,9,1,-4,-2,4,-1,-4,-5,-6,-6,-10,-1,-9,-8,7,9,8,5,3,-1,3,-3,-10,1,-9,10,6,-2,-2,-9,8,4,8,-8,-9,7,8,10,-8,3,-10,7,-4,10,1,6,-7,-5,-2,-5,9,-4,4,4,-8,1,10,3,9,2,3,1,-8,5,9,-4,4,7,3,1,-8,1,-10,-2,8,-1,1,10,-8,1,7,-6,-5,-10,-4,-2,-1,8,7,-2,-3,-5,5,-4,-10,-10,2,9,-1,-4,8,-7,8,2,-5,-2,7,1,-3,-5,-1,2,-3], dtype = "uint16")#candidate|2887|(1152,)|const|uint16
const_2888 = relay.const([-2,8,10,10,-1,5,7,4,-7,6,-1,-4,9,6,-9,-7,7,-10,3,6,2,-3,3,3,-4,9,-3,10,1,4,-10,-10,10,-5,-9,8,6,-10,-9,-6,-1,2,8,-6,9,-8,2,-7,9,5,5,-9,5,2,2,8,-5,-9,-2,1,-6,-10,8,-1,9,4,9,9,-5,-7,8,-4,4,5,8,-7,6,3,3,10,-1,-8,-10,-4,7,-5,9,-6,-3,-10,9,-7,3,9,-7,-9,-5,-9,-5,3,-8,-5,-8,-1,3,3,-9,5,2,9,4,8,-7,6,9,2,-8,4,9,6,-7,2,-1,9,4,5,-9,9,7,8,5,-5,8,-10,5,8,4,9,10,9,9,4,-6,-4,8,-10,3,-9,-5,9,-2,-3,1,-2,-3,7,-4,9,-3,2,4,-6,9,7,4,-5,5,5,-1,8,-9,-5,-5,-4,7,10,9,-8,3,4,3,4,-9,-5,7,6,8,8,8,-2,7,8,-1,-6,-4,-2,10,-9,8,-1,7,8,9,-9,-7,1,4,-3,8,9,-10,10,-8,10,3,8,9,3,3,4,-2,7,-4,9,10,3,9,-3,-2,-5,-4,-3,1,8,8,6,-7,-6,-1,-5,2,-2,-1,10,-8,6,-9,5,-7,-4,7,6,2,6,-8,-6,-9,3,-5,-3,9,-7,2,-8,6,-5,1,8,-5,7,-7,6,-1,-6,-6,-9,10,-5,9,1,-3,-8,-8,-8,-5,8,7,-8,7,-7,4,-9,-4,-9,6,-8,-6,5,-5,9,-7,-1,-5,5,4,-4,-7,-5,5,-2,3,2,-8,-5,2,-2,5,5,2,-9,-1,-5,5,-9,-3,1,-3,-5,-2,4,8,-4,1,2,-1,-2,-5,-1,6,-1,3,4,5,-6,4,10,8,-5,-5,-2,10,-9,10,5,9,4,-8,-9,10,9,-5,-5,4,2,9,-4,-8,7,-2,-4,8,5,6,10,-1,-7,-9,1,-4,-1,-7,-5,-9,-4,5,-5,4,1,-6,-6,-10,-3,-5,2,-7,4,9,2,-10,-2,2,9,7,-6,1,-2,-4,9,9,-1,-6,4,-6,5,1,-2,5,1,-9,7,-10,2,3,-5,3,-3,-3,-4,3,5,-9,9,6,7,6,7,4,9,-1,4,-10,-2,-3,-2,-8,-10,-3,2,-8,7,5,-9,-5,8,3,-9,6,8,10,6,8,-6,5,-10,-6,-7,3,10,4,-4,-8,10,4,5,-7,-3,-7,5,6,-2,-4,-1,-5,-7,-9,-6,3,2,5,1,-8,-6,-3,4,-8,-10,-7,3,6,-1,-2,3,-4,-3], dtype = "int64")#candidate|2888|(504,)|const|int64
call_2885 = relay.TupleGetItem(func_2135_call(relay.reshape(var_2886.astype('uint16'), []), relay.reshape(const_2887.astype('uint16'), [6, 16, 12]), relay.reshape(const_2888.astype('int64'), [504,]), ), 3)
call_2889 = relay.TupleGetItem(func_2139_call(relay.reshape(var_2886.astype('uint16'), []), relay.reshape(const_2887.astype('uint16'), [6, 16, 12]), relay.reshape(const_2888.astype('int64'), [504,]), ), 3)
func_2135_call = mod.get_global_var('func_2135')
func_2139_call = mutated_mod.get_global_var('func_2139')
call_2890 = relay.TupleGetItem(func_2135_call(relay.reshape(var_2886.astype('uint16'), []), relay.reshape(const_2887.astype('uint16'), [6, 16, 12]), relay.reshape(const_2888.astype('int64'), [504,]), ), 1)
call_2891 = relay.TupleGetItem(func_2139_call(relay.reshape(var_2886.astype('uint16'), []), relay.reshape(const_2887.astype('uint16'), [6, 16, 12]), relay.reshape(const_2888.astype('int64'), [504,]), ), 1)
output = relay.Tuple([call_2883,call_2885,var_2886,const_2887,const_2888,call_2890,])
output2 = relay.Tuple([call_2884,call_2889,var_2886,const_2887,const_2888,call_2891,])
func_2900 = relay.Function([var_2886,], output)
mod['func_2900'] = func_2900
mod = relay.transform.InferType()(mod)
var_2901 = relay.var("var_2901", dtype = "uint16", shape = ())#candidate|2901|()|var|uint16
output = func_2900(var_2901)
func_2902 = relay.Function([var_2901], output)
mutated_mod['func_2902'] = func_2902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_2960 = func_2513_call()
call_2961 = func_2513_call()
output = call_2960
output2 = call_2961
func_2964 = relay.Function([], output)
mod['func_2964'] = func_2964
mod = relay.transform.InferType()(mod)
output = func_2964()
func_2965 = relay.Function([], output)
mutated_mod['func_2965'] = func_2965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_2994 = func_2513_call()
call_2995 = func_2513_call()
func_2900_call = mod.get_global_var('func_2900')
func_2902_call = mutated_mod.get_global_var('func_2902')
var_2999 = relay.var("var_2999", dtype = "uint16", shape = ())#candidate|2999|()|var|uint16
call_2998 = relay.TupleGetItem(func_2900_call(relay.reshape(var_2999.astype('uint16'), [])), 3)
call_3000 = relay.TupleGetItem(func_2902_call(relay.reshape(var_2999.astype('uint16'), [])), 3)
bop_3004 = relay.divide(var_2999.astype('float32'), call_2994.astype('float32')) # shape=(8, 1, 5)
bop_3007 = relay.divide(var_2999.astype('float32'), call_2995.astype('float32')) # shape=(8, 1, 5)
uop_3012 = relay.log(bop_3004.astype('float32')) # shape=(8, 1, 5)
uop_3014 = relay.log(bop_3007.astype('float32')) # shape=(8, 1, 5)
output = relay.Tuple([call_2998,uop_3012,])
output2 = relay.Tuple([call_3000,uop_3014,])
func_3019 = relay.Function([var_2999,], output)
mod['func_3019'] = func_3019
mod = relay.transform.InferType()(mod)
var_3020 = relay.var("var_3020", dtype = "uint16", shape = ())#candidate|3020|()|var|uint16
output = func_3019(var_3020)
func_3021 = relay.Function([var_3020], output)
mutated_mod['func_3021'] = func_3021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_3075 = func_2513_call()
call_3076 = func_2513_call()
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_3082 = func_2513_call()
call_3083 = func_2513_call()
func_2964_call = mod.get_global_var('func_2964')
func_2965_call = mutated_mod.get_global_var('func_2965')
call_3099 = func_2964_call()
call_3100 = func_2964_call()
var_3109 = relay.var("var_3109", dtype = "float32", shape = (8, 3, 5))#candidate|3109|(8, 3, 5)|var|float32
bop_3110 = relay.maximum(call_3082.astype('int16'), var_3109.astype('int16')) # shape=(8, 3, 5)
bop_3113 = relay.maximum(call_3083.astype('int16'), var_3109.astype('int16')) # shape=(8, 3, 5)
bop_3118 = relay.left_shift(call_3082.astype('int16'), relay.reshape(call_3099.astype('int16'), relay.shape_of(call_3082))) # shape=(8, 1, 5)
bop_3121 = relay.left_shift(call_3083.astype('int16'), relay.reshape(call_3100.astype('int16'), relay.shape_of(call_3083))) # shape=(8, 1, 5)
output = relay.Tuple([call_3075,bop_3110,bop_3118,])
output2 = relay.Tuple([call_3076,bop_3113,bop_3121,])
func_3124 = relay.Function([var_3109,], output)
mod['func_3124'] = func_3124
mod = relay.transform.InferType()(mod)
var_3125 = relay.var("var_3125", dtype = "float32", shape = (8, 3, 5))#candidate|3125|(8, 3, 5)|var|float32
output = func_3124(var_3125)
func_3126 = relay.Function([var_3125], output)
mutated_mod['func_3126'] = func_3126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2571_call = mod.get_global_var('func_2571')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_3176 = relay.TupleGetItem(func_2571_call(), 0)
call_3177 = relay.TupleGetItem(func_2572_call(), 0)
func_2135_call = mod.get_global_var('func_2135')
func_2139_call = mutated_mod.get_global_var('func_2139')
const_3182 = relay.const(10, dtype = "uint16")#candidate|3182|()|const|uint16
const_3183 = relay.const([8,10,3,1,4,5,7,3,2,7,-9,-2,-1,-10,-9,-8,9,4,3,-7,7,10,-6,9,-3,1,7,10,-6,-10,9,2,5,2,-1,-7,-3,-2,2,-4,8,-8,1,-5,-10,2,5,9,-9,-10,-2,-1,-3,-3,-4,9,-4,-1,5,-2,2,-6,9,9,-8,10,-5,4,-4,1,4,4,-9,3,-10,10,-10,-1,2,8,-10,-2,7,-10,-3,-1,-3,6,-9,-5,-5,-2,-1,-3,4,5,-10,-8,-2,-10,-9,3,7,3,10,4,5,10,1,-9,7,-1,-10,7,-7,-9,9,8,5,1,-3,1,-5,4,-8,-2,-8,3,-2,-1,7,-5,6,-4,7,6,-4,-8,10,4,-4,3,1,-1,6,2,-6,4,2,-2,-5,9,-5,-6,-8,1,9,5,1,5,-9,-3,-3,8,-4,4,-9,7,-9,-9,5,10,-5,6,-2,3,7,8,-10,-7,7,2,-6,9,5,-4,-7,6,9,6,-6,-3,-3,-5,7,9,-5,9,-1,-7,-6,7,-5,-3,-9,-6,-8,-10,-1,-5,-6,4,5,-3,4,5,2,3,-8,-2,7,-2,10,-7,-6,9,9,5,9,-2,-9,4,10,-9,-6,-5,-2,10,-10,10,1,10,-7,4,5,10,3,-7,3,-1,-6,2,3,9,8,9,-1,7,-6,-3,-9,6,10,6,7,2,4,-3,-7,2,10,-5,10,10,-5,6,-9,-5,-4,-10,-8,6,8,1,-10,1,4,-4,7,8,-8,-5,7,-3,1,-3,8,5,9,-1,8,-2,5,-7,-9,-6,1,1,1,10,7,-3,3,1,5,-4,4,-5,1,3,9,6,-9,8,10,4,-1,4,-6,-7,-7,-3,-8,-1,-4,-8,4,-1,-10,-4,6,8,4,3,-7,10,3,4,-6,10,-9,-3,2,-7,4,3,-9,9,-2,-5,3,2,3,-7,3,8,-8,5,6,2,-5,-2,-5,2,-3,8,-4,-2,-8,-5,8,3,6,-6,1,-2,3,3,-5,7,1,4,6,2,8,-5,3,-4,5,3,8,-2,-3,10,1,-6,3,-8,9,-4,-7,5,8,-3,9,-9,-5,-9,10,-6,7,1,-3,10,9,1,5,-10,-5,-8,-10,1,-9,-4,10,-10,-4,-6,2,-1,9,10,9,-9,-2,-1,3,10,4,3,-5,-8,7,-6,-9,-1,2,-6,-9,7,1,6,10,10,-1,6,7,5,-10,-3,1,-9,3,-3,-10,8,6,9,-1,10,1,9,1,-2,-6,-10,-8,9,-6,-8,3,-10,-9,7,-8,-1,4,-7,-6,8,7,-9,8,-8,2,-3,-3,6,-1,-1,1,-8,-4,1,-5,1,8,-6,-10,3,4,9,-8,-7,-7,8,2,10,-10,-5,-10,8,8,4,-2,-2,-2,2,-3,9,-1,5,-10,1,-7,-6,5,-5,-7,1,-8,4,1,10,-8,3,3,-3,4,-2,8,-10,-1,6,-5,-7,-9,3,-8,-5,9,6,-7,-4,10,-1,-5,3,-5,-3,-5,3,1,7,6,-8,9,6,10,6,5,8,8,5,-10,4,-7,1,-3,-9,-10,4,8,5,8,-8,9,-5,7,2,6,-5,3,3,6,-2,9,-8,-6,7,-6,-8,-10,4,1,-5,10,-10,-5,8,4,-8,8,10,-10,-7,-1,-1,-8,-8,-9,-5,-2,3,-7,9,-2,4,4,3,10,-10,5,-2,4,-1,3,-5,9,4,-10,-9,3,-2,7,1,-5,10,2,-2,-4,-1,-9,3,4,-5,-2,7,-8,-4,-6,4,-6,3,8,4,10,-10,4,6,3,-2,-6,2,-10,8,-1,-7,-7,-5,-6,9,-8,5,-2,-10,2,10,3,-1,8,10,2,-6,-10,5,2,3,1,-10,9,-10,3,9,1,2,-9,-9,-2,9,-6,9,6,-9,-10,-2,10,9,1,1,10,-3,8,10,-7,-3,1,2,-3,-8,2,9,-1,5,-8,6,-2,7,-1,9,5,-10,1,6,4,7,4,-8,-6,-9,-9,-2,-3,10,-5,-3,-8,-7,-6,-7,4,8,9,5,7,2,8,-9,-3,7,6,6,-3,-7,3,3,7,7,5,3,-5,-10,-9,6,-7,-7,2,-1,6,8,-3,9,10,7,-10,-7,-7,8,5,-7,-6,5,10,7,-5,5,3,7,-4,7,7,10,3,2,-1,-10,3,-9,3,-7,8,-4,10,4,-8,-9,-9,8,7,7,9,9,5,3,3,-6,-5,-3,4,10,-10,-6,8,-8,4,-2,-5,4,-8,-9,10,1,-6,2,-2,9,-1,-1,-8,1,6,-6,-4,-4,9,3,-7,-7,-7,-10,-1,-10,-3,-1,-10,3,-8,1,-9,-6,6,-10,-4,-5,-7,-9,-3,1,2,7,6,9,8,6,3,-8,1,-4,-6,-5,6,-1,7,-7,6,8,-3,-4,7,10,1,-2,5,-7,-7,-4,-10,-3,9,-3,-3,4,10,-9,-9,-10,7,3,8,-5,-4,-9,5,1,-2,-8,-7,-1,2,5,-8,-2,-5,-7,6,-9,2,-7,9,-3,-2,6,-7,8,8,1,-6,-1,7,-7,1,-5,3,-1,10,1,-9,3,5,-5,3,-9,10,-4,-9,2,-7,4,-7,-2,3,10,2,7,-5,10,-10,-8,10,-7,-5,10,4,-1,1,1,-7,-7,4,-8,-8,-6,-9,9,8,-2,-5,-4,8,-3,9,4,-6,-6,-3,-9,3,1,10,3,8,-1,-8,3,10,-7,-1,-4,-10,-7,-7,5,-2,3,-6,1,4,6,-7,-9,8,-6,5,-8,-2,-9,1,-8,10,-8,10,10,-1,5,7,7,-10,-4,4,-1,7,7,3,3,-9,-2,10,2,-10,1,10,3,-2,-4,-9,3,4,5,7,3,-1,-4,8,-4,2,-8,-7,2,-9,6,-3,7,-10,5,2,-3,4,4,5,2,7,-10,2,2,10,3,-6,1,3,-5,-3,-6,8,-8,-1,-10,2,-3,-4,10,-2,7,5,5,-3,1,-9,-4,-10,-1,5,-9], dtype = "uint16")#candidate|3183|(1152,)|const|uint16
const_3184 = relay.const([-5,-6,9,10,-7,-6,-1,3,9,-10,2,-7,10,4,1,1,2,-1,-5,-1,-3,5,7,7,-1,-1,8,-5,10,-10,-7,-6,-8,2,-7,-4,-9,6,8,-4,-2,-1,2,1,-9,2,-1,7,-5,-3,-1,3,-7,-9,-6,-1,9,1,1,-3,4,-6,-4,-6,-3,1,7,5,-5,-6,-9,-9,2,10,-3,-6,8,6,7,9,3,4,-6,-4,3,-1,-1,-3,-2,8,3,6,6,-3,4,-2,2,6,5,8,-2,-2,-1,5,7,-3,-7,-2,-9,-7,7,-1,-5,8,9,-10,4,5,9,3,5,-6,2,-5,-3,5,2,-2,3,7,-3,-4,-8,-6,-8,3,-2,-6,-7,7,-5,-1,-10,-6,-10,-4,9,-3,6,-6,-8,-10,5,9,10,1,10,-4,6,3,4,-2,5,2,5,-8,4,-5,5,-1,10,10,-8,10,6,-2,1,3,-9,7,-10,9,2,-3,8,2,9,-7,6,-1,-1,3,6,7,-1,-9,1,5,4,2,5,9,6,9,5,8,-10,9,-7,1,-3,8,-10,1,2,-5,9,-9,10,-1,-7,-3,10,-4,8,-6,8,9,9,-4,-5,-8,-5,-1,6,-1,1,-1,-6,9,-10,9,10,-10,7,-10,4,-7,6,3,-2,-4,-8,5,9,10,-10,9,-6,-9,-4,-5,6,7,-2,1,-7,-6,-9,9,-4,7,-7,-3,9,5,-8,4,-2,5,3,9,-2,-5,7,-9,4,-4,4,5,7,7,-10,-1,-3,-8,4,-6,-4,9,8,10,-4,4,-2,-1,9,-6,8,1,4,8,9,-6,9,-2,-1,-9,-1,-5,2,-1,4,7,-5,-3,-2,-8,-7,3,10,-2,-10,-8,-4,3,6,4,-3,2,-3,-6,-8,-3,-9,-2,4,1,-5,-6,-1,2,4,7,-10,5,8,8,8,-4,10,7,9,7,-7,2,1,-5,-3,10,5,-7,-9,-10,8,5,9,-1,1,4,-10,-8,-4,4,7,-1,1,5,4,-8,-9,-2,6,9,-1,5,-1,2,8,-3,4,-7,-5,-7,-10,-3,10,9,1,3,-3,5,3,-1,7,-6,-9,8,-7,-5,1,-8,-5,5,7,10,-8,3,-6,10,10,4,9,5,6,3,-10,-8,-9,3,-3,-5,-1,10,-5,-9,-8,-6,5,-5,1,-10,-10,-8,-1,5,7,5,-8,-5,7,10,9,6,-5,-6,-8,1,-5,7,1,10,-3,8,-1,-6,7,8,2,-9,-3,-5,-9,9,5,-10,1,8,8,-7,9,9,-9,-1,1,10,-4,4,-1,-9,-2,-7,-2,9], dtype = "int64")#candidate|3184|(504,)|const|int64
call_3181 = relay.TupleGetItem(func_2135_call(relay.reshape(const_3182.astype('uint16'), []), relay.reshape(const_3183.astype('uint16'), [6, 16, 12]), relay.reshape(const_3184.astype('int64'), [504,]), ), 0)
call_3185 = relay.TupleGetItem(func_2139_call(relay.reshape(const_3182.astype('uint16'), []), relay.reshape(const_3183.astype('uint16'), [6, 16, 12]), relay.reshape(const_3184.astype('int64'), [504,]), ), 0)
uop_3203 = relay.atanh(call_3176.astype('float64')) # shape=(8, 1, 5)
uop_3205 = relay.atanh(call_3177.astype('float64')) # shape=(8, 1, 5)
output = relay.Tuple([call_3181,const_3182,const_3183,const_3184,uop_3203,])
output2 = relay.Tuple([call_3185,const_3182,const_3183,const_3184,uop_3205,])
func_3229 = relay.Function([], output)
mod['func_3229'] = func_3229
mod = relay.transform.InferType()(mod)
mutated_mod['func_3229'] = func_3229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3229_call = mutated_mod.get_global_var('func_3229')
call_3230 = func_3229_call()
output = call_3230
func_3231 = relay.Function([], output)
mutated_mod['func_3231'] = func_3231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_3287 = relay.TupleGetItem(func_2305_call(), 0)
call_3288 = relay.TupleGetItem(func_2307_call(), 0)
func_2964_call = mod.get_global_var('func_2964')
func_2965_call = mutated_mod.get_global_var('func_2965')
call_3289 = func_2964_call()
call_3290 = func_2964_call()
output = relay.Tuple([call_3287,call_3289,])
output2 = relay.Tuple([call_3288,call_3290,])
func_3298 = relay.Function([], output)
mod['func_3298'] = func_3298
mod = relay.transform.InferType()(mod)
output = func_3298()
func_3299 = relay.Function([], output)
mutated_mod['func_3299'] = func_3299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3229_call = mod.get_global_var('func_3229')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_3355 = relay.TupleGetItem(func_3229_call(), 3)
call_3356 = relay.TupleGetItem(func_3231_call(), 3)
output = call_3355
output2 = call_3356
func_3405 = relay.Function([], output)
mod['func_3405'] = func_3405
mod = relay.transform.InferType()(mod)
output = func_3405()
func_3406 = relay.Function([], output)
mutated_mod['func_3406'] = func_3406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2337_call = mutated_mod.get_global_var('func_2337')
call_3461 = relay.TupleGetItem(func_2336_call(), 0)
call_3462 = relay.TupleGetItem(func_2337_call(), 0)
output = call_3461
output2 = call_3462
func_3475 = relay.Function([], output)
mod['func_3475'] = func_3475
mod = relay.transform.InferType()(mod)
output = func_3475()
func_3476 = relay.Function([], output)
mutated_mod['func_3476'] = func_3476
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3477 = relay.var("var_3477", dtype = "float64", shape = (16, 9, 14))#candidate|3477|(16, 9, 14)|var|float64
uop_3478 = relay.atanh(var_3477.astype('float64')) # shape=(16, 9, 14)
func_2571_call = mod.get_global_var('func_2571')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_3485 = relay.TupleGetItem(func_2571_call(), 0)
call_3486 = relay.TupleGetItem(func_2572_call(), 0)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_3488 = func_2513_call()
call_3489 = func_2513_call()
bop_3505 = relay.minimum(uop_3478.astype('int64'), relay.reshape(var_3477.astype('int64'), relay.shape_of(uop_3478))) # shape=(16, 9, 14)
output = relay.Tuple([call_3485,call_3488,bop_3505,])
output2 = relay.Tuple([call_3486,call_3489,bop_3505,])
func_3508 = relay.Function([var_3477,], output)
mod['func_3508'] = func_3508
mod = relay.transform.InferType()(mod)
var_3509 = relay.var("var_3509", dtype = "float64", shape = (16, 9, 14))#candidate|3509|(16, 9, 14)|var|float64
output = func_3508(var_3509)
func_3510 = relay.Function([var_3509], output)
mutated_mod['func_3510'] = func_3510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2964_call = mod.get_global_var('func_2964')
func_2965_call = mutated_mod.get_global_var('func_2965')
call_3607 = func_2964_call()
call_3608 = func_2964_call()
const_3627 = relay.const([[[-1.111199,9.886853,-9.070435,2.855349,5.330172],[5.143353,1.814687,-1.811480,8.180049,6.390234],[-3.000462,-1.368075,-2.995901,-4.886847,7.595606]],[[4.846597,-4.318246,-4.677986,-9.157361,4.338675],[-7.454423,2.438117,-4.951136,-2.039199,-7.918064],[0.828130,6.465974,-7.911505,-2.892025,-8.521448]],[[-0.907978,2.951423,-3.609570,4.212808,5.900307],[-5.140142,9.386838,3.179610,1.932805,-3.504584],[4.797589,-3.746470,1.118219,-9.062005,9.789752]],[[4.760425,-1.132657,-9.179479,-5.782962,7.874750],[-5.664284,8.904656,9.756280,7.799926,1.351755],[8.606501,1.083903,7.374708,-6.782911,-2.656669]],[[-3.253152,7.034343,-3.536481,0.150742,3.229007],[-2.789618,-1.269735,-0.914901,-1.326521,-7.338062],[1.484843,1.294023,4.398479,9.821218,-5.080287]],[[4.077783,1.287513,-9.374134,9.074172,-9.484859],[-1.356548,-1.308079,9.876924,6.150860,1.874941],[2.827867,0.849739,0.060953,8.595087,-4.845220]],[[2.313527,0.164001,-7.786984,-7.346297,3.549932],[-8.576888,-8.813621,0.196594,0.855411,8.817614],[-5.204143,1.770056,6.883822,6.261437,2.900138]],[[5.573517,6.122019,1.545357,-3.215803,9.642364],[9.204173,0.250022,4.984112,8.360824,0.326468],[2.280207,3.728556,2.312786,1.325025,3.210543]]], dtype = "float32")#candidate|3627|(8, 3, 5)|const|float32
bop_3628 = relay.logical_and(call_3607.astype('bool'), const_3627.astype('bool')) # shape=(8, 3, 5)
bop_3631 = relay.logical_and(call_3608.astype('bool'), const_3627.astype('bool')) # shape=(8, 3, 5)
output = bop_3628
output2 = bop_3631
func_3632 = relay.Function([], output)
mod['func_3632'] = func_3632
mod = relay.transform.InferType()(mod)
mutated_mod['func_3632'] = func_3632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3632_call = mutated_mod.get_global_var('func_3632')
call_3633 = func_3632_call()
output = call_3633
func_3634 = relay.Function([], output)
mutated_mod['func_3634'] = func_3634
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3667 = relay.const(-5.227229, dtype = "float32")#candidate|3667|()|const|float32
var_3668 = relay.var("var_3668", dtype = "float32", shape = (6, 4, 5))#candidate|3668|(6, 4, 5)|var|float32
bop_3669 = relay.floor_mod(const_3667.astype('float32'), var_3668.astype('float32')) # shape=(6, 4, 5)
uop_3673 = relay.rsqrt(bop_3669.astype('float64')) # shape=(6, 4, 5)
output = uop_3673
output2 = uop_3673
func_3675 = relay.Function([var_3668,], output)
mod['func_3675'] = func_3675
mod = relay.transform.InferType()(mod)
var_3676 = relay.var("var_3676", dtype = "float32", shape = (6, 4, 5))#candidate|3676|(6, 4, 5)|var|float32
output = func_3675(var_3676)
func_3677 = relay.Function([var_3676], output)
mutated_mod['func_3677'] = func_3677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2337_call = mutated_mod.get_global_var('func_2337')
call_3693 = relay.TupleGetItem(func_2336_call(), 0)
call_3694 = relay.TupleGetItem(func_2337_call(), 0)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_3707 = relay.TupleGetItem(func_2305_call(), 0)
call_3708 = relay.TupleGetItem(func_2307_call(), 0)
output = relay.Tuple([call_3693,call_3707,])
output2 = relay.Tuple([call_3694,call_3708,])
func_3726 = relay.Function([], output)
mod['func_3726'] = func_3726
mod = relay.transform.InferType()(mod)
output = func_3726()
func_3727 = relay.Function([], output)
mutated_mod['func_3727'] = func_3727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_3761 = relay.TupleGetItem(func_2813_call(), 1)
call_3762 = relay.TupleGetItem(func_2814_call(), 1)
const_3764 = relay.const([[[-4.125586,6.398110,4.620518,6.395567,-8.779250],[2.601889,1.391667,7.917435,3.640115,8.428243],[5.890786,6.485648,1.186320,9.380355,4.304126],[3.193087,-2.891248,1.109564,5.339896,-4.803125],[9.531709,-7.533735,3.884986,-9.600813,-8.252632],[-6.410445,-6.887330,-0.570450,-2.750963,-6.788913],[-8.137880,3.797759,1.898083,-7.015290,0.400453],[-1.153959,-5.459323,-7.471136,8.831969,5.538674],[-9.847762,6.481513,5.997194,-0.778758,1.804091]],[[3.249105,-5.207331,-8.522128,6.095257,7.996593],[-9.736133,8.338505,-2.117670,-0.958003,-5.535875],[0.504559,2.206307,1.388111,-5.517720,-4.702227],[-7.930730,-9.454659,7.014854,-9.940017,8.444975],[0.641900,-1.859641,1.517035,-3.305918,-3.142479],[7.033101,3.728154,-0.808704,3.549908,-1.059754],[-6.844660,5.607485,-5.570102,3.848993,7.572149],[-9.695807,-5.766977,6.608734,8.452344,2.787680],[-0.140240,8.110314,3.516726,-6.899331,-2.533752]],[[2.569470,4.543317,1.058117,8.673833,6.536912],[-9.517258,5.003432,-7.415696,-0.928303,3.719699],[5.185960,-8.173704,0.818533,-9.391788,-7.696900],[6.006689,4.392490,-4.926141,-4.491077,0.420946],[-1.226117,4.766789,4.157743,-9.632210,4.352431],[3.059903,7.744754,8.379912,-4.999308,-8.338991],[-4.587322,-1.326730,-9.472666,8.597405,-9.932499],[-3.199787,-7.100570,-6.166879,3.262790,8.595670],[-1.875777,3.947729,-1.439469,1.056843,-1.502658]],[[3.882724,0.897106,-9.302424,-2.215633,-8.979953],[5.525976,9.228568,-3.481680,4.770564,-8.003559],[-2.431301,9.487232,-8.514675,-6.557572,-1.083613],[4.843589,0.421295,2.585471,-7.225648,4.763246],[-0.391284,-0.462869,-5.930629,-0.137548,-6.165053],[-3.715313,7.270953,0.181999,5.741160,6.005127],[-8.573484,1.589356,3.987738,-2.046377,-5.718207],[-3.728471,-7.868103,-9.040952,0.858398,-7.855726],[7.186940,-9.672816,-1.725087,-3.035898,6.284926]],[[-3.383679,-3.021909,-6.053575,-2.466827,-1.198655],[-6.768229,-7.201429,3.205756,-0.933571,5.653214],[-2.968881,9.936422,5.373855,-0.660018,-5.579539],[-8.465588,-6.252778,-1.760242,-2.637999,4.861388],[-9.708121,-0.491260,-9.914298,0.898539,-1.274371],[7.906453,-2.587743,-0.827095,-1.887229,2.731343],[-4.373243,9.788797,5.599669,2.347386,8.330347],[-0.092198,6.428749,-4.714870,-6.400463,-8.941571],[-2.762712,4.804672,-1.834917,-9.887202,5.900275]],[[9.481607,7.430459,-6.873111,6.245157,0.622119],[-1.449835,-9.033294,-2.888286,3.022057,-2.656724],[9.173707,5.552389,6.734776,-7.861723,-3.207421],[-0.434409,-0.627407,9.788892,-3.696635,-6.072904],[3.178916,0.276182,-2.100681,-9.747411,-2.974161],[8.679578,2.629767,-2.202909,0.003119,-7.188468],[-9.072178,1.801597,4.967050,4.827517,2.971653],[1.987947,-8.275383,-5.025539,-0.656046,-4.418016],[-2.108348,-8.164909,-5.674819,-2.186137,-2.568063]],[[-8.100130,5.182723,6.600057,-2.322697,-7.783217],[-9.303661,-8.099825,-4.612897,-9.791036,2.241027],[0.186597,-9.282361,1.781552,5.682187,-1.974822],[-1.193453,-9.776721,8.125755,-9.118918,5.726622],[3.366799,-3.938593,-2.348607,4.466844,6.413248],[-3.394179,-7.852445,3.754986,7.233740,3.658426],[-0.440912,-0.143687,-6.000206,-3.858815,4.376500],[9.273391,6.636041,-5.874006,7.260893,-5.651778],[-5.453675,2.281694,-2.676632,-6.638906,4.353973]],[[5.889216,-1.373688,5.398811,9.693044,2.123596],[4.762668,-1.829987,1.855613,-5.330605,-3.357956],[3.132175,5.553796,5.161300,5.972724,-9.080244],[8.433160,-9.588357,8.720375,-7.353892,6.675764],[-2.147522,7.769863,-9.849328,4.996353,2.205540],[7.497282,4.580357,9.470280,-9.250942,-2.998342],[-7.826601,7.698697,2.320215,-9.147109,2.442962],[-2.338974,-7.857217,-1.763796,-8.046365,7.595837],[5.667277,-4.367980,-8.816176,6.982350,3.993907]]], dtype = "float32")#candidate|3764|(8, 9, 5)|const|float32
bop_3765 = relay.left_shift(call_3761.astype('uint64'), const_3764.astype('uint64')) # shape=(8, 9, 5)
bop_3768 = relay.left_shift(call_3762.astype('uint64'), const_3764.astype('uint64')) # shape=(8, 9, 5)
func_2442_call = mod.get_global_var('func_2442')
func_2445_call = mutated_mod.get_global_var('func_2445')
var_3776 = relay.var("var_3776", dtype = "float32", shape = (1134,))#candidate|3776|(1134,)|var|float32
call_3775 = relay.TupleGetItem(func_2442_call(relay.reshape(var_3776.astype('float32'), [1134,])), 1)
call_3777 = relay.TupleGetItem(func_2445_call(relay.reshape(var_3776.astype('float32'), [1134,])), 1)
output = relay.Tuple([bop_3765,call_3775,var_3776,])
output2 = relay.Tuple([bop_3768,call_3777,var_3776,])
func_3778 = relay.Function([var_3776,], output)
mod['func_3778'] = func_3778
mod = relay.transform.InferType()(mod)
var_3779 = relay.var("var_3779", dtype = "float32", shape = (1134,))#candidate|3779|(1134,)|var|float32
output = func_3778(var_3779)
func_3780 = relay.Function([var_3779], output)
mutated_mod['func_3780'] = func_3780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3800 = relay.var("var_3800", dtype = "float64", shape = (7, 14, 14))#candidate|3800|(7, 14, 14)|var|float64
uop_3801 = relay.log10(var_3800.astype('float64')) # shape=(7, 14, 14)
output = relay.Tuple([uop_3801,])
output2 = relay.Tuple([uop_3801,])
func_3805 = relay.Function([var_3800,], output)
mod['func_3805'] = func_3805
mod = relay.transform.InferType()(mod)
var_3806 = relay.var("var_3806", dtype = "float64", shape = (7, 14, 14))#candidate|3806|(7, 14, 14)|var|float64
output = func_3805(var_3806)
func_3807 = relay.Function([var_3806], output)
mutated_mod['func_3807'] = func_3807
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3896 = relay.const([[[6,-1,3,-1,-6],[5,10,7,8,-2],[9,7,-5,9,9]],[[-3,-9,7,2,-9],[8,-4,-7,-2,7],[5,1,1,1,3]],[[-4,-6,-1,-7,3],[-1,1,1,-6,-2],[6,-10,1,2,5]],[[-3,-2,-2,-4,-5],[-2,-7,-2,10,3],[3,-1,-6,-6,4]],[[4,10,6,10,-10],[8,1,-6,6,-1],[10,-10,-6,-3,7]],[[-6,5,-8,8,3],[-2,2,6,4,-4],[3,-8,-4,1,1]],[[-5,8,4,2,-5],[2,8,1,-9,-10],[-2,6,-7,-6,-10]]], dtype = "uint64")#candidate|3896|(7, 3, 5)|const|uint64
var_3897 = relay.var("var_3897", dtype = "uint64", shape = (7, 3, 5))#candidate|3897|(7, 3, 5)|var|uint64
bop_3898 = relay.logical_xor(const_3896.astype('uint64'), relay.reshape(var_3897.astype('uint64'), relay.shape_of(const_3896))) # shape=(7, 3, 5)
bop_3908 = relay.add(var_3897.astype('uint64'), relay.reshape(bop_3898.astype('uint64'), relay.shape_of(var_3897))) # shape=(7, 3, 5)
uop_3914 = relay.log2(bop_3908.astype('float32')) # shape=(7, 3, 5)
output = relay.Tuple([uop_3914,])
output2 = relay.Tuple([uop_3914,])
func_3917 = relay.Function([var_3897,], output)
mod['func_3917'] = func_3917
mod = relay.transform.InferType()(mod)
var_3918 = relay.var("var_3918", dtype = "uint64", shape = (7, 3, 5))#candidate|3918|(7, 3, 5)|var|uint64
output = func_3917(var_3918)
func_3919 = relay.Function([var_3918], output)
mutated_mod['func_3919'] = func_3919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2964_call = mod.get_global_var('func_2964')
func_2965_call = mutated_mod.get_global_var('func_2965')
call_3973 = func_2964_call()
call_3974 = func_2964_call()
var_3985 = relay.var("var_3985", dtype = "float32", shape = (8, 8, 5))#candidate|3985|(8, 8, 5)|var|float32
bop_3986 = relay.minimum(call_3973.astype('uint32'), var_3985.astype('uint32')) # shape=(8, 8, 5)
bop_3989 = relay.minimum(call_3974.astype('uint32'), var_3985.astype('uint32')) # shape=(8, 8, 5)
output = relay.Tuple([bop_3986,])
output2 = relay.Tuple([bop_3989,])
func_3990 = relay.Function([var_3985,], output)
mod['func_3990'] = func_3990
mod = relay.transform.InferType()(mod)
mutated_mod['func_3990'] = func_3990
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3991 = relay.var("var_3991", dtype = "float32", shape = (8, 8, 5))#candidate|3991|(8, 8, 5)|var|float32
func_3990_call = mutated_mod.get_global_var('func_3990')
call_3992 = func_3990_call(var_3991)
output = call_3992
func_3993 = relay.Function([var_3991], output)
mutated_mod['func_3993'] = func_3993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3726_call = mod.get_global_var('func_3726')
func_3727_call = mutated_mod.get_global_var('func_3727')
call_3995 = relay.TupleGetItem(func_3726_call(), 1)
call_3996 = relay.TupleGetItem(func_3727_call(), 1)
var_4005 = relay.var("var_4005", dtype = "float32", shape = (8, 15, 5))#candidate|4005|(8, 15, 5)|var|float32
bop_4006 = relay.left_shift(call_3995.astype('uint64'), var_4005.astype('uint64')) # shape=(8, 15, 5)
bop_4009 = relay.left_shift(call_3996.astype('uint64'), var_4005.astype('uint64')) # shape=(8, 15, 5)
func_2964_call = mod.get_global_var('func_2964')
func_2965_call = mutated_mod.get_global_var('func_2965')
call_4011 = func_2964_call()
call_4012 = func_2964_call()
output = relay.Tuple([bop_4006,call_4011,])
output2 = relay.Tuple([bop_4009,call_4012,])
func_4016 = relay.Function([var_4005,], output)
mod['func_4016'] = func_4016
mod = relay.transform.InferType()(mod)
mutated_mod['func_4016'] = func_4016
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4017 = relay.var("var_4017", dtype = "float32", shape = (8, 15, 5))#candidate|4017|(8, 15, 5)|var|float32
func_4016_call = mutated_mod.get_global_var('func_4016')
call_4018 = func_4016_call(var_4017)
output = call_4018
func_4019 = relay.Function([var_4017], output)
mutated_mod['func_4019'] = func_4019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2337_call = mutated_mod.get_global_var('func_2337')
call_4038 = relay.TupleGetItem(func_2336_call(), 0)
call_4039 = relay.TupleGetItem(func_2337_call(), 0)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_4044 = func_2513_call()
call_4045 = func_2513_call()
bop_4056 = relay.power(call_4038.astype('float64'), relay.reshape(call_4044.astype('float64'), relay.shape_of(call_4038))) # shape=(8, 1, 5)
bop_4059 = relay.power(call_4039.astype('float64'), relay.reshape(call_4045.astype('float64'), relay.shape_of(call_4039))) # shape=(8, 1, 5)
output = relay.Tuple([bop_4056,])
output2 = relay.Tuple([bop_4059,])
func_4065 = relay.Function([], output)
mod['func_4065'] = func_4065
mod = relay.transform.InferType()(mod)
output = func_4065()
func_4066 = relay.Function([], output)
mutated_mod['func_4066'] = func_4066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3229_call = mod.get_global_var('func_3229')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_4075 = relay.TupleGetItem(func_3229_call(), 1)
call_4076 = relay.TupleGetItem(func_3231_call(), 1)
output = call_4075
output2 = call_4076
func_4096 = relay.Function([], output)
mod['func_4096'] = func_4096
mod = relay.transform.InferType()(mod)
mutated_mod['func_4096'] = func_4096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4096_call = mutated_mod.get_global_var('func_4096')
call_4097 = func_4096_call()
output = call_4097
func_4098 = relay.Function([], output)
mutated_mod['func_4098'] = func_4098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3475_call = mod.get_global_var('func_3475')
func_3476_call = mutated_mod.get_global_var('func_3476')
call_4146 = func_3475_call()
call_4147 = func_3475_call()
uop_4148 = relay.erf(call_4146.astype('float32')) # shape=(8, 1, 5)
uop_4150 = relay.erf(call_4147.astype('float32')) # shape=(8, 1, 5)
output = relay.Tuple([uop_4148,])
output2 = relay.Tuple([uop_4150,])
func_4153 = relay.Function([], output)
mod['func_4153'] = func_4153
mod = relay.transform.InferType()(mod)
output = func_4153()
func_4154 = relay.Function([], output)
mutated_mod['func_4154'] = func_4154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_4199 = relay.TupleGetItem(func_2813_call(), 6)
call_4200 = relay.TupleGetItem(func_2814_call(), 6)
const_4203 = relay.const([[[4.371023,1.105393,8.537885,8.245182,7.540224],[-1.742959,6.201841,6.487545,7.387370,-5.004211],[-5.375775,1.572239,6.399880,-1.055396,-9.650856],[4.165555,-4.003898,-5.379245,-5.672347,6.937225],[-7.199933,-0.688234,3.574932,-1.407169,2.816599],[2.182696,-3.635054,8.799503,8.625678,-9.751706],[3.093824,-3.418678,-1.512459,7.490069,-0.695359],[-8.093179,-6.492292,-9.039992,-4.648470,3.178896],[1.470350,2.616788,3.433299,4.023765,8.920351],[-1.728239,-7.280112,-2.945770,3.349897,3.384576],[-2.117994,-2.385098,-4.505969,9.912731,-6.700687]],[[-6.455372,5.632521,1.854673,-8.140925,-7.263442],[-3.783515,8.567653,4.188515,3.877336,0.637351],[-7.265473,-1.331280,6.061474,-8.931996,3.803168],[9.916973,-2.037975,-9.711381,6.856275,4.719480],[-4.659328,-7.166494,-7.585136,2.081329,-7.422766],[-7.680919,6.462073,-7.011979,-9.824898,4.356513],[9.257977,0.875744,8.843301,6.594096,1.522471],[-7.251297,-1.750997,1.884030,-3.988446,-9.023613],[2.297706,-5.159824,4.483863,4.719600,6.466375],[8.771033,9.068996,-0.571920,-3.087181,7.431799],[-6.347945,5.065551,-7.056131,3.734656,-9.818500]],[[-5.827648,6.188582,-8.875335,5.858112,-5.972421],[-4.451410,6.499363,-3.799343,-5.348950,0.050168],[-1.197169,-2.637079,-7.322016,-3.192383,5.228024],[1.221373,0.760882,-9.042679,1.787072,1.799761],[-0.937787,7.303421,-9.985465,-4.477824,5.429895],[-4.489717,3.608652,1.369476,-7.953776,-1.664757],[-2.796917,2.052366,-0.590785,6.962333,8.868168],[8.834263,-0.391891,8.345770,-4.045660,-2.874049],[4.110403,-6.076414,6.069496,-8.433108,5.475346],[6.653153,-8.047544,0.682591,6.400518,-0.093679],[-7.982038,-0.261897,-8.664260,9.335104,4.151960]],[[-7.728146,-0.890910,-1.687066,0.655304,5.401807],[9.256163,-4.723418,5.924178,-2.707783,0.873447],[7.627647,-7.637638,-6.769921,2.170872,5.152008],[5.777125,2.156778,-0.064571,7.366974,-1.368591],[0.161109,-5.515932,0.107213,1.234958,-5.728208],[-5.601936,-0.977762,5.996268,-8.325431,-5.180495],[-0.524603,8.134386,-0.356041,9.961360,4.044736],[-3.102505,8.058441,0.908448,4.002756,-3.796584],[5.007650,6.116963,1.566621,-7.612501,-2.770733],[6.694192,7.906312,-0.392679,0.235683,4.228054],[-1.275189,7.737530,-9.417717,-6.537557,8.844741]],[[7.148280,-2.724614,9.849015,-2.485092,9.580473],[-6.587194,3.694953,8.244490,7.335992,7.238432],[-0.119037,0.001087,5.215877,-0.616225,9.248603],[-4.331507,-6.183313,7.358221,-8.703704,1.492285],[-9.816258,-8.286699,3.620478,-9.120920,-4.155440],[-6.318274,8.361485,-7.710432,1.631324,-5.518442],[3.227452,-0.179692,9.432107,8.492086,0.051139],[5.128754,-5.662473,5.206721,-6.896737,4.391411],[8.941602,4.929550,4.998611,0.291663,-6.600033],[3.436967,-6.057254,8.209862,7.496356,2.257443],[0.865103,2.773165,-4.364094,-7.766560,-9.352930]],[[-8.323530,5.550658,-5.725298,8.336195,9.177568],[9.734922,2.913559,-1.722203,-8.927805,7.175816],[-8.554624,-6.631969,0.903529,-5.330263,8.305457],[7.933227,-8.666927,7.132005,0.636144,-2.330699],[-2.937303,4.143214,3.521402,-6.639753,1.304482],[8.115842,1.332343,1.852870,1.531598,-7.933375],[-2.881755,-3.212848,-9.334781,8.330381,-3.244096],[-7.188733,-4.056403,7.045764,-9.371344,0.100943],[7.866511,7.040395,-3.515528,7.414596,8.659976],[8.579815,5.420034,-8.317972,9.020219,1.409207],[-7.593146,4.192680,9.508293,-0.520324,-8.601494]],[[-3.623486,2.205671,-1.117641,-8.591401,6.136276],[9.076375,-9.786299,-0.046342,-8.510929,-2.615264],[6.814589,-2.775501,4.891322,5.631965,1.870087],[2.043424,-1.437797,2.626033,5.055196,-0.804741],[9.114248,4.687030,1.805400,7.673566,8.497150],[5.762540,-6.492357,5.875988,-4.423661,0.941303],[2.289740,4.600284,4.808062,-5.431137,-6.290912],[8.887295,6.185646,1.853363,-7.375746,-6.729394],[1.434810,3.560755,0.117346,4.151174,3.399391],[5.939647,-4.383467,-2.204148,-4.893941,-6.910549],[-5.614091,-8.970273,-5.938973,-4.498784,-1.687908]],[[-0.560433,-9.111259,8.798649,2.919682,2.039412],[-0.481379,1.328187,3.957584,-8.098036,-0.046347],[6.589589,9.179149,-5.925589,6.028797,-6.704251],[-2.809813,5.641467,-1.657425,-8.725097,-3.676068],[7.668998,0.703333,8.761549,-6.946667,-0.696351],[-1.064633,4.682902,7.687413,2.432007,-9.118725],[6.530406,-5.112327,-8.892399,1.174462,-5.658516],[-0.529122,-7.050106,-5.518626,0.934571,-9.555952],[-2.495571,0.720538,-6.725409,5.148258,2.501736],[7.914326,-7.534369,-8.728139,1.468882,-6.193731],[1.707118,4.641283,-2.640027,5.272647,-4.483659]]], dtype = "float32")#candidate|4203|(8, 11, 5)|const|float32
bop_4204 = relay.greater_equal(call_4199.astype('bool'), const_4203.astype('bool')) # shape=(8, 11, 5)
bop_4207 = relay.greater_equal(call_4200.astype('bool'), const_4203.astype('bool')) # shape=(8, 11, 5)
func_3990_call = mod.get_global_var('func_3990')
func_3993_call = mutated_mod.get_global_var('func_3993')
const_4247 = relay.const([8.394436,2.366479,6.462364,-7.311422,3.169864,-1.201352,6.067394,9.534471,9.138188,2.491737,-1.754861,7.819325,1.112283,3.860780,3.622066,-2.739387,-1.947392,2.617936,8.031251,-5.112700,5.732532,-6.988406,-2.872828,-5.990116,-7.454458,-4.657325,7.531205,7.078553,-1.855764,2.287977,0.315307,-6.540984,9.920729,4.367172,6.666480,7.523266,7.345132,-6.552409,-9.832747,3.905797,-3.732607,4.980266,2.754147,-8.098634,9.943527,-2.210336,3.895243,-3.514048,-1.493613,2.456764,-1.923457,-5.989102,-7.571372,9.273787,-4.998585,8.671745,-2.401135,-6.330556,5.589752,-4.865840,-1.777035,1.206555,9.437698,7.744035,-4.456186,-3.537794,9.473730,-9.694635,5.311567,-8.121020,-9.541117,-8.459439,-1.508199,3.061065,6.386612,-0.496114,-6.700593,1.058018,-8.909753,4.788121,2.292612,1.425204,-4.445729,-7.878323,0.540409,8.477761,-4.582483,-8.416969,-7.740771,-5.125203,9.390796,-9.526205,2.832260,-2.728061,-0.944519,-1.683786,7.099858,-6.230009,0.162810,9.635651,-7.119319,-9.942103,-1.795468,9.129469,-4.045180,-3.745714,6.673571,5.668818,-2.200118,-8.700784,6.884646,-6.082811,-9.038786,1.308431,6.306601,-9.111714,2.845045,-5.469883,7.730167,7.356870,0.975369,-4.894008,-2.433970,7.730029,4.441102,1.022991,-2.740838,1.721948,-3.421169,-2.019595,8.061987,3.477297,-6.711077,-2.828584,-0.421631,2.287705,3.740431,-7.214312,-3.889448,-7.773053,7.302552,-9.970505,5.261003,-2.618616,-0.828942,2.831309,4.972791,5.269331,-6.816750,2.835544,6.136369,-3.413862,-7.512807,-6.845659,0.007317,-2.689280,-9.452106,-8.454745,-2.342295,3.573525,-1.234153,-3.431637,-4.469431,2.240724,8.086615,8.063160,9.377837,0.715449,-3.162972,-6.636562,-3.491560,-8.939686,-2.807737,-2.882136,4.890483,7.767582,-4.187693,5.741485,6.256159,6.515123,3.536849,0.700999,7.400290,9.868607,-4.859767,8.351371,-3.933746,9.164621,-8.878022,-6.661018,-3.488887,4.707582,7.666782,7.601294,5.529922,-4.963753,7.036281,-7.051343,-6.304669,-8.493019,5.748376,-6.933040,4.468123,-9.406712,3.467030,4.816800,3.403319,7.238986,6.992378,6.816362,1.339279,0.189749,-9.125771,8.453168,2.048975,0.382082,0.520632,0.910387,-4.280626,8.674039,-2.710119,2.063756,3.275492,-1.527204,8.515069,-0.360931,0.917311,6.609293,7.549631,6.292053,-4.809523,4.860042,-7.221297,-2.124457,2.131267,-7.959023,-0.976151,9.561597,-2.783865,-0.583596,9.726898,3.080750,-4.606188,-9.614662,1.982617,3.748856,7.105893,-4.978382,4.158341,-9.973762,-3.352487,-9.733675,-6.646873,-9.191510,2.765238,-8.435079,8.888253,-1.360142,-5.818805,7.989010,-0.457744,0.996784,-6.521261,0.814941,-1.734743,-8.104954,-1.017086,1.628428,-5.374675,-9.313392,-1.830400,-9.611175,-3.250802,6.215193,-0.364334,-6.626124,8.104195,-3.789232,8.729082,9.201350,2.242823,-3.018394,-9.392301,-5.490581,-4.645957,0.157831,0.588172,-2.166667,-7.131363,-5.755164,5.215675,0.494360,-9.786779,-2.711282,1.283540,6.566893,9.281416,-5.252868,2.496817,-8.368661,6.596157,-0.918765,4.748835,-3.485206,-2.895290,-1.898191,-8.371352,8.516506,9.293583,-2.659415,3.355501,1.718377,-2.177397,4.240234,-6.491350,9.699042,0.413323,-7.566995,-4.913658,-1.511709], dtype = "float32")#candidate|4247|(320,)|const|float32
call_4246 = relay.TupleGetItem(func_3990_call(relay.reshape(const_4247.astype('float32'), [8, 8, 5])), 0)
call_4248 = relay.TupleGetItem(func_3993_call(relay.reshape(const_4247.astype('float32'), [8, 8, 5])), 0)
uop_4267 = relay.erf(const_4203.astype('float64')) # shape=(8, 11, 5)
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_4269 = relay.TupleGetItem(func_4065_call(), 0)
call_4270 = relay.TupleGetItem(func_4066_call(), 0)
output = relay.Tuple([bop_4204,call_4246,const_4247,uop_4267,call_4269,])
output2 = relay.Tuple([bop_4207,call_4248,const_4247,uop_4267,call_4270,])
func_4271 = relay.Function([], output)
mod['func_4271'] = func_4271
mod = relay.transform.InferType()(mod)
output = func_4271()
func_4272 = relay.Function([], output)
mutated_mod['func_4272'] = func_4272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4153_call = mod.get_global_var('func_4153')
func_4154_call = mutated_mod.get_global_var('func_4154')
call_4273 = relay.TupleGetItem(func_4153_call(), 0)
call_4274 = relay.TupleGetItem(func_4154_call(), 0)
output = call_4273
output2 = call_4274
func_4280 = relay.Function([], output)
mod['func_4280'] = func_4280
mod = relay.transform.InferType()(mod)
output = func_4280()
func_4281 = relay.Function([], output)
mutated_mod['func_4281'] = func_4281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2964_call = mod.get_global_var('func_2964')
func_2965_call = mutated_mod.get_global_var('func_2965')
call_4394 = func_2964_call()
call_4395 = func_2964_call()
func_2442_call = mod.get_global_var('func_2442')
func_2445_call = mutated_mod.get_global_var('func_2445')
const_4426 = relay.const([-6.680240,7.994516,8.108350,4.777113,3.952293,-0.917680,-9.112486,7.118841,-0.426670,-8.832937,-2.958063,7.004230,0.132836,2.218934,-7.991423,0.703255,2.019398,8.517876,4.808268,6.825020,1.614477,-5.354189,4.373538,9.166604,7.282980,-7.454514,-1.905253,-8.364804,3.549215,-4.323372,9.104520,-5.733544,8.586152,3.695908,-5.536433,2.904534,-4.383721,-0.289639,9.341620,1.061947,1.408103,2.115228,4.602281,5.113099,5.377331,9.804358,-2.534007,4.926880,7.018936,-0.704870,1.746671,2.946121,3.250465,4.501201,9.559296,-0.453971,-7.829073,-5.250465,2.734195,-3.428616,-6.934186,1.412990,3.333906,-0.884467,8.696665,6.107871,-1.491708,-7.577946,-7.717769,1.974618,-7.673063,-6.735129,4.990191,8.027478,0.148980,0.033765,2.625882,-3.558629,-8.469951,3.279081,7.957271,-7.779525,3.555609,-3.711569,2.449170,3.431133,6.743280,-6.470564,4.009447,1.187256,-9.016476,-4.670964,-7.677322,-2.712015,4.888413,-1.234400,-8.013973,-4.117642,-2.406731,0.549433,-2.928486,3.683827,2.668890,-7.182735,2.910525,4.229657,2.192165,2.536288,-1.650724,-7.369902,9.063371,-3.283833,8.174191,3.139953,9.662030,8.067293,-2.548986,2.812499,0.649945,-4.551687,-9.621189,-5.358984,0.397793,2.736328,6.093111,8.728362,-6.082458,0.299887,-2.366379,0.410500,7.393809,-7.333097,-2.368461,5.952380,8.130065,-0.981791,0.754386,6.151324,4.110859,-7.286476,-4.117549,5.564750,-1.509869,5.604691,-3.609476,-0.331714,3.502514,1.243984,0.956311,7.760008,-4.268825,-7.583827,-2.445085,-2.348351,-4.414262,0.158581,-0.363563,6.875610,3.642979,0.883380,-7.971398,2.757975,-2.760902,5.425525,-8.170669,9.850142,-0.400702,-5.546520,0.923592,-3.938929,-1.812852,4.026520,2.482766,2.008288,7.406326,-9.020674,-9.406218,4.588049,-6.780288,-3.588215,-0.765125,2.786028,6.453262,8.980703,-6.988145,-3.030237,4.740947,7.250334,4.271648,5.388303,1.899207,-5.748944,-1.223600,1.286280,-6.498659,0.605904,5.650486,7.419205,-5.778263,5.513973,5.958764,6.731354,4.848054,2.118147,0.837148,0.091894,-5.713399,9.136103,-8.458422,8.283515,-6.311700,5.182897,2.821075,7.934133,0.196375,-0.274774,-3.181828,-1.357020,-9.747463,-6.742093,-4.554328,-5.155289,6.067660,8.949436,-3.053904,-1.150759,5.344821,-0.624598,8.770220,0.727725,5.154245,3.343017,9.340258,1.550159,0.328123,-8.688746,-4.658813,-5.680949,-2.671405,5.088198,-7.872756,6.960435,8.623997,-7.173413,6.754342,3.748046,2.378067,7.990269,-8.640891,-3.428140,-5.249395,-9.761328,2.010767,6.508833,-5.041124,3.521853,-7.173210,4.189231,-1.319845,-9.775231,6.327120,-1.075027,-2.042158,3.005966,7.581343,-0.921336,-1.360557,-5.698177,2.987022,2.607798,-1.554810,-2.468085,-9.929555,-4.695148,8.551228,-4.028673,-6.882917,1.971410,-5.713843,-9.622129,-2.950039,-4.771600,0.086901,9.317145,-5.730444,-8.474131,2.224294,2.344619,-9.019520,-2.985631,4.662871,-7.041686,-1.400875,-7.927223,9.172027,-8.632384,-3.002504,-8.517709,7.417071,-3.754417,9.123408,-6.146307,-6.690247,-2.377468,7.260425,-2.199825,6.632009,-1.144071,5.043182,0.309602,4.610614,-4.991266,-1.850143,0.451084,-1.817740,2.963616,3.568302,-1.497354,7.954971,-6.244275,-9.446992,4.206092,-1.425787,5.757533,8.453948,-6.078971,-5.950034,-8.249523,7.430174,-8.524493,6.732006,1.174318,4.687498,-2.837508,-2.298756,1.202055,-4.209981,4.663436,-8.360393,-1.803380,7.167207,5.921366,5.426038,-1.206441,7.406903,9.759620,-9.038705,7.220559,-9.665030,-3.866814,9.523240,5.528941,7.824634,-7.563998,6.523436,2.035098,7.129728,-2.608396,-5.262596,8.049008,6.228672,-5.984591,-1.822330,5.676058,-9.206930,9.455832,2.749390,5.532532,7.875395,0.903861,-0.866943,1.718486,1.984608,-7.486363,-1.443532,9.800238,-9.982018,3.174233,-6.648996,-1.506995,0.144606,-4.583786,-0.938945,7.111777,0.518126,1.215610,3.220328,4.329982,-1.741733,-9.156102,8.387774,7.892637,3.529918,-5.394922,0.891296,-4.872480,8.306453,-1.096541,-9.622822,1.020829,-3.615365,6.820386,-5.846898,-3.101481,5.820183,5.736046,-9.571968,-0.295526,-6.518632,2.176032,6.359115,-4.973487,-4.521424,7.254227,-9.519721,-4.414382,2.914762,-2.795827,-0.204989,-9.388200,7.243036,1.976057,-9.629157,4.460077,-1.556259,6.086445,1.201769,-9.581925,-4.196429,-9.310737,5.741664,1.220702,0.937162,-3.928062,-6.156910,0.919299,-5.319853,0.197095,-5.228380,5.531160,-3.734438,2.165553,-6.986164,6.054903,4.820956,9.050310,0.266973,3.851222,-1.435857,-8.760825,-2.063520,-7.892365,-7.398908,-1.857243,9.731344,-1.191537,-5.682549,2.747523,2.068866,3.531135,-6.578674,2.936926,9.184181,-5.623871,-3.057134,-2.283592,-1.487104,-4.675192,-2.617172,-4.025637,-5.407238,5.181804,-7.408799,-7.740149,-1.653010,-5.460081,-7.964748,-5.874948,-4.294815,-7.242124,6.468211,2.627221,1.307759,5.881076,-6.900363,6.671385,-7.956143,1.616150,5.154391,-0.998553,3.037292,0.421913,5.192153,9.546581,-9.340465,-7.693950,-1.725032,-1.278699,8.107040,-4.515108,2.688899,2.532033,-8.856995,-5.066250,-9.437569,8.278330,7.349471,5.604495,-0.044683,-1.598686,-0.204449,5.196939,-8.873050,7.427903,3.078964,-9.920569,4.050075,-6.515171,-1.231900,-1.484919,2.559193,1.961237,-9.776705,4.912451,4.461154,2.822964,4.699341,2.792716,-9.459234,8.879774,-9.429784,-3.804907,1.004365,0.336086,0.011963,-3.174927,-7.748793,3.041828,3.409172,7.429771,-8.207303,-1.554855,2.876220,-7.514321,-0.494871,1.915634,6.017721,5.577327,-4.198022,-7.329911,-5.025207,2.426549,-3.979840,2.304845,6.909779,1.228729,1.754312,1.406363,5.773686,7.780048,-1.468514,-2.001002,-5.034078,-2.057214,-0.674994,9.035971,-1.293261,0.899445,1.711136,-7.710445,-2.412391,5.638751,3.187088,-9.340145,-7.349412,0.714721,4.101256,-5.862197,2.724509,-8.870748,4.885085,-0.661937,-2.126851,2.542803,-1.743696,3.506105,3.085651,-1.523374,2.619185,9.237892,-8.906201,-5.983819,-1.506942,-1.416077,-2.267870,0.431041,-9.114745,6.848459,-1.010737,-6.185162,-1.958044,1.940123,-2.393474,-5.241020,-9.258215,7.130414,-4.613379,-5.814151,-8.141313,-2.587010,-3.827547,2.023602,6.773193,3.919193,7.852692,-5.168950,8.009949,8.138365,-0.695563,-7.408161,9.358404,5.298092,7.966421,-4.170499,-4.210346,-3.045548,-4.399225,6.248265,-7.561992,2.484394,5.194505,3.474550,6.682332,-1.805367,3.118730,5.023188,5.017650,-1.765515,-4.092515,-1.993591,-8.855481,6.491175,-0.960454,-9.645186,-2.046006,-7.383674,-7.261174,-6.545195,-8.093122,3.241406,8.466176,-0.860390,8.407388,-1.903127,2.816711,4.135619,1.479715,4.950275,6.776995,0.207750,1.246143,6.286522,6.530182,-3.731710,3.452240,6.833877,-8.498156,2.468697,7.551953,5.001461,-7.006119,-5.271694,-7.073778,-3.899931,7.390570,8.606618,0.677198,-1.685762,-3.928908,5.649740,-3.637726,2.171640,-8.545465,8.746776,-6.746470,5.521897,0.816338,-7.848050,3.445522,8.735943,-0.864285,9.220024,-4.919745,3.350071,-7.493432,-1.313208,8.788006,7.371514,-6.829092,3.981716,-3.585823,1.712163,-6.192536,5.279694,-0.304136,0.767066,3.670614,6.012491,-2.276651,-6.874280,7.646174,-6.705654,-7.279706,-9.381280,-2.156332,6.673329,-9.982391,-1.930483,5.434440,-7.581968,-5.537914,-9.428340,2.431121,0.897055,-2.024362,-9.052932,-8.915327,5.235319,7.884768,2.694491,1.785968,-9.866206,-5.434009,8.109809,-4.614855,8.601202,5.038258,-8.391286,3.328563,-8.475620,0.884101,2.525909,9.272474,5.981979,1.284939,-6.614587,4.631550,-6.333520,7.184152,3.436727,-1.494316,0.454037,9.728125,-9.510483,3.807512,-7.322641,8.095514,5.903814,-6.868309,1.914146,1.735381,4.031451,-7.811847,-1.362350,2.160425,8.838468,8.796814,0.081469,-8.729051,7.161359,-5.131078,6.649506,-3.886214,1.411549,0.049346,-0.234028,-9.401535,5.311502,7.017423,1.447111,-2.489278,-5.358019,4.379867,-0.739932,6.010571,3.442446,7.864563,-4.738388,4.876415,6.798753,-1.519218,-7.605556,8.153068,-1.288022,0.575634,4.866752,-4.481970,9.985679,4.501248,-9.866495,-9.301636,-1.195105,-7.818401,1.286632,-4.344609,-6.041339,-5.005319,-3.857983,-7.772854,-3.177236,-5.548981,5.851698,-6.587919,-3.466572,-4.289409,-3.160053,-4.000936,2.075458,7.637649,0.798502,2.413377,6.724153,-4.769062,7.533782,-2.487985,-6.705924,7.120071,7.105803,9.892989,4.457781,-3.575591,-2.085768,-2.468787,5.110439,-2.588331,-3.737844,-1.700810,3.482451,2.080979,-3.679875,-1.212788,-3.628793,-8.626425,1.821177,5.072254,-7.781215,3.639507,-2.914456,-4.228562,2.623474,-7.586733,-7.592420,7.965894,0.644182,-7.139711,-9.617869,4.366158,-9.384603,7.300067,3.069951,-8.986697,-9.767944,-9.987421,6.092878,9.572776,1.180673,-4.846472,-6.189849,1.138750,-3.548934,8.451560,-9.266191,8.028373,1.717557,1.991575,1.578611,-6.967934,4.636586,8.524529,2.649826,0.185871,-0.084312,-3.066819,-1.678666,2.208679,5.263163,1.156135,1.513755,-0.018902,3.077106,9.165349,6.017927,2.908780,-0.288470,6.638225,8.628363,-1.913026,6.441979,-6.488080,-9.023218,-5.287276,9.490772,7.604981,8.815674,4.448033,5.629483,2.595162,-6.489408,8.786232,1.931749,-7.047035,-3.978124,4.407459,0.693781,6.249294,6.416693,8.948101,1.293035,2.884099,-3.751400,-1.884017,9.848745,-2.778848,-1.197542,-3.117069,-5.938194,-2.918164,2.722221,-2.681783,6.697167,-4.555505,-5.097406,3.357816,-8.111567,-0.985364,4.320353,3.839284,-8.557646,-9.129609,3.747570,2.697961,0.930400,-3.439407,6.537162,0.868551,-3.449726,9.600566,9.268783,7.131623,2.721850,-1.868245,-3.170647,9.563449,5.650238,7.993637,-1.975515,3.853366,-4.832844,-7.120989,-9.293847,-1.275026,2.665791,9.904786,4.619732,-7.104513,-0.590567,1.243125,-0.446100,-7.469939,3.158439,7.306143,-9.330720,9.304610,-1.830019,-5.678525,-5.722602,-4.127901,-0.280668,-7.485106,-7.597389,-6.979605,-3.649154,4.233273,-8.883791,-5.777352,2.258630,5.181589,-4.143768,-8.225145,-9.914021,-5.209928,6.261003,-9.254415,-0.049050,7.316584,4.595465,-1.300494,-0.154483,3.123833,1.289988,-5.676788,6.334870,-0.054950,-6.454884,-8.105707,4.328603,8.708237,4.290345,-4.648075,7.584829,-9.617774,3.153056,-7.440950,-2.032743,-6.860340,3.495140,-5.638269,-3.960083,7.854372,9.076492,8.592341,-2.381320,-7.154190,-0.486097,3.687553,-9.362068,-6.177294,-1.487996,6.443281,-0.798418,-2.125507,-0.830848,-7.144706,8.983627,-4.286405,-8.605860,7.759313,-0.649403,-9.453240,-4.141748,-6.497821,-4.416243,-2.793054,4.241935,4.492622,1.036606,-5.450820,5.027446,-9.386760,-5.148852,0.038789,-4.061819,0.457826,-1.590453,0.606280,5.203393,-8.096517,5.829857,2.553115,-6.683831,-5.965205,-5.995298,-1.228544,-4.030342,7.873847,5.835792,9.916306,2.348226,-5.270351,-1.268924,5.731405,-7.243119,0.189847,-1.999255,-7.354664,-0.785516,7.637283,1.365502,-8.024374,-1.016604,-1.240699,-1.458395,-0.884988,-0.624602,-0.692047,-1.867843,1.330180,2.393358,-3.402747,0.642302,-3.420764,-5.127452,-7.159024,5.449397,6.490883,-7.572459,5.934310,5.791220,8.318999,5.108974,-7.321632,3.870778,-7.418215,9.476486,-7.393382,4.943653,-6.156648,-6.728303,-9.935521,4.733844,-1.654926,9.973507,-4.364453,5.588099,1.217860,5.984782,-2.526134,2.589357,6.689450,-4.357271,4.557771,5.800567,0.189337,-4.584042,8.308064,2.434281,-4.718048,-3.814925,0.590097,-7.469145,-8.696294,-9.544160,-0.608980,6.894993], dtype = "float32")#candidate|4426|(1134,)|const|float32
call_4425 = relay.TupleGetItem(func_2442_call(relay.reshape(const_4426.astype('float32'), [1134,])), 0)
call_4427 = relay.TupleGetItem(func_2445_call(relay.reshape(const_4426.astype('float32'), [1134,])), 0)
uop_4438 = relay.sqrt(call_4425.astype('float32')) # shape=(8, 1, 5)
uop_4440 = relay.sqrt(call_4427.astype('float32')) # shape=(8, 1, 5)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_4443 = func_2513_call()
call_4444 = func_2513_call()
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_4453 = relay.TupleGetItem(func_2813_call(), 3)
call_4454 = relay.TupleGetItem(func_2814_call(), 3)
output = relay.Tuple([call_4394,const_4426,uop_4438,call_4443,call_4453,])
output2 = relay.Tuple([call_4395,const_4426,uop_4440,call_4444,call_4454,])
func_4459 = relay.Function([], output)
mod['func_4459'] = func_4459
mod = relay.transform.InferType()(mod)
mutated_mod['func_4459'] = func_4459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4459_call = mutated_mod.get_global_var('func_4459')
call_4460 = func_4459_call()
output = call_4460
func_4461 = relay.Function([], output)
mutated_mod['func_4461'] = func_4461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_4482 = func_2513_call()
call_4483 = func_2513_call()
output = call_4482
output2 = call_4483
func_4501 = relay.Function([], output)
mod['func_4501'] = func_4501
mod = relay.transform.InferType()(mod)
output = func_4501()
func_4502 = relay.Function([], output)
mutated_mod['func_4502'] = func_4502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4459_call = mod.get_global_var('func_4459')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_4509 = relay.TupleGetItem(func_4459_call(), 2)
call_4510 = relay.TupleGetItem(func_4461_call(), 2)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_4518 = relay.TupleGetItem(func_2305_call(), 0)
call_4519 = relay.TupleGetItem(func_2307_call(), 0)
func_3298_call = mod.get_global_var('func_3298')
func_3299_call = mutated_mod.get_global_var('func_3299')
call_4528 = relay.TupleGetItem(func_3298_call(), 1)
call_4529 = relay.TupleGetItem(func_3299_call(), 1)
output = relay.Tuple([call_4509,call_4518,call_4528,])
output2 = relay.Tuple([call_4510,call_4519,call_4529,])
func_4530 = relay.Function([], output)
mod['func_4530'] = func_4530
mod = relay.transform.InferType()(mod)
output = func_4530()
func_4531 = relay.Function([], output)
mutated_mod['func_4531'] = func_4531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mod.get_global_var('func_4501')
func_4502_call = mutated_mod.get_global_var('func_4502')
call_4546 = func_4501_call()
call_4547 = func_4501_call()
func_2694_call = mod.get_global_var('func_2694')
func_2697_call = mutated_mod.get_global_var('func_2697')
const_4551 = relay.const([-5.033992,3.649473,8.125833,-4.660108,-9.279190,3.484124,7.421886,-4.853584,5.594868,-2.713905,-2.412077,-8.779836,2.886438,-4.295720,-7.343736,-2.460429,-9.231218,2.002926,3.340619,-0.848002,-9.441788,-6.646575,6.862523,3.005652,7.302553,8.417030,-4.045176,-8.225894,-7.809757,-8.709341,7.114247,7.058172,-3.146161,9.490996,0.588517,8.766498,6.295490,8.109101,6.646608,8.647305,-6.127629,-4.019558,6.439562,-1.391441,2.210259,-3.246265,8.600122,-8.835147,-3.290197,5.463330,-4.075431,1.142168,5.447125,-5.530505,5.193092,6.543505,-4.868460,2.361818,-8.215217,2.188423,-5.893507,-1.848111,-6.788664,-0.152776,-1.850934,-4.426654,-3.772757,-0.978172,-2.916805,-3.652317,5.678204,6.659362,-7.755681,6.620877,0.094662,-0.376719,-0.680171,0.294353,-7.948062,3.057578,-6.989802,7.535906,-8.461919,-9.975453,-3.351134,-1.692927,-7.572863,-7.488281,-1.443413,7.474316,-7.378197,-6.800284,-8.037486,8.929670,2.931200,3.472838,-8.099809,-9.144867,-9.512539,0.418315,-8.225902,-9.455284,-4.248599,2.594888,-4.497527,-8.924123,-3.979127,5.545760,-0.338268,8.734638,-3.706935,3.637223,4.824354,8.292383,-9.814256,5.564512,-0.637193,3.395361,-5.297285,-5.855540,9.061094,0.168695,1.213587,-9.794356,-5.686461,5.815525,-1.585170,7.409428,-0.212185,-1.857708,-9.763390,8.131547,6.173164,2.071925,1.678581,9.167899,-9.677378,6.490893,1.670646,8.339108,9.763489,-8.675007,-9.147019,-1.741053,-2.804784,9.386521,-5.514757,-1.614556,-2.555971,2.024428,0.041989,-9.477342,0.361138,4.168146,-1.804047,-3.258742,8.389441,9.785569,4.635274,-1.967834,-1.241363,-8.070839,9.672552,4.994331,-0.940044,7.998666,0.815755,1.474990,9.474492,6.343448,7.936817,-7.384194,5.535075,-9.117241,0.616187,-6.898536,8.611427,-3.808503,0.123642,-5.888251,-7.452153,2.059444,0.532073,-6.947432,6.158476,-7.735505,-5.705665,6.865808,6.790041,-4.650720,5.479675,-6.967859,9.790968,8.127787,-9.218740,-5.948062,5.140104,-0.995611,-5.865473,-2.815275,8.002756,-6.123145,0.816815,6.065227,-8.138831,8.212670,-0.717122,-9.811544,-5.350459,2.458530,8.418309,8.069688,9.627811,1.823342,-1.777645,-9.436406,4.699497,4.699737,-4.694129,7.950105,-3.402466,-4.230279,-7.310613,-3.591955,-5.475920,-1.940844,9.300478,9.435187,9.935737,-6.183768,-6.757234,2.502889,-3.191932,-4.972323,6.856881,4.147874,-3.996363,4.334836,-4.747607,9.703552,4.112224,-2.480886,9.001264,2.243362,-9.050537,-0.955909,-5.185555,-0.925385,3.779693,-4.680600,-5.295000,-3.119610,0.379094,-6.932964,-0.455376,2.345664,8.772649,-7.222502,0.931887,9.535795,-8.737485,-1.450417,-5.073384,6.791997,6.174009,-0.441856,7.252327,-0.002322,-5.042414,-6.848836,-6.440976,-1.657804,1.139463,-2.690326,4.809924,-5.681424,9.694860,-1.328986,-7.125635,0.884972,2.153803,3.775057,3.323700,-1.876840,-3.975930,-4.449121,-8.222338,-3.980819,4.759940,-2.191407,6.064235,-9.707324,2.896437,-8.791491,-3.699388,8.068560,4.644909,-9.240814,-8.352014,1.985379,2.220285,1.329448,-5.105033,6.166739,-8.797586,-0.003027,4.542083,-4.365872,-7.870032,-6.344118,8.641163,-6.900249,-5.370253,5.690227,9.411092,-3.749142,-7.211530,-9.905666,1.045673,-4.243218,0.657599,5.776004,-4.287421,9.612441,-7.722655,0.351543,8.321622,7.312652,8.423639,-9.338879,8.426235,2.246630,-6.672658,-2.666519,-8.036833,2.681145,-5.882278,-5.973017,7.473483,4.247020,1.229391,5.300390,-9.614470,-1.953105,6.642797,2.159487,5.803017,-4.031347,-3.556942,-6.962768,7.306995,3.330318,-9.987670,-5.652791,8.979124,-9.476486,5.004009,-1.714995,-9.455273,6.990818,5.306371,-9.563427,4.290803,1.347242,1.220398,-1.491830,8.708757,-8.579358,0.408468,4.272771,-6.317187,7.228369,0.644632,-1.395701,2.054000,8.513214,-1.025463,5.681238,-1.376386,3.344685,-2.238861,1.478616,8.448166,-5.405734,-3.336132,-7.715178,0.858804,-5.218911,8.170181,-9.583702,-8.613261,6.463668,7.695366,1.000908,5.737405,3.507094,-1.323196,-7.068852,4.855906,7.399033,-5.276649,-9.377300,3.782858,2.197950,6.353855,7.590517,6.496586,-2.961482,-0.927965,8.414323,1.753119,8.550379,6.843159,8.462835,-3.385059,-8.004295,-6.182542,-9.003036,-9.701794,-2.454914,7.033327,5.014864,5.366442,1.113271,2.814317,9.506030,-2.928703,7.403911,-1.402533,-3.381062,0.455578,-9.101305,8.199268,2.183422,-5.887759,-7.294209,-1.799042,-0.231825,9.656314,9.857728,-4.572115,4.201549,9.629416,-4.860315,-5.792305,1.923294,-1.380453,3.465022,-0.916813,2.243492,0.967045,4.195182,7.050084,7.123986,0.448739,-6.303205,7.764820,-9.071925,-4.126879,1.160820,4.447817,-0.942677,-0.540687,-5.774866,-8.389252,9.750943,9.992773,2.359772,-9.334546,4.097029,9.132724,-0.908651,-7.194836,-2.249218,9.446648,9.329640,-3.543823,-0.913108,4.604803,3.646463,-8.993000,8.860017,8.812005,3.102641,9.084592,-5.888382,-8.670551,-2.508630,6.148352,9.773636,-2.393517,-9.525425,-9.621075,3.062523,8.902849,0.232449,0.984336,2.191137,-5.328654,-9.786424,3.820489,-9.541247,5.730652,-0.432176,4.706502,-4.175179,-4.876631,-1.103592,3.034321,9.663405,9.147195,7.991858,5.710913,9.783742,6.440781,-2.944072,-5.649903,-2.214862,9.545327,8.961699,-4.129753,-6.726601,-0.906419,0.684427,-9.989045,-1.639339,3.171941,-6.153064,-9.389366,-2.956779,4.873365,-0.094438,-9.676116,-0.170308,-6.884018,-3.481017,0.909613,9.484393,-4.455550,0.203383,2.175424,-4.759181,0.765599,-0.178511,-1.963116,3.505958,6.045462,-4.619789,-4.798847,8.999214,-5.183264,0.065103,-1.627460,3.895419,6.209592,6.743251,-7.116853,-9.054688,-0.173787,2.254932,6.182967,-7.452770,-1.994190,-4.936862,4.369742,2.545711,-2.541664,8.805176,-8.085716,5.807883,-4.983060,-7.040507,-5.922470,-6.575984,7.039523,7.532731,3.743058,4.072437,-4.594713,-9.778295,8.762017,1.167130,8.041511,-9.882599,3.697135,3.519380,-9.495576,-4.658285,-2.520266,0.975212,-4.775755,6.430500,9.725696,-9.182876,-8.377263,6.175106,-5.457251,1.802648,-4.392441,4.822375,6.954259,1.701122,1.840159,-0.446536,-4.325382,8.379165,9.425678,-2.767031,-8.143280,-0.202290,-1.654875,-5.461087,6.407039,-3.604724,-1.970989,9.572445,-0.425918,2.223686,6.308860,-8.293506,-1.261305,-9.870513,-0.086356,-9.341441,8.321643,1.434892,-7.411727,0.903520,-4.331921,2.440409,0.974381,-1.677611,1.586680,9.426786,-6.154389,0.179206,-7.432535,-4.429836,-8.217077,6.223430,7.537375,8.539433,-3.980335,6.944145,-4.361863,2.137383,-2.871978,-5.965220,-1.389493,-2.208064,8.198591,4.014483,7.362723,-4.709771,-1.096911,-1.913409,-4.853742,5.996304,-0.213392,4.806956,-3.103303,-2.845959,1.603260,-2.130604,2.156527,-6.237008,-3.933597,-5.684660,8.425873,-5.773052,-5.778641,4.833827,-3.427420,4.005184,-6.690443,-8.783726,-7.551563,1.185957,6.711186,2.728563,-5.567619,8.614288,8.064063,-1.174302,-4.063347,-7.446677,8.041746,9.984339,-8.619151,-5.828273,-5.206336,4.891671,-2.130471,-5.414381,5.399390,-1.070633,4.203943,-0.763291,0.877993,1.940951,6.450736,-4.725144,2.805234,8.188446,-0.934464,-3.985539,-5.620840,2.882855,-5.047612,-2.251799,7.817070,5.814506,-9.443782,0.470304,7.270546,4.495285,-6.612594,8.481740,3.735145,-7.732126,9.205650,-8.390555,-8.793053,-1.367903,8.418870,-1.707163,4.688677,7.311848,-0.344308,1.821667,1.534139,-5.540477,-9.855469,-9.311136,-8.511544,6.535606,1.959370,5.352405,-3.278387,5.948295,-1.282639,-7.304043,2.453019,0.966632,5.611291,9.264593,2.641027,-5.183289,-1.046293,-5.093343,1.307809,-7.720169,4.938283,9.340100,9.466702,-3.306894,-9.697800,6.919237,-6.167531,8.080098,2.613321,5.638567,0.709319,-2.550184,-1.548350,-2.163277,-7.964876,-3.543019,1.278889,7.083751,-8.831686,-5.757187,8.058815,5.951682,8.598380,1.574603,1.096513,0.074759,-8.876747,-4.607541,-2.719328,5.690747,4.095945,2.228583,8.695837,2.065385,-9.999011,-9.123031,1.595854,2.095218,0.905338,8.809991,2.455723,0.559611,-2.955633,-9.290184,-6.307945,-4.609043,-9.608430,-2.339383,-4.999217,8.861818,-2.841062,-5.005579,1.910072,-1.665566,-6.446352,-8.276609,-7.208214,-2.251273,6.533076,-3.852010,-6.138804,-2.684725,-1.852484,-0.673404,-6.915883,8.341672,6.587450,5.775552,1.319878,7.589819,6.184405,-6.062613,8.684256,0.129824,9.319817,3.106241,-3.501501,-8.303069,-8.409693,3.179727,4.438756,6.422335,2.166393,3.622295,-7.860812,-4.158428,-2.652018,-8.651057,4.052110,0.106818,3.031131,-9.338075,-0.705759,-8.672575,8.484830,1.971731,-3.107909,-7.600133,4.757170,-2.964314,-1.534074,-9.055655,6.457113,3.979758,-2.042032,-1.453303,2.510371,4.089461,8.696934,-5.812141,6.242901,0.145895,5.892023,6.519429,-8.843056,-4.179902,3.039409,4.567352,6.741946,4.795427,5.848769,6.935428,0.332608,-5.818929,-2.979031,8.617410,7.156208,1.589819,-8.565382,4.738397,6.103463,-5.083306,-5.875056,5.227655,-7.786123,0.368076,-5.972807,-3.104248,5.179586,9.366094,2.719832,-2.168894,4.283107,1.680493,-3.105414,-9.211759,1.218022,-4.739379,7.540216,6.556506,6.694189,9.904403,-3.507828,9.866760,0.124716,9.827058,6.741510,4.941171,-7.472005,6.001656,4.870062,-1.781658,-1.136014,0.381953,-1.385206,9.777126,9.036330,-3.764024,-3.226010,-6.850022,-3.158487,-5.098423,3.027430,-4.606735,0.872488,-4.332539,-7.222358,4.243488,-9.627399,-6.343471,3.549851,-0.209845,-4.115841,-0.905344,-0.571617,-5.387501,3.891579,-0.769705,-3.234871,-4.754234,-9.774596,7.793840,5.197792,9.852596,7.582115,-8.061783,8.099502,8.497737,2.845762,-5.251400,-7.552064,-0.932898,-0.420255,-3.260789,-1.702565,-0.978472,-4.456957,7.840010,-4.861325,0.472585,-1.017979,-8.749061,-0.186407,1.604654,-0.315913,3.972676,7.619371,-2.744786,-1.174826,-2.942775,3.858769,-7.158160,-6.416583,7.364833,-9.165452,-0.523082,-6.038110,2.626225,3.359794,8.165436,-0.838991,-6.248867,-2.501314,2.598040,-4.282016,1.688288,-3.674944,7.049827,4.111256,2.325245,8.401775,-7.270773,8.671258,-7.234310,3.633191,-7.697085,-3.565917,7.232491,7.565766,9.566715,-8.053824,9.301549,-2.177897,-4.517526,1.795650,-6.215466,8.044030,-6.454210,-6.230306,6.026997,-0.567349,2.029605,4.675650,-0.672662,-1.025441,-8.916439,-5.149343,5.412845,-1.332228,5.443407,-3.228295,-2.786595,-1.098709,-7.809594,3.819513,-0.911363,1.225786,-0.168916,-9.592136,7.198190,-5.201268,-5.186562,8.247114,-8.337989,5.885034,9.486681,4.599420,8.008433,-8.084126,-4.692145,-2.229002,-8.656780,-8.937745,-1.197142,7.550691,3.117095,9.166069,-4.843802,-8.237031,-2.075621,-3.262681,6.553160,8.143187,-9.891490,-6.370226,7.281071,6.689949,-4.820987,-4.339321,7.360746,-7.352939,1.170622,-9.129675,-3.970054,-2.210298,-9.130238,-2.324140,-1.189175,-0.482596,8.563655,5.373760,2.537609,-0.718298,0.006792,-5.451468,-4.155763,4.188265,-2.189390,-9.698160,-4.706671,4.298823,6.353083,-5.482681,1.712341,-4.075382,4.600894,6.711235,6.708582,-6.203400,-8.384687,6.469753,8.538002,7.535057,-1.070528,-7.972821,-4.394052,8.051354,6.813373,-2.370810,-9.116289,-4.091943,-8.755846,0.561075,3.835614,-7.157236,-3.048828,9.122831,1.162510,-4.357820,-3.393525,-3.027668,-7.316681,-3.749223,-3.734388,4.267937,-2.509230,-5.687617,2.344863,-4.483372,-9.125144,8.234676,-0.257110,-1.695333,2.399723,5.655797,-4.859972,-9.381562,0.337179,-8.683884,9.130621,-8.381421,2.425474], dtype = "float32")#candidate|4551|(1134,)|const|float32
call_4550 = relay.TupleGetItem(func_2694_call(relay.reshape(const_4551.astype('float32'), [1134,])), 1)
call_4552 = relay.TupleGetItem(func_2697_call(relay.reshape(const_4551.astype('float32'), [1134,])), 1)
func_3726_call = mod.get_global_var('func_3726')
func_3727_call = mutated_mod.get_global_var('func_3727')
call_4581 = relay.TupleGetItem(func_3726_call(), 1)
call_4582 = relay.TupleGetItem(func_3727_call(), 1)
func_4016_call = mod.get_global_var('func_4016')
func_4019_call = mutated_mod.get_global_var('func_4019')
var_4595 = relay.var("var_4595", dtype = "float32", shape = (600,))#candidate|4595|(600,)|var|float32
call_4594 = relay.TupleGetItem(func_4016_call(relay.reshape(var_4595.astype('float32'), [8, 15, 5])), 1)
call_4596 = relay.TupleGetItem(func_4019_call(relay.reshape(var_4595.astype('float32'), [8, 15, 5])), 1)
bop_4600 = relay.floor_mod(call_4550.astype('float32'), relay.reshape(const_4551.astype('float32'), relay.shape_of(call_4550))) # shape=(1134,)
bop_4603 = relay.floor_mod(call_4552.astype('float32'), relay.reshape(const_4551.astype('float32'), relay.shape_of(call_4552))) # shape=(1134,)
var_4612 = relay.var("var_4612", dtype = "float32", shape = (1134,))#candidate|4612|(1134,)|var|float32
bop_4613 = relay.left_shift(bop_4600.astype('uint32'), relay.reshape(var_4612.astype('uint32'), relay.shape_of(bop_4600))) # shape=(1134,)
bop_4616 = relay.left_shift(bop_4603.astype('uint32'), relay.reshape(var_4612.astype('uint32'), relay.shape_of(bop_4603))) # shape=(1134,)
uop_4617 = relay.erf(bop_4600.astype('float32')) # shape=(1134,)
uop_4619 = relay.erf(bop_4603.astype('float32')) # shape=(1134,)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_4627 = relay.TupleGetItem(func_2305_call(), 0)
call_4628 = relay.TupleGetItem(func_2307_call(), 0)
output = relay.Tuple([call_4546,call_4581,call_4594,var_4595,bop_4613,uop_4617,call_4627,])
output2 = relay.Tuple([call_4547,call_4582,call_4596,var_4595,bop_4616,uop_4619,call_4628,])
func_4650 = relay.Function([var_4595,var_4612,], output)
mod['func_4650'] = func_4650
mod = relay.transform.InferType()(mod)
var_4651 = relay.var("var_4651", dtype = "float32", shape = (600,))#candidate|4651|(600,)|var|float32
var_4652 = relay.var("var_4652", dtype = "float32", shape = (1134,))#candidate|4652|(1134,)|var|float32
output = func_4650(var_4651,var_4652,)
func_4653 = relay.Function([var_4651,var_4652,], output)
mutated_mod['func_4653'] = func_4653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3726_call = mod.get_global_var('func_3726')
func_3727_call = mutated_mod.get_global_var('func_3727')
call_4733 = relay.TupleGetItem(func_3726_call(), 1)
call_4734 = relay.TupleGetItem(func_3727_call(), 1)
uop_4744 = relay.asinh(call_4733.astype('float32')) # shape=(8, 1, 5)
uop_4746 = relay.asinh(call_4734.astype('float32')) # shape=(8, 1, 5)
output = uop_4744
output2 = uop_4746
func_4751 = relay.Function([], output)
mod['func_4751'] = func_4751
mod = relay.transform.InferType()(mod)
output = func_4751()
func_4752 = relay.Function([], output)
mutated_mod['func_4752'] = func_4752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mod.get_global_var('func_4280')
func_4281_call = mutated_mod.get_global_var('func_4281')
call_4775 = func_4280_call()
call_4776 = func_4280_call()
output = call_4775
output2 = call_4776
func_4778 = relay.Function([], output)
mod['func_4778'] = func_4778
mod = relay.transform.InferType()(mod)
output = func_4778()
func_4779 = relay.Function([], output)
mutated_mod['func_4779'] = func_4779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_4809 = func_2513_call()
call_4810 = func_2513_call()
func_2637_call = mod.get_global_var('func_2637')
func_2640_call = mutated_mod.get_global_var('func_2640')
var_4819 = relay.var("var_4819", dtype = "bool", shape = ())#candidate|4819|()|var|bool
call_4818 = relay.TupleGetItem(func_2637_call(relay.reshape(var_4819.astype('bool'), [])), 5)
call_4820 = relay.TupleGetItem(func_2640_call(relay.reshape(var_4819.astype('bool'), [])), 5)
output = relay.Tuple([call_4809,call_4818,var_4819,])
output2 = relay.Tuple([call_4810,call_4820,var_4819,])
func_4825 = relay.Function([var_4819,], output)
mod['func_4825'] = func_4825
mod = relay.transform.InferType()(mod)
var_4826 = relay.var("var_4826", dtype = "bool", shape = ())#candidate|4826|()|var|bool
output = func_4825(var_4826)
func_4827 = relay.Function([var_4826], output)
mutated_mod['func_4827'] = func_4827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3229_call = mod.get_global_var('func_3229')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_4839 = relay.TupleGetItem(func_3229_call(), 1)
call_4840 = relay.TupleGetItem(func_3231_call(), 1)
output = call_4839
output2 = call_4840
func_4856 = relay.Function([], output)
mod['func_4856'] = func_4856
mod = relay.transform.InferType()(mod)
mutated_mod['func_4856'] = func_4856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4856_call = mutated_mod.get_global_var('func_4856')
call_4857 = func_4856_call()
output = call_4857
func_4858 = relay.Function([], output)
mutated_mod['func_4858'] = func_4858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2337_call = mutated_mod.get_global_var('func_2337')
call_4903 = relay.TupleGetItem(func_2336_call(), 0)
call_4904 = relay.TupleGetItem(func_2337_call(), 0)
func_2019_call = mod.get_global_var('func_2019')
func_2022_call = mutated_mod.get_global_var('func_2022')
var_4922 = relay.var("var_4922", dtype = "float32", shape = (1400,))#candidate|4922|(1400,)|var|float32
call_4921 = func_2019_call(relay.reshape(var_4922.astype('float32'), [10, 10, 14]))
call_4923 = func_2019_call(relay.reshape(var_4922.astype('float32'), [10, 10, 14]))
uop_4938 = relay.rsqrt(var_4922.astype('float32')) # shape=(1400,)
output = relay.Tuple([call_4903,call_4921,uop_4938,])
output2 = relay.Tuple([call_4904,call_4923,uop_4938,])
func_4941 = relay.Function([var_4922,], output)
mod['func_4941'] = func_4941
mod = relay.transform.InferType()(mod)
var_4942 = relay.var("var_4942", dtype = "float32", shape = (1400,))#candidate|4942|(1400,)|var|float32
output = func_4941(var_4942)
func_4943 = relay.Function([var_4942], output)
mutated_mod['func_4943'] = func_4943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3632_call = mod.get_global_var('func_3632')
func_3634_call = mutated_mod.get_global_var('func_3634')
call_4951 = func_3632_call()
call_4952 = func_3632_call()
var_4954 = relay.var("var_4954", dtype = "bool", shape = (8, 3, 5))#candidate|4954|(8, 3, 5)|var|bool
bop_4955 = relay.bitwise_and(call_4951.astype('uint64'), relay.reshape(var_4954.astype('uint64'), relay.shape_of(call_4951))) # shape=(8, 3, 5)
bop_4958 = relay.bitwise_and(call_4952.astype('uint64'), relay.reshape(var_4954.astype('uint64'), relay.shape_of(call_4952))) # shape=(8, 3, 5)
output = bop_4955
output2 = bop_4958
func_4961 = relay.Function([var_4954,], output)
mod['func_4961'] = func_4961
mod = relay.transform.InferType()(mod)
var_4962 = relay.var("var_4962", dtype = "bool", shape = (8, 3, 5))#candidate|4962|(8, 3, 5)|var|bool
output = func_4961(var_4962)
func_4963 = relay.Function([var_4962], output)
mutated_mod['func_4963'] = func_4963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3229_call = mod.get_global_var('func_3229')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_5000 = relay.TupleGetItem(func_3229_call(), 2)
call_5001 = relay.TupleGetItem(func_3231_call(), 2)
func_3990_call = mod.get_global_var('func_3990')
func_3993_call = mutated_mod.get_global_var('func_3993')
var_5025 = relay.var("var_5025", dtype = "float32", shape = (320,))#candidate|5025|(320,)|var|float32
call_5024 = relay.TupleGetItem(func_3990_call(relay.reshape(var_5025.astype('float32'), [8, 8, 5])), 0)
call_5026 = relay.TupleGetItem(func_3993_call(relay.reshape(var_5025.astype('float32'), [8, 8, 5])), 0)
uop_5031 = relay.sigmoid(call_5024.astype('float32')) # shape=(8, 8, 5)
uop_5033 = relay.sigmoid(call_5026.astype('float32')) # shape=(8, 8, 5)
func_2135_call = mod.get_global_var('func_2135')
func_2139_call = mutated_mod.get_global_var('func_2139')
var_5035 = relay.var("var_5035", dtype = "uint16", shape = ())#candidate|5035|()|var|uint16
const_5036 = relay.const([10,-4,-9,-3,-2,-7,6,-2,4,-10,6,3,-6,-1,10,-6,9,-3,6,-1,3,-1,-4,2,10,-6,-1,-6,5,-9,-3,-5,5,-3,4,-1,-3,-5,-9,6,2,-8,8,-2,-3,-8,-6,-1,1,-3,-9,1,9,1,-7,-9,-9,-2,1,10,2,10,-10,-10,6,-5,10,-7,6,-8,4,-1,-2,-10,6,-9,-5,-6,-2,6,-2,1,9,-10,7,-9,5,4,3,-2,-1,7,2,2,2,9,1,5,-9,8,-4,7,-6,-9,-4,-8,-4,4,10,9,6,-5,10,-10,8,-7,2,2,-6,7,-3,-6,1,4,-7,-5,-3,-1,-2,-1,6,3,-1,-6,-5,6,1,7,-3,-5,-4,-3,-1,-9,3,3,10,-9,-10,-10,9,5,2,-4,-2,5,-7,4,-1,1,5,-5,-8,7,-1,-3,7,-2,1,-1,-3,1,-5,10,-8,-3,-4,1,3,2,-7,6,-4,-10,-4,-7,9,9,-3,-1,-1,-5,3,7,-5,1,5,-5,-6,3,10,-7,8,-3,6,-3,10,-1,5,10,8,-2,-9,-1,4,2,-6,2,-6,6,-1,-8,6,-6,7,10,7,8,9,-8,-7,-6,1,8,5,7,10,8,5,8,-10,-7,10,-1,-5,3,-1,-5,-9,10,-7,-9,-2,-5,-9,-9,9,5,9,10,7,8,-2,-10,7,2,-9,-1,8,-10,-8,7,4,9,-8,-9,-2,-4,-3,-5,6,-4,-10,6,10,-6,-2,8,-7,-1,-7,1,-9,-4,-9,3,-8,-8,2,8,-9,-4,9,9,10,2,-10,7,-6,-4,-9,2,-5,-8,6,1,-10,6,-7,-7,3,-6,-10,2,3,-3,-4,2,7,6,-5,7,-2,-7,8,-7,3,3,6,1,3,2,1,7,-1,1,10,3,1,-2,-4,-1,2,-10,1,-8,7,4,-1,8,-3,-9,-7,6,2,8,-7,-3,-2,9,-6,10,4,-3,-4,-8,8,-2,10,4,6,-6,-10,5,-1,7,-1,1,10,10,-5,-3,-6,7,-4,7,-2,4,1,-3,-4,-2,-7,10,-8,-5,1,-5,4,-4,-2,10,-2,-5,-4,9,-1,2,-5,7,-5,6,2,-2,5,7,-4,1,-1,-3,7,4,-3,3,-1,1,5,-9,-3,3,8,5,-5,10,-5,3,-4,-7,3,5,2,-7,7,4,-10,6,-7,10,9,9,4,3,9,5,2,6,-5,-1,-3,-10,3,1,-9,3,-2,10,-6,-3,3,-9,-7,-8,-1,5,-7,-7,3,10,8,9,-8,7,2,-3,10,-1,-8,-7,10,-3,7,7,7,-1], dtype = "int64")#candidate|5036|(504,)|const|int64
call_5034 = relay.TupleGetItem(func_2135_call(relay.reshape(var_5035.astype('uint16'), []), relay.reshape(call_5000.astype('uint16'), [6, 16, 12]), relay.reshape(const_5036.astype('int64'), [504,]), ), 0)
call_5037 = relay.TupleGetItem(func_2139_call(relay.reshape(var_5035.astype('uint16'), []), relay.reshape(call_5000.astype('uint16'), [6, 16, 12]), relay.reshape(const_5036.astype('int64'), [504,]), ), 0)
func_3990_call = mod.get_global_var('func_3990')
func_3993_call = mutated_mod.get_global_var('func_3993')
call_5040 = relay.TupleGetItem(func_3990_call(relay.reshape(uop_5031.astype('float32'), [8, 8, 5])), 0)
call_5041 = relay.TupleGetItem(func_3993_call(relay.reshape(uop_5031.astype('float32'), [8, 8, 5])), 0)
func_1241_call = mod.get_global_var('func_1241')
func_1246_call = mutated_mod.get_global_var('func_1246')
const_5051 = relay.const([True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False], dtype = "bool")#candidate|5051|(560,)|const|bool
call_5050 = relay.TupleGetItem(func_1241_call(relay.reshape(var_5035.astype('bool'), []), relay.reshape(const_5051.astype('bool'), [4, 10, 14]), relay.reshape(const_5036.astype('int64'), [504,]), ), 1)
call_5052 = relay.TupleGetItem(func_1246_call(relay.reshape(var_5035.astype('bool'), []), relay.reshape(const_5051.astype('bool'), [4, 10, 14]), relay.reshape(const_5036.astype('int64'), [504,]), ), 1)
uop_5056 = relay.tan(uop_5031.astype('float32')) # shape=(8, 8, 5)
uop_5058 = relay.tan(uop_5033.astype('float32')) # shape=(8, 8, 5)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_5069 = func_2513_call()
call_5070 = func_2513_call()
output = relay.Tuple([call_5000,var_5025,call_5034,var_5035,const_5036,call_5040,call_5050,const_5051,uop_5056,call_5069,])
output2 = relay.Tuple([call_5001,var_5025,call_5037,var_5035,const_5036,call_5041,call_5052,const_5051,uop_5058,call_5070,])
func_5074 = relay.Function([var_5025,var_5035,], output)
mod['func_5074'] = func_5074
mod = relay.transform.InferType()(mod)
mutated_mod['func_5074'] = func_5074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5074_call = mutated_mod.get_global_var('func_5074')
var_5076 = relay.var("var_5076", dtype = "float32", shape = (320,))#candidate|5076|(320,)|var|float32
var_5077 = relay.var("var_5077", dtype = "uint16", shape = ())#candidate|5077|()|var|uint16
call_5075 = func_5074_call(var_5076,var_5077,)
output = call_5075
func_5078 = relay.Function([var_5076,var_5077,], output)
mutated_mod['func_5078'] = func_5078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_5082 = relay.TupleGetItem(func_2813_call(), 6)
call_5083 = relay.TupleGetItem(func_2814_call(), 6)
uop_5086 = relay.sin(call_5082.astype('float64')) # shape=(8, 1, 5)
uop_5088 = relay.sin(call_5083.astype('float64')) # shape=(8, 1, 5)
output = uop_5086
output2 = uop_5088
func_5091 = relay.Function([], output)
mod['func_5091'] = func_5091
mod = relay.transform.InferType()(mod)
output = func_5091()
func_5092 = relay.Function([], output)
mutated_mod['func_5092'] = func_5092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_5152 = relay.TupleGetItem(func_2305_call(), 0)
call_5153 = relay.TupleGetItem(func_2307_call(), 0)
uop_5169 = relay.acos(call_5152.astype('float64')) # shape=(8, 1, 5)
uop_5171 = relay.acos(call_5153.astype('float64')) # shape=(8, 1, 5)
output = relay.Tuple([uop_5169,])
output2 = relay.Tuple([uop_5171,])
func_5173 = relay.Function([], output)
mod['func_5173'] = func_5173
mod = relay.transform.InferType()(mod)
output = func_5173()
func_5174 = relay.Function([], output)
mutated_mod['func_5174'] = func_5174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_5196 = relay.TupleGetItem(func_2813_call(), 3)
call_5197 = relay.TupleGetItem(func_2814_call(), 3)
output = call_5196
output2 = call_5197
func_5199 = relay.Function([], output)
mod['func_5199'] = func_5199
mod = relay.transform.InferType()(mod)
output = func_5199()
func_5200 = relay.Function([], output)
mutated_mod['func_5200'] = func_5200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3298_call = mod.get_global_var('func_3298')
func_3299_call = mutated_mod.get_global_var('func_3299')
call_5220 = relay.TupleGetItem(func_3298_call(), 0)
call_5221 = relay.TupleGetItem(func_3299_call(), 0)
func_3632_call = mod.get_global_var('func_3632')
func_3634_call = mutated_mod.get_global_var('func_3634')
call_5233 = func_3632_call()
call_5234 = func_3632_call()
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_5235 = relay.TupleGetItem(func_4065_call(), 0)
call_5236 = relay.TupleGetItem(func_4066_call(), 0)
func_3019_call = mod.get_global_var('func_3019')
func_3021_call = mutated_mod.get_global_var('func_3021')
var_5240 = relay.var("var_5240", dtype = "uint16", shape = ())#candidate|5240|()|var|uint16
call_5239 = relay.TupleGetItem(func_3019_call(relay.reshape(var_5240.astype('uint16'), [])), 1)
call_5241 = relay.TupleGetItem(func_3021_call(relay.reshape(var_5240.astype('uint16'), [])), 1)
func_2743_call = mod.get_global_var('func_2743')
func_2746_call = mutated_mod.get_global_var('func_2746')
var_5246 = relay.var("var_5246", dtype = "int16", shape = (1, 980))#candidate|5246|(1, 980)|var|int16
call_5245 = relay.TupleGetItem(func_2743_call(relay.reshape(var_5246.astype('int16'), [7, 10, 14])), 0)
call_5247 = relay.TupleGetItem(func_2746_call(relay.reshape(var_5246.astype('int16'), [7, 10, 14])), 0)
output = relay.Tuple([call_5220,call_5233,call_5235,call_5239,var_5240,call_5245,var_5246,])
output2 = relay.Tuple([call_5221,call_5234,call_5236,call_5241,var_5240,call_5247,var_5246,])
func_5252 = relay.Function([var_5240,var_5246,], output)
mod['func_5252'] = func_5252
mod = relay.transform.InferType()(mod)
mutated_mod['func_5252'] = func_5252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5252_call = mutated_mod.get_global_var('func_5252')
var_5254 = relay.var("var_5254", dtype = "uint16", shape = ())#candidate|5254|()|var|uint16
var_5255 = relay.var("var_5255", dtype = "int16", shape = (1, 980))#candidate|5255|(1, 980)|var|int16
call_5253 = func_5252_call(var_5254,var_5255,)
output = call_5253
func_5256 = relay.Function([var_5254,var_5255,], output)
mutated_mod['func_5256'] = func_5256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4459_call = mod.get_global_var('func_4459')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_5258 = relay.TupleGetItem(func_4459_call(), 2)
call_5259 = relay.TupleGetItem(func_4461_call(), 2)
output = relay.Tuple([call_5258,])
output2 = relay.Tuple([call_5259,])
func_5274 = relay.Function([], output)
mod['func_5274'] = func_5274
mod = relay.transform.InferType()(mod)
mutated_mod['func_5274'] = func_5274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5274_call = mutated_mod.get_global_var('func_5274')
call_5275 = func_5274_call()
output = call_5275
func_5276 = relay.Function([], output)
mutated_mod['func_5276'] = func_5276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4459_call = mod.get_global_var('func_4459')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_5294 = relay.TupleGetItem(func_4459_call(), 4)
call_5295 = relay.TupleGetItem(func_4461_call(), 4)
uop_5303 = relay.asinh(call_5294.astype('float32')) # shape=(10, 10, 14)
uop_5305 = relay.asinh(call_5295.astype('float32')) # shape=(10, 10, 14)
func_3917_call = mod.get_global_var('func_3917')
func_3919_call = mutated_mod.get_global_var('func_3919')
const_5308 = relay.const([[-1,3,4,3,10,5,-1,-8,-3,8,7,-10,-10,4,4,-9,8,-4,9,2,-1,3,-5,-10,7,2,1,-10,4,-10,4,1,1,-4,-1,10,-7,-5,-5,-1,-2,-6,-7,-6,8,9,-5,-6,6,-9,-10,2,-3,10,-3,-10,-5,7,-3,-5,9,7,-4,2,-4,-10,1,4,10,-4,4,-7,-2,-3,9,8,-9,4,9,-7,9,9,-1,6,6,2,5,3,4,-4,1,1,-6,-5,-2,-10,-2,-1,-2,4,-6,-2,-8,10,-8]], dtype = "uint64")#candidate|5308|(1, 105)|const|uint64
call_5307 = relay.TupleGetItem(func_3917_call(relay.reshape(const_5308.astype('uint64'), [7, 3, 5])), 0)
call_5309 = relay.TupleGetItem(func_3919_call(relay.reshape(const_5308.astype('uint64'), [7, 3, 5])), 0)
bop_5311 = relay.power(uop_5303.astype('float64'), relay.reshape(call_5294.astype('float64'), relay.shape_of(uop_5303))) # shape=(10, 10, 14)
bop_5314 = relay.power(uop_5305.astype('float64'), relay.reshape(call_5295.astype('float64'), relay.shape_of(uop_5305))) # shape=(10, 10, 14)
func_1716_call = mod.get_global_var('func_1716')
func_1718_call = mutated_mod.get_global_var('func_1718')
var_5322 = relay.var("var_5322", dtype = "float32", shape = (1134,))#candidate|5322|(1134,)|var|float32
call_5321 = relay.TupleGetItem(func_1716_call(relay.reshape(var_5322.astype('float32'), [9, 14, 9])), 0)
call_5323 = relay.TupleGetItem(func_1718_call(relay.reshape(var_5322.astype('float32'), [9, 14, 9])), 0)
output = relay.Tuple([call_5307,const_5308,bop_5311,call_5321,var_5322,])
output2 = relay.Tuple([call_5309,const_5308,bop_5314,call_5323,var_5322,])
func_5324 = relay.Function([var_5322,], output)
mod['func_5324'] = func_5324
mod = relay.transform.InferType()(mod)
mutated_mod['func_5324'] = func_5324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5325 = relay.var("var_5325", dtype = "float32", shape = (1134,))#candidate|5325|(1134,)|var|float32
func_5324_call = mutated_mod.get_global_var('func_5324')
call_5326 = func_5324_call(var_5325)
output = call_5326
func_5327 = relay.Function([var_5325], output)
mutated_mod['func_5327'] = func_5327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4856_call = mod.get_global_var('func_4856')
func_4858_call = mutated_mod.get_global_var('func_4858')
call_5340 = func_4856_call()
call_5341 = func_4856_call()
output = call_5340
output2 = call_5341
func_5342 = relay.Function([], output)
mod['func_5342'] = func_5342
mod = relay.transform.InferType()(mod)
mutated_mod['func_5342'] = func_5342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5342_call = mutated_mod.get_global_var('func_5342')
call_5343 = func_5342_call()
output = call_5343
func_5344 = relay.Function([], output)
mutated_mod['func_5344'] = func_5344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3298_call = mod.get_global_var('func_3298')
func_3299_call = mutated_mod.get_global_var('func_3299')
call_5486 = relay.TupleGetItem(func_3298_call(), 0)
call_5487 = relay.TupleGetItem(func_3299_call(), 0)
uop_5488 = relay.acosh(call_5486.astype('float32')) # shape=(8, 1, 5)
uop_5490 = relay.acosh(call_5487.astype('float32')) # shape=(8, 1, 5)
func_3990_call = mod.get_global_var('func_3990')
func_3993_call = mutated_mod.get_global_var('func_3993')
const_5492 = relay.const([[-5.349138,5.603621,-5.040550,2.143689,-5.585444,3.344619,4.539091,-1.018522,-7.044946,-9.386510,-0.518009,-6.764221,-8.162206,-5.599678,8.887108,-5.778165,1.895882,-5.225153,9.647337,8.019890,8.789137,1.010250,-4.058167,5.294812,5.039588,-5.721638,-4.657525,1.200720,-7.083838,4.627601,-6.082397,0.612923,2.832396,6.261190,-8.096125,-2.322794,-9.991389,-4.454456,-4.597213,1.103011],[4.507413,0.004315,-1.288568,-7.768736,-2.567717,8.874208,-4.023706,-3.024935,-0.801392,-7.549424,-3.940425,-5.331825,-6.670496,5.113135,4.194825,7.705689,3.306861,-8.844534,2.817829,-9.883455,2.942555,3.111804,9.837098,3.147933,7.275533,-7.325180,9.279612,-9.035241,7.905056,-0.395859,-6.802679,8.047173,-6.239440,-6.751916,-2.856075,-3.757528,-7.326141,1.058860,4.013403,6.188225],[7.491237,0.311516,3.196322,-8.371634,6.460551,3.459122,-1.855015,5.983425,-7.522369,9.482092,2.902894,-4.308821,2.248846,4.494790,2.468301,0.593258,-2.265606,4.108306,2.076118,-4.146203,-1.276610,-1.777213,-3.343142,5.041644,1.918237,9.840425,-1.854074,-2.839619,-4.819038,0.718886,0.077377,-7.823884,2.059358,9.840166,7.522315,1.021563,2.259594,0.039711,-1.383112,-6.290902],[7.952313,-0.364785,-8.423481,5.697485,-8.564766,-5.711013,6.777244,7.063824,-7.035426,1.700867,-2.250245,8.089692,3.707372,1.416835,0.612980,6.704319,1.390715,3.605701,1.338945,-5.460475,6.898571,0.557978,3.521682,4.536488,6.388886,-1.613655,8.851959,2.098416,-3.218282,-7.597241,-8.114943,-3.219282,8.615399,3.300936,-1.404317,-2.675739,-5.855809,-3.118789,-9.099420,7.893344],[5.930542,9.792112,3.250262,4.668542,8.161976,-6.236511,6.284018,-0.485584,-6.369133,0.434366,1.778468,-4.407702,9.728309,-3.460953,-0.501586,5.632010,1.786147,-9.040689,1.595860,-1.749880,-8.742540,1.839991,8.693992,-0.721607,6.428899,-7.016967,-5.806159,9.430374,6.542824,8.649231,6.309779,7.105117,-3.760260,-3.788946,6.672778,-5.004978,0.885264,-6.415380,8.067377,-1.312026],[-0.206062,-4.395247,3.939237,3.148374,7.800181,-4.646280,9.621274,6.949977,1.478492,-9.776148,-3.267022,-5.169744,-6.408215,-4.653074,-9.358934,-9.528459,5.095968,8.966297,-6.902014,7.274368,0.125469,6.608380,-1.943625,-1.324527,-0.914653,-6.347796,-8.730323,-4.999345,5.572209,-0.575194,5.832834,6.342665,7.751055,7.965961,1.535798,8.784526,-9.889146,2.498223,2.604811,-0.500483],[-2.868677,-2.204376,-7.753111,0.312600,9.240424,7.180960,5.026681,2.276143,5.097172,-6.879460,-3.846406,7.026283,-7.915229,3.858206,2.499573,6.085519,-3.704072,-4.422289,-2.330785,0.135654,7.063757,-5.414493,2.385193,-0.714845,-2.129402,3.652150,-4.976320,5.898183,1.880969,0.419486,7.125946,7.938859,-7.281035,-5.186429,0.235229,9.248648,-3.165586,2.294392,3.353191,-1.020196],[5.104575,-5.082839,-9.531284,-7.396293,-3.638428,-9.373492,3.655282,-5.105673,6.400682,-3.389364,-5.263830,-7.514494,-0.732328,-5.882606,0.821682,2.119443,-8.162133,-2.487869,-9.013428,-6.919121,-1.111121,-4.232387,-1.226226,-2.504790,3.953705,9.541787,-7.646912,-1.338872,0.217319,-4.784394,6.752278,6.279934,-1.032490,-2.395984,7.586712,1.696843,-0.610194,9.453045,-5.693874,-8.340695]], dtype = "float32")#candidate|5492|(8, 40)|const|float32
call_5491 = relay.TupleGetItem(func_3990_call(relay.reshape(const_5492.astype('float32'), [8, 8, 5])), 0)
call_5493 = relay.TupleGetItem(func_3993_call(relay.reshape(const_5492.astype('float32'), [8, 8, 5])), 0)
output = relay.Tuple([uop_5488,call_5491,const_5492,])
output2 = relay.Tuple([uop_5490,call_5493,const_5492,])
func_5506 = relay.Function([], output)
mod['func_5506'] = func_5506
mod = relay.transform.InferType()(mod)
mutated_mod['func_5506'] = func_5506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5506_call = mutated_mod.get_global_var('func_5506')
call_5507 = func_5506_call()
output = call_5507
func_5508 = relay.Function([], output)
mutated_mod['func_5508'] = func_5508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
call_5513 = relay.TupleGetItem(func_2305_call(), 0)
call_5514 = relay.TupleGetItem(func_2307_call(), 0)
output = call_5513
output2 = call_5514
func_5529 = relay.Function([], output)
mod['func_5529'] = func_5529
mod = relay.transform.InferType()(mod)
mutated_mod['func_5529'] = func_5529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5529_call = mutated_mod.get_global_var('func_5529')
call_5530 = func_5529_call()
output = call_5530
func_5531 = relay.Function([], output)
mutated_mod['func_5531'] = func_5531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4153_call = mod.get_global_var('func_4153')
func_4154_call = mutated_mod.get_global_var('func_4154')
call_5539 = relay.TupleGetItem(func_4153_call(), 0)
call_5540 = relay.TupleGetItem(func_4154_call(), 0)
output = call_5539
output2 = call_5540
func_5545 = relay.Function([], output)
mod['func_5545'] = func_5545
mod = relay.transform.InferType()(mod)
output = func_5545()
func_5546 = relay.Function([], output)
mutated_mod['func_5546'] = func_5546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2571_call = mod.get_global_var('func_2571')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_5566 = relay.TupleGetItem(func_2571_call(), 0)
call_5567 = relay.TupleGetItem(func_2572_call(), 0)
func_2378_call = mod.get_global_var('func_2378')
func_2380_call = mutated_mod.get_global_var('func_2380')
const_5575 = relay.const([-0.714190,-9.752057,3.962192,-4.449273,-9.724360,-0.418355,6.995848,8.465532,-1.446947,-5.098259,9.204121,8.598798,6.456134,5.865467,-6.302844,2.315104,0.702492,7.349721,-2.201147,-3.390410,-8.905507,-0.470380,-2.927451,-5.371492,2.493969,-2.303405,-6.170789,-5.876641,-9.716331,-3.190984,-2.805269,2.276311,-5.790203,-6.733067,5.081737,1.617490,0.952303,4.947488,-8.075985,-0.809604,-2.401546,-9.649013,-4.364358,8.982021,6.836972,3.123469,5.282000,8.028105,-9.127326,-5.982449,-8.333969,8.648109,2.450319,-2.661310,-7.445290,7.470970,1.748700,-4.385295,-2.776112,-0.989856,3.826420,0.367505,9.128419,-5.663041,-8.600158,2.923494,4.314826,-4.374312,6.541358,-3.754153,-5.798124,5.350799,4.494721,0.757386,0.746071,1.842904,-9.332190,0.862378,-8.714636,6.956165,-3.949484,9.250531,4.599867,-3.612682,-7.185072,-0.069121,-0.566131,-7.161553,3.590551,9.670207,-3.907592,-1.662777,-8.111057,-4.625972,7.188195,3.714317,-1.342908,1.579582,5.121511,-9.798180,-7.001793,-6.471903,-0.995633,4.832689,-9.583307,-6.204768,0.351706,6.879271,-6.735420,-2.066465,6.529720,5.791285,3.113811,2.876525,-6.366663,-9.152084,9.164315,2.314778,-3.158562,7.069496,-8.460683,6.669423,-6.429461,4.989532,-8.827510,7.315841,5.424926,5.769795], dtype = "float32")#candidate|5575|(128,)|const|float32
call_5574 = func_2378_call(relay.reshape(const_5575.astype('float32'), [8, 1, 16]))
call_5576 = func_2378_call(relay.reshape(const_5575.astype('float32'), [8, 1, 16]))
output = relay.Tuple([call_5566,call_5574,const_5575,])
output2 = relay.Tuple([call_5567,call_5576,const_5575,])
func_5577 = relay.Function([], output)
mod['func_5577'] = func_5577
mod = relay.transform.InferType()(mod)
mutated_mod['func_5577'] = func_5577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mutated_mod.get_global_var('func_5577')
call_5578 = func_5577_call()
output = call_5578
func_5579 = relay.Function([], output)
mutated_mod['func_5579'] = func_5579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5545_call = mod.get_global_var('func_5545')
func_5546_call = mutated_mod.get_global_var('func_5546')
call_5608 = func_5545_call()
call_5609 = func_5545_call()
func_3726_call = mod.get_global_var('func_3726')
func_3727_call = mutated_mod.get_global_var('func_3727')
call_5615 = relay.TupleGetItem(func_3726_call(), 0)
call_5616 = relay.TupleGetItem(func_3727_call(), 0)
func_4961_call = mod.get_global_var('func_4961')
func_4963_call = mutated_mod.get_global_var('func_4963')
var_5628 = relay.var("var_5628", dtype = "bool", shape = (120,))#candidate|5628|(120,)|var|bool
call_5627 = func_4961_call(relay.reshape(var_5628.astype('bool'), [8, 3, 5]))
call_5629 = func_4961_call(relay.reshape(var_5628.astype('bool'), [8, 3, 5]))
func_3124_call = mod.get_global_var('func_3124')
func_3126_call = mutated_mod.get_global_var('func_3126')
call_5639 = relay.TupleGetItem(func_3124_call(relay.reshape(call_5627.astype('float32'), [8, 3, 5])), 1)
call_5640 = relay.TupleGetItem(func_3126_call(relay.reshape(call_5627.astype('float32'), [8, 3, 5])), 1)
output = relay.Tuple([call_5608,call_5615,call_5627,var_5628,call_5639,])
output2 = relay.Tuple([call_5609,call_5616,call_5629,var_5628,call_5640,])
func_5648 = relay.Function([var_5628,], output)
mod['func_5648'] = func_5648
mod = relay.transform.InferType()(mod)
mutated_mod['func_5648'] = func_5648
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5649 = relay.var("var_5649", dtype = "bool", shape = (120,))#candidate|5649|(120,)|var|bool
func_5648_call = mutated_mod.get_global_var('func_5648')
call_5650 = func_5648_call(var_5649)
output = call_5650
func_5651 = relay.Function([var_5649], output)
mutated_mod['func_5651'] = func_5651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_5704 = relay.TupleGetItem(func_2813_call(), 1)
call_5705 = relay.TupleGetItem(func_2814_call(), 1)
output = call_5704
output2 = call_5705
func_5710 = relay.Function([], output)
mod['func_5710'] = func_5710
mod = relay.transform.InferType()(mod)
output = func_5710()
func_5711 = relay.Function([], output)
mutated_mod['func_5711'] = func_5711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_5736 = relay.TupleGetItem(func_2813_call(), 5)
call_5737 = relay.TupleGetItem(func_2814_call(), 5)
var_5749 = relay.var("var_5749", dtype = "float32", shape = (8, 1, 5))#candidate|5749|(8, 1, 5)|var|float32
bop_5750 = relay.bitwise_xor(call_5736.astype('int32'), relay.reshape(var_5749.astype('int32'), relay.shape_of(call_5736))) # shape=(8, 1, 5)
bop_5753 = relay.bitwise_xor(call_5737.astype('int32'), relay.reshape(var_5749.astype('int32'), relay.shape_of(call_5737))) # shape=(8, 1, 5)
output = bop_5750
output2 = bop_5753
func_5762 = relay.Function([var_5749,], output)
mod['func_5762'] = func_5762
mod = relay.transform.InferType()(mod)
mutated_mod['func_5762'] = func_5762
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5763 = relay.var("var_5763", dtype = "float32", shape = (8, 1, 5))#candidate|5763|(8, 1, 5)|var|float32
func_5762_call = mutated_mod.get_global_var('func_5762')
call_5764 = func_5762_call(var_5763)
output = call_5764
func_5765 = relay.Function([var_5763], output)
mutated_mod['func_5765'] = func_5765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5710_call = mod.get_global_var('func_5710')
func_5711_call = mutated_mod.get_global_var('func_5711')
call_5898 = func_5710_call()
call_5899 = func_5710_call()
func_5252_call = mod.get_global_var('func_5252')
func_5256_call = mutated_mod.get_global_var('func_5256')
const_5907 = relay.const(2, dtype = "uint16")#candidate|5907|()|const|uint16
var_5908 = relay.var("var_5908", dtype = "int16", shape = (980,))#candidate|5908|(980,)|var|int16
call_5906 = relay.TupleGetItem(func_5252_call(relay.reshape(const_5907.astype('uint16'), []), relay.reshape(var_5908.astype('int16'), [1, 980]), ), 3)
call_5909 = relay.TupleGetItem(func_5256_call(relay.reshape(const_5907.astype('uint16'), []), relay.reshape(var_5908.astype('int16'), [1, 980]), ), 3)
bop_5910 = relay.add(call_5898.astype('uint32'), const_5907.astype('uint32')) # shape=(8, 1, 5)
bop_5913 = relay.add(call_5899.astype('uint32'), const_5907.astype('uint32')) # shape=(8, 1, 5)
func_3778_call = mod.get_global_var('func_3778')
func_3780_call = mutated_mod.get_global_var('func_3780')
var_5919 = relay.var("var_5919", dtype = "float32", shape = (1134,))#candidate|5919|(1134,)|var|float32
call_5918 = relay.TupleGetItem(func_3778_call(relay.reshape(var_5919.astype('float32'), [1134,])), 2)
call_5920 = relay.TupleGetItem(func_3780_call(relay.reshape(var_5919.astype('float32'), [1134,])), 2)
uop_5927 = relay.sqrt(var_5908.astype('float32')) # shape=(980,)
func_4280_call = mod.get_global_var('func_4280')
func_4281_call = mutated_mod.get_global_var('func_4281')
call_5932 = func_4280_call()
call_5933 = func_4280_call()
output = relay.Tuple([call_5906,bop_5910,call_5918,var_5919,uop_5927,call_5932,])
output2 = relay.Tuple([call_5909,bop_5913,call_5920,var_5919,uop_5927,call_5933,])
func_5941 = relay.Function([var_5908,var_5919,], output)
mod['func_5941'] = func_5941
mod = relay.transform.InferType()(mod)
mutated_mod['func_5941'] = func_5941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5941_call = mutated_mod.get_global_var('func_5941')
var_5943 = relay.var("var_5943", dtype = "int16", shape = (980,))#candidate|5943|(980,)|var|int16
var_5944 = relay.var("var_5944", dtype = "float32", shape = (1134,))#candidate|5944|(1134,)|var|float32
call_5942 = func_5941_call(var_5943,var_5944,)
output = call_5942
func_5945 = relay.Function([var_5943,var_5944,], output)
mutated_mod['func_5945'] = func_5945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4153_call = mod.get_global_var('func_4153')
func_4154_call = mutated_mod.get_global_var('func_4154')
call_5947 = relay.TupleGetItem(func_4153_call(), 0)
call_5948 = relay.TupleGetItem(func_4154_call(), 0)
output = relay.Tuple([call_5947,])
output2 = relay.Tuple([call_5948,])
func_5949 = relay.Function([], output)
mod['func_5949'] = func_5949
mod = relay.transform.InferType()(mod)
mutated_mod['func_5949'] = func_5949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5949_call = mutated_mod.get_global_var('func_5949')
call_5950 = func_5949_call()
output = call_5950
func_5951 = relay.Function([], output)
mutated_mod['func_5951'] = func_5951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_5981 = relay.TupleGetItem(func_5577_call(), 0)
call_5982 = relay.TupleGetItem(func_5579_call(), 0)
func_1241_call = mod.get_global_var('func_1241')
func_1246_call = mutated_mod.get_global_var('func_1246')
const_5987 = relay.const(False, dtype = "bool")#candidate|5987|()|const|bool
const_5988 = relay.const([False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,True], dtype = "bool")#candidate|5988|(560,)|const|bool
const_5989 = relay.const([8,-2,-2,-3,-6,-9,-8,5,8,9,9,7,-5,-9,-5,-5,-10,10,-1,6,9,-6,6,1,7,6,-5,-5,-9,1,9,-8,3,5,-1,1,6,-7,9,6,7,-2,-4,-3,3,8,-10,-3,4,-6,8,-7,5,7,-3,1,-7,-2,-10,-4,7,-7,10,-9,-9,-1,2,-1,5,2,3,8,4,10,5,1,8,10,-7,4,5,2,5,-6,-3,10,10,7,10,-2,-3,-8,8,-1,-8,-2,10,2,-1,-8,7,-2,8,2,7,4,4,3,9,-10,6,-1,6,-4,4,-1,1,-7,-3,8,3,-1,3,1,-7,10,3,-4,9,-5,-1,3,2,-3,-8,-8,-3,8,-5,10,1,7,-3,4,8,-4,-8,1,4,-8,4,-5,-4,-3,-3,-3,4,10,-1,-9,4,8,-10,-3,-10,9,8,1,7,3,8,8,-3,7,-3,-3,-2,8,-7,-6,-3,-2,-9,2,-6,9,10,4,-6,-9,1,-3,-2,-3,-3,7,4,-8,2,-8,-7,-10,4,2,9,6,-3,1,3,6,2,5,-3,-8,3,3,5,-8,-9,9,-2,-8,-8,-10,-4,9,10,-4,7,7,-10,-1,-6,-5,9,-5,-3,-8,1,-3,4,10,6,-6,6,2,-6,2,-1,-6,-3,5,-1,8,-1,-6,-3,-1,-10,1,-2,3,-5,9,2,-10,6,2,8,-1,10,-6,-8,3,5,6,-6,-5,-2,1,-2,10,8,-7,-1,-7,-10,6,-9,-5,-3,-2,-10,10,-3,-9,-1,7,2,-6,-4,5,-6,-3,-10,-9,-1,-1,-10,-4,-3,-10,-1,-6,10,-7,-4,2,5,-7,6,-7,-9,-8,1,-1,-7,9,-7,3,6,6,4,2,-3,-6,6,-6,4,-1,-7,7,3,-2,-10,10,6,-6,3,-2,8,5,-5,-9,2,4,-2,3,-1,-6,9,5,-3,6,8,2,7,-9,6,-1,-10,10,-10,-7,-8,-9,10,-2,6,9,-5,-1,-6,-5,10,3,-1,-10,-5,-1,2,10,6,7,10,-6,-6,-7,7,7,8,-7,-4,-1,8,4,1,-3,5,-9,-7,10,-1,-10,-9,-8,-8,5,6,2,7,3,9,-5,8,-1,-8,-2,8,-9,-8,3,4,9,5,3,7,-9,1,-3,9,-6,3,-8,-10,9,8,4,-3,3,2,7,1,8,-2,-3,-4,-10,8,9,6,4,3,7,10,-1,5,4,4,8,-4,6,1,-5,5,5,-6,-5,-10,5,2,4,4,3,-1,-5,-1,3,9,9,5,-5,-6,10,-5,-5,10,6,7,-5,10,5,3,3], dtype = "int64")#candidate|5989|(504,)|const|int64
call_5986 = relay.TupleGetItem(func_1241_call(relay.reshape(const_5987.astype('bool'), []), relay.reshape(const_5988.astype('bool'), [4, 10, 14]), relay.reshape(const_5989.astype('int64'), [504,]), ), 0)
call_5990 = relay.TupleGetItem(func_1246_call(relay.reshape(const_5987.astype('bool'), []), relay.reshape(const_5988.astype('bool'), [4, 10, 14]), relay.reshape(const_5989.astype('int64'), [504,]), ), 0)
output = relay.Tuple([call_5981,call_5986,const_5987,const_5988,const_5989,])
output2 = relay.Tuple([call_5982,call_5990,const_5987,const_5988,const_5989,])
func_5997 = relay.Function([], output)
mod['func_5997'] = func_5997
mod = relay.transform.InferType()(mod)
output = func_5997()
func_5998 = relay.Function([], output)
mutated_mod['func_5998'] = func_5998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4778_call = mod.get_global_var('func_4778')
func_4779_call = mutated_mod.get_global_var('func_4779')
call_6029 = func_4778_call()
call_6030 = func_4778_call()
func_3229_call = mod.get_global_var('func_3229')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_6044 = relay.TupleGetItem(func_3229_call(), 0)
call_6045 = relay.TupleGetItem(func_3231_call(), 0)
func_5199_call = mod.get_global_var('func_5199')
func_5200_call = mutated_mod.get_global_var('func_5200')
call_6049 = func_5199_call()
call_6050 = func_5199_call()
func_3019_call = mod.get_global_var('func_3019')
func_3021_call = mutated_mod.get_global_var('func_3021')
const_6057 = relay.const(3, dtype = "uint16")#candidate|6057|()|const|uint16
call_6056 = relay.TupleGetItem(func_3019_call(relay.reshape(const_6057.astype('uint16'), [])), 1)
call_6058 = relay.TupleGetItem(func_3021_call(relay.reshape(const_6057.astype('uint16'), [])), 1)
output = relay.Tuple([call_6029,call_6044,call_6049,call_6056,const_6057,])
output2 = relay.Tuple([call_6030,call_6045,call_6050,call_6058,const_6057,])
func_6059 = relay.Function([], output)
mod['func_6059'] = func_6059
mod = relay.transform.InferType()(mod)
output = func_6059()
func_6060 = relay.Function([], output)
mutated_mod['func_6060'] = func_6060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mod.get_global_var('func_4280')
func_4281_call = mutated_mod.get_global_var('func_4281')
call_6076 = func_4280_call()
call_6077 = func_4280_call()
output = relay.Tuple([call_6076,])
output2 = relay.Tuple([call_6077,])
func_6096 = relay.Function([], output)
mod['func_6096'] = func_6096
mod = relay.transform.InferType()(mod)
mutated_mod['func_6096'] = func_6096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6096_call = mutated_mod.get_global_var('func_6096')
call_6097 = func_6096_call()
output = call_6097
func_6098 = relay.Function([], output)
mutated_mod['func_6098'] = func_6098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5342_call = mod.get_global_var('func_5342')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_6110 = func_5342_call()
call_6111 = func_5342_call()
func_5091_call = mod.get_global_var('func_5091')
func_5092_call = mutated_mod.get_global_var('func_5092')
call_6112 = func_5091_call()
call_6113 = func_5091_call()
output = relay.Tuple([call_6110,call_6112,])
output2 = relay.Tuple([call_6111,call_6113,])
func_6120 = relay.Function([], output)
mod['func_6120'] = func_6120
mod = relay.transform.InferType()(mod)
mutated_mod['func_6120'] = func_6120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6120_call = mutated_mod.get_global_var('func_6120')
call_6121 = func_6120_call()
output = call_6121
func_6122 = relay.Function([], output)
mutated_mod['func_6122'] = func_6122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4856_call = mod.get_global_var('func_4856')
func_4858_call = mutated_mod.get_global_var('func_4858')
call_6143 = func_4856_call()
call_6144 = func_4856_call()
output = relay.Tuple([call_6143,])
output2 = relay.Tuple([call_6144,])
func_6168 = relay.Function([], output)
mod['func_6168'] = func_6168
mod = relay.transform.InferType()(mod)
output = func_6168()
func_6169 = relay.Function([], output)
mutated_mod['func_6169'] = func_6169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5997_call = mod.get_global_var('func_5997')
func_5998_call = mutated_mod.get_global_var('func_5998')
call_6257 = relay.TupleGetItem(func_5997_call(), 0)
call_6258 = relay.TupleGetItem(func_5998_call(), 0)
func_2442_call = mod.get_global_var('func_2442')
func_2445_call = mutated_mod.get_global_var('func_2445')
const_6261 = relay.const([-1.764333,6.296871,-7.003632,-2.869110,-0.807950,-6.518386,-8.434038,-8.821582,-2.562634,9.638794,3.599992,-5.470836,-0.024535,-3.038119,0.369460,-7.822794,-6.019081,3.887331,-2.066792,5.347544,1.640316,-5.853326,-1.084814,2.037091,-0.327864,5.953301,-0.981149,5.660126,8.550656,2.494488,-0.880332,-9.024384,3.815238,7.701222,3.713195,-0.348705,-1.396019,-5.448911,3.304654,2.955897,-1.552901,-9.240630,4.533337,-8.160539,7.933816,0.131757,2.794180,9.436467,-7.481333,7.570706,9.519555,-7.424335,-0.298750,-5.533939,-1.332725,9.191268,-0.220750,1.717613,-3.530457,3.540030,9.280511,5.192407,-6.852730,1.423524,-7.036790,7.818721,-9.476883,6.767182,-5.014850,3.778062,-1.255333,-9.560550,-9.512822,-7.092934,2.660072,-4.902976,-5.487498,1.605366,-3.666869,9.229722,8.872406,-9.797124,-8.023191,-1.497572,1.820929,8.207179,9.111150,3.729915,-6.949235,-9.698251,3.893346,-1.204882,-8.261104,-3.610992,5.715642,4.653026,-1.054112,-1.516011,-6.727390,-8.788402,-1.816617,3.967449,7.086758,7.708259,-9.316741,5.113964,3.579619,6.198470,8.212835,-4.189957,-8.097616,-2.529052,-1.250097,5.222718,1.118692,-0.306821,-2.980498,0.723974,-6.924780,1.469613,-3.619463,-4.837221,-3.082181,-3.366379,-9.283533,-5.962287,-5.133017,2.522318,-7.299362,1.000691,-8.481743,8.702331,3.490654,-1.086199,-4.703446,-6.173617,-3.794861,-9.365471,7.971641,8.948253,9.125712,-2.746805,-7.215714,-6.616057,-9.699862,-2.107096,-3.693812,5.331280,2.354465,8.307856,3.281753,-7.676627,9.103533,9.714425,8.252431,-5.302373,-8.558582,3.206038,-0.347448,4.367349,3.570300,-2.304995,-7.707492,-4.078705,8.846962,7.144665,1.843008,3.959812,-9.797824,1.270046,9.075721,-0.378551,-2.319336,-8.592709,-3.373411,-5.445480,1.441628,8.065157,-4.021834,1.077502,4.582536,6.232566,8.719584,5.067010,7.292890,2.673893,-0.429532,-0.828882,2.102330,-1.800993,5.736154,-9.674926,8.759512,-9.500875,0.246052,4.058571,-7.020535,7.293693,2.908576,8.244479,-1.494283,4.986913,-5.863742,8.191016,-5.260623,0.346056,-5.384853,0.447481,9.418549,-7.488560,6.931428,-2.681848,-2.882739,7.680876,-3.919252,-3.403950,-2.851171,-7.278729,9.860945,-1.811236,9.807327,5.394771,5.892565,7.993247,-9.722764,1.444317,9.399747,7.390083,-5.817685,-2.902159,2.911204,4.074143,-0.220435,0.935243,5.310939,-3.496363,6.484313,9.427245,-7.028770,-6.993896,-9.216205,-5.762161,3.256730,2.382489,8.852169,-1.749030,-9.601260,-4.083792,9.406708,-4.746598,0.035948,5.684663,7.945301,-6.422977,8.888412,-1.037664,-9.237653,-1.867458,9.413392,0.089040,6.612592,7.242639,9.767545,-9.695919,3.067584,-9.340179,4.217293,-0.901293,-7.619568,-9.795966,8.542586,0.351776,-4.458360,9.275631,6.703168,-6.359255,-4.931535,-5.244872,8.022678,2.262506,1.513927,8.955836,9.348554,9.926657,-7.677553,-8.687327,2.486870,-2.812891,3.638973,2.842627,-5.331169,2.406459,8.439696,0.502340,-4.480415,-2.961196,-2.925962,4.523873,2.442847,8.013657,-8.769290,7.521676,6.402168,4.850728,0.217797,9.496707,-8.263952,-6.175774,-3.958959,-7.864865,-4.530851,-0.552594,2.725435,8.568094,9.026388,-1.289905,-5.282452,0.216796,5.165741,-9.450327,6.311878,4.178550,-2.540649,9.628505,5.785652,0.383625,-4.427942,-0.757495,7.521612,-6.281384,-8.885725,4.023524,-0.823532,-0.739162,8.907732,-8.378306,-9.498793,1.557938,-2.363986,7.201852,-9.943221,3.648635,-2.804056,-3.637729,0.041643,-4.053536,-2.224127,-1.420227,-4.595178,-0.897791,1.674108,-6.215496,-6.426610,-2.055876,2.996267,-8.731196,7.002848,-9.345871,7.005735,4.558156,-8.256422,-2.221154,9.569587,9.602010,7.366881,-6.486567,1.092088,-4.208504,-6.772012,-2.350384,-0.017679,0.214035,-3.169967,-4.284738,8.654108,1.951767,7.483852,-6.846659,-7.604123,3.193850,5.073074,3.924341,-7.160844,1.727677,-3.699088,-8.588235,-9.173802,-4.987538,-8.504670,1.673927,1.016900,3.800973,-4.894122,4.188329,8.136058,7.410144,-5.776412,1.267864,-1.724748,5.976226,-9.450595,-8.992294,-9.158908,-5.869458,1.433221,-4.708271,-5.519763,5.845366,3.619357,4.522098,9.983016,1.969434,9.129689,6.294841,6.918040,7.904921,-2.636917,0.560525,-2.079839,5.819608,1.409046,-6.396997,2.941324,-7.444468,1.286844,-2.241760,-1.531616,-3.570241,-6.012930,-5.480874,5.686104,-6.070422,4.783774,-9.772501,9.976889,7.327312,2.388534,-2.101499,4.714622,5.116085,-7.764370,-7.312846,5.372645,1.848370,-6.612261,-8.862668,3.514184,0.808609,-9.335788,-0.437877,-7.263508,-1.730250,-5.219539,-7.954942,9.882258,-6.402126,8.281697,0.962330,7.843168,3.661376,-1.538953,9.354786,-3.353156,-7.177901,-2.251507,-0.477138,-8.624752,-7.933561,3.552743,-7.314890,-9.222193,-4.538629,7.139042,1.680550,-2.885416,-9.785708,-5.746255,-2.416735,5.961588,6.105308,-5.331043,-3.913650,-4.231526,1.333996,5.020335,-0.258879,-7.104316,-3.636136,-4.785605,-9.409019,-3.375328,5.533797,5.669714,6.540493,-2.297374,-0.152327,-1.265834,0.117474,-8.081490,-4.695892,2.609684,2.383673,5.283997,9.575577,8.420551,1.952045,9.750165,-9.037615,-1.235961,9.069843,-5.122594,8.050278,-4.202763,5.348867,7.454578,-1.242199,6.857249,-6.665002,3.885458,-9.317820,-3.422999,-1.999830,0.469832,-7.239513,-7.090127,-0.743611,8.406618,1.175650,2.362275,-0.484665,-4.971276,0.174605,6.292911,9.639425,4.221619,8.124658,6.655763,3.481994,9.878640,-0.750880,5.797099,-0.647717,5.263713,-0.163782,1.459005,2.613854,-1.257641,8.772808,6.216904,-2.357060,-1.940345,-7.391175,-5.336474,-2.946316,9.004888,7.950462,-7.158562,6.234019,-7.225317,-2.865897,7.693836,2.550084,-6.775980,1.033027,9.813583,-5.357671,4.334746,2.365257,7.036886,3.438203,7.545176,0.789588,0.394136,1.550120,6.089309,1.845515,5.005882,-6.508996,7.179852,3.621875,4.677809,-9.675627,-0.881635,-0.831993,-4.755340,-0.593181,6.006019,7.764325,7.711159,-5.164672,-4.303400,9.538933,-2.697332,1.015257,4.938349,7.924026,-4.299151,7.016717,6.950145,-4.858022,-5.253941,4.523009,7.911222,-5.914891,8.302886,6.458734,-2.440858,-8.663628,-6.059709,-6.907744,-3.687772,-3.409929,5.581006,-9.915812,-5.733216,-2.520673,0.797460,-5.786014,-0.872377,5.683304,9.344769,1.563789,2.291114,-2.334178,1.010917,9.992876,-5.979195,0.299332,-9.588689,4.968579,-1.045252,4.436648,3.468962,-7.728236,-4.499259,-5.364161,-9.747946,5.881684,6.215860,0.583348,-7.159436,-5.813605,4.202256,-4.839621,8.928877,-1.513068,-6.339557,-7.838705,3.455087,3.414965,-4.444823,7.251667,-4.612674,0.913113,-5.382583,-3.699148,9.087012,-9.921738,-2.853519,-0.277157,-5.191816,-6.041154,-6.736903,-8.337609,4.710661,4.489112,1.340597,9.161594,4.185811,6.802939,7.067704,-5.760504,5.946447,6.348189,-7.992032,5.278126,-8.523520,1.544249,-8.758161,-1.565320,7.303515,-2.532194,-2.895749,-8.713582,-6.657048,-3.437169,-0.960311,-0.985425,4.053602,2.005334,-7.774034,-3.345394,-1.329145,6.746811,8.456291,6.235964,-7.533836,-2.151846,3.768965,-7.794639,-6.315019,0.879544,-8.484415,-8.462985,-0.106475,7.127223,2.235150,0.005983,6.959125,-3.084363,3.938154,2.403190,0.044714,-7.144332,0.851278,-8.970035,7.066710,-3.180868,-0.845241,9.296057,-6.677943,7.013700,-2.591116,-1.093657,6.520897,0.269882,-4.698771,-6.620887,-0.588636,-2.496682,-0.062169,5.810330,-5.383586,6.113843,1.032343,2.944141,3.965884,4.598609,-5.564545,7.427418,-0.679036,-7.875437,0.263071,1.120774,8.904275,4.707910,-0.170941,-5.197345,-5.630691,3.191360,-2.924204,-2.640306,4.713399,-5.128455,6.757680,-4.045507,-8.078127,-5.293522,9.313030,0.429274,2.024180,-8.973273,3.364659,-4.882179,-5.897882,5.334097,9.184055,-4.324343,9.202979,-7.639341,-4.101030,9.745547,0.590202,9.963523,4.531663,5.357120,0.603110,-0.517495,-7.464487,0.405956,4.785507,-4.028779,-7.464495,9.297074,4.421003,-2.386963,-4.604366,-7.150327,5.896357,6.968563,-5.054707,6.239670,-7.905352,-2.982520,-0.221269,-1.922941,5.530154,-9.150156,4.650212,3.989314,6.528762,8.750323,1.716668,3.448539,1.607093,5.598969,-0.851082,1.538905,3.982623,0.797349,6.202856,1.512630,-6.780005,-1.708619,1.406746,-9.800712,2.044954,5.895168,2.176731,4.488940,3.780209,-9.848134,9.865707,-6.204229,-3.552970,1.620631,7.876553,-5.656463,-0.864031,-8.456267,-7.809982,2.440099,-2.815868,3.881913,4.215165,-4.052475,0.167099,-2.974161,-8.316553,7.448013,5.749844,7.301615,1.961982,-3.698937,-3.101344,-0.991524,-1.786262,3.820053,-9.600378,-3.851813,9.356297,-8.929519,-4.542545,-9.019657,2.947004,3.486337,-5.170590,-2.224731,-5.353601,0.700295,0.411393,8.543685,2.984399,-0.470585,8.798138,-4.473665,7.849698,-1.491935,1.971534,-0.561076,-6.275287,2.974712,-9.359939,7.787872,1.709573,-8.176708,-1.694567,-8.679110,-2.219514,8.328323,5.119380,-7.547190,-7.550838,-4.603377,4.244938,-2.230543,-0.012744,-1.516541,9.884987,8.507671,5.020900,3.082183,-9.946295,6.975381,-2.971935,-2.450507,-4.824540,-7.817379,9.949345,7.980911,-1.950085,9.102026,6.780264,0.287948,7.295280,4.820937,-9.187810,-5.188889,-6.219290,1.052999,-0.237931,0.101193,5.905363,3.026553,-0.475593,4.613390,-0.082339,-6.344337,0.164625,7.786796,-0.162101,9.339839,0.925868,2.900600,7.074592,6.931058,5.128335,4.572718,-7.918453,8.936286,8.776975,5.108991,0.375983,4.801479,-7.695235,8.348563,-9.465701,8.923281,-1.669916,2.563475,-9.486679,4.872590,6.826840,-3.131469,4.197812,9.959925,-8.242832,6.914340,-7.557583,-1.161140,8.624449,4.155195,-8.277336,3.446782,-4.517529,5.985587,9.049124,-2.107719,5.650930,2.273637,-4.662461,7.107989,9.405693,1.063096,5.384130,-3.371186,7.478617,-4.455029,4.889503,7.589364,0.389722,-1.484359,4.399261,2.595139,0.380256,-2.912660,5.459696,-3.115764,-8.190751,-8.164059,-1.179754,-7.343605,2.637575,2.855087,-8.028939,-7.480346,0.276094,6.207332,2.726091,9.817743,1.854410,-2.865710,0.087737,8.932836,-3.200015,-0.052433,4.630677,1.487276,5.842984,1.210789,1.788299,7.873301,-8.904654,5.715111,-7.209387,-2.468502,-5.997766,-6.071360,6.067812,8.584320,-3.013868,-7.359833,-2.949120,-2.248347,9.166781,-9.674696,1.460407,9.123590,-8.637644,9.072224,-3.011653,-5.448002,-8.275245,-6.794498,-2.359906,-8.191124,4.635976,-1.040732,-5.998103,-4.480292,-7.407901,-2.968934,-8.700237,4.053186,-4.925876,2.928932,-7.726823,-9.723493,6.760992,3.544250,-3.328704,-6.368528,-5.823093,-7.095768,4.606047,-4.109215,3.449503,5.186642,6.788866,-4.206126,9.416872,-0.586223,3.781531,-7.857116,6.324741,-7.947264,9.400610,-9.015955,-4.770854,-7.786049,4.978471,9.990304,3.985983,-0.359681,-7.971087,0.971332,3.566923,4.226119,-1.738761,8.282938,9.084603,6.082219,-3.417355,1.190068,-8.935823,-0.066646,-5.606243,-5.749204,-4.757380,-6.309929,9.891394,-9.122997,3.510566,2.292087,8.304717,-3.188125,2.522297,-2.932875,3.537919,-8.315790,7.526325,4.945391,-8.025268,-4.209288,-4.008527,1.789206,-8.093338,-4.162391,-2.258336,4.169875,-7.742674,-5.174450,7.764397,1.692724,-0.306441,0.695446,-9.071959,-7.067843,-8.854671,6.061298,9.644218,6.415994,-8.295069,-3.825560,5.946096,6.517471,0.098288,8.837354,-1.330327,9.033131,-4.348107,-9.521475,3.312740,-1.398832,1.717660,-8.414798,-3.939121,-7.507709,-5.604083,5.543974,-3.865883,7.673938,2.590918,4.328477], dtype = "float32")#candidate|6261|(1134,)|const|float32
call_6260 = relay.TupleGetItem(func_2442_call(relay.reshape(const_6261.astype('float32'), [1134,])), 1)
call_6262 = relay.TupleGetItem(func_2445_call(relay.reshape(const_6261.astype('float32'), [1134,])), 1)
func_2964_call = mod.get_global_var('func_2964')
func_2965_call = mutated_mod.get_global_var('func_2965')
call_6274 = func_2964_call()
call_6275 = func_2964_call()
bop_6291 = relay.bitwise_and(const_6261.astype('int16'), relay.reshape(call_6260.astype('int16'), relay.shape_of(const_6261))) # shape=(1134,)
bop_6294 = relay.bitwise_and(const_6261.astype('int16'), relay.reshape(call_6262.astype('int16'), relay.shape_of(const_6261))) # shape=(1134,)
output = relay.Tuple([call_6257,call_6274,bop_6291,])
output2 = relay.Tuple([call_6258,call_6275,bop_6294,])
func_6304 = relay.Function([], output)
mod['func_6304'] = func_6304
mod = relay.transform.InferType()(mod)
output = func_6304()
func_6305 = relay.Function([], output)
mutated_mod['func_6305'] = func_6305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3726_call = mod.get_global_var('func_3726')
func_3727_call = mutated_mod.get_global_var('func_3727')
call_6336 = relay.TupleGetItem(func_3726_call(), 1)
call_6337 = relay.TupleGetItem(func_3727_call(), 1)
func_4941_call = mod.get_global_var('func_4941')
func_4943_call = mutated_mod.get_global_var('func_4943')
var_6349 = relay.var("var_6349", dtype = "float32", shape = (700, 2))#candidate|6349|(700, 2)|var|float32
call_6348 = relay.TupleGetItem(func_4941_call(relay.reshape(var_6349.astype('float32'), [1400,])), 1)
call_6350 = relay.TupleGetItem(func_4943_call(relay.reshape(var_6349.astype('float32'), [1400,])), 1)
var_6351 = relay.var("var_6351", dtype = "float32", shape = (8, 3, 5))#candidate|6351|(8, 3, 5)|var|float32
bop_6352 = relay.greater(call_6336.astype('bool'), var_6351.astype('bool')) # shape=(8, 3, 5)
bop_6355 = relay.greater(call_6337.astype('bool'), var_6351.astype('bool')) # shape=(8, 3, 5)
uop_6360 = relay.sinh(var_6351.astype('float32')) # shape=(8, 3, 5)
output = relay.Tuple([call_6348,var_6349,bop_6352,uop_6360,])
output2 = relay.Tuple([call_6350,var_6349,bop_6355,uop_6360,])
func_6362 = relay.Function([var_6349,var_6351,], output)
mod['func_6362'] = func_6362
mod = relay.transform.InferType()(mod)
mutated_mod['func_6362'] = func_6362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6362_call = mutated_mod.get_global_var('func_6362')
var_6364 = relay.var("var_6364", dtype = "float32", shape = (700, 2))#candidate|6364|(700, 2)|var|float32
var_6365 = relay.var("var_6365", dtype = "float32", shape = (8, 3, 5))#candidate|6365|(8, 3, 5)|var|float32
call_6363 = func_6362_call(var_6364,var_6365,)
output = call_6363
func_6366 = relay.Function([var_6364,var_6365,], output)
mutated_mod['func_6366'] = func_6366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4459_call = mod.get_global_var('func_4459')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_6382 = relay.TupleGetItem(func_4459_call(), 4)
call_6383 = relay.TupleGetItem(func_4461_call(), 4)
uop_6385 = relay.acos(call_6382.astype('float32')) # shape=(10, 10, 14)
uop_6387 = relay.acos(call_6383.astype('float32')) # shape=(10, 10, 14)
output = relay.Tuple([uop_6385,])
output2 = relay.Tuple([uop_6387,])
func_6393 = relay.Function([], output)
mod['func_6393'] = func_6393
mod = relay.transform.InferType()(mod)
mutated_mod['func_6393'] = func_6393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6393_call = mutated_mod.get_global_var('func_6393')
call_6394 = func_6393_call()
output = call_6394
func_6395 = relay.Function([], output)
mutated_mod['func_6395'] = func_6395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5529_call = mod.get_global_var('func_5529')
func_5531_call = mutated_mod.get_global_var('func_5531')
call_6408 = func_5529_call()
call_6409 = func_5529_call()
func_4501_call = mod.get_global_var('func_4501')
func_4502_call = mutated_mod.get_global_var('func_4502')
call_6419 = func_4501_call()
call_6420 = func_4501_call()
var_6425 = relay.var("var_6425", dtype = "float32", shape = (8, 14, 5))#candidate|6425|(8, 14, 5)|var|float32
bop_6426 = relay.add(call_6419.astype('int8'), var_6425.astype('int8')) # shape=(8, 14, 5)
bop_6429 = relay.add(call_6420.astype('int8'), var_6425.astype('int8')) # shape=(8, 14, 5)
output = relay.Tuple([call_6408,bop_6426,])
output2 = relay.Tuple([call_6409,bop_6429,])
func_6435 = relay.Function([var_6425,], output)
mod['func_6435'] = func_6435
mod = relay.transform.InferType()(mod)
mutated_mod['func_6435'] = func_6435
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6436 = relay.var("var_6436", dtype = "float32", shape = (8, 14, 5))#candidate|6436|(8, 14, 5)|var|float32
func_6435_call = mutated_mod.get_global_var('func_6435')
call_6437 = func_6435_call(var_6436)
output = call_6437
func_6438 = relay.Function([var_6436], output)
mutated_mod['func_6438'] = func_6438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4459_call = mod.get_global_var('func_4459')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_6518 = relay.TupleGetItem(func_4459_call(), 3)
call_6519 = relay.TupleGetItem(func_4461_call(), 3)
output = call_6518
output2 = call_6519
func_6526 = relay.Function([], output)
mod['func_6526'] = func_6526
mod = relay.transform.InferType()(mod)
output = func_6526()
func_6527 = relay.Function([], output)
mutated_mod['func_6527'] = func_6527
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6557 = relay.var("var_6557", dtype = "int16", shape = (9, 11, 15))#candidate|6557|(9, 11, 15)|var|int16
const_6558 = relay.const([[[-9,3,-3,-2,-3,-8,-8,-1,-10,-3,-4,-8,4,6,-5],[5,5,3,-2,-4,3,5,-10,4,-5,1,-3,10,10,-5],[8,-1,8,10,1,5,8,5,-6,8,-5,-1,-9,-10,-6],[-3,6,7,8,-6,-3,-2,10,-1,-10,10,-9,6,3,-6],[-2,3,-3,-2,10,-9,-8,6,-2,-6,9,10,8,-5,-3],[-10,-9,10,5,-2,-9,-8,4,7,-2,-10,1,-6,-7,10],[3,4,-4,2,8,2,5,-4,-5,-8,-4,-5,-10,3,-5],[9,2,-8,10,6,3,7,10,-10,-2,2,-1,-2,10,-10],[8,-3,-3,-9,-10,-10,4,5,-9,-1,-5,9,-1,-7,-6],[-6,-6,-5,9,-1,10,3,1,2,-5,2,-5,6,-2,7],[-1,2,-3,6,2,2,-3,10,5,5,-4,-9,-8,6,-1]],[[-9,7,10,10,-5,-5,6,4,-1,9,-8,-3,-3,4,-2],[-2,7,-4,-1,-5,7,-3,-10,-1,3,-9,3,10,4,3],[8,8,-5,4,-5,4,3,-6,-4,5,7,10,5,-5,-3],[4,-4,-9,-5,8,-6,-3,-10,3,6,-1,2,-2,-9,-8],[5,-6,-6,-1,9,-2,-10,3,4,3,-4,2,4,-4,2],[5,-6,8,5,-3,-7,-1,-2,8,-2,5,-5,-3,4,2],[-1,-3,10,-7,1,1,-6,8,9,-3,6,7,8,10,7],[-8,-3,-5,4,-9,-3,6,5,9,-9,2,-2,-9,-9,2],[5,6,5,-2,-3,-6,3,8,-6,-9,1,4,-2,-6,6],[-1,-10,-10,8,3,-4,10,3,-5,-6,7,8,1,-6,5],[6,2,2,-2,3,4,8,-5,1,-1,-4,4,-2,6,-1]],[[8,6,5,4,-10,5,-4,-9,4,-1,-7,-5,-9,-6,-5],[-7,-8,4,2,-1,5,-8,10,10,-7,1,5,7,-3,10],[-3,10,9,5,2,-6,3,-3,-1,-7,3,-4,-5,4,-5],[-5,-3,-8,-1,-6,8,-7,5,-5,5,5,-1,-6,-10,-2],[7,5,-4,-2,7,-5,7,-7,-4,-9,4,6,-2,2,5],[9,3,9,9,2,9,-9,1,-9,10,-3,9,-10,4,-5],[5,-10,-9,6,2,2,-9,-8,-8,-5,-4,-3,-2,5,4],[-4,5,-9,-4,-2,5,8,6,-4,2,3,10,8,-10,7],[-3,4,8,2,-8,-8,8,-7,-1,-7,10,8,7,-3,9],[10,2,9,7,2,4,8,-8,-6,-4,2,4,-6,-6,-9],[-1,-6,-5,5,-6,7,8,4,8,5,-3,-8,8,10,-4]],[[-8,8,-10,-9,-4,1,-7,-7,-3,8,-7,-6,8,2,8],[6,3,-2,-8,-5,7,6,-2,-4,-7,4,5,-10,4,10],[-8,-1,-2,-3,7,-3,-3,-10,-1,2,7,2,6,5,-4],[5,3,2,-9,4,-2,-10,-7,1,-5,5,-9,-3,9,-8],[-5,4,6,-3,-2,1,-5,10,-3,9,-4,-9,-9,9,-4],[-10,9,-9,1,-4,-7,8,7,-4,-9,-8,5,-5,4,2],[-2,-7,6,7,-7,2,-7,-6,10,-5,-2,1,2,2,1],[-4,-6,-5,-10,-4,5,-1,-8,-7,8,7,-6,-7,-6,4],[3,-2,2,5,-2,-9,7,-9,6,3,-7,1,-3,-2,7],[8,-8,1,8,4,-7,8,10,8,3,-9,6,-4,10,7],[3,-7,6,3,-6,-5,-9,-6,10,4,-5,-6,4,-9,-7]],[[2,-2,5,9,-3,4,-9,-10,-1,-8,4,9,-6,3,9],[-2,1,2,-1,3,-7,1,-9,10,1,-6,-3,6,-10,-3],[-8,2,8,-7,-4,-2,-7,-6,3,-8,-3,-1,9,-6,-6],[-10,3,-8,-5,-9,-5,-7,-3,1,-8,-2,3,-9,-1,-5],[-1,3,-8,-4,-6,-9,3,3,8,6,5,7,1,4,1],[9,4,-8,3,-5,-5,9,-10,-8,8,-4,-9,-3,-9,2],[-6,-1,-5,5,1,8,-2,-5,-1,1,-4,6,-8,-6,8],[8,-1,6,-8,-5,-1,-6,-1,-7,4,6,5,-3,-1,-1],[-9,2,-7,-5,9,5,-4,-5,2,9,-2,-5,-7,1,9],[6,2,-5,6,6,-1,-7,2,10,-6,9,6,-6,-2,2],[2,7,-5,4,4,5,1,-10,6,6,-1,-9,-10,-1,-5]],[[-6,-10,-2,7,4,-6,-9,-3,-1,-9,10,-3,-10,-5,7],[-5,-6,6,-9,3,-6,-6,-7,4,-9,-4,-6,7,2,-8],[-3,-4,7,6,4,-1,6,7,-8,1,7,-6,4,8,7],[-9,-8,-9,2,1,5,-6,9,4,6,5,-3,-6,-6,7],[2,-6,-6,3,2,-3,6,-8,5,-4,-9,4,-2,1,7],[-3,-3,-7,-4,8,-6,3,-2,-1,-2,10,4,3,6,-3],[-1,2,-3,-2,3,5,1,-3,8,4,9,-9,-9,8,-6],[8,7,-1,1,1,3,3,-5,-9,-2,-1,6,-5,-4,-10],[-6,-10,-10,-5,-2,7,2,9,8,-10,-2,3,-3,-3,-1],[-9,-3,2,-8,6,-1,7,-3,-3,-6,-1,-4,-6,-3,5],[-4,-3,-3,-2,-9,-3,3,8,-10,-7,3,-5,-4,-5,-2]],[[3,5,4,-10,-1,7,1,-5,6,-9,-2,-4,-9,-1,-7],[5,10,-7,-7,3,6,-1,-1,-8,-4,3,9,-4,-10,-3],[10,9,7,8,-3,-2,-2,7,-1,-4,4,-10,7,-1,1],[-3,3,2,-8,-4,1,1,8,9,-5,-4,-10,-9,-10,-3],[-8,5,8,1,-8,-10,-10,-4,-9,10,8,10,-10,-5,3],[5,-6,-3,8,2,-1,-6,-3,3,-5,-5,-9,-1,4,-1],[-5,8,-7,-8,9,10,2,4,8,9,-10,-6,-7,-10,-6],[10,9,5,-1,10,2,-1,-6,2,-2,-7,3,-3,-2,-5],[-6,-10,-5,9,-5,-7,9,-3,-2,-8,6,-7,9,-3,-5],[-7,-3,3,1,5,3,5,9,8,3,-6,-1,1,-4,-9],[5,9,-3,8,-8,-10,-5,4,2,-7,-8,-7,-5,7,3]],[[8,1,7,-2,10,8,-1,-6,10,7,-5,10,3,10,-7],[-7,-2,4,4,4,4,-5,-6,-9,9,4,10,5,1,3],[-10,-5,-9,-2,5,-9,10,5,5,4,10,9,4,-3,-1],[5,7,4,10,-10,-3,-5,3,9,-4,3,3,-3,-5,-1],[3,8,7,7,-9,10,8,-3,5,-10,-6,-10,4,-5,-10],[-7,-4,2,-6,-9,-7,-7,6,7,-1,-8,-1,-6,-4,4],[-7,4,6,3,4,-9,2,-8,-5,8,2,-4,6,8,1],[1,-2,1,2,2,-7,1,-8,-6,1,-2,1,8,8,-7],[-7,-8,7,9,-7,-7,3,-4,4,3,-5,2,10,5,-5],[6,-1,3,8,-7,-2,-9,-2,-5,4,-6,2,7,8,-10],[4,-5,2,5,9,-5,8,-5,9,-1,-7,-6,-2,8,4]],[[-3,6,5,7,10,-2,8,-10,-2,-2,-4,9,7,-2,3],[5,-6,5,10,3,-9,-6,-7,-9,-5,-4,-1,10,6,7],[10,5,-4,1,-4,4,1,8,4,9,-10,2,-7,1,6],[3,1,-6,-2,-7,-1,-10,8,-10,-5,6,3,-9,10,-6],[-8,-4,8,-4,-7,7,-1,-10,-4,5,-1,-7,9,-9,-5],[-7,3,-4,1,3,8,-6,8,-9,-6,2,-3,4,-6,-3],[7,6,3,-2,5,-2,7,1,4,8,4,9,-10,1,5],[6,8,-3,1,5,3,8,-5,-7,-1,-9,6,2,9,3],[1,-8,-1,-10,-6,-8,-10,1,7,4,-3,-3,-9,5,2],[3,-9,-2,4,1,-7,-9,7,-4,-5,2,-9,7,4,5],[-3,-9,3,-1,5,7,2,1,-5,4,3,-10,-5,-10,10]]], dtype = "int16")#candidate|6558|(9, 11, 15)|const|int16
bop_6559 = relay.left_shift(var_6557.astype('int16'), relay.reshape(const_6558.astype('int16'), relay.shape_of(var_6557))) # shape=(9, 11, 15)
func_5506_call = mod.get_global_var('func_5506')
func_5508_call = mutated_mod.get_global_var('func_5508')
call_6564 = relay.TupleGetItem(func_5506_call(), 1)
call_6565 = relay.TupleGetItem(func_5508_call(), 1)
uop_6568 = relay.erf(var_6557.astype('float32')) # shape=(9, 11, 15)
output = relay.Tuple([bop_6559,call_6564,uop_6568,])
output2 = relay.Tuple([bop_6559,call_6565,uop_6568,])
func_6570 = relay.Function([var_6557,], output)
mod['func_6570'] = func_6570
mod = relay.transform.InferType()(mod)
mutated_mod['func_6570'] = func_6570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6571 = relay.var("var_6571", dtype = "int16", shape = (9, 11, 15))#candidate|6571|(9, 11, 15)|var|int16
func_6570_call = mutated_mod.get_global_var('func_6570')
call_6572 = func_6570_call(var_6571)
output = call_6572
func_6573 = relay.Function([var_6571], output)
mutated_mod['func_6573'] = func_6573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_6590 = relay.TupleGetItem(func_4065_call(), 0)
call_6591 = relay.TupleGetItem(func_4066_call(), 0)
output = relay.Tuple([call_6590,])
output2 = relay.Tuple([call_6591,])
func_6661 = relay.Function([], output)
mod['func_6661'] = func_6661
mod = relay.transform.InferType()(mod)
mutated_mod['func_6661'] = func_6661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6661_call = mutated_mod.get_global_var('func_6661')
call_6662 = func_6661_call()
output = call_6662
func_6663 = relay.Function([], output)
mutated_mod['func_6663'] = func_6663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3229_call = mod.get_global_var('func_3229')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_6768 = relay.TupleGetItem(func_3229_call(), 0)
call_6769 = relay.TupleGetItem(func_3231_call(), 0)
var_6786 = relay.var("var_6786", dtype = "uint16", shape = (6, 16, 12))#candidate|6786|(6, 16, 12)|var|uint16
bop_6787 = relay.logical_xor(call_6768.astype('uint8'), relay.reshape(var_6786.astype('uint8'), relay.shape_of(call_6768))) # shape=(6, 16, 12)
bop_6790 = relay.logical_xor(call_6769.astype('uint8'), relay.reshape(var_6786.astype('uint8'), relay.shape_of(call_6769))) # shape=(6, 16, 12)
output = bop_6787
output2 = bop_6790
func_6794 = relay.Function([var_6786,], output)
mod['func_6794'] = func_6794
mod = relay.transform.InferType()(mod)
var_6795 = relay.var("var_6795", dtype = "uint16", shape = (6, 16, 12))#candidate|6795|(6, 16, 12)|var|uint16
output = func_6794(var_6795)
func_6796 = relay.Function([var_6795], output)
mutated_mod['func_6796'] = func_6796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6096_call = mod.get_global_var('func_6096')
func_6098_call = mutated_mod.get_global_var('func_6098')
call_6805 = relay.TupleGetItem(func_6096_call(), 0)
call_6806 = relay.TupleGetItem(func_6098_call(), 0)
output = call_6805
output2 = call_6806
func_6809 = relay.Function([], output)
mod['func_6809'] = func_6809
mod = relay.transform.InferType()(mod)
output = func_6809()
func_6810 = relay.Function([], output)
mutated_mod['func_6810'] = func_6810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5710_call = mod.get_global_var('func_5710')
func_5711_call = mutated_mod.get_global_var('func_5711')
call_6825 = func_5710_call()
call_6826 = func_5710_call()
func_1716_call = mod.get_global_var('func_1716')
func_1718_call = mutated_mod.get_global_var('func_1718')
var_6869 = relay.var("var_6869", dtype = "float32", shape = (1134,))#candidate|6869|(1134,)|var|float32
call_6868 = relay.TupleGetItem(func_1716_call(relay.reshape(var_6869.astype('float32'), [9, 14, 9])), 0)
call_6870 = relay.TupleGetItem(func_1718_call(relay.reshape(var_6869.astype('float32'), [9, 14, 9])), 0)
func_3298_call = mod.get_global_var('func_3298')
func_3299_call = mutated_mod.get_global_var('func_3299')
call_6872 = relay.TupleGetItem(func_3298_call(), 1)
call_6873 = relay.TupleGetItem(func_3299_call(), 1)
output = relay.Tuple([call_6825,call_6868,var_6869,call_6872,])
output2 = relay.Tuple([call_6826,call_6870,var_6869,call_6873,])
func_6876 = relay.Function([var_6869,], output)
mod['func_6876'] = func_6876
mod = relay.transform.InferType()(mod)
var_6877 = relay.var("var_6877", dtype = "float32", shape = (1134,))#candidate|6877|(1134,)|var|float32
output = func_6876(var_6877)
func_6878 = relay.Function([var_6877], output)
mutated_mod['func_6878'] = func_6878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3475_call = mod.get_global_var('func_3475')
func_3476_call = mutated_mod.get_global_var('func_3476')
call_6914 = func_3475_call()
call_6915 = func_3475_call()
uop_6930 = relay.tan(call_6914.astype('float64')) # shape=(8, 1, 5)
uop_6932 = relay.tan(call_6915.astype('float64')) # shape=(8, 1, 5)
output = uop_6930
output2 = uop_6932
func_6939 = relay.Function([], output)
mod['func_6939'] = func_6939
mod = relay.transform.InferType()(mod)
mutated_mod['func_6939'] = func_6939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6939_call = mutated_mod.get_global_var('func_6939')
call_6940 = func_6939_call()
output = call_6940
func_6941 = relay.Function([], output)
mutated_mod['func_6941'] = func_6941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5342_call = mod.get_global_var('func_5342')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_6966 = func_5342_call()
call_6967 = func_5342_call()
output = call_6966
output2 = call_6967
func_6990 = relay.Function([], output)
mod['func_6990'] = func_6990
mod = relay.transform.InferType()(mod)
mutated_mod['func_6990'] = func_6990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6990_call = mutated_mod.get_global_var('func_6990')
call_6991 = func_6990_call()
output = call_6991
func_6992 = relay.Function([], output)
mutated_mod['func_6992'] = func_6992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3298_call = mod.get_global_var('func_3298')
func_3299_call = mutated_mod.get_global_var('func_3299')
call_7038 = relay.TupleGetItem(func_3298_call(), 0)
call_7039 = relay.TupleGetItem(func_3299_call(), 0)
output = relay.Tuple([call_7038,])
output2 = relay.Tuple([call_7039,])
func_7065 = relay.Function([], output)
mod['func_7065'] = func_7065
mod = relay.transform.InferType()(mod)
mutated_mod['func_7065'] = func_7065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7065_call = mutated_mod.get_global_var('func_7065')
call_7066 = func_7065_call()
output = call_7066
func_7067 = relay.Function([], output)
mutated_mod['func_7067'] = func_7067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5949_call = mod.get_global_var('func_5949')
func_5951_call = mutated_mod.get_global_var('func_5951')
call_7098 = relay.TupleGetItem(func_5949_call(), 0)
call_7099 = relay.TupleGetItem(func_5951_call(), 0)
output = relay.Tuple([call_7098,])
output2 = relay.Tuple([call_7099,])
func_7100 = relay.Function([], output)
mod['func_7100'] = func_7100
mod = relay.transform.InferType()(mod)
mutated_mod['func_7100'] = func_7100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7100_call = mutated_mod.get_global_var('func_7100')
call_7101 = func_7100_call()
output = call_7101
func_7102 = relay.Function([], output)
mutated_mod['func_7102'] = func_7102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6059_call = mod.get_global_var('func_6059')
func_6060_call = mutated_mod.get_global_var('func_6060')
call_7165 = relay.TupleGetItem(func_6059_call(), 1)
call_7166 = relay.TupleGetItem(func_6060_call(), 1)
func_2964_call = mod.get_global_var('func_2964')
func_2965_call = mutated_mod.get_global_var('func_2965')
call_7182 = func_2964_call()
call_7183 = func_2964_call()
output = relay.Tuple([call_7165,call_7182,])
output2 = relay.Tuple([call_7166,call_7183,])
func_7216 = relay.Function([], output)
mod['func_7216'] = func_7216
mod = relay.transform.InferType()(mod)
mutated_mod['func_7216'] = func_7216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7216_call = mutated_mod.get_global_var('func_7216')
call_7217 = func_7216_call()
output = call_7217
func_7218 = relay.Function([], output)
mutated_mod['func_7218'] = func_7218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6120_call = mod.get_global_var('func_6120')
func_6122_call = mutated_mod.get_global_var('func_6122')
call_7239 = relay.TupleGetItem(func_6120_call(), 0)
call_7240 = relay.TupleGetItem(func_6122_call(), 0)
func_4751_call = mod.get_global_var('func_4751')
func_4752_call = mutated_mod.get_global_var('func_4752')
call_7243 = func_4751_call()
call_7244 = func_4751_call()
output = relay.Tuple([call_7239,call_7243,])
output2 = relay.Tuple([call_7240,call_7244,])
func_7254 = relay.Function([], output)
mod['func_7254'] = func_7254
mod = relay.transform.InferType()(mod)
mutated_mod['func_7254'] = func_7254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7254_call = mutated_mod.get_global_var('func_7254')
call_7255 = func_7254_call()
output = call_7255
func_7256 = relay.Function([], output)
mutated_mod['func_7256'] = func_7256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4271_call = mod.get_global_var('func_4271')
func_4272_call = mutated_mod.get_global_var('func_4272')
call_7257 = relay.TupleGetItem(func_4271_call(), 2)
call_7258 = relay.TupleGetItem(func_4272_call(), 2)
output = relay.Tuple([call_7257,])
output2 = relay.Tuple([call_7258,])
func_7260 = relay.Function([], output)
mod['func_7260'] = func_7260
mod = relay.transform.InferType()(mod)
output = func_7260()
func_7261 = relay.Function([], output)
mutated_mod['func_7261'] = func_7261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6120_call = mod.get_global_var('func_6120')
func_6122_call = mutated_mod.get_global_var('func_6122')
call_7290 = relay.TupleGetItem(func_6120_call(), 1)
call_7291 = relay.TupleGetItem(func_6122_call(), 1)
func_6570_call = mod.get_global_var('func_6570')
func_6573_call = mutated_mod.get_global_var('func_6573')
const_7328 = relay.const([7,-7,-1,3,1,-9,-4,4,8,-3,7,7,-4,10,3,10,-7,-8,-1,10,-8,9,-2,1,2,-4,-4,8,6,-1,-9,-8,2,-7,-10,-5,8,10,8,9,-3,-10,3,-5,9,-9,-1,-7,4,-5,2,1,-3,-9,10,4,2,2,-3,-6,7,3,4,-10,-5,-3,3,9,4,-9,-8,2,9,5,3,4,-9,-5,-6,-1,9,2,-7,10,-8,10,3,6,-5,4,6,-7,5,-10,-8,6,7,9,-8,7,-1,-2,8,6,10,-1,-10,-3,-2,-9,-4,-6,-2,4,8,-6,10,-3,5,-2,-1,-1,-3,5,-7,-6,9,1,8,1,-1,-5,4,-9,-7,-4,-6,-9,-1,-6,1,9,-3,3,-8,-7,1,9,-8,-4,9,-5,-3,8,3,2,6,-7,-4,10,5,2,-9,-1,9,-4,-3,3,-7,2,5,-5,-5,-1,1,2,1,3,-5,9,-2,-2,3,-3,-6,-8,8,3,-4,-4,-8,-2,-2,-8,-1,-1,-9,-10,-8,-1,-7,-7,-4,10,-7,-4,3,-3,-3,2,-8,-1,-5,7,1,10,-9,-4,-9,1,-9,8,-3,6,2,1,10,4,2,-1,-1,2,-7,-3,1,2,-8,-3,-1,-6,7,-2,-1,4,-8,-6,-3,-9,5,7,-5,-5,9,-4,4,-5,9,-10,4,2,9,10,-6,-2,-2,-6,-10,-10,6,-3,-3,-5,-4,1,-9,9,-2,-9,2,9,4,1,-6,-5,4,-7,6,7,7,7,2,-5,9,-3,7,6,-7,7,7,-8,-10,8,-6,-6,-5,-10,-3,9,9,4,4,-9,-5,6,8,5,-8,-6,7,9,8,-7,4,-2,10,3,6,-4,-8,-4,-6,-8,1,-1,7,10,-9,6,-5,-10,-6,10,5,-4,-6,-3,7,-7,5,-7,-7,-8,6,-2,4,-7,-5,4,-10,-4,7,9,9,2,-3,6,10,10,10,8,-6,-6,-3,-2,9,9,3,9,5,6,4,2,8,7,-4,3,1,10,10,-7,7,-6,-6,-4,6,-1,-4,2,2,9,6,5,-1,-9,6,1,-2,8,2,8,-4,8,-1,9,4,7,-1,-7,-7,5,-2,1,-5,-3,10,7,-2,1,7,-5,9,-1,6,5,4,-1,8,2,8,2,-1,-2,-4,-6,-5,2,-5,-6,-10,-8,-1,-3,-10,4,-2,-6,5,-6,10,-2,5,9,-6,2,-6,-10,-1,5,10,9,-6,-7,-4,-10,6,-1,5,-10,-7,-6,-5,7,1,-7,-1,-3,3,8,4,4,-9,9,-7,6,3,4,-10,4,-4,4,-9,-2,8,2,9,10,-10,-3,-7,-10,1,-8,6,-4,-5,6,7,8,10,-7,-3,9,5,-2,-1,5,-6,-4,-7,1,-9,5,6,1,-1,-7,5,-10,1,5,4,-5,2,-1,10,-10,10,4,1,4,-2,-8,10,-7,2,3,1,6,-7,-2,-10,3,10,-8,3,-4,-2,3,-2,10,-4,10,3,9,-5,-7,5,-5,-9,7,4,6,4,9,-2,2,4,-1,7,6,-1,7,3,3,6,4,1,-7,1,-1,-6,1,4,-6,-10,-5,5,8,-5,-2,1,2,-7,-7,6,3,2,2,4,10,-10,6,8,-3,-7,5,-10,1,9,-8,-9,-7,-5,-8,-8,-6,5,4,-7,6,4,3,-10,1,-4,4,-10,-6,-1,7,-5,8,4,-1,10,7,1,-10,-6,-2,-10,6,1,-8,-6,-4,5,-1,5,-9,1,1,-6,7,-1,-2,9,-2,2,3,-2,-1,8,-7,-3,-9,2,8,-10,10,6,-4,-4,3,6,-3,4,7,-5,-4,1,-3,-5,1,-8,9,-6,8,9,5,-9,6,-4,5,5,6,-5,9,1,-7,4,2,-1,2,-4,-7,-7,8,6,-9,-5,7,5,1,-7,-5,-8,-10,9,-1,9,10,3,-5,3,9,8,-9,-3,9,3,-10,-2,10,-4,-8,10,-9,8,-1,-10,1,6,3,2,-9,7,-4,2,4,-6,1,10,1,5,-7,10,-5,7,6,-1,4,4,6,-3,-4,-3,-5,4,-9,7,6,-5,6,8,-3,8,-6,5,-2,4,-9,10,8,-1,-5,-6,-6,9,-4,7,-5,-5,9,2,-10,7,3,-3,-1,9,-3,-4,-5,2,-3,7,3,-10,-1,6,-9,1,10,5,10,-7,1,1,-6,7,3,-7,5,-3,-10,-8,-1,4,-4,-1,5,7,-9,3,-5,-7,4,7,3,-8,8,-5,6,10,-8,-6,9,8,4,-5,2,9,8,-7,-5,-6,-10,4,10,-8,5,1,9,-3,-1,-4,-2,10,9,3,-10,-9,-9,6,6,-8,-10,-4,8,-2,8,3,8,-4,-9,-3,7,9,4,7,-9,-1,-6,8,6,5,7,-6,9,4,-8,-9,8,10,3,-1,2,3,-1,-2,-2,-1,-4,6,8,3,8,10,10,-7,5,5,-4,-5,-1,9,3,2,6,3,1,-9,-8,4,-9,10,9,-3,-8,-7,7,-10,-6,8,-2,8,-8,2,-8,-5,7,2,5,-10,-6,-1,3,-1,-6,10,3,3,7,-9,-2,-1,-4,-7,-8,3,2,-5,5,-3,-9,1,1,5,-9,-2,-1,-2,-7,5,5,-9,1,-1,4,-7,7,6,2,-7,-6,-4,3,1,4,-5,-3,6,-10,10,1,8,-7,-7,4,10,2,-6,-9,-4,2,-1,-6,10,-4,-10,10,-4,-2,6,6,5,-9,4,9,-10,-9,-7,8,9,-8,8,8,-2,4,6,3,9,-4,1,-10,6,4,4,-1,-5,-3,6,4,2,6,-7,1,1,8,9,-3,-9,8,-8,-6,7,-5,-3,-1,-8,-2,5,10,9,10,-7,-2,-1,-10,9,-3,7,9,6,4,-8,10,2,-1,-9,8,5,4,10,6,-10,-6,-6,7,-7,-7,-9,-8,8,-3,-2,5,-1,-5,3,-10,2,-9,3,4,9,2,-10,-1,2,5,5,1,-7,10,-10,2,-8,-2,-9,10,-10,5,5,-8,10,-8,3,4,8,9,-4,-1,4,-3,2,10,-6,-3,5,-7,-5,1,-6,10,-6,-1,-4,3,10,10,9,-5,8,-7,9,7,1,-4,2,-9,4,1,6,5,-1,-7,6,-7,-10,-9,-10,-3,-4,-8,-2,9,8,-4,-5,10,6,6,9,-8,2,8,-2,5,-7,-6,-9,-4,4,-1,7,-3,-1,4,-6,9,-10,10,-7,9,7,2,10,-4,4,-3,9,5,-9,-1,3,-1,-6,-4,9,8,3,-1,-8,7,-10,-4,-8,-10,9,-10,-1,3,5,2,-5,9,2,10,4,-1,-8,5,5,-3,-7,5,5,7,7,3,10,9,1,-2,-7,-1,-8,-2,-4,-5,7,10,10,-3,9,-1,7,10,1,3,5,-4,-2,5,-9,-10,-2,2,10,-1,1,-7,-5,-6,-1,4,-7,-8,-3,7,-5,2,-1,-9,8,-1,3,-9,7,5,-8,-5,-9,4,-7,-6,1,-8,-2,3,-9,1,2,-2,-9,8,-6,-2,7,-7,-10,7,-2,-4,-3,4,-1,6,7,4,-5,-5,7,-7,5,1,8,-7,-4,-5,-7,-1,-6,-4,4,-10,2,9,-5,6,-10,-5,4,1,4,4,-6,2,1,6,-3,2,4,-7,-8,8,1,-6,-7,4,4,-3,-3,2,-10,-9,9,-10,-5,-3,-9,10,-4,6,5,1,8,-8,8,6,2,-2,-9,5,7,-4,7,-6,-10,4,-2,5,-10,10,-4,-5,4,-9,-10,-6,10,-3,5,2,4,1,1,-6,8,9,4,10,3,-2,4,8,-9,-5,-4,10,-10,-6,6,10,-1,7,2,5,1,-8,5,-10,-9,-9,-9,3,-9,-10,2,-10,-8,-10,8], dtype = "int16")#candidate|7328|(1485,)|const|int16
call_7327 = relay.TupleGetItem(func_6570_call(relay.reshape(const_7328.astype('int16'), [9, 11, 15])), 0)
call_7329 = relay.TupleGetItem(func_6573_call(relay.reshape(const_7328.astype('int16'), [9, 11, 15])), 0)
func_7254_call = mod.get_global_var('func_7254')
func_7256_call = mutated_mod.get_global_var('func_7256')
call_7353 = relay.TupleGetItem(func_7254_call(), 0)
call_7354 = relay.TupleGetItem(func_7256_call(), 0)
output = relay.Tuple([call_7290,call_7327,const_7328,call_7353,])
output2 = relay.Tuple([call_7291,call_7329,const_7328,call_7354,])
func_7385 = relay.Function([], output)
mod['func_7385'] = func_7385
mod = relay.transform.InferType()(mod)
output = func_7385()
func_7386 = relay.Function([], output)
mutated_mod['func_7386'] = func_7386
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7387 = relay.var("var_7387", dtype = "float32", shape = (7, 1, 2))#candidate|7387|(7, 1, 2)|var|float32
var_7388 = relay.var("var_7388", dtype = "float32", shape = (7, 12, 2))#candidate|7388|(7, 12, 2)|var|float32
bop_7389 = relay.multiply(var_7387.astype('float32'), var_7388.astype('float32')) # shape=(7, 12, 2)
output = relay.Tuple([bop_7389,])
output2 = relay.Tuple([bop_7389,])
func_7420 = relay.Function([var_7387,var_7388,], output)
mod['func_7420'] = func_7420
mod = relay.transform.InferType()(mod)
mutated_mod['func_7420'] = func_7420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7420_call = mutated_mod.get_global_var('func_7420')
var_7422 = relay.var("var_7422", dtype = "float32", shape = (7, 1, 2))#candidate|7422|(7, 1, 2)|var|float32
var_7423 = relay.var("var_7423", dtype = "float32", shape = (7, 12, 2))#candidate|7423|(7, 12, 2)|var|float32
call_7421 = func_7420_call(var_7422,var_7423,)
output = call_7421
func_7424 = relay.Function([var_7422,var_7423,], output)
mutated_mod['func_7424'] = func_7424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6168_call = mod.get_global_var('func_6168')
func_6169_call = mutated_mod.get_global_var('func_6169')
call_7431 = relay.TupleGetItem(func_6168_call(), 0)
call_7432 = relay.TupleGetItem(func_6169_call(), 0)
func_4459_call = mod.get_global_var('func_4459')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_7433 = relay.TupleGetItem(func_4459_call(), 3)
call_7434 = relay.TupleGetItem(func_4461_call(), 3)
func_3990_call = mod.get_global_var('func_3990')
func_3993_call = mutated_mod.get_global_var('func_3993')
const_7436 = relay.const([-6.164409,-9.134594,-0.217696,-5.953090,-2.986687,-4.701772,-7.207616,6.768448,-0.515667,6.911879,-6.762117,-7.985634,-6.976379,-4.230194,6.628270,-8.405990,9.264954,-9.929763,-1.615507,-1.186645,-3.008608,0.329829,-5.528038,0.590066,-1.815430,-1.348802,9.636841,-2.869380,0.965047,7.110837,-0.929420,-6.347123,-3.561029,-3.440770,-4.345383,2.869546,2.438599,4.285508,-7.228531,-5.327928,7.275052,0.694118,2.526722,-7.003141,-4.444166,-3.681947,3.297680,-8.385615,9.746975,5.218162,-9.777628,-9.117787,0.688542,0.780403,-5.633010,-3.044533,-6.409159,-1.644427,8.289243,-0.534671,-4.376425,5.376555,-6.347142,1.696011,-2.687970,6.871698,-6.031052,-3.973379,2.965359,3.241268,-9.778733,4.079873,7.018377,-2.928287,-0.149674,-8.066277,7.450213,-5.339991,3.316680,9.899286,-7.060122,-2.883073,3.089024,-6.322803,5.765708,-8.279134,2.997426,-7.576574,-2.446931,-8.076342,-6.861545,2.583708,-3.835585,3.093859,-3.477644,1.754164,1.589632,4.509850,-7.460479,4.046477,5.808448,5.005289,2.683398,8.126491,4.499689,-1.948175,-1.272658,9.518576,6.881526,-9.375426,-5.703591,6.941151,-1.592167,-7.709068,-4.100845,-1.722115,2.981137,9.839534,3.506311,-2.827500,-0.025880,-1.604550,1.828866,1.240565,-0.959646,-2.956041,2.546536,-0.310962,-4.302104,-2.320029,-5.586337,-9.804737,0.076411,-8.593100,-8.998980,8.809078,4.276765,8.284864,6.097072,-2.724213,-5.553827,-6.314765,-0.456896,0.482896,7.436421,2.684337,-3.558049,-2.381734,2.069651,8.185822,1.590501,-1.705889,-0.916017,4.645865,-3.476935,-3.947724,-7.610804,-4.190357,9.651427,0.861026,-9.892955,3.633000,-7.365622,-8.098692,-7.733841,8.024122,-1.155847,5.277909,3.580213,-8.317488,-1.928854,3.936442,-7.846489,7.745833,6.400405,-1.728669,3.188084,3.460471,8.591827,-9.091900,7.932476,-6.432934,4.235430,-5.057383,-3.327654,8.257322,2.292425,-6.239445,-5.296126,-6.397301,-7.251183,0.778515,-7.982827,-7.259650,-5.648434,2.050508,-5.862037,4.488551,1.151291,6.710081,4.524892,-3.361070,9.055177,-9.781913,-0.297402,8.080944,5.234548,0.453741,3.556318,-3.161201,-6.141430,7.692055,5.322726,-9.046309,0.148694,-1.208988,-8.389705,4.618300,4.807924,-1.083270,-3.314252,9.264926,-2.511625,2.072847,-1.107918,-3.031804,-8.225153,2.202068,-1.757436,-3.111570,9.907258,-2.385344,-2.105158,0.243587,6.960910,0.872844,-0.634370,-5.481321,1.646009,-1.812841,5.831247,-9.813089,2.333376,9.953787,-4.643734,0.309743,-2.794572,0.415801,3.035829,9.395969,-6.633154,8.908926,2.942150,-2.051084,5.974383,-2.192330,3.826367,-8.467231,-8.029463,-1.137409,-7.605080,4.615286,-9.655230,7.028251,9.120976,-8.944314,8.830800,-6.647122,0.346508,-5.361264,-6.817152,1.729562,9.465544,-9.276033,0.981911,-2.856551,-0.246551,1.446434,3.886896,-1.702797,7.059393,-1.563643,-4.240869,1.874876,8.804321,8.363555,-7.894145,4.304419,-9.393614,2.066912,2.224058,0.761749,7.488598,-7.244976,3.645689,-2.272463,2.440123,-9.841254,7.105360,-5.951085,6.509368,-5.045659,-1.457645,4.796311,5.526762,8.843622,3.611855,-4.680758,9.582038,3.567462,-7.799031,9.463342,-8.545917,3.559327,7.652068,9.634394,8.763770,-2.547088,0.966129,7.888146], dtype = "float32")#candidate|7436|(320,)|const|float32
call_7435 = relay.TupleGetItem(func_3990_call(relay.reshape(const_7436.astype('float32'), [8, 8, 5])), 0)
call_7437 = relay.TupleGetItem(func_3993_call(relay.reshape(const_7436.astype('float32'), [8, 8, 5])), 0)
func_3990_call = mod.get_global_var('func_3990')
func_3993_call = mutated_mod.get_global_var('func_3993')
call_7438 = relay.TupleGetItem(func_3990_call(relay.reshape(const_7436.astype('float32'), [8, 8, 5])), 0)
call_7439 = relay.TupleGetItem(func_3993_call(relay.reshape(const_7436.astype('float32'), [8, 8, 5])), 0)
output = relay.Tuple([call_7431,call_7433,call_7435,const_7436,call_7438,])
output2 = relay.Tuple([call_7432,call_7434,call_7437,const_7436,call_7439,])
func_7447 = relay.Function([], output)
mod['func_7447'] = func_7447
mod = relay.transform.InferType()(mod)
mutated_mod['func_7447'] = func_7447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7447_call = mutated_mod.get_global_var('func_7447')
call_7448 = func_7447_call()
output = call_7448
func_7449 = relay.Function([], output)
mutated_mod['func_7449'] = func_7449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6168_call = mod.get_global_var('func_6168')
func_6169_call = mutated_mod.get_global_var('func_6169')
call_7490 = relay.TupleGetItem(func_6168_call(), 0)
call_7491 = relay.TupleGetItem(func_6169_call(), 0)
func_5762_call = mod.get_global_var('func_5762')
func_5765_call = mutated_mod.get_global_var('func_5765')
const_7499 = relay.const([6.365866,5.867773,-5.702544,-6.506786,-4.229242,8.867217,1.994053,-1.669585,7.797974,8.774856,-7.295513,0.769642,-3.245175,-6.186549,5.782213,-2.929547,3.130683,-8.808689,-8.820285,-3.678057,-8.380189,-0.187993,0.263639,4.575600,7.961644,8.584733,-8.514888,7.064188,-8.458810,2.433391,5.463149,-0.109634,1.356555,8.883017,-4.887092,-3.737259,4.109060,-6.241602,-2.541356,-8.715286], dtype = "float32")#candidate|7499|(40,)|const|float32
call_7498 = func_5762_call(relay.reshape(const_7499.astype('float32'), [8, 1, 5]))
call_7500 = func_5762_call(relay.reshape(const_7499.astype('float32'), [8, 1, 5]))
output = relay.Tuple([call_7490,call_7498,const_7499,])
output2 = relay.Tuple([call_7491,call_7500,const_7499,])
func_7501 = relay.Function([], output)
mod['func_7501'] = func_7501
mod = relay.transform.InferType()(mod)
mutated_mod['func_7501'] = func_7501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7501_call = mutated_mod.get_global_var('func_7501')
call_7502 = func_7501_call()
output = call_7502
func_7503 = relay.Function([], output)
mutated_mod['func_7503'] = func_7503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4751_call = mod.get_global_var('func_4751')
func_4752_call = mutated_mod.get_global_var('func_4752')
call_7527 = func_4751_call()
call_7528 = func_4751_call()
output = call_7527
output2 = call_7528
func_7532 = relay.Function([], output)
mod['func_7532'] = func_7532
mod = relay.transform.InferType()(mod)
output = func_7532()
func_7533 = relay.Function([], output)
mutated_mod['func_7533'] = func_7533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6096_call = mod.get_global_var('func_6096')
func_6098_call = mutated_mod.get_global_var('func_6098')
call_7534 = relay.TupleGetItem(func_6096_call(), 0)
call_7535 = relay.TupleGetItem(func_6098_call(), 0)
var_7557 = relay.var("var_7557", dtype = "float32", shape = (8, 14, 5))#candidate|7557|(8, 14, 5)|var|float32
bop_7558 = relay.less(call_7534.astype('bool'), var_7557.astype('bool')) # shape=(8, 14, 5)
bop_7561 = relay.less(call_7535.astype('bool'), var_7557.astype('bool')) # shape=(8, 14, 5)
func_7501_call = mod.get_global_var('func_7501')
func_7503_call = mutated_mod.get_global_var('func_7503')
call_7579 = relay.TupleGetItem(func_7501_call(), 1)
call_7580 = relay.TupleGetItem(func_7503_call(), 1)
func_5199_call = mod.get_global_var('func_5199')
func_5200_call = mutated_mod.get_global_var('func_5200')
call_7595 = func_5199_call()
call_7596 = func_5199_call()
output = relay.Tuple([bop_7558,call_7579,call_7595,])
output2 = relay.Tuple([bop_7561,call_7580,call_7596,])
func_7601 = relay.Function([var_7557,], output)
mod['func_7601'] = func_7601
mod = relay.transform.InferType()(mod)
var_7602 = relay.var("var_7602", dtype = "float32", shape = (8, 14, 5))#candidate|7602|(8, 14, 5)|var|float32
output = func_7601(var_7602)
func_7603 = relay.Function([var_7602], output)
mutated_mod['func_7603'] = func_7603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7216_call = mod.get_global_var('func_7216')
func_7218_call = mutated_mod.get_global_var('func_7218')
call_7617 = relay.TupleGetItem(func_7216_call(), 1)
call_7618 = relay.TupleGetItem(func_7218_call(), 1)
func_4096_call = mod.get_global_var('func_4096')
func_4098_call = mutated_mod.get_global_var('func_4098')
call_7629 = func_4096_call()
call_7630 = func_4096_call()
bop_7634 = relay.floor_mod(call_7617.astype('float64'), call_7629.astype('float64')) # shape=(8, 1, 5)
bop_7637 = relay.floor_mod(call_7618.astype('float64'), call_7630.astype('float64')) # shape=(8, 1, 5)
output = relay.Tuple([bop_7634,])
output2 = relay.Tuple([bop_7637,])
func_7674 = relay.Function([], output)
mod['func_7674'] = func_7674
mod = relay.transform.InferType()(mod)
output = func_7674()
func_7675 = relay.Function([], output)
mutated_mod['func_7675'] = func_7675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6393_call = mod.get_global_var('func_6393')
func_6395_call = mutated_mod.get_global_var('func_6395')
call_7700 = relay.TupleGetItem(func_6393_call(), 0)
call_7701 = relay.TupleGetItem(func_6395_call(), 0)
func_4530_call = mod.get_global_var('func_4530')
func_4531_call = mutated_mod.get_global_var('func_4531')
call_7703 = relay.TupleGetItem(func_4530_call(), 1)
call_7704 = relay.TupleGetItem(func_4531_call(), 1)
func_7501_call = mod.get_global_var('func_7501')
func_7503_call = mutated_mod.get_global_var('func_7503')
call_7717 = relay.TupleGetItem(func_7501_call(), 2)
call_7718 = relay.TupleGetItem(func_7503_call(), 2)
output = relay.Tuple([call_7700,call_7703,call_7717,])
output2 = relay.Tuple([call_7701,call_7704,call_7718,])
func_7722 = relay.Function([], output)
mod['func_7722'] = func_7722
mod = relay.transform.InferType()(mod)
output = func_7722()
func_7723 = relay.Function([], output)
mutated_mod['func_7723'] = func_7723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5342_call = mod.get_global_var('func_5342')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_7930 = func_5342_call()
call_7931 = func_5342_call()
output = relay.Tuple([call_7930,])
output2 = relay.Tuple([call_7931,])
func_7958 = relay.Function([], output)
mod['func_7958'] = func_7958
mod = relay.transform.InferType()(mod)
output = func_7958()
func_7959 = relay.Function([], output)
mutated_mod['func_7959'] = func_7959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6809_call = mod.get_global_var('func_6809')
func_6810_call = mutated_mod.get_global_var('func_6810')
call_7990 = func_6809_call()
call_7991 = func_6809_call()
func_1420_call = mod.get_global_var('func_1420')
func_1424_call = mutated_mod.get_global_var('func_1424')
const_7993 = relay.const([2.116304,4.923350,-4.770333,-8.052646,0.650183,0.087535,9.246135,-7.451721,-6.186386,-5.882415,6.637408,-5.727689,1.061027,-2.631531,-4.824803,-0.357412,-0.222004,4.473557,2.461351,-3.231763,8.891070,9.897590,7.941085,3.411718,-0.808307,-5.754584,-4.454663,2.656617,-1.587765,-3.528319,-0.426113,-3.970885,-0.087250,7.058124,4.238369,3.647882,8.772501,8.709923,-5.026286,-6.739546,-2.816829,-4.176739,-7.041955,0.564133,0.849365,8.470275,-9.656132,-4.132658,6.314285,-7.889245,8.605018,5.272558,-0.694957,3.823393,-2.472698,2.464304,7.323434,0.010247,0.525730,-3.356389,-6.298108,-8.887760,3.390492,9.295792,-1.858025,-8.582724,2.823104,-0.509498,-9.891238,-2.976010,4.145089,-3.820769,9.646000,-0.475246,-4.168145,2.740870,-7.955747,5.006486,3.400078,-5.959387,-2.738991,5.176043,9.468202,8.064412,-9.699443,-9.329407,4.445849,-3.430196], dtype = "float64")#candidate|7993|(88,)|const|float64
var_7994 = relay.var("var_7994", dtype = "int64", shape = (504,))#candidate|7994|(504,)|var|int64
call_7992 = relay.TupleGetItem(func_1420_call(relay.reshape(const_7993.astype('float64'), [1, 8, 11]), relay.reshape(var_7994.astype('int64'), [504,]), ), 1)
call_7995 = relay.TupleGetItem(func_1424_call(relay.reshape(const_7993.astype('float64'), [1, 8, 11]), relay.reshape(var_7994.astype('int64'), [504,]), ), 1)
output = relay.Tuple([call_7990,call_7992,const_7993,var_7994,])
output2 = relay.Tuple([call_7991,call_7995,const_7993,var_7994,])
func_8012 = relay.Function([var_7994,], output)
mod['func_8012'] = func_8012
mod = relay.transform.InferType()(mod)
mutated_mod['func_8012'] = func_8012
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8013 = relay.var("var_8013", dtype = "int64", shape = (504,))#candidate|8013|(504,)|var|int64
func_8012_call = mutated_mod.get_global_var('func_8012')
call_8014 = func_8012_call(var_8013)
output = call_8014
func_8015 = relay.Function([var_8013], output)
mutated_mod['func_8015'] = func_8015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3632_call = mod.get_global_var('func_3632')
func_3634_call = mutated_mod.get_global_var('func_3634')
call_8031 = func_3632_call()
call_8032 = func_3632_call()
var_8046 = relay.var("var_8046", dtype = "bool", shape = (8, 3, 5))#candidate|8046|(8, 3, 5)|var|bool
bop_8047 = relay.floor_mod(call_8031.astype('float64'), relay.reshape(var_8046.astype('float64'), relay.shape_of(call_8031))) # shape=(8, 3, 5)
bop_8050 = relay.floor_mod(call_8032.astype('float64'), relay.reshape(var_8046.astype('float64'), relay.shape_of(call_8032))) # shape=(8, 3, 5)
func_6362_call = mod.get_global_var('func_6362')
func_6366_call = mutated_mod.get_global_var('func_6366')
const_8052 = relay.const([[5.977207,-6.407978,-3.144994,-1.587846,7.278874,2.080070,-1.672582,0.190283,4.898561,8.206520,8.886585,-4.032695,5.065707,-6.057370,-8.187645,-9.207402,0.332203,-2.299967,-6.754303,-5.460722,6.312870,1.509115,4.323840,-2.977214,-6.261081,5.726016,-5.390205,-8.513312,5.732245,-4.849391,-4.806415,5.829263,3.486729,-8.580881,-3.271112,3.270512,-6.201728,4.031353,0.064062,3.102982,6.392471,-7.115892,-1.935890,7.968885,4.815250,2.320864,6.891216,6.448419,-9.325396,-3.640968,-9.489943,-0.715336,-4.421551,3.294305,2.136183,2.590377,4.649041,5.578979,-5.744112,9.396984,-7.404391,-5.268289,8.084855,-5.090959,7.514203,-4.012071,8.289492,-4.835705,-0.663219,2.355528],[-8.029599,0.185276,-8.115171,8.192774,4.358532,-8.219138,-0.696179,0.809073,5.500200,9.553898,-8.435320,-9.821882,9.214036,0.509790,-3.323398,1.234645,8.038215,-8.021694,2.947907,9.692597,-1.873713,-6.678165,-8.894572,-8.294254,-0.751308,-4.097084,5.968515,-1.407718,9.285724,8.283444,-6.848998,3.810304,2.676682,-2.431000,3.347277,7.236067,1.677900,-4.326824,-9.787139,1.158815,2.560696,8.685152,2.084946,8.593781,-2.080962,-5.543805,6.217867,-1.053655,-3.341059,-7.569587,-0.797340,7.485499,6.132063,1.279629,2.243683,-5.792583,-9.386327,7.101219,0.102530,8.786664,6.845373,3.474693,3.325862,4.566170,-4.283260,5.860481,-1.808507,-8.305799,8.108128,0.792040],[4.888447,9.082038,2.098225,7.541013,0.554663,-8.114100,-7.807228,1.030668,-4.228070,9.947567,-1.766893,2.582031,-5.546234,0.597606,-7.095642,-9.741067,-3.810711,0.365590,-3.349891,9.432479,8.805360,2.706178,6.768085,9.451071,5.394212,-2.780531,-7.287181,-6.627332,0.061164,-1.174126,-6.852241,7.480639,-2.587398,8.971804,1.000894,-2.758484,-9.482582,3.626988,-0.554232,8.903961,2.494973,-7.945223,-7.180946,-5.755884,-7.132619,4.697505,8.640337,4.906040,2.672621,1.528100,1.285323,-9.214369,3.561947,6.656377,-9.422447,9.339695,-6.706484,3.934423,2.326506,7.740205,-9.135197,-6.814929,5.798959,4.054374,-3.560563,-9.794423,-3.013894,-2.532187,-9.348918,-1.031012],[-1.014948,-0.759661,5.131899,1.938349,-3.303227,-5.143403,1.335075,-8.643905,-9.918607,-5.066755,-7.230379,1.207650,1.317736,-7.394368,1.608362,-2.216464,3.683927,1.135156,4.533587,1.129591,9.736061,-8.017597,-3.892189,7.125340,0.382743,-4.534426,-5.671136,-9.654755,6.296870,3.370257,7.127055,-5.948864,2.969428,4.357857,9.321723,-3.565053,-9.322247,4.095121,5.254895,-3.174334,-5.144692,7.920430,-6.009131,-8.606126,-7.994813,-6.066487,-2.582626,-8.818269,-6.085489,-1.471009,-9.504119,-7.505803,2.929006,-1.782268,5.435130,6.024891,5.168277,-8.264497,8.608211,8.831138,9.546710,6.994786,-8.706271,3.063641,-1.229569,-2.638414,-1.939102,8.479056,5.094244,-6.429063],[-9.543202,-4.431599,-2.869956,5.263691,-8.183153,-6.975451,5.797206,1.887782,7.383592,-8.107260,-4.580882,8.141952,-6.572011,-2.107139,-7.935973,-8.818820,1.741806,-1.661359,0.118269,0.803025,-9.397946,1.111022,8.498045,1.648872,4.295788,-7.314288,8.134428,-4.715705,9.523600,3.786789,-6.784440,-9.991427,-6.862624,5.955603,4.001021,2.599412,-4.483289,8.735108,6.821713,7.436746,-3.121908,-9.723840,1.394270,8.447664,-4.139129,-6.914513,-2.692796,-0.015421,5.950075,8.640513,-5.029064,-0.591083,8.048714,-2.825484,-1.613562,-0.294528,-0.580243,-2.726713,5.490380,-7.991636,-8.349547,-6.584310,0.706211,-0.282610,7.322176,5.175569,-1.084679,-7.091663,5.014076,5.303710],[-5.512420,0.454003,-7.524865,-0.503924,2.585834,8.182434,1.811359,4.039423,-9.921447,5.790956,8.921240,2.404534,-1.416878,6.769590,9.632649,-5.294895,-5.525958,-3.590897,4.184419,7.595200,7.694974,8.163014,-3.625451,7.936311,-6.397654,-1.596010,-9.559595,6.512321,-6.417881,-3.817479,3.141170,6.000312,-7.678937,9.831241,4.863332,5.839366,5.620222,1.945413,0.523166,8.232705,-0.296400,9.071170,0.359404,9.693683,9.105700,4.776211,-4.419044,6.209223,-4.162282,4.059110,1.834390,-5.505911,2.706260,-8.756433,1.335406,-7.036346,-1.418965,-3.980679,-8.319458,6.563805,1.549026,9.202990,9.544613,6.232366,5.629245,2.705499,9.511772,3.947507,-4.961484,8.329746],[3.586097,0.228847,8.234223,-1.302516,8.481293,4.797710,-7.313120,0.265808,7.823860,-4.336581,3.884973,8.582113,4.797076,1.961401,4.941309,8.619166,-0.370972,-3.008068,-1.679050,9.936259,-1.617715,2.344311,3.481227,-7.813909,7.040356,3.814028,9.736576,2.175010,-9.076782,-7.347728,0.637770,-9.497948,-1.025879,1.521903,2.640792,-7.266524,1.778404,0.716299,-8.397331,-5.254498,-7.404556,-2.386291,-7.555371,-5.372517,-2.898576,-5.430417,8.045955,5.130261,2.702477,-2.710568,-7.761712,-6.196985,-0.312796,-3.202819,-0.422170,-8.917466,2.540059,-0.345575,-4.310979,-0.140395,3.483305,-3.044519,5.367764,-6.586677,-2.516969,-3.835772,3.939652,9.968614,-7.880747,7.437526],[-6.650469,8.498488,-5.767182,1.900526,-8.879276,-8.292650,8.058280,-8.631032,-9.746623,4.213172,-0.140431,8.349564,6.317637,5.627114,5.082173,-8.323067,8.756952,5.918406,8.283131,-6.057211,-0.515554,5.345487,-5.608745,-1.861866,-9.718164,2.138012,6.451834,-2.303479,5.366493,-9.478523,-2.874175,-1.094498,-6.256727,-3.729445,6.202409,-9.060213,1.054730,1.225216,0.561385,-5.770203,2.902753,-2.562144,4.282828,2.841820,2.529977,1.879447,-8.495792,5.110740,8.916754,-2.337953,-5.894570,-1.038966,-9.525332,7.848255,8.139658,2.078663,-6.935841,-5.911045,7.944380,-0.725959,7.912466,-1.713039,-2.867508,4.660410,7.470321,-0.847535,-3.216001,8.187725,-9.661155,-3.338075],[3.220659,-4.292577,-1.633773,6.573701,5.447873,-9.494194,1.211656,-3.145489,-5.638951,1.026895,-9.247529,7.409574,-7.024340,9.691964,-9.748132,-5.138096,-6.440668,6.662923,6.703065,-3.074666,-4.437701,-9.044452,5.777915,4.190505,-0.321755,-3.628678,-8.013183,5.078574,-6.815843,7.883176,-9.700853,-8.528839,7.681817,4.415114,-1.366225,8.141747,-7.950462,-3.602928,-8.340180,9.330337,-3.921392,6.648712,-8.093883,0.554516,-6.177040,7.771354,1.666912,9.877178,1.390136,2.743348,-5.461276,-1.086945,-1.508515,-5.599700,7.410526,1.519818,8.216155,-8.574951,6.814443,3.919863,1.949274,1.004000,-5.808094,7.073057,5.054883,-0.365211,4.599587,7.219449,0.557108,-3.593394],[4.165886,6.794987,6.471654,-2.892756,5.540452,-2.313941,-9.431357,3.108833,-3.168363,-6.440537,-2.335207,4.539522,-8.407124,9.157092,-5.352027,-1.226252,-9.923168,7.454716,4.442877,-7.598521,8.848641,7.164100,-6.397339,-3.308791,2.107575,4.318967,7.063628,8.529049,6.002003,-6.312225,3.697289,8.951687,-9.149970,7.445334,0.707741,-9.601564,-3.560611,-1.732669,4.371550,7.055625,-7.382340,-0.616503,7.604473,6.776925,-3.520097,-5.428327,-4.669398,4.026846,-6.312975,-0.926505,3.824076,-3.827986,5.051884,-1.197027,-5.700026,8.167395,-8.243439,-0.695906,-0.121984,-8.892662,0.065779,-9.440346,1.344038,-6.124457,-9.728378,7.626701,-4.032280,3.162378,-4.509222,-1.728423],[4.974727,4.745296,3.193921,8.941478,7.704680,-2.089658,-4.902238,-9.657185,3.406927,-3.605262,-5.035199,5.378737,9.483446,-4.126805,-9.731720,-1.609415,-2.655087,-2.340041,-5.753360,9.906192,7.941446,-9.973460,-7.588675,7.646168,-4.615818,3.014999,6.656952,2.257046,9.589551,2.404336,-1.346425,2.855727,4.912023,-1.293065,0.288301,-1.545589,3.598164,6.638409,5.865739,1.514309,-4.271923,-4.333890,2.407201,-4.106028,8.379692,7.290054,-7.854818,6.032850,-2.739476,7.314514,8.164863,-0.911704,-5.554127,8.707289,7.518388,2.453371,7.401307,0.829509,3.595562,-1.836413,0.822576,-3.767582,-1.201616,-1.433861,2.433027,2.718222,7.285093,-1.031791,6.439869,2.149810],[-1.842909,-7.270410,1.070167,2.308322,6.154526,1.464724,7.334642,-6.172150,0.980926,-4.806633,-6.152978,-8.745662,6.933991,-4.989474,-1.861691,0.078279,-5.916885,-3.593598,-2.493625,5.811235,8.655579,-5.603259,-4.714209,8.254116,2.298409,1.005130,3.434792,7.330242,-3.033499,5.254490,-0.305305,4.048891,-4.820204,-6.628472,5.810116,-2.266558,-5.179370,0.647286,-7.546345,9.095328,-7.812420,7.991720,-0.954603,5.411032,-1.980300,9.788431,1.442447,-2.900378,-4.093507,-6.056215,-6.077960,6.991792,-6.479253,2.627083,2.032736,-4.970259,1.011388,7.219767,8.432812,-8.650453,5.949569,-7.329393,2.742423,-6.447797,4.128873,2.066308,6.769129,-2.239414,-3.637096,-1.539239],[-1.923740,3.948509,0.622131,9.160316,2.389356,-0.992614,9.717672,-6.810715,5.959611,4.324150,0.956961,-0.185160,1.365689,-8.537813,3.857333,3.718658,-3.641532,4.468728,6.498757,-3.665290,5.025755,9.249509,7.900570,9.382847,-1.839359,8.464625,5.341315,-5.329536,-2.412364,-1.060631,-4.995852,-1.671786,5.742840,-8.488504,-7.252185,5.739288,5.960981,7.664535,-3.333032,-2.085676,5.192680,2.909382,1.190816,8.164030,-8.974543,3.571440,2.680410,8.363019,-4.960501,2.767633,-6.839594,-4.250221,2.578039,-5.967729,-0.761017,-2.360802,-4.980732,-5.845901,7.435413,-0.169601,-1.567015,-1.072061,0.747848,-9.532481,0.290795,-3.422020,-4.242716,-1.945533,-5.785602,-9.502386],[7.158061,-8.613922,-1.950082,7.133004,-5.637144,2.243868,-1.582664,-4.212159,-5.385565,8.614522,-3.246192,3.408074,-6.776122,-2.659473,1.545106,9.042511,4.661696,-5.602882,-8.731796,-5.494349,5.886452,3.184071,8.064247,2.129459,-7.956184,-2.503841,0.110441,-9.485741,5.880116,-8.797668,0.251469,8.280532,-1.525642,-7.050401,6.049748,8.739575,-1.291849,-0.045293,8.544525,3.950729,-2.467728,-4.815248,-7.479788,8.221616,-0.372482,-4.643862,6.148517,-9.044610,2.854449,0.449543,0.112590,-5.061365,6.060684,-9.757633,-4.423999,5.521152,8.673451,-1.590699,-4.150964,1.389182,-9.658263,-3.144444,2.140626,3.232863,5.507265,7.423278,4.907265,-2.113309,4.761085,6.765552],[0.548804,-9.708058,3.059277,-2.065849,9.558691,-9.927024,5.984873,4.743281,7.715891,7.199258,4.492783,-7.862686,-4.190038,-6.603415,1.233413,-1.106177,-5.321272,4.924584,6.133492,1.516734,9.520183,-6.634036,-9.967988,8.383657,-2.747065,-8.086476,1.197232,1.820167,6.317918,1.354757,0.388523,0.037757,4.499481,4.271391,-2.373807,5.966224,-5.533164,-1.439831,8.202038,3.664406,6.907106,-9.391592,-3.345597,-6.035550,8.987188,-3.276867,9.423568,-3.825460,-0.662839,-5.470761,-0.077197,-6.610430,3.532896,0.607990,-2.372421,4.701715,-6.221365,-1.199470,5.513074,-0.094627,3.406482,1.784968,2.091505,7.687277,-4.400462,-6.755694,4.681202,3.291519,-3.215029,4.550766],[6.288143,-9.274662,-2.857127,-8.760391,9.485138,-2.769630,1.851265,-1.049860,0.639393,-0.876765,1.259453,-2.042994,1.900593,3.615780,-3.050453,-9.842749,8.324382,0.574156,-1.099383,5.550601,3.986562,-1.616214,-5.653377,4.535497,-1.720814,8.528881,-1.497109,-3.117313,0.199756,8.376325,-3.863920,-6.990003,-8.415210,-1.994591,7.345315,4.509957,0.989739,-3.761726,-6.395995,-9.269385,5.862617,-8.142827,9.782890,-4.883706,-5.628458,0.960484,0.796878,5.501835,5.597561,-9.387296,4.946590,3.432282,6.304284,-6.629299,5.752600,-8.205292,-2.340365,5.112381,4.920133,1.325428,8.378713,5.454789,-3.722144,7.950554,-1.217894,-0.711446,9.482883,-4.005708,9.156276,-1.822468],[6.092874,-1.763132,0.362861,-1.641625,9.988610,-3.234336,-2.649589,5.268620,-7.234990,-8.441717,5.537441,5.162020,7.326065,2.005565,-6.388930,7.993436,1.270629,-1.012119,4.066636,1.272001,-6.124314,-3.311361,3.920978,1.834008,-9.663442,-3.394000,-8.822956,-7.005713,-0.256454,8.820675,8.057860,-5.911389,-3.206060,0.831031,4.473271,-7.151323,-1.660736,-7.869527,-7.496358,-0.667739,-6.377564,-4.861094,-7.212519,-1.276397,9.993390,7.488218,-9.609191,6.728352,-9.323212,8.132190,2.186051,0.625086,-0.018386,-9.205534,4.497019,7.709678,1.599627,3.674957,-8.046402,-2.471107,8.679440,-2.184976,-4.559493,-5.923214,-1.464654,-0.416254,9.589843,3.190598,-2.716644,-9.020784],[-9.594937,0.029199,-2.836508,5.767329,-9.741760,-7.473195,-1.183746,2.681435,-2.086828,1.715482,6.222374,-4.571462,-0.874609,-0.868781,2.493388,-7.677499,-5.823011,-8.150385,-4.245536,6.573933,1.070445,-4.621461,-7.512174,-9.607279,5.263034,1.744001,-9.261829,5.120089,-5.989172,4.753185,0.834257,3.353042,8.852231,-8.562272,-9.442382,-0.943486,0.266433,6.980487,-5.065033,-5.131338,0.912575,6.103638,4.658656,-9.670100,-9.801111,-7.434750,-4.450769,-8.906174,5.403817,4.266049,-2.242799,7.753166,3.368582,-1.386220,2.919299,0.247941,-6.346796,-8.249729,-6.791349,0.445480,-6.182194,-2.051244,-1.383376,-0.830562,6.867486,3.135440,3.633478,1.453543,8.915956,-8.712304],[-4.064789,5.816428,-6.598696,-9.398912,3.706331,-8.166941,7.428387,-4.153030,9.582406,8.931305,-4.946518,-6.701664,-8.921509,-1.646908,7.121448,-8.772233,5.024515,6.209165,7.114660,-8.488256,1.852299,-4.967710,1.621837,-2.826299,9.965384,8.019504,-6.370195,8.676649,8.361892,-9.931073,-3.552046,-2.557609,4.118039,-5.076346,7.090795,8.884890,7.155886,-2.651624,-7.489974,8.854809,-7.360847,0.612405,-5.248152,6.495352,7.516475,7.310048,-2.560477,8.251903,2.495493,-9.425708,-6.936080,0.977910,4.933345,-1.209171,3.717728,6.644115,-4.125847,-8.295416,7.765294,-1.392058,-1.755204,7.498292,6.948737,-5.759858,-0.906446,8.762847,-2.219140,-6.425673,-2.760245,3.473353],[-0.384647,-4.943647,2.324656,1.470951,-9.235940,0.724736,1.329588,-5.679980,9.900403,8.120484,6.541943,-6.770937,-1.812738,-7.892672,1.681658,-0.550562,-1.981837,-8.166799,9.640129,7.088154,6.205071,-0.474583,8.546627,3.265256,3.745677,-9.351922,-0.341753,-8.720530,7.919695,6.934032,-1.972381,-1.813645,-9.411615,9.934746,-7.661846,-8.911318,1.832839,2.783898,4.562902,-2.590280,0.903156,3.559971,1.253894,-1.815963,-0.546565,-7.809330,7.871538,-5.483468,1.933243,-9.063522,-0.689046,-5.689883,0.889100,-7.640362,-0.828014,-5.111644,3.774441,1.435389,8.179824,7.612262,-1.623398,4.690593,-3.157052,2.428366,6.508661,6.912179,-9.626399,1.929280,8.785444,-3.168088]], dtype = "float32")#candidate|8052|(20, 70)|const|float32
call_8051 = relay.TupleGetItem(func_6362_call(relay.reshape(const_8052.astype('float32'), [700, 2]), relay.reshape(bop_8047.astype('float32'), [8, 3, 5]), ), 2)
call_8053 = relay.TupleGetItem(func_6366_call(relay.reshape(const_8052.astype('float32'), [700, 2]), relay.reshape(bop_8047.astype('float32'), [8, 3, 5]), ), 2)
output = relay.Tuple([bop_8047,call_8051,const_8052,])
output2 = relay.Tuple([bop_8050,call_8053,const_8052,])
func_8062 = relay.Function([var_8046,], output)
mod['func_8062'] = func_8062
mod = relay.transform.InferType()(mod)
var_8063 = relay.var("var_8063", dtype = "bool", shape = (8, 3, 5))#candidate|8063|(8, 3, 5)|var|bool
output = func_8062(var_8063)
func_8064 = relay.Function([var_8063], output)
mutated_mod['func_8064'] = func_8064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6120_call = mod.get_global_var('func_6120')
func_6122_call = mutated_mod.get_global_var('func_6122')
call_8068 = relay.TupleGetItem(func_6120_call(), 1)
call_8069 = relay.TupleGetItem(func_6122_call(), 1)
output = call_8068
output2 = call_8069
func_8093 = relay.Function([], output)
mod['func_8093'] = func_8093
mod = relay.transform.InferType()(mod)
output = func_8093()
func_8094 = relay.Function([], output)
mutated_mod['func_8094'] = func_8094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8185 = relay.var("var_8185", dtype = "int64", shape = (2, 9, 14))#candidate|8185|(2, 9, 14)|var|int64
var_8186 = relay.var("var_8186", dtype = "int64", shape = (2, 9, 14))#candidate|8186|(2, 9, 14)|var|int64
bop_8187 = relay.less_equal(var_8185.astype('bool'), relay.reshape(var_8186.astype('bool'), relay.shape_of(var_8185))) # shape=(2, 9, 14)
var_8193 = relay.var("var_8193", dtype = "int64", shape = (2, 9, 14))#candidate|8193|(2, 9, 14)|var|int64
bop_8194 = relay.logical_xor(var_8186.astype('int64'), relay.reshape(var_8193.astype('int64'), relay.shape_of(var_8186))) # shape=(2, 9, 14)
func_7674_call = mod.get_global_var('func_7674')
func_7675_call = mutated_mod.get_global_var('func_7675')
call_8216 = relay.TupleGetItem(func_7674_call(), 0)
call_8217 = relay.TupleGetItem(func_7675_call(), 0)
bop_8226 = relay.right_shift(bop_8187.astype('int16'), relay.reshape(var_8185.astype('int16'), relay.shape_of(bop_8187))) # shape=(2, 9, 14)
func_6809_call = mod.get_global_var('func_6809')
func_6810_call = mutated_mod.get_global_var('func_6810')
call_8233 = func_6809_call()
call_8234 = func_6809_call()
output = relay.Tuple([bop_8194,call_8216,bop_8226,call_8233,])
output2 = relay.Tuple([bop_8194,call_8217,bop_8226,call_8234,])
func_8253 = relay.Function([var_8185,var_8186,var_8193,], output)
mod['func_8253'] = func_8253
mod = relay.transform.InferType()(mod)
mutated_mod['func_8253'] = func_8253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8253_call = mutated_mod.get_global_var('func_8253')
var_8255 = relay.var("var_8255", dtype = "int64", shape = (2, 9, 14))#candidate|8255|(2, 9, 14)|var|int64
var_8256 = relay.var("var_8256", dtype = "int64", shape = (2, 9, 14))#candidate|8256|(2, 9, 14)|var|int64
var_8257 = relay.var("var_8257", dtype = "int64", shape = (2, 9, 14))#candidate|8257|(2, 9, 14)|var|int64
call_8254 = func_8253_call(var_8255,var_8256,var_8257,)
output = call_8254
func_8258 = relay.Function([var_8255,var_8256,var_8257,], output)
mutated_mod['func_8258'] = func_8258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8300 = relay.var("var_8300", dtype = "uint8", shape = (16, 14, 6))#candidate|8300|(16, 14, 6)|var|uint8
var_8301 = relay.var("var_8301", dtype = "uint8", shape = (16, 14, 6))#candidate|8301|(16, 14, 6)|var|uint8
bop_8302 = relay.less(var_8300.astype('bool'), relay.reshape(var_8301.astype('bool'), relay.shape_of(var_8300))) # shape=(16, 14, 6)
func_2900_call = mod.get_global_var('func_2900')
func_2902_call = mutated_mod.get_global_var('func_2902')
const_8308 = relay.const(1, dtype = "uint16")#candidate|8308|()|const|uint16
call_8307 = relay.TupleGetItem(func_2900_call(relay.reshape(const_8308.astype('uint16'), [])), 2)
call_8309 = relay.TupleGetItem(func_2902_call(relay.reshape(const_8308.astype('uint16'), [])), 2)
uop_8312 = relay.rsqrt(var_8300.astype('float64')) # shape=(16, 14, 6)
func_5324_call = mod.get_global_var('func_5324')
func_5327_call = mutated_mod.get_global_var('func_5327')
var_8320 = relay.var("var_8320", dtype = "float32", shape = (567, 2))#candidate|8320|(567, 2)|var|float32
call_8319 = relay.TupleGetItem(func_5324_call(relay.reshape(var_8320.astype('float32'), [1134,])), 0)
call_8321 = relay.TupleGetItem(func_5327_call(relay.reshape(var_8320.astype('float32'), [1134,])), 0)
output = relay.Tuple([bop_8302,call_8307,const_8308,uop_8312,call_8319,var_8320,])
output2 = relay.Tuple([bop_8302,call_8309,const_8308,uop_8312,call_8321,var_8320,])
func_8331 = relay.Function([var_8300,var_8301,var_8320,], output)
mod['func_8331'] = func_8331
mod = relay.transform.InferType()(mod)
var_8332 = relay.var("var_8332", dtype = "uint8", shape = (16, 14, 6))#candidate|8332|(16, 14, 6)|var|uint8
var_8333 = relay.var("var_8333", dtype = "uint8", shape = (16, 14, 6))#candidate|8333|(16, 14, 6)|var|uint8
var_8334 = relay.var("var_8334", dtype = "float32", shape = (567, 2))#candidate|8334|(567, 2)|var|float32
output = func_8331(var_8332,var_8333,var_8334,)
func_8335 = relay.Function([var_8332,var_8333,var_8334,], output)
mutated_mod['func_8335'] = func_8335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mod.get_global_var('func_4280')
func_4281_call = mutated_mod.get_global_var('func_4281')
call_8376 = func_4280_call()
call_8377 = func_4280_call()
output = relay.Tuple([call_8376,])
output2 = relay.Tuple([call_8377,])
func_8384 = relay.Function([], output)
mod['func_8384'] = func_8384
mod = relay.transform.InferType()(mod)
mutated_mod['func_8384'] = func_8384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8384_call = mutated_mod.get_global_var('func_8384')
call_8385 = func_8384_call()
output = call_8385
func_8386 = relay.Function([], output)
mutated_mod['func_8386'] = func_8386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_8490 = relay.TupleGetItem(func_5577_call(), 1)
call_8491 = relay.TupleGetItem(func_5579_call(), 1)
output = relay.Tuple([call_8490,])
output2 = relay.Tuple([call_8491,])
func_8520 = relay.Function([], output)
mod['func_8520'] = func_8520
mod = relay.transform.InferType()(mod)
mutated_mod['func_8520'] = func_8520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8520_call = mutated_mod.get_global_var('func_8520')
call_8521 = func_8520_call()
output = call_8521
func_8522 = relay.Function([], output)
mutated_mod['func_8522'] = func_8522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2337_call = mutated_mod.get_global_var('func_2337')
call_8616 = relay.TupleGetItem(func_2336_call(), 0)
call_8617 = relay.TupleGetItem(func_2337_call(), 0)
func_2019_call = mod.get_global_var('func_2019')
func_2022_call = mutated_mod.get_global_var('func_2022')
const_8622 = relay.const([3.746253,-8.636633,-4.846753,-9.200683,-1.332705,-1.029022,-5.041337,1.185044,-6.903773,4.024576,0.495810,-2.001243,-4.925089,0.315823,5.101324,-5.169618,-3.626350,1.440478,2.357538,9.433286,2.896444,-1.484343,8.706703,-7.243742,9.384467,-7.886384,1.963592,7.986473,-7.304159,3.324565,3.332773,6.267194,-4.717849,-6.548304,-3.970189,-3.615598,-7.013138,2.301848,-4.485782,5.484044,6.527885,6.036248,-7.064566,-9.263235,4.538057,-6.752152,-0.628884,-1.720496,-7.412675,-3.002344,8.194503,-1.563874,3.468834,3.302219,-3.440628,9.848674,-2.473613,-1.316537,1.216481,5.292683,-1.711048,7.128676,5.646591,-8.569562,-8.728172,7.344405,9.672544,1.471688,1.181252,-2.832548,5.296673,-2.873181,-9.130244,6.988951,9.402280,-4.130909,-7.455737,-8.852951,-4.727052,-9.215386,4.705513,-2.717349,3.833416,5.981362,-9.043936,-1.116523,8.847401,5.240135,6.919397,2.120942,0.132028,6.135610,0.907162,-7.408700,-7.973761,9.108294,-4.321235,-1.107130,7.212166,-0.510041,8.457398,-2.982065,6.589875,2.128926,-0.161865,-0.017858,-2.345967,3.371146,9.017344,7.330390,-7.635955,-4.890128,-2.103638,4.843375,-3.953249,3.399893,-4.506613,6.663734,6.277038,3.500576,6.442474,-7.125764,4.296419,-7.243429,4.675018,-0.799409,-3.376563,-4.795739,8.835845,-5.347041,9.513153,7.383601,9.741108,-2.023664,0.956007,-3.174553,8.321046,0.096128,3.042833,5.764786,2.648544,-0.375639,-8.679395,2.676133,-3.271919,-6.279387,3.316939,-9.771275,-8.572778,-0.793834,-7.899784,-5.196892,7.780582,-0.041178,1.306737,0.791375,5.831856,-2.713349,-7.111428,9.223654,-2.612288,-4.721888,1.074177,-3.872428,3.591332,-9.517387,-2.462842,4.741777,-2.004161,-7.324537,-1.031944,-2.448312,6.575901,8.617671,-4.908818,2.634762,-4.733111,3.986157,-5.032924,0.667188,-1.822168,7.718993,9.463877,-4.554498,-1.387857,2.396006,-4.297203,-6.049763,6.299049,2.885275,-2.409992,-1.241931,-6.264107,-5.914383,5.202690,1.687307,6.827134,-4.781908,4.584328,-9.368419,8.900479,-4.222444,-4.319901,-5.201568,1.819309,7.897814,-6.015916,-5.452736,2.390881,3.791060,1.663433,-6.293144,2.726146,3.950659,3.473433,-1.801450,7.066700,-4.394201,7.132506,4.328576,-2.077720,-7.715378,-8.465003,-7.627686,1.363295,0.843260,-9.519945,-0.455166,-9.981812,-9.247696,6.922784,9.352908,-1.052315,-4.400604,-0.574218,-1.025740,1.758585,5.840337,8.938944,3.795109,4.736476,9.725797,0.294648,0.701718,7.129070,9.417643,-0.007182,-4.245324,1.912241,-9.269565,-4.573338,-8.087921,8.860453,-9.701918,4.751719,7.194540,-9.642995,-0.160696,-2.385088,3.185248,-0.633116,5.418882,8.844737,5.752116,-5.669364,-6.808402,-4.459022,-1.039502,-5.905126,-8.418522,0.803442,-3.108102,4.818109,0.238968,-1.686543,4.728800,8.866456,7.417510,-1.470645,8.148371,-3.165702,-5.658526,1.959512,-2.022070,1.295924,3.575259,5.689096,-6.603611,0.595771,-6.891575,-3.851457,-1.954429,-0.818067,5.627308,-0.582152,-0.665081,-2.970066,6.142511,9.231682,-0.520862,-3.498551,2.300261,0.807404,-3.988478,7.511951,9.651308,4.754821,-9.388056,4.720442,-1.672636,-4.210663,2.751365,4.758620,-1.562920,-0.481755,6.293581,8.167496,-9.048992,-2.002429,2.274062,-1.703143,-7.483566,-7.711603,2.059238,-3.800440,4.495165,-2.986787,5.380074,7.595810,1.621754,-7.757933,-4.281967,8.395521,8.752303,-3.033560,-0.777183,7.576173,-1.403547,1.988923,7.244913,4.108552,-4.913602,2.109815,-6.050551,-1.877327,0.323869,-3.283387,-1.897871,-5.495006,-8.721466,-3.920089,4.386418,7.084173,7.360998,-8.998001,-5.442798,0.997609,3.325602,-2.611488,6.708278,3.579930,-9.315047,-0.712364,-0.024997,-3.321863,3.032900,6.882629,-4.904376,-7.842519,9.579210,-3.376229,0.356356,-0.183126,0.989271,-1.150483,8.808634,5.521438,9.020081,-4.510183,-4.402453,-7.453397,8.360536,4.952454,-0.942119,9.312220,-7.082913,5.319595,5.629824,-6.675910,5.968540,2.003707,7.236599,-6.319943,8.559256,-6.719693,7.748386,9.710577,-2.837293,-3.123347,8.650449,-6.126826,6.512448,5.095815,7.530453,3.288498,-0.855056,-8.570994,0.800006,-9.531971,8.501774,7.803269,-9.697544,-9.681902,4.166309,8.669587,-7.850893,-4.913365,-0.560911,2.509827,6.977349,-5.916465,5.450343,9.822005,3.900448,9.020834,-7.663090,9.109299,-8.043311,6.294203,-3.885392,-5.323854,-8.289803,-5.503634,-5.262023,5.110843,6.821698,8.956186,-6.839585,6.148049,-7.173288,-8.657612,6.043500,1.258100,2.720228,7.656750,-7.826714,7.789568,-7.714329,6.112610,3.160663,8.009294,-1.047507,8.703533,0.051256,-8.172392,-5.397608,5.557328,-1.709949,6.973134,9.839633,4.486749,-8.188371,0.455818,-6.887867,0.126759,0.678917,-5.405105,7.491656,-2.190917,9.014493,-1.030766,7.958207,6.621260,9.828845,-2.997250,-3.276527,-6.902059,-6.416450,7.078859,-8.210372,-3.081519,0.526987,6.330173,-6.509553,-8.400169,-7.818931,7.200161,-2.256362,0.104591,8.975809,-1.887255,9.488169,-6.422354,-0.711678,-1.580459,-9.913734,-6.161083,-4.472769,-7.359867,3.869634,-7.493572,-8.874902,-2.601198,-4.335299,-4.051627,0.781230,6.822343,9.040661,-3.683412,-6.073560,-2.439770,1.870394,-3.853412,-1.772401,-7.869197,4.813395,4.529040,0.190242,-7.444513,6.347121,5.586925,-6.595638,8.830418,4.613123,5.298206,-6.066635,-0.728893,0.041562,5.269556,-3.147843,3.710806,-2.086752,9.834185,-6.915790,-4.507779,-6.125661,-0.132069,-7.515157,-4.141084,5.999948,7.511902,5.896361,8.832951,5.231499,-1.101549,0.221111,3.279776,-6.810250,8.019952,1.569444,-8.381066,9.009913,-9.979502,-2.571750,6.797013,-1.140915,1.858078,8.032683,-7.342462,-5.592953,-6.564766,2.753169,4.563731,-8.438181,-2.395370,-1.340247,0.661017,-9.118580,-2.351151,-0.518871,-3.015049,-4.962094,-0.283681,3.318997,-5.006601,4.177146,8.115138,2.158408,-7.463890,1.882424,8.507948,0.105449,7.625949,-3.459675,-0.780048,-9.855266,1.643979,-5.255096,-1.078000,8.735714,0.730810,8.946489,7.137745,-7.490979,-2.274804,-6.285752,1.661109,-0.177217,2.048628,-2.458646,9.608677,2.651090,-0.967134,-4.550531,7.492336,6.520900,-8.238596,7.196671,1.055781,7.490986,6.394189,7.893006,9.014249,1.223874,-1.552271,-1.852594,-2.022623,3.583436,0.653461,7.970240,8.498379,-3.815691,6.155230,7.094516,6.245729,-1.200375,-9.524655,0.302061,6.065712,4.061274,3.165389,0.899833,2.551026,-2.733958,-6.334244,4.185943,-0.932434,0.682114,5.662245,0.622852,5.293724,4.821342,0.526353,4.576525,0.884448,9.783699,-5.228015,1.905776,1.433118,9.856735,3.108835,3.575535,-7.700321,-7.664388,6.625622,-9.479834,4.921508,-0.927876,-9.717454,-4.822136,-7.366628,-9.985565,-6.465869,-0.451734,9.326124,-6.956911,-0.672801,2.257782,-3.333794,-3.599668,1.958543,1.678316,-4.207002,4.932965,9.356589,9.917452,6.649759,2.209537,3.107921,0.647777,9.146081,7.472813,5.139353,-8.046779,-1.603557,8.514157,7.119550,2.983258,4.517466,-2.782184,-1.475665,-0.965019,-8.038913,8.509632,-6.778645,-1.626506,-9.651052,9.516129,-7.597793,-1.534097,1.495965,-8.372558,-4.123452,-0.234115,8.407471,-2.988238,-5.472207,9.700240,-9.274244,-2.947445,-2.584225,-6.711278,4.676688,-5.947697,6.215195,-9.135858,6.664678,0.620586,-2.431422,1.064368,6.706017,1.702197,-1.907415,-7.938200,-9.679726,6.536305,5.067803,4.513457,-2.239790,9.907600,-9.089910,-0.961121,-4.435466,6.860838,4.676168,-7.273645,1.933883,5.747817,0.878090,-5.167741,-4.264414,-4.756402,-0.057235,-9.899828,7.349584,-5.429277,-8.593002,5.697010,4.224365,0.346506,7.557120,4.566748,-8.493008,2.592555,-4.367337,5.217177,2.308355,-2.920559,3.971253,-5.254864,-0.448093,9.555337,6.002005,-2.621956,2.153948,-1.385382,3.111337,4.281711,-6.686190,3.382836,0.182108,8.076115,-9.783414,-1.259133,6.317184,1.844411,8.213413,-7.031144,7.334683,2.355224,-0.910097,-8.353822,1.134907,6.993402,-9.752132,-6.815643,4.767154,-8.734087,-6.082342,-0.768662,-4.471859,9.851862,-8.514884,-9.590379,-3.630920,-1.836177,1.317907,5.113910,2.831781,-2.397063,3.935863,3.364222,2.482700,3.526472,-9.721732,4.183517,5.327911,-6.063180,-9.319407,4.775068,2.805407,4.797099,-8.221457,9.221634,-2.503496,2.423413,5.506842,-4.227209,5.052325,-6.184151,0.646676,-0.534503,-7.973967,-6.429244,9.670853,-1.864929,-0.696299,-7.927116,-8.864449,-6.734359,6.270998,-4.850800,-9.156859,3.997942,-8.389573,0.364200,0.283626,-1.620978,-5.375779,-7.875878,4.824421,-9.687234,4.664017,-0.273075,5.875232,-4.610911,9.300573,0.707281,3.336805,8.071225,-4.887465,-9.975397,-1.739179,2.770913,2.148289,-4.090184,-9.800405,-4.458345,0.910243,8.688871,1.232578,-7.897110,9.740686,-4.420742,-5.753338,-7.477880,-2.659080,7.124874,-9.310516,-3.896322,-8.365753,-3.636133,9.793957,-1.042386,1.598870,1.671820,7.828718,5.621047,0.661750,-4.785581,1.954323,-8.074643,8.835408,-8.511181,6.225835,6.133526,-8.863953,-1.953453,3.786360,-5.443675,2.886245,4.137852,0.410515,1.734695,0.282529,6.904906,-6.101330,-1.201267,0.388570,0.085795,4.280991,-1.456852,-8.778750,-1.304903,-5.135950,1.275076,-5.344686,-7.922653,1.458432,3.528883,8.486225,-3.593130,-7.161481,4.058457,8.484138,-1.886767,-9.295870,-1.108687,-1.149142,-7.229219,-0.327153,-1.900624,-3.361452,-9.410961,-4.953159,-2.760735,-5.797291,6.461488,-6.420823,-0.287831,-2.256668,-9.832931,-7.181074,7.104120,9.314320,3.133774,2.052113,5.239385,-2.240864,-6.774015,8.147130,0.418432,9.318344,-7.510714,7.156125,7.218241,-0.284752,-3.743740,8.980602,1.469109,2.606640,-0.273833,-8.685538,4.115827,3.120000,9.811250,-2.627160,4.978699,5.823527,5.538637,-1.515670,-0.675410,4.228534,2.577960,7.890963,4.361567,8.077947,1.903232,3.720865,5.140668,-1.453436,8.730654,3.716182,-0.793987,7.019078,1.436300,1.742176,-3.999193,1.642608,8.802954,-4.349835,9.600782,-1.904151,7.135444,4.757478,-6.943842,2.642011,4.516173,-9.505979,1.668252,2.489332,-5.504232,6.699732,7.247504,-6.348688,8.165172,-2.753856,8.441931,5.332527,-6.372855,8.372424,2.587796,3.985270,9.288159,-8.160596,0.054641,8.026766,-2.886890,-5.896644,5.228643,-3.625172,3.758773,-9.296775,8.723367,9.517063,-7.013842,2.700718,7.893931,-3.707214,-3.804242,0.848039,1.861324,2.915784,9.305838,2.442262,8.697382,1.660535,-5.940280,0.775894,-9.949191,-1.823494,2.230385,-0.879995,-4.209357,5.936568,4.738440,-0.878023,2.671497,7.883788,5.157115,-6.742699,-2.645348,1.025508,0.531522,6.007665,0.226701,-7.943216,6.350449,4.521752,-9.600450,-1.080416,6.587294,-1.625061,0.351061,-0.286526,-8.140386,3.786534,-8.521430,-3.921617,1.893948,5.152790,7.134357,1.394760,-8.222154,-8.250452,0.598106,7.315187,4.930475,7.433705,8.106316,5.322350,-4.775519,-5.652321,1.536529,-1.154064,-1.245608,3.273436,-1.620842,-2.484465,5.952160,3.924575,-8.451602,6.809946,-2.485332,-4.169786,-5.126046,5.782692,-9.006219,-0.789571,-6.713277,-4.860671,-4.007837,-6.046997,-9.053950,-4.738878,2.461959,-4.811079,-6.010038,8.386050,-7.053317,-1.502345,1.504311,-3.120284,7.798404,8.134110,8.985319,8.807707,5.362636,-4.145558,-5.004772,2.101787,-7.949743,9.728134,-0.530317,3.336990,-0.193294,1.299286,-8.586030,8.328055,-9.676529,9.819202,-1.554823,-4.230825,0.302277,6.552646,4.589779,7.078513,-6.148763,-1.505793,-7.726416,-0.196518,2.788102,-5.159513,3.679694,7.223129,7.079125,6.568587,9.135493,5.140875,6.991710,6.493281,-5.549167,-0.518194,9.220305,6.657560,6.940026,2.182733,5.360041,-0.194567,6.126615,3.459056,-1.537141,2.448787,-1.592867,-5.199278,1.881024,-4.667464,3.828305,9.738894,0.303707,-4.505316,-4.746140,7.116903,9.573119,-9.616720,6.010691,3.217373,-0.211761,-2.811186,-3.693085,-6.604008,-2.239017,3.269031,-2.733755,-3.622172,5.672671,-7.810517,-0.068939,7.529584,6.369415,0.938299,8.242448,-5.269980,1.500877,-1.397094,-6.600310,5.750246,4.610645,-1.357469,4.966902,8.632116,2.413688,-5.516715,8.593795,0.771642,7.536046,-3.722540,-1.589711,7.507079,8.152995,5.795030,-9.881994,-8.400381,8.146411,2.840131,2.643732,6.648295,-5.093211,1.807956,6.357202,-2.787925,7.920333,-5.253368,-6.268686,3.441314,3.983783,3.413880,1.151531,-6.364917,-4.240488,-3.407181,-2.053204,-0.287519,7.648759,5.244300,-5.967247,-1.191716,-8.370960,0.193601,-6.699384,-8.408898,5.900997,4.893223,5.599802,3.352474,-0.835032,2.127850,9.034175,2.127287,3.204791,-2.195367,5.810337,1.419121,4.761852,-4.870218,2.783211,1.850597,-5.164228,-7.152178,-5.794715,9.872912,7.390213,-9.894186,-2.529661,2.523127,-8.428394,5.127650,-5.378225,7.360730,-3.691090,1.179715,-1.157308,-5.606905,-8.383220,-3.379414,6.463734,9.798807,-4.648583,5.397377,7.418674,1.724901,-5.568294,3.190474,6.195680,-0.344920,-4.107253,-8.735294,7.125480,6.249091,2.718397,-0.391431,9.820942,9.866079,2.037432,-9.905142,9.988199,-5.919501,8.121404,7.875429,-8.690981,-9.223472,4.455789,8.126880,4.220190,-0.789769,-3.282259,2.071364,-0.035021,-1.679811,-8.231028,2.473546,-6.820059,2.196260,5.422001,-8.131814,7.702832,5.144165,5.407340,2.780822,0.370478,0.257096,-0.264600,-6.745870,8.164527,7.094367,1.268997,-3.284677,-8.650468,2.281442,-4.594979,-8.756482,-8.642453,-4.788421,-7.337015,9.514570,-9.137919,-7.594858,4.200768,8.570970,2.217769,-4.541308,5.175957,-3.334822,3.983804,-8.784415,9.202671,1.154379,-3.456497,-4.643874,4.339236,-1.473037,-0.261675,-8.280984,9.513776,2.079193,-9.377873,-4.504412,-9.173341,-9.241251,-7.136833,9.129496,4.577939,-6.263279,-5.440289,-3.535578,-1.667143,7.815762,5.336700,-6.559954,-4.156242,3.893643,-0.836577,-4.897285,-3.684824,-9.262131,9.307247,2.104648,-5.058003,-7.551945,-2.412926,-3.698328,-4.600442,9.568407,2.779629,-3.823176,8.897279,1.699308,3.715176,-1.779353,-6.009796,5.331873,-6.799461,-8.358905,-4.253300,-2.780288,8.820103,0.914519,-4.115063,-7.236991,-8.077370,3.195270,-2.769332,0.700752,0.894334,-0.503878,-2.826115,5.810096,-6.072500,9.574544,8.612277], dtype = "float32")#candidate|8622|(1400,)|const|float32
call_8621 = func_2019_call(relay.reshape(const_8622.astype('float32'), [10, 10, 14]))
call_8623 = func_2019_call(relay.reshape(const_8622.astype('float32'), [10, 10, 14]))
output = relay.Tuple([call_8616,call_8621,const_8622,])
output2 = relay.Tuple([call_8617,call_8623,const_8622,])
func_8626 = relay.Function([], output)
mod['func_8626'] = func_8626
mod = relay.transform.InferType()(mod)
output = func_8626()
func_8627 = relay.Function([], output)
mutated_mod['func_8627'] = func_8627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3726_call = mod.get_global_var('func_3726')
func_3727_call = mutated_mod.get_global_var('func_3727')
call_8647 = relay.TupleGetItem(func_3726_call(), 0)
call_8648 = relay.TupleGetItem(func_3727_call(), 0)
func_4016_call = mod.get_global_var('func_4016')
func_4019_call = mutated_mod.get_global_var('func_4019')
const_8650 = relay.const([-1.874346,9.880014,2.845940,2.786030,9.126019,7.318384,-6.903951,6.734591,-1.631873,5.725604,6.004449,-8.397943,7.004570,-1.057124,4.259273,7.226179,-5.112969,6.855804,-5.691513,3.870067,-1.201675,-9.450107,-9.354931,-5.280154,7.785509,-9.411950,8.539331,-9.677474,-4.799591,1.031563,3.820431,9.243166,2.610669,7.204267,5.189670,-1.332737,-0.443309,-1.145726,-9.789304,8.221896,-9.633927,-0.615830,-2.190879,8.992445,6.103413,-6.958874,4.076879,-5.070543,1.509554,-4.461019,-1.516582,-5.152861,6.924161,4.709568,0.697402,-5.738748,-7.249940,0.818341,8.524781,-6.198185,2.090147,3.275661,-0.638262,-1.333801,-4.603504,2.351580,1.626038,3.830404,-6.657921,-9.712042,3.762542,-4.828185,6.403770,-6.911116,-2.947669,9.797329,-4.745616,-7.154087,-9.872240,-6.125211,-8.450523,-6.198097,9.255903,-1.214894,-7.893267,-2.190543,8.279922,-0.084368,-8.371516,-9.186812,8.214684,1.589474,-0.157012,-1.964128,-5.567154,8.902571,-4.537925,-9.173278,8.922865,-9.968327,8.445031,1.560817,6.673200,7.929620,0.013450,-8.063730,6.165455,-9.734459,4.505704,-7.564407,9.678324,-8.348502,7.530971,8.860059,-1.633942,5.997739,-6.751381,-1.511535,-0.112494,-4.943350,5.431997,-2.488709,-6.567562,7.268174,6.944201,0.251594,2.594190,1.850428,-0.581019,-5.110159,-5.003703,-9.933201,-3.036602,-1.039244,-7.513066,-9.990759,9.359362,-6.433141,0.296140,8.457737,2.359975,0.753543,3.875474,-0.345349,-1.265048,-4.250149,-8.542411,7.889014,7.041441,7.190147,-1.761888,-5.253381,-3.811446,0.276530,-7.669193,-0.904564,9.423820,-0.301775,-5.329090,-4.660284,9.630591,8.837442,5.663647,2.274378,-5.506103,-5.185057,-8.826191,-0.211786,3.600917,2.859745,9.240961,-6.295358,8.411949,0.347564,8.946986,-0.185079,-8.923212,-7.125582,2.066879,-1.005199,-4.418426,-8.675457,2.314805,3.294115,9.075769,-8.447449,-5.121953,6.247030,-1.848143,-1.356518,0.191034,-8.629423,-6.594597,7.852700,-2.285376,-7.051775,5.035106,-9.930529,1.661362,2.330587,-1.698523,7.434297,-0.604021,-6.918710,4.186708,-8.220904,-6.321745,-0.922487,0.481651,-1.566413,-2.506557,-4.517631,7.148735,-6.611245,-7.350926,3.632641,-9.765554,-3.646994,-7.872817,9.354927,1.043642,-3.885164,-7.488017,-1.793100,-0.594639,-1.578572,7.681487,-5.984066,5.310941,-0.998131,0.084753,-4.627135,-2.446921,-7.169595,1.048684,2.549712,-2.863748,-1.867734,-1.776916,-0.878676,7.045965,7.493220,-4.971775,-0.311211,8.817719,9.948358,-1.126770,-9.060440,-2.563036,9.984202,-8.454879,-0.417779,-6.522176,3.662147,-7.294859,-6.108363,-8.459010,-6.572389,2.698649,-2.262267,6.977400,6.876226,2.431780,7.880788,7.730017,-8.258998,8.649014,-2.588058,9.270632,-9.023986,5.236465,-7.060290,0.618129,-9.951211,6.503061,7.635459,6.889632,-0.355036,-7.373153,-4.062418,6.236755,3.266292,-4.807323,-4.757444,4.161204,7.710744,3.801558,4.638074,-8.066464,-8.852530,-3.122777,1.183132,-3.977682,4.942791,1.350856,-7.587755,-1.739856,1.156278,4.624702,-7.268740,-9.349932,-3.255649,1.709499,-5.552379,6.780444,7.164443,-9.626628,8.296604,7.386450,5.228230,5.679990,1.411269,9.622680,-9.281510,-9.008895,-8.161265,-1.826576,4.039047,-7.114316,5.416432,-4.729644,4.119470,5.805769,0.763147,6.540474,8.652003,3.004268,-6.325454,9.878649,5.069743,-3.960204,7.992542,-0.820620,-6.729904,-4.467547,6.188509,3.636873,-8.012991,7.697975,6.071543,-9.043193,1.869897,2.950690,2.473192,-7.309236,-0.289275,-9.502387,5.378199,-7.062983,6.342728,-8.437683,9.135090,8.229470,-1.952715,-2.494388,-3.992282,7.823001,-2.493696,0.388190,2.812085,-7.012393,-9.658055,1.300446,-5.624030,-2.825999,3.981929,-8.155273,-9.354258,-8.196208,-4.119827,-6.210317,4.076066,1.633349,-7.932528,3.399500,-5.248652,6.524311,-7.748696,5.231292,8.386115,-4.458802,-7.201554,0.559656,7.721053,4.888351,-5.384947,-6.313062,6.944663,1.973388,-2.396434,-5.153819,0.563089,-0.262785,-3.854998,-2.097915,3.645378,-1.238222,9.346131,-2.005023,5.213269,-2.223830,1.637860,-3.690926,-2.238121,-6.952937,-8.443575,-7.497362,-4.771186,-8.607686,-8.813518,-3.077641,1.176075,4.386114,9.114460,1.498890,1.743710,-1.644244,-0.956180,-3.040460,0.151859,-4.912316,2.624253,1.177452,0.309574,-3.038691,-7.141623,2.166458,-7.338785,-3.717722,-4.946026,-3.539181,3.916191,-2.037143,3.394392,1.664094,3.301532,2.169895,-7.765485,-5.860714,-3.661921,8.427129,-6.113148,-1.355003,8.123111,-7.401947,3.064893,0.391926,2.259390,-9.772031,-9.465524,1.174454,8.983090,-9.699212,2.745611,9.287537,-8.422959,-2.878605,9.296098,1.832868,0.962470,-2.774360,-4.898559,-3.396855,0.621338,7.915603,-3.132897,8.747403,3.010981,0.631336,3.211947,-6.429191,2.889189,-0.597837,2.955438,3.682261,3.844051,9.157364,3.771098,3.224378,3.085862,3.609628,-0.757242,3.407146,-5.222236,-9.591531,-4.703920,5.436339,-1.457446,-7.517715,0.677190,-8.595010,-2.706224,3.113586,3.623452,-0.070743,5.705817,-6.943246,5.920182,7.562352,-5.133913,5.798369,-6.834177,-3.112305,-9.761009,-4.761198,-1.775856,-4.633675,5.118637,0.256539,-2.670747,7.637030,0.829809,4.422838,9.354636,-2.314105,2.244298,-4.607248,9.197028,-5.221230,-8.947495,5.021603,5.437354,2.003842,0.027190,-4.079710,-3.290754,5.614294,2.568490,-7.668924,8.254432,7.821897,-6.701217,-8.114511,-4.056122,1.134539,-5.685344,-9.063438,-0.323678,-7.905622,-0.757548,-3.033015,-9.188810,-2.448689,-9.611713,-7.788587,2.986278,-0.642209,-8.555074,5.824012,2.305627,8.338227,-3.572724,-4.165019,3.129224,-5.053414,5.936844,-2.359435,7.395070,2.250864,-7.521310,6.493145,3.115867,4.938690,2.351709,3.311984,-0.774348,-9.501300,-1.884861,2.128560,9.794669,6.862528,-6.998619,-5.026925,-2.717743,-1.961767,0.758435,-3.490044,5.567010,-1.688337,2.587407,-7.479936,-8.906823,-8.575503,8.181918,-6.966607,7.153567,5.939565,-5.132036,5.618657,9.869360,8.507235,-6.393912,-4.178474,7.155814,-9.977271,-4.238334,-7.673001,2.666375,8.340926,3.019243], dtype = "float32")#candidate|8650|(600,)|const|float32
call_8649 = relay.TupleGetItem(func_4016_call(relay.reshape(const_8650.astype('float32'), [8, 15, 5])), 0)
call_8651 = relay.TupleGetItem(func_4019_call(relay.reshape(const_8650.astype('float32'), [8, 15, 5])), 0)
bop_8662 = relay.bitwise_or(call_8647.astype('uint32'), call_8649.astype('uint32')) # shape=(8, 15, 5)
bop_8665 = relay.bitwise_or(call_8648.astype('uint32'), call_8651.astype('uint32')) # shape=(8, 15, 5)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
const_8679 = relay.const([7.914912,-3.710384,8.047304,8.574226,9.610431,4.336668,-5.998835,-4.562646,5.461440,2.553595,-1.988404,-8.983895,-3.462473,7.600546,3.343770,-5.031713,-3.565953,-8.140951,7.909718,0.634357,2.501048,-0.103015,2.738787,-4.702332,5.168982,-5.208708,7.622441,-1.931475,7.392733,7.916907,-2.718841,-2.857211,-9.978704,-3.645974,-1.296271,-4.018669,6.856714,5.788738,2.304283,8.565213,-2.099044,1.875430,-6.045108,3.428711,9.942335,5.258479,-1.544237,-6.947895,-1.245822,-5.263199,-1.628521,-6.278327,6.262483,-8.302039,5.912795,2.246873,-1.412570,6.105771,2.326509,-9.468006,6.260737,-5.321873,2.426489,9.357032,-5.388924,8.860717,-1.222020,-1.668053,8.054081,8.381583,-2.621360,-8.490626,6.859975,-3.677401,-9.682055,7.988053,-1.998663,0.675173,1.828602,6.087468,-7.845794,-8.370447,-7.920369,6.818588,-3.776489,-0.620691,7.536475,9.998468,4.531438,8.439299,-8.357546,0.328576,0.067501,4.229971,5.617452,-4.017160,0.157129,1.800818,2.078645,1.270413,0.344983,-6.683692,7.297751,0.978755,6.245233,-7.364993,3.341134,-0.855044,7.311788,7.687071,-3.133844,-2.982826,6.799807,9.684448,-8.795385,-0.588647,6.387637,8.059771,-5.046904,0.579428,5.252641,2.794632,6.946862,0.210773,1.133260,-5.048565,-0.605395,2.832259,-8.668270,-0.128952,-3.357271,-7.547126,-2.350754,-1.352926,-7.823598,-7.889177,7.358765,-6.784040,-1.559649,2.789212,0.471254,0.767221,7.852317,6.253625,-5.449736,-5.254037,-9.894955,-4.764854,-0.227088,9.681645,-9.501100,5.848456,1.331720,-9.118946,1.468354,-0.159863,4.841914,7.955255,-1.671955,-0.340154,-4.595099,9.500167,8.303129,1.574462,-4.408617,-3.781461,1.743207,9.307979,-6.366180,-9.922442,6.678266,-8.242328,-3.271969,6.978944,-7.646837,9.969143,3.679971,5.259696,-6.732319,-7.061082,0.862977,6.370497,-1.348780,0.950206,1.699968,4.431720,-0.864173,6.995239,0.733164,-8.061354,9.538912,-3.377659,-2.994931,8.238167,5.140835,-3.035518,0.970822,3.261928,-0.964164,-2.669644,-9.805230,-5.312311,7.804718,0.896320,8.736479,-3.727248,-7.519454,5.190610,-5.683534,3.399976,-3.310745,-9.113075,-7.024250,-4.473307,-0.828666,-2.321221,-7.205480,-9.698049,-4.128326,-4.787625,0.785781,-8.488949,0.799126,-0.589756,4.117222,8.934636,4.900525,0.710880,6.602372,-3.538754,-1.032238,-6.206717,-5.179550,-5.937776,7.376271,-0.027335,6.283281,-4.702914,-5.712549,-7.959588,-0.974007,6.494496,2.126608,2.738089,-9.229778,-6.793104,-0.931714,1.644819,9.128219,-0.626984,-5.596266,0.551054,5.373781,8.018826,5.051191,0.267599,6.598290,4.143093,2.154757,-3.010367,3.157152,-8.242917,0.568638,-0.623600,9.846623,5.570687,3.018847,6.367971,-3.934182,-7.245352,-2.815550,-8.572365,-0.728076,-2.024586,-9.505187,-4.363864,-6.330615,-7.321951,-3.277990,-7.003322,3.617211,-3.403634,4.390303,3.146971,-4.383755,6.928274,-0.858357,-6.149166,0.727848,-9.895811,6.257420,3.731705,-3.955322,-4.663726,-0.296747,-4.006948,-1.918000,-0.109981,3.540564,-6.295676,7.958236,-5.167662,3.588101,3.885994,-2.059988,-8.497072,-3.800829,7.623247,0.827784,2.192034,-5.170369,9.103854,-5.326979,-9.808529,-0.878195,8.986856,-1.034628,0.535979,9.741559,5.977750,-5.181257,6.184131,7.122564,4.175878,-7.324483,4.196484,8.860024,-4.414646,-0.151031,3.003240,5.714032,0.265399,-9.487954,3.733677,5.774020,2.498356,-3.093980,-0.946946,4.932273,9.244887,-6.987767,4.943629,7.904230,-7.642439,-5.594275,-4.489527,-6.100439,-4.815428,-1.744733,-0.045353,-6.523889,-1.414790,8.431866,-9.872956,-5.893222,-7.241902,-1.501550,-9.776691,5.494792,-4.894447,-4.218735,5.749745,-5.228473,-8.629318,3.232551,-2.236369,-0.844189,8.171775,8.156050,0.131068,6.218694,-8.031140,0.166937,4.450126,0.126206,-7.869729,6.609961,6.877382,9.801634,-9.764779,-1.202169,-1.623320,0.431163,-1.609749,-3.896710,7.160699,-3.910201,8.019968,-0.122610,-9.363865,-7.195425,-6.328733,9.862314,2.205159,6.756034,5.414548,-4.031749,-7.822731,8.940501,-0.892185,-1.516061,7.469312,-3.033395,-3.646640,-6.805588,-2.202561,-0.733495,-0.617746,-6.711454,-6.735126,6.308965,-5.715639,-9.202967,-5.925343,3.176736,3.455251,-2.214439,-3.779544,7.649322,1.520303,-7.884632,5.307994,-9.033887,-3.821404,9.603083,-1.055412,-7.328992,1.352482,-2.319180,1.012084,-8.061734,4.654936,5.729163,9.676106,9.981444,-7.586933,9.405869,-3.670421,7.588132,-4.002555,6.053564,-4.618567,9.239544,-7.363552,5.604765,-2.058514,-6.831542,-6.109612,7.489889,4.465743,-5.958280,-8.217143,7.726509,-6.181706,4.731314,0.031214,2.334305,9.870093,6.005355,-4.464247,5.373955,8.851718,0.876777,3.676276,2.606378,7.525397,2.112728,4.940088,-4.488394,6.766300,5.084067,-1.376605,-7.785174,6.333723,-0.008389,-6.094079,-1.315140,7.013231,5.649763,8.374178,8.687211,4.946979,-2.286548,2.555105,-8.494967,4.484468,-2.394565,-7.721994,2.887465,-8.933795,-2.557607,6.303626,-8.703561,-2.550773,7.959889,6.139461,-0.203225,3.753290,5.928934,5.145836,-7.137518,9.608568,-4.536322,5.035141,-0.684292,6.400150,6.617559,0.108170,-2.042193,0.403675,0.146497,-5.287597,5.161353,4.647273,1.403221,-0.411981,7.099446,-9.046115,-2.109750,7.037008,0.092015,5.819754,1.076611,8.294977,-0.280431,3.742528,7.904214,1.482340,-8.609033,1.469082,1.544125,4.805928,-4.226489,-3.234815,9.647150,6.729409,4.712507,8.640123,7.048186,-5.787953,-0.351642,-5.853759,2.079585,-7.320334,-7.994505,6.092566,-2.887074,-6.686907,-3.972659,2.641280,-9.465182,3.847722,8.746507,-5.081186,7.270255,-2.819880,-6.066606,0.310081,-6.605848,6.597859,9.655125,-0.845724,9.007597,-7.321550,4.490108,-0.771244,-6.607772,9.864086,-7.516718,5.279428,-1.873997,4.328656,-9.131564,1.526567,1.515306,1.264279,4.767023,-7.437775,-6.440433,3.629356,-1.480478,9.395336,4.015304,-0.336245,-7.301016,0.258799,8.728431,0.160699,7.096445,-3.731795,-9.307384,5.995263,0.401383,-7.786975,7.976904,1.679728,5.746485,-2.212936,-9.087560,8.640421,-9.187664,6.079970,3.459809,6.668344,8.507514,6.412208,3.056609,-7.393908,-5.420612,-8.844908,-6.265643,9.372051,-6.865873,-6.959390,-3.341532,3.162815,-8.859596,-1.343368,-9.669266,-3.997588,4.597383,3.212751,-4.450002,7.992834,-4.205114,-3.595226,-5.934126,9.899301,-6.970443,4.098261,1.925802,0.613526,0.169634,7.628449,-2.321575,-7.386597,-2.223214,-9.089633,9.943777,8.382961,-8.738649,-8.128389,-8.794680,3.641233,0.705554,9.914578,-9.715417,-5.043506,0.191272,8.718364,5.203416,2.017773,0.150342,-9.022880,-9.658868,-3.686784,-0.701763,0.308212,-3.739843,5.771855,2.837923,-7.071067,2.009816,7.794224,7.983057,-3.884587,-8.265476,-0.366441,-0.159664,-1.258998,-7.139061,5.718535,1.578621,9.745910,6.847725,9.411947,-6.809172,-4.398663,-0.886798,-7.411119,-9.415425,-7.655842,-2.989556,-7.330011,-2.891024,3.550379,-3.829244,7.000659,9.955287,5.943573,8.297480,0.522984,5.113947,4.810724,-7.171500,7.842585,3.716444,6.162702,-2.883677,-4.963795,7.346064,3.740074,-1.693910,7.197990,-9.340057,-9.864743,-9.081899,9.424589,-0.336247,5.350393,-9.305051,3.081285,3.132741,9.836182,7.597055,-5.382050,-8.738387,-2.102726,-3.193580,-9.664040,-8.230747,-6.844879,1.186768,-2.633354,-4.177384,-4.696458,-4.335326,-9.103420,-3.476191,5.889259,5.680760,-7.892821,-0.784654,-4.714592,4.918362,5.178657,-4.584783,-3.239316,8.275614,9.674997,-6.742242,-9.329177,9.070053,-6.919455,-3.212338,9.841868,4.837185,7.096940,-8.085584,-2.335384,9.305168,-9.488529,7.966588,6.454370,7.711466,5.975750,-2.422736,7.440698,-3.684203,0.777996,0.613880,8.354179,3.166868,-2.403341,-2.371192,0.774133,-9.688000,9.847225,-9.844533,-8.934357,3.816045,5.183454,3.696798,-4.407466,2.543885,4.249674,-9.012812,4.609611,7.851122,-7.251652,7.264479,7.508039,5.599022,4.096782,2.429321,2.112680,8.769348,-5.030745,5.208193,3.257426,4.873224,-6.561172,2.139943,7.081316,5.562289,-2.214680,7.782903,6.903289,9.568461,-8.197699,-1.985563,0.317602,-6.658238,1.754828,-1.553077,-2.645469,7.818424,-7.590635,9.882600,4.039167,7.372705,9.283167,-0.569143,2.350538,5.368453,-6.036418,0.750312,-2.766671,-9.391947,-4.409329,-3.646476,-6.358829,6.026073,-4.423503,-1.212583,2.802183,6.549381,-3.466976,0.566995,4.700058,5.188688,8.093483,-2.759225,-8.692451,5.461189,2.135175,-7.633742,3.188821,-4.056670,-3.918671,1.085420,-8.124844,-0.498579,-2.527615,-9.069176,-1.611939,-2.024394,8.886531,3.244236,2.346200,-8.322348,-2.988355,-0.409396,-5.205352,7.094420,3.034720,-6.071932,-2.314391,-3.756116,3.591726,-6.655765,-7.689472,9.083942,6.778103,9.541724,3.514536,-1.533447,-6.039689,5.097773,7.906048,5.111188,3.148168,2.622928,-8.537130,0.774073,-6.509690,-0.744535,-6.320165,-5.706930,-0.832027,-9.282445,6.679745,-7.237626,6.803631,-7.452439,-5.870390,1.091234,-9.715303,5.691126,-9.342176,-6.453440,8.880621,4.011776,-8.199110,3.909419,5.733308,-9.784705,-4.505014,3.117182,-4.801178,8.139376,4.334681,-5.162788,4.651558,2.137208,-7.967859,-1.707325,-5.314520,7.035120,-2.395822,9.076069,-7.174651,-2.316173,-3.329342,-8.207229,-2.366844,-3.752477,-3.268951,9.766262,-8.754001,8.809865,-0.295015,-7.224557,0.388368,5.559643,8.483761,-1.453422,-4.865244,-2.892406,-1.038398,7.047523,-3.970432,-1.211449,-6.670922,-9.117544,-3.399305,-3.658920,-9.904570,6.836697,-2.969929,8.814549,-2.089242,-5.149980,-9.568359,2.187538,9.718010,4.892299,-5.687798,6.743902,5.165698,-2.343356,8.438317,-6.952479,2.710989,-7.361881,-1.862570,3.474622,5.258405,6.349131,6.835583,-5.319236,8.006025,-2.795301,0.643520,3.036933,-0.385477,9.173527,-8.979901,5.986392,3.338074,5.478887,2.205065,-8.796740,-3.448540,-3.319658,8.987388,0.237913,1.428538,-7.115688,6.278436,9.803624,5.897131,5.513682,1.010392,-3.432647,-0.674664,-0.108232,-1.929174,-0.329019,9.583787,-3.274186,2.852775,4.134906,-5.152977,-0.230367,7.933474,8.600493,-5.566326,-3.441382,8.043495,-0.663631,3.144728,0.041082,-0.587995,-9.151321,-1.029931,-4.355724,-8.402698,-1.459314,2.296972,-1.118582,1.871880,-9.738128,6.132862,8.715285,1.182529,-2.610745,-7.901702,-7.858463,-9.410114,-8.492178,-3.767741,-3.457775,9.632037,4.417398,8.891609,0.559718,9.758620,-5.330077,4.389436,1.749204,-5.283249,0.605654,0.531073,3.167248,-5.938883,-6.468185,-9.345897,-3.219523,-5.638261,-2.809694,6.535921,-5.795456,8.443331,1.414909,-0.592342,1.855953,4.168585,7.305351,3.100731,-9.057081,8.177984,-0.945833,7.648853,1.872744,-7.762967,-1.334125,0.990758,-5.991710,8.048332,5.115004,-0.933897,-7.692506,6.028492,-5.971053,-9.434281,3.816444,9.861253,7.105907,-3.066917,-7.238974,8.871440,-4.777270,6.037511,8.714882,8.175162,-1.796147,-7.163819,2.005032,9.401439,-5.333440,-8.372386,8.178604,2.677533,-5.026541,1.030535,-6.038296,8.549743,4.850042,6.343212,-9.215719,-1.022914,-0.043395,6.810459,-0.308967,1.444093,6.961637,-6.872423,1.806068,8.723286,5.197708,5.845063,1.737899,6.561444,7.235741,-3.658283,4.157709,5.296602,8.276174,8.390355,3.964475,-1.791630,-7.982033,7.913274,-7.355592,2.491097,7.105364,3.310990,-7.074915,1.433787,3.790583,8.851182,-0.670150,-0.762852,3.932725,-7.773775,-5.291860,9.848529,8.055260,-5.049783,-7.704279,-1.281699,-4.995208,-0.098813,-7.922828,2.893066,0.801665,-5.761690,7.211909,5.706582,-2.430327,9.320580,-8.840322,6.281151,7.320258,5.713579,4.320200,1.927161,0.673721,-3.893509,5.674965,3.529577,-9.874924,4.485896,-6.508406,4.662826,-8.840204,4.150992,6.781454,-4.865270,1.104894,-0.618051,1.335745,-8.784710,-9.470932,-1.271851,-1.739081,-1.399955,6.343377,-0.416895,0.697528,-9.038859,-1.696048,-7.974573,-5.203384,-9.114472,7.392153,2.841404,-5.171027,4.219126,-5.661614,5.436725,-7.388872,-6.369026,2.144304,4.884926,-1.098037,-8.125697,-3.141390,-2.175235,2.847136,-1.278599,-1.813964,-0.874182,8.994245,5.993605,3.505429,4.820453,-8.424492,-6.668490,-2.575098,-3.670579,4.089184,-7.987440,-7.310318,3.553264,6.969213,-7.948477,9.938955,8.581824,-1.921446,-8.587141,4.787052,7.789141,7.800686,1.827557,-0.491478,-9.182891,-4.964507,1.588395,-0.029361,-1.973737,-4.036779,3.466927,9.871384,-1.537413,2.402009,-6.452966,-8.906503,-3.884309,9.705828,-6.515595,-3.103635,8.552648,1.619190,6.538326,4.066557,3.197285,-1.504544,8.000317,3.251261,5.488789,6.768269,1.415424,-9.159984,2.374725,4.419696,4.590448,3.583191,-5.876413,4.630071,-8.160307,-6.197284,-5.091874,-1.890293,-8.449080,4.335758,-1.082539,1.331228,4.740196,1.129383,7.530922,-2.245820,-0.407027,-4.282451,-7.345407,-8.862750,-4.768563,-1.036365,8.210819,3.427422,1.287027,-6.300609,2.800743,6.581444,7.019276,2.469285,-1.489516,2.033560,4.376756,0.686553,3.088966,-7.087646,-1.708746,-4.677597,9.243388,-6.768134,-9.988030,-3.845607,-1.456476,-9.239123,2.835695,9.547149,3.824731,-9.329884,-3.193963,-3.299363,-5.990827,6.129478,-6.213223,-5.552231,4.471992,-1.408919,0.365311,5.623866,-6.629344,4.334613,-7.238746,1.138254,4.284802,-9.988670,-0.633052,9.223021,-6.918912,4.372007,-4.486295,-3.501910,-7.783515,-5.400625,-5.123014,-4.033314,5.356872,-8.709311,-3.583267,-6.675930,2.370812,5.748202,5.388270,-3.804192,5.737037,-9.275424,-5.040294,-0.350958,9.416199,-0.116222,-2.232692,5.281030,8.410153,8.272721,0.897795,2.956048,8.154092,-4.234899,-9.788013,-4.746290,8.568401,7.526652,9.182475,-3.789230,-2.376310,-8.313279,5.778057,4.350485,4.238273,-1.748479,-0.974664,-8.555950,-4.290909,-3.174596,5.285786,1.574484,-9.592069,-8.759831,-5.436029,-8.415913,-3.806706,3.480608,-7.318510,-0.396867,-7.373645,7.519771,-1.332891,-0.989321,-5.739404,3.648772,9.078397,-4.872446,-9.743800,3.513927,-5.776942,8.786537,8.813467,-0.625566,9.023420,8.638398,-5.413518,-6.161721,-8.949176,7.257024,-6.112734,1.265338,5.709396,0.488285,-4.791845,-8.989171,-6.578591,9.432779,8.807095,-1.143000,-9.049512,-2.449952,-5.308622,-7.706354,2.536501,6.565027,-0.121739,3.738463,1.041735,4.234325,0.227096,-9.289760,-3.903374,1.203258,8.622844,-1.629355,-1.482986,-0.025261,-5.375902,9.650929,7.497296,4.887160,9.823782,3.330318,2.324556,0.941400,2.440300,-3.607614,7.312791,5.414015,6.316923,9.867789,-3.674350,-3.734688,-3.568301,-7.851914,0.208634,5.069988,-6.218804,3.245255,-7.369097,-7.510294,-1.923184,5.352890,4.700334,-9.070064,-4.847564,-5.842350,-7.510842,8.805849,-0.782080,-9.676064,2.018366,2.220570,-0.521292,2.478728,7.367910,-2.778561,1.237218,1.891594,-6.756967,0.270803,7.934912,9.418383,7.012760,-0.369137,-2.362732,4.669567,9.406520,0.325170,3.294521,-2.779224,6.272147,-7.704040,-5.889482,1.779725,3.923649,1.516545,-6.294352,-0.118732,-6.432991,5.992135,1.259988,-2.130515,6.756134,3.913382,8.357351,7.769540,-9.457093,8.966909,-6.072019,-5.215084,8.787292,-3.945425,-8.493571,8.865260,-5.011943,-8.274092,2.504948,-7.776565,-9.083949,0.051984,2.852464,-2.869786,-9.073872,-6.723980,-2.620470,3.694963,-1.661746,7.241476,-2.563270,5.112068,-8.694376,6.767089,2.483339,-2.343208,1.416033,0.452348,8.860199,-4.561374,1.912527,-9.190911,3.493149,2.147963,0.065830,7.750056,-5.655827,-3.890762,-4.978044,-0.604423,1.893407,5.260080,0.848218,2.997721,1.673688,-2.632899,-8.669075,-7.730682,-9.213337,-6.798144,2.182144,-3.218439,-3.053052,-0.844898,-7.957781,-5.095946,9.478549,-4.359889,-0.527608,4.266317,2.804671,-2.233745,-8.632105,-4.015210,5.964473,2.651329,-8.270961,-0.560864,-0.786511,9.036082,8.084480,3.084422,7.467570,4.577301,2.764830,9.313167,7.516406,0.856949,7.711294,-6.936315,-4.054506,2.631741,9.951197,3.615242,-0.489128,-3.971743,0.333538,-3.618296,1.717122,-2.495487,2.364108,-6.783479,-0.029786,-9.050715,3.661847,-4.330292,-8.913313,-7.484235,3.086489,-1.658041,-7.683690,9.574721,-3.102537,-4.930718,-6.299554,-6.030718,7.367963,-3.235047,-1.341322,0.177314,9.315248,2.941673,1.650352,-8.919018,-2.514623,-9.488295,3.996945,-2.757889,4.421297,-0.325919,7.313584,2.769304,0.879631,-8.775256,7.295432,2.541930,5.543661,-5.659137,-9.308228,4.219554,4.309144,9.023325,-2.959076,-6.691694,-7.130321,4.969260,-9.860378,-9.322025,-4.631764,3.488792,-4.172839,-6.893039,-2.924842,-2.348019,5.030272,3.642909,3.543775,-1.521512,-7.507911,-5.278500,1.741176,-0.500199,-4.314411,4.119923,-2.665995,-6.229573,4.734203,-8.248784,-1.918137,-9.931033,2.293151,-9.140149,-7.097544,-8.731179,-9.464045,0.488721,-8.366600,4.311708,9.603030,7.390350,6.458934,-0.817978,-8.102391,-5.593101,-6.143258,4.887236,-8.841302,-0.232204,-1.957723,6.535760,3.728902,-3.264662,5.009554,0.757192,-7.469510,-8.349168,-3.724054,-6.595998,0.817135,2.595436,8.398060,5.261978,1.227337,-9.511207,-9.459800,-9.020517,-0.581825,2.910039,-5.212506,-4.739402,3.207546,-0.071264,-9.036324,3.652309,-0.699891,8.258284,3.923552,6.189310,-6.268760,-1.019930,-6.373009,6.585895,5.860546,-0.862961,9.427285,-3.463605,9.613098,-2.077729,4.378044,8.333675,6.163157,9.663192,-2.601603,7.369649,-6.248175,2.769089,-4.858259,2.558096,-5.442220,9.684154,3.896596,-7.251886,-5.928040,-4.633890,-0.258519,5.692914,-6.307962,-5.493927,-0.348008,4.393646,2.448871,2.408186,5.482838,5.694810,-9.434421,3.351523,-6.454497,-6.357353,9.903036,-4.359448,-6.535788,6.702857,-7.972111,9.854353,6.727181,5.591092,-6.175546,-6.422145,-9.878963,4.897722,-5.815754,-2.861447,-5.120969,9.390820,1.536672,-2.828192,-2.432516,-8.510905,5.869523,5.744032,-1.128013,-1.654570,4.688515,8.489593,-2.052501,-7.440043,0.535091,-5.073424,7.943661,0.103646,9.607579,-4.811751,7.404113,9.176949,5.496148,4.380006,0.275811,-8.868166,-8.018020,-8.782213,-3.799621,3.305504,6.739697,5.312681,-1.434747,9.066249,-5.447311,3.443982,-1.534957,5.073420,4.072600,-5.972921,-7.504789,1.267649,-3.037408,4.086152,-6.193216,-0.678151,-6.237875,-8.649258,1.511887,3.706655,6.670220,0.040154,6.271930,4.615883,-2.120640,8.591421,-1.255774,5.984061,4.350749,8.084276,-7.973642,2.475563,-6.318865,0.031545,-6.899959,0.623146,6.585463,0.247822,4.504785,5.054290,-7.972757,-4.865518,9.890699,5.563373,1.311376,-0.559176,7.692636,-9.814396,1.633170,8.808629,-2.103984,0.884923,2.289318,-9.675817,-1.328888,-5.626283,9.782864,6.052667,4.317191,6.708887,-8.355280,-1.553959,9.049872,2.018600,-1.693094,-7.562940,3.246146,-3.862764,5.738358,-6.215842,-2.153454,-8.859558,1.496490,-3.142651,2.240619,9.602863,3.443120,4.127023,2.324775,8.078016,8.044508,-9.084077,7.068050,2.057361,-0.663927,-8.259623,1.897162,-5.812822,4.538389,2.522676,-4.543079,-8.623147,-9.814743,-8.129230,-1.670257,6.417283,-2.080417,-2.184742,-4.104578,-8.311222,4.639547,0.267600,1.447993,-1.915838,-9.472057,4.939573,-2.015654,-8.542030,9.812822,-2.114693,-6.480148,0.640634,-3.714388,-1.996300,-1.152642,8.269030,-2.326878,-4.024031,-0.110312,-8.744603,-8.953656,9.751586,2.608260,0.916523,-8.118721,-4.855904,6.830440,2.176321,7.735009,-7.407791,-9.834939,-9.351356,-0.832631,3.565815,6.266941,2.391004,0.472095,-0.219500,-7.481588,-4.326542,-0.006420,0.888108,-5.816434,9.415713,-3.343171,4.510523,6.662539,3.704917,-2.455250,-8.884809,-6.585184,2.862217,-7.077675,-9.468588,4.502045,9.236705,4.797013,1.219843,-8.176402,-5.105216,-2.531500,1.937237,9.903698,6.492736,4.776368,7.963637,8.632091,-7.678341,-6.380790,-4.177712,7.869196,5.979071,-0.555100,-3.679989,6.563232,-5.300234,2.778940,5.605700,-6.234779,-9.051477,-2.329912,-6.999164,4.073760,6.682937,2.358602,3.786734,-5.511655,-3.396257,-3.247287,1.799500,7.461187,0.534725,2.860773,1.721730,-6.997959,-6.690323,5.400551,-5.669455,0.345983,-1.634870,-4.143574,8.179530,6.176027,1.777087,-7.113935,4.462703,-9.296638,-9.129430,-2.518835,-3.188604,-6.542355,6.839359,1.115435,-5.522743,-3.960969,2.500293,-1.512471,3.752273,-0.064876,2.155907,0.286423,-8.422206,-5.362689,0.075021,-9.068212,8.817432,-3.550558,-1.015578,-9.231578,-9.074120,-5.778285,4.027524,-8.511661,-6.051048,-7.134444], dtype = "float64")#candidate|8679|(2016,)|const|float64
call_8678 = relay.TupleGetItem(func_3508_call(relay.reshape(const_8679.astype('float64'), [16, 9, 14])), 0)
call_8680 = relay.TupleGetItem(func_3510_call(relay.reshape(const_8679.astype('float64'), [16, 9, 14])), 0)
output = relay.Tuple([const_8650,bop_8662,call_8678,const_8679,])
output2 = relay.Tuple([const_8650,bop_8665,call_8680,const_8679,])
func_8684 = relay.Function([], output)
mod['func_8684'] = func_8684
mod = relay.transform.InferType()(mod)
output = func_8684()
func_8685 = relay.Function([], output)
mutated_mod['func_8685'] = func_8685
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8762 = relay.const([[[9.588759,-7.779022,-5.464025,7.216273,-3.822890,-2.197574,-3.386668,6.730516,-6.470972,-6.944340,-0.868289,-6.486361,9.443785,5.223523],[-9.296219,-2.985266,8.024641,-6.442662,-6.018753,3.820750,-2.498354,5.467665,-7.172254,6.232211,-5.233802,7.096934,-2.463263,-7.770481],[6.532217,0.458815,-7.927204,5.194934,-2.891362,9.265299,-7.326861,-9.695701,-8.160984,0.278021,-0.354741,1.401280,-0.340151,3.411563],[-1.026863,-5.802096,-5.386713,1.464420,7.266313,-3.732667,-2.706545,-1.165535,-5.060358,0.758661,2.921311,3.539081,4.841054,-3.535902],[-7.264481,-7.267389,-3.919534,-0.304410,-6.671483,0.079046,2.788023,-9.065950,-3.133740,-9.224880,3.451084,2.450028,-0.900164,-3.158290],[-3.710552,5.722790,3.370192,2.917711,0.187280,-0.352666,-6.957090,1.279346,8.101335,0.658231,8.754492,4.591544,-4.922581,7.411239],[3.407562,-8.958038,-7.397797,-2.651582,-3.418317,6.495079,-3.496174,3.728144,-1.427533,-8.035766,-3.802773,3.411754,7.435459,-0.689245],[7.107362,-4.518290,-0.514338,-4.255071,-2.697212,-5.121309,8.323377,-0.717843,2.770300,-3.778956,0.733983,7.353504,-1.051075,5.796130],[8.811685,6.336509,5.065324,-0.443541,4.450704,-8.664825,2.901844,-5.038246,4.911473,-6.183552,-6.663097,-9.679495,5.741141,-2.659504],[-6.029239,1.982214,4.450879,-4.082276,-1.910586,-0.647978,-4.304164,-1.419134,3.904030,-2.987208,6.305703,8.847442,9.051546,3.795502],[-9.554390,-8.844674,2.059374,-9.313181,3.422134,0.889258,4.232930,6.141169,0.175063,-2.415830,-1.597175,2.102812,0.274284,0.436349],[-9.272729,-0.662633,-3.229522,4.885029,-7.784353,2.862912,-3.289594,-7.427312,-5.973020,4.174186,3.868459,0.270175,-9.933466,6.488211],[3.172293,-5.313105,-2.416614,-4.311199,-5.971100,-0.848326,-4.314052,-2.477869,7.413392,-4.030728,-6.693451,0.918624,4.955167,1.952828],[4.959707,-4.944406,8.927102,-5.146692,8.781929,8.896287,-5.606629,-9.151046,3.218160,4.579581,9.430734,-7.582302,-0.691064,6.046593],[-1.474905,1.225289,-6.364519,3.754117,0.210470,8.620663,-6.738761,-4.641752,-9.816614,5.796872,9.271946,-9.850506,8.192092,-9.474370]]], dtype = "float32")#candidate|8762|(1, 15, 14)|const|float32
uop_8763 = relay.rsqrt(const_8762.astype('float32')) # shape=(1, 15, 14)
output = relay.Tuple([uop_8763,])
output2 = relay.Tuple([uop_8763,])
func_8766 = relay.Function([], output)
mod['func_8766'] = func_8766
mod = relay.transform.InferType()(mod)
output = func_8766()
func_8767 = relay.Function([], output)
mutated_mod['func_8767'] = func_8767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7674_call = mod.get_global_var('func_7674')
func_7675_call = mutated_mod.get_global_var('func_7675')
call_8771 = relay.TupleGetItem(func_7674_call(), 0)
call_8772 = relay.TupleGetItem(func_7675_call(), 0)
output = call_8771
output2 = call_8772
func_8797 = relay.Function([], output)
mod['func_8797'] = func_8797
mod = relay.transform.InferType()(mod)
output = func_8797()
func_8798 = relay.Function([], output)
mutated_mod['func_8798'] = func_8798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6120_call = mod.get_global_var('func_6120')
func_6122_call = mutated_mod.get_global_var('func_6122')
call_8825 = relay.TupleGetItem(func_6120_call(), 1)
call_8826 = relay.TupleGetItem(func_6122_call(), 1)
output = relay.Tuple([call_8825,])
output2 = relay.Tuple([call_8826,])
func_8827 = relay.Function([], output)
mod['func_8827'] = func_8827
mod = relay.transform.InferType()(mod)
mutated_mod['func_8827'] = func_8827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8827_call = mutated_mod.get_global_var('func_8827')
call_8828 = func_8827_call()
output = call_8828
func_8829 = relay.Function([], output)
mutated_mod['func_8829'] = func_8829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6990_call = mod.get_global_var('func_6990')
func_6992_call = mutated_mod.get_global_var('func_6992')
call_8882 = func_6990_call()
call_8883 = func_6990_call()
func_6990_call = mod.get_global_var('func_6990')
func_6992_call = mutated_mod.get_global_var('func_6992')
call_8887 = func_6990_call()
call_8888 = func_6990_call()
output = relay.Tuple([call_8882,call_8887,])
output2 = relay.Tuple([call_8883,call_8888,])
func_8893 = relay.Function([], output)
mod['func_8893'] = func_8893
mod = relay.transform.InferType()(mod)
mutated_mod['func_8893'] = func_8893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8893_call = mutated_mod.get_global_var('func_8893')
call_8894 = func_8893_call()
output = call_8894
func_8895 = relay.Function([], output)
mutated_mod['func_8895'] = func_8895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6120_call = mod.get_global_var('func_6120')
func_6122_call = mutated_mod.get_global_var('func_6122')
call_8916 = relay.TupleGetItem(func_6120_call(), 1)
call_8917 = relay.TupleGetItem(func_6122_call(), 1)
output = call_8916
output2 = call_8917
func_8939 = relay.Function([], output)
mod['func_8939'] = func_8939
mod = relay.transform.InferType()(mod)
mutated_mod['func_8939'] = func_8939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8939_call = mutated_mod.get_global_var('func_8939')
call_8940 = func_8939_call()
output = call_8940
func_8941 = relay.Function([], output)
mutated_mod['func_8941'] = func_8941
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8942 = relay.var("var_8942", dtype = "float64", shape = (3, 6, 15))#candidate|8942|(3, 6, 15)|var|float64
uop_8943 = relay.sqrt(var_8942.astype('float64')) # shape=(3, 6, 15)
func_2964_call = mod.get_global_var('func_2964')
func_2965_call = mutated_mod.get_global_var('func_2965')
call_8949 = func_2964_call()
call_8950 = func_2964_call()
output = relay.Tuple([uop_8943,call_8949,])
output2 = relay.Tuple([uop_8943,call_8950,])
func_8960 = relay.Function([var_8942,], output)
mod['func_8960'] = func_8960
mod = relay.transform.InferType()(mod)
mutated_mod['func_8960'] = func_8960
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8961 = relay.var("var_8961", dtype = "float64", shape = (3, 6, 15))#candidate|8961|(3, 6, 15)|var|float64
func_8960_call = mutated_mod.get_global_var('func_8960')
call_8962 = func_8960_call(var_8961)
output = call_8962
func_8963 = relay.Function([var_8961], output)
mutated_mod['func_8963'] = func_8963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6120_call = mod.get_global_var('func_6120')
func_6122_call = mutated_mod.get_global_var('func_6122')
call_8981 = relay.TupleGetItem(func_6120_call(), 1)
call_8982 = relay.TupleGetItem(func_6122_call(), 1)
output = call_8981
output2 = call_8982
func_8986 = relay.Function([], output)
mod['func_8986'] = func_8986
mod = relay.transform.InferType()(mod)
mutated_mod['func_8986'] = func_8986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8986_call = mutated_mod.get_global_var('func_8986')
call_8987 = func_8986_call()
output = call_8987
func_8988 = relay.Function([], output)
mutated_mod['func_8988'] = func_8988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3298_call = mod.get_global_var('func_3298')
func_3299_call = mutated_mod.get_global_var('func_3299')
call_8994 = relay.TupleGetItem(func_3298_call(), 1)
call_8995 = relay.TupleGetItem(func_3299_call(), 1)
output = relay.Tuple([call_8994,])
output2 = relay.Tuple([call_8995,])
func_9008 = relay.Function([], output)
mod['func_9008'] = func_9008
mod = relay.transform.InferType()(mod)
mutated_mod['func_9008'] = func_9008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9008_call = mutated_mod.get_global_var('func_9008')
call_9009 = func_9008_call()
output = call_9009
func_9010 = relay.Function([], output)
mutated_mod['func_9010'] = func_9010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4778_call = mod.get_global_var('func_4778')
func_4779_call = mutated_mod.get_global_var('func_4779')
call_9033 = func_4778_call()
call_9034 = func_4778_call()
var_9054 = relay.var("var_9054", dtype = "float32", shape = (8, 13, 5))#candidate|9054|(8, 13, 5)|var|float32
bop_9055 = relay.logical_xor(call_9033.astype('int32'), var_9054.astype('int32')) # shape=(8, 13, 5)
bop_9058 = relay.logical_xor(call_9034.astype('int32'), var_9054.astype('int32')) # shape=(8, 13, 5)
bop_9059 = relay.not_equal(call_9033.astype('bool'), bop_9055.astype('bool')) # shape=(8, 13, 5)
bop_9062 = relay.not_equal(call_9034.astype('bool'), bop_9058.astype('bool')) # shape=(8, 13, 5)
func_7065_call = mod.get_global_var('func_7065')
func_7067_call = mutated_mod.get_global_var('func_7067')
call_9064 = relay.TupleGetItem(func_7065_call(), 0)
call_9065 = relay.TupleGetItem(func_7067_call(), 0)
func_6661_call = mod.get_global_var('func_6661')
func_6663_call = mutated_mod.get_global_var('func_6663')
call_9069 = relay.TupleGetItem(func_6661_call(), 0)
call_9070 = relay.TupleGetItem(func_6663_call(), 0)
output = relay.Tuple([bop_9059,call_9064,call_9069,])
output2 = relay.Tuple([bop_9062,call_9065,call_9070,])
func_9076 = relay.Function([var_9054,], output)
mod['func_9076'] = func_9076
mod = relay.transform.InferType()(mod)
mutated_mod['func_9076'] = func_9076
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9077 = relay.var("var_9077", dtype = "float32", shape = (8, 13, 5))#candidate|9077|(8, 13, 5)|var|float32
func_9076_call = mutated_mod.get_global_var('func_9076')
call_9078 = func_9076_call(var_9077)
output = call_9078
func_9079 = relay.Function([var_9077], output)
mutated_mod['func_9079'] = func_9079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6809_call = mod.get_global_var('func_6809')
func_6810_call = mutated_mod.get_global_var('func_6810')
call_9111 = func_6809_call()
call_9112 = func_6809_call()
var_9121 = relay.var("var_9121", dtype = "float32", shape = (8, 16, 5))#candidate|9121|(8, 16, 5)|var|float32
bop_9122 = relay.minimum(call_9111.astype('uint16'), var_9121.astype('uint16')) # shape=(8, 16, 5)
bop_9125 = relay.minimum(call_9112.astype('uint16'), var_9121.astype('uint16')) # shape=(8, 16, 5)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_9131 = func_2513_call()
call_9132 = func_2513_call()
bop_9142 = relay.bitwise_xor(var_9121.astype('uint64'), call_9131.astype('uint64')) # shape=(8, 16, 5)
bop_9145 = relay.bitwise_xor(var_9121.astype('uint64'), call_9132.astype('uint64')) # shape=(8, 16, 5)
uop_9155 = relay.cosh(bop_9122.astype('float64')) # shape=(8, 16, 5)
uop_9157 = relay.cosh(bop_9125.astype('float64')) # shape=(8, 16, 5)
output = relay.Tuple([bop_9142,uop_9155,])
output2 = relay.Tuple([bop_9145,uop_9157,])
func_9168 = relay.Function([var_9121,], output)
mod['func_9168'] = func_9168
mod = relay.transform.InferType()(mod)
var_9169 = relay.var("var_9169", dtype = "float32", shape = (8, 16, 5))#candidate|9169|(8, 16, 5)|var|float32
output = func_9168(var_9169)
func_9170 = relay.Function([var_9169], output)
mutated_mod['func_9170'] = func_9170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8797_call = mod.get_global_var('func_8797')
func_8798_call = mutated_mod.get_global_var('func_8798')
call_9206 = func_8797_call()
call_9207 = func_8797_call()
var_9213 = relay.var("var_9213", dtype = "float64", shape = (8, 2, 5))#candidate|9213|(8, 2, 5)|var|float64
bop_9214 = relay.bitwise_or(call_9206.astype('int64'), var_9213.astype('int64')) # shape=(8, 2, 5)
bop_9217 = relay.bitwise_or(call_9207.astype('int64'), var_9213.astype('int64')) # shape=(8, 2, 5)
output = relay.Tuple([bop_9214,])
output2 = relay.Tuple([bop_9217,])
func_9232 = relay.Function([var_9213,], output)
mod['func_9232'] = func_9232
mod = relay.transform.InferType()(mod)
mutated_mod['func_9232'] = func_9232
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9233 = relay.var("var_9233", dtype = "float64", shape = (8, 2, 5))#candidate|9233|(8, 2, 5)|var|float64
func_9232_call = mutated_mod.get_global_var('func_9232')
call_9234 = func_9232_call(var_9233)
output = call_9234
func_9235 = relay.Function([var_9233], output)
mutated_mod['func_9235'] = func_9235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4271_call = mod.get_global_var('func_4271')
func_4272_call = mutated_mod.get_global_var('func_4272')
call_9242 = relay.TupleGetItem(func_4271_call(), 1)
call_9243 = relay.TupleGetItem(func_4272_call(), 1)
output = relay.Tuple([call_9242,])
output2 = relay.Tuple([call_9243,])
func_9270 = relay.Function([], output)
mod['func_9270'] = func_9270
mod = relay.transform.InferType()(mod)
output = func_9270()
func_9271 = relay.Function([], output)
mutated_mod['func_9271'] = func_9271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4856_call = mod.get_global_var('func_4856')
func_4858_call = mutated_mod.get_global_var('func_4858')
call_9305 = func_4856_call()
call_9306 = func_4856_call()
output = relay.Tuple([call_9305,])
output2 = relay.Tuple([call_9306,])
func_9309 = relay.Function([], output)
mod['func_9309'] = func_9309
mod = relay.transform.InferType()(mod)
output = func_9309()
func_9310 = relay.Function([], output)
mutated_mod['func_9310'] = func_9310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_9323 = relay.TupleGetItem(func_2813_call(), 3)
call_9324 = relay.TupleGetItem(func_2814_call(), 3)
func_5274_call = mod.get_global_var('func_5274')
func_5276_call = mutated_mod.get_global_var('func_5276')
call_9332 = relay.TupleGetItem(func_5274_call(), 0)
call_9333 = relay.TupleGetItem(func_5276_call(), 0)
output = relay.Tuple([call_9323,call_9332,])
output2 = relay.Tuple([call_9324,call_9333,])
func_9353 = relay.Function([], output)
mod['func_9353'] = func_9353
mod = relay.transform.InferType()(mod)
output = func_9353()
func_9354 = relay.Function([], output)
mutated_mod['func_9354'] = func_9354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8939_call = mod.get_global_var('func_8939')
func_8941_call = mutated_mod.get_global_var('func_8941')
call_9373 = func_8939_call()
call_9374 = func_8939_call()
func_8827_call = mod.get_global_var('func_8827')
func_8829_call = mutated_mod.get_global_var('func_8829')
call_9383 = relay.TupleGetItem(func_8827_call(), 0)
call_9384 = relay.TupleGetItem(func_8829_call(), 0)
func_3405_call = mod.get_global_var('func_3405')
func_3406_call = mutated_mod.get_global_var('func_3406')
call_9388 = func_3405_call()
call_9389 = func_3405_call()
output = relay.Tuple([call_9373,call_9383,call_9388,])
output2 = relay.Tuple([call_9374,call_9384,call_9389,])
func_9392 = relay.Function([], output)
mod['func_9392'] = func_9392
mod = relay.transform.InferType()(mod)
mutated_mod['func_9392'] = func_9392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9392_call = mutated_mod.get_global_var('func_9392')
call_9393 = func_9392_call()
output = call_9393
func_9394 = relay.Function([], output)
mutated_mod['func_9394'] = func_9394
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9458 = relay.const([[[-3,-3,9]],[[-2,8,-9]],[[8,10,-8]],[[4,-3,-8]],[[-6,-1,10]],[[-2,-4,-3]],[[4,-2,-7]],[[-9,2,7]],[[-10,3,-3]],[[-10,-8,7]],[[-4,3,5]],[[5,-1,10]],[[-5,-5,8]],[[-4,-4,-4]],[[7,-7,6]]], dtype = "int64")#candidate|9458|(15, 1, 3)|const|int64
var_9459 = relay.var("var_9459", dtype = "int64", shape = (15, 7, 3))#candidate|9459|(15, 7, 3)|var|int64
bop_9460 = relay.minimum(const_9458.astype('int64'), var_9459.astype('int64')) # shape=(15, 7, 3)
output = relay.Tuple([bop_9460,])
output2 = relay.Tuple([bop_9460,])
func_9466 = relay.Function([var_9459,], output)
mod['func_9466'] = func_9466
mod = relay.transform.InferType()(mod)
var_9467 = relay.var("var_9467", dtype = "int64", shape = (15, 7, 3))#candidate|9467|(15, 7, 3)|var|int64
output = func_9466(var_9467)
func_9468 = relay.Function([var_9467], output)
mutated_mod['func_9468'] = func_9468
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9498 = relay.var("var_9498", dtype = "float64", shape = (9, 8, 14))#candidate|9498|(9, 8, 14)|var|float64
uop_9499 = relay.erf(var_9498.astype('float64')) # shape=(9, 8, 14)
bop_9502 = relay.logical_and(uop_9499.astype('bool'), relay.reshape(var_9498.astype('bool'), relay.shape_of(uop_9499))) # shape=(9, 8, 14)
output = bop_9502
output2 = bop_9502
func_9507 = relay.Function([var_9498,], output)
mod['func_9507'] = func_9507
mod = relay.transform.InferType()(mod)
var_9508 = relay.var("var_9508", dtype = "float64", shape = (9, 8, 14))#candidate|9508|(9, 8, 14)|var|float64
output = func_9507(var_9508)
func_9509 = relay.Function([var_9508], output)
mutated_mod['func_9509'] = func_9509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7722_call = mod.get_global_var('func_7722')
func_7723_call = mutated_mod.get_global_var('func_7723')
call_9540 = relay.TupleGetItem(func_7722_call(), 0)
call_9541 = relay.TupleGetItem(func_7723_call(), 0)
output = call_9540
output2 = call_9541
func_9546 = relay.Function([], output)
mod['func_9546'] = func_9546
mod = relay.transform.InferType()(mod)
output = func_9546()
func_9547 = relay.Function([], output)
mutated_mod['func_9547'] = func_9547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6304_call = mod.get_global_var('func_6304')
func_6305_call = mutated_mod.get_global_var('func_6305')
call_9567 = relay.TupleGetItem(func_6304_call(), 0)
call_9568 = relay.TupleGetItem(func_6305_call(), 0)
func_7674_call = mod.get_global_var('func_7674')
func_7675_call = mutated_mod.get_global_var('func_7675')
call_9574 = relay.TupleGetItem(func_7674_call(), 0)
call_9575 = relay.TupleGetItem(func_7675_call(), 0)
output = relay.Tuple([call_9567,call_9574,])
output2 = relay.Tuple([call_9568,call_9575,])
func_9594 = relay.Function([], output)
mod['func_9594'] = func_9594
mod = relay.transform.InferType()(mod)
mutated_mod['func_9594'] = func_9594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9594_call = mutated_mod.get_global_var('func_9594')
call_9595 = func_9594_call()
output = call_9595
func_9596 = relay.Function([], output)
mutated_mod['func_9596'] = func_9596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mod.get_global_var('func_4280')
func_4281_call = mutated_mod.get_global_var('func_4281')
call_9612 = func_4280_call()
call_9613 = func_4280_call()
func_5506_call = mod.get_global_var('func_5506')
func_5508_call = mutated_mod.get_global_var('func_5508')
call_9642 = relay.TupleGetItem(func_5506_call(), 0)
call_9643 = relay.TupleGetItem(func_5508_call(), 0)
output = relay.Tuple([call_9612,call_9642,])
output2 = relay.Tuple([call_9613,call_9643,])
func_9649 = relay.Function([], output)
mod['func_9649'] = func_9649
mod = relay.transform.InferType()(mod)
mutated_mod['func_9649'] = func_9649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9649_call = mutated_mod.get_global_var('func_9649')
call_9650 = func_9649_call()
output = call_9650
func_9651 = relay.Function([], output)
mutated_mod['func_9651'] = func_9651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7722_call = mod.get_global_var('func_7722')
func_7723_call = mutated_mod.get_global_var('func_7723')
call_9657 = relay.TupleGetItem(func_7722_call(), 0)
call_9658 = relay.TupleGetItem(func_7723_call(), 0)
func_9466_call = mod.get_global_var('func_9466')
func_9468_call = mutated_mod.get_global_var('func_9468')
var_9669 = relay.var("var_9669", dtype = "int64", shape = (315,))#candidate|9669|(315,)|var|int64
call_9668 = relay.TupleGetItem(func_9466_call(relay.reshape(var_9669.astype('int64'), [15, 7, 3])), 0)
call_9670 = relay.TupleGetItem(func_9468_call(relay.reshape(var_9669.astype('int64'), [15, 7, 3])), 0)
func_9232_call = mod.get_global_var('func_9232')
func_9235_call = mutated_mod.get_global_var('func_9235')
const_9703 = relay.const([2.965735,-5.899894,-0.081509,-6.567517,-1.869075,-4.347345,-0.737182,-9.568224,-9.059529,8.110328,6.433444,-6.700631,9.358360,-7.158491,0.174569,-0.253188,1.294165,-5.823497,-6.638799,8.787028,-8.515651,6.484004,-4.847668,8.954997,-4.591062,1.188308,6.357955,-4.835681,4.166994,-8.700731,8.055212,0.723309,0.168719,-3.236370,4.637778,9.812969,-1.882755,-8.457344,-9.613359,0.187406,-5.431282,5.937789,-7.893411,3.240396,-1.266170,-9.980836,-0.703463,-1.601592,1.664781,8.230499,-3.858298,-1.046016,1.731985,7.965615,9.163607,-2.704418,6.347900,1.944176,6.171809,8.854328,-8.133095,-1.133074,1.178688,5.732502,8.492162,0.192962,5.269468,-1.393907,6.574132,-7.702416,-4.586156,-4.231075,-4.461000,4.516614,-1.059468,9.626068,4.511622,6.381367,-2.356195,5.013596], dtype = "float64")#candidate|9703|(80,)|const|float64
call_9702 = relay.TupleGetItem(func_9232_call(relay.reshape(const_9703.astype('float64'), [8, 2, 5])), 0)
call_9704 = relay.TupleGetItem(func_9235_call(relay.reshape(const_9703.astype('float64'), [8, 2, 5])), 0)
output = relay.Tuple([call_9657,call_9668,var_9669,call_9702,const_9703,])
output2 = relay.Tuple([call_9658,call_9670,var_9669,call_9704,const_9703,])
func_9708 = relay.Function([var_9669,], output)
mod['func_9708'] = func_9708
mod = relay.transform.InferType()(mod)
var_9709 = relay.var("var_9709", dtype = "int64", shape = (315,))#candidate|9709|(315,)|var|int64
output = func_9708(var_9709)
func_9710 = relay.Function([var_9709], output)
mutated_mod['func_9710'] = func_9710
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9728 = relay.var("var_9728", dtype = "float32", shape = (5, 6, 14))#candidate|9728|(5, 6, 14)|var|float32
var_9729 = relay.var("var_9729", dtype = "float32", shape = (5, 6, 14))#candidate|9729|(5, 6, 14)|var|float32
bop_9730 = relay.floor_mod(var_9728.astype('float32'), relay.reshape(var_9729.astype('float32'), relay.shape_of(var_9728))) # shape=(5, 6, 14)
output = relay.Tuple([bop_9730,])
output2 = relay.Tuple([bop_9730,])
func_9733 = relay.Function([var_9728,var_9729,], output)
mod['func_9733'] = func_9733
mod = relay.transform.InferType()(mod)
mutated_mod['func_9733'] = func_9733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9733_call = mutated_mod.get_global_var('func_9733')
var_9735 = relay.var("var_9735", dtype = "float32", shape = (5, 6, 14))#candidate|9735|(5, 6, 14)|var|float32
var_9736 = relay.var("var_9736", dtype = "float32", shape = (5, 6, 14))#candidate|9736|(5, 6, 14)|var|float32
call_9734 = func_9733_call(var_9735,var_9736,)
output = call_9734
func_9737 = relay.Function([var_9735,var_9736,], output)
mutated_mod['func_9737'] = func_9737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6809_call = mod.get_global_var('func_6809')
func_6810_call = mutated_mod.get_global_var('func_6810')
call_9764 = func_6809_call()
call_9765 = func_6809_call()
uop_9782 = relay.cosh(call_9764.astype('float32')) # shape=(8, 1, 5)
uop_9784 = relay.cosh(call_9765.astype('float32')) # shape=(8, 1, 5)
output = relay.Tuple([uop_9782,])
output2 = relay.Tuple([uop_9784,])
func_9791 = relay.Function([], output)
mod['func_9791'] = func_9791
mod = relay.transform.InferType()(mod)
output = func_9791()
func_9792 = relay.Function([], output)
mutated_mod['func_9792'] = func_9792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9594_call = mod.get_global_var('func_9594')
func_9596_call = mutated_mod.get_global_var('func_9596')
call_9869 = relay.TupleGetItem(func_9594_call(), 0)
call_9870 = relay.TupleGetItem(func_9596_call(), 0)
func_4271_call = mod.get_global_var('func_4271')
func_4272_call = mutated_mod.get_global_var('func_4272')
call_9876 = relay.TupleGetItem(func_4271_call(), 3)
call_9877 = relay.TupleGetItem(func_4272_call(), 3)
func_6526_call = mod.get_global_var('func_6526')
func_6527_call = mutated_mod.get_global_var('func_6527')
call_9885 = func_6526_call()
call_9886 = func_6526_call()
func_9392_call = mod.get_global_var('func_9392')
func_9394_call = mutated_mod.get_global_var('func_9394')
call_9891 = relay.TupleGetItem(func_9392_call(), 1)
call_9892 = relay.TupleGetItem(func_9394_call(), 1)
var_9894 = relay.var("var_9894", dtype = "float32", shape = (8, 9, 5))#candidate|9894|(8, 9, 5)|var|float32
bop_9895 = relay.subtract(call_9885.astype('float32'), var_9894.astype('float32')) # shape=(8, 9, 5)
bop_9898 = relay.subtract(call_9886.astype('float32'), var_9894.astype('float32')) # shape=(8, 9, 5)
output = relay.Tuple([call_9869,call_9876,call_9891,bop_9895,])
output2 = relay.Tuple([call_9870,call_9877,call_9892,bop_9898,])
func_9904 = relay.Function([var_9894,], output)
mod['func_9904'] = func_9904
mod = relay.transform.InferType()(mod)
var_9905 = relay.var("var_9905", dtype = "float32", shape = (8, 9, 5))#candidate|9905|(8, 9, 5)|var|float32
output = func_9904(var_9905)
func_9906 = relay.Function([var_9905], output)
mutated_mod['func_9906'] = func_9906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8893_call = mod.get_global_var('func_8893')
func_8895_call = mutated_mod.get_global_var('func_8895')
call_9947 = relay.TupleGetItem(func_8893_call(), 1)
call_9948 = relay.TupleGetItem(func_8895_call(), 1)
output = relay.Tuple([call_9947,])
output2 = relay.Tuple([call_9948,])
func_9967 = relay.Function([], output)
mod['func_9967'] = func_9967
mod = relay.transform.InferType()(mod)
output = func_9967()
func_9968 = relay.Function([], output)
mutated_mod['func_9968'] = func_9968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3632_call = mod.get_global_var('func_3632')
func_3634_call = mutated_mod.get_global_var('func_3634')
call_10012 = func_3632_call()
call_10013 = func_3632_call()
func_6435_call = mod.get_global_var('func_6435')
func_6438_call = mutated_mod.get_global_var('func_6438')
var_10015 = relay.var("var_10015", dtype = "float32", shape = (560,))#candidate|10015|(560,)|var|float32
call_10014 = relay.TupleGetItem(func_6435_call(relay.reshape(var_10015.astype('float32'), [8, 14, 5])), 1)
call_10016 = relay.TupleGetItem(func_6438_call(relay.reshape(var_10015.astype('float32'), [8, 14, 5])), 1)
func_2442_call = mod.get_global_var('func_2442')
func_2445_call = mutated_mod.get_global_var('func_2445')
const_10033 = relay.const([[-1.913943,-1.838176,6.402147,1.504259,-4.549755,-2.603105,7.869536,2.763559,0.249433,-0.393898,2.366968,-3.645257,-3.551771,2.943179,0.389282,5.926367,1.897284,-4.872378,1.204222,3.534885,-0.722172,-2.486517,7.160693,4.630084,-2.766773,-2.367931,1.895562,-6.074259,2.235523,-0.750264,-4.964739,-5.483182,9.497694,-3.920690,6.713036,4.151988,4.741879,5.353626,9.108584,-4.106653,4.824954,3.346516,0.113272,-0.110970,7.154485,-1.773504,-8.188641,7.907726,0.978188,6.016983,2.931482,-2.700349,-6.055579,-3.697617,-8.620945,3.536617,8.661150,-7.799897,-9.923493,8.709717,-3.864099,-9.783778,1.923992,-8.634679,5.360705,1.582638,-2.233112,-0.870161,2.639834,-7.902698,8.670916,5.589349,6.840010,5.300132,6.139136,1.093939,-0.817845,-7.789251,-2.113823,-4.985604,-2.278790,-8.146001,8.346361,-5.002728,1.679794,1.976221,-3.825619,-0.574421,-7.580159,-5.860166,-3.080995,7.444792,6.651821,-7.125528,6.009774,9.479233,-5.809845,-6.570134,-7.332362,1.603390,-9.127038,-5.338072,4.520944,-8.540787,5.200640,7.383637,-0.374110,-5.749291,6.407466,4.724481,-5.800598,-3.296835,9.610180,-7.218709,7.696249,3.504729,-6.009384,4.243360,-7.098652,-0.907052,-7.505661,-6.135499,-0.496264,-7.494813,3.429647,-6.034071],[-9.714829,2.414179,-2.072532,-4.543307,9.223882,0.223966,6.630625,1.286536,-9.448894,3.008590,-8.763331,0.489594,3.813838,-2.937798,-1.333750,-6.160434,1.187203,-8.532397,8.984911,-8.199218,-2.453431,7.098285,-1.228627,-3.028569,-9.531107,6.169049,5.935481,8.001650,-0.983887,9.094847,1.963249,4.814840,5.416766,-5.500841,-2.694491,1.743100,-4.298193,5.204363,-9.079191,5.599663,6.014559,1.571430,9.037282,1.516624,-5.512740,-5.983604,-0.358889,-5.151063,3.803289,7.045514,7.323122,7.716040,1.082464,-5.764745,-1.365988,-1.761145,-0.701439,-2.070193,-7.932855,0.752848,-0.391972,-6.624559,-1.160324,3.567553,1.909319,3.329166,4.866416,-1.924358,2.271958,-0.508648,-3.328826,-4.731498,-8.744475,5.830910,-9.980703,1.718467,-2.947229,-4.247065,5.898789,7.171311,-4.620709,3.688880,0.437436,-1.626001,2.902360,-2.340245,5.103477,-5.076638,5.520609,-5.594136,3.427320,-2.302155,-9.883270,-8.697985,-6.136595,-9.505564,-2.951469,9.285824,-3.725411,7.172482,-6.321088,0.332526,-0.583180,-5.484635,7.368286,0.273322,-3.123794,0.678463,-7.331127,-7.743533,8.373416,4.086691,6.573527,8.087497,-1.178799,3.032732,-5.275744,-8.925698,-2.395026,-7.698779,-6.628647,-0.775945,3.494439,3.505500,8.447902,4.795210],[-2.398085,2.368305,5.187012,7.882670,8.471524,-1.384939,-9.994725,-1.908359,9.087699,-7.332086,-5.873785,5.692272,-2.801659,-5.286803,-6.755317,-2.871673,-2.880884,-7.571413,-3.297653,-3.889743,-5.013682,7.694798,0.251355,-1.114262,-0.738318,-2.723623,8.625099,3.924958,-1.234742,-5.259020,3.691550,-9.741937,-7.967769,8.136487,-0.550713,-7.988057,-2.376957,0.381172,5.193468,4.149849,1.443345,-6.917897,3.089169,-9.146750,1.176107,-4.671548,-4.649983,1.455443,-2.859322,3.032007,-0.432303,5.053398,-0.225843,-1.523908,-6.112988,7.601352,-0.836963,8.913345,5.969841,3.881141,-1.985904,4.670953,-1.732671,2.097149,6.419936,-0.675725,-5.384550,2.190267,-1.410267,-9.917960,0.053065,-5.534597,2.070970,6.251247,-4.930586,-2.446668,-2.514858,6.548306,-4.355010,1.615612,4.764752,7.047149,-0.261177,-9.711082,-1.205732,1.423887,6.363971,4.412993,9.714224,4.574552,-6.514743,-8.518647,-5.586258,8.448491,-2.757342,-9.875545,-2.228562,1.871879,-6.517347,-4.230615,-1.599460,-4.783211,4.273370,3.518834,-6.989688,-7.913416,-5.742658,-7.968842,-5.565156,7.120224,-4.977002,2.833442,1.427987,2.436601,-9.428462,-3.385854,-7.071408,-2.997512,8.537802,-0.286504,2.394007,-6.864508,-1.341180,-9.490536,-5.914918,1.670980],[4.989210,-9.285631,-1.150579,6.779061,4.726210,2.258887,-5.256089,2.637291,1.435633,-4.381060,4.891246,-8.731786,4.041485,-3.368551,-9.558271,-1.277423,-2.907405,-1.202619,4.404085,-1.045315,-7.953347,-3.998007,4.326326,-5.597372,7.330383,1.375888,2.410753,-9.354657,-5.326617,-3.418302,4.816750,6.611546,7.651859,-0.798394,3.296833,5.321787,-5.460740,-0.775534,-7.372676,0.656823,4.644606,-7.272581,-9.642211,0.984056,4.176072,-5.133752,3.704190,5.105893,4.318347,2.986035,-8.511327,-0.665875,-6.002894,-8.120284,1.364311,-6.360831,7.496489,5.360820,-0.820628,-5.516669,8.265894,-4.852324,-7.144442,4.629261,6.987850,-7.075586,-4.240540,-1.288620,-6.656447,1.288078,-0.884416,-4.607602,-4.688784,-2.526946,9.004596,-2.586953,7.889662,1.529030,-2.800579,5.483841,4.057808,0.257812,6.397908,-1.861837,1.544579,7.760876,4.464149,6.670775,-2.333776,-8.880294,-2.956657,-5.944208,5.434818,-5.671043,-7.658359,6.332207,4.001781,6.901346,9.118699,-5.140464,0.627183,-0.915093,-1.288111,-9.044567,5.998915,-3.796540,-0.187026,0.567728,-2.678394,7.267394,-2.931814,-2.091992,-8.770220,-1.212062,5.240196,-5.739843,-0.195830,3.793328,-9.191375,1.807887,8.285143,9.413523,-8.902918,4.591549,-1.042344,-6.703944],[-9.531433,3.133787,-3.232596,-4.366476,-4.469751,3.211397,0.946199,5.017978,-9.207165,-8.629763,-6.301798,4.049035,-1.987966,2.349985,-2.526647,4.225186,-1.565409,7.511066,-1.135396,-3.423272,-4.021832,-6.660154,5.034860,5.560976,-0.915998,0.423287,0.676341,-5.854573,3.656062,7.474047,5.019707,-0.775095,1.402874,-1.606161,0.292801,-9.591208,-4.294521,-3.318300,9.752923,-4.252687,5.404457,-4.467012,-1.959438,-3.733371,7.832039,5.364385,4.963590,-4.844025,4.213304,-3.176608,-1.753664,-8.603082,5.331720,-3.369240,-9.708878,0.460650,-5.079377,5.750509,-5.468574,-7.391774,6.239892,-1.540831,-1.821266,0.349718,6.138146,-6.947427,-8.091703,1.850697,6.643260,-2.527347,-7.234083,4.226516,-2.874173,2.551934,4.522598,-7.111935,-3.147882,8.200398,0.420515,-8.625837,-2.761641,-0.076793,-9.700670,6.672319,8.353713,7.804590,4.413520,-8.987180,2.729807,-4.107762,-1.861555,2.594703,9.523248,9.404897,6.491943,0.309255,-5.695396,5.492794,2.490903,2.749913,-2.006261,-0.025098,9.094884,0.316830,2.653142,8.213256,-1.230509,-8.349466,4.682486,1.140588,6.066720,6.505928,-0.834521,-2.753722,7.787585,0.129126,5.510073,1.414375,-6.503498,1.366607,-1.472183,8.917959,-2.543858,-0.168711,2.714397,-1.175436],[-5.924698,1.914350,-5.148836,5.294302,3.459150,-7.696378,-4.929875,4.959620,-1.708906,-4.799847,-2.914198,-3.805075,6.895400,-3.325067,-8.249984,-1.788559,-6.565895,8.068952,9.430510,-2.131111,3.550837,1.510703,-9.494670,8.420749,-9.946923,4.198645,1.239987,4.889218,-3.335057,-0.032446,-6.291435,-3.944384,-4.015342,-5.981301,-4.327418,-7.344074,5.337944,5.721454,-9.191249,-6.458201,3.632293,1.915362,6.288813,2.990781,3.949622,-3.078906,-4.850755,-3.820081,6.169872,5.601297,-0.848662,3.463223,5.353493,2.398595,3.171122,-8.377096,-7.857640,-5.636754,-5.574951,9.208423,5.626378,-0.603508,-0.183798,-5.153587,2.753500,2.352848,9.658138,1.971493,-0.695651,-6.841350,-9.730025,-2.008016,2.830242,1.824533,-5.700277,9.674913,-5.491846,-8.996046,-9.336974,-8.995246,-7.824502,2.179405,2.603048,-5.832046,-1.462529,0.540097,-2.454639,4.867246,-8.863505,0.023617,1.647947,-6.411594,-2.242783,1.847690,2.187759,-1.315985,9.759786,2.911127,-3.389430,-6.238960,7.243696,-8.565141,4.838080,4.006907,-3.125441,6.911793,4.722837,6.307175,-6.235535,-6.857930,1.075948,5.429067,0.809255,2.564800,-4.777725,-5.967875,3.472032,9.060085,-2.445893,9.309561,-7.822849,-6.718712,-0.386935,0.636052,-0.714988,5.265812],[6.449013,4.708952,0.783685,-8.940930,-0.314017,1.017260,1.879893,8.977913,8.403353,-8.294714,0.077608,9.711124,8.806944,-5.654626,0.950513,5.682866,-6.987705,9.612668,7.924165,2.434487,-9.091650,0.812106,-7.234542,3.868967,6.592926,8.967679,-3.250149,0.696017,6.505131,-2.016228,2.122225,7.176829,-2.717583,3.920815,8.961875,9.816528,-9.090161,0.496257,9.267113,-2.275745,2.379798,2.453538,8.441489,5.540168,-9.692372,6.363532,7.256104,7.066734,1.619067,0.652358,-9.020812,-2.738879,2.373540,0.006372,-3.676968,-5.836975,9.949119,9.372462,-1.561489,5.284980,-4.086178,-7.787472,-0.276666,5.252215,-7.606075,-3.635551,-3.581303,0.263780,-6.049727,-0.836741,2.236242,-2.718488,4.787484,9.081420,-4.636733,-6.036342,6.226621,-7.492850,6.392585,9.063330,-0.652008,-8.471256,-9.318611,6.947187,-1.128822,1.482211,-4.114407,-1.633635,1.009450,1.441545,-5.603490,2.196484,-0.346436,6.958757,5.750531,1.862206,-6.840128,-1.217313,-5.285132,-2.402891,-6.059314,-9.340317,2.451352,-1.167638,-1.118899,5.013709,3.812038,-3.740444,-0.353887,8.799936,-0.847334,-8.083169,-7.524953,2.456879,-9.466895,7.363570,6.792410,2.050996,-8.228095,3.362024,2.895213,-3.439088,2.861855,-6.998111,-7.562961,-6.288790],[-9.897024,-7.799471,2.889624,6.086511,9.346108,-1.271827,-0.028794,7.868185,0.230994,8.716083,6.309703,-6.360963,-4.419804,8.461941,-0.533784,0.075041,-3.646321,-8.740181,1.499253,1.995363,-6.323146,7.551499,1.321863,-7.722167,-7.767353,4.545347,6.837576,-6.997228,-9.809083,-0.186092,2.150337,8.028571,8.252912,-1.003872,-2.362834,4.598289,0.473053,1.534356,-5.569459,-7.338934,-2.908438,-9.062566,3.253514,2.292437,-5.524298,-8.532430,-0.415423,5.136226,3.663719,-2.751969,2.421521,3.350740,1.343554,7.070730,-3.150512,-1.451604,4.448353,-4.107306,3.791999,-0.652483,0.119944,-7.122248,9.701033,-6.663172,3.396267,-0.603694,-0.712878,1.888724,-1.519344,2.756918,-0.543298,9.374869,5.206855,-0.619957,-4.832389,-7.362402,-9.509791,7.370339,9.142240,-5.664481,-8.010584,4.333916,-8.936353,-7.428034,-4.500616,6.256859,5.042147,-8.502334,-3.752498,-7.125796,-3.221524,8.415325,0.907894,-8.864025,-8.048422,2.840625,3.403495,9.759607,2.230431,-7.007408,-8.824446,4.847844,9.135245,-9.549802,-2.231739,-0.574183,7.474616,0.579554,-1.943365,7.121053,1.739802,3.658062,-8.962324,-1.150733,4.923279,7.149898,9.292862,0.875365,-3.646691,-6.294047,-2.403207,6.995665,-0.554644,-9.911993,-4.010396,3.990967],[-8.618860,-9.939489,-2.606133,5.029285,-5.880699,8.602047,1.975501,-0.797897,-1.808061,-4.882684,5.055928,-5.544784,9.405343,-2.769002,5.013569,9.484869,-3.948703,-1.291981,-9.776861,-5.852465,-3.332344,-3.012496,3.620890,9.055577,-1.883436,-6.223147,-9.024176,3.213729,-6.043681,0.221273,-4.736440,9.921570,0.889861,0.472244,5.752694,-7.590352,9.801157,0.305495,9.743200,-3.897886,4.653061,1.710145,4.378252,7.175371,-3.129339,9.268834,9.587421,9.366925,-4.666153,-4.306508,2.197745,6.826028,-2.387745,6.238296,-3.241137,4.600077,-7.944118,7.401607,4.162401,3.962886,2.318961,-0.416236,-9.983574,3.419579,-9.668789,-0.359761,-7.696199,-3.513972,8.661220,-2.516588,7.559954,5.901792,-6.509538,-5.883262,6.789230,2.052449,-0.312984,8.316988,-8.021711,-6.568904,-3.750719,-0.931086,-3.841332,8.658500,-9.621334,9.930149,2.433595,1.864106,0.234484,-7.545455,-2.253608,-0.837534,3.905799,8.937148,-5.327156,7.084829,-2.338021,-6.202489,-8.259016,-3.321595,9.796458,8.888184,-4.603016,4.944926,-7.373143,-0.453828,1.364952,9.229155,-8.491269,-8.841118,-8.999099,-6.871187,3.620070,-7.511576,-9.330045,-5.192787,-2.642508,2.883239,8.993834,9.961835,-3.606318,-3.233036,-1.743434,-6.541442,-0.789557,6.803367]], dtype = "float32")#candidate|10033|(9, 126)|const|float32
call_10032 = relay.TupleGetItem(func_2442_call(relay.reshape(const_10033.astype('float32'), [1134,])), 2)
call_10034 = relay.TupleGetItem(func_2445_call(relay.reshape(const_10033.astype('float32'), [1134,])), 2)
output = relay.Tuple([call_10012,call_10014,var_10015,call_10032,const_10033,])
output2 = relay.Tuple([call_10013,call_10016,var_10015,call_10034,const_10033,])
func_10036 = relay.Function([var_10015,], output)
mod['func_10036'] = func_10036
mod = relay.transform.InferType()(mod)
mutated_mod['func_10036'] = func_10036
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10037 = relay.var("var_10037", dtype = "float32", shape = (560,))#candidate|10037|(560,)|var|float32
func_10036_call = mutated_mod.get_global_var('func_10036')
call_10038 = func_10036_call(var_10037)
output = call_10038
func_10039 = relay.Function([var_10037], output)
mutated_mod['func_10039'] = func_10039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4530_call = mod.get_global_var('func_4530')
func_4531_call = mutated_mod.get_global_var('func_4531')
call_10045 = relay.TupleGetItem(func_4530_call(), 2)
call_10046 = relay.TupleGetItem(func_4531_call(), 2)
func_9076_call = mod.get_global_var('func_9076')
func_9079_call = mutated_mod.get_global_var('func_9079')
var_10057 = relay.var("var_10057", dtype = "float32", shape = (520,))#candidate|10057|(520,)|var|float32
call_10056 = relay.TupleGetItem(func_9076_call(relay.reshape(var_10057.astype('float32'), [8, 13, 5])), 2)
call_10058 = relay.TupleGetItem(func_9079_call(relay.reshape(var_10057.astype('float32'), [8, 13, 5])), 2)
bop_10079 = relay.logical_xor(call_10056.astype('uint32'), relay.reshape(call_10045.astype('uint32'), relay.shape_of(call_10056))) # shape=(8, 1, 5)
bop_10082 = relay.logical_xor(call_10058.astype('uint32'), relay.reshape(call_10046.astype('uint32'), relay.shape_of(call_10058))) # shape=(8, 1, 5)
output = relay.Tuple([var_10057,bop_10079,])
output2 = relay.Tuple([var_10057,bop_10082,])
func_10100 = relay.Function([var_10057,], output)
mod['func_10100'] = func_10100
mod = relay.transform.InferType()(mod)
var_10101 = relay.var("var_10101", dtype = "float32", shape = (520,))#candidate|10101|(520,)|var|float32
output = func_10100(var_10101)
func_10102 = relay.Function([var_10101], output)
mutated_mod['func_10102'] = func_10102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4271_call = mod.get_global_var('func_4271')
func_4272_call = mutated_mod.get_global_var('func_4272')
call_10107 = relay.TupleGetItem(func_4271_call(), 2)
call_10108 = relay.TupleGetItem(func_4272_call(), 2)
output = relay.Tuple([call_10107,])
output2 = relay.Tuple([call_10108,])
func_10111 = relay.Function([], output)
mod['func_10111'] = func_10111
mod = relay.transform.InferType()(mod)
output = func_10111()
func_10112 = relay.Function([], output)
mutated_mod['func_10112'] = func_10112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6526_call = mod.get_global_var('func_6526')
func_6527_call = mutated_mod.get_global_var('func_6527')
call_10130 = func_6526_call()
call_10131 = func_6526_call()
output = relay.Tuple([call_10130,])
output2 = relay.Tuple([call_10131,])
func_10138 = relay.Function([], output)
mod['func_10138'] = func_10138
mod = relay.transform.InferType()(mod)
mutated_mod['func_10138'] = func_10138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10138_call = mutated_mod.get_global_var('func_10138')
call_10139 = func_10138_call()
output = call_10139
func_10140 = relay.Function([], output)
mutated_mod['func_10140'] = func_10140
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10154 = relay.var("var_10154", dtype = "float64", shape = (4, 15, 9))#candidate|10154|(4, 15, 9)|var|float64
const_10155 = relay.const([[[-5.915452,6.289383,-8.721076,-7.630170,-3.112045,1.493468,-8.781758,1.227817,1.896277],[3.477524,-0.885149,9.233194,-2.908608,-4.257299,-3.941108,3.973216,-9.252031,-3.927941],[-2.142726,-6.697973,0.077847,7.692801,7.499208,-1.288830,-6.710249,0.093599,1.508577],[-3.956301,5.371738,-5.862267,-2.367498,-8.661671,-5.587686,3.212166,3.034416,-6.966794],[6.561219,-5.729081,-8.850187,-4.610055,5.093358,7.782965,-9.557105,-7.752723,-6.562864],[7.529812,-0.038090,3.603705,2.499472,-4.970303,-2.520080,5.083277,-2.634914,1.808760],[-7.251215,0.670147,0.764698,-3.732822,-9.074932,6.626802,6.552148,-3.673648,-1.168277],[-0.771151,-6.291992,-9.304251,2.518769,5.881615,5.329964,-3.130778,-8.191128,9.333737],[2.803621,0.367893,6.794663,-8.369767,9.949251,-4.699544,1.648505,5.565810,4.741656],[-4.007452,5.180132,1.084960,-4.671127,-2.110454,7.892908,-6.161856,0.467937,5.188565],[-3.841859,8.014311,-0.227708,1.267649,4.681326,0.684245,-1.199223,1.921113,4.097742],[9.375043,4.718192,-6.696115,7.227065,2.899871,-0.813190,3.426162,-3.169646,9.777358],[9.839249,-3.046553,0.302693,4.172637,-6.382380,-1.480649,6.425136,9.099752,9.220768],[-1.128077,4.933127,-0.728572,-4.103385,-3.273365,-2.489171,5.936153,6.658927,-3.990758],[5.439636,-1.201315,0.329165,-1.235904,-1.824311,3.948535,0.568672,0.480205,7.276238]],[[3.406455,3.620504,-8.802737,3.072081,3.434754,-7.101578,6.274982,-9.107602,1.720039],[-3.750123,-5.817407,9.416584,6.395777,4.479433,5.958895,-2.654789,-2.658992,9.332105],[0.841524,-6.961482,1.831938,3.608630,4.015724,-5.813418,7.334555,-3.369473,-2.435127],[1.457638,-7.289166,-4.299067,6.133282,-7.839045,-7.463679,-9.765007,-6.028191,3.100709],[6.813073,8.721844,-5.305019,9.698639,-5.104474,6.139821,-0.748174,-9.289827,-2.498707],[-3.846777,2.337280,2.794928,-1.566012,-6.600674,6.933662,-8.930716,-7.272812,1.701649],[-3.515033,-2.736981,-0.273421,7.293318,-7.341281,0.354776,-8.659362,-3.508793,9.770540],[6.686097,7.854921,-4.693662,1.111442,-5.821274,-1.189112,-4.008504,-4.645296,-8.606872],[7.626542,4.465064,5.165708,-6.886892,9.277472,-3.326209,-3.624031,-2.561530,8.670241],[-9.533545,-9.466860,-1.375388,-8.116101,8.443200,1.122859,8.980929,2.053834,-9.257239],[-0.229533,-3.164075,1.776054,-8.635360,-3.616950,7.838163,2.694451,6.790799,-3.888722],[5.353211,-4.915844,-3.199196,-5.277259,-7.330589,-9.858565,-9.654737,2.657341,-7.960822],[3.276207,9.815208,-0.266938,2.766850,-6.301630,4.378241,-4.525101,-4.822506,3.137813],[-2.700060,-7.970641,1.104192,7.162894,9.947933,-9.788805,7.483954,-3.461337,7.815170],[-4.593815,7.883012,6.816532,3.334392,2.362931,5.169360,-0.081585,-4.788245,-5.559979]],[[-6.620976,9.939582,7.530319,3.327368,-6.712440,0.551016,-9.057874,-3.959408,-8.697167],[-2.837370,-7.067058,3.528074,-5.197416,9.389831,2.498933,-3.680259,-8.237966,7.864006],[3.071305,-7.112713,0.255501,-2.883492,6.063646,9.133480,-8.874148,-7.932499,3.524933],[-5.290775,2.684491,-6.739549,-0.160053,-2.402199,-3.758887,-5.090430,9.506138,0.355292],[-9.503279,-9.471985,2.147968,9.299489,-0.360118,-7.970610,-4.339642,2.046480,-3.160335],[-1.049743,6.403376,4.719398,-3.752334,1.944787,7.086674,-5.012357,-1.774344,4.417110],[-0.647696,-2.075437,-9.615471,-0.431540,1.081679,8.833413,6.820159,-5.933509,-7.777326],[5.592202,8.179009,-8.770150,3.759140,-4.586130,-1.631707,0.763645,7.216502,9.441296],[-8.625983,-7.779930,3.960261,-6.298269,5.773142,7.980396,-6.211316,-5.213254,-8.555008],[-7.737956,-3.716759,6.768974,8.263327,2.161987,-0.031888,-1.675465,1.640764,0.836988],[-7.031173,5.059154,-9.628452,-5.997498,1.866867,1.605670,3.663297,-9.795525,-8.447123],[-8.022281,-3.003598,-1.966990,-1.043108,-9.786721,4.542843,2.415642,7.196159,9.080809],[6.157825,-0.949856,5.556802,-7.884872,-6.350177,-1.132228,1.557548,-2.133670,-5.195986],[-2.259637,7.447435,-8.907011,-2.019025,9.084838,7.878836,-8.227850,-7.931998,8.989816],[-7.245762,-2.354534,-5.159525,3.562111,-9.025480,-2.122260,1.661454,1.453908,1.475018]],[[8.081297,2.891326,8.869142,-7.649341,-6.423213,-3.173192,-1.962134,3.929885,3.412872],[5.647574,4.108996,-2.616949,-8.073324,9.707152,7.185146,-5.343080,-2.338857,7.369988],[-1.768730,9.482713,-1.827116,-5.661098,-7.483354,8.808937,-7.358349,8.501959,-1.564878],[7.201219,0.971497,4.538586,5.988319,8.785134,8.779784,0.012380,-3.070605,-9.418222],[-4.531237,2.815243,6.179230,1.668409,6.774683,1.388249,-2.130473,2.131084,0.627889],[-2.072213,-2.625937,2.688841,-0.857980,6.306017,8.017557,6.082867,-2.991721,3.901049],[-6.902070,4.769730,9.437702,3.480323,6.721413,1.445665,6.809234,2.057255,1.314099],[-3.486594,2.972217,4.127185,3.796802,3.540726,0.928424,9.466327,7.164615,-8.490471],[-0.316036,-2.590714,-5.290365,-7.147421,-5.872526,6.787829,-1.188281,1.348315,5.201668],[3.611978,-0.445383,-4.025774,0.721457,0.704482,4.055069,1.943786,9.516548,6.972633],[9.128010,-6.034122,-6.024831,6.025423,4.411528,-4.747585,8.531668,3.338270,-6.216394],[-7.995455,-0.891762,-4.165009,5.901757,6.527235,-2.874505,-5.973399,-9.791802,5.942849],[-4.025626,-5.572043,9.635928,-4.306718,-7.820860,-2.692392,7.865212,-8.889270,-0.596197],[3.607666,-3.772361,6.265346,-6.902990,-7.419417,-7.627924,1.548937,-7.151474,-8.191194],[-3.447058,5.316005,-5.788106,-6.184596,-4.990655,3.612150,5.288173,-2.693239,2.752527]]], dtype = "float64")#candidate|10155|(4, 15, 9)|const|float64
bop_10156 = relay.power(var_10154.astype('float64'), relay.reshape(const_10155.astype('float64'), relay.shape_of(var_10154))) # shape=(4, 15, 9)
uop_10162 = relay.exp(bop_10156.astype('float64')) # shape=(4, 15, 9)
func_9353_call = mod.get_global_var('func_9353')
func_9354_call = mutated_mod.get_global_var('func_9354')
call_10173 = relay.TupleGetItem(func_9353_call(), 1)
call_10174 = relay.TupleGetItem(func_9354_call(), 1)
uop_10179 = relay.log2(uop_10162.astype('float32')) # shape=(4, 15, 9)
const_10187 = relay.const([[[-8.969777,-6.627312,-1.619207,-8.144029,0.523203,8.955148,6.695828,-1.406595,-1.308057],[4.716173,-3.471742,2.770315,4.433519,-7.919596,5.007254,-0.422632,4.914253,-0.199352],[8.192598,-1.306686,3.435656,3.569302,-7.971335,2.971906,-4.857512,-9.926940,-8.414891],[-4.724842,1.265773,0.561244,1.519220,8.328771,-0.887173,-3.949048,-9.657253,-0.773569],[-5.318118,0.434554,6.518071,1.738336,9.382087,4.673974,5.812388,-5.201342,-0.616578],[1.563209,7.004648,-8.513224,-0.911646,-4.351610,0.993099,-8.145496,-1.298020,-3.560351],[-0.727556,2.751846,-1.773815,2.311657,-4.586787,-9.788939,-3.766721,-4.405353,-5.543881],[1.358815,9.136533,-0.632202,6.825380,-8.383187,-9.318324,8.089289,-4.133748,-4.324236],[2.857855,2.304365,6.615891,-7.988097,8.341548,-9.497551,0.917023,5.813273,4.731283],[-7.198665,-6.780114,-7.506210,9.041657,-3.869681,-3.527204,-9.535655,-5.350882,2.293677],[-8.084075,9.746704,0.017917,6.114335,-2.193776,5.785311,-7.275238,-2.166104,4.967204],[6.048517,-6.326788,-4.652921,5.158400,7.780252,-7.235782,9.946941,-2.132355,0.268957],[-5.541104,2.093498,9.988296,-6.772646,-4.238843,-2.960636,0.079979,-0.952312,4.261097],[-9.387230,-2.109626,1.078428,5.599162,9.346011,0.355658,7.429587,1.869381,-4.740045],[0.909198,6.721747,3.527156,6.834669,6.748263,6.102277,2.219831,2.228025,6.424745]],[[-5.036778,-7.967290,-9.254278,-1.540307,0.620430,-4.118239,-1.985089,2.409544,9.899130],[-0.024944,3.052004,3.392124,-3.047712,2.842241,-2.260714,-2.309145,7.924780,-1.267675],[6.750964,8.314998,-5.675103,-9.335708,4.883529,-5.859218,9.081710,-1.456866,5.268416],[2.104907,-7.196200,3.622602,8.073275,0.123682,-4.722770,-3.269475,6.430445,1.134860],[-2.319198,-9.539212,2.005054,-0.881333,1.603398,0.607452,-6.329759,9.105973,2.046886],[9.191113,-1.756522,4.398957,-6.770373,-2.410278,4.935533,-9.533643,-5.333597,-3.259011],[0.657406,-3.959901,5.448151,9.868476,-5.849735,-0.896990,-2.321504,-2.316299,-0.372967],[7.820840,5.333234,-2.056265,0.731971,-3.863750,-5.242383,1.241598,-0.076781,-7.034198],[-1.646704,6.693032,-8.820207,-5.585253,-3.574228,-5.675078,7.271297,0.353020,2.886301],[3.690698,-8.977264,-8.659308,-2.129946,1.630646,7.026307,-3.598887,5.622585,-8.611262],[9.621608,-3.591189,8.934121,6.081545,3.770134,-2.420037,-4.049398,7.942552,1.986410],[9.924498,-7.097402,-2.658641,8.001438,1.316592,0.711988,-4.558616,-7.405455,-0.776670],[4.978777,-0.513861,-1.964224,-4.297340,5.551774,-7.021421,7.261868,-5.179239,-4.776331],[-9.873902,-4.147272,-0.765485,3.798829,-1.521856,-3.031206,-3.989873,-3.027779,-1.403671],[0.006204,-4.637725,-8.386452,6.807454,-5.144624,0.408345,3.940173,-6.264747,3.948513]],[[3.806634,-4.717462,4.042823,-2.295390,-0.246838,-0.856814,9.305220,4.678133,-6.483620],[-8.306956,-0.798042,-7.728962,1.991809,5.867543,0.426045,6.250010,2.225122,-3.689192],[-0.187171,-9.808632,-6.636636,9.222022,-4.133514,1.053114,-8.959660,5.921309,-7.284137],[7.848103,5.035423,-0.396393,4.282536,6.026283,2.513466,0.427503,-0.407913,-4.703810],[1.068771,-0.660740,0.304623,-4.416518,-4.066563,-4.286185,7.425443,-1.326057,-2.319312],[6.065049,-8.853597,-1.308585,7.595223,5.876113,-0.861909,-0.866674,7.030006,7.712135],[-4.150545,4.108327,3.634048,6.095664,5.414999,5.612454,-6.293451,5.593236,2.916106],[-8.953342,-6.182123,-9.273380,-5.647411,-7.535114,-4.019869,-1.198504,1.247116,9.980953],[1.401811,-4.647614,-8.391770,-4.620424,-0.337990,-5.165322,2.778217,-5.772656,-7.016471],[-5.407117,2.738086,0.249022,2.854550,-0.520605,8.543989,6.563386,5.088409,3.373804],[-2.247610,-4.220948,9.495183,-0.908682,-5.514338,-8.767443,-7.136109,2.217250,2.101294],[6.145265,-0.979307,-6.295646,4.951398,-8.746223,4.519705,-3.341070,5.332383,-8.600288],[2.905970,1.798814,-6.110139,6.010419,1.587547,-9.642332,1.075969,4.904646,-2.374017],[2.746533,2.821025,-0.342541,9.922283,-1.196693,1.335879,8.215517,-4.197335,-8.044110],[1.805652,0.196348,-7.265305,0.706992,9.802968,8.205374,-6.121136,2.334445,-0.518136]],[[-9.263818,-1.660497,-1.651006,-6.245902,9.265410,7.102798,4.320431,6.326609,1.140037],[-3.835355,1.617972,2.292923,4.996098,3.642291,0.556793,-0.013117,7.639315,3.530564],[7.343326,5.055482,-6.772710,-4.267649,6.903814,-9.038030,-9.371655,-2.854042,-1.779377],[-1.980109,9.800045,-7.999380,-6.582353,3.373170,9.277606,9.183661,-7.510748,8.481887],[7.776286,-9.423068,6.645847,8.400076,3.144601,2.241010,2.209044,-5.766056,4.191098],[-8.351623,2.723063,5.244054,-0.937341,2.784948,-3.280452,9.212020,6.883957,-0.918825],[-1.671007,-2.707867,6.310915,7.016128,4.785459,-1.322859,-6.800797,-3.166367,-3.878895],[-9.515134,0.169104,7.043232,5.874613,6.666579,-1.666404,9.898940,-1.106538,-3.980110],[-5.088562,-5.497592,1.900016,-8.024637,3.818196,-2.820987,8.170515,-1.481841,-4.076451],[-7.169319,-5.053188,-6.840357,1.906761,5.802379,3.988057,-9.967863,9.687920,-0.561001],[4.412965,-3.608018,5.914850,-6.223721,-1.890621,9.633023,-0.462907,-5.046699,-6.990972],[1.270661,-8.503879,6.605501,-2.861235,8.723339,-6.911314,8.034910,9.705971,9.228805],[-1.300123,0.859080,-0.914387,5.717581,-0.996122,-7.868054,0.366026,-3.487091,-4.041518],[6.503119,1.480332,1.708401,-9.344094,2.255863,-2.774617,6.880251,-9.315069,2.460468],[4.886369,8.697611,-7.296272,-9.792512,2.495349,-7.396647,-7.126290,1.453613,-1.430962]]], dtype = "float32")#candidate|10187|(4, 15, 9)|const|float32
bop_10188 = relay.subtract(uop_10179.astype('float32'), relay.reshape(const_10187.astype('float32'), relay.shape_of(uop_10179))) # shape=(4, 15, 9)
func_9076_call = mod.get_global_var('func_9076')
func_9079_call = mutated_mod.get_global_var('func_9079')
const_10195 = relay.const([-9.805624,7.467300,-9.568185,0.500717,9.172126,8.923225,4.436043,9.785622,-9.533488,9.672964,-0.041323,0.980015,-8.548849,8.472235,7.511705,4.865504,-7.220925,-2.387739,5.319169,-1.548121,2.477454,0.717428,1.182557,-3.448646,8.154246,2.841235,9.467584,8.881488,-8.266115,0.053558,-1.292051,2.842677,3.276001,-7.301303,7.732705,2.134258,-5.282433,8.751656,7.159378,7.151871,5.922063,-9.111417,3.153499,-7.155781,-2.188531,2.521254,-7.196734,-0.224860,0.142658,-7.098531,1.970308,6.180169,9.163254,6.384376,-3.143700,5.631419,1.706335,-7.152455,8.878628,-2.439664,1.776886,4.336539,-9.921768,6.675595,-0.857921,-6.033136,-9.223158,8.384565,-4.195062,-8.928552,6.900771,-7.907863,-4.834719,6.118551,6.979754,6.480164,-9.574713,-1.428950,-3.485315,-3.471772,-4.729824,-2.378320,-6.873911,-9.122118,-1.629248,-7.555657,-6.225411,2.181506,6.604443,8.569580,-8.463116,4.879212,6.727665,-2.382265,-0.151963,-5.416271,2.362792,4.011915,-0.096260,3.543983,-7.449944,-1.825579,-9.576537,4.069697,-4.165719,8.155791,-1.424458,8.277029,-1.687784,0.413944,-8.604601,0.547250,2.139085,-3.076273,-4.143345,-4.112099,5.682342,-1.047440,-6.853648,3.868123,-3.141508,-2.554277,-1.925466,-4.119169,8.046547,2.966816,1.737364,3.821608,1.252748,-9.350700,0.222978,-6.539560,5.711808,4.181748,5.454290,-5.255696,0.872271,-6.326012,0.760036,-8.342479,-4.551104,-6.818510,0.486049,-4.085092,1.494593,-6.280847,-4.765421,3.798549,9.873221,7.937339,-6.280291,-4.172468,-0.941558,3.884256,1.155146,-0.434026,6.842994,1.175547,5.123363,6.708496,-0.227095,6.122138,-9.613890,-4.558005,0.340228,-7.956540,-8.027840,9.990528,4.333388,-1.200148,1.877983,2.391858,5.544553,0.765879,-5.520241,-7.660300,-8.535834,3.354102,-6.455336,8.875509,-3.280371,3.070407,-8.889854,2.147733,8.617968,5.637831,5.510614,5.638556,8.324604,3.090539,8.542393,5.436565,4.868532,0.208317,-8.065501,-0.722092,-2.834925,6.074027,-9.521022,8.544125,-1.316065,-1.730840,8.108844,2.891478,-6.714125,-0.197945,-0.248078,-1.345469,6.689672,9.273131,-6.588250,-0.012707,-1.375009,7.280398,-8.269384,-6.997714,9.232244,-5.182814,4.291850,-0.524008,-5.187869,8.427913,-4.346348,4.879380,4.957636,6.068852,-1.305039,1.898994,-1.945569,2.181133,4.370825,5.963180,8.062110,2.080127,6.872427,-9.748455,-2.796697,-8.862618,8.963480,-6.667318,3.512197,-8.344530,3.804351,-4.976941,2.638522,2.719438,6.756501,3.918140,-9.464835,0.459515,-9.667484,-1.480718,-3.790257,9.855365,-0.806758,-8.878723,-1.569916,4.448768,-0.083580,4.166449,1.346981,-8.200748,1.022564,9.018681,-5.124818,-1.770973,5.635420,-7.989940,5.058201,1.537571,9.421002,9.893600,5.301997,-6.735365,-4.278175,7.787112,-7.985303,4.544394,3.321456,9.687397,8.153458,2.193682,-4.389527,-8.184023,3.413992,5.405501,-9.304699,-8.573157,6.142370,6.963599,-8.433234,-6.403179,6.917758,6.472683,-4.448152,-7.782538,-0.783810,-0.664974,8.228156,-4.935512,1.585660,-8.103678,1.060339,0.119396,9.853612,-8.740110,6.129450,-0.964482,-3.900318,2.573628,-9.733458,6.786320,7.772210,-1.972634,-7.376538,-9.247868,-5.465885,4.701767,6.150987,9.232121,-6.078211,2.726394,-1.856040,-7.250248,2.899850,0.750381,6.924333,-7.597313,6.858129,-1.281421,3.896513,2.394287,0.996285,0.985412,1.869470,3.973194,5.627670,8.148518,-6.954256,-8.042180,1.091721,7.738366,-2.074410,-6.416207,-6.832092,-5.409415,1.744078,-9.962140,-0.402462,9.266333,-2.155345,3.438242,8.247153,6.216378,-6.877997,4.116790,4.150601,0.275750,-5.279705,7.128158,-4.675979,3.161582,6.887154,-4.016251,0.616953,3.432638,-3.596940,7.633513,6.243005,6.732204,6.441204,-2.478533,6.763223,-5.876482,6.637310,8.627170,1.955036,3.321320,-7.495848,7.264359,2.119486,6.155016,0.987595,-8.411598,3.151180,6.033679,-8.684751,0.167751,9.887637,-5.530307,-0.908991,-1.964187,-3.116097,-4.960846,5.495717,-3.478647,9.537549,-5.092266,8.267203,3.952995,-7.599721,7.053760,-0.474352,-8.017399,-8.225541,-6.044434,-4.636436,6.253389,-3.359408,9.915908,9.931959,5.463616,4.170786,1.440723,-4.958659,1.976515,0.829860,3.188994,-3.814596,9.986629,-5.284458,6.939133,-0.819927,3.992513,-0.573664,-2.882159,7.854083,-3.645455,3.609890,6.507013,5.031321,-7.137852,2.624183,-0.185312,-7.003835,-6.832377,-7.235461,7.870670,-9.374925,2.856798,-5.877145,-0.485805,4.430230,-8.334272,1.865231,-1.209774,7.346845,0.372533,6.667561,-0.675277,-5.891881,-8.343515,-4.147121,4.584757,4.826171,5.660172,9.828110,9.663890,5.882274,9.544894,2.968254,6.312764,0.616175,1.029072,-9.730009,-4.852830,-8.977939,5.977158,-6.343138,-6.817054,-8.515778,7.301238,7.906788,-5.988242,3.281909,0.885512,-5.890059,7.671745,-4.750300,-0.278948,-4.952352,8.602758,2.528446,9.551411,3.144254,3.781309,5.880434,8.205660,3.541480,2.127558,-6.359424,9.587506,4.287618,-3.347174,9.597842,6.100402,0.200358,6.523323,6.685823,-6.774238,-8.293902,-9.065245,3.355680,-5.378369,-6.077102,4.132127,5.800263,9.351666,0.473527,-2.889863,-3.021002,-6.392724,-9.633003,-8.839525,-7.582603,-1.090682,4.309634,-4.517627,3.687431,1.582716], dtype = "float32")#candidate|10195|(520,)|const|float32
call_10194 = relay.TupleGetItem(func_9076_call(relay.reshape(const_10195.astype('float32'), [8, 13, 5])), 2)
call_10196 = relay.TupleGetItem(func_9079_call(relay.reshape(const_10195.astype('float32'), [8, 13, 5])), 2)
output = relay.Tuple([call_10173,bop_10188,call_10194,const_10195,])
output2 = relay.Tuple([call_10174,bop_10188,call_10196,const_10195,])
func_10201 = relay.Function([var_10154,], output)
mod['func_10201'] = func_10201
mod = relay.transform.InferType()(mod)
var_10202 = relay.var("var_10202", dtype = "float64", shape = (4, 15, 9))#candidate|10202|(4, 15, 9)|var|float64
output = func_10201(var_10202)
func_10203 = relay.Function([var_10202], output)
mutated_mod['func_10203'] = func_10203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3298_call = mod.get_global_var('func_3298')
func_3299_call = mutated_mod.get_global_var('func_3299')
call_10263 = relay.TupleGetItem(func_3298_call(), 1)
call_10264 = relay.TupleGetItem(func_3299_call(), 1)
func_6435_call = mod.get_global_var('func_6435')
func_6438_call = mutated_mod.get_global_var('func_6438')
const_10269 = relay.const([-3.666477,2.352027,4.022778,-2.517247,-3.560219,-2.662162,3.956478,-2.387127,5.577123,8.124477,9.565104,9.087959,9.167793,5.174965,-9.019545,-3.726125,-1.820921,8.409682,-0.012347,8.024175,9.966960,9.996679,8.246923,-5.404227,-9.628712,-4.276835,-9.603829,0.974365,-6.348158,-7.872342,6.537081,1.844794,-3.007888,0.620920,7.066205,7.662804,0.016497,8.742491,-3.895182,8.464705,-6.617992,1.271823,3.209846,-9.506549,1.539408,-1.405740,6.142570,-2.937408,3.493036,-8.373406,-3.207955,8.236564,-8.002189,0.840334,0.423507,-2.330034,-2.079564,-9.521133,-4.149368,2.655476,3.226089,-4.320640,-9.946183,-7.860505,8.614780,-0.893738,-7.826982,8.687643,-2.022361,9.402110,9.391253,4.093676,0.943959,-9.905254,-2.212636,-4.425755,8.892347,-2.624226,2.209791,8.621441,-5.875973,9.085964,-9.947504,5.894332,3.590648,-6.100602,-4.725905,-3.818338,4.367667,4.405221,-3.877931,4.135921,7.557073,9.042367,-3.997355,8.456651,-2.226570,0.486510,9.842489,-9.313815,0.826992,6.270467,-4.349877,-6.467031,-8.755634,-9.931937,6.318302,9.945779,8.880720,9.288430,0.824833,-7.229734,9.144819,-2.744341,5.281960,4.145559,7.816260,-2.479452,-0.763013,8.583235,2.982472,-6.741874,4.494469,6.155286,-4.764291,-0.852488,7.004448,-6.244371,-0.211609,0.629254,5.027823,6.549207,6.636760,-4.395668,-2.528880,0.704267,0.213273,-0.567040,0.845741,-8.478415,-5.318815,1.223797,0.517482,8.068264,7.455578,2.730786,9.626170,9.547650,3.595200,8.518570,-1.532232,3.522433,-6.444895,-5.287620,8.937720,8.490317,-6.428644,8.202570,-2.179816,8.808838,0.487200,-2.223617,8.245453,8.862992,-1.345138,-6.626617,1.588840,-9.536051,6.374813,5.921573,4.755726,5.061989,-8.558816,-2.249322,7.980733,-5.411205,-9.954583,3.513338,-1.876676,-5.060590,7.294145,5.280966,-6.124087,-2.221672,2.165806,-8.750989,1.307379,-3.921566,-4.591640,-8.411780,-5.284604,-7.412702,-8.147703,2.444637,8.537404,4.887283,-5.613269,5.666053,-8.212021,3.104732,-2.192256,3.201913,6.566332,7.865839,-0.240285,0.729216,-5.000208,2.631471,7.634854,4.541870,4.851739,-6.796627,-4.628089,-8.729369,7.630561,-4.923164,-6.950857,9.053316,0.408740,1.549817,7.959589,-6.837550,3.919661,-6.776178,-9.191487,7.211130,-0.062676,-7.023641,0.378813,6.466782,-6.006413,-8.468858,4.015045,-6.807414,-2.867657,-0.291393,-1.162081,0.232304,9.639555,-9.332349,-3.525764,4.167713,5.045954,7.770982,-8.001300,-1.633548,-8.963252,2.715922,-4.325321,-9.845822,-1.078193,-8.731021,0.631617,-5.892400,5.784945,5.210984,-6.489677,-1.164772,-4.200054,-2.511601,5.230147,7.810395,-3.799402,5.555694,-9.738167,6.304899,6.250222,6.627886,-4.477760,0.698201,-3.731552,7.254552,5.838520,8.717764,7.860403,-6.883344,-6.067470,-1.730498,3.865757,6.045016,5.304770,-2.455559,0.155356,2.840478,1.173014,9.139530,2.476029,-4.265646,8.047895,-7.847474,5.279819,2.767944,-2.349385,-7.571393,8.945786,4.397825,8.772808,7.037869,2.355660,-9.806418,9.401470,1.180490,-3.086240,7.011003,6.693411,-5.425894,1.980235,-0.339558,6.744209,2.014004,-7.819749,1.136196,-1.376431,-3.257513,8.277166,-4.733254,6.130460,-0.142526,2.401579,4.197596,3.895676,0.009338,7.818164,1.790627,4.167845,4.931398,7.451903,1.653701,-0.555045,-6.733764,-6.930676,-8.064767,-8.711235,7.294045,8.839384,-2.120304,-6.241950,6.303047,5.616028,-2.630582,6.765125,-5.176581,-8.213737,-7.026005,-5.809141,-9.052637,5.903278,-5.666513,4.277737,1.813454,-1.035041,-3.158315,1.219254,-1.833400,-7.860295,6.329111,-0.801328,-9.432915,7.203653,0.101840,9.606945,-0.824715,2.794868,-4.241164,-3.784079,3.217377,2.310277,8.569184,4.902895,3.757494,-9.679093,5.189262,7.120126,3.346940,-5.275656,-0.122247,9.611268,-9.922475,0.686036,9.760411,-1.879510,-2.593361,-3.928665,-1.107705,7.838193,7.777335,1.191296,-0.651364,4.213893,0.712598,5.952237,1.849273,9.290531,3.947982,3.495362,-5.600056,5.865164,0.365589,8.730165,0.215082,-4.669920,-1.084075,1.188925,-8.235783,8.698214,-7.704418,9.110303,3.723344,4.167124,2.819720,4.844562,-6.790425,-0.160431,0.202429,6.137765,-1.514098,1.972902,1.011873,4.760811,3.385832,-1.225668,3.585882,-5.163767,-5.975500,2.967268,-7.216755,7.542953,4.819340,-3.487693,1.166608,0.926696,1.577342,6.029522,9.942396,-4.241846,9.125219,-5.220195,-6.075379,8.824618,-2.206591,-4.584932,0.475624,6.408706,7.036150,9.409759,-3.362654,-4.315327,-5.755373,-2.338488,3.566806,-3.734325,0.644472,8.244224,4.338489,-5.723662,-5.928033,-5.721338,2.252507,-7.696424,-3.453805,0.270182,5.109061,-7.581905,9.804633,0.628198,-1.628235,3.830053,8.340003,3.870399,8.872181,-2.021834,7.109421,-9.142860,3.005892,3.758440,-4.871008,-6.949185,0.066588,1.082652,0.581940,4.214328,1.992047,-3.449709,3.548089,7.737808,3.186537,-6.659258,1.595692,8.675436,-7.155817,-6.484663,-7.865668,-7.573907,1.815403,-5.468964,-1.673073,-1.494726,2.721424,-2.958722,0.172841,1.774965,-7.701646,1.976417,-9.938370,-2.156936,4.036038,-7.135211,5.236078,3.355718,-2.082386,4.925280,2.130937,-7.712968,-5.631883,-5.825542,5.984743,2.917994,3.733775,7.140021,1.686335,-5.436177,-3.952613,-3.990828,4.795436,-9.422828,-0.662751,7.702391,-2.437831,-3.316357,-6.838167,-9.971728,-1.066473,7.406265,-8.065504,-1.493294,-7.990346,-3.663629,8.864589,-1.246920,4.751313,-0.528347,0.222934,5.351068,-6.852308,-3.063061,-9.152123,-1.490447,-4.035213,1.796313,-2.879619,9.034373,-2.791481,2.015063,-4.559835,6.125938,-7.130553,8.250572,5.709094,9.752378,-5.986343], dtype = "float32")#candidate|10269|(560,)|const|float32
call_10268 = relay.TupleGetItem(func_6435_call(relay.reshape(const_10269.astype('float32'), [8, 14, 5])), 0)
call_10270 = relay.TupleGetItem(func_6438_call(relay.reshape(const_10269.astype('float32'), [8, 14, 5])), 0)
output = relay.Tuple([call_10263,call_10268,const_10269,])
output2 = relay.Tuple([call_10264,call_10270,const_10269,])
func_10283 = relay.Function([], output)
mod['func_10283'] = func_10283
mod = relay.transform.InferType()(mod)
mutated_mod['func_10283'] = func_10283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10283_call = mutated_mod.get_global_var('func_10283')
call_10284 = func_10283_call()
output = call_10284
func_10285 = relay.Function([], output)
mutated_mod['func_10285'] = func_10285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6304_call = mod.get_global_var('func_6304')
func_6305_call = mutated_mod.get_global_var('func_6305')
call_10315 = relay.TupleGetItem(func_6304_call(), 2)
call_10316 = relay.TupleGetItem(func_6305_call(), 2)
func_9076_call = mod.get_global_var('func_9076')
func_9079_call = mutated_mod.get_global_var('func_9079')
const_10318 = relay.const([1.423928,-9.908082,-2.218314,2.333033,-2.346661,-9.907463,-1.098568,-7.917561,0.802135,1.400453,6.838955,8.888932,-2.299082,6.994720,-8.169038,3.628706,-0.792515,-0.580845,-1.149540,-7.943445,-9.060495,-8.105842,-8.062577,4.358793,8.781477,0.071826,1.929635,-1.912810,-8.615451,2.924216,6.208312,2.477409,-3.820470,-9.656114,3.400103,2.872869,-5.236342,4.985777,4.113046,-3.044060,9.810564,5.405816,-9.249083,-2.934913,-1.240703,9.698490,4.747721,9.185564,-3.463509,-5.414414,-3.970514,3.268181,1.377668,-5.692296,8.373365,8.974887,-6.190507,2.147260,-5.475975,7.401309,9.235634,1.214761,4.989375,7.467668,-7.904745,-8.601070,6.505124,5.833838,-2.391187,0.423733,-7.065403,-2.943070,-0.425325,3.824716,5.130420,0.783035,1.303409,6.633999,2.996123,-3.213945,5.666435,-9.420579,8.792798,1.215245,8.567678,9.173734,-7.707990,-8.045876,-6.002159,4.174097,3.256301,-6.145175,4.780398,3.445778,-1.135324,4.473716,-8.451670,9.152255,6.758175,4.202680,7.360887,0.826827,-4.538986,-1.268892,8.161806,2.334343,-0.812303,-0.221038,3.150246,-3.066780,6.834531,5.378883,-8.113427,9.701604,-7.856329,-4.510139,-9.284573,5.308773,-4.827162,9.389523,1.032883,-4.285638,-4.587949,-7.575139,-7.238157,-6.085905,-9.395335,-5.144856,-8.255451,-4.380312,-0.145458,-7.869238,-3.351701,-5.320495,-9.013257,2.907370,-0.205694,8.233923,-3.401995,-0.054723,0.985476,-6.245109,4.062451,-6.121241,9.834621,-2.345455,3.918143,-5.873200,-9.486102,-0.609420,-6.428203,-2.309115,2.151106,0.740422,9.970187,6.621177,-3.251474,-3.988695,-8.188224,9.432385,-1.718463,8.057824,2.787630,4.291658,-8.074455,-2.030694,4.983479,1.463417,-6.652559,-9.564988,8.351737,-2.353833,-2.526685,4.494609,0.362587,-7.564667,-7.518822,-6.347343,3.608383,0.861948,6.407583,-6.477473,-8.787963,-5.004069,-2.028655,7.237051,-3.829460,-5.993559,-1.431933,0.080380,-6.424419,7.570978,7.325353,-9.085717,-7.350234,9.589395,3.910327,-4.400879,1.698378,4.334708,-1.715506,4.677135,-2.681451,4.342170,6.300747,2.628672,-7.069895,-6.522866,-8.412449,-3.169630,-6.590721,-3.137130,9.816510,-6.863476,7.086641,-1.636041,-4.599555,-6.893117,1.359402,2.502628,-6.930535,7.782732,-2.180922,0.452856,-8.027120,4.179973,8.761138,3.854321,-8.310315,8.150777,4.964340,3.219989,-2.934481,-7.442997,0.494076,-1.192747,-8.758598,-7.588195,-6.744229,9.176623,2.911193,9.994205,3.574744,4.519243,-4.351508,1.329383,5.285374,9.442907,1.760352,0.340686,-2.405668,-7.955890,4.778685,1.482684,-3.364781,0.437498,7.998274,-6.294334,2.092307,-6.520438,7.796706,0.873203,7.966427,-1.793567,-8.315061,4.213796,0.004742,-8.240666,7.579008,-3.603278,-3.622613,4.327413,5.632529,-8.058715,-2.282517,-7.516407,8.448878,-7.846112,3.336919,7.434746,-7.514566,-6.800484,-3.642504,9.237030,-6.392941,-3.155943,5.576048,-5.841010,1.483266,6.326660,8.150098,2.502804,8.219069,0.126268,-0.002335,-3.184133,-1.819258,7.289614,1.302712,-6.352594,-1.277268,6.558194,-1.129415,-0.398239,-9.567553,1.621177,-9.733907,-2.431406,-5.687319,-4.309530,-7.513379,-9.211897,6.843385,-1.936373,-0.232420,-7.522500,2.608365,-7.971940,2.359437,9.795237,-1.488844,4.510039,-5.552120,-5.660458,-0.676936,6.441876,8.966463,7.800267,2.989986,-1.737845,-9.746037,7.349962,-2.291066,2.822475,-9.453919,5.470128,-8.983131,2.688393,5.242771,6.816306,-4.737121,-5.490138,-1.989324,-7.679173,2.534155,9.890476,8.001761,4.525825,-1.790508,0.149668,-9.874163,8.844717,-7.686800,5.106819,-9.033660,9.580531,8.002218,2.789776,3.558987,-6.754012,-1.233288,-2.822309,-3.337455,2.681759,-0.855124,7.804915,9.183641,3.933719,-3.560392,0.677073,-3.557300,4.586356,7.605759,1.183867,0.650394,0.398160,-6.412870,4.460355,-9.684377,5.608213,-2.056618,0.235662,-3.765100,8.669984,5.000629,5.241365,8.195662,2.672989,2.822794,2.407403,-2.112775,-2.501218,-8.832845,3.457662,-9.851705,1.191066,-8.786661,8.571523,-3.041475,8.723952,1.489593,4.616682,2.246615,1.099051,2.206721,4.010588,-0.241743,-0.400326,-7.738123,3.350939,5.085779,4.132374,7.659838,-9.655613,5.489632,4.167014,-9.525099,6.330281,0.471850,5.974534,9.196591,0.127771,-4.293679,-3.218265,3.104642,-4.696283,-3.615874,-5.976103,-3.240887,8.947371,-2.639956,-0.397403,1.406890,7.800728,6.311259,-1.208187,6.993240,-0.319277,4.677564,-4.004203,-9.298274,8.105785,-7.099721,-3.621003,-0.113626,-4.554488,-2.042105,-1.416234,-6.098893,-7.333156,-7.592956,-4.104392,-0.347872,6.227452,0.127699,6.733108,-6.782341,3.560570,-0.589056,5.419321,8.130702,-6.564075,6.837204,-6.570462,-6.463108,0.524157,5.810323,-2.568804,-5.416855,8.933629,-1.816846,3.565840,-4.646764,0.619087,-4.488459,0.546925,1.012914,7.870190,-8.402209,-0.647611,-1.035686,9.416477,-5.336013,-9.090473,-2.302239,-0.926746,-0.297012,1.788296,-2.226369,4.084705,-3.411859,4.318015,-0.537748,-0.938920,-0.456477,0.211566,-0.003952,-9.360756,4.851332,6.879854,-8.947574,-9.084939,3.088793,1.909352,-6.159599,-3.905394,-0.711304,-3.779986,-0.421198,8.926847,-5.404316,9.490662,-9.611915,5.083350,-7.481307,9.599195,-7.906691,7.914810,0.521554,-9.262506], dtype = "float32")#candidate|10318|(520,)|const|float32
call_10317 = relay.TupleGetItem(func_9076_call(relay.reshape(const_10318.astype('float32'), [8, 13, 5])), 1)
call_10319 = relay.TupleGetItem(func_9079_call(relay.reshape(const_10318.astype('float32'), [8, 13, 5])), 1)
func_10036_call = mod.get_global_var('func_10036')
func_10039_call = mutated_mod.get_global_var('func_10039')
const_10337 = relay.const([-9.109024,-7.460099,-7.109630,2.869370,0.323869,7.367152,1.999801,-7.892719,3.289068,8.511562,8.612561,-5.675401,-3.272731,6.562269,-8.328703,-6.091786,-1.456411,-0.809403,-3.918637,-9.048582,0.263054,8.399605,-1.349446,5.520407,-3.862714,-2.137745,-8.030261,-3.048106,-6.617941,-3.672611,2.209268,7.704582,2.556967,-4.135236,-6.802868,-4.535139,2.288352,-8.290134,5.188657,0.958296,-6.512776,3.271188,1.117009,9.585569,2.952297,-5.519080,3.997097,7.911039,7.725015,-2.309786,-3.497824,8.432954,-3.738017,0.662281,2.759621,1.484411,5.194788,-2.307666,9.560162,-1.600320,1.167878,5.306532,-7.517371,-8.484723,-0.481792,0.896941,2.731552,-5.034892,-1.996144,6.422124,2.480035,2.396256,9.261087,4.189497,-5.419475,-9.563664,-5.179067,-9.431439,-0.284633,3.471047,8.797359,1.107592,5.055313,-9.048135,-6.514503,-6.000823,-5.298319,-1.651622,6.953946,-9.232801,4.669586,-9.691937,-1.847633,-6.177740,4.858002,-1.091458,5.005037,6.914921,0.692577,-4.718048,6.975224,5.781372,1.987968,6.879727,1.915630,-1.057265,-9.250958,2.270623,4.945193,3.135518,1.593025,0.440569,-4.309339,1.796975,-5.007284,5.952088,-1.297241,8.121355,-3.704544,7.499798,9.144354,-2.873891,-0.642241,-8.747310,4.538601,-5.487621,3.632281,5.710521,-4.110187,-0.606815,1.352982,-4.683151,-5.867453,6.506957,-3.923811,8.054598,-9.727377,-0.220003,0.738660,-0.311512,-5.939403,8.688015,-4.166629,2.205755,8.284074,3.401711,4.596948,4.722387,2.340484,-8.100923,1.295419,1.296478,3.506331,-0.388604,1.024279,-7.258327,3.814835,2.477493,-1.918351,-0.165133,-6.184381,-8.157567,7.504912,-4.963518,-4.812614,-6.765673,-9.567695,7.327125,9.731929,-5.241641,-1.314699,3.595235,-8.488896,7.535917,2.748536,-0.646096,9.323261,-5.489543,-8.439761,-8.196984,4.075173,-6.044361,-0.462358,-1.505897,2.229884,-6.865680,8.222752,6.287749,7.130619,-0.691670,-2.393218,-7.725690,-2.115639,-8.361360,8.468697,5.099756,-8.101653,-4.690534,-0.246882,-8.995667,3.172340,8.891160,-8.497333,-5.216744,-3.385274,1.421270,-7.920304,-3.602564,-7.901312,5.344208,7.563909,-0.254889,6.413638,6.646797,2.836231,6.517684,-8.070858,0.802313,-5.458199,-5.757416,7.229616,8.078200,-1.043726,-5.182434,7.707975,-1.991289,-8.866257,-5.655557,-5.237834,3.816076,3.575359,-4.668104,-0.415373,5.458025,-8.103086,1.854624,7.856231,9.224967,-1.610910,-9.860044,9.643875,2.567955,0.117071,2.883236,5.634795,-5.526394,-4.043116,-6.137600,-2.320382,5.840163,-8.594085,-6.736490,2.627172,4.973710,9.400613,1.395377,-8.943130,8.485862,-0.830423,0.396063,0.552071,1.291963,9.992206,-0.048057,0.328332,-6.674701,-3.487779,9.130409,-8.773806,-1.381279,-7.932009,-9.267406,-6.829106,-4.700868,2.977805,-7.066565,1.577405,-2.572739,0.609453,6.608511,-9.456385,-5.558095,-5.541915,-1.081908,-4.993146,5.426840,3.180515,-5.959911,4.961566,-5.421854,-5.232370,5.550913,-7.171317,-3.082747,4.222389,-1.471980,2.214589,-6.887975,-7.508391,-8.715104,2.031492,7.783613,-6.495964,-0.939915,5.528782,-7.874733,0.290186,9.945644,8.777346,-4.551935,3.118069,-2.376323,6.024486,8.980198,3.462445,6.895069,0.433571,5.079546,-8.193204,4.821839,0.314298,3.953548,3.707981,-9.635706,6.936723,3.168710,-3.062125,3.483979,8.538973,0.896850,5.481740,5.169497,-6.655542,-7.414640,6.428786,-2.650421,3.095685,7.400382,-8.322432,9.843868,-2.686401,1.937196,-5.473246,1.748664,4.215641,-2.693373,9.757947,0.928460,2.977017,-8.164561,4.491261,6.520103,-1.537638,8.259692,-7.327813,-5.122606,-4.806162,2.895120,3.009824,-2.265365,-2.947984,6.050040,-4.059986,3.398565,-0.523822,-2.631577,-0.124180,-0.909847,4.272091,0.005802,-8.720255,-7.022899,5.623677,5.129588,-9.638254,3.940525,-3.658503,-4.053309,6.133120,-2.735273,7.428118,5.776615,-4.809679,3.338224,-9.250256,-8.378152,-4.226476,9.942002,-5.878340,-0.094259,-6.444509,7.374330,-7.245638,7.935451,8.874798,2.428640,4.455212,-8.462690,-8.223753,9.571761,0.935758,3.434821,-6.549456,7.110695,6.472936,-8.271360,-9.837010,7.745219,9.348437,-6.329226,-1.800630,-6.839030,5.783569,-1.969811,-7.186757,-0.775681,8.146930,6.366219,-8.331343,-5.337830,8.226804,5.301763,7.421929,-2.397712,8.997766,8.774262,3.101578,7.384410,1.821812,-1.864754,7.517839,3.754666,4.205990,6.150418,5.075805,8.883890,-9.835575,-5.323948,5.422477,-6.721978,-7.548682,3.114198,9.385411,-7.173079,-9.667192,-0.384553,3.270601,-5.832215,4.429415,-2.284965,0.120327,8.604164,-9.156728,3.469815,-7.473918,-8.538695,-1.576716,-6.638830,8.225331,-5.278735,-3.207484,3.041854,-6.421715,-7.437484,2.390370,-0.069793,-5.136657,-4.133170,-1.358871,8.155814,-3.451793,9.449697,0.008794,-9.729593,-7.653159,-1.058891,-9.744995,-9.301488,5.121801,-6.847937,8.716360,9.192644,-6.826718,-4.030874,-4.194266,3.173946,0.080007,0.132811,7.824476,7.580717,-2.761021,-1.958993,-0.205257,6.578193,9.615602,-0.457393,-0.239891,-1.326687,-3.480103,2.000407,-2.207628,1.252095,9.113090,-1.990381,-0.512199,-9.609167,0.190642,1.695504,0.843890,8.751568,-1.382606,4.990829,-1.601828,7.963817,-4.980409,3.320846,-9.546274,7.639600,2.316769,-3.622847,0.307989,-6.021983,7.000863,-2.471174,-5.971671,9.619607,-6.725838,1.452834,-5.521508,9.712728,-9.451268,-4.364886,3.445861,-4.352303,6.282288,-1.009305,-4.542724,-6.431106,2.248157,-2.026749,-6.557412,-9.615786,8.713790,0.206154,2.533975,-1.647948,2.629885,-2.255807,-3.615191,9.519200,0.558687,8.282635,-0.949352,3.181837,-6.375947,4.715654,0.370759,5.490860,-8.287158,-7.235425], dtype = "float32")#candidate|10337|(560,)|const|float32
call_10336 = relay.TupleGetItem(func_10036_call(relay.reshape(const_10337.astype('float32'), [560,])), 0)
call_10338 = relay.TupleGetItem(func_10039_call(relay.reshape(const_10337.astype('float32'), [560,])), 0)
func_3778_call = mod.get_global_var('func_3778')
func_3780_call = mutated_mod.get_global_var('func_3780')
call_10341 = relay.TupleGetItem(func_3778_call(relay.reshape(call_10315.astype('float32'), [1134,])), 2)
call_10342 = relay.TupleGetItem(func_3780_call(relay.reshape(call_10315.astype('float32'), [1134,])), 2)
output = relay.Tuple([call_10315,call_10317,const_10318,call_10336,const_10337,call_10341,])
output2 = relay.Tuple([call_10316,call_10319,const_10318,call_10338,const_10337,call_10342,])
func_10345 = relay.Function([], output)
mod['func_10345'] = func_10345
mod = relay.transform.InferType()(mod)
mutated_mod['func_10345'] = func_10345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10345_call = mutated_mod.get_global_var('func_10345')
call_10346 = func_10345_call()
output = call_10346
func_10347 = relay.Function([], output)
mutated_mod['func_10347'] = func_10347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9008_call = mod.get_global_var('func_9008')
func_9010_call = mutated_mod.get_global_var('func_9010')
call_10402 = relay.TupleGetItem(func_9008_call(), 0)
call_10403 = relay.TupleGetItem(func_9010_call(), 0)
output = call_10402
output2 = call_10403
func_10412 = relay.Function([], output)
mod['func_10412'] = func_10412
mod = relay.transform.InferType()(mod)
output = func_10412()
func_10413 = relay.Function([], output)
mutated_mod['func_10413'] = func_10413
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10451 = relay.const([[[-0.840920,6.985440,5.542834,-8.549096,0.165589,-9.724098,6.000881,2.364009,-2.527036,-4.299526,-1.411611,6.927025,3.446441],[-7.801361,-6.529095,6.024229,2.285860,0.106219,4.982142,9.307214,8.874194,-7.155170,2.588745,4.149152,-9.072841,3.237622],[7.131475,-4.031288,9.880002,0.713948,1.558217,-3.428530,1.027746,9.143270,-6.951996,7.662929,-2.310092,-4.319679,-2.614313],[6.869468,7.720260,4.617454,4.021077,-3.531705,-5.185357,-1.999777,-3.958389,-6.242544,-1.017834,-1.856184,-8.813850,9.664099],[4.909600,-7.332983,8.110552,-8.944673,4.156324,3.770260,0.064997,6.986985,1.464950,7.359305,-6.578659,0.895293,0.698514],[1.097030,-3.011019,-8.690750,-3.655399,4.435398,-4.991086,0.782050,0.177818,8.874168,-3.479469,-9.900825,-8.786361,0.659586]],[[-9.353838,-0.114900,-4.397511,1.255936,-0.450831,-5.096888,7.452211,-6.448185,4.122555,8.499831,0.915331,1.740044,4.913289],[2.456248,-9.219065,-9.733305,-8.617922,-7.656737,2.550132,9.394303,-2.409440,-3.181345,8.070963,8.225682,-4.302515,6.235467],[8.743074,6.035786,-7.860281,9.407104,7.056958,4.582715,-3.936820,-6.494155,-8.183918,0.502650,9.694715,-3.336857,-3.606645],[8.419840,-2.611966,-7.435248,-7.287502,-8.627886,6.405662,7.016978,6.851767,-6.540909,-6.941984,9.139618,-8.065855,8.623602],[1.404932,-7.244762,-7.282853,-6.036954,-2.864781,-8.171451,7.905089,5.751515,-4.316364,3.488016,-4.622517,0.396707,8.426591],[2.770282,2.352878,8.183592,-6.423869,6.249094,-7.077496,8.481300,-3.442840,4.384714,-8.013898,-1.244769,0.009999,-0.532494]],[[2.032826,-7.216584,3.596152,-9.508952,0.788322,5.098129,0.423449,-3.521519,-6.109448,-6.734996,8.192398,-0.286388,6.986766],[1.869725,4.539438,-3.799398,8.573257,7.413108,-6.022316,-4.720908,6.727332,1.472482,-3.206444,-4.916824,1.262300,9.407782],[-6.923758,-0.681727,9.670994,-4.983329,7.283152,7.355021,-4.792287,3.623245,8.374215,-9.156795,1.171268,7.665789,1.692640],[2.673130,7.468904,1.716562,-8.331135,3.263229,3.861610,-9.007781,-7.069789,-0.083854,-4.539571,9.854577,1.032533,2.893459],[8.515324,-4.492101,-2.553468,1.789565,-8.175686,-6.811063,-3.151702,-6.439670,0.625446,-3.993066,3.415094,-2.734492,9.024751],[2.428554,3.111567,7.951544,3.316710,9.236034,6.260702,7.198603,-7.978427,6.150091,1.650273,-1.132519,-2.615838,-9.711930]],[[9.009627,-7.604389,-0.792606,2.507841,-1.835843,-0.127317,-8.632327,0.362853,-8.944697,-2.719367,-3.490048,6.721442,6.644820],[0.539669,0.824185,2.061999,-9.635843,2.356906,4.749703,5.371339,5.091940,-2.620060,3.569901,-9.124218,-2.110616,-7.201841],[-4.585314,3.564017,-5.943465,3.890027,-7.574544,-1.294612,-3.020665,-9.484663,4.669122,9.208247,4.579572,-1.144554,-7.193148],[1.365765,5.371849,7.628455,4.777663,-8.491906,5.474243,9.074269,-9.557808,6.348528,9.344702,1.454148,0.231218,-5.001159],[-4.696250,1.125184,7.345382,3.412093,8.055549,-1.030114,7.837639,-5.283490,-7.945807,5.498038,9.152921,-8.624258,-4.096359],[9.523617,-1.413214,-0.158326,2.372236,1.475398,-3.046868,0.336108,-4.976139,4.288257,-3.333349,-6.177055,8.223605,-4.864695]],[[-8.984034,-7.383237,-7.217213,-9.160953,8.765191,0.686635,3.412409,4.884880,2.267247,7.003122,-4.880662,-3.126875,-6.871293],[6.810800,-2.976167,-5.181348,-1.235351,1.141754,7.112222,-1.491413,-0.904495,8.796271,-0.523235,-1.746644,6.214698,3.004094],[-2.728219,7.022765,4.569982,-3.407918,-1.073358,-2.482159,8.183557,3.101326,-3.270870,8.974224,5.713919,-0.233265,5.037979],[1.051793,-4.591698,-8.326747,-9.112276,8.441694,5.476412,7.607860,-9.464959,-2.825770,3.586769,-2.797977,7.782718,9.303394],[-7.868928,0.450999,-9.809784,7.930445,9.094831,5.884165,8.931567,0.449361,-1.085355,-0.406532,0.337239,7.806917,-0.184144],[-8.169279,7.591797,-8.048363,3.365108,-7.863047,-1.493135,-2.489709,3.184778,-8.145494,-9.430787,6.354733,-4.322677,5.926856]],[[2.436587,6.889294,4.651485,8.275847,8.670661,-2.518110,2.978092,-0.075513,-9.808666,-5.963866,-6.511525,-1.511828,-2.656989],[8.769268,6.162688,-1.490339,7.050556,-2.424325,7.026555,-3.059794,4.528153,3.573388,7.823704,1.633721,-7.957175,3.341969],[-3.367024,6.332913,-6.746142,9.665048,-7.022917,-6.446072,7.087358,-0.048043,-2.684983,7.844956,5.424412,3.483309,-5.148112],[9.727320,-9.402797,1.832944,-1.062714,4.195248,-5.770662,3.648642,2.230144,-0.486576,-6.793379,8.752365,1.876215,0.061245],[-3.157817,0.138303,6.319977,8.909932,-7.167585,-7.645076,-9.942660,9.345658,-3.491367,6.434504,-1.462303,2.003298,-0.241950],[4.952059,8.936976,-6.980239,4.162185,7.574536,-1.072305,-9.486584,7.474076,-4.693278,6.370920,-2.124641,-5.906086,3.537151]],[[-5.017322,0.637500,6.503172,-0.470932,0.560157,-9.106643,3.442897,8.054827,8.418633,-3.286179,-4.066270,-6.433867,-1.219366],[-1.362318,-1.191849,1.320439,-5.292052,8.570223,3.831756,-3.476005,-4.481542,-6.289307,-4.039773,-9.925888,2.113186,2.648235],[2.865183,8.200594,-1.467855,-3.896475,0.256384,4.282981,-0.267156,-0.852396,3.653151,7.249238,1.868706,2.209365,2.161166],[2.045777,-3.864453,6.709681,-7.368069,2.676308,-0.329432,3.903163,3.982543,6.861470,1.495235,7.103578,-8.174826,8.026825],[-5.774074,-6.940918,-9.667559,1.020511,-8.370242,-7.740109,9.124988,2.716056,4.259205,-9.039086,-2.866488,-7.777286,5.029188],[-9.950044,-2.721198,2.562544,-1.221933,8.579139,-4.316850,4.700507,8.799015,7.533870,8.080308,-8.951665,-9.291359,1.778154]],[[-4.839970,-7.871357,1.217892,0.101714,-6.657775,1.999620,-7.177328,9.744898,9.420036,2.951113,-1.475783,0.564270,-4.771067],[-9.537977,-9.722407,0.433643,-5.375769,-3.262491,-1.489131,8.787344,4.647367,0.624814,7.280810,-5.184900,6.015922,1.007849],[-1.818688,7.174238,-8.743743,5.127777,3.629014,3.538575,7.037136,3.515172,-9.360681,-7.270224,3.517004,7.684169,2.030807],[0.103176,-9.400712,-8.264486,-6.017633,6.380394,-0.148588,4.582489,2.812454,3.903090,6.952011,-0.038782,0.173668,1.419053],[-9.502022,-3.143351,-6.823565,-2.327148,-9.304798,0.765428,-3.153776,-4.248784,-1.613822,-9.731662,-4.677470,-3.409409,-9.514180],[6.665285,1.576595,6.187687,-0.798330,9.858865,8.243056,2.785058,6.213775,-1.044114,0.682303,-7.291328,8.043302,9.565025]],[[-4.368371,5.912585,-6.228821,-7.596415,6.317857,7.759401,6.433930,-8.112122,-5.203023,0.912839,-7.512624,1.810834,-7.501131],[4.833353,-0.177640,5.419399,-1.347859,4.009113,-8.627281,6.948168,6.315506,8.407449,8.790864,-9.150345,9.260073,6.667376],[2.944322,0.039888,-6.991401,0.957183,4.649342,2.151869,3.363685,-5.306711,0.729849,2.169909,-6.157327,1.096316,-9.755930],[0.265883,9.556611,-9.337916,0.447376,-8.636708,-7.401181,-7.672697,2.106891,-4.871330,-5.055646,-1.521078,-5.935550,2.205154],[-7.768374,-9.507527,-1.233074,-5.105548,2.548770,-6.518667,-5.743630,-2.191893,1.819987,-7.326057,0.637851,5.477507,8.345472],[4.895921,-6.185301,-2.922006,9.274609,5.081185,-1.519989,-4.209689,-2.679389,-0.308384,2.679313,-8.351424,6.831109,2.701743]],[[3.764561,-0.346389,-5.496237,-6.949580,-5.544885,4.033530,6.567688,5.169709,-8.695335,9.559573,6.853374,8.811837,7.341560],[0.916660,-7.157804,4.080143,2.769194,-9.525426,9.483372,-0.310297,5.198712,4.484423,2.722353,-2.174653,-6.358530,-3.900467],[5.743401,9.591207,6.634974,1.358772,9.109355,4.729607,8.245570,3.869578,-1.489936,-6.479268,4.133355,4.452832,7.083560],[3.811392,1.932881,0.258552,2.957293,9.942411,0.089368,7.382330,9.463464,4.667722,-6.847246,0.310229,2.681827,8.862337],[-3.942546,6.610280,-3.381961,6.253649,-2.719966,6.502597,4.030064,0.261467,2.942692,-7.592313,5.167747,8.257195,-3.150359],[8.386207,0.575836,-9.633821,8.767296,4.422327,-8.197332,6.383868,9.081826,0.963305,-1.378433,3.524531,4.234215,-1.314278]],[[4.467635,-8.632040,1.582850,8.817169,-5.114660,-9.379386,8.768733,-4.689363,-4.022691,0.265369,-4.040780,1.477549,5.529552],[-8.373983,-4.623514,6.989201,9.352487,9.031215,4.056209,7.922654,-2.745829,7.764389,5.281507,-7.281955,-3.613923,8.477369],[-3.376800,0.798181,7.469045,-8.964323,-8.434223,5.605696,3.082130,-3.588550,-0.040779,4.663834,0.883539,-6.907691,-1.884500],[4.236548,-3.345998,5.617834,3.171057,-4.835834,-8.936331,-1.187898,7.673694,-9.316028,-4.110214,1.108331,-5.020387,8.634775],[-3.184135,-3.541190,-7.892736,5.993930,-4.177059,7.751722,3.833071,-0.910616,-2.692477,-2.090563,3.651844,4.640285,-7.997826],[-4.249533,6.326619,-6.676434,8.951710,-7.463247,-1.562883,4.792859,-5.743597,-8.904057,-1.206969,1.649315,4.763541,-6.954333]],[[1.626010,-9.268576,8.523585,-8.842485,5.471303,-1.449183,-1.504472,-4.079862,-2.126928,7.599672,6.930267,-9.798958,8.674358],[-3.009768,5.198441,6.194795,-4.971654,-8.529527,-1.601143,-9.233753,-6.609286,-7.599149,3.680335,1.075059,-4.281527,-3.093235],[1.611120,-8.075263,9.164570,8.919576,3.613669,1.043229,6.801689,7.174291,-3.754051,0.072610,-3.676310,6.130828,-3.798006],[3.719639,-4.488228,-6.590040,-0.333997,-9.290527,-9.475040,1.465299,-4.944213,2.948530,-1.045109,8.579174,5.269807,2.558126],[-7.315264,2.754088,-6.283856,-7.915514,4.374615,-1.351584,0.068663,2.174081,-9.948771,2.487118,2.747773,-3.908055,-1.054197],[-9.803258,-7.721827,6.905767,7.727874,-8.212200,-3.643767,-1.748998,5.434748,1.093615,2.942415,-8.341909,6.699985,-0.385351]],[[1.583811,3.878394,-2.414670,9.178636,5.938919,0.860379,2.424642,-3.081068,-7.206092,9.867121,9.538251,-0.960785,8.125896],[8.063413,2.836212,8.021673,-9.725547,-4.149640,1.779690,-7.670966,-3.308953,5.594081,1.886832,0.872012,-9.304045,1.661224],[-8.097986,-5.005154,4.069119,-7.371493,5.935247,1.325089,-9.774736,-9.185930,6.434714,4.352608,-8.018118,1.299797,-7.283612],[-3.426385,-6.075366,8.163249,3.880842,-9.996066,0.415327,4.345077,5.534833,-9.280887,-1.432410,1.872267,9.495938,-8.888393],[5.343425,2.698170,-6.352668,-2.230713,-2.907203,6.731045,9.492776,-4.885684,5.936952,3.591387,-9.277384,-1.624820,-6.443803],[-4.611566,-5.076178,6.674776,-2.377318,-0.801559,-8.982240,1.258261,-0.699156,8.112740,4.558039,-6.685184,1.596821,3.475234]]], dtype = "float64")#candidate|10451|(13, 6, 13)|const|float64
uop_10452 = relay.log10(const_10451.astype('float64')) # shape=(13, 6, 13)
output = uop_10452
output2 = uop_10452
func_10460 = relay.Function([], output)
mod['func_10460'] = func_10460
mod = relay.transform.InferType()(mod)
output = func_10460()
func_10461 = relay.Function([], output)
mutated_mod['func_10461'] = func_10461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8093_call = mod.get_global_var('func_8093')
func_8094_call = mutated_mod.get_global_var('func_8094')
call_10475 = func_8093_call()
call_10476 = func_8093_call()
func_7674_call = mod.get_global_var('func_7674')
func_7675_call = mutated_mod.get_global_var('func_7675')
call_10477 = relay.TupleGetItem(func_7674_call(), 0)
call_10478 = relay.TupleGetItem(func_7675_call(), 0)
output = relay.Tuple([call_10475,call_10477,])
output2 = relay.Tuple([call_10476,call_10478,])
func_10480 = relay.Function([], output)
mod['func_10480'] = func_10480
mod = relay.transform.InferType()(mod)
output = func_10480()
func_10481 = relay.Function([], output)
mutated_mod['func_10481'] = func_10481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9967_call = mod.get_global_var('func_9967')
func_9968_call = mutated_mod.get_global_var('func_9968')
call_10495 = relay.TupleGetItem(func_9967_call(), 0)
call_10496 = relay.TupleGetItem(func_9968_call(), 0)
output = call_10495
output2 = call_10496
func_10501 = relay.Function([], output)
mod['func_10501'] = func_10501
mod = relay.transform.InferType()(mod)
mutated_mod['func_10501'] = func_10501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10501_call = mutated_mod.get_global_var('func_10501')
call_10502 = func_10501_call()
output = call_10502
func_10503 = relay.Function([], output)
mutated_mod['func_10503'] = func_10503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4096_call = mod.get_global_var('func_4096')
func_4098_call = mutated_mod.get_global_var('func_4098')
call_10511 = func_4096_call()
call_10512 = func_4096_call()
output = call_10511
output2 = call_10512
func_10524 = relay.Function([], output)
mod['func_10524'] = func_10524
mod = relay.transform.InferType()(mod)
mutated_mod['func_10524'] = func_10524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10524_call = mutated_mod.get_global_var('func_10524')
call_10525 = func_10524_call()
output = call_10525
func_10526 = relay.Function([], output)
mutated_mod['func_10526'] = func_10526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10524_call = mod.get_global_var('func_10524')
func_10526_call = mutated_mod.get_global_var('func_10526')
call_10548 = func_10524_call()
call_10549 = func_10524_call()
output = relay.Tuple([call_10548,])
output2 = relay.Tuple([call_10549,])
func_10572 = relay.Function([], output)
mod['func_10572'] = func_10572
mod = relay.transform.InferType()(mod)
output = func_10572()
func_10573 = relay.Function([], output)
mutated_mod['func_10573'] = func_10573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_10600 = relay.TupleGetItem(func_4065_call(), 0)
call_10601 = relay.TupleGetItem(func_4066_call(), 0)
output = relay.Tuple([call_10600,])
output2 = relay.Tuple([call_10601,])
func_10623 = relay.Function([], output)
mod['func_10623'] = func_10623
mod = relay.transform.InferType()(mod)
output = func_10623()
func_10624 = relay.Function([], output)
mutated_mod['func_10624'] = func_10624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5545_call = mod.get_global_var('func_5545')
func_5546_call = mutated_mod.get_global_var('func_5546')
call_10728 = func_5545_call()
call_10729 = func_5545_call()
output = call_10728
output2 = call_10729
func_10731 = relay.Function([], output)
mod['func_10731'] = func_10731
mod = relay.transform.InferType()(mod)
output = func_10731()
func_10732 = relay.Function([], output)
mutated_mod['func_10732'] = func_10732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7722_call = mod.get_global_var('func_7722')
func_7723_call = mutated_mod.get_global_var('func_7723')
call_10736 = relay.TupleGetItem(func_7722_call(), 2)
call_10737 = relay.TupleGetItem(func_7723_call(), 2)
output = call_10736
output2 = call_10737
func_10747 = relay.Function([], output)
mod['func_10747'] = func_10747
mod = relay.transform.InferType()(mod)
output = func_10747()
func_10748 = relay.Function([], output)
mutated_mod['func_10748'] = func_10748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7254_call = mod.get_global_var('func_7254')
func_7256_call = mutated_mod.get_global_var('func_7256')
call_10842 = relay.TupleGetItem(func_7254_call(), 0)
call_10843 = relay.TupleGetItem(func_7256_call(), 0)
output = call_10842
output2 = call_10843
func_10863 = relay.Function([], output)
mod['func_10863'] = func_10863
mod = relay.transform.InferType()(mod)
output = func_10863()
func_10864 = relay.Function([], output)
mutated_mod['func_10864'] = func_10864
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10893 = relay.var("var_10893", dtype = "float64", shape = (1, 3, 9))#candidate|10893|(1, 3, 9)|var|float64
uop_10894 = relay.acos(var_10893.astype('float64')) # shape=(1, 3, 9)
output = uop_10894
output2 = uop_10894
F = relay.Function([var_10893,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10893,], output2)
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
