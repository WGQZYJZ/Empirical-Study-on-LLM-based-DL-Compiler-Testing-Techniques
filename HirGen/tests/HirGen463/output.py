import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_2 = relay.var("var_2", dtype = "int8", shape = (7, 4, 1))#candidate|2|(7, 4, 1)|var|int8
var_3 = relay.var("var_3", dtype = "int8", shape = (7, 4, 16))#candidate|3|(7, 4, 16)|var|int8
bop_4 = relay.add(var_2.astype('int8'), var_3.astype('int8')) # shape=(7, 4, 16)
bop_12 = relay.floor_divide(var_3.astype('float32'), var_2.astype('float32')) # shape=(7, 4, 16)
output = relay.Tuple([bop_4,bop_12,])
output2 = relay.Tuple([bop_4,bop_12,])
func_19 = relay.Function([var_2,var_3,], output)
mod['func_19'] = func_19
mod = relay.transform.InferType()(mod)
var_20 = relay.var("var_20", dtype = "int8", shape = (7, 4, 1))#candidate|20|(7, 4, 1)|var|int8
var_21 = relay.var("var_21", dtype = "int8", shape = (7, 4, 16))#candidate|21|(7, 4, 16)|var|int8
output = func_19(var_20,var_21,)
func_22 = relay.Function([var_20,var_21,], output)
mutated_mod['func_22'] = func_22
mutated_mod = relay.transform.InferType()(mutated_mod)
var_77 = relay.var("var_77", dtype = "float64", shape = (4, 2, 3))#candidate|77|(4, 2, 3)|var|float64
uop_78 = relay.acos(var_77.astype('float64')) # shape=(4, 2, 3)
func_19_call = mod.get_global_var('func_19')
func_22_call = mutated_mod.get_global_var('func_22')
var_94 = relay.var("var_94", dtype = "int8", shape = (28,))#candidate|94|(28,)|var|int8
var_95 = relay.var("var_95", dtype = "int8", shape = (448,))#candidate|95|(448,)|var|int8
call_93 = relay.TupleGetItem(func_19_call(relay.reshape(var_94.astype('int8'), [7, 4, 1]), relay.reshape(var_95.astype('int8'), [7, 4, 16]), ), 0)
call_96 = relay.TupleGetItem(func_22_call(relay.reshape(var_94.astype('int8'), [7, 4, 1]), relay.reshape(var_95.astype('int8'), [7, 4, 16]), ), 0)
const_119 = relay.const([[[-5.513474,-1.710040,5.374652],[9.019595,-2.590745,0.866540]],[[2.940217,-9.405411,8.988371],[8.033585,-8.091405,-1.322586]],[[5.191435,3.647191,-2.214549],[-8.108460,8.882422,-2.229369]],[[3.992095,6.505508,-3.874039],[-3.087895,-3.152724,0.631342]]], dtype = "float64")#candidate|119|(4, 2, 3)|const|float64
bop_120 = relay.multiply(var_77.astype('uint32'), relay.reshape(const_119.astype('uint32'), relay.shape_of(var_77))) # shape=(4, 2, 3)
func_19_call = mod.get_global_var('func_19')
func_22_call = mutated_mod.get_global_var('func_22')
call_135 = relay.TupleGetItem(func_19_call(relay.reshape(var_94.astype('int8'), [7, 4, 1]), relay.reshape(var_95.astype('int8'), [7, 4, 16]), ), 0)
call_136 = relay.TupleGetItem(func_22_call(relay.reshape(var_94.astype('int8'), [7, 4, 1]), relay.reshape(var_95.astype('int8'), [7, 4, 16]), ), 0)
uop_151 = relay.atanh(call_93.astype('float32')) # shape=(7, 4, 16)
uop_153 = relay.atanh(call_96.astype('float32')) # shape=(7, 4, 16)
output = relay.Tuple([uop_78,var_94,var_95,bop_120,call_135,uop_151,])
output2 = relay.Tuple([uop_78,var_94,var_95,bop_120,call_136,uop_153,])
func_159 = relay.Function([var_77,var_94,var_95,], output)
mod['func_159'] = func_159
mod = relay.transform.InferType()(mod)
mutated_mod['func_159'] = func_159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_159_call = mutated_mod.get_global_var('func_159')
var_161 = relay.var("var_161", dtype = "float64", shape = (4, 2, 3))#candidate|161|(4, 2, 3)|var|float64
var_162 = relay.var("var_162", dtype = "int8", shape = (28,))#candidate|162|(28,)|var|int8
var_163 = relay.var("var_163", dtype = "int8", shape = (448,))#candidate|163|(448,)|var|int8
call_160 = func_159_call(var_161,var_162,var_163,)
output = call_160
func_164 = relay.Function([var_161,var_162,var_163,], output)
mutated_mod['func_164'] = func_164
mutated_mod = relay.transform.InferType()(mutated_mod)
const_185 = relay.const([[[-9.031814,9.549136,7.919937,-4.663404,-8.024450,3.219109],[8.771417,-9.382124,-3.913556,6.316166,-4.287254,-5.189560],[-1.946957,-8.818879,6.792121,7.891728,2.909500,-1.856897],[-7.912693,-5.810370,-6.416625,-6.641081,7.021022,-6.706220]],[[8.230417,-3.951671,8.176671,-4.130052,0.777423,-3.279867],[2.624308,9.258592,8.912323,9.051435,-0.514451,-5.699911],[3.450220,-0.327845,5.666418,-3.197455,4.575810,4.928433],[8.763308,-1.425470,-9.433191,-1.269719,-3.144180,-4.791380]],[[3.171279,-5.106381,-9.268362,-7.031500,0.106036,-1.302859],[0.409953,1.857296,3.952982,7.557157,8.891885,2.679728],[5.208187,5.073311,6.482835,8.804709,1.739088,8.201686],[-4.902346,9.130038,-7.273698,7.131548,-1.676810,-9.145644]],[[7.125381,-6.723025,-7.850268,-4.116358,7.230657,8.119487],[-4.703665,9.643492,-0.810865,8.040984,4.104904,-8.649547],[-9.534079,2.607388,9.192157,-4.020882,-1.407477,0.913161],[-3.895077,-9.677034,4.900619,4.682420,-9.103914,6.763239]],[[1.426263,5.228050,4.259924,-0.990866,6.098865,-9.014262],[-8.617705,7.112893,7.305485,5.063330,9.869134,-9.676216],[4.761477,-3.394422,-0.561862,5.706816,-6.394093,-5.324466],[-5.675451,7.046918,2.110703,-2.689480,-3.565193,-1.184338]],[[-0.001164,7.845655,5.709011,-9.079054,6.250063,-8.484902],[-4.876704,9.470994,-7.426798,-5.737861,6.662870,6.434672],[3.045800,-5.059115,8.904698,-1.681206,-4.743600,0.840107],[1.568068,-7.462551,-1.659954,-6.123515,-2.905688,8.977095]],[[-3.696502,-1.785723,2.362885,-8.553315,1.848679,-6.412420],[5.960756,1.316613,3.836530,7.265277,-8.248953,6.475231],[-4.431871,-3.650644,-3.875322,8.903968,2.028273,-1.491673],[1.723528,-2.874562,6.156125,-1.682757,6.878023,-1.615951]],[[-9.712317,4.320569,3.494195,-3.139236,-3.512402,2.126659],[-3.405984,9.639879,-6.222300,4.454693,-5.623545,-7.265879],[-2.933127,-7.879829,-5.515168,-5.942080,-4.585390,-0.976369],[6.113571,1.457315,4.512555,-6.551670,-8.124306,9.352971]],[[7.931444,-9.746232,-6.425540,1.234796,3.201313,-9.550677],[-0.165221,8.536724,-7.428735,-5.020924,-9.130252,-0.168980],[-2.436161,1.507156,-2.347374,0.633185,6.619057,-5.216766],[4.642015,0.924101,4.824923,-8.242460,-3.572329,2.683260]],[[7.712950,-6.291515,0.451823,2.897545,6.472004,-8.699976],[-7.814338,9.879761,-1.259625,7.566756,0.474520,-1.583649],[1.487349,-1.258109,-3.077368,-5.892793,-2.384076,3.121774],[2.905221,0.951255,-2.374495,5.361402,-4.903002,-3.506115]],[[-1.292722,-7.966406,-2.802895,-1.455980,3.673442,-2.218048],[-6.115675,-8.230531,1.130300,9.753852,-3.612634,-6.653635],[-5.448743,0.298786,-3.183170,0.397034,-1.815842,5.250817],[7.703761,-4.039020,-7.273438,-7.637648,9.725433,6.804324]],[[6.400675,-8.995427,-1.691985,-9.368449,-7.674642,4.433838],[7.331365,5.340270,-5.362315,7.958538,-6.325908,-7.513148],[-7.466590,-1.800996,5.406093,-2.039113,-9.254235,9.441809],[3.358001,5.598611,5.330414,4.708254,-3.883049,-3.769017]]], dtype = "float32")#candidate|185|(12, 4, 6)|const|float32
uop_186 = relay.acos(const_185.astype('float32')) # shape=(12, 4, 6)
bop_195 = relay.mod(uop_186.astype('float64'), relay.reshape(const_185.astype('float64'), relay.shape_of(uop_186))) # shape=(12, 4, 6)
func_159_call = mod.get_global_var('func_159')
func_164_call = mutated_mod.get_global_var('func_164')
var_204 = relay.var("var_204", dtype = "float64", shape = (24,))#candidate|204|(24,)|var|float64
var_205 = relay.var("var_205", dtype = "int8", shape = (28,))#candidate|205|(28,)|var|int8
const_206 = relay.const([2,6,-7,7,8,-4,-2,-2,3,-9,7,-8,-6,7,1,-1,-9,1,6,5,9,3,-6,4,10,6,-7,-10,-3,6,4,1,6,3,-9,6,-10,9,1,3,5,7,-6,-7,-4,4,-2,-5,-6,-2,9,-3,4,2,5,7,7,-6,-4,1,-7,8,-2,10,3,5,8,8,-1,-9,8,-6,3,7,4,5,-6,3,-8,-6,-2,3,-8,-4,-3,-3,9,7,3,7,-5,9,5,-7,-4,6,-5,-8,3,-2,-2,-9,-6,3,2,9,2,7,1,-2,9,10,8,7,-9,8,-3,4,-3,1,9,-3,9,2,-3,2,4,-6,-2,-4,9,4,-10,3,7,1,5,1,-1,1,-9,6,9,-6,2,-1,5,-4,8,-8,-3,-3,10,-10,8,5,-6,-1,-2,5,-8,-8,6,7,9,-8,-4,-1,-6,-7,2,-2,-4,5,-1,-1,-9,-3,1,8,5,4,-9,-8,-4,1,-7,-8,5,7,4,-4,-9,7,-7,1,10,-5,-10,4,-6,-2,8,-5,3,-9,-2,-9,10,-2,-2,-10,10,-1,-6,4,2,8,8,-4,-7,-8,-6,1,-5,-4,8,1,-9,8,-1,-1,8,2,-5,7,-9,-3,3,2,9,-9,4,-6,-4,10,7,-8,-3,3,7,1,8,-3,-8,-1,5,-5,-9,1,5,9,-7,9,7,9,3,-2,-2,1,3,6,-3,-6,1,-8,-1,8,-5,-7,10,-8,5,-5,-6,6,10,9,2,10,3,10,6,-9,7,-3,1,2,-1,3,-5,9,3,-1,-3,6,10,7,4,-4,3,9,-9,2,-10,-9,7,2,-6,-3,-5,-5,5,-8,-10,-1,2,-1,-3,-8,9,9,5,-4,-6,2,-7,6,-10,2,-7,-5,5,9,-8,-4,-6,4,6,-4,6,4,4,-7,4,-4,-2,-1,4,6,7,-10,-3,-6,-4,-3,-8,-8,-7,-5,-2,-4,-8,5,3,4,3,6,-10,-7,3,-9,-7,3,1,4,7,-10,-3,6,8,7,-6,9,5,4,-6,-1,9,-8,2,-4,2,-5,-10,-10,-1,-10,-1,-4,-5,-6,-1,-3,-9,-1,-4,1,10,8,6,-10,6,5,9,4,8,-4,-5,9,9,-6,-6,7,-2,8,3,-5,8,-6,9,-8,10,-4,-10,-8,5,-9], dtype = "int8")#candidate|206|(448,)|const|int8
call_203 = relay.TupleGetItem(func_159_call(relay.reshape(var_204.astype('float64'), [4, 2, 3]), relay.reshape(var_205.astype('int8'), [28,]), relay.reshape(const_206.astype('int8'), [448,]), ), 4)
call_207 = relay.TupleGetItem(func_164_call(relay.reshape(var_204.astype('float64'), [4, 2, 3]), relay.reshape(var_205.astype('int8'), [28,]), relay.reshape(const_206.astype('int8'), [448,]), ), 4)
uop_208 = relay.log2(uop_186.astype('float64')) # shape=(12, 4, 6)
func_159_call = mod.get_global_var('func_159')
func_164_call = mutated_mod.get_global_var('func_164')
call_213 = relay.TupleGetItem(func_159_call(relay.reshape(var_204.astype('float64'), [4, 2, 3]), relay.reshape(var_205.astype('int8'), [28,]), relay.reshape(const_206.astype('int8'), [448,]), ), 4)
call_214 = relay.TupleGetItem(func_164_call(relay.reshape(var_204.astype('float64'), [4, 2, 3]), relay.reshape(var_205.astype('int8'), [28,]), relay.reshape(const_206.astype('int8'), [448,]), ), 4)
output = relay.Tuple([bop_195,call_203,var_204,var_205,const_206,uop_208,call_213,])
output2 = relay.Tuple([bop_195,call_207,var_204,var_205,const_206,uop_208,call_214,])
func_233 = relay.Function([var_204,var_205,], output)
mod['func_233'] = func_233
mod = relay.transform.InferType()(mod)
var_234 = relay.var("var_234", dtype = "float64", shape = (24,))#candidate|234|(24,)|var|float64
var_235 = relay.var("var_235", dtype = "int8", shape = (28,))#candidate|235|(28,)|var|int8
output = func_233(var_234,var_235,)
func_236 = relay.Function([var_234,var_235,], output)
mutated_mod['func_236'] = func_236
mutated_mod = relay.transform.InferType()(mutated_mod)
const_967 = relay.const([[[8.526173,6.781188,6.166124,8.362026],[0.519239,6.936110,-1.477752,3.463096],[-4.728695,-7.467758,7.122379,-6.870285],[-9.851278,-7.794583,-9.635139,0.360875],[7.940322,7.502456,-9.439226,-4.050417],[-9.431829,7.768344,-6.890911,9.493644],[9.391734,2.482676,2.648729,-6.152794],[3.686260,-2.434592,-4.407118,-3.075438],[-8.373941,-2.406205,-4.981062,-8.332146]],[[9.246270,7.361852,0.050287,-9.833057],[-3.801205,9.463775,8.431340,3.879698],[-8.728202,-6.622992,0.633323,-6.506447],[0.541794,-7.646795,7.598379,-4.180303],[3.075511,-9.896914,6.706303,3.297298],[1.689180,0.856152,-9.340111,6.095200],[-3.507988,5.831416,-1.860199,8.802433],[-0.430177,-9.827122,2.947030,-2.434997],[-4.223477,4.704764,-3.870533,-9.219484]]], dtype = "float32")#candidate|967|(2, 9, 4)|const|float32
uop_968 = relay.cos(const_967.astype('float32')) # shape=(2, 9, 4)
output = relay.Tuple([uop_968,])
output2 = relay.Tuple([uop_968,])
func_975 = relay.Function([], output)
mod['func_975'] = func_975
mod = relay.transform.InferType()(mod)
output = func_975()
func_976 = relay.Function([], output)
mutated_mod['func_976'] = func_976
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1021 = relay.const(-6, dtype = "int32")#candidate|1021|()|const|int32
var_1022 = relay.var("var_1022", dtype = "int32", shape = (14, 12, 5))#candidate|1022|(14, 12, 5)|var|int32
bop_1023 = relay.greater_equal(const_1021.astype('bool'), var_1022.astype('bool')) # shape=(14, 12, 5)
func_19_call = mod.get_global_var('func_19')
func_22_call = mutated_mod.get_global_var('func_22')
var_1030 = relay.var("var_1030", dtype = "int8", shape = (7, 4))#candidate|1030|(7, 4)|var|int8
var_1031 = relay.var("var_1031", dtype = "int8", shape = (56, 8))#candidate|1031|(56, 8)|var|int8
call_1029 = relay.TupleGetItem(func_19_call(relay.reshape(var_1030.astype('int8'), [7, 4, 1]), relay.reshape(var_1031.astype('int8'), [7, 4, 16]), ), 1)
call_1032 = relay.TupleGetItem(func_22_call(relay.reshape(var_1030.astype('int8'), [7, 4, 1]), relay.reshape(var_1031.astype('int8'), [7, 4, 16]), ), 1)
const_1046 = relay.const([[[-6.028428,3.488022,8.717155,-3.064050,-6.212728,-8.763318,-2.020773,6.984549,9.289053,7.326888,-3.060964,-9.049535,-8.745231,-7.795022,-1.122516,9.658639],[7.449569,-9.983407,-7.798470,-5.006779,2.571362,-0.765643,2.401894,-5.870132,6.003260,-3.350699,2.497657,-6.724062,-2.807124,-8.387216,-5.883227,7.679370],[-8.467845,5.371370,-4.788488,-9.465957,-5.014727,7.050658,-7.660234,-7.629659,8.645597,7.064304,-4.473804,-2.547919,-7.527976,8.572659,-0.627064,8.228964],[-0.527601,9.571731,-9.433279,-4.488448,-0.413309,-9.129017,1.266607,1.954948,-7.416381,-9.546747,-4.026226,0.386153,5.698242,3.891305,7.941519,8.874465]],[[1.542832,-9.197430,-5.366396,4.996179,-0.425159,5.614599,-1.145396,-2.792426,2.705434,1.560882,8.130685,-2.549083,4.334041,-0.037316,-6.081560,8.987925],[9.940197,3.849826,-4.791375,-3.096353,0.606584,2.442217,-3.863952,-9.105619,-9.962549,9.541267,-5.920986,-8.353871,-4.241289,-3.926340,-1.183110,-2.553446],[4.326154,2.307658,-9.526016,-2.089145,4.339704,-0.686917,4.561399,3.562718,-8.936964,7.778772,5.776210,2.559780,-6.396358,-7.207828,8.130404,-6.865027],[5.606886,-4.092576,-2.124728,0.408922,-7.023663,6.689247,-8.693499,6.830768,-4.820237,5.378790,1.773227,1.645411,-8.143976,-7.533925,-2.391283,-0.855380]],[[7.202250,-6.676847,0.578595,9.852583,1.095600,5.022535,-9.047249,-2.034804,5.506473,-1.223715,-9.196019,-3.561058,0.109055,-4.905083,-8.117741,2.283608],[-1.523069,6.824276,0.156750,8.602918,7.857533,-3.316876,-8.632605,-5.695095,-4.090957,-4.164160,-1.043492,2.175319,0.901786,-1.398732,-1.508613,1.198531],[3.724332,-0.520521,-3.005403,2.383164,-1.043345,6.510291,-2.282643,-0.270094,-3.315805,-5.577203,-8.715645,-2.133947,3.244279,4.879121,1.221401,-6.175654],[7.963709,1.966643,3.147666,4.703445,6.830338,-7.949789,8.033683,-6.385340,2.349750,-4.947360,7.807311,4.955223,0.419532,-5.567531,-3.378700,6.580667]],[[-1.815750,1.803229,1.277622,7.323870,8.407288,4.458477,0.793167,-0.480473,-6.144055,-5.128551,7.890554,-4.033983,-1.634272,4.077610,-5.228313,-1.829023],[-8.157079,-7.036462,-6.846655,-0.298762,1.615517,-0.322567,6.106737,3.336773,-5.456166,3.085682,1.491985,-8.645507,4.362982,-8.266625,5.938658,-8.784900],[-0.970900,7.895436,-2.133263,-6.423790,3.594079,-1.445091,5.082801,-3.605800,3.321565,-9.178576,-6.457512,-7.607224,-6.675664,8.613019,4.834830,3.245127],[-3.153635,2.283909,-7.198007,-8.392563,-1.345965,5.383223,-4.148703,1.185418,3.202407,-0.891118,7.984293,2.114237,-5.741075,7.660982,-9.351874,5.889013]],[[9.676089,-1.651277,1.454220,-6.226817,6.702908,6.416200,1.111649,-6.921038,-7.370048,-7.174306,4.267530,-1.610123,-0.365737,-2.050132,-1.460399,6.955571],[-4.954987,-7.777117,-6.406852,7.393607,-0.115106,8.811699,-4.829023,-9.234560,8.072497,-1.660624,1.693691,-6.558944,-5.697189,-7.204961,-8.458742,-8.565510],[3.980779,-8.488040,1.323285,-1.363774,4.160822,-9.465660,0.530558,-9.075460,4.209881,0.740010,7.740516,6.861880,-4.370266,1.015694,8.641191,6.629712],[-4.070678,7.887098,-4.241848,5.692705,8.794925,4.078396,-6.076135,0.678340,-1.553194,-7.414518,-4.931586,9.258022,-0.710294,-0.724246,-8.621225,-0.040102]],[[0.298352,0.270125,7.346466,1.905569,-6.201933,4.173059,1.491814,-2.569253,-6.361857,1.088815,-6.575674,6.874426,6.648974,6.712630,-8.770053,-2.887550],[2.284996,4.330252,-0.089678,9.905000,7.639491,-8.190390,-6.052820,-5.890997,5.105401,7.589583,-8.988985,-2.253951,-4.729184,2.197137,-6.019371,2.403919],[4.763666,-8.079999,0.252498,-3.263468,4.064649,6.378516,-6.389314,-1.133660,-9.432779,5.185226,-0.569165,-3.043012,3.385869,1.749423,-2.442683,6.738027],[1.660022,7.233630,-8.250251,2.026434,-3.970795,9.810732,-2.406108,6.649607,0.114838,1.377551,-7.559094,1.128926,-3.337818,0.990534,4.273836,-9.041229]],[[9.324563,1.813466,-8.012947,8.402119,-3.587141,1.738852,-1.360352,7.892564,1.783236,1.230517,-1.467858,-7.355299,-5.713933,9.035951,-5.640451,-3.274964],[-8.990088,6.146861,3.236618,8.252518,1.085390,-4.518980,2.171403,-3.087257,8.161427,0.717003,-4.914088,-8.392566,5.359635,-2.487300,7.266243,5.128679],[-0.054588,-5.222259,6.505812,5.187497,-9.849463,-4.493538,4.079185,9.136615,1.746370,0.024755,-1.196895,-1.120991,1.522985,6.515324,7.509632,-4.400338],[-6.306379,4.740820,3.074859,-1.943058,5.439450,1.177503,4.232522,5.112641,8.909492,-9.311993,-3.157263,-6.209614,4.081919,-3.284909,-2.679822,8.965805]]], dtype = "float32")#candidate|1046|(7, 4, 16)|const|float32
bop_1047 = relay.bitwise_or(call_1029.astype('uint16'), relay.reshape(const_1046.astype('uint16'), relay.shape_of(call_1029))) # shape=(7, 4, 16)
bop_1050 = relay.bitwise_or(call_1032.astype('uint16'), relay.reshape(const_1046.astype('uint16'), relay.shape_of(call_1032))) # shape=(7, 4, 16)
func_19_call = mod.get_global_var('func_19')
func_22_call = mutated_mod.get_global_var('func_22')
call_1053 = relay.TupleGetItem(func_19_call(relay.reshape(var_1030.astype('int8'), [7, 4, 1]), relay.reshape(bop_1047.astype('int8'), [7, 4, 16]), ), 0)
call_1054 = relay.TupleGetItem(func_22_call(relay.reshape(var_1030.astype('int8'), [7, 4, 1]), relay.reshape(bop_1047.astype('int8'), [7, 4, 16]), ), 0)
func_233_call = mod.get_global_var('func_233')
func_236_call = mutated_mod.get_global_var('func_236')
const_1059 = relay.const([-7.329527,4.055803,7.638803,-2.712517,9.296325,-8.834808,-6.174639,-1.705548,5.182130,-8.968672,-6.880288,-5.767526,6.961348,-4.153052,-6.741612,-9.574269,5.769045,-3.205597,-2.042660,7.056745,-9.006468,-2.513807,9.395725,6.451572], dtype = "float64")#candidate|1059|(24,)|const|float64
call_1058 = relay.TupleGetItem(func_233_call(relay.reshape(const_1059.astype('float64'), [24,]), relay.reshape(var_1030.astype('int8'), [28,]), ), 0)
call_1060 = relay.TupleGetItem(func_236_call(relay.reshape(const_1059.astype('float64'), [24,]), relay.reshape(var_1030.astype('int8'), [28,]), ), 0)
uop_1061 = relay.acosh(bop_1047.astype('float64')) # shape=(7, 4, 16)
uop_1063 = relay.acosh(bop_1050.astype('float64')) # shape=(7, 4, 16)
output = relay.Tuple([bop_1023,var_1030,var_1031,call_1053,call_1058,const_1059,uop_1061,])
output2 = relay.Tuple([bop_1023,var_1030,var_1031,call_1054,call_1060,const_1059,uop_1063,])
func_1068 = relay.Function([var_1022,var_1030,var_1031,], output)
mod['func_1068'] = func_1068
mod = relay.transform.InferType()(mod)
var_1069 = relay.var("var_1069", dtype = "int32", shape = (14, 12, 5))#candidate|1069|(14, 12, 5)|var|int32
var_1070 = relay.var("var_1070", dtype = "int8", shape = (7, 4))#candidate|1070|(7, 4)|var|int8
var_1071 = relay.var("var_1071", dtype = "int8", shape = (56, 8))#candidate|1071|(56, 8)|var|int8
output = func_1068(var_1069,var_1070,var_1071,)
func_1072 = relay.Function([var_1069,var_1070,var_1071,], output)
mutated_mod['func_1072'] = func_1072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_1077 = relay.TupleGetItem(func_975_call(), 0)
call_1078 = relay.TupleGetItem(func_976_call(), 0)
output = relay.Tuple([call_1077,])
output2 = relay.Tuple([call_1078,])
func_1104 = relay.Function([], output)
mod['func_1104'] = func_1104
mod = relay.transform.InferType()(mod)
output = func_1104()
func_1105 = relay.Function([], output)
mutated_mod['func_1105'] = func_1105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_1116 = relay.TupleGetItem(func_975_call(), 0)
call_1117 = relay.TupleGetItem(func_976_call(), 0)
output = relay.Tuple([call_1116,])
output2 = relay.Tuple([call_1117,])
func_1120 = relay.Function([], output)
mod['func_1120'] = func_1120
mod = relay.transform.InferType()(mod)
output = func_1120()
func_1121 = relay.Function([], output)
mutated_mod['func_1121'] = func_1121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_1127 = relay.TupleGetItem(func_1104_call(), 0)
call_1128 = relay.TupleGetItem(func_1105_call(), 0)
uop_1144 = relay.erf(call_1127.astype('float64')) # shape=(2, 9, 4)
uop_1146 = relay.erf(call_1128.astype('float64')) # shape=(2, 9, 4)
output = uop_1144
output2 = uop_1146
func_1157 = relay.Function([], output)
mod['func_1157'] = func_1157
mod = relay.transform.InferType()(mod)
output = func_1157()
func_1158 = relay.Function([], output)
mutated_mod['func_1158'] = func_1158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_1182 = relay.TupleGetItem(func_1120_call(), 0)
call_1183 = relay.TupleGetItem(func_1121_call(), 0)
output = call_1182
output2 = call_1183
func_1184 = relay.Function([], output)
mod['func_1184'] = func_1184
mod = relay.transform.InferType()(mod)
output = func_1184()
func_1185 = relay.Function([], output)
mutated_mod['func_1185'] = func_1185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_1188 = relay.TupleGetItem(func_1104_call(), 0)
call_1189 = relay.TupleGetItem(func_1105_call(), 0)
func_19_call = mod.get_global_var('func_19')
func_22_call = mutated_mod.get_global_var('func_22')
var_1207 = relay.var("var_1207", dtype = "int8", shape = (28, 1))#candidate|1207|(28, 1)|var|int8
var_1208 = relay.var("var_1208", dtype = "int8", shape = (448,))#candidate|1208|(448,)|var|int8
call_1206 = relay.TupleGetItem(func_19_call(relay.reshape(var_1207.astype('int8'), [7, 4, 1]), relay.reshape(var_1208.astype('int8'), [7, 4, 16]), ), 1)
call_1209 = relay.TupleGetItem(func_22_call(relay.reshape(var_1207.astype('int8'), [7, 4, 1]), relay.reshape(var_1208.astype('int8'), [7, 4, 16]), ), 1)
const_1215 = relay.const([[[2.028814,-7.989276,8.098737,-5.802121,-1.334396,0.651484,-3.609205,5.250274,4.453800,4.646172,7.977718,-9.364575,2.409665,9.467035,-6.334281,0.885488],[-5.015038,6.568513,9.356260,-4.908281,-7.866367,5.895175,-8.212255,-5.001632,-1.979880,4.610167,0.364390,2.650034,8.051872,1.867088,-9.468869,4.846563],[-8.178981,-4.399281,2.364330,8.415860,4.931117,-8.412103,-0.288308,5.436436,-7.293912,-5.682281,2.847784,4.905388,-4.490878,-5.158115,2.777517,-5.023704],[-8.267048,7.810889,6.575734,-3.997289,4.900459,-6.439118,8.854455,-4.149101,-5.843330,-3.821154,1.169731,-6.322231,-0.950283,-8.025607,3.543519,5.847581]],[[5.338488,5.586907,-6.213040,8.701903,-1.077707,2.266690,-2.840483,5.044557,-7.207198,-3.568192,6.663138,2.235968,0.046513,-6.779378,-3.327646,8.361988],[-1.942941,-2.940793,-3.227270,6.214810,4.381630,-0.281563,-7.537347,7.832402,8.323799,-0.993950,-2.971758,-0.316687,1.611930,-6.244377,0.980411,-0.736254],[-1.197573,-6.139069,-3.483898,0.913567,-2.255388,3.160072,-6.004472,6.479307,-4.363146,-9.229641,4.249357,5.388892,3.705750,9.495932,3.567585,9.429345],[-0.110719,-4.298451,4.519963,9.354677,2.423097,-2.577593,8.229888,-1.852197,-6.133173,-3.264899,4.531776,-7.762754,-2.471870,5.193066,2.338604,3.101296]],[[-2.104397,5.357956,-9.225012,5.495614,2.118799,7.233033,6.503755,4.338332,-9.792599,-4.891614,4.909225,6.537992,-8.859898,7.779203,0.247247,6.617109],[-6.706036,4.988799,3.145141,-1.761890,-0.909588,6.041047,2.475955,0.606605,6.466749,-2.762400,4.378278,-5.651371,-8.563325,8.651464,-3.353315,-4.845979],[3.501986,0.268689,-0.450938,-1.424433,2.475251,6.445673,-6.938367,2.510606,-9.675355,-7.912646,4.871905,9.610971,-3.604828,4.288794,6.041151,7.414413],[3.104022,-3.405112,-6.222583,-3.641500,-8.509923,9.915265,7.086430,-6.531598,-6.151761,7.800538,2.491997,7.418335,6.596066,0.990393,-2.732217,-3.345889]],[[1.430383,-9.596903,4.467516,-4.018190,-0.135847,-0.169812,-5.818137,2.689970,3.402248,-3.139552,4.366735,-3.290643,-0.149272,8.417288,-4.081844,-0.980021],[-3.905523,8.980062,6.135855,-6.869314,9.614862,7.834993,0.601924,-0.112253,5.838374,-9.719261,7.601295,-4.259823,-6.463798,-6.515692,5.494613,-4.642100],[8.697010,2.467144,4.940259,-1.138708,-1.132991,-0.654163,-0.872495,-2.664033,3.851135,-2.245991,4.583095,-7.635024,3.418899,-5.762934,5.768196,-1.942502],[-8.135686,-0.001338,4.081659,8.639537,-9.810740,-7.331420,-4.418746,6.543396,7.087453,-6.955860,-3.830172,-2.148946,-5.432522,-5.771397,8.824865,-4.869315]],[[-7.439009,-5.151593,-4.635540,7.104414,5.837007,9.744603,-3.320482,-3.400148,2.839317,-9.022924,9.599547,5.476863,1.420199,-8.396558,-1.279494,-5.091556],[8.168911,3.715082,-3.676452,-7.809155,-7.701527,-3.569067,-2.217417,-8.817784,3.567102,4.442005,8.967841,-2.666037,-0.192802,2.399490,-2.384450,1.430623],[-3.555785,8.643540,0.874490,3.899092,4.184006,-7.793342,-9.091015,6.175628,2.575214,-6.752743,8.531413,0.140145,7.492087,4.976993,5.275200,5.575026],[1.014169,-0.162664,5.107780,-2.387170,2.395994,-0.011644,8.485486,-5.550474,3.371907,9.536829,9.853487,-6.948696,0.657546,-2.260049,2.772908,9.276000]],[[-4.903444,5.541736,8.883389,8.657074,1.008618,-6.631662,5.824233,0.834495,0.736749,-7.971342,-8.657649,-7.478480,-0.632901,-1.867644,-6.594059,-1.170762],[7.844409,-6.410761,1.848651,-3.284236,-3.180458,0.569341,9.000102,-2.578009,0.458183,8.448613,9.213886,1.377207,6.068888,0.089818,0.987919,-8.219023],[-5.909726,6.694251,-8.657657,-4.042425,-3.363743,6.169113,-7.768264,1.953290,-9.988021,2.427238,-5.864134,8.050142,-5.152294,9.492887,-6.762029,8.849399],[8.120111,-3.250502,-2.297355,-1.117494,-7.128567,-0.609883,4.759922,-5.201808,-3.025140,3.042940,-2.669922,-7.633008,-9.096770,4.448573,-6.790145,3.457257]],[[0.010163,6.933747,-2.961358,1.176423,3.768708,6.042206,4.299526,-8.810161,-6.553049,-2.869231,-9.800597,5.737092,-8.268658,2.027367,8.664898,-0.993931],[-4.727562,-7.014212,8.961842,7.260925,0.671317,2.762424,-7.339555,4.309272,-3.753903,-9.292580,-4.169986,0.153733,-1.389204,1.389784,3.951317,-1.919129],[-9.756353,-5.691092,-6.992439,-6.132598,-3.334357,-3.711052,-0.901411,6.278795,4.231987,6.710451,-8.241330,0.706742,-0.913765,-2.903553,-6.709613,0.195950],[-7.534647,0.736994,-5.479817,-7.842584,6.233264,1.902546,-3.789630,-0.930837,-1.022281,-0.590668,-1.608560,4.437232,-9.646132,-6.251092,1.768606,8.317192]]], dtype = "float32")#candidate|1215|(7, 4, 16)|const|float32
bop_1216 = relay.bitwise_xor(call_1206.astype('uint16'), relay.reshape(const_1215.astype('uint16'), relay.shape_of(call_1206))) # shape=(7, 4, 16)
bop_1219 = relay.bitwise_xor(call_1209.astype('uint16'), relay.reshape(const_1215.astype('uint16'), relay.shape_of(call_1209))) # shape=(7, 4, 16)
output = relay.Tuple([call_1188,var_1207,var_1208,bop_1216,])
output2 = relay.Tuple([call_1189,var_1207,var_1208,bop_1219,])
func_1245 = relay.Function([var_1207,var_1208,], output)
mod['func_1245'] = func_1245
mod = relay.transform.InferType()(mod)
var_1246 = relay.var("var_1246", dtype = "int8", shape = (28, 1))#candidate|1246|(28, 1)|var|int8
var_1247 = relay.var("var_1247", dtype = "int8", shape = (448,))#candidate|1247|(448,)|var|int8
output = func_1245(var_1246,var_1247,)
func_1248 = relay.Function([var_1246,var_1247,], output)
mutated_mod['func_1248'] = func_1248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_1259 = func_1184_call()
call_1260 = func_1184_call()
output = call_1259
output2 = call_1260
func_1263 = relay.Function([], output)
mod['func_1263'] = func_1263
mod = relay.transform.InferType()(mod)
mutated_mod['func_1263'] = func_1263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1263_call = mutated_mod.get_global_var('func_1263')
call_1264 = func_1263_call()
output = call_1264
func_1265 = relay.Function([], output)
mutated_mod['func_1265'] = func_1265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_1304 = relay.TupleGetItem(func_975_call(), 0)
call_1305 = relay.TupleGetItem(func_976_call(), 0)
output = relay.Tuple([call_1304,])
output2 = relay.Tuple([call_1305,])
func_1309 = relay.Function([], output)
mod['func_1309'] = func_1309
mod = relay.transform.InferType()(mod)
mutated_mod['func_1309'] = func_1309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1309_call = mutated_mod.get_global_var('func_1309')
call_1310 = func_1309_call()
output = call_1310
func_1311 = relay.Function([], output)
mutated_mod['func_1311'] = func_1311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_1315 = func_1184_call()
call_1316 = func_1184_call()
const_1324 = relay.const([[[5.530819,-1.862747,0.166820,2.858796],[-9.628483,-4.871769,5.457469,2.025850],[5.957695,2.527799,-7.724793,-8.526340],[-0.895881,-6.290604,-2.924435,-3.485881],[-7.314585,8.847030,-0.534359,-3.275743],[5.450382,6.375323,-8.877997,-1.908348],[8.075908,3.699303,-7.062300,-6.341893],[-1.997568,-2.350655,5.845781,-8.735313],[1.071767,4.652100,-3.214222,-7.237057]],[[-9.400426,-1.325796,8.997529,8.361667],[9.435213,-3.813167,-1.217840,-3.286392],[8.303927,4.202248,2.085255,1.034149],[4.641308,-8.046294,-7.431670,7.623996],[-3.325873,1.884739,3.695126,6.124897],[9.122580,-9.215517,-4.601222,-7.818968],[0.865609,-0.401208,0.338397,4.758467],[-1.874995,7.786031,5.156156,-7.639498],[-5.783426,0.876736,-3.756484,-4.020217]]], dtype = "float32")#candidate|1324|(2, 9, 4)|const|float32
bop_1325 = relay.bitwise_and(call_1315.astype('uint32'), relay.reshape(const_1324.astype('uint32'), relay.shape_of(call_1315))) # shape=(2, 9, 4)
bop_1328 = relay.bitwise_and(call_1316.astype('uint32'), relay.reshape(const_1324.astype('uint32'), relay.shape_of(call_1316))) # shape=(2, 9, 4)
func_1263_call = mod.get_global_var('func_1263')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_1337 = func_1263_call()
call_1338 = func_1263_call()
output = relay.Tuple([bop_1325,call_1337,])
output2 = relay.Tuple([bop_1328,call_1338,])
func_1340 = relay.Function([], output)
mod['func_1340'] = func_1340
mod = relay.transform.InferType()(mod)
output = func_1340()
func_1341 = relay.Function([], output)
mutated_mod['func_1341'] = func_1341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_1353 = relay.TupleGetItem(func_1309_call(), 0)
call_1354 = relay.TupleGetItem(func_1311_call(), 0)
output = call_1353
output2 = call_1354
func_1368 = relay.Function([], output)
mod['func_1368'] = func_1368
mod = relay.transform.InferType()(mod)
mutated_mod['func_1368'] = func_1368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1368_call = mutated_mod.get_global_var('func_1368')
call_1369 = func_1368_call()
output = call_1369
func_1370 = relay.Function([], output)
mutated_mod['func_1370'] = func_1370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_1424 = relay.TupleGetItem(func_1120_call(), 0)
call_1425 = relay.TupleGetItem(func_1121_call(), 0)
func_1157_call = mod.get_global_var('func_1157')
func_1158_call = mutated_mod.get_global_var('func_1158')
call_1428 = func_1157_call()
call_1429 = func_1157_call()
output = relay.Tuple([call_1424,call_1428,])
output2 = relay.Tuple([call_1425,call_1429,])
func_1449 = relay.Function([], output)
mod['func_1449'] = func_1449
mod = relay.transform.InferType()(mod)
mutated_mod['func_1449'] = func_1449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1449_call = mutated_mod.get_global_var('func_1449')
call_1450 = func_1449_call()
output = call_1450
func_1451 = relay.Function([], output)
mutated_mod['func_1451'] = func_1451
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1512 = relay.var("var_1512", dtype = "float64", shape = (10, 8, 5))#candidate|1512|(10, 8, 5)|var|float64
uop_1513 = relay.acosh(var_1512.astype('float64')) # shape=(10, 8, 5)
output = uop_1513
output2 = uop_1513
func_1527 = relay.Function([var_1512,], output)
mod['func_1527'] = func_1527
mod = relay.transform.InferType()(mod)
var_1528 = relay.var("var_1528", dtype = "float64", shape = (10, 8, 5))#candidate|1528|(10, 8, 5)|var|float64
output = func_1527(var_1528)
func_1529 = relay.Function([var_1528], output)
mutated_mod['func_1529'] = func_1529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1263_call = mod.get_global_var('func_1263')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_1540 = func_1263_call()
call_1541 = func_1263_call()
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_1549 = relay.TupleGetItem(func_1309_call(), 0)
call_1550 = relay.TupleGetItem(func_1311_call(), 0)
func_1340_call = mod.get_global_var('func_1340')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_1551 = relay.TupleGetItem(func_1340_call(), 0)
call_1552 = relay.TupleGetItem(func_1341_call(), 0)
func_1449_call = mod.get_global_var('func_1449')
func_1451_call = mutated_mod.get_global_var('func_1451')
call_1580 = relay.TupleGetItem(func_1449_call(), 0)
call_1581 = relay.TupleGetItem(func_1451_call(), 0)
func_159_call = mod.get_global_var('func_159')
func_164_call = mutated_mod.get_global_var('func_164')
var_1583 = relay.var("var_1583", dtype = "float64", shape = (24, 1))#candidate|1583|(24, 1)|var|float64
var_1584 = relay.var("var_1584", dtype = "int8", shape = (28,))#candidate|1584|(28,)|var|int8
const_1585 = relay.const([[-3,5,-5,8,9,3,-2,5,-1,4,6,6,8,-4,5,-8,-9,2,-7,-3,6,6,-8,-10,4,10,5,-9,-9,-10,4,-3,-1,8,-5,-8,10,1,-5,-10,4,-8,-8,-1,-1,-1,1,8,1,3,1,-1,3,1,-10,6,1,-4,-4,-5,-8,-10,4,-2,-5,5,4,7,5,-7,8,-10,9,9,-10,6,1,-8,5,-2,-5,-6,-10,-8,2,-9,-9,3,-4,1,5,2,5,-4,2,-1,-10,5,2,6,-9,8,5,-3,-2,-5,-2,-6,8,7,6,4],[5,-8,5,4,-1,9,4,7,8,4,8,7,9,-6,2,-1,-1,5,-2,-7,1,-9,10,10,9,-8,-5,-2,8,9,8,-8,-10,-5,2,-7,10,6,5,7,-10,-10,-9,1,-10,9,2,-9,10,9,7,-3,-4,-8,4,3,-10,1,3,9,2,-5,7,9,9,-9,5,-5,10,-8,-1,-10,-1,-2,-3,-2,-1,1,1,5,-9,-8,4,-3,-9,1,-3,-10,-4,-3,-3,3,-1,2,-6,4,1,2,-9,2,-8,-7,5,-7,10,-7,-4,7,-7,-9,-5,-10],[9,2,7,-4,-8,-5,-8,4,-2,-1,3,2,-6,-3,-6,-7,-5,10,4,6,-9,-5,-5,5,1,-6,3,-4,-10,1,-2,-2,-7,8,10,-3,8,4,-6,3,-6,-2,8,9,5,-8,8,3,-2,-9,8,9,-10,9,5,-5,-2,1,3,10,10,2,-5,5,7,-2,-6,10,8,-5,-1,4,-7,3,-5,-7,-10,4,5,5,-3,-8,-7,-8,8,-8,4,-2,6,-1,8,-7,7,4,-1,6,5,7,-2,9,-10,9,-8,3,6,-7,1,5,-5,10,7,4],[-9,5,7,1,10,9,3,-4,-7,-7,6,6,8,-9,-3,-8,5,-6,-9,8,-9,7,-1,2,3,8,-9,3,2,4,-7,10,8,-2,2,-6,9,4,-6,1,6,-1,4,4,-5,3,-3,-4,8,-5,6,-3,5,-6,-4,2,-6,4,-4,10,-7,1,-8,8,-1,-10,6,-5,-1,-4,7,4,7,-5,-6,-2,10,2,10,-3,5,-9,7,2,4,2,1,7,5,1,-9,-4,-8,-6,-6,-9,-4,-4,4,-8,3,2,-9,-4,-4,-6,9,1,-6,-6,-8,5]], dtype = "int8")#candidate|1585|(4, 112)|const|int8
call_1582 = relay.TupleGetItem(func_159_call(relay.reshape(var_1583.astype('float64'), [4, 2, 3]), relay.reshape(var_1584.astype('int8'), [28,]), relay.reshape(const_1585.astype('int8'), [448,]), ), 5)
call_1586 = relay.TupleGetItem(func_164_call(relay.reshape(var_1583.astype('float64'), [4, 2, 3]), relay.reshape(var_1584.astype('int8'), [28,]), relay.reshape(const_1585.astype('int8'), [448,]), ), 5)
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_1587 = relay.TupleGetItem(func_1309_call(), 0)
call_1588 = relay.TupleGetItem(func_1311_call(), 0)
output = relay.Tuple([call_1540,call_1549,call_1551,call_1580,call_1582,var_1583,var_1584,const_1585,call_1587,])
output2 = relay.Tuple([call_1541,call_1550,call_1552,call_1581,call_1586,var_1583,var_1584,const_1585,call_1588,])
func_1595 = relay.Function([var_1583,var_1584,], output)
mod['func_1595'] = func_1595
mod = relay.transform.InferType()(mod)
var_1596 = relay.var("var_1596", dtype = "float64", shape = (24, 1))#candidate|1596|(24, 1)|var|float64
var_1597 = relay.var("var_1597", dtype = "int8", shape = (28,))#candidate|1597|(28,)|var|int8
output = func_1595(var_1596,var_1597,)
func_1598 = relay.Function([var_1596,var_1597,], output)
mutated_mod['func_1598'] = func_1598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_1664 = relay.TupleGetItem(func_1309_call(), 0)
call_1665 = relay.TupleGetItem(func_1311_call(), 0)
func_233_call = mod.get_global_var('func_233')
func_236_call = mutated_mod.get_global_var('func_236')
var_1668 = relay.var("var_1668", dtype = "float64", shape = (2, 12))#candidate|1668|(2, 12)|var|float64
var_1669 = relay.var("var_1669", dtype = "int8", shape = (1, 28))#candidate|1669|(1, 28)|var|int8
call_1667 = relay.TupleGetItem(func_233_call(relay.reshape(var_1668.astype('float64'), [24,]), relay.reshape(var_1669.astype('int8'), [28,]), ), 6)
call_1670 = relay.TupleGetItem(func_236_call(relay.reshape(var_1668.astype('float64'), [24,]), relay.reshape(var_1669.astype('int8'), [28,]), ), 6)
func_1068_call = mod.get_global_var('func_1068')
func_1072_call = mutated_mod.get_global_var('func_1072')
const_1672 = relay.const([[1,9,7,2,-9,-3,-10,7,-5,-7,-5,-6,-4,-5,-8,-6,-10,-2,6,-10,-1,-5,-3,-7,3,-1,-4,5,3,-2,-10,7,-5,7,-3,6,2,-6,-4,-5,-6,7,-5,-8,10,-7,-10,10,-5,9,-6,3,8,2,2,-9,4,-10,6,-5,-8,9,-9,3,6,2,-9,-7,-6,-7,6,9,-3,9,7,-8,-6,-2,5,-9,-9,10,-7,5,6,2,-9,2,-9,1,-4,-2,-7,-7,2,-1,8,1,10,9,-7,10,3,7,-2,10,9,-6,6,9,9,1,3,3,7,1,-4,-9,2,2,6,10,6,4,-9,-2,-2,6,-8,-1,10,8,-5,-4,4,-3,-8,6,8,7],[-10,6,5,-1,10,7,-6,-5,-1,1,2,6,6,-5,-1,-2,3,-4,9,-3,-7,-8,-5,-7,-1,-2,10,-5,9,1,-4,10,10,-8,-9,-5,-1,-3,-5,3,-7,-8,-4,-5,3,-2,8,6,7,-6,-7,7,3,2,-8,-3,1,-6,-4,-9,-9,-6,6,5,-8,-2,-2,-10,-8,-5,1,-5,-1,9,-2,-4,1,9,4,1,-7,-6,3,-5,10,9,-8,-4,-5,-4,-1,-9,-8,8,-4,-3,-3,9,-7,-8,4,8,4,-3,-7,8,-7,10,5,9,-8,-10,3,8,-4,7,-4,4,-9,8,3,-3,3,8,-5,7,9,-6,-7,-10,-1,-10,2,-4,8,8,-8,-4,6,8],[8,5,-5,10,5,2,7,-2,4,1,-10,7,-9,8,4,-5,3,10,10,7,-7,1,1,-4,-1,-8,3,-8,8,-6,-2,-5,-10,3,2,-7,-1,5,-4,-8,4,-8,1,7,-2,2,-5,-8,-1,-7,1,3,4,3,-9,-5,-6,9,-8,9,-3,-3,9,5,2,-10,-6,4,-3,10,-9,4,-7,-7,1,-5,8,-3,9,6,10,4,-10,-7,-9,-2,1,6,-9,5,8,6,-7,-4,7,-8,7,-4,-10,2,8,-8,2,-1,6,2,-5,3,-9,10,8,-4,10,3,-9,-1,-1,-9,4,3,-3,5,3,-2,4,10,-10,8,10,-1,-8,-7,-3,9,6,9,-7,9,-2,-4],[-5,-10,-9,-6,-2,10,-3,-7,5,6,-8,-1,9,6,-1,10,5,10,2,4,4,4,-3,4,8,9,2,2,-10,-5,-9,6,8,-9,-1,-2,7,2,8,-9,-3,4,-10,9,5,2,10,1,5,8,-2,-1,-8,-10,9,3,-10,9,3,4,3,-3,6,-3,-5,5,3,10,-10,-8,-2,1,7,-3,-8,-8,3,-6,-7,-7,9,-2,1,4,4,10,-2,-7,-1,-7,7,1,-9,8,5,-10,1,-9,-6,4,4,6,-5,4,5,-6,-7,4,-4,-3,2,-3,9,-3,-6,5,-1,5,5,-3,-1,5,-5,-5,3,-8,-3,-6,-5,-7,8,-1,4,6,-5,2,-7,5,5,-1],[-10,-3,-9,5,-10,5,6,-8,1,-4,2,-4,2,-10,-9,-5,-7,-4,-7,-10,-3,6,8,2,5,-8,1,-5,1,-1,-6,1,-7,10,4,-5,-3,-6,3,2,5,7,2,-10,7,7,-2,-7,-3,-4,-6,-4,8,-4,10,-8,-8,3,-7,4,6,9,10,-6,-4,-4,9,-1,-9,-7,3,-4,-2,-10,9,7,7,-3,4,4,10,-8,5,6,-6,-3,-10,-7,-3,3,5,9,-6,3,-2,5,4,-10,5,-2,-9,-10,-1,1,-6,-8,-4,4,-9,-9,-3,-4,-10,-3,10,-7,-10,10,-6,7,-7,4,2,-3,-5,4,9,-5,2,-7,5,3,-3,-9,6,-2,1,-6,3,5],[-2,-8,-9,-9,10,5,-1,3,1,-2,7,10,9,-2,5,-4,8,-7,4,-8,-3,-2,-1,-6,-6,-1,-4,3,-7,8,4,-9,4,9,-2,-4,2,-7,2,7,-6,1,1,3,-8,-10,-5,-7,4,8,-3,-1,10,-7,-3,-10,-5,9,6,-6,7,9,6,2,1,6,-4,-8,4,9,-2,-8,-10,4,3,2,-5,-1,-6,1,-2,-1,3,-1,9,-8,-8,9,-5,6,3,7,9,-9,8,-2,6,-7,7,7,9,-6,-2,-5,-7,5,8,-8,-10,4,6,8,-3,10,-4,-5,-2,10,-5,-3,5,-4,1,-2,10,1,-3,-9,-6,6,8,5,-2,6,-9,4,10,-10,2,4]], dtype = "int32")#candidate|1672|(6, 140)|const|int32
call_1671 = relay.TupleGetItem(func_1068_call(relay.reshape(const_1672.astype('int32'), [14, 12, 5]), relay.reshape(var_1669.astype('int8'), [7, 4]), relay.reshape(call_1667.astype('int8'), [56, 8]), ), 6)
call_1673 = relay.TupleGetItem(func_1072_call(relay.reshape(const_1672.astype('int32'), [14, 12, 5]), relay.reshape(var_1669.astype('int8'), [7, 4]), relay.reshape(call_1667.astype('int8'), [56, 8]), ), 6)
func_233_call = mod.get_global_var('func_233')
func_236_call = mutated_mod.get_global_var('func_236')
call_1693 = relay.TupleGetItem(func_233_call(relay.reshape(var_1668.astype('float64'), [24,]), relay.reshape(var_1669.astype('int8'), [28,]), ), 1)
call_1694 = relay.TupleGetItem(func_236_call(relay.reshape(var_1668.astype('float64'), [24,]), relay.reshape(var_1669.astype('int8'), [28,]), ), 1)
var_1695 = relay.var("var_1695", dtype = "int32", shape = (6, 140))#candidate|1695|(6, 140)|var|int32
bop_1696 = relay.equal(const_1672.astype('bool'), relay.reshape(var_1695.astype('bool'), relay.shape_of(const_1672))) # shape=(6, 140)
var_1715 = relay.var("var_1715", dtype = "int32", shape = (6, 140))#candidate|1715|(6, 140)|var|int32
bop_1716 = relay.left_shift(var_1695.astype('int64'), relay.reshape(var_1715.astype('int64'), relay.shape_of(var_1695))) # shape=(6, 140)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_1719 = relay.TupleGetItem(func_1104_call(), 0)
call_1720 = relay.TupleGetItem(func_1105_call(), 0)
output = relay.Tuple([call_1664,call_1667,var_1668,var_1669,call_1671,call_1693,bop_1696,bop_1716,call_1719,])
output2 = relay.Tuple([call_1665,call_1670,var_1668,var_1669,call_1673,call_1694,bop_1696,bop_1716,call_1720,])
func_1723 = relay.Function([var_1668,var_1669,var_1695,var_1715,], output)
mod['func_1723'] = func_1723
mod = relay.transform.InferType()(mod)
mutated_mod['func_1723'] = func_1723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1723_call = mutated_mod.get_global_var('func_1723')
var_1725 = relay.var("var_1725", dtype = "float64", shape = (2, 12))#candidate|1725|(2, 12)|var|float64
var_1726 = relay.var("var_1726", dtype = "int8", shape = (1, 28))#candidate|1726|(1, 28)|var|int8
var_1727 = relay.var("var_1727", dtype = "int32", shape = (6, 140))#candidate|1727|(6, 140)|var|int32
var_1728 = relay.var("var_1728", dtype = "int32", shape = (6, 140))#candidate|1728|(6, 140)|var|int32
call_1724 = func_1723_call(var_1725,var_1726,var_1727,var_1728,)
output = call_1724
func_1729 = relay.Function([var_1725,var_1726,var_1727,var_1728,], output)
mutated_mod['func_1729'] = func_1729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_1757 = relay.TupleGetItem(func_1309_call(), 0)
call_1758 = relay.TupleGetItem(func_1311_call(), 0)
func_1263_call = mod.get_global_var('func_1263')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_1796 = func_1263_call()
call_1797 = func_1263_call()
uop_1799 = relay.acos(call_1757.astype('float64')) # shape=(2, 9, 4)
uop_1801 = relay.acos(call_1758.astype('float64')) # shape=(2, 9, 4)
uop_1804 = relay.rsqrt(uop_1799.astype('float32')) # shape=(2, 9, 4)
uop_1806 = relay.rsqrt(uop_1801.astype('float32')) # shape=(2, 9, 4)
func_1368_call = mod.get_global_var('func_1368')
func_1370_call = mutated_mod.get_global_var('func_1370')
call_1826 = func_1368_call()
call_1827 = func_1368_call()
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_1849 = relay.TupleGetItem(func_1309_call(), 0)
call_1850 = relay.TupleGetItem(func_1311_call(), 0)
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_1852 = relay.TupleGetItem(func_1309_call(), 0)
call_1853 = relay.TupleGetItem(func_1311_call(), 0)
output = relay.Tuple([call_1796,uop_1804,call_1826,call_1849,call_1852,])
output2 = relay.Tuple([call_1797,uop_1806,call_1827,call_1850,call_1853,])
func_1864 = relay.Function([], output)
mod['func_1864'] = func_1864
mod = relay.transform.InferType()(mod)
output = func_1864()
func_1865 = relay.Function([], output)
mutated_mod['func_1865'] = func_1865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_1907 = func_1184_call()
call_1908 = func_1184_call()
func_1263_call = mod.get_global_var('func_1263')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_1932 = func_1263_call()
call_1933 = func_1263_call()
output = relay.Tuple([call_1907,call_1932,])
output2 = relay.Tuple([call_1908,call_1933,])
func_1934 = relay.Function([], output)
mod['func_1934'] = func_1934
mod = relay.transform.InferType()(mod)
mutated_mod['func_1934'] = func_1934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1934_call = mutated_mod.get_global_var('func_1934')
call_1935 = func_1934_call()
output = call_1935
func_1936 = relay.Function([], output)
mutated_mod['func_1936'] = func_1936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_1966 = func_1184_call()
call_1967 = func_1184_call()
func_1340_call = mod.get_global_var('func_1340')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_1987 = relay.TupleGetItem(func_1340_call(), 0)
call_1988 = relay.TupleGetItem(func_1341_call(), 0)
output = relay.Tuple([call_1966,call_1987,])
output2 = relay.Tuple([call_1967,call_1988,])
func_1989 = relay.Function([], output)
mod['func_1989'] = func_1989
mod = relay.transform.InferType()(mod)
mutated_mod['func_1989'] = func_1989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1989_call = mutated_mod.get_global_var('func_1989')
call_1990 = func_1989_call()
output = call_1990
func_1991 = relay.Function([], output)
mutated_mod['func_1991'] = func_1991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1263_call = mod.get_global_var('func_1263')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_2017 = func_1263_call()
call_2018 = func_1263_call()
output = call_2017
output2 = call_2018
func_2025 = relay.Function([], output)
mod['func_2025'] = func_2025
mod = relay.transform.InferType()(mod)
mutated_mod['func_2025'] = func_2025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2025_call = mutated_mod.get_global_var('func_2025')
call_2026 = func_2025_call()
output = call_2026
func_2027 = relay.Function([], output)
mutated_mod['func_2027'] = func_2027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_2028 = relay.TupleGetItem(func_1309_call(), 0)
call_2029 = relay.TupleGetItem(func_1311_call(), 0)
output = call_2028
output2 = call_2029
func_2035 = relay.Function([], output)
mod['func_2035'] = func_2035
mod = relay.transform.InferType()(mod)
output = func_2035()
func_2036 = relay.Function([], output)
mutated_mod['func_2036'] = func_2036
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2052 = relay.var("var_2052", dtype = "uint64", shape = (5, 6, 2))#candidate|2052|(5, 6, 2)|var|uint64
var_2053 = relay.var("var_2053", dtype = "uint64", shape = (5, 6, 2))#candidate|2053|(5, 6, 2)|var|uint64
bop_2054 = relay.right_shift(var_2052.astype('uint64'), relay.reshape(var_2053.astype('uint64'), relay.shape_of(var_2052))) # shape=(5, 6, 2)
output = bop_2054
output2 = bop_2054
func_2078 = relay.Function([var_2052,var_2053,], output)
mod['func_2078'] = func_2078
mod = relay.transform.InferType()(mod)
mutated_mod['func_2078'] = func_2078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2078_call = mutated_mod.get_global_var('func_2078')
var_2080 = relay.var("var_2080", dtype = "uint64", shape = (5, 6, 2))#candidate|2080|(5, 6, 2)|var|uint64
var_2081 = relay.var("var_2081", dtype = "uint64", shape = (5, 6, 2))#candidate|2081|(5, 6, 2)|var|uint64
call_2079 = func_2078_call(var_2080,var_2081,)
output = call_2079
func_2082 = relay.Function([var_2080,var_2081,], output)
mutated_mod['func_2082'] = func_2082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1368_call = mod.get_global_var('func_1368')
func_1370_call = mutated_mod.get_global_var('func_1370')
call_2089 = func_1368_call()
call_2090 = func_1368_call()
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_2099 = relay.TupleGetItem(func_975_call(), 0)
call_2100 = relay.TupleGetItem(func_976_call(), 0)
func_1527_call = mod.get_global_var('func_1527')
func_1529_call = mutated_mod.get_global_var('func_1529')
var_2105 = relay.var("var_2105", dtype = "float64", shape = (400,))#candidate|2105|(400,)|var|float64
call_2104 = func_1527_call(relay.reshape(var_2105.astype('float64'), [10, 8, 5]))
call_2106 = func_1527_call(relay.reshape(var_2105.astype('float64'), [10, 8, 5]))
output = relay.Tuple([call_2089,call_2099,call_2104,var_2105,])
output2 = relay.Tuple([call_2090,call_2100,call_2106,var_2105,])
func_2119 = relay.Function([var_2105,], output)
mod['func_2119'] = func_2119
mod = relay.transform.InferType()(mod)
mutated_mod['func_2119'] = func_2119
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2120 = relay.var("var_2120", dtype = "float64", shape = (400,))#candidate|2120|(400,)|var|float64
func_2119_call = mutated_mod.get_global_var('func_2119')
call_2121 = func_2119_call(var_2120)
output = call_2121
func_2122 = relay.Function([var_2120], output)
mutated_mod['func_2122'] = func_2122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1934_call = mod.get_global_var('func_1934')
func_1936_call = mutated_mod.get_global_var('func_1936')
call_2155 = relay.TupleGetItem(func_1934_call(), 0)
call_2156 = relay.TupleGetItem(func_1936_call(), 0)
func_19_call = mod.get_global_var('func_19')
func_22_call = mutated_mod.get_global_var('func_22')
const_2172 = relay.const([7,-9,-3,-10,2,-10,-4,5,4,3,-2,-5,6,-7,1,9,10,-6,10,3,-6,5,9,-1,-2,10,1,6], dtype = "int8")#candidate|2172|(28,)|const|int8
const_2173 = relay.const([4,-10,8,3,-4,-2,7,1,7,9,-1,-4,6,6,-3,-4,-1,-2,-4,-2,7,7,-1,5,-6,-8,7,10,7,5,9,7,-4,8,1,6,4,-4,-10,3,-5,-5,-2,8,-2,-9,2,10,2,-4,8,3,-3,-4,-9,-1,7,9,-2,9,9,5,-2,5,-1,-9,9,10,10,-7,1,3,3,-7,8,8,-6,7,6,-3,5,7,-5,-7,10,-6,-1,9,1,-10,-6,6,-1,-9,9,5,4,-7,8,-6,8,-7,10,-5,-6,2,5,-3,3,3,-3,-5,2,-8,7,-7,3,-8,-4,4,9,-1,3,1,7,7,4,-9,-5,-5,10,-9,-5,-5,-9,-8,-6,3,4,-7,-7,3,8,6,-6,8,-2,-10,-6,-8,6,5,9,-3,-1,-6,-5,-10,8,8,6,1,-7,-6,5,-7,-2,-5,2,3,-10,-2,5,-10,9,-8,-8,-4,1,-7,4,1,8,-6,-6,6,8,-3,-1,8,4,4,7,6,-7,-6,9,-6,3,-1,-1,-7,4,-1,-2,6,5,8,7,-3,9,7,7,8,5,3,6,-4,7,-7,4,-6,3,-2,2,-7,7,2,7,-5,9,8,-7,8,-8,6,-8,1,-10,2,-10,-2,2,2,6,-4,7,-2,4,10,-5,-4,-1,-2,1,3,-4,-10,-1,-8,2,-1,3,5,3,1,-2,-1,-1,-3,9,-6,1,1,-10,8,-2,1,4,3,1,-5,1,7,-9,6,8,-2,2,2,4,-4,-1,-2,-2,4,10,-8,5,5,-10,1,7,-9,-7,-10,3,9,-10,-10,-7,6,4,-10,-9,-5,10,-7,9,5,-8,-1,9,-6,-1,1,-1,-7,9,5,4,9,6,-10,-3,-3,10,-2,3,7,-2,-4,-5,9,-10,-4,-2,10,-2,-3,7,-5,-1,7,-5,-8,3,2,-4,-4,5,9,-2,7,1,-8,-7,5,-10,-10,7,3,-3,-9,-6,-1,10,10,1,7,-7,-10,10,10,6,-6,-1,4,-4,1,6,10,-2,-2,-8,-6,-6,9,10,7,-3,-10,3,-8,-8,6,-1,-4,9,-7,-4,3,-7,-7,6,-6,10,3,1,10,-2,-5,-3,5,2,-10,-3,8,7,-9,-3,2,-1,7,-8,-3,-1,5,-7,7,-2,-8,10,-7,5,-8,2,-10], dtype = "int8")#candidate|2173|(448,)|const|int8
call_2171 = relay.TupleGetItem(func_19_call(relay.reshape(const_2172.astype('int8'), [7, 4, 1]), relay.reshape(const_2173.astype('int8'), [7, 4, 16]), ), 0)
call_2174 = relay.TupleGetItem(func_22_call(relay.reshape(const_2172.astype('int8'), [7, 4, 1]), relay.reshape(const_2173.astype('int8'), [7, 4, 16]), ), 0)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_2176 = relay.TupleGetItem(func_1120_call(), 0)
call_2177 = relay.TupleGetItem(func_1121_call(), 0)
var_2180 = relay.var("var_2180", dtype = "float32", shape = (2, 9, 4))#candidate|2180|(2, 9, 4)|var|float32
bop_2181 = relay.multiply(call_2155.astype('int32'), relay.reshape(var_2180.astype('int32'), relay.shape_of(call_2155))) # shape=(2, 9, 4)
bop_2184 = relay.multiply(call_2156.astype('int32'), relay.reshape(var_2180.astype('int32'), relay.shape_of(call_2156))) # shape=(2, 9, 4)
bop_2189 = relay.power(call_2171.astype('float32'), relay.reshape(const_2173.astype('float32'), relay.shape_of(call_2171))) # shape=(7, 4, 16)
bop_2192 = relay.power(call_2174.astype('float32'), relay.reshape(const_2173.astype('float32'), relay.shape_of(call_2174))) # shape=(7, 4, 16)
func_1723_call = mod.get_global_var('func_1723')
func_1729_call = mutated_mod.get_global_var('func_1729')
var_2198 = relay.var("var_2198", dtype = "float64", shape = (24,))#candidate|2198|(24,)|var|float64
var_2199 = relay.var("var_2199", dtype = "int32", shape = (840,))#candidate|2199|(840,)|var|int32
call_2197 = relay.TupleGetItem(func_1723_call(relay.reshape(var_2198.astype('float64'), [2, 12]), relay.reshape(const_2172.astype('int8'), [1, 28]), relay.reshape(var_2199.astype('int32'), [6, 140]), relay.reshape(var_2199.astype('int32'), [6, 140]), ), 0)
call_2200 = relay.TupleGetItem(func_1729_call(relay.reshape(var_2198.astype('float64'), [2, 12]), relay.reshape(const_2172.astype('int8'), [1, 28]), relay.reshape(var_2199.astype('int32'), [6, 140]), relay.reshape(var_2199.astype('int32'), [6, 140]), ), 0)
output = relay.Tuple([const_2172,call_2176,bop_2181,bop_2189,call_2197,var_2198,var_2199,])
output2 = relay.Tuple([const_2172,call_2177,bop_2184,bop_2192,call_2200,var_2198,var_2199,])
func_2204 = relay.Function([var_2180,var_2198,var_2199,], output)
mod['func_2204'] = func_2204
mod = relay.transform.InferType()(mod)
mutated_mod['func_2204'] = func_2204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2204_call = mutated_mod.get_global_var('func_2204')
var_2206 = relay.var("var_2206", dtype = "float32", shape = (2, 9, 4))#candidate|2206|(2, 9, 4)|var|float32
var_2207 = relay.var("var_2207", dtype = "float64", shape = (24,))#candidate|2207|(24,)|var|float64
var_2208 = relay.var("var_2208", dtype = "int32", shape = (840,))#candidate|2208|(840,)|var|int32
call_2205 = func_2204_call(var_2206,var_2207,var_2208,)
output = call_2205
func_2209 = relay.Function([var_2206,var_2207,var_2208,], output)
mutated_mod['func_2209'] = func_2209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_2219 = relay.TupleGetItem(func_1120_call(), 0)
call_2220 = relay.TupleGetItem(func_1121_call(), 0)
func_2078_call = mod.get_global_var('func_2078')
func_2082_call = mutated_mod.get_global_var('func_2082')
const_2222 = relay.const([2,-1,-3,9,3,6,-5,2,1,-5,1,7,9,-8,6,2,7,2,-4,7,-2,-5,-8,-4,8,-3,-7,-5,-2,-5,-10,6,-10,-9,-1,2,-9,-10,-3,4,-6,-10,-9,7,10,8,9,-7,-4,5,-1,9,-5,-7,-5,-10,7,-4,-7,-8], dtype = "uint64")#candidate|2222|(60,)|const|uint64
call_2221 = func_2078_call(relay.reshape(const_2222.astype('uint64'), [5, 6, 2]), relay.reshape(const_2222.astype('uint64'), [5, 6, 2]), )
call_2223 = func_2078_call(relay.reshape(const_2222.astype('uint64'), [5, 6, 2]), relay.reshape(const_2222.astype('uint64'), [5, 6, 2]), )
output = relay.Tuple([call_2219,call_2221,const_2222,])
output2 = relay.Tuple([call_2220,call_2223,const_2222,])
func_2229 = relay.Function([], output)
mod['func_2229'] = func_2229
mod = relay.transform.InferType()(mod)
mutated_mod['func_2229'] = func_2229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2229_call = mutated_mod.get_global_var('func_2229')
call_2230 = func_2229_call()
output = call_2230
func_2231 = relay.Function([], output)
mutated_mod['func_2231'] = func_2231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1340_call = mod.get_global_var('func_1340')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_2366 = relay.TupleGetItem(func_1340_call(), 1)
call_2367 = relay.TupleGetItem(func_1341_call(), 1)
func_1449_call = mod.get_global_var('func_1449')
func_1451_call = mutated_mod.get_global_var('func_1451')
call_2372 = relay.TupleGetItem(func_1449_call(), 1)
call_2373 = relay.TupleGetItem(func_1451_call(), 1)
func_2229_call = mod.get_global_var('func_2229')
func_2231_call = mutated_mod.get_global_var('func_2231')
call_2393 = relay.TupleGetItem(func_2229_call(), 0)
call_2394 = relay.TupleGetItem(func_2231_call(), 0)
output = relay.Tuple([call_2366,call_2372,call_2393,])
output2 = relay.Tuple([call_2367,call_2373,call_2394,])
func_2397 = relay.Function([], output)
mod['func_2397'] = func_2397
mod = relay.transform.InferType()(mod)
output = func_2397()
func_2398 = relay.Function([], output)
mutated_mod['func_2398'] = func_2398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_2443 = func_2025_call()
call_2444 = func_2025_call()
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_2450 = relay.TupleGetItem(func_1864_call(), 4)
call_2451 = relay.TupleGetItem(func_1865_call(), 4)
bop_2455 = relay.greater_equal(call_2443.astype('bool'), relay.reshape(call_2450.astype('bool'), relay.shape_of(call_2443))) # shape=(2, 9, 4)
bop_2458 = relay.greater_equal(call_2444.astype('bool'), relay.reshape(call_2451.astype('bool'), relay.shape_of(call_2444))) # shape=(2, 9, 4)
uop_2468 = relay.sqrt(call_2443.astype('float32')) # shape=(2, 9, 4)
uop_2470 = relay.sqrt(call_2444.astype('float32')) # shape=(2, 9, 4)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_2479 = relay.TupleGetItem(func_1120_call(), 0)
call_2480 = relay.TupleGetItem(func_1121_call(), 0)
output = relay.Tuple([bop_2455,uop_2468,call_2479,])
output2 = relay.Tuple([bop_2458,uop_2470,call_2480,])
func_2486 = relay.Function([], output)
mod['func_2486'] = func_2486
mod = relay.transform.InferType()(mod)
output = func_2486()
func_2487 = relay.Function([], output)
mutated_mod['func_2487'] = func_2487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1368_call = mod.get_global_var('func_1368')
func_1370_call = mutated_mod.get_global_var('func_1370')
call_2552 = func_1368_call()
call_2553 = func_1368_call()
uop_2558 = relay.sigmoid(call_2552.astype('float32')) # shape=(2, 9, 4)
uop_2560 = relay.sigmoid(call_2553.astype('float32')) # shape=(2, 9, 4)
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_2569 = func_2025_call()
call_2570 = func_2025_call()
uop_2574 = relay.asin(uop_2558.astype('float32')) # shape=(2, 9, 4)
uop_2576 = relay.asin(uop_2560.astype('float32')) # shape=(2, 9, 4)
output = relay.Tuple([call_2569,uop_2574,])
output2 = relay.Tuple([call_2570,uop_2576,])
func_2582 = relay.Function([], output)
mod['func_2582'] = func_2582
mod = relay.transform.InferType()(mod)
output = func_2582()
func_2583 = relay.Function([], output)
mutated_mod['func_2583'] = func_2583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_2691 = func_2025_call()
call_2692 = func_2025_call()
const_2698 = relay.const([[[-8.485701,9.686972,4.360242,-6.258250],[-1.477309,6.095762,-4.482321,2.924254],[4.671320,1.336594,6.631285,-2.104251],[-4.001045,8.034013,2.900078,-4.118708],[1.649675,-8.663217,8.865506,3.433428],[-4.883924,7.480056,2.666426,2.831051],[-9.552226,-9.126448,-1.726572,4.701588],[-5.924322,-4.228590,-9.563055,-2.760341],[-4.007057,-8.286552,2.705085,0.265583]],[[-8.213642,-8.298740,6.602272,-8.081885],[-7.482982,-6.966826,-8.088070,5.251972],[-3.906574,-7.318231,1.111879,1.818247],[-1.843809,6.067858,6.494409,7.232127],[7.229143,0.878388,3.323060,-8.247315],[-7.056152,1.151495,5.412548,8.766922],[-3.220102,-0.326596,-7.501569,-6.701516],[2.676721,-0.652782,-2.968117,0.480870],[1.181248,2.238053,-1.060991,-8.412741]]], dtype = "float32")#candidate|2698|(2, 9, 4)|const|float32
bop_2699 = relay.maximum(call_2691.astype('float32'), relay.reshape(const_2698.astype('float32'), relay.shape_of(call_2691))) # shape=(2, 9, 4)
bop_2702 = relay.maximum(call_2692.astype('float32'), relay.reshape(const_2698.astype('float32'), relay.shape_of(call_2692))) # shape=(2, 9, 4)
output = bop_2699
output2 = bop_2702
func_2710 = relay.Function([], output)
mod['func_2710'] = func_2710
mod = relay.transform.InferType()(mod)
output = func_2710()
func_2711 = relay.Function([], output)
mutated_mod['func_2711'] = func_2711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2397_call = mod.get_global_var('func_2397')
func_2398_call = mutated_mod.get_global_var('func_2398')
call_2803 = relay.TupleGetItem(func_2397_call(), 1)
call_2804 = relay.TupleGetItem(func_2398_call(), 1)
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_2810 = func_1184_call()
call_2811 = func_1184_call()
output = relay.Tuple([call_2803,call_2810,])
output2 = relay.Tuple([call_2804,call_2811,])
func_2815 = relay.Function([], output)
mod['func_2815'] = func_2815
mod = relay.transform.InferType()(mod)
output = func_2815()
func_2816 = relay.Function([], output)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2821 = relay.const([[[7.347457,-5.061020,-3.925679,-6.043954,-1.256001,-1.242371,0.190862,9.413412,-1.479140,7.777653,-3.550972,6.897504,2.115150,9.508934,-1.328044],[0.230977,0.998048,-2.150621,0.677352,1.426144,-0.469944,2.587120,6.666123,-6.547531,8.165779,9.597466,7.093930,9.132021,-7.750552,0.678348],[3.330441,-5.881425,-2.822025,-0.674581,8.536848,1.228025,0.587540,-4.078919,-3.711003,-5.338886,-8.870895,4.104438,5.410901,-7.593658,8.789343],[-9.708936,-1.510972,0.328450,7.542380,4.693653,2.292162,-1.970522,0.118137,-4.678409,1.610790,0.218706,-3.337788,1.091165,8.092957,4.028364],[-8.266659,-5.337708,7.651695,6.230836,4.345877,4.700292,-9.942192,-6.324043,-9.287985,4.362255,5.626183,-7.662408,9.261310,7.016500,6.954484],[4.467720,-7.238374,4.636071,-8.081705,-1.263184,3.664373,-6.404014,0.646648,4.971250,4.104855,5.310756,-8.195095,1.993261,-2.900166,-9.902140],[9.702123,8.931210,9.380208,1.710743,9.781052,-8.416494,-5.976704,-2.857592,0.450710,8.625113,-7.292542,3.613613,-0.960782,-9.247842,-2.134067],[5.319712,1.398207,3.739215,7.375008,-3.674105,5.114404,3.909682,6.637909,7.733396,5.099062,-1.672386,-5.686324,-5.971932,-5.035178,0.346715],[-1.853429,-5.142352,8.816530,-6.434237,7.011196,1.719234,7.827396,-1.115467,8.129152,6.782507,-8.619608,-6.463946,-8.972971,-6.258736,-3.323649],[5.328328,-7.241479,-6.128808,8.758537,-3.635616,5.756827,1.971086,-7.406398,2.465979,-3.994169,-1.858581,-0.319858,8.120193,-9.760668,0.439613],[1.180612,4.177941,4.611704,1.555879,-4.259987,7.860084,0.228506,3.362389,-8.946082,7.593217,1.897194,1.680989,2.621113,-0.687102,-4.501856],[-1.060837,-2.040889,8.586920,8.525316,3.009259,-2.293564,4.515711,4.409358,1.880378,6.269204,-1.383979,0.637812,3.389692,-0.019276,-9.519219],[9.800156,-2.057983,-0.700601,7.682886,-3.845967,7.446777,3.716383,0.420182,8.788220,-9.011035,0.288986,-0.138362,7.340659,7.965298,3.423413],[-3.359296,-8.017046,4.508521,9.641343,-8.091945,8.414728,-6.917872,-1.378992,8.253105,7.385195,0.992751,2.802439,9.461557,7.844026,-3.789833],[-0.323612,9.826200,-0.838623,0.090300,-0.153810,4.054052,3.523259,-3.127967,5.098200,-6.758643,-7.803413,-5.389412,7.434108,-1.612837,-5.128158]],[[5.559011,6.110203,-9.132056,7.365171,3.826063,6.351566,7.674393,1.788306,7.169808,-0.183664,2.748048,4.958063,-0.792963,3.412398,4.010071],[7.000581,-8.887832,0.004692,-3.686115,-7.592162,-4.996133,4.908789,-2.602064,-9.646747,1.829690,3.779925,3.932763,-1.642895,6.960342,-0.734535],[-5.073388,-1.005570,-6.479035,7.808065,-3.660781,1.176938,4.906167,4.604711,0.708680,7.442254,-6.397723,6.533096,2.179279,7.841731,7.237160],[7.094397,9.598461,-1.861336,-5.880853,2.799708,0.324883,8.622245,2.849651,-5.174339,-5.612982,6.821136,0.404776,-9.173127,1.530717,0.683922],[0.931045,-3.667258,-8.537594,7.597609,-1.437224,-2.909981,9.820483,-9.167611,-1.973205,6.368377,9.761836,8.096196,7.219922,8.351227,7.531306],[6.865353,-4.823900,1.912637,-2.369953,0.518188,3.946128,-4.073699,1.441864,8.614537,4.626850,5.753512,-4.658114,6.571381,-0.462616,-0.529364],[-1.767681,6.864654,0.114163,6.494011,7.945212,-9.982467,-1.680989,0.936936,6.712928,2.287630,9.731260,0.999980,5.012931,5.266326,-8.806560],[3.290045,8.344815,1.920494,-8.748938,-4.666427,7.943537,-9.703902,4.400142,4.851611,1.056828,9.470428,1.822295,-7.322388,-0.340473,6.430094],[1.566843,8.064375,7.384807,3.884344,8.880656,2.479178,-7.390746,7.712964,7.109711,-6.063595,2.707510,0.265809,6.563470,-7.090072,0.495964],[-5.671162,-0.275483,7.531965,-7.505453,3.669960,-2.370261,-9.864828,2.452913,-2.381516,-7.283607,3.236907,-9.257800,5.129965,-0.762344,6.149289],[2.673900,-1.209298,5.166068,2.535099,-9.641175,-6.144003,1.161590,9.012069,-9.935697,0.045866,-3.542189,-7.633897,1.312103,-3.080214,0.546885],[9.588099,5.699520,6.080136,5.361795,-9.538093,9.405259,-2.135706,3.101669,7.788114,1.023278,4.380608,1.674999,-9.633007,8.703266,-3.110653],[8.515965,1.724787,6.110887,8.387809,4.825026,-6.703013,-8.590859,8.616611,-9.295309,4.985691,7.056459,-4.119459,5.898856,6.865391,7.852157],[3.094726,1.941348,-6.338241,5.791847,8.316010,0.577738,-9.630902,-4.676818,-5.614208,-1.261621,-8.492493,-2.448577,1.565110,3.598980,-7.601210],[-9.043997,3.879986,-5.051171,4.804513,-8.873617,-1.694865,-0.537928,0.067644,-7.064401,-5.582452,-7.124681,-6.047258,0.469628,-5.091201,-8.518463]],[[3.024736,-1.017445,-7.972706,-5.273614,1.144939,-7.633684,4.781593,-7.629476,7.846209,-4.731160,4.353660,-3.238395,4.186070,0.466390,-5.961384],[-3.943601,3.683482,6.153668,3.942734,1.474768,-6.357091,-3.798761,-6.354465,-2.337062,1.885099,1.054524,2.475778,-4.995467,4.070495,-2.715319],[5.343408,-0.232971,-4.963625,-9.618607,7.116413,-3.025441,7.317662,5.593966,9.373411,6.589412,-2.961773,5.520172,-1.824344,-0.957114,-3.715517],[3.673923,4.425459,-2.997739,5.571569,2.190248,-8.857208,-9.046625,-0.677883,2.966790,-1.766263,-3.866270,-6.580768,-2.826586,3.944432,-8.745155],[-3.137855,5.010732,9.020341,8.707993,-1.481924,-7.019481,-3.672224,-9.565822,-5.170518,-3.926231,-0.929179,-9.011319,-4.477954,0.219469,2.574054],[1.350118,-1.408680,-5.540281,-3.180910,-3.699158,-5.230277,0.830418,-4.004106,-2.897903,-0.506573,3.699953,3.190132,8.067474,-8.047348,-5.882826],[-5.510858,8.284853,-0.572606,8.675800,1.504899,-4.006903,-2.637139,-7.709771,1.925574,8.887481,7.354674,3.657180,-7.348774,0.726418,9.726836],[6.330636,6.889907,-8.181378,-5.991348,6.128469,-7.078754,4.032548,8.344549,3.201780,-6.660023,-4.313064,7.870870,0.737218,-2.315946,-5.943214],[-0.191951,-9.596501,7.792449,6.493173,-7.495584,5.365058,-5.555687,7.080402,5.776445,6.383715,2.647466,7.265232,8.246755,9.203313,3.507579],[2.979544,0.397418,-3.888966,4.231220,-7.856380,-0.844383,-6.706426,-7.612009,-4.769141,-6.728016,-3.304271,-5.518944,-0.264427,-9.392606,3.571127],[7.578833,2.436241,-6.498255,6.350604,8.038294,5.189716,-0.741860,2.692466,7.828114,-7.459527,9.047055,-0.347159,-3.697492,6.994355,-8.806549],[4.186255,1.414345,-1.505150,-5.464335,7.186554,0.576319,9.048352,-5.502330,-8.181860,-0.563721,2.057637,2.162857,5.399849,-0.769557,-0.262425],[-4.649011,8.238113,-9.105357,7.596723,0.650862,4.212861,-5.141437,-0.741616,4.843513,-2.286735,8.712521,7.470850,6.870516,6.580400,5.646348],[-8.766143,3.371663,5.645214,1.539113,-7.011575,-2.744765,9.562142,-2.571320,7.189668,7.490085,0.638502,-7.956735,9.965904,-3.546673,3.407504],[2.374315,6.270706,4.338843,-9.576369,1.593394,-0.066120,-0.708622,-5.956436,0.450803,-3.939974,-8.129471,-9.699653,-2.057182,-4.504739,-2.567706]],[[-3.938361,-1.478378,-3.328542,1.468535,-0.599804,6.098336,-7.834824,2.453260,-7.214035,-5.063942,5.064379,-0.513621,1.230048,0.179895,0.810594],[-6.744589,0.707755,0.230163,-8.986910,6.196500,-0.711690,1.806298,-5.630080,6.887567,-8.954777,-3.123430,-5.959220,3.578420,5.167997,-8.258073],[-5.590452,5.671002,8.859243,3.514226,0.249287,-5.724762,4.196834,-0.472935,-6.888024,-9.862106,3.183095,-4.039429,5.686305,-8.333812,9.687628],[-8.021133,3.103005,1.292847,-8.701222,-0.971410,0.137499,0.809670,9.036291,8.191571,-5.763349,-8.177627,-9.255208,7.309757,-8.462713,-0.831765],[-1.385377,9.777012,-3.774233,-7.097374,6.386449,-0.876120,-2.272731,7.305505,7.956171,4.987424,-7.219760,-7.664782,9.199899,-1.770003,4.264318],[7.573821,8.511153,1.627771,4.758667,6.487889,-3.527478,-2.120161,4.537436,-1.840378,-4.529981,-0.380264,5.686177,9.127724,2.441185,-4.284646],[-6.234378,-4.789355,-0.537691,-7.888835,-0.767752,-2.481744,9.847209,7.337700,-2.102721,-5.590715,9.780924,7.238977,9.565893,5.297173,8.031552],[7.448638,2.745572,0.818545,2.462356,-0.815110,3.509886,-5.877673,9.051645,-5.365383,-3.100617,-5.260572,1.443127,-6.507370,-5.929554,0.491755],[-2.352833,5.449290,8.520766,5.564772,-2.241663,-6.251619,5.920186,1.863674,-3.619122,-5.288070,-9.663874,-3.250444,2.160073,-4.934381,5.109617],[5.183073,-7.076751,9.047041,9.606149,-6.099436,-4.947718,-0.555097,2.567364,-7.461534,3.573233,-7.200905,2.570085,3.215586,-8.747038,-0.201802],[-3.082125,3.863604,3.420659,-7.403655,2.787927,-8.808455,2.773158,4.415265,-7.591431,-4.291656,2.302045,1.671316,0.532977,4.814449,-7.030005],[3.957646,6.296422,3.759239,-8.463179,5.410914,-9.942246,3.933248,-7.903545,7.259979,8.115658,-6.930453,-5.540021,3.859945,0.427137,4.455055],[2.462815,-5.315728,6.538317,7.917961,9.830154,-6.661382,-6.092500,3.631716,-4.530534,-9.657206,-7.674001,-3.538915,-7.027838,-7.014707,-8.281464],[-6.812481,9.014214,-1.459580,-8.424979,-3.887770,0.864829,-1.121889,-5.039139,-9.283577,-2.946570,-8.409393,-7.110569,1.812809,8.417573,-2.223874],[-5.059031,7.701245,8.724664,-0.880984,6.060841,9.964097,6.436836,-4.714167,5.508269,7.051308,8.348891,-2.231421,-9.160497,3.672307,8.430871]],[[-9.288352,-0.638943,4.086081,7.776591,6.421667,-1.562907,2.408137,-9.839896,-7.243460,6.376317,7.242659,3.084092,-0.011677,-2.961593,8.337956],[1.666019,6.411995,3.973016,7.357170,-2.182030,3.248362,7.625364,3.299031,6.332270,5.450073,2.730394,5.281975,-4.702841,-5.870519,2.043302],[-7.876015,9.295420,-4.864450,7.129919,-3.135557,4.632251,-9.182945,-8.402611,-6.792064,4.622882,-6.007417,2.455903,-8.910793,8.269520,-3.695343],[-5.273129,2.648957,-6.871987,6.487331,8.376475,9.826309,2.013844,8.239996,1.124909,3.777081,8.391698,4.199607,-1.359375,-7.576855,5.227900],[-9.774570,-9.521653,7.081194,-6.049800,-9.548725,-2.650240,-5.695683,1.081657,-2.121880,1.215620,-7.697017,6.742297,8.979389,1.023623,-4.713294],[-3.220282,-7.944982,-6.492964,0.995170,-4.867687,9.967308,-4.950748,7.305918,9.594706,-6.759894,5.139639,-6.457985,8.004740,-4.019386,5.956351],[1.925840,-9.503570,-2.613431,2.625329,5.791057,0.749427,0.035111,-2.570146,-3.879171,-8.107527,-0.239236,3.489594,-0.569560,0.104360,1.416368],[4.931680,-1.932381,-1.487211,3.699474,8.502562,-2.186821,7.885530,-6.111241,-0.565877,7.826264,7.665632,-4.490691,-4.589705,8.243505,-9.578223],[9.496247,3.330922,1.607670,-1.884258,-5.755606,0.742619,1.834956,-2.109116,-3.099509,-9.457097,7.445599,6.978352,-3.025040,-9.435837,2.371332],[-3.126519,4.341903,0.715850,8.932380,6.691322,7.437660,-1.011393,8.423054,-0.974031,3.713760,2.033936,-1.334320,9.809069,9.966717,2.942013],[-5.073704,0.727338,8.982291,-7.093835,-7.266488,-8.961148,-5.317859,-5.658227,3.981621,4.061855,9.193559,5.508768,4.075686,-0.075108,0.599583],[-5.280216,3.839689,5.854833,-4.753498,-4.645470,4.838828,-9.775035,8.981377,0.194358,8.676739,-9.720692,4.988817,-0.907189,-7.325018,9.308048],[-0.316307,0.170282,1.002843,5.667248,-9.465724,3.483719,-9.744229,1.916125,-7.279599,0.327974,9.533348,0.481467,1.277964,7.609363,-1.438423],[2.757394,-8.683607,6.909263,8.283372,3.737012,-2.940680,2.915778,-7.702108,-3.978753,7.507487,-1.215763,1.818244,-0.248754,-1.817933,-2.875306],[-4.757491,8.334725,-2.339772,1.063036,5.643289,2.311765,1.009109,8.300389,2.485336,-8.561243,7.687979,9.052257,-1.714092,7.639199,-2.734715]],[[-8.697322,-9.266232,0.727046,-3.915108,-1.784502,-1.195682,9.303366,0.848898,2.809289,-2.691367,2.131743,1.566686,4.702058,-0.017560,-9.029585],[-2.324059,-3.554640,-7.395737,-1.758720,-7.350856,1.168718,-1.889067,-3.604526,3.092155,4.922182,4.414137,7.426659,0.553064,5.503003,3.638286],[-9.167657,-4.937889,-4.400252,6.278848,9.143648,-8.223860,-7.017536,0.169977,-2.862903,-9.889873,-9.736198,-4.927660,-1.727388,-1.607203,-6.118616],[0.939663,-5.837825,7.454238,1.539390,0.088984,-0.520706,1.755656,-0.963930,3.171956,7.732256,-3.642616,4.834975,7.819385,8.397029,7.548073],[7.826834,-3.540188,-1.887556,9.068851,-2.804896,-2.767560,-7.437532,4.313590,-0.415459,1.704726,5.408979,-2.688794,-2.778778,-1.727397,9.863289],[0.759264,6.780645,-6.556675,2.108972,8.172154,-5.036474,-3.046155,1.050947,-3.777700,-3.128516,8.170098,5.105978,9.092895,8.905968,1.592125],[0.291549,3.921596,7.557187,3.160540,2.859019,-1.893544,-1.239835,-5.499278,4.309936,-7.656767,-2.398816,2.495868,7.728808,-0.738199,-2.104725],[0.399690,-7.238364,-8.331254,1.702662,6.137193,-5.139225,-6.159289,-6.721346,-2.018609,2.651376,-4.275646,-6.559501,-9.725152,-5.542399,-0.311440],[-4.661735,-1.981661,5.588458,-7.761467,-8.003431,5.960427,-6.315590,-1.044836,2.058155,-7.579555,1.219737,-9.340978,-4.351443,4.093224,8.943463],[3.459413,5.220705,2.801291,4.417189,7.396752,1.799453,-1.044119,1.766738,-0.646498,-0.779789,9.754941,9.356473,1.737221,-2.800724,-2.391592],[6.859167,-7.594545,-7.112021,7.062935,4.810109,8.417284,4.690194,-1.208531,-7.678689,6.323429,2.044132,-7.904616,7.086658,-7.553830,-4.957031],[8.851227,7.235721,2.725734,2.945794,1.285202,7.697852,6.315649,-2.294455,2.776178,6.970481,7.945724,-1.755078,2.253906,-1.544359,6.910600],[1.812186,-3.944805,-4.091908,-0.539291,-9.457359,2.099966,-0.284484,-1.673976,-0.644157,-5.053645,1.182934,2.595106,9.262625,5.330899,-8.814940],[2.369959,9.925427,-0.068719,9.486769,-9.976554,-9.996940,7.754017,-4.092373,-3.543511,-9.281585,-9.609835,-4.509872,1.240661,6.776031,6.780838],[5.712063,2.370597,-8.549578,3.118936,-6.464183,6.313538,6.699968,3.657030,7.974038,-0.663516,-3.515102,3.771383,-1.475929,3.258559,0.887761]],[[-5.602469,4.886361,4.565246,9.056543,2.811130,-5.778464,5.589061,8.157733,-3.946233,-2.703191,-4.473227,7.229054,6.989841,-4.511910,8.909444],[-7.771622,3.505530,0.057701,6.961483,1.782983,-9.438983,-2.741110,5.078006,7.541936,-6.567548,-6.046382,-0.692752,-7.908727,-5.319983,-8.571581],[-9.851315,6.102623,-7.193533,-9.139769,8.627467,-1.900258,-1.780640,2.697677,1.955429,0.616709,-3.071916,-4.932057,3.929428,1.339162,-7.442039],[-6.894127,-1.217171,-3.209949,-4.745211,-3.757750,-0.455903,-6.212228,7.647232,-7.365655,-8.918717,-9.100692,0.992406,9.519767,0.418969,-8.053722],[2.416807,-8.473057,-4.323920,-7.372727,-9.317719,1.545493,-5.761456,4.874545,2.739761,-5.163722,1.802050,1.783802,2.697173,7.859128,9.185424],[-3.173858,-2.677773,-0.086345,1.618376,-5.759143,1.845395,-4.767032,3.614836,-9.428383,5.882463,-9.097256,0.720714,-9.405730,-7.102740,-3.468353],[8.955152,-0.399840,8.259619,9.590101,-0.070809,-6.536599,0.730239,3.859884,-0.508966,3.042490,-8.987699,-8.854784,6.123612,-8.272573,0.045175],[3.949855,-2.754876,-3.726497,-5.894761,-6.151457,7.559282,7.085938,-0.207047,3.925654,-0.442318,-1.524770,-3.570763,-0.677807,8.746728,-5.494175],[9.668005,-0.180684,0.530191,-2.121293,-9.304977,-5.118716,3.550117,-4.376371,-0.823027,6.292239,-6.714774,4.373782,-0.621809,3.254504,2.475670],[-2.594094,5.845142,-8.185262,-6.819910,8.842870,5.798787,-4.422441,8.294500,-3.360377,7.476926,-6.218999,-7.031442,-2.463885,0.723103,-6.355448],[0.512063,-0.637462,1.228610,-9.527037,6.616046,-2.418457,0.770851,0.003698,0.846920,4.165135,0.958599,6.640698,3.172672,4.506624,5.841455],[7.261588,-9.889105,1.131383,-9.752655,9.073128,3.209223,6.094856,0.117603,0.565403,-3.993119,5.253068,-1.165652,6.606892,-6.312489,3.572855],[9.820818,6.070797,-8.161389,2.982857,-6.883881,-7.035179,7.033549,-7.441247,-5.331711,5.776594,-7.246973,3.722166,3.451703,0.477801,6.514581],[7.615634,3.488568,-4.876829,-9.945890,5.412051,2.119293,-1.708440,8.672734,2.627324,6.840479,-6.452903,3.695485,-6.992217,8.328735,-4.748102],[-0.339412,8.470727,-9.020831,8.024428,4.170088,2.719128,-5.615692,1.326153,1.574686,-2.870244,-1.648575,-9.022834,-2.200184,-9.370040,-4.458528]],[[-2.722728,3.257555,8.533900,9.967344,-7.715389,5.825578,2.401121,4.447861,8.571750,1.272371,5.572979,-0.974334,1.372415,2.542459,-7.358395],[1.823222,-2.654175,-1.329007,-6.052386,7.182679,0.677178,0.752781,-3.044484,0.612331,8.903959,6.914559,-3.635130,-7.530929,-5.408379,-3.038656],[-7.523891,4.339175,-5.633487,-3.365220,-8.344716,5.381077,-8.263267,-4.695503,6.969703,-0.213997,4.093205,-2.334855,3.193860,1.339033,-2.758113],[5.451532,0.552892,9.425249,-6.834925,4.917814,3.655797,-0.392058,6.227614,7.802093,0.094163,1.539015,5.900480,-2.519427,-6.892347,4.861698],[9.306268,4.642655,4.220214,-3.039563,-3.100828,-9.653244,-6.517864,2.187430,-7.055951,7.582631,-6.379758,-8.850946,-6.989147,7.948337,-2.925354],[1.770738,8.487009,9.007688,4.333708,-2.620367,6.662980,-6.429296,-5.801012,3.351757,-3.189191,-6.415102,1.485272,-7.702004,5.795861,-6.411987],[-1.203651,-5.122922,5.846307,9.495274,1.133856,-9.441201,-5.490813,7.659503,6.640189,6.250032,6.439606,-9.170408,-5.825418,-9.920947,-4.080117],[-7.125140,-3.413898,-8.805883,-2.664573,-0.109922,-8.194127,-7.586493,9.318147,7.293959,-4.476049,-5.425924,-8.892095,-8.943013,-3.369481,-8.177362],[1.795195,8.765869,9.848729,3.960500,3.924376,-0.587124,0.810987,3.244872,-4.819018,5.104627,0.578622,-5.768410,-5.871862,5.593921,5.981525],[-2.026477,-1.622533,-1.250897,0.732851,0.639668,1.929283,-3.662054,-7.656777,-2.927536,-9.708004,2.736177,4.994297,3.398189,-8.865510,-8.306682],[0.524961,-1.091136,7.208980,8.162530,5.805298,8.578604,-5.613437,8.513469,8.794247,9.455593,6.011273,-1.515957,-9.862499,-7.891286,-1.687408],[-4.208353,0.862194,8.328729,6.946141,-9.825661,9.704921,-3.119619,9.899168,-9.865106,0.647051,2.836658,-8.563568,5.827722,7.290595,0.788244],[3.990649,3.897444,-2.904173,5.510117,-7.060339,-7.525998,5.092559,4.344745,-8.956425,-8.881412,-5.509117,-2.289958,2.028090,6.763726,-2.974256],[-0.098901,0.070175,-6.777154,-3.263905,4.476848,9.359564,-1.062534,-9.780165,-2.333597,1.386578,-9.973332,-4.103650,-2.051007,2.287062,-9.871634],[-7.287747,6.546036,6.062494,3.668236,6.109461,-5.645415,6.384596,0.283867,-8.202814,-3.117377,-7.470594,8.097831,-5.585019,-3.388888,-5.595427]],[[8.956993,2.203630,-6.344610,-6.792263,-5.342603,-9.024010,1.727674,5.134263,-2.090485,-9.275462,1.238800,8.605005,5.748555,-2.794560,2.517809],[-8.170327,6.740388,7.272455,-4.506416,-2.617018,8.512331,7.092003,-4.043519,-9.442847,7.851800,9.423627,2.933877,8.881012,-6.551658,7.830487],[-6.392963,-4.804565,6.573975,2.406409,-6.600413,1.750597,2.710435,-8.666709,0.050622,-2.324213,8.801549,-4.226788,-6.088783,6.600175,7.386936],[6.287577,-6.260103,-4.605762,9.706390,-0.497337,6.120116,-4.559167,-8.001394,-9.658204,0.315674,-5.236310,-4.864342,3.716948,1.027004,-9.324170],[4.858665,-5.476129,4.180797,-5.831831,0.280091,-2.164062,-7.738195,7.668373,5.879814,-5.948597,-3.608199,1.172190,6.275229,9.680270,7.445917],[-4.598489,3.104200,2.926628,4.644397,-4.598843,-2.491402,1.256992,1.704048,6.846633,-5.578008,3.340703,2.038204,0.574300,4.590393,3.153229],[-4.484904,-5.549106,-4.567030,6.512172,8.754473,-7.482585,-8.752831,-3.134020,-9.044226,3.070559,1.298937,0.380609,3.187956,-6.064174,-3.837590],[-3.300600,0.396137,-1.221003,-7.128876,5.131717,3.533990,1.966903,1.918442,6.658045,5.703614,-8.321732,7.116485,6.107325,-4.936745,-1.669924],[0.321466,-0.376050,4.198943,9.324622,-4.910594,4.364483,-6.758878,0.204348,-0.694943,-6.624495,7.696869,-4.385103,-0.071999,-2.517117,6.970128],[4.200362,5.808333,1.615688,4.829750,-0.373370,1.111616,4.928889,-9.451801,2.756418,-7.759369,-8.696409,-0.850053,-7.995882,8.245173,-2.840403],[3.693507,5.412694,3.442968,5.413720,7.593771,-2.855864,8.715349,8.850828,-3.002037,-7.898053,-7.093240,1.297006,-2.642295,7.090444,-1.649182],[-4.159458,-7.166372,-9.190518,6.660592,-1.532136,6.807950,7.635045,-1.903372,-2.637134,-3.084248,3.503105,2.296187,4.353267,6.443495,6.069059],[-0.986554,7.889684,-7.610148,-0.434185,-9.682706,-5.224479,7.747942,-9.898279,-9.701563,2.384018,-8.129224,6.122749,3.622318,6.683316,-9.997691],[-2.251321,-5.566514,4.076379,8.269209,-6.163323,-7.162684,8.684133,6.858153,0.534496,-3.331846,-2.999775,-1.908139,-7.168544,-8.421798,-5.021225],[0.122662,-2.205118,-8.785233,-9.301533,6.396073,6.206927,6.449212,-7.343313,6.561618,0.759971,-3.278808,-3.268227,1.274829,-9.303972,-9.750360]],[[-5.424764,8.670534,2.275405,-4.443892,4.092940,0.413183,6.464228,9.942526,4.608722,-1.109034,-2.870036,-9.663536,0.539170,8.109084,7.167055],[-2.376917,0.270615,-9.010292,9.514273,-8.955306,5.307150,-5.891552,5.214654,-8.867518,-6.196077,4.797617,0.264658,9.929990,5.394037,-6.249647],[-1.071395,4.930935,-9.066317,-4.621501,-6.554109,-6.057882,-0.285218,2.718885,-4.441103,-0.609334,-0.616744,1.828841,2.124184,-3.264587,6.643285],[-1.986897,2.742602,-5.521945,1.624885,4.981669,8.276400,0.255972,-0.569393,8.214202,-1.392104,0.393842,6.296047,-2.884775,5.316164,-9.425131],[3.154779,-7.538026,-9.918513,-4.409264,-5.025350,4.834596,3.188095,3.964358,4.321691,-5.635161,2.575032,-9.218026,-4.595861,5.527253,0.690194],[5.526566,-5.690928,0.651863,-3.088401,8.910404,-9.891706,-8.730576,1.344485,5.509554,7.897255,1.818870,-9.810919,4.324241,-7.791570,-7.325214],[-9.800285,2.918883,-8.578007,4.874959,-5.619700,9.888511,-1.196698,0.716375,8.355746,-0.355344,-4.327190,1.282625,-8.918147,-7.386669,-5.285564],[-0.887689,-1.475448,9.048869,7.096180,5.250429,5.359591,-5.708398,-7.318883,-2.262275,-3.517250,-8.843037,-1.016953,0.850540,7.935599,7.249912],[2.496461,-5.443965,1.859982,-2.232938,9.798875,7.244504,-5.043305,-5.275276,3.670169,-3.579387,4.344931,-7.342116,6.022979,-7.331811,5.699302],[-0.395716,-1.101438,-9.574311,-6.928870,-2.302478,-7.370054,4.225871,2.029296,-0.849128,-6.107521,-9.247405,1.761844,7.164879,9.431076,8.539885],[6.589210,0.442296,6.432836,-2.671775,-1.839765,1.457888,-8.518344,4.618435,-8.538368,-1.078954,-1.149451,-6.383382,9.146097,-0.134556,-7.691150],[-2.233593,9.246995,8.710437,4.294944,1.270802,-6.446960,6.754380,6.663726,-7.531635,-3.227161,-1.727447,6.756956,-1.439043,-8.392831,2.363521],[3.268906,-5.930250,4.403219,8.414715,0.329946,-9.606109,0.964495,-1.275054,-0.448435,-2.907940,5.397128,-4.215527,4.090111,-2.045823,9.620480],[-9.528749,2.982752,-5.981028,-8.631039,8.150025,-3.463727,7.771890,6.248100,-1.123872,-1.542931,-7.325530,2.426890,5.002882,-4.117432,-1.022705],[9.554981,-6.764309,3.967144,-9.739867,-1.390363,-4.088881,5.829884,-0.489412,7.983529,7.226857,1.544618,-3.966010,-9.930237,2.603200,2.215378]],[[-5.843425,8.763720,5.694221,8.390104,-1.973174,8.340888,-7.509286,5.418201,-3.138889,0.572966,-8.650786,5.135158,9.123593,-7.107172,-6.784180],[-1.502677,3.661460,2.171176,5.137250,-4.657965,-5.183084,-0.880724,-1.605206,7.099201,-8.020523,-4.960317,7.295517,1.452078,8.462704,-9.107946],[8.230702,2.977209,-8.015694,9.891152,5.537928,6.833580,-6.990349,9.946961,4.229039,9.462599,2.151645,5.947754,3.078590,-4.001122,-8.538084],[4.571386,0.531410,-0.986952,0.689144,8.660442,3.090860,5.780516,-9.041219,3.937009,5.516160,-2.018817,-6.010217,-5.037820,-5.820202,8.069855],[5.828522,6.728659,1.764017,-4.231130,8.442414,1.701684,-8.283445,-8.013380,5.314575,7.309018,-7.439440,-2.233066,8.104998,3.402812,5.749629],[-7.577943,7.903773,4.155409,-8.814415,2.581205,-9.442105,-9.003205,2.298313,4.471640,-3.534279,-0.359345,-0.047252,-9.437202,3.267294,-2.110202],[-6.166972,4.557963,-2.346590,-9.338566,-8.694677,-4.827496,-9.629477,9.768934,-2.094917,1.891454,1.757458,9.016077,-3.388302,1.087134,5.421816],[-4.149192,0.624893,0.034794,-9.209452,-6.568502,-7.845854,7.700241,5.245330,-8.240777,-5.355269,6.496240,2.837416,9.624395,-3.991877,8.228070],[-3.649634,7.427156,9.399438,8.884544,-7.324319,-1.731384,0.372911,5.382100,0.314940,-5.482466,3.520322,9.980350,-9.018341,-8.790016,-2.127144],[0.826557,6.867069,-1.861307,9.556223,6.254465,3.990383,-7.394278,4.171881,9.142570,-8.558059,-1.957567,7.164845,-0.262867,6.607825,-5.879544],[0.289135,-8.167269,-4.046337,6.841574,4.822452,0.052215,2.514920,4.317446,-5.077824,0.572595,-1.227955,-6.686353,8.823623,5.493964,-9.155421],[-2.838322,8.762269,-6.695215,0.491823,-5.523300,-9.704020,6.314116,4.467987,9.982715,-7.614811,-2.924377,-7.807721,-4.088422,-2.687963,-0.546454],[-3.326117,-4.960160,-3.226548,1.486723,-2.898548,-8.235883,-9.496653,-2.408361,-2.712982,1.182144,-5.883100,8.898555,-1.558819,8.267288,8.255015],[4.642874,-1.574695,-9.410398,6.205256,3.022053,9.678105,-8.115833,9.636258,3.915363,-6.145142,-8.997904,3.105412,-9.459094,-6.582635,-1.290949],[1.519339,4.168460,0.455371,-6.010621,9.647684,-6.839813,8.915755,-9.349445,-4.799988,-5.180995,-0.011942,0.338768,-9.680812,-0.322721,8.083997]]], dtype = "float64")#candidate|2821|(11, 15, 15)|const|float64
const_2822 = relay.const([[[-5.825868,4.157211,-1.362860,-9.987580,4.535223,-3.827860,-5.725912,9.487791,-2.155090,7.787717,9.510777,-1.318938,-1.228311,-3.030029,2.375799],[5.079533,-0.487620,6.264788,-8.855582,-9.238833,7.052183,1.003170,-3.423240,-9.067677,-2.910227,3.197942,-1.437810,-2.374563,-9.758135,2.439686],[-1.252934,-0.278003,5.059994,7.623005,7.709135,9.260524,-8.008878,-0.409031,0.595499,0.049667,3.020019,4.766335,7.366698,-0.475701,-2.911687],[9.291647,-4.489911,5.623152,-9.396117,-3.854448,9.652032,-9.212754,-5.953460,-5.676232,4.864651,5.320455,-7.300210,-3.979849,-4.142111,-5.480144],[-0.130869,4.441910,1.783552,-0.065942,6.746178,1.698503,-8.701515,-1.623337,6.593384,2.804509,3.983211,0.896972,6.226616,7.206227,-1.886217],[8.997210,4.447817,-9.666401,8.536004,-6.161315,5.419413,0.315023,1.306777,-1.037820,-7.282571,9.688895,-9.784042,-9.712699,5.267191,-7.047056],[1.405611,-2.101363,-9.029723,7.308604,-5.403112,2.466236,1.822168,6.366560,-3.320703,0.350078,6.300337,-8.601251,0.275410,-6.101172,-3.386170],[9.977837,-9.386526,3.806223,-3.008587,-9.931846,-3.298629,-3.971467,3.459395,6.943622,0.233651,-8.923538,5.080334,-8.817687,9.286942,0.329279],[0.632944,0.238799,1.204142,1.837962,2.033464,-7.191861,5.470309,-5.828394,-3.925521,-3.811942,-2.391958,9.323042,-5.665044,9.330705,-4.092062],[8.391097,6.109654,0.465101,4.573600,-4.721477,-9.325393,1.375227,7.134182,-7.411155,2.379002,5.771988,-5.376285,1.790138,-1.805710,-8.473908],[-0.503189,1.195407,0.736010,-7.403878,3.547837,1.747983,2.244483,5.211590,-8.137254,-0.123244,-8.907311,-5.894691,-6.371627,6.878294,-6.590784],[3.244903,-3.525400,-6.935667,9.564062,-2.415619,0.733544,0.626341,-9.670965,7.613228,-3.957963,-3.276178,5.397263,5.131678,2.918347,-1.070058],[3.004491,-2.907272,-2.746472,4.485673,0.614178,-2.899274,0.501815,6.953483,-0.079622,4.356418,-3.065681,-6.159538,-9.319019,-2.480889,-7.662548],[2.903560,-6.369549,8.504767,-8.447973,7.749606,0.777454,-0.573331,7.283338,-5.530785,-3.719508,-2.748196,-5.556421,-7.484021,9.592559,-1.408009],[2.787064,6.652949,9.381420,9.812520,6.212921,4.166671,-5.844591,7.216436,9.393271,-0.745034,2.122035,-3.196297,0.799700,-0.093796,9.497840]],[[-3.418743,-5.387777,4.876355,5.221136,8.497490,3.468586,3.265968,-6.189086,7.903515,-6.607424,5.435860,-1.347840,1.158094,-0.764766,-6.495153],[-9.515525,1.462985,-5.193220,-5.202427,4.296776,-2.317077,-1.276819,-8.175314,7.267424,-6.091491,6.372801,7.426221,-4.851057,5.172553,9.290939],[-3.059686,0.581737,-8.308658,-6.598968,2.497502,1.396671,-0.009139,9.863183,-2.219252,-3.777573,-3.687486,8.132080,-3.930700,8.792159,-0.011731],[5.381515,-1.802843,-1.272633,5.748006,-7.623026,-6.113517,-6.477697,0.653810,-8.291180,-4.842514,1.423970,-0.174867,8.354523,-0.994089,1.582367],[6.789415,9.496116,7.034938,-9.216688,0.846302,4.919315,-1.051500,-1.979603,8.414529,-4.976506,-0.609144,-0.564108,-6.986311,6.987113,-0.667484],[5.645932,4.820567,-2.845915,7.808355,2.966044,5.385489,-7.431367,8.179021,1.422143,4.999653,-1.060676,5.794972,3.744825,-8.594596,-9.864350],[4.794948,-3.098687,9.703529,1.039442,-2.462127,6.362038,6.154336,6.341554,-1.945972,5.451914,-7.282244,6.673043,-7.852855,9.250253,0.278291],[-7.306529,-0.401817,-9.733577,9.106213,-6.422429,-2.288270,2.782305,5.767427,-4.009060,7.097033,-3.706303,-3.270188,-3.648848,-3.742132,5.354726],[3.671415,-8.825225,8.665703,9.962218,-1.877530,-6.632820,1.719271,-1.107765,-6.107066,3.726989,-7.432053,-6.959715,9.693341,9.951634,-2.640377],[-0.007065,-1.066515,0.511149,0.733319,-9.255912,-4.137772,-4.175226,-8.919504,6.899487,-9.528547,9.988012,-7.936673,2.646753,-4.305982,5.030348],[3.470514,-6.375182,-5.904579,5.949591,6.348814,9.340021,-4.078579,4.012857,-9.197186,-8.409855,6.526949,5.058925,5.354662,-2.012523,3.583305],[-6.957606,4.971702,0.782121,2.941689,0.120617,-8.181159,-9.080276,-0.813951,-3.800627,-8.118153,9.583296,-6.752332,0.769991,7.034152,7.443011],[6.000930,-2.096972,-4.087923,-2.921659,-0.707744,-1.137283,-3.568734,-1.133769,2.267358,2.147090,6.971271,2.485359,0.375616,0.308899,-1.944161],[-9.585160,-3.178114,-2.851498,-1.329442,-3.002518,-4.955652,8.898961,-5.085193,-7.332913,-3.499742,5.078282,-5.572906,8.171299,-1.995745,7.362747],[3.708565,-2.785862,-6.986482,5.805058,-7.544641,0.362041,-6.101896,2.112586,-9.544451,-8.069669,-5.817441,-1.925577,2.539500,-3.543883,-5.473340]],[[-8.012927,3.907223,-1.371571,-4.612048,-1.735461,3.072489,4.333382,3.785039,-2.069479,-8.160014,-6.101550,0.605244,-8.250827,9.470583,-0.260243],[-6.406861,8.119201,3.073349,9.480823,2.177812,-3.479724,4.647674,8.222290,3.197745,9.366792,-5.215223,-0.129821,-2.765889,-3.417757,3.703512],[-1.287414,-2.768621,-9.607979,9.213145,0.318816,2.883226,3.470754,8.708933,3.682892,6.859709,9.437633,0.493624,4.069520,-5.564067,7.689743],[-2.145231,4.914353,3.210875,-0.295538,5.264156,-1.784552,-8.104225,4.068753,-0.106959,-6.873650,5.924743,4.711976,7.712872,7.210622,2.202969],[9.201210,-6.693184,-6.617824,-5.571899,-6.936457,-8.361078,4.791244,-0.915979,-8.878414,2.956390,-2.627902,-9.479625,3.644391,-2.058122,1.047050],[9.274658,3.174380,2.887095,-0.496368,7.866583,8.182532,6.295504,-9.767919,-2.005223,-2.883458,4.929326,-5.757760,-7.860394,1.933591,-0.901690],[-4.362354,5.162627,4.366216,5.896649,4.034505,-2.466824,-9.831345,9.552216,-6.235880,-0.760252,2.792983,3.161164,3.578326,-5.971312,5.095943],[-0.796445,-6.984278,9.825589,-1.349564,6.120338,6.178048,2.619865,8.282915,-6.499765,-6.040103,-0.930649,-6.185952,8.431428,-0.368429,-0.981119],[4.972757,8.710923,1.450045,1.402244,-8.299122,0.747789,1.121269,2.233283,9.410264,-7.144524,-5.103361,7.756688,-8.142024,1.392469,-6.451243],[-7.143567,-4.929885,-7.889368,6.750201,2.159474,-5.167845,7.002563,3.172103,1.435335,7.296705,-1.466043,-2.843325,-3.789193,5.386241,0.253647],[-1.991666,1.430083,-7.534556,-0.781934,2.216531,0.998174,-1.296994,9.152215,8.699243,-5.544879,-6.626145,0.123801,-3.720058,-0.423721,6.337805],[-4.876172,2.660865,-7.774007,3.871896,0.273955,-9.616286,-5.348003,-1.529768,4.752468,-1.645606,-8.782883,-5.653641,-7.045657,0.041010,-6.457121],[-8.869605,-2.668553,-5.614451,2.952133,7.468234,2.562501,4.749942,-9.425429,4.903147,-4.344917,2.428629,3.985463,-8.233495,4.634164,-0.427619],[-9.984430,-8.190787,-4.390085,7.145477,-9.894913,9.002234,-9.911895,9.022846,-0.208287,-1.204429,1.661253,9.766902,-4.751685,-1.716095,8.916904],[4.661467,3.704463,9.446646,1.544822,-8.926892,4.682546,8.962534,-1.595718,5.389586,3.765705,5.536924,8.925876,1.672312,-3.116665,2.497263]],[[-1.527112,3.290587,-6.924208,-6.125851,3.154473,5.517744,-8.347871,4.466652,-7.893243,1.095736,-4.452660,-1.433407,1.039293,3.751491,2.652424],[7.424190,-1.896648,3.478641,1.004848,-7.536657,-1.705295,-9.397817,-6.950507,-9.792840,-6.680273,-6.851805,-8.146653,-5.961747,5.233725,-2.216256],[8.870951,-9.188647,-9.444737,-3.865281,1.512341,3.838122,4.998323,-0.425399,3.822792,-2.385524,-7.648058,-0.694750,0.807605,-2.151141,9.547272],[2.948928,5.260764,-8.244244,8.184401,9.125935,1.479670,3.168855,-6.461942,-2.440902,-8.549770,5.677711,6.727128,0.269790,8.951701,9.282157],[-9.469726,3.610242,5.436301,-7.504245,-0.038363,3.897815,-4.816598,-1.133255,4.411745,-1.843727,7.151192,-1.314611,1.177451,8.823758,-1.111889],[8.638919,5.443391,-2.535114,-6.683916,-9.515538,-8.715733,-0.012307,-4.100813,-2.744923,3.905477,7.443505,-8.804045,-0.104839,0.869514,-2.607243],[-9.815280,6.515645,-2.345478,-2.021686,-0.119188,-9.521408,4.920607,2.462199,5.261874,3.417892,-7.851722,-0.139459,-8.061147,-5.601383,-6.629162],[8.622662,1.157648,6.176114,-0.140936,-4.467525,-5.085218,-6.589918,-0.659330,9.070714,9.835576,-4.457222,1.244928,-1.341172,6.590382,6.706979],[-6.967288,8.484246,4.636343,4.795118,-3.016304,-7.884310,-4.831142,-6.986182,-9.109652,2.933616,-5.546839,0.087140,-8.163248,-7.425814,0.807397],[6.395212,-5.832203,1.147704,3.078352,-7.726353,-8.435482,-5.261862,1.504519,4.358357,-7.208323,2.468488,5.622390,-1.344507,-9.349157,6.455116],[8.208379,6.576077,3.531177,4.283873,-1.688572,6.071487,3.574016,4.652035,-6.574849,-9.830238,4.207228,-9.542473,2.270968,-0.699507,4.208493],[1.742711,5.742148,-7.387113,3.161052,9.886728,7.499520,-9.522867,5.349571,9.819768,4.963341,-9.773451,6.288887,2.722988,-4.298340,9.640568],[5.524874,-4.278618,6.608408,-2.045614,-0.554221,-7.538815,-1.129639,-6.339643,3.863336,1.298802,-1.025196,5.128158,-1.341288,-9.889603,4.387261],[-6.765964,-2.181064,5.311366,-1.379319,-0.863335,8.814938,-1.394301,7.550611,8.607326,1.870908,7.942702,9.277850,6.439555,1.528889,-9.180156],[6.743438,-0.057848,2.100731,-0.849818,7.045500,-2.372198,3.451288,-1.217568,-5.343456,4.716479,-6.252383,5.636132,-7.232083,-1.275019,-6.953100]],[[-4.763816,1.595161,0.815249,-9.741759,-7.403411,-4.580538,-0.731605,-5.801859,-0.841110,5.128091,-1.334191,8.722177,9.352852,-3.252257,9.212504],[-3.802389,6.602968,-5.840528,-3.967048,-3.970913,-4.228362,7.230078,-0.898492,4.489488,-0.766099,0.137841,0.549387,-1.639971,-4.462518,-6.070354],[2.888014,4.144473,-0.832553,9.962334,-7.097379,-4.823018,-7.010506,1.862123,2.554568,-1.275951,8.321321,-7.763570,-3.201753,8.738346,3.004557],[-7.949381,-8.387737,4.642155,-7.661097,2.343577,-3.205540,1.674051,-0.974154,-2.737892,-7.443207,7.404344,-8.037989,-5.376629,9.804473,6.791737],[1.184834,4.328836,4.178713,-9.634247,-8.879885,-8.396812,1.656494,4.764245,-8.540353,4.601474,-9.946396,1.993696,-5.582524,6.982669,6.217629],[1.304655,2.000370,9.895623,9.114239,-8.910241,7.133610,8.454551,-3.489521,-8.332414,-2.224000,1.959690,6.473031,7.149399,-8.342827,9.379493],[9.857658,-9.991177,6.663224,6.861269,-0.671123,-9.420330,-7.052486,-3.538268,2.462484,5.798479,4.078590,-6.738961,6.381409,-2.588383,0.125420],[-6.277068,-5.693643,4.418962,-8.922067,3.115550,-5.057133,-4.795998,6.612502,7.884255,-2.328845,-4.462638,-4.799893,-7.237943,-3.970575,9.579131],[-1.843541,-7.928427,3.175378,-1.558310,-7.444575,-1.934090,-8.632515,8.762662,4.912740,-4.951537,4.853468,0.169793,2.419110,-4.273960,1.525459],[3.712669,9.984417,-4.002083,1.013295,-7.792394,-3.394624,-9.370398,1.144262,-9.757461,9.805952,-2.069452,5.444000,-8.335808,4.729710,-3.494110],[-6.723784,-4.486432,5.259188,-1.631660,-4.462448,-4.370886,6.557618,8.414757,-7.024059,-1.793788,-4.287452,0.304838,-4.859841,-8.366289,-0.375415],[-6.265948,9.320876,-6.626167,-9.169834,2.684660,3.589671,0.360062,9.558093,2.110164,0.491879,7.161894,8.336771,1.339335,-0.960872,3.804738],[5.506428,4.683153,9.806950,7.721203,6.020854,-5.288972,4.247904,3.565515,-3.465499,-5.687972,-5.803688,9.633963,-0.034701,-7.560340,-6.622392],[0.815902,7.776809,-4.405619,-3.367573,-3.574474,2.475588,-6.166799,3.240674,8.575983,5.282137,8.964688,8.909398,5.419749,9.680372,-0.527891],[6.497779,6.840810,-1.198225,2.543366,-8.338096,-7.483392,-7.594629,-4.273150,1.643061,1.022358,4.490089,-7.567902,7.849698,3.286423,3.864793]],[[0.302505,9.736469,-6.698121,-1.569180,6.066185,4.266449,-4.353751,-5.242073,0.352436,-0.011391,-2.366832,8.946730,-1.066211,-3.960905,-4.787681],[4.802908,4.707834,-1.323303,0.929775,4.072074,5.585172,-2.708527,5.815397,-3.235083,-1.717434,6.811096,8.951074,-2.859356,-2.147979,8.492710],[-1.060491,-0.525194,7.511228,6.579070,6.235517,4.244565,-7.817724,2.374493,9.959845,-7.792581,-8.785980,-3.886096,5.535281,-2.345806,-5.662648],[-1.446142,-2.223874,-0.697624,7.366170,-7.068797,-3.788406,-5.984315,-6.277766,-8.562215,7.596993,1.748767,0.427022,3.419286,-9.903336,-6.802395],[5.837735,-5.189845,2.510443,-5.381365,-1.040265,1.961042,-0.740242,7.498024,8.196600,-5.627682,7.268798,0.964128,-6.013662,1.981954,-2.428944],[4.549081,-5.275432,6.210307,-6.209382,-2.589199,6.591764,0.371769,2.565888,-4.897791,9.753143,-5.546539,-3.708302,7.714459,-6.015893,-2.248114],[-2.907343,5.188876,5.411958,-1.093899,-9.291484,-3.284215,-1.994294,3.320617,2.390999,7.774280,1.073760,6.967675,2.515756,-9.479906,7.184942],[-5.815922,-2.824555,-4.194144,-8.998289,9.655118,6.299937,-5.564580,7.553583,-6.708943,0.175630,0.387479,2.235401,0.435506,7.098013,-6.203946],[-3.630756,-3.380655,-9.090471,-9.882083,5.334397,5.832383,1.361175,7.085230,-0.326941,3.112554,2.054485,-2.580735,4.835679,3.812985,0.868987],[2.205096,-2.011230,-2.483869,-8.215654,3.745348,-1.785550,0.438733,5.987809,-5.557346,-0.254611,5.527344,4.777904,-5.046220,1.846002,5.343636],[5.949186,-4.175804,8.819132,6.307931,9.041377,5.865503,1.903048,-5.965959,6.639390,-1.681908,-9.590445,2.136174,3.569418,3.058613,5.740444],[9.731562,7.487101,-0.483649,-5.458897,2.224220,7.014991,9.249263,6.683022,0.429407,9.490966,-3.774347,3.613320,7.945301,7.621879,-6.726196],[8.841504,4.858530,8.622633,1.775070,2.650446,-6.265661,-3.739918,-2.266184,9.167499,-7.967067,9.917126,-3.662972,6.145682,-7.900574,-1.575721],[7.152439,-5.965940,9.374555,9.558284,-4.098078,8.850849,1.246956,-3.968409,1.223339,4.301476,-1.829039,-7.826642,7.277087,-5.858879,-4.854667],[-2.457416,1.334444,-2.199794,5.429972,7.772316,1.701808,-7.859527,-7.996552,-1.014764,-7.031276,-4.377320,-3.535541,9.788684,-9.767751,8.848674]],[[0.501513,-3.110318,5.309260,8.179804,-5.102181,-1.780563,5.686125,-9.462361,0.192978,0.147624,-3.672079,2.168920,-9.998658,0.555957,-1.041395],[7.224254,-3.536180,-5.968683,-6.675663,-5.586989,1.422343,-8.846058,1.920396,-5.215408,6.650782,-5.657188,3.577901,5.695084,4.941883,-8.045653],[8.270510,6.776597,-5.185739,2.871711,7.866753,5.915370,-8.800484,3.803309,6.927437,4.130950,2.709048,-1.460637,2.480307,-9.377016,-1.685426],[-4.577446,-7.266141,-5.730836,-1.656543,2.664808,8.758590,-9.347135,5.165867,-0.900405,9.690359,3.670580,2.698965,-2.312016,6.452632,2.676217],[9.950619,-4.932033,0.975481,-2.931774,-3.808250,6.516384,8.981561,-3.338962,4.949022,5.378189,-6.721856,7.134363,-3.887280,-3.546554,-2.740291],[-4.102923,5.941237,5.836431,6.024465,-9.012155,-7.240292,1.161368,3.563112,-3.075764,-7.483653,-5.237410,-4.575475,9.145987,4.058821,0.092766],[5.256438,4.853988,-0.689181,-9.850152,8.710140,9.617522,-4.208526,5.693430,-1.554385,5.184293,1.362820,4.725515,1.247075,-1.842050,-1.103635],[6.967146,1.930746,2.288869,1.166320,4.990554,-0.664257,-7.972071,-8.386467,5.015791,9.502883,4.351501,-4.302329,6.854732,6.520425,-6.669527],[3.397242,-7.598481,-6.567964,-5.657866,2.444752,-4.385336,-1.247691,-9.247995,-4.119312,-3.436553,-3.022002,-1.020328,-2.855358,1.014111,-8.288449],[-6.887721,4.133663,-5.258147,-5.095462,5.031159,0.419180,4.933903,4.426945,-3.236105,6.349497,2.077016,-2.621024,-9.633642,6.976425,4.717478],[0.816250,3.868286,-0.620783,3.327870,-0.900656,-4.100770,-7.684862,-0.462493,8.470497,-6.401820,0.866868,8.262096,4.991299,-2.745983,9.806602],[-6.259728,0.585486,9.009698,-0.061598,-6.804038,9.439995,-8.145281,0.960733,1.544305,8.209666,0.009155,-6.040837,-7.315795,9.291086,-2.355316],[-1.021120,4.860685,6.472306,8.736741,8.534272,-0.277699,-5.447625,4.655059,7.198164,6.796723,-3.501823,0.593467,8.339324,-4.202075,3.189875],[5.414785,-5.853381,2.501475,6.500850,6.103361,2.613983,8.119521,-5.035495,0.298133,-5.837139,-9.920042,1.825868,8.068435,9.145180,3.474755],[-5.050623,4.498184,-2.696825,-0.231664,1.042437,-2.746132,-6.524383,7.651146,-1.638876,-9.961686,4.797693,6.322308,0.157518,1.205057,6.661059]],[[4.173129,9.594561,-6.609170,7.604687,8.183406,-0.822885,8.047174,2.207433,8.927806,3.355540,-9.743213,-0.421784,-0.453629,-9.267533,-3.810245],[-3.368485,-6.082334,-0.667596,7.498462,2.418349,3.814095,1.137772,-0.897400,9.083473,-1.337147,-8.026421,2.055208,3.852444,-5.214779,4.178808],[2.412226,-9.454960,8.601505,-0.661497,-8.540074,1.556037,6.754556,3.209507,8.925943,3.843113,2.818573,3.903938,-8.881266,-9.077134,-9.844721],[5.504469,-9.281052,2.740018,2.337932,-4.576351,-2.627913,4.001838,-9.928505,2.671573,4.160618,-1.211695,-1.298864,0.571260,-2.967783,7.948872],[3.536887,-4.010480,-1.187302,7.726656,2.649940,-4.743590,2.182286,7.788386,-7.747284,7.469116,4.182915,-6.613412,9.086378,-8.651031,-8.757703],[7.164553,-4.791115,0.079153,9.457578,-1.880567,-6.071414,-8.886138,-0.439633,-0.580845,8.152984,-3.966784,4.278067,-9.546595,-2.490599,-2.188080],[6.107435,-5.243351,6.662475,-7.621236,-6.348778,0.477625,1.062318,-6.952158,4.284600,-3.816426,0.846589,3.296111,-8.034879,5.524506,-0.205491],[7.882086,8.352669,2.016523,5.074301,-5.370319,1.312465,-6.077342,9.153930,-4.565152,3.388448,5.589803,-9.035382,2.421050,2.214263,2.268683],[-9.156616,7.017813,4.298955,-3.874655,-4.475503,-2.954976,-7.105790,5.759287,-1.063026,-3.636520,-4.233306,-6.878767,-5.302896,8.507960,-1.114541],[4.605276,7.033085,0.740330,-1.423788,7.244177,-2.618952,-7.669843,0.156225,-4.878649,0.747263,4.434604,4.697901,-1.168536,-1.557257,4.141316],[0.082664,2.975730,4.008280,0.033477,9.400312,-8.561409,-0.577011,-4.495722,-2.271277,0.164886,-7.654005,-6.768556,-7.325805,4.751688,-9.231231],[-0.188706,-9.337112,3.379390,-2.732887,2.333882,6.501039,7.504423,-6.509361,9.961357,-1.239742,-4.908159,-3.020909,-9.604148,-5.746090,8.135262],[-5.843745,-3.561175,5.498242,-6.221165,-7.656748,3.369452,-4.863192,7.927619,5.000880,6.501524,-2.777451,-9.617549,-1.934655,1.871777,-5.963543],[-7.659166,-4.999537,7.762368,-4.418920,9.426037,4.995572,-7.038214,1.088252,-4.387747,8.755894,0.548754,-0.645337,-5.594452,-4.888903,4.708588],[-7.469836,-4.255058,-5.248050,-1.675593,1.680031,2.724408,7.560174,-1.048003,7.035216,2.212307,3.362353,-2.082434,-7.457763,-9.743299,0.651282]],[[2.893529,3.762989,-5.989470,-2.462960,-2.662168,6.751671,-1.444607,-3.804564,7.122904,-2.158733,-1.934561,0.152175,1.908549,6.242734,5.049999],[3.328289,-8.920185,-2.600008,-6.672179,2.638072,-6.427310,-8.523958,5.779901,-5.679853,-1.799204,8.262015,-5.702064,-3.800820,-1.193715,1.179150],[-3.810209,3.167471,-2.289892,3.481402,-9.188441,7.470158,5.394171,6.251824,-0.534084,-9.422015,-8.706293,7.825560,-0.071632,-4.154265,1.148670],[-8.652060,-3.809535,-2.684003,9.580954,9.277811,5.193109,2.613874,-3.497121,8.429501,-0.939767,-5.083405,-0.172691,9.682875,1.427725,6.021568],[1.747003,-5.632326,7.187104,-0.830247,-5.926672,-9.261476,6.636298,1.975870,1.934005,-1.865996,-1.075483,-3.775106,2.431943,2.195116,-6.316781],[0.908259,4.020594,4.365545,0.076269,3.806811,-5.879268,4.646525,3.768817,5.284386,8.884159,-0.280072,-8.493790,-6.858040,-6.956904,-0.722216],[4.975057,5.605239,5.174403,4.648658,-0.860492,1.476634,7.295399,-0.121192,7.839334,4.396664,-0.394476,-9.090906,-9.760443,-1.201425,-1.012485],[2.138950,-2.129471,-4.342271,-2.133821,-2.161045,4.510909,5.785893,-9.389311,2.533775,3.549400,3.453408,1.034585,5.972386,-9.286816,-7.623773],[-3.193623,-9.915908,-4.489057,6.789034,1.102056,-3.303007,8.703859,0.573636,6.397996,6.332720,6.492008,-8.060616,-7.138328,-4.416102,4.338065],[3.284972,4.263516,7.325375,5.409096,-2.896975,-7.446525,3.550945,-6.133494,-5.909686,1.172376,-1.917932,-2.231526,3.434239,-3.916346,8.856487],[1.004484,-5.870279,6.587647,-7.945288,-4.520300,7.724677,8.352963,-2.853771,1.947857,-0.154426,-9.505217,9.776203,1.625598,4.640467,-4.941860],[-8.590744,4.595334,-7.207983,-5.862770,2.184121,7.926467,7.012626,3.861359,-4.310774,-2.855921,-7.293099,-0.812368,6.625468,-9.177664,5.592004],[-5.971897,-1.354563,-7.670680,-3.524735,-6.539482,6.271476,-9.463951,-1.463982,-6.819678,-0.620561,1.764557,7.075901,-3.158169,-3.316592,2.306576],[9.879332,5.946803,-3.389739,7.504168,-5.291731,-7.114467,3.855940,-0.631762,9.003014,0.350042,-1.571890,-7.812295,-3.274621,-5.231112,0.152826],[-6.990594,4.800660,1.060150,-1.895357,-0.430114,-8.449077,-3.078740,2.526743,4.930721,-9.736102,-3.343765,-6.683263,-2.359230,6.636519,5.419561]],[[2.341034,-4.610799,5.445242,-9.247215,-1.512919,-1.569350,6.097474,-3.603006,9.375015,6.310896,-9.871538,-3.005859,-1.806603,7.335828,-5.264363],[5.966775,2.989432,-7.476468,0.348535,-9.497404,-5.414861,-4.231629,0.687961,-3.929927,-6.474627,-3.347984,-4.115938,0.891528,-9.535637,-1.495667],[3.209413,-2.132259,5.002968,8.485603,9.085118,-2.489536,-9.743485,4.369684,-9.212365,5.401068,-7.122917,7.551575,-4.071327,4.776970,-9.255903],[5.108021,3.232691,-9.425384,4.114398,7.706995,2.690037,-9.286575,-4.493300,0.652792,8.131415,-0.067550,3.378309,-6.278108,-0.328280,-7.270207],[-7.779206,9.661449,6.783371,-7.549970,6.801920,6.843344,-9.899537,6.892036,0.202422,2.158908,8.670227,-9.620954,0.035225,-5.241824,7.832875],[-9.293712,4.688653,6.387138,3.768567,6.010587,-6.853224,2.849958,-5.701772,5.403961,-2.010994,-9.793697,-1.921493,-9.263875,-5.932372,-2.560160],[6.170856,9.888526,-4.632200,0.501141,-9.234535,-9.614820,7.172136,9.764873,-7.464926,5.993036,9.885052,-3.921117,2.502887,-4.350414,-1.307010],[6.335942,1.695704,-4.791602,2.940516,-0.421792,-6.846942,-4.618359,-7.711722,3.612734,3.470872,9.741861,-6.994162,-6.778161,-4.514523,9.960843],[2.858124,-8.930571,5.746174,-7.293635,-1.578320,8.544588,-4.258505,-0.334168,0.045610,6.115215,6.326154,-8.682759,1.485097,3.236871,3.887964],[-1.017592,7.990346,9.268262,4.167330,6.782971,-2.031191,-3.372033,1.858667,-1.546554,-0.869931,0.973354,-0.052583,5.130824,-0.397995,-3.308940],[-1.418458,5.289753,0.246661,-8.175646,-8.819194,9.152609,-5.731101,9.952147,-3.484002,2.314002,-5.260037,-2.161691,-5.567790,-5.182721,-2.695660],[-7.038379,0.484132,-6.416522,-7.656136,9.517475,6.041595,-6.413876,-5.587320,0.025469,6.342921,9.014818,2.603811,-0.159328,5.431731,-1.173811],[8.553000,-2.634423,-5.693084,-9.640638,-8.301595,-5.022109,-0.076973,3.348156,-2.295766,4.325408,6.090836,9.062448,5.993895,-8.735405,-8.999499],[-2.750126,8.185049,-5.734337,-4.666870,9.550165,-6.934649,-7.421450,-5.195483,0.276528,-8.820758,-4.691666,4.619798,-1.443441,1.890459,-7.414625],[9.207903,-2.814757,1.985207,4.975741,0.262795,-8.540447,-6.927057,-5.475662,9.390442,1.155126,-9.235558,1.386274,-0.747953,-6.050685,3.653082]],[[8.495891,-7.928914,1.400917,0.873323,5.462204,3.696106,-1.257435,-8.906775,-3.822693,9.770412,6.272922,7.166074,8.190600,-4.450644,-6.397408],[-0.873732,-3.339433,9.180166,6.514319,-5.424134,7.276573,-5.919531,1.029558,-2.924126,-9.255788,-2.069834,2.288099,2.856961,3.011037,1.036651],[0.556787,5.770076,-8.395709,8.147217,3.634435,-5.868015,-3.141561,2.587129,4.899396,6.994831,6.606574,0.526541,-2.711107,3.544479,-5.012714],[5.477384,3.702904,0.595322,4.460827,6.753530,0.504941,2.435762,-2.245130,3.868360,-8.375141,-5.038419,-8.923608,-9.354672,-3.892292,-1.924718],[-2.421634,-8.068144,3.433754,4.375692,-0.957863,8.294707,-9.179062,9.683536,3.586230,-2.757020,-5.359566,4.963203,-6.171175,3.524103,-3.323033],[5.175775,2.696492,-0.295337,-2.207286,2.810904,-4.196539,-7.040650,4.464518,4.844780,-7.739804,-0.266830,-7.845812,-7.005972,6.889189,9.194533],[5.778727,2.452983,-4.601014,7.675241,2.435597,-3.525514,-5.439285,6.280835,-5.945056,-1.852421,-4.924692,7.067811,4.899276,-9.062502,1.617061],[-9.767100,-0.719748,3.019307,1.577958,5.930407,0.579057,-0.473917,-3.675369,4.839462,-0.035955,-2.882504,-6.896686,-0.109776,7.390360,7.894977],[-6.673034,7.139745,5.748762,-8.288306,-3.368757,5.040883,5.153010,7.085974,4.896190,-0.471032,-1.736835,9.483336,5.549452,-7.521309,-9.735584],[6.480650,2.868419,4.037167,-1.547453,3.424485,-8.338079,-4.890671,-2.979872,0.780524,7.929099,-1.833792,-6.540195,-2.668887,4.664977,-9.263666],[-4.460000,-6.697118,2.416181,-0.048464,8.256640,-9.239292,9.902831,1.806267,-2.808539,5.065617,3.008178,4.083515,8.338911,5.910925,1.322659],[-1.968233,9.932358,7.684160,5.536742,-2.992710,-5.945802,-0.904420,-1.752523,6.065804,-8.456022,-6.055566,-3.365947,-4.026675,9.256288,-5.348054],[4.745473,3.988753,-3.291885,5.419470,-4.838775,-1.619908,-7.892443,-4.240410,2.585841,5.365343,5.616637,5.616689,-1.441608,3.527829,9.046025],[-2.381984,0.296493,3.361516,-0.555554,9.507604,2.095910,4.863733,-7.360144,-9.390707,-6.703435,3.157153,2.107137,5.605811,-3.797900,2.505080],[8.531192,6.344984,3.337009,-9.828690,1.325534,1.165520,9.512658,4.295466,-4.161203,8.019054,6.067269,-7.318057,8.278928,-9.687120,1.435453]]], dtype = "float64")#candidate|2822|(11, 15, 15)|const|float64
bop_2823 = relay.mod(const_2821.astype('float64'), relay.reshape(const_2822.astype('float64'), relay.shape_of(const_2821))) # shape=(11, 15, 15)
func_1723_call = mod.get_global_var('func_1723')
func_1729_call = mutated_mod.get_global_var('func_1729')
var_2834 = relay.var("var_2834", dtype = "float64", shape = (24, 1))#candidate|2834|(24, 1)|var|float64
const_2835 = relay.const([-5,2,5,10,2,10,-3,-1,8,-5,3,10,-2,4,-6,-8,6,-2,2,6,-6,-5,7,-9,3,7,-9,-5], dtype = "int8")#candidate|2835|(28,)|const|int8
var_2836 = relay.var("var_2836", dtype = "int32", shape = (1, 840))#candidate|2836|(1, 840)|var|int32
call_2833 = relay.TupleGetItem(func_1723_call(relay.reshape(var_2834.astype('float64'), [2, 12]), relay.reshape(const_2835.astype('int8'), [1, 28]), relay.reshape(var_2836.astype('int32'), [6, 140]), relay.reshape(var_2836.astype('int32'), [6, 140]), ), 7)
call_2837 = relay.TupleGetItem(func_1729_call(relay.reshape(var_2834.astype('float64'), [2, 12]), relay.reshape(const_2835.astype('int8'), [1, 28]), relay.reshape(var_2836.astype('int32'), [6, 140]), relay.reshape(var_2836.astype('int32'), [6, 140]), ), 7)
uop_2841 = relay.acosh(const_2821.astype('float32')) # shape=(11, 15, 15)
var_2844 = relay.var("var_2844", dtype = "float32", shape = (11, 15, 15))#candidate|2844|(11, 15, 15)|var|float32
bop_2845 = relay.right_shift(uop_2841.astype('int64'), relay.reshape(var_2844.astype('int64'), relay.shape_of(uop_2841))) # shape=(11, 15, 15)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_2849 = relay.TupleGetItem(func_1104_call(), 0)
call_2850 = relay.TupleGetItem(func_1105_call(), 0)
uop_2857 = relay.atan(const_2821.astype('float64')) # shape=(11, 15, 15)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_2865 = relay.TupleGetItem(func_975_call(), 0)
call_2866 = relay.TupleGetItem(func_976_call(), 0)
bop_2869 = relay.less_equal(uop_2841.astype('bool'), relay.reshape(uop_2857.astype('bool'), relay.shape_of(uop_2841))) # shape=(11, 15, 15)
output = relay.Tuple([bop_2823,call_2833,var_2834,const_2835,var_2836,bop_2845,call_2849,call_2865,bop_2869,])
output2 = relay.Tuple([bop_2823,call_2837,var_2834,const_2835,var_2836,bop_2845,call_2850,call_2866,bop_2869,])
func_2874 = relay.Function([var_2834,var_2836,var_2844,], output)
mod['func_2874'] = func_2874
mod = relay.transform.InferType()(mod)
var_2875 = relay.var("var_2875", dtype = "float64", shape = (24, 1))#candidate|2875|(24, 1)|var|float64
var_2876 = relay.var("var_2876", dtype = "int32", shape = (1, 840))#candidate|2876|(1, 840)|var|int32
var_2877 = relay.var("var_2877", dtype = "float32", shape = (11, 15, 15))#candidate|2877|(11, 15, 15)|var|float32
output = func_2874(var_2875,var_2876,var_2877,)
func_2878 = relay.Function([var_2875,var_2876,var_2877,], output)
mutated_mod['func_2878'] = func_2878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2486_call = mod.get_global_var('func_2486')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_2892 = relay.TupleGetItem(func_2486_call(), 1)
call_2893 = relay.TupleGetItem(func_2487_call(), 1)
func_1368_call = mod.get_global_var('func_1368')
func_1370_call = mutated_mod.get_global_var('func_1370')
call_2896 = func_1368_call()
call_2897 = func_1368_call()
func_2582_call = mod.get_global_var('func_2582')
func_2583_call = mutated_mod.get_global_var('func_2583')
call_2903 = relay.TupleGetItem(func_2582_call(), 1)
call_2904 = relay.TupleGetItem(func_2583_call(), 1)
uop_2907 = relay.asinh(call_2896.astype('float32')) # shape=(2, 9, 4)
uop_2909 = relay.asinh(call_2897.astype('float32')) # shape=(2, 9, 4)
uop_2914 = relay.atanh(call_2903.astype('float32')) # shape=(2, 9, 4)
uop_2916 = relay.atanh(call_2904.astype('float32')) # shape=(2, 9, 4)
output = relay.Tuple([call_2892,uop_2907,uop_2914,])
output2 = relay.Tuple([call_2893,uop_2909,uop_2916,])
func_2923 = relay.Function([], output)
mod['func_2923'] = func_2923
mod = relay.transform.InferType()(mod)
output = func_2923()
func_2924 = relay.Function([], output)
mutated_mod['func_2924'] = func_2924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2582_call = mod.get_global_var('func_2582')
func_2583_call = mutated_mod.get_global_var('func_2583')
call_2995 = relay.TupleGetItem(func_2582_call(), 1)
call_2996 = relay.TupleGetItem(func_2583_call(), 1)
func_1157_call = mod.get_global_var('func_1157')
func_1158_call = mutated_mod.get_global_var('func_1158')
call_2997 = func_1157_call()
call_2998 = func_1157_call()
output = relay.Tuple([call_2995,call_2997,])
output2 = relay.Tuple([call_2996,call_2998,])
func_3012 = relay.Function([], output)
mod['func_3012'] = func_3012
mod = relay.transform.InferType()(mod)
output = func_3012()
func_3013 = relay.Function([], output)
mutated_mod['func_3013'] = func_3013
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3024 = relay.const([[[9,6],[2,-2],[3,2],[3,-10],[6,4],[-5,2],[10,10],[2,-1],[4,1],[-9,2],[4,1],[-3,-2],[4,-1],[-10,-3]],[[-10,-8],[3,-5],[7,2],[8,-10],[-6,-10],[4,8],[-1,-7],[3,-5],[2,-7],[-3,1],[-10,-7],[-9,-3],[-2,3],[-6,-3]],[[1,9],[-1,9],[8,-2],[8,-2],[-8,-9],[8,1],[-4,5],[7,-6],[-2,-4],[-3,-10],[-9,-3],[-6,7],[4,1],[5,-3]],[[8,8],[7,-8],[3,2],[5,7],[4,10],[5,-4],[-3,-2],[-8,-9],[2,-4],[3,8],[1,2],[-3,9],[10,-5],[-7,5]],[[-3,10],[1,-8],[7,2],[3,8],[1,2],[-10,9],[-10,-7],[3,-9],[-9,10],[10,-3],[-1,9],[-6,-9],[-8,10],[2,9]],[[6,-1],[8,-7],[-10,-6],[-6,-7],[5,-10],[4,9],[10,1],[-1,-4],[-6,5],[-6,8],[-1,6],[5,-4],[-1,3],[-4,9]]], dtype = "int32")#candidate|3024|(6, 14, 2)|const|int32
var_3025 = relay.var("var_3025", dtype = "int32", shape = (6, 14, 2))#candidate|3025|(6, 14, 2)|var|int32
bop_3026 = relay.add(const_3024.astype('int32'), relay.reshape(var_3025.astype('int32'), relay.shape_of(const_3024))) # shape=(6, 14, 2)
func_19_call = mod.get_global_var('func_19')
func_22_call = mutated_mod.get_global_var('func_22')
const_3030 = relay.const([-8,7,-9,10,3,1,2,4,7,5,-4,4,5,-2,-7,-2,5,8,-2,-9,6,4,-5,-9,-8,-8,3,-10], dtype = "int8")#candidate|3030|(28,)|const|int8
const_3031 = relay.const([9,4,-9,-5,-4,-7,10,3,1,-10,-2,-5,1,-2,8,2,3,1,4,1,2,2,-3,-4,5,-3,4,-9,7,3,-1,3,8,8,-1,-1,8,3,-10,-4,-4,-4,-6,-3,-6,-8,-1,3,-8,-5,-9,-10,-10,8,3,-7,-2,5,-5,1,-7,8,-2,9,-1,9,-1,-9,-5,2,-1,-4,9,-1,2,-4,4,6,5,6,-10,-6,-5,3,-3,7,-4,-7,4,7,-3,-4,-5,3,-8,5,-5,8,-9,-9,7,-6,-10,-6,-4,-10,-6,-2,-7,-2,-5,2,10,-9,2,-1,5,-2,4,-9,2,5,-6,-8,3,9,-7,-5,4,7,-1,6,6,1,7,8,1,-7,10,1,5,9,-4,10,8,5,6,7,3,-1,10,-10,-3,-8,-2,6,1,-9,2,5,7,-1,-5,-4,-8,9,-8,-7,-7,6,5,7,9,-3,7,1,9,-8,4,-5,9,-10,-4,-8,3,-2,-5,-4,-7,3,6,10,10,2,-10,-6,-2,7,-7,-8,-8,1,-9,8,-4,4,9,-7,-1,-2,-7,-1,-7,6,-3,4,-3,7,-2,2,7,7,-9,4,-7,-3,5,5,4,5,4,-1,6,2,2,-5,-7,7,-1,6,-9,2,4,-5,-9,-6,-2,1,-4,10,-7,8,-9,8,8,-8,2,1,1,4,8,4,-8,2,10,-9,6,8,2,5,-9,-7,7,9,-5,6,5,-7,-7,-5,8,-3,-3,2,-7,7,2,-1,3,-4,2,-4,-4,-8,-10,7,10,6,10,-1,5,-5,2,-5,-5,-3,-3,-2,10,7,4,9,3,-9,3,2,-6,4,-2,-10,10,-1,-10,1,2,9,-3,2,-6,-10,9,-7,-8,2,2,4,7,6,-8,-9,-6,-8,1,-8,9,7,10,2,5,-8,9,-8,1,6,-4,2,5,10,10,-4,7,-6,3,7,-5,4,8,2,9,-9,-5,2,10,8,1,-10,3,-5,7,6,-6,-8,4,4,-8,-6,-3,-6,10,5,-8,-10,-1,7,5,-10,6,5,-7,-5,1,1,10,9,1,-1,-10,-2,-4,-9,-4,9,-8,-10,-3,-2,-6,8,-10,6,-2,-2,10,3,5,-4,-2,9,-9,-7,-5,7,-1,7,-4,3,-4,8,1,9,-3,4,-7,-9,1,-9,4,8], dtype = "int8")#candidate|3031|(448,)|const|int8
call_3029 = relay.TupleGetItem(func_19_call(relay.reshape(const_3030.astype('int8'), [7, 4, 1]), relay.reshape(const_3031.astype('int8'), [7, 4, 16]), ), 0)
call_3032 = relay.TupleGetItem(func_22_call(relay.reshape(const_3030.astype('int8'), [7, 4, 1]), relay.reshape(const_3031.astype('int8'), [7, 4, 16]), ), 0)
var_3045 = relay.var("var_3045", dtype = "int8", shape = (28,))#candidate|3045|(28,)|var|int8
bop_3046 = relay.logical_or(const_3030.astype('bool'), relay.reshape(var_3045.astype('bool'), relay.shape_of(const_3030))) # shape=(28,)
output = relay.Tuple([bop_3026,call_3029,const_3031,bop_3046,])
output2 = relay.Tuple([bop_3026,call_3032,const_3031,bop_3046,])
func_3064 = relay.Function([var_3025,var_3045,], output)
mod['func_3064'] = func_3064
mod = relay.transform.InferType()(mod)
var_3065 = relay.var("var_3065", dtype = "int32", shape = (6, 14, 2))#candidate|3065|(6, 14, 2)|var|int32
var_3066 = relay.var("var_3066", dtype = "int8", shape = (28,))#candidate|3066|(28,)|var|int8
output = func_3064(var_3065,var_3066,)
func_3067 = relay.Function([var_3065,var_3066,], output)
mutated_mod['func_3067'] = func_3067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1157_call = mod.get_global_var('func_1157')
func_1158_call = mutated_mod.get_global_var('func_1158')
call_3127 = func_1157_call()
call_3128 = func_1157_call()
output = relay.Tuple([call_3127,])
output2 = relay.Tuple([call_3128,])
func_3129 = relay.Function([], output)
mod['func_3129'] = func_3129
mod = relay.transform.InferType()(mod)
mutated_mod['func_3129'] = func_3129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mutated_mod.get_global_var('func_3129')
call_3130 = func_3129_call()
output = call_3130
func_3131 = relay.Function([], output)
mutated_mod['func_3131'] = func_3131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1157_call = mod.get_global_var('func_1157')
func_1158_call = mutated_mod.get_global_var('func_1158')
call_3208 = func_1157_call()
call_3209 = func_1157_call()
uop_3210 = relay.acosh(call_3208.astype('float32')) # shape=(2, 9, 4)
uop_3212 = relay.acosh(call_3209.astype('float32')) # shape=(2, 9, 4)
func_1157_call = mod.get_global_var('func_1157')
func_1158_call = mutated_mod.get_global_var('func_1158')
call_3216 = func_1157_call()
call_3217 = func_1157_call()
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_3233 = func_2025_call()
call_3234 = func_2025_call()
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_3235 = func_1184_call()
call_3236 = func_1184_call()
uop_3242 = relay.exp(uop_3210.astype('float32')) # shape=(2, 9, 4)
uop_3244 = relay.exp(uop_3212.astype('float32')) # shape=(2, 9, 4)
output = relay.Tuple([call_3216,call_3233,call_3235,uop_3242,])
output2 = relay.Tuple([call_3217,call_3234,call_3236,uop_3244,])
func_3245 = relay.Function([], output)
mod['func_3245'] = func_3245
mod = relay.transform.InferType()(mod)
output = func_3245()
func_3246 = relay.Function([], output)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
call_3247 = relay.TupleGetItem(func_1989_call(), 1)
call_3248 = relay.TupleGetItem(func_1991_call(), 1)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_3257 = relay.TupleGetItem(func_2815_call(), 1)
call_3258 = relay.TupleGetItem(func_2816_call(), 1)
output = relay.Tuple([call_3247,call_3257,])
output2 = relay.Tuple([call_3248,call_3258,])
func_3262 = relay.Function([], output)
mod['func_3262'] = func_3262
mod = relay.transform.InferType()(mod)
mutated_mod['func_3262'] = func_3262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3262_call = mutated_mod.get_global_var('func_3262')
call_3263 = func_3262_call()
output = call_3263
func_3264 = relay.Function([], output)
mutated_mod['func_3264'] = func_3264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3245_call = mod.get_global_var('func_3245')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_3268 = relay.TupleGetItem(func_3245_call(), 2)
call_3269 = relay.TupleGetItem(func_3246_call(), 2)
func_2874_call = mod.get_global_var('func_2874')
func_2878_call = mutated_mod.get_global_var('func_2878')
const_3277 = relay.const([4.173132,7.062259,-3.008459,-2.440234,8.394349,7.994245,6.399207,-6.932125,-8.318221,4.977594,-7.805583,3.192868,-9.062966,-2.867462,-9.386525,-1.577190,-3.932526,-1.564512,6.053872,4.205710,8.447030,6.022941,6.973011,9.884060], dtype = "float64")#candidate|3277|(24,)|const|float64
const_3278 = relay.const([10,-5,3,-6,4,-2,-2,5,-10,7,-3,8,5,4,-5,-10,-2,7,-2,-8,-6,-9,3,-10,-3,10,8,-8,5,2,4,-6,-8,2,8,6,10,-4,-1,5,-3,-10,1,3,-9,-8,6,1,-9,-4,1,-10,-7,-6,-9,4,6,-3,1,6,1,-3,10,-3,-5,3,-10,8,7,10,7,-8,-8,-1,-6,-9,3,-8,-5,1,9,-7,8,8,1,1,-2,2,-9,8,-2,-4,10,9,2,-5,-5,-2,10,-8,10,1,-8,1,-8,5,-8,6,-1,-3,-2,-6,1,-9,9,-5,7,-10,-1,-4,-2,8,8,-9,-6,1,-9,6,-4,4,-2,-2,-7,8,5,-6,3,-10,9,-9,10,-4,7,-2,6,-4,-4,-1,-1,8,1,7,-9,2,-6,2,2,-6,7,8,5,4,-8,-10,-4,-7,6,6,8,-5,10,2,-5,-1,-8,8,10,-3,-8,7,5,6,7,7,1,-2,9,-3,4,-1,-2,8,-2,2,5,-4,5,-2,-10,-8,2,2,-3,10,-10,2,9,-5,10,-2,9,5,-6,6,9,6,3,-5,-6,4,5,9,-5,-4,4,-7,-4,8,-1,-5,-6,2,-1,-6,3,3,7,1,-8,4,-2,6,-5,-3,7,-7,-9,4,7,8,-1,9,5,-9,-4,7,-6,-2,-7,7,5,1,-4,-5,-5,2,-6,-8,-10,3,2,2,5,6,2,-8,-9,2,-3,4,-2,8,9,8,-2,5,-3,9,10,-1,-1,9,7,-3,10,10,8,-7,-3,6,8,-9,-8,-8,-6,-1,8,-8,3,7,3,-5,-5,-7,7,-4,-5,-5,-1,-1,10,5,4,-4,7,2,9,10,-10,-2,10,-2,-7,6,-10,5,1,-1,-5,3,4,-3,-3,-7,-10,9,-5,3,-10,1,7,3,8,-2,6,-7,1,5,3,-4,-1,2,-6,7,5,-5,4,8,-1,-4,-6,-9,-3,2,6,-8,10,2,-5,9,5,-10,-3,2,9,-1,9,3,-6,-7,-2,1,6,-6,-2,-1,-1,7,-1,8,-7,6,-10,-9,5,-1,2,9,-5,9,9,6,10,4,4,-1,2,6,-10,10,-10,2,-3,10,-5,-7,8,4,7,-1,-1,-4,2,7,-7,-7,8,-1,-10,10,1,-8,1,8,2,-10,2,8,-4,-5,-9,-7,2,9,10,-7,-5,9,9,-5,-7,-5,-9,-2,-5,-3,9,-3,-2,5,10,-3,7,2,-1,8,-1,8,6,-2,-9,7,-9,-1,3,-2,-5,9,-1,7,-9,2,8,10,10,-4,1,6,-2,-2,2,9,1,9,-10,-5,-1,-6,9,-4,-10,-7,-10,10,2,8,-7,9,-4,1,-7,2,5,9,-6,4,-1,-6,6,4,9,9,-8,4,-9,7,-3,-3,9,-4,-5,2,1,-9,-5,4,5,-9,-4,-7,10,-10,-3,1,7,6,6,-9,5,2,3,3,1,-2,-7,-9,-1,7,-2,-5,-6,2,-6,-8,1,10,-8,-3,-6,-4,-4,-9,-2,8,-7,-6,1,-6,10,-7,-6,6,-1,-10,4,10,-9,-2,5,6,4,-6,9,-3,8,10,8,-7,-7,-5,-3,10,4,-2,5,-3,-9,5,3,-6,9,-6,-4,-5,1,3,-7,-7,-4,-1,6,-7,5,2,-9,10,4,4,-8,-8,-2,-5,3,-1,-1,-7,8,-2,5,10,2,-1,-5,-6,-7,4,-7,-8,10,-9,-2,8,2,3,-3,3,-3,4,3,-3,-4,10,7,-4,-7,-10,1,9,7,1,4,-5,-10,7,7,-4,10,-4,1,-7,-1,7,4,-3,9,1,10,2,-3,5,-2,2,-4,10,4,-2,-4,-5,7,9,4,1,4,-7,-4,-10,3,10,-10,-3,-10,9,5,2,4,10,-1,-3,6,-3,-4,1,-7,-7,3,-1,-6,-7,-6,5,-2,9,7,8,4,8,-4,-9,9,-8,-7,-5,1,4,-3,-1,-5,8,-4,7,-10,10,-1,-5,-5,3,3,-5,-2,-6,-9,1,7,7,-6,9,-9,-9,8,-3,8,6,-5,-10,9,1,-10,3,-2,9,5,5,9,-6,-2,1,-6,3,-6,-8,8,-7,2,8,-8,-5,6,-7,-7,-3,2,9,9,-9,5,-3,7,-1,-8,6,-5,9,2,-10,6,8,-5,8,-8,-2,2,-8,-5,-9,-8,-3,5,-8,-7,-6], dtype = "int32")#candidate|3278|(840,)|const|int32
var_3279 = relay.var("var_3279", dtype = "float32", shape = (2475,))#candidate|3279|(2475,)|var|float32
call_3276 = relay.TupleGetItem(func_2874_call(relay.reshape(const_3277.astype('float64'), [24, 1]), relay.reshape(const_3278.astype('int32'), [1, 840]), relay.reshape(var_3279.astype('float32'), [11, 15, 15]), ), 5)
call_3280 = relay.TupleGetItem(func_2878_call(relay.reshape(const_3277.astype('float64'), [24, 1]), relay.reshape(const_3278.astype('int32'), [1, 840]), relay.reshape(var_3279.astype('float32'), [11, 15, 15]), ), 5)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3281 = relay.TupleGetItem(func_3129_call(), 0)
call_3282 = relay.TupleGetItem(func_3131_call(), 0)
output = relay.Tuple([call_3268,call_3276,const_3277,const_3278,var_3279,call_3281,])
output2 = relay.Tuple([call_3269,call_3280,const_3277,const_3278,var_3279,call_3282,])
func_3286 = relay.Function([var_3279,], output)
mod['func_3286'] = func_3286
mod = relay.transform.InferType()(mod)
var_3287 = relay.var("var_3287", dtype = "float32", shape = (2475,))#candidate|3287|(2475,)|var|float32
output = func_3286(var_3287)
func_3288 = relay.Function([var_3287], output)
mutated_mod['func_3288'] = func_3288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2035_call = mod.get_global_var('func_2035')
func_2036_call = mutated_mod.get_global_var('func_2036')
call_3300 = func_2035_call()
call_3301 = func_2035_call()
func_2119_call = mod.get_global_var('func_2119')
func_2122_call = mutated_mod.get_global_var('func_2122')
const_3304 = relay.const([-5.486118,8.716698,-6.520480,-6.342506,-6.334605,-5.187633,-6.995212,-8.395350,-8.608877,0.957980,-7.679488,5.417738,-4.823903,-4.434043,-7.272020,4.777760,5.239942,-5.508491,2.983996,-1.072861,3.044833,6.841613,-5.634747,-2.034940,0.290542,4.346025,-7.175686,8.393336,-1.095654,-8.081263,1.819469,9.104317,1.838744,3.297439,6.519110,-3.068617,-2.702254,-7.467239,1.788599,6.472242,2.408240,-4.597525,0.692025,-8.015162,1.655415,-8.172422,-7.929019,4.360947,-4.736341,-8.275767,9.990279,-0.650933,1.550431,-8.431129,4.959695,3.323429,1.636889,-3.480916,-9.412207,-8.068578,-0.973727,-7.120343,8.284676,-5.171842,-5.756470,2.238761,0.424851,2.482609,-4.107381,-8.706990,1.809865,-8.387242,2.261559,-0.465810,-1.288422,-7.310532,6.821281,2.442265,-6.924758,-7.541774,4.011674,-4.125271,3.202329,2.095785,-9.267207,6.358401,3.808672,-1.027305,5.934838,-0.371991,9.577478,-5.294342,-8.568789,0.393054,7.341863,5.112127,3.458215,5.189824,-3.023097,6.600393,-8.539517,-1.210898,-4.381417,3.423387,2.456281,7.759713,-5.716817,-9.132036,-8.215844,1.102547,2.756086,-6.897173,9.964510,-9.371122,-0.195785,-7.872761,-6.423795,-9.159782,9.983494,-4.630020,-9.462371,9.765835,4.633324,6.145223,-0.293147,1.439153,9.990974,-6.965426,-5.340363,-5.321335,-0.214119,2.879014,-7.439734,-0.003323,8.816074,-1.241785,-3.856196,-5.528904,0.500637,6.674457,4.254136,-5.303084,-7.474020,2.649127,4.873714,7.106043,-7.293033,-8.258944,4.472615,-7.814388,-5.347202,-2.680314,-3.108898,-3.548068,-7.934135,0.466979,5.024853,-8.412957,9.263275,-9.687510,-9.493352,-0.738232,-6.723389,0.528952,5.275627,7.249364,-3.458232,8.520528,-0.853013,4.991671,3.845077,-0.234457,-5.144930,5.817356,-8.582723,-7.155132,8.209602,9.096877,3.182939,6.107271,-5.736902,-5.994138,-4.145867,-0.074971,-7.466800,4.348459,-5.828768,-0.066604,9.270322,-4.088641,6.058430,-9.147804,-5.156182,-0.782303,-1.625662,-3.718415,-4.626297,5.186566,-4.720957,-4.170990,9.750340,5.302271,5.311530,-2.309941,8.618174,7.823293,4.025420,5.891167,1.826315,-5.778705,-6.911656,7.299428,4.113179,0.948277,-9.851997,-9.947872,-3.142864,6.115792,5.353785,-6.229679,9.751149,0.483619,5.355224,-2.814844,2.830526,-6.489214,2.166314,-4.695426,-6.906173,3.069091,6.937713,1.729071,3.377108,-4.627754,-7.137533,1.790032,-6.667602,5.078310,4.019233,-7.512570,-7.246755,-2.368919,-7.374785,-5.814472,5.424317,4.094924,-9.006247,-8.807262,-3.410085,-3.742752,0.918491,-6.333714,3.965112,2.763534,7.748079,3.067435,-9.066911,0.204742,-5.688770,0.463429,4.281732,9.766994,2.115203,3.315127,-1.651069,1.920261,1.538940,4.352239,9.475723,-0.578916,-2.888713,-3.621089,7.225041,-5.856496,3.531504,3.505924,-4.491731,-9.349051,-4.621361,3.857491,-6.996185,-7.285523,-2.619907,-5.205288,-7.397588,-6.599871,-1.082070,5.540855,4.457419,3.202710,-2.040344,1.606128,6.784414,-6.515504,-8.865658,-9.704640,-6.660927,-0.949791,-4.720307,-6.835662,2.838941,-8.229106,8.893076,-8.547046,3.514285,-2.464111,-6.662478,-2.770345,2.211063,-8.535970,8.272179,-4.564751,4.544182,-4.765182,5.580812,9.918618,-6.913291,-9.254513,6.348729,-0.637616,2.904636,-6.680748,-6.651352,3.918343,-2.028589,0.998072,2.553295,1.533367,0.454878,-3.530009,7.476584,3.919513,5.607199,7.215450,-9.071049,1.742748,-2.034982,-0.177680,8.621848,2.930403,6.262176,2.178674,-2.166320,9.531205,-9.572294,4.569341,8.854893,5.995065,-6.699108,-7.782342,-1.368130,-6.105821,9.631294,-8.850868,7.385902,-4.058920,-7.038826,3.220251,4.529054,-8.821014,-3.278965,7.226308,5.296230,6.248612,9.242909,-5.930404,1.172166,3.571091,0.255001,9.196559,8.265410,9.017988,1.010441,-7.721797,-5.134195,2.104828,-8.889515,-6.072433,5.180316,-6.324796,3.196606,5.564711,3.600594,-9.708271,-2.848790,8.499446,8.858986,5.575573,3.974206,4.992727,9.122950,5.614096,2.051766,8.210230,3.974925,-1.819966,-7.392315,5.668177,-1.753804,9.471163], dtype = "float64")#candidate|3304|(400,)|const|float64
call_3303 = relay.TupleGetItem(func_2119_call(relay.reshape(const_3304.astype('float64'), [400,])), 3)
call_3305 = relay.TupleGetItem(func_2122_call(relay.reshape(const_3304.astype('float64'), [400,])), 3)
output = relay.Tuple([call_3300,call_3303,const_3304,])
output2 = relay.Tuple([call_3301,call_3305,const_3304,])
func_3320 = relay.Function([], output)
mod['func_3320'] = func_3320
mod = relay.transform.InferType()(mod)
mutated_mod['func_3320'] = func_3320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3320_call = mutated_mod.get_global_var('func_3320')
call_3321 = func_3320_call()
output = call_3321
func_3322 = relay.Function([], output)
mutated_mod['func_3322'] = func_3322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_3399 = relay.TupleGetItem(func_2815_call(), 0)
call_3400 = relay.TupleGetItem(func_2816_call(), 0)
func_1245_call = mod.get_global_var('func_1245')
func_1248_call = mutated_mod.get_global_var('func_1248')
var_3417 = relay.var("var_3417", dtype = "int8", shape = (28,))#candidate|3417|(28,)|var|int8
const_3418 = relay.const([-9,-7,-8,9,-5,-2,6,-7,6,-6,-10,10,10,2,-5,10,7,-2,-10,-9,-8,3,-7,-10,-8,1,-5,-10,5,1,-8,-6,8,4,-9,-2,3,2,-6,4,-7,4,8,-7,7,-4,6,-1,-8,-2,-9,-5,-10,4,-7,1,-7,-8,-8,-9,2,9,-1,-4,-9,-5,9,-3,-5,6,-7,-8,2,1,-10,7,2,-1,10,2,-2,-8,-7,1,-7,-7,-5,-1,10,9,2,3,-1,7,-10,1,-5,2,-9,5,-9,4,-7,1,9,-1,-5,3,1,-9,8,-2,8,-7,6,-7,-6,8,-8,-3,10,-7,10,-3,9,-9,-2,2,-6,9,10,-6,-6,2,-7,8,8,-2,-5,-9,-7,-3,-1,8,-1,7,2,-10,2,-2,-6,6,-8,-4,5,7,-2,-10,-5,-10,7,10,5,-10,3,-5,4,6,-2,-5,4,9,-4,2,-9,-6,10,-8,9,1,3,2,9,-9,8,6,-6,1,3,-9,-4,1,-4,-10,-10,-4,8,8,2,8,1,-4,-8,7,6,6,-3,-5,-7,-10,5,7,8,1,-5,1,-3,-5,8,6,9,4,-10,-1,-4,-1,-4,4,-6,-3,-6,-6,-7,-3,2,7,-1,5,1,-6,6,-6,8,2,9,-2,8,-5,9,-8,-7,-2,9,10,3,5,-5,-10,4,-4,5,-7,6,-8,10,-5,4,-3,-7,2,-1,1,-9,9,-3,6,1,-3,-5,-1,8,10,-7,4,8,-6,-5,4,-10,-9,6,-10,-9,3,5,-9,-1,-6,3,-4,8,-9,9,-10,8,9,-7,10,-4,-9,6,2,8,8,8,2,2,-10,7,-9,9,1,-8,1,-4,1,-2,-9,-10,10,9,-7,-5,3,7,9,9,-4,-10,1,9,6,-4,10,2,-6,-5,-3,10,-4,-5,6,4,-2,-7,10,6,7,-1,-6,10,7,6,6,3,4,-5,-5,-2,-5,2,7,1,8,5,-8,-7,-10,2,-9,-8,-6,-3,1,-8,4,-2,-9,-7,7,-2,-4,-10,4,-2,9,-5,-2,6,6,2,7,3,6,-3,-1,-10,6,1,1,2,-5,7,-9,-3,-10,-7,8,2,-9,9,-10,6,8,-5,-1,1,3,-3,4,7,8,2,3,2,-9,-1,1,-6,-5,9,7,3,-1,-4,2,-8,5], dtype = "int8")#candidate|3418|(448,)|const|int8
call_3416 = relay.TupleGetItem(func_1245_call(relay.reshape(var_3417.astype('int8'), [28, 1]), relay.reshape(const_3418.astype('int8'), [448,]), ), 2)
call_3419 = relay.TupleGetItem(func_1248_call(relay.reshape(var_3417.astype('int8'), [28, 1]), relay.reshape(const_3418.astype('int8'), [448,]), ), 2)
func_1368_call = mod.get_global_var('func_1368')
func_1370_call = mutated_mod.get_global_var('func_1370')
call_3420 = func_1368_call()
call_3421 = func_1368_call()
func_3064_call = mod.get_global_var('func_3064')
func_3067_call = mutated_mod.get_global_var('func_3067')
var_3424 = relay.var("var_3424", dtype = "int32", shape = (168,))#candidate|3424|(168,)|var|int32
call_3423 = relay.TupleGetItem(func_3064_call(relay.reshape(var_3424.astype('int32'), [6, 14, 2]), relay.reshape(var_3417.astype('int8'), [28,]), ), 2)
call_3425 = relay.TupleGetItem(func_3067_call(relay.reshape(var_3424.astype('int32'), [6, 14, 2]), relay.reshape(var_3417.astype('int8'), [28,]), ), 2)
output = relay.Tuple([call_3399,call_3416,var_3417,const_3418,call_3420,call_3423,var_3424,])
output2 = relay.Tuple([call_3400,call_3419,var_3417,const_3418,call_3421,call_3425,var_3424,])
func_3441 = relay.Function([var_3417,var_3424,], output)
mod['func_3441'] = func_3441
mod = relay.transform.InferType()(mod)
var_3442 = relay.var("var_3442", dtype = "int8", shape = (28,))#candidate|3442|(28,)|var|int8
var_3443 = relay.var("var_3443", dtype = "int32", shape = (168,))#candidate|3443|(168,)|var|int32
output = func_3441(var_3442,var_3443,)
func_3444 = relay.Function([var_3442,var_3443,], output)
mutated_mod['func_3444'] = func_3444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_3493 = relay.TupleGetItem(func_975_call(), 0)
call_3494 = relay.TupleGetItem(func_976_call(), 0)
var_3514 = relay.var("var_3514", dtype = "float32", shape = (2, 9, 4))#candidate|3514|(2, 9, 4)|var|float32
bop_3515 = relay.greater(call_3493.astype('bool'), relay.reshape(var_3514.astype('bool'), relay.shape_of(call_3493))) # shape=(2, 9, 4)
bop_3518 = relay.greater(call_3494.astype('bool'), relay.reshape(var_3514.astype('bool'), relay.shape_of(call_3494))) # shape=(2, 9, 4)
func_2874_call = mod.get_global_var('func_2874')
func_2878_call = mutated_mod.get_global_var('func_2878')
var_3523 = relay.var("var_3523", dtype = "float64", shape = (6, 4))#candidate|3523|(6, 4)|var|float64
var_3524 = relay.var("var_3524", dtype = "int32", shape = (840,))#candidate|3524|(840,)|var|int32
var_3525 = relay.var("var_3525", dtype = "float32", shape = (825, 3))#candidate|3525|(825, 3)|var|float32
call_3522 = relay.TupleGetItem(func_2874_call(relay.reshape(var_3523.astype('float64'), [24, 1]), relay.reshape(var_3524.astype('int32'), [1, 840]), relay.reshape(var_3525.astype('float32'), [11, 15, 15]), ), 7)
call_3526 = relay.TupleGetItem(func_2878_call(relay.reshape(var_3523.astype('float64'), [24, 1]), relay.reshape(var_3524.astype('int32'), [1, 840]), relay.reshape(var_3525.astype('float32'), [11, 15, 15]), ), 7)
func_1340_call = mod.get_global_var('func_1340')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_3531 = relay.TupleGetItem(func_1340_call(), 1)
call_3532 = relay.TupleGetItem(func_1341_call(), 1)
func_1527_call = mod.get_global_var('func_1527')
func_1529_call = mutated_mod.get_global_var('func_1529')
const_3569 = relay.const([3.457141,-4.735879,-9.290613,-5.032780,-6.053259,-7.981965,-5.520412,-2.304921,0.326714,-5.780685,-4.748296,-7.516227,7.727054,-6.026429,8.329528,4.430575,-4.351803,-1.602564,-1.747695,0.448681,4.019207,6.806593,5.184639,-9.176806,-2.948449,-4.446607,-4.124635,-9.001129,9.336686,-1.818190,8.930858,9.561374,3.401085,5.456195,-5.801912,-5.713854,-8.122733,3.711679,4.889972,-7.510482,5.245847,-8.154754,-9.840154,7.745734,-9.326291,-8.341432,-4.987230,4.814158,6.733568,0.905440,5.747331,3.744656,8.415451,4.593886,-0.749070,1.721302,-0.303176,3.910786,-2.395647,-6.798744,-7.321241,-9.980591,-3.201157,-6.777231,-4.103699,5.198163,-7.335478,1.321348,-0.691679,-9.526096,4.473939,-1.074190,-5.487945,-4.641174,-7.150961,4.592073,3.093573,3.689651,0.175771,6.550294,-6.378425,8.077183,-5.588923,-2.197919,2.132089,8.524005,-8.312539,-6.845516,-4.592655,4.102239,2.176100,8.175545,8.623217,-0.812454,4.023394,-5.374136,-6.592808,-8.715297,6.714437,7.682598,8.235082,2.509846,-2.889207,-1.245280,-3.591906,-1.886573,-5.285007,-6.195243,-5.428249,-7.268552,-1.738503,0.373357,-8.279484,0.211230,3.163225,-2.512313,-5.394151,-8.621998,7.956609,5.785207,1.933343,1.434415,7.808869,3.369142,-4.576834,6.046041,-0.009230,-6.452357,-1.936261,-8.570284,-0.454500,2.943464,-4.543968,-6.208209,-4.036736,2.053759,9.794647,-2.235682,-4.134596,-8.629932,0.033665,-5.740669,1.804061,7.629817,-1.155780,7.677876,-7.502318,7.270690,-8.150055,6.177899,3.488162,-7.500268,6.628423,-4.928097,-8.065055,5.296366,-0.662641,-9.042309,-8.070968,-8.802230,4.284097,8.774322,-8.034998,7.651953,-6.818171,1.251793,1.657815,-0.982478,-3.487277,3.690322,-7.486518,6.109833,-9.322957,-6.797287,1.754681,2.248567,-2.531101,-3.683814,-5.567701,4.763264,-0.062594,-5.708615,1.648541,6.371697,3.901277,-0.702353,9.770673,0.351129,4.021962,-8.487007,-4.843449,-0.830447,-5.657070,3.078778,-1.966111,-2.750205,0.663866,-4.632258,3.289169,0.242838,-8.920070,-6.681464,8.298140,4.817243,7.869585,9.984404,-0.595296,-3.887867,-5.285216,6.492261,0.518207,-5.299320,-9.900626,5.652272,-2.328046,2.196129,-7.973665,-4.572361,6.753567,3.844961,5.972990,-2.025144,-2.272912,-9.081157,-2.385437,7.749921,8.144668,-0.230151,-7.501466,-7.648813,-4.195991,-8.279724,0.108565,-6.538611,-6.068917,-6.144533,-8.408300,1.391145,6.848473,-4.895654,9.861163,9.635911,9.277685,0.631062,1.523747,-9.652219,8.332546,7.784982,2.786465,0.742378,5.094509,7.043422,-0.316248,-5.438512,-1.048815,0.786136,-8.171360,0.618892,-3.221601,9.542476,-4.691754,-7.263702,-8.864507,-7.422662,3.607106,-5.816574,1.222951,0.592027,-4.410110,-6.121779,-6.293773,7.871147,-4.845063,-6.668231,3.001324,3.970101,1.909724,8.274523,2.090772,5.671494,3.810725,9.986856,4.358974,-9.099317,-7.533760,-1.758803,-7.174901,0.800462,-6.073823,3.439602,8.303668,5.836210,-8.756097,9.462030,1.310523,8.959471,-2.852519,4.616883,9.157914,3.445932,-8.166545,-3.939854,8.647711,-8.556352,4.556081,2.541609,-3.209132,4.918699,9.476532,-9.102015,9.500430,7.633732,-2.263336,2.431354,-4.677838,5.258673,-5.145927,0.950848,4.983776,-3.778604,-3.089047,2.577284,-7.887588,9.913250,2.197119,-8.554444,8.882806,-3.611181,8.605844,3.103914,5.903248,-6.531383,-2.550592,5.514984,2.135435,-1.234070,-9.576486,-2.307006,-6.353781,-0.859428,1.424699,-0.412608,6.404614,-5.659202,-7.221053,-6.092861,-8.482231,-3.777774,4.928928,-2.901048,0.785563,-4.024728,0.794173,-9.616274,-5.923043,3.018732,-5.748068,5.762729,7.271006,-6.912377,1.777833,0.980638,8.319147,4.636255,5.296858,-3.594470,-1.289254,-9.986206,0.974105,-4.214856,-0.489151,-2.323716,5.227119,-4.498767,3.492677,7.183990,5.575196,3.931736,-8.486664,2.967111,-2.860819,-1.877473,-5.418939,-7.632246,0.866041,-1.308279,4.487215,-9.610465,-2.095033,7.877740,9.607915,-4.055561,8.131600,-0.830030,-2.234308,0.203980,1.087797,-2.040089,8.448144,0.987051], dtype = "float64")#candidate|3569|(400,)|const|float64
call_3568 = func_1527_call(relay.reshape(const_3569.astype('float64'), [10, 8, 5]))
call_3570 = func_1527_call(relay.reshape(const_3569.astype('float64'), [10, 8, 5]))
output = relay.Tuple([bop_3515,call_3522,var_3523,var_3524,var_3525,call_3531,call_3568,const_3569,])
output2 = relay.Tuple([bop_3518,call_3526,var_3523,var_3524,var_3525,call_3532,call_3570,const_3569,])
func_3583 = relay.Function([var_3514,var_3523,var_3524,var_3525,], output)
mod['func_3583'] = func_3583
mod = relay.transform.InferType()(mod)
mutated_mod['func_3583'] = func_3583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3583_call = mutated_mod.get_global_var('func_3583')
var_3585 = relay.var("var_3585", dtype = "float32", shape = (2, 9, 4))#candidate|3585|(2, 9, 4)|var|float32
var_3586 = relay.var("var_3586", dtype = "float64", shape = (6, 4))#candidate|3586|(6, 4)|var|float64
var_3587 = relay.var("var_3587", dtype = "int32", shape = (840,))#candidate|3587|(840,)|var|int32
var_3588 = relay.var("var_3588", dtype = "float32", shape = (825, 3))#candidate|3588|(825, 3)|var|float32
call_3584 = func_3583_call(var_3585,var_3586,var_3587,var_3588,)
output = call_3584
func_3589 = relay.Function([var_3585,var_3586,var_3587,var_3588,], output)
mutated_mod['func_3589'] = func_3589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_3596 = relay.TupleGetItem(func_1864_call(), 3)
call_3597 = relay.TupleGetItem(func_1865_call(), 3)
output = relay.Tuple([call_3596,])
output2 = relay.Tuple([call_3597,])
func_3634 = relay.Function([], output)
mod['func_3634'] = func_3634
mod = relay.transform.InferType()(mod)
output = func_3634()
func_3635 = relay.Function([], output)
mutated_mod['func_3635'] = func_3635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_3663 = relay.TupleGetItem(func_1864_call(), 1)
call_3664 = relay.TupleGetItem(func_1865_call(), 1)
output = call_3663
output2 = call_3664
func_3677 = relay.Function([], output)
mod['func_3677'] = func_3677
mod = relay.transform.InferType()(mod)
mutated_mod['func_3677'] = func_3677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3677_call = mutated_mod.get_global_var('func_3677')
call_3678 = func_3677_call()
output = call_3678
func_3679 = relay.Function([], output)
mutated_mod['func_3679'] = func_3679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2397_call = mod.get_global_var('func_2397')
func_2398_call = mutated_mod.get_global_var('func_2398')
call_3715 = relay.TupleGetItem(func_2397_call(), 2)
call_3716 = relay.TupleGetItem(func_2398_call(), 2)
output = call_3715
output2 = call_3716
func_3721 = relay.Function([], output)
mod['func_3721'] = func_3721
mod = relay.transform.InferType()(mod)
output = func_3721()
func_3722 = relay.Function([], output)
mutated_mod['func_3722'] = func_3722
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3746 = relay.var("var_3746", dtype = "uint32", shape = (8, 5, 7))#candidate|3746|(8, 5, 7)|var|uint32
var_3747 = relay.var("var_3747", dtype = "uint32", shape = (8, 5, 7))#candidate|3747|(8, 5, 7)|var|uint32
bop_3748 = relay.minimum(var_3746.astype('uint32'), relay.reshape(var_3747.astype('uint32'), relay.shape_of(var_3746))) # shape=(8, 5, 7)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_3751 = relay.TupleGetItem(func_1864_call(), 4)
call_3752 = relay.TupleGetItem(func_1865_call(), 4)
func_159_call = mod.get_global_var('func_159')
func_164_call = mutated_mod.get_global_var('func_164')
const_3767 = relay.const([0.225236,-9.433442,3.368972,5.219567,5.067342,9.721988,8.962148,-8.128351,-0.359255,4.303794,4.693591,-4.812267,8.311622,0.385953,9.691075,-0.321458,-3.813134,-1.976644,-2.117016,-8.174457,-8.791399,9.281902,5.928092,-5.615894], dtype = "float64")#candidate|3767|(24,)|const|float64
var_3768 = relay.var("var_3768", dtype = "int8", shape = (28,))#candidate|3768|(28,)|var|int8
var_3769 = relay.var("var_3769", dtype = "int8", shape = (448,))#candidate|3769|(448,)|var|int8
call_3766 = relay.TupleGetItem(func_159_call(relay.reshape(const_3767.astype('float64'), [4, 2, 3]), relay.reshape(var_3768.astype('int8'), [28,]), relay.reshape(var_3769.astype('int8'), [448,]), ), 4)
call_3770 = relay.TupleGetItem(func_164_call(relay.reshape(const_3767.astype('float64'), [4, 2, 3]), relay.reshape(var_3768.astype('int8'), [28,]), relay.reshape(var_3769.astype('int8'), [448,]), ), 4)
func_2119_call = mod.get_global_var('func_2119')
func_2122_call = mutated_mod.get_global_var('func_2122')
var_3775 = relay.var("var_3775", dtype = "float64", shape = (8, 50))#candidate|3775|(8, 50)|var|float64
call_3774 = relay.TupleGetItem(func_2119_call(relay.reshape(var_3775.astype('float64'), [400,])), 2)
call_3776 = relay.TupleGetItem(func_2122_call(relay.reshape(var_3775.astype('float64'), [400,])), 2)
bop_3783 = relay.less(var_3747.astype('bool'), relay.reshape(var_3746.astype('bool'), relay.shape_of(var_3747))) # shape=(8, 5, 7)
output = relay.Tuple([bop_3748,call_3751,call_3766,const_3767,var_3768,var_3769,call_3774,var_3775,bop_3783,])
output2 = relay.Tuple([bop_3748,call_3752,call_3770,const_3767,var_3768,var_3769,call_3776,var_3775,bop_3783,])
func_3787 = relay.Function([var_3746,var_3747,var_3768,var_3769,var_3775,], output)
mod['func_3787'] = func_3787
mod = relay.transform.InferType()(mod)
mutated_mod['func_3787'] = func_3787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3787_call = mutated_mod.get_global_var('func_3787')
var_3789 = relay.var("var_3789", dtype = "uint32", shape = (8, 5, 7))#candidate|3789|(8, 5, 7)|var|uint32
var_3790 = relay.var("var_3790", dtype = "uint32", shape = (8, 5, 7))#candidate|3790|(8, 5, 7)|var|uint32
var_3791 = relay.var("var_3791", dtype = "int8", shape = (28,))#candidate|3791|(28,)|var|int8
var_3792 = relay.var("var_3792", dtype = "int8", shape = (448,))#candidate|3792|(448,)|var|int8
var_3793 = relay.var("var_3793", dtype = "float64", shape = (8, 50))#candidate|3793|(8, 50)|var|float64
call_3788 = func_3787_call(var_3789,var_3790,var_3791,var_3792,var_3793,)
output = call_3788
func_3794 = relay.Function([var_3789,var_3790,var_3791,var_3792,var_3793,], output)
mutated_mod['func_3794'] = func_3794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2397_call = mod.get_global_var('func_2397')
func_2398_call = mutated_mod.get_global_var('func_2398')
call_3804 = relay.TupleGetItem(func_2397_call(), 0)
call_3805 = relay.TupleGetItem(func_2398_call(), 0)
func_2923_call = mod.get_global_var('func_2923')
func_2924_call = mutated_mod.get_global_var('func_2924')
call_3816 = relay.TupleGetItem(func_2923_call(), 1)
call_3817 = relay.TupleGetItem(func_2924_call(), 1)
func_2486_call = mod.get_global_var('func_2486')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_3818 = relay.TupleGetItem(func_2486_call(), 1)
call_3819 = relay.TupleGetItem(func_2487_call(), 1)
uop_3830 = relay.sinh(call_3804.astype('float64')) # shape=(2, 9, 4)
uop_3832 = relay.sinh(call_3805.astype('float64')) # shape=(2, 9, 4)
output = relay.Tuple([call_3816,call_3818,uop_3830,])
output2 = relay.Tuple([call_3817,call_3819,uop_3832,])
func_3838 = relay.Function([], output)
mod['func_3838'] = func_3838
mod = relay.transform.InferType()(mod)
mutated_mod['func_3838'] = func_3838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3838_call = mutated_mod.get_global_var('func_3838')
call_3839 = func_3838_call()
output = call_3839
func_3840 = relay.Function([], output)
mutated_mod['func_3840'] = func_3840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_3855 = relay.TupleGetItem(func_975_call(), 0)
call_3856 = relay.TupleGetItem(func_976_call(), 0)
output = relay.Tuple([call_3855,])
output2 = relay.Tuple([call_3856,])
func_3869 = relay.Function([], output)
mod['func_3869'] = func_3869
mod = relay.transform.InferType()(mod)
output = func_3869()
func_3870 = relay.Function([], output)
mutated_mod['func_3870'] = func_3870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3869_call = mod.get_global_var('func_3869')
func_3870_call = mutated_mod.get_global_var('func_3870')
call_3927 = relay.TupleGetItem(func_3869_call(), 0)
call_3928 = relay.TupleGetItem(func_3870_call(), 0)
output = relay.Tuple([call_3927,])
output2 = relay.Tuple([call_3928,])
func_3931 = relay.Function([], output)
mod['func_3931'] = func_3931
mod = relay.transform.InferType()(mod)
output = func_3931()
func_3932 = relay.Function([], output)
mutated_mod['func_3932'] = func_3932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3931_call = mod.get_global_var('func_3931')
func_3932_call = mutated_mod.get_global_var('func_3932')
call_3958 = relay.TupleGetItem(func_3931_call(), 0)
call_3959 = relay.TupleGetItem(func_3932_call(), 0)
output = relay.Tuple([call_3958,])
output2 = relay.Tuple([call_3959,])
func_3961 = relay.Function([], output)
mod['func_3961'] = func_3961
mod = relay.transform.InferType()(mod)
mutated_mod['func_3961'] = func_3961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mutated_mod.get_global_var('func_3961')
call_3962 = func_3961_call()
output = call_3962
func_3963 = relay.Function([], output)
mutated_mod['func_3963'] = func_3963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mod.get_global_var('func_3961')
func_3963_call = mutated_mod.get_global_var('func_3963')
call_3964 = relay.TupleGetItem(func_3961_call(), 0)
call_3965 = relay.TupleGetItem(func_3963_call(), 0)
func_1723_call = mod.get_global_var('func_1723')
func_1729_call = mutated_mod.get_global_var('func_1729')
var_3969 = relay.var("var_3969", dtype = "float64", shape = (24,))#candidate|3969|(24,)|var|float64
const_3970 = relay.const([-4,10,4,-9,3,-6,1,8,-1,-5,-5,3,6,7,2,8,10,-5,-5,7,-6,-5,-9,2,-1,8,-10,7], dtype = "int8")#candidate|3970|(28,)|const|int8
var_3971 = relay.var("var_3971", dtype = "int32", shape = (840,))#candidate|3971|(840,)|var|int32
call_3968 = relay.TupleGetItem(func_1723_call(relay.reshape(var_3969.astype('float64'), [2, 12]), relay.reshape(const_3970.astype('int8'), [1, 28]), relay.reshape(var_3971.astype('int32'), [6, 140]), relay.reshape(var_3971.astype('int32'), [6, 140]), ), 6)
call_3972 = relay.TupleGetItem(func_1729_call(relay.reshape(var_3969.astype('float64'), [2, 12]), relay.reshape(const_3970.astype('int8'), [1, 28]), relay.reshape(var_3971.astype('int32'), [6, 140]), relay.reshape(var_3971.astype('int32'), [6, 140]), ), 6)
output = relay.Tuple([call_3964,call_3968,var_3969,const_3970,var_3971,])
output2 = relay.Tuple([call_3965,call_3972,var_3969,const_3970,var_3971,])
func_3982 = relay.Function([var_3969,var_3971,], output)
mod['func_3982'] = func_3982
mod = relay.transform.InferType()(mod)
var_3983 = relay.var("var_3983", dtype = "float64", shape = (24,))#candidate|3983|(24,)|var|float64
var_3984 = relay.var("var_3984", dtype = "int32", shape = (840,))#candidate|3984|(840,)|var|int32
output = func_3982(var_3983,var_3984,)
func_3985 = relay.Function([var_3983,var_3984,], output)
mutated_mod['func_3985'] = func_3985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_3997 = relay.TupleGetItem(func_1864_call(), 0)
call_3998 = relay.TupleGetItem(func_1865_call(), 0)
output = call_3997
output2 = call_3998
func_4002 = relay.Function([], output)
mod['func_4002'] = func_4002
mod = relay.transform.InferType()(mod)
output = func_4002()
func_4003 = relay.Function([], output)
mutated_mod['func_4003'] = func_4003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_4018 = relay.TupleGetItem(func_2815_call(), 1)
call_4019 = relay.TupleGetItem(func_2816_call(), 1)
output = call_4018
output2 = call_4019
func_4027 = relay.Function([], output)
mod['func_4027'] = func_4027
mod = relay.transform.InferType()(mod)
mutated_mod['func_4027'] = func_4027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4027_call = mutated_mod.get_global_var('func_4027')
call_4028 = func_4027_call()
output = call_4028
func_4029 = relay.Function([], output)
mutated_mod['func_4029'] = func_4029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2923_call = mod.get_global_var('func_2923')
func_2924_call = mutated_mod.get_global_var('func_2924')
call_4030 = relay.TupleGetItem(func_2923_call(), 2)
call_4031 = relay.TupleGetItem(func_2924_call(), 2)
func_3262_call = mod.get_global_var('func_3262')
func_3264_call = mutated_mod.get_global_var('func_3264')
call_4037 = relay.TupleGetItem(func_3262_call(), 1)
call_4038 = relay.TupleGetItem(func_3264_call(), 1)
output = relay.Tuple([call_4030,call_4037,])
output2 = relay.Tuple([call_4031,call_4038,])
func_4047 = relay.Function([], output)
mod['func_4047'] = func_4047
mod = relay.transform.InferType()(mod)
output = func_4047()
func_4048 = relay.Function([], output)
mutated_mod['func_4048'] = func_4048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_4060 = func_1184_call()
call_4061 = func_1184_call()
output = relay.Tuple([call_4060,])
output2 = relay.Tuple([call_4061,])
func_4064 = relay.Function([], output)
mod['func_4064'] = func_4064
mod = relay.transform.InferType()(mod)
mutated_mod['func_4064'] = func_4064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4064_call = mutated_mod.get_global_var('func_4064')
call_4065 = func_4064_call()
output = call_4065
func_4066 = relay.Function([], output)
mutated_mod['func_4066'] = func_4066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_4104 = func_2025_call()
call_4105 = func_2025_call()
output = relay.Tuple([call_4104,])
output2 = relay.Tuple([call_4105,])
func_4106 = relay.Function([], output)
mod['func_4106'] = func_4106
mod = relay.transform.InferType()(mod)
mutated_mod['func_4106'] = func_4106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4106_call = mutated_mod.get_global_var('func_4106')
call_4107 = func_4106_call()
output = call_4107
func_4108 = relay.Function([], output)
mutated_mod['func_4108'] = func_4108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_4155 = relay.TupleGetItem(func_3129_call(), 0)
call_4156 = relay.TupleGetItem(func_3131_call(), 0)
func_2119_call = mod.get_global_var('func_2119')
func_2122_call = mutated_mod.get_global_var('func_2122')
const_4193 = relay.const([2.794994,-1.269574,5.487057,8.400090,-7.031449,8.169984,4.146041,9.398373,-2.291056,5.036004,-7.021404,-0.921344,-7.727132,5.359643,-1.466612,-5.298009,-8.630630,-1.255876,-3.268125,7.331814,-6.527411,8.216462,6.726308,-5.735552,3.406062,5.556247,9.556750,3.688532,7.645661,8.547213,2.913286,0.587377,-8.379390,-0.607427,6.930356,6.174932,-9.292190,-2.551372,-6.447535,5.013086,-6.042850,4.810222,-8.368949,9.263419,-9.563979,1.057600,-7.287837,3.976772,-9.922399,1.495435,-1.551450,7.289693,0.455617,-9.209533,-2.477739,5.184419,-2.346859,-5.699152,4.132242,-3.875537,-9.329985,-5.663346,-4.395973,6.579228,8.238957,2.839762,-6.166497,-4.813516,-1.883214,2.659255,-8.099042,5.248921,9.968438,0.101647,-0.928146,-8.001410,8.950986,7.731133,5.407593,-2.310795,-5.761245,-6.448042,-4.631121,-7.990243,4.002039,2.101873,3.513031,-6.153722,-1.949863,9.748759,-7.304889,4.173139,-3.763146,9.680966,9.964689,-9.837118,5.778939,-6.507011,3.032945,-5.524742,-5.631081,-6.141279,3.990658,5.879604,-6.022914,-5.981521,-1.150837,-6.184392,-9.821653,-8.611233,3.695545,4.212347,4.631177,-8.576731,8.206801,3.839480,-9.712835,0.364177,7.855997,8.906033,3.189751,-3.630142,4.661587,1.407535,-4.110331,-3.234314,-9.288695,0.668632,2.277065,2.679675,-1.894629,0.736645,-6.700770,-5.405741,6.904724,-7.701790,2.052314,-0.412037,3.432584,9.735721,-7.525835,-9.183623,1.960016,-4.558176,6.928451,1.199621,8.458191,3.376668,5.211359,5.243650,9.632969,-3.318099,-0.951389,-8.177828,-6.315682,7.063552,8.173945,6.969556,2.755295,1.448148,2.826870,7.252900,4.015161,6.541984,-4.540601,2.923545,-3.466488,3.796070,7.593099,-2.489181,6.171300,-5.079619,7.105347,6.291849,1.172616,-4.741819,-0.122175,1.672058,-1.060710,-5.864860,4.835820,-5.023968,3.142739,-5.532367,6.634629,-0.970310,7.348463,9.127172,1.821400,2.414077,-2.466152,5.651181,5.332220,-4.053588,4.452651,1.687643,0.218603,-2.942689,4.297762,9.163125,-9.526753,8.573120,-7.537235,-3.258884,5.564061,-5.603190,7.111502,-4.951402,5.520388,-4.902100,-4.105107,8.177814,-7.870778,-2.424850,3.527483,-2.218943,-6.036497,5.333297,5.302167,-0.582251,4.784882,-2.156183,-4.305903,-9.278018,1.712215,9.443694,-0.011587,9.275273,-3.131526,-1.073988,8.127355,4.861978,-1.527588,-4.929073,6.479986,-1.280873,-2.582476,1.106207,-4.932536,-9.847002,7.199388,3.658569,-2.436851,-3.068015,-5.595231,-0.157470,4.630821,1.745958,-9.459023,2.552330,-6.229990,8.306814,-7.188231,-8.010016,-7.826277,5.399523,-2.931548,1.346804,1.402847,3.580090,-2.266153,-8.808775,-4.007292,6.564624,5.179807,-0.796827,-6.153303,-4.364575,-3.598444,3.897993,2.687300,-5.543331,2.589622,0.839868,8.409076,9.546582,-3.071712,-9.688204,9.176663,-5.977941,-0.008500,0.114064,-8.694226,-1.278966,-9.404684,2.799309,-0.664299,9.673658,2.741059,-0.059263,4.113713,-4.655543,7.548026,-8.887762,-1.448502,-8.745120,8.393993,2.988705,8.019414,9.643290,-9.240461,-8.589186,-2.548332,-8.010832,-5.830938,8.626344,-8.853357,2.872751,-9.964183,8.940945,-3.621495,7.067753,5.357799,0.293477,-8.543898,-2.468189,5.767353,2.618163,-4.796886,1.434961,5.289033,-4.715548,-9.354265,2.817668,-3.566810,9.338938,-1.346097,-4.648534,-6.898211,0.903914,-0.913915,5.216399,-6.394017,-8.836353,-4.226097,5.875370,-1.430935,-9.280098,1.890736,9.690652,-8.154926,9.516381,7.417934,-3.580954,3.005063,9.755045,4.978809,-4.815921,4.811194,-3.736799,-0.697440,5.651497,0.176804,-2.945198,-0.370743,-9.902531,-3.252830,9.931283,-7.234840,9.374908,0.633138,7.354119,7.918185,-7.940330,-3.978128,6.732556,-3.946937,7.892749,-6.428051,5.589788,9.433629,0.296598,2.650484,-3.755723,-3.473363,9.178240,-2.014445,-5.996614,-1.006213,-9.561308,8.500119,-7.591054,9.209047,6.229980,2.891017,-1.696553,2.473200,-2.488012,-2.029023,-8.515019,5.503610,0.862533,-5.889072,1.585506,-7.326672,-4.229665,5.917211,-6.214667,-1.351588,-6.629954], dtype = "float64")#candidate|4193|(400,)|const|float64
call_4192 = relay.TupleGetItem(func_2119_call(relay.reshape(const_4193.astype('float64'), [400,])), 1)
call_4194 = relay.TupleGetItem(func_2122_call(relay.reshape(const_4193.astype('float64'), [400,])), 1)
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_4195 = func_1184_call()
call_4196 = func_1184_call()
output = relay.Tuple([call_4155,call_4192,const_4193,call_4195,])
output2 = relay.Tuple([call_4156,call_4194,const_4193,call_4196,])
func_4197 = relay.Function([], output)
mod['func_4197'] = func_4197
mod = relay.transform.InferType()(mod)
output = func_4197()
func_4198 = relay.Function([], output)
mutated_mod['func_4198'] = func_4198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_4233 = relay.TupleGetItem(func_1120_call(), 0)
call_4234 = relay.TupleGetItem(func_1121_call(), 0)
func_4002_call = mod.get_global_var('func_4002')
func_4003_call = mutated_mod.get_global_var('func_4003')
call_4237 = func_4002_call()
call_4238 = func_4002_call()
uop_4241 = relay.atan(call_4237.astype('float32')) # shape=(2, 9, 4)
uop_4243 = relay.atan(call_4238.astype('float32')) # shape=(2, 9, 4)
output = relay.Tuple([call_4233,uop_4241,])
output2 = relay.Tuple([call_4234,uop_4243,])
func_4252 = relay.Function([], output)
mod['func_4252'] = func_4252
mod = relay.transform.InferType()(mod)
mutated_mod['func_4252'] = func_4252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4252_call = mutated_mod.get_global_var('func_4252')
call_4253 = func_4252_call()
output = call_4253
func_4254 = relay.Function([], output)
mutated_mod['func_4254'] = func_4254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3931_call = mod.get_global_var('func_3931')
func_3932_call = mutated_mod.get_global_var('func_3932')
call_4282 = relay.TupleGetItem(func_3931_call(), 0)
call_4283 = relay.TupleGetItem(func_3932_call(), 0)
output = relay.Tuple([call_4282,])
output2 = relay.Tuple([call_4283,])
func_4288 = relay.Function([], output)
mod['func_4288'] = func_4288
mod = relay.transform.InferType()(mod)
output = func_4288()
func_4289 = relay.Function([], output)
mutated_mod['func_4289'] = func_4289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_4298 = relay.TupleGetItem(func_2815_call(), 1)
call_4299 = relay.TupleGetItem(func_2816_call(), 1)
output = call_4298
output2 = call_4299
func_4301 = relay.Function([], output)
mod['func_4301'] = func_4301
mod = relay.transform.InferType()(mod)
mutated_mod['func_4301'] = func_4301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4301_call = mutated_mod.get_global_var('func_4301')
call_4302 = func_4301_call()
output = call_4302
func_4303 = relay.Function([], output)
mutated_mod['func_4303'] = func_4303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4288_call = mod.get_global_var('func_4288')
func_4289_call = mutated_mod.get_global_var('func_4289')
call_4384 = relay.TupleGetItem(func_4288_call(), 0)
call_4385 = relay.TupleGetItem(func_4289_call(), 0)
output = relay.Tuple([call_4384,])
output2 = relay.Tuple([call_4385,])
func_4402 = relay.Function([], output)
mod['func_4402'] = func_4402
mod = relay.transform.InferType()(mod)
output = func_4402()
func_4403 = relay.Function([], output)
mutated_mod['func_4403'] = func_4403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4027_call = mod.get_global_var('func_4027')
func_4029_call = mutated_mod.get_global_var('func_4029')
call_4425 = func_4027_call()
call_4426 = func_4027_call()
func_1340_call = mod.get_global_var('func_1340')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_4432 = relay.TupleGetItem(func_1340_call(), 1)
call_4433 = relay.TupleGetItem(func_1341_call(), 1)
output = relay.Tuple([call_4425,call_4432,])
output2 = relay.Tuple([call_4426,call_4433,])
func_4436 = relay.Function([], output)
mod['func_4436'] = func_4436
mod = relay.transform.InferType()(mod)
mutated_mod['func_4436'] = func_4436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4436_call = mutated_mod.get_global_var('func_4436')
call_4437 = func_4436_call()
output = call_4437
func_4438 = relay.Function([], output)
mutated_mod['func_4438'] = func_4438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_4463 = relay.TupleGetItem(func_1104_call(), 0)
call_4464 = relay.TupleGetItem(func_1105_call(), 0)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_4467 = relay.TupleGetItem(func_2815_call(), 1)
call_4468 = relay.TupleGetItem(func_2816_call(), 1)
output = relay.Tuple([call_4463,call_4467,])
output2 = relay.Tuple([call_4464,call_4468,])
func_4476 = relay.Function([], output)
mod['func_4476'] = func_4476
mod = relay.transform.InferType()(mod)
output = func_4476()
func_4477 = relay.Function([], output)
mutated_mod['func_4477'] = func_4477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_4488 = func_1184_call()
call_4489 = func_1184_call()
func_1368_call = mod.get_global_var('func_1368')
func_1370_call = mutated_mod.get_global_var('func_1370')
call_4509 = func_1368_call()
call_4510 = func_1368_call()
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
call_4527 = relay.TupleGetItem(func_1989_call(), 0)
call_4528 = relay.TupleGetItem(func_1991_call(), 0)
output = relay.Tuple([call_4488,call_4509,call_4527,])
output2 = relay.Tuple([call_4489,call_4510,call_4528,])
func_4529 = relay.Function([], output)
mod['func_4529'] = func_4529
mod = relay.transform.InferType()(mod)
output = func_4529()
func_4530 = relay.Function([], output)
mutated_mod['func_4530'] = func_4530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
call_4557 = relay.TupleGetItem(func_1989_call(), 0)
call_4558 = relay.TupleGetItem(func_1991_call(), 0)
func_1723_call = mod.get_global_var('func_1723')
func_1729_call = mutated_mod.get_global_var('func_1729')
const_4564 = relay.const([-7.224674,6.491457,6.880102,7.525862,-8.285196,-0.831729,8.050870,0.186761,8.167521,-1.951977,-4.604194,0.657298,-6.817742,1.863956,-5.705650,0.635891,-3.828543,-0.982502,4.871310,-0.240468,4.731085,5.240346,9.133584,0.753035], dtype = "float64")#candidate|4564|(24,)|const|float64
const_4565 = relay.const([-5,2,10,-9,-7,1,9,-10,-10,10,-10,4,9,-9,5,6,6,9,3,-4,-1,4,-7,-6,7,-6,-4,6], dtype = "int8")#candidate|4565|(28,)|const|int8
var_4566 = relay.var("var_4566", dtype = "int32", shape = (840,))#candidate|4566|(840,)|var|int32
call_4563 = relay.TupleGetItem(func_1723_call(relay.reshape(const_4564.astype('float64'), [2, 12]), relay.reshape(const_4565.astype('int8'), [1, 28]), relay.reshape(var_4566.astype('int32'), [6, 140]), relay.reshape(var_4566.astype('int32'), [6, 140]), ), 8)
call_4567 = relay.TupleGetItem(func_1729_call(relay.reshape(const_4564.astype('float64'), [2, 12]), relay.reshape(const_4565.astype('int8'), [1, 28]), relay.reshape(var_4566.astype('int32'), [6, 140]), relay.reshape(var_4566.astype('int32'), [6, 140]), ), 8)
func_4529_call = mod.get_global_var('func_4529')
func_4530_call = mutated_mod.get_global_var('func_4530')
call_4571 = relay.TupleGetItem(func_4529_call(), 1)
call_4572 = relay.TupleGetItem(func_4530_call(), 1)
func_1449_call = mod.get_global_var('func_1449')
func_1451_call = mutated_mod.get_global_var('func_1451')
call_4591 = relay.TupleGetItem(func_1449_call(), 0)
call_4592 = relay.TupleGetItem(func_1451_call(), 0)
func_4476_call = mod.get_global_var('func_4476')
func_4477_call = mutated_mod.get_global_var('func_4477')
call_4597 = relay.TupleGetItem(func_4476_call(), 0)
call_4598 = relay.TupleGetItem(func_4477_call(), 0)
func_4106_call = mod.get_global_var('func_4106')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_4618 = relay.TupleGetItem(func_4106_call(), 0)
call_4619 = relay.TupleGetItem(func_4108_call(), 0)
output = relay.Tuple([call_4557,call_4563,const_4564,const_4565,var_4566,call_4571,call_4591,call_4597,call_4618,])
output2 = relay.Tuple([call_4558,call_4567,const_4564,const_4565,var_4566,call_4572,call_4592,call_4598,call_4619,])
func_4695 = relay.Function([var_4566,], output)
mod['func_4695'] = func_4695
mod = relay.transform.InferType()(mod)
var_4696 = relay.var("var_4696", dtype = "int32", shape = (840,))#candidate|4696|(840,)|var|int32
output = func_4695(var_4696)
func_4697 = relay.Function([var_4696], output)
mutated_mod['func_4697'] = func_4697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2035_call = mod.get_global_var('func_2035')
func_2036_call = mutated_mod.get_global_var('func_2036')
call_4721 = func_2035_call()
call_4722 = func_2035_call()
output = call_4721
output2 = call_4722
func_4763 = relay.Function([], output)
mod['func_4763'] = func_4763
mod = relay.transform.InferType()(mod)
mutated_mod['func_4763'] = func_4763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4763_call = mutated_mod.get_global_var('func_4763')
call_4764 = func_4763_call()
output = call_4764
func_4765 = relay.Function([], output)
mutated_mod['func_4765'] = func_4765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_4836 = relay.TupleGetItem(func_3129_call(), 0)
call_4837 = relay.TupleGetItem(func_3131_call(), 0)
func_4002_call = mod.get_global_var('func_4002')
func_4003_call = mutated_mod.get_global_var('func_4003')
call_4840 = func_4002_call()
call_4841 = func_4002_call()
output = relay.Tuple([call_4836,call_4840,])
output2 = relay.Tuple([call_4837,call_4841,])
func_4845 = relay.Function([], output)
mod['func_4845'] = func_4845
mod = relay.transform.InferType()(mod)
mutated_mod['func_4845'] = func_4845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4845_call = mutated_mod.get_global_var('func_4845')
call_4846 = func_4845_call()
output = call_4846
func_4847 = relay.Function([], output)
mutated_mod['func_4847'] = func_4847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4436_call = mod.get_global_var('func_4436')
func_4438_call = mutated_mod.get_global_var('func_4438')
call_4882 = relay.TupleGetItem(func_4436_call(), 1)
call_4883 = relay.TupleGetItem(func_4438_call(), 1)
output = relay.Tuple([call_4882,])
output2 = relay.Tuple([call_4883,])
func_4907 = relay.Function([], output)
mod['func_4907'] = func_4907
mod = relay.transform.InferType()(mod)
mutated_mod['func_4907'] = func_4907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mutated_mod.get_global_var('func_4907')
call_4908 = func_4907_call()
output = call_4908
func_4909 = relay.Function([], output)
mutated_mod['func_4909'] = func_4909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1340_call = mod.get_global_var('func_1340')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_4937 = relay.TupleGetItem(func_1340_call(), 1)
call_4938 = relay.TupleGetItem(func_1341_call(), 1)
func_3583_call = mod.get_global_var('func_3583')
func_3589_call = mutated_mod.get_global_var('func_3589')
const_4940 = relay.const([8.277350,7.298022,-8.119968,3.765567,-0.057111,-5.839836,0.587561,-5.826454,7.799119,3.636003,-4.551692,-1.987205,4.156247,1.517689,9.562308,-3.117376,8.343771,7.570176,3.915548,1.949508,-6.410949,4.602847,5.012961,-9.170579], dtype = "float64")#candidate|4940|(24,)|const|float64
var_4941 = relay.var("var_4941", dtype = "int32", shape = (840,))#candidate|4941|(840,)|var|int32
const_4942 = relay.const([[3.562765,3.080730,0.830886,-5.347122,6.766239,5.150130,6.810911,-2.339294,7.587883,-1.925195,2.260160,6.028599,-7.643372,-9.012630,-2.021837,-9.379359,-5.949967,7.223714,-3.836708,-9.723436,-2.890270,9.661318,-3.657727,-1.708475,1.858442,7.273961,-8.473445,2.589638,1.807444,4.149160,9.998705,3.252310,-0.795584,2.293152,-6.117468,-8.496866,2.774929,0.880758,0.628400,5.498790,-3.731890,1.599278,-8.148408,4.644708,4.931390,5.530928,-3.105402,-9.005957,4.824556,-2.307609,-9.355997,-5.086020,-6.238064,8.199357,-4.923238,-7.578135,8.930090,7.273015,-8.591440,5.495365,6.230030,-8.398922,2.380659,-2.414476,-1.706922,3.689740,2.628471,-4.217232,3.292678,-3.121708,-9.918770,-4.276389,-4.954946,9.305284,2.982493,-6.615564,7.615784,-9.584213,-6.127062,-0.959007,9.330151,3.773913,8.818632,-2.719949,7.841846,-5.184088,5.670792,6.860719,-6.941174,-6.513898,0.416550,4.643144,3.490596,3.702767,-3.035213,-1.811150,1.048729,3.536231,9.724579,5.605306,-5.260862,0.534154,3.132237,1.229354,5.502770,9.599502,2.864083,-7.145270,-6.259041,-9.584008,9.012480,5.912990,-8.984169,5.937383,-3.008017,-4.260896,9.542619,6.949164,-3.870452,-0.575589,-9.758151,-0.228930,-7.525321,6.082707,-2.867348,-9.627490,-7.190630,7.053825,-4.563547,1.309822,3.221093,0.737137,3.708357,4.998958,8.085289,1.847726,0.876735,7.040426,-3.152023,7.796184,-0.136581,-8.548316,3.278718,8.189080,0.900569,-0.927616,-0.219149,7.996078,-0.903204,6.487687,-3.344287,-3.534601,-0.133471,-1.772145,-9.600570,-4.667162,9.083001,2.295862,-7.888545,-5.707429,9.755555,-2.602688,-1.657939,3.307988,7.558092],[-5.468545,-6.245956,2.121607,0.609890,0.985704,4.089966,-7.304979,3.126820,2.739386,0.290236,2.884762,3.307103,-1.323767,4.068920,-7.418827,9.806642,-2.221989,1.818270,-8.316250,9.006908,-2.896002,1.848577,1.078869,9.526625,-3.004180,-3.088237,3.849193,-7.927386,7.297904,-1.545106,-7.697675,1.096542,6.270057,-1.616384,2.761384,8.118652,0.778092,-7.696538,4.031916,1.713495,-6.868134,3.618326,9.255181,-8.565604,8.191461,8.804750,-4.552337,2.551884,3.650837,5.587675,2.872806,9.848589,-2.625627,-1.482709,5.280606,8.564802,3.759603,4.570946,-1.589964,-8.194052,-4.648251,3.604487,-0.336649,-5.037455,5.232973,-2.492368,9.477551,0.764507,2.193130,2.694632,8.823325,2.956416,-6.103512,-7.952870,-5.765807,-1.422323,-5.147583,9.325135,-2.048613,-0.806364,9.397567,9.867100,-5.818028,-3.324554,-5.202742,-7.847999,5.715024,-7.798867,3.859033,-2.267996,4.733571,-2.536782,5.124182,-3.911665,-8.326858,9.427637,5.259736,-4.265141,4.463123,-3.769753,-1.440128,2.545198,-4.284725,5.377927,-4.879472,6.887444,9.762757,0.458166,1.734954,-3.515918,4.432250,0.306587,-6.624794,-5.309977,5.485587,4.974295,-0.720846,3.612517,6.191472,-7.456571,-1.507821,6.635337,0.585782,-2.401889,5.254068,-3.991353,-8.145156,3.114284,1.420438,-3.363398,-3.900167,2.176908,0.343982,0.521814,5.275912,-0.421641,3.468076,7.296888,6.237338,4.907511,4.720958,7.406524,-4.690708,-7.555660,-2.983982,-8.982168,3.571711,5.267569,-4.753289,4.247185,-0.193285,7.652676,4.262362,8.511500,4.639666,1.271503,-7.746642,-7.540096,-8.631216,6.697450,-9.914752,2.522984,7.729128,-0.675722,-6.184550],[7.567201,1.127326,-5.384077,-0.987664,8.714023,7.708970,-0.971430,5.858875,-8.949300,2.654752,1.556539,3.960981,7.775301,4.148184,-2.045911,6.881498,1.846818,-5.770137,-3.531947,0.465479,-0.170612,-8.661890,-1.610795,-9.984050,7.905219,-2.538218,9.219181,-2.271041,-4.499881,-0.260257,2.277044,5.142517,-8.327537,-4.360506,-0.088877,7.227503,-8.030535,9.355080,6.842187,0.168270,6.835071,3.178315,3.423162,-9.573789,-4.406740,-0.914367,-4.485226,-2.569750,-7.566948,4.785892,-6.052414,1.066475,3.218273,4.289275,-3.705273,6.773084,9.483010,-4.003733,-7.706916,-1.564962,6.387714,-0.760962,-8.299755,6.951499,-1.690239,2.646518,2.133685,7.653724,3.447007,2.367263,-0.879067,-1.489709,-2.335701,-6.407475,0.456261,3.648896,-8.213864,-7.104422,-4.144687,0.797493,6.014266,6.525820,8.749903,9.297475,5.033742,3.232477,7.543630,4.330554,-9.236258,4.365167,8.772996,6.798788,-1.175849,-0.999544,1.077840,0.678498,0.342810,9.457300,-9.672513,9.236595,5.121347,6.082266,-5.694719,-2.196915,-5.396378,-8.252584,-4.255719,4.937158,-0.149574,3.189873,8.566225,-7.478342,1.597216,-0.504894,-9.331586,-7.958070,-2.420782,-7.588098,-1.795700,6.550699,-9.850431,-5.755616,2.760362,-5.423332,-7.816118,1.654491,-2.529492,-4.469532,8.657920,8.021787,-8.409190,-7.180332,9.572027,-0.514349,6.210486,9.310398,5.411179,3.863525,5.893495,-4.343575,3.077849,-1.471435,6.823592,-7.341475,3.063214,-5.833476,8.067842,-3.913470,-9.189898,-9.127376,-6.105769,5.060749,-1.531934,3.283474,-5.823089,6.972005,8.669827,-5.629409,-2.421220,-2.382832,-4.735112,2.258479,1.267724,7.578389,-9.016835],[6.897712,4.617139,4.527604,5.969083,4.548991,-1.813054,-3.245218,-1.175606,6.251260,6.536597,-9.910116,-4.262337,2.792653,0.092494,2.596594,-8.579147,7.152025,-6.151882,4.814337,5.403041,6.310243,7.702548,9.170147,-9.837124,-2.996855,-1.772092,-7.207676,3.719830,-2.168389,-4.030881,-1.429435,2.807032,-1.686257,-6.605223,4.550678,-5.459180,-1.170181,-8.723777,-9.696791,-7.240220,-5.871427,8.813530,3.725272,-9.498517,-2.721620,-6.503892,-0.239974,-8.941945,0.881398,-0.769179,-7.543988,1.648061,9.291229,-8.254214,9.313763,-4.138340,-1.725383,-2.302923,-4.228161,5.572341,4.993963,-0.861225,8.140087,-2.961669,8.711259,-6.840735,2.567139,-4.243821,2.621314,-5.747524,4.373824,8.752054,8.475321,-1.504968,-3.521603,-9.361459,5.345247,8.018706,3.735424,2.612529,1.508859,-4.654876,6.386249,1.278507,1.008824,2.035084,-0.833413,-5.503877,-9.172742,-0.303182,8.394963,-9.834403,4.664792,3.685062,6.061837,0.291565,-4.311899,-0.136080,3.808340,9.884800,8.055438,4.826377,1.271309,1.351475,-4.615270,-8.679155,-7.429670,-1.302125,0.036039,-5.434153,-7.549516,8.921948,4.494979,7.934451,5.609382,-3.063710,8.253298,-8.594884,5.680496,4.135478,5.870304,5.071739,-9.765690,1.008885,-6.637378,4.926152,-0.456130,5.463949,-6.174391,-7.162100,1.256076,-0.312275,-4.439465,0.873890,1.488082,-7.162086,4.426504,-8.574644,1.770668,0.461094,-6.843459,1.964741,6.360712,-5.513013,9.777229,8.558994,6.101026,5.139693,-6.043780,-7.018072,9.809081,3.530473,-4.887485,0.947134,8.047758,4.908389,3.433964,-7.205304,-6.732836,-6.370392,4.427613,-7.910622,6.629461,1.873596,2.494048],[2.014029,-3.205566,7.349826,4.189856,-4.167656,9.061422,-1.770775,-4.552712,9.054698,3.992987,-8.203596,1.022271,-2.067356,7.107403,-3.347111,2.537080,7.688864,-1.761212,-8.605893,1.738695,6.631011,2.622590,4.258894,-3.261524,-8.693971,-3.559596,6.061118,6.917005,1.021596,2.304887,0.085767,7.823439,-3.296364,4.567498,3.416878,1.353503,8.838165,-9.535981,2.679972,2.189217,4.180209,-7.868354,9.939316,-8.229576,-0.838049,9.089233,-0.488774,9.838027,-5.830956,0.540473,6.716999,-1.170487,4.260216,-6.132574,-0.561223,-1.221535,8.658403,-2.108104,1.361320,7.568768,-9.322109,3.241634,-2.978714,7.308891,-6.584178,-2.989018,1.522140,-3.912940,-6.698968,8.925195,3.229850,-1.899088,0.039429,3.669192,0.773192,-9.040954,0.656957,-3.173195,-9.281914,5.305135,-3.785927,0.665244,-0.283948,0.020334,-5.701479,6.164448,-2.716763,-5.769009,-2.859310,-6.426827,1.759620,4.080708,8.899776,-8.578516,7.646323,-9.601941,2.038328,-7.950790,8.396438,-8.346844,-2.645909,6.761914,4.538377,-7.152028,-8.615393,3.929158,-8.559690,-8.329579,-1.981795,0.545604,-3.916414,-0.239215,6.818792,-5.965821,-0.015935,-8.780556,-8.882834,3.868998,-1.827201,-3.796443,3.159973,-4.372023,-6.659108,0.436145,3.127108,0.414196,-1.165131,4.821662,-7.435725,-5.534246,5.462087,3.013167,8.367976,9.810483,5.081894,-8.468201,-8.268960,-0.075270,9.044575,0.710953,-6.740339,6.471811,-5.748208,4.646487,-8.664458,4.476656,-8.104855,2.721106,-7.791575,0.200985,-3.707152,-9.158218,-3.567124,-6.992992,-9.993061,-6.482993,-9.995870,5.018266,0.612528,3.591197,-0.927506,2.658230,6.451536,-5.812253,0.713352],[2.031294,0.594139,-9.734797,-4.452479,-0.191397,2.716498,-4.788270,-5.739615,-5.432296,-5.348665,9.082449,5.816384,2.505480,3.276626,-0.431699,-2.242377,3.115293,0.297259,6.950687,-8.370877,-3.674730,8.600588,1.151091,-7.415680,7.760045,4.795112,6.286142,9.677531,1.176912,7.413680,1.530211,-5.098264,3.290313,3.208476,8.628043,-5.340878,6.208097,-2.229680,2.125711,-0.915669,6.411176,2.938079,-3.406526,-8.558034,-6.172200,3.608303,8.418021,-8.278485,5.972699,1.738422,6.044968,-5.737827,1.071486,2.423943,4.127449,1.422901,2.437684,-2.694982,0.823341,2.455448,-1.980488,-8.451013,-9.787115,-6.189725,-9.706612,5.999416,-2.300713,-3.498720,-3.282392,-7.327926,5.195013,1.997157,5.812861,0.735740,-7.078845,-4.467316,6.375986,-8.522132,0.797418,-9.477798,-0.105427,5.375153,9.558199,7.940390,7.285198,-7.797371,7.234212,0.243084,0.933364,-7.331041,2.343572,-4.462915,5.180915,3.205498,8.300709,-3.743846,8.142171,-8.822727,5.569592,-2.509025,-3.447655,6.037396,-4.168105,-6.546055,0.944674,6.885799,5.535165,-2.925409,-9.169836,3.148301,9.958669,-7.486506,6.079667,8.525632,-5.444165,9.108355,-0.269950,-3.417356,6.340108,-8.893898,5.635148,6.523771,8.138421,6.533299,3.368132,-2.727577,-6.049751,1.316848,2.886622,-0.629807,2.326825,-4.142263,8.067115,-4.985158,9.495436,8.858532,7.716570,2.227324,-0.428929,-7.495915,0.609070,-1.653113,4.424940,5.723865,9.154051,-7.366578,5.528291,-9.552724,-3.175345,7.992175,-7.448923,-2.815901,-6.631053,-7.324711,2.617974,-4.647798,9.182373,-7.256491,1.169552,-2.454146,-4.827108,7.647228,3.251596,-0.446331,-7.411019],[-9.929434,-9.194015,-7.595551,-8.913083,-5.295189,-6.121365,8.499472,5.930731,-1.402251,8.214526,1.205731,-8.728883,-7.209865,6.385725,7.624750,-9.903665,-1.240811,-2.665915,5.077827,0.331007,-2.113527,7.684596,-6.102753,-1.215718,4.319376,2.082578,6.311876,3.288648,1.777730,-4.180257,-5.048111,-4.620311,6.881921,-7.727972,-1.338283,-0.676961,8.891849,-0.136889,1.108757,-0.392577,-2.948693,5.366510,1.908150,5.233238,8.927258,5.490468,5.171775,-2.936859,6.243384,7.956001,0.804282,-7.635335,1.879791,-2.611701,8.670978,5.826043,-8.462601,7.917769,8.713548,-5.954337,-7.752430,0.769386,-5.637379,8.978134,-4.555328,3.086784,-2.572588,-4.275737,-3.711701,-8.126188,2.133074,0.907554,3.472249,-9.999384,-0.949082,5.243637,-6.930046,-0.491702,8.691684,-2.249294,-8.891167,2.667662,-4.220699,2.756317,-4.715864,-5.971214,6.230631,4.185723,3.156964,-6.017069,-2.530138,-2.833132,-5.745957,0.771699,-9.947293,6.456831,8.629388,-2.335496,-7.504334,-0.089547,2.596250,-6.943824,8.065090,1.087136,6.874829,-3.184435,-1.435058,5.568235,6.500232,-9.086406,-1.715098,-2.222024,-8.114412,8.378951,-5.880304,6.392689,1.060527,9.078590,1.967537,6.599212,-9.720957,-7.262717,-8.781760,5.221386,3.558543,-8.539370,1.922924,3.365054,8.622945,-8.642834,6.341792,5.192885,8.344337,4.803356,-8.212330,-1.706217,-3.254050,9.972463,-6.001375,-9.969812,-2.282887,8.332098,6.612116,1.478261,-6.041011,9.242443,8.932428,-7.516384,9.300767,3.950206,-6.863400,-9.635169,-7.183051,6.928627,-4.589582,-9.298413,-9.450565,-3.029524,8.357003,-4.062147,1.101068,8.317298,5.901516,7.427262,6.300364],[-3.876117,-1.334475,-1.644545,-7.649072,3.061150,5.782055,9.193476,-4.668029,8.069092,6.086163,0.235969,0.551959,0.805742,-0.135954,2.947436,4.827107,4.908112,-8.011877,-4.446021,8.509725,8.784895,-4.648963,7.413505,-2.526432,-0.641085,-5.811926,-8.919561,-1.147426,-6.261964,6.964506,-4.552491,9.623202,-6.829676,5.454884,-0.936445,4.101899,8.242208,-0.751306,-0.025675,8.313737,-1.587945,-5.504411,-4.260675,-3.242967,4.172183,-9.766510,-9.154418,9.068287,-8.350898,-5.662341,1.722054,-3.349126,1.795496,6.709582,-4.722773,-2.052978,8.725929,0.126887,1.966099,-7.622483,7.842302,-9.712362,1.058964,5.981344,-6.556078,-0.547124,8.844744,-1.638497,-9.264649,-0.641395,-0.256548,2.097427,0.121110,9.944959,2.164132,0.086762,1.459270,-9.855047,5.829127,-4.566694,2.305168,6.290106,0.767309,6.936574,-3.633940,-1.215035,-2.382705,-8.950607,0.321564,-0.109787,6.137583,1.759036,5.581739,7.466090,4.042678,-4.127997,8.982093,0.443020,8.916441,-0.737120,-5.088529,7.761286,-7.246660,-8.013555,3.296032,-9.542920,-9.137531,2.104333,-2.334967,-9.834603,-9.122494,-4.796885,2.819651,4.096427,7.966709,-1.462290,-4.260247,-1.267403,6.723477,-1.902206,-4.741971,3.247280,6.320002,-1.053499,-6.330978,2.231564,-4.798616,-2.200601,-6.255853,-9.353640,8.966935,0.253652,-6.267440,-5.393025,1.716164,0.060046,-2.735931,-1.111144,0.222266,5.638544,-5.699286,6.091545,-7.761815,-9.794614,2.088916,-6.933049,2.193691,-8.545930,-7.238339,9.416677,-1.150495,2.765693,0.590090,-7.701688,-5.909326,-4.243590,-9.227168,9.341292,8.080001,3.898114,4.583825,5.612775,-5.831513,-7.423432,3.748176],[-3.609019,-2.291186,-8.271828,3.599522,4.244484,-6.416291,-4.387183,3.057107,2.840286,3.560823,1.645785,1.865971,3.976109,-7.091043,-7.307471,4.885654,6.722489,-5.115822,-6.886358,-1.934000,4.642370,6.680578,-7.269530,-5.394196,-1.200433,-1.709289,-0.435875,-5.683969,5.376156,0.460309,-7.687242,-4.701481,5.558816,9.234890,4.512075,0.378589,-1.635767,-4.106291,8.255498,3.097007,1.747766,2.622051,9.376872,2.360120,-3.178165,-2.959731,-3.200943,4.327990,3.983401,0.643538,-1.390619,9.430169,7.936084,8.731689,-7.577655,-3.728208,5.125942,0.749372,-7.579240,9.490396,-5.964351,9.053715,1.651443,-2.775797,-3.871336,2.438477,-0.275907,0.739090,-2.356901,-6.213586,6.822707,-7.397144,-8.408171,2.870332,6.334541,0.199615,-2.364996,-8.010758,4.788234,-2.048192,-7.000229,8.953045,3.485450,-3.790954,3.961310,-6.690963,-1.413793,6.302927,6.144080,2.137364,-0.332896,-0.574584,1.957780,-9.429053,5.445576,-1.476764,-0.737830,-4.252153,5.225446,9.272690,7.348812,0.056346,0.273325,-3.864918,-2.209635,8.872532,-1.933686,4.014687,-9.042037,0.366137,4.252136,3.894611,2.154126,3.436909,-3.022884,2.780749,-6.771121,5.930535,-0.140671,-9.243294,9.692987,6.187363,9.444483,-9.362136,-4.976494,4.881938,8.892853,5.749803,-4.224285,0.620903,0.642241,-9.738223,-3.353386,0.209428,7.934053,4.336254,8.678975,7.450088,0.620740,-8.205947,1.401134,7.802931,-0.210839,4.072728,0.514215,-1.235605,9.703545,4.077132,-4.417816,-1.454238,-9.246391,1.814960,-0.292742,1.921629,-4.941831,5.687259,1.926618,-5.178714,8.829817,4.195280,0.893155,-9.397526,-5.848012,-0.501148,-0.768484],[9.332201,-6.164709,0.347098,2.499986,-1.522734,-9.361303,1.475221,3.594054,-0.152806,3.626751,1.980385,1.374250,1.010256,7.406185,-9.894204,9.281283,9.168689,-1.562461,-7.045630,4.062306,9.993564,6.519389,3.937229,7.534418,1.718256,1.281920,7.644369,-8.504076,5.867732,-6.549622,-3.535875,2.485938,2.684341,-1.248102,5.286648,-3.150593,2.515590,6.569043,-6.354992,-4.851556,0.740783,8.656452,-6.316465,4.593498,1.870413,-4.892689,7.072776,9.647368,4.537641,1.755852,9.077532,-2.736798,8.532264,-1.102767,-4.886614,3.194245,-0.072717,-0.712436,9.932113,-0.186459,5.681551,-1.142036,-5.602474,2.857861,3.516622,-6.531471,-4.005568,8.650104,-1.302182,-1.098326,1.005420,-1.191260,-2.625863,-1.383981,5.886625,-1.902193,1.363393,6.498897,8.005276,-2.031700,3.086596,2.944511,6.278653,1.125732,-8.095441,-6.852631,-3.362266,-4.544455,8.398061,-1.756682,3.525760,9.355860,8.722466,8.054353,2.082460,9.148415,-2.868094,-1.638438,9.963807,-8.434702,7.705106,9.168402,8.277182,-0.472724,6.744551,7.636215,-9.747027,5.480578,-5.701743,-1.496586,-3.010545,-2.733818,-2.809486,-9.169994,4.889886,-1.138413,3.375855,-8.362623,1.009018,8.008704,0.916502,2.398050,2.856549,9.501580,9.811933,9.283274,5.526422,6.873938,9.966097,7.422830,-3.028403,7.610520,-9.955615,-4.308739,0.535762,-8.725071,7.773825,-2.509133,-3.331632,-8.015696,6.391688,-4.307218,2.135490,-8.481184,7.986836,0.217161,8.413753,-4.444288,-4.083955,8.020834,-1.469650,-8.773355,-1.361305,5.959245,-1.806621,-7.108468,7.670743,-7.950340,-9.734978,0.115792,9.471014,6.744754,-8.258739,-6.945485,0.048889],[-2.142482,2.074602,0.713070,3.065413,-1.706648,-2.216971,6.086171,2.053664,-5.154088,-0.289245,-2.766892,6.532474,9.265990,0.521102,-5.038772,9.148097,-9.682795,-6.807640,-1.207859,-3.855170,3.116853,-7.990636,2.634346,9.101608,4.706612,7.473200,9.163683,-0.002374,-8.792281,-4.657793,-3.549752,6.632947,-7.955377,-6.765336,6.845925,7.032957,1.930378,6.888310,-5.782566,-4.261128,5.150067,6.280145,-7.416877,9.813866,5.586628,-9.540439,5.572362,-9.204562,1.175863,6.993680,-9.015646,0.365108,-5.122756,-8.179862,0.809745,-4.316742,-4.659114,7.788975,1.998340,-6.681524,-6.082148,-8.252676,-9.474256,6.118450,9.462141,0.792089,-5.195407,1.632341,6.835931,6.138830,6.022044,9.829547,7.340183,-9.027253,9.039830,1.652331,5.737577,-6.287484,-5.692938,7.920744,-6.501701,3.067858,-3.759396,8.577064,-7.440294,-0.260801,-8.267764,-6.811195,8.717992,1.241432,7.356307,-4.299184,-8.551342,-9.552025,9.719305,1.774143,-1.402634,-7.154977,7.463262,8.958048,-7.325253,6.270348,7.342396,-0.383412,2.162115,-5.768386,-8.041341,4.945283,8.652643,4.349968,-4.304118,-5.683193,-4.740794,9.094589,-5.485021,9.482878,-9.023618,7.058799,-9.184735,-0.411504,6.248764,-6.920344,-4.673400,5.655026,-1.481607,-3.388792,6.112498,0.496457,0.722572,7.100957,6.132534,-0.573974,-2.955962,-6.775106,0.192437,-0.684584,2.012279,-5.820043,-7.960631,6.904794,-3.340884,9.970384,-3.880953,7.264279,0.847536,4.958694,-8.677614,0.071386,6.468480,3.017685,-5.704036,-4.012394,6.130739,0.424961,-7.362732,-0.181562,-8.185791,-5.975385,-9.014870,-6.808096,-4.821263,8.640861,9.389051,9.157792,-3.570067],[4.859308,-6.559098,-4.394135,-4.703073,-7.418219,-3.319517,-6.971223,-6.367697,8.885200,-0.604193,9.825700,3.555693,4.458670,7.594650,3.180056,-8.578997,-0.810737,-2.851143,-9.955576,3.208424,1.882585,7.786696,-0.581247,-8.899065,-5.939192,-1.713141,-7.043709,-1.193719,-6.908149,-1.159461,4.781333,1.652620,-3.407112,-0.170014,-9.414901,4.355885,5.385018,7.180955,-1.847051,1.988875,1.595416,-9.344402,8.279704,2.032775,-8.480109,-7.839184,-6.290657,-2.552831,4.718752,8.848811,-9.609415,-1.032087,0.973542,4.170119,7.473418,3.929125,-3.003533,-7.612537,-1.423778,-6.641151,-8.204845,1.216111,-8.056648,6.426208,-6.448829,8.432144,6.021042,1.601799,-1.160938,-5.732447,1.511560,-0.728831,-9.342702,-5.245864,-2.757582,3.355125,1.650635,-1.293557,-4.379221,9.380796,-4.586281,1.925000,-0.070730,7.893745,-0.942308,9.355292,3.499764,9.480760,-6.664012,-4.204962,-7.932228,9.187295,-9.861366,8.946861,0.055066,-5.965386,-3.740720,6.334061,-5.285404,4.376920,8.155698,-2.038616,-2.731188,-2.295137,6.520147,7.432267,-4.675596,8.727891,-0.733409,-4.216294,-0.168605,-1.808922,-6.663066,3.901219,-8.412163,6.065032,5.299901,-6.768685,-9.734142,9.791117,3.997754,0.588218,6.956498,1.136059,-7.135081,-8.597180,-7.935230,8.148888,-6.992902,3.643653,4.416422,-6.633262,-0.243254,-7.768646,4.024604,0.830951,-1.807369,7.717213,4.956923,-8.801994,-6.846978,-7.549752,9.274464,3.149797,4.786173,-3.241689,-4.849995,5.332900,1.682822,3.015995,8.153762,7.874048,4.336327,-4.226813,5.045862,-4.273496,4.039557,-9.083885,-8.041461,-4.913518,-6.204502,-1.512753,-7.556327,-7.588742,4.499279],[-6.651984,-3.713867,1.615046,-8.005705,-5.584447,-1.176906,7.994655,-5.421609,-8.852190,-7.839936,-8.360923,6.423135,7.344779,-9.777726,0.389414,2.434395,9.895395,0.799046,3.470001,-7.503648,-7.799045,7.487354,-6.629820,1.155042,-8.162064,0.556739,8.041192,-5.002438,-3.587464,-9.744717,-2.336871,-8.009462,6.102627,-4.564326,0.690048,-1.115697,6.951406,-4.231184,6.550149,-5.125772,7.101889,-2.250704,-1.576025,9.896723,-7.075396,-9.417868,7.269515,-0.274279,9.778182,6.752291,1.897250,-6.665923,3.676037,-0.723813,-7.843479,7.763095,-1.672508,-7.847897,-3.987602,-8.839613,6.666250,1.933705,7.150454,1.102847,6.155446,1.708829,7.338911,9.059814,-9.325091,8.242329,8.472242,-0.725816,7.826518,-4.290753,-2.066151,-2.583548,-4.288469,-3.291331,5.821119,-3.051179,3.139554,4.350145,2.741565,5.857438,-4.695401,-7.943763,4.260674,1.964550,-9.748096,-6.330202,-3.390061,-2.155325,2.093132,-4.393650,2.423568,6.335673,4.612423,4.283778,1.523679,-1.867972,1.817694,2.930435,-3.994132,4.392847,5.022668,9.028280,-5.849547,-5.159069,0.093033,-3.994527,2.339229,9.887998,-2.929748,8.761030,4.999341,4.327548,-9.452336,-3.165029,-0.724389,2.459670,8.172892,2.189951,8.097024,8.448840,8.148679,1.920073,9.028258,7.177832,0.948780,-3.631250,-7.537034,8.945682,-4.826019,2.717992,-1.839640,-2.384087,-0.607351,8.529614,2.039523,-6.645888,1.704659,2.662144,-8.261699,-7.201335,2.638064,-2.510910,0.336432,0.828030,9.139878,-7.937632,9.975855,-6.008473,-5.021315,6.043573,-7.864416,-7.870591,5.163256,3.586607,-7.367757,3.275487,-0.705995,-8.741928,-0.371079,7.189995,-8.870451],[2.289989,4.753255,8.089051,3.011573,0.442797,-5.047412,6.850271,-4.019475,0.805356,5.082528,-4.433442,9.659394,6.838424,-3.063285,1.808921,-9.463457,1.478184,-8.054842,9.084199,7.660803,-7.113087,2.322446,-8.786350,-7.746367,-9.251758,-7.292974,7.839549,6.329424,6.823180,2.034381,1.954901,1.582005,8.162141,2.104012,-8.027586,-1.514274,9.652529,-7.255759,4.773964,1.284642,-7.744923,-8.580257,6.615129,-2.108421,-4.182859,-0.823306,6.873016,-6.401733,8.815382,-4.818411,-1.987352,-9.188330,-9.864921,1.579202,7.446352,5.677992,1.617684,4.803897,-4.166490,8.159255,-3.567849,-9.506129,-2.587482,-5.204361,-4.868066,8.055424,1.115822,-1.196675,-2.489292,9.260517,9.914448,-8.875614,5.580892,3.739236,0.189018,-6.653286,-1.810802,-7.831931,0.384263,3.170657,2.017325,-9.399488,-7.656207,-0.625711,5.811839,4.466277,-9.800733,8.285431,7.360744,2.407120,7.637913,-2.490326,-6.970482,-4.107863,-7.822661,-1.158571,-2.989532,-7.707946,7.869195,-0.753623,6.687330,6.944025,5.933063,3.122465,-8.489579,9.437672,-2.786167,2.500506,-5.432977,-6.952786,6.924002,-3.135606,1.206355,1.921719,5.849950,1.186774,3.179131,9.020236,7.277637,6.925610,9.034495,-8.777939,9.061439,9.728949,8.916483,-8.246786,-2.105623,8.266747,3.637349,-0.089865,-0.947968,7.533038,9.010282,-5.524899,1.901876,-0.683531,-4.241091,-4.353456,-3.182998,-2.886135,5.768975,2.168642,0.259185,-0.496969,4.115038,-4.979593,-9.558305,7.318616,-7.241814,0.069304,6.778166,-5.594838,-2.536908,9.875725,-1.478753,-2.634796,-8.683703,6.038050,-4.577319,6.884467,5.875447,7.309800,2.538497,2.473745,-4.340426],[-6.598850,-6.571966,-5.351722,3.360601,7.539122,4.862258,-0.359801,1.421424,3.983253,5.480220,5.372187,-9.243384,-5.983540,5.095116,4.902316,-9.984750,-1.297739,0.902394,4.840160,-7.054455,-4.206454,4.775819,-9.193888,7.389964,-3.802023,-9.609117,4.948898,4.782053,-2.102680,7.459050,-5.435230,1.028275,-5.367364,5.434613,-8.071085,-4.988807,2.476715,3.551717,3.216865,-3.011941,2.674770,2.645175,3.173438,-5.163440,-3.224191,-8.964551,-5.315915,4.655256,-6.807757,-9.967638,-5.920821,3.011740,-0.699465,4.706849,2.993286,-0.759274,-0.106314,8.904874,-8.519802,-8.379137,4.587804,2.830590,-2.377700,-6.234947,-3.321283,8.455587,-4.133849,-1.058122,7.974030,-3.804543,6.162590,6.025328,-0.701397,-2.495762,0.122828,9.617441,6.106630,-1.152044,8.476788,-1.821540,6.965563,1.156256,-6.004823,3.903047,5.380516,4.456562,-9.557956,8.762908,0.032620,6.262962,-5.422689,-7.641958,2.599435,7.855616,5.572448,-9.310426,-7.709106,-6.846361,-8.316021,-7.777897,2.286919,-9.608065,8.547116,3.402020,4.529116,3.307559,7.819981,2.854705,-1.300169,-8.580557,-2.265713,-5.014769,-6.217330,-0.708595,-6.214967,-0.312434,-9.980451,0.994063,-3.854751,-8.542910,3.174183,3.244729,3.776964,-2.079630,-2.508940,-3.750979,1.089805,4.224534,5.233493,-9.192766,-6.642907,-6.930370,-3.583063,-8.012553,-6.235103,-3.149630,-5.481903,-0.205197,6.954436,3.393267,4.411108,-4.782625,7.341705,-0.965301,8.140704,-5.421902,-3.514829,-8.861138,3.916748,8.553756,-0.205979,5.316393,-0.544505,-4.987751,-3.474553,0.354261,7.299057,4.152949,6.574816,-4.666570,-9.233061,-5.663423,3.376730,1.758169,-1.294792]], dtype = "float32")#candidate|4942|(15, 165)|const|float32
call_4939 = relay.TupleGetItem(func_3583_call(relay.reshape(call_4937.astype('float32'), [2, 9, 4]), relay.reshape(const_4940.astype('float64'), [6, 4]), relay.reshape(var_4941.astype('int32'), [840,]), relay.reshape(const_4942.astype('float32'), [825, 3]), ), 0)
call_4943 = relay.TupleGetItem(func_3589_call(relay.reshape(call_4937.astype('float32'), [2, 9, 4]), relay.reshape(const_4940.astype('float64'), [6, 4]), relay.reshape(var_4941.astype('int32'), [840,]), relay.reshape(const_4942.astype('float32'), [825, 3]), ), 0)
output = relay.Tuple([call_4937,call_4939,const_4940,var_4941,const_4942,])
output2 = relay.Tuple([call_4938,call_4943,const_4940,var_4941,const_4942,])
func_4956 = relay.Function([var_4941,], output)
mod['func_4956'] = func_4956
mod = relay.transform.InferType()(mod)
mutated_mod['func_4956'] = func_4956
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4957 = relay.var("var_4957", dtype = "int32", shape = (840,))#candidate|4957|(840,)|var|int32
func_4956_call = mutated_mod.get_global_var('func_4956')
call_4958 = func_4956_call(var_4957)
output = call_4958
func_4959 = relay.Function([var_4957], output)
mutated_mod['func_4959'] = func_4959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2397_call = mod.get_global_var('func_2397')
func_2398_call = mutated_mod.get_global_var('func_2398')
call_4987 = relay.TupleGetItem(func_2397_call(), 1)
call_4988 = relay.TupleGetItem(func_2398_call(), 1)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_5028 = relay.TupleGetItem(func_1120_call(), 0)
call_5029 = relay.TupleGetItem(func_1121_call(), 0)
output = relay.Tuple([call_4987,call_5028,])
output2 = relay.Tuple([call_4988,call_5029,])
func_5035 = relay.Function([], output)
mod['func_5035'] = func_5035
mod = relay.transform.InferType()(mod)
output = func_5035()
func_5036 = relay.Function([], output)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4002_call = mod.get_global_var('func_4002')
func_4003_call = mutated_mod.get_global_var('func_4003')
call_5047 = func_4002_call()
call_5048 = func_4002_call()
func_4106_call = mod.get_global_var('func_4106')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_5059 = relay.TupleGetItem(func_4106_call(), 0)
call_5060 = relay.TupleGetItem(func_4108_call(), 0)
output = relay.Tuple([call_5047,call_5059,])
output2 = relay.Tuple([call_5048,call_5060,])
func_5066 = relay.Function([], output)
mod['func_5066'] = func_5066
mod = relay.transform.InferType()(mod)
mutated_mod['func_5066'] = func_5066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5066_call = mutated_mod.get_global_var('func_5066')
call_5067 = func_5066_call()
output = call_5067
func_5068 = relay.Function([], output)
mutated_mod['func_5068'] = func_5068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_5069 = relay.TupleGetItem(func_1104_call(), 0)
call_5070 = relay.TupleGetItem(func_1105_call(), 0)
func_4301_call = mod.get_global_var('func_4301')
func_4303_call = mutated_mod.get_global_var('func_4303')
call_5080 = func_4301_call()
call_5081 = func_4301_call()
output = relay.Tuple([call_5069,call_5080,])
output2 = relay.Tuple([call_5070,call_5081,])
func_5088 = relay.Function([], output)
mod['func_5088'] = func_5088
mod = relay.transform.InferType()(mod)
mutated_mod['func_5088'] = func_5088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5088_call = mutated_mod.get_global_var('func_5088')
call_5089 = func_5088_call()
output = call_5089
func_5090 = relay.Function([], output)
mutated_mod['func_5090'] = func_5090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1934_call = mod.get_global_var('func_1934')
func_1936_call = mutated_mod.get_global_var('func_1936')
call_5144 = relay.TupleGetItem(func_1934_call(), 0)
call_5145 = relay.TupleGetItem(func_1936_call(), 0)
output = relay.Tuple([call_5144,])
output2 = relay.Tuple([call_5145,])
func_5155 = relay.Function([], output)
mod['func_5155'] = func_5155
mod = relay.transform.InferType()(mod)
mutated_mod['func_5155'] = func_5155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5155_call = mutated_mod.get_global_var('func_5155')
call_5156 = func_5155_call()
output = call_5156
func_5157 = relay.Function([], output)
mutated_mod['func_5157'] = func_5157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_5164 = func_2025_call()
call_5165 = func_2025_call()
func_4476_call = mod.get_global_var('func_4476')
func_4477_call = mutated_mod.get_global_var('func_4477')
call_5167 = relay.TupleGetItem(func_4476_call(), 0)
call_5168 = relay.TupleGetItem(func_4477_call(), 0)
func_2874_call = mod.get_global_var('func_2874')
func_2878_call = mutated_mod.get_global_var('func_2878')
var_5172 = relay.var("var_5172", dtype = "float64", shape = (24,))#candidate|5172|(24,)|var|float64
var_5173 = relay.var("var_5173", dtype = "int32", shape = (840,))#candidate|5173|(840,)|var|int32
const_5174 = relay.const([8.407027,2.886472,-2.263947,7.916656,9.606094,-8.477033,-5.561391,8.228444,9.226508,8.008753,5.670261,-6.895708,-1.714971,2.568683,3.758646,-4.913886,7.448638,9.259691,8.082069,5.873669,-0.308759,8.895939,-3.401781,-4.676071,-6.087528,-7.953066,-7.661350,7.166261,-6.943044,-1.597143,6.485817,-1.351444,9.650795,-5.389078,-0.571585,6.556575,1.588560,-3.567826,5.986764,2.596261,-7.691735,1.233021,-1.565982,0.023178,0.122067,-7.244131,-4.319510,-5.284765,-0.318684,-7.697794,-4.395817,-2.613479,-8.049099,-9.086470,2.991429,8.757122,6.118517,2.778448,9.725439,-7.212949,-9.296267,8.588853,8.852278,-6.557808,-6.648521,2.764751,-2.609811,-0.296132,-7.849623,-9.536406,-3.251824,1.494459,-7.139567,9.011521,0.864623,2.743478,6.896411,-5.044071,-4.298917,-0.039721,-0.488190,8.068073,9.879063,2.752550,-2.856118,-4.210902,-8.880842,-8.278478,-8.502724,-6.016431,5.405088,4.793444,6.241403,-6.507374,4.772221,-3.523413,-9.079753,-5.251695,-9.424281,3.522069,-7.971833,8.326840,6.744803,3.142481,-8.158800,8.947498,5.974667,-7.989297,-2.880971,-8.991306,3.919844,3.928351,6.608403,-4.630011,-7.606852,-2.799439,1.194555,3.567590,-0.894443,-1.748580,-4.020427,-3.559340,-1.869342,-7.262580,0.177638,-6.463091,-7.113503,-2.769555,-2.660691,6.260583,-5.530668,6.883581,6.955892,-2.221541,1.007397,-4.976941,-6.025964,-4.223862,1.360989,-0.103761,2.058002,-4.006044,-7.814247,2.007919,0.278634,0.887410,4.349180,7.599890,9.519258,-7.624178,-0.263473,5.134258,6.113822,7.148722,-5.120201,-6.102757,6.088896,0.778001,7.953240,-8.622801,4.627833,3.497380,-4.135483,-3.923209,-1.799678,-9.733861,9.520953,-8.530635,8.036895,-5.453371,1.370738,-7.605755,0.553291,-2.561117,-4.367436,5.731238,6.490307,-7.045152,7.540709,6.804122,8.846741,-0.093104,7.234865,-8.766926,-8.352666,4.255958,7.526950,-1.601111,9.550842,9.381542,7.566166,-4.385169,1.989759,-5.951849,0.348180,0.368677,-4.451169,1.183678,-5.664495,-3.359738,-5.755353,-3.698157,4.442133,-9.890397,9.583421,5.177529,-5.079725,3.253516,-3.132692,-6.069437,-8.288131,5.238385,8.031075,-5.686150,-0.129320,3.974809,-6.009040,-2.318285,-4.533534,1.893091,-9.448772,5.261809,-0.426721,9.797875,-7.523819,-7.568973,3.875892,3.950495,-5.412031,-1.439428,7.604778,-8.281430,3.635781,0.285255,6.227577,3.983837,1.587396,9.069142,-1.769286,2.698957,-9.018333,6.778083,3.358445,0.825535,-2.415422,-5.208977,9.110504,-2.426125,2.238956,-9.060510,-5.581066,-1.988263,-8.283746,5.601138,-6.465018,-8.371658,-3.658097,-9.541256,-8.054898,1.990856,5.278079,-8.395863,-8.731426,4.833893,0.442477,3.225977,-9.979760,8.288839,8.607189,2.547949,5.140326,-1.030811,9.490439,6.736123,-0.733274,-9.664962,-0.539683,-5.176807,6.164212,-1.676257,-3.844907,-9.164231,-8.995057,0.484361,-3.806174,7.766444,-8.047995,4.138582,6.310660,-9.094340,-6.309861,7.752332,6.596822,0.844199,-4.343666,5.069781,9.289321,7.015194,-8.481700,6.904491,0.844449,-2.579714,8.665746,7.054506,0.543813,-6.543581,-2.608912,-5.984607,-2.120039,4.267316,-3.678946,7.922880,-7.930279,8.121542,1.675307,-2.994629,5.048490,3.515841,-5.131408,8.402024,-4.950019,1.482777,-1.244809,-0.311415,-1.763343,5.636994,2.842319,-9.317131,3.198260,-0.985933,3.361582,6.428303,0.882643,0.555158,6.814033,0.386720,-3.014865,-0.635988,2.553013,8.512356,-3.126166,-9.068285,6.810076,-2.257393,-8.746830,-0.252029,9.991860,-0.173430,-9.872208,-6.273400,1.349386,5.288137,5.218942,-8.383245,-2.312471,-6.090084,-6.001193,-3.602354,5.411407,-5.788591,6.067391,4.143165,-0.080129,-3.398138,0.221124,-3.733475,-3.767472,3.241945,0.384156,-8.727403,0.076759,6.220207,0.565154,-8.791962,-9.547288,-0.425120,2.871838,-4.071067,-1.633225,-0.303105,1.637769,-8.259421,-5.596049,1.455478,1.039222,4.506411,-2.641240,-4.158364,0.766843,6.813367,6.721557,4.825668,5.119115,-6.521243,-9.761963,-8.929857,6.278761,-9.589716,-2.787837,1.185348,9.207854,-7.298282,3.777615,-0.264040,1.454060,-5.610510,0.654653,9.284341,6.663880,-4.616303,-0.945098,-4.679778,7.642312,2.081799,-2.087980,3.733412,-6.914829,-9.363906,-1.471672,-2.175918,-2.524116,-1.604897,-9.446839,-6.809250,6.075949,-1.393815,5.814945,3.229901,9.941413,-1.946825,-2.112010,2.705517,-2.209442,-8.470854,-3.015233,-1.464948,-0.333184,8.439803,6.205316,-8.026205,-4.798343,-3.929289,3.531489,1.358309,0.691736,0.518832,4.889895,-1.361646,-4.344832,4.693563,0.381695,8.793298,-1.366070,-0.272265,-3.365581,4.610228,7.668328,8.527898,2.331370,3.222821,-6.842440,-4.932506,-1.511612,1.116286,-1.393348,3.120735,7.384024,1.490091,4.643633,8.560039,-5.658250,0.355328,-5.796416,4.849931,0.317045,-7.077863,6.690117,7.619401,5.389499,-6.807821,1.711752,5.927431,-9.384574,3.577817,3.676176,5.962643,9.227889,7.623271,4.637267,7.955397,-2.620280,1.144649,2.650418,9.127016,4.966523,-4.238722,2.344149,5.447920,-0.059535,-0.582441,3.892109,3.511136,-2.903231,4.462149,3.870227,-8.086706,-2.989664,8.316106,-3.322317,0.095525,-8.718712,6.011689,6.761944,4.787695,5.853707,4.677506,-4.613405,1.465047,-9.110236,-0.003524,0.453987,3.763810,-3.937842,7.303660,4.756813,3.221864,-5.510221,2.287085,9.547665,9.870836,-8.602687,-8.278693,-6.321633,1.672484,-4.929907,-0.023406,-7.718574,5.246204,7.125511,-8.318111,6.914041,-5.055949,-2.736857,-0.398952,4.380004,-6.673682,-1.153881,-3.880539,-6.455667,9.568823,9.460382,-3.141093,7.853952,9.855189,9.972496,8.332053,1.569509,-9.433953,-8.603423,6.050863,8.875544,8.808398,-6.871788,-4.890184,-1.192727,2.052391,4.749300,6.041908,-8.108820,8.785116,-8.208264,-6.027601,7.436983,2.730171,9.844934,5.847684,-6.566451,3.896132,-1.795171,4.901799,5.773983,-6.062032,2.825307,-4.904784,-9.275716,8.483114,-4.395609,-8.356957,-7.568612,1.056748,1.404420,-1.192953,-0.892667,-2.060095,3.920581,5.819481,9.804798,-7.794501,6.171742,-8.079736,-5.338594,7.544012,0.699995,-7.578263,8.643289,-5.710739,-0.122187,0.592420,-8.575506,7.380668,8.591784,-8.578077,8.094675,4.383724,8.535772,-4.313321,9.314242,3.880145,-3.832554,7.691443,2.232933,-0.429795,-4.391785,-2.899787,8.861700,9.437741,-5.330511,0.069136,-3.237313,0.508013,-0.657311,9.944703,4.166107,5.604551,1.628507,2.577480,-8.817607,-8.856702,3.886569,6.485349,4.649700,-4.054953,-7.077818,7.338612,-8.250651,9.153254,-0.197849,1.494447,6.084362,2.555255,4.825207,8.258545,-2.426899,-0.421961,3.330141,9.665174,-4.317980,-3.032205,7.426401,0.138231,-8.224818,5.764040,-6.020943,-0.968925,7.854609,-7.265211,2.669382,-4.749888,7.156590,6.500307,-4.773686,0.790918,-1.116049,6.786027,3.100734,-8.039381,6.830248,6.413164,-1.408435,7.860689,6.764454,-8.153949,-6.569033,5.829637,4.217479,-3.926153,0.678408,5.199102,9.839455,2.634882,3.200516,2.831799,1.933065,-3.313113,-5.654664,8.162556,6.162592,-5.159658,-1.051215,-8.430421,9.953224,7.238204,-4.063362,-1.426897,-5.924944,5.840244,5.030384,-8.913104,8.084101,-7.582683,8.979232,6.320994,1.577825,-1.499449,3.080375,-6.352402,2.961071,5.104885,-4.819889,3.463013,-7.575155,-2.561133,8.925607,-0.471628,-5.410129,7.814002,1.068773,-6.698486,-2.921954,-9.610956,3.036465,-6.151314,5.587181,2.884222,-8.300890,-9.982964,8.782678,-8.646694,8.025493,4.997950,-5.490923,9.422348,6.528148,-9.560662,-6.360644,-1.813279,2.823960,-9.134285,-1.442148,-2.288072,6.405130,2.623170,-4.832859,9.964726,1.904943,9.953494,7.254815,2.098151,-7.657884,1.494111,-1.353707,2.025079,-5.377019,-6.137854,1.072851,7.757439,7.343568,5.513338,0.074853,-7.457096,6.946034,-8.027339,-3.367143,6.129410,1.133715,-6.732977,-1.818642,-2.064540,4.701484,-8.649054,0.013852,0.740176,-6.666004,-3.177033,-9.222628,-8.463875,-7.649863,-5.971258,-5.841291,-0.881156,-9.732303,-6.064530,-9.850044,-1.715535,6.501085,-7.631155,-0.120383,-2.387392,-3.581542,-7.028932,2.028169,-3.877683,1.275550,-1.657606,-4.612996,-6.705481,7.603166,-7.266967,2.671883,-4.208259,3.584762,5.709544,-0.582956,-1.610881,2.104455,4.260098,-6.372472,-7.198181,7.620256,1.766352,8.656068,-2.904800,-5.851788,-0.478525,2.580202,4.243599,9.549219,0.449635,-3.940810,-8.455828,-3.818408,-7.547604,7.192425,9.522943,9.553102,6.196732,-5.191308,-6.334885,-0.614652,-1.850836,2.792463,-0.082924,-5.386947,-7.444191,3.949611,-8.065949,0.088687,-9.058118,-6.607724,9.763770,0.134634,-2.600647,-4.241317,-4.348970,-0.523174,9.666984,-9.757588,-1.993092,7.787220,7.888913,-9.256602,-2.561142,-5.527883,-6.621257,-3.041805,3.347301,-5.959206,1.245476,-4.951956,0.376469,-3.172333,-7.174414,-3.828242,-7.879318,6.365497,5.910152,1.932927,4.611696,-8.909146,-3.697587,6.302539,-4.474340,-9.776880,6.271041,-6.526527,7.421503,2.207250,0.712961,-1.795902,0.735560,-4.541589,3.789984,-2.937587,3.116595,9.331561,-5.012799,6.608747,-5.325040,-0.966097,-6.349428,5.623942,-8.665089,0.835107,-8.074193,5.101066,-1.967735,-0.445336,2.133121,-2.535096,-7.283810,6.867464,0.677344,8.855280,-4.930827,5.938295,-7.863052,-9.836218,6.247320,5.859555,7.739988,3.494433,-7.316654,-6.428349,-2.326520,-8.903925,-5.324560,8.883240,5.749142,0.650904,0.203325,-2.426318,0.308359,-7.957866,5.153830,2.308337,-0.503733,-3.063752,-1.501916,-6.943693,1.893863,0.270085,-6.037506,1.120207,-7.842928,5.640897,3.957740,2.902119,-8.161558,0.937090,5.155641,3.566023,4.931988,-3.868533,-3.869209,7.218697,-2.406905,8.561647,8.677712,-1.160244,9.877834,9.795133,1.179039,-6.663981,-8.185657,8.265917,-6.228621,8.085464,-9.822526,2.558847,0.162612,3.646934,-9.318093,-5.979321,7.883326,9.902485,2.574275,-5.238568,7.184994,-0.725504,-3.349647,-9.631995,-2.831160,0.889153,6.780704,5.202349,8.354965,-2.831002,7.593116,2.036121,8.237722,-8.425003,-3.933625,-1.267317,8.720231,8.474154,-0.833463,-1.406649,-5.932408,-2.408333,-8.027559,-1.844196,-4.402665,5.814931,4.538746,-2.672545,6.179684,3.687548,1.843313,-7.878745,5.896997,2.111265,8.738887,-7.917966,3.815029,9.314950,9.203799,8.520370,4.909040,7.012350,7.527763,2.129273,-9.754328,-9.933516,-6.894796,-7.049527,1.220762,-9.897465,6.921371,-2.585770,8.272941,2.609559,3.314985,-0.812157,5.101039,8.865305,9.012042,-0.975942,-5.874725,-8.215762,2.644599,-2.174882,-8.456886,0.537730,8.244575,-6.334163,7.475352,0.734723,-5.253864,7.877699,-2.519083,-4.799511,-1.094479,3.007207,-2.554366,3.633310,0.641424,-2.479815,-0.570256,7.372788,5.469216,-2.081646,6.260649,7.748930,0.267034,-0.589689,4.404309,-8.995888,4.976546,-4.940545,9.923394,6.769656,4.003754,-5.538248,8.505343,-2.729591,8.294388,7.074765,-6.692192,-8.699542,-3.921225,2.961323,8.672421,8.566052,-5.354181,-0.522483,7.377619,-0.926368,5.436589,6.190865,-4.908913,3.901585,-0.719032,9.881953,3.100738,4.363837,-4.214716,-8.298258,-5.643681,-4.793239,2.084702,-6.615068,-4.018107,-6.144545,6.466302,-5.009487,5.565596,9.469905,-5.765630,-8.297471,-1.363551,6.769848,4.609830,-2.482512,7.274153,-1.694177,-7.297456,-6.008714,7.822866,-2.479972,-6.434925,-6.546807,4.272232,7.379412,-6.064681,3.946596,7.985566,2.166197,-7.262093,-5.843442,-5.112802,1.754754,6.877906,9.588944,-3.162719,5.904540,-2.512707,-1.136535,0.130723,-9.864604,9.707427,-2.970360,-4.875148,6.391365,-9.717615,2.488001,-4.123941,8.943616,-5.324249,-8.039634,-4.506128,2.981882,-8.864425,-6.219735,9.438454,2.273043,1.215918,-8.635951,-2.143187,-0.874411,5.947262,4.297285,-6.986458,-7.146315,-1.101516,4.955825,-7.711887,3.568083,-0.188908,2.296675,-9.201914,5.987110,-4.996554,-5.284285,9.906998,9.349701,-3.766656,5.315519,0.707250,3.092332,-3.172683,0.758036,9.100728,8.200828,-3.716084,1.189061,-8.463849,-8.600393,-3.287470,1.388357,-2.536708,1.466994,3.489759,5.472542,-6.086083,-6.917113,-7.058448,1.705937,5.990584,7.154565,1.797229,-5.092453,0.698921,7.967582,4.183272,-7.149757,2.369521,-9.078439,-8.602267,-3.959447,-6.977397,1.464128,-8.675101,-1.914551,-7.883232,6.377608,2.404638,5.046104,2.268148,-5.032389,1.471776,-4.381280,-4.870014,9.486454,-2.594294,3.908407,3.601021,6.913986,-5.893618,9.426417,-8.574498,-0.223496,-3.707669,-0.920788,-5.246063,5.100456,7.058623,3.067405,-9.141931,-4.037856,-2.183215,-1.144895,1.606481,4.927909,1.308831,-3.737798,4.522385,0.493413,-4.981842,6.564374,6.770688,-2.552278,-3.147601,-0.935714,-5.627670,-7.888146,9.085154,-7.872055,-7.232770,-2.374311,-4.319933,4.412279,5.660825,-5.864818,2.804855,3.803608,-8.613669,4.681438,9.321237,0.640265,8.628273,-4.604938,-1.696644,3.886908,-1.310607,2.139211,-9.075156,-0.769720,7.255228,1.641555,2.333919,5.610915,-5.990275,-1.174742,0.387311,1.733246,0.675240,7.870317,8.846062,2.899547,-8.178529,-2.601129,9.251264,-6.692027,2.816840,2.759106,-0.694147,-3.432900,-9.589917,-5.360964,7.540760,-9.091189,2.386547,-0.151872,-7.231021,-7.909641,-5.346409,9.353814,-5.201371,4.205209,7.556552,-0.110983,4.065023,-2.536456,8.284543,5.432956,-5.754813,-8.115696,7.752839,-7.214146,-6.895193,-5.262680,-8.490997,-6.111070,-6.747000,-7.037992,9.031754,7.829846,-4.962974,-8.316031,3.802263,-7.068366,0.453201,2.678425,0.973132,-3.650015,7.370284,1.057895,-6.007139,-7.758032,6.558049,-2.105876,8.763059,2.552950,3.041408,0.006814,-4.677543,-6.478256,-0.422091,-1.653090,-9.060866,1.802192,-0.555556,4.538574,6.697043,7.458815,-0.045259,9.547021,6.140871,4.563178,-1.961109,1.379342,-4.470138,-7.566509,-5.156407,4.864855,5.308485,-3.997417,5.600232,-9.364588,2.895846,2.706150,2.142318,6.417205,5.220489,0.590842,5.416631,-2.213356,-4.529194,1.327053,-7.574489,4.508728,2.581797,9.919389,2.719742,8.925026,0.070019,7.767076,0.691857,2.290758,6.704945,-5.287432,-8.116550,3.441781,3.078979,8.465287,9.724306,8.073230,-9.876419,4.832379,-8.872910,-9.330047,5.328141,-9.057181,-6.588125,7.046317,-9.810784,-2.753545,5.445837,-9.858551,-7.255300,-5.590413,-5.535451,7.823048,-9.028466,4.950993,9.980010,-9.889159,6.812957,-4.955469,-4.602647,5.268505,0.737761,9.490648,3.561484,-6.171258,2.087724,0.287326,-8.999559,-0.593110,2.110178,-5.522813,4.871752,8.850618,4.736767,-9.618109,-3.358247,5.374521,-0.805925,-1.112778,-8.377403,4.325915,7.959527,6.564926,2.429306,-1.731187,3.190160,-1.836270,7.812438,3.041084,1.191447,-0.243911,-0.357529,4.147815,2.445908,-1.622136,-7.126005,3.864549,7.694269,-9.665629,9.604401,8.820252,3.271363,8.490938,-9.579180,8.796259,5.540069,0.393654,0.739386,-1.346808,-0.897333,-6.192844,-3.464961,-6.450948,7.253416,6.171743,6.764575,9.830816,-2.677246,0.430533,-1.436770,-9.955599,-6.769232,0.885906,-6.953077,-0.873723,-0.085402,-4.542116,2.365299,-5.967313,2.677123,7.701357,7.383359,2.023410,7.418994,-7.903194,6.685323,9.157380,-6.842953,-4.687287,-4.307902,3.007650,0.121361,-3.380018,-5.304273,5.356904,-9.484666,-0.266229,-4.733514,8.522655,-9.309361,4.401462,-1.757506,3.587656,9.967532,9.640659,8.101812,-3.883930,-5.474630,5.183707,-3.777040,-6.869426,9.491842,-4.614418,-6.417008,7.874808,5.477368,7.809326,-6.823965,-9.220397,-9.203978,0.202288,-8.932385,-9.631536,-3.351682,9.184290,1.403087,6.498581,-0.149656,-1.239120,5.497084,5.886055,-1.402859,-3.168208,8.610725,-6.802758,3.157909,3.765669,1.714098,-6.530958,5.872158,-9.029113,-0.218066,9.160070,0.316140,3.896340,-4.912871,2.652389,3.462737,5.431934,-2.428597,-6.175369,1.072469,6.321333,-5.304343,9.939993,5.508457,-6.248735,0.095945,-4.806154,4.098827,-1.024211,-2.172118,-6.922427,0.602906,8.628093,2.079683,4.039041,5.754854,8.133578,1.643837,-9.516396,1.361314,-6.745475,-3.403711,0.239288,-7.644678,4.730728,-5.626370,4.439352,2.565528,2.092517,-5.922871,-5.469833,-4.170517,7.483117,-1.382809,-4.371125,-3.998301,-1.124688,-2.207635,-0.310755,9.679639,3.135320,6.920251,-0.599899,3.774511,9.207295,-7.117731,-5.935964,-3.442811,-6.874936,7.381446,-4.483167,7.282258,-7.042548,-2.665208,9.855393,9.952148,5.959780,4.313740,3.897652,-2.152398,-4.698084,-3.311028,2.109908,2.432946,4.230173,-6.116590,-8.517158,1.397246,0.581615,-2.071691,6.687410,-6.444812,-1.035301,-2.036734,-3.904794,6.335506,-9.957476,5.373418,-3.756415,4.559100,8.064071,4.614385,-7.354189,1.282819,-3.047187,-1.048616,3.176551,3.513002,-7.099640,8.938787,-0.487622,6.955384,4.466515,-4.663448,0.864497,8.768996,3.926666,1.318737,8.710635,-8.664717,-1.013767,-4.295017,9.531425,0.445435,4.566222,-4.086560,7.961706,-9.478478,5.604110,-7.895890,2.759653,5.360075,-4.015225,-0.138041,8.410881,-9.638605,7.268463,4.538852,-9.321156,-7.924078,-2.919465,3.338204,-0.460120,-1.851161,-7.291739,9.879174,-2.275471,-2.774723,4.494438,9.401205,6.282727,-1.930219,-1.280537,7.542363,-6.493509,-9.011341,0.861053,6.077128,-8.440458,1.855975,-2.382366,-8.424872,4.589706,-1.783505,0.952035,-3.768069,8.486595,0.697606,-7.847192,-7.186817,-5.569854,0.943184,-2.399786,9.053939,-4.471053,3.785816,8.697762,-5.996554,-7.672326,3.757720,-8.094575,7.142312,-2.377799,1.258698,4.449447,-8.877316,-7.321738,3.708685,-5.776926,4.485465,7.581114,9.369130,-8.665256,-1.992040,-5.567223,-4.716187,5.600878,-9.658849,-0.225018,-6.660623,7.300207,2.988879,4.848129,-6.530248,-4.835886,-7.320396,-1.288233,-7.109721,9.756456,-6.470642,1.293408,-0.002746,-5.717062,-3.141371,-6.525197,-4.255304,8.768457,-6.717342,9.964769,-6.520254,-9.015015,0.349163,0.497290,-4.012866,-3.780355,-7.306320,4.315996,-6.297375,-1.926451,3.292455,-8.525851,-1.171588,1.949784,-2.003554,-7.259963,-4.311994,4.475154,0.186165,-2.744705,-6.882035,-9.928038,-0.743938,1.217750,5.752526,9.050329,1.520136,2.377135,-1.169926,-2.646853,1.870650,1.879790,2.705831,9.520214,4.463680,-8.608671,5.587612,3.246354,0.185062,-8.659823,-6.683804,7.472699,0.468948,5.700784,5.209094,-9.140385,-5.391058,0.030634,0.134035,3.669214,-3.318968,-1.235620,-8.180964,3.513642,-9.054544,3.226223,4.090303,-0.681012,5.414294,-9.764077,9.314133,4.418262,5.338374,-6.223433,9.182137,4.831321,7.341310,1.559874,2.233882,9.660647,0.980867,-9.901510,8.147812,8.798068,5.421038,-0.175160,0.515419,-3.750265,-2.111990,6.582085,-5.044780,3.213855,-2.755863,-6.579587,3.620792,8.369161,-1.725235,4.078503,3.643671,-3.676856,4.149424,0.597260,-9.506678,6.983784,-4.310446,-5.896328,5.968866,5.145381,0.403408,-1.145401,7.782600,3.994241,4.017111,-7.243507,5.133037,3.167904,4.878382,5.564169,9.776756,-6.491998,2.607776,-1.818352,-2.649634,-0.433538,5.279588,-5.262426,2.580509,-2.724027,-3.037245,4.077551,4.613096,-5.621444,2.045642,-6.568905,-4.391586,0.874405,-7.244855,4.525568,8.574122,-8.680526,-5.006183,8.924162,-4.765972,-4.943096,-6.241331,-8.482168,4.896308,-2.091656,3.831130,9.757538,4.441610,9.534308,-9.336854,-2.449912,1.689437,5.473880,3.359265,0.611122,-0.700750,2.431993,0.591938,3.516418,-8.793156,7.289620,-3.562855,-1.958981,1.560405,0.352952,-2.652665,6.877115,-9.273907,9.022557,-1.414848,6.969630,-9.077556,6.946293,3.066104,-8.581609,7.073515,9.630003,-0.281264,4.626412,6.948763,-7.483177,9.583600,8.963677,-3.392763,5.407203,9.887862,5.423790,4.936967,5.739032,9.481828,5.991360,-1.502779,6.331033,-6.027008,-7.707018,3.192555,9.819089,1.051906,1.632923,7.602766,-6.698094,1.112167,-2.411528,-1.911600,0.972106,-0.493386,-0.006804,9.703666,3.544255,0.527456,-1.869868,-3.946019,7.194158,-0.764897,3.050977,7.693115,1.197339,-0.401833,-9.888087,6.118632,-1.321926,-4.478546,-2.937350,-0.747476,6.453408,-2.134393,2.594865,2.091865,-3.476763,2.963436,8.735000,5.212744,9.785884,-7.152431,-0.207669,-2.772025,6.110520,-4.976361,-8.957564,-9.271562,-1.344890,7.563116,4.243021,-7.242030,6.810728,-3.838931,-3.936118,1.755954,0.830448,1.851010,3.183403,-0.275307,-3.988678,3.769960,-3.096033,-2.633533,-3.519088,-7.765041,-0.394322,8.568871,-9.914719,-0.469759,6.235680,-8.505182,-8.020721,-2.723850,0.434639,-8.088657,3.119619,0.185259,3.910186,-1.575058,8.767847,-6.504117,3.271000,9.157664,1.910168,4.313382,6.071546,9.939710,5.020215,-6.498885,-6.162898,8.198591,-5.354630,6.188039,-8.608545,5.280280,-9.047891,-3.496658,4.523907,2.464847,3.602270,8.821975,3.874660,-0.463877,-5.697210,3.743345,-0.518616,2.889233,0.387723,-4.115553,-2.789311,-1.773949,4.681445,5.102182,-2.635362,3.638502,2.117287,5.789819,2.743708,5.762348,-0.087729,5.615128,2.037267,0.004443,4.873365,4.395807,8.213087,3.194692,-7.430374,2.935577,8.514500,-0.179039,4.080173,9.440196,-3.395481,-8.970762,-4.044444,5.480495,-5.357305,-6.398888,-0.390228,-1.422198,8.476565,0.384873,-0.986671,5.520679,5.782539,-0.153728,6.890128,-5.081847,-9.361247,-9.839099,-6.354276,1.440243,-6.532283,-9.387824,9.989424,-0.902476,-1.933365,-9.647079,-2.640710,3.254490,7.333149,-6.254382,7.465311,-1.202052,6.657961,-8.198540,-3.553911,9.226326,-9.636533,-9.542854,-2.483001,-5.784438,-6.115256,3.117799,-3.997859,-7.009171,-4.345736,-0.697655,5.712401,8.975125,0.250512,-8.993957,0.225369,-7.015745,-1.561294,3.164992,9.358672,2.686953,-8.769747,-3.482811,2.234417,1.490935,8.099402,-4.578007,-5.290025,-0.508609,4.358688,-3.812007,-6.940285,-1.405048,2.487014,6.039774,-4.788866,-3.863183,9.817751,5.863358,6.412700,-0.346893,3.663007,-6.339623,-1.982305,5.112421,6.227100,0.411786,4.342880,-8.458258,5.985741,6.303114,5.423381,0.485881,0.382533,3.798397,8.068640,2.804388,-0.553742,-9.275560,-4.343800,5.865250,4.626393,2.512271,-4.436115,8.306040,9.024978,1.967912,-9.471139,2.932577,-2.903760,6.769922,-2.151626,-0.098389,-7.025517,-9.085035,-6.195781,-3.951150,-9.656228,-3.378217,-0.025932,-5.809477,5.251892,-6.906575,-4.673310,8.490773,-9.237493,-5.654491,0.586605,-4.960159,-8.971166,5.910106,-7.578202,-6.996244,4.247599,1.690702,5.711353,-2.133311,-9.799155,-1.794495,-3.020350,8.318390,-6.602464,-7.775082,-1.244725,4.660703,6.316567,5.492891,9.874994,-8.485479,6.412726,-0.992647,6.290877,1.847404,5.836213,7.734175,7.005810,-6.880613,-7.201022,9.601431,5.748847,7.787824,8.051554,-7.002493,9.379960,-8.990081,5.469878,3.005963,7.631877,-1.240247,-9.246238,-6.871039,-1.405329,-7.614414,7.226767,6.300262,-5.785313,0.158747,6.722513,-6.414929,-4.614938,0.975465,7.109718,5.034848,9.352592,4.305896,8.313541,5.697804,7.212827,-0.274273,-9.088992,2.407158,7.887631,-3.541639,2.456415,2.439835,9.513820,3.774934,2.797376,5.221089,-1.179945,-4.231557,5.189927,1.611001,3.561456,8.128282,6.324340,7.616276,-0.643612,0.671490,-7.092717,4.538208,-0.114082,4.506213,8.607731,-4.868246,6.607646,3.910273,4.997291,5.014891,6.727028,-0.133893,-0.065557,8.422070,9.349761,-6.647798,3.191939,-8.169961,-4.987205,3.117091,-5.765062,1.626193,-3.960372,-8.446846,7.111235,4.185146,8.837253,3.724598,8.664874,-9.274447,2.279659,-4.028957,-1.903213,-1.840071,-6.122046,8.422904,-2.642460,5.885736,3.045828,-3.204669,2.549060,6.215440,4.596145,-6.092043,7.238658,6.265908,0.271275,0.356917,-1.529436,-2.092670,7.685878,-9.894060,-8.534866,0.577742,1.699504,-7.996855,1.892453,7.219300,-2.190487,5.185475,-0.536275,7.882883,-7.319373,-2.710108,-2.882039,-5.677739,-8.457054,1.891264,-9.931313,-5.994553,-1.308656,-3.745876,5.938340,-5.520099,-3.096892,6.890561,3.081234,-8.363079,-8.752897,-4.876871,-3.576860,-0.106350,9.167544,9.454218,-4.179340,-5.966076,4.498798,-6.131374,-1.836746,-7.800232,-4.460062,-3.990172,-5.294678,-5.003145,0.499905,-0.770224,9.368649,-2.952923,-3.856745,-4.812731,9.523805,-9.417388,5.535510,6.521149,1.931667,-2.287319,-6.376569,7.522589,-8.895287,3.526293,8.819325,0.533066,-2.571142,9.570661,8.260995,-4.129074,-4.104609,6.740083,8.230435,-1.410421,8.066432,9.375348,4.250371,-4.048173,-0.306964,2.633716,7.081260,-6.732018,-2.363628,1.814350,3.564636,-7.482913,-8.330799,0.257784,1.246352,-9.694336,1.373889,-2.670374,7.278109,-7.091271,-1.881660,0.362309,-2.326900,0.523895,5.635745,-5.648845,-0.653622,4.221052,7.831924,1.532741,-9.185717,7.371824,7.765015,-8.739128,-3.560367,-7.653392,-0.297719,0.304515,6.327515,5.778307,4.159178,4.970611,-8.456205,-1.083045,7.665270,-9.125370,1.768020,8.191217,0.152861,9.911371,-3.494796,-7.266327,9.282593,0.239289,4.979392,-5.510550,1.549936,-5.116023,-9.360396,8.196905,-9.576262,1.502609,1.053036,-7.691907,-4.280194,-5.674805,8.092290,9.162571,-0.030052,9.359537,1.112196], dtype = "float32")#candidate|5174|(2475,)|const|float32
call_5171 = relay.TupleGetItem(func_2874_call(relay.reshape(var_5172.astype('float64'), [24, 1]), relay.reshape(var_5173.astype('int32'), [1, 840]), relay.reshape(const_5174.astype('float32'), [11, 15, 15]), ), 8)
call_5175 = relay.TupleGetItem(func_2878_call(relay.reshape(var_5172.astype('float64'), [24, 1]), relay.reshape(var_5173.astype('int32'), [1, 840]), relay.reshape(const_5174.astype('float32'), [11, 15, 15]), ), 8)
output = relay.Tuple([call_5164,call_5167,call_5171,var_5172,var_5173,const_5174,])
output2 = relay.Tuple([call_5165,call_5168,call_5175,var_5172,var_5173,const_5174,])
func_5195 = relay.Function([var_5172,var_5173,], output)
mod['func_5195'] = func_5195
mod = relay.transform.InferType()(mod)
mutated_mod['func_5195'] = func_5195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5195_call = mutated_mod.get_global_var('func_5195')
var_5197 = relay.var("var_5197", dtype = "float64", shape = (24,))#candidate|5197|(24,)|var|float64
var_5198 = relay.var("var_5198", dtype = "int32", shape = (840,))#candidate|5198|(840,)|var|int32
call_5196 = func_5195_call(var_5197,var_5198,)
output = call_5196
func_5199 = relay.Function([var_5197,var_5198,], output)
mutated_mod['func_5199'] = func_5199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4436_call = mod.get_global_var('func_4436')
func_4438_call = mutated_mod.get_global_var('func_4438')
call_5250 = relay.TupleGetItem(func_4436_call(), 1)
call_5251 = relay.TupleGetItem(func_4438_call(), 1)
output = relay.Tuple([call_5250,])
output2 = relay.Tuple([call_5251,])
func_5252 = relay.Function([], output)
mod['func_5252'] = func_5252
mod = relay.transform.InferType()(mod)
output = func_5252()
func_5253 = relay.Function([], output)
mutated_mod['func_5253'] = func_5253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_5254 = relay.TupleGetItem(func_3129_call(), 0)
call_5255 = relay.TupleGetItem(func_3131_call(), 0)
output = relay.Tuple([call_5254,])
output2 = relay.Tuple([call_5255,])
func_5268 = relay.Function([], output)
mod['func_5268'] = func_5268
mod = relay.transform.InferType()(mod)
mutated_mod['func_5268'] = func_5268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5268_call = mutated_mod.get_global_var('func_5268')
call_5269 = func_5268_call()
output = call_5269
func_5270 = relay.Function([], output)
mutated_mod['func_5270'] = func_5270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5252_call = mod.get_global_var('func_5252')
func_5253_call = mutated_mod.get_global_var('func_5253')
call_5287 = relay.TupleGetItem(func_5252_call(), 0)
call_5288 = relay.TupleGetItem(func_5253_call(), 0)
output = call_5287
output2 = call_5288
func_5293 = relay.Function([], output)
mod['func_5293'] = func_5293
mod = relay.transform.InferType()(mod)
output = func_5293()
func_5294 = relay.Function([], output)
mutated_mod['func_5294'] = func_5294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4529_call = mod.get_global_var('func_4529')
func_4530_call = mutated_mod.get_global_var('func_4530')
call_5332 = relay.TupleGetItem(func_4529_call(), 0)
call_5333 = relay.TupleGetItem(func_4530_call(), 0)
output = relay.Tuple([call_5332,])
output2 = relay.Tuple([call_5333,])
func_5344 = relay.Function([], output)
mod['func_5344'] = func_5344
mod = relay.transform.InferType()(mod)
mutated_mod['func_5344'] = func_5344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5344_call = mutated_mod.get_global_var('func_5344')
call_5345 = func_5344_call()
output = call_5345
func_5346 = relay.Function([], output)
mutated_mod['func_5346'] = func_5346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
call_5443 = relay.TupleGetItem(func_1989_call(), 1)
call_5444 = relay.TupleGetItem(func_1991_call(), 1)
func_4106_call = mod.get_global_var('func_4106')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_5449 = relay.TupleGetItem(func_4106_call(), 0)
call_5450 = relay.TupleGetItem(func_4108_call(), 0)
output = relay.Tuple([call_5443,call_5449,])
output2 = relay.Tuple([call_5444,call_5450,])
func_5462 = relay.Function([], output)
mod['func_5462'] = func_5462
mod = relay.transform.InferType()(mod)
output = func_5462()
func_5463 = relay.Function([], output)
mutated_mod['func_5463'] = func_5463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
call_5470 = relay.TupleGetItem(func_1989_call(), 1)
call_5471 = relay.TupleGetItem(func_1991_call(), 1)
func_4907_call = mod.get_global_var('func_4907')
func_4909_call = mutated_mod.get_global_var('func_4909')
call_5475 = relay.TupleGetItem(func_4907_call(), 0)
call_5476 = relay.TupleGetItem(func_4909_call(), 0)
func_1595_call = mod.get_global_var('func_1595')
func_1598_call = mutated_mod.get_global_var('func_1598')
const_5480 = relay.const([-8.929473,-9.521025,-3.550949,-9.171632,-1.699430,5.427913,6.831314,-6.064069,6.915085,-7.374061,-1.192836,-2.251913,-2.278120,-4.519210,-7.572832,7.833587,6.810703,9.972137,0.895540,3.158342,-6.988215,7.533725,-7.731237,2.106686], dtype = "float64")#candidate|5480|(24,)|const|float64
const_5481 = relay.const([3,1,-2,9,-9,8,-1,-4,1,7,-9,-3,6,10,-9,6,-2,-5,7,8,8,-7,1,10,-1,-3,-1,5], dtype = "int8")#candidate|5481|(28,)|const|int8
call_5479 = relay.TupleGetItem(func_1595_call(relay.reshape(const_5480.astype('float64'), [24, 1]), relay.reshape(const_5481.astype('int8'), [28,]), ), 0)
call_5482 = relay.TupleGetItem(func_1598_call(relay.reshape(const_5480.astype('float64'), [24, 1]), relay.reshape(const_5481.astype('int8'), [28,]), ), 0)
var_5483 = relay.var("var_5483", dtype = "float64", shape = (24,))#candidate|5483|(24,)|var|float64
bop_5484 = relay.left_shift(const_5480.astype('uint8'), relay.reshape(var_5483.astype('uint8'), relay.shape_of(const_5480))) # shape=(24,)
output = relay.Tuple([call_5470,call_5475,call_5479,const_5481,bop_5484,])
output2 = relay.Tuple([call_5471,call_5476,call_5482,const_5481,bop_5484,])
func_5488 = relay.Function([var_5483,], output)
mod['func_5488'] = func_5488
mod = relay.transform.InferType()(mod)
mutated_mod['func_5488'] = func_5488
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5489 = relay.var("var_5489", dtype = "float64", shape = (24,))#candidate|5489|(24,)|var|float64
func_5488_call = mutated_mod.get_global_var('func_5488')
call_5490 = func_5488_call(var_5489)
output = call_5490
func_5491 = relay.Function([var_5489], output)
mutated_mod['func_5491'] = func_5491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4476_call = mod.get_global_var('func_4476')
func_4477_call = mutated_mod.get_global_var('func_4477')
call_5578 = relay.TupleGetItem(func_4476_call(), 1)
call_5579 = relay.TupleGetItem(func_4477_call(), 1)
func_3262_call = mod.get_global_var('func_3262')
func_3264_call = mutated_mod.get_global_var('func_3264')
call_5584 = relay.TupleGetItem(func_3262_call(), 0)
call_5585 = relay.TupleGetItem(func_3264_call(), 0)
func_3583_call = mod.get_global_var('func_3583')
func_3589_call = mutated_mod.get_global_var('func_3589')
var_5591 = relay.var("var_5591", dtype = "float64", shape = (24,))#candidate|5591|(24,)|var|float64
var_5592 = relay.var("var_5592", dtype = "int32", shape = (840,))#candidate|5592|(840,)|var|int32
var_5593 = relay.var("var_5593", dtype = "float32", shape = (1, 2475))#candidate|5593|(1, 2475)|var|float32
call_5590 = relay.TupleGetItem(func_3583_call(relay.reshape(call_5578.astype('float32'), [2, 9, 4]), relay.reshape(var_5591.astype('float64'), [6, 4]), relay.reshape(var_5592.astype('int32'), [840,]), relay.reshape(var_5593.astype('float32'), [825, 3]), ), 3)
call_5594 = relay.TupleGetItem(func_3589_call(relay.reshape(call_5578.astype('float32'), [2, 9, 4]), relay.reshape(var_5591.astype('float64'), [6, 4]), relay.reshape(var_5592.astype('int32'), [840,]), relay.reshape(var_5593.astype('float32'), [825, 3]), ), 3)
output = relay.Tuple([call_5578,call_5584,call_5590,var_5591,var_5592,var_5593,])
output2 = relay.Tuple([call_5579,call_5585,call_5594,var_5591,var_5592,var_5593,])
func_5608 = relay.Function([var_5591,var_5592,var_5593,], output)
mod['func_5608'] = func_5608
mod = relay.transform.InferType()(mod)
var_5609 = relay.var("var_5609", dtype = "float64", shape = (24,))#candidate|5609|(24,)|var|float64
var_5610 = relay.var("var_5610", dtype = "int32", shape = (840,))#candidate|5610|(840,)|var|int32
var_5611 = relay.var("var_5611", dtype = "float32", shape = (1, 2475))#candidate|5611|(1, 2475)|var|float32
output = func_5608(var_5609,var_5610,var_5611,)
func_5612 = relay.Function([var_5609,var_5610,var_5611,], output)
mutated_mod['func_5612'] = func_5612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2582_call = mod.get_global_var('func_2582')
func_2583_call = mutated_mod.get_global_var('func_2583')
call_5636 = relay.TupleGetItem(func_2582_call(), 1)
call_5637 = relay.TupleGetItem(func_2583_call(), 1)
func_2710_call = mod.get_global_var('func_2710')
func_2711_call = mutated_mod.get_global_var('func_2711')
call_5638 = func_2710_call()
call_5639 = func_2710_call()
func_3286_call = mod.get_global_var('func_3286')
func_3288_call = mutated_mod.get_global_var('func_3288')
const_5657 = relay.const([[1.854030,-7.119693,-3.282671,9.992072,5.180833,9.936311,0.335148,-7.166220,-8.461792,-5.574981,4.225882,4.088488,7.309519,3.452765,5.060329,-3.656453,8.119270,-6.423097,-1.090910,-2.200563,4.764365,-3.683802,0.788554,-2.795586,5.461224,1.078019,4.135705,4.346253,9.743040,-3.127617,6.732436,-3.198481,0.535946,-9.410234,-1.043187,7.790990,7.443443,-3.501990,-7.456752,-7.607605,9.633705,-4.679368,-4.110320,4.128846,-4.090652,-9.342518,7.082402,-7.833275,3.767580,-3.593116,0.189386,3.269655,2.798544,7.581150,0.377268,5.461130,-8.514612,0.116983,5.845704,-8.070994,6.627953,3.696779,0.620292,2.056544,2.468489,4.817330,-1.554558,4.341922,-1.521221,7.589838,-0.079122,1.167916,8.417801,1.446374,3.134473,-0.155775,7.126531,5.794148,-5.505520,4.560742,-8.289848,-9.422087,-7.716535,-6.554892,5.266384,-6.308543,-4.831154,-7.826892,-9.190022,-1.848219,7.812246,-7.740243,3.474951,-0.936680,7.399488,1.584305,-3.647097,-8.432443,3.432368,1.106896,-1.390176,-4.862439,7.563092,-6.424425,-5.012723,-1.643599,-2.641100,-5.295366,-9.560838,0.578858,4.492759,-4.853284,-9.700786,-0.786803,2.001667,-9.626219,2.220623,0.611443,2.156474,-9.001494,-8.598494,-1.257838,-6.004289,-1.373919,0.826163,-9.627889,-2.587867,-8.430882,4.847163,-0.316991,-3.294247,-8.228608,8.888624,8.782770,-6.365256,7.137030,-1.292293,0.888008,-0.587791,1.160119,4.346840,-3.882222,-5.949936,-7.503784,2.347855,7.749360,-4.964966,8.244008,4.635934,-7.549367,9.661256,-1.778823,1.418381,-7.708217,-5.120581,4.636254,1.265546,7.099243,-1.297314,3.883725,0.674834,-7.498783,-0.731336,7.161958,-7.956109,7.442103,8.797431,9.393337,4.620271,4.396931,8.484837,1.264965,-2.189661,5.391471,9.152576,2.604660,2.893785,-3.176667,2.927912,8.331778,8.877255,1.378149,-1.425953,-1.040142,-7.552941,3.557649,-3.660377,-2.882220,-0.418393,-2.384795,-4.381450,-8.022391,1.178395,-6.490524,-8.376469,-6.501324,-9.005598,6.476979,-2.360260,8.873014,2.037292,-7.099270,6.636914,-0.335679,-8.314680,7.822994,-8.728637,-5.037802,-7.401151,5.695943,-7.094279,0.732384,0.937121,-8.105374,-2.341363,6.206084,-5.669483,1.298503,-5.994852,6.779865,-5.287489,-2.787923,-0.238264,-8.187620,8.319382,-9.252900,1.310439,-0.830927,-4.765221,-9.446995,-1.244619,-3.632613,-1.544832,1.049574,1.889413,0.556275,6.803378,3.278066,8.882769,4.691427,5.460923,-2.155010,9.649026,5.838457,0.555047,-3.330710,7.785324,8.979360,-2.702612,2.083344,1.929943,-4.223280,-9.701198,1.027864,1.657566,-6.669048,-6.904412,-1.392277,9.169546,1.256016,4.520309,4.130646,-9.178343,-7.340116,4.307532,-0.785951,1.636873,0.364170,-8.640956,6.371072,9.141578,-8.022958,-6.467637,2.233416,4.922473,4.268686,-6.457371,1.884816,2.934594,-9.037460,9.077685,7.176514,3.337773,-3.138297,7.022851,9.299191,3.319435,-0.935905,-8.474041,-0.733931,-4.305970,7.106749,-3.046117,0.680700,-9.755729,-8.585869,7.049025,-0.900080,-0.481740,-0.946763,-5.023137,3.886428,-2.012784,-0.812257,1.589828,-9.627930,-2.367359,9.259621,-7.625483,-4.713796,-9.705809,4.095880,-6.690285,-0.051150,-7.415962,5.294842,-6.304319,8.199865,-4.747340,-3.332654,-1.690251,-9.821600,-4.584666,6.878340,-0.870744,8.820835,-8.670638,-3.676033,4.532718,3.640746,-6.914272,-4.201116,0.805768,7.064855,1.162365,-6.513299,-5.337880,-7.560251,-5.188637,0.467596,5.208776,7.811854,5.370595,5.772341,-3.833223,2.061613,9.572036,6.227059,9.949526,-2.448961,-7.196662,-3.213160,3.495113,2.886677,-0.825391,2.795083,-5.860066,3.746265,-6.820923,-8.465488,3.899351,4.061588,6.383827,-6.090129,5.832701,-5.482799,2.584039,-3.823350,2.385286,-6.479947,1.759001,-6.527805,-8.425093,1.879934,-3.862515,3.609313,7.586748,-1.547608,8.760012,5.017956,7.667927,3.711503,-3.392819,-5.408548,8.068326,4.127529,-0.889075,-8.587213,3.237860,5.902493,9.993752,-5.991921,-9.766912,-9.679481,6.944052,-8.823911,1.442242,7.886964,-3.616181,4.939035,-2.867323,-9.831860,-0.700452,2.402041,-9.402597,4.715478,1.242632,7.687982,-7.117412,4.260602,3.763664,2.053712,3.660131,4.209807,-8.687290,-6.148780,2.305064,9.320959,4.533339,-0.500604,7.252790,-0.786286,5.291897,-9.822797,0.943657,2.269504,-0.091970,0.503417,0.448425,9.272620,2.184847,-6.402481,-4.983140,3.554295,-9.325345,8.562106,6.502272,-9.526272,0.818026,9.426717,-9.114371,-2.039926,2.620585,6.755386,-9.228669,-3.856163,-6.109332,-8.110752,-9.275245,-9.255683,5.231166,-0.838680,0.971306,6.625592,-7.731914,9.616442,4.160993,9.283940,2.307721,0.512967,7.374307,-4.178188,-2.187151,-4.896792,-9.035808,4.205091,-3.974987,-4.706647,-8.408302,3.985044,-6.991642,-4.906481,-5.868258,-0.352344,-8.204758,4.349272,8.976495,0.273025,-2.444824,-7.108257,-3.268415,8.007856,-1.689201,3.983470,8.662754,4.182144,7.582229,-3.228410,9.338547,-7.440169,-7.599444,2.634962,1.140917,-0.277371,-5.958200,-0.189323,-3.078254,2.429043,6.435325,-5.342413,0.070866,1.936172,4.625635,-2.828605,-5.093789,-5.391325,-1.167173,7.584741,-7.155444,-2.664153,-3.043854,5.476067,-0.720741,9.971794,9.737535,-4.616143,7.475489,-6.143108,6.466551,9.109897,5.172299,1.125208,4.069251,1.579890,-2.311683,-6.186585,-2.530260,6.192155,9.107459,-4.619560,-3.640334,6.068398,-6.760509,-7.226233,6.095067,-9.414294,2.654213,-5.107240,-5.498832,-5.411419,8.745994,6.643198,8.218121,-0.658563,-5.161656,3.276913,-9.903812,-3.440749,-3.231439,-2.758346,3.183122,-7.914774,-8.588270,3.741403,-9.777045,6.619116,0.175716,5.373097,-1.038749,2.798978,7.857337,0.338127,6.087345,-8.222512,7.505074,9.731944,2.754818,9.394571,2.153199,-8.340332,0.166063,9.535865,6.488183,3.248735,0.088037,-4.728944,3.835093,-3.481563,1.831188,3.530446,3.548582,3.830331,-6.506228,7.649602,-0.602525,-8.796369,2.193373,-7.949032,-1.265961,-4.305107,-7.292070,-8.158844,2.398094,-9.000105,-6.919459,6.019946,6.274957,-6.820086,3.919810,7.870987,-9.270294,6.830754,4.776919,-6.081149,3.867114,8.194763,1.210215,-1.934104,-5.584037,0.750023,-2.350469,3.604514,-3.987748,2.610534,4.212468,1.249676,-8.154180,4.265359,-3.240221,-9.119116,8.940443,8.933169,0.322071,9.785336,-6.464270,-9.212253,2.855364,-0.958101,-9.143871,4.098983,-4.083449,7.275453,-2.536453,3.852897,-8.359908,-6.019075,9.839335,-7.684678,8.197050,4.736116,-0.898108,-7.282212,2.123854,4.777299,9.951682,8.000203,6.024448,-1.900979,8.565473,-8.822066,2.607656,6.752250,-9.465044,-0.452284,5.456935,-4.490162,2.294190,3.881972,4.278511,-7.314571,-3.941853,3.628388,-6.620329,4.660626,2.190451,5.942922,-1.844982,4.430960,-7.917600,4.558206,8.463522,-3.686469,-4.023763,5.938456,-1.762818,-1.940442,0.836106,9.813865,-8.751910,-3.889061,-1.107863,-8.183111,-9.275479,-9.030475,1.146622,7.302892,3.101380,-7.048300,1.626000,8.485944,8.367212,-7.292078,2.216633,3.024553,-0.091583,6.726173,8.398048,-7.229974,-3.924385,1.840892,-2.979459,-4.674439,-1.787254,9.703256,5.070198,2.012911,1.664343,5.406533,2.817801,-9.209873,-4.475257,9.522805,9.646365,-4.656407,-4.820379,-4.269192,-3.764652,-8.186713,4.145847,-3.033167,-5.191140,8.370926,-3.421490,3.404940,6.040774,0.240373,3.414263,-0.997271,-0.218021,-2.448504,-9.845117,7.432456,-3.580555,0.325398,-8.935571,-1.800840,7.685993,-6.586641,-0.287813,-8.884125,0.204366,-7.449316,-2.385293,9.219263,9.964394,1.789219,-9.334549,-6.087408,-0.526076,-7.795262,4.569929,0.337508,9.056376,-6.243747,7.496026,1.084419,4.269443,-1.123373,-0.168342,-6.439493,0.064411,6.775594,1.128779,-5.819981,7.126412,-7.352822,3.104452,-4.029783,9.877508,7.822970,5.887545,7.132919,-8.866501,-7.399550,6.968911,-0.484671,-8.503535,0.517534,9.288089,3.382741,-3.292948,4.833979,9.244445,-5.435191,2.207168,-6.946341,7.754278,0.860388,8.247043,-5.788893,-3.564789,4.908074,5.974198,-6.957237,2.880244,6.327089,5.680437,5.271911,-5.952278,8.825951,3.583192,-2.703526,5.197183,-0.874757,0.221168,-7.095913,7.450121,-6.325554,-9.745198,8.971492,-2.663252,8.926536,-4.975094,6.977574,7.851724,-3.194886,-3.434846,3.198154,-2.405893,-5.891499,-2.324225,2.717657,-2.294141,-3.943581,2.314613,-9.420860,3.556018,0.979802,5.659749,-4.967503,-6.055127,7.463086,-1.522238,-5.455673,3.236195,-3.105488,2.544119,7.116401,-8.386010,-4.549209,-6.291866,8.528297,8.761844,4.136077,1.326718,6.222236,-0.266896,-6.497387,6.224685,6.446379,8.298151,-1.041002,1.389880,3.433022,-8.187631,1.597973,-6.398342,-1.809834,-4.829568,-5.361748,9.070259,3.774505,6.282929,-5.151684,-8.609362,6.957389,-0.816332,9.363971,7.826817,4.059105,-6.592799,-9.432509,1.223109,-1.622988,-9.299788,-5.614618,-6.249314,8.905366,4.978868,-6.632021,1.837187,-1.431698,-9.554942,-2.868902,-3.051567,8.516630,-2.544870,1.389352,-9.170754,3.423614,2.408356,-7.150739,2.094804,1.821122,-5.803332,2.795760,8.463756,9.718790,7.436714,1.758350,9.338321,-3.192597,9.634006,3.977485,-0.584772,-7.604269,-1.483889,9.889580,3.980386,2.714954,1.892958,3.935512,-5.317712,-9.730418,-0.620949,7.495887,-1.584562,-6.470617,3.375340,4.787282,-4.578801,2.888659,-9.486136,1.480538,8.223851,7.483758,3.230758,5.956004,3.194999,5.669768,-7.899237,8.977760,-1.015482,-7.395627,-2.583359,2.668440,1.124866,0.134299,-4.633911,7.193129,5.757177,-3.982408,-8.930936,-6.740593,2.535658,9.168389,-8.616732,-7.885328,-6.539204,0.376994,-9.928968,-8.065304,3.965656,7.913267,-8.507853,-9.873713,-5.431393,-0.817264,-9.971822,-6.605756,-7.329894,9.836689,1.337087,4.548330,-9.626453,-0.659547,-5.449465,8.018649,-3.578794,3.754958,6.765587,1.013414,-0.487198,-8.605224,-5.988844,-6.319627,2.776034,-7.380099,9.969504,-6.528636,-3.792598,-4.960995,9.210976,-8.054378,-9.099657,-6.597489,3.587695,1.303951,3.065750,7.624740,9.093941,-4.407647,8.041011,8.697181,6.334988,6.002334,-3.626696,-7.960593,1.257526,8.913877,-8.796439,4.291878,2.338924,5.928137,4.078592,7.307097,-4.678028,7.307005,-3.540706,-7.633353,-7.509491,9.139303,6.158990,9.433667,-2.341252,-0.510843,-9.558728,8.135855,0.816783,3.568935,7.064363,6.074181,-1.183587,1.606282,6.350211,-7.645730,3.075690,-9.169499,0.176518,2.191433,-3.765820,-3.844119,-0.839958,8.811888,-9.148160,-2.364542,5.171071,4.701114,-7.848779,-6.489081,-0.942813,7.698144,-5.140959,-7.422370,2.982736,2.915615,-9.387716,2.255151,6.320692,-3.658176,6.985746,8.735095,-3.344789,-0.737944,-3.164777,-7.171085,-5.473361,-1.724649,5.760223,-6.849585,5.240937,-9.245119,-0.618467,-7.225181,-0.232295,4.182477,4.477135,-0.877790,-1.741378,-8.221645,0.048197,6.435279,-5.151406,-8.903321,1.529668,8.383615,3.859254,-3.849097,0.009960,4.299920,5.620661,1.080139,-2.911932,-3.046452,-1.614467,8.771210,5.815470,9.782974,-0.761558,6.490661,4.004543,-7.309473,-2.351863,-0.226367,5.835269,-7.717404,-5.706685,7.350298,9.571703,5.645677,-5.170379,-5.129764,-9.361545,-6.538004,3.239299,-7.474637,-8.291996,8.811809,9.484891,-0.345528,-2.691484,7.793021,-6.360218,9.096677,-3.233753,4.119832,3.459238,-7.694277,-3.199754,-1.169793,-8.890233,-1.137478,-5.246503,0.406384,5.579946,-6.409894,-4.473934,-9.496066,8.361430,4.273412,7.189243,-0.596364,-7.526927,-3.821275,0.255410,-3.297926,9.386324,-6.287718,7.968067,4.195455,6.064992,-0.176978,7.412091,-5.341976,-5.683951,-9.999498,7.007280,-1.944066,1.063625,-1.284992,1.796330,-7.929816,5.938869,-5.487618,-1.982377,1.803941,-1.504312,-0.012548,-0.151069,-6.895841,-5.483716,-3.039736,0.804469,4.586154,7.908675,-7.961029,-4.724704,0.201467,9.858412,-6.554826,7.244120,-0.383862,0.743920,7.013049,9.292004,-7.925845,-2.318218,7.943322,3.370906,-6.193646,-6.593976,-8.029037,2.361300,-6.439075,9.390323,3.064045,-4.241572,-4.677136,-6.418949,-7.719771,3.669873,0.114894,6.834680,-3.485433,0.276004,-1.649438,0.590681,-4.482413,-7.584818,0.554521,-7.206778,4.324069,-6.357680,-0.256714,7.843635,9.285597,-7.785461,7.468180,5.882468,-4.978268,-8.336641,9.842899,4.502148,7.349237,-1.534322,-8.657919,7.189214,-1.940165,0.094547,-6.806916,9.628279,-1.836507,-1.575472,4.985879,0.619634,-1.297399,-4.970034,8.885953,6.296599,-2.279916,8.143465,-5.569754,-9.184292,8.839863,-5.243413,-3.862059,6.837712,1.682407,-9.794926,4.931844,-8.676506,-4.439077,8.356013,9.049498,-5.110418,8.758636,-1.603694,-7.094693,-0.341527,-4.818252,1.389334,-9.194410,9.680024,-0.800694,-1.359536,1.382972,9.350070,-7.450253,5.958860,4.452143,1.685711,-3.441354,4.182565,-5.926535,-3.240170,-0.356903,9.544456,-2.318022,-7.892669,0.653402,-4.700006,2.714084,-4.524356,5.424624,4.007025,5.798520,2.739528,-8.851157,-3.895779,-5.058797,-5.412574,-0.548322,7.002256,-1.760780,4.014921,-6.811910,9.264023,1.066586,7.296776,3.542125,6.050624,3.041951,-5.879511,4.040146,-0.015145,7.163944,-8.711386,0.706436,-1.656595,3.367773,0.594262,-9.694917,-0.521452,-9.592556,-5.807973,-5.264871,-5.566988,-6.451239,-7.140631,0.870029,4.461910,6.369635,-5.702742,0.063334,-4.803323,-8.820555,-0.431276,-6.401144,-3.107609,5.034264,6.946893,-3.568518,8.045247,-3.803075,9.051906,4.941178,2.314457,-3.462720,2.355550,-1.522265,2.355642,3.372774,3.889888,-9.361507,-4.802246,-8.286179,4.968016,9.637951,5.197777,-4.418857,0.819445,6.897312,-8.470312,-8.713725,9.025972,-1.299687,7.071361,7.944586,2.234444,-3.014998,6.459141,9.644737,5.185463,1.313147,8.400742,9.577698,3.720875,6.873056,4.356096,4.470560,-8.743071,9.671186,3.893073,0.493840,-5.513951,-1.909514,-2.381063,-1.602624,-5.373542,9.254343,-6.132086,-2.986768,2.891858,3.924099,8.405485,-2.452341,-5.213969,4.270488,-0.882095,8.313413,-5.625487,-1.608121,2.054864,1.022206,-2.960505,4.798295,2.981828,6.771157,4.554931,7.293688,1.293427,3.540468,5.363971,-7.591789,2.899187,-4.769579,3.703859,-2.750238,-0.146331,3.862588,-8.340419,2.718163,-1.526449,7.682324,3.992277,8.383762,-8.250267,8.229638,1.875038,1.289662,7.909367,9.823841,-8.207664,6.313989,1.887537,7.951792,-4.473101,8.424165,6.751616,-6.567696,-3.197034,-3.053492,-5.419310,-1.620033,3.719107,-2.556862,-0.195650,5.213226,-9.077382,3.662806,6.026697,0.436857,1.509528,5.371693,4.409038,2.077712,0.250418,-4.291950,3.659869,7.593239,-4.670420,2.304186,1.902127,7.269722,-9.814590,8.878904,-5.333564,5.176995,-8.213624,-7.056850,-9.522020,1.212246,3.538167,-2.763168,-9.619035,8.736336,3.964741,8.869145,-2.148957,-7.719676,1.233854,-8.285276,1.168296,7.714915,-7.596172,2.034706,-3.821400,-7.834702,2.293986,-1.955844,4.903742,-3.766934,6.445239,6.550949,5.494880,-5.901724,-4.226547,-6.807328,-6.084014,2.651531,3.846641,9.736525,6.326051,-5.446058,-1.620725,-5.355701,-8.353952,1.548824,5.857992,6.425590,-3.647074,1.637160,0.365960,-6.573982,-9.353013,-9.336946,7.150413,7.033902,-2.184811,7.942874,-5.889856,-4.153413,-8.557275,-9.758732,-3.309353,-0.545677,8.760976,2.542434,4.254156,-5.720090,1.077270,-0.508759,5.474444,1.107483,9.386199,-4.488079,2.261600,-0.237228,-1.407687,3.043858,3.819444,-7.326137,4.613432,2.096252,2.966987,-2.884084,-2.296079,9.892869,-3.883424,3.281961,1.409600,-2.200397,-5.750153,7.863908,3.609320,-3.176113,-2.760007,-2.760930,-2.959593,1.362781,5.541798,2.503048,-2.349261,4.390016,9.351751,-1.500319,6.555191,0.939359,8.291663,-0.154424,4.523110,4.380916,8.413990,-0.489796,2.058202,-9.223006,0.485788,5.686823,-1.077664,1.794089,8.164587,6.670027,-2.705603,5.810847,0.827838,-0.924005,-9.989187,-5.590792,8.243279,1.050404,-1.304282,-6.014533,0.654251,5.582159,-1.304387,-4.141295,-3.899568,-1.521900,-9.429716,4.416693,-4.232983,0.047915,6.076700,-4.493804,-3.862345,-5.137613,5.727147,-9.380453,-2.938074,6.411275,-9.522213,-4.300301,3.645251,2.668495,-8.810212,7.837268,4.553860,2.919236,-9.256875,7.349641,-8.069132,-8.861288,-9.325905,-3.571435,-4.464670,-7.195091,1.729286,-4.386240,8.067429,5.087737,-1.304954,-4.671201,7.357419,-1.965750,-1.398831,-4.202865,6.797192,-0.790707,1.968235,-4.112882,-5.575577,7.856966,-6.854175,-3.987301,1.837347,8.141591,-7.094549,7.136809,-3.141829,-9.046183,-5.665368,6.058950,1.058789,5.831540,-7.239690,-1.759186,-1.334166,0.289316,5.007981,4.823006,3.760338,-4.761638,-7.983510,1.627455,-2.469590,0.102540,-1.397761,-0.569291,5.432928,-9.828260,-9.694301,-5.158126,-5.133246,2.362452,-4.919396,6.659639,8.152053,4.866551,8.796824,-7.245624,-8.387023,-1.018458,-0.934809,-7.674732,4.347182,-7.915146,-0.734929,-6.002407,-4.423397,-5.364217,-8.666108,-9.348699,-6.324238,-2.841964,-0.099791,5.576206,-6.565224,6.463498,-8.863792,-1.854641,-4.602537,1.244369,-7.926213,-7.190290,7.463317,4.900106,-4.838227,-5.882448,0.689719,-2.280933,4.541282,7.763180,-9.260480,8.203301,-3.361024,-3.696432,-1.858908,0.573309,3.930298,0.496289,4.756603,0.224740,-2.473783,-2.437263,-8.837917,8.697899,-7.607702,7.409667,4.879296,5.344044,1.884203,-3.846192,-0.164681,-5.148073,0.609897,-9.447012,-7.991717,-3.732113,5.663959,-0.299972,-9.960550,-9.238808,-7.429609,9.787568,-5.933194,-7.959929,-8.069247,4.894841,-9.674267,-5.007851,2.364710,-4.944476,-1.825709,-5.550107,2.688658,6.421660,-8.487874,-9.697964,-8.486289,-9.878773,2.640306,-7.584305,0.659437,-4.550996,4.948872,-0.561778,6.372626,-8.854921,1.541583,-3.224898,7.219274,-8.548746,3.634186,4.325824,-1.914175,-0.358922,-8.003905,9.554858,-6.953886,7.849579,6.326241,-6.635825,9.158882,-2.050786,0.448228,6.935356,0.588441,-2.385736,9.512792,-3.921426,7.001356,0.117068,1.072055,6.042295,-3.626966,4.644408,-3.490975,-5.637513,-1.441982,6.882250,8.084211,-6.290602,-9.981519,7.433336,-2.398274,-3.513331,-5.418262,2.559089,-9.306222,4.859690,-6.297959,-6.665053,-7.946448,-4.513688,-2.335428,-3.860398,-7.484193,-0.824971,5.131918,-6.595060,4.880130,5.743758,-3.634393,3.370607,-5.194153,3.763552,9.940328,3.615568,6.508239,-1.788040,6.966765,3.170664,5.890604,8.933178,-0.691219,1.007054,-7.172448,0.838887,2.038865,3.759056,-0.183484,-3.680892,5.206730,2.101409,8.610753,-3.132099,0.334252,1.650468,3.005366,4.628284,-9.237840,3.043106,-1.177253,-2.312721,6.583718,3.652429,-4.702811,3.382954,9.822761,-2.439103,-7.614342,-1.753070,4.526277,-1.142959,-8.054744,-0.524519,-0.382062,9.053045,-3.067564,4.943925,7.924687,2.664109,-7.950899,7.267056,-5.814754,9.861694,-9.886032,-2.647965,8.190549,-1.630789,-9.421601,-8.741100,-7.569172,9.054805,3.399288,-6.167527,0.432032,8.444111,-8.338905,-8.972216,-1.393713,4.088626,1.093746,-5.938747,0.441823,-7.309646,4.772980,-4.724027,-3.971048,7.438060,-4.924416,-2.440133,3.037115,-8.839065,7.655882,-6.702672,-8.994899,-4.386763,9.614633,-1.246748,-2.680264,8.103141,0.934404,7.939984,0.179690,-5.097744,4.593056,-1.740301,-3.481021,-6.697212,6.208664,1.563459,8.380819,8.125926,1.770548,8.347957,-2.951492,2.813980,-9.543644,2.271519,0.082969,-2.747890,-6.703053,-9.616492,0.080203,-7.690710,5.667309,-8.765856,-2.231579,-9.436529,3.023882,0.585634,-0.460843,3.633299,5.237633,-6.777409,-4.340570,6.420760,4.406306,4.458805,4.212084,2.362916,-4.952264,6.778266,4.007934,-4.354807,6.041300,-6.239159,-5.479991,-6.527534,-0.543716,6.449822,9.790301,-6.672108,-4.925646,4.862118,3.034237,-1.309033,-6.892357,-7.265441,0.457749,-9.991342,-5.716506,-9.824887,6.584820,2.534067,-9.104423,-4.558409,9.436811,-7.431904,6.153600,5.071526,1.808689,-1.325199,5.876204,2.532977,2.817892,1.978297,0.522825,-7.206727,6.468099,-4.824552,-2.933448,8.818676,2.813088,0.405255,-9.984068,-7.346826,4.123393,9.049479,7.874781,5.820475,5.763777,0.195110,8.486641,0.943151,8.045702,-7.272821,-2.599116,7.759461,3.554629,-1.484584,-3.191698,7.532849,2.237071,-3.355795,-5.196778,3.101635,1.783051,-6.749405,6.317369,7.530958,2.290172,-3.636779,3.604641,-2.186746,7.533145,-0.744377,8.648222,9.384115,5.278237,3.577837,8.008840,7.297840,3.895701,7.888995,2.949262,3.298571,-1.010764,-6.193156,-8.793433,7.975678,-1.361215,3.017105,0.708542,-7.113118,-8.082585,-1.492482,7.246095,-6.988615,1.245125,7.547277,-0.493076,-8.576762,-0.746167,0.806910,9.932003,-1.729453,-0.352215,8.498478,-5.808665,-5.244689,9.180282,0.161736,-2.478298,-4.142310,6.828478,-3.068431,-2.838840,4.245400,-8.928573,0.936438,0.337401,1.483416,9.994861,9.569962,-6.931840,0.620405,8.437025,-9.366369,-6.956471,7.443568,-8.196374,-1.836146,-4.515436,-5.554496,-3.553835,-0.172506,6.985641,2.302844,-8.958395,9.480073,3.890447,5.526406,9.409298,-0.968218,-9.049595,3.345285,-6.134162,3.777989,2.514051,7.982996,-3.978560,2.597706,1.256208,-9.161699,-9.305696,-2.610752,-3.935749,-2.538262,-5.980213,-0.429476,-6.950311,3.928114,1.248746,-8.039461,-8.028025,-8.237649,3.088568,1.214386,-4.537869,5.996879,8.262293,-9.297894,8.159808,0.184330,-9.835230,-5.736156,2.247796,3.986743,-4.123304,-5.376639,2.551119,0.358456,-4.355948,6.740069,1.818946,3.967914,-3.768542,-0.969991,-9.268468,2.432808,3.747853,-4.252128,-5.318056,1.176050,6.547006,7.987744,-0.650463,3.710171,6.941546,-2.486405,3.202902,4.452907,1.704783,7.861381,9.740729,-2.439382,-1.597223,-8.272851,-4.511152,-9.837237,3.959941,-5.178636,-3.283971,-1.639837,-8.627910,-1.446323,8.149187,-8.153703,-3.684966,-8.841592,-4.066721,-1.645672,6.497085,9.039424,5.565453,3.111684,-8.735712,-5.347041,-4.246395,-4.119270,1.301552,-1.374140,8.280897,-9.493329,2.747087,0.946781,5.507601,-7.167019,-6.681184,3.018732,4.838587,-0.776772,-5.475154,3.690800,-3.112945,-5.405993,-0.387349,-2.677984,8.683682,2.309946,9.550687,-8.202639,7.723987,-5.041845,5.624651,4.379130,-7.781894,-7.532332,-5.803859,8.624239,3.545217,2.788108,8.114087,3.139662,-5.507806,1.851250,-5.159499,-9.614421,-9.303582,5.546903,-9.294650,8.231479,8.931876,-7.298714,4.923807,-1.662679,5.378150,-8.182985,0.513543,7.934126,0.913757,7.084243,-7.560904,5.692771,-1.119655,-2.209587,6.680773,-6.352951,0.700644,-0.755525,-1.606611,-5.601930,-7.043642,-1.887658,-7.243774,8.390400,-6.007444,0.646334,7.664425,-3.559608,-5.551946,-6.165892,-9.517810,-0.429221,5.648066,-2.303876,6.885393,0.473209,9.249108,5.948545,5.396607,6.029231,4.006282,7.248968,5.021358,5.136718,-3.689605,2.264006,-9.928426,3.058271,1.794101,1.017881,-2.173548,-4.204868,7.989241,0.332325,0.939542,-5.815653,-7.128609,3.266525,2.066309,0.705632,-8.442615,-4.322013,-2.481548,8.635603,6.757501,-5.054480,6.562719,-5.190438,-3.133735,-1.380892,-5.618708,-7.439481,-9.577648,5.992531,-4.590286,7.350983,1.182681,2.344867,0.764294,0.958371,-9.553942,-5.722012,0.097053,-9.556999,0.917135,5.741848,3.766118,-3.744773,5.290143,-6.577834,-0.793393,-7.694976,1.107801,8.605849,-0.163939,-9.327026,-3.557663,4.058759,7.461784,8.462623,-1.719442,-5.470289,-7.120388,7.502625,-4.333403,-3.580655,2.800399,6.888727,-8.732246,-3.509223,3.935153,9.738250,0.877967,9.401267,-2.125788,9.198871,8.685320,8.634371,-3.921520,6.486587,-4.310259,1.129082,8.685136,-0.558240,7.926739,-4.491125,2.232552,-4.810940,-4.737576,6.425935,-2.584679,0.942258,3.337090,-5.737949,7.903628,-7.476819,3.419098,-9.109914,-6.348963,-0.710156,9.153714,5.748787,9.515201,3.622104,5.396253,-2.945347,-8.319895,-7.249458,-2.674284,7.428869,-8.154272,7.631102,-7.998672,-7.010968,6.893919,-5.869803,-1.803122,5.032884,-8.704413,6.317769,-3.217533,6.908788,-5.004277,-6.933599,-2.994952,-7.364770,1.307985,-3.928973,3.077393,4.685897,-5.378075,8.274373,2.259440,-1.090582,-7.756352,0.261062,2.687019,4.297064,-3.701084,4.165989,3.626919,-8.663213,0.136346,-4.220319,2.017729,3.235761,-4.336225,-8.416358,-0.713715,8.183649,0.357489,1.999011,6.936766,-5.465897,-4.343568,5.526464,2.054960,-3.498933,-8.729728,-6.330898,-4.280572,7.625765,-5.604706,-5.070051,-8.162569,4.412762,1.162902,5.543079,2.962555,-5.229553,6.844838,-0.658565,0.554837,7.425684,0.808529,-5.441467,-0.607339,-1.653455,9.388503,7.254814,-1.007280,8.402358,5.255345,8.296090,-0.206372,-1.316560,1.930189,9.061126,9.819796,-9.354568,-5.991205,6.095028,9.732582,7.186422,-1.487541,-0.268957,-8.601668,-6.289999,-4.385524,-4.776427,-8.606776,-2.262652,3.272575,-0.398514,2.011353,-1.790546,2.073776,-0.643270,4.304999,-0.527934,-5.623918,9.037099,-9.307164,-3.155305,5.485595,-6.754016,8.611582,7.516081,-5.342648,1.028988,-1.978197,6.020962,6.572662,-3.064971,9.691981,0.328275,-2.578981,-7.255989,-6.346798,0.757387,-3.521808]], dtype = "float32")#candidate|5657|(1, 2475)|const|float32
call_5656 = relay.TupleGetItem(func_3286_call(relay.reshape(const_5657.astype('float32'), [2475,])), 4)
call_5658 = relay.TupleGetItem(func_3288_call(relay.reshape(const_5657.astype('float32'), [2475,])), 4)
output = relay.Tuple([call_5636,call_5638,call_5656,const_5657,])
output2 = relay.Tuple([call_5637,call_5639,call_5658,const_5657,])
func_5661 = relay.Function([], output)
mod['func_5661'] = func_5661
mod = relay.transform.InferType()(mod)
output = func_5661()
func_5662 = relay.Function([], output)
mutated_mod['func_5662'] = func_5662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5462_call = mod.get_global_var('func_5462')
func_5463_call = mutated_mod.get_global_var('func_5463')
call_5743 = relay.TupleGetItem(func_5462_call(), 1)
call_5744 = relay.TupleGetItem(func_5463_call(), 1)
output = call_5743
output2 = call_5744
func_5754 = relay.Function([], output)
mod['func_5754'] = func_5754
mod = relay.transform.InferType()(mod)
mutated_mod['func_5754'] = func_5754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5754_call = mutated_mod.get_global_var('func_5754')
call_5755 = func_5754_call()
output = call_5755
func_5756 = relay.Function([], output)
mutated_mod['func_5756'] = func_5756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5155_call = mod.get_global_var('func_5155')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5775 = relay.TupleGetItem(func_5155_call(), 0)
call_5776 = relay.TupleGetItem(func_5157_call(), 0)
func_2582_call = mod.get_global_var('func_2582')
func_2583_call = mutated_mod.get_global_var('func_2583')
call_5777 = relay.TupleGetItem(func_2582_call(), 0)
call_5778 = relay.TupleGetItem(func_2583_call(), 0)
func_1068_call = mod.get_global_var('func_1068')
func_1072_call = mutated_mod.get_global_var('func_1072')
const_5787 = relay.const([[2,3,2,-8,9,-3,-10,-9,-3,-1,8,7,-3,-5,-6,4,-2,2,2,2,-1,-6,1,7,6,4,5,5,2,4,5,-6,6,-1,-7,2,8,-10,-5,5,-4,-3,-10,8,8,-10,2,2,-5,8,7,-1,-8,-8,-9,-4,3,1,-8,5,-2,1,-2,-2,7,8,-10,1,-1,10],[-1,2,-2,7,-3,5,9,7,-10,-10,-1,-9,9,-10,8,-2,-6,4,7,-7,-6,-6,-2,-8,-6,-7,7,9,-7,-8,-10,-7,5,4,5,-4,6,3,5,-10,10,-7,5,-4,-6,9,-3,10,-8,-3,6,3,9,1,7,-4,-9,3,8,8,10,-8,4,2,-4,6,-2,3,-4,3],[8,-8,10,-2,-7,-2,6,9,-10,5,-3,4,-9,-5,1,-4,-9,7,2,-8,8,7,10,5,8,-3,-10,-6,-6,-1,3,8,-8,1,-2,10,-9,-3,4,2,-1,-2,-4,1,-1,6,8,6,-7,-5,-8,-9,3,-7,-2,-10,3,-4,-2,6,-9,-1,-6,-2,-6,4,-3,10,-6,6],[7,3,-10,9,-3,-9,-1,9,7,-2,10,6,8,-1,6,-2,-5,-7,1,-9,2,7,8,1,-7,8,-1,-1,4,-3,9,-5,2,9,7,10,-8,3,2,1,10,-5,8,10,-7,-2,2,-1,7,-10,8,4,-6,1,-4,7,6,3,-7,-3,7,1,3,4,1,-6,3,-6,8,6],[4,6,-5,-1,3,7,1,1,-9,4,8,-1,-2,9,8,4,7,9,10,-4,-4,-6,10,-9,-2,-1,4,1,-2,-6,4,-2,1,-2,-1,-5,-9,2,-8,-8,-5,-1,4,-7,-10,7,-4,-4,-10,7,5,8,4,-3,10,-3,2,-8,-5,3,9,-9,8,-9,4,-10,1,-2,8,7],[7,-7,-5,-5,1,4,-9,4,-10,8,10,-10,-7,-5,-8,-7,4,1,-10,-10,6,10,8,-3,-6,10,-2,-6,-5,-6,-5,5,8,1,-2,-8,6,4,-1,-2,-9,-2,5,9,-2,10,-9,-1,10,-6,4,1,-3,3,1,10,8,-2,-3,2,8,-3,6,6,5,-8,-6,-6,-3,3],[-4,7,-7,4,10,3,7,-6,9,7,-4,2,6,-8,-9,-5,4,-7,-3,-10,7,10,1,-7,8,4,-10,3,-6,-5,2,10,-3,6,9,8,1,-2,-6,1,-4,9,3,8,-10,6,4,-9,-2,5,-3,7,-3,-4,-7,-6,-4,-5,-4,8,-7,-8,-2,-1,4,-8,-1,10,-6,-4],[1,-6,-4,4,5,5,-6,-4,-2,5,-1,2,7,-5,-6,8,10,4,4,-3,10,10,3,-6,-8,-10,3,-8,-1,5,-1,-5,-6,6,-7,-10,9,2,-3,8,9,-8,-9,5,1,-9,3,-5,5,1,-2,-6,1,4,8,3,9,2,-10,-8,-6,-3,-3,8,-10,7,-9,3,-2,-4],[-9,10,8,4,6,9,10,-1,-2,10,-9,4,-9,10,3,4,10,-8,5,-6,-7,-4,-9,-10,5,3,-7,4,3,9,-7,-8,8,-5,1,5,8,-4,4,8,-6,-5,-7,10,2,-7,-4,-6,-4,-7,-2,-2,-2,7,-2,7,-7,10,-3,7,-2,4,1,10,1,-10,-10,3,-9,-1],[-9,-9,-3,10,1,-1,2,-1,-5,10,-8,9,3,3,-4,4,-3,8,4,-1,-7,-10,-6,-6,1,7,8,-9,-7,4,-7,5,-3,-5,4,4,6,4,4,-5,8,4,9,7,-8,-9,1,-6,-10,-1,-8,-8,8,8,-4,7,-8,-7,6,3,7,2,8,2,10,-2,8,-3,-4,8],[-6,9,8,1,2,-10,7,-8,-2,5,-6,8,-1,-2,-2,2,-5,-3,6,9,-7,-6,-2,3,5,-6,7,4,-5,-2,7,6,-6,7,3,10,4,6,2,-10,7,7,9,1,-8,-2,8,8,-7,4,8,9,3,8,3,2,3,4,-1,-8,10,5,-10,-10,6,8,-1,6,2,-7],[3,7,-1,1,-9,-10,-1,-7,-7,-9,-2,-7,-5,4,10,-6,-3,10,-7,-5,-10,-5,1,3,8,1,2,-10,-2,6,-8,-4,7,-4,-4,1,5,8,-8,3,4,6,3,-3,-10,8,3,-10,7,7,4,-9,7,-6,8,-3,-5,-10,-4,-5,6,-4,-7,-1,8,-8,-9,-1,4,-1]], dtype = "int32")#candidate|5787|(12, 70)|const|int32
const_5788 = relay.const([9,-2,-4,4,3,-7,8,1,10,9,-4,-7,-5,4,-5,2,9,-3,-4,-4,-6,6,-5,-5,-8,3,7,7], dtype = "int8")#candidate|5788|(28,)|const|int8
var_5789 = relay.var("var_5789", dtype = "int8", shape = (448,))#candidate|5789|(448,)|var|int8
call_5786 = relay.TupleGetItem(func_1068_call(relay.reshape(const_5787.astype('int32'), [14, 12, 5]), relay.reshape(const_5788.astype('int8'), [7, 4]), relay.reshape(var_5789.astype('int8'), [56, 8]), ), 4)
call_5790 = relay.TupleGetItem(func_1072_call(relay.reshape(const_5787.astype('int32'), [14, 12, 5]), relay.reshape(const_5788.astype('int8'), [7, 4]), relay.reshape(var_5789.astype('int8'), [56, 8]), ), 4)
var_5798 = relay.var("var_5798", dtype = "int32", shape = (12, 70))#candidate|5798|(12, 70)|var|int32
bop_5799 = relay.power(const_5787.astype('float32'), relay.reshape(var_5798.astype('float32'), relay.shape_of(const_5787))) # shape=(12, 70)
func_1340_call = mod.get_global_var('func_1340')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_5802 = relay.TupleGetItem(func_1340_call(), 0)
call_5803 = relay.TupleGetItem(func_1341_call(), 0)
func_2923_call = mod.get_global_var('func_2923')
func_2924_call = mutated_mod.get_global_var('func_2924')
call_5808 = relay.TupleGetItem(func_2923_call(), 2)
call_5809 = relay.TupleGetItem(func_2924_call(), 2)
uop_5812 = relay.rsqrt(const_5787.astype('float32')) # shape=(12, 70)
output = relay.Tuple([call_5775,call_5777,call_5786,const_5788,var_5789,bop_5799,call_5802,call_5808,uop_5812,])
output2 = relay.Tuple([call_5776,call_5778,call_5790,const_5788,var_5789,bop_5799,call_5803,call_5809,uop_5812,])
func_5823 = relay.Function([var_5789,var_5798,], output)
mod['func_5823'] = func_5823
mod = relay.transform.InferType()(mod)
var_5824 = relay.var("var_5824", dtype = "int8", shape = (448,))#candidate|5824|(448,)|var|int8
var_5825 = relay.var("var_5825", dtype = "int32", shape = (12, 70))#candidate|5825|(12, 70)|var|int32
output = func_5823(var_5824,var_5825,)
func_5826 = relay.Function([var_5824,var_5825,], output)
mutated_mod['func_5826'] = func_5826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5293_call = mod.get_global_var('func_5293')
func_5294_call = mutated_mod.get_global_var('func_5294')
call_5859 = func_5293_call()
call_5860 = func_5293_call()
func_2035_call = mod.get_global_var('func_2035')
func_2036_call = mutated_mod.get_global_var('func_2036')
call_5871 = func_2035_call()
call_5872 = func_2035_call()
output = relay.Tuple([call_5859,call_5871,])
output2 = relay.Tuple([call_5860,call_5872,])
func_5873 = relay.Function([], output)
mod['func_5873'] = func_5873
mod = relay.transform.InferType()(mod)
output = func_5873()
func_5874 = relay.Function([], output)
mutated_mod['func_5874'] = func_5874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4252_call = mod.get_global_var('func_4252')
func_4254_call = mutated_mod.get_global_var('func_4254')
call_5875 = relay.TupleGetItem(func_4252_call(), 0)
call_5876 = relay.TupleGetItem(func_4254_call(), 0)
var_5885 = relay.var("var_5885", dtype = "float32", shape = (2, 9, 4))#candidate|5885|(2, 9, 4)|var|float32
bop_5886 = relay.subtract(call_5875.astype('uint32'), relay.reshape(var_5885.astype('uint32'), relay.shape_of(call_5875))) # shape=(2, 9, 4)
bop_5889 = relay.subtract(call_5876.astype('uint32'), relay.reshape(var_5885.astype('uint32'), relay.shape_of(call_5876))) # shape=(2, 9, 4)
output = bop_5886
output2 = bop_5889
func_5895 = relay.Function([var_5885,], output)
mod['func_5895'] = func_5895
mod = relay.transform.InferType()(mod)
mutated_mod['func_5895'] = func_5895
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5896 = relay.var("var_5896", dtype = "float32", shape = (2, 9, 4))#candidate|5896|(2, 9, 4)|var|float32
func_5895_call = mutated_mod.get_global_var('func_5895')
call_5897 = func_5895_call(var_5896)
output = call_5897
func_5898 = relay.Function([var_5896], output)
mutated_mod['func_5898'] = func_5898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_5943 = relay.TupleGetItem(func_1104_call(), 0)
call_5944 = relay.TupleGetItem(func_1105_call(), 0)
func_3721_call = mod.get_global_var('func_3721')
func_3722_call = mutated_mod.get_global_var('func_3722')
call_5960 = func_3721_call()
call_5961 = func_3721_call()
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_5962 = relay.TupleGetItem(func_1864_call(), 4)
call_5963 = relay.TupleGetItem(func_1865_call(), 4)
output = relay.Tuple([call_5943,call_5960,call_5962,])
output2 = relay.Tuple([call_5944,call_5961,call_5963,])
func_5975 = relay.Function([], output)
mod['func_5975'] = func_5975
mod = relay.transform.InferType()(mod)
mutated_mod['func_5975'] = func_5975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5975_call = mutated_mod.get_global_var('func_5975')
call_5976 = func_5975_call()
output = call_5976
func_5977 = relay.Function([], output)
mutated_mod['func_5977'] = func_5977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2229_call = mod.get_global_var('func_2229')
func_2231_call = mutated_mod.get_global_var('func_2231')
call_6044 = relay.TupleGetItem(func_2229_call(), 1)
call_6045 = relay.TupleGetItem(func_2231_call(), 1)
uop_6054 = relay.atan(call_6044.astype('float32')) # shape=(5, 6, 2)
uop_6056 = relay.atan(call_6045.astype('float32')) # shape=(5, 6, 2)
output = uop_6054
output2 = uop_6056
func_6067 = relay.Function([], output)
mod['func_6067'] = func_6067
mod = relay.transform.InferType()(mod)
mutated_mod['func_6067'] = func_6067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6067_call = mutated_mod.get_global_var('func_6067')
call_6068 = func_6067_call()
output = call_6068
func_6069 = relay.Function([], output)
mutated_mod['func_6069'] = func_6069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
call_6086 = relay.TupleGetItem(func_1989_call(), 0)
call_6087 = relay.TupleGetItem(func_1991_call(), 0)
func_1934_call = mod.get_global_var('func_1934')
func_1936_call = mutated_mod.get_global_var('func_1936')
call_6126 = relay.TupleGetItem(func_1934_call(), 1)
call_6127 = relay.TupleGetItem(func_1936_call(), 1)
func_4027_call = mod.get_global_var('func_4027')
func_4029_call = mutated_mod.get_global_var('func_4029')
call_6145 = func_4027_call()
call_6146 = func_4027_call()
func_5344_call = mod.get_global_var('func_5344')
func_5346_call = mutated_mod.get_global_var('func_5346')
call_6147 = relay.TupleGetItem(func_5344_call(), 0)
call_6148 = relay.TupleGetItem(func_5346_call(), 0)
func_5975_call = mod.get_global_var('func_5975')
func_5977_call = mutated_mod.get_global_var('func_5977')
call_6177 = relay.TupleGetItem(func_5975_call(), 0)
call_6178 = relay.TupleGetItem(func_5977_call(), 0)
func_3931_call = mod.get_global_var('func_3931')
func_3932_call = mutated_mod.get_global_var('func_3932')
call_6185 = relay.TupleGetItem(func_3931_call(), 0)
call_6186 = relay.TupleGetItem(func_3932_call(), 0)
output = relay.Tuple([call_6086,call_6126,call_6145,call_6147,call_6177,call_6185,])
output2 = relay.Tuple([call_6087,call_6127,call_6146,call_6148,call_6178,call_6186,])
func_6187 = relay.Function([], output)
mod['func_6187'] = func_6187
mod = relay.transform.InferType()(mod)
output = func_6187()
func_6188 = relay.Function([], output)
mutated_mod['func_6188'] = func_6188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3931_call = mod.get_global_var('func_3931')
func_3932_call = mutated_mod.get_global_var('func_3932')
call_6231 = relay.TupleGetItem(func_3931_call(), 0)
call_6232 = relay.TupleGetItem(func_3932_call(), 0)
func_2204_call = mod.get_global_var('func_2204')
func_2209_call = mutated_mod.get_global_var('func_2209')
var_6246 = relay.var("var_6246", dtype = "float64", shape = (24,))#candidate|6246|(24,)|var|float64
var_6247 = relay.var("var_6247", dtype = "int32", shape = (60, 14))#candidate|6247|(60, 14)|var|int32
call_6245 = relay.TupleGetItem(func_2204_call(relay.reshape(call_6231.astype('float32'), [2, 9, 4]), relay.reshape(var_6246.astype('float64'), [24,]), relay.reshape(var_6247.astype('int32'), [840,]), ), 2)
call_6248 = relay.TupleGetItem(func_2209_call(relay.reshape(call_6231.astype('float32'), [2, 9, 4]), relay.reshape(var_6246.astype('float64'), [24,]), relay.reshape(var_6247.astype('int32'), [840,]), ), 2)
output = relay.Tuple([call_6231,call_6245,var_6246,var_6247,])
output2 = relay.Tuple([call_6232,call_6248,var_6246,var_6247,])
func_6261 = relay.Function([var_6246,var_6247,], output)
mod['func_6261'] = func_6261
mod = relay.transform.InferType()(mod)
var_6262 = relay.var("var_6262", dtype = "float64", shape = (24,))#candidate|6262|(24,)|var|float64
var_6263 = relay.var("var_6263", dtype = "int32", shape = (60, 14))#candidate|6263|(60, 14)|var|int32
output = func_6261(var_6262,var_6263,)
func_6264 = relay.Function([var_6262,var_6263,], output)
mutated_mod['func_6264'] = func_6264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3838_call = mod.get_global_var('func_3838')
func_3840_call = mutated_mod.get_global_var('func_3840')
call_6328 = relay.TupleGetItem(func_3838_call(), 0)
call_6329 = relay.TupleGetItem(func_3840_call(), 0)
func_3634_call = mod.get_global_var('func_3634')
func_3635_call = mutated_mod.get_global_var('func_3635')
call_6344 = relay.TupleGetItem(func_3634_call(), 0)
call_6345 = relay.TupleGetItem(func_3635_call(), 0)
func_5873_call = mod.get_global_var('func_5873')
func_5874_call = mutated_mod.get_global_var('func_5874')
call_6348 = relay.TupleGetItem(func_5873_call(), 0)
call_6349 = relay.TupleGetItem(func_5874_call(), 0)
output = relay.Tuple([call_6328,call_6344,call_6348,])
output2 = relay.Tuple([call_6329,call_6345,call_6349,])
func_6362 = relay.Function([], output)
mod['func_6362'] = func_6362
mod = relay.transform.InferType()(mod)
output = func_6362()
func_6363 = relay.Function([], output)
mutated_mod['func_6363'] = func_6363
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6369 = relay.var("var_6369", dtype = "float32", shape = (7, 1, 6))#candidate|6369|(7, 1, 6)|var|float32
uop_6370 = relay.erf(var_6369.astype('float32')) # shape=(7, 1, 6)
output = relay.Tuple([uop_6370,])
output2 = relay.Tuple([uop_6370,])
func_6372 = relay.Function([var_6369,], output)
mod['func_6372'] = func_6372
mod = relay.transform.InferType()(mod)
mutated_mod['func_6372'] = func_6372
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6373 = relay.var("var_6373", dtype = "float32", shape = (7, 1, 6))#candidate|6373|(7, 1, 6)|var|float32
func_6372_call = mutated_mod.get_global_var('func_6372')
call_6374 = func_6372_call(var_6373)
output = call_6374
func_6375 = relay.Function([var_6373], output)
mutated_mod['func_6375'] = func_6375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2229_call = mod.get_global_var('func_2229')
func_2231_call = mutated_mod.get_global_var('func_2231')
call_6382 = relay.TupleGetItem(func_2229_call(), 1)
call_6383 = relay.TupleGetItem(func_2231_call(), 1)
uop_6390 = relay.sin(call_6382.astype('float64')) # shape=(5, 6, 2)
uop_6392 = relay.sin(call_6383.astype('float64')) # shape=(5, 6, 2)
func_3677_call = mod.get_global_var('func_3677')
func_3679_call = mutated_mod.get_global_var('func_3679')
call_6396 = func_3677_call()
call_6397 = func_3677_call()
output = relay.Tuple([uop_6390,call_6396,])
output2 = relay.Tuple([uop_6392,call_6397,])
func_6398 = relay.Function([], output)
mod['func_6398'] = func_6398
mod = relay.transform.InferType()(mod)
mutated_mod['func_6398'] = func_6398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6398_call = mutated_mod.get_global_var('func_6398')
call_6399 = func_6398_call()
output = call_6399
func_6400 = relay.Function([], output)
mutated_mod['func_6400'] = func_6400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3838_call = mod.get_global_var('func_3838')
func_3840_call = mutated_mod.get_global_var('func_3840')
call_6404 = relay.TupleGetItem(func_3838_call(), 1)
call_6405 = relay.TupleGetItem(func_3840_call(), 1)
func_3012_call = mod.get_global_var('func_3012')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_6426 = relay.TupleGetItem(func_3012_call(), 1)
call_6427 = relay.TupleGetItem(func_3013_call(), 1)
output = relay.Tuple([call_6404,call_6426,])
output2 = relay.Tuple([call_6405,call_6427,])
func_6429 = relay.Function([], output)
mod['func_6429'] = func_6429
mod = relay.transform.InferType()(mod)
mutated_mod['func_6429'] = func_6429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6429_call = mutated_mod.get_global_var('func_6429')
call_6430 = func_6429_call()
output = call_6430
func_6431 = relay.Function([], output)
mutated_mod['func_6431'] = func_6431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4064_call = mod.get_global_var('func_4064')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_6440 = relay.TupleGetItem(func_4064_call(), 0)
call_6441 = relay.TupleGetItem(func_4066_call(), 0)
func_2582_call = mod.get_global_var('func_2582')
func_2583_call = mutated_mod.get_global_var('func_2583')
call_6448 = relay.TupleGetItem(func_2582_call(), 1)
call_6449 = relay.TupleGetItem(func_2583_call(), 1)
func_3245_call = mod.get_global_var('func_3245')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_6473 = relay.TupleGetItem(func_3245_call(), 3)
call_6474 = relay.TupleGetItem(func_3246_call(), 3)
output = relay.Tuple([call_6440,call_6448,call_6473,])
output2 = relay.Tuple([call_6441,call_6449,call_6474,])
func_6480 = relay.Function([], output)
mod['func_6480'] = func_6480
mod = relay.transform.InferType()(mod)
mutated_mod['func_6480'] = func_6480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6480_call = mutated_mod.get_global_var('func_6480')
call_6481 = func_6480_call()
output = call_6481
func_6482 = relay.Function([], output)
mutated_mod['func_6482'] = func_6482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5088_call = mod.get_global_var('func_5088')
func_5090_call = mutated_mod.get_global_var('func_5090')
call_6488 = relay.TupleGetItem(func_5088_call(), 1)
call_6489 = relay.TupleGetItem(func_5090_call(), 1)
func_5754_call = mod.get_global_var('func_5754')
func_5756_call = mutated_mod.get_global_var('func_5756')
call_6493 = func_5754_call()
call_6494 = func_5754_call()
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_6504 = relay.TupleGetItem(func_975_call(), 0)
call_6505 = relay.TupleGetItem(func_976_call(), 0)
func_3634_call = mod.get_global_var('func_3634')
func_3635_call = mutated_mod.get_global_var('func_3635')
call_6507 = relay.TupleGetItem(func_3634_call(), 0)
call_6508 = relay.TupleGetItem(func_3635_call(), 0)
output = relay.Tuple([call_6488,call_6493,call_6504,call_6507,])
output2 = relay.Tuple([call_6489,call_6494,call_6505,call_6508,])
func_6517 = relay.Function([], output)
mod['func_6517'] = func_6517
mod = relay.transform.InferType()(mod)
output = func_6517()
func_6518 = relay.Function([], output)
mutated_mod['func_6518'] = func_6518
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6521 = relay.const([[[4,9,-7,-3,-5,6,-3],[1,-1,4,4,3,3,-5],[6,10,-10,-3,-2,-9,5],[2,-4,5,-1,-3,8,-6],[-3,3,-7,-7,-4,5,-1],[2,10,3,-8,-1,7,1]],[[-9,-6,8,-10,-4,5,1],[5,-4,7,-10,10,-9,6],[-5,3,6,4,1,-10,-5],[5,4,-8,-5,-2,5,5],[-3,2,-8,9,2,-5,-9],[8,-9,-10,2,-1,2,4]],[[-5,1,-7,-5,-6,6,-10],[-3,-7,3,-5,-9,2,6],[3,-1,-8,-8,5,-2,10],[1,3,10,-6,-8,-7,-7],[-6,3,4,10,6,9,-3],[-2,-2,-4,-6,5,-7,-2]],[[7,-5,4,-2,2,10,-2],[-1,1,2,6,-8,-10,6],[-5,4,-8,7,-7,-10,-3],[-8,1,-3,-5,-8,1,-7],[9,10,10,8,-3,9,5],[8,2,-4,9,7,-2,-7]],[[1,4,5,-5,-8,-2,9],[-8,3,-4,-5,-7,-8,8],[-9,5,-9,3,-2,9,-3],[-8,6,-9,-5,-3,-3,-5],[-5,1,8,-6,-4,2,-7],[-6,4,5,4,-9,6,9]],[[2,-8,-7,-1,-6,3,-5],[-6,6,5,9,-1,1,-10],[-2,6,-3,3,5,4,-2],[-1,-1,-1,10,10,5,2],[3,-5,-3,1,7,-5,-9],[-6,-5,9,-6,7,-8,7]],[[8,1,3,8,-1,1,4],[-10,4,-3,-5,-7,3,-8],[8,-6,7,10,7,6,-9],[-4,3,-6,-2,-6,-1,7],[-4,7,-2,-10,2,9,-2],[-5,-1,5,-5,-9,-10,-5]],[[5,-7,8,-4,-8,-9,6],[8,-10,8,2,-3,4,3],[6,-9,1,-3,1,-9,-2],[9,-4,-8,8,8,-9,6],[-5,-9,8,-4,-5,7,-4],[5,7,-6,1,-7,-9,-10]]], dtype = "int32")#candidate|6521|(8, 6, 7)|const|int32
var_6522 = relay.var("var_6522", dtype = "int32", shape = (8, 6, 7))#candidate|6522|(8, 6, 7)|var|int32
bop_6523 = relay.bitwise_and(const_6521.astype('int32'), relay.reshape(var_6522.astype('int32'), relay.shape_of(const_6521))) # shape=(8, 6, 7)
output = bop_6523
output2 = bop_6523
func_6540 = relay.Function([var_6522,], output)
mod['func_6540'] = func_6540
mod = relay.transform.InferType()(mod)
mutated_mod['func_6540'] = func_6540
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6541 = relay.var("var_6541", dtype = "int32", shape = (8, 6, 7))#candidate|6541|(8, 6, 7)|var|int32
func_6540_call = mutated_mod.get_global_var('func_6540')
call_6542 = func_6540_call(var_6541)
output = call_6542
func_6543 = relay.Function([var_6541], output)
mutated_mod['func_6543'] = func_6543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_6579 = relay.TupleGetItem(func_975_call(), 0)
call_6580 = relay.TupleGetItem(func_976_call(), 0)
output = call_6579
output2 = call_6580
func_6592 = relay.Function([], output)
mod['func_6592'] = func_6592
mod = relay.transform.InferType()(mod)
output = func_6592()
func_6593 = relay.Function([], output)
mutated_mod['func_6593'] = func_6593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_6642 = relay.TupleGetItem(func_1104_call(), 0)
call_6643 = relay.TupleGetItem(func_1105_call(), 0)
output = call_6642
output2 = call_6643
func_6662 = relay.Function([], output)
mod['func_6662'] = func_6662
mod = relay.transform.InferType()(mod)
mutated_mod['func_6662'] = func_6662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6662_call = mutated_mod.get_global_var('func_6662')
call_6663 = func_6662_call()
output = call_6663
func_6664 = relay.Function([], output)
mutated_mod['func_6664'] = func_6664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5661_call = mod.get_global_var('func_5661')
func_5662_call = mutated_mod.get_global_var('func_5662')
call_6665 = relay.TupleGetItem(func_5661_call(), 3)
call_6666 = relay.TupleGetItem(func_5662_call(), 3)
func_1340_call = mod.get_global_var('func_1340')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_6679 = relay.TupleGetItem(func_1340_call(), 0)
call_6680 = relay.TupleGetItem(func_1341_call(), 0)
output = relay.Tuple([call_6665,call_6679,])
output2 = relay.Tuple([call_6666,call_6680,])
func_6681 = relay.Function([], output)
mod['func_6681'] = func_6681
mod = relay.transform.InferType()(mod)
mutated_mod['func_6681'] = func_6681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6681_call = mutated_mod.get_global_var('func_6681')
call_6682 = func_6681_call()
output = call_6682
func_6683 = relay.Function([], output)
mutated_mod['func_6683'] = func_6683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4252_call = mod.get_global_var('func_4252')
func_4254_call = mutated_mod.get_global_var('func_4254')
call_6774 = relay.TupleGetItem(func_4252_call(), 1)
call_6775 = relay.TupleGetItem(func_4254_call(), 1)
output = relay.Tuple([call_6774,])
output2 = relay.Tuple([call_6775,])
func_6779 = relay.Function([], output)
mod['func_6779'] = func_6779
mod = relay.transform.InferType()(mod)
mutated_mod['func_6779'] = func_6779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6779_call = mutated_mod.get_global_var('func_6779')
call_6780 = func_6779_call()
output = call_6780
func_6781 = relay.Function([], output)
mutated_mod['func_6781'] = func_6781
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6823 = relay.var("var_6823", dtype = "bool", shape = ())#candidate|6823|()|var|bool
var_6824 = relay.var("var_6824", dtype = "bool", shape = (16, 2, 7))#candidate|6824|(16, 2, 7)|var|bool
bop_6825 = relay.logical_or(var_6823.astype('bool'), var_6824.astype('bool')) # shape=(16, 2, 7)
bop_6830 = relay.logical_xor(bop_6825.astype('uint32'), var_6823.astype('uint32')) # shape=(16, 2, 7)
bop_6835 = relay.less(var_6824.astype('bool'), relay.reshape(bop_6830.astype('bool'), relay.shape_of(var_6824))) # shape=(16, 2, 7)
output = relay.Tuple([bop_6835,])
output2 = relay.Tuple([bop_6835,])
func_6860 = relay.Function([var_6823,var_6824,], output)
mod['func_6860'] = func_6860
mod = relay.transform.InferType()(mod)
var_6861 = relay.var("var_6861", dtype = "bool", shape = ())#candidate|6861|()|var|bool
var_6862 = relay.var("var_6862", dtype = "bool", shape = (16, 2, 7))#candidate|6862|(16, 2, 7)|var|bool
output = func_6860(var_6861,var_6862,)
func_6863 = relay.Function([var_6861,var_6862,], output)
mutated_mod['func_6863'] = func_6863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2486_call = mod.get_global_var('func_2486')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_6868 = relay.TupleGetItem(func_2486_call(), 1)
call_6869 = relay.TupleGetItem(func_2487_call(), 1)
output = call_6868
output2 = call_6869
func_6875 = relay.Function([], output)
mod['func_6875'] = func_6875
mod = relay.transform.InferType()(mod)
output = func_6875()
func_6876 = relay.Function([], output)
mutated_mod['func_6876'] = func_6876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4301_call = mod.get_global_var('func_4301')
func_4303_call = mutated_mod.get_global_var('func_4303')
call_6883 = func_4301_call()
call_6884 = func_4301_call()
func_5344_call = mod.get_global_var('func_5344')
func_5346_call = mutated_mod.get_global_var('func_5346')
call_6906 = relay.TupleGetItem(func_5344_call(), 0)
call_6907 = relay.TupleGetItem(func_5346_call(), 0)
func_5252_call = mod.get_global_var('func_5252')
func_5253_call = mutated_mod.get_global_var('func_5253')
call_6921 = relay.TupleGetItem(func_5252_call(), 0)
call_6922 = relay.TupleGetItem(func_5253_call(), 0)
func_4064_call = mod.get_global_var('func_4064')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_6944 = relay.TupleGetItem(func_4064_call(), 0)
call_6945 = relay.TupleGetItem(func_4066_call(), 0)
output = relay.Tuple([call_6883,call_6906,call_6921,call_6944,])
output2 = relay.Tuple([call_6884,call_6907,call_6922,call_6945,])
func_6955 = relay.Function([], output)
mod['func_6955'] = func_6955
mod = relay.transform.InferType()(mod)
mutated_mod['func_6955'] = func_6955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6955_call = mutated_mod.get_global_var('func_6955')
call_6956 = func_6955_call()
output = call_6956
func_6957 = relay.Function([], output)
mutated_mod['func_6957'] = func_6957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6187_call = mod.get_global_var('func_6187')
func_6188_call = mutated_mod.get_global_var('func_6188')
call_6990 = relay.TupleGetItem(func_6187_call(), 5)
call_6991 = relay.TupleGetItem(func_6188_call(), 5)
output = relay.Tuple([call_6990,])
output2 = relay.Tuple([call_6991,])
func_7001 = relay.Function([], output)
mod['func_7001'] = func_7001
mod = relay.transform.InferType()(mod)
mutated_mod['func_7001'] = func_7001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7001_call = mutated_mod.get_global_var('func_7001')
call_7002 = func_7001_call()
output = call_7002
func_7003 = relay.Function([], output)
mutated_mod['func_7003'] = func_7003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_7059 = relay.TupleGetItem(func_2815_call(), 1)
call_7060 = relay.TupleGetItem(func_2816_call(), 1)
func_1368_call = mod.get_global_var('func_1368')
func_1370_call = mutated_mod.get_global_var('func_1370')
call_7065 = func_1368_call()
call_7066 = func_1368_call()
func_6517_call = mod.get_global_var('func_6517')
func_6518_call = mutated_mod.get_global_var('func_6518')
call_7067 = relay.TupleGetItem(func_6517_call(), 0)
call_7068 = relay.TupleGetItem(func_6518_call(), 0)
func_3320_call = mod.get_global_var('func_3320')
func_3322_call = mutated_mod.get_global_var('func_3322')
call_7069 = relay.TupleGetItem(func_3320_call(), 2)
call_7070 = relay.TupleGetItem(func_3322_call(), 2)
func_3320_call = mod.get_global_var('func_3320')
func_3322_call = mutated_mod.get_global_var('func_3322')
call_7072 = relay.TupleGetItem(func_3320_call(), 1)
call_7073 = relay.TupleGetItem(func_3322_call(), 1)
output = relay.Tuple([call_7059,call_7065,call_7067,call_7069,call_7072,])
output2 = relay.Tuple([call_7060,call_7066,call_7068,call_7070,call_7073,])
func_7086 = relay.Function([], output)
mod['func_7086'] = func_7086
mod = relay.transform.InferType()(mod)
mutated_mod['func_7086'] = func_7086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7086_call = mutated_mod.get_global_var('func_7086')
call_7087 = func_7086_call()
output = call_7087
func_7088 = relay.Function([], output)
mutated_mod['func_7088'] = func_7088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6517_call = mod.get_global_var('func_6517')
func_6518_call = mutated_mod.get_global_var('func_6518')
call_7093 = relay.TupleGetItem(func_6517_call(), 1)
call_7094 = relay.TupleGetItem(func_6518_call(), 1)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_7096 = relay.TupleGetItem(func_6480_call(), 1)
call_7097 = relay.TupleGetItem(func_6482_call(), 1)
func_5035_call = mod.get_global_var('func_5035')
func_5036_call = mutated_mod.get_global_var('func_5036')
call_7116 = relay.TupleGetItem(func_5035_call(), 1)
call_7117 = relay.TupleGetItem(func_5036_call(), 1)
func_3012_call = mod.get_global_var('func_3012')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_7122 = relay.TupleGetItem(func_3012_call(), 0)
call_7123 = relay.TupleGetItem(func_3013_call(), 0)
func_6362_call = mod.get_global_var('func_6362')
func_6363_call = mutated_mod.get_global_var('func_6363')
call_7136 = relay.TupleGetItem(func_6362_call(), 1)
call_7137 = relay.TupleGetItem(func_6363_call(), 1)
output = relay.Tuple([call_7093,call_7096,call_7116,call_7122,call_7136,])
output2 = relay.Tuple([call_7094,call_7097,call_7117,call_7123,call_7137,])
func_7140 = relay.Function([], output)
mod['func_7140'] = func_7140
mod = relay.transform.InferType()(mod)
output = func_7140()
func_7141 = relay.Function([], output)
mutated_mod['func_7141'] = func_7141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3634_call = mod.get_global_var('func_3634')
func_3635_call = mutated_mod.get_global_var('func_3635')
call_7212 = relay.TupleGetItem(func_3634_call(), 0)
call_7213 = relay.TupleGetItem(func_3635_call(), 0)
func_159_call = mod.get_global_var('func_159')
func_164_call = mutated_mod.get_global_var('func_164')
const_7216 = relay.const([9.579133,-7.394811,9.745139,-3.403525,9.965590,7.671305,0.016578,-7.586088,-1.640980,6.810249,8.473688,-1.635582,9.653820,-9.657699,-7.006901,9.852325,-0.974165,-6.777848,-0.989799,6.632771,4.789818,9.847107,-8.492599,-5.811936], dtype = "float64")#candidate|7216|(24,)|const|float64
const_7217 = relay.const([[-3,5,-8,1,2,-1,7,-4,10,-10,6,-4,-9,-5,7,10,-2,3,1,3,8,-6,8,3,-1,4,10,-4]], dtype = "int8")#candidate|7217|(1, 28)|const|int8
const_7218 = relay.const([1,-9,-1,5,-2,-9,-2,10,9,-7,3,5,7,7,6,5,1,6,6,7,-10,4,3,-7,2,-7,3,-4,7,4,-1,-9,-2,6,8,5,-8,-9,2,5,1,-3,-4,-7,-8,4,-1,-4,2,10,-3,-10,-3,-4,-7,1,1,-2,-10,-5,1,10,2,4,5,-4,10,-9,-4,-8,-2,-9,-4,7,2,-2,9,7,-7,-7,-7,-9,6,-10,1,-9,8,5,9,-3,1,-5,9,-6,-5,9,4,10,7,10,7,-2,-7,4,8,8,7,4,7,4,-10,5,4,4,3,-1,3,-5,2,-10,-1,2,4,-5,5,-3,6,-9,-1,-2,-8,7,8,-4,3,1,-2,1,-8,-5,6,7,5,-2,10,-5,1,-10,3,-9,7,10,10,3,8,10,7,-9,5,3,7,2,9,7,5,10,-6,9,-4,6,4,9,5,-6,-9,-4,6,-6,-9,10,-1,-5,-3,-2,9,-2,-6,-6,8,9,-10,8,10,-4,-9,2,5,4,4,-8,6,7,10,10,3,7,-6,-3,9,5,2,-7,-7,-6,8,3,3,-5,1,-2,7,-10,-6,-9,-10,4,-6,-8,1,1,7,3,-3,-4,-4,-9,-10,5,-1,5,-3,-3,8,-9,5,-10,5,4,-4,2,-9,-10,-1,-6,-1,6,-8,10,-10,6,-2,-8,2,7,-2,-5,-2,-9,1,-7,-6,4,-4,3,7,9,-8,6,-1,-5,4,6,-6,-8,2,-9,2,4,10,-10,-7,-6,-6,-4,-5,-9,-10,4,-10,4,2,2,-7,-10,4,-3,6,5,-2,-10,7,-8,4,4,6,8,1,2,6,6,9,-10,-1,-9,-1,1,-8,-8,3,-10,2,-9,-10,1,-2,-6,8,-9,9,9,-7,-2,1,1,4,5,9,-8,-4,5,-8,8,-6,-3,7,7,-4,10,10,9,3,7,7,-3,6,6,10,8,-3,3,2,-5,-10,4,-6,-4,-9,5,8,-7,-7,-6,1,2,-4,-5,6,7,-4,-4,5,1,8,-10,-3,1,-1,8,-1,-5,7,3,9,7,-10,4,-10,-1,-1,7,9,-6,4,-4,6,10,-1,-5,5,-2,5,-2,2,-5,4,9,-9,6,10,-8,9,-10,-3,9,-8,-6,-8,10,-2,5,7,3,-10,9,7,8,7,6], dtype = "int8")#candidate|7218|(448,)|const|int8
call_7215 = relay.TupleGetItem(func_159_call(relay.reshape(const_7216.astype('float64'), [4, 2, 3]), relay.reshape(const_7217.astype('int8'), [28,]), relay.reshape(const_7218.astype('int8'), [448,]), ), 3)
call_7219 = relay.TupleGetItem(func_164_call(relay.reshape(const_7216.astype('float64'), [4, 2, 3]), relay.reshape(const_7217.astype('int8'), [28,]), relay.reshape(const_7218.astype('int8'), [448,]), ), 3)
func_3245_call = mod.get_global_var('func_3245')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_7220 = relay.TupleGetItem(func_3245_call(), 0)
call_7221 = relay.TupleGetItem(func_3246_call(), 0)
output = relay.Tuple([call_7212,call_7215,const_7216,const_7217,const_7218,call_7220,])
output2 = relay.Tuple([call_7213,call_7219,const_7216,const_7217,const_7218,call_7221,])
func_7257 = relay.Function([], output)
mod['func_7257'] = func_7257
mod = relay.transform.InferType()(mod)
output = func_7257()
func_7258 = relay.Function([], output)
mutated_mod['func_7258'] = func_7258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_7310 = relay.TupleGetItem(func_1309_call(), 0)
call_7311 = relay.TupleGetItem(func_1311_call(), 0)
output = relay.Tuple([call_7310,])
output2 = relay.Tuple([call_7311,])
func_7312 = relay.Function([], output)
mod['func_7312'] = func_7312
mod = relay.transform.InferType()(mod)
output = func_7312()
func_7313 = relay.Function([], output)
mutated_mod['func_7313'] = func_7313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4436_call = mod.get_global_var('func_4436')
func_4438_call = mutated_mod.get_global_var('func_4438')
call_7415 = relay.TupleGetItem(func_4436_call(), 0)
call_7416 = relay.TupleGetItem(func_4438_call(), 0)
func_4301_call = mod.get_global_var('func_4301')
func_4303_call = mutated_mod.get_global_var('func_4303')
call_7421 = func_4301_call()
call_7422 = func_4301_call()
output = relay.Tuple([call_7415,call_7421,])
output2 = relay.Tuple([call_7416,call_7422,])
func_7424 = relay.Function([], output)
mod['func_7424'] = func_7424
mod = relay.transform.InferType()(mod)
mutated_mod['func_7424'] = func_7424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7424_call = mutated_mod.get_global_var('func_7424')
call_7425 = func_7424_call()
output = call_7425
func_7426 = relay.Function([], output)
mutated_mod['func_7426'] = func_7426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4252_call = mod.get_global_var('func_4252')
func_4254_call = mutated_mod.get_global_var('func_4254')
call_7443 = relay.TupleGetItem(func_4252_call(), 1)
call_7444 = relay.TupleGetItem(func_4254_call(), 1)
func_7086_call = mod.get_global_var('func_7086')
func_7088_call = mutated_mod.get_global_var('func_7088')
call_7451 = relay.TupleGetItem(func_7086_call(), 0)
call_7452 = relay.TupleGetItem(func_7088_call(), 0)
output = relay.Tuple([call_7443,call_7451,])
output2 = relay.Tuple([call_7444,call_7452,])
func_7461 = relay.Function([], output)
mod['func_7461'] = func_7461
mod = relay.transform.InferType()(mod)
output = func_7461()
func_7462 = relay.Function([], output)
mutated_mod['func_7462'] = func_7462
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7499 = relay.const([[[8],[-9],[-6],[-3],[-3],[-9],[7],[-4],[4],[-4]],[[-8],[2],[-5],[8],[-1],[-5],[-1],[-6],[-7],[10]],[[-7],[-1],[-10],[3],[-4],[5],[-5],[6],[4],[-6]],[[-5],[6],[7],[4],[10],[-6],[-2],[1],[1],[-6]],[[-4],[10],[5],[-9],[-10],[-4],[6],[-10],[1],[-7]],[[-8],[7],[-9],[10],[6],[-6],[6],[-10],[-10],[2]],[[6],[4],[7],[4],[-9],[-10],[-5],[5],[-7],[3]],[[-2],[4],[5],[-10],[2],[6],[7],[9],[5],[1]],[[-6],[1],[8],[-5],[-4],[8],[7],[3],[-5],[6]]], dtype = "uint32")#candidate|7499|(9, 10, 1)|const|uint32
var_7500 = relay.var("var_7500", dtype = "uint32", shape = (9, 10, 13))#candidate|7500|(9, 10, 13)|var|uint32
bop_7501 = relay.maximum(const_7499.astype('uint32'), var_7500.astype('uint32')) # shape=(9, 10, 13)
func_6362_call = mod.get_global_var('func_6362')
func_6363_call = mutated_mod.get_global_var('func_6363')
call_7507 = relay.TupleGetItem(func_6362_call(), 0)
call_7508 = relay.TupleGetItem(func_6363_call(), 0)
output = relay.Tuple([bop_7501,call_7507,])
output2 = relay.Tuple([bop_7501,call_7508,])
func_7517 = relay.Function([var_7500,], output)
mod['func_7517'] = func_7517
mod = relay.transform.InferType()(mod)
var_7518 = relay.var("var_7518", dtype = "uint32", shape = (9, 10, 13))#candidate|7518|(9, 10, 13)|var|uint32
output = func_7517(var_7518)
func_7519 = relay.Function([var_7518], output)
mutated_mod['func_7519'] = func_7519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4402_call = mod.get_global_var('func_4402')
func_4403_call = mutated_mod.get_global_var('func_4403')
call_7521 = relay.TupleGetItem(func_4402_call(), 0)
call_7522 = relay.TupleGetItem(func_4403_call(), 0)
func_7461_call = mod.get_global_var('func_7461')
func_7462_call = mutated_mod.get_global_var('func_7462')
call_7535 = relay.TupleGetItem(func_7461_call(), 0)
call_7536 = relay.TupleGetItem(func_7462_call(), 0)
output = relay.Tuple([call_7521,call_7535,])
output2 = relay.Tuple([call_7522,call_7536,])
func_7542 = relay.Function([], output)
mod['func_7542'] = func_7542
mod = relay.transform.InferType()(mod)
mutated_mod['func_7542'] = func_7542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7542_call = mutated_mod.get_global_var('func_7542')
call_7543 = func_7542_call()
output = call_7543
func_7544 = relay.Function([], output)
mutated_mod['func_7544'] = func_7544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7086_call = mod.get_global_var('func_7086')
func_7088_call = mutated_mod.get_global_var('func_7088')
call_7554 = relay.TupleGetItem(func_7086_call(), 2)
call_7555 = relay.TupleGetItem(func_7088_call(), 2)
output = relay.Tuple([call_7554,])
output2 = relay.Tuple([call_7555,])
func_7567 = relay.Function([], output)
mod['func_7567'] = func_7567
mod = relay.transform.InferType()(mod)
mutated_mod['func_7567'] = func_7567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7567_call = mutated_mod.get_global_var('func_7567')
call_7568 = func_7567_call()
output = call_7568
func_7569 = relay.Function([], output)
mutated_mod['func_7569'] = func_7569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7591 = relay.var("var_7591", dtype = "float64", shape = (11, 16, 10))#candidate|7591|(11, 16, 10)|var|float64
var_7592 = relay.var("var_7592", dtype = "float64", shape = (11, 16, 10))#candidate|7592|(11, 16, 10)|var|float64
bop_7593 = relay.divide(var_7591.astype('float64'), relay.reshape(var_7592.astype('float64'), relay.shape_of(var_7591))) # shape=(11, 16, 10)
func_7140_call = mod.get_global_var('func_7140')
func_7141_call = mutated_mod.get_global_var('func_7141')
call_7603 = relay.TupleGetItem(func_7140_call(), 3)
call_7604 = relay.TupleGetItem(func_7141_call(), 3)
output = relay.Tuple([bop_7593,call_7603,])
output2 = relay.Tuple([bop_7593,call_7604,])
func_7622 = relay.Function([var_7591,var_7592,], output)
mod['func_7622'] = func_7622
mod = relay.transform.InferType()(mod)
var_7623 = relay.var("var_7623", dtype = "float64", shape = (11, 16, 10))#candidate|7623|(11, 16, 10)|var|float64
var_7624 = relay.var("var_7624", dtype = "float64", shape = (11, 16, 10))#candidate|7624|(11, 16, 10)|var|float64
output = func_7622(var_7623,var_7624,)
func_7625 = relay.Function([var_7623,var_7624,], output)
mutated_mod['func_7625'] = func_7625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2397_call = mod.get_global_var('func_2397')
func_2398_call = mutated_mod.get_global_var('func_2398')
call_7627 = relay.TupleGetItem(func_2397_call(), 2)
call_7628 = relay.TupleGetItem(func_2398_call(), 2)
output = call_7627
output2 = call_7628
func_7633 = relay.Function([], output)
mod['func_7633'] = func_7633
mod = relay.transform.InferType()(mod)
output = func_7633()
func_7634 = relay.Function([], output)
mutated_mod['func_7634'] = func_7634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_7680 = relay.TupleGetItem(func_1309_call(), 0)
call_7681 = relay.TupleGetItem(func_1311_call(), 0)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_7687 = relay.TupleGetItem(func_975_call(), 0)
call_7688 = relay.TupleGetItem(func_976_call(), 0)
func_159_call = mod.get_global_var('func_159')
func_164_call = mutated_mod.get_global_var('func_164')
const_7697 = relay.const([[0.162635,-2.623512,-0.224758,1.471425,5.671670,-1.242414,-3.843687,-6.149215,-2.739515,8.224296,-1.749678,7.817544,-3.929426,0.972847,-6.270165,-9.660516,3.581052,-2.815153,-4.903055,-4.370204,-3.273108,9.453379,-1.654534,7.096103]], dtype = "float64")#candidate|7697|(1, 24)|const|float64
const_7698 = relay.const([6,2,-9,-8,3,-10,10,-8,5,6,-6,-6,-8,6,-6,6,5,7,6,-6,3,-9,5,-5,-5,4,4,4], dtype = "int8")#candidate|7698|(28,)|const|int8
var_7699 = relay.var("var_7699", dtype = "int8", shape = (448,))#candidate|7699|(448,)|var|int8
call_7696 = relay.TupleGetItem(func_159_call(relay.reshape(const_7697.astype('float64'), [4, 2, 3]), relay.reshape(const_7698.astype('int8'), [28,]), relay.reshape(var_7699.astype('int8'), [448,]), ), 0)
call_7700 = relay.TupleGetItem(func_164_call(relay.reshape(const_7697.astype('float64'), [4, 2, 3]), relay.reshape(const_7698.astype('int8'), [28,]), relay.reshape(var_7699.astype('int8'), [448,]), ), 0)
func_3245_call = mod.get_global_var('func_3245')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_7716 = relay.TupleGetItem(func_3245_call(), 2)
call_7717 = relay.TupleGetItem(func_3246_call(), 2)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_7728 = relay.TupleGetItem(func_6480_call(), 0)
call_7729 = relay.TupleGetItem(func_6482_call(), 0)
output = relay.Tuple([call_7680,call_7687,call_7696,const_7697,const_7698,var_7699,call_7716,call_7728,])
output2 = relay.Tuple([call_7681,call_7688,call_7700,const_7697,const_7698,var_7699,call_7717,call_7729,])
func_7732 = relay.Function([var_7699,], output)
mod['func_7732'] = func_7732
mod = relay.transform.InferType()(mod)
mutated_mod['func_7732'] = func_7732
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7733 = relay.var("var_7733", dtype = "int8", shape = (448,))#candidate|7733|(448,)|var|int8
func_7732_call = mutated_mod.get_global_var('func_7732')
call_7734 = func_7732_call(var_7733)
output = call_7734
func_7735 = relay.Function([var_7733], output)
mutated_mod['func_7735'] = func_7735
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7748 = relay.var("var_7748", dtype = "float64", shape = (13, 15, 12))#candidate|7748|(13, 15, 12)|var|float64
var_7749 = relay.var("var_7749", dtype = "float64", shape = (13, 15, 12))#candidate|7749|(13, 15, 12)|var|float64
bop_7750 = relay.greater(var_7748.astype('bool'), relay.reshape(var_7749.astype('bool'), relay.shape_of(var_7748))) # shape=(13, 15, 12)
output = bop_7750
output2 = bop_7750
func_7754 = relay.Function([var_7748,var_7749,], output)
mod['func_7754'] = func_7754
mod = relay.transform.InferType()(mod)
mutated_mod['func_7754'] = func_7754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7754_call = mutated_mod.get_global_var('func_7754')
var_7756 = relay.var("var_7756", dtype = "float64", shape = (13, 15, 12))#candidate|7756|(13, 15, 12)|var|float64
var_7757 = relay.var("var_7757", dtype = "float64", shape = (13, 15, 12))#candidate|7757|(13, 15, 12)|var|float64
call_7755 = func_7754_call(var_7756,var_7757,)
output = call_7755
func_7758 = relay.Function([var_7756,var_7757,], output)
mutated_mod['func_7758'] = func_7758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5293_call = mod.get_global_var('func_5293')
func_5294_call = mutated_mod.get_global_var('func_5294')
call_7776 = func_5293_call()
call_7777 = func_5293_call()
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_7780 = relay.TupleGetItem(func_6480_call(), 0)
call_7781 = relay.TupleGetItem(func_6482_call(), 0)
output = relay.Tuple([call_7776,call_7780,])
output2 = relay.Tuple([call_7777,call_7781,])
func_7795 = relay.Function([], output)
mod['func_7795'] = func_7795
mod = relay.transform.InferType()(mod)
mutated_mod['func_7795'] = func_7795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7795_call = mutated_mod.get_global_var('func_7795')
call_7796 = func_7795_call()
output = call_7796
func_7797 = relay.Function([], output)
mutated_mod['func_7797'] = func_7797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3262_call = mod.get_global_var('func_3262')
func_3264_call = mutated_mod.get_global_var('func_3264')
call_7811 = relay.TupleGetItem(func_3262_call(), 0)
call_7812 = relay.TupleGetItem(func_3264_call(), 0)
output = relay.Tuple([call_7811,])
output2 = relay.Tuple([call_7812,])
func_7843 = relay.Function([], output)
mod['func_7843'] = func_7843
mod = relay.transform.InferType()(mod)
output = func_7843()
func_7844 = relay.Function([], output)
mutated_mod['func_7844'] = func_7844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7542_call = mod.get_global_var('func_7542')
func_7544_call = mutated_mod.get_global_var('func_7544')
call_7982 = relay.TupleGetItem(func_7542_call(), 0)
call_7983 = relay.TupleGetItem(func_7544_call(), 0)
func_3961_call = mod.get_global_var('func_3961')
func_3963_call = mutated_mod.get_global_var('func_3963')
call_7987 = relay.TupleGetItem(func_3961_call(), 0)
call_7988 = relay.TupleGetItem(func_3963_call(), 0)
func_7542_call = mod.get_global_var('func_7542')
func_7544_call = mutated_mod.get_global_var('func_7544')
call_7990 = relay.TupleGetItem(func_7542_call(), 1)
call_7991 = relay.TupleGetItem(func_7544_call(), 1)
func_5155_call = mod.get_global_var('func_5155')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_8021 = relay.TupleGetItem(func_5155_call(), 0)
call_8022 = relay.TupleGetItem(func_5157_call(), 0)
output = relay.Tuple([call_7982,call_7987,call_7990,call_8021,])
output2 = relay.Tuple([call_7983,call_7988,call_7991,call_8022,])
func_8027 = relay.Function([], output)
mod['func_8027'] = func_8027
mod = relay.transform.InferType()(mod)
mutated_mod['func_8027'] = func_8027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8027_call = mutated_mod.get_global_var('func_8027')
call_8028 = func_8027_call()
output = call_8028
func_8029 = relay.Function([], output)
mutated_mod['func_8029'] = func_8029
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8068 = relay.var("var_8068", dtype = "float64", shape = (1, 1, 6))#candidate|8068|(1, 1, 6)|var|float64
uop_8069 = relay.cos(var_8068.astype('float64')) # shape=(1, 1, 6)
uop_8071 = relay.erf(var_8068.astype('float64')) # shape=(1, 1, 6)
uop_8080 = relay.sin(uop_8069.astype('float64')) # shape=(1, 1, 6)
output = relay.Tuple([uop_8071,uop_8080,])
output2 = relay.Tuple([uop_8071,uop_8080,])
func_8083 = relay.Function([var_8068,], output)
mod['func_8083'] = func_8083
mod = relay.transform.InferType()(mod)
mutated_mod['func_8083'] = func_8083
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8084 = relay.var("var_8084", dtype = "float64", shape = (1, 1, 6))#candidate|8084|(1, 1, 6)|var|float64
func_8083_call = mutated_mod.get_global_var('func_8083')
call_8085 = func_8083_call(var_8084)
output = call_8085
func_8086 = relay.Function([var_8084], output)
mutated_mod['func_8086'] = func_8086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4402_call = mod.get_global_var('func_4402')
func_4403_call = mutated_mod.get_global_var('func_4403')
call_8097 = relay.TupleGetItem(func_4402_call(), 0)
call_8098 = relay.TupleGetItem(func_4403_call(), 0)
func_6779_call = mod.get_global_var('func_6779')
func_6781_call = mutated_mod.get_global_var('func_6781')
call_8100 = relay.TupleGetItem(func_6779_call(), 0)
call_8101 = relay.TupleGetItem(func_6781_call(), 0)
func_7795_call = mod.get_global_var('func_7795')
func_7797_call = mutated_mod.get_global_var('func_7797')
call_8107 = relay.TupleGetItem(func_7795_call(), 0)
call_8108 = relay.TupleGetItem(func_7797_call(), 0)
output = relay.Tuple([call_8097,call_8100,call_8107,])
output2 = relay.Tuple([call_8098,call_8101,call_8108,])
func_8114 = relay.Function([], output)
mod['func_8114'] = func_8114
mod = relay.transform.InferType()(mod)
output = func_8114()
func_8115 = relay.Function([], output)
mutated_mod['func_8115'] = func_8115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_8170 = relay.TupleGetItem(func_1104_call(), 0)
call_8171 = relay.TupleGetItem(func_1105_call(), 0)
output = call_8170
output2 = call_8171
func_8182 = relay.Function([], output)
mod['func_8182'] = func_8182
mod = relay.transform.InferType()(mod)
mutated_mod['func_8182'] = func_8182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8182_call = mutated_mod.get_global_var('func_8182')
call_8183 = func_8182_call()
output = call_8183
func_8184 = relay.Function([], output)
mutated_mod['func_8184'] = func_8184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8271 = relay.var("var_8271", dtype = "int8", shape = ())#candidate|8271|()|var|int8
var_8272 = relay.var("var_8272", dtype = "int8", shape = (9, 16, 1))#candidate|8272|(9, 16, 1)|var|int8
bop_8273 = relay.subtract(var_8271.astype('int8'), var_8272.astype('int8')) # shape=(9, 16, 1)
bop_8280 = relay.greater_equal(var_8271.astype('bool'), var_8272.astype('bool')) # shape=(9, 16, 1)
output = relay.Tuple([bop_8273,bop_8280,])
output2 = relay.Tuple([bop_8273,bop_8280,])
func_8288 = relay.Function([var_8271,var_8272,], output)
mod['func_8288'] = func_8288
mod = relay.transform.InferType()(mod)
var_8289 = relay.var("var_8289", dtype = "int8", shape = ())#candidate|8289|()|var|int8
var_8290 = relay.var("var_8290", dtype = "int8", shape = (9, 16, 1))#candidate|8290|(9, 16, 1)|var|int8
output = func_8288(var_8289,var_8290,)
func_8291 = relay.Function([var_8289,var_8290,], output)
mutated_mod['func_8291'] = func_8291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1157_call = mod.get_global_var('func_1157')
func_1158_call = mutated_mod.get_global_var('func_1158')
call_8342 = func_1157_call()
call_8343 = func_1157_call()
output = call_8342
output2 = call_8343
func_8349 = relay.Function([], output)
mod['func_8349'] = func_8349
mod = relay.transform.InferType()(mod)
mutated_mod['func_8349'] = func_8349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8349_call = mutated_mod.get_global_var('func_8349')
call_8350 = func_8349_call()
output = call_8350
func_8351 = relay.Function([], output)
mutated_mod['func_8351'] = func_8351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_8354 = relay.TupleGetItem(func_975_call(), 0)
call_8355 = relay.TupleGetItem(func_976_call(), 0)
output = call_8354
output2 = call_8355
func_8356 = relay.Function([], output)
mod['func_8356'] = func_8356
mod = relay.transform.InferType()(mod)
mutated_mod['func_8356'] = func_8356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8356_call = mutated_mod.get_global_var('func_8356')
call_8357 = func_8356_call()
output = call_8357
func_8358 = relay.Function([], output)
mutated_mod['func_8358'] = func_8358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3931_call = mod.get_global_var('func_3931')
func_3932_call = mutated_mod.get_global_var('func_3932')
call_8424 = relay.TupleGetItem(func_3931_call(), 0)
call_8425 = relay.TupleGetItem(func_3932_call(), 0)
output = relay.Tuple([call_8424,])
output2 = relay.Tuple([call_8425,])
func_8429 = relay.Function([], output)
mod['func_8429'] = func_8429
mod = relay.transform.InferType()(mod)
mutated_mod['func_8429'] = func_8429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8429_call = mutated_mod.get_global_var('func_8429')
call_8430 = func_8429_call()
output = call_8430
func_8431 = relay.Function([], output)
mutated_mod['func_8431'] = func_8431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3012_call = mod.get_global_var('func_3012')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_8451 = relay.TupleGetItem(func_3012_call(), 0)
call_8452 = relay.TupleGetItem(func_3013_call(), 0)
func_8182_call = mod.get_global_var('func_8182')
func_8184_call = mutated_mod.get_global_var('func_8184')
call_8458 = func_8182_call()
call_8459 = func_8182_call()
func_6681_call = mod.get_global_var('func_6681')
func_6683_call = mutated_mod.get_global_var('func_6683')
call_8470 = relay.TupleGetItem(func_6681_call(), 1)
call_8471 = relay.TupleGetItem(func_6683_call(), 1)
func_5293_call = mod.get_global_var('func_5293')
func_5294_call = mutated_mod.get_global_var('func_5294')
call_8490 = func_5293_call()
call_8491 = func_5293_call()
func_6779_call = mod.get_global_var('func_6779')
func_6781_call = mutated_mod.get_global_var('func_6781')
call_8495 = relay.TupleGetItem(func_6779_call(), 0)
call_8496 = relay.TupleGetItem(func_6781_call(), 0)
output = relay.Tuple([call_8451,call_8458,call_8470,call_8490,call_8495,])
output2 = relay.Tuple([call_8452,call_8459,call_8471,call_8491,call_8496,])
func_8517 = relay.Function([], output)
mod['func_8517'] = func_8517
mod = relay.transform.InferType()(mod)
mutated_mod['func_8517'] = func_8517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8517_call = mutated_mod.get_global_var('func_8517')
call_8518 = func_8517_call()
output = call_8518
func_8519 = relay.Function([], output)
mutated_mod['func_8519'] = func_8519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7567_call = mod.get_global_var('func_7567')
func_7569_call = mutated_mod.get_global_var('func_7569')
call_8530 = relay.TupleGetItem(func_7567_call(), 0)
call_8531 = relay.TupleGetItem(func_7569_call(), 0)
func_6372_call = mod.get_global_var('func_6372')
func_6375_call = mutated_mod.get_global_var('func_6375')
const_8544 = relay.const([9.620182,-5.440765,-7.326157,-0.156569,2.843004,-5.160536,2.815704,4.650702,7.290823,-5.231864,-4.252050,7.914778,-5.916775,9.971690,5.213163,-0.077343,5.961132,-1.164236,5.767009,-2.057458,-2.815850,0.988063,1.790984,4.516976,-6.343065,-8.776860,0.036562,2.060428,2.113758,6.796799,3.542697,-7.125187,-6.357263,-1.132800,9.700212,-7.084806,-5.040864,-0.500081,0.424142,-2.433691,3.419094,-7.028047], dtype = "float32")#candidate|8544|(42,)|const|float32
call_8543 = relay.TupleGetItem(func_6372_call(relay.reshape(const_8544.astype('float32'), [7, 1, 6])), 0)
call_8545 = relay.TupleGetItem(func_6375_call(relay.reshape(const_8544.astype('float32'), [7, 1, 6])), 0)
output = relay.Tuple([call_8530,call_8543,const_8544,])
output2 = relay.Tuple([call_8531,call_8545,const_8544,])
func_8552 = relay.Function([], output)
mod['func_8552'] = func_8552
mod = relay.transform.InferType()(mod)
mutated_mod['func_8552'] = func_8552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8552_call = mutated_mod.get_global_var('func_8552')
call_8553 = func_8552_call()
output = call_8553
func_8554 = relay.Function([], output)
mutated_mod['func_8554'] = func_8554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7312_call = mod.get_global_var('func_7312')
func_7313_call = mutated_mod.get_global_var('func_7313')
call_8593 = relay.TupleGetItem(func_7312_call(), 0)
call_8594 = relay.TupleGetItem(func_7313_call(), 0)
func_2582_call = mod.get_global_var('func_2582')
func_2583_call = mutated_mod.get_global_var('func_2583')
call_8612 = relay.TupleGetItem(func_2582_call(), 1)
call_8613 = relay.TupleGetItem(func_2583_call(), 1)
func_6592_call = mod.get_global_var('func_6592')
func_6593_call = mutated_mod.get_global_var('func_6593')
call_8618 = func_6592_call()
call_8619 = func_6592_call()
output = relay.Tuple([call_8593,call_8612,call_8618,])
output2 = relay.Tuple([call_8594,call_8613,call_8619,])
func_8630 = relay.Function([], output)
mod['func_8630'] = func_8630
mod = relay.transform.InferType()(mod)
mutated_mod['func_8630'] = func_8630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8630_call = mutated_mod.get_global_var('func_8630')
call_8631 = func_8630_call()
output = call_8631
func_8632 = relay.Function([], output)
mutated_mod['func_8632'] = func_8632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_8678 = func_2025_call()
call_8679 = func_2025_call()
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_8693 = relay.TupleGetItem(func_1864_call(), 1)
call_8694 = relay.TupleGetItem(func_1865_call(), 1)
output = relay.Tuple([call_8678,call_8693,])
output2 = relay.Tuple([call_8679,call_8694,])
func_8704 = relay.Function([], output)
mod['func_8704'] = func_8704
mod = relay.transform.InferType()(mod)
mutated_mod['func_8704'] = func_8704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8704_call = mutated_mod.get_global_var('func_8704')
call_8705 = func_8704_call()
output = call_8705
func_8706 = relay.Function([], output)
mutated_mod['func_8706'] = func_8706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6779_call = mod.get_global_var('func_6779')
func_6781_call = mutated_mod.get_global_var('func_6781')
call_8759 = relay.TupleGetItem(func_6779_call(), 0)
call_8760 = relay.TupleGetItem(func_6781_call(), 0)
func_5344_call = mod.get_global_var('func_5344')
func_5346_call = mutated_mod.get_global_var('func_5346')
call_8767 = relay.TupleGetItem(func_5344_call(), 0)
call_8768 = relay.TupleGetItem(func_5346_call(), 0)
func_6955_call = mod.get_global_var('func_6955')
func_6957_call = mutated_mod.get_global_var('func_6957')
call_8771 = relay.TupleGetItem(func_6955_call(), 0)
call_8772 = relay.TupleGetItem(func_6957_call(), 0)
output = relay.Tuple([call_8759,call_8767,call_8771,])
output2 = relay.Tuple([call_8760,call_8768,call_8772,])
func_8783 = relay.Function([], output)
mod['func_8783'] = func_8783
mod = relay.transform.InferType()(mod)
mutated_mod['func_8783'] = func_8783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8783_call = mutated_mod.get_global_var('func_8783')
call_8784 = func_8783_call()
output = call_8784
func_8785 = relay.Function([], output)
mutated_mod['func_8785'] = func_8785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8630_call = mod.get_global_var('func_8630')
func_8632_call = mutated_mod.get_global_var('func_8632')
call_8893 = relay.TupleGetItem(func_8630_call(), 1)
call_8894 = relay.TupleGetItem(func_8632_call(), 1)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_8895 = relay.TupleGetItem(func_2815_call(), 1)
call_8896 = relay.TupleGetItem(func_2816_call(), 1)
func_8356_call = mod.get_global_var('func_8356')
func_8358_call = mutated_mod.get_global_var('func_8358')
call_8897 = func_8356_call()
call_8898 = func_8356_call()
func_8356_call = mod.get_global_var('func_8356')
func_8358_call = mutated_mod.get_global_var('func_8358')
call_8899 = func_8356_call()
call_8900 = func_8356_call()
func_8083_call = mod.get_global_var('func_8083')
func_8086_call = mutated_mod.get_global_var('func_8086')
const_8907 = relay.const([-4.190860,-4.521153,4.709616,5.576106,7.894527,2.974995], dtype = "float64")#candidate|8907|(6,)|const|float64
call_8906 = relay.TupleGetItem(func_8083_call(relay.reshape(const_8907.astype('float64'), [1, 1, 6])), 1)
call_8908 = relay.TupleGetItem(func_8086_call(relay.reshape(const_8907.astype('float64'), [1, 1, 6])), 1)
func_8783_call = mod.get_global_var('func_8783')
func_8785_call = mutated_mod.get_global_var('func_8785')
call_8911 = relay.TupleGetItem(func_8783_call(), 2)
call_8912 = relay.TupleGetItem(func_8785_call(), 2)
var_8915 = relay.var("var_8915", dtype = "float64", shape = (6, 3, 6))#candidate|8915|(6, 3, 6)|var|float64
bop_8916 = relay.greater_equal(call_8906.astype('bool'), var_8915.astype('bool')) # shape=(6, 3, 6)
bop_8919 = relay.greater_equal(call_8908.astype('bool'), var_8915.astype('bool')) # shape=(6, 3, 6)
func_8552_call = mod.get_global_var('func_8552')
func_8554_call = mutated_mod.get_global_var('func_8554')
call_8924 = relay.TupleGetItem(func_8552_call(), 1)
call_8925 = relay.TupleGetItem(func_8554_call(), 1)
const_8935 = relay.const([[[-7.399461,3.470713,-8.066859,-4.206647,5.490697,0.671452],[-8.560270,1.915188,-1.939467,-3.503715,-0.499196,-9.796934],[-8.535927,-9.805480,6.972222,6.970837,6.682869,8.211453]],[[3.592002,9.330674,8.181190,2.260050,1.166423,-8.821024],[3.799263,-2.255274,2.738525,-9.466932,-0.179067,7.153537],[-5.541818,4.460066,9.669369,8.108219,-5.521528,0.815240]],[[0.967259,-2.619574,9.929199,5.895304,3.201941,9.250170],[-9.444241,-5.847294,-9.500953,-6.946789,6.492033,-2.353546],[-2.339540,1.150271,-4.525493,4.850836,0.814114,4.032547]],[[-7.674542,0.610920,-2.910094,8.774599,6.463920,6.706828],[0.494761,-1.832148,-4.600964,-3.277975,4.338269,4.502241],[-0.099676,1.973528,-9.596908,7.634349,0.067549,1.244873]],[[1.580281,-5.863475,-5.457260,-1.745001,-0.691071,-6.090753],[-0.794968,9.803577,2.148490,9.371518,0.534091,7.121811],[3.646570,1.821785,-2.154953,3.192382,3.965440,-8.645630]],[[7.929715,5.846128,7.555092,-8.048117,-4.309081,8.170802],[1.653686,-3.475755,-8.971309,-8.648005,-0.224584,-7.122119],[-0.579641,-1.862345,-6.812872,-4.713615,9.924385,1.955608]],[[4.637724,-4.121396,8.025881,9.756995,3.438461,-4.798221],[-0.544779,8.820160,-7.584186,0.597650,5.185019,-7.787048],[-3.634067,-6.282002,-9.225878,-2.963069,3.504879,-2.840768]],[[4.422790,7.875482,9.445713,-1.693246,5.831355,-5.300311],[6.644946,-6.530377,4.668184,-8.169035,9.315207,3.550117],[-1.942117,-1.805920,2.988197,3.706357,-9.209271,4.381331]],[[-5.342654,6.923708,3.476454,2.591886,2.366482,-6.482430],[-0.603977,-4.133276,4.089910,1.559695,-8.532715,5.516385],[-4.685847,-3.215541,-2.784178,-7.631494,4.981190,-7.691490]],[[5.244336,0.760371,9.093403,3.006340,7.420774,-2.267480],[-9.189751,-7.594369,7.722040,-3.224795,-4.616907,-7.833252],[-3.263283,6.458154,5.885395,-8.115232,8.342886,6.246047]],[[5.863602,-3.280652,0.364809,1.193056,4.873172,-0.972663],[-0.520613,-4.894920,5.552883,8.962977,-8.729817,0.898051],[-8.535760,-8.723469,9.648579,-6.789609,6.908059,2.254496]],[[8.662014,-8.501448,9.360146,0.217488,4.568173,-1.977104],[1.880986,-6.332790,6.381459,3.991058,5.128325,9.443178],[2.770917,-9.516639,0.263223,2.457472,-7.330232,0.107543]]], dtype = "float64")#candidate|8935|(12, 3, 6)|const|float64
bop_8936 = relay.logical_or(call_8906.astype('bool'), const_8935.astype('bool')) # shape=(12, 3, 6)
bop_8939 = relay.logical_or(call_8908.astype('bool'), const_8935.astype('bool')) # shape=(12, 3, 6)
func_7633_call = mod.get_global_var('func_7633')
func_7634_call = mutated_mod.get_global_var('func_7634')
call_8950 = func_7633_call()
call_8951 = func_7633_call()
func_8288_call = mod.get_global_var('func_8288')
func_8291_call = mutated_mod.get_global_var('func_8291')
const_8962 = relay.const(-1, dtype = "int8")#candidate|8962|()|const|int8
var_8963 = relay.var("var_8963", dtype = "int8", shape = (144,))#candidate|8963|(144,)|var|int8
call_8961 = relay.TupleGetItem(func_8288_call(relay.reshape(const_8962.astype('int8'), []), relay.reshape(var_8963.astype('int8'), [9, 16, 1]), ), 0)
call_8964 = relay.TupleGetItem(func_8291_call(relay.reshape(const_8962.astype('int8'), []), relay.reshape(var_8963.astype('int8'), [9, 16, 1]), ), 0)
func_2229_call = mod.get_global_var('func_2229')
func_2231_call = mutated_mod.get_global_var('func_2231')
call_8971 = relay.TupleGetItem(func_2229_call(), 0)
call_8972 = relay.TupleGetItem(func_2231_call(), 0)
func_8083_call = mod.get_global_var('func_8083')
func_8086_call = mutated_mod.get_global_var('func_8086')
call_8977 = relay.TupleGetItem(func_8083_call(relay.reshape(const_8907.astype('float64'), [1, 1, 6])), 1)
call_8978 = relay.TupleGetItem(func_8086_call(relay.reshape(const_8907.astype('float64'), [1, 1, 6])), 1)
output = relay.Tuple([call_8893,call_8895,call_8897,call_8899,const_8907,call_8911,bop_8916,call_8924,bop_8936,call_8950,call_8961,const_8962,var_8963,call_8971,call_8977,])
output2 = relay.Tuple([call_8894,call_8896,call_8898,call_8900,const_8907,call_8912,bop_8919,call_8925,bop_8939,call_8951,call_8964,const_8962,var_8963,call_8972,call_8978,])
func_8985 = relay.Function([var_8915,var_8963,], output)
mod['func_8985'] = func_8985
mod = relay.transform.InferType()(mod)
mutated_mod['func_8985'] = func_8985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8985_call = mutated_mod.get_global_var('func_8985')
var_8987 = relay.var("var_8987", dtype = "float64", shape = (6, 3, 6))#candidate|8987|(6, 3, 6)|var|float64
var_8988 = relay.var("var_8988", dtype = "int8", shape = (144,))#candidate|8988|(144,)|var|int8
call_8986 = func_8985_call(var_8987,var_8988,)
output = call_8986
func_8989 = relay.Function([var_8987,var_8988,], output)
mutated_mod['func_8989'] = func_8989
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9005 = relay.var("var_9005", dtype = "bool", shape = (16, 5, 3))#candidate|9005|(16, 5, 3)|var|bool
var_9006 = relay.var("var_9006", dtype = "bool", shape = (16, 5, 3))#candidate|9006|(16, 5, 3)|var|bool
bop_9007 = relay.logical_and(var_9005.astype('bool'), relay.reshape(var_9006.astype('bool'), relay.shape_of(var_9005))) # shape=(16, 5, 3)
uop_9012 = relay.sinh(var_9006.astype('float64')) # shape=(16, 5, 3)
bop_9020 = relay.mod(uop_9012.astype('float64'), relay.reshape(var_9005.astype('float64'), relay.shape_of(uop_9012))) # shape=(16, 5, 3)
output = relay.Tuple([bop_9007,bop_9020,])
output2 = relay.Tuple([bop_9007,bop_9020,])
func_9023 = relay.Function([var_9005,var_9006,], output)
mod['func_9023'] = func_9023
mod = relay.transform.InferType()(mod)
mutated_mod['func_9023'] = func_9023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9023_call = mutated_mod.get_global_var('func_9023')
var_9025 = relay.var("var_9025", dtype = "bool", shape = (16, 5, 3))#candidate|9025|(16, 5, 3)|var|bool
var_9026 = relay.var("var_9026", dtype = "bool", shape = (16, 5, 3))#candidate|9026|(16, 5, 3)|var|bool
call_9024 = func_9023_call(var_9025,var_9026,)
output = call_9024
func_9027 = relay.Function([var_9025,var_9026,], output)
mutated_mod['func_9027'] = func_9027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7086_call = mod.get_global_var('func_7086')
func_7088_call = mutated_mod.get_global_var('func_7088')
call_9115 = relay.TupleGetItem(func_7086_call(), 4)
call_9116 = relay.TupleGetItem(func_7088_call(), 4)
uop_9123 = relay.atan(call_9115.astype('float32')) # shape=(400,)
uop_9125 = relay.atan(call_9116.astype('float32')) # shape=(400,)
output = relay.Tuple([uop_9123,])
output2 = relay.Tuple([uop_9125,])
func_9126 = relay.Function([], output)
mod['func_9126'] = func_9126
mod = relay.transform.InferType()(mod)
output = func_9126()
func_9127 = relay.Function([], output)
mutated_mod['func_9127'] = func_9127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7001_call = mod.get_global_var('func_7001')
func_7003_call = mutated_mod.get_global_var('func_7003')
call_9159 = relay.TupleGetItem(func_7001_call(), 0)
call_9160 = relay.TupleGetItem(func_7003_call(), 0)
output = relay.Tuple([call_9159,])
output2 = relay.Tuple([call_9160,])
func_9171 = relay.Function([], output)
mod['func_9171'] = func_9171
mod = relay.transform.InferType()(mod)
mutated_mod['func_9171'] = func_9171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9171_call = mutated_mod.get_global_var('func_9171')
call_9172 = func_9171_call()
output = call_9172
func_9173 = relay.Function([], output)
mutated_mod['func_9173'] = func_9173
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9174 = relay.var("var_9174", dtype = "float64", shape = (3, 4, 11))#candidate|9174|(3, 4, 11)|var|float64
uop_9175 = relay.log(var_9174.astype('float64')) # shape=(3, 4, 11)
uop_9182 = relay.acos(uop_9175.astype('float64')) # shape=(3, 4, 11)
bop_9184 = relay.greater_equal(uop_9182.astype('bool'), relay.reshape(var_9174.astype('bool'), relay.shape_of(uop_9182))) # shape=(3, 4, 11)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_9187 = relay.TupleGetItem(func_1104_call(), 0)
call_9188 = relay.TupleGetItem(func_1105_call(), 0)
bop_9192 = relay.logical_xor(uop_9175.astype('int64'), relay.reshape(bop_9184.astype('int64'), relay.shape_of(uop_9175))) # shape=(3, 4, 11)
output = relay.Tuple([call_9187,bop_9192,])
output2 = relay.Tuple([call_9188,bop_9192,])
func_9195 = relay.Function([var_9174,], output)
mod['func_9195'] = func_9195
mod = relay.transform.InferType()(mod)
var_9196 = relay.var("var_9196", dtype = "float64", shape = (3, 4, 11))#candidate|9196|(3, 4, 11)|var|float64
output = func_9195(var_9196)
func_9197 = relay.Function([var_9196], output)
mutated_mod['func_9197'] = func_9197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5754_call = mod.get_global_var('func_5754')
func_5756_call = mutated_mod.get_global_var('func_5756')
call_9231 = func_5754_call()
call_9232 = func_5754_call()
output = call_9231
output2 = call_9232
func_9236 = relay.Function([], output)
mod['func_9236'] = func_9236
mod = relay.transform.InferType()(mod)
output = func_9236()
func_9237 = relay.Function([], output)
mutated_mod['func_9237'] = func_9237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mod.get_global_var('func_3961')
func_3963_call = mutated_mod.get_global_var('func_3963')
call_9260 = relay.TupleGetItem(func_3961_call(), 0)
call_9261 = relay.TupleGetItem(func_3963_call(), 0)
output = call_9260
output2 = call_9261
func_9293 = relay.Function([], output)
mod['func_9293'] = func_9293
mod = relay.transform.InferType()(mod)
mutated_mod['func_9293'] = func_9293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9293_call = mutated_mod.get_global_var('func_9293')
call_9294 = func_9293_call()
output = call_9294
func_9295 = relay.Function([], output)
mutated_mod['func_9295'] = func_9295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3838_call = mod.get_global_var('func_3838')
func_3840_call = mutated_mod.get_global_var('func_3840')
call_9334 = relay.TupleGetItem(func_3838_call(), 2)
call_9335 = relay.TupleGetItem(func_3840_call(), 2)
func_3245_call = mod.get_global_var('func_3245')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_9341 = relay.TupleGetItem(func_3245_call(), 0)
call_9342 = relay.TupleGetItem(func_3246_call(), 0)
func_8552_call = mod.get_global_var('func_8552')
func_8554_call = mutated_mod.get_global_var('func_8554')
call_9354 = relay.TupleGetItem(func_8552_call(), 1)
call_9355 = relay.TupleGetItem(func_8554_call(), 1)
output = relay.Tuple([call_9334,call_9341,call_9354,])
output2 = relay.Tuple([call_9335,call_9342,call_9355,])
func_9370 = relay.Function([], output)
mod['func_9370'] = func_9370
mod = relay.transform.InferType()(mod)
output = func_9370()
func_9371 = relay.Function([], output)
mutated_mod['func_9371'] = func_9371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3262_call = mod.get_global_var('func_3262')
func_3264_call = mutated_mod.get_global_var('func_3264')
call_9372 = relay.TupleGetItem(func_3262_call(), 1)
call_9373 = relay.TupleGetItem(func_3264_call(), 1)
output = relay.Tuple([call_9372,])
output2 = relay.Tuple([call_9373,])
func_9395 = relay.Function([], output)
mod['func_9395'] = func_9395
mod = relay.transform.InferType()(mod)
output = func_9395()
func_9396 = relay.Function([], output)
mutated_mod['func_9396'] = func_9396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4047_call = mod.get_global_var('func_4047')
func_4048_call = mutated_mod.get_global_var('func_4048')
call_9463 = relay.TupleGetItem(func_4047_call(), 0)
call_9464 = relay.TupleGetItem(func_4048_call(), 0)
output = call_9463
output2 = call_9464
func_9465 = relay.Function([], output)
mod['func_9465'] = func_9465
mod = relay.transform.InferType()(mod)
output = func_9465()
func_9466 = relay.Function([], output)
mutated_mod['func_9466'] = func_9466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_9520 = relay.TupleGetItem(func_1864_call(), 4)
call_9521 = relay.TupleGetItem(func_1865_call(), 4)
output = call_9520
output2 = call_9521
func_9535 = relay.Function([], output)
mod['func_9535'] = func_9535
mod = relay.transform.InferType()(mod)
output = func_9535()
func_9536 = relay.Function([], output)
mutated_mod['func_9536'] = func_9536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5975_call = mod.get_global_var('func_5975')
func_5977_call = mutated_mod.get_global_var('func_5977')
call_9619 = relay.TupleGetItem(func_5975_call(), 1)
call_9620 = relay.TupleGetItem(func_5977_call(), 1)
output = relay.Tuple([call_9619,])
output2 = relay.Tuple([call_9620,])
func_9631 = relay.Function([], output)
mod['func_9631'] = func_9631
mod = relay.transform.InferType()(mod)
output = func_9631()
func_9632 = relay.Function([], output)
mutated_mod['func_9632'] = func_9632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3931_call = mod.get_global_var('func_3931')
func_3932_call = mutated_mod.get_global_var('func_3932')
call_9647 = relay.TupleGetItem(func_3931_call(), 0)
call_9648 = relay.TupleGetItem(func_3932_call(), 0)
output = call_9647
output2 = call_9648
func_9675 = relay.Function([], output)
mod['func_9675'] = func_9675
mod = relay.transform.InferType()(mod)
mutated_mod['func_9675'] = func_9675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9675_call = mutated_mod.get_global_var('func_9675')
call_9676 = func_9675_call()
output = call_9676
func_9677 = relay.Function([], output)
mutated_mod['func_9677'] = func_9677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4301_call = mod.get_global_var('func_4301')
func_4303_call = mutated_mod.get_global_var('func_4303')
call_9757 = func_4301_call()
call_9758 = func_4301_call()
func_6429_call = mod.get_global_var('func_6429')
func_6431_call = mutated_mod.get_global_var('func_6431')
call_9767 = relay.TupleGetItem(func_6429_call(), 1)
call_9768 = relay.TupleGetItem(func_6431_call(), 1)
output = relay.Tuple([call_9757,call_9767,])
output2 = relay.Tuple([call_9758,call_9768,])
func_9771 = relay.Function([], output)
mod['func_9771'] = func_9771
mod = relay.transform.InferType()(mod)
output = func_9771()
func_9772 = relay.Function([], output)
mutated_mod['func_9772'] = func_9772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1309_call = mod.get_global_var('func_1309')
func_1311_call = mutated_mod.get_global_var('func_1311')
call_9781 = relay.TupleGetItem(func_1309_call(), 0)
call_9782 = relay.TupleGetItem(func_1311_call(), 0)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_9807 = relay.TupleGetItem(func_1120_call(), 0)
call_9808 = relay.TupleGetItem(func_1121_call(), 0)
func_7567_call = mod.get_global_var('func_7567')
func_7569_call = mutated_mod.get_global_var('func_7569')
call_9812 = relay.TupleGetItem(func_7567_call(), 0)
call_9813 = relay.TupleGetItem(func_7569_call(), 0)
func_8349_call = mod.get_global_var('func_8349')
func_8351_call = mutated_mod.get_global_var('func_8351')
call_9816 = func_8349_call()
call_9817 = func_8349_call()
output = relay.Tuple([call_9781,call_9807,call_9812,call_9816,])
output2 = relay.Tuple([call_9782,call_9808,call_9813,call_9817,])
func_9822 = relay.Function([], output)
mod['func_9822'] = func_9822
mod = relay.transform.InferType()(mod)
output = func_9822()
func_9823 = relay.Function([], output)
mutated_mod['func_9823'] = func_9823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3677_call = mod.get_global_var('func_3677')
func_3679_call = mutated_mod.get_global_var('func_3679')
call_9867 = func_3677_call()
call_9868 = func_3677_call()
func_9023_call = mod.get_global_var('func_9023')
func_9027_call = mutated_mod.get_global_var('func_9027')
var_9879 = relay.var("var_9879", dtype = "bool", shape = (240,))#candidate|9879|(240,)|var|bool
call_9878 = relay.TupleGetItem(func_9023_call(relay.reshape(var_9879.astype('bool'), [16, 5, 3]), relay.reshape(var_9879.astype('bool'), [16, 5, 3]), ), 0)
call_9880 = relay.TupleGetItem(func_9027_call(relay.reshape(var_9879.astype('bool'), [16, 5, 3]), relay.reshape(var_9879.astype('bool'), [16, 5, 3]), ), 0)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_9881 = relay.TupleGetItem(func_2815_call(), 1)
call_9882 = relay.TupleGetItem(func_2816_call(), 1)
func_8356_call = mod.get_global_var('func_8356')
func_8358_call = mutated_mod.get_global_var('func_8358')
call_9894 = func_8356_call()
call_9895 = func_8356_call()
output = relay.Tuple([call_9867,call_9878,var_9879,call_9881,call_9894,])
output2 = relay.Tuple([call_9868,call_9880,var_9879,call_9882,call_9895,])
func_9920 = relay.Function([var_9879,], output)
mod['func_9920'] = func_9920
mod = relay.transform.InferType()(mod)
mutated_mod['func_9920'] = func_9920
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9921 = relay.var("var_9921", dtype = "bool", shape = (240,))#candidate|9921|(240,)|var|bool
func_9920_call = mutated_mod.get_global_var('func_9920')
call_9922 = func_9920_call(var_9921)
output = call_9922
func_9923 = relay.Function([var_9921], output)
mutated_mod['func_9923'] = func_9923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2923_call = mod.get_global_var('func_2923')
func_2924_call = mutated_mod.get_global_var('func_2924')
call_9925 = relay.TupleGetItem(func_2923_call(), 1)
call_9926 = relay.TupleGetItem(func_2924_call(), 1)
func_9395_call = mod.get_global_var('func_9395')
func_9396_call = mutated_mod.get_global_var('func_9396')
call_9936 = relay.TupleGetItem(func_9395_call(), 0)
call_9937 = relay.TupleGetItem(func_9396_call(), 0)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_9948 = relay.TupleGetItem(func_1864_call(), 4)
call_9949 = relay.TupleGetItem(func_1865_call(), 4)
func_3064_call = mod.get_global_var('func_3064')
func_3067_call = mutated_mod.get_global_var('func_3067')
const_9960 = relay.const([9,-6,-8,1,-1,-10,-8,3,-2,-9,4,4,-8,4,-8,-3,-1,-8,-10,-8,-2,4,-9,-7,2,5,-5,-3,5,6,-10,-2,2,10,9,-2,10,2,-5,-2,5,4,8,5,-7,-9,-4,10,9,5,-9,10,5,9,-2,-8,8,-9,1,2,-4,7,-9,1,4,-7,-7,2,-2,-3,-2,1,2,6,3,3,8,7,-6,7,-6,-5,-5,6,-8,2,-7,9,3,7,5,3,-2,3,1,-10,-6,2,1,-1,-5,10,3,5,9,2,-4,9,7,3,-4,7,-7,-3,4,-9,6,5,9,5,-4,1,-6,-3,2,1,1,6,-6,6,5,-1,3,10,7,-1,6,8,-2,-5,9,2,3,-7,9,10,-9,4,-8,7,2,6,-9,8,-5,8,10,-5,-10,-1,-10,-2,2,2,-2,5,6,-4], dtype = "int32")#candidate|9960|(168,)|const|int32
var_9961 = relay.var("var_9961", dtype = "int8", shape = (28,))#candidate|9961|(28,)|var|int8
call_9959 = relay.TupleGetItem(func_3064_call(relay.reshape(const_9960.astype('int32'), [6, 14, 2]), relay.reshape(var_9961.astype('int8'), [28,]), ), 2)
call_9962 = relay.TupleGetItem(func_3067_call(relay.reshape(const_9960.astype('int32'), [6, 14, 2]), relay.reshape(var_9961.astype('int8'), [28,]), ), 2)
var_9963 = relay.var("var_9963", dtype = "int8", shape = (28,))#candidate|9963|(28,)|var|int8
bop_9964 = relay.less_equal(var_9961.astype('bool'), relay.reshape(var_9963.astype('bool'), relay.shape_of(var_9961))) # shape=(28,)
func_5195_call = mod.get_global_var('func_5195')
func_5199_call = mutated_mod.get_global_var('func_5199')
var_9985 = relay.var("var_9985", dtype = "float64", shape = (24,))#candidate|9985|(24,)|var|float64
var_9986 = relay.var("var_9986", dtype = "int32", shape = (840,))#candidate|9986|(840,)|var|int32
call_9984 = relay.TupleGetItem(func_5195_call(relay.reshape(var_9985.astype('float64'), [24,]), relay.reshape(var_9986.astype('int32'), [840,]), ), 2)
call_9987 = relay.TupleGetItem(func_5199_call(relay.reshape(var_9985.astype('float64'), [24,]), relay.reshape(var_9986.astype('int32'), [840,]), ), 2)
func_1263_call = mod.get_global_var('func_1263')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_9988 = func_1263_call()
call_9989 = func_1263_call()
func_2486_call = mod.get_global_var('func_2486')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_9994 = relay.TupleGetItem(func_2486_call(), 2)
call_9995 = relay.TupleGetItem(func_2487_call(), 2)
output = relay.Tuple([call_9925,call_9936,call_9948,call_9959,const_9960,bop_9964,call_9984,var_9985,var_9986,call_9988,call_9994,])
output2 = relay.Tuple([call_9926,call_9937,call_9949,call_9962,const_9960,bop_9964,call_9987,var_9985,var_9986,call_9989,call_9995,])
func_9998 = relay.Function([var_9961,var_9963,var_9985,var_9986,], output)
mod['func_9998'] = func_9998
mod = relay.transform.InferType()(mod)
mutated_mod['func_9998'] = func_9998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9998_call = mutated_mod.get_global_var('func_9998')
var_10000 = relay.var("var_10000", dtype = "int8", shape = (28,))#candidate|10000|(28,)|var|int8
var_10001 = relay.var("var_10001", dtype = "int8", shape = (28,))#candidate|10001|(28,)|var|int8
var_10002 = relay.var("var_10002", dtype = "float64", shape = (24,))#candidate|10002|(24,)|var|float64
var_10003 = relay.var("var_10003", dtype = "int32", shape = (840,))#candidate|10003|(840,)|var|int32
call_9999 = func_9998_call(var_10000,var_10001,var_10002,var_10003,)
output = call_9999
func_10004 = relay.Function([var_10000,var_10001,var_10002,var_10003,], output)
mutated_mod['func_10004'] = func_10004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5661_call = mod.get_global_var('func_5661')
func_5662_call = mutated_mod.get_global_var('func_5662')
call_10013 = relay.TupleGetItem(func_5661_call(), 3)
call_10014 = relay.TupleGetItem(func_5662_call(), 3)
output = relay.Tuple([call_10013,])
output2 = relay.Tuple([call_10014,])
func_10015 = relay.Function([], output)
mod['func_10015'] = func_10015
mod = relay.transform.InferType()(mod)
mutated_mod['func_10015'] = func_10015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10015_call = mutated_mod.get_global_var('func_10015')
call_10016 = func_10015_call()
output = call_10016
func_10017 = relay.Function([], output)
mutated_mod['func_10017'] = func_10017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_10024 = relay.TupleGetItem(func_1864_call(), 4)
call_10025 = relay.TupleGetItem(func_1865_call(), 4)
output = relay.Tuple([call_10024,])
output2 = relay.Tuple([call_10025,])
func_10035 = relay.Function([], output)
mod['func_10035'] = func_10035
mod = relay.transform.InferType()(mod)
output = func_10035()
func_10036 = relay.Function([], output)
mutated_mod['func_10036'] = func_10036
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10083 = relay.const([[[-4.994179,-1.896047,-7.797619,-3.233513,0.034142,6.780295,2.526685,5.088109,6.568421],[-4.882996,1.165689,-0.520040,-8.536087,3.249753,-1.941741,-2.781654,3.133819,-6.282413],[-0.769258,-8.780162,-1.441113,6.157265,-7.743032,-8.232155,1.324453,-6.210803,4.646253],[-8.366735,-1.491010,4.674249,-3.259394,8.331284,2.738868,1.235861,6.600732,2.424299],[9.380547,7.870716,7.172589,8.920407,-0.176128,-5.850895,0.824536,9.055221,-1.917386],[-0.033232,6.031071,-3.947656,9.770994,-0.010752,9.445301,4.386549,-4.736930,3.481464],[-9.374350,-1.850096,-4.284647,-3.442274,0.394543,8.950169,1.894646,-7.956365,5.153566],[4.427049,-1.429887,9.407832,7.397106,7.808763,-6.464563,-4.308989,7.046743,8.929481],[5.672184,4.331508,-7.588152,-5.267667,-0.380241,-3.375692,5.771948,8.387534,4.875238],[1.994625,5.612191,-6.014686,5.943862,-0.290515,-1.606949,-5.083628,0.370668,-9.133705],[-2.765121,4.445832,-5.992361,5.341243,5.840886,1.072848,3.765525,-5.264707,6.435982]],[[-9.257640,0.947090,-7.440731,9.254709,9.878640,-3.399065,-7.604535,-9.389651,-2.199529],[7.467838,-5.370304,-8.546802,0.780881,-7.287302,-2.663069,-1.647311,2.775931,9.461287],[8.788957,-2.742335,6.528857,8.014431,-2.472235,-3.373240,-0.247219,-7.217490,-7.447587],[-6.671682,-6.267576,2.924971,2.241262,-0.119966,2.747922,-0.886913,-0.757177,1.974838],[5.101892,4.432231,-1.718831,-7.163751,0.768115,1.794969,5.336460,9.701259,6.810407],[-6.238427,-1.145559,1.648180,-6.881095,8.087693,-9.057554,4.539965,6.843846,1.278686],[-9.801279,-8.633445,-4.002652,0.838419,2.872487,-4.102054,-5.549962,7.868558,8.392024],[-4.858878,-7.415670,-4.204323,0.222906,2.609094,-2.431713,-9.325854,-7.566674,-9.222455],[4.306140,1.036304,-8.609387,3.119200,-8.367943,0.133337,7.307875,-7.752820,9.927162],[-1.824942,-6.666538,5.913765,6.263184,3.297921,-7.985242,-9.158278,8.431193,1.282821],[4.458661,-1.814043,6.828053,3.886534,-2.290109,0.617451,-7.526673,-7.724240,6.949181]],[[2.806785,4.977709,-0.175660,-1.765106,9.851865,-3.820605,1.917404,7.907201,-7.036232],[-7.362354,9.092389,6.121395,-5.481018,9.232210,-7.562261,2.652415,9.353454,-7.290796],[-7.985709,-4.757124,-6.420719,-0.895613,6.140677,-4.612888,8.771858,9.863850,1.840804],[3.931978,5.374443,-9.857951,2.285438,6.975366,-4.926666,-9.836071,9.967080,5.887646],[-8.192387,7.183253,3.198169,9.374376,-2.438996,-6.907491,4.412444,-2.022652,-7.503921],[-5.660065,-6.819700,-5.449128,6.682000,1.378869,5.130094,-6.322950,5.318254,4.935409],[3.242246,9.935963,-6.209881,8.009313,1.207839,-4.501521,-5.809268,8.926983,-9.250910],[-1.111691,-7.348851,-8.632093,-8.089869,3.681672,3.193118,-5.603441,3.328395,-3.749032],[2.966432,5.424087,6.039967,-1.363911,-5.894301,-8.043490,8.224265,-3.815091,6.719723],[-7.280459,-0.117055,2.415625,-0.895218,-9.521368,3.861828,0.958015,9.068308,2.307055],[-8.159898,-8.111839,5.257637,-2.104790,4.073590,-0.291812,3.542602,-7.405779,3.259402]],[[6.213215,-8.827231,7.469169,8.168863,-4.202716,-8.671874,1.169496,-4.756670,6.135926],[7.378717,-3.930418,4.608613,1.683646,0.788595,-1.011164,9.992329,4.248852,5.397770],[0.881003,0.038011,0.516308,5.127281,9.737559,4.464660,4.204700,-4.525385,5.334557],[-5.225625,-4.129441,2.918399,-8.676998,8.514177,-3.941446,2.047634,6.690107,9.598719],[-3.961412,6.557247,-0.604685,-1.190757,3.432574,-4.557494,-4.642417,8.135862,-4.963465],[1.473256,8.950904,-7.907068,-7.423681,1.745574,9.898687,-3.450006,9.269876,2.323752],[-8.710457,9.575284,-4.087738,7.625824,6.023449,2.639658,6.531368,-6.122282,0.860629],[-9.752614,-6.740712,5.528438,-1.012980,7.817624,-6.208387,-3.600362,4.875478,-2.123586],[2.762180,-0.031482,9.604410,-0.105130,0.462715,9.235426,-9.244188,-2.438990,-6.368267],[-7.737927,1.532943,-0.057610,-7.440695,6.039145,7.737669,2.469013,8.223507,2.846427],[2.625547,7.483031,-0.626732,-4.712212,-0.588743,-1.142280,-9.675086,9.335148,-2.045007]],[[3.776980,-9.566935,-3.871071,2.659362,-9.049137,-1.014566,7.232121,-3.162284,-8.657053],[8.787204,1.504509,5.191501,-1.442695,-9.155616,4.042185,-0.404430,7.188420,4.418918],[-6.479307,8.781052,8.367149,-7.347927,2.147295,9.634207,0.289005,-2.767842,-6.257521],[-6.634853,-2.159975,0.702981,-7.093639,-1.297988,-3.629377,5.288025,-9.814517,-2.173387],[-1.699964,-1.339910,6.292896,6.034604,0.367521,1.973639,1.933402,-6.330737,-6.405711],[-4.958077,4.003428,-8.821555,-0.062902,-0.584353,-5.174724,0.100239,6.828709,-6.998802],[3.976278,-4.394687,-4.799727,7.761561,9.897501,6.846729,8.847074,-4.372968,-8.068909],[-1.310789,7.868019,-2.276575,0.293127,-4.840437,6.808830,7.175996,4.998709,0.386750],[6.161587,7.397738,6.581720,-8.251398,-0.261886,8.542855,0.709712,-8.021385,8.008410],[-5.423828,-1.746316,4.793288,-1.919657,-6.787898,-3.583831,2.550482,-2.109716,0.247477],[2.928793,-7.735361,-0.763474,-0.744721,-8.679006,-7.018164,3.627781,-0.462982,-5.523019]],[[-7.321856,8.151889,-6.757159,-6.263917,5.371571,-5.334372,-7.150536,1.390493,-8.493542],[4.351163,1.048813,5.833087,7.387571,5.721643,-2.598791,6.872501,-2.974032,2.315435],[3.392561,-9.694878,6.903161,1.055184,-1.150049,-3.539819,-0.326103,3.146279,9.138371],[-3.236512,-4.194841,5.980645,7.296868,1.571318,4.584392,-8.940200,-8.287215,6.513649],[6.639673,-1.499419,8.020275,-3.145910,-4.599440,-4.754051,-0.535852,-4.156743,-0.710622],[4.336071,-3.685714,1.370897,-1.149477,-7.182038,-5.647467,-5.459182,-0.539004,8.831283],[0.601416,-2.005468,3.016852,-4.092710,2.576077,-8.089607,-9.361153,6.188360,-8.971900],[-4.934218,-6.860782,-3.924573,-7.214919,-1.662247,6.133285,7.985373,-9.749257,-8.138273],[-6.104584,1.622632,5.870714,2.856504,-2.140006,-2.175359,5.041998,4.919625,-9.986445],[-2.348271,-2.949135,7.415072,-6.400401,-6.161436,-5.005093,-7.099122,7.235539,-7.770881],[-8.027630,-2.247273,-4.108652,6.221178,9.587095,8.817982,-5.914563,5.359842,8.479367]]], dtype = "float32")#candidate|10083|(6, 11, 9)|const|float32
uop_10084 = relay.atan(const_10083.astype('float32')) # shape=(6, 11, 9)
bop_10089 = relay.equal(uop_10084.astype('bool'), relay.reshape(const_10083.astype('bool'), relay.shape_of(uop_10084))) # shape=(6, 11, 9)
output = relay.Tuple([bop_10089,])
output2 = relay.Tuple([bop_10089,])
func_10093 = relay.Function([], output)
mod['func_10093'] = func_10093
mod = relay.transform.InferType()(mod)
output = func_10093()
func_10094 = relay.Function([], output)
mutated_mod['func_10094'] = func_10094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3931_call = mod.get_global_var('func_3931')
func_3932_call = mutated_mod.get_global_var('func_3932')
call_10132 = relay.TupleGetItem(func_3931_call(), 0)
call_10133 = relay.TupleGetItem(func_3932_call(), 0)
func_6517_call = mod.get_global_var('func_6517')
func_6518_call = mutated_mod.get_global_var('func_6518')
call_10160 = relay.TupleGetItem(func_6517_call(), 1)
call_10161 = relay.TupleGetItem(func_6518_call(), 1)
output = relay.Tuple([call_10132,call_10160,])
output2 = relay.Tuple([call_10133,call_10161,])
func_10168 = relay.Function([], output)
mod['func_10168'] = func_10168
mod = relay.transform.InferType()(mod)
mutated_mod['func_10168'] = func_10168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10168_call = mutated_mod.get_global_var('func_10168')
call_10169 = func_10168_call()
output = call_10169
func_10170 = relay.Function([], output)
mutated_mod['func_10170'] = func_10170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1934_call = mod.get_global_var('func_1934')
func_1936_call = mutated_mod.get_global_var('func_1936')
call_10179 = relay.TupleGetItem(func_1934_call(), 0)
call_10180 = relay.TupleGetItem(func_1936_call(), 0)
func_19_call = mod.get_global_var('func_19')
func_22_call = mutated_mod.get_global_var('func_22')
const_10204 = relay.const([[9,8,-3,-4,9,-1,9,-8,-8,9,6,-8,9,10,-9,4,6,2,8,-6,-5,2,10,-1,10,2,-10,-7]], dtype = "int8")#candidate|10204|(1, 28)|const|int8
var_10205 = relay.var("var_10205", dtype = "int8", shape = (448,))#candidate|10205|(448,)|var|int8
call_10203 = relay.TupleGetItem(func_19_call(relay.reshape(const_10204.astype('int8'), [7, 4, 1]), relay.reshape(var_10205.astype('int8'), [7, 4, 16]), ), 0)
call_10206 = relay.TupleGetItem(func_22_call(relay.reshape(const_10204.astype('int8'), [7, 4, 1]), relay.reshape(var_10205.astype('int8'), [7, 4, 16]), ), 0)
func_3064_call = mod.get_global_var('func_3064')
func_3067_call = mutated_mod.get_global_var('func_3067')
const_10211 = relay.const([9,-7,4,7,2,3,-5,-9,1,8,4,-4,-8,-1,-2,10,-4,10,2,5,-1,5,5,4,7,-5,10,3,-2,-8,7,-6,8,8,-3,4,-1,10,3,2,-6,3,8,-5,-2,-7,-5,-7,-10,3,-8,-9,-5,7,-3,-10,-7,8,-10,-8,-7,9,-1,-7,3,-6,6,-2,-4,-1,-1,7,-5,-5,-7,-5,-1,8,-3,5,-4,9,-8,-3,1,1,-6,-9,-5,-5,-7,-9,-9,10,-4,9,8,8,-8,-8,4,10,10,-10,-6,-7,9,3,7,-9,-8,8,6,-2,4,5,1,-7,-7,-6,-4,-7,-3,1,4,8,10,-10,2,1,3,-4,-3,5,-10,4,6,-6,-2,6,9,-9,-1,-3,2,9,-2,-10,-3,-9,-8,6,-6,4,9,5,-5,5,3,9,6,1,-10,-4,-7,-6,6,2], dtype = "int32")#candidate|10211|(168,)|const|int32
call_10210 = relay.TupleGetItem(func_3064_call(relay.reshape(const_10211.astype('int32'), [6, 14, 2]), relay.reshape(const_10204.astype('int8'), [28,]), ), 0)
call_10212 = relay.TupleGetItem(func_3067_call(relay.reshape(const_10211.astype('int32'), [6, 14, 2]), relay.reshape(const_10204.astype('int8'), [28,]), ), 0)
const_10215 = relay.const([[-3,7,7,3,1,2,-9,5,6,10,4,-6,-9,-9,-1,7,4,-3,7,10,10,-5,-5,-8,6,2,1,10],[-9,5,2,5,3,8,7,-9,10,-7,4,3,-1,-2,6,-4,-3,-4,-8,-10,10,2,-7,-4,7,-9,9,3],[-10,-4,-8,-1,5,5,-6,-6,-6,4,1,10,1,1,3,10,6,10,-2,7,8,-3,-9,-3,-7,-8,-4,8],[-8,-7,-10,4,1,-2,-5,-10,-10,-7,2,-6,6,-7,2,10,-2,-1,-4,-8,9,7,8,-8,2,7,-7,3],[7,-8,5,1,4,10,6,-10,10,2,-7,-8,8,-3,8,-10,5,-8,-5,8,10,5,9,-3,-5,9,-5,-10],[-2,-8,8,9,-4,-4,5,-8,1,1,9,1,8,7,-6,-6,2,3,10,5,-9,4,-2,-7,6,-7,1,-10],[-9,-2,-5,-5,2,9,10,-7,5,-10,-2,4,-6,-4,8,-6,10,-1,-10,-2,-4,4,6,-2,-1,-10,1,4],[2,4,1,-6,-10,7,-3,2,-1,3,8,-8,10,-3,-1,-6,-4,-4,10,7,7,2,5,9,-10,3,10,6],[-9,-8,-7,-5,7,-5,9,1,-6,-6,-8,-6,9,-8,-1,8,-7,-2,5,5,-7,10,-2,2,5,10,-2,4],[6,-2,-10,8,-9,2,-8,-5,-7,10,8,-1,9,8,10,7,-8,2,9,5,-10,3,4,-2,-7,-4,6,9]], dtype = "int8")#candidate|10215|(10, 28)|const|int8
bop_10216 = relay.bitwise_and(const_10204.astype('int64'), const_10215.astype('int64')) # shape=(10, 28)
output = relay.Tuple([call_10179,call_10203,var_10205,call_10210,const_10211,bop_10216,])
output2 = relay.Tuple([call_10180,call_10206,var_10205,call_10212,const_10211,bop_10216,])
func_10258 = relay.Function([var_10205,], output)
mod['func_10258'] = func_10258
mod = relay.transform.InferType()(mod)
mutated_mod['func_10258'] = func_10258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10259 = relay.var("var_10259", dtype = "int8", shape = (448,))#candidate|10259|(448,)|var|int8
func_10258_call = mutated_mod.get_global_var('func_10258')
call_10260 = func_10258_call(var_10259)
output = call_10260
func_10261 = relay.Function([var_10259], output)
mutated_mod['func_10261'] = func_10261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_10275 = relay.TupleGetItem(func_1120_call(), 0)
call_10276 = relay.TupleGetItem(func_1121_call(), 0)
func_1068_call = mod.get_global_var('func_1068')
func_1072_call = mutated_mod.get_global_var('func_1072')
var_10278 = relay.var("var_10278", dtype = "int32", shape = (60, 14))#candidate|10278|(60, 14)|var|int32
const_10279 = relay.const([-5,-9,9,-7,3,7,-5,7,6,5,-9,3,-1,-2,3,3,10,-1,6,-4,-5,9,9,7,2,-9,-5,5], dtype = "int8")#candidate|10279|(28,)|const|int8
const_10280 = relay.const([2,-4,2,-7,-3,-2,-3,7,8,-8,1,-9,2,-5,1,-6,7,-7,6,-3,-8,5,3,-3,-9,-8,-10,-3,10,-1,-1,5,9,-9,8,5,9,7,-5,5,-9,4,-7,-2,-4,-1,10,-5,7,-7,7,1,3,8,-6,1,3,5,-4,-10,-1,-3,6,-1,1,-8,-9,4,4,-1,-4,-8,-10,10,1,4,2,3,5,-3,-2,-7,-9,-5,5,-5,-8,10,7,4,2,2,-5,-4,-10,9,5,5,6,-8,3,2,10,1,-3,-7,-5,1,-5,10,-9,9,4,-9,-1,-3,-4,-10,-8,2,-8,-6,-10,-2,-1,2,1,5,3,-8,-3,-1,-8,1,-1,-9,2,3,2,6,-10,-3,-10,-8,2,-9,9,-4,-2,4,6,6,7,-7,-5,-4,3,-5,6,8,-9,3,-1,-4,-1,-8,-10,-2,-2,-9,6,-1,9,-4,1,-2,-10,-10,-3,-4,3,-1,4,3,6,4,-5,1,-5,8,-8,8,-7,-7,-5,7,2,-2,-3,2,-8,1,3,7,10,4,8,-4,-2,-9,3,-6,4,-1,4,-8,2,-4,-5,3,-6,1,-10,-1,9,9,6,9,3,8,-5,-10,6,-2,-4,-6,3,-6,-6,5,-7,-9,2,-2,10,-4,4,10,9,3,-10,-6,10,-5,-1,2,-9,-8,1,-7,9,3,-7,-7,8,2,1,-10,1,5,-8,-9,-10,-9,8,3,7,-1,1,-9,-8,-7,-10,-9,-2,3,5,-10,-1,-7,3,6,-6,-4,-5,-7,5,-5,3,-6,-10,7,-10,-10,6,-10,9,-10,-3,5,-9,-2,-8,-9,-10,-6,-3,6,1,-4,7,-7,10,-3,-4,-10,1,-7,-10,10,3,-2,10,-2,6,-10,-2,1,-4,2,5,1,5,-4,6,4,-9,-8,6,2,7,-7,8,-8,4,-2,-3,4,-1,-4,-4,6,7,-4,3,-5,7,9,1,8,1,-6,-3,4,-3,-10,-9,10,-2,8,-10,8,-6,3,-6,7,-10,-2,7,6,-6,-7,-5,-2,-3,4,5,1,9,-3,6,2,4,1,-2,9,5,3,-5,7,-5,-1,5,4,-7,-10,-6,9,8,1,-8,10,-6,-3,9,-9,3,7,-2,-1,-7,-2,-5,4,2,5,-4,3,-9,-5,8,-3,3,-8,-10,-4,2,-1], dtype = "int8")#candidate|10280|(448,)|const|int8
call_10277 = relay.TupleGetItem(func_1068_call(relay.reshape(var_10278.astype('int32'), [14, 12, 5]), relay.reshape(const_10279.astype('int8'), [7, 4]), relay.reshape(const_10280.astype('int8'), [56, 8]), ), 4)
call_10281 = relay.TupleGetItem(func_1072_call(relay.reshape(var_10278.astype('int32'), [14, 12, 5]), relay.reshape(const_10279.astype('int8'), [7, 4]), relay.reshape(const_10280.astype('int8'), [56, 8]), ), 4)
uop_10338 = relay.rsqrt(const_10279.astype('float32')) # shape=(28,)
output = relay.Tuple([call_10275,call_10277,var_10278,const_10280,uop_10338,])
output2 = relay.Tuple([call_10276,call_10281,var_10278,const_10280,uop_10338,])
func_10340 = relay.Function([var_10278,], output)
mod['func_10340'] = func_10340
mod = relay.transform.InferType()(mod)
var_10341 = relay.var("var_10341", dtype = "int32", shape = (60, 14))#candidate|10341|(60, 14)|var|int32
output = func_10340(var_10341)
func_10342 = relay.Function([var_10341], output)
mutated_mod['func_10342'] = func_10342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9293_call = mod.get_global_var('func_9293')
func_9295_call = mutated_mod.get_global_var('func_9295')
call_10511 = func_9293_call()
call_10512 = func_9293_call()
func_9370_call = mod.get_global_var('func_9370')
func_9371_call = mutated_mod.get_global_var('func_9371')
call_10530 = relay.TupleGetItem(func_9370_call(), 2)
call_10531 = relay.TupleGetItem(func_9371_call(), 2)
output = relay.Tuple([call_10511,call_10530,])
output2 = relay.Tuple([call_10512,call_10531,])
func_10535 = relay.Function([], output)
mod['func_10535'] = func_10535
mod = relay.transform.InferType()(mod)
output = func_10535()
func_10536 = relay.Function([], output)
mutated_mod['func_10536'] = func_10536
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10546 = relay.var("var_10546", dtype = "float32", shape = (8, 16, 1))#candidate|10546|(8, 16, 1)|var|float32
uop_10547 = relay.log(var_10546.astype('float32')) # shape=(8, 16, 1)
bop_10553 = relay.logical_xor(uop_10547.astype('int64'), relay.reshape(var_10546.astype('int64'), relay.shape_of(uop_10547))) # shape=(8, 16, 1)
uop_10569 = relay.sqrt(uop_10547.astype('float32')) # shape=(8, 16, 1)
bop_10584 = relay.not_equal(uop_10547.astype('bool'), relay.reshape(uop_10569.astype('bool'), relay.shape_of(uop_10547))) # shape=(8, 16, 1)
func_5268_call = mod.get_global_var('func_5268')
func_5270_call = mutated_mod.get_global_var('func_5270')
call_10592 = relay.TupleGetItem(func_5268_call(), 0)
call_10593 = relay.TupleGetItem(func_5270_call(), 0)
uop_10602 = relay.cosh(uop_10547.astype('float64')) # shape=(8, 16, 1)
bop_10613 = relay.divide(uop_10547.astype('float64'), relay.reshape(var_10546.astype('float64'), relay.shape_of(uop_10547))) # shape=(8, 16, 1)
uop_10616 = relay.log10(uop_10547.astype('float64')) # shape=(8, 16, 1)
uop_10623 = relay.log2(uop_10616.astype('float64')) # shape=(8, 16, 1)
bop_10634 = relay.less(uop_10602.astype('bool'), relay.reshape(bop_10584.astype('bool'), relay.shape_of(uop_10602))) # shape=(8, 16, 1)
bop_10643 = relay.minimum(uop_10623.astype('int16'), relay.reshape(bop_10584.astype('int16'), relay.shape_of(uop_10623))) # shape=(8, 16, 1)
output = relay.Tuple([bop_10553,call_10592,bop_10613,bop_10634,bop_10643,])
output2 = relay.Tuple([bop_10553,call_10593,bop_10613,bop_10634,bop_10643,])
func_10666 = relay.Function([var_10546,], output)
mod['func_10666'] = func_10666
mod = relay.transform.InferType()(mod)
var_10667 = relay.var("var_10667", dtype = "float32", shape = (8, 16, 1))#candidate|10667|(8, 16, 1)|var|float32
output = func_10666(var_10667)
func_10668 = relay.Function([var_10667], output)
mutated_mod['func_10668'] = func_10668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9370_call = mod.get_global_var('func_9370')
func_9371_call = mutated_mod.get_global_var('func_9371')
call_10692 = relay.TupleGetItem(func_9370_call(), 2)
call_10693 = relay.TupleGetItem(func_9371_call(), 2)
uop_10694 = relay.asinh(call_10692.astype('float32')) # shape=(7, 1, 6)
uop_10696 = relay.asinh(call_10693.astype('float32')) # shape=(7, 1, 6)
output = uop_10694
output2 = uop_10696
func_10702 = relay.Function([], output)
mod['func_10702'] = func_10702
mod = relay.transform.InferType()(mod)
output = func_10702()
func_10703 = relay.Function([], output)
mutated_mod['func_10703'] = func_10703
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10716 = relay.var("var_10716", dtype = "uint8", shape = (5, 1, 16))#candidate|10716|(5, 1, 16)|var|uint8
var_10717 = relay.var("var_10717", dtype = "uint8", shape = (5, 14, 16))#candidate|10717|(5, 14, 16)|var|uint8
bop_10718 = relay.right_shift(var_10716.astype('uint8'), var_10717.astype('uint8')) # shape=(5, 14, 16)
output = bop_10718
output2 = bop_10718
func_10728 = relay.Function([var_10716,var_10717,], output)
mod['func_10728'] = func_10728
mod = relay.transform.InferType()(mod)
var_10729 = relay.var("var_10729", dtype = "uint8", shape = (5, 1, 16))#candidate|10729|(5, 1, 16)|var|uint8
var_10730 = relay.var("var_10730", dtype = "uint8", shape = (5, 14, 16))#candidate|10730|(5, 14, 16)|var|uint8
output = func_10728(var_10729,var_10730,)
func_10731 = relay.Function([var_10729,var_10730,], output)
mutated_mod['func_10731'] = func_10731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7633_call = mod.get_global_var('func_7633')
func_7634_call = mutated_mod.get_global_var('func_7634')
call_10790 = func_7633_call()
call_10791 = func_7633_call()
func_1245_call = mod.get_global_var('func_1245')
func_1248_call = mutated_mod.get_global_var('func_1248')
const_10799 = relay.const([2,4,2,7,-6,1,-1,-7,-4,-9,7,7,-5,6,-3,-1,-10,-8,3,-2,-10,-4,-5,-6,-9,7,1,7], dtype = "int8")#candidate|10799|(28,)|const|int8
const_10800 = relay.const([7,4,-2,-3,9,-8,6,5,9,-2,-9,7,9,10,-4,-1,8,9,10,-2,9,-9,10,-6,1,1,10,-6,6,7,8,10,-3,-5,10,-1,7,-5,-3,-3,10,-6,4,7,9,-1,-2,-10,2,10,-3,1,5,7,9,-4,-6,9,-4,1,2,10,-4,1,-6,-8,-5,8,-6,-8,7,-4,-4,-4,-1,4,8,7,4,10,2,10,-8,7,-3,1,-9,-4,9,-3,-2,2,-1,-6,9,-5,-3,-6,3,-6,-10,-8,-1,-4,-10,-9,-4,-4,9,9,7,9,-7,2,-10,-6,-5,-1,-7,-7,2,1,6,-2,-7,-5,5,4,-10,-3,7,5,6,-6,-1,-9,-8,10,8,-1,6,-9,1,-4,2,-3,9,-8,-4,-7,9,7,-8,3,2,1,9,9,-5,-3,10,-5,4,3,2,-2,-8,10,7,-2,-7,-6,-4,6,-6,4,7,-5,5,-10,8,7,2,-1,-9,7,-7,2,-6,1,-9,9,6,-6,2,5,-7,-5,10,-7,9,4,-7,-9,7,6,-5,-2,1,-2,-6,-6,-1,-2,-6,-9,3,3,4,-4,2,-8,6,-7,-10,1,-8,-8,7,8,-1,10,-4,5,-7,-8,-8,7,8,1,5,-5,1,1,-5,3,10,9,10,-10,2,7,8,-4,-10,-8,10,-9,9,1,1,-10,-9,2,5,-8,4,7,-9,-10,-7,-7,2,-10,-6,-4,6,9,-5,7,-5,-6,-8,2,-5,10,1,-9,-3,-1,-1,-7,9,4,-7,1,-6,2,2,-3,8,-9,1,9,8,-3,5,5,6,-5,10,6,4,10,-5,3,8,-10,1,-3,9,9,5,-7,5,5,-9,1,-2,9,6,9,-7,3,8,8,-1,3,-5,9,10,5,-7,-3,1,-6,-8,-3,4,3,-1,1,-2,-7,3,-6,2,-4,-10,-7,3,-8,-8,5,6,-6,-1,-8,-1,9,-5,-9,-6,5,4,-7,-7,5,7,-9,-10,-9,-2,-5,3,9,10,-6,-2,4,-5,2,-7,9,-9,-4,-3,-1,1,-8,-1,-4,-4,7,1,4,2,10,-3,3,9,-10,-10,5,-8,-8,1,-1,-10,3,-2,9,-2,-5,-10,-6,6,9,-8,9,-1,-6,9,-5,10,2,4,-7,-10,1,1,-9,3,4,4,9,2,-6], dtype = "int8")#candidate|10800|(448,)|const|int8
call_10798 = relay.TupleGetItem(func_1245_call(relay.reshape(const_10799.astype('int8'), [28, 1]), relay.reshape(const_10800.astype('int8'), [448,]), ), 0)
call_10801 = relay.TupleGetItem(func_1248_call(relay.reshape(const_10799.astype('int8'), [28, 1]), relay.reshape(const_10800.astype('int8'), [448,]), ), 0)
output = relay.Tuple([call_10790,call_10798,const_10799,const_10800,])
output2 = relay.Tuple([call_10791,call_10801,const_10799,const_10800,])
func_10808 = relay.Function([], output)
mod['func_10808'] = func_10808
mod = relay.transform.InferType()(mod)
mutated_mod['func_10808'] = func_10808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10808_call = mutated_mod.get_global_var('func_10808')
call_10809 = func_10808_call()
output = call_10809
func_10810 = relay.Function([], output)
mutated_mod['func_10810'] = func_10810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3838_call = mod.get_global_var('func_3838')
func_3840_call = mutated_mod.get_global_var('func_3840')
call_10926 = relay.TupleGetItem(func_3838_call(), 2)
call_10927 = relay.TupleGetItem(func_3840_call(), 2)
output = call_10926
output2 = call_10927
func_10943 = relay.Function([], output)
mod['func_10943'] = func_10943
mod = relay.transform.InferType()(mod)
mutated_mod['func_10943'] = func_10943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10943_call = mutated_mod.get_global_var('func_10943')
call_10944 = func_10943_call()
output = call_10944
func_10945 = relay.Function([], output)
mutated_mod['func_10945'] = func_10945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_10956 = relay.TupleGetItem(func_1104_call(), 0)
call_10957 = relay.TupleGetItem(func_1105_call(), 0)
func_8985_call = mod.get_global_var('func_8985')
func_8989_call = mutated_mod.get_global_var('func_8989')
var_10959 = relay.var("var_10959", dtype = "float64", shape = (108,))#candidate|10959|(108,)|var|float64
const_10960 = relay.const([9,-5,-10,6,3,-1,-5,-5,-1,-8,-7,9,4,4,-7,10,-1,-2,6,-8,2,-5,-8,-6,7,-3,2,10,5,-4,1,2,-10,2,-4,9,10,1,-4,8,-2,8,2,9,-4,-4,8,-6,10,-8,-10,8,-9,-9,-5,-4,7,2,10,7,-6,-10,4,-5,-5,7,-10,-5,-4,-3,1,-8,9,-8,-5,4,5,-8,-9,-5,7,-10,-9,-5,-1,-3,-6,-1,-5,8,3,1,-8,-8,3,-3,-7,7,-10,-8,3,-5,2,-7,-6,-7,7,-10,-9,1,-2,-4,7,-5,-6,-2,-2,-1,7,-3,3,4,10,-4,-2,10,-9,-5,8,5,-2,-4,-6,-1,4,-5,-6,4,3,-2,3,3,8,8], dtype = "int8")#candidate|10960|(144,)|const|int8
call_10958 = relay.TupleGetItem(func_8985_call(relay.reshape(var_10959.astype('float64'), [6, 3, 6]), relay.reshape(const_10960.astype('int8'), [144,]), ), 13)
call_10961 = relay.TupleGetItem(func_8989_call(relay.reshape(var_10959.astype('float64'), [6, 3, 6]), relay.reshape(const_10960.astype('int8'), [144,]), ), 13)
output = relay.Tuple([call_10956,call_10958,var_10959,const_10960,])
output2 = relay.Tuple([call_10957,call_10961,var_10959,const_10960,])
func_10967 = relay.Function([var_10959,], output)
mod['func_10967'] = func_10967
mod = relay.transform.InferType()(mod)
var_10968 = relay.var("var_10968", dtype = "float64", shape = (108,))#candidate|10968|(108,)|var|float64
output = func_10967(var_10968)
func_10969 = relay.Function([var_10968], output)
mutated_mod['func_10969'] = func_10969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6875_call = mod.get_global_var('func_6875')
func_6876_call = mutated_mod.get_global_var('func_6876')
call_11012 = func_6875_call()
call_11013 = func_6875_call()
func_4002_call = mod.get_global_var('func_4002')
func_4003_call = mutated_mod.get_global_var('func_4003')
call_11021 = func_4002_call()
call_11022 = func_4002_call()
func_5975_call = mod.get_global_var('func_5975')
func_5977_call = mutated_mod.get_global_var('func_5977')
call_11025 = relay.TupleGetItem(func_5975_call(), 0)
call_11026 = relay.TupleGetItem(func_5977_call(), 0)
func_1184_call = mod.get_global_var('func_1184')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_11028 = func_1184_call()
call_11029 = func_1184_call()
output = relay.Tuple([call_11012,call_11021,call_11025,call_11028,])
output2 = relay.Tuple([call_11013,call_11022,call_11026,call_11029,])
func_11038 = relay.Function([], output)
mod['func_11038'] = func_11038
mod = relay.transform.InferType()(mod)
mutated_mod['func_11038'] = func_11038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11038_call = mutated_mod.get_global_var('func_11038')
call_11039 = func_11038_call()
output = call_11039
func_11040 = relay.Function([], output)
mutated_mod['func_11040'] = func_11040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_11053 = relay.TupleGetItem(func_1104_call(), 0)
call_11054 = relay.TupleGetItem(func_1105_call(), 0)
output = relay.Tuple([call_11053,])
output2 = relay.Tuple([call_11054,])
func_11057 = relay.Function([], output)
mod['func_11057'] = func_11057
mod = relay.transform.InferType()(mod)
output = func_11057()
func_11058 = relay.Function([], output)
mutated_mod['func_11058'] = func_11058
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11116 = relay.var("var_11116", dtype = "float64", shape = ())#candidate|11116|()|var|float64
const_11117 = relay.const([[[-7.868492,0.755387,-9.036759,-9.287437,-3.984361,0.373970,9.797506,-8.141317,6.226369,-1.353657,7.415071,-7.775658],[5.585251,-1.858663,-3.701617,-6.085758,7.114606,-6.637635,8.679771,-1.369153,-1.228439,-0.064446,5.808981,-5.694970],[-3.366920,-1.895646,8.516837,9.103242,9.870221,6.439567,3.500436,-4.134219,2.919556,-3.791243,5.594416,-7.543759],[7.582418,-4.262894,-6.787652,2.855273,7.664742,-7.147419,-4.875293,-3.793105,2.889049,4.530465,0.503009,0.837008],[0.383244,0.880852,-4.498067,-1.476200,-6.222114,-6.693273,3.706509,2.060266,-4.987405,0.093156,4.437386,-7.052882],[6.465195,3.605238,5.538237,6.081181,8.651681,8.394017,7.818207,1.640399,-3.150238,-4.046415,2.447948,7.413331],[6.888227,-2.932229,-7.245062,3.777371,8.136926,-1.747813,6.993923,7.981243,-7.131186,-9.126685,-2.986933,8.241679],[9.593510,-9.959288,0.025008,-7.750164,-5.406815,-9.164453,4.990724,2.782056,-4.408358,9.583891,1.847460,-4.636126],[-3.176049,4.588446,-0.543709,5.063246,-0.802963,-2.435897,0.421579,-2.573729,-4.353666,-7.087807,-0.032578,-0.120264]],[[2.515528,-9.329356,-4.317377,-4.350073,9.070655,0.724153,-6.631877,-4.485341,-4.909158,0.526191,2.834661,9.563960],[-7.114573,-0.954238,3.278063,9.396638,-1.350520,-8.895496,4.751132,4.210299,-1.342262,-4.077119,-7.323715,-3.921874],[-1.584723,-0.132411,3.859844,2.569166,-9.598448,5.254891,-5.545077,-1.387790,-6.361157,2.890250,-2.677870,9.835357],[9.661782,1.344911,-1.403895,-6.061714,2.737336,-8.452454,-3.273293,-6.525544,8.049067,4.423777,6.123635,5.227375],[-3.208713,1.309886,2.750707,9.533587,-3.172926,-4.205797,-5.970656,8.078822,-8.345395,0.887856,8.207963,0.637703],[1.235227,-7.710514,-9.338729,-2.081764,-1.675352,7.560396,-3.937821,-8.835965,-3.240213,8.280120,7.215828,-4.665322],[2.883626,8.744501,-4.559217,2.578734,3.033088,-1.921472,1.357614,-9.384216,-4.300390,-0.540833,-6.853840,3.637397],[4.540254,-0.936196,-5.979531,-8.552210,-8.589394,-1.610208,-4.668744,-7.635838,-9.883545,-6.448578,0.422646,1.219323],[-4.071776,5.087610,7.423694,4.070942,9.077363,8.404729,4.049256,2.991973,8.101643,-8.432127,-7.789839,9.380530]],[[8.475439,-8.298555,-5.659116,-8.320191,8.554863,-5.392198,-8.434623,-5.911088,6.696790,3.071358,4.873642,-0.618941],[0.321981,9.977904,0.463434,-6.771300,-7.024287,6.306969,-8.016611,6.423147,1.929020,-3.205109,-4.437002,-7.193083],[5.986424,-9.961904,-4.815847,3.600316,4.107700,7.860268,-2.546886,5.230016,1.103343,6.199849,-3.051097,9.836804],[-9.647109,6.822253,-6.847324,-9.957094,-2.185693,2.720604,5.222161,-2.501335,3.604412,8.462226,5.268949,-3.623587],[-8.925522,-4.942813,-7.158093,-5.152148,-7.927841,5.317825,6.966789,-3.640245,-3.553663,5.503303,-1.583782,-5.453428],[4.989113,4.382480,-6.323652,4.104726,-1.801463,0.708776,-4.580969,8.509555,-2.030462,8.437013,0.129657,5.132362],[6.175754,2.744414,-0.224036,1.133749,-5.540694,-5.377241,-1.270959,8.912809,8.170801,-2.596565,-8.579530,-0.929086],[-9.905619,1.909851,4.275335,-2.222361,3.094245,0.545635,1.279378,0.019672,3.467645,2.709036,-7.298302,-5.123332],[0.993559,8.659720,0.015587,-7.355670,9.903630,2.499573,-7.191825,-2.515241,4.817305,4.234544,-0.915885,-8.383308]],[[-6.420445,-1.441357,-9.608119,7.398132,5.905663,-3.914167,-4.181219,-7.570158,-0.525696,7.917990,4.250962,-0.906985],[2.932930,-7.048062,-4.523201,4.853735,-5.467802,9.111305,4.126081,-5.146441,2.503947,6.777133,-3.129547,-2.011798],[1.854504,3.405275,8.043109,2.416260,-6.881909,-4.021083,0.865750,4.111243,0.193844,-3.117701,8.225738,7.141545],[2.222082,8.979857,4.292770,-2.854817,1.154800,7.457244,4.029520,7.745629,-1.209070,1.288936,1.322045,7.217795],[4.459981,2.698778,6.031453,-8.324878,0.519106,-8.640204,4.663602,0.944424,-6.783863,3.393993,-5.934972,6.034574],[-9.958437,-8.244235,-5.479826,0.091862,6.684539,-0.553155,3.736181,-3.074209,-3.881658,1.148957,7.192916,-6.934778],[-0.343371,-5.949068,-0.066747,8.547242,-1.206065,7.921345,-8.394946,-9.225623,2.433226,-3.719534,6.774154,-8.250263],[3.339351,9.605661,-7.402120,-5.880198,6.921063,4.877485,4.182254,5.552564,-0.153814,-9.495355,9.551728,8.896419],[6.197634,0.909971,-2.103930,3.313737,-5.547529,-8.777333,-9.667797,9.344951,8.087037,-3.137295,1.643802,-9.070436]],[[-5.785920,-5.220100,-1.891538,-6.549386,5.182048,-8.900914,9.411318,0.273162,6.800402,0.481141,2.720043,4.140581],[4.920562,7.834015,0.338688,3.950496,-8.486853,9.419419,1.625789,-4.792428,-2.479531,-5.382017,-2.603463,1.074398],[8.281271,-2.500438,5.788250,-2.274485,8.320970,3.728567,8.466373,-4.641943,2.014746,-2.393068,6.798871,5.620460],[-3.643652,-0.289641,-0.756859,-3.942866,-0.901010,-2.843766,-7.203420,-8.266853,-7.183237,3.361427,-1.562847,1.211886],[0.693489,-3.842337,-9.759371,-2.924510,5.864313,-9.072013,-2.463420,-2.971262,1.666522,-3.495400,5.722825,0.242503],[8.455134,1.920462,-6.092235,0.540202,0.234805,-4.675133,7.235149,-8.595050,0.825109,-7.865791,8.777496,-4.811653],[7.602825,-0.554433,-7.062379,-8.653545,-2.051895,5.346186,-0.661076,9.846464,4.167931,-3.203099,-0.300785,8.325612],[6.652647,-6.643578,-8.319790,5.309044,0.655423,-1.439145,5.046125,7.588885,3.749756,-3.272721,1.841388,3.958740],[3.267451,-1.352667,-8.772907,-2.955755,1.184344,-5.191859,0.169368,-2.538172,1.178360,-0.267818,4.288275,1.092344]],[[2.892888,6.449617,1.438234,1.995140,-6.181446,-0.175397,7.885167,-6.123713,5.967004,6.151326,-5.848223,-8.933608],[-6.207524,-7.096913,-1.585501,-8.094425,5.547349,0.948309,-4.867321,9.644197,-1.138594,7.101390,-2.230599,-4.596121],[-7.126145,8.332325,1.847582,7.159619,-9.581280,-5.675722,4.129931,-7.155921,-8.012430,5.101352,-6.030608,1.207539],[-2.251658,9.277624,-7.979948,9.509810,7.056725,0.848293,-0.417518,-2.152447,-2.585451,2.830511,-0.356769,-9.941354],[5.483598,8.994915,-4.166343,-9.519975,-7.117008,-3.481267,-0.582830,2.232471,-0.898774,-1.865489,5.709872,1.818378],[0.283216,0.992254,4.627616,-7.803065,3.553148,-3.195057,-9.917521,7.657238,-9.810241,2.145982,5.643769,-2.755834],[7.003428,-2.009347,-2.598532,-8.561134,-1.560334,8.400062,2.247412,1.665006,6.100580,0.876785,-6.974412,-7.554300],[-2.948797,2.525927,4.214595,3.501577,0.815511,8.078346,9.745991,4.598186,-4.236300,3.985839,5.863830,-7.698973],[7.929528,-1.890168,-4.249539,-7.618755,0.650341,-8.839101,-0.952384,3.116564,0.981151,5.259662,9.686405,5.027987]],[[7.204536,6.191462,7.698444,6.001987,3.341235,-1.303066,9.263269,-2.480236,4.088881,0.137366,-5.068643,4.033853],[4.271509,2.970863,8.190038,-7.193825,1.577531,3.370189,-2.237929,2.341263,3.759177,7.578937,1.182231,2.176072],[2.255676,-8.167314,7.115375,1.003308,-7.482201,7.226456,8.688479,-8.274962,-9.911551,5.399681,-8.965726,-8.411062],[0.370272,-6.677523,-6.836720,4.070773,-6.994481,2.196303,5.444420,3.847863,0.942647,2.371509,-7.143297,-1.046583],[-4.767792,3.933635,-2.073061,-5.345441,-6.489633,-9.520349,-6.538894,-7.327651,2.211015,-2.811344,-2.180359,-2.202886],[9.154659,7.449814,8.269518,-9.013392,8.542079,2.260862,8.385443,0.401324,-0.149346,-3.610489,5.528368,-3.320263],[5.528954,0.028678,-4.279478,4.100907,-4.149992,7.385318,-7.372460,9.423227,-3.042051,-8.454519,-0.415905,9.415190],[2.121987,8.460794,-1.100080,-5.674895,-6.161662,6.408769,0.455706,-5.103717,2.390111,-5.066516,0.387872,-2.227399],[-7.573137,-8.840504,-8.157639,5.183915,8.708505,1.420567,-1.440447,4.436698,5.670021,3.898642,-4.580259,-9.843113]],[[-5.151581,2.684415,-3.854979,0.005843,-6.836619,4.358896,8.978644,4.313127,4.398006,-2.169793,-3.960591,8.446894],[-4.708509,-2.088709,-2.544613,7.184077,0.683760,9.298899,-6.923509,-9.859218,-9.884283,3.948721,0.452615,-4.604658],[5.793686,-9.683686,8.119155,-4.672993,2.060144,-9.371937,8.035490,-3.627594,-7.808873,1.775915,-3.240813,-7.827366],[3.292418,-4.814495,-3.652187,-1.963044,1.781925,9.733165,-7.611709,-6.012156,-6.705894,5.444815,-1.609306,5.097156],[9.278797,5.180193,-1.081278,-5.587530,-5.394230,-6.145424,-7.846375,-1.043086,-4.022340,-4.197304,2.629262,-0.648885],[8.329407,-2.350553,7.869934,-4.178727,-7.462648,-7.452553,1.970287,-7.566128,8.512123,-4.081538,0.656247,4.948273],[-8.777257,-6.701849,-1.844337,-9.527893,8.738400,-7.687496,-2.101206,6.933875,-3.188278,7.644557,0.212401,5.539475],[9.868264,-0.670766,1.745873,-1.171951,0.851064,4.235707,8.543213,4.882960,-1.026166,9.168059,-7.941005,5.407714],[-6.434036,6.482244,5.307268,-9.233739,-9.384559,0.030995,-8.778063,-1.912609,0.206786,8.511213,8.291979,4.826271]],[[-5.316293,-2.457961,5.942432,-0.557502,-7.241889,3.817716,-0.361645,-9.078822,-2.329948,-8.991653,9.286063,-3.722550],[4.171977,3.893962,-5.264268,-7.338824,3.074015,-7.921885,9.272864,-9.827187,-0.506535,5.207342,5.580795,3.868545],[7.073562,-8.071732,-9.198213,6.264183,8.089212,-4.195850,7.903960,-3.438756,5.640737,-8.427661,2.153336,0.990139],[-9.001123,1.381464,-1.679909,-8.197045,-9.972534,8.428509,9.251840,-5.180443,9.334198,5.628758,-1.330840,-2.764310],[-7.650308,-9.033209,7.766799,5.128492,-6.119554,-7.965209,2.646748,-8.163125,9.081434,5.084121,7.345115,6.404316],[-3.022829,8.661161,6.501106,5.754511,-9.627466,3.272914,6.170980,-5.720497,9.968441,-2.951716,2.640184,9.045098],[-2.805769,5.215767,-3.276949,7.644347,1.000744,9.042705,-3.010575,-3.785553,-7.376417,-9.659413,-3.812619,9.468383],[1.454237,5.934718,6.785007,-2.942625,7.309170,3.477638,-5.952757,-4.044305,3.858159,-5.893795,-4.345894,4.478214],[5.736204,-9.356181,-4.425834,4.896956,-8.195063,-7.457089,2.328076,8.996567,-7.446768,5.854021,7.473901,9.962433]],[[0.410784,-3.234953,-6.527685,9.005179,-9.654487,-5.711543,2.961238,-3.359172,-3.610810,4.127893,1.684728,-0.686530],[6.832279,5.371278,1.842624,-1.970322,-0.684436,1.930836,-4.016470,-8.344400,-5.867144,8.966302,2.764395,7.645104],[-8.951787,5.048359,-2.274758,8.262456,3.659126,-2.530580,9.462276,-9.513408,-8.650415,6.989985,-8.744019,5.366373],[-4.808456,-3.591912,-2.941553,5.220556,5.531498,9.300555,-2.858176,8.291951,3.568347,-6.242848,-1.699031,-5.982287],[-2.545318,1.746631,-6.508728,-3.720158,6.711458,-3.818061,-8.455857,-1.955911,-8.515941,6.953728,3.058526,9.301138],[3.185094,2.996869,-5.497266,-4.813653,9.796436,0.652396,-0.998433,-6.679256,-3.731768,9.620855,-5.320299,-8.311830],[3.008181,2.863327,9.761509,0.161697,9.230138,-1.027500,1.028359,-1.369114,9.080750,-1.049033,8.114953,6.779368],[1.102339,1.219137,5.223935,-2.359738,0.487183,8.388328,-4.756244,4.539596,9.289396,1.859505,-0.851357,-2.739045],[4.544183,0.817904,1.793061,6.472537,-0.829355,2.837951,-1.101696,-1.072793,6.646110,-9.857225,8.764251,9.023559]],[[-6.920610,3.560126,2.013572,-8.720532,-8.821567,9.020760,-8.781533,-9.185331,3.250129,-5.997628,0.915975,-0.843339],[-7.475564,4.810320,-8.729901,3.568181,1.982716,-0.583851,-0.814684,-5.669870,-6.138052,-4.174244,-8.298147,4.226280],[-0.187254,2.878215,2.892209,2.935812,1.465490,9.862251,0.368186,-9.248984,5.587558,8.840629,4.381482,-0.153095],[-8.051095,-8.292910,5.278416,-3.734557,-7.034815,0.113985,8.912450,5.533153,2.477882,1.437747,6.727916,-8.647549],[-7.381673,-2.428923,1.736934,8.378556,-1.568122,-8.294058,-0.473887,6.408890,-6.347020,-8.795287,8.757311,-8.332777],[-5.905115,-4.588893,4.758349,-3.472677,-2.914547,6.839770,7.424917,7.665326,4.635338,4.765219,1.562700,-2.737985],[1.222004,7.465674,-6.076534,-8.968774,6.217550,2.155394,7.377990,-4.808121,-7.888258,2.703715,2.915075,1.067776],[-4.260113,-0.403113,-6.499125,2.014808,2.756510,-7.325888,4.213516,-0.080575,6.357827,8.440231,7.584807,9.555986],[-3.741005,4.416909,1.715802,-7.446871,8.203671,4.144100,6.617363,2.126656,-3.099063,-3.824519,-2.581469,-1.362005]],[[-2.658223,-2.153723,-6.584172,-7.149085,-4.463928,-8.591017,-1.071853,5.223977,5.033320,6.408794,-9.575417,8.617892],[5.253396,-0.821608,-5.391831,2.314200,-5.105655,-1.627627,9.635049,6.556330,-5.034161,-8.141212,-8.972418,-6.547714],[-2.853520,-1.277991,-8.638064,3.931349,-1.133251,-5.004240,7.513832,5.988021,5.050029,-2.582379,-5.789329,5.613273],[9.736798,-8.949929,0.188177,8.183718,-0.894939,-2.482075,5.891102,-3.600120,0.790216,-7.486032,1.871170,3.758203],[2.978212,5.102612,7.363599,-8.635461,-4.702343,1.988653,4.704691,-2.044731,-2.778388,-0.356280,-1.270844,5.021726],[0.314206,-7.733498,-1.270119,-0.484503,3.495020,1.130600,-6.574651,6.656712,-8.387031,-6.434323,5.586528,-2.052905],[-7.352470,1.509805,8.028627,-7.230143,-2.716272,2.818738,-3.052006,-3.273919,-0.473290,4.694123,8.619977,8.622340],[4.893271,0.776159,-3.077060,-5.795941,1.920915,-0.542859,8.312711,8.147423,4.169724,-2.865829,-0.169631,-9.788161],[-7.113433,9.724269,-0.720005,-9.226026,5.027344,2.232107,6.762068,-0.491210,6.824821,2.910667,2.840836,1.862657]],[[-2.221043,6.521942,-2.033235,9.682315,9.089665,2.777909,1.231426,3.939566,1.612427,6.404352,-2.363372,9.747169],[-3.210861,-9.618075,-4.251922,-0.194729,5.193596,4.481122,2.232700,2.312701,-7.172399,3.226783,-9.033865,-5.056772],[2.736504,-9.553752,0.093654,5.746260,-7.030255,9.916896,6.542057,2.683565,0.009019,5.772631,7.277204,7.571442],[4.736269,-7.026617,4.079101,3.041161,-9.673889,5.570888,-0.444619,6.891670,-0.244776,9.540073,-6.958771,8.913502],[8.280428,3.318363,2.571506,-1.458981,3.537937,-9.477679,1.912569,9.557504,5.850595,1.058738,8.172673,-3.783581],[-6.166837,-3.307735,1.056647,-8.147890,-2.343290,2.135123,2.183872,-9.132863,-3.661939,4.172068,-2.757751,3.791532],[8.088712,2.889409,7.507498,7.566817,8.222332,0.750695,1.280097,-2.675402,9.810401,2.809534,3.858783,0.068311],[-4.038584,-9.967413,1.310104,-0.343374,-4.845335,7.275161,2.943069,5.264189,-9.396656,5.389379,8.562160,3.796740],[-6.246753,5.298857,-1.481847,9.684898,3.434755,-6.370916,-8.963624,-7.366586,-8.409959,-5.541253,-2.764800,1.547689]],[[-9.812249,-7.922224,-5.247691,-0.410104,-0.727196,-2.599229,-5.120652,8.543627,7.225134,-9.760968,-7.660946,6.477377],[6.275506,-3.941113,4.569280,-8.379878,7.560690,8.477467,4.104785,-5.991368,8.121516,-1.496042,-1.936698,-4.016019],[3.559826,4.080553,5.700528,8.091854,6.316684,-4.204167,4.378936,-8.997388,8.337203,-8.801933,-3.780199,-6.321791],[7.122918,8.106746,-4.740543,-1.103528,0.984148,0.799009,-3.075496,5.757138,-0.817626,-7.985819,-9.190875,-4.148695],[9.327386,-0.034153,9.999724,6.185219,-8.483071,8.255147,-4.576440,-3.868931,2.631707,-8.044280,-4.654445,8.008314],[3.707487,-4.397276,6.965282,4.049576,6.274873,-8.802805,-6.279105,-3.396247,-1.580993,1.176982,1.142658,-7.849484],[0.946848,-6.484966,-4.801303,2.635996,2.117040,-8.911153,-8.686744,5.243392,7.887561,0.587917,-2.126404,-3.042235],[1.791637,2.835040,-3.558711,6.014976,6.471946,0.120390,-9.427357,4.147013,9.578405,-7.101238,-8.801380,3.055950],[5.140634,2.811853,-5.588619,-1.623910,-6.388022,-3.664655,-4.026533,-1.261316,3.536988,9.230102,-5.562132,-0.443909]],[[-7.655363,-6.389337,-0.662179,3.986937,-7.123376,1.970189,-7.667279,-5.953484,-1.972497,5.744668,-9.859022,-6.137643],[-9.141008,7.527399,-9.315880,-1.556818,-4.612385,2.351587,-2.365509,-1.825076,-2.800943,-0.082431,-2.958570,9.231810],[1.999574,0.354539,-6.927467,-9.453072,5.786333,-7.016821,4.938731,0.657845,5.973915,-5.735394,2.606169,-5.974764],[7.136722,-9.339618,6.131856,-8.276774,7.359101,-1.963391,5.871945,-0.092062,3.280490,-6.952169,0.854406,-9.233817],[1.927494,-7.361767,-8.021667,-8.212753,5.260437,5.222926,-9.849513,-7.119833,0.396149,3.415081,6.279288,8.035333],[-4.252313,4.298275,9.127461,-4.900334,-9.305370,1.386263,4.269551,-1.793876,9.948013,3.345344,1.371647,5.063435],[9.485098,9.287426,-9.084111,7.529143,3.890396,-5.552518,-5.500500,6.309870,5.655808,4.382131,-9.805010,-4.289860],[1.917744,4.329504,1.007908,8.964832,2.323822,7.485886,-4.732575,3.474561,9.702583,-6.818256,-9.234231,-8.113150],[2.675692,5.746931,-4.317601,5.452596,5.954058,-3.090755,2.897274,5.024179,0.103584,-3.370086,7.667785,4.928599]]], dtype = "float64")#candidate|11117|(15, 9, 12)|const|float64
bop_11118 = relay.divide(var_11116.astype('float64'), const_11117.astype('float64')) # shape=(15, 9, 12)
func_4476_call = mod.get_global_var('func_4476')
func_4477_call = mutated_mod.get_global_var('func_4477')
call_11127 = relay.TupleGetItem(func_4476_call(), 1)
call_11128 = relay.TupleGetItem(func_4477_call(), 1)
func_1157_call = mod.get_global_var('func_1157')
func_1158_call = mutated_mod.get_global_var('func_1158')
call_11134 = func_1157_call()
call_11135 = func_1157_call()
func_3838_call = mod.get_global_var('func_3838')
func_3840_call = mutated_mod.get_global_var('func_3840')
call_11154 = relay.TupleGetItem(func_3838_call(), 0)
call_11155 = relay.TupleGetItem(func_3840_call(), 0)
uop_11168 = relay.sin(const_11117.astype('float64')) # shape=(15, 9, 12)
output = relay.Tuple([bop_11118,call_11127,call_11134,call_11154,uop_11168,])
output2 = relay.Tuple([bop_11118,call_11128,call_11135,call_11155,uop_11168,])
func_11172 = relay.Function([var_11116,], output)
mod['func_11172'] = func_11172
mod = relay.transform.InferType()(mod)
var_11173 = relay.var("var_11173", dtype = "float64", shape = ())#candidate|11173|()|var|float64
output = func_11172(var_11173)
func_11174 = relay.Function([var_11173], output)
mutated_mod['func_11174'] = func_11174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3012_call = mod.get_global_var('func_3012')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_11189 = relay.TupleGetItem(func_3012_call(), 0)
call_11190 = relay.TupleGetItem(func_3013_call(), 0)
output = relay.Tuple([call_11189,])
output2 = relay.Tuple([call_11190,])
func_11206 = relay.Function([], output)
mod['func_11206'] = func_11206
mod = relay.transform.InferType()(mod)
mutated_mod['func_11206'] = func_11206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11206_call = mutated_mod.get_global_var('func_11206')
call_11207 = func_11206_call()
output = call_11207
func_11208 = relay.Function([], output)
mutated_mod['func_11208'] = func_11208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1121_call = mutated_mod.get_global_var('func_1121')
call_11211 = relay.TupleGetItem(func_1120_call(), 0)
call_11212 = relay.TupleGetItem(func_1121_call(), 0)
output = call_11211
output2 = call_11212
func_11235 = relay.Function([], output)
mod['func_11235'] = func_11235
mod = relay.transform.InferType()(mod)
mutated_mod['func_11235'] = func_11235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11235_call = mutated_mod.get_global_var('func_11235')
call_11236 = func_11235_call()
output = call_11236
func_11237 = relay.Function([], output)
mutated_mod['func_11237'] = func_11237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7843_call = mod.get_global_var('func_7843')
func_7844_call = mutated_mod.get_global_var('func_7844')
call_11240 = relay.TupleGetItem(func_7843_call(), 0)
call_11241 = relay.TupleGetItem(func_7844_call(), 0)
output = call_11240
output2 = call_11241
func_11242 = relay.Function([], output)
mod['func_11242'] = func_11242
mod = relay.transform.InferType()(mod)
mutated_mod['func_11242'] = func_11242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11242_call = mutated_mod.get_global_var('func_11242')
call_11243 = func_11242_call()
output = call_11243
func_11244 = relay.Function([], output)
mutated_mod['func_11244'] = func_11244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1368_call = mod.get_global_var('func_1368')
func_1370_call = mutated_mod.get_global_var('func_1370')
call_11257 = func_1368_call()
call_11258 = func_1368_call()
func_3634_call = mod.get_global_var('func_3634')
func_3635_call = mutated_mod.get_global_var('func_3635')
call_11265 = relay.TupleGetItem(func_3634_call(), 0)
call_11266 = relay.TupleGetItem(func_3635_call(), 0)
func_7001_call = mod.get_global_var('func_7001')
func_7003_call = mutated_mod.get_global_var('func_7003')
call_11283 = relay.TupleGetItem(func_7001_call(), 0)
call_11284 = relay.TupleGetItem(func_7003_call(), 0)
func_9293_call = mod.get_global_var('func_9293')
func_9295_call = mutated_mod.get_global_var('func_9295')
call_11288 = func_9293_call()
call_11289 = func_9293_call()
output = relay.Tuple([call_11257,call_11265,call_11283,call_11288,])
output2 = relay.Tuple([call_11258,call_11266,call_11284,call_11289,])
func_11302 = relay.Function([], output)
mod['func_11302'] = func_11302
mod = relay.transform.InferType()(mod)
output = func_11302()
func_11303 = relay.Function([], output)
mutated_mod['func_11303'] = func_11303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6362_call = mod.get_global_var('func_6362')
func_6363_call = mutated_mod.get_global_var('func_6363')
call_11317 = relay.TupleGetItem(func_6362_call(), 1)
call_11318 = relay.TupleGetItem(func_6363_call(), 1)
func_10535_call = mod.get_global_var('func_10535')
func_10536_call = mutated_mod.get_global_var('func_10536')
call_11319 = relay.TupleGetItem(func_10535_call(), 1)
call_11320 = relay.TupleGetItem(func_10536_call(), 1)
func_8114_call = mod.get_global_var('func_8114')
func_8115_call = mutated_mod.get_global_var('func_8115')
call_11359 = relay.TupleGetItem(func_8114_call(), 0)
call_11360 = relay.TupleGetItem(func_8115_call(), 0)
func_7567_call = mod.get_global_var('func_7567')
func_7569_call = mutated_mod.get_global_var('func_7569')
call_11362 = relay.TupleGetItem(func_7567_call(), 0)
call_11363 = relay.TupleGetItem(func_7569_call(), 0)
output = relay.Tuple([call_11317,call_11319,call_11359,call_11362,])
output2 = relay.Tuple([call_11318,call_11320,call_11360,call_11363,])
func_11370 = relay.Function([], output)
mod['func_11370'] = func_11370
mod = relay.transform.InferType()(mod)
output = func_11370()
func_11371 = relay.Function([], output)
mutated_mod['func_11371'] = func_11371
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11372 = relay.var("var_11372", dtype = "float32", shape = (9, 9, 7))#candidate|11372|(9, 9, 7)|var|float32
uop_11373 = relay.log10(var_11372.astype('float32')) # shape=(9, 9, 7)
var_11381 = relay.var("var_11381", dtype = "float32", shape = (9, 9, 7))#candidate|11381|(9, 9, 7)|var|float32
bop_11382 = relay.power(uop_11373.astype('float64'), relay.reshape(var_11381.astype('float64'), relay.shape_of(uop_11373))) # shape=(9, 9, 7)
output = bop_11382
output2 = bop_11382
func_11386 = relay.Function([var_11372,var_11381,], output)
mod['func_11386'] = func_11386
mod = relay.transform.InferType()(mod)
mutated_mod['func_11386'] = func_11386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11386_call = mutated_mod.get_global_var('func_11386')
var_11388 = relay.var("var_11388", dtype = "float32", shape = (9, 9, 7))#candidate|11388|(9, 9, 7)|var|float32
var_11389 = relay.var("var_11389", dtype = "float32", shape = (9, 9, 7))#candidate|11389|(9, 9, 7)|var|float32
call_11387 = func_11386_call(var_11388,var_11389,)
output = call_11387
func_11390 = relay.Function([var_11388,var_11389,], output)
mutated_mod['func_11390'] = func_11390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7461_call = mod.get_global_var('func_7461')
func_7462_call = mutated_mod.get_global_var('func_7462')
call_11464 = relay.TupleGetItem(func_7461_call(), 0)
call_11465 = relay.TupleGetItem(func_7462_call(), 0)
output = call_11464
output2 = call_11465
func_11467 = relay.Function([], output)
mod['func_11467'] = func_11467
mod = relay.transform.InferType()(mod)
output = func_11467()
func_11468 = relay.Function([], output)
mutated_mod['func_11468'] = func_11468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9236_call = mod.get_global_var('func_9236')
func_9237_call = mutated_mod.get_global_var('func_9237')
call_11474 = func_9236_call()
call_11475 = func_9236_call()
func_8288_call = mod.get_global_var('func_8288')
func_8291_call = mutated_mod.get_global_var('func_8291')
var_11477 = relay.var("var_11477", dtype = "int8", shape = ())#candidate|11477|()|var|int8
const_11478 = relay.const([5,-10,7,-5,-9,-5,-9,10,1,-8,-10,-6,-6,-7,3,-8,1,5,-1,7,3,8,8,7,-7,-8,8,5,5,6,-6,-8,2,7,6,-3,5,2,1,-7,-6,7,-8,-10,8,3,-8,-3,2,4,-5,8,-10,5,10,10,-8,-2,1,1,7,3,3,-8,9,5,-10,-6,-3,-4,5,-1,-2,9,-6,-3,4,-2,4,-6,-3,7,-5,-6,3,3,5,-1,10,2,-2,-1,-3,-7,-5,1,5,-1,-10,3,10,-1,2,4,4,10,-3,6,5,4,-8,6,-3,-8,-6,8,6,3,-3,-2,2,-7,-4,-10,8,-7,-9,2,9,-4,-8,3,4,-2,2,8,-7,-9,-7,7,3,2,6,3], dtype = "int8")#candidate|11478|(144,)|const|int8
call_11476 = relay.TupleGetItem(func_8288_call(relay.reshape(var_11477.astype('int8'), []), relay.reshape(const_11478.astype('int8'), [9, 16, 1]), ), 1)
call_11479 = relay.TupleGetItem(func_8291_call(relay.reshape(var_11477.astype('int8'), []), relay.reshape(const_11478.astype('int8'), [9, 16, 1]), ), 1)
output = relay.Tuple([call_11474,call_11476,var_11477,const_11478,])
output2 = relay.Tuple([call_11475,call_11479,var_11477,const_11478,])
func_11481 = relay.Function([var_11477,], output)
mod['func_11481'] = func_11481
mod = relay.transform.InferType()(mod)
var_11482 = relay.var("var_11482", dtype = "int8", shape = ())#candidate|11482|()|var|int8
output = func_11481(var_11482)
func_11483 = relay.Function([var_11482], output)
mutated_mod['func_11483'] = func_11483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9535_call = mod.get_global_var('func_9535')
func_9536_call = mutated_mod.get_global_var('func_9536')
call_11607 = func_9535_call()
call_11608 = func_9535_call()
func_4301_call = mod.get_global_var('func_4301')
func_4303_call = mutated_mod.get_global_var('func_4303')
call_11610 = func_4301_call()
call_11611 = func_4301_call()
output = relay.Tuple([call_11607,call_11610,])
output2 = relay.Tuple([call_11608,call_11611,])
func_11618 = relay.Function([], output)
mod['func_11618'] = func_11618
mod = relay.transform.InferType()(mod)
mutated_mod['func_11618'] = func_11618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11618_call = mutated_mod.get_global_var('func_11618')
call_11619 = func_11618_call()
output = call_11619
func_11620 = relay.Function([], output)
mutated_mod['func_11620'] = func_11620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9370_call = mod.get_global_var('func_9370')
func_9371_call = mutated_mod.get_global_var('func_9371')
call_11644 = relay.TupleGetItem(func_9370_call(), 2)
call_11645 = relay.TupleGetItem(func_9371_call(), 2)
func_1263_call = mod.get_global_var('func_1263')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_11676 = func_1263_call()
call_11677 = func_1263_call()
func_10666_call = mod.get_global_var('func_10666')
func_10668_call = mutated_mod.get_global_var('func_10668')
const_11690 = relay.const([[2.692832,-4.227718,6.279585,-4.608175,3.493054,-2.992414,6.726308,-9.554506,7.873514,4.670936,2.965220,9.520635,5.239256,1.841692,-4.723105,-3.027805],[8.763030,9.645435,4.644286,3.609839,-2.698443,9.998719,-8.301290,0.534267,-2.451004,5.002585,5.664454,-0.135693,6.252159,-7.990389,-9.847151,-8.690423],[3.770798,-7.539280,2.037122,-5.743635,6.915585,7.227896,3.652004,0.625712,-8.677233,5.915075,1.225257,-2.944042,8.760013,-3.208334,4.016911,4.413733],[-2.606118,0.040900,-6.859830,3.463687,-9.543061,1.525726,4.714339,2.190080,-7.609836,-2.977618,5.327486,-5.643873,4.965187,-6.467646,5.999512,-9.822848],[5.544972,-8.344906,0.783073,8.229433,-2.005035,3.788692,-4.495683,8.540801,8.073091,-6.018477,0.351754,-4.787314,-2.170832,8.209675,-6.948653,2.216961],[-1.210652,9.287765,-8.713429,9.449746,-5.086163,-6.650996,4.443834,2.047073,3.084670,0.786291,-2.476780,-3.252138,-3.732131,0.607828,0.651095,-8.956582],[-6.019234,5.121996,2.402105,9.257898,2.237664,-0.770639,-7.345330,0.546846,8.764549,-6.099381,-5.587475,-4.910244,-2.894474,-9.935920,1.276286,1.219336],[-5.761629,-6.690415,1.886194,2.447352,4.057001,-6.267225,2.121479,-6.851621,-1.237801,3.744130,0.802371,-0.170498,1.608239,3.035270,1.993681,-2.209609]], dtype = "float32")#candidate|11690|(8, 16)|const|float32
call_11689 = relay.TupleGetItem(func_10666_call(relay.reshape(const_11690.astype('float32'), [8, 16, 1])), 0)
call_11691 = relay.TupleGetItem(func_10668_call(relay.reshape(const_11690.astype('float32'), [8, 16, 1])), 0)
func_11235_call = mod.get_global_var('func_11235')
func_11237_call = mutated_mod.get_global_var('func_11237')
call_11692 = func_11235_call()
call_11693 = func_11235_call()
output = relay.Tuple([call_11644,call_11676,call_11689,const_11690,call_11692,])
output2 = relay.Tuple([call_11645,call_11677,call_11691,const_11690,call_11693,])
func_11698 = relay.Function([], output)
mod['func_11698'] = func_11698
mod = relay.transform.InferType()(mod)
output = func_11698()
func_11699 = relay.Function([], output)
mutated_mod['func_11699'] = func_11699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7461_call = mod.get_global_var('func_7461')
func_7462_call = mutated_mod.get_global_var('func_7462')
call_11747 = relay.TupleGetItem(func_7461_call(), 1)
call_11748 = relay.TupleGetItem(func_7462_call(), 1)
func_1263_call = mod.get_global_var('func_1263')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_11762 = func_1263_call()
call_11763 = func_1263_call()
output = relay.Tuple([call_11747,call_11762,])
output2 = relay.Tuple([call_11748,call_11763,])
func_11770 = relay.Function([], output)
mod['func_11770'] = func_11770
mod = relay.transform.InferType()(mod)
mutated_mod['func_11770'] = func_11770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11770_call = mutated_mod.get_global_var('func_11770')
call_11771 = func_11770_call()
output = call_11771
func_11772 = relay.Function([], output)
mutated_mod['func_11772'] = func_11772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2486_call = mod.get_global_var('func_2486')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_11822 = relay.TupleGetItem(func_2486_call(), 1)
call_11823 = relay.TupleGetItem(func_2487_call(), 1)
func_3012_call = mod.get_global_var('func_3012')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_11835 = relay.TupleGetItem(func_3012_call(), 1)
call_11836 = relay.TupleGetItem(func_3013_call(), 1)
output = relay.Tuple([call_11822,call_11835,])
output2 = relay.Tuple([call_11823,call_11836,])
func_11850 = relay.Function([], output)
mod['func_11850'] = func_11850
mod = relay.transform.InferType()(mod)
mutated_mod['func_11850'] = func_11850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11850_call = mutated_mod.get_global_var('func_11850')
call_11851 = func_11850_call()
output = call_11851
func_11852 = relay.Function([], output)
mutated_mod['func_11852'] = func_11852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7461_call = mod.get_global_var('func_7461')
func_7462_call = mutated_mod.get_global_var('func_7462')
call_11913 = relay.TupleGetItem(func_7461_call(), 0)
call_11914 = relay.TupleGetItem(func_7462_call(), 0)
func_8356_call = mod.get_global_var('func_8356')
func_8358_call = mutated_mod.get_global_var('func_8358')
call_11949 = func_8356_call()
call_11950 = func_8356_call()
func_6398_call = mod.get_global_var('func_6398')
func_6400_call = mutated_mod.get_global_var('func_6400')
call_11969 = relay.TupleGetItem(func_6398_call(), 1)
call_11970 = relay.TupleGetItem(func_6400_call(), 1)
output = relay.Tuple([call_11913,call_11949,call_11969,])
output2 = relay.Tuple([call_11914,call_11950,call_11970,])
func_11974 = relay.Function([], output)
mod['func_11974'] = func_11974
mod = relay.transform.InferType()(mod)
mutated_mod['func_11974'] = func_11974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11974_call = mutated_mod.get_global_var('func_11974')
call_11975 = func_11974_call()
output = call_11975
func_11976 = relay.Function([], output)
mutated_mod['func_11976'] = func_11976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11206_call = mod.get_global_var('func_11206')
func_11208_call = mutated_mod.get_global_var('func_11208')
call_11998 = relay.TupleGetItem(func_11206_call(), 0)
call_11999 = relay.TupleGetItem(func_11208_call(), 0)
output = relay.Tuple([call_11998,])
output2 = relay.Tuple([call_11999,])
func_12000 = relay.Function([], output)
mod['func_12000'] = func_12000
mod = relay.transform.InferType()(mod)
mutated_mod['func_12000'] = func_12000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12000_call = mutated_mod.get_global_var('func_12000')
call_12001 = func_12000_call()
output = call_12001
func_12002 = relay.Function([], output)
mutated_mod['func_12002'] = func_12002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10943_call = mod.get_global_var('func_10943')
func_10945_call = mutated_mod.get_global_var('func_10945')
call_12036 = func_10943_call()
call_12037 = func_10943_call()
output = call_12036
output2 = call_12037
func_12040 = relay.Function([], output)
mod['func_12040'] = func_12040
mod = relay.transform.InferType()(mod)
output = func_12040()
func_12041 = relay.Function([], output)
mutated_mod['func_12041'] = func_12041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_12081 = relay.TupleGetItem(func_2815_call(), 1)
call_12082 = relay.TupleGetItem(func_2816_call(), 1)
output = relay.Tuple([call_12081,])
output2 = relay.Tuple([call_12082,])
func_12091 = relay.Function([], output)
mod['func_12091'] = func_12091
mod = relay.transform.InferType()(mod)
mutated_mod['func_12091'] = func_12091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12091_call = mutated_mod.get_global_var('func_12091')
call_12092 = func_12091_call()
output = call_12092
func_12093 = relay.Function([], output)
mutated_mod['func_12093'] = func_12093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5293_call = mod.get_global_var('func_5293')
func_5294_call = mutated_mod.get_global_var('func_5294')
call_12176 = func_5293_call()
call_12177 = func_5293_call()
output = call_12176
output2 = call_12177
func_12197 = relay.Function([], output)
mod['func_12197'] = func_12197
mod = relay.transform.InferType()(mod)
output = func_12197()
func_12198 = relay.Function([], output)
mutated_mod['func_12198'] = func_12198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1157_call = mod.get_global_var('func_1157')
func_1158_call = mutated_mod.get_global_var('func_1158')
call_12259 = func_1157_call()
call_12260 = func_1157_call()
output = call_12259
output2 = call_12260
func_12311 = relay.Function([], output)
mod['func_12311'] = func_12311
mod = relay.transform.InferType()(mod)
mutated_mod['func_12311'] = func_12311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12311_call = mutated_mod.get_global_var('func_12311')
call_12312 = func_12311_call()
output = call_12312
func_12313 = relay.Function([], output)
mutated_mod['func_12313'] = func_12313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7001_call = mod.get_global_var('func_7001')
func_7003_call = mutated_mod.get_global_var('func_7003')
call_12314 = relay.TupleGetItem(func_7001_call(), 0)
call_12315 = relay.TupleGetItem(func_7003_call(), 0)
output = relay.Tuple([call_12314,])
output2 = relay.Tuple([call_12315,])
func_12331 = relay.Function([], output)
mod['func_12331'] = func_12331
mod = relay.transform.InferType()(mod)
output = func_12331()
func_12332 = relay.Function([], output)
mutated_mod['func_12332'] = func_12332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8114_call = mod.get_global_var('func_8114')
func_8115_call = mutated_mod.get_global_var('func_8115')
call_12348 = relay.TupleGetItem(func_8114_call(), 2)
call_12349 = relay.TupleGetItem(func_8115_call(), 2)
func_4047_call = mod.get_global_var('func_4047')
func_4048_call = mutated_mod.get_global_var('func_4048')
call_12351 = relay.TupleGetItem(func_4047_call(), 1)
call_12352 = relay.TupleGetItem(func_4048_call(), 1)
output = relay.Tuple([call_12348,call_12351,])
output2 = relay.Tuple([call_12349,call_12352,])
func_12381 = relay.Function([], output)
mod['func_12381'] = func_12381
mod = relay.transform.InferType()(mod)
output = func_12381()
func_12382 = relay.Function([], output)
mutated_mod['func_12382'] = func_12382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7001_call = mod.get_global_var('func_7001')
func_7003_call = mutated_mod.get_global_var('func_7003')
call_12388 = relay.TupleGetItem(func_7001_call(), 0)
call_12389 = relay.TupleGetItem(func_7003_call(), 0)
func_9195_call = mod.get_global_var('func_9195')
func_9197_call = mutated_mod.get_global_var('func_9197')
var_12391 = relay.var("var_12391", dtype = "float64", shape = (132,))#candidate|12391|(132,)|var|float64
call_12390 = relay.TupleGetItem(func_9195_call(relay.reshape(var_12391.astype('float64'), [3, 4, 11])), 1)
call_12392 = relay.TupleGetItem(func_9197_call(relay.reshape(var_12391.astype('float64'), [3, 4, 11])), 1)
func_11386_call = mod.get_global_var('func_11386')
func_11390_call = mutated_mod.get_global_var('func_11390')
const_12407 = relay.const([8.339302,-3.818312,0.011617,6.091252,5.814311,5.257131,9.766776,5.645325,-4.338790,1.388730,-4.309410,9.295012,-8.830451,-2.264888,-9.509670,-1.755030,2.536626,-3.287845,5.645205,8.109857,1.544360,-6.940162,-1.984912,-6.435608,2.008129,-9.961536,-4.994065,-9.846410,-8.088466,3.069629,3.120658,-7.246679,-6.649158,6.097374,-3.433538,-6.018101,3.710559,9.618403,-5.822866,9.955789,2.976320,9.686389,9.118408,-2.338314,5.736652,-0.900027,1.161954,6.513453,0.845539,-9.523145,1.670370,0.221219,7.137427,-4.806103,-3.065098,-8.350390,8.215764,-4.708153,8.727846,8.227034,-8.097674,4.968286,-0.231009,3.211041,9.451253,-3.313795,6.733949,5.024234,-4.504414,-8.324193,1.947308,-7.911255,4.310341,-9.177322,0.791377,0.633820,0.810094,8.254721,9.494242,-1.738393,-7.214764,-5.747330,-6.047341,5.932895,3.422670,-6.196564,-9.513660,-6.369198,0.770427,-1.854549,-0.960925,-7.772961,-9.470530,0.792412,-3.332342,-0.105385,-7.048958,-3.852839,-3.061166,5.030418,-9.045753,6.988759,-8.825956,-0.607448,-9.685920,-5.671284,-3.619894,-1.043552,5.696092,-5.443910,7.194658,-8.400409,2.294028,7.552067,-5.525443,-6.561620,-2.965581,0.660576,0.500156,-8.757406,-6.268364,-0.787146,3.970118,5.021714,-2.049225,-4.611318,-0.689246,-0.082616,-9.954358,-6.538455,-7.663688,2.968640,-4.074262,-9.995363,-7.503153,3.761835,5.394729,5.307235,-4.132698,2.511570,-7.449678,4.924830,6.213995,8.041493,2.349034,-0.710480,-4.514503,-7.261329,7.383410,-9.160310,5.395713,-6.497775,9.983126,7.722580,4.536360,-2.509019,-6.039791,-1.213897,5.455326,5.575304,0.768979,4.591863,1.558228,-7.954547,-3.565617,-5.585292,-4.636309,-0.532900,-3.131775,-4.788494,9.688020,-9.351689,-7.316593,7.479255,-5.487243,-9.797547,-4.902878,2.808105,8.501544,-9.665265,-3.571108,8.658831,-9.198356,-5.731551,5.153593,-4.154797,2.201100,-0.462905,6.496201,-6.783721,1.219791,-8.325293,-2.741696,6.048451,9.072470,1.936369,6.985638,9.340786,-2.214713,-0.401136,-9.980143,-9.915990,3.128503,6.115827,-5.399077,-7.509884,-6.327434,-1.247596,-9.243262,-2.991080,2.649454,9.088808,-0.624117,-1.799801,-5.448868,-9.298509,4.170489,1.010736,5.664701,-0.951608,-0.007006,3.613565,4.749971,2.555460,-4.620908,9.697962,4.881314,-6.816299,9.318205,-1.370929,7.967299,-7.676835,-3.632211,-0.876572,-4.789179,5.315723,7.269888,4.405524,-3.909929,1.976321,-4.964314,2.512906,8.200860,1.488482,-8.992236,6.095536,-3.174182,1.359383,1.634486,3.883536,-4.662217,-4.395402,2.730170,-1.187035,-3.892548,-5.887325,-7.550321,-4.799582,9.667740,5.118763,2.595037,-5.275037,-6.004798,-0.641546,2.797890,-2.611344,7.730076,2.940056,-1.092615,-2.441938,1.346118,-0.875612,-4.032382,-6.783221,-7.799838,-9.489555,-0.185324,-7.038461,-7.247232,-5.563339,-0.869379,5.539687,3.710044,-5.428442,-2.148141,-0.339673,-8.044546,9.960437,2.054691,-9.936366,1.021344,2.586688,4.769433,6.144092,6.577354,8.181800,-4.011577,1.899561,-4.625728,0.187902,-5.148920,-2.218659,-4.843180,-2.954631,6.808755,-5.600006,3.314148,-6.809035,2.781440,-4.666174,3.015302,-6.738326,-4.378857,4.134873,4.825594,9.743130,-3.292991,-4.642078,9.509533,-3.345247,-2.374058,-3.803524,9.463529,-4.878415,-7.909725,9.158348,5.290676,2.437542,6.060651,-7.059017,1.180375,-9.584275,0.496053,1.754613,5.235570,-4.988170,-7.976840,6.074673,9.562440,-8.926328,-2.178090,-4.927680,0.843744,9.567239,-0.719887,8.416283,2.486068,-1.208751,2.541022,-0.841381,0.636577,-3.662007,3.158944,2.893604,8.224771,-6.600385,0.480101,0.020284,-7.154514,3.584410,-3.631161,-3.611774,3.508785,2.901312,-3.140787,1.204673,-4.580840,3.508622,-8.104257,-1.053354,-9.069106,4.874764,3.727633,-7.674934,-5.070146,9.914408,8.715895,-1.224466,-7.304757,2.128817,5.765544,-9.596982,-3.148303,2.665176,8.163242,-6.589981,-1.242017,2.309422,4.325827,2.094076,-6.142455,-9.647479,0.460357,-7.669726,-3.090088,-6.067895,-2.833563,1.996041,7.540523,8.257628,9.317975,-4.156995,-2.314530,9.025209,-6.300836,8.606563,6.608301,-0.812995,-9.268605,-8.428394,-9.061985,5.793301,-1.387161,9.562474,6.342416,-6.146937,-4.483929,0.580931,-0.431959,-0.066429,7.196381,8.946467,-0.362322,4.571288,-8.699254,2.674254,4.431921,-4.198446,-4.380225,0.442250,-1.570781,-9.867290,-8.253596,0.918518,-3.154165,4.389742,2.220367,1.656931,-8.605741,0.073020,-3.451175,1.819803,6.764346,2.033216,6.726741,2.924260,-2.887252,6.092386,0.799700,-3.553491,-3.598674,-8.679189,-8.036477,1.288112,-2.610655,-2.308878,-0.715393,-2.789898,6.587483,2.563729,-5.240977,-4.167567,-3.228049,-9.880442,8.960357,1.855184,-3.888445,3.224628,5.823222,-9.301207,9.112372,5.094814,-9.185739,4.708753,7.337725,9.110673,-6.847590,5.024359,9.422856,-0.131779,-3.792923,-5.500289,8.099848,5.287472,0.379048,6.886743,-4.500489,-5.113390,-0.711489,-6.130556,-9.735021,-4.699930,-1.497268,7.298343,0.551682,-0.524355,9.257436,-6.050409,-2.471101,-6.359978,6.124466,5.185140,-8.586702,7.894403,9.598672,-4.537239,4.270511,-6.640321,-4.661759,8.991050,-0.908794,9.656154,-9.403213,-8.640884,-1.120720,-7.041292,-4.450807,3.340180,0.493933,-6.492603,5.478615,-1.717525,3.873445,-8.312758,-2.072302,9.720086,4.609729,5.149420,-7.594105,-3.522323,-3.711936,5.186808,-4.559708,0.617468,9.663478,9.963945,-6.095310,9.629696,-2.016218,-9.111190,1.242668,7.404233,-9.899457,-4.105690,0.599980,6.648898,-0.977408,-5.621155,-4.912360,-8.139307,1.671592,-3.456568,-9.949874,4.626836,1.869371,8.729284,8.159784,8.190424,6.708616,5.882016,-6.150107,-3.136750,1.488282,-2.487173,-6.376508,4.570206,-6.310600], dtype = "float32")#candidate|12407|(567,)|const|float32
call_12406 = func_11386_call(relay.reshape(const_12407.astype('float32'), [9, 9, 7]), relay.reshape(const_12407.astype('float32'), [9, 9, 7]), )
call_12408 = func_11386_call(relay.reshape(const_12407.astype('float32'), [9, 9, 7]), relay.reshape(const_12407.astype('float32'), [9, 9, 7]), )
func_8985_call = mod.get_global_var('func_8985')
func_8989_call = mutated_mod.get_global_var('func_8989')
const_12412 = relay.const([[0.326934,4.932912,5.967420,-4.772679,-0.950846,7.228634,6.594971,-5.547667,0.306102,-8.445170,9.574659,4.467627,7.298351,0.237649,1.943973,-5.820442,-1.251556,-8.370093,6.378712,-2.336092,0.541417,2.338728,2.472286,0.530587,-8.424365,3.551188,-2.345435,-4.012474,0.038428,2.032503,-2.398318,3.478847,4.310198,-5.563641,2.989021,5.288656,-7.703853,1.875447,-3.157443,-9.842975,5.269780,-7.128391,-6.339071,1.125989,-6.616230,-2.275100,-9.479371,0.072518,5.072855,-4.652321,3.165956,5.383342,-2.547755,8.070746,5.820478,-9.140689,-4.168294,-0.930309,1.156079,-1.017136,0.395987,-8.367524,7.307479,2.473039,6.802735,6.884948,7.806958,-9.054669,4.562221,-8.953075,5.803236,7.078212,8.173154,-2.616662,3.091786,-6.613392,8.105835,-6.649001,7.303275,6.277383,8.040192,9.965626,-2.591223,4.470214,1.188960,-5.431014,-9.648152,-5.571231,-7.524280,-6.837992,-9.131656,-7.197428,3.110564,-5.261617,-1.267824,2.727422,-7.893159,1.252754,-9.120734,-7.346563,-6.033578,-6.824366,6.412733,1.502726,3.545518,2.807394,-6.014605,6.662396]], dtype = "float64")#candidate|12412|(1, 108)|const|float64
const_12413 = relay.const([[-1,6,-9,-8,1,-1,-1,7,1,10,3,7,1,10,-9,-6,7,10,-10,-1,6,1,-1,7,10,-9,7,-4,-6,-2,7,3,2,2,-4,5],[4,-9,-2,-9,6,-9,2,3,10,-2,5,-10,1,-1,2,-4,1,3,10,8,-10,2,2,1,-3,8,-8,-7,10,-3,3,3,9,-7,-10,6],[4,3,3,8,6,-8,-6,-5,-2,-1,4,-8,1,-1,-2,10,-6,4,6,-7,-9,9,9,-4,-10,7,10,-6,-3,-2,5,3,-5,-1,10,-7],[3,6,10,5,6,4,7,7,-9,7,10,-5,10,8,-6,-10,-1,-4,-8,-10,1,2,-8,-10,-7,10,10,2,3,-9,-7,1,7,8,4,-2]], dtype = "int8")#candidate|12413|(4, 36)|const|int8
call_12411 = relay.TupleGetItem(func_8985_call(relay.reshape(const_12412.astype('float64'), [6, 3, 6]), relay.reshape(const_12413.astype('int8'), [144,]), ), 4)
call_12414 = relay.TupleGetItem(func_8989_call(relay.reshape(const_12412.astype('float64'), [6, 3, 6]), relay.reshape(const_12413.astype('int8'), [144,]), ), 4)
output = relay.Tuple([call_12388,call_12390,var_12391,call_12406,const_12407,call_12411,const_12412,const_12413,])
output2 = relay.Tuple([call_12389,call_12392,var_12391,call_12408,const_12407,call_12414,const_12412,const_12413,])
func_12415 = relay.Function([var_12391,], output)
mod['func_12415'] = func_12415
mod = relay.transform.InferType()(mod)
mutated_mod['func_12415'] = func_12415
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12416 = relay.var("var_12416", dtype = "float64", shape = (132,))#candidate|12416|(132,)|var|float64
func_12415_call = mutated_mod.get_global_var('func_12415')
call_12417 = func_12415_call(var_12416)
output = call_12417
func_12418 = relay.Function([var_12416], output)
mutated_mod['func_12418'] = func_12418
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12463 = relay.const([[[-2,-6,-9,-5,9,7,-6],[3,10,-9,-7,-6,8,3],[1,-4,4,-5,3,10,-8],[7,5,-6,-3,5,-4,3],[9,9,-6,2,-3,5,-10],[9,5,4,7,4,4,7],[10,-9,-4,10,1,1,8],[-9,4,-6,5,8,-1,9]],[[-2,3,-6,1,-1,1,-3],[-4,-10,-1,1,1,1,-8],[-2,8,-3,5,3,1,-7],[6,5,-4,2,-9,-3,9],[-2,6,3,-7,7,8,-10],[-6,1,8,1,-3,5,8],[-4,4,5,1,6,-8,2],[2,5,8,9,4,-7,-7]],[[-8,-4,3,2,2,7,3],[-10,1,8,2,-4,5,-5],[2,7,-6,-6,-1,-6,-2],[-10,10,4,5,-9,-2,-10],[-8,9,6,4,7,10,8],[2,10,-7,-5,4,-4,7],[-4,1,1,-4,6,-10,7],[4,7,-5,9,9,-4,-3]],[[4,4,-8,-9,-7,-7,-2],[7,-6,-7,6,-2,-6,10],[-4,8,-7,-5,1,4,-1],[-10,-8,4,-9,-7,-3,-1],[-9,-8,-8,-10,-1,7,-9],[2,2,4,-1,5,9,5],[10,8,-9,-2,-3,9,7],[7,-7,-7,1,10,-10,-1]],[[7,-9,-2,-8,-3,5,5],[3,-1,8,-9,8,6,3],[-3,3,2,8,-10,4,-7],[1,-4,3,-5,3,6,6],[-9,10,-5,9,6,1,4],[-1,-4,-4,-7,2,-8,7],[-6,7,-2,-7,-1,-4,6],[3,9,-2,8,-1,-2,8]],[[10,5,-8,1,-1,-9,-5],[-9,8,-8,8,10,-5,-3],[-4,9,6,-7,-8,6,-7],[2,-8,2,7,-3,-1,10],[-1,-4,-4,8,7,-4,-6],[-6,7,-6,3,1,7,2],[6,-5,-7,-4,2,-10,-9],[-5,7,9,-1,1,4,-1]]], dtype = "uint8")#candidate|12463|(6, 8, 7)|const|uint8
const_12464 = relay.const([[[-4,4,4,-5,-6,7,-5],[-9,2,-10,5,9,7,6],[-4,9,-7,9,4,-6,-10],[10,-9,-8,-6,8,-2,-5],[-6,10,-7,-2,-1,-6,5],[-7,-4,-2,-8,3,-9,-5],[5,1,-1,3,-9,2,8],[-4,1,-9,8,5,-4,-8]],[[-9,-3,3,6,-4,-3,6],[2,5,-8,-7,3,-10,9],[-7,4,-2,-10,10,10,-5],[-6,8,6,4,-2,-10,-4],[3,2,-2,10,5,10,4],[-9,3,-3,-3,-8,10,6],[7,10,-5,2,1,3,1],[-1,-3,5,6,-1,-6,6]],[[9,8,3,-5,-2,-4,-10],[9,10,6,2,3,1,1],[-3,3,-8,-9,9,-9,-3],[-4,-2,6,-4,-7,-6,-6],[-6,-4,3,-4,-6,-4,-9],[6,8,6,-2,3,-5,-2],[-3,-7,7,-2,7,-3,-9],[10,2,9,-3,-9,5,10]],[[-2,-10,3,6,9,10,3],[2,2,7,7,1,1,4],[-4,6,7,3,-7,7,6],[-3,1,-1,9,-7,6,-6],[-10,2,5,9,6,-9,2],[9,5,7,1,-1,7,-5],[-7,-9,1,2,9,-7,5],[10,-4,-5,4,9,1,-4]],[[-7,3,-1,-3,-4,-10,6],[2,3,-9,2,8,-6,-9],[-6,-7,-5,-8,-7,-9,-6],[5,-6,5,8,8,8,6],[-2,10,10,-2,-2,-1,3],[-1,1,-5,3,-8,-4,3],[-10,-5,-5,-2,-4,2,-7],[6,-7,1,3,6,-5,-10]],[[-9,-10,-3,-3,2,5,-10],[-4,4,-8,-7,10,6,5],[-10,-2,-8,-2,-9,-1,-10],[7,-7,-8,-2,-1,-5,8],[-7,-3,-10,6,9,-10,2],[-9,10,-6,-6,-6,-3,7],[8,-1,8,1,-1,7,6],[-8,9,-3,-3,3,-5,10]]], dtype = "uint8")#candidate|12464|(6, 8, 7)|const|uint8
bop_12465 = relay.bitwise_xor(const_12463.astype('uint8'), relay.reshape(const_12464.astype('uint8'), relay.shape_of(const_12463))) # shape=(6, 8, 7)
uop_12473 = relay.acosh(bop_12465.astype('float32')) # shape=(6, 8, 7)
func_11618_call = mod.get_global_var('func_11618')
func_11620_call = mutated_mod.get_global_var('func_11620')
call_12476 = relay.TupleGetItem(func_11618_call(), 0)
call_12477 = relay.TupleGetItem(func_11620_call(), 0)
output = relay.Tuple([uop_12473,call_12476,])
output2 = relay.Tuple([uop_12473,call_12477,])
func_12480 = relay.Function([], output)
mod['func_12480'] = func_12480
mod = relay.transform.InferType()(mod)
output = func_12480()
func_12481 = relay.Function([], output)
mutated_mod['func_12481'] = func_12481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1368_call = mod.get_global_var('func_1368')
func_1370_call = mutated_mod.get_global_var('func_1370')
call_12488 = func_1368_call()
call_12489 = func_1368_call()
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_12493 = relay.TupleGetItem(func_1864_call(), 4)
call_12494 = relay.TupleGetItem(func_1865_call(), 4)
output = relay.Tuple([call_12488,call_12493,])
output2 = relay.Tuple([call_12489,call_12494,])
func_12495 = relay.Function([], output)
mod['func_12495'] = func_12495
mod = relay.transform.InferType()(mod)
output = func_12495()
func_12496 = relay.Function([], output)
mutated_mod['func_12496'] = func_12496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8783_call = mod.get_global_var('func_8783')
func_8785_call = mutated_mod.get_global_var('func_8785')
call_12510 = relay.TupleGetItem(func_8783_call(), 2)
call_12511 = relay.TupleGetItem(func_8785_call(), 2)
output = call_12510
output2 = call_12511
func_12515 = relay.Function([], output)
mod['func_12515'] = func_12515
mod = relay.transform.InferType()(mod)
mutated_mod['func_12515'] = func_12515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12515_call = mutated_mod.get_global_var('func_12515')
call_12516 = func_12515_call()
output = call_12516
func_12517 = relay.Function([], output)
mutated_mod['func_12517'] = func_12517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_12577 = relay.TupleGetItem(func_2815_call(), 1)
call_12578 = relay.TupleGetItem(func_2816_call(), 1)
output = call_12577
output2 = call_12578
func_12589 = relay.Function([], output)
mod['func_12589'] = func_12589
mod = relay.transform.InferType()(mod)
mutated_mod['func_12589'] = func_12589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12589_call = mutated_mod.get_global_var('func_12589')
call_12590 = func_12589_call()
output = call_12590
func_12591 = relay.Function([], output)
mutated_mod['func_12591'] = func_12591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1449_call = mod.get_global_var('func_1449')
func_1451_call = mutated_mod.get_global_var('func_1451')
call_12635 = relay.TupleGetItem(func_1449_call(), 1)
call_12636 = relay.TupleGetItem(func_1451_call(), 1)
output = relay.Tuple([call_12635,])
output2 = relay.Tuple([call_12636,])
func_12649 = relay.Function([], output)
mod['func_12649'] = func_12649
mod = relay.transform.InferType()(mod)
output = func_12649()
func_12650 = relay.Function([], output)
mutated_mod['func_12650'] = func_12650
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12658 = relay.const([[[-8.399023,-0.130090,-8.287486,4.576749,6.097704,7.688110,7.351514,8.051148,4.057034,1.599043,3.429344,-8.502203,9.582155,3.885593,-3.493808]],[[-5.409822,-9.164206,-3.447925,3.110607,0.103439,2.458436,-0.837791,-8.499315,-6.546561,-4.686176,4.620352,2.980607,-8.065347,4.435763,8.421533]],[[-0.773338,8.236273,-1.962679,-2.017543,5.331335,1.307532,-1.499309,1.556718,3.848352,-5.662344,1.222304,5.177739,6.763744,-6.737437,-3.564926]],[[5.194578,2.612904,5.937178,-9.663569,7.381404,0.689346,-3.825775,8.301433,-6.999304,6.373803,-1.483022,6.061859,-0.999106,7.945112,1.724811]],[[-9.569957,9.945801,2.592452,-5.047797,-3.339901,6.362358,-4.003407,8.481663,-9.606616,-3.777071,7.296100,-0.449240,5.553266,8.555288,6.770075]],[[-9.828726,9.387220,1.595792,-6.653960,0.392898,-9.231312,-4.411019,-8.376678,-9.496638,-4.010452,2.718238,9.891858,-9.818868,-7.867950,7.758704]],[[-1.749748,4.530820,8.726978,0.860733,-2.575862,-5.203294,4.381585,1.683135,8.448503,-4.871747,3.506820,6.083464,-4.912632,5.054401,9.178484]],[[-0.645556,-8.031004,-2.208424,6.864859,0.283996,-4.938249,-9.297532,-3.120530,2.299998,3.796614,3.030758,9.934480,8.408988,-1.934463,-2.883937]],[[1.128410,-1.985388,4.534092,-7.458116,-7.689635,-9.504959,6.253288,-2.967116,6.223768,6.758015,-6.898554,0.844525,5.996369,5.226283,7.996092]],[[-5.105681,-1.212753,-2.382960,9.739090,-9.876462,-4.668072,-1.847460,5.497510,9.031730,-9.910702,8.148672,-0.873198,5.552582,9.812073,5.229786]],[[-2.847042,-4.115416,-4.271385,-9.765045,5.616840,2.460850,-9.652353,2.999008,4.059214,-9.686909,-8.857448,-4.732188,-8.110303,-8.114836,-4.473043]],[[-9.367774,5.676540,4.237460,8.656194,3.471957,7.907254,-2.901697,-6.557370,5.696635,-6.061320,-7.234653,-6.733918,2.536293,-3.727712,-5.833097]],[[-8.916501,5.980223,9.040430,1.722335,8.319215,0.984370,-1.224981,-3.837454,-8.673889,-6.511117,2.346717,1.114177,3.494380,-5.733423,-7.603606]],[[-8.261933,2.783460,0.730268,-9.633860,3.912780,7.382270,-4.934154,-3.128124,6.862338,2.941927,9.290139,-9.501809,-8.722222,-1.004542,7.087152]],[[9.054962,6.510251,6.229134,-0.218253,1.428756,8.750281,-7.834338,-7.238588,-3.441707,5.093209,4.292427,-3.769093,1.379513,4.725900,9.687462]]], dtype = "float32")#candidate|12658|(15, 1, 15)|const|float32
uop_12659 = relay.tan(const_12658.astype('float32')) # shape=(15, 1, 15)
bop_12662 = relay.greater(const_12658.astype('bool'), relay.reshape(uop_12659.astype('bool'), relay.shape_of(const_12658))) # shape=(15, 1, 15)
bop_12666 = relay.bitwise_xor(const_12658.astype('uint32'), relay.reshape(bop_12662.astype('uint32'), relay.shape_of(const_12658))) # shape=(15, 1, 15)
uop_12674 = relay.cos(uop_12659.astype('float64')) # shape=(15, 1, 15)
output = relay.Tuple([bop_12666,uop_12674,])
output2 = relay.Tuple([bop_12666,uop_12674,])
F = relay.Function([], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([], output2)
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
