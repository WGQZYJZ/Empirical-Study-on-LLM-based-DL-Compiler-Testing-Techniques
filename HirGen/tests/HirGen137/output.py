import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_29 = relay.const(7, dtype = "uint16")#candidate|29|()|const|uint16
var_30 = relay.var("var_30", dtype = "uint16", shape = (10, 7, 4))#candidate|30|(10, 7, 4)|var|uint16
bop_31 = relay.logical_xor(const_29.astype('uint16'), var_30.astype('uint16')) # shape=(10, 7, 4)
uop_37 = relay.asinh(bop_31.astype('float64')) # shape=(10, 7, 4)
output = uop_37
output2 = uop_37
func_60 = relay.Function([var_30,], output)
mod['func_60'] = func_60
mod = relay.transform.InferType()(mod)
var_61 = relay.var("var_61", dtype = "uint16", shape = (10, 7, 4))#candidate|61|(10, 7, 4)|var|uint16
output = func_60(var_61)
func_62 = relay.Function([var_61], output)
mutated_mod['func_62'] = func_62
mutated_mod = relay.transform.InferType()(mutated_mod)
const_88 = relay.const([[[-9.774377,4.694124,-0.945008,-1.753967,5.489768,-4.063739,1.918273,-4.132808],[0.038950,-2.910506,-7.061429,7.028572,2.165219,-4.388469,-6.851164,4.229982],[-5.605549,1.261897,-7.735768,-4.326927,8.685292,-5.635948,1.313325,-2.356095],[4.204033,8.556038,8.968351,-0.946933,-0.120156,-2.567091,-8.110414,0.592689]],[[8.356875,9.502348,4.930455,1.547683,1.509709,3.201045,-9.507041,1.031103],[-1.187682,6.186876,-8.096340,-0.722112,-9.215399,6.538930,-2.838455,-3.926583],[0.861262,-5.457203,3.734536,9.367555,0.220871,9.156219,-5.816104,-8.098764],[9.646387,-0.577371,3.001871,4.380161,-3.170380,-7.732562,1.879415,-9.295824]],[[-0.477863,6.136155,-9.832481,-1.579694,1.140768,-5.352778,3.973005,-7.889080],[-8.762724,-8.282369,-7.567658,-0.310600,-0.035976,8.912533,1.524272,-3.880962],[-4.413128,1.360027,-3.231884,6.502479,9.529364,-8.534965,-4.169867,-4.294654],[7.694522,-5.198212,-2.450512,-1.253583,2.286334,-3.182624,4.282747,-7.513671]],[[0.595108,6.449059,-3.064122,3.859703,-7.902488,-8.988829,6.667394,2.896339],[2.175193,-0.503483,-4.946361,-3.479288,-1.111406,-7.517011,9.903712,-4.677123],[-1.588378,-5.271963,-4.928542,6.572996,8.925708,8.406121,-3.937154,-7.748320],[-7.353257,6.672364,8.122287,-2.747525,-4.760826,-1.519329,5.133199,-7.624974]],[[-1.910148,-8.205292,0.230871,6.268908,0.489528,3.830398,1.150276,7.323194],[-9.846794,1.597209,-8.360416,2.622361,-4.152589,-3.617183,-5.584871,-0.223985],[-5.144054,4.490635,-5.432141,-3.467574,7.601829,4.504136,3.593987,-8.413365],[3.916304,-3.227110,9.004559,-1.464914,7.746198,-7.197178,-4.646721,-9.088284]],[[2.050788,-2.021735,-4.794018,-5.290159,-4.879676,-2.890682,-6.808983,8.733760],[-2.729000,-7.728547,2.230837,-1.581705,9.889253,5.630721,5.134956,-0.202021],[1.010033,-8.815709,-1.535924,-4.553877,-0.671789,-8.931645,2.976710,-0.404456],[5.167230,-5.480410,9.873993,7.287127,9.088243,-9.671044,-2.539509,2.339115]],[[9.086959,4.705929,-3.184071,-2.677880,6.905419,-2.906623,-9.610320,-0.171868],[4.406368,6.346482,1.597944,6.492411,1.381645,1.711949,3.453766,8.682052],[-8.294572,-5.721228,-4.507403,5.187459,4.862520,5.177332,-3.828409,-9.918280],[-9.286243,2.633639,-7.633701,-3.321047,-8.299251,-2.582567,-1.192607,1.853943]],[[-9.668557,-5.605653,-9.943349,-0.507648,7.099061,-3.252786,-5.609853,1.371048],[-8.004342,-2.192046,0.888260,-7.341592,2.489021,8.692367,-2.120153,-3.033380],[-1.654607,-7.082778,9.842009,3.289677,-1.831469,-3.449689,-1.783964,7.276002],[-4.932948,2.839056,-0.778493,-3.103035,-5.959943,9.108184,-7.257790,-8.382293]],[[-2.409629,4.898258,3.963605,-7.478929,-9.810874,-0.671540,-6.652149,1.958674],[-6.792030,6.117829,-1.571293,-4.797940,5.763810,-1.893838,1.542956,2.418739],[3.895296,2.285644,6.100427,-5.218498,5.175022,-3.173436,-4.585063,-9.899847],[-3.448126,8.930419,0.504101,-1.302639,8.827776,-3.588209,3.154517,4.861297]],[[7.926040,3.774162,-0.741506,-7.189492,2.733656,-5.650080,1.962451,-5.764818],[-9.642221,-2.881061,1.909851,-9.550240,7.714745,2.489401,-6.587724,7.684408],[-6.358525,-0.399176,-5.737010,-8.491994,5.613739,8.513882,8.522791,3.295380],[9.267465,-1.323079,-5.711532,-6.156929,0.805474,-8.959178,-2.438433,1.640126]],[[-0.391350,1.086223,6.106748,-2.019390,-0.860804,5.562953,9.191834,9.153790],[-0.277165,2.962489,4.540615,6.820662,-9.372905,-2.538308,1.838976,4.536396],[-4.067374,6.164464,-9.326511,-7.125943,4.431519,-3.804137,-6.353974,-9.094220],[8.877595,8.235807,8.273478,-1.000693,-0.671103,-3.345658,-7.921523,-6.545088]]], dtype = "float32")#candidate|88|(11, 4, 8)|const|float32
uop_89 = relay.atanh(const_88.astype('float32')) # shape=(11, 4, 8)
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
var_92 = relay.var("var_92", dtype = "uint16", shape = (70, 4))#candidate|92|(70, 4)|var|uint16
call_91 = func_60_call(relay.reshape(var_92.astype('uint16'), [10, 7, 4]))
call_93 = func_60_call(relay.reshape(var_92.astype('uint16'), [10, 7, 4]))
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
call_97 = func_60_call(relay.reshape(call_91.astype('uint16'), [10, 7, 4]))
call_98 = func_60_call(relay.reshape(call_91.astype('uint16'), [10, 7, 4]))
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
call_104 = func_60_call(relay.reshape(var_92.astype('uint16'), [10, 7, 4]))
call_105 = func_60_call(relay.reshape(var_92.astype('uint16'), [10, 7, 4]))
uop_117 = relay.cosh(uop_89.astype('float64')) # shape=(11, 4, 8)
var_122 = relay.var("var_122", dtype = "float64", shape = (11, 4, 8))#candidate|122|(11, 4, 8)|var|float64
bop_123 = relay.maximum(uop_117.astype('uint16'), relay.reshape(var_122.astype('uint16'), relay.shape_of(uop_117))) # shape=(11, 4, 8)
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
call_126 = func_60_call(relay.reshape(var_92.astype('uint16'), [10, 7, 4]))
call_127 = func_60_call(relay.reshape(var_92.astype('uint16'), [10, 7, 4]))
bop_132 = relay.logical_or(uop_117.astype('bool'), relay.reshape(uop_89.astype('bool'), relay.shape_of(uop_117))) # shape=(11, 4, 8)
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
call_137 = func_60_call(relay.reshape(call_91.astype('uint16'), [10, 7, 4]))
call_138 = func_60_call(relay.reshape(call_91.astype('uint16'), [10, 7, 4]))
output = relay.Tuple([call_91,var_92,call_97,call_104,bop_123,call_126,bop_132,call_137,])
output2 = relay.Tuple([call_93,var_92,call_98,call_105,bop_123,call_127,bop_132,call_138,])
func_139 = relay.Function([var_92,var_122,], output)
mod['func_139'] = func_139
mod = relay.transform.InferType()(mod)
mutated_mod['func_139'] = func_139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mutated_mod.get_global_var('func_139')
var_141 = relay.var("var_141", dtype = "uint16", shape = (70, 4))#candidate|141|(70, 4)|var|uint16
var_142 = relay.var("var_142", dtype = "float64", shape = (11, 4, 8))#candidate|142|(11, 4, 8)|var|float64
call_140 = func_139_call(var_141,var_142,)
output = call_140
func_143 = relay.Function([var_141,var_142,], output)
mutated_mod['func_143'] = func_143
mutated_mod = relay.transform.InferType()(mutated_mod)
var_339 = relay.var("var_339", dtype = "int64", shape = ())#candidate|339|()|var|int64
var_340 = relay.var("var_340", dtype = "int64", shape = (7, 13, 13))#candidate|340|(7, 13, 13)|var|int64
bop_341 = relay.left_shift(var_339.astype('int64'), var_340.astype('int64')) # shape=(7, 13, 13)
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
var_345 = relay.var("var_345", dtype = "uint16", shape = (280,))#candidate|345|(280,)|var|uint16
call_344 = func_60_call(relay.reshape(var_345.astype('uint16'), [10, 7, 4]))
call_346 = func_60_call(relay.reshape(var_345.astype('uint16'), [10, 7, 4]))
output = relay.Tuple([bop_341,call_344,var_345,])
output2 = relay.Tuple([bop_341,call_346,var_345,])
func_354 = relay.Function([var_339,var_340,var_345,], output)
mod['func_354'] = func_354
mod = relay.transform.InferType()(mod)
var_355 = relay.var("var_355", dtype = "int64", shape = ())#candidate|355|()|var|int64
var_356 = relay.var("var_356", dtype = "int64", shape = (7, 13, 13))#candidate|356|(7, 13, 13)|var|int64
var_357 = relay.var("var_357", dtype = "uint16", shape = (280,))#candidate|357|(280,)|var|uint16
output = func_354(var_355,var_356,var_357,)
func_358 = relay.Function([var_355,var_356,var_357,], output)
mutated_mod['func_358'] = func_358
mutated_mod = relay.transform.InferType()(mutated_mod)
var_417 = relay.var("var_417", dtype = "float64", shape = (11, 5, 4))#candidate|417|(11, 5, 4)|var|float64
uop_418 = relay.cosh(var_417.astype('float64')) # shape=(11, 5, 4)
uop_426 = relay.erf(uop_418.astype('float32')) # shape=(11, 5, 4)
func_139_call = mod.get_global_var('func_139')
func_143_call = mutated_mod.get_global_var('func_143')
var_438 = relay.var("var_438", dtype = "uint16", shape = (280,))#candidate|438|(280,)|var|uint16
const_439 = relay.const([-6.527486,3.086295,-3.721650,-1.794950,3.215113,-9.474272,-6.613488,3.866396,4.984670,-7.563785,-1.624489,-3.470057,7.948936,-9.078123,-4.720381,-7.830298,4.616863,-4.566787,-7.934331,9.586799,3.035217,5.412838,8.165196,-7.808444,-8.787934,5.461380,-7.506438,0.695051,-7.461428,-4.937464,0.989758,7.942208,-1.587617,-4.272119,6.784051,2.834933,6.166797,-5.483483,6.949446,2.441297,-3.781094,8.328374,-7.551857,-2.566304,-2.931956,-7.791712,1.607305,-6.559720,5.252739,-6.137655,-2.011268,9.356021,-3.779158,-3.003749,3.544778,5.948247,-6.282249,-4.862996,3.183170,6.324002,2.609329,0.357445,-1.840697,6.685783,4.589511,-2.996962,1.389951,2.943004,6.289606,3.729168,-8.886042,-9.319334,7.440946,6.347277,2.365241,-0.221422,-3.641901,1.871000,0.335755,1.342426,-0.694392,-8.640800,2.547387,8.083597,5.539997,4.584129,6.708196,4.464041,-9.399537,6.002491,8.644291,6.122438,-2.990918,-2.327133,2.927594,-9.891470,6.668787,2.716233,-9.169396,-2.805886,7.588497,3.104040,2.126209,-9.786454,-2.793244,-6.134313,7.436614,8.355431,-7.873738,-1.239304,1.282998,-8.487723,0.231876,-7.071634,-8.323723,-8.244120,-4.902760,4.352195,-2.515497,-1.360365,3.991986,-6.993577,-3.594716,-3.848521,-3.019562,-7.975633,5.841099,-9.383302,-1.286166,7.601447,4.465678,-9.927437,4.977761,-2.410023,0.304614,-7.115364,4.706448,-3.873962,4.388244,-5.955838,0.236176,8.757043,3.102265,0.220176,-9.023337,9.500431,-9.055722,-1.926813,7.135015,5.750944,3.270380,7.586023,1.320420,-2.978366,3.170496,-6.350073,2.372436,0.239795,1.319315,-9.414134,1.640566,-3.553938,0.267912,-9.452224,8.892595,-3.664393,5.161472,9.686268,5.289934,2.388318,-6.701295,3.467262,-2.663726,7.578126,4.470873,8.477148,9.737723,5.058914,-2.042840,0.987709,5.601362,-0.596341,8.675768,0.125118,7.256226,3.692072,-9.131016,5.629407,-3.427439,1.682324,-5.178472,-1.423948,-5.694848,8.370892,3.423778,-6.169016,-1.591108,-5.936642,-2.128089,-3.040305,-8.304631,8.612944,-3.785966,9.319083,5.267794,-0.065285,-0.997307,3.426833,-2.299916,4.496460,2.268161,8.301589,0.998628,-9.344609,7.863846,3.165748,-1.797914,7.825891,-8.384676,8.390829,6.608241,6.633800,2.782869,-9.381734,2.403271,1.718985,3.468521,-5.408829,-5.047590,-5.128364,2.133468,-0.290735,-0.740650,-6.722504,-0.934946,9.645176,-3.225500,1.030797,4.396839,4.845291,-4.107719,-1.710578,5.790299,-3.513359,8.847189,-1.875219,-7.361898,-3.141218,-4.385616,0.842315,7.728667,-7.571211,-0.806545,1.458386,2.254726,-9.514927,1.430134,6.181140,-5.241843,4.377720,-1.303169,-9.671205,-2.242946,6.889921,-2.595296,2.109226,1.093290,1.960434,-3.360780,-7.976940,4.138986,6.421541,4.194934,-5.004946,-8.801510,9.510085,8.092930,7.699939,-6.194689,-3.956341,-1.611169,-7.445537,8.058329,8.002659,-0.123024,0.561645,-6.416664,1.328053,1.539934,9.532512,2.296234,-0.841935,9.295607,-1.546805,-6.867740,-3.653575,-2.044221,9.623691,-6.562448,2.130276,-9.960489,-4.310135,9.049510,-7.261214,6.797566,-0.086507,-9.219058,3.515573,2.600074,6.177420,-9.983692,-9.336573,3.083905,-1.776936,-9.865915,-9.720667,-2.910685,6.531438,-4.463387,-0.685395,-8.555255,-9.690983,0.406192,-8.572660,4.862036,3.000573,6.903297,7.843014,4.599751,-5.104850,5.679597,-0.902377,1.852362,-4.315088,6.741839,-2.614442,2.324343,-0.740505,-6.351380,0.648530,-6.883520,-8.635001,-8.836780,-8.691883,0.820697,6.416861,-8.961491,3.536215,-0.452898,3.248703,-4.691530,0.358855], dtype = "float64")#candidate|439|(352,)|const|float64
call_437 = relay.TupleGetItem(func_139_call(relay.reshape(var_438.astype('uint16'), [70, 4]), relay.reshape(const_439.astype('float64'), [11, 4, 8]), ), 5)
call_440 = relay.TupleGetItem(func_143_call(relay.reshape(var_438.astype('uint16'), [70, 4]), relay.reshape(const_439.astype('float64'), [11, 4, 8]), ), 5)
bop_457 = relay.floor_mod(uop_426.astype('float64'), relay.reshape(var_417.astype('float64'), relay.shape_of(uop_426))) # shape=(11, 5, 4)
output = relay.Tuple([call_437,var_438,const_439,bop_457,])
output2 = relay.Tuple([call_440,var_438,const_439,bop_457,])
func_460 = relay.Function([var_417,var_438,], output)
mod['func_460'] = func_460
mod = relay.transform.InferType()(mod)
var_461 = relay.var("var_461", dtype = "float64", shape = (11, 5, 4))#candidate|461|(11, 5, 4)|var|float64
var_462 = relay.var("var_462", dtype = "uint16", shape = (280,))#candidate|462|(280,)|var|uint16
output = func_460(var_461,var_462,)
func_463 = relay.Function([var_461,var_462,], output)
mutated_mod['func_463'] = func_463
mutated_mod = relay.transform.InferType()(mutated_mod)
var_504 = relay.var("var_504", dtype = "int16", shape = (6, 10, 14))#candidate|504|(6, 10, 14)|var|int16
const_505 = relay.const([[[9,-2,9,4,-8,-1,-10,4,-8,-5,7,-3,8,1],[4,-9,-3,-9,-2,-8,-10,3,7,-1,10,-5,-8,6],[-4,7,6,10,-8,6,1,-2,10,-2,5,-3,9,-4],[6,2,-8,-7,-8,6,7,-6,3,-1,3,3,7,5],[-5,5,-10,1,-10,2,7,-2,1,5,7,-10,-9,2],[-8,6,-5,-5,9,-3,-4,5,-7,6,-8,-4,8,9],[7,-5,-6,8,-1,-8,-9,-9,10,-4,2,6,2,-7],[4,-8,-5,5,6,-7,-8,-7,-8,10,2,-6,6,4],[-10,6,7,4,-9,-5,4,-3,-7,-9,-9,-4,5,-5],[1,-6,-10,-6,8,-9,1,-3,-6,-7,-7,1,-9,6]],[[6,-4,-1,-10,5,-10,-8,-2,-2,3,-9,4,-1,1],[9,-2,9,2,6,-2,7,-4,10,-3,-10,2,-9,7],[-1,-9,-8,-7,-9,-8,10,6,10,4,7,-4,-4,-6],[5,4,-4,8,6,-8,4,-1,-5,-4,8,-7,-5,-10],[9,3,-9,-10,2,4,1,2,-9,-2,2,1,5,-3],[-1,9,-10,2,9,-4,-7,-8,10,8,3,-6,-7,4],[-5,2,1,3,-2,-3,-6,2,5,4,10,-7,-1,9],[-9,9,10,-1,-3,-4,-1,7,-4,-3,-7,-6,-8,-9],[7,-8,-10,2,10,-3,-10,-9,-4,8,-5,8,-7,-8],[-1,-5,-6,-5,-2,6,-2,5,6,1,-10,1,-10,-7]],[[5,-2,-4,-5,10,7,-8,-3,4,2,-4,1,4,9],[-2,10,4,4,-9,-8,-10,2,-10,8,-5,-5,3,-2],[9,-10,-10,8,2,-1,2,1,-6,8,10,-1,6,3],[-3,4,-8,3,-5,-1,-5,-10,-4,9,-6,8,-4,-10],[-7,8,7,4,-8,-5,-9,2,9,-3,2,2,2,1],[-1,6,3,-7,-8,8,-9,-1,-9,2,-2,10,-10,2],[-4,-6,4,-10,8,1,-10,3,4,-8,6,1,-7,-4],[7,9,-8,4,-8,3,6,1,-3,-5,-10,-9,5,6],[5,10,-5,1,3,9,4,9,-6,-5,-7,-7,5,1],[10,-3,7,-6,2,8,-5,-9,9,-6,-8,-5,3,-10]],[[-9,-8,10,3,5,-2,7,2,-8,-10,9,-1,8,10],[7,-10,2,-5,-1,2,8,-3,-5,-6,8,-8,-3,-3],[-7,2,4,-2,2,-3,-8,9,10,-2,10,5,-5,4],[6,-8,-2,-8,-2,7,2,7,4,7,-1,-8,-6,-9],[-8,6,2,-8,4,-3,8,10,-9,-9,6,-8,2,8],[-10,8,1,3,-8,8,-7,-8,-2,-5,7,7,-10,10],[10,10,2,8,-2,7,-2,-3,9,-5,2,-3,6,2],[-6,9,-8,-7,-9,-6,-8,2,-9,10,-8,8,-7,-9],[-2,10,-5,3,8,-6,5,-7,-4,-4,7,10,10,-5],[8,3,-9,7,10,7,-1,6,-6,10,3,4,9,5]],[[-9,-8,4,-8,-4,7,6,3,-9,-5,1,9,-9,-4],[-7,10,9,5,-9,8,-10,9,-1,5,-1,-6,-6,-6],[10,-5,-1,4,-3,5,2,7,-8,-7,-7,8,-3,-10],[-1,-5,-8,-7,5,9,2,2,-7,7,-3,4,-9,10],[7,10,-8,-1,9,-7,1,2,2,-7,-3,4,-9,8],[1,9,-9,5,5,-6,-4,-9,-1,-6,7,1,8,-7],[-6,-2,-4,4,-9,1,-7,-10,-9,7,2,-2,7,-10],[-3,-1,-2,7,-3,9,3,7,6,2,6,7,3,6],[7,4,-1,-10,-7,8,1,3,9,4,7,3,3,1],[3,5,-5,1,-5,10,-9,5,8,-4,10,-2,-3,-2]],[[9,2,3,2,-10,6,4,-9,-4,5,-4,9,-4,-1],[-10,-3,8,-10,7,-1,-5,-2,10,-3,8,8,-6,4],[-10,9,7,6,9,8,-8,-1,-5,5,6,2,8,6],[7,-4,-6,-4,4,10,-7,-9,9,-1,5,-10,4,9],[-1,5,-6,4,1,4,-1,-1,5,5,-2,-8,10,1],[9,-5,-2,8,-9,-9,2,8,-10,-10,-8,10,-1,6],[6,7,-5,8,5,7,-8,-6,2,2,2,-10,8,10],[-10,-3,6,-4,4,-10,7,3,-8,6,5,-5,-1,-7],[4,-10,-6,3,-3,-4,-8,-6,-4,10,9,1,5,1],[10,9,-7,-10,-2,-6,-9,-3,-5,-10,9,-10,-8,-10]]], dtype = "int16")#candidate|505|(6, 10, 14)|const|int16
bop_506 = relay.multiply(var_504.astype('int16'), relay.reshape(const_505.astype('int16'), relay.shape_of(var_504))) # shape=(6, 10, 14)
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
const_510 = relay.const([9,-7,3,-1,-8,3,-1,-5,-9,-1,-5,-9,-9,3,4,-1,4,-4,-1,1,4,-1,-5,7,9,-6,-6,1,-10,9,6,1,-1,-4,9,-4,-1,9,-1,-2,6,-7,3,-10,-4,-8,-10,-8,-3,-3,-10,-7,-4,-7,-5,-5,6,-5,-10,3,5,-4,-10,8,-7,-6,-10,7,1,8,4,-1,7,-9,-3,3,-4,5,-1,9,-5,-6,10,-8,-9,1,4,-4,-7,2,-5,-8,-3,-7,5,2,-1,-7,-2,-5,3,-6,7,-10,3,4,8,-9,6,-5,9,3,8,2,4,4,-3,-6,8,-5,-9,-9,3,-10,-1,10,-4,2,2,3,3,-3,8,7,7,-9,10,-5,-5,10,10,7,-4,10,-7,1,-2,6,-8,-6,-2,-3,-4,-5,-3,-4,-8,1,-2,-7,-3,8,-5,-5,-7,7,-7,-4,-9,9,-6,9,6,6,-10,-8,1,8,10,8,6,7,-6,-4,9,-8,-6,1,-6,9,-9,-9,-3,-4,-2,-10,-8,4,7,-10,3,3,7,-3,-2,1,1,10,8,-9,-8,1,-6,-9,-6,9,-7,1,10,-6,-8,2,6,-3,5,7,1,-9,-6,9,-7,1,3,-9,6,3,-2,-1,-6,5,8,-7,3,-5,-6,10,3,9,-1,-8,4,9,8,-6,-8,-8,-6,-5,-4,-9,7,4,-9,7,-3,-7,8,-5,-7,3,-4,2,-9,-1,7,1,-9,3,2,-6], dtype = "uint16")#candidate|510|(280,)|const|uint16
call_509 = func_60_call(relay.reshape(const_510.astype('uint16'), [10, 7, 4]))
call_511 = func_60_call(relay.reshape(const_510.astype('uint16'), [10, 7, 4]))
output = relay.Tuple([bop_506,call_509,const_510,])
output2 = relay.Tuple([bop_506,call_511,const_510,])
func_512 = relay.Function([var_504,], output)
mod['func_512'] = func_512
mod = relay.transform.InferType()(mod)
var_513 = relay.var("var_513", dtype = "int16", shape = (6, 10, 14))#candidate|513|(6, 10, 14)|var|int16
output = func_512(var_513)
func_514 = relay.Function([var_513], output)
mutated_mod['func_514'] = func_514
mutated_mod = relay.transform.InferType()(mutated_mod)
var_890 = relay.var("var_890", dtype = "float32", shape = (6, 7, 6))#candidate|890|(6, 7, 6)|var|float32
uop_891 = relay.sin(var_890.astype('float32')) # shape=(6, 7, 6)
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
const_912 = relay.const([[-5,-8,-6,-7,-2,-1,-5,-2,-6,8,-9,-1,7,-7,-3,-3,-10,7,7,-3,9,1,-7,-6,-10,-6,-1,9],[10,3,6,2,-8,-10,-1,6,-6,-7,2,7,6,-2,-8,-6,-6,2,4,6,2,-9,-10,4,3,-1,3,-8],[9,7,-10,8,2,6,3,-10,-9,-8,3,6,-5,3,-5,8,-1,-1,-10,7,-10,-9,-8,-10,7,7,-1,-6],[-10,-4,-9,8,9,-3,10,-2,6,3,-10,2,-10,9,-9,-8,5,-3,4,6,-1,-6,-2,1,-10,3,-7,9],[-1,-1,-3,-9,-10,-3,-4,-10,2,5,-4,4,-1,6,-10,-7,3,-1,-4,-7,5,-1,-10,3,8,-6,4,-6],[6,5,9,5,8,8,-8,-8,-4,-1,9,8,2,10,5,3,10,-5,9,-10,-8,3,-3,1,10,-6,4,6],[10,-1,4,4,3,-10,1,-1,8,9,7,-3,-9,-5,2,10,9,-5,-7,-6,2,3,8,6,-10,-9,2,3],[10,-8,-3,-4,-10,-7,2,7,1,-7,8,7,8,-6,-10,4,8,4,-10,6,-7,-9,6,3,10,6,-5,5],[-1,-4,1,-10,-9,10,3,9,9,-1,6,4,-5,-1,3,2,8,-4,-3,7,9,1,-3,3,8,9,-7,-9],[5,-3,-7,-2,-2,-3,-3,8,8,-3,10,5,10,-4,-8,9,5,2,8,9,2,-6,-10,8,-4,1,7,-3]], dtype = "uint16")#candidate|912|(10, 28)|const|uint16
call_911 = func_60_call(relay.reshape(const_912.astype('uint16'), [10, 7, 4]))
call_913 = func_60_call(relay.reshape(const_912.astype('uint16'), [10, 7, 4]))
func_139_call = mod.get_global_var('func_139')
func_143_call = mutated_mod.get_global_var('func_143')
var_924 = relay.var("var_924", dtype = "float64", shape = (2, 176))#candidate|924|(2, 176)|var|float64
call_923 = relay.TupleGetItem(func_139_call(relay.reshape(call_911.astype('uint16'), [70, 4]), relay.reshape(var_924.astype('float64'), [11, 4, 8]), ), 3)
call_925 = relay.TupleGetItem(func_143_call(relay.reshape(call_911.astype('uint16'), [70, 4]), relay.reshape(var_924.astype('float64'), [11, 4, 8]), ), 3)
var_927 = relay.var("var_927", dtype = "float32", shape = (6, 7, 6))#candidate|927|(6, 7, 6)|var|float32
bop_928 = relay.bitwise_or(uop_891.astype('uint64'), relay.reshape(var_927.astype('uint64'), relay.shape_of(uop_891))) # shape=(6, 7, 6)
bop_943 = relay.maximum(bop_928.astype('int8'), relay.reshape(var_927.astype('int8'), relay.shape_of(bop_928))) # shape=(6, 7, 6)
output = relay.Tuple([call_911,const_912,call_923,var_924,bop_943,])
output2 = relay.Tuple([call_913,const_912,call_925,var_924,bop_943,])
func_947 = relay.Function([var_890,var_924,var_927,], output)
mod['func_947'] = func_947
mod = relay.transform.InferType()(mod)
mutated_mod['func_947'] = func_947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mutated_mod.get_global_var('func_947')
var_949 = relay.var("var_949", dtype = "float32", shape = (6, 7, 6))#candidate|949|(6, 7, 6)|var|float32
var_950 = relay.var("var_950", dtype = "float64", shape = (2, 176))#candidate|950|(2, 176)|var|float64
var_951 = relay.var("var_951", dtype = "float32", shape = (6, 7, 6))#candidate|951|(6, 7, 6)|var|float32
call_948 = func_947_call(var_949,var_950,var_951,)
output = call_948
func_952 = relay.Function([var_949,var_950,var_951,], output)
mutated_mod['func_952'] = func_952
mutated_mod = relay.transform.InferType()(mutated_mod)
var_954 = relay.var("var_954", dtype = "bool", shape = ())#candidate|954|()|var|bool
var_955 = relay.var("var_955", dtype = "bool", shape = (13, 7, 15))#candidate|955|(13, 7, 15)|var|bool
bop_956 = relay.logical_or(var_954.astype('bool'), var_955.astype('bool')) # shape=(13, 7, 15)
output = relay.Tuple([bop_956,])
output2 = relay.Tuple([bop_956,])
func_962 = relay.Function([var_954,var_955,], output)
mod['func_962'] = func_962
mod = relay.transform.InferType()(mod)
var_963 = relay.var("var_963", dtype = "bool", shape = ())#candidate|963|()|var|bool
var_964 = relay.var("var_964", dtype = "bool", shape = (13, 7, 15))#candidate|964|(13, 7, 15)|var|bool
output = func_962(var_963,var_964,)
func_965 = relay.Function([var_963,var_964,], output)
mutated_mod['func_965'] = func_965
mutated_mod = relay.transform.InferType()(mutated_mod)
var_979 = relay.var("var_979", dtype = "float64", shape = ())#candidate|979|()|var|float64
const_980 = relay.const([[[-9.909568,7.400736,3.073166,2.271869,-8.010786,-5.990524,-3.135550,0.144771,4.770771,6.688582,6.287805,-5.277129,4.609741],[-6.676597,-7.000010,5.103842,2.023662,5.129970,5.192467,8.903053,8.068923,0.351593,-2.153027,5.998284,-1.156033,-9.869400]],[[-3.013813,5.806393,-5.288810,-7.922444,-6.465737,5.591187,-9.841351,-3.588190,-1.359696,-9.297340,-0.535433,2.439234,-8.382995],[-7.032976,4.812064,3.189293,8.643408,9.700929,-9.735944,-2.072507,-8.269849,-1.341337,-7.411337,-3.923363,6.484384,-8.486404]]], dtype = "float64")#candidate|980|(2, 2, 13)|const|float64
bop_981 = relay.mod(var_979.astype('float64'), const_980.astype('float64')) # shape=(2, 2, 13)
func_947_call = mod.get_global_var('func_947')
func_952_call = mutated_mod.get_global_var('func_952')
var_992 = relay.var("var_992", dtype = "float32", shape = (252, 1))#candidate|992|(252, 1)|var|float32
const_993 = relay.const([-3.134758,6.984112,8.072262,0.283331,6.954561,-3.871938,-4.025417,-8.316920,-0.572616,-0.556322,9.336532,5.818779,8.833429,6.669087,-0.424516,-7.665867,6.320164,-1.810658,8.241037,1.238794,1.025449,-3.455646,-0.186870,7.795631,-7.624031,-4.789736,-3.196772,-5.532656,2.900229,-9.029313,-5.808997,-7.516921,-2.118090,-2.874758,-7.711254,-5.557827,7.163266,0.475030,8.249552,-6.598073,0.494096,0.759012,5.578717,6.253873,-0.397034,-6.069808,-3.062569,-9.713102,3.919234,9.865102,9.864814,2.284478,-5.905932,-1.144518,9.431592,-8.765017,7.886837,-6.568560,2.515394,8.238825,1.330620,-8.204448,-8.653641,2.951278,5.695703,2.788858,-6.908425,7.873740,-8.547276,4.370565,-5.420252,-9.739075,5.123206,-9.570020,-6.266037,-8.277200,0.691333,7.870314,-2.511533,1.267976,6.521372,-8.133486,-0.923500,4.939445,9.202332,-5.495858,-1.700532,-5.293103,-0.455025,-3.495667,-4.569658,-3.058277,8.146708,-8.997280,-0.679047,0.282573,-8.377508,-2.923310,5.014102,3.798992,-1.773023,-0.296510,-9.101980,-6.477623,-3.385344,3.055769,-9.154420,-4.387451,-5.294134,9.731030,4.030087,-3.764694,-5.881989,-8.554831,-0.814044,-2.039694,1.349237,2.167755,9.513582,-9.185417,-0.694028,1.995958,-0.231993,-1.750190,-8.268071,0.069867,-2.512030,1.843704,-3.381676,-6.839903,-8.843443,0.196063,-3.646220,4.794712,8.760100,4.458665,-7.388539,-0.707446,-8.760998,6.462244,-9.052931,-0.607593,-9.229526,8.831248,2.431751,-6.998846,-2.975663,-2.913312,-5.459802,9.063942,6.042972,-5.864563,8.360730,-8.470991,2.313849,-9.854077,2.988780,6.113593,-9.176147,-0.427763,-2.869112,8.492350,5.596902,5.354430,-4.953302,8.301052,5.417469,7.523374,-1.032194,9.306372,3.135477,3.023023,-7.214253,-0.433389,1.864747,7.191300,8.546244,-9.618816,-7.251548,6.503273,-9.320959,-3.989319,-1.380050,-2.710320,-8.548998,-8.453297,8.727789,-0.834390,-5.907109,1.594134,6.386456,-5.370781,4.190432,9.684937,-7.897484,-4.351209,8.535610,1.772034,-7.918470,-0.820668,9.175227,-0.600039,-9.476488,-6.320590,-8.613622,-3.390696,-1.584138,-0.405519,-5.829390,4.533974,-6.830378,7.888163,0.615695,5.167168,5.402407,-3.830184,4.338293,5.331664,3.971457,-9.954123,1.317037,1.434757,1.104939,-4.927505,-8.359149,3.408995,5.816680,-7.261872,2.792807,8.417061,-1.433217,8.408975,-2.050326,2.935771,-7.326247,6.542442,7.206508,-1.121902,7.792012,-8.357894,-5.780461,-4.243829,-1.459392,-1.217380,2.122819,-9.920414,4.555867,5.497942,4.122076,5.661751,-5.749828,1.259758,-7.676704,0.227425,-6.419618,3.527220,4.355210,5.028364,-7.228020,1.339114,4.224669,2.364370,5.225345,-6.558103,-3.125617,-9.701368,8.015673,-9.834990,9.798357,6.563208,4.592006,5.604106,-2.224364,-1.671504,-4.879693,-7.039441,-9.100226,6.824315,-4.031442,-1.298603,8.256714,-1.925301,-4.205352,-0.139532,-9.512919,-2.840599,-6.429921,-8.658259,-8.218789,-1.110931,-3.830499,-3.196907,-7.323320,-3.952949,6.598001,2.715822,4.127230,7.711969,-8.635177,-8.680875,4.611706,-6.058965,-0.677019,7.718644,-4.163842,5.438716,-3.306102,3.195377,8.439740,-6.586492,-1.564031,-7.658371,2.227951,5.205508,0.560831,-2.995069,-6.938435,1.863995,3.591348,4.173846,-5.662585,-8.158431,-7.510654,6.249044,0.719086,4.972357,-2.017577,7.043752,1.177005,1.592264,-2.799734,-3.892734,1.081122,7.531985,-7.184764,-2.369155,-6.985856,1.569580,-4.866695,-1.469063,-9.407143,4.276542,4.431389,-0.163445,0.965003,-4.552655,4.037910,2.791745,-8.150086,4.343464,8.762922,9.119372], dtype = "float64")#candidate|993|(352,)|const|float64
call_991 = relay.TupleGetItem(func_947_call(relay.reshape(var_992.astype('float32'), [6, 7, 6]), relay.reshape(const_993.astype('float64'), [2, 176]), relay.reshape(var_992.astype('float32'), [6, 7, 6]), ), 0)
call_994 = relay.TupleGetItem(func_952_call(relay.reshape(var_992.astype('float32'), [6, 7, 6]), relay.reshape(const_993.astype('float64'), [2, 176]), relay.reshape(var_992.astype('float32'), [6, 7, 6]), ), 0)
output = relay.Tuple([bop_981,call_991,var_992,const_993,])
output2 = relay.Tuple([bop_981,call_994,var_992,const_993,])
func_997 = relay.Function([var_979,var_992,], output)
mod['func_997'] = func_997
mod = relay.transform.InferType()(mod)
var_998 = relay.var("var_998", dtype = "float64", shape = ())#candidate|998|()|var|float64
var_999 = relay.var("var_999", dtype = "float32", shape = (252, 1))#candidate|999|(252, 1)|var|float32
output = func_997(var_998,var_999,)
func_1000 = relay.Function([var_998,var_999,], output)
mutated_mod['func_1000'] = func_1000
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1019 = relay.var("var_1019", dtype = "uint8", shape = (15, 13, 15))#candidate|1019|(15, 13, 15)|var|uint8
var_1020 = relay.var("var_1020", dtype = "uint8", shape = (15, 13, 15))#candidate|1020|(15, 13, 15)|var|uint8
bop_1021 = relay.maximum(var_1019.astype('uint8'), relay.reshape(var_1020.astype('uint8'), relay.shape_of(var_1019))) # shape=(15, 13, 15)
func_962_call = mod.get_global_var('func_962')
func_965_call = mutated_mod.get_global_var('func_965')
const_1026 = relay.const(False, dtype = "bool")#candidate|1026|()|const|bool
const_1027 = relay.const([False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,True], dtype = "bool")#candidate|1027|(1365,)|const|bool
call_1025 = relay.TupleGetItem(func_962_call(relay.reshape(const_1026.astype('bool'), []), relay.reshape(const_1027.astype('bool'), [13, 7, 15]), ), 0)
call_1028 = relay.TupleGetItem(func_965_call(relay.reshape(const_1026.astype('bool'), []), relay.reshape(const_1027.astype('bool'), [13, 7, 15]), ), 0)
output = relay.Tuple([bop_1021,call_1025,const_1026,const_1027,])
output2 = relay.Tuple([bop_1021,call_1028,const_1026,const_1027,])
func_1029 = relay.Function([var_1019,var_1020,], output)
mod['func_1029'] = func_1029
mod = relay.transform.InferType()(mod)
mutated_mod['func_1029'] = func_1029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mutated_mod.get_global_var('func_1029')
var_1031 = relay.var("var_1031", dtype = "uint8", shape = (15, 13, 15))#candidate|1031|(15, 13, 15)|var|uint8
var_1032 = relay.var("var_1032", dtype = "uint8", shape = (15, 13, 15))#candidate|1032|(15, 13, 15)|var|uint8
call_1030 = func_1029_call(var_1031,var_1032,)
output = call_1030
func_1033 = relay.Function([var_1031,var_1032,], output)
mutated_mod['func_1033'] = func_1033
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1073 = relay.var("var_1073", dtype = "float64", shape = ())#candidate|1073|()|var|float64
var_1074 = relay.var("var_1074", dtype = "float64", shape = (9, 16, 16))#candidate|1074|(9, 16, 16)|var|float64
bop_1075 = relay.mod(var_1073.astype('float64'), var_1074.astype('float64')) # shape=(9, 16, 16)
var_1080 = relay.var("var_1080", dtype = "float64", shape = (9, 16, 16))#candidate|1080|(9, 16, 16)|var|float64
bop_1081 = relay.minimum(var_1074.astype('int64'), relay.reshape(var_1080.astype('int64'), relay.shape_of(var_1074))) # shape=(9, 16, 16)
bop_1085 = relay.logical_xor(var_1073.astype('uint16'), bop_1075.astype('uint16')) # shape=(9, 16, 16)
bop_1088 = relay.bitwise_and(bop_1075.astype('uint64'), relay.reshape(bop_1081.astype('uint64'), relay.shape_of(bop_1075))) # shape=(9, 16, 16)
bop_1104 = relay.add(bop_1088.astype('float64'), var_1073.astype('float64')) # shape=(9, 16, 16)
uop_1115 = relay.log2(var_1074.astype('float32')) # shape=(9, 16, 16)
var_1124 = relay.var("var_1124", dtype = "uint64", shape = (9, 16, 16))#candidate|1124|(9, 16, 16)|var|uint64
bop_1125 = relay.greater_equal(bop_1088.astype('bool'), relay.reshape(var_1124.astype('bool'), relay.shape_of(bop_1088))) # shape=(9, 16, 16)
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
const_1132 = relay.const([-6,4,-2,-1,6,2,-7,-2,-4,-6,-1,-5,-5,4,-1,-7,-7,6,7,-6,3,10,3,-10,-6,3,9,4,2,5,10,-10,-3,8,-6,-3,-2,-10,7,-4,-8,-2,7,-2,7,-4,-7,6,3,-10,-10,-9,-5,9,-8,-5,-2,-3,7,9,3,3,-10,-2,4,-1,2,-9,8,9,3,-4,4,-3,3,7,7,-7,-10,9,10,8,-3,-1,5,9,-5,-2,-10,-10,-8,10,6,4,6,-9,5,-8,-2,-9,8,-6,1,-4,2,-4,2,6,1,3,5,-2,7,1,7,-10,-8,-2,2,-9,-1,-5,-7,10,-4,5,-4,2,-7,5,-2,10,9,10,7,8,-4,-10,7,-1,2,-10,3,10,-2,-3,-9,-6,-5,2,8,2,6,-5,6,3,1,6,5,3,10,4,9,8,8,9,-3,-10,-7,-1,10,-10,-9,-7,2,-4,6,-2,9,10,-1,5,-10,-2,-7,-9,-6,10,-3,10,6,8,3,8,9,9,-7,-3,-9,-5,7,-5,-10,8,3,9,-3,5,4,-8,-9,4,-3,-4,-3,9,2,-4,-3,6,-10,7,-1,-9,-4,-9,-4,-1,-1,9,6,5,-4,-10,1,2,2,-7,4,9,3,-2,-2,-3,-2,10,-2,5,4,-4,-5,8,-8,2,1,9,-1,10,-6,10,-7,7,7,-9,9,-6,10,4,7,1,9,-1,-2,8,5,-7,8,6,-6,-6], dtype = "uint16")#candidate|1132|(280,)|const|uint16
call_1131 = func_60_call(relay.reshape(const_1132.astype('uint16'), [10, 7, 4]))
call_1133 = func_60_call(relay.reshape(const_1132.astype('uint16'), [10, 7, 4]))
uop_1135 = relay.asin(uop_1115.astype('float32')) # shape=(9, 16, 16)
func_947_call = mod.get_global_var('func_947')
func_952_call = mutated_mod.get_global_var('func_952')
const_1142 = relay.const([-5.057861,-9.695616,4.607359,-1.841462,4.287706,7.262536,-4.561664,5.910685,-3.011663,6.841612,-1.505491,9.056967,-2.408378,2.231136,3.465681,4.501763,-2.474688,-3.698876,4.743038,-2.451266,-1.407117,-0.997639,-9.891581,2.986963,1.918514,9.383063,-5.271509,-8.215039,0.716406,-4.161779,6.178411,-9.580668,-0.713183,7.609131,3.930431,-9.381574,5.235255,-5.839135,-4.423925,-6.958294,-0.687605,-9.136355,-4.680494,-0.284535,-8.567755,1.893018,-2.607347,5.618341,-6.974349,-6.630196,-4.737540,-6.149620,9.481907,6.840777,-5.463621,-7.315678,-6.811295,6.587048,2.247438,-8.839924,0.876841,2.677975,7.035805,-1.331278,1.357445,9.112427,7.353025,7.488921,-8.385761,4.409797,0.799170,4.088918,-4.355282,-3.044307,-8.658385,0.812803,-4.519217,4.570546,7.717672,-8.296204,0.785250,-0.079745,3.974257,2.795591,-5.361930,-0.983231,-6.083887,3.146164,-7.453880,5.941173,-7.130228,-1.065322,8.322523,-0.557406,6.351272,-1.304427,-1.972800,-6.960395,-7.287205,8.065691,-1.740907,-2.259603,-0.096345,0.610455,-9.382813,2.064095,3.845728,2.836812,-4.459115,0.576058,-5.966373,-2.429719,-4.171032,-7.508503,-2.141645,7.682001,6.250320,-4.850361,-8.394588,7.184304,-7.933245,2.860612,-9.051946,-0.923602,5.698930,4.785333,2.411198,-0.912781,-8.075254,3.584329,5.009982,4.571796,-6.883942,-0.425565,4.028231,6.890893,-7.733014,3.539090,-4.161572,8.992753,5.315167,8.671319,-1.039726,-8.852134,6.988428,-1.018127,-4.796271,1.981577,0.371022,0.963496,9.727453,-1.616394,-0.666308,7.527739,9.895193,-4.141312,3.048840,-4.424488,5.231799,-4.271336,-3.255298,5.995193,-3.542052,6.031948,-3.497618,-5.369993,-6.363112,-3.618979,-0.025746,4.745635,-7.138919,-2.693281,3.453433,-7.341544,5.657840,1.500807,8.309836,-6.465386,-4.288487,1.325554,6.233146,-7.281401,-8.296299,-8.130798,-4.794998,-7.620898,0.730838,-2.674165,0.068756,9.842651,8.563869,-2.392920,-7.510106,-3.625739,7.329848,7.932672,1.081619,-7.906292,-1.515743,-4.305579,-5.829588,-6.017363,2.838383,-7.386124,8.894809,0.753178,9.950998,6.110415,3.047837,-6.546918,3.769178,4.236756,9.511461,-3.863012,-7.859443,1.500466,8.400709,-6.107490,-8.554606,-2.810436,-5.400215,1.159624,8.967272,9.903730,-4.831092,3.964330,-4.033510,7.667789,-0.387012,5.144419,-5.963294,8.107590,-1.809968,1.163879,7.122930,-1.802170,7.461191,3.760403,-6.213429,4.690250,-5.812126,-3.327195,8.151211,-3.648894,0.048078,-9.317598,-6.832574,-3.176053,2.800195,-4.847613,5.149072,4.203729], dtype = "float32")#candidate|1142|(252,)|const|float32
var_1143 = relay.var("var_1143", dtype = "float64", shape = (352,))#candidate|1143|(352,)|var|float64
call_1141 = relay.TupleGetItem(func_947_call(relay.reshape(const_1142.astype('float32'), [6, 7, 6]), relay.reshape(var_1143.astype('float64'), [2, 176]), relay.reshape(const_1142.astype('float32'), [6, 7, 6]), ), 0)
call_1144 = relay.TupleGetItem(func_952_call(relay.reshape(const_1142.astype('float32'), [6, 7, 6]), relay.reshape(var_1143.astype('float64'), [2, 176]), relay.reshape(const_1142.astype('float32'), [6, 7, 6]), ), 0)
func_997_call = mod.get_global_var('func_997')
func_1000_call = mutated_mod.get_global_var('func_1000')
call_1145 = relay.TupleGetItem(func_997_call(relay.reshape(var_1073.astype('float64'), []), relay.reshape(const_1142.astype('float32'), [252, 1]), ), 3)
call_1146 = relay.TupleGetItem(func_1000_call(relay.reshape(var_1073.astype('float64'), []), relay.reshape(const_1142.astype('float32'), [252, 1]), ), 3)
bop_1151 = relay.floor_mod(uop_1135.astype('float32'), relay.reshape(bop_1104.astype('float32'), relay.shape_of(uop_1135))) # shape=(9, 16, 16)
uop_1155 = relay.tan(uop_1135.astype('float32')) # shape=(9, 16, 16)
func_947_call = mod.get_global_var('func_947')
func_952_call = mutated_mod.get_global_var('func_952')
call_1157 = relay.TupleGetItem(func_947_call(relay.reshape(const_1142.astype('float32'), [6, 7, 6]), relay.reshape(call_1145.astype('float64'), [2, 176]), relay.reshape(const_1142.astype('float32'), [6, 7, 6]), ), 1)
call_1158 = relay.TupleGetItem(func_952_call(relay.reshape(const_1142.astype('float32'), [6, 7, 6]), relay.reshape(call_1145.astype('float64'), [2, 176]), relay.reshape(const_1142.astype('float32'), [6, 7, 6]), ), 1)
func_512_call = mod.get_global_var('func_512')
func_514_call = mutated_mod.get_global_var('func_514')
var_1161 = relay.var("var_1161", dtype = "int16", shape = (2, 420))#candidate|1161|(2, 420)|var|int16
call_1160 = relay.TupleGetItem(func_512_call(relay.reshape(var_1161.astype('int16'), [6, 10, 14])), 0)
call_1162 = relay.TupleGetItem(func_514_call(relay.reshape(var_1161.astype('int16'), [6, 10, 14])), 0)
output = relay.Tuple([bop_1085,bop_1125,call_1131,const_1132,call_1141,const_1142,var_1143,call_1145,bop_1151,uop_1155,call_1157,call_1160,var_1161,])
output2 = relay.Tuple([bop_1085,bop_1125,call_1133,const_1132,call_1144,const_1142,var_1143,call_1146,bop_1151,uop_1155,call_1158,call_1162,var_1161,])
func_1168 = relay.Function([var_1073,var_1074,var_1080,var_1124,var_1143,var_1161,], output)
mod['func_1168'] = func_1168
mod = relay.transform.InferType()(mod)
mutated_mod['func_1168'] = func_1168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1168_call = mutated_mod.get_global_var('func_1168')
var_1170 = relay.var("var_1170", dtype = "float64", shape = ())#candidate|1170|()|var|float64
var_1171 = relay.var("var_1171", dtype = "float64", shape = (9, 16, 16))#candidate|1171|(9, 16, 16)|var|float64
var_1172 = relay.var("var_1172", dtype = "float64", shape = (9, 16, 16))#candidate|1172|(9, 16, 16)|var|float64
var_1173 = relay.var("var_1173", dtype = "uint64", shape = (9, 16, 16))#candidate|1173|(9, 16, 16)|var|uint64
var_1174 = relay.var("var_1174", dtype = "float64", shape = (352,))#candidate|1174|(352,)|var|float64
var_1175 = relay.var("var_1175", dtype = "int16", shape = (2, 420))#candidate|1175|(2, 420)|var|int16
call_1169 = func_1168_call(var_1170,var_1171,var_1172,var_1173,var_1174,var_1175,)
output = call_1169
func_1176 = relay.Function([var_1170,var_1171,var_1172,var_1173,var_1174,var_1175,], output)
mutated_mod['func_1176'] = func_1176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1247 = relay.var("var_1247", dtype = "float64", shape = (3, 12, 1))#candidate|1247|(3, 12, 1)|var|float64
uop_1248 = relay.log10(var_1247.astype('float64')) # shape=(3, 12, 1)
func_354_call = mod.get_global_var('func_354')
func_358_call = mutated_mod.get_global_var('func_358')
const_1252 = relay.const(-3, dtype = "int64")#candidate|1252|()|const|int64
const_1253 = relay.const([-4,-6,-4,-8,8,-10,-6,-10,-1,2,-3,-1,-6,-9,1,7,-2,2,-3,-1,-6,9,-7,6,-7,9,-1,1,5,4,-1,-1,3,10,-4,6,1,-3,6,8,10,-5,6,-8,-9,6,3,-2,-1,-4,-5,-6,-6,7,-10,7,-2,1,-10,10,-1,-7,6,-3,-4,-3,-9,-7,7,7,1,-7,6,-1,-7,6,-9,-2,-4,1,4,-9,2,6,-4,-7,8,-7,2,-3,-1,6,-3,7,3,-7,4,8,4,7,10,2,-10,2,-1,10,3,-3,2,4,-8,2,9,-7,-5,-10,8,3,-2,-9,-2,-4,5,-3,-7,-4,-10,-6,8,3,-8,10,-6,6,-2,1,-6,-10,2,9,2,4,-4,2,-6,7,9,-1,-2,3,2,9,8,-10,-5,-10,4,1,-4,10,-8,-3,-6,-2,-3,-4,6,4,5,4,3,-8,-8,7,-2,2,-5,8,1,-2,4,1,1,4,9,5,2,1,2,1,-4,-5,2,-10,3,7,-8,-7,-6,-5,1,-9,3,4,-7,-9,-10,9,8,-4,3,-8,4,2,-8,-4,-6,3,-2,-7,4,9,-10,7,-10,-7,-4,6,2,-7,4,1,-6,-3,1,-7,-4,8,-7,-2,-6,1,-5,10,-4,8,-10,-2,-1,-5,3,-7,8,-2,2,1,-2,10,9,5,-6,-3,-1,-1,10,-7,7,3,-1,2,9,-1,-8,-10,-8,-2,7,-1,10,1,9,4,-3,-3,2,-10,-1,-1,2,7,6,6,-3,-2,-8,-5,-2,-3,4,1,-3,6,-4,4,10,-7,9,2,10,-6,-10,5,10,8,6,-1,-4,5,-5,3,-8,-4,4,8,-3,-4,5,-6,9,-10,-5,4,-5,-7,-7,8,1,-2,-9,8,-9,4,4,-9,-3,-8,8,-10,-2,-7,-5,6,-6,-10,-1,6,3,-3,1,-9,-3,-5,-10,7,-9,-5,-7,10,-9,10,-1,1,-8,10,-8,-4,-6,3,-3,2,-3,6,-5,-5,9,6,4,5,-2,3,-1,-3,5,5,-4,-10,3,9,4,-4,-1,-4,-8,7,1,-3,7,1,2,10,2,-5,7,5,-9,-6,-1,-5,9,-10,10,-7,9,-10,4,7,1,-3,7,2,8,8,8,8,-3,-2,-4,-1,6,6,-3,-8,-6,-3,-10,10,-2,-9,2,-10,8,10,-10,6,2,4,4,10,-4,4,-9,-5,-5,-1,-2,1,-2,1,-2,6,9,-9,-3,-5,-3,4,-7,1,1,-10,3,-2,-4,7,-10,-2,-4,-3,2,-5,-7,5,7,-8,9,1,1,7,6,3,-6,4,8,6,-5,4,-9,8,4,4,7,-5,9,-6,-7,-3,-6,4,6,1,-2,-5,-4,9,-10,3,-10,-6,4,4,-10,6,-5,9,2,-1,7,-7,9,-10,9,-6,6,8,5,3,10,-3,-2,4,-4,-10,3,1,3,2,-9,-1,-2,4,4,5,9,-8,-10,-8,-9,5,-6,-3,10,-3,4,1,-4,5,6,-3,-8,7,5,-2,6,8,2,2,-7,-10,-8,8,7,3,3,-8,7,9,-5,-10,-8,4,2,-3,-1,-1,-3,-5,6,6,4,-2,-1,4,-4,6,3,-2,-6,-5,8,-5,8,-3,-8,4,3,10,7,-2,10,-2,8,9,1,-10,-1,1,-5,-4,5,2,3,4,9,10,-5,-4,6,-8,9,-5,-3,2,1,10,5,6,7,10,7,5,2,-7,-1,5,-3,10,7,5,-9,5,-8,-2,8,-10,1,7,3,2,-8,-5,7,8,-9,-1,-9,-2,5,1,5,-10,-7,10,2,-5,6,3,5,-7,-4,3,-7,10,9,7,5,8,8,-1,9,3,5,-9,7,7,6,-5,-4,-5,8,-7,-1,4,-5,2,-2,9,10,2,-6,1,10,7,2,-9,3,-3,2,-8,2,-1,2,4,10,1,4,9,7,9,7,-8,-3,7,-8,-2,-4,7,-3,-9,-8,8,-2,7,3,9,-6,-10,-7,6,-3,-8,-3,2,7,-6,2,8,-3,1,2,7,8,9,-4,3,-5,-4,-5,2,-6,6,6,-1,-8,6,4,-8,-9,-8,-1,-2,-1,3,-1,-7,-5,6,-6,8,-1,3,-6,-8,7,-1,6,-3,8,-2,-10,9,-3,-5,-1,-4,-9,-10,10,-1,-5,-3,6,7,-1,4,-9,7,7,2,4,2,4,10,9,1,4,4,-2,-3,-1,6,-9,9,-4,-3,6,-4,7,-4,-5,-2,-1,-8,-9,-5,7,8,4,-1,-10,-7,-2,-9,-2,9,10,-6,-10,-3,5,-9,1,10,7,-4,-10,7,1,-2,1,-2,-3,-3,5,1,-5,-4,-8,-4,10,5,-6,-9,-8,-9,2,-1,10,-7,-1,-6,-7,-5,-7,-1,4,4,-6,-8,-5,5,-10,2,2,6,-8,-10,-3,9,3,-6,3,10,6,-6,-6,-10,-9,10,-4,7,-9,6,-3,3,-2,-6,10,6,3,-8,-5,9,5,-7,4,-2,2,-6,-10,2,7,-8,-1,4,8,-7,4,-7,3,-9,-10,9,-6,7,-3,9,5,8,4,4,-6,3,4,1,7,-4,1,-9,10,7,4,-1,5,-9,-1,-9,1,-1,3,2,-1,7,10,3,3,-1,-5,-8,-4,-7,9,6,-9,4,-6,-4,-1,-3,8,-2,5,7,-10,10,1,10,5,-9,2,8,10,-7,2,5,-5,10,10,9,2,3,7,5,-1,8,-10,1,8,-2,-9,2,-3,5,-10,3,-6,-7,-2,-6,-9,-4,1,-8,5,-3,6,-10,10,2,10,5,-6,8,7,10,-10,-4,2,-4,-3,-1,4,9,7,-5,-1,-4,3,2,7,5,-8,10,2,-9,1,-3,3,9,5,10,4,-10,7,-4,-8,4,7,-8,-10,-3,8,5,10,-5,10,3,-9,-1,-9,-3,-6,-2,2,4,-6,-2,5,-10,-3,-3,10,7,1,8,-2,6,1,-3,-8,5,-3,2,6,4,7,-4,-1,8,8,-3,-10,-10,-5,-4,-9,-8,-7,2,-2,-5,-2,-8,10,7,4,2,-7,5,-5,-6,9,9,-4,-1,5,-5,-5,-10,-9,-6,-4,-8,-9], dtype = "int64")#candidate|1253|(1183,)|const|int64
var_1254 = relay.var("var_1254", dtype = "uint16", shape = (280,))#candidate|1254|(280,)|var|uint16
call_1251 = relay.TupleGetItem(func_354_call(relay.reshape(const_1252.astype('int64'), []), relay.reshape(const_1253.astype('int64'), [7, 13, 13]), relay.reshape(var_1254.astype('uint16'), [280,]), ), 2)
call_1255 = relay.TupleGetItem(func_358_call(relay.reshape(const_1252.astype('int64'), []), relay.reshape(const_1253.astype('int64'), [7, 13, 13]), relay.reshape(var_1254.astype('uint16'), [280,]), ), 2)
func_1029_call = mod.get_global_var('func_1029')
func_1033_call = mutated_mod.get_global_var('func_1033')
var_1261 = relay.var("var_1261", dtype = "uint8", shape = (2925,))#candidate|1261|(2925,)|var|uint8
call_1260 = relay.TupleGetItem(func_1029_call(relay.reshape(var_1261.astype('uint8'), [15, 13, 15]), relay.reshape(var_1261.astype('uint8'), [15, 13, 15]), ), 2)
call_1262 = relay.TupleGetItem(func_1033_call(relay.reshape(var_1261.astype('uint8'), [15, 13, 15]), relay.reshape(var_1261.astype('uint8'), [15, 13, 15]), ), 2)
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
call_1268 = func_60_call(relay.reshape(var_1254.astype('uint16'), [10, 7, 4]))
call_1269 = func_60_call(relay.reshape(var_1254.astype('uint16'), [10, 7, 4]))
func_962_call = mod.get_global_var('func_962')
func_965_call = mutated_mod.get_global_var('func_965')
const_1274 = relay.const([True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True], dtype = "bool")#candidate|1274|(1365,)|const|bool
call_1273 = relay.TupleGetItem(func_962_call(relay.reshape(const_1252.astype('bool'), []), relay.reshape(const_1274.astype('bool'), [13, 7, 15]), ), 0)
call_1275 = relay.TupleGetItem(func_965_call(relay.reshape(const_1252.astype('bool'), []), relay.reshape(const_1274.astype('bool'), [13, 7, 15]), ), 0)
bop_1280 = relay.logical_or(uop_1248.astype('bool'), var_1261.astype('bool')) # shape=(3, 12, 2925)
output = relay.Tuple([call_1251,const_1252,const_1253,var_1254,call_1260,call_1268,call_1273,const_1274,bop_1280,])
output2 = relay.Tuple([call_1255,const_1252,const_1253,var_1254,call_1262,call_1269,call_1275,const_1274,bop_1280,])
func_1292 = relay.Function([var_1247,var_1254,var_1261,], output)
mod['func_1292'] = func_1292
mod = relay.transform.InferType()(mod)
var_1293 = relay.var("var_1293", dtype = "float64", shape = (3, 12, 1))#candidate|1293|(3, 12, 1)|var|float64
var_1294 = relay.var("var_1294", dtype = "uint16", shape = (280,))#candidate|1294|(280,)|var|uint16
var_1295 = relay.var("var_1295", dtype = "uint8", shape = (2925,))#candidate|1295|(2925,)|var|uint8
output = func_1292(var_1293,var_1294,var_1295,)
func_1296 = relay.Function([var_1293,var_1294,var_1295,], output)
mutated_mod['func_1296'] = func_1296
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1390 = relay.var("var_1390", dtype = "int32", shape = (1, 15, 15))#candidate|1390|(1, 15, 15)|var|int32
var_1391 = relay.var("var_1391", dtype = "int32", shape = (7, 15, 15))#candidate|1391|(7, 15, 15)|var|int32
bop_1392 = relay.maximum(var_1390.astype('int32'), var_1391.astype('int32')) # shape=(7, 15, 15)
output = bop_1392
output2 = bop_1392
func_1409 = relay.Function([var_1390,var_1391,], output)
mod['func_1409'] = func_1409
mod = relay.transform.InferType()(mod)
mutated_mod['func_1409'] = func_1409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1409_call = mutated_mod.get_global_var('func_1409')
var_1411 = relay.var("var_1411", dtype = "int32", shape = (1, 15, 15))#candidate|1411|(1, 15, 15)|var|int32
var_1412 = relay.var("var_1412", dtype = "int32", shape = (7, 15, 15))#candidate|1412|(7, 15, 15)|var|int32
call_1410 = func_1409_call(var_1411,var_1412,)
output = call_1410
func_1413 = relay.Function([var_1411,var_1412,], output)
mutated_mod['func_1413'] = func_1413
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1627 = relay.const([[[-8.059542,-8.352704,-4.538349,-5.441651,-1.980210,-0.623242,-9.354354],[0.824366,5.846758,2.060530,-6.654226,-7.648348,2.254778,3.763767],[5.626694,1.426106,6.725861,-0.035599,-7.316278,-7.236414,-3.920529],[-6.820995,0.589818,-2.363340,-4.432700,-8.513919,4.077047,-1.510572]],[[6.070196,-0.042206,1.081274,-2.444981,2.827192,-2.548555,-8.805468],[-2.880096,-0.088598,3.548839,2.547005,-3.315017,2.191718,-5.195899],[9.582870,-1.049431,-8.872186,1.918015,-3.655617,5.409975,-1.831928],[1.590116,-6.927645,-7.486904,-5.037531,6.486205,8.869286,9.260590]],[[-8.039721,6.636158,4.733210,0.234042,-7.941184,1.574210,-8.078647],[-4.669958,-0.857303,6.659540,-7.767840,5.215407,-4.009395,-2.178070],[-0.428831,-3.824619,2.427528,-9.695012,8.887996,-4.206090,-7.615733],[-9.848524,-5.193142,-2.367674,-0.436906,-2.079617,8.941112,-8.041964]],[[-5.538228,8.992593,-3.054596,4.944100,3.739143,-9.409686,7.811107],[8.582189,-7.140431,2.247364,-8.642018,-7.849364,5.277720,9.840871],[-2.598431,-0.650514,-5.154029,-6.570241,-0.307871,-9.264169,9.845550],[-0.322791,-3.913303,3.752428,-1.273154,3.361802,-7.388620,1.131718]],[[-3.303091,-4.086906,-6.078714,6.590711,-6.246141,-1.957105,-8.713598],[-2.187062,1.835754,-7.800862,-8.208167,4.905711,-0.964261,-6.550146],[-4.264186,0.521682,-0.504066,9.959088,-1.566196,-1.658264,-5.643102],[9.175450,7.194226,0.719359,4.627398,-2.294506,5.353592,-1.894579]],[[0.051699,-0.907113,-1.251460,-0.548896,0.030325,-0.023947,5.401495],[-0.621483,6.473155,-3.286420,1.867657,4.029226,0.953453,3.590527],[1.087786,5.582343,-1.304524,-8.690209,7.461537,5.414252,3.840818],[-8.424114,-6.127247,-6.629173,8.867933,2.928759,-6.377283,3.707026]],[[-1.881003,-2.012488,-1.139436,-5.445754,3.610642,2.512224,-5.279300],[1.805627,-6.834946,-1.927610,-6.210214,-0.653436,6.843353,2.810790],[5.661491,0.984636,3.062761,7.319581,4.356873,-7.850008,0.998258],[5.271269,-3.656911,2.475212,2.608477,-7.307715,-1.221153,1.200100]],[[-3.980836,-0.960452,6.074120,3.583370,1.648990,-1.104428,8.275089],[-3.106445,-5.421973,-1.495751,-7.840386,-9.310685,1.310271,-8.605647],[3.800702,8.846690,-5.584423,7.451902,2.257412,-9.573691,-8.942082],[-0.818808,8.657065,-8.730697,-5.254537,-0.277359,-8.229011,-9.389901]],[[0.038274,0.460462,-5.065378,-8.569510,-5.402665,-0.224220,1.614317],[2.773847,2.920702,9.640690,-3.220238,9.723394,-3.622263,0.268388],[-3.206051,-6.411995,-4.752012,-5.383434,-3.044528,3.677867,4.277060],[-8.562604,-5.712227,-7.075351,5.765379,-1.936535,6.363965,2.077448]],[[-9.434255,-0.102709,-8.064426,-7.833915,-6.839124,-0.316149,-8.402062],[-6.450985,3.513665,-4.259337,-2.917817,-6.503716,-3.573971,3.817039],[-0.891124,1.913622,4.952840,3.981349,-8.687627,7.455518,-2.928456],[9.701452,2.887427,-2.658056,-8.630191,2.676388,7.784657,8.715331]],[[-9.515017,5.100539,3.667232,6.417851,-5.721206,-3.787205,0.684159],[-5.542202,4.114984,-6.922812,5.222717,-6.336663,5.186559,-8.532178],[1.299789,-1.706882,-5.665345,-3.754479,-2.407945,-9.891146,-2.902821],[3.957952,-1.082661,8.772417,5.725080,5.690639,5.199210,-5.873226]]], dtype = "float32")#candidate|1627|(11, 4, 7)|const|float32
uop_1628 = relay.cos(const_1627.astype('float32')) # shape=(11, 4, 7)
output = relay.Tuple([uop_1628,])
output2 = relay.Tuple([uop_1628,])
func_1632 = relay.Function([], output)
mod['func_1632'] = func_1632
mod = relay.transform.InferType()(mod)
output = func_1632()
func_1633 = relay.Function([], output)
mutated_mod['func_1633'] = func_1633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_1686 = relay.TupleGetItem(func_1632_call(), 0)
call_1687 = relay.TupleGetItem(func_1633_call(), 0)
var_1688 = relay.var("var_1688", dtype = "float32", shape = (11, 4, 7))#candidate|1688|(11, 4, 7)|var|float32
bop_1689 = relay.power(call_1686.astype('float32'), relay.reshape(var_1688.astype('float32'), relay.shape_of(call_1686))) # shape=(11, 4, 7)
bop_1692 = relay.power(call_1687.astype('float32'), relay.reshape(var_1688.astype('float32'), relay.shape_of(call_1687))) # shape=(11, 4, 7)
output = relay.Tuple([bop_1689,])
output2 = relay.Tuple([bop_1692,])
func_1699 = relay.Function([var_1688,], output)
mod['func_1699'] = func_1699
mod = relay.transform.InferType()(mod)
mutated_mod['func_1699'] = func_1699
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1700 = relay.var("var_1700", dtype = "float32", shape = (11, 4, 7))#candidate|1700|(11, 4, 7)|var|float32
func_1699_call = mutated_mod.get_global_var('func_1699')
call_1701 = func_1699_call(var_1700)
output = call_1701
func_1702 = relay.Function([var_1700], output)
mutated_mod['func_1702'] = func_1702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_1710 = relay.TupleGetItem(func_1632_call(), 0)
call_1711 = relay.TupleGetItem(func_1633_call(), 0)
func_512_call = mod.get_global_var('func_512')
func_514_call = mutated_mod.get_global_var('func_514')
const_1713 = relay.const([-7,10,6,-5,2,5,-10,4,2,6,4,4,7,2,-4,-3,-3,2,7,-4,-9,3,-2,9,-10,1,-8,-10,10,-6,-4,5,3,5,-5,9,10,3,8,-7,8,4,4,10,7,8,6,9,1,9,4,7,-1,5,4,-10,1,-8,-10,-1,-6,-10,-2,-10,-2,-6,7,2,6,9,-1,-4,-7,-1,1,-5,1,-9,-4,-6,8,-7,-7,-4,8,5,-6,-4,-1,1,-7,1,4,10,7,-6,-10,-1,-4,2,-2,-1,-5,-1,-10,-2,-9,-6,3,10,-4,6,-1,-10,3,5,10,2,-1,-4,3,1,-9,4,-4,1,-3,1,5,9,5,1,-1,3,-8,-6,-4,-5,-3,4,-5,5,-5,2,-10,-6,-6,-2,-4,3,-1,4,-6,-10,-8,-8,1,-9,-4,6,5,-10,-1,-9,7,-6,1,-6,9,-7,10,9,1,-10,10,-8,8,-5,-2,5,-8,-2,2,-5,-3,7,-10,-7,-6,-7,-10,3,-6,-6,-5,-10,1,2,-9,4,1,-5,8,3,8,-2,6,-6,-4,-1,-3,-1,-2,-8,10,-4,3,-2,-3,7,-7,-2,2,7,10,4,10,8,8,4,-9,-9,-2,-5,7,8,3,-9,6,3,-6,9,-2,-8,4,8,-4,6,-9,-1,-5,4,-7,-2,-1,-8,2,2,6,-4,-4,2,1,-4,-10,-9,-3,10,-6,-2,-9,-3,-2,3,-7,-8,1,-10,9,5,8,2,-8,1,9,2,-8,7,10,-7,8,7,-5,-4,-1,-2,4,10,10,-6,9,-5,3,-4,-1,-9,6,2,4,-6,4,4,5,10,9,2,-5,2,8,-10,-9,-2,6,-8,10,5,-5,-4,7,6,1,4,7,-4,4,-8,3,-9,3,-9,-5,-7,-3,1,-6,-6,8,-4,5,-2,10,-3,-9,3,-2,-5,5,7,4,10,8,-8,7,3,-10,1,6,-4,-8,7,7,9,3,-4,6,6,3,2,5,-9,10,-4,6,1,5,6,-9,8,10,6,7,10,5,-7,7,3,10,6,-5,1,-7,4,9,6,3,5,-6,-9,9,9,-3,-7,-2,-8,2,-7,-6,2,2,-5,2,4,-9,8,8,-5,-2,4,7,-10,-1,7,9,-3,7,-7,-9,8,-3,-5,-4,2,3,1,-7,-9,10,-6,-5,-10,-6,-3,10,-3,6,6,8,-7,5,3,8,10,5,-7,-2,3,5,-3,7,-6,3,4,-9,4,-8,-5,8,2,-1,6,-5,-3,6,5,-1,-6,-2,-8,9,6,1,-4,9,2,7,5,-8,-4,4,6,8,-2,2,5,3,1,-3,3,-10,-1,-5,-9,-5,-5,-10,-6,5,-3,9,-8,-9,8,-3,5,-8,-10,-5,7,-2,10,-5,2,-4,9,-3,10,6,-6,-1,-2,-1,3,9,-7,4,3,-4,1,2,-5,-7,-8,3,1,9,2,-4,-6,-4,-4,-2,10,-3,-8,-1,1,8,-10,-5,4,2,4,10,1,-2,-4,3,2,5,3,3,-1,-5,-9,-1,4,8,1,7,1,8,-6,9,9,8,-9,9,-9,2,5,-2,9,9,7,4,7,-5,-5,3,-10,9,9,1,10,-9,-7,4,-2,-7,-8,8,5,10,-2,5,1,1,-9,1,6,-4,10,8,-2,-10,-8,-6,6,2,-7,9,-8,-2,-5,-6,-1,-3,-8,-3,-5,-1,-3,-5,-2,-4,1,-1,-6,-4,3,1,10,-5,2,-1,10,2,-10,2,-2,-5,2,2,6,-8,-7,3,2,8,-7,-2,2,10,-9,-5,1,-3,-5,-10,10,2,-10,5,-4,-5,-5,-7,3,10,-2,-2,-5,5,-10,1,-6,9,9,-5,8,-3,8,-1,-1,-2,6,-5,3,-2,-6,4,7,7,7,8,-5,10,3,6,-2,7,4,-2,-4,9,1,-4,-9,4,-5,3,7,5,7,-6,-10,1,-6,1,9,-2,5,7,-8,-10,-7,-5,8,-4,9,-6,-2,-3,9,-8,5,-7,5,2,8,8,-5,-10,3,10,4,3,2,-4,-1,9,4,4,-3,5,-10,-7,-6,-10,10,2,-3,-2,2,-5,-10,-9,-2,4,-3,5,9,-8,10,3,5,8,10,-6,5,7,6,10,1,3,10,-5,3,-8,-1,-5,-8,-8,-2,-3,6,2,6,-1,-5,-10,6,8,1,2,-6,-10,-9,-3,5], dtype = "int16")#candidate|1713|(840,)|const|int16
call_1712 = relay.TupleGetItem(func_512_call(relay.reshape(const_1713.astype('int16'), [6, 10, 14])), 0)
call_1714 = relay.TupleGetItem(func_514_call(relay.reshape(const_1713.astype('int16'), [6, 10, 14])), 0)
uop_1715 = relay.asin(call_1712.astype('float32')) # shape=(6, 10, 14)
uop_1717 = relay.asin(call_1714.astype('float32')) # shape=(6, 10, 14)
func_1699_call = mod.get_global_var('func_1699')
func_1702_call = mutated_mod.get_global_var('func_1702')
call_1732 = relay.TupleGetItem(func_1699_call(relay.reshape(call_1710.astype('float32'), [11, 4, 7])), 0)
call_1733 = relay.TupleGetItem(func_1702_call(relay.reshape(call_1710.astype('float32'), [11, 4, 7])), 0)
uop_1735 = relay.sin(call_1712.astype('float32')) # shape=(6, 10, 14)
uop_1737 = relay.sin(call_1714.astype('float32')) # shape=(6, 10, 14)
output = relay.Tuple([call_1710,const_1713,uop_1715,call_1732,uop_1735,])
output2 = relay.Tuple([call_1711,const_1713,uop_1717,call_1733,uop_1737,])
func_1742 = relay.Function([], output)
mod['func_1742'] = func_1742
mod = relay.transform.InferType()(mod)
mutated_mod['func_1742'] = func_1742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1742_call = mutated_mod.get_global_var('func_1742')
call_1743 = func_1742_call()
output = call_1743
func_1744 = relay.Function([], output)
mutated_mod['func_1744'] = func_1744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1742_call = mod.get_global_var('func_1742')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_1794 = relay.TupleGetItem(func_1742_call(), 1)
call_1795 = relay.TupleGetItem(func_1744_call(), 1)
uop_1805 = relay.exp(call_1794.astype('float32')) # shape=(840,)
uop_1807 = relay.exp(call_1795.astype('float32')) # shape=(840,)
func_1029_call = mod.get_global_var('func_1029')
func_1033_call = mutated_mod.get_global_var('func_1033')
const_1825 = relay.const([-1,-8,-4,-5,-5,-5,-4,-9,-1,-6,3,-8,-1,-9,-6,-5,-3,-10,-5,-6,-3,7,-1,-10,1,7,-5,-4,3,7,4,-8,7,6,3,2,4,-3,-8,-7,-9,10,1,-2,-7,-6,1,10,2,-9,9,-10,3,-7,-8,-7,-1,3,-2,6,4,-4,8,4,-1,4,6,-2,1,7,8,-6,-4,-10,-2,10,10,2,8,-7,-8,-7,-9,3,-2,9,6,-8,-4,9,-7,-3,-2,5,8,-7,5,3,6,-3,-8,-8,-6,7,5,8,-6,10,-4,8,-1,2,-10,1,1,-6,-4,5,1,4,1,-9,-10,5,-6,-8,9,-2,-5,6,-6,-8,5,4,7,-1,7,3,10,3,-2,-4,3,1,10,-5,-8,-7,-6,10,-9,10,-2,3,-5,-10,9,8,-2,9,6,8,-7,-10,6,-6,2,10,1,8,10,-4,3,-1,3,-7,-4,-5,-10,5,5,-10,7,1,-3,-7,10,-4,-3,8,-6,3,9,-2,2,-6,9,4,-8,-8,-5,-8,4,7,-8,3,1,-6,5,3,7,4,7,-4,4,-8,6,-5,-7,-10,-9,-8,9,5,2,-1,7,-5,-5,9,-10,10,2,-8,8,-3,9,9,5,-1,-4,-6,-10,-5,-9,-6,-3,6,-2,4,4,-8,9,2,5,-1,-8,10,-7,4,-1,-8,7,-2,10,-10,5,7,9,-8,-3,-1,-5,10,8,-1,-6,-5,-2,-3,-5,5,3,4,1,4,10,-8,8,10,-4,5,7,-5,9,1,1,5,-10,-5,10,9,-9,-8,5,-3,8,-10,-7,6,-3,1,-5,-7,5,5,5,9,1,1,5,4,9,10,9,4,-3,5,3,-10,-5,-6,-1,4,-2,5,-8,-3,-6,-5,-7,6,-5,-5,-4,7,-1,4,9,3,5,-3,8,-10,-6,-1,3,2,-10,-6,-3,-8,7,-8,9,10,-9,5,-6,4,-9,7,-2,-9,8,-9,-6,7,6,-2,7,9,4,3,-10,-3,10,8,-1,-4,-2,-1,-7,-2,4,-10,-5,-6,4,10,-4,2,5,6,8,-6,-1,9,-5,-3,-6,-1,5,-1,-7,-4,5,5,-7,-5,-8,-7,8,-9,8,4,-8,-4,-2,-1,-5,-10,-10,-10,5,-3,-8,6,-6,-9,-8,8,-9,6,-9,-2,1,-7,-8,-9,4,-8,2,-8,-10,7,-1,-3,-9,-4,5,7,10,6,-10,-1,-6,-7,-4,1,4,-3,2,5,-4,-2,-7,-6,2,4,-6,8,-5,-2,-2,4,-10,-10,2,4,8,-6,4,1,3,-9,2,3,-2,8,-10,1,9,2,1,-7,5,-4,-5,-6,10,-7,1,-2,5,-9,2,4,-1,5,4,1,-7,-8,-9,9,10,-4,8,-3,5,9,-2,-1,1,5,1,-5,-10,-9,9,-10,7,-9,-9,-7,4,2,-9,1,10,-7,3,-9,7,1,7,-7,7,-9,-8,-1,-4,-10,-7,-5,8,-9,-4,-3,-6,10,-8,-10,-3,-1,9,5,8,-8,-8,-5,-5,-5,-3,-3,-5,-6,2,-7,-7,7,-4,-9,10,7,-2,-4,7,7,10,-10,-5,-7,2,-3,4,-5,2,9,3,2,10,-2,9,-6,-3,3,3,-4,-4,6,-7,-4,-6,3,-1,-7,-4,8,10,2,2,-1,5,-2,4,-5,-8,2,-2,-5,1,-3,-1,-10,-5,-4,8,-4,1,-10,-3,-8,3,-8,4,-7,-5,1,9,9,-4,3,-8,-4,2,-6,10,7,-1,-8,8,1,4,-1,5,-9,1,-2,-6,10,2,-2,-9,8,3,6,-3,-3,8,2,-4,-2,-10,5,-3,-5,-10,-9,-7,10,7,9,2,-7,-8,6,9,-8,-4,-6,-8,2,-1,9,-2,-7,-5,-8,-2,9,-1,1,-3,-10,2,4,8,-7,8,6,7,10,-2,8,1,-4,-10,-4,-4,2,10,-5,1,-9,10,-1,-1,-8,7,-8,3,3,-7,-8,3,6,-5,2,-2,5,6,-8,8,1,10,-6,-1,8,-7,-10,6,4,6,-7,6,-2,-9,1,-6,3,-2,-1,-9,3,-5,6,1,-5,5,7,4,-4,-2,10,-7,-4,-3,2,-1,-8,9,10,-2,-7,6,8,5,-3,-9,3,-6,-5,-9,1,-1,8,10,10,-4,-1,-10,10,-5,2,-4,9,1,10,-10,-2,9,3,-2,3,9,-6,-7,4,-7,-5,3,-4,-6,4,7,-7,8,6,-10,-5,5,9,8,-1,2,-8,9,-7,8,9,9,-10,5,-6,4,-5,3,-10,-9,-3,-8,4,-5,-2,-4,8,8,-10,-5,9,8,-10,-10,-9,1,10,7,7,-6,-4,-2,6,2,3,4,7,-10,10,-7,-8,3,10,-3,1,-7,-2,7,7,7,7,3,-1,10,2,-2,-8,10,6,-6,-5,-2,-2,-8,-8,-10,-4,10,-6,1,-8,2,-10,3,-8,-1,-1,-1,-1,1,-1,6,-4,3,7,-1,6,2,-8,2,-3,10,-7,7,9,9,1,-7,2,-6,-5,5,-2,9,-3,7,-5,1,9,10,-8,-10,-4,3,-1,6,-9,1,-7,1,-3,-5,-7,-10,6,4,9,-2,-3,1,-7,-1,-8,-8,-3,5,9,-4,-10,-3,-6,-10,-3,10,-1,-9,7,-5,-2,-10,-3,-1,-8,-1,3,5,-2,-6,1,-2,-6,1,3,-10,10,-10,-6,-7,7,-3,3,10,4,2,-4,6,-5,5,4,3,-5,6,3,6,-1,-2,6,10,10,3,-6,3,-7,-9,4,-2,-2,-10,4,-7,-4,9,-1,-2,-3,-2,-6,-10,3,-4,9,4,6,8,-10,5,6,-6,7,7,-2,8,-5,-1,-8,-5,-10,-10,-5,-6,-5,-8,7,7,1,3,-6,1,1,-2,-6,-6,8,-5,-8,7,-4,-6,1,6,-9,5,-9,-9,-8,-9,-7,-1,3,-5,8,6,-7,4,6,-9,-6,2,-1,-8,-1,-5,2,-3,-3,7,10,-3,6,8,5,8,-4,-1,-1,-5,-5,-1,6,3,-4,-1,6,5,1,-5,-1,-2,-3,-1,1,9,6,-5,5,2,-10,4,-8,9,10,-6,7,5,2,-6,-2,8,-6,10,1,-1,-6,-9,3,4,2,-6,9,-10,-7,-3,-3,7,-6,-3,1,-9,8,-3,-4,6,-6,-6,4,-5,4,2,-1,-1,7,3,7,-9,8,5,7,-1,-4,10,-2,-8,7,8,-8,2,-10,-5,6,3,6,-9,1,-9,-4,-2,-6,-7,-10,-10,1,-6,-8,9,7,-10,-9,-7,9,-5,5,-1,8,5,-2,-6,8,5,3,1,-5,-2,-2,-5,4,-3,-9,-1,4,-3,-2,9,-9,5,-8,9,-7,-10,-9,-9,-6,2,-9,-10,-1,-9,-2,-1,7,-10,-2,8,1,10,2,-2,2,-4,9,3,-9,-2,-5,9,-1,-6,-1,4,-4,-3,-4,7,-1,6,-6,-1,-5,5,8,-1,4,-3,4,6,-4,4,-6,-3,-3,8,-9,-6,1,-4,5,7,-5,-4,-10,6,-1,-9,3,-5,-2,-6,1,-7,3,-3,-7,6,1,-10,10,4,-6,8,6,4,6,2,3,-2,-1,3,-5,9,-8,-8,4,-10,6,8,3,3,3,7,-3,2,-3,-3,5,4,-10,4,6,-4,5,-4,5,6,-3,8,1,1,7,2,-5,-7,-3,-10,-8,9,8,10,3,5,-10,-3,3,6,-7,3,-7,8,3,6,6,-5,-3,10,-2,1,8,-2,9,2,-6,-7,-7,-10,-6,-4,-4,-7,-5,-2,-3,-8,10,-3,-9,2,-2,-8,-5,-1,-7,-3,5,9,-6,8,5,-2,7,-3,-10,4,5,1,2,-2,7,1,3,4,10,-1,-8,-1,8,-5,-8,-10,-1,-2,-5,4,-10,-5,-7,-6,-3,-4,-10,7,-7,-6,-1,8,9,9,-6,7,-9,1,-3,3,-2,6,1,9,6,-5,-4,-3,2,-7,4,-4,-8,9,10,5,10,-5,7,-1,1,-1,8,8,-5,-8,-10,-4,-9,-10,-6,2,-8,-6,-3,7,-2,9,-4,10,1,-10,2,9,-8,10,-4,1,1,7,8,-10,-2,-10,5,8,8,6,4,3,4,8,-8,-2,-10,-7,-10,-9,-5,1,-9,-5,-6,8,8,-2,7,-2,10,-7,2,-1,10,-7,8,-4,-6,3,2,10,5,4,-1,-8,-10,-5,7,-7,5,2,1,-10,7,-6,5,8,-9,3,-9,-3,3,3,6,-7,-3,6,-4,-10,-10,-9,4,6,-10,-3,9,9,-8,2,-2,6,-9,-1,9,-4,-2,5,-10,9,-1,8,2,1,-10,5,3,9,-4,-5,-4,3,3,1,-10,-3,7,-8,-1,-1,4,-4,7,-7,6,5,2,-5,5,-8,8,-3,-7,6,-2,8,2,2,-7,-2,2,2,-3,-1,-5,-3,-2,-10,1,-4,2,10,-8,-3,3,8,3,1,7,6,1,-4,8,-10,9,-2,10,7,4,10,7,3,8,-6,8,-8,3,-3,-8,-10,9,-10,-3,6,6,3,6,3,-3,-2,3,1,-3,-7,-7,10,8,-4,6,8,-8,5,-8,9,-7,2,10,-6,-8,-4,9,-9,-5,-9,5,-10,8,-6,-2,-8,5,-9,-5,-7,-7,6,-6,-4,-1,9,10,-8,7,-5,-8,-9,6,7,-2,-4,7,6,8,2,3,-3,3,3,7,10,-2,-10,5,-10,4,-6,6,4,-2,-1,-10,-1,-10,-2,10,-2,-10,-1,-2,4,6,6,-1,-8,-7,-1,-5,-9,-5,-2,2,1,8,9,-4,-7,2,-4,4,-8,-1,5,1,3,-6,5,10,-1,8,10,10,4,-1,-5,-10,-5,1,-7,5,-2,-6,8,-3,-4,-9,-4,-4,-9,5,-9,6,-6,-5,1,4,10,10,-5,8,-5,8,6,-8,-6,-10,7,-10,-4,7,-4,1,-2,3,-8,-1,-8,2,10,10,2,4,5,-6,8,8,-6,-5,2,10,-8,2,-9,-9,-4,-6,8,-10,3,-4,9,2,-3,-6,6,6,6,-2,-4,-5,-2,9,-10,-5,-2,3,-2,-9,-3,-9,-10,4,5,-10,-1,-9,5,-4,-6,-7,7,10,-6,-4,3,-7,-8,-8,1,2,-4,-4,9,-5,5,3,-3,-3,3,7,1,-8,6,-4,5,-6,8,-1,6,-4,-9,4,2,-10,-5,9,-8,-4,5,1,5,1,9,-2,8,-7,3,-9,-1,9,4,1,-7,10,5,1,1,3,6,7,1,2,-7,10,10,5,7,9,1,3,-1,7,-8,3,8,-9,4,-5,-4,3,4,9,-2,-3,-6,-10,-3,-10,-7,-9,3,-6,-1,1,5,9,-10,9,7,-6,10,-1,-2,8,-5,4,6,4,10,3,9,-3,2,-10,7,3,1,4,6,3,-10,-7,7,-4,-9,2,-2,-9,-8,3,-7,5,-10,-1,1,-8,-1,5,-10,-4,-7,9,3,4,-6,-7,5,1,10,-4,8,-10,-8,-8,6,-9,10,4,5,5,7,2,-5,-7,-7,-6,4,-3,-2,3,4,-5,-10,-8,-9,4,-6,-7,-1,7,-7,2,-10,-6,-7,2,-10,8,6,-5,-10,10,-7,-8,-3,-8,-8,4,7,-10,-10,8,1,-2,-1,-3,-7,-8,10,-5,-10,3,-5,-6,8,9,-10,10,10,-10,2,-5,-4,5,10,9,5,10,1,-4,-3,9,-9,-7,-2,1,8,-2,8,10,-7,10,1,4,7,10,-1,5,7,-9,9,-2,-8,3,2,-4,10,-1,-3,4,-4,-1,-3,-7,10,-9,7,-8,-6,1,-4,-6,-10,-7,3,2,-6,-4,-9,7,-8,10,8,10,-1,-3,-7,-1,-6,-9,-10,8,-6,-4,3,6,-10,7,-4,-3,10,-10,-4,4,-7,-1,-8,4,-1,-8,-10,4,-1,-7,7,-10,5,-6,10,1,4,6,-10,5,9,-6,10,-10,-10,-5,-6,-6,6,-9,3,-4,1,9,2,-5,-9,-1,-10,7,-5,-10,1,3,-9,4,4,9,9,1,3,-2,6,9,-4,9,-3,2,7,1,-10,10,-4,1,8,-5,-7,-3,-10,-8,-1,6,6,-7,-3,-10,5,9,8,1,2,-9,2,-2,6,-7,-7,-2,10,5,-10,-10,-5,-4,-9,-1,10,-9,-1,7,1,6,-8,10,-10,3,3,6,-2,-3,5,3,-3,10,-5,5,2,3,-2,9,-1,-3,-6,2,-9,-1,8,-10,6,9,8,7,-7,-9,7,-2,-10,1,-6,-6,-10,7,-10,-3,8,8,-5,-5,9,-1,4,3,10,10,10,1,2,8,-7,-8,2,-1,5,1,-4,8,-8,1,-8,-4,-8,6,4,-2,4,6,-8,-5,6,6,-10,5,-9,6,9,4,6,7,-6,1,-1,-8,-5,-3,-10,-1,7,-6,4,4,5,-1,9,-3,7,9,-2,-8,-1,-9,1,-9,8,5,-1,-5,8,-1,2,-6,-9,-6,1,7,-4,-10,6,5,9,6,-10,8,7,-7,-1,-9,-7,1,-10,9,-7,-10,2,-9,-5,1,-7,3,6,4,-2,-10,-7,-8,-1,10,-8,5,4,-9,10,-4,6,-3,-7,10,8,-10,-10,10,5,-1,10,3,1,-3,-1,-8,-4,1,-7,-1,-2,-8,9,-6,-9,7,5,3,1,7,-3,-1,7,6,-5,-7,-10,-1,-6,-3,-8,-4,2,8,-1,7,1,1,-2,-2,-8,5,-7,-6,5,-5,4,5,7,9,-2,4,-4,3,-3,-2,5,8,-4,-4,6,4,-9,5,-6,-3,-1,-4,-3,-3,-4,-7,2,3,-2,9,-6,-7,3,2,6,-8,4,4,-8,4,-1,3,8,3,2,-5,4,5,6,5,-7,-1,-4,8,3,6,-5,-9,-4,1,4,-6,10,4,-1,7,3,-8,-4,-2,10,-3,6,6,-4,-8,2,7,-5,5,-1,3,2,-4,10,3,4,5,-8,2,7,-10,-3,-1,7,6,10,-5,-3,-9,5,-6,-8,10,1,7,3,-9,4,7,-7,1,-4,-2,-3,3,2,8,-8,5,-2,9,10,4,-9,-5,-5,6,1,8,10,6,9,-4,-10,-10,1,-8,9,-5,4,-7,-6,-8,-2,3,-8,-3,-2,-5,6,-7,-5,10,-8,2,-4,-10,-1,-7,5,-4,10,-1,4,7,1,1,-8,10,7,-5,-3,1,-3,9,-2,-4,-8,-7,1,4,-5,-8,5,6,-1,5,7,-10,-8,-10,-1,5,9,4,5,10,3,4,5,2,-2,-2,2,-1,2,-1,6,-2,7,5,-4,-3,-4,-6,8,6,2,-10,3,-5,3,-8,1,7,8,1,6,10,2,8,-2,3,-6,10,-4,-4,10,-9,-4,8,-8,-5,-4,6,-10,7,1,-8,3,-6,-5,-6,-4,8,1,1,7,-6,2,-9,6,-6,6,-4,4,-5,-2,-5,-8,-4,1,8,3,8,-4,10,3,-7,-10,5,2,-4,-1,-1,-4,-7,2,2,1,-3,-7,5,8,6,-6,1,-2,-4,-6,3,-2,4,8,-1,5,4,-6,-9,-4,2,5,9,10,2,8,7,-6,4,-6,10,1,-1,-4,1,5,-5,-7,-10,8,5,5,-6,3,-2,-6,-8,8,-4,-8,-8,10,-5,-8,6,-5,1,-2,-9,-8,-2,5,1,-7,-4,2,10,-5,-9,-8,-10,5,-2,-8], dtype = "uint8")#candidate|1825|(2925,)|const|uint8
call_1824 = relay.TupleGetItem(func_1029_call(relay.reshape(const_1825.astype('uint8'), [15, 13, 15]), relay.reshape(const_1825.astype('uint8'), [15, 13, 15]), ), 2)
call_1826 = relay.TupleGetItem(func_1033_call(relay.reshape(const_1825.astype('uint8'), [15, 13, 15]), relay.reshape(const_1825.astype('uint8'), [15, 13, 15]), ), 2)
output = relay.Tuple([uop_1805,call_1824,const_1825,])
output2 = relay.Tuple([uop_1807,call_1826,const_1825,])
func_1839 = relay.Function([], output)
mod['func_1839'] = func_1839
mod = relay.transform.InferType()(mod)
mutated_mod['func_1839'] = func_1839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1839_call = mutated_mod.get_global_var('func_1839')
call_1840 = func_1839_call()
output = call_1840
func_1841 = relay.Function([], output)
mutated_mod['func_1841'] = func_1841
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1850 = relay.var("var_1850", dtype = "int64", shape = (14, 13, 4))#candidate|1850|(14, 13, 4)|var|int64
var_1851 = relay.var("var_1851", dtype = "int64", shape = (14, 13, 4))#candidate|1851|(14, 13, 4)|var|int64
bop_1852 = relay.less_equal(var_1850.astype('bool'), relay.reshape(var_1851.astype('bool'), relay.shape_of(var_1850))) # shape=(14, 13, 4)
uop_1867 = relay.atan(var_1851.astype('float64')) # shape=(14, 13, 4)
bop_1873 = relay.logical_xor(uop_1867.astype('uint8'), relay.reshape(var_1851.astype('uint8'), relay.shape_of(uop_1867))) # shape=(14, 13, 4)
func_1742_call = mod.get_global_var('func_1742')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_1877 = relay.TupleGetItem(func_1742_call(), 3)
call_1878 = relay.TupleGetItem(func_1744_call(), 3)
func_997_call = mod.get_global_var('func_997')
func_1000_call = mutated_mod.get_global_var('func_1000')
var_1888 = relay.var("var_1888", dtype = "float64", shape = ())#candidate|1888|()|var|float64
var_1889 = relay.var("var_1889", dtype = "float32", shape = (252, 1))#candidate|1889|(252, 1)|var|float32
call_1887 = relay.TupleGetItem(func_997_call(relay.reshape(var_1888.astype('float64'), []), relay.reshape(var_1889.astype('float32'), [252, 1]), ), 3)
call_1890 = relay.TupleGetItem(func_1000_call(relay.reshape(var_1888.astype('float64'), []), relay.reshape(var_1889.astype('float32'), [252, 1]), ), 3)
bop_1892 = relay.divide(bop_1873.astype('float64'), relay.reshape(var_1851.astype('float64'), relay.shape_of(bop_1873))) # shape=(14, 13, 4)
var_1897 = relay.var("var_1897", dtype = "float64", shape = (14, 13, 4))#candidate|1897|(14, 13, 4)|var|float64
bop_1898 = relay.power(bop_1892.astype('float64'), relay.reshape(var_1897.astype('float64'), relay.shape_of(bop_1892))) # shape=(14, 13, 4)
func_354_call = mod.get_global_var('func_354')
func_358_call = mutated_mod.get_global_var('func_358')
var_1903 = relay.var("var_1903", dtype = "int64", shape = (1183,))#candidate|1903|(1183,)|var|int64
var_1904 = relay.var("var_1904", dtype = "uint16", shape = (280,))#candidate|1904|(280,)|var|uint16
call_1902 = relay.TupleGetItem(func_354_call(relay.reshape(var_1888.astype('int64'), []), relay.reshape(var_1903.astype('int64'), [7, 13, 13]), relay.reshape(var_1904.astype('uint16'), [280,]), ), 0)
call_1905 = relay.TupleGetItem(func_358_call(relay.reshape(var_1888.astype('int64'), []), relay.reshape(var_1903.astype('int64'), [7, 13, 13]), relay.reshape(var_1904.astype('uint16'), [280,]), ), 0)
var_1910 = relay.var("var_1910", dtype = "float64", shape = (14, 13, 4))#candidate|1910|(14, 13, 4)|var|float64
bop_1911 = relay.minimum(uop_1867.astype('int32'), relay.reshape(var_1910.astype('int32'), relay.shape_of(uop_1867))) # shape=(14, 13, 4)
bop_1916 = relay.bitwise_or(bop_1898.astype('uint32'), relay.reshape(uop_1867.astype('uint32'), relay.shape_of(bop_1898))) # shape=(14, 13, 4)
bop_1919 = relay.bitwise_xor(bop_1898.astype('int64'), relay.reshape(var_1910.astype('int64'), relay.shape_of(bop_1898))) # shape=(14, 13, 4)
func_1292_call = mod.get_global_var('func_1292')
func_1296_call = mutated_mod.get_global_var('func_1296')
var_1933 = relay.var("var_1933", dtype = "float64", shape = (36,))#candidate|1933|(36,)|var|float64
var_1934 = relay.var("var_1934", dtype = "uint8", shape = (2925,))#candidate|1934|(2925,)|var|uint8
call_1932 = relay.TupleGetItem(func_1292_call(relay.reshape(var_1933.astype('float64'), [3, 12, 1]), relay.reshape(var_1904.astype('uint16'), [280,]), relay.reshape(var_1934.astype('uint8'), [2925,]), ), 4)
call_1935 = relay.TupleGetItem(func_1296_call(relay.reshape(var_1933.astype('float64'), [3, 12, 1]), relay.reshape(var_1904.astype('uint16'), [280,]), relay.reshape(var_1934.astype('uint8'), [2925,]), ), 4)
output = relay.Tuple([bop_1852,call_1877,call_1887,var_1888,var_1889,call_1902,var_1903,var_1904,bop_1911,bop_1916,bop_1919,call_1932,var_1933,var_1934,])
output2 = relay.Tuple([bop_1852,call_1878,call_1890,var_1888,var_1889,call_1905,var_1903,var_1904,bop_1911,bop_1916,bop_1919,call_1935,var_1933,var_1934,])
func_1936 = relay.Function([var_1850,var_1851,var_1888,var_1889,var_1897,var_1903,var_1904,var_1910,var_1933,var_1934,], output)
mod['func_1936'] = func_1936
mod = relay.transform.InferType()(mod)
mutated_mod['func_1936'] = func_1936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1936_call = mutated_mod.get_global_var('func_1936')
var_1938 = relay.var("var_1938", dtype = "int64", shape = (14, 13, 4))#candidate|1938|(14, 13, 4)|var|int64
var_1939 = relay.var("var_1939", dtype = "int64", shape = (14, 13, 4))#candidate|1939|(14, 13, 4)|var|int64
var_1940 = relay.var("var_1940", dtype = "float64", shape = ())#candidate|1940|()|var|float64
var_1941 = relay.var("var_1941", dtype = "float32", shape = (252, 1))#candidate|1941|(252, 1)|var|float32
var_1942 = relay.var("var_1942", dtype = "float64", shape = (14, 13, 4))#candidate|1942|(14, 13, 4)|var|float64
var_1943 = relay.var("var_1943", dtype = "int64", shape = (1183,))#candidate|1943|(1183,)|var|int64
var_1944 = relay.var("var_1944", dtype = "uint16", shape = (280,))#candidate|1944|(280,)|var|uint16
var_1945 = relay.var("var_1945", dtype = "float64", shape = (14, 13, 4))#candidate|1945|(14, 13, 4)|var|float64
var_1946 = relay.var("var_1946", dtype = "float64", shape = (36,))#candidate|1946|(36,)|var|float64
var_1947 = relay.var("var_1947", dtype = "uint8", shape = (2925,))#candidate|1947|(2925,)|var|uint8
call_1937 = func_1936_call(var_1938,var_1939,var_1940,var_1941,var_1942,var_1943,var_1944,var_1945,var_1946,var_1947,)
output = call_1937
func_1948 = relay.Function([var_1938,var_1939,var_1940,var_1941,var_1942,var_1943,var_1944,var_1945,var_1946,var_1947,], output)
mutated_mod['func_1948'] = func_1948
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1980 = relay.var("var_1980", dtype = "float64", shape = (2, 5, 8))#candidate|1980|(2, 5, 8)|var|float64
uop_1981 = relay.asinh(var_1980.astype('float64')) # shape=(2, 5, 8)
output = relay.Tuple([uop_1981,])
output2 = relay.Tuple([uop_1981,])
func_1992 = relay.Function([var_1980,], output)
mod['func_1992'] = func_1992
mod = relay.transform.InferType()(mod)
mutated_mod['func_1992'] = func_1992
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1993 = relay.var("var_1993", dtype = "float64", shape = (2, 5, 8))#candidate|1993|(2, 5, 8)|var|float64
func_1992_call = mutated_mod.get_global_var('func_1992')
call_1994 = func_1992_call(var_1993)
output = call_1994
func_1995 = relay.Function([var_1993], output)
mutated_mod['func_1995'] = func_1995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_2022 = relay.TupleGetItem(func_1632_call(), 0)
call_2023 = relay.TupleGetItem(func_1633_call(), 0)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_2024 = relay.TupleGetItem(func_1839_call(), 0)
call_2025 = relay.TupleGetItem(func_1841_call(), 0)
output = relay.Tuple([call_2022,call_2024,])
output2 = relay.Tuple([call_2023,call_2025,])
func_2027 = relay.Function([], output)
mod['func_2027'] = func_2027
mod = relay.transform.InferType()(mod)
mutated_mod['func_2027'] = func_2027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mutated_mod.get_global_var('func_2027')
call_2028 = func_2027_call()
output = call_2028
func_2029 = relay.Function([], output)
mutated_mod['func_2029'] = func_2029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_2070 = relay.TupleGetItem(func_1839_call(), 2)
call_2071 = relay.TupleGetItem(func_1841_call(), 2)
uop_2072 = relay.erf(call_2070.astype('float64')) # shape=(2925,)
uop_2074 = relay.erf(call_2071.astype('float64')) # shape=(2925,)
func_460_call = mod.get_global_var('func_460')
func_463_call = mutated_mod.get_global_var('func_463')
var_2080 = relay.var("var_2080", dtype = "float64", shape = (220,))#candidate|2080|(220,)|var|float64
var_2081 = relay.var("var_2081", dtype = "uint16", shape = (10, 28))#candidate|2081|(10, 28)|var|uint16
call_2079 = relay.TupleGetItem(func_460_call(relay.reshape(var_2080.astype('float64'), [11, 5, 4]), relay.reshape(var_2081.astype('uint16'), [280,]), ), 0)
call_2082 = relay.TupleGetItem(func_463_call(relay.reshape(var_2080.astype('float64'), [11, 5, 4]), relay.reshape(var_2081.astype('uint16'), [280,]), ), 0)
func_997_call = mod.get_global_var('func_997')
func_1000_call = mutated_mod.get_global_var('func_1000')
var_2090 = relay.var("var_2090", dtype = "float64", shape = ())#candidate|2090|()|var|float64
var_2091 = relay.var("var_2091", dtype = "float32", shape = (252,))#candidate|2091|(252,)|var|float32
call_2089 = relay.TupleGetItem(func_997_call(relay.reshape(var_2090.astype('float64'), []), relay.reshape(var_2091.astype('float32'), [252, 1]), ), 2)
call_2092 = relay.TupleGetItem(func_1000_call(relay.reshape(var_2090.astype('float64'), []), relay.reshape(var_2091.astype('float32'), [252, 1]), ), 2)
uop_2102 = relay.exp(uop_2072.astype('float32')) # shape=(2925,)
uop_2104 = relay.exp(uop_2074.astype('float32')) # shape=(2925,)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_2107 = relay.TupleGetItem(func_1839_call(), 1)
call_2108 = relay.TupleGetItem(func_1841_call(), 1)
func_1409_call = mod.get_global_var('func_1409')
func_1413_call = mutated_mod.get_global_var('func_1413')
const_2110 = relay.const([9,-8,-8,5,10,-1,-7,3,-2,7,1,1,6,5,-5,1,-10,2,-3,-4,-2,5,10,3,3,7,3,9,3,3,6,4,4,-6,5,-10,-2,6,-5,3,9,3,2,-3,5,5,-9,-7,-6,-10,2,-10,4,-8,7,8,-5,-7,-2,10,-8,9,5,-2,1,-4,3,9,9,10,-1,9,-9,3,-1,-1,9,8,-9,4,6,5,1,-9,-1,6,7,-10,-4,-10,-5,5,10,-9,-8,9,3,3,7,-4,-3,2,6,6,6,-6,-6,6,-6,5,10,-6,-9,6,-5,6,-1,-5,2,-6,7,9,4,-9,10,2,1,2,-1,6,9,1,2,-4,9,-3,5,-10,-9,7,5,1,1,6,2,-7,5,10,4,-2,-7,9,-8,10,8,-9,1,8,3,-4,-5,-9,-9,-8,6,-7,-8,4,-5,-5,4,-7,4,-4,9,-6,-9,7,-4,2,-8,3,-7,-1,-1,-7,-10,9,2,-3,-1,7,1,-1,-10,7,4,-3,-6,5,-3,-4,9,-9,7,3,-10,-10,-8,-8,-4,8,4,10,10,-9,8,-7,5,1,7,-9,-6,-8,10], dtype = "int32")#candidate|2110|(225,)|const|int32
const_2111 = relay.const([-10,3,-4,3,-8,6,4,-6,-9,-2,-1,-3,-2,3,10,9,7,-3,-4,-5,-9,-2,-4,5,-5,10,-9,-5,8,6,-4,-8,-4,-3,9,5,-9,-4,-3,-4,5,-6,-1,-7,9,-6,6,-5,7,3,6,-6,2,7,9,6,9,10,5,6,-1,-8,-6,-9,2,1,-9,4,6,-1,-5,1,-10,-4,6,-8,4,-6,-8,-5,9,8,-2,-1,6,-5,10,-6,5,-5,2,10,9,8,10,-10,9,7,10,4,-2,8,-5,2,4,4,3,4,9,3,-5,-8,-1,-8,3,-9,-10,-6,-1,6,-8,-3,-4,6,7,5,-2,-8,6,-4,-5,3,-7,-10,-9,-4,-9,-1,4,-8,-7,-4,-6,2,6,2,-6,-7,-5,-3,-7,3,-4,1,-2,-8,4,9,-4,-3,-6,4,-9,7,1,-10,7,-2,-6,8,4,6,-1,5,6,8,2,-4,-4,-8,-10,-1,10,7,-8,5,-4,7,7,-1,-1,-5,-10,5,9,-6,10,6,-3,-7,10,1,4,-1,10,-4,-2,6,-5,7,4,2,3,5,1,-4,-5,-8,3,-10,3,7,-10,-7,-2,10,10,-2,-10,-8,1,3,-9,7,-10,8,-2,9,6,8,10,5,-9,-2,4,-1,2,-2,-5,-4,7,-10,-4,10,3,-9,-7,-5,-1,-7,-7,-1,2,-1,-4,4,8,10,-3,2,-10,10,-5,-6,-4,-3,-1,3,8,2,10,5,2,-9,-8,10,2,-7,-7,-5,-8,-3,3,-4,-9,-4,4,6,-5,-10,6,2,2,-8,4,1,2,-3,-1,5,-5,8,8,-7,10,5,9,-5,7,-1,5,-3,7,1,2,7,-4,-7,10,-7,-1,-6,10,-3,-5,9,8,8,-9,5,-6,9,9,4,9,-2,4,3,1,4,-2,-7,-7,6,-5,-5,3,-3,-9,-4,8,9,3,-7,-7,10,4,-10,6,4,8,2,-3,-4,2,1,3,2,-1,10,-10,9,-2,2,6,-9,7,-8,8,5,1,10,5,9,10,5,-2,1,-5,1,-3,10,4,10,-9,2,10,-3,3,-2,3,-1,4,-10,9,4,4,9,1,9,-6,-1,10,-3,6,-6,-3,-6,10,-9,9,-10,5,-10,1,-6,8,-3,-1,-3,-2,-8,7,3,9,-6,-5,-9,6,-9,-9,-3,-2,9,-3,-2,3,-1,1,-6,7,-7,10,3,7,2,6,-3,2,-4,4,1,4,-8,5,5,7,4,-10,-1,8,-3,1,-5,-9,9,2,3,-1,3,4,-7,10,8,10,-8,-5,3,8,8,-6,3,6,-6,-4,2,-4,10,-2,-7,8,-1,6,-8,3,-4,-4,6,10,6,10,-3,-6,-10,9,-1,3,-1,-5,5,-6,6,5,-9,-4,10,-4,-8,-6,-1,8,-6,-1,1,-6,5,-7,-4,-2,9,10,2,2,4,-10,5,-4,-10,7,-4,-2,-7,-7,3,-5,-7,-2,9,-1,-2,-8,1,-9,9,-4,1,2,-5,8,-8,10,8,-6,-4,9,-2,-6,-7,5,10,-10,5,8,1,-8,9,-6,-8,3,3,-1,-7,7,-1,-1,-2,-4,3,7,-8,-4,-10,3,5,3,7,3,8,-7,2,2,1,1,5,-9,-2,1,3,2,-1,-8,-9,-10,2,-6,5,8,-1,1,8,3,5,2,8,-8,10,-5,8,6,5,4,-1,8,-3,1,1,1,-6,3,-8,-4,8,9,-7,8,10,-1,-4,4,10,-1,7,-8,-5,-8,-4,5,-4,-10,1,2,-7,2,-6,1,10,-8,3,2,6,3,4,2,2,8,9,7,-5,-9,7,-6,1,-6,9,-2,-9,3,-5,-9,6,-2,-9,10,2,-6,1,-6,5,9,-1,9,8,-1,-8,9,10,-8,4,5,-9,-5,-3,5,6,-4,-6,6,6,8,10,7,-3,-10,-6,5,4,-8,-2,6,8,4,4,2,7,-3,9,8,-8,-9,1,-2,3,-3,4,6,1,7,-9,-5,-1,5,2,-10,-2,-7,-4,-10,-8,5,-4,5,10,-1,3,7,-8,-3,-8,3,3,-2,8,5,5,-9,8,4,-7,7,5,-5,-8,5,1,-7,7,-1,-1,4,-6,-5,-8,10,-6,-7,-1,-3,-9,7,6,4,3,-2,-4,10,-9,4,-6,3,3,2,-10,-5,5,9,-5,-7,-2,3,-3,-8,8,10,-8,5,-2,-5,5,-1,1,-4,-5,-7,9,-5,-2,7,-4,-5,9,-4,-10,3,-7,6,6,-6,-10,-10,-4,-1,7,-8,4,-3,-5,6,-6,-1,-3,2,-8,2,5,4,4,-6,3,2,-9,-2,4,4,-7,4,3,-1,6,8,3,9,-9,-10,10,10,9,-8,2,-2,6,-10,1,9,-5,1,8,7,6,10,9,7,-3,-10,6,3,9,-10,-3,10,-7,7,-10,3,-10,-3,-2,-7,-7,10,-3,7,6,-4,8,8,6,1,8,3,-4,8,-9,2,6,-9,-7,-10,-4,2,10,-9,5,-6,1,-4,-8,-4,-9,-2,10,-3,8,8,10,7,-1,-10,-4,9,6,4,-6,-10,5,-2,-3,-10,10,6,9,2,10,6,6,1,1,-3,-4,-3,-5,3,-2,3,-4,-10,2,5,-1,6,-8,-9,-4,7,-7,8,7,-2,-8,-9,-3,7,2,-7,-3,-2,2,10,-6,-6,9,-5,-7,5,3,8,-4,3,-5,9,-5,-8,4,5,-7,1,6,2,6,-7,-1,6,7,3,2,-1,5,-4,-1,7,9,-4,7,-8,-5,-3,-1,-4,-10,2,1,7,-5,4,-1,6,2,-4,-7,-3,9,-1,-7,-9,-3,7,6,-9,8,-9,-8,-8,4,-9,-4,3,8,-4,-8,10,-3,5,-4,2,-2,8,3,-8,7,6,-10,7,-3,-1,-3,4,9,-7,8,4,8,9,7,8,7,-7,5,2,-2,-2,-5,1,8,8,5,7,3,7,-5,6,-1,6,-5,-7,-1,-4,-5,-10,-2,10,-10,5,3,7,-6,-10,6,-4,-4,9,-8,-4,9,8,4,-1,5,10,-7,-7,-10,2,3,-6,-7,-6,10,-9,-4,2,-5,2,10,-1,1,-2,7,4,1,8,-8,4,4,9,-2,-8,6,10,-4,-5,-9,5,-2,-7,-2,3,-1,10,-2,-5,-1,-5,5,-5,6,-5,8,10,-8,4,-2,-9,-6,8,7,-6,6,-7,5,-9,1,-8,3,-8,-5,-10,1,-1,10,7,-3,-6,-4,-2,-5,2,7,5,-5,1,-7,-8,4,-7,1,2,7,-4,2,-10,9,3,9,5,10,6,9,-8,-7,7,-9,1,6,-4,3,5,5,7,-5,10,8,-5,-1,-2,-5,6,8,9,5,4,9,-10,-5,-8,9,8,-3,-6,5,5,-9,-6,-8,-2,-8,3,-6,-2,9,-3,-6,-6,3,5,10,-8,9,-7,-6,-4,-7,-4,9,6,-3,-6,2,-8,-4,3,-3,4,-2,10,1,-6,10,-1,-3,-7,-10,5,-5,-6,-8,-4,7,-4,8,-1,-10,7,-5,9,7,-6,8,-8,-8,1,-1,-8,2,9,8,9,7,9,6,1,3,2,-1,-4,5,5,-10,-4,5,-4,-5,2,-9,-5,-9,10,-4,-1,5,1,1,-5,9,5,5,8,10,-2,-10,-8,5,-1,2,-3,-9,6,2,-3,1,6,5,7,-3,8,8,-2,-4,2,-5,5,-1,4,-2,-8,-4,8,8,7,-6,3,-1,-7,-8,-2,-3,-6,8,2,8,-3,-2,-10,-8,-2,-1,8,-1,-6,-1,-1,7,-3,-1,5,2,-10,10,-7,-8,-3,-5,1,-4,-5,7,-3,5,-9,10,-6,3,9,7,-2,-4,-3,3,-4,-1,6,-7,2,5,-10,7,-7,3,2,3,-4,8,-7,3,10,2,-4,6,-3,-9,-8,-1,5,-3,2,2,5,5,-2,7,4,9,10,-4,-8,8,-9,3,2,2,3,2,-5,4,-5,9,-10,-7,-4,3,-4,-8,-9,7,-8,-5,-5,1,-4,-7,-5,10,7,-6,-10,2,10,-9,2,8,6,-3,10,3,10,-5,-8,-2,4,-7,9,-10,-1,7,6,-7,1,-3,5,-7,8,2,8,-3,4,-9,-9], dtype = "int32")#candidate|2111|(1575,)|const|int32
call_2109 = func_1409_call(relay.reshape(const_2110.astype('int32'), [1, 15, 15]), relay.reshape(const_2111.astype('int32'), [7, 15, 15]), )
call_2112 = func_1409_call(relay.reshape(const_2110.astype('int32'), [1, 15, 15]), relay.reshape(const_2111.astype('int32'), [7, 15, 15]), )
func_60_call = mod.get_global_var('func_60')
func_62_call = mutated_mod.get_global_var('func_62')
call_2114 = func_60_call(relay.reshape(var_2081.astype('uint16'), [10, 7, 4]))
call_2115 = func_60_call(relay.reshape(var_2081.astype('uint16'), [10, 7, 4]))
bop_2120 = relay.logical_and(uop_2102.astype('bool'), var_2090.astype('bool')) # shape=(2925,)
bop_2123 = relay.logical_and(uop_2104.astype('bool'), var_2090.astype('bool')) # shape=(2925,)
output = relay.Tuple([call_2079,var_2080,var_2081,call_2089,var_2091,call_2107,call_2109,const_2110,const_2111,call_2114,bop_2120,])
output2 = relay.Tuple([call_2082,var_2080,var_2081,call_2092,var_2091,call_2108,call_2112,const_2110,const_2111,call_2115,bop_2123,])
func_2128 = relay.Function([var_2080,var_2081,var_2090,var_2091,], output)
mod['func_2128'] = func_2128
mod = relay.transform.InferType()(mod)
var_2129 = relay.var("var_2129", dtype = "float64", shape = (220,))#candidate|2129|(220,)|var|float64
var_2130 = relay.var("var_2130", dtype = "uint16", shape = (10, 28))#candidate|2130|(10, 28)|var|uint16
var_2131 = relay.var("var_2131", dtype = "float64", shape = ())#candidate|2131|()|var|float64
var_2132 = relay.var("var_2132", dtype = "float32", shape = (252,))#candidate|2132|(252,)|var|float32
output = func_2128(var_2129,var_2130,var_2131,var_2132,)
func_2133 = relay.Function([var_2129,var_2130,var_2131,var_2132,], output)
mutated_mod['func_2133'] = func_2133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_2145 = relay.TupleGetItem(func_2027_call(), 1)
call_2146 = relay.TupleGetItem(func_2029_call(), 1)
func_460_call = mod.get_global_var('func_460')
func_463_call = mutated_mod.get_global_var('func_463')
const_2158 = relay.const([[9.620709,-5.566401,-9.933414,3.870723,-7.896698,7.446854,2.344105,-6.092105,6.804812,7.774698,7.167326,-8.473811,-5.144087,-5.519915,5.168070,-5.822272,-3.228980,-5.351387,0.360029,-9.087309,-4.785264,9.813316,-9.398481,-0.139093,-2.446988,-3.630162,4.878974,4.479106,4.129319,-4.608657,-6.282518,6.005418,3.423018,1.606409,3.713887,6.360175,1.737404,0.203152,-8.067383,-4.384248,-9.377225,-4.090309,7.937568,5.938699,8.980599,1.760879,-3.854712,-4.097442,2.778968,-3.451128,-7.982426,-9.511201,-6.149889,5.182606,6.905914,1.412631,0.690355,9.835398,3.196250,9.141251,6.481379,-6.614462,8.466117,0.689254,2.937684,2.149138,3.355338,5.851020,-7.680182,6.029819,-7.433366,9.368634,-9.499275,-5.938190,9.674274,2.785991,8.556647,-6.081456,-3.566817,6.692453,9.209268,9.501270,-7.976155,-5.561299,-7.968340,-8.377840,-2.054277,-1.338156,-6.849186,-4.185295,-3.999238,-6.746038,6.552656,-3.597811,1.632162,7.431648,-4.926436,1.968299,-9.446442,1.360139,9.674680,7.543879,2.503783,2.437953,1.183249,5.816786,6.204917,9.871409,-5.174233,-3.339843,7.307871,-5.327308,2.116051,-5.026058,6.751420,-0.065150,6.248884,-1.912976,5.908749,-2.557143,3.970167,-3.363787,-5.844182,-1.651171,8.437627,-7.278601,-5.074135,-9.568112,-3.474752,4.637088,7.812685,8.832020,-7.894817,4.315901,7.780608,-0.236605,-4.164700,9.639840,-2.833821,3.260946,-6.855515,-8.113160,2.691865,-9.844952,0.879849,7.238311,6.230173,6.422696,9.482610,7.569925,-7.494607,2.920825,-3.959588,7.280522,-6.337345,-7.347846,-4.649188,-7.360064,-2.600671,-0.476759,-9.258180,-6.937867,-9.332649,9.583504,-3.418919,-1.424835,-7.632281,7.049664,-9.219508,6.588721,-4.394310,2.952896,-1.811966,-8.523916,4.763906,-1.846427,-9.391753,7.361337,-6.217630,-1.367763,-1.014298,-2.885763,7.681843,3.181945,-7.773989,-9.067753,7.714344,-5.025527,7.725258,-8.206222,0.230269,6.939697,8.215085,-4.513992,2.150844,-4.146175,0.611044,3.705697,1.432579,-8.205647,1.559803,-1.857618,-4.399761,5.675536,5.076058,-5.535536,-9.968877,-7.389438,3.961823,-0.587200,-1.702749,-1.648140,5.571386,-2.811766,-5.641549,-9.817207,6.650685,-2.952472,9.108967,-0.679835]], dtype = "float64")#candidate|2158|(1, 220)|const|float64
const_2159 = relay.const([6,-8,-3,10,5,4,-5,-4,-7,-3,7,9,-3,6,9,-6,5,5,5,5,-7,3,7,-10,2,1,-5,9,-7,8,6,2,-5,1,-2,-2,-7,-2,-2,-9,8,-6,-4,-9,-1,8,10,-1,7,-7,-10,8,5,2,-2,4,4,-1,8,-9,8,6,-7,2,-9,-1,-9,-6,10,-4,2,-2,-1,-5,6,7,1,-9,10,-10,-10,10,1,4,6,4,7,2,-3,-6,-1,1,4,-10,-1,3,-3,-1,-9,-6,4,-2,-9,8,3,1,4,-8,3,-5,8,8,-1,8,5,-6,5,1,-4,6,-2,1,-8,-6,-7,-5,-9,8,3,1,-7,8,-4,-8,7,-6,-10,7,-6,-8,2,-7,8,10,-9,-9,7,-2,6,9,-5,-4,-2,4,-2,10,-10,6,4,7,-8,-2,6,7,-6,-5,3,-6,8,4,4,7,-3,-2,-8,2,7,-2,10,5,10,-6,9,2,2,1,-2,-2,9,3,2,5,9,-4,-1,-6,-9,5,-4,9,-5,-4,7,1,9,-5,-9,-4,-10,-9,7,3,6,6,-7,8,5,6,-9,8,-10,2,-3,-6,-3,5,10,8,6,-8,10,4,9,7,-6,9,-8,-5,-5,6,-8,10,9,-8,3,-1,-3,8,6,1,8,9,-10,9,-5,-5,-7,3,-4,-4,-6,-10,9,-2,-1,6,2,7,10,-7,-2,8,-9,9,1,-8,10,5,-4,-6], dtype = "uint16")#candidate|2159|(280,)|const|uint16
call_2157 = relay.TupleGetItem(func_460_call(relay.reshape(const_2158.astype('float64'), [11, 5, 4]), relay.reshape(const_2159.astype('uint16'), [280,]), ), 1)
call_2160 = relay.TupleGetItem(func_463_call(relay.reshape(const_2158.astype('float64'), [11, 5, 4]), relay.reshape(const_2159.astype('uint16'), [280,]), ), 1)
func_354_call = mod.get_global_var('func_354')
func_358_call = mutated_mod.get_global_var('func_358')
var_2165 = relay.var("var_2165", dtype = "int64", shape = ())#candidate|2165|()|var|int64
const_2166 = relay.const([[-9,9,2,1,-10,-3,-9,-1,10,8,-7,-1,4,-5,7,-1,-6,6,-4,-6,-3,-3,-5,1,10,-3,2,7,9,4,3,-4,6,9,-6,8,3,2,-8,3,10,2,-1,8,2,8,7,-6,-2,5,-9,7,-4,10,-10,9,-3,2,1,4,1,-1,-3,-1,4,-1,1,-5,-7,-9,9,6,9,6,9,-5,3,9,5,-9,8,-1,9,3,2,4,-8,-3,-10,8,2],[-10,-3,1,8,8,1,4,5,8,9,-9,2,-5,3,-2,9,10,-2,10,10,-8,7,-2,1,-8,-10,9,-8,-4,10,-8,1,-10,8,5,-8,-10,6,5,-10,8,-1,1,1,-4,3,-7,9,-9,7,-6,8,-2,-6,2,2,-5,4,4,-3,-6,10,3,3,6,-6,7,-6,8,5,-7,9,2,2,-1,-6,-3,2,-6,8,5,4,-7,10,-4,7,-4,7,-4,-5,4],[-3,8,5,-8,-3,6,-4,10,2,1,-5,-8,2,-1,-8,-8,2,-4,-7,-9,-5,10,1,5,3,-3,-10,1,4,9,-7,-10,-3,5,9,2,10,-5,-1,-4,-4,-5,7,-6,-9,10,-2,-6,-7,6,-6,1,-10,7,-7,-6,-8,-5,8,-8,6,3,-10,-4,-10,4,9,-4,-2,-10,1,-9,-8,8,6,3,3,2,4,4,-8,-2,4,6,6,-4,-2,10,5,-6,-1],[5,-4,1,4,-2,4,1,-9,-5,-1,-3,-9,-2,8,-7,6,7,10,-6,3,-1,3,6,-7,8,-9,-10,4,7,10,5,8,6,9,-6,-1,1,7,5,-10,1,-5,-2,-2,3,4,10,7,2,7,8,5,1,9,-5,10,-10,6,4,-2,-2,4,-8,9,8,-10,-3,8,-6,-1,-7,6,5,-1,1,-7,-8,6,-3,8,2,-2,4,10,-8,-4,1,-4,1,7,-9],[-5,-7,-4,8,4,3,-7,-7,-8,10,-1,1,9,-1,6,-1,8,3,-8,4,-3,9,4,8,4,4,-9,3,9,-4,-5,-7,3,-2,3,5,5,-7,-2,2,1,1,3,7,7,8,-6,-4,-4,-2,-4,-6,-2,9,8,-2,-9,10,-7,7,-8,-8,9,7,-8,-4,-7,3,-3,-5,-6,-9,-10,-1,8,2,3,4,2,7,10,4,10,-7,2,4,-7,-6,-6,3,-5],[9,3,-9,-5,-6,-8,2,-8,2,9,9,-1,-2,-2,-10,-9,4,-2,-8,-7,-4,5,-2,-3,4,-10,-9,-9,-7,-5,5,-8,6,2,-9,-8,-6,6,-5,-4,-2,-3,-7,-1,1,-3,-10,7,-1,1,10,2,2,3,9,-8,2,-2,-4,-3,-1,-5,-7,8,-1,-7,-10,-6,5,2,9,-6,1,-9,-3,2,-1,6,9,-6,-4,-3,10,-7,-3,2,6,2,-6,-4,7],[4,3,8,5,-2,8,3,7,6,6,-1,-4,2,5,-10,4,-2,3,6,-7,8,4,-3,1,8,-7,-2,1,10,1,-10,-3,9,6,5,4,9,5,8,3,-3,-4,-1,10,2,-3,-6,9,-4,3,-6,-5,4,9,7,-7,-2,7,9,-5,9,-5,6,-2,-7,-4,-1,-10,-10,-8,-2,-9,-7,6,-2,-9,10,-7,8,-9,-6,1,-1,-6,-1,7,-9,-8,3,-6,-6],[7,9,-4,-7,3,3,3,-7,4,3,-3,-10,-3,-4,9,4,-8,3,-1,3,4,-9,10,7,-6,-7,-7,10,1,8,4,7,-4,-3,1,-8,4,5,3,-9,-4,-8,5,-10,-1,-8,10,-8,8,-1,9,-5,7,6,1,1,-4,-6,-6,-7,5,-2,3,-9,-1,-9,2,-1,3,10,-5,-9,9,-7,-2,-2,10,-9,-3,-1,1,-3,3,3,-5,1,-4,-8,6,10,10],[4,-5,10,-3,2,-2,-8,-3,2,-2,8,3,-2,1,-8,5,10,5,8,10,4,7,6,1,-7,-1,2,3,7,-6,-7,-7,1,-7,-9,-10,-9,-5,6,5,10,8,-1,3,-7,3,10,-10,-3,9,-4,-7,6,9,7,-5,9,-6,-6,-10,-8,8,-4,-8,-7,-1,5,-5,-7,3,10,8,1,4,2,2,-9,-7,-1,10,-3,-9,8,-1,10,-10,2,-2,3,-2,-9],[7,5,1,-9,1,3,-2,8,9,-7,-10,8,-4,9,-7,10,-6,-8,-10,7,10,-5,-4,-4,-1,-1,-2,5,1,-3,10,-2,10,-3,-6,-4,-2,-9,-2,-7,-5,-3,9,-4,10,9,-1,-8,3,-1,-2,7,6,8,8,10,-6,-4,-1,-7,6,-2,-9,9,-2,2,5,-7,5,8,3,-9,-1,5,-1,-2,8,-5,-4,10,-5,9,-10,-3,-2,-8,-7,5,2,-9,-2],[-2,-4,-7,1,6,10,6,-2,4,-9,8,-1,-5,2,-8,4,-5,6,1,-1,-3,-4,10,-9,-9,-9,6,9,7,-5,4,-2,10,-2,5,-9,4,-7,-9,-1,7,-3,-3,4,4,2,9,-8,2,-3,5,3,-5,-4,-9,3,6,-8,-10,7,-2,-3,-3,-1,3,1,-5,-7,-7,7,7,-3,-5,2,-3,-1,-9,5,5,8,9,-6,-4,-7,4,-6,-3,4,9,-5,-6],[-7,-1,9,-10,6,6,6,-6,10,6,-1,-4,8,2,6,-10,-4,-7,10,10,9,-9,6,9,-5,2,5,-4,9,-6,3,10,-8,-10,6,-4,8,1,1,9,-4,-6,9,2,4,-3,-6,4,-1,2,-4,4,2,-7,-5,10,9,10,4,6,-2,8,-3,9,9,-5,8,5,3,4,8,7,8,5,-1,-3,-9,10,3,10,-1,-5,2,-2,3,5,7,-1,1,-10,-9],[5,2,-2,5,5,4,-8,1,3,5,5,2,-1,-4,-7,-2,2,10,-8,-7,2,4,-10,-3,9,1,-1,2,7,-3,-10,7,-8,8,-1,-3,-4,6,-4,-7,6,-8,2,-9,7,-3,6,9,-4,-1,9,9,-1,-9,3,-7,-5,-6,-7,8,-8,1,9,-7,8,-10,-2,-2,6,-7,1,-8,10,-5,-2,1,2,-1,3,-5,-7,-7,6,1,5,10,1,2,3,-10,-10]], dtype = "int64")#candidate|2166|(13, 91)|const|int64
call_2164 = relay.TupleGetItem(func_354_call(relay.reshape(var_2165.astype('int64'), []), relay.reshape(const_2166.astype('int64'), [7, 13, 13]), relay.reshape(call_2157.astype('uint16'), [280,]), ), 2)
call_2167 = relay.TupleGetItem(func_358_call(relay.reshape(var_2165.astype('int64'), []), relay.reshape(const_2166.astype('int64'), [7, 13, 13]), relay.reshape(call_2157.astype('uint16'), [280,]), ), 2)
output = relay.Tuple([call_2145,call_2157,const_2158,const_2159,call_2164,var_2165,const_2166,])
output2 = relay.Tuple([call_2146,call_2160,const_2158,const_2159,call_2167,var_2165,const_2166,])
func_2187 = relay.Function([var_2165,], output)
mod['func_2187'] = func_2187
mod = relay.transform.InferType()(mod)
mutated_mod['func_2187'] = func_2187
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2188 = relay.var("var_2188", dtype = "int64", shape = ())#candidate|2188|()|var|int64
func_2187_call = mutated_mod.get_global_var('func_2187')
call_2189 = func_2187_call(var_2188)
output = call_2189
func_2190 = relay.Function([var_2188], output)
mutated_mod['func_2190'] = func_2190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1742_call = mod.get_global_var('func_1742')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_2211 = relay.TupleGetItem(func_1742_call(), 0)
call_2212 = relay.TupleGetItem(func_1744_call(), 0)
uop_2217 = relay.rsqrt(call_2211.astype('float64')) # shape=(11, 4, 7)
uop_2219 = relay.rsqrt(call_2212.astype('float64')) # shape=(11, 4, 7)
func_1168_call = mod.get_global_var('func_1168')
func_1176_call = mutated_mod.get_global_var('func_1176')
const_2227 = relay.const(-4.340442, dtype = "float64")#candidate|2227|()|const|float64
var_2228 = relay.var("var_2228", dtype = "float64", shape = (2304,))#candidate|2228|(2304,)|var|float64
var_2229 = relay.var("var_2229", dtype = "float64", shape = (8, 44))#candidate|2229|(8, 44)|var|float64
const_2230 = relay.const([-8,-3,-2,10,-9,-10,-7,8,1,-7,-1,-10,2,9,-5,-9,-5,-7,-5,2,-10,-5,-9,10,-8,-5,-10,10,-2,-9,-5,-10,-1,7,4,10,-4,-10,9,-5,9,-7,-6,10,-6,-2,7,3,-1,-6,10,10,2,-8,-9,7,2,8,3,-5,9,3,-1,8,5,-10,9,-10,7,-1,3,-8,-3,5,4,-8,7,-3,-8,-4,-4,-9,-4,3,10,-10,1,8,-4,-4,2,3,5,-2,6,5,10,-2,-6,-6,6,-9,-3,5,-1,8,-2,5,-7,-10,2,-5,-1,5,-10,6,-6,-7,4,-8,10,10,-7,9,1,8,-5,4,-10,7,-9,-9,10,3,5,-8,-7,7,3,-7,5,8,10,10,-10,-1,-2,3,6,3,-7,-10,-9,-6,3,7,-1,-10,6,1,8,4,-6,-9,2,6,5,4,3,6,-5,5,-9,-5,6,-2,9,4,4,-8,7,8,1,6,1,-1,-7,2,-1,3,-2,4,3,-9,-1,-3,-4,-8,2,1,6,-2,8,10,-1,-9,-8,-6,-10,7,-3,-10,3,2,-4,1,-4,-4,8,-4,-9,-2,7,-7,5,10,6,3,-10,5,7,-5,-10,5,-4,-9,-5,9,10,-1,-10,3,3,-5,2,-6,-7,-1,-1,-7,7,-6,-6,6,-1,-1,10,-8,9,-5,-3,-9,3,9,8,6,1,-10,9,5,5,-10,9,7,1,-10,-4,-7,10,-8,2,-6,10,-4,-5,8,6,-4,-5,-4,2,1,4,10,3,-4,6,10,9,-4,4,4,-9,4,7,10,-3,-3,8,2,-5,-6,10,6,3,-4,1,4,4,4,5,1,5,-4,-1,-4,-3,-7,8,2,3,-8,-4,4,10,1,2,-1,8,-9,2,-5,-4,9,6,-5,9,-5,6,3,9,-1,-6,7,-8,4,8,6,-10,7,-6,6,6,8,-5,7,-5,-7,1,-6,10,8,7,-1,-8,-4,-1,-8,6,-8,-7,4,-3,4,5,-2,9,-3,5,5,4,-8,2,1,-3,8,6,-1,-1,3,-4,10,-7,10,-1,-5,-6,10,-8,7,-4,1,-5,8,-7,5,-8,-5,-10,-6,9,5,-4,-5,-10,6,-7,1,-9,-9,2,10,-9,-6,1,1,3,7,-3,-4,5,4,-4,4,-7,-4,9,10,10,-10,-8,-2,6,-10,2,-9,-3,8,1,-3,-5,9,2,5,-5,-2,3,-4,3,-6,-10,-1,2,-10,-9,1,-9,-1,10,-2,8,-8,10,-10,9,-6,-4,2,6,9,5,3,-2,7,-8,-9,-5,-9,-10,-5,-6,-8,10,6,-1,3,-5,-2,-9,-1,9,7,-6,6,5,6,4,2,5,-10,-3,4,9,6,-6,7,6,7,10,9,7,-9,-3,-5,-8,-5,-9,-8,-7,-8,-1,8,1,-9,-1,8,-6,-8,-7,7,1,-6,-3,1,-9,4,-4,-7,-10,-5,5,-8,2,1,-1,7,-2,-2,-7,6,-2,6,-5,-2,-9,5,-2,-8,10,-4,-8,3,-5,-5,-10,8,1,9,-9,10,-7,4,1,4,1,-4,-10,-1,4,7,6,5,1,7,4,-10,4,10,7,-7,-3,-9,10,8,-5,7,2,3,7,-5,-7,3,10,9,9,-6,-8,5,-7,1,10,5,3,7,-8,-2,9,8,-9,7,-4,-10,9,8,10,10,-9,-4,-5,-2,-5,-1,10,-4,-6,-6,-3,3,-2,10,10,4,6,-2,10,7,-10,10,8,10,-2,-4,-1,-10,8,6,1,9,-9,10,9,-5,-6,9,-8,7,5,6,10,10,-6,-8,-6,4,-10,-5,2,7,4,1,7,1,-3,10,2,1,-8,-5,-6,10,-3,-4,-4,4,-9,9,7,7,-8,1,-1,-8,-1,-3,-1,-2,9,-1,7,2,-2,-1,2,7,7,2,2,8,2,-2,-6,7,-10,-8,-4,4,-3,3,3,7,-1,9,-8,9,-8,-5,5,10,10,4,-8,10,-3,7,6,-7,3,-2,-3,-5,4,-5,-1,6,-5,-7,-9,6,-9,-8,-9,2,1,6,-5,-4,8,7,6,-3,4,-4,5,6,5,1,-9,7,-6,-1,-4,1,-4,-1,4,1,-4,-2,7,4,-2,-9,5,8,-10,4,5,6,-6,2,-3,-9,-2,-5,-10,2,-4,-2,6,2,-2,10,6,7,-2,-3,3,-1,4,5], dtype = "int16")#candidate|2230|(840,)|const|int16
call_2226 = relay.TupleGetItem(func_1168_call(relay.reshape(const_2227.astype('float64'), []), relay.reshape(var_2228.astype('float64'), [9, 16, 16]), relay.reshape(var_2228.astype('float64'), [9, 16, 16]), relay.reshape(var_2228.astype('uint64'), [9, 16, 16]), relay.reshape(var_2229.astype('float64'), [352,]), relay.reshape(const_2230.astype('int16'), [2, 420]), ), 7)
call_2231 = relay.TupleGetItem(func_1176_call(relay.reshape(const_2227.astype('float64'), []), relay.reshape(var_2228.astype('float64'), [9, 16, 16]), relay.reshape(var_2228.astype('float64'), [9, 16, 16]), relay.reshape(var_2228.astype('uint64'), [9, 16, 16]), relay.reshape(var_2229.astype('float64'), [352,]), relay.reshape(const_2230.astype('int16'), [2, 420]), ), 7)
output = relay.Tuple([uop_2217,call_2226,const_2227,var_2228,var_2229,const_2230,])
output2 = relay.Tuple([uop_2219,call_2231,const_2227,var_2228,var_2229,const_2230,])
func_2233 = relay.Function([var_2228,var_2229,], output)
mod['func_2233'] = func_2233
mod = relay.transform.InferType()(mod)
mutated_mod['func_2233'] = func_2233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2233_call = mutated_mod.get_global_var('func_2233')
var_2235 = relay.var("var_2235", dtype = "float64", shape = (2304,))#candidate|2235|(2304,)|var|float64
var_2236 = relay.var("var_2236", dtype = "float64", shape = (8, 44))#candidate|2236|(8, 44)|var|float64
call_2234 = func_2233_call(var_2235,var_2236,)
output = call_2234
func_2237 = relay.Function([var_2235,var_2236,], output)
mutated_mod['func_2237'] = func_2237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1742_call = mod.get_global_var('func_1742')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_2251 = relay.TupleGetItem(func_1742_call(), 1)
call_2252 = relay.TupleGetItem(func_1744_call(), 1)
output = relay.Tuple([call_2251,])
output2 = relay.Tuple([call_2252,])
func_2262 = relay.Function([], output)
mod['func_2262'] = func_2262
mod = relay.transform.InferType()(mod)
mutated_mod['func_2262'] = func_2262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2262_call = mutated_mod.get_global_var('func_2262')
call_2263 = func_2262_call()
output = call_2263
func_2264 = relay.Function([], output)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2262_call = mod.get_global_var('func_2262')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_2284 = relay.TupleGetItem(func_2262_call(), 0)
call_2285 = relay.TupleGetItem(func_2264_call(), 0)
func_997_call = mod.get_global_var('func_997')
func_1000_call = mutated_mod.get_global_var('func_1000')
const_2300 = relay.const(4.108174, dtype = "float64")#candidate|2300|()|const|float64
const_2301 = relay.const([-4.534679,-5.527296,-4.669709,-0.447310,0.763867,6.476531,2.762657,-3.012358,4.208288,6.846957,2.090420,9.887272,3.814575,-9.397114,-1.871228,6.592440,-7.967152,2.117466,5.783688,-3.126106,-6.049519,-6.721006,-3.861162,-3.262347,8.322221,-3.145354,-2.738962,6.176957,-3.190211,-4.272936,-7.548279,-0.011547,1.658103,1.340098,8.708661,-8.980046,8.884013,8.907627,0.741960,-6.112942,7.084776,2.713192,-4.159834,-7.684677,-4.586037,-1.080657,-2.820278,-1.482318,-2.023113,-8.858657,2.616142,9.989731,3.219009,-4.484199,8.681090,3.331494,-2.346947,-0.097249,-2.684440,6.268107,-4.593854,5.811838,-9.240116,-5.283031,8.899312,5.304617,2.046334,0.693180,6.056782,-4.072340,-1.306433,-6.699490,-1.302484,-4.434659,9.164486,-4.455084,0.301832,-0.401414,6.698140,-1.488951,0.416056,4.322912,-8.687678,8.803751,9.261034,-0.633654,1.791154,-0.615250,-3.577535,-3.501899,-3.087061,0.934812,-2.718754,-4.794835,-3.061939,-2.851594,-3.080144,5.317960,5.210787,-1.575918,-8.522563,-9.154188,6.334930,0.221503,1.687996,3.505216,-5.476634,4.615935,-4.264677,-4.455147,-4.232749,-6.562625,5.898737,-8.867572,-9.247122,6.481188,6.424905,1.752018,-5.363655,-0.620219,-8.873538,6.369296,-2.914716,-1.342239,-7.213814,-7.280342,4.337715,4.633077,-9.575715,3.870539,6.311483,9.153018,6.446539,8.907943,2.402836,3.887878,-6.003276,9.602070,-8.088333,9.730525,-8.055399,1.865390,6.975047,-8.091646,-0.920346,-2.631045,-5.844964,1.565114,-7.218267,1.020271,-4.264396,-9.752011,-0.689841,-5.341215,0.808875,6.702251,8.658775,0.972021,-9.957091,-0.166064,-6.624432,-3.696546,-8.425079,-5.733049,-7.983363,-9.081632,-2.923068,9.711797,-5.822826,4.165979,-7.189998,-1.447258,-7.240940,-3.884366,8.920802,6.288870,7.518195,3.963768,5.805631,9.952513,8.248075,1.736052,-0.448544,-9.248214,-7.963396,-6.531961,2.041824,-9.154123,-1.346816,-3.588355,6.201192,8.154549,1.582806,-6.397865,-0.692304,-5.347058,1.499759,-6.237034,1.385292,6.407780,-6.066248,-4.115355,-5.463322,2.825102,9.390267,-5.310091,-3.758418,7.388426,-9.920415,-0.646517,3.306045,5.404479,-1.969426,-1.348032,-5.578361,1.445813,4.654374,-2.828468,-5.904769,9.867304,8.797002,-0.459681,5.841102,1.671599,9.175490,4.824672,6.016655,-5.016363,-5.184705,9.443984,-3.808773,7.098613,-8.749479,6.287644,-9.810994,-5.060572,-5.741599,6.598290,-5.901694,-6.956598,-2.999475,7.076182,-2.056413,-1.930998,-8.737265,6.802048,-6.234336,1.840421,3.179761,-2.264708,2.879891,5.167053], dtype = "float32")#candidate|2301|(252,)|const|float32
call_2299 = relay.TupleGetItem(func_997_call(relay.reshape(const_2300.astype('float64'), []), relay.reshape(const_2301.astype('float32'), [252, 1]), ), 0)
call_2302 = relay.TupleGetItem(func_1000_call(relay.reshape(const_2300.astype('float64'), []), relay.reshape(const_2301.astype('float32'), [252, 1]), ), 0)
bop_2311 = relay.floor_mod(call_2299.astype('float64'), const_2300.astype('float64')) # shape=(2, 2, 13)
bop_2314 = relay.floor_mod(call_2302.astype('float64'), const_2300.astype('float64')) # shape=(2, 2, 13)
bop_2322 = relay.greater_equal(const_2300.astype('bool'), call_2299.astype('bool')) # shape=(2, 2, 13)
bop_2325 = relay.greater_equal(const_2300.astype('bool'), call_2302.astype('bool')) # shape=(2, 2, 13)
func_1292_call = mod.get_global_var('func_1292')
func_1296_call = mutated_mod.get_global_var('func_1296')
var_2327 = relay.var("var_2327", dtype = "float64", shape = (3, 12))#candidate|2327|(3, 12)|var|float64
const_2328 = relay.const([-7,-1,-1,-10,-7,9,10,1,3,-5,9,-9,-6,5,9,4,7,4,6,-7,6,-8,-3,4,-3,3,2,2,3,5,7,7,7,-4,-7,5,-6,-2,1,9,5,-3,5,9,5,9,-5,8,2,-6,-4,4,3,-2,-2,-8,4,5,9,7,-10,-5,-5,-1,-4,5,8,-9,5,-5,2,-5,-5,6,-6,7,9,1,3,-10,8,7,7,9,7,9,9,8,6,-9,4,8,-8,-7,2,-9,5,8,-2,-3,5,10,8,2,-9,6,-7,-9,3,5,7,6,10,3,-3,10,-2,3,-6,4,6,-3,2,9,9,-1,-9,-8,10,-10,-2,2,1,-4,2,4,-5,4,-10,5,10,6,2,10,-9,-7,-1,3,-6,-8,-2,-8,-1,8,-7,1,-8,7,-4,2,-7,2,-7,1,1,-4,4,-4,4,6,-5,-9,5,1,-2,1,-1,9,-10,-3,-10,6,9,-6,-1,6,-9,-9,2,-4,-4,-4,-9,-4,3,-10,4,-4,-5,8,5,4,-1,-8,2,7,-6,4,6,-4,5,2,9,4,8,-2,8,-5,-6,3,-5,-7,-5,-6,-8,10,4,5,-7,7,-3,-6,-4,3,6,-9,8,1,6,-4,6,8,-7,-3,-3,10,1,6,-9,-7,-5,-5,4,-8,-1,-5,-6,9,7,8,4,6,5,3,3,8,-6,-2,-7,1,1,-7,2,-2,9,10,9,-1,10,-8], dtype = "uint16")#candidate|2328|(280,)|const|uint16
const_2329 = relay.const([10,1,2,-10,-8,-10,2,2,-2,4,-6,-8,7,10,8,6,-5,-9,5,-9,-2,9,-2,8,3,5,-8,6,-10,3,-2,-7,-5,5,8,4,-6,6,5,-1,9,-8,9,-2,-10,7,5,-10,-2,2,-10,2,1,-1,1,9,-8,-6,-8,-5,3,-2,-8,9,-7,10,7,-1,-9,9,4,1,-2,10,3,-2,-7,-5,5,7,-4,9,-8,-2,-3,-6,-8,3,-3,-3,6,5,10,-10,-5,-8,3,-2,8,-7,-8,9,9,-7,-5,-1,6,8,-7,2,5,-2,-5,-9,-2,-3,-1,-6,6,-3,6,6,1,9,-2,9,-8,8,-9,6,5,-10,6,7,1,-5,-5,8,-2,-3,5,4,4,7,-10,5,-6,2,-2,4,-2,-8,-9,-2,-1,-7,-8,10,-2,-7,1,10,6,-9,-2,10,1,10,4,3,8,2,3,-7,-10,-9,-6,-8,10,1,-10,5,-8,-5,6,8,10,-9,-3,-9,-3,-3,9,1,3,-3,-2,-6,5,5,-1,-7,-4,-5,-5,9,5,8,7,7,-3,3,-1,8,-4,9,-5,-6,3,5,6,-7,-9,-6,8,6,-4,-7,-2,2,7,1,8,-2,-7,-10,-2,-3,-5,7,2,5,6,10,-6,-6,-4,6,2,-4,4,1,2,-6,5,-10,-1,-3,-6,7,-7,-6,1,6,1,-4,3,-10,-1,4,4,-5,7,-3,2,7,-4,4,-5,9,-8,1,-8,8,1,-7,6,-9,-1,5,4,-5,-5,4,-9,7,5,3,-3,7,3,-1,8,-1,2,-2,-10,-5,-8,-8,-1,8,-5,1,2,-1,4,5,2,8,-5,-2,-9,-1,-7,6,4,-6,-5,-6,-7,-5,1,-2,7,8,-2,7,1,-8,7,-6,8,-9,-1,1,1,8,5,4,-9,3,7,3,-8,-4,-5,-7,4,-7,10,-2,5,3,-9,-3,3,2,-6,6,5,10,-2,-4,-10,1,10,-10,-5,-6,-4,-5,-5,-5,-1,4,2,-8,8,3,5,-9,-9,-2,4,9,7,2,-2,-2,9,10,9,-6,-2,-6,-2,3,-1,-6,-5,2,-2,3,-1,-6,10,-2,4,5,-8,2,-3,3,-2,-1,-5,-8,-7,-10,7,-1,-2,5,2,1,-10,-1,-9,-10,-3,-7,-6,-5,5,5,3,-8,-10,10,-4,3,-5,-8,-9,5,-9,-10,5,-10,-3,2,-1,-1,-3,5,2,-1,4,-3,-8,-3,-1,4,10,-6,-6,-9,1,10,-10,3,-2,-3,4,9,2,-10,7,-1,-7,2,-7,2,10,4,-4,-6,-1,-5,2,-8,-8,-9,2,3,-7,3,-5,-4,7,-9,-4,9,3,-10,-8,1,-9,-10,-2,-2,-6,-5,-2,-8,-8,9,-1,5,4,8,6,-7,-2,7,10,5,4,10,2,4,4,-9,-4,6,-2,2,-6,4,-8,3,2,-7,-1,-4,-3,-10,4,2,6,9,-2,7,-10,7,-3,7,10,2,10,-2,-6,10,4,9,-9,7,9,-1,-4,-6,-1,-2,8,-10,-4,1,-7,-10,-4,10,-9,-7,8,7,8,-10,-8,-10,10,5,6,-2,7,-5,-2,4,-9,-10,-3,-2,-10,-2,7,-5,5,9,-5,6,6,5,-6,9,-2,-4,-6,5,-9,4,-10,2,-10,7,-3,-9,2,-7,5,-4,5,-3,6,-6,-7,-2,-1,2,-5,-7,10,9,4,-2,2,-7,6,9,-9,9,-7,-5,-3,-8,-6,9,4,9,4,6,-9,-4,-4,9,9,-1,6,3,-3,-10,-7,-6,-6,9,-8,7,-10,2,-5,-1,-6,-3,10,-4,8,-3,-4,7,6,2,-3,-1,10,-8,4,-1,4,5,-1,-9,4,5,-3,-1,-10,-4,2,5,1,-6,5,-5,3,-4,-8,5,-5,3,-5,-10,5,-8,-9,8,-10,-5,6,-5,8,5,-2,-10,-9,6,7,-8,10,-1,1,-1,6,8,-5,-10,2,-9,-4,-1,3,-8,3,-3,4,-6,-3,-7,-2,-10,-8,10,-8,2,9,8,1,2,-1,-9,-1,1,-1,-5,-3,-9,-7,-1,-7,8,6,-8,1,-3,7,9,-6,-3,1,9,3,5,7,7,-8,-10,3,3,9,8,5,-5,-10,-7,4,-4,-4,-7,4,-2,8,-9,1,-5,-8,-8,2,4,-2,10,-9,-5,3,1,-5,-2,-9,6,-2,10,-3,3,-4,7,1,3,4,-2,-1,4,8,-1,-8,-6,-7,2,-5,-7,-5,-4,-2,6,-7,2,-9,-4,-4,-5,3,3,-8,-1,-10,-1,-3,-1,3,10,4,-8,8,-4,-8,-5,10,10,-2,10,-9,7,7,-8,5,-2,10,6,3,-2,-8,-9,-2,-6,-2,-6,-9,-5,-3,9,-1,-1,-3,10,-4,7,7,10,-7,-4,5,1,5,2,-9,9,4,-2,6,2,-4,2,5,3,-8,-10,-8,-7,-7,4,2,9,-3,4,4,-9,-5,2,-5,-3,-5,-8,-5,8,5,-9,7,-4,8,-2,-4,-1,-6,-10,-1,3,-7,8,7,-4,-2,-1,3,-9,-3,-3,4,9,-10,-10,-3,6,-6,-2,2,7,-2,-3,4,-6,-5,-6,-5,-10,4,-6,4,7,-6,-5,6,2,-10,1,-7,3,-7,2,3,-7,-3,-6,-4,-7,1,-3,-5,2,-10,-1,1,-10,4,10,-5,6,1,4,-2,-10,-4,9,7,-7,8,5,-6,10,10,-7,9,2,-3,9,-7,10,9,-3,3,-3,-1,-2,7,7,2,-2,-5,-2,1,6,10,1,5,6,-5,-1,-1,-5,3,-4,4,-9,-2,-9,-4,-1,3,4,8,-8,-10,1,-1,8,6,2,-9,1,2,4,-7,10,9,-9,-1,9,-7,-3,-5,-4,-4,-1,7,-6,-1,7,-7,7,-9,2,3,-3,2,-9,-6,9,9,-7,-1,-7,5,-2,9,10,-6,-7,-6,9,8,-4,-1,6,-3,6,8,-8,-5,7,2,1,-4,4,1,-5,-1,5,1,10,6,8,9,-9,10,10,7,-7,10,-8,-7,1,-3,-8,10,6,5,-2,-4,1,-8,4,-2,6,-4,-6,9,-7,-6,5,-6,-1,-9,-7,5,8,1,-9,-5,-7,-1,-10,-10,1,3,-1,-8,-1,-7,-1,8,-6,-1,4,-3,-5,-5,3,1,1,-1,-4,-7,10,-3,6,10,2,10,9,10,6,-8,-3,4,-6,8,-7,-3,7,-8,7,7,-1,-9,8,4,-5,2,5,3,4,9,4,-6,8,-6,-4,-8,7,3,7,9,4,-3,9,8,5,5,-1,-2,7,-8,10,3,-3,3,8,5,3,-8,-4,-8,-6,-10,-3,6,10,-10,9,-8,-4,4,2,3,-7,-10,9,-10,10,-10,2,-5,-1,5,-10,2,-3,-5,6,-10,9,4,7,-3,-3,10,-10,-10,-9,10,-7,5,-9,-4,-10,-9,-4,7,8,6,2,7,-10,2,3,1,4,-1,-8,-9,-1,7,1,7,-3,-1,1,-6,6,-4,-4,8,-3,-3,3,-9,-10,10,-10,1,1,10,-1,-7,-8,5,-6,-10,-9,3,-4,-6,9,-8,-4,6,-4,-7,3,-1,5,-1,-6,-3,3,-10,-6,-3,-2,-8,3,-2,-8,-9,5,2,-5,-10,-3,7,8,-4,4,1,-10,4,5,-10,7,6,9,-1,-10,-7,-5,-10,4,7,-3,5,1,9,-7,9,-8,5,10,4,-6,-4,5,-4,-7,-6,1,-6,-1,8,-3,4,-1,-3,-5,-2,5,-4,7,-9,10,7,-7,6,7,7,-1,5,8,-3,-2,5,-9,10,-6,-2,-4,-10,1,8,7,2,-6,2,-5,-8,9,6,2,-8,5,-7,-9,8,10,-2,3,9,-10,-3,3,2,5,-2,6,-7,9,9,-10,2,5,1,7,-5,-8,-2,10,-4,5,-3,-7,-9,-4,-6,7,6,-3,8,-4,7,-3,-2,-6,-9,-4,10,-3,-8,9,-3,4,-6,6,-7,1,2,-4,9,3,-8,2,-8,7,4,-2,2,-8,-4,-6,-5,-4,3,3,5,9,5,-1,6,1,-8,9,-8,10,-9,3,-3,3,3,7,-6,-3,-8,3,6,6,-6,2,9,-6,-10,4,-3,1,-5,-8,-5,-1,7,8,10,5,-6,8,1,-6,2,-6,9,5,-4,-6,-1,-3,-2,2,-5,-6,4,-8,9,-7,4,-7,9,-6,2,3,8,4,4,-10,2,10,9,2,2,10,-3,8,1,-4,-5,-10,2,2,9,5,-7,7,6,7,-9,3,-6,-3,-6,-9,5,-5,3,-10,-9,-4,-3,6,10,-7,-10,2,-3,10,1,2,9,2,-7,2,9,-4,-9,-2,-4,10,1,-8,7,4,7,6,5,6,10,8,8,-4,2,7,-6,8,1,2,3,-9,-5,-6,5,-2,2,6,4,6,-9,2,10,-3,-7,8,-4,-2,-4,-9,10,3,1,-3,-1,-1,-4,6,-6,-4,5,-4,-10,7,-5,-2,8,-1,5,4,-7,-6,1,-4,10,-9,-1,-5,-1,7,-9,-3,4,-5,-9,5,-7,6,3,-4,-7,2,-8,-1,9,5,6,-4,3,9,8,8,5,3,2,-2,10,9,1,7,9,-10,1,7,-3,5,-2,-7,9,-6,-7,1,4,-7,9,7,-7,3,8,1,-8,-3,1,9,1,-10,6,8,-3,-5,9,10,-6,4,-5,-7,3,-5,-1,-4,-10,1,-8,-5,5,3,1,-2,8,-3,10,8,-10,-8,5,-3,8,10,4,7,5,-5,-5,3,10,-8,6,4,7,6,3,1,-5,7,8,1,6,-2,-1,-6,-3,-3,-8,-6,10,1,3,-5,2,-8,-8,4,4,-6,-10,-8,-7,-3,-10,4,-3,5,6,4,4,10,2,-7,-1,1,-7,6,2,3,-8,-3,-3,-9,-8,8,-7,-3,4,5,-5,7,-7,-8,-2,-10,9,3,2,2,5,2,-10,-10,5,10,-6,-3,-1,2,5,6,-7,-7,-3,9,-1,-1,-5,5,-8,3,-1,-7,-9,-8,2,8,6,-8,-4,-6,-7,-6,-10,6,6,-4,-6,-1,-1,-1,4,-2,-7,-9,5,-8,2,7,-4,2,2,9,6,-5,1,-9,7,3,-2,-7,-8,1,8,4,3,-4,-1,-5,4,-3,7,-8,-5,-10,-5,-6,-1,-5,-7,3,-6,-6,-1,-3,4,10,7,-8,10,9,-5,8,-2,-3,3,-10,2,-5,9,-7,-1,-6,4,-1,2,-10,3,-2,-3,5,-2,5,10,-6,6,-2,10,-5,2,9,-8,-10,6,-7,9,-5,4,5,-9,-3,-6,-2,-4,3,7,-9,-10,5,3,7,3,-10,-3,2,-6,7,-1,10,-7,1,-2,8,-1,2,-4,-7,2,-3,2,6,-10,2,1,-7,3,-4,-8,1,-3,5,-1,-4,10,7,-3,-4,4,-4,-9,5,9,-1,2,-8,4,-4,-8,9,6,-1,-8,9,2,9,4,-3,5,-2,5,-4,5,-3,6,10,7,8,8,-9,3,-2,-6,-4,1,10,7,-7,1,7,2,-9,1,-8,7,1,-7,-8,10,-6,9,-8,-7,1,5,-5,-5,9,2,-7,5,10,1,-7,-2,-3,-8,-7,8,-4,6,-1,4,1,5,6,5,4,-7,-10,-3,-10,-6,7,-7,-6,-2,7,8,3,-5,-5,-6,10,-9,2,3,-4,-1,4,4,4,-8,-2,-9,10,-4,8,-4,-3,9,7,-7,1,-4,7,-7,-3,-10,-1,-8,4,-6,1,-1,4,-10,-1,4,5,9,5,1,-10,1,-1,-2,2,-7,1,9,-5,-6,4,-8,-5,10,-2,-8,-5,4,9,-1,8,-5,-6,-4,-3,-7,8,7,4,-5,-2,9,-3,3,2,4,4,9,-6,-2,1,8,-9,-7,4,-9,7,4,-2,-4,1,-2,-1,-8,4,-8,1,6,-2,-3,7,3,-10,3,-1,4,-7,10,9,-5,-8,-8,10,1,7,8,-3,-7,5,-5,-7,2,-7,-1,10,7,-10,9,1,2,1,3,1,1,9,4,-4,3,-7,-8,-2,-5,2,-4,3,10,-8,-1,2,-2,-5,1,1,5,-8,-6,-9,-5,-6,-5,-7,-2,7,-1,-5,-2,-1,2,-4,-1,9,3,8,-1,8,-3,1,7,1,1,-5,8,7,-8,-6,-5,8,-5,5,3,3,8,3,6,-5,2,9,6,10,6,4,-1,9,-9,3,8,7,-2,3,-6,2,-8,6,8,7,1,5,-4,-9,1,-2,-10,6,9,7,-10,3,-1,-4,-4,2,4,7,-4,-8,8,7,-1,9,4,5,-4,-4,7,1,8,-7,3,-8,-2,-3,8,-10,4,-9,3,4,4,2,3,5,7,4,7,8,-8,-10,2,5,7,-6,-8,10,8,5,5,3,-1,-3,-6,-8,1,-1,9,-9,-10,9,-5,1,-8,5,6,5,-4,8,9,-6,-5,3,3,-10,-7,2,-5,7,9,7,9,-5,-2,3,-10,-2,-6,-8,-9,3,-7,-9,-5,-8,-8,10,-8,-10,-9,-4,2,1,-2,-8,-9,-6,3,1,-4,4,5,-9,10,-5,-4,5,6,-5,-7,7,3,2,-1,-6,1,6,6,9,7,-7,5,-9,10,-7,-7,4,-2,-6,9,-7,-3,-8,-10,-7,1,2,-5,-6,4,-1,2,3,-4,-6,-2,-5,7,4,-10,-8,4,-8,-10,-4,-10,7,2,5,-8,9,5,5,-9,1,1,-10,-9,5,-3,-6,-4,4,-1,-4,-1,9,8,7,-6,-7,-2,-3,5,2,5,-2,9,6,6,-10,-2,-2,6,10,-10,8,-3,-4,-9,8,-2,-4,8,-4,-2,1,5,8,3,-3,4,6,2,-6,4,-4,8,-1,10,3,8,-7,7,6,3,6,1,-3,-2,4,6,-6,8,1,1,-3,9,-3,5,-6,-7,6,-4,10,9,-6,4,9,7,1,5,-8,3,-1,-1,9,-1,7,-3,3,-3,-6,1,8,-9,-6,4,-9,5,7,8,3,10,-7,7,4,-9,6,10,-7,-4,3,7,6,3,6,-9,3,9,2,-7,5,-7,-5,-4,5,-5,5,-2,4,4,7,8,-3,-9,2,-9,4,-7,-4,1,-10,-8,8,6,5,1,5,3,8,-1,10,9,-10,2,9,5,-2,4,5,4,-4,-4,-6,-5,1,-5,9,-4,2,5,1,-3,-5,5,-9,-1,-5,9,2,-4,-3,-3,-6,-3,4,2,-10,-10,-1,6,-5,-2,2,2,7,-8,-6,5,9,-10,10,10,-6,6,7,-9,10,3,-3,7,-10,2,-7,7,9,-1,-1,8,1,-7,9,-1,5,3,10,10,9,7,1,4,-3,-8,3,-4,-3,3,6,2,-7,-9,-7,8,-1,1,-8,3,-9,-8,10,-9,2,4,5,9,-1,8,9,3,10,3,1,1,-8,4,-10,10,4,-10,-8,-10,7,-6,-5,-6,4,-3,7,7,-3,-5,6,7,-7,-1,-5,-3,-1,1,-7,1,8,8,-7,3,8,5,1,-5,8,-3,-7,7,5,-3,5,-6,7,-8,-9,-8,-7,10,-6,8,1,9,10,-5,4,-7,-4,-1,9,7,8,-6,8,-7,-2,-8,-8,10,-3,-3,3,-5,5,7,-3,3,-10,10,-4,4,-2,9,-1,8,-4,-10,-2,-3,1,10,-4,7], dtype = "uint8")#candidate|2329|(2925,)|const|uint8
call_2326 = relay.TupleGetItem(func_1292_call(relay.reshape(var_2327.astype('float64'), [3, 12, 1]), relay.reshape(const_2328.astype('uint16'), [280,]), relay.reshape(const_2329.astype('uint8'), [2925,]), ), 7)
call_2330 = relay.TupleGetItem(func_1296_call(relay.reshape(var_2327.astype('float64'), [3, 12, 1]), relay.reshape(const_2328.astype('uint16'), [280,]), relay.reshape(const_2329.astype('uint8'), [2925,]), ), 7)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_2336 = relay.TupleGetItem(func_1839_call(), 2)
call_2337 = relay.TupleGetItem(func_1841_call(), 2)
func_1992_call = mod.get_global_var('func_1992')
func_1995_call = mutated_mod.get_global_var('func_1995')
var_2353 = relay.var("var_2353", dtype = "float64", shape = (2, 40))#candidate|2353|(2, 40)|var|float64
call_2352 = relay.TupleGetItem(func_1992_call(relay.reshape(var_2353.astype('float64'), [2, 5, 8])), 0)
call_2354 = relay.TupleGetItem(func_1995_call(relay.reshape(var_2353.astype('float64'), [2, 5, 8])), 0)
func_1992_call = mod.get_global_var('func_1992')
func_1995_call = mutated_mod.get_global_var('func_1995')
call_2355 = relay.TupleGetItem(func_1992_call(relay.reshape(var_2353.astype('float64'), [2, 5, 8])), 0)
call_2356 = relay.TupleGetItem(func_1995_call(relay.reshape(var_2353.astype('float64'), [2, 5, 8])), 0)
bop_2359 = relay.floor_divide(call_2336.astype('float32'), relay.reshape(const_2329.astype('float32'), relay.shape_of(call_2336))) # shape=(2925,)
bop_2362 = relay.floor_divide(call_2337.astype('float32'), relay.reshape(const_2329.astype('float32'), relay.shape_of(call_2337))) # shape=(2925,)
var_2368 = relay.var("var_2368", dtype = "int16", shape = (840,))#candidate|2368|(840,)|var|int16
bop_2369 = relay.greater(call_2284.astype('bool'), relay.reshape(var_2368.astype('bool'), relay.shape_of(call_2284))) # shape=(840,)
bop_2372 = relay.greater(call_2285.astype('bool'), relay.reshape(var_2368.astype('bool'), relay.shape_of(call_2285))) # shape=(840,)
func_139_call = mod.get_global_var('func_139')
func_143_call = mutated_mod.get_global_var('func_143')
const_2378 = relay.const([1.293436,2.589154,-7.722228,-9.089220,0.762906,8.112860,1.567196,2.164476,6.506944,9.224314,5.478555,-8.445784,1.017150,4.938910,-0.194572,-1.937087,2.147759,-6.907570,2.181244,0.562198,4.107445,-3.370667,-1.726893,6.116959,7.630144,-4.490644,5.231484,7.555052,9.528114,9.449133,0.179159,5.698288,-4.127636,-4.453021,-2.531727,-1.513213,-2.726291,-3.282109,-3.310669,-9.561614,-8.078832,-3.847071,7.992431,-1.007668,-4.538510,4.836031,3.061102,-6.870030,-8.845682,3.030894,2.109603,1.905513,0.299025,-8.895106,4.312747,4.200185,5.983231,1.190899,9.349507,3.305722,5.638781,9.669033,-9.055091,-9.386827,-6.009321,0.661036,8.196066,1.603162,8.162986,-5.081099,-9.080492,-7.067010,-7.245149,5.075754,-3.531664,3.000939,7.631408,-3.223422,1.200196,-7.991135,6.143634,1.960038,-0.623049,5.412668,-6.622183,-3.816753,8.511053,-2.975470,-6.426576,8.554798,7.532554,8.757068,6.769445,-5.180546,-5.257753,-1.484147,-4.768995,8.314704,-1.096767,-8.434683,-3.535849,4.729972,-9.918994,6.003004,1.028979,9.121683,-5.895083,4.174197,-0.114546,-8.699309,2.071117,-2.062017,-8.187780,-6.993416,-9.836570,7.559004,-2.994846,-3.170085,-9.972815,0.708164,-3.241869,-8.561770,9.467994,-7.052822,0.015560,8.857057,1.376506,9.602027,4.928775,-5.400885,-8.703801,-9.752339,1.996293,9.678716,3.379428,7.157922,2.693417,-2.719183,-6.344794,8.772391,6.742046,-8.395969,-3.767343,-0.023743,4.452180,-9.848648,-0.859285,-0.166726,5.215092,4.186798,7.470302,9.205101,7.088043,9.827718,-0.785994,6.324422,6.326417,4.166955,3.373296,2.700340,-8.112082,4.715164,1.406111,-7.601921,9.773210,0.262084,3.025696,-6.251719,-4.577458,-8.297806,-0.079178,-6.163984,7.541466,3.422215,9.920727,6.206741,-5.491426,-9.832317,2.664975,5.599210,-1.066667,9.740539,7.422517,-9.509890,0.639208,-7.234413,5.636913,-5.707116,-2.341539,4.945530,-0.557992,-2.256775,2.212846,-6.948702,1.230257,-7.412609,-9.887633,7.551512,3.434298,9.717367,-3.011638,-3.980612,-8.164618,-0.090622,-8.191683,-1.652896,8.400614,-4.466973,7.192769,3.122453,-6.031522,3.539765,1.751122,-4.592491,-2.365129,8.624093,9.794769,-5.173430,-4.936051,3.115903,0.351983,-5.052184,-7.870191,8.114224,2.917279,-7.746822,-0.282943,9.757248,5.151481,-6.776497,0.060145,-0.764276,4.309730,0.138961,-1.460608,5.603932,-7.584250,-2.985397,-6.991317,5.651808,-7.888909,4.200292,2.545018,-2.698438,-9.479428,-2.469779,-0.978570,-9.617703,-2.002100,-8.599019,-3.205973,-3.922924,5.336896,5.806792,-3.027513,0.391997,0.058338,-2.972267,4.482993,9.933832,2.259120,-5.645426,-3.595227,-7.309944,-1.203213,8.407805,-7.879062,6.782298,-6.314854,9.891750,3.135559,3.004067,3.475684,8.559017,-5.972615,-6.648676,2.101531,-6.792763,3.949934,-8.768323,8.852699,6.180697,8.708220,4.194266,5.322083,-7.407926,7.231480,7.343206,7.768944,-0.951476,4.617401,-3.214376,2.974102,4.087557,7.394296,-6.764807,5.334288,-3.462466,-6.062621,0.285497,-7.215872,3.830218,6.503279,-3.767919,0.768142,8.033175,5.282185,0.589518,-4.453097,6.326172,-7.417213,-6.907145,4.177575,-9.384116,-0.067882,-3.153022,-1.879758,-7.431596,-7.868283,-7.357713,0.703351,9.379480,9.533794,3.393410,8.478037,2.627015,-9.856949,4.294222,-0.092626,-8.754206,3.902814,3.921164,-5.701500,-1.857560,-5.925043,-8.875112,-1.730170,-8.570612,0.131541,3.583456,2.425937,-5.748110,-6.914163,2.108100,-8.165762,8.201708,-4.899914,1.657870,-0.213860,-6.210877,-3.986754,9.335944], dtype = "float64")#candidate|2378|(352,)|const|float64
call_2377 = relay.TupleGetItem(func_139_call(relay.reshape(const_2328.astype('uint16'), [70, 4]), relay.reshape(const_2378.astype('float64'), [11, 4, 8]), ), 2)
call_2379 = relay.TupleGetItem(func_143_call(relay.reshape(const_2328.astype('uint16'), [70, 4]), relay.reshape(const_2378.astype('float64'), [11, 4, 8]), ), 2)
output = relay.Tuple([const_2301,bop_2311,bop_2322,call_2326,var_2327,const_2328,call_2352,var_2353,call_2355,bop_2359,bop_2369,call_2377,const_2378,])
output2 = relay.Tuple([const_2301,bop_2314,bop_2325,call_2330,var_2327,const_2328,call_2354,var_2353,call_2356,bop_2362,bop_2372,call_2379,const_2378,])
func_2381 = relay.Function([var_2327,var_2353,var_2368,], output)
mod['func_2381'] = func_2381
mod = relay.transform.InferType()(mod)
var_2382 = relay.var("var_2382", dtype = "float64", shape = (3, 12))#candidate|2382|(3, 12)|var|float64
var_2383 = relay.var("var_2383", dtype = "float64", shape = (2, 40))#candidate|2383|(2, 40)|var|float64
var_2384 = relay.var("var_2384", dtype = "int16", shape = (840,))#candidate|2384|(840,)|var|int16
output = func_2381(var_2382,var_2383,var_2384,)
func_2385 = relay.Function([var_2382,var_2383,var_2384,], output)
mutated_mod['func_2385'] = func_2385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2262_call = mod.get_global_var('func_2262')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_2387 = relay.TupleGetItem(func_2262_call(), 0)
call_2388 = relay.TupleGetItem(func_2264_call(), 0)
var_2394 = relay.var("var_2394", dtype = "int16", shape = (840,))#candidate|2394|(840,)|var|int16
bop_2395 = relay.maximum(call_2387.astype('uint64'), relay.reshape(var_2394.astype('uint64'), relay.shape_of(call_2387))) # shape=(840,)
bop_2398 = relay.maximum(call_2388.astype('uint64'), relay.reshape(var_2394.astype('uint64'), relay.shape_of(call_2388))) # shape=(840,)
output = relay.Tuple([bop_2395,])
output2 = relay.Tuple([bop_2398,])
func_2404 = relay.Function([var_2394,], output)
mod['func_2404'] = func_2404
mod = relay.transform.InferType()(mod)
mutated_mod['func_2404'] = func_2404
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2405 = relay.var("var_2405", dtype = "int16", shape = (840,))#candidate|2405|(840,)|var|int16
func_2404_call = mutated_mod.get_global_var('func_2404')
call_2406 = func_2404_call(var_2405)
output = call_2406
func_2407 = relay.Function([var_2405], output)
mutated_mod['func_2407'] = func_2407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_2412 = relay.TupleGetItem(func_1839_call(), 0)
call_2413 = relay.TupleGetItem(func_1841_call(), 0)
output = call_2412
output2 = call_2413
func_2425 = relay.Function([], output)
mod['func_2425'] = func_2425
mod = relay.transform.InferType()(mod)
output = func_2425()
func_2426 = relay.Function([], output)
mutated_mod['func_2426'] = func_2426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2444 = relay.var("var_2444", dtype = "int32", shape = (2, 8, 2))#candidate|2444|(2, 8, 2)|var|int32
var_2445 = relay.var("var_2445", dtype = "int32", shape = (2, 8, 2))#candidate|2445|(2, 8, 2)|var|int32
bop_2446 = relay.left_shift(var_2444.astype('int32'), relay.reshape(var_2445.astype('int32'), relay.shape_of(var_2444))) # shape=(2, 8, 2)
output = relay.Tuple([bop_2446,])
output2 = relay.Tuple([bop_2446,])
func_2456 = relay.Function([var_2444,var_2445,], output)
mod['func_2456'] = func_2456
mod = relay.transform.InferType()(mod)
mutated_mod['func_2456'] = func_2456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2456_call = mutated_mod.get_global_var('func_2456')
var_2458 = relay.var("var_2458", dtype = "int32", shape = (2, 8, 2))#candidate|2458|(2, 8, 2)|var|int32
var_2459 = relay.var("var_2459", dtype = "int32", shape = (2, 8, 2))#candidate|2459|(2, 8, 2)|var|int32
call_2457 = func_2456_call(var_2458,var_2459,)
output = call_2457
func_2460 = relay.Function([var_2458,var_2459,], output)
mutated_mod['func_2460'] = func_2460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2262_call = mod.get_global_var('func_2262')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_2475 = relay.TupleGetItem(func_2262_call(), 0)
call_2476 = relay.TupleGetItem(func_2264_call(), 0)
func_1292_call = mod.get_global_var('func_1292')
func_1296_call = mutated_mod.get_global_var('func_1296')
const_2490 = relay.const([1.932581,-9.475925,1.135171,-2.511447,-4.234385,-2.883210,-1.024294,3.449431,2.088408,5.475318,-8.229967,-9.251430,-4.140861,6.071929,-1.115472,9.088174,-6.197337,4.714162,-5.799632,9.201944,-6.215664,-9.333171,5.142617,-0.020373,-2.991504,-2.864275,-5.516411,-0.873640,3.756469,-7.495197,-6.705005,-1.299833,-2.316573,9.032488,9.744590,9.766545], dtype = "float64")#candidate|2490|(36,)|const|float64
var_2491 = relay.var("var_2491", dtype = "uint16", shape = (280,))#candidate|2491|(280,)|var|uint16
const_2492 = relay.const([[-4,-4,-7,5,-3,6,-10,-6,1,2,9,4,-8,4,-7,-3,-5,8,-9,-7,5,8,8,-8,3,2,4,1,5,1,-2,-4,3,-10,-7,5,-10,1,-8,-5,-9,-1,3,2,-7,-3,-9,-5,-9,3,2,1,-2,10,-1,10,-3,10,3,7,7,7,5,8,-9,-3,10,10,4,3,6,5,2,-7,-9,5,2,-4,5,4,-3,-2,-9,-7,4,-10,3,10,-3,2,-1,10,8,4,-5,9,5,3,6,1,-1,-2,8,-2,1,3,-1,-7,8,-4,8,-1,5,-9,5,2,-10,-4,6,-9,2,-9,6,1,5,-5,1,8,-3,6,6,5,2,-4,7,-5,3,9,-10,-3,8,-10,5,4,6,7,-9,7,4,-2,-3,8,-1,-7,-9,-5,-8,7,-4,3,-2,1,-5,-5,-2,-9,-3,2,6,-6,10,6,-8,-5,-6,4,1,9,8,4,-10,4,10,9,5,-2,9,-5,3,-3,10,-6,7,-6,1,2,3,-7,1,-10,3,1,2,-3,6,3,-5,7,-4,6,3,7,3,-10,1,-3,5,-8,-2,3,7,5,3,-4,5,4,-8,-5,-6,7,8,-2,6,10,-1,5,9,1,-2,-10,-5,-4,-5,5,-5,-9,-4,3,-10,-7,8,-2,4,10,10,-2,6,9,-4,-5,1,-9,4,7,9,-9,-8,5,-6,-7,-6,-3,-4,6,-9,8,-6,4,-10,-7,7,-5,9,-8,-6,-5,-5,-7,-1,8,5,-9,-2,2,-6,-1,7,7,-8,2,9,6,-6,-2,7,8,-7,-2,3,-2,-5,1,1,-7,-10,-2,-8,2,3,-2,7,2,-10,2,-10,-2,7,6,-1,8,-4,2,-3,6,10,6,-10,1,5,-3,8,-10,1,5,-9,-3,5,4,2,4,10,9,-10,-9,-4,10,10,-10,-7,2,10,-8,-3,-3,-4,6,6,-3,-6,1,-7,-3,-4,9,-8,7,10,-2,-8,7,9,6,-1,-4,-1,6,-10,4,-3,-3,-6,8,-6,9,5,-7,-1,2,2,-8,4,9,-4,6,-6,8,-1,-7,9,2,4,-10,2,5,-9,5,7,-5,-8,8,-2,-7,-5,8,10,7,9,9,9,-7,8,-10,-7,6,8,9,-2,-2,3,-8,2,-9,1,4,3,-8,5,-4,7,-8,-5,4,5,4,-8,3,10,-10,-1,2,-8,-2,10,-7,-7,-1,-4,-2,1,-9,10,8,5,2,-6,9,-5,-9,7,2,-1,-8,8,-3,8,9,-3,10,4,-5,8,-6,-3,10,1,5,4,4,-3,-2,-9,3,-5,2,-4,-2,1,7,-3,3,8,-5,-1,-4,-5,7,5,-8,2,-4,6,-3,5,10,-5,-3,3,5,6,8,6,-7,-9,3,-4,-10,-4,9,10,-7,-4,-10,-8,-1,-4,8,-6,3,2,7,-5,-8,1,-8,7,-8,6,8,-4,-10,7,10,-5,-1,3,4,-6,-8,-10,-7,-4,9,-4,-5,5,-7,-5,6,-2,-8,-6,2,5,-8,-6,5,2,9,-1,4,-10,-6,10,7,-2,8,7,7,-9,10,-2,5,-7,1,9,-3,8,7,3,3,-9,3,-8,2,7,-5,7,2,4,-3,9,-3,-5,-7,4,-4,-1,-1,-7,-8,-6,-3,1,-8,-9,8,-5,6,-1,8,5,10,-1,6,-5,4,9,6,-5,7,-3,5,-5,-8,6,-4,8,-8,7,8,-2,5,10,-1,6,-10,-2,7,-5,-8,10,3,-7,8,-9,-8,-7,-10,6,3,-9,3,5,1,-6,1,10,-6,7,1,-10,-6,-1,7,10,-1,10,-10,-3,-5,9,-5,-1,6,-4,-3,5,5,-6,5,-10,-4,-10,7,7,-2,-9,-5,-7,8,9,10,-9,-2,-5,10,5,6,-8,9,-5,2,-8,-4,-2,-10,4,-5,-3,9,-7,-3,-2,-10,-4,-8,1,-4,-8,6,1,-1,4,-7,4,-4,4,5,-8,8,3,-2,-5,3,-5,3,5,-10,-1,-5,-4,8,-8,-5,8,-10,-9,-5,-9,8,-9,9,-7,2,-7,-5,-8,8,-7,-4,-6,8,-7,10,3,-1,2,-6,-10,-9,5,-5,-8,-9,-7,10,7,1,-10,1,10,6,3,-1,10,9,3,-10,-10,5,-2,-1,10,-3,2,6,8,-1,3,8,-3,3,-3,-6,2,8,-4,-10,-10,7,-9,-3,-4,-9,-8,4,-4,-7,10,9,5,-3,-10,-5,6,-2,4,1,2,9,-9,-3,-8,1,4,-7,1,7,-2,2,4,-4,-1,-8,-7,5,10,2,-8,7,4,10,5,-9,-10,7,-4,2,-6,-10,-9,-10,5,-6,-4,5,-8,-5,2,10,-4,-6,5,-6,10,5,-3,10,-8,10,-1,2,-2,10,1,-6,4,5,-9,2,1,1,-4,-3,-7,-4,10,6,5,5,-6,2,2,1,10,-3,3,-6,-6,9,2,2,1,3,5,-3,1,-3,5,-8,-1,8,6,-1,3,-6,5,-6,-9,4,8,-7,5,4,7,-6,5,-10,-10,-5,-3,7,-10,-6,-1,-5,10,-10,5,6,7,8,-8,3,1,10,-9,-2,9,2,-10,10,10,-4,3,-6,-2,2,-3,9,-5,10,5,4,1,5,-4,3,5,8,-7,-8,-9,10,-7,7,-7,5,10,7,7,5,9,3,5,-1,8,-3,2,-8,-2,1,4,3,-7,-7,4,-6,-2,-6,2,1,-1,-6,10,3,1,-3,-2,-2,7,-3,-5,-6,10,6,-1,2,3,-4,4,-5,1,-3,-4,-2,-6,4,6,8,9,-7,-1,2,-9,-7,4,-7,9,8,2,-6,8,10,7,-1,-2,-1,-9,4,-9,-8,-2,8,4,-7,-9,-7,-3,3,4,10,-2,6,-2,-7,3,4,2,-7,9,3,8,-6,-8,3,-1,-8,2,4,6,8,1,-5,5,7,7,-3,1,-6,-8,-1,-1,-4,2,-10,-1,10,-10,5,6,-1,-4,-9,-6,6,-5,-3,-5,-1,6,9,-8,9,1,-5,-8,3,-1,-8,9,-10,-2,-1,1,6,-3,-5,4,-9,2,6,-10,-1,-3,-9,3,-9,2,4,3,-1,6,7,3,-7,-2,4,-1,-5,2,-9,3,1,-9,9,4,-8,9,10,-5,-9,-9,-9,6,5,7,-6,-1,6,-2,3,8,-8,-9,10,-7,-1,2,5,5,7,-5,4,7,-7,6,9,-3,2,-7,-6,-3,-9,8,-2,-5,6,-1,-7,10,-9,5,-4,-5,10,1,6,-4,1,-10,-2,-2,-4,-9,-3,-6,9,10,-8,10,-1,-6,6,-2,10,10,9,-2,-6,6,2,-2,1,-4,1,9,-6,-8,4,1,-4,-6,6,-7,-1,-4,7,3,9,9,3,9,4,6,-9,-10,10,5,-5,8,7,6,7,-2,-9,6,10,5,-5,9,-8,7,4,3,6,5,5,-9,-3,1,-3,-5,-6,-4,9,-5,4,-6,5,10,-3,7,6,-4,-9,10,4,5,-6,-1,4,-4,9,7,-9,7,1,4,2,-8,-3,-2,-6,8,-6,8,4,-8,-2,-7,3,-5,-8,4,4,-10,2,7,9,-1,2,-4,-1,-1,7,-4,-2,7,-7,-9,-4,-2,-10,-6,2,-3,7,3,8,-3,-2,7,7,3,4,-8,10,5,-7,-1,8,-5,9,-7,4,2,-8,-1,3,-10,5,-5,8,-6,-3,-5,-9,8,-10,5,-4,1,9,8,5,1,7,-6,-8,-1,-1,3,-9,-8,-5,-7,3,2,2,-4,-9,-9,-10,3,-9,-10,3,10,4,4,-4,-10,-9,-9,-6,9,9,-4,-5,7,-3,4,-10,-9,4,-6,4,-7,10,-5,-10,-4,4,-8,-6,5,-3,9,-5,8,4,10,-9,3,5,-10,4,-4,3,-9,6,-10,5,4,10,1,-5,-1,10,-8,4,9,-1,6,4,2,-1,1,-4,8,-5,5,2,8,10,6,-3,1,6,7,7,10,-6,4,5,5,10,2,7,-3,-6,-2,2,3,3,9,-3,-7,-1,-10,-4,-6,4,6,10,10,-6,6,-6,-7,-1,10,-7,-5,-8,5,-2,6,-3,-9,2,8,2,6,-3,8,1,-1,4,7,3,-6,4,-2,6,9,-1,-6,1,4,6,1,9,-8,-10,-7,-6,9,-4,-9,4,-8,5,9,-7,1,4,-3,-5,-8,-5,-9,9,-4,-1,-5,9,10,-7,-9,4,10,-3,3,-5,5,7,2,4,-8,9,1,-7,1,4,10,1,5,4,-5,10,-8,6,2,-8,-8,-6,-4,-2,6,-4,-1,6,-10,-6,9,5,-5,-9,-10,9,-3,-6,9,9,-1,2,9,-10,10,2,-3,9,7,-5,7,6,3,7,10,-7,-1,7,-9,-7,-4,-2,-7,5,1,10,7,5,9,-2,-8,-2,-8,-8,-7,-9,5,9,2,-3,-7,-8,10,6,7,-8,5,-5,10,-1,8,7,-9,5,-2,4,-3,4,6,-5,-6,-10,-7,-5,8,-4,-5,-2,-9,8,5,-1,-4,4,-4,5,-3,4,-9,7,-4,6,3,-8,2,6,-7,8,1,-3,2,-9,-4,7,2,3,-4,-9,-6,1,-2,7,-3,3,8,1,6,5,2,1,5,-2,-2,9,-8,8,-7,-1,2,4,-10,10,-6,-5,-8,-4,2,-3,9,-2,2,6,7,-2,1,-6,3,-8,10,7,10,10,-9,6,-7,-2,-10,-10,8,-5,8,-4,9,9,-5,-9,10,-7,-6,-5,-5,2,7,-4,6,6,3,6,-1,-3,-5,-1,6,4,-5,3,-7,-5,8,1,-9,9,-6,3,-2,-4,-3,-2,5,8,-6,-9,-7,9,-4,-1,-7,6,-7,-1,-7,8,9,8,-7,-5,-7,-5,-1,-2,-7,7,-5,-9,1,-3,-4,10,-2,-9,-5,1,-9,8,1,4,-5,1,-5,4,10,-8,-10,-10,-7,9,-3,5,7,1,-5,7,7,10,8,-10,1,5,-6,-2,-3,-6,3,10,9,9,8,2,4,9,-5,-2,-7,-8,3,-6,2,5,-7,7,-6,-10,10,10,-3,6,6,-4,7,5,-1,8,-7,1,6,2,4,-4,3,8,3,-3,6,-3,1,-4,-1,8,-3,-5,-8,-1,-6,-7,-9,4,1,-10,-7,1,-2,-10,7,-2,10,-1,4,-1,7,1,4,-9,-5,1,3,-9,7,10,1,6,1,10,-9,8,-10,5,4,-9,4,-2,4,-4,3,6,-7,-5,-8,-4,7,-5,10,-1,4,5,9,-7,-1,5,4,-9,-4,9,-1,-10,-6,-5,5,-5,3,-6,-7,9,-3,-1,-6,10,-5,3,-4,4,8,-10,-5,-9,-5,5,8,-10,-8,10,1,5,8,4,1,-6,9,-1,1,5,4,7,-1,3,-10,-5,-2,9,-8,-4,2,9,3,8,-7,9,-2,-5,3,-4,10,4,-2,2,7,-1,5,2,10,-4,-6,10,1,-3,-3,7,-8,5,-5,2,-4,-3,-2,7,-9,-1,-5,-3,6,1,4,-3,1,4,7,-2,-8,-8,-1,4,-7,5,4,8,-3,-9,7,1,10,-7,-3,7,-3,-4,3,6,-1,-2,6,-4,7,8,-5,-3,8,3,-9,3,-7,-10,-4,-8,7,9,10,-4,7,4,-3,-7,6,-10,-10,1,-1,6,7,-8,8,8,1,8,4,-9,6,7,8,1,2,7,-4,7,-9,-6,4,-6,7,-2,3,-7,-1,-4,-2,9,8,-7,9,6,3,-6,7,2,5,7,7,-8,8,7,7,-8,-2,-9,-3,10,8,-10,7,1,6,-1,-1,1,-10,-3,-4,4,-6,-4,8,2,9,3,4,9,9,4,8,-1,-2,3,-3,-2,10,7,-10,-3,3,-7,9,10,6,10,-7,-10,5,-7,-2,9,-4,9,-9,5,10,10,5,-9,-4,-3,-10,-4,-8,-5,-9,-2,3,9,6,4,5,7,-8,3,3,-4,10,-8,-6,-9,-9,10,-2,4,4,-6,-5,-8,-7,-4,-6,-5,-4,-5,8,-7,-2,-9,-7,-4,2,-7,3,10,6,-2,2,-9,10,9,7,-5,3,5,8,1,7,8,5,10,4,4,-7,2,-8,-7,7,5,-9,-9,8,-8,-10,-5,-6,4,6,6,4,5,9,6,6,-5,2,2,6,4,-6,-8,-7,4,4,-9,10,-10,-5,-2,-10,6,2,1,-7,1,8,-10,6,8,-4,6,-10,2,3,-8,2,4,-3,-2,-1,-8,4,4,1,-10,7,-8,2,-4,-5,-7,-8,1,-7,-4,5,9,-9,1,-3,5,-5,-8,-5,2,-5,-7,2,-4,2,-9,-9,10,1,8,-2,-3,7,6,4,-4,-8,9,10,1,1,-10,-10,10,2,5,-2,1,-10,3,-4,2,-7,-2,-6,10,-6,-10,3,-8,-10,8,-1,-1,-3,-6,1,-9,-1,-7,7,-8,2,-9,-8,9,-10,-9,-4,-2,5,6,-6,-6,9,5,3,-8,1,-7,4,8,10,5,-10,-3,-4,2,-5,10,2,-9,-9,9,6,-3,-3,-6,-2,1,9,8,-4,-7,9,-2,-3,9,9,3,7,8,1,-4,-7,3,-8,1,-1,10,4,-4,-4,8,-10,-9,-1,6,-2,-2,-7,5,8,-9,6,1,-3,6,8,1,9,7,-8,9,-7,-9,8,2,-3,6,-10,7,4,1,1,3,5,-7,5,2,-9,-6,8,6,9,-9,1,-4,-3,-8,-10,-2,1,5,9,9,2,-6,3,2,-4,-3,-10,9,-4,8,7,7,1,-7,-3,8,-2,-6,8,9,10,6,-10,3,-1,-8,-3,10,8,4,-4,7,-1,-2,-4,3,-4,-5,-4,-10,1,7,4,-6,5,-6,-4,-4,7,-6,-9,-4,-7,-9,9,-10,-7,2,6,-4,10,9,-2,-1,-3,1,-5,4,5,-3,-5,3,-1,3,-5,-6,8,8,-2,-2,-7,4,-9,-4,-6,-9,9,2,6,-5,4,-5,1,-6,-4,6,1,-3,-2,5,3,6,-5,-2,-6,4,-2,-4,-4,-6,7,10,-3,8,-10,-5,6,-5,-2,4,7,7,6,-2,2,-9,-1,-8,-3,-4,-1,4,-10,8,7,7,-1,3,6,10,-7,-8,9,7,-2,5,-7,3,-9,9,-5,1,-1,-5,-4,-6,3,9,9,4,-6,7,9,3,10,-5,8,-1,10,7,-1,5,6,6,2,7,10,-1,3,-8,-6,10,-8,-3,8,-4,-3,-3,-3,-2,-10,2,4,-10,7,-2,2,7,4,10,-9,1,1,1,-2,8,-4,3,-4,-5,-2,4,-10,3,10,-5,6,-1,7,-3,-4,10,-1,-8,-5,-6,1,-10,2,2,-5,-2,-3,1,4,-1,-5,8,4,-3,-8,-6,10,7,-9,5,-8,-8,10,2,-3,4,-2,6,-6,-6,7,-3,-10,-10,-1,-5,-1,-1,2,9,-4,3,-3,5,7,6,-7,-10,9,-8,-4,1,-5,10,-8,3,10,-10,-7,6,8,8,1,2,10,2,2,1,10,5,8,9,-5,5,-6,8,5,7,5,-7,7,9,7,-7,1,2,-1,1,2,10,9,9,-3,9,6,-5,7,2,-5,-8,10,-6,-5,-7,-5,6,-4,-7,3,-6,-3,-10,6,4,-1,-8,6,-2,-2,-7,-5,-8,-10,-7,-10]], dtype = "uint8")#candidate|2492|(1, 2925)|const|uint8
call_2489 = relay.TupleGetItem(func_1292_call(relay.reshape(const_2490.astype('float64'), [3, 12, 1]), relay.reshape(var_2491.astype('uint16'), [280,]), relay.reshape(const_2492.astype('uint8'), [2925,]), ), 6)
call_2493 = relay.TupleGetItem(func_1296_call(relay.reshape(const_2490.astype('float64'), [3, 12, 1]), relay.reshape(var_2491.astype('uint16'), [280,]), relay.reshape(const_2492.astype('uint8'), [2925,]), ), 6)
func_354_call = mod.get_global_var('func_354')
func_358_call = mutated_mod.get_global_var('func_358')
const_2499 = relay.const(8, dtype = "int64")#candidate|2499|()|const|int64
var_2500 = relay.var("var_2500", dtype = "int64", shape = (1183,))#candidate|2500|(1183,)|var|int64
call_2498 = relay.TupleGetItem(func_354_call(relay.reshape(const_2499.astype('int64'), []), relay.reshape(var_2500.astype('int64'), [7, 13, 13]), relay.reshape(var_2491.astype('uint16'), [280,]), ), 1)
call_2501 = relay.TupleGetItem(func_358_call(relay.reshape(const_2499.astype('int64'), []), relay.reshape(var_2500.astype('int64'), [7, 13, 13]), relay.reshape(var_2491.astype('uint16'), [280,]), ), 1)
bop_2506 = relay.right_shift(const_2492.astype('int8'), const_2499.astype('int8')) # shape=(1, 2925)
output = relay.Tuple([call_2475,call_2489,const_2490,var_2491,call_2498,var_2500,bop_2506,])
output2 = relay.Tuple([call_2476,call_2493,const_2490,var_2491,call_2501,var_2500,bop_2506,])
func_2512 = relay.Function([var_2491,var_2500,], output)
mod['func_2512'] = func_2512
mod = relay.transform.InferType()(mod)
mutated_mod['func_2512'] = func_2512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mutated_mod.get_global_var('func_2512')
var_2514 = relay.var("var_2514", dtype = "uint16", shape = (280,))#candidate|2514|(280,)|var|uint16
var_2515 = relay.var("var_2515", dtype = "int64", shape = (1183,))#candidate|2515|(1183,)|var|int64
call_2513 = func_2512_call(var_2514,var_2515,)
output = call_2513
func_2516 = relay.Function([var_2514,var_2515,], output)
mutated_mod['func_2516'] = func_2516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2262_call = mod.get_global_var('func_2262')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_2592 = relay.TupleGetItem(func_2262_call(), 0)
call_2593 = relay.TupleGetItem(func_2264_call(), 0)
func_1699_call = mod.get_global_var('func_1699')
func_1702_call = mutated_mod.get_global_var('func_1702')
var_2598 = relay.var("var_2598", dtype = "float32", shape = (308, 1))#candidate|2598|(308, 1)|var|float32
call_2597 = relay.TupleGetItem(func_1699_call(relay.reshape(var_2598.astype('float32'), [11, 4, 7])), 0)
call_2599 = relay.TupleGetItem(func_1702_call(relay.reshape(var_2598.astype('float32'), [11, 4, 7])), 0)
output = relay.Tuple([call_2592,call_2597,var_2598,])
output2 = relay.Tuple([call_2593,call_2599,var_2598,])
func_2602 = relay.Function([var_2598,], output)
mod['func_2602'] = func_2602
mod = relay.transform.InferType()(mod)
var_2603 = relay.var("var_2603", dtype = "float32", shape = (308, 1))#candidate|2603|(308, 1)|var|float32
output = func_2602(var_2603)
func_2604 = relay.Function([var_2603], output)
mutated_mod['func_2604'] = func_2604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1742_call = mod.get_global_var('func_1742')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_2609 = relay.TupleGetItem(func_1742_call(), 2)
call_2610 = relay.TupleGetItem(func_1744_call(), 2)
output = relay.Tuple([call_2609,])
output2 = relay.Tuple([call_2610,])
func_2611 = relay.Function([], output)
mod['func_2611'] = func_2611
mod = relay.transform.InferType()(mod)
mutated_mod['func_2611'] = func_2611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2611_call = mutated_mod.get_global_var('func_2611')
call_2612 = func_2611_call()
output = call_2612
func_2613 = relay.Function([], output)
mutated_mod['func_2613'] = func_2613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_2649 = relay.TupleGetItem(func_1632_call(), 0)
call_2650 = relay.TupleGetItem(func_1633_call(), 0)
var_2651 = relay.var("var_2651", dtype = "float32", shape = (11, 4, 7))#candidate|2651|(11, 4, 7)|var|float32
bop_2652 = relay.bitwise_and(call_2649.astype('uint8'), relay.reshape(var_2651.astype('uint8'), relay.shape_of(call_2649))) # shape=(11, 4, 7)
bop_2655 = relay.bitwise_and(call_2650.astype('uint8'), relay.reshape(var_2651.astype('uint8'), relay.shape_of(call_2650))) # shape=(11, 4, 7)
func_1936_call = mod.get_global_var('func_1936')
func_1948_call = mutated_mod.get_global_var('func_1948')
const_2658 = relay.const([9,3,-9,-3,-4,8,1,-10,-1,-10,-9,-8,-1,3,-7,-6,6,6,-2,4,5,-6,8,-5,-1,3,7,-8,8,6,-2,4,2,3,10,-2,9,-3,-3,6,-5,-3,10,-1,-3,-8,7,-2,1,-3,-5,7,-2,-3,-1,7,7,8,-3,8,8,-10,-7,6,-10,-10,-5,-8,-9,9,9,-8,10,-4,7,-9,-7,1,-1,-1,-5,5,9,-4,6,10,1,-2,4,-4,-7,7,1,-9,5,3,-2,-10,2,9,1,-5,-7,-5,-2,-3,1,-6,-10,-3,6,4,4,9,2,-8,-9,-5,-10,7,-9,-3,-2,1,4,6,-1,6,-8,3,-4,1,4,10,-6,5,7,4,-5,-1,10,-6,10,8,10,-6,-4,10,4,-9,-8,6,2,-7,6,5,7,-8,-7,5,-10,4,9,-2,-3,-5,-5,6,-10,4,3,5,5,7,2,9,-4,-7,-6,-7,-10,-10,3,4,-1,1,-10,-3,10,6,3,-5,6,-9,-1,-1,-1,7,1,7,-10,7,7,-4,10,-10,-5,10,-6,-6,-7,7,-10,-2,-4,2,-1,5,-8,4,8,3,-8,-7,-3,-9,-9,-10,1,-9,-5,10,-1,4,3,-7,4,4,-4,6,3,-10,4,-3,-4,-9,-5,-2,3,6,-6,8,-5,-1,5,-6,3,-1,6,1,6,8,8,-8,8,8,6,-3,8,2,1,2,-6,10,-8,-1,-2,8,8,2,9,-1,6,8,8,-9,-7,-5,-3,4,-8,6,3,2,9,9,-6,4,6,7,-9,-5,5,-9,6,2,8,6,3,5,1,-1,-6,-10,5,8,-2,-2,4,-9,-3,-4,10,-2,-7,-6,-5,-7,2,-5,5,-2,-8,-7,-6,-1,-7,9,7,10,-2,-6,3,-8,-3,1,6,-8,-10,5,9,-4,-4,-6,8,-7,-2,5,-8,-8,4,10,7,-2,-1,2,4,-8,10,-9,10,7,9,-5,5,-8,7,8,-6,-10,9,8,-9,-10,-10,9,7,2,-10,-4,4,-3,-10,4,3,-2,9,6,6,-9,6,-6,4,10,-9,-10,-6,4,5,-1,-4,-3,-1,-1,6,3,7,-7,-1,6,9,1,-8,1,-2,4,-5,1,5,-3,1,4,-9,-1,-8,-10,-1,-4,5,2,8,-7,2,-9,1,1,1,-2,-6,1,-7,3,-2,-9,-2,6,7,-1,1,-10,-3,4,6,-4,-8,8,-6,5,8,4,-5,8,-4,-2,10,-7,3,-6,-7,1,5,-3,10,8,-2,-8,3,-8,8,1,-2,-10,10,-1,-8,4,-2,6,-5,-2,9,3,-9,-10,-2,2,1,-6,9,2,2,1,-3,9,-3,6,-2,-7,-3,-5,-10,-7,-10,6,2,7,3,1,-6,5,-9,3,-3,2,7,-9,8,-10,10,-10,-1,10,6,10,-10,-1,-10,-2,-5,9,6,9,-7,-4,4,-1,2,8,1,-10,-7,-1,7,1,10,4,-9,9,1,-3,7,9,-5,9,-7,6,2,-10,-1,-3,-3,6,-9,10,-8,4,-6,7,9,7,5,-9,-1,7,2,-4,6,-8,2,-4,10,-6,-8,10,-6,-3,-10,-7,-1,-4,4,-9,7,3,5,10,5,4,10,1,10,-9,6,3,2,-2,7,-7,9,6,9,-1,-3,-8,-10,-2,-4,-3,9,-8,5,-9,3,9,-8,-10,-10,-3,-8,7,-1,10,-10,-6,9,1,-5,-8,-8,2,9,-7,3,-3,1,10,-1,-9,-3,3,8,8,6,-2,1,2,-6,-1,9,1,-6,-5,-3,-1,7,10,7,9,-4,-8,4,6,-1,10,-3,-1,2,-9,8,3,1,3,3,-1,-2,3,1,8,8,-1,7,-1,9,5,-9,5,2,-10,-7,-4,-2,-6,6,-4,-10,-7,-6,-7], dtype = "int64")#candidate|2658|(728,)|const|int64
const_2659 = relay.const(-1.541108, dtype = "float64")#candidate|2659|()|const|float64
const_2660 = relay.const([-5.081782,6.440671,6.910836,-8.049136,-7.171205,4.263234,-6.039745,-5.704595,-4.275319,3.518918,2.466220,3.814895,7.138359,-8.256968,8.960661,3.255634,7.996492,-3.864772,-7.108411,-3.456664,-3.050663,1.631115,5.699550,6.965194,9.125229,-0.128415,3.829177,-9.264930,-7.770164,3.687717,7.704942,6.455734,7.021940,-2.145022,2.702830,8.071026,-4.336030,-5.527834,-0.819765,9.019157,3.257912,-4.556357,6.505881,7.839470,4.974256,4.369930,7.986589,0.798281,-1.746867,3.420410,-7.169453,-4.875436,8.925124,-7.486743,-7.663380,-0.632556,6.858910,-5.156172,7.673336,-6.227671,-8.506756,9.065035,8.912450,7.428748,-2.919594,2.556015,5.531980,7.808428,-0.068523,-3.010572,3.640152,-6.953654,4.620621,-5.596386,-7.486986,0.181053,-2.654743,0.522495,8.351324,-9.541893,8.074986,-2.785890,4.471748,2.541507,4.185079,-9.866529,-3.358191,2.578908,-9.410433,-7.228607,5.970448,4.459723,8.811497,1.893117,8.980886,-4.614964,4.730188,7.319851,4.898981,-4.726463,-6.528548,6.723670,-3.477367,-2.595004,-7.846630,7.776540,-1.947446,-6.745949,5.637022,-3.163560,8.503331,0.892212,5.413974,3.609365,-3.554627,1.060616,-6.760644,2.002089,-7.210645,0.134650,9.336484,-4.910551,-6.941076,5.927668,-2.278274,-3.388967,-8.998681,-0.138429,3.872043,-4.028962,0.578043,-6.041262,5.782100,-1.464628,-8.393729,-9.242267,3.429106,3.801050,0.056234,9.906040,0.625327,6.741749,-3.156165,3.366282,9.763681,6.764098,-3.137246,7.718742,7.209054,9.374685,6.049902,4.353743,-6.396395,-3.756578,5.891915,3.745734,-0.571050,5.395487,-4.418792,-0.420637,-2.038536,-8.947235,3.678181,-7.436641,-9.866756,-9.519160,-0.429014,-1.377180,2.267746,-0.459123,-4.232397,8.030749,0.242976,1.585720,0.496482,7.860112,5.078684,-9.109372,5.120675,-4.246792,-0.451351,-3.749610,-7.937701,0.214250,6.163511,5.742029,2.246823,-9.215613,3.752249,-2.417895,8.235486,-3.252481,-9.761363,-2.284258,-7.134831,2.712985,5.373005,5.028669,-1.855755,9.200849,-2.572887,1.469155,2.946382,-3.756124,-5.154036,-5.627975,4.375250,-0.719533,4.026653,1.393774,4.843184,9.524693,-6.730668,8.574799,5.775460,4.362929,8.415911,-1.071975,-1.710427,5.634138,4.995536,1.321133,-5.300853,-0.960129,-7.162102,2.082342,-3.098849,-5.754727,7.813576,2.742032,4.535782,1.277654,-3.860456,1.058952,-8.901898,7.038909,-3.594407,-6.907544,-7.400829,1.909761,7.641245,0.418004,8.948187,-3.045079,4.759973,7.617106,-8.439856,6.026076,-3.110729,-5.614266,9.280952,2.588870], dtype = "float32")#candidate|2660|(252,)|const|float32
var_2661 = relay.var("var_2661", dtype = "int64", shape = (91, 13))#candidate|2661|(91, 13)|var|int64
const_2662 = relay.const([4,-6,5,3,-3,8,-8,-3,2,9,-1,8,6,-8,-5,5,-9,6,-5,5,4,7,10,3,7,2,4,-9,2,-1,2,-8,-6,-5,3,-3,5,9,8,-7,-3,-5,7,-5,3,5,1,6,-8,-2,-3,8,-5,-3,-8,-9,7,9,-10,-4,2,8,-5,-5,-7,5,-2,-6,-9,-9,7,-9,-4,10,-5,-4,-4,-2,-9,1,4,4,9,2,-8,7,10,4,6,-7,6,8,6,-10,-7,-10,7,8,3,5,10,1,-8,4,-8,-5,-2,6,-4,-2,-7,3,-6,1,-8,5,8,10,10,4,-2,-2,-1,-4,-7,8,-1,-8,-10,8,-7,10,8,5,-1,-8,5,1,10,-3,-6,-9,-1,-5,9,-3,-6,-2,-10,-4,4,-7,-2,9,6,9,4,-8,-6,-6,-6,-1,-1,-9,-10,3,5,-6,-8,8,-6,5,-4,5,-6,7,1,4,-1,-2,-6,-8,6,-7,-7,-8,2,3,8,6,-8,-6,2,-10,5,-5,-8,1,7,8,-2,6,-2,10,6,4,10,2,3,5,3,-8,-3,5,-8,-5,-9,-4,2,1,-9,-4,8,-9,10,-9,-3,6,-10,7,3,-8,-3,-3,4,4,2,2,-6,1,4,10,8,3,-6,6,4,-2,-6,-3,1,-6,7,-1,9,-8,-3,-8,6,-1,-4,4,2,-7,10,-3,-7,-4,-6,-9,8,-8,8,3,9,-8,2,-3,7,5], dtype = "uint16")#candidate|2662|(280,)|const|uint16
const_2663 = relay.const([-2.222876,-1.944022,4.096783,6.791761,6.756040,-5.984310,5.031517,1.218281,8.474036,9.201437,-4.813469,-0.641544,-3.642837,-3.174366,2.980646,0.474155,3.613424,1.680848,-9.768916,-8.759843,2.957407,6.654695,-3.789241,-7.303506,9.983217,-3.121282,-0.944071,7.758523,3.356570,-8.548080,3.469175,-8.914003,5.603937,7.581107,-7.884906,8.658551], dtype = "float64")#candidate|2663|(36,)|const|float64
const_2664 = relay.const([1,-9,-7,6,-8,-3,3,6,-4,2,-9,6,-1,-1,5,6,-8,-7,-9,8,-3,10,1,-3,4,-1,-4,4,2,-2,9,-4,-10,3,-3,1,-6,-2,-8,9,4,-5,-1,-4,6,1,-4,4,8,-7,8,7,-10,10,7,10,-1,10,3,4,-1,-5,-2,3,6,-10,-8,10,-9,-6,10,-8,10,-5,-3,2,-6,9,6,9,-1,-8,-8,-9,-1,-1,-2,3,8,-4,-9,-5,3,-6,-5,5,-3,-7,3,8,-2,6,10,3,-9,9,5,-6,7,9,4,9,9,8,3,-6,5,-8,-1,-2,-10,-10,-2,-3,-6,-10,8,-10,7,-9,-6,-7,6,7,-8,2,10,3,8,-1,-10,-7,-2,3,8,4,-8,-4,-8,-4,10,6,-7,3,7,-2,-7,-5,-9,-10,2,-1,-7,-5,-6,1,6,-7,8,-10,4,-10,-4,-1,3,10,-7,6,-3,-9,1,-6,-1,1,5,-2,7,1,7,4,5,-7,-2,8,-5,8,-1,2,9,9,7,2,-5,5,5,6,-3,4,-6,-3,-1,7,-7,-2,-4,-10,-4,7,7,1,-1,-4,10,10,-10,8,-5,-3,-6,9,-6,5,1,-7,-3,-10,7,-1,-4,2,-7,5,-7,-4,-3,-5,10,-9,1,1,8,2,-7,-10,-7,5,7,6,10,9,1,-2,-3,3,-9,-1,8,-2,-8,6,-7,9,-2,-7,5,4,9,10,-9,9,-9,-4,-6,2,9,9,-8,9,5,10,2,-9,-4,-5,2,-10,4,8,2,-4,-5,-8,-3,-2,-5,-10,10,9,6,6,8,9,-4,2,6,-7,-8,3,-4,-2,9,9,1,3,2,7,5,-3,-4,5,10,-10,-8,2,8,-4,-3,-6,1,-2,-9,2,-5,-3,10,9,-1,-8,2,5,-1,-8,-4,-9,-4,-7,-1,6,-5,-7,8,-5,-6,2,-3,9,7,-10,-4,5,3,-2,2,10,-9,-2,-4,-10,10,-8,10,-8,-7,-8,-1,-10,5,-9,-1,4,-8,1,-1,-10,-4,5,6,-10,6,-3,-3,3,4,-6,-1,-7,7,10,-8,3,9,-3,-3,-9,3,8,-4,5,-1,4,-3,2,8,10,-2,-5,10,7,3,2,7,-3,1,10,-10,5,-5,3,-8,-9,-5,3,-6,-9,-8,6,-1,6,-8,-3,3,2,-4,3,-8,-4,9,-6,-8,6,6,-1,5,-10,-4,-1,-2,4,8,7,2,-6,-9,-7,-7,-4,9,1,-3,-6,3,-5,-10,10,6,1,9,10,10,-4,2,-2,-3,2,-4,-4,-6,4,8,2,-3,4,2,9,-1,1,-3,2,-5,-4,5,-8,7,-8,7,-10,5,-2,6,-1,4,-10,-4,-5,-1,8,6,-8,9,7,6,-6,-1,-9,10,4,9,-3,8,-4,6,4,9,7,10,3,1,-8,-8,9,-5,3,9,-9,-3,-6,4,-3,4,10,-3,-9,-4,9,1,1,-3,4,-2,10,5,-6,-10,1,-8,7,7,8,-4,-5,-6,-3,-3,-4,-9,10,-2,4,-3,5,9,5,-1,-7,-1,-10,-9,10,1,6,-10,-5,-1,4,5,7,5,-7,-8,-9,-7,8,5,7,-3,5,7,6,10,-4,-3,-8,7,-3,10,-4,5,2,-1,6,-1,-7,-3,-8,5,8,7,6,-1,-6,3,7,-3,5,-5,-10,-2,-7,-2,-9,-9,4,-3,7,-9,7,5,9,-1,4,7,-6,-10,5,-8,-6,-9,2,-3,8,-3,6,-8,-6,1,-7,-3,-7,-6,3,-5,10,3,10,10,-10,4,1,-2,1,6,-4,-2,1,5,3,-5,8,4,4,7,-9,1,-2,-6,8,4,-2,-5,6,7,2,2,-9,-5,4,-8,-2,10,2,7,-9,-4,-7,4,-10,5,-4,-9,5,10,5,-2,-7,-1,10,10,10,10,4,-3,8,4,4,7,-9,-1,-6,-3,7,3,3,9,-9,3,5,-10,3,-5,9,-6,-2,3,2,-1,10,-6,-9,-8,-4,-6,8,-3,9,-8,1,-5,3,-9,3,-3,5,-10,4,5,-1,-10,6,-10,9,-3,1,3,7,-8,3,-5,-1,-3,3,5,-10,2,8,10,7,-8,-3,-4,-5,3,6,-6,-1,3,10,7,-5,-5,1,8,9,10,-1,4,-9,-3,5,1,10,-1,2,-10,8,-7,9,9,-5,3,5,9,-4,-6,-4,6,-1,-4,-4,-9,8,-3,3,-6,-3,2,6,-10,6,9,5,3,2,-8,-10,1,2,6,6,-4,10,-6,1,-7,6,-6,1,8,7,-10,-4,6,2,3,-3,-8,-5,7,2,3,-10,-8,8,-4,1,-3,-4,-1,10,-8,-3,6,-1,-3,9,-1,-7,-1,3,2,-1,7,6,4,3,1,-8,-3,-3,4,-4,-2,1,6,1,8,-4,7,-4,-8,-5,-5,7,4,8,-4,10,-3,-9,5,-8,-2,-7,-4,2,-1,4,-1,-6,3,-2,6,2,5,10,-1,-2,-3,-4,1,3,-4,-8,8,-8,7,7,-2,-3,-10,6,3,4,8,-7,5,-2,6,2,5,-4,-1,-8,-2,9,-5,-3,4,6,-7,-2,-2,-9,-6,4,-2,6,1,-6,6,-3,2,-1,5,-10,-10,-5,7,-1,-5,-6,3,-10,-5,-9,2,6,-10,-2,-4,-7,5,7,8,-6,-4,1,4,4,-6,4,5,-3,5,-9,-8,-3,2,8,9,2,6,-1,-3,-2,7,10,-4,-6,8,9,-6,2,4,6,2,5,1,10,2,-6,6,1,-7,-10,-6,5,-3,10,5,-9,5,-6,-1,-2,-8,1,2,-5,-3,-8,-6,-1,-7,4,-6,-10,-8,-7,5,-3,-6,9,8,-9,-9,-8,-9,3,9,-2,2,-5,-10,-1,-2,10,-1,-7,2,-8,6,-7,-6,-3,-10,1,8,-4,10,7,-2,-1,-3,9,-8,-8,6,9,6,8,-8,-9,7,-7,1,-9,1,5,10,-1,5,-3,5,-5,-6,8,-4,-2,-2,-7,5,7,8,9,-6,-6,-10,-1,3,-7,-9,-2,-1,1,5,8,6,5,-7,-9,7,-3,-6,-1,10,-5,2,-1,4,-8,-2,1,2,-9,10,-2,-5,3,1,10,3,-2,5,-8,7,-1,4,6,-6,7,-5,5,5,-3,4,-2,1,2,9,-6,-9,5,9,-1,8,-4,-8,3,7,-4,9,7,-9,-7,-10,7,10,-5,5,5,-4,6,-8,-7,-7,5,6,8,-5,-6,-8,6,-6,8,-5,-5,-1,-2,2,-3,10,-4,4,-4,7,-3,2,4,10,-9,6,-5,5,-6,-7,-3,-9,-3,-3,1,6,4,3,6,-1,-8,9,3,-9,8,-10,-4,1,3,2,-3,-7,-6,8,-2,7,3,-3,9,-7,-9,1,9,9,-8,-5,-3,10,3,-3,7,4,7,8,1,-4,-4,4,-9,-7,-7,-7,-5,10,-7,4,3,1,7,-8,7,-9,-9,6,7,4,-6,-2,10,-10,5,8,-3,-7,-10,-9,9,10,2,-5,-7,-10,-9,-5,-4,-7,-10,6,6,6,-10,-5,-4,6,-10,4,7,-10,6,-9,-4,-9,1,-10,3,-7,2,2,6,3,-9,3,10,-6,3,-7,2,-1,-3,2,-6,9,-10,7,10,-1,-6,-7,-2,-3,8,9,-7,-3,-1,6,-1,-7,-7,8,-6,-10,-5,-9,10,9,-3,8,-9,10,-5,9,-3,-8,3,-10,4,1,7,-6,3,6,6,-4,6,-6,10,8,4,-4,1,3,-5,5,-4,2,-6,1,-4,-10,-9,-3,2,2,7,-2,-1,-2,-9,8,-7,3,9,-7,1,5,-4,10,-10,-3,-8,5,-1,-6,3,-6,-6,-6,-4,-10,-2,6,-5,-5,9,-4,-2,8,6,-4,10,9,-10,3,-10,9,-9,-10,-3,3,-1,-1,-6,8,5,-8,3,-10,-4,7,5,-6,10,1,10,-5,9,-8,7,6,10,-6,3,6,-7,3,-8,6,-6,-3,-1,7,-6,-6,1,-6,5,-3,-6,-8,-3,-6,-10,3,1,2,6,-3,-6,-7,8,9,-3,-4,5,-3,2,1,2,-10,2,5,3,10,7,-10,9,10,4,-3,7,7,-5,-3,-4,2,-5,2,4,-1,9,6,1,-2,-2,-3,-8,8,1,-2,2,-1,-10,-9,6,5,-1,5,-7,-8,9,7,4,-3,-7,-1,9,-10,-6,-3,-6,2,-9,9,2,-6,1,-10,-9,9,8,-8,2,5,-4,-4,9,10,-1,-6,8,-5,5,1,10,1,10,6,5,1,4,-2,9,10,10,-4,6,-5,-7,-7,6,9,-9,-9,-8,6,4,-4,-9,-5,-8,7,-8,-7,1,-6,-1,-5,9,5,-4,9,8,-1,8,5,-4,-2,-5,1,-2,-2,-1,-3,1,-10,-10,3,2,6,1,-6,6,-9,-6,6,7,-10,7,9,-3,4,-9,5,2,-3,-5,-10,-8,1,-9,-9,6,-5,5,2,-6,-3,-3,6,10,-10,8,-3,7,8,10,4,-9,9,-6,1,-7,-5,-3,-8,10,-5,6,-5,-1,-2,-2,-6,-5,6,8,-1,4,-5,-9,-7,1,-5,1,3,-3,-4,9,-10,7,-6,-5,-9,-7,3,9,2,1,8,-9,3,-4,-1,-7,7,-6,8,-4,-8,1,-6,1,-10,-7,-4,7,-10,-4,-4,-9,6,6,7,-3,10,8,4,-3,-2,3,9,-5,3,-8,-4,-9,-6,-6,-6,10,5,-1,-7,-5,7,9,2,-4,5,1,3,-10,5,-2,9,7,9,-4,4,-7,9,-8,-10,-5,6,-4,4,-8,4,-7,1,6,2,8,9,-1,-1,-9,-3,8,8,8,8,10,5,6,3,-8,1,-3,1,-1,2,5,-4,-5,-5,-6,-9,6,6,-2,5,6,-5,-8,-2,1,7,-9,7,5,7,6,8,1,-5,4,4,5,8,8,-2,-4,-2,-2,-9,2,6,3,9,9,9,-3,-5,4,4,1,-8,-7,-10,-3,5,4,-1,-7,-4,-6,4,-8,10,10,4,9,8,4,4,6,3,3,10,-6,-10,9,-2,1,-9,-5,4,-4,-2,2,-8,-7,10,-8,-2,5,7,-4,-1,2,-7,2,2,6,6,2,-6,-6,-9,-7,9,10,5,8,10,5,-8,3,-3,-4,6,-5,-4,-9,7,3,9,5,-9,10,-2,9,10,-10,10,3,3,-10,-1,10,-6,-4,-8,9,-2,7,1,-6,9,-5,-3,4,-6,-2,3,5,-7,-6,-7,-2,-3,-5,-8,-9,-8,-5,3,-6,4,-6,-10,-10,-9,3,1,-7,8,-1,4,3,-4,-4,8,8,7,-10,-6,-5,-7,2,-8,4,-2,2,5,-7,-4,10,10,3,-3,-4,5,3,-10,10,4,3,9,2,-1,-6,2,6,-3,9,3,-4,-7,-8,4,4,-2,-3,-2,-6,6,7,-8,-1,-3,-7,-8,-3,-10,9,-3,-3,9,7,-3,-4,4,8,-4,3,1,-4,-2,1,9,7,4,6,-8,-7,-5,9,-2,-3,9,-4,5,9,-4,-1,-2,-7,-8,2,-8,-6,-9,4,5,-8,3,-5,7,-6,-4,-5,5,7,-7,-9,9,9,2,9,-1,2,-8,-2,8,-7,-5,3,4,-5,-10,-5,-2,6,10,-3,-2,-6,-1,5,-8,-4,-5,-5,8,2,-4,8,5,-4,-9,5,2,-4,-10,2,1,1,6,9,-5,3,-9,-9,-5,9,-10,9,-6,4,-2,-3,6,-1,1,-6,10,-8,-10,-5,-10,3,9,-1,-5,-8,-5,9,7,2,7,-4,9,8,-9,-6,-7,8,-3,10,5,-4,-1,10,3,5,1,-9,-1,10,1,-10,7,6,-6,7,-6,-10,3,6,5,6,-1,8,3,6,4,-4,-2,10,-9,-9,-7,4,10,-6,3,1,-6,-8,7,-2,-9,-3,-9,1,1,4,1,-7,-10,-6,-4,7,-5,8,-10,-4,-9,4,-9,7,-4,-9,-1,-6,9,3,8,-3,6,5,-4,-9,-6,-10,-5,-7,9,6,2,10,3,-7,7,1,3,-1,5,-9,-10,-7,7,-6,10,6,-3,5,2,-6,-4,-2,5,6,-5,2,-8,-2,3,-1,1,6,6,1,-5,-6,-4,-8,4,-10,2,6,-8,-5,8,5,5,-7,-3,8,-5,-9,-5,-9,-4,1,8,-6,-6,9,-8,5,-8,-6,-1,10,-1,5,9,-8,-3,-9,-6,9,-5,-6,-5,-8,-3,3,-9,10,-6,-9,-10,-8,-7,4,-1,5,-1,8,-4,-10,-9,1,-8,1,7,-8,8,-10,4,-8,6,10,-6,5,5,7,10,3,10,-3,5,-3,-9,9,6,-6,-1,-10,-5,7,10,-3,3,-10,1,1,5,10,-7,-7,8,-5,-10,-8,-10,4,-10,-2,-2,-7,6,-2,1,4,2,-3,5,-9,-3,-9,-1,-6,-9,-5,3,-5,-1,-9,-8,10,-4,-10,3,3,6,2,2,-8,8,-1,7,-9,4,1,-1,-4,6,-2,-3,4,7,-7,-3,2,-2,2,1,-8,-7,7,-1,-3,-4,7,-9,7,6,7,-10,-1,-1,2,4,5,10,-9,2,10,-8,3,8,5,1,5,10,2,1,-3,3,-6,1,-5,-9,9,2,5,10,-3,-2,4,6,-3,-1,2,4,8,7,-8,-6,4,-9,-7,-10,1,3,-4,-3,-6,1,10,-9,-9,-10,3,-4,-6,-7,-3,7,7,-1,-7,-7,-1,-4,-4,-7,-9,9,-7,-10,-7,7,-2,-4,-2,-1,1,3,-6,1,2,-10,9,5,-4,6,-2,1,-5,4,-2,-8,10,-5,8,4,-7,3,6,9,-4,5,-10,-1,-3,-4,-7,10,-4,4,4,-4,-4,5,8,4,-3,-10,-5,-9,6,-5,-8,10,1,-3,-2,4,-7,-8,6,-9,-8,1,-9,-2,-6,8,2,-5,4,6,9,3,-10,1,4,-5,8,-6,10,6,4,9,3,-9,-4,-4,6,8,-10,-1,10,5,-6,7,-10,2,-6,-2,-7,-6,5,-5,-7,8,-4,10,-7,-2,-7,-6,3,-2,1,1,-4,-10,-9,1,-9,-3,-8,-9,-9,7,-3,6,-3,8,-2,-1,-6,-5,-9,10,5,-3,8,5,4,-7,7,4,10,3,8,8,6,-10,-2,-4,-6,8,-10,3,-7,10,2,1,3,5,7,-7,1,-9,-8,7,-10,7,-2,-4,1,-10,-6,-6,-6,-4,6,-7,1,-9,-8,4,-3,-8,3,3,-3,-6,7,-2,5,-5,7,10,-7,6,5,-3,-1,5,-2,8,3,-6,8,-3,-2,-5,-10,7,-4,-3,3,1,-9,-9,-9,6,-3,-2,8,3,4,1,5,-1,10,-1,-2,-8,1,1,4,-1,8,5,1,-8,-10,-10,6,5,9,-9,-8,-3,-4,-10,10,3,-7,5,-10,2,3,-4,-5,-7,3,-5,-4,-2,3,-5,3,2,-10,-7,-2,-8,-3,6,-1,2,10,7,-8,-10,-2,3,-7,-5,-1,-7,1,10,10,-4,8,7,7,-1,4,5,8,-3,-2,2,-3,8,4,10,3,-5,1,-10,5,-3,-3,-6,6,-8,10,-4,6,-6,10,-6,-1,-8,2,-1,1,7,10,-7,-5,-7,-2,7,-2,2,-3,7,-1,6,-4,2,9,-1,5,9,2,6,-6,-4,9,2,-6,6], dtype = "uint8")#candidate|2664|(2925,)|const|uint8
call_2657 = relay.TupleGetItem(func_1936_call(relay.reshape(const_2658.astype('int64'), [14, 13, 4]), relay.reshape(const_2658.astype('int64'), [14, 13, 4]), relay.reshape(const_2659.astype('float64'), []), relay.reshape(const_2660.astype('float32'), [252, 1]), relay.reshape(const_2658.astype('float64'), [14, 13, 4]), relay.reshape(var_2661.astype('int64'), [1183,]), relay.reshape(const_2662.astype('uint16'), [280,]), relay.reshape(const_2658.astype('float64'), [14, 13, 4]), relay.reshape(const_2663.astype('float64'), [36,]), relay.reshape(const_2664.astype('uint8'), [2925,]), ), 1)
call_2665 = relay.TupleGetItem(func_1948_call(relay.reshape(const_2658.astype('int64'), [14, 13, 4]), relay.reshape(const_2658.astype('int64'), [14, 13, 4]), relay.reshape(const_2659.astype('float64'), []), relay.reshape(const_2660.astype('float32'), [252, 1]), relay.reshape(const_2658.astype('float64'), [14, 13, 4]), relay.reshape(var_2661.astype('int64'), [1183,]), relay.reshape(const_2662.astype('uint16'), [280,]), relay.reshape(const_2658.astype('float64'), [14, 13, 4]), relay.reshape(const_2663.astype('float64'), [36,]), relay.reshape(const_2664.astype('uint8'), [2925,]), ), 1)
uop_2668 = relay.erf(call_2649.astype('float64')) # shape=(11, 4, 7)
uop_2670 = relay.erf(call_2650.astype('float64')) # shape=(11, 4, 7)
output = relay.Tuple([bop_2652,call_2657,const_2658,const_2659,const_2660,var_2661,const_2662,const_2663,const_2664,uop_2668,])
output2 = relay.Tuple([bop_2655,call_2665,const_2658,const_2659,const_2660,var_2661,const_2662,const_2663,const_2664,uop_2670,])
func_2674 = relay.Function([var_2651,var_2661,], output)
mod['func_2674'] = func_2674
mod = relay.transform.InferType()(mod)
mutated_mod['func_2674'] = func_2674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2674_call = mutated_mod.get_global_var('func_2674')
var_2676 = relay.var("var_2676", dtype = "float32", shape = (11, 4, 7))#candidate|2676|(11, 4, 7)|var|float32
var_2677 = relay.var("var_2677", dtype = "int64", shape = (91, 13))#candidate|2677|(91, 13)|var|int64
call_2675 = func_2674_call(var_2676,var_2677,)
output = call_2675
func_2678 = relay.Function([var_2676,var_2677,], output)
mutated_mod['func_2678'] = func_2678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_2680 = relay.TupleGetItem(func_1839_call(), 1)
call_2681 = relay.TupleGetItem(func_1841_call(), 1)
output = call_2680
output2 = call_2681
func_2700 = relay.Function([], output)
mod['func_2700'] = func_2700
mod = relay.transform.InferType()(mod)
output = func_2700()
func_2701 = relay.Function([], output)
mutated_mod['func_2701'] = func_2701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2425_call = mod.get_global_var('func_2425')
func_2426_call = mutated_mod.get_global_var('func_2426')
call_2734 = func_2425_call()
call_2735 = func_2425_call()
output = call_2734
output2 = call_2735
func_2745 = relay.Function([], output)
mod['func_2745'] = func_2745
mod = relay.transform.InferType()(mod)
mutated_mod['func_2745'] = func_2745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2745_call = mutated_mod.get_global_var('func_2745')
call_2746 = func_2745_call()
output = call_2746
func_2747 = relay.Function([], output)
mutated_mod['func_2747'] = func_2747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2700_call = mod.get_global_var('func_2700')
func_2701_call = mutated_mod.get_global_var('func_2701')
call_2750 = func_2700_call()
call_2751 = func_2700_call()
func_1409_call = mod.get_global_var('func_1409')
func_1413_call = mutated_mod.get_global_var('func_1413')
var_2755 = relay.var("var_2755", dtype = "int32", shape = (25, 9))#candidate|2755|(25, 9)|var|int32
var_2756 = relay.var("var_2756", dtype = "int32", shape = (1575,))#candidate|2756|(1575,)|var|int32
call_2754 = func_1409_call(relay.reshape(var_2755.astype('int32'), [1, 15, 15]), relay.reshape(var_2756.astype('int32'), [7, 15, 15]), )
call_2757 = func_1409_call(relay.reshape(var_2755.astype('int32'), [1, 15, 15]), relay.reshape(var_2756.astype('int32'), [7, 15, 15]), )
output = relay.Tuple([call_2750,call_2754,var_2755,var_2756,])
output2 = relay.Tuple([call_2751,call_2757,var_2755,var_2756,])
func_2758 = relay.Function([var_2755,var_2756,], output)
mod['func_2758'] = func_2758
mod = relay.transform.InferType()(mod)
mutated_mod['func_2758'] = func_2758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2758_call = mutated_mod.get_global_var('func_2758')
var_2760 = relay.var("var_2760", dtype = "int32", shape = (25, 9))#candidate|2760|(25, 9)|var|int32
var_2761 = relay.var("var_2761", dtype = "int32", shape = (1575,))#candidate|2761|(1575,)|var|int32
call_2759 = func_2758_call(var_2760,var_2761,)
output = call_2759
func_2762 = relay.Function([var_2760,var_2761,], output)
mutated_mod['func_2762'] = func_2762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1742_call = mod.get_global_var('func_1742')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_2778 = relay.TupleGetItem(func_1742_call(), 3)
call_2779 = relay.TupleGetItem(func_1744_call(), 3)
const_2788 = relay.const([[[-2.727527,3.809292,8.352424,-5.548272,-0.864075,1.989259,-5.027050],[-7.293938,-9.874151,-6.902011,9.339632,2.726897,-3.095323,0.421433],[-5.549475,-2.028105,6.225404,3.587496,-9.686678,0.708523,8.011520],[2.682929,6.495360,-1.235858,0.639981,-7.067964,-4.232012,-2.051382]],[[-3.506713,3.267531,-0.909811,4.112968,1.725134,-8.951394,6.925868],[5.139991,-4.710705,-6.883179,-3.848989,6.034938,5.500269,0.639837],[2.560940,-7.461627,3.667764,-0.551492,0.348352,9.068069,-8.050909],[-7.990734,8.942230,7.131567,8.125414,9.402096,-9.820365,2.789867]],[[9.568373,4.261054,-0.576926,-7.334388,8.919203,1.991556,-2.910392],[2.990310,-6.400303,-8.792046,1.675737,-7.058754,7.864927,0.474650],[-8.489359,-4.513179,0.564423,2.163435,9.625806,1.284180,-9.011319],[-2.514056,4.465936,-1.982145,6.121224,7.144733,-0.693205,2.397177]],[[-4.515270,5.790223,-6.213746,-4.149774,9.448851,3.936692,3.413491],[7.192474,-9.356395,-7.897669,5.242504,6.981030,-0.935511,-6.936242],[-7.237543,-8.241674,-2.109278,-5.864878,8.392398,-4.731212,-2.182025],[-0.562002,-0.079491,7.953255,4.115564,-0.366412,-0.228913,5.046895]],[[-0.234852,3.333088,-2.819102,3.372871,7.459186,7.718906,-9.852713],[0.548232,4.787129,-4.837242,5.670049,-0.640947,-0.689702,-0.238572],[0.332468,1.040280,3.056302,-1.432155,-7.985065,-7.040269,8.927167],[9.888818,1.872739,-6.311012,-5.310919,-3.590867,1.776199,-4.919458]],[[8.054012,-9.473093,-0.456611,-6.199674,7.966537,2.121470,4.093380],[0.349697,3.887383,-6.245761,-3.720130,-5.472830,-1.965773,-3.184891],[3.309100,3.200659,6.120030,1.570293,4.161750,9.905643,6.546884],[-9.102591,-4.079412,7.103364,-9.842641,-4.832243,4.022721,5.711755]],[[2.362688,6.965841,-2.260392,1.895602,-2.452574,-9.969834,2.747985],[-9.781277,-5.621715,4.738155,1.299753,1.697702,-1.574761,-4.907745],[-5.757450,3.409771,0.075935,-5.585753,2.676761,-1.924023,3.564225],[4.776147,-6.906587,1.257809,5.104973,-4.652069,2.829201,-5.138813]],[[0.501121,3.632681,6.496098,-4.911637,7.955470,-3.092152,-5.961195],[8.238123,5.011982,-3.531511,-3.079302,5.229494,-3.109125,-2.685827],[7.687276,-5.175411,8.462293,-8.499011,-7.528337,-9.940933,6.006432],[5.173674,5.262624,0.287900,4.751138,-9.650639,4.400764,3.993134]],[[9.111230,-6.686857,8.735105,-1.674503,-7.195737,2.653481,5.978118],[9.547847,-3.838005,-9.104675,2.715932,0.013642,-0.006473,-5.880283],[1.414909,2.003053,-4.351925,3.632809,-2.594063,-3.689752,-5.695967],[-8.470354,9.922323,-0.924336,-0.501179,4.051225,1.319717,-1.947189]],[[6.128055,6.095606,8.380000,3.245323,-9.014410,5.360017,-6.692223],[-6.789291,4.245780,-5.303605,-0.681380,-7.397049,-3.905387,-5.702688],[-3.390293,9.811774,0.904326,-8.336918,4.320878,-2.613859,-0.401008],[2.737389,-8.060205,7.347824,-6.490001,-1.755582,4.716165,4.681870]],[[1.343386,0.830020,-7.222232,4.551804,7.612400,-4.806220,8.140508],[4.969892,-8.639245,3.417751,-6.155658,-3.791662,-6.338423,1.920643],[-4.088409,4.002146,-3.844791,9.289181,8.155291,-2.740327,8.171166],[-1.239684,-0.950940,-6.179318,-6.216099,5.381812,6.980032,4.348746]]], dtype = "float32")#candidate|2788|(11, 4, 7)|const|float32
bop_2789 = relay.less_equal(call_2778.astype('bool'), relay.reshape(const_2788.astype('bool'), relay.shape_of(call_2778))) # shape=(11, 4, 7)
bop_2792 = relay.less_equal(call_2779.astype('bool'), relay.reshape(const_2788.astype('bool'), relay.shape_of(call_2779))) # shape=(11, 4, 7)
var_2802 = relay.var("var_2802", dtype = "float32", shape = (11, 4, 7))#candidate|2802|(11, 4, 7)|var|float32
bop_2803 = relay.less(call_2778.astype('bool'), relay.reshape(var_2802.astype('bool'), relay.shape_of(call_2778))) # shape=(11, 4, 7)
bop_2806 = relay.less(call_2779.astype('bool'), relay.reshape(var_2802.astype('bool'), relay.shape_of(call_2779))) # shape=(11, 4, 7)
uop_2809 = relay.asin(const_2788.astype('float32')) # shape=(11, 4, 7)
uop_2817 = relay.cosh(uop_2809.astype('float64')) # shape=(11, 4, 7)
func_2512_call = mod.get_global_var('func_2512')
func_2516_call = mutated_mod.get_global_var('func_2516')
var_2824 = relay.var("var_2824", dtype = "uint16", shape = (280,))#candidate|2824|(280,)|var|uint16
var_2825 = relay.var("var_2825", dtype = "int64", shape = (1183,))#candidate|2825|(1183,)|var|int64
call_2823 = relay.TupleGetItem(func_2512_call(relay.reshape(var_2824.astype('uint16'), [280,]), relay.reshape(var_2825.astype('int64'), [1183,]), ), 3)
call_2826 = relay.TupleGetItem(func_2516_call(relay.reshape(var_2824.astype('uint16'), [280,]), relay.reshape(var_2825.astype('int64'), [1183,]), ), 3)
output = relay.Tuple([bop_2789,bop_2803,uop_2817,call_2823,var_2824,var_2825,])
output2 = relay.Tuple([bop_2792,bop_2806,uop_2817,call_2826,var_2824,var_2825,])
func_2840 = relay.Function([var_2802,var_2824,var_2825,], output)
mod['func_2840'] = func_2840
mod = relay.transform.InferType()(mod)
mutated_mod['func_2840'] = func_2840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2840_call = mutated_mod.get_global_var('func_2840')
var_2842 = relay.var("var_2842", dtype = "float32", shape = (11, 4, 7))#candidate|2842|(11, 4, 7)|var|float32
var_2843 = relay.var("var_2843", dtype = "uint16", shape = (280,))#candidate|2843|(280,)|var|uint16
var_2844 = relay.var("var_2844", dtype = "int64", shape = (1183,))#candidate|2844|(1183,)|var|int64
call_2841 = func_2840_call(var_2842,var_2843,var_2844,)
output = call_2841
func_2845 = relay.Function([var_2842,var_2843,var_2844,], output)
mutated_mod['func_2845'] = func_2845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_2858 = relay.TupleGetItem(func_2027_call(), 0)
call_2859 = relay.TupleGetItem(func_2029_call(), 0)
output = call_2858
output2 = call_2859
func_2863 = relay.Function([], output)
mod['func_2863'] = func_2863
mod = relay.transform.InferType()(mod)
output = func_2863()
func_2864 = relay.Function([], output)
mutated_mod['func_2864'] = func_2864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_2880 = relay.TupleGetItem(func_1839_call(), 2)
call_2881 = relay.TupleGetItem(func_1841_call(), 2)
func_997_call = mod.get_global_var('func_997')
func_1000_call = mutated_mod.get_global_var('func_1000')
const_2891 = relay.const(3.564926, dtype = "float64")#candidate|2891|()|const|float64
const_2892 = relay.const([-9.411554,1.649839,-1.210051,8.793774,-2.526197,7.105368,-0.862505,8.344216,9.303911,-4.356586,2.741404,-7.336966,1.672543,-8.206472,6.892910,-0.421201,6.428219,-0.439989,6.090110,6.456550,-6.913495,-9.349417,-6.531882,3.671714,8.805848,4.490848,5.499381,3.569976,2.251377,6.321220,8.341314,7.418618,8.822271,5.777186,6.574203,-1.293513,5.804675,7.647540,-2.727824,2.301303,-8.544342,-5.840638,-3.442018,-7.242689,-7.755759,0.086827,-4.669926,-9.214896,-2.586702,-1.991140,-0.708240,8.191069,9.056803,6.072638,-9.802660,-5.692482,1.898552,-7.940256,-9.631674,-5.855548,-7.688114,4.312659,-1.755357,-5.609796,8.209238,-1.036707,5.514987,6.701774,-7.366225,3.068048,8.263318,-6.103225,-7.787633,-6.544830,3.858801,7.364597,-7.867858,-7.366828,3.819687,-6.005232,-3.965456,-5.867592,-0.043105,-1.660983,1.958067,5.200731,5.006408,0.785054,-9.142182,7.187209,-4.313527,7.591995,8.913900,0.215841,-0.288863,3.067865,2.706222,8.989895,7.474477,-5.666240,5.807329,5.199777,5.784559,-1.975438,-1.315896,-5.391936,5.534934,-7.193458,2.005842,8.686257,9.027407,-8.028599,-8.846759,-5.345892,-0.060613,-7.436479,3.786966,-7.494122,1.420334,-1.622501,-4.148053,-5.776233,2.385349,-9.362010,5.477016,-9.180362,-7.086620,4.864839,-5.434881,-0.854853,-5.766863,-9.231161,-1.763029,5.696834,-7.683019,-8.277751,-5.177675,-5.649398,3.398330,-3.608355,-5.915685,4.088007,-4.240763,4.051722,-4.855238,8.081860,8.976879,-8.784843,-5.707631,3.405459,-0.700238,-9.342209,-5.539624,-4.435765,5.111702,-5.296234,4.600908,1.298876,-7.254069,3.466529,-6.911907,-9.197442,-4.746400,-9.780445,-8.345404,0.431447,2.657609,7.854579,-6.153281,7.575929,-3.906758,3.087090,6.314841,5.296732,-9.255418,-6.211022,7.785740,-4.860106,-7.378573,8.101474,-8.366216,5.991024,-1.553251,5.236017,-4.768680,-0.215611,2.264003,-2.423526,-6.456462,-3.443837,-4.023293,-5.909768,4.318188,-7.522448,1.335780,-0.624907,-7.120493,2.285990,-8.745193,-1.801226,7.347758,-6.514416,-7.237967,3.033918,-0.660307,2.348327,-6.267857,8.037471,-9.192518,9.339331,5.015380,9.691896,6.756799,-3.859388,-7.508290,-5.194353,5.809596,-1.294526,-3.674801,4.158173,7.534031,4.893753,-8.623021,-7.659058,-2.209031,-9.244373,8.106532,-4.767418,-2.506274,5.028909,9.660292,-3.115883,-0.542658,-1.631367,-1.649070,0.268823,7.107862,3.673999,5.176336,-6.995801,-1.139388,5.343144,6.142561,-2.594313,-5.849927,-1.415041,-2.320451,9.197906,2.219853,9.043370,4.499524,7.777327], dtype = "float32")#candidate|2892|(252,)|const|float32
call_2890 = relay.TupleGetItem(func_997_call(relay.reshape(const_2891.astype('float64'), []), relay.reshape(const_2892.astype('float32'), [252, 1]), ), 1)
call_2893 = relay.TupleGetItem(func_1000_call(relay.reshape(const_2891.astype('float64'), []), relay.reshape(const_2892.astype('float32'), [252, 1]), ), 1)
output = relay.Tuple([call_2880,call_2890,const_2891,const_2892,])
output2 = relay.Tuple([call_2881,call_2893,const_2891,const_2892,])
func_2903 = relay.Function([], output)
mod['func_2903'] = func_2903
mod = relay.transform.InferType()(mod)
output = func_2903()
func_2904 = relay.Function([], output)
mutated_mod['func_2904'] = func_2904
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2905 = relay.const([[[2,8,3,-10,5],[-4,-5,4,-3,-7],[-5,-10,-4,-2,-1],[1,-6,-5,-2,4],[8,-6,9,3,3],[3,-2,4,7,-1],[2,-4,-2,-7,-3],[-10,1,5,8,-9]],[[9,-8,4,9,6],[2,3,-6,4,-7],[-6,-7,7,-6,2],[-5,-9,4,-4,7],[-4,-10,4,1,-1],[4,-7,4,-4,8],[-8,-7,-7,10,-5],[-1,-7,-3,7,2]],[[2,3,8,-5,8],[8,-6,2,-7,5],[1,-10,-7,3,9],[-9,-1,2,2,10],[1,-5,-5,2,-1],[-4,1,3,7,1],[9,-6,-4,10,6],[-5,9,5,9,4]],[[4,-2,-9,2,-1],[1,5,-10,6,3],[9,-10,-10,-2,2],[-10,-3,-1,9,10],[10,-2,9,-2,-2],[-8,4,1,4,-6],[-9,-5,1,5,-3],[2,6,-6,7,-1]],[[-4,-2,-8,-2,-6],[1,5,6,-1,-7],[-5,8,4,6,2],[10,6,-4,-7,-9],[5,8,5,7,6],[2,5,-3,-2,10],[-4,-1,4,-7,2],[-4,7,8,-8,7]],[[8,-5,9,-4,5],[-6,4,-3,3,-9],[-7,9,-7,-5,-1],[-8,4,-4,1,6],[1,9,9,6,-4],[-4,-8,-7,1,9],[-6,1,-2,5,-4],[-1,2,2,4,3]],[[3,-10,-2,5,1],[-5,2,-9,2,8],[-4,3,-1,-5,-3],[4,6,6,-1,1],[-8,10,-4,-4,2],[2,-3,10,-10,-8],[5,-8,7,1,6],[1,8,-3,8,-9]]], dtype = "int32")#candidate|2905|(7, 8, 5)|const|int32
const_2906 = relay.const([[[-2,-1,5,9,-4],[-5,9,3,7,8],[-2,-9,-2,-1,-10],[9,6,-10,-4,4],[9,5,7,9,-9],[-5,7,3,-4,10],[-5,-6,1,-4,3],[2,-7,10,-6,1]],[[-6,-6,2,-4,-2],[-10,5,10,2,-10],[-3,-8,1,8,7],[-1,-8,5,6,4],[-4,-7,-2,3,-2],[-10,-5,-7,6,-2],[-5,-5,-1,10,-10],[5,1,-10,-8,7]],[[-6,-5,7,7,-7],[8,5,-4,-6,2],[-3,9,-7,-8,-2],[7,4,-10,3,-4],[-8,4,-8,10,7],[9,8,-5,-6,2],[-10,7,10,-4,-5],[-5,3,-8,10,-2]],[[-9,6,-8,2,3],[-2,-2,4,-6,-5],[9,6,9,-10,2],[-5,-6,8,-1,-7],[-6,-5,8,2,-10],[-7,-7,10,10,9],[5,-5,-7,4,-5],[2,2,2,1,-5]],[[1,1,-8,-7,4],[-10,-2,-9,-10,-6],[-5,-8,10,-6,4],[-1,7,6,-4,4],[9,-4,-1,-9,-9],[5,5,-1,-3,-3],[2,5,-7,-5,-4],[-6,2,-5,6,-3]],[[-8,7,4,-8,6],[-6,-9,-8,-10,5],[1,-8,-3,8,-4],[2,-9,-7,8,-10],[9,5,-6,2,5],[1,-1,8,1,-5],[7,9,8,-1,-1],[3,8,8,10,-2]],[[-9,8,4,-8,-2],[-2,-10,-4,-4,7],[5,-7,-9,-9,-5],[5,-5,-4,10,6],[4,-10,-6,5,9],[-9,-5,9,9,6],[-8,6,3,-4,3],[-7,-5,-3,1,-5]]], dtype = "int32")#candidate|2906|(7, 8, 5)|const|int32
bop_2907 = relay.right_shift(const_2905.astype('int32'), relay.reshape(const_2906.astype('int32'), relay.shape_of(const_2905))) # shape=(7, 8, 5)
output = bop_2907
output2 = bop_2907
func_2916 = relay.Function([], output)
mod['func_2916'] = func_2916
mod = relay.transform.InferType()(mod)
output = func_2916()
func_2917 = relay.Function([], output)
mutated_mod['func_2917'] = func_2917
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2958 = relay.var("var_2958", dtype = "int64", shape = (16, 1, 1))#candidate|2958|(16, 1, 1)|var|int64
var_2959 = relay.var("var_2959", dtype = "int64", shape = (16, 5, 11))#candidate|2959|(16, 5, 11)|var|int64
bop_2960 = relay.less_equal(var_2958.astype('bool'), var_2959.astype('bool')) # shape=(16, 5, 11)
bop_2976 = relay.bitwise_or(var_2959.astype('uint16'), relay.reshape(bop_2960.astype('uint16'), relay.shape_of(var_2959))) # shape=(16, 5, 11)
bop_2979 = relay.not_equal(var_2958.astype('bool'), bop_2960.astype('bool')) # shape=(16, 5, 11)
output = relay.Tuple([bop_2976,bop_2979,])
output2 = relay.Tuple([bop_2976,bop_2979,])
func_2984 = relay.Function([var_2958,var_2959,], output)
mod['func_2984'] = func_2984
mod = relay.transform.InferType()(mod)
var_2985 = relay.var("var_2985", dtype = "int64", shape = (16, 1, 1))#candidate|2985|(16, 1, 1)|var|int64
var_2986 = relay.var("var_2986", dtype = "int64", shape = (16, 5, 11))#candidate|2986|(16, 5, 11)|var|int64
output = func_2984(var_2985,var_2986,)
func_2987 = relay.Function([var_2985,var_2986,], output)
mutated_mod['func_2987'] = func_2987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2611_call = mod.get_global_var('func_2611')
func_2613_call = mutated_mod.get_global_var('func_2613')
call_3019 = relay.TupleGetItem(func_2611_call(), 0)
call_3020 = relay.TupleGetItem(func_2613_call(), 0)
output = call_3019
output2 = call_3020
func_3021 = relay.Function([], output)
mod['func_3021'] = func_3021
mod = relay.transform.InferType()(mod)
output = func_3021()
func_3022 = relay.Function([], output)
mutated_mod['func_3022'] = func_3022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2916_call = mod.get_global_var('func_2916')
func_2917_call = mutated_mod.get_global_var('func_2917')
call_3039 = func_2916_call()
call_3040 = func_2916_call()
var_3041 = relay.var("var_3041", dtype = "int32", shape = (7, 8, 5))#candidate|3041|(7, 8, 5)|var|int32
bop_3042 = relay.logical_xor(call_3039.astype('uint64'), relay.reshape(var_3041.astype('uint64'), relay.shape_of(call_3039))) # shape=(7, 8, 5)
bop_3045 = relay.logical_xor(call_3040.astype('uint64'), relay.reshape(var_3041.astype('uint64'), relay.shape_of(call_3040))) # shape=(7, 8, 5)
var_3046 = relay.var("var_3046", dtype = "int32", shape = (7, 8, 5))#candidate|3046|(7, 8, 5)|var|int32
bop_3047 = relay.bitwise_or(call_3039.astype('uint16'), relay.reshape(var_3046.astype('uint16'), relay.shape_of(call_3039))) # shape=(7, 8, 5)
bop_3050 = relay.bitwise_or(call_3040.astype('uint16'), relay.reshape(var_3046.astype('uint16'), relay.shape_of(call_3040))) # shape=(7, 8, 5)
const_3052 = relay.const([[[2,7,7,4,6],[-1,-9,4,2,5],[5,3,3,7,-7],[1,-3,5,-10,5],[-3,5,-1,-5,4],[-5,1,8,10,-5],[-6,-8,-5,-9,6],[-3,10,10,-8,-4]],[[-6,-3,7,-9,9],[-5,2,-4,-6,10],[-8,-10,10,10,4],[10,3,7,5,6],[-1,8,4,-8,6],[-2,-2,3,-10,-10],[8,-6,-5,2,8],[3,9,-3,-3,3]],[[1,-2,-8,7,-9],[-4,-8,8,5,3],[-8,-3,8,-1,-8],[-8,2,4,-8,-7],[9,-4,4,-10,1],[-2,-2,7,-4,-10],[-5,-1,-2,-6,-7],[7,-6,3,-2,1]],[[-8,2,10,1,10],[-6,2,1,-4,2],[9,7,10,-5,3],[-4,9,-3,9,-4],[-5,-5,8,9,-2],[3,-2,-9,10,-5],[-2,-4,-6,1,-10],[4,5,-10,-5,5]],[[2,1,10,-6,-5],[-3,-9,7,3,1],[-5,9,-4,1,8],[9,7,5,1,8],[-4,1,8,-1,8],[-6,-8,-10,-2,4],[-8,1,2,-3,-9],[6,-3,-7,5,-6]],[[9,-5,-5,-1,-8],[10,-5,-1,8,9],[8,1,4,-2,7],[3,10,-4,3,-5],[-8,6,7,-10,5],[4,-7,-3,-4,-10],[-5,-8,-1,1,8],[6,2,-1,1,-3]],[[3,10,-4,-10,9],[1,7,10,-4,3],[-8,7,-2,8,10],[-10,9,-4,2,-3],[-8,-7,-4,2,-8],[1,5,-6,6,10],[5,2,9,-9,2],[2,-4,4,5,-7]]], dtype = "int32")#candidate|3052|(7, 8, 5)|const|int32
bop_3053 = relay.add(var_3041.astype('int8'), relay.reshape(const_3052.astype('int8'), relay.shape_of(var_3041))) # shape=(7, 8, 5)
output = relay.Tuple([bop_3042,bop_3047,bop_3053,])
output2 = relay.Tuple([bop_3045,bop_3050,bop_3053,])
func_3061 = relay.Function([var_3041,var_3046,], output)
mod['func_3061'] = func_3061
mod = relay.transform.InferType()(mod)
var_3062 = relay.var("var_3062", dtype = "int32", shape = (7, 8, 5))#candidate|3062|(7, 8, 5)|var|int32
var_3063 = relay.var("var_3063", dtype = "int32", shape = (7, 8, 5))#candidate|3063|(7, 8, 5)|var|int32
output = func_3061(var_3062,var_3063,)
func_3064 = relay.Function([var_3062,var_3063,], output)
mutated_mod['func_3064'] = func_3064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_3126 = relay.TupleGetItem(func_1839_call(), 0)
call_3127 = relay.TupleGetItem(func_1841_call(), 0)
output = relay.Tuple([call_3126,])
output2 = relay.Tuple([call_3127,])
func_3131 = relay.Function([], output)
mod['func_3131'] = func_3131
mod = relay.transform.InferType()(mod)
mutated_mod['func_3131'] = func_3131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3132 = func_3131_call()
output = call_3132
func_3133 = relay.Function([], output)
mutated_mod['func_3133'] = func_3133
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3144 = relay.var("var_3144", dtype = "float32", shape = (14, 8, 16))#candidate|3144|(14, 8, 16)|var|float32
uop_3145 = relay.acosh(var_3144.astype('float32')) # shape=(14, 8, 16)
output = uop_3145
output2 = uop_3145
func_3158 = relay.Function([var_3144,], output)
mod['func_3158'] = func_3158
mod = relay.transform.InferType()(mod)
mutated_mod['func_3158'] = func_3158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3159 = relay.var("var_3159", dtype = "float32", shape = (14, 8, 16))#candidate|3159|(14, 8, 16)|var|float32
func_3158_call = mutated_mod.get_global_var('func_3158')
call_3160 = func_3158_call(var_3159)
output = call_3160
func_3161 = relay.Function([var_3159], output)
mutated_mod['func_3161'] = func_3161
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3233 = relay.const([[[5.244705,-6.672928,-2.486310,-8.973867,8.988925,7.132133,-8.562035,-3.771012],[7.731292,-1.378539,8.209621,9.813656,-4.261419,5.972572,7.741543,5.573750],[-6.393879,6.427953,-1.363557,-0.627782,4.550459,-2.393109,-2.727778,4.887366],[-0.321090,4.818604,-4.952724,-6.471151,9.751477,6.062274,9.582744,-3.466209],[-9.342252,-1.723130,0.074481,-5.458072,4.261307,1.231110,-5.769550,5.759559],[-8.320942,-6.138980,-6.240339,-6.978761,-9.600661,-9.835036,-4.791072,3.725705],[-9.332164,-9.881875,3.378911,-3.799151,5.717786,-3.664850,-9.282830,-0.135734],[-5.749826,5.287429,-8.148800,-2.064652,-8.800778,-9.656292,9.669412,7.790472],[5.225381,-4.146364,4.152000,6.961177,-3.100982,-1.571020,-6.190825,0.213712],[9.226252,4.466928,-1.781957,-7.602740,-3.709815,-1.890450,4.257128,5.103638],[3.843260,6.773263,-8.097167,2.273819,-7.613888,1.013335,-2.726964,7.343516]],[[1.352005,3.597321,-3.544777,-5.376357,-7.340932,5.180660,4.948118,4.204682],[-7.291795,5.779595,4.503331,3.862770,-6.215829,-5.719799,3.429397,-3.472923],[-3.462783,2.368244,0.211835,8.536371,-1.405762,0.565094,4.160450,-4.040665],[5.468070,-4.260379,-5.187687,-6.734515,-8.001103,4.615558,-2.235517,6.189918],[-1.405738,-6.528643,-7.445025,4.654957,-5.216046,-6.311775,7.975154,0.356748],[-0.420195,-2.450773,8.893658,2.835815,9.372548,0.549344,-2.740308,5.634507],[8.548780,2.036597,2.145823,-0.669898,4.293103,-5.448069,9.813606,-3.485074],[9.976635,-5.420679,1.747710,8.462649,9.025786,0.241891,4.068008,-9.362338],[-5.766233,-6.082072,-5.181513,9.067468,-7.537290,2.456468,0.724240,4.519870],[-8.765632,8.845542,-2.002951,-6.719375,7.778519,2.904628,-7.670366,-7.360025],[5.485145,9.414430,4.589212,-0.191982,-0.422553,-3.168153,9.467173,-8.238413]],[[9.638819,1.890901,-2.542753,2.170605,1.855764,-4.966619,-2.948986,-3.508062],[-6.366088,-9.462816,-1.471977,2.852891,-8.497513,-7.462097,9.737639,6.143521],[-9.535980,-6.950058,-4.659768,8.303286,7.039963,-0.774840,-7.013543,1.402702],[-7.459759,-8.551633,-3.666406,5.303256,3.801435,-4.328310,-4.145099,-9.002437],[2.759161,-5.526061,-8.368664,1.173886,9.983386,-4.967783,8.609864,-5.634753],[5.419120,-3.582732,-5.196770,-1.717467,-6.463734,3.353966,-9.243757,8.169655],[-1.742442,9.948624,2.526526,-6.210304,-6.951158,-9.548630,2.172500,1.999427],[-9.014678,-0.304207,1.631328,-9.918615,-2.547026,7.584309,7.933646,-6.721515],[-8.796182,6.430829,-0.860822,-1.459493,-6.227451,-1.866059,-5.351121,-1.342936],[-3.526360,6.302628,1.554737,1.646974,8.458090,-7.290193,7.225930,5.986725],[-3.279124,-6.162759,-4.115906,-9.846620,2.517575,-0.756182,-9.219435,-5.973545]],[[-2.961997,4.010616,-9.777556,5.909229,1.764409,-0.716330,-3.681978,-6.086075],[-7.804244,7.407927,5.885554,6.858851,5.914405,-0.786233,-1.196152,-1.946955],[9.678535,-8.588441,-1.075643,9.257446,3.091252,-0.303383,2.165697,3.837455],[6.569173,8.984291,-0.540526,-2.416337,-8.389826,9.835361,9.321372,8.415318],[7.277999,-4.288737,4.359477,7.821170,-1.785471,-1.398319,-7.287973,4.009189],[3.724205,0.760949,-5.622422,6.594061,-1.267843,4.722018,-6.740019,-4.682621],[4.705486,7.454799,1.357178,4.778794,-8.422289,7.084101,1.317867,8.887981],[7.645529,-8.715276,-9.383316,1.061577,0.243040,-0.847419,3.205311,6.718653],[-6.185188,-2.143679,-6.509497,8.374518,7.032512,5.283412,3.113780,2.413089],[9.421115,-2.674600,6.115143,7.575287,0.288096,-5.975945,-8.830971,3.285730],[-5.574540,-6.907357,3.733376,-9.266867,0.835742,-2.964950,-9.986775,7.233841]],[[5.934258,4.289881,7.937180,9.429911,-3.719661,-2.820724,-2.414255,5.013696],[7.171887,6.916134,5.995812,3.943485,4.662139,-7.609159,-6.515954,-8.493523],[0.979449,-1.247462,-8.751979,7.389890,-6.995759,5.326600,9.224769,0.705373],[1.396627,-5.983528,-9.299457,7.729403,8.724190,2.062858,9.427795,5.328373],[0.552913,-1.649602,-0.127168,1.658955,0.501683,0.576612,1.483883,3.791619],[2.316599,-2.828318,6.134772,1.373517,3.267282,-4.808158,-6.126607,2.783813],[-5.684103,0.053776,-9.278347,4.662102,-9.183374,-3.656480,0.181006,-0.175681],[1.399595,1.480099,-2.739601,7.699529,5.374961,-3.949261,-3.166616,-6.707893],[1.559575,5.361965,-3.202245,8.798066,8.673700,-7.814424,7.074360,6.785476],[8.814141,-0.880877,8.957408,6.452059,4.724083,6.015005,-6.168814,-5.302655],[9.148450,1.751272,-8.305820,-5.464149,-5.545635,7.510421,5.601497,1.485770]],[[8.316886,-0.145770,1.052616,0.720060,-4.068362,-2.013169,-8.699703,-0.334581],[-5.860818,3.608475,3.696581,-2.999219,7.488558,8.391541,-9.455495,8.901658],[-4.260628,2.557695,-7.322110,0.997869,4.478498,9.038809,-3.802809,5.581970],[7.825791,-9.473398,2.479719,-9.233294,-2.173122,5.376957,-6.080129,-3.513022],[0.873268,3.150561,-6.784212,-9.173438,-4.465806,-8.158452,4.825129,-3.057965],[-4.478818,8.296435,8.788509,-2.627798,-1.185205,8.099254,7.934609,2.950482],[0.744334,-4.061064,0.564692,2.930946,-4.081254,9.455674,6.611314,-6.615578],[-2.265829,0.511010,7.833873,3.813710,-7.239700,1.223447,-9.530069,-3.520635],[0.426266,5.949521,7.008737,-4.843798,-4.245151,0.342550,3.425817,-9.429319],[-9.430428,-5.398399,4.178899,3.496420,-1.444755,2.154379,2.873322,-9.930227],[-0.758213,-6.859895,-8.956309,7.226736,-3.736106,-5.881480,-2.079006,7.112582]],[[5.084617,7.979630,8.556629,-9.230451,9.815999,-5.150581,8.412500,1.110087],[-5.066443,3.972578,-6.200365,-3.702921,7.963356,9.205347,7.808681,-4.719201],[-0.612078,2.964578,-8.357239,9.825246,-1.047810,5.958251,-9.227931,6.670081],[-5.848803,5.267347,-0.366955,6.493563,-4.102312,8.993174,5.517002,-9.856470],[9.409695,0.903611,8.180495,6.214325,-8.668472,8.015132,6.269873,7.674842],[7.231630,2.468068,-2.947167,-0.551382,6.254715,-4.946723,1.212461,-0.584557],[4.640543,6.118757,-4.714939,-4.853635,1.361280,4.306655,-5.054681,-6.262550],[4.319758,2.950654,-6.108132,-9.662393,-7.506966,-2.419932,-1.949120,-0.746220],[-0.135662,-1.504548,3.608376,2.243181,0.585136,9.159347,0.797882,3.419214],[9.942364,8.645177,-8.670156,3.670113,-5.256629,5.307732,-2.213119,-7.988540],[7.505582,6.802601,2.979115,3.444702,4.126057,4.284765,-5.037294,7.096119]],[[0.969277,6.629636,8.645956,-6.341592,-7.234433,-6.915020,-7.364213,6.359816],[0.552237,-8.165588,8.892023,2.165073,-1.798366,1.091027,-0.104626,7.430024],[6.814120,2.263195,2.357407,0.398612,6.969916,3.352060,-1.934440,5.346281],[1.915268,9.449529,0.584828,-3.245770,0.547778,-6.432234,-5.545238,3.885117],[-6.891821,-4.245496,5.879292,6.325926,3.786811,-3.165024,9.204810,-2.737415],[5.157481,4.463283,-9.294538,-6.957237,-6.237262,3.487573,-9.949565,-8.194249],[-6.380397,4.017622,-7.363534,-1.436093,6.292034,-8.903363,0.664516,3.636424],[-9.017813,5.004263,-3.034091,-7.190685,8.020347,-4.785833,-2.354112,-3.170865],[8.653672,-3.043749,7.571879,-2.481827,0.898298,1.484516,8.699348,6.517961],[-9.659675,-1.072825,8.018081,4.460580,1.756041,-9.861436,-4.670669,-5.508761],[-1.422803,-5.817512,6.807403,-1.249262,9.304929,0.848482,5.567719,-3.593424]],[[-1.995342,-6.584036,4.029682,-3.890028,7.982253,-6.094821,4.894440,-4.278984],[-2.873414,3.678347,2.168465,-8.627212,-0.479635,6.727252,1.081908,5.162262],[-9.466378,4.179920,9.068720,-5.227420,-7.933527,-0.550143,6.131717,-6.135361],[9.009971,-4.843677,9.443263,6.562376,-2.892824,3.382836,-1.860517,8.211656],[8.029892,-4.768026,-5.027174,5.398944,-8.060342,2.842977,-5.623276,4.638355],[0.005279,-4.505450,-4.562799,-6.325266,-7.678058,-2.811324,-9.966045,-5.760947],[-2.919512,-0.733846,3.760352,-2.047635,-5.603754,-8.309580,2.464896,-5.221732],[8.338962,5.187105,0.501651,-3.091609,-7.126218,-3.396123,1.949823,-9.577229],[-0.784345,-7.039564,-4.756473,5.679671,-9.073071,-3.477609,9.610675,2.821993],[5.027727,-1.135569,-3.286497,8.416678,-9.433919,-3.401030,-6.923630,9.840290],[1.453576,-1.125929,-4.990970,-0.413285,8.810572,-5.085619,-3.189165,8.583122]],[[3.773936,-5.967897,5.406123,-5.361043,6.020847,2.811260,7.361894,-1.293668],[-5.403203,-6.624025,-7.433737,-1.331115,0.332832,-2.281989,-9.411442,-1.172306],[-5.351705,1.096715,-9.708498,0.242433,-8.354696,8.881928,0.583955,7.385271],[-4.122897,3.001156,-5.860659,6.970426,-7.021696,9.400156,8.038995,-1.652950],[-2.050046,2.495681,6.151315,9.343628,7.641831,3.309253,-6.227584,9.571498],[6.121328,-6.552342,-8.012904,8.028151,2.123392,7.300157,-4.200848,-1.264912],[2.589172,3.394845,-9.790549,8.342271,1.545664,2.325820,3.049891,7.644063],[0.405827,-8.089514,8.493957,-3.708276,0.353725,9.681942,-6.929199,-1.065611],[-1.223604,-8.965569,-5.732401,-1.753440,8.679736,-7.763100,-9.544055,1.265166],[3.920153,4.799184,7.564147,5.142872,7.739452,4.251592,4.835625,-4.966484],[6.112357,-0.637647,-2.291093,-2.370872,-6.501799,-6.143747,-8.253135,-6.614602]],[[3.138317,-1.064342,-0.988312,6.425706,-6.258949,6.691877,1.000137,4.572812],[-5.812888,-5.740666,7.789936,-9.467873,6.749724,-7.921232,-3.012668,4.170225],[8.208343,6.438933,-6.425813,6.883324,9.476850,-4.998102,-9.415568,2.040603],[0.546129,0.552411,-7.343766,2.313622,-9.094057,9.873810,-9.817804,1.527534],[-2.068941,1.010849,2.233878,-6.566347,7.982144,5.064922,-0.345227,5.068077],[6.583393,-8.292149,-1.847899,7.523046,-8.618912,-6.825080,-1.603959,-8.516979],[-4.103015,8.746438,-6.247676,-5.293809,-6.899401,-7.739499,-2.354592,-2.106193],[-5.979268,-3.275716,-6.185486,-0.414490,-4.785410,-7.786911,-6.858148,-3.712262],[-3.473574,-8.357211,0.641015,1.132513,9.362288,-8.000498,2.381586,5.944499],[-3.741550,-5.742283,4.375073,3.833430,0.453108,-7.833926,-4.293191,-3.998058],[-8.415433,7.670136,5.128168,7.139002,-3.956571,1.015965,8.582399,-1.150865]],[[-1.586224,-9.581992,5.989461,0.033488,3.507902,-0.115138,-6.909365,5.660408],[5.226235,-6.119673,6.195550,2.128390,-1.473297,5.486701,1.739445,4.905358],[-8.679741,-6.985166,1.954837,4.597952,3.145336,-0.487243,-3.071108,0.193646],[-5.556468,0.508674,8.206499,-4.017747,0.307172,0.668405,7.384633,-7.116473],[0.781528,3.539647,-5.078592,8.934652,-3.873811,-3.736028,5.429747,-9.417440],[6.472526,3.222154,9.174168,-1.101652,3.653888,4.613156,-5.239218,4.462872],[-0.215800,-7.082416,1.171953,6.705281,4.476129,-7.298538,6.382320,8.236545],[-7.965026,8.550510,-2.383167,-4.410788,-8.319652,-6.508760,6.868728,-9.630942],[-4.674202,9.377082,-8.413653,4.483995,-3.566031,7.756191,-9.981630,-9.943515],[3.231944,-8.788882,-2.980341,-1.228610,4.813041,5.652418,-8.471207,-7.128746],[1.496649,-1.154355,-7.211939,0.248992,0.983057,-5.714032,9.404565,6.286363]],[[6.823520,-3.163667,-2.607664,-0.898364,8.821525,8.606490,5.097826,-1.793697],[7.329795,-8.942136,-8.695635,-3.992526,-2.610754,-7.646978,5.032631,4.385771],[4.029956,-2.738222,-9.483641,7.738186,8.256592,0.768168,8.696884,9.353797],[-1.824879,-8.344976,5.107157,-8.647428,-2.213984,-6.571879,-1.430154,-0.877205],[0.704836,-9.780523,0.627920,-2.471331,-7.879376,5.179603,1.123295,-8.785081],[-0.508978,1.980266,0.390529,-1.512414,-5.280850,2.256555,-0.851735,-0.097432],[4.621877,9.609099,9.582278,6.397602,3.956265,4.966758,5.872940,-0.563826],[-6.064834,0.130691,3.002492,6.177114,-2.682328,6.806453,-5.057247,1.422405],[-2.984352,-5.863346,-3.702573,7.505691,-1.576513,-8.710472,-8.924970,-7.830131],[-6.423476,-8.800002,0.535228,5.365687,-9.363704,-3.234425,2.459437,-0.968298],[-6.246716,0.241273,-5.652308,-6.989945,8.487888,-3.549699,3.336608,-3.582455]],[[2.716304,9.201062,7.370781,-4.864047,9.673588,-6.689489,-5.493989,-3.601816],[-8.319231,8.960917,-6.930549,8.911461,8.127330,2.657242,-5.419690,-0.201132],[-5.323517,-3.680160,7.798790,-9.494151,8.220239,1.950921,6.282332,-8.182836],[2.842814,2.551759,9.270831,9.201264,-2.217027,1.420218,-2.381182,-8.183281],[-7.987003,-5.922485,-3.078886,-1.291991,-0.785594,3.921797,-0.587612,8.550225],[-8.593533,9.580048,8.869293,-4.237252,-8.648309,6.584087,1.673196,2.996371],[-2.242099,0.457862,-1.275235,1.287479,4.407421,3.200937,-6.664276,7.956287],[1.380684,0.005052,8.029842,-0.257941,2.157846,2.309150,-2.082431,-3.754259],[-5.669255,1.119763,-0.540547,1.348681,7.045818,8.377706,3.236636,-0.131631],[3.424147,-7.693061,8.308299,-9.370210,-4.037286,-8.509208,7.259895,0.885665],[-8.547102,-1.826423,0.386910,8.822541,-9.353084,7.493920,2.109451,-7.474686]],[[6.526571,-8.732791,-7.618337,3.387756,-4.226476,1.811960,2.812773,2.898651],[1.022566,-0.477326,-2.826437,2.491101,-1.896153,-2.021500,1.821648,-0.335601],[5.864638,3.584029,-8.387338,-8.885841,-8.911854,-2.432913,7.663228,-8.853078],[3.471319,5.952355,-9.547010,6.562157,8.751895,-2.586670,-4.650194,4.305447],[8.728962,2.226618,-6.534584,-7.038559,1.634614,-8.236519,3.222204,2.576240],[5.914895,-1.870577,-3.836223,-6.765635,7.570452,-5.973237,4.957803,-5.188374],[-7.193046,-7.119209,5.514564,-6.121134,4.540315,4.935286,4.477792,-1.304332],[-6.790412,-6.546302,-0.978679,-4.314667,3.917022,9.368633,5.401433,-2.009039],[-2.781321,-9.807739,3.189639,-7.250820,5.142186,0.474041,6.190627,6.838357],[-0.138698,-3.769788,-3.503127,6.655066,8.154752,-6.472048,-3.169897,-8.700014],[-2.755056,-3.634775,0.863714,-3.684583,7.487173,1.749372,1.883133,-3.357965]]], dtype = "float32")#candidate|3233|(15, 11, 8)|const|float32
uop_3234 = relay.sqrt(const_3233.astype('float32')) # shape=(15, 11, 8)
output = uop_3234
output2 = uop_3234
func_3243 = relay.Function([], output)
mod['func_3243'] = func_3243
mod = relay.transform.InferType()(mod)
output = func_3243()
func_3244 = relay.Function([], output)
mutated_mod['func_3244'] = func_3244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_3280 = relay.TupleGetItem(func_2027_call(), 0)
call_3281 = relay.TupleGetItem(func_2029_call(), 0)
func_2187_call = mod.get_global_var('func_2187')
func_2190_call = mutated_mod.get_global_var('func_2190')
var_3289 = relay.var("var_3289", dtype = "int64", shape = ())#candidate|3289|()|var|int64
call_3288 = relay.TupleGetItem(func_2187_call(relay.reshape(var_3289.astype('int64'), [])), 5)
call_3290 = relay.TupleGetItem(func_2190_call(relay.reshape(var_3289.astype('int64'), [])), 5)
output = relay.Tuple([call_3280,call_3288,var_3289,])
output2 = relay.Tuple([call_3281,call_3290,var_3289,])
func_3291 = relay.Function([var_3289,], output)
mod['func_3291'] = func_3291
mod = relay.transform.InferType()(mod)
var_3292 = relay.var("var_3292", dtype = "int64", shape = ())#candidate|3292|()|var|int64
output = func_3291(var_3292)
func_3293 = relay.Function([var_3292], output)
mutated_mod['func_3293'] = func_3293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2864_call = mutated_mod.get_global_var('func_2864')
call_3297 = func_2863_call()
call_3298 = func_2863_call()
var_3303 = relay.var("var_3303", dtype = "float32", shape = (11, 4, 7))#candidate|3303|(11, 4, 7)|var|float32
bop_3304 = relay.logical_xor(call_3297.astype('uint16'), relay.reshape(var_3303.astype('uint16'), relay.shape_of(call_3297))) # shape=(11, 4, 7)
bop_3307 = relay.logical_xor(call_3298.astype('uint16'), relay.reshape(var_3303.astype('uint16'), relay.shape_of(call_3298))) # shape=(11, 4, 7)
output = relay.Tuple([bop_3304,])
output2 = relay.Tuple([bop_3307,])
func_3316 = relay.Function([var_3303,], output)
mod['func_3316'] = func_3316
mod = relay.transform.InferType()(mod)
var_3317 = relay.var("var_3317", dtype = "float32", shape = (11, 4, 7))#candidate|3317|(11, 4, 7)|var|float32
output = func_3316(var_3317)
func_3318 = relay.Function([var_3317], output)
mutated_mod['func_3318'] = func_3318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2903_call = mod.get_global_var('func_2903')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_3357 = relay.TupleGetItem(func_2903_call(), 2)
call_3358 = relay.TupleGetItem(func_2904_call(), 2)
var_3359 = relay.var("var_3359", dtype = "float64", shape = (12, 14, 14))#candidate|3359|(12, 14, 14)|var|float64
bop_3360 = relay.left_shift(call_3357.astype('int16'), var_3359.astype('int16')) # shape=(12, 14, 14)
bop_3363 = relay.left_shift(call_3358.astype('int16'), var_3359.astype('int16')) # shape=(12, 14, 14)
func_3158_call = mod.get_global_var('func_3158')
func_3161_call = mutated_mod.get_global_var('func_3161')
var_3365 = relay.var("var_3365", dtype = "float32", shape = (1792,))#candidate|3365|(1792,)|var|float32
call_3364 = func_3158_call(relay.reshape(var_3365.astype('float32'), [14, 8, 16]))
call_3366 = func_3158_call(relay.reshape(var_3365.astype('float32'), [14, 8, 16]))
output = relay.Tuple([bop_3360,call_3364,var_3365,])
output2 = relay.Tuple([bop_3363,call_3366,var_3365,])
func_3367 = relay.Function([var_3359,var_3365,], output)
mod['func_3367'] = func_3367
mod = relay.transform.InferType()(mod)
var_3368 = relay.var("var_3368", dtype = "float64", shape = (12, 14, 14))#candidate|3368|(12, 14, 14)|var|float64
var_3369 = relay.var("var_3369", dtype = "float32", shape = (1792,))#candidate|3369|(1792,)|var|float32
output = func_3367(var_3368,var_3369,)
func_3370 = relay.Function([var_3368,var_3369,], output)
mutated_mod['func_3370'] = func_3370
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3386 = relay.var("var_3386", dtype = "uint16", shape = (4, 13, 10))#candidate|3386|(4, 13, 10)|var|uint16
const_3387 = relay.const([[[-7,-8,-7,4,-1,4,-9,5,-9,-5],[6,4,-2,-5,-5,6,7,8,10,1],[9,9,8,-7,-4,10,8,4,-4,-2],[7,2,1,10,-2,-5,6,8,2,1],[-8,4,2,-7,-8,-9,8,-2,1,-2],[-3,-3,3,-3,9,-8,4,4,-1,-6],[9,-5,7,5,7,1,6,-9,9,1],[7,-4,1,-10,-8,-1,-2,-3,-2,-6],[-8,1,1,1,5,8,1,-4,10,3],[10,5,8,8,-6,3,1,8,-5,4],[2,1,-5,-4,-8,-5,2,-8,-7,2],[-3,9,-8,-8,7,2,-5,3,-7,5],[5,-4,1,7,10,-3,-4,-9,-3,-5]],[[8,-10,-10,2,-1,3,-8,-2,8,-9],[1,-3,8,9,-6,2,4,8,-6,-1],[1,2,4,-10,-5,3,3,-1,8,10],[6,10,3,-2,-10,7,-1,-3,-3,7],[2,-4,-6,5,4,-7,-7,-10,9,-1],[-7,10,-7,4,6,10,3,-2,-8,2],[2,4,-10,-2,-6,-6,3,-2,-1,-2],[10,-6,5,-2,6,-5,-5,10,3,2],[6,4,-8,-2,5,-7,-6,-5,-2,4],[-1,6,9,-9,9,2,1,-7,-4,-9],[2,1,-10,9,-3,10,1,10,-4,-2],[2,8,-4,4,3,7,9,5,6,1],[-8,-5,-1,-1,-8,7,9,-5,2,10]],[[-5,3,5,-3,-2,2,9,9,4,4],[2,-4,-9,-3,10,-8,-10,-9,9,-6],[10,2,-7,9,10,-5,-5,5,-10,8],[-4,5,7,9,-9,8,-4,1,1,5],[1,8,-1,-1,1,-10,-6,-9,2,3],[-2,3,1,-7,3,-8,6,-10,8,7],[-3,-6,-6,3,2,9,7,10,-7,-4],[1,-5,-7,3,8,-5,-8,9,-6,2],[-8,-2,7,5,-10,-2,-1,7,2,1],[1,1,7,-5,-2,-10,10,-5,3,10],[-9,4,1,-7,-5,-5,4,-6,-7,5],[10,2,-7,-8,9,6,2,9,5,-8],[-4,-5,-10,3,-3,-9,-4,-4,9,3]],[[-2,7,1,9,4,6,-2,-8,3,-2],[-10,1,3,6,7,-10,-2,-5,5,-9],[-1,6,-8,-6,8,7,-10,-3,-4,-4],[2,-2,-3,7,10,8,3,-5,-10,1],[-10,5,9,-10,9,-5,-8,-5,-5,10],[10,-9,1,3,-6,7,-3,5,-2,-4],[-10,4,-10,-10,1,2,-7,-4,6,10],[-2,-9,1,6,10,-8,2,8,-3,9],[-8,7,4,6,1,-4,-4,7,-5,-1],[-4,5,3,8,-10,1,-7,-5,-2,-1],[-8,-3,7,8,-2,9,9,1,-5,-9],[-5,-7,9,-3,5,-3,10,3,-5,-9],[1,-4,-2,-4,6,-4,-4,-1,-2,-5]]], dtype = "uint16")#candidate|3387|(4, 13, 10)|const|uint16
bop_3388 = relay.left_shift(var_3386.astype('uint16'), relay.reshape(const_3387.astype('uint16'), relay.shape_of(var_3386))) # shape=(4, 13, 10)
output = bop_3388
output2 = bop_3388
func_3394 = relay.Function([var_3386,], output)
mod['func_3394'] = func_3394
mod = relay.transform.InferType()(mod)
mutated_mod['func_3394'] = func_3394
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3395 = relay.var("var_3395", dtype = "uint16", shape = (4, 13, 10))#candidate|3395|(4, 13, 10)|var|uint16
func_3394_call = mutated_mod.get_global_var('func_3394')
call_3396 = func_3394_call(var_3395)
output = call_3396
func_3397 = relay.Function([var_3395], output)
mutated_mod['func_3397'] = func_3397
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3441 = relay.var("var_3441", dtype = "float64", shape = (11, 11, 12))#candidate|3441|(11, 11, 12)|var|float64
uop_3442 = relay.asinh(var_3441.astype('float64')) # shape=(11, 11, 12)
var_3447 = relay.var("var_3447", dtype = "float64", shape = (11, 11, 12))#candidate|3447|(11, 11, 12)|var|float64
bop_3448 = relay.floor_mod(var_3441.astype('float64'), relay.reshape(var_3447.astype('float64'), relay.shape_of(var_3441))) # shape=(11, 11, 12)
func_3021_call = mod.get_global_var('func_3021')
func_3022_call = mutated_mod.get_global_var('func_3022')
call_3452 = func_3021_call()
call_3453 = func_3021_call()
output = relay.Tuple([uop_3442,bop_3448,call_3452,])
output2 = relay.Tuple([uop_3442,bop_3448,call_3453,])
func_3455 = relay.Function([var_3441,var_3447,], output)
mod['func_3455'] = func_3455
mod = relay.transform.InferType()(mod)
mutated_mod['func_3455'] = func_3455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3455_call = mutated_mod.get_global_var('func_3455')
var_3457 = relay.var("var_3457", dtype = "float64", shape = (11, 11, 12))#candidate|3457|(11, 11, 12)|var|float64
var_3458 = relay.var("var_3458", dtype = "float64", shape = (11, 11, 12))#candidate|3458|(11, 11, 12)|var|float64
call_3456 = func_3455_call(var_3457,var_3458,)
output = call_3456
func_3459 = relay.Function([var_3457,var_3458,], output)
mutated_mod['func_3459'] = func_3459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_3495 = relay.TupleGetItem(func_1839_call(), 0)
call_3496 = relay.TupleGetItem(func_1841_call(), 0)
output = relay.Tuple([call_3495,])
output2 = relay.Tuple([call_3496,])
func_3497 = relay.Function([], output)
mod['func_3497'] = func_3497
mod = relay.transform.InferType()(mod)
mutated_mod['func_3497'] = func_3497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3497_call = mutated_mod.get_global_var('func_3497')
call_3498 = func_3497_call()
output = call_3498
func_3499 = relay.Function([], output)
mutated_mod['func_3499'] = func_3499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2903_call = mod.get_global_var('func_2903')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_3518 = relay.TupleGetItem(func_2903_call(), 3)
call_3519 = relay.TupleGetItem(func_2904_call(), 3)
func_2758_call = mod.get_global_var('func_2758')
func_2762_call = mutated_mod.get_global_var('func_2762')
const_3534 = relay.const([-8,-8,-1,-4,5,7,-10,-8,5,1,5,10,2,-9,9,-8,-8,1,7,6,5,1,10,6,-5,5,-1,-1,2,-1,3,9,-4,-1,-8,-4,10,-8,7,6,-1,1,5,-6,4,-8,-7,-8,-9,-3,-4,10,4,-4,10,-4,-8,-4,9,-2,9,9,6,6,-4,2,6,2,8,3,-6,2,4,-9,-7,-5,10,4,-1,1,9,-3,-3,-9,3,-2,10,2,-9,-8,-1,-5,-9,7,9,-5,-9,-7,5,7,9,6,-3,-5,9,-9,10,-1,4,9,6,-4,-4,1,-9,9,8,-9,-6,-1,2,5,-5,1,6,5,-7,7,1,5,6,2,-1,-3,7,-10,-6,-3,5,2,-5,1,5,-5,6,8,4,-4,-1,10,10,9,8,9,-5,3,8,-5,-4,1,10,1,-9,9,-1,2,-2,1,2,-3,3,-10,-2,3,-5,3,4,-1,9,5,-10,5,-9,-2,-6,-9,-3,-9,-5,-8,-7,-6,-6,-5,7,-9,8,-9,-10,-7,5,7,-6,2,1,2,4,-8,-6,-7,3,-10,-2,8,-7,2,1,-10,8,-8,2,4,7,6,4], dtype = "int32")#candidate|3534|(225,)|const|int32
var_3535 = relay.var("var_3535", dtype = "int32", shape = (525, 3))#candidate|3535|(525, 3)|var|int32
call_3533 = relay.TupleGetItem(func_2758_call(relay.reshape(const_3534.astype('int32'), [25, 9]), relay.reshape(var_3535.astype('int32'), [1575,]), ), 1)
call_3536 = relay.TupleGetItem(func_2762_call(relay.reshape(const_3534.astype('int32'), [25, 9]), relay.reshape(var_3535.astype('int32'), [1575,]), ), 1)
bop_3543 = relay.bitwise_and(call_3533.astype('uint64'), relay.reshape(var_3535.astype('uint64'), relay.shape_of(call_3533))) # shape=(7, 15, 15)
bop_3546 = relay.bitwise_and(call_3536.astype('uint64'), relay.reshape(var_3535.astype('uint64'), relay.shape_of(call_3536))) # shape=(7, 15, 15)
bop_3548 = relay.greater_equal(call_3533.astype('bool'), relay.reshape(bop_3543.astype('bool'), relay.shape_of(call_3533))) # shape=(7, 15, 15)
bop_3551 = relay.greater_equal(call_3536.astype('bool'), relay.reshape(bop_3546.astype('bool'), relay.shape_of(call_3536))) # shape=(7, 15, 15)
func_1409_call = mod.get_global_var('func_1409')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_3552 = func_1409_call(relay.reshape(const_3534.astype('int32'), [1, 15, 15]), relay.reshape(bop_3548.astype('int32'), [7, 15, 15]), )
call_3553 = func_1409_call(relay.reshape(const_3534.astype('int32'), [1, 15, 15]), relay.reshape(bop_3548.astype('int32'), [7, 15, 15]), )
var_3555 = relay.var("var_3555", dtype = "int32", shape = (7, 15, 15))#candidate|3555|(7, 15, 15)|var|int32
bop_3556 = relay.minimum(call_3552.astype('uint32'), relay.reshape(var_3555.astype('uint32'), relay.shape_of(call_3552))) # shape=(7, 15, 15)
bop_3559 = relay.minimum(call_3553.astype('uint32'), relay.reshape(var_3555.astype('uint32'), relay.shape_of(call_3553))) # shape=(7, 15, 15)
func_3455_call = mod.get_global_var('func_3455')
func_3459_call = mutated_mod.get_global_var('func_3459')
const_3570 = relay.const([-1.493218,6.750264,-4.301659,9.536157,9.159870,-7.339857,3.730142,7.947351,-3.164051,8.843380,2.576353,6.845710,-6.569966,9.098802,-3.519764,3.886480,8.715264,2.388152,6.995444,7.678513,-9.842649,-6.637623,7.898353,-5.553760,-9.956466,0.173423,-6.535068,-4.849729,-8.506250,-9.207271,-9.131878,5.955156,-3.914953,4.527646,5.114662,-6.070168,-7.318923,9.121074,-6.244100,3.172946,-2.500877,8.863102,6.100708,2.889328,6.820083,-9.894287,3.086756,-8.999157,-2.678726,1.002635,-1.314380,5.387775,-5.579418,-9.849529,-1.294542,4.066678,-3.308427,6.976007,7.832738,1.925356,-9.377780,-3.848756,-1.694326,3.877267,-8.537034,-7.692069,-1.297770,3.880523,2.340178,7.499181,5.613033,-7.542228,0.602182,9.600429,-2.911779,-7.860745,-8.084026,-4.993228,1.768570,2.016015,-8.185210,-4.825227,8.097417,-3.575799,9.708700,-4.401834,-8.184717,-4.369816,-3.216618,-4.436051,-1.656736,0.462611,7.575259,2.819315,0.767746,-3.444100,4.755640,-2.233304,-4.768345,3.565401,-4.148944,-4.702005,-2.749839,8.060907,-4.643030,8.011739,-9.066341,1.562859,-4.512024,-8.618208,0.316156,6.264199,5.998006,0.496687,-3.176330,3.762750,-6.363254,-0.491263,-8.050970,8.678500,0.659377,1.740721,6.128409,-8.671818,-2.204429,3.444419,4.110558,-4.404555,-1.824340,6.682167,-6.444096,-1.378596,-9.027723,3.916697,-5.139706,-3.761170,9.511988,4.055321,-4.010014,-7.314029,-9.032475,0.096952,-1.227430,-4.429447,7.529530,-2.194785,-0.207208,7.547068,2.653779,6.484058,3.349925,6.270741,3.129849,-0.618554,-8.457536,-9.349545,-7.315926,0.901688,1.383856,-6.877942,5.769931,-1.398528,4.169602,-0.596473,-0.170323,-1.153456,7.203289,-4.524098,-4.532287,9.384916,1.832055,9.458987,2.035188,4.687609,-5.613517,1.669211,-8.133212,8.778468,1.726727,-6.815610,1.205353,-8.399933,-0.813455,0.704717,5.870377,-9.530787,5.991881,-6.750283,-7.967516,3.586641,5.714872,-6.238633,8.092178,8.702132,2.101282,-0.358825,-9.408246,-6.656203,-2.043979,6.925301,-5.402017,-1.055253,6.486984,-7.923375,-6.118641,-2.073452,-4.178814,6.882905,-3.207507,5.141040,-7.287118,-4.222416,-9.227123,-0.596525,3.801220,-9.307359,8.103343,5.754091,5.986789,-2.592416,7.454748,-8.909241,3.751496,0.983838,-4.735519,8.875335,7.723307,-6.725814,-0.287946,-4.352377,-1.173257,1.495842,4.625431,1.212879,-4.912635,4.566307,-0.936743,-2.180205,6.675526,-3.241536,-6.808095,6.084037,1.169835,8.331651,-0.380531,2.492705,-0.373674,-1.771007,0.554534,-9.698586,4.359475,-5.149787,2.345025,8.507028,-5.837727,9.795471,7.426000,-5.037160,-6.232098,7.092166,4.327578,6.968951,6.496022,-7.113290,8.334123,4.520023,-7.838523,1.663858,-4.200067,-7.817673,-5.286014,3.005180,-1.315975,-1.764678,2.004388,4.380024,7.015007,-8.137850,-9.739860,1.461894,0.540696,-6.929003,-5.918999,-7.669012,-9.485464,-8.185607,-5.902935,3.940610,2.900591,1.885198,2.683183,-4.619289,5.737660,9.472730,0.807949,-2.312694,7.962930,-1.684315,-9.138099,-2.187898,2.494622,1.012162,-7.042490,6.482781,-2.720497,-1.743664,2.433665,-5.222857,2.102747,0.996451,3.686954,-1.950742,-0.008830,-0.428192,3.543790,-2.925081,7.965352,-2.428865,-2.436939,-0.563668,-3.678523,-6.275718,0.740300,-6.545210,-3.849229,9.178685,5.861950,8.010689,-5.442199,-5.724962,-0.038505,-8.936731,-6.631824,-9.299024,-5.599043,-7.961515,6.229642,0.969704,3.211209,-1.109305,6.955050,0.897423,8.291964,-9.229751,2.177156,7.655336,0.372057,6.614564,-8.503256,-0.816567,-8.944585,5.325199,9.882936,-8.577091,-2.252362,6.055870,-8.803493,2.720134,2.186229,6.588490,-1.147027,-3.666400,5.515822,-4.084256,2.219797,-6.390903,0.307962,-0.196641,-0.025132,3.837049,5.775914,-6.818140,-7.380275,2.281420,-0.793638,-9.577847,0.719274,-0.629812,-4.728864,-9.942509,-4.944548,-6.434350,-6.545360,-2.017702,0.783294,0.709679,-6.858562,9.121320,5.996996,-3.395730,9.294954,9.305398,-2.060604,8.429737,-2.046640,-8.662654,6.014715,-6.047466,3.989880,-9.310821,-9.629723,0.944320,-3.194837,2.340893,9.076053,9.534754,-0.488660,0.880426,-4.082131,-2.181594,-7.133776,5.325815,1.625244,8.935265,2.673308,9.120181,-9.803089,-3.392045,6.944916,-9.556254,-4.700065,-2.006685,-1.750338,2.159155,-9.386846,9.764817,-5.697945,-1.382818,-3.270778,5.319880,-4.908740,-8.869412,9.109056,1.363174,-7.259443,-9.134882,1.754393,-4.332243,-0.154353,-7.947534,3.609092,-5.415949,6.169767,3.461685,-4.888578,7.576600,6.293319,2.785414,-9.991154,-2.256278,8.269593,5.059885,1.306498,-6.892805,8.823288,-1.038442,0.188555,3.733379,-7.432812,-5.894676,6.749330,8.063035,9.325921,9.253209,8.396820,1.819884,-8.201411,8.994619,-7.239654,-0.547893,-4.141256,-5.070847,6.092833,-3.180309,-9.505354,-2.248821,-2.721485,-8.487906,5.583293,-7.965474,6.429013,0.107878,-0.676906,6.160154,-9.340363,6.390310,8.941639,-5.122363,2.839875,-5.384044,-4.013266,4.357370,-4.315280,-1.394280,7.215516,-3.728583,-8.537636,5.966217,-5.608479,6.714517,-7.097060,2.709174,-4.160549,-8.823359,4.827554,8.653741,1.019233,-0.410603,6.966475,4.683011,1.116815,7.973165,3.593767,5.970292,-2.625490,8.003943,4.244175,-0.753268,-3.136992,6.664979,6.824149,6.422769,0.792300,-2.579068,1.731055,4.325430,4.666524,-8.065652,6.905633,-1.578927,8.332743,-9.679730,-9.397402,-6.441654,5.643254,-3.320053,7.579246,-3.861063,-2.284127,6.916888,-4.195678,-6.691004,3.490013,2.332373,-3.870370,-2.241172,4.601021,-9.333131,7.854970,-9.904540,-6.706675,5.795488,2.873196,-3.894867,-4.750559,0.220064,4.865722,-9.284805,-5.994447,0.304665,1.544531,-7.127693,1.378696,5.634561,-1.333689,7.740036,-1.407448,-2.583748,-0.751395,2.613727,-4.673464,-5.795533,6.855614,-6.735433,-3.227083,-1.246255,-2.967429,-7.638867,-0.458614,-6.338151,2.643760,9.703652,7.259063,1.274205,1.910226,-7.953885,9.864479,7.672967,-5.634682,4.615565,8.749600,-6.288932,-9.149046,8.268577,-5.899967,2.298618,-2.881547,-5.955103,-2.898250,0.059149,-4.103981,8.249840,-7.051508,-7.455095,0.484894,6.490729,-7.534900,-6.486248,-5.925110,2.342483,8.360300,3.973143,7.952808,4.632301,8.328925,1.745048,9.323711,-6.983800,2.464995,-1.592711,-7.424193,-2.346180,5.471590,6.335903,-5.003736,0.832683,-6.830672,0.545257,-2.651893,1.589248,-1.278122,4.034946,-7.076974,2.685789,0.848810,-8.885292,-6.549966,-5.386343,2.156703,1.241252,-3.312306,3.440388,7.503939,-0.208485,-1.484246,-2.858522,6.080138,-1.669044,0.983786,0.503857,9.392530,-9.183696,-8.972689,7.705148,-9.068723,-3.910861,9.159610,2.436926,-3.022462,-6.379649,-2.490227,8.987901,3.509434,2.300106,-7.925057,3.670338,-2.842966,6.015625,-5.367629,-1.470629,0.021854,6.478956,-5.417182,-1.566428,-5.280586,9.790900,4.477788,-7.561046,-0.627773,7.727206,5.859798,-8.494937,-0.128395,-4.689213,8.836834,9.352363,4.109145,3.200312,-4.928618,6.291834,6.876143,4.227529,7.832675,5.332453,3.791660,-4.409399,8.383427,-0.306499,-3.802822,-3.994989,1.218601,7.140523,-5.361637,-3.636993,-6.618134,0.736275,1.819178,-1.564408,0.199563,-4.058994,-4.262344,8.026239,-8.242495,6.316258,-0.660378,-9.042975,4.539894,7.373428,-4.553860,-0.438216,9.712484,-5.222942,-5.084728,2.810109,-2.803249,-2.095320,8.039379,-4.856926,3.339280,-7.818899,5.558886,8.318741,-7.591848,-9.754613,0.008489,1.923250,4.369970,9.385274,-4.374297,2.846215,-6.501101,4.160569,3.191240,1.318442,6.298770,-7.064343,-1.062436,-9.915220,-4.539958,-3.598134,4.397123,-3.552840,7.502432,8.675111,6.004711,1.936094,-1.167317,2.215542,-9.722679,4.751013,-9.848238,9.103313,1.598782,-1.352285,-1.628737,2.129160,-5.099369,-6.640738,0.567232,-2.816166,-3.397184,3.700385,-2.923976,-4.882046,1.833066,1.729893,-2.237583,8.734786,-8.435422,1.687896,-0.443546,-9.854071,9.881647,-1.960495,-5.962051,7.689624,-3.630743,-9.108088,8.789929,-1.422766,-2.584472,-2.607458,-4.451480,-7.294142,0.244238,2.675705,6.956320,8.670386,0.244982,5.400667,-5.815448,-2.148527,1.323800,8.564848,-8.216623,-1.041854,1.406204,5.109778,-0.205394,-7.376769,0.056191,5.660178,-6.885805,8.437062,-6.256109,0.730719,3.034905,-7.941802,-2.540346,6.234940,6.815793,2.882750,9.189535,-1.884132,8.494970,2.092464,-9.766422,2.150064,4.911205,-3.824117,8.580642,-0.135486,-4.024620,-0.885386,6.329862,5.524482,8.359101,4.754348,8.890737,-7.792228,5.987445,7.320689,-2.369924,-6.461249,-4.458465,8.432156,-9.918871,-8.732125,-5.085369,-6.484735,1.598463,-2.298487,-3.524253,3.201920,7.679983,-6.202923,6.764690,2.477220,-4.590967,-3.563852,-5.605147,3.929115,8.350388,8.669746,-8.385650,7.974582,9.837168,-9.907682,-3.274762,6.597365,9.561996,-5.029175,-9.334001,-1.530297,4.298808,4.152838,-9.862561,-5.659758,-5.687091,-8.462136,3.127605,-2.194519,2.251396,4.420818,-9.560513,-0.882916,-0.345128,5.413092,-4.760207,-9.215268,-8.869678,7.519872,-4.397220,-2.142200,-7.163179,5.437173,1.559242,-3.843143,-7.720399,-9.283959,1.787454,-8.775011,5.366511,-2.581329,5.887235,7.592032,-7.347034,-8.504195,-0.835726,2.983897,8.256373,2.857074,9.252848,-4.774985,4.712981,-6.597926,5.397276,-3.242040,-8.167541,-3.603015,7.983079,6.621925,-0.412261,-7.128198,1.108324,0.857725,-6.783907,9.364026,6.808057,6.372181,-4.636758,2.928212,-7.245608,-1.145868,-1.471172,-6.780265,-0.198980,2.914448,-2.539252,8.793445,3.691634,-4.556003,9.973453,1.032510,6.192700,3.666304,1.139778,3.155594,9.171733,-5.395981,-9.456867,4.236017,4.766395,-2.574674,5.868281,7.281714,-7.114057,-5.687963,0.498255,-7.162538,0.977113,-9.551301,-2.390484,-5.080274,8.615341,4.464589,-7.211885,-2.508690,4.149003,4.398242,-6.594841,-9.452275,-9.131883,3.496535,-2.744112,1.475500,1.501252,-6.129601,1.869117,0.501272,-2.835464,6.725043,-1.244780,-5.738888,-2.299643,-6.507377,-7.979033,5.407659,7.414076,-1.958355,6.103369,0.968710,9.470101,-4.805987,6.285482,9.763833,7.213748,-4.048889,-7.993738,5.718404,-6.288497,2.611750,-8.506766,9.326620,4.641089,-3.738016,9.668711,-2.394565,7.410138,-5.626345,-5.868516,-2.056802,-4.155424,8.615825,8.443867,0.781283,-3.906328,-2.882749,5.985943,7.819069,7.359505,8.768143,5.550866,7.762895,5.817368,7.304446,9.166582,4.114947,-7.164980,-9.557274,6.868741,3.123772,2.603677,1.221908,-3.811178,0.561323,-2.607525,-6.617921,-6.490556,-3.923274,8.841780,-3.436454,-1.265814,-1.759004,-4.201696,-4.782934,-1.935282,-7.365103,-6.454473,5.512691,-8.618466,-2.948048,0.268473,-5.532551,3.271665,4.988850,9.757218,6.034478,1.936240,-7.300034,3.979365,-6.466398,5.633279,9.791337,-3.240578,-1.669078,4.545215,9.759318,6.557458,8.761233,-3.027473,-3.393692,-6.324081,5.870806,3.849722,4.937641,2.693655,1.192000,-0.718781,-1.526870,9.301883,1.944607,0.902951,4.047327,5.065139,9.619818,-6.834080,3.804195,-7.332912,-2.765694,-5.925969,-5.289840,3.406457,-1.812524,-4.559948,-6.978839,8.497398,-3.258954,-5.129146,-1.053534,-0.089005,-7.191309,6.034585,5.599966,-3.967455,9.874957,-7.757766,-9.712694,7.750840,1.607994,0.103477,0.533264,-7.933222,-1.343281,-4.697343,-0.675754,-5.854891,3.598543,-3.753655,6.468726,-7.931158,6.055227,-5.283092,1.130174,2.722534,1.649788,-7.269829,9.187286,7.972512,-0.011237,-9.792712,-0.962188,3.640106,-1.944772,9.465564,-2.794510,9.037563,-0.646887,-9.852000,9.319268,-3.234230,-2.164860,-6.264873,7.045972,1.615928,8.111011,-1.213377,8.273377,4.046524,2.404769,6.246007,-8.579208,-1.114646,4.347433,-6.808328,-6.721871,9.165596,-1.581070,-7.014323,5.347170,0.557285,-7.714864,9.466372,3.116133,0.230075,6.031076,-8.865265,9.409920,-9.073752,5.000709,-6.097184,7.527351,0.251941,5.189070,-9.284600,1.987681,2.636944,8.136109,1.310723,5.823423,-7.209877,-8.622489,-7.210253,5.842487,-8.901733,-0.063764,-5.952961,-7.941648,8.020493,9.940228,3.744026,5.791497,-8.165541,2.755113,7.136697,9.854515,4.744767,-4.183608,6.290049,-8.458356,6.742868,-3.013242,-1.017435,9.718314,-8.308504,4.146958,5.937617,-5.238750,-3.817125,-2.223876,-4.689497,4.147279,4.539175,-2.962355,7.075271,-2.469547,2.738167,-7.584727,0.364792,7.432557,-4.141740,8.042684,9.891456,-3.647071,9.881541,2.038936,-5.423771,9.445576,-5.784391,-5.665863,-2.508923,-3.018662,-2.012638,-3.037308,-7.451257,0.156510,-5.691743,1.661691,8.440519,9.761089,-8.867741,-3.263466,1.666658,-8.077649,6.891435,6.183814,9.342544,9.898093,-2.892393,1.155562,2.876258,-9.068312,-7.516302,5.045945,4.845198,-6.874228,8.372780,-1.015210,0.479384,3.868252,7.853855,-8.421372,-6.006078,-8.452286,2.290352,-7.648788,4.825586,0.996489,-1.920470,7.609534,2.852088,3.380032,-6.753252,-9.968864,-2.550060,9.468615,-0.277115,-4.394220,0.774412,-3.153602,-2.815203,-9.276202,6.823924,0.766288,-1.845058,6.624915,9.743277,0.170939,-5.215643,7.914367,1.928164,-8.807682,-0.820704,-5.683822,-2.680794,1.993865,8.132767,-9.525715,8.463328,-0.675738,-0.270496,0.865516,-0.543226,5.869389,-6.976023,9.929610,7.311481,-7.991673,-5.919309,-6.548913,1.887911,-6.798523,1.481839,2.814419,-1.165566,-8.284727,3.086891,-5.075093,-1.383651,-1.903426,-3.643589,-3.891796,0.572437,-6.832489,-3.250714,-8.363065,-3.961097,-8.447650,7.730019,-1.376126,-2.496199,-0.478253,-7.336347,0.926199,3.144268,-8.992696,-0.928918,3.343634,4.115450,6.853968,-6.184646,4.052106,-9.822879,-9.482475,7.018426,-4.805982,-2.880540,3.095898,9.472605,8.614310,-7.453539,5.924670,8.825411,-6.776161,-1.864436,-0.030508,-5.820214,8.720166,2.960267,-7.471642,-9.782800,-4.108018,-7.791654,4.577116,1.425466,-0.696659,-3.086433,-4.520569,-7.750064,-7.891962,-8.037340,-1.019462,-6.183561,-9.718078,9.776540,-9.628314,9.909419,-8.145769,-7.682200,9.758113,2.122112,4.390178,8.929847,2.935021,0.808278,-2.830657,-3.437510,-6.268395,-7.237639,-1.625045,2.212854,5.328970,-9.958996,-2.023666,-9.221407,-6.189740,9.883081,3.504930,5.994821,8.832316,9.638372,-6.998793,-3.532272,-7.694245,7.020014,-1.276596,-0.686759,1.814765,-9.998317,5.230901,-9.665199,-0.412535,-7.087985,-8.281397,-7.714455,-3.993573,-9.961401,4.957274,4.623089,7.779888,-4.424791,8.957098,-5.481580,2.525190,9.266413,4.245929,-0.482266,6.831327,3.823065,-8.233669,3.970304,0.387001,-5.290740,-6.592913,7.720458,-2.205777,-3.936149,-4.824020,7.830826,7.889125,-1.914536,-7.476713,-3.821656,8.236847,0.997900,7.742551,-7.714329,-8.736075,2.627130,-0.059388,3.709399,-3.974832], dtype = "float64")#candidate|3570|(1452,)|const|float64
call_3569 = relay.TupleGetItem(func_3455_call(relay.reshape(const_3570.astype('float64'), [11, 11, 12]), relay.reshape(const_3570.astype('float64'), [11, 11, 12]), ), 2)
call_3571 = relay.TupleGetItem(func_3459_call(relay.reshape(const_3570.astype('float64'), [11, 11, 12]), relay.reshape(const_3570.astype('float64'), [11, 11, 12]), ), 2)
func_1992_call = mod.get_global_var('func_1992')
func_1995_call = mutated_mod.get_global_var('func_1995')
const_3574 = relay.const([1.815449,-9.580283,-8.802708,-5.730032,-2.618900,-5.371597,1.942733,1.519457,8.122723,-1.798071,-7.659477,8.384338,7.164376,1.344771,1.615460,6.945298,7.109392,7.510141,2.914706,-0.913379,0.740457,4.604396,6.736218,-4.780504,0.963938,1.794027,6.272404,-8.738739,3.273937,7.803638,6.548636,3.610382,8.423395,-6.327057,-7.432678,-6.468417,-9.491499,-2.182003,8.667257,-7.926356,8.001903,-7.160135,4.313970,-0.316523,-8.208542,1.861837,-7.254630,8.803093,8.702262,-9.785946,-5.499797,6.883162,-9.235587,4.026057,7.951604,-6.353526,7.800613,9.993403,-8.594022,4.831236,-4.575680,-4.415911,4.502367,-2.759275,6.721555,-2.596830,5.503490,-7.475494,8.187303,4.038797,-0.802637,-4.019319,-1.832466,-4.149482,5.415611,-9.782215,-9.481970,-5.335530,-2.704923,9.922500], dtype = "float64")#candidate|3574|(80,)|const|float64
call_3573 = relay.TupleGetItem(func_1992_call(relay.reshape(const_3574.astype('float64'), [2, 5, 8])), 0)
call_3575 = relay.TupleGetItem(func_1995_call(relay.reshape(const_3574.astype('float64'), [2, 5, 8])), 0)
func_3367_call = mod.get_global_var('func_3367')
func_3370_call = mutated_mod.get_global_var('func_3370')
var_3583 = relay.var("var_3583", dtype = "float64", shape = (2352,))#candidate|3583|(2352,)|var|float64
const_3584 = relay.const([9.939951,-3.068320,5.878979,-9.382315,-9.946451,-6.835766,9.825310,-0.966125,-0.030682,2.084675,-7.233128,1.743831,-4.706127,2.190434,-4.137944,0.820118,-8.438572,-9.430773,6.415842,3.105663,8.059277,0.361977,-7.645548,-6.466633,7.908190,-9.021246,-2.444514,2.798171,-4.425456,-6.587345,3.917184,-7.554666,8.945318,1.152022,6.971661,9.448695,-3.107463,3.785405,-0.336870,-8.754895,7.678663,8.277931,-8.244456,-3.608748,-3.502637,3.736391,0.424069,5.830566,9.443356,8.097767,6.947903,5.303916,0.938967,-7.345110,2.404819,-0.518476,3.961793,-1.097846,-9.957629,-4.222315,-5.229244,-4.098189,-7.096387,-9.501210,-4.896562,-3.161849,-9.857021,-5.976962,2.152967,8.981621,7.868867,5.282373,-5.194947,-7.012626,9.480581,4.753342,-7.845637,7.165220,7.912680,-8.771903,4.681606,4.851173,8.895315,-9.770511,5.383349,3.024911,8.852478,5.281126,-3.911124,-2.807095,2.137812,6.998890,0.520764,-2.683311,4.997640,-5.901058,2.767880,-4.900496,2.711194,9.877381,4.801081,6.212362,-9.510676,-0.303596,-3.385330,-4.831121,-8.619982,-2.801418,-5.401404,-9.290805,8.948000,-4.412523,-3.779310,9.033235,7.134184,-7.741834,5.143845,5.146274,7.376760,1.013258,-8.335619,7.575545,2.867107,-9.078190,-3.515440,2.918094,-1.019684,-2.686271,0.636535,-0.576379,9.076336,8.418529,9.878763,-4.446235,-7.584172,-4.448200,0.803848,6.933040,3.953340,-2.688244,-6.684277,-3.691367,3.308830,3.453404,-9.509966,-3.884791,3.363455,5.735743,-6.042064,0.190101,3.913198,-9.310511,9.228883,9.086338,4.877338,-3.720958,-0.379497,-1.742687,8.148376,-3.438998,-7.601617,9.784806,-4.299194,-3.674022,-3.341493,8.356619,8.758924,-9.965916,4.653332,-7.018681,5.103745,-0.263930,4.257533,-4.892425,-1.267705,-0.405951,7.472327,-7.440304,-5.520317,-9.653400,-5.576232,-4.263250,5.797509,-4.482652,9.028211,-6.762763,5.385101,-0.902341,7.496340,-5.884717,8.700458,-3.098575,-4.249006,-1.621808,4.163412,-2.012140,-9.552347,-1.082805,9.175028,-5.410204,1.735915,-2.347751,1.725004,2.836091,0.542441,-5.277684,-7.331754,5.041179,-0.013717,-0.600946,-7.074939,4.411844,2.418819,0.024602,0.976831,5.298607,-7.273914,5.312500,-8.350480,-8.570278,-2.164651,-4.727248,-9.728161,-4.011032,5.870120,-9.397314,7.630635,-1.235807,4.815234,7.064164,5.432133,0.381533,-8.725207,2.175044,3.214680,-1.135037,3.956717,9.180614,-8.821002,-6.761438,-4.261531,-3.182446,-3.882794,-6.281500,-5.127665,-2.371183,4.005932,2.822087,5.564561,-8.176269,-6.036764,-1.410604,-2.138184,8.526509,0.887674,-2.670738,1.125225,7.376492,-9.423995,0.963895,-9.825860,-3.120402,-4.967524,1.124627,7.317831,-4.229444,4.539501,6.768853,-7.708034,-7.116645,-8.948393,7.755783,6.684357,9.514180,0.381040,-1.551712,2.510144,4.096762,-4.384554,0.321913,-2.247443,-1.852463,-1.530911,7.662643,-1.593338,6.273836,1.133592,-9.574853,6.586166,-0.555932,3.618549,-6.392569,3.375705,-0.136496,7.415717,1.569869,8.911510,7.580980,6.431265,8.267503,-7.252717,-4.735495,8.653220,5.838183,0.523952,2.465945,-6.940888,0.239072,5.408012,-2.149303,7.779482,0.644867,0.307396,-1.214148,0.021934,-9.762292,-5.867144,9.284452,-6.618071,7.739518,-4.262507,-9.906234,-9.385473,7.881079,3.822770,-6.181292,9.048364,8.458211,-1.883649,-6.890298,3.637880,-5.587393,2.209285,-2.021521,-7.239200,4.425696,-6.964615,4.849494,4.780935,3.791309,-0.706427,3.210176,1.490780,-7.171618,7.563883,9.656788,-5.007513,-1.316093,-5.628288,8.567565,-2.621712,9.182642,-3.762811,-6.755249,0.771440,-2.374071,9.077400,-0.600003,-0.617514,8.034299,0.274797,2.555257,-5.036304,5.583311,-7.698227,8.161348,-6.600183,1.191751,0.786876,-3.908753,1.751729,8.578665,6.620900,2.503421,-8.179507,3.464305,-7.000653,3.063112,-1.776076,5.850660,7.813723,-9.345797,6.592165,-5.021799,8.405383,-5.800120,4.908302,0.069010,2.951923,8.269111,1.619271,3.791876,8.832250,-7.634279,8.932343,-8.976135,-7.500230,-4.845060,-7.448929,7.063957,-1.434776,2.867570,4.693213,-6.568387,4.432844,-7.568855,-1.538881,-0.438218,2.889262,5.141006,-7.708919,1.181380,-8.358626,7.402642,3.518575,-2.256810,-4.051926,7.544683,9.393226,-1.297440,0.729658,3.722728,-3.103740,8.984364,8.274145,-7.960405,-3.729465,-3.123284,-1.687259,-1.107369,-1.785046,4.056396,-5.252233,-1.616083,-3.588585,-8.261960,-9.532870,9.194266,-1.534649,-6.755271,2.675191,4.451967,-5.479670,1.726204,2.205697,-6.009548,-6.788551,-0.698431,5.898342,-5.397551,4.541659,7.001658,4.994437,-2.653221,-4.945034,3.439015,-2.664845,9.152202,-1.860376,2.773114,-5.673211,-9.183590,2.823816,8.985455,9.059515,-4.834613,7.162926,-0.774134,-2.577904,-1.211666,9.236346,-6.540446,-7.451439,4.659462,-2.385148,6.684549,-4.787168,-3.346649,-1.243786,-6.654648,2.685365,0.790687,4.914138,1.652445,-2.776280,-4.619420,9.209074,6.044992,-4.018347,1.177335,6.853422,-4.231488,-9.229472,9.382500,-5.671937,-8.118806,-2.235703,-5.636558,-7.288761,0.404244,5.467761,-8.402497,5.217421,2.666469,-4.552484,-9.421131,5.056224,-5.355611,1.299902,-5.051466,8.601657,-9.303370,-5.764734,5.928954,-4.211298,-0.558234,-8.038653,9.898774,-4.917793,-6.264205,3.868537,0.557780,2.445597,-4.971277,3.033253,-6.988640,7.965309,4.771214,-6.815968,-9.786949,1.276312,-2.530110,-2.016830,0.340976,-3.635184,6.665901,8.842288,-6.454257,-6.883855,8.605877,-0.558036,3.137621,-8.204742,7.231486,7.469865,-7.872342,-3.667741,9.164199,-6.473922,-3.481819,-6.965338,-2.260155,-7.719770,-2.790908,7.238457,-9.743579,1.603219,9.822217,-4.206261,-6.803752,2.872985,0.203270,-4.703821,-9.815596,3.166438,7.514705,-0.532930,6.236788,1.037218,-3.694080,-9.055526,-4.165025,-6.372471,7.192560,-5.911321,-5.392262,-1.162857,-8.809706,-2.203238,8.225731,8.836227,3.146530,-6.421186,-7.659846,-1.793165,-1.830907,5.621112,3.849486,4.822195,6.752288,-8.838150,8.809139,3.871399,7.620305,-5.682967,1.677261,-6.274067,1.079727,-9.880667,-1.315504,-2.560035,4.095121,3.795292,0.966421,2.779258,-9.526637,7.152206,2.549107,0.502023,-8.855984,8.500036,6.163436,1.087721,1.549917,-5.908848,-8.134475,-1.936631,0.694327,-1.489552,-1.977281,5.561628,-2.013079,-4.035436,3.576358,-3.983465,9.696183,3.516744,4.548308,-1.567681,-2.685241,-4.020359,9.469406,-2.424582,-3.173928,-9.069915,2.616589,-0.822611,-0.792135,3.539432,-7.738638,3.652219,7.204437,3.092981,0.014925,0.457996,-0.980596,3.916985,9.249419,-9.757846,-5.865801,-2.006881,-4.252529,9.365199,-1.141747,-2.953184,6.968124,-1.231004,4.801238,6.361277,1.781303,-9.529565,0.296875,-0.393446,-1.900789,-6.426665,5.306986,-1.479847,2.699786,-5.055440,-4.173421,6.712661,-2.542159,-3.219737,7.307777,5.491722,5.380531,-5.811173,3.937924,2.278670,-1.675707,-4.706252,-1.112281,1.080161,8.856018,2.144082,3.639041,2.384323,1.630582,1.187103,1.437204,9.134278,-6.457424,9.507962,-3.677244,9.190209,7.163290,-7.202886,-1.830250,5.178179,3.525478,9.640576,4.868045,8.879478,9.609152,2.100798,9.565713,5.632678,4.220930,3.298003,7.867590,-7.524479,-0.784299,-7.937116,-3.076782,-0.150102,7.277823,-9.955408,-1.959370,6.829088,-5.736852,5.697341,0.460579,-4.602960,5.322032,3.151967,-9.351336,2.605202,-8.638042,-5.601018,-1.001721,5.312988,-4.162433,-0.095326,4.687724,-2.038824,2.207188,6.913446,-1.135670,5.722212,6.587501,-1.076473,-8.639304,-9.945213,-5.348016,9.065995,-8.792175,-1.111738,5.706970,6.771262,-2.876467,-6.434852,4.766233,-1.546436,1.805383,-5.039073,-1.834661,9.407520,-6.667776,-7.824151,-2.541107,8.098235,-0.140538,2.956641,3.608017,-8.601275,7.607217,1.283743,-8.586289,-6.184369,3.216270,-1.404031,-0.323904,-4.724067,7.931531,3.562053,-3.160820,-9.123080,-2.303346,-8.317342,8.090503,7.643327,-3.028664,6.558702,-0.174667,-2.446528,-9.342363,-5.512545,-6.710792,-3.620414,1.279654,4.093626,-2.930853,-5.503322,-2.687249,-0.074731,4.349058,-6.245649,-3.886632,-6.827643,3.302293,-3.516144,8.953666,-9.954705,2.874343,4.478753,-2.159817,1.469513,6.599795,4.865059,-6.369718,0.059592,9.145044,1.069964,9.752610,0.205640,7.295227,3.412260,-8.838152,-0.091655,-0.808780,-7.059974,0.417939,6.683655,7.304649,-2.707400,9.881380,3.789806,1.618695,-5.684025,-2.866574,2.898243,-9.717932,-2.853009,3.521005,-6.464808,-2.923247,-0.639731,-7.758506,-5.857851,0.092805,-7.165078,-3.221089,4.276438,-9.194608,7.579867,4.770385,-6.295169,3.295414,-9.285869,-9.969110,-8.991540,1.947307,-0.927554,-5.759035,6.217821,5.778100,-4.680392,5.533577,6.688413,-0.802718,-5.041520,7.814118,2.950476,0.010781,0.463944,-3.602644,0.379873,7.412046,-4.251539,-3.401884,1.655719,9.642138,-7.415916,3.959044,-3.661621,-9.908982,-2.218139,-1.717809,-7.871750,1.302384,2.823008,3.947350,-3.420214,-9.287554,-3.440206,-6.462674,-5.444584,-2.752047,7.351067,-1.305745,6.296011,-7.937654,-4.087094,6.412765,6.492376,7.719586,-5.123716,3.613383,7.358983,6.796662,-2.785206,8.688017,2.940502,1.592297,2.292546,6.404720,-0.943832,-8.149154,-6.145442,5.796433,8.986978,-3.233876,7.822550,-9.607498,0.401906,9.016067,4.769588,-1.784308,-1.532545,3.923977,7.634545,-9.452640,1.326543,-4.007501,-9.996902,2.922286,-9.266698,4.529860,6.843846,-1.973859,-2.205837,-0.613179,-8.433001,-3.034226,2.329232,4.372657,-9.999979,-6.187032,-5.066056,5.790830,2.293934,-8.432335,-3.624143,9.236163,9.995008,-8.427536,0.523012,-3.893768,2.701876,-0.688639,-8.495461,7.242591,6.829957,-7.547936,9.658726,-3.086045,-9.223576,-2.366518,3.188429,-1.779847,-1.471512,-4.507135,-2.653727,5.124603,3.673791,-3.763157,6.443863,2.257118,1.885545,6.185709,4.425481,3.453284,-4.294871,6.330081,-6.905334,6.980850,-1.601243,-1.958044,-3.439715,6.751654,-7.696103,8.754296,7.686204,-9.247005,7.853215,3.091421,-8.398527,-4.499111,1.022890,-1.940487,-9.442494,-1.306098,4.349164,0.485523,-9.263516,7.489126,-3.310791,7.283064,1.544640,-9.501083,4.278613,-1.817702,0.508236,-5.208063,-4.993303,-0.986308,-1.129886,2.317904,5.574280,9.028446,1.345579,-6.533262,-9.663814,-0.854652,-3.588202,-6.644776,-5.900921,2.125749,0.856960,-6.419912,-8.061338,-8.272640,7.500844,-3.566687,-4.974082,6.831654,-1.785215,5.780967,9.138267,9.162408,1.344737,6.895452,-1.515934,2.290545,-8.935326,1.409900,-9.953921,-8.254765,9.233176,-4.875180,-5.005750,-2.989807,-7.617685,8.581852,2.160004,3.580855,-9.515999,-0.529514,8.235287,8.011596,-5.028083,-9.823702,-9.069888,-5.553726,3.857613,-5.301825,-8.884042,-2.202656,-3.392575,-3.213556,-5.328332,-9.862160,-7.440133,0.135768,-2.659134,-8.271738,2.322341,3.109338,2.908389,-2.178286,6.377432,-3.710577,3.186001,-3.884258,7.690874,1.286092,-6.527289,-9.988921,-1.994996,-4.404393,-4.739324,9.897275,7.389741,-3.024483,0.659680,4.540123,6.921118,-7.885643,-3.836630,-2.912361,-2.628472,-0.275624,-9.061081,8.160609,-9.054256,8.570774,-5.285558,8.526124,-1.175759,-5.441412,-0.080827,-6.400988,-9.019540,-8.270921,7.088698,-7.352635,-6.649884,-9.351999,1.618109,6.728043,0.380563,4.682002,-1.559636,8.156232,-3.684543,-8.781868,7.714011,-0.375347,2.256621,-1.966193,9.105167,-1.243806,4.011688,-5.055601,5.505276,8.285929,2.323738,-1.060346,2.511342,-7.741092,-7.986798,-9.287373,4.062222,7.272215,1.944008,0.656758,-4.732630,-9.334626,-9.294031,-3.989871,-6.044874,-9.505198,-9.303875,0.594705,-7.357468,3.560240,-3.453559,-2.246128,-2.473869,3.903385,6.576252,3.274202,-0.848145,-0.267734,-3.556977,-6.128232,-8.870537,-4.328528,-7.742464,-0.745007,4.492591,6.386579,3.954871,9.936375,4.672427,3.845908,4.836768,-6.963251,-1.027474,-3.221586,8.743579,8.692778,1.844189,2.504707,-7.581418,-2.015544,8.492856,1.397769,5.220324,7.981785,1.997101,-5.466508,8.429193,5.573067,7.381027,-6.820954,-9.783666,-3.661311,-4.560350,5.071816,4.944351,-3.992612,8.692615,4.436564,2.942269,0.838996,4.573356,1.806996,-6.904295,-2.059418,2.252848,0.282546,-4.519314,2.123254,0.502946,6.572572,8.721106,3.590593,-3.781186,7.923640,0.219732,-0.518468,-4.347775,0.181004,-5.108772,-4.056173,0.980890,-5.927287,0.396806,-9.066747,-4.447033,2.911730,2.974614,3.361590,2.526032,6.088693,5.774623,2.218430,-2.648853,2.631822,-9.330360,-1.049306,2.853465,-2.379275,-8.201912,5.188589,-5.535608,-3.327264,2.126823,6.079358,3.777506,-1.102292,2.225986,-2.434451,-8.312990,-5.588588,-4.133982,-1.896452,2.377134,-7.011654,5.979094,8.228680,6.493768,-8.223510,8.954774,4.874915,-3.439616,8.685407,-5.537408,3.553680,5.484013,6.725652,-4.367450,6.599323,-2.781336,-4.718915,7.355196,-0.437674,3.074065,-4.906882,-7.525674,2.635406,4.291355,-7.078934,7.230755,-3.620793,-7.378181,-8.337445,-7.369549,-1.001447,1.694832,-2.168917,-4.681417,0.260590,4.950429,-3.546803,-1.765092,2.174138,2.332330,0.901366,6.962308,9.035898,4.669928,1.724998,-6.921414,5.395013,-1.775105,-5.299207,-1.262464,-1.807664,5.736329,3.169489,2.628789,2.459137,2.648090,6.758341,8.093813,-8.421650,-6.503432,-2.610645,9.579261,-0.171767,6.400109,7.526251,7.710844,-7.417790,-7.068569,-1.966775,-5.444896,-8.355564,-0.287220,-0.481488,6.496770,-6.545521,-6.164684,-0.781493,-7.968855,4.913700,1.118798,2.837859,1.025320,-1.666057,-4.033292,7.109746,-6.116336,-1.274656,3.994652,-7.151396,3.126621,-8.604492,9.724063,4.350366,2.015510,-1.753769,1.384427,6.984864,6.141027,6.276883,-8.849644,-6.796151,-4.482777,3.503536,1.384314,-3.302394,4.707462,5.468319,0.554706,-9.717828,2.744198,-9.213393,0.661305,3.459076,0.618627,-9.756925,0.978861,-9.241830,8.736704,0.384698,-4.096129,1.102521,-9.708877,-7.535117,7.376337,6.015618,4.327261,-3.126919,7.251392,1.914506,-5.340569,6.938110,-3.372438,4.817038,9.103927,1.063720,1.119507,9.226423,7.220763,1.196201,8.651854,7.010715,-8.491548,8.117146,-8.354749,-1.761243,-9.005048,-3.064154,-9.572275,-0.515557,4.019646,0.177326,-5.029003,-2.922467,-9.066583,-0.462545,-2.981673,6.835541,5.826915,0.211187,2.184498,-3.635353,0.391271,3.383822,6.437574,3.678518,7.815151,6.685106,-9.636954,1.106032,5.108135,-3.500361,5.002580,7.383914,-3.000330,-6.562406,-4.612552,5.248637,-7.449343,4.984070,-6.863176,-6.995839,1.404250,3.840715,9.515444,0.619453,-2.619345,5.554702,8.717421,5.399700,1.052260,1.633969,-6.031643,0.855658,0.402115,-3.709565,4.107801,6.598397,-2.372454,-6.121092,4.074730,1.226315,3.765117,-3.963221,7.847568,-7.092715,3.666076,-8.651120,-7.274016,-8.373614,5.374129,3.626506,8.059069,4.289808,8.903346,-9.298852,6.102299,1.098317,-3.790037,6.566019,9.611026,-7.966690,-1.719496,-0.817875,-5.295467,-7.586639,-6.763973,-6.622174,7.608562,2.973809,-6.792236,7.579491,9.089112,-6.699344,-0.875499,2.409348,-9.671748,9.824564,2.469271,4.547093,-3.589558,8.809094,-6.967177,4.415568,4.850616,-1.108015,-3.024871,-8.045331,-0.147358,4.794103,-5.186051,-7.558274,-2.115067,0.353077,-1.547650,3.335270,6.553587,9.720258,-9.947020,0.890993,6.561236,9.968516,4.530968,-0.009743,1.799487,3.665717,-9.791239,-1.154852,4.480718,-6.037941,-4.598777,-1.659817,-8.005272,5.468265,-3.532191,2.429045,6.044065,8.656184,-4.076862,-7.877044,2.865815,3.172743,-0.521924,-2.756412,-1.714109,7.521409,-2.216836,-5.760363,3.155568,-4.832016,-3.830603,7.946978,-8.567838,-2.582776,-2.824244,-3.420224,-7.384488,-3.684562,3.876821,-1.871693,1.652517,8.126715,-9.150761,9.740121,7.817348,8.814305,5.047988,3.520096,-1.112210,-7.823522,8.337108,-1.312367,-9.000758,-6.296653,-5.678787,0.225561,-3.713755,7.582480,-4.789045,-2.131046,-7.865700,5.736421,-2.481070,-0.866490,0.385978,-0.978321,2.929696,-1.351868,9.837088,-4.665082,-4.331103,2.227330,-1.097575,6.478417,1.403409,-0.863305,9.041801,7.341585,9.400400,-6.758280,-9.565743,6.976752,-4.946633,-8.105310,-6.400595,5.951368,-5.400190,4.494291,1.579091,-7.271060,-1.234321,2.831133,-4.390177,2.152404,-1.537195,-5.246690,-6.210034,-9.605371,-0.442011,-4.492874,7.797283,4.666841,8.511914,-0.873314,1.104529,1.916382,-6.799374,5.071212,-0.855417,-5.713885,3.904068,7.369517,-7.746395,-3.658882,-9.666293,9.831570,-4.129555,-4.175664,7.771481,-7.933734,9.166613,-2.441353,-0.716460,-5.734329,-3.115393,9.362261,-8.088081,-5.302038,9.985503,2.260801,4.210813,0.494270,3.563320,1.297422,7.731503,5.181658,-8.799654,-6.582494,1.495000,3.341040,9.089863,0.081885,2.682126,-3.347990,-4.442167,5.289324,-5.751870,2.758437,-8.350554,-8.358882,3.514518,-4.151324,4.337951,-8.886962,3.959538,-8.294127,9.050350,-1.713214,2.501433,8.710947,-1.524387,-2.145924,9.949631,-7.128595,-3.259144,1.051385,-8.346000,9.825684,-9.688971,3.585194,7.315868,-4.576952,7.076546,-2.107517,9.773333,5.458813,-8.253931,-3.504297,1.311351,1.525199,4.157215,6.230283,-3.070224,9.189619,6.579034,-5.929721,5.679924,3.660619,-7.390305,5.277049,6.181166,0.621606,-9.957492,8.491465,7.390184,-5.764056,-0.969228,-3.669906,-3.235880,2.733180,-1.085122,8.112720,4.643206,3.614779,-1.227652,3.549900,7.068721,7.969936,4.372725,9.109705,3.361453,5.652796,-6.205009,-4.860716,-3.690509,-6.835431,7.608132,-5.351814,-9.318417,-5.136838,-1.322068,-3.842230,6.229538,-3.635237,-6.061049,4.037848,6.787696,1.339864,-7.627812,-8.912405,-9.491180,-3.619746,-1.222385,-8.693178,-5.174859,1.465250,-6.469181,-5.089816,8.705492,-7.876068,-9.631945,9.189714,4.311502,6.789374,-4.523460,-4.230920,-0.134189,8.453835,2.872055,3.241639,-3.551952,-1.411329,-3.951447,-3.343252,9.471571,-6.385496,-9.200490,5.732226,-7.597275,-3.006164,6.519986,1.936723,9.838126,-6.548784,-0.207503,-9.449943,4.992799,-7.731217,2.011376,8.193937,2.325894,-9.203951,-2.096244,6.639453,7.497491,7.617202,-6.802224,-8.328792,5.068148,-3.453711,6.897644,6.974129,-6.426616,-3.720562], dtype = "float32")#candidate|3584|(1792,)|const|float32
call_3582 = relay.TupleGetItem(func_3367_call(relay.reshape(var_3583.astype('float64'), [12, 14, 14]), relay.reshape(const_3584.astype('float32'), [1792,]), ), 0)
call_3585 = relay.TupleGetItem(func_3370_call(relay.reshape(var_3583.astype('float64'), [12, 14, 14]), relay.reshape(const_3584.astype('float32'), [1792,]), ), 0)
output = relay.Tuple([call_3518,const_3534,bop_3548,bop_3556,call_3569,const_3570,call_3573,const_3574,call_3582,var_3583,const_3584,])
output2 = relay.Tuple([call_3519,const_3534,bop_3551,bop_3559,call_3571,const_3570,call_3575,const_3574,call_3585,var_3583,const_3584,])
func_3589 = relay.Function([var_3535,var_3555,var_3583,], output)
mod['func_3589'] = func_3589
mod = relay.transform.InferType()(mod)
var_3590 = relay.var("var_3590", dtype = "int32", shape = (525, 3))#candidate|3590|(525, 3)|var|int32
var_3591 = relay.var("var_3591", dtype = "int32", shape = (7, 15, 15))#candidate|3591|(7, 15, 15)|var|int32
var_3592 = relay.var("var_3592", dtype = "float64", shape = (2352,))#candidate|3592|(2352,)|var|float64
output = func_3589(var_3590,var_3591,var_3592,)
func_3593 = relay.Function([var_3590,var_3591,var_3592,], output)
mutated_mod['func_3593'] = func_3593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3021_call = mod.get_global_var('func_3021')
func_3022_call = mutated_mod.get_global_var('func_3022')
call_3603 = func_3021_call()
call_3604 = func_3021_call()
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
var_3613 = relay.var("var_3613", dtype = "float32", shape = (308, 1))#candidate|3613|(308, 1)|var|float32
call_3612 = relay.TupleGetItem(func_3316_call(relay.reshape(var_3613.astype('float32'), [11, 4, 7])), 0)
call_3614 = relay.TupleGetItem(func_3318_call(relay.reshape(var_3613.astype('float32'), [11, 4, 7])), 0)
func_2602_call = mod.get_global_var('func_2602')
func_2604_call = mutated_mod.get_global_var('func_2604')
call_3628 = relay.TupleGetItem(func_2602_call(relay.reshape(var_3613.astype('float32'), [308, 1])), 0)
call_3629 = relay.TupleGetItem(func_2604_call(relay.reshape(var_3613.astype('float32'), [308, 1])), 0)
output = relay.Tuple([call_3603,call_3612,var_3613,call_3628,])
output2 = relay.Tuple([call_3604,call_3614,var_3613,call_3629,])
func_3632 = relay.Function([var_3613,], output)
mod['func_3632'] = func_3632
mod = relay.transform.InferType()(mod)
var_3633 = relay.var("var_3633", dtype = "float32", shape = (308, 1))#candidate|3633|(308, 1)|var|float32
output = func_3632(var_3633)
func_3634 = relay.Function([var_3633], output)
mutated_mod['func_3634'] = func_3634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_3641 = relay.TupleGetItem(func_2027_call(), 0)
call_3642 = relay.TupleGetItem(func_2029_call(), 0)
output = relay.Tuple([call_3641,])
output2 = relay.Tuple([call_3642,])
func_3691 = relay.Function([], output)
mod['func_3691'] = func_3691
mod = relay.transform.InferType()(mod)
mutated_mod['func_3691'] = func_3691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3691_call = mutated_mod.get_global_var('func_3691')
call_3692 = func_3691_call()
output = call_3692
func_3693 = relay.Function([], output)
mutated_mod['func_3693'] = func_3693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2864_call = mutated_mod.get_global_var('func_2864')
call_3694 = func_2863_call()
call_3695 = func_2863_call()
output = relay.Tuple([call_3694,])
output2 = relay.Tuple([call_3695,])
func_3698 = relay.Function([], output)
mod['func_3698'] = func_3698
mod = relay.transform.InferType()(mod)
mutated_mod['func_3698'] = func_3698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3698_call = mutated_mod.get_global_var('func_3698')
call_3699 = func_3698_call()
output = call_3699
func_3700 = relay.Function([], output)
mutated_mod['func_3700'] = func_3700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_3737 = relay.TupleGetItem(func_2027_call(), 1)
call_3738 = relay.TupleGetItem(func_2029_call(), 1)
func_3394_call = mod.get_global_var('func_3394')
func_3397_call = mutated_mod.get_global_var('func_3397')
var_3742 = relay.var("var_3742", dtype = "uint16", shape = (520,))#candidate|3742|(520,)|var|uint16
call_3741 = func_3394_call(relay.reshape(var_3742.astype('uint16'), [4, 13, 10]))
call_3743 = func_3394_call(relay.reshape(var_3742.astype('uint16'), [4, 13, 10]))
output = relay.Tuple([call_3737,call_3741,var_3742,])
output2 = relay.Tuple([call_3738,call_3743,var_3742,])
func_3749 = relay.Function([var_3742,], output)
mod['func_3749'] = func_3749
mod = relay.transform.InferType()(mod)
mutated_mod['func_3749'] = func_3749
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3750 = relay.var("var_3750", dtype = "uint16", shape = (520,))#candidate|3750|(520,)|var|uint16
func_3749_call = mutated_mod.get_global_var('func_3749')
call_3751 = func_3749_call(var_3750)
output = call_3751
func_3752 = relay.Function([var_3750], output)
mutated_mod['func_3752'] = func_3752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2864_call = mutated_mod.get_global_var('func_2864')
call_3782 = func_2863_call()
call_3783 = func_2863_call()
output = call_3782
output2 = call_3783
func_3798 = relay.Function([], output)
mod['func_3798'] = func_3798
mod = relay.transform.InferType()(mod)
mutated_mod['func_3798'] = func_3798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3798_call = mutated_mod.get_global_var('func_3798')
call_3799 = func_3798_call()
output = call_3799
func_3800 = relay.Function([], output)
mutated_mod['func_3800'] = func_3800
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3801 = relay.var("var_3801", dtype = "int16", shape = ())#candidate|3801|()|var|int16
var_3802 = relay.var("var_3802", dtype = "int16", shape = (16, 1, 13))#candidate|3802|(16, 1, 13)|var|int16
bop_3803 = relay.greater_equal(var_3801.astype('bool'), var_3802.astype('bool')) # shape=(16, 1, 13)
var_3812 = relay.var("var_3812", dtype = "int16", shape = (16, 8, 13))#candidate|3812|(16, 8, 13)|var|int16
bop_3813 = relay.floor_divide(var_3802.astype('float32'), var_3812.astype('float32')) # shape=(16, 8, 13)
uop_3821 = relay.atan(var_3802.astype('float32')) # shape=(16, 1, 13)
bop_3830 = relay.bitwise_xor(bop_3813.astype('uint16'), relay.reshape(var_3812.astype('uint16'), relay.shape_of(bop_3813))) # shape=(16, 8, 13)
uop_3839 = relay.log10(uop_3821.astype('float64')) # shape=(16, 1, 13)
uop_3845 = relay.erf(uop_3839.astype('float64')) # shape=(16, 1, 13)
func_1699_call = mod.get_global_var('func_1699')
func_1702_call = mutated_mod.get_global_var('func_1702')
const_3857 = relay.const([-7.749041,-1.655920,-8.110699,-8.176379,-1.905267,0.100469,-2.934528,-9.677648,-3.425625,9.363739,-9.031385,3.025186,8.339150,5.910502,-3.799863,-0.353408,1.105791,-6.431901,-7.306823,-1.411190,8.837779,-5.640770,8.426559,8.807798,4.584141,-3.465206,0.169985,5.938437,-0.986799,3.453147,1.324800,8.336335,8.057481,5.897092,-0.016964,-1.035231,7.795002,4.297548,7.702755,-0.460331,-3.627927,-7.438950,-3.600615,-3.927684,-3.584616,5.607078,2.893380,0.295597,-3.919174,-8.457896,-1.668534,5.166309,9.274327,-7.832504,4.697825,-5.031662,-2.599107,0.152401,-2.394826,0.741658,6.565599,-4.169882,1.560347,4.326908,-5.778330,-0.836196,-6.490475,-3.827382,-1.279816,9.953825,-7.684537,0.256918,-5.032848,6.153004,5.056049,-3.639586,-2.050714,4.146900,-4.062618,4.161308,3.579666,1.952713,6.284704,8.330777,-2.191261,7.713142,-5.423702,2.843896,6.795523,1.224389,9.349584,-3.758407,0.083791,6.056333,-1.716017,-5.021848,-3.469291,-7.326331,-9.337187,-5.511715,-5.241318,4.610138,-6.159043,2.461552,9.160723,-7.766901,-1.034341,-5.041008,9.410530,9.913861,3.400222,4.953470,1.216100,7.412692,3.516642,6.049661,-8.960431,8.370624,4.417654,-5.781336,8.327594,-0.781772,6.285063,8.252473,-9.141035,8.492576,9.108249,-1.743132,-4.657009,-0.377242,4.092906,0.204044,-4.130848,-8.040402,5.559065,-9.508634,-9.379383,5.058270,-4.490659,-7.981664,5.813391,-1.802540,-9.784027,-9.775642,-9.294185,-9.777407,-3.477930,7.467000,-1.721407,-4.852843,6.194334,8.968369,7.599587,8.669595,3.953111,1.628204,6.463149,3.587304,-9.462385,-3.212139,-9.115405,-4.231904,-5.907123,5.517082,9.971066,8.435944,3.006408,-0.359452,1.087601,-9.058265,8.169670,6.491160,2.778981,-5.685850,-5.247798,-9.415004,-4.273137,7.503108,6.143720,2.427406,3.497527,2.867938,2.886402,6.689678,5.537104,-3.363688,9.885513,-5.715684,-5.824807,-6.677756,9.282278,-1.207383,0.757253,5.506900,-3.450748,-6.736219,8.259573,-0.344787,1.161521,2.056980,3.280483,-9.409374,1.972640,9.416269,1.025838,6.980179,2.659081,-2.700231,7.650775,8.138063,2.802613,1.402820,8.952133,9.107109,-3.247874,4.058025,-1.004872,-8.242428,-1.697768,-5.896555,-0.368196,6.535104,1.277517,-5.972900,3.589065,-2.959760,4.572903,1.523874,-9.591973,-0.497645,2.038777,-1.024351,3.557992,4.025581,0.622646,6.574899,5.918277,8.284714,7.960425,-6.814868,2.219489,5.359774,-4.735675,5.810324,3.103814,7.783087,6.588109,9.418263,3.624991,8.335717,-3.623689,-4.268358,3.381004,-4.506572,4.832613,4.702965,9.595853,-8.471571,0.101588,-4.670589,7.492926,4.644081,-2.506970,6.586718,5.558008,-0.624291,8.299702,-6.579714,-3.990745,5.274550,5.209593,-3.155453,0.665746,-4.047768,-1.513623,-3.128239,9.371204,-2.234359,-8.699526,9.503904,-7.750750,8.301273,-0.845545,-5.062962,-9.859522,-3.826658,-1.707467,-7.037926,1.346640,-1.497122,-8.727702,8.190459,-8.520067,9.848705,1.472246,5.870755,-2.667706,-0.489643,-5.971595,9.511037,-1.418758,-1.881025,-8.359185,0.012319,7.808630,2.468103,-6.846250,7.415376], dtype = "float32")#candidate|3857|(308,)|const|float32
call_3856 = relay.TupleGetItem(func_1699_call(relay.reshape(const_3857.astype('float32'), [11, 4, 7])), 0)
call_3858 = relay.TupleGetItem(func_1702_call(relay.reshape(const_3857.astype('float32'), [11, 4, 7])), 0)
func_2674_call = mod.get_global_var('func_2674')
func_2678_call = mutated_mod.get_global_var('func_2678')
const_3861 = relay.const([-4,6,-10,-1,-7,7,-2,-4,-6,1,6,7,3,-3,6,6,-5,-9,-5,-7,5,-10,-2,7,3,-1,-3,10,8,10,-9,1,-1,8,-5,10,-8,9,5,10,-6,-9,-1,-7,-2,10,5,5,6,-4,8,-10,-6,-8,7,-1,9,1,10,-9,-7,6,-4,10,4,-8,-9,1,-9,8,-7,6,10,-7,5,5,-7,-4,9,1,-9,8,-7,-5,7,2,-2,-3,-8,-1,8,-7,-6,-8,-4,-10,7,-2,8,1,-9,-3,-3,-3,7,-6,-9,-2,3,-2,8,-1,-2,1,8,-5,-5,10,-5,1,-7,8,7,3,-1,-8,-8,6,-1,10,-9,8,3,3,3,1,10,-5,1,-6,2,-3,-2,10,8,-3,-7,2,-3,10,-9,-3,10,6,8,6,-8,2,-2,3,6,-6,1,3,-2,-9,3,2,1,-7,-1,-1,-3,-9,9,4,10,-6,-7,4,-3,-2,4,-10,-3,-6,-1,3,1,-1,-4,6,7,4,3,5,10,2,3,-10,10,-1,2,9,4,6,6,-1,-5,7,4,4,9,-7,-8,9,3,-3,1,-2,1,-4,-3,-2,-1,-8,10,8,-8,4,-4,-5,2,-3,9,10,7,-9,-1,9,-9,-7,-7,-10,2,2,-4,2,-7,9,-2,8,-2,-8,-9,5,1,8,-6,6,10,-3,-5,2,-10,7,-9,1,-3,4,-5,-1,2,-8,-6,6,2,-2,-4,8,5,-8,-2,6,8,-9,-1,-3,10,1,6,3,9,-5,-10,-9,-2,-1,-3,-2,-9,6,-3,-4,2,10,5,6,-1,-6,-5,7,-1,-2,7,5,-8,7,4,6,-7,4,2,-7,-2,-3,10,-4,10,3,-3,3,-3,-3,-4,-3,-3,-2,-6,7,3,-6,-4,2,-8,1,-5,-1,9,-5,10,3,-2,10,5,7,1,-9,-4,9,3,-3,8,-7,7,7,10,5,-4,-2,-6,5,2,2,-4,-8,-3,-7,5,8,-8,3,7,-9,-7,-2,-10,10,-2,6,5,2,4,-1,-3,-3,5,6,6,-7,-6,5,5,-8,8,-2,9,-1,3,-4,-10,-7,4,1,1,-2,6,-5,-3,-7,-8,-3,2,9,-5,-2,-1,4,-4,-5,2,2,-5,8,-9,-8,-3,-1,5,10,5,7,-1,-1,-5,-8,2,-4,6,-4,6,-1,10,-1,3,7,3,6,-4,-7,-1,-7,-6,9,-2,8,-2,-4,-10,-1,8,3,-1,-5,3,-5,6,7,-2,3,-9,9,-9,-8,-10,4,-7,9,-5,7,8,-4,6,6,10,-2,-2,4,6,2,3,5,-2,-9,1,-7,-8,3,2,1,-3,-5,-6,8,-1,9,4,-3,10,-3,8,8,-1,-7,2,-7,1,-10,2,-10,-8,-6,-4,-9,3,-3,-2,-4,-4,7,8,-3,-7,7,-10,-2,-7,1,1,4,-3,-2,10,9,-8,-1,10,9,-6,-9,-3,-7,1,-2,9,6,-2,9,6,-7,-2,-5,4,-2,-10,1,3,-6,9,7,-3,-1,3,1,6,6,-8,-2,2,-7,6,8,7,4,-1,5,3,-10,-6,6,9,-9,2,1,7,8,7,1,-9,9,5,3,10,4,2,-7,3,-8,-9,-3,-9,10,-9,8,-5,8,-5,-7,4,-2,-3,-7,-6,5,8,-4,1,10,4,-9,-9,10,-8,8,10,10,8,2,-6,3,-7,8,-10,9,8,-4,5,-8,1,-8,-5,-4,6,1,7,6,9,-1,2,-5,-7,7,3,8,-5,-4,-3,-5,8,-2,8,-8,-2,7,8,6,1,9,3,9,-2,-8,5,5,-9,-8,-5,-7,-3,4,-6,-9,8,-2,-5,-8,-6,-1,4,-4,-5,2,-7,8,3,5,4,8,-2,-4,-3,-4,-1,-10,3,7,-6,-7,-8,-7,8,-2,-4,4,-3,2,1,7,-3,8,-10,-1,6,1,4,6,-8,4,-9,1,-9,9,1,3,-2,-7,5,-1,9,-6,-10,2,-3,3,7,5,6,-5,10,10,-8,-6,-6,-6,1,-7,6,-10,-8,-10,-6,10,-1,-9,-4,2,-6,4,7,9,4,10,5,-7,-4,7,-4,-6,-3,-5,-3,-8,-7,-5,4,4,-7,-8,-6,-5,-3,-2,1,-3,2,3,5,8,-6,6,-4,10,5,-4,-4,-3,1,-6,-3,9,5,5,-5,-3,4,3,-2,-9,-10,9,-2,-10,8,-7,3,10,-10,-9,6,8,-3,-7,-3,-3,-9,-8,3,-6,-4,-5,1,-8,-8,7,-10,3,-5,8,7,2,4,-7,-8,9,7,10,7,2,4,9,-4,7,3,7,7,-5,9,-7,6,6,1,-5,3,-4,-7,-3,7,2,7,1,-9,6,-10,-5,-10,4,-9,10,4,-1,8,2,5,-5,-3,8,-3,-2,-7,1,-7,1,-2,10,-4,9,-6,-7,-4,3,9,3,-8,-4,3,-4,-2,6,5,-2,-8,1,1,-5,10,-6,1,-10,-6,4,4,10,5,10,4,9,4,-6,-7,1,8,8,-9,-8,5,-2,2,-4,8,6,-7,-5,-6,5,-9,3,-6,-7,-9,7,7,-4,-3,-5,-4,4,8,2,8,7,6,7,1,6,-6,-6,4,1,8,-8,-9,-4,2,10,5,-9,9,4,9,10,3,-10,5,2,-9,4,3,-4,-3,-6,4,-1,1,-1,-5,6,8,-5,-7,-6,7,4,-7,-6,-3,-1,8,-9,9,-9,-2,10,-9,3,-2,-2,-9,1,-5,10,-9,-6,-5,6,-7,-6,-8,-1,3,-2,-4,-6,-1,1,-5,-5,-4,-9,-5,2,-10,3,7,4,9,-9,-2,-8,-3,8,-1,-10,3,-3,6,2,-4,-3,-10,-2,-3,-4,7,8,10,-8,1,8,-1,4,-4,3,-3,8,-3,2,3,-3,-7,-10,8,-10,8,-5,-6,-6,7,-8,-6,-4,9,7,2,-2,-10,8,2,9,7,-7,-4,5,2,2,2,-9,1,-4,-5,-4,1,-6,-9,1,8,-8,2,-4,9,-4,-9,3,-10,-5,-3,3,10,-7,4,-6,7,-7,-7,5,6,-6,-6,-6,-6,-5,-9,-5,8,9,-1,8,-9,8,7,-4,7,-7,1], dtype = "int64")#candidate|3861|(1183,)|const|int64
call_3860 = relay.TupleGetItem(func_2674_call(relay.reshape(call_3856.astype('float32'), [11, 4, 7]), relay.reshape(const_3861.astype('int64'), [91, 13]), ), 9)
call_3862 = relay.TupleGetItem(func_2678_call(relay.reshape(call_3856.astype('float32'), [11, 4, 7]), relay.reshape(const_3861.astype('int64'), [91, 13]), ), 9)
output = relay.Tuple([bop_3803,bop_3830,uop_3845,call_3856,const_3857,call_3860,const_3861,])
output2 = relay.Tuple([bop_3803,bop_3830,uop_3845,call_3858,const_3857,call_3862,const_3861,])
func_3864 = relay.Function([var_3801,var_3802,var_3812,], output)
mod['func_3864'] = func_3864
mod = relay.transform.InferType()(mod)
mutated_mod['func_3864'] = func_3864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3864_call = mutated_mod.get_global_var('func_3864')
var_3866 = relay.var("var_3866", dtype = "int16", shape = ())#candidate|3866|()|var|int16
var_3867 = relay.var("var_3867", dtype = "int16", shape = (16, 1, 13))#candidate|3867|(16, 1, 13)|var|int16
var_3868 = relay.var("var_3868", dtype = "int16", shape = (16, 8, 13))#candidate|3868|(16, 8, 13)|var|int16
call_3865 = func_3864_call(var_3866,var_3867,var_3868,)
output = call_3865
func_3869 = relay.Function([var_3866,var_3867,var_3868,], output)
mutated_mod['func_3869'] = func_3869
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3877 = relay.var("var_3877", dtype = "uint64", shape = ())#candidate|3877|()|var|uint64
var_3878 = relay.var("var_3878", dtype = "uint64", shape = (7, 1, 10))#candidate|3878|(7, 1, 10)|var|uint64
bop_3879 = relay.add(var_3877.astype('uint64'), var_3878.astype('uint64')) # shape=(7, 1, 10)
output = bop_3879
output2 = bop_3879
func_3887 = relay.Function([var_3877,var_3878,], output)
mod['func_3887'] = func_3887
mod = relay.transform.InferType()(mod)
var_3888 = relay.var("var_3888", dtype = "uint64", shape = ())#candidate|3888|()|var|uint64
var_3889 = relay.var("var_3889", dtype = "uint64", shape = (7, 1, 10))#candidate|3889|(7, 1, 10)|var|uint64
output = func_3887(var_3888,var_3889,)
func_3890 = relay.Function([var_3888,var_3889,], output)
mutated_mod['func_3890'] = func_3890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2903_call = mod.get_global_var('func_2903')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_3936 = relay.TupleGetItem(func_2903_call(), 2)
call_3937 = relay.TupleGetItem(func_2904_call(), 2)
func_2916_call = mod.get_global_var('func_2916')
func_2917_call = mutated_mod.get_global_var('func_2917')
call_3945 = func_2916_call()
call_3946 = func_2916_call()
func_3632_call = mod.get_global_var('func_3632')
func_3634_call = mutated_mod.get_global_var('func_3634')
const_3950 = relay.const([-5.463962,8.014598,0.591737,-0.839655,-5.785037,2.417996,-6.974304,-3.433886,6.587493,-3.125748,-0.433457,9.219532,1.572055,-7.946268,-5.224410,-5.760607,-8.637234,-1.094495,-4.867803,0.358009,-8.269555,-3.276025,-6.187006,9.523980,-5.054293,7.750033,9.562931,-3.791608,-4.383970,4.497514,8.096303,8.535535,7.935417,1.688405,-4.336737,-1.461956,5.396075,8.977803,-7.422273,5.800271,-4.368904,6.232054,6.427216,4.233957,-1.826676,-9.537752,-2.479361,-8.543759,4.169931,5.547715,-1.394149,-1.322724,-8.698064,-5.333333,8.638760,9.575189,-6.059909,4.476677,-4.848473,3.269237,0.189194,7.524192,7.505055,7.855005,3.918105,-6.749575,-6.917385,-3.418542,-3.610989,4.594657,-1.031164,-5.669534,-1.327452,7.530351,-0.150593,3.875870,-8.225694,8.500414,-3.448532,8.088678,8.512936,-5.756851,-7.028097,-5.888574,2.967840,-1.480633,-6.138396,-4.474635,-5.556997,-1.576542,1.515634,-4.377376,-1.370957,5.711143,-9.453900,-0.711629,7.225033,-7.301536,0.398433,-5.718223,-4.765528,3.385902,8.659788,8.107219,3.058645,-7.257994,-4.582908,-0.450650,-9.114065,1.860834,-0.183695,-8.011475,-8.706129,-5.272766,9.815914,-5.694830,6.460342,3.954836,-7.074282,0.512106,-2.534721,-8.989726,-0.583604,9.846068,-5.166736,-1.067533,-7.448030,-9.455934,0.283299,1.959138,-6.690547,-7.451746,9.633671,-5.851359,8.200663,3.550213,-3.271460,-1.482373,-2.174844,1.338297,-0.460072,-8.626351,6.097976,-0.053223,0.230870,6.474684,9.120237,3.148811,9.940098,-3.144810,9.037411,-1.982045,8.223731,3.038920,-4.898235,1.713696,-1.003478,-9.269647,-1.452812,-0.189977,-5.655339,2.649026,3.136940,-2.590668,3.728317,2.806456,-3.140078,-1.106461,-0.390449,0.525263,-5.643303,-2.157100,-8.017158,-7.536032,0.721277,-4.011096,2.369877,6.186956,6.473645,4.443830,7.667320,1.611939,9.829379,5.845567,5.947854,-8.569188,4.987950,-9.599848,6.238947,8.700431,2.187256,-8.806306,8.261079,-8.696795,6.260262,5.184912,-9.157662,-5.836026,-8.545670,-7.008068,9.497372,-4.241264,8.026784,-3.427202,8.727732,3.950829,-7.638836,3.286602,2.318188,-7.065589,-1.180761,9.601136,-3.884169,-6.019529,-7.779921,5.494453,8.390287,-2.974296,-9.680971,-3.182091,-8.509328,5.191110,8.726846,4.059553,-4.863295,-8.235795,5.547390,4.934526,4.647480,7.308924,-9.347641,4.633594,-2.649161,-4.032520,0.903351,-9.028876,-0.976060,-7.732995,8.930582,2.168300,5.413708,-5.981163,3.477576,-1.236342,7.258395,-1.180189,-0.785776,1.714236,-7.283029,-8.612564,-4.184120,4.074218,-3.031105,5.713004,2.029104,2.658817,-8.692402,-2.183036,4.087574,-8.944309,-8.551670,5.938988,5.204281,8.433076,-3.145333,8.951265,-3.534233,-4.949188,-8.959617,-8.227141,-5.245145,-1.811247,5.768094,-5.844675,8.670348,7.633079,-2.734396,0.983832,-6.593399,7.764922,-0.728230,4.275009,5.150497,1.308937,8.102081,-1.105761,2.695933,-2.334585,5.222399,3.828799,-2.604274,-1.082167,8.164500,-4.547133,-8.992186,4.174575,-3.951379,5.064647,-6.843549,8.700653,2.344062,3.743083,-0.850914,7.533704,-4.258940,-9.687089,-7.889871,1.640460], dtype = "float32")#candidate|3950|(308,)|const|float32
call_3949 = relay.TupleGetItem(func_3632_call(relay.reshape(const_3950.astype('float32'), [308, 1])), 2)
call_3951 = relay.TupleGetItem(func_3634_call(relay.reshape(const_3950.astype('float32'), [308, 1])), 2)
func_2233_call = mod.get_global_var('func_2233')
func_2237_call = mutated_mod.get_global_var('func_2237')
var_3958 = relay.var("var_3958", dtype = "float64", shape = (2304,))#candidate|3958|(2304,)|var|float64
const_3959 = relay.const([1.428280,-0.774706,0.719730,-2.629162,6.188814,5.014667,9.079807,-1.089336,-3.976306,-5.671797,7.621323,-0.221025,-5.034799,-8.518035,-9.872459,-3.918678,-9.784726,6.967832,0.421232,-4.559569,-9.867399,0.071569,-0.566312,-9.433333,2.346534,-7.988928,-7.657828,-8.499435,-6.941423,-9.066651,-7.985301,-9.642110,-1.602046,-0.831613,2.662205,-4.641414,-6.279355,8.275815,7.113897,9.991548,0.353001,1.263175,-3.482235,-9.602196,9.148745,-3.379213,7.583050,-3.564564,-2.307811,2.334289,1.337588,0.494480,0.124261,0.906084,-7.578552,-1.940047,-5.504143,2.217865,0.214821,3.376934,-7.331987,5.209991,-5.687924,1.296510,-4.822195,9.733064,-2.129226,-2.109550,5.024806,9.479884,-5.525373,8.351518,1.035121,-3.215927,-4.200529,5.861605,8.534579,4.258166,-0.308301,-0.858674,5.174069,3.728813,-9.659274,-3.928612,4.090147,7.143764,6.080081,-8.965438,0.306104,6.688315,-8.137048,-1.411695,6.130960,5.513432,3.002525,0.272813,9.008725,-4.821225,-1.605183,-3.645487,-8.031605,2.871082,-5.556272,9.619023,-0.235929,-0.126518,0.480923,-1.053034,-4.546792,3.642109,6.565315,-4.719978,1.812901,-4.078967,9.693992,0.264166,-0.860454,4.987438,-3.557051,-8.317491,-3.749159,3.661259,-4.618557,-1.949136,1.273043,-3.995964,-4.110645,-6.462585,7.081802,8.560239,5.518565,9.282182,-3.782999,-3.133950,6.939621,9.037468,5.975408,6.524797,3.001031,-6.375067,9.793644,7.386924,-0.531042,1.898650,8.818548,-1.059899,4.484778,-8.891014,8.115536,-9.602817,-2.583218,-6.942586,-1.528363,1.977729,9.633285,0.741786,-5.444808,4.504271,-6.111108,-9.746115,8.015394,-3.509976,-5.911861,-9.034884,9.872369,-7.034107,4.673575,-2.100294,3.569873,9.739253,5.832130,5.340925,5.777683,-4.162339,-5.697718,7.407240,-0.945524,-7.340956,9.181179,-4.087445,-9.467347,-2.405713,7.740138,3.272869,-0.167322,3.714613,1.723655,0.496349,5.693719,-3.547835,-8.301753,-1.447275,7.085859,-1.714365,9.767867,-6.844918,3.359015,4.667620,6.128637,5.783623,6.561568,9.542542,-0.408585,-7.915029,3.596918,1.855183,-4.748719,-7.681004,-4.055566,-7.539226,1.795599,5.371725,9.159224,5.482772,-9.132670,-7.401965,4.155808,-1.842787,-9.465403,-5.665839,-2.729753,-9.834582,2.845001,-3.715860,9.106964,7.774008,8.021528,4.683414,-3.449301,8.271473,-5.731779,-2.076843,-1.728161,2.886283,3.592913,-0.442500,5.124618,8.598657,8.429085,-9.086415,-3.295584,6.824236,1.173108,0.311903,8.282992,-2.404097,-0.492347,9.384852,0.027179,-0.204112,-0.209798,-2.766343,1.556775,-0.016696,-4.932168,9.239869,5.552233,-6.110933,3.194211,-5.888858,9.085645,-7.972736,6.440447,-0.798799,-9.212468,-0.546002,5.108561,-6.101875,-1.547311,6.402368,-2.439581,4.536138,8.827879,-3.687003,4.989394,0.840693,3.142290,7.766092,7.844333,9.984971,-2.387211,3.571655,0.545879,-8.395319,-5.134663,-7.906288,-5.144480,-1.807441,0.077324,-0.536708,0.705704,5.978124,-9.206056,-2.373545,-2.096523,6.681860,2.113688,-3.926585,4.010487,-6.718856,-4.853870,-7.927377,-7.003357,-4.672325,6.104454,4.873266,-1.722232,2.307064,0.654115,5.968683,4.776338,-1.335562,6.539415,7.102395,6.325788,-0.245099,-0.460859,-2.584218,-3.144763,4.427855,7.964032,-6.265969,8.164540,-7.729393,7.985673,9.816563,3.973086,9.560328,-0.139652,5.566705,-1.548413,-8.305146,-0.166481,-5.293980,8.298162,-6.585205,-6.907466,3.645138,-3.219830,-3.747246,5.400515,-8.083043,4.488848,6.959346,9.755731,0.246091,-2.336768,-0.904630,-3.210366,5.927020,-3.036823,-7.901957], dtype = "float64")#candidate|3959|(352,)|const|float64
call_3957 = relay.TupleGetItem(func_2233_call(relay.reshape(var_3958.astype('float64'), [2304,]), relay.reshape(const_3959.astype('float64'), [8, 44]), ), 2)
call_3960 = relay.TupleGetItem(func_2237_call(relay.reshape(var_3958.astype('float64'), [2304,]), relay.reshape(const_3959.astype('float64'), [8, 44]), ), 2)
bop_3971 = relay.minimum(call_3949.astype('int64'), const_3959.astype('int64')) # shape=(308, 352)
bop_3974 = relay.minimum(call_3951.astype('int64'), const_3959.astype('int64')) # shape=(308, 352)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_3994 = relay.TupleGetItem(func_3316_call(relay.reshape(const_3950.astype('float32'), [11, 4, 7])), 0)
call_3995 = relay.TupleGetItem(func_3318_call(relay.reshape(const_3950.astype('float32'), [11, 4, 7])), 0)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
call_3999 = func_2745_call()
call_4000 = func_2745_call()
func_997_call = mod.get_global_var('func_997')
func_1000_call = mutated_mod.get_global_var('func_1000')
var_4016 = relay.var("var_4016", dtype = "float32", shape = (252,))#candidate|4016|(252,)|var|float32
call_4015 = relay.TupleGetItem(func_997_call(relay.reshape(call_3957.astype('float64'), []), relay.reshape(var_4016.astype('float32'), [252, 1]), ), 2)
call_4017 = relay.TupleGetItem(func_1000_call(relay.reshape(call_3957.astype('float64'), []), relay.reshape(var_4016.astype('float32'), [252, 1]), ), 2)
output = relay.Tuple([call_3936,call_3945,const_3950,call_3957,var_3958,bop_3971,call_3994,call_3999,call_4015,var_4016,])
output2 = relay.Tuple([call_3937,call_3946,const_3950,call_3960,var_3958,bop_3974,call_3995,call_4000,call_4017,var_4016,])
func_4018 = relay.Function([var_3958,var_4016,], output)
mod['func_4018'] = func_4018
mod = relay.transform.InferType()(mod)
var_4019 = relay.var("var_4019", dtype = "float64", shape = (2304,))#candidate|4019|(2304,)|var|float64
var_4020 = relay.var("var_4020", dtype = "float32", shape = (252,))#candidate|4020|(252,)|var|float32
output = func_4018(var_4019,var_4020,)
func_4021 = relay.Function([var_4019,var_4020,], output)
mutated_mod['func_4021'] = func_4021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2903_call = mod.get_global_var('func_2903')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_4124 = relay.TupleGetItem(func_2903_call(), 3)
call_4125 = relay.TupleGetItem(func_2904_call(), 3)
func_2233_call = mod.get_global_var('func_2233')
func_2237_call = mutated_mod.get_global_var('func_2237')
var_4137 = relay.var("var_4137", dtype = "float64", shape = (2304,))#candidate|4137|(2304,)|var|float64
var_4138 = relay.var("var_4138", dtype = "float64", shape = (4, 88))#candidate|4138|(4, 88)|var|float64
call_4136 = relay.TupleGetItem(func_2233_call(relay.reshape(var_4137.astype('float64'), [2304,]), relay.reshape(var_4138.astype('float64'), [8, 44]), ), 0)
call_4139 = relay.TupleGetItem(func_2237_call(relay.reshape(var_4137.astype('float64'), [2304,]), relay.reshape(var_4138.astype('float64'), [8, 44]), ), 0)
var_4154 = relay.var("var_4154", dtype = "float64", shape = (4, 88))#candidate|4154|(4, 88)|var|float64
bop_4155 = relay.add(var_4138.astype('float64'), relay.reshape(var_4154.astype('float64'), relay.shape_of(var_4138))) # shape=(4, 88)
const_4158 = relay.const([[-1.080514,-1.504324,0.742503,-8.098560,-4.696635,-8.620402,-4.215428,9.725373,-6.323015,-3.810698,-8.347500,2.425267,-0.880922,-2.768354,-6.072411,5.867954,5.502027,5.206731,0.920922,3.945341,4.844962,6.220591,-5.338881,8.597021,-9.428378,5.028672,8.173742,-5.271771,8.242736,-3.257205,0.046257,-4.122948,0.523937,1.211379,4.783655,-2.529635,-3.298805,-9.024738,-2.929417,-3.942153,2.120085,4.729182,-9.439330,6.057139,2.918353,-7.569081,4.688282,0.531929,-3.628384,7.296455,3.399864,-1.571252,-2.644724,-2.178529,-6.476600,8.943964,-8.907721,6.584671,-8.652168,3.231509,-8.019851,-6.240119,-2.764649,-2.541348,-3.248287,5.594345,3.038276,-4.798892,-8.809669,4.379256,9.160344,1.515038,5.166621,-4.625772,6.031630,6.803807,3.088440,1.567685,9.899582,-9.535546,-7.637680,-4.800193,-1.075919,4.858153,7.892859,7.542886,7.361123,9.485983],[8.043730,-6.766528,6.826680,-2.965387,-3.000293,-9.303531,4.669290,0.102824,-4.849003,-3.680769,-8.741998,-8.076442,-5.346669,-7.243259,-5.250958,-5.726569,-2.740121,-0.541100,6.768883,-0.535590,-1.538188,4.633918,-1.252810,8.983735,-7.770923,0.386210,9.633414,3.197421,4.363308,0.926230,1.780099,-1.212733,0.465700,9.052687,0.297169,-8.092466,-0.874157,-6.947459,-0.646930,-2.805411,4.884402,-4.652574,7.050971,-3.959837,5.807030,-4.386871,0.038301,-1.761636,9.348269,5.251337,-8.883315,-4.252432,-5.593496,6.233393,1.075312,3.145424,9.170415,7.756997,8.938839,9.250638,-5.356415,7.611729,-1.905134,-8.042548,4.565882,7.410494,8.745081,6.500870,-7.215710,-8.548841,-5.527018,-5.271871,5.508380,-9.799691,1.223333,-5.515615,8.156324,3.727624,7.854451,6.568889,-2.002825,-6.507474,-5.964064,5.379574,-1.450006,-0.411420,2.005620,-0.677133],[0.392621,-8.414086,1.765862,-3.469967,-4.221453,-9.058257,2.324474,5.144623,-7.214957,9.573561,8.029963,7.320370,-7.075102,-5.522775,-8.305240,7.887092,1.534413,-0.870961,-5.637536,5.071909,6.123799,-0.182656,9.298931,-3.926234,-4.024888,-0.561486,-3.425659,4.667103,-0.448758,-4.350640,6.470472,-6.836796,8.092174,3.983336,6.407260,4.122070,-2.513101,0.069197,9.083475,-1.917337,0.365582,7.420625,-4.443378,-4.698061,-0.516289,-3.769885,-2.335524,-1.151264,0.662847,9.133024,-4.800677,5.604518,8.652929,-0.669772,-9.986654,-3.194379,2.108465,6.879644,-1.691268,-0.170711,4.805399,-3.732842,9.652663,2.796224,-7.591591,6.180437,7.176429,-8.959605,2.881967,7.706185,9.431978,8.130493,1.029306,-2.197713,6.051758,-1.477185,5.157055,-7.144621,3.479922,-5.201658,4.942289,-7.494647,-3.423382,4.217538,0.477507,-4.972936,-1.573880,-2.536998],[-7.940672,2.417057,4.742166,-6.727761,7.403035,-9.695070,8.434289,-3.356545,-7.156753,8.475940,6.120943,8.410800,-5.458158,9.458768,6.985577,-5.617556,4.260767,4.032670,-0.927346,5.101942,0.184050,-2.927372,-0.867141,8.147782,-8.113195,-3.350422,5.433005,-4.624558,7.418736,-3.176288,9.627190,-5.529710,-4.799961,-9.499387,-3.988802,-3.712401,3.229153,-0.340959,-7.058983,-7.862468,-7.583499,-6.242811,-9.059702,7.118125,6.666118,2.812868,8.816652,7.020266,5.738855,-8.219589,0.995777,2.704227,7.086945,3.642882,6.493825,-5.056608,-1.009800,2.063783,-3.910126,-7.372889,-6.077712,-8.660650,8.500898,-1.128451,8.031971,-2.553669,7.433132,4.993995,0.851186,-4.888926,5.280524,3.993833,-7.411215,-0.210438,2.804807,-1.440417,-1.825161,3.308098,-0.378284,4.684438,-8.517824,-0.116633,2.555464,0.338415,-0.047772,-5.480357,-3.899131,1.854866]], dtype = "float64")#candidate|4158|(4, 88)|const|float64
bop_4159 = relay.logical_and(var_4154.astype('bool'), relay.reshape(const_4158.astype('bool'), relay.shape_of(var_4154))) # shape=(4, 88)
bop_4163 = relay.floor_divide(var_4154.astype('float64'), relay.reshape(var_4138.astype('float64'), relay.shape_of(var_4154))) # shape=(4, 88)
uop_4179 = relay.sin(bop_4155.astype('float32')) # shape=(4, 88)
output = relay.Tuple([call_4124,call_4136,var_4137,bop_4159,bop_4163,uop_4179,])
output2 = relay.Tuple([call_4125,call_4139,var_4137,bop_4159,bop_4163,uop_4179,])
func_4181 = relay.Function([var_4137,var_4138,var_4154,], output)
mod['func_4181'] = func_4181
mod = relay.transform.InferType()(mod)
mutated_mod['func_4181'] = func_4181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4181_call = mutated_mod.get_global_var('func_4181')
var_4183 = relay.var("var_4183", dtype = "float64", shape = (2304,))#candidate|4183|(2304,)|var|float64
var_4184 = relay.var("var_4184", dtype = "float64", shape = (4, 88))#candidate|4184|(4, 88)|var|float64
var_4185 = relay.var("var_4185", dtype = "float64", shape = (4, 88))#candidate|4185|(4, 88)|var|float64
call_4182 = func_4181_call(var_4183,var_4184,var_4185,)
output = call_4182
func_4186 = relay.Function([var_4183,var_4184,var_4185,], output)
mutated_mod['func_4186'] = func_4186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_4239 = relay.TupleGetItem(func_1839_call(), 2)
call_4240 = relay.TupleGetItem(func_1841_call(), 2)
output = call_4239
output2 = call_4240
func_4241 = relay.Function([], output)
mod['func_4241'] = func_4241
mod = relay.transform.InferType()(mod)
mutated_mod['func_4241'] = func_4241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4241_call = mutated_mod.get_global_var('func_4241')
call_4242 = func_4241_call()
output = call_4242
func_4243 = relay.Function([], output)
mutated_mod['func_4243'] = func_4243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
call_4244 = func_2745_call()
call_4245 = func_2745_call()
func_1292_call = mod.get_global_var('func_1292')
func_1296_call = mutated_mod.get_global_var('func_1296')
const_4257 = relay.const([[-6.724405,5.322617,-5.051259,5.821409],[-1.966333,0.377019,-5.407816,5.708977],[-0.666218,-5.494889,-5.177258,-2.444132],[-8.677986,-3.067247,-2.757296,7.078845],[2.174153,0.332886,-6.147629,7.621807],[0.423250,-6.544058,-2.000612,-9.906144],[-5.604666,-9.026400,8.694956,-9.676022],[-4.418411,-9.153623,8.307260,0.577833],[-5.244494,-4.383282,1.644204,1.956317]], dtype = "float64")#candidate|4257|(9, 4)|const|float64
var_4258 = relay.var("var_4258", dtype = "uint16", shape = (280,))#candidate|4258|(280,)|var|uint16
const_4259 = relay.const([-4,4,7,9,4,-3,-4,1,5,2,-10,1,-1,-10,-2,6,-6,-2,-10,7,8,6,-9,1,-2,5,-3,4,3,-8,-2,2,7,-5,7,-1,-3,7,6,4,-3,10,3,2,9,-10,-2,-3,8,-6,-9,10,-7,-2,6,-9,-4,5,-6,-5,4,-9,10,7,-9,1,-3,-2,9,-3,1,-4,-2,4,7,-4,7,-1,-5,-6,-3,-6,9,9,1,3,-4,7,-5,6,2,-4,3,-9,4,-7,-4,5,1,9,6,4,-8,-7,-3,6,-5,8,4,8,-3,-6,10,-8,5,-4,1,10,10,4,-10,-1,-9,-3,-8,-4,10,8,1,-10,7,-7,4,8,5,-7,2,-10,-1,-7,-5,-10,1,4,3,-8,10,9,-3,5,-10,-4,4,-5,-8,4,1,10,-9,4,10,4,-7,1,-1,9,3,-6,-9,2,1,-3,-9,6,7,1,2,-5,-10,1,7,5,-3,-8,1,-10,-5,7,-5,-1,-3,-8,-10,5,1,1,6,-7,8,3,-5,-4,-7,-8,5,5,-4,4,7,-3,-3,-6,2,-10,-9,2,8,-8,-6,-9,6,9,-8,3,10,2,2,-6,3,7,-1,-8,2,5,-4,8,-8,-9,8,10,10,5,1,-6,-7,6,1,-4,4,2,-4,8,-7,-8,3,-7,1,-4,-1,-7,-5,-6,-1,-1,2,10,6,-7,9,10,-3,-4,8,7,8,10,6,-10,-6,1,6,3,-1,5,-4,-1,-1,-9,1,-8,9,4,4,4,7,-8,-9,5,9,-2,-4,-10,-6,-5,7,7,1,-3,7,5,-5,7,3,-5,-1,-5,-10,1,6,-4,-9,-10,4,7,3,5,6,3,1,10,-5,-6,-2,10,1,2,4,-2,7,10,-3,9,7,9,-8,-10,5,-7,-3,6,8,5,10,-2,9,9,9,3,8,3,-2,10,-9,6,-3,-5,8,4,-9,7,10,-2,-3,-4,9,-10,8,-10,-8,-8,-7,-3,3,7,6,10,1,7,-10,-5,-6,-2,5,-3,8,-6,-4,-4,-6,9,-6,-2,-2,8,-7,1,-10,-2,-4,-9,-8,-9,-2,9,5,-4,8,5,2,-2,-10,4,5,-4,3,-3,-6,5,-7,-8,4,-1,-5,-2,2,7,6,-2,9,2,-7,5,9,-3,-6,-1,2,-3,-10,5,-9,-6,4,-8,3,-7,6,6,-3,4,-10,10,-6,-9,9,10,6,5,-3,-3,2,7,-3,3,-3,-3,-1,5,7,-4,9,4,-8,-5,9,-7,9,9,8,6,-1,4,-4,-9,-4,5,7,-9,8,5,-4,-10,-8,-3,-5,8,9,-7,-3,-2,-9,2,-8,-10,7,-6,10,5,7,6,8,7,8,-10,8,9,1,-1,4,-7,-7,-3,-9,6,-6,-7,6,2,5,6,6,-3,7,-7,-5,4,-7,10,-5,9,9,-8,9,-1,-3,-10,-2,-7,-6,2,9,7,4,10,-6,-3,-7,1,10,-2,9,-4,-4,-2,5,4,-3,-10,10,6,-10,-10,9,-5,-3,4,9,-5,-6,3,-4,-5,-10,1,6,-4,6,5,7,-4,9,6,-3,10,9,-1,2,7,-1,-2,8,5,-3,-9,2,-3,-9,-10,-10,-4,-6,2,-10,-2,9,-10,-1,3,7,4,-3,-10,-6,9,-1,-6,7,-6,9,2,3,7,8,8,9,-3,-9,-9,5,4,10,-4,-10,-3,-10,6,-8,-7,-2,10,-7,8,-9,-2,6,2,-7,-2,-9,-3,2,4,6,-6,6,-2,10,8,8,6,7,-9,-6,-9,-5,-8,4,7,-1,8,9,-10,-3,-2,8,4,-8,8,-3,-1,-1,-7,10,5,-7,1,-7,6,-9,1,-8,3,-10,-2,-9,-3,-3,-5,4,-4,-7,8,-6,-3,5,-2,-9,-9,-7,-3,-5,7,7,-8,-4,-4,9,-6,-8,-2,1,6,-1,10,-7,2,-9,7,-3,-9,-1,-9,-4,-9,-3,5,-7,5,-7,5,8,-3,8,-3,9,7,4,10,10,10,10,-7,-6,6,9,-7,-1,-4,-2,-2,-6,1,-5,-7,8,-8,3,-7,2,-2,5,8,2,6,8,7,7,5,8,-8,-9,7,6,3,-7,10,6,9,1,-4,-5,4,-8,7,1,2,-4,4,-5,9,-1,4,-7,3,-2,7,-7,-3,-10,-1,-6,2,4,-9,2,10,6,-9,1,-1,1,2,8,5,6,2,-10,1,10,-4,-9,-6,-8,-8,-10,-2,6,1,1,-6,5,-8,-2,-1,-10,-7,-7,4,1,-6,10,4,-2,-1,-2,-10,5,-1,7,-1,7,10,2,-1,7,-6,5,-4,-4,10,2,-2,-7,3,-7,5,-2,-9,-8,-9,-10,-1,-2,4,9,-3,-3,5,-10,-4,-3,-2,-3,-9,-3,-5,5,10,2,-5,-7,10,-3,-9,-5,9,-3,1,2,-6,-2,10,8,5,3,9,-6,9,7,-4,3,8,-4,2,1,-3,-9,-10,-4,-7,5,-6,-6,-2,-4,-5,10,1,-2,-2,-10,-8,9,-6,-5,9,-10,10,-1,-10,7,-2,-9,-10,7,-8,8,-6,5,9,6,7,6,-3,-10,-4,10,-5,-8,-10,7,-1,-5,2,-2,8,-3,-5,6,6,3,-4,-3,-10,4,-9,9,7,-9,-1,-4,-1,8,3,-4,-10,8,-9,-3,-5,10,-1,4,-2,1,-5,6,1,10,10,3,-2,-3,4,-10,6,-3,-1,-7,1,8,-10,-10,10,4,-5,-9,-2,7,-10,-4,-7,3,5,2,-7,-10,7,-9,3,7,2,4,-10,-9,10,-9,2,6,2,-1,-8,-6,-2,-2,-8,-2,6,-6,1,-9,1,-7,-9,-10,10,-2,4,-3,-2,-3,5,3,-3,10,-6,-4,-6,-8,5,10,9,6,-9,-2,-6,-3,10,4,7,-9,4,8,6,7,-5,-1,-8,-8,7,-7,-2,-8,6,-8,-6,4,10,-10,-7,2,-5,-6,1,9,3,3,-6,-10,2,5,-4,-10,10,-5,-10,-9,-9,7,1,9,3,1,-2,-4,-6,-4,6,7,3,-5,6,-7,10,-6,-3,-5,7,-8,7,-3,10,5,1,-2,-3,-7,-2,5,-10,3,8,-10,5,3,-1,-7,6,-7,-4,-1,-7,-6,-3,-8,-6,8,10,10,-7,5,1,-7,4,4,-2,-6,3,7,-5,-1,-8,6,7,1,-10,2,-10,8,2,3,7,4,-1,8,-5,-10,5,1,1,8,10,-3,-8,4,5,7,-9,5,-3,8,9,-3,4,-8,5,6,-5,-6,2,-6,-1,2,-3,10,8,-4,-5,-3,10,-4,9,-2,9,-9,10,-9,-8,1,-7,-7,-8,-4,-9,-4,2,6,7,8,-6,10,-4,-8,-1,-4,-1,-5,-2,-4,8,2,7,3,-3,-2,10,8,-1,4,7,-10,9,-7,-4,3,-8,-2,-10,9,-8,6,-4,-1,1,9,-5,4,6,-6,2,-4,4,-5,3,-10,4,-8,-10,-5,4,9,-5,-3,4,-3,7,-5,3,7,-4,6,5,-8,1,-6,-9,4,5,7,7,6,-5,-6,2,4,-10,-4,2,-8,7,-10,8,-4,-3,4,1,3,2,-6,-3,-8,1,-8,6,-10,1,-3,5,-3,6,-6,7,5,-1,2,3,6,4,9,-9,4,8,-8,3,-9,9,8,-7,5,-3,-1,-9,-10,-1,10,7,-2,1,8,-3,3,-2,-10,-5,8,-2,-6,-8,-3,-7,-10,8,9,-4,-1,4,9,-6,-9,-3,-1,-8,7,3,-6,2,-5,10,8,-3,-10,-5,-2,-7,-4,-8,7,-9,-3,-2,-3,6,3,-3,9,1,2,-8,1,-7,-8,-9,2,-1,2,-5,8,-2,9,-3,1,6,2,-8,-1,-7,10,6,-3,9,10,10,-9,-10,-10,-5,-9,-4,6,5,9,-8,5,4,-1,-5,9,1,-8,6,-8,-10,-3,9,10,-9,-5,9,1,9,-8,-4,-8,7,-10,5,-6,-6,-1,8,-10,-10,4,-4,-3,-6,5,-8,-7,-10,-9,-6,2,-2,6,2,-9,-10,4,-7,-4,9,-4,-2,-3,-9,-7,-5,-6,2,1,7,-8,10,-10,-10,9,-2,8,6,-6,4,-10,2,10,-8,-10,8,4,2,6,-8,1,9,-4,3,-10,5,7,-5,-3,-7,-10,1,-4,7,4,4,5,-5,6,3,6,-5,-5,-2,-1,-1,4,6,4,-6,9,2,-3,7,8,7,-5,-8,1,1,9,-5,-4,10,4,-4,8,-9,6,2,3,7,2,-10,-3,8,-3,-4,-6,2,-10,5,4,-9,-9,4,2,1,7,8,-2,-4,9,-9,2,-5,10,10,-3,6,-2,3,4,-8,5,4,4,2,6,10,-5,-2,-4,-10,-3,-10,-1,-9,-7,7,-4,-1,9,-2,5,4,-7,-8,9,10,6,-7,3,1,4,3,-9,6,6,-2,10,-4,4,-9,-9,5,1,2,9,-5,3,10,-10,9,-4,10,1,-2,5,-8,-2,-10,4,-6,-9,-5,-9,-4,1,9,-6,-1,3,2,5,-2,2,2,8,-8,-1,7,7,-10,-7,-4,-8,-10,8,-8,-9,-10,6,6,9,1,8,-9,1,5,-8,1,-2,6,-2,-3,-9,-1,-6,-9,4,5,7,-8,5,4,-2,1,5,-6,-4,-7,3,-7,6,3,3,-3,4,-7,-5,-6,6,-3,-7,-8,-7,3,3,-8,-4,-9,1,-7,5,7,9,-9,1,7,-10,-8,-8,-8,2,1,8,-5,4,-5,-8,-9,6,-1,9,-4,1,-7,-4,3,2,2,-6,1,8,10,-10,2,-6,-4,1,5,1,-4,-8,1,-10,2,-9,-7,10,-3,-6,-8,-10,-1,-10,4,8,-6,-2,8,7,10,-6,-3,6,-9,-2,7,9,2,4,-1,-1,-3,-4,-7,-3,-9,5,5,9,-4,-1,3,-10,-1,1,9,1,-7,2,-7,2,-4,-9,8,1,9,4,-3,-10,-9,6,-5,9,-3,-9,-6,6,9,8,-3,1,2,5,2,-10,6,-10,-5,4,-1,-8,-5,-6,-10,-4,-3,7,2,1,-7,6,8,-8,-6,1,-5,-6,-5,-5,-7,10,-3,7,10,1,10,-3,-5,9,3,-1,-1,1,9,1,-6,-8,-9,-6,5,-6,-7,1,-2,-3,4,-5,1,1,5,-10,4,-2,4,-1,7,2,-8,6,-7,3,5,4,-6,-9,-6,4,6,-4,5,-7,-3,-6,6,-1,5,2,-3,-7,3,2,3,-1,1,9,-3,8,-7,-6,-8,-6,10,2,-6,4,5,9,3,8,7,10,4,-3,4,-6,8,-7,9,4,8,-3,8,-2,-1,-7,-8,6,6,-4,3,-3,1,-1,-1,6,-5,-4,-10,-3,7,-1,6,-6,9,3,10,-4,7,-1,-10,-10,3,-7,-10,-6,-2,-1,-6,-3,7,-8,-3,7,-6,2,3,-1,6,3,-10,-5,8,3,5,9,-3,8,-9,-9,3,-3,3,-5,3,7,9,-6,-7,10,-6,-3,-8,-6,-8,-6,-8,9,2,-10,-4,-8,8,1,-4,7,-2,10,3,-8,3,-4,-2,2,-9,-1,-9,9,5,-3,10,9,-2,1,7,8,3,10,-9,1,7,4,-1,3,10,4,-8,10,-4,-7,10,10,9,9,4,-7,-2,-9,1,-10,10,9,-9,-7,-1,3,-10,-7,4,-9,5,-3,5,1,-4,7,5,3,8,-6,-6,10,-1,-9,4,7,-3,8,10,4,-2,-1,8,2,6,4,-6,-10,-3,4,-6,-7,-1,9,-6,-9,-5,-7,4,10,7,4,10,10,4,1,7,10,-6,-3,-3,3,3,-2,1,-9,-6,10,8,1,8,-3,-3,4,4,-2,-2,-7,-6,3,3,-6,6,6,7,-5,1,-9,5,-2,3,-7,10,9,7,5,-4,8,6,4,-1,-8,1,7,-3,6,-4,10,-9,1,-2,5,-5,6,6,7,-10,-2,-2,-6,7,-2,7,4,-10,-1,9,-8,8,8,-5,5,-9,8,-5,8,-8,-10,2,-10,-9,7,-6,4,1,10,-6,3,2,-1,-8,7,-1,1,-3,8,-2,9,9,2,5,6,-6,9,10,5,10,6,-2,-3,-5,-8,5,5,-1,4,10,9,8,-6,-9,10,6,1,10,5,-6,-2,-10,-4,3,-7,7,9,-8,-8,7,-8,-2,10,-2,9,8,8,-8,9,10,6,-3,-5,-1,10,10,2,-5,-6,-9,-5,-4,-5,5,6,9,3,7,3,-10,8,10,-2,4,4,-10,-10,-1,-1,-10,-10,-8,-1,2,7,-8,1,-6,-5,-10,-4,5,9,3,-2,6,10,-6,3,8,9,-4,5,5,10,6,-10,-10,-9,-8,5,-7,-9,9,-1,9,-2,2,5,-7,5,-9,-6,-3,-3,10,-4,-5,9,5,1,-2,1,10,3,8,-3,-2,-7,6,5,-10,-10,-2,-10,-9,-2,-4,6,8,-5,7,5,-7,-2,4,10,6,2,-8,-6,-3,-9,3,3,5,8,-6,-1,5,7,-1,-7,6,7,-2,-5,3,-2,-1,8,4,10,-8,4,-4,-7,7,-4,-3,-1,3,-10,9,-3,-10,8,6,4,1,-1,9,2,2,-1,6,-2,5,5,5,-6,-8,8,4,-2,-2,-2,1,-6,-1,-9,-6,-5,-4,-7,-10,-3,7,4,5,-8,9,7,3,2,-8,-10,2,7,10,5,5,8,-3,-7,8,-7,-5,-4,6,4,-9,-10,2,8,-1,1,5,2,-2,6,4,7,-8,10,9,1,10,10,1,3,-3,8,4,5,8,-7,7,-4,7,10,-9,5,-2,-9,-4,-5,-9,-6,4,2,-5,4,5,6,1,-1,8,-8,-2,5,3,5,-2,6,2,-8,7,8,10,-5,1,1,-1,-10,-10,-8,-5,-5,-6,5,-7,5,-4,7,9,5,7,9,-7,-10,4,-9,3,-7,3,6,-4,-5,6,-2,-3,4,3,7,-2,6,-4,-4,7,7,3,1,6,6,7,6,-5,7,4,7,-10,2,7,3,9,-5,3,10,1,1,5,7,10,7,7,-9,-8,3,9,3,-5,-2,4,10,-9,-5,-10,4,6,1,-7,2,-3,5,10,2,6,-4,8,-8,-6,-1,3,6,9,5,-10,-5,2,7,-6,9,-4,2,8,-9,1,1,-7,5,4,6,-7,-9,9,-2,6,6,-6,-2,-8,-9,10,5,6,-7,-10,-4,-2,-7,-10,5,-2,-6,1,3,6,8,-1,-5,-3,-7,5,-9,6,-9,6,-2,7,9,3,-7,1,9,6,-8,8,1,7,-2,7,9,5,6,-9,-2,-4,-5,2,-8,8,9,-1,9,4,3,3,7,-3,-2,7,-7,2,-7,-4,7,2,9,-10,-5,10,-6,-10,-2,7,7,9,4,-6,8,-7,-3,2,-6,2,7,-1,-6,-7,6,-2,5,-7,-5,-3,4,-9,-10,-8,-5,10,-4,-4,-2,9,-4,-2,-4,-9,1,-3,1,1,5,2,2,4,4,6,-9,-5,6,2,-6,9,3,4,6,-9,-7,-2,4,-8,-4,-6,9,-5,-9,-5,8,-4,-5,-8,6,-1,8,-5,-9,-1,-5,-5,-8,-9,7,-6,9,-7,10,7,-3,-8,-4,-3,6,-8,-3,-7,-5,-2,2,9,-7,6,-2,-3,1,-7,-4,10,6,-1,10], dtype = "uint8")#candidate|4259|(2925,)|const|uint8
call_4256 = relay.TupleGetItem(func_1292_call(relay.reshape(const_4257.astype('float64'), [3, 12, 1]), relay.reshape(var_4258.astype('uint16'), [280,]), relay.reshape(const_4259.astype('uint8'), [2925,]), ), 2)
call_4260 = relay.TupleGetItem(func_1296_call(relay.reshape(const_4257.astype('float64'), [3, 12, 1]), relay.reshape(var_4258.astype('uint16'), [280,]), relay.reshape(const_4259.astype('uint8'), [2925,]), ), 2)
output = relay.Tuple([call_4244,call_4256,const_4257,var_4258,const_4259,])
output2 = relay.Tuple([call_4245,call_4260,const_4257,var_4258,const_4259,])
func_4272 = relay.Function([var_4258,], output)
mod['func_4272'] = func_4272
mod = relay.transform.InferType()(mod)
mutated_mod['func_4272'] = func_4272
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4273 = relay.var("var_4273", dtype = "uint16", shape = (280,))#candidate|4273|(280,)|var|uint16
func_4272_call = mutated_mod.get_global_var('func_4272')
call_4274 = func_4272_call(var_4273)
output = call_4274
func_4275 = relay.Function([var_4273], output)
mutated_mod['func_4275'] = func_4275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3698_call = mod.get_global_var('func_3698')
func_3700_call = mutated_mod.get_global_var('func_3700')
call_4301 = relay.TupleGetItem(func_3698_call(), 0)
call_4302 = relay.TupleGetItem(func_3700_call(), 0)
func_2404_call = mod.get_global_var('func_2404')
func_2407_call = mutated_mod.get_global_var('func_2407')
var_4306 = relay.var("var_4306", dtype = "int16", shape = (840, 1))#candidate|4306|(840, 1)|var|int16
call_4305 = relay.TupleGetItem(func_2404_call(relay.reshape(var_4306.astype('int16'), [840,])), 0)
call_4307 = relay.TupleGetItem(func_2407_call(relay.reshape(var_4306.astype('int16'), [840,])), 0)
func_2700_call = mod.get_global_var('func_2700')
func_2701_call = mutated_mod.get_global_var('func_2701')
call_4308 = func_2700_call()
call_4309 = func_2700_call()
func_3367_call = mod.get_global_var('func_3367')
func_3370_call = mutated_mod.get_global_var('func_3370')
var_4315 = relay.var("var_4315", dtype = "float64", shape = (2352,))#candidate|4315|(2352,)|var|float64
const_4316 = relay.const([[9.788568,-7.014382,-5.908957,-6.257145,-6.577284,-3.985041,-6.905804,-9.417042,5.505898,-4.537303,5.770812,-8.662235,6.074375,4.199426,7.849841,7.056806,-9.258066,-8.336049,-9.368090,-7.471417,9.605087,-4.404888,-2.732692,-6.959482,-5.595968,6.296222,4.469733,-4.723914,-3.620539,-0.937077,-4.827750,-0.054269,0.138873,6.680702,-0.067963,-1.730325,-0.663393,9.389683,6.852422,-4.460428,-4.311211,-0.945388,4.346645,-1.588003,-1.325525,-0.588252,-1.801270,-8.967188,7.787821,2.987639,9.518474,-8.277982,-7.950758,0.113979,0.420216,7.024856],[5.317198,9.320900,1.603397,-8.223026,3.099557,-5.345883,-6.267750,9.852742,-8.215115,7.943169,6.462260,7.361563,8.876198,0.703437,-6.677097,-8.024955,-5.074395,-0.689131,-8.153785,-1.906048,3.714217,9.666409,2.383395,-4.795170,-4.014250,4.842046,5.295299,4.457024,8.325914,2.356466,-7.627157,-0.682066,6.992330,-2.246555,5.471161,0.348912,1.373108,-3.290233,-7.976279,-5.064751,-9.564722,-2.120754,-7.798246,-0.274733,-5.099255,2.986423,-3.196193,-5.931184,-9.840815,7.171000,0.363899,4.622743,3.891510,8.902464,-4.612888,-4.319253],[2.239433,-9.070170,5.226838,-6.558202,-0.664283,-0.280926,3.795605,-0.116238,0.813591,4.135821,9.049703,7.351750,1.306204,-2.111481,-9.054261,-9.412428,2.467110,9.021379,-4.376151,-5.433839,3.083400,8.476230,8.748877,-8.763046,7.695496,4.581319,-8.520405,3.725472,8.131937,8.160537,6.687308,-0.257857,-5.900592,9.132313,8.183238,7.761355,-3.926744,8.012466,4.810143,-6.253885,4.546380,8.784766,-7.739543,4.856528,-8.336240,0.958328,7.951316,-9.640865,3.391232,-0.832703,2.434074,6.057569,-0.407527,-0.703658,-9.574318,-4.471410],[-7.319483,-1.005212,-3.808596,8.237256,-7.737460,-7.655524,-3.346383,-5.817674,-5.832752,-4.500417,-5.886730,5.929508,-2.871316,-0.045758,-6.070239,-8.982892,-9.330565,5.780341,2.892182,3.053295,6.603240,0.744765,-5.187931,3.183677,-5.063065,7.811644,6.229376,9.913074,-5.580411,4.161724,-2.502876,0.840702,-5.283512,3.489856,5.081704,3.753048,0.302076,-0.239448,-6.897499,-8.544821,4.815733,-0.980478,0.801446,-8.912068,0.995036,-9.598116,-5.046305,3.469392,7.872926,-3.013251,3.694613,0.934185,-0.735177,7.179523,-2.218756,9.191596],[0.625441,-1.320886,6.390873,-2.062424,-8.344601,-0.398103,-8.056731,0.576451,-6.943246,5.993395,-5.878499,-4.365076,-4.783421,2.666178,-7.772401,1.964146,-5.655416,-8.520813,-6.123976,6.942755,8.503986,5.277073,6.020937,6.047503,-4.682519,3.543835,-4.782047,1.700422,9.781466,5.923502,9.705445,6.048070,-4.332103,1.107538,-4.069530,-4.628798,-8.910080,-3.494750,-4.325221,-2.166570,-2.179129,2.872032,1.020988,4.784561,-4.382059,-2.754605,8.461565,5.391762,8.347728,2.876326,8.045281,-3.114080,0.774832,4.136316,-9.339857,9.934815],[-9.613422,4.157859,2.753716,-2.949441,6.696228,-3.058471,7.155351,4.614999,-5.192506,-8.874290,-9.524678,-8.237094,8.220156,8.333296,1.198125,-4.058770,-8.168082,0.400978,7.994075,7.639576,1.328228,5.005298,5.190199,8.878230,5.738673,-9.033883,-6.754499,-7.019112,-7.838899,-9.530228,-4.800069,0.664988,-0.995627,-0.726597,4.830243,2.166383,5.271055,9.969963,5.847979,5.330536,-9.947841,-6.832481,-0.600515,7.214872,-9.142831,-0.551767,-8.317825,3.242890,-2.820392,-7.161378,3.580885,-8.169897,3.905364,-4.652566,1.266904,5.743138],[5.645912,-4.057936,-2.293379,-8.357050,4.737861,2.950010,7.538195,4.305420,7.277782,0.731637,7.563838,6.375062,4.619232,3.430544,2.017041,-1.102244,-4.300743,-5.902763,-6.994765,8.653156,0.639238,-4.747134,-0.471069,3.589613,6.614123,-7.175278,-8.605377,6.676412,3.654626,-6.924391,-1.161201,3.238239,-8.919856,4.357177,7.744533,-8.583521,-9.214288,9.549490,-2.437729,-6.291203,5.355613,-4.811459,-9.703847,1.653202,-9.310347,2.819927,-4.550423,5.570278,-3.107212,-8.632481,-8.513963,0.174014,8.766311,9.355882,1.915902,5.803573],[-9.293203,-2.829955,-2.927812,9.817789,-9.046052,8.879924,7.685376,5.441969,4.312594,2.071449,-3.416224,-3.636156,8.970343,-8.984568,7.496455,7.226178,4.758356,3.823251,6.375717,6.446056,0.533333,2.943605,3.817082,-9.096213,-8.689972,-4.251363,-1.163062,-4.199626,-5.658417,-0.500318,-6.665368,-9.926789,-0.767689,0.628071,-5.214329,2.374154,2.294611,-3.950876,1.120188,-6.143225,6.180879,-9.657322,5.628585,7.642631,1.136859,-5.642887,-6.495498,-5.548501,-7.376315,-0.455623,-2.773282,-7.971921,-4.651359,-6.371788,3.670364,1.394419],[-3.977906,7.570785,-4.309828,3.830245,-8.521924,-1.198358,-5.112452,4.727962,-2.562860,7.395606,1.264629,8.341595,6.152269,1.717882,-3.914478,4.465055,3.900806,-0.691253,4.163503,2.902003,3.734073,-9.399416,-7.884903,-8.449856,-5.006745,0.168773,5.444803,2.485535,5.708385,-8.224480,-9.903786,-2.600400,-4.968371,9.122970,-2.363740,8.539769,-2.856895,-5.278512,-7.767115,-7.156623,-6.385428,-6.060545,-8.172934,-1.694385,7.687288,1.975530,-2.073177,6.037162,-8.998994,8.010783,9.094810,5.052325,-1.539452,6.602240,-1.088171,6.091820],[9.891789,7.652150,-0.134537,4.826656,-0.270076,9.550121,-8.398220,6.101406,9.654910,-1.985324,9.352276,7.475847,0.944398,-5.422853,-0.270584,-9.928242,-3.780999,5.178498,-9.365889,-8.317625,3.162920,2.490956,-7.891815,-4.944507,3.630317,-7.861329,-5.879345,3.061116,-2.969932,-1.106066,8.982847,3.365880,-8.014305,-2.996172,3.303931,6.365913,-7.739119,0.971552,8.174481,4.943652,-8.767931,4.223114,8.865327,-4.733967,8.063304,-2.433464,7.518245,-5.121464,-2.840206,-3.303746,9.789523,-9.578792,7.697706,-4.475391,8.608953,1.893207],[6.583986,9.255821,1.624365,5.296456,-9.420299,-5.614037,4.657937,3.073385,7.732144,3.979872,4.629823,1.930436,9.889404,3.395375,2.389426,-9.547675,9.068896,5.377688,4.464001,8.922340,-2.544265,-1.456670,-4.031105,5.642577,8.735531,-6.142797,-1.701677,8.138978,3.367682,-6.290292,-8.229213,-6.111642,-2.762283,-2.599350,-0.053531,8.453089,5.573866,-6.190822,7.870317,-7.991454,-9.819680,4.887345,-8.425373,6.393545,8.862590,-5.191012,-5.314014,-9.078962,-0.113371,4.933795,-2.062832,9.734296,-5.246146,-6.049725,6.690924,-3.005657],[4.000559,-1.430554,6.152471,-1.896505,4.845800,-9.022986,5.098110,1.752467,1.817890,-7.968292,4.617646,-0.275805,7.436148,-6.231178,6.635021,-5.059615,-8.925806,-4.441184,-9.749927,3.911419,7.024482,-5.554040,-5.732569,-4.949104,-1.255781,9.885020,-8.312327,5.832148,-9.814446,-9.809455,-2.184498,9.647946,9.358167,-8.298390,-6.247955,5.291708,1.716528,-2.533706,7.997573,-9.773083,3.063413,-8.511869,3.164398,0.962270,8.741435,9.140381,-7.912840,-5.490124,-6.828739,-6.704911,-4.345257,-5.183321,1.879003,7.732954,0.931938,-1.239429],[-7.180189,-2.150703,-5.325929,2.039966,0.241222,4.873024,6.860359,3.663164,5.154743,-8.621373,9.692090,4.953890,2.278045,-9.072845,-5.038387,2.258299,8.608183,-2.804145,7.128161,9.535008,-7.565389,0.500027,-2.590736,1.961706,-4.418327,-7.322399,-2.036322,-5.815990,-7.681969,-0.068623,1.552959,2.718005,9.550328,-9.054808,-7.760608,2.748451,-4.254847,-9.419720,3.958874,-6.657417,-8.325494,-3.599575,6.719668,-4.135182,9.659416,-8.061295,6.208367,4.280955,-6.093099,3.761792,1.343723,4.247906,8.528897,-0.323214,-6.719279,-1.816188],[6.789028,4.052610,9.093612,2.199105,9.679218,9.037636,1.374435,7.874810,-5.683776,-9.183267,-9.044646,-9.517118,-9.834614,-9.193828,5.359184,0.433145,6.603413,7.655365,-1.452564,4.425967,9.603812,-4.254322,0.458322,-6.762809,1.774952,5.201418,-2.964591,5.563605,8.982542,5.242550,5.893668,5.757584,-7.336787,2.362809,4.691200,-2.929444,-7.233216,-2.371261,-9.681015,8.598295,0.607790,0.755679,-1.950762,-6.264520,7.656589,8.486011,-6.865483,9.431247,5.222988,-7.933217,-9.550761,5.617632,2.824894,-7.014479,-6.641898,9.725938],[1.513459,-2.509513,-2.721345,9.948501,-2.436929,-0.439145,3.208869,2.459493,-2.074862,-0.904974,-1.948425,4.721083,0.015542,-2.214422,-8.620389,8.228134,-6.692178,1.747245,2.694531,-8.432102,9.027596,-8.910002,7.330859,-6.348809,7.494665,-4.732722,-6.075444,-2.764778,9.688250,-7.438354,-3.952334,9.775698,8.478915,3.781749,3.303271,-6.465241,-9.593627,-1.160381,1.290248,-8.373085,9.808955,-4.200486,-8.776563,9.175892,6.838732,4.611979,1.058402,4.713485,-3.007365,4.021247,-0.592840,-5.627241,0.678086,-6.696636,7.038190,7.406436],[6.429449,1.295399,-9.232412,-7.175339,-7.578714,-1.219532,-6.061215,-5.313041,-7.460919,7.842999,8.094851,-6.345532,-8.829498,1.822077,5.144548,-2.433870,3.033379,-9.246499,-3.192013,1.880997,9.037666,-7.220530,0.672465,-0.271565,6.213587,1.138009,2.234076,3.971750,-6.779004,-0.300548,5.828371,1.680740,-2.408303,8.006669,-0.539541,6.348088,-4.627198,6.942971,-1.324471,8.824841,1.999140,-2.970309,-6.779278,-2.440240,1.910143,-4.526292,2.245822,5.968379,-0.730142,-1.420109,7.385503,-7.300950,-2.232674,-2.258322,7.773254,-9.494762],[-2.067250,2.206843,-5.097603,6.573192,-3.983740,-3.740560,5.992531,8.502499,-4.556740,-4.935703,6.476373,6.598271,4.821634,-8.460391,-3.936488,4.429369,-5.301344,0.034498,1.094016,-7.976432,4.285800,8.987634,-9.874707,-0.833374,2.279083,-1.843110,2.883790,-0.681740,8.361407,2.841329,5.457041,-7.810975,4.091162,-8.939389,0.765565,9.218877,8.345082,5.607290,9.545645,3.560376,1.165320,-4.826847,9.931130,3.133447,4.404871,-4.874399,4.011931,-2.337215,0.164151,4.658998,8.807404,3.574618,-7.634564,-4.276292,-0.432271,-9.626186],[-2.687124,-9.263455,1.058699,-3.717585,-3.537213,5.052970,-0.271777,-3.436596,-4.064632,-9.917036,-7.320403,-1.615289,-8.573968,7.852004,-5.113693,-3.615579,-3.562890,3.818820,-0.045140,-9.990219,-1.795905,0.483463,-7.105015,-5.042939,0.886906,-7.416164,-3.449888,-1.433731,-7.172414,1.218050,7.705849,6.542507,-6.559109,2.587033,-8.784204,4.013314,1.745934,9.224823,7.801875,-3.448083,-8.633871,-9.976699,-7.129550,-5.178838,-8.017520,5.422609,0.453029,7.153685,3.012959,2.797547,7.624103,0.201522,3.305411,-8.999314,-5.593702,9.757758],[9.148049,-1.248735,7.881573,-4.895380,-5.617286,3.247497,-2.643176,-7.390968,-9.355298,-7.431863,-3.528536,-0.429445,-6.226963,-8.912601,-8.888699,-1.765112,-7.130498,6.781509,4.713681,3.881945,8.909876,7.625612,-9.000702,-9.098039,5.101919,-2.710922,-9.485153,2.778995,9.591091,2.462101,-3.913842,7.368187,-9.536054,-1.149316,5.516929,-2.656728,-5.671465,-8.047366,7.770373,2.832567,0.791449,-5.836773,1.317594,9.845048,-2.571774,-8.253525,-4.773569,1.096942,-2.631231,-0.202784,2.934261,-8.347782,-0.961302,-6.243210,4.242202,8.835536],[2.481189,-3.560985,7.215592,8.803950,9.054636,-5.606975,-8.743466,-6.053150,4.554786,-9.762587,2.999654,9.609204,9.184951,7.963508,6.887357,-2.909505,1.721379,7.055980,-0.859365,-9.242495,-0.046815,5.623767,-6.971228,7.043325,-2.508473,-7.152922,6.299335,8.600440,-0.344461,0.887783,7.241334,-4.521733,1.769334,-1.297962,2.366942,8.327086,6.886189,-2.071907,-0.706200,-0.658733,7.306271,0.714714,-9.049175,2.467523,5.406565,-1.259961,-3.422099,6.842141,6.115432,6.701329,-1.586378,-6.298198,4.616767,9.726302,2.926107,-2.935134],[0.839158,9.828187,4.091629,-7.744529,4.934248,0.598034,0.292271,5.885471,-0.527774,9.089842,1.278106,2.471407,-4.181092,9.091346,-0.486838,-4.294144,2.821038,7.884440,3.170529,6.688194,-0.940919,-8.515267,-2.141217,-9.194722,1.162724,3.616350,-7.969445,8.102197,-8.906451,-3.974719,5.282777,-8.901513,-5.343970,4.856660,0.232668,-5.806955,4.276955,6.582378,8.671690,8.507418,-5.081381,8.410546,2.699042,8.192125,5.694450,-4.936222,1.012258,7.919251,-4.606360,8.276018,-1.920594,4.385243,-4.674154,5.719017,2.715427,-1.286529],[6.855488,-4.626870,7.788841,-0.027462,1.131786,0.221860,0.077852,-6.914625,4.260971,4.167878,3.795164,2.912025,-8.499724,0.068157,8.289110,3.096505,-9.986283,4.822236,5.060560,-5.623225,-5.979594,3.142546,4.839574,2.305511,6.039724,-0.389561,-4.925691,4.798211,-7.624082,-4.308694,-3.743972,-4.164465,3.805149,-8.251537,-1.120586,7.960773,-2.082096,-7.585552,-1.713646,-0.836459,5.541161,-2.748015,0.293986,-8.036070,2.937551,1.076032,-6.461296,-8.049757,-1.261665,-5.509115,2.996731,0.438470,4.472632,2.239164,-9.159181,6.083101],[-4.514086,5.591885,8.926898,9.045219,-4.145713,1.868056,1.930725,-0.888809,-2.266261,-5.575913,-6.962213,-9.952118,3.238316,4.499921,5.937917,2.322958,-9.233964,5.110104,-7.516777,-8.783092,-3.215754,6.803891,8.355935,3.454962,9.809092,-7.701435,4.014531,6.086043,-8.203313,-7.721272,5.380361,-1.893080,-0.338346,-4.196093,-0.090496,9.301069,-9.620287,-3.814988,-4.076193,9.835279,7.967486,0.079706,-8.551526,-8.563529,7.417823,4.981842,-0.763075,7.832086,5.013190,-4.630041,-1.258091,-7.450327,-1.033856,6.065531,-2.725014,-1.208393],[-2.746989,5.845934,-2.916472,4.561602,-5.093501,1.988022,-8.792243,-1.983055,-4.319594,-5.556437,-7.288453,6.241863,7.789455,-3.994211,5.024949,-0.349517,-8.010337,6.906657,5.480172,0.632195,8.066051,-0.903289,6.210843,4.717089,6.778091,-5.699844,5.643668,7.465817,-6.787582,-9.366694,-8.256897,4.200058,-0.407351,-7.153403,-3.223563,-9.320923,-6.778666,8.028478,5.817285,0.771425,-5.160046,-7.640470,6.089402,3.043244,3.419176,4.081728,-1.589409,7.978121,2.539049,-5.689961,6.487451,5.875728,4.350609,7.280005,-9.998645,-7.184368],[-7.856999,-2.382555,-8.345280,-3.105735,3.807583,9.650765,-3.347373,2.464539,-6.022860,0.551540,-5.725934,1.040132,-1.321459,-9.394605,5.975296,2.832624,8.476432,0.716143,3.435191,-1.798425,-7.533167,-2.226892,-0.278719,-9.518641,2.512028,-1.920018,6.823037,-1.512126,-4.552985,-7.480415,6.939006,8.162422,7.441974,-3.824822,-4.928593,7.380277,-1.309560,-2.469207,8.961450,-0.315959,-0.230602,-3.473471,-3.343659,4.323204,2.490522,5.823790,-3.581776,-1.544469,9.873805,-7.134951,5.153304,-0.472434,-2.840460,-0.540019,-3.309462,-3.499328],[1.444934,-2.525303,5.025184,-9.982472,1.933038,9.661040,-6.264012,3.189687,-0.451576,-0.529747,9.350971,-3.797727,1.280134,-3.953130,0.950591,-6.956126,2.120528,-8.178036,5.784531,-3.207802,-8.692581,-4.137184,7.316035,7.922070,5.210875,5.290017,-6.428938,-3.173500,-7.178942,5.516717,-6.220773,-1.591951,-1.070680,-2.046043,8.428167,-1.008007,9.235226,-6.415116,-4.883154,-1.329593,5.612244,3.772317,7.951688,9.175912,-0.187615,3.698887,8.395083,-5.701387,5.383839,7.526645,0.326466,-2.859163,-0.612915,8.890121,-1.242716,-0.238596],[4.238328,-8.807181,-7.230439,-0.287055,-5.980013,4.136777,0.704983,-0.549088,-2.656745,2.064454,7.319332,-4.364497,2.902168,0.306486,-3.571340,1.330328,9.243696,-7.052114,-6.128727,-5.135241,4.035866,-0.334367,9.198204,0.961096,-8.685455,-1.053919,-3.426465,8.592067,-9.315635,-6.935205,-9.859904,9.014355,3.755669,9.258737,-8.151327,-5.133337,6.594581,3.485629,2.133660,9.945528,9.566847,-1.404666,-8.202775,1.061535,-8.578051,4.473103,-5.993776,-0.877716,6.255123,5.512040,0.954681,3.001526,-4.359655,1.432562,3.001586,0.492861],[-8.119985,-9.269262,5.029358,-6.926819,3.268645,-3.229309,-0.007842,5.740819,6.285403,3.122241,0.905107,0.779223,5.051421,3.761292,9.410718,-9.545302,-3.680311,9.155271,-9.022019,5.693833,7.094122,9.110151,-9.082889,5.613930,6.713413,-0.482276,1.723713,-2.993612,0.601102,5.179978,-1.844370,-8.501113,1.597160,-0.046913,3.049785,1.870658,-5.208961,-6.876502,-2.423062,-6.162826,0.135508,-9.087514,-8.407105,1.398959,-7.652234,5.990909,-2.656008,-4.707651,2.605299,-1.194277,-3.732573,9.648584,-2.973278,-7.564991,-9.146567,1.303128],[8.172250,-2.437462,-6.507160,3.060743,4.815601,-2.182699,7.985455,8.744887,9.680078,4.726829,7.035314,-9.507769,2.271565,-9.393509,8.583664,3.695366,4.760221,7.831033,9.851387,8.053325,1.396605,8.169183,-5.486256,5.623731,-3.193317,7.958899,6.398584,4.137567,-7.056335,-7.948069,0.174866,5.493155,-0.213494,3.740727,5.652347,-5.083179,-3.789995,1.939805,-4.233846,-4.390577,-0.344590,-0.105650,-4.853465,-0.523140,-0.006434,-7.629500,-7.278910,-7.939212,-6.348621,-2.730459,-4.975948,-6.151411,-4.121982,9.066509,-8.942555,3.870556],[-1.861605,8.363376,-4.462574,1.894205,-2.628986,-9.261978,1.643454,7.004501,-2.349656,-8.753707,-0.140974,3.063919,-4.814287,9.312665,1.656092,1.763424,8.052928,-8.530773,-9.298324,-1.174972,9.502817,6.430032,0.164302,5.505586,6.998519,8.228635,-7.084991,-9.514706,5.027453,-8.761911,0.732279,-8.666893,-6.747973,-5.754929,7.014545,1.129941,4.055320,1.240760,-6.300402,5.949385,-1.817232,5.421182,7.510153,-5.217492,-7.187434,9.721749,-2.135142,-5.612772,-1.061720,-4.194135,5.033831,2.144592,-6.273890,6.133922,1.785571,-4.561273],[1.409112,-8.202721,-9.126314,-2.390155,6.599927,-5.879478,2.537201,-9.879578,8.399686,5.116206,8.904370,9.732072,-1.307043,-9.779574,4.421454,5.960570,-4.303564,-1.723226,-9.735930,2.024955,-7.128479,-2.254691,-7.978429,-0.580179,0.343837,-4.282961,-6.241406,-9.461228,9.032157,-3.497936,-4.338625,1.570518,0.123832,8.290464,-4.833750,-6.084531,-5.965677,4.927359,7.863655,-4.778916,9.832005,6.329423,-1.155384,-3.253330,-4.167290,6.626593,0.783787,-1.782429,-5.414218,-1.730630,-4.405521,0.212776,6.419507,-1.115069,-6.054907,0.304049],[4.015386,7.500180,4.576953,6.557129,-2.042078,-5.515468,-4.649376,5.815845,-8.677231,5.160183,-5.683634,3.902206,0.434806,-1.334273,-7.348094,-0.791783,5.218486,2.488682,7.482948,-8.104309,8.665489,1.121651,0.256593,-4.089363,0.842077,4.294584,8.411985,3.616120,-6.692159,-1.635475,-0.697914,-8.282675,2.968942,-3.724317,0.690223,-3.138406,5.550847,-9.107102,-0.878991,-5.133778,-7.496277,7.178998,-4.604737,8.269817,9.513293,1.052405,-9.870684,2.352837,0.704521,-4.109586,-1.329666,-3.711532,7.988448,6.661135,2.518406,9.212874]], dtype = "float32")#candidate|4316|(32, 56)|const|float32
call_4314 = relay.TupleGetItem(func_3367_call(relay.reshape(var_4315.astype('float64'), [12, 14, 14]), relay.reshape(const_4316.astype('float32'), [1792,]), ), 2)
call_4317 = relay.TupleGetItem(func_3370_call(relay.reshape(var_4315.astype('float64'), [12, 14, 14]), relay.reshape(const_4316.astype('float32'), [1792,]), ), 2)
output = relay.Tuple([call_4301,call_4305,var_4306,call_4308,call_4314,var_4315,const_4316,])
output2 = relay.Tuple([call_4302,call_4307,var_4306,call_4309,call_4317,var_4315,const_4316,])
func_4318 = relay.Function([var_4306,var_4315,], output)
mod['func_4318'] = func_4318
mod = relay.transform.InferType()(mod)
mutated_mod['func_4318'] = func_4318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4318_call = mutated_mod.get_global_var('func_4318')
var_4320 = relay.var("var_4320", dtype = "int16", shape = (840, 1))#candidate|4320|(840, 1)|var|int16
var_4321 = relay.var("var_4321", dtype = "float64", shape = (2352,))#candidate|4321|(2352,)|var|float64
call_4319 = func_4318_call(var_4320,var_4321,)
output = call_4319
func_4322 = relay.Function([var_4320,var_4321,], output)
mutated_mod['func_4322'] = func_4322
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4338 = relay.const([[[-10,4,8,-7,-4,10,10],[8,2,-8,3,-6,3,-9],[5,-6,-9,-8,-8,-8,3]],[[-6,9,-2,9,5,-5,5],[1,5,-10,-1,-5,7,-6],[-8,2,-4,9,4,-4,-1]],[[4,-9,8,8,-6,6,-10],[5,-8,4,6,-3,-4,2],[-7,-6,-9,-3,8,-6,2]],[[8,-6,9,7,-6,-1,-7],[-5,2,-3,3,5,10,9],[10,9,7,-4,-3,-10,-3]],[[7,8,2,-6,-10,9,-6],[1,-7,9,2,5,-2,6],[-7,-3,-2,8,2,-8,-4]],[[-10,-8,-6,-3,-4,10,-8],[8,-2,-4,9,9,7,-3],[6,6,8,8,-10,6,5]],[[-5,-8,-8,8,-7,-5,8],[8,10,1,-1,-9,-10,9],[7,3,8,5,-10,-7,1]],[[3,-7,-3,6,-3,2,5],[5,7,7,-1,1,-10,-10],[10,-10,-3,4,2,-9,-7]],[[10,-2,-6,-6,10,8,5],[2,7,-9,5,-2,7,10],[-10,8,7,-5,-10,5,-8]],[[1,3,9,5,4,9,8],[-1,-5,-5,3,4,6,8],[-7,-6,-2,-2,-10,-10,-7]],[[-2,6,-5,-4,-5,-4,-4],[-6,-4,1,-1,-1,-5,-2],[-5,5,-5,-1,-3,3,-4]],[[8,9,-2,-6,5,7,2],[6,8,-2,9,5,10,-6],[5,-3,-8,10,-7,3,4]],[[9,4,10,9,7,9,-9],[-10,-5,-7,-10,3,4,-6],[4,-9,-8,8,-6,-9,-6]],[[-3,-1,-2,-9,-7,5,-1],[-7,-8,-1,-4,9,-8,-1],[-8,-7,-6,5,5,8,-5]]], dtype = "uint64")#candidate|4338|(14, 3, 7)|const|uint64
var_4339 = relay.var("var_4339", dtype = "uint64", shape = (14, 3, 7))#candidate|4339|(14, 3, 7)|var|uint64
bop_4340 = relay.left_shift(const_4338.astype('uint64'), relay.reshape(var_4339.astype('uint64'), relay.shape_of(const_4338))) # shape=(14, 3, 7)
func_2700_call = mod.get_global_var('func_2700')
func_2701_call = mutated_mod.get_global_var('func_2701')
call_4345 = func_2700_call()
call_4346 = func_2700_call()
func_3131_call = mod.get_global_var('func_3131')
func_3133_call = mutated_mod.get_global_var('func_3133')
call_4353 = relay.TupleGetItem(func_3131_call(), 0)
call_4354 = relay.TupleGetItem(func_3133_call(), 0)
output = relay.Tuple([bop_4340,call_4345,call_4353,])
output2 = relay.Tuple([bop_4340,call_4346,call_4354,])
func_4355 = relay.Function([var_4339,], output)
mod['func_4355'] = func_4355
mod = relay.transform.InferType()(mod)
var_4356 = relay.var("var_4356", dtype = "uint64", shape = (14, 3, 7))#candidate|4356|(14, 3, 7)|var|uint64
output = func_4355(var_4356)
func_4357 = relay.Function([var_4356], output)
mutated_mod['func_4357'] = func_4357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3691_call = mod.get_global_var('func_3691')
func_3693_call = mutated_mod.get_global_var('func_3693')
call_4364 = relay.TupleGetItem(func_3691_call(), 0)
call_4365 = relay.TupleGetItem(func_3693_call(), 0)
func_3291_call = mod.get_global_var('func_3291')
func_3293_call = mutated_mod.get_global_var('func_3293')
var_4397 = relay.var("var_4397", dtype = "int64", shape = ())#candidate|4397|()|var|int64
call_4396 = relay.TupleGetItem(func_3291_call(relay.reshape(var_4397.astype('int64'), [])), 2)
call_4398 = relay.TupleGetItem(func_3293_call(relay.reshape(var_4397.astype('int64'), [])), 2)
func_3291_call = mod.get_global_var('func_3291')
func_3293_call = mutated_mod.get_global_var('func_3293')
call_4403 = relay.TupleGetItem(func_3291_call(relay.reshape(var_4397.astype('int64'), [])), 1)
call_4404 = relay.TupleGetItem(func_3293_call(relay.reshape(var_4397.astype('int64'), [])), 1)
func_1292_call = mod.get_global_var('func_1292')
func_1296_call = mutated_mod.get_global_var('func_1296')
var_4410 = relay.var("var_4410", dtype = "float64", shape = (36,))#candidate|4410|(36,)|var|float64
const_4411 = relay.const([5,-8,6,6,2,-9,-7,-4,9,1,-9,10,-1,-1,3,5,-9,-8,10,5,1,6,-2,8,-6,-1,-1,4,-8,-9,2,-8,6,10,-3,9,-8,1,-7,-3,-10,-9,-7,-3,7,-5,-3,-2,10,-8,-4,6,-3,-3,-10,5,-1,8,-9,-3,10,-5,-1,-5,-6,6,9,-3,-1,-5,3,8,6,3,9,-2,-4,-4,-2,5,-2,-10,-3,5,1,6,10,9,-1,3,-10,9,-2,6,5,-3,-2,-10,-8,-2,5,-3,1,-2,8,-2,-10,10,-7,-5,-10,9,-1,-1,-4,-8,-9,5,-4,-2,-2,-1,-7,-4,9,-5,6,-5,3,-6,8,-9,6,7,-10,-2,-5,-5,-4,-5,8,4,-5,3,-4,6,-2,1,8,-7,10,3,2,8,-6,-3,-4,-10,-7,-7,-9,-4,-10,10,4,-8,-7,-8,10,-9,10,3,-8,-2,-4,-5,-4,6,4,3,3,2,6,-1,7,-3,1,-8,-6,1,9,-5,-6,8,4,8,7,-7,10,-7,9,4,5,8,-4,3,6,-8,-6,-2,10,-10,-10,1,-7,8,10,6,4,9,3,-1,8,9,8,6,1,-6,-5,10,-5,7,-10,1,7,2,-9,-8,4,1,-9,9,-5,3,-10,-3,3,8,-5,7,-8,9,-4,4,-4,-8,-4,-7,2,8,-2,6,-2,-9,5,6,-5,-1,-4,6,2,5,1,-4,1,-4,4,10,-6,3], dtype = "uint16")#candidate|4411|(280,)|const|uint16
const_4412 = relay.const([5,8,8,10,1,8,-9,-7,3,-8,1,-8,-10,-10,-4,-3,-4,4,2,3,-10,-7,-9,2,2,-8,-4,4,1,-6,-8,5,-10,1,4,5,-5,1,-9,-6,4,4,2,-1,-3,-7,8,10,-10,-1,-4,-6,-1,3,-3,2,4,-5,-5,9,-5,-6,6,-2,6,-1,-10,-1,6,-2,4,-6,10,-5,10,-3,-10,-10,7,-5,3,-5,-4,5,-10,-1,-1,-5,10,7,3,7,-1,2,-6,10,4,2,4,8,-4,-10,-5,7,-4,7,6,-3,-8,-4,-3,-4,2,2,5,9,10,6,4,-3,8,8,-2,1,-7,4,1,-6,6,-6,10,10,-5,-7,10,7,-8,3,7,1,1,3,-5,-5,-7,-4,8,-8,2,2,-5,-1,-8,-4,2,-9,1,5,1,9,-10,-6,6,-1,-9,-10,6,7,10,8,-5,7,9,3,1,-9,-4,-1,-8,9,-9,-4,-2,8,-2,-4,-3,4,2,-1,1,7,-2,-6,-1,2,3,5,-6,-9,-9,-5,5,-4,9,1,-3,5,-7,10,5,-7,5,-8,-7,9,-2,-8,-6,-4,-8,-6,3,8,2,7,-9,10,10,-5,4,5,-8,3,-7,-10,-3,-6,8,8,4,-9,-2,7,6,-9,5,8,-8,9,1,-10,4,3,-4,1,-6,10,-9,10,-6,8,6,5,9,9,3,-4,-9,-10,8,10,-4,-2,7,8,2,7,4,-1,-7,-2,-2,-7,5,-6,1,-7,-8,7,10,9,3,-9,9,9,2,4,2,-7,-1,10,-8,-6,-3,-2,-8,4,-8,-6,4,-2,-9,-10,-10,-7,-9,4,3,6,2,-8,10,2,4,-4,5,5,-2,6,4,-2,10,10,5,9,3,-6,9,10,5,-4,-2,6,-5,-6,6,2,6,-1,-8,-6,6,-4,1,-8,10,9,-2,7,-7,-4,3,-3,8,9,2,6,9,-5,-4,9,7,-5,4,6,-7,8,-8,8,-3,-1,4,7,7,-6,-6,-4,-4,2,3,3,8,-9,-2,-2,5,4,-1,3,-2,9,-3,-1,-2,-8,10,-4,-3,-5,-1,4,8,-3,8,7,4,-9,8,7,4,-6,7,3,2,-6,4,-7,7,-3,10,4,5,3,3,5,3,2,-1,9,2,4,-7,-8,5,-9,1,-8,-7,2,-9,9,-8,4,-5,-3,-10,3,-2,-2,-4,1,-6,-4,10,-5,4,-2,5,4,-9,-7,3,-8,2,-3,3,-2,3,-4,-1,-3,-4,-9,-1,9,9,-10,-9,-9,-2,-7,-4,-6,4,-1,10,2,-9,1,4,-1,-9,5,-3,8,5,-2,6,-10,-7,-7,-5,1,2,7,3,8,10,9,-8,-9,-4,-5,-9,1,6,-3,9,-8,-5,6,2,1,7,-5,8,-9,-3,3,9,-9,3,7,-7,2,7,-1,2,-1,1,6,-8,-4,-9,-4,-10,-5,-7,5,-7,-6,-5,-3,9,7,-10,1,-8,-2,1,-7,-8,-6,-5,9,-9,6,9,10,5,-10,-10,4,4,-5,1,8,4,-6,-4,-1,-9,-7,-8,6,4,-10,-7,-2,-2,7,-1,-5,-6,6,-8,-3,5,3,6,-9,-7,7,-7,6,8,-3,6,-5,-2,4,-9,-5,6,-8,-1,-3,9,-2,-8,6,-2,6,8,2,-2,8,-5,6,2,4,-4,-2,6,7,-2,10,3,-2,7,1,-4,3,-3,-1,-6,10,1,-2,6,2,4,4,10,-6,-3,8,-7,7,3,-9,-2,-8,-1,-1,-10,6,7,-1,7,-5,6,8,-6,5,2,10,-1,8,-1,-10,3,4,8,-6,3,-7,-5,-2,9,-4,-1,4,3,3,-2,4,1,-5,5,3,-5,9,-5,-4,-8,5,3,1,-3,9,-9,3,4,8,1,9,2,-9,9,-1,-2,-6,8,-10,-4,-6,-3,-5,-9,6,2,8,-3,1,10,9,-10,6,2,7,-6,-3,4,-8,8,-4,9,-8,-9,-4,-3,-3,-8,9,7,-8,-2,2,8,10,-3,-8,-6,-7,-5,6,-6,1,7,3,-9,-7,-1,-9,-10,-5,-1,7,1,-4,7,-6,-8,6,-8,-1,2,-8,-8,2,-5,-1,3,-4,4,-5,-8,3,-10,5,-7,-7,-6,-2,3,2,-4,-4,1,-5,8,5,1,-3,-6,-10,-5,-4,3,5,3,-4,10,-5,-8,7,8,-1,1,-1,2,-2,10,8,-3,1,-10,-2,-5,-5,-7,8,-4,4,4,-4,9,-3,-3,2,6,3,-8,-8,2,-7,-6,4,-3,7,8,-4,-9,-5,10,10,1,-3,10,4,-5,-3,-6,-2,9,-10,3,1,-3,-6,-4,-10,-2,7,-4,-4,-4,1,5,-10,-7,9,-4,-3,9,-3,-8,9,6,1,-7,-3,3,-2,9,1,2,-7,-2,-5,-10,1,1,-7,6,-9,3,5,-5,-4,-8,-2,5,-9,2,6,-4,1,1,-4,-7,1,6,8,2,8,7,10,-1,-8,5,-6,-5,4,-6,2,-3,3,-8,1,-3,9,10,1,-8,-4,-7,2,9,7,-6,7,3,-1,1,10,-2,1,8,-3,2,-9,-10,-2,-9,-2,-9,6,-9,2,8,1,1,-2,-5,-5,-4,6,5,5,-7,9,-8,-10,2,8,-4,-2,2,-5,-10,-3,-5,2,-9,4,-6,3,-7,-10,3,-1,-6,5,8,6,-10,-4,-10,-5,-5,-4,-1,4,8,-1,3,-1,6,8,5,3,3,-10,-6,-1,-3,2,1,-6,-2,-3,8,4,9,-9,6,-10,1,-3,5,8,8,-4,7,-10,-6,4,7,9,9,-2,1,-5,2,-9,-1,-4,10,10,7,-6,2,-8,-5,-7,-6,1,-1,-10,-2,9,-8,2,1,3,1,1,-9,-6,-6,1,4,-9,-8,-7,8,6,8,-1,-2,-5,4,-8,-4,9,7,-2,-2,5,10,2,9,1,8,4,-8,10,-6,-7,3,2,6,1,7,-9,2,-4,-9,-8,-8,-4,-3,8,-5,2,1,-7,8,-4,-8,1,-4,10,-1,-10,-1,7,9,5,-10,-1,3,-7,-8,7,6,5,-4,-3,1,5,-6,-6,-8,8,-2,-1,8,7,1,-1,1,-4,1,1,1,-4,8,3,-4,6,-1,-8,-4,-5,8,-1,2,-5,5,6,2,2,-1,8,7,1,2,6,-4,-3,7,-3,-1,3,-4,1,-9,6,9,7,-9,-3,8,6,-10,-6,5,5,8,2,-5,6,8,-5,-7,3,9,-4,5,8,-3,2,4,3,-3,5,-2,3,-4,-8,-1,4,9,6,2,-1,10,2,-9,7,-4,2,-3,7,-3,6,-8,-1,-10,2,3,-6,7,7,5,-7,-6,4,-4,-7,-7,-1,7,3,1,9,1,6,-5,3,7,-8,1,-4,-4,3,8,-8,8,-10,9,2,7,9,1,2,3,2,-4,2,1,-9,9,-2,9,5,-5,7,5,6,7,5,-7,-6,5,-9,5,-5,-3,1,-1,9,3,8,9,3,1,6,5,1,1,-8,7,-1,10,-4,10,9,-7,-1,-2,-4,2,-2,-3,-1,-2,3,4,-10,9,7,5,-3,2,3,-10,-8,-7,1,3,6,-3,-5,-6,1,-8,5,4,-10,-1,2,-7,4,-3,6,9,3,3,-8,4,-4,-8,8,4,10,-10,-7,-5,3,-5,5,-10,-5,6,-2,3,-5,-3,-2,-4,2,-7,2,-9,-1,3,8,4,-8,7,3,4,-10,2,5,4,-9,-8,6,-8,-2,3,-6,-3,7,4,7,-9,-6,9,-8,-1,-8,10,6,9,10,-6,-8,3,-9,5,-5,-5,7,4,-8,4,4,10,-3,8,2,2,-4,-5,-1,1,7,9,-9,-1,6,5,-1,-1,-5,-8,2,-6,4,-9,2,-3,5,4,2,3,5,9,-6,-10,7,7,-9,-8,-4,10,-7,4,-2,6,-8,-4,-10,8,-5,-6,-8,4,5,2,8,-5,4,7,-2,4,3,-2,2,8,8,-10,8,-4,7,-2,10,10,-1,-4,1,2,5,-8,3,4,1,-8,9,1,1,-9,-3,7,-5,6,6,-9,-1,7,4,-5,-3,-3,6,8,-7,8,-5,3,-3,-5,6,-9,-2,1,6,-10,-9,-3,7,4,-8,6,-7,-5,-8,9,-6,-9,5,-4,-5,3,-7,1,-10,10,7,-3,-4,5,1,-6,-4,-5,4,-1,-4,-5,3,-7,-10,2,2,2,-6,-8,10,-1,-8,3,-6,4,-1,2,-4,-10,7,-4,9,-7,-10,9,-8,4,9,-1,-2,-6,4,8,1,4,9,-9,3,-1,-2,3,-5,7,4,10,2,10,5,4,5,-4,-6,-3,10,2,-8,-3,3,6,7,-3,1,-7,-3,-4,8,3,2,1,-3,3,7,2,-5,7,-6,5,6,-6,10,7,10,2,-7,-6,-7,2,7,3,-4,-8,-5,-8,2,9,-5,-3,-8,1,-9,6,7,7,-1,8,5,6,8,10,-9,3,5,1,1,1,-8,-4,-4,-9,-5,2,4,7,-1,1,6,-4,-9,6,-6,2,3,-8,-8,4,7,-3,-4,-10,-9,-7,-4,8,7,-5,-9,8,2,-1,-7,4,-2,3,-9,-3,4,3,-2,-1,-5,3,-5,7,8,-8,4,-9,2,2,-6,10,-6,8,-6,-8,-9,-6,-3,2,1,-8,-3,-9,10,-6,8,-6,3,-4,-5,1,-5,-8,7,10,9,3,7,-9,-5,3,5,8,5,8,-4,6,5,8,4,-2,-7,9,8,1,4,-7,-3,-8,8,-8,4,-2,8,1,-9,8,-7,-8,-4,-8,-2,9,9,4,1,10,8,4,-3,9,-7,5,-2,1,-3,6,6,-3,-3,2,10,1,7,3,10,9,-7,-1,1,-6,-3,-2,-2,-3,3,-10,1,-1,7,-6,6,-4,2,-5,-7,9,-5,-8,7,1,9,3,5,6,-9,-8,-10,9,6,-6,5,7,-6,9,6,-1,3,5,-9,-9,3,-1,-8,4,-4,-10,-6,3,2,3,-3,-5,10,6,8,6,-5,-6,-9,8,3,-6,-7,-10,10,8,-10,4,10,-9,-7,2,4,-4,10,-10,-4,-1,5,9,-5,-3,-8,6,6,8,10,5,10,1,-5,-5,9,-9,7,2,-5,-8,-1,-2,-10,10,2,6,-7,4,-9,-1,4,3,-8,-5,9,5,-8,6,-7,9,-6,-1,-3,-6,-3,1,5,-9,8,-5,7,-6,6,4,10,3,10,10,-9,8,-1,7,2,10,-10,-4,4,-2,3,6,-1,9,2,-7,-4,-3,5,-5,-6,4,10,2,9,8,4,-5,-2,-8,-4,7,3,4,-10,2,4,5,-7,1,3,-8,-3,3,7,-10,-8,10,-7,-9,5,-6,-9,-6,7,2,7,6,3,5,-3,-3,-4,-4,9,-9,-5,5,5,10,-1,4,10,-7,-1,5,7,-5,-10,1,10,-4,-6,-9,-4,-7,-1,2,10,6,-2,-5,8,-10,-1,-8,5,-8,-4,-6,-7,-3,3,-10,3,-8,9,-3,-5,5,-8,-9,-8,-5,-5,1,3,10,7,3,-8,-4,4,1,-4,5,1,4,2,-4,-10,9,-8,3,9,-7,7,-1,3,-10,10,7,-1,3,-2,-10,-1,-8,-8,-6,9,3,9,4,-7,6,-2,-3,6,6,-2,-10,7,-3,3,1,5,5,-9,-5,-5,-6,-6,10,4,9,4,2,-1,6,6,-3,1,-4,-1,9,-10,5,-3,-9,2,-4,9,-8,10,-4,1,-7,7,5,2,6,-6,-1,7,-5,-8,-5,-4,9,7,2,1,10,-5,-8,6,1,6,-2,-2,1,-7,-8,1,7,-3,6,2,-3,-1,-4,-8,1,-6,8,2,-9,8,-10,-7,7,-9,5,8,-6,1,-6,-6,-5,-9,-2,2,10,1,9,8,-9,8,6,-3,3,-6,-3,5,7,-10,-7,-10,-2,-4,8,-8,8,-2,2,-1,-9,3,9,9,3,5,-2,4,6,7,-1,3,-1,-6,-10,7,3,-1,-9,8,-2,4,8,9,8,-7,9,10,5,-2,-2,2,8,-10,4,10,3,-9,2,4,-4,-10,-1,4,8,-10,-2,10,6,6,7,7,10,10,5,-3,-5,3,-5,1,-2,8,5,-5,-5,2,-9,-2,8,10,-6,-4,5,-6,-2,-8,9,-8,1,7,4,-9,-10,-1,-3,-4,1,-9,-3,9,-3,2,10,-8,5,8,-5,-2,8,-5,-4,1,7,4,-6,-9,-9,-4,-3,1,-8,-7,3,-1,-5,-3,7,6,3,-8,-2,-9,8,-1,6,8,10,10,-7,6,9,-10,-1,-2,6,-5,-7,-7,-8,5,-10,-1,-8,-6,3,-6,-1,-1,-3,-9,3,7,-6,4,-5,-9,1,5,-10,2,-3,6,-5,6,-9,8,7,-3,-2,-9,5,-1,-8,6,7,9,-6,-6,3,-10,-7,6,6,10,-6,2,-7,-10,9,-10,3,10,8,10,-8,-2,1,-2,9,2,1,9,-8,2,6,-6,5,6,-2,3,-7,6,4,4,7,1,1,-7,-10,6,3,4,-10,1,7,3,-10,-3,-4,-10,-4,-3,10,1,9,5,-3,-1,-9,6,-8,-3,7,-5,-4,6,-5,-10,6,-6,-3,8,1,-1,-4,8,8,-2,-7,8,3,9,2,4,5,5,-2,3,4,4,5,-2,1,-9,-1,4,-10,4,4,-10,-2,8,9,7,-7,3,-3,4,9,6,10,-5,-3,-2,1,-10,8,6,9,-1,6,-8,-9,5,-6,9,9,6,-5,10,2,-8,8,-8,-7,3,4,-2,-6,10,-6,-9,3,8,6,5,-10,10,6,4,8,-9,-1,-3,8,10,-4,-10,6,4,-7,-4,1,6,-2,3,10,-2,2,7,-1,-3,-7,2,2,9,-7,8,-9,-7,5,-10,-3,5,10,-5,-10,-5,-1,4,7,5,-8,-3,-7,7,2,8,-2,1,6,2,-4,7,-8,-1,6,-8,-8,1,-1,1,8,9,6,-1,-5,10,-3,-7,10,3,-5,-2,2,-10,4,10,-5,-1,10,3,6,-5,2,10,-1,8,6,8,-3,-4,-2,-10,-3,7,-4,9,4,1,-7,8,3,-3,-5,-8,-1,-7,7,9,-10,-3,9,-6,-3,10,5,-7,5,-9,1,1,2,-5,7,8,2,-2,1,-5,5,6,3,-10,3,9,1,-6,-7,-1,-6,-2,8,1,-1,6,2,-6,5,-1,9,4,9,-2,-10,-3,-2,5,10,-1,-2,9,-9,7,4,4,-10,-1,8,-9,6,5,8,8,-7,1,6,-3,6,10,-2,3,-5,-4,10,1,5,4,9,-3,10,8,-5,-2,-3,-3,9,10,10,4,5,-6,5,-4,-3,-1,-1,1,-9,9,5,8,5,5,10,-5,-9,7,-2,-6,-8,-8,-5,-8,-1,-6,-8,10,2,9,9,1,7,-1,9,-2,6,9,-8,-6,2,5,6,-3,3,4,-10,-9,1,5,-9,8,-6,9,-3,-3,6,-5,5,5,-4,7,2,-10,-8,-6,2,4,-2,-4,-9,10,-8,10,-4,9,-3,-1,-4,9,-4,9,-10,5,-8,-5,-9,2,9,-9,8,1,6,-6,1,-2,-2,-4,-6,4,-2,-2,-5,8,-8,-9,5,-6,1,1,9,10,4,6,3], dtype = "uint8")#candidate|4412|(2925,)|const|uint8
call_4409 = relay.TupleGetItem(func_1292_call(relay.reshape(var_4410.astype('float64'), [3, 12, 1]), relay.reshape(const_4411.astype('uint16'), [280,]), relay.reshape(const_4412.astype('uint8'), [2925,]), ), 7)
call_4413 = relay.TupleGetItem(func_1296_call(relay.reshape(var_4410.astype('float64'), [3, 12, 1]), relay.reshape(const_4411.astype('uint16'), [280,]), relay.reshape(const_4412.astype('uint8'), [2925,]), ), 7)
output = relay.Tuple([call_4364,call_4396,var_4397,call_4403,call_4409,var_4410,const_4411,const_4412,])
output2 = relay.Tuple([call_4365,call_4398,var_4397,call_4404,call_4413,var_4410,const_4411,const_4412,])
func_4414 = relay.Function([var_4397,var_4410,], output)
mod['func_4414'] = func_4414
mod = relay.transform.InferType()(mod)
var_4415 = relay.var("var_4415", dtype = "int64", shape = ())#candidate|4415|()|var|int64
var_4416 = relay.var("var_4416", dtype = "float64", shape = (36,))#candidate|4416|(36,)|var|float64
output = func_4414(var_4415,var_4416,)
func_4417 = relay.Function([var_4415,var_4416,], output)
mutated_mod['func_4417'] = func_4417
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4429 = relay.var("var_4429", dtype = "float64", shape = (14, 10, 12))#candidate|4429|(14, 10, 12)|var|float64
uop_4430 = relay.atanh(var_4429.astype('float64')) # shape=(14, 10, 12)
uop_4435 = relay.asinh(uop_4430.astype('float32')) # shape=(14, 10, 12)
output = uop_4435
output2 = uop_4435
func_4442 = relay.Function([var_4429,], output)
mod['func_4442'] = func_4442
mod = relay.transform.InferType()(mod)
var_4443 = relay.var("var_4443", dtype = "float64", shape = (14, 10, 12))#candidate|4443|(14, 10, 12)|var|float64
output = func_4442(var_4443)
func_4444 = relay.Function([var_4443], output)
mutated_mod['func_4444'] = func_4444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_4493 = relay.TupleGetItem(func_1632_call(), 0)
call_4494 = relay.TupleGetItem(func_1633_call(), 0)
func_1839_call = mod.get_global_var('func_1839')
func_1841_call = mutated_mod.get_global_var('func_1841')
call_4504 = relay.TupleGetItem(func_1839_call(), 2)
call_4505 = relay.TupleGetItem(func_1841_call(), 2)
var_4508 = relay.var("var_4508", dtype = "uint8", shape = (2925,))#candidate|4508|(2925,)|var|uint8
bop_4509 = relay.power(call_4504.astype('float64'), relay.reshape(var_4508.astype('float64'), relay.shape_of(call_4504))) # shape=(2925,)
bop_4512 = relay.power(call_4505.astype('float64'), relay.reshape(var_4508.astype('float64'), relay.shape_of(call_4505))) # shape=(2925,)
func_1742_call = mod.get_global_var('func_1742')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_4524 = relay.TupleGetItem(func_1742_call(), 3)
call_4525 = relay.TupleGetItem(func_1744_call(), 3)
func_3061_call = mod.get_global_var('func_3061')
func_3064_call = mutated_mod.get_global_var('func_3064')
var_4527 = relay.var("var_4527", dtype = "int32", shape = (280,))#candidate|4527|(280,)|var|int32
call_4526 = relay.TupleGetItem(func_3061_call(relay.reshape(var_4527.astype('int32'), [7, 8, 5]), relay.reshape(var_4527.astype('int32'), [7, 8, 5]), ), 2)
call_4528 = relay.TupleGetItem(func_3064_call(relay.reshape(var_4527.astype('int32'), [7, 8, 5]), relay.reshape(var_4527.astype('int32'), [7, 8, 5]), ), 2)
output = relay.Tuple([call_4493,bop_4509,call_4524,call_4526,var_4527,])
output2 = relay.Tuple([call_4494,bop_4512,call_4525,call_4528,var_4527,])
func_4549 = relay.Function([var_4508,var_4527,], output)
mod['func_4549'] = func_4549
mod = relay.transform.InferType()(mod)
var_4550 = relay.var("var_4550", dtype = "uint8", shape = (2925,))#candidate|4550|(2925,)|var|uint8
var_4551 = relay.var("var_4551", dtype = "int32", shape = (280,))#candidate|4551|(280,)|var|int32
output = func_4549(var_4550,var_4551,)
func_4552 = relay.Function([var_4550,var_4551,], output)
mutated_mod['func_4552'] = func_4552
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4594 = relay.var("var_4594", dtype = "float32", shape = (13, 10, 1))#candidate|4594|(13, 10, 1)|var|float32
uop_4595 = relay.sinh(var_4594.astype('float32')) # shape=(13, 10, 1)
func_354_call = mod.get_global_var('func_354')
func_358_call = mutated_mod.get_global_var('func_358')
const_4601 = relay.const(10, dtype = "int64")#candidate|4601|()|const|int64
const_4602 = relay.const([[7,2,1,-9,8,1,-3,2,-1,-7,-7,-3,10],[-1,9,-6,3,4,-8,10,-5,1,-7,-7,5,5],[10,-4,5,-3,3,1,-9,-2,7,6,-5,2,-1],[2,-3,-10,4,5,-1,4,-10,-10,1,6,3,2],[9,10,2,-6,9,-2,-1,-2,5,-6,2,-4,7],[-1,-3,8,6,4,10,-7,-9,1,5,-2,-1,7],[-6,6,-2,2,9,-9,-8,5,6,-8,-8,-3,-4],[5,-7,9,-7,5,-2,-7,6,4,-1,-3,-10,2],[-2,2,1,-1,4,-10,-7,-10,-3,-7,-5,5,1],[-4,1,-10,-10,10,2,10,5,4,-8,-8,1,1],[10,3,6,-2,-1,1,-5,-5,-6,2,6,1,2],[4,-7,-1,-1,-8,-10,-3,5,4,-6,-10,3,-2],[-9,2,4,-7,1,8,10,8,-8,-3,-4,6,6],[-10,7,-10,5,-8,-10,-10,2,-6,5,4,-4,10],[-6,7,2,4,1,8,8,7,-2,2,6,-6,-9],[-8,-9,-10,-7,-8,-6,10,6,3,3,-3,-6,7],[-10,-5,-5,-3,-3,9,2,9,-10,3,-5,10,-6],[-3,6,6,-4,7,6,-2,-3,-9,10,2,4,-4],[4,9,4,4,-1,-6,-3,-2,2,-8,-7,-9,4],[7,-7,-9,4,2,-7,10,7,2,-10,9,-10,-7],[5,-6,-7,8,-3,-6,-4,-6,5,10,-1,-1,7],[-1,8,-6,3,-1,4,-8,-6,-5,-5,5,5,1],[8,-7,4,3,-7,3,2,2,-5,6,-7,6,-2],[-1,6,4,-5,-2,8,-9,6,-7,-7,-8,-1,6],[5,-9,2,-3,3,-4,-8,-7,2,3,9,-10,-1],[1,-3,10,-10,7,9,10,-7,10,1,-4,-1,-2],[-9,9,1,1,-6,3,10,-7,10,-10,-2,-6,6],[-7,-9,9,3,5,7,-9,-7,-8,2,5,-3,-3],[-3,-9,1,10,-6,5,7,5,-9,9,-7,-2,-4],[-5,10,-5,8,-6,1,8,-4,-9,6,7,8,-1],[6,-8,-10,9,-2,5,-10,1,-4,1,4,1,5],[7,-5,-10,2,1,-10,2,-7,-4,-7,-8,-5,-10],[-10,1,8,-9,-4,2,-7,-8,5,1,-6,-9,-1],[5,-6,5,6,9,3,5,-7,5,-1,-2,-10,8],[-9,10,-4,6,-10,5,-8,-9,4,-10,4,8,-8],[-2,5,-6,-7,-4,3,-10,-2,10,9,1,-7,8],[-8,-5,-5,5,-6,-4,-7,-3,-8,-5,6,-2,-5],[2,-6,3,5,8,-6,-1,4,-7,-4,3,-1,-4],[-4,-6,9,-10,8,-9,-1,4,2,2,-1,-10,9],[-10,-2,9,-3,4,5,-9,9,-6,8,10,5,5],[10,4,-9,-2,-1,8,8,-9,7,-5,-7,7,-9],[5,-10,2,8,-1,-2,-9,-6,8,10,-6,-5,-5],[10,-8,-10,6,3,-10,-4,7,4,1,-4,3,-6],[3,9,-4,10,1,4,10,5,-8,10,7,3,1],[6,-3,4,2,4,4,7,-5,-3,8,-2,-7,2],[-6,3,-4,3,9,-5,-1,-8,-4,8,-4,2,-9],[8,9,-1,7,-4,2,10,5,4,-6,-10,-5,-10],[1,3,-10,-7,3,6,1,2,-9,5,-10,9,9],[-8,2,-7,2,3,3,3,-8,-7,-10,2,-3,-3],[-6,-9,-4,3,-5,-8,-2,-10,-1,-2,-3,9,8],[-1,10,6,-6,5,1,5,8,-4,-6,-5,7,-7],[-6,4,-10,7,-8,-10,-7,4,2,-6,5,-1,4],[8,-3,4,3,-3,2,7,-2,-2,-1,-7,-10,-3],[2,-5,-2,-10,10,-4,1,-8,-7,10,-9,6,-3],[-2,7,7,1,-6,7,-10,9,9,-1,-4,1,6],[8,-9,9,3,9,5,-2,-7,-6,-3,8,8,1],[8,6,2,-9,7,4,-4,-10,5,10,10,-8,5],[-6,-7,-5,-7,-10,6,-9,9,-5,-8,-2,6,6],[1,10,2,-9,1,4,4,8,-5,-5,10,-5,-4],[3,2,7,-3,-9,2,-4,1,-2,1,-7,7,-1],[1,-7,-5,-6,-2,-10,1,-2,7,-6,3,5,10],[-2,-3,5,-9,8,5,-10,-8,-3,-10,-2,8,-5],[-7,-7,-2,3,-2,-1,3,4,5,6,-4,2,2],[1,1,-3,6,-5,-10,6,-7,10,8,9,-8,9],[-3,-8,-5,9,4,-4,3,-1,-8,-3,-5,6,-7],[-9,9,8,8,-9,4,-1,-9,9,6,4,-8,-10],[10,-8,-2,-3,-4,-5,9,-7,1,1,3,-3,-1],[-3,-4,4,1,-2,-1,-6,-7,9,-4,-1,4,-8],[-2,-4,-9,-2,1,6,9,5,-4,5,1,-9,2],[-1,-2,3,-1,8,5,-3,-7,-10,-9,-4,-5,4],[7,-2,-1,-5,-3,8,-7,-4,-8,1,-7,10,6],[-7,-7,9,-4,2,6,-10,-8,-5,-5,-9,7,8],[3,-10,-6,-1,9,6,3,-9,-5,-9,7,10,-4],[-7,-1,7,-5,-10,-5,3,-3,5,6,6,-3,6],[1,-2,-7,6,-3,9,-9,10,-1,7,-1,1,-6],[-1,-4,-9,-5,9,-1,9,9,6,8,-3,-9,5],[3,-9,5,-10,-9,5,3,7,1,9,-3,-10,-9],[9,3,9,-10,-7,-8,-3,7,10,-1,3,10,-4],[5,3,-6,3,4,5,10,-8,-8,-3,8,4,-10],[-3,-9,5,-8,-9,1,-2,-5,9,-9,-2,-6,4],[8,-5,-7,1,3,9,4,-6,1,10,-6,-1,-3],[-4,8,5,7,6,-8,9,5,-3,-7,4,6,6],[-2,-9,-10,6,-10,-5,2,-3,10,-2,-4,-4,3],[-1,-1,-2,-5,-7,-3,-6,5,2,-5,-8,8,10],[4,-3,1,7,-4,-4,-10,-6,6,-6,3,8,4],[3,-5,-4,-4,-7,4,6,3,-6,2,5,-2,-9],[-8,3,5,2,8,9,6,8,10,-5,-5,-5,3],[-5,9,-1,2,-7,-1,-7,8,2,3,-3,5,5],[10,-7,8,-9,-9,-5,6,8,-4,6,-2,-5,8],[6,-7,3,1,-2,5,9,4,5,-8,9,7,-4],[-4,3,-9,5,-2,-3,10,3,9,-9,3,-4,8]], dtype = "int64")#candidate|4602|(91, 13)|const|int64
const_4603 = relay.const([-9,-5,-5,4,7,-8,-8,1,10,-5,-3,-1,8,-9,9,1,-8,8,5,7,-1,-3,10,1,8,-7,10,-9,-5,5,4,-9,-4,-6,-1,3,10,5,9,-9,9,8,-6,-8,-9,5,2,-6,5,7,6,9,7,-9,-7,-5,-6,8,4,-5,10,6,5,2,5,7,-1,-1,-10,7,9,-6,5,-9,9,-1,5,4,-1,-2,-6,-10,-5,7,3,3,-8,-9,2,-1,3,3,-1,-1,-1,-9,-2,-6,-1,-2,-9,-8,-3,-9,6,-7,3,-8,5,7,2,7,-6,-3,-7,3,10,-4,-8,-8,-4,5,3,2,-5,-7,6,3,4,8,10,9,1,-3,-8,-5,-5,10,6,-7,-2,9,8,-9,-9,6,-6,-1,8,-10,-4,9,-5,-9,-4,3,-3,-5,4,3,-10,-5,4,5,-10,10,-2,-5,-1,-10,-3,10,-5,6,8,-5,8,5,7,-6,7,-5,7,7,-6,-3,-10,-6,-2,4,-4,8,-2,4,5,8,-9,2,-3,-6,-4,10,5,-8,-10,5,-3,6,6,-5,-1,4,4,-6,2,7,-2,-1,3,-2,-2,-7,-1,-2,-2,-9,-10,4,8,-2,-3,-8,6,-2,9,-5,4,-7,4,4,-6,2,-6,1,-8,6,-2,8,4,-10,-7,-3,7,-6,1,1,-10,5,-9,2,9,-1,-2,10,3,10,-7,1,-5,6,-4,3,-10,-2,5,8,-3,5,-2,-1], dtype = "uint16")#candidate|4603|(280,)|const|uint16
call_4600 = relay.TupleGetItem(func_354_call(relay.reshape(const_4601.astype('int64'), []), relay.reshape(const_4602.astype('int64'), [7, 13, 13]), relay.reshape(const_4603.astype('uint16'), [280,]), ), 1)
call_4604 = relay.TupleGetItem(func_358_call(relay.reshape(const_4601.astype('int64'), []), relay.reshape(const_4602.astype('int64'), [7, 13, 13]), relay.reshape(const_4603.astype('uint16'), [280,]), ), 1)
func_3798_call = mod.get_global_var('func_3798')
func_3800_call = mutated_mod.get_global_var('func_3800')
call_4606 = func_3798_call()
call_4607 = func_3798_call()
bop_4608 = relay.multiply(uop_4595.astype('int16'), const_4601.astype('int16')) # shape=(13, 10, 1)
uop_4632 = relay.atanh(bop_4608.astype('float32')) # shape=(13, 10, 1)
output = relay.Tuple([call_4600,const_4602,const_4603,call_4606,uop_4632,])
output2 = relay.Tuple([call_4604,const_4602,const_4603,call_4607,uop_4632,])
func_4640 = relay.Function([var_4594,], output)
mod['func_4640'] = func_4640
mod = relay.transform.InferType()(mod)
mutated_mod['func_4640'] = func_4640
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4641 = relay.var("var_4641", dtype = "float32", shape = (13, 10, 1))#candidate|4641|(13, 10, 1)|var|float32
func_4640_call = mutated_mod.get_global_var('func_4640')
call_4642 = func_4640_call(var_4641)
output = call_4642
func_4643 = relay.Function([var_4641], output)
mutated_mod['func_4643'] = func_4643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2864_call = mutated_mod.get_global_var('func_2864')
call_4704 = func_2863_call()
call_4705 = func_2863_call()
func_3632_call = mod.get_global_var('func_3632')
func_3634_call = mutated_mod.get_global_var('func_3634')
call_4706 = relay.TupleGetItem(func_3632_call(relay.reshape(call_4704.astype('float32'), [308, 1])), 0)
call_4707 = relay.TupleGetItem(func_3634_call(relay.reshape(call_4704.astype('float32'), [308, 1])), 0)
func_2425_call = mod.get_global_var('func_2425')
func_2426_call = mutated_mod.get_global_var('func_2426')
call_4708 = func_2425_call()
call_4709 = func_2425_call()
func_139_call = mod.get_global_var('func_139')
func_143_call = mutated_mod.get_global_var('func_143')
const_4728 = relay.const([-6,-9,-3,-1,1,1,-1,-8,-1,-10,6,-1,-9,-6,-1,8,-5,-10,9,3,7,5,-8,-9,-3,-4,-4,-9,9,-10,8,10,6,-2,-1,-5,10,6,-5,7,-3,-9,5,-2,5,7,-9,-5,-6,9,1,-6,8,-8,-9,2,-7,-1,-1,9,4,-7,2,9,2,-7,-6,3,7,6,8,9,9,10,-2,5,-4,2,-8,-7,-1,-3,-9,8,10,3,-1,3,-2,-9,-1,-4,-9,-10,7,5,-4,-2,5,-1,5,-2,6,-8,8,7,-2,-2,-9,-7,-4,2,-3,10,-8,2,5,-10,9,1,5,-7,-3,9,-5,-6,-1,6,-5,-1,-5,6,6,1,4,-5,4,-8,-4,6,-3,8,-3,7,1,2,-10,-6,-4,4,-10,7,-2,10,-1,-7,9,10,10,-1,-3,6,9,10,8,-3,2,4,-6,1,-1,2,4,3,9,-6,4,6,4,9,1,-4,-2,6,-3,5,-5,-3,1,4,9,-4,2,8,-7,9,9,-10,2,-10,5,6,-6,-9,-4,-9,-3,-5,3,10,-2,-8,2,3,4,-8,1,-8,-2,6,-10,-10,5,5,-1,-8,5,6,-3,-3,2,-5,3,2,10,5,10,-2,-3,3,-3,-8,8,-8,-3,-10,-10,10,8,-3,9,-8,-3,3,7,-1,10,1,-3,1,-9,1,-7,7,2,-6,7,-7,6,8,10,6,-1,10,-5,10,-3,3,1,-7], dtype = "uint16")#candidate|4728|(280,)|const|uint16
const_4729 = relay.const([9.898362,-3.138027,9.599955,6.975842,1.325921,-7.657792,4.978834,-1.891640,-9.923356,-1.540232,-7.274911,7.801380,8.723776,-4.670785,-3.356753,-1.983553,9.724502,-4.636822,0.724049,-7.191472,5.375685,9.842430,7.663894,3.410966,5.498977,4.249158,-1.668469,-3.567603,-3.658555,-0.428250,0.756300,-8.255967,3.785503,3.160402,-2.024044,8.877421,6.896743,-5.974732,5.058511,-0.731732,-3.190885,-3.745974,0.856969,-0.016209,-4.736841,-1.810901,1.729019,-4.314772,-4.978192,3.236456,3.574645,-1.034342,8.163380,2.613003,-9.865853,7.813569,1.295208,2.233668,-8.624646,-9.778540,5.989669,8.094560,9.731470,9.434094,9.204912,-2.432950,-5.656638,9.102692,3.939063,-6.529453,0.406374,-8.542827,2.875044,6.137669,5.968811,-1.417179,-8.467442,1.075344,3.834216,8.314792,6.906049,0.312738,-9.087170,3.751818,6.287818,-4.843572,-3.818699,0.248790,-6.935387,6.320094,-3.292473,-2.487153,6.867580,-7.549965,7.934068,-9.797680,7.290179,-1.328301,-9.358313,-8.135192,2.921633,-2.511611,9.858696,9.474487,-7.561369,-6.087747,7.724100,-5.471845,-7.284982,8.423786,-3.256043,6.311693,-0.095854,-0.627931,7.299291,-4.875609,2.736430,-2.404073,3.503386,-3.009988,3.081825,-8.454993,-7.476040,9.725391,-8.851180,-3.161396,-4.299236,-6.944433,7.712713,-9.928923,1.588306,0.267293,6.471640,-5.176091,4.841954,7.761595,4.191976,7.454484,-8.472959,-9.535758,-5.508932,1.620820,-0.692315,1.271938,-7.820432,8.671113,-5.027005,-8.383857,-8.593970,-7.904797,-5.492478,-9.309005,-9.665022,4.577797,6.502433,1.875566,-9.270031,-1.144394,-2.030076,-4.949583,7.196736,7.706851,-3.541749,-1.480980,-8.143731,-5.222509,-7.813869,-8.630748,9.536375,9.472862,2.860207,-0.689588,5.547510,7.312851,-2.657416,5.732137,0.474536,7.873946,-3.893623,-1.384583,8.003368,8.609368,-1.307346,-9.704647,9.713379,-1.656315,-6.630447,-9.505411,6.802655,4.818930,6.510795,-1.110156,3.389350,-6.539856,6.635811,-0.614472,-6.315090,-3.467597,4.792083,-1.295948,-2.328371,-1.854570,4.915363,-9.113477,-9.022507,-4.437028,-0.056341,-6.100385,-9.946688,-4.545636,1.253572,-9.163906,-8.832663,-7.814589,6.694991,8.265953,4.533167,-0.351141,-6.097606,-4.558943,3.254177,0.964340,5.361470,7.033887,-9.062130,9.245649,4.312590,7.299163,-1.609615,5.585759,-3.563245,9.322503,-9.733194,-6.690585,-2.902045,7.953737,9.604689,-1.397269,-7.486561,1.478589,6.248234,5.939679,-1.871343,-6.762475,-6.339623,0.638572,-1.485177,3.238541,-2.284494,-9.188288,-5.007172,-4.576854,-9.232218,-2.690552,9.301897,1.201097,-3.824894,5.394473,-7.551268,5.815871,2.819764,3.762687,4.139667,1.214818,9.756967,-8.388449,6.032763,3.495883,5.989926,4.989975,2.580463,9.289467,0.860927,2.464157,8.643469,-8.045088,5.583126,-9.886161,-5.074083,-5.369852,9.373793,1.175954,-9.743408,-3.457121,-5.720796,-8.494017,2.423063,6.972515,-9.895544,-3.294253,8.495292,-3.157714,-2.074798,4.122440,-1.605356,-7.374516,8.016253,4.698575,6.353052,9.912948,4.484741,4.314871,-7.303991,6.768373,0.620544,-4.990238,-5.500428,6.119994,2.663474,-9.655950,6.041266,-5.688756,-5.476899,-0.304694,2.785430,-2.840292,5.736514,7.665404,-4.943366,-7.444996,-6.397716,4.004345,9.130831,-4.659511,4.285714,1.463854,0.956930,0.267930,4.690029,3.192040,-1.376047,2.979128,-8.047120,9.259776,8.253917,-2.927016,-2.207652,-9.054252,0.614897,-3.846737,7.925584,9.004926,5.895862,5.554278,-3.455621,-4.249450,-8.414263,-4.880896,-4.172991,6.501716,8.482829,-7.525344], dtype = "float64")#candidate|4729|(352,)|const|float64
call_4727 = relay.TupleGetItem(func_139_call(relay.reshape(const_4728.astype('uint16'), [70, 4]), relay.reshape(const_4729.astype('float64'), [11, 4, 8]), ), 7)
call_4730 = relay.TupleGetItem(func_143_call(relay.reshape(const_4728.astype('uint16'), [70, 4]), relay.reshape(const_4729.astype('float64'), [11, 4, 8]), ), 7)
func_1292_call = mod.get_global_var('func_1292')
func_1296_call = mutated_mod.get_global_var('func_1296')
var_4734 = relay.var("var_4734", dtype = "float64", shape = (1, 36))#candidate|4734|(1, 36)|var|float64
var_4735 = relay.var("var_4735", dtype = "uint8", shape = (2925,))#candidate|4735|(2925,)|var|uint8
call_4733 = relay.TupleGetItem(func_1292_call(relay.reshape(var_4734.astype('float64'), [3, 12, 1]), relay.reshape(call_4727.astype('uint16'), [280,]), relay.reshape(var_4735.astype('uint8'), [2925,]), ), 5)
call_4736 = relay.TupleGetItem(func_1296_call(relay.reshape(var_4734.astype('float64'), [3, 12, 1]), relay.reshape(call_4727.astype('uint16'), [280,]), relay.reshape(var_4735.astype('uint8'), [2925,]), ), 5)
output = relay.Tuple([call_4704,call_4706,call_4708,call_4727,const_4728,const_4729,call_4733,var_4734,var_4735,])
output2 = relay.Tuple([call_4705,call_4707,call_4709,call_4730,const_4728,const_4729,call_4736,var_4734,var_4735,])
func_4745 = relay.Function([var_4734,var_4735,], output)
mod['func_4745'] = func_4745
mod = relay.transform.InferType()(mod)
mutated_mod['func_4745'] = func_4745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4745_call = mutated_mod.get_global_var('func_4745')
var_4747 = relay.var("var_4747", dtype = "float64", shape = (1, 36))#candidate|4747|(1, 36)|var|float64
var_4748 = relay.var("var_4748", dtype = "uint8", shape = (2925,))#candidate|4748|(2925,)|var|uint8
call_4746 = func_4745_call(var_4747,var_4748,)
output = call_4746
func_4749 = relay.Function([var_4747,var_4748,], output)
mutated_mod['func_4749'] = func_4749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2262_call = mod.get_global_var('func_2262')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_4753 = relay.TupleGetItem(func_2262_call(), 0)
call_4754 = relay.TupleGetItem(func_2264_call(), 0)
output = relay.Tuple([call_4753,])
output2 = relay.Tuple([call_4754,])
func_4755 = relay.Function([], output)
mod['func_4755'] = func_4755
mod = relay.transform.InferType()(mod)
mutated_mod['func_4755'] = func_4755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4755_call = mutated_mod.get_global_var('func_4755')
call_4756 = func_4755_call()
output = call_4756
func_4757 = relay.Function([], output)
mutated_mod['func_4757'] = func_4757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2700_call = mod.get_global_var('func_2700')
func_2701_call = mutated_mod.get_global_var('func_2701')
call_4770 = func_2700_call()
call_4771 = func_2700_call()
output = call_4770
output2 = call_4771
func_4789 = relay.Function([], output)
mod['func_4789'] = func_4789
mod = relay.transform.InferType()(mod)
mutated_mod['func_4789'] = func_4789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4789_call = mutated_mod.get_global_var('func_4789')
call_4790 = func_4789_call()
output = call_4790
func_4791 = relay.Function([], output)
mutated_mod['func_4791'] = func_4791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4789_call = mod.get_global_var('func_4789')
func_4791_call = mutated_mod.get_global_var('func_4791')
call_4871 = func_4789_call()
call_4872 = func_4789_call()
func_1409_call = mod.get_global_var('func_1409')
func_1413_call = mutated_mod.get_global_var('func_1413')
var_4891 = relay.var("var_4891", dtype = "int32", shape = (225,))#candidate|4891|(225,)|var|int32
var_4892 = relay.var("var_4892", dtype = "int32", shape = (1575,))#candidate|4892|(1575,)|var|int32
call_4890 = func_1409_call(relay.reshape(var_4891.astype('int32'), [1, 15, 15]), relay.reshape(var_4892.astype('int32'), [7, 15, 15]), )
call_4893 = func_1409_call(relay.reshape(var_4891.astype('int32'), [1, 15, 15]), relay.reshape(var_4892.astype('int32'), [7, 15, 15]), )
uop_4901 = relay.acos(var_4892.astype('float64')) # shape=(1575,)
output = relay.Tuple([call_4871,call_4890,var_4891,uop_4901,])
output2 = relay.Tuple([call_4872,call_4893,var_4891,uop_4901,])
func_4903 = relay.Function([var_4891,var_4892,], output)
mod['func_4903'] = func_4903
mod = relay.transform.InferType()(mod)
var_4904 = relay.var("var_4904", dtype = "int32", shape = (225,))#candidate|4904|(225,)|var|int32
var_4905 = relay.var("var_4905", dtype = "int32", shape = (1575,))#candidate|4905|(1575,)|var|int32
output = func_4903(var_4904,var_4905,)
func_4906 = relay.Function([var_4904,var_4905,], output)
mutated_mod['func_4906'] = func_4906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4789_call = mod.get_global_var('func_4789')
func_4791_call = mutated_mod.get_global_var('func_4791')
call_4949 = func_4789_call()
call_4950 = func_4789_call()
func_2128_call = mod.get_global_var('func_2128')
func_2133_call = mutated_mod.get_global_var('func_2133')
var_4967 = relay.var("var_4967", dtype = "float64", shape = (55, 4))#candidate|4967|(55, 4)|var|float64
const_4968 = relay.const([[2,-1,-6,-1,-10,4,-1,5,-5,10,-4,10,3,-6,1,10,-5,8,9,4,8,-1,9,7,-6,9,4,-9],[-9,-7,-5,2,10,-3,-9,6,-5,6,-2,9,2,9,7,-4,-3,5,-7,-9,-8,6,1,5,-1,-3,6,3],[2,-5,-10,-5,9,2,-8,-5,-5,-6,-6,-2,3,-10,-9,-8,-4,10,-3,6,7,-10,-1,3,-7,-2,-7,-10],[2,-1,2,10,6,10,4,-1,-4,-6,-5,2,-6,-5,-1,-7,-4,3,-10,1,-4,-5,-7,-9,-7,-7,-4,4],[-3,4,1,-4,10,10,10,-7,-2,-3,1,9,7,-2,-5,2,5,-10,9,-3,3,2,7,-8,-4,-8,-4,-6],[-5,3,-7,5,-5,10,1,5,-9,9,-6,4,9,8,-1,4,5,3,4,-1,5,3,7,1,-4,-1,-7,-4],[-9,10,7,5,5,1,7,10,-5,1,-2,-7,3,9,-3,8,5,9,4,-3,1,10,-8,-2,-3,7,5,2],[-2,-10,3,-4,-8,10,8,-2,-9,-8,3,2,-3,3,-2,8,7,-8,9,-1,-6,10,-6,6,-7,2,6,-9],[-2,-9,-7,-8,-6,-7,8,-2,10,-2,-6,-2,3,-6,8,10,-8,-4,-7,-1,9,-7,-7,1,3,-4,2,-4],[9,-5,-5,-7,-3,8,-5,4,9,1,2,-5,-7,-6,6,3,-1,-4,-3,-9,-4,-10,-8,-1,8,2,5,-7]], dtype = "uint16")#candidate|4968|(10, 28)|const|uint16
var_4969 = relay.var("var_4969", dtype = "float32", shape = (252,))#candidate|4969|(252,)|var|float32
call_4966 = relay.TupleGetItem(func_2128_call(relay.reshape(var_4967.astype('float64'), [220,]), relay.reshape(const_4968.astype('uint16'), [10, 28]), relay.reshape(call_4949.astype('float64'), []), relay.reshape(var_4969.astype('float32'), [252,]), ), 8)
call_4970 = relay.TupleGetItem(func_2133_call(relay.reshape(var_4967.astype('float64'), [220,]), relay.reshape(const_4968.astype('uint16'), [10, 28]), relay.reshape(call_4949.astype('float64'), []), relay.reshape(var_4969.astype('float32'), [252,]), ), 8)
output = relay.Tuple([call_4949,call_4966,var_4967,const_4968,var_4969,])
output2 = relay.Tuple([call_4950,call_4970,var_4967,const_4968,var_4969,])
func_4972 = relay.Function([var_4967,var_4969,], output)
mod['func_4972'] = func_4972
mod = relay.transform.InferType()(mod)
mutated_mod['func_4972'] = func_4972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4972_call = mutated_mod.get_global_var('func_4972')
var_4974 = relay.var("var_4974", dtype = "float64", shape = (55, 4))#candidate|4974|(55, 4)|var|float64
var_4975 = relay.var("var_4975", dtype = "float32", shape = (252,))#candidate|4975|(252,)|var|float32
call_4973 = func_4972_call(var_4974,var_4975,)
output = call_4973
func_4976 = relay.Function([var_4974,var_4975,], output)
mutated_mod['func_4976'] = func_4976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_5016 = relay.TupleGetItem(func_1632_call(), 0)
call_5017 = relay.TupleGetItem(func_1633_call(), 0)
output = call_5016
output2 = call_5017
func_5021 = relay.Function([], output)
mod['func_5021'] = func_5021
mod = relay.transform.InferType()(mod)
mutated_mod['func_5021'] = func_5021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5021_call = mutated_mod.get_global_var('func_5021')
call_5022 = func_5021_call()
output = call_5022
func_5023 = relay.Function([], output)
mutated_mod['func_5023'] = func_5023
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5035 = relay.const([[[5,-3,-8,7,10,1,-6,-1,10,10],[8,-9,-3,3,8,-5,3,-9,-9,-10],[-8,8,-7,-3,-10,-2,5,5,-2,1],[4,-4,6,-7,-10,1,1,1,10,-4],[7,9,9,1,4,3,9,-4,-1,-7],[-9,10,-10,5,-3,10,-7,3,5,-7],[-7,7,-8,-9,2,-9,-6,9,9,8],[5,3,7,7,-3,2,-5,-6,-2,1],[2,-4,-10,-6,9,3,4,-7,6,-4],[10,-9,-7,-9,9,-10,3,-1,9,4]],[[-5,-5,4,9,-7,9,9,4,2,-4],[3,-3,-9,9,-6,-5,9,8,-1,-3],[8,-8,9,-4,3,-3,-3,5,3,-8],[-7,9,-5,1,-2,8,8,10,6,-10],[1,7,2,-5,-6,-3,8,-2,9,-2],[-10,2,4,5,5,9,1,-1,8,7],[9,-8,3,1,-5,-2,3,3,5,9],[5,9,6,8,-6,-9,-6,3,8,9],[8,8,-5,-1,9,4,10,2,5,-1],[5,-5,8,10,3,9,3,5,8,-2]],[[-7,-1,-2,-2,-2,-6,-2,2,1,6],[-3,5,4,-6,7,-9,4,1,6,-1],[-8,-7,-9,10,1,6,-5,-2,3,3],[-5,6,6,-7,5,-1,6,3,9,9],[-1,5,-6,-5,4,10,-2,-1,6,-1],[6,1,-9,1,-8,-7,-3,-7,9,9],[1,1,6,2,-9,-10,-4,-9,7,-1],[10,6,-2,6,6,-3,3,-10,7,10],[6,3,2,3,3,6,5,9,-6,9],[10,-7,-9,1,-1,-3,2,-5,7,-4]],[[5,4,-6,5,9,4,-7,4,7,1],[-8,-5,10,3,-9,10,10,3,-8,-8],[4,8,-2,-5,-8,9,3,-4,-5,2],[7,7,5,-5,-8,-2,2,4,-2,5],[7,8,7,5,-1,7,7,7,-5,7],[-3,6,10,-1,10,4,1,9,4,-9],[9,4,1,-9,4,-10,6,-6,7,-9],[-5,-4,5,-4,7,5,-1,-3,-2,9],[-8,-5,-4,-1,10,9,4,-4,9,9],[3,-2,-5,-9,7,3,4,2,-10,-10]],[[-2,8,2,-5,9,-7,-8,-7,3,-9],[3,-10,1,6,2,4,6,-9,3,1],[8,4,-6,8,-6,-4,1,5,-3,-5],[-8,-10,-10,-3,3,-5,-2,4,2,1],[-10,-9,6,-3,7,-5,-7,-1,4,-2],[-10,7,-7,-1,-4,7,5,5,1,4],[7,5,4,3,-2,6,-3,3,5,-9],[6,3,3,7,-7,2,-10,-10,-2,6],[-7,7,5,-9,6,9,7,5,1,4],[1,-2,4,7,4,-2,-6,-2,-9,-3]],[[-1,6,6,8,1,5,-7,-5,10,6],[5,-6,7,2,-9,10,7,9,-7,-1],[6,-2,-7,-5,1,5,-1,5,-1,3],[-1,-1,1,4,-5,-8,-4,-8,-9,10],[-4,4,-7,3,-7,7,3,8,8,-2],[8,-7,-10,3,-8,9,-9,-7,-3,4],[9,10,1,-6,10,3,-9,8,5,-9],[6,5,3,2,4,-6,9,-5,-3,-9],[-10,-1,-5,8,-2,-5,7,4,3,5],[-3,-10,-6,1,5,-4,-4,-4,6,1]],[[1,8,7,7,9,-7,3,-5,4,10],[-7,6,1,-2,-2,-7,-8,-10,-1,5],[8,-4,-3,4,6,1,-10,5,-7,-8],[-10,3,-4,-3,9,-6,-3,-10,1,6],[-7,1,3,1,-10,2,-8,8,-7,8],[2,-5,-6,3,-8,-7,7,-4,-1,-4],[-6,3,-1,-3,-5,-6,-6,-1,-5,-2],[-7,-2,4,-7,-1,-9,7,-10,-4,-1],[-5,-5,-8,-1,-3,8,1,-6,-5,3],[-4,-4,4,-3,8,-9,-9,-2,-3,3]],[[-8,-7,2,4,-4,5,9,1,7,6],[-8,-6,9,7,1,-7,-1,-5,-6,10],[8,-10,-7,2,6,9,3,2,-1,4],[-7,10,5,-10,-8,3,-6,-5,-5,-8],[7,7,-1,1,-10,-8,6,-6,5,2],[-6,1,9,4,-5,6,-10,-9,6,4],[5,-4,10,-3,-7,10,1,3,9,5],[2,5,8,2,6,-9,-8,5,6,4],[-3,5,10,-6,-9,-5,4,-2,8,4],[2,6,-10,-9,-8,-8,-9,-7,-4,10]],[[-3,4,-4,10,2,5,-9,5,3,4],[1,4,-6,9,-3,-5,3,-6,8,9],[9,-8,-9,6,9,3,3,-9,8,8],[8,-10,5,-10,-1,4,6,-8,7,7],[5,5,7,6,-6,9,-8,-7,-6,-5],[-7,-6,-3,6,-10,5,2,3,5,-7],[4,5,4,6,-8,-6,9,7,-10,-1],[5,6,-3,-7,8,9,9,-5,-7,-2],[9,-9,-1,2,1,-2,7,-4,-8,-1],[4,-8,6,-7,-2,10,-6,-4,7,-10]],[[9,-5,-1,9,9,-6,1,-7,7,2],[2,3,-2,6,-2,8,-10,8,-1,1],[-6,-2,-10,6,2,9,1,-1,-6,4],[5,9,-4,-9,1,-2,6,6,4,5],[3,1,3,-8,-1,9,4,-3,3,3],[1,-5,-3,5,6,-5,-2,-2,10,-6],[-2,-9,2,-7,4,-3,9,-4,-10,10],[-8,4,3,7,-5,6,-9,-6,-7,-8],[-4,5,-10,6,7,5,-2,5,4,-1],[-6,-8,10,-10,8,-7,10,8,3,9]],[[9,-5,-10,8,-4,-2,-8,9,-6,-6],[-6,1,-4,-5,2,-7,7,-3,4,-10],[-4,1,3,-9,-9,-5,7,1,4,10],[-10,-8,1,-2,5,-5,6,-3,6,-10],[-7,9,3,-7,4,5,-6,-10,4,-2],[-6,2,-3,-1,-4,-3,9,7,2,9],[3,9,-6,-4,1,-1,-3,8,-5,4],[-3,-4,-8,4,-5,5,8,-7,5,5],[7,2,9,5,-3,7,7,8,-10,-7],[-7,5,8,-8,-3,-8,10,-2,4,-7]],[[10,2,-3,5,5,2,-6,-7,-9,7],[1,4,-7,-2,-6,5,1,3,10,-7],[2,8,6,-2,4,9,-5,5,-1,-1],[6,-3,5,-10,8,1,9,-5,7,-2],[-9,4,-3,-5,8,3,4,-10,6,6],[-7,1,8,-1,-5,6,3,7,-1,-2],[10,4,3,-3,-1,-10,-5,4,-9,6],[7,8,-4,-8,9,5,-7,-5,2,-9],[6,3,10,-3,-4,3,-3,-5,-7,-3],[5,10,-8,2,1,-4,1,-8,-7,-8]],[[-2,-6,3,5,6,-10,7,-3,-3,4],[8,-2,-7,10,1,-9,-10,-1,6,-2],[-1,3,2,-2,5,-10,-6,-2,3,1],[1,-9,4,-1,-6,-5,7,5,-6,-4],[-5,-3,-7,7,8,-7,5,7,6,4],[-3,8,-6,9,4,-4,10,-1,6,-8],[-6,-1,-1,-2,8,-10,4,-3,5,-6],[-9,-7,10,7,-7,-10,2,-4,2,1],[-4,5,2,-10,-3,-5,7,-1,-1,-4],[-3,-9,-8,7,3,-3,2,-4,-5,-1]]], dtype = "uint64")#candidate|5035|(13, 10, 10)|const|uint64
const_5036 = relay.const([[[8,-7,-1,-1,-9,-3,-8,-1,5,6],[6,-5,-6,1,-2,9,10,-1,10,10],[-10,2,9,10,7,-8,-7,6,-5,-3],[-5,-9,8,-7,-1,-8,1,-6,-3,-6],[4,1,-8,-7,3,10,-2,-4,8,-1],[-10,9,-6,4,3,10,-4,9,2,-7],[-5,5,-7,-10,-2,-3,9,-6,6,8],[1,-7,1,-9,1,9,4,-3,-5,-5],[5,3,-1,-3,-10,8,-9,6,-10,-2],[-2,7,5,4,-5,10,8,-8,-2,-8]],[[9,2,1,-7,-5,-10,-2,-1,-6,-8],[6,3,-1,5,-1,4,10,-8,-7,2],[6,1,8,6,8,9,3,-10,-4,-6],[1,-4,9,2,9,-10,-7,-2,2,10],[-3,4,10,8,10,-8,-7,1,-4,-2],[8,-5,-10,1,8,-1,-10,-7,-10,6],[-1,2,5,-4,8,-10,-7,-1,-6,10],[-6,5,8,8,-6,-2,9,7,-7,2],[4,-2,-9,-9,-7,-8,-1,-9,-2,-9],[-1,7,4,3,4,9,-9,10,-5,-4]],[[-7,-7,5,7,5,8,-8,-6,-1,-6],[-6,5,-5,3,2,-6,10,-7,-1,2],[2,-4,7,5,-10,-4,-5,2,-4,3],[4,6,5,9,-10,4,3,2,-1,-1],[-7,9,-4,1,-8,5,-4,-6,-6,6],[7,8,9,1,7,1,5,-6,-1,-8],[-3,-2,5,5,2,5,-3,-9,-3,4],[-10,-1,-5,7,-6,-6,9,-6,-6,4],[-4,9,-2,-2,1,-2,-1,10,-4,3],[-4,-6,8,7,-3,-4,-10,6,1,8]],[[4,-5,-4,2,-1,-7,5,-6,-5,7],[-6,7,-3,-9,-1,-8,-6,1,-5,-10],[-9,1,-2,6,-2,9,5,-3,1,3],[-8,8,-4,-7,-1,7,-6,3,-5,-5],[-4,-4,-2,-7,10,4,3,-5,-10,-5],[-9,-10,-1,1,4,5,-4,-8,8,7],[7,10,-5,4,5,-8,-4,-9,3,-10],[-10,4,-6,8,8,-3,-1,3,-6,-3],[8,7,-2,-6,-10,2,1,-2,8,10],[9,1,4,6,-2,-5,2,2,-10,-9]],[[-5,10,8,-3,-4,-2,-6,-1,-8,-4],[-7,1,-3,-3,1,5,4,-4,-7,-9],[-1,4,-6,10,3,6,-3,7,-10,-8],[4,-9,-7,1,1,7,-2,9,-5,6],[5,7,-9,-3,-7,-1,4,-1,4,-7],[3,7,4,-7,-9,8,-5,1,9,2],[-4,-9,5,-1,4,-4,-3,-4,8,-7],[-4,-10,-8,-2,4,-5,7,9,7,-10],[10,-8,4,-2,-5,9,4,10,-2,-2],[-6,-7,2,6,-7,-10,10,-2,2,-7]],[[6,10,-9,3,3,-6,-4,-6,8,-8],[8,-2,8,3,1,-8,-9,-7,9,8],[5,2,8,6,10,10,1,-6,-9,8],[-2,5,5,10,1,-7,-3,-8,7,-6],[9,6,-2,-9,-3,9,5,7,-7,5],[4,-8,1,7,-9,6,10,8,-4,3],[5,-5,7,10,8,5,7,8,-7,-5],[-9,-4,1,-1,8,6,-5,2,2,9],[1,-1,-7,-6,3,1,-2,-1,7,-2],[5,8,9,-3,6,-1,5,-5,3,7]],[[5,-8,-4,-4,2,-6,3,6,-6,3],[2,-6,7,1,5,4,5,8,2,10],[5,-10,10,10,-6,5,-8,6,4,-3],[-5,-8,-2,10,6,7,-6,2,2,3],[5,-7,10,-8,1,5,10,-6,10,6],[8,9,-2,-1,1,4,3,-10,-5,9],[-2,1,8,4,-5,-5,-8,6,-3,4],[-2,-3,10,-8,-4,10,-3,-7,10,10],[6,8,-10,-3,1,9,6,8,7,-10],[5,4,10,-3,-3,-6,10,2,-8,5]],[[10,3,-7,-1,-9,5,10,-3,1,3],[-1,-4,2,-3,8,-10,-5,8,5,8],[2,-7,-3,3,8,-7,-6,10,-6,10],[2,-6,-4,10,-4,3,-10,-8,-1,-6],[-8,8,3,-2,2,4,-2,2,3,-7],[-10,2,-1,2,3,10,10,-5,-5,-3],[1,-2,6,-2,6,7,-10,-6,1,-10],[8,8,-8,-3,2,-10,3,-7,-6,9],[8,9,-9,6,5,-6,8,2,-7,-8],[1,3,10,3,8,-9,10,-2,-3,8]],[[-8,2,8,-3,9,5,9,-1,5,6],[-6,10,3,2,4,-5,-6,-8,2,-9],[-3,8,10,3,-3,-3,-6,-4,6,-6],[-8,5,-9,-8,6,-10,2,3,9,-1],[6,1,6,-2,1,-5,8,-3,-2,-8],[8,7,7,-6,-7,7,9,-7,3,-9],[7,3,3,4,7,-6,-9,-7,-5,1],[7,7,-7,-3,6,-3,4,-10,-2,-4],[6,3,5,4,-10,1,-4,-5,5,-9],[8,5,8,10,-10,8,-6,-3,-9,-2]],[[1,-8,4,-4,-1,-1,7,-2,-9,-6],[9,-5,4,-8,5,2,3,-9,-5,-7],[9,5,2,-2,2,-2,-1,7,-6,-8],[7,5,2,-9,10,-3,-2,5,-10,6],[5,2,-4,-1,8,-1,1,-4,-3,-2],[-9,-2,-7,-6,3,6,10,4,-1,-6],[8,1,-7,-2,8,-5,-1,7,-3,-3],[-6,4,1,2,7,-8,-7,-2,-3,-7],[2,-7,7,1,8,-6,-4,-10,10,-4],[2,-2,10,5,10,-6,4,-5,1,2]],[[-9,4,1,-8,-8,10,8,-10,7,4],[9,-10,-5,-5,1,6,8,-5,5,-1],[-10,4,-2,8,4,-7,-2,-8,-5,3],[-10,8,-8,6,10,8,-8,-10,1,-2],[-8,9,-9,8,10,10,10,-8,2,-4],[1,4,8,-4,10,5,-6,-1,-3,-6],[10,-3,-3,1,-6,8,8,-9,-6,7],[-8,7,9,6,6,-3,8,-9,10,6],[4,3,6,10,4,9,2,-5,-3,-10],[-5,-7,2,3,5,-8,-5,-3,-3,-4]],[[-4,1,10,-6,-9,4,-3,6,-9,7],[-10,5,6,-6,-4,-7,3,4,-6,-8],[9,8,7,9,-2,-9,1,-8,5,7],[-2,8,4,1,-4,-2,1,5,3,3],[2,8,8,-2,9,2,6,7,4,8],[4,-9,2,-4,-1,10,1,-7,-5,-3],[10,4,-7,-8,8,9,7,-1,-3,2],[4,-5,2,-7,5,-1,-9,-3,-7,-9],[6,-1,5,2,8,2,-9,-10,-1,8],[-9,10,-6,-4,3,-10,-1,-4,4,2]],[[3,6,3,3,-3,9,-3,-9,2,-4],[9,6,6,6,-9,1,-4,-3,1,10],[-8,5,6,10,9,4,7,-8,1,2],[4,-1,-8,-5,10,-4,-2,10,5,7],[2,-2,1,-4,3,2,9,6,-8,8],[-4,-6,3,4,4,2,5,6,3,10],[-4,-3,-8,10,-10,1,3,10,-1,-6],[10,-2,-1,10,-6,1,-3,-3,-3,-6],[-3,9,-6,4,7,-4,-9,1,3,-5],[2,-9,10,7,-4,10,-1,3,-10,-5]]], dtype = "uint64")#candidate|5036|(13, 10, 10)|const|uint64
bop_5037 = relay.bitwise_or(const_5035.astype('uint64'), relay.reshape(const_5036.astype('uint64'), relay.shape_of(const_5035))) # shape=(13, 10, 10)
func_3749_call = mod.get_global_var('func_3749')
func_3752_call = mutated_mod.get_global_var('func_3752')
var_5045 = relay.var("var_5045", dtype = "uint16", shape = (130, 4))#candidate|5045|(130, 4)|var|uint16
call_5044 = relay.TupleGetItem(func_3749_call(relay.reshape(var_5045.astype('uint16'), [520,])), 1)
call_5046 = relay.TupleGetItem(func_3752_call(relay.reshape(var_5045.astype('uint16'), [520,])), 1)
output = relay.Tuple([bop_5037,call_5044,var_5045,])
output2 = relay.Tuple([bop_5037,call_5046,var_5045,])
func_5055 = relay.Function([var_5045,], output)
mod['func_5055'] = func_5055
mod = relay.transform.InferType()(mod)
var_5056 = relay.var("var_5056", dtype = "uint16", shape = (130, 4))#candidate|5056|(130, 4)|var|uint16
output = func_5055(var_5056)
func_5057 = relay.Function([var_5056], output)
mutated_mod['func_5057'] = func_5057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3691_call = mod.get_global_var('func_3691')
func_3693_call = mutated_mod.get_global_var('func_3693')
call_5119 = relay.TupleGetItem(func_3691_call(), 0)
call_5120 = relay.TupleGetItem(func_3693_call(), 0)
func_4972_call = mod.get_global_var('func_4972')
func_4976_call = mutated_mod.get_global_var('func_4976')
var_5130 = relay.var("var_5130", dtype = "float64", shape = (220,))#candidate|5130|(220,)|var|float64
const_5131 = relay.const([[-5.457997,1.253729,8.787922,-3.391222,-5.361385,9.357026,-5.170812,6.843666,4.049623,2.854289,3.755345,-7.090801,7.154531,-8.343375,-0.606266,-5.591793,-1.839533,-5.319707,-9.669452,-5.181851,-5.753220,-5.424853,1.360095,2.598207,3.808860,-5.526202,-1.206475,-0.252787,4.289273,-7.482816,-3.349708,-8.134818,-2.513406,-8.015011,-1.396373,0.113031,4.539243,8.290624,3.177253,6.221184,1.507690,5.655272,-7.997421,-8.131648,-8.182614,9.568172,4.620600,8.082589,9.417016,-9.887782,-6.365925,-3.399554,-4.643044,-9.356424,2.458414,-7.049313,-4.362333,-4.274302,1.625947,-4.443841,4.357371,-8.208620,3.952300,-3.913039,-8.674849,-5.001381,-9.040282,-5.613601,-1.207552,-8.867768,-0.275299,5.556994,-4.883976,5.408901,-5.227255,2.618289,-7.508444,-3.250717,5.107822,-9.356338,-1.706280,-0.646121,0.906548,4.368614,-9.201057,2.163819,-1.600333,8.455748,3.783553,-3.807306,-0.218590,0.520179,8.670410,-0.728257,2.814001,-5.106044,-3.942558,-4.582255,4.295352,7.637144,-5.949624,-2.981189,3.681729,0.967068,6.470188,-7.152563,-9.872270,-2.095750,-5.040362,-2.389856,4.350428,3.123758,-1.364980,2.809190,9.209209,2.536326,-5.295499,-8.067383,9.608187,-9.747407,8.233362,-7.603652,-9.144023,5.062902,2.339810,-7.103955,2.799879,-6.155304,-0.996020,0.465979,2.248560,1.389049,5.297078,1.615416,1.844367,6.496718,9.354846,-3.826691,-3.170196,-4.716389,-5.955924,-1.291973,-9.535239,9.909748,-2.467343,-0.720532,7.791292,6.589777,5.495636,2.214386,-3.655473,6.234439,-1.104329,-7.482864,4.997924,-1.479199,5.638206,2.962479,-1.527822,-8.232270,-7.085368,-0.724844,-1.381051,-2.933161,-6.421587,5.003891,-0.853232,-6.508424,-1.828868,1.403127,6.029608,4.085723,-8.928512,-4.572588,9.436129,7.832569,1.229826,8.099861,-9.652396,4.865756,5.342752,7.107120,3.134434,-8.607763,-6.968191,-0.785690,-0.182973,4.673779,-7.040130,0.786098,-6.600383,0.490373,-4.094279,-5.579409,-5.757738,0.853098,-7.318818,0.166483,5.383757,9.022349,2.891171,1.548813,-5.498603,-8.288728,9.680470,-6.640966,7.439240,8.418038,7.789805,-4.008409,-7.457758,4.337705,-3.300350,-9.250112,0.744241,-6.847524,2.008040,-0.236354,-8.148020,1.975662,-2.468993,2.724357,1.429425,6.966327,-0.134622,6.741873,2.272013,3.078337,1.465373,8.849570,-8.117458,-6.535153,-2.088335,9.895704,2.812233,-7.358021,-1.021388,7.972291,-7.056333,-9.953699,-4.858423,8.178731,3.556074,-6.827106,7.697799,9.920216,2.040315,5.727207,-8.857721,-4.465680,4.594678,8.503291]], dtype = "float32")#candidate|5131|(1, 252)|const|float32
call_5129 = relay.TupleGetItem(func_4972_call(relay.reshape(var_5130.astype('float64'), [55, 4]), relay.reshape(const_5131.astype('float32'), [252,]), ), 3)
call_5132 = relay.TupleGetItem(func_4976_call(relay.reshape(var_5130.astype('float64'), [55, 4]), relay.reshape(const_5131.astype('float32'), [252,]), ), 3)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_5134 = relay.TupleGetItem(func_3316_call(relay.reshape(call_5119.astype('float32'), [11, 4, 7])), 0)
call_5135 = relay.TupleGetItem(func_3318_call(relay.reshape(call_5119.astype('float32'), [11, 4, 7])), 0)
output = relay.Tuple([call_5119,call_5129,var_5130,const_5131,call_5134,])
output2 = relay.Tuple([call_5120,call_5132,var_5130,const_5131,call_5135,])
func_5139 = relay.Function([var_5130,], output)
mod['func_5139'] = func_5139
mod = relay.transform.InferType()(mod)
var_5140 = relay.var("var_5140", dtype = "float64", shape = (220,))#candidate|5140|(220,)|var|float64
output = func_5139(var_5140)
func_5141 = relay.Function([var_5140], output)
mutated_mod['func_5141'] = func_5141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
call_5149 = func_2745_call()
call_5150 = func_2745_call()
func_2840_call = mod.get_global_var('func_2840')
func_2845_call = mutated_mod.get_global_var('func_2845')
var_5175 = relay.var("var_5175", dtype = "float32", shape = (308,))#candidate|5175|(308,)|var|float32
const_5176 = relay.const([4,10,2,-5,-4,-10,-2,-6,4,10,3,-3,4,-3,4,6,3,-4,-4,5,5,-9,-8,4,6,-1,5,8,-3,-2,1,6,5,-3,8,5,5,-10,10,-4,-9,-5,-8,-4,4,-9,5,10,-5,7,9,7,-7,-7,-1,3,-6,4,3,-7,3,1,1,-8,-4,-10,-6,-7,3,9,-4,6,3,6,-8,-3,10,1,-7,10,3,-4,-8,-3,4,-7,-4,-10,2,5,8,-3,3,-10,4,-2,1,-7,7,-9,1,1,6,-4,-7,8,-6,4,6,10,5,8,-9,4,-4,9,9,-5,-3,-5,8,6,8,-5,-3,6,-8,5,-9,5,3,1,8,-9,4,9,-1,8,-4,-6,8,6,-4,5,-9,-9,6,6,-5,-3,1,3,-9,-3,-3,-10,9,-9,7,8,-6,-10,-8,-6,-1,6,-5,6,-9,4,8,-5,2,-1,9,6,-8,-10,3,3,-9,8,5,5,-4,10,-5,-10,10,-5,-3,-6,7,1,-4,-6,1,-6,-1,-4,9,9,-8,10,-10,-9,-6,-6,-3,-5,-1,-1,-8,-1,-7,3,9,-10,1,-5,5,-6,10,-3,10,1,10,4,-10,-6,1,3,-1,7,4,-5,-7,-9,-2,10,-2,-3,-7,-2,-3,-4,-10,-4,-9,-5,2,-2,-10,6,3,3,-10,-8,7,-4,10,5,-4,-1,2,5,-5,-5,-8,-6,-8,6,9,-5,-8,7,6,8,-2,4], dtype = "uint16")#candidate|5176|(280,)|const|uint16
var_5177 = relay.var("var_5177", dtype = "int64", shape = (1183,))#candidate|5177|(1183,)|var|int64
call_5174 = relay.TupleGetItem(func_2840_call(relay.reshape(var_5175.astype('float32'), [11, 4, 7]), relay.reshape(const_5176.astype('uint16'), [280,]), relay.reshape(var_5177.astype('int64'), [1183,]), ), 3)
call_5178 = relay.TupleGetItem(func_2845_call(relay.reshape(var_5175.astype('float32'), [11, 4, 7]), relay.reshape(const_5176.astype('uint16'), [280,]), relay.reshape(var_5177.astype('int64'), [1183,]), ), 3)
var_5183 = relay.var("var_5183", dtype = "int64", shape = (1183,))#candidate|5183|(1183,)|var|int64
bop_5184 = relay.greater(var_5177.astype('bool'), relay.reshape(var_5183.astype('bool'), relay.shape_of(var_5177))) # shape=(1183,)
output = relay.Tuple([call_5149,call_5174,var_5175,const_5176,bop_5184,])
output2 = relay.Tuple([call_5150,call_5178,var_5175,const_5176,bop_5184,])
F = relay.Function([var_5175,var_5177,var_5183,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5175,var_5177,var_5183,], output2)
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
