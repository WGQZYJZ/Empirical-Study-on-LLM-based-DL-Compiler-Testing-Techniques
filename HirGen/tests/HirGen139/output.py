import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_58 = relay.var("var_58", dtype = "int16", shape = ())#candidate|58|()|var|int16
var_59 = relay.var("var_59", dtype = "int16", shape = (4, 4, 3))#candidate|59|(4, 4, 3)|var|int16
bop_60 = relay.not_equal(var_58.astype('bool'), var_59.astype('bool')) # shape=(4, 4, 3)
output = bop_60
output2 = bop_60
func_70 = relay.Function([var_58,var_59,], output)
mod['func_70'] = func_70
mod = relay.transform.InferType()(mod)
mutated_mod['func_70'] = func_70
mutated_mod = relay.transform.InferType()(mutated_mod)
func_70_call = mutated_mod.get_global_var('func_70')
var_72 = relay.var("var_72", dtype = "int16", shape = ())#candidate|72|()|var|int16
var_73 = relay.var("var_73", dtype = "int16", shape = (4, 4, 3))#candidate|73|(4, 4, 3)|var|int16
call_71 = func_70_call(var_72,var_73,)
output = call_71
func_74 = relay.Function([var_72,var_73,], output)
mutated_mod['func_74'] = func_74
mutated_mod = relay.transform.InferType()(mutated_mod)
var_302 = relay.var("var_302", dtype = "float32", shape = (14, 1, 13))#candidate|302|(14, 1, 13)|var|float32
uop_303 = relay.sin(var_302.astype('float32')) # shape=(14, 1, 13)
output = uop_303
output2 = uop_303
func_316 = relay.Function([var_302,], output)
mod['func_316'] = func_316
mod = relay.transform.InferType()(mod)
mutated_mod['func_316'] = func_316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_317 = relay.var("var_317", dtype = "float32", shape = (14, 1, 13))#candidate|317|(14, 1, 13)|var|float32
func_316_call = mutated_mod.get_global_var('func_316')
call_318 = func_316_call(var_317)
output = call_318
func_319 = relay.Function([var_317], output)
mutated_mod['func_319'] = func_319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_613 = relay.var("var_613", dtype = "int64", shape = (15, 3, 10))#candidate|613|(15, 3, 10)|var|int64
const_614 = relay.const([[[-2,-10,4,-10,5,1,-9,-6,7,-5],[1,-1,-5,6,-5,8,7,-6,-7,-4],[-8,-4,3,5,9,3,3,4,-7,6]],[[3,1,1,-2,4,3,-4,-8,-6,-5],[3,7,-5,6,9,6,-7,3,2,6],[-3,7,-7,-2,-8,-10,-6,8,5,-3]],[[-7,8,6,10,7,4,-9,5,8,1],[-6,-8,7,6,-2,-8,-8,1,-6,-1],[-10,-2,10,7,9,-5,-10,-9,-2,10]],[[-6,3,5,-7,8,5,-5,-9,6,-2],[-5,-10,-1,-3,-6,7,1,5,5,-8],[-1,10,-10,2,4,-1,-2,-5,1,-8]],[[-1,8,-6,-10,6,1,-1,-5,8,6],[-3,3,9,-2,6,-7,4,10,8,-10],[-10,-4,-2,1,-6,3,4,-7,-4,3]],[[-9,-8,6,5,-10,10,6,8,-3,-9],[5,-10,-10,4,-6,-3,-9,-9,10,1],[-9,-1,-5,6,-9,-8,-8,5,-3,-1]],[[8,-5,-8,-4,-8,-10,5,3,-10,9],[5,4,-4,-3,-10,8,-10,-6,7,9],[-2,4,10,-9,-8,10,4,7,4,6]],[[4,-1,7,5,7,1,2,-7,3,-5],[-4,2,-10,5,1,-8,-3,1,6,8],[-9,3,4,-4,-5,6,5,-7,-1,8]],[[2,-6,3,-9,-1,-4,-5,2,6,6],[8,-3,4,-5,-2,4,9,1,5,-2],[-8,-9,-3,2,-10,3,2,8,-5,8]],[[7,3,2,-9,5,-7,10,-6,8,2],[-8,-3,-2,6,-7,-5,8,2,2,-9],[3,-8,2,5,3,6,-4,-10,4,-4]],[[-10,-5,6,8,-9,5,-3,-6,-8,-4],[10,-10,1,-1,-8,5,-5,-8,-8,-1],[3,10,2,10,-8,-10,-4,-5,4,9]],[[-2,-2,5,-9,6,1,-7,-7,8,8],[-4,8,-3,-5,10,1,-8,-10,2,-7],[9,-8,-10,5,4,6,2,-6,-7,-1]],[[4,-1,-4,-7,-10,7,-2,-6,-1,10],[4,3,-2,-2,9,7,5,10,-9,-8],[-1,10,9,4,7,-5,-10,9,-7,-10]],[[-4,4,5,1,-10,4,-5,3,-10,-3],[-10,8,-5,3,-7,10,2,-1,5,2],[10,-7,8,-8,-8,5,-9,10,-1,-8]],[[10,8,-2,-10,10,4,-9,4,2,6],[-4,10,6,-9,-4,5,-5,-7,-1,-5],[10,10,10,-7,-7,2,5,-7,3,10]]], dtype = "int64")#candidate|614|(15, 3, 10)|const|int64
bop_615 = relay.less(var_613.astype('bool'), relay.reshape(const_614.astype('bool'), relay.shape_of(var_613))) # shape=(15, 3, 10)
func_70_call = mod.get_global_var('func_70')
func_74_call = mutated_mod.get_global_var('func_74')
const_619 = relay.const(-8, dtype = "int16")#candidate|619|()|const|int16
var_620 = relay.var("var_620", dtype = "int16", shape = (24, 2))#candidate|620|(24, 2)|var|int16
call_618 = func_70_call(relay.reshape(const_619.astype('int16'), []), relay.reshape(var_620.astype('int16'), [4, 4, 3]), )
call_621 = func_70_call(relay.reshape(const_619.astype('int16'), []), relay.reshape(var_620.astype('int16'), [4, 4, 3]), )
output = relay.Tuple([bop_615,call_618,const_619,var_620,])
output2 = relay.Tuple([bop_615,call_621,const_619,var_620,])
func_632 = relay.Function([var_613,var_620,], output)
mod['func_632'] = func_632
mod = relay.transform.InferType()(mod)
var_633 = relay.var("var_633", dtype = "int64", shape = (15, 3, 10))#candidate|633|(15, 3, 10)|var|int64
var_634 = relay.var("var_634", dtype = "int16", shape = (24, 2))#candidate|634|(24, 2)|var|int16
output = func_632(var_633,var_634,)
func_635 = relay.Function([var_633,var_634,], output)
mutated_mod['func_635'] = func_635
mutated_mod = relay.transform.InferType()(mutated_mod)
var_673 = relay.var("var_673", dtype = "float64", shape = (6, 16, 5))#candidate|673|(6, 16, 5)|var|float64
uop_674 = relay.log10(var_673.astype('float64')) # shape=(6, 16, 5)
uop_682 = relay.asin(var_673.astype('float64')) # shape=(6, 16, 5)
output = relay.Tuple([uop_674,uop_682,])
output2 = relay.Tuple([uop_674,uop_682,])
func_687 = relay.Function([var_673,], output)
mod['func_687'] = func_687
mod = relay.transform.InferType()(mod)
mutated_mod['func_687'] = func_687
mutated_mod = relay.transform.InferType()(mutated_mod)
var_688 = relay.var("var_688", dtype = "float64", shape = (6, 16, 5))#candidate|688|(6, 16, 5)|var|float64
func_687_call = mutated_mod.get_global_var('func_687')
call_689 = func_687_call(var_688)
output = call_689
func_690 = relay.Function([var_688], output)
mutated_mod['func_690'] = func_690
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1342 = relay.var("var_1342", dtype = "float32", shape = (13, 3, 4))#candidate|1342|(13, 3, 4)|var|float32
uop_1343 = relay.atanh(var_1342.astype('float32')) # shape=(13, 3, 4)
func_70_call = mod.get_global_var('func_70')
func_74_call = mutated_mod.get_global_var('func_74')
const_1346 = relay.const(-10, dtype = "int16")#candidate|1346|()|const|int16
const_1347 = relay.const([8,-7,10,-6,-5,-1,-9,-1,-5,-1,-2,7,-3,7,9,-4,-1,-1,-8,-7,2,-8,-2,4,-7,-4,-2,-10,-5,10,5,3,6,7,3,-1,-4,5,-5,3,-6,10,-10,-4,-7,9,8,-8], dtype = "int16")#candidate|1347|(48,)|const|int16
call_1345 = func_70_call(relay.reshape(const_1346.astype('int16'), []), relay.reshape(const_1347.astype('int16'), [4, 4, 3]), )
call_1348 = func_70_call(relay.reshape(const_1346.astype('int16'), []), relay.reshape(const_1347.astype('int16'), [4, 4, 3]), )
func_70_call = mod.get_global_var('func_70')
func_74_call = mutated_mod.get_global_var('func_74')
call_1360 = func_70_call(relay.reshape(const_1346.astype('int16'), []), relay.reshape(const_1347.astype('int16'), [4, 4, 3]), )
call_1361 = func_70_call(relay.reshape(const_1346.astype('int16'), []), relay.reshape(const_1347.astype('int16'), [4, 4, 3]), )
uop_1370 = relay.cos(uop_1343.astype('float64')) # shape=(13, 3, 4)
func_632_call = mod.get_global_var('func_632')
func_635_call = mutated_mod.get_global_var('func_635')
const_1384 = relay.const([-8,-9,-7,3,7,4,2,-7,-2,-5,1,-6,-10,-9,3,-10,-2,-8,-1,3,-4,5,-6,-2,-1,1,5,-2,-4,-1,-8,-8,7,-1,4,4,1,-7,-4,-5,-5,6,-4,4,-3,7,-5,-2,-10,9,-9,3,6,8,6,-4,-8,3,-3,1,4,-7,-2,9,4,-3,5,-2,5,-9,-3,-4,-5,4,5,-4,-3,6,-10,5,-5,6,6,2,-9,-4,6,-5,6,7,-5,10,1,-1,-3,4,7,-9,-9,-6,-2,1,10,-8,-3,10,7,-6,-6,-9,5,6,-3,-5,-7,-9,3,6,-5,-2,1,-6,9,-7,1,3,-9,-8,-5,-5,3,-1,5,2,4,-8,-3,3,8,-7,8,-3,-9,1,3,6,3,4,5,-8,7,1,-2,-4,-6,9,2,-3,2,-7,-4,-5,-10,-5,-5,1,-10,-4,9,-5,2,1,6,9,1,-5,8,-10,-8,-3,-9,-5,-7,3,10,4,-2,7,10,3,1,6,7,8,-2,-6,-5,2,-3,-1,3,-6,10,-10,-9,-4,3,2,6,5,2,9,-4,1,-5,10,-8,2,10,-10,7,1,-6,9,-2,-9,8,2,-8,9,7,-1,8,5,-5,10,1,-3,-4,-8,-9,-1,-5,-8,9,-6,1,-3,1,8,5,10,-9,2,7,8,-6,-2,-3,4,2,-8,7,1,-1,4,6,1,-6,9,-2,-9,7,9,-6,3,3,10,-5,10,9,-2,-7,-4,-6,8,1,4,1,-9,-6,-6,6,-3,-6,-6,6,-3,1,-7,10,4,-3,9,-4,2,1,-3,3,-9,-6,5,5,4,-5,4,6,-5,6,4,4,-2,-3,3,8,6,-7,7,-1,7,-3,9,8,-8,-2,6,8,9,10,1,4,-3,10,-2,-4,5,1,-7,-2,5,7,7,9,9,10,9,-7,4,4,-6,-6,-6,-7,-7,-9,-2,-6,-2,-5,-4,10,8,8,5,-9,-10,4,-5,10,9,-4,6,7,3,-10,8,2,9,1,2,7,-8,-10,9,3,-1,-8,-7,6,1,-10,-10,-7,2,3,10,10,10,-9,1,-8,10,-9,2,-8,-3,-4,-1,-2,-8,1,-4,6,-2,-4,8,5,-9,-5,-10,-6,1,6,10,7,2,8,8,1,-10,2,6,-7,2,5,-7,6,8,2,-9], dtype = "int64")#candidate|1384|(450,)|const|int64
call_1383 = relay.TupleGetItem(func_632_call(relay.reshape(const_1384.astype('int64'), [15, 3, 10]), relay.reshape(const_1347.astype('int16'), [24, 2]), ), 2)
call_1385 = relay.TupleGetItem(func_635_call(relay.reshape(const_1384.astype('int64'), [15, 3, 10]), relay.reshape(const_1347.astype('int16'), [24, 2]), ), 2)
output = relay.Tuple([call_1345,const_1346,const_1347,call_1360,uop_1370,call_1383,const_1384,])
output2 = relay.Tuple([call_1348,const_1346,const_1347,call_1361,uop_1370,call_1385,const_1384,])
func_1387 = relay.Function([var_1342,], output)
mod['func_1387'] = func_1387
mod = relay.transform.InferType()(mod)
var_1388 = relay.var("var_1388", dtype = "float32", shape = (13, 3, 4))#candidate|1388|(13, 3, 4)|var|float32
output = func_1387(var_1388)
func_1389 = relay.Function([var_1388], output)
mutated_mod['func_1389'] = func_1389
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1686 = relay.var("var_1686", dtype = "float32", shape = (8, 15, 9))#candidate|1686|(8, 15, 9)|var|float32
uop_1687 = relay.atan(var_1686.astype('float32')) # shape=(8, 15, 9)
func_687_call = mod.get_global_var('func_687')
func_690_call = mutated_mod.get_global_var('func_690')
const_1692 = relay.const([-6.485354,2.939483,7.856838,-7.114297,-9.541876,-7.147278,6.334462,2.763119,0.373834,-8.971782,9.939511,-9.135201,-1.626960,5.548507,0.359672,-9.904732,8.811389,9.532871,2.656183,-0.752004,0.996543,-8.973359,9.440965,-2.089167,7.723674,-0.308039,-2.923667,-7.359580,2.933059,3.036185,-3.215611,4.289618,6.966572,-7.126754,-6.337387,6.460831,-4.917703,-4.606136,7.211903,-0.287871,4.121286,4.724706,5.354055,7.148818,4.664451,-5.729558,-1.721392,8.481342,-2.177309,-6.069037,-3.039687,-6.979845,1.305342,4.301008,9.195966,0.813983,-8.273144,1.141209,-6.427300,-1.628103,9.378715,3.077195,-0.054981,6.973104,7.640833,0.919213,0.750874,-0.371550,-1.062162,-4.565212,1.727596,4.142069,-7.405410,-9.166952,0.436766,0.677361,0.081534,-9.960947,9.272417,-7.606372,8.781129,7.545293,-7.444642,1.407485,7.454677,-2.498627,-5.714078,-2.496627,-3.082641,4.425344,6.530100,-4.828484,-2.539708,9.993890,3.995990,-0.528824,8.748176,2.834174,1.965617,2.002792,-7.503048,0.992872,4.491828,-7.690277,-4.056009,0.488832,-1.361597,-9.087321,-1.959737,-3.295703,-6.878858,-8.306314,-7.001493,6.633636,-1.492498,-6.487845,-2.811624,0.329354,3.746677,-8.874359,-5.733956,-3.364526,2.022171,5.590632,-5.771392,3.974780,-5.362915,-5.555362,-9.520836,-2.447014,-4.499451,2.944689,-5.355758,-1.620121,-9.395796,-2.483900,-1.645924,6.745116,0.629317,0.407765,2.156882,-7.846187,-0.239695,-1.023822,-9.504497,-0.766980,-8.247030,-8.476658,-4.340806,-0.837245,5.034107,2.185839,9.479030,3.098184,9.422569,-1.347485,-4.433487,-3.907000,-0.677347,8.015235,4.328055,4.212193,0.882299,5.183701,4.777926,1.994092,-3.691489,-5.588851,3.073747,-5.486110,2.685588,4.092916,-8.701319,-9.333433,4.827606,9.268921,5.714777,-7.758381,-3.448485,5.599448,1.495883,-7.901161,8.621753,-3.659101,9.597431,-5.056369,3.289667,-5.168049,0.913553,-5.209317,-8.146235,-6.180034,9.333017,-1.975971,-9.782475,6.206192,-5.686942,8.140568,-4.220978,8.377744,-1.287776,-6.740961,7.874776,3.421615,-0.016618,1.805353,-1.556762,-6.919158,-5.125711,0.644071,-8.506344,5.982892,5.592938,4.820737,-4.033448,2.159274,-3.586165,-6.056942,-4.632298,-6.426357,-2.392946,9.470306,6.075497,-6.504104,-2.958718,-9.937572,-6.146699,-7.212730,-9.921039,7.605214,-5.566754,-2.567838,6.396512,-9.479238,-0.231743,-3.603209,5.189082,3.567312,1.518285,-1.839960,-3.061280,2.338437,-9.386540,-4.633323,5.625254,6.677024,-2.678284,-2.221006,6.350597,4.998025,7.605558,-3.164735,0.987618,-8.850807,0.750684,-0.557343,2.484167,-5.638853,7.571275,5.213297,-5.040807,-1.753188,-2.524076,-3.185282,-3.743717,6.757873,6.503551,-9.085487,-7.917185,-7.383235,6.526969,8.689572,-4.910115,2.537339,-0.659920,-9.414500,0.949553,0.372764,1.115758,5.391908,3.479598,8.384303,-7.835569,9.538160,-7.605883,-1.807273,-5.565576,1.316447,4.842041,5.628759,0.628631,5.300324,-0.060507,-7.300518,-8.284494,3.248793,-1.985806,4.636357,-7.702754,1.859658,-0.215296,9.039716,6.955458,4.811109,7.132599,-0.508232,-0.576189,0.161976,-1.342443,-7.291212,-8.057912,-7.269351,-1.969860,7.626477,-6.788807,-8.015243,5.272256,-7.974024,-0.974160,0.511802,-6.302217,-9.621190,7.851089,8.962597,0.889603,7.066128,-3.249027,-0.382964,6.051501,2.304236,6.560103,-1.837893,1.371417,6.116887,-7.469278,2.172884,4.302238,5.131282,-7.693391,-1.427011,-7.700023,4.914712,-7.094260,3.744407,3.407758,2.823027,-1.104207,2.238855,-6.816422,0.417455,-3.608705,3.198339,-6.170020,-9.641305,-8.478347,-1.559771,-8.961735,2.297980,-3.072687,-3.638175,8.526303,-1.717325,9.009631,-1.718836,-5.781440,-4.023746,-2.584168,-8.673261,-4.244516,8.643891,-9.167087,8.354962,5.072778,9.066458,-9.048096,-3.364947,5.611300,6.689633,-0.309660,0.486291,-2.908254,5.414938,3.630361,5.075996,8.284534,-3.251766,5.082134,-7.559477,-3.858870,-9.062329,-7.132181,6.953272,1.179868,-7.941437,-2.024602,-3.440961,-1.261540,7.785141,-6.873261,6.344823,-4.058775,3.556011,-2.125483,-2.729609,7.438876,7.246432,0.579277,0.114966,3.760016,8.519477,5.207978,-7.259758,6.794310,-0.871825,7.991218,8.304193,9.323577,3.680614,3.574584,1.051050,-1.714104,-3.937331,6.559531,-5.240330,0.268768,-8.714837,3.815285,-0.471404,-1.573301,-0.207503,6.889367,4.760504,-4.374899,-7.136013,6.629785,-9.113218,-0.429974,3.947859,1.792114,-3.857446,7.316107,8.856214,-4.579158,-6.275496,-1.086333,-0.234636,-1.652218,1.750539,-4.202147,-5.523928,3.133016,9.808088,3.680747,4.591105,-9.613525,-0.246597,-5.208978,-7.313840,1.236801,4.859004,-4.272845,3.079479,-9.667774,2.306408,-4.850441,-2.071606,8.503680,6.313248,-2.956486,9.509095,3.080864,9.021634,1.270734,-9.741229,-0.437291,1.396251,4.771259,2.933870,3.675517,-8.182261], dtype = "float64")#candidate|1692|(480,)|const|float64
call_1691 = relay.TupleGetItem(func_687_call(relay.reshape(const_1692.astype('float64'), [6, 16, 5])), 1)
call_1693 = relay.TupleGetItem(func_690_call(relay.reshape(const_1692.astype('float64'), [6, 16, 5])), 1)
func_687_call = mod.get_global_var('func_687')
func_690_call = mutated_mod.get_global_var('func_690')
call_1695 = relay.TupleGetItem(func_687_call(relay.reshape(call_1691.astype('float64'), [6, 16, 5])), 0)
call_1696 = relay.TupleGetItem(func_690_call(relay.reshape(call_1691.astype('float64'), [6, 16, 5])), 0)
func_70_call = mod.get_global_var('func_70')
func_74_call = mutated_mod.get_global_var('func_74')
const_1699 = relay.const(-4, dtype = "int16")#candidate|1699|()|const|int16
const_1700 = relay.const([-10,-3,6,6,-5,-4,-4,3,8,-9,6,-5,-1,-6,9,9,4,-4,-3,-10,-9,3,7,-5,10,6,-8,-6,4,-5,3,2,-5,8,9,6,-4,3,-5,-8,2,10,5,-10,-7,-1,6,-10], dtype = "int16")#candidate|1700|(48,)|const|int16
call_1698 = func_70_call(relay.reshape(const_1699.astype('int16'), []), relay.reshape(const_1700.astype('int16'), [4, 4, 3]), )
call_1701 = func_70_call(relay.reshape(const_1699.astype('int16'), []), relay.reshape(const_1700.astype('int16'), [4, 4, 3]), )
func_687_call = mod.get_global_var('func_687')
func_690_call = mutated_mod.get_global_var('func_690')
call_1702 = relay.TupleGetItem(func_687_call(relay.reshape(const_1692.astype('float64'), [6, 16, 5])), 0)
call_1703 = relay.TupleGetItem(func_690_call(relay.reshape(const_1692.astype('float64'), [6, 16, 5])), 0)
output = relay.Tuple([uop_1687,call_1691,const_1692,call_1695,call_1698,const_1699,const_1700,call_1702,])
output2 = relay.Tuple([uop_1687,call_1693,const_1692,call_1696,call_1701,const_1699,const_1700,call_1703,])
func_1737 = relay.Function([var_1686,], output)
mod['func_1737'] = func_1737
mod = relay.transform.InferType()(mod)
mutated_mod['func_1737'] = func_1737
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1738 = relay.var("var_1738", dtype = "float32", shape = (8, 15, 9))#candidate|1738|(8, 15, 9)|var|float32
func_1737_call = mutated_mod.get_global_var('func_1737')
call_1739 = func_1737_call(var_1738)
output = call_1739
func_1740 = relay.Function([var_1738], output)
mutated_mod['func_1740'] = func_1740
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1799 = relay.var("var_1799", dtype = "uint16", shape = (4, 6, 8))#candidate|1799|(4, 6, 8)|var|uint16
var_1800 = relay.var("var_1800", dtype = "uint16", shape = (4, 6, 8))#candidate|1800|(4, 6, 8)|var|uint16
bop_1801 = relay.logical_xor(var_1799.astype('uint16'), relay.reshape(var_1800.astype('uint16'), relay.shape_of(var_1799))) # shape=(4, 6, 8)
bop_1805 = relay.greater(var_1799.astype('bool'), relay.reshape(bop_1801.astype('bool'), relay.shape_of(var_1799))) # shape=(4, 6, 8)
func_1387_call = mod.get_global_var('func_1387')
func_1389_call = mutated_mod.get_global_var('func_1389')
const_1820 = relay.const([[0.845132,7.164342,9.249864,9.777312,6.054256,-5.856912,-6.294398,1.266269,-2.024740,-2.961429,-2.574196,-5.648800,2.534301,8.627005,-4.262943,0.898165,-6.634248,-5.234744,4.148975,5.803245,-2.577581,-4.011984,-0.529711,-0.850784,-2.960906,9.554532,-4.120396,1.575157,5.174929,-1.885328,-1.065586,-6.940647,-4.814549,3.016994,-2.332805,8.958562,-3.648479,9.690778,8.002155,-3.201546,-7.500496,3.332034,7.833999,8.230140,8.559083,-0.413724,4.376922,-8.643482,5.711924,-8.299937,3.559756,-8.592676],[9.869630,-1.530060,0.765296,-4.435735,9.824693,7.737208,-8.658960,7.249478,-9.324194,-1.622666,-9.413035,4.667456,-0.773414,-3.522624,9.837692,4.825246,-4.483604,-0.719070,-4.309012,-3.615409,-0.969139,-9.503797,-4.685945,-3.339388,8.019683,-7.598345,-1.339416,8.444269,7.670253,-6.652908,4.581144,-3.824947,1.939141,4.582587,6.625999,7.970697,5.619708,6.751742,-9.374982,-1.096560,-4.383529,1.526909,3.057326,1.072905,-8.479310,6.579857,4.687605,-6.065852,-4.670623,0.288491,5.480640,1.485296],[-9.381734,-8.888976,3.424036,0.685942,2.718664,-3.959931,3.386175,-2.822054,7.899392,9.361024,6.734208,5.897468,-2.855857,2.561100,-6.091968,-6.579328,0.427562,6.270119,-9.301334,-6.044999,7.323623,-7.377445,-5.326707,1.395906,-6.563938,1.192949,-6.763883,-2.545205,1.024932,-6.584396,-5.558616,-2.494227,6.128488,-8.464110,-4.194791,3.530857,5.752965,4.028442,-5.157196,2.851585,7.658517,-9.210272,-2.129648,-3.704885,4.613203,6.071531,-4.941460,6.159877,7.974548,3.472522,9.747644,5.956195]], dtype = "float32")#candidate|1820|(3, 52)|const|float32
call_1819 = relay.TupleGetItem(func_1387_call(relay.reshape(const_1820.astype('float32'), [13, 3, 4])), 4)
call_1821 = relay.TupleGetItem(func_1389_call(relay.reshape(const_1820.astype('float32'), [13, 3, 4])), 4)
output = relay.Tuple([bop_1805,call_1819,const_1820,])
output2 = relay.Tuple([bop_1805,call_1821,const_1820,])
func_1824 = relay.Function([var_1799,var_1800,], output)
mod['func_1824'] = func_1824
mod = relay.transform.InferType()(mod)
mutated_mod['func_1824'] = func_1824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1824_call = mutated_mod.get_global_var('func_1824')
var_1826 = relay.var("var_1826", dtype = "uint16", shape = (4, 6, 8))#candidate|1826|(4, 6, 8)|var|uint16
var_1827 = relay.var("var_1827", dtype = "uint16", shape = (4, 6, 8))#candidate|1827|(4, 6, 8)|var|uint16
call_1825 = func_1824_call(var_1826,var_1827,)
output = call_1825
func_1828 = relay.Function([var_1826,var_1827,], output)
mutated_mod['func_1828'] = func_1828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1923 = relay.var("var_1923", dtype = "float32", shape = (15, 13, 10))#candidate|1923|(15, 13, 10)|var|float32
uop_1924 = relay.exp(var_1923.astype('float32')) # shape=(15, 13, 10)
uop_1939 = relay.acos(var_1923.astype('float64')) # shape=(15, 13, 10)
func_1387_call = mod.get_global_var('func_1387')
func_1389_call = mutated_mod.get_global_var('func_1389')
const_1947 = relay.const([5.541023,0.214487,1.881273,5.755638,4.941372,5.619565,-5.771255,1.695683,-6.250105,-7.027748,1.334498,2.475658,1.272650,8.469560,-7.668290,3.580052,3.697370,-8.310185,5.090682,-6.849736,6.620454,-4.116803,7.413263,8.549911,8.534153,5.374284,-2.501459,-8.739586,-6.101847,3.309475,-0.616459,-3.764424,7.687802,-0.909518,-6.713630,-0.533822,-3.158507,8.911017,-8.260976,4.623389,6.573258,-0.165409,-0.901156,8.028683,-7.396899,3.244483,6.630319,-0.824328,-9.191876,-4.708237,4.793673,4.792165,2.055405,7.885758,4.410473,4.263735,2.191178,-7.202469,-4.357584,-5.486840,-3.316783,6.155928,6.405173,1.821321,-7.634374,-1.414906,-2.824267,9.734145,5.810613,5.113560,-8.571399,5.335397,-7.656709,6.269386,5.301419,3.336121,3.285748,7.637619,-6.949000,-1.054894,-6.406790,-5.110530,-6.526029,-8.699496,-5.068684,-9.099943,-5.486349,-8.013949,-4.027944,-1.792081,2.196147,8.477122,-6.824784,9.214724,9.690420,-2.719223,-3.339303,-7.369591,-8.687956,-8.981394,-4.809971,6.601763,-1.636926,5.466093,7.810061,-7.028374,0.754721,8.675614,8.230949,-7.068799,0.533568,-4.471149,5.897684,-1.692599,-1.752584,-5.425502,-1.461352,6.486890,9.697949,7.636213,-6.545395,4.283786,4.606356,-1.007449,2.093775,-5.592150,1.100062,8.695807,6.514364,-6.046579,-2.454699,5.377465,0.526504,-4.257871,9.399116,9.427661,8.334557,-5.139715,-7.009706,8.800071,7.764229,-2.756147,5.096197,-0.767469,9.768743,-1.529044,3.651915,-1.764917,-8.140146,-2.136487,-6.411688,-6.981758,-5.655695,8.758354,0.301861,3.945588], dtype = "float32")#candidate|1947|(156,)|const|float32
call_1946 = relay.TupleGetItem(func_1387_call(relay.reshape(const_1947.astype('float32'), [13, 3, 4])), 1)
call_1948 = relay.TupleGetItem(func_1389_call(relay.reshape(const_1947.astype('float32'), [13, 3, 4])), 1)
func_632_call = mod.get_global_var('func_632')
func_635_call = mutated_mod.get_global_var('func_635')
var_1956 = relay.var("var_1956", dtype = "int64", shape = (150, 3))#candidate|1956|(150, 3)|var|int64
var_1957 = relay.var("var_1957", dtype = "int16", shape = (4, 12))#candidate|1957|(4, 12)|var|int16
call_1955 = relay.TupleGetItem(func_632_call(relay.reshape(var_1956.astype('int64'), [15, 3, 10]), relay.reshape(var_1957.astype('int16'), [24, 2]), ), 1)
call_1958 = relay.TupleGetItem(func_635_call(relay.reshape(var_1956.astype('int64'), [15, 3, 10]), relay.reshape(var_1957.astype('int16'), [24, 2]), ), 1)
bop_1981 = relay.bitwise_or(uop_1939.astype('uint8'), relay.reshape(var_1923.astype('uint8'), relay.shape_of(uop_1939))) # shape=(15, 13, 10)
func_687_call = mod.get_global_var('func_687')
func_690_call = mutated_mod.get_global_var('func_690')
var_1998 = relay.var("var_1998", dtype = "float64", shape = (8, 60))#candidate|1998|(8, 60)|var|float64
call_1997 = relay.TupleGetItem(func_687_call(relay.reshape(var_1998.astype('float64'), [6, 16, 5])), 0)
call_1999 = relay.TupleGetItem(func_690_call(relay.reshape(var_1998.astype('float64'), [6, 16, 5])), 0)
func_1824_call = mod.get_global_var('func_1824')
func_1828_call = mutated_mod.get_global_var('func_1828')
var_2002 = relay.var("var_2002", dtype = "uint16", shape = (96, 2))#candidate|2002|(96, 2)|var|uint16
call_2001 = relay.TupleGetItem(func_1824_call(relay.reshape(var_2002.astype('uint16'), [4, 6, 8]), relay.reshape(var_2002.astype('uint16'), [4, 6, 8]), ), 1)
call_2003 = relay.TupleGetItem(func_1828_call(relay.reshape(var_2002.astype('uint16'), [4, 6, 8]), relay.reshape(var_2002.astype('uint16'), [4, 6, 8]), ), 1)
uop_2009 = relay.erf(uop_1924.astype('float64')) # shape=(15, 13, 10)
output = relay.Tuple([call_1946,const_1947,call_1955,var_1956,var_1957,bop_1981,call_1997,var_1998,call_2001,var_2002,uop_2009,])
output2 = relay.Tuple([call_1948,const_1947,call_1958,var_1956,var_1957,bop_1981,call_1999,var_1998,call_2003,var_2002,uop_2009,])
func_2019 = relay.Function([var_1923,var_1956,var_1957,var_1998,var_2002,], output)
mod['func_2019'] = func_2019
mod = relay.transform.InferType()(mod)
mutated_mod['func_2019'] = func_2019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2019_call = mutated_mod.get_global_var('func_2019')
var_2021 = relay.var("var_2021", dtype = "float32", shape = (15, 13, 10))#candidate|2021|(15, 13, 10)|var|float32
var_2022 = relay.var("var_2022", dtype = "int64", shape = (150, 3))#candidate|2022|(150, 3)|var|int64
var_2023 = relay.var("var_2023", dtype = "int16", shape = (4, 12))#candidate|2023|(4, 12)|var|int16
var_2024 = relay.var("var_2024", dtype = "float64", shape = (8, 60))#candidate|2024|(8, 60)|var|float64
var_2025 = relay.var("var_2025", dtype = "uint16", shape = (96, 2))#candidate|2025|(96, 2)|var|uint16
call_2020 = func_2019_call(var_2021,var_2022,var_2023,var_2024,var_2025,)
output = call_2020
func_2026 = relay.Function([var_2021,var_2022,var_2023,var_2024,var_2025,], output)
mutated_mod['func_2026'] = func_2026
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2223 = relay.var("var_2223", dtype = "float64", shape = (13, 2, 11))#candidate|2223|(13, 2, 11)|var|float64
uop_2224 = relay.acosh(var_2223.astype('float64')) # shape=(13, 2, 11)
uop_2227 = relay.exp(uop_2224.astype('float32')) # shape=(13, 2, 11)
output = relay.Tuple([uop_2227,])
output2 = relay.Tuple([uop_2227,])
func_2232 = relay.Function([var_2223,], output)
mod['func_2232'] = func_2232
mod = relay.transform.InferType()(mod)
mutated_mod['func_2232'] = func_2232
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2233 = relay.var("var_2233", dtype = "float64", shape = (13, 2, 11))#candidate|2233|(13, 2, 11)|var|float64
func_2232_call = mutated_mod.get_global_var('func_2232')
call_2234 = func_2232_call(var_2233)
output = call_2234
func_2235 = relay.Function([var_2233], output)
mutated_mod['func_2235'] = func_2235
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2433 = relay.var("var_2433", dtype = "float32", shape = (5, 2, 15))#candidate|2433|(5, 2, 15)|var|float32
const_2434 = relay.const([[[0.919329,-2.849402,9.620763,1.966488,-7.216442,-3.000001,0.677956,7.118289,-7.514671,-3.698422,-0.457515,8.466450,-9.626269,-9.470200,-2.899827],[0.109797,2.103849,1.706121,7.707541,0.299972,-8.745970,7.940553,9.776929,-3.736728,-8.664577,-6.101497,-7.026050,7.065941,-8.211915,3.219725]],[[-4.534922,-2.694106,4.549850,-0.925198,-9.285801,-2.686004,9.868326,-2.607974,-3.335879,-2.886803,5.918822,-7.564879,-9.844891,6.935347,1.756866],[-7.319740,5.994302,6.330170,-6.034731,-9.192092,9.611097,8.941009,-5.029442,7.954608,-8.721040,2.713239,-7.353463,8.735084,-4.732067,-8.383194]],[[9.748502,0.161202,8.394743,1.542138,-9.557344,3.136475,2.894115,-8.762811,-2.575541,-1.009806,7.857291,9.192714,0.114974,-8.874383,5.132333],[3.234693,0.168150,5.792518,-7.938783,-0.727210,-4.163074,-7.840678,-9.360105,0.152413,9.100456,2.024830,-3.897276,-6.060791,7.880188,0.488468]],[[1.116465,-0.345318,5.275768,-4.709619,-8.423226,-8.435878,-7.649239,-1.834723,7.299413,8.845241,-2.971362,5.709802,2.565707,-2.574915,-9.429642],[2.596749,8.246333,2.134534,-3.591415,-6.395573,-4.196841,9.810965,2.784222,-4.789465,-9.176760,8.791466,-7.910375,4.308580,2.631777,9.349026]],[[4.586721,4.474639,-2.941088,9.457495,-2.946018,2.567481,-0.359222,9.678363,8.399336,-3.783470,-1.637165,-5.406509,-7.116557,-7.823681,7.043977],[2.405128,8.979927,8.537031,4.313639,-8.918091,-5.195038,6.760650,-8.969340,9.564692,-5.806446,1.767630,4.363221,5.045338,3.956110,3.660451]]], dtype = "float32")#candidate|2434|(5, 2, 15)|const|float32
bop_2435 = relay.power(var_2433.astype('float32'), relay.reshape(const_2434.astype('float32'), relay.shape_of(var_2433))) # shape=(5, 2, 15)
func_316_call = mod.get_global_var('func_316')
func_319_call = mutated_mod.get_global_var('func_319')
const_2442 = relay.const([-4.329267,-2.443254,2.961368,1.674783,6.605520,-2.124281,2.767322,0.825218,-9.039700,-7.270509,7.375472,4.289739,3.401059,6.094668,-5.864741,-2.754660,0.591495,9.180398,-7.628716,-3.147616,-7.531991,1.609541,9.548273,-2.703107,5.714044,4.810445,0.007839,1.278640,2.139454,5.100355,8.406097,-9.730344,0.009297,-1.548045,-9.582996,1.843548,6.921850,7.176176,7.729338,-0.397248,-0.586934,9.364295,-2.551555,-0.319177,2.042789,-0.428969,3.736482,6.815912,-0.003644,-3.671006,-2.300248,3.956110,9.161941,7.810860,3.990367,6.834261,0.826349,9.854577,7.109649,5.083818,6.566948,-3.728304,8.796251,3.675648,9.670151,-4.362503,5.971964,2.165202,-5.092502,-3.453193,-9.759192,-6.534083,-8.332979,-3.883651,7.333588,6.603823,2.472688,-4.929332,9.951634,-2.303546,4.440146,2.615878,-7.892847,9.919401,4.938469,-0.255209,0.674929,1.322943,-9.795588,-7.832444,-2.431244,8.495236,8.780748,-1.846713,9.232174,9.378809,5.059380,-9.446628,4.968114,1.510214,8.232144,-2.340118,-0.265829,-1.470933,9.011324,-9.153770,-4.153840,4.936000,6.029738,7.177366,-5.995159,-9.445128,0.819517,-3.526658,-6.344800,9.413832,2.074676,4.460158,3.120744,3.051542,-5.374779,-9.193790,2.979318,-5.469072,3.128163,1.850230,-1.664139,-0.215402,-2.868847,-3.822121,-7.795070,-9.055783,7.409712,3.712922,-8.405626,-8.247958,-6.740208,3.871570,-9.664727,9.992177,1.385324,-6.486832,-4.071589,9.463974,2.062708,4.009394,7.885415,0.159853,9.563631,-1.554404,7.583429,-2.757759,2.862941,7.039875,9.129917,-6.236295,-1.815191,-5.063544,7.628601,0.681321,5.196052,-1.714463,1.427467,-9.815718,-8.884555,-1.953867,1.331085,0.979876,-4.974617,-5.862170,5.275609,4.188781,6.764957,-4.734480,3.349797,1.039511,2.831166,-8.563843,-5.004265,0.244268,1.627312,-5.725677], dtype = "float32")#candidate|2442|(182,)|const|float32
call_2441 = func_316_call(relay.reshape(const_2442.astype('float32'), [14, 1, 13]))
call_2443 = func_316_call(relay.reshape(const_2442.astype('float32'), [14, 1, 13]))
func_1387_call = mod.get_global_var('func_1387')
func_1389_call = mutated_mod.get_global_var('func_1389')
var_2447 = relay.var("var_2447", dtype = "float32", shape = (156,))#candidate|2447|(156,)|var|float32
call_2446 = relay.TupleGetItem(func_1387_call(relay.reshape(var_2447.astype('float32'), [13, 3, 4])), 0)
call_2448 = relay.TupleGetItem(func_1389_call(relay.reshape(var_2447.astype('float32'), [13, 3, 4])), 0)
uop_2480 = relay.erf(bop_2435.astype('float64')) # shape=(5, 2, 15)
uop_2482 = relay.sin(const_2434.astype('float32')) # shape=(5, 2, 15)
bop_2488 = relay.add(uop_2482.astype('float64'), relay.reshape(const_2434.astype('float64'), relay.shape_of(uop_2482))) # shape=(5, 2, 15)
output = relay.Tuple([call_2441,const_2442,call_2446,var_2447,uop_2480,bop_2488,])
output2 = relay.Tuple([call_2443,const_2442,call_2448,var_2447,uop_2480,bop_2488,])
func_2502 = relay.Function([var_2433,var_2447,], output)
mod['func_2502'] = func_2502
mod = relay.transform.InferType()(mod)
mutated_mod['func_2502'] = func_2502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2502_call = mutated_mod.get_global_var('func_2502')
var_2504 = relay.var("var_2504", dtype = "float32", shape = (5, 2, 15))#candidate|2504|(5, 2, 15)|var|float32
var_2505 = relay.var("var_2505", dtype = "float32", shape = (156,))#candidate|2505|(156,)|var|float32
call_2503 = func_2502_call(var_2504,var_2505,)
output = call_2503
func_2506 = relay.Function([var_2504,var_2505,], output)
mutated_mod['func_2506'] = func_2506
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2543 = relay.const(5.202862, dtype = "float32")#candidate|2543|()|const|float32
var_2544 = relay.var("var_2544", dtype = "float32", shape = (15, 10, 5))#candidate|2544|(15, 10, 5)|var|float32
bop_2545 = relay.power(const_2543.astype('float32'), var_2544.astype('float32')) # shape=(15, 10, 5)
bop_2548 = relay.subtract(const_2543.astype('int64'), bop_2545.astype('int64')) # shape=(15, 10, 5)
func_1387_call = mod.get_global_var('func_1387')
func_1389_call = mutated_mod.get_global_var('func_1389')
var_2557 = relay.var("var_2557", dtype = "float32", shape = (156,))#candidate|2557|(156,)|var|float32
call_2556 = relay.TupleGetItem(func_1387_call(relay.reshape(var_2557.astype('float32'), [13, 3, 4])), 0)
call_2558 = relay.TupleGetItem(func_1389_call(relay.reshape(var_2557.astype('float32'), [13, 3, 4])), 0)
output = relay.Tuple([bop_2548,call_2556,var_2557,])
output2 = relay.Tuple([bop_2548,call_2558,var_2557,])
func_2560 = relay.Function([var_2544,var_2557,], output)
mod['func_2560'] = func_2560
mod = relay.transform.InferType()(mod)
mutated_mod['func_2560'] = func_2560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2560_call = mutated_mod.get_global_var('func_2560')
var_2562 = relay.var("var_2562", dtype = "float32", shape = (15, 10, 5))#candidate|2562|(15, 10, 5)|var|float32
var_2563 = relay.var("var_2563", dtype = "float32", shape = (156,))#candidate|2563|(156,)|var|float32
call_2561 = func_2560_call(var_2562,var_2563,)
output = call_2561
func_2564 = relay.Function([var_2562,var_2563,], output)
mutated_mod['func_2564'] = func_2564
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2806 = relay.var("var_2806", dtype = "bool", shape = (6, 6, 10))#candidate|2806|(6, 6, 10)|var|bool
const_2807 = relay.const([[[True,True,True,True,True,False,False,True,False,False],[False,True,True,True,False,True,False,True,True,True],[False,True,True,True,False,True,False,True,False,False],[True,True,False,False,False,True,True,True,False,True],[True,False,False,False,True,False,False,True,False,True],[False,False,False,False,True,True,True,True,False,True]],[[False,False,False,False,False,True,True,True,False,True],[True,True,False,True,True,True,False,True,True,False],[False,True,False,True,True,False,False,False,True,False],[True,True,False,False,True,True,True,False,False,True],[False,True,False,False,True,True,True,True,True,False],[True,True,False,True,False,True,True,False,False,True]],[[True,True,False,True,True,False,False,False,False,True],[True,False,False,True,False,True,True,False,False,False],[False,True,True,False,True,False,False,False,False,False],[True,True,True,False,True,True,False,True,True,False],[False,True,True,True,False,True,False,True,True,True],[True,False,False,True,False,True,True,False,False,True]],[[False,True,True,False,True,False,True,True,True,False],[False,False,True,True,True,False,False,True,True,False],[False,True,False,True,False,False,False,True,True,False],[False,True,False,True,True,True,True,False,True,True],[True,True,True,False,False,False,False,False,True,False],[False,False,True,False,True,True,True,True,False,False]],[[False,False,True,False,False,True,True,True,True,False],[False,False,True,True,True,True,True,True,False,True],[True,False,True,False,True,False,True,False,True,True],[False,True,False,True,True,False,False,True,True,False],[True,False,False,True,True,True,False,True,True,False],[False,False,True,True,True,False,True,False,False,False]],[[False,False,False,False,True,True,False,False,False,True],[False,False,True,False,True,True,False,True,False,True],[False,False,True,True,True,False,True,False,True,True],[False,True,True,False,True,False,False,True,False,False],[False,False,False,False,True,True,True,True,True,True],[False,True,True,True,False,False,False,True,False,True]]], dtype = "bool")#candidate|2807|(6, 6, 10)|const|bool
bop_2808 = relay.logical_and(var_2806.astype('bool'), relay.reshape(const_2807.astype('bool'), relay.shape_of(var_2806))) # shape=(6, 6, 10)
func_2019_call = mod.get_global_var('func_2019')
func_2026_call = mutated_mod.get_global_var('func_2026')
const_2821 = relay.const([-7.125615,-3.049236,-0.098353,2.576121,4.212533,-5.663624,-1.762355,0.007016,-6.624282,9.292876,8.603324,-6.809801,-3.825304,-2.165833,-2.922838,-0.797706,-2.102657,5.975413,-5.364482,-8.141655,3.765554,4.236939,-8.077747,7.405917,7.627627,4.897724,-3.316297,6.457334,2.381916,-1.639878,-2.809602,-3.444231,-4.553898,4.641945,-6.855341,-2.900571,-5.135164,-9.628147,-0.801488,8.282902,-8.857264,0.376699,7.125193,6.340377,-2.610276,-6.333132,-7.337525,2.613325,-5.475211,-6.774844,3.718877,2.323690,-4.198297,-3.871283,6.832092,-0.626493,-5.711733,-4.143530,8.916874,-7.517729,-6.997178,-9.421755,-8.725310,5.574247,-4.808394,9.103778,-4.598580,4.208453,-5.309930,7.392568,-7.500901,-8.242940,3.900931,-1.091115,-8.651650,2.125868,0.407205,-1.020167,7.989045,-5.841098,6.973618,2.972686,-5.302632,-8.011400,-2.100984,5.387621,7.106420,2.566320,-1.495534,0.588798,5.824364,5.255607,-9.671852,-9.913515,1.603772,6.496370,-0.890919,-4.089309,-8.321802,-6.569843,6.357330,5.235368,5.446648,9.721199,-9.148736,-3.804791,9.371856,-2.804815,9.423685,-2.683473,1.015275,3.806798,-4.957117,3.741947,-5.337003,-3.616607,7.038398,9.686655,-9.255051,-9.011459,3.521516,-4.609071,8.992215,2.984272,3.792319,8.544943,8.299323,0.524714,9.206653,-7.344795,-5.425386,7.277673,-4.847239,-7.328338,4.781139,4.955243,4.459480,-6.067368,-6.711343,-7.067055,4.885165,4.559032,-3.570646,-5.252780,2.938223,-5.370905,4.986438,1.066038,-8.245318,4.180679,-2.983484,-4.234745,-2.653102,-9.198446,-1.411201,7.211575,6.654170,6.605219,5.668336,4.250473,-5.041962,-8.804013,5.570094,-0.757332,7.959253,7.237464,-6.910510,5.546599,-3.528020,-7.979105,-6.954443,-6.235838,-1.772164,-8.278923,-7.384349,-9.432541,0.662387,-7.850734,-4.293784,-2.047681,-4.183932,2.571705,8.138715,-2.966251,0.033278,0.863336,-4.922296,8.213266,7.800714,-0.596193,9.084805,-5.892475,6.971464,4.422504,0.162270,0.812468,4.710230,7.651532,2.052064,3.910114,-4.356989,2.635094,-2.370996,6.159126,-9.235624,5.165357,-8.514449,-4.560794,6.119061,4.382454,6.979620,-4.724630,0.834895,2.846033,8.447985,9.774913,6.208774,-4.456189,0.663701,9.418045,3.534510,8.650517,3.856880,4.338287,7.535628,1.350488,6.552586,-6.444333,8.425526,-2.171312,-3.078449,-6.889900,-7.860020,9.902544,-0.113061,7.038449,-9.428056,7.684680,-4.571334,-0.088791,9.696054,-9.484376,2.052212,-5.733517,-5.915446,-0.194311,-7.431167,8.288290,2.119865,4.214952,2.093614,-0.145993,0.145950,6.423503,-1.292319,-7.638118,-5.031807,9.109123,3.820595,-1.457805,-5.302103,-8.812679,-9.347669,5.184106,-4.007321,1.092136,2.438025,2.967593,-9.149380,-9.858711,-9.827799,-3.985050,4.886135,8.478325,8.458944,-1.249032,-2.417807,9.038924,-4.075838,-8.903914,4.167482,1.728422,6.226589,5.942519,3.379253,9.917877,-2.838556,-9.028930,5.380719,-1.931272,-8.638920,-9.695930,1.583558,8.154415,-1.797813,7.727458,9.601457,-7.255734,7.947849,-8.082100,6.502395,6.434395,-2.601437,3.988954,8.639983,-5.912645,-9.420191,-8.799643,-6.265803,-2.872761,6.978305,-1.739502,-7.549759,-5.740457,5.440918,-0.463146,-6.439245,-1.452009,-4.685119,-0.077295,-6.405701,4.359052,1.801657,-8.317578,7.523138,-4.079688,-9.691739,5.363383,9.658163,4.381521,5.624654,3.494653,7.386608,-6.039605,2.160091,6.491945,9.121423,-2.834757,-1.679729,5.452780,5.334577,-9.552770,-7.894231,-2.587963,0.222460,-2.442142,-5.628981,-1.719052,-5.292776,6.914986,6.506716,3.217033,6.054553,4.704932,-2.678684,2.902710,-2.414245,-9.152268,0.405526,-0.726695,-2.205767,5.348974,-4.559443,-8.252699,-0.773224,-8.953450,-0.390150,6.822344,-4.499685,9.689989,1.627096,-5.558597,-4.611572,-7.684984,-5.519747,8.470008,-2.907551,0.043000,-7.371332,3.593192,3.692111,4.745790,8.044861,4.711755,4.665927,-2.053207,1.853217,0.391499,6.434090,3.346332,-8.006794,-3.166177,-1.290241,-1.349091,7.636276,0.976764,3.245517,-8.034051,3.399830,-9.911387,-6.442576,3.942726,-6.482651,-8.989475,7.490300,0.093030,-0.226231,-8.555662,3.834492,0.672598,-8.419268,1.080536,2.340483,-0.967209,8.028309,-8.065290,9.684013,7.107152,-3.041866,-2.519904,6.850157,2.226185,6.606336,-1.356633,-6.652783,-2.648799,9.447149,3.429768,2.884674,9.613394,-7.169769,0.029177,-2.016635,0.912150,-7.218890,-1.830558,2.938810,3.975501,4.591664,6.434573,1.807604,-9.849656,5.894790,-0.750684,3.253617,2.762295,8.221893,3.676663,2.048026,-3.840433,-3.577677,-7.481029,-7.026033,8.214470,7.004747,-0.199176,-8.309920,6.092125,-5.538181,-5.799824,-3.742854,0.059989,-8.285140,8.222603,-1.657025,1.389193,-9.924298,-7.543743,8.313499,-5.750328,6.104516,-9.648088,6.967800,6.874761,2.951349,9.025750,-4.110545,4.291690,7.687311,-8.943499,-8.497465,2.976147,5.414888,8.150428,5.713373,-6.831533,-4.477643,-3.172301,-6.159026,1.860880,7.517108,7.136235,-3.172781,5.549531,6.326554,2.333579,6.915934,-0.051935,-4.615373,-0.603884,3.767185,-2.455889,3.519942,2.444380,9.664234,9.871734,8.035392,-7.095564,3.008039,-1.292696,1.942337,-5.511217,-1.019722,-5.750459,-1.850895,-6.828877,5.879909,-1.193660,9.077630,-3.693149,-5.663443,4.793298,2.798284,3.914381,8.637320,6.796798,5.342988,-9.241175,3.621237,1.229395,7.604019,9.249354,-8.599736,3.920435,-1.265517,-4.081876,2.495322,-0.378468,1.641077,2.693456,8.980871,-4.545333,-1.246721,-5.703266,5.386981,7.213555,2.168824,9.524372,-4.697225,8.603364,-1.589111,-4.968957,-2.400120,-9.296764,-5.856316,-5.967962,6.499754,1.220714,6.118252,1.586756,0.646504,9.957747,7.624806,-3.360181,3.958546,-1.863888,-8.034561,7.004165,-0.697848,-0.421537,3.217061,-1.745082,5.863907,-9.555283,-8.315974,6.900425,3.626666,-7.394404,9.842161,-5.332342,3.840994,3.743154,6.545527,-7.563581,-7.511826,1.309202,7.923725,-7.527783,2.276530,-7.122661,-3.798619,8.376801,-0.137731,6.939550,-4.909634,8.252609,-3.903565,8.142021,9.613236,7.379686,6.073222,-2.993170,4.179334,0.007265,1.253128,-8.358073,-5.265823,3.828264,0.747115,-5.108371,8.936206,3.681465,-1.158078,1.995205,-6.642348,-2.462701,9.940716,4.414758,6.000963,9.929561,-0.132604,0.143286,3.101596,2.811954,1.582228,3.929095,9.036476,-9.634233,7.821151,-4.453750,6.884052,4.047887,0.315473,0.730432,-0.536454,5.262197,-6.555895,4.260782,-4.668268,-7.347657,-8.680564,-5.794419,4.437946,-3.841653,-4.346926,-8.967398,3.131835,5.142526,-3.414124,7.141477,2.876858,8.755342,4.608642,-0.994402,-4.028330,2.578763,-0.155285,-6.292573,2.184071,-8.317718,2.409575,7.649581,8.067581,4.515840,5.946828,-6.242154,-6.314613,-2.902333,-8.327020,3.777274,4.332537,7.341364,-9.037241,9.065962,-1.064902,2.658468,9.697532,-9.553949,2.937010,-3.606963,8.368437,-6.747305,4.667373,6.240977,8.702132,-9.714099,-6.908188,-4.004121,6.441112,-0.017925,0.986476,-6.535524,-7.397301,3.342081,-3.887023,-1.261424,-1.038546,4.432474,7.258716,8.318010,9.395542,5.121487,-9.350010,-9.544894,-6.115122,4.249140,0.819996,-2.186396,1.213159,2.053711,3.564643,1.493154,-2.898757,0.931708,6.742797,-4.717422,-5.941305,-1.556722,5.809737,2.417525,4.423155,-3.251141,-3.366857,-1.665191,-6.824866,9.618207,3.026861,-5.916036,-6.256036,1.687880,-8.417525,-2.295858,-4.938815,9.470459,-7.519297,9.811061,-4.489407,-0.634208,-0.697286,-1.952138,-7.019890,-2.077078,-5.740263,-9.114823,1.260443,-7.553900,7.858047,-2.054139,-6.530830,-3.272253,-5.171115,-4.753685,7.055519,1.814169,-6.426483,-1.446022,-3.635097,-3.889692,9.278832,6.196759,5.945428,2.950854,-4.587834,-0.306350,5.675786,4.250245,-8.115571,-9.519128,-1.526471,9.050877,2.019014,-8.643299,-1.031783,-4.737477,7.941152,-0.359489,-8.850004,7.605225,-9.422968,3.886143,-4.619992,4.545700,-9.877217,-7.406941,-0.793984,9.084430,-1.872669,0.705327,2.777779,-2.409213,7.703259,9.454809,-2.425156,-2.378328,-2.257870,8.380683,3.170707,2.701601,-7.027835,-6.584781,8.196126,9.361658,9.611411,-5.406209,-9.315120,7.482317,-9.131497,4.814870,-0.927912,1.659114,7.703363,9.216120,3.031026,0.575238,1.415737,-4.378106,8.910001,-6.280608,-3.483676,0.186681,1.963669,-7.182090,0.165293,0.057268,-7.601353,-9.177619,2.724740,-6.068925,-9.628829,-7.648848,5.810557,-4.297301,-3.964761,-1.769477,-3.729039,-5.483165,-4.701096,5.320513,-8.811479,0.524021,4.986423,3.320782,-5.299692,6.379204,4.396581,-8.854278,7.788082,0.092632,1.130309,-2.365526,-2.475907,7.110727,-2.999192,-6.356253,6.997864,9.852673,-3.481119,3.668376,-4.301451,0.455486,1.070998,-9.223887,4.353238,-2.985711,9.430911,-5.567033,7.013400,8.290919,-0.605248,2.984078,7.424860,-3.182195,7.828576,-1.401984,-4.152490,7.687555,1.708347,-9.879561,3.578100,6.910813,-8.486524,-1.872641,-7.838141,2.080834,-1.596863,-1.463792,5.881790,2.250018,9.105233,-4.550825,9.594312,1.452378,6.955615,6.496584,-5.037892,-4.667915,-7.074182,2.202144,-1.596005,9.307265,9.090119,-7.819078,-0.311063,9.207780,-0.839763,-7.370474,0.105401,-0.366730,9.581443,1.938796,7.165198,-2.752784,9.540052,-7.469432,-4.757006,-3.834957,9.676404,-6.302171,-2.718274,5.553340,3.180756,-6.105086,0.425133,-5.175204,3.407423,2.225542,1.522945,-9.774956,2.356555,-5.492643,0.140052,9.579927,2.353647,-5.144233,2.857692,-6.332061,0.360165,1.486968,-8.072440,-9.930190,2.262406,-5.356932,6.823394,9.798758,2.069059,1.649923,-1.001925,5.696488,-9.130374,6.437533,-9.024722,9.189210,7.717197,-5.695410,-7.013562,7.078783,-1.437979,-4.926285,-4.980317,-5.934872,0.047999,-7.484600,-1.903981,6.671135,-9.886068,-4.925414,4.898168,-2.626391,-9.321175,-3.173643,1.159677,9.992213,4.239225,-8.393204,1.941008,5.663413,-7.240072,9.337141,4.513643,1.875685,7.217861,-3.531447,6.518215,7.770074,-1.327921,-4.554265,0.564054,1.171930,5.843835,8.980332,2.127928,4.860203,-4.895519,-2.885126,-4.841711,6.794279,-1.915664,-2.834301,8.607041,3.286143,1.742793,8.238739,7.532081,5.353191,-6.961917,-2.009961,3.941542,0.516337,-1.474351,6.094614,-9.564030,-8.024514,6.061867,-9.259270,9.377283,-4.466288,-9.523308,9.331909,-7.131609,-5.393646,8.685193,-1.503609,0.044653,6.427396,-6.305918,-0.150893,5.086123,0.040253,7.559684,4.426028,3.950393,3.662129,-9.089285,-6.952895,6.553027,7.900149,7.648596,0.199846,-4.837791,-1.215159,6.912212,5.548332,0.173116,7.061615,-2.107182,4.151063,-4.897297,7.026604,-7.293235,-2.993138,5.615447,-5.770879,3.043828,3.028414,-2.186873,-2.932513,-3.394613,0.565633,-4.531858,-5.789190,0.794703,5.380182,-8.449755,-8.127505,-2.428639,-6.270907,4.392504,-2.251117,-7.172375,-3.266470,1.764355,-9.961541,-3.436650,2.336026,2.833462,3.075414,-6.324347,-1.868647,-2.977787,1.155974,3.964145,-4.081761,-6.226852,-2.946465,-5.401337,-8.227176,8.144590,8.490122,-6.226239,9.859807,-1.997947,-1.372514,9.850438,1.214100,-0.368323,-9.005239,-8.854025,-2.933700,5.406379,3.145154,2.618130,0.886886,-6.057900,-2.798363,9.872125,-2.589298,-5.236311,-7.136267,-4.936698,3.917693,-6.831114,-3.107706,-5.433586,-9.371870,1.646004,5.514846,6.422952,-5.455709,2.376025,-9.191426,-6.856150,-6.913696,4.951982,-1.059775,-1.060933,-3.940462,1.459840,9.146626,8.854947,5.332666,2.697499,2.158681,4.550355,7.735065,-1.272627,8.416527,-4.540122,-8.851841,8.160984,0.109128,-4.655542,-6.664226,6.628630,-9.115061,6.821892,2.877699,-6.641120,7.448313,-3.005919,0.520434,-5.507403,1.089208,-5.406060,5.865017,-7.882031,-9.298078,-1.319210,-1.570603,-6.374274,8.075804,-6.406551,7.718848,3.750921,-6.003754,5.846547,5.008712,0.675627,-5.289989,-3.174691,0.601018,9.238769,4.043512,-4.637230,8.590047,-0.959258,0.319070,6.067011,-2.026642,7.251312,9.969566,-9.167690,7.547869,9.772740,9.165073,7.549360,9.943941,-4.379560,-4.845873,-2.799956,-0.789588,-9.379799,-6.173348,-0.758201,2.475432,1.714139,-6.717501,3.762018,7.803876,9.612971,-2.455762,8.755290,7.926525,-7.745748,7.050624,2.503891,-9.500104,9.351783,-5.877336,6.105208,5.232955,-7.515531,-7.908184,8.592220,-6.235270,-3.634174,1.753205,-6.295197,-2.803540,2.340261,-8.348035,8.201043,-7.741397,2.441900,-0.482561,-3.050311,8.091506,3.891658,-2.804755,-2.814233,5.444152,7.657485,-0.008505,-3.977545,1.517646,-1.073948,-8.051694,-3.317877,-7.970401,7.356055,-1.602283,0.615711,-8.566723,9.206411,0.357821,-5.906012,-0.202203,-1.341798,9.681221,3.426649,-1.851241,-0.538118,8.316217,1.776229,-6.991543,-2.808371,2.795054,8.641979,-9.761674,-0.251252,-9.007301,1.190984,9.366061,8.304140,-8.102701,5.663808,8.436319,7.729765,-9.311247,-7.279271,-3.223067,9.677278,-4.040290,7.418669,9.961250,8.643308,-6.655516,-2.880079,-2.992996,9.425048,6.111206,6.810549,-9.472959,7.219788,0.149571,-5.968444,0.952217,2.524510,-4.728041,-5.981666,4.580681,9.867300,-6.405291,8.513910,6.757789,4.374835,8.274392,4.082307,-7.391565,-5.155516,4.857711,3.768476,-8.546221,-6.825505,1.968096,-5.370947,-1.374322,7.535628,0.823139,6.550039,8.858182,5.115137,9.726213,-9.167561,-2.894801,-6.152061,9.408264,-6.896565,-1.650794,-1.287160,9.096914,-5.863800,-5.240025,9.378602,-8.229645,7.677184,8.803559,-4.093003,5.745450,-1.063330,5.293265,6.569354,-3.609864,-4.982302,9.623946,0.885950,6.003126,-0.916358,6.738720,-2.441764,7.502231,1.073614,-2.456053,7.812775,-2.323631,7.423633,-1.519640,4.668851,-0.498812,-4.840660,-3.152920,8.729734,1.603031,-9.247491,7.160544,0.933160,-1.874679,4.138089,-7.828589,-7.051375,7.420392,9.681308,3.339444,-1.865529,-9.108797,2.277676,-9.297812,5.353884,-7.537178,-0.878244,-5.018683,-8.840714,-0.747519,4.114724,3.641911,-1.406646,-5.249479,-6.091951,-4.097249,9.638980,0.119264,9.658861,8.853729,-7.270686,-6.926634,1.689024,-9.529608,2.632381,-0.881149,6.657403,9.453256,-0.132073,5.529393,2.946078,6.452442,2.888986,9.534535,1.889608,2.765230,-2.821129,-3.930189,-2.822190,-1.855223,-7.305241,-9.113005,-3.626540,1.866999,9.156964,8.912158,-3.359203,-1.320719,-0.089291,-7.924190,-7.836791,1.592331,-3.228184,1.973498,-1.874666,-1.920808,-4.471411,-7.961884,-0.860379,4.128437,8.946108,-9.144784,9.006537,0.977762,-8.362177,4.863623,4.829742,-9.709924,9.330667,-5.249420,4.931153,-3.147025,4.203599,-4.343767,-8.700727,-8.508208,-4.113613,2.136676,3.601567,9.860554,-3.094597,-3.016839,7.840057,0.861658,-4.526014,-7.564271,0.472643,2.760782,-4.463982,-9.897148,1.693218,-3.092830,-5.190754,-6.241158,-9.713517,8.600878,-5.399425,-3.778709,-6.885070,-5.727460,7.274514,-5.775150,7.030082,7.915643,1.054479,-3.420878,-3.956381,5.183198,-7.996123,-3.984958,1.014477,-6.357990,-0.158526,-7.104023,-7.528027,1.608619,1.385758,-3.348564,-0.208634,-7.516587,-4.647771,-6.994037,9.984765,7.720860,5.682850,-3.306958,7.865645,7.591124,7.231737,6.604447,-3.006800,3.952149,-8.176489,9.740936,-2.629821,4.569095,-0.448021,1.944740,2.858863,-7.819560,5.839492,5.781242,0.019793,-1.602159,-7.905552,-2.042434,-0.822114,4.636567,-1.783061,0.571347,-4.435105,5.249554,9.364721,7.856577,2.011136,9.230668,-1.556664,0.908212,0.386157,8.028473,5.823165,6.611652,3.790722,8.340752,3.411991,-0.463751,6.401635,-1.209870,0.035495,2.661584,3.020367,8.726846,4.422610,2.495206,-4.007170,4.807690,6.439068,2.894462,7.630892,-4.317490,-9.970210,-9.951004,-8.585228,-0.154963,-0.556469,-8.777277,-8.215736,-7.612276,-7.068757,5.956537,-7.926121,9.038984,8.746423,-9.396405,9.255353,0.040271,-3.558042,1.141969,-4.052622,-9.181276,2.932930,7.346567,-9.802725,6.417314,3.149611,9.538306,6.603310,5.138288,2.019903,4.780184,-5.546934,-3.533506,5.776325,9.867645,9.381364,-6.494072,-4.471736,9.299616,7.439071,-4.680488,7.412799,-2.755196,-2.521185,6.247558,-9.907208,-4.600486,0.181754,0.295443,-9.651746,-2.812623,-5.790655,-1.083494,-4.928603,3.930541,-5.961680,2.429793,1.420594,5.015475,7.784114,2.243176,4.461146,3.104577,5.061060,5.943388,3.111643,5.850318,1.317212,4.526053,5.914086,9.566819,-4.564513,5.007024,9.348196,1.770208,6.581488,-6.951992,-2.273656,4.260270,-6.611745,7.069244,1.841503,0.570333,-5.986325,-3.416973,8.688656,2.739791,-5.915630,6.504850,8.228782,8.721837,8.318929,-6.312892,4.365417,8.499416,-6.644356,8.338166,-3.205996,-6.210509,5.272751,-6.583455,4.333966,-1.571287,1.980898,7.319728,-4.202614,3.358894,-8.020498,8.784169,-5.679899,8.975307,8.068209,-2.222840,4.670280,-8.536981,1.436641,8.859843,4.350145,6.680731,6.813836,7.348206,8.590009,8.427011,-6.106486,5.189093,-4.358357,-1.685411,4.936279,7.124068,7.370554,-6.885424,-2.799071,4.827978,5.489856,-6.139185,8.869035,2.081850,4.605512,-6.008371,7.984115,-1.165502,-6.887832,-6.451825,1.551035,-5.533351,1.815714,2.574770,-6.755643,2.734673,9.760729,-0.679971,-0.881013,1.384501,9.250606,9.893268,2.692830,-5.868185,-6.174936,-8.032423,-3.091685,8.691466,6.172438,1.584917,9.181943,7.039757,8.142704,-6.959718,4.004838,6.799855,7.547114,-1.385395,-9.515439,1.024310,5.893295,-0.885542,-7.606357,6.894749,-0.400011,-3.863064,-1.201953,3.842230,2.879026,0.077852,7.945262,6.570836,7.476585,-3.690040,-5.140458,1.630204,7.483357,9.326621,1.174084,9.071334,-3.509474,2.807213,0.273101,-7.659697,-5.573249,-1.409257,-6.909989,5.098093,8.958787,3.707062,2.078467,6.803161,-4.695482,-7.236764,3.427796,9.667622,6.776312,-5.247973,9.546682,-1.388621,-4.392070,-9.063147,-3.534761,3.449226,1.704066,-7.484769,8.407477,4.393530,-4.149608,7.015454,0.229519,1.332148,2.943553,0.936868,-8.367164,0.096149,-4.341856,1.395170,5.816175,-1.007205,3.431986,0.498439,-5.609881,-2.614115,-6.792793,4.711640,8.566875,5.128258,-0.114720,0.518758,-7.524654,-7.188845,-5.871510,1.551751,-4.713027,-0.606288,-1.359720,-9.390746,-9.809096,-1.677451,-4.860782,-7.762785,-6.178064,-2.090507,9.885302,-0.257744,-9.270696,-2.302691,-1.398877,-3.471534,-9.690850,0.364292,-5.154618,4.891442,-8.094322,-7.221048,3.609245,-5.056111,-4.825631,6.386144,4.616580,4.951120,-1.155460,-2.891943,5.833546,5.247955,-7.518236,7.768947,-7.553898,6.360378,-0.586548,3.488563,6.862223,4.087973,-4.460262,9.468847,-4.939817,-9.449280,-7.851523,-3.049915,9.755055,3.220036,-0.408411,8.061503,-9.851128,8.869977,-1.884594,-6.786988,2.659089,3.144683,-2.989170,9.936787,4.386645,5.326504,-8.971518,9.870306,5.335033,3.893712,6.670815,-0.202574,-9.934215,-0.407821,-3.799605,-8.468591,4.699416,-0.228091,-8.533860,-1.760380,2.840722,1.997879,3.104730,4.087971,-1.885413,-8.238681,5.849639,1.140587,1.463313,-2.840285,-8.135667,4.155393,-0.589991,-5.982152,1.221026,-6.207292,-5.313355,-1.411245,8.044204,5.267115,4.264437,1.031385,-4.838109,-5.172325,1.465322,-2.300519,9.995636,1.675326,1.137462,-1.867163,-9.938438,5.364668,-8.664888,4.409233,0.183526,7.728289,-3.242679,-3.541539,9.018832,-9.172394,2.909328,1.499134,-5.258186,2.643455,-2.327149,-4.512689,-9.892066,3.595010,-0.833948,-7.658097,8.178642,-6.448361,5.838636,1.546148,1.637397,8.126056,-6.402698,9.882158,7.865486,-3.737827,-8.395957,-9.290565,-5.258173,6.114696,-1.904019,-1.182115,-9.073780,-6.262710,0.119309,-6.592398,4.762908,-5.117725,-3.358303,4.504052,-3.159566,2.447966,-1.659147,4.926684,-2.628993,3.621920,7.062288,-0.897264,-4.422943,2.676241,-2.463106,-3.090318,1.826065,1.388810], dtype = "float32")#candidate|2821|(1950,)|const|float32
var_2822 = relay.var("var_2822", dtype = "int64", shape = (450,))#candidate|2822|(450,)|var|int64
var_2823 = relay.var("var_2823", dtype = "int16", shape = (48,))#candidate|2823|(48,)|var|int16
var_2824 = relay.var("var_2824", dtype = "float64", shape = (480,))#candidate|2824|(480,)|var|float64
var_2825 = relay.var("var_2825", dtype = "uint16", shape = (1, 192))#candidate|2825|(1, 192)|var|uint16
call_2820 = relay.TupleGetItem(func_2019_call(relay.reshape(const_2821.astype('float32'), [15, 13, 10]), relay.reshape(var_2822.astype('int64'), [150, 3]), relay.reshape(var_2823.astype('int16'), [4, 12]), relay.reshape(var_2824.astype('float64'), [8, 60]), relay.reshape(var_2825.astype('uint16'), [96, 2]), ), 0)
call_2826 = relay.TupleGetItem(func_2026_call(relay.reshape(const_2821.astype('float32'), [15, 13, 10]), relay.reshape(var_2822.astype('int64'), [150, 3]), relay.reshape(var_2823.astype('int16'), [4, 12]), relay.reshape(var_2824.astype('float64'), [8, 60]), relay.reshape(var_2825.astype('uint16'), [96, 2]), ), 0)
bop_2834 = relay.left_shift(const_2807.astype('uint16'), relay.reshape(var_2806.astype('uint16'), relay.shape_of(const_2807))) # shape=(6, 6, 10)
bop_2844 = relay.not_equal(const_2807.astype('bool'), relay.reshape(bop_2808.astype('bool'), relay.shape_of(const_2807))) # shape=(6, 6, 10)
func_687_call = mod.get_global_var('func_687')
func_690_call = mutated_mod.get_global_var('func_690')
call_2848 = relay.TupleGetItem(func_687_call(relay.reshape(var_2824.astype('float64'), [6, 16, 5])), 0)
call_2849 = relay.TupleGetItem(func_690_call(relay.reshape(var_2824.astype('float64'), [6, 16, 5])), 0)
func_1387_call = mod.get_global_var('func_1387')
func_1389_call = mutated_mod.get_global_var('func_1389')
var_2853 = relay.var("var_2853", dtype = "float32", shape = (39, 4))#candidate|2853|(39, 4)|var|float32
call_2852 = relay.TupleGetItem(func_1387_call(relay.reshape(var_2853.astype('float32'), [13, 3, 4])), 2)
call_2854 = relay.TupleGetItem(func_1389_call(relay.reshape(var_2853.astype('float32'), [13, 3, 4])), 2)
uop_2863 = relay.sqrt(bop_2808.astype('float32')) # shape=(6, 6, 10)
output = relay.Tuple([call_2820,const_2821,var_2822,var_2823,var_2824,var_2825,bop_2834,bop_2844,call_2848,call_2852,var_2853,uop_2863,])
output2 = relay.Tuple([call_2826,const_2821,var_2822,var_2823,var_2824,var_2825,bop_2834,bop_2844,call_2849,call_2854,var_2853,uop_2863,])
func_2878 = relay.Function([var_2806,var_2822,var_2823,var_2824,var_2825,var_2853,], output)
mod['func_2878'] = func_2878
mod = relay.transform.InferType()(mod)
mutated_mod['func_2878'] = func_2878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2878_call = mutated_mod.get_global_var('func_2878')
var_2880 = relay.var("var_2880", dtype = "bool", shape = (6, 6, 10))#candidate|2880|(6, 6, 10)|var|bool
var_2881 = relay.var("var_2881", dtype = "int64", shape = (450,))#candidate|2881|(450,)|var|int64
var_2882 = relay.var("var_2882", dtype = "int16", shape = (48,))#candidate|2882|(48,)|var|int16
var_2883 = relay.var("var_2883", dtype = "float64", shape = (480,))#candidate|2883|(480,)|var|float64
var_2884 = relay.var("var_2884", dtype = "uint16", shape = (1, 192))#candidate|2884|(1, 192)|var|uint16
var_2885 = relay.var("var_2885", dtype = "float32", shape = (39, 4))#candidate|2885|(39, 4)|var|float32
call_2879 = func_2878_call(var_2880,var_2881,var_2882,var_2883,var_2884,var_2885,)
output = call_2879
func_2886 = relay.Function([var_2880,var_2881,var_2882,var_2883,var_2884,var_2885,], output)
mutated_mod['func_2886'] = func_2886
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2899 = relay.var("var_2899", dtype = "float32", shape = (13, 3, 15))#candidate|2899|(13, 3, 15)|var|float32
uop_2900 = relay.cos(var_2899.astype('float32')) # shape=(13, 3, 15)
output = uop_2900
output2 = uop_2900
func_2910 = relay.Function([var_2899,], output)
mod['func_2910'] = func_2910
mod = relay.transform.InferType()(mod)
mutated_mod['func_2910'] = func_2910
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2911 = relay.var("var_2911", dtype = "float32", shape = (13, 3, 15))#candidate|2911|(13, 3, 15)|var|float32
func_2910_call = mutated_mod.get_global_var('func_2910')
call_2912 = func_2910_call(var_2911)
output = call_2912
func_2913 = relay.Function([var_2911], output)
mutated_mod['func_2913'] = func_2913
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3110 = relay.var("var_3110", dtype = "int64", shape = ())#candidate|3110|()|var|int64
var_3111 = relay.var("var_3111", dtype = "int64", shape = (16, 15, 10))#candidate|3111|(16, 15, 10)|var|int64
bop_3112 = relay.minimum(var_3110.astype('int64'), var_3111.astype('int64')) # shape=(16, 15, 10)
func_2910_call = mod.get_global_var('func_2910')
func_2913_call = mutated_mod.get_global_var('func_2913')
const_3119 = relay.const([[-9.038602,-2.769643,-7.770651],[-1.818824,-6.395818,9.293754],[6.539130,0.125416,5.815616],[-3.080224,2.869014,1.646458],[0.562608,-4.948080,-6.054228],[3.843170,-3.548286,-1.565065],[-8.246253,1.529440,-2.947658],[-1.295545,0.320945,2.895976],[-1.898867,-9.125016,-3.999898],[-9.120641,-6.120354,1.824353],[-1.824920,9.735717,-2.323205],[4.270341,1.020359,-4.017108],[5.870663,5.109892,-2.822038],[5.122227,6.212240,-9.804430],[-8.687116,5.978211,4.979528],[4.310255,-0.488972,9.506792],[0.960450,9.216700,6.943362],[-3.768977,3.426129,6.121155],[-8.573381,-0.622363,-9.458435],[7.730426,7.567988,7.663095],[-8.715323,9.147319,-4.009121],[5.738818,6.863463,-9.684521],[-9.387506,-6.188065,-9.526237],[-5.436732,-5.454389,-1.054825],[0.719654,9.091502,8.237043],[-8.328074,-9.551994,-3.771394],[-3.761284,-9.494920,-6.371150],[-7.025965,5.676250,-0.198131],[-8.819761,-1.313446,-5.611095],[0.312321,8.221818,-6.497025],[7.665540,-0.463401,-9.104536],[-8.662793,-6.646719,3.771617],[7.791524,-8.216549,-1.869511],[0.723196,3.764956,5.048692],[-2.633586,3.348642,-3.580583],[-4.373974,-6.425546,2.439397],[6.833548,8.451951,-6.129308],[2.745466,-5.843837,-1.725724],[-3.521364,9.332732,7.059559],[7.366748,3.786076,7.465592],[0.788686,-4.085663,-7.259078],[-9.579646,0.840699,-8.383334],[-4.433908,-1.178188,5.903331],[0.248919,-7.083235,2.226475],[-9.640924,1.788189,7.539598],[4.881969,4.917914,3.385421],[6.965251,4.019952,8.362957],[-4.399944,9.890798,0.882197],[8.041449,6.313575,8.568636],[1.666304,4.259735,-3.426843],[-4.363153,1.873624,3.256949],[1.756329,2.709837,5.337473],[-5.525154,-3.870564,-0.086963],[-0.298463,0.128676,5.585674],[-4.751122,-1.362642,-4.747215],[8.962477,-4.888131,-0.911073],[8.361546,-1.885197,-1.098574],[4.200530,0.251209,3.686690],[8.980211,1.931527,7.931620],[-1.616379,6.881996,4.075693],[0.246737,-1.093928,-6.115513],[7.802883,1.340756,-2.600833],[7.704327,-5.976612,5.406084],[6.227779,-5.322862,0.753615],[4.433932,4.023488,-3.242987],[-3.147155,2.521110,6.583872],[0.793231,8.217176,-9.371688],[8.437460,-9.398291,-4.599813],[5.046801,-8.604510,-7.595359],[5.619342,4.734766,4.946294],[2.344871,8.307968,-6.345043],[-8.911443,1.281337,-7.700450],[2.226695,-8.060183,-1.355938],[-6.424967,-0.376155,6.214616],[-0.602663,-1.676701,4.124772],[-4.134617,-0.746452,-5.042320],[-9.248263,-8.065478,-8.545694],[-9.853530,-9.198303,2.134374],[2.386704,-4.083537,3.594611],[5.817178,-1.031345,3.695993],[3.253892,0.021093,-5.064794],[-9.260042,-8.481160,-8.372465],[-0.531526,3.800141,3.869002],[4.006228,-1.636357,-6.470162],[7.239282,9.357356,-8.305919],[8.459249,-7.737025,7.950623],[-0.090022,-9.331367,-4.449737],[-9.406377,3.768400,-4.761208],[-5.717687,3.319971,3.419888],[-7.595396,7.478817,1.892068],[6.637379,5.289263,1.430071],[-2.620329,3.972172,-1.103320],[3.294849,-9.186273,-5.530796],[-9.520997,-2.105542,8.023744],[0.878758,-6.328980,-3.994807],[-0.082341,-6.213366,3.936893],[-2.121129,-2.532783,-2.264692],[-0.968105,5.985734,-6.618821],[7.976628,-4.701597,8.853679],[2.465434,-0.955569,0.380218],[2.695268,-0.866919,-7.642514],[1.632130,0.440955,-9.119434],[4.299489,3.242043,8.312964],[-7.542550,-6.683861,-0.833829],[8.805074,6.027134,1.379860],[-7.364213,-5.058060,-6.011992],[-4.276090,-2.142929,3.407461],[-1.956057,4.936480,2.842416],[7.560185,4.487465,1.263474],[7.995852,7.140540,-8.728856],[-7.681279,-5.018409,9.425764],[3.870254,-4.074915,6.265450],[-5.098121,-9.495573,7.494333],[-2.052117,-9.970606,4.532633],[2.125995,-7.250082,9.073209],[0.387890,6.184224,-1.744759],[-5.270076,-6.313640,7.854912],[3.748081,9.031374,9.252972],[1.438953,-8.293305,4.148931],[9.760801,-8.356602,-8.232598],[-0.346276,4.382070,1.077839],[-5.575351,2.050741,-7.909375],[-4.650268,-6.089040,-3.305294],[9.450302,9.090724,3.490755],[5.506164,7.575516,-2.239465],[6.567497,3.170316,-9.871420],[-7.490444,2.138796,0.099599],[3.201704,7.132123,-4.374435],[9.831500,2.626282,5.973556],[-2.799821,-0.049509,-2.226374],[9.530908,4.827015,2.111995],[5.241251,4.400825,1.167438],[-7.006746,-5.376773,2.983815],[0.700176,-5.647744,5.222401],[9.312160,-7.464469,-5.813509],[-5.568358,-1.572197,-2.348698],[8.152990,-9.544212,-6.330506],[-2.756485,-3.546820,-9.075396],[8.557170,-8.203231,4.895005],[9.935175,6.563467,-3.633766],[-2.197638,2.978553,-2.416273],[-6.527502,3.506796,-7.288786],[5.489635,2.489517,-4.293827],[2.379950,5.192002,0.404170],[8.070200,-5.206363,1.779085],[-0.817213,7.559068,-7.691910],[-8.040834,-8.739092,5.635749],[0.196595,2.858498,-2.018083],[0.815307,4.237741,-7.031635],[2.591872,2.128005,-1.853156],[-7.359861,-7.199436,0.820282],[1.795868,-2.794148,8.481247],[6.214591,-3.340476,3.551421],[-0.528709,-0.376702,-7.349678],[-0.799335,-8.965086,9.402054],[-2.336750,-9.924357,9.949623],[-1.093719,4.567382,-7.231663],[-9.952604,7.605529,-6.340631],[-3.322350,5.729239,-0.306654],[8.424708,1.462939,-6.634788],[-6.625552,-8.908035,-4.305668],[-4.740528,0.794473,5.313106],[6.829199,7.836154,-9.528707],[4.171003,-4.895158,0.378438],[-1.982041,1.629561,-6.921859],[-3.146569,3.364579,9.482154],[9.241079,-7.187247,6.274253],[-6.269385,0.870819,-4.597751],[-3.547316,-6.159436,-7.566740],[2.536754,-3.470495,5.663270],[9.883846,-8.414307,-5.751771],[-7.213177,8.716788,-4.906742],[-6.468932,1.285135,-3.679387],[9.747395,-9.735825,3.971640],[8.112601,9.227364,-1.268065],[-3.740668,2.870777,-5.730655],[9.188842,0.755577,2.255773],[6.230557,-4.403240,8.261712],[-6.178822,0.325048,4.945650],[-1.935192,-1.532236,-9.515406],[-8.979218,-8.825461,2.574399],[4.457863,6.608813,-1.294553],[4.349945,-0.189483,-8.518109],[-6.603571,-4.591791,1.077076],[2.305077,-3.880505,-0.626919],[-4.885607,9.450196,-5.469358],[5.509946,0.842133,-3.116090],[5.380874,-1.523804,5.222610],[9.418056,0.799151,-4.934870],[3.395718,-2.565853,4.991921],[7.652829,5.334773,-2.782003],[3.248148,-3.339248,-0.074707],[-6.446728,-2.771185,3.545713],[-2.856082,6.784713,-7.484835],[-1.059207,1.520443,2.844135]], dtype = "float32")#candidate|3119|(195, 3)|const|float32
call_3118 = func_2910_call(relay.reshape(const_3119.astype('float32'), [13, 3, 15]))
call_3120 = func_2910_call(relay.reshape(const_3119.astype('float32'), [13, 3, 15]))
output = relay.Tuple([bop_3112,call_3118,const_3119,])
output2 = relay.Tuple([bop_3112,call_3120,const_3119,])
func_3126 = relay.Function([var_3110,var_3111,], output)
mod['func_3126'] = func_3126
mod = relay.transform.InferType()(mod)
var_3127 = relay.var("var_3127", dtype = "int64", shape = ())#candidate|3127|()|var|int64
var_3128 = relay.var("var_3128", dtype = "int64", shape = (16, 15, 10))#candidate|3128|(16, 15, 10)|var|int64
output = func_3126(var_3127,var_3128,)
func_3129 = relay.Function([var_3127,var_3128,], output)
mutated_mod['func_3129'] = func_3129
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3503 = relay.var("var_3503", dtype = "uint16", shape = (4, 6, 4))#candidate|3503|(4, 6, 4)|var|uint16
var_3504 = relay.var("var_3504", dtype = "uint16", shape = (4, 6, 4))#candidate|3504|(4, 6, 4)|var|uint16
bop_3505 = relay.maximum(var_3503.astype('uint16'), relay.reshape(var_3504.astype('uint16'), relay.shape_of(var_3503))) # shape=(4, 6, 4)
uop_3510 = relay.atan(var_3503.astype('float64')) # shape=(4, 6, 4)
uop_3513 = relay.cosh(uop_3510.astype('float32')) # shape=(4, 6, 4)
output = relay.Tuple([bop_3505,uop_3513,])
output2 = relay.Tuple([bop_3505,uop_3513,])
func_3535 = relay.Function([var_3503,var_3504,], output)
mod['func_3535'] = func_3535
mod = relay.transform.InferType()(mod)
var_3536 = relay.var("var_3536", dtype = "uint16", shape = (4, 6, 4))#candidate|3536|(4, 6, 4)|var|uint16
var_3537 = relay.var("var_3537", dtype = "uint16", shape = (4, 6, 4))#candidate|3537|(4, 6, 4)|var|uint16
output = func_3535(var_3536,var_3537,)
func_3538 = relay.Function([var_3536,var_3537,], output)
mutated_mod['func_3538'] = func_3538
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3610 = relay.var("var_3610", dtype = "int8", shape = (6, 12, 14))#candidate|3610|(6, 12, 14)|var|int8
const_3611 = relay.const([[[-1,7,-2,1,4,4,7,-7,9,1,-3,5,-10,-10],[-2,-4,-9,-10,7,-9,-9,2,-3,8,-2,9,10,5],[2,6,6,8,-3,8,-10,-3,-10,-6,6,2,-5,-3],[-4,4,-6,2,10,-1,10,3,6,10,4,6,10,-8],[-10,9,-3,-2,5,3,7,8,-3,9,10,-5,5,-4],[1,1,7,7,-5,9,4,5,5,-9,6,-10,-7,-3],[-6,7,-1,3,8,-7,1,-5,9,-8,-5,5,-7,2],[-9,6,1,7,2,1,-9,5,6,9,-1,-2,-6,-10],[3,8,-4,-9,8,9,5,-1,2,-6,-7,-6,2,5],[-6,-2,6,4,2,6,-9,-1,-7,-9,-8,9,-2,4],[-4,1,-3,-2,-10,-8,10,-4,9,3,8,8,1,-3],[-4,-4,-5,10,-7,-6,9,-1,8,-7,-3,-4,6,-10]],[[9,7,-2,2,9,5,4,-5,5,-1,-3,1,-1,-8],[-9,4,-4,1,-6,-3,-7,-9,10,-4,-9,-10,-5,10],[-6,-3,-9,-2,9,-8,8,-8,-10,6,2,-6,6,5],[7,-7,6,-7,-6,9,-6,-8,8,9,-4,7,4,-9],[9,4,-9,-8,-1,-1,8,2,-5,-6,8,-1,10,-10],[-1,-7,-3,8,-1,9,3,-9,-8,-3,-5,7,6,-8],[6,-3,7,9,2,-1,4,-5,8,8,-6,2,-1,5],[-9,-6,-10,-3,-10,6,2,2,-7,-6,2,-2,6,2],[-3,7,-9,-6,-1,-8,5,-2,3,-4,-3,-3,6,-5],[-9,2,-1,1,-3,3,-8,-6,6,10,1,8,-6,-9],[6,5,-1,7,-7,4,-7,-5,-9,-8,6,-2,3,3],[3,-2,-7,6,3,10,2,-7,2,-6,10,5,3,6]],[[-9,5,-10,3,-3,5,-2,3,10,5,-1,-4,6,-10],[-1,6,5,4,-8,3,5,7,-3,-3,10,7,-10,4],[-4,-6,-1,5,-4,1,7,5,-4,-1,-1,-1,6,-4],[-3,-4,-3,10,-5,-9,-5,2,6,7,-8,-8,5,-3],[9,7,4,-7,-4,-10,-3,7,-9,3,4,5,8,-4],[3,4,-5,-4,-2,5,-9,4,-3,-3,10,8,-3,10],[6,-4,1,3,-7,-4,-1,7,-5,-3,2,1,-9,7],[-3,3,1,10,-3,8,1,1,1,3,8,4,-1,1],[-5,-2,-5,10,2,6,5,7,5,10,-3,4,7,1],[-5,8,3,10,6,-2,10,-4,-3,10,9,6,3,5],[-7,9,-1,4,8,-9,-6,3,-10,-2,7,1,-4,-8],[-4,-8,-1,5,-4,3,-4,6,-5,9,-5,-8,-5,-10]],[[5,-7,-3,4,-1,-4,-7,-9,-1,-5,6,-4,5,7],[3,8,-5,9,-9,2,1,7,4,2,-2,4,1,1],[1,3,-5,-2,-5,10,5,7,7,7,-1,7,-6,-3],[10,-2,-4,-3,-5,1,9,7,3,-1,6,-2,-8,2],[1,-10,1,-1,6,-6,-10,-2,-8,2,-1,-2,2,-5],[4,-4,-5,7,6,-3,-4,5,7,5,-4,-9,-2,3],[-6,2,-8,-4,-1,-8,-8,1,-3,-8,-2,8,-9,-3],[7,-3,-4,2,1,4,-8,9,5,-10,6,9,-8,-6],[-3,8,-6,-2,7,-4,-9,-10,-1,2,9,-6,-7,-5],[-1,4,1,-3,-6,-9,8,-1,2,-1,10,-10,-5,-6],[-3,-9,-3,10,6,2,10,-5,7,-3,-7,1,-2,-8],[9,-9,-8,-7,-5,6,-10,-5,2,-7,6,-7,8,2]],[[-8,7,8,-10,-8,7,1,5,6,2,-10,8,-2,-10],[-2,2,-3,-7,-7,-5,-3,-8,-10,8,3,-3,-10,10],[3,-6,-10,-6,7,6,-2,1,-5,-10,2,-8,-9,-9],[-1,2,-8,-10,-7,5,-10,8,-2,-7,-7,-4,4,-5],[5,1,4,-10,2,-5,6,2,1,-10,-10,1,-4,8],[9,3,9,9,-1,-10,-1,-3,6,-5,-7,1,-3,-5],[-7,7,6,9,-7,-3,-7,1,-7,-7,10,-10,-8,-4],[-3,-8,-2,8,6,-7,6,-3,-2,-3,9,-4,1,-5],[4,9,-8,10,3,-10,-7,-4,-7,-8,-1,10,8,-10],[7,-9,5,-10,7,3,-10,-9,-1,10,9,-7,-8,10],[-8,-6,-6,-5,4,-3,7,-9,10,4,10,-9,3,-9],[4,6,2,8,8,8,-1,3,9,-3,-1,-10,2,-9]],[[-7,3,-10,3,10,9,-5,1,9,1,9,9,-2,2],[10,6,-2,9,9,-3,3,8,10,-3,-7,-9,2,-6],[-8,-8,-10,4,-5,-5,4,5,1,-7,-5,1,9,-8],[-9,3,3,-4,8,-6,-2,9,-8,-5,-8,-9,5,6],[-2,-2,7,6,1,-2,1,-3,-10,3,7,-8,-2,-9],[-8,10,-7,9,-10,-3,-9,9,4,5,4,-1,-5,5],[5,4,-9,3,7,-2,-9,9,2,7,1,2,-9,-4],[2,-2,3,4,10,-10,9,7,6,5,-5,-8,6,2],[2,10,7,-5,-9,4,6,10,3,3,-5,-9,-1,-7],[-6,-2,6,6,-7,-6,10,8,2,-9,-5,-6,1,3],[4,-10,-10,3,-6,9,-8,10,5,-3,-5,-3,5,3],[9,-7,-5,-5,1,10,7,-1,-6,-4,-6,-7,-9,3]]], dtype = "int8")#candidate|3611|(6, 12, 14)|const|int8
bop_3612 = relay.multiply(var_3610.astype('int8'), relay.reshape(const_3611.astype('int8'), relay.shape_of(var_3610))) # shape=(6, 12, 14)
output = bop_3612
output2 = bop_3612
func_3626 = relay.Function([var_3610,], output)
mod['func_3626'] = func_3626
mod = relay.transform.InferType()(mod)
mutated_mod['func_3626'] = func_3626
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3627 = relay.var("var_3627", dtype = "int8", shape = (6, 12, 14))#candidate|3627|(6, 12, 14)|var|int8
func_3626_call = mutated_mod.get_global_var('func_3626')
call_3628 = func_3626_call(var_3627)
output = call_3628
func_3629 = relay.Function([var_3627], output)
mutated_mod['func_3629'] = func_3629
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3708 = relay.var("var_3708", dtype = "uint8", shape = (10, 14, 14))#candidate|3708|(10, 14, 14)|var|uint8
var_3709 = relay.var("var_3709", dtype = "uint8", shape = (10, 14, 14))#candidate|3709|(10, 14, 14)|var|uint8
bop_3710 = relay.bitwise_xor(var_3708.astype('uint8'), relay.reshape(var_3709.astype('uint8'), relay.shape_of(var_3708))) # shape=(10, 14, 14)
output = bop_3710
output2 = bop_3710
func_3720 = relay.Function([var_3708,var_3709,], output)
mod['func_3720'] = func_3720
mod = relay.transform.InferType()(mod)
var_3721 = relay.var("var_3721", dtype = "uint8", shape = (10, 14, 14))#candidate|3721|(10, 14, 14)|var|uint8
var_3722 = relay.var("var_3722", dtype = "uint8", shape = (10, 14, 14))#candidate|3722|(10, 14, 14)|var|uint8
output = func_3720(var_3721,var_3722,)
func_3723 = relay.Function([var_3721,var_3722,], output)
mutated_mod['func_3723'] = func_3723
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3806 = relay.var("var_3806", dtype = "float32", shape = ())#candidate|3806|()|var|float32
var_3807 = relay.var("var_3807", dtype = "float32", shape = (3, 16, 4))#candidate|3807|(3, 16, 4)|var|float32
bop_3808 = relay.greater(var_3806.astype('bool'), var_3807.astype('bool')) # shape=(3, 16, 4)
bop_3812 = relay.mod(var_3806.astype('float32'), var_3807.astype('float32')) # shape=(3, 16, 4)
uop_3819 = relay.sigmoid(bop_3812.astype('float32')) # shape=(3, 16, 4)
uop_3825 = relay.acos(uop_3819.astype('float32')) # shape=(3, 16, 4)
output = relay.Tuple([bop_3808,uop_3825,])
output2 = relay.Tuple([bop_3808,uop_3825,])
func_3832 = relay.Function([var_3806,var_3807,], output)
mod['func_3832'] = func_3832
mod = relay.transform.InferType()(mod)
var_3833 = relay.var("var_3833", dtype = "float32", shape = ())#candidate|3833|()|var|float32
var_3834 = relay.var("var_3834", dtype = "float32", shape = (3, 16, 4))#candidate|3834|(3, 16, 4)|var|float32
output = func_3832(var_3833,var_3834,)
func_3835 = relay.Function([var_3833,var_3834,], output)
mutated_mod['func_3835'] = func_3835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3846 = relay.var("var_3846", dtype = "uint16", shape = (1, 12, 3))#candidate|3846|(1, 12, 3)|var|uint16
var_3847 = relay.var("var_3847", dtype = "uint16", shape = (2, 12, 3))#candidate|3847|(2, 12, 3)|var|uint16
bop_3848 = relay.right_shift(var_3846.astype('uint16'), var_3847.astype('uint16')) # shape=(2, 12, 3)
func_70_call = mod.get_global_var('func_70')
func_74_call = mutated_mod.get_global_var('func_74')
const_3858 = relay.const(-1, dtype = "int16")#candidate|3858|()|const|int16
const_3859 = relay.const([[2,10],[-8,10],[-4,-9],[-2,-7],[-1,-10],[9,-3],[-3,8],[10,5],[-2,8],[3,-4],[-10,2],[-10,-6],[7,5],[-2,-4],[9,-6],[-6,10],[6,-7],[-5,-6],[6,7],[-4,8],[-9,-9],[3,5],[7,-10],[-4,10]], dtype = "int16")#candidate|3859|(24, 2)|const|int16
call_3857 = func_70_call(relay.reshape(const_3858.astype('int16'), []), relay.reshape(const_3859.astype('int16'), [4, 4, 3]), )
call_3860 = func_70_call(relay.reshape(const_3858.astype('int16'), []), relay.reshape(const_3859.astype('int16'), [4, 4, 3]), )
output = relay.Tuple([bop_3848,call_3857,const_3858,const_3859,])
output2 = relay.Tuple([bop_3848,call_3860,const_3858,const_3859,])
func_3865 = relay.Function([var_3846,var_3847,], output)
mod['func_3865'] = func_3865
mod = relay.transform.InferType()(mod)
mutated_mod['func_3865'] = func_3865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3865_call = mutated_mod.get_global_var('func_3865')
var_3867 = relay.var("var_3867", dtype = "uint16", shape = (1, 12, 3))#candidate|3867|(1, 12, 3)|var|uint16
var_3868 = relay.var("var_3868", dtype = "uint16", shape = (2, 12, 3))#candidate|3868|(2, 12, 3)|var|uint16
call_3866 = func_3865_call(var_3867,var_3868,)
output = call_3866
func_3869 = relay.Function([var_3867,var_3868,], output)
mutated_mod['func_3869'] = func_3869
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3935 = relay.var("var_3935", dtype = "int16", shape = (7, 16, 4))#candidate|3935|(7, 16, 4)|var|int16
var_3936 = relay.var("var_3936", dtype = "int16", shape = (7, 16, 4))#candidate|3936|(7, 16, 4)|var|int16
bop_3937 = relay.equal(var_3935.astype('bool'), relay.reshape(var_3936.astype('bool'), relay.shape_of(var_3935))) # shape=(7, 16, 4)
output = relay.Tuple([bop_3937,])
output2 = relay.Tuple([bop_3937,])
func_3941 = relay.Function([var_3935,var_3936,], output)
mod['func_3941'] = func_3941
mod = relay.transform.InferType()(mod)
var_3942 = relay.var("var_3942", dtype = "int16", shape = (7, 16, 4))#candidate|3942|(7, 16, 4)|var|int16
var_3943 = relay.var("var_3943", dtype = "int16", shape = (7, 16, 4))#candidate|3943|(7, 16, 4)|var|int16
output = func_3941(var_3942,var_3943,)
func_3944 = relay.Function([var_3942,var_3943,], output)
mutated_mod['func_3944'] = func_3944
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3966 = relay.var("var_3966", dtype = "float32", shape = (10, 15, 4))#candidate|3966|(10, 15, 4)|var|float32
uop_3967 = relay.acosh(var_3966.astype('float32')) # shape=(10, 15, 4)
output = uop_3967
output2 = uop_3967
func_3974 = relay.Function([var_3966,], output)
mod['func_3974'] = func_3974
mod = relay.transform.InferType()(mod)
mutated_mod['func_3974'] = func_3974
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3975 = relay.var("var_3975", dtype = "float32", shape = (10, 15, 4))#candidate|3975|(10, 15, 4)|var|float32
func_3974_call = mutated_mod.get_global_var('func_3974')
call_3976 = func_3974_call(var_3975)
output = call_3976
func_3977 = relay.Function([var_3975], output)
mutated_mod['func_3977'] = func_3977
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4093 = relay.var("var_4093", dtype = "float32", shape = (1, 3))#candidate|4093|(1, 3)|var|float32
var_4094 = relay.var("var_4094", dtype = "float32", shape = (12, 3))#candidate|4094|(12, 3)|var|float32
bop_4095 = relay.floor_divide(var_4093.astype('float32'), var_4094.astype('float32')) # shape=(12, 3)
func_3974_call = mod.get_global_var('func_3974')
func_3977_call = mutated_mod.get_global_var('func_3977')
var_4150 = relay.var("var_4150", dtype = "float32", shape = (600,))#candidate|4150|(600,)|var|float32
call_4149 = func_3974_call(relay.reshape(var_4150.astype('float32'), [10, 15, 4]))
call_4151 = func_3974_call(relay.reshape(var_4150.astype('float32'), [10, 15, 4]))
output = relay.Tuple([bop_4095,call_4149,var_4150,])
output2 = relay.Tuple([bop_4095,call_4151,var_4150,])
func_4168 = relay.Function([var_4093,var_4094,var_4150,], output)
mod['func_4168'] = func_4168
mod = relay.transform.InferType()(mod)
mutated_mod['func_4168'] = func_4168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4168_call = mutated_mod.get_global_var('func_4168')
var_4170 = relay.var("var_4170", dtype = "float32", shape = (1, 3))#candidate|4170|(1, 3)|var|float32
var_4171 = relay.var("var_4171", dtype = "float32", shape = (12, 3))#candidate|4171|(12, 3)|var|float32
var_4172 = relay.var("var_4172", dtype = "float32", shape = (600,))#candidate|4172|(600,)|var|float32
call_4169 = func_4168_call(var_4170,var_4171,var_4172,)
output = call_4169
func_4173 = relay.Function([var_4170,var_4171,var_4172,], output)
mutated_mod['func_4173'] = func_4173
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4234 = relay.var("var_4234", dtype = "uint8", shape = (6, 4, 16))#candidate|4234|(6, 4, 16)|var|uint8
const_4235 = relay.const([[[-10,10,-5,-6,-6,-8,-5,-7,-5,-5,7,-9,-7,-5,-1,-6],[-1,2,-7,-1,-1,6,-1,-2,-4,-7,6,-9,2,-5,4,8],[2,-3,10,-1,-4,8,8,2,-6,-4,-4,3,-4,2,4,5],[-10,4,-2,-9,-10,4,7,-3,-4,7,-9,-5,-1,-2,5,-10]],[[8,2,-8,8,10,-9,7,-3,-8,-10,-1,9,10,-8,1,-9],[-1,-8,-6,9,8,6,-8,6,-7,1,1,-1,-3,5,8,-2],[-9,-10,-7,-2,4,10,-6,8,-5,3,-2,7,5,9,10,-2],[2,-3,-10,-3,4,8,2,-3,-6,-2,-3,6,-3,-9,8,9]],[[3,10,10,10,9,-1,-4,9,-3,10,2,-3,-1,-5,4,-1],[-9,-2,6,-10,-10,9,9,5,1,-9,-1,7,3,-5,9,5],[6,-6,9,-9,-8,4,6,-1,-5,9,3,2,-9,4,-2,5],[-8,2,6,-8,-10,6,-2,-3,9,6,10,-9,-6,9,2,8]],[[5,-9,1,-9,-2,7,2,-2,5,-3,8,6,-5,-2,8,-8],[9,-6,-7,-1,10,10,9,-4,-1,-9,-1,3,-9,4,6,-2],[1,3,-3,-4,4,6,9,-10,-9,1,6,-7,-10,4,-2,9],[4,-1,10,-1,-1,-10,9,1,10,7,6,1,-4,2,-1,1]],[[-6,-4,8,-1,-2,-1,2,6,-6,8,-8,7,-5,-10,-3,4],[3,-6,-1,4,-9,-4,-7,-2,5,4,-10,7,-4,-6,8,-6],[7,-2,2,-4,10,-3,8,1,-7,9,8,7,-1,-10,-2,-9],[-10,-9,-8,-3,-1,-7,-4,-2,-5,-2,-7,6,-1,-8,-3,-2]],[[-8,5,-4,-4,9,-3,2,-5,8,-2,8,2,4,-10,7,-10],[-5,-10,-7,3,10,8,1,10,3,-4,-10,10,-6,-1,-4,-7],[9,-5,6,2,-4,-7,-8,-4,-9,-1,7,-2,-2,6,-7,-5],[4,3,-8,5,9,-8,-1,7,-3,10,10,2,7,9,3,-10]]], dtype = "uint8")#candidate|4235|(6, 4, 16)|const|uint8
bop_4236 = relay.bitwise_or(var_4234.astype('uint8'), relay.reshape(const_4235.astype('uint8'), relay.shape_of(var_4234))) # shape=(6, 4, 16)
func_3126_call = mod.get_global_var('func_3126')
func_3129_call = mutated_mod.get_global_var('func_3129')
var_4248 = relay.var("var_4248", dtype = "int64", shape = ())#candidate|4248|()|var|int64
var_4249 = relay.var("var_4249", dtype = "int64", shape = (2400,))#candidate|4249|(2400,)|var|int64
call_4247 = relay.TupleGetItem(func_3126_call(relay.reshape(var_4248.astype('int64'), []), relay.reshape(var_4249.astype('int64'), [16, 15, 10]), ), 1)
call_4250 = relay.TupleGetItem(func_3129_call(relay.reshape(var_4248.astype('int64'), []), relay.reshape(var_4249.astype('int64'), [16, 15, 10]), ), 1)
output = relay.Tuple([bop_4236,call_4247,var_4248,var_4249,])
output2 = relay.Tuple([bop_4236,call_4250,var_4248,var_4249,])
func_4254 = relay.Function([var_4234,var_4248,var_4249,], output)
mod['func_4254'] = func_4254
mod = relay.transform.InferType()(mod)
var_4255 = relay.var("var_4255", dtype = "uint8", shape = (6, 4, 16))#candidate|4255|(6, 4, 16)|var|uint8
var_4256 = relay.var("var_4256", dtype = "int64", shape = ())#candidate|4256|()|var|int64
var_4257 = relay.var("var_4257", dtype = "int64", shape = (2400,))#candidate|4257|(2400,)|var|int64
output = func_4254(var_4255,var_4256,var_4257,)
func_4258 = relay.Function([var_4255,var_4256,var_4257,], output)
mutated_mod['func_4258'] = func_4258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4274 = relay.var("var_4274", dtype = "uint8", shape = ())#candidate|4274|()|var|uint8
const_4275 = relay.const([[[-10,4,-1,4,6,-7,5,6,-5,9,-8,1,8,-9],[-7,-1,-9,6,-1,-6,-8,-1,10,6,-10,-1,-9,10],[-10,-8,-10,-6,5,9,-4,3,1,6,3,7,7,2],[2,-3,5,-1,-2,3,1,-3,8,9,-10,-1,7,8],[7,1,-4,-4,-8,3,2,-1,-10,9,10,7,1,5],[-7,-5,5,-4,10,7,2,2,-7,-8,7,7,5,9],[2,-5,9,3,-6,2,-4,-8,2,-2,-2,8,-8,-9],[8,1,4,-9,6,8,9,-9,-2,1,6,-2,4,10],[-6,-6,-6,4,-3,-6,7,10,-3,-10,6,8,-3,-2],[2,-10,10,-3,-3,10,-10,-4,8,4,4,8,-5,2],[9,-8,6,1,6,-4,-9,-6,9,-9,-7,-2,-6,9],[-9,3,4,10,9,-6,3,5,-4,-4,-2,-4,3,10],[-6,-5,1,-4,-7,-5,-4,-3,-2,-1,-9,3,-6,-2],[3,-2,-8,-6,5,4,-2,10,1,-3,2,-1,-6,4],[-1,3,-6,-3,-2,-5,-8,-8,-1,8,-2,7,4,-4],[-4,4,-5,-9,2,7,-2,-10,3,-3,-6,6,-2,1]],[[5,-8,-6,-4,9,-3,-7,6,5,4,-2,4,-9,-6],[-7,7,-2,1,-7,-8,8,9,6,-9,-1,-10,-9,1],[-9,9,1,8,-2,1,3,8,-5,-9,4,1,-8,-8],[-7,4,-5,-2,10,-2,-8,-4,4,-2,-8,-9,8,8],[1,4,-5,6,3,6,9,-6,1,-7,9,-4,-10,-1],[-3,6,-5,3,-1,9,8,-5,-1,5,-10,-9,-2,10],[-7,2,-2,-5,-1,6,-7,5,-10,4,3,5,10,4],[8,5,7,-5,-8,-5,-1,2,-7,5,7,-1,7,-6],[10,2,-6,-3,-4,1,3,2,8,-1,-9,4,-4,-10],[1,-1,-8,10,7,6,-4,-5,4,10,-1,8,-5,-10],[7,3,6,8,-4,7,-2,7,9,-4,1,-6,2,6],[8,10,6,5,5,5,4,5,4,-3,-3,-7,-10,9],[-8,-3,1,-4,-5,8,-4,3,2,3,9,-8,-4,9],[9,-10,-4,-5,-6,-9,-10,5,9,-2,-6,-6,3,-7],[10,-3,-5,8,-7,2,6,6,-10,9,-9,-10,-6,-9],[-4,-5,4,5,-10,9,-10,3,-6,-1,10,-6,1,-5]],[[6,-3,2,-5,6,8,-7,-5,9,10,-7,-2,10,-7],[7,5,7,4,-8,6,2,-9,-10,-5,-2,-4,5,5],[5,-4,5,-8,9,-10,4,10,9,-5,6,5,5,9],[5,-5,8,-5,-1,3,-6,7,-10,-5,8,5,-10,-4],[-10,-2,6,9,9,7,8,1,5,-3,-7,-2,-8,9],[-7,-10,-3,-6,-4,-3,9,-2,-9,1,3,7,-4,-4],[-7,-10,-5,3,-7,-9,2,-1,-3,7,7,6,-4,9],[5,10,-8,6,5,3,10,10,-5,4,7,10,9,-4],[-10,-3,-8,-6,-5,10,-4,1,-5,8,5,8,3,-6],[5,-7,4,-1,-5,9,-1,-2,-1,1,-6,-8,10,3],[-5,6,-10,8,-3,8,-7,-7,-7,-7,2,8,8,-8],[-3,2,1,-9,-8,-7,-7,-8,6,-7,4,3,4,3],[7,-10,4,10,9,8,-6,10,-4,10,-4,2,10,4],[-9,6,8,-8,-10,-10,8,6,-5,-9,-5,-8,7,6],[7,3,-7,-4,7,-9,-10,5,9,2,-8,-4,2,-1],[-3,-6,9,10,10,-2,6,5,-10,-4,2,4,8,4]],[[-1,-9,-3,7,-6,-9,1,-5,-5,-4,3,-6,5,6],[8,-3,6,-3,7,-3,9,1,-5,8,9,7,-2,-10],[4,2,7,-1,7,1,6,-7,8,-6,6,-5,7,-8],[6,8,5,2,-5,-6,8,6,-1,-10,3,-4,-9,-4],[2,5,-2,-9,-3,3,-5,10,-6,7,9,8,3,-1],[-2,9,8,5,-7,1,7,-7,2,-6,-4,-8,2,7],[10,8,-4,10,-2,-4,-1,-8,8,1,-5,-8,1,1],[2,1,-7,-7,-7,-1,-2,-8,9,-3,5,6,-2,8],[2,7,9,-7,-6,-5,1,-3,-2,-10,-9,9,7,-4],[2,2,-1,-10,-6,5,3,-8,8,9,-2,-3,2,-7],[-7,-5,2,5,-6,-4,-1,-8,-8,9,8,8,-9,-1],[10,9,8,8,-1,3,-5,-2,5,3,8,1,-1,4],[-9,2,-4,9,-5,3,-2,-3,-5,-5,7,-4,-9,-9],[-6,-4,-1,-4,-7,8,-4,8,-9,-2,8,-3,-5,-9],[5,-7,-2,-4,7,-7,-5,-8,8,-2,9,-9,1,-1],[2,1,10,6,8,7,2,-2,1,-3,-6,-3,-10,1]],[[6,-6,-5,-6,6,9,2,1,-1,10,-3,-10,1,-5],[8,10,1,4,6,1,10,6,-7,9,-10,-10,3,3],[5,-4,-5,9,-2,-1,1,-10,5,6,-5,-10,3,9],[3,-9,-1,1,7,1,3,10,6,-6,8,-3,-8,-7],[4,-8,-9,5,-1,-5,6,-10,7,-2,9,-4,-1,-7],[9,-1,-1,1,-7,-9,3,-9,-1,-8,8,-3,-8,-4],[-3,2,-7,6,4,-8,-4,-1,3,7,-8,2,3,-3],[-4,1,-9,9,8,2,5,-2,6,-9,5,3,-9,9],[2,-6,-10,4,-2,3,-10,-9,-6,-5,8,3,10,-7],[3,-2,10,1,-6,9,-10,5,1,7,9,-2,-6,8],[-3,4,3,-10,5,-4,8,7,8,-10,-10,-6,8,3],[5,1,-8,-3,-2,-5,6,-6,-3,-4,8,1,10,-4],[5,6,9,-7,2,-10,-5,-9,-2,-5,1,7,-3,5],[6,-6,7,3,9,6,2,-6,-9,-7,-2,-10,-2,-2],[5,-10,9,4,-8,-3,-8,10,3,4,1,-6,4,7],[3,2,-9,1,-10,3,1,-7,-4,-7,-1,2,-4,6]],[[-2,-5,4,-3,10,10,-8,-8,-6,-5,1,9,7,-5],[-10,1,8,7,3,-5,-5,-3,-6,1,7,4,2,-2],[-7,-1,2,8,-6,-1,6,-2,-1,-5,7,10,-4,3],[-2,-6,-4,5,-7,-5,8,3,-2,-7,9,9,-10,9],[-7,-1,-7,-7,3,6,-5,-4,7,-8,-2,1,9,-7],[-2,4,-1,8,3,1,-9,6,8,-8,-7,3,3,3],[5,-2,8,-6,-10,-1,4,-9,-10,1,-6,4,-7,-5],[2,-4,-7,6,2,-8,-8,7,10,-7,2,-8,-6,2],[-9,6,4,-10,6,-8,-10,1,3,2,-4,4,8,2],[4,9,-10,7,-7,-5,-5,-1,9,-4,10,8,6,9],[3,10,-7,5,4,-3,10,-3,-3,1,6,4,3,1],[-5,-5,-6,-8,-2,2,6,8,-7,3,5,2,1,-9],[-10,-6,-5,-3,-6,3,5,-5,-3,5,3,-10,3,-10],[-7,-1,-3,10,-9,-8,6,-2,-9,10,-9,-1,-4,-9],[-10,3,9,-4,4,2,-9,-10,-2,-5,-9,-2,-1,-1],[2,6,-2,-1,5,-5,1,4,-8,6,7,10,8,6]],[[-2,8,10,10,-3,3,8,8,-5,-1,7,2,1,-3],[3,10,-8,-1,-10,-10,-4,2,-1,3,-5,9,-2,-7],[3,3,9,1,-10,8,5,-5,-1,1,9,7,8,5],[9,4,4,-7,-1,-4,1,4,-10,-7,8,-2,-3,1],[7,3,2,7,7,2,-2,-10,6,3,3,-6,9,9],[9,5,-8,3,8,-7,-5,4,3,4,-7,7,6,-10],[1,7,9,-7,10,8,-3,-4,2,-8,1,-6,7,-8],[-9,6,-10,-2,-4,-8,1,4,-9,-2,6,9,10,-8],[1,9,-6,9,-9,7,-2,-10,8,-6,-2,-1,-8,8],[6,-6,1,6,-10,5,8,7,-4,-4,10,-3,-10,-5],[-5,-8,-8,-9,-10,10,1,-1,7,10,4,-6,-4,1],[3,4,-8,8,-9,-6,-1,-10,2,-3,9,10,7,-2],[-5,7,-8,6,3,3,-9,10,-5,-4,2,-6,1,8],[2,-9,2,6,4,5,6,-1,7,6,-2,1,-8,-6],[-2,6,-2,-4,-8,-4,4,2,-9,4,-4,10,-3,-9],[9,-1,-10,9,-10,6,-5,10,4,-7,7,-9,-4,-7]]], dtype = "uint8")#candidate|4275|(7, 16, 14)|const|uint8
bop_4276 = relay.logical_xor(var_4274.astype('uint8'), const_4275.astype('uint8')) # shape=(7, 16, 14)
func_3626_call = mod.get_global_var('func_3626')
func_3629_call = mutated_mod.get_global_var('func_3629')
var_4283 = relay.var("var_4283", dtype = "int8", shape = (1008, 1))#candidate|4283|(1008, 1)|var|int8
call_4282 = func_3626_call(relay.reshape(var_4283.astype('int8'), [6, 12, 14]))
call_4284 = func_3626_call(relay.reshape(var_4283.astype('int8'), [6, 12, 14]))
bop_4287 = relay.bitwise_xor(var_4283.astype('int32'), var_4274.astype('int32')) # shape=(1008, 1)
uop_4290 = relay.atanh(const_4275.astype('float32')) # shape=(7, 16, 14)
func_2910_call = mod.get_global_var('func_2910')
func_2913_call = mutated_mod.get_global_var('func_2913')
const_4293 = relay.const([-3.253507,-2.802456,-4.154587,-6.199925,-8.447106,3.373395,7.525584,-9.929004,-9.817239,-2.829604,-8.827886,7.953167,4.373014,1.816982,3.519073,5.355058,0.391698,8.231204,-3.117348,9.865793,1.686427,-3.117393,5.260928,2.807513,2.867002,-7.872230,-1.458015,-8.877105,-9.713763,-0.763929,-1.520165,3.025443,3.272193,9.605320,6.878567,-3.662233,-5.811831,0.321710,3.814874,9.009886,8.770027,-0.322728,-3.209713,1.483533,-9.969221,-3.293470,6.522098,-3.157646,4.861120,8.058574,-4.022249,7.273692,-4.109995,-3.108347,4.338891,-2.705705,-4.946471,-9.934390,0.390066,9.229893,5.487554,-3.180732,-7.818555,-7.692891,2.760356,-1.801631,1.531920,-9.359453,-1.393524,-4.348117,-0.972037,-1.665630,6.442769,5.011023,-5.429857,9.222709,6.345323,4.617541,-3.532212,4.333106,2.935335,-2.299397,4.189529,-0.436778,5.222880,-7.478678,0.827085,-6.473532,1.710843,9.764229,4.582824,-5.753272,-7.387860,-3.001431,0.904228,-9.999302,8.831322,8.250441,5.602375,-7.565203,-8.105801,8.038120,-0.337353,1.245428,1.292207,7.085974,1.452592,4.698881,3.645923,-5.735981,8.498195,8.154843,8.366688,-1.236828,-9.161477,-4.774724,8.167720,-7.500685,2.909654,0.266379,-4.641655,9.197746,-8.762008,-7.208909,-5.641361,-7.772406,8.131909,-5.718168,3.986794,-9.764353,-6.787861,-9.250770,-5.018403,5.569007,-8.687787,-3.911344,4.384729,-8.272042,0.523547,-1.895883,-3.030721,3.889774,-9.726889,-1.371280,-5.312533,-0.758033,4.033802,-3.441150,9.828588,-3.036813,6.046896,0.685298,-6.979580,-9.439138,-1.267056,-2.937377,-7.153234,-6.848512,7.898237,-8.518941,0.653095,-3.989192,7.650160,-4.712948,-0.091776,0.279196,-9.116385,0.541313,-4.761970,-3.858000,-5.878953,6.517973,-2.392524,6.735566,2.414546,-2.787748,-2.839072,9.922075,3.403228,9.494395,-6.028365,6.473951,5.451592,-7.283055,1.029689,-3.635477,8.528240,-6.902799,8.673966,9.874257,8.613884,-8.340763,6.822975,2.485849,6.682023,-1.337164,5.026696,-8.429895,-6.351422,0.738335,1.632098,9.049609,4.918858,3.692614,-7.381731,2.466447,-6.048574,7.078407,-5.080628,-4.078738,8.773524,7.038144,2.805435,1.830215,-1.080245,5.739029,-7.404426,-5.030270,-9.102649,1.556010,8.662629,-8.017439,-9.981748,8.983260,-0.113790,-6.679118,-9.053188,7.347542,-7.431956,-6.193695,8.656447,-0.734632,-2.143412,6.837089,-9.530781,9.233490,-0.012628,3.271965,-3.025817,7.445678,5.939911,-3.802467,2.336720,1.217929,7.448471,5.896041,4.340918,-9.307049,-3.914055,-2.177049,-1.710528,-3.629536,9.881351,0.349639,-0.804628,-6.924441,0.118310,-3.073652,-1.641076,-6.021447,9.250482,-1.535587,5.148855,-0.702322,7.620996,6.077560,1.379425,-7.291963,1.123526,-5.000788,-1.098439,5.544052,7.369367,-6.228883,2.209349,6.610039,-8.780506,4.546013,2.682035,-7.793241,-4.872645,-2.584866,2.620221,-8.907205,4.627630,8.336466,-3.382256,6.612056,-1.065602,0.081601,-4.620456,-5.953794,9.234435,-0.712355,9.650864,7.598837,-0.885826,1.725523,-2.187352,0.517059,-9.383202,9.974857,0.637367,2.112145,-4.917414,-9.627994,7.329533,-7.557747,-7.568000,9.236287,9.155947,-6.276834,2.652724,7.950860,5.229271,1.485088,8.949996,-0.672519,2.981776,-6.439647,0.103687,-9.030672,5.016870,7.569869,3.510052,-7.351444,0.005511,4.114475,-5.660329,-2.234996,9.118958,-7.117166,-2.098785,6.454086,-0.613147,4.075808,-8.809365,-1.664200,-3.288416,-7.422768,2.002824,-4.301945,9.955761,8.053361,9.652612,7.199516,5.829174,5.486719,5.256665,0.748382,3.581383,0.462534,-7.293298,9.864987,6.268040,-9.512753,-3.921321,4.380832,-4.700872,-9.752819,-0.698935,-4.954258,9.034602,0.650219,9.818192,-0.213233,9.757808,-5.813563,2.692155,3.462998,0.338691,8.019307,-0.513394,4.597723,7.058562,-1.863792,-6.148773,7.740712,5.351175,-4.871148,8.324765,9.198298,-2.979856,-8.300011,2.837799,-8.347005,-0.302244,8.946296,-2.039972,4.561905,-3.344285,8.235707,5.250213,-4.609375,7.477137,6.984060,0.008827,2.858628,-4.236332,3.763436,5.931505,4.661818,-5.606622,3.466657,6.107578,-0.722925,-5.073931,-7.124356,2.118462,-8.000893,6.962379,9.893848,-6.334190,-6.490843,4.819549,6.852364,0.748895,-1.887450,7.180047,-6.361449,-4.152454,-9.820052,-7.441503,-2.196167,1.310351,-3.411344,-7.995111,5.562289,3.255401,-6.001967,5.777250,9.654096,-5.592967,-1.667895,5.009525,-8.642569,-6.771959,0.973877,-0.922610,-5.509411,-9.013498,-9.386775,-6.357204,-1.671784,-4.182067,-5.395954,-0.026677,-0.025798,2.053413,-0.402313,-8.541348,0.897535,1.060866,2.371705,-4.843521,8.125802,2.741851,-1.467979,4.690643,6.943379,7.570878,5.350815,8.007613,-2.249906,2.651944,-5.676249,8.081168,-9.629411,-6.048277,-3.581840,4.328507,5.907491,-8.837092,-8.540679,-5.827557,6.602776,-7.274822,8.049301,-9.721987,-9.558182,-8.764983,3.619887,-4.329995,-7.151903,-6.083053,-2.124210,-5.353953,-9.579712,8.765534,-4.450476,-2.662465,3.902353,4.598612,-5.145724,-3.290196,8.526350,3.497996,-8.964106,-2.763564,-2.268132,-0.898902,-2.012963,5.402732,0.066755,6.951840,-1.171163,7.629725,-9.181235,2.652149,-1.952593,-8.150880,-7.840428,8.187639,5.226499,-0.262615,-2.783392,-6.216475,3.306641,5.066985,-6.774377,3.470411,-7.135719,-7.449895,5.544657,4.335508,8.518903,4.018196,-4.923529,9.527835,-9.574687,1.996423,-9.576377,2.808476,6.727601,-5.511863,3.102558,4.512603,-8.925400,0.255867,6.783461,1.780686,-8.484795,-7.068605,9.582411,-4.369263,2.705854,-1.182320,-9.978478,-8.941004,-5.657793,1.196136,-5.142185,6.471250,4.263993,-1.139713,-7.598580,0.603153,-3.627243,3.455254,9.775406,2.245708,7.053780,-8.724684,6.927947,-3.714533,4.542692,7.193962,-4.025254,-2.655588,5.941570,-6.688612,2.093501,-7.855911,1.791340,1.008341,-7.218863,-0.694944,3.874797,5.737623,3.227546,-6.507115,8.360799,-2.599307,7.062536,6.327799], dtype = "float32")#candidate|4293|(585,)|const|float32
call_4292 = func_2910_call(relay.reshape(const_4293.astype('float32'), [13, 3, 15]))
call_4294 = func_2910_call(relay.reshape(const_4293.astype('float32'), [13, 3, 15]))
bop_4296 = relay.greater_equal(uop_4290.astype('bool'), relay.reshape(bop_4276.astype('bool'), relay.shape_of(uop_4290))) # shape=(7, 16, 14)
bop_4302 = relay.multiply(bop_4296.astype('uint32'), relay.reshape(const_4275.astype('uint32'), relay.shape_of(bop_4296))) # shape=(7, 16, 14)
func_4168_call = mod.get_global_var('func_4168')
func_4173_call = mutated_mod.get_global_var('func_4173')
const_4306 = relay.const([3.805802,-8.381253,6.005340], dtype = "float32")#candidate|4306|(3,)|const|float32
var_4307 = relay.var("var_4307", dtype = "float32", shape = (36,))#candidate|4307|(36,)|var|float32
var_4308 = relay.var("var_4308", dtype = "float32", shape = (600,))#candidate|4308|(600,)|var|float32
call_4305 = relay.TupleGetItem(func_4168_call(relay.reshape(const_4306.astype('float32'), [1, 3]), relay.reshape(var_4307.astype('float32'), [12, 3]), relay.reshape(var_4308.astype('float32'), [600,]), ), 0)
call_4309 = relay.TupleGetItem(func_4173_call(relay.reshape(const_4306.astype('float32'), [1, 3]), relay.reshape(var_4307.astype('float32'), [12, 3]), relay.reshape(var_4308.astype('float32'), [600,]), ), 0)
func_316_call = mod.get_global_var('func_316')
func_319_call = mutated_mod.get_global_var('func_319')
var_4313 = relay.var("var_4313", dtype = "float32", shape = (182, 1))#candidate|4313|(182, 1)|var|float32
call_4312 = func_316_call(relay.reshape(var_4313.astype('float32'), [14, 1, 13]))
call_4314 = func_316_call(relay.reshape(var_4313.astype('float32'), [14, 1, 13]))
func_2502_call = mod.get_global_var('func_2502')
func_2506_call = mutated_mod.get_global_var('func_2506')
var_4316 = relay.var("var_4316", dtype = "float32", shape = (150,))#candidate|4316|(150,)|var|float32
const_4317 = relay.const([-3.232923,-7.601053,0.253442,-2.957513,5.782474,4.671324,5.581053,5.606071,3.502194,5.470110,-5.302733,1.999163,-3.541234,-6.940243,5.536555,0.771605,-6.872459,4.570234,5.070631,-2.120912,5.344834,-3.273825,7.794044,7.799428,4.211934,7.326682,-2.878077,-8.455931,9.574746,1.086002,2.337662,-6.907020,-9.043695,9.637862,3.067854,-1.239086,9.647075,-3.070294,-0.977400,6.385323,-9.580972,-6.755543,-7.535659,1.595332,0.350897,-2.476045,8.593574,4.395862,-9.183674,-0.314909,-4.591325,7.760227,3.561361,7.436209,4.339189,6.955832,1.677177,-5.110286,-0.256290,-6.424632,-0.926629,-6.129497,3.588099,2.961097,-9.289353,-7.874350,-6.399969,2.141885,6.027122,-5.326410,1.541179,-9.280428,2.774602,-1.148112,-3.465966,4.633176,-8.164109,-3.313595,4.797803,8.525933,3.100202,8.440394,6.212139,-2.115938,2.923845,0.134694,-4.411677,8.653085,8.722511,-1.929529,-0.346608,-3.252958,0.598988,8.562227,8.501308,3.722685,-5.489918,-5.664401,1.840974,-3.606074,5.945620,6.486956,3.094141,7.625742,0.024569,-2.782279,-2.503431,-3.541616,7.176064,-7.486370,-7.541889,-1.017458,-3.730077,9.004225,8.469850,-2.585025,3.333313,-1.198745,1.404341,3.582966,9.623273,-1.747730,4.423703,-4.370681,-5.274181,0.789211,-3.797030,6.823558,-2.226773,-3.047575,-2.849890,8.230845,-4.205193,-5.403567,5.204851,-9.759102,9.553348,-8.556219,0.361287,-1.607086,-6.788582,2.795630,1.637277,0.944198,9.514274,2.003718,7.794535,8.004558,-4.270723,1.879454,-5.827235,5.161115,-9.256357,-5.722778,-0.428967,-3.748223], dtype = "float32")#candidate|4317|(156,)|const|float32
call_4315 = relay.TupleGetItem(func_2502_call(relay.reshape(var_4316.astype('float32'), [5, 2, 15]), relay.reshape(const_4317.astype('float32'), [156,]), ), 3)
call_4318 = relay.TupleGetItem(func_2506_call(relay.reshape(var_4316.astype('float32'), [5, 2, 15]), relay.reshape(const_4317.astype('float32'), [156,]), ), 3)
func_3865_call = mod.get_global_var('func_3865')
func_3869_call = mutated_mod.get_global_var('func_3869')
const_4327 = relay.const([5,1,8,-5,3,1,3,-4,2,-7,9,3,-2,9,8,-8,-9,-2,-9,4,-8,-5,9,-4,-7,10,-8,9,1,-3,-5,-3,10,-3,-2,-2,2,-5,-7,1,-9,-1,-5,6,8,4,2,10,-5,-10,-10,9,-8,-2,-1,-2,-6,-7,5,7,-5,-9,-10,-7,-9,-4,-9,-2,7,-3,-9,-1], dtype = "uint16")#candidate|4327|(72,)|const|uint16
call_4326 = relay.TupleGetItem(func_3865_call(relay.reshape(var_4307.astype('uint16'), [1, 12, 3]), relay.reshape(const_4327.astype('uint16'), [2, 12, 3]), ), 3)
call_4328 = relay.TupleGetItem(func_3869_call(relay.reshape(var_4307.astype('uint16'), [1, 12, 3]), relay.reshape(const_4327.astype('uint16'), [2, 12, 3]), ), 3)
func_3865_call = mod.get_global_var('func_3865')
func_3869_call = mutated_mod.get_global_var('func_3869')
call_4337 = relay.TupleGetItem(func_3865_call(relay.reshape(var_4307.astype('uint16'), [1, 12, 3]), relay.reshape(const_4327.astype('uint16'), [2, 12, 3]), ), 3)
call_4338 = relay.TupleGetItem(func_3869_call(relay.reshape(var_4307.astype('uint16'), [1, 12, 3]), relay.reshape(const_4327.astype('uint16'), [2, 12, 3]), ), 3)
output = relay.Tuple([call_4282,bop_4287,call_4292,const_4293,bop_4302,call_4305,const_4306,var_4307,var_4308,call_4312,var_4313,call_4315,var_4316,const_4317,call_4326,const_4327,call_4337,])
output2 = relay.Tuple([call_4284,bop_4287,call_4294,const_4293,bop_4302,call_4309,const_4306,var_4307,var_4308,call_4314,var_4313,call_4318,var_4316,const_4317,call_4328,const_4327,call_4338,])
func_4341 = relay.Function([var_4274,var_4283,var_4307,var_4308,var_4313,var_4316,], output)
mod['func_4341'] = func_4341
mod = relay.transform.InferType()(mod)
mutated_mod['func_4341'] = func_4341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4341_call = mutated_mod.get_global_var('func_4341')
var_4343 = relay.var("var_4343", dtype = "uint8", shape = ())#candidate|4343|()|var|uint8
var_4344 = relay.var("var_4344", dtype = "int8", shape = (1008, 1))#candidate|4344|(1008, 1)|var|int8
var_4345 = relay.var("var_4345", dtype = "float32", shape = (36,))#candidate|4345|(36,)|var|float32
var_4346 = relay.var("var_4346", dtype = "float32", shape = (600,))#candidate|4346|(600,)|var|float32
var_4347 = relay.var("var_4347", dtype = "float32", shape = (182, 1))#candidate|4347|(182, 1)|var|float32
var_4348 = relay.var("var_4348", dtype = "float32", shape = (150,))#candidate|4348|(150,)|var|float32
call_4342 = func_4341_call(var_4343,var_4344,var_4345,var_4346,var_4347,var_4348,)
output = call_4342
func_4349 = relay.Function([var_4343,var_4344,var_4345,var_4346,var_4347,var_4348,], output)
mutated_mod['func_4349'] = func_4349
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4429 = relay.const([[-2,-3,-3,1,-9,8,5,2],[10,8,-7,-1,-1,-1,-1,-2],[5,-2,-4,-10,3,4,-7,-10],[10,3,4,-6,-9,9,2,-7],[-9,-5,-3,8,7,3,-10,-3],[2,2,1,9,4,2,-1,5],[9,3,-9,9,2,-9,7,-5],[-7,-3,4,10,1,-6,-10,-2],[-10,-2,-5,4,3,10,-5,-8],[-1,-3,-4,4,5,-8,8,-6],[5,9,7,7,-7,1,-1,6],[-10,10,-2,-9,-2,-3,-7,3],[5,1,-5,3,5,-4,2,10],[-9,-6,-5,-9,2,-9,1,10]], dtype = "int32")#candidate|4429|(14, 8)|const|int32
var_4430 = relay.var("var_4430", dtype = "int32", shape = (14, 8))#candidate|4430|(14, 8)|var|int32
bop_4431 = relay.not_equal(const_4429.astype('bool'), relay.reshape(var_4430.astype('bool'), relay.shape_of(const_4429))) # shape=(14, 8)
func_3941_call = mod.get_global_var('func_3941')
func_3944_call = mutated_mod.get_global_var('func_3944')
var_4442 = relay.var("var_4442", dtype = "int16", shape = (448,))#candidate|4442|(448,)|var|int16
call_4441 = relay.TupleGetItem(func_3941_call(relay.reshape(var_4442.astype('int16'), [7, 16, 4]), relay.reshape(var_4442.astype('int16'), [7, 16, 4]), ), 0)
call_4443 = relay.TupleGetItem(func_3944_call(relay.reshape(var_4442.astype('int16'), [7, 16, 4]), relay.reshape(var_4442.astype('int16'), [7, 16, 4]), ), 0)
func_3832_call = mod.get_global_var('func_3832')
func_3835_call = mutated_mod.get_global_var('func_3835')
const_4445 = relay.const(-5.460842, dtype = "float32")#candidate|4445|()|const|float32
const_4446 = relay.const([5.959724,-2.525538,-2.398444,-2.596684,-2.376971,0.478178,1.465678,-4.706240,3.378604,0.567794,-3.318296,2.319665,-2.538116,-0.458576,-7.367439,-9.525556,2.031459,-5.963335,-7.695339,0.526849,3.185972,-4.796413,-8.057598,6.995195,8.185802,-3.763305,-4.537537,9.320506,7.721329,-6.506481,-3.561809,8.767350,1.172493,6.878248,5.579902,-0.151904,6.393860,0.346696,-1.223808,7.592731,-6.821136,3.849233,-9.332911,5.284615,-3.137113,4.338630,-1.164336,9.178668,9.203166,1.612174,8.355676,1.124555,-6.937117,-8.593187,1.660004,-0.207700,1.216282,-1.534958,5.473249,9.911893,8.243749,-5.989987,-8.049313,9.305302,-9.236710,-1.018686,-0.542496,-2.280988,-1.114091,1.577305,4.596218,8.790416,4.054350,-7.504229,1.971945,8.084299,-8.397498,-6.120896,8.129805,-9.433197,5.714838,8.950065,-0.314648,-7.026062,-7.240367,-4.345688,-0.604097,1.478072,9.357780,-3.817113,8.273909,5.722383,9.496565,-9.497333,1.030615,-9.344917,4.095022,2.554586,6.036033,6.053402,1.095320,2.328358,6.900504,-1.053036,-5.464655,-1.936133,-8.007445,-8.056374,8.258868,-5.334516,8.416916,4.850360,-8.595075,4.257004,9.322402,4.234558,-2.475030,-4.514428,3.083888,6.109957,8.273723,-0.616941,6.960423,6.821280,3.853264,-0.616438,-3.702442,-0.525142,-6.576032,-7.127751,-3.270752,-2.653398,1.944197,-6.631353,2.125739,-1.206106,0.786131,-4.470830,1.505440,-3.534595,8.583992,-5.412993,-7.384901,-0.629837,-5.912197,-6.972704,1.894784,5.350039,2.139658,5.668881,4.583770,3.260019,-1.897484,-3.099977,5.354298,2.900341,3.465012,-0.916007,-0.953247,-6.446755,-4.477648,7.074151,0.437183,-9.014605,-0.073950,-5.729396,8.470069,0.399316,8.716353,-0.755278,-8.144922,-1.712531,0.112806,6.959233,5.838840,-1.759227,3.063619,0.604698,-0.224800,9.472734,-5.601493,8.298662,-2.265914,7.476184,-0.548311,-6.487550,6.516468,-5.261565,-6.193425,-7.520699,6.270892,1.469565], dtype = "float32")#candidate|4446|(192,)|const|float32
call_4444 = relay.TupleGetItem(func_3832_call(relay.reshape(const_4445.astype('float32'), []), relay.reshape(const_4446.astype('float32'), [3, 16, 4]), ), 1)
call_4447 = relay.TupleGetItem(func_3835_call(relay.reshape(const_4445.astype('float32'), []), relay.reshape(const_4446.astype('float32'), [3, 16, 4]), ), 1)
output = relay.Tuple([bop_4431,call_4441,var_4442,call_4444,const_4445,const_4446,])
output2 = relay.Tuple([bop_4431,call_4443,var_4442,call_4447,const_4445,const_4446,])
func_4466 = relay.Function([var_4430,var_4442,], output)
mod['func_4466'] = func_4466
mod = relay.transform.InferType()(mod)
var_4467 = relay.var("var_4467", dtype = "int32", shape = (14, 8))#candidate|4467|(14, 8)|var|int32
var_4468 = relay.var("var_4468", dtype = "int16", shape = (448,))#candidate|4468|(448,)|var|int16
output = func_4466(var_4467,var_4468,)
func_4469 = relay.Function([var_4467,var_4468,], output)
mutated_mod['func_4469'] = func_4469
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4495 = relay.var("var_4495", dtype = "float32", shape = (4, 1, 8))#candidate|4495|(4, 1, 8)|var|float32
uop_4496 = relay.cosh(var_4495.astype('float32')) # shape=(4, 1, 8)
output = uop_4496
output2 = uop_4496
func_4500 = relay.Function([var_4495,], output)
mod['func_4500'] = func_4500
mod = relay.transform.InferType()(mod)
var_4501 = relay.var("var_4501", dtype = "float32", shape = (4, 1, 8))#candidate|4501|(4, 1, 8)|var|float32
output = func_4500(var_4501)
func_4502 = relay.Function([var_4501], output)
mutated_mod['func_4502'] = func_4502
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4732 = relay.const([[[1,1,3]],[[-10,-4,8]],[[6,-8,8]],[[5,-6,10]],[[7,-9,6]],[[-8,-9,8]]], dtype = "uint32")#candidate|4732|(6, 1, 3)|const|uint32
var_4733 = relay.var("var_4733", dtype = "uint32", shape = (6, 16, 3))#candidate|4733|(6, 16, 3)|var|uint32
bop_4734 = relay.bitwise_xor(const_4732.astype('uint32'), var_4733.astype('uint32')) # shape=(6, 16, 3)
func_4341_call = mod.get_global_var('func_4341')
func_4349_call = mutated_mod.get_global_var('func_4349')
var_4739 = relay.var("var_4739", dtype = "uint8", shape = ())#candidate|4739|()|var|uint8
var_4740 = relay.var("var_4740", dtype = "int8", shape = (1008,))#candidate|4740|(1008,)|var|int8
const_4741 = relay.const([4.462790,0.640185,3.409440,5.144126,-4.238084,-2.314914,5.486904,7.768854,3.269384,8.992818,7.045041,3.915065,-6.808112,-7.203124,-6.440986,-1.550895,4.256967,-1.829928,0.710533,0.597372,2.673805,4.816236,5.415243,-7.474427,-8.503459,-1.809914,6.768644,9.818475,-2.398715,0.617295,6.386924,-3.676810,8.104746,-9.124639,1.262117,-8.397917], dtype = "float32")#candidate|4741|(36,)|const|float32
const_4742 = relay.const([-6.949876,-2.677475,-5.122655,-5.921681,-5.138268,4.478184,-5.991121,7.506199,-0.840336,-8.365680,-7.618759,-4.241669,-4.246163,-5.896733,3.389965,6.988027,2.706551,-7.869132,-1.889505,8.245584,6.955122,6.678472,3.699901,2.810916,-1.109298,0.474744,-2.017296,-0.859570,-3.574744,9.895336,4.813344,-3.776334,-9.953791,-4.407641,9.951954,2.882674,-1.275817,-0.922885,6.727489,3.993240,-5.276690,-9.233511,-7.710190,1.440719,2.958331,-5.967551,2.432145,-7.826394,-8.714817,-4.628343,-7.851865,-8.330614,-8.564416,4.725213,-7.636509,-3.256389,8.032048,-9.590187,7.834839,9.517550,-0.882016,0.477099,-6.933498,2.911745,-1.600012,-6.178360,6.010389,7.387255,-9.315594,3.912163,5.712842,5.209582,-6.033437,9.050994,0.801054,-9.427527,-4.778502,-0.655759,9.112821,1.170525,5.191243,8.841055,-9.565267,5.698502,3.401333,-1.784147,-3.247150,7.029229,2.079735,-9.215173,7.406054,-2.966388,3.576407,-1.740214,-2.912935,-5.221297,-9.651221,-9.735097,9.139623,8.525457,-4.477912,5.220457,0.549103,3.102843,3.918581,9.600332,-5.290933,1.173662,-2.975565,5.671045,0.999657,1.486627,7.347392,1.313599,8.186502,1.484395,-6.787957,-5.936431,7.143875,-5.835723,0.630157,-0.014054,9.533131,9.871140,2.448506,-9.860578,4.766296,-5.012914,2.642506,3.671469,-6.410398,-5.201378,7.119936,-8.307500,-2.895850,-5.544457,0.541697,3.798287,-1.652652,-7.016201,0.630410,-1.647690,-3.998989,7.157234,-4.264532,-2.821061,8.149597,3.058412,9.852927,-9.248451,-9.840795,-2.039011,3.103019,-4.283101,-0.114584,1.394104,8.996043,-7.931840,5.176657,2.261342,-0.084230,-2.865578,-1.409340,2.800851,-8.503277,5.250460,-2.088213,-1.057726,-8.320039,7.264973,2.182061,-0.099908,-9.165785,1.719892,6.310562,-4.861179,-7.742471,8.208112,-5.135831,7.417905,-0.741981,-4.919497,-1.871292,-4.732374,8.072763,7.205182,3.939131,-1.696866,2.981156,1.011309,-8.820745,-4.950340,-3.576292,-1.026611,-3.329423,2.478081,-6.533939,5.924306,-5.121399,4.815097,5.465874,4.725289,6.870510,2.144864,2.194083,2.821172,-7.332961,-0.671985,9.377094,2.538286,-9.692870,6.167773,-3.459880,1.410500,-8.887563,9.632797,-3.152020,-3.012978,-2.008642,-8.796392,-1.012930,0.376203,7.837890,-9.071220,-9.161913,8.858476,-0.803287,-8.236218,1.855289,-8.933668,-8.597349,-9.498211,-9.770478,-3.742297,-0.591104,-5.940485,-4.088767,9.832458,3.023246,8.402302,5.244261,0.654437,9.889163,3.829646,1.619317,-6.792268,3.282294,-3.719571,-4.061102,-6.685109,5.610554,2.282159,-5.867239,-8.711747,-8.994154,-5.969218,-5.570121,-6.105196,6.877173,-1.982978,4.636218,-6.758608,4.058705,-7.973665,-8.470792,-6.032281,9.053062,4.834915,-4.755749,4.830528,7.036453,3.557157,9.497788,9.208769,5.841692,-0.008820,1.882167,6.334939,0.441249,-9.918332,-4.278974,-4.043199,-3.286661,9.499207,7.083165,-5.550707,-2.416471,-5.371807,5.549079,-0.204406,1.255008,0.523044,-5.003310,-7.216459,-0.358782,0.155587,7.272391,-9.272965,6.598816,4.854076,-7.079839,-7.331292,6.773228,5.729596,-0.889705,1.913102,-5.489200,-7.427240,5.869899,-2.647831,5.421645,-4.914810,9.933679,7.485967,-7.922835,0.860699,-1.342075,-1.744526,-1.502289,-4.557953,2.973548,8.545056,-1.701814,-1.220083,-5.073377,2.386431,-8.612794,-5.392158,-1.096169,5.741671,-0.354149,3.727263,-1.491737,-7.391336,9.627594,5.801951,-5.643208,-7.885105,7.481110,-2.340555,-0.632334,9.141137,8.655851,-4.008685,9.980435,9.621652,8.414611,-3.118890,-5.760414,-9.930450,9.666557,-4.693859,-2.769650,-8.945981,-1.377035,9.036789,-5.516135,1.161390,4.951255,4.454993,0.621371,-8.292877,-4.111254,-9.197171,-7.870275,-1.234702,5.400550,9.651203,-2.601394,3.743874,8.264627,7.563598,7.373992,9.340282,-7.694433,-1.556999,1.944943,-2.393000,4.783572,-9.607697,-8.138180,-1.584339,-2.619751,1.643606,3.860851,5.484404,-5.175520,0.776199,2.564026,-8.824661,7.705054,-7.472290,7.279931,-0.308669,0.192269,-8.157162,-1.374427,1.453813,7.760108,0.254869,3.989053,9.419729,6.452254,-3.792793,8.718941,-5.543776,0.870800,-0.619280,-1.977834,8.025780,7.039443,8.730682,-6.987303,-3.977496,1.939751,4.037654,-1.777243,-3.493155,3.593821,9.605011,7.672977,7.937531,-6.223146,-6.393996,3.836161,-1.901265,2.687158,-4.508946,5.908156,5.550608,-3.121884,4.553810,1.036097,-2.843674,-1.382729,-8.397442,4.782308,-6.324556,4.097196,-0.041850,3.703886,1.224829,-1.551271,-2.121191,7.653736,9.166740,-6.638285,-4.370590,-3.282154,-0.850009,-2.110772,0.840931,6.500857,8.958092,-3.902190,9.928454,7.629520,-6.727279,-0.482307,7.829772,2.135152,3.699491,7.928555,8.301966,-8.488368,8.524639,-3.946589,-5.187314,-8.977073,-0.452288,-5.220395,-8.958664,8.819407,0.443181,-0.563638,2.322074,6.948748,0.958399,-3.700255,8.577205,8.128706,-2.296647,9.944648,2.937484,-6.821372,-0.595698,6.349332,-6.433974,2.840362,-8.568713,-9.387463,3.439835,-8.974123,7.270395,-2.461093,7.935720,7.832355,1.599893,-8.515888,-5.623505,0.679005,0.355443,-1.515223,0.835428,-0.293333,2.219284,8.625700,-9.480325,0.647635,-7.114243,-0.290548,6.134618,4.164750,-0.677228,0.426792,9.714540,0.956563,1.387437,-5.476085,-6.117288,-0.354307,-9.400753,-8.199126,0.658437,-4.097546,8.844339,6.142196,-7.601100,-1.954285,4.172422,1.745243,-6.886371,4.187802,-3.092753,-1.096617,-0.446947,-3.715908,-9.001806,-0.808331,2.632938,4.784800,2.216713,8.900063,-0.723881,3.100662,-6.070360,-6.366165,7.219961,-0.702401,9.987404,-3.365183,-8.076058,-1.413141,-3.671397,-3.444822,0.122113,-7.193541,9.793268,-7.839039,6.839367,8.263070,9.378035,-3.278853,4.914487,-4.711965,0.192980,0.781923,-2.843313,-5.151260,-8.300560,-2.690329,0.013496,-7.858808,-9.517408,-4.971605,-0.795506,4.856039,8.386902,9.136631,0.304604,2.420066,-5.562316,-9.787770,7.738297,1.306352,9.972422,4.742278,9.684311,1.254515,6.880372,8.980997,7.071708,1.466226,8.645713,-1.118696,-8.603619,8.181199,-4.145361,0.293120,2.221921], dtype = "float32")#candidate|4742|(600,)|const|float32
const_4743 = relay.const([2.995841,-9.149333,-1.972989,-8.756607,-7.200973,-1.366165,-4.560044,-5.207666,-0.661594,-5.517869,2.685015,4.911059,-7.820964,-2.855047,-3.732134,9.172271,-7.620238,-9.418884,3.944317,-8.560324,6.263435,1.918199,-8.713049,-7.934803,-1.421762,4.079530,9.174548,6.289223,0.317756,6.892631,-8.936522,3.235228,-1.608468,2.990354,-2.321132,1.721031,3.138613,3.036943,-5.742459,-3.927320,-6.675967,2.954908,8.539401,-9.820436,-2.420925,-5.578365,-5.003313,3.577364,6.429444,-9.986329,-4.378399,6.076985,-0.286468,-0.869767,-8.101028,0.767975,-7.125656,-9.020941,2.681554,-0.147608,-5.962485,5.850999,-0.921596,-6.081807,2.582241,8.031017,-1.053656,1.824685,6.642031,-2.206009,5.823500,-1.537074,-7.775548,2.305482,7.989632,3.899830,-7.191793,-8.394724,9.548830,-0.946217,5.986297,-0.285275,0.700459,-1.165369,3.035751,-0.276464,6.489735,-7.005753,-7.702011,8.587578,4.607403,2.354936,8.527372,-8.103476,-0.724474,-5.381212,-6.674422,-3.759770,-3.713012,-9.441103,5.220955,-4.529793,-8.863202,-1.117066,-2.657832,-6.030492,-2.547721,1.097103,-9.142720,-3.981757,5.648950,-2.858427,1.671186,9.495940,-9.271818,-3.660506,-4.800748,-1.483147,0.552949,0.095125,-0.814157,-0.715798,-2.826041,6.448853,8.812966,5.983051,-3.053674,3.358773,-3.241944,3.111396,-0.380639,-0.503148,1.611262,9.081856,9.724494,-5.460626,8.251034,-1.879622,4.284054,-0.513929,1.236907,2.618900,0.978977,-8.319815,2.780206,-5.067856,6.380619,-0.310825,1.658224,0.249513,6.483724,7.571445,-2.881169,-4.078687,5.211730,0.030522,-8.630813,-8.013636,9.223982,-6.331434,-7.693891,-6.982461,6.079675,-2.806471,0.825198,-4.624726,-0.156433,1.704584,0.843773,-8.902776,-8.159900,-6.652739,-4.725222,-8.354664,7.413335,-7.024937,-0.272037,8.924498,1.184672,-4.001952,0.400227,4.802210], dtype = "float32")#candidate|4743|(182,)|const|float32
var_4744 = relay.var("var_4744", dtype = "float32", shape = (150,))#candidate|4744|(150,)|var|float32
call_4738 = relay.TupleGetItem(func_4341_call(relay.reshape(var_4739.astype('uint8'), []), relay.reshape(var_4740.astype('int8'), [1008, 1]), relay.reshape(const_4741.astype('float32'), [36,]), relay.reshape(const_4742.astype('float32'), [600,]), relay.reshape(const_4743.astype('float32'), [182, 1]), relay.reshape(var_4744.astype('float32'), [150,]), ), 1)
call_4745 = relay.TupleGetItem(func_4349_call(relay.reshape(var_4739.astype('uint8'), []), relay.reshape(var_4740.astype('int8'), [1008, 1]), relay.reshape(const_4741.astype('float32'), [36,]), relay.reshape(const_4742.astype('float32'), [600,]), relay.reshape(const_4743.astype('float32'), [182, 1]), relay.reshape(var_4744.astype('float32'), [150,]), ), 1)
output = relay.Tuple([bop_4734,call_4738,var_4739,var_4740,const_4741,const_4742,const_4743,var_4744,])
output2 = relay.Tuple([bop_4734,call_4745,var_4739,var_4740,const_4741,const_4742,const_4743,var_4744,])
func_4749 = relay.Function([var_4733,var_4739,var_4740,var_4744,], output)
mod['func_4749'] = func_4749
mod = relay.transform.InferType()(mod)
var_4750 = relay.var("var_4750", dtype = "uint32", shape = (6, 16, 3))#candidate|4750|(6, 16, 3)|var|uint32
var_4751 = relay.var("var_4751", dtype = "uint8", shape = ())#candidate|4751|()|var|uint8
var_4752 = relay.var("var_4752", dtype = "int8", shape = (1008,))#candidate|4752|(1008,)|var|int8
var_4753 = relay.var("var_4753", dtype = "float32", shape = (150,))#candidate|4753|(150,)|var|float32
output = func_4749(var_4750,var_4751,var_4752,var_4753,)
func_4754 = relay.Function([var_4750,var_4751,var_4752,var_4753,], output)
mutated_mod['func_4754'] = func_4754
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4781 = relay.var("var_4781", dtype = "int32", shape = ())#candidate|4781|()|var|int32
var_4782 = relay.var("var_4782", dtype = "int32", shape = (1, 11, 12))#candidate|4782|(1, 11, 12)|var|int32
bop_4783 = relay.subtract(var_4781.astype('int32'), var_4782.astype('int32')) # shape=(1, 11, 12)
func_316_call = mod.get_global_var('func_316')
func_319_call = mutated_mod.get_global_var('func_319')
var_4792 = relay.var("var_4792", dtype = "float32", shape = (182,))#candidate|4792|(182,)|var|float32
call_4791 = func_316_call(relay.reshape(var_4792.astype('float32'), [14, 1, 13]))
call_4793 = func_316_call(relay.reshape(var_4792.astype('float32'), [14, 1, 13]))
func_4254_call = mod.get_global_var('func_4254')
func_4258_call = mutated_mod.get_global_var('func_4258')
var_4810 = relay.var("var_4810", dtype = "uint8", shape = (384,))#candidate|4810|(384,)|var|uint8
const_4811 = relay.const([4,5,2,10,2,-4,3,1,-1,-10,1,-2,8,-5,7,9,7,-3,-9,-5,-10,-1,2,-2,-7,2,10,4,-5,-6,-9,4,-10,7,3,-2,4,5,-7,7,-7,-2,4,4,-7,2,9,5,4,-1,-5,-7,6,5,8,5,-10,4,-5,3,-1,9,10,1,8,-10,-3,-4,-10,-2,10,4,6,-5,-8,-2,-3,9,7,-7,2,-7,-4,-5,9,-3,-7,-8,4,-4,2,-1,9,8,2,8,-3,-10,-6,-1,4,-4,10,-4,5,-7,5,2,10,9,-7,7,-4,7,1,6,2,6,10,-6,-1,-4,3,-2,7,-6,-2,2,-9,7,9,-5,1,-2,-3,-10,1,1,-9,6,6,-10,-4,-4,3,3,5,2,-1,-1,-3,1,4,-10,6,-10,-10,9,-7,5,6,-4,7,-9,10,-5,2,9,-5,-10,6,3,2,-10,-7,-9,-4,-6,-10,-9,6,5,7,3,-4,-5,2,-6,2,-3,2,5,-6,-9,7,-7,4,-10,-6,7,5,2,-1,-2,-6,-3,-9,-6,-9,-3,5,-9,2,1,2,1,9,-7,-2,3,-7,10,-5,3,3,10,6,8,9,-7,7,-10,-1,-5,7,-5,-6,-2,-1,-5,-1,-4,-4,-6,-2,-6,10,5,5,6,-10,8,-4,-7,3,1,8,-2,8,7,-10,-10,7,4,5,-3,9,-3,2,-9,-3,-1,-6,5,-1,-5,-3,3,-10,3,-5,2,-10,8,-4,-6,-9,-8,-10,-8,-5,-3,-10,10,1,7,2,1,-2,-1,-10,-3,-4,4,4,-6,-7,-9,3,-8,5,-10,3,-8,-4,1,-7,-1,-5,-4,6,-2,-9,1,2,-6,-3,7,-10,2,5,-8,-8,-3,3,-6,9,2,-8,-10,2,-1,-2,10,-3,-6,6,3,2,-8,5,-3,-9,4,10,10,-8,7,-9,-2,9,-3,1,-8,-1,-7,10,3,-7,-1,-1,-8,-3,-2,10,-7,3,4,5,8,-2,-4,-5,6,-6,-8,7,9,-9,-4,-7,9,-2,-6,9,-3,-9,3,-6,5,-5,10,-6,-4,1,5,-3,-8,9,10,-5,9,1,-7,3,8,4,-2,8,5,-5,7,-7,1,-6,4,-5,7,-6,-1,-6,-7,-9,-1,4,-6,8,-9,6,-1,-2,-6,-9,-2,-7,6,-4,-6,-1,-9,4,-5,7,-7,3,-7,-4,-1,4,-2,8,6,10,-4,8,-7,9,5,6,-2,2,4,-10,9,-10,-7,-8,10,-3,-10,-10,-3,10,8,10,5,-7,7,5,3,8,6,3,5,-2,6,3,2,7,-9,10,-8,2,6,1,5,-9,5,-8,-7,5,-4,-5,2,-6,9,-3,-5,-2,6,-8,3,1,9,-8,10,4,-2,10,-10,-2,-4,-6,4,10,3,1,7,-6,1,-5,-9,-5,-7,-6,-3,6,5,-8,1,-7,6,-2,9,-9,2,-3,2,-2,7,6,6,9,5,10,-3,-2,-6,2,-10,10,-7,-3,-3,10,2,-9,-9,10,4,-3,1,-8,10,4,2,-4,-7,10,1,-1,7,1,-8,3,3,1,-1,-2,-10,5,-10,-3,-5,8,-2,-8,9,-8,-2,-9,6,10,-10,10,-9,-3,3,6,8,3,3,2,3,-8,-10,-2,6,4,4,-7,-1,2,6,-2,-3,8,-10,-7,10,-10,2,-5,-3,6,6,-2,2,1,-3,-6,-1,2,5,-4,7,-5,5,-7,10,-8,7,-3,4,-8,-8,3,9,1,-7,6,9,10,3,4,3,10,-2,10,1,-2,2,-10,-1,4,-6,-1,-2,-10,-10,-8,6,2,5,3,2,4,-3,5,-7,-3,9,-9,2,-8,6,7,6,-10,-3,-6,10,-7,6,6,-10,6,10,-10,7,-7,4,4,3,-10,9,-1,9,2,1,9,-7,-1,-2,-1,1,-1,2,-6,1,3,-3,9,-2,7,6,-5,3,-10,-8,-6,-1,-3,-4,9,-4,-5,7,-1,4,-2,-6,-3,-4,-5,-6,-1,-10,9,3,1,-10,-8,-10,-6,9,-5,5,-5,5,-1,-3,-9,7,8,7,9,8,4,8,-4,-6,-1,1,1,-6,-6,-5,3,-4,-3,-2,8,-4,10,2,7,5,10,2,1,-6,-8,-3,-6,-1,9,5,-3,-10,9,9,10,5,-9,5,-6,6,-5,-2,7,10,-9,3,-4,-7,7,-10,-9,10,2,7,-6,2,1,2,9,3,-9,-2,-1,5,-4,-6,-7,-2,-2,7,-1,1,4,9,7,3,-6,8,-3,-7,5,-1,-10,3,3,9,-8,-5,2,-8,-4,5,-6,-1,-6,-6,-10,5,-4,-1,6,-1,8,1,-10,1,9,-5,-8,2,5,-5,6,6,-8,-7,4,-3,3,-2,-10,-6,8,-2,10,-2,-3,-1,-9,-1,1,-1,5,5,5,-1,-2,-6,2,7,-3,6,-8,-4,-3,1,-2,-9,8,5,3,10,4,-6,-3,8,-3,-1,3,-7,-10,-10,-3,-9,3,4,-9,3,-2,10,1,-3,-2,5,-10,2,3,2,1,6,-7,-1,-9,-2,3,-8,9,1,4,7,-10,-3,8,-8,-1,2,7,6,8,-6,-9,-5,6,10,-4,3,3,-7,-5,2,1,4,9,-5,6,-8,-8,3,-1,-3,9,8,-5,-7,-2,-6,4,1,10,2,9,-2,5,8,-10,10,8,3,3,-4,8,-7,2,8,4,-9,-10,-10,8,-8,1,-10,-5,4,3,-4,8,5,-1,-3,1,-10,4,-5,-9,3,-2,-1,-5,9,-3,-1,6,2,-7,6,6,10,-7,-2,-1,-6,-9,-1,2,-4,-5,-5,-1,10,-1,-7,-4,6,-5,8,5,-8,-1,-9,-9,5,10,-6,-6,-8,-5,-3,-3,8,9,-3,-10,-9,7,3,2,1,7,-2,4,-1,6,-5,4,8,-1,-8,-9,-1,4,6,1,10,5,-2,-4,5,6,-3,-7,-4,2,-9,-6,1,6,9,-5,7,3,-8,-4,-10,-6,1,-4,2,-6,8,1,3,9,7,1,5,-5,4,7,-2,-7,-6,9,-6,9,6,-7,9,10,-9,2,-6,6,-8,4,-8,4,-1,-4,-5,-4,2,1,5,-9,-4,-8,-10,2,1,-10,6,-5,-7,5,1,-5,9,6,7,10,-8,2,7,8,8,7,1,1,2,-10,-5,5,8,8,7,-7,-8,-3,-10,1,8,-4,-3,-7,-2,7,1,-1,-3,6,-9,-7,9,10,-10,9,-10,-8,-9,7,1,1,5,-3,-5,10,-10,-10,8,10,4,7,4,8,-10,9,10,5,3,6,5,-3,5,-5,5,1,7,-5,5,6,-8,-9,4,4,2,-9,-7,3,6,-5,5,2,5,-3,-1,-6,-6,5,-10,1,-10,8,-1,-9,9,1,9,-6,-3,5,-9,-10,7,-5,8,-9,-4,-6,-8,-5,-1,10,2,-6,-4,6,3,6,-5,9,9,-2,6,10,-4,-10,-1,-7,-6,-5,-6,-4,9,3,3,7,-1,-4,10,-3,-9,1,3,1,3,-2,7,1,7,1,-5,3,9,7,3,4,-2,2,-5,7,-8,-8,-4,-4,3,1,6,-8,-1,-6,2,6,7,1,10,-1,-6,7,9,1,7,-2,7,-7,4,5,-3,1,-9,-3,10,-9,-4,6,-8,-7,-10,7,10,6,-9,-3,-1,2,9,-3,9,7,8,7,2,-2,-3,-10,5,9,8,-6,-6,-3,6,-4,-7,10,-4,-3,1,1,-6,-6,-10,5,-7,-10,-9,-8,8,2,2,-1,9,5,1,3,-8,10,-6,-7,-6,-5,-10,2,4,-3,5,5,10,-3,7,-10,-5,-4,-3,-3,7,-6,1,-5,1,1,2,2,-5,2,-1,6,1,8,-10,5,-8,-6,-10,-4,-9,-8,1,10,5,8,6,-3,-6,3,1,-5,10,10,2,-10,10,-1,-10,-1,-5,-2,-4,8,-5,6,-10,4,4,-9,-9,7,-8,2,-9,4,1,5,-8,-5,-5,-8,-2,6,-6,2,5,-5,-10,-3,-2,-5,3,-8,4,-4,4,5,-4,-4,7,6,-7,-6,-1,-6,-8,-6,10,1,-7,4,-7,-7,-9,1,-9,7,-9,-5,-4,3,-1,-2,-1,4,8,-9,-6,-3,-9,10,-1,-6,-9,-1,1,6,3,2,1,-1,-5,-3,9,5,-10,10,1,4,-6,-5,-8,-10,9,4,9,10,-8,-6,-10,-8,5,4,3,-5,2,7,-1,1,-8,-1,-2,2,7,-10,-8,-9,-6,8,2,10,3,8,-6,-5,5,1,10,-9,1,6,-10,2,-10,7,4,-10,7,-5,6,-7,-8,8,4,-5,-9,-2,-5,-4,5,-1,-9,9,6,8,4,4,-8,9,2,-6,-4,1,-3,6,-6,-10,-7,-2,-1,-6,-8,6,-5,-7,-9,-9,1,2,-6,-3,-5,-7,2,-5,10,9,-4,-5,9,5,2,1,-5,-7,-1,-3,-5,-1,2,1,9,-1,4,9,5,-1,7,10,5,1,2,-4,-4,6,-1,7,7,-3,3,6,8,-7,-7,5,8,8,1,9,-7,3,-1,9,2,1,-6,5,4,8,-1,-5,-10,1,7,1,4,-3,6,-5,4,4,-2,-5,-1,10,-6,2,-8,-9,2,8,-4,3,2,6,5,-9,9,5,-5,-3,-10,6,10,4,3,-10,-4,7,-2,-6,-5,5,-7,5,7,-2,4,6,3,-8,3,-5,2,3,-7,2,-3,7,9,-3,-9,-5,5,9,-3,-8,4,3,7,1,-6,5,1,-1,-3,1,1,7,9,-6,4,1,9,-5,2,8,10,-7,-5,-3,3,10,-10,-2,6,3,1,-7,8,7,-9,-7,-8,10,-5,2,7,-1,-3,-7,-10,7,6,4,-8,-3,-5,6,5,9,-10,-7,4,-7,-3,-4,-7,-6,6,7,2,3,-8,-3,6,4,-2,5,1,3,-8,-6,-9,-8,-6,-3,4,-8,-6,7,4,9,4,-3,8,8,-4,-1,-1,-2,-3,-7,-10,9,-7,-9,2,6,4,1,-5,7,7,4,6,-5,10,8,-9,5,5,-5,-2,3,2,7,4,9,-10,9,1,-7,-6,-3,1,-10,-2,5,8,1,3,9,9,-9,3,7,2,6,-6,-4,5,-5,-9,-4,-10,8,10,-1,7,8,-9,-3,8,8,6,-2,6,-1,-10,1,-9,-3,6,8,5,-3,-10,5,6,1,-7,-7,10,5,3,10,-7,-1,-5,6,6,4,8,5,3,9,8,-1,4,-10,4,-10,-1,5,1,-7,3,-4,-1,6,-4,-1,9,-3,-2,1,-3,8,-2,-9,6,-10,7,9,-3,-1,-8,-1,8,1,7,5,-2,3,6,7,-9,-1,2,-6,5,-4,-2,1,9,8,-5,-5,6,9,1,5,4,6,-6,-1,-10,3,7,9,-7,1,2,8,-5,1,4,6,2,2,-6,6,-7,7,-4,-2,-7,-4,1,6,-9,-2,3,-9,-9,2,7,1,-6,9,-9,2,6,-5,-7,2,10,-9,9,-9,-2,-6,-8,2,-9,5,-2,4,-10,-2,1,-3,8,-3,1,-7,-4,1,-2,-5,1,-9,-4,10,3,3,8,5,1,2,2,4,-4,6,-7,9,1,-3,-2,-3,5,-8,-5,8,1,-7,-1,8,7,5,7,1,3,-4,-7,9,4,-4,10,-4,-3,-3,3,4,-5,5,-5,1,10,-3,6,-10,1,1,7,-4,8,7,-9,5,-1,8,-7,-4,-6,-6,10,5,10,-5,-1,9,4,-5,8,9,-10,-5,-7,6,5,8,-5,-7,8,4,-8,-1,9,-7,5,6,4,10,10,7,-7,-1,9,-9,-9,-6,-4,-1,-2,9,6,-1,-7,-4,-9,2,-7,10,10,-10,-2,8,-3,10,9,3,5,8,6,-6,-2,-3,-1,2,4,-4,8,4,-3,7,6,-9,-5,-10,6,8,-4,6,5,9,-10,8,5,1,8,1,-9,2,7,7,-8,3,7,7,7,-3,-1,9,5,-3,10,-9,-4,5,5,-5,8,-4,7,-8,1,3,4,-5,2,6,-4,2,-7,9,2,6,-2,-4,-4,-5,-6,5,8,3,-2,3,5,3,-4,-6,6,6,-2,9,3,-1,2,-2,-7,-2,3,2,1,-2,8,1,9,2,-8,-5,6,-1,-1,-1,-8,-7,8,-1,-7,-6,-10,-6,4,10,10,-4,-1,-5,8,3,10,-6,-1,9,-1,-10,-2,10,6,-8,5,-3,7,-3,5,-2,7,-5,-7,6,-7,-9,-5,-5,-10,7,6,-4,-9,9,-2,-3,1], dtype = "int64")#candidate|4811|(2400,)|const|int64
call_4809 = relay.TupleGetItem(func_4254_call(relay.reshape(var_4810.astype('uint8'), [6, 4, 16]), relay.reshape(var_4781.astype('int64'), []), relay.reshape(const_4811.astype('int64'), [2400,]), ), 2)
call_4812 = relay.TupleGetItem(func_4258_call(relay.reshape(var_4810.astype('uint8'), [6, 4, 16]), relay.reshape(var_4781.astype('int64'), []), relay.reshape(const_4811.astype('int64'), [2400,]), ), 2)
output = relay.Tuple([bop_4783,call_4791,var_4792,call_4809,var_4810,const_4811,])
output2 = relay.Tuple([bop_4783,call_4793,var_4792,call_4812,var_4810,const_4811,])
func_4813 = relay.Function([var_4781,var_4782,var_4792,var_4810,], output)
mod['func_4813'] = func_4813
mod = relay.transform.InferType()(mod)
mutated_mod['func_4813'] = func_4813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4813_call = mutated_mod.get_global_var('func_4813')
var_4815 = relay.var("var_4815", dtype = "int32", shape = ())#candidate|4815|()|var|int32
var_4816 = relay.var("var_4816", dtype = "int32", shape = (1, 11, 12))#candidate|4816|(1, 11, 12)|var|int32
var_4817 = relay.var("var_4817", dtype = "float32", shape = (182,))#candidate|4817|(182,)|var|float32
var_4818 = relay.var("var_4818", dtype = "uint8", shape = (384,))#candidate|4818|(384,)|var|uint8
call_4814 = func_4813_call(var_4815,var_4816,var_4817,var_4818,)
output = call_4814
func_4819 = relay.Function([var_4815,var_4816,var_4817,var_4818,], output)
mutated_mod['func_4819'] = func_4819
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4830 = relay.var("var_4830", dtype = "bool", shape = (10, 4, 6))#candidate|4830|(10, 4, 6)|var|bool
var_4831 = relay.var("var_4831", dtype = "bool", shape = (10, 4, 6))#candidate|4831|(10, 4, 6)|var|bool
bop_4832 = relay.logical_or(var_4830.astype('bool'), relay.reshape(var_4831.astype('bool'), relay.shape_of(var_4830))) # shape=(10, 4, 6)
uop_4835 = relay.sqrt(var_4831.astype('float64')) # shape=(10, 4, 6)
bop_4837 = relay.divide(uop_4835.astype('float64'), relay.reshape(bop_4832.astype('float64'), relay.shape_of(uop_4835))) # shape=(10, 4, 6)
func_2560_call = mod.get_global_var('func_2560')
func_2564_call = mutated_mod.get_global_var('func_2564')
var_4841 = relay.var("var_4841", dtype = "float32", shape = (50, 15))#candidate|4841|(50, 15)|var|float32
const_4842 = relay.const([-6.413690,-7.301539,-5.823756,-0.039594,1.061382,-0.605189,8.146805,-1.971486,-4.790627,3.088871,-8.889270,-0.883788,-0.392368,-0.263766,-9.633078,-3.725525,-2.944787,8.241791,6.570105,7.755822,-7.683939,5.502616,0.451514,-6.835272,1.920183,1.103972,-0.675791,-3.428165,-0.235662,-1.341403,-2.573769,-4.839103,5.622770,-1.464904,3.372336,6.800811,4.293015,5.914611,-8.062275,-0.443051,9.322175,-9.744825,9.240326,9.466061,8.540856,-8.247827,-5.634737,6.713051,-4.250022,0.617011,7.611978,-4.364728,7.559198,-8.218487,2.345001,0.944598,-9.613219,-7.909999,-8.249523,-8.524192,4.875037,4.188234,9.156297,2.766906,-1.456773,1.616729,1.014032,-1.919678,9.887780,3.907464,9.861672,-5.394502,-8.375140,6.765707,-8.632008,-1.472068,4.326225,5.140089,-0.300409,-4.165386,3.913914,5.596086,4.428873,5.015793,-1.176727,-7.075209,7.732883,8.508585,4.970301,-1.156442,-2.798854,-1.244343,7.456890,-6.642891,-8.906627,-1.680729,-7.079292,4.670195,-5.941870,7.032175,7.161491,-3.169802,-4.580324,-0.234177,7.078225,3.237924,6.816683,6.046842,8.680684,3.897948,-1.957717,-7.440013,2.683844,3.147703,-6.167081,-7.939573,-7.798868,7.615404,-4.389674,-8.324710,-4.284207,-9.580803,5.620446,-2.988818,9.509056,0.756577,-3.802648,9.538075,8.896361,2.058713,2.348639,8.065107,-6.158785,-8.299085,-8.999792,-7.135347,-4.682675,-6.436173,-2.345694,-4.925815,-0.079955,-5.962113,8.167819,-6.769427,-0.102898,0.125185,1.137917,1.661009,6.438674,7.262219,-2.231490,-1.702551,-4.208390,9.852006,-1.293182,-3.682179], dtype = "float32")#candidate|4842|(156,)|const|float32
call_4840 = relay.TupleGetItem(func_2560_call(relay.reshape(var_4841.astype('float32'), [15, 10, 5]), relay.reshape(const_4842.astype('float32'), [156,]), ), 0)
call_4843 = relay.TupleGetItem(func_2564_call(relay.reshape(var_4841.astype('float32'), [15, 10, 5]), relay.reshape(const_4842.astype('float32'), [156,]), ), 0)
func_632_call = mod.get_global_var('func_632')
func_635_call = mutated_mod.get_global_var('func_635')
const_4854 = relay.const([[4,6,-2,4,2,-5,-2,-6,-8,4,-3,7,2,-5,9,-4,1,-1,-9,-1,10,9,-10,7,-1,5,10,10,-3,9,-2,-7,3,8,-4,4,6,6,-8,2,-3,-5,-1,5,2],[8,-6,-7,-4,2,-3,-9,-10,4,7,-9,-5,5,1,-1,-3,7,3,-2,-10,-2,1,-3,-8,10,3,10,-6,-5,5,10,-5,1,2,5,-8,-4,-10,-3,-3,8,4,5,2,-9],[-8,-7,7,-10,-1,-10,2,1,10,-10,7,-1,5,3,10,6,-8,-8,1,3,-3,-3,6,4,-8,-2,-4,5,1,-9,-9,-6,10,-1,3,2,-8,8,-1,-3,1,-3,8,-6,-8],[-9,-4,4,-10,2,1,-1,1,5,4,-10,-1,1,2,8,6,7,-4,-1,-7,10,-9,9,10,1,-1,-10,5,-4,1,-7,3,5,6,-2,1,5,2,-1,9,10,-4,-6,2,-3],[4,-9,5,-4,4,-8,-9,6,-6,-6,10,8,-6,10,-4,2,7,7,-7,-5,-9,5,-5,-9,-7,-9,-3,-10,9,9,-5,3,4,3,1,2,2,-7,-8,1,5,2,-5,9,2],[-9,-10,-10,2,-4,3,4,3,6,10,-9,-5,3,3,6,-9,-6,-7,3,-10,-6,-3,2,-2,7,4,-8,-7,9,-4,-9,9,-4,-4,8,4,-8,-4,2,9,-9,7,3,10,-8],[-8,7,-4,6,6,1,9,6,2,-1,-1,-7,10,6,2,4,3,-9,-2,7,2,9,-1,-7,7,7,10,10,-2,2,2,-7,-9,4,-5,1,-2,9,7,8,5,4,7,-9,-10],[-6,7,7,-10,-7,-3,2,-1,1,-10,2,6,3,9,4,-3,2,-6,7,-10,-2,-5,2,-7,3,-4,3,2,3,7,3,-2,9,-3,-3,-3,8,9,-5,3,-4,-5,-6,2,-10],[-9,-9,9,-8,-6,-7,-5,-8,-5,1,-1,6,3,-2,-1,5,7,-2,4,3,10,1,-7,2,-2,-1,-9,6,8,6,-10,3,5,-8,-5,8,-2,-3,-8,10,-7,10,9,5,-5],[1,1,5,-9,-4,-5,-2,-1,-4,7,8,9,9,5,-9,4,-6,-6,-3,-5,1,-9,-4,7,9,6,-9,5,-4,1,-1,-3,-2,-7,4,-1,-1,-10,-1,7,-3,7,-7,-2,-5]], dtype = "int64")#candidate|4854|(10, 45)|const|int64
var_4855 = relay.var("var_4855", dtype = "int16", shape = (48,))#candidate|4855|(48,)|var|int16
call_4853 = relay.TupleGetItem(func_632_call(relay.reshape(const_4854.astype('int64'), [15, 3, 10]), relay.reshape(var_4855.astype('int16'), [24, 2]), ), 2)
call_4856 = relay.TupleGetItem(func_635_call(relay.reshape(const_4854.astype('int64'), [15, 3, 10]), relay.reshape(var_4855.astype('int16'), [24, 2]), ), 2)
var_4865 = relay.var("var_4865", dtype = "bool", shape = (10, 4, 6))#candidate|4865|(10, 4, 6)|var|bool
bop_4866 = relay.greater_equal(bop_4832.astype('bool'), relay.reshape(var_4865.astype('bool'), relay.shape_of(bop_4832))) # shape=(10, 4, 6)
uop_4869 = relay.sinh(bop_4837.astype('float32')) # shape=(10, 4, 6)
bop_4874 = relay.subtract(uop_4869.astype('float64'), relay.reshape(bop_4832.astype('float64'), relay.shape_of(uop_4869))) # shape=(10, 4, 6)
output = relay.Tuple([call_4840,var_4841,const_4842,call_4853,const_4854,var_4855,bop_4866,bop_4874,])
output2 = relay.Tuple([call_4843,var_4841,const_4842,call_4856,const_4854,var_4855,bop_4866,bop_4874,])
func_4877 = relay.Function([var_4830,var_4831,var_4841,var_4855,var_4865,], output)
mod['func_4877'] = func_4877
mod = relay.transform.InferType()(mod)
mutated_mod['func_4877'] = func_4877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4877_call = mutated_mod.get_global_var('func_4877')
var_4879 = relay.var("var_4879", dtype = "bool", shape = (10, 4, 6))#candidate|4879|(10, 4, 6)|var|bool
var_4880 = relay.var("var_4880", dtype = "bool", shape = (10, 4, 6))#candidate|4880|(10, 4, 6)|var|bool
var_4881 = relay.var("var_4881", dtype = "float32", shape = (50, 15))#candidate|4881|(50, 15)|var|float32
var_4882 = relay.var("var_4882", dtype = "int16", shape = (48,))#candidate|4882|(48,)|var|int16
var_4883 = relay.var("var_4883", dtype = "bool", shape = (10, 4, 6))#candidate|4883|(10, 4, 6)|var|bool
call_4878 = func_4877_call(var_4879,var_4880,var_4881,var_4882,var_4883,)
output = call_4878
func_4884 = relay.Function([var_4879,var_4880,var_4881,var_4882,var_4883,], output)
mutated_mod['func_4884'] = func_4884
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4987 = relay.var("var_4987", dtype = "float32", shape = ())#candidate|4987|()|var|float32
const_4988 = relay.const([[[9.167849,5.513551,-9.497578,-9.690896,2.200894,-5.002153,-3.472413,0.007083,-6.446260,-0.167303,-3.253245,-5.906183,3.936083,-7.007965,3.893009],[2.985283,-9.377657,1.405519,-1.720784,1.964889,7.560267,-2.828431,-5.396924,-5.642528,6.501137,5.282075,-1.166673,5.546837,9.042630,-5.948912],[6.241047,3.539175,-2.924300,-3.592206,-8.044413,-0.052811,9.116713,8.633813,9.786781,-6.993884,-7.894899,-9.678288,8.418041,-9.064465,2.068155],[3.443099,1.373206,7.557421,-5.116413,-1.728924,5.795718,-9.045453,-9.210235,-9.752218,-1.408346,-6.255322,-9.305296,1.528383,-8.597792,-4.105629],[-5.042747,-5.927997,-2.576366,3.623904,8.220363,1.690375,-4.432435,-6.282417,4.593829,-2.686771,8.449173,-0.622103,-8.318788,-7.530727,-7.652931],[-9.849107,-6.638962,-2.469239,-1.901598,8.434076,8.745883,-4.158440,8.654403,-9.344310,6.316620,-8.358006,6.577337,9.705329,-9.537493,-5.443874],[-5.011093,4.114046,5.077222,-2.481959,6.582801,-3.862373,-1.345180,-1.521563,3.607497,3.326585,-7.562683,8.390922,-7.975619,6.117572,-2.985069],[7.569783,-1.491188,-0.925652,-8.190833,-0.388618,-4.451794,8.201144,3.874891,-2.499511,-4.508501,-5.974234,3.202316,0.177412,-2.152479,-6.734077],[-7.334942,1.715269,-6.722295,0.864189,-0.577234,-8.961619,-1.555974,-7.939994,-6.524994,-5.655115,-8.947050,1.503372,-4.327584,1.482265,5.267109],[-9.232391,-9.582477,-8.517992,8.313748,1.616429,7.690254,-2.494784,4.087402,-3.181319,-4.443955,5.129982,9.029675,-5.076048,8.205752,-1.075764],[-0.178416,-1.425738,-4.195702,4.032166,-6.083874,-8.286156,7.565515,9.354666,0.135895,-3.414434,-0.681444,-0.369681,-2.575925,-0.928365,-3.381270],[-2.403088,3.865350,4.700460,1.747903,0.396086,-7.545671,-3.083108,-4.731089,-3.314809,6.913011,4.713758,-2.130730,7.656166,4.047718,-8.302323],[-4.677605,-7.079027,-2.178609,7.179016,-5.592561,5.701497,-2.450588,-7.697541,-1.360257,-2.323830,9.382175,3.377136,0.195099,-8.416858,-9.343686],[0.004658,1.952839,-1.170617,7.705479,-7.855640,-8.989398,-3.281320,1.907591,-1.955406,-0.013011,3.734033,-4.869960,0.179442,1.624413,-6.756040]],[[2.514716,-6.661230,2.173655,-4.484917,-0.786274,1.766605,-7.743164,-6.584989,-1.614214,3.268196,1.346355,5.673439,-2.120754,-7.605374,-9.239579],[4.489644,-7.500068,3.861536,7.782257,-8.542349,-1.843981,-1.627356,-9.104178,-7.296002,3.073709,9.531130,-5.382277,0.609028,5.602291,-4.548203],[-8.748339,8.186156,7.014606,6.119179,-7.358499,-3.937104,0.688338,-8.819477,7.487041,-9.102130,-3.800134,-9.741201,-4.459557,1.865127,6.067620],[-9.745549,-2.545828,-7.112241,-2.043200,-1.568453,4.520642,0.861757,8.451910,-1.530595,-5.858467,-6.092948,-2.460421,7.645074,-7.829851,3.430673],[-1.169368,1.072960,7.516791,-0.474101,3.450215,9.292674,4.674146,9.592545,-5.071620,-2.762241,6.731147,5.075581,0.194254,-3.924033,-0.939852],[5.830530,9.766898,9.828270,-3.203098,-9.361936,-4.454565,-0.719891,-5.756244,-8.803337,-2.528043,0.524861,0.374553,6.272936,7.671628,-9.271017],[8.108106,-6.725118,1.697743,-9.753966,4.968032,2.268169,-4.780657,-3.275799,-7.336556,4.800641,0.952534,-4.209124,7.335107,1.822104,4.712635],[-7.501786,8.449558,-0.354865,-7.621443,-9.373106,2.998241,0.354531,0.941339,9.312004,7.518418,-5.381457,2.849107,4.702807,6.281245,-1.358725],[8.711550,1.795538,9.634820,9.825723,-6.899713,-5.108005,9.174062,6.992135,5.891094,-3.763172,9.304522,5.157814,8.054438,-1.515166,0.131234],[-9.684669,5.318455,9.775205,1.345154,1.213039,-3.105024,3.982824,4.761477,-2.027515,3.981890,9.064429,-4.272494,-3.244751,-9.027985,-6.851897],[5.931706,-6.164304,-2.673965,0.864686,-8.348669,-6.350630,-4.956260,-6.115431,-2.784497,-6.373353,-7.725920,0.801648,-3.628897,-9.596628,-4.936184],[-1.290478,6.675152,-1.878369,-0.039574,9.770879,-7.229025,0.088908,-9.294625,2.589802,5.125598,-8.776006,6.885958,-3.455804,2.110934,-3.490357],[0.202102,0.710867,2.212808,-4.552953,-7.280372,-9.646481,5.063317,9.794224,-5.314661,2.361296,5.648298,9.665174,7.959551,-2.337188,-6.030685],[-5.186293,-7.698336,1.962266,6.872076,6.774182,9.534870,3.180714,-7.043380,-7.693586,0.202240,-0.409338,-3.420347,9.978442,8.254441,-1.682228]],[[9.037929,0.440152,1.438158,3.350375,-1.059850,-3.742231,1.631892,2.331544,-0.333333,-2.614492,1.737389,-8.367275,-5.777810,0.544872,-9.389727],[6.188609,-6.572001,4.548991,5.305140,-8.665513,2.040458,-6.839057,-9.078799,-3.839113,7.593925,-3.524534,0.745846,-2.151823,9.627780,5.787824],[-2.491335,5.305876,4.460900,-5.288736,6.504546,0.301121,7.467947,7.232367,5.653699,-9.376520,-5.153771,7.542486,-3.285257,3.246398,4.689902],[0.786244,-9.016598,-6.098736,7.346855,-8.965105,1.721845,7.835450,6.106499,7.561379,4.265623,-2.418764,-4.773652,0.661044,4.886004,-8.728698],[-6.999932,-2.661609,-7.213976,-0.918503,8.082752,2.676369,-8.229478,3.727828,8.478764,-0.749338,0.300475,5.085948,-8.496186,-5.632483,7.005734],[-5.890827,-0.688160,-8.648360,6.813936,-0.308895,-4.726064,-9.642338,-6.168858,-2.370844,-0.293019,-1.555245,4.996972,8.163942,8.240940,-5.007244],[8.027587,-0.983293,2.355026,-6.123842,2.923330,-6.404819,-1.816309,6.607286,-4.478852,3.756832,-2.956093,-5.295752,6.139410,-6.063218,8.459999],[0.784907,3.450741,-9.606571,4.133681,-1.810625,4.091820,-4.118233,2.694229,4.399426,4.773546,-4.657084,-2.837661,-1.106580,-4.204180,-4.251783],[3.179650,-2.671099,2.843046,9.838504,-2.299267,-3.360786,-4.429073,0.603487,-6.380438,-7.046514,2.657281,7.647477,9.998649,0.126783,-9.302079],[-9.928320,-4.304917,7.383170,1.811096,-1.666257,-0.152846,-9.501814,8.024263,-3.502276,-0.947193,7.968696,2.324138,5.072407,-8.959766,-9.666681],[8.623551,-2.761253,-3.136110,9.163708,4.393989,8.312222,-3.894805,-1.503265,1.368436,5.737882,4.104606,-7.079208,-4.727344,-8.159682,-8.944221],[1.170400,9.671514,2.148581,8.240684,1.871944,-7.454792,-0.569243,-4.981183,-3.968591,1.343565,9.328899,4.481965,8.553905,-4.281741,-1.347312],[8.072359,-5.119525,-6.392134,-1.035618,-7.513420,-2.437653,-8.927874,-4.613074,2.781010,-9.707319,-5.270870,-5.145073,2.479933,0.823120,3.115014],[1.031956,-0.075725,5.292604,6.017908,-2.545923,8.218294,0.345300,-9.003924,3.380696,-6.292069,-2.841649,8.322986,-3.703890,7.180043,-4.460855]],[[-0.591087,0.515328,0.712542,0.259191,-1.199064,9.592225,-6.278540,6.931320,-3.243858,-2.643384,-1.923368,2.893939,5.288581,7.465722,-7.758110],[2.356546,0.122927,4.700352,0.596916,8.932533,-6.833017,-7.787577,0.566731,1.789137,-2.811902,4.661634,0.115910,-8.461117,-5.361094,9.970797],[-8.785892,1.103364,9.217100,-5.400128,7.433801,-6.551702,-7.826569,-6.304692,-4.925331,9.980367,-7.824173,3.417587,-4.143300,-3.669203,9.528694],[6.967792,5.952467,9.132600,7.983838,3.874235,-2.019827,-8.368026,-8.731840,-2.760303,5.668623,7.465078,-8.571591,0.090145,3.392897,-6.330578],[3.035028,-6.839936,-1.569039,9.255288,3.571548,8.724461,-4.166148,4.276730,-0.862100,1.211896,6.847063,6.953365,2.461553,-9.535807,2.672285],[-4.259625,-2.382256,6.110771,-8.482682,-7.936798,4.733079,1.785857,-6.376160,4.217260,7.576075,-1.926099,0.767658,-0.157594,-8.836624,2.221563],[6.857407,-6.306121,-0.895030,1.382801,-6.275385,7.805709,6.309521,7.797365,5.246972,-0.587085,5.195546,9.267338,0.650148,7.802608,0.703207],[9.979304,-1.102964,-1.330105,2.002576,-9.105506,-9.129541,0.836356,-5.097409,2.816024,0.915664,-8.097582,-8.902517,-2.418502,-7.728856,5.440627],[-2.785712,-2.926285,-2.243109,-9.154446,-5.491750,1.422320,-9.693113,-3.457090,2.645209,-3.205769,-7.107308,6.872150,-3.111674,-3.492492,6.310759],[-5.450955,-8.669811,9.427987,-2.358797,-8.237858,-6.393858,0.819346,-7.313449,7.238126,1.593554,3.070205,1.200415,-6.215163,-5.767372,-7.881674],[-5.807968,8.187393,6.338162,0.277917,-0.435917,4.312785,3.373016,7.393709,-9.553151,7.167517,-2.866001,7.682225,4.319337,-2.942608,-1.855086],[4.321941,6.751635,7.073588,8.488242,-4.965976,-7.806093,-8.199982,-1.745311,-4.690498,6.800002,-2.654980,-5.043601,1.039242,1.847312,5.915484],[-0.615863,-5.529794,2.551288,-4.652417,-8.278324,8.914518,-5.956361,-4.074866,3.422097,-6.846368,-2.721724,4.637966,-1.378205,-5.127618,-6.621559],[-7.798733,7.534484,-6.161787,-9.500520,9.368783,-6.372989,-9.392252,9.567592,1.151885,5.839198,0.514052,6.641869,-1.505261,9.119223,0.490377]],[[-9.355890,-2.182909,5.225539,-8.920794,3.322263,-9.139120,-8.967880,7.184470,-7.735375,7.466424,-7.038726,6.009660,7.271179,0.152559,7.085369],[-9.490921,-6.001362,9.181616,4.729353,-5.047001,3.315196,-9.771006,0.019479,3.734418,7.943845,1.443624,0.324250,8.811977,-7.829995,0.511186],[1.792592,9.669659,-2.172121,2.011299,-5.831809,5.994195,7.846917,-8.070921,8.533618,-4.086484,-3.160035,-7.164062,-2.201014,-5.496132,-5.221860],[-3.109654,1.522536,-7.047676,-7.668663,9.085444,5.273868,5.289345,8.094366,5.209100,9.597445,5.933336,1.054122,-9.321224,3.766160,-1.769379],[-0.685503,3.054592,-5.267461,-6.926644,-4.552393,7.938164,-3.465426,-5.143893,-2.327224,-6.844367,6.394841,3.862213,4.294026,-7.235721,-7.905068],[-5.134600,-2.841391,-8.098778,9.850097,8.467886,1.856745,9.915363,1.788192,8.780541,6.811618,-5.731290,0.979675,8.983107,0.228100,8.357520],[-1.675587,-6.001759,7.014833,9.909140,9.116167,-7.668312,-4.561746,-0.628943,2.227863,6.957996,2.889688,0.790792,-5.291486,6.311726,0.693988],[4.794173,2.882993,-9.873583,8.876096,0.698282,-8.601323,3.444311,-9.376359,7.700188,5.569665,-2.291995,-1.844691,5.315459,9.181069,-4.865360],[2.932688,-1.897794,5.874301,5.016447,9.638210,-6.667345,9.090286,-9.906809,3.838921,9.498028,-4.929494,-5.251500,-8.841218,8.394699,-2.358166],[-2.092886,-8.156400,-4.501579,1.187676,-7.339234,3.449063,-4.249909,-4.520619,-8.201042,-4.478886,-8.402391,2.674148,9.765216,-4.943431,6.034384],[-8.805314,-2.393225,8.954326,7.247874,-3.039815,7.311615,-2.524782,-1.046907,-0.444232,-8.441382,1.866843,0.388642,3.366513,-2.402069,-5.059201],[3.870493,8.248882,2.073153,-3.909246,1.745975,-0.037387,-3.486395,-3.554425,5.820101,1.391415,-9.526811,-9.414839,-3.347819,-1.438262,8.629388],[-6.358539,-2.626435,-0.918065,-1.555722,-6.156213,8.685779,-9.432808,8.841680,4.249990,6.160315,-2.847247,1.172378,-3.210200,9.175606,-6.884682],[2.075963,0.251178,-5.561745,1.089210,-3.274532,-4.597771,-4.446939,-0.616034,5.257300,-4.767537,-9.368145,-6.149906,4.248314,4.154701,-9.722514]],[[9.769287,5.229578,9.370385,-1.648514,-9.892603,-9.080200,-6.120808,-7.520796,-8.141440,-8.820030,-1.713578,3.539248,-7.398656,0.486807,0.524955],[7.571839,9.682550,3.287387,-5.205564,9.578914,6.254564,0.556226,-2.761304,-1.963499,-0.709917,8.463086,3.516505,2.118067,5.826198,-7.075884],[-5.743112,1.243095,-1.153921,-3.858653,-6.306765,1.595870,2.177156,-9.307228,-9.938647,-3.487643,6.902794,-3.067029,2.526467,5.969311,-6.197208],[7.229461,9.055105,1.953707,-1.041841,6.019339,6.945837,-6.814467,7.881455,1.851293,0.937940,-7.909373,1.435923,9.518807,3.878124,-1.237827],[-8.091030,-6.513427,-9.791820,8.487796,-3.216904,-3.000121,-3.490823,-1.276284,9.433310,9.323433,-3.526903,1.871019,-8.820079,-2.662744,2.668839],[-2.779738,-2.795166,-5.381683,-3.464033,5.905513,-6.601024,-1.694248,-6.512614,-5.997924,-9.311718,-4.178626,-1.925064,2.008955,0.117954,-8.168691],[-2.698879,-1.848910,4.357642,0.109477,9.708305,-9.080626,-0.403768,-1.339793,-9.143405,-2.491600,-8.363742,6.837029,5.764325,-6.130795,-4.783241],[2.269790,1.119061,7.033627,-6.277446,-7.405480,-3.654576,7.054698,9.806744,8.215517,8.330324,4.184528,7.817409,-7.529910,2.811915,5.254744],[3.588455,-9.463604,-6.863056,9.027674,-1.717726,-9.860902,9.609164,-7.666816,5.567926,-1.863330,6.464263,7.743553,-2.918847,3.823288,-5.690750],[1.448705,-3.530742,-8.748515,7.759689,7.815991,8.343952,-1.683998,-8.147285,6.849966,6.679431,-7.533653,6.414415,2.956453,3.882485,3.195087],[9.948933,1.119496,-0.433857,-9.606486,5.853790,-2.365346,-7.838268,1.746926,7.855375,-7.985842,-6.852598,6.472970,-2.743117,1.736301,-1.779588],[5.850367,8.105626,9.611376,-1.077625,-2.288665,0.638906,-8.449698,5.684975,-5.788581,1.767144,9.236706,3.181522,5.087877,9.809594,3.669606],[-6.179630,4.244998,3.882987,7.075721,6.385851,-0.036281,-9.276476,-9.721699,-1.102523,-2.633248,9.769178,-8.478555,0.862931,6.760427,-7.895977],[-4.181210,5.918375,4.446047,-8.431423,5.952062,-8.291089,-7.203329,-3.646025,-2.632347,-0.070530,-3.403719,6.868660,-8.854691,8.759471,6.571171]],[[5.794722,-9.404234,-2.741945,8.501028,-2.724797,-3.450493,-5.033024,-6.119670,3.026904,-7.716415,9.035111,0.242613,2.924168,9.898291,7.833775],[-0.799933,-4.273044,-5.364569,-3.446274,1.155811,-3.232018,6.249229,2.895867,9.985488,3.385326,-6.974042,7.594755,5.951942,6.417698,5.204420],[2.985052,2.621645,-0.507620,-4.438470,-5.930302,7.806570,5.340112,4.750335,-0.158789,1.363486,-4.853874,4.219433,-2.648346,-7.372527,2.025286],[-3.406603,-7.607101,1.375811,4.672805,0.235276,9.848709,-1.155580,-7.873310,6.996889,0.323982,-3.906623,-4.656508,5.349508,-2.330096,6.671767],[1.527514,-9.121519,5.872959,-8.638238,-9.719117,-9.466823,-6.213327,-1.285646,7.975135,-9.286560,6.412888,-6.617563,-0.409055,-5.128700,-1.515772],[-9.774730,5.784816,4.506137,-4.570349,-3.528032,9.444027,8.655395,7.866391,-6.994384,7.922097,3.838678,0.073839,7.132745,4.119165,-5.775039],[8.302942,5.731282,-4.582743,2.415251,-2.110378,4.897049,1.573896,-6.339567,-7.254959,7.004418,8.229521,-1.788103,-6.229421,-1.397993,7.937722],[8.813115,2.903647,-4.639993,4.600286,8.263261,0.072954,-2.828225,8.318223,6.439529,8.707652,8.071532,-2.385912,-7.110884,2.478541,-9.138709],[4.274629,4.537900,1.073785,-7.802861,-2.460335,-0.856957,-6.033976,-9.668371,9.832168,-5.239642,-0.517196,1.772685,2.382313,2.763925,-7.270432],[-0.957755,-2.964767,1.359112,8.249913,-6.719866,5.452146,8.578102,8.147383,2.367841,1.280510,-7.785342,2.255516,-0.336724,0.140253,-9.293979],[-6.015452,8.150859,-2.911113,-4.106586,2.298244,0.861162,4.428465,-3.656523,-4.192192,-3.183682,4.821391,4.281262,-6.670570,-6.746737,-4.156948],[-6.895885,8.498227,1.778439,-2.641008,5.835323,-6.264776,-9.977707,5.793592,0.705573,-7.296999,9.380274,-1.329564,-4.555272,7.851273,-3.053846],[2.521503,-8.785919,-5.028620,4.113144,7.793589,-4.218007,8.951419,7.793265,-0.828286,5.008487,-5.653224,-3.126270,8.248784,-5.399189,8.930011],[-2.601583,9.441528,3.773916,-3.198564,-2.150780,6.271351,-9.825211,0.129917,9.332996,-2.843265,-0.126569,-8.024647,6.891279,5.085579,-1.139241]]], dtype = "float32")#candidate|4988|(7, 14, 15)|const|float32
bop_4989 = relay.floor_mod(var_4987.astype('float32'), const_4988.astype('float32')) # shape=(7, 14, 15)
func_3720_call = mod.get_global_var('func_3720')
func_3723_call = mutated_mod.get_global_var('func_3723')
const_5000 = relay.const([[3,10,4,-6,-3,-4,9,-3,-6,10,-6,4,5,-2,4,-10,7,-6,8,-9,-8,-9,-2,1,-3,-7,2,-10,3,-1,7,4,1,-6,-4,10,-1,-1,3,1,3,-7,-1,-1,3,9,-3,-6,3,-5,-9,8,-4,-3,1,7,1,-8,-2,-7,10,5,-9,8,-4,-10,8,3,9,2,-7,3,-2,-10,-1,-9,3,4,4,-5,-7,-1,4,-6,7,4,-7,-2,9,3,-1,1,-6,-5,7,9,8,8,4,-7,-3,5,-10,-9,10,-9,4,-4,-6,-1,10,8,1,-2,-1,-6,-9,-4,-9,-8,-9,-2,8,3,7,-7,-5,-7,-1,1,-7,6,-9,5,-7,9,-1,-9,6,-2,-8,-2,-6,-1,-7,8,-1,-1,9,8,-10,-2,-7,9,4,6,2,7,6,-4,-10,8,9,2,5,1,-5,8,3,5,9,-9,1,7,-4,2,-3,5,-8,-9,-5,2,-5,-3,-6,-6,-10,-5,3,-10,-5,10,1,-2,-2,-5,3,-10,6,9,-10,8,-1,2,-9,8,-5,3,-6,8,-10,-7,-10,3,10,9,-4,1,4,-9,8,-8,-8,2,10,3,2,-2,7,-10,5,9,10,7,5,-6,5,-9,-7,-8,8,-6,1,7,-1,-7,10,-8,-5,-4,-4,5,-6,-2,-5,9,-2,-6,-3,1,1,2,3,10,8,-8,6,-2,8,-7,-6,6,3,1,6,2,9,7,-6,7,2,-6,1,-3,2,1,10,6,-3,9,-6,-7,5,-6,-2,6,-10,-4,-8,1,-9,-8,4,-2,10,6,-2,-2,6,9,2,-4,8,7,-7,8,3,-6,-1,-1,10,8,10,-3,7,-4,9,-5,-6,-5,-1,8,10,-8,-2,3,-8,-8,-10,-5,-4,7,-7,-10,-5,5,-7,-7,-6,-9,7,4,2,6,-2,-8,1,2,2,-10,-7,2,-7,1,5,4,2,9,-10,6,3,-10,1,-2,-4,-9,-7,-4,-1,10,7,-10,-3,-2,2,-5,-4,-1,7,-10,-6,-1,-2,-9,-10,-9,-4,5,-7,-10,-7,-4,-2,-5,-8,1,4,1,6,8,-1,-4,-7,-2,-10,-1,-1,-7,2,3,7,-6,-7,8,6,-3,5,4,8,4,10,4,-2,6,3,4,5,-2,6,10,-7,3,-10,-4,4,-6,-3,8,1,9,-3,-3,-2,3,-6,4,-7,7,-3,-6,9,9,-4,9,-1,7,-9,2,-9,1,-9,-1,1,4,9,9,3,1,-7,3,9,9,4,1,-8,9,7,-6,7,2,-1,5,-9,3,9,1,8,7,-3,5,1,1,-3,-8,-4,-8,1,10,2,-5,9,-8,-8,-1,3,2,-10,-6,9,-3,6,9,5,-7,-3,5,-8,1,9,-9,-5,-8,6,-8,-8,8,-2,-1,-6,-1,9,-1,10,5,3,2,4,5,-2,5,-3,5,-1,2,3,8,-1,2,-2,-3,-10,-5,4,6,-2,-9,-3,-2,-1,4,10,-9,-3,-6,-8,10,-3,4,-4,7,-3,-2,-1,3,-9,-5,8,-1,4,6,6,2,10,1,8,9,-4,-8,-5,6,-7,-4,6,-8,3,-2,9,-8,-2,2,-7,-3,-1,-8,3,10,-7,-7,-10,-5,8,-1,1,-5,-10,-5,7,8,9,4,-1,4,-1,-3,5,-3,5,-9,5,1,2,-2,6,-8,-5,-8,1,6,-10,-2,-7,9,10,8,3,-1,-7,-7,3,9,2,-6,-7,4,1,4,4,10,1,-1,9,-3,-5,1,-6,7,8,-10,6,-4,-9,-5,-2,-8,4,9,-1,2,-3,-3,-5,-6,4,10,9,8,-2,2,7,7,9,-5,-10,-4,1,-5,-8,1,-8,-3,-5,-6,4,-9,10,-4,-5,7,9,-10,1,-9,6,-4,-1,3,7,-10,-7,-4,6,6,-1,9,-6,-10,-4,-9,-9,7,9,-7,-9,-9,-8,5,-5,7,6,5,5,-1,4,-1,5,6,-8,-10,10,5,-4,-3,-1,-4,4,-1,5,-8,-3,6,9,-2,5,-5,-3,2,-1,10,-5,1,4,-10,5,1,-9,6,9,4,-1,-8,9,6,4,2,-10,1,-6,-4,9,8,4,-7,-3,-6,1,-1,-3,10,4,-7,6,8,-8,-10,-2,6,-2,7,-5,-10,-9,7,-9,-1,1,-7,7,1,-2,4,-1,7,5,-9,-1,9,1,1,-4,-6,2,4,-1,-5,-7,-6,-1,-2,-1,9,1,1,3,-5,-6,-2,4,-8,-10,-9,-3,-3,-10,-3,5,4,-9,9,8,-8,3,-3,-3,-2,-5,10,-6,4,-8,-8,8,-9,8,8,-2,-10,-4,3,-7,2,6,10,5,-9,-1,-5,10,6,4,3,10,-2,-10,6,10,9,-10,-9,5,7,6,4,10,5,6,1,-3,4,7,-3,6,4,-3,10,-2,3,-10,5,9,-1,8,-2,-4,6,-6,2,-3,7,-1,3,3,1,-4,-1,-4,9,6,-5,-8,4,2,-6,-2,8,-10,-7,8,6,4,-5,2,2,-5,-8,8,7,-10,4,5,-5,4,8,10,3,3,-2,-4,-3,-1,-4,-5,-8,5,6,3,-5,-3,-10,8,9,-3,-6,-5,-10,2,-7,6,-3,-7,-10,-2,9,9,10,-3,1,-2,-7,-10,5,-2,10,-8,-8,3,7,-5,3,-6,-3,4,6,-5,-2,1,-6,10,10,10,-6,6,-6,-10,6,2,6,7,1,-7,6,2,9,-1,-1,7,-2,1,-5,-9,-10,2,8,-9,1,3,4,-1,-7,-3,3,-6,-4,-5,9,-2,6,4,-1,-4,-9,-10,-10,7,5,-6,10,3,10,-3,-3,-5,-8,4,1,4,5,-4,-6,4,9,-10,-1,-2,-1,9,1,3,-4,9,-5,7,6,6,-10,-3,-8,1,6,-2,10,8,-5,9,8,-5,10,2,1,9,-6,-4,7,-6,9,-9,9,-8,-8,2,-6,10,8,1,-10,3,-5,4,2,-5,10,-8,1,3,-5,-7,1,7,9,-1,10,-9,-2,-7,3,-5,-5,-1,-3,6,-9,-8,-10,2,-3,-10,-10,8,-2,-8,6,-9,8,-5,-4,8,-4,4,9,5,2,5,-4,3,7,-2,-7,-1,-9,-6,9,-6,8,9,9,-9,9,2,6,-1,9,5,-2,-10,5,6,10,7,4,-7,-9,-4,2,-4,-3,1,-8,-9,3,3,-7,-3,1,-7,7,-7,-4,-5,-7,5,3,6,-4,-2,-6,6,6,-2,-9,-1,7,-3,9,5,8,-9,-10,2,10,3,-1,-3,8,3,6,-6,-5,2,-8,1,-9,-6,-5,-4,-6,-5,6,3,3,3,-3,-4,9,-2,5,4,-6,-4,3,-8,-3,-4,-10,4,7,5,-8,8,-5,6,-8,3,-3,6,4,-2,8,-9,7,2,-3,-3,7,10,-6,1,9,9,-10,-5,-1,-5,-5,5,-6,-5,7,-9,1,-4,8,-2,-9,6,-8,-6,-1,5,-3,-7,1,-9,-2,-1,-10,2,2,4,7,-3,-2,-3,9,-9,10,5,-10,10,-3,-6,7,10,6,-3,3,-9,4,-9,9,9,-6,3,-7,9,-3,4,7,-1,9,7,9,-10,-9,10,-7,-9,3,10,-2,-1,-7,7,10,-8,-4,-2,2,-10,1,9,8,2,2,1,-10,-1,7,1,-5,-6,-6,4,10,-9,3,-10,7,-2,1,-3,6,-10,-1,10,-1,-7,-7,-5,4,-10,1,7,2,-7,5,-6,5,5,8,-3,4,-6,-10,9,-4,-2,1,-2,-1,7,-2,-8,-10,4,8,9,-7,2,7,-5,4,-5,-7,9,-10,5,-1,1,-5,1,10,5,8,-9,1,-5,1,10,-1,-7,5,-4,-4,8,-8,1,9,-7,3,2,-10,-9,-1,1,7,-2,10,7,-1,-3,3,8,2,-1,-3,-1,3,6,-10,-5,-4,9,5,8,-2,4,7,-1,7,-5,6,5,-7,-3,-9,4,-7,7,-1,-7,-6,-10,3,1,3,4,4,-1,2,10,2,7,8,-1,-9,-4,9,9,7,-6,7,-2,-9,2,6,-5,7,-10,-5,4,9,-8,-3,-10,6,1,-6,-4,7,-8,-9,3,-4,1,-4,-3,6,-1,8,-9,9,-8,4,-10,10,-6,-1,-7,4,6,4,2,1,-8,5,3,-9,7,-5,-8,4,-5,5,-10,1,-8,5,6,-1,5,4,-10,-9,8,-5,-10,-10,-2,9,3,-7,-7,-1,8,-7,-10,1,6,10,-5,-10,-3,-1,5,-8,10,-1,10,1,-6,1,1,-7,-3,9,-3,2,-9,-3,-3,-5,8,1,10,6,-10,1,8,-6,-6,-8,6,-2,-6,-1,8,1,2,6,4,7,10,5,7,-10,6,9,-1,-9,8,6,-6,5,-1,-1,4,10,5,3,-7,-2,-4,-7,3,-2,5,-10,4,-10,-6,-9,6,-6,5,4,6,-4,-8,3,-6,6,-2,-2,-10,1,-3,8,-10,-2,-6,6,2,-2,3,-4,2,-2,-4,1,9,2,4,1,6,8,10,6,6,-4,5,7,6,4,-6,-6,6,-6,9,6,-3,-1,-10,6,-7,2,8,1,-1,-6,9,3,-9,8,8,-7,-8,-3,7,4,-2,8,-8,-6,6,-7,3,10,10,-3,-2,7,-9,10,-4,4,1,-7,-2,9,6,-3,-7,-4,3,-5,-8,-8,-5,-4,1,4,-9,2,-6,1,8,-3,-7,3,-4,8,9,8,-2,-2,2,6,8,7,10,8,-10,-4,9,10,6,-3,1,8,8,8,-7,-5,4,-9,-8,4,-9,8,6,9,-3,6,8,9,7,7,-4,8,-4,4,-5,3,-9,-10,-8,-6,5,-5,9,8,1,-9,-10,3,-4,-10,-7,1,-2,10,1,-1,9,9,1,-3,7,-9,7,-4,1,9,5,-2,2,8,-8,-2,-8,7,10,-4,-10,-7,7,9,3,5,-8,6,-9,-5,-3,5,10,1,-10,9,9,10,-7,-3,-6,8,-5,6,-9,10,10,5,7,-1,2,8,8,-9,-6,-5,1,8,10,-10,7,-2,7,-8,-5,3,1,-1,9,3,-4,-8,4,3,-2,-4,4,7,-5,-8,-3,8,-2,4,2,-9,-8,3,4,7,-10,-4,-8,6,7,-4,4,-6]], dtype = "uint8")#candidate|5000|(1, 1960)|const|uint8
call_4999 = func_3720_call(relay.reshape(const_5000.astype('uint8'), [10, 14, 14]), relay.reshape(const_5000.astype('uint8'), [10, 14, 14]), )
call_5001 = func_3720_call(relay.reshape(const_5000.astype('uint8'), [10, 14, 14]), relay.reshape(const_5000.astype('uint8'), [10, 14, 14]), )
var_5006 = relay.var("var_5006", dtype = "float32", shape = (7, 14, 15))#candidate|5006|(7, 14, 15)|var|float32
bop_5007 = relay.left_shift(bop_4989.astype('int16'), relay.reshape(var_5006.astype('int16'), relay.shape_of(bop_4989))) # shape=(7, 14, 15)
var_5011 = relay.var("var_5011", dtype = "float32", shape = (7, 14, 15))#candidate|5011|(7, 14, 15)|var|float32
bop_5012 = relay.multiply(bop_4989.astype('float32'), relay.reshape(var_5011.astype('float32'), relay.shape_of(bop_4989))) # shape=(7, 14, 15)
output = relay.Tuple([call_4999,const_5000,bop_5007,bop_5012,])
output2 = relay.Tuple([call_5001,const_5000,bop_5007,bop_5012,])
func_5016 = relay.Function([var_4987,var_5006,var_5011,], output)
mod['func_5016'] = func_5016
mod = relay.transform.InferType()(mod)
var_5017 = relay.var("var_5017", dtype = "float32", shape = ())#candidate|5017|()|var|float32
var_5018 = relay.var("var_5018", dtype = "float32", shape = (7, 14, 15))#candidate|5018|(7, 14, 15)|var|float32
var_5019 = relay.var("var_5019", dtype = "float32", shape = (7, 14, 15))#candidate|5019|(7, 14, 15)|var|float32
output = func_5016(var_5017,var_5018,var_5019,)
func_5020 = relay.Function([var_5017,var_5018,var_5019,], output)
mutated_mod['func_5020'] = func_5020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5677 = relay.var("var_5677", dtype = "float64", shape = ())#candidate|5677|()|var|float64
var_5678 = relay.var("var_5678", dtype = "float64", shape = (7, 3, 11))#candidate|5678|(7, 3, 11)|var|float64
bop_5679 = relay.not_equal(var_5677.astype('bool'), var_5678.astype('bool')) # shape=(7, 3, 11)
func_3720_call = mod.get_global_var('func_3720')
func_3723_call = mutated_mod.get_global_var('func_3723')
const_5694 = relay.const([5,-3,-4,-10,4,-5,-5,-9,-9,2,-10,-1,-6,-10,-2,-6,-2,3,-7,-10,-3,7,-9,-1,-7,-10,-3,-7,-5,-3,-5,-6,-7,3,-2,-6,-10,-2,-1,9,7,6,-10,8,-9,4,1,1,9,-3,-8,7,-2,-7,2,-3,-7,9,-2,-5,-2,-5,1,1,9,-2,-3,-5,5,-9,7,-8,-1,-6,-5,-3,1,10,-3,3,-4,-9,1,-3,-5,5,-4,-10,1,-5,-6,3,-6,1,-3,3,9,-6,7,9,2,8,1,1,4,8,6,-9,-4,6,-5,9,-3,6,-4,6,3,4,-1,-3,2,-3,3,-3,-4,-6,-7,3,-8,4,6,-10,5,10,-8,9,4,-8,-5,2,1,-8,-3,-2,2,6,7,4,9,-6,-6,-9,-8,-5,-10,-4,-7,9,5,-2,7,-2,4,-6,9,2,-6,6,-7,-9,-8,-8,-5,-6,10,5,5,-4,5,-4,10,2,4,-2,-8,8,1,-2,6,-7,7,-6,1,-3,-7,-3,-2,5,-2,7,-7,8,4,6,-8,-6,5,7,-9,-2,-7,5,9,-5,8,-1,-10,7,-8,4,6,-1,2,-6,-10,9,-3,-7,8,-3,6,3,2,-8,3,-8,-1,-1,-7,-6,-5,-4,-1,3,3,-6,-2,2,1,6,-3,-4,-1,9,-1,-7,-2,-7,2,-2,5,-3,-9,1,-7,5,-1,-8,3,4,-4,2,-2,7,-8,8,-7,2,-5,7,2,-6,10,-7,1,8,-10,9,9,5,-7,3,-3,-1,8,2,9,-2,10,-5,-9,-6,5,-1,5,2,-7,5,9,-10,-3,6,-8,4,-6,-1,-2,-3,6,1,-10,-3,-9,-8,-4,7,9,-3,2,9,4,2,-8,-5,1,-6,-9,7,-7,8,3,3,7,-1,3,6,1,-5,6,-3,-6,-5,10,-4,-9,10,-8,-4,-1,5,-6,-1,-2,5,-8,3,9,-10,-4,-8,1,-4,3,3,4,7,-10,6,5,-7,2,-9,-2,2,7,6,7,6,-8,5,-8,2,1,9,-9,-10,-8,2,10,-3,-3,5,-1,-2,-10,10,9,6,-10,-5,3,10,6,3,-5,3,7,9,-8,8,-10,-8,2,9,8,3,-1,5,4,-3,4,6,-5,1,6,3,-10,4,-4,-6,-9,6,-3,-9,-10,-7,-2,8,-9,-3,10,10,-9,-2,9,7,-8,-10,-5,7,3,10,6,-3,8,-10,3,8,6,7,9,-5,-9,7,4,-9,-7,-4,-8,-8,2,5,-9,9,3,3,10,-9,3,-2,10,-5,4,-2,6,-9,9,8,-6,-5,5,-1,6,-3,-5,-7,10,-4,3,7,5,10,1,-3,-6,-8,-8,3,10,-4,-3,-2,5,7,9,9,-1,9,8,-9,-10,-3,-5,-4,-6,-9,-9,4,-6,-6,-5,10,-6,8,-1,-8,3,9,10,4,-2,-7,-4,7,-1,7,-7,-4,6,-7,-8,-5,-6,2,8,4,-8,10,-3,4,-1,-2,7,-1,7,-9,-1,-7,-1,-3,-4,8,9,8,7,7,-4,-4,4,-6,-3,3,9,1,8,8,2,-6,4,-6,-5,-6,-10,9,-8,-3,10,-5,8,9,-1,-10,3,-7,-7,5,-3,-10,-5,-9,8,4,-9,-6,-6,-5,-2,-1,8,-9,8,-8,8,6,-10,4,8,-5,8,6,-6,10,-5,-10,-8,1,-6,-9,-8,6,1,-8,-10,5,-4,-2,1,8,-3,-10,-1,7,9,-10,2,-7,-5,-9,7,3,-5,2,6,-10,2,10,-1,1,-4,7,6,-8,-8,-8,-10,-4,5,-1,-8,4,2,-3,2,3,4,3,-3,-3,-7,-3,3,2,-5,-2,5,-7,7,-8,-6,6,-10,-2,-9,1,7,5,-3,-9,-1,5,5,10,4,3,-8,9,-10,-8,-7,5,5,3,6,-10,3,2,9,-9,8,10,3,-4,10,1,3,1,-5,-7,6,-9,-5,6,1,-7,-7,6,6,-4,4,-4,-1,-4,-9,1,-10,-6,-1,9,8,-4,-2,-7,-2,5,-6,2,5,-6,-1,-2,9,-6,-2,6,-10,5,1,-10,-10,-1,-5,-4,3,7,-8,2,8,-10,2,10,-6,-6,4,-2,-3,1,-7,10,-8,3,5,5,-3,6,3,-1,-1,-6,3,1,10,-5,10,7,2,4,-5,-5,-6,-8,-8,-7,-8,-6,-10,8,-1,-9,10,-7,-7,-2,-9,-3,-9,-3,-1,-6,3,1,-8,-3,2,10,-9,-4,1,9,4,-5,4,-2,8,6,-9,-5,6,8,2,-9,8,-5,1,8,-7,-10,3,-10,9,4,-2,7,-9,-7,-2,9,-2,-6,10,10,-7,10,2,2,-5,9,5,5,-10,4,9,-1,-10,3,3,7,4,1,-7,-9,-9,-8,-4,-8,-7,6,6,8,6,-5,-5,-8,-2,-8,2,-9,-4,7,4,-2,-8,9,-8,1,6,-3,-10,3,10,9,7,-4,7,-10,-7,-1,1,-10,-5,-2,-6,-6,-6,6,-10,-9,-5,7,2,-4,-10,-3,-5,1,-3,2,6,6,7,-9,1,4,-10,-9,-10,1,-5,2,-9,-9,4,4,1,5,3,7,-1,-9,3,3,-10,3,3,5,-6,8,8,-3,1,-9,1,8,6,-3,5,10,4,-1,9,-1,-4,9,3,3,10,-8,-7,-3,6,-1,5,6,-7,6,-7,-4,-10,-5,5,-4,-1,7,1,-10,-7,-7,4,-2,2,-6,-9,-10,-3,9,-4,-4,7,2,1,-6,4,-3,-9,-9,4,-10,6,-9,6,9,-3,2,2,10,7,-4,-9,9,-1,-9,-4,8,-10,8,-5,3,-10,7,-2,-7,-3,1,-9,2,-9,-7,-1,-2,9,6,-9,-3,-7,-2,7,7,4,4,8,-5,8,-9,-4,9,-3,9,-5,2,3,8,-5,2,4,-3,3,-9,-10,1,1,9,-6,-7,-3,10,5,7,-4,1,6,-10,2,1,8,-5,-3,-3,3,9,-3,1,8,9,-7,-2,4,4,-1,-9,-9,8,-9,3,4,-9,3,-4,9,7,-4,9,-10,8,-9,10,1,4,-10,-5,10,-1,3,-8,-9,-8,-1,-4,1,-2,-9,10,10,-2,-2,-7,1,7,-3,6,-9,6,-3,-1,-2,-7,-5,3,-3,-10,-1,9,-4,6,3,-1,6,2,-10,4,-6,-5,9,8,4,-9,4,-9,-6,8,-8,-4,8,6,9,-4,-2,-7,8,3,1,8,-1,4,1,9,-10,-6,6,-10,1,-1,-4,1,4,-3,7,-10,8,6,-7,1,-5,-8,8,-8,-2,9,9,-8,-6,-8,4,-1,-6,-4,-1,10,3,-7,-6,9,7,-3,-9,-7,-4,8,-7,-10,8,-3,10,-3,1,-5,8,-6,1,-1,-2,7,-5,2,6,4,6,2,-1,1,6,1,-10,-1,6,-3,-10,4,5,-7,8,6,-9,1,3,1,6,5,9,-8,8,3,2,-5,-3,-10,6,-6,2,4,-9,-5,9,2,-6,10,10,3,-1,8,1,-7,-2,3,-10,9,3,4,-4,7,7,-7,3,8,8,-9,6,7,9,-3,-6,6,-6,1,-7,3,8,-2,10,4,-7,-9,1,10,6,6,-6,1,-3,6,-1,-5,-7,-9,-6,-4,-7,6,9,-5,9,-6,4,-9,-2,-10,-3,1,1,-6,-4,-1,-5,1,3,8,-9,-9,4,1,-4,-10,-7,7,-2,6,7,-8,-4,-4,-5,3,7,-9,1,-8,3,1,10,8,3,9,-3,2,-6,-8,-9,6,-2,-8,7,7,-5,-9,-8,-6,-3,3,-1,-5,1,7,2,-5,-10,-7,-10,-6,5,-9,-4,-8,-9,-3,5,-5,-1,6,8,8,-8,-5,-1,3,-6,-3,-5,-7,1,3,8,-4,-2,4,6,10,-7,10,3,4,-6,-10,-7,5,7,-7,8,5,4,4,9,3,6,-4,9,-10,6,-5,-5,4,-10,6,-2,10,10,7,-7,-7,-6,-3,2,9,1,2,4,-9,-7,-2,8,7,5,9,-4,4,9,4,-1,1,9,-2,-1,9,6,7,3,-3,-5,2,-1,9,6,-1,-8,-10,8,-2,-3,-5,2,4,-5,6,1,9,-8,2,-6,2,-7,-3,-4,-4,-5,7,-2,-3,-10,-6,8,-1,-8,10,-5,-9,5,-9,-8,6,-3,-9,4,1,2,2,-5,-6,-5,-8,-9,5,9,-2,7,10,-1,-5,2,10,5,4,7,4,8,-4,-1,10,-3,8,-10,-9,7,7,-10,-5,-9,7,-9,-9,7,4,4,-7,-4,-8,3,-7,-1,-2,-3,8,-6,-9,-9,1,-2,3,9,-5,-3,9,-10,6,1,2,5,-6,-6,7,3,-3,-5,3,4,-6,8,-5,-2,-10,1,8,4,8,-9,7,-4,-7,5,-2,-7,-8,-6,5,-5,2,7,-3,-4,-10,5,4,-8,-10,-2,-3,-1,-4,-5,-6,4,-4,5,-1,-8,1,10,5,-8,-2,7,9,-8,6,4,2,9,-10,-3,3,-5,7,10,5,8,8,5,-5,2,4,5,-7,-4,-9,9,-10,-6,10,-8,-6,4,-4,-3,10,2,5,-2,2,-7,-4,-2,-3,-1,4,9,8,6,-2,10,-6,8,10,2,-7,-2,7,5,-2,-4,6,8,7,-5,-3,-1,-7,-10,10,-8,3,7,-6,2,9,-8,-1,8,-10,-7,7,-4,8,1,6,-4,-1,-10,5,9,-10,-10,3,1,10,8,7,-4,-6,2,4,4,8,4,-8,9,8,-10,-7,6,-8,-7,-6,9,-3,5,-6,-3,-3,-10,-10,8,8,8,-7,-3,9,-10,-10,-7,8,2,-1,2,4,2,1,-1,-9,4,-5,1,-6,9,9,-1,-7,5,-10,1,-9,7,4,10,-6,9,1,5,2,5,9,-10,-1,-4,10,-4,-8,-10,8,6,-4,7,-9,-3,6,2,-4,-2,7,-5,-1,7,-1,-4,7,-4,8,-6,-4,8,5,-5,-4,3,3,8,10,-5,-2,-1,-10,-2,8,5,-7,4,-5,-2,-6,-8,-4,4,2,4,-10,-5,-1,1,2,-3,-9,10,6,2,-8,10,7,-7,-5,4,-7,-8,-3,2,-4,-6,-2,10,-10,-9,-3,2,4,8,2,5,-9,2,1,-9,8,2,2,1,4], dtype = "uint8")#candidate|5694|(1960,)|const|uint8
call_5693 = func_3720_call(relay.reshape(const_5694.astype('uint8'), [10, 14, 14]), relay.reshape(const_5694.astype('uint8'), [10, 14, 14]), )
call_5695 = func_3720_call(relay.reshape(const_5694.astype('uint8'), [10, 14, 14]), relay.reshape(const_5694.astype('uint8'), [10, 14, 14]), )
func_3974_call = mod.get_global_var('func_3974')
func_3977_call = mutated_mod.get_global_var('func_3977')
var_5700 = relay.var("var_5700", dtype = "float32", shape = (60, 10))#candidate|5700|(60, 10)|var|float32
call_5699 = func_3974_call(relay.reshape(var_5700.astype('float32'), [10, 15, 4]))
call_5701 = func_3974_call(relay.reshape(var_5700.astype('float32'), [10, 15, 4]))
output = relay.Tuple([bop_5679,call_5693,const_5694,call_5699,var_5700,])
output2 = relay.Tuple([bop_5679,call_5695,const_5694,call_5701,var_5700,])
func_5703 = relay.Function([var_5677,var_5678,var_5700,], output)
mod['func_5703'] = func_5703
mod = relay.transform.InferType()(mod)
var_5704 = relay.var("var_5704", dtype = "float64", shape = ())#candidate|5704|()|var|float64
var_5705 = relay.var("var_5705", dtype = "float64", shape = (7, 3, 11))#candidate|5705|(7, 3, 11)|var|float64
var_5706 = relay.var("var_5706", dtype = "float32", shape = (60, 10))#candidate|5706|(60, 10)|var|float32
output = func_5703(var_5704,var_5705,var_5706,)
func_5707 = relay.Function([var_5704,var_5705,var_5706,], output)
mutated_mod['func_5707'] = func_5707
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5824 = relay.var("var_5824", dtype = "float64", shape = (16, 5, 2))#candidate|5824|(16, 5, 2)|var|float64
uop_5825 = relay.sqrt(var_5824.astype('float64')) # shape=(16, 5, 2)
uop_5843 = relay.cosh(uop_5825.astype('float32')) # shape=(16, 5, 2)
func_3974_call = mod.get_global_var('func_3974')
func_3977_call = mutated_mod.get_global_var('func_3977')
const_5854 = relay.const([7.205918,5.403653,-1.271769,8.549051,-2.751600,4.152325,-9.158933,3.684886,-7.244875,-1.848341,-8.519807,-9.543095,-1.053358,-0.221851,-7.817311,3.216383,-8.665991,-5.644557,7.102202,0.866689,6.886942,5.538056,-6.619949,6.659072,3.488201,-0.115135,2.240428,-0.914766,4.546236,8.233752,-5.351936,-3.928382,1.421705,9.802246,-2.294744,4.492002,5.095029,-3.376208,3.853714,0.005951,5.073957,-0.831782,-3.746907,-3.453394,0.854031,8.099732,-9.453487,2.556993,5.170472,-9.676801,6.166269,8.647040,6.344331,-5.184469,4.063671,5.235243,1.073542,1.098215,-7.946089,-7.663459,-2.312333,7.995024,5.315034,-8.271386,-9.362444,-2.529480,-3.477552,-6.354531,4.700422,-4.229743,-9.056627,5.809772,-5.242543,8.277883,-7.316050,-8.588272,-2.026293,-9.888011,-6.840743,-7.988885,4.347578,2.136597,-6.333267,7.676001,-7.326905,-1.567974,5.792104,4.559787,0.697642,9.280488,-9.126441,-6.130089,8.427076,-8.409111,2.844303,-3.980098,0.740605,3.812589,-0.585695,-0.166950,-3.728935,9.840851,-1.695821,4.949551,-7.299022,-3.914560,0.472263,4.190531,8.850744,-4.933413,-5.774814,0.913779,-7.410500,4.448648,-9.556012,-9.197076,-2.140832,-9.097761,-2.392447,-7.928124,-2.362778,2.784061,7.331756,2.835114,-5.932106,-7.163805,-5.010105,-5.094546,-3.789100,9.665227,9.029628,8.133940,-4.512699,2.111043,-0.823649,0.265273,-5.838782,-6.874923,6.171700,-8.426543,6.073785,-3.283694,-6.133311,4.804206,-0.207078,9.313567,-8.312934,8.278440,5.265228,0.528370,0.716600,-6.758942,0.731285,0.996384,-8.965543,-4.712135,-9.346424,-8.915375,2.170370,3.869080,-2.851135,-9.996964,-5.186937,6.479382,-9.210359,3.621123,6.447680,1.072926,-1.606252,5.713306,-9.526702,-0.951245,-5.739671,8.759860,-5.509329,2.403106,-7.727951,1.893002,-6.335294,-9.616181,5.711167,-0.777235,5.036744,3.885664,-0.318093,9.119254,-4.154141,-0.921087,-6.058479,3.018960,-6.773795,6.265465,-5.226400,3.795215,-5.366874,3.737107,9.426323,-1.636731,5.585035,-4.969440,6.554563,-5.764630,-1.039947,-6.394331,-2.084917,9.638431,2.225935,4.177072,-8.169576,-7.886497,-3.896013,-4.577421,4.894618,6.007330,2.759413,-2.224399,1.928084,-2.844935,2.564018,-9.082209,-0.599208,1.151505,-4.388023,3.507994,3.868841,6.940387,5.348324,-1.204139,5.271819,3.940024,4.828012,8.682169,-5.207443,-2.745029,-9.598898,-5.410887,3.866700,-8.035589,-8.266556,-1.584628,8.670551,-2.378777,5.553044,3.632847,-6.047274,9.456280,4.856960,-8.384231,5.849451,5.079781,1.750635,-0.484384,2.853005,-0.046165,8.850486,-0.967425,2.124950,2.906648,6.341287,9.641585,-7.690591,2.569892,9.875088,8.778623,4.725629,-6.635939,-7.668865,5.291996,-0.722732,-9.970583,-2.632495,-8.566317,3.073718,-9.739558,9.830718,-1.814983,5.049457,3.619165,2.118463,1.235204,7.365802,3.390579,-5.490806,-6.361986,-8.256925,-0.472089,9.496268,-7.288227,2.628704,6.926942,-1.474024,-1.614713,2.918836,-5.239881,-5.439986,2.339679,-4.222534,-9.211025,1.871203,8.945156,1.016318,-4.251363,-8.435455,8.599408,-4.021091,-0.927632,-9.275459,-6.390514,-6.932444,-7.912440,-1.413830,9.108579,-0.351986,3.021111,-7.450187,9.170777,5.632518,-2.446158,9.552161,8.224024,-3.149790,-7.989258,-4.966980,-3.820338,-5.064452,2.839476,4.117180,4.460661,-1.133572,1.459858,0.105463,-7.881638,9.224422,-8.633844,-8.999085,-7.945303,-4.795955,1.668577,2.098182,8.992867,-3.830764,-0.248063,1.368851,4.669630,-8.523564,-8.248597,-8.612560,-0.153552,6.383481,-9.784077,-2.327525,-3.960430,4.313723,1.173193,-9.196919,-0.724046,-6.174139,-5.521409,-9.483599,0.745043,-0.380695,-7.286466,0.137182,-7.788090,-8.938393,-8.101821,7.807622,3.417247,1.129293,1.421079,6.415390,-9.675234,-2.071887,-6.989990,8.332170,-2.674131,6.260849,-4.272492,0.589783,-0.167295,4.708484,1.572011,7.891993,5.538361,6.839803,-7.170786,5.168471,-4.241829,5.707641,-5.826440,9.197308,2.887569,-1.946471,3.613551,-6.652966,4.821846,-3.906112,3.838364,5.600073,-7.422838,3.923784,2.610107,-7.468213,7.276606,-2.326600,-1.194146,-5.507688,4.873203,5.875058,-1.008916,-4.688935,8.061611,-9.451096,-2.755663,6.700104,4.969442,-8.849936,6.501322,-6.581819,-0.569056,5.337512,-6.528316,-3.781693,-8.068357,-2.141942,-4.598347,-8.341978,-3.944306,-7.019900,-0.890265,7.938232,-7.205539,-0.795051,-3.093198,-8.256347,-4.061282,6.173271,1.085911,-8.643089,8.733123,0.513081,2.011540,0.379987,-8.618652,-3.814425,-1.560274,-7.793797,5.270174,-4.932389,-1.798168,3.183775,-1.389289,1.216280,-7.616514,6.970296,1.491904,2.278188,-5.881672,-4.548449,-0.504694,2.551381,-3.484780,-3.812203,3.135143,-6.858796,9.269845,-2.246846,-2.917062,-0.187145,7.515109,5.307469,-8.848578,0.013845,2.249210,5.406443,-4.786094,-9.434104,6.873410,4.812779,-4.298609,-0.613646,5.316520,5.249845,-3.013270,-2.843445,-0.225980,-3.229076,4.488580,5.213289,4.309556,-2.569392,-6.518737,0.360231,7.209617,-6.670569,-0.191422,-8.140423,8.142280,5.677274,9.231533,8.593021,6.588619,-5.955592,7.689974,-2.898548,-9.970016,-6.531868,2.644895,-8.262788,-6.463718,-2.127074,9.213213,-5.839985,0.291453,5.753434,-0.908103,-8.449457,-5.524159,-6.985643,-0.251309,5.651287,3.126262,8.695202,8.069694,-1.535570,-3.665204,-0.293231,4.016446,-6.814816,-6.888104,6.819199,-8.080420,6.171927,-0.599378,-2.934934,-8.131610,2.408053,-5.248073,-3.462301,5.000003,3.636830,-8.555213,1.489938,0.447970,-0.108406,3.839874,-5.381405,8.241383,7.986956,4.806027,-5.942124,5.113530,9.436063,2.381632,4.981515,-2.244360,-9.614649,-1.935477,-5.317171,-8.127945,7.410561,-3.851991,0.263440,3.161661,6.037617,2.706178,-8.098528,-7.094606,-3.790385,-9.277750,-7.279178,-0.944618,5.947479,-7.601695,-8.048302,-8.737548,4.979816,5.589307,-4.158098,1.366865,8.435271,9.578078,2.176133,-2.240613,5.265963,6.674310,5.166831,0.606888,-1.733658,8.738636,-9.741080,-9.090517,-0.858647,-1.059480,0.418503,3.388045,-3.021024,-9.742326,-3.750785,0.727902], dtype = "float32")#candidate|5854|(600,)|const|float32
call_5853 = func_3974_call(relay.reshape(const_5854.astype('float32'), [10, 15, 4]))
call_5855 = func_3974_call(relay.reshape(const_5854.astype('float32'), [10, 15, 4]))
output = relay.Tuple([uop_5843,call_5853,const_5854,])
output2 = relay.Tuple([uop_5843,call_5855,const_5854,])
func_5858 = relay.Function([var_5824,], output)
mod['func_5858'] = func_5858
mod = relay.transform.InferType()(mod)
var_5859 = relay.var("var_5859", dtype = "float64", shape = (16, 5, 2))#candidate|5859|(16, 5, 2)|var|float64
output = func_5858(var_5859)
func_5860 = relay.Function([var_5859], output)
mutated_mod['func_5860'] = func_5860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5879 = relay.var("var_5879", dtype = "float64", shape = (13, 2, 10))#candidate|5879|(13, 2, 10)|var|float64
var_5880 = relay.var("var_5880", dtype = "float64", shape = (13, 2, 10))#candidate|5880|(13, 2, 10)|var|float64
bop_5881 = relay.floor_divide(var_5879.astype('float64'), relay.reshape(var_5880.astype('float64'), relay.shape_of(var_5879))) # shape=(13, 2, 10)
func_4813_call = mod.get_global_var('func_4813')
func_4819_call = mutated_mod.get_global_var('func_4819')
const_5898 = relay.const(-8, dtype = "int32")#candidate|5898|()|const|int32
var_5899 = relay.var("var_5899", dtype = "int32", shape = (132,))#candidate|5899|(132,)|var|int32
const_5900 = relay.const([3.066387,-0.496010,-3.612512,-1.583200,9.372474,-4.173374,5.954010,-6.476114,-5.815067,8.177461,-5.848350,9.810106,-6.174427,2.767642,-7.404739,-6.177702,2.683486,7.866903,6.678702,-3.716492,0.623583,-6.007435,-4.644021,0.653269,-2.301368,2.457621,-1.983405,5.410396,1.545387,-1.664294,-4.546820,-6.448713,-8.358302,6.662976,0.998867,-4.397249,-8.041045,8.204531,9.178377,-3.934454,6.678329,-2.252972,-2.356309,-6.174881,6.344546,7.456243,-4.105176,1.191017,2.334685,-6.133221,3.752332,0.537349,5.424081,-2.761606,0.384094,7.927432,-8.193456,-1.684194,8.959597,-4.709521,-3.985962,-3.052031,1.496574,2.081080,3.940705,0.877289,-3.933343,-5.304667,7.349395,-7.629836,0.324529,-2.776899,5.720558,-4.983556,1.139764,8.155756,-3.586218,-2.486200,-7.922895,-6.107386,-6.149426,-2.121365,4.776396,-1.626956,0.412783,3.359780,-0.014835,-8.642429,3.169290,6.908160,1.315902,-1.738033,-7.356001,-4.529720,-3.345964,-4.519588,-0.810587,0.074356,-3.850681,5.193057,-9.990955,-5.528978,-4.867487,-3.591499,-2.095325,-3.993727,6.348933,1.560036,-5.858733,-3.758211,3.242898,8.688522,2.673584,7.725621,-8.237929,1.021629,4.352769,-9.784804,-6.009567,5.855148,-7.656839,-2.295363,-3.078064,3.759558,4.265372,2.286527,4.274960,9.920895,8.979017,-2.139971,8.315862,-1.939276,9.688157,-1.153817,-1.147551,-6.955687,9.753416,-3.544592,2.232318,-1.570625,2.729766,0.989007,-8.663058,9.569224,9.396034,-3.429140,2.701202,4.819820,9.019696,-5.762154,-5.252639,-0.891535,9.234725,7.027096,-9.265635,-3.227579,-8.804945,-9.317735,-6.109663,-5.692177,3.730977,-8.100219,-3.484242,-5.376022,8.032993,8.683806,2.497424,7.942854,-0.742031,5.998742,8.985495,-7.605168,2.089466,-5.873455,-3.556389,9.871511,8.135524,-5.316655,-6.280022,9.188064,7.887505,4.811225], dtype = "float32")#candidate|5900|(182,)|const|float32
var_5901 = relay.var("var_5901", dtype = "uint8", shape = (384,))#candidate|5901|(384,)|var|uint8
call_5897 = relay.TupleGetItem(func_4813_call(relay.reshape(const_5898.astype('int32'), []), relay.reshape(var_5899.astype('int32'), [1, 11, 12]), relay.reshape(const_5900.astype('float32'), [182,]), relay.reshape(var_5901.astype('uint8'), [384,]), ), 5)
call_5902 = relay.TupleGetItem(func_4819_call(relay.reshape(const_5898.astype('int32'), []), relay.reshape(var_5899.astype('int32'), [1, 11, 12]), relay.reshape(const_5900.astype('float32'), [182,]), relay.reshape(var_5901.astype('uint8'), [384,]), ), 5)
output = relay.Tuple([bop_5881,call_5897,const_5898,var_5899,const_5900,var_5901,])
output2 = relay.Tuple([bop_5881,call_5902,const_5898,var_5899,const_5900,var_5901,])
func_5906 = relay.Function([var_5879,var_5880,var_5899,var_5901,], output)
mod['func_5906'] = func_5906
mod = relay.transform.InferType()(mod)
var_5907 = relay.var("var_5907", dtype = "float64", shape = (13, 2, 10))#candidate|5907|(13, 2, 10)|var|float64
var_5908 = relay.var("var_5908", dtype = "float64", shape = (13, 2, 10))#candidate|5908|(13, 2, 10)|var|float64
var_5909 = relay.var("var_5909", dtype = "int32", shape = (132,))#candidate|5909|(132,)|var|int32
var_5910 = relay.var("var_5910", dtype = "uint8", shape = (384,))#candidate|5910|(384,)|var|uint8
output = func_5906(var_5907,var_5908,var_5909,var_5910,)
func_5911 = relay.Function([var_5907,var_5908,var_5909,var_5910,], output)
mutated_mod['func_5911'] = func_5911
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6411 = relay.var("var_6411", dtype = "float64", shape = (12, 16, 14))#candidate|6411|(12, 16, 14)|var|float64
var_6412 = relay.var("var_6412", dtype = "float64", shape = (12, 16, 14))#candidate|6412|(12, 16, 14)|var|float64
bop_6413 = relay.divide(var_6411.astype('float64'), relay.reshape(var_6412.astype('float64'), relay.shape_of(var_6411))) # shape=(12, 16, 14)
uop_6425 = relay.cosh(bop_6413.astype('float32')) # shape=(12, 16, 14)
bop_6430 = relay.maximum(uop_6425.astype('float64'), relay.reshape(bop_6413.astype('float64'), relay.shape_of(uop_6425))) # shape=(12, 16, 14)
func_4466_call = mod.get_global_var('func_4466')
func_4469_call = mutated_mod.get_global_var('func_4469')
const_6434 = relay.const([3,-2,-7,-9,-9,-3,10,-10,-9,10,-7,-2,4,2,8,-3,3,8,-2,-6,4,4,3,1,-1,5,-5,-4,10,-8,7,7,-9,-2,2,9,-7,-1,1,4,2,-7,-6,-8,6,5,7,3,-9,-4,3,8,-8,-4,-3,-10,-8,2,9,2,-5,-1,1,8,-1,2,6,7,10,-5,-10,8,4,-1,1,10,-10,-10,-7,2,9,-3,3,2,-3,-6,4,10,5,10,-5,-4,1,8,2,-7,6,-7,2,-4,-8,8,6,1,9,9,-4,-3,-7,-5,2,2], dtype = "int32")#candidate|6434|(112,)|const|int32
var_6435 = relay.var("var_6435", dtype = "int16", shape = (448,))#candidate|6435|(448,)|var|int16
call_6433 = relay.TupleGetItem(func_4466_call(relay.reshape(const_6434.astype('int32'), [14, 8]), relay.reshape(var_6435.astype('int16'), [448,]), ), 3)
call_6436 = relay.TupleGetItem(func_4469_call(relay.reshape(const_6434.astype('int32'), [14, 8]), relay.reshape(var_6435.astype('int16'), [448,]), ), 3)
bop_6447 = relay.less_equal(bop_6430.astype('bool'), relay.reshape(bop_6413.astype('bool'), relay.shape_of(bop_6430))) # shape=(12, 16, 14)
uop_6451 = relay.log(var_6412.astype('float64')) # shape=(12, 16, 14)
bop_6463 = relay.power(bop_6430.astype('float32'), relay.reshape(uop_6425.astype('float32'), relay.shape_of(bop_6430))) # shape=(12, 16, 14)
output = relay.Tuple([call_6433,const_6434,var_6435,bop_6447,uop_6451,bop_6463,])
output2 = relay.Tuple([call_6436,const_6434,var_6435,bop_6447,uop_6451,bop_6463,])
func_6468 = relay.Function([var_6411,var_6412,var_6435,], output)
mod['func_6468'] = func_6468
mod = relay.transform.InferType()(mod)
var_6469 = relay.var("var_6469", dtype = "float64", shape = (12, 16, 14))#candidate|6469|(12, 16, 14)|var|float64
var_6470 = relay.var("var_6470", dtype = "float64", shape = (12, 16, 14))#candidate|6470|(12, 16, 14)|var|float64
var_6471 = relay.var("var_6471", dtype = "int16", shape = (448,))#candidate|6471|(448,)|var|int16
output = func_6468(var_6469,var_6470,var_6471,)
func_6472 = relay.Function([var_6469,var_6470,var_6471,], output)
mutated_mod['func_6472'] = func_6472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6486 = relay.var("var_6486", dtype = "float32", shape = (1, 14, 13))#candidate|6486|(1, 14, 13)|var|float32
uop_6487 = relay.asin(var_6486.astype('float32')) # shape=(1, 14, 13)
func_632_call = mod.get_global_var('func_632')
func_635_call = mutated_mod.get_global_var('func_635')
var_6492 = relay.var("var_6492", dtype = "int64", shape = (450,))#candidate|6492|(450,)|var|int64
var_6493 = relay.var("var_6493", dtype = "int16", shape = (48, 1))#candidate|6493|(48, 1)|var|int16
call_6491 = relay.TupleGetItem(func_632_call(relay.reshape(var_6492.astype('int64'), [15, 3, 10]), relay.reshape(var_6493.astype('int16'), [24, 2]), ), 2)
call_6494 = relay.TupleGetItem(func_635_call(relay.reshape(var_6492.astype('int64'), [15, 3, 10]), relay.reshape(var_6493.astype('int16'), [24, 2]), ), 2)
uop_6499 = relay.tan(uop_6487.astype('float64')) # shape=(1, 14, 13)
func_3974_call = mod.get_global_var('func_3974')
func_3977_call = mutated_mod.get_global_var('func_3977')
var_6504 = relay.var("var_6504", dtype = "float32", shape = (600,))#candidate|6504|(600,)|var|float32
call_6503 = func_3974_call(relay.reshape(var_6504.astype('float32'), [10, 15, 4]))
call_6505 = func_3974_call(relay.reshape(var_6504.astype('float32'), [10, 15, 4]))
output = relay.Tuple([call_6491,var_6492,var_6493,uop_6499,call_6503,var_6504,])
output2 = relay.Tuple([call_6494,var_6492,var_6493,uop_6499,call_6505,var_6504,])
func_6515 = relay.Function([var_6486,var_6492,var_6493,var_6504,], output)
mod['func_6515'] = func_6515
mod = relay.transform.InferType()(mod)
mutated_mod['func_6515'] = func_6515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6515_call = mutated_mod.get_global_var('func_6515')
var_6517 = relay.var("var_6517", dtype = "float32", shape = (1, 14, 13))#candidate|6517|(1, 14, 13)|var|float32
var_6518 = relay.var("var_6518", dtype = "int64", shape = (450,))#candidate|6518|(450,)|var|int64
var_6519 = relay.var("var_6519", dtype = "int16", shape = (48, 1))#candidate|6519|(48, 1)|var|int16
var_6520 = relay.var("var_6520", dtype = "float32", shape = (600,))#candidate|6520|(600,)|var|float32
call_6516 = func_6515_call(var_6517,var_6518,var_6519,var_6520,)
output = call_6516
func_6521 = relay.Function([var_6517,var_6518,var_6519,var_6520,], output)
mutated_mod['func_6521'] = func_6521
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6579 = relay.var("var_6579", dtype = "int32", shape = (3, 13, 10))#candidate|6579|(3, 13, 10)|var|int32
var_6580 = relay.var("var_6580", dtype = "int32", shape = (3, 13, 10))#candidate|6580|(3, 13, 10)|var|int32
bop_6581 = relay.greater(var_6579.astype('bool'), relay.reshape(var_6580.astype('bool'), relay.shape_of(var_6579))) # shape=(3, 13, 10)
output = bop_6581
output2 = bop_6581
func_6606 = relay.Function([var_6579,var_6580,], output)
mod['func_6606'] = func_6606
mod = relay.transform.InferType()(mod)
mutated_mod['func_6606'] = func_6606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6606_call = mutated_mod.get_global_var('func_6606')
var_6608 = relay.var("var_6608", dtype = "int32", shape = (3, 13, 10))#candidate|6608|(3, 13, 10)|var|int32
var_6609 = relay.var("var_6609", dtype = "int32", shape = (3, 13, 10))#candidate|6609|(3, 13, 10)|var|int32
call_6607 = func_6606_call(var_6608,var_6609,)
output = call_6607
func_6610 = relay.Function([var_6608,var_6609,], output)
mutated_mod['func_6610'] = func_6610
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6647 = relay.var("var_6647", dtype = "int16", shape = ())#candidate|6647|()|var|int16
var_6648 = relay.var("var_6648", dtype = "int16", shape = (11, 7, 9))#candidate|6648|(11, 7, 9)|var|int16
bop_6649 = relay.minimum(var_6647.astype('int16'), var_6648.astype('int16')) # shape=(11, 7, 9)
bop_6652 = relay.less_equal(var_6648.astype('bool'), var_6647.astype('bool')) # shape=(11, 7, 9)
func_1387_call = mod.get_global_var('func_1387')
func_1389_call = mutated_mod.get_global_var('func_1389')
const_6659 = relay.const([-1.687513,-1.596897,7.774205,0.681458,-1.005225,6.754808,-7.310403,2.550370,-6.147858,-4.146228,-1.160226,2.210460,-6.432158,9.320879,7.312602,0.601076,-0.269280,3.592644,-9.721847,1.893759,8.916073,7.036293,-9.700663,-6.174893,-5.883450,-5.285632,-8.055380,-2.667104,-5.380928,-4.938939,-7.824702,-0.427339,1.147759,-9.478310,-0.154125,8.660751,-0.309569,8.266581,7.323058,-8.258637,-7.443756,-4.784030,-7.058864,6.443874,-8.098548,-6.365816,-7.398142,7.494423,-2.941103,3.814310,6.728378,-1.972241,8.288301,-7.574219,0.214312,-1.742094,-0.709379,-0.708841,6.385987,2.911984,2.091120,-8.240336,-8.249923,-0.414934,3.540076,-5.449197,-4.165378,9.399786,-1.796998,-6.457128,-0.700149,-0.371066,0.593550,5.068873,-2.073708,-0.603201,-0.449005,3.614780,-2.435347,-5.411654,8.290709,-1.081576,8.558089,6.050353,8.428293,-3.333812,-2.827726,-2.533138,9.740946,-2.759187,0.940215,-2.515413,6.631904,-7.170601,5.433206,-1.640008,3.241035,-4.204610,-2.914829,4.191593,6.370601,4.018499,-3.461380,3.507849,9.487679,0.215425,-8.220461,-7.629469,-9.132206,1.575828,8.413078,-6.199961,-3.435557,-4.242431,5.197198,-9.045166,1.550154,-3.552552,-5.804452,1.927466,-0.621157,-7.093764,-8.963041,-2.568172,3.259820,-2.090269,3.767954,-1.410543,0.063964,-9.162632,-9.653644,2.341276,-6.203223,3.073197,6.804689,-9.413016,2.458120,-5.017206,-5.859995,-1.334040,-6.537603,-0.541201,-8.697897,4.062069,3.119398,-7.530506,3.967603,8.030695,1.709308,-7.509639,-6.685083,-8.277114,0.316108,3.154176,-7.972804,6.419745], dtype = "float32")#candidate|6659|(156,)|const|float32
call_6658 = relay.TupleGetItem(func_1387_call(relay.reshape(const_6659.astype('float32'), [13, 3, 4])), 1)
call_6660 = relay.TupleGetItem(func_1389_call(relay.reshape(const_6659.astype('float32'), [13, 3, 4])), 1)
func_3832_call = mod.get_global_var('func_3832')
func_3835_call = mutated_mod.get_global_var('func_3835')
var_6665 = relay.var("var_6665", dtype = "float32", shape = (48, 4))#candidate|6665|(48, 4)|var|float32
call_6664 = relay.TupleGetItem(func_3832_call(relay.reshape(var_6647.astype('float32'), []), relay.reshape(var_6665.astype('float32'), [3, 16, 4]), ), 1)
call_6666 = relay.TupleGetItem(func_3835_call(relay.reshape(var_6647.astype('float32'), []), relay.reshape(var_6665.astype('float32'), [3, 16, 4]), ), 1)
func_4466_call = mod.get_global_var('func_4466')
func_4469_call = mutated_mod.get_global_var('func_4469')
const_6681 = relay.const([4,8,6,-4,-9,1,-7,5,8,-3,-3,4,2,3,6,7,-7,7,-5,2,-9,9,3,-6,-7,-9,-3,-10,-9,-6,6,8,-8,-7,-7,8,-9,5,-10,4,-9,8,6,-7,-3,-3,-6,-2,-7,1,5,1,6,-7,-7,4,4,8,-1,8,-9,3,-3,4,-4,-3,4,-7,9,5,-7,-4,10,-2,8,-5,2,-4,4,2,-3,-1,8,-5,3,5,-8,2,10,9,3,-6,-3,-9,-8,-7,5,-6,-5,2,-1,-10,7,-7,6,-6,9,6,-2,-8,-4,-9], dtype = "int32")#candidate|6681|(112,)|const|int32
var_6682 = relay.var("var_6682", dtype = "int16", shape = (112, 4))#candidate|6682|(112, 4)|var|int16
call_6680 = relay.TupleGetItem(func_4466_call(relay.reshape(const_6681.astype('int32'), [14, 8]), relay.reshape(var_6682.astype('int16'), [448,]), ), 4)
call_6683 = relay.TupleGetItem(func_4469_call(relay.reshape(const_6681.astype('int32'), [14, 8]), relay.reshape(var_6682.astype('int16'), [448,]), ), 4)
func_2019_call = mod.get_global_var('func_2019')
func_2026_call = mutated_mod.get_global_var('func_2026')
const_6688 = relay.const([[9.735415,8.475782,-9.562471,-2.557403,4.043009,-7.646968,-1.251514,0.954652,6.950765,2.477131,-2.381778,5.729218,4.048795,7.750971,-4.859710,-5.338678,4.386777,2.077891,-8.794428,-4.784590,6.494616,-1.831356,-1.176769,-4.027312,-7.018502,0.278830,5.692945,2.588588,3.226297,-2.163601,-9.979089,9.172308,-8.460792,2.330813,2.774532,9.832522,-2.599650,-4.325853,8.031816,-7.511029,-4.651026,-9.050627,-4.947049,9.548691,-4.919187,3.534931,-4.722617,-5.015647,9.587169,2.652649,8.958837,2.177887,6.428243,8.466223,-3.199857,-8.465997,0.262042,2.324903,2.208803,3.061065,-2.970926,-3.405427,-3.052695,-6.619565,-1.495045,-4.625722,-7.743643,-1.109085,6.250287,-7.421753,2.597734,-1.312466,9.466177,5.185885,-5.747005,-0.893751,3.374116,-8.093483,6.094566,-0.895243,-7.804444,-9.516820,-1.679613,-6.675128,-9.867729,-1.426286,-1.232581,-5.852054,-1.193692,-5.438143,-8.444374,5.629783,4.452278,6.723708,-1.689199,-6.293142,-9.589784,9.919573,0.364382,-1.942544,-0.690491,-0.461087,-0.822160,-5.177768,-0.624236,2.884507,3.711822,-1.810828,-4.209682,-3.637100,1.167128,-5.785532,5.650998,9.871354,6.234986,-4.081779,-2.527809,-2.915239,6.053256,2.390496,5.835148,-6.147940,6.556063,6.771260,7.047240,8.063454,1.175570,-2.546183,1.593659,3.910326,-7.428051,2.564004,-6.118074,8.300020,-4.879795,2.423412,8.593884,1.157850,3.544943,4.406329,-5.573416,7.966446,-1.030728,-6.688391,8.575263,-9.684586,3.089404,-7.212971,-8.758665,9.162366,-9.079077,-6.510424,-5.623522,2.194191,8.771998,-0.218438,7.614712,2.300702,-7.941022,7.004575,1.398231,9.274029,6.623979,0.772924,5.361709,2.668850,8.872262,9.573896,5.027187,9.461505,1.611057,-8.245483,-7.143835,-2.559714,9.714954,-5.732485,-3.796533,7.794813,-9.034827,9.895506,1.388972,4.061722,-9.841823,-2.511116,9.569850,-8.304237,-8.292820,1.565012,-2.555836,7.832511,-8.536758,3.106419,6.493030,-4.374305,9.878410],[4.621993,-4.725070,0.670093,9.824408,-3.735563,-2.366500,-4.053046,7.737616,2.534360,4.381552,2.272156,-3.458992,-1.387461,0.360772,8.217801,-0.735974,8.139871,-6.084884,-6.769814,2.806773,-2.561612,4.297338,-5.183374,3.806875,2.847531,-6.517647,-3.117376,4.844147,-5.872129,7.575732,4.324285,-9.373428,4.810282,6.775588,-9.352065,-0.231048,-0.389124,2.890024,0.930566,-5.514878,-0.913427,8.559804,-6.546095,2.279565,-7.382450,-1.314858,7.094224,-6.543065,3.186006,-4.630284,-2.015658,4.238626,-4.393689,0.663264,3.456533,-5.798087,-9.815838,-9.529559,-7.339611,6.051332,-1.979612,-5.763431,-5.808857,-3.791893,5.252605,-6.029106,-7.159087,-8.909064,-3.237110,-3.256053,-5.646454,0.547221,-4.352483,8.233974,-2.182724,8.052692,-5.191520,-7.401355,4.406400,3.093724,8.739673,-3.267363,0.375104,-7.327248,8.673032,5.067685,-1.565087,-5.507902,-0.310000,0.552856,1.321854,3.907556,3.664274,-3.373173,9.703400,9.326731,5.618929,-6.518315,-3.023570,2.448291,3.307532,0.936916,6.522311,-5.422522,3.352022,-0.966949,2.426096,4.221427,8.522613,5.317893,6.511443,8.550960,-3.608919,4.700547,7.718226,-5.977591,3.541233,-7.299534,-1.233672,-8.109350,-1.281204,-2.610179,-1.237210,-3.911415,1.443319,-2.611290,-5.225810,-0.315210,4.025218,-0.758106,-8.811043,4.262696,-2.455292,-4.893157,3.150894,1.170776,-1.969549,6.646481,5.419726,-2.101554,2.255349,7.561516,5.148747,-1.296304,0.147416,3.368043,-2.951643,0.147535,-9.756881,6.455326,-6.168778,9.463252,-0.801660,7.912860,1.760603,-4.885498,1.488114,-5.689765,6.927621,1.014327,1.395474,-8.942216,-1.756806,0.613962,-6.901890,-2.892828,0.041504,3.239426,-2.537071,9.921094,-4.425751,-8.679743,9.699381,-4.593240,8.332476,4.281595,-9.535925,-4.505618,7.547312,6.664600,-9.141410,-3.881337,-1.458774,7.121021,-9.342107,-9.553097,3.349427,-7.159353,5.431989,7.249838,7.922082,-8.193142,6.545197,-9.420306,-2.141555],[-5.054163,8.852696,-3.838313,-4.766824,-2.768501,-2.152120,6.016076,8.405949,-4.000551,3.280571,3.010655,-3.631052,-0.859622,2.161172,-2.445331,2.472855,-6.168236,0.417210,-5.268529,5.813911,-6.344502,6.421146,1.423239,-6.991527,7.365288,3.678574,-9.242217,-3.577774,6.218020,9.137416,6.158543,-1.569104,1.463895,-3.033385,7.622056,-1.198086,8.974678,-4.110159,-3.427031,-8.035812,-3.012775,-6.400303,0.066297,8.628651,-3.535635,-5.850221,2.944346,-7.853469,-3.879071,-6.410350,-8.541066,-3.734365,-3.736075,-7.036304,2.994899,7.066490,-8.216748,-5.388712,-0.157214,9.200500,-6.930671,2.821041,-1.868816,-3.756800,-6.422362,6.586595,0.211452,7.168525,-8.259561,-6.544973,-1.588850,6.112390,6.347592,0.871403,1.680185,4.528233,-9.967478,-1.975358,-9.814506,-7.851133,0.371077,4.228804,3.657120,0.354573,-7.128522,2.760161,9.084280,1.690758,-5.100371,-6.729392,8.218460,5.611655,-2.624708,5.142609,-8.409708,-5.783918,4.531178,-5.704227,-3.795033,-4.713313,0.962893,8.751827,-8.070691,1.207209,3.633487,-4.487752,0.632112,5.547798,3.865442,-6.827619,-3.697509,-4.963662,-0.284689,-8.325563,-0.917719,9.420594,-8.770139,-3.297733,-8.619577,3.180471,3.824288,-2.050998,0.531860,3.345424,-4.158139,-4.509020,-2.287787,-4.852993,4.998492,2.941536,0.043192,1.989786,9.492737,-5.918780,4.712761,-6.915247,-9.038855,-0.327671,-7.305941,-6.787741,6.526184,7.483780,7.410155,8.049911,-1.044118,-2.313931,7.887402,9.478490,8.178922,-8.409536,9.169967,-6.039574,-3.449539,3.447001,-7.928402,7.941973,-4.100336,7.176996,2.307064,-6.247495,6.384642,2.482103,-3.592641,2.276348,8.979819,-3.689226,-2.168098,-3.386418,7.358057,8.049717,5.885908,-4.158321,8.821965,-2.308243,-2.644852,-2.069715,2.428869,-1.849075,-7.579696,-1.638363,-7.682215,-3.713178,4.207603,3.111479,-2.383696,-3.034936,7.512743,2.899401,-2.182419,1.542096,-7.607594,-1.318482,-0.107794,7.305454,-5.434737],[-5.048172,5.907856,-0.863278,2.506599,8.106085,-8.738896,5.934650,-0.345172,5.224364,-0.811213,9.839156,-3.726091,7.891331,3.323092,-0.482649,-0.134409,-4.615473,9.953940,-0.362859,-9.326496,1.441885,1.262993,-4.438746,0.534873,-4.278110,6.706463,3.634932,8.108820,-8.707589,2.029132,-8.273448,2.341273,7.300631,2.777566,1.687973,-8.001022,8.038856,5.237311,4.016093,4.153510,2.755664,-5.854405,-2.395415,7.542039,-4.874851,4.901041,-8.929696,8.985366,-1.931134,1.561835,-8.670982,-7.561891,2.833055,4.621977,-6.190718,-6.176981,5.631832,-5.840215,-1.193602,-3.218569,5.012798,2.586891,-2.952623,2.622314,-7.594944,-9.240674,-0.702601,-5.243447,3.197433,2.997623,-0.616770,9.761596,-0.603263,1.550141,5.639327,2.682492,-4.126860,-1.198903,8.002476,3.352590,-7.334736,-6.021233,-5.760010,-6.155043,-9.053311,2.753312,1.981197,1.509745,9.832877,-2.640106,-6.756980,8.556344,-7.061620,-2.059177,2.614289,5.828762,1.799617,7.865536,-6.811140,2.913386,1.709715,1.973731,4.095683,-4.077396,-0.840776,4.092475,-2.012785,6.378357,-5.373488,-4.515230,3.526852,3.167104,8.825850,-7.434278,-3.887463,-7.343204,-6.096015,-9.710992,-8.775013,-1.258006,5.127011,-0.510547,-5.862663,2.300764,6.183577,1.002732,6.701332,8.138557,6.196767,3.325518,-0.139734,1.529037,9.569252,-6.221463,-7.033648,-1.845517,5.906402,1.922406,-9.202483,-9.615673,-4.936377,-6.945885,7.944695,-9.594741,6.683966,-6.911890,6.590547,3.219887,-1.964832,8.264968,-6.831879,-1.236773,-9.239603,-1.125227,-5.092719,-9.736838,-4.578623,9.054069,-1.582445,-7.623786,1.701288,5.669891,-4.647455,9.924457,6.108265,0.774770,0.569044,2.441729,9.875483,-6.021089,-0.638175,-2.222141,-4.699541,-1.928766,1.362977,-5.041923,-4.711245,3.991438,-1.520978,9.613521,1.963806,-7.734156,-4.477898,-2.684424,2.438325,-1.796480,0.964695,-2.774657,-4.731227,9.746986,9.843540,-8.342258,7.661009,-6.114317,-5.382923],[4.160037,-3.030005,-7.748418,7.280002,-8.439692,-7.576752,9.344403,9.253062,6.083830,-6.037868,2.738663,-4.621391,9.884206,2.111460,-9.102401,2.878655,-4.815906,8.332589,1.978248,3.942004,6.273827,-1.333436,-2.528469,-4.959052,0.021330,-5.492239,-9.128590,-2.978078,-5.978348,1.067550,0.646349,0.465737,-3.148525,0.720836,6.441435,7.711639,-0.760368,3.765831,7.008989,-5.097161,3.975788,2.014229,7.740837,3.517146,2.241382,-1.550050,-7.828650,-1.198057,-1.524354,-7.828960,0.235842,-4.805504,9.329773,-4.587401,1.154124,6.604519,7.006633,-6.422324,-5.676767,-8.070095,-1.581601,-7.550217,-6.642657,6.787105,-9.242042,6.913549,5.311993,8.077029,0.124992,8.608919,-5.911943,3.494661,6.975119,2.283241,-2.073246,-3.935358,-2.807224,4.888370,3.071602,-3.189707,-5.088666,3.931397,5.004254,-0.830681,-6.996918,-8.469159,-4.589150,-0.485123,4.249021,5.102762,-1.381996,0.071705,-6.326647,6.637137,5.113668,-7.462653,5.746798,-8.049753,-9.037588,-4.191209,-0.616606,-1.402005,-9.468718,6.881693,-9.306444,4.558356,-4.753393,0.948045,1.561824,-3.116721,-8.611274,-8.098615,9.549581,7.895592,6.692636,-0.552371,-9.251401,-5.215039,-5.430099,-2.841744,-6.552846,1.286592,-7.039515,-0.151073,8.984041,2.413416,5.647548,-6.835843,-2.711878,-4.065650,7.123337,4.479963,2.035884,-7.274000,0.826964,-4.178152,3.007176,-6.707185,7.720345,5.362481,-1.340865,-8.881644,2.615776,-3.218903,-5.552621,4.057233,9.875387,1.476880,8.590940,-8.625605,2.341801,-7.783097,-3.942945,-8.122280,4.459567,8.990944,-6.023544,8.841617,-1.515466,8.387599,0.725353,-9.048397,-8.237903,6.540767,0.671533,-1.661208,8.666965,1.413662,-9.768689,9.790766,-6.744990,6.766239,-3.096928,-0.046205,-9.065896,-4.275729,-1.551998,-0.493397,-1.874086,-9.516201,-4.735551,-3.947973,-8.502077,9.557561,-5.877311,-4.016315,5.155434,0.837958,4.752758,-7.219554,-8.289234,1.009435,8.708226,9.825635,2.113097],[-2.687685,-2.819285,0.049790,-0.161573,9.204606,6.083958,2.838309,3.696288,1.421748,-4.422170,-1.607141,-6.670138,-7.563532,-4.187197,4.224991,6.840553,9.619043,3.925485,-6.837209,7.232153,-5.393893,-1.513262,-8.246433,-8.556022,-1.317146,4.555701,5.044225,-4.856923,-6.513984,5.297777,-7.479936,0.921273,8.118101,1.297315,-7.790194,8.444448,4.975997,4.290943,-3.651568,6.198581,-7.998881,5.234488,-9.596370,5.959238,-1.761191,1.988851,-4.860753,-2.017056,0.851270,9.608728,5.405345,-7.742036,-1.463621,-3.908373,3.903875,7.905543,-0.146061,-2.059441,-3.900838,8.948788,-7.346984,-8.371308,6.171637,-0.584488,-1.250419,6.740775,3.682789,-5.901905,0.958147,-3.063189,8.671422,-7.394168,-5.220306,-4.879420,7.556668,-4.615132,-9.084040,-2.404020,6.304330,-1.807193,-4.032502,6.909714,0.081485,-5.508409,-7.407927,-4.688954,-8.775990,-0.469773,2.377135,-6.945960,-6.300060,-5.734649,1.582487,8.059276,-1.350049,-8.547404,5.325528,-0.356225,1.627884,5.172641,8.157742,1.452354,-8.378746,-2.516282,6.288879,-0.538952,2.838190,-6.955731,1.851507,-4.491111,-3.528653,3.675083,-4.773592,-0.740799,-1.769593,-7.109682,8.967827,2.808899,9.992439,5.074898,-0.646190,-5.394279,6.523388,-8.188854,-4.500389,-2.828194,6.230612,-3.701588,7.184086,-0.235358,-2.623851,0.079026,-0.209239,-6.783479,-4.735932,-6.884883,8.953756,4.019558,-5.919824,-9.892824,-4.304529,2.938501,-7.369237,0.997488,-1.588154,9.651176,-5.505451,4.774861,9.155351,-9.582866,4.544784,1.041871,-8.519935,2.856145,-9.821827,7.674732,-6.557881,1.212356,6.652354,-8.691808,-2.863774,-3.082297,-3.266803,4.038084,8.836323,-9.673928,5.589104,-0.238977,-4.553395,-2.829787,6.317680,3.159250,-6.161231,-5.493095,0.270344,1.253648,-5.887633,0.147515,8.061189,-1.643372,-1.481072,-9.874480,-7.801564,5.891274,-0.406012,-8.610783,-9.229179,-0.132420,-2.261643,-9.138661,9.691696,1.856769,1.976943,5.841834,0.131456],[-4.213011,-8.965594,4.233352,1.544201,2.404287,-8.154553,7.691490,9.806541,6.345817,-9.739044,9.772076,-9.675966,8.144899,7.980985,-1.164577,-7.869272,7.494412,8.107222,-0.354384,5.046961,2.894057,7.333261,-4.745327,-3.848905,-2.736626,0.142852,-4.372356,-0.979109,-7.379195,-0.957964,-5.839387,4.432486,3.822722,6.233887,3.409211,0.875437,-3.672324,3.500244,2.004288,4.920656,-1.743994,-5.073004,-9.730806,-4.611593,-5.812230,9.253577,7.068076,-3.870065,-1.837533,-7.705629,1.912087,-4.898182,-2.527685,-5.449773,3.540643,7.360465,6.396673,-3.472065,-7.653598,-1.759026,-5.260867,-5.800549,-9.060007,-4.859154,-8.916196,-3.362255,0.337012,2.061005,-4.303730,3.135929,8.239942,0.842980,-2.005114,-3.235893,-3.581446,-2.551569,4.371435,-1.933052,4.487054,-1.892361,-0.245666,6.847589,2.528717,4.860940,5.863552,4.127688,-9.113169,6.021115,-1.112065,3.209899,-5.635091,7.042463,-2.087465,4.104363,4.329186,8.396019,-4.172854,4.138310,-7.471155,8.936695,2.425213,-3.636024,2.195984,8.119132,-8.466130,-7.792079,-4.761652,-9.148798,9.778576,-2.775709,3.047483,-5.313091,8.385738,0.355798,2.359906,9.826282,0.671742,-3.230482,2.503878,-9.143450,-8.935160,-3.389519,3.882422,-8.920369,-0.965330,8.279122,-3.846255,0.989381,1.740137,4.358852,5.642641,4.098588,0.947343,1.683666,2.244325,-2.168370,-4.394655,-9.852704,0.290916,-2.584511,-5.309384,1.156471,-3.851439,-5.047826,1.342564,-1.805826,-0.882100,0.428690,4.260062,-7.865247,-9.180441,-8.646045,3.668893,-2.197599,1.895183,-0.113715,-0.188472,1.032853,-0.163958,-2.845999,7.348583,-4.784206,8.858126,7.836363,-8.743493,0.847163,-1.488268,4.420595,5.338466,-6.860595,-6.294473,-7.179953,-8.451296,4.721090,6.708271,-6.724460,-6.812387,-3.273355,-3.060511,-1.875214,6.998166,-4.723547,-3.911000,8.553636,5.113888,-5.741189,-2.350002,1.913989,-1.936223,7.605973,-0.985793,8.710158,-3.447048,-3.733732,1.708519],[4.033693,4.360075,4.847049,6.671538,6.829486,-2.491912,-5.730680,-3.680262,-9.547067,6.880644,-5.540535,3.491849,-6.314395,8.750475,5.282786,-6.467905,1.233304,-9.782564,7.524203,9.445584,-2.000852,-1.257592,-0.840861,-2.134146,-2.139131,-4.045436,-9.913773,-8.817033,0.304288,2.919671,-4.473259,1.039898,8.057973,-9.358827,3.551944,9.061265,-5.711896,-4.708415,-4.224808,2.020598,-0.006458,2.189661,5.397447,-8.210111,3.800621,0.767843,5.363955,2.938396,-6.713403,8.280958,3.686676,-5.770491,-6.120339,-3.708147,3.856513,7.779294,7.197195,-8.045235,-1.127770,7.766620,2.165847,-4.014901,6.972019,6.013847,3.152952,4.599771,-4.804380,-6.583312,5.510696,4.325153,-7.893858,-6.623154,-4.107347,9.126774,8.934886,-4.892339,1.367302,7.051060,7.557337,9.455885,8.559386,3.774594,-3.687671,0.655071,9.646837,-6.405451,4.202683,3.830225,-6.429944,9.007718,-5.021710,-2.127592,-7.389722,-2.331253,-7.433455,-1.434484,4.480631,7.391097,-2.710339,2.152208,-8.901122,5.750878,-9.507004,7.225991,9.665776,2.124041,-8.486922,-3.518834,3.056940,-6.466496,-4.063418,-4.315579,0.394334,4.872255,-8.146828,5.235922,-8.184617,-8.616009,9.411772,0.867369,-3.621323,-5.941502,-3.008253,0.675894,-1.489798,-1.741620,9.224065,-3.727272,-4.325514,-9.562488,-9.764803,4.403337,-6.419962,7.831394,6.430231,1.197592,7.022401,5.625189,-9.822412,-8.016363,-0.360770,0.002018,9.214861,-9.954765,0.315062,-2.627132,-7.564691,-3.351761,6.098595,0.304782,0.944083,6.192282,-8.942562,-2.073329,8.817292,4.833645,3.740274,0.434713,-5.893405,0.751590,-3.036223,4.512789,5.520495,-1.969238,-0.851934,-5.544276,-9.231085,-0.054227,-3.619496,8.170786,9.665824,2.932189,9.931951,9.338140,1.785618,9.911332,-1.383279,-5.934947,-5.295563,4.038801,-2.293932,-4.738461,2.590718,-0.895544,-2.907735,7.563693,-7.497778,-2.872826,-5.952586,-0.947978,-8.844352,3.779913,-7.929564,4.445840,-0.149230],[0.820358,-7.858865,4.628816,2.022503,6.578771,4.102966,7.962532,9.522070,0.368518,-2.633860,3.514839,9.325900,3.147877,3.773171,8.357307,6.332901,-1.450053,-4.778294,2.178044,8.023338,3.129346,-3.529346,7.674555,7.458254,9.765091,-8.034149,-1.709607,3.993310,7.521810,-5.059988,0.590758,-0.356745,9.348111,7.273052,-6.894807,0.756056,-9.186220,-2.676076,-1.881420,-0.081701,0.722050,-2.970892,1.004428,-3.230303,-0.899624,3.105041,-7.080326,-0.044901,-9.227057,5.002499,-2.190476,5.904343,-7.516024,-3.890717,9.941862,-5.039531,5.466067,-2.630806,-0.303334,-9.026029,-7.584843,-1.832697,1.886784,-9.990490,1.057288,-0.683090,8.817513,-2.213299,0.677229,-4.786617,1.059752,-8.236454,6.403958,2.911614,5.466599,8.477103,5.005056,-8.178921,-6.021051,5.955589,-1.098079,2.366753,5.038529,4.321578,4.287672,0.723669,-1.832073,7.846334,-1.795531,-0.409177,-1.628725,1.366943,8.159137,-3.051567,8.567139,5.619219,8.722821,7.417479,-5.778059,-3.884969,-5.183152,0.506746,6.841936,-3.681984,3.071086,7.214193,-0.078368,-5.061045,-7.198729,4.451932,-3.642510,-6.177758,-3.680011,-3.448266,-3.001853,-0.806253,-6.008814,-5.190021,-4.634229,4.410566,2.329140,-3.338038,-5.394824,2.763119,7.101992,-5.887218,-5.133370,-7.165399,-0.399832,1.063417,2.338506,4.175797,1.821524,5.850588,-2.544933,-6.520007,2.352498,-7.884704,9.810781,-5.276562,-1.743017,-1.834300,9.407649,7.444283,5.768434,9.727268,-8.504059,-1.109170,-5.707543,-7.355244,-7.321577,-8.632007,6.576379,6.168373,-1.634177,3.093518,-9.986570,8.195557,-6.758078,5.628245,-7.361864,-8.553512,4.759404,-1.547599,-7.852520,8.303459,1.113566,-6.397326,-9.222588,9.226656,-9.404338,0.213094,-6.625530,-6.695091,-0.463419,-6.586753,-9.622360,3.887797,6.426401,9.739150,-2.120157,4.136035,-1.045282,-2.582799,7.824196,-6.447300,8.243800,9.015713,-4.668308,-4.933925,7.204409,7.364586,-2.159728,-1.406332,6.058906],[4.903488,-2.528998,4.284367,9.083642,0.863949,-7.492189,-4.126947,8.396881,1.215802,3.062648,-0.087529,6.524118,5.841395,8.054138,7.188930,1.049044,-7.375881,8.788477,3.228978,-3.723926,-3.247236,-3.991547,-7.143641,-3.503999,7.146733,1.462645,-6.633429,-9.733538,-2.042184,8.930173,-1.047242,7.942889,-7.651221,-6.966650,8.262340,-7.759600,4.693003,-2.283566,2.471803,-0.255141,-1.070220,-0.170899,-3.918759,-3.148905,-7.679564,-0.204250,8.436663,-8.508927,0.723298,9.587570,2.647782,-1.208654,-3.618466,-2.607878,8.517938,-0.277747,-0.059583,-8.183009,0.722995,-2.747277,5.774399,-8.794349,-4.554913,-3.806462,-8.916043,-6.489788,-6.292233,-4.913162,9.362304,-0.528473,0.741224,-5.501013,7.476962,-4.435996,-5.662324,8.179650,-5.579337,-0.387797,-3.245729,-6.476287,-6.434592,-5.824239,6.014483,5.338113,9.239901,9.707281,-2.986146,-1.785550,-5.720694,3.223781,8.375886,-0.790315,-6.110465,-6.937273,-5.951950,1.194257,5.264638,8.404332,2.466414,0.334602,-8.691214,1.888197,8.283465,-7.213648,0.469735,-3.972069,-2.083714,-6.632941,1.317858,1.607655,9.722856,-7.682741,-4.558703,4.967206,-3.209083,-4.899985,1.160775,3.758699,-5.448774,-1.888078,0.122005,-6.646374,-3.833967,4.689424,-8.631362,6.797577,5.470694,-2.611419,0.399001,2.954931,8.077551,-3.634397,-6.482428,1.443245,1.620596,-4.977531,-6.063710,0.563440,6.809900,-7.627164,2.426758,9.374458,3.804452,0.820547,2.168637,-5.526104,-2.341133,7.378690,-0.750415,4.518979,-9.116048,2.584807,3.328763,0.255827,5.155402,-3.786280,4.995189,9.195427,4.934009,5.146518,-2.544253,9.452532,-9.920588,9.968320,2.169593,2.141948,-6.268112,-3.952525,6.717401,-0.281321,1.188610,4.158079,-4.659895,1.478407,8.596310,-3.298015,-8.916307,6.497434,-9.150614,-4.095120,5.266619,7.741483,-3.411867,0.553153,-8.278510,-3.722172,-5.823554,-3.239415,-2.441462,9.603541,4.697891,5.139139,6.879414,-0.789628,2.173672]], dtype = "float32")#candidate|6688|(10, 195)|const|float32
var_6689 = relay.var("var_6689", dtype = "int64", shape = (450,))#candidate|6689|(450,)|var|int64
var_6690 = relay.var("var_6690", dtype = "int16", shape = (48,))#candidate|6690|(48,)|var|int16
var_6691 = relay.var("var_6691", dtype = "float64", shape = (480,))#candidate|6691|(480,)|var|float64
call_6687 = relay.TupleGetItem(func_2019_call(relay.reshape(const_6688.astype('float32'), [15, 13, 10]), relay.reshape(var_6689.astype('int64'), [150, 3]), relay.reshape(var_6690.astype('int16'), [4, 12]), relay.reshape(var_6691.astype('float64'), [8, 60]), relay.reshape(call_6664.astype('uint16'), [96, 2]), ), 0)
call_6692 = relay.TupleGetItem(func_2026_call(relay.reshape(const_6688.astype('float32'), [15, 13, 10]), relay.reshape(var_6689.astype('int64'), [150, 3]), relay.reshape(var_6690.astype('int16'), [4, 12]), relay.reshape(var_6691.astype('float64'), [8, 60]), relay.reshape(call_6664.astype('uint16'), [96, 2]), ), 0)
var_6695 = relay.var("var_6695", dtype = "int16", shape = (11, 7, 9))#candidate|6695|(11, 7, 9)|var|int16
bop_6696 = relay.subtract(var_6648.astype('float32'), relay.reshape(var_6695.astype('float32'), relay.shape_of(var_6648))) # shape=(11, 7, 9)
func_4168_call = mod.get_global_var('func_4168')
func_4173_call = mutated_mod.get_global_var('func_4173')
const_6700 = relay.const([[5.215072,5.838123,-3.741928]], dtype = "float32")#candidate|6700|(1, 3)|const|float32
const_6701 = relay.const([[0.427123,7.407992,-7.113630,2.506017,-1.972838,-5.246116,4.050446,3.516645,3.710718,5.509025,4.906696,-2.761211],[0.111104,-6.332199,4.290287,-7.419354,-7.616933,-5.465428,-2.863007,-7.286916,4.339424,5.717717,-7.826100,5.117054],[0.059792,-2.926397,2.132846,-2.156255,-1.038353,-1.613141,7.979873,8.781298,-6.461375,-5.968009,8.313702,-6.695152]], dtype = "float32")#candidate|6701|(3, 12)|const|float32
var_6702 = relay.var("var_6702", dtype = "float32", shape = (600,))#candidate|6702|(600,)|var|float32
call_6699 = relay.TupleGetItem(func_4168_call(relay.reshape(const_6700.astype('float32'), [1, 3]), relay.reshape(const_6701.astype('float32'), [12, 3]), relay.reshape(var_6702.astype('float32'), [600,]), ), 2)
call_6703 = relay.TupleGetItem(func_4173_call(relay.reshape(const_6700.astype('float32'), [1, 3]), relay.reshape(const_6701.astype('float32'), [12, 3]), relay.reshape(var_6702.astype('float32'), [600,]), ), 2)
func_6606_call = mod.get_global_var('func_6606')
func_6610_call = mutated_mod.get_global_var('func_6610')
var_6713 = relay.var("var_6713", dtype = "int32", shape = (390,))#candidate|6713|(390,)|var|int32
call_6712 = func_6606_call(relay.reshape(var_6713.astype('int32'), [3, 13, 10]), relay.reshape(var_6713.astype('int32'), [3, 13, 10]), )
call_6714 = func_6606_call(relay.reshape(var_6713.astype('int32'), [3, 13, 10]), relay.reshape(var_6713.astype('int32'), [3, 13, 10]), )
output = relay.Tuple([bop_6649,bop_6652,call_6658,const_6659,call_6664,var_6665,call_6680,const_6681,var_6682,call_6687,const_6688,var_6689,var_6690,var_6691,bop_6696,call_6699,const_6700,const_6701,var_6702,call_6712,var_6713,])
output2 = relay.Tuple([bop_6649,bop_6652,call_6660,const_6659,call_6666,var_6665,call_6683,const_6681,var_6682,call_6692,const_6688,var_6689,var_6690,var_6691,bop_6696,call_6703,const_6700,const_6701,var_6702,call_6714,var_6713,])
func_6724 = relay.Function([var_6647,var_6648,var_6665,var_6682,var_6689,var_6690,var_6691,var_6695,var_6702,var_6713,], output)
mod['func_6724'] = func_6724
mod = relay.transform.InferType()(mod)
mutated_mod['func_6724'] = func_6724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6724_call = mutated_mod.get_global_var('func_6724')
var_6726 = relay.var("var_6726", dtype = "int16", shape = ())#candidate|6726|()|var|int16
var_6727 = relay.var("var_6727", dtype = "int16", shape = (11, 7, 9))#candidate|6727|(11, 7, 9)|var|int16
var_6728 = relay.var("var_6728", dtype = "float32", shape = (48, 4))#candidate|6728|(48, 4)|var|float32
var_6729 = relay.var("var_6729", dtype = "int16", shape = (112, 4))#candidate|6729|(112, 4)|var|int16
var_6730 = relay.var("var_6730", dtype = "int64", shape = (450,))#candidate|6730|(450,)|var|int64
var_6731 = relay.var("var_6731", dtype = "int16", shape = (48,))#candidate|6731|(48,)|var|int16
var_6732 = relay.var("var_6732", dtype = "float64", shape = (480,))#candidate|6732|(480,)|var|float64
var_6733 = relay.var("var_6733", dtype = "int16", shape = (11, 7, 9))#candidate|6733|(11, 7, 9)|var|int16
var_6734 = relay.var("var_6734", dtype = "float32", shape = (600,))#candidate|6734|(600,)|var|float32
var_6735 = relay.var("var_6735", dtype = "int32", shape = (390,))#candidate|6735|(390,)|var|int32
call_6725 = func_6724_call(var_6726,var_6727,var_6728,var_6729,var_6730,var_6731,var_6732,var_6733,var_6734,var_6735,)
output = call_6725
func_6736 = relay.Function([var_6726,var_6727,var_6728,var_6729,var_6730,var_6731,var_6732,var_6733,var_6734,var_6735,], output)
mutated_mod['func_6736'] = func_6736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7078 = relay.var("var_7078", dtype = "int32", shape = (12, 12, 16))#candidate|7078|(12, 12, 16)|var|int32
var_7079 = relay.var("var_7079", dtype = "int32", shape = (12, 12, 16))#candidate|7079|(12, 12, 16)|var|int32
bop_7080 = relay.bitwise_and(var_7078.astype('int32'), relay.reshape(var_7079.astype('int32'), relay.shape_of(var_7078))) # shape=(12, 12, 16)
func_4168_call = mod.get_global_var('func_4168')
func_4173_call = mutated_mod.get_global_var('func_4173')
var_7087 = relay.var("var_7087", dtype = "float32", shape = (3,))#candidate|7087|(3,)|var|float32
const_7088 = relay.const([-5.919071,9.375029,-3.175488,-0.220456,5.747846,9.575182,4.750934,-1.818333,6.087913,7.327959,-1.030289,0.750127,0.752204,-2.479228,-7.454342,-0.398097,9.429944,-8.728371,-2.688752,2.010519,-4.189423,9.830007,6.359169,6.141971,-5.200421,3.019506,-6.036606,7.288681,4.675787,-7.979885,-4.377081,-0.639516,-1.425123,6.391821,-3.943919,-5.226319], dtype = "float32")#candidate|7088|(36,)|const|float32
const_7089 = relay.const([[-0.608174,-7.506313,7.248828,-3.594891,-5.731994,-5.300939,6.286090,2.760981,9.165923,-1.749372,0.954148,8.477295,-2.843845,8.825475,4.407726,-1.767569,-6.322121,6.759509,1.950240,-1.757809,-8.598901,-5.853589,1.394961,4.670060,-9.031429,-2.508343,-7.304384,0.725601,-7.383507,4.103691,-5.857376,6.382549,0.197035,9.935754,7.599529,-2.810451,-0.895696,3.409552,1.756676,-5.326831,0.908113,2.587391,-1.005380,-8.764445,2.793263,-2.899976,4.494037,-6.632991,6.111170,2.717250,3.883922,-9.788980,-9.126920,-9.496178,-4.889162,8.184594,6.300015,-6.413100,-2.381720,-6.414757,-4.594798,0.917736,1.643159,-8.940329,0.718478,6.303488,-3.946507,2.896440,7.101414,-6.522444,-9.508310,7.384451,-8.515539,-6.178067,-4.690613,-5.552093,1.091410,-3.133712,5.719135,8.000199,-4.869383,8.644697,-8.895026,-3.748272,-0.231720,-2.859342,-2.633422,-4.784524,4.639022,7.109799,-7.441095,-8.675612,-3.715861,-9.707832,-1.003840,-0.620472,-7.943728,7.622958,-3.875680,-3.354080],[-2.771874,-5.745519,1.838639,0.373406,3.509635,-9.822962,-3.658336,2.428160,-7.333873,-7.048869,-8.927402,0.039510,-5.337637,5.514391,-9.007621,-8.526417,-1.320579,-0.696277,9.280940,-6.504236,-5.498462,-3.561390,-0.164119,6.418159,2.394403,5.459929,8.301019,-9.197129,0.518280,-6.136192,-0.667328,-0.465662,5.112979,-2.119955,-7.512095,9.981448,2.337130,0.707668,-3.464735,-2.229309,-4.043111,0.904669,1.984952,0.201461,1.351208,-6.159499,-8.443182,1.914647,3.135203,6.298969,-8.977807,0.116976,-9.484349,3.696056,8.300951,8.831086,5.153585,3.298325,-9.775135,4.973122,9.870988,6.293097,-1.690309,3.120752,-6.611227,1.305484,-7.437396,3.180295,2.466912,4.449153,-5.305294,-1.413110,6.571416,-5.800277,6.641334,1.367449,-9.979391,-4.749914,4.038789,-5.927878,-0.761780,6.840235,-9.390442,-9.553863,9.818270,2.087349,-5.198375,-9.789001,4.809591,6.746405,-0.860156,9.022634,-2.885755,-4.637282,-7.525058,1.964336,-3.698665,0.328391,7.597455,9.718383],[3.440364,3.912022,-5.808620,4.969518,-4.335976,-8.187251,6.586509,9.377967,-0.882310,-1.199947,0.889678,0.602775,-1.491709,-1.998977,-8.123310,-5.729002,-7.438888,9.796491,0.328887,3.693619,-7.101034,3.454075,3.895942,0.467676,-1.350492,-7.973018,8.743438,2.352853,-9.502365,-0.259181,7.788924,-0.346191,-4.651969,7.280301,-8.527402,7.629464,-3.833944,2.914365,-4.775630,8.558341,-6.744770,-1.415741,-8.384298,1.483339,7.869747,3.147412,-5.585823,7.325574,-7.800005,0.475792,3.238212,3.754088,1.351792,7.744235,8.133865,-6.126466,2.733603,4.926741,-0.353146,-1.761121,-4.940556,0.116590,-5.304721,7.539966,5.460411,6.190368,-8.211804,-6.265445,5.152326,1.816865,8.543401,-6.846094,-6.573097,-1.178024,-3.304563,-4.665100,-3.944505,-6.862904,-9.793516,9.777234,-8.662414,-5.565974,5.197175,-1.492217,0.934654,5.560684,1.753903,7.662090,-7.048423,-0.871385,-9.261257,0.582950,-2.429410,4.535160,-1.494405,-8.931603,-0.323126,8.020920,-0.658965,-3.686208],[2.411583,-4.312076,-1.379506,-8.160317,5.233221,2.397948,4.266998,-9.214345,-6.231372,9.149760,4.761294,4.375377,-9.178099,7.670867,-3.510652,-4.529799,-3.083262,-2.073510,-7.415945,5.181182,-6.027858,-3.210868,0.277579,3.623593,-9.496907,-3.755812,4.718785,1.156177,-3.760691,-3.981321,1.729176,-7.542084,0.107975,-1.861913,3.800632,3.335169,-0.336110,-3.695566,-0.217825,-3.804341,-7.854690,-0.187245,-6.223992,8.590011,8.893808,-7.664672,5.809387,-9.600348,8.592682,-7.182052,-8.062816,-7.880558,8.059094,-5.603923,7.041973,7.058777,-1.385954,5.719919,6.317543,2.905655,-4.059730,5.928397,1.650256,-9.022564,-0.236275,1.456339,-2.221055,-6.311825,-4.859687,8.693089,7.351034,7.912167,9.670282,-5.670911,-4.098206,6.266410,1.506841,-3.772177,-1.781676,-5.469865,2.646580,2.576597,4.147471,-1.744047,-8.821011,6.157320,-6.199563,6.406647,6.650258,-2.396543,-2.794336,-5.574309,6.302283,-6.478224,9.622888,-1.861857,-4.782318,-7.233128,5.947946,-4.851766],[0.192809,0.929116,-9.038065,8.159417,4.792381,4.944477,9.456616,3.084767,-7.621441,-8.625019,-9.534600,7.547268,-7.469436,5.160624,-5.163827,8.349316,2.796326,3.575775,-9.911944,-0.772542,-9.430027,2.644185,7.850059,-3.834764,-4.742131,-9.746057,-3.775080,7.140530,2.225622,-1.190985,-6.330427,8.365139,5.584266,-5.577244,8.383220,1.142581,-9.118467,1.141898,7.276702,-2.517603,-8.408721,7.654890,-4.249224,9.400742,8.305889,8.238610,-8.289631,7.199565,9.544700,8.430016,-2.281024,-0.878073,9.784685,0.898128,-6.210292,-5.093494,-7.817333,3.720523,-3.000947,-0.421634,-2.494059,-6.455648,8.552060,-0.555997,6.925116,0.304369,-3.359842,-1.200102,-9.290953,5.145131,9.319896,7.510966,8.337312,-6.690441,-5.142002,8.368327,-8.765988,1.750437,5.874710,-9.111388,4.010291,1.139763,-4.179363,8.189987,0.762657,7.208494,-0.519540,-0.059018,5.127696,8.229393,3.866829,-4.325558,-7.467461,9.108173,-7.483934,-9.860295,-6.692228,9.237428,-6.615925,3.988655],[8.418199,-5.497776,7.288775,5.003019,-8.396487,-0.159081,9.801245,8.409042,-6.021515,-1.795624,7.409776,-5.723066,-4.748144,-0.976840,-8.856695,-7.592545,-4.599602,2.615745,2.876823,-6.099560,-2.179934,5.696131,5.073352,4.465457,-1.529016,-3.411933,0.892609,3.780211,2.017171,-2.511554,1.728358,7.714424,7.047702,3.139583,-7.078479,-1.145209,5.061553,-3.465032,0.299438,-7.099247,6.759061,7.981512,-3.503462,-3.302747,-6.444886,8.326295,9.297747,5.876642,-3.955602,4.605940,-6.310631,7.458264,-2.388636,-1.365779,7.846472,6.072552,-0.562825,1.944291,7.041475,-2.716891,-0.267968,8.080387,-2.892263,9.965257,6.378328,6.328713,-3.807551,5.682837,7.479573,-7.138176,2.880010,4.520428,-1.775651,-6.989298,5.537624,3.008210,-0.596256,2.087389,3.080949,9.996517,-1.310135,-0.380452,5.583468,5.662027,-8.203772,-7.194216,2.431015,2.071856,-4.644401,4.940754,-2.885902,-7.599456,7.238390,8.201206,-5.816844,3.815535,-9.711030,5.576282,-7.664603,-7.935955]], dtype = "float32")#candidate|7089|(6, 100)|const|float32
call_7086 = relay.TupleGetItem(func_4168_call(relay.reshape(var_7087.astype('float32'), [1, 3]), relay.reshape(const_7088.astype('float32'), [12, 3]), relay.reshape(const_7089.astype('float32'), [600,]), ), 1)
call_7090 = relay.TupleGetItem(func_4173_call(relay.reshape(var_7087.astype('float32'), [1, 3]), relay.reshape(const_7088.astype('float32'), [12, 3]), relay.reshape(const_7089.astype('float32'), [600,]), ), 1)
output = relay.Tuple([bop_7080,call_7086,var_7087,const_7088,const_7089,])
output2 = relay.Tuple([bop_7080,call_7090,var_7087,const_7088,const_7089,])
func_7101 = relay.Function([var_7078,var_7079,var_7087,], output)
mod['func_7101'] = func_7101
mod = relay.transform.InferType()(mod)
var_7102 = relay.var("var_7102", dtype = "int32", shape = (12, 12, 16))#candidate|7102|(12, 12, 16)|var|int32
var_7103 = relay.var("var_7103", dtype = "int32", shape = (12, 12, 16))#candidate|7103|(12, 12, 16)|var|int32
var_7104 = relay.var("var_7104", dtype = "float32", shape = (3,))#candidate|7104|(3,)|var|float32
output = func_7101(var_7102,var_7103,var_7104,)
func_7105 = relay.Function([var_7102,var_7103,var_7104,], output)
mutated_mod['func_7105'] = func_7105
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7327 = relay.var("var_7327", dtype = "float32", shape = (1, 6, 14))#candidate|7327|(1, 6, 14)|var|float32
uop_7328 = relay.tan(var_7327.astype('float32')) # shape=(1, 6, 14)
output = relay.Tuple([uop_7328,])
output2 = relay.Tuple([uop_7328,])
func_7334 = relay.Function([var_7327,], output)
mod['func_7334'] = func_7334
mod = relay.transform.InferType()(mod)
var_7335 = relay.var("var_7335", dtype = "float32", shape = (1, 6, 14))#candidate|7335|(1, 6, 14)|var|float32
output = func_7334(var_7335)
func_7336 = relay.Function([var_7335], output)
mutated_mod['func_7336'] = func_7336
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7631 = relay.var("var_7631", dtype = "float64", shape = (11, 8, 16))#candidate|7631|(11, 8, 16)|var|float64
uop_7632 = relay.sigmoid(var_7631.astype('float64')) # shape=(11, 8, 16)
func_3832_call = mod.get_global_var('func_3832')
func_3835_call = mutated_mod.get_global_var('func_3835')
var_7636 = relay.var("var_7636", dtype = "float32", shape = ())#candidate|7636|()|var|float32
var_7637 = relay.var("var_7637", dtype = "float32", shape = (2, 96))#candidate|7637|(2, 96)|var|float32
call_7635 = relay.TupleGetItem(func_3832_call(relay.reshape(var_7636.astype('float32'), []), relay.reshape(var_7637.astype('float32'), [3, 16, 4]), ), 0)
call_7638 = relay.TupleGetItem(func_3835_call(relay.reshape(var_7636.astype('float32'), []), relay.reshape(var_7637.astype('float32'), [3, 16, 4]), ), 0)
bop_7646 = relay.equal(var_7637.astype('bool'), relay.reshape(call_7635.astype('bool'), relay.shape_of(var_7637))) # shape=(2, 96)
bop_7649 = relay.equal(var_7637.astype('bool'), relay.reshape(call_7638.astype('bool'), relay.shape_of(var_7637))) # shape=(2, 96)
func_1737_call = mod.get_global_var('func_1737')
func_1740_call = mutated_mod.get_global_var('func_1740')
const_7653 = relay.const([2.413243,-2.071009,8.791106,6.453770,8.766370,2.520148,-1.892950,1.369886,1.723917,-7.058529,4.021385,8.664938,-1.557098,6.610313,-8.841300,8.393378,-7.493245,4.852339,4.428282,-2.053252,-2.112815,2.921337,-7.613901,-4.268110,0.837152,4.915385,-4.527294,8.634799,0.370128,-6.492225,-3.390514,5.511705,-4.204269,-6.547562,6.089857,-8.569154,-1.400659,9.615940,-2.433615,5.307727,-7.763148,9.165731,2.750244,7.057524,9.961089,8.433565,-6.422802,-7.962591,2.636637,-7.612118,-0.346535,-6.351847,8.599698,8.787080,4.222340,7.144656,-0.366619,-3.776827,7.431590,-1.906149,-2.936791,8.514398,6.734310,4.057058,-0.454047,8.091448,-7.161310,-1.121158,2.581157,-2.082654,-0.379295,-1.987273,-4.024032,-6.102199,6.706027,-7.190803,-1.038287,-6.345064,-1.656034,-8.229588,9.800543,1.822038,7.347059,8.238694,5.721546,-6.420976,-4.754648,-0.994989,6.326935,-2.677901,-2.157798,-5.046553,-8.434478,-0.164810,-4.946741,-7.000293,-8.495362,-7.992446,1.248340,4.062457,1.248770,-1.351802,-5.133092,-3.602169,7.683836,-8.795924,7.180908,6.206945,7.234838,-1.200781,-7.921065,-0.844344,-8.807252,7.799388,-0.518470,4.595566,-3.096711,2.308262,-1.392243,-4.814876,4.308322,5.839636,-5.285913,-9.552447,-8.396148,9.362138,3.338130,-1.243432,-5.313288,2.203688,-6.890655,-6.899766,-5.534529,7.264612,9.065627,1.748984,5.510945,-0.228762,4.496076,8.710238,8.973778,-3.395629,-7.204783,8.699110,-5.090099,-7.901036,0.160992,8.320587,-3.978951,-9.709500,4.313376,-5.491552,7.968044,-6.759252,-1.824673,-8.157772,-3.996168,-9.142624,0.804557,-2.127371,8.244589,-6.112332,4.109185,-0.369209,5.930557,-7.143968,-3.552595,5.152804,7.479062,-6.071023,9.231633,9.689152,-0.736143,4.803832,2.056731,8.594622,-9.032760,9.973884,-3.355915,0.190460,5.578753,-1.625885,5.146813,7.193884,9.764770,-3.371961,-6.703093,-6.453725,1.685499,4.840247,6.480590,5.322462,-8.474519,-0.950133,6.329017,-3.587728,7.801827,-2.606389,-0.005101,8.010357,-1.598322,9.659629,4.478056,8.422101,1.287042,-1.861607,3.484555,-5.608995,-0.808424,-8.051248,-0.125425,-5.512794,5.177815,-0.229144,-3.042420,6.015113,1.420150,-5.510229,4.391714,-6.102366,-7.628689,5.180435,-1.910204,2.298565,-8.426537,-3.360634,2.025089,-1.891988,-4.790022,-2.442318,-3.571445,9.936350,-5.757281,6.798653,3.109760,-2.721970,-2.240060,6.318920,2.405330,0.852034,5.919970,0.546885,8.601845,3.551863,-5.906084,-8.020761,-5.558633,1.388864,7.297096,-1.193759,-9.519891,-5.051875,-6.840714,1.842631,5.385528,-1.594955,2.010129,2.916587,2.947164,-6.773523,-3.670906,2.261252,-6.050750,-0.305345,0.493378,-6.666819,6.619971,-8.272991,-0.816261,-8.869441,-4.881722,-4.155924,-2.567152,-7.465739,6.950480,3.854526,-1.288469,-8.878942,9.789259,-6.030943,9.816225,-2.790420,-1.262358,-0.274728,0.746078,-9.865772,5.969375,3.781515,-4.374314,-1.940829,-9.946930,3.052316,-9.682329,3.679637,-7.493061,-8.235228,-1.037418,2.829453,1.273141,1.534310,-9.260380,-3.701666,3.006977,3.635704,-5.510295,6.124203,7.314461,9.691045,-4.275512,-0.197266,-4.357983,-4.194249,9.879685,7.532740,3.628535,1.759575,-4.905647,-4.397192,8.703788,0.357458,5.242258,-9.130954,-6.948370,-2.214457,-0.371971,8.947052,9.404278,0.425134,3.756792,1.748477,-1.184409,-8.187513,-8.692862,-4.446746,-3.896836,5.167551,-7.433882,7.561710,6.408868,2.937614,-5.119494,4.381645,-8.630359,-2.974736,9.605957,-2.623974,8.206281,4.188348,4.111986,1.506008,5.742582,5.317007,6.473192,-0.218487,-9.242792,-9.866693,7.065993,-4.553838,2.665933,6.004005,-5.425490,-6.669802,6.674873,-5.703305,0.183918,-8.687277,-8.129297,-6.167630,-2.388472,1.384612,-3.890679,2.660492,9.287214,7.632375,4.256106,2.792508,-9.380797,2.063617,7.003546,6.227936,8.236489,-1.710424,6.628610,0.439245,7.753741,9.718393,4.229172,0.278535,-1.719374,5.934733,-0.120966,-3.452419,-3.018449,-5.156101,6.915106,-8.404472,0.830379,-2.655095,4.117960,9.486585,-7.117569,-2.475772,8.111478,-1.384659,-4.393074,1.267610,0.208520,6.156631,8.432647,6.561665,6.867100,-0.787558,-6.660623,-0.711133,-3.140972,4.990128,-5.665027,-7.193101,1.503890,7.205229,-1.001692,-1.681536,-6.839574,3.947744,5.567535,-6.356969,-6.652316,-7.699034,-7.771696,-7.375925,-8.197838,3.152328,8.537692,-6.524096,2.555317,-9.156635,6.479589,0.906881,7.951433,1.158482,3.276134,7.160198,-0.805785,4.054195,-6.291573,-6.132047,8.986380,8.112613,7.349361,2.769759,-4.873104,6.163503,4.082861,3.463090,7.631725,2.787682,9.156829,6.103802,-3.362646,-0.010411,-7.638445,2.507233,-7.064232,9.989492,5.526348,-8.320229,-0.652458,7.688543,-7.182352,-7.379009,1.841717,7.120385,3.328623,1.516578,0.190230,-9.263820,-2.192085,8.920022,5.725776,-2.222180,2.890706,-9.189526,-8.656017,5.329724,-9.092026,9.165302,-6.859519,-2.349441,8.853757,5.976480,8.948340,-6.177419,-8.028336,4.285060,-6.968686,-5.381327,-3.061672,-7.249007,-4.828176,-3.079489,8.886797,-9.354085,-8.126637,4.421159,-2.232609,-2.227023,0.146069,7.490949,-5.424256,5.065564,5.716376,-1.124780,-2.812247,-3.467718,3.894485,9.035331,-0.225547,-7.605974,4.579284,-8.676181,-2.929277,1.087390,-8.190128,2.262554,0.337482,3.143759,-9.699052,1.854835,-8.691967,7.008320,-9.816769,8.533991,8.945799,5.551262,9.512504,-3.543099,-3.120324,8.139652,0.846282,9.738948,6.544749,6.948710,-3.093302,-0.280389,-1.390825,-5.499544,8.117517,-1.237746,8.454718,4.983372,3.606849,4.059727,3.872389,-3.157075,9.069745,-7.055217,0.949344,8.958141,-0.542108,-2.352640,5.843392,3.326181,-0.448776,6.285077,1.513917,6.946912,4.879379,-9.765314,1.416691,8.847994,-7.850709,-3.790952,1.155546,9.836211,2.010467,-3.957094,1.863997,1.866039,5.476645,8.898480,3.828166,-3.052852,0.075038,-1.645274,4.206169,-6.710183,0.995850,9.235964,-8.826377,-6.827742,3.455061,-8.564011,-8.414884,-4.188624,6.307306,-9.423214,-8.984661,2.462141,1.448057,3.584813,2.402121,-5.797527,-8.802106,3.775965,-0.466517,-5.045173,-1.527782,-1.361142,6.366197,0.246047,1.158332,4.162780,-7.096374,5.245227,-2.580670,-0.227189,-8.960096,-8.163324,7.987398,6.562537,8.011578,0.052276,8.465939,-5.086951,-9.734889,5.250967,5.444897,-9.795866,5.787521,5.429049,-8.225434,9.356784,-0.104256,8.717105,7.114577,-3.069831,-6.130133,-8.835466,0.263690,-9.712650,-3.264110,9.802882,6.172433,9.857636,-1.579880,-7.862231,3.174849,9.786531,-1.081192,1.292256,-2.455215,-5.715662,3.465156,-3.554602,-5.551077,-8.969993,-9.974314,-1.043472,4.533152,-8.901621,4.803031,-1.259949,-4.442940,-9.527083,-7.940798,-3.710224,4.604033,-9.965732,7.569075,-6.356767,4.426115,8.757406,-1.588605,3.934431,1.762215,3.913803,2.198313,3.828080,-6.195024,-9.649915,4.253929,6.934522,2.318317,4.578241,-4.932130,-3.442861,0.511683,9.227641,-3.087948,4.696346,-2.941117,-4.885915,4.843318,7.596679,2.390257,-6.552445,-8.496073,-1.836944,6.563840,-5.809372,7.235601,-6.398993,-7.457853,-5.647027,-7.963116,2.181412,2.743413,-6.429485,7.997317,-0.451779,4.920275,-9.783382,-4.289803,-8.441449,-9.289419,5.919804,6.701302,-4.191156,0.101652,-6.830801,9.632332,-1.133626,3.327795,6.225778,-0.326586,-8.044133,-1.534572,5.867114,4.594714,4.103604,-9.952132,6.073493,-4.680189,-1.432104,-7.999591,5.817451,-0.031305,-9.662155,7.927006,-6.322388,6.698247,7.438679,9.769833,-9.075837,-3.198587,0.453026,-3.503795,5.236595,-4.649970,-6.354237,-8.076454,-2.284890,9.566882,2.696685,-6.512875,-0.877529,-3.207061,-0.084121,-8.225926,-1.292974,-0.078009,-4.084247,-6.233340,5.647865,1.716267,4.021384,7.111514,-2.499370,4.021369,3.163840,5.825569,0.970730,-8.763260,-7.526051,5.597787,4.053858,-2.299242,-7.250161,0.278517,3.406265,-4.605354,5.604137,3.852556,-8.572536,0.665817,-0.991235,-9.694135,-9.240670,3.344702,8.453480,6.783854,-5.275222,-8.476037,-1.056100,-3.686876,-5.476325,-3.897550,1.243783,3.604664,-7.768121,6.794284,-8.243346,3.208489,-7.992028,5.379111,5.967364,3.506187,-9.266067,-3.423326,0.471614,-7.509470,9.212571,9.668406,-8.723364,2.808268,7.519373,-9.680764,-4.561929,-4.688785,-4.282403,-7.617395,-6.770308,-6.633489,-2.318410,4.194283,6.286485,3.581945,3.369707,1.890423,-3.122473,-3.473748,-9.168266,4.173837,-7.270275,7.498349,2.509487,-4.410923,2.799615,-4.344148,-1.100753,-7.840117,1.616362,-8.474573,-1.287204,7.894210,-2.210718,1.991974,-8.680995,2.798777,-7.065006,4.019624,1.397748,-1.727654,-8.829227,-2.206651,-5.378123,5.495621,-1.240795,-6.652899,4.523774,0.345426,-9.344109,-7.248851,5.150422,0.893208,6.059547,8.621969,7.400142,2.882878,-9.992067,-9.570885,-1.872440,6.761780,5.371851,-9.434286,4.244662,8.717345,-6.228773,-0.849017,9.235623,2.335420,-5.144647,1.249051,-8.892396,-4.599507,-1.255696,-1.127990,-2.067148,-9.957688,0.341904,-3.970383,-9.333981,-9.389322,-0.499383,1.893093,3.258242,-0.124466,0.174951,3.043598,-6.288642,9.538751,-1.075314,-0.644466,7.116959,-0.171303,8.145889,7.137295,-7.128904,-4.429112,-4.758660,6.565959,-9.897462,8.522828,6.067707,-8.950003,-4.310019,7.896342,9.807873,1.720931,-5.379931,3.512205,1.345014,1.726445,2.682758,-3.349204,9.750231,7.528835,7.507892,-4.239973,3.162873,-1.550160,-2.532072,-1.857999,0.536961,-7.394102,5.026871,4.202944,-6.340578,1.869121,-7.639617,3.951617,9.616118,-9.302705,2.576779,0.005773,1.800517,3.284756,0.040560,1.788218,2.117923,-7.775889,0.006034,0.440583,7.087587,9.644319,-2.684484,1.085814,3.683761,-6.946301,-9.508856,2.827930,-3.936771,3.972977,-4.590037,-4.588288,-4.257543,3.106629,4.777548,8.575254,7.806238,-0.119186,4.583888,5.959724,3.649939,-5.490810,1.502606,0.187337,-4.773679,-5.064740,0.092452,-1.380637,3.040304,-3.869867,1.266323,1.017449,-1.355567,-7.247222,-9.339712,4.574351,-8.217979,9.013847,7.861110,1.185515,-4.309804,8.172975,-9.715833,0.572588,3.752323,-9.626634,-1.360922,3.054330,-2.257179,-7.552395,0.625224,-4.585692,9.663062,8.339531,4.446753,-4.327100,-2.698724,7.810567,-4.849191,4.984904,-0.945993,-1.168020,4.380169,-2.052848,0.024742,-8.230815,-9.844004,-0.656935,8.563578,-9.671239,-7.610131,-7.937030,-2.287202,-0.787027,-5.899466,-2.287325,2.711248,5.767444,-7.173969,-8.092134,7.609165,-5.033433,-6.029280,5.398276,6.220908,-1.275829,4.416562,-8.809656,-5.189165,-4.454087,-6.135840,-0.933818,5.327502,3.345557,2.527546,9.375431,-4.699794,-5.442069,7.491281,-5.769257,2.339212,-9.547435,8.963860,8.167002,3.608496,0.612989,-1.808253,-5.900829,9.957821,-0.996150,0.399370,2.218244,3.031636,-0.203374,-2.744338,2.080495,5.140107,-8.294238,0.465288,9.888016,3.991061,-9.854066,-1.474911,7.004520,-6.325851,-9.532044,0.448117], dtype = "float32")#candidate|7653|(1080,)|const|float32
call_7652 = relay.TupleGetItem(func_1737_call(relay.reshape(const_7653.astype('float32'), [8, 15, 9])), 2)
call_7654 = relay.TupleGetItem(func_1740_call(relay.reshape(const_7653.astype('float32'), [8, 15, 9])), 2)
output = relay.Tuple([uop_7632,var_7636,bop_7646,call_7652,const_7653,])
output2 = relay.Tuple([uop_7632,var_7636,bop_7649,call_7654,const_7653,])
func_7666 = relay.Function([var_7631,var_7636,var_7637,], output)
mod['func_7666'] = func_7666
mod = relay.transform.InferType()(mod)
var_7667 = relay.var("var_7667", dtype = "float64", shape = (11, 8, 16))#candidate|7667|(11, 8, 16)|var|float64
var_7668 = relay.var("var_7668", dtype = "float32", shape = ())#candidate|7668|()|var|float32
var_7669 = relay.var("var_7669", dtype = "float32", shape = (2, 96))#candidate|7669|(2, 96)|var|float32
output = func_7666(var_7667,var_7668,var_7669,)
func_7670 = relay.Function([var_7667,var_7668,var_7669,], output)
mutated_mod['func_7670'] = func_7670
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7705 = relay.var("var_7705", dtype = "float64", shape = (10, 9, 11))#candidate|7705|(10, 9, 11)|var|float64
var_7706 = relay.var("var_7706", dtype = "float64", shape = (10, 9, 11))#candidate|7706|(10, 9, 11)|var|float64
bop_7707 = relay.floor_mod(var_7705.astype('float64'), relay.reshape(var_7706.astype('float64'), relay.shape_of(var_7705))) # shape=(10, 9, 11)
output = bop_7707
output2 = bop_7707
func_7710 = relay.Function([var_7705,var_7706,], output)
mod['func_7710'] = func_7710
mod = relay.transform.InferType()(mod)
mutated_mod['func_7710'] = func_7710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7710_call = mutated_mod.get_global_var('func_7710')
var_7712 = relay.var("var_7712", dtype = "float64", shape = (10, 9, 11))#candidate|7712|(10, 9, 11)|var|float64
var_7713 = relay.var("var_7713", dtype = "float64", shape = (10, 9, 11))#candidate|7713|(10, 9, 11)|var|float64
call_7711 = func_7710_call(var_7712,var_7713,)
output = call_7711
func_7714 = relay.Function([var_7712,var_7713,], output)
mutated_mod['func_7714'] = func_7714
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8594 = relay.var("var_8594", dtype = "float32", shape = (16, 15, 13))#candidate|8594|(16, 15, 13)|var|float32
uop_8595 = relay.sin(var_8594.astype('float32')) # shape=(16, 15, 13)
func_4254_call = mod.get_global_var('func_4254')
func_4258_call = mutated_mod.get_global_var('func_4258')
var_8617 = relay.var("var_8617", dtype = "uint8", shape = (384, 1))#candidate|8617|(384, 1)|var|uint8
var_8618 = relay.var("var_8618", dtype = "int64", shape = ())#candidate|8618|()|var|int64
var_8619 = relay.var("var_8619", dtype = "int64", shape = (20, 120))#candidate|8619|(20, 120)|var|int64
call_8616 = relay.TupleGetItem(func_4254_call(relay.reshape(var_8617.astype('uint8'), [6, 4, 16]), relay.reshape(var_8618.astype('int64'), []), relay.reshape(var_8619.astype('int64'), [2400,]), ), 1)
call_8620 = relay.TupleGetItem(func_4258_call(relay.reshape(var_8617.astype('uint8'), [6, 4, 16]), relay.reshape(var_8618.astype('int64'), []), relay.reshape(var_8619.astype('int64'), [2400,]), ), 1)
uop_8640 = relay.acos(uop_8595.astype('float32')) # shape=(16, 15, 13)
func_4877_call = mod.get_global_var('func_4877')
func_4884_call = mutated_mod.get_global_var('func_4884')
const_8648 = relay.const([[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[True],[False],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[True],[False],[True],[False]], dtype = "bool")#candidate|8648|(240, 1)|const|bool
var_8649 = relay.var("var_8649", dtype = "float32", shape = (750,))#candidate|8649|(750,)|var|float32
var_8650 = relay.var("var_8650", dtype = "int16", shape = (48,))#candidate|8650|(48,)|var|int16
call_8647 = relay.TupleGetItem(func_4877_call(relay.reshape(const_8648.astype('bool'), [10, 4, 6]), relay.reshape(const_8648.astype('bool'), [10, 4, 6]), relay.reshape(var_8649.astype('float32'), [50, 15]), relay.reshape(var_8650.astype('int16'), [48,]), relay.reshape(const_8648.astype('bool'), [10, 4, 6]), ), 0)
call_8651 = relay.TupleGetItem(func_4884_call(relay.reshape(const_8648.astype('bool'), [10, 4, 6]), relay.reshape(const_8648.astype('bool'), [10, 4, 6]), relay.reshape(var_8649.astype('float32'), [50, 15]), relay.reshape(var_8650.astype('int16'), [48,]), relay.reshape(const_8648.astype('bool'), [10, 4, 6]), ), 0)
uop_8654 = relay.log(uop_8595.astype('float64')) # shape=(16, 15, 13)
output = relay.Tuple([call_8616,var_8617,var_8618,var_8619,uop_8640,call_8647,const_8648,var_8649,var_8650,uop_8654,])
output2 = relay.Tuple([call_8620,var_8617,var_8618,var_8619,uop_8640,call_8651,const_8648,var_8649,var_8650,uop_8654,])
func_8669 = relay.Function([var_8594,var_8617,var_8618,var_8619,var_8649,var_8650,], output)
mod['func_8669'] = func_8669
mod = relay.transform.InferType()(mod)
var_8670 = relay.var("var_8670", dtype = "float32", shape = (16, 15, 13))#candidate|8670|(16, 15, 13)|var|float32
var_8671 = relay.var("var_8671", dtype = "uint8", shape = (384, 1))#candidate|8671|(384, 1)|var|uint8
var_8672 = relay.var("var_8672", dtype = "int64", shape = ())#candidate|8672|()|var|int64
var_8673 = relay.var("var_8673", dtype = "int64", shape = (20, 120))#candidate|8673|(20, 120)|var|int64
var_8674 = relay.var("var_8674", dtype = "float32", shape = (750,))#candidate|8674|(750,)|var|float32
var_8675 = relay.var("var_8675", dtype = "int16", shape = (48,))#candidate|8675|(48,)|var|int16
output = func_8669(var_8670,var_8671,var_8672,var_8673,var_8674,var_8675,)
func_8676 = relay.Function([var_8670,var_8671,var_8672,var_8673,var_8674,var_8675,], output)
mutated_mod['func_8676'] = func_8676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8678 = relay.var("var_8678", dtype = "float64", shape = (1, 16, 6))#candidate|8678|(1, 16, 6)|var|float64
uop_8679 = relay.asinh(var_8678.astype('float64')) # shape=(1, 16, 6)
output = uop_8679
output2 = uop_8679
func_8684 = relay.Function([var_8678,], output)
mod['func_8684'] = func_8684
mod = relay.transform.InferType()(mod)
mutated_mod['func_8684'] = func_8684
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8685 = relay.var("var_8685", dtype = "float64", shape = (1, 16, 6))#candidate|8685|(1, 16, 6)|var|float64
func_8684_call = mutated_mod.get_global_var('func_8684')
call_8686 = func_8684_call(var_8685)
output = call_8686
func_8687 = relay.Function([var_8685], output)
mutated_mod['func_8687'] = func_8687
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8766 = relay.const(-3.882042, dtype = "float64")#candidate|8766|()|const|float64
var_8767 = relay.var("var_8767", dtype = "float64", shape = (10, 12, 11))#candidate|8767|(10, 12, 11)|var|float64
bop_8768 = relay.mod(const_8766.astype('float64'), var_8767.astype('float64')) # shape=(10, 12, 11)
func_8684_call = mod.get_global_var('func_8684')
func_8687_call = mutated_mod.get_global_var('func_8687')
const_8805 = relay.const([[3.793226,-4.552365,-5.968702,-9.102001,4.532402,-3.476355],[8.248154,-3.066541,-1.709210,2.655254,-8.279871,7.485276],[-1.378495,-7.494895,8.104754,1.200675,9.782134,-3.915002],[0.088828,7.934755,-8.671058,7.115052,-9.339175,-9.165106],[6.985775,8.855128,4.221584,3.384285,7.798944,-6.377214],[7.903086,-4.605003,-7.761329,-1.020029,1.388319,-7.919884],[7.552750,3.436145,2.547249,-1.454981,8.516964,-8.370173],[2.688214,3.292546,9.020857,2.816666,8.333384,-9.191864],[0.517828,5.944824,-9.520223,-9.505257,-5.393212,6.176038],[8.185405,-5.914826,9.406086,-6.688266,-2.958681,-8.133144],[0.570956,-2.052631,5.882825,-4.655826,3.876731,2.380639],[-2.799980,-0.578643,2.633810,-3.748996,7.338960,-9.794081],[-1.816785,3.841534,-5.687215,-5.849215,-2.943933,-4.972653],[0.660341,-5.736844,-3.863722,3.666970,0.797039,5.764969],[2.664417,6.689942,-4.684610,-0.496092,-4.464539,-4.351731],[8.089210,0.027135,0.968903,4.945513,-3.310429,-6.560520]], dtype = "float64")#candidate|8805|(16, 6)|const|float64
call_8804 = func_8684_call(relay.reshape(const_8805.astype('float64'), [1, 16, 6]))
call_8806 = func_8684_call(relay.reshape(const_8805.astype('float64'), [1, 16, 6]))
output = relay.Tuple([bop_8768,call_8804,const_8805,])
output2 = relay.Tuple([bop_8768,call_8806,const_8805,])
func_8826 = relay.Function([var_8767,], output)
mod['func_8826'] = func_8826
mod = relay.transform.InferType()(mod)
var_8827 = relay.var("var_8827", dtype = "float64", shape = (10, 12, 11))#candidate|8827|(10, 12, 11)|var|float64
output = func_8826(var_8827)
func_8828 = relay.Function([var_8827], output)
mutated_mod['func_8828'] = func_8828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9083 = relay.var("var_9083", dtype = "float64", shape = (13, 10, 10))#candidate|9083|(13, 10, 10)|var|float64
uop_9084 = relay.tan(var_9083.astype('float64')) # shape=(13, 10, 10)
func_2019_call = mod.get_global_var('func_2019')
func_2026_call = mutated_mod.get_global_var('func_2026')
var_9088 = relay.var("var_9088", dtype = "float32", shape = (650, 3))#candidate|9088|(650, 3)|var|float32
const_9089 = relay.const([-8,-5,8,1,-9,-10,-7,-9,-10,-5,6,5,-8,4,8,-4,10,5,-5,5,-5,10,-1,-4,4,2,-5,-8,7,-8,-9,-9,-4,-8,1,4,-2,7,-5,-6,2,-1,-4,-9,10,6,-10,2,-1,4,6,9,2,1,1,-8,-3,2,-9,10,8,1,-3,3,-5,-10,-3,-9,9,4,-7,-4,3,-2,9,-2,-10,-9,7,-8,9,5,9,10,-6,-9,-7,5,-1,10,9,-10,-6,1,-1,10,-9,5,-1,-7,7,3,-8,-4,7,10,-8,6,-1,9,-8,-3,4,-6,-1,3,10,4,4,7,-3,-9,1,-5,2,4,3,-8,5,3,8,8,3,6,-1,1,3,-7,3,5,-7,5,8,8,-9,1,-8,7,-2,-1,7,-9,1,-5,9,10,-10,-8,10,2,-9,-1,4,10,-1,3,2,10,-9,8,4,-3,-6,-3,-7,8,-7,-6,-6,-1,7,7,-5,5,-2,1,4,10,-5,6,7,-9,-4,-9,1,-7,3,10,-1,-3,9,-6,-6,-2,-1,-2,-6,-7,5,-1,6,-5,-4,-7,1,5,-4,4,1,-10,4,-3,4,-3,5,-3,3,-10,-4,-1,8,4,9,1,-4,4,-4,10,-8,7,6,4,10,6,2,-9,-5,10,3,-6,4,-4,-9,-10,-7,10,-9,-3,-10,-4,-8,3,-8,-7,-6,-5,-5,3,-5,-10,-10,-6,-7,-9,-9,9,6,9,5,-2,-9,5,7,-7,-9,-3,-9,9,9,5,2,5,8,-1,-10,-7,-9,-2,-8,-9,7,-9,2,-4,-7,8,7,-7,-7,-9,9,-7,-8,-7,9,-5,-7,-3,-2,1,-10,-9,4,3,4,8,9,4,-4,4,-6,-10,-3,3,1,-7,6,-9,1,2,3,-9,-7,10,5,-7,-2,5,9,3,5,-3,5,9,-2,-3,3,9,-6,-3,2,-3,8,-2,-7,9,4,-3,3,-6,5,4,-1,9,-2,2,4,-10,3,-1,6,4,-3,-8,-9,3,-2,-1,10,4,-2,-7,2,-9,9,7,10,-7,8,-9,-8,8,-9,-6,-9,-2,7,-5,9,5,-4,5,-6,6,8,1,-10,-7,-8,-10,3,7,-3,10,8,2,-10,7,9,-7,1,-2,-7,-9,-4,-3,1,7,-2,-6,4,4,4,7,-5,2,-2,-6,-5,-5], dtype = "int64")#candidate|9089|(450,)|const|int64
var_9090 = relay.var("var_9090", dtype = "int16", shape = (48,))#candidate|9090|(48,)|var|int16
var_9091 = relay.var("var_9091", dtype = "float64", shape = (480,))#candidate|9091|(480,)|var|float64
var_9092 = relay.var("var_9092", dtype = "uint16", shape = (192, 1))#candidate|9092|(192, 1)|var|uint16
call_9087 = relay.TupleGetItem(func_2019_call(relay.reshape(var_9088.astype('float32'), [15, 13, 10]), relay.reshape(const_9089.astype('int64'), [150, 3]), relay.reshape(var_9090.astype('int16'), [4, 12]), relay.reshape(var_9091.astype('float64'), [8, 60]), relay.reshape(var_9092.astype('uint16'), [96, 2]), ), 0)
call_9093 = relay.TupleGetItem(func_2026_call(relay.reshape(var_9088.astype('float32'), [15, 13, 10]), relay.reshape(const_9089.astype('int64'), [150, 3]), relay.reshape(var_9090.astype('int16'), [4, 12]), relay.reshape(var_9091.astype('float64'), [8, 60]), relay.reshape(var_9092.astype('uint16'), [96, 2]), ), 0)
bop_9115 = relay.logical_xor(uop_9084.astype('int32'), relay.reshape(var_9083.astype('int32'), relay.shape_of(uop_9084))) # shape=(13, 10, 10)
func_8826_call = mod.get_global_var('func_8826')
func_8828_call = mutated_mod.get_global_var('func_8828')
var_9120 = relay.var("var_9120", dtype = "float64", shape = (1320,))#candidate|9120|(1320,)|var|float64
call_9119 = relay.TupleGetItem(func_8826_call(relay.reshape(var_9120.astype('float64'), [10, 12, 11])), 2)
call_9121 = relay.TupleGetItem(func_8828_call(relay.reshape(var_9120.astype('float64'), [10, 12, 11])), 2)
uop_9127 = relay.sigmoid(var_9092.astype('float32')) # shape=(192, 1)
output = relay.Tuple([call_9087,var_9088,const_9089,var_9090,var_9091,bop_9115,call_9119,var_9120,uop_9127,])
output2 = relay.Tuple([call_9093,var_9088,const_9089,var_9090,var_9091,bop_9115,call_9121,var_9120,uop_9127,])
func_9139 = relay.Function([var_9083,var_9088,var_9090,var_9091,var_9092,var_9120,], output)
mod['func_9139'] = func_9139
mod = relay.transform.InferType()(mod)
var_9140 = relay.var("var_9140", dtype = "float64", shape = (13, 10, 10))#candidate|9140|(13, 10, 10)|var|float64
var_9141 = relay.var("var_9141", dtype = "float32", shape = (650, 3))#candidate|9141|(650, 3)|var|float32
var_9142 = relay.var("var_9142", dtype = "int16", shape = (48,))#candidate|9142|(48,)|var|int16
var_9143 = relay.var("var_9143", dtype = "float64", shape = (480,))#candidate|9143|(480,)|var|float64
var_9144 = relay.var("var_9144", dtype = "uint16", shape = (192, 1))#candidate|9144|(192, 1)|var|uint16
var_9145 = relay.var("var_9145", dtype = "float64", shape = (1320,))#candidate|9145|(1320,)|var|float64
output = func_9139(var_9140,var_9141,var_9142,var_9143,var_9144,var_9145,)
func_9146 = relay.Function([var_9140,var_9141,var_9142,var_9143,var_9144,var_9145,], output)
mutated_mod['func_9146'] = func_9146
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9316 = relay.var("var_9316", dtype = "uint8", shape = (7, 10, 15))#candidate|9316|(7, 10, 15)|var|uint8
var_9317 = relay.var("var_9317", dtype = "uint8", shape = (7, 10, 15))#candidate|9317|(7, 10, 15)|var|uint8
bop_9318 = relay.greater_equal(var_9316.astype('bool'), relay.reshape(var_9317.astype('bool'), relay.shape_of(var_9316))) # shape=(7, 10, 15)
uop_9321 = relay.log(var_9317.astype('float64')) # shape=(7, 10, 15)
uop_9324 = relay.sqrt(var_9316.astype('float64')) # shape=(7, 10, 15)
func_4466_call = mod.get_global_var('func_4466')
func_4469_call = mutated_mod.get_global_var('func_4469')
var_9336 = relay.var("var_9336", dtype = "int32", shape = (112,))#candidate|9336|(112,)|var|int32
var_9337 = relay.var("var_9337", dtype = "int16", shape = (448,))#candidate|9337|(448,)|var|int16
call_9335 = relay.TupleGetItem(func_4466_call(relay.reshape(var_9336.astype('int32'), [14, 8]), relay.reshape(var_9337.astype('int16'), [448,]), ), 5)
call_9338 = relay.TupleGetItem(func_4469_call(relay.reshape(var_9336.astype('int32'), [14, 8]), relay.reshape(var_9337.astype('int16'), [448,]), ), 5)
output = relay.Tuple([bop_9318,uop_9321,uop_9324,call_9335,var_9336,var_9337,])
output2 = relay.Tuple([bop_9318,uop_9321,uop_9324,call_9338,var_9336,var_9337,])
func_9341 = relay.Function([var_9316,var_9317,var_9336,var_9337,], output)
mod['func_9341'] = func_9341
mod = relay.transform.InferType()(mod)
var_9342 = relay.var("var_9342", dtype = "uint8", shape = (7, 10, 15))#candidate|9342|(7, 10, 15)|var|uint8
var_9343 = relay.var("var_9343", dtype = "uint8", shape = (7, 10, 15))#candidate|9343|(7, 10, 15)|var|uint8
var_9344 = relay.var("var_9344", dtype = "int32", shape = (112,))#candidate|9344|(112,)|var|int32
var_9345 = relay.var("var_9345", dtype = "int16", shape = (448,))#candidate|9345|(448,)|var|int16
output = func_9341(var_9342,var_9343,var_9344,var_9345,)
func_9346 = relay.Function([var_9342,var_9343,var_9344,var_9345,], output)
mutated_mod['func_9346'] = func_9346
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9400 = relay.const([[[1,-1,-1,-7,4,9,4,8,9,5,8],[-3,9,-2,-7,-10,-3,7,7,-2,-6,9],[-5,3,6,1,2,-9,-1,-3,-7,7,7],[3,7,-7,6,-7,4,-6,-8,6,-4,10],[7,-2,-8,4,4,-1,5,-8,-3,4,2],[8,9,-9,1,8,5,-2,-10,2,6,-7],[-1,-3,-7,-2,9,9,7,2,-9,8,10]]], dtype = "int8")#candidate|9400|(1, 7, 11)|const|int8
var_9401 = relay.var("var_9401", dtype = "int8", shape = (9, 7, 11))#candidate|9401|(9, 7, 11)|var|int8
bop_9402 = relay.left_shift(const_9400.astype('int8'), var_9401.astype('int8')) # shape=(9, 7, 11)
func_7101_call = mod.get_global_var('func_7101')
func_7105_call = mutated_mod.get_global_var('func_7105')
var_9426 = relay.var("var_9426", dtype = "int32", shape = (2304,))#candidate|9426|(2304,)|var|int32
const_9427 = relay.const([[-3.732688],[6.069256],[0.235229]], dtype = "float32")#candidate|9427|(3, 1)|const|float32
call_9425 = relay.TupleGetItem(func_7101_call(relay.reshape(var_9426.astype('int32'), [12, 12, 16]), relay.reshape(var_9426.astype('int32'), [12, 12, 16]), relay.reshape(const_9427.astype('float32'), [3,]), ), 1)
call_9428 = relay.TupleGetItem(func_7105_call(relay.reshape(var_9426.astype('int32'), [12, 12, 16]), relay.reshape(var_9426.astype('int32'), [12, 12, 16]), relay.reshape(const_9427.astype('float32'), [3,]), ), 1)
bop_9429 = relay.right_shift(const_9400.astype('uint32'), bop_9402.astype('uint32')) # shape=(9, 7, 11)
uop_9443 = relay.log2(var_9401.astype('float32')) # shape=(9, 7, 11)
output = relay.Tuple([call_9425,var_9426,const_9427,bop_9429,uop_9443,])
output2 = relay.Tuple([call_9428,var_9426,const_9427,bop_9429,uop_9443,])
func_9445 = relay.Function([var_9401,var_9426,], output)
mod['func_9445'] = func_9445
mod = relay.transform.InferType()(mod)
var_9446 = relay.var("var_9446", dtype = "int8", shape = (9, 7, 11))#candidate|9446|(9, 7, 11)|var|int8
var_9447 = relay.var("var_9447", dtype = "int32", shape = (2304,))#candidate|9447|(2304,)|var|int32
output = func_9445(var_9446,var_9447,)
func_9448 = relay.Function([var_9446,var_9447,], output)
mutated_mod['func_9448'] = func_9448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9793 = relay.var("var_9793", dtype = "float64", shape = (11, 15, 11))#candidate|9793|(11, 15, 11)|var|float64
uop_9794 = relay.sqrt(var_9793.astype('float64')) # shape=(11, 15, 11)
output = relay.Tuple([uop_9794,])
output2 = relay.Tuple([uop_9794,])
func_9801 = relay.Function([var_9793,], output)
mod['func_9801'] = func_9801
mod = relay.transform.InferType()(mod)
mutated_mod['func_9801'] = func_9801
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9802 = relay.var("var_9802", dtype = "float64", shape = (11, 15, 11))#candidate|9802|(11, 15, 11)|var|float64
func_9801_call = mutated_mod.get_global_var('func_9801')
call_9803 = func_9801_call(var_9802)
output = call_9803
func_9804 = relay.Function([var_9802], output)
mutated_mod['func_9804'] = func_9804
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10094 = relay.var("var_10094", dtype = "int8", shape = (4, 15, 5))#candidate|10094|(4, 15, 5)|var|int8
var_10095 = relay.var("var_10095", dtype = "int8", shape = (4, 15, 5))#candidate|10095|(4, 15, 5)|var|int8
bop_10096 = relay.greater_equal(var_10094.astype('bool'), relay.reshape(var_10095.astype('bool'), relay.shape_of(var_10094))) # shape=(4, 15, 5)
uop_10107 = relay.asinh(var_10095.astype('float64')) # shape=(4, 15, 5)
var_10109 = relay.var("var_10109", dtype = "int8", shape = (4, 15, 5))#candidate|10109|(4, 15, 5)|var|int8
bop_10110 = relay.logical_xor(var_10094.astype('uint16'), relay.reshape(var_10109.astype('uint16'), relay.shape_of(var_10094))) # shape=(4, 15, 5)
const_10116 = relay.const([[[-9.709942,6.147846,-9.717243,-8.651129,8.298646],[8.096954,-8.638023,3.013950,7.189602,-1.501389],[-0.689275,6.575406,-6.789930,8.425714,3.277878],[-2.539275,-7.486479,-3.494590,-0.722116,-4.609367],[1.090031,4.519384,-9.692711,-2.537851,-7.083889],[7.144036,8.049149,-9.043182,-7.985807,6.787547],[-0.332221,3.093301,3.986705,2.387721,-7.982280],[5.483773,9.294629,-5.225905,9.759800,5.833245],[0.299835,-4.099250,8.853856,2.321870,-9.202277],[-9.785730,-9.236552,-8.088024,3.928937,-7.332853],[3.396651,6.307244,-7.455809,-4.088430,0.149561],[-4.974017,5.525506,8.904735,6.723236,-1.236080],[1.812552,-1.079425,7.210750,8.343260,-9.800356],[-0.716056,-3.791028,-7.637893,6.231876,-8.493414],[-1.461875,-6.671208,-7.852231,-6.517273,-1.989129]],[[0.274241,4.900803,9.103678,-5.432396,0.113841],[-4.901456,5.765114,-3.750855,-8.959527,-8.204599],[-6.410740,8.819866,-1.678197,-8.559629,0.418621],[-9.802118,-6.085358,-2.004789,-8.578154,-7.271209],[2.384502,0.162644,2.106643,-1.318183,-5.545047],[9.013094,0.575669,8.181415,-8.834661,-5.451169],[-9.895055,-5.353451,4.899973,-4.708666,-6.653565],[7.555797,-8.079262,-6.263971,-4.812710,2.972157],[8.960290,1.019002,4.410150,2.127958,-9.227154],[8.170437,-2.454903,5.659071,-6.760885,8.145938],[7.089385,-1.601741,8.575836,9.957557,9.057793],[-3.423835,7.491377,6.506122,-0.569865,-7.912994],[-9.754380,9.244815,-7.680669,-1.833813,9.957038],[8.075114,8.372278,-3.546119,-9.113201,-0.909804],[-0.352287,-6.161450,3.769680,-1.540006,-8.423729]],[[-6.622044,-3.250787,9.247849,2.265019,3.052269],[0.103230,0.230602,-9.991880,-0.166968,6.785417],[-0.532376,5.882474,-8.566301,-4.539525,2.322535],[3.269255,7.534082,5.815700,-1.840064,9.383381],[6.719973,-3.320820,7.354904,-9.344785,1.270262],[-9.663801,3.924937,4.465335,-0.355817,-9.850765],[-0.664827,-6.448791,8.368456,5.235810,-7.556715],[5.921727,0.744099,-8.332644,-3.663269,-0.268446],[-6.205394,7.285855,4.152962,7.592317,-0.306596],[5.951318,-3.639798,3.970954,4.029892,8.862872],[1.544797,-5.414866,9.056893,1.781841,5.907689],[6.722569,-4.486142,-5.598613,4.616653,-7.000259],[2.327833,3.882530,2.012984,-8.348774,2.690416],[-5.998235,-5.107405,7.354377,1.770930,-1.782444],[7.922292,-9.241066,-4.214590,6.396014,9.067241]],[[-5.074288,7.617271,-3.436375,-4.506099,9.594201],[-9.808714,-6.870388,-0.539949,-0.845022,-8.542553],[8.933972,3.833620,1.649871,-9.673182,3.219883],[-4.538063,-7.814813,0.704790,-3.760480,0.235337],[4.422564,2.561686,0.056694,-2.846094,1.148638],[-2.555629,-8.113191,2.218226,8.604984,-8.349862],[5.579666,-3.941659,-5.193211,-6.956966,6.620972],[-0.985648,9.895615,-4.717968,-2.005081,3.526854],[5.340342,-6.281418,8.165725,-8.850672,2.407766],[8.880474,6.220459,-8.944051,-3.354382,1.056776],[6.290931,-9.623067,5.791066,8.062903,2.393426],[-6.258599,-0.412541,-4.951317,-2.966494,-1.684464],[5.690695,-3.714814,-9.458536,-2.626984,8.787099],[-1.084582,-3.246757,4.073026,-1.900565,2.843939],[8.913909,-8.710878,-8.802912,4.672050,8.034048]]], dtype = "float64")#candidate|10116|(4, 15, 5)|const|float64
bop_10117 = relay.mod(uop_10107.astype('float64'), relay.reshape(const_10116.astype('float64'), relay.shape_of(uop_10107))) # shape=(4, 15, 5)
output = relay.Tuple([bop_10096,bop_10110,bop_10117,])
output2 = relay.Tuple([bop_10096,bop_10110,bop_10117,])
F = relay.Function([var_10094,var_10095,var_10109,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10094,var_10095,var_10109,], output2)
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
