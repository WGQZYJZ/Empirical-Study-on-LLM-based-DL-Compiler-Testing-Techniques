import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_26 = relay.const([[[True,True,True,True,True,True,True],[True,False,True,False,False,True,False],[True,False,True,False,False,False,True],[True,False,True,False,True,False,False],[False,False,True,True,True,False,False],[True,True,True,False,True,False,False],[True,True,True,False,True,False,True],[False,False,False,True,False,True,True],[False,False,False,False,False,True,True]],[[False,True,True,True,False,False,True],[True,False,False,False,True,True,False],[True,True,True,True,False,True,False],[False,True,False,False,True,False,False],[True,True,True,True,False,False,False],[False,False,False,True,False,False,True],[False,True,True,True,False,True,False],[False,False,False,True,True,False,True],[False,False,False,False,True,True,True]],[[True,False,False,True,False,False,False],[True,False,True,True,True,True,False],[True,False,False,False,False,False,True],[False,True,False,False,True,False,False],[True,False,False,False,False,False,False],[False,False,False,True,False,False,False],[True,True,False,False,True,False,False],[True,True,True,True,False,False,False],[True,False,False,False,False,False,True]],[[False,False,True,True,False,True,False],[False,True,True,True,False,True,False],[True,False,False,True,True,False,False],[True,False,False,False,False,True,True],[True,True,False,True,False,True,False],[False,False,True,True,False,False,False],[False,True,False,False,True,True,True],[False,True,True,True,True,False,False],[True,True,True,False,False,True,False]],[[False,False,False,True,False,True,False],[False,True,False,True,True,True,True],[False,False,False,True,True,True,False],[False,True,False,True,False,True,False],[True,False,False,True,False,False,False],[True,False,False,True,True,True,False],[False,False,True,True,False,True,False],[True,True,False,True,False,True,False],[True,False,False,False,True,False,True]],[[True,True,False,False,True,False,False],[False,True,False,True,True,False,False],[True,True,False,False,False,False,True],[True,True,False,False,False,False,False],[True,True,True,False,False,True,True],[True,False,True,True,True,True,False],[True,True,False,False,True,False,True],[True,True,False,False,False,False,False],[False,True,False,True,False,False,False]],[[False,True,True,True,True,False,False],[True,True,True,False,True,True,False],[False,False,True,True,True,False,False],[True,False,False,False,True,True,True],[True,True,True,True,False,False,False],[False,False,True,True,False,False,True],[True,True,True,True,True,True,False],[False,True,False,False,True,True,False],[True,False,True,False,True,True,False]],[[True,True,False,True,False,True,False],[False,True,True,True,True,True,False],[False,False,False,True,True,True,True],[False,False,True,True,False,False,False],[True,True,False,False,True,False,False],[True,False,False,True,True,False,False],[False,True,False,True,True,False,False],[False,True,True,False,True,False,False],[True,False,False,False,False,False,True]],[[True,False,True,False,False,True,True],[False,True,True,False,False,True,True],[True,True,True,True,True,False,False],[False,False,False,False,True,False,False],[True,False,True,False,False,False,False],[True,False,True,True,True,False,True],[False,True,True,True,False,False,True],[True,True,True,False,True,True,False],[False,True,False,True,True,False,True]],[[True,False,True,False,False,False,True],[False,False,True,False,True,False,True],[False,False,False,True,True,True,True],[True,False,True,True,True,False,True],[False,False,False,False,False,False,False],[True,False,False,True,True,True,True],[False,True,False,False,True,True,False],[True,False,True,False,True,True,True],[False,True,False,True,True,True,True]],[[True,True,True,False,True,True,True],[False,False,False,True,True,True,True],[True,False,True,False,False,True,False],[True,False,True,False,True,False,True],[False,True,False,True,False,True,False],[True,True,True,False,True,False,True],[True,True,False,False,True,False,False],[True,True,False,True,True,True,True],[False,True,False,False,False,False,True]],[[False,True,True,False,False,True,False],[False,True,True,True,False,True,True],[True,True,True,False,False,True,True],[True,False,False,True,False,False,True],[False,False,True,True,False,False,True],[False,True,True,False,False,False,True],[False,True,False,True,True,True,False],[True,False,True,True,True,False,False],[True,False,False,True,True,True,False]],[[True,True,True,True,True,False,False],[True,False,True,False,False,False,True],[True,True,True,False,False,True,True],[True,True,False,False,True,False,True],[False,True,False,True,False,True,True],[True,False,True,True,False,False,True],[False,False,False,True,False,False,False],[False,True,True,True,False,True,True],[True,True,False,False,False,False,True]]], dtype = "bool")#candidate|26|(13, 9, 7)|const|bool
var_27 = relay.var("var_27", dtype = "bool", shape = (13, 9, 7))#candidate|27|(13, 9, 7)|var|bool
bop_28 = relay.logical_or(const_26.astype('bool'), relay.reshape(var_27.astype('bool'), relay.shape_of(const_26))) # shape=(13, 9, 7)
uop_45 = relay.acos(const_26.astype('float32')) # shape=(13, 9, 7)
output = relay.Tuple([bop_28,uop_45,])
output2 = relay.Tuple([bop_28,uop_45,])
func_47 = relay.Function([var_27,], output)
mod['func_47'] = func_47
mod = relay.transform.InferType()(mod)
mutated_mod['func_47'] = func_47
mutated_mod = relay.transform.InferType()(mutated_mod)
var_48 = relay.var("var_48", dtype = "bool", shape = (13, 9, 7))#candidate|48|(13, 9, 7)|var|bool
func_47_call = mutated_mod.get_global_var('func_47')
call_49 = func_47_call(var_48)
output = call_49
func_50 = relay.Function([var_48], output)
mutated_mod['func_50'] = func_50
mutated_mod = relay.transform.InferType()(mutated_mod)
const_88 = relay.const([[[-6.955526,-8.198847,5.745473,3.933513,8.867476],[5.234352,-2.291969,5.545827,-0.875197,5.343803],[0.111371,8.391530,-0.705022,-8.254893,-3.118938],[-2.997257,-9.304653,1.231344,-3.098910,-8.751240],[-2.272941,-0.265251,5.410048,0.894975,-3.538918]],[[8.697424,-3.282692,-4.045571,9.927771,-1.702835],[-0.566802,8.531131,-8.936691,-8.299310,0.994305],[-9.802086,-4.150208,-5.440027,-1.126372,5.602553],[-8.043211,9.123291,-8.258824,3.307323,-5.018733],[4.857835,4.477031,9.675820,5.844409,-4.939717]],[[-6.505327,5.809811,4.990734,-0.318193,7.703313],[-5.459559,-1.784586,-1.423812,8.313546,2.453874],[-7.467551,9.706714,8.104990,6.467534,-9.847986],[8.803686,-8.401340,-2.927679,1.819067,-5.649517],[-1.169987,-6.666850,-2.427726,2.784826,8.433628]],[[5.353963,-0.890407,0.649111,0.313854,-8.467378],[-6.530025,-9.491203,-6.531742,-3.272270,8.124634],[-2.941770,6.859254,-0.177759,-0.448036,-1.179765],[-3.924114,0.943151,-4.931252,-4.751638,4.870015],[7.493569,0.139354,-6.849199,-2.052859,5.681244]],[[4.483865,-9.774343,-8.043771,-2.739196,-5.233266],[-6.119525,-4.785734,2.228855,-6.855364,-0.923049],[4.421240,8.098713,5.878940,-2.490091,-5.955544],[4.854555,-2.241909,5.666425,7.115313,8.872503],[-8.286083,-0.232164,0.373505,4.127918,-0.807126]],[[2.590095,9.735208,-8.999689,-0.519305,2.495338],[-6.680509,9.924781,-7.282459,2.849460,-2.512315],[7.078529,1.069928,-4.234974,-0.220733,-4.286148],[6.036265,-7.869203,8.348008,-2.395570,5.479318],[-4.684843,-2.365912,-8.663747,-6.328053,-7.404690]],[[-3.206620,8.793908,-8.854047,-1.597410,4.056208],[5.906682,-6.317905,-9.331493,-9.976561,-4.593540],[-3.659035,7.965343,-3.384795,3.285216,4.280334],[2.834749,7.386706,8.652870,-7.345332,-1.146483],[2.971617,1.062309,3.203355,6.312776,-7.700109]],[[-4.787298,-1.957712,5.269004,4.418807,-8.757817],[6.437994,0.481485,-2.975829,-5.210110,-5.439762],[5.072178,-0.554772,-1.939283,-1.685900,1.171003],[1.497066,3.277845,0.451035,-4.321439,7.531392],[0.782077,-0.913054,9.875071,-4.565374,-6.359682]]], dtype = "float64")#candidate|88|(8, 5, 5)|const|float64
uop_89 = relay.tan(const_88.astype('float64')) # shape=(8, 5, 5)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
var_99 = relay.var("var_99", dtype = "bool", shape = (819,))#candidate|99|(819,)|var|bool
call_98 = relay.TupleGetItem(func_47_call(relay.reshape(var_99.astype('bool'), [13, 9, 7])), 0)
call_100 = relay.TupleGetItem(func_50_call(relay.reshape(var_99.astype('bool'), [13, 9, 7])), 0)
uop_112 = relay.asin(uop_89.astype('float64')) # shape=(8, 5, 5)
output = relay.Tuple([call_98,var_99,uop_112,])
output2 = relay.Tuple([call_100,var_99,uop_112,])
func_121 = relay.Function([var_99,], output)
mod['func_121'] = func_121
mod = relay.transform.InferType()(mod)
mutated_mod['func_121'] = func_121
mutated_mod = relay.transform.InferType()(mutated_mod)
var_122 = relay.var("var_122", dtype = "bool", shape = (819,))#candidate|122|(819,)|var|bool
func_121_call = mutated_mod.get_global_var('func_121')
call_123 = func_121_call(var_122)
output = call_123
func_124 = relay.Function([var_122], output)
mutated_mod['func_124'] = func_124
mutated_mod = relay.transform.InferType()(mutated_mod)
var_223 = relay.var("var_223", dtype = "float32", shape = ())#candidate|223|()|var|float32
var_224 = relay.var("var_224", dtype = "float32", shape = (5, 7, 5))#candidate|224|(5, 7, 5)|var|float32
bop_225 = relay.floor_mod(var_223.astype('float32'), var_224.astype('float32')) # shape=(5, 7, 5)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
const_230 = relay.const([[False,False,False],[False,False,True],[False,False,True],[False,True,True],[True,False,False],[True,False,True],[True,False,False],[True,True,True],[False,False,True],[False,True,True],[False,True,True],[False,False,False],[True,False,False],[False,False,True],[False,True,False],[False,False,False],[True,False,True],[True,True,False],[False,True,False],[True,True,True],[False,True,True],[False,False,True],[False,True,True],[False,False,True],[True,False,True],[True,False,True],[False,True,True],[True,False,False],[True,False,True],[True,True,True],[True,False,False],[False,False,False],[True,False,False],[False,False,False],[True,True,False],[False,True,False],[False,True,True],[True,False,True],[False,True,True],[True,False,False],[False,True,False],[True,True,False],[True,False,False],[True,False,False],[True,False,False],[True,False,True],[True,False,False],[False,False,False],[True,False,True],[False,True,True],[True,False,True],[True,True,False],[False,False,True],[False,False,True],[True,True,True],[True,True,False],[False,False,False],[False,True,False],[False,False,False],[True,True,False],[False,False,False],[True,True,True],[False,True,True],[True,False,True],[False,True,True],[False,False,False],[False,False,False],[False,False,True],[True,False,False],[True,True,True],[True,True,True],[True,True,False],[False,True,False],[False,False,False],[True,False,True],[False,False,True],[False,False,True],[True,True,True],[False,False,True],[False,True,False],[True,True,True],[False,False,False],[True,True,True],[True,True,True],[True,False,False],[False,True,False],[True,True,True],[False,False,False],[True,True,False],[False,True,True],[False,True,False],[True,True,True],[False,False,False],[True,True,True],[True,False,True],[True,False,False],[True,True,False],[False,True,False],[False,False,True],[False,False,True],[False,False,False],[False,False,True],[True,False,False],[True,True,True],[False,False,False],[False,True,False],[False,True,False],[False,True,True],[True,False,False],[False,False,False],[True,False,True],[True,True,True],[True,False,True],[True,False,False],[False,False,True],[False,False,False],[True,True,True],[True,True,True],[False,False,True],[False,True,True],[True,False,False],[False,False,True],[True,True,True],[False,False,True],[False,False,False],[True,True,False],[False,False,True],[True,True,True],[False,True,True],[True,False,False],[True,True,True],[True,True,True],[False,False,False],[True,False,False],[True,False,False],[True,False,True],[True,False,True],[True,True,False],[False,False,False],[True,True,False],[False,False,True],[True,True,False],[False,True,False],[False,True,False],[False,False,False],[False,True,False],[False,False,False],[True,True,False],[False,True,False],[False,True,True],[False,True,False],[True,False,True],[True,False,True],[True,False,False],[True,False,False],[True,False,True],[False,False,True],[False,False,True],[False,False,False],[False,False,True],[False,False,False],[False,True,False],[True,False,False],[False,True,False],[False,False,False],[False,True,True],[True,True,True],[True,False,True],[False,False,True],[False,True,True],[False,True,True],[False,True,False],[True,False,False],[True,True,True],[False,True,True],[False,False,True],[True,True,False],[True,False,False],[False,False,True],[False,True,False],[True,True,True],[True,True,False],[True,False,False],[False,False,True],[True,False,True],[True,False,True],[False,False,False],[False,True,True],[True,True,True],[False,True,False],[False,True,True],[True,False,True],[True,True,True],[True,True,True],[True,True,True],[False,False,False],[True,False,False],[True,False,True],[False,True,False],[False,True,False],[False,True,True],[False,False,True],[True,True,False],[False,True,False],[False,False,True],[True,False,True],[True,True,True],[True,False,True],[False,True,True],[True,True,False],[True,True,False],[False,True,False],[True,False,False],[True,True,True],[True,True,True],[False,False,True],[True,False,False],[False,True,False],[False,False,True],[True,True,False],[True,False,False],[True,False,True],[False,True,False],[False,False,True],[True,False,False],[False,False,False],[True,False,False],[True,False,False],[True,False,False],[True,True,True],[True,True,True],[True,False,True],[True,False,False],[True,False,False],[False,True,False],[False,True,True],[False,False,True],[True,True,True],[True,True,False],[True,False,True],[False,True,False],[True,True,True],[False,False,True],[False,True,False],[False,True,True],[True,True,True],[False,True,True],[True,False,True],[False,True,False],[False,False,False],[False,False,True],[False,True,False],[True,True,False],[True,True,True],[True,False,False],[False,True,True],[True,True,True],[True,False,True],[False,False,True],[False,True,True],[False,True,False],[True,True,True],[False,True,True],[False,False,False],[False,True,False],[False,True,True],[False,True,False],[True,False,False],[False,False,True],[True,False,False],[True,False,True],[True,True,False],[False,True,True]], dtype = "bool")#candidate|230|(273, 3)|const|bool
call_229 = relay.TupleGetItem(func_47_call(relay.reshape(const_230.astype('bool'), [13, 9, 7])), 0)
call_231 = relay.TupleGetItem(func_50_call(relay.reshape(const_230.astype('bool'), [13, 9, 7])), 0)
output = relay.Tuple([bop_225,call_229,const_230,])
output2 = relay.Tuple([bop_225,call_231,const_230,])
func_232 = relay.Function([var_223,var_224,], output)
mod['func_232'] = func_232
mod = relay.transform.InferType()(mod)
mutated_mod['func_232'] = func_232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_232_call = mutated_mod.get_global_var('func_232')
var_234 = relay.var("var_234", dtype = "float32", shape = ())#candidate|234|()|var|float32
var_235 = relay.var("var_235", dtype = "float32", shape = (5, 7, 5))#candidate|235|(5, 7, 5)|var|float32
call_233 = func_232_call(var_234,var_235,)
output = call_233
func_236 = relay.Function([var_234,var_235,], output)
mutated_mod['func_236'] = func_236
mutated_mod = relay.transform.InferType()(mutated_mod)
var_253 = relay.var("var_253", dtype = "uint16", shape = ())#candidate|253|()|var|uint16
var_254 = relay.var("var_254", dtype = "uint16", shape = (1, 6, 9))#candidate|254|(1, 6, 9)|var|uint16
bop_255 = relay.minimum(var_253.astype('uint16'), var_254.astype('uint16')) # shape=(1, 6, 9)
output = relay.Tuple([bop_255,])
output2 = relay.Tuple([bop_255,])
func_258 = relay.Function([var_253,var_254,], output)
mod['func_258'] = func_258
mod = relay.transform.InferType()(mod)
mutated_mod['func_258'] = func_258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_258_call = mutated_mod.get_global_var('func_258')
var_260 = relay.var("var_260", dtype = "uint16", shape = ())#candidate|260|()|var|uint16
var_261 = relay.var("var_261", dtype = "uint16", shape = (1, 6, 9))#candidate|261|(1, 6, 9)|var|uint16
call_259 = func_258_call(var_260,var_261,)
output = call_259
func_262 = relay.Function([var_260,var_261,], output)
mutated_mod['func_262'] = func_262
mutated_mod = relay.transform.InferType()(mutated_mod)
const_353 = relay.const([[[-8.923549,-5.520033,6.778986,8.771632,8.718056,8.221361,9.939031,2.129790,-4.918019,-9.679964,-6.048054,-4.900864,-6.974591,-4.379353,-8.088596,-1.630588]],[[1.981453,-9.247309,-9.901242,-6.127197,-7.409489,-5.120539,0.216903,-0.088614,-1.974382,5.963376,-3.541533,-5.432669,0.653661,9.527352,-5.441983,-4.526792]],[[8.804647,-1.548877,-6.227645,5.491947,-1.086620,-6.684891,-6.320308,-8.957781,-4.832817,6.197472,6.715356,0.946076,-6.091071,-1.161461,-5.968150,-3.535498]],[[8.937057,3.642615,-2.121700,6.070923,6.100480,-7.356663,-0.634745,-0.363415,4.146504,3.360784,4.893347,8.163484,-4.755132,-5.707182,8.198691,-5.061257]],[[0.064627,-4.233053,-6.663291,8.628119,-3.818816,8.356922,-6.712423,6.808939,-1.759459,-8.409806,5.293363,9.467876,-3.384240,-0.199872,5.454812,-5.606330]]], dtype = "float64")#candidate|353|(5, 1, 16)|const|float64
uop_354 = relay.log10(const_353.astype('float64')) # shape=(5, 1, 16)
func_121_call = mod.get_global_var('func_121')
func_124_call = mutated_mod.get_global_var('func_124')
var_359 = relay.var("var_359", dtype = "bool", shape = (819,))#candidate|359|(819,)|var|bool
call_358 = relay.TupleGetItem(func_121_call(relay.reshape(var_359.astype('bool'), [819,])), 0)
call_360 = relay.TupleGetItem(func_124_call(relay.reshape(var_359.astype('bool'), [819,])), 0)
uop_364 = relay.sin(call_358.astype('float64')) # shape=(13, 9, 7)
uop_366 = relay.sin(call_360.astype('float64')) # shape=(13, 9, 7)
func_121_call = mod.get_global_var('func_121')
func_124_call = mutated_mod.get_global_var('func_124')
call_370 = relay.TupleGetItem(func_121_call(relay.reshape(uop_364.astype('bool'), [819,])), 2)
call_371 = relay.TupleGetItem(func_124_call(relay.reshape(uop_364.astype('bool'), [819,])), 2)
uop_374 = relay.log(call_358.astype('float64')) # shape=(13, 9, 7)
uop_376 = relay.log(call_360.astype('float64')) # shape=(13, 9, 7)
bop_380 = relay.logical_xor(uop_374.astype('uint8'), relay.reshape(uop_364.astype('uint8'), relay.shape_of(uop_374))) # shape=(13, 9, 7)
bop_383 = relay.logical_xor(uop_376.astype('uint8'), relay.reshape(uop_366.astype('uint8'), relay.shape_of(uop_376))) # shape=(13, 9, 7)
func_258_call = mod.get_global_var('func_258')
func_262_call = mutated_mod.get_global_var('func_262')
var_389 = relay.var("var_389", dtype = "uint16", shape = ())#candidate|389|()|var|uint16
const_390 = relay.const([-3,10,-6,-1,10,-10,-10,-1,-6,-3,8,-2,-7,3,9,5,-10,5,7,-6,8,8,-6,-6,5,7,-5,8,-5,3,-10,7,-3,-5,-8,9,-8,5,5,-8,-3,2,7,9,2,7,-2,1,7,-8,-8,1,4,-1], dtype = "uint16")#candidate|390|(54,)|const|uint16
call_388 = relay.TupleGetItem(func_258_call(relay.reshape(var_389.astype('uint16'), []), relay.reshape(const_390.astype('uint16'), [1, 6, 9]), ), 0)
call_391 = relay.TupleGetItem(func_262_call(relay.reshape(var_389.astype('uint16'), []), relay.reshape(const_390.astype('uint16'), [1, 6, 9]), ), 0)
func_232_call = mod.get_global_var('func_232')
func_236_call = mutated_mod.get_global_var('func_236')
var_393 = relay.var("var_393", dtype = "float32", shape = (1, 175))#candidate|393|(1, 175)|var|float32
call_392 = relay.TupleGetItem(func_232_call(relay.reshape(var_389.astype('float32'), []), relay.reshape(var_393.astype('float32'), [5, 7, 5]), ), 2)
call_394 = relay.TupleGetItem(func_236_call(relay.reshape(var_389.astype('float32'), []), relay.reshape(var_393.astype('float32'), [5, 7, 5]), ), 2)
output = relay.Tuple([uop_354,var_359,call_370,bop_380,call_388,var_389,const_390,call_392,var_393,])
output2 = relay.Tuple([uop_354,var_359,call_371,bop_383,call_391,var_389,const_390,call_394,var_393,])
func_407 = relay.Function([var_359,var_389,var_393,], output)
mod['func_407'] = func_407
mod = relay.transform.InferType()(mod)
mutated_mod['func_407'] = func_407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mutated_mod.get_global_var('func_407')
var_409 = relay.var("var_409", dtype = "bool", shape = (819,))#candidate|409|(819,)|var|bool
var_410 = relay.var("var_410", dtype = "uint16", shape = ())#candidate|410|()|var|uint16
var_411 = relay.var("var_411", dtype = "float32", shape = (1, 175))#candidate|411|(1, 175)|var|float32
call_408 = func_407_call(var_409,var_410,var_411,)
output = call_408
func_412 = relay.Function([var_409,var_410,var_411,], output)
mutated_mod['func_412'] = func_412
mutated_mod = relay.transform.InferType()(mutated_mod)
var_769 = relay.var("var_769", dtype = "float64", shape = (9, 9, 15))#candidate|769|(9, 9, 15)|var|float64
var_770 = relay.var("var_770", dtype = "float64", shape = (9, 9, 15))#candidate|770|(9, 9, 15)|var|float64
bop_771 = relay.mod(var_769.astype('float64'), relay.reshape(var_770.astype('float64'), relay.shape_of(var_769))) # shape=(9, 9, 15)
uop_775 = relay.asinh(bop_771.astype('float32')) # shape=(9, 9, 15)
func_121_call = mod.get_global_var('func_121')
func_124_call = mutated_mod.get_global_var('func_124')
const_780 = relay.const([[True,True,True],[True,False,True],[False,False,False],[True,False,True],[True,False,True],[False,False,False],[False,True,True],[False,True,False],[True,False,True],[True,False,True],[True,False,False],[False,True,False],[True,False,False],[False,True,False],[True,False,True],[True,True,True],[True,True,False],[False,True,True],[False,False,True],[False,True,False],[True,False,False],[True,False,True],[True,False,True],[False,False,True],[False,True,True],[True,False,False],[False,False,True],[False,False,False],[True,True,False],[True,True,True],[True,False,True],[True,True,False],[False,False,False],[False,False,False],[True,True,True],[False,False,False],[True,True,False],[False,True,False],[True,True,True],[True,False,False],[True,True,False],[False,False,True],[False,False,False],[False,False,False],[False,True,True],[False,False,False],[False,True,True],[False,True,False],[False,False,True],[False,False,True],[False,True,False],[True,True,False],[False,False,True],[False,False,True],[True,True,True],[False,True,True],[False,True,False],[True,True,True],[False,True,False],[True,True,False],[True,False,True],[True,True,False],[False,True,False],[True,False,True],[False,True,False],[True,True,True],[False,False,False],[False,True,True],[False,True,False],[False,True,False],[False,False,False],[True,True,True],[True,True,False],[False,False,False],[True,True,True],[True,False,True],[False,True,True],[False,True,False],[True,True,False],[True,True,True],[True,True,True],[True,False,False],[False,False,False],[True,False,False],[True,True,True],[True,False,False],[False,False,True],[True,False,False],[True,True,False],[True,False,True],[False,False,True],[True,True,True],[False,False,True],[False,True,True],[False,False,False],[False,True,False],[False,True,False],[True,False,False],[True,False,True],[True,True,False],[True,False,False],[False,True,True],[True,True,True],[True,True,False],[False,False,True],[True,False,False],[True,False,False],[False,True,False],[False,False,False],[False,False,False],[False,True,False],[False,True,True],[True,False,True],[True,True,False],[True,False,False],[False,True,False],[True,False,False],[True,False,True],[True,True,False],[False,True,False],[False,True,True],[False,True,False],[True,False,False],[False,True,False],[True,True,False],[True,True,True],[False,False,True],[False,True,False],[False,True,True],[False,True,False],[False,True,True],[True,True,False],[True,False,False],[True,True,False],[True,False,True],[True,True,False],[False,True,True],[False,False,False],[False,False,True],[True,False,False],[True,False,True],[False,True,False],[False,False,True],[False,True,False],[False,True,False],[True,False,True],[False,True,True],[True,True,True],[True,True,True],[True,False,True],[True,True,True],[True,True,False],[True,True,False],[False,True,True],[False,False,False],[False,True,True],[False,True,False],[True,False,True],[False,False,False],[True,True,False],[False,False,True],[True,True,False],[True,True,True],[True,True,False],[False,False,False],[True,False,False],[False,False,True],[False,True,False],[True,True,False],[True,False,True],[True,False,True],[False,True,True],[False,False,False],[True,True,True],[True,False,True],[False,True,False],[False,True,False],[True,True,False],[True,False,True],[True,True,False],[False,False,False],[False,False,False],[True,False,False],[True,True,False],[False,False,False],[False,False,True],[False,False,False],[False,False,True],[False,True,True],[False,True,False],[False,True,False],[False,True,False],[False,False,False],[True,True,True],[True,False,True],[True,False,False],[False,False,False],[False,False,False],[True,True,False],[False,True,True],[False,True,False],[False,True,False],[False,False,False],[False,True,False],[True,False,False],[False,True,False],[False,True,False],[True,True,False],[True,False,True],[True,False,False],[False,False,True],[True,False,True],[True,False,True],[True,False,False],[True,True,False],[True,True,True],[True,False,False],[True,True,True],[False,False,True],[True,False,True],[False,False,True],[True,True,True],[False,False,True],[True,False,True],[True,True,False],[True,True,True],[False,False,True],[False,False,False],[True,False,True],[False,True,True],[True,True,True],[False,True,True],[True,True,True],[False,True,True],[True,False,True],[True,False,False],[True,False,False],[False,True,False],[True,False,False],[False,True,False],[True,False,True],[False,True,False],[True,False,False],[True,True,True],[False,False,True],[True,False,True],[True,True,False],[False,True,True],[False,False,True],[True,False,False],[True,True,True],[False,False,False],[True,True,False],[True,False,True],[False,True,False],[True,False,False],[True,False,True],[True,False,False],[False,False,True],[True,True,True],[False,False,True],[True,True,True],[True,False,False],[True,True,True],[True,True,False],[True,False,False],[True,True,False],[False,False,False],[False,False,True],[True,False,False],[True,False,True],[False,True,False],[True,False,False]], dtype = "bool")#candidate|780|(273, 3)|const|bool
call_779 = relay.TupleGetItem(func_121_call(relay.reshape(const_780.astype('bool'), [819,])), 0)
call_781 = relay.TupleGetItem(func_124_call(relay.reshape(const_780.astype('bool'), [819,])), 0)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
call_785 = relay.TupleGetItem(func_47_call(relay.reshape(call_779.astype('bool'), [13, 9, 7])), 1)
call_786 = relay.TupleGetItem(func_50_call(relay.reshape(call_779.astype('bool'), [13, 9, 7])), 1)
const_787 = relay.const([[[5.289464,9.651621,3.433525,0.993455,-1.049600,-1.406398,3.339714,3.333242,-9.218950,-8.742251,-7.406535,2.679096,7.533149,4.807420,2.158127],[-9.281552,8.964350,5.922447,-1.290585,-5.080326,-9.954056,9.336653,8.328514,2.591093,1.492191,-5.254554,-0.125838,6.704867,-7.411726,-8.352724],[-0.530740,-1.667286,-2.997918,-5.252530,-1.336009,-5.796634,-4.427257,6.273426,-3.259114,5.853399,-4.123976,9.584441,4.724594,-5.501504,6.091848],[1.109898,7.650273,-4.110274,-1.035955,8.670613,6.223188,4.435282,6.732787,2.577913,-8.431462,4.412167,9.492387,7.018495,-3.585595,-1.291737],[0.918981,8.211039,6.533052,-3.278582,-6.851892,7.512523,6.613520,7.157650,4.983527,-3.405532,-5.361180,-1.389382,8.193320,-9.472336,8.414114],[6.310602,3.747881,2.870374,-7.124175,-9.477334,7.339645,2.185591,-0.265898,-2.130448,1.399299,5.819797,-0.752081,1.700673,-4.353857,5.712561],[-8.341794,-5.109380,8.031650,2.132386,1.076831,3.486312,5.835865,-3.904035,3.880947,9.635304,4.840515,-7.772305,-2.533108,0.507042,-2.296855],[-1.684708,-2.667652,-0.363634,-0.234926,7.892058,5.314621,6.514369,1.077094,-1.950921,-4.502975,-2.296104,0.996209,9.517480,-5.209152,-7.173991],[-2.160431,-2.779163,3.327934,-2.590901,-7.071278,2.188441,-5.450082,-9.321348,-5.714231,7.786046,-1.159819,9.811927,-9.610907,3.460119,7.358256]],[[4.946607,-3.007713,-5.155927,-0.319833,3.820389,3.513905,-6.252923,7.384691,2.841197,-7.026800,-1.736905,-1.838830,-9.813717,8.823006,-9.207247],[9.964551,-8.013436,8.567075,5.550089,3.995127,-2.530976,3.195751,7.288445,7.285995,0.317778,1.146543,-9.374477,8.074133,-8.359424,-4.627539],[1.270372,6.182284,9.868654,3.603825,-9.126717,7.111680,5.592100,-5.490247,-1.938448,6.821409,5.049473,1.530046,8.355443,-0.160769,9.373097],[-9.749212,-8.571491,-3.180405,-6.738431,-5.096041,3.096184,0.227947,-2.001774,7.148086,9.441110,-9.212119,1.730512,-0.280739,-8.467384,-4.786347],[9.023287,9.366084,-4.527361,2.740788,7.107776,-2.402176,8.557770,8.097653,7.505882,-4.532416,5.922276,0.147175,3.646031,4.517745,-1.972026],[0.281110,-1.963693,2.909948,8.705120,1.190660,-7.803817,7.264988,9.081655,5.461380,9.545213,9.623322,9.158873,4.767514,-3.594847,-3.479809],[-4.043735,-1.600246,-9.547002,-3.248936,-1.810779,-7.922873,2.833294,4.778043,-1.443932,8.693147,-6.698507,1.801229,5.286508,-2.593832,2.350109],[-5.056053,6.694029,8.299141,-5.139946,2.247527,5.600694,9.111224,9.122182,-6.714486,5.743542,0.809808,-8.286926,9.602762,8.038400,-1.489893],[5.788886,-8.777238,4.863479,-0.137759,9.292203,2.041861,-0.156554,8.934185,8.705893,7.885095,3.871748,-4.120382,2.772877,8.551732,-0.308325]],[[-5.471230,-3.286827,-7.386980,-6.924861,4.728540,-3.695499,-5.296039,1.964854,-2.358556,7.795487,-1.926049,-9.875576,6.940776,-7.353205,-4.677557],[-3.088939,-5.978757,2.544194,-2.958426,-6.207353,-4.757349,-8.687997,9.217902,-1.610428,-0.016676,3.616167,6.905246,-6.339530,-4.746745,3.197735],[5.827272,6.354325,0.941941,-6.116051,-4.412096,0.480513,4.212803,1.822703,-2.341364,-4.866404,-7.911200,9.515960,1.532914,-6.722882,-2.027681],[-4.398833,3.524090,-7.559471,-5.532551,-2.817620,9.545717,9.192179,-4.632568,8.171734,7.598425,2.478553,3.304480,6.691573,-2.733487,-2.483115],[9.052623,-0.373491,-5.995366,3.517121,0.456572,0.999853,-7.787592,1.213741,-0.704068,1.820466,-8.667955,5.135278,0.055070,-0.222232,-9.940155],[-6.089266,0.289754,-2.463283,0.300218,8.329260,3.856330,6.700984,3.811354,-2.513386,5.050376,9.063517,6.066477,-4.273058,5.634791,-0.451774],[4.215169,-0.783692,-2.313408,1.334787,-0.076718,-9.526839,0.956768,6.131309,9.799521,-5.240880,7.550004,-2.187608,-0.170547,3.129852,-9.236871],[3.040014,1.902344,-7.032398,-2.845660,8.099088,-4.647488,9.730607,-2.373277,1.312282,-7.630359,-0.464281,9.020427,-6.735162,8.074464,-9.619715],[-9.791781,-0.664671,8.407603,9.627312,-1.000836,-4.517935,-3.844365,-0.854675,6.709381,-1.100582,-2.915479,7.889616,-6.304326,0.777714,-3.412837]],[[1.084951,-5.453483,-4.601371,-0.391525,2.587992,-1.524425,-2.146323,5.227280,3.350364,-7.267443,6.895867,7.384288,-4.826783,-0.763359,0.436848],[0.127078,1.766175,-1.236819,5.965365,4.703706,6.769997,7.201436,6.827457,5.996245,1.906763,-0.812787,-1.644083,6.220857,8.412905,-2.664477],[-4.688286,9.533399,0.646740,2.753503,1.136542,-5.547136,1.195877,-3.812351,-2.571370,9.000784,9.779351,-4.590095,0.056405,-7.955418,-8.023285],[-0.957220,0.548034,-9.941122,7.987387,3.282366,6.234807,-3.465833,2.095422,7.328618,-9.729745,6.012503,-9.025213,4.894101,-3.158220,6.944723],[-8.328391,8.240986,9.970469,9.455200,-6.053830,7.903327,-1.066239,-5.990466,-1.675096,4.568724,-6.916222,-2.444779,6.584539,0.074579,-5.051561],[-4.889755,-9.932793,-9.767569,6.970721,-0.154041,-0.384313,0.679040,5.590849,9.495099,7.894202,-7.468484,8.756411,3.445121,-7.408806,-1.238694],[9.772672,-3.497852,4.597047,5.081723,-7.095682,-0.672141,-8.535352,2.762217,0.468965,2.368701,1.344077,-7.226309,4.523793,2.323013,-8.979240],[-7.122751,-1.114740,3.868065,1.884606,4.435688,4.968255,-3.544228,3.858486,2.174778,-3.839513,-9.778823,4.133109,4.043698,-8.503715,-0.594315],[-4.372647,-4.683764,0.945368,-4.446880,-3.539207,-9.046413,0.513975,4.633019,-0.482718,6.408223,-5.141315,4.918226,9.427217,-3.110168,4.542360]],[[-8.701116,8.165035,2.311005,5.511344,9.914035,0.880181,0.612674,-1.700155,2.962151,6.151991,-1.089670,-2.371631,1.339718,-8.186602,3.039052],[5.326449,5.430019,-5.306179,1.179099,5.249804,-3.055565,6.605132,0.313295,-0.310097,-7.285105,-0.881243,4.943007,-8.872554,-6.700114,-1.990235],[2.810463,9.511530,-3.041388,4.808856,4.819933,-8.404734,1.505709,7.326258,-1.351088,4.005376,-2.502167,2.586415,1.171884,-4.032342,-8.972630],[4.653097,-5.704158,-2.883153,2.089173,3.845974,-1.937138,-5.524172,6.081306,1.552858,7.520018,-2.983189,-3.076989,-9.435153,-7.604768,2.338032],[3.938508,-0.953180,4.954697,2.824648,-5.514086,-3.430280,-2.358465,-3.045868,-7.998463,7.187275,-0.284286,0.134496,7.199391,-7.362721,5.234343],[-2.449545,4.799294,-2.527014,-7.286986,7.046362,-2.276255,9.590170,-0.285028,-8.049936,3.877108,-5.864909,-2.734285,-9.433952,3.075305,1.698287],[-0.915061,-6.147332,-5.919525,9.196161,-7.815025,5.142659,-3.034275,9.537555,-8.642871,7.575376,-9.767564,9.440027,-3.500660,-8.827617,5.413414],[-1.665951,-8.385580,1.982264,4.132507,0.561129,7.011936,0.038518,3.641322,-9.941933,-6.523095,-4.238494,8.152349,2.519798,8.369231,-3.765336],[5.807845,1.889930,4.187357,-0.865091,7.935085,-9.973533,-3.065290,-5.497904,-6.521772,7.104539,-9.485916,2.445527,-0.276897,8.368022,4.104970]],[[-3.530776,-5.598827,-9.273648,-5.729654,8.463699,-5.428726,-6.182060,0.707723,-6.891085,1.301898,-9.345061,8.886564,6.629706,4.127348,-5.288680],[-0.763825,5.839218,-9.064998,-8.712397,5.295070,-5.889123,5.774372,-8.607225,0.429552,0.019253,5.378726,-4.712780,7.316483,-7.021090,5.612098],[1.437788,0.348229,-2.144528,-6.043592,-6.865711,-2.174474,2.399170,4.147092,-8.678373,9.696655,0.614161,-7.539574,0.722182,2.330504,-5.136069],[-5.299766,2.934052,-7.969028,4.710004,-0.485098,-1.336781,-2.962559,9.488727,-4.674728,-8.845426,3.613189,-0.187843,-7.876748,7.133815,5.106712],[-7.076902,-7.714604,1.912203,6.182921,3.209896,-8.408125,9.643599,-6.397186,-5.405052,-8.810879,-9.176046,-2.354929,8.945926,-1.822306,-6.359044],[-9.558459,-7.113582,-1.729849,-1.602205,-2.048457,-8.526212,6.906065,-1.319693,-7.604117,-5.760065,9.209043,-2.454568,6.414024,-2.301630,-1.348346],[5.678619,7.809221,8.447909,0.536679,-3.455805,-5.733362,-6.032909,-8.117059,2.515774,5.875394,6.122579,-1.085426,-1.560377,-7.086292,4.152421],[-6.185291,7.401643,-9.451989,7.862135,-9.543734,-0.629681,-1.548308,5.272579,2.835612,5.799041,-5.251030,1.435404,-2.741005,3.342448,5.860872],[-8.660576,9.319218,0.338289,-8.813515,-4.909991,-4.734684,9.955690,1.128668,5.545350,6.493119,-5.232104,-1.867427,-8.887169,6.017132,6.357267]],[[6.073846,-1.654533,7.755322,-5.395804,3.276240,7.473477,1.950069,-5.365975,2.338033,1.464441,3.922893,-9.547560,-2.014762,-5.391197,-6.305774],[-2.388278,2.746886,3.262320,-2.503442,5.123541,-9.921125,-8.910176,2.774230,-8.723314,-5.445174,-6.675414,2.773617,6.187860,5.632605,-9.855670],[9.523828,1.399015,8.654262,-2.805517,4.867699,1.705267,-3.906559,3.862873,4.129842,-6.681905,-2.503764,7.494770,4.777241,5.124657,-3.464073],[5.374516,-5.438610,1.084046,4.318384,1.514834,8.918242,-1.553913,-9.475447,4.902600,6.310159,-5.259804,-1.711992,-3.385544,-3.295557,7.055483],[7.003368,0.108895,1.197325,8.992370,-3.630414,7.760581,-2.325256,7.768497,-7.684074,-6.553594,-7.893880,1.350728,-0.404260,-0.484100,7.852760],[4.059521,-1.078264,-7.333453,9.695061,-1.040301,-7.641441,6.579808,7.151156,-6.868992,-1.200821,-7.821551,2.431998,6.345694,6.426911,-4.466973],[4.001063,3.870474,-8.745032,-7.337104,7.755800,6.428224,-3.981282,-7.679726,6.819035,1.878936,3.716403,-7.403563,9.463936,-5.866438,-0.791379],[6.267136,2.736195,1.335217,-3.305859,0.197438,2.773673,-6.156189,-7.555205,1.608786,2.747147,7.097107,-4.261520,1.977483,8.212590,-3.426557],[-2.761606,-7.491892,-5.577380,-6.126851,6.108482,8.191522,-2.217705,-9.342859,-0.601073,5.136577,7.197560,4.701342,-4.494610,3.927861,-7.926341]],[[8.243936,-0.718368,-1.562147,-0.985601,5.684768,9.671371,-7.670897,-9.168341,-2.366477,-6.955608,-7.575372,-0.304965,-1.439465,-5.966190,-2.476518],[9.606507,-6.343554,8.729479,9.672220,6.955014,0.498815,4.945985,-9.064511,9.776660,-3.190750,-3.556213,0.049571,-3.885238,-1.952991,5.981106],[-5.143980,-8.332579,-4.810406,3.797994,2.326976,8.422513,9.261566,-3.046250,-8.303167,-7.306662,-5.617821,-6.727038,3.048368,4.182069,7.534274],[1.519121,7.419939,-2.086886,7.578027,8.321769,-1.212769,-4.689809,2.579783,-3.547433,-5.829865,5.589639,0.665774,-7.077729,-1.965383,-7.491391],[-6.875297,1.344176,-9.690871,-3.386259,-9.661210,-5.849890,-4.911027,-7.013565,-8.092415,8.532146,-8.647607,5.045322,-8.039700,-6.262938,1.269307],[6.528423,-4.447244,6.398047,-5.027462,6.121403,-0.561278,-2.001518,-6.980875,-4.184551,8.714984,3.211237,-9.476824,0.295188,-3.193868,-0.681794],[4.705077,4.299936,-5.406679,-8.195032,-8.985840,8.605320,4.252137,4.374427,8.140319,-9.677529,-8.767184,-8.008521,-0.905509,9.816138,7.116788],[-6.265512,1.957949,5.512603,7.319828,7.239555,8.085781,-2.093263,-5.978495,-7.144769,4.705737,-1.746025,-1.775202,6.497570,-5.269053,0.142586],[-1.462529,-7.857315,8.585697,9.697839,4.961097,8.979418,-1.119095,-9.841380,1.298088,-1.904957,6.608980,-2.484904,3.948789,3.971773,1.646845]],[[2.226134,-3.613785,6.729210,2.992697,-2.599442,6.050386,4.441372,7.747637,-3.046034,-8.551230,-7.169331,5.663865,3.626793,-7.760412,7.427689],[1.509812,6.032333,-1.580253,-8.914884,5.363996,7.885001,-4.948569,-1.409143,-2.601590,-6.834599,7.211632,-5.609237,-8.716550,1.585068,-8.456464],[-4.434054,-2.635992,-3.658318,-3.180518,-4.239394,4.058007,1.997509,6.329844,-8.507391,-3.770288,-7.302655,2.683967,7.525157,6.420672,-0.900449],[6.991342,9.647148,-5.647494,-6.114654,-9.346722,-0.834210,-0.094014,6.527271,-9.816522,3.397572,8.157998,-8.102824,9.921044,-9.082043,9.707252],[-9.544834,5.635088,-9.092445,0.429260,-3.789321,6.927660,-5.123942,-9.067671,0.704008,7.098613,-0.413866,4.778231,9.215878,-1.736762,5.127239],[-0.990397,-0.603663,3.354526,9.986632,1.202864,9.425319,-6.425690,7.840275,2.436517,4.733989,4.477239,8.753203,9.841945,9.400819,-2.213111],[3.884739,3.863862,-9.730270,-1.956162,4.679851,-6.265079,-5.090211,-3.649744,6.649776,0.761984,-2.165569,-9.836749,6.051101,-3.262185,6.262928],[9.489080,9.191102,-4.486110,0.019509,0.707480,2.766598,6.044114,1.870648,8.113784,-9.320814,6.565369,7.374676,-4.193615,3.975229,-0.246072],[-5.972726,6.716829,-2.338063,5.720962,-9.353607,-8.637105,-2.941181,-9.229459,-7.190463,4.537054,-9.461870,1.211215,-9.575753,-2.749067,1.867369]]], dtype = "float32")#candidate|787|(9, 9, 15)|const|float32
bop_788 = relay.subtract(uop_775.astype('int32'), relay.reshape(const_787.astype('int32'), relay.shape_of(uop_775))) # shape=(9, 9, 15)
func_407_call = mod.get_global_var('func_407')
func_412_call = mutated_mod.get_global_var('func_412')
var_807 = relay.var("var_807", dtype = "uint16", shape = ())#candidate|807|()|var|uint16
const_808 = relay.const([[1.834891],[-5.251115],[-9.269884],[2.432743],[2.727430],[9.658104],[6.639404],[-5.422679],[-8.948816],[7.897562],[4.758246],[-8.479710],[0.438824],[2.062614],[8.157815],[-0.845109],[1.200841],[2.934728],[-6.140332],[2.106035],[-5.532580],[9.453344],[-5.284000],[-6.309290],[3.705449],[1.334095],[7.516200],[-1.342011],[0.339002],[-6.167074],[6.742901],[6.756126],[7.812299],[6.037407],[-4.989560],[6.013872],[5.681530],[-3.705619],[-7.332390],[-8.071299],[-1.766049],[4.614135],[3.448232],[3.339374],[3.075764],[5.669716],[-7.099535],[-2.696061],[-8.544974],[6.429761],[-0.219345],[5.880561],[3.164452],[9.998589],[8.927671],[5.696248],[2.541863],[3.536389],[-8.346426],[-0.336119],[-1.491561],[2.550230],[-9.140090],[-4.196511],[6.820411],[2.217292],[-3.246517],[2.830225],[-9.515769],[-1.735874],[-7.609573],[-8.983330],[-3.323282],[5.343403],[-6.765118],[-4.925800],[5.720906],[6.777925],[2.915669],[-1.265664],[3.824233],[-6.960476],[0.832918],[0.042094],[-8.534042],[7.497096],[4.051036],[5.499470],[1.033746],[-7.747122],[-1.728328],[-6.779536],[-2.670022],[9.536029],[9.564297],[-5.764517],[-9.418502],[-1.696781],[-1.904595],[7.368608],[1.590455],[-3.925954],[-3.936576],[-2.690247],[-1.210782],[0.650635],[-3.077854],[-4.423517],[9.875013],[-4.886094],[-6.340436],[9.850313],[-4.435312],[-2.183176],[7.465245],[6.946514],[-1.556955],[4.325764],[1.414569],[-8.164912],[4.142808],[-2.779060],[6.399791],[-9.036547],[6.833232],[9.729368],[-0.178746],[-9.454816],[-3.622857],[8.853708],[-8.750091],[9.613530],[-8.917309],[-9.667691],[-9.634378],[3.294033],[-5.355673],[6.249539],[5.476340],[3.845392],[8.319640],[-8.694370],[7.901767],[-6.473451],[3.902692],[-6.554501],[-3.079781],[-6.879754],[-0.150421],[0.541545],[7.118398],[-3.531453],[-1.654988],[9.598322],[-4.839352],[-3.538308],[2.095027],[4.473398],[2.343077],[-6.321727],[0.184308],[5.256155],[-7.349443],[6.685613],[-4.092297],[-1.340385],[2.146271],[4.152052],[-9.835684],[3.227576],[6.424868],[-4.890507],[-1.305835],[-7.411373],[6.889484]], dtype = "float32")#candidate|808|(175, 1)|const|float32
call_806 = relay.TupleGetItem(func_407_call(relay.reshape(const_780.astype('bool'), [819,]), relay.reshape(var_807.astype('uint16'), []), relay.reshape(const_808.astype('float32'), [1, 175]), ), 1)
call_809 = relay.TupleGetItem(func_412_call(relay.reshape(const_780.astype('bool'), [819,]), relay.reshape(var_807.astype('uint16'), []), relay.reshape(const_808.astype('float32'), [1, 175]), ), 1)
output = relay.Tuple([call_779,const_780,call_785,bop_788,call_806,var_807,const_808,])
output2 = relay.Tuple([call_781,const_780,call_786,bop_788,call_809,var_807,const_808,])
func_810 = relay.Function([var_769,var_770,var_807,], output)
mod['func_810'] = func_810
mod = relay.transform.InferType()(mod)
mutated_mod['func_810'] = func_810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_810_call = mutated_mod.get_global_var('func_810')
var_812 = relay.var("var_812", dtype = "float64", shape = (9, 9, 15))#candidate|812|(9, 9, 15)|var|float64
var_813 = relay.var("var_813", dtype = "float64", shape = (9, 9, 15))#candidate|813|(9, 9, 15)|var|float64
var_814 = relay.var("var_814", dtype = "uint16", shape = ())#candidate|814|()|var|uint16
call_811 = func_810_call(var_812,var_813,var_814,)
output = call_811
func_815 = relay.Function([var_812,var_813,var_814,], output)
mutated_mod['func_815'] = func_815
mutated_mod = relay.transform.InferType()(mutated_mod)
var_858 = relay.var("var_858", dtype = "uint16", shape = (1, 2))#candidate|858|(1, 2)|var|uint16
const_859 = relay.const([[4,4]], dtype = "uint16")#candidate|859|(1, 2)|const|uint16
bop_860 = relay.less(var_858.astype('bool'), relay.reshape(const_859.astype('bool'), relay.shape_of(var_858))) # shape=(1, 2)
output = bop_860
output2 = bop_860
func_871 = relay.Function([var_858,], output)
mod['func_871'] = func_871
mod = relay.transform.InferType()(mod)
mutated_mod['func_871'] = func_871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_872 = relay.var("var_872", dtype = "uint16", shape = (1, 2))#candidate|872|(1, 2)|var|uint16
func_871_call = mutated_mod.get_global_var('func_871')
call_873 = func_871_call(var_872)
output = call_873
func_874 = relay.Function([var_872], output)
mutated_mod['func_874'] = func_874
mutated_mod = relay.transform.InferType()(mutated_mod)
var_883 = relay.var("var_883", dtype = "float64", shape = ())#candidate|883|()|var|float64
const_884 = relay.const([[[-2.552523,-9.572938,5.116593,-1.649959,-2.879215,-7.833904,-7.468924,-2.995335,3.309680,7.696133,-2.203211,-1.341541,-2.651407,-8.749126,-3.475158],[3.288067,4.496311,8.555425,5.451887,1.998946,5.824201,4.013749,3.084955,-6.015186,-1.990664,-4.887401,6.885562,4.785534,2.960218,0.479596]],[[-8.309384,-9.914610,-3.251082,-8.971344,-2.960866,6.642147,-6.317572,4.029178,-8.952266,-8.920354,-6.638559,-2.914745,5.146758,5.213995,3.065034],[-0.363479,7.297427,2.134713,-0.598983,-9.731833,-3.143136,3.099065,-9.695274,-0.027191,-7.939536,2.617401,-6.687143,-5.523803,-8.121583,-5.784056]],[[-2.197390,7.459616,-8.724993,4.167237,-3.257977,8.495136,0.957849,8.252205,8.260089,-0.681993,-1.193722,-4.877896,4.877047,5.255044,0.312098],[-6.163222,-5.691442,6.294961,-1.245321,-1.974147,-4.976225,5.393445,-5.502950,-1.474154,0.737403,2.425557,-1.675167,-7.839318,-0.637676,2.326232]],[[1.740212,5.692351,2.859317,-7.005904,6.038236,9.705622,-0.584282,9.175893,5.133128,4.801407,-5.835780,6.636810,-2.730096,7.221076,4.590269],[-5.192641,-5.598473,-8.149547,6.460949,9.009796,2.468873,-1.733026,-6.532896,-4.252478,2.259081,-2.518153,-9.084022,2.510212,5.169542,7.495798]],[[8.588993,4.305081,3.676524,-9.399369,8.540695,6.379313,-8.920616,-0.381685,9.298900,-7.684929,-3.047198,4.625068,-1.625340,-8.705551,4.217536],[-0.494530,8.451129,-4.963751,-5.182650,8.656236,-2.416090,-6.465037,1.267753,2.977477,-4.560264,5.784173,-3.284387,6.969663,0.445416,-6.012520]],[[-0.521316,-4.516398,7.727646,-5.412745,8.851308,0.865912,4.208242,-0.560445,-9.432734,5.492890,1.483362,-7.910201,8.584733,2.455558,5.720727],[1.816588,-3.442780,1.795300,-3.632977,2.463265,-2.598182,-4.692108,5.887593,-4.310307,-5.607799,-4.187555,-2.485442,-6.461685,-2.847170,5.981376]],[[5.515721,7.964177,-7.369070,0.103516,8.844525,-0.531637,3.876149,3.147657,7.978749,9.653173,1.977117,4.985684,-5.808031,-0.521038,6.524121],[-7.869180,-2.842801,3.811024,-6.394481,-8.851989,8.461476,7.182755,6.640574,3.894226,-7.483827,-2.951709,-6.712577,-8.251914,1.684545,-3.082272]],[[-9.226023,-6.135783,-6.871043,9.602827,-7.447008,-6.198171,-1.443245,1.715768,-6.272886,-6.049781,9.758449,6.454673,-8.909166,-4.669217,-2.178853],[7.195430,5.684481,4.038839,6.724523,-7.780644,-2.400830,5.204442,5.818194,-6.561742,-2.858600,-6.172963,-2.235615,2.451298,8.243145,-6.291648]]], dtype = "float64")#candidate|884|(8, 2, 15)|const|float64
bop_885 = relay.floor_divide(var_883.astype('float64'), const_884.astype('float64')) # shape=(8, 2, 15)
uop_890 = relay.log2(bop_885.astype('float32')) # shape=(8, 2, 15)
func_871_call = mod.get_global_var('func_871')
func_874_call = mutated_mod.get_global_var('func_874')
var_897 = relay.var("var_897", dtype = "uint16", shape = (2, 1))#candidate|897|(2, 1)|var|uint16
call_896 = func_871_call(relay.reshape(var_897.astype('uint16'), [1, 2]))
call_898 = func_871_call(relay.reshape(var_897.astype('uint16'), [1, 2]))
bop_903 = relay.mod(uop_890.astype('float64'), var_883.astype('float64')) # shape=(8, 2, 15)
output = relay.Tuple([call_896,var_897,bop_903,])
output2 = relay.Tuple([call_898,var_897,bop_903,])
func_930 = relay.Function([var_883,var_897,], output)
mod['func_930'] = func_930
mod = relay.transform.InferType()(mod)
mutated_mod['func_930'] = func_930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_930_call = mutated_mod.get_global_var('func_930')
var_932 = relay.var("var_932", dtype = "float64", shape = ())#candidate|932|()|var|float64
var_933 = relay.var("var_933", dtype = "uint16", shape = (2, 1))#candidate|933|(2, 1)|var|uint16
call_931 = func_930_call(var_932,var_933,)
output = call_931
func_934 = relay.Function([var_932,var_933,], output)
mutated_mod['func_934'] = func_934
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1043 = relay.var("var_1043", dtype = "float64", shape = (3, 11, 6))#candidate|1043|(3, 11, 6)|var|float64
uop_1044 = relay.sigmoid(var_1043.astype('float64')) # shape=(3, 11, 6)
output = uop_1044
output2 = uop_1044
func_1055 = relay.Function([var_1043,], output)
mod['func_1055'] = func_1055
mod = relay.transform.InferType()(mod)
mutated_mod['func_1055'] = func_1055
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1056 = relay.var("var_1056", dtype = "float64", shape = (3, 11, 6))#candidate|1056|(3, 11, 6)|var|float64
func_1055_call = mutated_mod.get_global_var('func_1055')
call_1057 = func_1055_call(var_1056)
output = call_1057
func_1058 = relay.Function([var_1056], output)
mutated_mod['func_1058'] = func_1058
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1193 = relay.var("var_1193", dtype = "float64", shape = (15, 12, 14))#candidate|1193|(15, 12, 14)|var|float64
var_1194 = relay.var("var_1194", dtype = "float64", shape = (15, 12, 14))#candidate|1194|(15, 12, 14)|var|float64
bop_1195 = relay.mod(var_1193.astype('float64'), relay.reshape(var_1194.astype('float64'), relay.shape_of(var_1193))) # shape=(15, 12, 14)
output = relay.Tuple([bop_1195,])
output2 = relay.Tuple([bop_1195,])
func_1200 = relay.Function([var_1193,var_1194,], output)
mod['func_1200'] = func_1200
mod = relay.transform.InferType()(mod)
mutated_mod['func_1200'] = func_1200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1200_call = mutated_mod.get_global_var('func_1200')
var_1202 = relay.var("var_1202", dtype = "float64", shape = (15, 12, 14))#candidate|1202|(15, 12, 14)|var|float64
var_1203 = relay.var("var_1203", dtype = "float64", shape = (15, 12, 14))#candidate|1203|(15, 12, 14)|var|float64
call_1201 = func_1200_call(var_1202,var_1203,)
output = call_1201
func_1204 = relay.Function([var_1202,var_1203,], output)
mutated_mod['func_1204'] = func_1204
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1407 = relay.const([[[-5.789806,-1.183779,-8.388464,1.437343,-8.762843],[-4.820783,7.607219,7.166913,6.359988,6.983643],[-2.675525,1.820718,0.880441,-3.549941,-1.941975],[1.338858,-3.765578,6.531264,7.146116,-3.207114],[8.468871,-0.976808,3.830638,-6.205829,7.177532],[8.199561,7.143564,9.127919,8.825028,3.715431],[2.302195,-2.170178,-1.895213,-7.589035,5.543449]]], dtype = "float32")#candidate|1407|(1, 7, 5)|const|float32
uop_1408 = relay.acos(const_1407.astype('float32')) # shape=(1, 7, 5)
func_871_call = mod.get_global_var('func_871')
func_874_call = mutated_mod.get_global_var('func_874')
var_1421 = relay.var("var_1421", dtype = "uint16", shape = (2,))#candidate|1421|(2,)|var|uint16
call_1420 = func_871_call(relay.reshape(var_1421.astype('uint16'), [1, 2]))
call_1422 = func_871_call(relay.reshape(var_1421.astype('uint16'), [1, 2]))
uop_1424 = relay.log10(uop_1408.astype('float32')) # shape=(1, 7, 5)
output = relay.Tuple([call_1420,var_1421,uop_1424,])
output2 = relay.Tuple([call_1422,var_1421,uop_1424,])
func_1427 = relay.Function([var_1421,], output)
mod['func_1427'] = func_1427
mod = relay.transform.InferType()(mod)
mutated_mod['func_1427'] = func_1427
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1428 = relay.var("var_1428", dtype = "uint16", shape = (2,))#candidate|1428|(2,)|var|uint16
func_1427_call = mutated_mod.get_global_var('func_1427')
call_1429 = func_1427_call(var_1428)
output = call_1429
func_1430 = relay.Function([var_1428], output)
mutated_mod['func_1430'] = func_1430
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1721 = relay.const([[[4,2,-4,6,-9,7,4,-5,8,-7,-3,5,-1,9,-7,-3]],[[-4,-9,-5,10,-4,5,4,6,9,2,-4,2,-10,-3,5,9]],[[2,-10,5,-8,-8,8,-3,3,-6,2,2,7,6,-2,-5,-2]],[[1,3,-5,-4,6,-4,-4,10,4,2,-7,-9,-9,6,3,3]],[[4,-7,-9,-2,3,-3,-7,-7,-7,8,-9,7,-7,4,-4,4]],[[-4,-7,-2,-7,6,-1,5,3,-8,5,7,7,-8,-6,9,10]],[[-8,6,7,4,5,6,5,1,-2,3,10,-5,-1,9,-10,-3]],[[6,-10,-3,6,-2,-10,-4,10,-7,7,-3,6,-3,3,-5,-4]],[[8,-4,8,10,4,7,-9,6,-10,-5,-7,-6,-5,-6,7,-1]],[[-3,5,7,-3,3,1,-7,-10,-1,-9,-6,-1,-3,-1,-6,-3]],[[-7,2,4,-7,7,1,-6,-2,-5,-7,5,-2,-6,9,5,-3]],[[-2,8,-10,5,4,1,4,-9,4,10,6,10,-4,6,-4,-4]],[[1,4,-7,-9,2,1,5,7,-7,-1,-8,5,-1,-1,-7,3]],[[7,1,4,-6,-4,-4,-8,10,-7,-8,-3,9,3,1,7,10]],[[-1,1,-3,-4,6,5,1,7,8,5,8,5,7,3,-2,-9]],[[4,-8,7,-5,10,-6,7,8,-1,-7,8,2,10,9,-8,2]]], dtype = "uint16")#candidate|1721|(16, 1, 16)|const|uint16
var_1722 = relay.var("var_1722", dtype = "uint16", shape = (16, 10, 16))#candidate|1722|(16, 10, 16)|var|uint16
bop_1723 = relay.equal(const_1721.astype('bool'), var_1722.astype('bool')) # shape=(16, 10, 16)
func_407_call = mod.get_global_var('func_407')
func_412_call = mutated_mod.get_global_var('func_412')
const_1727 = relay.const([False,False,True,False,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True], dtype = "bool")#candidate|1727|(819,)|const|bool
var_1728 = relay.var("var_1728", dtype = "uint16", shape = ())#candidate|1728|()|var|uint16
var_1729 = relay.var("var_1729", dtype = "float32", shape = (175, 1))#candidate|1729|(175, 1)|var|float32
call_1726 = relay.TupleGetItem(func_407_call(relay.reshape(const_1727.astype('bool'), [819,]), relay.reshape(var_1728.astype('uint16'), []), relay.reshape(var_1729.astype('float32'), [1, 175]), ), 4)
call_1730 = relay.TupleGetItem(func_412_call(relay.reshape(const_1727.astype('bool'), [819,]), relay.reshape(var_1728.astype('uint16'), []), relay.reshape(var_1729.astype('float32'), [1, 175]), ), 4)
uop_1732 = relay.log10(bop_1723.astype('float64')) # shape=(16, 10, 16)
func_1427_call = mod.get_global_var('func_1427')
func_1430_call = mutated_mod.get_global_var('func_1430')
var_1748 = relay.var("var_1748", dtype = "uint16", shape = (2,))#candidate|1748|(2,)|var|uint16
call_1747 = relay.TupleGetItem(func_1427_call(relay.reshape(var_1748.astype('uint16'), [2,])), 0)
call_1749 = relay.TupleGetItem(func_1430_call(relay.reshape(var_1748.astype('uint16'), [2,])), 0)
output = relay.Tuple([call_1726,const_1727,var_1728,var_1729,uop_1732,call_1747,var_1748,])
output2 = relay.Tuple([call_1730,const_1727,var_1728,var_1729,uop_1732,call_1749,var_1748,])
func_1753 = relay.Function([var_1722,var_1728,var_1729,var_1748,], output)
mod['func_1753'] = func_1753
mod = relay.transform.InferType()(mod)
var_1754 = relay.var("var_1754", dtype = "uint16", shape = (16, 10, 16))#candidate|1754|(16, 10, 16)|var|uint16
var_1755 = relay.var("var_1755", dtype = "uint16", shape = ())#candidate|1755|()|var|uint16
var_1756 = relay.var("var_1756", dtype = "float32", shape = (175, 1))#candidate|1756|(175, 1)|var|float32
var_1757 = relay.var("var_1757", dtype = "uint16", shape = (2,))#candidate|1757|(2,)|var|uint16
output = func_1753(var_1754,var_1755,var_1756,var_1757,)
func_1758 = relay.Function([var_1754,var_1755,var_1756,var_1757,], output)
mutated_mod['func_1758'] = func_1758
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1980 = relay.var("var_1980", dtype = "uint8", shape = (11, 4, 9))#candidate|1980|(11, 4, 9)|var|uint8
var_1981 = relay.var("var_1981", dtype = "uint8", shape = (11, 4, 9))#candidate|1981|(11, 4, 9)|var|uint8
bop_1982 = relay.maximum(var_1980.astype('uint8'), relay.reshape(var_1981.astype('uint8'), relay.shape_of(var_1980))) # shape=(11, 4, 9)
uop_1987 = relay.sinh(var_1981.astype('float32')) # shape=(11, 4, 9)
func_258_call = mod.get_global_var('func_258')
func_262_call = mutated_mod.get_global_var('func_262')
const_1990 = relay.const(6, dtype = "uint16")#candidate|1990|()|const|uint16
const_1991 = relay.const([[1,-1,-5,4,7,2,2,-2,-10,-7,-9,-4,-3,7,-8,-1,6,8],[9,5,-7,-1,-6,10,-1,9,-4,-2,-3,-10,-3,-8,2,-10,-7,10],[-1,-5,-3,5,1,-5,-6,-1,-7,9,-3,9,-2,-10,-4,-3,9,-4]], dtype = "uint16")#candidate|1991|(3, 18)|const|uint16
call_1989 = relay.TupleGetItem(func_258_call(relay.reshape(const_1990.astype('uint16'), []), relay.reshape(const_1991.astype('uint16'), [1, 6, 9]), ), 0)
call_1992 = relay.TupleGetItem(func_262_call(relay.reshape(const_1990.astype('uint16'), []), relay.reshape(const_1991.astype('uint16'), [1, 6, 9]), ), 0)
func_232_call = mod.get_global_var('func_232')
func_236_call = mutated_mod.get_global_var('func_236')
var_1998 = relay.var("var_1998", dtype = "float32", shape = (175,))#candidate|1998|(175,)|var|float32
call_1997 = relay.TupleGetItem(func_232_call(relay.reshape(const_1990.astype('float32'), []), relay.reshape(var_1998.astype('float32'), [5, 7, 5]), ), 0)
call_1999 = relay.TupleGetItem(func_236_call(relay.reshape(const_1990.astype('float32'), []), relay.reshape(var_1998.astype('float32'), [5, 7, 5]), ), 0)
output = relay.Tuple([bop_1982,uop_1987,call_1989,const_1990,const_1991,call_1997,var_1998,])
output2 = relay.Tuple([bop_1982,uop_1987,call_1992,const_1990,const_1991,call_1999,var_1998,])
func_2007 = relay.Function([var_1980,var_1981,var_1998,], output)
mod['func_2007'] = func_2007
mod = relay.transform.InferType()(mod)
var_2008 = relay.var("var_2008", dtype = "uint8", shape = (11, 4, 9))#candidate|2008|(11, 4, 9)|var|uint8
var_2009 = relay.var("var_2009", dtype = "uint8", shape = (11, 4, 9))#candidate|2009|(11, 4, 9)|var|uint8
var_2010 = relay.var("var_2010", dtype = "float32", shape = (175,))#candidate|2010|(175,)|var|float32
output = func_2007(var_2008,var_2009,var_2010,)
func_2011 = relay.Function([var_2008,var_2009,var_2010,], output)
mutated_mod['func_2011'] = func_2011
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2111 = relay.const([[2.244633,0.505189,-3.109024,9.946517,-3.992336,9.940083,9.250167,6.568971,5.881289,5.888963,6.682144],[-5.538595,-7.848170,6.176959,-2.779918,8.096714,-3.501473,-3.117102,-7.120697,-3.805940,-9.393212,-0.534556],[-8.956583,0.448334,1.882403,5.949162,9.815832,-0.447700,6.305374,-2.024610,-8.338881,3.936483,-9.790154],[0.731109,-2.033800,2.243492,-8.979750,-3.332623,1.690872,-3.625613,-3.906988,-1.081303,8.986504,-6.601447],[-4.670337,6.768178,-3.038101,9.646009,-8.960330,7.479509,4.592594,9.591330,-8.109128,-9.746676,3.605332],[0.898509,-5.881014,-7.801557,-3.956122,-3.005107,9.497411,3.749512,3.736060,-3.995486,-1.246210,-7.358882],[9.489709,4.241607,4.355000,8.367839,-7.562493,-7.641682,-7.596791,8.402709,5.682649,7.661479,3.655752],[-4.948947,-9.929543,-3.140891,2.907386,-2.674735,-3.884890,-7.462449,3.306867,-2.436338,-8.355134,0.240853],[3.917821,7.595385,-9.177557,4.088545,-4.025979,-0.812287,0.473905,5.531665,1.010975,6.836328,5.652931],[3.275393,6.120056,-5.560147,1.821060,4.054642,-7.719915,7.518960,9.630109,-2.186236,5.325317,-0.547984],[7.850003,6.271233,9.543193,-6.019216,-0.683441,-5.713356,-0.984824,-7.160129,-4.630726,-2.966086,-8.485511],[6.262427,8.425606,2.594351,6.326890,3.829473,6.401464,3.502777,2.903089,0.737148,-9.993402,7.812839],[5.000323,-6.831568,9.169504,-1.285889,-9.760837,-0.451175,-1.321306,-2.354806,8.473646,-6.079706,-8.286481],[-8.743206,-0.246292,-2.519427,7.311824,3.877791,2.431230,-0.848400,-9.596450,-3.255473,-0.006027,-2.496888],[8.129568,-6.852717,-0.934951,0.341337,4.367123,-9.742830,-1.279800,-4.169438,6.920637,-4.427634,5.578670]], dtype = "float64")#candidate|2111|(15, 11)|const|float64
uop_2112 = relay.atanh(const_2111.astype('float64')) # shape=(15, 11)
output = relay.Tuple([uop_2112,])
output2 = relay.Tuple([uop_2112,])
func_2133 = relay.Function([], output)
mod['func_2133'] = func_2133
mod = relay.transform.InferType()(mod)
output = func_2133()
func_2134 = relay.Function([], output)
mutated_mod['func_2134'] = func_2134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2133_call = mod.get_global_var('func_2133')
func_2134_call = mutated_mod.get_global_var('func_2134')
call_2144 = relay.TupleGetItem(func_2133_call(), 0)
call_2145 = relay.TupleGetItem(func_2134_call(), 0)
output = relay.Tuple([call_2144,])
output2 = relay.Tuple([call_2145,])
func_2152 = relay.Function([], output)
mod['func_2152'] = func_2152
mod = relay.transform.InferType()(mod)
mutated_mod['func_2152'] = func_2152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2152_call = mutated_mod.get_global_var('func_2152')
call_2153 = func_2152_call()
output = call_2153
func_2154 = relay.Function([], output)
mutated_mod['func_2154'] = func_2154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2133_call = mod.get_global_var('func_2133')
func_2134_call = mutated_mod.get_global_var('func_2134')
call_2186 = relay.TupleGetItem(func_2133_call(), 0)
call_2187 = relay.TupleGetItem(func_2134_call(), 0)
func_407_call = mod.get_global_var('func_407')
func_412_call = mutated_mod.get_global_var('func_412')
const_2205 = relay.const([True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False], dtype = "bool")#candidate|2205|(819,)|const|bool
const_2206 = relay.const(4, dtype = "uint16")#candidate|2206|()|const|uint16
var_2207 = relay.var("var_2207", dtype = "float32", shape = (175,))#candidate|2207|(175,)|var|float32
call_2204 = relay.TupleGetItem(func_407_call(relay.reshape(const_2205.astype('bool'), [819,]), relay.reshape(const_2206.astype('uint16'), []), relay.reshape(var_2207.astype('float32'), [1, 175]), ), 1)
call_2208 = relay.TupleGetItem(func_412_call(relay.reshape(const_2205.astype('bool'), [819,]), relay.reshape(const_2206.astype('uint16'), []), relay.reshape(var_2207.astype('float32'), [1, 175]), ), 1)
output = relay.Tuple([call_2186,call_2204,const_2205,const_2206,var_2207,])
output2 = relay.Tuple([call_2187,call_2208,const_2205,const_2206,var_2207,])
func_2216 = relay.Function([var_2207,], output)
mod['func_2216'] = func_2216
mod = relay.transform.InferType()(mod)
mutated_mod['func_2216'] = func_2216
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2217 = relay.var("var_2217", dtype = "float32", shape = (175,))#candidate|2217|(175,)|var|float32
func_2216_call = mutated_mod.get_global_var('func_2216')
call_2218 = func_2216_call(var_2217)
output = call_2218
func_2219 = relay.Function([var_2217], output)
mutated_mod['func_2219'] = func_2219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2133_call = mod.get_global_var('func_2133')
func_2134_call = mutated_mod.get_global_var('func_2134')
call_2233 = relay.TupleGetItem(func_2133_call(), 0)
call_2234 = relay.TupleGetItem(func_2134_call(), 0)
output = call_2233
output2 = call_2234
func_2238 = relay.Function([], output)
mod['func_2238'] = func_2238
mod = relay.transform.InferType()(mod)
output = func_2238()
func_2239 = relay.Function([], output)
mutated_mod['func_2239'] = func_2239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2255 = func_2238_call()
call_2256 = func_2238_call()
output = relay.Tuple([call_2255,])
output2 = relay.Tuple([call_2256,])
func_2268 = relay.Function([], output)
mod['func_2268'] = func_2268
mod = relay.transform.InferType()(mod)
output = func_2268()
func_2269 = relay.Function([], output)
mutated_mod['func_2269'] = func_2269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_2291 = relay.TupleGetItem(func_2152_call(), 0)
call_2292 = relay.TupleGetItem(func_2154_call(), 0)
func_407_call = mod.get_global_var('func_407')
func_412_call = mutated_mod.get_global_var('func_412')
var_2330 = relay.var("var_2330", dtype = "bool", shape = (819,))#candidate|2330|(819,)|var|bool
const_2331 = relay.const(3, dtype = "uint16")#candidate|2331|()|const|uint16
const_2332 = relay.const([9.737323,-8.198917,9.550829,-8.450244,9.788631,-7.966703,2.728715,5.936162,-7.781838,3.425375,6.520279,-1.429473,-1.650089,3.541416,7.955173,1.150346,-7.638290,7.792993,-3.522776,-5.286044,-6.533931,-9.242351,8.915056,6.432072,-0.363431,7.402565,5.562347,-6.156244,3.129733,-9.175862,-1.068536,-9.992413,9.694597,-0.427326,0.101529,0.178372,5.068718,-1.823403,0.891783,-2.201379,-6.328142,1.218577,-2.806241,2.279228,5.238543,-8.267463,5.232440,-3.196607,1.925233,-2.587426,-9.144666,-3.071050,-5.723365,-0.159491,6.021769,9.527437,-5.966276,2.263234,-8.840553,1.399292,-3.568358,0.384003,-6.821564,6.695168,-4.913674,-9.413538,8.557906,-6.282206,6.829263,-4.328448,-7.808264,-1.970119,-2.989848,9.020591,3.376985,0.359763,-9.867733,5.361960,-5.070674,-1.310807,2.228898,7.835819,-2.649100,-9.653981,-9.638235,-5.259689,-2.859828,-4.171579,-1.912888,6.769715,-7.460802,-6.173545,-3.035235,6.945702,-2.766672,6.062239,-7.359787,-2.568785,1.123096,3.337307,0.375151,-2.120335,-9.759850,3.371020,-4.081677,-3.525510,0.285878,8.559110,6.606955,-6.804493,9.864843,4.795273,7.963215,-0.896425,-7.520024,-3.879925,3.433282,1.248169,7.635216,-8.335468,8.779661,-0.401688,4.365399,-3.892920,-3.479075,-2.855422,8.363964,-2.589103,-7.934643,8.524886,-5.645962,-0.710595,-1.940186,0.623400,-2.272847,6.235135,1.909482,-9.387995,1.955431,6.475935,-1.707048,8.033168,9.360109,-9.129724,-6.679736,-5.686458,3.724412,-9.890981,-4.050828,-5.710168,-1.421169,-0.414713,7.883416,-2.602930,-7.504693,6.850218,-5.855318,-2.580090,-3.748711,8.848184,-3.051549,8.307575,-6.809089,7.998461,1.340233,-8.642463,5.000564,6.585952,7.957549,4.881314,5.971343,-9.733438,-9.281767,0.723164,2.088516], dtype = "float32")#candidate|2332|(175,)|const|float32
call_2329 = relay.TupleGetItem(func_407_call(relay.reshape(var_2330.astype('bool'), [819,]), relay.reshape(const_2331.astype('uint16'), []), relay.reshape(const_2332.astype('float32'), [1, 175]), ), 0)
call_2333 = relay.TupleGetItem(func_412_call(relay.reshape(var_2330.astype('bool'), [819,]), relay.reshape(const_2331.astype('uint16'), []), relay.reshape(const_2332.astype('float32'), [1, 175]), ), 0)
func_810_call = mod.get_global_var('func_810')
func_815_call = mutated_mod.get_global_var('func_815')
var_2343 = relay.var("var_2343", dtype = "float64", shape = (1215,))#candidate|2343|(1215,)|var|float64
call_2342 = relay.TupleGetItem(func_810_call(relay.reshape(var_2343.astype('float64'), [9, 9, 15]), relay.reshape(var_2343.astype('float64'), [9, 9, 15]), relay.reshape(const_2331.astype('uint16'), []), ), 4)
call_2344 = relay.TupleGetItem(func_815_call(relay.reshape(var_2343.astype('float64'), [9, 9, 15]), relay.reshape(var_2343.astype('float64'), [9, 9, 15]), relay.reshape(const_2331.astype('uint16'), []), ), 4)
func_407_call = mod.get_global_var('func_407')
func_412_call = mutated_mod.get_global_var('func_412')
call_2345 = relay.TupleGetItem(func_407_call(relay.reshape(var_2330.astype('bool'), [819,]), relay.reshape(const_2331.astype('uint16'), []), relay.reshape(const_2332.astype('float32'), [1, 175]), ), 6)
call_2346 = relay.TupleGetItem(func_412_call(relay.reshape(var_2330.astype('bool'), [819,]), relay.reshape(const_2331.astype('uint16'), []), relay.reshape(const_2332.astype('float32'), [1, 175]), ), 6)
func_1753_call = mod.get_global_var('func_1753')
func_1758_call = mutated_mod.get_global_var('func_1758')
var_2350 = relay.var("var_2350", dtype = "uint16", shape = (2560,))#candidate|2350|(2560,)|var|uint16
var_2351 = relay.var("var_2351", dtype = "uint16", shape = (2,))#candidate|2351|(2,)|var|uint16
call_2349 = relay.TupleGetItem(func_1753_call(relay.reshape(var_2350.astype('uint16'), [16, 10, 16]), relay.reshape(const_2331.astype('uint16'), []), relay.reshape(const_2332.astype('float32'), [175, 1]), relay.reshape(var_2351.astype('uint16'), [2,]), ), 3)
call_2352 = relay.TupleGetItem(func_1758_call(relay.reshape(var_2350.astype('uint16'), [16, 10, 16]), relay.reshape(const_2331.astype('uint16'), []), relay.reshape(const_2332.astype('float32'), [175, 1]), relay.reshape(var_2351.astype('uint16'), [2,]), ), 3)
var_2360 = relay.var("var_2360", dtype = "uint16", shape = (2560,))#candidate|2360|(2560,)|var|uint16
bop_2361 = relay.not_equal(var_2350.astype('bool'), relay.reshape(var_2360.astype('bool'), relay.shape_of(var_2350))) # shape=(2560,)
func_407_call = mod.get_global_var('func_407')
func_412_call = mutated_mod.get_global_var('func_412')
call_2378 = relay.TupleGetItem(func_407_call(relay.reshape(var_2330.astype('bool'), [819,]), relay.reshape(const_2331.astype('uint16'), []), relay.reshape(const_2332.astype('float32'), [1, 175]), ), 0)
call_2379 = relay.TupleGetItem(func_412_call(relay.reshape(var_2330.astype('bool'), [819,]), relay.reshape(const_2331.astype('uint16'), []), relay.reshape(const_2332.astype('float32'), [1, 175]), ), 0)
uop_2385 = relay.acos(var_2343.astype('float64')) # shape=(1215,)
output = relay.Tuple([call_2291,call_2329,var_2330,const_2331,const_2332,call_2342,call_2345,call_2349,var_2351,bop_2361,call_2378,uop_2385,])
output2 = relay.Tuple([call_2292,call_2333,var_2330,const_2331,const_2332,call_2344,call_2346,call_2352,var_2351,bop_2361,call_2379,uop_2385,])
func_2403 = relay.Function([var_2330,var_2343,var_2350,var_2351,var_2360,], output)
mod['func_2403'] = func_2403
mod = relay.transform.InferType()(mod)
var_2404 = relay.var("var_2404", dtype = "bool", shape = (819,))#candidate|2404|(819,)|var|bool
var_2405 = relay.var("var_2405", dtype = "float64", shape = (1215,))#candidate|2405|(1215,)|var|float64
var_2406 = relay.var("var_2406", dtype = "uint16", shape = (2560,))#candidate|2406|(2560,)|var|uint16
var_2407 = relay.var("var_2407", dtype = "uint16", shape = (2,))#candidate|2407|(2,)|var|uint16
var_2408 = relay.var("var_2408", dtype = "uint16", shape = (2560,))#candidate|2408|(2560,)|var|uint16
output = func_2403(var_2404,var_2405,var_2406,var_2407,var_2408,)
func_2409 = relay.Function([var_2404,var_2405,var_2406,var_2407,var_2408,], output)
mutated_mod['func_2409'] = func_2409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2268_call = mod.get_global_var('func_2268')
func_2269_call = mutated_mod.get_global_var('func_2269')
call_2419 = relay.TupleGetItem(func_2268_call(), 0)
call_2420 = relay.TupleGetItem(func_2269_call(), 0)
func_2007_call = mod.get_global_var('func_2007')
func_2011_call = mutated_mod.get_global_var('func_2011')
var_2422 = relay.var("var_2422", dtype = "uint8", shape = (396,))#candidate|2422|(396,)|var|uint8
const_2423 = relay.const([[1.130576,-2.588028,5.291215,4.254252,-6.033923],[-6.900927,-2.728226,-1.620197,-7.543710,4.340392],[-1.173537,-9.840841,0.634772,-0.489263,2.192728],[5.485729,6.517082,-8.638648,8.932919,-0.634658],[0.640100,2.586984,-3.473562,-9.007806,2.776742],[2.934845,-8.379075,-3.982294,3.566204,5.616405],[-3.948324,6.738826,-5.018888,-5.998142,-7.934833],[-6.384954,-4.667580,2.410554,0.804754,7.172163],[-0.964792,-4.028825,-2.032135,-5.746829,-8.907705],[-1.025719,-3.840025,-3.741627,6.746018,-9.906626],[9.369166,-0.357586,-9.966742,1.275928,0.185077],[-7.964093,7.544480,-0.606232,5.255788,-6.981761],[-9.282972,9.032841,-3.925694,-5.268702,-1.245152],[1.707699,2.321262,2.371408,-9.044232,1.947479],[-7.976242,6.552736,-2.361361,8.115515,-5.338503],[8.925346,7.628132,3.509639,-8.899017,4.014065],[-3.827647,2.663440,-9.236767,1.076064,0.251556],[9.028181,7.598206,3.482882,-5.975450,6.303704],[-2.548768,-4.605957,5.151561,-1.442311,9.073359],[4.673523,-5.318625,1.331024,1.594975,2.890245],[1.452931,-2.290761,2.028359,-2.185175,0.391296],[-6.496404,6.205284,3.917115,-0.031251,-4.661421],[0.448397,8.462816,-2.175294,0.869378,-3.010715],[-8.566978,6.796169,-3.373466,9.186502,-8.852791],[-1.289045,-4.870960,3.018256,6.762919,2.641620],[4.436846,6.715252,8.787865,7.352788,3.840106],[4.131410,3.917377,5.395551,-3.709152,1.529541],[5.357938,5.526364,5.977760,3.413411,3.324920],[-2.822971,6.054775,7.745071,-8.406985,5.153810],[-1.127663,2.192327,0.504652,4.504208,0.089570],[7.750278,8.989459,3.695165,6.640508,4.959471],[2.947171,-0.996476,6.383971,3.325282,-1.833598],[6.681874,-8.477730,6.708019,9.259390,9.764067],[5.131534,1.569472,1.920610,1.290067,5.855973],[4.405322,-2.587333,-4.330256,-7.155221,7.464437]], dtype = "float32")#candidate|2423|(35, 5)|const|float32
call_2421 = relay.TupleGetItem(func_2007_call(relay.reshape(var_2422.astype('uint8'), [11, 4, 9]), relay.reshape(var_2422.astype('uint8'), [11, 4, 9]), relay.reshape(const_2423.astype('float32'), [175,]), ), 4)
call_2424 = relay.TupleGetItem(func_2011_call(relay.reshape(var_2422.astype('uint8'), [11, 4, 9]), relay.reshape(var_2422.astype('uint8'), [11, 4, 9]), relay.reshape(const_2423.astype('float32'), [175,]), ), 4)
var_2432 = relay.var("var_2432", dtype = "uint16", shape = (3, 18))#candidate|2432|(3, 18)|var|uint16
bop_2433 = relay.less_equal(call_2421.astype('bool'), relay.reshape(var_2432.astype('bool'), relay.shape_of(call_2421))) # shape=(3, 18)
bop_2436 = relay.less_equal(call_2424.astype('bool'), relay.reshape(var_2432.astype('bool'), relay.shape_of(call_2424))) # shape=(3, 18)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
var_2441 = relay.var("var_2441", dtype = "bool", shape = (819,))#candidate|2441|(819,)|var|bool
call_2440 = relay.TupleGetItem(func_47_call(relay.reshape(var_2441.astype('bool'), [13, 9, 7])), 1)
call_2442 = relay.TupleGetItem(func_50_call(relay.reshape(var_2441.astype('bool'), [13, 9, 7])), 1)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2451 = func_2238_call()
call_2452 = func_2238_call()
output = relay.Tuple([call_2419,var_2422,const_2423,bop_2433,call_2440,var_2441,call_2451,])
output2 = relay.Tuple([call_2420,var_2422,const_2423,bop_2436,call_2442,var_2441,call_2452,])
func_2457 = relay.Function([var_2422,var_2432,var_2441,], output)
mod['func_2457'] = func_2457
mod = relay.transform.InferType()(mod)
mutated_mod['func_2457'] = func_2457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2457_call = mutated_mod.get_global_var('func_2457')
var_2459 = relay.var("var_2459", dtype = "uint8", shape = (396,))#candidate|2459|(396,)|var|uint8
var_2460 = relay.var("var_2460", dtype = "uint16", shape = (3, 18))#candidate|2460|(3, 18)|var|uint16
var_2461 = relay.var("var_2461", dtype = "bool", shape = (819,))#candidate|2461|(819,)|var|bool
call_2458 = func_2457_call(var_2459,var_2460,var_2461,)
output = call_2458
func_2462 = relay.Function([var_2459,var_2460,var_2461,], output)
mutated_mod['func_2462'] = func_2462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2507 = func_2238_call()
call_2508 = func_2238_call()
output = call_2507
output2 = call_2508
func_2509 = relay.Function([], output)
mod['func_2509'] = func_2509
mod = relay.transform.InferType()(mod)
mutated_mod['func_2509'] = func_2509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2509_call = mutated_mod.get_global_var('func_2509')
call_2510 = func_2509_call()
output = call_2510
func_2511 = relay.Function([], output)
mutated_mod['func_2511'] = func_2511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2515 = func_2238_call()
call_2516 = func_2238_call()
func_871_call = mod.get_global_var('func_871')
func_874_call = mutated_mod.get_global_var('func_874')
var_2548 = relay.var("var_2548", dtype = "uint16", shape = (2,))#candidate|2548|(2,)|var|uint16
call_2547 = func_871_call(relay.reshape(var_2548.astype('uint16'), [1, 2]))
call_2549 = func_871_call(relay.reshape(var_2548.astype('uint16'), [1, 2]))
output = relay.Tuple([call_2515,call_2547,var_2548,])
output2 = relay.Tuple([call_2516,call_2549,var_2548,])
func_2550 = relay.Function([var_2548,], output)
mod['func_2550'] = func_2550
mod = relay.transform.InferType()(mod)
var_2551 = relay.var("var_2551", dtype = "uint16", shape = (2,))#candidate|2551|(2,)|var|uint16
output = func_2550(var_2551)
func_2552 = relay.Function([var_2551], output)
mutated_mod['func_2552'] = func_2552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_2573 = relay.TupleGetItem(func_2152_call(), 0)
call_2574 = relay.TupleGetItem(func_2154_call(), 0)
func_871_call = mod.get_global_var('func_871')
func_874_call = mutated_mod.get_global_var('func_874')
const_2591 = relay.const([1,2], dtype = "uint16")#candidate|2591|(2,)|const|uint16
call_2590 = func_871_call(relay.reshape(const_2591.astype('uint16'), [1, 2]))
call_2592 = func_871_call(relay.reshape(const_2591.astype('uint16'), [1, 2]))
output = relay.Tuple([call_2573,call_2590,const_2591,])
output2 = relay.Tuple([call_2574,call_2592,const_2591,])
func_2600 = relay.Function([], output)
mod['func_2600'] = func_2600
mod = relay.transform.InferType()(mod)
output = func_2600()
func_2601 = relay.Function([], output)
mutated_mod['func_2601'] = func_2601
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2605 = relay.var("var_2605", dtype = "uint32", shape = (1, 13, 5))#candidate|2605|(1, 13, 5)|var|uint32
const_2606 = relay.const([[[3,1,-5,-1,-5],[-6,-9,6,-4,8],[7,1,-10,-7,-9],[10,-8,4,-3,-2],[9,-3,-2,-6,3],[6,3,-1,8,-7],[-3,-10,8,-6,1],[9,-8,10,1,-6],[-2,-4,10,2,-3],[6,8,9,-2,-6],[1,-4,-8,-8,-10],[5,7,-9,-5,6],[9,-4,-9,-2,-5]],[[7,6,6,-6,4],[1,10,-9,6,1],[1,-3,9,-9,-7],[1,-4,-5,-2,-7],[9,-6,-7,-7,10],[-2,-7,8,-10,-7],[3,1,5,-8,-9],[3,-4,-8,-5,-3],[-2,-8,3,-7,4],[8,-1,5,-6,-3],[9,-4,5,5,6],[5,-4,-9,10,7],[-9,1,5,6,-10]]], dtype = "uint32")#candidate|2606|(2, 13, 5)|const|uint32
bop_2607 = relay.add(var_2605.astype('uint32'), const_2606.astype('uint32')) # shape=(2, 13, 5)
func_2600_call = mod.get_global_var('func_2600')
func_2601_call = mutated_mod.get_global_var('func_2601')
call_2610 = relay.TupleGetItem(func_2600_call(), 1)
call_2611 = relay.TupleGetItem(func_2601_call(), 1)
output = relay.Tuple([bop_2607,call_2610,])
output2 = relay.Tuple([bop_2607,call_2611,])
func_2628 = relay.Function([var_2605,], output)
mod['func_2628'] = func_2628
mod = relay.transform.InferType()(mod)
var_2629 = relay.var("var_2629", dtype = "uint32", shape = (1, 13, 5))#candidate|2629|(1, 13, 5)|var|uint32
output = func_2628(var_2629)
func_2630 = relay.Function([var_2629], output)
mutated_mod['func_2630'] = func_2630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2600_call = mod.get_global_var('func_2600')
func_2601_call = mutated_mod.get_global_var('func_2601')
call_2639 = relay.TupleGetItem(func_2600_call(), 2)
call_2640 = relay.TupleGetItem(func_2601_call(), 2)
output = call_2639
output2 = call_2640
func_2649 = relay.Function([], output)
mod['func_2649'] = func_2649
mod = relay.transform.InferType()(mod)
output = func_2649()
func_2650 = relay.Function([], output)
mutated_mod['func_2650'] = func_2650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2600_call = mod.get_global_var('func_2600')
func_2601_call = mutated_mod.get_global_var('func_2601')
call_2656 = relay.TupleGetItem(func_2600_call(), 0)
call_2657 = relay.TupleGetItem(func_2601_call(), 0)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_2684 = func_2649_call()
call_2685 = func_2649_call()
output = relay.Tuple([call_2656,call_2684,])
output2 = relay.Tuple([call_2657,call_2685,])
func_2717 = relay.Function([], output)
mod['func_2717'] = func_2717
mod = relay.transform.InferType()(mod)
mutated_mod['func_2717'] = func_2717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2717_call = mutated_mod.get_global_var('func_2717')
call_2718 = func_2717_call()
output = call_2718
func_2719 = relay.Function([], output)
mutated_mod['func_2719'] = func_2719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_2725 = relay.TupleGetItem(func_2717_call(), 0)
call_2726 = relay.TupleGetItem(func_2719_call(), 0)
func_1055_call = mod.get_global_var('func_1055')
func_1058_call = mutated_mod.get_global_var('func_1058')
var_2733 = relay.var("var_2733", dtype = "float64", shape = (198,))#candidate|2733|(198,)|var|float64
call_2732 = func_1055_call(relay.reshape(var_2733.astype('float64'), [3, 11, 6]))
call_2734 = func_1055_call(relay.reshape(var_2733.astype('float64'), [3, 11, 6]))
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_2736 = relay.TupleGetItem(func_2152_call(), 0)
call_2737 = relay.TupleGetItem(func_2154_call(), 0)
func_930_call = mod.get_global_var('func_930')
func_934_call = mutated_mod.get_global_var('func_934')
var_2739 = relay.var("var_2739", dtype = "float64", shape = ())#candidate|2739|()|var|float64
const_2740 = relay.const([[-7,9]], dtype = "uint16")#candidate|2740|(1, 2)|const|uint16
call_2738 = relay.TupleGetItem(func_930_call(relay.reshape(var_2739.astype('float64'), []), relay.reshape(const_2740.astype('uint16'), [2, 1]), ), 1)
call_2741 = relay.TupleGetItem(func_934_call(relay.reshape(var_2739.astype('float64'), []), relay.reshape(const_2740.astype('uint16'), [2, 1]), ), 1)
output = relay.Tuple([call_2725,call_2732,var_2733,call_2736,call_2738,var_2739,const_2740,])
output2 = relay.Tuple([call_2726,call_2734,var_2733,call_2737,call_2741,var_2739,const_2740,])
func_2756 = relay.Function([var_2733,var_2739,], output)
mod['func_2756'] = func_2756
mod = relay.transform.InferType()(mod)
var_2757 = relay.var("var_2757", dtype = "float64", shape = (198,))#candidate|2757|(198,)|var|float64
var_2758 = relay.var("var_2758", dtype = "float64", shape = ())#candidate|2758|()|var|float64
output = func_2756(var_2757,var_2758,)
func_2759 = relay.Function([var_2757,var_2758,], output)
mutated_mod['func_2759'] = func_2759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2600_call = mod.get_global_var('func_2600')
func_2601_call = mutated_mod.get_global_var('func_2601')
call_2772 = relay.TupleGetItem(func_2600_call(), 1)
call_2773 = relay.TupleGetItem(func_2601_call(), 1)
func_871_call = mod.get_global_var('func_871')
func_874_call = mutated_mod.get_global_var('func_874')
call_2778 = func_871_call(relay.reshape(call_2772.astype('uint16'), [1, 2]))
call_2779 = func_871_call(relay.reshape(call_2772.astype('uint16'), [1, 2]))
output = relay.Tuple([call_2772,call_2778,])
output2 = relay.Tuple([call_2773,call_2779,])
func_2781 = relay.Function([], output)
mod['func_2781'] = func_2781
mod = relay.transform.InferType()(mod)
output = func_2781()
func_2782 = relay.Function([], output)
mutated_mod['func_2782'] = func_2782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_2800 = relay.TupleGetItem(func_2152_call(), 0)
call_2801 = relay.TupleGetItem(func_2154_call(), 0)
func_1753_call = mod.get_global_var('func_1753')
func_1758_call = mutated_mod.get_global_var('func_1758')
var_2824 = relay.var("var_2824", dtype = "uint16", shape = (128, 20))#candidate|2824|(128, 20)|var|uint16
const_2825 = relay.const(6, dtype = "uint16")#candidate|2825|()|const|uint16
const_2826 = relay.const([[-8.098635],[2.302317],[5.769725],[-7.034097],[-2.756182],[8.480840],[-5.455730],[9.923649],[7.533568],[7.823822],[-2.804246],[-6.577052],[3.628682],[-5.292916],[8.443744],[2.116089],[-0.552567],[-2.090078],[8.393277],[-9.926740],[2.270354],[-2.407894],[-5.544996],[-3.217075],[-4.746914],[-4.620928],[-1.952399],[-8.529618],[-3.784252],[6.856651],[-9.295128],[3.361835],[1.985417],[-2.791265],[-3.788672],[-4.326543],[-7.232897],[-1.938496],[-7.300250],[-0.975033],[-2.618467],[0.625905],[3.546171],[-4.202974],[-5.262203],[0.148053],[-7.660810],[-2.853315],[-7.554011],[-3.552946],[6.282315],[-7.118169],[-9.890194],[-5.741465],[-8.202883],[0.424954],[3.288935],[5.603503],[-1.427440],[-1.176918],[0.634368],[8.891546],[4.719521],[6.246267],[3.592733],[-7.877704],[-2.284806],[-8.153737],[1.683557],[5.986190],[-3.099602],[-6.517648],[9.350333],[-9.595002],[-1.405107],[-2.212697],[4.726180],[0.846670],[9.799238],[-3.990214],[9.740910],[-0.640175],[-7.205816],[-6.883942],[9.313573],[5.384114],[-1.479252],[-7.001703],[1.038724],[9.776297],[4.938090],[6.830885],[-1.094161],[0.770505],[1.898288],[-1.367960],[4.253454],[-2.554914],[3.836565],[9.892601],[-4.651373],[-6.051268],[5.566263],[-7.749494],[-1.729666],[-0.077030],[1.825122],[-7.679549],[-7.386692],[-6.311816],[6.259271],[-2.793495],[5.196854],[-4.777266],[7.577977],[5.739010],[-4.645750],[-6.088243],[-0.455271],[-6.259509],[4.977159],[7.186628],[-1.303700],[-9.093160],[3.687433],[-8.755565],[0.240585],[2.492070],[4.684931],[2.039740],[-4.374547],[-1.743168],[0.723879],[-8.925350],[1.682060],[-8.805321],[9.770078],[-2.624150],[7.882873],[-8.551850],[5.666519],[8.866426],[-7.978112],[8.682848],[3.179347],[-2.617093],[8.637066],[-1.961305],[-0.647174],[9.946208],[-8.378487],[-9.085083],[2.079573],[8.920918],[6.354785],[8.035338],[3.416077],[4.245677],[-0.800528],[9.014757],[1.674307],[2.060198],[0.336721],[9.079427],[-0.212160],[0.521594],[-9.929568],[-4.680630],[-5.240318],[-5.607988],[2.430544],[-5.364758],[5.667157],[-3.511599],[-3.320625]], dtype = "float32")#candidate|2826|(175, 1)|const|float32
const_2827 = relay.const([-7,1], dtype = "uint16")#candidate|2827|(2,)|const|uint16
call_2823 = relay.TupleGetItem(func_1753_call(relay.reshape(var_2824.astype('uint16'), [16, 10, 16]), relay.reshape(const_2825.astype('uint16'), []), relay.reshape(const_2826.astype('float32'), [175, 1]), relay.reshape(const_2827.astype('uint16'), [2,]), ), 4)
call_2828 = relay.TupleGetItem(func_1758_call(relay.reshape(var_2824.astype('uint16'), [16, 10, 16]), relay.reshape(const_2825.astype('uint16'), []), relay.reshape(const_2826.astype('float32'), [175, 1]), relay.reshape(const_2827.astype('uint16'), [2,]), ), 4)
output = relay.Tuple([call_2800,call_2823,var_2824,const_2825,const_2826,const_2827,])
output2 = relay.Tuple([call_2801,call_2828,var_2824,const_2825,const_2826,const_2827,])
func_2833 = relay.Function([var_2824,], output)
mod['func_2833'] = func_2833
mod = relay.transform.InferType()(mod)
var_2834 = relay.var("var_2834", dtype = "uint16", shape = (128, 20))#candidate|2834|(128, 20)|var|uint16
output = func_2833(var_2834)
func_2835 = relay.Function([var_2834], output)
mutated_mod['func_2835'] = func_2835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_2926 = relay.TupleGetItem(func_2152_call(), 0)
call_2927 = relay.TupleGetItem(func_2154_call(), 0)
output = call_2926
output2 = call_2927
func_2953 = relay.Function([], output)
mod['func_2953'] = func_2953
mod = relay.transform.InferType()(mod)
output = func_2953()
func_2954 = relay.Function([], output)
mutated_mod['func_2954'] = func_2954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2268_call = mod.get_global_var('func_2268')
func_2269_call = mutated_mod.get_global_var('func_2269')
call_2980 = relay.TupleGetItem(func_2268_call(), 0)
call_2981 = relay.TupleGetItem(func_2269_call(), 0)
output = relay.Tuple([call_2980,])
output2 = relay.Tuple([call_2981,])
func_2990 = relay.Function([], output)
mod['func_2990'] = func_2990
mod = relay.transform.InferType()(mod)
mutated_mod['func_2990'] = func_2990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2990_call = mutated_mod.get_global_var('func_2990')
call_2991 = func_2990_call()
output = call_2991
func_2992 = relay.Function([], output)
mutated_mod['func_2992'] = func_2992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2990_call = mod.get_global_var('func_2990')
func_2992_call = mutated_mod.get_global_var('func_2992')
call_3030 = relay.TupleGetItem(func_2990_call(), 0)
call_3031 = relay.TupleGetItem(func_2992_call(), 0)
func_2953_call = mod.get_global_var('func_2953')
func_2954_call = mutated_mod.get_global_var('func_2954')
call_3032 = func_2953_call()
call_3033 = func_2953_call()
output = relay.Tuple([call_3030,call_3032,])
output2 = relay.Tuple([call_3031,call_3033,])
func_3042 = relay.Function([], output)
mod['func_3042'] = func_3042
mod = relay.transform.InferType()(mod)
output = func_3042()
func_3043 = relay.Function([], output)
mutated_mod['func_3043'] = func_3043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_3058 = func_2649_call()
call_3059 = func_2649_call()
output = call_3058
output2 = call_3059
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
const_3063 = relay.const([[[0.713767,-5.285244],[4.825614,6.190782],[-7.248949,0.661540],[3.612740,-6.651179],[-1.939831,-0.208539]],[[-1.187178,-1.304991],[1.270600,-1.366580],[0.801046,3.860043],[-3.800768,-5.041508],[-3.761622,-5.194343]],[[-3.880265,-4.336003],[-1.692373,-3.433165],[-1.472805,-6.789410],[-9.277918,-9.563532],[1.649951,0.379017]]], dtype = "float64")#candidate|3063|(3, 5, 2)|const|float64
var_3064 = relay.var("var_3064", dtype = "float64", shape = (3, 5, 2))#candidate|3064|(3, 5, 2)|var|float64
bop_3065 = relay.greater(const_3063.astype('bool'), relay.reshape(var_3064.astype('bool'), relay.shape_of(const_3063))) # shape=(3, 5, 2)
output = relay.Tuple([bop_3065,])
output2 = relay.Tuple([bop_3065,])
func_3092 = relay.Function([var_3064,], output)
mod['func_3092'] = func_3092
mod = relay.transform.InferType()(mod)
var_3093 = relay.var("var_3093", dtype = "float64", shape = (3, 5, 2))#candidate|3093|(3, 5, 2)|var|float64
output = func_3092(var_3093)
func_3094 = relay.Function([var_3093], output)
mutated_mod['func_3094'] = func_3094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_3123 = relay.TupleGetItem(func_2717_call(), 0)
call_3124 = relay.TupleGetItem(func_2719_call(), 0)
output = call_3123
output2 = call_3124
func_3128 = relay.Function([], output)
mod['func_3128'] = func_3128
mod = relay.transform.InferType()(mod)
output = func_3128()
func_3129 = relay.Function([], output)
mutated_mod['func_3129'] = func_3129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_3154 = func_3060_call()
call_3155 = func_3060_call()
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_3157 = func_2238_call()
call_3158 = func_2238_call()
func_2756_call = mod.get_global_var('func_2756')
func_2759_call = mutated_mod.get_global_var('func_2759')
const_3163 = relay.const([-9.794232,-8.964851,-6.377005,-3.111443,0.729205,-1.207617,8.656571,1.625185,9.576311,5.067799,-6.423475,4.401633,4.214241,-8.788598,-2.546605,7.012586,9.707427,8.750014,0.393333,-0.495739,-7.478435,-8.979389,7.729571,0.432561,-8.740060,4.766858,6.079167,-3.597254,9.163606,8.673095,-6.478251,-0.710914,-1.049492,2.847268,-1.450048,-3.053330,-9.889681,-3.636836,-3.808925,6.166963,-2.291888,7.736842,8.784535,1.063424,7.611361,4.502519,8.441430,6.782106,5.488871,9.102744,-1.467458,-2.263913,1.643558,-8.872780,5.414476,-3.354765,5.549605,7.628643,6.201898,2.864214,-8.649240,-6.498132,8.320478,5.180112,1.227739,-0.860360,1.991000,-8.771361,5.939688,-3.959774,-5.227769,-6.485472,3.286741,3.826201,-3.703795,0.265300,1.873332,-1.476149,2.512297,0.709881,9.309264,-1.687021,-0.596344,5.080681,2.778063,-9.665935,-0.981845,6.347727,9.224159,2.518605,-7.455641,-2.211393,-4.695026,-9.744290,-2.183135,-3.309581,4.133497,-1.549386,-0.445130,6.870638,-2.085633,8.905900,-9.731249,-1.013578,9.309391,-3.649650,-2.954411,6.749968,5.975885,-2.933620,7.010888,2.470209,8.190649,8.318710,9.466124,0.865109,-7.817081,3.832863,-7.537027,-0.297752,0.739570,3.947588,1.820275,-9.200422,-9.588474,6.233622,-3.719882,-2.714960,-5.852810,2.047680,-5.017350,0.490024,6.104501,7.213495,-9.998700,-6.174123,-3.106046,7.413987,-2.422024,8.522433,-9.937354,4.682986,5.539295,-9.839853,9.889694,-9.835598,4.233854,-2.041458,-8.616015,-9.117473,-6.267687,-4.635644,-8.751847,-3.232984,3.522888,1.229831,-3.291954,-6.554217,-6.046892,-0.964233,-4.704079,9.721906,-5.098486,4.933626,9.456091,-6.168784,-8.382480,8.837236,-0.787243,4.332854,1.618130,-6.732513,6.989090,7.981996,1.600454,0.391194,-1.653911,1.127079,9.296247,4.410860,-5.215082,-7.309735,-5.176403,4.106626,4.632403,2.552455,1.535636,7.462319,-3.745083,-1.213258,-7.407329,-3.681820,-1.236712,7.281509,-9.851456,8.220690,-4.179550,7.593510], dtype = "float64")#candidate|3163|(198,)|const|float64
const_3164 = relay.const(-4.957800, dtype = "float64")#candidate|3164|()|const|float64
call_3162 = relay.TupleGetItem(func_2756_call(relay.reshape(const_3163.astype('float64'), [198,]), relay.reshape(const_3164.astype('float64'), []), ), 0)
call_3165 = relay.TupleGetItem(func_2759_call(relay.reshape(const_3163.astype('float64'), [198,]), relay.reshape(const_3164.astype('float64'), []), ), 0)
output = relay.Tuple([call_3154,call_3157,call_3162,const_3163,const_3164,])
output2 = relay.Tuple([call_3155,call_3158,call_3165,const_3163,const_3164,])
func_3169 = relay.Function([], output)
mod['func_3169'] = func_3169
mod = relay.transform.InferType()(mod)
output = func_3169()
func_3170 = relay.Function([], output)
mutated_mod['func_3170'] = func_3170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_3171 = relay.TupleGetItem(func_2717_call(), 1)
call_3172 = relay.TupleGetItem(func_2719_call(), 1)
func_1753_call = mod.get_global_var('func_1753')
func_1758_call = mutated_mod.get_global_var('func_1758')
var_3184 = relay.var("var_3184", dtype = "uint16", shape = (2560,))#candidate|3184|(2560,)|var|uint16
const_3185 = relay.const(9, dtype = "uint16")#candidate|3185|()|const|uint16
const_3186 = relay.const([-3.164732,-9.775765,-7.455427,8.267462,5.217738,7.713106,-6.379457,2.181591,9.270423,1.690604,8.595904,-8.693135,8.143546,4.394353,-4.441636,-2.571069,1.765459,5.245329,0.365169,-2.946849,-0.022417,-6.671359,4.643781,6.507307,8.582612,-5.676313,-0.015905,1.392553,-8.756205,-8.118784,-5.532385,7.701531,-1.643146,7.118363,9.987139,-3.206887,-2.377154,-2.632302,-6.748100,-9.175421,-0.784078,-0.351337,3.706576,-2.123370,-2.132304,-6.872181,-7.901100,0.810064,-8.604657,-3.893960,-8.546510,-8.211205,1.243684,-9.110906,-1.630054,5.421252,9.158442,7.868308,-2.886441,-9.548218,7.023595,9.304926,-2.247464,-0.828177,6.228049,-9.519390,5.855096,-9.547854,-2.506982,-6.319711,1.099831,6.582085,9.287090,-3.694568,0.916444,4.915334,9.894897,-8.273161,8.423876,1.712664,7.357345,-5.517306,-8.074806,9.760214,2.473348,0.779146,4.823397,2.346082,-8.213694,-9.564145,-3.453340,-3.299338,-4.282214,8.747266,2.031975,4.265506,-9.693244,1.711080,-4.161354,5.091817,-8.231573,0.132943,-9.734765,-2.805528,-8.010886,-3.632113,-9.225936,-3.587197,1.976659,-7.562804,-1.282774,2.508441,3.648586,3.684556,7.868848,1.821994,-6.383058,0.028998,9.220249,8.243225,6.078961,-0.794300,-2.839766,-4.856778,-8.526017,-7.393928,-6.440548,-0.209022,-0.971838,-4.496181,-8.689544,5.929556,-9.337045,5.847950,-3.770279,5.469832,-3.313171,-3.732486,-2.816755,-6.193756,3.956015,-8.293851,-7.403974,-6.940849,-5.258565,-9.323454,-4.376720,0.611490,9.825730,5.940994,1.910981,5.455412,-5.258260,-1.717419,-7.807668,-2.642354,4.215179,-9.837281,7.907947,-9.676020,9.241368,-4.059873,-5.335893,-9.582906,8.519674,-5.397288,-2.519552,-3.621622,9.974860,2.977673,-7.335587,1.364141,-1.561039,9.820714,-0.938446], dtype = "float32")#candidate|3186|(175,)|const|float32
call_3183 = relay.TupleGetItem(func_1753_call(relay.reshape(var_3184.astype('uint16'), [16, 10, 16]), relay.reshape(const_3185.astype('uint16'), []), relay.reshape(const_3186.astype('float32'), [175, 1]), relay.reshape(call_3171.astype('uint16'), [2,]), ), 4)
call_3187 = relay.TupleGetItem(func_1758_call(relay.reshape(var_3184.astype('uint16'), [16, 10, 16]), relay.reshape(const_3185.astype('uint16'), []), relay.reshape(const_3186.astype('float32'), [175, 1]), relay.reshape(call_3171.astype('uint16'), [2,]), ), 4)
output = relay.Tuple([call_3171,call_3183,var_3184,const_3185,const_3186,])
output2 = relay.Tuple([call_3172,call_3187,var_3184,const_3185,const_3186,])
func_3190 = relay.Function([var_3184,], output)
mod['func_3190'] = func_3190
mod = relay.transform.InferType()(mod)
var_3191 = relay.var("var_3191", dtype = "uint16", shape = (2560,))#candidate|3191|(2560,)|var|uint16
output = func_3190(var_3191)
func_3192 = relay.Function([var_3191], output)
mutated_mod['func_3192'] = func_3192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_3194 = func_3060_call()
call_3195 = func_3060_call()
output = relay.Tuple([call_3194,])
output2 = relay.Tuple([call_3195,])
func_3216 = relay.Function([], output)
mod['func_3216'] = func_3216
mod = relay.transform.InferType()(mod)
output = func_3216()
func_3217 = relay.Function([], output)
mutated_mod['func_3217'] = func_3217
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3300 = relay.var("var_3300", dtype = "float64", shape = (7, 4, 12))#candidate|3300|(7, 4, 12)|var|float64
uop_3301 = relay.exp(var_3300.astype('float64')) # shape=(7, 4, 12)
output = uop_3301
output2 = uop_3301
func_3311 = relay.Function([var_3300,], output)
mod['func_3311'] = func_3311
mod = relay.transform.InferType()(mod)
var_3312 = relay.var("var_3312", dtype = "float64", shape = (7, 4, 12))#candidate|3312|(7, 4, 12)|var|float64
output = func_3311(var_3312)
func_3313 = relay.Function([var_3312], output)
mutated_mod['func_3313'] = func_3313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2953_call = mod.get_global_var('func_2953')
func_2954_call = mutated_mod.get_global_var('func_2954')
call_3320 = func_2953_call()
call_3321 = func_2953_call()
output = relay.Tuple([call_3320,])
output2 = relay.Tuple([call_3321,])
func_3332 = relay.Function([], output)
mod['func_3332'] = func_3332
mod = relay.transform.InferType()(mod)
output = func_3332()
func_3333 = relay.Function([], output)
mutated_mod['func_3333'] = func_3333
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3336 = relay.const([[[-0.990530,-3.394405,5.642195,8.417717,6.238546,2.846991,2.107416,7.327359,-0.192932,2.618647,-4.441237,-7.743417,3.974707,7.365269,6.082787]],[[-5.772545,6.402198,3.742087,-7.075899,-2.658602,2.116614,-4.716811,-1.848010,-1.154229,-8.123309,0.172840,-4.390341,-4.198139,4.023349,-0.034426]],[[-2.442895,-8.527076,7.610686,2.144402,5.931458,-9.862491,0.748756,2.155216,-8.010238,1.325498,8.064517,-0.663162,-6.000821,3.061597,-0.183208]],[[7.231018,-2.036152,-9.167059,8.632416,2.663930,4.872339,6.144761,-7.257167,-4.638336,0.951340,2.871750,-2.726396,-6.937642,0.201151,0.739553]],[[3.035065,-9.510077,-4.082835,8.578891,-0.894500,-1.636924,-4.698424,8.375545,-3.365694,-2.372900,1.128294,-6.978504,4.618544,-9.874702,-1.238286]],[[-3.888752,-1.299804,5.068739,1.366052,-8.641227,-8.532700,-9.454358,7.787711,9.192493,8.030638,3.324548,-9.526501,0.393878,-7.070630,-5.043181]],[[5.440328,-6.323447,5.243563,-8.826854,-1.111850,0.372688,-9.024191,-0.707009,1.973839,5.062037,8.038014,9.204623,5.546560,6.594115,-3.913562]],[[-9.364490,-2.294194,-9.841712,1.782860,-5.859622,6.235800,-2.319729,9.696476,6.281367,-4.091043,-2.861379,9.115298,1.440922,-9.747935,-9.588502]],[[-2.268329,-2.799486,4.872726,3.804773,4.476915,1.325744,9.294683,-4.417600,-0.077992,2.333093,1.946011,-8.346724,4.410418,4.002902,-7.710200]],[[-6.997027,-3.229312,4.899811,9.874797,-1.345087,-0.215862,-8.451630,0.853483,6.244493,-0.129546,2.962315,-5.921171,4.182159,0.755485,2.012130]],[[-7.129443,4.837204,-6.311054,6.436872,3.951296,-8.534173,8.936292,9.724487,-9.651884,-2.761726,0.473567,-7.177472,8.661340,9.751071,-4.014337]]], dtype = "float32")#candidate|3336|(11, 1, 15)|const|float32
uop_3337 = relay.log(const_3336.astype('float32')) # shape=(11, 1, 15)
func_3332_call = mod.get_global_var('func_3332')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_3343 = relay.TupleGetItem(func_3332_call(), 0)
call_3344 = relay.TupleGetItem(func_3333_call(), 0)
var_3345 = relay.var("var_3345", dtype = "float32", shape = (11, 2, 15))#candidate|3345|(11, 2, 15)|var|float32
bop_3346 = relay.less(uop_3337.astype('bool'), var_3345.astype('bool')) # shape=(11, 2, 15)
output = relay.Tuple([call_3343,bop_3346,])
output2 = relay.Tuple([call_3344,bop_3346,])
func_3353 = relay.Function([var_3345,], output)
mod['func_3353'] = func_3353
mod = relay.transform.InferType()(mod)
mutated_mod['func_3353'] = func_3353
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3354 = relay.var("var_3354", dtype = "float32", shape = (11, 2, 15))#candidate|3354|(11, 2, 15)|var|float32
func_3353_call = mutated_mod.get_global_var('func_3353')
call_3355 = func_3353_call(var_3354)
output = call_3355
func_3356 = relay.Function([var_3354], output)
mutated_mod['func_3356'] = func_3356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3169_call = mod.get_global_var('func_3169')
func_3170_call = mutated_mod.get_global_var('func_3170')
call_3381 = relay.TupleGetItem(func_3169_call(), 2)
call_3382 = relay.TupleGetItem(func_3170_call(), 2)
func_2628_call = mod.get_global_var('func_2628')
func_2630_call = mutated_mod.get_global_var('func_2630')
const_3391 = relay.const([[7,3,-4,-8,-8],[-10,-8,10,-1,4],[4,4,-3,10,6],[-5,-3,-10,7,-3],[-10,3,9,-4,6],[8,7,-1,-10,2],[6,-10,6,-7,-10],[8,-5,-8,6,7],[-7,-3,-8,-7,-7],[6,-6,4,8,5],[-2,-8,3,3,5],[1,-4,-8,-1,3],[-6,3,7,2,-9]], dtype = "uint32")#candidate|3391|(13, 5)|const|uint32
call_3390 = relay.TupleGetItem(func_2628_call(relay.reshape(const_3391.astype('uint32'), [1, 13, 5])), 0)
call_3392 = relay.TupleGetItem(func_2630_call(relay.reshape(const_3391.astype('uint32'), [1, 13, 5])), 0)
output = relay.Tuple([call_3381,call_3390,const_3391,])
output2 = relay.Tuple([call_3382,call_3392,const_3391,])
func_3398 = relay.Function([], output)
mod['func_3398'] = func_3398
mod = relay.transform.InferType()(mod)
mutated_mod['func_3398'] = func_3398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3398_call = mutated_mod.get_global_var('func_3398')
call_3399 = func_3398_call()
output = call_3399
func_3400 = relay.Function([], output)
mutated_mod['func_3400'] = func_3400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2953_call = mod.get_global_var('func_2953')
func_2954_call = mutated_mod.get_global_var('func_2954')
call_3428 = func_2953_call()
call_3429 = func_2953_call()
output = relay.Tuple([call_3428,])
output2 = relay.Tuple([call_3429,])
func_3456 = relay.Function([], output)
mod['func_3456'] = func_3456
mod = relay.transform.InferType()(mod)
output = func_3456()
func_3457 = relay.Function([], output)
mutated_mod['func_3457'] = func_3457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_3470 = relay.TupleGetItem(func_2717_call(), 1)
call_3471 = relay.TupleGetItem(func_2719_call(), 1)
func_1055_call = mod.get_global_var('func_1055')
func_1058_call = mutated_mod.get_global_var('func_1058')
const_3483 = relay.const([-0.552437,3.527420,-2.809076,0.527917,-6.675230,-1.242567,-6.692664,-6.402118,-8.287291,0.531629,0.788311,-8.972200,-1.152779,-0.668247,-8.424690,5.261891,-2.079181,-3.930123,6.664544,6.693862,1.882298,-4.887109,5.805020,-0.715381,-8.101097,2.350492,4.942680,9.672860,-8.891258,0.332739,7.623451,8.403551,-1.834838,-6.521433,1.909387,2.383162,0.199803,1.042612,-3.007038,-8.888277,0.025632,3.670676,3.106519,-1.893615,-5.445695,-2.844338,-6.376780,-8.844076,8.354837,-9.539650,-2.970220,-3.698891,3.871589,-3.398517,7.413346,-2.613397,-6.687226,7.895437,0.168350,0.102510,-9.675951,9.259274,4.329659,1.736317,-0.610847,-0.990848,1.529558,-5.938759,-4.813094,4.658110,7.399111,-2.219561,3.103856,4.321390,6.842781,-7.901989,-7.385502,-3.847198,9.280244,6.903191,6.584666,-7.387766,-3.440682,2.331313,0.748173,-1.845487,0.735969,8.530130,0.944394,9.504373,4.062676,-9.821586,7.023923,-5.562894,-8.972115,-8.442145,7.694231,-7.317176,2.085850,-0.278982,-5.993633,9.149844,7.912588,-9.044596,2.410559,9.261458,-8.258639,-2.615047,-7.171619,-4.038536,-3.896656,-4.331499,-2.326146,0.537683,-0.062685,-2.402639,4.643591,-4.029908,-4.149686,4.647401,-9.996052,3.830436,-6.109732,-4.548825,-7.325101,7.049500,1.598328,-6.102276,-5.179310,5.026269,9.921958,-6.681995,5.413636,8.885852,2.525528,8.079639,8.475030,-4.534714,7.618988,-0.492242,-5.932342,-6.132527,6.586077,2.449125,2.414781,-9.833807,-8.707145,6.418142,-1.344468,-5.296896,7.328703,7.927797,-9.180610,-1.599258,4.542725,1.099435,-4.158454,1.739063,-3.826100,1.863600,-8.267745,-2.135470,-4.336748,-6.880234,-0.274501,9.642417,6.931720,-4.894708,-8.366334,0.698825,2.504143,6.940097,-1.751615,6.236496,2.572193,-2.658562,-6.747996,6.836827,-1.871322,1.750073,-8.368370,-5.934227,-4.250520,2.281303,8.232811,-2.383879,5.867124,-4.094495,-3.188843,-9.550334,2.481473,9.097801,9.009483,-9.586431,3.909153,-8.901503,-6.620917,8.692991], dtype = "float64")#candidate|3483|(198,)|const|float64
call_3482 = func_1055_call(relay.reshape(const_3483.astype('float64'), [3, 11, 6]))
call_3484 = func_1055_call(relay.reshape(const_3483.astype('float64'), [3, 11, 6]))
output = relay.Tuple([call_3470,call_3482,const_3483,])
output2 = relay.Tuple([call_3471,call_3484,const_3483,])
func_3493 = relay.Function([], output)
mod['func_3493'] = func_3493
mod = relay.transform.InferType()(mod)
output = func_3493()
func_3494 = relay.Function([], output)
mutated_mod['func_3494'] = func_3494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_3531 = relay.TupleGetItem(func_2781_call(), 1)
call_3532 = relay.TupleGetItem(func_2782_call(), 1)
output = call_3531
output2 = call_3532
func_3538 = relay.Function([], output)
mod['func_3538'] = func_3538
mod = relay.transform.InferType()(mod)
output = func_3538()
func_3539 = relay.Function([], output)
mutated_mod['func_3539'] = func_3539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3558 = relay.var("var_3558", dtype = "float64", shape = (8, 14, 12))#candidate|3558|(8, 14, 12)|var|float64
uop_3559 = relay.acos(var_3558.astype('float64')) # shape=(8, 14, 12)
output = relay.Tuple([uop_3559,])
output2 = relay.Tuple([uop_3559,])
func_3573 = relay.Function([var_3558,], output)
mod['func_3573'] = func_3573
mod = relay.transform.InferType()(mod)
mutated_mod['func_3573'] = func_3573
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3574 = relay.var("var_3574", dtype = "float64", shape = (8, 14, 12))#candidate|3574|(8, 14, 12)|var|float64
func_3573_call = mutated_mod.get_global_var('func_3573')
call_3575 = func_3573_call(var_3574)
output = call_3575
func_3576 = relay.Function([var_3574], output)
mutated_mod['func_3576'] = func_3576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3128_call = mod.get_global_var('func_3128')
func_3129_call = mutated_mod.get_global_var('func_3129')
call_3600 = func_3128_call()
call_3601 = func_3128_call()
func_232_call = mod.get_global_var('func_232')
func_236_call = mutated_mod.get_global_var('func_236')
var_3628 = relay.var("var_3628", dtype = "float32", shape = ())#candidate|3628|()|var|float32
const_3629 = relay.const([-6.451794,-8.224828,-4.874258,5.263564,-7.390323,1.807807,1.144417,9.252557,9.609559,-2.134444,7.618169,6.156236,9.989121,-6.206831,4.307935,5.000974,-4.547665,-8.853830,3.491473,-9.961744,3.270841,3.971881,-9.114414,7.624218,3.011836,5.153102,7.097116,-0.881634,2.727764,9.206457,4.679224,-0.677846,2.455237,3.018114,-8.527609,-3.041154,5.866294,0.319579,4.536179,0.623482,-4.070922,4.360090,7.201101,-1.156693,-8.630450,7.055813,-4.579297,6.651629,-5.167747,2.517733,-7.391489,-9.775298,5.684600,5.766912,-0.791470,2.147155,-0.509670,6.036865,-8.167285,-5.186350,1.980849,4.586148,1.404499,0.361760,9.693912,9.036586,9.425698,9.133905,9.209971,6.813465,5.505946,-5.541462,7.233553,-1.772141,4.335205,-8.366861,-2.921005,-1.964132,-3.580618,-0.155474,-8.507804,-2.183753,8.223686,1.870361,-8.717669,8.219471,8.333155,0.244379,3.564487,8.898897,-7.239374,7.853382,5.140301,9.659792,-4.132563,8.568615,9.634897,-0.451303,7.201316,3.463074,-5.002314,8.874850,-5.595271,-0.149442,-3.047787,-3.511071,7.853925,-6.293112,0.506150,-4.458010,9.342167,6.673010,6.141347,2.471081,6.429974,4.252590,9.537779,1.817023,9.609213,5.730273,0.502990,5.724027,-2.838350,0.708890,2.236864,3.669961,8.369830,5.942349,-7.630858,7.064122,6.134788,1.562387,-9.361188,-2.532584,-5.532505,6.867124,9.946699,-5.434552,-2.272144,9.988315,3.561327,-9.510329,0.582800,-4.035924,8.884995,1.218336,-1.476628,0.810084,-7.712038,-8.140564,-8.480008,-0.531899,-9.045304,8.815209,8.325515,-3.207942,9.674033,6.053403,-4.826442,-3.893120,-2.569371,-0.614430,-9.688267,2.973983,9.111604,4.741693,3.696857,7.549020,-8.980441,8.400331,-8.798773,-2.070723,-7.540483,-6.014381,6.649569], dtype = "float32")#candidate|3629|(175,)|const|float32
call_3627 = relay.TupleGetItem(func_232_call(relay.reshape(var_3628.astype('float32'), []), relay.reshape(const_3629.astype('float32'), [5, 7, 5]), ), 1)
call_3630 = relay.TupleGetItem(func_236_call(relay.reshape(var_3628.astype('float32'), []), relay.reshape(const_3629.astype('float32'), [5, 7, 5]), ), 1)
func_2457_call = mod.get_global_var('func_2457')
func_2462_call = mutated_mod.get_global_var('func_2462')
const_3635 = relay.const([[-9,4,3,-3,8,5,8,-10,8,1,-4,-1,-7,9,-8,-2,10,-3,5,9,3,9,-6,10,3,-7,-4,7,1,9,1,-8,-7,-7,7,8,-9,-1,7,9,3,-8,-4,10,9,5,-3,2,-4,-2,4,-2,6,6,-5,5,10,-6,-6,-10,-8,-4,9,-8,-6,3,10,-3,-9,4,-3,-3,-10,-9,-5,-1,5,-3,3,7,-2,9,6,-2,10,-10,-5,-8,-1,-9,-6,-1,-6,-3,-6,8,1,-3,9,3,-3,2,7,1,7,-6,2,3,-4,9,-9,9,6,8,-1,-5,-5,2,-7,1,5,-8,-5,-9,9,10,-6,-7,-2,10,-7,8],[3,5,-3,5,-4,-8,-6,-9,-4,-5,7,-5,-9,4,9,10,-4,-4,-1,-8,4,3,1,-6,-10,-5,5,8,4,-1,-6,7,-8,-8,9,-2,-9,2,-7,-7,1,4,4,9,-5,-3,3,-10,10,-8,3,-10,8,-4,-2,2,3,-9,-9,4,-1,5,-6,5,-5,5,-4,8,-8,-7,-3,4,-6,-4,-1,10,-7,6,-2,-9,3,-2,-8,-10,-5,9,-7,-8,5,-9,2,10,4,5,4,-2,-8,5,9,6,-4,5,-7,-4,5,-1,-5,-8,-7,-7,-7,-10,-5,4,-2,-9,-3,-8,5,5,9,9,-8,-3,10,-8,8,3,-4,-7,-5,-5],[-1,1,8,10,-5,-1,5,-8,3,3,3,-5,3,5,10,-8,-4,-9,-8,-10,-7,4,5,7,9,9,6,-8,8,8,-7,9,5,4,8,-6,4,-4,-3,7,3,-3,2,9,-7,5,3,-5,-3,-2,4,-5,8,-9,2,-3,4,7,7,3,3,8,-6,-4,4,2,-4,10,6,-6,-7,-7,-5,8,-8,-8,1,-5,-2,7,-5,-6,4,4,5,-10,9,5,2,7,-4,-1,4,-3,-6,-2,9,-1,-6,-5,-7,5,-4,1,6,6,-5,-7,6,5,2,3,5,-4,-1,2,-6,3,1,-8,1,9,2,7,7,9,7,-1,-10,-5,-6,10]], dtype = "uint8")#candidate|3635|(3, 132)|const|uint8
var_3636 = relay.var("var_3636", dtype = "uint16", shape = (54,))#candidate|3636|(54,)|var|uint16
call_3634 = relay.TupleGetItem(func_2457_call(relay.reshape(const_3635.astype('uint8'), [396,]), relay.reshape(var_3636.astype('uint16'), [3, 18]), relay.reshape(call_3627.astype('bool'), [819,]), ), 3)
call_3637 = relay.TupleGetItem(func_2462_call(relay.reshape(const_3635.astype('uint8'), [396,]), relay.reshape(var_3636.astype('uint16'), [3, 18]), relay.reshape(call_3627.astype('bool'), [819,]), ), 3)
bop_3641 = relay.add(const_3635.astype('int64'), var_3628.astype('int64')) # shape=(3, 132)
var_3644 = relay.var("var_3644", dtype = "uint16", shape = (54,))#candidate|3644|(54,)|var|uint16
bop_3645 = relay.bitwise_and(var_3636.astype('int16'), relay.reshape(var_3644.astype('int16'), relay.shape_of(var_3636))) # shape=(54,)
output = relay.Tuple([call_3600,call_3627,const_3629,call_3634,bop_3641,bop_3645,])
output2 = relay.Tuple([call_3601,call_3630,const_3629,call_3637,bop_3641,bop_3645,])
func_3659 = relay.Function([var_3628,var_3636,var_3644,], output)
mod['func_3659'] = func_3659
mod = relay.transform.InferType()(mod)
mutated_mod['func_3659'] = func_3659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3659_call = mutated_mod.get_global_var('func_3659')
var_3661 = relay.var("var_3661", dtype = "float32", shape = ())#candidate|3661|()|var|float32
var_3662 = relay.var("var_3662", dtype = "uint16", shape = (54,))#candidate|3662|(54,)|var|uint16
var_3663 = relay.var("var_3663", dtype = "uint16", shape = (54,))#candidate|3663|(54,)|var|uint16
call_3660 = func_3659_call(var_3661,var_3662,var_3663,)
output = call_3660
func_3664 = relay.Function([var_3661,var_3662,var_3663,], output)
mutated_mod['func_3664'] = func_3664
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3690 = relay.var("var_3690", dtype = "uint32", shape = (15, 14, 12))#candidate|3690|(15, 14, 12)|var|uint32
var_3691 = relay.var("var_3691", dtype = "uint32", shape = (15, 14, 12))#candidate|3691|(15, 14, 12)|var|uint32
bop_3692 = relay.right_shift(var_3690.astype('uint32'), relay.reshape(var_3691.astype('uint32'), relay.shape_of(var_3690))) # shape=(15, 14, 12)
var_3706 = relay.var("var_3706", dtype = "uint32", shape = (15, 14, 12))#candidate|3706|(15, 14, 12)|var|uint32
bop_3707 = relay.logical_or(var_3691.astype('bool'), relay.reshape(var_3706.astype('bool'), relay.shape_of(var_3691))) # shape=(15, 14, 12)
func_3659_call = mod.get_global_var('func_3659')
func_3664_call = mutated_mod.get_global_var('func_3664')
var_3721 = relay.var("var_3721", dtype = "float32", shape = ())#candidate|3721|()|var|float32
var_3722 = relay.var("var_3722", dtype = "uint16", shape = (54,))#candidate|3722|(54,)|var|uint16
call_3720 = relay.TupleGetItem(func_3659_call(relay.reshape(var_3721.astype('float32'), []), relay.reshape(var_3722.astype('uint16'), [54,]), relay.reshape(var_3722.astype('uint16'), [54,]), ), 1)
call_3723 = relay.TupleGetItem(func_3664_call(relay.reshape(var_3721.astype('float32'), []), relay.reshape(var_3722.astype('uint16'), [54,]), relay.reshape(var_3722.astype('uint16'), [54,]), ), 1)
output = relay.Tuple([bop_3692,bop_3707,call_3720,var_3721,var_3722,])
output2 = relay.Tuple([bop_3692,bop_3707,call_3723,var_3721,var_3722,])
func_3728 = relay.Function([var_3690,var_3691,var_3706,var_3721,var_3722,], output)
mod['func_3728'] = func_3728
mod = relay.transform.InferType()(mod)
mutated_mod['func_3728'] = func_3728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3728_call = mutated_mod.get_global_var('func_3728')
var_3730 = relay.var("var_3730", dtype = "uint32", shape = (15, 14, 12))#candidate|3730|(15, 14, 12)|var|uint32
var_3731 = relay.var("var_3731", dtype = "uint32", shape = (15, 14, 12))#candidate|3731|(15, 14, 12)|var|uint32
var_3732 = relay.var("var_3732", dtype = "uint32", shape = (15, 14, 12))#candidate|3732|(15, 14, 12)|var|uint32
var_3733 = relay.var("var_3733", dtype = "float32", shape = ())#candidate|3733|()|var|float32
var_3734 = relay.var("var_3734", dtype = "uint16", shape = (54,))#candidate|3734|(54,)|var|uint16
call_3729 = func_3728_call(var_3730,var_3731,var_3732,var_3733,var_3734,)
output = call_3729
func_3735 = relay.Function([var_3730,var_3731,var_3732,var_3733,var_3734,], output)
mutated_mod['func_3735'] = func_3735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3169_call = mod.get_global_var('func_3169')
func_3170_call = mutated_mod.get_global_var('func_3170')
call_3834 = relay.TupleGetItem(func_3169_call(), 4)
call_3835 = relay.TupleGetItem(func_3170_call(), 4)
var_3852 = relay.var("var_3852", dtype = "float64", shape = (1, 3, 14))#candidate|3852|(1, 3, 14)|var|float64
bop_3853 = relay.right_shift(call_3834.astype('uint8'), var_3852.astype('uint8')) # shape=(1, 3, 14)
bop_3856 = relay.right_shift(call_3835.astype('uint8'), var_3852.astype('uint8')) # shape=(1, 3, 14)
func_1200_call = mod.get_global_var('func_1200')
func_1204_call = mutated_mod.get_global_var('func_1204')
const_3864 = relay.const([-7.503657,-8.569571,-5.335232,-0.568542,4.535507,8.925414,-0.888998,-6.470201,-9.523914,-0.415812,-6.388422,2.177867,0.347578,-3.090130,-6.394822,8.497544,0.950453,6.937347,-2.555009,4.277982,6.872042,4.733977,8.937940,-4.377679,8.704566,9.105066,-5.045760,0.019037,1.332870,-5.746404,-4.959013,8.940338,-8.511951,5.457056,-5.285957,-2.732576,9.998532,-0.777541,5.192956,-9.859441,5.540159,-6.583766,1.777705,7.480953,1.643045,-3.638529,7.082786,-0.548806,-9.845431,-6.345284,-3.920798,7.538156,1.100920,-7.310291,-6.054927,1.578092,-4.416193,4.597955,4.268269,9.236271,8.066618,-2.649499,7.425175,-0.119789,6.022761,-5.406685,7.093491,9.491164,2.836367,5.691185,1.874402,8.266397,-5.942384,4.331639,4.696253,3.127588,-5.092239,5.691189,-5.201554,8.066000,5.000857,1.626292,6.737492,1.021290,3.448919,6.444413,0.074103,-2.165791,8.465123,-2.155900,-1.494687,3.653262,1.825922,-0.941967,-8.661121,4.202608,-8.721581,-0.728827,-3.542012,-5.732309,-5.724572,-2.253689,1.043439,-8.588019,-7.055916,8.503833,-7.604731,9.753581,-4.567527,5.633771,3.566031,-1.776952,4.703021,-4.206084,-0.628291,4.452724,-0.649580,-5.229308,2.753047,-3.315996,1.786535,-5.461450,5.998329,-5.628313,-6.305542,-4.256234,-6.477786,1.048282,-4.169024,5.267725,-6.880157,9.023727,-9.629022,-8.343949,-3.816301,0.751696,5.280181,2.133097,3.657799,-9.244183,6.985605,-9.865229,0.783176,-2.366499,3.736986,-0.956304,-2.962013,-0.254982,5.150742,-1.081689,3.497379,-7.223812,-4.960137,0.171790,8.380767,9.012986,3.307190,-5.655562,4.674848,-0.735112,6.606945,-1.356601,-0.565462,-0.042187,-4.612017,-0.197883,0.941610,-1.814966,-2.098442,6.937085,3.559172,2.869594,-5.716647,9.922106,-3.525769,-9.078462,-3.791469,0.985723,4.591389,-1.062722,8.270236,-1.773391,7.299149,-5.720324,-4.259864,0.089889,-5.787494,-2.666865,8.833725,-6.447495,3.670303,7.712512,2.241929,1.726996,-6.512543,-1.634191,-7.199694,-6.127582,3.682605,7.591466,0.057297,8.510363,5.091833,-9.379579,4.260400,-3.992843,-4.889187,-5.702465,0.591456,-5.487945,-3.944003,4.594126,4.804377,-2.299633,-8.809040,1.800827,9.106777,1.570204,-1.926045,0.750325,-1.528578,2.454363,8.204983,-3.843397,5.589734,-4.356407,-5.325377,-3.796556,-2.000182,-8.602277,-5.055408,-8.964148,9.154280,5.163715,3.531160,8.381795,-4.935632,-2.342258,4.542515,-4.438609,-2.725284,-8.363542,-9.972555,-3.072369,2.931891,5.062131,-1.056740,8.966866,5.262394,-5.237537,9.237839,-4.691621,-0.109528,2.828502,-8.965692,-6.472822,5.415110,8.965753,5.796817,-1.032521,-2.462990,-8.607489,4.279082,-2.538933,-4.488296,4.347631,9.531900,-3.570833,5.888523,1.735000,9.057382,-5.084906,-5.200586,1.280356,2.993412,-8.130491,5.220143,2.307545,9.392436,-8.512289,-7.120165,5.428340,7.202392,0.376743,-9.953219,-8.047482,-7.657982,-7.299790,-3.759499,-1.723897,3.968936,-9.167305,5.610389,8.349907,7.065502,8.876069,9.681423,3.610362,-5.522903,8.844584,4.165437,-6.380283,-5.434986,-1.733591,-3.253327,4.306423,-2.365468,6.720167,7.147419,-0.846002,-4.067689,-1.666214,-8.959749,-4.555733,-7.381317,7.943111,-2.349868,8.056095,-6.078908,6.492754,-4.575513,-7.048827,-3.039263,-7.159777,-8.284812,8.489906,-6.083391,0.755135,5.183144,0.492122,2.880145,-0.974972,9.738000,9.982703,0.827959,-0.137665,0.665420,-8.432522,-8.618210,4.007167,9.760118,2.641766,-8.124090,0.333201,8.777453,4.364101,1.628864,-7.346035,7.519904,5.171494,-0.738190,-2.893043,-2.949540,-7.347824,6.954075,-0.699784,-0.844425,1.947957,-5.707894,-8.254610,9.528288,-1.148157,1.319606,3.726170,-0.061643,-8.280171,1.685134,-0.356386,7.378752,-7.693242,-7.282471,-4.343201,3.192310,3.720996,-6.298415,3.808918,9.877060,-3.974466,-2.337973,6.940414,-2.011709,1.768825,-1.064635,-8.535658,-2.265091,0.676015,2.325028,8.360593,8.572063,-9.399713,1.242963,1.649683,3.546000,9.116907,-4.057486,6.208847,-3.124484,-9.093478,-8.813080,6.468351,9.089809,-0.702191,-3.206670,0.746795,-5.613922,4.695007,0.364938,2.161699,-7.321927,-0.809240,5.124375,-0.366630,3.004005,1.645706,8.160793,-8.038364,8.837135,4.169744,0.671947,6.740195,-2.114493,8.888020,5.009160,-6.980527,7.779281,-5.053222,-4.021086,2.053943,0.293855,-9.581854,8.118819,-1.224433,2.450902,-7.648475,-9.282708,-8.898356,-9.187283,3.927374,-9.080410,2.967436,-8.806679,6.671980,-9.269186,-4.342982,1.720917,-0.580409,-9.776617,3.694324,-5.443085,-7.334019,6.847361,2.185666,-1.059304,8.556352,1.261459,-1.495683,2.776450,-3.082583,-7.072987,2.805649,4.598699,-2.227891,-9.329348,8.429122,7.247627,-5.998773,6.924027,-5.155885,-5.494604,-9.988809,3.884398,4.390909,-5.252390,-5.890416,2.961525,-1.889993,-6.656964,-9.073962,-1.941903,6.423734,2.356579,-4.398426,-1.900630,-1.347305,2.997893,-6.821282,7.672977,3.542289,6.508014,0.909069,7.244817,-0.089642,-4.839146,2.593556,-0.541007,7.178048,-8.079203,-8.884076,-4.397489,6.469067,-3.153532,-2.323910,8.416259,7.162261,-9.007248,8.663114,2.378780,6.678604,-0.911265,-7.565827,4.050573,-8.121950,-9.966791,-1.507094,9.008639,-4.956045,6.303980,-3.046278,-3.237591,-1.644753,-5.795256,-4.062221,5.236591,4.625542,-9.818602,-1.730291,0.156444,3.324219,-6.218038,7.261320,8.489368,1.614496,-5.946581,-9.364172,7.777489,4.458594,-8.351170,7.713353,7.055524,-0.847723,1.627757,-5.537154,5.135246,-2.576540,8.836980,-3.759318,2.384705,-8.209396,2.134842,-0.864341,2.832667,-8.914275,5.459625,4.800521,-8.114775,0.444249,-6.678493,3.465635,0.947835,9.388207,9.468202,-1.756638,5.372471,-4.761483,8.522534,-0.997307,8.501104,-2.208804,-0.593111,9.895210,6.710482,-9.797594,-2.169681,-6.526124,2.433114,1.104046,6.526044,5.322008,-2.287894,3.837116,-8.324454,-5.456894,-5.135875,3.255371,-9.780767,4.989412,9.815673,9.271744,1.097244,2.888146,-6.716150,1.548545,-3.479725,-2.876843,7.017170,-9.308687,3.406315,1.605359,-7.069313,3.585655,7.249631,-0.379571,-3.092791,0.320418,1.333426,4.386607,2.101603,7.270789,3.205199,-6.018410,5.831742,6.710884,9.361820,-9.795658,7.863053,-1.629083,3.521540,5.285713,-3.836675,4.847504,5.533461,2.931265,-8.771317,7.691393,0.502100,-5.055048,-5.864439,5.566275,-0.787610,9.846379,1.221007,-3.683854,6.980944,9.622951,-6.119691,1.095878,3.160309,-8.997848,-1.994403,8.969148,9.243594,-3.834478,1.912111,8.505640,-2.264390,9.518831,-0.094802,-1.696818,2.613492,-6.256653,-3.955556,-1.283870,-3.413508,8.485649,-2.975844,-0.497484,-9.813076,8.552911,8.118219,4.708301,-4.955523,0.252571,0.696856,-8.212786,3.303434,-7.742745,-8.151974,5.455901,-4.658445,2.966525,-4.128297,-7.599112,2.568534,-4.526884,3.224608,-7.914471,8.047991,-8.083235,2.177518,0.925491,8.303691,-9.862681,-7.559430,0.602508,0.965968,2.983773,-8.911563,-1.468806,-9.148619,-8.583111,7.833610,5.400844,3.126322,8.373838,-8.441380,5.959940,-4.455917,9.181817,-1.255432,8.614317,-1.928375,0.894848,4.723594,-6.778580,-9.243262,0.749846,0.746799,-1.354670,-6.144432,1.358444,6.207322,8.926042,-8.121194,-6.282418,6.623875,-2.611427,8.182185,-6.125573,-7.353220,-5.601449,-9.059573,-3.825029,-3.652240,-1.791771,-0.745213,8.003288,-0.876455,2.980478,7.419112,6.837485,-6.606518,-8.156979,1.101008,-0.242930,7.848782,6.867876,-9.047676,9.601861,-7.080037,6.320864,9.394781,-0.171433,2.633059,5.919515,-0.816327,1.037233,-7.886890,-0.534222,2.529063,2.329997,6.190198,-2.874340,-7.454243,-0.758869,3.023455,9.959703,-8.496596,-4.113573,-5.899236,-1.227339,0.077222,5.126111,-1.572943,0.040932,-3.983093,-6.288981,9.223507,9.551362,4.646543,4.327412,3.726631,6.290643,-8.182654,-6.296399,4.651936,4.896152,-3.304940,7.356039,-4.501368,-5.116896,9.455438,-3.472700,6.744221,0.644365,1.971318,7.612273,1.190368,-7.929872,8.173151,-0.633163,-8.946797,0.697847,-0.041880,6.850576,2.410261,2.728820,-1.917785,-2.521540,1.085960,-2.852025,-6.961578,-2.396699,2.509556,8.974020,3.246911,3.644786,-3.061326,-7.702183,0.775550,3.079564,-9.196460,-9.202978,3.686520,-0.443354,-2.371687,3.889265,8.920901,-4.663179,1.182526,0.992146,-7.635419,-2.613654,2.183747,4.337380,-5.400849,8.921252,-2.654706,1.114579,-7.191608,-4.335719,4.609707,2.422982,9.201729,7.472463,-3.708467,9.304822,1.089656,6.985328,6.914333,-8.017155,0.696477,-8.777279,3.617748,6.462843,9.173640,-4.981114,-4.746763,4.790751,5.359152,-4.976111,7.512092,-4.301095,6.273253,1.734239,5.258066,-0.820329,-5.410116,-5.435070,-0.117916,5.390680,5.200287,-8.000102,-5.366871,-4.017091,-2.652095,4.039269,-0.868348,4.755550,6.857152,-8.578186,-0.134006,8.407117,5.934665,-5.649860,-7.901730,-4.924477,1.041413,4.914092,-9.081740,5.165632,-0.171224,4.272324,1.194918,-5.340353,1.654126,3.036557,8.400844,-4.171242,-9.146614,-1.688300,4.804885,-7.349080,-4.894449,-4.562014,5.527566,9.131111,-4.437651,5.706183,1.283946,-0.458898,-6.274103,-1.964199,-6.295108,2.166790,3.184836,7.568295,-5.776617,0.693831,3.887108,0.866094,-9.540720,-6.805357,7.820129,-6.587330,5.190402,-1.922253,-7.118333,2.394486,8.877172,9.838712,5.317161,6.659629,-7.194356,-0.693954,-6.151139,8.134928,-9.604799,7.434488,8.140201,6.404819,-7.502001,-4.464978,-0.644991,-8.387709,-6.308825,8.945800,-9.290354,6.342215,0.917116,1.377772,-5.748799,-6.008809,-5.659654,-7.736464,8.909787,4.217712,3.217258,-7.021212,6.242679,-2.174384,-4.094884,8.600077,-6.307177,-8.742520,-3.461172,-7.726995,-1.712438,-6.467935,-7.945513,-1.561965,-8.849427,-4.734097,6.464830,5.063309,5.235549,4.181758,6.293717,-0.041030,1.235088,-0.088554,-9.589513,-4.070133,2.819457,-6.880411,-9.866230,-7.248817,-5.868445,-6.688172,9.423619,-6.214514,1.579139,7.434395,4.081827,5.695997,-5.629826,-3.194263,-5.500173,9.480747,4.694130,5.868912,-9.810840,-9.925091,-9.048848,-2.440548,5.594510,-9.397506,-3.299504,2.390374,-1.450666,1.833460,-8.683758,4.918691,-9.112490,7.968189,-6.966635,6.428105,-6.941083,0.913972,0.133934,-5.520906,8.624300,0.423142,-2.322123,2.519786,6.873489,9.010203,-6.817684,-0.714309,5.039983,5.759894,8.501515,-8.532070,-8.176722,-3.126673,-6.802896,-1.507140,-5.525708,2.728933,7.621634,2.878241,0.400597,-8.428816,5.853584,3.877348,-1.308004,6.500025,2.723064,1.405250,9.143399,5.560651,1.838590,2.853481,-6.103110,-9.015673,8.844594,-3.050782,0.989821,2.359725,-3.028287,0.408683,2.710199,-5.529488,3.635271,-1.898287,5.549998,-4.485541,-7.705153,-5.120596,-2.843405,-9.927625,-8.841614,9.897256,9.915989,7.161527,9.192843,1.661332,1.923419,2.132694,6.196958,3.742340,-8.506819,8.798016,-9.780054,7.959942,3.398601,-7.224278,-6.438055,6.646245,-7.686731,1.656823,9.936357,-6.556310,-0.460797,2.683832,-0.098330,2.027066,-1.097299,1.898446,-7.287016,-5.590007,-1.521189,-3.248971,-9.690728,-6.206623,-4.908358,-9.181978,-8.767342,-0.930544,-4.734259,3.658119,-3.458224,1.374217,4.731849,5.548171,1.011414,2.479207,1.577722,4.959926,2.019896,-0.732233,1.809370,-0.839163,-4.241651,1.133502,-3.998172,8.999567,3.133709,-5.721103,1.853115,-9.863916,1.620395,-0.731934,5.129942,-6.195380,1.419189,-6.313561,8.325435,2.011334,8.366112,-1.241568,4.209750,0.458336,3.194711,5.255886,2.158560,3.775862,-8.255824,2.069700,6.777506,-7.291200,6.810307,-9.207538,7.999734,-0.901648,-4.430099,8.934604,-5.909988,-0.614320,-4.135941,-3.064173,8.138969,-6.422259,8.896277,-7.698227,3.361899,7.957219,4.128684,8.323048,8.122862,-7.096009,-1.287073,2.663615,-6.659317,-3.997713,-4.725023,-7.886509,2.128758,4.054348,0.675032,2.408423,-0.069964,4.593691,-6.821238,6.552682,-2.501488,4.586272,1.060822,2.822298,-4.052877,-7.360421,-3.074340,5.651581,0.283539,-9.433597,-9.998712,5.902523,-6.198122,-9.192603,8.997107,5.227048,3.198194,-1.128034,9.380730,-4.823832,-4.437688,-6.489697,-0.737560,-4.279585,-0.924106,-1.712841,-1.109640,-2.663612,-8.621981,-8.850648,-0.053458,0.614489,-4.535086,-8.023795,9.059899,-8.575606,7.043752,-6.066622,-8.941718,9.336748,8.627998,6.857112,3.139590,-0.020481,-0.710253,6.034459,-4.845119,3.174614,-2.228254,1.003394,-9.935896,2.209805,-5.501952,0.343793,-8.194595,-8.464222,-6.888098,-5.239198,9.314109,0.491656,1.632595,-9.330132,7.084425,-4.449327,4.576495,1.494039,7.990039,2.641593,-6.949486,-3.243620,6.823661,-5.114371,-7.306919,9.344513,-4.326419,-6.192406,5.151688,0.911416,-7.298852,-3.082547,4.891879,3.026448,1.274824,7.186234,-3.098756,-3.555821,-3.792157,4.921149,3.096669,-3.252685,-8.567430,0.384213,1.359121,-3.472027,3.425525,5.237500,0.091157,8.272735,7.690397,-7.732186,5.275827,6.883523,-5.017022,-5.051113,2.201989,7.753849,4.336134,0.828865,6.944351,-4.634457,-8.884530,-1.649043,4.748346,-4.562577,-5.022994,-2.433810,-7.027555,1.760771,-1.595232,-4.126660,-8.669112,2.567689,5.114699,-9.451571,2.021659,1.060446,-1.460026,2.880287,8.685882,-1.941455,-9.064172,9.939067,-8.285713,2.774795,6.817481,-8.294652,5.684991,4.665860,-9.510859,-8.769816,2.182384,8.234992,0.170657,6.537406,6.822588,-4.213022,-0.159267,-0.352043,-9.777974,0.421862,8.452604,0.991807,-4.875378,8.908354,-2.389524,-5.018133,6.386556,2.979136,-2.742602,-8.853313,-2.637377,2.355627,-6.121719,2.974389,-0.381279,-1.621235,-1.609431,-3.679224,1.911246,4.675707,9.765507,7.656365,2.965823,9.213275,2.662398,7.107563,-4.861291,-8.376182,-1.930348,0.837506,-7.965237,6.462384,4.999122,3.986863,8.575422,-6.652189,-1.865892,-6.822406,-9.618103,3.213193,5.657112,6.751207,-6.830386,-0.061972,1.184944,1.787234,-1.592362,-9.649841,-9.879804,-9.999766,-6.058159,7.636969,-7.501539,6.967573,0.014906,-0.447678,3.129119,0.642331,0.954618,6.708744,6.499523,-2.098011,1.554292,-9.462340,0.609399,8.826056,0.369398,-2.305245,-3.946020,2.624487,7.909927,-9.057005,2.838900,-8.325057,-3.194930,-7.685109,-7.132132,4.953051,4.568473,7.465574,-8.431024,5.595679,0.990399,2.119731,9.696846,-4.062286,-5.331388,1.850029,-5.052068,-5.864714,5.174074,-8.631633,0.466778,3.462194,3.082742,2.870894,-9.401041,-0.751393,4.719350,2.729936,-9.713878,3.155595,2.406774,-3.958797,-0.171901,-2.734385,5.847751,4.663643,-6.288724,-4.880235,7.836423,5.923430,-0.522900,-9.029519,7.477573,-7.386976,4.816122,-0.869773,-0.157506,-5.446223,1.006183,5.717290,4.042518,6.071154,8.519870,-8.194796,-7.083020,-2.093260,3.201575,-1.055466,3.220178,-9.958205,-4.490552,8.987059,3.544898,5.859516,-5.271184,-0.036340,5.048492,4.044834,4.062001,7.739782,6.385713,-4.635086,-4.143411,6.214995,5.437238,-1.139346,-0.220335,-3.015656,0.652254,-1.037810,-3.543759,-1.708820,-8.898267,5.147240,1.418508,5.569665,-6.668240,3.994254,-2.056715,-8.152976,-4.784851,6.230898,-3.934972,-9.220760,7.546877,4.426438,4.535698,0.136412,2.498091,5.650559,-4.588144,7.519262,-4.616131,8.412022,2.995877,-3.154034,7.048214,-4.314071,-2.990332,7.948689,9.500696,1.928132,-9.551441,7.194945,5.638702,-7.453288,0.941913,6.941888,-8.552981,1.935311,-6.653962,8.192600,3.095818,-0.265757,4.649086,-1.560634,-3.929116,4.954317,-5.078179,4.752468,-6.609986,5.513754,2.963181,9.507611,-3.779856,-2.865327,6.109475,-0.332598,8.971437,-1.128938,-4.221000,-3.522815,-6.220563,-1.547382,-6.686282,2.092714,1.946529,-6.499688,9.701335,7.925638,-5.650655,-0.526450,3.873359,7.190157,1.920328,1.095503,-2.763630,3.436589,-0.221214,4.519028,4.730865,5.798616,-7.794699,2.432728,8.681799,8.044571,-8.419071,7.050866,-1.859833,4.809202,-2.912380,1.652006,-8.539966,-0.506068,-2.105074,1.773698,-6.545808,4.928439,-9.282787,-1.167971,8.587475,-3.379248,0.824279,7.174921,-0.335498,-9.077420,-9.513622,5.043631,-0.758124,4.065680,7.793568,-1.514323,6.199012,-8.383729,-2.830675,9.120836,-6.055346,-4.806645,-1.866148,4.326958,-3.893322,4.661543,-3.929562,1.781457,-6.566103,8.078397,0.048073,5.755083,5.914471,-1.627664,-2.365915,8.894367,1.929398,9.072361,-8.467842,-7.817358,-8.681961,1.787194,-5.789764,0.529206,5.128449,1.138228,-0.900823,3.497758,-0.594086,9.521534,9.315571,-3.741945,-5.450815,-4.744088,-4.424444,7.740838,4.596094,4.072507,0.786223,-9.658015,-3.854749,2.468687,3.605584,-6.177432,0.425825,-3.161463,1.785239,7.574366,-7.329121,-6.887737,5.855967,7.835561,-1.422806,-8.423424,9.137162,-1.023565,-3.064417,-3.448571,-7.895604,-2.156646,2.455670,-9.419698,2.063416,-2.731136,-9.424328,-5.706207,8.717723,-6.279270,6.333474,4.139312,1.700608,-8.593201,-5.417286,7.361772,0.098348,-4.828430,3.120807,0.132465,-0.412188,-8.804781,-3.793881,-5.465435,6.334383,1.067698,-5.692202,9.641077,-6.489404,1.611711,3.550141,2.459409,-3.379590,4.023232,1.243732,-0.117302,-3.849284,-3.209514,-2.705292,-2.306881,9.642253,-9.449938,8.118881,0.582943,4.665730,-7.259786,-7.490021,5.722446,2.661230,-3.254800,-4.798004,-3.520954,8.695244,6.634945,-7.385681,5.237444,-3.713569,2.096350,-9.142489,4.105630,1.561092,-3.819836,-5.611166,4.803780,-5.196845,-3.681745,-6.217701,8.184090,3.485309,9.817248,2.299472,2.408371,-0.041761,4.508702,6.486107,-5.031243,-9.088078,-5.795865,6.225646,-6.963674,3.102943,-3.157527,8.611670,-5.405468,-2.074645,-1.754196,-5.491409,7.655199,-1.739249,2.544544,-0.936645,8.107906,-9.076254,8.493138,5.601151,5.873338,-6.550444,-0.546313,-6.074260,-4.337565,9.009638,-4.169343,-6.668925,-8.466657,-5.505879,-2.893671,-1.003023,5.129256,-7.882562,-0.228255,-2.891550,-1.498168,7.849549,-9.725192,6.450484,-1.300505,-5.935901,7.130922,3.950836,4.580465,5.354176,-2.993378,9.580405,9.587302,-3.542094,3.242758,8.777560,3.724050,5.575183,-6.653865,-5.096485,5.976114,7.293602,6.257046,-4.836932,-3.402838,-1.985488,6.821736,-5.624624,1.021994,-7.404765,0.371935,3.157238,-0.144066,7.154704,3.700311,-9.165567,-1.057875,0.737287,-2.685873,-1.784773,-4.304863,4.923593,3.292595,-5.072688,-9.538459,9.353874,-3.240444,-8.770608,4.402741,-4.968017,6.914627,4.532992,-1.554972,9.884213,9.801277,-8.227272,-6.161353,8.726738,1.461045,3.442161,7.486864,-3.571792,7.670747,-8.358922,-6.363133,8.939797,8.204677,0.746731,-1.207082,-4.575716,-7.049502,3.403220,-7.389248,-7.801373,-6.927577,4.763357,4.226347,7.319422,-8.902609,7.746682,-1.065280,-4.740341,-4.538634,-3.550734,-6.891202,-9.227638,0.184663,-4.442984,-2.860631,7.809854,-9.151354,-8.972393,-1.152313,-0.160100,-5.423566,2.426873,-1.580494,-9.234828,2.881694,9.457807,-5.809776,6.150649,5.328063,4.594844,-0.557044,-5.781048,-9.584064,-7.201278,4.799335,2.560705,7.004676,-3.751108,0.343777,-9.427900,6.523215,-1.153031,3.661598,7.897999,1.725753,-8.190626,-2.473956,-4.590582,-5.993638,7.044756,4.734404,2.484197,-6.424243,1.908843,-6.485212,-6.595439,2.664363,4.800791,-6.571473,-7.714221,-5.689114,-4.039157,8.934658,5.871049,3.852893,4.154880,9.851969,0.072040,9.402894,4.205088,-3.444485,9.268707,7.428415,-1.452879,-2.463045,6.007112,-8.529427,9.465349,7.824054,4.836268,7.829137,2.087612,7.847694,-3.964908,0.058408,-5.330381,-9.767369,-8.831315,7.327173,7.572721,3.954669,-7.035744,-0.083641,7.175758,-2.346840,5.576624,-6.311698,-8.854950,1.783282,-3.211557,8.190353,8.578720,-6.780915,0.552501,-7.021336,3.079380,0.296192,3.276097,6.510206,6.466541,1.621394,-0.474968,-4.739292,3.189741,3.011954,-4.819374,6.100034,-7.374538,3.846026,1.419444,8.934900,8.655740,-9.829705,-4.109107,-8.707138,7.602109,-8.344308,0.235028,-1.582831,0.685926,-6.317777,-9.362280,0.548421,6.987760,-6.662152,-2.977451,-2.904196,6.309130,7.203575,-3.470455,5.273428,2.184668,8.331506,-4.054510,-3.673666,-0.155491,-8.829975,-3.947306,4.763848,-2.721687,-0.675927,6.711476,2.812062,2.050409,7.186805,-9.405559,2.423182,-1.237042,-3.743254,-4.537697,-5.485351,8.784282,-4.655945,-6.363033,1.062107,7.096542,-4.408010,-1.490194,9.484227,-6.293485,-4.531152,-4.281990,-9.296383,-1.673963,2.372161,1.340750,6.316034,-0.820460,-0.426041,-2.049540,-0.393688,6.304853,-0.244088,-1.592943,2.319631,-9.927034,6.973481,3.854437,-2.748048,-8.397433,7.035071,6.714948,-6.526447,-9.575762,7.639077,-0.790672,-1.159398,-0.052258,-4.779199,1.460099,8.021959,8.908633,-1.870375,-1.843328,-7.337247,-2.735377,3.130444,2.501390,-4.463431,-3.737951,-8.075753,2.162669,5.352087,0.014641,-2.889951,4.711193,2.129337,-2.537361,-8.725644,-3.287498,3.427460,-0.109947,-2.901828,-3.687246,8.813965,-7.935872,7.710782,-4.491154,3.460362,-3.352903,-1.581156,5.174258,-1.925764,0.823514,5.596051,-3.330585,4.150133,2.565032,-2.103588,-9.557419,-0.782328,7.055213,-5.199665,-5.305601,3.269228,7.039066,0.144253,0.468498,-3.956780,-4.548109,-6.998279,-8.230100,9.632206,-2.352701,0.641052,2.440401,7.681389,2.350876,-7.252906,-7.701255,0.863152,-1.602122,-8.157597,-5.513488,-1.370628,-4.449845,6.163064,-9.154145,-4.847582,-4.595981,2.322588,-0.991239,-5.364891,-2.746601,2.130630,7.795977,-0.083054,9.545399,0.069956,6.525363,-5.187467,6.665101,-6.423089,-5.265078,-4.631266,-7.514513,-6.992863,-2.618484,6.717425,-1.472152,5.090049,5.842788,1.027072,9.881501,-0.280680,-1.939107,-8.044003,6.756584,-4.070081,-0.330166,-0.586858,-8.060627,4.418071,-4.706147,-9.342061,5.759846,-5.584238,3.032712,-0.436843,-3.840426,-8.141031,7.619903,-4.097988,9.459615,3.189282,3.678549,2.224210,-0.782119,3.704621,3.426500,2.978813,0.575429,5.582312,0.444915,2.368938,-6.210378,5.750044,1.274038,-6.296608,-7.610811,-7.667605,-2.535935,2.831157,-0.938854,4.833131,-3.400490,-1.692123,-3.168633,6.781752,3.417033,6.191108,-3.703161,-7.482958,3.681552,-7.421761,-8.157130,5.653090,-3.495301,9.103475,2.216950,-8.886044,-7.502608,-9.362094,-3.792584,-8.588695,-7.893118,-5.983931,-3.112237,-0.417211,7.991199,6.316058,6.936722,-8.803426,-2.246730,-6.106219,-9.225631,2.335849,-4.379141,0.313732,8.162169,-6.580937,-4.525554,-8.282511,7.640617,-6.162407,-2.200399,-7.264314,-1.916057,2.856116,4.855723,6.428718,3.840390,-4.861732,-8.108687,-2.783032,2.718678,0.463199,0.309117,0.616273,9.469387,-8.729339,2.892454,2.567415,5.601094,-5.741307,3.936949,6.098155,8.169517,-8.031545,8.204638,8.164673,1.782542,-8.127258,7.680093,-2.312794,9.958997,-8.177131,3.470469,8.035096,-1.811767,1.796540,0.163670,-4.637935,-8.704743,-2.066714,-5.938661,1.482222,-8.382474,-7.469879,8.260367,-2.752529,7.130667,8.427304,8.268190,-6.852437,0.957029,2.753507,-1.318329,3.707865,-2.515927,-2.309694,8.268756,-0.851776,-1.605194,1.955219,5.246318,-3.787093,-7.063374,-6.885928,-9.861133,-0.292808,-3.676256,-6.322324,8.109941,-0.072916,2.740521,-3.086263,-3.386351,4.790457,-3.043045,-5.321526,-3.462025,-4.633583,-3.044061,-5.300098,6.878179,-7.732948,-8.560413,-3.786268,-3.598030,0.848673,-3.642312,6.063940,1.579812,6.517486,3.819985,6.292848,-6.868751,4.112788,-7.809794,-9.891323,-2.828954,-3.847882,5.221665,-5.481582,0.938093,-2.798644,-7.352635,-8.705244,-4.387871,2.952658,9.558586,2.280295,-8.197576,-5.614236,6.289395,7.653650,-1.595293,-9.704275,-3.114770,8.217326,3.249917,8.122714,0.777827,9.662251,9.082846,-8.685077,0.282682,0.927882,-4.085078,1.085222,-4.867063,6.749532,-0.912007,-8.840210,-1.820061,-6.819007,9.951856,0.626488,4.364764,-9.082891,2.637130,8.732601,6.395276,0.769604,-7.789923,4.304949,4.214717,6.170295,-5.353484,-6.371084,-6.010055,-5.097849,4.077317,-1.476238,-6.069594,1.696400,6.061277,7.264526,2.273372,-3.063035,5.707970,-5.805697,-9.352147,-9.588193,-3.768646,-7.961954,5.507422,-7.669141,-9.804497,0.377021,-5.824876,9.676294,5.034706,-8.872084,0.485844,-1.280457,-6.216876,9.721719,7.477131,5.052311,-0.356851,-8.164426,3.664534,-3.248905,5.465344,-4.313620,2.642404,-8.205309,-1.968917,8.769787,8.821033,-8.056445,4.645456,8.963976,7.178638,-5.546354,-0.816491,8.841130,3.817767,3.873426,5.067595,-6.222362,5.983061,7.961649,7.993755,1.097189,0.123744,-5.153796,2.738259,1.410731,5.405532,7.917057,-4.802448,0.315832,-7.233265,-5.074354,-2.354085,-6.289170,4.555125,-4.560947,3.505681,-7.530710,5.177694,1.267444,-4.739762,-7.268919,-6.381714,1.872124,-9.085144,-3.543254,2.759725,0.071065,-6.020009,-6.242725,7.776117,-8.065504,-2.461539,0.096862,-8.123263,6.571234,5.388925,-6.856436,4.271156,-2.608708,-8.367651,-3.017592,-2.336450,8.414306,-1.696650,-8.431097,-7.335026,-5.358309,3.052218,8.163407,-3.749088,-4.716560,-6.314711,1.587552,-4.340664,8.541575,-4.139485,5.079550,5.636745,9.911050,-7.452518,-3.753217,1.032759,7.594171,-3.677717,-9.106286,1.430647,3.280151,8.094085,3.475379,-4.713227,-2.393078,2.118442,1.522968,-9.648605,-7.860463,1.087837,-4.754633,4.580664,1.683339,-1.657606,-8.665347,1.987470,4.497688,-1.967832,-6.990013,7.440968,1.135413,-8.325576,-6.171026,-4.168209,9.443020,9.976277,-1.210872,-9.289717,-6.776200,0.303069,-0.311142,-4.329596,0.601346,8.203159,-0.711969,-2.947655,6.751771,-5.823058,3.654927,-5.919796,-5.196515,-4.771767,-5.704021], dtype = "float64")#candidate|3864|(2520,)|const|float64
call_3863 = relay.TupleGetItem(func_1200_call(relay.reshape(const_3864.astype('float64'), [15, 12, 14]), relay.reshape(const_3864.astype('float64'), [15, 12, 14]), ), 0)
call_3865 = relay.TupleGetItem(func_1204_call(relay.reshape(const_3864.astype('float64'), [15, 12, 14]), relay.reshape(const_3864.astype('float64'), [15, 12, 14]), ), 0)
bop_3875 = relay.bitwise_xor(const_3864.astype('uint32'), relay.reshape(call_3863.astype('uint32'), relay.shape_of(const_3864))) # shape=(2520,)
bop_3878 = relay.bitwise_xor(const_3864.astype('uint32'), relay.reshape(call_3865.astype('uint32'), relay.shape_of(const_3864))) # shape=(2520,)
output = relay.Tuple([bop_3853,bop_3875,])
output2 = relay.Tuple([bop_3856,bop_3878,])
func_3895 = relay.Function([var_3852,], output)
mod['func_3895'] = func_3895
mod = relay.transform.InferType()(mod)
mutated_mod['func_3895'] = func_3895
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3896 = relay.var("var_3896", dtype = "float64", shape = (1, 3, 14))#candidate|3896|(1, 3, 14)|var|float64
func_3895_call = mutated_mod.get_global_var('func_3895')
call_3897 = func_3895_call(var_3896)
output = call_3897
func_3898 = relay.Function([var_3896], output)
mutated_mod['func_3898'] = func_3898
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3948 = relay.var("var_3948", dtype = "float32", shape = (7, 3, 10))#candidate|3948|(7, 3, 10)|var|float32
uop_3949 = relay.atan(var_3948.astype('float32')) # shape=(7, 3, 10)
func_930_call = mod.get_global_var('func_930')
func_934_call = mutated_mod.get_global_var('func_934')
const_3956 = relay.const(3.431742, dtype = "float64")#candidate|3956|()|const|float64
var_3957 = relay.var("var_3957", dtype = "uint16", shape = (2,))#candidate|3957|(2,)|var|uint16
call_3955 = relay.TupleGetItem(func_930_call(relay.reshape(const_3956.astype('float64'), []), relay.reshape(var_3957.astype('uint16'), [2, 1]), ), 0)
call_3958 = relay.TupleGetItem(func_934_call(relay.reshape(const_3956.astype('float64'), []), relay.reshape(var_3957.astype('uint16'), [2, 1]), ), 0)
func_2007_call = mod.get_global_var('func_2007')
func_2011_call = mutated_mod.get_global_var('func_2011')
const_3970 = relay.const([[-3,9,-9,6,-1,10,-4,9,-5,-7,-6,7,3,7,-5,5,-5,3,-9,1,7,-7,4,-6,-10,5,8,-2,-7,4,3,9,4,-3,-8,2,-6,6,-8,10,-7,-6,6,-6,6,-4,-9,-6,-4,7,-3,-9,1,-2,8,-7,-8,8,10,6,5,-4,4,9,-8,2],[-5,-4,-6,5,10,-7,-4,2,-2,-9,-2,-1,-2,-6,9,6,1,-10,8,-3,7,5,-6,5,-7,4,9,6,8,-6,2,-10,-1,1,8,-8,-3,-8,1,-8,-10,-8,10,2,5,-6,9,-1,-10,2,8,5,-4,-2,-8,5,-3,-9,-8,4,3,2,7,4,10,5],[7,-9,7,-10,-4,-5,10,1,-8,-3,4,-5,-1,-8,7,8,5,9,-1,-9,5,-3,9,-3,8,10,-1,2,-3,2,-4,-6,-8,-3,3,3,5,3,9,-2,9,-10,6,2,-2,9,-3,-7,1,9,1,4,-9,1,-2,-4,7,-1,7,2,8,-7,10,5,3,5],[-7,3,5,-3,-9,8,-2,-10,-4,8,8,6,-9,-7,-4,-10,3,-6,-7,3,-7,-5,2,10,2,10,3,-7,-5,-5,-9,10,8,10,7,5,-6,5,-8,4,2,7,7,8,-8,-3,-9,1,-2,-5,6,-5,10,10,6,5,7,-3,-8,8,-5,-5,3,2,-8,-6],[-8,-7,-2,6,1,6,-5,-2,-2,-9,1,-1,-1,-2,1,3,7,-8,7,7,-7,-3,3,-5,6,-4,-1,1,-2,-1,9,4,4,-4,-6,-8,-5,-5,-6,7,-6,7,8,9,1,2,-8,5,-8,4,2,-9,2,-7,-4,-10,-3,-10,-7,10,-1,-5,9,-10,8,1],[5,-7,3,5,8,2,6,-4,-10,-10,-7,9,-4,-2,-4,-2,-4,6,-5,-7,-10,-4,-10,7,3,3,2,-5,-3,-1,-2,6,4,-3,4,-1,10,1,4,-2,-7,6,-6,-8,-9,-6,3,-7,3,-5,-2,3,4,4,2,-4,10,8,4,-5,-4,4,-10,-4,2,1]], dtype = "uint8")#candidate|3970|(6, 66)|const|uint8
var_3971 = relay.var("var_3971", dtype = "float32", shape = (175,))#candidate|3971|(175,)|var|float32
call_3969 = relay.TupleGetItem(func_2007_call(relay.reshape(const_3970.astype('uint8'), [11, 4, 9]), relay.reshape(const_3970.astype('uint8'), [11, 4, 9]), relay.reshape(var_3971.astype('float32'), [175,]), ), 6)
call_3972 = relay.TupleGetItem(func_2011_call(relay.reshape(const_3970.astype('uint8'), [11, 4, 9]), relay.reshape(const_3970.astype('uint8'), [11, 4, 9]), relay.reshape(var_3971.astype('float32'), [175,]), ), 6)
var_3984 = relay.var("var_3984", dtype = "float32", shape = (7, 3, 10))#candidate|3984|(7, 3, 10)|var|float32
bop_3985 = relay.floor_divide(uop_3949.astype('float32'), relay.reshape(var_3984.astype('float32'), relay.shape_of(uop_3949))) # shape=(7, 3, 10)
var_3995 = relay.var("var_3995", dtype = "float32", shape = (7, 3, 10))#candidate|3995|(7, 3, 10)|var|float32
bop_3996 = relay.not_equal(uop_3949.astype('bool'), relay.reshape(var_3995.astype('bool'), relay.shape_of(uop_3949))) # shape=(7, 3, 10)
func_3311_call = mod.get_global_var('func_3311')
func_3313_call = mutated_mod.get_global_var('func_3313')
var_4001 = relay.var("var_4001", dtype = "float64", shape = (336,))#candidate|4001|(336,)|var|float64
call_4000 = func_3311_call(relay.reshape(var_4001.astype('float64'), [7, 4, 12]))
call_4002 = func_3311_call(relay.reshape(var_4001.astype('float64'), [7, 4, 12]))
output = relay.Tuple([call_3955,const_3956,var_3957,call_3969,const_3970,var_3971,bop_3985,bop_3996,call_4000,var_4001,])
output2 = relay.Tuple([call_3958,const_3956,var_3957,call_3972,const_3970,var_3971,bop_3985,bop_3996,call_4002,var_4001,])
func_4009 = relay.Function([var_3948,var_3957,var_3971,var_3984,var_3995,var_4001,], output)
mod['func_4009'] = func_4009
mod = relay.transform.InferType()(mod)
mutated_mod['func_4009'] = func_4009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4009_call = mutated_mod.get_global_var('func_4009')
var_4011 = relay.var("var_4011", dtype = "float32", shape = (7, 3, 10))#candidate|4011|(7, 3, 10)|var|float32
var_4012 = relay.var("var_4012", dtype = "uint16", shape = (2,))#candidate|4012|(2,)|var|uint16
var_4013 = relay.var("var_4013", dtype = "float32", shape = (175,))#candidate|4013|(175,)|var|float32
var_4014 = relay.var("var_4014", dtype = "float32", shape = (7, 3, 10))#candidate|4014|(7, 3, 10)|var|float32
var_4015 = relay.var("var_4015", dtype = "float32", shape = (7, 3, 10))#candidate|4015|(7, 3, 10)|var|float32
var_4016 = relay.var("var_4016", dtype = "float64", shape = (336,))#candidate|4016|(336,)|var|float64
call_4010 = func_4009_call(var_4011,var_4012,var_4013,var_4014,var_4015,var_4016,)
output = call_4010
func_4017 = relay.Function([var_4011,var_4012,var_4013,var_4014,var_4015,var_4016,], output)
mutated_mod['func_4017'] = func_4017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_4033 = relay.TupleGetItem(func_2717_call(), 1)
call_4034 = relay.TupleGetItem(func_2719_call(), 1)
output = call_4033
output2 = call_4034
func_4057 = relay.Function([], output)
mod['func_4057'] = func_4057
mod = relay.transform.InferType()(mod)
mutated_mod['func_4057'] = func_4057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4057_call = mutated_mod.get_global_var('func_4057')
call_4058 = func_4057_call()
output = call_4058
func_4059 = relay.Function([], output)
mutated_mod['func_4059'] = func_4059
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4153 = relay.var("var_4153", dtype = "float32", shape = (5, 11, 15))#candidate|4153|(5, 11, 15)|var|float32
uop_4154 = relay.sqrt(var_4153.astype('float32')) # shape=(5, 11, 15)
uop_4163 = relay.rsqrt(var_4153.astype('float64')) # shape=(5, 11, 15)
output = relay.Tuple([uop_4154,uop_4163,])
output2 = relay.Tuple([uop_4154,uop_4163,])
func_4168 = relay.Function([var_4153,], output)
mod['func_4168'] = func_4168
mod = relay.transform.InferType()(mod)
mutated_mod['func_4168'] = func_4168
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4169 = relay.var("var_4169", dtype = "float32", shape = (5, 11, 15))#candidate|4169|(5, 11, 15)|var|float32
func_4168_call = mutated_mod.get_global_var('func_4168')
call_4170 = func_4168_call(var_4169)
output = call_4170
func_4171 = relay.Function([var_4169], output)
mutated_mod['func_4171'] = func_4171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_4198 = func_2649_call()
call_4199 = func_2649_call()
func_3895_call = mod.get_global_var('func_3895')
func_3898_call = mutated_mod.get_global_var('func_3898')
const_4203 = relay.const([9.042461,-8.289042,1.183489,-6.606294,-7.770118,-6.137642,5.352904,2.550173,-9.219335,-2.952567,7.376652,-8.321929,-2.372450,1.115531,-3.773293,-2.491022,-7.002552,9.598758,-6.265244,-2.980351,-6.085119,-9.787855,6.504914,-5.918838,9.721579,-3.743894,-0.166550,0.917769,-0.735892,1.331958,-2.614686,-9.459617,-5.570459,-6.534836,0.539696,6.728945,8.462396,1.802482,-3.663023,-9.784716,2.074235,-4.895292], dtype = "float64")#candidate|4203|(42,)|const|float64
call_4202 = relay.TupleGetItem(func_3895_call(relay.reshape(const_4203.astype('float64'), [1, 3, 14])), 0)
call_4204 = relay.TupleGetItem(func_3898_call(relay.reshape(const_4203.astype('float64'), [1, 3, 14])), 0)
func_3332_call = mod.get_global_var('func_3332')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_4205 = relay.TupleGetItem(func_3332_call(), 0)
call_4206 = relay.TupleGetItem(func_3333_call(), 0)
output = relay.Tuple([call_4198,call_4202,const_4203,call_4205,])
output2 = relay.Tuple([call_4199,call_4204,const_4203,call_4206,])
func_4207 = relay.Function([], output)
mod['func_4207'] = func_4207
mod = relay.transform.InferType()(mod)
mutated_mod['func_4207'] = func_4207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4207_call = mutated_mod.get_global_var('func_4207')
call_4208 = func_4207_call()
output = call_4208
func_4209 = relay.Function([], output)
mutated_mod['func_4209'] = func_4209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_4246 = relay.TupleGetItem(func_2717_call(), 1)
call_4247 = relay.TupleGetItem(func_2719_call(), 1)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_4256 = func_2238_call()
call_4257 = func_2238_call()
func_2216_call = mod.get_global_var('func_2216')
func_2219_call = mutated_mod.get_global_var('func_2219')
var_4281 = relay.var("var_4281", dtype = "float32", shape = (175,))#candidate|4281|(175,)|var|float32
call_4280 = relay.TupleGetItem(func_2216_call(relay.reshape(var_4281.astype('float32'), [175,])), 4)
call_4282 = relay.TupleGetItem(func_2219_call(relay.reshape(var_4281.astype('float32'), [175,])), 4)
output = relay.Tuple([call_4246,call_4256,call_4280,var_4281,])
output2 = relay.Tuple([call_4247,call_4257,call_4282,var_4281,])
func_4302 = relay.Function([var_4281,], output)
mod['func_4302'] = func_4302
mod = relay.transform.InferType()(mod)
var_4303 = relay.var("var_4303", dtype = "float32", shape = (175,))#candidate|4303|(175,)|var|float32
output = func_4302(var_4303)
func_4304 = relay.Function([var_4303], output)
mutated_mod['func_4304'] = func_4304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2600_call = mod.get_global_var('func_2600')
func_2601_call = mutated_mod.get_global_var('func_2601')
call_4308 = relay.TupleGetItem(func_2600_call(), 2)
call_4309 = relay.TupleGetItem(func_2601_call(), 2)
func_3169_call = mod.get_global_var('func_3169')
func_3170_call = mutated_mod.get_global_var('func_3170')
call_4310 = relay.TupleGetItem(func_3169_call(), 0)
call_4311 = relay.TupleGetItem(func_3170_call(), 0)
func_2403_call = mod.get_global_var('func_2403')
func_2409_call = mutated_mod.get_global_var('func_2409')
var_4313 = relay.var("var_4313", dtype = "bool", shape = (819,))#candidate|4313|(819,)|var|bool
const_4314 = relay.const([-1.520820,-0.251434,3.603434,-0.472551,-4.739660,5.554741,-2.990737,-5.979887,-8.415820,-8.956277,4.574718,1.652661,0.535830,4.822936,9.836957,-2.302687,0.145023,4.422371,5.707842,5.735477,8.866559,-5.707595,-2.930857,9.755474,1.353428,2.270654,-4.797552,-3.893486,9.750874,-4.708582,3.672023,3.980588,-7.350358,0.510606,-5.357038,0.177716,-7.848128,-5.827008,-4.588555,2.092016,1.156286,1.176239,-1.410748,1.889280,4.714696,-5.136176,-1.476711,1.331074,3.524622,-7.259266,4.041023,5.478860,6.967537,-8.700989,2.429814,3.036204,-5.883473,2.924198,-6.943168,3.010104,-1.388739,-4.912141,2.500328,0.882862,-5.002142,-6.676286,0.149828,4.792449,6.555099,0.074141,-2.974615,5.599655,5.536115,9.126740,2.969492,6.284105,-1.691384,-4.386855,5.251920,-1.147495,9.186350,3.045476,-1.657051,7.648243,-0.132376,2.512338,7.286491,-4.021261,3.434354,-9.170062,-2.284043,-6.315731,0.176309,-9.631478,4.072912,0.028943,5.802406,5.036619,5.664376,-0.132913,5.585966,-5.846387,-5.860961,1.357419,-1.044932,9.408370,7.454506,-7.678936,-6.202331,4.727967,0.172862,7.414805,5.285131,9.332439,4.992956,0.633318,5.151642,-9.563249,-1.198853,2.289509,7.351072,0.706931,-3.137429,-5.094575,-2.288205,-7.826098,-6.789314,-1.577217,2.488792,-4.283685,3.172260,6.649205,-8.589677,5.386374,-9.836108,9.567366,2.365031,-7.416390,-7.970087,-6.168614,3.558039,0.306754,-3.252006,6.344493,4.543005,8.951651,2.769803,6.458283,-0.814580,-1.030562,8.966905,-3.117057,-1.295877,-1.204769,1.270447,2.645066,-2.937510,-3.725255,5.786929,-2.920299,-0.875476,9.740802,-1.008859,8.253665,7.011053,0.430240,8.334182,2.947675,8.474112,1.653837,2.116395,1.761955,3.209793,-5.505775,6.262646,7.770046,-6.085917,-9.336535,3.774765,7.402708,9.626960,4.204498,6.211685,3.176026,-3.095323,6.102641,0.012315,7.717693,4.866492,0.871990,-0.614622,-7.057504,-3.184848,-2.704226,-3.382156,-2.979462,-4.571035,-5.376474,2.708779,-7.909874,-1.226391,2.582529,-8.182232,-0.584659,-2.701519,9.360994,-0.019959,-6.336856,-5.904041,-3.830728,-1.606392,-4.100777,-7.648063,-6.776999,-0.458181,-8.425700,3.872833,6.495414,-5.389060,1.590143,9.937237,-8.004837,-8.277518,-6.341521,6.905778,7.849382,-1.423291,-7.913638,-2.817607,-7.470492,-3.742646,-8.980296,-1.756462,4.084674,7.501999,1.352091,2.489347,3.811351,-8.541317,-7.793642,-8.164359,-4.962694,-8.158205,-7.163830,4.892667,8.620314,0.108962,5.610265,1.379205,-3.163440,1.330840,-0.306066,1.511320,-5.685133,2.650434,2.765984,-2.293296,-7.623945,9.305930,-5.387781,0.432337,-1.682401,1.046412,-8.611458,-5.270095,5.682332,1.542601,2.367838,0.811613,-0.390360,-4.934557,6.293601,2.806165,7.265774,-6.201944,-3.427070,-1.393423,-9.035333,-8.255021,-8.113503,4.183901,5.692931,9.038778,-5.535584,-1.644871,-9.754419,-8.314094,-5.351746,3.054879,-8.675051,1.011106,-9.791904,8.691690,4.540270,5.876895,5.251040,2.830659,4.330615,1.134712,-5.114089,7.220211,-6.527106,-3.109316,8.924342,7.155907,7.028327,-9.191308,-1.391140,-8.598092,-9.085670,4.733998,-8.333152,-2.317157,-1.577506,9.619603,1.844792,2.598953,1.622116,-3.913031,8.514946,-3.658553,-9.288628,-2.388337,2.015923,-3.730413,1.241199,0.704597,5.242124,7.434367,0.076169,-2.643226,9.153034,-5.788488,1.798364,-1.337870,-7.523081,1.789158,6.440027,1.136370,-4.024039,-2.862745,-3.738084,5.009931,3.711895,7.792341,-3.890045,-7.830005,0.911589,-8.575577,5.851185,3.808642,0.664074,4.800051,1.944470,0.734858,-4.956308,7.084720,2.258901,-5.243712,6.793847,6.212749,4.198365,-1.410914,4.790899,1.641528,4.804588,-1.198401,0.463469,8.175013,9.808693,-0.326866,5.833115,-5.490919,9.865992,3.536324,-5.876673,-9.348202,-7.192371,-3.959884,5.348599,6.913984,-2.686564,0.336623,3.215728,-9.771570,-1.867682,-4.286339,-1.412495,-5.380036,-2.629675,7.873843,3.740808,-6.591164,-7.253390,5.907411,8.298837,-3.593823,-8.841064,5.682779,-3.491007,-0.596628,7.504894,-2.632402,6.312718,7.741690,6.920889,-3.107898,-0.718339,-7.068425,3.651385,-8.974495,-1.727038,8.544662,-1.465512,-2.499099,-3.858164,3.154374,-6.052877,-4.227982,6.712065,7.263569,-3.068912,5.475742,-9.340226,5.025681,0.791746,-2.976226,-2.448204,-6.940678,3.688358,4.887277,-4.704807,2.059548,3.744997,-7.927652,4.469673,7.054568,-0.419828,-3.423513,-7.853892,-6.396976,9.612955,-0.923310,-4.322324,-6.745215,1.133394,-2.699220,9.274983,-3.876658,7.087232,1.287568,-1.881134,-7.415602,8.362445,-6.004614,-5.316132,2.144118,8.544122,4.127582,-5.502591,0.948690,4.297272,7.906633,5.882262,8.709862,7.428250,5.205930,8.036235,-3.096349,-7.532813,4.404231,8.957597,-2.921772,-3.377268,0.646247,-0.699416,-2.180323,-0.381900,-0.738499,-2.358830,-7.390246,-5.745538,5.758223,1.229106,-2.863559,-4.942818,-0.048506,-0.291824,5.260022,-0.550957,9.469820,7.145618,-3.250643,-0.843487,-6.580072,2.224470,-4.843148,-8.068036,1.854442,8.632181,-4.384174,0.906903,1.624839,6.944792,-5.871288,1.476604,-3.735565,-7.796061,-9.080907,6.751733,4.880086,7.909036,-7.535320,6.971815,7.320079,1.732545,6.852850,-0.264933,-1.757878,1.404530,6.299153,0.838163,6.932848,0.857763,-3.648428,-7.528175,5.441742,5.367829,-1.376284,2.219075,1.535505,4.868970,-5.694540,8.315896,6.076947,5.184690,-4.288471,4.884517,-3.588051,7.933216,6.023202,-8.474647,-8.836113,7.246998,3.618887,-1.568462,7.946021,2.798545,-8.572004,6.123918,5.517916,-5.894046,3.148627,5.699081,-5.709908,-0.859250,9.485521,-4.438782,-9.721101,-7.564619,1.963879,-9.449363,-3.318318,-1.918027,-6.052693,-0.835294,-0.601269,9.918525,-2.459359,-5.877679,-0.330678,0.959765,0.283139,1.991032,0.715217,1.318548,-9.470926,2.452412,8.683224,0.493732,8.313405,4.273714,9.753371,1.519551,-3.367510,-0.388497,-4.932322,-2.363449,-3.972325,8.808990,2.230345,-0.010343,-0.390530,-3.171943,1.250809,-5.796709,3.027368,-3.331512,-2.161304,9.386923,7.352226,2.317117,9.250375,-7.671036,5.783372,7.832525,-0.292297,7.734551,4.405938,2.494444,5.851402,-1.309802,4.183574,7.081520,-9.566161,-1.004637,1.666608,-1.131911,6.989585,-6.411802,-8.328010,0.436376,6.751824,-3.101804,-9.537274,8.675134,3.820834,4.864330,-9.787575,-5.510974,3.027932,4.925247,9.337488,2.671954,-2.906195,8.733394,8.201112,8.631041,2.289058,8.858224,1.841073,-1.101453,-8.382290,-4.159146,-1.879279,-8.592407,3.908328,-3.553663,0.021622,-9.026172,9.488729,-6.368094,-5.598476,1.540099,6.437016,-9.659864,9.080607,1.334074,-5.444265,3.615532,1.484436,-9.185378,8.659542,6.904781,-3.450588,-2.521008,3.104966,-5.131260,-7.354670,-1.685310,-2.084018,8.211639,3.079507,-5.355435,-9.314240,-0.485332,4.381013,-1.077406,-3.548674,2.570449,7.921735,-6.745649,-8.396993,1.835170,3.256421,9.854813,-5.080980,9.598233,1.236156,1.257013,5.192194,6.301194,-0.841570,7.342544,6.741577,5.294014,-3.987377,-4.943313,-0.809372,-7.204464,1.002039,0.568122,-7.831939,0.176240,-1.132892,4.241711,-9.283585,-1.430657,-0.637554,0.014166,-4.295864,4.540034,6.473426,-1.964475,5.325793,2.740011,-8.829672,-8.442891,3.223029,-6.943466,-6.987098,-6.673590,2.981959,4.435882,-9.217948,8.631405,5.627423,-9.404399,-7.003293,-4.421873,2.734537,-9.322498,-8.641207,-1.336334,-8.669437,-7.877827,-7.226234,-5.247363,1.228661,1.661428,-4.739301,4.723991,0.459751,-0.735803,-8.297925,9.867005,-3.855695,5.026959,-5.271698,7.426053,-9.060114,8.834097,-4.426922,-1.119674,3.305913,7.233712,5.106805,7.733816,-7.420093,-3.929351,-3.540662,-7.500077,-6.330354,-8.670595,9.561306,0.959550,7.282787,-9.378323,-3.133313,9.051064,9.666025,-2.239446,5.010759,8.201062,8.999022,-8.090341,-1.118066,0.268662,-6.210840,5.787997,8.902577,-0.750202,-6.088836,-3.596297,7.334484,-8.156416,-7.831414,7.395988,8.685939,-4.361846,5.877910,-2.952230,3.173175,-3.318615,9.570314,-4.328592,-9.952694,0.532030,9.598734,-3.496027,-1.457680,5.944354,8.980889,-8.759460,-8.053063,1.672828,-3.400040,9.972823,0.156336,9.586153,3.473920,7.058156,-7.547501,-3.990515,-8.868348,5.300988,-2.986645,-4.395927,3.598492,-3.186725,3.905464,4.889842,6.143579,7.092137,-8.258075,-8.916277,-6.645940,-0.313252,-9.412892,0.840091,1.176249,2.361917,9.768444,7.808722,8.366265,-8.318583,8.161439,-9.709628,-4.242643,-7.618973,-7.358112,5.686398,-2.028114,-2.190452,-4.692043,-1.897913,-5.238622,7.528917,1.521449,-8.374182,-6.649347,6.665544,8.796564,9.453397,5.151553,-5.992828,-3.859445,8.330022,8.849061,5.743034,2.438631,8.516214,-1.222642,3.779902,8.304053,-2.739390,0.429273,-1.424289,1.125995,-6.882034,8.698750,-0.283855,-6.935353,-7.869560,0.939569,-9.883057,4.414811,-1.701073,-4.607940,1.788787,-3.144218,-0.536233,4.671707,-4.645226,-0.514693,-3.184650,1.715269,7.832201,-7.872496,-2.948802,0.645183,-0.171258,-4.426597,-9.573595,-2.031661,9.466410,2.234276,-6.220451,-4.318100,1.486751,-8.920569,-8.574036,9.481977,3.378443,5.615927,8.210328,-7.990567,-2.832249,2.544053,-9.114452,-2.082646,-3.859497,9.239367,3.246851,9.285721,-8.580554,-8.934815,1.420990,-6.515554,5.323105,-8.146497,-4.571633,-4.929802,-6.484937,-5.726029,0.582058,-4.685433,-8.914148,3.008776,0.183369,2.494839,-8.398131,-2.631839,9.592402,-7.144470,-3.465568,0.298597,-1.454295,2.145697,2.775770,3.652511,3.465827,-7.276758,1.277764,9.351681,-8.091334,-3.065636,-7.943232,7.659429,3.712047,-4.414006,-7.462291,-6.549237,9.025316,6.690510,5.452790,8.115219,-3.628988,0.920412,8.765597,-0.795653,1.306509,-2.118066,0.455562,7.941579,-5.321870,3.428095,7.332787,1.070229,0.367367,-8.760794,9.676231,2.470016,0.488640,1.930399,2.184051,8.820107,-5.494209,-2.242753,6.916923,-7.477551,4.481405,-1.687932,6.530366,9.176094,1.365387,-1.545051,-4.874426,-5.403202,-2.263891,-3.665845,-7.573628,-7.064557,-6.767396,-2.536076,-9.835243,0.433971,-9.768084,-8.434283,2.926794,6.003446,1.153487,9.260359,0.373022,-4.729593,3.495379,-9.791487,-1.356668,-5.812024,6.451016,-1.981127,3.034480,-7.003497,4.727242,1.263290,-9.583179,5.669243,-6.522918,1.853144,3.751735,7.592958,4.431982,-0.070447,-9.395724,-3.655873,7.971252,9.997585,-8.468292,2.073194,8.260764,-0.962820,0.822285,9.194948,-2.765251,8.367486,-3.670772,-4.071535,-5.477726,4.316684,3.050167,5.679406,-0.221773,8.480053,-2.927633,7.983794,7.130645,3.052296,6.888386,5.756226,-9.918338,8.869592,6.808075,-5.720369,-6.297219,0.395443,3.288943,9.805019,2.838252,-6.759417,4.055953,8.251916,6.011087,0.131920,-8.405816,-0.693902,7.514601,8.168815,6.982501,3.828431,-8.063584,2.954340,2.474377,4.351925,7.802618,-6.061157,6.459520,1.500774,-4.587647,-1.114389,7.871087,1.489244,-1.227296,-7.528470,-6.913628,-5.980630,-2.814596,-8.368968,-5.191674,-1.792509,9.236486,-5.682460,2.384719,3.692479,-9.995646,-2.545407,-9.770275,-5.579428,-0.851825,-0.002048,-2.375174,7.959177,-8.810337,-4.328743,-8.823639,-3.963827,4.592789,-4.932281,3.608561,3.605332,1.616214,7.662226,7.646422,3.105335,-2.325266,1.978086,-0.064912,2.260951,-4.289957,9.797254,5.925225,1.971941,-6.919227,5.137613,9.532429,1.746225,-5.262143,5.182504,-4.293915,1.524970,-8.307850,-2.951359,-4.636583,-9.748257,4.258521,5.625035,2.557697,-7.162812,-0.247161,1.071376,-2.233065,1.523308,-8.351357,-3.318806,2.012291,0.821744,-5.933693,-9.966495,-6.147407,-9.924231,-0.036458,-9.715376,-5.568921,6.794190,-5.314610,-7.473596,4.842205,2.170253,-9.345975,-3.148070,0.732608,-7.387324,5.077151,-0.423933,8.981363,-8.540522,-2.176762,5.374037,8.154828,-7.867708,-3.818657,-2.385760,-8.524531,8.474147,5.348121,-1.428781,9.945461,4.132123,5.946591,-9.605715,-0.653288,-6.487472,9.248324,6.988190,-4.260786,-8.464668,-7.435830,-6.195888,-7.222404,-0.662512,8.988896,2.117602,2.600967,-1.680009,-7.923265,2.348971,2.455371,-4.091920,0.478064,8.296485,4.166998,-6.563833,-1.352476,-4.467149,-5.038226,-6.403836,5.876267,9.247629,-9.738733,4.363965,-4.907163,0.070757,-2.215738,9.635320,1.086117,0.385618], dtype = "float64")#candidate|4314|(1215,)|const|float64
var_4315 = relay.var("var_4315", dtype = "uint16", shape = (2560,))#candidate|4315|(2560,)|var|uint16
call_4312 = relay.TupleGetItem(func_2403_call(relay.reshape(var_4313.astype('bool'), [819,]), relay.reshape(const_4314.astype('float64'), [1215,]), relay.reshape(var_4315.astype('uint16'), [2560,]), relay.reshape(call_4310.astype('uint16'), [2,]), relay.reshape(var_4315.astype('uint16'), [2560,]), ), 1)
call_4316 = relay.TupleGetItem(func_2409_call(relay.reshape(var_4313.astype('bool'), [819,]), relay.reshape(const_4314.astype('float64'), [1215,]), relay.reshape(var_4315.astype('uint16'), [2560,]), relay.reshape(call_4310.astype('uint16'), [2,]), relay.reshape(var_4315.astype('uint16'), [2560,]), ), 1)
output = relay.Tuple([call_4308,call_4310,call_4312,var_4313,const_4314,var_4315,])
output2 = relay.Tuple([call_4309,call_4311,call_4316,var_4313,const_4314,var_4315,])
func_4322 = relay.Function([var_4313,var_4315,], output)
mod['func_4322'] = func_4322
mod = relay.transform.InferType()(mod)
mutated_mod['func_4322'] = func_4322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4322_call = mutated_mod.get_global_var('func_4322')
var_4324 = relay.var("var_4324", dtype = "bool", shape = (819,))#candidate|4324|(819,)|var|bool
var_4325 = relay.var("var_4325", dtype = "uint16", shape = (2560,))#candidate|4325|(2560,)|var|uint16
call_4323 = func_4322_call(var_4324,var_4325,)
output = call_4323
func_4326 = relay.Function([var_4324,var_4325,], output)
mutated_mod['func_4326'] = func_4326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_4328 = relay.TupleGetItem(func_2152_call(), 0)
call_4329 = relay.TupleGetItem(func_2154_call(), 0)
output = call_4328
output2 = call_4329
func_4340 = relay.Function([], output)
mod['func_4340'] = func_4340
mod = relay.transform.InferType()(mod)
output = func_4340()
func_4341 = relay.Function([], output)
mutated_mod['func_4341'] = func_4341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2953_call = mod.get_global_var('func_2953')
func_2954_call = mutated_mod.get_global_var('func_2954')
call_4417 = func_2953_call()
call_4418 = func_2953_call()
output = relay.Tuple([call_4417,])
output2 = relay.Tuple([call_4418,])
func_4422 = relay.Function([], output)
mod['func_4422'] = func_4422
mod = relay.transform.InferType()(mod)
mutated_mod['func_4422'] = func_4422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4422_call = mutated_mod.get_global_var('func_4422')
call_4423 = func_4422_call()
output = call_4423
func_4424 = relay.Function([], output)
mutated_mod['func_4424'] = func_4424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2953_call = mod.get_global_var('func_2953')
func_2954_call = mutated_mod.get_global_var('func_2954')
call_4463 = func_2953_call()
call_4464 = func_2953_call()
func_121_call = mod.get_global_var('func_121')
func_124_call = mutated_mod.get_global_var('func_124')
var_4479 = relay.var("var_4479", dtype = "bool", shape = (819,))#candidate|4479|(819,)|var|bool
call_4478 = relay.TupleGetItem(func_121_call(relay.reshape(var_4479.astype('bool'), [819,])), 1)
call_4480 = relay.TupleGetItem(func_124_call(relay.reshape(var_4479.astype('bool'), [819,])), 1)
output = relay.Tuple([call_4463,call_4478,var_4479,])
output2 = relay.Tuple([call_4464,call_4480,var_4479,])
func_4482 = relay.Function([var_4479,], output)
mod['func_4482'] = func_4482
mod = relay.transform.InferType()(mod)
mutated_mod['func_4482'] = func_4482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4483 = relay.var("var_4483", dtype = "bool", shape = (819,))#candidate|4483|(819,)|var|bool
func_4482_call = mutated_mod.get_global_var('func_4482')
call_4484 = func_4482_call(var_4483)
output = call_4484
func_4485 = relay.Function([var_4483], output)
mutated_mod['func_4485'] = func_4485
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4512 = relay.var("var_4512", dtype = "float32", shape = (12, 1, 4))#candidate|4512|(12, 1, 4)|var|float32
uop_4513 = relay.erf(var_4512.astype('float32')) # shape=(12, 1, 4)
const_4515 = relay.const([[[0.674315,-5.473710,-3.752823,1.294755]],[[-5.223176,-7.694750,-3.808279,-2.617971]],[[1.971707,-1.460167,-6.869737,-0.589581]],[[6.735658,7.604982,-2.822387,-2.750812]],[[-6.264211,-1.915754,0.676472,8.550048]],[[-0.128961,-8.291964,-7.522345,4.495024]],[[-5.274885,-2.893874,0.730407,8.566754]],[[-0.972626,3.148127,-6.217514,-7.070855]],[[-2.359380,9.608800,4.013769,-4.123480]],[[4.631742,-7.360749,5.583119,9.426100]],[[-6.579756,-5.363571,-3.675388,-0.385399]],[[8.369942,-2.969846,7.219669,-5.645448]]], dtype = "float32")#candidate|4515|(12, 1, 4)|const|float32
bop_4516 = relay.mod(uop_4513.astype('float32'), relay.reshape(const_4515.astype('float32'), relay.shape_of(uop_4513))) # shape=(12, 1, 4)
output = relay.Tuple([bop_4516,])
output2 = relay.Tuple([bop_4516,])
func_4522 = relay.Function([var_4512,], output)
mod['func_4522'] = func_4522
mod = relay.transform.InferType()(mod)
var_4523 = relay.var("var_4523", dtype = "float32", shape = (12, 1, 4))#candidate|4523|(12, 1, 4)|var|float32
output = func_4522(var_4523)
func_4524 = relay.Function([var_4523], output)
mutated_mod['func_4524'] = func_4524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_4545 = func_2649_call()
call_4546 = func_2649_call()
func_3895_call = mod.get_global_var('func_3895')
func_3898_call = mutated_mod.get_global_var('func_3898')
var_4550 = relay.var("var_4550", dtype = "float64", shape = (42,))#candidate|4550|(42,)|var|float64
call_4549 = relay.TupleGetItem(func_3895_call(relay.reshape(var_4550.astype('float64'), [1, 3, 14])), 0)
call_4551 = relay.TupleGetItem(func_3898_call(relay.reshape(var_4550.astype('float64'), [1, 3, 14])), 0)
func_4168_call = mod.get_global_var('func_4168')
func_4171_call = mutated_mod.get_global_var('func_4171')
const_4553 = relay.const([5.715866,2.069492,8.136595,-9.198218,-3.489851,3.137379,2.324032,3.188221,-5.591602,1.189429,4.549032,3.551570,9.307684,-6.803815,-4.542352,3.760766,-3.184274,-3.500342,-6.944763,-6.463168,7.206121,-5.366120,-5.003164,3.854843,5.274475,-5.177799,-3.046487,4.355411,-9.094267,8.153582,5.314192,-2.300501,2.608762,8.858677,-9.200534,4.364133,4.899109,-8.282126,5.891234,4.139932,-9.716590,6.621939,9.264250,-2.555496,-4.746921,-4.131999,-0.420688,7.549639,-3.693939,-8.448646,-9.763757,-6.042149,3.426218,-2.353516,7.021469,-7.899909,9.366535,-5.737299,-9.082008,-9.423758,-9.642088,4.257813,-2.349488,2.939540,6.766469,5.142488,3.488513,-6.035962,-7.668090,8.986517,-9.572020,-2.172820,5.997746,-5.666779,9.514961,-3.762932,2.351981,8.874202,-7.050193,-9.068776,-2.450024,9.501425,-6.903155,-9.175084,-8.843123,-4.313594,8.745092,6.819748,2.538885,0.091492,-3.393866,3.242452,8.524032,5.230509,5.828645,7.472708,2.378578,0.236052,-3.100818,0.708844,1.361688,8.363732,-0.894712,7.393328,-7.684157,-2.559024,-8.158213,9.946973,-0.383649,8.101097,-1.553550,5.892689,1.636881,8.197084,0.016665,9.447735,-8.108630,7.214626,8.368955,1.062548,1.667604,-2.661187,1.576589,7.969554,5.833362,4.223185,-0.952021,0.979343,6.563739,5.489537,0.848279,9.523897,-2.842414,-2.957595,1.149672,6.076404,-1.329604,-6.828714,5.271303,3.862146,-2.766217,2.708780,-7.313157,-5.223621,2.194677,-5.496740,-1.261023,1.555354,-9.579768,-3.017229,0.912358,8.752415,-1.612227,3.564953,0.632347,-6.980342,7.095095,-2.354054,-6.249323,8.016162,4.333528,8.948067,1.947821,-7.852308,-9.904919,0.218355,-5.216281,7.881492,-0.534854,7.037760,-1.907002,2.228368,7.547102,8.436807,-0.455138,8.117525,-4.508146,-7.168491,5.749576,7.019945,6.026416,1.303724,0.347072,-0.537321,4.721037,-6.563746,2.947977,2.474013,9.221783,3.259760,0.715517,4.518592,3.558123,3.806163,-0.581239,-0.064895,2.634481,-3.223389,3.432054,-3.079909,-5.494527,-0.752952,-9.487459,-0.864532,-8.072502,-1.728962,-5.668270,0.887257,6.669866,3.483466,3.060243,9.215906,7.409664,-0.542408,3.572953,-2.714271,5.224455,6.489526,-5.495583,6.349896,1.545889,6.003264,-4.215088,6.985143,5.290694,7.973210,7.489794,-5.588517,-3.573055,9.038771,2.534914,2.705611,-2.916537,8.487334,-1.297473,8.504257,-1.342746,-9.432626,6.002386,-3.888382,-2.309984,8.466871,-3.127361,-9.653967,-9.892342,-2.197898,2.354970,-6.953567,2.450785,4.776039,3.378475,7.865066,2.059231,-8.020062,-9.799338,4.123179,-1.334885,-0.576385,-0.429204,-8.977273,-4.250821,1.445303,-4.089010,2.178370,5.154192,-8.661619,9.204148,-6.122395,7.693905,3.182186,0.697997,-0.184526,5.527897,-8.072126,1.797740,7.379049,-9.695881,-3.253476,-0.525761,-8.961844,-6.728366,-1.457667,-2.824099,-4.051263,3.795948,3.355511,-4.181621,7.376519,-0.358598,-3.508963,-9.370112,9.678935,-9.582120,8.989881,6.219537,-8.367105,-1.773495,5.619862,6.397951,-9.204966,6.007681,0.207090,7.077502,-6.005368,-8.077119,-6.982685,-2.547487,8.231064,4.596600,7.889375,-3.228516,-9.007229,9.404118,-8.544878,3.803726,5.270063,-3.690280,-8.730867,6.488867,-1.027129,3.275148,-4.676027,-4.133494,-6.260377,7.979771,4.545501,5.777673,-1.764665,1.350914,0.117131,-9.335274,-8.335683,6.551963,-8.171179,9.704518,9.708954,7.338499,-8.520272,5.205016,6.714178,-3.190770,4.871115,-0.027238,-3.681239,-4.708245,-2.168837,8.890262,1.312845,-8.542382,8.144633,-8.692458,-0.245950,8.965420,-3.785571,-0.630642,2.702174,-4.571621,-1.145691,-2.066246,-1.620491,5.158730,1.454159,0.273838,1.295359,5.924836,3.399888,7.961513,4.788387,-0.292210,-0.120805,-1.493126,-2.401209,-2.885854,8.158525,7.620663,1.201539,5.536882,6.070827,0.773585,-7.686550,-8.963059,7.433678,9.237006,-0.362200,-0.917488,-1.680216,-0.439755,2.313789,-9.473505,5.777580,-3.535830,-2.844679,-0.906116,0.685169,-3.646583,-1.201303,0.297113,4.766959,-9.034006,2.520538,-0.578021,8.659534,-5.820977,1.898599,-2.659349,-5.463826,1.995510,-4.937957,3.971575,3.767473,9.231036,-9.254324,0.868341,4.076002,1.175056,-6.949433,7.004359,-5.100453,-8.048747,-3.251942,-8.907251,-9.199443,9.828085,9.902537,-1.581015,-7.868205,-0.722974,-9.502277,-0.360632,-9.569679,-1.594716,6.599891,-9.764329,8.251506,3.330787,1.926609,7.778238,4.558483,-8.027172,8.967117,-3.542571,-7.578750,-4.352289,-5.063397,6.608590,-4.768898,-9.741549,4.858741,8.708003,8.732406,-0.480671,-6.119584,-2.789398,-0.302638,8.414970,9.120197,5.075098,-8.053642,8.572385,8.239610,2.826105,-1.505105,4.982079,1.274627,9.490451,-2.487661,3.062958,9.376477,-5.319389,2.029413,1.992947,5.605487,-1.087067,-6.477653,6.285211,-0.607868,5.045192,-3.721501,-9.149865,7.439786,-8.128684,0.651102,-5.960091,-8.710756,-0.384116,-4.307078,-0.887929,6.165171,-1.882790,-5.757404,7.629510,-0.915895,-9.006499,7.223348,-9.764920,-2.976139,-3.579396,8.631818,-5.137174,-1.089046,1.927718,-5.474007,-2.052199,-5.068893,1.725769,-5.458373,-7.062405,9.669564,6.338312,1.795139,1.656668,7.514708,-2.784081,-5.964666,-4.288362,2.341743,-6.486418,4.911142,1.034162,7.834553,8.341060,8.089730,-4.786526,-0.492376,-3.738480,-3.741464,5.562646,9.086648,-7.297276,-5.582220,-9.534872,-7.899654,4.574171,-4.232074,1.606706,9.857616,1.565805,-8.909732,1.690776,-9.009266,8.270778,0.943575,-1.088423,-1.357465,-0.191457,7.485209,-8.059169,7.412819,5.880590,9.169258,3.559494,8.005353,5.564022,1.392065,-4.834020,-3.623661,-3.889980,-8.453054,1.889410,9.934500,1.456396,-8.058278,-3.499868,5.104889,2.277369,-9.193154,9.554742,-2.269478,-0.371148,2.956096,7.122524,-9.021450,7.218109,-4.092058,6.335647,3.440686,-2.939276,-9.769251,8.041808,-8.500847,-5.934514,-2.224298,4.235502,1.368877,-8.297786,-0.663393,-2.833852,8.083918,-0.879875,-7.488347,9.760554,-8.545501,-9.615145,-7.446597,1.461966,-9.510484,2.349256,6.987814,6.469467,-8.306686,-6.468907,3.111302,5.261746,-0.006542,-4.284701,8.034913,-1.485740,4.012286,3.327694,9.347925,4.952456,-1.412099,-2.171217,3.727416,-9.484506,0.616788,-6.513137,-7.047388,5.221647,0.536905,9.088766,4.450303,2.057896,-3.330597,-8.554737,4.346206,-9.630423,-4.599337,6.084970,-7.399757,-9.044790,-8.017310,9.594949,-0.978852,-9.730207,-5.535831,2.009247,3.215957,8.154407,1.825682,0.669074,6.559686,-3.795399,-1.605499,5.953485,-6.683954,-4.616659,-3.568242,0.329564,-9.571783,0.667904,3.796083,-7.286551,5.350845,2.785521,7.943820,4.790024,-5.737637,9.597211,5.136163,2.647485,-4.271119,9.054278,1.799284,6.928091,-2.208088,8.047004,1.471012,-6.545305,0.835673,8.170676,7.753059,7.254066,1.215613,-7.800059,4.877924,-9.938005,-9.354380,-2.255783,-4.398575,4.260396,-4.074383,-9.519074,9.055516,-2.169722,-6.391715,9.954013,-3.481576,5.014527,7.279441,2.569403,-2.759758,-3.549771,1.618598,-3.073042,7.410401,-9.355962,-2.449017,5.167795,0.177137,-1.085609,-8.027717,5.301321,-4.476754,-6.246783,4.831651,-6.848662,9.937326,-8.872229,-4.416868,-9.351584,-4.800710,9.243569,5.230977,-8.934018,1.068506,2.311451,3.243289,-1.365044,3.583036,1.522141,-1.855522,-3.808273,7.409772,-5.147541,-8.058439,6.543043,2.346420,6.586217,0.826139,-5.469944,1.730221,-6.199063,-9.932922,-3.031852,4.695853,-3.045532,-0.895793,9.843765,9.583589,8.750019,-2.896740,2.809444,5.153755,6.660760,-8.098527,2.144882,4.662486,-2.376819,5.079400,5.145775,4.041955,-5.251377,2.026968,8.101187,-4.918548,-6.745233,4.985226,-0.152334,-0.106837,1.639764,0.992350,-4.725784,8.369653,1.087301,-8.005819,7.171858,-7.788358,7.076766,-7.726854,7.557368,8.093677,6.348482,8.606542,3.468189,4.689864,-6.484481,-9.413668,5.599324,-1.310106,-8.791675,-7.298912,-1.229139,5.054383,-7.912696,-6.097202,-4.431033,5.978154,-4.812606,-6.154412,-3.914096,-9.994547,-7.071649,-6.713798,-6.647340,-7.689840,0.815708,0.816002,-5.958803,7.016786,-9.528120,-6.300818,0.422785,-2.783525,-9.543205,1.397767,6.631637,1.784532,-1.041417,2.739421,-1.523157,8.741051,-5.958809,6.307200,-0.131102,3.766682,-0.690980,2.209994,3.308909,5.602239,-3.793146,9.814086,0.519384,-2.106398,-2.961877], dtype = "float32")#candidate|4553|(825,)|const|float32
call_4552 = relay.TupleGetItem(func_4168_call(relay.reshape(const_4553.astype('float32'), [5, 11, 15])), 1)
call_4554 = relay.TupleGetItem(func_4171_call(relay.reshape(const_4553.astype('float32'), [5, 11, 15])), 1)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_4567 = relay.TupleGetItem(func_2717_call(), 0)
call_4568 = relay.TupleGetItem(func_2719_call(), 0)
output = relay.Tuple([call_4545,call_4549,var_4550,call_4552,const_4553,call_4567,])
output2 = relay.Tuple([call_4546,call_4551,var_4550,call_4554,const_4553,call_4568,])
func_4577 = relay.Function([var_4550,], output)
mod['func_4577'] = func_4577
mod = relay.transform.InferType()(mod)
mutated_mod['func_4577'] = func_4577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4578 = relay.var("var_4578", dtype = "float64", shape = (42,))#candidate|4578|(42,)|var|float64
func_4577_call = mutated_mod.get_global_var('func_4577')
call_4579 = func_4577_call(var_4578)
output = call_4579
func_4580 = relay.Function([var_4578], output)
mutated_mod['func_4580'] = func_4580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3332_call = mod.get_global_var('func_3332')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_4626 = relay.TupleGetItem(func_3332_call(), 0)
call_4627 = relay.TupleGetItem(func_3333_call(), 0)
output = relay.Tuple([call_4626,])
output2 = relay.Tuple([call_4627,])
func_4648 = relay.Function([], output)
mod['func_4648'] = func_4648
mod = relay.transform.InferType()(mod)
mutated_mod['func_4648'] = func_4648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4648_call = mutated_mod.get_global_var('func_4648')
call_4649 = func_4648_call()
output = call_4649
func_4650 = relay.Function([], output)
mutated_mod['func_4650'] = func_4650
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4750 = relay.var("var_4750", dtype = "float32", shape = (3, 9, 2))#candidate|4750|(3, 9, 2)|var|float32
uop_4751 = relay.log(var_4750.astype('float32')) # shape=(3, 9, 2)
uop_4762 = relay.asin(var_4750.astype('float64')) # shape=(3, 9, 2)
func_4302_call = mod.get_global_var('func_4302')
func_4304_call = mutated_mod.get_global_var('func_4304')
const_4774 = relay.const([3.125394,-6.752171,6.142975,9.713129,-7.170662,1.677369,-8.966049,-6.527590,8.243563,9.892074,-1.861136,9.497143,5.405043,-7.811208,1.008584,8.644184,-7.450094,-9.907051,3.853039,-1.530416,3.888140,-8.576518,3.879580,-8.173480,-3.753840,4.815999,8.731884,-7.411325,-3.482296,1.553301,7.952463,-6.188888,-5.796301,1.235623,-3.207155,4.514457,0.037706,3.198152,-5.051832,2.412894,-4.973413,7.893529,3.425707,-5.031509,3.477441,-6.314725,1.059648,-7.583561,4.456908,5.535491,4.806363,6.305738,0.487310,3.915689,4.090102,-0.212764,8.694386,5.099156,0.149528,-7.554247,4.500317,5.981379,3.269370,-3.912263,5.690251,3.990303,-6.734498,6.818390,0.404331,-5.979954,-5.503558,-3.380081,-4.283927,-2.319413,-8.710016,-7.294885,3.877049,-7.121312,-2.571239,-3.365824,-2.411457,-1.972899,-4.007407,-6.978138,8.306536,-3.229248,0.690422,0.505947,-6.044478,-7.091643,4.363090,-1.431313,-0.134995,1.241197,4.709842,4.565607,7.581126,4.349461,5.377668,-8.472597,-4.634249,-6.734860,2.053031,4.866345,-4.480538,-6.179700,9.836177,-3.314498,3.290434,-6.390632,4.069811,5.599097,3.940127,0.889495,-9.883797,9.889305,-0.647864,3.596896,-3.752336,-5.293468,-7.358593,-4.517102,9.840502,3.973918,-3.140519,-2.406817,0.419139,6.032093,-3.927698,-2.573111,-1.832888,4.144667,3.562458,-1.729988,8.485538,-6.234064,-5.433964,7.477516,-9.051930,-7.370579,-6.415497,-2.735809,-4.233161,0.428515,-1.046537,-0.996725,4.435592,-1.411994,-8.225187,-9.006416,9.926976,4.218223,6.997366,1.395763,6.435899,5.564737,-8.116865,-1.257272,2.986217,5.613946,0.209562,-0.788907,8.897989,7.208214,8.766166,-1.801498,9.049308,-3.350281,-8.397966,-5.525995,-9.737713,-5.218218,7.659754,5.635317,-8.881317], dtype = "float32")#candidate|4774|(175,)|const|float32
call_4773 = relay.TupleGetItem(func_4302_call(relay.reshape(const_4774.astype('float32'), [175,])), 1)
call_4775 = relay.TupleGetItem(func_4304_call(relay.reshape(const_4774.astype('float32'), [175,])), 1)
uop_4786 = relay.sin(uop_4762.astype('float32')) # shape=(3, 9, 2)
func_4322_call = mod.get_global_var('func_4322')
func_4326_call = mutated_mod.get_global_var('func_4326')
var_4792 = relay.var("var_4792", dtype = "bool", shape = (819, 1))#candidate|4792|(819, 1)|var|bool
var_4793 = relay.var("var_4793", dtype = "uint16", shape = (2560,))#candidate|4793|(2560,)|var|uint16
call_4791 = relay.TupleGetItem(func_4322_call(relay.reshape(var_4792.astype('bool'), [819,]), relay.reshape(var_4793.astype('uint16'), [2560,]), ), 2)
call_4794 = relay.TupleGetItem(func_4326_call(relay.reshape(var_4792.astype('bool'), [819,]), relay.reshape(var_4793.astype('uint16'), [2560,]), ), 2)
const_4807 = relay.const([[[-8.182629,9.323321],[-4.766468,3.423849],[-4.751727,8.886056],[4.644167,6.573017],[0.482499,8.989160],[-6.199727,7.648525],[9.539138,7.767794],[3.084986,8.726469],[-4.323021,-4.742941]],[[-3.642994,6.314556],[-7.572872,1.435174],[7.185654,-7.839967],[8.005022,3.417272],[3.652769,1.925322],[-0.469593,2.976886],[4.420660,9.320993],[8.349404,8.385471],[-7.802834,-2.657592]],[[7.812042,-8.131703],[-8.460629,2.802904],[-5.803056,4.856144],[-7.782959,-9.205980],[8.531322,-2.645025],[-8.995196,-9.314225],[9.526280,3.687445],[1.206099,-4.713271],[7.955109,9.755055]]], dtype = "float64")#candidate|4807|(3, 9, 2)|const|float64
bop_4808 = relay.logical_or(uop_4762.astype('bool'), relay.reshape(const_4807.astype('bool'), relay.shape_of(uop_4762))) # shape=(3, 9, 2)
output = relay.Tuple([uop_4751,call_4773,const_4774,uop_4786,call_4791,var_4792,var_4793,bop_4808,])
output2 = relay.Tuple([uop_4751,call_4775,const_4774,uop_4786,call_4794,var_4792,var_4793,bop_4808,])
func_4821 = relay.Function([var_4750,var_4792,var_4793,], output)
mod['func_4821'] = func_4821
mod = relay.transform.InferType()(mod)
var_4822 = relay.var("var_4822", dtype = "float32", shape = (3, 9, 2))#candidate|4822|(3, 9, 2)|var|float32
var_4823 = relay.var("var_4823", dtype = "bool", shape = (819, 1))#candidate|4823|(819, 1)|var|bool
var_4824 = relay.var("var_4824", dtype = "uint16", shape = (2560,))#candidate|4824|(2560,)|var|uint16
output = func_4821(var_4822,var_4823,var_4824,)
func_4825 = relay.Function([var_4822,var_4823,var_4824,], output)
mutated_mod['func_4825'] = func_4825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3538_call = mod.get_global_var('func_3538')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_4847 = func_3538_call()
call_4848 = func_3538_call()
output = relay.Tuple([call_4847,])
output2 = relay.Tuple([call_4848,])
func_4851 = relay.Function([], output)
mod['func_4851'] = func_4851
mod = relay.transform.InferType()(mod)
output = func_4851()
func_4852 = relay.Function([], output)
mutated_mod['func_4852'] = func_4852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_4858 = func_2649_call()
call_4859 = func_2649_call()
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_4862 = func_2238_call()
call_4863 = func_2238_call()
func_810_call = mod.get_global_var('func_810')
func_815_call = mutated_mod.get_global_var('func_815')
const_4882 = relay.const([-7.957438,2.585632,8.256727,9.397733,6.295624,-6.536978,-2.325273,5.419065,-8.503464,6.162852,1.439783,7.971284,1.807895,6.721934,-9.291998,-1.886097,-9.675863,-2.690956,0.390374,0.081741,-7.799190,8.203164,-3.979453,3.718771,4.320001,-3.657399,-3.122937,1.666657,-7.506146,8.456098,-2.724559,3.609615,8.059288,9.174287,2.077976,7.898735,-6.854564,-2.176068,8.379623,3.352827,-9.126329,-5.037778,1.901641,5.394706,-7.859413,2.828964,-1.246680,1.572887,-1.131694,-3.266919,-2.889200,6.212205,-7.352390,0.838170,-6.547978,3.867881,-9.825178,4.295746,9.703297,2.706576,6.994005,6.051164,8.468407,-0.489960,8.537806,4.812553,-7.088964,-3.722277,3.970365,3.187870,-5.244047,-3.161599,-9.084117,-7.778662,-6.544148,1.254724,-0.509999,-8.378878,-5.831199,7.155836,2.812967,5.349638,-1.801961,4.912600,7.572865,2.440873,9.783074,9.257258,3.469021,3.958835,7.884241,-5.852857,5.767931,-6.631336,9.070871,8.227435,-3.929217,-4.796490,-5.430745,-8.361908,-1.363423,9.593384,-4.374773,0.630481,7.810339,7.097743,-1.497153,-9.513292,-6.783949,1.205382,4.288852,9.669802,6.239518,-4.782986,0.580792,7.530920,-8.374751,6.854721,4.259289,-4.153437,8.979530,-8.828247,0.771742,-4.080888,2.545871,6.508467,-2.508356,-6.302555,8.568397,-8.940505,-6.785040,-4.593074,-4.937492,0.010909,3.246468,-3.578624,6.786390,-8.211598,-5.595323,6.748729,-5.932809,-8.191581,4.354711,-9.367222,0.471018,6.757234,-8.839853,-3.444989,6.979144,7.443295,9.967620,1.703604,-7.069755,-6.487428,-6.633253,-6.430242,-4.912408,-5.255847,2.256114,-6.013647,0.648248,-8.219412,-8.124551,-9.844500,-3.035505,-2.803449,-2.886977,9.487597,3.057130,5.038030,4.239469,-3.441455,-9.855826,5.849817,0.144364,-2.809206,2.919759,-4.385337,4.450426,3.094203,-5.590281,8.301856,0.326626,3.988942,-7.321269,0.979291,-7.968627,-7.929888,-2.047426,5.610845,3.187470,-8.195525,-2.006027,-6.360642,7.292434,-6.433207,8.260861,-8.806970,-3.404415,9.762038,-9.217945,-1.391276,-2.960848,7.994411,-8.749532,-7.166933,-7.615357,-0.481256,-9.206973,-5.132469,-5.533100,4.787051,1.492804,-1.803759,-9.887457,-4.869116,-9.849899,0.924666,5.447886,9.982804,3.527170,-4.065007,-7.441799,7.171341,3.276981,1.855884,-1.138631,-7.363897,-2.752825,9.245954,-4.543083,-7.869747,-9.786372,-6.985555,-9.982230,3.541006,0.047519,-8.473703,-3.289880,-8.571912,7.646763,3.999575,4.286646,0.702643,-8.428404,-2.037878,4.072670,-9.866755,-0.237936,7.234006,-1.322553,0.443431,-6.660075,-4.763635,5.664036,5.123399,-3.738648,-7.501162,-5.421171,4.190135,-4.905500,9.311137,-9.002877,5.628246,-5.531677,-0.165324,3.581946,1.592551,9.406987,-5.826416,-4.816157,8.419028,-5.496382,-2.123773,-2.806813,2.074126,1.923977,-9.020851,-0.979648,1.409014,-5.545464,-1.914849,7.919907,-0.097569,4.731838,1.953198,-1.900961,-3.082762,-8.169179,7.650325,-2.495481,9.103006,7.558765,-7.279002,2.093648,3.426062,2.645032,8.671011,5.374260,5.099306,-8.572493,-8.059276,1.187991,8.771160,-7.795800,-1.095369,9.910800,-9.018310,9.105464,4.594303,-9.806554,9.821560,-8.114342,-9.884367,-5.474178,-2.438960,-7.818674,4.974015,0.785567,5.344129,0.668805,-8.435904,0.064391,7.727801,7.946336,1.641065,7.318170,2.721240,7.064566,7.611624,9.428621,-9.930002,1.054173,-4.476025,-6.708414,-8.647445,6.414990,2.805218,6.025751,-4.019832,6.758551,7.262795,-5.462500,-4.574589,-8.236895,2.307717,3.315565,-9.375875,1.382476,0.141715,-7.302395,2.012686,-8.483071,3.785110,2.534492,4.361719,5.701225,-8.839210,0.050908,-5.944202,-1.491457,-3.973807,2.281174,-5.713368,7.715859,4.945347,6.103846,6.127480,7.094815,-6.652412,-8.619079,6.332029,-2.176113,5.161320,-2.627444,1.711577,3.537438,-3.462790,-7.676708,1.194440,-2.404529,-5.410089,6.512205,9.741711,-7.474709,-0.357368,9.040729,-5.547943,4.992000,-3.745696,6.616840,-2.359012,7.050683,-4.698920,-6.935147,9.926129,-9.820474,-5.751982,2.233371,-4.581008,9.804434,7.835792,-7.320599,-1.340446,1.749446,6.201541,1.335852,-7.773312,-2.801964,-1.240539,-2.162358,9.023823,5.310370,6.017231,1.599481,-1.850909,-9.557486,-5.454191,-1.685537,-6.617074,7.194049,-2.547768,5.473933,4.328071,9.508482,-1.855353,2.186735,-1.186462,-1.198361,4.899820,2.996110,-9.828032,7.177676,-0.393735,-4.589294,-8.067073,-1.176393,-4.070860,2.449109,9.642434,8.780701,-4.975441,0.681156,-8.963477,-5.794565,-9.500760,9.679716,1.349121,5.649119,-0.729154,-2.521690,4.265108,-2.855794,9.178808,0.521431,-8.939073,-6.104440,2.398916,-1.068889,8.827029,1.578034,-7.055664,8.980115,-4.202838,-2.926417,-2.104785,3.281299,2.597092,2.820918,6.418777,-3.793696,7.644043,-5.920485,-2.239596,-9.954243,-1.073251,9.113168,8.355976,-0.169493,7.106151,-8.265478,-5.304797,3.613884,6.809274,-9.545960,6.052383,1.060901,6.114130,0.877356,-8.161666,-5.288531,-0.495693,6.986863,-2.711375,9.440353,-6.774203,3.338388,5.857420,4.993394,5.337466,7.043912,-2.333690,4.346710,-8.236293,4.417054,3.226312,4.038904,-6.630521,0.578228,7.012421,-9.114271,-2.578785,-1.686938,1.578003,6.924810,3.522369,5.284719,9.403605,2.446082,-6.780107,-6.144502,-7.550903,4.405442,-2.458135,8.853000,3.923060,-6.022079,7.606571,1.282688,-4.418186,6.086999,1.599431,2.252168,-1.235932,-4.137513,1.579402,-6.951565,2.525911,-6.528452,-9.879420,3.165083,-1.887993,9.493353,-4.620263,-6.401972,3.087447,-2.577597,-9.982561,0.239822,-6.899543,2.556838,-9.349505,-1.744459,8.290671,-3.711069,-6.065075,3.370170,0.642212,4.339641,4.462448,-3.756981,3.135189,8.413853,-3.926790,-6.851700,5.584524,-7.188673,8.821220,9.557687,-6.543251,-0.400006,9.828493,4.390650,0.064869,-3.276789,-0.119141,5.057352,4.036319,5.533803,-7.430040,-5.104459,-2.400870,1.635554,3.539992,-2.064642,-4.962745,0.653899,9.822029,-6.846416,2.984463,3.175813,9.904766,1.857441,-8.061911,-4.181900,5.489389,-8.502186,-2.758717,2.922060,-1.357695,5.533650,4.250670,-6.288321,4.621269,5.873762,2.280221,-8.541978,5.812139,5.907411,-0.865903,-3.259540,-4.275742,8.085098,1.710207,1.843103,5.788493,-6.647299,1.195780,0.303037,-2.257458,0.355681,9.882546,-2.949988,3.146328,-5.716804,-2.951766,3.397201,4.727522,9.525969,-6.128428,-4.174420,8.530866,-4.990139,5.710068,7.339791,-0.204010,0.351755,-3.898919,-6.817271,2.100141,3.627306,-1.216915,0.164144,-4.126298,-8.864403,8.475912,-3.570912,7.014435,1.766518,-0.887547,-2.714809,7.631980,-0.518519,-5.752801,0.707276,-9.435364,7.763820,-6.537766,-4.974400,6.761787,2.622266,-9.851961,6.505499,-0.823982,-0.263531,3.640182,9.472252,8.168176,-7.025350,-0.538037,6.482356,-6.819792,8.098178,6.802717,9.592393,-8.966198,9.279402,-9.155175,9.182863,4.113069,6.053862,-2.800586,8.045738,5.207205,2.319216,-1.240602,-2.278813,5.509244,6.662207,6.514694,1.438791,9.035334,-6.760377,5.910542,-3.441550,-6.147713,9.502550,-2.195939,-4.013309,-1.192153,8.708059,-7.674950,-8.623540,-3.422314,1.603908,-4.030095,9.835312,3.939416,-9.725759,6.358215,-1.013600,-4.079976,8.089960,-6.270018,-3.265250,5.699243,9.646628,5.902306,-0.579665,6.351186,-9.636078,-3.595748,2.076486,5.616205,3.892928,-6.294476,-4.481960,9.806190,1.791192,9.338422,4.701078,-3.472403,9.300198,-7.636281,3.490255,7.886648,1.405552,1.226450,5.749725,-9.267466,-1.657855,-4.306900,-4.361481,-6.302784,-4.735601,3.259144,-7.162757,-7.118504,-6.163153,1.471611,1.982571,2.847954,8.729280,2.394371,5.879218,2.769157,8.057872,6.731926,8.243902,8.264131,8.809296,5.717768,-0.410438,7.986460,-4.261347,-5.462851,4.610945,3.764983,3.498384,-3.519421,-4.815829,-1.865014,0.083857,9.001970,6.992638,-6.236806,-1.558644,-8.958381,-8.676905,2.248845,7.604067,-4.636115,1.066275,9.607279,-2.062490,0.687406,6.576283,-5.507879,1.617018,9.464595,2.533720,-6.985381,-5.049113,-2.166674,-4.905049,4.825048,-2.589001,3.931446,1.391499,-0.769708,-1.628754,0.477990,9.259640,-9.946448,5.103340,2.675182,-1.988053,-5.750667,-3.059335,7.218771,-4.922210,-9.607285,-9.644554,-0.981230,-5.052334,7.369387,1.556773,-1.046924,6.433759,4.263320,9.478039,2.658847,-1.212317,-0.038192,-9.553891,-5.219981,-7.938171,0.882574,-9.395173,6.712588,-8.642172,9.125696,9.820107,-5.989500,-7.898898,2.385357,-4.755037,2.401523,9.318022,-4.204644,7.849206,-5.654409,2.039222,-5.852341,-1.554039,3.614209,5.858748,-2.533954,-3.839390,2.404629,-3.583009,-1.057662,5.652407,-8.038069,6.534875,-3.637830,6.120376,8.024609,9.502615,-3.780114,6.109919,-6.246974,-2.802010,3.092592,-4.997384,1.234434,6.739011,1.033887,-7.064337,0.957399,-9.630689,-2.472191,4.316842,0.489979,-0.322453,-9.442573,0.399164,-0.704741,4.756518,-8.179998,-6.814649,-4.088461,-4.242036,-6.682649,7.374143,-5.507756,6.242312,9.096134,-5.489941,7.495317,-1.244523,-4.824971,4.748110,6.663243,-9.373850,-1.512844,-7.016103,4.396458,-2.409379,4.763569,9.220080,-4.106039,-4.346391,6.507803,-2.414862,4.327217,-7.505558,-8.065253,-7.835274,-8.609922,2.362719,6.291105,-3.553863,-0.771986,-1.615035,-6.875486,-9.098446,8.898071,2.465485,8.395309,1.793323,-0.306919,5.269198,5.596423,1.378553,-6.680679,-0.769732,-0.780987,-1.801505,-2.062422,-2.929449,3.181969,8.053301,5.218774,3.133616,-3.348144,-5.332120,5.237190,7.240879,3.773300,-9.039573,6.195329,-6.435394,6.037756,4.210453,2.867500,3.075191,-7.171191,6.234577,4.287551,-9.800485,-1.670094,-7.535703,-4.494254,-1.323166,-0.238485,-8.900940,-9.405164,5.997371,5.977567,1.982628,-5.206240,9.082352,5.014871,8.939746,-8.887839,-4.415828,-9.855658,-0.014434,-7.457572,-1.746013,6.403749,-0.403059,8.603484,-5.756671,-7.977542,-7.508745,-6.513973,5.802387,-5.824129,-3.814385,1.563780,9.076973,6.899965,-8.065315,9.828225,5.563973,0.564048,-4.039295,8.023793,-8.903269,-3.341696,3.163747,-6.930429,-0.619951,6.079612,0.985437,7.917163,-5.588850,-9.207870,-6.614187,2.769002,4.491619,5.250689,-9.134303,-1.437716,9.492275,4.696736,0.757335,2.955404,-9.534871,-2.571799,9.110114,8.438094,-0.344181,1.317273,5.342647,-5.476272,5.857622,-5.192062,1.338324,-7.050223,7.548846,4.848778,-5.051282,-3.678432,2.099751,-8.499666,-8.780489,-3.251560,-2.691451,7.613543,-2.788776,-0.987008,5.184020,4.403277,9.136017,5.831284,2.104735,6.129162,-9.593465,7.769432,-6.472858,-1.831104,1.838122,5.346922,-9.265162,3.763607,0.104671,1.232222,-5.299656,3.878001,-0.313662,-0.327606,6.873908,8.690956,9.855084,5.024370,4.010852,-8.178484,-7.353726,-0.807801,-0.584633,5.163086,6.147296,-8.028727,-5.132911,6.991188,4.128109,-7.588515,0.858755,-6.670931,-2.450843,-8.669100,1.472393,-1.498140,-4.043975,8.975845,-6.919155,-9.364646,5.552638,2.953039,-8.866215,-1.853367,-3.710833,-3.401139,5.987313,-6.057344,-6.639496,0.724401,1.961137,8.765413,-2.928191,-6.346144,-1.019982,-7.328119,-2.760263,1.789146,-1.588782,-2.675456,-5.547748,-7.310194,0.075619,-8.701137,5.039109,7.913388,7.753930,-9.675253,7.716206,7.110555,-7.639720,8.306737,1.543457,4.081447,6.905062,3.351460,5.520437,4.183191,-2.492569,-8.886822,0.326390,8.797252,1.715478,-1.925026,-1.389445,-0.915117,7.801647,7.242670,-4.303261,-7.176369,-3.069777,9.217591,8.757894,-8.472728,-2.532827,2.520909,7.256685,3.798246,-1.269746,0.458297,6.555715,1.733499,-4.715883,5.126719,-8.673374,-5.208457,5.296865,-3.396009,-6.648036,2.704066,6.234851,-6.647700,3.219464,0.455344,0.895846,-4.880501,-6.148601,1.090689,8.052173,6.051896,-1.223940,-8.614431,-3.577243,-7.620584,-2.726978,8.873346,-3.828093,-9.696562,1.102416,0.834033,-3.274953,6.335634,-3.826148,4.440926,-0.588624,4.847054,-4.632307,-4.248344,-2.236482,8.676003,-7.611217,-2.257541,-5.425903,-7.631144,3.095298,-4.853646,-8.266539,-6.620560,-1.900000,-0.725394,4.075743,9.851669,9.198324,-6.743302,-4.097137,-8.519853,-9.235103,4.874073,2.707705,1.341781,-3.601891,2.317596,7.373444,8.484236,2.488464,-2.302200,0.875508,5.286984,-0.230493,-4.367257,9.322645,9.684582,9.324551,1.514750,7.664550], dtype = "float64")#candidate|4882|(1215,)|const|float64
var_4883 = relay.var("var_4883", dtype = "uint16", shape = ())#candidate|4883|()|var|uint16
call_4881 = relay.TupleGetItem(func_810_call(relay.reshape(const_4882.astype('float64'), [9, 9, 15]), relay.reshape(const_4882.astype('float64'), [9, 9, 15]), relay.reshape(var_4883.astype('uint16'), []), ), 6)
call_4884 = relay.TupleGetItem(func_815_call(relay.reshape(const_4882.astype('float64'), [9, 9, 15]), relay.reshape(const_4882.astype('float64'), [9, 9, 15]), relay.reshape(var_4883.astype('uint16'), []), ), 6)
bop_4898 = relay.bitwise_and(call_4881.astype('int32'), call_4858.astype('int32')) # shape=(175, 2)
bop_4901 = relay.bitwise_and(call_4884.astype('int32'), call_4859.astype('int32')) # shape=(175, 2)
output = relay.Tuple([call_4862,const_4882,var_4883,bop_4898,])
output2 = relay.Tuple([call_4863,const_4882,var_4883,bop_4901,])
func_4902 = relay.Function([var_4883,], output)
mod['func_4902'] = func_4902
mod = relay.transform.InferType()(mod)
mutated_mod['func_4902'] = func_4902
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4903 = relay.var("var_4903", dtype = "uint16", shape = ())#candidate|4903|()|var|uint16
func_4902_call = mutated_mod.get_global_var('func_4902')
call_4904 = func_4902_call(var_4903)
output = call_4904
func_4905 = relay.Function([var_4903], output)
mutated_mod['func_4905'] = func_4905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4057_call = mod.get_global_var('func_4057')
func_4059_call = mutated_mod.get_global_var('func_4059')
call_4939 = func_4057_call()
call_4940 = func_4057_call()
output = relay.Tuple([call_4939,])
output2 = relay.Tuple([call_4940,])
func_4942 = relay.Function([], output)
mod['func_4942'] = func_4942
mod = relay.transform.InferType()(mod)
output = func_4942()
func_4943 = relay.Function([], output)
mutated_mod['func_4943'] = func_4943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_4955 = func_2238_call()
call_4956 = func_2238_call()
output = call_4955
output2 = call_4956
func_4968 = relay.Function([], output)
mod['func_4968'] = func_4968
mod = relay.transform.InferType()(mod)
output = func_4968()
func_4969 = relay.Function([], output)
mutated_mod['func_4969'] = func_4969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_4992 = func_2238_call()
call_4993 = func_2238_call()
func_1753_call = mod.get_global_var('func_1753')
func_1758_call = mutated_mod.get_global_var('func_1758')
var_4998 = relay.var("var_4998", dtype = "uint16", shape = (2560,))#candidate|4998|(2560,)|var|uint16
const_4999 = relay.const(-4, dtype = "uint16")#candidate|4999|()|const|uint16
const_5000 = relay.const([-2.176801,-4.731780,9.946824,9.941280,-4.626306,-1.073311,1.129785,-7.248418,0.322112,-1.300981,9.362704,-1.497124,-7.169650,0.623904,0.491993,-3.487386,6.123691,9.391932,9.887767,6.675779,-0.691584,-9.107669,4.817554,-8.778503,8.150199,4.538071,-8.035467,-1.698901,-9.976883,3.447157,-4.114124,9.941486,-8.966205,-6.025655,-5.620592,0.550655,-8.428013,-3.098396,-6.067969,-3.618738,8.680941,-6.242212,0.302160,-8.273929,2.950777,-6.521888,-4.619560,9.259444,-0.205166,-1.050370,0.388333,4.644915,0.052753,5.401503,3.464989,-6.371083,8.904886,-4.612862,6.407346,-4.272234,-1.217852,-1.595236,5.758057,2.611294,-5.603280,-9.656892,-1.870507,4.974638,0.430612,8.925279,-1.788819,9.694689,3.099912,-0.070979,2.594139,0.472443,6.646190,-8.778931,9.733216,-8.101336,3.607151,6.069875,4.582383,7.481388,-0.154704,8.198522,-6.048707,-7.527131,-9.619561,6.953432,-6.845027,-7.189077,-1.817907,-5.251459,-7.606775,5.041285,2.415099,0.370348,9.022070,4.158486,-2.147647,-6.156445,6.797489,-7.435801,-4.675991,9.711701,-0.437316,-2.098496,-8.298766,-3.140959,-0.029829,-8.346724,-5.593090,-9.350483,0.619410,3.306398,-1.388221,-7.770043,8.260950,6.415317,-5.015818,-2.246487,-5.903658,-6.933023,7.665295,-5.588400,-9.206234,3.824836,-5.107485,5.903015,1.647881,1.790981,-9.911896,2.802042,-3.846135,8.374156,-3.612316,7.413330,4.074162,8.763613,-6.109686,-0.168584,5.586446,-7.030947,4.198604,4.841046,-8.187306,-3.384811,-8.977148,-8.076036,-7.455466,-7.076897,7.801823,-8.316210,4.664299,4.299534,9.552465,-2.749397,2.541700,-8.332508,-1.995528,5.717492,2.638267,-1.058057,-1.380589,-5.489458,-2.889333,8.995639,0.984185,-2.636276,8.757453,-2.078059,1.150394,0.138592,6.546893], dtype = "float32")#candidate|5000|(175,)|const|float32
const_5001 = relay.const([-3,-1], dtype = "uint16")#candidate|5001|(2,)|const|uint16
call_4997 = relay.TupleGetItem(func_1753_call(relay.reshape(var_4998.astype('uint16'), [16, 10, 16]), relay.reshape(const_4999.astype('uint16'), []), relay.reshape(const_5000.astype('float32'), [175, 1]), relay.reshape(const_5001.astype('uint16'), [2,]), ), 0)
call_5002 = relay.TupleGetItem(func_1758_call(relay.reshape(var_4998.astype('uint16'), [16, 10, 16]), relay.reshape(const_4999.astype('uint16'), []), relay.reshape(const_5000.astype('float32'), [175, 1]), relay.reshape(const_5001.astype('uint16'), [2,]), ), 0)
output = relay.Tuple([call_4992,call_4997,var_4998,const_4999,const_5000,const_5001,])
output2 = relay.Tuple([call_4993,call_5002,var_4998,const_4999,const_5000,const_5001,])
func_5020 = relay.Function([var_4998,], output)
mod['func_5020'] = func_5020
mod = relay.transform.InferType()(mod)
var_5021 = relay.var("var_5021", dtype = "uint16", shape = (2560,))#candidate|5021|(2560,)|var|uint16
output = func_5020(var_5021)
func_5022 = relay.Function([var_5021], output)
mutated_mod['func_5022'] = func_5022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_5053 = func_2649_call()
call_5054 = func_2649_call()
func_3128_call = mod.get_global_var('func_3128')
func_3129_call = mutated_mod.get_global_var('func_3129')
call_5055 = func_3128_call()
call_5056 = func_3128_call()
func_3728_call = mod.get_global_var('func_3728')
func_3735_call = mutated_mod.get_global_var('func_3735')
var_5087 = relay.var("var_5087", dtype = "uint32", shape = (630, 4))#candidate|5087|(630, 4)|var|uint32
const_5088 = relay.const(-5.361529, dtype = "float32")#candidate|5088|()|const|float32
const_5089 = relay.const([[-4],[-8],[-4],[-7],[-7],[9],[8],[-1],[-4],[3],[4],[2],[-4],[9],[-10],[9],[-1],[6],[1],[-6],[-6],[4],[-10],[-10],[4],[10],[7],[-3],[4],[6],[-5],[8],[1],[-1],[-9],[-1],[-5],[1],[-7],[-10],[6],[-8],[-3],[-1],[-3],[2],[3],[-3],[-6],[-7],[3],[-2],[-2],[-4]], dtype = "uint16")#candidate|5089|(54, 1)|const|uint16
call_5086 = relay.TupleGetItem(func_3728_call(relay.reshape(var_5087.astype('uint32'), [15, 14, 12]), relay.reshape(var_5087.astype('uint32'), [15, 14, 12]), relay.reshape(var_5087.astype('uint32'), [15, 14, 12]), relay.reshape(const_5088.astype('float32'), []), relay.reshape(const_5089.astype('uint16'), [54,]), ), 1)
call_5090 = relay.TupleGetItem(func_3735_call(relay.reshape(var_5087.astype('uint32'), [15, 14, 12]), relay.reshape(var_5087.astype('uint32'), [15, 14, 12]), relay.reshape(var_5087.astype('uint32'), [15, 14, 12]), relay.reshape(const_5088.astype('float32'), []), relay.reshape(const_5089.astype('uint16'), [54,]), ), 1)
bop_5092 = relay.logical_and(var_5087.astype('bool'), relay.reshape(call_5086.astype('bool'), relay.shape_of(var_5087))) # shape=(630, 4)
bop_5095 = relay.logical_and(var_5087.astype('bool'), relay.reshape(call_5090.astype('bool'), relay.shape_of(var_5087))) # shape=(630, 4)
bop_5098 = relay.not_equal(call_5053.astype('bool'), const_5089.astype('bool')) # shape=(54, 2)
bop_5101 = relay.not_equal(call_5054.astype('bool'), const_5089.astype('bool')) # shape=(54, 2)
func_4057_call = mod.get_global_var('func_4057')
func_4059_call = mutated_mod.get_global_var('func_4059')
call_5103 = func_4057_call()
call_5104 = func_4057_call()
output = relay.Tuple([call_5055,const_5088,bop_5092,bop_5098,call_5103,])
output2 = relay.Tuple([call_5056,const_5088,bop_5095,bop_5101,call_5104,])
func_5109 = relay.Function([var_5087,], output)
mod['func_5109'] = func_5109
mod = relay.transform.InferType()(mod)
mutated_mod['func_5109'] = func_5109
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5110 = relay.var("var_5110", dtype = "uint32", shape = (630, 4))#candidate|5110|(630, 4)|var|uint32
func_5109_call = mutated_mod.get_global_var('func_5109')
call_5111 = func_5109_call(var_5110)
output = call_5111
func_5112 = relay.Function([var_5110], output)
mutated_mod['func_5112'] = func_5112
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5128 = relay.var("var_5128", dtype = "int16", shape = (12, 15, 6))#candidate|5128|(12, 15, 6)|var|int16
var_5129 = relay.var("var_5129", dtype = "int16", shape = (12, 15, 6))#candidate|5129|(12, 15, 6)|var|int16
bop_5130 = relay.not_equal(var_5128.astype('bool'), relay.reshape(var_5129.astype('bool'), relay.shape_of(var_5128))) # shape=(12, 15, 6)
uop_5146 = relay.erf(bop_5130.astype('float32')) # shape=(12, 15, 6)
func_4851_call = mod.get_global_var('func_4851')
func_4852_call = mutated_mod.get_global_var('func_4852')
call_5156 = relay.TupleGetItem(func_4851_call(), 0)
call_5157 = relay.TupleGetItem(func_4852_call(), 0)
bop_5160 = relay.multiply(var_5128.astype('uint64'), relay.reshape(uop_5146.astype('uint64'), relay.shape_of(var_5128))) # shape=(12, 15, 6)
func_3216_call = mod.get_global_var('func_3216')
func_3217_call = mutated_mod.get_global_var('func_3217')
call_5171 = relay.TupleGetItem(func_3216_call(), 0)
call_5172 = relay.TupleGetItem(func_3217_call(), 0)
func_3332_call = mod.get_global_var('func_3332')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_5177 = relay.TupleGetItem(func_3332_call(), 0)
call_5178 = relay.TupleGetItem(func_3333_call(), 0)
func_3353_call = mod.get_global_var('func_3353')
func_3356_call = mutated_mod.get_global_var('func_3356')
var_5189 = relay.var("var_5189", dtype = "float32", shape = (330,))#candidate|5189|(330,)|var|float32
call_5188 = relay.TupleGetItem(func_3353_call(relay.reshape(var_5189.astype('float32'), [11, 2, 15])), 0)
call_5190 = relay.TupleGetItem(func_3356_call(relay.reshape(var_5189.astype('float32'), [11, 2, 15])), 0)
var_5193 = relay.var("var_5193", dtype = "uint64", shape = (12, 15, 6))#candidate|5193|(12, 15, 6)|var|uint64
bop_5194 = relay.equal(bop_5160.astype('bool'), relay.reshape(var_5193.astype('bool'), relay.shape_of(bop_5160))) # shape=(12, 15, 6)
output = relay.Tuple([call_5156,call_5171,call_5177,call_5188,var_5189,bop_5194,])
output2 = relay.Tuple([call_5157,call_5172,call_5178,call_5190,var_5189,bop_5194,])
func_5204 = relay.Function([var_5128,var_5129,var_5189,var_5193,], output)
mod['func_5204'] = func_5204
mod = relay.transform.InferType()(mod)
var_5205 = relay.var("var_5205", dtype = "int16", shape = (12, 15, 6))#candidate|5205|(12, 15, 6)|var|int16
var_5206 = relay.var("var_5206", dtype = "int16", shape = (12, 15, 6))#candidate|5206|(12, 15, 6)|var|int16
var_5207 = relay.var("var_5207", dtype = "float32", shape = (330,))#candidate|5207|(330,)|var|float32
var_5208 = relay.var("var_5208", dtype = "uint64", shape = (12, 15, 6))#candidate|5208|(12, 15, 6)|var|uint64
output = func_5204(var_5205,var_5206,var_5207,var_5208,)
func_5209 = relay.Function([var_5205,var_5206,var_5207,var_5208,], output)
mutated_mod['func_5209'] = func_5209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2600_call = mod.get_global_var('func_2600')
func_2601_call = mutated_mod.get_global_var('func_2601')
call_5235 = relay.TupleGetItem(func_2600_call(), 2)
call_5236 = relay.TupleGetItem(func_2601_call(), 2)
output = relay.Tuple([call_5235,])
output2 = relay.Tuple([call_5236,])
func_5238 = relay.Function([], output)
mod['func_5238'] = func_5238
mod = relay.transform.InferType()(mod)
output = func_5238()
func_5239 = relay.Function([], output)
mutated_mod['func_5239'] = func_5239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3169_call = mod.get_global_var('func_3169')
func_3170_call = mutated_mod.get_global_var('func_3170')
call_5322 = relay.TupleGetItem(func_3169_call(), 2)
call_5323 = relay.TupleGetItem(func_3170_call(), 2)
func_930_call = mod.get_global_var('func_930')
func_934_call = mutated_mod.get_global_var('func_934')
var_5334 = relay.var("var_5334", dtype = "float64", shape = ())#candidate|5334|()|var|float64
var_5335 = relay.var("var_5335", dtype = "uint16", shape = (2, 1))#candidate|5335|(2, 1)|var|uint16
call_5333 = relay.TupleGetItem(func_930_call(relay.reshape(var_5334.astype('float64'), []), relay.reshape(var_5335.astype('uint16'), [2, 1]), ), 1)
call_5336 = relay.TupleGetItem(func_934_call(relay.reshape(var_5334.astype('float64'), []), relay.reshape(var_5335.astype('uint16'), [2, 1]), ), 1)
func_4322_call = mod.get_global_var('func_4322')
func_4326_call = mutated_mod.get_global_var('func_4326')
const_5339 = relay.const([False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True], dtype = "bool")#candidate|5339|(819,)|const|bool
var_5340 = relay.var("var_5340", dtype = "uint16", shape = (2560,))#candidate|5340|(2560,)|var|uint16
call_5338 = relay.TupleGetItem(func_4322_call(relay.reshape(const_5339.astype('bool'), [819,]), relay.reshape(var_5340.astype('uint16'), [2560,]), ), 4)
call_5341 = relay.TupleGetItem(func_4326_call(relay.reshape(const_5339.astype('bool'), [819,]), relay.reshape(var_5340.astype('uint16'), [2560,]), ), 4)
output = relay.Tuple([call_5322,call_5333,var_5334,var_5335,call_5338,const_5339,var_5340,])
output2 = relay.Tuple([call_5323,call_5336,var_5334,var_5335,call_5341,const_5339,var_5340,])
func_5363 = relay.Function([var_5334,var_5335,var_5340,], output)
mod['func_5363'] = func_5363
mod = relay.transform.InferType()(mod)
var_5364 = relay.var("var_5364", dtype = "float64", shape = ())#candidate|5364|()|var|float64
var_5365 = relay.var("var_5365", dtype = "uint16", shape = (2, 1))#candidate|5365|(2, 1)|var|uint16
var_5366 = relay.var("var_5366", dtype = "uint16", shape = (2560,))#candidate|5366|(2560,)|var|uint16
output = func_5363(var_5364,var_5365,var_5366,)
func_5367 = relay.Function([var_5364,var_5365,var_5366,], output)
mutated_mod['func_5367'] = func_5367
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5379 = relay.var("var_5379", dtype = "uint32", shape = (2, 12, 3))#candidate|5379|(2, 12, 3)|var|uint32
var_5380 = relay.var("var_5380", dtype = "uint32", shape = (2, 12, 3))#candidate|5380|(2, 12, 3)|var|uint32
bop_5381 = relay.greater_equal(var_5379.astype('bool'), relay.reshape(var_5380.astype('bool'), relay.shape_of(var_5379))) # shape=(2, 12, 3)
func_3493_call = mod.get_global_var('func_3493')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_5386 = relay.TupleGetItem(func_3493_call(), 2)
call_5387 = relay.TupleGetItem(func_3494_call(), 2)
output = relay.Tuple([bop_5381,call_5386,])
output2 = relay.Tuple([bop_5381,call_5387,])
func_5391 = relay.Function([var_5379,var_5380,], output)
mod['func_5391'] = func_5391
mod = relay.transform.InferType()(mod)
mutated_mod['func_5391'] = func_5391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5391_call = mutated_mod.get_global_var('func_5391')
var_5393 = relay.var("var_5393", dtype = "uint32", shape = (2, 12, 3))#candidate|5393|(2, 12, 3)|var|uint32
var_5394 = relay.var("var_5394", dtype = "uint32", shape = (2, 12, 3))#candidate|5394|(2, 12, 3)|var|uint32
call_5392 = func_5391_call(var_5393,var_5394,)
output = call_5392
func_5395 = relay.Function([var_5393,var_5394,], output)
mutated_mod['func_5395'] = func_5395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5238_call = mod.get_global_var('func_5238')
func_5239_call = mutated_mod.get_global_var('func_5239')
call_5460 = relay.TupleGetItem(func_5238_call(), 0)
call_5461 = relay.TupleGetItem(func_5239_call(), 0)
func_4942_call = mod.get_global_var('func_4942')
func_4943_call = mutated_mod.get_global_var('func_4943')
call_5467 = relay.TupleGetItem(func_4942_call(), 0)
call_5468 = relay.TupleGetItem(func_4943_call(), 0)
func_810_call = mod.get_global_var('func_810')
func_815_call = mutated_mod.get_global_var('func_815')
var_5477 = relay.var("var_5477", dtype = "float64", shape = (27, 45))#candidate|5477|(27, 45)|var|float64
var_5478 = relay.var("var_5478", dtype = "uint16", shape = ())#candidate|5478|()|var|uint16
call_5476 = relay.TupleGetItem(func_810_call(relay.reshape(var_5477.astype('float64'), [9, 9, 15]), relay.reshape(var_5477.astype('float64'), [9, 9, 15]), relay.reshape(var_5478.astype('uint16'), []), ), 0)
call_5479 = relay.TupleGetItem(func_815_call(relay.reshape(var_5477.astype('float64'), [9, 9, 15]), relay.reshape(var_5477.astype('float64'), [9, 9, 15]), relay.reshape(var_5478.astype('uint16'), []), ), 0)
uop_5484 = relay.asinh(var_5477.astype('float32')) # shape=(27, 45)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_5488 = relay.TupleGetItem(func_2781_call(), 0)
call_5489 = relay.TupleGetItem(func_2782_call(), 0)
output = relay.Tuple([call_5460,call_5467,call_5476,var_5478,uop_5484,call_5488,])
output2 = relay.Tuple([call_5461,call_5468,call_5479,var_5478,uop_5484,call_5489,])
func_5493 = relay.Function([var_5477,var_5478,], output)
mod['func_5493'] = func_5493
mod = relay.transform.InferType()(mod)
mutated_mod['func_5493'] = func_5493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5493_call = mutated_mod.get_global_var('func_5493')
var_5495 = relay.var("var_5495", dtype = "float64", shape = (27, 45))#candidate|5495|(27, 45)|var|float64
var_5496 = relay.var("var_5496", dtype = "uint16", shape = ())#candidate|5496|()|var|uint16
call_5494 = func_5493_call(var_5495,var_5496,)
output = call_5494
func_5497 = relay.Function([var_5495,var_5496,], output)
mutated_mod['func_5497'] = func_5497
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5508 = relay.var("var_5508", dtype = "float64", shape = (5, 2, 15))#candidate|5508|(5, 2, 15)|var|float64
uop_5509 = relay.sigmoid(var_5508.astype('float64')) # shape=(5, 2, 15)
output = relay.Tuple([uop_5509,])
output2 = relay.Tuple([uop_5509,])
func_5511 = relay.Function([var_5508,], output)
mod['func_5511'] = func_5511
mod = relay.transform.InferType()(mod)
mutated_mod['func_5511'] = func_5511
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5512 = relay.var("var_5512", dtype = "float64", shape = (5, 2, 15))#candidate|5512|(5, 2, 15)|var|float64
func_5511_call = mutated_mod.get_global_var('func_5511')
call_5513 = func_5511_call(var_5512)
output = call_5513
func_5514 = relay.Function([var_5512], output)
mutated_mod['func_5514'] = func_5514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_5577 = relay.TupleGetItem(func_2717_call(), 0)
call_5578 = relay.TupleGetItem(func_2719_call(), 0)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
var_5632 = relay.var("var_5632", dtype = "bool", shape = (819,))#candidate|5632|(819,)|var|bool
call_5631 = relay.TupleGetItem(func_47_call(relay.reshape(var_5632.astype('bool'), [13, 9, 7])), 0)
call_5633 = relay.TupleGetItem(func_50_call(relay.reshape(var_5632.astype('bool'), [13, 9, 7])), 0)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_5637 = relay.TupleGetItem(func_2152_call(), 0)
call_5638 = relay.TupleGetItem(func_2154_call(), 0)
output = relay.Tuple([call_5577,call_5631,var_5632,call_5637,])
output2 = relay.Tuple([call_5578,call_5633,var_5632,call_5638,])
func_5643 = relay.Function([var_5632,], output)
mod['func_5643'] = func_5643
mod = relay.transform.InferType()(mod)
mutated_mod['func_5643'] = func_5643
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5644 = relay.var("var_5644", dtype = "bool", shape = (819,))#candidate|5644|(819,)|var|bool
func_5643_call = mutated_mod.get_global_var('func_5643')
call_5645 = func_5643_call(var_5644)
output = call_5645
func_5646 = relay.Function([var_5644], output)
mutated_mod['func_5646'] = func_5646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_5669 = func_2649_call()
call_5670 = func_2649_call()
func_1753_call = mod.get_global_var('func_1753')
func_1758_call = mutated_mod.get_global_var('func_1758')
var_5693 = relay.var("var_5693", dtype = "uint16", shape = (2560,))#candidate|5693|(2560,)|var|uint16
const_5694 = relay.const(5, dtype = "uint16")#candidate|5694|()|const|uint16
const_5695 = relay.const([8.819853,3.067242,0.380250,3.674435,-5.304755,-9.336871,3.713351,5.142704,6.720193,4.677852,0.507072,-0.212455,-0.813863,6.551168,6.455767,9.771709,-6.389338,-2.349565,5.376713,-5.759551,-6.720443,-0.539543,-7.012387,-5.056555,9.581385,-8.998809,3.751851,-2.927160,-9.931682,7.402956,-7.851108,4.892958,7.547459,-3.342317,0.349364,-5.520034,-4.574051,7.520092,-2.515636,-9.710596,-4.897958,-4.148159,6.570894,7.780404,-5.163279,-2.507260,1.703520,8.013802,9.483352,9.586174,9.194297,-4.702767,7.627542,-0.320941,-2.420095,8.569332,6.186976,-9.655907,-6.821213,9.984015,-7.551897,0.870426,5.587809,4.251142,8.369349,0.683941,-2.629588,-9.378262,-1.307715,-2.398229,9.969889,8.776852,8.711301,7.471770,6.558650,0.771439,-9.727615,0.705632,4.771301,4.205692,-4.020902,6.780995,-7.648527,-5.043920,-4.881772,6.306180,-1.099600,8.691149,-6.832472,-0.565431,9.472364,-4.730481,-2.792991,8.886431,-5.559032,-0.037764,2.212494,3.686214,7.059936,-5.036834,-2.097731,0.929529,-7.932862,5.467472,-5.717629,-0.670481,2.940923,8.660186,3.819356,2.034753,9.673348,-3.296768,-6.298047,4.707896,7.266296,4.324713,7.943307,-0.760334,5.915265,4.545967,4.842251,8.844676,-1.875795,7.901271,3.333480,8.916575,-3.408411,-7.417463,2.814746,9.126888,0.151824,4.827250,4.832634,7.017423,0.343003,-9.793738,-6.262550,5.209824,5.528211,-6.080800,1.899712,9.647652,9.271212,-5.494695,5.421803,9.698353,2.585281,-5.094688,0.315884,5.145290,-7.168511,4.917423,-1.885636,9.022230,8.976881,-4.219014,0.585385,7.986347,7.460357,2.977492,9.146307,-9.615402,3.942004,0.631858,-1.018576,6.674140,1.140153,6.544337,9.693806,4.082013,6.844883,-5.320330,0.435663,4.407072,2.896315], dtype = "float32")#candidate|5695|(175,)|const|float32
call_5692 = relay.TupleGetItem(func_1753_call(relay.reshape(var_5693.astype('uint16'), [16, 10, 16]), relay.reshape(const_5694.astype('uint16'), []), relay.reshape(const_5695.astype('float32'), [175, 1]), relay.reshape(call_5669.astype('uint16'), [2,]), ), 0)
call_5696 = relay.TupleGetItem(func_1758_call(relay.reshape(var_5693.astype('uint16'), [16, 10, 16]), relay.reshape(const_5694.astype('uint16'), []), relay.reshape(const_5695.astype('float32'), [175, 1]), relay.reshape(call_5669.astype('uint16'), [2,]), ), 0)
func_4422_call = mod.get_global_var('func_4422')
func_4424_call = mutated_mod.get_global_var('func_4424')
call_5699 = relay.TupleGetItem(func_4422_call(), 0)
call_5700 = relay.TupleGetItem(func_4424_call(), 0)
output = relay.Tuple([call_5669,call_5692,var_5693,const_5694,const_5695,call_5699,])
output2 = relay.Tuple([call_5670,call_5696,var_5693,const_5694,const_5695,call_5700,])
func_5704 = relay.Function([var_5693,], output)
mod['func_5704'] = func_5704
mod = relay.transform.InferType()(mod)
mutated_mod['func_5704'] = func_5704
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5705 = relay.var("var_5705", dtype = "uint16", shape = (2560,))#candidate|5705|(2560,)|var|uint16
func_5704_call = mutated_mod.get_global_var('func_5704')
call_5706 = func_5704_call(var_5705)
output = call_5706
func_5707 = relay.Function([var_5705], output)
mutated_mod['func_5707'] = func_5707
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5814 = relay.var("var_5814", dtype = "float32", shape = (6, 1))#candidate|5814|(6, 1)|var|float32
var_5815 = relay.var("var_5815", dtype = "float32", shape = (6, 1))#candidate|5815|(6, 1)|var|float32
bop_5816 = relay.power(var_5814.astype('float32'), relay.reshape(var_5815.astype('float32'), relay.shape_of(var_5814))) # shape=(6, 1)
func_2007_call = mod.get_global_var('func_2007')
func_2011_call = mutated_mod.get_global_var('func_2011')
var_5821 = relay.var("var_5821", dtype = "uint8", shape = (6, 66))#candidate|5821|(6, 66)|var|uint8
var_5822 = relay.var("var_5822", dtype = "float32", shape = (175,))#candidate|5822|(175,)|var|float32
call_5820 = relay.TupleGetItem(func_2007_call(relay.reshape(var_5821.astype('uint8'), [11, 4, 9]), relay.reshape(var_5821.astype('uint8'), [11, 4, 9]), relay.reshape(var_5822.astype('float32'), [175,]), ), 6)
call_5823 = relay.TupleGetItem(func_2011_call(relay.reshape(var_5821.astype('uint8'), [11, 4, 9]), relay.reshape(var_5821.astype('uint8'), [11, 4, 9]), relay.reshape(var_5822.astype('float32'), [175,]), ), 6)
uop_5827 = relay.log2(var_5821.astype('float64')) # shape=(6, 66)
func_258_call = mod.get_global_var('func_258')
func_262_call = mutated_mod.get_global_var('func_262')
var_5834 = relay.var("var_5834", dtype = "uint16", shape = ())#candidate|5834|()|var|uint16
const_5835 = relay.const([-5,-8,1,-6,-3,7,-1,6,3,6,6,4,2,4,-3,7,-3,4,1,4,-3,9,-9,-5,-8,10,3,-5,-6,-10,-4,-4,4,-3,-7,8,8,-5,-6,-9,-1,10,5,-9,-4,7,-10,9,10,-10,8,7,9,5], dtype = "uint16")#candidate|5835|(54,)|const|uint16
call_5833 = relay.TupleGetItem(func_258_call(relay.reshape(var_5834.astype('uint16'), []), relay.reshape(const_5835.astype('uint16'), [1, 6, 9]), ), 0)
call_5836 = relay.TupleGetItem(func_262_call(relay.reshape(var_5834.astype('uint16'), []), relay.reshape(const_5835.astype('uint16'), [1, 6, 9]), ), 0)
uop_5837 = relay.exp(uop_5827.astype('float64')) # shape=(6, 66)
uop_5845 = relay.sinh(uop_5837.astype('float32')) # shape=(6, 66)
uop_5852 = relay.asinh(uop_5845.astype('float64')) # shape=(6, 66)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_5856 = func_2649_call()
call_5857 = func_2649_call()
uop_5858 = relay.tan(uop_5852.astype('float64')) # shape=(6, 66)
bop_5866 = relay.greater_equal(uop_5858.astype('bool'), relay.reshape(uop_5837.astype('bool'), relay.shape_of(uop_5858))) # shape=(6, 66)
bop_5870 = relay.less(uop_5858.astype('bool'), relay.reshape(uop_5837.astype('bool'), relay.shape_of(uop_5858))) # shape=(6, 66)
func_5391_call = mod.get_global_var('func_5391')
func_5395_call = mutated_mod.get_global_var('func_5395')
const_5874 = relay.const([-7,-10,4,-2,-6,-4,-8,7,-5,-1,9,10,-5,-10,8,-10,6,1,-7,-3,-7,3,5,3,2,-7,-6,-7,-2,5,8,7,7,-6,-3,7,-5,-9,-2,-4,-4,5,6,2,3,-7,5,7,-2,-4,3,8,2,2,-10,8,7,-6,9,10,5,3,3,-2,4,-1,7,-4,-9,-5,-3,2], dtype = "uint32")#candidate|5874|(72,)|const|uint32
call_5873 = relay.TupleGetItem(func_5391_call(relay.reshape(const_5874.astype('uint32'), [2, 12, 3]), relay.reshape(const_5874.astype('uint32'), [2, 12, 3]), ), 0)
call_5875 = relay.TupleGetItem(func_5395_call(relay.reshape(const_5874.astype('uint32'), [2, 12, 3]), relay.reshape(const_5874.astype('uint32'), [2, 12, 3]), ), 0)
uop_5882 = relay.atanh(uop_5845.astype('float64')) # shape=(6, 66)
const_5885 = relay.const([[8.350557,1.511636,-2.960580,3.874795,6.658179,3.690277,3.768602,5.907281,7.897215,-6.992983,2.291904,-6.977096,-9.210163,-9.553924,1.749429,4.434299,-2.493753,-7.783148,4.691527,8.847308,-2.120497,-4.158334,1.132477,1.027335,3.916425,4.857323,4.102333,-6.227581,-4.794552,-4.326996,-0.350801,2.877866,-7.269497,-2.000102,9.627228,-0.575176,-2.773856,0.692691,-8.284612,-8.805302,-0.331945,-1.523851,7.296189,9.461996,1.032738,9.049644,5.785644,-0.926027,-0.416083,-9.548132,7.678896,0.541465,7.688792,4.441997,6.600335,6.108846,0.479588,-4.022154,-5.244153,4.292880,6.814117,-8.186890,3.646178,-0.280458,9.768782,0.828594],[1.215752,-9.578615,4.565666,-8.490005,1.512256,-1.901880,3.619412,0.567920,6.372611,9.326153,0.976422,2.449650,-7.889682,-4.954288,-6.681474,-5.528383,4.471000,-0.188679,0.523461,3.782122,-8.443277,5.742034,-0.555314,-3.014557,5.513750,-6.551628,6.310175,0.911090,3.726649,8.473208,6.544132,9.544175,-8.724279,9.373200,-1.907891,-3.328729,6.379337,-0.201546,-3.831410,1.494220,-7.381079,-6.891981,4.872908,-8.142290,5.282211,9.451275,4.934480,9.692886,-1.301216,1.789302,-7.580943,-2.130233,-6.788344,8.015022,9.238545,-8.773639,1.535258,8.468506,1.426145,9.090167,0.540696,1.448715,-4.179866,-4.527234,-7.737163,4.850839],[6.574638,-2.613957,5.868572,-5.615887,-9.358916,-4.500237,9.376020,-7.734144,5.301911,5.260725,-6.773079,-4.735809,-3.655018,-1.044392,-6.275765,2.565220,4.997997,0.334782,5.756307,0.501421,4.122126,1.374781,6.430517,1.159001,-4.520600,4.526998,0.838409,9.878270,-1.907422,-5.875475,6.294567,-0.942423,1.540367,5.619364,2.767192,-7.371118,6.096713,4.835403,-9.706237,6.612655,7.966762,5.416814,-6.979237,-9.133458,-1.455948,-5.279777,-0.310154,-4.691860,-0.473694,1.710550,-0.892328,-0.515239,8.897124,-7.915336,-4.016280,-8.446449,-8.238435,4.501327,-5.028812,2.210276,-5.816758,7.692028,-2.163673,2.123822,5.770799,-3.805096],[-4.278614,6.281764,-5.827303,7.278219,-0.964491,6.187896,-5.648065,4.566210,-2.319729,9.775664,-9.719363,-4.012903,6.452434,-3.620173,-9.123856,-5.612251,5.971853,-6.443117,-3.173885,3.445090,-0.884821,5.480515,7.218812,5.040258,-1.229039,-5.744736,6.641508,3.243605,-1.786679,-3.901982,9.840497,-9.695787,-0.818115,-4.492652,-0.360679,5.641461,-2.727802,6.873253,-2.254325,-7.284473,-1.408154,9.585561,3.608342,-9.134988,-6.197150,-2.770850,1.503229,3.058340,6.100970,-4.024219,5.276719,-4.156210,3.206675,1.345678,1.069676,-6.629307,-7.983353,1.947926,-4.093326,-1.409975,-5.863399,-4.992056,0.421225,-8.678654,-5.192420,-4.999554],[-2.688106,2.692359,6.798970,2.812718,-3.594461,-5.240313,-1.379529,-6.136252,0.535924,0.333882,5.291396,6.425983,0.364202,-0.363565,8.063490,7.318317,6.405026,1.393288,2.143036,1.669586,-3.211568,0.745744,-7.589949,6.026915,-3.863681,0.933533,7.989302,-3.594541,-9.616070,-5.569650,9.809598,-7.833221,-5.727170,6.025963,-0.034338,-2.900787,-6.721164,8.260141,2.627853,-6.107393,-0.217927,-9.672776,6.057708,-9.603360,8.509901,7.216849,2.679090,6.248477,9.855475,1.291635,-2.411961,-3.833337,2.879691,9.483343,-3.408391,-5.594207,3.256070,-2.040236,9.903163,7.497388,3.287639,-1.973238,-8.186714,4.463430,-8.223029,6.819358],[-0.067675,-0.149604,-9.332459,-3.602131,9.389072,7.996524,7.455430,5.581005,-6.019862,8.795636,0.538508,-7.718143,-2.504797,6.165093,6.760302,8.641992,-8.237467,2.105374,8.471011,-5.646335,5.713932,4.378003,4.757515,4.087481,5.034891,-7.520728,-6.891703,-3.129710,-2.580108,-2.160704,5.793804,8.520283,4.717530,-2.685775,-2.507720,7.454424,-3.884008,8.801967,-9.487920,8.433779,4.253977,-4.413678,9.923380,-3.062786,4.468529,2.307354,-2.052106,-7.462777,2.585451,-9.755193,8.682164,4.323077,4.915864,-1.457083,-1.762253,2.939837,2.738177,7.063616,4.774213,-1.368045,-0.392889,2.340528,-8.804316,-3.473964,-3.555887,1.869681]], dtype = "float64")#candidate|5885|(6, 66)|const|float64
bop_5886 = relay.maximum(uop_5837.astype('int8'), relay.reshape(const_5885.astype('int8'), relay.shape_of(uop_5837))) # shape=(6, 66)
const_5889 = relay.const([[0.778942,4.982453,0.397349,1.210332,5.525401,4.408381,-9.582339,-6.700797,5.382247,-5.027469,-0.770319,-9.860242,5.895413,8.522121,-7.852194,-4.955715,3.737340,0.882199,3.435669,3.591359,-6.150535,6.658903,-2.250907,6.329944,3.292486,-3.984618,2.378547,-3.624618,-8.545569,-5.632320,-3.549716,4.635735,1.437717,1.690436,6.927933,9.736112,5.773963,-5.874838,-6.269989,7.239733,-8.812674,-6.431364,5.405395,-3.748413,-8.100054,-0.543985,9.278370,-6.320220,1.469094,-1.152631,-6.094276,-6.230832,-8.882879,2.522505,-9.443366,-3.207682,-7.722454,7.503475,7.509024,1.837762,-1.255295,-1.934158,5.186176,-8.804686,-4.177194,-7.598002],[-9.867609,-9.995394,2.988854,-8.586592,8.541145,-8.099719,6.886304,1.129485,-6.743603,-5.612462,-5.277507,-5.569841,8.754356,-1.854019,1.461671,-9.472220,-2.662489,-6.111974,-5.243102,1.603323,7.081065,9.079542,9.878921,9.783478,9.934595,1.673024,6.862559,-4.049414,-7.537421,-3.245746,9.073780,-3.199361,-5.617806,4.357008,0.725512,-3.787961,7.669726,8.762330,-4.572175,-4.848131,-5.859950,6.458497,9.078984,-7.645503,0.719161,-6.143446,9.479960,-3.807381,2.260607,-9.569450,-9.454910,-0.926609,-2.708536,6.015281,-9.873697,-5.606368,8.685851,-7.050190,1.449944,-1.508454,-8.608742,9.989186,8.056879,5.371310,-2.549699,9.690892],[-3.609433,-2.649454,0.773781,3.167938,3.232950,-1.461705,6.575150,9.374612,9.691614,4.251307,-2.454546,2.689112,-2.302221,0.972389,-9.500763,-1.382064,-4.149147,8.025755,-1.061994,1.456280,5.667981,-0.182042,2.446826,3.309555,0.037270,-6.202778,-7.956610,-5.144969,-3.816081,6.781324,-3.799259,0.199827,-2.023444,7.308236,8.668938,-4.341695,-9.104149,8.871537,-5.897487,1.899981,-2.334614,-8.487658,7.151284,4.755023,-3.762439,9.920676,-2.565360,9.938283,5.795607,5.032887,3.472599,4.758717,-0.064605,1.183801,-5.217094,3.689078,-5.718210,8.899457,-5.281685,5.702977,0.499529,3.956133,0.878408,-0.538887,3.481454,2.366725],[4.984471,6.208957,-1.022513,-7.723702,6.965426,9.895527,5.806165,9.842437,2.079092,-8.294056,9.640478,3.038072,-9.121423,-7.540942,4.227450,9.405027,-4.910945,9.829001,3.469913,5.177975,0.743996,2.462103,4.676224,-0.062012,0.456072,2.985632,-4.193356,-2.412326,-0.332272,4.611215,-1.524861,-1.376789,3.993323,3.019582,-6.287230,1.322220,0.328042,-5.661383,5.620584,-6.000605,-0.976617,-3.720907,-7.753166,5.471548,7.889348,-0.630630,0.664015,-8.114866,-5.454127,-2.543256,4.535388,-3.920104,-9.657849,9.805606,9.561273,-4.511403,-7.871147,7.063014,9.706641,6.736085,1.235624,9.661430,2.390234,7.771828,0.977762,-4.677657],[0.265709,-7.790005,2.496871,7.714118,4.969633,-9.081279,-5.634354,-3.687269,1.986701,-7.360437,7.725548,8.544096,-6.570092,9.545205,-4.190773,-2.797876,-1.034939,4.762211,-9.708235,3.385113,3.105188,9.172271,1.447896,1.895611,-6.106331,2.226229,0.612630,-4.829188,7.279222,-4.974726,9.549019,7.930264,2.340509,5.624617,8.343470,0.987116,2.726160,0.632535,-9.750222,1.294088,-8.364816,-3.609696,1.157016,7.016041,-5.508629,4.725831,-0.564135,-3.115244,6.908408,-5.434476,-9.864601,1.789679,-6.972383,-6.862203,-6.130618,7.847150,-5.877918,-1.127018,-0.781554,-0.335932,0.240239,-1.356243,-6.695799,8.866078,5.192511,-1.804307],[3.657069,8.217444,-5.285983,-0.742078,6.437744,-8.955497,-7.057200,7.568354,-6.178942,9.818848,3.056341,-8.176176,-4.179087,-8.365544,6.480056,4.273735,-2.717555,-3.016041,-7.021247,0.599217,1.931877,7.619615,7.162966,-1.506828,-4.678553,1.855992,-2.574110,1.995653,-3.172265,-4.741869,2.030765,-9.711632,-4.607120,-7.842959,-8.543932,-7.184750,9.456755,9.424321,-3.104763,6.849117,2.355548,6.876758,-7.017304,5.358641,-0.671989,-5.203556,8.509103,3.210903,5.861530,9.762375,-7.497573,8.891320,1.814191,-1.632640,9.757045,9.474188,-9.937576,-8.302568,2.616482,8.752784,1.091749,9.299621,0.716227,-9.291723,1.802554,-8.879281]], dtype = "float64")#candidate|5889|(6, 66)|const|float64
bop_5890 = relay.floor_divide(uop_5858.astype('float64'), relay.reshape(const_5889.astype('float64'), relay.shape_of(uop_5858))) # shape=(6, 66)
output = relay.Tuple([bop_5816,call_5820,var_5822,call_5833,var_5834,const_5835,call_5856,bop_5866,bop_5870,call_5873,const_5874,uop_5882,bop_5886,bop_5890,])
output2 = relay.Tuple([bop_5816,call_5823,var_5822,call_5836,var_5834,const_5835,call_5857,bop_5866,bop_5870,call_5875,const_5874,uop_5882,bop_5886,bop_5890,])
func_5893 = relay.Function([var_5814,var_5815,var_5821,var_5822,var_5834,], output)
mod['func_5893'] = func_5893
mod = relay.transform.InferType()(mod)
var_5894 = relay.var("var_5894", dtype = "float32", shape = (6, 1))#candidate|5894|(6, 1)|var|float32
var_5895 = relay.var("var_5895", dtype = "float32", shape = (6, 1))#candidate|5895|(6, 1)|var|float32
var_5896 = relay.var("var_5896", dtype = "uint8", shape = (6, 66))#candidate|5896|(6, 66)|var|uint8
var_5897 = relay.var("var_5897", dtype = "float32", shape = (175,))#candidate|5897|(175,)|var|float32
var_5898 = relay.var("var_5898", dtype = "uint16", shape = ())#candidate|5898|()|var|uint16
output = func_5893(var_5894,var_5895,var_5896,var_5897,var_5898,)
func_5899 = relay.Function([var_5894,var_5895,var_5896,var_5897,var_5898,], output)
mutated_mod['func_5899'] = func_5899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_5947 = func_3060_call()
call_5948 = func_3060_call()
output = call_5947
output2 = call_5948
func_5982 = relay.Function([], output)
mod['func_5982'] = func_5982
mod = relay.transform.InferType()(mod)
output = func_5982()
func_5983 = relay.Function([], output)
mutated_mod['func_5983'] = func_5983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_5997 = relay.TupleGetItem(func_2717_call(), 0)
call_5998 = relay.TupleGetItem(func_2719_call(), 0)
output = call_5997
output2 = call_5998
func_6009 = relay.Function([], output)
mod['func_6009'] = func_6009
mod = relay.transform.InferType()(mod)
output = func_6009()
func_6010 = relay.Function([], output)
mutated_mod['func_6010'] = func_6010
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6023 = relay.const([[[-7,-4,6],[-7,4,-3],[10,8,-9],[-8,-5,4],[9,-2,-4],[6,-8,10],[-8,2,-2],[4,8,-5],[10,-10,8],[10,2,2],[-5,-9,-7],[-10,5,6],[7,-9,-3],[-10,8,9]],[[5,-7,3],[5,6,-2],[3,9,-4],[-5,-6,-3],[-9,-3,4],[6,3,-10],[-3,-4,-1],[3,8,1],[-8,2,3],[4,-10,-2],[10,6,1],[8,1,4],[-8,-5,2],[8,-6,-5]],[[-6,2,5],[8,2,-9],[-10,-9,-8],[-2,-4,1],[-6,-6,-9],[-1,2,-9],[-7,-4,-3],[-4,-7,3],[-7,-2,-5],[-7,-3,-3],[-5,-5,10],[-6,5,6],[1,10,-2],[-5,-1,2]],[[-9,-8,3],[5,8,5],[-6,-2,10],[-8,9,-9],[4,-2,1],[2,4,-2],[-1,-4,-7],[-4,-1,3],[-8,2,-8],[8,7,6],[5,-9,7],[-5,8,-7],[10,9,2],[3,-2,5]],[[8,-3,-7],[-2,-8,3],[-2,-4,-10],[9,-4,5],[10,-4,-5],[-4,6,7],[-8,-8,-1],[4,1,-8],[-8,-5,5],[8,8,-10],[5,-5,1],[4,2,-8],[3,8,9],[-7,3,1]],[[9,-3,-3],[1,7,9],[-9,-1,-5],[6,10,-5],[10,-8,-1],[-10,8,9],[-8,-9,6],[5,1,8],[5,-5,8],[6,2,-2],[2,-5,-9],[4,-7,-2],[-1,8,-1],[7,10,2]]], dtype = "uint64")#candidate|6023|(6, 14, 3)|const|uint64
const_6024 = relay.const([[[7,6,-10],[5,-6,3],[1,-9,1],[-6,-2,8],[-6,-9,6],[-3,-4,7],[1,9,-8],[-9,-10,-5],[2,8,10],[-2,-3,-5],[8,3,9],[8,-1,-7],[-7,1,-7],[-8,8,4]],[[6,-4,8],[-7,7,8],[2,-4,-1],[4,-7,7],[1,-4,-5],[-7,-4,-9],[10,9,-8],[1,-3,4],[8,-3,-3],[1,-8,-3],[3,4,-2],[-10,-9,-8],[-5,8,8],[1,-8,-2]],[[-7,-4,-8],[-7,-8,-10],[2,-1,-8],[9,-9,-1],[-6,2,-1],[4,-9,-2],[-5,10,10],[4,-2,4],[-7,5,-9],[-5,-1,9],[-3,-9,-3],[-1,-1,-4],[3,-2,4],[-6,10,-6]],[[-8,-6,-10],[-2,-9,-5],[-3,5,-7],[3,-6,4],[-5,-2,2],[6,1,-10],[6,-3,-4],[-1,7,8],[-2,4,8],[-9,-8,7],[-9,9,-2],[10,-2,7],[3,10,-2],[4,9,-4]],[[-7,7,-4],[-5,-7,4],[7,9,6],[5,4,1],[-4,-9,-2],[10,-6,7],[3,-4,8],[2,-1,-5],[9,-8,7],[-8,-4,-6],[10,8,-6],[7,-6,-2],[6,-2,-8],[-5,8,9]],[[-3,-8,6],[5,-3,5],[7,1,-2],[10,10,6],[-8,5,4],[-3,3,-6],[-7,-8,-6],[-2,-4,8],[7,-3,-9],[-4,-9,5],[3,10,9],[-6,9,-1],[-6,9,7],[5,5,-2]]], dtype = "uint64")#candidate|6024|(6, 14, 3)|const|uint64
bop_6025 = relay.multiply(const_6023.astype('uint64'), relay.reshape(const_6024.astype('uint64'), relay.shape_of(const_6023))) # shape=(6, 14, 3)
func_4648_call = mod.get_global_var('func_4648')
func_4650_call = mutated_mod.get_global_var('func_4650')
call_6028 = relay.TupleGetItem(func_4648_call(), 0)
call_6029 = relay.TupleGetItem(func_4650_call(), 0)
output = relay.Tuple([bop_6025,call_6028,])
output2 = relay.Tuple([bop_6025,call_6029,])
func_6038 = relay.Function([], output)
mod['func_6038'] = func_6038
mod = relay.transform.InferType()(mod)
output = func_6038()
func_6039 = relay.Function([], output)
mutated_mod['func_6039'] = func_6039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3538_call = mod.get_global_var('func_3538')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_6042 = func_3538_call()
call_6043 = func_3538_call()
output = call_6042
output2 = call_6043
func_6056 = relay.Function([], output)
mod['func_6056'] = func_6056
mod = relay.transform.InferType()(mod)
mutated_mod['func_6056'] = func_6056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6056_call = mutated_mod.get_global_var('func_6056')
call_6057 = func_6056_call()
output = call_6057
func_6058 = relay.Function([], output)
mutated_mod['func_6058'] = func_6058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_6180 = relay.TupleGetItem(func_2152_call(), 0)
call_6181 = relay.TupleGetItem(func_2154_call(), 0)
func_4968_call = mod.get_global_var('func_4968')
func_4969_call = mutated_mod.get_global_var('func_4969')
call_6189 = func_4968_call()
call_6190 = func_4968_call()
func_1200_call = mod.get_global_var('func_1200')
func_1204_call = mutated_mod.get_global_var('func_1204')
const_6192 = relay.const([2.953233,-6.070451,0.618512,3.850944,9.599104,-0.327839,-6.869969,2.691947,-0.981445,9.501776,3.001575,9.895719,-6.587047,-0.415104,-0.894737,3.331568,8.488847,-6.348585,8.432718,-4.886506,-9.445705,5.432641,2.404159,4.723069,-0.732139,0.179881,-2.006599,3.327501,5.265518,-6.168023,8.611023,2.156281,5.677825,1.801179,2.051595,0.820898,-6.320951,0.270551,-8.527683,4.320876,1.013838,-6.474608,0.735790,-1.183407,8.515664,3.547244,4.883251,7.624974,-7.574266,0.404218,6.439480,-9.490691,9.011901,2.692315,-8.019845,3.253030,1.715527,-0.039792,7.197088,-2.836443,5.113941,7.360582,-6.015550,-2.984418,6.051350,8.977187,-6.181906,-4.434890,2.447692,8.561749,6.883248,2.722691,-6.483033,4.218324,9.271916,3.743705,5.170806,3.990852,6.286581,1.550026,7.152461,1.481496,-4.965505,5.430144,-9.564465,1.678784,8.241850,-5.657766,-3.226207,-2.435640,5.668845,0.680265,-2.458857,6.619272,-5.434601,3.800190,2.968333,3.580708,-3.657751,4.524015,-7.294024,-0.572726,1.133109,9.297734,6.878119,1.026965,7.671113,8.343990,6.572074,-2.402065,7.938114,7.066719,-5.872547,-2.699203,-9.250588,4.096350,4.994298,-6.221306,6.835081,-9.077018,7.011554,9.428677,-4.954773,5.552140,5.587495,3.009834,5.538285,8.105082,-2.422167,-4.691176,3.806518,5.323651,-1.193443,-1.572102,9.265050,-6.849508,-6.082250,-4.559643,-9.984606,6.881656,8.220253,3.009481,2.703101,-5.839820,-9.192440,-1.286626,4.527939,-9.702419,-8.539353,0.186306,-1.335436,-6.687535,7.445913,0.590496,-6.453269,-4.030667,-2.383490,-6.977755,-0.420806,6.030337,-4.059669,2.301657,5.885365,9.782941,-2.620225,8.142298,-4.072965,0.372077,-8.102946,6.282647,5.995532,-7.612144,9.117356,-3.976203,-5.276992,8.808202,1.359473,-1.823919,-1.504874,-6.806390,-2.896436,6.612477,-1.930456,-9.868283,-7.407007,5.242087,5.855925,3.575038,1.382436,4.587594,8.671042,-9.445232,3.105917,1.475557,-2.711316,-3.605307,4.034163,2.071464,-8.285130,1.842582,5.683692,5.109158,-3.342407,-0.213286,-9.857951,3.622650,-7.740156,-0.593402,-6.439191,9.643049,-8.618603,4.477620,-8.886237,5.857135,8.483677,1.965004,1.234154,8.601730,0.652973,2.713435,2.767289,3.982482,-9.242394,7.338404,5.240432,3.099850,-4.656660,3.894358,2.903458,-2.600141,6.111346,-0.806582,-2.236432,8.981618,0.223811,9.255127,5.118899,-1.385966,-0.315852,7.735779,-7.520373,8.357830,7.428988,3.717291,3.178006,9.171011,9.559828,-1.861614,-3.585136,8.211375,-3.982911,-5.314047,9.783574,-6.909348,8.070239,7.276084,-9.175854,-7.531351,-3.298149,2.089010,8.177404,-5.589911,-5.461080,-7.798450,-8.765088,-5.066090,-0.199641,0.358718,9.821913,-0.510760,2.800467,-1.887214,-6.270138,5.486154,5.402492,3.647294,-6.376968,7.620704,-5.279878,6.108999,-6.383294,3.353222,-6.171334,-8.918142,-8.351635,-6.855580,8.067706,-9.905310,-1.990108,-2.985499,-1.405064,-6.855901,6.265337,2.274603,-3.495657,6.448063,-7.282088,3.867170,7.741545,-0.561903,-4.644972,1.853886,5.946844,-5.411629,8.305581,8.341816,-3.875185,-9.138976,-8.208749,8.268412,-6.260853,1.623161,1.455629,-9.779718,-9.561542,5.875672,8.654556,-2.062535,-3.096406,-5.202572,1.345695,6.599214,-5.403319,-7.091943,0.057855,9.985395,-5.475137,-3.624615,1.158314,-3.669975,4.909426,9.778058,-4.936757,8.128528,-6.285161,-4.907919,-0.903639,2.228907,-1.153373,1.863785,5.766559,0.815121,9.072338,5.730058,-6.779910,-1.205199,3.291994,2.512754,-2.936230,-8.517694,-4.391804,-8.489342,-0.036876,9.529236,3.902338,-8.612413,5.519297,-9.473379,1.890582,-9.621900,2.732224,7.067675,-9.091668,-4.681689,-1.890363,5.872768,-4.624993,2.867159,4.983850,9.240840,4.815048,4.613411,6.144568,9.799776,4.297045,4.008777,-7.365193,-7.595801,5.652351,4.015452,1.317736,-9.012838,4.842378,5.897769,2.939463,6.918558,-8.321069,4.801010,9.092816,5.866953,-8.202686,7.407781,8.584821,1.634023,7.701717,-9.331920,9.121712,-0.606417,-9.254992,8.100899,-5.536370,-3.494720,2.352454,-1.836477,-5.146899,-8.894249,-9.384891,-5.525661,0.921169,-8.191762,-5.476302,9.036996,-0.922926,-8.341477,8.682065,-9.611317,1.843355,5.937797,-1.362768,5.736493,6.956957,-1.663735,8.004553,4.333708,-3.330024,9.058344,9.123806,6.472795,-6.483962,-1.054413,1.050968,5.105398,-3.240670,-0.458909,9.682665,8.300645,7.233339,-7.881557,-6.356042,3.698247,-9.950792,-3.734281,7.746338,1.055016,0.589871,-3.802029,-4.505486,3.242451,-0.851107,3.961237,8.821073,-9.441034,-7.636723,-8.798000,-9.739258,-0.995708,-5.290731,-7.669006,-2.648943,-5.858684,-9.464920,-6.646073,-4.471276,4.052098,6.349081,-6.804586,5.145030,0.863021,-8.418218,6.666195,0.631895,3.648863,-8.788678,-1.116211,4.817243,-5.522102,5.594086,-6.499500,6.269370,-1.173384,-5.516582,7.625108,8.041649,-6.313393,-5.109296,-9.351210,9.523467,-3.653475,-3.447810,-1.918588,3.836296,0.991390,7.726091,-7.421376,9.536970,-9.635758,-2.056626,4.969590,-0.826131,0.445788,3.704343,1.885076,7.536226,-0.137270,-2.963367,6.955966,-9.474669,-7.594186,-3.847678,-2.513018,0.757198,4.858318,-7.453309,1.339014,-0.456009,-0.785674,-5.054280,-5.943886,1.000684,8.378023,1.491133,9.649677,9.953838,-0.560250,-9.967224,6.183332,9.736344,9.677711,-6.295292,-1.891699,4.934200,-6.513194,-3.929800,3.547771,-2.537460,2.034890,1.295317,7.677862,-5.123711,-0.911398,-9.656569,-9.332392,1.265436,8.592173,-6.365035,-8.864962,-6.506749,-9.890456,-9.401500,-6.147012,-8.111531,-3.201822,-4.456225,6.175396,8.742713,-9.431064,9.185792,6.562724,-6.869175,-6.721295,7.731491,8.729763,-8.219370,-5.405058,2.709990,0.631710,7.513600,-6.413123,5.613721,-5.663401,4.627561,-7.546696,-9.704338,0.675971,-1.131603,4.197119,1.846339,-6.583146,-9.676776,-9.073408,0.197637,-9.972121,7.917192,0.630523,-1.500892,-7.928014,-3.918702,-0.315429,-2.184175,0.782933,-2.540734,-6.539198,1.487119,5.868019,-4.781984,-2.533172,1.382008,-1.033070,9.910673,3.346017,6.899144,0.674824,-7.921818,-5.665567,-0.577364,3.610819,6.536562,-0.354228,-9.216209,-4.265736,9.726676,4.462951,2.056964,0.975635,6.924257,-0.570232,-6.966201,-1.657056,-7.900458,-9.403884,-6.381437,7.291252,1.636070,9.128464,2.410764,-0.416809,-9.827659,9.105488,8.221399,-9.779183,3.272956,-0.222513,-7.270218,-8.716098,3.392662,6.173515,-9.843467,1.007623,-1.099896,-7.804903,7.068136,-4.313120,-2.628819,9.118263,9.278281,-2.996632,1.048745,-2.927665,3.840168,-1.761432,8.943774,-5.033582,-9.226882,-2.605448,-4.178733,-8.300361,3.617805,0.716689,-4.260896,-2.894373,-1.865378,-3.452989,6.659996,-5.646946,5.065814,3.337616,-9.857211,-4.126580,-5.099100,-3.512211,5.932835,-3.934018,9.690488,-4.122484,-4.163624,8.618400,2.536642,-9.590575,0.484509,7.643581,5.231395,0.556520,6.244226,-0.476553,-6.174251,-7.715375,5.652334,8.685828,3.835118,-5.715972,-8.066837,-6.731732,2.637212,-2.972259,5.945533,7.196770,-4.760289,8.915054,7.746759,5.093699,-0.847825,7.395595,-6.828307,-5.746170,2.112203,-9.836075,6.400915,6.750863,6.218354,7.101394,-3.301323,-9.343363,7.806621,-4.363204,0.228877,3.345262,3.858725,-2.456254,6.253965,3.037575,4.512795,-2.657208,7.929402,-3.252480,0.552757,0.196177,-0.606722,-0.129360,7.743996,-6.728455,4.599044,-9.041659,5.657661,-9.838860,-1.087250,9.198513,2.757875,-3.839813,2.213446,-1.941344,-9.972476,-6.264568,3.507992,-2.552361,4.477483,7.014666,-9.463675,-3.158294,-4.030874,-2.475515,-3.225800,8.078490,3.266176,-0.959089,-4.591200,3.877575,7.080651,5.483067,0.279976,6.130561,0.682749,5.461816,8.663102,8.203723,-9.371204,-1.369458,2.073040,5.893902,9.238162,7.778779,-1.401547,-2.908729,5.654166,-5.899367,5.359500,1.801546,-0.542125,4.417109,-0.322272,-8.207104,-5.864211,-4.029815,-4.212227,6.324192,5.934499,3.713655,4.979406,0.626862,6.572644,4.263721,-3.208875,4.076946,5.184521,-0.234768,9.160667,7.363802,6.670682,9.563573,6.033772,1.376995,-9.607256,-1.009589,-3.404542,-2.050982,4.520691,-7.478814,-2.564757,-7.611708,-1.315235,-1.356695,7.595153,-7.745111,7.288444,-9.070330,-9.031610,8.765211,-2.459853,-3.615461,-9.491909,4.656166,9.798668,0.732567,8.667332,1.247508,-6.851808,-4.223171,0.027954,-1.645140,-6.926251,3.068305,-6.767259,2.975319,-4.702408,7.402446,-3.940687,-7.564701,-1.333666,-6.004732,-6.320101,-3.257427,0.910634,-4.239071,2.232806,4.976716,-8.464246,-9.803069,3.542028,1.991802,7.012216,-1.715954,3.168667,4.382999,-2.103071,-1.054274,-0.525585,6.057670,7.254155,-7.872994,-2.045693,-6.322883,5.633822,7.862056,8.138015,-3.933829,9.857908,-6.252608,-4.824978,1.325083,5.055234,3.959511,-6.677842,1.657239,-7.589786,-2.204564,0.491059,3.005381,8.473200,-4.999306,-2.769570,4.920477,6.457737,-1.288586,-2.583674,8.659113,3.902504,6.068576,2.557407,1.872951,-2.783195,5.845405,9.105136,-0.504792,5.650620,6.978792,-3.696833,-7.712181,-2.327590,6.357080,-6.915149,1.881128,9.590193,8.531929,2.222427,-7.739812,-9.384939,-6.264771,4.881936,-0.878959,6.482597,-9.059197,-7.178436,4.121038,4.112331,9.124848,6.554448,-8.075286,8.428607,-9.927866,-7.878523,1.992885,-5.516518,-5.331355,-4.950536,-1.864469,-6.836893,4.015564,2.914775,-9.439331,0.160344,-7.858173,-5.383179,5.044276,-4.228141,-6.862675,4.983467,6.224727,5.179805,7.761067,-7.747841,0.823564,-2.337750,-1.428562,-1.347346,-6.126296,-1.152959,-5.319933,9.740550,4.377224,9.610398,0.952528,0.158729,-9.540447,-8.359301,-7.891475,-7.283259,-6.493777,3.523055,-8.787983,9.986195,5.138027,-1.304727,-7.898554,-6.562451,6.704122,6.931435,-3.905430,-3.636580,-6.940768,-4.605516,4.240463,-7.497275,9.236386,-1.907143,9.914251,-0.924774,-4.774288,7.326968,1.010207,-4.359103,4.579312,2.815611,-9.124396,2.640995,-3.694795,0.552099,-3.797945,7.599751,1.383426,3.900602,4.357472,-3.104833,-0.621026,-9.352793,5.306258,3.881690,1.589774,-2.818956,-7.500696,-3.622703,4.731513,-1.111216,7.270078,6.578650,-3.006696,-3.070078,-8.167991,7.432199,-1.238729,-1.442008,-9.701368,-9.011389,-6.148963,0.201942,-0.806625,-4.257806,1.206010,3.966955,-1.474901,-0.496586,-3.998035,0.523065,3.645696,0.740195,-8.376021,0.922053,0.522968,-6.970524,-5.782986,-9.671778,7.113468,-3.971964,-1.161245,-6.934753,-3.676125,7.843111,5.465610,7.089211,6.066012,-5.798180,0.840489,-3.469795,2.102136,-9.040682,-9.429732,9.917299,4.807083,-5.396318,6.539408,9.726604,2.180565,-4.113359,3.221094,5.641575,6.677469,-0.443047,4.690067,9.034945,-0.069602,-2.122181,3.188282,-5.245999,6.842349,-2.774088,2.425226,-4.098592,-5.675218,5.799289,0.136337,-3.539461,-2.898430,2.931101,6.251775,9.412968,-3.292508,-3.801473,4.318742,5.428015,1.136159,5.686026,7.194411,-0.663419,8.127405,8.428767,-3.285316,1.575638,-9.603088,4.022958,5.075065,2.820519,-3.450321,3.528570,5.925142,9.801756,-7.183875,5.528250,-4.015496,7.649220,-1.650573,-1.701484,-6.655924,7.573180,-1.802749,-9.349201,1.002241,-7.174235,7.398610,0.182955,-9.309062,-9.287528,-7.719364,-8.132403,7.814892,-5.038436,-2.259439,-5.912765,-1.559604,5.971504,-7.585381,-3.870365,-1.880349,-2.886386,8.606262,-1.570676,-8.835486,-1.748173,-8.286079,1.834285,8.060331,4.037236,8.773386,-5.152012,-1.149288,-5.896555,-4.343717,-9.694709,9.665322,-0.288068,2.781542,-1.621545,1.834780,-7.768258,6.238964,3.408016,3.450921,-1.906106,0.737321,-5.424255,8.423066,-0.152797,7.308575,-5.908983,8.718590,8.396848,3.419450,-6.204328,6.675333,-3.048210,9.000659,9.273581,6.930921,7.131699,-6.744922,-9.710812,-2.185387,9.991843,2.574826,4.722067,8.856513,3.102978,-9.966607,2.530629,-5.133290,7.841833,-5.774997,-3.874955,-3.939724,-2.339577,0.554618,-0.509271,1.486977,-2.377609,9.154821,-3.904383,-5.258010,6.294572,0.763830,-9.216581,8.313322,0.769721,-0.224595,1.717805,7.675331,-6.549684,-9.304835,2.008121,-0.947814,-0.455670,5.484023,-9.368383,5.955154,-8.275529,2.668056,-3.708927,-6.945318,-4.169827,-9.711274,-1.725298,7.583324,-0.502608,8.771454,2.669163,0.844922,-0.037646,-2.872454,3.396415,-0.509357,5.405365,-4.909992,-9.977367,3.929159,-5.708907,-9.611071,-2.441073,0.866176,4.994172,-5.683562,-0.605275,4.024403,-1.245556,-2.450285,2.155058,0.335955,-9.742870,-7.014859,6.218009,3.845267,2.399512,-0.791464,7.028315,9.721341,-3.832555,4.513631,6.152391,1.797047,1.359867,9.223499,6.113695,5.056294,3.124620,-7.607971,7.814819,-7.321966,-7.076569,-9.578612,-3.379009,-2.973424,7.444629,0.903604,-7.948257,-6.988535,-6.635330,-6.545211,2.123035,5.917119,-8.151840,3.076572,3.174668,-0.321586,-0.042277,5.389652,-8.472211,8.014097,-7.173011,0.277633,-4.628279,-1.964187,4.559922,-7.641900,-9.588975,9.697392,6.626880,-8.997757,-4.325736,-6.327926,-1.249586,3.613194,-4.504963,-2.235343,-0.103523,7.287480,-0.238018,4.456145,0.147542,-0.950944,-6.093016,-1.546496,-1.938361,-4.610464,4.107537,1.369891,7.440746,6.399168,1.471671,-7.714989,0.885868,-0.985267,8.765645,8.788135,1.162660,-4.703502,-6.215917,-5.175045,0.610202,0.966720,7.776034,-3.855205,-5.262776,-6.058348,-2.559122,5.018961,4.286374,4.082505,9.688234,4.630826,-4.956311,-2.625026,-3.624320,8.988729,-0.555460,-9.488754,7.876764,-5.711179,-2.462401,5.532461,8.813471,-8.433907,6.318523,4.167072,5.537879,5.284094,-7.853411,-1.948951,-6.103121,-5.409620,-0.609411,7.105318,-4.878081,4.070163,-9.279505,5.060704,9.999738,-9.936199,3.085330,-6.369064,-8.222034,-3.477568,9.911237,6.113614,-8.229810,-2.072216,3.534102,-8.745118,7.139088,-1.466769,-1.075869,5.263694,-2.572849,-8.492101,2.362980,-4.445652,9.492948,-2.632400,9.522814,-5.315491,-5.667177,-5.975934,-5.619901,7.714887,4.580679,-2.143203,9.904398,6.826631,0.327364,1.379945,-1.582737,1.202112,-8.396133,4.828047,1.664464,9.832285,-1.252344,3.124521,-1.383643,7.108031,5.236127,0.366818,7.925454,-4.952340,1.223894,-2.112121,0.795837,6.957982,0.079230,6.338544,-1.938840,-4.005595,-2.552996,-1.865680,-0.217085,-3.955318,3.045448,-6.777570,9.878180,0.056680,-5.415290,-3.488457,6.354263,0.548054,-1.220011,-7.994942,0.956137,-3.952220,-5.485546,-5.855702,-7.893984,-9.320720,2.591645,-8.559187,0.958670,8.740949,6.898384,6.739817,2.264087,-8.308792,7.887415,-8.126764,3.144710,4.144394,3.104534,0.940365,-0.721084,4.543945,-3.820972,-0.280249,-1.231976,-5.038044,-8.041831,-7.689118,-2.841829,0.438110,2.007701,1.742291,-6.440342,0.775503,-7.517442,0.346314,-8.728384,-3.951779,3.264602,7.381679,-6.548834,2.176929,1.108163,-8.617732,-8.950508,-0.284449,-0.282633,9.833296,-7.535853,-6.512112,6.887002,5.820004,2.253528,-6.208501,0.518756,-4.392785,1.241317,-7.365072,0.497523,6.639882,-7.080815,-0.470845,2.329101,-0.103718,-1.035101,-2.884556,-2.957550,6.848930,-2.847802,-2.536563,9.673181,9.696115,7.881311,-3.892720,2.464605,-6.276338,2.850549,-4.571043,-5.138640,-4.674356,3.016905,-5.017032,-2.847165,2.051710,-4.519255,-1.673199,-6.098816,-4.591134,6.626996,0.813763,-4.160820,0.328902,-0.598133,-2.380125,-9.038759,7.599311,-4.023528,7.117278,3.952763,2.523682,6.300999,-7.030145,6.780872,1.646862,9.767067,9.652473,-2.180111,4.975168,-2.995320,-0.262499,-5.034638,9.497558,4.314087,7.256561,6.415496,-2.049232,0.381584,1.826479,-9.217801,3.801139,6.064347,4.065757,5.711837,-0.146745,6.507898,-3.624934,-4.472453,-4.613966,6.401146,-0.261711,-4.701206,9.223930,8.948709,-8.000224,7.991868,6.812769,5.013622,-2.855271,3.778628,-5.109627,9.746031,-1.587974,-5.772883,-2.728952,0.733179,5.221420,1.719526,0.027437,1.686988,-4.232924,8.977447,9.042116,9.218311,-2.789657,-5.491804,8.693769,3.606179,8.897627,-1.367719,6.712153,-4.241725,5.943537,6.347659,3.741356,-8.197859,6.410543,5.842380,-7.461374,1.524484,-3.991785,-0.207759,5.161926,8.287868,8.848725,-9.700031,5.313974,7.465737,8.993181,8.537825,1.968252,-4.560330,-0.539642,9.616515,-2.909831,0.464381,-2.729369,-0.205563,8.303039,-1.199414,8.508004,-1.713221,-5.552926,3.603640,-2.788649,-9.053509,1.376317,1.292312,-6.430936,-4.180764,5.873146,4.631719,3.132897,8.179351,-8.413073,-2.731930,6.935109,-0.801625,-2.126649,5.656865,7.826205,7.200999,-2.359566,-4.010597,9.750124,-5.062702,-3.250151,4.271426,1.683218,-0.895811,-2.750739,-1.531975,3.598981,4.109614,-1.116180,6.144272,-6.887544,-6.257591,1.403033,-0.465218,-4.907913,6.359757,-0.306615,-0.640378,5.602612,8.176569,0.001866,4.345631,0.056450,4.315661,8.113735,0.989968,3.072449,4.700052,-7.046920,0.863712,-4.899070,7.092724,6.069963,-0.658985,-4.809686,6.282723,0.175299,3.400310,0.745205,5.606329,4.517848,5.583961,-3.708917,4.101172,-6.657827,2.782076,9.872580,7.296806,4.823730,4.021843,-4.386089,4.628586,-7.711375,-5.010388,7.565539,-1.442821,-6.493830,8.571741,-3.682953,0.330619,-2.173986,7.077507,6.460839,-2.095768,5.052892,-8.641176,-2.225254,5.151795,-1.627443,5.238165,2.193303,-5.958194,3.975471,8.632182,-4.450263,-4.216253,8.892974,-1.268930,-9.791503,0.161030,9.992035,4.916061,-2.198153,-7.525978,-3.663334,-2.494217,3.914656,5.618166,5.868848,7.079205,9.911753,-7.319456,6.131540,7.161416,3.646048,2.235915,0.446642,8.512955,-0.367225,-5.598723,7.950175,-1.693170,-8.748127,3.234283,-0.739346,6.782355,-1.251285,5.884120,1.121170,4.372718,2.274119,2.072239,-6.553040,-9.122977,-0.020384,4.726409,-8.257149,-7.547684,-9.587874,-8.358211,-7.252811,-5.205303,2.991204,9.935059,1.375809,8.214398,7.705713,9.398953,0.798190,-2.404713,-7.927909,8.939098,-9.333062,2.008105,0.560263,9.934334,-0.317098,-8.692885,1.620406,-9.657745,8.905806,-2.389097,-4.040174,-0.372216,8.014596,0.475494,-0.100072,-5.259231,-4.412614,6.478464,9.590047,-4.755163,1.522710,3.265499,-4.125452,5.496810,-0.880195,-3.849582,6.622442,-1.914148,-1.159074,-9.082628,9.519154,7.044651,4.910423,9.774088,3.116263,-0.777820,9.825280,-3.217784,4.532336,4.525351,5.674940,-4.389884,-9.388378,2.564544,-3.048740,3.678211,2.055728,4.811251,-7.878219,7.330750,-0.929446,-7.364328,-6.043189,2.922953,-1.432955,4.260846,6.180687,-0.619440,-7.437665,-1.617052,5.024670,-0.785081,-7.584685,5.816592,8.269727,-4.231244,-5.792674,2.242109,2.303527,-7.742738,7.727735,3.706070,2.524264,-4.306039,-2.870351,-8.308281,-6.998869,-2.182821,5.021312,5.239223,-3.916459,-9.364491,-2.711102,8.969146,4.664484,9.500524,5.583991,6.918354,-1.891865,3.989064,-3.723339,1.093169,-0.629824,3.283439,5.207814,-7.254686,-6.393772,2.095061,-6.069698,2.451053,-0.695063,-4.583946,4.942175,5.248197,9.649864,-9.369489,-7.461927,5.258484,9.840270,-6.227394,6.499864,5.707371,-0.718562,7.287709,8.805958,-3.773905,3.419288,-4.839205,-6.918055,3.709250,-5.609153,4.574000,4.230686,3.955950,1.031164,5.915711,7.424247,-1.038968,6.926883,-4.875235,-1.073977,1.214794,-5.641468,8.019353,5.561664,-2.041424,-9.133195,-3.325841,-1.424945,9.279477,-1.190316,0.947446,0.826223,6.630367,9.846577,1.129127,-2.557063,0.906533,-3.126378,6.541112,9.411432,9.594989,5.156954,6.069750,-4.327932,6.064560,-7.845576,-9.538599,-6.270363,-9.592633,6.171176,-0.900745,-3.090555,-1.186137,-7.190761,-6.121716,-0.261438,4.432891,-4.280695,6.544023,5.321596,2.124666,3.669959,4.728500,5.987188,6.016783,-0.748681,-5.170708,-5.805463,0.987685,-2.763847,-8.085066,-1.595098,-1.932757,2.188752,3.159505,-7.076585,-6.408329,-5.809429,6.763433,7.325236,-3.398356,-9.287190,8.875976,-3.352961,7.327808,-0.215116,6.383269,-8.538484,7.497748,7.534179,-2.616140,2.142199,-8.464636,4.528990,3.475722,-4.387500,-0.693041,-6.457218,6.272296,-5.433622,7.526263,1.145793,3.778700,-1.105978,0.171183,9.982572,0.095086,-1.187511,-5.200080,-5.239143,-8.658790,-4.080122,2.116206,-0.719721,5.648805,-3.313086,-6.630381,5.095303,1.796288,-9.169294,9.044699,-6.633115,8.140196,-4.336842,-2.780053,9.422010,-6.746658,2.799243,8.993199,-9.643443,2.398967,2.784754,-5.845746,3.245052,3.594733,-4.334182,-2.433706,9.708794,1.646168,6.627472,-8.379310,4.773692,-6.636412,6.375101,-0.062125,-8.646606,-4.722481,0.006765,-3.056252,-9.503494,8.880573,6.484803,2.370614,2.028576,-8.542165,8.426913,6.123802,5.510027,8.750745,9.238792,8.949963,1.820024,-7.198933,-2.951742,-6.128556,-3.891188,-3.877359,3.423079,-5.975582,-6.456212,6.164066,-3.822023,-9.164000,7.500107,-1.333035,-4.892366,-3.323418,4.551016,-8.183619,-8.231627,-0.037904,-6.028985,-6.464343,-0.049944,-4.852537,0.178497,-0.075386,2.186145,-8.452748,0.260311,6.366563,-6.358711,4.282560,-4.450001,7.804859,-0.864498,5.431332,-7.608007,-0.100771,0.794347,-6.507782,1.460428,-8.782744,2.136876,4.382807,2.062962,-6.021745,-2.477670,2.031336,-9.405886,8.575673,-0.159882,2.693871,-4.141318,0.170750,0.914439,9.114122,6.332893,3.984488,-7.296944,2.488549,2.318893,8.945061,7.365082,7.008307,1.208937,6.568144,7.927422,9.103888,-5.253740,6.940132,-7.962286,-5.627915,-8.998743,-7.441689,-9.956391,-4.912317,-1.015144,-5.490421,-2.617815,6.265500,-5.290641,4.810731,1.245765,-8.645672,-9.754969,2.460452,-2.056199,-3.544493,6.189933,2.838200,-4.077162,-6.141872,0.923113,-5.475930,-1.645120,1.237902,-0.587733,-9.428187,4.493455,-1.477816,4.393304,-3.165120,2.398708,-1.490451,-6.723468,1.629488,-3.699306,3.536928,-2.655016,7.407777,8.764555,6.544453,-8.292023,3.175444,-3.366253,0.531316,-9.595572,1.548681,-5.762112,-2.495336,4.595066,2.073827,1.475264,0.392534,-0.796898,-9.764710,-6.434751,-0.928958,-2.786260,-7.566333,1.635297,-9.613738,-6.240462,4.911180,6.345510,5.305468,8.666000,-0.390498,0.102928,-5.452725,2.127511,8.097336,1.402711,-8.192561,4.018868,-8.443491,-4.678653,-2.078546,2.565152,0.131704,-0.238152,1.502164,4.846393,-9.585578,-3.045260,-2.701088,-6.236992,9.634436,1.285564,1.940513,-2.301731,4.450053,-2.275463,4.573567,-0.030394,-2.743577,5.084669,-0.698275,-5.596916,9.492986,-9.710226,-7.211237,6.974697,-4.382193,6.564093,-0.333256,1.617653,-0.070315,0.152225,6.880811,-6.353900,-3.967395,-3.780532,-1.334092,-6.650590,8.062894,6.358219,6.917888,6.527449,-6.831092,4.697102,-0.978979,-8.850013,-0.329636,3.275969,8.051671,1.991056,1.007523,4.208150,-1.731289,-1.047667,-4.363635,1.721731,-5.191978,7.994965,4.565473,9.005112,9.185761,-7.359100,-4.821486,-3.877141,2.587415,2.678324,9.182706,-6.654873,-6.896788,8.145808,3.294166,-7.324365,7.003111,-0.644362,-3.118050,-2.117506,3.973284,0.370391,-5.983846,-0.017781,-5.356445,9.452547,-0.723602,3.451607,-7.218655,4.243588,-6.958024,3.234222,6.150702,-9.206835,-9.432205,6.130306,-7.749419,6.360511,-8.128994,-3.452225,1.584101,-4.017561,-1.229445,3.721030,-8.102570,-8.273984,-5.538267,-3.071305,3.523321,-5.906273,-5.944881,7.520736,-8.012029,0.671470,-3.458133,0.427225,8.378595,0.021015,-3.725870,-3.688229,7.871257,5.109417,9.116372,8.180985,-6.607812,-8.630216,-4.434400,2.484944,-0.476525,1.349569,8.408323,-8.282102,6.796540,-3.323292,-4.536937,-0.252770,2.145998,-9.700285,-3.600422,5.106630,9.771173,6.736770,8.292071,-7.077616,0.188832,9.346681,0.293127,-5.330632,2.091394,-8.108525,9.998369,-6.682047,-1.520185,9.913755,-6.547545,5.547412,-4.100640,0.513203,-1.120055,5.119895,-6.695210,-5.013756,7.915617,-0.434552,7.359172,-3.272104,9.176466,2.233344,2.702181,-6.672956,5.474313,2.944663,-0.748057,6.966443,9.590792,8.627484,3.580228,8.847029,-0.023430,-6.205766,-1.864676,-3.714103,6.221256,4.296579,1.012739,-3.273201,7.260963,-5.645289,5.144936,-0.255332,3.774919,-4.738731,5.376290,0.064052,5.448815,0.394135,-9.811076,6.804274,7.871362,0.849629,4.839469,7.673766,0.017815,-5.982319,-5.412260,8.329851,-4.860494,-9.402673,3.625397,3.981923,2.628599,-6.039819,3.494887,9.806177,-8.044337,8.804985,3.387300,3.525852,-3.421418,6.149792,-9.794738,-1.531962,-3.347352,3.661081,-1.199571,-4.352685,7.636788,-8.194338,-5.102327,-2.810107,-6.810884,-8.959127,-0.152594,-1.086791,-1.771802,5.246735,9.766008,5.904001,8.471839,9.551331,-2.155488,2.837249,9.537206,-6.030572,-4.443118,-1.980098,-6.920715,-6.104321,-3.964214,9.310271,-7.719400,-8.929768,1.036745,4.398244,-4.423229,-4.800368,-7.723336,-1.290241,1.224697,2.992470,7.679972,-1.601664,5.267458,6.450454,-3.907924,-3.041469,3.108634,-5.383908,-2.653673,4.771176,-2.005154,0.351903,-7.215218,-2.607161,-6.317998,9.492279,-8.682889,7.646593,-1.107921,7.465751,-4.870003,9.230103,-3.123058,-8.586562,0.727624,3.780038,8.403652,-6.608516,2.839801,-3.398512,-7.571416,7.450910,5.943074,-7.856305,0.198437,-3.677252,1.382376,-4.476480,2.664909,9.850767,-9.457830,9.988340,3.371672,1.717853,-7.021664,4.670571,2.191460,3.489616,0.950835,-9.445085,-9.865028,-2.288222,-4.378921,6.021480,8.787507,-3.795094,-2.902822,-5.274912,0.956210,-0.465173,8.869931,1.195452,-3.558924,4.314731,-9.236221,7.371514,5.240068,0.091229,-8.885078,0.621605,3.490280,1.600715,7.878125,3.461725,-4.750701,8.160333,7.751917,-6.256476], dtype = "float64")#candidate|6192|(2520,)|const|float64
call_6191 = relay.TupleGetItem(func_1200_call(relay.reshape(const_6192.astype('float64'), [15, 12, 14]), relay.reshape(const_6192.astype('float64'), [15, 12, 14]), ), 0)
call_6193 = relay.TupleGetItem(func_1204_call(relay.reshape(const_6192.astype('float64'), [15, 12, 14]), relay.reshape(const_6192.astype('float64'), [15, 12, 14]), ), 0)
uop_6214 = relay.log10(const_6192.astype('float32')) # shape=(2520,)
func_2717_call = mod.get_global_var('func_2717')
func_2719_call = mutated_mod.get_global_var('func_2719')
call_6223 = relay.TupleGetItem(func_2717_call(), 0)
call_6224 = relay.TupleGetItem(func_2719_call(), 0)
output = relay.Tuple([call_6180,call_6189,call_6191,uop_6214,call_6223,])
output2 = relay.Tuple([call_6181,call_6190,call_6193,uop_6214,call_6224,])
func_6229 = relay.Function([], output)
mod['func_6229'] = func_6229
mod = relay.transform.InferType()(mod)
mutated_mod['func_6229'] = func_6229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6229_call = mutated_mod.get_global_var('func_6229')
call_6230 = func_6229_call()
output = call_6230
func_6231 = relay.Function([], output)
mutated_mod['func_6231'] = func_6231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6010_call = mutated_mod.get_global_var('func_6010')
call_6245 = func_6009_call()
call_6246 = func_6009_call()
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
const_6252 = relay.const([[8.709107,-1.283991,5.999032,-1.366214],[2.145522,1.541642,-0.941042,4.567658],[6.793630,-7.065125,3.420030,0.654458],[-4.564970,-2.160822,5.776472,-6.568591],[-4.371498,-2.733414,-3.864971,1.386963],[2.144439,-7.530094,-4.024048,-8.676207],[0.570469,1.745749,1.967955,-8.338821],[1.842762,-8.752917,0.049822,-7.558840],[-6.668423,5.491412,3.617028,-6.285287],[3.253324,3.343750,-8.515448,4.727024],[-0.962367,-8.668973,-4.659024,4.045664],[6.689569,-5.595734,2.429707,-7.911418]], dtype = "float32")#candidate|6252|(12, 4)|const|float32
call_6251 = relay.TupleGetItem(func_4522_call(relay.reshape(const_6252.astype('float32'), [12, 1, 4])), 0)
call_6253 = relay.TupleGetItem(func_4524_call(relay.reshape(const_6252.astype('float32'), [12, 1, 4])), 0)
uop_6254 = relay.sqrt(call_6251.astype('float32')) # shape=(12, 1, 4)
uop_6256 = relay.sqrt(call_6253.astype('float32')) # shape=(12, 1, 4)
func_930_call = mod.get_global_var('func_930')
func_934_call = mutated_mod.get_global_var('func_934')
var_6259 = relay.var("var_6259", dtype = "float64", shape = ())#candidate|6259|()|var|float64
var_6260 = relay.var("var_6260", dtype = "uint16", shape = (2,))#candidate|6260|(2,)|var|uint16
call_6258 = relay.TupleGetItem(func_930_call(relay.reshape(var_6259.astype('float64'), []), relay.reshape(var_6260.astype('uint16'), [2, 1]), ), 1)
call_6261 = relay.TupleGetItem(func_934_call(relay.reshape(var_6259.astype('float64'), []), relay.reshape(var_6260.astype('uint16'), [2, 1]), ), 1)
output = relay.Tuple([call_6245,const_6252,uop_6254,call_6258,var_6259,var_6260,])
output2 = relay.Tuple([call_6246,const_6252,uop_6256,call_6261,var_6259,var_6260,])
func_6267 = relay.Function([var_6259,var_6260,], output)
mod['func_6267'] = func_6267
mod = relay.transform.InferType()(mod)
mutated_mod['func_6267'] = func_6267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6267_call = mutated_mod.get_global_var('func_6267')
var_6269 = relay.var("var_6269", dtype = "float64", shape = ())#candidate|6269|()|var|float64
var_6270 = relay.var("var_6270", dtype = "uint16", shape = (2,))#candidate|6270|(2,)|var|uint16
call_6268 = func_6267_call(var_6269,var_6270,)
output = call_6268
func_6271 = relay.Function([var_6269,var_6270,], output)
mutated_mod['func_6271'] = func_6271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3332_call = mod.get_global_var('func_3332')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_6284 = relay.TupleGetItem(func_3332_call(), 0)
call_6285 = relay.TupleGetItem(func_3333_call(), 0)
func_3573_call = mod.get_global_var('func_3573')
func_3576_call = mutated_mod.get_global_var('func_3576')
const_6287 = relay.const([-3.289785,-6.077086,-3.978068,-7.858502,-5.919414,-2.575890,-0.450937,2.600429,-4.817933,3.539209,-5.865278,1.808223,-0.477384,3.212248,-7.705470,-3.514913,-4.641787,-6.926395,-9.832837,3.236060,-0.564189,9.104338,-2.222968,7.912182,-6.408922,-6.798833,-2.701606,-3.365625,-3.799437,-7.830063,6.409721,-5.354329,2.251524,-1.574843,9.503986,-5.925231,0.060555,-1.464545,-9.322785,5.865967,-7.750052,9.170325,9.669572,-5.889657,3.777258,-2.814557,9.970059,4.097670,-7.408929,-8.080653,9.497277,5.882972,-3.345200,-7.894558,2.294442,1.363364,3.518039,-0.326300,-8.694972,4.152286,8.508846,-4.152625,-6.427865,8.920197,-9.493689,-6.280317,-1.764362,-8.821464,7.754037,2.136424,-2.396189,5.201693,-3.513624,6.936159,-0.055693,-6.974400,-7.058094,-6.272630,-2.080512,5.076597,5.763493,-1.806028,4.533205,-6.307346,7.142439,7.505010,2.463077,-2.584660,-3.647344,-0.681022,-3.546771,-9.156537,-0.612581,2.391437,-0.992277,4.599409,-5.960430,9.314088,-3.650163,-5.368260,-5.719890,-2.376576,-5.672257,3.764060,-1.810738,9.117491,-2.762044,0.499703,-5.558026,-8.976771,-5.092307,-2.684525,0.153682,-0.937615,-1.740977,-8.286170,5.262369,-2.973009,7.564994,-8.684634,0.016731,-9.211479,-5.486377,-9.267405,-6.437641,0.690252,-7.049654,5.526980,-1.819280,-7.622898,-8.786248,6.717965,0.304190,-2.121857,7.704794,-9.452073,-1.988377,-9.324218,-8.979231,-1.059078,1.630000,9.145868,2.002469,-9.974077,1.827494,-2.999217,3.588805,4.585363,1.416335,1.297665,-0.119903,-3.853401,-7.684370,0.035244,0.266094,0.072520,-1.128296,2.784964,1.110568,4.719136,-0.064565,-8.997329,4.030703,-2.409451,7.767285,6.699906,3.229040,6.860514,-3.935511,-2.674271,-8.526983,3.432115,0.014393,-2.296028,-1.786237,0.784090,-1.069614,-5.196254,1.870400,-7.907412,-1.047393,-3.194937,1.803629,5.791449,1.134923,-1.699511,0.691582,-4.529604,-1.362077,1.532720,-2.312306,9.031054,-5.096512,-0.238880,-9.463025,0.218994,-0.751148,-5.372204,5.398729,6.999424,6.007177,-1.797896,9.560116,9.905150,5.102990,-4.130877,4.603850,-6.572445,2.761989,0.406405,-2.375441,-1.632512,7.554799,-7.276172,-0.331657,0.637820,8.955853,-1.190486,-2.594467,-9.022280,-1.102569,1.885489,-4.254064,-6.914788,-4.411233,1.872371,-6.670647,3.829701,-2.495861,-4.370316,1.767338,7.288822,8.110818,-4.711682,0.013232,5.879674,0.945856,-9.657106,3.816887,-9.218487,-2.511475,-7.732024,7.826090,-6.522560,3.210451,5.232828,-5.329007,-9.003136,-5.007316,6.488305,2.919284,-1.056212,3.156558,5.932072,7.634809,-2.508916,8.891947,-4.402554,-6.574644,4.989545,8.822999,1.019982,2.472962,0.554363,-0.863835,5.927975,1.204503,-0.140978,-4.503678,3.432565,6.591855,-1.403940,-9.590807,-9.834028,0.512208,0.957844,-9.018761,0.394936,-5.651404,3.275905,3.488460,-5.918838,-3.801613,-5.718699,-7.423981,-1.991565,9.840661,5.694851,6.692824,4.265851,5.430943,8.210105,9.360616,4.859536,3.280366,-0.575889,8.478969,-6.519291,6.612811,3.787840,-3.326704,-9.705344,-2.345496,-7.858594,9.105333,-8.606370,-0.640482,-6.873810,-8.877020,9.672877,-7.437065,3.618936,-8.089064,-8.131376,-1.099606,-2.391752,4.440923,-7.861813,-0.304147,-1.990655,-1.660509,-1.534498,-4.706900,-1.197580,-1.686660,7.032852,1.307800,-9.577738,-2.319231,-7.730788,-3.052115,4.206184,8.208346,7.188876,-2.960867,5.810919,1.046235,3.062756,-6.475473,-3.135898,0.431672,8.757982,-1.679084,9.605805,-8.822476,9.247552,-9.894013,8.912177,0.976100,0.696220,-1.131341,-0.482581,-4.931831,2.509770,-1.069818,7.112036,8.613195,-0.920977,-5.973621,-0.344407,3.571630,-4.822342,3.772529,5.378577,-8.242728,-2.358643,4.485128,-2.343695,5.603194,-1.399465,-2.662870,5.984569,6.541855,2.520288,6.651629,-3.652494,-3.509454,-3.542606,-5.941653,-5.979095,-1.784852,0.453209,1.194314,8.714921,-0.612691,-7.049550,4.435986,-1.213234,-8.596773,2.506931,-5.245334,-2.595345,-4.966880,-7.859971,8.408550,2.413846,1.845188,9.381735,2.905931,0.644818,3.422471,-0.975626,-7.808971,2.533082,-6.435584,-9.842455,-8.300719,4.396444,-5.711462,-5.084792,-1.530657,5.256290,-3.582030,0.085137,-5.766718,0.390565,-2.623048,-4.221707,2.396031,1.131679,-3.627708,-9.611773,3.943606,2.415195,8.173036,3.422093,-7.686293,7.013500,7.514300,-8.138379,-5.536137,1.457929,8.722000,1.307108,4.686797,-3.494201,-3.839971,7.897632,1.892315,1.145029,-5.978171,-9.489482,-1.777768,9.101771,-3.056527,8.462679,-8.284320,-9.973293,-0.470310,-2.579967,-9.492940,-5.967843,4.262718,-3.832092,-2.971346,5.538784,-5.592370,7.297924,0.195203,5.124613,-7.832376,-2.100467,6.771541,-6.267213,-5.772025,-4.333325,-6.080597,-6.694103,-5.694397,-9.134324,-9.746795,8.948081,8.072855,7.720877,7.868264,9.960787,2.173489,-6.358863,-6.201706,1.015641,0.859044,9.556975,-8.510388,9.862829,6.237103,1.989875,3.213214,-8.636532,-5.522615,-1.251573,-1.300212,3.187941,0.057290,9.381520,6.078047,8.752579,-1.253444,-6.610934,-3.883940,2.594546,7.569115,5.655620,4.738351,6.038278,-5.917924,8.658341,6.743528,-5.280576,8.057599,-7.338836,-8.985658,8.942746,5.368402,9.719726,-8.977023,5.881303,-0.345382,-4.517797,-2.965760,2.542576,4.572563,-4.087300,8.801816,-5.182753,-0.737605,7.465193,-1.231491,7.684717,-3.928050,0.976995,5.371863,-2.431984,2.829943,5.962663,2.410401,-9.422422,7.182307,2.260623,-5.273723,4.866588,3.732175,8.256843,-4.216578,8.940684,-5.032493,5.905781,1.572493,3.230872,-4.302288,-6.915897,6.574270,2.465322,6.166776,4.639555,-3.056861,-8.938468,-2.244162,0.131287,-3.361633,1.034128,3.974107,-3.018242,0.503416,4.605823,-5.003843,7.707935,3.376097,7.513699,4.126836,-7.444819,1.241077,7.419080,-5.765182,-1.375733,4.369165,9.789541,-7.533577,1.556711,9.145310,-6.147574,8.406883,5.964883,-6.249574,6.773194,-2.751641,1.322480,8.996056,3.140099,4.374962,-3.393885,4.947468,4.249501,-6.186862,7.116873,8.212118,0.406014,6.821047,0.571469,2.528191,-2.288965,-5.301990,-5.448575,-4.338929,-0.919300,9.907358,9.214715,-3.390772,1.205190,4.784459,8.163824,-0.218320,7.112471,2.882259,3.082026,-6.721353,-5.274846,4.238963,-3.366921,-1.762269,3.862648,0.727235,6.325802,0.695102,-9.276165,2.895531,6.453736,6.451361,-5.936162,-7.155191,1.193968,3.103061,6.012989,-9.090373,-0.260658,-8.949737,4.554804,-2.509018,-7.282935,6.300063,6.321717,-4.681057,-0.968824,1.557693,-0.574632,-8.845842,-8.684444,-8.554715,-5.582152,2.588441,1.082474,-3.713760,-6.376891,8.803517,-8.281529,6.516792,-0.488324,-7.382089,3.977524,6.801434,4.195697,-9.432459,5.141304,-3.558580,8.041394,-8.556458,2.692094,8.911719,-1.269994,-6.469216,2.236604,-0.712399,8.316832,-3.551007,-3.114214,7.567126,4.855658,-6.725087,-3.339655,-7.734726,-4.262252,-9.729544,6.597797,6.933972,1.194242,-3.680195,-0.244935,-9.727567,-0.375719,-6.642974,-6.806262,-9.491422,2.492932,-9.946400,0.464959,-1.941816,9.948966,-1.796968,-5.019902,-6.846190,2.854265,4.673658,7.941023,-1.984032,-4.600139,4.820977,-1.961792,9.501662,-4.909513,0.953155,-6.283154,8.591822,-1.125750,3.301936,-7.550676,-3.780221,-3.971034,2.047793,4.004362,4.493726,-5.941956,-9.710584,4.615339,7.179388,0.732095,4.709902,-8.086360,-3.893848,-2.770743,3.470566,0.935388,2.093946,4.897238,-8.945371,-7.681423,6.869309,-8.891528,4.585861,7.235410,5.070156,7.690814,-6.815117,6.899191,-6.384573,-3.323939,-0.485037,-1.650016,-7.617570,-3.762290,-3.635479,-5.802516,-7.494340,-7.815815,-4.596043,-0.198027,-8.534517,3.059611,3.982958,8.039580,-6.280147,0.365339,-6.423138,-7.638919,-5.681607,4.664046,7.405210,-0.110523,-1.214604,3.815971,-6.045297,-8.245333,7.796087,1.690259,-5.781504,4.774585,3.690971,-7.839363,-0.936786,-2.252646,4.136002,6.176308,1.561644,-7.966053,-8.157209,1.601046,1.149473,-5.157771,5.702274,2.874504,-3.586153,-8.116797,-0.073690,1.549096,-7.354292,9.965579,2.031988,-3.873274,-4.162932,-1.078772,0.640040,0.007920,5.175727,7.042703,3.548255,3.726206,9.320372,7.572831,-8.069773,-3.719908,-6.578308,-2.125859,0.683359,5.615761,-1.648824,-2.434844,5.107961,-1.129969,5.271672,9.294128,2.165961,0.492433,-5.985964,-2.274188,9.146104,7.872226,-5.410527,-1.128459,4.852141,0.096911,2.099814,0.384790,3.295501,-4.821641,9.260578,4.649794,-7.776528,-0.294058,-2.566653,8.587217,0.158673,1.759456,-5.788891,7.152991,6.557972,2.756707,9.498606,8.250171,5.665291,6.694493,6.051771,8.126612,4.540846,1.001997,-8.075582,-2.107364,9.501898,8.737788,0.677669,8.919409,2.765927,9.527303,7.256862,1.024207,-8.401487,-0.642650,8.777012,4.666098,8.902637,-9.085312,2.506128,1.439311,9.173884,9.019008,-9.183416,8.361449,9.152487,-8.251372,-4.517281,3.312969,-7.323582,-6.185026,8.327971,0.434926,-2.285595,-8.620154,-6.915574,5.132678,-9.080688,-5.772323,6.296961,-2.193770,-6.453542,-7.344090,-1.882959,-0.931100,6.104218,5.305289,-3.591560,2.517459,-6.152916,6.363361,2.773585,-6.978269,4.430481,-2.472512,6.518812,2.713793,9.625199,-2.737753,-3.528160,4.911095,4.969626,-7.032644,4.962445,1.580225,-3.077458,-4.387158,8.747297,5.956109,4.370697,0.767830,4.362712,-2.067567,-6.201890,-8.380648,5.710704,-7.527551,-4.930159,7.470489,-9.439723,-1.082432,9.287812,5.716035,9.959818,4.071764,-6.202430,7.941419,4.928792,0.542606,-8.508728,-7.313006,9.568647,3.094469,-7.015720,5.934204,9.031879,8.012084,-0.600552,2.443066,6.141616,-9.925228,0.004586,9.616478,2.504618,5.653684,7.986233,-1.041767,-5.562518,-4.273731,-1.390989,-6.563681,9.837172,-4.803395,-4.757502,-4.977087,-4.467057,3.441302,-4.122545,-6.021471,8.079870,-5.292450,-9.447374,3.494413,-3.970101,4.876849,4.654695,-3.315511,4.720292,-9.664414,-1.977232,4.132712,1.962958,-7.127345,-9.603341,-3.207888,-8.271741,-4.023090,2.320074,-9.648279,4.819990,-9.417041,8.614512,-4.660705,4.462555,-6.313200,1.339663,-2.746627,-9.283303,-3.614517,1.791726,9.857372,0.651651,-1.229384,7.213063,-2.349670,-3.686195,-2.802964,4.334809,-2.715934,0.898591,-5.140728,0.217629,-7.376832,-3.093312,-3.051539,6.641545,0.137343,3.499609,5.093350,-2.390356,3.563936,-8.019184,-6.025649,-4.553768,-0.216410,9.610851,-0.897119,7.816724,5.790318,-0.165715,7.918486,5.328574,-7.561092,5.443389,0.301218,-9.184906,-7.905243,-4.611721,-6.113077,-4.978386,6.830486,-7.652491,-1.817253,-4.371827,2.556280,0.655344,-9.490991,9.370232,0.147806,-0.456482,7.595327,9.173966,0.179725,-5.397405,5.849843,-9.170192,4.968391,-6.817791,-5.695253,8.539006,6.735858,-9.973959,1.989294,3.880906,-9.908657,7.287910,-6.750315,-9.677479,9.702134,8.250202,2.480541,8.831363,-9.716117,-7.001370,-1.206128,-3.812516,-7.145653,9.468925,2.079338,-1.649244,-0.104554,7.253642,-9.242024,-3.757288,-2.215658,-8.510283,4.651921,-2.615174,-9.816797,-5.285820,-9.720842,-7.125407,0.416532,-9.681878,-3.959291,5.767794,7.955628,8.546734,-2.343459,8.470158,-8.210104,-5.610481,6.251625,5.625335,1.298742,-1.247196,3.223675,-7.473995,-0.697425,9.270602,6.541033,3.048137,7.924467,-7.710933,-4.541596,-4.366789,-0.181294,-3.577289,-2.604270,2.058460,0.605492,4.563633,-3.653915,4.606491,9.915811,-4.361717,4.472494,3.431955,-8.084551,-8.569875,8.338212,5.357553,1.326568,2.947915,-1.240662,6.166140,-0.421457,-0.096542,-1.305885,3.328333,-0.182621,-3.374942,7.845128,-3.418128,-6.458723,-7.030382,1.585796,0.146341,9.772118,-4.803215,7.230527,2.078322,5.261552,-7.751738,3.492006,6.112301,3.403016,-3.688165,9.899756,6.278588,7.570140,8.669241,4.028246,-0.520912,6.837923,-5.292725,-2.625584,-6.533627,2.960303,-8.942672,-2.659176,-2.199752,6.320050,-9.345554,5.118569,-1.028418,6.420550,-6.626333,-5.219900,5.402268,5.645039,-7.463913,5.225713,0.133721,-5.878719,2.976295,9.243921,-9.831343,-8.946423,1.328873,-2.917073,0.373222,7.544692,5.304154,-8.057415,3.429837,-5.837529,2.391569,-3.167424,1.556987,-8.719512,8.447988,-3.743485,1.264248,-7.880059,5.605939,-1.398675,-3.397833,-0.056808,-1.150478,-1.122587,-5.049876,7.186784,-7.556556,4.421803,-5.725984,7.912119,6.593321,-3.297799,-3.771636,-5.795867,1.611843,-4.036754,-0.055575,7.653950,0.255329,5.968506,5.688233,-1.723215,-9.467761,6.032345,4.356444,4.442702,-8.969963,2.754293,-4.957734,-1.022626,8.092057,-0.061484,5.488885,-6.456381,1.654272,2.041099,-8.959608,6.217937,1.683899,-7.461187,4.357728,2.913241,6.486082,-4.721887,-2.269584,9.917992,-6.735209,-4.601530,-8.718889,-0.660391,-0.548667,-2.905155,6.937931,7.609592,-0.920085,-1.239513,6.895628,0.911338,-4.640283,6.434914,0.373306,-6.906796,-0.778651,9.067316,3.814964,-7.086745,3.384600,0.536343,-3.170644,4.800794,-0.019858,-5.709518,-1.585481,-0.483478,-6.200646,4.583479,-2.105234,0.537935,-2.441952,2.995509,-0.560638,9.519622,-6.070219,8.027407,-3.793678,5.695803,-0.850836,-3.398549,-2.399044,6.876776,-3.515447,-8.038110,5.033116,1.497551,-5.665724,2.704263,1.700694,7.722757,7.085397,-8.149337,0.240525,-9.515860,-6.541450,-6.515183,3.992702,4.844918,6.352647,6.809593,8.854491,-9.047611,2.344854,-1.470447,8.981466,4.665939,-7.582791,-7.527020,7.954183,5.454097,5.587420,-7.134807,-4.877059,3.180852,5.789695,-2.668785,8.398557,8.703487,-0.804921,2.511820,4.231274,8.722941,9.387665,9.458691,-5.388301,-4.295684,4.693534,2.541947,-8.752925,9.001073], dtype = "float64")#candidate|6287|(1344,)|const|float64
call_6286 = relay.TupleGetItem(func_3573_call(relay.reshape(const_6287.astype('float64'), [8, 14, 12])), 0)
call_6288 = relay.TupleGetItem(func_3576_call(relay.reshape(const_6287.astype('float64'), [8, 14, 12])), 0)
func_232_call = mod.get_global_var('func_232')
func_236_call = mutated_mod.get_global_var('func_236')
const_6294 = relay.const(9.971028, dtype = "float32")#candidate|6294|()|const|float32
var_6295 = relay.var("var_6295", dtype = "float32", shape = (175,))#candidate|6295|(175,)|var|float32
call_6293 = relay.TupleGetItem(func_232_call(relay.reshape(const_6294.astype('float32'), []), relay.reshape(var_6295.astype('float32'), [5, 7, 5]), ), 0)
call_6296 = relay.TupleGetItem(func_236_call(relay.reshape(const_6294.astype('float32'), []), relay.reshape(var_6295.astype('float32'), [5, 7, 5]), ), 0)
output = relay.Tuple([call_6284,call_6286,const_6287,call_6293,const_6294,var_6295,])
output2 = relay.Tuple([call_6285,call_6288,const_6287,call_6296,const_6294,var_6295,])
func_6329 = relay.Function([var_6295,], output)
mod['func_6329'] = func_6329
mod = relay.transform.InferType()(mod)
var_6330 = relay.var("var_6330", dtype = "float32", shape = (175,))#candidate|6330|(175,)|var|float32
output = func_6329(var_6330)
func_6331 = relay.Function([var_6330], output)
mutated_mod['func_6331'] = func_6331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3493_call = mod.get_global_var('func_3493')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_6342 = relay.TupleGetItem(func_3493_call(), 1)
call_6343 = relay.TupleGetItem(func_3494_call(), 1)
func_5893_call = mod.get_global_var('func_5893')
func_5899_call = mutated_mod.get_global_var('func_5899')
var_6349 = relay.var("var_6349", dtype = "float32", shape = (6,))#candidate|6349|(6,)|var|float32
const_6350 = relay.const([3,4,9,-3,-3,-1,3,5,-2,5,-1,10,-9,2,10,6,3,9,5,-6,3,5,-9,-7,-7,6,-3,3,1,2,1,3,10,-5,8,-3,-1,6,-1,3,-7,-5,-9,-2,6,-2,-2,2,-8,8,10,-6,10,-3,5,8,-8,2,-1,-8,6,3,-4,3,2,10,3,-5,8,-3,-3,-6,-5,-6,3,-3,-5,-9,3,-3,-3,9,10,8,-9,2,-3,-2,-7,5,6,8,-6,8,-1,6,-5,2,8,-3,5,10,-4,-8,-5,-10,3,-10,-7,10,-1,-1,-1,10,-5,8,-8,7,3,2,8,-6,-10,-2,5,4,-8,10,10,-9,-5,-6,-5,5,-10,-3,1,-1,-6,-9,-3,-6,-9,-10,-8,-7,-8,-4,-8,1,7,6,5,-10,-8,-1,1,-2,4,1,-3,-5,-9,-3,9,5,-10,-6,8,-6,-3,9,-4,4,5,10,-2,-10,-5,10,-9,-1,-5,5,-1,2,-10,9,2,-2,9,-6,8,-5,-10,-8,-9,-9,-6,-10,7,-2,-2,3,-6,-2,10,7,-5,2,7,-6,8,3,-10,-10,4,8,-5,-10,7,-6,-4,-4,7,-6,-5,-3,8,5,-8,8,9,5,-6,-4,1,-1,-7,5,2,-8,-4,8,-6,1,-9,3,-5,-3,7,6,-9,2,2,10,1,-1,-1,-8,-3,1,7,10,-6,3,-10,3,3,-7,-5,1,7,10,10,-6,-8,-4,3,-7,7,-2,8,-10,3,10,-4,-1,-10,2,-10,2,5,2,-2,-9,-10,7,6,-1,-5,-6,-9,-2,9,-10,4,8,-9,-9,9,9,-9,-9,4,-6,10,-9,-1,1,-7,-1,-4,10,9,-4,7,10,-2,1,-1,-6,-8,-2,-8,-9,4,5,8,3,7,8,3,-10,-8,-2,7,-10,4,2,-4,6,10,8,-1,7,-8,-1,-4,-5,-1,3,-6,-1,-4,-2,-3,-10,2,-2,9,-10,-4,-8,-2,-5,2,9,1,-8,-2,-5,1,-9,-3,5,-10,-9,-5,-7,1,-8,-7,9,-8,3], dtype = "uint8")#candidate|6350|(396,)|const|uint8
const_6351 = relay.const([-6.724560,3.856638,6.349743,-3.249636,-1.284222,-9.703657,8.087375,-2.464558,-7.733615,8.561274,0.302725,-1.646273,-7.619219,-4.880448,5.180813,-1.878311,8.578071,-4.738450,-5.670088,-4.027788,2.432360,-9.534573,4.470115,3.806204,1.700950,-3.113982,2.366356,3.199563,-3.146439,0.172777,7.969327,7.615803,-2.542452,-9.018042,-2.095844,6.291253,5.409888,5.670559,1.111257,-7.986979,0.514653,5.702140,-1.229535,-0.585489,-9.163065,-1.606133,3.998534,8.665295,4.387912,-3.545109,-0.653946,-9.946762,4.191690,3.599128,-2.417255,9.963905,-6.793498,-3.832033,8.568737,-6.509302,9.391556,-0.638442,-5.505259,-3.691971,1.747849,-1.428725,-7.721984,3.542252,-3.539584,-7.263474,-6.444635,-9.403271,1.446183,1.534857,5.738764,-7.823111,0.246166,2.253607,-4.411377,7.409061,-0.890935,-4.651612,-2.733851,-5.457848,-1.831099,-1.543068,0.778748,7.791276,4.729327,2.586848,-0.691267,7.418262,-2.296536,-6.284093,-8.486421,-6.488645,6.727238,-5.471544,-9.868763,-5.107103,2.601250,-6.915105,5.877970,1.284148,-6.585605,5.597467,9.732663,-9.676525,3.782319,-8.326419,0.317129,-8.323264,8.966288,-1.581925,1.605487,-2.796011,5.552791,8.684842,4.359993,-7.368452,-4.803851,-2.120436,-0.751008,6.243830,7.282654,-8.956278,9.428876,1.787136,7.991911,-0.006968,-3.580052,9.329128,2.602336,-3.727165,-1.750346,2.713718,-9.066721,-0.965452,-3.457560,-2.225044,9.740428,-8.200997,4.901589,-3.256778,-6.175885,-3.604165,0.501360,-9.028683,-8.883155,1.450195,2.660855,8.218369,3.288767,6.299634,-0.317162,3.143608,-7.549917,-2.034583,-1.964144,-8.653300,4.178619,3.450044,-6.997788,-6.508254,2.775697,8.538860,-1.802152,-7.014678,-8.719176,8.393879,-3.701637,1.140652,5.605906,-6.572304,-2.148908], dtype = "float32")#candidate|6351|(175,)|const|float32
var_6352 = relay.var("var_6352", dtype = "uint16", shape = ())#candidate|6352|()|var|uint16
call_6348 = relay.TupleGetItem(func_5893_call(relay.reshape(var_6349.astype('float32'), [6, 1]), relay.reshape(var_6349.astype('float32'), [6, 1]), relay.reshape(const_6350.astype('uint8'), [6, 66]), relay.reshape(const_6351.astype('float32'), [175,]), relay.reshape(var_6352.astype('uint16'), []), ), 0)
call_6353 = relay.TupleGetItem(func_5899_call(relay.reshape(var_6349.astype('float32'), [6, 1]), relay.reshape(var_6349.astype('float32'), [6, 1]), relay.reshape(const_6350.astype('uint8'), [6, 66]), relay.reshape(const_6351.astype('float32'), [175,]), relay.reshape(var_6352.astype('uint16'), []), ), 0)
output = relay.Tuple([call_6342,call_6348,var_6349,const_6350,const_6351,var_6352,])
output2 = relay.Tuple([call_6343,call_6353,var_6349,const_6350,const_6351,var_6352,])
func_6369 = relay.Function([var_6349,var_6352,], output)
mod['func_6369'] = func_6369
mod = relay.transform.InferType()(mod)
mutated_mod['func_6369'] = func_6369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6369_call = mutated_mod.get_global_var('func_6369')
var_6371 = relay.var("var_6371", dtype = "float32", shape = (6,))#candidate|6371|(6,)|var|float32
var_6372 = relay.var("var_6372", dtype = "uint16", shape = ())#candidate|6372|()|var|uint16
call_6370 = func_6369_call(var_6371,var_6372,)
output = call_6370
func_6373 = relay.Function([var_6371,var_6372,], output)
mutated_mod['func_6373'] = func_6373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_6419 = relay.TupleGetItem(func_2781_call(), 0)
call_6420 = relay.TupleGetItem(func_2782_call(), 0)
output = call_6419
output2 = call_6420
func_6441 = relay.Function([], output)
mod['func_6441'] = func_6441
mod = relay.transform.InferType()(mod)
output = func_6441()
func_6442 = relay.Function([], output)
mutated_mod['func_6442'] = func_6442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5238_call = mod.get_global_var('func_5238')
func_5239_call = mutated_mod.get_global_var('func_5239')
call_6458 = relay.TupleGetItem(func_5238_call(), 0)
call_6459 = relay.TupleGetItem(func_5239_call(), 0)
output = call_6458
output2 = call_6459
func_6460 = relay.Function([], output)
mod['func_6460'] = func_6460
mod = relay.transform.InferType()(mod)
output = func_6460()
func_6461 = relay.Function([], output)
mutated_mod['func_6461'] = func_6461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6010_call = mutated_mod.get_global_var('func_6010')
call_6470 = func_6009_call()
call_6471 = func_6009_call()
func_2268_call = mod.get_global_var('func_2268')
func_2269_call = mutated_mod.get_global_var('func_2269')
call_6483 = relay.TupleGetItem(func_2268_call(), 0)
call_6484 = relay.TupleGetItem(func_2269_call(), 0)
output = relay.Tuple([call_6470,call_6483,])
output2 = relay.Tuple([call_6471,call_6484,])
func_6495 = relay.Function([], output)
mod['func_6495'] = func_6495
mod = relay.transform.InferType()(mod)
output = func_6495()
func_6496 = relay.Function([], output)
mutated_mod['func_6496'] = func_6496
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6499 = relay.const([[[8.759863,-3.071237,-8.849453,-3.785255,-3.021311,8.207192],[7.546544,-8.021348,0.576947,-1.951382,0.753474,-2.213321],[-1.778393,-3.349921,-3.656761,-9.760631,2.639689,4.880013],[2.409591,-9.076649,-7.916489,-8.596297,7.272738,-1.681185]],[[-2.725206,-1.730502,7.253571,0.645072,2.502060,-9.467521],[5.342493,-4.798640,-4.168753,4.315245,6.683157,1.016478],[1.803079,5.863409,3.952717,-2.580302,-6.670812,9.988761],[7.517004,-7.346655,-1.276294,-3.548637,8.527768,-9.406261]]], dtype = "float32")#candidate|6499|(2, 4, 6)|const|float32
uop_6500 = relay.acosh(const_6499.astype('float32')) # shape=(2, 4, 6)
bop_6502 = relay.logical_or(uop_6500.astype('bool'), relay.reshape(const_6499.astype('bool'), relay.shape_of(uop_6500))) # shape=(2, 4, 6)
uop_6507 = relay.atan(bop_6502.astype('float32')) # shape=(2, 4, 6)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_6514 = func_2649_call()
call_6515 = func_2649_call()
output = relay.Tuple([uop_6507,call_6514,])
output2 = relay.Tuple([uop_6507,call_6515,])
func_6518 = relay.Function([], output)
mod['func_6518'] = func_6518
mod = relay.transform.InferType()(mod)
mutated_mod['func_6518'] = func_6518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6518_call = mutated_mod.get_global_var('func_6518')
call_6519 = func_6518_call()
output = call_6519
func_6520 = relay.Function([], output)
mutated_mod['func_6520'] = func_6520
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6554 = relay.const([[[1,-6,4,-10,-4,-9,-6,3],[3,-4,-9,8,10,-10,5,-10],[-7,-5,-2,4,-7,-2,-7,9],[-10,5,-1,7,-6,2,-6,-8],[-1,-6,9,10,4,10,-8,-3],[2,-8,-1,-4,-5,-8,1,5],[-8,-8,2,-4,-9,-8,-3,-3]],[[-9,8,9,6,-10,-4,10,-6],[10,-7,9,9,-6,-5,9,4],[1,9,5,6,2,8,-9,2],[6,4,-3,-5,3,7,-8,-10],[-6,2,6,9,-8,-2,1,8],[5,5,8,-6,10,1,-6,-8],[1,4,-8,3,-9,-2,-9,8]],[[-6,-2,4,3,3,3,-4,2],[1,-3,10,-4,1,9,-8,-3],[-3,7,3,3,-4,5,-7,5],[6,6,4,-5,6,4,-3,10],[-4,-1,-7,-2,1,10,8,-6],[3,-8,-4,3,-7,5,6,3],[-2,-8,1,9,9,9,-7,2]],[[9,-9,5,2,-1,-1,4,-6],[2,-5,-5,-4,6,-4,10,-4],[-7,9,-7,5,2,4,2,10],[5,7,-10,6,6,-10,5,-3],[-1,6,7,-5,-7,-3,-10,-3],[8,4,-2,-5,-10,5,1,10],[2,9,7,-8,-2,5,4,6]],[[9,2,-8,-2,-4,-6,6,-6],[-3,-10,8,5,9,-3,-8,-4],[6,-8,5,-5,-8,-3,-8,-3],[-3,-9,10,-10,-6,1,1,-10],[-3,3,10,-6,-10,1,7,9],[8,8,4,7,2,-3,-3,-10],[-1,4,-3,-8,-7,-3,6,2]],[[-9,-1,2,-2,-8,-9,-8,-7],[4,-8,2,-1,6,3,5,-5],[-10,9,6,8,8,7,8,5],[-7,-10,9,-8,-5,-9,8,9],[10,-2,1,4,-9,5,5,9],[3,1,-1,10,-1,10,-3,-9],[-7,1,3,7,-6,-9,-4,-5]],[[8,-10,-6,-8,-9,8,7,3],[8,-2,-1,3,3,8,-10,6],[-8,10,-7,3,-9,8,-10,-10],[6,9,2,5,-4,5,-4,4],[9,8,-4,-4,3,9,-2,2],[-2,7,5,-1,5,-4,9,2],[6,6,4,3,1,-1,-10,2]],[[5,7,-1,10,-4,-6,-6,3],[-10,-10,-8,-2,-4,3,-5,9],[6,2,4,-3,6,-3,8,4],[4,4,6,2,-6,-7,2,3],[-2,5,-6,-4,10,5,-3,9],[3,-1,7,3,10,6,-8,10],[-3,7,7,-2,-9,6,7,1]],[[-9,3,8,9,9,-10,6,8],[6,9,-7,2,-1,9,-6,-10],[-5,-10,2,-10,7,-8,1,4],[-9,5,-5,3,-7,-4,5,7],[8,4,7,8,6,-8,-2,-8],[-5,-9,10,-6,6,-10,-5,-2],[4,-2,-2,6,-8,8,-7,3]],[[9,-4,-5,6,2,2,-2,-2],[-4,9,7,-5,10,-5,10,-10],[-1,8,9,-7,9,-10,-6,7],[-9,6,-2,10,-4,10,4,-5],[-6,-9,8,-6,7,-7,-10,-5],[-3,-4,-3,8,9,3,7,8],[-2,6,5,6,10,7,2,-9]],[[-4,-1,-7,-4,4,-2,7,2],[-7,9,4,5,9,-6,-5,-7],[7,-4,4,5,-9,-8,-4,-6],[-3,-6,10,-1,-5,-1,1,7],[-5,-4,-3,8,-5,8,9,4],[-1,-6,-2,-4,-3,5,-3,4],[5,9,-9,8,1,3,2,-1]],[[8,3,-8,6,2,-5,-6,-4],[-7,9,-10,-9,-4,3,2,6],[3,1,-6,3,8,4,-7,5],[3,-1,2,4,-6,10,10,9],[7,7,9,-5,7,1,10,-1],[1,-6,6,6,6,10,-6,-1],[1,8,7,-6,-3,-10,6,-5]],[[-5,-9,2,1,-3,-4,-3,4],[5,3,5,8,-8,-2,10,-1],[-10,-4,-6,-10,7,10,1,4],[-5,-7,8,-10,-4,1,2,8],[4,4,-8,-9,-8,-7,-2,-4],[7,9,7,-4,-2,4,8,-5],[6,2,-4,1,1,-1,-8,-2]],[[-6,-2,10,3,-10,-7,-1,-1],[-2,2,-6,-7,8,10,5,-1],[-2,-4,-9,-6,8,-7,6,7],[-3,-5,10,3,-2,-4,-8,-7],[-9,5,-10,7,2,8,-2,-7],[1,-1,6,1,-1,-4,-1,9],[4,8,-5,-3,-8,7,3,4]],[[-6,7,1,9,-2,-10,5,-4],[3,2,-6,-7,3,4,-7,-2],[-5,6,-4,9,7,-10,1,1],[6,4,-8,6,-4,-9,-9,6],[7,-10,-7,8,8,-8,2,5],[-5,-9,7,-6,6,-3,-6,8],[1,6,-9,-3,4,8,-1,5]]], dtype = "int64")#candidate|6554|(15, 7, 8)|const|int64
const_6555 = relay.const([[[-4,-9,-6,-7,-4,-7,1,-6],[-7,-10,6,-7,-6,8,-8,9],[6,4,-6,-4,-5,-5,-1,9],[-3,-2,-8,-8,3,4,3,-5],[9,10,2,10,-4,-4,-5,6],[1,-8,7,3,2,-3,-9,3],[-8,7,-8,7,-1,9,-3,5]],[[3,3,9,-1,-3,5,1,-4],[-10,2,8,-10,-10,5,5,7],[3,-9,-8,-3,-3,3,-6,-6],[7,-4,7,4,-4,1,10,9],[-2,6,-9,8,-7,7,-7,-10],[8,9,-8,3,3,3,-5,-9],[-3,4,-5,-3,5,-6,10,7]],[[7,-5,1,1,5,-9,8,-7],[4,2,-6,-2,4,3,3,6],[-8,-7,1,4,1,8,3,2],[-1,-9,-9,9,-8,-1,-4,10],[-8,-10,-4,6,-8,-7,-2,-10],[-3,-9,7,-8,-10,-5,6,6],[-4,-2,9,-4,-2,7,1,-4]],[[-4,7,-1,-8,5,-5,1,-4],[8,-3,-4,3,9,-10,9,5],[9,9,-8,-10,2,-6,7,-6],[-6,1,6,-5,-7,-5,9,2],[-1,-7,-7,4,2,-2,9,-5],[7,-4,3,-9,-4,-7,-4,2],[-1,6,6,7,1,-1,7,5]],[[4,-8,1,-9,4,10,6,-5],[1,-5,3,-4,-9,-5,1,-10],[-1,3,-8,9,-10,-9,-2,-3],[6,-9,10,-3,8,-7,2,-7],[-8,7,5,-7,6,3,-10,9],[6,5,1,5,10,2,9,-4],[-2,-2,-8,3,-5,-10,-5,-1]],[[6,5,5,-1,-1,-6,-4,9],[1,4,10,-1,-4,-8,-1,9],[4,-7,5,-6,10,-9,2,10],[-9,3,4,4,7,8,-10,5],[1,7,-1,2,-4,-8,9,10],[-4,5,10,-5,-3,7,10,-9],[6,-8,-8,-8,3,9,-4,10]],[[-3,-4,-6,10,-2,3,8,2],[10,3,-2,2,-7,-5,-1,8],[10,7,-3,-5,5,-6,10,9],[7,9,2,-5,2,9,5,-9],[1,2,4,-8,5,-4,-3,-4],[6,10,-3,-7,4,-10,7,-7],[5,4,-7,10,8,7,-8,2]],[[2,-4,-8,4,10,3,3,-6],[9,10,2,-8,-6,2,3,10],[5,-4,6,4,-10,-1,-7,1],[-7,-2,1,-9,-4,-2,4,-4],[-5,-1,6,5,2,-9,3,7],[-3,8,10,2,10,-10,-6,-3],[-5,-10,-2,7,10,-5,7,2]],[[-10,7,-2,3,-5,-6,1,9],[-6,7,3,1,9,8,-7,-8],[-5,-8,-6,-8,-6,-9,6,3],[1,9,1,9,8,-7,-8,-4],[2,9,-5,-6,-1,-7,6,-10],[-9,1,9,-1,-5,-3,-5,-5],[1,2,1,8,-4,-1,-7,7]],[[10,-10,-8,-7,9,-8,-9,1],[9,9,-1,3,3,10,-5,-8],[7,-5,8,9,-3,4,-2,-3],[8,10,-10,7,-7,3,-3,6],[-10,-6,2,-10,2,7,8,-6],[4,8,-9,7,-1,7,-3,6],[3,-4,7,7,7,-5,6,3]],[[-9,5,-5,3,3,2,2,-1],[-9,-7,-8,-8,-10,2,-6,7],[-6,-1,-5,5,-4,-7,-4,-1],[-5,9,-7,-2,2,5,9,-1],[-6,-3,9,-2,6,1,-2,-5],[3,2,-3,-6,-8,-10,5,-3],[-8,-6,6,-1,-9,-4,-7,8]],[[5,9,-6,-10,8,-3,-3,-5],[-3,-7,-9,3,3,9,-8,-9],[6,-2,2,9,2,-4,10,-6],[-10,-2,-1,9,6,-1,2,9],[7,2,-3,-1,5,-2,7,-6],[10,8,-6,-5,-4,7,8,5],[9,-7,8,-7,-5,8,6,-9]],[[-3,-8,-3,-1,9,2,-6,-3],[6,-7,-1,-7,-5,8,-8,-8],[5,2,-8,4,3,-5,5,-3],[-1,5,-7,8,-9,3,-5,-10],[8,-8,-7,4,-2,-8,-10,-8],[-3,2,-7,-4,-7,6,2,2],[-10,-4,7,-6,10,6,4,10]],[[-6,1,-1,2,6,7,5,-5],[2,-3,-1,5,-2,-9,4,-6],[-2,-6,4,8,-7,5,6,9],[1,-6,1,-2,-2,-1,-2,7],[-6,4,10,-7,1,-8,-3,-5],[-1,7,-4,-6,3,3,4,9],[4,7,9,10,9,-7,7,7]],[[4,-9,-4,-5,2,-4,9,-6],[9,4,1,-6,-3,1,8,5],[3,-10,-1,-5,4,-9,3,5],[-1,7,-4,10,-9,-5,-2,-9],[-6,-3,-6,10,-8,-5,4,-2],[-9,-7,-4,-8,10,8,-6,7],[7,-1,-10,5,9,8,7,8]]], dtype = "int64")#candidate|6555|(15, 7, 8)|const|int64
bop_6556 = relay.bitwise_or(const_6554.astype('int64'), relay.reshape(const_6555.astype('int64'), relay.shape_of(const_6554))) # shape=(15, 7, 8)
output = relay.Tuple([bop_6556,])
output2 = relay.Tuple([bop_6556,])
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
var_6584 = relay.var("var_6584", dtype = "float64", shape = (2, 12, 6))#candidate|6584|(2, 12, 6)|var|float64
uop_6585 = relay.log(var_6584.astype('float64')) # shape=(2, 12, 6)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_6589 = func_2649_call()
call_6590 = func_2649_call()
func_407_call = mod.get_global_var('func_407')
func_412_call = mutated_mod.get_global_var('func_412')
var_6599 = relay.var("var_6599", dtype = "bool", shape = (1, 819))#candidate|6599|(1, 819)|var|bool
const_6600 = relay.const(-9, dtype = "uint16")#candidate|6600|()|const|uint16
var_6601 = relay.var("var_6601", dtype = "float32", shape = (7, 25))#candidate|6601|(7, 25)|var|float32
call_6598 = relay.TupleGetItem(func_407_call(relay.reshape(var_6599.astype('bool'), [819,]), relay.reshape(const_6600.astype('uint16'), []), relay.reshape(var_6601.astype('float32'), [1, 175]), ), 0)
call_6602 = relay.TupleGetItem(func_412_call(relay.reshape(var_6599.astype('bool'), [819,]), relay.reshape(const_6600.astype('uint16'), []), relay.reshape(var_6601.astype('float32'), [1, 175]), ), 0)
func_6329_call = mod.get_global_var('func_6329')
func_6331_call = mutated_mod.get_global_var('func_6331')
call_6626 = relay.TupleGetItem(func_6329_call(relay.reshape(var_6601.astype('float32'), [175,])), 5)
call_6627 = relay.TupleGetItem(func_6331_call(relay.reshape(var_6601.astype('float32'), [175,])), 5)
func_4340_call = mod.get_global_var('func_4340')
func_4341_call = mutated_mod.get_global_var('func_4341')
call_6631 = func_4340_call()
call_6632 = func_4340_call()
output = relay.Tuple([uop_6585,call_6589,call_6598,var_6599,const_6600,var_6601,call_6626,call_6631,])
output2 = relay.Tuple([uop_6585,call_6590,call_6602,var_6599,const_6600,var_6601,call_6627,call_6632,])
func_6633 = relay.Function([var_6584,var_6599,var_6601,], output)
mod['func_6633'] = func_6633
mod = relay.transform.InferType()(mod)
mutated_mod['func_6633'] = func_6633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6633_call = mutated_mod.get_global_var('func_6633')
var_6635 = relay.var("var_6635", dtype = "float64", shape = (2, 12, 6))#candidate|6635|(2, 12, 6)|var|float64
var_6636 = relay.var("var_6636", dtype = "bool", shape = (1, 819))#candidate|6636|(1, 819)|var|bool
var_6637 = relay.var("var_6637", dtype = "float32", shape = (7, 25))#candidate|6637|(7, 25)|var|float32
call_6634 = func_6633_call(var_6635,var_6636,var_6637,)
output = call_6634
func_6638 = relay.Function([var_6635,var_6636,var_6637,], output)
mutated_mod['func_6638'] = func_6638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4340_call = mod.get_global_var('func_4340')
func_4341_call = mutated_mod.get_global_var('func_4341')
call_6851 = func_4340_call()
call_6852 = func_4340_call()
output = relay.Tuple([call_6851,])
output2 = relay.Tuple([call_6852,])
func_6857 = relay.Function([], output)
mod['func_6857'] = func_6857
mod = relay.transform.InferType()(mod)
mutated_mod['func_6857'] = func_6857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6857_call = mutated_mod.get_global_var('func_6857')
call_6858 = func_6857_call()
output = call_6858
func_6859 = relay.Function([], output)
mutated_mod['func_6859'] = func_6859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4942_call = mod.get_global_var('func_4942')
func_4943_call = mutated_mod.get_global_var('func_4943')
call_6865 = relay.TupleGetItem(func_4942_call(), 0)
call_6866 = relay.TupleGetItem(func_4943_call(), 0)
output = call_6865
output2 = call_6866
func_6902 = relay.Function([], output)
mod['func_6902'] = func_6902
mod = relay.transform.InferType()(mod)
mutated_mod['func_6902'] = func_6902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6902_call = mutated_mod.get_global_var('func_6902')
call_6903 = func_6902_call()
output = call_6903
func_6904 = relay.Function([], output)
mutated_mod['func_6904'] = func_6904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_6962 = relay.TupleGetItem(func_2152_call(), 0)
call_6963 = relay.TupleGetItem(func_2154_call(), 0)
func_6460_call = mod.get_global_var('func_6460')
func_6461_call = mutated_mod.get_global_var('func_6461')
call_6975 = func_6460_call()
call_6976 = func_6460_call()
func_2007_call = mod.get_global_var('func_2007')
func_2011_call = mutated_mod.get_global_var('func_2011')
var_6990 = relay.var("var_6990", dtype = "uint8", shape = (1, 396))#candidate|6990|(1, 396)|var|uint8
const_6991 = relay.const([[4.409894,8.934563,0.862747,-5.812404,-6.714108,6.739299,-4.869290,8.947254,-1.804555,-7.719572,-0.713081,-7.952821,6.683858,6.677322,4.904529,-4.882967,9.555025,7.864165,1.376427,-7.333335,9.811038,0.603000,-2.595876,3.155846,2.624311,2.482433,-6.481546,-1.476914,3.046271,1.135376,-9.123993,1.454354,8.576050,-4.769781,-3.079504,0.634025,-2.739032,-0.809481,3.339481,3.441957,1.292207,5.061175,-8.827835,1.104387,7.436544,1.039247,9.903888,-5.596941,7.559861,1.090886,5.233603,2.537958,7.531407,-2.763509,-1.513856,4.077708,-8.817040,9.188264,2.171961,9.342414,8.326651,-0.446226,7.001418,-0.237721,-2.169089,1.798312,-0.896175,4.790041,-2.155872,-3.312724,-6.051721,-8.767728,-6.346823,2.418818,-5.621077,7.859463,3.309314,-3.727452,-0.485483,-2.521017,-4.316974,-5.863860,-9.418419,7.101236,8.759531,1.593892,1.759975,-4.463131,2.893479,3.489255,-9.679889,-3.906383,5.478344,6.483503,4.809310,-6.854932,2.602643,-9.168361,-3.448517,-2.405349,8.864257,4.114809,6.258719,5.221469,-1.500046,-8.124012,9.387163,-7.642165,-3.079372,-2.590867,3.392459,3.609587,4.956126,2.786212,8.530207,9.784540,0.791966,-8.426700,-4.809698,-0.959529,-7.812035,-2.517193,7.798755,-7.854709,-9.135079,1.129128,4.200658,-1.462221,-2.617369,9.836008,5.284530,-8.140127,9.609793,3.920704,-7.012291,-3.645744,-5.879639,-5.402738,-8.368000,0.766504,5.907090,-9.104557,-7.359152,4.392072,-5.813379,-0.185425,0.071232,1.113910,9.777922,1.260298,-6.687767,4.412537,-3.851856,-8.774683,-7.390264,2.845033,-7.763109,5.479106,-0.728886,3.192859,6.816000,-7.601614,-4.852673,6.816108,-8.194032,-4.731496,6.414644,9.800654,2.156612,-9.837441,-9.658595,-6.757933,4.505052,8.494772,-1.557109]], dtype = "float32")#candidate|6991|(1, 175)|const|float32
call_6989 = relay.TupleGetItem(func_2007_call(relay.reshape(var_6990.astype('uint8'), [11, 4, 9]), relay.reshape(var_6990.astype('uint8'), [11, 4, 9]), relay.reshape(const_6991.astype('float32'), [175,]), ), 5)
call_6992 = relay.TupleGetItem(func_2011_call(relay.reshape(var_6990.astype('uint8'), [11, 4, 9]), relay.reshape(var_6990.astype('uint8'), [11, 4, 9]), relay.reshape(const_6991.astype('float32'), [175,]), ), 5)
var_7020 = relay.var("var_7020", dtype = "uint8", shape = (13, 396))#candidate|7020|(13, 396)|var|uint8
bop_7021 = relay.maximum(var_6990.astype('int64'), var_7020.astype('int64')) # shape=(13, 396)
func_3169_call = mod.get_global_var('func_3169')
func_3170_call = mutated_mod.get_global_var('func_3170')
call_7024 = relay.TupleGetItem(func_3169_call(), 0)
call_7025 = relay.TupleGetItem(func_3170_call(), 0)
uop_7048 = relay.sin(var_6990.astype('float32')) # shape=(1, 396)
output = relay.Tuple([call_6962,call_6975,call_6989,const_6991,bop_7021,call_7024,uop_7048,])
output2 = relay.Tuple([call_6963,call_6976,call_6992,const_6991,bop_7021,call_7025,uop_7048,])
func_7050 = relay.Function([var_6990,var_7020,], output)
mod['func_7050'] = func_7050
mod = relay.transform.InferType()(mod)
var_7051 = relay.var("var_7051", dtype = "uint8", shape = (1, 396))#candidate|7051|(1, 396)|var|uint8
var_7052 = relay.var("var_7052", dtype = "uint8", shape = (13, 396))#candidate|7052|(13, 396)|var|uint8
output = func_7050(var_7051,var_7052,)
func_7053 = relay.Function([var_7051,var_7052,], output)
mutated_mod['func_7053'] = func_7053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4340_call = mod.get_global_var('func_4340')
func_4341_call = mutated_mod.get_global_var('func_4341')
call_7063 = func_4340_call()
call_7064 = func_4340_call()
output = call_7063
output2 = call_7064
func_7077 = relay.Function([], output)
mod['func_7077'] = func_7077
mod = relay.transform.InferType()(mod)
mutated_mod['func_7077'] = func_7077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7077_call = mutated_mod.get_global_var('func_7077')
call_7078 = func_7077_call()
output = call_7078
func_7079 = relay.Function([], output)
mutated_mod['func_7079'] = func_7079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_7080 = relay.TupleGetItem(func_2781_call(), 0)
call_7081 = relay.TupleGetItem(func_2782_call(), 0)
output = relay.Tuple([call_7080,])
output2 = relay.Tuple([call_7081,])
func_7111 = relay.Function([], output)
mod['func_7111'] = func_7111
mod = relay.transform.InferType()(mod)
output = func_7111()
func_7112 = relay.Function([], output)
mutated_mod['func_7112'] = func_7112
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7118 = relay.var("var_7118", dtype = "float32", shape = (10, 6, 8))#candidate|7118|(10, 6, 8)|var|float32
uop_7119 = relay.log(var_7118.astype('float32')) # shape=(10, 6, 8)
var_7121 = relay.var("var_7121", dtype = "float32", shape = (10, 6, 8))#candidate|7121|(10, 6, 8)|var|float32
bop_7122 = relay.multiply(uop_7119.astype('uint64'), relay.reshape(var_7121.astype('uint64'), relay.shape_of(uop_7119))) # shape=(10, 6, 8)
func_6369_call = mod.get_global_var('func_6369')
func_6373_call = mutated_mod.get_global_var('func_6373')
const_7127 = relay.const([7.209584,-0.564308,6.300321,-6.471653,-8.352587,3.493946], dtype = "float32")#candidate|7127|(6,)|const|float32
const_7128 = relay.const(1, dtype = "uint16")#candidate|7128|()|const|uint16
call_7126 = relay.TupleGetItem(func_6369_call(relay.reshape(const_7127.astype('float32'), [6,]), relay.reshape(const_7128.astype('uint16'), []), ), 2)
call_7129 = relay.TupleGetItem(func_6373_call(relay.reshape(const_7127.astype('float32'), [6,]), relay.reshape(const_7128.astype('uint16'), []), ), 2)
uop_7132 = relay.sinh(uop_7119.astype('float64')) # shape=(10, 6, 8)
const_7140 = relay.const([[[-3.887623,-9.083783,1.828467,6.919093,-3.214435,-9.925922,4.791902,-0.414879],[-5.658363,-5.900887,-3.337747,8.758550,-1.930118,-3.507120,8.611804,5.493835],[7.947819,9.420386,5.571612,6.966005,9.037587,-4.467852,-6.112410,-9.819030],[-1.624409,-4.779351,-2.775268,6.337074,-2.158760,2.465853,7.951496,7.445374],[-1.725408,-2.512998,8.049821,7.892924,8.308879,-0.738992,5.631244,-2.807466],[9.286411,-4.329932,6.204065,0.302096,5.915820,2.515380,7.941644,6.583029]],[[2.819961,8.987360,5.102771,3.624554,1.807674,0.994671,-6.439480,-5.245823],[-4.331078,-0.885383,-0.775726,8.634142,-5.567005,6.107211,-9.252063,9.915386],[-0.393978,-8.109678,0.654513,-5.997538,5.650812,5.232082,-5.490695,-6.952232],[8.494289,-7.099784,-8.154872,0.698110,-6.526479,-5.503858,-5.539442,9.361872],[6.142956,-7.296780,5.984385,2.461481,-1.261786,9.391953,-4.115968,2.602800],[-3.388352,-9.412835,-2.946110,0.913220,-6.877973,3.844592,7.968081,8.613295]],[[-4.485678,9.322996,-9.176301,9.318381,-2.012166,6.963804,-4.439853,-3.085963],[-5.364556,1.513929,-2.370345,-8.854498,-0.826183,8.430058,-4.131244,-6.831117],[0.699373,-0.796720,-5.047629,-9.380182,-2.546109,-5.949051,6.394015,4.215516],[7.395090,-0.769439,3.038734,-7.805985,-7.159775,2.217770,-7.818125,1.253314],[-5.850599,8.276107,7.580763,2.805674,-6.508667,-8.977988,-5.088467,1.316493],[-8.660149,6.407772,-3.429231,-7.759221,-4.437357,4.763815,9.049733,-7.144692]],[[4.622649,9.155369,8.029158,-2.576633,-4.961343,5.299377,4.808968,-9.815947],[-9.964022,2.742161,2.420558,0.962745,-9.112385,-8.106993,-9.688103,0.066663],[-0.538179,-8.883538,4.042445,2.017755,-0.758820,-8.006939,-0.472026,0.615394],[-8.221983,0.826924,-0.249896,3.746925,-0.675079,3.378704,-6.900816,-6.065932],[0.479165,3.047770,9.658215,-5.777630,3.739116,8.892771,1.704222,7.627061],[-8.612485,8.018757,5.941958,6.255083,-4.229533,-7.759864,7.228764,4.581057]],[[-8.663299,6.917540,-9.513303,9.178816,-3.041824,5.088493,0.613048,2.909891],[1.478823,1.888866,-8.435247,-6.909854,5.199361,1.875922,9.653519,0.609621],[5.419330,-6.675758,-7.544597,-8.607228,-6.765311,-8.507051,-5.943539,4.508130],[-4.852342,-1.919293,6.083604,3.361753,-5.965032,4.812020,1.913071,4.921621],[4.980778,-4.811737,9.557456,-5.170279,-5.993206,6.236988,6.499304,6.245889],[4.387706,-9.624656,-6.553215,5.517715,-9.668365,8.807083,5.816938,0.665352]],[[-5.257720,-9.265348,-8.235870,5.949998,2.957203,6.366973,-9.013187,-0.611877],[-5.297239,-0.302870,-1.621756,7.895625,6.813300,7.583966,1.410660,4.768311],[-1.191668,5.967916,4.944547,-7.226019,-1.041870,5.304979,-7.502542,-1.496310],[-2.168640,2.111425,8.339351,5.491396,0.314686,1.145851,2.919839,-8.432855],[2.712348,-2.651930,4.784430,3.145851,-4.316749,-9.047660,1.921045,-8.297350],[3.854514,-1.416660,-5.673902,7.881972,-1.043698,2.099104,-0.427223,-0.896459]],[[7.803009,-5.315554,6.637571,-6.623209,-9.216147,-7.731332,-3.964907,0.568190],[-7.959846,-1.724135,9.276549,7.224417,-5.322625,-4.432527,-4.911534,-9.389361],[2.217581,-1.373237,2.382455,3.966966,2.647570,5.504295,-2.029877,-1.792157],[-9.978976,0.077206,-3.871523,-4.521013,3.178100,5.754867,2.755595,-3.950703],[-3.595659,4.586149,3.562163,2.310459,-1.378860,-0.497990,1.441271,4.668762],[2.653394,-1.045411,2.047012,9.618899,5.461094,9.570787,-7.644859,0.455676]],[[-7.327078,-0.127028,5.170872,9.902980,-5.341641,-7.925350,-3.314390,-1.390089],[7.074415,1.194936,4.985438,1.812579,-5.043842,6.539286,-0.369786,7.471073],[2.494430,4.490302,-5.288841,-9.736721,-8.608558,-0.945362,-8.656146,5.369991],[5.946112,8.404640,6.016650,6.194576,3.107177,-5.731863,-3.955131,-5.810700],[-7.703245,-5.770179,-9.774146,5.719664,-2.414858,3.957061,-3.098032,-1.176018],[-1.423996,-0.084910,-8.934529,4.610395,-1.635360,-9.007042,9.141054,-0.832405]],[[-0.901137,-6.113590,1.885854,8.973147,-0.581422,7.325847,3.130615,-2.602562],[0.419979,1.595164,6.629322,3.861045,4.391227,-2.370663,-1.395030,-9.332827],[0.400224,-1.027842,-1.266686,-8.336658,-6.579715,-4.254593,9.174378,7.194552],[6.207520,5.188825,2.216473,0.112575,-2.038662,-5.752667,-8.907313,1.013783],[6.253045,0.124611,9.553492,-9.396926,8.370708,-4.459744,-0.309942,0.427832],[-3.541637,-7.471395,2.919702,-7.887827,3.183291,-1.492723,9.596413,5.381112]],[[2.028922,7.407103,5.634965,8.566917,-5.311454,8.622946,6.058558,-0.334450],[6.298046,-7.513274,-6.741677,-1.296602,1.893253,-3.402340,-8.435105,3.192398],[-5.002359,1.919860,1.628448,-8.949955,-3.346300,-0.918420,-0.630577,7.816629],[0.121691,-6.742124,2.209600,1.240202,8.036802,9.149760,8.202503,-5.847831],[1.358802,1.498169,-9.281236,-6.222174,-9.919996,-0.033006,-0.128131,-5.756849],[9.016770,5.233350,-9.368634,1.438112,-8.085180,5.007423,-4.196388,0.021157]]], dtype = "float64")#candidate|7140|(10, 6, 8)|const|float64
bop_7141 = relay.equal(uop_7132.astype('bool'), relay.reshape(const_7140.astype('bool'), relay.shape_of(uop_7132))) # shape=(10, 6, 8)
output = relay.Tuple([bop_7122,call_7126,const_7127,const_7128,bop_7141,])
output2 = relay.Tuple([bop_7122,call_7129,const_7127,const_7128,bop_7141,])
func_7147 = relay.Function([var_7118,var_7121,], output)
mod['func_7147'] = func_7147
mod = relay.transform.InferType()(mod)
var_7148 = relay.var("var_7148", dtype = "float32", shape = (10, 6, 8))#candidate|7148|(10, 6, 8)|var|float32
var_7149 = relay.var("var_7149", dtype = "float32", shape = (10, 6, 8))#candidate|7149|(10, 6, 8)|var|float32
output = func_7147(var_7148,var_7149,)
func_7150 = relay.Function([var_7148,var_7149,], output)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4851_call = mod.get_global_var('func_4851')
func_4852_call = mutated_mod.get_global_var('func_4852')
call_7203 = relay.TupleGetItem(func_4851_call(), 0)
call_7204 = relay.TupleGetItem(func_4852_call(), 0)
output = call_7203
output2 = call_7204
func_7216 = relay.Function([], output)
mod['func_7216'] = func_7216
mod = relay.transform.InferType()(mod)
output = func_7216()
func_7217 = relay.Function([], output)
mutated_mod['func_7217'] = func_7217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6495_call = mod.get_global_var('func_6495')
func_6496_call = mutated_mod.get_global_var('func_6496')
call_7247 = relay.TupleGetItem(func_6495_call(), 1)
call_7248 = relay.TupleGetItem(func_6496_call(), 1)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
const_7250 = relay.const([[-1.728026,5.736747,-1.955766,7.153717,9.809884,8.297287,-3.770315,2.451126,-6.933845,3.395814,6.927829,3.603291,-7.987283,-2.586082,4.590903,-5.563780,-6.992650,1.102912,-4.861701,-8.819836,-4.585942,-8.606539,5.955394,2.485476,2.960877,-1.764017,7.146717,-2.538079,-0.930298,-7.063173,6.039979,8.319118,-9.627639,-2.500660,-8.509988,0.333616,-5.695355,4.936122,1.793868,-7.868040,-2.401195,0.910934,-0.266568,8.950188,-3.437197,3.392533,-3.038550,7.690465]], dtype = "float32")#candidate|7250|(1, 48)|const|float32
call_7249 = relay.TupleGetItem(func_4522_call(relay.reshape(const_7250.astype('float32'), [12, 1, 4])), 0)
call_7251 = relay.TupleGetItem(func_4524_call(relay.reshape(const_7250.astype('float32'), [12, 1, 4])), 0)
func_3538_call = mod.get_global_var('func_3538')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_7255 = func_3538_call()
call_7256 = func_3538_call()
output = relay.Tuple([call_7247,call_7249,const_7250,call_7255,])
output2 = relay.Tuple([call_7248,call_7251,const_7250,call_7256,])
func_7261 = relay.Function([], output)
mod['func_7261'] = func_7261
mod = relay.transform.InferType()(mod)
output = func_7261()
func_7262 = relay.Function([], output)
mutated_mod['func_7262'] = func_7262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6056_call = mod.get_global_var('func_6056')
func_6058_call = mutated_mod.get_global_var('func_6058')
call_7268 = func_6056_call()
call_7269 = func_6056_call()
func_4942_call = mod.get_global_var('func_4942')
func_4943_call = mutated_mod.get_global_var('func_4943')
call_7278 = relay.TupleGetItem(func_4942_call(), 0)
call_7279 = relay.TupleGetItem(func_4943_call(), 0)
output = relay.Tuple([call_7268,call_7278,])
output2 = relay.Tuple([call_7269,call_7279,])
func_7286 = relay.Function([], output)
mod['func_7286'] = func_7286
mod = relay.transform.InferType()(mod)
mutated_mod['func_7286'] = func_7286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7286_call = mutated_mod.get_global_var('func_7286')
call_7287 = func_7286_call()
output = call_7287
func_7288 = relay.Function([], output)
mutated_mod['func_7288'] = func_7288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_7304 = func_3060_call()
call_7305 = func_3060_call()
func_5020_call = mod.get_global_var('func_5020')
func_5022_call = mutated_mod.get_global_var('func_5022')
const_7314 = relay.const([[-9],[7],[4],[-5],[-2],[-1],[9],[6],[-6],[6],[3],[10],[5],[3],[5],[10],[-4],[8],[-4],[-5],[9],[-9],[-4],[10],[1],[-5],[5],[2],[-7],[8],[8],[6],[7],[-2],[-6],[7],[2],[6],[1],[8],[-5],[8],[8],[-1],[-5],[-9],[-9],[3],[-8],[6],[1],[-9],[-9],[1],[-2],[-4],[1],[8],[2],[-4],[-10],[-7],[7],[-6],[-6],[-7],[6],[-2],[-1],[-5],[-1],[2],[10],[1],[1],[10],[10],[2],[-1],[2],[-9],[-4],[5],[9],[10],[-8],[2],[-5],[2],[-8],[-3],[4],[-8],[-1],[-3],[4],[-2],[-8],[-8],[-2],[1],[-1],[2],[9],[4],[-6],[-6],[10],[-5],[10],[-6],[3],[-7],[-6],[7],[3],[-9],[-5],[10],[6],[-1],[-1],[-3],[8],[-6],[7],[5],[1],[-10],[-6],[6],[-7],[6],[8],[5],[-10],[-4],[-3],[5],[-6],[-2],[-4],[-4],[10],[5],[-1],[7],[-6],[1],[9],[-5],[2],[1],[8],[-7],[-9],[-9],[7],[-2],[-7],[2],[6],[9],[10],[-5],[6],[7],[3],[1],[8],[-8],[-6],[-1],[-10],[7],[10],[7],[-9],[-9],[6],[8],[-5],[-8],[-7],[-2],[9],[-1],[6],[-8],[-7],[-6],[-6],[-2],[-9],[6],[2],[-7],[-2],[-7],[-6],[-3],[6],[-1],[-8],[-1],[-6],[9],[-1],[-9],[-9],[-8],[-10],[1],[-10],[1],[5],[2],[-8],[6],[-10],[10],[-5],[9],[9],[10],[2],[10],[-3],[-4],[-9],[-10],[10],[6],[2],[5],[-10],[-9],[-3],[2],[-6],[-1],[-10],[-10],[4],[-5],[-10],[-5],[-6],[-10],[2],[4],[10],[6],[-2],[7],[-3],[-6],[-1],[-8],[-4],[-8],[-10],[7],[-4],[6],[-10],[-8],[2],[6],[-6],[-3],[1],[-6],[8],[9],[-6],[6],[-8],[4],[10],[9],[-8],[10],[5],[-5],[-9],[2],[8],[6],[9],[-9],[10],[5],[-8],[1],[-6],[-8],[9],[4],[8],[-5],[-8],[8],[-4],[-3],[10],[9],[7],[10],[-10],[-5],[-3],[-9],[-3],[-8],[-2],[7],[-1],[-5],[1],[-7],[-10],[-3],[-10],[-4],[5],[-9],[2],[-5],[-2],[-5],[8],[-2],[1],[4],[-5],[-5],[9],[4],[2],[-2],[-5],[5],[8],[2],[3],[-4],[-3],[1],[-6],[-8],[-8],[-8],[2],[6],[7],[-10],[8],[10],[7],[8],[1],[-2],[8],[10],[8],[7],[-10],[3],[-4],[-3],[9],[-5],[-1],[5],[-9],[6],[6],[-6],[-1],[10],[-2],[-5],[9],[-4],[7],[6],[-1],[2],[-8],[-9],[-1],[6],[-3],[4],[7],[-3],[-9],[1],[4],[-3],[-3],[6],[-1],[-7],[7],[-5],[1],[8],[2],[-9],[-5],[7],[-1],[-4],[-4],[-8],[7],[10],[-2],[9],[2],[-10],[5],[-8],[9],[7],[-10],[-8],[5],[-5],[-8],[-5],[-5],[-4],[-3],[-8],[7],[10],[3],[1],[3],[-8],[4],[-1],[-7],[-9],[9],[1],[-10],[-3],[-6],[-10],[7],[4],[-5],[-6],[3],[-1],[-9],[8],[-3],[2],[-1],[-6],[-7],[-6],[1],[9],[5],[2],[10],[-10],[1],[2],[8],[-7],[-6],[-10],[3],[10],[8],[7],[1],[9],[-9],[7],[8],[-2],[1],[-6],[-1],[7],[-1],[4],[7],[-6],[-9],[6],[8],[7],[-4],[-7],[-4],[-9],[3],[3],[10],[3],[8],[-5],[-3],[-2],[5],[6],[3],[1],[10],[10],[-8],[-6],[-6],[-7],[10],[8],[-9],[-5],[-6],[-7],[-6],[4],[-6],[7],[-6],[-7],[-7],[5],[5],[-10],[2],[-3],[4],[3],[8],[3],[-3],[-3],[4],[5],[6],[4],[9],[9],[-1],[-7],[8],[4],[-1],[-2],[-7],[4],[1],[-8],[-7],[5],[-7],[9],[8],[7],[6],[10],[7],[5],[-1],[8],[-1],[-9],[-2],[-9],[10],[-4],[-3],[-2],[-2],[10],[-5],[1],[-6],[-2],[7],[-6],[-4],[3],[2],[7],[-6],[-8],[6],[1],[10],[-6],[-2],[9],[-7],[-7],[-2],[-3],[8],[4],[-5],[-1],[-4],[1],[-10],[7],[-4],[7],[10],[-5],[8],[1],[3],[-10],[-7],[-10],[-7],[-7],[-1],[-10],[1],[-4],[-10],[10],[-8],[9],[7],[8],[2],[-2],[4],[3],[-2],[-10],[-9],[7],[-8],[4],[2],[8],[-10],[-6],[6],[8],[1],[7],[9],[-7],[-10],[-7],[7],[-8],[5],[-3],[-9],[4],[7],[-8],[-3],[-1],[6],[2],[-7],[8],[5],[-6],[-9],[7],[10],[10],[-2],[-1],[-6],[4],[-5],[6],[2],[-9],[-6],[-8],[-4],[1],[-1],[-9],[10],[-10],[-4],[1],[-10],[-9],[-7],[-10],[-2],[10],[8],[7],[4],[-7],[-8],[-6],[4],[1],[7],[-7],[-5],[5],[1],[3],[-2],[1],[2],[-2],[-8],[1],[-5],[-6],[-5],[6],[7],[10],[-10],[-5],[10],[-4],[2],[-4],[3],[-1],[7],[9],[-9],[1],[-10],[-5],[-2],[10],[-1],[5],[-3],[-4],[6],[9],[6],[-2],[-2],[-2],[-4],[2],[-2],[2],[1],[6],[-6],[-3],[-9],[6],[-7],[-5],[-7],[-5],[-8],[7],[-2],[9],[-7],[7],[-2],[1],[-3],[-9],[-3],[10],[-1],[4],[-3],[-6],[-8],[4],[-3],[3],[3],[-9],[-3],[5],[5],[2],[8],[-10],[8],[7],[-3],[-2],[-6],[-10],[-1],[-1],[10],[-9],[10],[-1],[-7],[-7],[-5],[-4],[-10],[-4],[-3],[-5],[-5],[2],[-5],[10],[2],[-10],[-5],[-9],[2],[-9],[-2],[-9],[5],[-9],[-2],[-9],[-7],[-4],[-3],[8],[6],[-10],[-9],[-5],[-5],[-9],[9],[-3],[-3],[-3],[5],[3],[3],[4],[4],[3],[-10],[-2],[2],[-1],[4],[-5],[-9],[-7],[9],[9],[-2],[-5],[4],[2],[9],[-7],[-8],[9],[8],[6],[9],[-5],[10],[-1],[2],[2],[-4],[10],[6],[5],[9],[6],[3],[-7],[5],[-3],[5],[-3],[9],[-5],[-5],[4],[5],[9],[-10],[-7],[-8],[-6],[8],[4],[-7],[10],[-6],[-8],[-8],[-8],[1],[4],[8],[5],[10],[6],[-5],[-1],[-8],[-10],[1],[-8],[2],[3],[-2],[-3],[-3],[-6],[2],[10],[3],[2],[-10],[3],[-9],[2],[3],[-8],[-9],[-5],[4],[-1],[4],[-9],[-9],[10],[4],[-2],[-8],[-10],[-9],[8],[4],[7],[9],[-2],[9],[-9],[1],[1],[8],[1],[-7],[6],[-9],[-2],[-1],[-10],[-10],[-8],[-8],[-1],[6],[-10],[-9],[-8],[-2],[9],[-4],[-5],[-3],[1],[1],[1],[-8],[-10],[3],[-3],[-3],[-7],[-4],[1],[8],[7],[7],[4],[3],[6],[-9],[-5],[7],[-3],[-7],[1],[-9],[-6],[5],[-1],[9],[4],[-2],[-6],[8],[-8],[10],[-3],[-7],[9],[-3],[5],[9],[5],[9],[9],[-1],[-4],[3],[-7],[3],[-7],[-7],[1],[-5],[1],[3],[7],[9],[7],[7],[-6],[9],[1],[-9],[3],[4],[-6],[-10],[-8],[-9],[2],[4],[3],[-3],[-1],[-6],[-9],[8],[-9],[8],[10],[1],[4],[5],[6],[-10],[-6],[-10],[-10],[-1],[3],[10],[4],[-2],[5],[-4],[4],[3],[9],[-4],[1],[-7],[-10],[10],[-2],[-1],[-10],[-7],[-6],[-9],[10],[8],[-1],[6],[8],[-8],[3],[8],[2],[3],[10],[-9],[2],[-7],[4],[1],[-9],[2],[9],[-1],[7],[4],[5],[-5],[-3],[-9],[2],[-3],[3],[-5],[8],[-2],[7],[9],[9],[1],[-1],[8],[-8],[-1],[1],[3],[-7],[10],[-10],[6],[2],[-7],[10],[-3],[7],[-9],[-8],[2],[-9],[-8],[-4],[-6],[9],[10],[10],[7],[4],[1],[9],[-4],[-7],[-5],[-9],[-4],[2],[1],[-4],[9],[-4],[5],[5],[-5],[6],[-2],[9],[3],[7],[2],[7],[-4],[-7],[6],[-5],[-7],[2],[-2],[3],[-5],[-3],[-6],[-2],[-8],[-7],[5],[-8],[4],[8],[-9],[3],[-10],[7],[3],[9],[-1],[-6],[5],[-7],[5],[7],[7],[-10],[9],[1],[9],[-3],[2],[-2],[1],[4],[4],[-10],[5],[5],[-1],[-1],[6],[-3],[9],[4],[-9],[-10],[-8],[-5],[-4],[5],[-8],[8],[-2],[7],[-3],[-6],[-2],[-5],[-3],[1],[-7],[-3],[3],[-6],[-7],[-4],[7],[2],[5],[7],[-10],[9],[1],[2],[-3],[6],[-6],[-7],[-6],[-4],[5],[2],[10],[-1],[3],[-2],[-10],[4],[-5],[7],[-1],[-9],[1],[6],[8],[-2],[9],[-5],[8],[-3],[4],[6],[8],[-9],[-8],[2],[9],[-8],[5],[10],[5],[-6],[-6],[3],[-7],[-6],[4],[6],[4],[7],[-2],[-3],[10],[3],[-7],[-1],[-7],[-7],[8],[-8],[8],[7],[-8],[4],[-10],[5],[-9],[5],[4],[-7],[3],[5],[6],[2],[4],[10],[-5],[-2],[10],[6],[6],[-4],[-4],[6],[-6],[-8],[10],[-8],[7],[-10],[-7],[-3],[-7],[-5],[2],[9],[-5],[-4],[-3],[-8],[3],[8],[9],[-10],[6],[-7],[2],[5],[-6],[6],[-4],[-5],[9],[1],[-10],[-1],[-4],[8],[6],[2],[-10],[5],[9],[-1],[2],[3],[4],[8],[-9],[-5],[5],[4],[8],[-3],[-10],[8],[-3],[9],[-7],[-9],[8],[7],[-1],[-7],[-4],[-9],[-10],[-10],[-5],[-7],[-9],[-4],[-10],[-6],[-5],[-5],[8],[5],[9],[-10],[-6],[-5],[6],[-7],[10],[5],[-10],[2],[3],[-6],[5],[-1],[5],[4],[10],[8],[7],[-2],[-9],[-3],[4],[-8],[8],[-4],[-8],[-9],[-2],[-7],[6],[3],[-7],[2],[4],[-4],[-5],[-4],[4],[5],[10],[3],[10],[2],[-2],[-10],[-2],[6],[4],[3],[4],[-3],[-4],[-9],[-6],[2],[-2],[3],[-7],[-5],[-6],[9],[8],[7],[-5],[-9],[8],[7],[-8],[-4],[-1],[-2],[1],[8],[-2],[1],[7],[-6],[-7],[-6],[3],[-1],[-9],[5],[-7],[6],[5],[-2],[3],[8],[-2],[-3],[-9],[4],[10],[-8],[5],[-4],[-8],[-6],[7],[-2],[7],[-1],[-5],[-6],[-8],[-5],[-6],[2],[-7],[8],[8],[10],[2],[10],[5],[-2],[-5],[5],[-9],[-6],[-9],[-3],[8],[-4],[-8],[8],[-6],[-1],[-4],[6],[2],[-4],[-8],[-8],[1],[6],[-4],[7],[-6],[8],[-3],[9],[7],[-8],[2],[2],[1],[-2],[4],[-9],[-5],[5],[6],[3],[2],[6],[-10],[-5],[-9],[-7],[6],[-7],[-5],[7],[3],[6],[-1],[-7],[-4],[-8],[4],[2],[-1],[10],[-1],[-2],[-8],[3],[2],[-7],[-5],[2],[6],[2],[-2],[6],[4],[-9],[-6],[-8],[-7],[3],[3],[-9],[7],[-9],[8],[10],[-1],[-4],[3],[-8],[-10],[6],[5],[3],[4],[7],[4],[-2],[1],[5],[3],[5],[-6],[-8],[9],[-7],[-2],[-4],[-5],[-8],[7],[-8],[-3],[-3],[-4],[-6],[-2],[2],[10],[-8],[-5],[-7],[-8],[-5],[-2],[-3],[10],[9],[2],[8],[8],[2],[4],[9],[-3],[4],[-4],[4],[-4],[2],[-3],[4],[-6],[7],[-4],[-5],[-8],[4],[10],[-8],[2],[10],[5],[-7],[-2],[6],[6],[9],[2],[4],[-10],[8],[-8],[1],[-8],[1],[-3],[8],[-5],[-8],[8],[4],[-3],[-7],[-10],[10],[-10],[7],[-3],[-5],[9],[4],[7],[3],[-9],[-2],[-4],[-10],[-3],[3],[8],[3],[-4],[-3],[9],[1],[-4],[-4],[-9],[6],[8],[4],[6],[1],[2],[3],[9],[-7],[6],[-3],[10],[7],[-9],[8],[7],[-7],[-3],[7],[6],[1],[3],[-10],[-1],[7],[-7],[-4],[-6],[-2],[1],[-4],[-3],[3],[3],[-5],[9],[-9],[-1],[-9],[3],[10],[8],[-8],[7],[1],[9],[8],[6],[10],[-3],[-10],[-3],[9],[7],[-4],[3],[2],[-8],[-6],[-2],[4],[-2],[-3],[-4],[-10],[10],[-1],[9],[4],[-7],[-6],[-4],[2],[1],[-8],[-6],[-4],[5],[-9],[-2],[5],[-10],[-2],[-10],[5],[-7],[-8],[3],[5],[-9],[-7],[-7],[3],[8],[-10],[10],[-2],[-6],[9],[3],[1],[-9],[2],[-10],[-6],[-2],[-4],[-3],[1],[-7],[-2],[6],[9],[-8],[-6],[-6],[-10],[-8],[7],[-9],[-9],[-5],[2],[-7],[9],[-3],[3],[5],[-3],[-2],[-6],[10],[3],[8],[7],[2],[-10],[6],[7],[6],[9],[7],[1],[8],[8],[5],[-10],[10],[2],[-5],[5],[5],[-6],[-9],[8],[9],[5],[3],[-1],[-1],[1],[-3],[-10],[6],[10],[1],[9],[-3],[10],[-10],[-9],[8],[-6],[-1],[-10],[-5],[8],[-3],[8],[-10],[-9],[4],[-8],[-4],[2],[9],[-2],[5],[-7],[-4],[1],[-9],[-5],[7],[2],[-4],[8],[-2],[6],[7],[2],[9],[-4],[-4],[3],[10],[-7],[-2],[3],[-8],[7],[-9],[-1],[-3],[7],[-6],[9],[-2],[10],[-6],[4],[-8],[8],[5],[-1],[8],[6],[-5],[8],[-5],[2],[-3],[7],[-6],[3],[-1],[-1],[-8],[-8],[10],[-8],[9],[8],[5],[6],[1],[1],[8],[9],[-6],[-5],[9],[-3],[5],[-4],[5],[5],[-9],[10],[9],[4],[-3],[-3],[-5],[-5],[7],[8],[-8],[-7],[-4],[-7],[-2],[-3],[-7],[5],[-8],[-7],[-3],[1],[3],[9],[-8],[7],[7],[6],[-4],[10],[-9],[-9],[7],[-4],[10],[-7],[-2],[-1],[6],[6],[-4],[-7],[-9],[-2],[-8],[-1],[7],[-5],[3],[-1],[-3],[-7],[9],[-1],[-7],[-9],[1],[4],[9],[-5],[2],[5],[-5],[6],[-2],[-2],[-9],[9],[9],[3],[8],[-9],[-5],[1],[10],[-2],[1],[4],[10],[5],[-8],[6],[-7],[5],[6],[2],[-9],[-2],[-5],[-10],[-10],[-9],[-4],[8],[-2],[-5],[-1],[-10],[-7],[-6],[5],[6],[8],[-10],[-3],[-8],[-5],[-4],[10],[2],[-5],[4],[1],[8],[-1],[2],[10],[-1],[7],[1],[-2],[-3],[-4],[7],[-8],[-7],[9],[3],[-7],[7],[-3],[5],[-6],[-4],[-8],[3],[2],[8],[-2],[1],[5],[5],[9],[-1],[6],[6],[8],[5],[-10],[6],[-1],[-7],[-6],[10],[-9],[10],[-1],[7],[10],[8],[-9],[-7],[10],[10],[8],[7],[7],[-4],[-6],[-3],[-7],[10],[-7],[-10],[6],[-2],[6],[1],[-1],[5],[6],[-1],[-3],[-8],[-1],[-7],[-3],[8],[3],[-6],[10],[5],[9],[-2],[-6],[-4],[-7],[7],[-9],[-3],[5],[1],[-5],[9],[-1],[-1],[5],[6],[4],[6],[5],[2],[4],[3],[4],[6],[-6],[-9],[-9],[10],[-3],[10],[-9],[-2],[4],[-2],[-8],[2],[6],[7],[-3],[-9],[-1],[-9],[9],[10],[-2],[-10],[5],[-5],[9],[-10],[4],[1],[7],[-7],[-3],[7],[-9],[6],[-8],[9],[-5],[3],[10],[10],[5],[-8],[-2],[-6],[9],[9],[-4],[-5],[5],[-10],[-8],[-4],[-6],[4],[7],[7],[6],[1],[-4],[-6],[4],[4],[4],[-2],[3],[-1],[-1],[-3],[-4],[-4],[2],[4],[-5],[-5],[4],[2],[9],[-8],[5],[1],[10],[-8],[-8],[7],[-7],[4],[-2],[-7],[-3],[-6],[4],[-7],[-3],[-5],[2],[8],[-9],[-4],[-7],[-1],[-4],[4],[-5],[-3],[-3],[-7],[8],[-9],[6],[-1],[9],[2],[-6],[-5],[9],[-7],[-4],[7],[4],[-8],[-10],[4],[-9],[-8],[7],[5],[7],[-6],[-4],[-5],[-8],[6],[-7],[-1],[-4],[8],[4],[-1],[-6],[-7],[-6],[-1],[-10],[7],[-9],[-8],[7],[8],[8],[5],[-8],[5],[6],[6],[5],[-7],[6],[8],[-6],[-1],[-7],[3],[-5],[-10],[-10],[-5],[1],[-2],[-8],[-8],[-2],[5],[-4],[5],[8],[-6],[-6],[-3],[-8],[4],[-9],[8],[-8],[6],[7],[-6],[1],[-8],[-6],[5],[-8],[1],[10],[5],[-6],[-7],[7],[-4],[6],[-9],[-5],[3],[-8],[-1],[1],[-8],[-6],[4],[-4],[3],[-9],[6],[8],[9],[1],[-8],[-2],[-2],[-1],[5],[-8],[-2],[4],[2],[9],[10],[8],[4],[-8],[-9],[-10],[3],[7],[4],[-8],[-9],[-6],[3],[-8],[-9],[-2],[5],[-5],[-7],[3],[-9],[-2],[-8],[-10],[6],[-3],[-6],[-7],[10],[4],[4],[-6],[-8],[-9],[3],[-3],[-6],[-9],[-6],[7],[8],[-1],[1],[-3],[-5],[8],[-5],[-10],[7],[-9],[1],[5],[9],[-10],[-4],[8],[-8],[-8],[7],[8],[10],[-3],[2],[9],[-1],[10],[-2],[-9],[-10],[7],[7],[7],[4],[-4],[7],[-5],[8],[4],[-9],[7],[-1],[4],[-5],[-6],[6],[-10],[9],[-10],[-5],[4],[-4],[10],[6],[10],[-5],[7],[-8],[-3],[6],[8],[1],[4],[-7],[2],[9],[-3],[6],[-5],[-7],[8],[-5],[-10],[-4],[4],[2],[-1],[-9],[-2],[-1],[8],[2],[-1],[7],[9],[-2],[-6],[1],[-10],[10],[-6],[-5],[5],[4],[-8],[-2],[3],[10],[-2],[-1],[-8],[7],[-1]], dtype = "uint16")#candidate|7314|(2560, 1)|const|uint16
call_7313 = relay.TupleGetItem(func_5020_call(relay.reshape(const_7314.astype('uint16'), [2560,])), 0)
call_7315 = relay.TupleGetItem(func_5022_call(relay.reshape(const_7314.astype('uint16'), [2560,])), 0)
var_7316 = relay.var("var_7316", dtype = "uint16", shape = (2560, 15))#candidate|7316|(2560, 15)|var|uint16
bop_7317 = relay.subtract(const_7314.astype('uint8'), var_7316.astype('uint8')) # shape=(2560, 15)
output = relay.Tuple([call_7304,call_7313,bop_7317,])
output2 = relay.Tuple([call_7305,call_7315,bop_7317,])
func_7324 = relay.Function([var_7316,], output)
mod['func_7324'] = func_7324
mod = relay.transform.InferType()(mod)
var_7325 = relay.var("var_7325", dtype = "uint16", shape = (2560, 15))#candidate|7325|(2560, 15)|var|uint16
output = func_7324(var_7325)
func_7326 = relay.Function([var_7325], output)
mutated_mod['func_7326'] = func_7326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5982_call = mod.get_global_var('func_5982')
func_5983_call = mutated_mod.get_global_var('func_5983')
call_7332 = func_5982_call()
call_7333 = func_5982_call()
output = relay.Tuple([call_7332,])
output2 = relay.Tuple([call_7333,])
func_7337 = relay.Function([], output)
mod['func_7337'] = func_7337
mod = relay.transform.InferType()(mod)
mutated_mod['func_7337'] = func_7337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7337_call = mutated_mod.get_global_var('func_7337')
call_7338 = func_7337_call()
output = call_7338
func_7339 = relay.Function([], output)
mutated_mod['func_7339'] = func_7339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5982_call = mod.get_global_var('func_5982')
func_5983_call = mutated_mod.get_global_var('func_5983')
call_7481 = func_5982_call()
call_7482 = func_5982_call()
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
var_7487 = relay.var("var_7487", dtype = "bool", shape = (819,))#candidate|7487|(819,)|var|bool
call_7486 = relay.TupleGetItem(func_47_call(relay.reshape(var_7487.astype('bool'), [13, 9, 7])), 1)
call_7488 = relay.TupleGetItem(func_50_call(relay.reshape(var_7487.astype('bool'), [13, 9, 7])), 1)
output = relay.Tuple([call_7481,call_7486,var_7487,])
output2 = relay.Tuple([call_7482,call_7488,var_7487,])
func_7491 = relay.Function([var_7487,], output)
mod['func_7491'] = func_7491
mod = relay.transform.InferType()(mod)
mutated_mod['func_7491'] = func_7491
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7492 = relay.var("var_7492", dtype = "bool", shape = (819,))#candidate|7492|(819,)|var|bool
func_7491_call = mutated_mod.get_global_var('func_7491')
call_7493 = func_7491_call(var_7492)
output = call_7493
func_7494 = relay.Function([var_7492], output)
mutated_mod['func_7494'] = func_7494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4851_call = mod.get_global_var('func_4851')
func_4852_call = mutated_mod.get_global_var('func_4852')
call_7498 = relay.TupleGetItem(func_4851_call(), 0)
call_7499 = relay.TupleGetItem(func_4852_call(), 0)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_7528 = relay.TupleGetItem(func_2152_call(), 0)
call_7529 = relay.TupleGetItem(func_2154_call(), 0)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_7530 = func_2649_call()
call_7531 = func_2649_call()
output = relay.Tuple([call_7498,call_7528,call_7530,])
output2 = relay.Tuple([call_7499,call_7529,call_7531,])
func_7562 = relay.Function([], output)
mod['func_7562'] = func_7562
mod = relay.transform.InferType()(mod)
mutated_mod['func_7562'] = func_7562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7562_call = mutated_mod.get_global_var('func_7562')
call_7563 = func_7562_call()
output = call_7563
func_7564 = relay.Function([], output)
mutated_mod['func_7564'] = func_7564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7337_call = mod.get_global_var('func_7337')
func_7339_call = mutated_mod.get_global_var('func_7339')
call_7585 = relay.TupleGetItem(func_7337_call(), 0)
call_7586 = relay.TupleGetItem(func_7339_call(), 0)
output = call_7585
output2 = call_7586
func_7603 = relay.Function([], output)
mod['func_7603'] = func_7603
mod = relay.transform.InferType()(mod)
mutated_mod['func_7603'] = func_7603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7603_call = mutated_mod.get_global_var('func_7603')
call_7604 = func_7603_call()
output = call_7604
func_7605 = relay.Function([], output)
mutated_mod['func_7605'] = func_7605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4207_call = mod.get_global_var('func_4207')
func_4209_call = mutated_mod.get_global_var('func_4209')
call_7621 = relay.TupleGetItem(func_4207_call(), 1)
call_7622 = relay.TupleGetItem(func_4209_call(), 1)
output = relay.Tuple([call_7621,])
output2 = relay.Tuple([call_7622,])
func_7625 = relay.Function([], output)
mod['func_7625'] = func_7625
mod = relay.transform.InferType()(mod)
mutated_mod['func_7625'] = func_7625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7625_call = mutated_mod.get_global_var('func_7625')
call_7626 = func_7625_call()
output = call_7626
func_7627 = relay.Function([], output)
mutated_mod['func_7627'] = func_7627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4340_call = mod.get_global_var('func_4340')
func_4341_call = mutated_mod.get_global_var('func_4341')
call_7669 = func_4340_call()
call_7670 = func_4340_call()
func_2833_call = mod.get_global_var('func_2833')
func_2835_call = mutated_mod.get_global_var('func_2835')
const_7674 = relay.const([7,-8,2,10,-9,4,-7,-1,5,-6,1,-1,-4,-3,5,8,7,-1,-3,-2,5,8,9,8,-9,7,6,8,-5,8,4,2,-5,-10,-3,1,-10,-2,8,3,6,1,5,9,-10,-10,4,6,4,-8,-10,-6,7,7,10,7,9,-8,-7,6,6,2,9,-1,-3,1,7,-4,-5,-2,-3,3,-4,8,-9,-7,-10,9,6,-2,9,4,1,2,1,5,10,-7,10,-6,-10,6,-3,-1,4,-1,9,1,-5,7,5,-1,-1,-9,-4,10,1,7,-10,4,6,-9,1,6,-4,-2,-7,6,-1,-7,-4,-2,4,9,-2,7,8,-2,9,7,-10,-4,1,-5,7,-1,10,5,5,-7,7,-2,4,-6,-3,-8,-1,2,-2,-8,2,1,-3,7,10,-4,9,-4,1,6,2,-6,6,-6,-6,9,-4,-9,5,-4,9,-2,3,9,-7,-7,-1,-3,-1,-5,-5,-3,3,5,-8,-4,8,-3,-3,6,-9,8,-6,-7,2,-3,4,-6,-8,6,-10,10,6,1,-8,-7,10,9,8,2,-5,7,-3,-6,-3,-8,1,-3,3,-4,10,8,-1,-5,-2,-1,4,-4,-2,-9,-3,10,-4,10,-4,8,10,-4,-4,1,6,3,-3,-10,-9,10,5,-7,2,8,-6,9,-6,-8,-2,8,-1,1,-8,-9,-9,1,8,4,-7,-5,1,-8,1,-1,5,2,-10,1,3,7,8,7,-5,-7,3,5,10,-5,9,3,-5,1,-9,5,2,-5,9,-10,2,9,1,-1,9,-1,2,-4,8,-2,8,10,-1,-2,-6,-7,10,-4,-9,-4,-1,-7,-9,-9,6,6,3,4,3,-4,-8,7,-8,1,-6,-6,-9,9,5,7,-3,7,-2,-10,7,-4,-5,-3,10,10,10,-2,-2,9,2,1,10,1,-9,7,-5,10,-9,-4,-8,6,2,-7,10,-4,-1,-8,-2,-4,-10,-4,-1,-6,7,1,6,-5,7,5,-7,10,3,-10,-8,4,7,-4,4,9,4,9,7,-10,-6,-4,5,1,-3,-5,-7,-9,-8,-3,5,-4,-3,-8,-8,7,-5,-7,4,-10,-10,5,5,4,-9,6,2,-2,6,5,8,8,-4,4,2,2,1,3,-3,9,-5,-5,-4,2,-7,-4,1,-8,6,3,-8,-1,-4,4,1,-9,-8,-5,-3,2,4,-5,-9,-1,5,-2,9,-3,-8,-10,2,-9,-6,-3,-9,-9,3,9,-6,-7,-4,-5,2,4,9,-3,5,-1,4,2,-1,10,6,5,2,5,1,-9,-10,-7,8,1,-1,6,6,-3,-2,8,2,10,-7,10,-4,3,3,-4,9,4,-8,7,10,-1,-3,-10,4,1,-2,-9,1,2,-9,2,-4,10,-9,-5,9,1,5,-10,-1,2,1,2,3,-5,2,2,4,-7,-3,1,-10,-5,-6,-8,6,-10,1,-1,8,7,-1,-4,-3,9,-7,9,5,-4,8,7,10,-5,1,-3,9,-9,-1,9,-5,-9,9,8,1,-4,-4,7,10,4,5,2,-9,8,3,-3,6,-1,-9,10,2,3,6,-9,9,10,1,1,1,8,-7,-2,-3,9,-3,4,-2,1,-6,-4,2,-10,-6,-2,2,-2,-1,3,9,-9,-10,8,-9,-10,7,-1,-10,3,4,2,5,5,8,3,-10,10,7,-2,4,3,-7,-2,5,-2,1,3,8,6,-5,-3,-1,-5,-10,-5,10,-6,2,4,3,6,-10,2,6,3,-6,8,-9,6,-9,-6,10,-6,1,-10,5,-10,5,-2,7,4,-4,-1,-5,-4,7,-3,-3,-9,-10,9,-5,2,-1,2,-2,1,7,10,-8,-8,4,4,-10,-2,-4,-8,1,8,6,10,-6,-3,3,-7,-8,8,6,-1,-4,9,-7,-6,6,-10,4,10,1,5,7,-8,4,-10,7,9,6,9,4,10,9,-2,-2,-5,6,-8,1,-9,-2,-7,10,-10,3,-10,5,7,-1,-9,3,-7,-5,3,3,-2,3,-3,7,-1,-1,9,2,9,7,8,5,9,10,-7,4,-7,-1,9,-4,-8,1,10,-3,9,-1,10,-2,-6,-10,7,-2,-8,7,-1,-10,-5,-6,4,-7,1,-10,6,9,6,4,-1,2,-9,1,-9,1,-9,10,-8,6,7,-8,10,4,7,3,-6,9,1,7,10,5,-5,-3,-4,-10,-7,-3,-8,-4,6,-4,10,10,-5,5,-7,5,5,-4,-8,-1,7,-3,4,-1,-5,-5,-2,10,3,3,6,-3,7,-4,-6,-2,-1,-9,2,-5,6,-6,6,6,-3,-1,-8,-2,4,9,-2,-2,-6,8,-10,7,-7,-6,8,4,2,10,2,6,9,5,-8,4,5,-2,-7,2,-1,-6,-2,-2,-6,8,-6,1,2,5,-2,-4,1,3,-6,-1,-7,7,7,-6,2,10,-10,3,8,10,7,8,-9,-7,8,-1,6,6,9,-8,-8,1,1,10,2,-1,3,8,-10,8,-4,5,-10,7,5,-2,-8,-10,7,-10,9,7,-1,-7,-1,-3,7,8,10,-7,-3,-9,10,-9,9,-5,1,4,8,-4,-8,5,-4,-1,8,-1,-6,9,-10,-4,-8,-1,2,2,7,-8,-3,-10,-6,3,-10,-5,3,-6,-2,3,-1,2,10,-5,10,-3,8,1,-6,-8,-9,7,-6,-6,-5,-10,-3,-10,-6,1,-8,-10,10,10,6,-4,-8,-6,6,-3,-10,7,-5,8,4,9,6,10,-9,-1,8,-9,-8,1,6,5,10,1,1,-9,1,-6,-5,2,-7,-10,-10,-1,3,-2,-7,7,9,3,9,4,7,-6,6,-8,-3,-6,-5,-1,9,1,2,-3,8,-2,7,-7,-6,9,-3,5,-5,-6,7,1,3,-4,-2,10,5,6,-8,10,-8,-7,8,-4,2,3,1,7,-10,3,-10,-9,-4,6,-8,7,-5,-6,4,-6,-3,-8,-7,-10,-8,8,-3,2,3,-9,-4,8,9,-6,7,-1,-3,5,-6,8,8,-1,-4,-10,10,-8,6,-8,10,-1,-6,-7,3,-2,9,-4,-5,-9,7,5,-9,-4,9,-1,7,-7,-6,3,-8,-10,-4,-5,-9,-9,-2,-4,7,5,3,4,9,3,6,5,-1,-3,7,-6,-2,1,-9,-4,-6,-2,-6,6,-8,1,5,9,8,2,2,10,-5,8,9,-10,-1,-1,-9,-4,-6,-2,-8,-10,5,-10,10,-10,4,-8,-10,-5,3,9,2,10,8,-2,4,-1,-2,7,4,8,7,-8,-8,-9,-8,4,4,10,5,8,-2,10,1,-9,-7,4,4,-1,6,3,10,6,1,-6,7,-6,3,6,-3,1,-1,2,-9,-8,-2,-9,-10,6,10,-6,4,-10,7,-2,-9,8,10,-5,-2,-3,8,9,-6,7,-5,-5,-6,7,-10,-2,4,9,2,4,-1,-10,-9,-4,4,-1,8,-7,2,8,4,9,1,-3,-5,9,-4,-4,-10,7,2,2,-5,-4,4,7,1,-6,-7,7,8,8,5,-4,-10,8,9,2,8,9,8,-9,-3,3,-8,9,-6,-7,-9,-7,-1,3,-2,4,-10,1,-10,-7,7,-10,-10,-10,-8,-9,-9,-7,9,2,4,-3,-10,4,-9,2,3,-1,-1,-9,-10,-5,5,9,10,9,-7,2,-9,7,7,3,1,3,9,-10,-2,-5,-7,-1,8,-4,-2,-4,1,10,3,10,-9,6,6,-6,3,5,8,8,6,10,-6,-1,-8,-9,-4,4,3,-3,8,-9,-1,-10,10,6,9,4,-10,6,-3,8,-3,3,2,7,5,10,10,-8,9,-6,10,6,2,10,7,5,10,-6,-5,-2,-10,-10,-4,1,-2,2,5,-4,1,4,-9,6,10,2,6,8,6,-6,-8,-4,2,-4,7,5,1,-4,10,-2,3,-6,7,6,-3,8,7,-2,9,7,-6,-3,-2,7,-8,-10,2,1,1,-7,-8,-6,6,-6,-5,-2,-5,-8,-4,7,-4,5,7,9,3,-2,10,8,5,-2,8,3,-1,-10,-6,6,-6,-7,-5,10,-4,-1,-10,10,-4,10,-6,-5,2,9,4,9,6,-2,-4,-1,7,-3,-10,4,5,5,-7,-8,8,8,-5,-2,4,-6,-10,-7,8,4,10,3,4,-7,-2,1,-2,-2,5,-10,9,7,2,6,1,1,10,7,3,4,-8,-3,-3,9,-10,6,6,7,-5,-9,3,-10,-3,-6,10,10,-6,-2,10,6,2,-9,7,-8,9,1,-7,-6,7,-7,-3,-8,-1,-7,-2,3,6,6,-8,-6,-2,-10,7,1,7,2,4,10,-10,8,-1,-8,3,-2,8,7,-6,-3,2,-10,2,10,4,5,6,-8,4,-7,1,7,7,1,2,8,-8,10,10,7,-9,-8,6,5,-1,1,10,-1,-4,2,-6,8,1,-3,-10,-7,-3,-8,-10,-2,-3,-4,1,-2,8,8,8,-6,-6,2,-9,8,3,-2,-7,7,-5,5,-6,8,-4,-10,4,1,-4,9,1,7,1,8,-4,-2,-6,3,-5,-8,1,3,-3,-7,-7,-4,4,-4,-1,-7,-7,-1,5,5,-9,10,2,-5,-8,-3,1,-5,9,3,2,-2,-8,-2,-1,2,-1,-9,-6,7,1,8,7,8,-3,-3,-1,-1,-10,-2,9,2,-8,2,-7,7,9,9,-1,10,-10,-6,-10,9,-2,-2,5,-3,-6,7,4,-1,-1,8,9,-5,-5,-7,-10,6,7,2,-3,-7,2,2,9,-10,4,-2,8,-10,-8,9,-5,-9,4,-4,-6,7,4,3,-1,-4,3,-7,-5,5,6,-3,-8,3,4,10,-10,-10,-6,-10,8,-3,-3,-3,7,-4,-1,-6,-9,-4,8,-7,-2,-5,-1,-5,-10,-9,9,1,-9,1,-2,-10,5,8,-7,6,-1,8,-5,-1,3,7,-2,-8,-3,-1,-5,10,5,7,-2,-3,-3,4,-6,-4,5,-1,-10,-5,7,10,9,5,-7,-7,-3,-1,-3,-4,-8,-8,-2,9,7,6,2,-9,5,4,-6,8,-3,-6,4,7,-10,6,-5,5,8,9,7,-2,2,4,-9,7,-1,-10,5,-8,4,9,8,-3,-3,-8,-2,3,-8,-2,-1,-1,-2,-9,10,-1,9,6,-2,-6,5,7,4,-9,-9,9,10,2,3,-6,-7,7,-7,-7,-6,-5,-7,-6,4,-5,-8,3,-4,-9,-6,-10,-2,-3,4,9,1,10,-8,-8,4,5,8,10,-3,-1,-4,2,-1,-6,-4,-4,-10,-2,-1,-1,6,8,2,-9,7,-5,-2,10,3,8,-2,10,-5,10,-5,-2,5,-6,-8,-5,5,-9,-7,10,-4,5,9,7,10,-1,-10,-5,-2,5,3,8,-8,-5,-3,-2,3,2,5,-7,1,-7,2,-6,-2,-8,-1,-3,1,-3,-2,3,4,-9,-9,3,6,-8,3,-7,-7,8,-1,-4,-8,9,3,7,-7,8,5,-5,3,-9,9,9,-1,1,-7,-4,-3,-7,3,6,2,-8,-5,-8,-6,3,5,1,-9,7,9,-3,4,-1,-7,9,-10,6,7,4,-3,9,8,-3,2,5,1,6,-1,2,-3,-7,7,-8,9,10,-8,-9,8,-5,2,-4,9,6,-6,-6,-1,-3,6,5,-3,7,-5,-10,-8,5,-5,1,-8,2,7,-2,2,-7,7,6,-8,-5,-9,7,-10,-5,1,6,7,3,7,2,-1,8,4,1,-4,4,3,-1,4,-5,6,-4,1,-6,-3,6,9,3,5,-5,2,4,-3,-6,3,-3,5,9,-3,4,3,-9,3,8,-7,9,-4,-5,-8,-5,-6,-9,4,-7,-2,4,-1,10,6,-2,-2,-6,-5,-3,-4,5,7,-1,1,9,-8,-3,-5,-3,-2,7,7,8,4,5,2,-10,-4,-7,8,10,-8,-5,7,-5,4,-1,-5,10,-4,9,-5,-2,-9,-3,6,5,8,8,-9,-4,-7,3,-6,1,-10,-6,1,-3,9,-7,1,1,-1,7,-2,-2,-6,10,8,3,-4,-2,-7,7,-10,2,-6,5,10,9,10,10,6,9,-1,-3,-1,2,-9,5,3,3,8,1,9,-1,-1,9,1,3,-2,1,-1,-3,-1,-10,-4,6,-2,-4,-6,1,8,-7,10,2,-8,5,-7,-10,5,-3,-4,4,7,-8,-3,-10,-1,-1,-1,-10,8,-10,4,-1,9,-9,-6,-10,1,6,7,6,-5,8,9,-6,-3,-2,-6,5,9,-10,-9,10,8,-5,-3,4,7,5,2,-5,-8,4,-9,9,5,7,-10,3,2,-5,-10,-3,3,-6,-9,-1,-7,-1,6,-8,-9,-4,-9,-7,6,6,-10,-4,6,5,-3,2,-1,-8,-3,7,-1,-1,9,-1,-7,-2,5,10,-8,-9,-1,-10,-4,-1,-5,10,-9,-6,6,-3,6,2,3,-5,6,3,4,2,-4,-6,-9,-4,-7,7,2,8,7,-1,1,3,-1,5,-10,5,9,-2,10,-9,10,10,-7,-2,-8,5,1,7,6,9,-10,-9,-8,9,9,-4,-7,-1,-5,-9,5,2,-5,8,-10,5,-1,-9,5,6,-10,-3,7,1,4,-4,-5,-5,-5,10,-9,-3,1,-9,10,2,-10,-6,8,10,7,-3,10,5,-10,-9,1,-9,-6,3,-8,7,-10,6,8,2,-9,10,-2,5,9,10,7,-4,-10,8,-2,5,-6,3,-6,-3,-1,-2,-7,4,-2,8,8,2,-1,-7,5,-8,-4,7,6,-2,-3], dtype = "uint16")#candidate|7674|(2560,)|const|uint16
call_7673 = relay.TupleGetItem(func_2833_call(relay.reshape(const_7674.astype('uint16'), [128, 20])), 5)
call_7675 = relay.TupleGetItem(func_2835_call(relay.reshape(const_7674.astype('uint16'), [128, 20])), 5)
output = relay.Tuple([call_7669,call_7673,const_7674,])
output2 = relay.Tuple([call_7670,call_7675,const_7674,])
func_7685 = relay.Function([], output)
mod['func_7685'] = func_7685
mod = relay.transform.InferType()(mod)
mutated_mod['func_7685'] = func_7685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7685_call = mutated_mod.get_global_var('func_7685')
call_7686 = func_7685_call()
output = call_7686
func_7687 = relay.Function([], output)
mutated_mod['func_7687'] = func_7687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2509_call = mod.get_global_var('func_2509')
func_2511_call = mutated_mod.get_global_var('func_2511')
call_7721 = func_2509_call()
call_7722 = func_2509_call()
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
var_7794 = relay.var("var_7794", dtype = "bool", shape = (91, 9))#candidate|7794|(91, 9)|var|bool
call_7793 = relay.TupleGetItem(func_47_call(relay.reshape(var_7794.astype('bool'), [13, 9, 7])), 1)
call_7795 = relay.TupleGetItem(func_50_call(relay.reshape(var_7794.astype('bool'), [13, 9, 7])), 1)
output = relay.Tuple([call_7721,call_7793,var_7794,])
output2 = relay.Tuple([call_7722,call_7795,var_7794,])
func_7797 = relay.Function([var_7794,], output)
mod['func_7797'] = func_7797
mod = relay.transform.InferType()(mod)
var_7798 = relay.var("var_7798", dtype = "bool", shape = (91, 9))#candidate|7798|(91, 9)|var|bool
output = func_7797(var_7798)
func_7799 = relay.Function([var_7798], output)
mutated_mod['func_7799'] = func_7799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7111_call = mod.get_global_var('func_7111')
func_7112_call = mutated_mod.get_global_var('func_7112')
call_7832 = relay.TupleGetItem(func_7111_call(), 0)
call_7833 = relay.TupleGetItem(func_7112_call(), 0)
func_7111_call = mod.get_global_var('func_7111')
func_7112_call = mutated_mod.get_global_var('func_7112')
call_7848 = relay.TupleGetItem(func_7111_call(), 0)
call_7849 = relay.TupleGetItem(func_7112_call(), 0)
func_2628_call = mod.get_global_var('func_2628')
func_2630_call = mutated_mod.get_global_var('func_2630')
var_7859 = relay.var("var_7859", dtype = "uint32", shape = (65,))#candidate|7859|(65,)|var|uint32
call_7858 = relay.TupleGetItem(func_2628_call(relay.reshape(var_7859.astype('uint32'), [1, 13, 5])), 0)
call_7860 = relay.TupleGetItem(func_2630_call(relay.reshape(var_7859.astype('uint32'), [1, 13, 5])), 0)
func_1753_call = mod.get_global_var('func_1753')
func_1758_call = mutated_mod.get_global_var('func_1758')
const_7875 = relay.const([3,9,10,1,-7,-5,-3,3,-3,5,4,7,-5,-1,3,1,1,5,10,-1,7,3,-2,-7,9,-8,8,-10,-8,-3,6,9,4,7,2,-2,5,8,-2,-6,-5,-3,-10,5,4,2,-10,7,7,-9,-3,-5,-8,8,5,8,-8,4,-6,7,5,-9,-2,-10,-10,7,1,2,4,9,3,3,10,9,-6,-5,-8,9,-1,-9,9,-6,8,2,-7,-5,-10,-2,-6,6,7,-7,6,-7,5,9,1,-8,3,-3,1,-3,-6,1,7,-6,-1,-1,8,-7,3,-9,-9,-5,7,5,8,8,4,-8,1,5,-6,10,-4,9,2,2,-4,-6,-5,-10,-10,6,10,-4,7,-2,6,1,10,9,-7,-5,-8,-4,3,-7,-2,6,-9,2,2,1,7,-9,-1,9,9,-10,7,9,8,3,-1,6,9,-7,4,-8,1,8,-6,-9,2,-2,-5,-9,9,7,-8,1,10,10,-6,-5,-8,9,3,-10,1,-4,-5,9,4,5,8,-1,3,-10,-2,8,-9,5,-8,7,-7,4,-5,-5,1,-10,7,5,3,-1,-2,4,-7,-5,3,4,4,-3,3,7,9,2,9,6,-7,-6,5,2,10,-6,-1,5,8,-6,8,-4,-5,3,-6,-7,-5,3,4,1,-5,6,-5,3,1,-4,-7,7,7,-7,8,-7,8,4,-7,5,-2,-10,-4,-2,-4,-5,5,4,-4,6,-4,7,-2,3,6,1,-9,-4,-4,9,3,1,-7,-1,-8,3,9,-4,-10,10,5,3,10,8,-4,-4,-10,-6,-1,-8,-7,1,-2,8,-1,10,-10,9,-10,6,3,-2,4,-2,8,-4,-2,10,-9,5,-9,-8,-8,10,6,-4,5,-4,8,6,5,-1,-2,-10,-9,4,10,6,-1,-9,-4,5,-1,-10,2,-4,-3,-3,-6,-9,8,3,-5,9,7,2,1,1,-6,-10,7,7,-7,-9,5,-7,1,-4,-3,2,-1,3,2,3,-7,8,6,-5,8,-7,-2,-10,8,-9,9,3,6,1,8,-5,10,8,-1,-1,7,-3,-4,-1,-7,3,2,5,10,5,1,-4,5,6,-6,-4,5,-3,-2,-1,-5,-4,-2,2,-4,-1,-8,7,8,-1,2,-9,-5,-8,-7,6,7,8,9,-9,-8,10,-7,3,-10,-10,-2,-1,-3,3,-10,-3,-9,4,2,10,6,-10,-7,-8,7,-1,-1,5,-1,-6,-9,10,2,7,9,-6,7,10,6,1,6,-4,6,10,10,-10,7,-1,6,-4,5,-2,5,6,-9,-7,-1,-1,10,6,-1,1,6,8,-9,-7,-2,5,-10,-7,10,-4,-4,-7,10,6,-10,9,8,10,-10,2,-5,-7,7,-5,-9,7,-6,10,8,7,-3,-3,-4,8,9,5,-6,2,6,2,6,1,-6,8,-6,-1,3,-2,9,10,2,6,8,3,5,9,7,-5,-2,-8,-10,-9,-6,-10,3,-5,-5,-2,8,7,3,7,8,6,5,-10,4,7,-10,-5,7,7,2,5,7,5,7,-3,-4,-7,-2,5,6,-5,9,9,-3,-7,8,-7,1,-6,-8,5,7,-2,-9,-4,-6,-9,-3,10,7,-1,7,-9,-3,-9,1,2,8,-8,8,-9,-2,-1,9,9,7,10,-1,4,-1,3,-9,-1,-9,-1,10,3,-10,-7,4,-4,9,4,-2,-1,3,8,-1,8,-9,-8,9,-1,4,10,5,10,10,3,4,5,-10,-9,2,-4,6,-10,-1,-6,2,-4,9,-10,-10,1,8,1,-10,2,6,5,-6,-9,-7,-6,10,-7,-6,8,-1,-9,-6,7,-9,-10,-5,-8,-9,9,-1,-6,-5,-2,9,4,-10,8,-3,3,-6,-8,-7,1,5,-5,-3,7,-5,8,8,5,4,5,-10,1,1,-6,-8,-6,7,9,-4,9,-5,3,-8,3,-4,1,-9,10,2,10,-3,2,10,9,8,-3,-4,10,5,-5,-4,-2,9,-2,-8,-2,9,-10,-5,-10,6,8,10,-1,3,-5,-2,-9,9,-5,-2,-9,-1,7,-7,-1,-10,2,-8,6,-10,-8,6,-5,-7,-3,9,9,2,-6,-2,-3,-5,-4,-9,-4,-9,-1,-10,-1,9,5,7,-8,9,-7,10,-7,6,-9,10,-4,-6,6,-3,2,-3,10,2,-1,3,-5,-10,7,4,9,-9,-4,7,-2,9,2,2,3,1,4,4,6,-2,7,1,9,-8,7,-3,8,3,-3,4,-9,-2,1,-4,7,2,-1,10,2,-3,7,-8,-5,5,-5,5,-5,7,-10,-5,-7,1,-9,-8,-10,4,6,-2,-4,-10,-7,-5,2,10,-4,-9,3,1,-2,7,-1,-1,2,9,-10,6,-5,-4,4,-1,1,9,1,-6,-10,-6,3,-5,1,-10,4,10,9,-8,-8,-1,-8,-2,2,-3,2,-3,-5,9,-4,-6,-7,10,10,10,5,-6,-4,2,-8,-8,4,-7,-2,6,-7,6,1,-1,2,-9,-3,-9,-5,2,-6,6,-4,1,-9,-3,1,2,3,-3,3,9,-8,2,1,-9,-6,9,9,-7,-6,7,-8,-9,2,-4,-5,2,3,-7,8,1,4,-4,-9,3,9,-5,9,-8,8,-6,6,4,-10,6,-10,1,-7,7,6,-5,8,-4,4,5,-3,-4,-9,-2,1,6,-5,5,4,9,-10,6,4,6,-3,1,4,-7,-4,-9,-7,8,3,-5,7,-8,-10,-6,8,2,5,-7,9,-9,3,9,4,-1,5,6,1,1,-2,-4,1,10,-3,4,-1,6,2,5,5,4,3,3,8,5,-1,10,7,7,-9,2,3,-5,3,10,7,1,-8,5,-6,-5,9,8,-7,8,5,5,7,-2,1,10,10,1,-4,3,7,9,-5,-2,4,-8,9,7,-5,-6,-5,-6,8,2,-4,-3,4,4,3,-4,5,5,7,-10,3,1,-4,10,4,5,-8,6,-2,-3,-8,1,-1,9,-8,-2,-7,-8,10,3,9,-10,6,-9,8,-5,-1,10,-3,-3,10,-2,10,7,8,-4,10,6,-1,6,8,-6,10,-4,6,5,-5,-2,9,-5,-1,-5,-2,-9,-7,2,8,6,-3,4,6,-5,8,-5,1,5,-6,5,3,-1,-8,-4,1,6,-10,3,-10,8,8,-7,3,2,-4,9,8,-6,3,3,-1,7,-1,-9,9,-1,1,7,-1,3,-4,3,-2,-10,-2,-10,4,-4,8,-6,-1,5,4,-5,-10,10,-1,-8,1,-8,1,-6,5,-1,-5,1,1,-9,-9,10,3,3,-3,4,9,7,-10,-6,-6,10,-4,-9,-9,2,3,7,-3,9,-1,10,-7,-1,-1,-3,-6,8,6,-6,6,-2,3,-8,-2,-2,1,5,8,-6,5,-6,4,2,3,-4,-10,-9,-6,9,3,-2,-1,4,-3,10,4,10,2,-8,3,-6,-8,6,-4,-3,6,3,2,-1,-10,4,9,-1,-7,-7,-3,-1,-8,5,4,8,3,9,9,-2,-1,2,-10,10,-6,-6,-8,9,6,7,-4,-1,-4,-4,-8,-3,-1,-6,2,8,3,-4,-3,-6,-7,-10,-7,9,9,6,10,-6,-6,3,10,-5,-5,5,-2,-6,3,-1,7,4,3,-5,1,5,-8,5,-10,-3,9,-1,-7,1,5,2,10,-9,-8,-8,-8,8,1,-3,6,-6,-2,-8,-5,2,-9,-1,-2,3,-7,-3,-6,-8,-6,10,7,-7,-2,-9,-3,7,7,2,10,-1,8,1,-5,-3,-2,-3,8,1,6,-4,-10,3,-1,-7,2,-8,-4,-6,-10,9,1,-2,-3,-8,-2,2,-3,1,9,7,-8,2,5,-10,-9,6,3,1,-2,9,-1,-8,-3,10,-9,-5,-3,-10,7,1,10,-5,9,3,3,5,-10,-10,-2,-6,7,-9,-8,-7,10,10,9,-7,1,10,-9,-10,8,5,-10,10,-4,-8,-9,-9,6,10,-5,4,4,-4,8,3,3,3,-9,-3,-3,7,-7,-10,-6,-10,7,10,7,4,7,-9,-7,6,-9,-1,1,6,-4,2,-9,2,-6,7,4,9,1,2,4,6,-6,-8,4,-6,4,-8,-10,-1,1,-2,-1,8,2,-2,9,-2,2,3,-5,4,-7,-4,-1,5,-3,10,-9,8,8,6,7,-4,7,4,-4,-3,9,8,-10,-5,-10,-9,-3,8,6,-9,-3,9,-10,-4,-1,5,-4,-3,6,9,1,2,-2,5,6,10,-9,-9,-4,-5,-10,7,3,-8,6,-4,-5,4,7,-7,5,2,6,5,4,5,10,8,1,-2,-3,-5,5,6,-1,6,-10,-2,-8,4,-8,-6,10,2,9,-8,4,-1,-5,2,-1,1,-5,-8,1,6,1,-6,5,-10,-5,9,4,-6,-10,-2,-7,2,6,-6,2,-4,6,-3,1,-7,4,4,7,-6,10,-6,2,8,10,7,-8,8,-3,6,6,10,9,-9,-6,3,-6,-1,-9,-8,-5,-4,6,-8,2,-6,-9,-2,10,5,8,-2,-7,5,-3,8,8,2,3,-6,6,-5,8,-3,9,-6,8,-3,2,2,3,-5,3,8,1,-2,5,2,-5,4,5,-4,8,7,-7,7,-2,-4,2,-10,5,-10,9,8,6,-1,1,-3,5,1,2,6,8,6,2,-3,-8,-9,-2,5,8,1,3,10,-6,2,7,-2,7,-7,6,8,-2,4,-6,3,7,5,8,8,4,-3,-9,8,-5,-5,-4,8,9,-9,1,9,6,7,-9,1,4,-4,1,9,6,10,8,-3,9,2,-4,9,-6,7,1,9,-3,10,-7,-1,-4,3,8,9,-10,9,-5,-7,7,6,-3,7,2,-2,-8,-3,4,4,-4,1,-7,7,1,3,-7,7,-6,5,-2,8,-10,4,-9,-7,-3,-6,-9,2,-8,-1,4,6,-4,9,-8,8,9,3,10,10,8,-4,10,10,-1,-2,9,-6,-9,-1,-3,8,-10,-2,2,-6,10,9,7,8,10,-2,8,-4,-2,-7,-5,-7,-7,-5,-10,9,-2,10,8,7,9,-1,-7,5,1,6,-8,-10,1,2,-6,-1,-1,-8,-10,9,6,6,6,-5,-3,2,4,-6,7,6,9,4,2,-1,6,-2,1,-8,-9,-1,-3,-6,4,2,10,-7,-9,10,-10,2,10,-10,1,-5,10,3,-2,-8,10,8,-10,-8,-3,-8,9,2,-5,-10,10,-7,5,4,10,4,4,8,6,-4,-6,3,-4,5,-9,8,-2,2,6,3,-9,-3,-10,8,-1,-4,-5,-10,-5,-10,10,4,2,7,3,1,-10,5,-9,3,-3,7,-7,-9,-2,7,-7,-3,-8,-7,2,-2,-6,2,8,-5,4,1,9,-4,-10,-2,-3,-6,-7,3,-2,-2,10,4,-9,2,-1,7,-4,-2,3,3,-8,10,-3,5,-7,-4,2,8,-6,-7,3,8,6,-4,-3,6,6,-7,8,-4,2,6,5,5,4,10,-7,-5,-8,1,-5,-5,2,10,7,-9,-4,-10,8,-2,-1,-10,-5,-1,-5,6,-9,1,-4,-1,6,7,4,-1,-7,7,-9,4,1,7,-8,-5,4,6,8,-7,9,6,-3,8,-2,-6,1,3,7,-9,2,2,2,2,-7,-6,-4,2,1,-7,-6,-4,-7,8,-8,9,-2,6,8,8,8,4,8,1,-9,-4,5,9,-6,6,-7,-6,7,-7,-9,-2,8,-10,3,8,4,-6,-10,1,-5,4,3,1,1,4,-2,8,4,6,1,-1,6,4,-2,3,-1,9,6,-1,-7,-8,3,9,-6,-5,1,-4,3,2,-2,-5,4,6,-6,-1,-1,-4,-7,-2,-7,1,-4,4,4,7,3,-8,7,-10,-10,8,10,-8,2,-9,8,9,-5,-3,1,5,-3,-2,5,-7,-1,-6,4,7,5,-9,3,7,10,-9,10,-4,6,-7,-8,-6,9,1,8,-1,3,6,-5,6,-2,8,-8,9,8,7,-10,6,-6,3,4,-9,-2,-5,-5,-6,-7,-1,7,-10,-5,1,-9,5,6,1,1,-9,2,-2,4,-6,-2,-5,-6,-4,-10,-8,-3,-4,2,9,5,8,9,-6,10,3,10,1,-10,9,-9,1,-2,1,10,7,7,3,-7,-8,-1,-1,8,9,6,-8,-4,6,-3,10,-4,-1,6,6,2,-2,-6,4,-4,10,10,4,-10,-10,5,8,-8,-10,-2,-8,2,-7,-3,-2,5,-7,-3,-1,-9,-4,2,6,1,-6,4,-7,-6,-5,-7,-7,1,9,7,5,-2,2,2,-4,4,8,-4,6,-3,-8,-10,-5,1,2,-6,3,7,10,3,-4,5,-7,-9,8,6,2,-3,6,3,-3,7,4,1,-3,1,-3,9,5,5,-10,9,6,9,7,3,10,6,-4,-2,-3,-2,7,-8,-9,-6,-3,-1,9,4,3,-8,7,-10,2,8,5,4,3,-6,7,3,7,1,-5,5,-2,2,-6,-10,4,-6,8,-1,-3,3,-7,10,-10,1,5,5,9,-7,-10,7,-5,-1,4,5,-8,-9,-5,-10,-9,-2,9,4,-5,-4,9,10,-6,-8,4,-10,-2,-7,8,-5,10,-3,-5,8,-9,-6,6,4,-7,-4,8,3,-5,-8,-8,1,-10,-7,-3,-6,7,-3,-10,-5,-1,-9,-3,8,3,-10,-9,-8,-7,-4,2,-5,4,4,-8,10,-7,10,-1,7,-6,-4,-10,-6,9,-7,9,-2,1,6,4,-1,-5,1], dtype = "uint16")#candidate|7875|(2560,)|const|uint16
const_7876 = relay.const(-9, dtype = "uint16")#candidate|7876|()|const|uint16
const_7877 = relay.const([9.389584,-6.930780,-3.642064,-1.862065,2.857897,4.866981,7.311402,8.212310,-3.378319,-6.143248,-7.715034,-4.353963,5.727567,1.261065,7.493447,2.926386,1.977747,0.243851,-5.649149,1.600552,3.750555,-3.306905,2.488493,-6.154425,-4.923791,-9.165024,6.996208,-8.662712,8.287694,0.461283,-3.646075,5.667855,-2.321770,8.120225,3.042377,2.748192,-2.012036,4.760852,1.641398,1.602421,-2.358574,-9.213328,-5.668121,5.506215,5.550099,-3.715920,4.123474,3.119575,-9.828359,7.356962,5.851998,-7.469715,-1.689237,-2.494055,-8.126274,6.587108,1.454471,-3.565505,-3.687763,3.134909,-3.292138,-8.357039,4.937486,4.646087,-5.132235,9.134587,1.118547,7.063680,2.604979,-7.848413,8.783009,3.831455,0.115254,1.886614,2.279731,1.136285,-7.449785,7.869591,0.546931,-6.664269,5.586541,-3.286794,2.796428,-0.201876,7.576062,-8.566078,-3.436190,0.659987,4.962147,-8.440514,3.624352,-1.348022,0.838474,1.470189,9.545241,-4.514378,-7.796256,1.322930,5.770095,-2.413138,-7.491268,7.503487,-9.578800,7.511055,6.776309,-3.830467,5.319377,8.443745,8.061213,-9.462352,-8.320742,9.402944,5.424522,-3.199558,4.078524,2.415339,-0.135228,-6.532608,5.636042,-1.365822,7.943391,5.512362,-7.628940,5.171727,7.420702,-3.139737,4.759005,-3.483747,-3.810805,2.736705,-5.005165,-1.214695,3.076669,2.759387,-3.883590,-1.480986,9.180448,-2.592694,-4.755917,3.226969,1.763301,0.910286,0.649595,8.140459,-5.711164,0.426046,5.490014,3.886151,3.838030,7.799772,5.123339,2.043673,3.459392,-8.357107,-1.568770,-1.851363,9.035579,-0.434467,3.840973,-8.712475,-5.633938,-7.623889,4.768402,-5.184168,8.497153,-2.446376,8.530040,7.321917,-4.687308,-5.244394,4.267055,-8.389318,-9.252521,3.084317,8.403111], dtype = "float32")#candidate|7877|(175,)|const|float32
call_7874 = relay.TupleGetItem(func_1753_call(relay.reshape(const_7875.astype('uint16'), [16, 10, 16]), relay.reshape(const_7876.astype('uint16'), []), relay.reshape(const_7877.astype('float32'), [175, 1]), relay.reshape(call_7848.astype('uint16'), [2,]), ), 0)
call_7878 = relay.TupleGetItem(func_1758_call(relay.reshape(const_7875.astype('uint16'), [16, 10, 16]), relay.reshape(const_7876.astype('uint16'), []), relay.reshape(const_7877.astype('float32'), [175, 1]), relay.reshape(call_7848.astype('uint16'), [2,]), ), 0)
bop_7896 = relay.minimum(call_7832.astype('int64'), relay.reshape(call_7848.astype('int64'), relay.shape_of(call_7832))) # shape=(1, 2)
bop_7899 = relay.minimum(call_7833.astype('int64'), relay.reshape(call_7849.astype('int64'), relay.shape_of(call_7833))) # shape=(1, 2)
output = relay.Tuple([call_7858,var_7859,call_7874,const_7875,const_7876,const_7877,bop_7896,])
output2 = relay.Tuple([call_7860,var_7859,call_7878,const_7875,const_7876,const_7877,bop_7899,])
func_7903 = relay.Function([var_7859,], output)
mod['func_7903'] = func_7903
mod = relay.transform.InferType()(mod)
mutated_mod['func_7903'] = func_7903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7904 = relay.var("var_7904", dtype = "uint32", shape = (65,))#candidate|7904|(65,)|var|uint32
func_7903_call = mutated_mod.get_global_var('func_7903')
call_7905 = func_7903_call(var_7904)
output = call_7905
func_7906 = relay.Function([var_7904], output)
mutated_mod['func_7906'] = func_7906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6010_call = mutated_mod.get_global_var('func_6010')
call_7933 = func_6009_call()
call_7934 = func_6009_call()
output = call_7933
output2 = call_7934
func_7935 = relay.Function([], output)
mod['func_7935'] = func_7935
mod = relay.transform.InferType()(mod)
mutated_mod['func_7935'] = func_7935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7935_call = mutated_mod.get_global_var('func_7935')
call_7936 = func_7935_call()
output = call_7936
func_7937 = relay.Function([], output)
mutated_mod['func_7937'] = func_7937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2152_call = mod.get_global_var('func_2152')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_7944 = relay.TupleGetItem(func_2152_call(), 0)
call_7945 = relay.TupleGetItem(func_2154_call(), 0)
func_7216_call = mod.get_global_var('func_7216')
func_7217_call = mutated_mod.get_global_var('func_7217')
call_7964 = func_7216_call()
call_7965 = func_7216_call()
output = relay.Tuple([call_7944,call_7964,])
output2 = relay.Tuple([call_7945,call_7965,])
func_7975 = relay.Function([], output)
mod['func_7975'] = func_7975
mod = relay.transform.InferType()(mod)
output = func_7975()
func_7976 = relay.Function([], output)
mutated_mod['func_7976'] = func_7976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7625_call = mod.get_global_var('func_7625')
func_7627_call = mutated_mod.get_global_var('func_7627')
call_8016 = relay.TupleGetItem(func_7625_call(), 0)
call_8017 = relay.TupleGetItem(func_7627_call(), 0)
func_3190_call = mod.get_global_var('func_3190')
func_3192_call = mutated_mod.get_global_var('func_3192')
const_8021 = relay.const([-3,9,3,3,-8,8,9,2,-10,9,5,-9,-6,4,-9,4,-10,-7,-3,-8,3,9,-6,3,7,3,-5,-8,-7,6,9,-7,-3,10,5,8,-6,9,9,7,3,-8,2,-9,2,6,7,8,10,-5,8,2,-2,3,4,-7,-1,5,-3,-2,-2,-6,-2,7,2,6,7,3,10,9,7,-10,3,10,10,2,-2,8,-3,-7,-9,7,10,5,6,-3,2,-9,-1,-2,5,-2,2,-3,7,2,-1,-3,-6,1,2,5,9,8,5,10,2,8,-2,-1,-9,8,-9,-10,-9,7,7,5,7,8,3,-3,10,1,10,-2,4,-8,-2,7,1,5,7,-6,5,-8,1,-5,1,-2,9,-10,5,5,-8,9,8,7,-3,-2,4,7,1,8,-10,-5,-6,4,-4,-1,1,10,-5,9,-10,8,-10,1,1,-5,10,1,-4,-9,2,-1,-3,4,-9,-8,3,3,3,7,3,-4,-10,1,8,4,-4,-4,-9,-3,-3,-7,6,-2,-6,-2,8,6,-9,-4,8,10,7,9,4,4,4,4,1,-9,-4,8,7,2,10,6,7,10,-9,10,10,1,-3,-5,2,1,-7,9,-2,1,-8,10,10,-9,-8,2,-1,3,1,-10,2,-8,2,-4,-8,-6,1,-2,-7,-1,8,-6,-8,4,-7,-4,-6,1,-10,2,-7,6,4,10,-1,-8,-4,-9,-3,6,7,-10,-10,9,-5,2,9,1,-8,-7,-2,7,7,-10,8,10,-6,6,-3,-8,8,-2,7,-2,-4,1,4,-2,3,9,10,7,-2,-1,-2,5,8,10,-9,-10,3,-9,-1,-6,-2,8,-8,5,-9,-5,5,4,-7,9,-7,1,10,7,-8,6,1,4,-8,-7,7,-10,4,-6,-6,-9,5,3,7,-7,-4,-8,6,2,1,2,3,-10,6,2,-4,7,8,-5,1,-3,-4,9,1,5,-1,1,9,-5,-1,8,-7,-3,8,-1,9,-3,-4,-4,-4,-6,7,2,-1,2,-5,5,7,6,-5,4,2,-8,2,9,10,4,5,3,5,7,-6,-2,10,10,-7,-1,4,3,-1,5,-10,-9,6,-2,-9,-3,-1,10,2,-1,6,6,-1,-7,3,-4,-2,-9,-8,1,10,-2,8,-4,-4,9,-5,10,-6,-8,9,-2,-8,-9,-10,4,4,-10,-10,5,7,3,-1,-2,10,-3,-4,9,-6,8,1,-5,-10,9,9,-3,10,-2,1,-7,6,1,5,-3,10,-6,-5,-8,-7,-4,-3,-7,-7,3,5,-10,-9,10,-2,-4,6,5,-2,8,-2,-8,-1,9,5,5,-1,2,5,4,7,-2,-2,6,-2,5,-9,10,-9,-8,-2,-6,-10,-2,10,-4,8,2,5,-1,-4,-2,9,-3,-2,5,-5,-6,9,10,6,8,10,-3,8,9,-2,5,4,2,-10,-1,-9,-8,6,10,9,-7,6,3,4,7,4,9,-1,-3,7,-4,2,-5,-1,10,2,1,9,-3,-6,1,4,10,-9,6,9,-4,-3,7,3,4,-7,5,-8,1,1,-6,9,10,-8,-8,6,6,-1,3,-2,-1,-1,7,5,5,-9,2,-4,-8,7,-9,-7,4,10,2,-6,3,9,9,7,1,3,-5,-6,-1,-10,7,5,-7,-9,-9,4,-2,-1,7,5,5,3,-6,3,-3,-8,-10,2,-10,-6,7,10,-3,2,-10,-9,-6,-4,-1,-2,10,7,-4,7,1,2,3,1,4,7,-2,-8,-9,3,-9,-8,-4,7,3,4,9,-4,-10,8,8,-8,2,-1,8,4,-8,4,-5,-9,-7,2,1,-6,-3,-4,2,3,10,8,5,-3,6,4,10,-2,8,-3,-2,-9,5,-7,-7,-4,4,5,6,4,-7,5,-2,6,-1,-9,8,-7,5,-2,4,-1,10,8,6,-9,-10,4,-9,4,-7,-2,-2,10,3,-10,-9,-5,-9,-6,3,-7,8,-5,-2,-5,-1,-6,6,-2,9,5,-5,9,-3,6,-10,1,8,5,6,-9,-8,1,2,-4,7,10,-2,-5,-4,3,8,10,-9,-4,-6,3,1,-8,9,-3,-1,-8,2,8,-6,7,-4,-10,3,-9,10,-3,-5,-3,4,3,-10,8,6,-5,-8,8,3,-6,-3,-5,8,3,10,-10,-3,10,3,5,-8,2,7,10,10,-4,3,-8,-9,4,9,4,6,7,-3,-1,-5,7,-4,1,10,-9,-7,4,9,5,-4,2,-4,3,3,6,-6,-1,-7,6,-8,-2,3,-10,8,10,6,-3,-3,6,10,-4,-5,1,-5,-1,4,-7,3,-7,3,-10,9,7,-2,6,5,10,-6,3,-8,6,10,-6,9,4,1,10,9,-10,10,-3,-7,-8,4,6,-6,1,-4,-10,10,-6,8,-9,-3,10,-6,-10,-5,-7,10,10,-6,5,-6,4,9,-7,5,-5,-4,2,7,-4,-10,3,4,7,4,9,-7,6,-4,4,-8,6,6,-3,-9,9,-5,1,-6,9,-2,-10,3,6,10,5,-3,-3,10,-3,-10,-10,7,-6,2,2,6,-3,-9,-6,-1,10,-3,-2,-6,2,7,3,-3,-6,-4,7,2,1,-8,-4,-8,-2,7,4,9,1,7,-10,5,-3,6,-1,9,10,8,6,-8,9,-10,-1,10,-5,-6,-7,-2,-1,10,7,-3,5,-2,-7,9,6,-10,10,-8,7,1,6,4,-4,-1,-4,-9,-6,-1,-1,-1,-10,5,1,7,1,3,5,-7,2,9,10,4,-1,1,5,-1,2,-9,3,-2,5,-2,-5,-7,-6,-4,6,-2,-4,9,4,-6,-9,-9,10,9,-9,4,-9,-2,9,1,3,-4,-8,-6,-4,9,9,8,-1,7,-7,5,-3,-2,10,-10,9,-10,7,-9,10,6,6,-1,2,-9,10,-8,-9,-5,-6,-4,1,3,-1,10,-10,3,4,-5,3,-9,7,5,-8,7,-7,10,-6,-5,3,6,-6,1,4,-8,1,-9,-3,-4,-5,6,3,-10,-6,6,4,7,3,-10,6,-6,-3,5,9,8,2,6,9,6,4,-7,6,-8,3,-7,-6,-4,-6,-7,-8,-9,-9,8,4,5,8,6,-7,-2,-4,7,-2,9,2,2,-10,-4,9,-9,8,3,-8,-1,-5,5,-1,-9,5,-10,-3,9,-7,-2,-7,-3,5,-10,-7,7,-5,3,-5,1,-8,9,5,-5,-2,-3,8,-3,-2,-3,5,10,2,-6,-4,7,7,-5,5,-9,7,-6,-5,-5,2,-3,9,5,-7,-8,-9,6,2,-10,-1,4,8,2,-6,10,6,5,9,9,-2,-10,4,6,-7,-3,-5,8,-6,9,-9,10,-4,-1,6,10,6,8,8,-6,-2,5,3,-1,6,-10,8,-8,-6,5,10,-7,-7,-8,1,-10,-10,-8,-10,3,8,-9,-5,9,10,1,-1,-8,-7,5,-8,-1,-10,3,-10,4,-2,-4,-1,-8,9,9,-2,-8,3,7,8,10,-8,8,1,-6,6,-10,5,8,-1,-3,5,-2,-5,-8,6,1,-2,2,2,6,9,6,6,-7,-10,10,2,-2,10,1,9,-9,-2,2,-8,3,4,3,-3,9,-3,-7,-10,3,10,-5,6,9,7,-4,-2,4,8,8,-6,-3,5,-5,10,4,-1,-8,-4,-7,-2,8,9,2,7,-7,8,-3,1,-5,-3,-2,9,-1,10,-4,8,4,1,-5,5,-3,-5,5,2,8,10,-2,-1,-2,3,-1,9,10,-3,-10,8,-3,-8,8,10,-7,-5,9,-2,-9,10,-5,7,-9,-10,-3,2,9,4,-2,-3,-5,8,6,-7,-4,-7,6,-4,-6,-5,3,5,-1,-1,-3,4,5,-4,-3,-6,-9,-5,8,-1,-4,-3,6,-10,7,10,6,-10,5,3,-8,-4,-3,2,-10,4,-1,-2,-5,4,6,3,-7,4,-10,1,-6,-5,-5,8,1,-9,1,9,-6,1,6,-5,-9,-6,-5,-5,3,-2,8,-4,-4,-1,-6,4,-3,5,8,-2,-10,6,-7,-10,2,9,-2,10,7,4,4,-7,-2,8,-6,-9,-1,6,5,-8,-8,8,9,-7,-1,-10,-10,4,3,3,4,-8,4,-3,-7,-9,-8,-6,-5,3,-5,-1,-2,-8,4,-4,1,3,5,-6,7,-9,2,-1,-10,3,9,-2,-8,8,2,-2,6,-8,-1,3,-10,2,8,1,6,-3,9,-8,8,10,-7,-10,-8,-4,-5,-7,-9,-8,-10,5,4,-3,-7,-1,6,-2,-4,8,3,10,-8,4,4,6,-3,-2,-1,2,-7,-3,-4,7,-9,9,6,-3,-6,4,9,6,1,8,6,-9,3,-5,9,7,9,-4,-7,1,-2,-3,-7,2,8,9,8,-6,-2,-9,5,10,4,-10,9,-4,6,-3,-8,-10,-2,10,-9,-2,7,3,-1,-7,7,8,9,-8,-1,10,5,-6,1,9,-2,10,-6,3,-5,4,8,-7,-4,-1,-7,4,1,1,6,1,-2,-9,-5,8,5,-4,-4,1,8,-4,-5,1,8,9,1,-4,-2,-3,-9,8,1,-8,-5,-4,3,1,6,-5,1,2,5,-7,1,3,-1,6,5,8,3,4,-9,5,5,2,5,10,-10,-6,-6,-2,3,8,2,-9,-7,-4,-8,-10,10,-2,5,-6,8,-7,2,-1,7,-3,3,-5,-5,-7,-7,-7,-10,-3,-1,-2,-10,5,-8,5,4,-6,9,9,2,6,-4,8,4,-1,-10,-5,-9,10,-5,-7,-2,7,-6,-5,4,-10,8,4,-1,8,5,-4,6,-6,-1,-1,5,4,6,-2,5,-1,-1,-5,-10,-8,8,1,-7,4,-9,-1,-3,-6,6,-1,1,4,-7,-8,3,1,-7,-5,9,-10,-4,-3,-8,8,-10,-5,-3,4,-7,6,-8,1,-1,-10,6,1,5,-1,-4,6,-9,4,1,1,-2,-8,-4,-8,7,-5,9,5,9,-6,-6,-6,5,-5,10,6,3,-2,5,1,-7,-5,2,2,-9,-6,-1,7,4,4,-10,-6,4,-9,6,-1,6,-1,9,2,10,-10,-10,-8,-3,-8,1,-7,10,4,-7,10,2,-4,3,-8,3,5,-6,-8,5,1,8,3,-3,-7,-3,-4,8,-7,-5,3,4,1,-1,9,3,-2,-10,-2,-3,5,-5,2,-8,-2,3,-1,5,6,-9,10,7,-6,8,-1,-6,-6,5,4,-6,-8,-6,-5,-9,5,-8,-3,-10,3,6,6,10,4,-1,-3,-7,-5,10,-3,2,8,-6,4,-9,-1,-3,-6,2,-10,-8,-7,4,9,-3,2,2,-5,10,-4,8,-3,-4,-6,8,-7,-9,-5,-8,6,9,-7,7,-1,1,5,9,-2,8,9,-2,-4,3,-5,-6,-2,-6,-7,-9,9,2,-1,5,-5,-1,-8,-5,5,4,10,-8,4,-1,6,-7,-2,-2,-1,-8,7,3,2,10,5,-5,1,-7,-7,5,-10,10,-3,-7,-9,-1,4,-4,1,4,-5,10,4,10,-8,7,-9,-10,-1,-5,3,9,-9,6,6,-5,-2,-6,6,10,-4,2,7,-6,-10,-1,8,-2,2,6,-9,8,9,8,1,-9,-8,-8,2,3,4,5,-3,-6,5,2,6,5,-3,1,4,9,-1,-7,1,-3,6,-5,-4,-6,5,-3,8,-6,-3,-7,7,9,4,-10,-7,-10,-10,-6,5,3,9,-3,-4,-2,-6,-3,8,10,9,-9,-3,-1,-3,7,-8,10,-6,8,1,-6,10,7,-3,-10,-7,9,5,10,9,-5,-10,6,-7,-6,4,-5,-1,-10,1,7,6,-5,7,8,5,-3,-10,2,3,8,-10,-10,5,-5,10,4,9,-7,-5,4,-2,-6,8,-2,6,8,2,6,10,6,5,-5,7,3,-9,-3,-6,3,-9,-6,-4,-2,4,6,1,-3,-9,-1,2,-10,2,4,-6,-5,4,1,-8,4,1,8,-9,-6,-3,7,-4,-8,4,-8,1,-7,-7,-2,-9,8,4,2,1,4,-9,-1,1,1,3,6,-3,10,-1,-6,9,-2,2,-10,2,-8,6,3,-9,3,-4,-10,3,-8,2,-5,-7,-6,1,-5,10,5,3,5,4,5,-8,6,5,-6,-7,-10,7,7,-3,-2,-6,-3,5,-2,-8,9,-6,-9,-9,9,-5,-2,6,2,-2,6,-1,10,7,-7,10,10,10,-6,6,7,-6,-6,10,4,4,1,-7,3,2,-8,7,10,-9,6,-4,7,-2,2,4,-4,-8,-6,-8,10,1,4,-7,-5,3,-4,-6,6,-5,-2,8,9,-2,10,6,-2,7,-8,10,-5,-7,-1,9,3,-8,4,10,2,10,4,2,-6,-1,7,8,-6,8,-9,5,-2,-4,10,2,10,4,10,9,6,2,3,5,6,7,10,-5,8,1,-5,-2,6,8,-3,-4,9,4,8,1,3,-7,-3,-7,4,-9,-10,-6,8,-2,3,1,4,3,-5,5,-4,10,7,-6,-5,1,-7,-2,1,7,-2,5,4,-7,2,-6,4,-2,5,-3,-7,8,9,1,5,-5,4,2,-6,6,1,-4,8,-8,-6,-5,-3,-6,-10,6,5,-2,-9,-7,-5,5,-7,-3,-7,-9,-1,-7,-5,1,-2,-3,-8,5,9,-4,-7,10,-10,-8,-5,-1,1,-3,2,2,-10,-10,9,-6,9,5,-1,-1,-10,-5,8,-3,3,-5,-1,9,-3,-2,4,3,9,3,-4,8,-7,-1,10,-6,-10,-8,-10], dtype = "uint16")#candidate|8021|(2560,)|const|uint16
call_8020 = relay.TupleGetItem(func_3190_call(relay.reshape(const_8021.astype('uint16'), [2560,])), 3)
call_8022 = relay.TupleGetItem(func_3192_call(relay.reshape(const_8021.astype('uint16'), [2560,])), 3)
output = relay.Tuple([call_8016,call_8020,const_8021,])
output2 = relay.Tuple([call_8017,call_8022,const_8021,])
func_8024 = relay.Function([], output)
mod['func_8024'] = func_8024
mod = relay.transform.InferType()(mod)
mutated_mod['func_8024'] = func_8024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8024_call = mutated_mod.get_global_var('func_8024')
call_8025 = func_8024_call()
output = call_8025
func_8026 = relay.Function([], output)
mutated_mod['func_8026'] = func_8026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6038_call = mod.get_global_var('func_6038')
func_6039_call = mutated_mod.get_global_var('func_6039')
call_8040 = relay.TupleGetItem(func_6038_call(), 1)
call_8041 = relay.TupleGetItem(func_6039_call(), 1)
func_4168_call = mod.get_global_var('func_4168')
func_4171_call = mutated_mod.get_global_var('func_4171')
const_8046 = relay.const([-5.655208,0.840440,4.007162,9.479784,7.970183,0.099841,7.099253,7.077260,-7.995211,6.192774,-6.113537,-5.347720,7.670358,-7.376985,5.316653,0.171652,-9.845923,3.192079,6.600444,4.477525,-4.728328,-9.606794,8.550977,-4.629612,7.264279,5.287070,-9.886162,-9.979092,-0.375653,-0.054769,-9.364386,7.600373,-3.811418,-8.384512,2.615988,-1.059264,1.062805,-6.897049,-1.456016,-0.520822,-9.973755,1.174514,2.677522,1.141019,-1.514486,6.347899,0.918666,-7.679251,6.083372,2.015343,-0.343608,-3.698226,-5.008805,-8.713488,-2.106455,-7.058325,0.848212,5.199879,-3.092598,-7.887690,-7.017295,0.185769,-2.402199,4.518480,4.132716,-1.046322,-3.794698,2.416741,6.797874,6.539783,-7.421284,7.246809,7.676099,-7.778217,9.332827,8.258697,-2.669770,4.031190,-8.780755,-3.310024,3.297124,5.252882,-4.466354,1.755687,6.983624,1.225472,-0.665679,8.358401,0.001597,5.117291,-7.543602,-1.985510,-9.104698,4.971339,-0.531062,-2.848252,-4.991339,2.761184,-8.429091,7.678515,3.107795,2.281857,6.366648,8.636010,-9.373019,9.556250,1.636661,4.984350,0.281246,-3.353184,-7.980841,8.280037,7.596869,9.179879,0.280476,7.507976,5.658091,3.774494,9.406494,6.056073,6.935234,-5.405685,-8.664277,-8.797954,-5.941525,1.939817,6.239916,1.512885,7.035389,-2.147235,0.130387,6.288062,-2.663622,0.749105,-7.028096,1.110175,1.942996,-0.237307,3.430283,5.103298,-2.135763,8.062347,-6.197986,-7.169625,3.232839,-5.844860,-9.670564,-5.602451,-0.888533,-9.997773,-9.683153,9.880325,8.361193,-9.075316,-0.708872,-5.359830,-5.265304,4.942448,-0.253908,9.356201,-3.208578,2.366758,4.204361,-7.161902,4.482210,-9.334228,-9.189319,-4.271889,-6.914496,8.194708,-9.545326,4.368653,1.029638,5.368070,-8.206131,5.568907,0.748066,5.146052,-2.258119,-2.452926,-0.395848,-1.539788,-7.509517,-5.570369,5.737835,-0.934159,6.118878,-8.110562,-5.442625,-9.362793,-2.425797,8.259354,-5.351392,3.531608,-9.528339,7.962070,-7.409885,-6.569281,-8.162140,9.614064,-2.328777,8.234337,9.249335,-9.787831,-3.921788,-2.891494,-3.630442,-6.676091,-4.534220,-1.054405,1.771350,8.889780,7.158623,9.908977,-7.265756,6.593770,-7.599390,-9.979629,-0.258648,3.072786,-0.955803,-4.271464,7.660784,7.814425,-0.435461,5.260909,7.952432,5.198660,-9.520315,-1.146985,-0.589136,6.880960,5.654729,-8.066638,-9.902473,-9.579429,-4.516713,6.196122,5.451221,3.105605,-2.384132,3.877290,-7.484378,-0.281215,0.340593,2.331629,-3.990754,-4.460793,2.792434,-3.917570,-7.516265,-2.052078,5.265905,2.667106,-1.647709,-6.129344,7.359066,7.189477,-9.299968,-1.310709,-7.641743,6.187417,-5.424872,-8.528893,2.346854,2.228534,0.640364,-2.846708,0.984873,9.448633,-5.820145,5.981629,-6.525232,2.580217,-4.669402,-8.522265,-8.733907,-7.570511,-7.669094,-9.442007,9.781914,4.368810,5.966202,6.525895,2.203146,-5.935773,-2.653949,0.168573,-8.095443,7.705472,-4.240775,-2.610182,-0.818754,2.096893,9.594824,-7.805283,4.860407,-0.910317,3.129072,-7.786061,-2.166410,-3.103409,-9.210889,7.963485,2.136497,5.061487,4.022173,-0.831773,-3.852439,-7.253277,6.973315,-9.223985,-7.038653,7.635984,-9.283484,1.125258,-8.309841,1.108734,6.234279,-7.687515,-5.508713,9.427394,2.838457,1.673569,3.852719,2.086450,-3.625897,-5.203306,-8.081369,-3.390865,2.234483,-9.245722,9.774442,-3.976632,-3.198545,6.656890,-0.755334,-1.287726,-5.772068,-4.194918,1.817832,-3.724254,8.455571,5.232237,-8.718041,2.257362,6.436995,-4.822436,1.515203,4.775964,0.636180,-4.967289,3.152309,5.342478,-3.414588,-9.934885,7.676372,9.494529,2.147870,1.490220,-2.494488,5.192899,-5.212190,8.938042,-4.624519,3.881361,6.758736,7.207773,4.977346,7.268018,-0.606308,7.907016,-7.212516,2.747127,8.834982,-3.196784,9.122312,9.659094,3.754162,5.801874,-6.092234,4.370437,3.153307,-3.220372,3.797872,-9.863421,4.449129,5.417590,7.075260,8.256908,1.519432,-3.377356,3.749568,-0.813917,-4.548841,-1.005364,3.326445,9.350995,9.107155,0.531604,4.332465,-5.991276,7.451641,-0.591815,-2.491215,-9.321409,1.731873,-8.299174,-7.476595,9.865136,2.253436,4.449966,7.046079,7.689661,1.242348,7.672501,-0.802182,4.395446,-5.908299,-6.984147,-5.444120,-1.432106,-8.551664,-7.385335,-2.824910,9.125965,-6.590433,-5.657176,0.962072,-0.658387,-4.709922,0.453557,3.510233,-9.025256,5.957210,6.111322,7.875573,0.011681,-6.114170,4.245118,-4.985556,-5.833618,6.165078,-8.049651,-3.852241,3.646332,6.153071,-0.940144,-5.803940,-5.290825,1.208812,3.307567,5.076956,-8.333418,-5.934294,-7.495429,0.296456,0.535929,7.117866,9.852510,-3.210835,-1.570184,-6.840140,0.312170,-0.420088,-8.364070,7.978804,-7.380576,-1.311838,-9.568147,-3.955672,7.192495,-4.058062,0.290067,9.646899,5.380238,8.174237,8.924603,-0.211716,-7.635453,-8.311064,8.231694,-8.802279,-0.870914,-2.648375,-1.290981,-3.532284,-1.742294,-1.955232,-8.351970,8.697315,-1.551813,-4.613034,-1.836457,-2.297564,0.949982,5.008965,-0.585232,-0.956430,-2.075533,7.386336,-3.043682,9.344379,-9.053704,-9.714091,5.815885,0.211285,-3.014938,6.585658,-9.188746,-1.910560,-3.944603,-1.721618,8.022303,8.672533,-7.578074,-1.172284,-1.577783,5.421034,-6.336829,-7.024882,6.473715,6.539459,8.116021,-4.939871,-8.454017,4.490144,-6.448945,2.378775,-7.686576,-3.057111,4.284526,2.161376,-2.082971,5.187086,-7.780159,-9.599043,8.759176,-3.681005,-2.013107,-1.951434,2.348767,1.738646,-5.165969,8.999860,6.217495,7.080786,2.457636,9.381140,5.677535,-8.884179,-7.242506,-1.887818,-7.792417,-7.288468,5.170271,9.064480,-2.949929,0.113668,2.980588,3.692316,-3.203194,7.757210,-6.941403,7.012079,0.337483,5.101318,-8.618223,5.250104,-5.557839,9.457437,3.286112,-9.285636,9.111126,-3.071747,1.073204,6.734286,-1.945139,0.638798,5.051493,-9.739962,-5.419907,-1.143122,3.331198,7.794987,5.416169,-8.395857,1.631209,-1.424208,-8.924967,7.870301,5.915912,4.080456,8.401895,-4.002430,2.791697,-5.910846,-9.133063,-1.751815,-1.235057,-5.874229,-1.067126,-6.973687,0.520477,-3.294724,9.950262,8.173070,-1.196814,-9.176863,4.823276,1.617773,-0.076912,-1.012811,-7.990195,-4.412380,-3.953013,1.134532,5.469971,-4.944640,-1.461347,-0.901159,-1.409534,-7.381273,-3.661236,6.247511,7.920611,-1.259241,-9.856625,0.180645,9.420724,2.466692,-8.257430,-7.900791,5.910279,-3.440876,6.081569,9.187636,5.117929,4.332986,0.035667,7.155625,0.680914,-7.071339,3.763344,-3.340417,7.998289,-4.036675,-5.486241,-3.333991,-9.082478,-7.986854,1.281005,7.048841,6.200916,4.013154,3.098849,-5.655133,-4.308756,-7.195588,-0.456988,1.327708,1.376513,1.447030,-8.745020,7.113688,-8.233580,5.358410,0.820533,-7.568403,5.872563,7.097360,7.967641,3.334584,-8.240817,3.530074,-9.933417,6.660002,-6.809965,-3.491240,-7.249883,5.084856,3.737756,-3.977426,-9.213262,1.007933,-1.905133,-1.744819,-2.536777,-7.836504,-5.478574,0.188854,-9.869266,-6.582977,4.499294,6.000120,-6.278946,5.190532,7.621667,-2.708602,-5.446241,2.155780,9.444941,-9.204317,7.661634,-7.417798,-1.369468,7.517321,-7.888226,-6.120886,-8.382454,4.842415,-3.396623,-2.377730,7.577879,1.955327,-8.793504,-9.625380,8.527940,-1.039468,1.612929,-0.768993,-4.619737,-8.598466,0.216831,5.387151,0.292977,-5.108705,9.415711,4.726372,3.606646,-7.874970,-8.505935,6.232642,-1.735934,-8.049681,8.719023,2.036720,-8.836305,-2.570079,-6.347855,7.371937,4.827149,-9.491601,-5.114644,9.211572,-5.295950,-0.136766,-7.862076,-6.706646,3.402244,0.425124,7.521472,-9.935951,-9.338322,5.544309,-6.955996,-6.475555,-6.589622,-6.855365,2.693766,9.000460,-7.830564,-4.818291,0.687818,6.257523,0.415846,4.075891,5.423370,4.131192,5.863090,2.606257,9.078969,0.131263,-4.899475,8.522799,6.184618,2.582726,-2.406323,-8.987249,6.620340,-3.855753,-4.660974,6.006669,4.377523,-8.952859,-0.509818,7.198793,8.346687,8.164908,-9.116425,3.682411,7.009694,1.651514,-0.855886,-7.549772,3.618004,9.589229,-1.714510,-7.728886,0.511303,-4.908415,-5.524542,4.358665,-6.543141,7.141521,8.020743,-9.297813,8.881687,-1.347853,-6.562151,7.834157,5.220681,7.880821,-7.834586,-2.406834,-9.978221,0.848105,-1.042611,3.867417,6.855229,9.009014,8.459819,-6.355166,-5.879291,4.245063], dtype = "float32")#candidate|8046|(825,)|const|float32
call_8045 = relay.TupleGetItem(func_4168_call(relay.reshape(const_8046.astype('float32'), [5, 11, 15])), 0)
call_8047 = relay.TupleGetItem(func_4171_call(relay.reshape(const_8046.astype('float32'), [5, 11, 15])), 0)
uop_8052 = relay.cos(const_8046.astype('float32')) # shape=(825,)
func_5204_call = mod.get_global_var('func_5204')
func_5209_call = mutated_mod.get_global_var('func_5209')
const_8060 = relay.const([[-5,-4,3,-9],[-3,-10,-5,4],[-1,-10,-6,6],[-9,5,-2,-4],[-10,-9,4,3],[-7,2,3,5],[9,-8,-2,-2],[-1,-7,-4,7],[9,6,-5,3],[-4,-4,-1,1],[-2,6,-3,7],[5,-4,-6,2],[8,1,9,-5],[-8,-7,8,8],[-5,6,-3,2],[8,7,-9,-9],[1,2,5,2],[-8,4,-7,8],[9,1,-8,7],[9,7,-7,4],[-10,5,-6,9],[-5,10,5,5],[-3,-5,-7,4],[-10,-3,9,2],[-6,5,3,-3],[-6,10,2,-7],[-2,-3,-7,-5],[8,-2,7,-6],[-3,2,4,-6],[-10,-4,-4,7],[-5,4,-7,-9],[-9,6,6,-9],[-3,-5,-8,-9],[-7,-3,8,-6],[-2,7,9,6],[8,4,-4,-3],[3,7,-8,2],[-3,-8,-4,-4],[-3,6,6,10],[6,7,8,-8],[-7,4,1,-3],[-10,-5,-5,3],[-1,-10,2,10],[7,-7,-7,-5],[10,-2,-3,7],[-7,-10,-3,-10],[1,-1,3,3],[9,2,5,-10],[7,9,-10,5],[-1,10,7,10],[4,-3,3,5],[-5,7,4,-6],[3,1,2,-1],[-3,10,-2,2],[-2,-3,2,-6],[-2,-7,-2,7],[10,9,6,-6],[-10,10,7,-10],[-6,3,-10,5],[3,10,8,-1],[7,-10,-9,-3],[5,4,5,10],[-8,1,1,10],[9,9,7,-4],[9,7,-2,-8],[-6,-10,8,-4],[10,-2,1,-5],[2,-6,4,-3],[-3,3,-3,-6],[-5,9,4,-2],[9,7,8,8],[8,10,3,-4],[-4,-6,2,-5],[8,-2,7,9],[8,6,2,5],[-10,-9,-8,1],[-4,10,-9,-2],[-1,9,8,4],[6,1,5,-7],[3,-8,-10,5],[-6,-9,2,-1],[-8,10,10,2],[-5,-5,1,5],[-7,6,-2,3],[-10,10,-8,6],[3,9,-2,-9],[-4,-9,-6,10],[9,-3,1,-6],[2,2,9,3],[-5,-3,-5,-6],[-7,-5,-1,-6],[-3,9,7,-4],[3,7,3,6],[-4,5,-3,8],[7,-5,-10,-1],[10,-8,7,-5],[9,6,4,10],[-1,9,7,4],[-3,-6,-9,-10],[9,7,-10,-8],[-6,1,-4,-10],[-9,9,-6,-1],[1,4,4,-1],[1,-9,-4,-10],[-1,2,5,10],[-3,-9,1,10],[7,4,-7,6],[-6,-1,-4,-1],[-5,10,-9,1],[1,-2,9,-4],[7,2,4,-4],[-3,-1,7,1],[6,-9,6,-8],[-9,9,2,6],[5,5,-4,-10],[-3,5,2,1],[1,-5,-1,4],[-3,8,10,5],[2,3,-9,4],[-5,-6,-8,8],[-7,6,6,-8],[5,-4,-1,-8],[-1,8,7,3],[-2,-10,-6,-10],[1,-2,6,-6],[7,-5,9,1],[8,9,1,7],[3,-4,6,-3],[-9,-2,7,5],[-7,4,6,3],[5,7,-6,-1],[-2,5,10,4],[2,-4,5,-5],[-10,8,4,-7],[-5,-9,1,-7],[7,-2,1,6],[-4,-4,-10,1],[8,7,1,5],[10,-7,3,5],[-8,-7,-3,-4],[-5,-5,-9,-6],[-4,-1,7,-10],[-7,10,-1,-10],[-4,-9,1,-5],[6,-1,6,4],[-2,-6,-10,-8],[5,8,2,6],[6,4,-3,-4],[-9,-5,-4,-5],[-3,-5,-9,-3],[10,-2,-1,10],[-8,-5,-3,1],[3,5,5,6],[-4,3,6,10],[7,-2,-2,6],[-7,10,-9,2],[-7,3,-8,7],[10,5,-4,-1],[7,-9,-6,-9],[-7,4,8,-2],[-4,4,-4,6],[-3,-9,8,-9],[-5,-3,7,-7],[1,-2,9,3],[-9,-7,-1,8],[-6,10,8,10],[-2,-6,7,3],[5,6,-9,9],[-7,10,1,-2],[4,-2,5,-8],[7,4,-5,9],[-2,4,-5,9],[9,-1,-9,1],[7,8,7,9],[-7,-7,9,2],[2,-1,1,8],[9,-4,2,-2],[9,3,5,10],[-2,-4,-5,-2],[-6,-4,3,9],[-1,2,8,-6],[-5,3,-8,2],[1,5,-4,-3],[-2,-9,8,8],[-1,-7,-6,6],[-2,1,-5,4],[-9,-4,-5,-5],[-3,-1,2,-4],[-2,2,6,9],[-10,-9,-3,2],[3,-5,2,-5],[-4,-10,8,9],[-7,-7,-2,10],[-7,8,-4,-2],[-6,-5,-6,-7],[-7,-7,1,4],[-1,-8,7,7],[-8,4,3,7],[2,10,-2,-10],[-4,-3,-5,2],[8,-10,-9,-9],[-10,-9,6,4],[7,7,3,-8],[4,-5,-8,8],[-8,-1,3,-5],[2,8,9,-5],[8,-6,9,1],[5,6,-4,1],[1,2,-3,-7],[-1,2,-8,8],[1,8,-8,-5],[6,8,6,-1],[-3,-2,-10,-1],[3,2,-4,-7],[4,7,8,-7],[-5,-4,4,9],[10,6,-8,2],[-2,-5,5,-1],[9,3,10,-2],[4,-6,-3,8],[6,-3,2,-8],[-10,-3,6,7],[2,5,-9,8],[6,2,1,-3],[3,-1,-3,-1],[3,9,-8,7],[4,3,-10,9],[-7,5,10,-2],[6,-9,-2,2],[-2,5,5,1],[3,-5,5,10],[4,7,-3,-10],[-2,-8,9,2],[-8,3,-10,-5],[6,-7,-5,-10],[-2,4,8,4],[2,6,1,5],[4,3,10,-8],[-9,7,2,4],[8,9,3,-6],[7,-8,-10,8],[-9,-10,2,-5],[-3,-4,2,10],[5,6,5,4],[-3,-2,3,9],[-2,1,6,-4],[8,5,7,2],[5,1,9,3],[6,-7,5,1],[6,1,7,1],[7,-7,-1,8],[8,-7,-5,-1],[4,-1,3,-6],[3,-10,-7,6],[-9,8,-6,10],[-4,-1,5,-1],[9,10,2,-2],[5,5,-5,6],[8,5,-8,5],[2,-2,-7,8],[3,-9,-5,-9],[-3,4,7,-1],[4,6,3,-6],[9,-3,-1,2],[10,10,-2,-10],[5,-10,-6,9],[1,3,-9,8],[-9,4,-2,3],[-10,9,-1,-7],[-5,-1,2,-10]], dtype = "int16")#candidate|8060|(270, 4)|const|int16
var_8061 = relay.var("var_8061", dtype = "float32", shape = (330,))#candidate|8061|(330,)|var|float32
call_8059 = relay.TupleGetItem(func_5204_call(relay.reshape(const_8060.astype('int16'), [12, 15, 6]), relay.reshape(const_8060.astype('int16'), [12, 15, 6]), relay.reshape(var_8061.astype('float32'), [330,]), relay.reshape(const_8060.astype('uint64'), [12, 15, 6]), ), 4)
call_8062 = relay.TupleGetItem(func_5209_call(relay.reshape(const_8060.astype('int16'), [12, 15, 6]), relay.reshape(const_8060.astype('int16'), [12, 15, 6]), relay.reshape(var_8061.astype('float32'), [330,]), relay.reshape(const_8060.astype('uint64'), [12, 15, 6]), ), 4)
func_5363_call = mod.get_global_var('func_5363')
func_5367_call = mutated_mod.get_global_var('func_5367')
var_8064 = relay.var("var_8064", dtype = "float64", shape = ())#candidate|8064|()|var|float64
var_8065 = relay.var("var_8065", dtype = "uint16", shape = (2,))#candidate|8065|(2,)|var|uint16
var_8066 = relay.var("var_8066", dtype = "uint16", shape = (2560,))#candidate|8066|(2560,)|var|uint16
call_8063 = relay.TupleGetItem(func_5363_call(relay.reshape(var_8064.astype('float64'), []), relay.reshape(var_8065.astype('uint16'), [2, 1]), relay.reshape(var_8066.astype('uint16'), [2560,]), ), 5)
call_8067 = relay.TupleGetItem(func_5367_call(relay.reshape(var_8064.astype('float64'), []), relay.reshape(var_8065.astype('uint16'), [2, 1]), relay.reshape(var_8066.astype('uint16'), [2560,]), ), 5)
var_8068 = relay.var("var_8068", dtype = "float32", shape = (825,))#candidate|8068|(825,)|var|float32
bop_8069 = relay.floor_divide(uop_8052.astype('float32'), relay.reshape(var_8068.astype('float32'), relay.shape_of(uop_8052))) # shape=(825,)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_8081 = func_3060_call()
call_8082 = func_3060_call()
output = relay.Tuple([call_8040,call_8045,call_8059,const_8060,var_8061,call_8063,var_8064,var_8065,var_8066,bop_8069,call_8081,])
output2 = relay.Tuple([call_8041,call_8047,call_8062,const_8060,var_8061,call_8067,var_8064,var_8065,var_8066,bop_8069,call_8082,])
func_8085 = relay.Function([var_8061,var_8064,var_8065,var_8066,var_8068,], output)
mod['func_8085'] = func_8085
mod = relay.transform.InferType()(mod)
var_8086 = relay.var("var_8086", dtype = "float32", shape = (330,))#candidate|8086|(330,)|var|float32
var_8087 = relay.var("var_8087", dtype = "float64", shape = ())#candidate|8087|()|var|float64
var_8088 = relay.var("var_8088", dtype = "uint16", shape = (2,))#candidate|8088|(2,)|var|uint16
var_8089 = relay.var("var_8089", dtype = "uint16", shape = (2560,))#candidate|8089|(2560,)|var|uint16
var_8090 = relay.var("var_8090", dtype = "float32", shape = (825,))#candidate|8090|(825,)|var|float32
output = func_8085(var_8086,var_8087,var_8088,var_8089,var_8090,)
func_8091 = relay.Function([var_8086,var_8087,var_8088,var_8089,var_8090,], output)
mutated_mod['func_8091'] = func_8091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_8151 = relay.TupleGetItem(func_2781_call(), 0)
call_8152 = relay.TupleGetItem(func_2782_call(), 0)
output = relay.Tuple([call_8151,])
output2 = relay.Tuple([call_8152,])
func_8158 = relay.Function([], output)
mod['func_8158'] = func_8158
mod = relay.transform.InferType()(mod)
mutated_mod['func_8158'] = func_8158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8158_call = mutated_mod.get_global_var('func_8158')
call_8159 = func_8158_call()
output = call_8159
func_8160 = relay.Function([], output)
mutated_mod['func_8160'] = func_8160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2509_call = mod.get_global_var('func_2509')
func_2511_call = mutated_mod.get_global_var('func_2511')
call_8187 = func_2509_call()
call_8188 = func_2509_call()
func_3659_call = mod.get_global_var('func_3659')
func_3664_call = mutated_mod.get_global_var('func_3664')
var_8190 = relay.var("var_8190", dtype = "float32", shape = ())#candidate|8190|()|var|float32
var_8191 = relay.var("var_8191", dtype = "uint16", shape = (54,))#candidate|8191|(54,)|var|uint16
call_8189 = relay.TupleGetItem(func_3659_call(relay.reshape(var_8190.astype('float32'), []), relay.reshape(var_8191.astype('uint16'), [54,]), relay.reshape(var_8191.astype('uint16'), [54,]), ), 3)
call_8192 = relay.TupleGetItem(func_3664_call(relay.reshape(var_8190.astype('float32'), []), relay.reshape(var_8191.astype('uint16'), [54,]), relay.reshape(var_8191.astype('uint16'), [54,]), ), 3)
func_4968_call = mod.get_global_var('func_4968')
func_4969_call = mutated_mod.get_global_var('func_4969')
call_8194 = func_4968_call()
call_8195 = func_4968_call()
bop_8200 = relay.greater_equal(call_8194.astype('bool'), relay.reshape(call_8187.astype('bool'), relay.shape_of(call_8194))) # shape=(15, 11)
bop_8203 = relay.greater_equal(call_8195.astype('bool'), relay.reshape(call_8188.astype('bool'), relay.shape_of(call_8195))) # shape=(15, 11)
output = relay.Tuple([call_8189,var_8190,var_8191,bop_8200,])
output2 = relay.Tuple([call_8192,var_8190,var_8191,bop_8203,])
func_8205 = relay.Function([var_8190,var_8191,], output)
mod['func_8205'] = func_8205
mod = relay.transform.InferType()(mod)
var_8206 = relay.var("var_8206", dtype = "float32", shape = ())#candidate|8206|()|var|float32
var_8207 = relay.var("var_8207", dtype = "uint16", shape = (54,))#candidate|8207|(54,)|var|uint16
output = func_8205(var_8206,var_8207,)
func_8208 = relay.Function([var_8206,var_8207,], output)
mutated_mod['func_8208'] = func_8208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7685_call = mod.get_global_var('func_7685')
func_7687_call = mutated_mod.get_global_var('func_7687')
call_8252 = relay.TupleGetItem(func_7685_call(), 1)
call_8253 = relay.TupleGetItem(func_7687_call(), 1)
output = relay.Tuple([call_8252,])
output2 = relay.Tuple([call_8253,])
func_8264 = relay.Function([], output)
mod['func_8264'] = func_8264
mod = relay.transform.InferType()(mod)
output = func_8264()
func_8265 = relay.Function([], output)
mutated_mod['func_8265'] = func_8265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7286_call = mod.get_global_var('func_7286')
func_7288_call = mutated_mod.get_global_var('func_7288')
call_8266 = relay.TupleGetItem(func_7286_call(), 0)
call_8267 = relay.TupleGetItem(func_7288_call(), 0)
func_7324_call = mod.get_global_var('func_7324')
func_7326_call = mutated_mod.get_global_var('func_7326')
var_8269 = relay.var("var_8269", dtype = "uint16", shape = (38400,))#candidate|8269|(38400,)|var|uint16
call_8268 = relay.TupleGetItem(func_7324_call(relay.reshape(var_8269.astype('uint16'), [2560, 15])), 1)
call_8270 = relay.TupleGetItem(func_7326_call(relay.reshape(var_8269.astype('uint16'), [2560, 15])), 1)
func_6460_call = mod.get_global_var('func_6460')
func_6461_call = mutated_mod.get_global_var('func_6461')
call_8278 = func_6460_call()
call_8279 = func_6460_call()
func_6857_call = mod.get_global_var('func_6857')
func_6859_call = mutated_mod.get_global_var('func_6859')
call_8308 = relay.TupleGetItem(func_6857_call(), 0)
call_8309 = relay.TupleGetItem(func_6859_call(), 0)
output = relay.Tuple([call_8266,call_8268,var_8269,call_8278,call_8308,])
output2 = relay.Tuple([call_8267,call_8270,var_8269,call_8279,call_8309,])
func_8314 = relay.Function([var_8269,], output)
mod['func_8314'] = func_8314
mod = relay.transform.InferType()(mod)
var_8315 = relay.var("var_8315", dtype = "uint16", shape = (38400,))#candidate|8315|(38400,)|var|uint16
output = func_8314(var_8315)
func_8316 = relay.Function([var_8315], output)
mutated_mod['func_8316'] = func_8316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8333 = relay.var("var_8333", dtype = "float32", shape = (14, 2))#candidate|8333|(14, 2)|var|float32
uop_8334 = relay.asin(var_8333.astype('float32')) # shape=(14, 2)
output = relay.Tuple([uop_8334,])
output2 = relay.Tuple([uop_8334,])
func_8338 = relay.Function([var_8333,], output)
mod['func_8338'] = func_8338
mod = relay.transform.InferType()(mod)
var_8339 = relay.var("var_8339", dtype = "float32", shape = (14, 2))#candidate|8339|(14, 2)|var|float32
output = func_8338(var_8339)
func_8340 = relay.Function([var_8339], output)
mutated_mod['func_8340'] = func_8340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8351 = relay.var("var_8351", dtype = "float64", shape = (12, 13, 15))#candidate|8351|(12, 13, 15)|var|float64
uop_8352 = relay.asinh(var_8351.astype('float64')) # shape=(12, 13, 15)
output = relay.Tuple([uop_8352,])
output2 = relay.Tuple([uop_8352,])
func_8356 = relay.Function([var_8351,], output)
mod['func_8356'] = func_8356
mod = relay.transform.InferType()(mod)
var_8357 = relay.var("var_8357", dtype = "float64", shape = (12, 13, 15))#candidate|8357|(12, 13, 15)|var|float64
output = func_8356(var_8357)
func_8358 = relay.Function([var_8357], output)
mutated_mod['func_8358'] = func_8358
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8413 = relay.var("var_8413", dtype = "float64", shape = (9, 3, 12))#candidate|8413|(9, 3, 12)|var|float64
uop_8414 = relay.erf(var_8413.astype('float64')) # shape=(9, 3, 12)
func_3311_call = mod.get_global_var('func_3311')
func_3313_call = mutated_mod.get_global_var('func_3313')
const_8417 = relay.const([2.442620,7.311168,-5.574659,6.578424,-1.315620,2.442016,9.215767,-1.485822,8.376331,-3.857616,1.211136,-0.050524,3.705220,0.176611,1.640006,8.473389,2.286638,-8.055425,6.191550,-0.107111,-4.717131,-8.964895,-5.735009,1.949848,-2.148396,0.753642,3.074126,-5.428791,-4.145106,1.234010,-3.497242,1.432785,7.744141,2.142369,9.138662,-8.003067,8.470057,-9.943530,5.487217,-3.068030,4.733725,-2.576457,8.027292,8.838226,-8.088756,6.149485,0.478337,2.017647,-6.235059,-0.425676,-1.488106,-9.948926,4.236802,7.252069,-9.736349,-4.350682,-0.438742,-0.336573,9.329881,0.003781,-0.771666,8.269116,8.002615,-3.224756,7.296997,-8.905341,-1.115546,-3.694086,6.704571,-9.736751,5.263237,2.435437,3.972217,8.600916,5.366112,8.308060,4.980313,-8.281466,4.011994,6.236746,3.618622,-9.594046,-8.609761,2.801186,-9.376657,7.187436,1.171780,2.503301,-1.953514,1.285436,-1.681423,3.527826,2.461111,-7.188062,-3.236518,-6.894244,6.620296,3.925656,6.690506,2.324445,3.389189,2.102037,0.269978,6.657154,2.993538,-8.180477,0.337522,8.805019,8.084639,7.632009,0.298327,9.483199,-1.839416,-7.347260,0.894521,-9.418627,-2.092409,0.154661,-0.960986,2.977777,-4.223626,0.711947,5.506429,-5.548588,9.508986,7.545993,1.793137,3.884943,7.406459,4.833098,-1.327473,0.139590,4.910329,-0.322610,-7.402171,8.678383,3.508523,-9.064510,-4.321704,9.526520,1.976221,-9.341743,2.507437,-7.294017,-2.364246,-7.203203,5.426078,8.133033,-8.593728,5.179225,-2.379887,4.965174,4.179357,-7.536417,1.025079,2.780223,-9.562294,4.968875,-4.036587,3.775768,-5.103047,9.791872,8.834786,-6.805368,-8.996530,-4.022377,7.586562,6.175970,-9.263315,-3.926872,4.085462,-5.209581,8.218812,-8.740733,0.338910,-9.205426,8.195866,-7.256640,7.631246,-7.892211,-2.230111,-7.399594,7.722020,-2.597153,3.597944,3.971005,8.189466,5.177561,4.935356,-3.508093,5.799144,-3.337923,-4.749920,3.099568,-5.654348,0.826144,0.827009,-9.180966,4.320934,-8.079965,4.489801,-5.244052,1.735544,7.048886,4.441168,3.511398,3.827982,0.591144,-9.459348,3.484397,-2.658582,3.700237,-4.079385,-7.767016,1.437291,-5.642027,-1.647331,0.818997,-1.266292,3.346684,-8.594770,-8.771588,-8.432980,1.622922,5.762383,2.905873,0.433252,8.654147,-2.500678,-4.692014,-3.116147,-7.039684,9.277393,-3.911448,1.175414,9.061259,-4.256484,8.173907,3.539806,-6.025727,0.723329,-2.143139,-8.256153,-2.752861,-9.233052,-3.153578,8.983814,8.344597,-9.873684,1.180813,1.640784,6.020751,-3.800767,4.101697,2.564460,-6.242516,4.220600,-4.487148,-3.187560,7.844097,7.394252,1.952503,-8.682022,4.873824,-9.553711,-0.916942,7.842072,-7.197250,-4.307126,6.087275,5.472489,-9.512787,-3.860616,-0.462273,8.829168,5.882626,-7.966053,-2.126158,-4.521517,3.800141,-4.062732,-0.841028,-8.877096,4.237510,-8.856073,-7.280685,7.533601,9.637727,0.926524,-5.073511,1.397866,6.483570,9.666968,-9.885383,9.117062,-8.971555,-0.113894,4.978726,3.999200,0.525708,9.664077,3.942725,0.668484,0.087481,8.118764,9.974893,5.084306,-6.803758,-3.518153,-8.303605,-1.566798,9.964829,-6.893652,6.055196,-3.343133,7.926747,6.629040,-9.173083,9.712006,2.973279,8.866932,1.596484,-5.873746,3.061875,9.389603,-4.992585,7.230783,-5.113897,7.994110,4.766362,-5.267693,4.825987,-0.814572,-3.357079,1.206198,-3.493427], dtype = "float64")#candidate|8417|(336,)|const|float64
call_8416 = func_3311_call(relay.reshape(const_8417.astype('float64'), [7, 4, 12]))
call_8418 = func_3311_call(relay.reshape(const_8417.astype('float64'), [7, 4, 12]))
func_8205_call = mod.get_global_var('func_8205')
func_8208_call = mutated_mod.get_global_var('func_8208')
var_8423 = relay.var("var_8423", dtype = "float32", shape = ())#candidate|8423|()|var|float32
var_8424 = relay.var("var_8424", dtype = "uint16", shape = (54,))#candidate|8424|(54,)|var|uint16
call_8422 = relay.TupleGetItem(func_8205_call(relay.reshape(var_8423.astype('float32'), []), relay.reshape(var_8424.astype('uint16'), [54,]), ), 1)
call_8425 = relay.TupleGetItem(func_8208_call(relay.reshape(var_8423.astype('float32'), []), relay.reshape(var_8424.astype('uint16'), [54,]), ), 1)
func_1055_call = mod.get_global_var('func_1055')
func_1058_call = mutated_mod.get_global_var('func_1058')
var_8429 = relay.var("var_8429", dtype = "float64", shape = (99, 2))#candidate|8429|(99, 2)|var|float64
call_8428 = func_1055_call(relay.reshape(var_8429.astype('float64'), [3, 11, 6]))
call_8430 = func_1055_call(relay.reshape(var_8429.astype('float64'), [3, 11, 6]))
output = relay.Tuple([uop_8414,call_8416,const_8417,call_8422,var_8423,var_8424,call_8428,var_8429,])
output2 = relay.Tuple([uop_8414,call_8418,const_8417,call_8425,var_8423,var_8424,call_8430,var_8429,])
func_8437 = relay.Function([var_8413,var_8423,var_8424,var_8429,], output)
mod['func_8437'] = func_8437
mod = relay.transform.InferType()(mod)
mutated_mod['func_8437'] = func_8437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8437_call = mutated_mod.get_global_var('func_8437')
var_8439 = relay.var("var_8439", dtype = "float64", shape = (9, 3, 12))#candidate|8439|(9, 3, 12)|var|float64
var_8440 = relay.var("var_8440", dtype = "float32", shape = ())#candidate|8440|()|var|float32
var_8441 = relay.var("var_8441", dtype = "uint16", shape = (54,))#candidate|8441|(54,)|var|uint16
var_8442 = relay.var("var_8442", dtype = "float64", shape = (99, 2))#candidate|8442|(99, 2)|var|float64
call_8438 = func_8437_call(var_8439,var_8440,var_8441,var_8442,)
output = call_8438
func_8443 = relay.Function([var_8439,var_8440,var_8441,var_8442,], output)
mutated_mod['func_8443'] = func_8443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4942_call = mod.get_global_var('func_4942')
func_4943_call = mutated_mod.get_global_var('func_4943')
call_8453 = relay.TupleGetItem(func_4942_call(), 0)
call_8454 = relay.TupleGetItem(func_4943_call(), 0)
output = relay.Tuple([call_8453,])
output2 = relay.Tuple([call_8454,])
func_8467 = relay.Function([], output)
mod['func_8467'] = func_8467
mod = relay.transform.InferType()(mod)
mutated_mod['func_8467'] = func_8467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8467_call = mutated_mod.get_global_var('func_8467')
call_8468 = func_8467_call()
output = call_8468
func_8469 = relay.Function([], output)
mutated_mod['func_8469'] = func_8469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8158_call = mod.get_global_var('func_8158')
func_8160_call = mutated_mod.get_global_var('func_8160')
call_8485 = relay.TupleGetItem(func_8158_call(), 0)
call_8486 = relay.TupleGetItem(func_8160_call(), 0)
output = relay.Tuple([call_8485,])
output2 = relay.Tuple([call_8486,])
func_8491 = relay.Function([], output)
mod['func_8491'] = func_8491
mod = relay.transform.InferType()(mod)
output = func_8491()
func_8492 = relay.Function([], output)
mutated_mod['func_8492'] = func_8492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5238_call = mod.get_global_var('func_5238')
func_5239_call = mutated_mod.get_global_var('func_5239')
call_8505 = relay.TupleGetItem(func_5238_call(), 0)
call_8506 = relay.TupleGetItem(func_5239_call(), 0)
output = call_8505
output2 = call_8506
func_8511 = relay.Function([], output)
mod['func_8511'] = func_8511
mod = relay.transform.InferType()(mod)
mutated_mod['func_8511'] = func_8511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8511_call = mutated_mod.get_global_var('func_8511')
call_8512 = func_8511_call()
output = call_8512
func_8513 = relay.Function([], output)
mutated_mod['func_8513'] = func_8513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3456_call = mod.get_global_var('func_3456')
func_3457_call = mutated_mod.get_global_var('func_3457')
call_8541 = relay.TupleGetItem(func_3456_call(), 0)
call_8542 = relay.TupleGetItem(func_3457_call(), 0)
output = relay.Tuple([call_8541,])
output2 = relay.Tuple([call_8542,])
func_8545 = relay.Function([], output)
mod['func_8545'] = func_8545
mod = relay.transform.InferType()(mod)
output = func_8545()
func_8546 = relay.Function([], output)
mutated_mod['func_8546'] = func_8546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7562_call = mod.get_global_var('func_7562')
func_7564_call = mutated_mod.get_global_var('func_7564')
call_8624 = relay.TupleGetItem(func_7562_call(), 1)
call_8625 = relay.TupleGetItem(func_7564_call(), 1)
output = relay.Tuple([call_8624,])
output2 = relay.Tuple([call_8625,])
func_8639 = relay.Function([], output)
mod['func_8639'] = func_8639
mod = relay.transform.InferType()(mod)
mutated_mod['func_8639'] = func_8639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8639_call = mutated_mod.get_global_var('func_8639')
call_8640 = func_8639_call()
output = call_8640
func_8641 = relay.Function([], output)
mutated_mod['func_8641'] = func_8641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_8659 = func_2649_call()
call_8660 = func_2649_call()
func_7111_call = mod.get_global_var('func_7111')
func_7112_call = mutated_mod.get_global_var('func_7112')
call_8661 = relay.TupleGetItem(func_7111_call(), 0)
call_8662 = relay.TupleGetItem(func_7112_call(), 0)
func_2649_call = mod.get_global_var('func_2649')
func_2650_call = mutated_mod.get_global_var('func_2650')
call_8682 = func_2649_call()
call_8683 = func_2649_call()
func_6563_call = mod.get_global_var('func_6563')
func_6565_call = mutated_mod.get_global_var('func_6565')
call_8685 = relay.TupleGetItem(func_6563_call(), 0)
call_8686 = relay.TupleGetItem(func_6565_call(), 0)
output = relay.Tuple([call_8659,call_8661,call_8682,call_8685,])
output2 = relay.Tuple([call_8660,call_8662,call_8683,call_8686,])
func_8693 = relay.Function([], output)
mod['func_8693'] = func_8693
mod = relay.transform.InferType()(mod)
mutated_mod['func_8693'] = func_8693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8693_call = mutated_mod.get_global_var('func_8693')
call_8694 = func_8693_call()
output = call_8694
func_8695 = relay.Function([], output)
mutated_mod['func_8695'] = func_8695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6038_call = mod.get_global_var('func_6038')
func_6039_call = mutated_mod.get_global_var('func_6039')
call_8716 = relay.TupleGetItem(func_6038_call(), 1)
call_8717 = relay.TupleGetItem(func_6039_call(), 1)
func_4942_call = mod.get_global_var('func_4942')
func_4943_call = mutated_mod.get_global_var('func_4943')
call_8723 = relay.TupleGetItem(func_4942_call(), 0)
call_8724 = relay.TupleGetItem(func_4943_call(), 0)
output = relay.Tuple([call_8716,call_8723,])
output2 = relay.Tuple([call_8717,call_8724,])
func_8726 = relay.Function([], output)
mod['func_8726'] = func_8726
mod = relay.transform.InferType()(mod)
mutated_mod['func_8726'] = func_8726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8726_call = mutated_mod.get_global_var('func_8726')
call_8727 = func_8726_call()
output = call_8727
func_8728 = relay.Function([], output)
mutated_mod['func_8728'] = func_8728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8545_call = mod.get_global_var('func_8545')
func_8546_call = mutated_mod.get_global_var('func_8546')
call_8744 = relay.TupleGetItem(func_8545_call(), 0)
call_8745 = relay.TupleGetItem(func_8546_call(), 0)
func_5109_call = mod.get_global_var('func_5109')
func_5112_call = mutated_mod.get_global_var('func_5112')
var_8750 = relay.var("var_8750", dtype = "uint32", shape = (630, 4))#candidate|8750|(630, 4)|var|uint32
call_8749 = relay.TupleGetItem(func_5109_call(relay.reshape(var_8750.astype('uint32'), [630, 4])), 4)
call_8751 = relay.TupleGetItem(func_5112_call(relay.reshape(var_8750.astype('uint32'), [630, 4])), 4)
func_4851_call = mod.get_global_var('func_4851')
func_4852_call = mutated_mod.get_global_var('func_4852')
call_8753 = relay.TupleGetItem(func_4851_call(), 0)
call_8754 = relay.TupleGetItem(func_4852_call(), 0)
output = relay.Tuple([call_8744,call_8749,var_8750,call_8753,])
output2 = relay.Tuple([call_8745,call_8751,var_8750,call_8754,])
func_8759 = relay.Function([var_8750,], output)
mod['func_8759'] = func_8759
mod = relay.transform.InferType()(mod)
var_8760 = relay.var("var_8760", dtype = "uint32", shape = (630, 4))#candidate|8760|(630, 4)|var|uint32
output = func_8759(var_8760)
func_8761 = relay.Function([var_8760], output)
mutated_mod['func_8761'] = func_8761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6010_call = mutated_mod.get_global_var('func_6010')
call_8811 = func_6009_call()
call_8812 = func_6009_call()
func_3332_call = mod.get_global_var('func_3332')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_8820 = relay.TupleGetItem(func_3332_call(), 0)
call_8821 = relay.TupleGetItem(func_3333_call(), 0)
func_8437_call = mod.get_global_var('func_8437')
func_8443_call = mutated_mod.get_global_var('func_8443')
const_8824 = relay.const([[-3.859128,-3.756448,-4.680986,-9.611913,-1.933543,6.894475],[-8.659524,-6.425220,4.055613,5.830048,1.047278,-6.590703],[-3.194051,-9.104868,-2.087483,-2.823302,-5.320624,-7.137111],[-0.288803,2.125708,-3.546099,8.099581,2.535784,-5.842776],[-6.300367,-8.420873,8.021711,0.618732,-9.619633,-5.150647],[0.416093,-8.043266,-4.519878,8.722101,2.539295,8.543543],[9.789090,-0.744078,-4.485049,0.980033,-0.425601,-0.618115],[-4.108428,5.903074,-8.995748,-8.192758,6.295680,3.030491],[8.771614,-4.333828,9.875608,-7.811776,-4.395914,-0.693685],[7.546287,-0.991165,0.457797,4.443930,-6.467385,8.568546],[7.829894,2.864326,-1.612320,-2.119669,2.315226,-7.714439],[-0.855413,6.426666,9.876122,5.783289,7.573696,-3.134285],[3.530072,2.394249,0.154389,-2.887833,-5.815546,7.718013],[-8.556108,-2.457514,-6.721615,-3.159822,8.780669,-5.284886],[9.057062,-4.322284,2.911379,-5.211567,-4.371498,-9.853304],[-9.103620,-6.943912,-1.347912,3.533019,5.290812,-9.338881],[-3.067582,-6.782105,-9.725472,-2.417371,4.032081,7.172879],[5.004623,4.795951,2.177028,1.374668,-9.007568,-8.837665],[4.305005,9.574876,7.452137,8.303666,-7.837554,2.622085],[-6.658473,2.877348,-7.764424,-1.030824,-2.164140,-8.562912],[0.782385,6.932319,3.675050,1.325954,1.201355,-3.730376],[-8.466955,-4.459165,2.975607,-6.763176,6.540480,8.694176],[-4.522496,5.605680,2.369909,-3.850045,-8.668150,-4.099321],[2.132507,-2.929715,-8.247352,0.761508,-0.492341,-9.305451],[4.231935,2.036096,-4.126243,1.333793,-1.064809,8.383009],[-5.178051,2.842080,0.461614,-2.108503,8.299353,8.080225],[3.516127,-0.534125,-2.660522,-8.338641,2.344155,-9.772576],[-1.425983,-9.842444,-4.536615,5.798511,9.416298,3.538665],[-7.483580,7.463102,5.296515,-8.924908,1.841322,-5.707216],[8.097547,-5.781241,0.875219,-6.685805,-9.410592,-1.454505],[-1.706601,1.252524,-6.484817,-7.174640,-8.844377,-4.141458],[-4.868537,3.493976,-4.738761,7.503264,-3.423008,-4.541136],[-3.820564,5.690949,-3.621804,8.922432,2.321208,-2.574427],[-8.425348,3.690782,3.244318,-6.655158,-2.002641,2.327752],[1.203038,-3.949387,-9.935689,6.598422,9.263801,9.119979],[7.125450,-8.278678,7.460621,-5.549386,2.532834,3.110722],[-8.350542,-2.160783,8.194568,4.178761,-6.988219,-1.062164],[-3.146942,0.381512,-8.333700,4.751585,0.965421,8.078138],[1.911733,-1.649003,7.004714,1.986803,0.943238,-5.456103],[6.423978,-9.490921,8.179636,5.669405,-1.611298,5.032685],[2.796952,-5.829508,-9.029551,-0.348002,-0.922945,-6.389873],[-0.150947,3.696883,0.666772,-2.230868,0.347787,-4.628111],[5.010816,-8.429924,-5.799865,-6.200800,7.406386,-0.467442],[-8.920942,5.250419,-7.691488,-8.864857,5.861945,-0.298690],[3.593949,5.354880,8.638585,6.420672,6.147257,1.959552],[2.024669,-0.214626,-8.551384,-8.223266,7.839010,4.460147],[3.914238,-5.373622,8.481450,2.019280,0.666705,0.351170],[-1.528315,9.470862,5.022886,7.957477,-1.125123,3.613917],[8.682483,-7.150719,9.181537,-0.465803,8.833351,5.953164],[9.692689,-6.351513,2.433786,-0.136070,-9.752718,-0.147431],[-0.461080,9.109454,9.650798,5.026079,-4.841712,8.890225],[-0.878454,7.309607,-8.596377,-0.180513,5.508545,-5.100089],[8.039087,8.943082,-4.008614,1.639611,1.634105,5.358120],[7.526613,0.544214,-0.545635,1.648588,-7.856236,6.076963]], dtype = "float64")#candidate|8824|(54, 6)|const|float64
const_8825 = relay.const(9.831663, dtype = "float32")#candidate|8825|()|const|float32
var_8826 = relay.var("var_8826", dtype = "uint16", shape = (54,))#candidate|8826|(54,)|var|uint16
var_8827 = relay.var("var_8827", dtype = "float64", shape = (198,))#candidate|8827|(198,)|var|float64
call_8823 = relay.TupleGetItem(func_8437_call(relay.reshape(const_8824.astype('float64'), [9, 3, 12]), relay.reshape(const_8825.astype('float32'), []), relay.reshape(var_8826.astype('uint16'), [54,]), relay.reshape(var_8827.astype('float64'), [99, 2]), ), 5)
call_8828 = relay.TupleGetItem(func_8443_call(relay.reshape(const_8824.astype('float64'), [9, 3, 12]), relay.reshape(const_8825.astype('float32'), []), relay.reshape(var_8826.astype('uint16'), [54,]), relay.reshape(var_8827.astype('float64'), [99, 2]), ), 5)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_8833 = relay.TupleGetItem(func_2781_call(), 1)
call_8834 = relay.TupleGetItem(func_2782_call(), 1)
output = relay.Tuple([call_8811,call_8820,call_8823,const_8824,const_8825,var_8826,var_8827,call_8833,])
output2 = relay.Tuple([call_8812,call_8821,call_8828,const_8824,const_8825,var_8826,var_8827,call_8834,])
func_8836 = relay.Function([var_8826,var_8827,], output)
mod['func_8836'] = func_8836
mod = relay.transform.InferType()(mod)
mutated_mod['func_8836'] = func_8836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8836_call = mutated_mod.get_global_var('func_8836')
var_8838 = relay.var("var_8838", dtype = "uint16", shape = (54,))#candidate|8838|(54,)|var|uint16
var_8839 = relay.var("var_8839", dtype = "float64", shape = (198,))#candidate|8839|(198,)|var|float64
call_8837 = func_8836_call(var_8838,var_8839,)
output = call_8837
func_8840 = relay.Function([var_8838,var_8839,], output)
mutated_mod['func_8840'] = func_8840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6857_call = mod.get_global_var('func_6857')
func_6859_call = mutated_mod.get_global_var('func_6859')
call_8850 = relay.TupleGetItem(func_6857_call(), 0)
call_8851 = relay.TupleGetItem(func_6859_call(), 0)
func_8759_call = mod.get_global_var('func_8759')
func_8761_call = mutated_mod.get_global_var('func_8761')
const_8894 = relay.const([3,4,-5,3,2,10,1,-2,7,10,3,3,3,2,-2,5,-2,-1,6,10,5,-5,-5,3,-7,4,-1,10,2,-6,-10,-10,-3,-1,4,7,1,-8,-1,10,6,-7,-1,-10,8,-9,-8,3,9,10,-5,-3,-1,5,-1,-9,1,3,3,-6,1,9,4,3,-6,-7,2,-7,10,-4,-1,2,-8,-5,-10,10,-6,-1,1,-4,-6,7,-2,10,10,-6,6,-2,-3,-3,-6,2,-4,-4,6,-3,10,10,-8,-3,4,-9,7,7,6,1,-5,-8,8,7,2,4,-3,4,-5,-10,-8,1,8,-5,8,-10,3,-5,10,2,-3,3,-1,7,-8,4,6,5,-3,-10,-8,-3,8,1,9,9,-2,-8,-3,-8,4,1,7,-3,6,-1,-6,7,-4,2,-4,5,-7,-8,10,1,9,-3,8,9,1,-8,6,-1,-6,4,-5,-5,-4,3,10,-9,8,7,9,-7,6,7,1,-2,2,6,-5,-10,-5,-6,-8,3,-8,-1,-6,5,-4,-6,10,-3,-4,-10,1,9,-4,10,-9,-8,-5,3,-7,-7,-1,-9,1,-3,-2,-3,4,10,4,-10,7,1,6,5,-10,-6,5,4,-7,10,-2,4,-2,2,6,-10,-9,-5,5,-10,-4,8,2,-5,8,8,-6,-6,7,-8,-1,8,-1,6,-4,-1,-5,-6,-10,5,6,-10,8,-3,-3,9,-1,-3,-9,6,-7,10,3,-8,8,-3,-9,-9,8,-1,4,4,-9,6,7,-1,-7,8,-10,-5,2,-3,10,7,5,-8,9,2,10,-8,-8,-5,2,8,-2,10,-10,6,-4,-9,-2,-6,8,1,-6,9,7,-10,9,-1,-1,-6,4,3,6,7,-9,-1,2,7,2,-3,-9,-10,-3,9,1,-4,-7,5,9,3,6,4,-7,-10,-8,2,6,-8,-4,-2,2,2,-5,5,10,1,-2,-5,-6,10,8,3,-5,-4,8,3,-5,1,3,-3,4,10,9,-6,10,10,9,5,-2,10,6,10,-2,9,-9,-8,-8,-10,6,3,4,-6,-7,-7,-10,1,-4,-7,-3,2,1,-6,10,8,-4,2,6,-2,-10,4,-8,6,-5,8,1,10,10,3,-4,6,3,5,-7,-4,8,7,-4,-7,5,-9,-5,-8,-6,7,-3,-7,10,-8,1,-3,2,6,-2,7,10,4,8,10,-5,4,-7,-6,5,5,-8,8,8,-7,6,-8,3,-2,5,5,-9,10,1,5,10,5,-10,-9,6,-9,-4,-1,-10,-8,-4,-5,-1,1,10,2,-9,9,2,8,-8,10,-5,-8,5,7,8,-4,-6,-5,-2,8,5,-1,-7,-5,-9,8,-8,-8,-2,-2,-9,-9,3,3,10,7,9,2,-10,-3,-2,2,7,2,-4,-10,-1,10,-5,-9,4,-2,-7,-1,1,-5,-6,2,-6,-5,-9,5,-7,5,-10,7,-10,7,3,-6,3,-7,8,-2,-6,-7,3,-6,-9,-10,-5,10,-8,-5,-4,-7,-2,-6,8,5,5,8,3,6,-6,8,-5,-7,5,6,-2,-8,9,-3,2,-10,9,4,-3,2,9,1,8,9,-9,-7,-9,-3,1,-5,5,1,-5,-6,7,10,-7,2,-8,-3,7,7,-6,-4,8,3,9,9,-1,4,2,4,4,7,6,-8,9,-8,-8,4,-6,-3,-1,8,-5,9,-6,-7,10,2,-5,10,-8,8,5,-3,-9,7,-9,1,7,1,3,-4,3,1,-6,1,1,1,-3,8,-1,9,10,-3,-10,-8,6,7,8,9,-3,10,-2,-2,5,5,5,-7,-6,1,9,-10,-3,-4,7,5,-4,5,-7,-10,-7,10,9,-8,-10,-10,8,1,8,-2,-1,-6,3,-2,8,-3,-5,8,10,2,3,-8,3,-2,-7,6,3,-2,3,7,5,6,-4,-5,-10,-6,-8,-6,4,-2,4,8,3,-4,-3,10,4,8,-10,-2,-2,5,-3,-3,-9,-9,-4,-8,6,-3,-4,8,9,-6,1,-1,-8,-4,-7,1,1,-7,-6,2,-9,-2,-8,-3,-8,-5,-8,-3,5,1,-4,8,-10,-8,1,10,-5,-7,3,-9,8,2,-2,-6,4,-1,-8,2,3,6,-2,-8,-9,9,4,4,3,9,3,-4,-3,-5,-3,10,-7,-4,3,7,4,5,-5,1,7,5,5,8,6,8,-8,-7,-7,5,10,1,7,3,6,-10,-6,-4,-6,-9,-6,10,-7,1,8,3,8,-6,-1,9,-5,-10,-5,1,9,-2,9,8,-10,2,-7,-8,9,3,2,-7,2,7,-4,-9,-8,-7,-6,5,-6,-6,1,1,9,-2,-6,8,-8,5,3,4,-8,8,-6,2,7,-8,-1,10,10,2,1,-4,-5,3,-7,-9,8,9,-8,9,-8,-6,3,-10,8,-1,-2,-7,7,6,7,-9,1,-2,-10,8,5,6,10,4,-5,-4,-1,-5,3,4,-7,6,2,8,-8,-9,-10,2,10,5,-1,4,4,-2,-1,6,1,5,-3,-7,-1,3,-1,1,-8,-9,-9,-3,-4,-7,-3,-2,-8,-10,-2,-9,5,-6,6,-10,-8,-7,3,8,-5,2,-10,4,1,-9,3,8,2,6,3,-6,8,8,3,1,-10,8,7,-8,-6,-3,-8,8,-7,10,4,-3,-1,-4,-4,2,7,-4,10,3,10,6,7,8,10,-5,5,-5,-8,1,-5,6,1,-8,-3,-8,7,10,7,9,7,-10,-2,9,5,2,2,-1,7,5,-10,-2,6,4,-2,-1,-9,-3,5,10,3,1,1,8,1,9,-6,-2,-5,-6,-1,7,-7,10,-4,3,4,3,-5,-5,-4,-2,5,3,-2,8,5,1,6,5,4,7,1,5,-1,-6,5,5,2,10,4,-7,-3,-2,-2,1,2,-5,-8,-1,-3,3,-5,-5,-4,-2,5,9,10,1,6,-9,9,-5,6,-5,-5,4,5,-8,8,-9,-9,-3,10,10,-5,8,3,-1,1,8,4,-5,-5,10,-3,6,-9,-1,-2,-9,-8,-1,2,1,-9,9,-3,4,7,1,5,2,-6,-3,1,-5,8,-1,-9,-4,-3,4,9,-6,-4,-6,6,-2,-10,1,8,-2,4,-9,-8,-3,-7,-9,-7,-5,-3,1,-9,-2,-2,10,-10,6,-6,9,9,-4,-3,7,9,-2,-2,-2,9,-2,8,9,-4,2,-4,-3,6,-1,10,8,9,4,4,4,9,-4,-10,4,10,4,-10,-6,6,-5,7,-8,3,10,7,3,-2,6,10,5,-8,5,-8,4,10,4,3,8,5,5,3,-1,-5,-6,7,-6,-10,2,-1,6,6,-3,-4,-4,10,-3,7,8,1,8,7,4,2,7,-4,7,5,-10,-10,1,6,-2,10,-7,-6,-10,9,-10,1,6,-4,-7,2,9,-2,1,6,2,-5,-6,6,-6,3,-5,7,10,-4,-2,2,8,4,3,5,4,8,5,-10,-8,8,5,-5,-7,-2,5,10,2,-3,2,2,-7,7,-2,-2,-10,-6,-6,-2,9,-9,9,-6,-3,-6,6,-10,8,-7,-8,5,-9,-7,-9,7,-4,-2,6,-4,8,4,9,9,5,2,-4,1,5,8,6,5,2,5,-7,8,10,-3,10,-10,9,8,8,-7,-9,10,2,7,3,5,10,9,-9,-1,-6,4,5,-9,3,-10,2,-10,-5,2,1,-2,-3,3,5,1,-6,-5,6,6,9,-4,5,-9,10,-2,1,2,-7,5,10,1,10,-7,-9,6,8,-1,3,-7,3,6,5,7,-6,2,-10,-1,1,7,-2,8,-4,-7,10,3,-3,-5,-10,10,7,-9,-7,7,10,-7,-8,6,-5,10,7,9,4,-10,-8,-8,2,-4,-10,4,5,-6,-6,5,-7,9,10,-6,1,7,-6,-8,6,7,1,10,5,-8,-8,4,-10,9,-10,2,-3,-3,-8,7,-1,2,8,-9,-5,3,10,1,10,-9,5,2,-2,6,5,4,10,9,7,8,-5,-7,10,-6,-8,-3,-8,-2,1,2,3,-4,-1,8,1,10,-9,-2,5,-1,4,-7,-10,-3,-6,5,-1,2,-1,2,8,-9,-10,-10,-8,-9,7,-3,6,-6,-2,-4,1,7,-8,-6,-10,5,-4,9,8,-4,-6,9,-6,-4,7,9,4,10,4,10,8,8,-10,6,4,2,9,-2,6,3,-6,1,-8,-3,6,-8,9,-8,2,-9,-6,-6,2,-1,-4,4,-7,-1,6,9,7,8,-3,7,2,2,6,-4,6,9,-8,-1,7,-9,-5,-9,-8,-8,-3,8,8,-3,8,3,1,-7,6,-5,9,8,-4,6,-3,-3,-7,2,-1,-2,-2,-6,-8,5,8,-8,4,10,-2,10,-1,4,3,3,-2,-4,1,-9,-10,4,-4,6,-8,-8,5,8,2,-1,-9,-1,-3,-5,-5,-5,1,-7,-10,5,-1,10,10,9,-9,6,-9,9,2,-6,10,-5,9,-6,-5,6,-3,-10,-4,6,1,1,1,-2,6,1,7,7,-8,-4,-5,8,9,-4,7,6,3,8,9,-6,-7,-1,5,-8,-4,-7,-7,8,3,8,-1,9,-4,-8,8,8,-3,8,6,10,-2,-8,9,2,-9,3,-5,-5,-9,1,-7,1,-7,-5,-6,-2,3,7,7,6,-10,-7,-9,-5,3,6,-5,9,7,-5,-10,-3,-7,5,-10,2,-9,-8,-9,-7,-8,-2,1,5,7,2,4,-2,-6,9,-9,-7,-9,-7,7,-1,-10,-8,-6,8,10,3,-7,-7,4,-10,-6,-1,1,3,3,-3,-9,-3,-3,-10,-3,8,-10,3,-2,6,10,-3,5,-1,10,-3,-6,-5,9,3,-10,2,-4,3,7,-4,-7,10,-4,4,8,4,4,-4,-7,-5,-5,-9,9,7,-1,5,-9,-2,5,-7,-3,-6,8,-10,-6,-2,-9,10,-2,5,9,5,-2,-8,-3,1,-4,3,-8,9,-7,5,-3,-3,3,2,8,7,-4,-1,10,5,1,-9,2,-5,2,-4,-6,-2,6,8,-1,8,-1,-4,-10,-8,8,4,-9,10,8,6,2,-2,4,-6,8,-10,-10,-2,5,3,-9,-3,5,-10,7,8,6,10,3,-6,-10,10,3,2,9,-9,-2,7,-8,-4,-2,4,4,9,2,8,2,-1,9,-2,7,-9,6,10,-2,6,-7,-4,-6,10,-8,9,-8,4,-2,-6,-8,9,10,7,-4,-5,-5,3,2,1,-4,10,9,-9,-2,1,7,-5,1,-8,5,5,-4,3,-4,8,5,9,-5,6,-3,-7,-8,9,2,-6,3,-9,2,5,-8,-3,2,-8,10,4,2,-6,-4,2,2,-5,1,-4,-5,8,-3,-6,-5,-3,8,-10,9,-1,-1,-8,-2,10,4,8,-6,-5,-9,5,5,1,-3,4,-5,4,-1,-8,3,8,-5,-9,5,7,6,10,-10,-7,-9,7,-7,9,1,-10,-9,-4,-5,3,-8,5,-4,7,5,-7,2,-10,4,4,-9,10,3,2,6,9,6,7,-1,2,-8,-2,-4,9,4,-3,-10,-2,-4,10,-8,5,-2,-3,-9,-1,-5,-5,-7,-7,10,5,1,-4,2,7,2,3,6,-9,1,10,-2,5,1,-10,9,4,3,-7,1,-4,-7,1,2,-6,1,-1,3,4,-9,7,-2,-10,-7,9,-4,-3,1,-4,-3,10,-8,-6,-10,-5,7,-8,2,-3,6,9,6,-1,-7,1,-5,5,-3,-4,-3,1,10,-6,-7,5,2,5,7,6,3,5,10,1,1,6,4,-4,7,1,9,-1,-10,-9,-4,-3,4,-7,8,-8,5,2,3,6,-6,-6,-10,7,5,7,3,-6,-7,-1,-1,3,7,7,-1,-10,9,5,-4,1,10,-9,-7,-2,-10,-9,-6,-8,8,-2,8,8,-9,7,7,3,6,-2,8,9,-1,-10,-9,-9,-4,5,-3,9,8,-5,4,2,-1,4,2,-9,2,-7,8,9,7,3,-9,-1,-10,3,6,5,2,7,7,-7,5,-1,2,-6,7,8,-2,4,7,8,-5,-1,4,-2,-3,-9,3,-3,3,-1,-9,-6,-9,-4,8,-10,-5,-9,-8,-2,-10,-1,-3,5,4,-6,-8,-5,-5,-3,-1,7,5,-6,6,6,-9,8,-3,-9,2,9,10,-7,3,7,5,7,-1,-3,-1,5,-7,-1,8,5,-5,-10,-8,-9,10,-2,-1,7,6,-9,10,-4,-6,5,-6,6,7,-6,4,8,1,-9,3,-4,-5,-3,-6,-1,-5,-8,1,10,-1,-4,2,-9,2,-7,3,3,6,-6,-4,-7,-5,7,1,3,6,7,9,-2,3,7,5,-7,-5,-3,9,-5,-7,10,2,9,3,7,-1,5,2,-3,2,-6,-4,4,-1,8,3,-7,3,4,-2,-10,-2,9,4,9,-2,3,-5,9,-7,-5,7,7,10,10,2,4,-2,8,-3,-4,-3,2,3,6,-8,-10,5,-9,-9,-6,6,9,-1,5,-3,2,5,3,-3,8,2,-10,-5,1,-7,-9,4,-2,4,-10,8,4,-4,-9,-8,2,-5,4,-1,-6,-1,-5,4,2,7,-4,6,6,4,8,-4,-1,-5,9,-1,6,1,-9,-9,2,4,10,-5,-9,4,3,10], dtype = "uint32")#candidate|8894|(2520,)|const|uint32
call_8893 = relay.TupleGetItem(func_8759_call(relay.reshape(const_8894.astype('uint32'), [630, 4])), 1)
call_8895 = relay.TupleGetItem(func_8761_call(relay.reshape(const_8894.astype('uint32'), [630, 4])), 1)
output = relay.Tuple([call_8850,call_8893,const_8894,])
output2 = relay.Tuple([call_8851,call_8895,const_8894,])
func_8911 = relay.Function([], output)
mod['func_8911'] = func_8911
mod = relay.transform.InferType()(mod)
output = func_8911()
func_8912 = relay.Function([], output)
mutated_mod['func_8912'] = func_8912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8467_call = mod.get_global_var('func_8467')
func_8469_call = mutated_mod.get_global_var('func_8469')
call_8938 = relay.TupleGetItem(func_8467_call(), 0)
call_8939 = relay.TupleGetItem(func_8469_call(), 0)
output = call_8938
output2 = call_8939
func_8940 = relay.Function([], output)
mod['func_8940'] = func_8940
mod = relay.transform.InferType()(mod)
mutated_mod['func_8940'] = func_8940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8940_call = mutated_mod.get_global_var('func_8940')
call_8941 = func_8940_call()
output = call_8941
func_8942 = relay.Function([], output)
mutated_mod['func_8942'] = func_8942
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8967 = relay.var("var_8967", dtype = "float64", shape = (4, 12, 6))#candidate|8967|(4, 12, 6)|var|float64
uop_8968 = relay.asinh(var_8967.astype('float64')) # shape=(4, 12, 6)
output = uop_8968
output2 = uop_8968
func_8971 = relay.Function([var_8967,], output)
mod['func_8971'] = func_8971
mod = relay.transform.InferType()(mod)
var_8972 = relay.var("var_8972", dtype = "float64", shape = (4, 12, 6))#candidate|8972|(4, 12, 6)|var|float64
output = func_8971(var_8972)
func_8973 = relay.Function([var_8972], output)
mutated_mod['func_8973'] = func_8973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7111_call = mod.get_global_var('func_7111')
func_7112_call = mutated_mod.get_global_var('func_7112')
call_8994 = relay.TupleGetItem(func_7111_call(), 0)
call_8995 = relay.TupleGetItem(func_7112_call(), 0)
output = relay.Tuple([call_8994,])
output2 = relay.Tuple([call_8995,])
func_8996 = relay.Function([], output)
mod['func_8996'] = func_8996
mod = relay.transform.InferType()(mod)
output = func_8996()
func_8997 = relay.Function([], output)
mutated_mod['func_8997'] = func_8997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6010_call = mutated_mod.get_global_var('func_6010')
call_9024 = func_6009_call()
call_9025 = func_6009_call()
output = call_9024
output2 = call_9025
func_9026 = relay.Function([], output)
mod['func_9026'] = func_9026
mod = relay.transform.InferType()(mod)
mutated_mod['func_9026'] = func_9026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9026_call = mutated_mod.get_global_var('func_9026')
call_9027 = func_9026_call()
output = call_9027
func_9028 = relay.Function([], output)
mutated_mod['func_9028'] = func_9028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7562_call = mod.get_global_var('func_7562')
func_7564_call = mutated_mod.get_global_var('func_7564')
call_9046 = relay.TupleGetItem(func_7562_call(), 0)
call_9047 = relay.TupleGetItem(func_7564_call(), 0)
func_8314_call = mod.get_global_var('func_8314')
func_8316_call = mutated_mod.get_global_var('func_8316')
var_9074 = relay.var("var_9074", dtype = "uint16", shape = (38400,))#candidate|9074|(38400,)|var|uint16
call_9073 = relay.TupleGetItem(func_8314_call(relay.reshape(var_9074.astype('uint16'), [38400,])), 1)
call_9075 = relay.TupleGetItem(func_8316_call(relay.reshape(var_9074.astype('uint16'), [38400,])), 1)
uop_9113 = relay.acos(var_9074.astype('float64')) # shape=(38400,)
output = relay.Tuple([call_9046,call_9073,uop_9113,])
output2 = relay.Tuple([call_9047,call_9075,uop_9113,])
func_9119 = relay.Function([var_9074,], output)
mod['func_9119'] = func_9119
mod = relay.transform.InferType()(mod)
var_9120 = relay.var("var_9120", dtype = "uint16", shape = (38400,))#candidate|9120|(38400,)|var|uint16
output = func_9119(var_9120)
func_9121 = relay.Function([var_9120], output)
mutated_mod['func_9121'] = func_9121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4340_call = mod.get_global_var('func_4340')
func_4341_call = mutated_mod.get_global_var('func_4341')
call_9142 = func_4340_call()
call_9143 = func_4340_call()
output = call_9142
output2 = call_9143
func_9148 = relay.Function([], output)
mod['func_9148'] = func_9148
mod = relay.transform.InferType()(mod)
mutated_mod['func_9148'] = func_9148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9148_call = mutated_mod.get_global_var('func_9148')
call_9149 = func_9148_call()
output = call_9149
func_9150 = relay.Function([], output)
mutated_mod['func_9150'] = func_9150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3456_call = mod.get_global_var('func_3456')
func_3457_call = mutated_mod.get_global_var('func_3457')
call_9163 = relay.TupleGetItem(func_3456_call(), 0)
call_9164 = relay.TupleGetItem(func_3457_call(), 0)
output = relay.Tuple([call_9163,])
output2 = relay.Tuple([call_9164,])
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
func_7562_call = mod.get_global_var('func_7562')
func_7564_call = mutated_mod.get_global_var('func_7564')
call_9258 = relay.TupleGetItem(func_7562_call(), 1)
call_9259 = relay.TupleGetItem(func_7564_call(), 1)
func_8356_call = mod.get_global_var('func_8356')
func_8358_call = mutated_mod.get_global_var('func_8358')
var_9269 = relay.var("var_9269", dtype = "float64", shape = (9, 260))#candidate|9269|(9, 260)|var|float64
call_9268 = relay.TupleGetItem(func_8356_call(relay.reshape(var_9269.astype('float64'), [12, 13, 15])), 0)
call_9270 = relay.TupleGetItem(func_8358_call(relay.reshape(var_9269.astype('float64'), [12, 13, 15])), 0)
uop_9271 = relay.tan(call_9268.astype('float64')) # shape=(12, 13, 15)
uop_9273 = relay.tan(call_9270.astype('float64')) # shape=(12, 13, 15)
func_4821_call = mod.get_global_var('func_4821')
func_4825_call = mutated_mod.get_global_var('func_4825')
const_9277 = relay.const([[3.505322,1.416156],[7.795423,6.855071],[-3.570663,8.819553],[7.935955,-1.629389],[4.405299,-9.016976],[-1.827308,-1.521386],[-2.896257,6.539363],[-8.616475,-1.526415],[-6.107306,4.382181],[0.671369,8.152815],[7.079404,9.411314],[-5.746366,0.264565],[-9.027344,-3.087458],[4.397898,-5.376371],[2.355649,-9.481762],[5.028492,7.722966],[0.695356,-2.953377],[4.587860,-2.526526],[-9.755598,8.082615],[-2.163096,-8.430692],[2.726940,6.424413],[-1.431113,-8.789433],[4.249969,4.116986],[-1.491809,1.123877],[-1.788767,-1.294568],[8.281797,-0.786945],[-8.710807,-5.727864]], dtype = "float32")#candidate|9277|(27, 2)|const|float32
var_9278 = relay.var("var_9278", dtype = "bool", shape = (273, 3))#candidate|9278|(273, 3)|var|bool
var_9279 = relay.var("var_9279", dtype = "uint16", shape = (2560,))#candidate|9279|(2560,)|var|uint16
call_9276 = relay.TupleGetItem(func_4821_call(relay.reshape(const_9277.astype('float32'), [3, 9, 2]), relay.reshape(var_9278.astype('bool'), [819, 1]), relay.reshape(var_9279.astype('uint16'), [2560,]), ), 6)
call_9280 = relay.TupleGetItem(func_4825_call(relay.reshape(const_9277.astype('float32'), [3, 9, 2]), relay.reshape(var_9278.astype('bool'), [819, 1]), relay.reshape(var_9279.astype('uint16'), [2560,]), ), 6)
var_9292 = relay.var("var_9292", dtype = "float64", shape = (12, 13, 15))#candidate|9292|(12, 13, 15)|var|float64
bop_9293 = relay.less(uop_9271.astype('bool'), relay.reshape(var_9292.astype('bool'), relay.shape_of(uop_9271))) # shape=(12, 13, 15)
bop_9296 = relay.less(uop_9273.astype('bool'), relay.reshape(var_9292.astype('bool'), relay.shape_of(uop_9273))) # shape=(12, 13, 15)
output = relay.Tuple([call_9258,var_9269,call_9276,const_9277,var_9278,var_9279,bop_9293,])
output2 = relay.Tuple([call_9259,var_9269,call_9280,const_9277,var_9278,var_9279,bop_9296,])
func_9299 = relay.Function([var_9269,var_9278,var_9279,var_9292,], output)
mod['func_9299'] = func_9299
mod = relay.transform.InferType()(mod)
var_9300 = relay.var("var_9300", dtype = "float64", shape = (9, 260))#candidate|9300|(9, 260)|var|float64
var_9301 = relay.var("var_9301", dtype = "bool", shape = (273, 3))#candidate|9301|(273, 3)|var|bool
var_9302 = relay.var("var_9302", dtype = "uint16", shape = (2560,))#candidate|9302|(2560,)|var|uint16
var_9303 = relay.var("var_9303", dtype = "float64", shape = (12, 13, 15))#candidate|9303|(12, 13, 15)|var|float64
output = func_9299(var_9300,var_9301,var_9302,var_9303,)
func_9304 = relay.Function([var_9300,var_9301,var_9302,var_9303,], output)
mutated_mod['func_9304'] = func_9304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7216_call = mod.get_global_var('func_7216')
func_7217_call = mutated_mod.get_global_var('func_7217')
call_9337 = func_7216_call()
call_9338 = func_7216_call()
func_8205_call = mod.get_global_var('func_8205')
func_8208_call = mutated_mod.get_global_var('func_8208')
var_9345 = relay.var("var_9345", dtype = "float32", shape = ())#candidate|9345|()|var|float32
var_9346 = relay.var("var_9346", dtype = "uint16", shape = (54,))#candidate|9346|(54,)|var|uint16
call_9344 = relay.TupleGetItem(func_8205_call(relay.reshape(var_9345.astype('float32'), []), relay.reshape(var_9346.astype('uint16'), [54,]), ), 3)
call_9347 = relay.TupleGetItem(func_8208_call(relay.reshape(var_9345.astype('float32'), []), relay.reshape(var_9346.astype('uint16'), [54,]), ), 3)
func_5204_call = mod.get_global_var('func_5204')
func_5209_call = mutated_mod.get_global_var('func_5209')
const_9352 = relay.const([2,8,10,-6,-2,1,3,-3,-2,4,-1,7,3,8,-3,-8,2,2,2,3,7,9,7,2,-7,5,9,3,-1,7,-5,10,-1,-1,2,-6,-5,-1,-6,-4,-9,-10,-10,-10,7,-6,4,-10,-10,-7,-3,3,9,2,7,2,-4,4,-9,-8,4,7,-2,5,5,6,7,8,3,5,6,6,2,-6,6,5,8,10,-8,1,6,-3,-7,3,1,-2,5,-8,7,6,-6,5,-5,-1,9,8,9,2,-4,-10,1,3,9,5,-3,-1,-3,2,-3,-3,-7,10,2,-6,5,3,-7,5,10,-1,-10,2,1,3,9,6,7,-1,-10,-7,-2,-4,-9,-4,9,-1,-10,-4,1,4,-3,5,10,9,5,-6,8,-6,9,5,-3,-6,-3,3,8,-1,10,3,4,-10,7,5,-6,-4,9,10,8,-7,8,3,9,-9,2,9,-3,4,-4,7,10,-2,1,-2,-2,9,1,6,-8,9,8,-7,-8,2,1,-10,9,9,8,8,-2,-7,-1,-5,1,-10,-3,-1,9,10,3,1,6,3,-3,1,7,8,-5,6,6,-7,4,-9,9,3,3,-3,3,-10,-6,2,3,1,3,-5,5,8,-8,-2,-8,9,6,10,-8,6,3,9,-7,3,-10,-1,-10,4,-7,5,9,7,-7,-7,-7,-1,2,-6,10,1,10,5,-10,-8,-5,-2,-8,-2,-6,-4,-1,-3,4,-1,3,-6,-3,-2,10,-8,6,1,-9,-1,-9,7,-9,-4,10,-9,9,-5,-6,3,-1,-3,3,3,5,6,-10,-6,3,-3,-5,-5,6,7,1,10,-5,8,-8,-9,-6,9,-7,-4,4,3,-10,6,-10,-9,-2,-2,-3,4,-1,6,-9,-3,9,7,5,-5,-10,-10,-1,-1,10,-2,4,-6,-1,2,7,-8,-5,10,-7,-6,5,9,-6,10,2,9,-10,-10,-7,-4,-10,-9,-9,6,5,5,9,-5,-2,1,9,-1,6,1,-8,6,-7,-4,5,2,-3,9,1,-6,-8,-9,8,-5,3,-8,3,10,10,-8,-3,6,-7,5,8,1,10,-3,1,-5,-8,-7,8,2,-9,-4,1,8,6,8,-7,-9,10,-7,2,7,-6,10,2,-3,-2,-5,8,3,-7,7,-9,-2,8,9,-3,7,-1,-5,-9,-7,-7,4,-6,-1,-7,6,5,-6,-7,-1,1,2,-5,8,7,-4,6,4,-6,-4,3,8,7,-1,1,5,-1,6,5,-1,9,-1,-5,8,9,-2,-3,-2,-6,-5,6,9,-8,-5,-10,9,2,-6,-2,6,-6,8,3,-10,-5,-8,-6,8,3,-10,10,4,-7,8,-5,-5,-5,2,2,-6,8,8,10,-9,1,-8,9,2,-10,-7,5,8,4,-5,-2,3,-5,-4,-9,10,2,-1,-7,9,3,4,10,5,2,2,3,3,-8,-2,10,9,7,-5,4,4,9,-7,-2,5,-4,-9,4,-4,-1,-1,8,4,-3,2,2,9,5,-4,-8,-10,-8,1,1,6,4,2,9,-9,-7,-2,-8,4,-6,-10,-7,-9,9,7,-7,-3,-10,5,3,4,5,-10,-6,8,-1,6,-1,3,9,2,-2,-7,2,-4,5,4,5,-5,-8,-4,-1,9,9,2,1,-4,-8,7,-4,-4,2,-9,2,9,6,1,8,-9,-1,5,-4,-6,9,-4,-6,-1,6,5,-7,10,-2,3,2,-6,-5,-6,9,3,7,2,6,2,-7,-4,3,-8,-6,4,-2,-10,1,-6,-7,-8,-8,6,6,-8,6,7,-5,-6,-5,8,1,6,3,2,-5,-2,5,-7,-7,3,-6,-5,-7,-3,-3,2,10,-8,4,-10,-4,-9,2,9,-2,3,5,10,-10,4,5,-7,-8,7,7,-10,-10,10,-9,-1,3,9,-5,10,6,-9,2,6,-3,3,-10,2,3,4,-1,3,3,2,2,3,5,-9,-10,-8,-9,6,5,-1,-10,-10,-10,-4,4,-10,7,-8,-7,-1,3,-3,-4,2,-5,-8,6,7,-3,-10,9,7,5,-10,2,3,-5,-8,3,10,10,4,-8,-5,-4,-7,-7,2,-10,8,6,-5,-6,-1,2,-9,-9,-2,6,7,-4,-4,1,-5,-8,2,2,8,2,-9,3,9,-10,1,10,-5,-6,-5,7,-9,3,-1,-3,-5,10,-1,1,-5,3,-7,5,7,-3,8,2,-6,-1,2,-6,8,2,-9,1,3,9,7,2,-5,6,-6,3,5,-9,-9,-5,-2,-8,1,-4,-3,4,5,6,4,5,2,2,-1,4,7,-7,-10,10,4,6,7,1,-8,3,-1,-2,4,10,-8,-7,8,5,-1,-9,-9,4,5,-7,2,-4,8,-8,3,-10,-4,5,-3,10,-5,10,-4,-9,2,1,-8,9,-3,6,4,-7,5,10,2,3,-9,-3,-1,-1,10,9,6,-2,6,7,8,-10,-7,2,-4,-9,1,-7,6,-5,9,4,5,-6,-8,3,-8,8,7,3,4,-4,5,7,-9,-8,8,4,10,6,-3,-3,-6,-6,-8,4,-2,6,10,-7,-6,7,-8,9,1,5,8,6,-8,7,-1,7,9,-9,7,-8,-2,10,4,-8,-7,-10,3,-9,6,7,6,9,7,4,5,-10,-7,-8,10,-7,-1,3,2,-4,-7,6,-5,7,-2,-10,3,5,-10,2,-9,6,5,-5,-1,-5,-10,-2,-5,-8,1,7,6,5,-5,6,5,7,1,-9,2,3,-7,6,-3,1,10,8,-10,-2,10,-2,-9,-7,10,7,1,4,2,-10,-4,-8,8,2,9,-4,3,-5,4,7,7,-8,1,-6,3,7,-6,-6,3], dtype = "int16")#candidate|9352|(1080,)|const|int16
const_9353 = relay.const([-6.014729,-4.974156,-9.395583,-2.174424,-0.255229,2.386339,-6.814998,3.757368,4.904875,-1.566490,9.545143,1.013344,9.012973,-3.144442,5.187168,3.993541,-0.616406,-1.656137,-5.545074,-4.908998,-7.983544,-6.001696,-5.559743,-2.577120,8.776193,7.206926,-0.393794,1.969348,-4.813883,-2.316253,-2.145693,8.275289,7.796206,-0.658785,0.406271,-4.404940,-8.706560,-2.680040,-6.199043,5.836739,3.730448,9.722006,4.370886,-8.359170,-9.991656,-7.661473,-9.494050,5.620638,5.696895,9.118076,3.207917,7.248633,-8.418865,-4.285912,-1.568184,-1.037090,-8.009012,0.572785,7.454796,6.452625,-1.338554,-8.454810,-2.095357,-0.128839,1.083910,-2.902381,4.520208,1.667473,7.365777,0.838406,9.580735,6.764032,2.257817,5.451703,-3.804533,-1.727713,-8.677567,-6.605128,7.911992,2.943296,-2.592084,0.261930,2.254358,-0.054588,-1.046674,-9.136591,0.044270,2.871870,-8.572142,9.306572,0.510514,2.727489,1.343021,-9.554559,-0.367963,1.644052,1.702868,-7.603607,5.489115,4.872770,-3.387407,5.346798,-8.234365,-9.962553,-5.593016,9.109300,-4.656649,5.455620,-9.795995,-2.655667,8.383182,-9.634478,-8.089807,3.200884,0.570622,9.960009,-4.477716,7.178074,0.482026,9.608869,-3.671576,9.317803,5.356978,-0.887962,0.543089,-7.402167,-8.639022,1.087925,-7.951169,6.569205,-5.135543,5.270999,3.566589,3.934523,5.904965,-3.964890,6.115857,-4.703872,3.171978,0.248225,1.994549,1.028817,-5.174548,-2.564067,-1.246208,-1.110317,-8.977211,7.293050,-3.440440,-0.325043,-5.623222,4.013085,-8.069671,-0.025094,-8.374742,-4.290284,-7.410171,-9.471272,4.643114,9.810846,-5.007819,-5.268377,0.166098,-1.264397,-2.221901,4.221472,-4.276372,-0.741094,-0.174431,-9.964723,-3.069708,-5.640258,-5.196631,9.594550,4.093679,3.356971,-1.541565,-7.024592,-2.318037,-5.361596,1.399159,5.270746,-9.823731,9.947815,-4.708597,-1.885402,-4.969172,8.524121,0.324721,-5.688503,6.328949,-4.540699,7.887374,-6.911027,8.316217,-3.028254,-2.065843,-0.316805,-1.754620,-5.593620,2.646055,7.120815,2.417791,3.557715,-0.751599,-8.644941,9.932248,8.195159,9.977698,-2.376475,-0.219086,-1.510058,-3.377339,-0.697548,-3.130304,-1.795811,0.665137,9.320304,-2.971113,8.225544,8.666701,3.385611,-3.041860,0.483843,-9.598561,-5.266405,7.411479,5.872995,-1.686675,-2.263361,-8.102327,-4.560073,-2.966244,8.143793,-4.931199,7.455091,-1.661553,1.309127,-0.885255,-7.175083,-3.233860,3.151173,9.133185,-1.969440,-8.473669,-0.205681,8.766075,-0.774213,3.260216,-6.825507,-8.272004,1.133426,-4.295989,2.655448,9.171112,8.200252,2.058918,9.462556,-7.999959,-5.757361,-5.667813,0.229516,7.056074,-4.266129,7.003430,8.595790,-3.601414,-9.202205,8.875460,9.984154,-3.310782,-3.589233,-8.425829,-5.039580,3.852629,7.090783,-8.067736,3.800107,0.093744,-5.280642,6.822967,-8.254638,-7.772167,-4.986221,7.962762,-8.233810,2.838606,6.685616,9.478776,-1.005082,-8.475281,-9.016232,-3.029002,-7.658638,7.259347,1.419125,-0.071830,5.591063,-1.511083,-2.113752,9.221763,5.303723,-4.727765,-7.534053,3.529543,-2.969891,8.747349,-6.729201,1.138843,7.057157,3.688369,1.070735,-2.538302,-9.233562,-0.629065,-0.459305,5.699858,-0.083622,-5.716274,9.357558,9.390979,1.069847,2.065823,0.353265,0.373975,1.593386,3.989479,-0.557688,6.669976,-5.814273], dtype = "float32")#candidate|9353|(330,)|const|float32
call_9351 = relay.TupleGetItem(func_5204_call(relay.reshape(const_9352.astype('int16'), [12, 15, 6]), relay.reshape(const_9352.astype('int16'), [12, 15, 6]), relay.reshape(const_9353.astype('float32'), [330,]), relay.reshape(const_9352.astype('uint64'), [12, 15, 6]), ), 4)
call_9354 = relay.TupleGetItem(func_5209_call(relay.reshape(const_9352.astype('int16'), [12, 15, 6]), relay.reshape(const_9352.astype('int16'), [12, 15, 6]), relay.reshape(const_9353.astype('float32'), [330,]), relay.reshape(const_9352.astype('uint64'), [12, 15, 6]), ), 4)
func_3538_call = mod.get_global_var('func_3538')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_9366 = func_3538_call()
call_9367 = func_3538_call()
uop_9369 = relay.cosh(const_9353.astype('float64')) # shape=(330,)
output = relay.Tuple([call_9337,call_9344,var_9345,var_9346,call_9351,const_9352,call_9366,uop_9369,])
output2 = relay.Tuple([call_9338,call_9347,var_9345,var_9346,call_9354,const_9352,call_9367,uop_9369,])
F = relay.Function([var_9345,var_9346,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9345,var_9346,], output2)
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
