import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_230 = relay.const([[[-2.214277],[2.786511],[-5.168728],[-3.163044],[9.156500],[6.228424],[3.999557],[3.449926]],[[-7.736267],[2.092275],[8.551347],[-4.888666],[7.817492],[-1.107511],[-9.976579],[-7.719992]],[[-9.774158],[-6.181725],[9.288743],[-4.825802],[-7.226897],[6.899223],[5.507626],[-1.024462]]], dtype = "float32")#candidate|230|(3, 8, 1)|const|float32
uop_231 = relay.asinh(const_230.astype('float32')) # shape=(3, 8, 1)
bop_240 = relay.logical_and(uop_231.astype('bool'), relay.reshape(const_230.astype('bool'), relay.shape_of(uop_231))) # shape=(3, 8, 1)
bop_247 = relay.not_equal(const_230.astype('bool'), relay.reshape(uop_231.astype('bool'), relay.shape_of(const_230))) # shape=(3, 8, 1)
output = relay.Tuple([bop_240,bop_247,])
output2 = relay.Tuple([bop_240,bop_247,])
func_254 = relay.Function([], output)
mod['func_254'] = func_254
mod = relay.transform.InferType()(mod)
output = func_254()
func_255 = relay.Function([], output)
mutated_mod['func_255'] = func_255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_276 = relay.TupleGetItem(func_254_call(), 1)
call_277 = relay.TupleGetItem(func_255_call(), 1)
output = call_276
output2 = call_277
func_282 = relay.Function([], output)
mod['func_282'] = func_282
mod = relay.transform.InferType()(mod)
mutated_mod['func_282'] = func_282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_282_call = mutated_mod.get_global_var('func_282')
call_283 = func_282_call()
output = call_283
func_284 = relay.Function([], output)
mutated_mod['func_284'] = func_284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_282_call = mod.get_global_var('func_282')
func_284_call = mutated_mod.get_global_var('func_284')
call_306 = func_282_call()
call_307 = func_282_call()
const_311 = relay.const([[[True,True,True,False,True,True,False,True,True,False,False,True,True,True,True,False],[True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False],[False,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False],[False,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True],[False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False],[True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False],[False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True],[False,True,False,True,True,False,True,True,False,True,False,True,True,False,True,True]],[[False,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True],[False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False],[False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False],[True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,False],[True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True],[False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True],[False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True],[True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,False]],[[False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False],[True,False,True,True,True,True,False,True,True,True,True,True,False,False,True,False],[False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,True],[False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True],[True,False,False,False,False,True,False,False,True,True,False,True,True,False,False,True],[True,False,False,True,False,False,True,False,True,True,True,False,True,False,True,False],[False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False],[True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True]]], dtype = "bool")#candidate|311|(3, 8, 16)|const|bool
bop_312 = relay.minimum(call_306.astype('int64'), const_311.astype('int64')) # shape=(3, 8, 16)
bop_315 = relay.minimum(call_307.astype('int64'), const_311.astype('int64')) # shape=(3, 8, 16)
uop_318 = relay.log(bop_312.astype('float32')) # shape=(3, 8, 16)
uop_320 = relay.log(bop_315.astype('float32')) # shape=(3, 8, 16)
uop_323 = relay.exp(call_306.astype('float32')) # shape=(3, 8, 1)
uop_325 = relay.exp(call_307.astype('float32')) # shape=(3, 8, 1)
uop_336 = relay.sinh(uop_318.astype('float32')) # shape=(3, 8, 16)
uop_338 = relay.sinh(uop_320.astype('float32')) # shape=(3, 8, 16)
output = relay.Tuple([uop_323,uop_336,])
output2 = relay.Tuple([uop_325,uop_338,])
func_354 = relay.Function([], output)
mod['func_354'] = func_354
mod = relay.transform.InferType()(mod)
mutated_mod['func_354'] = func_354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_354_call = mutated_mod.get_global_var('func_354')
call_355 = func_354_call()
output = call_355
func_356 = relay.Function([], output)
mutated_mod['func_356'] = func_356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_435 = relay.TupleGetItem(func_254_call(), 1)
call_436 = relay.TupleGetItem(func_255_call(), 1)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_437 = relay.TupleGetItem(func_354_call(), 1)
call_438 = relay.TupleGetItem(func_356_call(), 1)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_469 = relay.TupleGetItem(func_354_call(), 1)
call_470 = relay.TupleGetItem(func_356_call(), 1)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_480 = relay.TupleGetItem(func_254_call(), 1)
call_481 = relay.TupleGetItem(func_255_call(), 1)
func_282_call = mod.get_global_var('func_282')
func_284_call = mutated_mod.get_global_var('func_284')
call_512 = func_282_call()
call_513 = func_282_call()
output = relay.Tuple([call_435,call_437,call_469,call_480,call_512,])
output2 = relay.Tuple([call_436,call_438,call_470,call_481,call_513,])
func_515 = relay.Function([], output)
mod['func_515'] = func_515
mod = relay.transform.InferType()(mod)
output = func_515()
func_516 = relay.Function([], output)
mutated_mod['func_516'] = func_516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_586 = relay.TupleGetItem(func_354_call(), 0)
call_587 = relay.TupleGetItem(func_356_call(), 0)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_589 = relay.TupleGetItem(func_254_call(), 1)
call_590 = relay.TupleGetItem(func_255_call(), 1)
bop_592 = relay.equal(call_586.astype('bool'), relay.reshape(call_589.astype('bool'), relay.shape_of(call_586))) # shape=(3, 8, 1)
bop_595 = relay.equal(call_587.astype('bool'), relay.reshape(call_590.astype('bool'), relay.shape_of(call_587))) # shape=(3, 8, 1)
func_282_call = mod.get_global_var('func_282')
func_284_call = mutated_mod.get_global_var('func_284')
call_603 = func_282_call()
call_604 = func_282_call()
bop_605 = relay.divide(call_586.astype('float64'), relay.reshape(call_589.astype('float64'), relay.shape_of(call_586))) # shape=(3, 8, 1)
bop_608 = relay.divide(call_587.astype('float64'), relay.reshape(call_590.astype('float64'), relay.shape_of(call_587))) # shape=(3, 8, 1)
output = relay.Tuple([bop_592,call_603,bop_605,])
output2 = relay.Tuple([bop_595,call_604,bop_608,])
func_609 = relay.Function([], output)
mod['func_609'] = func_609
mod = relay.transform.InferType()(mod)
mutated_mod['func_609'] = func_609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mutated_mod.get_global_var('func_609')
call_610 = func_609_call()
output = call_610
func_611 = relay.Function([], output)
mutated_mod['func_611'] = func_611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_282_call = mod.get_global_var('func_282')
func_284_call = mutated_mod.get_global_var('func_284')
call_615 = func_282_call()
call_616 = func_282_call()
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_623 = relay.TupleGetItem(func_515_call(), 1)
call_624 = relay.TupleGetItem(func_516_call(), 1)
output = relay.Tuple([call_615,call_623,])
output2 = relay.Tuple([call_616,call_624,])
func_627 = relay.Function([], output)
mod['func_627'] = func_627
mod = relay.transform.InferType()(mod)
mutated_mod['func_627'] = func_627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_627_call = mutated_mod.get_global_var('func_627')
call_628 = func_627_call()
output = call_628
func_629 = relay.Function([], output)
mutated_mod['func_629'] = func_629
mutated_mod = relay.transform.InferType()(mutated_mod)
var_743 = relay.var("var_743", dtype = "float32", shape = (3, 10, 1))#candidate|743|(3, 10, 1)|var|float32
const_744 = relay.const([[[-2.110122,-8.910264,7.252671,5.958385,3.406511,-6.966010,0.068926,-2.146223,-0.825420,7.123622,9.470057,-6.229914],[-6.349307,-4.821763,4.465960,-7.793947,-8.557266,9.530326,6.070292,-5.424472,-2.290670,6.706045,6.028904,7.414068],[-6.595093,2.902546,3.265796,3.417141,9.688000,-7.126738,8.783270,0.417291,3.426783,2.400855,6.177896,8.329637],[-9.113533,0.505565,-0.558520,8.886571,-8.682980,-3.717396,5.908987,3.462612,-4.857278,1.334032,-7.695003,1.607524],[-5.434150,8.708628,-7.146927,2.402997,6.439145,-6.939866,0.307277,5.572344,8.725270,5.245450,3.425710,2.821590],[-7.542421,6.670321,1.212350,-3.630414,1.978209,-1.365887,-1.503707,0.167743,-5.318588,-5.829826,5.031775,7.780568],[1.961685,7.352211,4.213419,-6.210685,-3.357134,6.385475,9.842732,1.408464,8.204904,-4.937106,6.119284,6.888699],[-8.995856,8.246547,9.981031,-3.197435,-6.886032,0.041742,-4.413006,9.838985,3.996889,7.088127,3.002374,-0.232626],[-4.815462,-0.394820,-2.727956,5.715568,1.791063,-0.210549,-8.526368,-5.134310,5.277527,-9.042000,9.355999,-3.348028],[-7.077576,0.918776,-5.455002,-0.739322,3.182558,-6.657580,5.356872,-6.154058,-1.827211,4.741799,6.182975,6.849054]],[[-2.495805,-2.250792,-2.146206,-1.455784,-4.485456,-6.653004,0.387643,4.185688,7.479964,-7.902818,-6.927343,-4.695546],[-0.292573,3.111597,0.284312,-4.364455,-0.221476,5.847897,2.762464,-0.161463,-2.988826,-5.610585,3.819968,-5.382232],[4.600568,2.271209,4.657037,-0.354614,-4.272452,0.266761,0.509653,1.310911,-8.152933,-8.939972,-6.940124,-9.264704],[6.981929,8.231122,-1.515726,3.920221,-1.950733,9.669105,-8.037071,8.919866,2.579075,-1.230496,-1.391009,1.748377],[6.280678,-8.910774,-1.714967,-3.741625,4.394203,-4.198752,8.568653,3.874594,8.067104,3.350689,4.941908,-3.276491],[1.453539,4.941318,-3.436321,-9.328389,-3.354465,5.543508,5.364247,-1.849844,0.859184,3.076306,-6.295419,3.763890],[2.925476,-7.788152,5.460517,-7.247229,9.798976,1.361408,-8.352667,0.205701,-4.137603,1.097818,-4.791760,1.967251],[-1.912443,-8.264067,2.270916,-6.443418,-5.853092,9.251671,4.386136,-2.414701,6.331319,-9.433800,-4.744671,-5.837984],[2.982014,-8.302374,7.648395,9.249397,-5.677536,0.916007,9.771230,2.964941,-9.271894,-2.534219,-5.863853,-0.024145],[-1.022336,6.627041,8.156708,4.241154,5.795699,-1.929182,6.987023,-6.592090,-6.892093,-9.948457,-0.702469,5.094909]],[[-5.971299,-0.634057,1.055940,3.185407,-9.252512,-5.292389,-1.887291,-6.741874,1.656744,0.438121,-1.998377,1.156717],[0.401476,6.016288,3.630928,-8.615138,-1.099858,-7.650379,5.096459,5.562028,-5.157730,3.434751,6.789350,-9.790453],[0.321992,-4.485528,3.779722,-2.094488,3.125819,-8.370120,-6.086804,-6.116060,-9.910455,-1.475445,-1.707129,7.319023],[7.039915,-5.793953,-1.740945,-1.176594,-4.135338,1.725561,-5.624265,-3.749642,5.852359,-4.185285,1.814585,-8.174623],[7.958851,7.575852,-8.486685,-0.636695,-9.110337,8.938940,4.792844,-2.222323,-2.681715,5.764897,9.518148,-2.428206],[5.065297,-8.337218,2.850651,-6.581437,-5.042323,9.127868,-4.057314,-7.662585,-5.758590,4.963656,5.349383,7.493687],[1.973566,-7.532421,-5.966372,-3.229238,7.171421,-8.118162,1.651255,0.612559,-4.721361,1.686179,-0.465906,7.015925],[0.406377,-8.398717,-6.120504,-4.302230,9.361755,-3.208043,1.453877,7.139645,-0.902309,3.620496,-0.130695,8.954135],[3.817692,0.054335,-6.514383,-0.928431,7.720011,4.426388,-6.154140,1.092984,-0.454243,9.413281,-2.455533,8.849948],[-4.442230,0.159266,6.468430,-2.498779,2.852193,5.647470,-9.981142,5.426248,-9.860534,-5.499719,-9.791718,-2.651939]]], dtype = "float32")#candidate|744|(3, 10, 12)|const|float32
bop_745 = relay.multiply(var_743.astype('float32'), const_744.astype('float32')) # shape=(3, 10, 12)
uop_753 = relay.log(bop_745.astype('float32')) # shape=(3, 10, 12)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_761 = relay.TupleGetItem(func_354_call(), 1)
call_762 = relay.TupleGetItem(func_356_call(), 1)
output = relay.Tuple([uop_753,call_761,])
output2 = relay.Tuple([uop_753,call_762,])
func_766 = relay.Function([var_743,], output)
mod['func_766'] = func_766
mod = relay.transform.InferType()(mod)
mutated_mod['func_766'] = func_766
mutated_mod = relay.transform.InferType()(mutated_mod)
var_767 = relay.var("var_767", dtype = "float32", shape = (3, 10, 1))#candidate|767|(3, 10, 1)|var|float32
func_766_call = mutated_mod.get_global_var('func_766')
call_768 = func_766_call(var_767)
output = call_768
func_769 = relay.Function([var_767], output)
mutated_mod['func_769'] = func_769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_775 = relay.TupleGetItem(func_515_call(), 3)
call_776 = relay.TupleGetItem(func_516_call(), 3)
func_627_call = mod.get_global_var('func_627')
func_629_call = mutated_mod.get_global_var('func_629')
call_789 = relay.TupleGetItem(func_627_call(), 0)
call_790 = relay.TupleGetItem(func_629_call(), 0)
output = relay.Tuple([call_775,call_789,])
output2 = relay.Tuple([call_776,call_790,])
func_791 = relay.Function([], output)
mod['func_791'] = func_791
mod = relay.transform.InferType()(mod)
output = func_791()
func_792 = relay.Function([], output)
mutated_mod['func_792'] = func_792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_804 = relay.TupleGetItem(func_515_call(), 4)
call_805 = relay.TupleGetItem(func_516_call(), 4)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_808 = relay.TupleGetItem(func_354_call(), 0)
call_809 = relay.TupleGetItem(func_356_call(), 0)
output = relay.Tuple([call_804,call_808,])
output2 = relay.Tuple([call_805,call_809,])
func_820 = relay.Function([], output)
mod['func_820'] = func_820
mod = relay.transform.InferType()(mod)
output = func_820()
func_821 = relay.Function([], output)
mutated_mod['func_821'] = func_821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_894 = relay.TupleGetItem(func_515_call(), 4)
call_895 = relay.TupleGetItem(func_516_call(), 4)
var_900 = relay.var("var_900", dtype = "bool", shape = (3, 8, 6))#candidate|900|(3, 8, 6)|var|bool
bop_901 = relay.logical_or(call_894.astype('bool'), var_900.astype('bool')) # shape=(3, 8, 6)
bop_904 = relay.logical_or(call_895.astype('bool'), var_900.astype('bool')) # shape=(3, 8, 6)
output = bop_901
output2 = bop_904
func_909 = relay.Function([var_900,], output)
mod['func_909'] = func_909
mod = relay.transform.InferType()(mod)
var_910 = relay.var("var_910", dtype = "bool", shape = (3, 8, 6))#candidate|910|(3, 8, 6)|var|bool
output = func_909(var_910)
func_911 = relay.Function([var_910], output)
mutated_mod['func_911'] = func_911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_282_call = mod.get_global_var('func_282')
func_284_call = mutated_mod.get_global_var('func_284')
call_970 = func_282_call()
call_971 = func_282_call()
var_978 = relay.var("var_978", dtype = "bool", shape = (3, 8, 6))#candidate|978|(3, 8, 6)|var|bool
bop_979 = relay.subtract(call_970.astype('uint64'), var_978.astype('uint64')) # shape=(3, 8, 6)
bop_982 = relay.subtract(call_971.astype('uint64'), var_978.astype('uint64')) # shape=(3, 8, 6)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_993 = relay.TupleGetItem(func_515_call(), 3)
call_994 = relay.TupleGetItem(func_516_call(), 3)
output = relay.Tuple([bop_979,call_993,])
output2 = relay.Tuple([bop_982,call_994,])
func_1000 = relay.Function([var_978,], output)
mod['func_1000'] = func_1000
mod = relay.transform.InferType()(mod)
mutated_mod['func_1000'] = func_1000
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1001 = relay.var("var_1001", dtype = "bool", shape = (3, 8, 6))#candidate|1001|(3, 8, 6)|var|bool
func_1000_call = mutated_mod.get_global_var('func_1000')
call_1002 = func_1000_call(var_1001)
output = call_1002
func_1003 = relay.Function([var_1001], output)
mutated_mod['func_1003'] = func_1003
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1025 = relay.var("var_1025", dtype = "uint16", shape = (12, 14, 8))#candidate|1025|(12, 14, 8)|var|uint16
var_1026 = relay.var("var_1026", dtype = "uint16", shape = (12, 14, 8))#candidate|1026|(12, 14, 8)|var|uint16
bop_1027 = relay.multiply(var_1025.astype('uint16'), relay.reshape(var_1026.astype('uint16'), relay.shape_of(var_1025))) # shape=(12, 14, 8)
func_627_call = mod.get_global_var('func_627')
func_629_call = mutated_mod.get_global_var('func_629')
call_1030 = relay.TupleGetItem(func_627_call(), 1)
call_1031 = relay.TupleGetItem(func_629_call(), 1)
uop_1048 = relay.asin(var_1026.astype('float64')) # shape=(12, 14, 8)
func_820_call = mod.get_global_var('func_820')
func_821_call = mutated_mod.get_global_var('func_821')
call_1051 = relay.TupleGetItem(func_820_call(), 0)
call_1052 = relay.TupleGetItem(func_821_call(), 0)
output = relay.Tuple([bop_1027,call_1030,uop_1048,call_1051,])
output2 = relay.Tuple([bop_1027,call_1031,uop_1048,call_1052,])
func_1058 = relay.Function([var_1025,var_1026,], output)
mod['func_1058'] = func_1058
mod = relay.transform.InferType()(mod)
mutated_mod['func_1058'] = func_1058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1058_call = mutated_mod.get_global_var('func_1058')
var_1060 = relay.var("var_1060", dtype = "uint16", shape = (12, 14, 8))#candidate|1060|(12, 14, 8)|var|uint16
var_1061 = relay.var("var_1061", dtype = "uint16", shape = (12, 14, 8))#candidate|1061|(12, 14, 8)|var|uint16
call_1059 = func_1058_call(var_1060,var_1061,)
output = call_1059
func_1062 = relay.Function([var_1060,var_1061,], output)
mutated_mod['func_1062'] = func_1062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_1074 = relay.TupleGetItem(func_354_call(), 0)
call_1075 = relay.TupleGetItem(func_356_call(), 0)
uop_1091 = relay.asin(call_1074.astype('float32')) # shape=(3, 8, 1)
uop_1093 = relay.asin(call_1075.astype('float32')) # shape=(3, 8, 1)
output = uop_1091
output2 = uop_1093
func_1100 = relay.Function([], output)
mod['func_1100'] = func_1100
mod = relay.transform.InferType()(mod)
output = func_1100()
func_1101 = relay.Function([], output)
mutated_mod['func_1101'] = func_1101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_627_call = mod.get_global_var('func_627')
func_629_call = mutated_mod.get_global_var('func_629')
call_1108 = relay.TupleGetItem(func_627_call(), 1)
call_1109 = relay.TupleGetItem(func_629_call(), 1)
uop_1116 = relay.sigmoid(call_1108.astype('float64')) # shape=(3, 8, 16)
uop_1118 = relay.sigmoid(call_1109.astype('float64')) # shape=(3, 8, 16)
bop_1120 = relay.left_shift(call_1108.astype('uint16'), relay.reshape(uop_1116.astype('uint16'), relay.shape_of(call_1108))) # shape=(3, 8, 16)
bop_1123 = relay.left_shift(call_1109.astype('uint16'), relay.reshape(uop_1118.astype('uint16'), relay.shape_of(call_1109))) # shape=(3, 8, 16)
output = bop_1120
output2 = bop_1123
func_1127 = relay.Function([], output)
mod['func_1127'] = func_1127
mod = relay.transform.InferType()(mod)
output = func_1127()
func_1128 = relay.Function([], output)
mutated_mod['func_1128'] = func_1128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_820_call = mod.get_global_var('func_820')
func_821_call = mutated_mod.get_global_var('func_821')
call_1184 = relay.TupleGetItem(func_820_call(), 1)
call_1185 = relay.TupleGetItem(func_821_call(), 1)
func_627_call = mod.get_global_var('func_627')
func_629_call = mutated_mod.get_global_var('func_629')
call_1192 = relay.TupleGetItem(func_627_call(), 1)
call_1193 = relay.TupleGetItem(func_629_call(), 1)
func_1127_call = mod.get_global_var('func_1127')
func_1128_call = mutated_mod.get_global_var('func_1128')
call_1197 = func_1127_call()
call_1198 = func_1127_call()
func_820_call = mod.get_global_var('func_820')
func_821_call = mutated_mod.get_global_var('func_821')
call_1202 = relay.TupleGetItem(func_820_call(), 0)
call_1203 = relay.TupleGetItem(func_821_call(), 0)
uop_1206 = relay.cos(call_1184.astype('float64')) # shape=(3, 8, 1)
uop_1208 = relay.cos(call_1185.astype('float64')) # shape=(3, 8, 1)
func_1058_call = mod.get_global_var('func_1058')
func_1062_call = mutated_mod.get_global_var('func_1062')
const_1224 = relay.const([2,1,-4,-8,-4,-9,-5,2,-6,3,6,-8,1,-7,8,6,-5,1,-9,-6,-4,-10,10,6,-6,3,4,-8,-1,-4,8,6,9,3,-6,1,-5,-8,4,10,2,1,3,1,-2,-3,-6,-6,-8,-3,9,6,-6,1,-10,-1,2,-8,-1,1,5,8,4,-6,-2,-7,-6,8,-9,3,10,2,8,-9,1,6,3,-7,5,-9,6,-1,1,4,8,7,-3,-2,-9,2,10,-5,-10,-1,-10,4,-10,-8,-6,-1,2,-4,7,8,6,5,7,-10,4,4,6,10,4,-5,2,5,-3,1,-5,-7,8,-9,-6,2,2,4,3,-4,-3,9,6,-1,5,1,2,10,-4,5,-10,9,-4,-2,10,5,-6,1,10,-10,-4,4,-3,-6,-3,-6,-1,-5,-10,1,2,5,2,-9,-10,7,4,-1,-4,-3,-9,2,-5,-4,-5,-7,3,-4,-10,9,-5,-3,6,3,3,10,4,2,8,-4,-1,9,-5,-10,9,-4,-4,1,-2,-1,-10,-5,-3,-4,2,-4,-1,6,-8,-10,6,9,-10,9,3,-5,10,-9,-8,4,3,5,-10,9,-9,-3,10,2,-10,-1,10,-10,-7,-3,-2,-5,4,-6,-2,10,-1,-6,-5,-2,-9,2,7,4,-10,9,4,4,5,-2,-4,-8,-5,9,-3,7,-2,-5,-2,4,-6,2,8,-7,8,10,2,-1,4,-1,9,-1,8,1,-3,-9,-8,8,-9,-9,-6,10,-10,-9,1,1,7,-2,-8,-4,-9,-1,-8,-5,7,5,-4,5,10,-6,3,2,1,-6,8,-9,7,-6,-10,3,4,3,6,1,2,-6,7,7,-1,-7,5,8,8,8,-4,7,10,5,10,2,5,8,-4,-10,-10,-6,2,8,9,-2,-8,2,-1,-5,-2,2,3,-9,-7,-1,-5,1,-2,-1,-8,5,-2,-3,3,5,-5,5,6,-4,-5,9,4,1,-2,1,5,-3,3,1,6,-3,2,-8,2,-3,-6,8,4,-10,-2,-4,4,-6,-7,-5,3,-5,-6,5,-4,-6,3,-2,5,-3,10,-6,9,5,8,-1,8,8,-9,-3,-1,5,4,1,9,6,3,6,-5,8,-9,-6,4,-10,-9,8,-1,-4,-10,4,-10,7,-4,7,-3,5,-3,10,5,2,2,-3,-3,-10,5,10,-4,-1,1,-10,-3,8,-5,5,8,-5,-9,5,-9,-5,-7,-10,-6,-3,-10,-3,7,-1,8,6,5,-8,2,-8,-6,-5,-2,6,-7,4,4,-2,-7,-5,1,2,-3,-2,-2,5,-5,-3,-5,-2,-1,-2,4,-6,-7,7,-2,-5,1,-9,-10,-3,3,10,6,-10,10,2,6,-6,-8,-2,-4,-5,-4,8,-1,9,-8,3,2,-2,7,-8,-1,5,-9,-10,-6,10,1,6,-10,7,-3,-5,-4,-1,9,4,-6,-9,-8,10,6,-3,-1,-1,3,10,-6,3,9,1,-5,-10,-5,-8,10,6,9,2,-8,10,9,-7,4,-9,8,-5,-6,-4,5,-4,9,10,-7,7,-3,7,6,1,8,4,-9,-6,5,-5,-1,5,7,7,8,-9,8,3,2,5,3,5,-8,4,-3,4,-8,-6,-6,8,7,-5,5,-1,1,8,-5,5,-6,-7,-9,-4,1,1,1,1,7,4,-3,1,-1,7,4,7,2,10,4,6,2,-3,7,2,10,-7,1,7,1,-5,-8,4,8,-9,7,-8,-5,1,-6,5,9,9,2,-1,1,-7,-10,-9,6,-1,-7,2,-1,-3,8,-3,10,8,-9,6,-4,-1,5,-3,9,-3,-2,-8,8,9,9,-2,3,2,8,2,-10,-6,-2,-5,-10,9,1,-4,9,4,3,-7,-7,-8,7,-7,-2,4,-2,9,9,-6,5,1,3,-10,-3,-5,-5,5,5,-3,-7,-3,7,-4,9,-9,10,-8,7,-1,6,1,1,5,10,-4,-4,7,-10,10,-1,-6,2,5,-2,10,-4,-1,-6,4,-4,-10,-9,4,8,-1,-6,1,10,5,-4,-2,-5,7,9,5,2,-6,4,2,-3,-2,-9,4,1,-3,-4,5,-8,-1,6,4,3,10,-7,1,7,-10,-6,-8,-6,4,-6,1,3,-2,-6,-10,-6,8,5,5,3,-8,10,8,7,-5,-10,8,6,6,-8,-3,-7,6,-10,-5,6,2,1,1,-9,-10,3,-4,-10,3,7,10,8,-7,9,-1,-5,-3,2,-4,-10,-2,6,2,-8,-4,4,8,-2,-2,7,7,6,-10,-4,9,-1,-7,-9,-3,-7,-2,10,4,-7,2,10,7,1,-6,2,-1,8,-1,10,-6,10,-9,-1,2,-9,-3,-8,-9,-8,6,-2,-4,-6,9,-7,-2,-6,7,1,-5,-6,3,7,-2,7,-4,4,1,-2,-3,-7,8,-3,-9,6,9,2,-5,4,-5,-5,1,-8,-7,-3,9,-5,-3,2,7,8,10,-7,-1,10,3,-5,-5,9,3,-4,3,-9,-10,-2,9,-2,-2,-1,2,-8,-9,1,6,-5,1,-3,-9,-3,-3,7,-5,-8,9,-9,-5,6,-10,7,9,6,3,6,-2,-10,-4,-5,-5,-9,6,-5,-4,4,-10,-1,7,10,-9,-10,7,-5,9,1,5,-8,7,2,4,7,-1,4,-8,-5,-3,9,7,1,4,-1,4,-1,-3,-2,3,3,-8,9,5,6,-1,8,-8,5,10,4,5,5,-10,-5,8,4,-8,3,-9,1,-3,7,5,5,5,-1,5,-8,-5,-8,2,-1,7,2,-3,3,2,-9,-9,4,6,-4,-1,7,-5,1,7,8,3,7,4,6,-9,3,-3,-1,2,1,-10,-1,1,4,1,-1,3,4,9,3,7,3,-3,-9,4,8,6,10,-1,-7,-8,9,-8,9,3,3,-10,-7,5,-7,6,4,7,9,-10,-2,-5,-2,-4,-10,4,6,-2,-6,1,-5,-1,6,4,-7,4,-5,-10,1,9,-2,5,-7,-1,3,6,-8,8,4,9,-8,-1,-1,-1,7,-4,-5,5,5,4,-7,-7,-9,8,10,-3,2,3,-4,-8,6,-10,-10,-2,-10,-6,-1,3,-9,-1,2,-9,-9,10,7,-6,9,-4,10,7,-6,-10,-5,5,6,4,2,-4,6,-6,-1,5,-10,-2,-7,-10,-1,10,-5,-1,2,1,-1,-7,-9,9,7,2,5,6,3,6,8,2,-10,-6,-10,-8,-2,-7,8,-10,10,-10,6,-8,4,4,10,7,1,-4,-10,2,-7,-2,-5,-10,6,3,-8,10,-4,5,-2,-8,10,2,6,4,4,-8,10,-7,8,8,-8,-9,5,-10,10,10,2,10,7,-3,1,4,-1,-10,9,-6,-8,-1,1,-2,1,-1,-5,5,6,-4,1,-8,9,3,6,4,6,-9,-1,8,-2,-7,9,-10,9,-1,2,-3,9,-8,7,1,9,10,10,2,-6,-10,10,-9,-5,-1,2,-9,-2,-6,-9,2,-6,8,8,-1,-8,9,-2,-8,1,-4,-5,-3,-10,-6,5,-8,8,-8,-3,-1,9,-10], dtype = "uint16")#candidate|1224|(1344,)|const|uint16
call_1223 = relay.TupleGetItem(func_1058_call(relay.reshape(const_1224.astype('uint16'), [12, 14, 8]), relay.reshape(const_1224.astype('uint16'), [12, 14, 8]), ), 0)
call_1225 = relay.TupleGetItem(func_1062_call(relay.reshape(const_1224.astype('uint16'), [12, 14, 8]), relay.reshape(const_1224.astype('uint16'), [12, 14, 8]), ), 0)
output = relay.Tuple([call_1192,call_1197,call_1202,uop_1206,call_1223,const_1224,])
output2 = relay.Tuple([call_1193,call_1198,call_1203,uop_1208,call_1225,const_1224,])
func_1228 = relay.Function([], output)
mod['func_1228'] = func_1228
mod = relay.transform.InferType()(mod)
mutated_mod['func_1228'] = func_1228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1228_call = mutated_mod.get_global_var('func_1228')
call_1229 = func_1228_call()
output = call_1229
func_1230 = relay.Function([], output)
mutated_mod['func_1230'] = func_1230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_1239 = relay.TupleGetItem(func_354_call(), 1)
call_1240 = relay.TupleGetItem(func_356_call(), 1)
var_1245 = relay.var("var_1245", dtype = "float32", shape = (3, 8, 16))#candidate|1245|(3, 8, 16)|var|float32
bop_1246 = relay.logical_and(call_1239.astype('bool'), relay.reshape(var_1245.astype('bool'), relay.shape_of(call_1239))) # shape=(3, 8, 16)
bop_1249 = relay.logical_and(call_1240.astype('bool'), relay.reshape(var_1245.astype('bool'), relay.shape_of(call_1240))) # shape=(3, 8, 16)
output = relay.Tuple([bop_1246,])
output2 = relay.Tuple([bop_1249,])
func_1254 = relay.Function([var_1245,], output)
mod['func_1254'] = func_1254
mod = relay.transform.InferType()(mod)
mutated_mod['func_1254'] = func_1254
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1255 = relay.var("var_1255", dtype = "float32", shape = (3, 8, 16))#candidate|1255|(3, 8, 16)|var|float32
func_1254_call = mutated_mod.get_global_var('func_1254')
call_1256 = func_1254_call(var_1255)
output = call_1256
func_1257 = relay.Function([var_1255], output)
mutated_mod['func_1257'] = func_1257
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1259 = relay.const([[[4.833557,-4.032306,6.709711,8.403090,3.968438,2.257416,2.053811,7.107586],[4.426393,9.497120,2.034618,1.724900,-0.333824,3.874190,6.615435,-1.380490],[-0.342479,-8.288655,-3.542873,-1.263684,-4.721228,0.823049,9.041078,-2.108752],[2.561982,2.318891,-8.723321,-1.700118,-9.039127,8.114112,-5.210826,-5.918918],[9.504469,-4.668095,-6.254270,8.058953,0.173075,-3.381405,3.122195,0.647159],[-8.423938,3.924255,5.260173,1.452686,5.706644,-3.301630,-6.278617,-1.687374],[9.957380,-5.172129,-4.954259,-3.709840,-0.172285,-9.332612,-9.111943,5.838035],[-0.802859,3.089208,-5.848260,5.278339,2.613438,-1.973167,-7.940270,2.068399]],[[5.960086,3.757175,3.867967,3.175869,0.404401,-9.905012,4.880331,-6.345022],[-7.398807,-9.720716,2.261380,7.305659,9.515699,-4.439464,-1.246567,3.148401],[3.918061,8.168435,2.253642,0.478545,1.584950,-0.070383,1.690580,-7.000103],[-1.848182,-7.291127,0.425222,-9.922631,7.199544,-9.288495,9.522133,-8.268888],[9.515073,1.364670,-7.768608,9.165713,-3.103060,5.457290,-3.701034,-5.990864],[-6.278916,-8.709481,-4.824960,-9.620315,-3.880283,7.499789,-3.012376,-2.046194],[-1.015523,-9.891210,-7.394190,-7.953100,9.007705,-2.087872,5.566610,-9.735773],[-5.664402,3.555379,-8.423961,-4.292933,9.492082,-3.557338,0.572018,1.219283]]], dtype = "float32")#candidate|1259|(2, 8, 8)|const|float32
var_1260 = relay.var("var_1260", dtype = "float32", shape = (2, 8, 8))#candidate|1260|(2, 8, 8)|var|float32
bop_1261 = relay.divide(const_1259.astype('float32'), relay.reshape(var_1260.astype('float32'), relay.shape_of(const_1259))) # shape=(2, 8, 8)
output = relay.Tuple([bop_1261,])
output2 = relay.Tuple([bop_1261,])
func_1264 = relay.Function([var_1260,], output)
mod['func_1264'] = func_1264
mod = relay.transform.InferType()(mod)
mutated_mod['func_1264'] = func_1264
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1265 = relay.var("var_1265", dtype = "float32", shape = (2, 8, 8))#candidate|1265|(2, 8, 8)|var|float32
func_1264_call = mutated_mod.get_global_var('func_1264')
call_1266 = func_1264_call(var_1265)
output = call_1266
func_1267 = relay.Function([var_1265], output)
mutated_mod['func_1267'] = func_1267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_1326 = relay.TupleGetItem(func_609_call(), 0)
call_1327 = relay.TupleGetItem(func_611_call(), 0)
func_820_call = mod.get_global_var('func_820')
func_821_call = mutated_mod.get_global_var('func_821')
call_1338 = relay.TupleGetItem(func_820_call(), 0)
call_1339 = relay.TupleGetItem(func_821_call(), 0)
func_1264_call = mod.get_global_var('func_1264')
func_1267_call = mutated_mod.get_global_var('func_1267')
var_1343 = relay.var("var_1343", dtype = "float32", shape = (128,))#candidate|1343|(128,)|var|float32
call_1342 = relay.TupleGetItem(func_1264_call(relay.reshape(var_1343.astype('float32'), [2, 8, 8])), 0)
call_1344 = relay.TupleGetItem(func_1267_call(relay.reshape(var_1343.astype('float32'), [2, 8, 8])), 0)
func_1264_call = mod.get_global_var('func_1264')
func_1267_call = mutated_mod.get_global_var('func_1267')
call_1345 = relay.TupleGetItem(func_1264_call(relay.reshape(var_1343.astype('float32'), [2, 8, 8])), 0)
call_1346 = relay.TupleGetItem(func_1267_call(relay.reshape(var_1343.astype('float32'), [2, 8, 8])), 0)
func_766_call = mod.get_global_var('func_766')
func_769_call = mutated_mod.get_global_var('func_769')
var_1355 = relay.var("var_1355", dtype = "float32", shape = (30,))#candidate|1355|(30,)|var|float32
call_1354 = relay.TupleGetItem(func_766_call(relay.reshape(var_1355.astype('float32'), [3, 10, 1])), 1)
call_1356 = relay.TupleGetItem(func_769_call(relay.reshape(var_1355.astype('float32'), [3, 10, 1])), 1)
output = relay.Tuple([call_1326,call_1338,call_1342,var_1343,call_1345,call_1354,var_1355,])
output2 = relay.Tuple([call_1327,call_1339,call_1344,var_1343,call_1346,call_1356,var_1355,])
func_1372 = relay.Function([var_1343,var_1355,], output)
mod['func_1372'] = func_1372
mod = relay.transform.InferType()(mod)
mutated_mod['func_1372'] = func_1372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1372_call = mutated_mod.get_global_var('func_1372')
var_1374 = relay.var("var_1374", dtype = "float32", shape = (128,))#candidate|1374|(128,)|var|float32
var_1375 = relay.var("var_1375", dtype = "float32", shape = (30,))#candidate|1375|(30,)|var|float32
call_1373 = func_1372_call(var_1374,var_1375,)
output = call_1373
func_1376 = relay.Function([var_1374,var_1375,], output)
mutated_mod['func_1376'] = func_1376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_1380 = relay.TupleGetItem(func_254_call(), 0)
call_1381 = relay.TupleGetItem(func_255_call(), 0)
func_766_call = mod.get_global_var('func_766')
func_769_call = mutated_mod.get_global_var('func_769')
const_1432 = relay.const([-0.220566,-0.327266,-3.383368,8.658906,0.173073,-7.429561,6.469042,-2.771986,0.009813,3.345506,9.650791,9.371507,7.673307,4.877218,-5.888906,-3.273341,3.496500,1.591384,8.351497,-1.227008,-4.723069,-6.031389,-7.026818,0.325497,5.144461,1.049661,-6.472184,8.430092,-8.428247,-3.840383], dtype = "float32")#candidate|1432|(30,)|const|float32
call_1431 = relay.TupleGetItem(func_766_call(relay.reshape(const_1432.astype('float32'), [3, 10, 1])), 0)
call_1433 = relay.TupleGetItem(func_769_call(relay.reshape(const_1432.astype('float32'), [3, 10, 1])), 0)
output = relay.Tuple([call_1380,call_1431,const_1432,])
output2 = relay.Tuple([call_1381,call_1433,const_1432,])
func_1435 = relay.Function([], output)
mod['func_1435'] = func_1435
mod = relay.transform.InferType()(mod)
mutated_mod['func_1435'] = func_1435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1435_call = mutated_mod.get_global_var('func_1435')
call_1436 = func_1435_call()
output = call_1436
func_1437 = relay.Function([], output)
mutated_mod['func_1437'] = func_1437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_627_call = mod.get_global_var('func_627')
func_629_call = mutated_mod.get_global_var('func_629')
call_1440 = relay.TupleGetItem(func_627_call(), 0)
call_1441 = relay.TupleGetItem(func_629_call(), 0)
output = call_1440
output2 = call_1441
func_1442 = relay.Function([], output)
mod['func_1442'] = func_1442
mod = relay.transform.InferType()(mod)
mutated_mod['func_1442'] = func_1442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1442_call = mutated_mod.get_global_var('func_1442')
call_1443 = func_1442_call()
output = call_1443
func_1444 = relay.Function([], output)
mutated_mod['func_1444'] = func_1444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1100_call = mod.get_global_var('func_1100')
func_1101_call = mutated_mod.get_global_var('func_1101')
call_1594 = func_1100_call()
call_1595 = func_1100_call()
uop_1606 = relay.log10(call_1594.astype('float32')) # shape=(3, 8, 1)
uop_1608 = relay.log10(call_1595.astype('float32')) # shape=(3, 8, 1)
bop_1610 = relay.floor_divide(uop_1606.astype('float64'), relay.reshape(call_1594.astype('float64'), relay.shape_of(uop_1606))) # shape=(3, 8, 1)
bop_1613 = relay.floor_divide(uop_1608.astype('float64'), relay.reshape(call_1595.astype('float64'), relay.shape_of(uop_1608))) # shape=(3, 8, 1)
bop_1614 = relay.maximum(bop_1610.astype('float32'), relay.reshape(call_1594.astype('float32'), relay.shape_of(bop_1610))) # shape=(3, 8, 1)
bop_1617 = relay.maximum(bop_1613.astype('float32'), relay.reshape(call_1595.astype('float32'), relay.shape_of(bop_1613))) # shape=(3, 8, 1)
var_1627 = relay.var("var_1627", dtype = "float32", shape = (3, 8, 14))#candidate|1627|(3, 8, 14)|var|float32
bop_1628 = relay.less(call_1594.astype('bool'), var_1627.astype('bool')) # shape=(3, 8, 14)
bop_1631 = relay.less(call_1595.astype('bool'), var_1627.astype('bool')) # shape=(3, 8, 14)
func_1058_call = mod.get_global_var('func_1058')
func_1062_call = mutated_mod.get_global_var('func_1062')
var_1634 = relay.var("var_1634", dtype = "uint16", shape = (1344,))#candidate|1634|(1344,)|var|uint16
call_1633 = relay.TupleGetItem(func_1058_call(relay.reshape(var_1634.astype('uint16'), [12, 14, 8]), relay.reshape(var_1634.astype('uint16'), [12, 14, 8]), ), 0)
call_1635 = relay.TupleGetItem(func_1062_call(relay.reshape(var_1634.astype('uint16'), [12, 14, 8]), relay.reshape(var_1634.astype('uint16'), [12, 14, 8]), ), 0)
output = relay.Tuple([bop_1614,bop_1628,call_1633,var_1634,])
output2 = relay.Tuple([bop_1617,bop_1631,call_1635,var_1634,])
func_1639 = relay.Function([var_1627,var_1634,], output)
mod['func_1639'] = func_1639
mod = relay.transform.InferType()(mod)
mutated_mod['func_1639'] = func_1639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1639_call = mutated_mod.get_global_var('func_1639')
var_1641 = relay.var("var_1641", dtype = "float32", shape = (3, 8, 14))#candidate|1641|(3, 8, 14)|var|float32
var_1642 = relay.var("var_1642", dtype = "uint16", shape = (1344,))#candidate|1642|(1344,)|var|uint16
call_1640 = func_1639_call(var_1641,var_1642,)
output = call_1640
func_1643 = relay.Function([var_1641,var_1642,], output)
mutated_mod['func_1643'] = func_1643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1127_call = mod.get_global_var('func_1127')
func_1128_call = mutated_mod.get_global_var('func_1128')
call_1725 = func_1127_call()
call_1726 = func_1127_call()
func_1435_call = mod.get_global_var('func_1435')
func_1437_call = mutated_mod.get_global_var('func_1437')
call_1728 = relay.TupleGetItem(func_1435_call(), 0)
call_1729 = relay.TupleGetItem(func_1437_call(), 0)
uop_1746 = relay.asinh(call_1725.astype('float32')) # shape=(3, 8, 16)
uop_1748 = relay.asinh(call_1726.astype('float32')) # shape=(3, 8, 16)
output = relay.Tuple([call_1728,uop_1746,])
output2 = relay.Tuple([call_1729,uop_1748,])
func_1749 = relay.Function([], output)
mod['func_1749'] = func_1749
mod = relay.transform.InferType()(mod)
mutated_mod['func_1749'] = func_1749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1749_call = mutated_mod.get_global_var('func_1749')
call_1750 = func_1749_call()
output = call_1750
func_1751 = relay.Function([], output)
mutated_mod['func_1751'] = func_1751
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1777 = relay.var("var_1777", dtype = "float64", shape = (13, 9, 14))#candidate|1777|(13, 9, 14)|var|float64
uop_1778 = relay.erf(var_1777.astype('float64')) # shape=(13, 9, 14)
output = uop_1778
output2 = uop_1778
func_1780 = relay.Function([var_1777,], output)
mod['func_1780'] = func_1780
mod = relay.transform.InferType()(mod)
mutated_mod['func_1780'] = func_1780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1781 = relay.var("var_1781", dtype = "float64", shape = (13, 9, 14))#candidate|1781|(13, 9, 14)|var|float64
func_1780_call = mutated_mod.get_global_var('func_1780')
call_1782 = func_1780_call(var_1781)
output = call_1782
func_1783 = relay.Function([var_1781], output)
mutated_mod['func_1783'] = func_1783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_1797 = relay.TupleGetItem(func_515_call(), 1)
call_1798 = relay.TupleGetItem(func_516_call(), 1)
func_1127_call = mod.get_global_var('func_1127')
func_1128_call = mutated_mod.get_global_var('func_1128')
call_1809 = func_1127_call()
call_1810 = func_1127_call()
uop_1812 = relay.cosh(call_1797.astype('float64')) # shape=(3, 8, 16)
uop_1814 = relay.cosh(call_1798.astype('float64')) # shape=(3, 8, 16)
output = relay.Tuple([call_1809,uop_1812,])
output2 = relay.Tuple([call_1810,uop_1814,])
func_1823 = relay.Function([], output)
mod['func_1823'] = func_1823
mod = relay.transform.InferType()(mod)
mutated_mod['func_1823'] = func_1823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mutated_mod.get_global_var('func_1823')
call_1824 = func_1823_call()
output = call_1824
func_1825 = relay.Function([], output)
mutated_mod['func_1825'] = func_1825
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1831 = relay.const([[[9],[-9],[-1],[3],[-6],[2],[9],[9]],[[6],[-6],[-5],[7],[1],[4],[1],[7]],[[7],[2],[-2],[8],[3],[-10],[-5],[-4]],[[6],[9],[10],[1],[-10],[-3],[10],[-4]]], dtype = "int32")#candidate|1831|(4, 8, 1)|const|int32
var_1832 = relay.var("var_1832", dtype = "int32", shape = (4, 8, 7))#candidate|1832|(4, 8, 7)|var|int32
bop_1833 = relay.bitwise_xor(const_1831.astype('int32'), var_1832.astype('int32')) # shape=(4, 8, 7)
func_1780_call = mod.get_global_var('func_1780')
func_1783_call = mutated_mod.get_global_var('func_1783')
const_1849 = relay.const([-3.610129,8.464597,7.295502,8.047275,1.705112,-9.423607,-3.874753,9.926251,3.733280,0.929046,-9.836128,-1.043759,-4.741736,4.388136,4.114267,-4.939636,1.777613,3.667606,3.942285,-4.110014,0.564887,5.405905,7.833394,-2.108380,-2.355878,8.781678,5.946114,9.941671,-7.889733,0.895501,1.223442,3.477881,3.451026,-5.774613,4.174422,0.678055,3.038552,-9.254868,2.327054,5.188076,-8.568928,-1.388697,-2.249624,-4.952199,-0.965102,3.210860,7.981769,-4.334455,0.194656,1.081921,1.378566,9.019517,2.383486,-7.340506,-6.294838,5.212274,-7.629599,-6.637291,8.204438,2.640586,-7.637593,-1.772656,8.239408,-5.678509,9.484942,6.351058,7.396142,1.454409,-2.052643,1.679294,9.870916,-7.041439,2.651895,0.090665,4.408873,-3.451454,7.684622,2.513016,-9.697723,4.570385,0.072412,-1.146534,6.399785,-8.489485,3.061936,-6.518713,-7.955547,3.908688,7.528902,-4.089108,7.824494,-5.243487,9.112085,-0.680597,9.904301,1.141058,-3.988444,4.963478,0.440179,-2.318254,-1.059020,-7.992594,4.696769,-9.297516,-0.360948,8.170024,2.598569,-7.606961,7.413164,-3.820804,-4.360458,8.068440,-6.505686,-5.031626,-4.402328,-4.385404,0.171305,0.904211,-6.804310,8.980419,8.601676,3.295295,-8.847444,3.487630,-5.691004,-5.108945,-4.093864,3.049243,6.172802,-6.666114,-8.816070,-3.904987,6.245937,-3.728628,9.255800,-8.173932,-9.685467,1.390219,5.094446,-0.736694,1.870082,-6.681047,9.137249,-6.815394,9.353359,-7.828128,7.513669,5.920852,9.467195,0.836949,3.892428,0.784798,6.428029,-3.313404,3.287574,-6.330522,-4.068772,-6.233143,-1.070636,-6.807076,-0.380310,-2.851635,4.942433,-6.346085,0.521307,1.467096,-8.455805,1.437819,0.037400,-6.139271,-4.566324,1.687419,-4.520792,-4.576252,-6.705900,-8.585335,-1.206458,2.149827,2.745148,-5.913518,9.672962,9.807583,-8.494688,8.470875,5.580883,-6.874815,-1.177818,-2.330687,-6.148415,1.487389,3.232799,6.283765,-1.196602,8.501890,-4.813712,1.926190,3.713876,9.795859,0.817524,8.105307,6.858754,-3.958323,-1.420615,-5.910473,-3.126801,4.823669,3.300934,3.062492,2.547024,1.397761,-9.422746,1.682443,-4.916863,0.675369,9.299848,-3.834578,-2.057701,-7.074416,5.045293,1.222535,5.495861,5.591108,7.683049,-9.382318,6.621042,2.495543,-2.374342,0.722629,0.451558,-6.902509,0.119525,1.777138,-0.924981,-7.643924,-8.680273,1.193858,9.189904,6.771123,7.062824,2.315984,2.132989,-4.629584,-0.379053,-0.741695,-8.618531,-0.671776,5.340302,9.929662,-9.385109,0.131069,-8.314467,-6.810686,8.505605,-0.406035,5.574447,1.182617,-5.966436,4.216041,4.691748,3.227778,-8.064724,-3.020413,7.574961,0.160027,9.305869,9.862926,2.204323,7.396819,0.998116,0.426373,-8.792587,6.431231,-2.203057,2.922850,7.858967,9.808239,-8.470468,8.816424,-6.801010,8.501279,-3.550007,3.163726,-6.917029,-2.470853,-5.574391,1.419824,4.440268,-2.795902,2.962284,3.085795,-6.064728,-1.599332,-3.319251,-1.592724,4.465360,7.347769,-9.319409,0.968175,8.002330,-8.935685,-6.130602,-7.343681,2.677249,5.509487,-1.717409,6.827136,-0.798644,-9.837277,2.524982,2.808114,-8.502826,-4.019447,9.576218,-7.573154,-9.547895,-0.759925,-6.851987,-2.402160,3.628356,-9.251819,-4.190598,-6.404952,1.769551,-0.966265,-8.264689,3.042928,-5.162882,5.346414,-7.405424,-4.799717,6.344769,8.424983,-5.956378,0.197588,0.853817,3.931053,9.637228,-0.147114,-2.294677,8.194865,-3.656945,-6.618956,2.347700,-5.511817,2.600788,-1.404851,-8.433455,-6.562086,2.449585,-5.518491,6.091560,-8.738727,-5.771390,5.092631,6.003960,9.850406,-2.674128,-1.844387,2.305473,7.408053,-4.381190,4.903598,1.898534,6.004882,7.440648,1.376617,3.293158,5.499365,0.298459,1.609323,-4.613721,-4.902431,-5.187229,-0.369191,-7.004798,-9.501101,8.039774,6.495440,6.455815,8.395457,-6.055865,6.995306,-8.741439,9.807994,4.577096,1.068102,6.683373,-8.741697,-5.114781,-1.256575,-5.332364,7.187549,-9.040322,-8.309148,5.378756,6.034309,0.133623,-9.992904,4.522456,9.344235,-3.817811,-2.526709,-4.104523,6.676236,9.486001,8.689348,-9.107859,1.589199,8.878136,-6.187943,3.142298,8.903539,-0.812070,5.030934,9.017257,-5.909867,5.113666,-3.132092,-6.609406,-0.915191,5.457187,5.101397,5.103817,-3.740772,4.427776,6.785975,-9.969392,4.800778,-8.589096,3.373557,1.313058,9.608233,-8.034681,-4.214495,5.219788,1.667879,5.790152,-9.073892,1.866739,2.596828,8.575888,-3.763650,1.384563,-3.198056,-7.014346,-4.269235,-7.820131,-2.538295,4.883052,3.932628,5.993280,9.620184,1.084004,1.243045,-0.030461,8.876680,-2.268033,-9.565141,1.403986,4.939957,-6.683131,9.365060,-0.599259,7.671343,8.113058,-4.326908,4.392081,7.212049,-9.197562,-8.344460,3.632603,-6.937278,9.598852,-8.258767,-4.832555,-6.963728,7.332057,8.448336,6.081730,4.354805,0.567370,5.672430,0.669177,1.239481,-2.218736,-3.488300,-8.648369,7.000249,6.081579,-3.466156,4.125409,-0.045361,3.131765,-7.926320,8.375924,2.193904,-8.927294,0.084526,3.863477,3.279878,-9.021754,5.705413,-2.292680,-9.211965,-5.112209,4.911048,1.711705,-0.428256,3.545898,1.806294,-2.975139,3.658400,-7.431363,-0.513137,-7.804854,8.515160,-1.104242,2.148058,2.331235,-2.022725,-6.141908,7.874766,-8.324420,-9.454039,3.471434,-9.374238,-4.862019,-9.411384,-7.005038,-1.698603,-1.823146,-8.047567,3.238683,7.556934,0.108043,-3.779802,-3.802893,-6.556915,-3.005124,-1.495244,-0.213473,7.094483,1.489452,6.721057,0.606876,-7.746470,9.186968,-0.927550,-7.504274,4.554457,6.972323,2.835386,-2.716285,-2.666205,9.093271,-5.377931,7.224527,-7.173753,2.958799,4.406715,-7.404292,-2.731766,-5.331731,-7.965127,-6.252024,-5.892368,2.755137,3.212410,8.625146,-9.243161,1.657287,4.684895,7.871861,6.807699,0.659889,6.871556,-3.582071,-6.232214,-0.303017,6.220029,-8.396937,-8.428519,9.224345,2.794383,-7.602498,9.136830,-0.680285,-0.880844,5.795036,-0.492196,-3.785317,-7.791570,2.301612,4.293098,0.037736,4.934647,6.880757,6.440433,1.215326,4.574103,0.536611,8.372084,8.585513,3.947892,0.671502,-0.305598,3.938716,-3.779512,7.934016,-8.084304,-4.993916,-6.186638,0.882224,1.437990,3.853262,-4.046568,1.477382,-6.802676,-4.989985,5.089811,-2.980195,8.246075,-6.162273,-3.753379,-2.700894,-1.330996,-7.856783,-0.794185,2.903004,3.194103,-2.535348,3.292003,6.717730,6.271155,0.962271,-6.857771,-7.051311,8.340743,0.797647,-5.972359,-1.499244,3.893895,9.547388,-5.171653,9.444090,9.487508,-0.904886,2.909220,0.163446,2.726581,-6.565163,-0.466269,9.350729,3.611490,5.758612,-1.023450,9.129176,9.346623,3.884537,8.328859,5.598737,4.663364,5.651098,7.081512,8.148645,1.263443,-0.454427,-7.238212,4.103096,9.746768,8.217906,-9.344043,4.683894,3.661832,5.398378,8.850968,-4.437602,-8.944745,3.070872,-7.955151,-1.071295,-8.788265,6.439078,8.441605,9.255702,7.867394,-0.209836,8.870502,3.625721,5.635326,7.305285,2.613347,3.345009,4.174433,-2.952278,3.646208,5.833069,5.755216,-4.137879,4.191468,5.900181,-6.570087,-6.931590,9.366248,-3.343656,-2.330825,5.510406,7.045237,-9.005847,-9.180531,-4.162513,2.924919,4.415239,-5.118674,1.924871,1.404514,7.961109,2.303443,0.743137,5.332520,4.294338,0.452384,-4.344517,3.064384,8.873676,8.073915,9.261845,3.726960,5.170242,-1.597065,4.796493,-4.953013,7.647184,-4.125035,-8.270614,-2.436891,-9.969008,1.532654,0.426586,1.829186,-0.946454,-4.502352,7.947841,-7.777696,-3.622384,-2.679211,4.527602,-9.678845,-8.105895,5.654360,-1.507128,-4.257323,-5.658795,3.800075,-5.229880,-3.901652,0.594235,-8.706918,8.288279,-9.919511,1.932420,1.422473,9.499716,3.889987,3.200213,-3.920889,-7.362873,-4.895015,-2.410734,-6.285820,-1.060082,0.323626,-9.463068,-7.881878,5.239241,3.801528,2.449779,6.782367,-0.870614,-9.326652,1.826502,8.263684,3.020219,-8.959951,-3.083184,-6.330699,-6.401247,-5.159953,8.916663,-8.771153,1.523354,2.132619,-7.800865,2.439939,2.554876,-6.320888,7.623792,6.625361,6.763351,-0.134689,-0.986858,-0.422237,9.833593,9.694881,-4.351465,9.270746,0.752698,-8.632551,1.613904,-7.503068,-4.669689,6.169351,7.852276,-8.128758,3.505110,-6.210624,-7.752545,-3.755520,9.941202,-9.230207,3.825017,-6.502222,3.373438,-0.411342,-3.156998,8.754352,-1.055574,-3.617171,6.890842,-1.201491,-0.794057,0.078054,-8.216018,-9.363265,2.995722,5.170254,-8.978705,-1.760631,-2.812617,-9.130817,0.197109,6.280151,-6.608476,8.032403,7.747923,-3.983150,-4.243795,-1.421045,8.426400,8.422923,4.158484,5.449724,-5.463704,6.672997,0.502384,3.301941,-8.014456,-7.373872,3.280454,-2.363216,3.228814,-4.196710,-2.465541,-6.907774,8.017416,7.451511,-5.019732,-4.175100,-7.584252,-8.921489,5.325987,-6.159842,-6.236891,-0.319931,5.861125,-7.649343,-3.322164,-6.870985,7.724926,-1.530041,-0.088453,-2.453055,8.863960,8.135437,-4.877250,6.081970,-7.058318,7.955802,-7.614599,-6.942950,1.434260,-3.639100,3.356678,-1.171427,-9.792992,6.604977,-7.766666,3.553038,-8.839345,3.590122,-7.787575,-1.977535,9.113424,-6.123087,0.442480,5.244287,1.582511,-8.064589,-7.510062,-2.525416,-9.223986,-8.807945,1.764385,-9.258829,-2.573063,-8.534924,-1.326509,5.154554,1.768501,4.154124,-1.836520,9.368948,-6.469781,-1.623459,-3.398311,5.334528,-8.958093,-7.238124,-1.703116,5.232112,-5.463299,7.164849,-5.190764,-4.048116,-1.357187,1.007635,-3.483992,1.318901,-9.739679,-2.584994,-5.913178,4.502658,8.072802,-0.272783,-1.402793,-4.934786,6.471423,6.781216,2.154944,1.965635,4.518786,-3.239020,4.233762,2.084456,-0.330197,2.767010,6.731529,6.627093,-6.340463,-8.149142,-7.582065,3.938673,6.215919,4.607329,5.805495,-3.352155,6.636520,-6.113107,-5.610524,5.353433,2.034075,3.101301,4.051733,3.173189,-7.020731,3.424504,6.902575,0.549092,2.499276,1.236212,8.140024,-7.801287,-5.294523,-1.505667,-8.934028,8.024897,-3.082273,-2.852332,-6.362999,8.458076,-1.569783,4.311117,1.540979,-2.526472,2.191213,2.916393,0.747283,-1.719518,7.779221,1.072788,-4.247355,1.175283,9.264188,-3.689954,-8.601178,4.614423,-4.528993,-2.523215,3.013183,8.345317,-2.108519,0.541128,-3.614439,7.210170,-9.090551,3.416931,-1.934996,4.771566,-7.523109,1.333861,2.357773,9.864288,4.870172,-9.661216,-1.136321,0.030067,-5.430610,0.106701,-7.105810,-2.140863,4.959850,2.307430,5.443793,2.938154,9.964148,-4.282281,2.178603,-4.818155,8.917783,6.610516,-6.004956,-5.768312,-9.297357,1.452916,-9.490943,0.683150,9.703847,2.091641,-4.643840,3.947280,3.137806,-1.181636,6.877407,2.972623,4.671407,0.157023,-8.897734,5.404472,5.912685,1.575954,-0.227762,8.640376,-5.580007,-8.673470,8.521223,-2.040997,6.313290,-6.693669,0.687842,2.323209,-9.324659,3.171085,-7.998570,3.013197,8.059760,-4.187424,-2.280743,-2.132897,-9.866744,7.192567,-1.092341,6.668974,-3.133333,-5.073338,9.631830,6.327660,-2.081872,-7.179813,5.892511,-9.365767,6.166090,-6.623789,-2.666426,-9.228775,-9.774050,1.380786,1.150603,-2.214539,-5.865742,9.235977,0.686813,9.701234,1.957512,-1.721596,-4.288311,-5.823596,5.976672,1.828265,5.419156,8.510611,2.638662,-3.715486,8.764154,-4.351023,6.574510,5.220696,-8.963891,1.277928,2.810909,-7.452685,-3.789972,5.986723,-2.112825,-2.417802,-1.138891,0.325477,-2.762427,-4.007141,-3.609732,4.424064,-3.042025,-9.709962,6.976623,5.792340,-9.913400,-5.412598,-2.507086,-0.305519,-1.969910,-2.283296,-9.421295,-0.470787,6.690034,-8.824274,-1.926203,3.785251,6.614497,0.527951,6.744949,1.353768,7.115447,5.566253,8.509757,-9.422529,-8.760501,-0.949946,-3.327485,8.666893,4.397244,6.487475,5.580831,-2.280381,5.155132,2.475437,-3.773504,-9.573336,4.294983,1.202178,5.067610,-6.527162,-0.313139,5.104175,-3.078248,-8.361304,-0.544715,2.176641,9.141099,-8.966844,9.426636,7.073598,-6.122033,1.099061,1.147804,-4.825312,-1.375717,-6.750512,7.811010,4.705328,-6.557850,9.380549,-3.362101,-5.821092,9.924588,-7.431761,9.342750,-6.561611,3.097577,0.716792,4.450153,1.073405,-6.876549,-7.533613,7.211817,3.918388,-1.404846,9.608633,9.842991,-7.947551,-9.336533,-5.497200,-9.822958,-7.085136,-2.034396,4.140153,6.147880,-0.985148,-4.793740,-0.556016,-5.436097,-0.184220,-0.521302,8.571686,3.172205,-4.648711,-1.368976,1.417089,-7.712134,-0.184455,5.593387,-7.289688,7.606475,0.904649,7.748360,6.283466,4.372717,-3.488909,5.799181,-4.837301,1.599192,3.170705,7.255607,0.183263,-2.538703,-2.619311,2.363637,-1.991846,8.715088,-3.306251,9.105468,8.111119,8.316293,2.365966,8.327911,-7.621109,-9.692331,8.856449,-3.069293,0.942248,-3.679484,0.771195,-4.496316,-9.923855,2.599520,8.302950,7.045011,0.567670,-8.451475,0.954941,-7.839983,4.141381,6.792693,-7.153595,2.990433,-8.321727,-0.771068,6.472260,-1.729347,-0.237245,-2.383344,-1.197264,-4.559983,3.278392,-0.813399,9.059592,-0.314963,-7.857476,9.321497,3.435621,-5.224838,-2.274155,4.435349,-0.189903,-7.680583,2.409185,-7.498854,-0.337238,-5.859107,7.964871,-6.011745,0.673598,7.827217,4.969383,4.190285,6.394326,-2.251747,-3.270175,7.086314,1.096058,7.709644,5.712973,4.471915,5.852749,7.545114,-5.701534,8.057101,-7.255181,1.669192,2.039884,-6.979583,0.101999,-2.626130,4.161365,-4.522725,5.724256,4.567260,8.784950,-2.989886,-1.800662,7.286080,-2.911293,4.746744,-8.729339,-4.480788,5.270891,-6.577082,8.330488,-7.560008,7.052768,-5.170139,-2.319598,2.320380,-3.602391,-7.259864,3.980993,9.706729,-5.077081,-6.815533,-5.675533,-6.469639,0.645603,-9.947508,-3.652670,4.870178,1.706851,-5.044033,-4.009175,9.926689,-5.865284,1.388606,5.749463,3.744081,3.715171,-7.022182,-5.935117,5.155921,-5.633362,-8.703123,-0.590013,-9.620058,9.253652,-4.914706,-6.762104,-3.333016,7.678726,-4.292402,1.470664,9.657372,8.253627,-2.873094,-5.045322,7.218671,6.317284,5.208624,-6.651828,4.417650,0.452284,8.637983,8.033955,-4.383035,8.816593,1.602206,-0.596176,-3.872348,8.451404,8.185089,-6.195211,-9.986124,-7.798002,-8.833329,8.589761,0.843677,9.838581,-9.424484,-3.938776,4.067453,4.502314,-0.552588,3.735083,7.586869,6.575233,1.286819,8.682653,5.808965,6.418104,-4.074875,2.671992,5.476712,-0.063730,1.993510,-1.291260,0.099733,-1.969091,5.805421,-3.351167,-6.805587,1.743502,7.096874,9.802565,6.989780,-4.747312,1.745029,4.697075,-8.591091,-3.662111,-8.174479,1.990831,-7.915640,-9.818422,0.623208,-3.528347,-6.250480,7.639275,-7.008883,3.595324,-4.573102,-7.157717,3.589372,-2.831892,7.264265,-1.563991,-6.607667,9.162524,1.515434,-2.218078,-3.387870,-6.096820,8.159178,9.063681,-1.236819,7.538623,-7.960439,-5.666839,0.953374,-4.990782,2.194392,-5.246884,-4.077788,-2.369981,7.685048,-0.310960,3.669943,1.064304,2.106356,-7.738160,6.733333,-1.416935,9.750343,5.378731,3.873436,-2.394781,-8.617767,-6.323989,-5.401063,-9.752183,-5.073887,-3.688798,1.418539,-6.895319,-7.112243,-9.206471,-9.746086,5.622283,8.573184,-7.124040,-4.580427,5.002745,5.859256,1.477602,-6.097154,-5.008261,5.255719,-3.009835,-9.141368,7.672136,-8.722154,-5.924446,-7.027558,-9.453870,-0.451013,-2.347395,6.424416,-5.538790,-0.226045,2.208788,1.662052,0.866661,-0.012547,-1.519582,-2.750117,3.614337,1.372189,4.117395,5.130982,-3.884463,-3.693660,9.135011,-0.240654,-8.985391,5.728057,-1.676866,5.443029,3.487584,1.607819,-6.001292,1.265053,-9.472039,2.369147,-2.267444,-3.568434,7.108235,-0.232134,-6.435017,-3.453611,8.066239,-8.232628,-9.827531,9.635187,4.853547,9.955414,-1.851138,8.421939,-7.737099,-9.376309,-2.994928,9.095283,7.528456,-0.837517,-1.516459,-4.431531,-1.894388,2.920286,8.823416,4.656381,-4.206073,-4.238298,2.187658,3.173183,8.516751,9.840114,-1.397322,9.987611,-1.756176,-8.304575,-9.397188,-0.521673,9.903866,5.058580,-4.937242,-3.318445,-4.192936,1.880901,-5.436118,1.814303,-7.035411,6.712329,6.780067,-8.159235,-9.838611,-7.245045,7.106656,-6.127922,8.908321,4.817867,-3.928528,-0.834446,8.854382,-5.514178,-3.818068,8.826562,-6.142053,-7.699948,9.806395,4.646569,8.340723,-5.465478,-6.349833,3.784517,-2.392257,5.331260,-3.878831,9.374147,9.139550,-5.707038,9.534562,-5.234643,-6.900653,3.825075,6.499462,-8.436044,7.815209,-5.035360,6.743926,7.719430,-6.601733,-5.760349,-8.973044,-5.417260,5.257292,5.174737,-5.857065,8.605829,-9.519985,-5.918316,4.989484,-2.144664,7.275203,9.692113,8.059199], dtype = "float64")#candidate|1849|(1638,)|const|float64
call_1848 = func_1780_call(relay.reshape(const_1849.astype('float64'), [13, 9, 14]))
call_1850 = func_1780_call(relay.reshape(const_1849.astype('float64'), [13, 9, 14]))
bop_1852 = relay.bitwise_or(call_1848.astype('int64'), relay.reshape(const_1849.astype('int64'), relay.shape_of(call_1848))) # shape=(13, 9, 14)
bop_1855 = relay.bitwise_or(call_1850.astype('int64'), relay.reshape(const_1849.astype('int64'), relay.shape_of(call_1850))) # shape=(13, 9, 14)
func_1254_call = mod.get_global_var('func_1254')
func_1257_call = mutated_mod.get_global_var('func_1257')
var_1860 = relay.var("var_1860", dtype = "float32", shape = (384,))#candidate|1860|(384,)|var|float32
call_1859 = relay.TupleGetItem(func_1254_call(relay.reshape(var_1860.astype('float32'), [3, 8, 16])), 0)
call_1861 = relay.TupleGetItem(func_1257_call(relay.reshape(var_1860.astype('float32'), [3, 8, 16])), 0)
output = relay.Tuple([bop_1833,bop_1852,call_1859,var_1860,])
output2 = relay.Tuple([bop_1833,bop_1855,call_1861,var_1860,])
func_1872 = relay.Function([var_1832,var_1860,], output)
mod['func_1872'] = func_1872
mod = relay.transform.InferType()(mod)
var_1873 = relay.var("var_1873", dtype = "int32", shape = (4, 8, 7))#candidate|1873|(4, 8, 7)|var|int32
var_1874 = relay.var("var_1874", dtype = "float32", shape = (384,))#candidate|1874|(384,)|var|float32
output = func_1872(var_1873,var_1874,)
func_1875 = relay.Function([var_1873,var_1874,], output)
mutated_mod['func_1875'] = func_1875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1127_call = mod.get_global_var('func_1127')
func_1128_call = mutated_mod.get_global_var('func_1128')
call_1906 = func_1127_call()
call_1907 = func_1127_call()
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_1925 = relay.TupleGetItem(func_1823_call(), 0)
call_1926 = relay.TupleGetItem(func_1825_call(), 0)
uop_1932 = relay.acosh(call_1906.astype('float64')) # shape=(3, 8, 16)
uop_1934 = relay.acosh(call_1907.astype('float64')) # shape=(3, 8, 16)
output = relay.Tuple([call_1925,uop_1932,])
output2 = relay.Tuple([call_1926,uop_1934,])
func_1940 = relay.Function([], output)
mod['func_1940'] = func_1940
mod = relay.transform.InferType()(mod)
output = func_1940()
func_1941 = relay.Function([], output)
mutated_mod['func_1941'] = func_1941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_627_call = mod.get_global_var('func_627')
func_629_call = mutated_mod.get_global_var('func_629')
call_2016 = relay.TupleGetItem(func_627_call(), 1)
call_2017 = relay.TupleGetItem(func_629_call(), 1)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_2027 = relay.TupleGetItem(func_515_call(), 1)
call_2028 = relay.TupleGetItem(func_516_call(), 1)
output = relay.Tuple([call_2016,call_2027,])
output2 = relay.Tuple([call_2017,call_2028,])
func_2031 = relay.Function([], output)
mod['func_2031'] = func_2031
mod = relay.transform.InferType()(mod)
output = func_2031()
func_2032 = relay.Function([], output)
mutated_mod['func_2032'] = func_2032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_2083 = relay.TupleGetItem(func_1940_call(), 0)
call_2084 = relay.TupleGetItem(func_1941_call(), 0)
output = call_2083
output2 = call_2084
func_2109 = relay.Function([], output)
mod['func_2109'] = func_2109
mod = relay.transform.InferType()(mod)
output = func_2109()
func_2110 = relay.Function([], output)
mutated_mod['func_2110'] = func_2110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1442_call = mod.get_global_var('func_1442')
func_1444_call = mutated_mod.get_global_var('func_1444')
call_2119 = func_1442_call()
call_2120 = func_1442_call()
output = relay.Tuple([call_2119,])
output2 = relay.Tuple([call_2120,])
func_2123 = relay.Function([], output)
mod['func_2123'] = func_2123
mod = relay.transform.InferType()(mod)
output = func_2123()
func_2124 = relay.Function([], output)
mutated_mod['func_2124'] = func_2124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_627_call = mod.get_global_var('func_627')
func_629_call = mutated_mod.get_global_var('func_629')
call_2132 = relay.TupleGetItem(func_627_call(), 1)
call_2133 = relay.TupleGetItem(func_629_call(), 1)
func_909_call = mod.get_global_var('func_909')
func_911_call = mutated_mod.get_global_var('func_911')
const_2152 = relay.const([[False,False],[True,False],[True,True],[True,True],[True,True],[True,True],[True,True],[True,False],[False,False],[False,True],[False,False],[True,True],[True,False],[True,False],[False,False],[True,True],[False,False],[True,True],[True,True],[True,False],[False,False],[False,True],[True,True],[True,False],[False,True],[True,False],[False,False],[True,True],[False,False],[True,False],[True,False],[True,True],[False,True],[True,True],[False,False],[False,False],[False,False],[True,False],[True,False],[False,True],[True,True],[True,True],[True,False],[True,True],[True,False],[True,False],[True,True],[True,True],[False,False],[True,False],[False,True],[False,True],[True,True],[True,False],[True,True],[False,False],[False,True],[False,True],[False,True],[False,True],[True,True],[True,False],[False,False],[False,False],[True,True],[False,True],[False,False],[False,True],[True,True],[True,False],[False,True],[True,False]], dtype = "bool")#candidate|2152|(72, 2)|const|bool
call_2151 = func_909_call(relay.reshape(const_2152.astype('bool'), [3, 8, 6]))
call_2153 = func_909_call(relay.reshape(const_2152.astype('bool'), [3, 8, 6]))
output = relay.Tuple([call_2132,call_2151,const_2152,])
output2 = relay.Tuple([call_2133,call_2153,const_2152,])
func_2157 = relay.Function([], output)
mod['func_2157'] = func_2157
mod = relay.transform.InferType()(mod)
output = func_2157()
func_2158 = relay.Function([], output)
mutated_mod['func_2158'] = func_2158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2174 = relay.var("var_2174", dtype = "float32", shape = (6, 6, 15))#candidate|2174|(6, 6, 15)|var|float32
const_2175 = relay.const([[[0.735668,1.746475,-1.811598,9.420513,-3.815265,6.953534,-0.671866,-1.709511,8.627173,8.967063,3.323734,-5.982985,1.415647,9.429722,4.252884],[-1.093393,3.287985,-0.610308,-0.252623,-5.274523,-7.751370,4.553104,-5.440357,-0.398669,-4.968644,6.308934,6.436908,-3.310710,6.918015,-3.434358],[-7.250345,-1.325401,-9.723470,-7.763038,-6.331414,6.956269,-5.554446,-0.886040,-9.127733,-6.355836,-6.066544,0.058505,1.087840,-0.353780,8.303353],[-1.712144,-0.144171,-6.298894,4.373989,9.957743,5.117437,-7.153556,9.100663,-2.356393,-3.887594,5.851155,5.173958,-9.074178,-0.960359,0.398016],[-8.806057,5.934806,-6.599975,5.236563,-4.964699,-3.946901,-8.024795,3.464165,5.889035,4.706433,5.835764,-7.655673,2.551436,5.390444,2.102059],[-8.479862,-6.995264,-9.878031,2.840050,-8.418216,9.836244,6.590776,-2.501737,0.006419,-2.923081,1.658254,0.627154,-6.845897,-3.325965,-7.849066]],[[1.236055,0.112889,3.155313,-4.946433,-6.620996,-2.392381,3.354431,1.725928,9.399954,0.134356,4.186510,6.609298,-7.548630,-2.359648,3.845429],[2.406805,5.630697,6.161517,-4.410527,4.816565,-9.429810,-7.981493,5.397244,4.564015,3.869907,-9.590289,4.513880,8.744105,-9.028757,3.820084],[4.034786,-3.410055,5.684338,1.461160,6.438706,-0.646806,-5.661539,-6.158181,-7.652626,-7.734100,-5.795890,2.441353,-7.771225,-1.086958,-1.459545],[7.181545,-0.537641,-0.611606,2.138969,0.115710,-3.780652,-7.912040,8.386540,-8.845937,8.498165,5.334646,5.407947,7.135891,0.566284,-0.548518],[4.745991,5.286291,0.422110,-2.797856,5.949158,-8.532551,3.145043,5.932946,0.908081,9.515618,-9.367802,-8.805834,3.079002,-9.467937,0.099351],[-3.575013,-2.817884,-7.931286,5.310690,-2.651263,6.306940,-0.659839,4.673362,7.264036,2.438113,3.378349,3.146591,6.765460,-9.484975,0.850921]],[[7.801736,-2.935269,-8.777313,3.106908,8.521350,-5.825363,-4.276564,-4.689128,-7.339404,-2.622899,-0.330693,-1.064571,-1.333057,-8.478448,9.270330],[-9.532964,0.794849,-5.165492,-1.596381,9.387698,0.674081,-5.747627,-7.287622,1.192980,-2.969778,-2.700236,-0.903911,-0.478372,-7.049253,0.676444],[-5.508211,-8.688493,-7.219495,2.499161,3.271636,4.490282,0.335765,-5.761273,-9.248489,-4.983787,-7.223429,3.220270,4.440582,0.689351,-5.940258],[2.528286,-5.641604,-4.390310,-5.742386,9.124805,-4.825004,-4.107389,-0.296767,2.145202,1.129827,8.007367,-7.343465,-6.753947,-5.233026,9.436340],[-2.774555,-9.249160,3.856654,9.844914,-3.160172,0.280418,1.687087,-0.120530,-4.949307,-8.447603,-8.520001,0.322289,-7.722805,-7.722846,4.039812],[5.075737,5.977410,2.273054,-5.216296,-3.502111,4.897277,3.044929,-5.955979,7.238044,8.002109,-3.291217,4.322159,-2.906174,3.676269,2.581290]],[[9.986298,-6.769478,-7.531967,8.656390,-0.929253,1.137751,8.498049,0.068669,8.753721,-0.171839,-7.288721,-4.999998,5.432113,-7.531596,8.750062],[8.668673,-8.867205,4.707411,5.270743,-0.429700,1.043719,-9.857086,-3.729862,-0.723754,-2.867515,6.866070,3.846532,-1.865148,-7.767010,0.583205],[-1.579655,-3.784635,-3.725925,2.181904,-5.666320,8.745970,-8.258715,-1.259664,4.655851,-4.915703,-3.321714,6.954763,9.131276,-3.137023,-4.181825],[4.905351,-3.495890,5.718407,-1.103958,8.736300,-7.138107,-3.156818,-7.462786,-3.055907,4.924487,0.998257,-0.959854,9.144789,-7.262474,0.126209],[8.676501,-5.310329,0.281507,-3.088285,-5.474034,-5.385677,-5.670014,7.830154,-1.832480,7.448314,-2.390736,6.626597,1.838814,-8.456221,-3.427432],[-7.261175,3.557729,3.588922,-6.897729,-3.774524,8.370111,-0.115077,2.945812,-7.394918,4.883171,1.907018,-6.338867,-6.472432,1.225298,-1.468252]],[[-2.972213,1.942798,7.995946,-5.425899,-6.291984,-7.689628,-9.973735,9.718114,9.563846,5.207018,4.594611,-2.173185,3.559198,2.353369,-9.256425],[-3.260185,-1.934131,-1.625990,-3.222191,-4.509680,3.105897,5.922251,3.402964,2.394984,-5.148094,0.770990,6.303372,-7.472907,-6.331930,0.090357],[7.966107,2.161554,8.661520,2.090128,1.740018,-4.511467,-1.408147,-0.429067,-1.058409,-3.980153,-5.936174,2.027141,-1.559147,-0.459285,8.047003],[9.633667,7.027737,6.083549,-5.595753,-7.330020,-9.718414,-6.063529,-5.651789,-5.982981,-2.067856,-7.914378,-5.972892,-4.215352,9.488183,5.783625],[-7.387347,9.115101,1.098524,-1.052909,9.205632,5.673228,2.711311,-9.282955,-1.912768,-0.340335,-3.532932,5.735040,-8.360131,1.255062,-5.332697],[0.881251,8.136694,-6.195932,7.182174,-5.113520,-5.549619,-5.816079,4.087018,6.588814,9.424713,-5.640850,-2.458635,-0.796525,6.929846,-6.498710]],[[-8.205050,-8.809946,-1.432588,-8.032419,0.313716,-4.711527,6.722744,8.505391,-6.363071,-1.615628,-4.312306,4.727120,2.962262,-9.058830,2.803887],[-1.574897,-0.427648,8.609246,-8.369087,-6.019447,-9.234678,1.848225,9.286773,-0.818685,3.504551,2.476639,5.790184,3.348336,-3.915757,3.318104],[-2.556655,0.981506,-3.822600,-8.580496,-9.292491,-6.584749,1.897077,-1.924853,-4.544866,-5.678082,-3.514889,8.130052,-8.084335,-1.494968,-5.803561],[-6.927355,8.237843,2.676802,-7.024093,-9.666516,-1.332492,9.340795,-3.069412,-8.476181,-8.237229,0.494376,-4.878094,-1.429527,0.460867,6.014927],[-5.792322,-3.604805,1.287005,1.139368,9.048490,3.410669,-6.086884,-0.290108,-2.633951,6.805493,8.132855,4.473248,-8.213509,0.565641,-7.873161],[4.266076,-7.220353,3.936935,-1.289956,-0.591016,-5.069524,1.145115,-1.250057,-3.125149,3.688163,-5.729921,-4.897311,-4.683041,4.609998,-3.531147]]], dtype = "float32")#candidate|2175|(6, 6, 15)|const|float32
bop_2176 = relay.subtract(var_2174.astype('float32'), relay.reshape(const_2175.astype('float32'), relay.shape_of(var_2174))) # shape=(6, 6, 15)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_2193 = relay.TupleGetItem(func_791_call(), 0)
call_2194 = relay.TupleGetItem(func_792_call(), 0)
func_2031_call = mod.get_global_var('func_2031')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_2199 = relay.TupleGetItem(func_2031_call(), 1)
call_2200 = relay.TupleGetItem(func_2032_call(), 1)
var_2205 = relay.var("var_2205", dtype = "float32", shape = (6, 6, 15))#candidate|2205|(6, 6, 15)|var|float32
bop_2206 = relay.not_equal(bop_2176.astype('bool'), relay.reshape(var_2205.astype('bool'), relay.shape_of(bop_2176))) # shape=(6, 6, 15)
output = relay.Tuple([call_2193,call_2199,bop_2206,])
output2 = relay.Tuple([call_2194,call_2200,bop_2206,])
func_2216 = relay.Function([var_2174,var_2205,], output)
mod['func_2216'] = func_2216
mod = relay.transform.InferType()(mod)
mutated_mod['func_2216'] = func_2216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2216_call = mutated_mod.get_global_var('func_2216')
var_2218 = relay.var("var_2218", dtype = "float32", shape = (6, 6, 15))#candidate|2218|(6, 6, 15)|var|float32
var_2219 = relay.var("var_2219", dtype = "float32", shape = (6, 6, 15))#candidate|2219|(6, 6, 15)|var|float32
call_2217 = func_2216_call(var_2218,var_2219,)
output = call_2217
func_2220 = relay.Function([var_2218,var_2219,], output)
mutated_mod['func_2220'] = func_2220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_2249 = relay.TupleGetItem(func_515_call(), 4)
call_2250 = relay.TupleGetItem(func_516_call(), 4)
output = call_2249
output2 = call_2250
func_2253 = relay.Function([], output)
mod['func_2253'] = func_2253
mod = relay.transform.InferType()(mod)
output = func_2253()
func_2254 = relay.Function([], output)
mutated_mod['func_2254'] = func_2254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1228_call = mod.get_global_var('func_1228')
func_1230_call = mutated_mod.get_global_var('func_1230')
call_2257 = relay.TupleGetItem(func_1228_call(), 1)
call_2258 = relay.TupleGetItem(func_1230_call(), 1)
output = call_2257
output2 = call_2258
func_2271 = relay.Function([], output)
mod['func_2271'] = func_2271
mod = relay.transform.InferType()(mod)
mutated_mod['func_2271'] = func_2271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mutated_mod.get_global_var('func_2271')
call_2272 = func_2271_call()
output = call_2272
func_2273 = relay.Function([], output)
mutated_mod['func_2273'] = func_2273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1435_call = mod.get_global_var('func_1435')
func_1437_call = mutated_mod.get_global_var('func_1437')
call_2287 = relay.TupleGetItem(func_1435_call(), 0)
call_2288 = relay.TupleGetItem(func_1437_call(), 0)
output = call_2287
output2 = call_2288
func_2292 = relay.Function([], output)
mod['func_2292'] = func_2292
mod = relay.transform.InferType()(mod)
output = func_2292()
func_2293 = relay.Function([], output)
mutated_mod['func_2293'] = func_2293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_627_call = mod.get_global_var('func_627')
func_629_call = mutated_mod.get_global_var('func_629')
call_2344 = relay.TupleGetItem(func_627_call(), 1)
call_2345 = relay.TupleGetItem(func_629_call(), 1)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_2346 = relay.TupleGetItem(func_515_call(), 2)
call_2347 = relay.TupleGetItem(func_516_call(), 2)
output = relay.Tuple([call_2344,call_2346,])
output2 = relay.Tuple([call_2345,call_2347,])
func_2356 = relay.Function([], output)
mod['func_2356'] = func_2356
mod = relay.transform.InferType()(mod)
mutated_mod['func_2356'] = func_2356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2356_call = mutated_mod.get_global_var('func_2356')
call_2357 = func_2356_call()
output = call_2357
func_2358 = relay.Function([], output)
mutated_mod['func_2358'] = func_2358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1100_call = mod.get_global_var('func_1100')
func_1101_call = mutated_mod.get_global_var('func_1101')
call_2361 = func_1100_call()
call_2362 = func_1100_call()
var_2376 = relay.var("var_2376", dtype = "float32", shape = (3, 8, 11))#candidate|2376|(3, 8, 11)|var|float32
bop_2377 = relay.not_equal(call_2361.astype('bool'), var_2376.astype('bool')) # shape=(3, 8, 11)
bop_2380 = relay.not_equal(call_2362.astype('bool'), var_2376.astype('bool')) # shape=(3, 8, 11)
func_2109_call = mod.get_global_var('func_2109')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_2386 = func_2109_call()
call_2387 = func_2109_call()
output = relay.Tuple([bop_2377,call_2386,])
output2 = relay.Tuple([bop_2380,call_2387,])
func_2389 = relay.Function([var_2376,], output)
mod['func_2389'] = func_2389
mod = relay.transform.InferType()(mod)
mutated_mod['func_2389'] = func_2389
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2390 = relay.var("var_2390", dtype = "float32", shape = (3, 8, 11))#candidate|2390|(3, 8, 11)|var|float32
func_2389_call = mutated_mod.get_global_var('func_2389')
call_2391 = func_2389_call(var_2390)
output = call_2391
func_2392 = relay.Function([var_2390], output)
mutated_mod['func_2392'] = func_2392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2123_call = mod.get_global_var('func_2123')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_2394 = relay.TupleGetItem(func_2123_call(), 0)
call_2395 = relay.TupleGetItem(func_2124_call(), 0)
output = relay.Tuple([call_2394,])
output2 = relay.Tuple([call_2395,])
func_2397 = relay.Function([], output)
mod['func_2397'] = func_2397
mod = relay.transform.InferType()(mod)
mutated_mod['func_2397'] = func_2397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2397_call = mutated_mod.get_global_var('func_2397')
call_2398 = func_2397_call()
output = call_2398
func_2399 = relay.Function([], output)
mutated_mod['func_2399'] = func_2399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_282_call = mod.get_global_var('func_282')
func_284_call = mutated_mod.get_global_var('func_284')
call_2443 = func_282_call()
call_2444 = func_282_call()
uop_2468 = relay.atan(call_2443.astype('float32')) # shape=(3, 8, 1)
uop_2470 = relay.atan(call_2444.astype('float32')) # shape=(3, 8, 1)
output = relay.Tuple([uop_2468,])
output2 = relay.Tuple([uop_2470,])
func_2471 = relay.Function([], output)
mod['func_2471'] = func_2471
mod = relay.transform.InferType()(mod)
mutated_mod['func_2471'] = func_2471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2471_call = mutated_mod.get_global_var('func_2471')
call_2472 = func_2471_call()
output = call_2472
func_2473 = relay.Function([], output)
mutated_mod['func_2473'] = func_2473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2109_call = mod.get_global_var('func_2109')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_2517 = func_2109_call()
call_2518 = func_2109_call()
func_1000_call = mod.get_global_var('func_1000')
func_1003_call = mutated_mod.get_global_var('func_1003')
const_2526 = relay.const([[True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,True,True,False,False,True],[False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,False],[True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True],[True,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False]], dtype = "bool")#candidate|2526|(4, 36)|const|bool
call_2525 = relay.TupleGetItem(func_1000_call(relay.reshape(const_2526.astype('bool'), [3, 8, 6])), 1)
call_2527 = relay.TupleGetItem(func_1003_call(relay.reshape(const_2526.astype('bool'), [3, 8, 6])), 1)
output = relay.Tuple([call_2517,call_2525,const_2526,])
output2 = relay.Tuple([call_2518,call_2527,const_2526,])
func_2532 = relay.Function([], output)
mod['func_2532'] = func_2532
mod = relay.transform.InferType()(mod)
mutated_mod['func_2532'] = func_2532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2532_call = mutated_mod.get_global_var('func_2532')
call_2533 = func_2532_call()
output = call_2533
func_2534 = relay.Function([], output)
mutated_mod['func_2534'] = func_2534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2397_call = mod.get_global_var('func_2397')
func_2399_call = mutated_mod.get_global_var('func_2399')
call_2566 = relay.TupleGetItem(func_2397_call(), 0)
call_2567 = relay.TupleGetItem(func_2399_call(), 0)
output = call_2566
output2 = call_2567
func_2574 = relay.Function([], output)
mod['func_2574'] = func_2574
mod = relay.transform.InferType()(mod)
mutated_mod['func_2574'] = func_2574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2574_call = mutated_mod.get_global_var('func_2574')
call_2575 = func_2574_call()
output = call_2575
func_2576 = relay.Function([], output)
mutated_mod['func_2576'] = func_2576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_820_call = mod.get_global_var('func_820')
func_821_call = mutated_mod.get_global_var('func_821')
call_2584 = relay.TupleGetItem(func_820_call(), 1)
call_2585 = relay.TupleGetItem(func_821_call(), 1)
var_2591 = relay.var("var_2591", dtype = "float32", shape = (3, 8, 5))#candidate|2591|(3, 8, 5)|var|float32
bop_2592 = relay.bitwise_xor(call_2584.astype('int64'), var_2591.astype('int64')) # shape=(3, 8, 5)
bop_2595 = relay.bitwise_xor(call_2585.astype('int64'), var_2591.astype('int64')) # shape=(3, 8, 5)
output = bop_2592
output2 = bop_2595
func_2600 = relay.Function([var_2591,], output)
mod['func_2600'] = func_2600
mod = relay.transform.InferType()(mod)
var_2601 = relay.var("var_2601", dtype = "float32", shape = (3, 8, 5))#candidate|2601|(3, 8, 5)|var|float32
output = func_2600(var_2601)
func_2602 = relay.Function([var_2601], output)
mutated_mod['func_2602'] = func_2602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2574_call = mod.get_global_var('func_2574')
func_2576_call = mutated_mod.get_global_var('func_2576')
call_2614 = func_2574_call()
call_2615 = func_2574_call()
output = relay.Tuple([call_2614,])
output2 = relay.Tuple([call_2615,])
func_2622 = relay.Function([], output)
mod['func_2622'] = func_2622
mod = relay.transform.InferType()(mod)
mutated_mod['func_2622'] = func_2622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2622_call = mutated_mod.get_global_var('func_2622')
call_2623 = func_2622_call()
output = call_2623
func_2624 = relay.Function([], output)
mutated_mod['func_2624'] = func_2624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_282_call = mod.get_global_var('func_282')
func_284_call = mutated_mod.get_global_var('func_284')
call_2640 = func_282_call()
call_2641 = func_282_call()
output = relay.Tuple([call_2640,])
output2 = relay.Tuple([call_2641,])
func_2652 = relay.Function([], output)
mod['func_2652'] = func_2652
mod = relay.transform.InferType()(mod)
mutated_mod['func_2652'] = func_2652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2652_call = mutated_mod.get_global_var('func_2652')
call_2653 = func_2652_call()
output = call_2653
func_2654 = relay.Function([], output)
mutated_mod['func_2654'] = func_2654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2253_call = mod.get_global_var('func_2253')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_2657 = func_2253_call()
call_2658 = func_2253_call()
func_1749_call = mod.get_global_var('func_1749')
func_1751_call = mutated_mod.get_global_var('func_1751')
call_2671 = relay.TupleGetItem(func_1749_call(), 1)
call_2672 = relay.TupleGetItem(func_1751_call(), 1)
func_1780_call = mod.get_global_var('func_1780')
func_1783_call = mutated_mod.get_global_var('func_1783')
const_2680 = relay.const([4.899281,-8.659385,3.381626,-6.939616,9.513843,-2.438133,4.401341,2.116809,-5.753437,7.737981,0.679083,-7.542044,3.451166,2.539599,-2.654703,-6.019110,1.651537,-0.304635,7.002550,1.556290,-8.791580,1.957187,1.152366,-0.372335,-0.094698,1.502283,4.161725,-7.107004,6.945701,6.343383,6.491402,5.854250,-4.949314,9.421457,-1.600681,-4.566752,0.618136,-3.879412,-2.357182,-1.064369,-5.892943,-5.010898,4.362225,-0.142190,-7.860366,-1.831697,-6.481094,-1.187756,6.285148,-5.778800,-0.927060,6.249160,-2.611874,3.337730,-8.115677,0.989118,9.153612,-3.307310,1.486998,3.026711,-8.423730,8.508741,6.290975,1.122286,7.824946,-0.326690,-7.388921,9.051400,8.809779,7.744496,-2.697300,-8.264038,-1.461573,-9.361626,-6.667629,8.302470,-4.327108,8.334744,-3.126794,-2.850911,-7.792327,-7.926456,-8.509242,2.400068,-9.718787,1.846671,4.676118,-9.635059,-6.575119,7.136377,4.521764,4.605573,4.372129,7.633792,5.434071,-1.067313,9.244255,-9.385019,-7.942340,2.363748,-3.586122,-3.648447,5.414256,8.082190,1.211370,-9.414131,7.720672,-6.736410,-6.999851,5.281962,-2.462166,8.684190,-8.163490,4.397552,8.471308,3.351763,-2.860559,6.617081,-5.456559,3.634404,-5.125898,-9.804105,-4.130271,-4.893376,6.536201,-5.447751,0.196336,9.529079,-1.853118,2.457208,5.560377,4.205925,-3.083135,4.232122,-7.741023,-1.363203,-3.914701,-2.678825,-9.311921,6.687831,-8.177014,4.745565,1.072563,5.529025,7.097973,1.039962,8.773829,-6.693737,-0.700829,8.460202,1.973430,8.360777,-6.105834,-1.306561,-3.195329,-1.870901,7.134423,3.628751,-7.059700,-5.198058,3.252709,3.439320,5.860008,-9.856337,4.584221,-8.580561,8.395944,1.819831,5.880655,-4.663659,2.581326,1.422431,-5.309476,-2.495569,2.393109,9.138404,-5.847430,-1.530156,-0.182710,7.324251,-5.367995,-7.349822,5.401741,8.625941,5.063073,1.638732,5.647269,-4.017535,2.170095,-0.024456,5.484569,7.328490,-8.747492,9.727841,-1.172828,4.519580,-8.501901,-8.060111,2.771757,7.280167,-0.981604,1.945702,1.081060,4.557758,-5.912740,3.059151,3.757683,-5.470571,-2.613020,1.505719,-5.374153,9.553468,-3.746967,6.368148,-5.604211,8.408661,6.110785,-9.344435,-5.087648,9.424213,3.509075,-9.943991,5.589096,6.085157,7.277212,-4.077075,4.942847,-7.232946,7.448080,0.332351,-7.236092,-4.123902,3.687380,-0.797560,3.994538,7.421476,8.499211,3.197359,-1.396864,-0.509316,7.364515,2.999154,4.138802,1.535582,6.193557,-4.877990,8.174486,0.154086,3.358693,-5.749380,0.435943,9.582305,7.400786,5.922512,8.944618,0.314027,-3.551192,0.317528,5.633023,1.488860,6.913834,-5.434338,-7.965270,-6.078330,-0.723592,-0.735943,-5.506081,-7.167333,4.125535,0.757316,0.638651,1.869502,9.230402,1.380920,5.184672,-4.584706,-5.761695,6.168407,-6.894905,-3.561295,-7.346022,0.548315,6.154701,1.148010,5.596837,0.635234,7.844087,8.902806,-9.138104,0.572455,9.038679,-9.442155,9.810172,-4.787523,8.654199,-4.374191,-3.274804,-4.825898,4.886705,-2.861600,-3.941490,8.881528,-3.957785,5.355303,-2.219175,5.974302,-4.930207,2.657078,9.644241,8.823307,0.005457,0.170336,9.493428,6.841766,8.127175,-8.579033,2.868253,8.851857,-7.730863,-3.001615,-6.440108,-5.748078,-8.788997,-2.609466,4.224632,-2.628318,1.961125,-6.160743,-4.646559,3.139735,0.607075,9.358020,7.068702,1.694056,5.187410,-0.960648,7.355736,-3.812105,4.654684,5.987546,4.992246,9.993240,0.628756,7.575864,8.456981,0.715604,-1.647276,0.943485,-5.318497,3.902597,7.471785,7.789264,-1.241368,-3.331090,-8.514962,5.930325,1.028287,-8.903547,-3.748443,-3.906608,-2.809696,1.123964,9.973291,-0.814652,9.158333,8.063087,-9.642598,3.212841,6.139818,-4.688548,9.652311,0.907981,-7.166496,-4.169770,5.704988,-6.044361,-4.416432,1.659761,-7.650952,3.505154,8.207409,-5.232246,6.690586,0.026280,5.296389,-4.931985,3.451739,-2.469277,8.796210,-6.543399,1.178824,-3.068911,-6.661188,3.607861,-0.875044,-3.594482,-0.422319,7.923474,-2.559537,-1.192454,-1.804859,4.540830,-9.313991,4.135849,-4.744397,-5.456049,-4.357068,9.398501,-2.332913,6.064715,-1.345199,1.416886,0.454565,-0.993845,2.803542,2.947672,-6.275209,6.795173,-3.838417,-4.539114,-6.888884,3.125850,-0.327392,-8.198825,6.312165,1.314346,5.176077,-1.393077,8.203415,9.811132,0.158975,-7.060351,8.619598,-8.781009,-7.971501,-4.683208,-0.581966,7.106555,-0.798447,3.568327,7.312127,1.096276,5.457714,1.931476,7.123825,3.116845,-4.891527,-6.404381,6.684343,5.096815,4.497859,8.497632,4.324425,-7.029634,-5.577189,-8.551209,-6.651940,-9.196501,7.634232,-9.885772,-3.386811,-9.462167,4.681145,-2.297335,7.376043,-4.270218,9.282336,-9.870516,-1.758086,7.506326,4.918755,8.284224,7.500113,7.318855,9.967694,0.237551,-2.397491,-0.267421,-6.666889,-2.028782,5.376621,0.552533,-0.966974,5.388203,-9.627598,6.591170,-4.754649,-9.467413,1.129788,3.655567,8.564031,-6.624277,-9.571821,-1.988543,-8.423353,-2.277399,4.413943,-4.846854,-7.300673,1.883110,-0.338426,-8.152429,0.593086,4.763897,-4.441102,0.180205,4.818773,6.249177,6.206734,8.181428,5.806081,8.723721,3.853341,-4.876136,8.185075,-0.005838,8.261759,9.070848,8.457789,2.725394,7.857882,-3.809734,-4.399166,-2.354792,5.502048,9.746583,5.519252,0.817828,2.663827,-3.234120,9.701081,-4.117401,0.331856,9.930466,-2.420475,6.474325,-7.230279,2.147585,5.295557,-5.294988,7.602019,9.887786,-4.307724,1.569583,5.837457,-8.740884,-9.411845,7.696929,-2.352791,6.765696,1.178668,-3.577761,-2.894526,-1.226056,3.379869,-3.081158,6.322672,-5.642395,-6.792048,0.627658,0.409141,2.807959,-9.467252,-2.568158,2.009272,-7.048736,-3.238250,-3.014556,-2.333998,-9.816347,0.594775,-4.038993,3.653492,-0.353585,-9.630295,5.204547,-0.248425,2.539986,6.811034,7.120497,1.713526,3.055437,5.570511,-1.815967,-9.064082,8.800879,8.513603,-6.858708,-2.935988,7.174481,-8.221418,8.809299,8.903355,-1.380658,-6.157547,2.332957,8.400943,0.324455,4.695113,-9.945899,-5.816686,9.763087,0.340386,-2.287411,0.377993,-7.061457,-8.802137,-3.034469,-1.135684,-7.382093,-1.876247,5.697313,-5.166293,-0.055015,-9.718584,-8.755597,9.834353,5.157882,9.102977,-8.675254,1.873338,6.954214,-7.999930,6.717835,-9.303654,2.390329,7.559974,-7.931055,0.834353,6.726336,9.185592,0.770689,-0.025712,6.821228,-4.913255,-2.033923,-8.880112,-9.660605,0.341103,1.003251,7.493887,-2.362072,3.135856,8.624003,-8.765160,1.057702,-1.025528,-4.954413,1.093085,-7.656264,3.376776,4.610895,-3.889997,6.755414,9.524567,7.543689,2.483396,3.238775,-1.066751,-9.784255,-6.902781,-8.300613,-7.321262,2.112859,-0.571525,2.794260,-0.954284,2.970928,-4.705817,-4.393199,-4.840742,7.305613,7.558596,-6.938968,4.080830,-5.256583,-4.120509,-5.007169,7.466851,-5.083254,3.966418,-8.094160,-9.134815,2.487137,-4.163990,-3.179200,9.235689,-1.523109,7.739317,2.346466,9.912111,-6.550164,-4.444830,-6.482690,-9.575983,-1.215859,4.685773,5.872280,-1.552711,-1.669795,-0.709266,0.879031,-2.637475,-5.932746,1.918468,-8.199854,-0.105389,-7.337991,5.324215,-8.968792,-6.539585,-0.320814,6.389030,8.638146,-3.769863,-3.983025,3.124140,-0.711878,-0.675513,0.370002,-4.586111,-9.754624,-4.685841,-7.790831,-7.614760,9.628089,3.700129,-0.197277,9.971532,-0.812828,8.093053,-8.702849,7.930414,7.049662,5.261798,0.481584,-9.166915,-2.934139,-7.646143,1.409676,-8.722106,0.861014,-7.619348,-8.461124,-0.364229,9.878712,-4.713182,-5.773343,-8.221253,0.941618,-9.758695,-6.210739,-3.801753,9.709934,2.698660,4.122497,5.685776,8.486611,-4.413359,5.821730,-2.072268,5.381662,-2.741800,-4.042354,1.983072,-0.347670,-4.702018,-9.180410,-7.824254,-6.037314,-4.028577,1.324189,-6.591523,5.874345,-6.466130,7.946505,4.410662,8.476770,-3.453022,5.781932,5.395419,9.032800,-3.622691,7.828958,2.751487,-2.943439,5.378208,1.862912,-2.814551,2.755892,8.161826,7.926189,6.982735,-0.944840,0.622865,0.635438,-1.734867,-3.072680,-4.574058,6.370964,1.392622,-7.516710,1.747862,1.938371,-1.640186,-3.211296,1.362059,9.238996,7.416312,4.914828,7.051828,8.253793,4.478402,-0.270527,5.917736,-3.175187,3.450104,-8.974904,-4.174770,-3.727261,-4.445045,1.099680,-6.939851,-7.486786,-8.006508,-0.718159,-1.656151,6.871101,-5.656137,7.669308,7.375350,-3.856909,-8.093598,6.020058,-9.578845,-2.148853,4.665117,5.472237,-4.702685,1.086683,3.537351,-7.346071,5.734770,9.430273,6.478478,-8.254508,-1.930085,6.123694,4.192724,-8.759694,-6.003039,-6.083951,-4.213181,9.851947,3.082816,7.171494,8.708370,-0.150537,-3.416115,-6.198813,-8.814836,-4.325457,2.841745,-5.638130,9.772806,1.869042,0.147349,0.511694,8.311334,-0.934416,7.563830,4.851180,4.085437,2.828332,9.968239,0.571029,-9.455990,9.186686,4.640871,-9.343020,-5.336509,-7.196887,3.639008,4.986550,-5.329556,8.716530,9.376709,-0.489262,-1.826409,-5.285922,9.308514,-1.180162,-5.787282,-1.442116,9.496917,-9.304124,-3.883992,5.825662,-4.443077,-2.002611,-7.942520,-5.784493,-3.689546,-7.732544,-2.273965,-2.425839,-2.324036,-6.595980,-0.924023,-6.956316,8.808112,9.326936,3.271764,-6.243005,0.375906,-9.032916,-4.447818,-9.201606,-3.961469,-6.729973,7.390782,-7.639868,4.843848,-3.722473,0.921697,7.994765,5.801144,-1.370792,4.741116,-7.140168,9.941794,-0.755086,4.458675,-9.698391,2.390034,4.150023,-5.813181,-8.453362,-3.117151,3.787389,9.347775,-3.041330,-5.126133,6.844541,0.638773,-5.244388,-3.328586,6.133374,9.391773,6.609736,-9.108604,-2.865401,3.598216,-1.514957,5.651093,3.014710,-1.659369,-5.168046,7.314556,-3.619323,1.452856,7.016146,5.265642,-5.215442,1.464362,5.650760,-7.877807,-6.524758,-0.094462,3.696089,-0.319257,-7.997706,-2.177364,2.854842,-5.369294,0.680236,7.408083,1.539790,1.604142,0.010793,-9.803737,-5.070474,-2.738002,-8.270246,1.091820,9.674152,-4.666038,-1.795760,-4.763129,-2.983676,8.651757,-2.164663,8.854598,1.970603,4.468281,7.412784,5.829259,-5.516520,-8.743883,-7.767195,-2.684293,2.588701,5.074507,-7.927473,-1.264432,-3.359827,-3.172859,-3.987208,-3.002833,-1.240512,-2.956526,0.504549,0.585649,-9.072710,-2.591607,6.376706,-8.805173,-2.925643,-3.260928,9.480822,0.650283,-6.647572,-7.873832,0.668726,-9.590035,4.812503,4.566434,-9.146957,-4.288646,-8.729653,8.226520,-3.799083,6.142343,6.593657,7.430579,-9.774707,-2.846692,-4.189154,4.708770,8.761901,6.894390,-3.274477,-3.497810,7.497404,9.311706,9.036628,3.845898,-4.386563,-5.030814,-6.689500,-6.234613,3.107188,7.940107,-3.621635,1.784796,-3.918496,-1.851112,-5.133878,2.168233,4.069117,7.342162,7.557231,-3.930617,0.678292,1.838832,-6.736901,-0.148199,-0.394095,9.254719,-8.927679,-4.711835,6.269699,-9.838351,3.116499,4.527645,-9.484785,-8.713778,7.261190,-5.097821,5.573867,-8.371440,9.480065,8.929200,-7.477441,-7.255803,-5.906535,6.311562,6.506732,1.151699,3.643146,-7.363448,1.793000,0.767770,8.571868,-3.425565,1.740659,9.064255,9.285225,-7.761165,7.612366,3.768792,-7.721940,-1.028657,-8.167054,-8.680495,-6.503439,9.624200,6.792988,3.015898,-4.687486,-9.399307,-8.683767,4.931719,-6.415522,-4.388026,-4.228951,9.628073,-1.813572,6.398179,7.786393,7.744177,-4.353440,-9.025269,5.309087,-0.498036,4.700744,-7.060138,-0.438095,2.262805,1.321217,7.206452,2.706177,-9.323260,-3.321527,-8.060893,-3.705544,1.496918,8.402801,-9.804385,5.441724,-5.998831,6.061142,4.681517,-4.253680,1.653994,-5.351202,-3.270049,4.363657,1.068611,-9.547568,-2.941730,5.768820,1.942717,2.410797,-8.257019,-0.547376,5.707205,3.194870,-9.118424,4.868498,8.024913,-7.818684,-6.974384,5.544231,5.223186,1.026397,-4.381225,8.162536,5.256854,9.523594,-7.869239,9.782095,-7.994173,-4.083417,-2.497443,-3.121351,8.044690,8.178588,-5.042917,5.964461,-9.074506,8.585670,-7.765703,-4.966899,8.966480,2.234494,-5.967452,2.111663,0.728296,5.784947,-9.614351,0.692466,-5.593393,8.055055,1.905487,-7.048776,3.788674,-8.284196,-7.536661,-2.637060,5.223073,0.589455,-3.070873,-4.915909,-0.528209,5.791991,7.005999,-4.048832,-0.329598,-1.907660,8.172183,0.259340,4.274971,-7.111661,5.901458,2.499259,-0.522626,-5.457414,-5.592832,-7.906872,-6.651429,1.547532,-7.608777,8.221007,2.192686,0.131356,-4.686513,6.665482,-1.939567,4.209993,-4.259268,-4.238209,-8.810318,2.433643,8.016795,6.153497,-9.605840,5.011167,0.770691,8.558271,7.384636,0.012916,7.405701,4.838263,-5.118376,3.998893,7.694463,6.266561,-1.384285,-8.540741,-4.543026,7.997945,-7.852320,6.812530,5.542953,-6.384871,0.282204,-6.333685,4.764438,9.150332,5.599728,-9.734138,-2.350121,-4.105364,7.589447,2.522406,-5.698610,-9.431990,7.592513,-4.583692,-3.853834,4.598461,-6.226699,-2.248242,0.662410,1.362690,3.415946,-3.738180,6.617526,-8.964419,9.224458,-2.315048,8.689044,3.523610,8.088327,4.804697,-3.371574,4.942551,6.219206,-0.224577,5.348429,5.713129,-1.916604,2.912162,-6.805040,-6.524818,8.792505,9.215595,8.171629,6.497467,4.045208,-5.968508,-8.141812,-6.941766,8.674301,-0.649890,6.823460,2.893562,3.133075,0.536791,4.451485,-1.609904,2.238292,3.600160,-6.308151,4.230029,1.882053,9.563830,6.686227,1.493875,1.641379,-8.179941,1.950112,-4.321166,-7.248906,-4.936178,5.551190,-6.034957,5.151354,7.671445,-4.340306,4.689799,-1.275739,3.166592,-5.455353,-0.034350,4.055692,-8.985272,0.811528,5.602894,7.592931,8.360493,-4.892189,0.578909,6.234038,9.935320,2.535483,7.837803,-5.674762,3.279980,-8.873889,-8.800808,-2.508610,-4.848333,7.824543,6.160147,-6.043166,4.289625,-5.871344,-6.999677,8.416417,-1.126187,-6.385880,-7.616394,-9.174481,6.203927,3.312723,-3.185327,5.804656,5.353068,0.896740,2.327274,3.247048,-9.026096,1.392074,7.047380,4.223081,4.643978,-9.536799,-5.852844,8.175436,5.248658,5.764151,5.307017,-7.177848,6.317277,7.777733,8.778013,0.846344,1.480165,-8.836306,4.652501,-2.777504,8.048933,-6.762681,5.732828,-3.374029,-7.740822,5.841506,-9.769614,3.769983,8.397888,-7.248809,4.226699,-8.600773,-6.167610,-4.740759,-5.935262,-4.814951,1.732911,2.581863,-5.353662,6.285341,8.332828,-8.650237,-0.808194,2.219392,1.452942,8.348982,4.876955,5.291447,-5.747934,1.062107,-6.148187,8.123705,-1.472591,-9.731632,-9.304044,-1.359565,-4.193677,9.586024,-3.199889,-4.562603,-6.683468,-7.649238,-1.945628,9.883272,0.564025,1.342872,-3.501202,6.340923,-1.113161,2.171237,3.209773,-1.878921,0.159796,7.701926,5.894997,8.417670,9.967617,7.611765,6.940601,-3.183977,-0.807151,-2.353336,-5.510458,5.570501,7.798076,4.388711,-0.202586,0.053821,7.820331,0.157693,-3.615064,-2.001518,4.854623,5.233385,-1.304550,9.747830,-0.426611,5.822227,-4.845703,8.209639,-6.338943,-8.600344,-4.559630,-9.056056,-5.149853,-9.846886,-0.279932,-6.312871,4.653616,-7.438268,-0.868260,-4.915185,0.063174,5.763489,-7.499221,9.233913,-3.714954,-0.268667,6.954664,-2.567057,-0.212004,4.195057,-5.973514,-3.455711,2.582634,6.502308,7.520137,-4.259941,-0.005432,-9.131813,-5.863748,5.098210,1.785826,-9.357441,-7.148447,4.926340,5.785645,4.471674,-5.136631,9.830981,-2.036368,4.091820,-9.771555,-0.155074,-2.252459,-9.900067,-6.629467,1.726725,6.769447,1.739232,-2.522558,-3.844243,0.848391,6.474237,-9.891627,4.056404,-6.244292,-7.914966,3.368282,0.465833,3.408119,-1.277292,5.625626,6.759289,2.310577,-3.258555,4.602542,-0.366190,-4.767614,2.559956,-6.813523,1.282669,2.822139,-8.371014,-6.795555,-2.842207,6.420476,5.815902,-3.244619,7.375449,7.259491,-1.109729,-4.967726,3.987459,-6.947829,1.021627,-3.410038,1.975763,-8.324364,-8.878472,0.672119,-2.370739,4.342871,0.667107,3.311385,-7.340285,-2.907190,6.488244,9.513623,7.326313,6.042707,-5.296532,3.307702,-2.629687,5.888800,-4.464604,3.377360,0.015859,6.218790,0.630810,5.808827,7.041763,-2.799918,6.310278,-7.813326,3.668924,2.036592,1.483518,-8.347032,4.329631,-0.594498,-5.908308,-8.555497,-9.662551,0.066459,-1.274436,4.314904,-5.295639,1.283848,1.700082,8.679963,9.336716,4.762699,7.097788,-6.847545,9.739585,1.945666,7.675186,-1.324862,2.325684,0.850863,-9.093085,7.771569,-4.919372,-8.780948,-4.488933,-7.562103,5.448255,-6.419056,8.338999,3.580401,6.137308,9.745027,-0.388989,4.942066,7.564111,-2.489333,5.288867,-1.016769,-8.836635,-5.321481,-0.546408,-3.345257,-6.690480,8.486845], dtype = "float64")#candidate|2680|(1638,)|const|float64
call_2679 = func_1780_call(relay.reshape(const_2680.astype('float64'), [13, 9, 14]))
call_2681 = func_1780_call(relay.reshape(const_2680.astype('float64'), [13, 9, 14]))
func_1872_call = mod.get_global_var('func_1872')
func_1875_call = mutated_mod.get_global_var('func_1875')
var_2683 = relay.var("var_2683", dtype = "int32", shape = (224,))#candidate|2683|(224,)|var|int32
call_2682 = relay.TupleGetItem(func_1872_call(relay.reshape(var_2683.astype('int32'), [4, 8, 7]), relay.reshape(call_2671.astype('float32'), [384,]), ), 0)
call_2684 = relay.TupleGetItem(func_1875_call(relay.reshape(var_2683.astype('int32'), [4, 8, 7]), relay.reshape(call_2671.astype('float32'), [384,]), ), 0)
uop_2688 = relay.exp(const_2680.astype('float64')) # shape=(1638,)
func_909_call = mod.get_global_var('func_909')
func_911_call = mutated_mod.get_global_var('func_911')
const_2691 = relay.const([True,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,False,True,True], dtype = "bool")#candidate|2691|(144,)|const|bool
call_2690 = func_909_call(relay.reshape(const_2691.astype('bool'), [3, 8, 6]))
call_2692 = func_909_call(relay.reshape(const_2691.astype('bool'), [3, 8, 6]))
output = relay.Tuple([call_2657,call_2671,call_2679,call_2682,var_2683,uop_2688,call_2690,const_2691,])
output2 = relay.Tuple([call_2658,call_2672,call_2681,call_2684,var_2683,uop_2688,call_2692,const_2691,])
func_2711 = relay.Function([var_2683,], output)
mod['func_2711'] = func_2711
mod = relay.transform.InferType()(mod)
mutated_mod['func_2711'] = func_2711
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2712 = relay.var("var_2712", dtype = "int32", shape = (224,))#candidate|2712|(224,)|var|int32
func_2711_call = mutated_mod.get_global_var('func_2711')
call_2713 = func_2711_call(var_2712)
output = call_2713
func_2714 = relay.Function([var_2712], output)
mutated_mod['func_2714'] = func_2714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2397_call = mod.get_global_var('func_2397')
func_2399_call = mutated_mod.get_global_var('func_2399')
call_2742 = relay.TupleGetItem(func_2397_call(), 0)
call_2743 = relay.TupleGetItem(func_2399_call(), 0)
var_2758 = relay.var("var_2758", dtype = "bool", shape = (3, 8, 4))#candidate|2758|(3, 8, 4)|var|bool
bop_2759 = relay.mod(call_2742.astype('float32'), var_2758.astype('float32')) # shape=(3, 8, 4)
bop_2762 = relay.mod(call_2743.astype('float32'), var_2758.astype('float32')) # shape=(3, 8, 4)
bop_2770 = relay.greater(var_2758.astype('bool'), call_2742.astype('bool')) # shape=(3, 8, 4)
bop_2773 = relay.greater(var_2758.astype('bool'), call_2743.astype('bool')) # shape=(3, 8, 4)
output = relay.Tuple([bop_2759,bop_2770,])
output2 = relay.Tuple([bop_2762,bop_2773,])
func_2794 = relay.Function([var_2758,], output)
mod['func_2794'] = func_2794
mod = relay.transform.InferType()(mod)
mutated_mod['func_2794'] = func_2794
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2795 = relay.var("var_2795", dtype = "bool", shape = (3, 8, 4))#candidate|2795|(3, 8, 4)|var|bool
func_2794_call = mutated_mod.get_global_var('func_2794')
call_2796 = func_2794_call(var_2795)
output = call_2796
func_2797 = relay.Function([var_2795], output)
mutated_mod['func_2797'] = func_2797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_2804 = relay.TupleGetItem(func_2356_call(), 1)
call_2805 = relay.TupleGetItem(func_2358_call(), 1)
func_820_call = mod.get_global_var('func_820')
func_821_call = mutated_mod.get_global_var('func_821')
call_2807 = relay.TupleGetItem(func_820_call(), 0)
call_2808 = relay.TupleGetItem(func_821_call(), 0)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_2810 = func_2271_call()
call_2811 = func_2271_call()
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_2820 = relay.TupleGetItem(func_1940_call(), 0)
call_2821 = relay.TupleGetItem(func_1941_call(), 0)
output = relay.Tuple([call_2804,call_2807,call_2810,call_2820,])
output2 = relay.Tuple([call_2805,call_2808,call_2811,call_2821,])
func_2828 = relay.Function([], output)
mod['func_2828'] = func_2828
mod = relay.transform.InferType()(mod)
output = func_2828()
func_2829 = relay.Function([], output)
mutated_mod['func_2829'] = func_2829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_2866 = relay.TupleGetItem(func_1940_call(), 1)
call_2867 = relay.TupleGetItem(func_1941_call(), 1)
output = call_2866
output2 = call_2867
func_2873 = relay.Function([], output)
mod['func_2873'] = func_2873
mod = relay.transform.InferType()(mod)
mutated_mod['func_2873'] = func_2873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2873_call = mutated_mod.get_global_var('func_2873')
call_2874 = func_2873_call()
output = call_2874
func_2875 = relay.Function([], output)
mutated_mod['func_2875'] = func_2875
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2889 = relay.var("var_2889", dtype = "float64", shape = (15, 1, 13))#candidate|2889|(15, 1, 13)|var|float64
var_2890 = relay.var("var_2890", dtype = "float64", shape = (15, 3, 13))#candidate|2890|(15, 3, 13)|var|float64
bop_2891 = relay.floor_mod(var_2889.astype('float64'), var_2890.astype('float64')) # shape=(15, 3, 13)
bop_2895 = relay.add(var_2889.astype('float64'), bop_2891.astype('float64')) # shape=(15, 3, 13)
func_2873_call = mod.get_global_var('func_2873')
func_2875_call = mutated_mod.get_global_var('func_2875')
call_2902 = func_2873_call()
call_2903 = func_2873_call()
func_1000_call = mod.get_global_var('func_1000')
func_1003_call = mutated_mod.get_global_var('func_1003')
const_2917 = relay.const([False,False,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False], dtype = "bool")#candidate|2917|(144,)|const|bool
call_2916 = relay.TupleGetItem(func_1000_call(relay.reshape(const_2917.astype('bool'), [3, 8, 6])), 1)
call_2918 = relay.TupleGetItem(func_1003_call(relay.reshape(const_2917.astype('bool'), [3, 8, 6])), 1)
output = relay.Tuple([bop_2895,call_2902,call_2916,const_2917,])
output2 = relay.Tuple([bop_2895,call_2903,call_2918,const_2917,])
func_2919 = relay.Function([var_2889,var_2890,], output)
mod['func_2919'] = func_2919
mod = relay.transform.InferType()(mod)
mutated_mod['func_2919'] = func_2919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2919_call = mutated_mod.get_global_var('func_2919')
var_2921 = relay.var("var_2921", dtype = "float64", shape = (15, 1, 13))#candidate|2921|(15, 1, 13)|var|float64
var_2922 = relay.var("var_2922", dtype = "float64", shape = (15, 3, 13))#candidate|2922|(15, 3, 13)|var|float64
call_2920 = func_2919_call(var_2921,var_2922,)
output = call_2920
func_2923 = relay.Function([var_2921,var_2922,], output)
mutated_mod['func_2923'] = func_2923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2292_call = mod.get_global_var('func_2292')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_2990 = func_2292_call()
call_2991 = func_2292_call()
const_2996 = relay.const([[[True,False,True,True,True,False,True,True,True],[False,True,False,False,False,False,False,False,True],[False,True,True,False,False,True,False,True,False],[False,False,False,False,True,True,True,True,False],[False,False,True,True,True,False,True,True,False],[False,True,False,True,True,False,False,True,False],[True,True,False,True,True,False,False,False,False],[True,True,True,True,True,True,True,True,False]],[[True,False,True,False,False,False,False,False,True],[False,False,False,True,False,True,True,True,True],[True,True,True,True,False,False,False,False,False],[False,True,True,False,False,True,False,False,False],[False,True,False,False,True,False,False,False,False],[False,True,False,True,True,True,False,False,False],[False,True,False,False,True,True,True,True,True],[True,True,False,True,False,True,True,False,False]],[[True,False,True,False,False,False,False,True,True],[True,True,False,True,False,True,True,False,False],[False,False,True,False,True,True,False,False,True],[True,True,True,True,False,True,False,False,False],[True,False,True,False,False,True,False,True,True],[True,True,True,True,True,True,True,True,False],[False,True,False,True,False,True,False,False,False],[True,False,False,True,True,True,True,False,True]]], dtype = "bool")#candidate|2996|(3, 8, 9)|const|bool
bop_2997 = relay.bitwise_and(call_2990.astype('uint32'), const_2996.astype('uint32')) # shape=(3, 8, 9)
bop_3000 = relay.bitwise_and(call_2991.astype('uint32'), const_2996.astype('uint32')) # shape=(3, 8, 9)
output = relay.Tuple([bop_2997,])
output2 = relay.Tuple([bop_3000,])
func_3005 = relay.Function([], output)
mod['func_3005'] = func_3005
mod = relay.transform.InferType()(mod)
mutated_mod['func_3005'] = func_3005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3005_call = mutated_mod.get_global_var('func_3005')
call_3006 = func_3005_call()
output = call_3006
func_3007 = relay.Function([], output)
mutated_mod['func_3007'] = func_3007
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3008 = relay.const([[[0.948942],[-3.653182],[-6.693658]],[[-9.523330],[-9.381174],[-7.184238]],[[-7.393988],[-5.366806],[-6.244020]],[[3.571510],[-5.111804],[-5.057539]],[[3.249784],[8.096559],[4.695038]],[[4.320452],[-2.115037],[1.633915]],[[4.232012],[9.484649],[3.764831]]], dtype = "float64")#candidate|3008|(7, 3, 1)|const|float64
uop_3009 = relay.cosh(const_3008.astype('float64')) # shape=(7, 3, 1)
func_2652_call = mod.get_global_var('func_2652')
func_2654_call = mutated_mod.get_global_var('func_2654')
call_3015 = relay.TupleGetItem(func_2652_call(), 0)
call_3016 = relay.TupleGetItem(func_2654_call(), 0)
output = relay.Tuple([uop_3009,call_3015,])
output2 = relay.Tuple([uop_3009,call_3016,])
func_3017 = relay.Function([], output)
mod['func_3017'] = func_3017
mod = relay.transform.InferType()(mod)
mutated_mod['func_3017'] = func_3017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3017_call = mutated_mod.get_global_var('func_3017')
call_3018 = func_3017_call()
output = call_3018
func_3019 = relay.Function([], output)
mutated_mod['func_3019'] = func_3019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2622_call = mod.get_global_var('func_2622')
func_2624_call = mutated_mod.get_global_var('func_2624')
call_3155 = relay.TupleGetItem(func_2622_call(), 0)
call_3156 = relay.TupleGetItem(func_2624_call(), 0)
output = call_3155
output2 = call_3156
func_3164 = relay.Function([], output)
mod['func_3164'] = func_3164
mod = relay.transform.InferType()(mod)
output = func_3164()
func_3165 = relay.Function([], output)
mutated_mod['func_3165'] = func_3165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2652_call = mod.get_global_var('func_2652')
func_2654_call = mutated_mod.get_global_var('func_2654')
call_3175 = relay.TupleGetItem(func_2652_call(), 0)
call_3176 = relay.TupleGetItem(func_2654_call(), 0)
output = call_3175
output2 = call_3176
func_3183 = relay.Function([], output)
mod['func_3183'] = func_3183
mod = relay.transform.InferType()(mod)
mutated_mod['func_3183'] = func_3183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mutated_mod.get_global_var('func_3183')
call_3184 = func_3183_call()
output = call_3184
func_3185 = relay.Function([], output)
mutated_mod['func_3185'] = func_3185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_3225 = func_2271_call()
call_3226 = func_2271_call()
output = call_3225
output2 = call_3226
func_3234 = relay.Function([], output)
mod['func_3234'] = func_3234
mod = relay.transform.InferType()(mod)
output = func_3234()
func_3235 = relay.Function([], output)
mutated_mod['func_3235'] = func_3235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2253_call = mod.get_global_var('func_2253')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_3240 = func_2253_call()
call_3241 = func_2253_call()
uop_3242 = relay.acosh(call_3240.astype('float32')) # shape=(3, 8, 1)
uop_3244 = relay.acosh(call_3241.astype('float32')) # shape=(3, 8, 1)
func_282_call = mod.get_global_var('func_282')
func_284_call = mutated_mod.get_global_var('func_284')
call_3246 = func_282_call()
call_3247 = func_282_call()
uop_3248 = relay.sigmoid(uop_3242.astype('float32')) # shape=(3, 8, 1)
uop_3250 = relay.sigmoid(uop_3244.astype('float32')) # shape=(3, 8, 1)
bop_3252 = relay.floor_mod(uop_3248.astype('float32'), relay.reshape(call_3240.astype('float32'), relay.shape_of(uop_3248))) # shape=(3, 8, 1)
bop_3255 = relay.floor_mod(uop_3250.astype('float32'), relay.reshape(call_3241.astype('float32'), relay.shape_of(uop_3250))) # shape=(3, 8, 1)
func_2031_call = mod.get_global_var('func_2031')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_3257 = relay.TupleGetItem(func_2031_call(), 0)
call_3258 = relay.TupleGetItem(func_2032_call(), 0)
uop_3259 = relay.tan(bop_3252.astype('float32')) # shape=(3, 8, 1)
uop_3261 = relay.tan(bop_3255.astype('float32')) # shape=(3, 8, 1)
func_2711_call = mod.get_global_var('func_2711')
func_2714_call = mutated_mod.get_global_var('func_2714')
var_3266 = relay.var("var_3266", dtype = "int32", shape = (224,))#candidate|3266|(224,)|var|int32
call_3265 = relay.TupleGetItem(func_2711_call(relay.reshape(var_3266.astype('int32'), [224,])), 3)
call_3267 = relay.TupleGetItem(func_2714_call(relay.reshape(var_3266.astype('int32'), [224,])), 3)
output = relay.Tuple([call_3246,call_3257,uop_3259,call_3265,var_3266,])
output2 = relay.Tuple([call_3247,call_3258,uop_3261,call_3267,var_3266,])
func_3285 = relay.Function([var_3266,], output)
mod['func_3285'] = func_3285
mod = relay.transform.InferType()(mod)
mutated_mod['func_3285'] = func_3285
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3286 = relay.var("var_3286", dtype = "int32", shape = (224,))#candidate|3286|(224,)|var|int32
func_3285_call = mutated_mod.get_global_var('func_3285')
call_3287 = func_3285_call(var_3286)
output = call_3287
func_3288 = relay.Function([var_3286], output)
mutated_mod['func_3288'] = func_3288
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3325 = relay.var("var_3325", dtype = "uint64", shape = (10, 15, 16))#candidate|3325|(10, 15, 16)|var|uint64
var_3326 = relay.var("var_3326", dtype = "uint64", shape = (10, 15, 16))#candidate|3326|(10, 15, 16)|var|uint64
bop_3327 = relay.right_shift(var_3325.astype('uint64'), relay.reshape(var_3326.astype('uint64'), relay.shape_of(var_3325))) # shape=(10, 15, 16)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_3338 = relay.TupleGetItem(func_354_call(), 1)
call_3339 = relay.TupleGetItem(func_356_call(), 1)
output = relay.Tuple([bop_3327,call_3338,])
output2 = relay.Tuple([bop_3327,call_3339,])
func_3342 = relay.Function([var_3325,var_3326,], output)
mod['func_3342'] = func_3342
mod = relay.transform.InferType()(mod)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3342_call = mutated_mod.get_global_var('func_3342')
var_3344 = relay.var("var_3344", dtype = "uint64", shape = (10, 15, 16))#candidate|3344|(10, 15, 16)|var|uint64
var_3345 = relay.var("var_3345", dtype = "uint64", shape = (10, 15, 16))#candidate|3345|(10, 15, 16)|var|uint64
call_3343 = func_3342_call(var_3344,var_3345,)
output = call_3343
func_3346 = relay.Function([var_3344,var_3345,], output)
mutated_mod['func_3346'] = func_3346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_3418 = relay.TupleGetItem(func_354_call(), 0)
call_3419 = relay.TupleGetItem(func_356_call(), 0)
var_3438 = relay.var("var_3438", dtype = "float32", shape = (3, 8, 16))#candidate|3438|(3, 8, 16)|var|float32
bop_3439 = relay.equal(call_3418.astype('bool'), var_3438.astype('bool')) # shape=(3, 8, 16)
bop_3442 = relay.equal(call_3419.astype('bool'), var_3438.astype('bool')) # shape=(3, 8, 16)
uop_3452 = relay.sqrt(var_3438.astype('float32')) # shape=(3, 8, 16)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_3460 = relay.TupleGetItem(func_1823_call(), 1)
call_3461 = relay.TupleGetItem(func_1825_call(), 1)
func_2109_call = mod.get_global_var('func_2109')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_3464 = func_2109_call()
call_3465 = func_2109_call()
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_3481 = relay.TupleGetItem(func_1823_call(), 1)
call_3482 = relay.TupleGetItem(func_1825_call(), 1)
output = relay.Tuple([bop_3439,uop_3452,call_3460,call_3464,call_3481,])
output2 = relay.Tuple([bop_3442,uop_3452,call_3461,call_3465,call_3482,])
func_3485 = relay.Function([var_3438,], output)
mod['func_3485'] = func_3485
mod = relay.transform.InferType()(mod)
var_3486 = relay.var("var_3486", dtype = "float32", shape = (3, 8, 16))#candidate|3486|(3, 8, 16)|var|float32
output = func_3485(var_3486)
func_3487 = relay.Function([var_3486], output)
mutated_mod['func_3487'] = func_3487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_3510 = func_2271_call()
call_3511 = func_2271_call()
output = call_3510
output2 = call_3511
func_3519 = relay.Function([], output)
mod['func_3519'] = func_3519
mod = relay.transform.InferType()(mod)
mutated_mod['func_3519'] = func_3519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3519_call = mutated_mod.get_global_var('func_3519')
call_3520 = func_3519_call()
output = call_3520
func_3521 = relay.Function([], output)
mutated_mod['func_3521'] = func_3521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3005_call = mod.get_global_var('func_3005')
func_3007_call = mutated_mod.get_global_var('func_3007')
call_3571 = relay.TupleGetItem(func_3005_call(), 0)
call_3572 = relay.TupleGetItem(func_3007_call(), 0)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_3593 = relay.TupleGetItem(func_254_call(), 1)
call_3594 = relay.TupleGetItem(func_255_call(), 1)
func_1442_call = mod.get_global_var('func_1442')
func_1444_call = mutated_mod.get_global_var('func_1444')
call_3610 = func_1442_call()
call_3611 = func_1442_call()
bop_3630 = relay.bitwise_and(call_3610.astype('uint16'), relay.reshape(call_3593.astype('uint16'), relay.shape_of(call_3610))) # shape=(3, 8, 1)
bop_3633 = relay.bitwise_and(call_3611.astype('uint16'), relay.reshape(call_3594.astype('uint16'), relay.shape_of(call_3611))) # shape=(3, 8, 1)
output = relay.Tuple([call_3571,bop_3630,])
output2 = relay.Tuple([call_3572,bop_3633,])
func_3636 = relay.Function([], output)
mod['func_3636'] = func_3636
mod = relay.transform.InferType()(mod)
output = func_3636()
func_3637 = relay.Function([], output)
mutated_mod['func_3637'] = func_3637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2828_call = mod.get_global_var('func_2828')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_3646 = relay.TupleGetItem(func_2828_call(), 2)
call_3647 = relay.TupleGetItem(func_2829_call(), 2)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_3650 = relay.TupleGetItem(func_515_call(), 2)
call_3651 = relay.TupleGetItem(func_516_call(), 2)
bop_3652 = relay.add(call_3646.astype('int32'), relay.reshape(call_3650.astype('int32'), relay.shape_of(call_3646))) # shape=(3, 8, 16)
bop_3655 = relay.add(call_3647.astype('int32'), relay.reshape(call_3651.astype('int32'), relay.shape_of(call_3647))) # shape=(3, 8, 16)
output = relay.Tuple([bop_3652,])
output2 = relay.Tuple([bop_3655,])
func_3660 = relay.Function([], output)
mod['func_3660'] = func_3660
mod = relay.transform.InferType()(mod)
mutated_mod['func_3660'] = func_3660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3660_call = mutated_mod.get_global_var('func_3660')
call_3661 = func_3660_call()
output = call_3661
func_3662 = relay.Function([], output)
mutated_mod['func_3662'] = func_3662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_515_call = mod.get_global_var('func_515')
func_516_call = mutated_mod.get_global_var('func_516')
call_3665 = relay.TupleGetItem(func_515_call(), 1)
call_3666 = relay.TupleGetItem(func_516_call(), 1)
func_1000_call = mod.get_global_var('func_1000')
func_1003_call = mutated_mod.get_global_var('func_1003')
var_3672 = relay.var("var_3672", dtype = "bool", shape = (1, 144))#candidate|3672|(1, 144)|var|bool
call_3671 = relay.TupleGetItem(func_1000_call(relay.reshape(var_3672.astype('bool'), [3, 8, 6])), 0)
call_3673 = relay.TupleGetItem(func_1003_call(relay.reshape(var_3672.astype('bool'), [3, 8, 6])), 0)
output = relay.Tuple([call_3665,call_3671,var_3672,])
output2 = relay.Tuple([call_3666,call_3673,var_3672,])
func_3676 = relay.Function([var_3672,], output)
mod['func_3676'] = func_3676
mod = relay.transform.InferType()(mod)
mutated_mod['func_3676'] = func_3676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3677 = relay.var("var_3677", dtype = "bool", shape = (1, 144))#candidate|3677|(1, 144)|var|bool
func_3676_call = mutated_mod.get_global_var('func_3676')
call_3678 = func_3676_call(var_3677)
output = call_3678
func_3679 = relay.Function([var_3677], output)
mutated_mod['func_3679'] = func_3679
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3694 = relay.const([[[-0.007447,-7.898311,4.372703,-0.581678,3.745276,4.685151,5.956598,-5.055490,-4.826629,7.689883,2.845048,-2.983017,-9.342826,3.203592,-7.182871,-4.395879],[-9.959563,-0.947268,3.733384,7.014760,-3.692061,7.875760,3.668795,9.638785,-9.678781,-1.956161,-0.554211,-2.659263,-1.343672,-3.747079,-3.060324,1.365753],[6.558877,-1.571437,-4.336457,-3.547635,-2.179146,-2.995550,0.010450,2.397592,-8.900713,0.105631,-3.626963,-7.487994,-1.743616,-0.087695,8.044532,0.860768],[0.937058,-3.826594,5.213421,-1.300727,-4.209470,9.711097,9.747470,-6.134770,1.195986,-7.913136,5.563945,-5.526764,5.992888,-2.722550,1.224338,-9.322080],[-4.101525,-4.038091,6.189545,4.272296,-1.418812,4.947078,-4.078444,1.376929,-4.073890,9.101913,-6.285189,8.299848,-9.124141,8.530747,5.102394,9.696721],[-2.349671,4.989893,-1.529802,4.949231,4.458260,-1.281788,-5.029934,7.418209,-1.517498,-0.486163,3.366653,-6.121377,-0.268803,1.284287,3.743755,8.256239],[-0.371003,1.649865,1.839514,7.167004,-9.121165,-6.736157,-7.373341,3.025134,4.030739,4.509266,9.732895,-8.638150,0.013237,6.343605,-3.874080,-9.567884],[2.616941,-3.595434,2.590653,7.334247,9.752126,-5.566716,-4.428980,-6.949738,-8.314630,-6.603993,-5.090257,8.763223,-5.101633,-7.390663,4.769466,6.112739],[8.680491,6.323340,-2.661102,-1.239104,3.019272,1.758610,-2.405158,6.693747,6.669876,-3.901339,-9.121603,-6.290336,-3.730620,-8.285289,5.719302,-8.894350],[4.710523,8.103069,-3.086693,0.929586,3.422470,3.460827,9.104745,-4.741082,-6.190191,-5.804144,-8.761147,4.056030,8.146208,-9.087450,-0.105660,6.820793],[-8.306568,3.731279,-5.258312,-9.846703,9.080493,1.768504,-8.805947,8.488490,-4.226307,-0.811183,-7.415676,4.829631,5.082037,2.520823,-4.780766,8.847342],[4.579706,-0.918650,7.627174,6.090448,-4.567601,3.481464,-0.470868,-7.491545,-3.109576,4.078934,-0.866015,7.073618,-9.122600,9.188197,0.218762,-1.071465],[3.422895,3.385469,4.067566,9.546723,2.901229,1.651679,-0.126739,7.597130,-8.596278,8.929204,6.665907,-3.604605,5.256516,7.169951,-4.558201,-4.874150],[-0.767107,-2.337678,-8.832141,5.251964,7.131385,-6.534614,-1.370656,-5.418459,-8.923165,-3.965876,-8.510992,-4.405440,-4.007393,6.504775,4.370747,0.798081],[3.191763,7.769625,9.486882,1.704937,5.204638,-2.847928,2.574703,-5.020496,7.381333,-6.936152,2.708856,6.884967,-9.183999,-2.569849,-3.350909,2.900753]],[[-9.696127,-7.674391,8.227935,-3.074185,3.169124,1.786307,5.543361,-3.312356,-2.405157,7.526402,2.903735,1.506683,6.125582,3.882992,6.345704,5.009503],[-3.254293,-6.051939,2.484407,-6.037590,4.576015,-5.108532,-5.206851,5.327619,8.243819,-1.181101,-4.197203,-5.688031,-9.480283,0.981847,-1.180962,0.962330],[-0.963846,-4.120689,-6.450570,-8.180034,-9.636196,-9.729681,-6.851106,6.596012,-6.943346,-9.941629,-4.427022,-0.596071,9.770692,-6.684093,-4.432235,-9.913084],[8.950029,6.728225,3.696139,-9.848882,-2.656153,-5.687663,-1.962039,-8.085477,-4.419367,6.478961,0.039563,8.527394,-0.133938,-0.210445,9.482224,5.693024],[5.708108,-6.744637,3.646328,7.916020,4.900681,-9.133135,5.892234,6.860288,4.282535,-0.649242,-2.881658,8.314136,-1.337011,-9.283317,-7.193833,-5.749933],[-6.308688,6.328434,4.484502,2.937229,-5.887646,6.346744,-5.663401,3.511561,1.206790,-3.552771,3.284125,-7.465974,1.936988,0.710991,5.972545,0.798513],[-4.802625,8.234784,6.100947,9.648015,-4.260224,-5.862932,0.318988,-9.065328,1.908902,-4.741658,2.986977,-1.128645,0.031130,-2.110930,-8.824224,-6.565130],[-3.505651,-2.105104,-6.679283,-3.029632,-4.401817,9.041353,-8.656452,3.575845,-5.894522,9.890213,-0.701274,-1.887583,7.048959,-0.921801,2.577940,6.749384],[-9.940125,4.386842,6.254221,1.128384,-2.869841,8.408243,7.113132,4.988052,-7.434174,7.973311,-1.975041,3.311666,-1.766093,7.096168,-2.122078,-5.714121],[9.046563,-5.466391,7.785965,-2.948600,-5.237067,-7.784854,-4.055694,-1.169445,-2.968553,-9.069532,2.601937,4.252282,6.397176,5.573117,8.567934,0.552807],[-3.816604,8.042460,8.778575,5.591349,9.330425,4.485253,9.338404,-6.061354,9.215869,9.450108,-3.612249,4.369207,3.498531,-4.818020,-3.023977,1.410763],[9.674641,-3.608123,4.923738,-4.841078,4.723870,-0.625182,3.719995,3.175663,4.204639,-4.698086,3.191227,-3.038248,-6.964629,3.724656,-0.603309,7.513674],[0.151711,-6.848333,-5.724459,9.922939,2.366584,-4.111023,-5.941656,6.130970,-2.163568,-0.055486,1.557541,2.014199,5.019936,-5.178846,4.723231,6.617428],[1.434971,9.017661,-4.327976,-6.997908,9.497434,7.601315,-8.237214,5.647880,-1.154441,-9.519039,-4.611972,6.414943,-2.203174,3.963127,-3.311010,-9.458595],[5.315757,1.971944,-9.219420,9.639333,-9.433479,3.264673,9.241992,-2.293665,-8.168653,-4.944474,-0.954349,-2.347377,7.995484,-4.163011,-6.108549,-0.013359]],[[2.868983,-8.687779,7.072766,4.781785,-3.560646,-1.748072,1.908445,7.653066,0.663294,3.566452,5.739395,-5.232739,8.685956,-8.819936,4.805037,6.500297],[-7.697887,-8.836707,3.407446,-8.828317,-9.756073,-5.156613,0.944708,-0.504205,1.314189,-7.804478,3.365182,8.414426,5.284105,1.269469,-0.059004,6.317624],[-0.323657,-0.485676,0.983372,0.793945,1.049812,-7.480797,7.051395,9.335027,-0.296097,5.678625,-4.090440,-0.555996,7.148973,-3.473673,5.187873,-0.263729],[8.061615,9.616343,4.432949,5.047458,-2.141925,1.066015,-1.319338,-0.903948,-5.409549,-5.873157,7.477359,9.438683,-6.390820,-1.639922,0.865168,4.760823],[-1.141619,-4.937269,7.605801,-5.186088,8.425264,3.505336,7.612692,-7.429514,-1.517319,-5.594424,3.392232,-8.802969,-6.974998,7.452782,3.501697,-4.747562],[-0.701327,-6.588051,-1.647727,9.010500,-7.669942,5.496121,6.709005,-6.686272,2.034513,5.347912,-9.033985,-0.357495,-8.997114,-9.959078,4.525111,2.998005],[7.388854,3.728131,2.243302,7.075062,-6.634584,6.541609,-8.457815,1.792976,-4.204005,1.860383,-3.667685,9.931191,9.131963,-2.110091,2.297292,-0.220811],[6.407134,-6.239169,9.788955,4.208574,7.747270,6.804947,-2.367641,3.729329,5.245564,3.651861,-3.398610,-2.271705,-4.489520,-1.191863,4.069408,4.409228],[1.047309,1.078032,0.785689,-9.092402,6.478155,4.865426,-9.602182,-9.177497,6.423727,9.643680,9.917032,7.698480,-5.659866,7.922606,6.352786,8.206422],[-0.909875,8.007913,8.596613,-4.098816,3.919858,-8.802686,-8.169865,3.982196,-8.579149,-9.215409,-3.859437,6.968799,8.774540,-5.139422,2.600337,6.832194],[-1.963698,-9.183720,-2.368592,-6.753891,-8.390381,8.200580,-6.981203,-1.558297,0.442910,-6.469081,-1.444795,9.976697,-6.279861,-9.821296,1.474063,6.171365],[-8.971990,0.912164,1.422588,-5.779292,-2.105253,-1.419104,-0.070263,3.243286,5.832764,-1.676000,1.518288,-1.968992,5.449399,-6.631570,-2.163581,0.307357],[0.854604,-0.922295,-7.637775,-9.395381,-1.680706,2.184967,3.717720,5.043652,-8.050474,-7.049903,4.518209,8.101813,-6.659359,5.860973,-3.095723,3.101553],[7.465227,-9.824439,6.991289,-6.724687,4.386187,-2.138545,-9.752567,-9.488585,1.769348,-2.611015,7.186560,-1.655288,0.282957,-5.470159,-3.362740,3.059424],[7.183617,4.375585,-7.074837,8.461237,-1.331855,-6.522881,9.298684,2.921658,-7.148307,8.139332,-1.535141,6.684319,6.683981,1.881581,6.772775,3.103601]],[[-3.655699,1.874000,-7.746593,-6.372965,0.827760,6.978231,6.107555,3.832478,-9.695636,4.911192,-1.021731,7.459486,5.118794,5.962573,7.808890,9.337115],[-9.466494,9.536183,2.250473,5.042594,-0.144696,6.572512,2.870333,1.716520,6.419620,-3.775000,5.637175,7.953135,-8.205372,-8.719094,6.013577,6.279080],[-4.151441,-6.592358,4.263007,-2.570173,-3.873476,0.605544,4.806544,-3.540854,-0.966491,-3.087395,-8.101408,-0.297944,3.047227,-2.792330,-9.419973,-7.466761],[-9.127811,9.768777,-9.678276,-0.835913,8.404976,-4.055328,-5.678610,-0.416327,-3.323557,8.657590,-2.172652,2.245490,-7.632989,2.801722,-5.810700,1.784542],[-4.427102,-2.531695,0.213548,-8.196466,-4.495967,8.859137,7.127729,0.507984,-9.636881,-1.497295,-3.342062,-9.487865,2.203266,-7.876634,0.405194,8.671997],[-8.672888,-9.830094,-4.244014,-0.938699,-8.697568,9.566643,4.784177,9.613288,7.783925,8.122133,5.401722,-9.138288,8.421050,-1.891478,3.302854,-6.825756],[2.649074,0.388311,6.334929,2.248440,2.210428,9.950276,1.078595,-5.322647,-4.529709,6.232851,-6.681944,7.393495,-7.745968,-2.694602,2.981986,7.346000],[-9.590946,-1.637421,-9.426896,1.633396,-9.007367,3.870915,5.653922,5.090538,2.034977,6.413155,-3.898587,4.229268,2.886455,-1.291605,-7.887477,3.835842],[-8.336022,7.256096,1.093024,-7.200141,8.887792,-9.753916,-8.288531,8.377154,-0.949515,0.110504,7.523933,5.573224,-3.860552,2.026975,9.391469,3.595909],[-5.236236,-4.310986,9.745018,6.985234,-5.953913,1.440778,8.943981,-1.716938,-1.627593,2.959564,-5.175900,-6.135842,-1.969547,-1.132982,-1.874334,-8.579241],[-2.996996,2.204070,9.092540,-2.648266,-1.350021,-8.861858,-2.415951,9.281911,-1.560391,-1.929243,2.231837,-0.495614,-3.987399,3.146175,-6.499008,3.723311],[-9.901637,5.898613,-9.414440,-8.755495,3.438391,-1.876225,8.550641,-9.285632,-5.473643,2.187639,9.948108,-0.966307,-9.785425,9.244530,0.326645,8.541232],[1.052471,9.818499,-7.852940,-2.245926,7.869716,-5.789636,-8.053448,-5.476464,0.350213,-9.107915,2.228266,8.257109,-8.640302,8.045198,7.108088,1.029993],[4.534037,-3.341736,-6.232532,9.243196,-1.583119,8.621074,9.763230,7.993566,2.447835,6.739359,-1.783601,-2.220801,0.874588,-2.256396,-1.889039,6.438450],[2.707504,1.287134,-3.569848,9.170268,-1.677116,0.833520,-4.841224,9.295281,-8.853682,8.168644,3.885624,1.475926,1.375007,8.166461,-7.755196,9.363354]],[[6.546277,7.730931,5.032163,-0.450135,2.606104,7.609975,-8.407341,1.004771,-3.292442,-2.984287,-1.881073,-7.094954,1.764196,3.183805,2.345549,0.352210],[-6.584106,-8.521151,6.042765,4.539677,8.808463,8.108130,0.949851,-8.088745,6.535581,5.683622,7.022485,4.800403,-9.366231,-8.835478,1.567006,-6.057216],[-7.466932,6.818592,3.544225,5.519774,-0.523086,-5.698135,9.122213,6.246006,9.290538,6.300873,-5.714621,-6.642397,6.521666,-1.155523,-8.788737,-1.625007],[-6.411172,7.753324,6.564954,-2.855976,3.533853,2.535058,6.739371,6.225384,-9.164961,8.547888,0.156256,2.678607,-3.147393,1.575101,-2.623512,-2.971005],[5.251419,-7.603323,-9.166649,-2.910509,4.004735,-2.944564,-5.903578,-7.783145,-9.689912,-4.651844,3.070030,4.246548,2.992934,-3.593875,-2.487062,-6.025953],[-4.901406,-1.087653,7.914452,-9.082095,3.259191,-0.907925,-3.212749,-4.888776,-8.010707,-7.429812,-8.135237,-5.299963,-5.822379,1.974971,3.556112,6.492593],[-4.679035,-2.999092,-6.617716,-7.999521,2.041686,-7.046082,9.182745,7.863992,1.932137,1.245520,6.114286,4.272265,5.795362,-6.926309,9.433830,-2.964549],[-6.973714,3.695855,-9.835638,-0.661127,-4.676588,1.004666,8.262861,-5.259849,8.471823,-6.217273,2.480492,-6.967350,-0.024310,7.308951,-8.275431,2.806801],[-2.354892,-5.381231,-5.640122,-7.908129,4.008612,2.193125,-8.029153,8.767786,6.218716,-1.180469,5.582337,2.015715,-1.756835,1.056628,4.665061,9.477448],[-4.356173,-9.486604,-2.197426,0.162444,-8.395296,-8.033919,-0.860876,-6.923719,0.115870,-6.024505,-9.905940,-8.679263,-1.258786,9.775942,-2.851507,7.967088],[-7.466012,3.419376,2.876319,-8.172552,8.351325,-7.941317,-8.529610,-1.779510,-9.994492,3.823513,-6.440090,1.121163,6.996771,-1.878437,3.157866,-2.878518],[7.922460,-1.634269,9.152249,3.655737,8.147846,-8.734536,-7.178104,8.010465,-8.393919,8.042181,-1.271056,5.289282,-0.521430,6.324745,-2.182979,4.653963],[2.573146,-5.865589,6.428255,-2.228743,4.999720,-1.945878,8.924063,-3.211707,-6.902212,-3.123756,-7.283569,2.069187,-9.191252,-4.292817,-6.308731,-2.914276],[3.816413,-7.165667,-7.014454,0.694466,-8.535072,-5.954451,3.352091,4.585289,-0.105602,-8.074001,1.435038,4.729625,-2.764472,-9.756114,-4.941517,0.039624],[8.177011,-7.014666,-5.255372,-8.334052,4.535109,-9.219456,3.010319,8.654700,7.106171,3.157098,2.605170,-2.395487,-9.160499,-3.224231,-3.457409,3.378078]],[[-5.904340,6.962285,4.275790,2.289415,-2.104642,-4.123295,5.067624,-9.296478,7.323792,7.610654,-0.071802,4.733990,3.962377,0.890622,1.761858,2.432404],[-9.139934,-3.626789,-2.520465,7.333180,7.667674,2.142902,4.338725,6.598630,3.322987,1.417213,6.884712,-9.857170,-8.982473,-7.679564,-6.986447,7.574593],[-1.355815,3.793271,0.172790,-2.141680,-1.204953,5.807733,7.605424,-6.506074,-6.685743,-7.384365,-3.832942,-5.443413,1.095448,-9.712308,-5.479790,-6.446832],[1.047090,-4.636770,-8.757834,4.004197,-9.139385,-3.939862,-1.803340,-9.050736,-5.505252,-2.301528,4.071826,-0.787474,3.336095,8.010390,-0.594270,-2.279878],[0.906522,2.494732,2.325998,-3.202379,8.424286,7.056334,9.169458,-3.363541,7.955203,0.184644,2.164849,9.272848,-4.670403,3.383951,-1.773234,3.286677],[-7.919286,-9.903181,6.391447,3.657577,0.895958,-4.621611,-7.460600,4.608904,0.170948,-7.158107,-3.885742,7.067965,-7.847640,9.674772,4.604787,-3.832103],[7.980803,9.917951,6.089033,-1.916949,-4.074846,-0.025049,2.021214,-3.125180,-0.252086,-5.209986,-7.998795,0.827781,-2.362563,7.684552,1.781167,2.419940],[-4.719136,-1.104984,5.603259,3.718318,4.744099,-1.189200,9.339147,-7.409432,1.246085,-3.276154,-9.235448,9.705301,-0.930738,-9.224869,-6.224590,3.392865],[8.847538,3.776847,-8.613466,-2.247313,-3.592403,-3.347380,4.934447,4.275986,8.550364,-4.128321,5.316331,-7.574492,-4.544754,-2.900386,-2.960561,-1.449811],[0.700711,-5.161732,-3.545474,4.409835,8.387971,-7.820133,-4.145684,-7.194782,0.120599,-6.699411,-5.911695,-0.058135,5.292888,1.655756,-4.918783,7.397962],[6.462376,9.784806,-6.628656,-1.784434,6.266974,-9.289797,-5.900965,4.749855,4.972871,6.417497,3.644850,8.508819,-2.210240,-6.550365,-6.484777,-4.211162],[-9.762681,1.295009,-9.221324,-7.915400,-1.977225,-3.291956,9.202102,-9.769752,5.791160,-4.448023,2.432898,9.790344,5.781326,2.140153,-7.399598,8.511796],[3.787835,7.590009,2.546158,1.516804,2.152921,-4.886100,-5.574833,8.540444,-4.539005,-2.945914,1.544889,1.739223,3.655864,-7.003623,-9.383322,-9.498815],[-9.656104,-0.500338,-6.126580,9.200721,2.490685,-8.078907,-1.098958,7.899487,-7.136120,4.366943,2.436190,-6.757105,5.005536,-6.687650,-3.136692,6.429834],[9.967076,-5.556376,-9.115032,9.548412,-7.865674,9.110502,7.398988,3.099747,-7.176915,-6.388367,-2.818556,-3.942889,5.003486,2.578059,-4.042870,5.391370]]], dtype = "float32")#candidate|3694|(6, 15, 16)|const|float32
var_3695 = relay.var("var_3695", dtype = "float32", shape = (6, 15, 16))#candidate|3695|(6, 15, 16)|var|float32
bop_3696 = relay.divide(const_3694.astype('float32'), relay.reshape(var_3695.astype('float32'), relay.shape_of(const_3694))) # shape=(6, 15, 16)
output = relay.Tuple([bop_3696,])
output2 = relay.Tuple([bop_3696,])
func_3699 = relay.Function([var_3695,], output)
mod['func_3699'] = func_3699
mod = relay.transform.InferType()(mod)
var_3700 = relay.var("var_3700", dtype = "float32", shape = (6, 15, 16))#candidate|3700|(6, 15, 16)|var|float32
output = func_3699(var_3700)
func_3701 = relay.Function([var_3700], output)
mutated_mod['func_3701'] = func_3701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2828_call = mod.get_global_var('func_2828')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_3723 = relay.TupleGetItem(func_2828_call(), 3)
call_3724 = relay.TupleGetItem(func_2829_call(), 3)
output = call_3723
output2 = call_3724
func_3733 = relay.Function([], output)
mod['func_3733'] = func_3733
mod = relay.transform.InferType()(mod)
mutated_mod['func_3733'] = func_3733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3733_call = mutated_mod.get_global_var('func_3733')
call_3734 = func_3733_call()
output = call_3734
func_3735 = relay.Function([], output)
mutated_mod['func_3735'] = func_3735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2532_call = mod.get_global_var('func_2532')
func_2534_call = mutated_mod.get_global_var('func_2534')
call_3738 = relay.TupleGetItem(func_2532_call(), 2)
call_3739 = relay.TupleGetItem(func_2534_call(), 2)
output = relay.Tuple([call_3738,])
output2 = relay.Tuple([call_3739,])
func_3744 = relay.Function([], output)
mod['func_3744'] = func_3744
mod = relay.transform.InferType()(mod)
mutated_mod['func_3744'] = func_3744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3744_call = mutated_mod.get_global_var('func_3744')
call_3745 = func_3744_call()
output = call_3745
func_3746 = relay.Function([], output)
mutated_mod['func_3746'] = func_3746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3793 = relay.var("var_3793", dtype = "float32", shape = ())#candidate|3793|()|var|float32
var_3794 = relay.var("var_3794", dtype = "float32", shape = (3, 11, 14))#candidate|3794|(3, 11, 14)|var|float32
bop_3795 = relay.floor_mod(var_3793.astype('float32'), var_3794.astype('float32')) # shape=(3, 11, 14)
output = relay.Tuple([bop_3795,])
output2 = relay.Tuple([bop_3795,])
func_3799 = relay.Function([var_3793,var_3794,], output)
mod['func_3799'] = func_3799
mod = relay.transform.InferType()(mod)
var_3800 = relay.var("var_3800", dtype = "float32", shape = ())#candidate|3800|()|var|float32
var_3801 = relay.var("var_3801", dtype = "float32", shape = (3, 11, 14))#candidate|3801|(3, 11, 14)|var|float32
output = func_3799(var_3800,var_3801,)
func_3802 = relay.Function([var_3800,var_3801,], output)
mutated_mod['func_3802'] = func_3802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2292_call = mod.get_global_var('func_2292')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_3804 = func_2292_call()
call_3805 = func_2292_call()
var_3821 = relay.var("var_3821", dtype = "bool", shape = (3, 8, 5))#candidate|3821|(3, 8, 5)|var|bool
bop_3822 = relay.right_shift(call_3804.astype('uint8'), var_3821.astype('uint8')) # shape=(3, 8, 5)
bop_3825 = relay.right_shift(call_3805.astype('uint8'), var_3821.astype('uint8')) # shape=(3, 8, 5)
output = relay.Tuple([bop_3822,])
output2 = relay.Tuple([bop_3825,])
func_3835 = relay.Function([var_3821,], output)
mod['func_3835'] = func_3835
mod = relay.transform.InferType()(mod)
mutated_mod['func_3835'] = func_3835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3836 = relay.var("var_3836", dtype = "bool", shape = (3, 8, 5))#candidate|3836|(3, 8, 5)|var|bool
func_3835_call = mutated_mod.get_global_var('func_3835')
call_3837 = func_3835_call(var_3836)
output = call_3837
func_3838 = relay.Function([var_3836], output)
mutated_mod['func_3838'] = func_3838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_3842 = func_2271_call()
call_3843 = func_2271_call()
output = call_3842
output2 = call_3843
func_3846 = relay.Function([], output)
mod['func_3846'] = func_3846
mod = relay.transform.InferType()(mod)
output = func_3846()
func_3847 = relay.Function([], output)
mutated_mod['func_3847'] = func_3847
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3888 = relay.const([[[-5.821481,5.194361,3.445867,-4.095097,5.764213,-9.712241,1.459539,-4.003517,-3.223432,-2.700569,7.496730,4.504073,6.715455,-9.727699,-8.767908,-5.096107]],[[-5.852260,0.829017,-8.732386,9.422418,4.913225,1.897767,2.569195,-4.632684,5.397645,4.215271,3.269321,-7.615808,1.718311,-1.660701,8.177172,6.316549]],[[-5.849579,6.776777,-2.596528,-5.346493,4.024319,1.786378,3.628866,-3.714432,-2.351070,6.274981,-5.978894,-6.491613,-8.620936,-9.808781,-4.860330,3.644261]],[[-9.020667,9.046231,2.272032,-2.599454,9.651953,-5.674417,6.825154,-0.551281,-8.596139,6.151432,8.231486,-8.710841,-1.408731,0.003502,-8.642887,1.205740]],[[-4.170272,-3.269004,3.053872,-3.882403,-1.642277,3.015894,4.024689,3.694433,-6.388182,-7.527062,4.258776,7.647529,6.120385,-6.998795,-5.138468,6.547425]],[[-0.829295,-5.150897,-4.190380,-6.850722,2.727660,8.955768,7.365666,-2.116329,9.459725,-5.367389,-8.399889,4.227739,-0.438653,4.249463,2.794210,3.158127]],[[-3.822930,2.264052,-2.058885,1.873186,-7.239654,-5.549784,-0.205263,7.663645,-6.992205,-8.038266,8.972913,-2.879748,2.715663,-2.613061,-9.661928,-7.435740]],[[-1.810156,-1.051975,2.642543,-2.205932,-5.683343,-2.825471,-9.885489,-1.725182,8.199939,1.793724,-4.297802,-7.166209,9.716616,0.229578,4.727961,2.528832]]], dtype = "float32")#candidate|3888|(8, 1, 16)|const|float32
var_3889 = relay.var("var_3889", dtype = "float32", shape = (8, 5, 16))#candidate|3889|(8, 5, 16)|var|float32
bop_3890 = relay.floor_divide(const_3888.astype('float32'), var_3889.astype('float32')) # shape=(8, 5, 16)
func_1100_call = mod.get_global_var('func_1100')
func_1101_call = mutated_mod.get_global_var('func_1101')
call_3902 = func_1100_call()
call_3903 = func_1100_call()
uop_3909 = relay.log2(call_3902.astype('float64')) # shape=(3, 8, 1)
uop_3911 = relay.log2(call_3903.astype('float64')) # shape=(3, 8, 1)
bop_3912 = relay.logical_xor(uop_3909.astype('int16'), relay.reshape(call_3902.astype('int16'), relay.shape_of(uop_3909))) # shape=(3, 8, 1)
bop_3915 = relay.logical_xor(uop_3911.astype('int16'), relay.reshape(call_3903.astype('int16'), relay.shape_of(uop_3911))) # shape=(3, 8, 1)
func_1264_call = mod.get_global_var('func_1264')
func_1267_call = mutated_mod.get_global_var('func_1267')
call_3916 = relay.TupleGetItem(func_1264_call(relay.reshape(const_3888.astype('float32'), [2, 8, 8])), 0)
call_3917 = relay.TupleGetItem(func_1267_call(relay.reshape(const_3888.astype('float32'), [2, 8, 8])), 0)
bop_3923 = relay.mod(bop_3912.astype('float32'), relay.reshape(call_3902.astype('float32'), relay.shape_of(bop_3912))) # shape=(3, 8, 1)
bop_3926 = relay.mod(bop_3915.astype('float32'), relay.reshape(call_3903.astype('float32'), relay.shape_of(bop_3915))) # shape=(3, 8, 1)
output = relay.Tuple([bop_3890,call_3916,bop_3923,])
output2 = relay.Tuple([bop_3890,call_3917,bop_3926,])
func_3953 = relay.Function([var_3889,], output)
mod['func_3953'] = func_3953
mod = relay.transform.InferType()(mod)
mutated_mod['func_3953'] = func_3953
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3954 = relay.var("var_3954", dtype = "float32", shape = (8, 5, 16))#candidate|3954|(8, 5, 16)|var|float32
func_3953_call = mutated_mod.get_global_var('func_3953')
call_3955 = func_3953_call(var_3954)
output = call_3955
func_3956 = relay.Function([var_3954], output)
mutated_mod['func_3956'] = func_3956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2109_call = mod.get_global_var('func_2109')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_3973 = func_2109_call()
call_3974 = func_2109_call()
output = relay.Tuple([call_3973,])
output2 = relay.Tuple([call_3974,])
func_3977 = relay.Function([], output)
mod['func_3977'] = func_3977
mod = relay.transform.InferType()(mod)
mutated_mod['func_3977'] = func_3977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3977_call = mutated_mod.get_global_var('func_3977')
call_3978 = func_3977_call()
output = call_3978
func_3979 = relay.Function([], output)
mutated_mod['func_3979'] = func_3979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4003 = relay.var("var_4003", dtype = "float64", shape = (11, 12, 3))#candidate|4003|(11, 12, 3)|var|float64
uop_4004 = relay.tan(var_4003.astype('float64')) # shape=(11, 12, 3)
func_3953_call = mod.get_global_var('func_3953')
func_3956_call = mutated_mod.get_global_var('func_3956')
var_4009 = relay.var("var_4009", dtype = "float32", shape = (640,))#candidate|4009|(640,)|var|float32
call_4008 = relay.TupleGetItem(func_3953_call(relay.reshape(var_4009.astype('float32'), [8, 5, 16])), 2)
call_4010 = relay.TupleGetItem(func_3956_call(relay.reshape(var_4009.astype('float32'), [8, 5, 16])), 2)
func_1127_call = mod.get_global_var('func_1127')
func_1128_call = mutated_mod.get_global_var('func_1128')
call_4030 = func_1127_call()
call_4031 = func_1127_call()
output = relay.Tuple([uop_4004,call_4008,var_4009,call_4030,])
output2 = relay.Tuple([uop_4004,call_4010,var_4009,call_4031,])
func_4032 = relay.Function([var_4003,var_4009,], output)
mod['func_4032'] = func_4032
mod = relay.transform.InferType()(mod)
var_4033 = relay.var("var_4033", dtype = "float64", shape = (11, 12, 3))#candidate|4033|(11, 12, 3)|var|float64
var_4034 = relay.var("var_4034", dtype = "float32", shape = (640,))#candidate|4034|(640,)|var|float32
output = func_4032(var_4033,var_4034,)
func_4035 = relay.Function([var_4033,var_4034,], output)
mutated_mod['func_4035'] = func_4035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2253_call = mod.get_global_var('func_2253')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_4039 = func_2253_call()
call_4040 = func_2253_call()
output = call_4039
output2 = call_4040
func_4042 = relay.Function([], output)
mod['func_4042'] = func_4042
mod = relay.transform.InferType()(mod)
mutated_mod['func_4042'] = func_4042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4042_call = mutated_mod.get_global_var('func_4042')
call_4043 = func_4042_call()
output = call_4043
func_4044 = relay.Function([], output)
mutated_mod['func_4044'] = func_4044
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4052 = relay.var("var_4052", dtype = "int32", shape = ())#candidate|4052|()|var|int32
var_4053 = relay.var("var_4053", dtype = "int32", shape = (9, 14, 10))#candidate|4053|(9, 14, 10)|var|int32
bop_4054 = relay.minimum(var_4052.astype('int32'), var_4053.astype('int32')) # shape=(9, 14, 10)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_4058 = relay.TupleGetItem(func_609_call(), 0)
call_4059 = relay.TupleGetItem(func_611_call(), 0)
output = relay.Tuple([bop_4054,call_4058,])
output2 = relay.Tuple([bop_4054,call_4059,])
func_4071 = relay.Function([var_4052,var_4053,], output)
mod['func_4071'] = func_4071
mod = relay.transform.InferType()(mod)
var_4072 = relay.var("var_4072", dtype = "int32", shape = ())#candidate|4072|()|var|int32
var_4073 = relay.var("var_4073", dtype = "int32", shape = (9, 14, 10))#candidate|4073|(9, 14, 10)|var|int32
output = func_4071(var_4072,var_4073,)
func_4074 = relay.Function([var_4072,var_4073,], output)
mutated_mod['func_4074'] = func_4074
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4136 = relay.const([[[-10,-1,-5,7],[5,9,1,6],[4,-4,10,-4],[-1,9,-4,-10],[-9,-5,1,-4]]], dtype = "int32")#candidate|4136|(1, 5, 4)|const|int32
const_4137 = relay.const([[[4,5,5,-1],[-8,6,5,6],[7,-7,6,-5],[-2,-4,-3,-10],[-8,-6,-4,3]],[[1,-5,-7,8],[-3,-1,1,-2],[4,-9,-3,-3],[-6,4,-9,-2],[-8,-5,-10,-9]],[[10,-3,-5,5],[-3,6,5,-8],[10,1,-1,-10],[-9,-4,-9,-1],[-2,-1,-9,6]],[[-1,1,4,9],[3,5,-10,-5],[-1,-8,-3,-1],[-3,-1,7,6],[2,5,7,9]],[[-3,-4,-9,-4],[9,1,10,4],[-2,-6,4,8],[1,1,-9,-8],[3,7,-2,-2]],[[-2,-10,5,-8],[2,-8,7,-2],[1,-6,4,-3],[7,-10,-3,-9],[-7,9,-4,-9]],[[-8,3,-2,4],[10,4,-4,-2],[-8,-8,-7,6],[-6,4,-2,6],[-9,-7,-6,4]],[[1,-10,6,-3],[-4,-7,-10,5],[-10,9,3,1],[-4,4,-1,6],[6,-6,5,1]],[[2,2,-3,-1],[-9,4,-6,5],[5,-2,8,8],[-1,8,-4,5],[7,2,-6,2]],[[3,-7,-2,9],[-2,4,8,-3],[6,4,10,-10],[9,-8,4,10],[5,6,-2,5]],[[-7,-3,10,-3],[9,8,7,8],[-9,2,-6,5],[-2,9,8,-7],[2,2,-7,-8]]], dtype = "int32")#candidate|4137|(11, 5, 4)|const|int32
bop_4138 = relay.left_shift(const_4136.astype('int32'), const_4137.astype('int32')) # shape=(11, 5, 4)
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_4156 = relay.TupleGetItem(func_2356_call(), 1)
call_4157 = relay.TupleGetItem(func_2358_call(), 1)
output = relay.Tuple([bop_4138,call_4156,])
output2 = relay.Tuple([bop_4138,call_4157,])
func_4158 = relay.Function([], output)
mod['func_4158'] = func_4158
mod = relay.transform.InferType()(mod)
output = func_4158()
func_4159 = relay.Function([], output)
mutated_mod['func_4159'] = func_4159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2471_call = mod.get_global_var('func_2471')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_4179 = relay.TupleGetItem(func_2471_call(), 0)
call_4180 = relay.TupleGetItem(func_2473_call(), 0)
var_4197 = relay.var("var_4197", dtype = "float32", shape = (3, 8, 11))#candidate|4197|(3, 8, 11)|var|float32
bop_4198 = relay.power(call_4179.astype('float32'), var_4197.astype('float32')) # shape=(3, 8, 11)
bop_4201 = relay.power(call_4180.astype('float32'), var_4197.astype('float32')) # shape=(3, 8, 11)
func_3846_call = mod.get_global_var('func_3846')
func_3847_call = mutated_mod.get_global_var('func_3847')
call_4206 = func_3846_call()
call_4207 = func_3846_call()
output = relay.Tuple([bop_4198,call_4206,])
output2 = relay.Tuple([bop_4201,call_4207,])
func_4211 = relay.Function([var_4197,], output)
mod['func_4211'] = func_4211
mod = relay.transform.InferType()(mod)
mutated_mod['func_4211'] = func_4211
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4212 = relay.var("var_4212", dtype = "float32", shape = (3, 8, 11))#candidate|4212|(3, 8, 11)|var|float32
func_4211_call = mutated_mod.get_global_var('func_4211')
call_4213 = func_4211_call(var_4212)
output = call_4213
func_4214 = relay.Function([var_4212], output)
mutated_mod['func_4214'] = func_4214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_4232 = relay.TupleGetItem(func_254_call(), 0)
call_4233 = relay.TupleGetItem(func_255_call(), 0)
output = call_4232
output2 = call_4233
func_4234 = relay.Function([], output)
mod['func_4234'] = func_4234
mod = relay.transform.InferType()(mod)
output = func_4234()
func_4235 = relay.Function([], output)
mutated_mod['func_4235'] = func_4235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3846_call = mod.get_global_var('func_3846')
func_3847_call = mutated_mod.get_global_var('func_3847')
call_4279 = func_3846_call()
call_4280 = func_3846_call()
func_1372_call = mod.get_global_var('func_1372')
func_1376_call = mutated_mod.get_global_var('func_1376')
var_4292 = relay.var("var_4292", dtype = "float32", shape = (128, 1))#candidate|4292|(128, 1)|var|float32
const_4293 = relay.const([0.529485,1.535641,3.960810,-7.465923,0.452269,3.802416,-6.036304,-2.454861,-4.216588,-3.969749,7.402269,4.425613,-3.799483,-5.579674,7.079500,-3.236691,-9.404777,3.912113,5.605909,-0.146129,5.221385,-0.560910,7.523873,-6.459022,4.946062,-8.270975,6.445194,-0.066102,-1.380563,-5.770215], dtype = "float32")#candidate|4293|(30,)|const|float32
call_4291 = relay.TupleGetItem(func_1372_call(relay.reshape(var_4292.astype('float32'), [128,]), relay.reshape(const_4293.astype('float32'), [30,]), ), 5)
call_4294 = relay.TupleGetItem(func_1376_call(relay.reshape(var_4292.astype('float32'), [128,]), relay.reshape(const_4293.astype('float32'), [30,]), ), 5)
func_2794_call = mod.get_global_var('func_2794')
func_2797_call = mutated_mod.get_global_var('func_2797')
var_4315 = relay.var("var_4315", dtype = "bool", shape = (48, 2))#candidate|4315|(48, 2)|var|bool
call_4314 = relay.TupleGetItem(func_2794_call(relay.reshape(var_4315.astype('bool'), [3, 8, 4])), 0)
call_4316 = relay.TupleGetItem(func_2797_call(relay.reshape(var_4315.astype('bool'), [3, 8, 4])), 0)
var_4325 = relay.var("var_4325", dtype = "float32", shape = (128, 2))#candidate|4325|(128, 2)|var|float32
bop_4326 = relay.less(var_4292.astype('bool'), var_4325.astype('bool')) # shape=(128, 2)
bop_4330 = relay.multiply(call_4291.astype('uint32'), relay.reshape(call_4279.astype('uint32'), relay.shape_of(call_4291))) # shape=(3, 8, 16)
bop_4333 = relay.multiply(call_4294.astype('uint32'), relay.reshape(call_4280.astype('uint32'), relay.shape_of(call_4294))) # shape=(3, 8, 16)
func_2711_call = mod.get_global_var('func_2711')
func_2714_call = mutated_mod.get_global_var('func_2714')
const_4339 = relay.const([[1,7,-2,-4,6,-10,-10,-6,-6,-8,3,7,9,6,10,-10,-9,2,3,-8,9,-3,7,-5,4,-7,7,2,6,9,-9,-6,7,2,3,10,10,-10,5,-1,9,9,10,1,9,-3,-1,7,-8,-10,10,4,5,8,-1,10,5,-5,1,2,-8,-6,-7,-8,3,7,-8,-7,4,3,-2,-5,-2,-1,-6,3,-1,4,-4,-2,-10,4,7,1,5,-7,6,-4,-2,-1,2,-4,-5,-1,-3,-5,10,-1,1,10,-5,-2,1,-9,-3,-5,6,-7,10,-9,-9,-5,4,-9,7,10,10,-3,8,-6,-4,-5,10,3,-10,-4,7,-9,7,-7,-7,8,-8,8,5,-8,-7,-1,-7,-9,-7,5,2,6,-3,-8,9,-10,7,5,-6,-2,6,-9,2,-9,1,-4,1,4,4,-6,8,-1,6,10,9,-2,-7,-7,9,9,-1,4,-2,5,10,10,7,-6,7,4,8,-10,-9,6,-2,-9,-8,4,3,8,1,3,7,-3,-5,-10,-7,10,7,5,2,2,-8,10,8,-5,5,-8,-9,-9,-10,-9,-9,-4,-6,-4,4,8,6,5,7,-4]], dtype = "int32")#candidate|4339|(1, 224)|const|int32
call_4338 = relay.TupleGetItem(func_2711_call(relay.reshape(const_4339.astype('int32'), [224,])), 6)
call_4340 = relay.TupleGetItem(func_2714_call(relay.reshape(const_4339.astype('int32'), [224,])), 6)
func_3733_call = mod.get_global_var('func_3733')
func_3735_call = mutated_mod.get_global_var('func_3735')
call_4344 = func_3733_call()
call_4345 = func_3733_call()
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_4359 = relay.TupleGetItem(func_2356_call(), 1)
call_4360 = relay.TupleGetItem(func_2358_call(), 1)
output = relay.Tuple([const_4293,call_4314,var_4315,bop_4326,bop_4330,call_4338,const_4339,call_4344,call_4359,])
output2 = relay.Tuple([const_4293,call_4316,var_4315,bop_4326,bop_4333,call_4340,const_4339,call_4345,call_4360,])
func_4363 = relay.Function([var_4292,var_4315,var_4325,], output)
mod['func_4363'] = func_4363
mod = relay.transform.InferType()(mod)
var_4364 = relay.var("var_4364", dtype = "float32", shape = (128, 1))#candidate|4364|(128, 1)|var|float32
var_4365 = relay.var("var_4365", dtype = "bool", shape = (48, 2))#candidate|4365|(48, 2)|var|bool
var_4366 = relay.var("var_4366", dtype = "float32", shape = (128, 2))#candidate|4366|(128, 2)|var|float32
output = func_4363(var_4364,var_4365,var_4366,)
func_4367 = relay.Function([var_4364,var_4365,var_4366,], output)
mutated_mod['func_4367'] = func_4367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2109_call = mod.get_global_var('func_2109')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_4488 = func_2109_call()
call_4489 = func_2109_call()
func_1639_call = mod.get_global_var('func_1639')
func_1643_call = mutated_mod.get_global_var('func_1643')
var_4493 = relay.var("var_4493", dtype = "float32", shape = (336,))#candidate|4493|(336,)|var|float32
var_4494 = relay.var("var_4494", dtype = "uint16", shape = (1344,))#candidate|4494|(1344,)|var|uint16
call_4492 = relay.TupleGetItem(func_1639_call(relay.reshape(var_4493.astype('float32'), [3, 8, 14]), relay.reshape(var_4494.astype('uint16'), [1344,]), ), 2)
call_4495 = relay.TupleGetItem(func_1643_call(relay.reshape(var_4493.astype('float32'), [3, 8, 14]), relay.reshape(var_4494.astype('uint16'), [1344,]), ), 2)
func_3660_call = mod.get_global_var('func_3660')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_4504 = relay.TupleGetItem(func_3660_call(), 0)
call_4505 = relay.TupleGetItem(func_3662_call(), 0)
func_2292_call = mod.get_global_var('func_2292')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_4506 = func_2292_call()
call_4507 = func_2292_call()
output = relay.Tuple([call_4488,call_4492,var_4493,var_4494,call_4504,call_4506,])
output2 = relay.Tuple([call_4489,call_4495,var_4493,var_4494,call_4505,call_4507,])
func_4514 = relay.Function([var_4493,var_4494,], output)
mod['func_4514'] = func_4514
mod = relay.transform.InferType()(mod)
var_4515 = relay.var("var_4515", dtype = "float32", shape = (336,))#candidate|4515|(336,)|var|float32
var_4516 = relay.var("var_4516", dtype = "uint16", shape = (1344,))#candidate|4516|(1344,)|var|uint16
output = func_4514(var_4515,var_4516,)
func_4517 = relay.Function([var_4515,var_4516,], output)
mutated_mod['func_4517'] = func_4517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3744_call = mod.get_global_var('func_3744')
func_3746_call = mutated_mod.get_global_var('func_3746')
call_4524 = relay.TupleGetItem(func_3744_call(), 0)
call_4525 = relay.TupleGetItem(func_3746_call(), 0)
output = call_4524
output2 = call_4525
func_4537 = relay.Function([], output)
mod['func_4537'] = func_4537
mod = relay.transform.InferType()(mod)
mutated_mod['func_4537'] = func_4537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mutated_mod.get_global_var('func_4537')
call_4538 = func_4537_call()
output = call_4538
func_4539 = relay.Function([], output)
mutated_mod['func_4539'] = func_4539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4042_call = mod.get_global_var('func_4042')
func_4044_call = mutated_mod.get_global_var('func_4044')
call_4561 = func_4042_call()
call_4562 = func_4042_call()
output = relay.Tuple([call_4561,])
output2 = relay.Tuple([call_4562,])
func_4570 = relay.Function([], output)
mod['func_4570'] = func_4570
mod = relay.transform.InferType()(mod)
mutated_mod['func_4570'] = func_4570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4570_call = mutated_mod.get_global_var('func_4570')
call_4571 = func_4570_call()
output = call_4571
func_4572 = relay.Function([], output)
mutated_mod['func_4572'] = func_4572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_627_call = mod.get_global_var('func_627')
func_629_call = mutated_mod.get_global_var('func_629')
call_4612 = relay.TupleGetItem(func_627_call(), 0)
call_4613 = relay.TupleGetItem(func_629_call(), 0)
var_4614 = relay.var("var_4614", dtype = "bool", shape = (3, 8, 5))#candidate|4614|(3, 8, 5)|var|bool
bop_4615 = relay.less_equal(call_4612.astype('bool'), var_4614.astype('bool')) # shape=(3, 8, 5)
bop_4618 = relay.less_equal(call_4613.astype('bool'), var_4614.astype('bool')) # shape=(3, 8, 5)
func_3799_call = mod.get_global_var('func_3799')
func_3802_call = mutated_mod.get_global_var('func_3802')
const_4623 = relay.const(-0.238527, dtype = "float32")#candidate|4623|()|const|float32
var_4624 = relay.var("var_4624", dtype = "float32", shape = (462,))#candidate|4624|(462,)|var|float32
call_4622 = relay.TupleGetItem(func_3799_call(relay.reshape(const_4623.astype('float32'), []), relay.reshape(var_4624.astype('float32'), [3, 11, 14]), ), 0)
call_4625 = relay.TupleGetItem(func_3802_call(relay.reshape(const_4623.astype('float32'), []), relay.reshape(var_4624.astype('float32'), [3, 11, 14]), ), 0)
func_3733_call = mod.get_global_var('func_3733')
func_3735_call = mutated_mod.get_global_var('func_3735')
call_4627 = func_3733_call()
call_4628 = func_3733_call()
output = relay.Tuple([bop_4615,call_4622,const_4623,var_4624,call_4627,])
output2 = relay.Tuple([bop_4618,call_4625,const_4623,var_4624,call_4628,])
func_4629 = relay.Function([var_4614,var_4624,], output)
mod['func_4629'] = func_4629
mod = relay.transform.InferType()(mod)
mutated_mod['func_4629'] = func_4629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4629_call = mutated_mod.get_global_var('func_4629')
var_4631 = relay.var("var_4631", dtype = "bool", shape = (3, 8, 5))#candidate|4631|(3, 8, 5)|var|bool
var_4632 = relay.var("var_4632", dtype = "float32", shape = (462,))#candidate|4632|(462,)|var|float32
call_4630 = func_4629_call(var_4631,var_4632,)
output = call_4630
func_4633 = relay.Function([var_4631,var_4632,], output)
mutated_mod['func_4633'] = func_4633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mod.get_global_var('func_4537')
func_4539_call = mutated_mod.get_global_var('func_4539')
call_4689 = func_4537_call()
call_4690 = func_4537_call()
var_4697 = relay.var("var_4697", dtype = "bool", shape = (4, 36))#candidate|4697|(4, 36)|var|bool
bop_4698 = relay.logical_or(call_4689.astype('bool'), relay.reshape(var_4697.astype('bool'), relay.shape_of(call_4689))) # shape=(4, 36)
bop_4701 = relay.logical_or(call_4690.astype('bool'), relay.reshape(var_4697.astype('bool'), relay.shape_of(call_4690))) # shape=(4, 36)
func_3485_call = mod.get_global_var('func_3485')
func_3487_call = mutated_mod.get_global_var('func_3487')
const_4703 = relay.const([-0.318014,0.402625,7.966404,-2.076860,3.485759,9.151693,4.338789,3.175247,-8.812696,-1.583956,2.287581,1.040475,-9.609932,9.879318,-4.005078,-0.479191,9.151911,-3.397476,8.394754,-2.664629,-4.062728,-0.950423,7.525479,8.926255,-9.614533,-5.592390,-5.807279,3.090312,-9.918563,-0.168760,6.758742,5.947299,-4.973535,1.779229,-8.037164,-7.892926,-9.988707,-3.962476,-5.574333,0.056721,5.409558,-0.982752,-8.639411,4.047178,-4.898247,6.101535,-7.268764,0.470301,-0.314688,-8.791192,-9.975495,5.891844,0.278214,8.737882,7.517927,-1.773653,-3.628522,-1.600766,-4.470641,2.756810,6.871456,7.969235,7.000823,-4.747125,2.728807,-9.346563,1.524448,-0.894142,1.824940,-3.416558,1.683263,-1.291680,-7.139290,-0.848456,-0.444807,5.042489,-3.053154,3.259047,4.631829,-0.352883,-5.898659,2.639724,-2.662280,6.822896,3.152548,8.740552,-9.953906,-4.987471,-2.559497,-0.587468,-6.946750,2.158904,-9.650223,-7.349355,-7.703394,-3.531948,0.222005,8.157699,-6.444135,6.933589,-8.536322,-4.022940,-3.033553,1.633211,8.990278,6.593615,-8.361426,-3.221871,1.420283,-9.866880,3.258327,6.273297,-5.961106,3.489113,5.024681,-9.671328,0.652257,-8.854872,7.501802,-3.206717,3.160575,-7.441817,-1.154928,-0.926089,2.934557,-3.926502,-1.494759,1.353411,-3.750550,9.263615,-9.304297,5.759334,-6.601346,4.704977,-3.730660,-6.315783,-6.900086,7.695449,9.673390,-6.923178,-7.371609,-5.689261,-4.138379,-0.937049,-2.016717,-4.181711,9.181573,-7.908542,-8.097711,-6.273864,5.126459,-3.477022,0.201843,1.120655,-1.223231,-6.931877,-7.290607,6.649296,-1.905438,8.969124,4.072549,2.812844,6.759810,-7.858504,-7.302977,-3.264845,0.723210,2.378134,-3.978014,5.833152,-7.446770,-3.330973,-2.396687,-8.710581,6.155155,7.896123,3.172744,7.305353,-3.047437,-8.700593,-1.023058,1.719473,-8.072666,5.328933,2.072872,8.937279,-8.890826,-6.517553,9.189365,4.789157,-5.197923,6.958794,-3.239077,-0.361568,-8.176197,7.742110,-6.752798,-1.672906,9.042285,3.446854,-5.147227,-1.633463,-1.032949,-8.157683,6.003858,-8.055783,-2.667329,-3.594248,1.642250,-1.188878,3.348038,-8.225060,-1.758363,-7.888871,-9.061391,-4.547578,-9.810329,6.383730,2.275004,-0.513316,-4.754841,-1.341393,-1.413317,7.736038,1.669668,8.735488,8.181792,-1.612355,-8.748420,9.257276,7.114404,-3.483981,-2.875034,-0.094617,7.306102,8.112031,-0.884682,-3.269696,-3.202226,-6.782781,4.019363,-0.692821,7.050721,-4.322317,-4.094769,5.841771,1.652512,8.080879,8.353545,6.488385,7.507492,-5.824621,-6.223750,-2.669070,-1.984598,4.894813,4.867716,-6.790482,-6.126060,-3.910962,-4.489758,-3.117560,9.626390,-3.629281,-1.878046,3.040824,-1.137453,0.211001,6.939353,5.779371,-9.409935,5.777922,-3.195119,-6.939822,4.502718,9.557044,-8.741418,2.021896,-6.436662,2.498656,-2.445848,-3.096191,-8.881491,8.345882,0.403773,-7.045593,5.028481,4.818618,4.377299,6.084527,2.040885,5.140380,-9.153739,7.940057,-6.542007,6.266065,-9.454388,3.620237,6.526734,-6.138135,0.210351,-3.477991,-1.904822,-4.760732,-1.794078,-7.477089,3.651391,8.220028,5.820770,-9.561233,6.806147,-9.977181,7.780285,3.398332,-8.423486,6.540455,-4.899005,7.238425,-4.015148,-3.469037,7.482327,-4.420047,-3.878257,-6.411760,-3.646574,9.214872,8.291662,4.492448,5.598700,9.000185,-1.346772,8.701375,8.408041,-9.779477,8.917249,-5.762142,9.773542,9.007875,-2.253549,4.071059,-4.530654,3.661444,-4.313024,-1.229802,4.662014,-7.644052,-8.299906,-1.674463,-8.566399,7.765059,7.476715,-8.310630,-8.362164,5.724822,0.586665,-2.699393,4.031366,4.029726,-8.365267,-3.929457,-0.559847,-8.525869,-5.838908,-3.105027,6.709054,-2.755785,3.389870,2.091902,-4.242466,-1.453439,-6.337633,5.250766,-2.089697,7.716881,-5.649647,-6.489900,-4.410026,-2.068705,2.492575,9.795272,-6.838154,-2.244432,-8.370869,-2.541940], dtype = "float32")#candidate|4703|(384,)|const|float32
call_4702 = relay.TupleGetItem(func_3485_call(relay.reshape(const_4703.astype('float32'), [3, 8, 16])), 1)
call_4704 = relay.TupleGetItem(func_3487_call(relay.reshape(const_4703.astype('float32'), [3, 8, 16])), 1)
func_2652_call = mod.get_global_var('func_2652')
func_2654_call = mutated_mod.get_global_var('func_2654')
call_4706 = relay.TupleGetItem(func_2652_call(), 0)
call_4707 = relay.TupleGetItem(func_2654_call(), 0)
bop_4713 = relay.logical_xor(bop_4698.astype('int32'), relay.reshape(var_4697.astype('int32'), relay.shape_of(bop_4698))) # shape=(4, 36)
bop_4716 = relay.logical_xor(bop_4701.astype('int32'), relay.reshape(var_4697.astype('int32'), relay.shape_of(bop_4701))) # shape=(4, 36)
output = relay.Tuple([call_4702,const_4703,call_4706,bop_4713,])
output2 = relay.Tuple([call_4704,const_4703,call_4707,bop_4716,])
func_4734 = relay.Function([var_4697,], output)
mod['func_4734'] = func_4734
mod = relay.transform.InferType()(mod)
mutated_mod['func_4734'] = func_4734
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4735 = relay.var("var_4735", dtype = "bool", shape = (4, 36))#candidate|4735|(4, 36)|var|bool
func_4734_call = mutated_mod.get_global_var('func_4734')
call_4736 = func_4734_call(var_4735)
output = call_4736
func_4737 = relay.Function([var_4735], output)
mutated_mod['func_4737'] = func_4737
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4778 = relay.var("var_4778", dtype = "float64", shape = (13, 16, 13))#candidate|4778|(13, 16, 13)|var|float64
uop_4779 = relay.asin(var_4778.astype('float64')) # shape=(13, 16, 13)
uop_4784 = relay.acosh(uop_4779.astype('float64')) # shape=(13, 16, 13)
func_3676_call = mod.get_global_var('func_3676')
func_3679_call = mutated_mod.get_global_var('func_3679')
var_4799 = relay.var("var_4799", dtype = "bool", shape = (144,))#candidate|4799|(144,)|var|bool
call_4798 = relay.TupleGetItem(func_3676_call(relay.reshape(var_4799.astype('bool'), [1, 144])), 2)
call_4800 = relay.TupleGetItem(func_3679_call(relay.reshape(var_4799.astype('bool'), [1, 144])), 2)
output = relay.Tuple([uop_4784,call_4798,var_4799,])
output2 = relay.Tuple([uop_4784,call_4800,var_4799,])
func_4802 = relay.Function([var_4778,var_4799,], output)
mod['func_4802'] = func_4802
mod = relay.transform.InferType()(mod)
var_4803 = relay.var("var_4803", dtype = "float64", shape = (13, 16, 13))#candidate|4803|(13, 16, 13)|var|float64
var_4804 = relay.var("var_4804", dtype = "bool", shape = (144,))#candidate|4804|(144,)|var|bool
output = func_4802(var_4803,var_4804,)
func_4805 = relay.Function([var_4803,var_4804,], output)
mutated_mod['func_4805'] = func_4805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_4815 = func_2271_call()
call_4816 = func_2271_call()
output = call_4815
output2 = call_4816
func_4823 = relay.Function([], output)
mod['func_4823'] = func_4823
mod = relay.transform.InferType()(mod)
mutated_mod['func_4823'] = func_4823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4823_call = mutated_mod.get_global_var('func_4823')
call_4824 = func_4823_call()
output = call_4824
func_4825 = relay.Function([], output)
mutated_mod['func_4825'] = func_4825
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4847 = relay.const([[[2.673898],[-5.903174],[3.172490],[8.056304],[-3.206444],[-4.665583],[-3.431866]],[[-8.460743],[4.654587],[-4.983318],[3.044574],[-5.738548],[-1.172901],[-1.201195]],[[-7.561672],[2.120631],[-9.219001],[-0.410696],[-6.857544],[-3.424733],[0.820293]],[[-8.129530],[-5.220305],[-9.034966],[3.336333],[8.657997],[8.014155],[1.746947]],[[8.683878],[6.900527],[-8.772478],[7.375346],[-4.637053],[-1.343800],[-1.559441]],[[9.622925],[-8.214359],[0.154623],[4.626963],[-1.537274],[-5.818667],[8.488179]],[[-1.858825],[2.591670],[-7.954634],[1.270939],[1.114990],[3.021129],[-1.211791]],[[-2.223138],[-0.515537],[-4.576073],[-9.558912],[-2.115637],[-6.963082],[-7.792654]],[[-8.863008],[-2.126258],[5.197882],[2.381668],[2.719515],[-1.638917],[5.788860]],[[-8.513829],[6.796713],[-5.772793],[8.995003],[-6.763980],[-0.363021],[2.107732]],[[-5.285870],[3.952264],[2.303979],[1.906281],[-2.051480],[-7.874203],[0.279158]],[[-8.379975],[-5.709452],[-1.676633],[-3.913526],[-9.089474],[-9.944936],[6.450686]],[[2.621327],[4.322815],[-9.512583],[-2.401032],[-4.470820],[-4.248085],[-0.637950]],[[-9.608243],[5.254656],[0.192229],[-0.819076],[-4.847012],[-6.504206],[-5.195668]],[[1.399001],[-0.540497],[-8.376025],[-9.076410],[-9.433062],[-8.115328],[-9.675954]]], dtype = "float32")#candidate|4847|(15, 7, 1)|const|float32
uop_4848 = relay.sqrt(const_4847.astype('float32')) # shape=(15, 7, 1)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_4852 = relay.TupleGetItem(func_354_call(), 1)
call_4853 = relay.TupleGetItem(func_356_call(), 1)
var_4860 = relay.var("var_4860", dtype = "float32", shape = (3, 8, 16))#candidate|4860|(3, 8, 16)|var|float32
bop_4861 = relay.maximum(call_4852.astype('float64'), relay.reshape(var_4860.astype('float64'), relay.shape_of(call_4852))) # shape=(3, 8, 16)
bop_4864 = relay.maximum(call_4853.astype('float64'), relay.reshape(var_4860.astype('float64'), relay.shape_of(call_4853))) # shape=(3, 8, 16)
func_4211_call = mod.get_global_var('func_4211')
func_4214_call = mutated_mod.get_global_var('func_4214')
const_4869 = relay.const([[-9.207800,-4.657105,-8.542481,4.682244,8.946445,2.627577,6.474845,-2.769578,7.516255,-6.900206,9.215407,-0.468154,7.133829,-6.384954,-7.764398,-6.681805,2.638318,-6.839542,3.675217,-3.109352,5.423403,-0.468925,-5.583428,-2.933811,1.143134,-9.843360,-7.193043,5.273181,5.097478,1.823522,-7.056569,-7.286749,2.457405,7.932080,0.694721,6.124781,9.294350,4.611188,-0.744272,0.288143,9.246287,-2.457414,-9.164991,1.156917,-0.412177,-8.833322,-2.858315,-1.422175,7.895288,-2.087805,6.031979,7.517468,2.100311,-1.305878,-7.607347,-3.596186,-7.298663,2.722276,-0.721613,-3.829819,-5.922036,6.748342,2.612040,-0.406743,4.509391,2.358595,-5.845042,-0.435437,-8.774791,-1.631366,-5.703212,-3.456766,4.362345,-0.504682,-8.923855,-4.340524,6.144910,-9.875196,7.245668,4.507999,2.106510,-0.656170,9.312291,-4.999222,0.506894,6.707519,9.274126,-4.143945,7.186653,-0.206664,1.718210,-3.370488,8.891978,-5.319324,5.834389,0.584890,-3.769517,6.722155,-1.813232,3.209141,-7.102599,-7.765010,-0.236285,-2.631787,7.995655,-7.813783,-6.978493,5.217550,6.298877,-3.084242,8.513207,7.232845,2.233747,1.259335,-1.857295,-5.778358,5.030116,-2.961123,3.930892,-4.452625,-2.219659,-4.564150,4.245542,-9.782975,9.202544,-1.843711,-2.151912,-0.946299,-2.549038,-8.950910,7.732692,7.523484,5.740581,-7.286996,-7.795456,4.964300,8.962596,6.762644,8.953452,9.807342,7.985987,1.676240,-2.639611,7.719860,0.742534,1.215608,-9.509340,-5.747633,7.447044,6.154405,8.458232,-8.915596,-0.289419,8.864058,0.283769,-7.110181,-5.879493,-5.703025,7.014474,0.372470,4.497690,3.641485,2.119803,1.906078,1.701524,9.399588,4.308088,7.977680,5.887928,2.486239,-2.954617,9.621674,8.904843,2.560230,-6.814179,-5.868704,5.726843,2.926115,2.541680,8.118102,9.318744,7.114094,-4.075287,-4.398107,1.927910,-1.192377,9.931169,7.087000,-0.687970,-7.351648,6.371529,-9.792839,-2.799401,-1.292733,1.169246,-5.740115,-8.008076,0.998445,6.587935,-1.940066,-6.589184,-9.835438,3.266326,-3.566855,-7.508202,-2.196654,6.583637,-8.616601,-6.575596,5.196080,2.528297,6.917426,3.980043,-5.597141,-1.149614,-9.971659,-8.539965,7.444997,-9.989646,2.276766,-7.454765,-6.160897,-6.414155,4.897696,8.455710,-3.840387,7.043788,-9.393186,1.358094,1.672460,-9.013141,-7.020254,-8.471606,-3.516641,8.439854,4.706785,2.944766,-1.075065,-8.756966,-8.464509,-5.268731,-1.079755,-3.715343,2.805885,-5.360324,-6.602593,-4.635523,3.603343,-0.326702,8.087606,9.656376,4.221550,-9.526684,-7.734636,7.429668,1.778693,-1.639392,3.399496,-8.102986,-3.650901,5.089424,8.979244,2.566380,-5.797267]], dtype = "float32")#candidate|4869|(1, 264)|const|float32
call_4868 = relay.TupleGetItem(func_4211_call(relay.reshape(const_4869.astype('float32'), [3, 8, 11])), 0)
call_4870 = relay.TupleGetItem(func_4214_call(relay.reshape(const_4869.astype('float32'), [3, 8, 11])), 0)
func_3953_call = mod.get_global_var('func_3953')
func_3956_call = mutated_mod.get_global_var('func_3956')
var_4872 = relay.var("var_4872", dtype = "float32", shape = (10, 64))#candidate|4872|(10, 64)|var|float32
call_4871 = relay.TupleGetItem(func_3953_call(relay.reshape(var_4872.astype('float32'), [8, 5, 16])), 0)
call_4873 = relay.TupleGetItem(func_3956_call(relay.reshape(var_4872.astype('float32'), [8, 5, 16])), 0)
output = relay.Tuple([uop_4848,bop_4861,call_4868,const_4869,call_4871,var_4872,])
output2 = relay.Tuple([uop_4848,bop_4864,call_4870,const_4869,call_4873,var_4872,])
func_4877 = relay.Function([var_4860,var_4872,], output)
mod['func_4877'] = func_4877
mod = relay.transform.InferType()(mod)
var_4878 = relay.var("var_4878", dtype = "float32", shape = (3, 8, 16))#candidate|4878|(3, 8, 16)|var|float32
var_4879 = relay.var("var_4879", dtype = "float32", shape = (10, 64))#candidate|4879|(10, 64)|var|float32
output = func_4877(var_4878,var_4879,)
func_4880 = relay.Function([var_4878,var_4879,], output)
mutated_mod['func_4880'] = func_4880
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4888 = relay.var("var_4888", dtype = "uint8", shape = ())#candidate|4888|()|var|uint8
var_4889 = relay.var("var_4889", dtype = "uint8", shape = (7, 7, 15))#candidate|4889|(7, 7, 15)|var|uint8
bop_4890 = relay.right_shift(var_4888.astype('uint8'), var_4889.astype('uint8')) # shape=(7, 7, 15)
output = bop_4890
output2 = bop_4890
func_4894 = relay.Function([var_4888,var_4889,], output)
mod['func_4894'] = func_4894
mod = relay.transform.InferType()(mod)
mutated_mod['func_4894'] = func_4894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4894_call = mutated_mod.get_global_var('func_4894')
var_4896 = relay.var("var_4896", dtype = "uint8", shape = ())#candidate|4896|()|var|uint8
var_4897 = relay.var("var_4897", dtype = "uint8", shape = (7, 7, 15))#candidate|4897|(7, 7, 15)|var|uint8
call_4895 = func_4894_call(var_4896,var_4897,)
output = call_4895
func_4898 = relay.Function([var_4896,var_4897,], output)
mutated_mod['func_4898'] = func_4898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_4983 = relay.TupleGetItem(func_354_call(), 1)
call_4984 = relay.TupleGetItem(func_356_call(), 1)
func_3953_call = mod.get_global_var('func_3953')
func_3956_call = mutated_mod.get_global_var('func_3956')
var_5021 = relay.var("var_5021", dtype = "float32", shape = (640,))#candidate|5021|(640,)|var|float32
call_5020 = relay.TupleGetItem(func_3953_call(relay.reshape(var_5021.astype('float32'), [8, 5, 16])), 0)
call_5022 = relay.TupleGetItem(func_3956_call(relay.reshape(var_5021.astype('float32'), [8, 5, 16])), 0)
output = relay.Tuple([call_4983,call_5020,var_5021,])
output2 = relay.Tuple([call_4984,call_5022,var_5021,])
func_5023 = relay.Function([var_5021,], output)
mod['func_5023'] = func_5023
mod = relay.transform.InferType()(mod)
var_5024 = relay.var("var_5024", dtype = "float32", shape = (640,))#candidate|5024|(640,)|var|float32
output = func_5023(var_5024)
func_5025 = relay.Function([var_5024], output)
mutated_mod['func_5025'] = func_5025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3164_call = mod.get_global_var('func_3164')
func_3165_call = mutated_mod.get_global_var('func_3165')
call_5038 = func_3164_call()
call_5039 = func_3164_call()
func_1000_call = mod.get_global_var('func_1000')
func_1003_call = mutated_mod.get_global_var('func_1003')
var_5058 = relay.var("var_5058", dtype = "bool", shape = (144,))#candidate|5058|(144,)|var|bool
call_5057 = relay.TupleGetItem(func_1000_call(relay.reshape(var_5058.astype('bool'), [3, 8, 6])), 0)
call_5059 = relay.TupleGetItem(func_1003_call(relay.reshape(var_5058.astype('bool'), [3, 8, 6])), 0)
func_3846_call = mod.get_global_var('func_3846')
func_3847_call = mutated_mod.get_global_var('func_3847')
call_5069 = func_3846_call()
call_5070 = func_3846_call()
func_4363_call = mod.get_global_var('func_4363')
func_4367_call = mutated_mod.get_global_var('func_4367')
const_5072 = relay.const([9.686587,3.978373,1.602220,-7.238353,-8.734711,-4.649656,8.161409,-1.109166,4.022622,-1.298282,-4.008105,-0.123561,3.494683,-1.459081,0.953632,6.103399,9.511820,2.317474,-1.851978,2.587054,3.706823,6.674804,4.114577,-5.525076,0.113200,6.241842,4.454570,-0.267567,1.686679,4.663944,-4.749360,4.667814,1.031261,-4.159965,-2.760381,-2.842244,-7.911345,0.657483,9.733733,-5.146537,-6.431323,-4.044254,1.567905,-6.793988,4.907167,4.526541,-1.231328,-2.271484,-5.322463,-9.850857,-4.308313,-4.931847,-4.319157,1.543286,-4.506455,-9.460478,4.115111,-8.701057,0.941913,8.096894,-1.260950,-6.542539,5.625442,-6.521669,-4.540900,-9.758373,1.940871,5.798782,-7.882549,7.707737,-8.865661,5.753845,-3.634827,7.087502,9.522946,5.448365,8.476048,-9.272163,-4.952712,-7.120643,0.542635,5.459632,-8.241327,-8.073330,5.447091,0.706455,-6.951277,4.233476,-6.250047,-8.056336,4.692235,3.276386,-7.563634,8.690335,-6.461787,4.490746,2.815578,-1.037639,8.373371,-7.922960,-4.064991,-7.245517,5.538716,6.567353,-9.001615,3.915222,5.278053,5.963327,-6.997243,-5.202818,-3.627515,5.710954,2.249845,0.049702,-4.142850,5.096609,1.129214,6.204144,-9.093933,-5.494509,6.793216,-0.445266,-9.889504,-6.630883,6.304376,6.008865,-6.459249,4.166651], dtype = "float32")#candidate|5072|(128,)|const|float32
var_5073 = relay.var("var_5073", dtype = "bool", shape = (4, 24))#candidate|5073|(4, 24)|var|bool
const_5074 = relay.const([-4.269960,-6.494195,6.928113,-9.846052,-1.820252,4.185901,-0.108780,-2.287715,-6.869942,-3.805535,-0.659147,6.742508,9.961933,-2.872519,9.346291,-4.638465,6.110284,4.201095,-0.651860,1.572553,-0.692869,9.437469,5.759164,1.446809,-2.257539,9.496481,-7.825895,6.534291,-7.109759,5.422107,7.067611,-1.484170,-3.412760,4.373106,9.256241,4.868224,6.864130,-1.671061,-7.690605,4.772071,7.616200,3.100913,3.040468,-8.520638,9.716402,5.070292,4.748597,4.616645,3.962655,-6.344916,8.216838,9.350898,-6.811444,4.449384,9.007885,9.585966,3.463795,-2.259956,0.028288,9.486684,-6.764351,1.231202,-2.242037,5.557773,-6.235147,-9.898977,-2.854136,-6.428830,-5.027859,1.957899,-2.517472,-9.846551,-8.336406,-6.738640,1.993006,-8.448495,2.942902,2.325457,-9.709423,3.474591,-5.633166,8.968064,7.666260,8.646168,9.098794,2.872046,3.123767,-5.346869,9.918139,3.897332,-1.742090,-9.215847,-0.156717,2.455573,5.316991,7.857859,-2.808844,-7.332077,-6.567319,4.045439,-7.222260,-9.595758,2.581935,2.402503,1.932700,2.242336,-2.013345,4.206994,-8.458703,-3.497467,-8.429803,5.678051,-3.414687,-2.286268,-2.398344,-8.345971,9.891060,-0.662587,9.945062,9.979334,8.905805,-5.804223,-7.254683,-0.086727,-0.495754,-0.957247,-3.254863,-7.098084,3.230589,3.586156,-2.040493,1.678610,-3.363582,-0.751150,2.325410,5.444301,6.880516,3.353019,5.634742,-0.749931,-3.555657,-7.203717,-9.254510,1.914992,-0.268532,9.769792,-2.760652,-9.473523,1.112951,0.406653,-1.577664,9.909135,-7.992918,7.748202,-9.667599,-4.447699,2.958087,7.461818,8.074090,6.233084,1.078742,-3.457217,0.364985,8.663335,-1.774129,-9.927181,2.941139,-7.629553,-1.630013,8.248455,9.624697,3.399450,5.349927,-4.641668,0.310425,-9.046699,3.092350,-7.209975,4.942242,8.130752,-7.687024,-7.989656,1.992026,-4.586894,-2.662901,-0.229880,8.770178,-4.243397,-0.340678,9.191938,5.949744,-3.565340,-9.778003,4.951441,-1.739936,6.214875,-6.860945,-2.361704,-1.183522,1.863373,1.461525,-0.142480,6.019131,7.859087,-6.410798,6.553976,-5.833066,-2.932505,0.286737,-7.651523,-8.463118,-3.463014,1.562460,-1.438882,8.224420,-2.722055,7.163874,7.259761,-2.834087,-9.963259,7.291070,-5.756289,0.343622,7.502164,-5.845655,8.043045,7.534044,-8.089021,-3.360364,6.846267,-9.443625,-1.802385,-1.885228,3.283634,-1.086468,6.343823,6.367858,2.566336,-0.716932,3.060981,-0.186337,4.698985,5.931027,-8.293972,-7.429586,1.854246,-2.643877,-8.263209,-3.492518,1.689985,3.477458,-2.774226,-4.719881,-6.685761,-6.696012,1.923502], dtype = "float32")#candidate|5074|(256,)|const|float32
call_5071 = relay.TupleGetItem(func_4363_call(relay.reshape(const_5072.astype('float32'), [128, 1]), relay.reshape(var_5073.astype('bool'), [48, 2]), relay.reshape(const_5074.astype('float32'), [128, 2]), ), 1)
call_5075 = relay.TupleGetItem(func_4367_call(relay.reshape(const_5072.astype('float32'), [128, 1]), relay.reshape(var_5073.astype('bool'), [48, 2]), relay.reshape(const_5074.astype('float32'), [128, 2]), ), 1)
func_3485_call = mod.get_global_var('func_3485')
func_3487_call = mutated_mod.get_global_var('func_3487')
call_5083 = relay.TupleGetItem(func_3485_call(relay.reshape(call_5069.astype('float32'), [3, 8, 16])), 0)
call_5084 = relay.TupleGetItem(func_3487_call(relay.reshape(call_5069.astype('float32'), [3, 8, 16])), 0)
output = relay.Tuple([call_5038,call_5057,var_5058,call_5069,call_5071,const_5072,var_5073,const_5074,call_5083,])
output2 = relay.Tuple([call_5039,call_5059,var_5058,call_5070,call_5075,const_5072,var_5073,const_5074,call_5084,])
func_5091 = relay.Function([var_5058,var_5073,], output)
mod['func_5091'] = func_5091
mod = relay.transform.InferType()(mod)
mutated_mod['func_5091'] = func_5091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5091_call = mutated_mod.get_global_var('func_5091')
var_5093 = relay.var("var_5093", dtype = "bool", shape = (144,))#candidate|5093|(144,)|var|bool
var_5094 = relay.var("var_5094", dtype = "bool", shape = (4, 24))#candidate|5094|(4, 24)|var|bool
call_5092 = func_5091_call(var_5093,var_5094,)
output = call_5092
func_5095 = relay.Function([var_5093,var_5094,], output)
mutated_mod['func_5095'] = func_5095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4042_call = mod.get_global_var('func_4042')
func_4044_call = mutated_mod.get_global_var('func_4044')
call_5103 = func_4042_call()
call_5104 = func_4042_call()
output = relay.Tuple([call_5103,])
output2 = relay.Tuple([call_5104,])
func_5108 = relay.Function([], output)
mod['func_5108'] = func_5108
mod = relay.transform.InferType()(mod)
output = func_5108()
func_5109 = relay.Function([], output)
mutated_mod['func_5109'] = func_5109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_5141 = relay.TupleGetItem(func_3977_call(), 0)
call_5142 = relay.TupleGetItem(func_3979_call(), 0)
output = call_5141
output2 = call_5142
func_5143 = relay.Function([], output)
mod['func_5143'] = func_5143
mod = relay.transform.InferType()(mod)
output = func_5143()
func_5144 = relay.Function([], output)
mutated_mod['func_5144'] = func_5144
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5174 = relay.const([[[1,7,4,3,5,-10,5,9],[-10,-4,5,-7,-3,-2,3,-5],[7,-10,-7,1,-7,6,-4,1],[-5,7,7,2,4,-2,-7,3]],[[-8,-5,6,-6,8,4,-8,-5],[2,-2,-7,-8,10,8,-7,-3],[6,10,3,-6,10,2,6,3],[-1,-4,1,9,-4,-1,8,5]],[[-2,-7,-3,-6,4,4,-5,-8],[4,-5,6,8,-1,-8,-5,-4],[-10,-1,-5,-7,-5,6,8,8],[-6,6,-7,1,-3,6,3,-4]],[[2,-7,4,-3,-5,-1,-5,-4],[2,-4,-4,6,5,5,3,-3],[5,-1,6,-8,-4,-3,-7,-3],[-8,-5,-3,2,-2,-8,-6,-9]],[[2,10,5,8,-6,-2,9,10],[-2,2,8,5,-2,-5,5,9],[-8,-7,6,4,-6,3,-10,7],[-9,-7,-4,7,5,-4,9,-10]],[[-2,-8,2,-8,-8,8,-5,-2],[-5,-3,1,-4,-3,-1,-10,7],[-9,8,-9,-4,9,-7,-8,-1],[7,-1,-4,-9,1,-9,-10,-3]],[[-3,2,9,-1,7,-5,6,-7],[7,-5,1,8,-3,-5,3,-4],[10,8,-2,-10,-6,6,-8,-9],[1,8,6,-5,2,2,7,2]],[[1,-7,-1,-4,1,-1,2,-3],[-1,-6,6,-8,1,-4,7,4],[-5,1,-9,3,4,6,-3,3],[-2,5,-2,6,4,-2,5,-8]],[[-8,-4,-5,-4,2,-7,2,1],[10,-4,10,6,10,-4,3,-3],[3,7,-8,-7,2,5,5,-10],[5,-7,-3,-8,10,-8,-6,-3]],[[10,-6,-2,9,8,-10,4,-10],[-3,2,2,7,-4,5,5,8],[10,6,-9,-6,10,2,5,3],[-10,1,6,6,-4,9,-8,7]]], dtype = "uint64")#candidate|5174|(10, 4, 8)|const|uint64
var_5175 = relay.var("var_5175", dtype = "uint64", shape = (10, 4, 8))#candidate|5175|(10, 4, 8)|var|uint64
bop_5176 = relay.greater_equal(const_5174.astype('bool'), relay.reshape(var_5175.astype('bool'), relay.shape_of(const_5174))) # shape=(10, 4, 8)
func_2873_call = mod.get_global_var('func_2873')
func_2875_call = mutated_mod.get_global_var('func_2875')
call_5180 = func_2873_call()
call_5181 = func_2873_call()
uop_5205 = relay.sin(call_5180.astype('float64')) # shape=(3, 8, 16)
uop_5207 = relay.sin(call_5181.astype('float64')) # shape=(3, 8, 16)
func_4234_call = mod.get_global_var('func_4234')
func_4235_call = mutated_mod.get_global_var('func_4235')
call_5211 = func_4234_call()
call_5212 = func_4234_call()
output = relay.Tuple([bop_5176,uop_5205,call_5211,])
output2 = relay.Tuple([bop_5176,uop_5207,call_5212,])
func_5214 = relay.Function([var_5175,], output)
mod['func_5214'] = func_5214
mod = relay.transform.InferType()(mod)
var_5215 = relay.var("var_5215", dtype = "uint64", shape = (10, 4, 8))#candidate|5215|(10, 4, 8)|var|uint64
output = func_5214(var_5215)
func_5216 = relay.Function([var_5215], output)
mutated_mod['func_5216'] = func_5216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2123_call = mod.get_global_var('func_2123')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_5240 = relay.TupleGetItem(func_2123_call(), 0)
call_5241 = relay.TupleGetItem(func_2124_call(), 0)
uop_5242 = relay.rsqrt(call_5240.astype('float32')) # shape=(3, 8, 1)
uop_5244 = relay.rsqrt(call_5241.astype('float32')) # shape=(3, 8, 1)
output = uop_5242
output2 = uop_5244
func_5247 = relay.Function([], output)
mod['func_5247'] = func_5247
mod = relay.transform.InferType()(mod)
mutated_mod['func_5247'] = func_5247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5247_call = mutated_mod.get_global_var('func_5247')
call_5248 = func_5247_call()
output = call_5248
func_5249 = relay.Function([], output)
mutated_mod['func_5249'] = func_5249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2397_call = mod.get_global_var('func_2397')
func_2399_call = mutated_mod.get_global_var('func_2399')
call_5263 = relay.TupleGetItem(func_2397_call(), 0)
call_5264 = relay.TupleGetItem(func_2399_call(), 0)
output = relay.Tuple([call_5263,])
output2 = relay.Tuple([call_5264,])
func_5275 = relay.Function([], output)
mod['func_5275'] = func_5275
mod = relay.transform.InferType()(mod)
mutated_mod['func_5275'] = func_5275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5275_call = mutated_mod.get_global_var('func_5275')
call_5276 = func_5275_call()
output = call_5276
func_5277 = relay.Function([], output)
mutated_mod['func_5277'] = func_5277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mod.get_global_var('func_4537')
func_4539_call = mutated_mod.get_global_var('func_4539')
call_5356 = func_4537_call()
call_5357 = func_4537_call()
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_5362 = relay.TupleGetItem(func_791_call(), 0)
call_5363 = relay.TupleGetItem(func_792_call(), 0)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_5381 = relay.TupleGetItem(func_791_call(), 0)
call_5382 = relay.TupleGetItem(func_792_call(), 0)
func_820_call = mod.get_global_var('func_820')
func_821_call = mutated_mod.get_global_var('func_821')
call_5393 = relay.TupleGetItem(func_820_call(), 1)
call_5394 = relay.TupleGetItem(func_821_call(), 1)
bop_5396 = relay.right_shift(call_5381.astype('uint16'), relay.reshape(call_5362.astype('uint16'), relay.shape_of(call_5381))) # shape=(3, 8, 1)
bop_5399 = relay.right_shift(call_5382.astype('uint16'), relay.reshape(call_5363.astype('uint16'), relay.shape_of(call_5382))) # shape=(3, 8, 1)
uop_5402 = relay.cos(call_5356.astype('float64')) # shape=(4, 36)
uop_5404 = relay.cos(call_5357.astype('float64')) # shape=(4, 36)
uop_5406 = relay.sinh(call_5393.astype('float64')) # shape=(3, 8, 1)
uop_5408 = relay.sinh(call_5394.astype('float64')) # shape=(3, 8, 1)
bop_5409 = relay.power(bop_5396.astype('float64'), relay.reshape(call_5381.astype('float64'), relay.shape_of(bop_5396))) # shape=(3, 8, 1)
bop_5412 = relay.power(bop_5399.astype('float64'), relay.reshape(call_5382.astype('float64'), relay.shape_of(bop_5399))) # shape=(3, 8, 1)
output = relay.Tuple([uop_5402,uop_5406,bop_5409,])
output2 = relay.Tuple([uop_5404,uop_5408,bop_5412,])
func_5415 = relay.Function([], output)
mod['func_5415'] = func_5415
mod = relay.transform.InferType()(mod)
output = func_5415()
func_5416 = relay.Function([], output)
mutated_mod['func_5416'] = func_5416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5415_call = mod.get_global_var('func_5415')
func_5416_call = mutated_mod.get_global_var('func_5416')
call_5431 = relay.TupleGetItem(func_5415_call(), 2)
call_5432 = relay.TupleGetItem(func_5416_call(), 2)
output = relay.Tuple([call_5431,])
output2 = relay.Tuple([call_5432,])
func_5436 = relay.Function([], output)
mod['func_5436'] = func_5436
mod = relay.transform.InferType()(mod)
output = func_5436()
func_5437 = relay.Function([], output)
mutated_mod['func_5437'] = func_5437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_5438 = func_2271_call()
call_5439 = func_2271_call()
const_5445 = relay.const([[[-8,9,-8,-2,-6,5,2,-10,-8,7,-9,-8,7,4,10,5],[-3,-5,5,-4,-6,-4,8,7,-8,-9,-5,10,7,-5,-1,4],[-7,7,-8,-2,1,-3,9,4,6,-2,2,-3,7,-7,-8,-4],[-2,8,3,4,-7,-2,-7,-6,10,4,-2,-3,6,-9,1,-1],[6,4,-9,-3,5,5,-2,7,-8,5,9,-1,10,-9,-3,5],[-2,-9,7,-9,9,-6,-4,-4,5,4,-9,-9,7,9,2,1],[1,5,2,-2,-10,4,3,-8,-7,-4,-1,5,-3,-10,-8,-9],[1,-9,-1,-5,-1,-5,-7,3,-9,-2,10,-10,2,1,1,9]],[[5,-6,-8,7,2,-4,-7,4,-5,-10,-4,9,-10,-5,10,2],[1,2,-1,-1,-3,1,-3,7,9,-3,8,8,4,-9,-9,-2],[1,2,-4,-2,-1,6,7,-1,3,-9,10,6,-5,10,8,-2],[5,10,8,-6,-6,-2,8,-7,-1,-1,-8,-7,-4,4,-9,10],[4,-5,3,-3,6,9,-1,6,-7,-7,7,-7,-10,-4,1,3],[5,8,-9,-6,6,-10,4,-3,4,5,1,-2,-4,8,-2,1],[-8,5,1,2,-7,-6,-10,-1,8,-6,7,-2,6,-10,-2,8],[-1,-7,6,-10,2,5,7,-6,9,4,4,1,-5,-10,10,-6]],[[3,-3,-3,-4,-9,6,-3,10,8,2,-9,4,1,-2,-6,-4],[-2,-9,-2,-9,-2,-8,1,10,2,-3,-2,7,-5,-6,9,-9],[9,-5,3,-1,-1,3,-4,1,-5,-9,3,10,-6,8,-8,-4],[9,5,3,6,-4,-4,-1,6,-1,-3,-2,-4,-1,4,3,6],[9,-1,-9,6,9,-4,9,6,-7,-6,-4,-9,-5,6,-5,10],[-6,-6,-2,-8,4,-1,2,-3,-6,9,-1,7,-3,6,5,-2],[6,4,2,-9,4,1,7,6,-5,5,5,-4,5,6,5,-9],[-8,1,6,10,9,-5,-5,10,-6,-10,7,9,3,9,5,-10]]], dtype = "uint16")#candidate|5445|(3, 8, 16)|const|uint16
bop_5446 = relay.bitwise_or(call_5438.astype('uint8'), relay.reshape(const_5445.astype('uint8'), relay.shape_of(call_5438))) # shape=(3, 8, 16)
bop_5449 = relay.bitwise_or(call_5439.astype('uint8'), relay.reshape(const_5445.astype('uint8'), relay.shape_of(call_5439))) # shape=(3, 8, 16)
func_2389_call = mod.get_global_var('func_2389')
func_2392_call = mutated_mod.get_global_var('func_2392')
const_5467 = relay.const([[-9.802682,-2.395004],[-3.677068,-6.663870],[-1.878297,6.747358],[-0.477967,2.075909],[-6.494478,-9.406844],[0.875578,4.170820],[0.694964,-8.425140],[8.912325,-7.170618],[-3.521913,-7.913141],[-2.697418,-4.416774],[-7.426496,-8.374064],[-3.340694,9.607833],[1.165619,-9.434249],[4.028056,-9.864587],[-3.361273,-5.779579],[-2.529432,5.575583],[5.637893,3.644818],[-2.022811,1.927458],[4.629142,9.651773],[0.180000,-1.365089],[-8.268509,2.114646],[7.350048,-1.841433],[8.263310,0.374523],[-0.842290,-8.326535],[-3.287266,1.940575],[4.383446,9.278050],[2.773352,-3.751722],[8.037948,1.974714],[9.919131,4.702428],[-9.231723,-9.646511],[-5.951470,9.514016],[8.930183,2.474317],[2.592101,-8.769632],[9.380087,-6.008901],[8.923610,1.151705],[1.499471,-1.710460],[-3.357971,2.043805],[-1.841434,-8.483518],[8.954919,5.863098],[4.591787,-6.661792],[5.816396,5.809553],[4.945474,5.138198],[3.178023,6.428310],[5.132357,9.949334],[-4.972104,-4.483990],[0.941385,2.109979],[-4.425549,2.875146],[9.771609,2.749578],[-4.753847,6.826648],[-9.406416,-4.484240],[-9.846692,-3.792332],[-8.023166,5.699517],[1.173948,9.302325],[-1.421635,1.704588],[7.940735,-3.708536],[1.204152,2.856797],[-6.758332,4.051765],[-0.557282,-8.378323],[9.155351,-5.545598],[1.407589,-4.300689],[-5.233270,6.355899],[3.242856,5.482994],[5.710503,0.420539],[8.240726,-6.868475],[-4.023425,-3.426599],[-3.503063,5.248740],[-3.135783,5.051838],[8.678287,-8.775876],[7.135650,-2.571955],[-9.105322,9.339375],[5.102274,-5.768323],[8.426915,-6.466662],[-0.970844,-5.023197],[-3.103212,5.472473],[-1.146060,-3.313316],[-3.266069,6.702594],[-9.438942,-0.083530],[8.710261,-2.883056],[5.035789,-5.036441],[7.646817,-6.639860],[4.591358,-1.559892],[-6.317653,-5.947747],[-2.410601,-1.915151],[0.525246,-2.886056],[3.458487,1.714418],[-6.610331,2.725592],[-1.217679,1.639915],[-4.975546,-7.162378],[-8.300511,3.721679],[-7.433580,5.822221],[-7.118751,5.026222],[4.395085,7.076094],[2.554338,-9.260583],[-6.410519,4.696065],[6.085359,8.044888],[-0.432337,9.492368],[-9.919449,2.873047],[7.112834,-0.670223],[-5.914093,0.707196],[8.992328,-6.978152],[6.939930,4.017831],[-4.085292,8.393267],[7.373791,9.993000],[-2.671705,-0.830468],[-5.247989,8.086084],[6.100190,1.559548],[4.143513,9.074681],[-2.831323,7.110493],[-7.275519,5.639301],[0.259637,-7.683239],[3.376745,-5.929104],[6.842188,0.919692],[-1.993960,3.994882],[-3.457887,0.312848],[6.370560,-6.814216],[-7.519101,-8.852564],[-6.958682,7.576073],[-8.307726,-7.863286],[-4.109408,9.110530],[-3.802861,7.785892],[5.023974,-1.274086],[7.892267,0.739058],[-5.479082,-5.629058],[-9.460999,-1.639242],[4.027209,-2.075168],[9.650672,0.268975],[-4.304602,2.079354],[2.007319,7.190206],[0.734919,-3.364158],[-7.577096,-4.018566],[-0.642113,0.876274],[3.301880,6.401705]], dtype = "float32")#candidate|5467|(132, 2)|const|float32
call_5466 = relay.TupleGetItem(func_2389_call(relay.reshape(const_5467.astype('float32'), [3, 8, 11])), 1)
call_5468 = relay.TupleGetItem(func_2392_call(relay.reshape(const_5467.astype('float32'), [3, 8, 11])), 1)
func_3676_call = mod.get_global_var('func_3676')
func_3679_call = mutated_mod.get_global_var('func_3679')
const_5488 = relay.const([True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,True], dtype = "bool")#candidate|5488|(144,)|const|bool
call_5487 = relay.TupleGetItem(func_3676_call(relay.reshape(const_5488.astype('bool'), [1, 144])), 0)
call_5489 = relay.TupleGetItem(func_3679_call(relay.reshape(const_5488.astype('bool'), [1, 144])), 0)
output = relay.Tuple([bop_5446,call_5466,const_5467,call_5487,const_5488,])
output2 = relay.Tuple([bop_5449,call_5468,const_5467,call_5489,const_5488,])
func_5490 = relay.Function([], output)
mod['func_5490'] = func_5490
mod = relay.transform.InferType()(mod)
mutated_mod['func_5490'] = func_5490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5490_call = mutated_mod.get_global_var('func_5490')
call_5491 = func_5490_call()
output = call_5491
func_5492 = relay.Function([], output)
mutated_mod['func_5492'] = func_5492
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5551 = relay.const([[[7,2,3,6,-3,3,5,-8],[-6,-4,1,9,-7,2,4,-7],[-1,-4,8,-6,-9,8,-6,6],[-1,-6,-10,-2,-10,6,-8,3],[-3,4,9,2,-1,-3,9,9],[-10,4,-10,8,3,-3,8,-10],[5,2,-4,-3,7,1,5,-5],[5,-8,6,-4,-1,-7,3,2],[1,-3,10,-9,-1,-2,10,-3]],[[9,-9,-1,-3,10,-3,-9,-2],[-9,-5,-8,-6,3,-5,-7,8],[-4,-2,-10,7,-7,4,3,6],[8,1,-6,-4,6,1,-2,3],[4,8,10,-5,-4,-3,-4,1],[2,7,-10,6,4,3,-6,1],[10,5,5,-9,8,7,2,-3],[3,-2,-5,-1,6,5,10,4],[-3,4,-9,-8,4,1,5,-10]],[[-4,-1,1,-7,10,10,6,-2],[1,9,-6,8,-4,5,3,-10],[-8,-7,7,-7,-6,4,9,4],[-3,-1,-2,10,10,-7,-1,-1],[10,-9,3,-1,-10,-4,-5,10],[-3,-7,-2,3,2,-4,-9,-3],[4,-5,7,6,2,-8,-8,5],[7,-6,-10,-10,9,7,-10,6],[-4,9,-6,9,-6,-7,5,-6]],[[5,-1,3,7,-7,9,-5,-1],[7,-10,-6,-4,-8,-9,-4,-5],[-6,-4,-10,-10,-5,6,7,1],[-9,8,-2,10,-3,2,3,-4],[4,10,9,4,-3,6,-8,-4],[7,-6,4,10,-4,-3,-10,8],[7,1,-1,9,-3,-4,1,-2],[9,9,4,1,4,7,-2,-9],[4,-4,2,9,-8,10,8,-8]],[[-10,2,-8,1,6,-5,4,9],[3,5,5,-3,-4,2,5,-10],[-7,-6,-5,7,7,-2,-8,-1],[2,-6,-7,-2,2,-2,4,-1],[-6,7,5,3,-8,5,5,8],[-9,6,5,-6,4,5,1,8],[-2,9,1,-3,6,-8,3,2],[-10,7,-8,4,4,7,-5,3],[2,-7,3,-5,-8,-1,8,-3]],[[2,6,5,-2,-1,-4,-6,4],[-8,-4,-2,9,-1,-9,6,9],[-1,9,-7,7,-2,4,8,7],[-2,-7,1,2,-10,2,4,3],[-6,-3,3,-3,-1,-2,-9,-4],[-3,5,9,-5,10,-3,9,-2],[-10,10,-5,10,-1,4,5,-1],[9,10,3,6,-3,8,7,-6],[4,-2,-8,4,7,1,6,-8]],[[-6,-4,4,-2,9,10,9,4],[-2,2,-1,3,-4,9,4,6],[6,1,-10,-10,5,8,5,-7],[10,-1,6,10,6,-2,7,-4],[-10,6,10,-2,5,8,1,9],[5,-2,-3,2,2,-2,4,5],[-1,-7,-6,-5,-6,-2,-6,-10],[-2,3,7,-7,-1,-9,4,-2],[-4,7,5,-2,3,-2,9,-4]],[[-4,-8,-4,1,3,2,-5,-6],[3,-10,5,1,-10,-1,-5,-9],[1,10,-2,3,-1,5,-1,-5],[-4,5,9,-9,1,7,4,2],[3,5,3,3,4,1,10,-2],[-3,6,-2,-10,-7,-8,-4,6],[-4,-5,10,-4,7,-2,1,1],[-2,7,-4,-9,-5,9,9,7],[8,-2,-9,5,-2,-2,2,9]],[[2,7,3,6,3,5,5,-5],[5,3,4,1,4,10,-9,-7],[-5,7,-2,-3,-10,-9,4,8],[-1,-3,-7,-2,-8,-7,3,7],[10,-3,-9,-9,9,-2,2,-10],[10,-10,10,10,-8,6,-10,-7],[-9,5,9,6,2,8,-9,8],[4,8,4,3,-6,-1,-3,9],[9,1,7,-5,-5,-4,-5,-4]],[[2,4,-2,6,-7,-6,-5,2],[8,3,1,8,-5,10,5,-1],[-8,1,-4,-9,3,-1,10,-4],[7,6,9,5,6,-6,-1,-8],[-3,-2,5,10,-7,-8,-4,-5],[-4,-2,7,-9,-3,4,1,7],[-10,-3,-10,-2,-3,4,-3,-2],[-2,-9,2,-3,-2,-10,-8,9],[8,2,-6,-5,-5,8,-7,-6]],[[-3,-9,-5,-1,-9,2,-10,7],[4,5,4,-8,-6,8,7,4],[2,-6,-4,-4,7,-2,8,6],[9,-1,-1,3,-7,3,-8,3],[-8,5,-5,-7,-6,9,10,-5],[7,3,8,5,8,7,-5,-6],[-9,-7,9,-7,6,-10,-3,5],[-2,8,-6,-3,-5,2,1,2],[-6,-4,-6,-3,-7,9,7,-10]]], dtype = "int32")#candidate|5551|(11, 9, 8)|const|int32
var_5552 = relay.var("var_5552", dtype = "int32", shape = (11, 9, 8))#candidate|5552|(11, 9, 8)|var|int32
bop_5553 = relay.minimum(const_5551.astype('int32'), relay.reshape(var_5552.astype('int32'), relay.shape_of(const_5551))) # shape=(11, 9, 8)
uop_5556 = relay.log(var_5552.astype('float32')) # shape=(11, 9, 8)
uop_5560 = relay.acosh(var_5552.astype('float32')) # shape=(11, 9, 8)
func_3835_call = mod.get_global_var('func_3835')
func_3838_call = mutated_mod.get_global_var('func_3838')
const_5571 = relay.const([[False,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True],[True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,True],[True,True,False,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,True,False],[True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True],[True,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,False,False,True],[False,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True]], dtype = "bool")#candidate|5571|(6, 20)|const|bool
call_5570 = relay.TupleGetItem(func_3835_call(relay.reshape(const_5571.astype('bool'), [3, 8, 5])), 0)
call_5572 = relay.TupleGetItem(func_3838_call(relay.reshape(const_5571.astype('bool'), [3, 8, 5])), 0)
func_2471_call = mod.get_global_var('func_2471')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_5574 = relay.TupleGetItem(func_2471_call(), 0)
call_5575 = relay.TupleGetItem(func_2473_call(), 0)
output = relay.Tuple([bop_5553,uop_5556,uop_5560,call_5570,const_5571,call_5574,])
output2 = relay.Tuple([bop_5553,uop_5556,uop_5560,call_5572,const_5571,call_5575,])
func_5579 = relay.Function([var_5552,], output)
mod['func_5579'] = func_5579
mod = relay.transform.InferType()(mod)
var_5580 = relay.var("var_5580", dtype = "int32", shape = (11, 9, 8))#candidate|5580|(11, 9, 8)|var|int32
output = func_5579(var_5580)
func_5581 = relay.Function([var_5580], output)
mutated_mod['func_5581'] = func_5581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mod.get_global_var('func_4158')
func_4159_call = mutated_mod.get_global_var('func_4159')
call_5598 = relay.TupleGetItem(func_4158_call(), 0)
call_5599 = relay.TupleGetItem(func_4159_call(), 0)
output = call_5598
output2 = call_5599
func_5616 = relay.Function([], output)
mod['func_5616'] = func_5616
mod = relay.transform.InferType()(mod)
output = func_5616()
func_5617 = relay.Function([], output)
mutated_mod['func_5617'] = func_5617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2622_call = mod.get_global_var('func_2622')
func_2624_call = mutated_mod.get_global_var('func_2624')
call_5650 = relay.TupleGetItem(func_2622_call(), 0)
call_5651 = relay.TupleGetItem(func_2624_call(), 0)
func_5091_call = mod.get_global_var('func_5091')
func_5095_call = mutated_mod.get_global_var('func_5095')
var_5656 = relay.var("var_5656", dtype = "bool", shape = (144,))#candidate|5656|(144,)|var|bool
var_5657 = relay.var("var_5657", dtype = "bool", shape = (96,))#candidate|5657|(96,)|var|bool
call_5655 = relay.TupleGetItem(func_5091_call(relay.reshape(var_5656.astype('bool'), [144,]), relay.reshape(var_5657.astype('bool'), [4, 24]), ), 1)
call_5658 = relay.TupleGetItem(func_5095_call(relay.reshape(var_5656.astype('bool'), [144,]), relay.reshape(var_5657.astype('bool'), [4, 24]), ), 1)
output = relay.Tuple([call_5650,call_5655,var_5656,var_5657,])
output2 = relay.Tuple([call_5651,call_5658,var_5656,var_5657,])
func_5659 = relay.Function([var_5656,var_5657,], output)
mod['func_5659'] = func_5659
mod = relay.transform.InferType()(mod)
var_5660 = relay.var("var_5660", dtype = "bool", shape = (144,))#candidate|5660|(144,)|var|bool
var_5661 = relay.var("var_5661", dtype = "bool", shape = (96,))#candidate|5661|(96,)|var|bool
output = func_5659(var_5660,var_5661,)
func_5662 = relay.Function([var_5660,var_5661,], output)
mutated_mod['func_5662'] = func_5662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_5697 = relay.TupleGetItem(func_1823_call(), 0)
call_5698 = relay.TupleGetItem(func_1825_call(), 0)
output = relay.Tuple([call_5697,])
output2 = relay.Tuple([call_5698,])
func_5710 = relay.Function([], output)
mod['func_5710'] = func_5710
mod = relay.transform.InferType()(mod)
mutated_mod['func_5710'] = func_5710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5710_call = mutated_mod.get_global_var('func_5710')
call_5711 = func_5710_call()
output = call_5711
func_5712 = relay.Function([], output)
mutated_mod['func_5712'] = func_5712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_5731 = relay.TupleGetItem(func_1940_call(), 0)
call_5732 = relay.TupleGetItem(func_1941_call(), 0)
output = call_5731
output2 = call_5732
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
func_2292_call = mod.get_global_var('func_2292')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_5766 = func_2292_call()
call_5767 = func_2292_call()
uop_5785 = relay.erf(call_5766.astype('float32')) # shape=(3, 8, 1)
uop_5787 = relay.erf(call_5767.astype('float32')) # shape=(3, 8, 1)
bop_5793 = relay.bitwise_or(call_5766.astype('int32'), relay.reshape(uop_5785.astype('int32'), relay.shape_of(call_5766))) # shape=(3, 8, 1)
bop_5796 = relay.bitwise_or(call_5767.astype('int32'), relay.reshape(uop_5787.astype('int32'), relay.shape_of(call_5767))) # shape=(3, 8, 1)
func_282_call = mod.get_global_var('func_282')
func_284_call = mutated_mod.get_global_var('func_284')
call_5797 = func_282_call()
call_5798 = func_282_call()
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_5813 = relay.TupleGetItem(func_791_call(), 0)
call_5814 = relay.TupleGetItem(func_792_call(), 0)
output = relay.Tuple([bop_5793,call_5797,call_5813,])
output2 = relay.Tuple([bop_5796,call_5798,call_5814,])
func_5815 = relay.Function([], output)
mod['func_5815'] = func_5815
mod = relay.transform.InferType()(mod)
mutated_mod['func_5815'] = func_5815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5815_call = mutated_mod.get_global_var('func_5815')
call_5816 = func_5815_call()
output = call_5816
func_5817 = relay.Function([], output)
mutated_mod['func_5817'] = func_5817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_5853 = relay.TupleGetItem(func_791_call(), 0)
call_5854 = relay.TupleGetItem(func_792_call(), 0)
func_2109_call = mod.get_global_var('func_2109')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_5856 = func_2109_call()
call_5857 = func_2109_call()
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_5860 = relay.TupleGetItem(func_1940_call(), 1)
call_5861 = relay.TupleGetItem(func_1941_call(), 1)
output = relay.Tuple([call_5853,call_5856,call_5860,])
output2 = relay.Tuple([call_5854,call_5857,call_5861,])
func_5892 = relay.Function([], output)
mod['func_5892'] = func_5892
mod = relay.transform.InferType()(mod)
output = func_5892()
func_5893 = relay.Function([], output)
mutated_mod['func_5893'] = func_5893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3164_call = mod.get_global_var('func_3164')
func_3165_call = mutated_mod.get_global_var('func_3165')
call_5897 = func_3164_call()
call_5898 = func_3164_call()
func_5490_call = mod.get_global_var('func_5490')
func_5492_call = mutated_mod.get_global_var('func_5492')
call_5900 = relay.TupleGetItem(func_5490_call(), 4)
call_5901 = relay.TupleGetItem(func_5492_call(), 4)
func_5490_call = mod.get_global_var('func_5490')
func_5492_call = mutated_mod.get_global_var('func_5492')
call_5909 = relay.TupleGetItem(func_5490_call(), 2)
call_5910 = relay.TupleGetItem(func_5492_call(), 2)
func_5275_call = mod.get_global_var('func_5275')
func_5277_call = mutated_mod.get_global_var('func_5277')
call_5911 = relay.TupleGetItem(func_5275_call(), 0)
call_5912 = relay.TupleGetItem(func_5277_call(), 0)
func_4894_call = mod.get_global_var('func_4894')
func_4898_call = mutated_mod.get_global_var('func_4898')
var_5933 = relay.var("var_5933", dtype = "uint8", shape = ())#candidate|5933|()|var|uint8
const_5934 = relay.const([[7,-9,4,-9,6,-6,-10,5,8,7,5,8,7,-6,6],[-2,-5,-8,-7,-2,7,-1,6,2,2,-3,-3,4,3,-1],[-10,-1,-4,-4,8,-3,3,-3,-9,-2,-8,9,8,-3,5],[-1,7,-8,1,-1,9,5,7,10,6,-7,6,6,-1,-6],[-1,1,-7,8,-2,-8,-4,-2,2,4,-1,2,9,3,5],[8,4,-7,-10,-2,5,-3,4,7,-7,-4,6,-8,-2,-4],[-10,-6,-2,7,7,4,9,8,-7,9,-7,-4,9,-5,5],[-9,-4,9,-7,9,6,-3,-5,10,5,5,4,-5,3,3],[3,-1,8,-4,6,8,-9,9,-1,5,10,-10,-9,-7,-6],[8,-6,-6,-1,-9,8,-1,8,2,-10,-7,-4,7,1,6],[8,-7,-7,9,7,-6,-3,1,-8,-1,7,1,5,7,-3],[5,6,-6,-9,10,-10,9,3,7,1,2,-7,1,2,-2],[-10,-8,1,9,8,-5,8,-6,-4,-4,2,-4,10,1,-3],[1,-9,10,-5,-1,-2,5,-10,3,-3,-8,-5,-4,-8,-9],[7,4,10,-10,-5,-2,-7,7,8,-9,6,-8,10,8,-6],[-8,-8,2,6,-7,-3,6,-5,-5,-2,6,4,9,-5,-3],[-3,-5,-3,10,-9,10,5,-9,-10,5,-1,-10,-4,-10,-7],[9,3,-2,1,8,9,9,8,4,4,-2,10,-1,-2,-3],[-5,-2,6,-7,-5,4,-6,8,3,-2,1,4,-7,-6,-8],[-9,-1,1,4,-2,-4,-3,-3,4,2,3,-1,7,-3,-8],[-1,-6,-7,-10,7,-2,-10,1,7,-9,3,-4,-2,2,-3],[-8,9,-7,-1,9,-8,-8,7,4,-7,5,-7,-6,-2,-4],[-1,9,8,-6,2,-8,-8,3,-10,-9,9,8,-3,-5,-7],[9,-3,7,4,-2,-1,-1,9,-4,10,-5,-7,5,9,4],[10,3,-2,7,-6,-4,-9,5,8,6,-3,7,4,-10,5],[-7,7,-10,-10,5,-6,-2,6,5,-1,4,-2,3,-4,-8],[-7,3,5,-3,2,1,-10,5,4,-10,10,8,4,7,6],[-8,-10,-9,6,-2,-1,-8,-9,7,-4,-8,-10,8,10,3],[-3,-9,3,10,9,8,4,-10,-1,-6,-3,-9,3,-8,-5],[8,-3,-10,6,-6,1,-6,-1,10,3,-7,2,-9,3,9],[10,7,6,-2,7,-7,3,7,-10,-8,-5,-9,-10,4,-8],[3,-2,-3,-8,-1,2,-5,-1,-1,-9,4,-1,-1,-3,-6],[7,1,8,8,-1,-2,8,2,-10,-10,1,5,1,4,-10],[-5,8,8,1,3,-6,-9,-2,4,1,5,2,-5,-3,-4],[-7,-1,6,4,-7,3,2,8,10,-10,-7,-4,-4,-9,8],[-1,6,-4,3,-2,-5,-4,7,-2,5,10,6,1,3,-8],[-7,7,-1,6,9,6,4,-10,3,8,6,10,-3,4,2],[6,1,1,-6,-7,6,6,3,-9,-10,6,6,-7,-6,-5],[-3,8,-8,-5,7,-7,3,-10,-1,-5,-9,-6,9,-6,-6],[-5,-3,10,-3,4,-7,2,-6,8,-5,-10,-6,-9,-10,9],[-5,-5,-9,-10,10,-4,-6,-8,-3,2,1,-2,8,3,-6],[6,-9,2,3,-4,-7,-1,7,7,-6,-9,3,-8,-3,-1],[-5,2,5,6,7,3,8,-7,3,-6,5,10,5,8,-8],[8,-5,1,-8,10,-5,-9,8,10,2,-2,1,6,1,5],[5,5,8,2,3,1,-4,4,8,3,8,-8,9,-5,10],[-10,-5,-6,2,-7,7,-6,-8,-1,4,8,-1,-1,2,1],[-7,-8,-7,-5,10,8,2,8,-4,-6,-3,10,-3,-4,-8],[7,-5,10,-9,3,-1,-7,-4,-2,-4,-7,-5,2,-8,2],[-9,-5,-6,-8,-2,-2,-9,7,-4,2,-9,6,7,-3,2]], dtype = "uint8")#candidate|5934|(49, 15)|const|uint8
call_5932 = func_4894_call(relay.reshape(var_5933.astype('uint8'), []), relay.reshape(const_5934.astype('uint8'), [7, 7, 15]), )
call_5935 = func_4894_call(relay.reshape(var_5933.astype('uint8'), []), relay.reshape(const_5934.astype('uint8'), [7, 7, 15]), )
func_5616_call = mod.get_global_var('func_5616')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_5950 = func_5616_call()
call_5951 = func_5616_call()
output = relay.Tuple([call_5897,call_5900,call_5909,call_5911,call_5932,var_5933,const_5934,call_5950,])
output2 = relay.Tuple([call_5898,call_5901,call_5910,call_5912,call_5935,var_5933,const_5934,call_5951,])
func_5960 = relay.Function([var_5933,], output)
mod['func_5960'] = func_5960
mod = relay.transform.InferType()(mod)
mutated_mod['func_5960'] = func_5960
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5961 = relay.var("var_5961", dtype = "uint8", shape = ())#candidate|5961|()|var|uint8
func_5960_call = mutated_mod.get_global_var('func_5960')
call_5962 = func_5960_call(var_5961)
output = call_5962
func_5963 = relay.Function([var_5961], output)
mutated_mod['func_5963'] = func_5963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3005_call = mod.get_global_var('func_3005')
func_3007_call = mutated_mod.get_global_var('func_3007')
call_5975 = relay.TupleGetItem(func_3005_call(), 0)
call_5976 = relay.TupleGetItem(func_3007_call(), 0)
output = relay.Tuple([call_5975,])
output2 = relay.Tuple([call_5976,])
func_6002 = relay.Function([], output)
mod['func_6002'] = func_6002
mod = relay.transform.InferType()(mod)
output = func_6002()
func_6003 = relay.Function([], output)
mutated_mod['func_6003'] = func_6003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mod.get_global_var('func_2031')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_6037 = relay.TupleGetItem(func_2031_call(), 1)
call_6038 = relay.TupleGetItem(func_2032_call(), 1)
var_6041 = relay.var("var_6041", dtype = "float32", shape = (3, 8, 16))#candidate|6041|(3, 8, 16)|var|float32
bop_6042 = relay.less(call_6037.astype('bool'), relay.reshape(var_6041.astype('bool'), relay.shape_of(call_6037))) # shape=(3, 8, 16)
bop_6045 = relay.less(call_6038.astype('bool'), relay.reshape(var_6041.astype('bool'), relay.shape_of(call_6038))) # shape=(3, 8, 16)
func_2794_call = mod.get_global_var('func_2794')
func_2797_call = mutated_mod.get_global_var('func_2797')
const_6051 = relay.const([False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True], dtype = "bool")#candidate|6051|(96,)|const|bool
call_6050 = relay.TupleGetItem(func_2794_call(relay.reshape(const_6051.astype('bool'), [3, 8, 4])), 0)
call_6052 = relay.TupleGetItem(func_2797_call(relay.reshape(const_6051.astype('bool'), [3, 8, 4])), 0)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_6053 = relay.TupleGetItem(func_1940_call(), 1)
call_6054 = relay.TupleGetItem(func_1941_call(), 1)
output = relay.Tuple([bop_6042,call_6050,const_6051,call_6053,])
output2 = relay.Tuple([bop_6045,call_6052,const_6051,call_6054,])
func_6058 = relay.Function([var_6041,], output)
mod['func_6058'] = func_6058
mod = relay.transform.InferType()(mod)
mutated_mod['func_6058'] = func_6058
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6059 = relay.var("var_6059", dtype = "float32", shape = (3, 8, 16))#candidate|6059|(3, 8, 16)|var|float32
func_6058_call = mutated_mod.get_global_var('func_6058')
call_6060 = func_6058_call(var_6059)
output = call_6060
func_6061 = relay.Function([var_6059], output)
mutated_mod['func_6061'] = func_6061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2828_call = mod.get_global_var('func_2828')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_6081 = relay.TupleGetItem(func_2828_call(), 1)
call_6082 = relay.TupleGetItem(func_2829_call(), 1)
const_6096 = relay.const([[[True],[False],[True],[True],[True],[False],[True],[True]],[[True],[True],[False],[False],[True],[False],[True],[True]],[[False],[True],[False],[True],[False],[False],[False],[True]]], dtype = "bool")#candidate|6096|(3, 8, 1)|const|bool
bop_6097 = relay.left_shift(call_6081.astype('int16'), relay.reshape(const_6096.astype('int16'), relay.shape_of(call_6081))) # shape=(3, 8, 1)
bop_6100 = relay.left_shift(call_6082.astype('int16'), relay.reshape(const_6096.astype('int16'), relay.shape_of(call_6082))) # shape=(3, 8, 1)
func_5815_call = mod.get_global_var('func_5815')
func_5817_call = mutated_mod.get_global_var('func_5817')
call_6128 = relay.TupleGetItem(func_5815_call(), 1)
call_6129 = relay.TupleGetItem(func_5817_call(), 1)
output = relay.Tuple([bop_6097,call_6128,])
output2 = relay.Tuple([bop_6100,call_6129,])
func_6135 = relay.Function([], output)
mod['func_6135'] = func_6135
mod = relay.transform.InferType()(mod)
output = func_6135()
func_6136 = relay.Function([], output)
mutated_mod['func_6136'] = func_6136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1435_call = mod.get_global_var('func_1435')
func_1437_call = mutated_mod.get_global_var('func_1437')
call_6183 = relay.TupleGetItem(func_1435_call(), 2)
call_6184 = relay.TupleGetItem(func_1437_call(), 2)
output = call_6183
output2 = call_6184
func_6185 = relay.Function([], output)
mod['func_6185'] = func_6185
mod = relay.transform.InferType()(mod)
output = func_6185()
func_6186 = relay.Function([], output)
mutated_mod['func_6186'] = func_6186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1100_call = mod.get_global_var('func_1100')
func_1101_call = mutated_mod.get_global_var('func_1101')
call_6249 = func_1100_call()
call_6250 = func_1100_call()
output = relay.Tuple([call_6249,])
output2 = relay.Tuple([call_6250,])
func_6258 = relay.Function([], output)
mod['func_6258'] = func_6258
mod = relay.transform.InferType()(mod)
output = func_6258()
func_6259 = relay.Function([], output)
mutated_mod['func_6259'] = func_6259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_6265 = relay.TupleGetItem(func_2356_call(), 1)
call_6266 = relay.TupleGetItem(func_2358_call(), 1)
output = call_6265
output2 = call_6266
func_6267 = relay.Function([], output)
mod['func_6267'] = func_6267
mod = relay.transform.InferType()(mod)
output = func_6267()
func_6268 = relay.Function([], output)
mutated_mod['func_6268'] = func_6268
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6293 = relay.var("var_6293", dtype = "int64", shape = (5, 1, 2))#candidate|6293|(5, 1, 2)|var|int64
var_6294 = relay.var("var_6294", dtype = "int64", shape = (5, 7, 2))#candidate|6294|(5, 7, 2)|var|int64
bop_6295 = relay.right_shift(var_6293.astype('int64'), var_6294.astype('int64')) # shape=(5, 7, 2)
const_6327 = relay.const([[[-3,1],[-9,5]],[[10,-9],[3,10]],[[2,-3],[1,3]],[[7,-2],[7,2]],[[10,-2],[-10,2]]], dtype = "int64")#candidate|6327|(5, 2, 2)|const|int64
bop_6328 = relay.right_shift(var_6293.astype('int64'), const_6327.astype('int64')) # shape=(5, 2, 2)
func_2292_call = mod.get_global_var('func_2292')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_6353 = func_2292_call()
call_6354 = func_2292_call()
output = relay.Tuple([bop_6295,bop_6328,call_6353,])
output2 = relay.Tuple([bop_6295,bop_6328,call_6354,])
func_6355 = relay.Function([var_6293,var_6294,], output)
mod['func_6355'] = func_6355
mod = relay.transform.InferType()(mod)
var_6356 = relay.var("var_6356", dtype = "int64", shape = (5, 1, 2))#candidate|6356|(5, 1, 2)|var|int64
var_6357 = relay.var("var_6357", dtype = "int64", shape = (5, 7, 2))#candidate|6357|(5, 7, 2)|var|int64
output = func_6355(var_6356,var_6357,)
func_6358 = relay.Function([var_6356,var_6357,], output)
mutated_mod['func_6358'] = func_6358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5616_call = mod.get_global_var('func_5616')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_6371 = func_5616_call()
call_6372 = func_5616_call()
output = relay.Tuple([call_6371,])
output2 = relay.Tuple([call_6372,])
func_6384 = relay.Function([], output)
mod['func_6384'] = func_6384
mod = relay.transform.InferType()(mod)
mutated_mod['func_6384'] = func_6384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6384_call = mutated_mod.get_global_var('func_6384')
call_6385 = func_6384_call()
output = call_6385
func_6386 = relay.Function([], output)
mutated_mod['func_6386'] = func_6386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5436_call = mod.get_global_var('func_5436')
func_5437_call = mutated_mod.get_global_var('func_5437')
call_6415 = relay.TupleGetItem(func_5436_call(), 0)
call_6416 = relay.TupleGetItem(func_5437_call(), 0)
output = relay.Tuple([call_6415,])
output2 = relay.Tuple([call_6416,])
func_6421 = relay.Function([], output)
mod['func_6421'] = func_6421
mod = relay.transform.InferType()(mod)
output = func_6421()
func_6422 = relay.Function([], output)
mutated_mod['func_6422'] = func_6422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2532_call = mod.get_global_var('func_2532')
func_2534_call = mutated_mod.get_global_var('func_2534')
call_6430 = relay.TupleGetItem(func_2532_call(), 1)
call_6431 = relay.TupleGetItem(func_2534_call(), 1)
uop_6439 = relay.cosh(call_6430.astype('float64')) # shape=(3, 8, 1)
uop_6441 = relay.cosh(call_6431.astype('float64')) # shape=(3, 8, 1)
output = uop_6439
output2 = uop_6441
func_6445 = relay.Function([], output)
mod['func_6445'] = func_6445
mod = relay.transform.InferType()(mod)
mutated_mod['func_6445'] = func_6445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6445_call = mutated_mod.get_global_var('func_6445')
call_6446 = func_6445_call()
output = call_6446
func_6447 = relay.Function([], output)
mutated_mod['func_6447'] = func_6447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2873_call = mod.get_global_var('func_2873')
func_2875_call = mutated_mod.get_global_var('func_2875')
call_6463 = func_2873_call()
call_6464 = func_2873_call()
func_3733_call = mod.get_global_var('func_3733')
func_3735_call = mutated_mod.get_global_var('func_3735')
call_6472 = func_3733_call()
call_6473 = func_3733_call()
output = relay.Tuple([call_6463,call_6472,])
output2 = relay.Tuple([call_6464,call_6473,])
func_6477 = relay.Function([], output)
mod['func_6477'] = func_6477
mod = relay.transform.InferType()(mod)
output = func_6477()
func_6478 = relay.Function([], output)
mutated_mod['func_6478'] = func_6478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_6582 = func_3234_call()
call_6583 = func_3234_call()
output = relay.Tuple([call_6582,])
output2 = relay.Tuple([call_6583,])
func_6597 = relay.Function([], output)
mod['func_6597'] = func_6597
mod = relay.transform.InferType()(mod)
mutated_mod['func_6597'] = func_6597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6597_call = mutated_mod.get_global_var('func_6597')
call_6598 = func_6597_call()
output = call_6598
func_6599 = relay.Function([], output)
mutated_mod['func_6599'] = func_6599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4234_call = mod.get_global_var('func_4234')
func_4235_call = mutated_mod.get_global_var('func_4235')
call_6638 = func_4234_call()
call_6639 = func_4234_call()
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_6640 = func_3234_call()
call_6641 = func_3234_call()
output = relay.Tuple([call_6638,call_6640,])
output2 = relay.Tuple([call_6639,call_6641,])
func_6643 = relay.Function([], output)
mod['func_6643'] = func_6643
mod = relay.transform.InferType()(mod)
output = func_6643()
func_6644 = relay.Function([], output)
mutated_mod['func_6644'] = func_6644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_6661 = func_3183_call()
call_6662 = func_3183_call()
output = relay.Tuple([call_6661,])
output2 = relay.Tuple([call_6662,])
func_6664 = relay.Function([], output)
mod['func_6664'] = func_6664
mod = relay.transform.InferType()(mod)
output = func_6664()
func_6665 = relay.Function([], output)
mutated_mod['func_6665'] = func_6665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5616_call = mod.get_global_var('func_5616')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_6678 = func_5616_call()
call_6679 = func_5616_call()
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_6690 = relay.TupleGetItem(func_2356_call(), 0)
call_6691 = relay.TupleGetItem(func_2358_call(), 0)
func_3017_call = mod.get_global_var('func_3017')
func_3019_call = mutated_mod.get_global_var('func_3019')
call_6703 = relay.TupleGetItem(func_3017_call(), 0)
call_6704 = relay.TupleGetItem(func_3019_call(), 0)
func_5415_call = mod.get_global_var('func_5415')
func_5416_call = mutated_mod.get_global_var('func_5416')
call_6705 = relay.TupleGetItem(func_5415_call(), 2)
call_6706 = relay.TupleGetItem(func_5416_call(), 2)
output = relay.Tuple([call_6678,call_6690,call_6703,call_6705,])
output2 = relay.Tuple([call_6679,call_6691,call_6704,call_6706,])
func_6712 = relay.Function([], output)
mod['func_6712'] = func_6712
mod = relay.transform.InferType()(mod)
output = func_6712()
func_6713 = relay.Function([], output)
mutated_mod['func_6713'] = func_6713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_6716 = relay.TupleGetItem(func_1823_call(), 1)
call_6717 = relay.TupleGetItem(func_1825_call(), 1)
output = relay.Tuple([call_6716,])
output2 = relay.Tuple([call_6717,])
func_6724 = relay.Function([], output)
mod['func_6724'] = func_6724
mod = relay.transform.InferType()(mod)
output = func_6724()
func_6725 = relay.Function([], output)
mutated_mod['func_6725'] = func_6725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_6745 = relay.TupleGetItem(func_3977_call(), 0)
call_6746 = relay.TupleGetItem(func_3979_call(), 0)
func_354_call = mod.get_global_var('func_354')
func_356_call = mutated_mod.get_global_var('func_356')
call_6755 = relay.TupleGetItem(func_354_call(), 0)
call_6756 = relay.TupleGetItem(func_356_call(), 0)
output = relay.Tuple([call_6745,call_6755,])
output2 = relay.Tuple([call_6746,call_6756,])
func_6766 = relay.Function([], output)
mod['func_6766'] = func_6766
mod = relay.transform.InferType()(mod)
output = func_6766()
func_6767 = relay.Function([], output)
mutated_mod['func_6767'] = func_6767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6766_call = mod.get_global_var('func_6766')
func_6767_call = mutated_mod.get_global_var('func_6767')
call_6789 = relay.TupleGetItem(func_6766_call(), 0)
call_6790 = relay.TupleGetItem(func_6767_call(), 0)
output = relay.Tuple([call_6789,])
output2 = relay.Tuple([call_6790,])
func_6793 = relay.Function([], output)
mod['func_6793'] = func_6793
mod = relay.transform.InferType()(mod)
mutated_mod['func_6793'] = func_6793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6793_call = mutated_mod.get_global_var('func_6793')
call_6794 = func_6793_call()
output = call_6794
func_6795 = relay.Function([], output)
mutated_mod['func_6795'] = func_6795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_6831 = relay.TupleGetItem(func_3977_call(), 0)
call_6832 = relay.TupleGetItem(func_3979_call(), 0)
output = relay.Tuple([call_6831,])
output2 = relay.Tuple([call_6832,])
func_6834 = relay.Function([], output)
mod['func_6834'] = func_6834
mod = relay.transform.InferType()(mod)
output = func_6834()
func_6835 = relay.Function([], output)
mutated_mod['func_6835'] = func_6835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3005_call = mod.get_global_var('func_3005')
func_3007_call = mutated_mod.get_global_var('func_3007')
call_6844 = relay.TupleGetItem(func_3005_call(), 0)
call_6845 = relay.TupleGetItem(func_3007_call(), 0)
output = relay.Tuple([call_6844,])
output2 = relay.Tuple([call_6845,])
func_6846 = relay.Function([], output)
mod['func_6846'] = func_6846
mod = relay.transform.InferType()(mod)
output = func_6846()
func_6847 = relay.Function([], output)
mutated_mod['func_6847'] = func_6847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6002_call = mod.get_global_var('func_6002')
func_6003_call = mutated_mod.get_global_var('func_6003')
call_6848 = relay.TupleGetItem(func_6002_call(), 0)
call_6849 = relay.TupleGetItem(func_6003_call(), 0)
func_3636_call = mod.get_global_var('func_3636')
func_3637_call = mutated_mod.get_global_var('func_3637')
call_6868 = relay.TupleGetItem(func_3636_call(), 1)
call_6869 = relay.TupleGetItem(func_3637_call(), 1)
output = relay.Tuple([call_6848,call_6868,])
output2 = relay.Tuple([call_6849,call_6869,])
func_6892 = relay.Function([], output)
mod['func_6892'] = func_6892
mod = relay.transform.InferType()(mod)
output = func_6892()
func_6893 = relay.Function([], output)
mutated_mod['func_6893'] = func_6893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2109_call = mod.get_global_var('func_2109')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_6909 = func_2109_call()
call_6910 = func_2109_call()
func_6002_call = mod.get_global_var('func_6002')
func_6003_call = mutated_mod.get_global_var('func_6003')
call_6932 = relay.TupleGetItem(func_6002_call(), 0)
call_6933 = relay.TupleGetItem(func_6003_call(), 0)
func_1749_call = mod.get_global_var('func_1749')
func_1751_call = mutated_mod.get_global_var('func_1751')
call_6934 = relay.TupleGetItem(func_1749_call(), 1)
call_6935 = relay.TupleGetItem(func_1751_call(), 1)
func_1435_call = mod.get_global_var('func_1435')
func_1437_call = mutated_mod.get_global_var('func_1437')
call_6938 = relay.TupleGetItem(func_1435_call(), 1)
call_6939 = relay.TupleGetItem(func_1437_call(), 1)
output = relay.Tuple([call_6909,call_6932,call_6934,call_6938,])
output2 = relay.Tuple([call_6910,call_6933,call_6935,call_6939,])
func_6951 = relay.Function([], output)
mod['func_6951'] = func_6951
mod = relay.transform.InferType()(mod)
mutated_mod['func_6951'] = func_6951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6951_call = mutated_mod.get_global_var('func_6951')
call_6952 = func_6951_call()
output = call_6952
func_6953 = relay.Function([], output)
mutated_mod['func_6953'] = func_6953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_6974 = func_2271_call()
call_6975 = func_2271_call()
func_3699_call = mod.get_global_var('func_3699')
func_3701_call = mutated_mod.get_global_var('func_3701')
const_6977 = relay.const([-2.305004,9.340201,-9.028672,8.840252,8.409076,8.352161,-2.671989,9.191179,9.843097,-4.087739,7.832205,2.383940,-1.328539,-5.485306,0.033274,-1.598597,-5.357670,4.753487,-4.262483,6.240794,-4.527262,8.489608,-0.509495,8.595743,-0.747562,2.098740,1.233481,2.358897,-4.905020,9.987327,1.825137,1.624449,8.135304,-3.397036,-8.795064,4.306222,7.705367,6.972376,-5.937674,8.270406,0.240908,-6.145287,8.376978,-9.207360,9.111785,9.542772,1.335419,-9.973960,-1.623325,1.561609,-2.510135,1.603650,5.839006,5.300964,-1.680939,0.757522,-9.648714,-1.115390,4.956445,1.581286,3.909749,7.088348,-4.676348,3.121227,0.084909,9.378626,-0.012502,0.380190,9.616725,4.336239,9.519515,4.063924,-3.389835,6.512087,-9.649186,-8.008327,-1.397703,6.007716,9.540477,2.035574,1.733677,-1.732823,9.559631,9.586073,-3.349914,-0.306799,0.977459,4.880006,-3.797996,1.376058,-1.653602,-0.524150,-4.712914,0.657365,-6.864420,-1.977365,6.947524,9.836300,-7.790780,7.320494,3.741039,-4.451800,-6.680861,-2.230963,-2.649988,9.184692,1.164204,4.752156,4.719949,6.161781,3.784099,0.838521,-8.081390,-2.892206,-8.029391,-2.325903,4.957332,-2.603260,-0.241798,-5.286740,6.000581,9.704501,0.372935,-3.557663,7.979354,6.754710,6.092047,0.324873,7.662779,-9.519855,-9.358333,-4.733955,7.921157,3.174423,6.320591,-5.018121,4.214103,-6.613493,2.867873,-8.789777,-5.962284,4.476162,-5.199796,-3.022830,-0.323072,1.031880,1.203549,4.349711,8.047201,-7.327004,-1.314803,6.475096,2.020468,0.689466,-7.342745,9.159400,3.688022,-3.024271,-7.108088,1.805153,4.538678,9.453359,-1.185054,8.138705,4.491820,7.387433,-9.400325,2.925060,-1.156864,-0.089366,-0.043030,1.691634,8.345889,-1.486930,-7.199961,-0.195574,-0.991139,-1.509338,-9.029488,-9.721305,-5.974567,-6.978704,-7.183180,-6.793291,-7.773532,3.202252,-4.739094,-2.261865,-5.383030,8.190948,-5.854721,-4.429450,0.460184,-6.962802,-4.729626,1.164047,-4.622874,-8.949061,-4.402634,6.533737,1.833344,4.141393,2.496056,1.829982,-4.634842,9.255763,9.854399,-2.343701,-1.551052,-5.277055,1.987342,4.144361,1.935895,1.764197,-0.641348,-0.607104,2.748346,-3.805456,7.449382,0.329443,-1.349421,5.557826,-5.606695,4.404310,-2.833339,-7.769199,8.709808,1.301050,7.538543,-5.159835,3.455395,7.742374,1.527957,6.443162,-0.983209,-0.238438,9.454885,-4.620814,4.194138,4.604981,8.769570,-3.453295,2.830055,-2.372384,-8.682063,6.745626,4.755638,-5.922960,-0.244689,-7.767293,-8.479591,3.542557,-6.298520,-2.658604,1.080430,9.928755,0.082680,-3.843835,3.231961,4.216595,4.012986,4.806114,0.732995,4.543894,8.242677,-7.519396,4.657962,-5.541428,4.412344,3.336642,-5.446321,-1.763663,-9.930828,-6.459099,3.563962,3.776522,-5.017172,4.851678,6.616047,3.941795,-1.884149,-1.096944,-8.377835,6.771258,1.976473,-5.855469,1.768014,3.050805,6.035795,6.973484,4.050226,-4.920276,8.367295,-6.205573,-6.079675,-3.972300,0.728133,-5.525982,3.702917,-6.205050,2.099892,-0.497773,7.880134,-3.251413,5.028185,8.931935,7.688879,2.237545,1.770777,7.148972,0.370279,8.148414,-3.570526,-5.050038,0.620577,1.083466,-5.299319,-7.175459,9.803971,-5.516625,-8.067152,-5.185732,7.591068,5.306251,5.268080,1.799421,-9.927906,7.365853,-0.939525,-1.271788,-4.731826,-2.546637,8.778070,-4.307890,-7.955881,6.752027,-2.568096,-2.066646,6.986033,6.483603,-9.414202,-0.081405,7.107994,7.433057,4.781990,7.536837,6.058204,-5.079624,-6.162965,-1.266153,-5.586148,-6.031139,5.918915,-7.237646,-8.817838,3.661386,-2.939221,5.940872,1.922755,-5.326164,-6.642594,2.149747,2.224903,-2.547820,-6.736841,-8.463353,-2.379841,-1.466073,2.213581,8.922035,-8.662694,-1.245418,-9.832168,-8.186853,9.341371,-7.686971,-6.302932,6.491614,-1.987112,-1.540433,-4.795472,4.616420,3.231592,-1.384719,-4.646731,-9.065592,-9.207963,-4.652924,-0.130517,5.093995,1.836517,5.555880,2.041124,8.056981,-0.046013,-3.914080,2.622814,8.689382,8.230209,2.012671,6.979453,-6.464916,0.826471,-1.999960,3.667352,0.044284,-6.018128,3.269822,9.064235,7.548079,-6.467072,7.155234,7.836876,-6.142388,-2.845595,-1.907607,6.792856,-5.319758,1.608027,-0.308676,-9.163107,8.383661,-2.702443,-6.495308,-9.174937,7.992989,1.799300,-3.409977,8.774794,-4.091525,-3.645350,-4.038990,1.191173,-7.883704,1.077096,-8.251621,-0.266508,-6.734346,-0.281149,3.857682,-2.617952,8.549382,6.368580,-1.829341,-9.417744,-7.127981,-7.375181,-0.302591,3.759469,-3.480386,4.507337,-4.453834,8.218109,-7.043153,6.867677,-4.523906,-0.880511,-6.446310,4.543854,-9.399426,8.794695,-6.188389,2.899146,3.216593,-7.115214,-2.140820,-2.647472,2.414684,8.222471,2.679790,1.118250,0.342811,1.167656,7.154362,-2.522279,-2.273423,2.655550,0.148804,1.513439,6.307420,3.454567,1.182264,9.327673,9.399000,-1.109080,0.512398,-5.476012,7.942322,-6.479386,-9.651247,8.217489,-1.923152,9.273221,3.632470,9.291326,-2.875906,-7.946666,-1.754449,1.378671,6.623005,5.410867,6.825670,8.114856,0.071747,-8.278504,-2.872614,2.131042,-1.566307,0.138483,5.721556,-1.142571,5.181428,-7.877149,-9.495693,7.516500,2.845350,3.892166,-9.475043,-3.712152,-4.552694,2.007397,-8.174022,-9.736699,4.079052,-0.970220,-6.994445,6.527113,-8.241498,8.348059,0.660460,-8.149386,7.895612,1.529626,-4.128017,-4.063947,-8.132620,3.755574,-4.637093,6.383848,2.253185,-9.731453,3.949120,6.139880,6.568229,-2.608489,1.979951,-3.232898,-2.385481,-6.451998,1.621809,-1.180485,-9.082676,-6.608539,2.299984,7.866885,3.310873,-0.982955,7.545769,-5.985831,-8.765909,1.508499,2.892767,6.791902,7.412227,-0.246104,-9.151082,9.077487,8.127976,1.359209,5.624123,0.017451,-8.450299,8.974379,-5.280803,2.791193,7.424067,-1.067406,-6.083257,-0.133316,-4.743848,-6.736369,8.166343,0.842278,0.988019,7.408261,4.873247,1.337128,-9.689670,4.140247,1.024683,-6.576544,0.674665,9.420892,-6.611284,-6.057425,2.663476,5.665692,-5.878003,3.321538,8.106723,-8.988570,2.538721,-0.242671,1.635756,-9.261289,-2.218155,1.578956,-3.934910,1.400805,-1.808286,1.201802,-4.734957,0.603336,8.160641,-4.879487,0.590380,-9.087210,7.254869,9.520338,-7.556364,5.318936,-7.803315,2.106020,6.849362,1.190581,-9.411127,6.169353,1.553416,4.595809,4.326206,1.103130,-5.556911,-6.295715,-2.382140,-5.456670,6.752539,-3.569222,-7.936571,-0.182468,-0.860434,-8.718128,-3.446649,-0.393302,-3.460606,9.394276,2.925829,-9.548020,-6.777508,1.249012,-0.866132,2.895903,4.762627,3.976615,0.335755,-2.586712,9.869314,-0.814651,-5.065599,1.248122,-9.470805,2.754226,3.698793,-1.153995,-9.246207,2.658621,1.749892,-2.644871,-3.043336,0.567794,-5.666868,6.538237,-4.582852,4.468151,-8.539805,7.073734,6.848254,9.343301,-6.047620,-8.482229,6.181703,-9.246573,1.101593,-7.766893,-7.728067,3.277043,4.832889,8.075530,3.741608,-7.921167,6.907831,-0.441433,-2.626336,-2.523584,3.496321,6.616318,-0.695272,-9.690670,2.923519,9.024644,-1.713451,-1.844735,7.958038,7.812509,-9.945774,7.735643,4.654506,8.950075,4.699423,-2.918724,-1.352134,2.401753,3.046615,-3.707535,-6.921950,1.778520,9.502771,-8.672545,9.039249,9.145167,-1.538002,4.868898,-5.621397,8.468869,-9.050187,2.410337,-0.829708,9.693311,-6.280879,-8.401902,5.727985,3.335878,1.760672,-6.812179,0.278272,-2.387533,-7.461296,3.108675,-5.953963,-1.619388,-8.554850,-5.582627,-7.807699,2.062974,1.428272,-3.296049,0.727566,1.250066,8.477481,7.504939,5.185379,-6.411194,1.429266,8.111195,3.799850,7.515401,3.670357,-5.806077,4.809616,-9.234032,0.823093,-8.302919,-5.893015,4.023468,7.097544,-1.599437,-4.936039,-3.751623,-9.870267,-7.049974,0.449831,8.582663,3.690123,-6.576560,9.132952,1.384578,6.657501,8.335010,-8.531304,-0.227646,2.754649,-5.831383,5.037332,-5.651958,-6.567383,1.714200,-7.372832,-6.785241,-2.630285,-5.996773,0.395743,-4.712753,1.218069,-7.693560,-2.321033,7.217901,2.832321,-7.044564,-6.131811,-7.953634,5.790461,-2.191520,4.794750,3.596309,-8.885351,6.158896,6.107547,-7.133705,-8.089513,-8.069168,1.985506,-5.729294,-5.739611,-1.192783,2.977616,4.433677,-5.385272,-9.517880,3.642611,-5.496523,-2.822270,6.054623,6.042412,-2.825954,3.139995,8.919424,8.737172,5.669097,-0.434350,-3.270049,7.577939,-5.246921,-7.831714,7.167676,-9.848968,3.572870,8.033307,-8.007740,-3.915308,-4.775659,-5.442059,9.005576,-8.142860,5.126970,-0.862307,-4.319252,6.214231,3.602488,-4.878960,6.694070,-1.673486,3.361073,-1.546441,4.863666,-2.440527,-8.988092,6.846768,-7.101044,-7.228913,-6.103787,-5.393093,-2.414355,4.799267,8.472955,-9.617696,-5.512057,1.342524,0.590558,6.236394,-8.852720,-7.884561,-3.599764,-8.579573,2.975706,-3.866302,7.350963,9.085085,5.189620,-4.166200,-6.526624,8.228944,0.094833,-3.174332,-4.210171,2.306746,9.027986,1.291579,0.053613,3.325202,4.142615,-4.201325,-3.059570,-5.497687,-7.034610,-6.671893,-0.091355,4.661256,-1.321805,-9.346336,-5.267537,8.630380,0.031694,9.800943,3.906207,-0.067155,5.280216,7.339980,-7.261130,8.376321,-9.395085,1.765319,1.799298,5.681164,-0.419082,6.114703,2.263727,-7.299343,9.098875,-4.764260,-8.107960,0.317950,2.413356,3.563082,1.333953,8.931575,-7.543713,-6.263492,5.284102,7.032677,5.802851,-4.555126,-3.718015,7.148399,1.973309,-4.546096,-8.223209,1.697417,-1.663448,9.953869,5.710315,-4.610079,8.174494,7.732713,-9.437626,-7.750378,0.553059,-8.248408,-2.682334,-1.269659,3.660126,3.896186,-9.855859,-2.163514,-1.046390,-1.662271,-4.521167,1.292685,5.348575,-2.205100,-0.437098,8.796241,-5.537666,8.683379,-5.970674,-6.908019,-5.511730,9.426442,-6.845414,6.095749,-0.448337,-9.320528,-4.451652,-6.358887,-2.113271,8.404115,-1.046547,7.853914,2.210001,7.247308,-7.411118,1.962541,0.944090,3.680457,-5.455204,-3.517453,9.562093,1.430213,4.850732,6.236745,0.103744,-0.516285,-1.381642,-1.185559,-2.328080,6.833050,6.946515,8.646931,2.840175,-4.292326,6.368976,-7.689959,2.715677,2.706706,-5.878202,-1.519812,2.238160,2.996303,-2.477945,8.074520,5.868069,1.412993,-3.062291,4.968004,-4.946983,7.807691,2.450593,-0.015511,-3.213664,3.337996,-4.887158,-7.824699,-3.432723,7.965062,4.864954,1.437163,3.754896,8.902091,4.380435,-5.091207,-4.838845,0.651921,8.759797,-1.788989,9.469890,-8.795469,5.596543,-8.391354,-0.422653,0.410448,-2.309901,-0.528717,4.395476,0.165231,7.053158,-3.065930,-5.484735,5.789596,6.083828,9.826121,5.335455,0.810583,-5.361765,-9.267953,0.740324,-3.444229,-2.844975,-6.941217,-6.216241,-5.675774,1.169210,3.608139,-5.062758,5.393500,-7.109546,8.477036,4.029304,-0.486403,-2.012988,-1.202608,-8.733548,3.648639,-8.845146,0.637529,-8.053666,-5.963905,-3.387586,4.089920,-1.687285,0.708181,2.484851,-4.057215,3.110936,-4.967521,6.963279,3.869784,8.712657,-3.994441,-4.795832,-4.745373,8.631740,-6.389560,-3.044123,-8.452017,6.791828,7.202307,-9.870149,6.183621,-9.107011,5.966417,-1.683103,-1.022141,-9.673683,5.304571,-7.409182,0.029879,-1.451251,3.095881,0.680141,3.654535,7.640730,7.832168,-1.131932,7.178075,-2.985484,-7.374690,-6.036422,-8.210557,4.897361,8.688800,0.161307,9.872709,5.596603,-9.323034,4.900294,5.104389,-4.453579,-8.114871,9.362857,6.349361,9.910482,-2.531994,-4.160142,-9.345455,3.173686,1.774229,-6.669997,-7.311101,-0.032856,-6.721579,8.249652,-2.630566,-8.760662,-2.663679,4.327824,6.543005,-1.984718,-2.505914,-0.709956,-0.453149,-6.889211,-6.845092,0.281311,-0.697264,1.359822,9.106113,-4.391444,-9.403106,-5.685982,-9.726178,-9.556711,-6.761794,-8.346204,-5.736250,7.891547,-8.181764,-4.937215,-3.829782,0.886641,2.712623,5.421500,3.673331,0.323915,-9.570754,9.144816,9.596749,-1.007362,-1.459414,-4.462035,3.106300,2.917149,1.682474,-8.443617,9.636258,4.472910,-8.433515,1.616589,-2.071218,9.418275,5.436868,-0.757904,5.055393,-5.031147,9.705126,-4.454689,3.902073,-2.685579,2.589346,-0.199619,-6.402251,-8.811748,6.688956,9.544008,-0.993386,-4.112544,2.044220,-5.048125,-1.736162,-3.670019,7.629324,-1.057636,-2.202358,0.152352,-1.255905,8.628627,1.595154,6.967138,7.296768,3.608054,-4.932232,2.791754,-8.922166,-3.579634,0.836545,-7.978532,4.651282,0.508159,0.847021,1.303456,-8.676449,-4.888784,-4.784095,-3.192057,-5.365256,4.234579,-9.833452,-5.373487,-2.693803,9.772216,7.856020,-1.662539,-4.462959,0.788973,3.658827,5.301389,7.842947,0.501146,-4.223952,0.374743,6.070300,8.299929,-9.587909,-1.910788,-0.010768,-3.471213,5.006180,-7.445384,-6.031832,8.009294,-4.842689,4.502843,7.228589,-3.532426,5.470098,-7.604829,-3.711809,-2.592996,-0.716482,-4.047303,-3.281037,-8.836302,4.851628,3.123964,-9.142757,3.852139,-5.480257,-7.306591,-7.193932,2.347280,3.729451,-3.976340,2.613464,-7.139926,-7.223253,-1.545272,6.344004,-0.132304,4.736940,-3.718661,9.344487,-3.013976,-2.265936,6.893222,9.589432,-2.724373,-9.600902,6.866704,5.353473,0.859523,-3.521208,-3.331980,1.053102,-3.621742,4.062192,-2.461502,5.925766,-1.631434,-5.752386,-6.353464,-8.023581,-2.331486,6.989015,-5.144831,3.674841,-8.281795,8.656196,0.065494,-0.837073,1.130502,-9.569663,-3.916325,-6.785184,6.519394,-7.928540,6.495784,0.548398,0.307062,1.574402,8.916126,-6.226048,-2.422107,3.025412,-9.399824,8.362943,9.654543,9.673809,0.996353,-4.016075,-6.730325,-3.482862,5.679031,9.440343,1.777996,-4.340049,4.036228,-7.102633,-0.444079,7.261027,1.084594,-1.835015,-8.799483,-4.861717,4.874077,7.546932,5.144285,7.639962,3.612762,-0.327164,8.336629,0.978789,6.792241,-8.944596,9.824485,-6.258470,8.051945,3.736134,-1.665102,6.225165,-8.384726,-2.607036,1.137652,-4.755912,-8.321970,6.216124,8.279205,3.293920,-7.371730,-9.664853,5.086293,5.820637,4.522147,1.015305,-7.685797,-2.238319,4.309974,3.901388,-5.176032,2.029197,-7.838517,9.129683,6.749183,-6.501435,-0.936117,-6.029405,3.596684,-3.959206,-8.822300,-3.054799,7.246747,-3.376750,9.487330,7.159993,2.299844,6.044974,6.537381,-9.053958,7.968374,-0.187524,9.237507,0.741986,-2.936496,-5.204071,2.289086,-2.186138,4.569218,8.801699,-6.370336,-8.961199,7.122109,9.045770,-6.554818,-8.302565,-9.618337,-1.637603,3.837290,-7.586533,4.193232,-2.621999,0.893244,7.816406,7.603549,-8.679693,5.548981,-7.534135,-3.426117,8.736499,6.138771,-9.307186,2.348154,6.256463,-6.295947,-9.043200], dtype = "float32")#candidate|6977|(1440,)|const|float32
call_6976 = relay.TupleGetItem(func_3699_call(relay.reshape(const_6977.astype('float32'), [6, 15, 16])), 0)
call_6978 = relay.TupleGetItem(func_3701_call(relay.reshape(const_6977.astype('float32'), [6, 15, 16])), 0)
output = relay.Tuple([call_6974,call_6976,const_6977,])
output2 = relay.Tuple([call_6975,call_6978,const_6977,])
func_6981 = relay.Function([], output)
mod['func_6981'] = func_6981
mod = relay.transform.InferType()(mod)
mutated_mod['func_6981'] = func_6981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6981_call = mutated_mod.get_global_var('func_6981')
call_6982 = func_6981_call()
output = call_6982
func_6983 = relay.Function([], output)
mutated_mod['func_6983'] = func_6983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1749_call = mod.get_global_var('func_1749')
func_1751_call = mutated_mod.get_global_var('func_1751')
call_6986 = relay.TupleGetItem(func_1749_call(), 0)
call_6987 = relay.TupleGetItem(func_1751_call(), 0)
var_6989 = relay.var("var_6989", dtype = "bool", shape = (3, 8, 4))#candidate|6989|(3, 8, 4)|var|bool
bop_6990 = relay.less_equal(call_6986.astype('bool'), var_6989.astype('bool')) # shape=(3, 8, 4)
bop_6993 = relay.less_equal(call_6987.astype('bool'), var_6989.astype('bool')) # shape=(3, 8, 4)
func_2574_call = mod.get_global_var('func_2574')
func_2576_call = mutated_mod.get_global_var('func_2576')
call_6999 = func_2574_call()
call_7000 = func_2574_call()
func_2828_call = mod.get_global_var('func_2828')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_7012 = relay.TupleGetItem(func_2828_call(), 2)
call_7013 = relay.TupleGetItem(func_2829_call(), 2)
output = relay.Tuple([bop_6990,call_6999,call_7012,])
output2 = relay.Tuple([bop_6993,call_7000,call_7013,])
func_7014 = relay.Function([var_6989,], output)
mod['func_7014'] = func_7014
mod = relay.transform.InferType()(mod)
mutated_mod['func_7014'] = func_7014
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7015 = relay.var("var_7015", dtype = "bool", shape = (3, 8, 4))#candidate|7015|(3, 8, 4)|var|bool
func_7014_call = mutated_mod.get_global_var('func_7014')
call_7016 = func_7014_call(var_7015)
output = call_7016
func_7017 = relay.Function([var_7015], output)
mutated_mod['func_7017'] = func_7017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2471_call = mod.get_global_var('func_2471')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_7125 = relay.TupleGetItem(func_2471_call(), 0)
call_7126 = relay.TupleGetItem(func_2473_call(), 0)
func_6643_call = mod.get_global_var('func_6643')
func_6644_call = mutated_mod.get_global_var('func_6644')
call_7154 = relay.TupleGetItem(func_6643_call(), 0)
call_7155 = relay.TupleGetItem(func_6644_call(), 0)
bop_7160 = relay.bitwise_xor(call_7125.astype('int64'), relay.reshape(call_7154.astype('int64'), relay.shape_of(call_7125))) # shape=(3, 8, 1)
bop_7163 = relay.bitwise_xor(call_7126.astype('int64'), relay.reshape(call_7155.astype('int64'), relay.shape_of(call_7126))) # shape=(3, 8, 1)
output = bop_7160
output2 = bop_7163
func_7170 = relay.Function([], output)
mod['func_7170'] = func_7170
mod = relay.transform.InferType()(mod)
mutated_mod['func_7170'] = func_7170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7170_call = mutated_mod.get_global_var('func_7170')
call_7171 = func_7170_call()
output = call_7171
func_7172 = relay.Function([], output)
mutated_mod['func_7172'] = func_7172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_7269 = relay.TupleGetItem(func_791_call(), 1)
call_7270 = relay.TupleGetItem(func_792_call(), 1)
output = call_7269
output2 = call_7270
func_7292 = relay.Function([], output)
mod['func_7292'] = func_7292
mod = relay.transform.InferType()(mod)
mutated_mod['func_7292'] = func_7292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7292_call = mutated_mod.get_global_var('func_7292')
call_7293 = func_7292_call()
output = call_7293
func_7294 = relay.Function([], output)
mutated_mod['func_7294'] = func_7294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6445_call = mod.get_global_var('func_6445')
func_6447_call = mutated_mod.get_global_var('func_6447')
call_7306 = func_6445_call()
call_7307 = func_6445_call()
const_7322 = relay.const([[[8.802326,9.469257,5.290362,-8.485635,1.821769,-1.428117,3.643644,0.285504],[-8.414250,4.661698,8.007284,-6.619287,-6.938593,2.133620,8.142140,6.105984],[3.818634,7.174117,1.078909,-2.467262,7.434944,9.536930,-2.358699,-7.237564],[-3.110297,-5.692369,-9.743163,3.531276,4.062734,6.957411,-3.170255,2.958746],[-8.762449,-8.233583,-4.094709,-1.934813,-6.151420,6.351831,-6.399020,5.380547],[8.275735,-9.225648,7.852424,-4.223493,-3.474467,4.125667,-4.803395,-2.771821],[9.683422,-0.205567,6.455710,-9.176531,-9.934720,-6.934488,5.322962,-7.887342],[5.593157,-8.739610,-4.492725,3.079227,-3.446988,7.215209,0.605699,0.452018]],[[5.387851,7.362259,-5.213999,-9.881268,3.151346,5.656055,-6.059333,2.301068],[-4.798986,-5.224609,-0.020376,5.645357,2.731120,4.756849,-4.401946,6.241531],[-1.146506,6.474822,-7.899999,3.614711,-7.948459,-9.175649,-3.561999,8.177662],[0.402502,-0.586101,2.004009,6.893280,-9.345243,-6.267523,6.343538,-6.802591],[-9.731802,6.366350,5.743513,-3.484477,4.769006,0.453825,-9.122981,8.295689],[-4.032553,5.619816,6.178990,-8.062216,9.825422,4.002235,7.687869,-1.722035],[2.563212,-5.641620,-2.519820,-3.280859,-0.995116,-0.030551,-0.302560,-3.296612],[2.108434,5.955035,-4.080483,-2.794003,-5.180951,6.789673,-2.944802,2.919427]],[[2.344711,-2.214034,-6.009837,2.109624,-6.349325,6.459462,3.917149,-9.926163],[5.377986,-7.757259,4.843750,8.988303,-2.264718,7.984743,-3.096629,-4.639633],[7.790108,9.356566,9.023531,-3.532087,-6.989066,3.018236,9.594192,-8.295631],[5.273150,8.080796,-6.855401,-4.786027,8.028765,5.731212,-1.771906,6.497303],[-0.832139,4.647105,6.534935,-5.422909,8.468533,-4.651493,6.395848,9.099745],[0.367580,9.083513,4.325492,-6.776033,-4.997394,-2.118898,0.968277,-2.982970],[-2.915515,6.616341,3.150892,-9.944178,3.357919,0.507096,2.684679,6.866842],[5.010737,-0.608961,-5.179892,5.284072,-4.517897,1.363323,8.004793,-0.241114]]], dtype = "float64")#candidate|7322|(3, 8, 8)|const|float64
bop_7323 = relay.right_shift(call_7306.astype('int8'), const_7322.astype('int8')) # shape=(3, 8, 8)
bop_7326 = relay.right_shift(call_7307.astype('int8'), const_7322.astype('int8')) # shape=(3, 8, 8)
func_3342_call = mod.get_global_var('func_3342')
func_3346_call = mutated_mod.get_global_var('func_3346')
var_7329 = relay.var("var_7329", dtype = "uint64", shape = (2400,))#candidate|7329|(2400,)|var|uint64
call_7328 = relay.TupleGetItem(func_3342_call(relay.reshape(var_7329.astype('uint64'), [10, 15, 16]), relay.reshape(var_7329.astype('uint64'), [10, 15, 16]), ), 0)
call_7330 = relay.TupleGetItem(func_3346_call(relay.reshape(var_7329.astype('uint64'), [10, 15, 16]), relay.reshape(var_7329.astype('uint64'), [10, 15, 16]), ), 0)
uop_7335 = relay.sin(call_7328.astype('float64')) # shape=(10, 15, 16)
uop_7337 = relay.sin(call_7330.astype('float64')) # shape=(10, 15, 16)
output = relay.Tuple([bop_7323,var_7329,uop_7335,])
output2 = relay.Tuple([bop_7326,var_7329,uop_7337,])
func_7346 = relay.Function([var_7329,], output)
mod['func_7346'] = func_7346
mod = relay.transform.InferType()(mod)
mutated_mod['func_7346'] = func_7346
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7347 = relay.var("var_7347", dtype = "uint64", shape = (2400,))#candidate|7347|(2400,)|var|uint64
func_7346_call = mutated_mod.get_global_var('func_7346')
call_7348 = func_7346_call(var_7347)
output = call_7348
func_7349 = relay.Function([var_7347], output)
mutated_mod['func_7349'] = func_7349
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7356 = relay.var("var_7356", dtype = "uint16", shape = (14, 13, 3))#candidate|7356|(14, 13, 3)|var|uint16
var_7357 = relay.var("var_7357", dtype = "uint16", shape = (14, 13, 3))#candidate|7357|(14, 13, 3)|var|uint16
bop_7358 = relay.left_shift(var_7356.astype('uint16'), relay.reshape(var_7357.astype('uint16'), relay.shape_of(var_7356))) # shape=(14, 13, 3)
func_6267_call = mod.get_global_var('func_6267')
func_6268_call = mutated_mod.get_global_var('func_6268')
call_7361 = func_6267_call()
call_7362 = func_6267_call()
uop_7367 = relay.asinh(bop_7358.astype('float64')) # shape=(14, 13, 3)
output = relay.Tuple([call_7361,uop_7367,])
output2 = relay.Tuple([call_7362,uop_7367,])
func_7375 = relay.Function([var_7356,var_7357,], output)
mod['func_7375'] = func_7375
mod = relay.transform.InferType()(mod)
mutated_mod['func_7375'] = func_7375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7375_call = mutated_mod.get_global_var('func_7375')
var_7377 = relay.var("var_7377", dtype = "uint16", shape = (14, 13, 3))#candidate|7377|(14, 13, 3)|var|uint16
var_7378 = relay.var("var_7378", dtype = "uint16", shape = (14, 13, 3))#candidate|7378|(14, 13, 3)|var|uint16
call_7376 = func_7375_call(var_7377,var_7378,)
output = call_7376
func_7379 = relay.Function([var_7377,var_7378,], output)
mutated_mod['func_7379'] = func_7379
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7394 = relay.var("var_7394", dtype = "float32", shape = (5, 10, 14))#candidate|7394|(5, 10, 14)|var|float32
uop_7395 = relay.sigmoid(var_7394.astype('float32')) # shape=(5, 10, 14)
output = relay.Tuple([uop_7395,])
output2 = relay.Tuple([uop_7395,])
func_7401 = relay.Function([var_7394,], output)
mod['func_7401'] = func_7401
mod = relay.transform.InferType()(mod)
mutated_mod['func_7401'] = func_7401
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7402 = relay.var("var_7402", dtype = "float32", shape = (5, 10, 14))#candidate|7402|(5, 10, 14)|var|float32
func_7401_call = mutated_mod.get_global_var('func_7401')
call_7403 = func_7401_call(var_7402)
output = call_7403
func_7404 = relay.Function([var_7402], output)
mutated_mod['func_7404'] = func_7404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2123_call = mod.get_global_var('func_2123')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_7426 = relay.TupleGetItem(func_2123_call(), 0)
call_7427 = relay.TupleGetItem(func_2124_call(), 0)
output = call_7426
output2 = call_7427
func_7436 = relay.Function([], output)
mod['func_7436'] = func_7436
mod = relay.transform.InferType()(mod)
mutated_mod['func_7436'] = func_7436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7436_call = mutated_mod.get_global_var('func_7436')
call_7437 = func_7436_call()
output = call_7437
func_7438 = relay.Function([], output)
mutated_mod['func_7438'] = func_7438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7523 = relay.var("var_7523", dtype = "float64", shape = (15, 1, 11))#candidate|7523|(15, 1, 11)|var|float64
const_7524 = relay.const([[[8.914008,-4.177536,2.241175,8.312710,-9.651122,-4.379553,2.960628,8.539026,-4.341570,-7.138948,-4.909011],[3.707502,-9.697068,5.323537,0.921250,-9.729580,-0.422110,-7.389429,5.301088,7.214257,0.372181,-4.881621],[1.646748,0.990332,3.228524,5.500091,0.478648,3.062335,2.050183,6.578555,-2.427888,7.892183,-4.766096],[-2.172936,-3.351917,-2.418126,5.096591,-9.318088,-1.123244,-1.912819,1.851396,6.287302,-1.034870,7.325362],[-9.347900,-2.852975,-3.492794,3.083127,9.954022,-6.982147,-0.370141,5.963347,6.783667,-7.298026,5.961765],[-7.786449,-2.594067,-8.756963,-7.176402,-4.570343,-0.194238,7.253720,-6.132683,6.827089,-4.493088,0.312605],[-1.670909,-3.498047,-6.754956,-3.664402,9.657874,0.804230,-0.404518,-6.967629,8.378867,6.361472,1.881778],[-1.368845,-3.140047,3.758889,8.476607,2.100390,8.868897,-0.972674,-5.835309,-9.125510,2.709427,3.802246],[9.135575,-9.467784,-3.610959,-4.583416,9.386522,1.593427,-6.293431,-2.815633,-8.195132,-6.696263,-6.890188],[1.898182,3.177513,-6.860883,8.600898,-7.651061,-5.180395,5.239785,4.414068,-2.796934,-6.486204,-9.044868],[3.978668,2.823624,-7.962669,4.559111,-7.183984,1.529741,-5.241615,-4.402654,7.262835,-0.282076,0.846078],[-2.614667,9.101552,1.075317,-3.787953,8.512004,1.650560,2.121638,-4.760704,-0.055265,-2.802862,-2.106310]],[[9.482530,-3.054387,5.167104,-7.955284,0.865743,2.266066,-8.712015,-4.952149,-5.948850,-4.206962,-0.865719],[4.268010,-5.866956,5.155843,2.911775,-8.073932,-5.738118,1.314725,8.193066,9.808544,-2.848095,-7.065050],[3.841085,-9.383709,-6.926344,9.251776,-3.046480,8.965475,-2.428667,0.200359,-9.317764,6.871515,2.610136],[-5.510862,-3.436503,5.642797,3.067711,6.089829,-7.672039,-8.245461,-7.956733,-6.750333,9.476129,-1.071746],[-4.492438,7.295238,8.916206,-6.203416,-5.550944,8.001279,-8.556006,9.193221,-2.504971,-7.552574,-6.906109],[6.834850,9.614841,-3.757149,0.097171,-3.812753,-8.540322,-2.096164,-9.308788,-4.532823,-2.398980,-1.654309],[-6.723529,-0.378653,-2.897187,-2.681036,7.271431,-7.249359,2.609049,4.567760,7.509403,-3.948667,-1.705396],[5.670099,4.834466,5.684885,1.536482,-8.557216,2.220298,7.428340,-5.149260,1.383287,3.444301,-2.828057],[-3.638876,-6.649123,7.690294,4.859895,0.993069,3.351533,7.619498,-1.626665,-2.249489,-1.030955,5.576725],[9.392991,6.203560,-8.118190,-5.035702,3.811543,-7.209984,-2.267230,4.854389,7.124572,-2.693044,2.505690],[8.837737,8.924280,2.510875,-1.097849,0.634177,-8.571107,-7.166733,6.099486,1.546069,4.734417,-4.834947],[7.382711,9.971781,9.770560,1.139555,4.004289,-0.356567,-0.316788,1.191538,9.201287,2.479385,1.963394]],[[-8.966874,-0.661238,-8.549847,5.973374,-2.206963,-7.532393,-1.052657,7.501464,-1.344673,-9.260935,4.044904],[-7.857663,2.057106,8.944006,3.944546,-0.131194,-8.837373,4.864486,-4.474341,3.109722,-6.664968,8.069140],[1.382752,-4.677265,9.112197,5.684991,-7.086409,5.055428,9.631349,-4.446432,-2.774703,-7.865158,8.010531],[2.798682,-1.046130,-7.355296,-7.747167,5.833749,4.237506,9.920360,7.403223,3.253989,5.332436,3.612327],[-3.837572,9.368645,7.256930,0.382589,-1.117655,-8.158012,4.652858,5.611424,-9.358721,-3.987054,-7.873186],[0.856931,-6.002976,3.999480,2.036519,-5.951605,-0.837766,-2.074420,0.714233,9.026433,-4.569437,-5.536609],[-5.879733,3.191696,3.408500,-0.677457,-8.369515,1.741463,6.469353,-8.687233,1.414162,-2.202678,-6.183300],[9.227573,-4.547239,8.611617,0.553399,-0.619902,0.828023,-8.561511,2.268694,1.733613,-4.772214,-7.215218],[7.028943,7.934498,0.293435,6.118976,-1.493887,2.291496,3.849130,-0.451890,9.401886,-8.938604,-1.491359],[0.438124,-6.267011,2.806565,3.390603,-9.362015,-7.878320,2.543618,3.474580,-5.893893,-6.441523,-9.593476],[-9.434789,-6.400637,5.874896,7.975806,2.088432,-5.362083,9.126776,4.695281,9.947250,1.132529,5.210541],[-2.335704,5.245521,-4.176049,-4.444271,2.837472,7.840418,-2.875703,0.443101,4.603182,-3.076753,-3.814089]],[[3.811182,-1.155100,5.735545,2.241431,7.934399,3.338639,-3.937997,-6.632283,-5.468249,1.289078,4.413554],[-4.034677,0.991860,6.974286,4.544290,7.020085,7.645900,-3.740639,-8.725972,8.354708,3.766735,-8.755325],[1.863876,-0.328181,8.800495,9.028343,-6.536585,3.902452,0.214620,8.464029,-2.693318,-0.877593,4.862010],[-4.243665,-8.624084,4.651698,-9.364041,2.897947,-9.988288,4.830220,5.140042,-5.055424,-8.437612,-6.584973],[-3.445986,5.514098,-8.045439,1.059972,-6.976256,8.505472,8.296835,-8.611064,9.525589,8.117020,2.108480],[3.648197,-4.135895,-8.492628,1.828480,-8.488817,2.265313,-4.976750,3.883985,5.882168,2.043716,-6.047684],[8.431439,-9.010410,-5.606705,-1.101990,-2.231375,1.175721,9.937087,0.494836,-4.163128,-1.444088,8.202126],[7.487665,-6.306119,-7.997429,-0.147261,0.531030,5.519956,-8.571455,4.974928,-1.894631,-0.725958,-7.002643],[1.023204,-1.980892,-2.280688,1.790308,4.757633,-6.460442,5.265505,1.994013,-4.364336,9.982527,-9.285538],[3.396526,-0.890504,8.856874,8.129569,-4.841569,5.082432,-0.500812,-8.233401,-0.316962,0.506772,1.611311],[3.299874,-9.923180,2.396114,-0.048538,3.759771,-9.156518,0.899909,-7.854330,4.981980,1.845841,5.105580],[-3.880786,-3.826651,1.255923,-9.047561,-0.484810,7.111214,3.740815,8.966899,-4.205723,1.416831,-8.896377]],[[-2.968138,-9.519865,-3.614513,-2.877667,5.596970,3.333053,0.268339,3.850826,4.938467,-4.081400,-7.637734],[-3.915814,5.783356,-3.969880,3.881803,4.089661,6.208909,8.905542,2.382701,5.242618,0.085253,-8.968346],[7.253093,-3.393961,-4.568715,1.614762,-3.863091,-5.046994,-3.847980,-0.174180,3.067585,8.528942,3.910628],[-8.910520,2.808179,-8.673547,-3.623438,6.199643,-5.673379,0.458193,-9.544277,-7.812647,-5.927700,-7.472422],[1.984430,-5.312720,-9.564877,-8.540241,-3.122447,5.411052,-7.162875,-5.067449,-0.533893,6.224041,1.667533],[5.264555,4.685684,-0.447352,-8.453688,1.513994,-8.733741,4.298407,0.368852,-7.707663,-9.264615,8.760152],[5.670415,-6.940606,-4.357759,6.728908,-0.137380,5.288670,-8.853331,4.301344,2.601269,-0.180675,-6.842764],[-6.587547,2.300209,5.562541,-4.276277,7.742308,0.698927,-0.771082,9.047945,2.648974,-0.331180,3.962162],[4.582777,-0.252220,0.810786,-1.035410,-6.510143,-9.660610,9.681217,2.357199,-2.075707,-3.286920,-2.521338],[9.390702,-0.165985,3.222221,-0.630685,1.757257,4.729492,-0.076309,-2.498032,-9.676823,3.020132,6.476743],[4.317588,9.221417,6.047537,3.277579,-9.794662,7.498460,1.359374,0.712115,3.799720,5.807977,-0.774818],[-0.553630,-3.095899,7.144167,5.147314,1.943612,-7.113859,-6.300287,-5.696805,7.786909,7.462248,4.791227]],[[-4.040685,-9.714848,2.712352,-6.276434,7.503140,-6.741592,-9.575621,3.237433,-7.264863,-4.190127,5.692604],[-7.635145,-3.954387,-1.750005,-3.747753,-3.981004,0.481430,5.439818,2.800605,-2.325685,-1.897060,-5.374572],[8.923405,-9.998956,-6.467225,-5.660050,3.499118,2.788659,-7.442387,8.383034,5.736270,8.911410,-1.667511],[4.679392,6.257467,-0.916336,5.059407,-7.309910,5.697580,-3.355345,6.050903,4.779030,-5.382503,-9.847292],[4.085570,7.273430,5.876362,9.767190,1.159692,9.334287,-9.244332,-7.685853,4.071522,-7.128189,1.551386],[-0.817222,8.312710,-0.624953,7.668650,1.068093,-4.435453,2.373507,6.558837,-7.496878,-6.068862,4.070877],[0.240714,-6.658809,-8.969014,2.522147,0.824468,-5.334636,-0.751757,-8.421214,9.463396,-3.925910,4.028544],[-4.898423,-0.778406,7.239283,-3.749504,8.431931,2.926874,-7.014543,0.083016,9.506266,-0.967435,6.290226],[-4.621866,-8.126767,3.899158,-9.725875,-8.212591,-4.936953,1.355246,7.534158,-2.728246,2.428906,-8.274013],[-3.375982,-1.251480,0.363836,8.123088,3.600585,-7.862857,-6.599668,-2.857251,-2.026157,1.367705,3.389472],[5.626945,-7.237048,9.333382,3.752405,-5.405970,9.479821,0.821326,2.402220,-3.730746,8.302889,-7.705482],[-5.324397,-6.870696,1.880125,9.577818,-5.281639,-3.646588,1.034513,-5.669160,1.049063,-1.532789,9.987438]],[[9.737552,-7.136532,2.583846,5.462675,2.876993,-9.223671,-6.052582,2.277062,-1.218342,-4.064954,5.161935],[3.231720,-7.026789,-7.980145,1.227922,3.812801,-2.300204,-2.712712,4.523207,1.467292,-6.806639,-5.000913],[3.776406,-4.599572,2.757481,-7.919785,-3.726627,-1.085208,3.462146,6.052334,5.991507,0.754834,9.750001],[9.097552,0.607542,5.696554,3.777858,9.320669,-7.850900,-1.044262,-2.936383,-2.388117,-9.274818,-5.131906],[2.378796,7.904635,-1.243228,-8.596009,-0.691230,-7.060488,-6.527902,5.294955,0.343422,-9.309737,5.089299],[5.368100,-9.122375,-2.083318,-1.957909,-5.912367,0.837367,-4.823508,-4.735185,4.374611,7.363521,3.061603],[7.342260,9.595389,6.121119,-0.613057,-9.129099,-7.297542,8.395143,-3.132326,5.372902,4.275941,-8.331185],[-1.792185,-1.998509,0.320438,2.624714,9.232916,-5.903846,9.388194,2.689156,-5.384072,8.631896,-8.278828],[4.156463,0.475551,0.895794,9.563455,-7.568697,-7.071795,3.928712,-0.835696,-2.938735,-4.411352,-7.366487],[-9.824536,3.915128,-3.475444,-1.651508,-0.897907,9.119760,-2.102854,-3.733977,-7.786058,-2.465542,-2.883685],[-2.062713,-6.870317,-4.321773,6.607404,8.421607,-6.130634,-7.421042,3.524826,0.067807,8.465846,3.493261],[2.850165,8.159911,3.934042,3.384490,-3.831546,-2.949412,-7.374458,6.413142,-3.425489,-3.497723,3.313042]],[[6.517774,8.341151,-3.553493,1.741319,-8.283483,-4.226295,-0.465216,5.838937,4.800997,0.569991,3.685857],[-3.999413,-2.847958,2.583950,-3.050274,6.724292,4.179684,-1.806601,3.402341,-7.750567,9.848599,-0.621986],[-7.069752,4.324831,9.870382,4.736855,-1.287410,5.458246,-7.736566,4.644585,5.925305,-5.568292,3.587414],[7.892716,-9.738077,3.213983,-1.615077,1.314846,5.387103,-8.769767,-4.711168,9.110808,3.010927,1.724214],[8.273486,-5.102911,0.013499,-8.300564,-1.489198,-3.627395,5.931509,-6.484136,7.452617,-2.632300,-6.876327],[6.998501,-3.030613,9.048379,9.452037,-0.687272,-1.221980,8.022268,8.786025,-2.604669,4.278230,3.858488],[-9.068467,-3.262344,6.064358,7.003532,1.413957,-6.256330,1.478848,-0.381468,-6.035379,-3.432801,7.569679],[8.554075,7.442534,-1.046834,-4.460683,4.533434,8.277370,-0.422868,-1.978342,-1.088837,-2.887555,8.113791],[3.251816,-0.304655,-6.080523,-1.446220,-8.635371,4.929413,0.070401,3.736466,1.301705,8.063497,-1.688287],[8.886062,1.114917,3.598496,1.417958,8.276071,-7.330270,-7.890695,-1.738760,-5.723383,-6.004367,-4.936262],[-4.009558,1.599405,-9.681374,-1.338218,-5.051853,5.535209,-5.188836,8.173366,-2.482543,-5.541061,-9.878443],[1.182599,8.912968,-5.128038,0.361680,7.531615,-2.795592,3.505233,7.273449,5.306593,-9.314453,2.288185]],[[1.491184,-9.515213,-6.471784,-1.546161,1.448873,9.933302,-2.080238,8.890524,8.371291,3.250075,5.343324],[-9.774254,-0.441132,9.666732,4.067754,0.232620,2.265767,-8.445686,-5.592850,3.905261,-4.926514,-0.429826],[-9.704340,7.232765,1.254151,6.427916,6.001490,1.502123,8.863851,-1.949423,-6.107756,-7.377759,3.820255],[7.275406,9.274071,-7.826609,8.013223,-7.563432,-9.705097,6.191017,-7.274312,-2.953983,4.094706,-1.784876],[-3.679861,9.920478,-9.410484,1.511302,-0.949406,-8.833318,0.333280,0.827679,0.434321,-0.361357,7.644397],[1.126290,-1.801159,-8.385527,-6.869619,-7.062085,9.576856,9.107457,3.918930,-4.769252,4.288135,-1.402788],[5.746434,6.474879,7.140227,-1.706482,-0.778528,0.448209,1.611718,-3.153280,-8.961840,0.179554,-7.627191],[4.305401,5.351862,7.701007,-3.435595,9.324266,9.552575,5.682931,-8.574436,-3.967546,9.755189,3.802079],[3.157769,-7.961199,-5.808035,7.680245,-8.992395,9.078232,-0.903950,-7.896715,-6.372435,-1.236914,4.092691],[-6.142806,6.993934,-4.751781,-9.723999,-0.697166,9.702137,6.543656,-6.360824,-5.556922,-4.214852,-1.699179],[-3.501673,9.774740,-1.374931,-7.473964,7.012923,8.163340,8.777452,-9.069069,5.442304,5.749875,3.633945],[-9.039212,-5.159934,0.872479,-5.727096,0.157398,-9.267378,0.993088,0.481571,-5.748620,7.848900,0.110704]],[[1.168757,-5.140609,-5.890325,0.498902,6.929862,9.171882,-9.372926,-2.411443,-0.125929,3.166694,-8.729552],[1.664114,0.599519,1.846776,0.287903,7.117016,-3.852382,8.542430,-2.600536,-1.560515,5.170009,4.107813],[-9.123334,-9.345509,3.216411,-2.115334,2.889767,9.746038,7.819247,1.236613,-5.509400,-5.278789,-1.738424],[1.975693,-0.730427,-8.918925,-0.180969,-6.515433,0.798531,6.433998,-2.595503,2.333305,-8.425261,-6.930563],[1.919011,-7.534000,6.889653,-5.706434,3.546388,-2.360017,4.887257,4.008318,-8.865871,9.218970,-9.498626],[-8.691891,-1.445540,-2.249177,8.462769,-3.565778,-1.148002,-2.251056,6.536878,-8.030153,-9.512104,8.980334],[6.126428,6.553389,-5.614339,-7.526875,-0.503541,5.936290,-4.885805,2.457903,3.711422,-0.497716,-5.899714],[1.793814,6.051306,-8.026312,-4.564460,3.079901,-5.297450,7.454312,2.442296,-9.370767,-2.469536,-8.188825],[9.588559,-3.715008,-7.977142,8.453682,9.747112,-4.503492,-1.612038,0.939207,-1.106988,-5.543470,2.878541],[3.968732,9.218333,-1.734657,-2.129477,-8.055941,-8.481490,-0.102132,4.622005,-4.301239,-3.242244,8.453416],[5.787177,7.195793,-4.879493,1.633227,3.337325,-0.263608,-4.259843,-2.748110,-2.293450,-7.698188,-0.932142],[0.974209,-9.998623,-8.960051,-7.461052,0.897144,-7.792972,-0.761859,2.517193,2.925613,-2.907580,7.614939]],[[-6.472596,2.496641,2.129475,-4.782788,-5.563271,6.341124,9.928654,4.187978,-2.887756,6.513880,3.662600],[0.090163,3.389005,2.011982,-9.415249,-4.848770,0.110051,9.037826,-0.385684,-6.289110,6.273961,3.882696],[1.749083,4.313578,-3.369767,8.122228,-5.441172,-1.645233,5.174349,4.009717,-9.278333,-1.535032,-1.724830],[-0.957181,5.938625,8.840784,5.699719,7.153700,-9.766701,-6.243263,-3.645314,-8.299807,-0.857720,-1.357819],[5.743596,3.349552,-7.743103,3.218133,-7.918820,4.255899,-0.533976,-3.112569,0.225199,-1.273691,-6.975150],[-1.389203,-6.749357,9.821548,2.949146,-9.052572,-4.057410,9.119173,-3.089924,1.694237,-9.093122,-0.898179],[8.963203,-3.427620,4.947507,-0.163010,9.668831,-4.501476,-9.769447,-9.641377,5.384571,-5.564096,1.455114],[-6.332515,-7.968394,-4.963166,-0.601472,7.550864,5.796129,3.722629,-6.254212,4.933233,-0.678738,-5.907120],[3.997117,8.671861,5.097382,-7.398917,0.680615,-2.456684,-3.792906,-7.395629,-8.951408,9.292265,-7.384943],[-3.585068,-0.166907,-3.875915,9.992135,7.874313,-0.155389,4.014799,-9.452518,-9.181007,8.796040,0.544963],[0.569385,-0.102311,1.638540,9.207029,-4.260882,2.483498,6.974066,-2.256937,-0.142618,-5.988346,-9.778156],[-2.400649,0.328124,-2.158925,-6.016902,8.567045,7.432871,8.268949,2.972057,-6.510683,-2.034664,-1.020495]],[[-0.911523,-2.262634,7.176182,7.832428,-9.856399,-6.175358,-0.551518,-5.233056,6.538358,-0.889632,-8.574081],[8.166972,-9.530429,0.610380,8.896234,8.577708,-6.199819,-7.740530,-9.413921,1.075181,-8.196823,-5.349816],[-9.454824,8.829764,-6.065364,3.858892,5.682754,-8.868268,-4.368661,-9.238701,-4.952939,6.195168,5.190050],[-1.938624,0.990073,-7.675401,4.458581,-1.621472,-9.617369,0.815799,0.221242,0.860582,-9.517839,2.081227],[5.740653,-9.928972,0.346970,0.027568,-2.207829,-0.419062,0.160902,7.935359,2.564240,9.472162,8.917293],[2.087589,1.786575,5.448156,-5.805376,-5.796761,-6.086872,1.691640,8.669399,-4.419234,-6.005307,6.265264],[8.504273,3.929570,9.635590,-5.763348,0.651101,4.874714,-5.840425,-7.570361,4.416009,4.359807,-4.225417],[7.563408,4.182275,4.143236,-9.467857,5.487339,1.572643,3.627327,8.688052,6.580481,6.110212,1.863031],[4.245679,-2.405209,3.671364,-0.877493,8.675730,8.715044,2.937540,-5.426338,6.956833,6.254504,-4.236623],[6.333591,2.253181,6.536886,-1.876010,-3.494387,-8.257285,-9.111139,-5.780776,5.763284,2.383139,-2.785241],[3.592615,-4.425915,1.096648,1.385903,-1.396438,0.385466,3.428314,-4.942841,-5.043380,2.811532,-9.408823],[-6.438770,-5.241092,-7.631804,-4.118238,-4.562118,8.208304,-8.342645,0.213755,8.177593,8.394392,7.123928]],[[4.936308,-2.518797,-8.070542,-2.358470,2.230359,-2.813084,1.430575,1.080422,9.673498,6.919188,4.830153],[8.339497,-1.198604,-5.559790,-4.897323,-0.494149,-3.992037,3.523415,8.070113,8.057938,-5.516278,-6.981609],[-8.049947,0.728444,-4.081993,-7.949810,-9.655994,-7.634059,-2.480889,-7.991981,-6.907224,-0.546264,1.257969],[3.775846,-9.985359,-2.328187,-6.924964,-3.642459,-2.736511,5.899125,-6.888907,-3.365288,0.177068,5.229869],[-3.704536,-9.193553,8.871791,1.153855,-2.034281,4.887871,5.007915,2.675923,-9.216840,-8.070895,0.954919],[8.684463,9.833317,1.582121,-7.739077,3.240080,-4.396070,3.882182,-9.779194,3.013187,-5.109846,3.391625],[-4.406758,9.482678,-9.380876,1.840532,5.020635,-4.811776,6.635208,-3.245980,-9.942358,-1.217940,6.379446],[-5.112109,-2.646963,2.420115,-2.654004,-8.695248,0.794042,-4.743412,2.951129,-3.808894,-9.254098,2.268569],[-6.993736,-9.902869,2.063076,3.191337,-4.531937,0.090036,5.713931,7.569827,7.812327,-6.908731,-7.427698],[2.927270,1.610449,-1.023900,-9.663880,5.926644,7.987830,9.455729,-5.455798,-6.029351,2.373958,0.420500],[-1.428588,-2.547933,-0.889129,-0.151270,3.409625,-9.993883,4.646146,2.924424,-3.350894,-8.613586,-4.463689],[6.396882,1.657484,8.583008,4.673325,9.904231,-8.489172,5.205809,6.583176,6.163398,2.020228,0.608153]],[[-0.672572,-2.255860,7.128184,5.211500,8.063664,-6.482351,-4.702590,0.169582,-1.217861,7.437679,-2.952864],[9.342414,-2.379300,6.473142,-5.129613,2.879509,7.408170,1.555363,-7.879588,-3.762700,9.120954,-4.374725],[-8.620823,8.388772,4.164002,6.381565,-2.112742,3.532290,1.621060,-0.532888,8.484624,0.724651,-9.545464],[7.638393,9.761919,-9.687691,-2.486584,-0.477729,-8.993908,3.602727,-4.159086,2.749447,1.280199,7.524312],[1.659465,-8.580950,9.006932,4.044239,-0.349385,1.126975,-6.271150,5.114685,-1.474815,-0.347459,8.827541],[-1.767798,-2.323047,-3.194957,-3.485402,4.112626,-7.621997,-8.517966,8.813977,5.811691,-5.094555,3.709952],[-9.637641,6.111801,-9.810031,0.858501,3.263292,0.832892,5.403346,6.116390,4.877623,-6.008067,-1.566549],[-1.866143,-5.345777,-5.307562,-5.395390,-9.192425,-5.593868,6.780809,5.661567,-1.481842,2.208154,-1.295021],[-3.754709,-8.457866,-7.066773,9.315950,-5.320860,-4.092284,5.204999,4.615400,-6.423553,-3.601441,-6.825983],[1.337355,-2.282690,-2.734721,4.834853,-6.660511,9.276778,-3.201982,7.712515,-9.397382,2.384869,8.435552],[9.009250,-7.607741,-6.286792,-1.176277,-8.452053,-8.459277,-1.608985,-4.086123,9.178037,8.673296,-7.894622],[5.838429,2.002029,4.090173,-0.594398,5.581753,6.773744,-9.866984,-8.461803,-9.435315,-2.280398,3.590740]],[[-2.182851,9.960310,-9.084740,-4.980047,-4.172831,1.502242,7.261464,-5.095223,5.346853,-3.156104,6.992412],[-3.776841,9.044151,-5.304215,0.251070,-6.368966,-9.526215,3.047430,-7.640542,2.282089,7.235641,-5.429141],[4.457593,6.186589,-8.357765,1.359314,-2.792493,3.365895,7.777583,4.191980,3.971269,-2.481656,7.785032],[1.090872,8.742862,-4.347247,7.355180,8.666876,9.361022,5.697420,-0.811262,7.747157,-4.567941,4.242922],[4.402874,-1.179252,-8.667806,-4.414780,-2.937802,-5.234076,-5.473918,0.300704,1.824767,-3.237433,9.372935],[4.605974,-5.610685,-6.222308,7.493185,-7.516969,-3.786703,-7.298043,1.437554,1.414293,-1.670008,9.381171],[-7.409969,-6.809036,-9.654932,2.423349,-9.032817,0.412956,1.119105,4.307031,4.843760,8.060695,-2.119748],[9.893192,-0.376199,3.521541,-5.297813,0.313835,0.528483,-1.659319,-6.343758,6.015917,-7.183251,-7.687901],[-7.192942,8.741550,3.925965,-0.590033,-4.766433,-8.806593,-4.386578,9.069358,-7.657726,3.368681,-6.734703],[9.397696,6.955968,9.047754,-2.075788,-5.652340,4.074461,-7.102879,-9.898684,-3.065129,-8.509725,-0.006885],[-9.826691,0.561047,-3.815495,9.304004,7.058135,-4.563051,1.017467,-7.663412,9.568086,6.024332,-6.920100],[3.512365,-6.356101,0.876635,-2.835860,4.187479,2.544964,-6.468848,9.029547,-4.304754,-3.582846,-5.576551]]], dtype = "float64")#candidate|7524|(15, 12, 11)|const|float64
bop_7525 = relay.power(var_7523.astype('float64'), const_7524.astype('float64')) # shape=(15, 12, 11)
bop_7529 = relay.bitwise_xor(const_7524.astype('int8'), var_7523.astype('int8')) # shape=(15, 12, 11)
output = relay.Tuple([bop_7525,bop_7529,])
output2 = relay.Tuple([bop_7525,bop_7529,])
F = relay.Function([var_7523,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7523,], output2)
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
