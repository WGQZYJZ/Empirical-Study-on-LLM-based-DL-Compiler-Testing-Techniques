import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_256 = relay.var("var_256", dtype = "uint16", shape = (5, 6, 6))#candidate|256|(5, 6, 6)|var|uint16
const_257 = relay.const([[[-9,-2,10,3,-9,-10],[8,3,1,-7,-3,3],[-10,9,-7,4,3,-1],[1,6,-4,6,10,-4],[-9,5,2,1,-8,5],[-3,3,3,10,7,8]],[[4,5,-3,4,-2,6],[-10,-5,9,2,-9,9],[-9,9,-7,-1,-1,3],[-5,-6,10,10,-10,6],[7,1,-3,1,9,1],[-7,5,7,3,-6,1]],[[-2,-6,8,-2,-2,-4],[-1,-8,-4,-6,-9,10],[8,-2,-2,-2,3,-9],[-2,9,-3,-8,9,5],[-4,2,-2,1,-6,8],[-5,-6,-10,3,-3,-3]],[[-7,-1,6,-10,10,4],[-6,4,8,-2,2,-3],[-1,2,1,2,-6,-6],[2,-1,-8,2,9,-6],[8,10,-3,10,-1,10],[10,2,7,-8,-2,9]],[[5,-3,-9,-3,-6,7],[-8,-3,-1,-1,-7,9],[-10,10,10,-3,-1,1],[-7,7,7,-1,2,4],[-9,6,-9,-9,-6,1],[8,-10,2,9,6,-3]]], dtype = "uint16")#candidate|257|(5, 6, 6)|const|uint16
bop_258 = relay.right_shift(var_256.astype('uint16'), relay.reshape(const_257.astype('uint16'), relay.shape_of(var_256))) # shape=(5, 6, 6)
output = relay.Tuple([bop_258,])
output2 = relay.Tuple([bop_258,])
func_261 = relay.Function([var_256,], output)
mod['func_261'] = func_261
mod = relay.transform.InferType()(mod)
var_262 = relay.var("var_262", dtype = "uint16", shape = (5, 6, 6))#candidate|262|(5, 6, 6)|var|uint16
output = func_261(var_262)
func_263 = relay.Function([var_262], output)
mutated_mod['func_263'] = func_263
mutated_mod = relay.transform.InferType()(mutated_mod)
var_529 = relay.var("var_529", dtype = "float32", shape = (16, 12, 6))#candidate|529|(16, 12, 6)|var|float32
uop_530 = relay.sin(var_529.astype('float32')) # shape=(16, 12, 6)
bop_539 = relay.minimum(uop_530.astype('int32'), relay.reshape(var_529.astype('int32'), relay.shape_of(uop_530))) # shape=(16, 12, 6)
uop_543 = relay.acos(bop_539.astype('float32')) # shape=(16, 12, 6)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
var_555 = relay.var("var_555", dtype = "uint16", shape = (180,))#candidate|555|(180,)|var|uint16
call_554 = relay.TupleGetItem(func_261_call(relay.reshape(var_555.astype('uint16'), [5, 6, 6])), 0)
call_556 = relay.TupleGetItem(func_263_call(relay.reshape(var_555.astype('uint16'), [5, 6, 6])), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_567 = relay.TupleGetItem(func_261_call(relay.reshape(call_554.astype('uint16'), [5, 6, 6])), 0)
call_568 = relay.TupleGetItem(func_263_call(relay.reshape(call_554.astype('uint16'), [5, 6, 6])), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_576 = relay.TupleGetItem(func_261_call(relay.reshape(call_554.astype('uint16'), [5, 6, 6])), 0)
call_577 = relay.TupleGetItem(func_263_call(relay.reshape(call_554.astype('uint16'), [5, 6, 6])), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_586 = relay.TupleGetItem(func_261_call(relay.reshape(call_576.astype('uint16'), [5, 6, 6])), 0)
call_587 = relay.TupleGetItem(func_263_call(relay.reshape(call_576.astype('uint16'), [5, 6, 6])), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_590 = relay.TupleGetItem(func_261_call(relay.reshape(call_554.astype('uint16'), [5, 6, 6])), 0)
call_591 = relay.TupleGetItem(func_263_call(relay.reshape(call_554.astype('uint16'), [5, 6, 6])), 0)
bop_594 = relay.bitwise_and(bop_539.astype('uint32'), relay.reshape(uop_543.astype('uint32'), relay.shape_of(bop_539))) # shape=(16, 12, 6)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_598 = relay.TupleGetItem(func_261_call(relay.reshape(call_576.astype('uint16'), [5, 6, 6])), 0)
call_599 = relay.TupleGetItem(func_263_call(relay.reshape(call_576.astype('uint16'), [5, 6, 6])), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_601 = relay.TupleGetItem(func_261_call(relay.reshape(call_590.astype('uint16'), [5, 6, 6])), 0)
call_602 = relay.TupleGetItem(func_263_call(relay.reshape(call_590.astype('uint16'), [5, 6, 6])), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_604 = relay.TupleGetItem(func_261_call(relay.reshape(call_554.astype('uint16'), [5, 6, 6])), 0)
call_605 = relay.TupleGetItem(func_263_call(relay.reshape(call_554.astype('uint16'), [5, 6, 6])), 0)
bop_612 = relay.logical_and(bop_539.astype('bool'), relay.reshape(var_529.astype('bool'), relay.shape_of(bop_539))) # shape=(16, 12, 6)
uop_620 = relay.cosh(uop_543.astype('float64')) # shape=(16, 12, 6)
var_623 = relay.var("var_623", dtype = "uint16", shape = (5, 6, 6))#candidate|623|(5, 6, 6)|var|uint16
bop_624 = relay.power(call_567.astype('float32'), relay.reshape(var_623.astype('float32'), relay.shape_of(call_567))) # shape=(5, 6, 6)
bop_627 = relay.power(call_568.astype('float32'), relay.reshape(var_623.astype('float32'), relay.shape_of(call_568))) # shape=(5, 6, 6)
output = relay.Tuple([call_554,var_555,call_576,call_586,call_590,bop_594,call_598,call_601,call_604,bop_612,uop_620,bop_624,])
output2 = relay.Tuple([call_556,var_555,call_577,call_587,call_591,bop_594,call_599,call_602,call_605,bop_612,uop_620,bop_627,])
func_631 = relay.Function([var_529,var_555,var_623,], output)
mod['func_631'] = func_631
mod = relay.transform.InferType()(mod)
mutated_mod['func_631'] = func_631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_631_call = mutated_mod.get_global_var('func_631')
var_633 = relay.var("var_633", dtype = "float32", shape = (16, 12, 6))#candidate|633|(16, 12, 6)|var|float32
var_634 = relay.var("var_634", dtype = "uint16", shape = (180,))#candidate|634|(180,)|var|uint16
var_635 = relay.var("var_635", dtype = "uint16", shape = (5, 6, 6))#candidate|635|(5, 6, 6)|var|uint16
call_632 = func_631_call(var_633,var_634,var_635,)
output = call_632
func_636 = relay.Function([var_633,var_634,var_635,], output)
mutated_mod['func_636'] = func_636
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1066 = relay.var("var_1066", dtype = "bool", shape = ())#candidate|1066|()|var|bool
var_1067 = relay.var("var_1067", dtype = "bool", shape = (12, 9, 13))#candidate|1067|(12, 9, 13)|var|bool
bop_1068 = relay.logical_and(var_1066.astype('bool'), var_1067.astype('bool')) # shape=(12, 9, 13)
output = relay.Tuple([bop_1068,])
output2 = relay.Tuple([bop_1068,])
func_1079 = relay.Function([var_1066,var_1067,], output)
mod['func_1079'] = func_1079
mod = relay.transform.InferType()(mod)
mutated_mod['func_1079'] = func_1079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1079_call = mutated_mod.get_global_var('func_1079')
var_1081 = relay.var("var_1081", dtype = "bool", shape = ())#candidate|1081|()|var|bool
var_1082 = relay.var("var_1082", dtype = "bool", shape = (12, 9, 13))#candidate|1082|(12, 9, 13)|var|bool
call_1080 = func_1079_call(var_1081,var_1082,)
output = call_1080
func_1083 = relay.Function([var_1081,var_1082,], output)
mutated_mod['func_1083'] = func_1083
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1102 = relay.const([[[8.293094,0.021859,-3.201229,2.632949,0.199012,-0.971723,-0.069975,-1.224214,1.885903,9.574167,4.633204,8.711285,-5.648164,-3.324393,3.947689]],[[-8.729675,3.990535,-1.004471,-1.337810,9.699382,9.328945,-1.277181,7.101041,4.455734,5.501730,-8.004585,-9.549588,2.989296,-4.038476,-8.586048]],[[5.094481,4.749390,-6.437104,-9.924513,7.503597,6.838276,8.409146,6.481483,-6.993724,-9.544594,0.918211,6.104204,-7.330943,-0.507629,-4.758169]],[[1.458362,-7.372740,-3.012121,-4.610141,5.643592,6.590759,2.958493,-0.374899,4.327199,3.750171,-5.927027,0.861191,-4.294520,-4.922071,-1.971205]],[[1.948372,4.925245,-1.649054,-6.089374,-0.367858,5.076133,-7.259905,3.981609,4.274254,-9.313512,-6.155513,6.339214,-7.456086,8.981521,6.681019]],[[8.957637,7.385688,-1.893877,9.992717,8.563345,-0.840090,3.090597,3.698572,2.293578,3.076863,6.830804,-8.143188,0.244299,-6.884337,1.249342]],[[9.159358,-2.361105,6.079520,-5.438147,7.927244,2.538785,-6.217035,5.908095,3.610639,-6.941851,-3.289899,-7.730167,6.010676,8.473408,-8.306592]],[[8.869154,4.211333,9.765021,-7.356965,7.445339,8.374090,4.249071,6.757170,7.080531,0.451349,-5.942366,2.866208,-8.258103,-3.571428,-9.552899]],[[-5.888440,-9.375972,0.554329,6.515521,-9.068164,9.541558,3.360076,7.360275,5.899863,1.326313,1.507739,-0.902877,-1.812055,5.410931,-1.963404]]], dtype = "float32")#candidate|1102|(9, 1, 15)|const|float32
var_1103 = relay.var("var_1103", dtype = "float32", shape = (9, 1, 15))#candidate|1103|(9, 1, 15)|var|float32
bop_1104 = relay.minimum(const_1102.astype('float32'), relay.reshape(var_1103.astype('float32'), relay.shape_of(const_1102))) # shape=(9, 1, 15)
func_631_call = mod.get_global_var('func_631')
func_636_call = mutated_mod.get_global_var('func_636')
var_1113 = relay.var("var_1113", dtype = "float32", shape = (1152,))#candidate|1113|(1152,)|var|float32
var_1114 = relay.var("var_1114", dtype = "uint16", shape = (180, 1))#candidate|1114|(180, 1)|var|uint16
call_1112 = relay.TupleGetItem(func_631_call(relay.reshape(var_1113.astype('float32'), [16, 12, 6]), relay.reshape(var_1114.astype('uint16'), [180,]), relay.reshape(var_1114.astype('uint16'), [5, 6, 6]), ), 7)
call_1115 = relay.TupleGetItem(func_636_call(relay.reshape(var_1113.astype('float32'), [16, 12, 6]), relay.reshape(var_1114.astype('uint16'), [180,]), relay.reshape(var_1114.astype('uint16'), [5, 6, 6]), ), 7)
output = relay.Tuple([bop_1104,call_1112,var_1113,var_1114,])
output2 = relay.Tuple([bop_1104,call_1115,var_1113,var_1114,])
func_1120 = relay.Function([var_1103,var_1113,var_1114,], output)
mod['func_1120'] = func_1120
mod = relay.transform.InferType()(mod)
mutated_mod['func_1120'] = func_1120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mutated_mod.get_global_var('func_1120')
var_1122 = relay.var("var_1122", dtype = "float32", shape = (9, 1, 15))#candidate|1122|(9, 1, 15)|var|float32
var_1123 = relay.var("var_1123", dtype = "float32", shape = (1152,))#candidate|1123|(1152,)|var|float32
var_1124 = relay.var("var_1124", dtype = "uint16", shape = (180, 1))#candidate|1124|(180, 1)|var|uint16
call_1121 = func_1120_call(var_1122,var_1123,var_1124,)
output = call_1121
func_1125 = relay.Function([var_1122,var_1123,var_1124,], output)
mutated_mod['func_1125'] = func_1125
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1200 = relay.var("var_1200", dtype = "float32", shape = (2, 13, 11))#candidate|1200|(2, 13, 11)|var|float32
uop_1201 = relay.tan(var_1200.astype('float32')) # shape=(2, 13, 11)
func_1120_call = mod.get_global_var('func_1120')
func_1125_call = mutated_mod.get_global_var('func_1125')
const_1218 = relay.const([-2.346665,9.471949,9.086510,-8.771166,1.419376,4.275144,7.131749,4.553406,-1.085600,-9.065533,-9.182932,-7.148412,6.270894,4.619131,-7.267039,8.611663,8.289798,-0.046844,-6.522887,-7.367595,5.334068,1.114463,7.442359,8.520428,0.760496,-1.334174,5.742479,-6.006591,-1.444562,-4.356731,9.908161,1.421070,-1.839813,6.475018,-1.758299,2.703607,9.009923,1.357582,4.640435,-5.165712,-1.039232,9.854772,0.872803,4.838722,4.029731,-4.055233,2.615640,8.941879,-1.888078,0.853299,-9.555962,-3.308568,9.820538,9.784768,-8.492166,-2.572112,-7.361161,0.425473,1.496765,1.575549,-5.045948,6.725952,-4.775933,6.875632,5.906531,4.258604,1.724891,3.045921,0.365346,-1.589653,0.397776,7.931893,-8.446243,6.393975,5.772586,-1.678337,2.406627,8.257275,-3.055998,-8.664401,1.714702,-7.648302,2.264289,-4.749639,-5.216537,-5.197583,4.713137,9.164643,-2.465806,6.311441,-4.853735,9.194826,-1.542725,2.640830,-6.886752,-6.696302,1.833087,-2.420009,4.172488,-7.546068,6.483383,5.579743,-5.577868,-6.614916,3.153702,-0.264790,6.318184,1.490766,-9.891585,8.797439,-4.026680,7.071234,-0.140367,-5.451135,-7.935598,5.271405,-6.871862,-7.079575,7.289663,7.760637,-3.298528,-3.772257,-3.667996,4.103996,-8.518952,4.547036,6.394181,1.124346,-2.585207,5.563532,-3.880608,5.702262,1.376306,1.445731,-2.787173], dtype = "float32")#candidate|1218|(135,)|const|float32
const_1219 = relay.const([[-3.102369,1.755669],[9.378361,3.721033],[2.329227,-4.918088],[6.160614,-4.595332],[-5.356959,-1.227299],[7.405163,-5.069245],[-6.482217,7.179651],[-9.592500,2.582426],[7.129803,9.317485],[7.260583,1.978056],[0.342270,9.208638],[1.802104,-0.576717],[9.744005,0.133745],[-4.631787,-9.789781],[-9.672858,5.795757],[-7.584344,5.143875],[-1.158786,-8.415768],[3.075626,-1.603018],[5.316491,7.214869],[-5.621202,-7.603705],[-5.618872,-5.077374],[-6.062089,-0.977745],[-0.966899,9.878144],[-9.883201,7.441355],[3.647750,4.588552],[1.619613,-3.557474],[6.401641,-9.220644],[7.858503,0.701155],[-2.236512,1.667212],[-7.675870,6.711527],[9.626498,-2.198526],[7.523967,-1.427324],[3.635483,-7.709120],[-0.407642,-6.582472],[-1.693498,1.762003],[1.167119,-3.744698],[-5.005522,-8.384246],[0.310796,-1.740818],[-7.805927,-1.984203],[-4.421755,3.646919],[-3.225592,-1.176319],[-8.899886,-3.606327],[6.254628,-4.757927],[-5.022168,2.024494],[-5.026195,-5.157890],[3.046808,6.521271],[7.847927,-0.967970],[-7.547877,1.760770],[9.168621,8.365142],[-3.091505,-1.774919],[3.288296,3.782170],[3.468554,0.949689],[-8.459606,6.850236],[-8.875692,-0.416858],[2.171178,8.159480],[-9.938770,-0.810680],[-8.192846,6.509777],[-0.032968,5.573855],[-7.351758,2.488157],[3.311687,-3.533173],[-6.891381,9.245781],[-0.405595,-1.401192],[-7.578874,7.954213],[6.373137,-8.376686],[-9.475023,-7.041138],[-7.816118,-8.910409],[-3.265189,-2.170304],[-8.987066,-6.117075],[7.794833,2.493895],[1.412151,3.609084],[4.999056,-9.614809],[-6.829573,1.525614],[-7.336026,2.303248],[6.268609,9.517628],[-4.445792,1.359562],[-7.570517,2.930064],[7.830772,7.979048],[6.699092,8.889997],[-2.468325,8.701206],[-1.163075,0.932111],[-0.678245,0.837533],[-9.924955,-1.848771],[9.731850,-2.885989],[4.509028,3.792664],[-0.381667,1.187055],[8.218440,8.467363],[-7.258215,-5.727225],[5.866543,7.236077],[4.226984,9.755313],[4.147048,-8.726534],[6.674185,2.224803],[-5.734621,2.452287],[4.929791,-5.362132],[6.013578,-3.716648],[-3.655924,7.484781],[-4.268959,-3.144495],[2.447897,-8.119607],[5.141966,4.318583],[4.738336,4.497621],[1.342750,-9.704333],[2.766874,9.149331],[-5.132083,-7.759918],[3.771051,-7.588512],[-2.382806,6.656835],[-7.302103,-9.543446],[-6.080806,-5.510535],[-8.584278,7.942442],[6.753924,7.476924],[0.262498,5.626067],[-7.747449,-3.819744],[6.284429,-2.391073],[9.341205,-1.526574],[5.424338,2.275711],[-2.013740,8.218154],[7.290344,2.923120],[-0.143328,7.662630],[0.855526,-7.987013],[-8.047368,0.819661],[0.869186,9.561363],[0.809419,4.134628],[6.590265,-6.069690],[-7.051083,-2.149891],[7.636501,-4.193601],[-8.468164,8.082031],[4.151832,-8.083306],[-0.428727,4.915965],[4.068403,5.734402],[-1.760578,8.920712],[5.712390,-6.316915],[1.611969,-7.469573],[-5.775541,-3.135764],[-6.724702,-3.764356],[1.628279,-1.640735],[8.608112,-7.754316],[-7.825513,3.922894],[-4.688371,-6.730488],[8.754673,3.179473],[-1.793014,2.183188],[0.486958,7.936729],[8.531014,8.221232],[-5.558241,-7.693611],[8.377318,-0.899067],[-5.227152,7.288932],[-4.719879,2.881151],[-8.787782,-9.868539],[-9.843668,1.214191],[-2.420326,4.016639],[-3.063101,-0.262486],[-7.936961,-5.597287],[5.204135,-3.549187],[9.845038,-0.495627],[0.040311,6.551036],[4.663066,-2.354833],[0.309397,4.786356],[4.137042,1.302820],[4.776825,-5.578203],[-1.597349,2.680492],[-2.242887,-7.678451],[7.093619,6.270543],[-4.369649,-4.275382],[4.190794,0.142887],[-7.351529,-4.590053],[0.586775,-6.095337],[3.086520,5.825705],[9.119158,-8.677520],[-8.467085,3.842536],[1.290576,-2.482728],[5.548340,2.179306],[-7.522154,0.821348],[8.314349,-0.931734],[4.166903,7.333070],[2.211947,2.138117],[-3.333392,-6.174108],[-0.525909,-1.553313],[4.960004,8.888819],[-6.870083,7.746878],[8.488021,9.217491],[-5.510388,1.121177],[-4.245160,-8.633304],[7.149555,2.450421],[2.981782,-0.247667],[8.197728,-2.941922],[-8.958126,-5.376251],[-3.525725,0.974344],[-8.245020,8.259918],[-1.152327,1.352851],[6.403287,-0.609125],[0.264983,-0.336358],[-5.316608,-3.080879],[-2.398439,-4.514166],[-0.438707,8.639245],[-6.045100,-0.396097],[2.914221,4.815855],[-6.346281,3.855866],[-3.319510,1.577766],[0.190126,5.036721],[-7.985734,5.270384],[-4.168633,9.724576],[-5.651484,5.499317],[1.078115,-6.914040],[2.724976,-9.764282],[-7.189903,-8.130787],[-3.014679,-5.918126],[1.686367,9.278500],[8.038177,-7.345193],[-2.824909,-5.217683],[-3.532237,9.088038],[9.565834,5.958546],[7.539265,-8.886536],[7.657973,-5.891407],[-4.357356,1.861313],[-2.941081,-5.703687],[5.569039,8.672539],[-4.537173,7.602296],[-8.619897,0.503211],[-5.703259,-5.564078],[-3.538085,5.441348],[6.272236,8.529404],[-2.711514,-6.923339],[3.952173,-5.325816],[5.711724,-3.904478],[5.878579,6.812645],[-3.851521,4.942127],[2.790385,-8.973100],[-5.022490,6.745037],[-3.151009,-6.399411],[8.078623,1.477285],[8.031038,6.752284],[-6.865321,-8.977111],[9.912108,9.006554],[-0.168574,-5.619676],[-2.981203,-7.983351],[-9.745421,6.568542],[-6.703421,5.888796],[-4.416795,7.519018],[-8.291325,-7.609580],[-3.160490,-2.397773],[-9.953840,-3.251873],[-1.958475,-9.482161],[9.031915,-6.647102],[-8.388046,-4.411979],[7.434723,-9.454029],[3.275861,3.308834],[6.242382,-0.579633],[-6.401972,3.590043],[-9.432410,-6.348464],[9.823689,5.695278],[2.963503,-3.063263],[1.274080,-7.766362],[2.302113,-3.807621],[-0.333483,-1.850531],[-7.162225,-0.290609],[-4.881718,6.918993],[3.611199,0.718897],[6.913474,3.654925],[-5.746781,-2.388255],[4.476231,-6.859348],[-0.745026,2.828720],[-7.542953,-1.466565],[-4.327377,-5.137228],[-9.460734,9.802983],[0.275546,-8.656934],[8.767766,9.142778],[-1.566453,-3.482470],[-0.858287,-9.156771],[3.529281,-3.837421],[0.480061,-1.335258],[3.403649,-0.561039],[7.742674,1.942924],[1.642532,9.136911],[9.336187,-6.863667],[-2.247473,3.063356],[-0.173884,7.583941],[1.778625,4.911461],[-0.690683,-2.278426],[-5.811819,-3.454180],[-6.467103,-0.251128],[0.487463,3.590450],[-4.329406,-4.329134],[-2.944548,-8.638140],[1.628537,-0.752970],[5.508263,-4.321822],[-5.001885,8.540380],[8.611173,-5.274799],[5.135022,4.433658],[-8.399049,7.064530],[1.391446,3.871912],[-7.508854,-6.721724],[-9.977258,-7.012703],[-3.365664,4.089506],[-1.214861,-2.793843],[-5.430805,4.680013],[8.429001,5.113472],[8.959349,1.590464],[-1.379882,-6.964190],[-8.822913,8.376010],[-7.993629,-6.975751],[-8.190052,2.556370],[-0.538989,-5.873743],[-0.129276,-0.164139],[2.036880,8.338252],[-1.242354,8.051909],[6.880843,6.776603],[-2.743418,-8.731049],[4.353887,9.287503],[4.987901,-1.491667],[-8.090645,-8.651260],[-2.344047,8.178102],[-3.522524,0.675440],[7.643655,-3.588561],[-2.988589,-3.475305],[-1.813089,5.147422],[7.126646,7.306425],[5.872159,-5.794585],[-1.502538,-0.908119],[4.156310,-2.906798],[-4.043456,-7.024158],[-1.802620,7.188610],[1.041614,9.794861],[-4.788110,8.706645],[-8.059814,-6.163874],[-2.632576,0.199256],[-4.848090,4.986776],[8.155346,2.606314],[8.371467,9.917594],[-4.114437,7.289883],[-4.053405,6.654899],[5.765524,-7.187689],[2.355562,-5.158018],[5.735388,6.712877],[7.073944,8.438495],[-7.951765,9.193287],[3.528482,-7.207400],[8.608128,7.853391],[-4.835824,-4.700321],[4.876418,1.700245],[-3.363236,-8.947049],[-4.793689,5.295355],[-7.443476,-8.831137],[7.884696,0.299364],[1.739468,8.221673],[5.219992,-0.461468],[4.669671,0.283308],[-4.068980,-8.053857],[-1.331367,-1.034920],[-7.379992,8.424948],[3.171257,8.511153],[9.859546,8.372167],[-2.222841,4.172193],[5.483441,-2.878422],[-8.837368,4.058213],[-1.627062,1.910945],[-7.027621,6.463723],[5.029733,4.536657],[2.916870,-6.632567],[6.021486,6.177194],[-3.423780,4.672594],[-7.052573,-6.020158],[-9.647757,5.145354],[6.114559,9.644209],[6.608197,-8.830514],[0.961340,0.123119],[3.015327,3.644379],[8.896262,-6.396104],[3.330314,2.020604],[8.494608,4.405044],[2.587094,1.691329],[2.703851,-4.067266],[2.475133,-0.221573],[-6.234772,5.963106],[4.346690,3.924278],[7.741207,-3.333413],[6.165137,2.900581],[9.201204,-9.104753],[1.723724,-5.779579],[5.044036,0.665184],[6.232292,3.886128],[7.762824,8.759067],[-0.127234,5.536300],[3.121438,-6.213451],[8.215225,7.227619],[-1.531701,1.821186],[3.405900,1.189874],[-2.586265,-9.838436],[-7.244965,-3.678487],[-9.142178,-7.327241],[-2.997976,1.862663],[0.722377,-1.384526],[4.000326,9.197040],[-8.782942,5.297936],[-8.370473,-9.893321],[-6.623165,4.255677],[-9.795626,-8.158871],[9.016327,5.729846],[9.489815,9.016571],[1.817189,3.141417],[-9.493260,-9.473180],[-0.870772,-3.723472],[-2.917512,8.819843],[5.007560,5.201524],[-2.726000,8.367758],[-5.085871,8.037590],[7.929429,-4.071169],[8.349742,2.591911],[1.126591,-9.625917],[0.404196,-1.383642],[4.743718,-0.481060],[-7.579323,-1.518756],[-5.728620,0.035762],[2.714069,-1.329047],[2.932027,1.955007],[-4.050068,-8.917265],[-6.535573,1.475485],[-3.709173,-4.722049],[-5.298095,-4.871298],[-2.726966,1.545852],[-4.472981,-3.068414],[-7.316556,-0.392014],[8.934417,-9.075848],[-6.857549,2.015259],[0.402429,4.941243],[1.645788,4.774722],[-0.874681,-8.974430],[-1.024480,9.163022],[-9.849791,-2.011073],[-2.168371,9.908014],[-4.315716,-5.650367],[-6.817955,-6.911119],[-8.175319,7.702857],[5.097249,2.921198],[5.390485,-3.249424],[-6.451677,-5.695980],[0.196934,5.646012],[-4.718116,-6.996382],[-2.746862,9.154589],[-6.820949,-5.227556],[0.421413,-0.684143],[-9.139976,0.821049],[-0.178736,4.815665],[2.516590,3.341470],[2.107498,8.171821],[1.363745,-9.298084],[-3.581830,3.186628],[1.023903,3.733836],[1.207488,9.401690],[-9.428513,3.530468],[5.504897,8.787697],[9.396184,7.225597],[5.163241,-4.193635],[-0.646994,-3.578050],[-2.394567,-5.320838],[0.371843,0.779430],[4.253027,-4.289507],[3.585936,-0.657003],[-7.781539,1.574260],[4.088432,-6.403055],[3.462329,8.164570],[-7.194633,-8.211218],[2.157452,-4.659510],[8.667914,-0.023875],[4.790922,-5.887475],[-2.955720,0.211624],[-1.376575,-7.963473],[3.866929,-7.129481],[2.682572,2.179114],[6.699701,5.677319],[-8.704497,0.582528],[6.928988,-5.453962],[-2.194196,1.865718],[-8.401515,8.550677],[6.764690,-5.437588],[5.550661,-9.350594],[-0.992672,-6.887040],[8.530285,5.019490],[0.900894,2.035215],[-0.562919,2.108010],[-5.855147,0.032050],[6.599849,0.829165],[8.419303,-8.790348],[-4.741636,6.891445],[-7.085268,-6.810711],[8.101835,7.072107],[-2.765363,4.563688],[-2.088571,1.019637],[4.759220,2.932068],[-8.287675,-8.403437],[-8.495272,-4.134202],[6.220478,-6.303764],[8.285514,0.018767],[-1.530674,0.603024],[-9.911655,7.591421],[-3.541928,8.469288],[6.170956,-4.444330],[-7.016678,2.424553],[4.420619,5.515091],[-3.980274,-4.799089],[0.634988,-0.548056],[-3.635785,-3.293513],[1.293355,-3.712667],[1.027435,5.942148],[-9.575034,-3.563078],[-5.238058,-8.171798],[2.121446,-0.735624],[6.701240,2.412799],[3.596605,-2.303119],[2.678656,-7.855201],[-5.773946,-5.807560],[-7.576676,-6.381768],[-3.699052,7.387500],[3.293033,-4.166393],[-5.036811,-2.994758],[-8.514906,-1.743565],[8.448255,0.323238],[8.695640,7.628132],[-8.702969,7.585390],[-4.886571,-6.227307],[-6.028234,9.685213],[3.747215,-4.629994],[6.756424,3.423939],[-7.833811,1.273067],[-5.342193,7.950841],[-4.529991,1.102464],[-1.399745,7.523019],[-5.232410,1.060885],[-8.637119,-4.802753],[7.770270,6.174328],[7.017405,-0.400141],[-1.431204,-1.113209],[-7.224814,-9.325086],[-6.235186,-8.611056],[4.166617,8.972846],[2.203546,-3.866273],[-2.675677,0.660507],[-2.445673,-4.577791],[0.533172,0.373601],[-7.707377,-8.087388],[5.475972,3.846879],[-5.045462,0.873523],[7.837702,7.087966],[0.593207,-6.543176],[9.898750,3.860041],[-6.166981,9.006126],[-1.698239,6.001904],[-2.357004,-3.767422],[2.102653,-3.427667],[7.328687,7.580129],[-6.343790,4.559188],[-7.365127,5.374113],[8.453477,6.333856],[-9.228895,3.602097],[-6.793973,3.483726],[-9.880714,-9.864578],[6.580216,9.319133],[-0.910025,-5.384515],[8.056862,7.006751],[8.977087,7.162664],[6.456113,4.746523],[-1.851135,2.931907],[5.132911,9.705590],[-6.726662,9.179206],[-9.250291,-2.265910],[7.385284,-7.668586],[-1.203157,6.241843],[-9.926814,-6.451575],[9.544926,-8.053320],[-9.634098,-8.511472],[-9.498262,0.848060],[-1.082339,5.442896],[5.408305,5.995892],[-4.031212,5.685635],[0.821611,-1.932792],[-4.505848,-1.078919],[-7.728491,5.694495],[-2.083191,8.093533],[9.074878,9.851359],[9.439165,1.390262]], dtype = "float32")#candidate|1219|(576, 2)|const|float32
var_1220 = relay.var("var_1220", dtype = "uint16", shape = (180,))#candidate|1220|(180,)|var|uint16
call_1217 = relay.TupleGetItem(func_1120_call(relay.reshape(const_1218.astype('float32'), [9, 1, 15]), relay.reshape(const_1219.astype('float32'), [1152,]), relay.reshape(var_1220.astype('uint16'), [180, 1]), ), 3)
call_1221 = relay.TupleGetItem(func_1125_call(relay.reshape(const_1218.astype('float32'), [9, 1, 15]), relay.reshape(const_1219.astype('float32'), [1152,]), relay.reshape(var_1220.astype('uint16'), [180, 1]), ), 3)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_1228 = relay.TupleGetItem(func_261_call(relay.reshape(var_1220.astype('uint16'), [5, 6, 6])), 0)
call_1229 = relay.TupleGetItem(func_263_call(relay.reshape(var_1220.astype('uint16'), [5, 6, 6])), 0)
func_631_call = mod.get_global_var('func_631')
func_636_call = mutated_mod.get_global_var('func_636')
call_1232 = relay.TupleGetItem(func_631_call(relay.reshape(const_1219.astype('float32'), [16, 12, 6]), relay.reshape(var_1220.astype('uint16'), [180,]), relay.reshape(call_1217.astype('uint16'), [5, 6, 6]), ), 5)
call_1233 = relay.TupleGetItem(func_636_call(relay.reshape(const_1219.astype('float32'), [16, 12, 6]), relay.reshape(var_1220.astype('uint16'), [180,]), relay.reshape(call_1217.astype('uint16'), [5, 6, 6]), ), 5)
func_1079_call = mod.get_global_var('func_1079')
func_1083_call = mutated_mod.get_global_var('func_1083')
var_1243 = relay.var("var_1243", dtype = "bool", shape = ())#candidate|1243|()|var|bool
const_1244 = relay.const([False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True], dtype = "bool")#candidate|1244|(1404,)|const|bool
call_1242 = relay.TupleGetItem(func_1079_call(relay.reshape(var_1243.astype('bool'), []), relay.reshape(const_1244.astype('bool'), [12, 9, 13]), ), 0)
call_1245 = relay.TupleGetItem(func_1083_call(relay.reshape(var_1243.astype('bool'), []), relay.reshape(const_1244.astype('bool'), [12, 9, 13]), ), 0)
var_1255 = relay.var("var_1255", dtype = "bool", shape = (12, 9, 13))#candidate|1255|(12, 9, 13)|var|bool
bop_1256 = relay.right_shift(call_1242.astype('uint32'), relay.reshape(var_1255.astype('uint32'), relay.shape_of(call_1242))) # shape=(12, 9, 13)
bop_1259 = relay.right_shift(call_1245.astype('uint32'), relay.reshape(var_1255.astype('uint32'), relay.shape_of(call_1245))) # shape=(12, 9, 13)
func_1079_call = mod.get_global_var('func_1079')
func_1083_call = mutated_mod.get_global_var('func_1083')
call_1261 = relay.TupleGetItem(func_1079_call(relay.reshape(var_1243.astype('bool'), []), relay.reshape(bop_1256.astype('bool'), [12, 9, 13]), ), 0)
call_1262 = relay.TupleGetItem(func_1083_call(relay.reshape(var_1243.astype('bool'), []), relay.reshape(bop_1256.astype('bool'), [12, 9, 13]), ), 0)
func_1079_call = mod.get_global_var('func_1079')
func_1083_call = mutated_mod.get_global_var('func_1083')
call_1264 = relay.TupleGetItem(func_1079_call(relay.reshape(var_1243.astype('bool'), []), relay.reshape(const_1244.astype('bool'), [12, 9, 13]), ), 0)
call_1265 = relay.TupleGetItem(func_1083_call(relay.reshape(var_1243.astype('bool'), []), relay.reshape(const_1244.astype('bool'), [12, 9, 13]), ), 0)
uop_1267 = relay.asin(uop_1201.astype('float64')) # shape=(2, 13, 11)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_1286 = relay.TupleGetItem(func_261_call(relay.reshape(call_1217.astype('uint16'), [5, 6, 6])), 0)
call_1287 = relay.TupleGetItem(func_263_call(relay.reshape(call_1217.astype('uint16'), [5, 6, 6])), 0)
output = relay.Tuple([call_1217,const_1218,const_1219,var_1220,call_1228,call_1232,var_1243,const_1244,bop_1256,call_1261,call_1264,uop_1267,call_1286,])
output2 = relay.Tuple([call_1221,const_1218,const_1219,var_1220,call_1229,call_1233,var_1243,const_1244,bop_1259,call_1262,call_1265,uop_1267,call_1287,])
func_1295 = relay.Function([var_1200,var_1220,var_1243,var_1255,], output)
mod['func_1295'] = func_1295
mod = relay.transform.InferType()(mod)
mutated_mod['func_1295'] = func_1295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mutated_mod.get_global_var('func_1295')
var_1297 = relay.var("var_1297", dtype = "float32", shape = (2, 13, 11))#candidate|1297|(2, 13, 11)|var|float32
var_1298 = relay.var("var_1298", dtype = "uint16", shape = (180,))#candidate|1298|(180,)|var|uint16
var_1299 = relay.var("var_1299", dtype = "bool", shape = ())#candidate|1299|()|var|bool
var_1300 = relay.var("var_1300", dtype = "bool", shape = (12, 9, 13))#candidate|1300|(12, 9, 13)|var|bool
call_1296 = func_1295_call(var_1297,var_1298,var_1299,var_1300,)
output = call_1296
func_1301 = relay.Function([var_1297,var_1298,var_1299,var_1300,], output)
mutated_mod['func_1301'] = func_1301
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2106 = relay.const([[[6.159195,2.358459,-8.668212,9.457508,-3.841351,4.228684,-6.930641,-9.739100,5.068603,-2.548663],[4.536779,-4.585649,9.763754,8.921953,-1.349959,-8.413670,2.825644,3.267944,-8.808765,0.626293],[2.109742,-6.511444,0.871358,-5.967312,6.344816,-5.422872,2.858184,-4.577753,1.816456,5.537324],[-9.700562,3.870016,6.831530,3.082236,-6.025536,-3.972604,-5.735800,7.795179,4.367813,-0.435748],[-2.911183,7.693143,5.633441,-3.677061,-5.460661,-1.577228,3.830195,-1.577165,-5.749358,-2.019486],[-3.085819,-1.413282,-6.128645,-7.434866,-4.689965,-4.682002,4.754489,-0.293101,1.104664,-3.573743]],[[-9.120719,-7.601306,-1.300349,-5.280751,6.127854,4.819426,9.735493,-3.827701,3.744229,-2.445420],[1.146242,-0.195720,-6.770446,4.908341,2.502744,4.801759,-9.889527,5.064341,3.702425,-5.809998],[5.595943,-6.448561,7.198818,-0.357095,-3.224822,-9.694183,9.741197,-4.765391,-7.359885,7.292903],[2.495319,1.989507,-3.448664,4.731143,2.757371,-6.839477,4.916557,8.304368,8.714151,-1.522352],[-9.092740,0.569666,7.536009,-9.078330,5.619024,-8.100292,-1.821256,1.003964,-0.810513,-0.960493],[-2.919684,-4.044839,-4.530966,-0.872003,8.273836,5.395616,-1.311156,9.507881,-8.904879,2.944961]],[[9.636945,2.495822,9.746427,0.433634,6.259199,9.885318,-9.401544,6.818390,-0.801818,6.693517],[-5.610248,5.878673,5.401146,6.364554,-4.152584,-4.914435,-1.351646,-4.403479,-8.578239,8.367701],[1.760701,3.477398,7.294950,-8.778040,-5.722361,9.144898,-7.505969,5.177101,-3.479049,-2.937280],[3.804201,-5.811823,-1.769003,-3.720702,-2.498784,-9.715598,-2.677115,-1.306672,-9.346554,2.321318],[-5.663311,-3.789059,-3.972615,-3.723976,-9.462463,0.917746,0.286293,0.099528,-6.430504,-8.842184],[8.842823,0.982871,-1.798785,3.421051,-1.150215,-1.523939,-0.449027,-7.922919,-4.047628,5.488916]],[[5.145771,5.730396,-1.051523,-7.054961,-5.793454,-7.647856,1.348408,5.444526,2.180006,-7.775643],[-2.706770,-1.786946,8.824073,1.146641,8.410904,-5.077601,0.446399,-9.796518,-6.813315,4.169538],[3.877653,7.904174,5.506995,1.628584,9.424859,-3.404329,-3.453124,-7.850435,8.063734,0.672803],[-0.729309,4.865440,1.785104,-5.856172,-7.831123,-6.412354,4.599039,-0.897905,1.738926,3.828507],[-8.141497,-0.303957,-7.776016,-6.158119,-1.424341,-5.093392,-8.220426,-5.557498,6.746361,4.875177],[-1.143141,-1.317105,4.251516,-1.341539,-9.661178,-4.834839,-3.336044,6.313922,4.845221,-1.334292]],[[3.995946,8.767463,1.210550,-9.345962,-8.906187,-4.400447,7.393213,-1.593808,-3.834244,3.228008],[-6.696136,4.786265,-7.966628,7.198794,-7.066351,4.159010,-8.844785,6.123717,5.372129,4.558121],[-5.539426,-3.672266,-7.416782,-4.394710,-9.364978,8.245321,6.237586,7.700048,2.020540,-7.859671],[-7.687429,9.343627,-5.210218,-5.774615,-0.257560,8.155419,-7.040730,4.737460,-5.561624,2.265152],[1.988490,6.402428,2.233667,7.341111,4.548771,-8.123358,0.817931,-8.856710,4.322294,8.566245],[-8.492165,-2.406216,6.439511,5.112838,5.634161,-8.798322,9.410179,-8.309088,-2.139597,8.544267]],[[3.024580,7.339134,-5.557909,-2.515540,9.797207,6.399247,-7.645731,-3.266511,0.442410,2.553086],[-6.630095,-2.536823,4.333976,-8.927388,-1.041678,0.398361,8.873871,-4.835122,-1.548747,8.353844],[7.502801,-6.947216,-1.050480,3.106375,-7.085571,8.160119,-2.468377,0.541935,-9.006092,8.740881],[4.011911,-4.404277,0.735727,-7.624242,7.741654,8.740373,7.663927,-5.529290,-5.946920,5.298581],[-6.410873,5.426064,-9.734718,-8.068535,-7.696590,7.744975,-7.901899,1.279084,9.397395,3.880565],[0.396044,6.426761,-3.253523,9.156033,0.029552,-1.147641,8.146821,-9.464888,-7.401564,-3.729514]],[[-4.130314,-6.901563,3.498802,-7.322537,-9.532872,9.602494,6.060211,-9.602087,-3.552134,-0.652921],[-9.774817,4.206757,9.269173,-1.456507,-5.297191,-8.040105,-7.995786,6.204271,-1.978668,-1.062971],[0.727802,5.539262,-4.015980,6.691057,2.878683,-9.705286,-0.536100,9.665071,6.382054,0.458877],[-2.030844,-8.154194,-0.875202,-1.696003,-9.463401,1.491839,-4.579605,-7.705743,-3.879857,5.668064],[5.051001,-7.902003,8.655294,2.264924,7.697981,-5.304949,8.534032,-0.468427,-4.475367,-4.192820],[-0.618397,-3.140246,-8.281332,5.061894,-7.898515,-0.165792,8.130261,2.607550,-6.692523,6.839124]],[[4.856956,0.627321,3.239194,3.485948,-0.117367,-1.682116,2.723763,6.111001,9.080841,6.737383],[7.773171,3.306517,-3.197300,3.501851,-9.420565,-1.581814,-7.261177,-8.869236,5.695922,5.605259],[4.224415,-2.683815,8.700861,6.488791,9.043789,-9.679024,-7.663584,8.119236,2.045684,-0.512798],[7.438669,3.152501,-7.412921,7.834058,0.062698,-3.596393,-1.132492,-3.627799,-0.690652,-7.222075],[-0.752286,7.445911,9.124227,6.149591,5.645109,-1.887360,-1.607678,9.982054,7.811657,-8.213407],[2.765619,1.955538,-7.634590,3.598645,0.772166,-9.674268,0.882274,5.900410,-2.117747,3.455519]],[[-0.898049,-0.137659,5.108509,8.946115,6.636656,-4.114787,-7.368058,-7.464380,5.566619,-3.140627],[-0.042105,-9.239808,-7.634065,-5.592589,-3.249925,-2.864156,7.382361,4.468087,-3.898718,1.121700],[-7.684864,2.605465,8.254028,4.502385,3.428243,-4.364883,-5.814663,4.737554,-3.527327,3.308740],[4.539400,5.655618,9.395733,-2.683765,1.486914,4.999338,6.180524,9.265323,-9.378639,2.345475],[-2.004759,5.184462,-4.936677,9.573031,-0.247793,2.845386,-6.867095,-5.751385,0.641807,-5.569251],[-9.823185,-4.686769,-7.182929,1.575622,4.404855,-3.832142,-3.779558,-7.548214,2.164571,3.941514]],[[6.086858,7.210072,0.718913,0.379818,-5.859370,5.986394,0.717044,-8.978966,9.677549,-1.169419],[-8.158494,-0.622984,0.300821,6.878338,-2.798837,-1.851773,6.698554,-1.664996,-6.812261,8.515567],[1.550956,9.115826,8.705185,-3.051797,4.461474,4.523018,3.607304,-7.637222,-8.540456,8.695928],[-0.628762,-3.009056,-0.943121,-5.676605,-8.963042,0.100678,3.216414,-6.422472,9.425648,5.899336],[-5.085972,-2.080581,0.845187,-5.448593,5.231828,-6.428922,2.912670,2.813135,6.686130,-8.457755],[-1.902295,8.207376,2.090177,-6.363369,-0.328441,6.001279,-4.757604,4.999401,3.328584,0.810684]],[[2.169720,-0.607296,0.618939,-4.472731,-0.836981,-8.675301,7.625132,-3.854780,-6.509231,7.893515],[-6.952561,9.022536,-1.446351,-6.011845,-9.494775,-6.578841,-3.172951,-3.081814,0.866436,-0.552580],[-5.933830,-7.158663,8.514652,-7.635026,0.320126,-5.686896,-8.135776,-0.191222,-9.527425,-9.873242],[-8.454841,7.905482,-0.636671,-5.171808,-4.143374,7.276285,-2.670720,-3.945877,-0.220689,2.118989],[-6.223420,2.126930,2.851808,-9.434256,6.903607,-5.853807,6.790591,-8.422279,2.094967,8.109353],[3.890779,-6.465551,-4.825272,6.384114,9.571743,-3.950989,7.417041,6.207104,7.338797,-5.374257]],[[-8.245736,2.478222,-3.123153,9.269075,-2.697766,-9.909061,6.721881,4.069889,6.128649,-9.412762],[5.153707,2.030751,4.125690,6.762518,-6.514311,6.030356,-1.557857,-4.278064,-5.594728,4.104432],[9.876145,-1.868702,-8.126820,-3.738517,3.902617,2.463286,-6.197762,8.106635,1.359425,-5.101194],[-9.474907,-7.029258,-1.182784,-4.831696,4.617648,-5.181214,4.863136,0.861978,-3.195141,5.517534],[8.560385,4.526798,3.486293,2.886023,6.539743,-0.124741,5.491923,4.768183,-6.426910,-8.179905],[7.542111,-3.846846,7.866484,-3.842979,4.662280,2.110517,-9.386639,-4.584525,4.879320,-1.635274]]], dtype = "float32")#candidate|2106|(12, 6, 10)|const|float32
uop_2107 = relay.sinh(const_2106.astype('float32')) # shape=(12, 6, 10)
uop_2115 = relay.log10(const_2106.astype('float32')) # shape=(12, 6, 10)
output = relay.Tuple([uop_2107,uop_2115,])
output2 = relay.Tuple([uop_2107,uop_2115,])
func_2131 = relay.Function([], output)
mod['func_2131'] = func_2131
mod = relay.transform.InferType()(mod)
output = func_2131()
func_2132 = relay.Function([], output)
mutated_mod['func_2132'] = func_2132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_2166 = relay.TupleGetItem(func_2131_call(), 1)
call_2167 = relay.TupleGetItem(func_2132_call(), 1)
output = relay.Tuple([call_2166,])
output2 = relay.Tuple([call_2167,])
func_2168 = relay.Function([], output)
mod['func_2168'] = func_2168
mod = relay.transform.InferType()(mod)
output = func_2168()
func_2169 = relay.Function([], output)
mutated_mod['func_2169'] = func_2169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_2227 = relay.TupleGetItem(func_2168_call(), 0)
call_2228 = relay.TupleGetItem(func_2169_call(), 0)
func_631_call = mod.get_global_var('func_631')
func_636_call = mutated_mod.get_global_var('func_636')
var_2230 = relay.var("var_2230", dtype = "float32", shape = (1152,))#candidate|2230|(1152,)|var|float32
const_2231 = relay.const([4,2,-3,5,-4,4,-7,9,-9,-4,-6,-5,5,-5,1,-6,6,-4,-2,-1,-4,-4,1,10,10,1,7,9,1,7,-5,-6,1,-2,-1,-9,7,5,9,-7,1,5,4,-10,-9,7,-9,7,-5,3,3,2,-5,5,6,5,2,5,-5,2,-1,-9,2,-2,-6,-4,7,8,-4,-8,-7,-8,-2,-6,10,-4,-7,-3,1,-7,-10,-8,10,9,-9,6,1,-8,9,-1,-3,1,-7,10,-10,7,-1,-7,10,-7,-6,-6,7,9,9,-8,-4,-4,-3,-1,3,-5,4,5,1,-3,-5,1,5,9,-9,-8,-5,-5,7,5,5,-4,3,3,3,8,-6,-9,6,-7,-6,7,-7,2,-8,6,7,2,-1,-4,10,-2,1,-7,3,2,-9,3,-1,2,1,5,-9,-10,4,7,-3,10,2,1,-1,5,3,-8,4,-6,-7,5,-9,-8,-6,-7,-4,3], dtype = "uint16")#candidate|2231|(180,)|const|uint16
call_2229 = relay.TupleGetItem(func_631_call(relay.reshape(var_2230.astype('float32'), [16, 12, 6]), relay.reshape(const_2231.astype('uint16'), [180,]), relay.reshape(const_2231.astype('uint16'), [5, 6, 6]), ), 0)
call_2232 = relay.TupleGetItem(func_636_call(relay.reshape(var_2230.astype('float32'), [16, 12, 6]), relay.reshape(const_2231.astype('uint16'), [180,]), relay.reshape(const_2231.astype('uint16'), [5, 6, 6]), ), 0)
output = relay.Tuple([call_2227,call_2229,var_2230,const_2231,])
output2 = relay.Tuple([call_2228,call_2232,var_2230,const_2231,])
func_2247 = relay.Function([var_2230,], output)
mod['func_2247'] = func_2247
mod = relay.transform.InferType()(mod)
var_2248 = relay.var("var_2248", dtype = "float32", shape = (1152,))#candidate|2248|(1152,)|var|float32
output = func_2247(var_2248)
func_2249 = relay.Function([var_2248], output)
mutated_mod['func_2249'] = func_2249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_2251 = relay.TupleGetItem(func_2168_call(), 0)
call_2252 = relay.TupleGetItem(func_2169_call(), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
var_2254 = relay.var("var_2254", dtype = "uint16", shape = (180,))#candidate|2254|(180,)|var|uint16
call_2253 = relay.TupleGetItem(func_261_call(relay.reshape(var_2254.astype('uint16'), [5, 6, 6])), 0)
call_2255 = relay.TupleGetItem(func_263_call(relay.reshape(var_2254.astype('uint16'), [5, 6, 6])), 0)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_2260 = relay.TupleGetItem(func_2131_call(), 0)
call_2261 = relay.TupleGetItem(func_2132_call(), 0)
output = relay.Tuple([call_2251,call_2253,var_2254,call_2260,])
output2 = relay.Tuple([call_2252,call_2255,var_2254,call_2261,])
func_2263 = relay.Function([var_2254,], output)
mod['func_2263'] = func_2263
mod = relay.transform.InferType()(mod)
mutated_mod['func_2263'] = func_2263
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2264 = relay.var("var_2264", dtype = "uint16", shape = (180,))#candidate|2264|(180,)|var|uint16
func_2263_call = mutated_mod.get_global_var('func_2263')
call_2265 = func_2263_call(var_2264)
output = call_2265
func_2266 = relay.Function([var_2264], output)
mutated_mod['func_2266'] = func_2266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_2395 = relay.TupleGetItem(func_2131_call(), 1)
call_2396 = relay.TupleGetItem(func_2132_call(), 1)
output = relay.Tuple([call_2395,])
output2 = relay.Tuple([call_2396,])
func_2402 = relay.Function([], output)
mod['func_2402'] = func_2402
mod = relay.transform.InferType()(mod)
mutated_mod['func_2402'] = func_2402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mutated_mod.get_global_var('func_2402')
call_2403 = func_2402_call()
output = call_2403
func_2404 = relay.Function([], output)
mutated_mod['func_2404'] = func_2404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_2453 = relay.TupleGetItem(func_2131_call(), 1)
call_2454 = relay.TupleGetItem(func_2132_call(), 1)
func_1120_call = mod.get_global_var('func_1120')
func_1125_call = mutated_mod.get_global_var('func_1125')
const_2456 = relay.const([-3.811025,6.520520,4.134946,-2.003746,4.867081,-3.547574,-6.694759,-9.506070,5.205180,-7.887535,-4.886051,-9.292390,-7.623037,1.244622,3.710796,-6.706222,-2.533296,7.761962,-8.627417,-6.157396,-2.999538,2.006377,-2.708891,-6.570364,-4.863751,2.090973,0.485193,6.781007,-1.553081,8.188119,-2.539872,0.630432,2.343730,9.314338,1.846277,9.369293,-3.357056,-3.801541,-1.773654,3.058852,-6.212148,5.270061,-9.007671,8.808719,9.156806,-2.532664,-6.804814,-2.114163,4.009353,9.697057,-0.746298,-9.221753,4.502503,7.933402,2.024469,-2.386931,-2.328656,2.749369,-1.272384,0.799490,-9.590987,0.471063,-3.993727,-9.187594,0.686011,-9.316522,9.161002,8.428111,4.221784,-8.410283,4.719163,-5.921816,7.992053,-4.010716,-8.110806,7.588321,-9.928984,2.295079,6.189155,-5.232308,6.014085,-1.498107,6.807691,4.123161,-1.310832,-5.370961,-1.853593,1.675206,-1.786929,4.344760,-3.826673,4.065896,-0.367081,0.122590,2.785865,-9.742762,-9.720127,9.878636,-0.928569,-0.540211,-0.126522,-6.894890,-1.708294,-5.042493,-2.695471,4.109940,5.655856,1.599069,-5.983077,3.714511,-4.920615,-2.207833,-2.403238,-9.446625,1.465890,1.428110,6.520850,-9.998623,-3.268224,7.585810,1.418113,3.971277,5.474971,-2.921551,6.129871,0.188381,9.865958,-2.474031,1.578466,1.119480,7.234637,7.445378,-2.524941,-6.238065,-0.303961], dtype = "float32")#candidate|2456|(135,)|const|float32
const_2457 = relay.const([-1.400577,9.646510,-1.252170,-6.253623,-8.423584,5.667569,9.895737,-7.062220,2.085581,-1.322328,-4.295184,1.464443,7.432751,-6.299183,5.902168,8.449270,2.670019,-5.643581,4.026778,5.334804,-3.749833,-0.233322,-5.482354,-5.938612,-5.231490,-7.128750,-5.042153,-2.635062,0.726646,-1.131514,-4.653104,5.941098,5.742875,5.858820,-3.955937,-8.213030,4.073205,6.991391,7.144451,-3.229859,-6.380505,2.576974,-5.917722,-1.540602,-4.720037,-6.604289,-8.773566,-4.734524,7.876012,-1.761358,2.355948,-9.917630,3.718191,-6.677285,-8.900021,-1.744805,9.150072,3.115004,5.384918,1.373958,-5.321565,-9.470215,4.548277,-3.943584,-9.478819,2.303230,-1.833376,0.287258,3.018596,-9.338504,-9.145156,-4.145836,-4.025861,9.836152,9.393269,-5.144128,-8.916040,-6.248220,2.505134,-7.985029,1.119418,6.999723,3.988097,7.493018,-4.622757,-7.713824,-8.721886,-2.784833,-9.023856,6.962425,3.938324,-0.576361,-5.185634,9.722600,1.363341,-9.279694,9.453614,-8.226468,-2.619903,1.232125,-6.961301,5.016104,-6.186803,3.611229,9.887396,-5.111194,-3.351198,-0.749880,8.502664,6.651699,4.790775,4.596011,7.023671,0.936830,7.044926,8.037058,5.248507,3.774504,-1.309664,-5.624907,4.366237,-9.238621,2.980149,-4.136643,9.532887,-2.373672,8.514510,3.226897,5.906836,-9.606660,-2.877890,-4.644497,-3.289158,1.798926,9.733641,-3.855600,6.892754,-0.183469,9.730988,4.655757,-3.054673,9.100258,-5.616065,7.749499,-9.925397,-8.804602,3.333050,-1.836489,-5.155872,-4.881579,4.596133,-4.113320,-3.061957,-6.320622,-9.355325,-4.202515,2.527261,-1.295356,-2.932124,1.996654,-5.069518,9.345928,9.345606,3.321152,-2.675774,2.929363,2.266953,-8.351276,-9.335807,9.146353,-8.835977,-4.154425,-8.868472,2.101984,-4.789695,4.257053,1.613518,-6.321677,-1.312986,-1.883599,7.257740,-8.765953,-7.076501,-3.165506,5.799607,8.555569,9.867038,2.311610,-0.924852,1.929679,-3.104069,2.540826,9.298938,-2.207397,-5.658498,-0.534031,-5.774983,-0.703792,8.555215,8.703931,-3.193656,1.551787,-6.252159,7.957945,9.936285,6.148728,8.202959,3.782376,-3.312823,-2.334576,2.001027,0.408916,-4.812901,-7.440132,-3.295183,-4.122463,-1.518796,8.731417,7.548097,9.742981,2.771582,-0.511091,-5.425972,8.525646,8.302094,2.029224,4.740377,-7.721395,-0.784338,0.247955,-1.095480,0.169036,2.546844,-4.718251,-5.579507,-9.729958,-2.478313,-5.944270,-9.786820,-1.544481,-0.757107,-7.777785,-6.656271,5.636960,4.889311,3.716963,-9.314531,-2.775639,5.280135,-9.973897,0.931807,5.641596,0.374985,-0.505680,-2.623093,2.026026,-1.771593,-5.757159,-5.443546,0.283764,-0.785558,-2.842700,3.979999,7.139536,2.763620,-7.689159,-7.590277,-9.997242,-2.853887,0.281773,3.273962,0.274091,2.624585,-0.896190,1.549892,2.349305,8.398936,-6.785728,8.438713,0.317835,-8.685329,1.779082,-5.193478,-2.182368,-9.670060,2.292755,0.225182,0.916838,-4.799816,-8.324466,8.471814,6.411233,4.846608,5.143545,9.226619,5.563038,5.092747,-2.790662,5.087584,-7.095927,5.038795,1.116928,-8.568077,7.446160,6.533325,-1.356113,8.680157,8.339206,7.613585,4.376262,0.114948,-0.791622,5.738303,-0.136699,-6.929950,-5.222626,-5.749731,-5.126266,-5.211541,2.691002,4.508831,-7.947955,-1.031497,-8.806930,2.602481,-7.959271,-2.247896,8.403367,-7.435643,-2.913437,-2.182794,-1.556554,0.727352,2.584833,-1.497159,3.405423,-5.776201,-8.806338,0.497891,-5.092331,8.901650,4.776644,-5.362124,3.932581,7.508894,0.365978,6.781801,-6.045117,-0.728412,-5.218782,5.946614,-8.018327,-3.918878,-2.687702,8.715455,-9.580957,0.975717,9.659586,-6.171215,-4.959429,-5.669410,5.708935,6.392845,-9.941984,7.496352,-5.753443,-5.512504,-4.377235,-5.809228,-3.839932,2.329039,-8.257268,4.846253,-3.379955,-2.603441,8.159170,-5.637973,-0.619217,-7.572040,8.598792,-9.065856,-1.024115,2.971535,7.463224,3.240797,6.411041,-9.993891,-9.080505,5.668069,8.075937,4.280529,0.369935,7.127019,-5.767588,-1.590120,7.461455,4.944675,-7.290974,-9.588053,-0.592358,1.623313,-8.160376,1.194888,7.451702,-0.516503,4.714396,2.172621,8.437874,-4.659034,1.016798,-1.447148,5.268257,-9.990328,-2.429693,2.610624,3.742760,-4.781849,-8.215102,-3.264047,0.918073,-3.784387,-4.716113,1.640644,-7.207703,7.070202,-9.665140,-0.264833,-1.013725,8.868292,2.152001,3.043608,-0.117223,5.356622,-7.262525,-8.406161,-5.332478,-1.984954,1.417182,-7.117408,1.946578,5.892095,9.589661,-4.111670,-9.751588,-1.799154,-4.641864,-6.871431,-8.605214,-4.617329,4.363234,-0.514385,5.162288,9.741906,-9.423860,7.974227,1.844496,0.326718,-4.830408,-1.808524,-3.397768,0.281175,8.869192,7.434369,9.327034,-4.084762,-0.561904,-9.089297,7.041448,-5.705806,0.771846,3.799832,-0.474457,-5.732121,-1.340475,-7.075414,1.271138,-2.243337,0.694848,-2.237166,8.889118,-5.943128,1.240951,7.486965,-7.905813,-0.700060,6.508313,-3.988379,0.122210,6.940402,-6.325835,-7.842944,8.364905,-1.291615,-5.581121,3.195539,9.374564,8.331590,-6.554504,2.789420,2.801154,-2.575487,5.933567,-0.174011,7.654629,5.341660,1.119396,-1.180583,-9.152444,-5.282849,5.627206,-5.823315,2.625691,-8.759006,-9.981893,-3.693149,2.220599,6.992295,5.280020,9.525130,9.079436,-8.662099,-7.543949,4.380853,0.459765,8.258515,7.810695,8.364610,-5.025445,-1.528275,4.026952,-7.649899,8.995542,-8.732066,7.541259,-5.473416,-9.947991,-0.463236,9.176339,8.893579,3.278738,0.878206,-5.681857,0.197584,-3.091230,9.783558,-8.483818,6.456065,9.367741,-7.742506,8.554946,3.078661,-0.254723,1.561210,2.284524,-9.230124,6.293181,7.934674,2.359155,-3.474478,-8.735148,6.859100,7.501224,9.244530,-2.828788,-9.408315,-2.628031,8.997231,5.597077,-7.674272,2.667159,2.651271,-1.948573,-8.563484,8.046927,-6.050432,9.496330,-2.630951,-0.462458,6.201078,9.535581,-4.388765,-3.403589,-6.606528,-7.658635,-0.943312,-4.539740,0.714860,0.871594,-2.845843,-9.263566,-1.892218,-4.539565,8.645789,-2.817551,-6.259836,-5.417634,6.187967,-0.635935,-1.362543,-8.722951,2.431425,-5.316001,-4.392287,-1.656215,-5.638829,6.401798,-8.608761,1.279592,-2.954342,9.442264,1.925145,7.441781,-1.132588,6.755451,5.567643,2.566849,-9.758955,6.287897,8.493270,9.608009,-9.274192,1.904495,-7.504878,-4.202790,-1.344859,4.517405,8.855401,1.905596,3.907719,-4.583939,-3.650855,4.388585,4.375048,1.481824,-2.795006,-3.006719,3.251951,-5.760125,-2.026070,-1.797749,-1.502998,7.955148,3.353330,0.078523,9.432831,3.112675,5.265956,-4.124600,7.475740,-8.955884,-6.112297,-5.024868,-9.471834,4.066234,-2.644995,9.494910,-8.096453,-2.116228,9.209222,-2.312231,-0.151128,5.449084,-5.610239,-4.019367,8.266200,0.931311,-8.649621,-8.175468,-6.180773,9.203776,5.908329,3.651781,6.813700,6.858391,1.951809,5.447820,4.019790,-1.802466,-8.821613,6.866693,3.622044,0.931780,7.607325,-5.953846,-3.570514,-9.315767,-7.193707,4.667707,4.440981,4.169982,-7.056965,-7.834290,0.478030,4.699464,-6.625468,5.820477,2.632544,6.859204,-4.174569,9.243840,6.915386,4.004212,8.059012,-0.771526,1.853160,-1.690806,-7.155819,-9.142417,6.434956,-0.664163,-3.664688,7.451741,-6.891040,-7.103139,-7.816057,8.313798,4.620701,4.005922,2.400159,-0.239771,7.770734,-3.744430,8.076767,3.707698,-6.856309,-6.939040,-4.404471,3.913395,-1.612871,8.722307,9.597246,6.878309,5.558147,8.452120,-5.564711,-3.353884,-7.992902,4.430825,9.304797,-9.771437,-3.862156,-2.174378,-0.329900,-9.271857,-2.788577,3.742373,-1.274595,-8.579690,-0.986717,3.771993,8.217960,-0.554477,-7.130589,-2.175887,7.332151,-0.217501,4.720107,-8.099669,-1.853171,7.961979,-8.011867,-3.631713,6.777788,3.062079,-6.089572,-3.300362,-4.704576,-6.895600,-6.726387,-7.181362,1.600505,-0.658590,1.304490,7.656808,9.244399,-7.997102,2.493165,-6.754172,-2.922165,-1.042642,-3.318491,-5.651808,-6.667418,-5.851722,0.591596,-0.785266,9.831629,-0.744385,5.055511,-4.720996,-0.843183,-5.627285,0.669354,-2.169759,-3.807043,-6.709410,4.838913,3.961543,2.235856,-0.153906,-7.829667,-4.869959,4.203470,0.014632,-2.759385,3.536075,-0.689887,-5.435499,5.267803,7.880365,-8.858342,-7.404609,0.167331,0.491331,6.101542,7.504628,-3.640484,4.025318,-5.009618,-2.645983,-2.687974,5.785119,4.242053,-8.918762,-5.661884,9.951744,-6.430190,-9.988879,2.921559,-3.816033,-0.724091,8.101541,4.540066,-6.893020,8.039265,-8.703991,3.613356,-3.888927,-3.040157,4.955347,7.454147,6.241453,-7.237146,0.033296,3.427646,8.364931,2.324671,-9.197775,9.664232,8.952779,5.957725,7.521811,2.890268,6.728556,-7.368954,0.798408,2.421572,1.855132,-8.348009,-6.240713,4.998737,7.723495,-1.161035,6.101280,9.695526,-8.345284,7.196150,2.556774,6.119554,-8.264366,5.418550,6.971548,-0.689743,-1.525187,3.642390,-0.654445,-2.794197,-5.875013,9.851258,7.685319,-8.159486,7.810408,4.992445,-2.525850,1.203992,-6.436907,-5.659728,-1.854477,5.275672,-6.241232,3.317637,5.428727,-2.607567,-5.837999,1.224214,-7.914775,5.066793,2.235946,-7.466995,4.523528,-1.699193,-4.869208,-7.618856,1.052397,-6.438827,-8.563904,-9.444343,9.873403,2.229984,-6.675308,8.060219,-5.647565,-1.845495,0.922181,-7.127785,0.940044,9.391990,1.879395,-6.685989,2.764794,-3.199887,-4.853463,4.930580,-4.135891,9.841493,0.829757,7.415018,2.854280,-6.272928,6.045650,8.198818,0.165982,-7.611472,-7.454333,-7.549209,0.679722,-0.090942,7.852532,-3.620310,-0.904308,0.114058,-5.129227,-4.610082,-1.633518,2.584748,2.707339,-8.479211,7.530230,5.818506,0.971416,7.840442,7.454554,-7.536499,3.986518,-8.751572,-4.149531,6.278596,-1.359433,-8.602661,-0.632537,-8.674750,5.138834,9.791464,-7.365581,-9.137420,-5.944475,-4.548848,9.675058,-0.964277,5.764946,5.930642,-1.651974,3.816922,-0.444079,-2.533554,3.499321,-9.661647,1.024135,1.652567,-9.613313,-0.374899,6.684735,-5.706537,9.000160,3.080182,5.446223,4.532233,7.161593,9.506368,-5.412904,5.860913,-5.072198,-0.224111,1.579719,1.889086,-3.631108,-7.527634,8.204566,-0.861905,6.308744,6.877190,-1.941436,4.328414,4.347556,6.723993,-6.429310,6.732031,-9.155917,-0.664655,1.934453,-2.048718,6.468332,3.838738,5.647779,-1.324853,6.254517,-9.792501,-1.232032,-2.168010,-6.007151,3.108614,-3.519368,4.269135,4.032980,-4.080910,-6.366006,-6.790434,7.159061,-9.922891,1.774909,1.215017,-8.441516,1.075319,2.755301,2.712045,5.234915,-9.252197,2.552138,9.861181,-9.646149,-7.815200,-7.160508,-9.223828,-7.453126,-6.538280,6.342294,6.619603,6.926775,-5.696810,-8.387726,-3.964919,1.004844,2.480684,5.859179,5.181826,-7.870970,-3.411887,-0.918416,-1.349703,6.494164,-1.418072,-2.523695,-5.332749,-7.021083,5.626914,-8.944073,6.489969,-6.158410,1.857806,3.320551,3.970140,-6.716810,-2.850100,2.360725,9.116390,0.717095,5.094570,2.182308,-0.969956,6.394276,-7.599127,5.445642,6.677091,-6.602925,4.489198,0.701850,8.729906,-4.505121,-6.697716,-3.159305,-9.951008,0.529384,-9.446960,-0.570056,5.394116,-5.068435,5.469223,6.740614,6.458605,6.519865,3.895135,-6.057870,-6.434683,-8.763646,-9.315063,1.977350,-3.896012,-1.257528,3.874246,2.823113,-6.077948,6.007662,-8.353602,-6.994896,-7.679151,-6.858413,-5.824767,6.412755,-9.073265,3.878580,-7.044160,8.620051,-9.349137,2.345137,-1.362488,-0.818793,-9.506683,1.276092,-4.814253,2.365583,4.608222,-4.692686,-2.484841,5.970324,4.752913,2.823945,3.522197,-5.861767,-8.423325,5.871776,2.519525,-6.141512,3.125128,-3.005457,1.007472,0.152500,2.627609,8.110624,2.894126,-4.543689,0.476846,-1.286519], dtype = "float32")#candidate|2457|(1152,)|const|float32
const_2458 = relay.const([-1,-7,-4,8,1,9,7,3,9,-4,-6,-6,-8,10,-9,6,5,7,-10,1,7,5,9,9,-7,-8,4,8,6,1,10,-3,3,-4,-9,4,4,-9,-7,-1,-1,-7,-3,-9,4,2,7,9,-7,5,-10,1,-10,7,9,2,-6,-7,6,6,3,-6,-3,-2,-1,-6,8,5,8,-3,-1,-8,-6,6,2,5,-1,-8,7,-7,-9,-9,10,2,7,6,-2,5,-1,3,-4,-1,-9,-3,8,-7,3,-3,2,-3,-3,-5,3,-5,2,10,-4,4,9,-4,-7,6,-8,5,4,-9,4,2,-5,-4,4,-4,6,-4,5,-3,-8,4,-6,6,-6,-7,-8,-10,3,-9,-9,-7,-2,1,8,10,1,-4,3,-8,-4,9,-3,4,-4,-5,7,-9,1,-4,2,-7,-8,-3,-8,9,-6,-3,-7,5,9,4,1,4,-3,-3,4,9,8,2,5,-9,10,-9], dtype = "uint16")#candidate|2458|(180,)|const|uint16
call_2455 = relay.TupleGetItem(func_1120_call(relay.reshape(const_2456.astype('float32'), [9, 1, 15]), relay.reshape(const_2457.astype('float32'), [1152,]), relay.reshape(const_2458.astype('uint16'), [180, 1]), ), 1)
call_2459 = relay.TupleGetItem(func_1125_call(relay.reshape(const_2456.astype('float32'), [9, 1, 15]), relay.reshape(const_2457.astype('float32'), [1152,]), relay.reshape(const_2458.astype('uint16'), [180, 1]), ), 1)
var_2464 = relay.var("var_2464", dtype = "uint16", shape = (5, 6, 6))#candidate|2464|(5, 6, 6)|var|uint16
bop_2465 = relay.equal(call_2455.astype('bool'), relay.reshape(var_2464.astype('bool'), relay.shape_of(call_2455))) # shape=(5, 6, 6)
bop_2468 = relay.equal(call_2459.astype('bool'), relay.reshape(var_2464.astype('bool'), relay.shape_of(call_2459))) # shape=(5, 6, 6)
output = relay.Tuple([call_2453,const_2456,const_2457,const_2458,bop_2465,])
output2 = relay.Tuple([call_2454,const_2456,const_2457,const_2458,bop_2468,])
func_2477 = relay.Function([var_2464,], output)
mod['func_2477'] = func_2477
mod = relay.transform.InferType()(mod)
var_2478 = relay.var("var_2478", dtype = "uint16", shape = (5, 6, 6))#candidate|2478|(5, 6, 6)|var|uint16
output = func_2477(var_2478)
func_2479 = relay.Function([var_2478], output)
mutated_mod['func_2479'] = func_2479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_2500 = relay.TupleGetItem(func_2168_call(), 0)
call_2501 = relay.TupleGetItem(func_2169_call(), 0)
output = call_2500
output2 = call_2501
func_2502 = relay.Function([], output)
mod['func_2502'] = func_2502
mod = relay.transform.InferType()(mod)
mutated_mod['func_2502'] = func_2502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2502_call = mutated_mod.get_global_var('func_2502')
call_2503 = func_2502_call()
output = call_2503
func_2504 = relay.Function([], output)
mutated_mod['func_2504'] = func_2504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_2535 = relay.TupleGetItem(func_2402_call(), 0)
call_2536 = relay.TupleGetItem(func_2404_call(), 0)
func_2247_call = mod.get_global_var('func_2247')
func_2249_call = mutated_mod.get_global_var('func_2249')
const_2538 = relay.const([-5.855721,0.094730,9.474029,0.210336,6.977166,3.344034,-5.576259,-8.761472,3.317572,-4.138903,-4.418691,-9.181916,-7.911503,3.647830,-3.990038,2.999134,-7.010775,9.074249,6.044264,-1.858979,9.919427,-4.165085,-3.236722,8.089227,-5.937302,-1.617787,-7.462361,-5.133456,-3.871592,1.436041,4.184585,3.940754,6.202915,5.525019,1.281385,4.931530,-7.948153,0.183235,-9.142418,-8.362595,-1.809827,-3.796279,4.178805,3.189548,-4.891012,3.405855,5.490164,8.924066,1.113323,7.335046,-8.932033,5.961254,-6.104689,0.074842,8.036145,8.078702,-0.810102,-6.065271,-2.930641,-3.918367,-0.854903,-4.320701,-5.945817,-3.486276,9.514943,4.452777,2.195109,-8.945392,7.625609,-3.364882,2.771526,-2.999125,7.877842,3.002949,-8.932710,9.880359,6.889336,-0.998808,4.903750,8.367345,-4.146031,9.492491,0.217058,5.769811,9.077326,7.638473,5.003713,4.817314,1.803949,5.985855,-0.987524,-0.046657,-2.022123,1.496138,-4.412822,-1.637201,2.040855,-8.009755,7.347490,5.569846,5.873296,7.642944,-5.536114,-9.411401,-8.548668,6.835261,-0.724053,-4.999772,-2.620482,-8.952481,0.917882,2.074782,-3.412053,5.971065,8.260565,1.517836,-9.095390,-4.585783,6.188320,-6.349568,-2.935340,-3.324196,9.679068,6.908502,-6.370637,-3.348876,4.356639,4.848188,6.059464,3.521406,5.226785,-1.315023,-8.963100,8.079192,8.873758,3.740952,4.992025,-3.264725,-9.111060,9.994356,5.875984,-6.197285,3.968579,4.026710,1.268416,-3.608204,8.627896,-5.531299,4.948873,3.926715,6.255252,-1.342004,-1.879053,2.317750,-3.632188,9.963594,3.758547,-3.993699,7.216149,2.579351,5.951088,-4.702581,-4.900122,-5.281171,-0.068905,-9.486340,-1.894585,-2.602931,0.226132,8.824376,-6.164964,-6.478948,3.709189,1.351122,-6.248754,9.068117,-1.310838,-4.402426,-9.857661,-5.874596,-2.763405,-2.481644,1.564156,0.136487,-9.845790,-3.585884,8.769185,-6.014715,-1.283450,-6.697248,4.953585,-7.150716,3.562159,-7.445057,6.577241,-1.330489,-7.290900,-5.947224,2.800077,-7.690038,-7.169991,3.241298,7.611008,-9.300038,5.251275,-4.597716,-8.758884,-1.504362,1.629840,4.052329,2.623244,-5.545201,-2.426628,8.313930,-5.695654,-2.072389,-0.229516,5.640736,0.273760,8.046984,-3.590262,5.916533,-3.561622,-9.520311,3.170986,-6.017081,8.092740,-2.242355,9.851095,5.516238,5.183696,6.674708,1.235611,-7.581222,-4.248201,2.886763,7.761122,-4.862675,-6.387162,-2.050241,-0.623277,-8.810575,3.114795,-5.869168,-4.998016,0.194046,3.494244,-1.271965,3.034187,4.293504,-6.356346,-7.082404,-3.442560,-8.184802,8.998452,-8.170703,5.414268,2.158859,6.845060,-0.904141,1.146834,8.835554,-6.951235,-4.129077,-9.892136,9.487327,-8.879091,2.241229,-9.367739,-9.092149,-7.590023,-5.553513,1.223388,-6.550486,6.486283,0.872367,-6.374543,5.499253,-8.144326,-7.241184,1.448391,9.737486,7.376257,-6.366277,-7.355669,4.076008,4.735785,4.382282,8.041409,6.824278,-2.157269,-4.687918,-8.450912,6.062663,2.576175,9.952699,5.139417,-1.568905,4.806877,4.054902,5.024511,-7.790398,-3.791885,-0.305832,-0.207374,-0.570402,-5.275184,6.723526,-8.126364,1.740704,1.333744,-5.874754,5.985871,7.752512,-3.871882,3.840494,-0.644285,-0.359045,5.825573,-5.467600,3.416612,-9.689546,4.153013,-6.785925,-9.092803,2.687380,-1.022863,-7.550214,3.322790,9.952119,-0.410359,6.681596,-3.814825,9.302529,-1.324532,0.037475,-0.801641,5.751221,-8.767057,6.271914,2.719974,-9.821724,6.128609,-0.025061,-8.400019,-6.679374,-8.470365,0.411837,9.727720,-0.903651,9.410088,6.165510,3.879560,8.572741,-8.674684,-2.254397,-6.731549,-3.401377,1.166334,-9.907127,-5.164019,8.477280,-7.652239,8.164156,5.946383,-6.772260,-5.125733,9.073921,-9.071817,9.661695,3.790788,2.818796,-0.379909,4.306698,-0.010464,5.980640,-9.505009,3.961259,-8.680324,9.409379,-8.125366,-1.398861,7.731949,-5.496138,-6.100125,6.485612,2.364146,5.599492,-2.609591,4.768036,-9.369474,5.748266,0.072684,-1.505787,1.488264,-7.674326,7.782595,-0.779237,-6.651353,-4.766362,-2.291338,-0.706134,-9.393309,1.507248,4.978759,4.634789,-9.491688,-7.713390,2.871805,5.695301,-7.802288,-4.108929,-8.012689,1.610650,9.751629,9.747861,0.064416,2.906287,-1.699708,-9.165513,-6.294995,8.503701,-6.165332,-5.660444,-9.372916,-8.819676,2.180485,-6.555163,-9.531386,-5.394876,-8.175237,5.150129,-2.867819,3.836587,-6.232518,-2.200051,-4.940779,6.557893,0.818803,-9.058052,2.154761,4.905989,-7.810649,-2.778233,1.643756,-9.808719,-6.949287,7.565260,6.180960,3.897672,-4.115005,-1.815980,-9.686352,1.348154,9.262030,9.635019,-2.585066,-8.196569,1.803421,6.617613,9.471909,-0.806034,-1.034769,-7.021076,-5.997700,1.723401,8.339414,8.344312,3.803071,-0.215769,7.952368,6.254045,-6.248729,-6.918860,-2.257642,-4.682604,7.799284,1.734666,-9.874355,2.778897,-3.319796,7.825898,-4.237935,3.441997,7.294113,7.050229,3.543899,-8.200787,-7.884008,0.487340,5.730744,-3.005159,-3.232729,-1.702203,-8.983664,-9.931760,-8.603922,-7.871060,-7.771329,-5.377776,6.716405,-0.971628,-0.366835,-4.861885,6.539719,3.076357,8.507322,-2.628095,9.049693,-3.734385,-2.600690,-4.638682,-6.598598,-6.618278,-7.752244,-7.835454,-1.088433,3.025547,-5.319633,2.840791,0.419520,-4.804236,-8.639880,3.381412,5.954860,0.660114,-0.713179,-4.834066,6.499234,2.042923,9.183762,6.899953,0.834387,-6.556414,2.573065,4.509657,-6.595511,3.578768,-9.054680,-7.895132,4.548927,-7.347090,-1.196850,-8.527694,8.316790,0.287598,-7.848681,-0.240807,4.837084,1.878487,-6.668318,-0.018278,-1.993912,8.948685,-1.216467,-3.580740,-7.831138,9.839918,8.635210,-7.085628,5.218601,5.827412,-9.911832,7.378136,-7.596392,-7.389520,-9.024599,4.276969,6.254277,2.571273,-8.943577,4.216445,-5.906644,0.710744,-3.237287,-2.078026,-7.968777,7.544509,8.756701,-4.152611,1.027976,-2.312542,6.743754,-6.327347,2.981476,-2.267948,8.301436,-1.862392,-1.444176,3.022862,1.584558,6.040023,7.869096,-9.787350,9.124545,-7.838516,-8.430043,-8.388147,-6.359368,-6.331983,2.426910,-7.916150,-8.277601,-1.775682,-4.685042,3.247026,-7.712485,5.580317,-7.251452,-7.768817,7.995858,-8.883822,-4.255513,4.126186,-3.030569,-0.412256,3.350086,-0.223892,9.984599,-4.966002,8.936189,3.677315,-3.389879,5.181689,-3.943798,1.664831,3.043373,2.507883,-5.497310,-2.196404,-9.330035,-9.529900,8.587359,7.561021,-1.110630,7.929833,-6.940363,3.295144,5.044501,6.216968,-5.130280,0.444480,-6.878491,6.330727,-8.799636,7.575412,-2.517073,-9.518407,9.706934,-3.027127,3.941911,3.008457,-1.152248,9.426736,6.887937,-9.827217,0.809253,4.323586,-0.052881,-0.324866,1.830175,-1.372775,-0.144303,1.526329,-7.449916,6.858765,3.233085,3.469137,4.254233,-7.814045,3.126710,-9.715351,-0.008500,2.541936,8.440601,4.876879,9.464373,-7.416717,-9.831598,3.805307,-4.869144,2.905360,9.907577,7.705466,6.448150,-8.851537,-6.678271,1.578063,-2.636637,-9.604252,-6.762038,-5.513298,5.679876,8.721353,5.849745,-2.685188,0.400910,4.011696,6.446936,3.723416,-8.679782,7.857621,8.763841,-4.095291,3.193529,3.837542,-2.168939,-1.908523,-8.892893,-2.962588,-6.531446,1.561619,-6.080604,3.285612,-9.532116,-7.196511,-6.079010,1.326701,-7.499655,8.675404,-0.033561,9.791318,2.577606,-9.199665,-9.523340,8.615306,-2.957410,-0.933965,2.678586,-9.682599,9.529564,4.038257,-4.506677,6.231642,-4.212772,1.158317,3.786794,0.283634,-3.504270,-9.529680,-0.706173,5.416626,4.703167,7.264566,6.605188,-5.651665,-1.445438,-8.883334,-4.437006,3.302578,6.044562,-8.890603,-0.142154,9.497267,4.381401,4.717509,8.687148,-4.083789,-8.677517,0.663844,8.818198,-7.379682,1.704754,5.194057,-8.255579,-4.911498,5.760096,-8.179719,3.891471,-5.960789,-8.833279,-2.225488,-8.628239,-7.846093,2.677842,8.645861,5.669347,-0.080781,-7.279471,-2.425630,7.034141,-2.503462,2.644960,-8.391522,-6.485268,-8.031086,-1.785437,-4.767850,5.435475,9.195186,9.748831,-6.271270,9.768472,9.300806,-5.723737,-2.232497,1.459239,-5.622369,-3.189948,9.444847,5.565934,2.892834,-1.205302,-2.317239,-2.268929,-1.658602,-6.825345,-9.213711,-8.609234,-0.388724,5.830081,-4.629449,7.778062,-3.114738,4.289815,8.563336,3.016362,-5.563010,-2.036203,9.030212,-8.168595,-3.453100,-1.914671,-2.385795,7.325432,1.579167,-0.191435,2.184047,-8.494370,2.905990,7.030101,-3.406126,7.509150,-9.859249,-8.805876,-2.259170,-2.120324,4.355107,5.999244,6.847515,-5.473806,0.673033,-6.254108,9.939857,-5.704457,-8.132892,6.010875,-0.489344,3.324370,-5.072187,4.402269,-8.898354,-4.829063,-6.645127,-7.746697,-2.591805,8.062544,3.232764,-5.317424,-1.132331,3.451468,-2.429959,-4.452547,6.391015,4.126299,5.680915,-8.633124,-3.287011,0.027155,-0.403085,-2.641848,5.405522,-8.980088,0.043687,5.431125,-4.338505,-7.721869,2.933472,9.252442,-6.500774,-1.623570,0.598374,-1.126128,7.100602,2.203308,3.831999,-5.112632,4.274705,9.455464,4.020012,-4.629794,5.475914,-0.676064,1.840799,5.284957,6.798971,3.973629,-4.519000,-1.957213,-2.957411,2.985535,-4.486750,-1.390007,-2.360597,-9.950102,-9.772507,9.513313,-1.189735,-2.173528,-5.639918,3.400010,7.640867,-3.189187,-1.511029,-1.292705,-0.612394,-6.469077,3.268488,-8.065395,-8.922367,-4.084050,-7.344535,-3.628192,9.818145,-8.309744,-6.236997,4.224403,3.159243,6.913869,3.302888,-8.143231,6.227004,-5.480342,9.380666,8.807096,6.825483,-2.408352,2.999702,-3.726442,5.558485,-7.440747,1.706929,3.923467,-9.074687,-2.037450,-8.828025,3.493159,-2.326118,4.442307,1.406825,2.943876,-2.135786,-4.657203,6.685101,-1.734978,1.925704,-8.760633,3.484806,5.711661,0.220054,6.954160,-3.366790,2.267506,-4.308631,-2.971690,7.138646,-4.689994,6.294460,-6.643726,-3.835271,3.749106,3.738528,-8.558793,-5.525311,-2.697219,5.358638,7.457543,6.356480,-2.852306,5.638587,1.459592,3.425842,-0.959080,-5.402153,4.081635,-8.592237,-2.913952,-3.840523,-5.900925,3.226821,-6.194018,-3.432307,-5.266252,8.605767,1.857221,-3.280103,2.576879,-5.774645,-5.049476,-1.421580,9.408137,9.364113,2.342640,-6.789865,-3.175775,-5.302479,9.349348,-5.831839,-6.924500,-8.828545,2.579913,-9.157070,-5.837125,-7.135628,3.523152,-9.468064,4.040744,9.203350,-3.381389,-9.705246,9.853461,5.509779,3.675582,-1.286446,1.677275,2.277899,4.868980,-6.674272,1.229162,4.308625,5.859593,2.611223,2.850255,8.853120,2.361284,-1.621358,6.992354,0.715875,9.696276,-8.764159,-0.921092,0.743712,-7.873264,-2.841552,1.655452,-0.666153,3.036877,7.387723,-7.891379,-9.772357,6.480635,-4.155203,2.722103,1.903171,-6.233904,3.738284,-6.417896,-2.143988,-3.222047,-2.254625,-4.622366,1.938289,-1.639233,-3.823351,2.862539,-2.726163,1.151237,2.284462,-2.190887,-9.012055,2.087257,-0.878943,-6.531305,-1.237130,4.183856,-5.754575,5.621132,2.181362,0.958632,7.405608,1.343976,7.853192,-7.231965,7.959648,4.694130,6.915569,4.921052,-6.820301,5.501949,3.928812,5.212865,-2.339339,9.076901,4.281753,-3.083719,0.029942,-9.732890,-5.616941,-1.158951,-0.561715,2.713226,-4.601339,8.594987,1.012938,3.576198,7.475298,-2.465045,7.891765,6.718183,-7.654947,3.345222,5.242305,-1.273261,9.264197,5.592708,8.723687,0.061234,-7.618882,-5.140596,8.058766,-8.976653,9.312305,8.495137,-1.656544,5.967144,-3.356027,-5.369094,-4.906959,7.194271,7.444010,3.918253,-8.796537,-2.845532,3.769245,-9.584539,-0.833197,4.046400,9.953596,7.879303,-3.658031,7.780721,5.272887,-8.996278,-3.300092,7.607290,2.167604,-4.543877,-4.069833,-6.600980,-7.528363,-3.937607,0.691478], dtype = "float32")#candidate|2538|(1152,)|const|float32
call_2537 = relay.TupleGetItem(func_2247_call(relay.reshape(const_2538.astype('float32'), [1152,])), 2)
call_2539 = relay.TupleGetItem(func_2249_call(relay.reshape(const_2538.astype('float32'), [1152,])), 2)
func_2247_call = mod.get_global_var('func_2247')
func_2249_call = mutated_mod.get_global_var('func_2249')
call_2558 = relay.TupleGetItem(func_2247_call(relay.reshape(call_2537.astype('float32'), [1152,])), 3)
call_2559 = relay.TupleGetItem(func_2249_call(relay.reshape(call_2537.astype('float32'), [1152,])), 3)
output = relay.Tuple([call_2535,call_2537,const_2538,call_2558,])
output2 = relay.Tuple([call_2536,call_2539,const_2538,call_2559,])
func_2562 = relay.Function([], output)
mod['func_2562'] = func_2562
mod = relay.transform.InferType()(mod)
output = func_2562()
func_2563 = relay.Function([], output)
mutated_mod['func_2563'] = func_2563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_2613 = relay.TupleGetItem(func_2402_call(), 0)
call_2614 = relay.TupleGetItem(func_2404_call(), 0)
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_2620 = func_2502_call()
call_2621 = func_2502_call()
output = relay.Tuple([call_2613,call_2620,])
output2 = relay.Tuple([call_2614,call_2621,])
func_2625 = relay.Function([], output)
mod['func_2625'] = func_2625
mod = relay.transform.InferType()(mod)
output = func_2625()
func_2626 = relay.Function([], output)
mutated_mod['func_2626'] = func_2626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_2632 = relay.TupleGetItem(func_2402_call(), 0)
call_2633 = relay.TupleGetItem(func_2404_call(), 0)
func_631_call = mod.get_global_var('func_631')
func_636_call = mutated_mod.get_global_var('func_636')
const_2649 = relay.const([-7.959327,9.724762,-8.827870,-9.977343,-7.186551,3.703462,-3.709335,7.795116,4.045867,-3.445219,-9.990856,2.132711,2.728609,-3.033730,3.913415,-1.590998,5.123166,-8.151035,4.997434,0.147349,-6.795595,2.871697,-8.489173,2.963810,5.685957,9.317336,5.437112,-4.425176,-8.557488,-3.075976,-7.670507,6.079421,-3.707102,9.902457,-0.629623,0.331764,1.657098,-9.037920,-9.596082,6.557419,4.734126,3.530206,6.499536,8.817610,-0.005478,4.087310,-2.428712,-1.163478,6.888583,-5.414502,5.722000,-2.200259,-8.354918,-6.043546,-9.077367,5.128849,-1.121016,4.762136,-2.061217,4.878240,-6.924018,6.223724,0.312568,8.342409,7.265391,-6.213239,-7.962016,-6.704597,3.478062,5.396010,-0.969274,7.155020,9.502660,8.810089,7.466320,-0.799439,6.845791,-9.749176,-6.068251,3.245506,4.279854,-5.497722,1.459392,4.021130,3.745372,-5.599257,9.067012,-8.997883,-4.180728,-2.508477,-8.992174,8.427836,5.266791,-9.284056,-7.201807,7.067603,3.406828,0.889429,-9.051060,-0.721774,5.597215,-3.371090,-1.235670,4.496518,-7.814404,9.626296,-9.475456,-8.052273,-6.433479,1.239700,5.874474,2.536252,-8.381119,8.244976,7.074870,-3.746883,-6.569345,1.856962,6.259801,-4.410429,-8.826980,-2.693409,-4.340841,-8.403685,1.804346,9.433109,3.150818,-2.219179,6.778744,-7.024796,8.494224,2.720930,5.851093,-5.795946,6.693397,-9.473398,-5.404284,2.780757,-6.094043,-8.535925,7.169473,-9.098623,-4.030175,0.572503,-3.848159,-7.902564,-1.521172,5.063118,-3.050872,4.750811,-6.677923,3.084189,-1.347053,-3.876327,4.642256,8.257391,-6.244948,4.834054,-5.328566,5.697815,-0.031752,-4.665048,2.965330,2.775618,0.800747,-4.297749,-9.364346,4.283727,-7.077958,3.047654,-9.299533,-2.835769,-0.964589,2.208062,-1.363970,8.150661,-7.008522,-0.622793,-3.066639,6.177587,-8.594987,6.908552,7.134278,1.064462,-3.912345,3.661284,4.160083,-5.103392,3.595557,-5.544618,-8.848999,1.925049,7.161848,-4.101910,5.203691,-3.603294,3.142250,-8.351810,-0.167972,-0.283691,1.258516,0.806369,-4.896528,-8.067807,7.950631,7.535757,4.161442,-8.346035,-3.147683,-2.309532,-7.644238,8.483825,-2.531398,-3.389357,-4.916216,-2.661343,4.103855,-8.936635,2.913629,6.119829,-8.538959,-3.046322,1.012257,-9.553831,2.886464,9.663427,5.741692,-4.218394,6.967964,-3.626179,6.326378,0.378866,-9.112641,-3.032755,-1.192873,-5.011559,4.922461,-4.119270,9.271528,-1.721461,4.260858,-8.851219,5.503509,8.207412,-4.100962,-8.245660,-9.641289,-9.273798,9.731615,-6.604723,-0.586618,-8.882883,1.675734,2.718644,-2.585434,3.859089,6.713531,-3.720622,-2.827311,2.204649,-5.758293,4.535970,8.516126,6.340300,-0.539469,6.750312,1.388804,-8.303696,-2.401761,2.690432,-8.837134,5.705978,3.131041,-8.546238,6.815185,-8.855517,5.399911,-8.187423,7.010711,1.345326,5.042213,-8.825953,0.690885,9.298941,-1.390413,-9.200481,8.606959,0.848826,4.634048,9.716567,6.800015,-1.251893,6.374975,-8.147813,4.227869,-5.524918,-3.399168,3.535380,-1.897234,4.987768,9.275516,3.354428,6.315452,2.752774,-1.185559,1.583777,-7.029893,-7.889392,-0.476897,-2.594860,-4.506318,-9.019704,-8.368978,-8.704601,-3.347206,3.414495,4.571555,3.366769,4.462799,-0.687754,3.800792,-9.016718,3.272458,3.250475,6.375121,5.403082,-0.406912,-0.111649,3.515286,0.581082,-7.232749,-9.071347,4.096042,5.517053,-3.594041,-1.377629,6.022411,-5.646186,1.595987,3.166197,0.777287,4.575622,-9.678402,-3.395061,-1.917948,-3.155785,8.674950,0.381842,-9.696421,0.018918,-7.558214,-5.482043,-2.501325,-0.549641,-8.798253,-4.479388,4.714242,6.383815,0.075911,5.031517,-1.266502,9.735696,-2.391551,-0.085352,2.877161,-1.983499,-2.331628,2.453362,2.315126,-6.655271,4.878455,6.452353,-8.003251,8.086497,8.356833,-0.264115,-6.962283,9.685951,-7.225430,1.793089,8.647058,5.577526,-1.853813,1.371403,-8.820400,7.366001,-9.469765,-7.200802,1.628686,5.391295,7.720413,-5.420662,2.619824,-2.637864,-6.300623,5.724083,0.450663,4.196668,4.170102,0.406711,-3.047263,-3.634839,-4.368884,-5.530556,-1.278362,-9.672531,1.671071,6.450103,-4.820600,-0.485847,8.877108,-6.573503,-6.836885,-6.069976,-6.135006,9.876199,-2.601696,-7.484960,8.245135,-4.070690,-0.387008,6.973987,-0.509700,-0.982644,-4.055124,9.050933,-4.922436,7.500690,8.964417,-3.238603,9.912815,-4.966444,2.231339,-6.470819,5.798447,-5.864999,7.034715,6.428805,-0.824118,-0.088799,-0.858333,-2.892802,-2.517038,6.169513,7.099832,1.263608,-0.604333,-3.910579,-0.302179,-0.504962,-7.890751,5.167254,-9.427762,6.754536,-0.345837,6.781536,4.084427,0.317462,9.014315,9.707134,6.122004,-0.687119,-9.878598,0.476822,4.712699,6.072315,9.289434,-2.553772,9.342684,-2.033800,7.623531,3.969820,-2.979719,-6.306387,9.387987,-0.295960,7.312785,-9.496816,-3.900877,-8.821854,7.017429,9.663804,3.090234,-4.133851,6.795283,-5.598476,5.994216,5.002378,4.891492,2.052622,9.484202,9.474634,-6.315200,-3.703143,3.557107,0.738491,-3.261620,2.285973,-4.121520,4.438009,0.493824,-7.986906,8.113437,-4.357106,-2.034488,1.605742,1.205436,-8.683328,7.025260,-4.690741,9.492860,0.515459,-9.213143,0.825218,8.900382,-0.820002,4.215927,4.189041,-6.732761,4.741064,6.399187,-6.684804,6.612776,6.202973,-1.428193,4.176060,8.969868,2.720691,-3.547727,-6.527054,5.556998,-1.593387,8.886361,0.097830,8.084602,-9.310421,-4.546958,5.459790,2.711935,-2.342021,7.026642,-1.809150,-9.827843,-7.006269,-0.917029,-2.866625,-8.952802,-8.183165,-8.195905,7.374607,-1.782414,2.338943,3.098338,-1.535062,2.426252,-5.147024,7.601074,7.239523,-8.910452,-4.160184,-9.423366,5.733179,9.270120,-3.680708,5.919398,3.526497,-8.726113,-4.582444,4.940425,-5.493617,7.702307,6.960624,9.741577,0.086365,4.057509,1.520609,-0.676412,-2.068908,-6.574118,-4.533884,-7.692572,-7.521841,-7.267816,-0.770451,1.985012,-4.486429,9.261923,5.505192,-8.441587,7.700759,-2.767156,0.440280,9.744807,-9.707582,-5.574452,9.266536,-6.107863,9.822250,0.295028,2.458590,3.138027,7.246928,7.068668,6.259949,7.860884,1.599221,2.963799,0.858803,-0.726415,7.838759,-1.499867,-0.054971,-9.992233,3.551370,0.273412,-2.328007,-7.143473,-6.772679,0.160489,4.858831,-2.799867,-9.491690,0.629709,-6.434684,-0.241668,-0.452259,-1.500907,7.661906,6.940329,-0.560748,8.192027,0.558147,5.513333,-4.395994,8.957259,1.745471,-6.895815,-9.301686,2.790881,-6.176228,-1.892207,-8.956025,8.517283,1.175089,-1.003240,8.614135,-6.190697,8.142133,-0.917030,-7.606830,8.976056,5.251580,-7.881559,6.515651,-3.621479,0.904965,8.287294,-8.010571,6.694568,2.282855,2.244931,-8.032143,2.807658,8.285547,6.439615,4.750643,-3.496928,-0.511859,-9.191544,-0.733553,2.744477,3.914059,-4.875200,0.010957,4.566381,2.671737,-2.922481,5.838592,-0.848914,6.947527,-9.375316,-4.761072,-9.546808,5.759895,0.645153,4.890902,2.820842,4.493580,-3.370713,-6.830263,8.880611,1.102024,7.536834,8.726295,1.344229,3.419476,4.198974,-4.728151,-2.690586,9.468486,-8.134426,7.629518,0.405573,5.399016,4.744733,-8.556343,3.133097,-0.049247,-4.592245,-0.040967,1.844765,6.343464,-5.765788,-2.073260,-0.412933,-5.298629,-9.024176,-1.998305,-7.001536,-7.281188,5.302526,-4.521848,-6.597260,0.801979,-0.672057,-2.263526,7.365325,-9.724606,-8.788790,7.150413,-2.206197,5.587602,1.952421,1.076631,6.500545,5.064187,-7.637390,6.518314,6.289221,4.226656,1.007473,7.689862,4.703233,-4.885717,-7.361698,-9.359974,8.534917,2.292102,-5.087513,-6.512719,-1.730054,-0.830188,7.974538,9.670129,9.477399,-9.459846,3.953292,7.310344,1.717223,-9.249304,2.561738,2.972357,-0.241183,0.575166,8.299981,-9.035581,-9.733298,-8.097456,-9.644564,-7.070764,-6.205366,-1.611124,-0.604600,-3.152628,0.638467,8.149832,-8.768963,7.468875,8.775867,4.708047,-6.394950,6.294451,-5.858133,-3.292887,2.045827,-1.235641,2.385495,1.887931,7.305923,-6.139851,-8.177003,5.901781,-1.573946,8.990669,-3.997761,-2.545356,-1.419573,7.158183,4.035718,-3.966727,-4.959987,-3.098600,6.508855,8.833784,7.212015,-2.922835,5.121665,-2.504062,-4.421276,0.163120,-8.464245,-7.730481,1.664332,-8.890046,2.776416,-7.146558,1.786043,-9.671634,-3.911707,0.117325,0.769682,-8.735245,-8.075685,-8.645382,-0.082864,9.226061,3.022940,-0.431247,7.245853,9.495509,5.049263,-8.668756,-2.991807,6.856650,-8.785559,-1.555999,-7.451951,-9.584877,-7.770330,-9.219857,-9.530256,4.782733,1.635085,2.521707,-5.465444,6.876653,-3.305349,8.802267,-9.629508,8.179554,5.435839,-2.614639,-4.566579,-3.607115,3.969044,-9.250465,-2.115550,1.203213,8.135397,-0.478352,1.917664,4.518436,8.383131,-3.747663,2.176642,-6.948624,-6.076026,6.377961,0.306618,9.458469,-8.414305,2.053689,4.406262,-6.379603,7.961898,8.597061,-4.311657,-1.905490,1.317198,-1.162400,-0.372495,5.269270,9.124800,-6.864683,6.471354,-8.078326,1.031175,-4.720870,-0.308647,2.216674,-7.090059,1.481894,4.438169,-7.125901,-1.192388,7.131246,-3.479771,9.475938,4.118901,-3.615411,0.222046,-6.946974,-7.200500,-7.506344,1.557239,-5.348786,-2.462377,2.715170,5.437072,-7.259192,-2.926884,4.738924,-9.958070,-1.163369,-8.812832,-9.981379,7.724140,-9.566372,-3.126063,1.214776,-1.211996,6.970913,1.982602,-9.465061,-0.622016,-7.163471,-2.200948,0.699134,3.195051,1.737716,1.354639,2.977595,-8.865575,-4.371054,-1.260993,7.852614,-0.312083,0.414172,1.611694,-2.576168,-0.736213,-6.355484,-4.024142,-7.050144,1.376326,4.148094,1.195518,-1.069303,-7.159317,-5.927297,-5.724905,8.133079,-1.980081,-5.818692,-0.798092,-6.350804,1.170717,-5.098137,-1.663117,9.491192,-0.616250,-7.521900,-0.350488,9.059894,-7.055257,6.843389,7.818444,4.084248,-2.018565,6.493048,-9.120994,8.681130,-2.273210,-3.594300,-2.630968,5.351589,-6.706653,1.691692,-8.622975,-9.195345,-3.891021,1.644235,-1.320006,-5.438652,-5.861295,-1.315807,4.988717,-4.123686,8.395009,-8.769027,7.144858,-2.122292,-5.559308,-5.424805,-9.869802,8.189990,-7.492778,9.020320,5.305800,1.311603,6.187918,-1.031377,-7.926386,2.930195,2.011480,9.747293,2.571090,7.032241,7.525666,-7.478206,-5.894551,5.017370,-9.257703,4.244828,-9.060056,2.997086,-1.470917,-3.202057,-2.373847,-6.631393,7.986283,-6.373753,4.616489,-2.921296,1.219674,8.219094,-8.807451,5.234728,4.012219,-5.701287,2.363212,9.446316,-0.611427,-6.095243,1.710312,-7.513146,1.461979,9.466893,-0.712313,8.350036,-1.232665,9.157028,7.511957,6.857546,-6.303039,-9.177035,3.527435,9.516242,0.463193,4.149341,5.882188,-8.738214,-9.301625,4.269870,9.009030,0.069144,3.103329,8.317019,6.423241,6.729649,-8.249840,1.527642,-5.975433,4.592742,1.448089,-0.199429,6.045408,1.060168,6.230804,-0.489386,0.105856,-8.297455,1.103855,-7.171498,8.472261,-7.433095,7.107508,1.367450,-3.708530,-0.417832,2.337665,-7.881318,2.845081,5.179328,5.399066,6.859322,5.683411,2.843182,9.382464,1.211256,-8.361995,5.321364,6.603187,0.069504,6.659012,3.027924,-9.678853,2.336298,5.999813,-0.523395,4.908839,-8.847664,-5.603313,7.490555,1.352150,-4.374731,-6.490749,4.861914,-7.297859,7.405523,-2.532210,9.455299,0.599315,-3.373970,3.816287,6.863151,4.199154,5.402577,2.917757,2.175040,8.773161,-2.772020,7.616758,7.412328,-7.704496,-9.351246,-3.854250,-6.655837,-0.064146,-4.402680,6.207238,-5.742603,4.100128,-6.343595,-4.703095,7.509427,1.293991,3.524208,-8.259129,8.277724,-9.245698,9.038588,8.398786,-6.393863,5.713983,6.922180,-4.369759,9.132251,2.382846,-0.702332,2.186867,7.772086], dtype = "float32")#candidate|2649|(1152,)|const|float32
var_2650 = relay.var("var_2650", dtype = "uint16", shape = (180,))#candidate|2650|(180,)|var|uint16
call_2648 = relay.TupleGetItem(func_631_call(relay.reshape(const_2649.astype('float32'), [16, 12, 6]), relay.reshape(var_2650.astype('uint16'), [180,]), relay.reshape(var_2650.astype('uint16'), [5, 6, 6]), ), 3)
call_2651 = relay.TupleGetItem(func_636_call(relay.reshape(const_2649.astype('float32'), [16, 12, 6]), relay.reshape(var_2650.astype('uint16'), [180,]), relay.reshape(var_2650.astype('uint16'), [5, 6, 6]), ), 3)
output = relay.Tuple([call_2632,call_2648,const_2649,var_2650,])
output2 = relay.Tuple([call_2633,call_2651,const_2649,var_2650,])
func_2655 = relay.Function([var_2650,], output)
mod['func_2655'] = func_2655
mod = relay.transform.InferType()(mod)
mutated_mod['func_2655'] = func_2655
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2656 = relay.var("var_2656", dtype = "uint16", shape = (180,))#candidate|2656|(180,)|var|uint16
func_2655_call = mutated_mod.get_global_var('func_2655')
call_2657 = func_2655_call(var_2656)
output = call_2657
func_2658 = relay.Function([var_2656], output)
mutated_mod['func_2658'] = func_2658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_2660 = func_2502_call()
call_2661 = func_2502_call()
func_1079_call = mod.get_global_var('func_1079')
func_1083_call = mutated_mod.get_global_var('func_1083')
const_2667 = relay.const(True, dtype = "bool")#candidate|2667|()|const|bool
var_2668 = relay.var("var_2668", dtype = "bool", shape = (1404,))#candidate|2668|(1404,)|var|bool
call_2666 = relay.TupleGetItem(func_1079_call(relay.reshape(const_2667.astype('bool'), []), relay.reshape(var_2668.astype('bool'), [12, 9, 13]), ), 0)
call_2669 = relay.TupleGetItem(func_1083_call(relay.reshape(const_2667.astype('bool'), []), relay.reshape(var_2668.astype('bool'), [12, 9, 13]), ), 0)
func_2247_call = mod.get_global_var('func_2247')
func_2249_call = mutated_mod.get_global_var('func_2249')
var_2690 = relay.var("var_2690", dtype = "float32", shape = (1152,))#candidate|2690|(1152,)|var|float32
call_2689 = relay.TupleGetItem(func_2247_call(relay.reshape(var_2690.astype('float32'), [1152,])), 1)
call_2691 = relay.TupleGetItem(func_2249_call(relay.reshape(var_2690.astype('float32'), [1152,])), 1)
output = relay.Tuple([call_2660,call_2666,const_2667,var_2668,call_2689,var_2690,])
output2 = relay.Tuple([call_2661,call_2669,const_2667,var_2668,call_2691,var_2690,])
func_2696 = relay.Function([var_2668,var_2690,], output)
mod['func_2696'] = func_2696
mod = relay.transform.InferType()(mod)
var_2697 = relay.var("var_2697", dtype = "bool", shape = (1404,))#candidate|2697|(1404,)|var|bool
var_2698 = relay.var("var_2698", dtype = "float32", shape = (1152,))#candidate|2698|(1152,)|var|float32
output = func_2696(var_2697,var_2698,)
func_2699 = relay.Function([var_2697,var_2698,], output)
mutated_mod['func_2699'] = func_2699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_2843 = relay.TupleGetItem(func_2131_call(), 0)
call_2844 = relay.TupleGetItem(func_2132_call(), 0)
output = relay.Tuple([call_2843,])
output2 = relay.Tuple([call_2844,])
func_2860 = relay.Function([], output)
mod['func_2860'] = func_2860
mod = relay.transform.InferType()(mod)
mutated_mod['func_2860'] = func_2860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2860_call = mutated_mod.get_global_var('func_2860')
call_2861 = func_2860_call()
output = call_2861
func_2862 = relay.Function([], output)
mutated_mod['func_2862'] = func_2862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_2873 = relay.TupleGetItem(func_2625_call(), 1)
call_2874 = relay.TupleGetItem(func_2626_call(), 1)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_2875 = relay.TupleGetItem(func_2402_call(), 0)
call_2876 = relay.TupleGetItem(func_2404_call(), 0)
output = relay.Tuple([call_2873,call_2875,])
output2 = relay.Tuple([call_2874,call_2876,])
func_2883 = relay.Function([], output)
mod['func_2883'] = func_2883
mod = relay.transform.InferType()(mod)
output = func_2883()
func_2884 = relay.Function([], output)
mutated_mod['func_2884'] = func_2884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2883_call = mod.get_global_var('func_2883')
func_2884_call = mutated_mod.get_global_var('func_2884')
call_2944 = relay.TupleGetItem(func_2883_call(), 1)
call_2945 = relay.TupleGetItem(func_2884_call(), 1)
var_2956 = relay.var("var_2956", dtype = "float32", shape = (12, 6, 10))#candidate|2956|(12, 6, 10)|var|float32
bop_2957 = relay.floor_mod(call_2944.astype('float64'), relay.reshape(var_2956.astype('float64'), relay.shape_of(call_2944))) # shape=(12, 6, 10)
bop_2960 = relay.floor_mod(call_2945.astype('float64'), relay.reshape(var_2956.astype('float64'), relay.shape_of(call_2945))) # shape=(12, 6, 10)
func_2860_call = mod.get_global_var('func_2860')
func_2862_call = mutated_mod.get_global_var('func_2862')
call_2967 = relay.TupleGetItem(func_2860_call(), 0)
call_2968 = relay.TupleGetItem(func_2862_call(), 0)
bop_2972 = relay.floor_divide(call_2967.astype('float64'), relay.reshape(var_2956.astype('float64'), relay.shape_of(call_2967))) # shape=(12, 6, 10)
bop_2975 = relay.floor_divide(call_2968.astype('float64'), relay.reshape(var_2956.astype('float64'), relay.shape_of(call_2968))) # shape=(12, 6, 10)
func_1120_call = mod.get_global_var('func_1120')
func_1125_call = mutated_mod.get_global_var('func_1125')
const_2985 = relay.const([-9.855236,-1.094259,7.869628,-1.042758,3.675738,-7.090527,9.361557,3.995018,-1.362663,2.100809,-8.914268,-6.409808,-2.967094,5.133525,2.139999,-9.409920,7.225488,-9.402050,-2.511300,2.665712,-5.215815,-1.662224,-7.718842,-8.809672,-2.558561,-4.139639,0.269742,3.545633,5.917602,4.401205,1.416621,6.770964,-8.957779,-6.175474,-2.681554,2.456044,6.970240,-8.615392,8.722951,3.598203,-3.746572,-1.832958,-9.146287,-0.498379,4.576647,2.419216,6.947613,3.273113,-5.240932,7.051589,9.587482,-5.369479,-9.615551,-2.347596,5.442419,9.820852,-8.174801,5.772934,-7.929610,-9.408460,3.359200,-5.471661,-7.937952,3.228104,3.323975,-2.083314,2.246655,-0.002796,2.583265,7.040761,-6.098956,9.841021,9.527202,1.717033,-2.041688,3.326381,9.815090,-9.555582,0.695654,6.973520,-3.927109,7.676141,-2.037784,6.105465,-6.167671,-9.599958,-5.695501,9.208126,-8.428336,7.143573,6.446827,-2.002213,-5.635946,-8.048288,-4.681934,6.752527,7.036419,-4.431264,-0.997009,-8.324823,2.537973,5.687668,-7.058394,1.475635,2.416271,3.003363,9.361469,-1.309865,-8.709058,8.107291,-9.050820,-9.123449,9.499384,4.145997,-6.033167,-7.921653,-7.145007,5.491475,9.840594,4.651338,9.738298,7.073705,-7.723009,1.202774,-4.044331,-9.759022,2.819155,4.903541,2.221597,-6.048664,-8.137297,9.590404,-9.836681,8.001245,6.233880], dtype = "float32")#candidate|2985|(135,)|const|float32
var_2986 = relay.var("var_2986", dtype = "float32", shape = (1152,))#candidate|2986|(1152,)|var|float32
const_2987 = relay.const([4,6,-5,5,9,3,2,-3,-6,-2,10,3,6,3,-9,4,8,7,5,5,8,8,-3,-6,5,-2,-1,-4,7,8,4,9,-2,-7,10,8,3,7,-10,-3,-4,-10,3,3,1,-8,-5,-7,5,1,10,-3,-9,7,5,2,8,-6,6,-1,-3,4,-5,-5,6,4,-7,-9,7,-4,7,-4,10,5,9,6,2,10,-10,-8,10,4,-8,2,8,-2,5,-9,-3,-2,-8,-4,8,-2,8,-7,-1,-4,2,8,5,5,3,-7,-8,-1,-7,1,-9,-6,-10,-5,-3,-1,8,-7,9,-3,5,1,8,2,-6,-3,-3,-4,-1,5,2,9,7,-3,7,9,5,-5,-1,-10,-7,4,1,4,-10,6,-7,2,-2,-10,-10,-2,10,-7,4,10,10,3,1,-5,-8,-3,-7,-7,-1,-9,8,7,9,-1,-1,6,2,-3,9,-5,1,10,-6,-9,7,-9], dtype = "uint16")#candidate|2987|(180,)|const|uint16
call_2984 = relay.TupleGetItem(func_1120_call(relay.reshape(const_2985.astype('float32'), [9, 1, 15]), relay.reshape(var_2986.astype('float32'), [1152,]), relay.reshape(const_2987.astype('uint16'), [180, 1]), ), 3)
call_2988 = relay.TupleGetItem(func_1125_call(relay.reshape(const_2985.astype('float32'), [9, 1, 15]), relay.reshape(var_2986.astype('float32'), [1152,]), relay.reshape(const_2987.astype('uint16'), [180, 1]), ), 3)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_2994 = relay.TupleGetItem(func_261_call(relay.reshape(call_2984.astype('uint16'), [5, 6, 6])), 0)
call_2995 = relay.TupleGetItem(func_263_call(relay.reshape(call_2984.astype('uint16'), [5, 6, 6])), 0)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_2997 = relay.TupleGetItem(func_2402_call(), 0)
call_2998 = relay.TupleGetItem(func_2404_call(), 0)
var_3000 = relay.var("var_3000", dtype = "uint16", shape = (180, 13))#candidate|3000|(180, 13)|var|uint16
bop_3001 = relay.greater_equal(call_2984.astype('bool'), var_3000.astype('bool')) # shape=(180, 13)
bop_3004 = relay.greater_equal(call_2988.astype('bool'), var_3000.astype('bool')) # shape=(180, 13)
func_1295_call = mod.get_global_var('func_1295')
func_1301_call = mutated_mod.get_global_var('func_1301')
const_3021 = relay.const([-5.064968,2.979354,0.842969,-6.278053,-1.843121,-7.920314,7.385407,-2.172971,-3.933072,5.940705,0.253118,-0.288017,-0.647294,-7.707910,2.957537,-3.930129,-9.497906,2.420790,7.612144,4.178755,1.689879,-3.537272,7.679172,9.036092,-5.251962,-8.224417,0.743009,-6.634961,1.443232,9.791336,6.000327,-6.016892,4.120038,6.107951,7.388430,-9.544668,3.644950,-5.400969,7.914941,-2.162367,-2.944051,7.031059,2.402384,2.408492,7.268255,7.605909,-2.235903,-9.625149,3.396961,-1.903748,0.014925,8.379898,-0.789389,9.058333,9.658876,1.422613,-0.764609,5.707936,-7.366539,-9.563154,5.504205,-4.062909,-5.640152,-2.933263,8.047988,-5.133355,6.746660,9.337547,2.574965,-9.381102,-2.101780,-7.771010,-7.381165,-2.077437,-3.014976,-9.038081,-6.220491,9.326611,-7.635773,-2.477057,8.466129,-2.561157,-6.554038,-5.614119,-2.588812,-3.686548,-8.101428,5.256095,8.269735,0.031855,-4.691991,3.660600,-6.260447,7.648438,-6.455034,-3.140971,3.215536,8.793365,-3.850496,8.716675,-8.556591,3.927471,4.089839,2.025692,-2.222013,-8.565614,7.966545,5.830448,9.894037,-4.176700,-2.226251,4.836861,5.777208,5.017101,-4.297517,-8.830396,1.037789,6.415570,-0.716378,6.329542,7.875431,6.446586,5.196913,-7.394924,-0.760715,8.939894,-8.518717,-5.672181,8.548242,7.548798,-7.829046,-3.009839,-3.864682,-2.175181,-1.115565,9.480397,-4.124358,-2.769287,-4.166152,-1.150558,4.359378,4.730225,-2.834404,5.123215,-6.144821,8.716378,-1.218386,-8.766464,7.930281,8.723422,-4.472338,9.204234,-3.855070,-9.342117,-1.734382,5.260228,-8.034489,4.356292,-6.602290,-4.441965,-3.253709,3.400977,8.906404,0.616454,7.814757,5.244124,7.193736,-1.805605,-2.372193,-2.440122,0.405730,9.877436,5.102769,-0.647457,8.509947,-0.794342,-6.582653,8.699284,7.800037,-2.206145,5.334249,-7.026397,-5.938379,-5.506318,7.199826,4.095595,-5.869402,5.675578,-7.782652,4.252616,-9.823989,5.366913,-7.080066,8.428168,1.707809,-8.220886,2.981713,2.377267,3.076644,-7.409057,6.257587,8.379608,-2.285153,0.776064,-1.567414,2.440819,-7.210917,4.992585,1.988117,-8.060633,-5.522844,9.425150,0.221386,3.452054,0.487099,3.201173,8.011027,-8.251508,6.159092,-6.250082,7.064471,5.170932,-0.734909,-0.409677,7.983813,-4.977055,2.858019,7.384769,4.698205,6.827457,-7.833441,8.439485,9.281014,-5.284686,2.735264,-9.530267,-8.218928,-2.259743,-6.617744,-6.944047,2.771848,0.463029,-0.715478,1.858316,3.048253,-3.060039,4.591769,2.742993,-2.692880,-2.658027,0.956763,-8.523080,-4.009723,-5.280335,4.231152,-9.553550,-7.959635,4.847897,-8.819230,-0.324651,5.822426,3.602834,-2.365163,9.867825,-7.518777,-4.675219,-2.698072,8.800562,3.449238,7.897337,-3.042226,0.416336,6.507336,-6.696845,3.235132,2.723725,8.446433,0.646120,0.510981,-5.398118,-6.329981,3.116806,0.292394,1.325239,8.677248,0.704013], dtype = "float32")#candidate|3021|(286,)|const|float32
var_3022 = relay.var("var_3022", dtype = "bool", shape = ())#candidate|3022|()|var|bool
const_3023 = relay.const([False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,False,False,True], dtype = "bool")#candidate|3023|(1404,)|const|bool
call_3020 = relay.TupleGetItem(func_1295_call(relay.reshape(const_3021.astype('float32'), [2, 13, 11]), relay.reshape(const_2987.astype('uint16'), [180,]), relay.reshape(var_3022.astype('bool'), []), relay.reshape(const_3023.astype('bool'), [12, 9, 13]), ), 2)
call_3024 = relay.TupleGetItem(func_1301_call(relay.reshape(const_3021.astype('float32'), [2, 13, 11]), relay.reshape(const_2987.astype('uint16'), [180,]), relay.reshape(var_3022.astype('bool'), []), relay.reshape(const_3023.astype('bool'), [12, 9, 13]), ), 2)
uop_3031 = relay.exp(call_2944.astype('float64')) # shape=(12, 6, 10)
uop_3033 = relay.exp(call_2945.astype('float64')) # shape=(12, 6, 10)
func_2883_call = mod.get_global_var('func_2883')
func_2884_call = mutated_mod.get_global_var('func_2884')
call_3037 = relay.TupleGetItem(func_2883_call(), 0)
call_3038 = relay.TupleGetItem(func_2884_call(), 0)
output = relay.Tuple([bop_2957,bop_2972,const_2985,var_2986,const_2987,call_2994,call_2997,bop_3001,call_3020,const_3021,var_3022,const_3023,uop_3031,call_3037,])
output2 = relay.Tuple([bop_2960,bop_2975,const_2985,var_2986,const_2987,call_2995,call_2998,bop_3004,call_3024,const_3021,var_3022,const_3023,uop_3033,call_3038,])
func_3049 = relay.Function([var_2956,var_2986,var_3000,var_3022,], output)
mod['func_3049'] = func_3049
mod = relay.transform.InferType()(mod)
mutated_mod['func_3049'] = func_3049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3049_call = mutated_mod.get_global_var('func_3049')
var_3051 = relay.var("var_3051", dtype = "float32", shape = (12, 6, 10))#candidate|3051|(12, 6, 10)|var|float32
var_3052 = relay.var("var_3052", dtype = "float32", shape = (1152,))#candidate|3052|(1152,)|var|float32
var_3053 = relay.var("var_3053", dtype = "uint16", shape = (180, 13))#candidate|3053|(180, 13)|var|uint16
var_3054 = relay.var("var_3054", dtype = "bool", shape = ())#candidate|3054|()|var|bool
call_3050 = func_3049_call(var_3051,var_3052,var_3053,var_3054,)
output = call_3050
func_3055 = relay.Function([var_3051,var_3052,var_3053,var_3054,], output)
mutated_mod['func_3055'] = func_3055
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3068 = relay.const([[[7.477680,-8.845571,7.265494,7.425039,4.667740,1.628741,-6.413905],[-9.137011,9.159583,-0.012609,-2.378989,-5.906025,8.527139,-6.018793],[4.592384,-0.914413,-4.560145,-9.841094,1.709173,4.310877,-0.113989],[-9.204142,-2.665241,2.669024,-2.051566,-6.902525,-1.189313,-4.189711],[2.650524,1.171049,-4.440858,5.974199,-8.499955,6.103403,5.652917],[1.426301,7.140047,-4.080814,-0.034560,4.628751,6.637854,-3.112724],[-3.666666,-7.135999,4.970081,9.565089,6.952187,-8.604694,-1.375107],[8.624591,-9.068698,-1.634749,-5.319393,-4.816499,-7.771521,8.493117]]], dtype = "float32")#candidate|3068|(1, 8, 7)|const|float32
uop_3069 = relay.cosh(const_3068.astype('float32')) # shape=(1, 8, 7)
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_3071 = func_2502_call()
call_3072 = func_2502_call()
bop_3078 = relay.equal(uop_3069.astype('bool'), relay.reshape(const_3068.astype('bool'), relay.shape_of(uop_3069))) # shape=(1, 8, 7)
func_631_call = mod.get_global_var('func_631')
func_636_call = mutated_mod.get_global_var('func_636')
const_3089 = relay.const([-6.394126,4.685550,9.607301,-3.595896,0.491853,-8.071396,-1.440941,-6.632408,-2.534097,8.986122,-3.000173,7.701568,-4.691917,-9.124433,8.941312,-0.171579,-0.556767,-7.345762,-5.896621,-8.601774,-6.766383,-5.656663,-6.090271,-2.721499,-1.911246,-1.771554,0.788851,0.934459,2.937868,3.742973,-1.455194,-8.534829,-7.821566,6.989397,-5.061047,-7.173429,-1.718270,6.491891,-9.056213,-1.885720,4.776567,9.577501,-2.182701,-6.562892,8.851373,-9.871432,0.703653,-4.182034,2.795319,3.899568,5.623407,-1.450503,-6.820624,-4.821900,4.683311,0.343036,2.807646,0.421653,-4.517351,-1.206130,-3.374317,1.768336,8.548183,7.947311,1.687931,-2.976938,-0.165082,2.212183,0.440168,4.354568,-2.305088,3.975659,-1.598285,2.830941,8.005013,-4.343369,7.071680,0.232509,0.157001,0.179523,2.930468,0.289263,5.219075,-5.160344,-5.180152,1.362500,3.200870,4.243197,-6.959313,-1.537005,-5.741807,0.781056,-9.175703,-5.051722,8.117084,6.202259,-1.449175,-2.509041,3.307676,-0.535957,6.997581,-7.264343,-9.196609,-3.881803,-5.216597,-0.957195,0.416494,-8.156708,9.002116,3.800515,6.770907,1.633597,6.036585,5.157600,6.213264,-4.167332,0.981949,8.476278,-0.201081,-7.083380,-3.439371,0.686899,-9.625286,8.480484,5.919651,-5.285674,6.718498,-0.769934,-2.596242,1.111745,1.919598,-9.724930,-7.434911,-5.515056,1.633231,-2.404273,-5.020874,5.877960,9.814907,-5.786831,4.017901,0.819347,-6.783464,2.348453,6.594433,-3.325999,-8.899776,-4.512100,-6.994979,-5.117005,8.115398,4.650999,-8.107705,6.483960,-4.912311,-7.369264,-5.640240,-9.183301,9.818943,4.578242,2.882586,1.884170,-3.532828,-5.535257,4.707042,-9.282920,4.296979,-8.281729,-2.101510,-6.173767,8.083709,-0.399360,-8.133529,-2.682039,-3.895056,0.802911,-0.402881,-8.554692,-9.884664,4.883921,1.208428,-8.566795,-5.992602,-2.791462,-0.344055,3.259931,-9.890564,-4.048671,-8.250297,-9.211417,-1.744129,-3.522029,6.978831,-0.143660,-9.327501,3.557073,1.212885,-3.414649,-6.562913,7.832569,1.770614,-4.361836,-5.700354,2.719263,9.519424,-4.195390,3.739937,-7.551024,1.526417,-8.502445,7.666719,3.445793,3.983981,-4.808590,-5.115860,4.800295,-5.921679,2.995683,-1.973206,9.131288,1.295561,4.444002,8.754987,3.394440,-5.186695,-9.515490,8.913729,5.877162,5.786665,-3.322011,9.172677,-1.603683,9.104009,-0.253616,-8.707276,9.518141,7.438741,-2.909792,2.547091,4.709153,1.989312,2.626330,5.817497,4.254458,-6.262034,2.566274,7.947474,8.069813,2.018572,-8.619182,9.456161,0.923226,4.914242,1.198243,6.871600,-1.591002,-6.402219,3.381331,-2.517164,2.810623,-1.486844,-3.172471,-0.906806,-1.440381,-2.478171,8.006033,1.564178,-6.397769,-7.556398,4.436278,7.884266,-2.724850,5.400936,9.871246,-0.786355,-6.399691,8.476489,1.945965,-7.319927,-6.602241,-2.888721,-4.756295,-7.210782,-7.866313,8.606640,1.568957,-7.591310,-7.836493,4.864885,3.704042,-8.850362,0.395396,9.806676,8.383895,-1.081811,-3.913787,2.003707,-1.412196,8.746633,-9.623009,-5.014752,8.427000,7.883187,-8.818067,-0.172763,0.267989,7.623767,-9.354124,8.563114,-1.375770,9.158329,-1.799384,-2.795781,9.477514,-5.657347,-0.646124,4.274131,5.043475,2.805647,3.805955,6.023675,0.932039,8.609568,0.527048,5.331775,4.794555,-7.710885,-7.480234,-0.079256,3.449220,3.170695,-0.113136,0.638239,-9.410223,5.493122,-6.525079,-2.448300,-5.905593,-5.639634,-7.307595,3.831841,-9.124993,5.699474,-5.635109,-6.290012,-0.987733,1.274567,-5.731694,-5.512801,-1.045970,2.468143,2.372819,-1.443119,6.602885,4.119943,-2.895657,1.880641,3.193449,8.955419,0.960324,3.643548,-2.699041,-9.047050,0.737102,4.176551,-5.587896,1.730742,-5.468571,9.732252,-3.719252,2.631782,-6.437691,4.483894,2.564504,3.869243,8.785617,7.525328,-0.330111,-5.388666,-1.695632,5.759519,-3.631299,-5.393655,-3.624455,3.128494,5.477295,4.300112,9.269524,1.305662,-6.790584,7.520894,4.385091,1.432805,-2.725289,0.112507,0.635821,-1.803418,4.035151,-8.211967,-0.133429,-2.170555,-1.249928,8.049642,9.629279,-8.655954,-0.731199,5.781223,-4.833295,3.374652,-2.095957,-8.616508,6.250894,-2.812843,7.589174,-8.300292,-9.897383,7.543565,-2.432494,-5.719992,1.513467,0.173994,4.416647,4.781717,3.549827,-5.746854,-0.155508,8.693772,9.092027,-7.507304,-1.420734,8.176693,-0.633867,8.095560,0.955051,-5.364127,9.712073,-4.549002,-2.798664,-0.918900,-2.251569,4.691370,7.593776,-7.848485,-4.257094,-5.950401,2.710363,5.529233,-1.656310,1.501014,3.189368,2.782652,4.420365,2.229379,1.201730,-6.308294,-0.011854,-7.898651,-3.070328,2.404249,-7.685533,-0.312896,7.338449,0.130853,-7.761838,1.224077,-2.328818,-1.073119,2.538274,6.227727,-5.804264,-9.378382,3.697281,-0.199438,-3.729818,8.429253,7.718763,-9.364004,1.267365,7.073120,-9.386818,0.177821,5.816167,5.147592,7.675488,0.457922,-8.252125,4.914407,8.747900,6.378314,9.221721,-9.072271,-2.006192,6.513220,-3.697937,-6.590172,2.063039,3.525886,4.219321,2.911215,0.280504,-7.574589,3.551289,7.377494,-5.951263,-9.116671,3.613375,-2.946526,4.196780,-7.036465,-4.041869,8.853344,-9.080599,-5.779510,5.612753,2.622785,9.577520,-1.836909,7.243640,2.049886,-3.525989,7.209153,-5.557160,-7.208739,0.794529,5.175389,2.173033,8.609555,2.425375,6.958647,-8.643740,5.465152,2.642959,-2.578825,9.343416,-7.258841,9.622064,-2.911228,8.653760,0.381582,3.962250,2.872266,9.633748,-4.613855,-8.123474,6.437152,-9.244435,-7.482865,-7.147980,-8.422749,-2.306353,-9.887026,-6.222672,9.699890,4.576595,-7.975090,9.965913,7.485590,8.170057,7.226543,8.988963,-0.480474,0.354573,3.324958,9.577153,-3.494041,-5.989589,1.906077,3.745773,1.634460,8.212345,1.656541,2.657688,-3.540873,-4.758437,-8.569355,-8.900013,-7.552100,-5.552383,-9.613440,9.573789,8.616320,3.607772,2.674305,-4.829491,4.031188,-6.358982,-2.894588,3.348799,-1.496227,0.261000,2.256609,7.070909,1.386071,-1.131701,7.853654,-4.046431,3.273828,9.680632,-9.162561,4.499795,-8.338273,-9.121522,0.804703,3.873120,-9.721743,5.932872,-9.301814,1.048527,-9.124883,7.545947,4.373869,-1.665142,2.930339,9.865473,6.565770,5.300374,4.358313,7.550343,1.030061,-4.213075,3.589015,-4.422447,5.557091,2.023871,5.391000,9.961652,6.443936,0.181039,-2.480239,-8.787436,-1.849320,0.903882,-2.613134,-0.561776,5.968508,6.940860,-3.142979,-2.916943,3.336691,1.089559,2.362166,7.551966,7.020867,7.429063,-2.379195,1.501846,-0.574538,-2.728155,6.875944,-5.413194,3.607448,4.638150,2.970960,8.404186,-1.214781,8.498037,-6.422140,-3.553471,-0.142474,3.652199,6.967763,9.128996,6.806120,-2.737524,-3.711291,2.459145,-8.940324,-6.262424,-9.335416,-8.164033,-0.851268,-0.600920,5.074083,-0.995907,5.146087,-3.094195,4.306807,-3.507448,1.661135,1.802659,6.017108,7.878334,-4.846414,-9.907999,-1.011696,3.120171,-4.763491,3.621615,-5.387356,8.188919,4.200648,-3.328973,2.265690,6.353334,-1.607030,9.910834,9.692026,2.749605,-0.699256,-1.515965,1.777881,2.256739,-3.639820,1.767015,9.409450,-4.756500,-5.638645,6.593397,4.602672,-8.103182,3.075640,8.436118,-8.847710,-7.414548,-9.109141,9.202009,-8.031176,-4.901559,0.433819,7.818497,-6.759491,7.558852,1.151756,5.329572,9.825875,-5.585884,8.091944,5.517933,-6.429358,-1.695681,0.365598,-6.656633,-3.533230,-7.008827,-6.527340,-2.908894,6.843259,8.065780,-0.673121,7.208037,-3.243338,0.186988,2.577100,-2.813303,-1.887646,4.292037,-5.426489,-3.749795,-7.928460,0.746188,-2.850443,8.518072,0.094335,-4.452198,8.047267,-0.680642,9.638752,6.433045,-8.426818,5.694204,-4.007680,-1.335090,-1.622254,-4.038761,4.596539,-4.146208,8.860371,4.999895,-4.379068,6.147771,3.474339,-0.172900,8.653109,-7.890533,7.889046,-0.673299,-7.667238,-5.381248,4.936633,0.635603,-1.479873,5.926512,0.387576,9.934241,-1.098166,-7.325764,-8.120824,4.858471,-1.815574,8.600631,2.076459,-5.012880,6.868440,-7.601052,8.997324,6.195262,0.788369,1.407573,-8.643123,7.454975,3.549482,-9.406255,-7.807816,8.125430,0.937967,-0.010749,5.852100,-1.065953,0.277377,2.511020,-0.413554,0.405994,4.691296,9.820887,8.118095,3.958886,-7.455746,-1.716646,9.566647,6.071543,-1.277872,3.582863,-9.315028,-1.362523,-0.720257,-9.228100,0.587961,3.113755,8.094640,-7.992890,7.502215,4.668806,3.817557,-8.277139,-9.722839,-3.779190,3.217556,-2.911262,4.173742,8.479060,-9.889590,3.002824,2.644797,3.406357,8.311802,9.491066,7.595464,-7.813834,-9.774467,1.061359,-6.914321,-6.223646,3.695331,-2.350330,1.979451,-8.192786,0.018168,2.492829,-4.698959,4.304949,-0.780058,-2.694702,-6.574205,8.893078,6.025070,0.386921,-6.373896,4.619807,-9.686420,-5.623883,-9.359884,5.741358,-1.447302,-6.290358,1.283018,-6.962377,4.347057,1.254865,8.458725,-5.165458,1.802060,7.181100,6.826028,4.177386,-5.110479,-3.307994,3.244712,-4.346797,-6.367908,-5.259445,7.132876,-7.391318,-6.897031,-9.763676,-1.851475,-0.564743,-6.220731,8.017352,3.662194,4.005098,-3.661669,-9.063859,4.656607,-7.350114,3.108005,-0.619941,2.687518,6.446779,-9.057941,-8.370375,5.013096,7.176889,-8.152555,8.034618,7.931632,2.501439,-2.570299,9.148013,-0.178022,-1.602922,6.230846,-0.785276,4.892587,-1.202959,5.288000,-0.885611,6.585110,-1.207574,-7.739026,5.481286,-1.013794,6.851933,-0.953076,1.965167,-5.765340,0.636957,-1.979891,9.094348,4.937645,3.769579,-2.252047,6.787885,6.074893,8.383970,-8.801466,-8.870361,7.202796,1.218993,-2.552751,-7.326793,-8.408644,-4.891800,-4.121821,-5.199223,1.171002,-2.826590,2.961360,-6.341472,-1.954220,-7.682934,-0.769108,1.827158,0.647147,-4.207856,8.825488,-7.766420,-7.038730,-6.169563,-6.125333,-1.857439,3.032491,9.788223,4.721371,2.747418,5.591536,-8.571371,-4.636071,2.665756,-8.912343,-8.659824,4.329749,-0.665445,9.109617,-3.829489,1.456193,-0.388554,7.681165,-7.527421,2.794781,-6.377771,9.828915,-0.214119,5.859235,8.868965,1.954474,2.068612,9.974647,-5.336991,3.714437,-7.611414,-4.165436,6.002658,8.603118,-6.392411,5.181025,9.476750,2.508181,5.574294,-6.532562,-1.668780,-8.591074,-1.369518,2.598506,-2.646823,0.719284,-5.211543,9.648361,6.017329,9.171834,9.410806,3.471135,6.322174,6.825286,6.657760,-6.637547,7.279996,9.744579,-7.106343,0.828232,0.150954,8.923855,-6.516743,2.838762,1.398656,8.415309,-1.616724,-3.436960,8.643914,-7.363272,4.101663,-9.004004,1.193421,-4.551232,9.022015,-4.632503,-0.781581,-4.335803,3.704477,-3.789157,-3.661703,4.183357,-8.710747,-1.546616,1.128549,-8.566995,8.688907,-4.383957,2.532128,-4.021034,-3.082979,3.648912,8.338544,9.672601,-6.401097,3.238017,5.736522,7.721018,-7.987463,2.580516,-1.430445,-7.447144,-0.268957,-0.008800,9.510986,-7.133023,3.723721,-9.829151,5.616671,2.644993,-9.352586,-6.414729,-6.241404,0.544551,-8.473502,-8.475957,8.396152,-8.162127,9.996685,9.153196,-6.815536,-8.843984,3.550587,-9.475741,-0.523959,-9.628296,-9.732167,-4.339593,-8.254087,-0.887028,-0.050546,7.301204,1.433669,-8.100520,-5.127821,-5.493039,9.914252,9.432625,3.857266,-8.949925,7.938939,-4.535519,8.191612,-5.873838,7.430675,-2.530350,-9.203986,3.903546,-2.746529,-4.250480,1.896095,8.209370,-2.461025,6.999719,-0.773629,5.739498,9.582597,4.956474,5.309955,-3.835543,-8.454500,-2.083708,6.420399,6.927253,6.763699,-9.805516,-0.794844,-7.334818,-0.943207,-1.647526,6.639402,5.200484,-7.667645,4.044865,-9.556655,-1.731099,9.789570,1.074928,-8.372094,-8.442404,6.117389,-7.686366,-5.902568], dtype = "float32")#candidate|3089|(1152,)|const|float32
var_3090 = relay.var("var_3090", dtype = "uint16", shape = (180,))#candidate|3090|(180,)|var|uint16
call_3088 = relay.TupleGetItem(func_631_call(relay.reshape(const_3089.astype('float32'), [16, 12, 6]), relay.reshape(var_3090.astype('uint16'), [180,]), relay.reshape(var_3090.astype('uint16'), [5, 6, 6]), ), 3)
call_3091 = relay.TupleGetItem(func_636_call(relay.reshape(const_3089.astype('float32'), [16, 12, 6]), relay.reshape(var_3090.astype('uint16'), [180,]), relay.reshape(var_3090.astype('uint16'), [5, 6, 6]), ), 3)
output = relay.Tuple([call_3071,bop_3078,call_3088,const_3089,var_3090,])
output2 = relay.Tuple([call_3072,bop_3078,call_3091,const_3089,var_3090,])
func_3095 = relay.Function([var_3090,], output)
mod['func_3095'] = func_3095
mod = relay.transform.InferType()(mod)
mutated_mod['func_3095'] = func_3095
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3096 = relay.var("var_3096", dtype = "uint16", shape = (180,))#candidate|3096|(180,)|var|uint16
func_3095_call = mutated_mod.get_global_var('func_3095')
call_3097 = func_3095_call(var_3096)
output = call_3097
func_3098 = relay.Function([var_3096], output)
mutated_mod['func_3098'] = func_3098
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3132 = relay.var("var_3132", dtype = "float32", shape = (13, 10, 8))#candidate|3132|(13, 10, 8)|var|float32
uop_3133 = relay.exp(var_3132.astype('float32')) # shape=(13, 10, 8)
uop_3143 = relay.sigmoid(var_3132.astype('float32')) # shape=(13, 10, 8)
const_3146 = relay.const([[[9.333660,-8.077517,9.828190,-0.767796,-3.247378,4.595916,-2.121748,-8.991627],[-4.310742,-1.832737,5.670706,-8.312326,-5.189089,-8.085378,4.238010,-1.318102],[-6.912545,6.020427,4.890082,-4.346857,1.213747,0.565413,-4.619373,-5.992892],[9.148346,-6.979278,7.398245,-4.576571,8.606910,-6.867723,-0.301497,4.037567],[3.289067,-2.908389,7.912275,6.061153,-3.280949,-2.282332,-4.309022,1.762126],[5.950351,-4.648031,-5.603469,9.142990,-9.411325,6.590959,-2.136408,9.566742],[2.947383,5.382408,-0.513524,3.043054,4.389041,-6.283713,2.668847,7.161856],[7.081255,8.607591,-5.679622,8.932484,-3.318614,0.266276,-7.480789,9.498537],[-5.260520,-6.658865,2.847688,4.775220,1.007235,-4.013673,2.766186,-9.307699],[5.827622,-1.055077,-5.033929,-2.748794,-0.053355,2.413798,-4.146329,-9.773612]],[[3.030500,-1.243182,1.807756,8.394005,1.045245,4.457743,3.570942,8.915612],[4.170962,-0.903883,1.553210,9.274666,-4.706273,-9.665580,1.989395,0.594984],[8.066682,3.100007,4.161517,-6.591261,-5.461231,1.163946,3.268288,-3.736599],[5.188765,-6.473381,-5.385371,-4.292506,-3.981142,9.234562,-5.761303,2.395851],[-7.056666,-1.448355,5.733680,-6.817223,-9.307590,-1.099392,-1.832901,-2.885819],[1.631412,6.363312,-3.941264,0.219519,-9.222305,-1.776257,3.860605,9.340679],[-6.826278,-3.641452,-0.145399,0.990569,-2.931638,-3.124706,1.521980,-6.084456],[6.191916,-0.754896,-3.663644,-4.931556,-4.935880,8.249742,-9.402285,-1.868871],[-1.312044,3.508581,0.597534,4.829023,-5.000798,5.590708,-2.696211,-0.961396],[8.264740,-2.771971,-2.957799,-9.336333,3.832223,3.572047,-9.691094,0.330963]],[[-6.563563,6.033699,3.628747,3.606162,-1.148582,1.627372,1.661432,-2.791337],[-5.402602,-0.664736,-7.962793,-2.314677,-0.681071,2.567374,1.451894,6.749984],[6.196555,7.697804,0.391148,-7.841216,2.384273,-1.053800,-8.557039,7.452687],[1.997181,8.468462,1.808311,-2.606007,9.391481,-7.784246,-1.067646,-9.623672],[1.387768,-5.647589,8.552523,-9.397417,2.926214,6.193489,-0.586604,-4.239212],[-3.854309,5.387633,6.562103,0.734845,8.153628,2.378719,8.963498,-1.249518],[-1.859731,7.003480,5.167647,-7.280141,-6.755462,-5.068710,2.664037,3.051151],[5.607919,3.313449,-1.100699,3.135369,-7.870680,0.750095,9.385425,-9.723081],[-5.974511,2.388470,-2.329884,-4.639886,1.657573,2.023240,-2.049277,-0.745698],[0.048777,-8.190366,-9.978056,2.884633,0.530957,-7.550440,-4.436318,-4.852746]],[[-9.177429,1.563944,3.234338,7.647915,-5.103840,3.704715,0.276356,-4.060656],[8.146080,-4.283782,4.998927,9.385940,-8.507321,0.905297,-1.780809,-1.557047],[3.671661,4.729890,5.983911,5.804053,2.997451,-8.309160,-8.185294,1.799735],[-1.933345,0.740077,-0.866884,-9.441684,-8.897040,9.916481,7.394115,4.044146],[7.198424,4.598252,3.380310,3.080820,-9.949049,-9.083143,-6.208196,-2.537162],[1.835504,-4.429774,-4.497765,0.035190,-8.790291,-2.385315,-3.441320,-6.942376],[-2.814798,-5.853848,-1.814836,9.601813,-4.301062,5.476440,2.443989,2.073484],[6.741614,-8.128862,-8.865254,-3.589240,1.814997,-9.615897,-7.098637,3.426166],[-8.002779,0.464868,6.249120,1.354074,-1.909811,7.186977,3.980285,-1.153764],[-3.195488,-4.419213,-4.577466,-5.358493,1.390635,1.095473,2.094244,3.033332]],[[6.694364,2.374917,9.643219,-9.841695,7.453475,0.394556,-5.151981,-7.714532],[0.895842,4.197044,4.751809,6.278054,-5.074412,2.947818,7.129904,0.267237],[3.005122,-1.086940,-2.497619,-0.653794,-2.901123,-3.383666,9.997364,1.174073],[1.375200,2.098533,-7.436392,-5.269228,7.663874,6.177719,-8.823128,0.320898],[4.757006,-4.317323,-7.959095,4.764238,-3.239482,7.892412,-4.125896,-9.925955],[8.972880,7.973930,-3.497449,-7.166376,9.196944,5.505931,4.490272,9.655971],[-0.086530,-9.974634,-0.151464,7.450798,7.878517,-6.964218,9.166091,8.415471],[-0.253518,2.262144,-6.034633,9.050314,8.232003,4.922649,8.010184,3.846835],[-3.474647,2.730823,1.523411,-8.751737,7.947624,6.450512,9.459794,-8.831641],[3.321854,0.265129,3.292903,2.043146,8.674671,2.725176,5.375272,-5.316892]],[[-0.387989,-1.836865,-9.454013,-8.242204,0.429782,-4.530922,7.724580,3.832178],[-6.501539,-0.883409,6.963463,-6.841314,4.758037,8.113511,-9.576209,-8.827439],[1.836593,2.768048,8.689204,-6.393969,0.632644,-7.565708,6.217572,7.459289],[-5.842745,2.534733,8.924746,-2.168948,-2.072380,5.906725,2.490512,4.042114],[-5.942112,-7.003291,0.831071,-3.681457,9.936971,9.009957,-1.940259,4.673402],[-6.248348,-4.718041,-4.054254,-8.167766,5.767165,-6.969906,-8.249042,1.791577],[-9.283617,-6.784900,-3.733102,-4.439604,1.920348,-8.510273,-8.609798,-1.670327],[2.909128,-0.092048,3.259981,-2.621117,-1.043891,4.840851,-7.529627,9.374786],[-3.155940,-6.325293,-0.715155,8.831028,-5.010426,-8.442336,7.400941,-6.901364],[6.446801,-4.077150,3.898003,7.000355,7.406700,-9.990206,-4.573432,-4.334875]],[[-7.330086,1.742464,6.634479,-2.724709,8.817685,-9.920446,-7.143910,4.559779],[6.149356,-3.978466,-5.155234,-6.442907,0.248510,9.622032,-2.299003,-7.384365],[2.091460,-5.865364,-9.593171,-8.283026,6.245159,-4.223342,7.066796,5.812345],[-1.134001,-0.124857,-2.201328,-1.844638,6.851695,4.489945,-5.979263,-2.078378],[6.287078,-9.764541,-4.362311,0.145973,-4.305121,2.106380,4.479342,-6.374113],[-1.371492,-4.293613,-5.261753,-4.570537,4.447469,3.302459,-2.906123,1.925870],[-2.272241,6.151652,-0.398813,-6.407236,5.990831,2.430985,7.310957,-4.618534],[-9.834891,-3.911308,9.757383,-3.226529,-2.530344,-7.773285,-1.536720,-7.484093],[-1.551229,6.633255,9.583126,3.081156,4.135813,9.257664,-7.101340,-7.865598],[2.147846,3.714565,-9.361365,9.951566,-6.345399,0.753854,4.479286,5.470485]],[[5.950208,-1.625494,6.276825,5.565609,-0.479583,6.946870,-3.951834,9.792688],[-9.891142,5.331968,6.073080,5.020007,-3.586229,-2.830310,-0.344594,8.696781],[-4.034668,-1.638651,9.597014,-9.418554,2.317936,6.912479,6.156525,9.420026],[6.846958,-2.881286,0.357791,-5.364012,-9.930861,5.952815,3.778691,2.308501],[-6.632965,1.458403,9.194686,-8.725408,5.643466,3.025942,-2.714060,-9.404784],[0.130325,-1.352995,-8.693046,-1.803747,8.831553,0.117994,7.853277,-2.998825],[2.474862,7.886718,5.878325,6.958929,8.345939,-1.458598,8.080668,-5.266135],[8.723921,4.308368,5.432370,0.133563,7.951826,8.791298,5.360554,-1.211709],[3.556603,7.719825,6.977513,8.015844,0.766230,8.349633,-7.006045,7.327495],[-1.602358,6.339460,0.988999,8.180027,-9.203880,3.972010,-3.959135,-7.187106]],[[2.625790,2.325972,-2.121810,-2.054409,-4.346504,-9.317226,2.678108,-4.289437],[-7.873658,7.489514,-4.986315,-2.665664,-7.879733,-6.091256,3.488839,-9.530755],[2.678517,-8.193887,8.629720,3.691263,-6.038363,-2.251141,-6.698245,7.299933],[7.428359,-3.530812,9.744962,-1.379726,-3.912961,0.491943,6.533552,-9.423134],[9.406111,-5.188689,4.912130,-8.631076,1.272129,2.410361,8.622093,-1.208132],[-2.364527,5.718316,3.337593,4.962513,-7.460979,1.077452,-4.606801,-8.869976],[-8.397935,-2.781372,6.569156,5.699149,-5.647355,-9.985054,-9.739020,-9.798615],[1.537601,-9.160134,7.557922,-6.031730,-6.644462,9.318003,3.838681,-2.856693],[-6.213076,-7.718503,7.869943,-9.580662,-4.059732,-2.869445,8.325437,0.180504],[-2.902119,2.946591,1.286110,4.229895,0.107512,3.008060,4.271297,3.729731]],[[-9.839676,7.817112,6.126277,7.200882,-6.054335,-6.684523,-8.398406,-6.092964],[-4.525199,-7.516538,9.243004,1.739962,-3.259017,1.096917,0.574896,4.730048],[-9.370892,8.736114,-2.614335,-6.620511,-9.857228,-2.161853,-6.094250,0.931997],[-5.927973,4.320121,-4.586438,2.279868,3.633696,-1.493226,6.344931,-6.916435],[-8.440016,6.992913,9.226365,3.760863,4.196850,-3.675209,-4.596451,-8.540022],[-8.097326,-5.908308,-5.592228,4.165022,-7.264440,-7.816603,-6.269111,-7.753823],[0.526047,8.599530,0.487082,-1.829640,5.597931,-5.301950,9.941475,-9.909929],[-2.910766,-6.046659,-9.567523,-5.108502,4.723830,-4.232377,-2.043244,-9.630675],[1.291256,-3.478031,-6.241677,9.646659,5.785107,4.248220,-0.084912,-0.841399],[-2.392632,5.734039,7.953376,5.467867,3.312472,-4.522562,-4.615355,4.048907]],[[-5.058038,-3.717471,-7.391741,-2.892793,-9.859934,-9.430753,-7.421584,7.943312],[0.840081,0.340392,9.658528,9.916529,4.456404,-1.340764,-0.469787,5.129392],[9.186717,1.544596,2.452211,1.992950,0.552891,-6.006091,7.387707,-7.957535],[-9.127340,6.494242,4.560846,-1.745704,-8.896076,-4.787148,-3.426993,7.401437],[-0.443241,-2.492666,5.624311,5.991869,3.104961,-6.466386,5.302820,-9.234208],[-0.854312,3.996440,-4.802077,-8.482534,-7.517793,-2.180274,-7.196116,-1.198258],[-2.496491,-1.886355,2.580393,6.245217,3.051633,0.523806,-5.334284,7.717241],[4.995166,-3.629310,-2.510479,-7.163402,-3.350404,-9.632029,-0.224986,9.835109],[0.154387,-0.040476,9.724197,6.175891,3.718006,5.337187,-0.464623,0.054471],[-8.576848,-5.950152,-3.534666,2.003203,5.287642,-0.039655,9.568055,-0.202563]],[[4.813818,0.617328,-6.041668,-0.771733,0.888432,-3.295274,-5.992383,6.661698],[8.168208,7.433701,-1.442980,-5.506413,-7.339555,1.582434,-1.847082,-1.510080],[9.788173,-8.960144,0.649902,5.217327,8.976688,-5.627596,7.469318,-0.247498],[4.080034,1.577677,-6.895196,4.672738,-3.429744,-6.494529,9.970205,-1.012025],[-8.543094,-8.930424,7.836784,-7.576136,4.449242,-1.026654,-1.452350,-7.521613],[4.291866,0.948031,6.799326,-2.423119,-0.607809,8.869996,-9.486236,-6.214022],[-1.850510,-5.469137,-7.876129,-3.206116,7.603966,3.261076,4.597518,-8.151628],[6.500306,9.075333,-1.210709,-7.512240,-9.079215,-4.160985,4.238296,-2.917946],[-9.520183,-1.181544,0.946897,-1.797980,2.538489,6.536175,7.450992,3.619941],[0.806677,-4.432065,7.030783,-3.637636,-7.274485,-4.195302,3.459836,7.235723]],[[8.523348,6.730373,5.766460,4.482740,8.832694,6.270104,-3.585786,6.607328],[4.289485,-7.832254,-3.046445,0.251062,6.276771,-7.012993,-2.213098,-2.945775],[3.621288,-7.888785,-9.806421,-2.021312,-3.755194,-5.165680,-4.915759,2.222819],[1.229051,-3.380145,-2.911057,-4.321214,0.630291,8.257554,8.159722,4.261485],[6.288964,9.976145,-2.059996,4.009539,4.707782,0.438946,1.038255,-3.034804],[-8.357714,-9.723580,-4.466805,6.558690,5.832189,9.091432,-1.009184,-4.058705],[-3.163293,5.559513,3.075295,-4.998128,8.373262,-9.059357,-4.033644,9.951731],[-9.228467,8.397265,7.293696,-4.572630,9.881334,5.241086,2.147713,5.195918],[3.823964,-3.439338,4.969048,1.059104,-7.379886,8.025495,-2.868825,-3.221096],[-8.706199,5.681365,-4.154047,0.733269,0.569456,2.807479,-3.922323,0.412005]]], dtype = "float32")#candidate|3146|(13, 10, 8)|const|float32
bop_3147 = relay.greater(var_3132.astype('bool'), relay.reshape(const_3146.astype('bool'), relay.shape_of(var_3132))) # shape=(13, 10, 8)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_3166 = relay.TupleGetItem(func_2131_call(), 0)
call_3167 = relay.TupleGetItem(func_2132_call(), 0)
func_2247_call = mod.get_global_var('func_2247')
func_2249_call = mutated_mod.get_global_var('func_2249')
var_3175 = relay.var("var_3175", dtype = "float32", shape = (1152,))#candidate|3175|(1152,)|var|float32
call_3174 = relay.TupleGetItem(func_2247_call(relay.reshape(var_3175.astype('float32'), [1152,])), 2)
call_3176 = relay.TupleGetItem(func_2249_call(relay.reshape(var_3175.astype('float32'), [1152,])), 2)
func_631_call = mod.get_global_var('func_631')
func_636_call = mutated_mod.get_global_var('func_636')
const_3180 = relay.const([[3,-9,-10,-8,10,4],[-5,2,9,-4,-2,-1],[5,5,-7,10,-9,-9],[-3,-5,-2,-7,-5,1],[-8,-1,8,-1,7,2],[-5,4,-3,-2,-9,-9],[7,-9,7,-6,-7,-7],[-1,7,-8,-4,1,-4],[2,-1,4,3,8,-4],[2,-9,-9,3,7,-1],[-8,10,2,6,-2,4],[-8,5,-1,-10,1,1],[8,-1,3,-1,-7,-2],[5,-5,-4,-2,8,-8],[-6,-1,8,8,-7,10],[-3,2,-2,-10,-2,-3],[-4,1,-2,-2,-5,-7],[4,-6,4,-10,7,-6],[-8,-7,1,-7,4,-10],[6,7,2,4,-9,6],[8,-10,-10,5,3,8],[-1,3,-4,-2,-3,-2],[2,3,-10,-3,-7,-5],[-9,4,-4,8,-9,1],[-3,4,1,-3,3,2],[-4,-2,-8,-7,9,1],[-6,-7,1,10,10,-2],[-3,-1,8,2,10,3],[10,7,3,-3,10,-8],[9,-6,4,-9,2,5]], dtype = "uint16")#candidate|3180|(30, 6)|const|uint16
call_3179 = relay.TupleGetItem(func_631_call(relay.reshape(var_3175.astype('float32'), [16, 12, 6]), relay.reshape(const_3180.astype('uint16'), [180,]), relay.reshape(const_3180.astype('uint16'), [5, 6, 6]), ), 6)
call_3181 = relay.TupleGetItem(func_636_call(relay.reshape(var_3175.astype('float32'), [16, 12, 6]), relay.reshape(const_3180.astype('uint16'), [180,]), relay.reshape(const_3180.astype('uint16'), [5, 6, 6]), ), 6)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_3206 = relay.TupleGetItem(func_2168_call(), 0)
call_3207 = relay.TupleGetItem(func_2169_call(), 0)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_3223 = relay.TupleGetItem(func_2625_call(), 0)
call_3224 = relay.TupleGetItem(func_2626_call(), 0)
output = relay.Tuple([uop_3133,uop_3143,bop_3147,call_3166,call_3174,var_3175,call_3179,const_3180,call_3206,call_3223,])
output2 = relay.Tuple([uop_3133,uop_3143,bop_3147,call_3167,call_3176,var_3175,call_3181,const_3180,call_3207,call_3224,])
func_3226 = relay.Function([var_3132,var_3175,], output)
mod['func_3226'] = func_3226
mod = relay.transform.InferType()(mod)
mutated_mod['func_3226'] = func_3226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3226_call = mutated_mod.get_global_var('func_3226')
var_3228 = relay.var("var_3228", dtype = "float32", shape = (13, 10, 8))#candidate|3228|(13, 10, 8)|var|float32
var_3229 = relay.var("var_3229", dtype = "float32", shape = (1152,))#candidate|3229|(1152,)|var|float32
call_3227 = func_3226_call(var_3228,var_3229,)
output = call_3227
func_3230 = relay.Function([var_3228,var_3229,], output)
mutated_mod['func_3230'] = func_3230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_3238 = relay.TupleGetItem(func_2131_call(), 1)
call_3239 = relay.TupleGetItem(func_2132_call(), 1)
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_3240 = func_2502_call()
call_3241 = func_2502_call()
uop_3244 = relay.sqrt(call_3238.astype('float32')) # shape=(12, 6, 10)
uop_3246 = relay.sqrt(call_3239.astype('float32')) # shape=(12, 6, 10)
func_3226_call = mod.get_global_var('func_3226')
func_3230_call = mutated_mod.get_global_var('func_3230')
const_3250 = relay.const([[-3.677281,3.134306,-1.107663,8.315267,-6.392785,-9.237640,0.905902,0.468434,-3.565395,-3.118383,-6.964611,-0.435543,6.259120,-4.695323,-5.272863,6.969751,-0.103378,-6.254558,-3.178716,8.228276,4.786422,-8.047937,-4.593753,-1.519185,3.761552,5.529599],[-8.736502,6.892663,-1.571044,7.133398,-7.640345,8.098852,-6.876192,5.000245,0.674995,3.932813,-4.455376,1.793732,-5.724378,-3.947856,-1.402901,7.987835,1.327922,3.967624,-3.014568,-5.634423,0.248730,3.777261,3.466506,-7.689136,-8.623514,-9.132453],[5.279226,0.689268,6.892889,-3.770329,6.547476,-6.221526,-9.493759,-6.283787,-4.228307,8.594355,-5.246826,7.046144,9.475132,-8.458066,-6.049857,6.616598,3.290414,0.448323,-1.875437,-6.599881,4.938014,-8.757500,-1.030635,-3.804723,7.429938,2.905246],[-6.036977,2.765371,-9.998305,7.083597,-3.735960,7.832804,1.879207,-1.529187,-7.080430,-0.718212,3.660002,9.402065,6.568387,3.345316,7.542798,4.529300,3.875795,1.443668,-4.363539,-4.190986,2.994634,-8.015904,-4.897483,-5.859824,-3.300154,-7.246907],[6.722179,2.012052,3.995377,7.590673,2.847663,5.415572,-4.318131,4.917664,4.729122,8.090787,0.840556,-1.308954,1.563156,-8.702465,1.235471,9.214508,-2.016482,5.174527,4.268747,-1.157722,4.211495,-2.633760,-0.074991,9.126917,4.677469,9.713324],[-7.922065,0.544413,-2.036418,2.753798,-5.751517,0.350111,-4.772535,8.832217,2.389119,-1.574548,0.992239,-0.627337,-8.727084,2.481672,3.015005,-2.829762,-8.171729,4.685714,9.624500,-2.507411,2.958231,-0.480567,6.094290,-0.531639,1.291697,5.795479],[3.087312,0.209719,0.614762,4.506496,3.162548,2.571475,0.067563,-0.366451,1.284262,9.886576,-9.977110,-0.791577,1.694812,5.268300,-1.783189,0.314178,-1.466487,1.567996,1.201637,-4.661815,5.389879,4.909679,-4.608622,6.539675,-0.215340,9.731382],[8.368074,-9.782931,-1.371726,1.889069,5.778125,-4.817271,3.950658,3.903600,-6.237952,6.733420,0.385603,9.408852,1.816432,-5.583645,3.812425,-0.987778,6.959671,0.334924,-4.833515,-8.164386,5.775728,-3.292396,6.252910,3.622508,9.320767,7.597325],[9.570461,3.552465,5.709564,4.239931,6.331278,7.859834,-4.557662,-2.952232,-6.378487,-4.248047,7.823114,-1.774210,5.447141,-4.933686,6.672046,7.832859,-6.387986,1.362451,-7.698532,-8.147562,-1.566430,3.275789,-8.666687,-9.693653,-7.123167,-1.547161],[5.315490,-7.594972,8.742496,8.018609,-4.623596,9.315716,1.521729,2.946477,8.377170,3.567928,3.754586,2.416250,-6.313369,-7.944888,-4.507686,-5.293635,-5.515837,-5.289853,-1.869071,-1.002188,0.727455,4.810887,-5.668581,-3.655999,3.518558,8.344190],[-4.588189,-5.432228,-0.889170,-9.553092,-2.556142,-9.318553,8.423225,-5.169972,7.694974,7.013119,-9.647620,8.374158,2.659925,8.634869,-9.230512,2.792547,8.240269,0.881044,5.967032,-8.978385,3.355335,-4.996072,-5.650783,-1.942648,3.258081,-7.447778],[-3.080441,-4.669133,6.794781,-9.175500,-6.594331,6.901139,-4.772387,-5.868133,-4.596871,5.716081,0.821896,-0.847423,-7.100521,2.177598,-1.931489,8.777032,-7.463491,-1.238257,0.524968,4.983965,4.933092,8.784574,8.524708,6.807658,2.252434,4.002428],[-4.946709,-6.096112,-5.874850,-8.916947,9.904233,-7.349983,2.883227,5.325680,7.871931,-5.170119,6.289995,-7.049012,2.780486,-7.206742,-5.037076,-8.524538,-7.449935,6.997153,-5.373675,1.292462,-1.764941,8.894528,1.072513,-1.689750,1.066142,7.044338],[1.316003,-9.236914,3.654285,3.804046,-3.980082,-6.692613,-1.264134,-2.926593,4.569881,-1.926678,3.909559,0.178630,-1.236590,2.744998,-4.404800,8.375264,3.863701,5.376308,-5.576302,-0.378399,-9.543833,5.280081,2.627593,1.161224,-7.895320,-7.663800],[-2.919674,-7.074925,8.032265,-3.016193,-9.733615,1.949172,7.617609,-7.916639,7.276627,2.484999,3.145123,-7.692385,-9.554605,5.147488,8.510281,-2.514475,1.728046,4.586000,-2.027893,-6.699982,0.188649,-5.403015,-4.585383,-9.127787,-7.377533,3.869332],[3.811137,-0.302181,-2.089704,-0.695366,0.120790,9.339758,1.109853,2.409008,-2.867529,-0.262569,-0.601492,2.978515,6.005130,-4.364745,0.139112,9.715533,-7.356301,-4.332206,9.463568,-4.047499,6.348574,4.205461,-7.855335,-3.926384,-8.984558,-0.555194],[-4.026362,-2.206128,-4.845415,6.637512,-9.300019,-8.828732,-2.568239,8.561276,3.926450,-6.468850,5.472674,0.332777,-9.189925,7.389308,-7.818619,0.928032,5.803751,-8.057676,0.814448,6.638339,-6.100257,-9.407081,-1.957696,-5.637571,9.592978,-0.227906],[-0.714298,0.879553,4.336667,3.406111,-1.094836,-4.866985,-6.137088,6.017487,-3.163614,-3.855136,-6.178806,9.803631,-8.621135,-0.440328,-4.489108,0.342317,-5.900256,-4.401345,5.079726,4.977005,-3.898126,8.066227,-1.425478,-8.943827,4.161232,8.868764],[8.732740,-8.615278,-3.537515,-2.024822,4.737525,7.723211,-8.965669,7.726226,-4.224773,9.302030,1.124376,6.269453,-3.768451,-9.912260,-5.276465,2.561013,7.633229,-7.086402,8.327807,-8.309552,-8.972017,-2.519155,3.043239,-7.402960,1.920582,5.060615],[-6.532041,-3.232437,-4.078806,-8.284156,0.369473,0.335242,9.560897,-8.257726,-6.387349,8.435248,0.861555,0.460526,4.063144,-2.429013,2.460448,0.808590,-4.805641,-5.645555,6.846973,-9.019156,6.584766,7.243764,3.205585,4.325217,-3.006762,-6.297670],[-1.307934,8.046917,0.662472,-9.741044,5.603752,-6.696122,-2.008516,-0.704269,3.390950,-4.167088,-7.925447,9.905329,5.806987,2.726107,3.379669,9.656014,3.554315,9.278517,-4.925166,-2.234460,-8.315856,-3.748565,8.721435,-0.164843,5.776486,1.718196],[-4.082089,5.669723,4.903006,4.477692,-9.374680,0.933360,4.755491,-4.590912,-7.927589,2.349519,2.669117,8.371425,1.952401,9.129074,-5.864206,-9.827678,7.077224,8.941688,8.286195,5.282854,1.923465,9.581132,3.218027,8.589660,-9.831584,-7.588173],[-4.842006,8.423918,3.059636,-8.377635,0.421460,-3.142111,-7.718356,-6.413315,2.719579,7.133820,-7.745886,0.148893,-3.913926,7.497129,-8.985696,-9.616461,-3.075782,-7.982085,-5.062449,9.744394,3.649664,-6.834215,0.663880,2.911813,-3.499778,-9.094059],[-3.339143,-3.577248,-7.316861,4.015439,-3.749519,1.208014,2.477970,-1.585608,-5.721915,-8.162908,-4.893253,6.711849,3.056328,-0.105275,4.094664,-4.193532,-5.686175,-5.164915,-8.641926,5.651503,0.875057,0.598711,-6.010433,-9.859083,-8.077118,8.152756],[7.708907,-9.994260,6.330513,-9.340846,4.742828,-7.399324,8.814019,-8.198374,8.623238,-8.889289,-9.877854,1.904292,-6.168597,3.741020,-7.044910,1.095081,9.833922,-4.589441,-4.740792,0.972275,4.824916,5.447186,-0.697361,3.411500,-8.393459,-7.746591],[0.075851,9.481919,0.320033,-3.908107,2.534747,9.502612,-4.242127,-2.459677,-8.797798,-7.924541,4.264356,8.445782,-3.229844,7.575460,-3.244808,0.030477,-9.699038,7.417748,-5.813927,3.227957,2.401285,-6.226354,0.169437,-3.740897,3.955044,2.108871],[4.643338,-4.591102,2.491357,-5.471917,-1.029373,-8.524464,-8.241120,-4.501716,1.189731,0.182806,6.231894,-1.205086,-0.321937,-5.105717,-3.413831,-6.398433,-8.955127,2.950784,7.407312,-2.055803,2.696880,-0.172827,-8.812970,-2.783581,-9.940312,7.435948],[-4.037812,-1.106820,-3.664422,-0.902912,4.559576,-7.233021,3.739894,9.973813,9.959918,-4.671872,-9.411351,8.025705,-6.225686,2.081477,1.420950,-8.979720,-9.848163,-9.631025,0.820453,7.053676,5.983270,1.879429,8.552052,8.052574,-0.630883,-6.629478],[-8.479548,8.018272,0.907213,-4.125617,2.505456,-0.566564,5.590011,3.237556,2.757581,8.113883,-5.560235,-1.298292,-8.344360,5.677474,9.917832,9.585443,2.430347,-4.406370,7.594181,4.916642,6.103237,9.543275,-5.701215,-8.018429,7.983943,-9.843184],[-1.980339,-5.573009,7.291341,7.592134,3.533313,-2.764540,5.273502,9.258821,8.975347,-8.960825,1.996025,-7.568820,-0.024412,6.497013,-7.092960,5.276470,-6.678523,3.623682,7.642647,5.162781,-0.854564,0.262452,-4.601405,-5.111635,2.603423,7.048466],[-9.374158,-8.466440,-6.730906,0.573718,-4.371745,7.709306,-8.266933,-7.776956,4.360499,-1.624865,9.726048,5.352223,-7.784787,-0.737307,-6.213889,-6.741812,1.686290,5.130813,5.025147,-8.542315,-3.519213,-4.156602,7.330490,-5.327294,-0.219884,-9.396817],[6.617129,-0.265890,6.944682,8.142247,-3.109756,5.468348,9.774126,4.305674,5.663579,-5.692999,6.084567,-9.922915,9.081243,4.845444,4.895789,7.787532,0.129074,-4.618722,-1.629794,1.847486,-5.995697,-2.963014,5.111371,-3.137881,-0.997263,-2.258522],[5.947749,-7.604181,-0.369397,1.887530,8.204854,-5.434862,-3.572306,8.507337,-6.175840,3.911475,3.461138,-1.687538,6.847979,6.595604,7.312255,2.807418,-0.993864,0.002319,9.323004,-3.638766,-4.156390,5.302004,-7.436447,7.161452,6.754416,7.560769],[7.947340,-9.352495,-6.192025,-7.753496,5.930991,-0.430087,3.486513,-4.403882,-2.058487,9.226025,4.404809,3.535648,8.625829,0.612973,0.775891,-5.224126,-4.098627,9.875819,-2.825119,4.808895,9.953682,-1.358972,7.217915,7.732907,7.909769,-4.228187],[-7.557042,-4.112348,9.054047,-3.281320,-9.746127,7.961076,4.400392,0.066736,-4.887866,-9.258722,6.895424,-0.101826,3.933911,-5.350109,-7.580773,-4.805900,6.957886,-3.350338,-6.230097,6.237348,4.205425,0.122650,-0.954527,5.519171,3.291862,-3.844525],[-5.451068,-0.109809,8.198510,-5.672217,9.217501,-2.399803,-8.665133,0.941049,4.260893,4.306376,6.786645,-3.775028,-0.405117,-3.027526,0.237875,-5.717319,2.550178,9.562380,1.297615,-0.235953,-7.025783,3.298115,-7.141361,6.305592,-3.048493,-0.905677],[-7.998488,4.901082,-9.680437,-7.206662,-8.007142,1.021979,3.100245,-1.987515,8.740835,-1.591240,2.742765,-4.964898,-8.699925,-7.347926,-4.356019,8.482222,0.910289,5.511956,-9.041254,5.095934,-5.886733,1.804972,0.075758,4.610772,-1.931332,0.066912],[7.313913,2.080047,7.859055,-3.000896,9.769856,-5.909952,-6.997802,-6.437425,-8.269076,-0.642366,2.425404,-0.208173,0.519478,5.771786,8.090693,-3.009257,-8.386876,1.576718,8.600309,2.396212,9.615740,5.804959,-8.885288,-1.097689,3.973787,0.820966],[-6.597069,2.974829,0.274814,-7.777601,1.482978,-6.636416,-2.898315,-2.575600,1.987695,-4.493571,4.447764,2.285529,-2.892937,-1.534455,-2.180633,-9.751044,-6.209417,-9.408671,-6.921500,-5.045441,0.533018,1.606576,-7.024022,7.526900,8.143028,-5.113558],[7.122081,-6.918553,-7.935683,8.828087,2.932601,5.319832,-2.445876,4.916609,-2.417970,-0.029090,-4.990279,-4.485118,7.930560,5.285994,9.367339,-6.698337,2.616209,-8.593359,2.538812,-0.605980,8.859038,-4.150486,4.104745,-1.796014,-0.525017,-1.006549]], dtype = "float32")#candidate|3250|(40, 26)|const|float32
var_3251 = relay.var("var_3251", dtype = "float32", shape = (1152,))#candidate|3251|(1152,)|var|float32
call_3249 = relay.TupleGetItem(func_3226_call(relay.reshape(const_3250.astype('float32'), [13, 10, 8]), relay.reshape(var_3251.astype('float32'), [1152,]), ), 5)
call_3252 = relay.TupleGetItem(func_3230_call(relay.reshape(const_3250.astype('float32'), [13, 10, 8]), relay.reshape(var_3251.astype('float32'), [1152,]), ), 5)
func_2263_call = mod.get_global_var('func_2263')
func_2266_call = mutated_mod.get_global_var('func_2266')
const_3254 = relay.const([10,-10,10,-4,8,-6,9,10,8,3,4,10,4,-10,-7,-6,3,-9,-3,9,6,6,-7,-9,2,7,-1,7,6,-2,2,-3,-4,-10,-5,8,-6,7,1,-10,-9,-1,2,4,5,3,6,2,10,4,-1,-7,9,10,-1,4,-5,-10,3,5,4,5,7,7,-9,3,5,9,-5,3,9,-7,4,-1,3,-5,7,-4,-7,-10,-2,-8,-2,-1,6,-4,-3,9,-6,4,-8,6,-1,10,1,-6,-4,2,-3,-4,10,2,-6,-3,-1,6,8,-5,-2,8,-6,10,3,7,-8,-3,-8,2,-5,-10,3,-6,-6,1,7,-5,6,-4,-9,4,-3,-4,1,-6,-2,-3,-10,6,-9,6,-8,10,8,4,-6,-5,-5,-9,-6,3,9,4,4,-7,-9,-10,6,3,-5,-3,5,-9,6,7,2,1,7,-5,7,3,-7,-3,2,-8,2,7,9,8,-3,-9], dtype = "uint16")#candidate|3254|(180,)|const|uint16
call_3253 = relay.TupleGetItem(func_2263_call(relay.reshape(const_3254.astype('uint16'), [180,])), 2)
call_3255 = relay.TupleGetItem(func_2266_call(relay.reshape(const_3254.astype('uint16'), [180,])), 2)
output = relay.Tuple([call_3240,uop_3244,call_3249,const_3250,var_3251,call_3253,const_3254,])
output2 = relay.Tuple([call_3241,uop_3246,call_3252,const_3250,var_3251,call_3255,const_3254,])
func_3258 = relay.Function([var_3251,], output)
mod['func_3258'] = func_3258
mod = relay.transform.InferType()(mod)
mutated_mod['func_3258'] = func_3258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3259 = relay.var("var_3259", dtype = "float32", shape = (1152,))#candidate|3259|(1152,)|var|float32
func_3258_call = mutated_mod.get_global_var('func_3258')
call_3260 = func_3258_call(var_3259)
output = call_3260
func_3261 = relay.Function([var_3259], output)
mutated_mod['func_3261'] = func_3261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2860_call = mod.get_global_var('func_2860')
func_2862_call = mutated_mod.get_global_var('func_2862')
call_3402 = relay.TupleGetItem(func_2860_call(), 0)
call_3403 = relay.TupleGetItem(func_2862_call(), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
var_3412 = relay.var("var_3412", dtype = "uint16", shape = (180,))#candidate|3412|(180,)|var|uint16
call_3411 = relay.TupleGetItem(func_261_call(relay.reshape(var_3412.astype('uint16'), [5, 6, 6])), 0)
call_3413 = relay.TupleGetItem(func_263_call(relay.reshape(var_3412.astype('uint16'), [5, 6, 6])), 0)
output = relay.Tuple([call_3402,call_3411,var_3412,])
output2 = relay.Tuple([call_3403,call_3413,var_3412,])
func_3427 = relay.Function([var_3412,], output)
mod['func_3427'] = func_3427
mod = relay.transform.InferType()(mod)
mutated_mod['func_3427'] = func_3427
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3428 = relay.var("var_3428", dtype = "uint16", shape = (180,))#candidate|3428|(180,)|var|uint16
func_3427_call = mutated_mod.get_global_var('func_3427')
call_3429 = func_3427_call(var_3428)
output = call_3429
func_3430 = relay.Function([var_3428], output)
mutated_mod['func_3430'] = func_3430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_3446 = relay.TupleGetItem(func_2562_call(), 1)
call_3447 = relay.TupleGetItem(func_2563_call(), 1)
uop_3449 = relay.log(call_3446.astype('float32')) # shape=(1152,)
uop_3451 = relay.log(call_3447.astype('float32')) # shape=(1152,)
uop_3456 = relay.acos(call_3446.astype('float64')) # shape=(1152,)
uop_3458 = relay.acos(call_3447.astype('float64')) # shape=(1152,)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_3459 = relay.TupleGetItem(func_2402_call(), 0)
call_3460 = relay.TupleGetItem(func_2404_call(), 0)
func_3427_call = mod.get_global_var('func_3427')
func_3430_call = mutated_mod.get_global_var('func_3430')
const_3467 = relay.const([-10,-2,-9,7,-9,4,9,1,5,-4,10,-7,-6,9,3,-7,-8,-1,-9,10,5,7,6,-3,-5,-9,-6,9,1,-5,9,9,-10,-4,-9,6,8,9,1,-4,8,-1,-10,-8,8,7,-7,7,-9,6,-3,3,8,-7,5,-5,-3,-9,9,-3,-5,6,-9,9,2,-5,10,10,9,6,9,8,2,-6,-7,9,1,5,-8,7,2,7,-9,1,-6,-3,10,8,9,2,7,9,7,-8,-10,5,7,5,10,-4,-5,-1,6,-9,-7,2,-2,-2,5,-4,-4,-9,2,7,-10,-8,7,9,3,10,-1,-4,3,4,5,-5,8,2,-7,-3,9,1,-5,9,10,-7,-2,-4,4,-5,7,-10,3,6,-10,-7,4,-4,8,-6,3,-9,-4,-7,10,-9,-3,3,-2,6,-10,2,-10,-3,-10,-9,2,-7,1,-9,8,-10,-9,-7,-2,3,-5,-3,3,-5], dtype = "uint16")#candidate|3467|(180,)|const|uint16
call_3466 = relay.TupleGetItem(func_3427_call(relay.reshape(const_3467.astype('uint16'), [180,])), 1)
call_3468 = relay.TupleGetItem(func_3430_call(relay.reshape(const_3467.astype('uint16'), [180,])), 1)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_3485 = relay.TupleGetItem(func_2168_call(), 0)
call_3486 = relay.TupleGetItem(func_2169_call(), 0)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_3487 = relay.TupleGetItem(func_2402_call(), 0)
call_3488 = relay.TupleGetItem(func_2404_call(), 0)
func_3226_call = mod.get_global_var('func_3226')
func_3230_call = mutated_mod.get_global_var('func_3230')
const_3491 = relay.const([0.990500,-2.301474,-0.490003,-4.467276,0.649889,-2.507448,-0.654267,6.840477,-0.523450,-7.750522,-9.474220,-2.309550,-7.853384,-7.709209,1.265565,5.675821,-6.245417,-6.565778,6.385897,1.966256,8.138553,4.754700,-7.412797,1.608294,2.275179,7.945028,5.613183,-9.784612,2.286758,-8.204094,2.779450,9.166648,1.488062,5.698139,2.656886,9.086719,-4.788600,-8.603405,8.475071,-4.633577,-1.876255,-9.141198,7.008424,5.966699,2.568511,8.071083,8.344733,-8.437711,-8.341649,3.401125,-9.764359,-4.407772,8.271320,0.282438,-0.977173,6.567241,-7.602954,7.731866,-7.061172,-2.163742,-0.357601,8.075237,4.938747,-0.956223,0.810869,5.908413,-8.399626,-3.652677,-0.015501,-4.390644,9.502034,7.779773,-7.750424,9.762450,-0.553439,-0.492171,-3.517273,-4.883250,-3.268956,4.612555,5.204013,2.570341,3.225104,2.648489,-5.800037,-0.311407,-0.925742,1.039748,-2.502918,7.168313,-2.937138,4.394469,1.503314,-1.475833,-2.747654,5.214228,-9.077459,6.655339,9.903340,-9.094430,2.116683,6.749857,-9.464925,-1.859800,-0.714460,9.896996,0.812230,0.588296,9.186571,-1.453438,8.667128,8.041783,1.542417,4.170212,6.654827,-7.366681,8.583412,-7.803751,-7.486351,-7.100045,2.093049,3.744901,8.723271,5.781740,7.726819,-2.556539,-0.046580,-8.481208,6.296694,-1.534085,0.360077,7.713058,-2.413660,9.413639,-9.455062,5.804784,6.026019,-8.997811,6.857677,2.963638,-4.231497,-5.853684,1.649012,-1.850672,-6.062025,-6.806880,5.839590,-1.537318,7.920801,-2.144738,-2.136749,2.903901,-7.139343,-0.281274,-1.893765,-4.127871,8.503507,9.237456,-8.494390,6.290986,-1.514804,-8.932084,1.504419,9.376144,-5.693841,-5.792145,-5.267910,7.276055,-8.079163,-8.933136,9.029671,0.651890,9.895510,-1.433065,-2.496609,7.723508,2.230175,-8.531250,-5.040530,0.504621,9.159290,4.617826,-2.233379,-4.286504,-2.850203,7.930382,-6.828909,7.692485,9.120502,9.349400,2.418718,-4.775951,-5.410841,-7.855188,-9.033495,-2.128966,1.944726,1.366898,-5.355085,-1.619106,8.807160,-7.317751,-4.980213,2.381738,3.964903,6.730659,0.459589,5.206885,-4.056110,4.286397,-4.295861,-8.857503,1.187756,8.285034,-0.839747,6.802258,1.285269,2.743816,3.499792,0.044227,2.271418,4.336673,-6.111250,-1.868060,-7.880211,0.777161,7.299883,6.540917,-2.381833,-6.855562,-3.435364,-6.955504,-0.171780,-3.954748,-7.225721,-0.050389,-9.139314,9.636796,9.564816,-5.340281,8.492860,-0.741203,8.845618,0.296011,-5.521102,-5.352158,8.821660,-1.404388,-4.256089,7.032536,-7.275644,-9.240429,-6.639338,9.939777,-8.200361,5.136820,5.921053,-0.454819,5.037175,-3.364174,-9.518564,8.502510,7.275834,5.471779,-1.139171,2.230515,-4.972383,7.555553,7.020030,-7.274690,-7.349596,2.483288,7.796640,8.917346,6.776056,-0.307368,-0.261562,-7.002404,3.202163,-0.571801,-0.671085,-3.381144,9.281917,3.041930,-9.635640,-1.231923,-6.552236,8.257444,-9.123120,-5.162209,-1.104686,6.404077,-1.759877,2.680326,5.521295,6.619579,3.009991,-2.053536,-6.068560,0.442520,-7.901149,1.998609,1.627173,-4.535501,4.382453,9.100777,-8.282864,6.452738,-0.964386,-5.633077,-7.880320,-8.151011,-1.818957,-7.739317,-4.645446,6.499965,-6.951237,5.482910,5.754767,6.344860,9.034655,9.361116,0.658516,-3.155900,0.903057,3.540183,8.457558,9.009600,-2.769434,-6.838328,4.216938,7.221093,-5.913699,4.875307,2.248401,6.714654,0.472922,-4.166733,2.323631,8.837673,8.254838,-2.134158,-6.697002,-9.790718,2.204637,5.045249,1.439009,-2.510022,-1.756429,7.364642,-4.155042,-7.076025,4.644363,-2.754001,0.920087,3.501886,-5.639153,0.244660,0.246611,-7.642838,-0.838278,0.743656,-6.097103,-5.821053,2.485417,-1.488210,-9.056545,-3.490361,0.473635,-5.801117,-9.600947,-2.368575,4.029247,1.615232,8.633673,6.857384,0.397178,3.201913,6.783137,-5.625801,-8.761372,-5.384538,7.739750,-6.120483,-9.859868,-0.478922,0.192956,9.778831,-1.824653,4.972554,-9.095752,-3.881732,-4.680183,-3.441567,1.209848,-3.788812,6.927535,-5.327865,5.307259,-5.655931,1.930418,-1.546299,1.059721,8.106973,-9.891884,9.043401,4.648226,9.846241,-2.170766,9.419672,-5.411275,5.422612,5.626527,4.830407,-0.233446,-4.408530,-4.618221,-4.292411,-6.143395,9.569699,7.611625,-2.286924,-5.435792,-2.970909,9.998899,-7.057928,1.700673,0.636676,7.420015,-3.173383,-4.661733,8.100902,1.474017,-6.773757,7.881828,3.954474,9.828861,-8.870172,9.265829,-8.392378,-6.142614,-6.328878,-2.511322,-3.011895,-6.623783,3.051765,8.416678,1.975638,1.330256,4.044469,-1.228796,7.963806,-3.712195,0.865661,-0.409104,-4.533265,0.433592,-4.343576,-5.179859,8.203881,3.194254,-8.037190,-0.222627,-1.541402,5.976008,-1.037901,-6.555302,6.935267,4.401533,-1.038701,-8.981466,0.477581,0.447829,3.693356,-3.239049,3.043037,-5.113103,3.935047,5.845759,-4.293648,5.574821,-1.357925,-9.917535,-4.149240,3.560649,1.748793,8.025237,9.859955,-7.193615,-7.612267,3.986762,1.048180,7.595974,-5.457676,-4.318099,-5.488389,-8.948828,6.559823,-3.394378,-1.351726,-0.768147,-7.408309,-2.443072,-5.600911,-2.811285,-8.037858,-6.498037,0.039174,-0.876395,0.562479,-5.339863,-9.314248,-5.638183,1.950703,2.897489,-9.473832,4.813695,7.908260,-5.602960,9.562138,-2.662460,8.537754,3.769118,9.860065,-4.947655,-6.281948,-6.961690,6.542637,-3.834217,9.251976,8.320903,7.329374,-5.205890,-3.997855,-7.304310,-1.360937,6.060899,-4.985224,-9.941665,-5.448455,-8.222209,-8.577990,5.977193,6.721209,-3.973824,2.146841,3.368755,2.524774,8.593350,-1.303435,3.802715,2.240667,-9.843815,6.083865,9.740091,-7.969491,-1.954175,-8.488641,-7.224204,4.984740,-1.643848,-5.137032,1.977677,-5.575116,-1.074757,-3.850157,5.828820,-3.314211,1.222658,-0.190329,-7.643402,-5.317198,4.302222,-8.557014,8.644632,1.860466,5.797992,0.455907,0.307459,2.779072,-7.521354,8.235481,1.318536,-7.589717,4.830247,5.373260,2.174655,-2.962935,-0.623868,-3.705639,-0.521055,-6.234423,-9.886189,-7.333963,7.213228,0.103950,8.342486,2.942654,-5.828467,-9.727634,-0.619689,2.040453,9.140400,8.670444,6.455619,7.877779,7.481735,0.070489,9.128391,0.900943,2.590052,3.122944,7.510387,-0.521193,-4.604804,0.899968,-7.912913,-5.885011,-6.490823,-8.374364,0.206235,3.001096,2.661296,-7.693864,-1.072054,1.154725,-7.658429,-7.483168,3.880589,-2.841964,6.356128,-6.380768,-1.691570,-8.754684,-5.299194,-9.470973,-6.524515,-9.970487,-5.373624,0.716343,-4.668195,4.273932,2.277806,-1.753463,-5.011357,-2.132834,-6.166618,9.717313,6.471657,6.021565,-8.492450,4.520959,8.700141,-9.159290,0.583740,-6.841725,-7.523472,-3.133189,-9.291297,-4.371953,3.641420,-2.905745,-8.579552,9.146817,9.493738,3.668446,-1.259035,1.649304,6.823489,-4.534762,9.715667,-5.711277,-1.499246,1.244026,-3.442692,5.518650,-0.698111,0.532718,0.427131,-0.102867,-3.579431,6.613980,-0.099158,-9.382453,-7.250733,-4.419130,-0.150136,-5.750213,-8.806373,6.398423,1.874761,-1.729874,-9.454995,-0.531013,-9.883122,2.764548,2.547644,-4.964063,5.030605,0.371447,1.667241,7.320570,-7.017656,-0.358252,7.103039,4.665094,-0.555991,-8.861069,-4.794421,-8.269184,2.649742,6.584908,-5.534214,-9.066430,-4.066215,-3.610729,-2.933768,1.153779,1.774517,0.641108,1.187837,0.348042,-0.355070,2.437816,4.881912,-3.226195,1.200601,1.879900,3.831160,6.598691,9.434753,7.223552,6.440448,-8.398246,-5.056453,4.964826,8.874014,4.266038,-8.441850,-4.310847,-3.140147,-2.264743,-4.625558,-2.814569,7.087317,0.176770,6.662885,-0.721461,-3.174307,6.441519,-8.674317,-5.270261,2.688924,-4.696363,-0.725480,3.008514,2.967217,-0.742989,4.696094,9.270923,-7.072867,5.362799,3.428330,-3.799664,6.917856,-3.396381,-6.403332,4.870880,-2.360274,6.109245,-6.824504,3.237595,-1.145467,6.303624,-9.727658,5.339622,3.286264,-5.660189,-4.463379,-3.872480,-4.203754,-9.964185,-8.444882,1.120402,2.221394,0.450789,5.136835,6.949020,6.853088,-3.357563,9.852582,-8.798349,-8.641125,1.588299,-1.885869,-6.692865,-5.409188,4.690551,-9.238253,5.505671,-1.777041,0.904406,6.351766,3.984864,9.496813,2.734640,7.902901,-8.940270,-7.574682,9.956604,6.067574,-3.007060,-7.103050,-5.155165,-4.850718,-7.877197,2.215526,-5.540646,-3.658093,8.624756,7.686368,-6.682391,-1.563559,4.724240,-4.663329,5.802049,-7.783151,9.755491,-6.982464,-8.299512,3.263739,5.935798,-0.571027,9.760722,6.972486,9.247069,7.687031,-8.036152,-8.457644,0.141331,-6.862970,-2.196813,-5.135241,2.051013,-1.277996,7.104158,-8.259898,-0.801359,-1.859847,9.945618,-1.557571,5.936745,-4.730383,9.030017,4.387724,6.934415,-2.087917,-4.023553,9.807292,5.461954,3.850875,8.530105,0.119735,7.163712,6.824881,8.768577,8.752980,-0.609848,-8.997033,-4.984240,-3.047612,1.150218,8.875193,2.922562,7.408280,-7.571359,2.337794,-8.796672,3.889746,-0.088304,-1.297326,-3.330120,-4.875501,3.166956,2.980598,-5.273683,2.344126,-3.781611,-9.110140,1.705499,-7.890055,-8.837993,8.900503,-8.640367,-1.903837,-8.877518,-2.119475,-0.101201,8.812904,-8.699587,6.723796,-3.615696,-1.078562,-4.555792,-3.562574,1.649030,8.306077,-0.717640,-3.707770,-2.033300,6.388734,-6.070871,7.367605,6.826818,-1.272075,8.695538,-3.057413,0.768041,-9.896341,7.959657,8.822092,6.551278,9.004166,-4.239079,-1.104531,-5.168816,2.030040,-3.222272,-8.918751,7.252476,6.370328,-9.076207,-0.755309,-3.095467,6.331762,4.024810,-0.292005,-3.124527,-1.766487,-2.687147,2.180511,-5.705631,4.078433,6.634862,-1.344855,-5.979090,-9.305630,-6.131364,-9.174994,2.451244,-1.327467,4.031356,-0.261608,-8.909240,-8.836678,7.147703,-0.554616,-6.303468,-5.088747,9.873856,-1.074025,-2.558133,-2.134862,1.513487,-4.196732,0.270780,7.455727,3.547185,-8.693632,-8.727318,-9.142057,-7.421400,6.474688,-1.123437,-6.275087,2.497979,-7.931966,1.970426,-2.908654,7.551962,-0.497844,3.567628,1.499819,0.970420,9.716908,-6.603163,3.452871,-5.662996,9.133438,9.369225,-1.853140,-2.882976,-1.069077,0.735116,-6.019620,1.257600,4.316749,-4.770787,-1.014494,-6.062525,4.469390,3.670275,3.241686,-2.743254,9.884240,5.912922,-5.096163,-4.810980,3.894682,1.619974,-5.929826,-2.353098,6.889025,1.281958,-7.602643,6.242745,-0.431866,1.549553,-3.285372,2.421180,5.592782,1.300444,-1.593197,-0.499074,-2.839261,-9.896550,2.123010,-0.723924,1.975194,-5.618143,-5.030214,-0.581530,-6.546106,-6.049568,6.194952,-1.823969,-2.388631,-8.559152,1.726982,8.039540], dtype = "float32")#candidate|3491|(1040,)|const|float32
call_3490 = relay.TupleGetItem(func_3226_call(relay.reshape(const_3491.astype('float32'), [13, 10, 8]), relay.reshape(uop_3449.astype('float32'), [1152,]), ), 2)
call_3492 = relay.TupleGetItem(func_3230_call(relay.reshape(const_3491.astype('float32'), [13, 10, 8]), relay.reshape(uop_3449.astype('float32'), [1152,]), ), 2)
uop_3496 = relay.cosh(call_3446.astype('float64')) # shape=(1152,)
uop_3498 = relay.cosh(call_3447.astype('float64')) # shape=(1152,)
output = relay.Tuple([uop_3449,uop_3456,call_3459,call_3466,const_3467,call_3485,call_3487,call_3490,const_3491,uop_3496,])
output2 = relay.Tuple([uop_3451,uop_3458,call_3460,call_3468,const_3467,call_3486,call_3488,call_3492,const_3491,uop_3498,])
func_3526 = relay.Function([], output)
mod['func_3526'] = func_3526
mod = relay.transform.InferType()(mod)
output = func_3526()
func_3527 = relay.Function([], output)
mutated_mod['func_3527'] = func_3527
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3555 = relay.const([[[6.716368,8.757534,6.836037,3.398981,4.327824,5.622667,8.602922,-5.511750,3.197612,-4.192753,-6.788547,-7.409142,-8.601549,-0.309702],[-6.556846,4.878234,8.420135,-0.619509,-9.614955,-0.895282,-3.523468,3.301624,-6.897018,3.944267,-8.999860,6.191704,-4.473823,-3.732573]],[[-5.641839,-9.403887,9.959172,2.776011,-9.663094,8.637837,4.703144,-5.464388,-0.378025,8.283195,4.289922,-0.090711,-4.492077,1.276128],[2.565855,-9.681887,-4.656667,-2.374870,-8.479877,-0.055749,8.044742,8.465715,4.528691,-0.235380,-7.684978,-4.616298,7.885716,6.394519]],[[0.383618,-8.521830,-7.871024,-1.505343,7.471868,-6.190025,-8.064792,8.536700,4.045281,3.527433,-9.061198,-1.574315,0.532267,2.338184],[0.229634,7.319500,5.937048,-7.098677,-3.278993,-7.231106,4.128033,4.323329,7.659481,-5.606553,5.316448,1.731088,9.633713,-5.503861]],[[-4.090487,6.619011,-2.803466,-1.357928,9.753335,-4.658632,-1.841839,1.416029,5.286016,9.387076,5.929367,6.067070,8.591602,7.244889],[-4.817123,-7.269588,9.434608,7.668690,-4.620785,0.912457,-8.563682,0.726863,-2.821782,-8.374187,1.889432,-1.935739,2.097390,2.167386]],[[-3.125760,-4.046227,3.259220,0.373830,-0.522546,-8.357347,2.844816,-5.489203,3.039195,-5.069419,8.029990,-1.456091,-6.697205,9.373349],[-7.955022,5.350428,7.209942,-9.445372,-0.428845,8.975348,-4.078911,4.249532,6.579659,5.164309,1.047882,-7.246010,-6.536573,0.232263]],[[2.535514,3.338018,3.177635,-9.806153,-6.259546,2.405160,3.052372,0.642695,2.110366,3.177287,4.853445,9.354845,-1.052440,2.299743],[-0.464829,9.436445,8.748003,-2.960434,5.432327,-7.525373,9.160800,-1.170118,-1.240657,-1.314427,-7.169900,0.829486,-1.483095,-7.396371]],[[-4.272730,1.749660,-1.373781,6.054740,8.839055,9.710405,-0.671328,-2.940087,9.763710,-9.008416,5.050574,9.626571,-1.958073,2.181534],[-8.319096,2.700204,2.542277,1.757922,-8.810947,7.803878,-3.716906,-5.147136,-2.997507,-9.043937,-4.627381,-6.440165,3.902223,8.135633]],[[-3.435931,-4.938394,9.096125,4.490410,3.232103,-5.305592,7.848502,3.405566,-9.821034,9.751441,2.912035,5.176700,-7.100134,7.504425],[2.083208,-9.535063,3.313327,-5.141678,-8.404932,9.078937,0.337140,1.347753,2.421276,-2.720814,1.136116,0.925506,-1.108650,-1.579096]],[[-7.356409,-9.560668,-7.484131,6.412992,-9.908155,-5.988898,8.441743,-6.281530,-4.067482,-8.528968,-6.716386,8.040091,-9.192523,-2.728824],[7.425887,3.858102,-1.297978,-1.163506,-6.731388,-9.435010,1.136426,-0.980433,-9.878251,4.139662,-3.615104,7.561799,2.368061,-3.809121]],[[3.629460,-4.281823,6.499826,-6.432114,8.313839,1.951730,-4.667739,-5.976612,-7.311304,-0.153171,2.810423,2.760191,0.243267,4.548965],[-9.080164,-4.506916,-3.092093,-9.761577,4.818101,-4.565692,6.655540,-6.726254,5.417046,-5.321975,7.113443,9.055075,-7.363175,8.260799]],[[0.999402,-0.395417,-2.682680,8.926172,0.406220,9.220433,-1.925748,-5.415143,5.187863,1.148488,5.238269,-4.172952,-5.653254,-2.360653],[8.364097,5.135910,-8.084619,-3.335019,-2.657499,8.028224,5.568775,-6.614012,-2.804965,-0.421003,-5.404621,1.626532,2.491066,-6.837401]]], dtype = "float32")#candidate|3555|(11, 2, 14)|const|float32
uop_3556 = relay.tan(const_3555.astype('float32')) # shape=(11, 2, 14)
output = uop_3556
output2 = uop_3556
func_3561 = relay.Function([], output)
mod['func_3561'] = func_3561
mod = relay.transform.InferType()(mod)
output = func_3561()
func_3562 = relay.Function([], output)
mutated_mod['func_3562'] = func_3562
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3572 = relay.var("var_3572", dtype = "float64", shape = (13, 5, 13))#candidate|3572|(13, 5, 13)|var|float64
uop_3573 = relay.cosh(var_3572.astype('float64')) # shape=(13, 5, 13)
uop_3583 = relay.exp(var_3572.astype('float32')) # shape=(13, 5, 13)
func_3427_call = mod.get_global_var('func_3427')
func_3430_call = mutated_mod.get_global_var('func_3430')
var_3587 = relay.var("var_3587", dtype = "uint16", shape = (180,))#candidate|3587|(180,)|var|uint16
call_3586 = relay.TupleGetItem(func_3427_call(relay.reshape(var_3587.astype('uint16'), [180,])), 2)
call_3588 = relay.TupleGetItem(func_3430_call(relay.reshape(var_3587.astype('uint16'), [180,])), 2)
output = relay.Tuple([uop_3573,uop_3583,call_3586,var_3587,])
output2 = relay.Tuple([uop_3573,uop_3583,call_3588,var_3587,])
func_3595 = relay.Function([var_3572,var_3587,], output)
mod['func_3595'] = func_3595
mod = relay.transform.InferType()(mod)
mutated_mod['func_3595'] = func_3595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3595_call = mutated_mod.get_global_var('func_3595')
var_3597 = relay.var("var_3597", dtype = "float64", shape = (13, 5, 13))#candidate|3597|(13, 5, 13)|var|float64
var_3598 = relay.var("var_3598", dtype = "uint16", shape = (180,))#candidate|3598|(180,)|var|uint16
call_3596 = func_3595_call(var_3597,var_3598,)
output = call_3596
func_3599 = relay.Function([var_3597,var_3598,], output)
mutated_mod['func_3599'] = func_3599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_3634 = relay.TupleGetItem(func_2562_call(), 3)
call_3635 = relay.TupleGetItem(func_2563_call(), 3)
func_2263_call = mod.get_global_var('func_2263')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_3638 = relay.TupleGetItem(func_2263_call(relay.reshape(call_3634.astype('uint16'), [180,])), 2)
call_3639 = relay.TupleGetItem(func_2266_call(relay.reshape(call_3634.astype('uint16'), [180,])), 2)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_3649 = relay.TupleGetItem(func_2562_call(), 1)
call_3650 = relay.TupleGetItem(func_2563_call(), 1)
func_3258_call = mod.get_global_var('func_3258')
func_3261_call = mutated_mod.get_global_var('func_3261')
call_3659 = relay.TupleGetItem(func_3258_call(relay.reshape(call_3649.astype('float32'), [1152,])), 2)
call_3660 = relay.TupleGetItem(func_3261_call(relay.reshape(call_3649.astype('float32'), [1152,])), 2)
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_3664 = func_2502_call()
call_3665 = func_2502_call()
output = relay.Tuple([call_3634,call_3638,call_3649,call_3659,call_3664,])
output2 = relay.Tuple([call_3635,call_3639,call_3650,call_3660,call_3665,])
func_3669 = relay.Function([], output)
mod['func_3669'] = func_3669
mod = relay.transform.InferType()(mod)
mutated_mod['func_3669'] = func_3669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3669_call = mutated_mod.get_global_var('func_3669')
call_3670 = func_3669_call()
output = call_3670
func_3671 = relay.Function([], output)
mutated_mod['func_3671'] = func_3671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_3674 = relay.TupleGetItem(func_2168_call(), 0)
call_3675 = relay.TupleGetItem(func_2169_call(), 0)
output = call_3674
output2 = call_3675
func_3689 = relay.Function([], output)
mod['func_3689'] = func_3689
mod = relay.transform.InferType()(mod)
mutated_mod['func_3689'] = func_3689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3689_call = mutated_mod.get_global_var('func_3689')
call_3690 = func_3689_call()
output = call_3690
func_3691 = relay.Function([], output)
mutated_mod['func_3691'] = func_3691
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3733 = relay.var("var_3733", dtype = "int32", shape = ())#candidate|3733|()|var|int32
var_3734 = relay.var("var_3734", dtype = "int32", shape = (13, 14, 12))#candidate|3734|(13, 14, 12)|var|int32
bop_3735 = relay.greater(var_3733.astype('bool'), var_3734.astype('bool')) # shape=(13, 14, 12)
func_2860_call = mod.get_global_var('func_2860')
func_2862_call = mutated_mod.get_global_var('func_2862')
call_3742 = relay.TupleGetItem(func_2860_call(), 0)
call_3743 = relay.TupleGetItem(func_2862_call(), 0)
func_3427_call = mod.get_global_var('func_3427')
func_3430_call = mutated_mod.get_global_var('func_3430')
var_3747 = relay.var("var_3747", dtype = "uint16", shape = (180,))#candidate|3747|(180,)|var|uint16
call_3746 = relay.TupleGetItem(func_3427_call(relay.reshape(var_3747.astype('uint16'), [180,])), 1)
call_3748 = relay.TupleGetItem(func_3430_call(relay.reshape(var_3747.astype('uint16'), [180,])), 1)
func_3561_call = mod.get_global_var('func_3561')
func_3562_call = mutated_mod.get_global_var('func_3562')
call_3752 = func_3561_call()
call_3753 = func_3561_call()
output = relay.Tuple([bop_3735,call_3742,call_3746,var_3747,call_3752,])
output2 = relay.Tuple([bop_3735,call_3743,call_3748,var_3747,call_3753,])
func_3757 = relay.Function([var_3733,var_3734,var_3747,], output)
mod['func_3757'] = func_3757
mod = relay.transform.InferType()(mod)
var_3758 = relay.var("var_3758", dtype = "int32", shape = ())#candidate|3758|()|var|int32
var_3759 = relay.var("var_3759", dtype = "int32", shape = (13, 14, 12))#candidate|3759|(13, 14, 12)|var|int32
var_3760 = relay.var("var_3760", dtype = "uint16", shape = (180,))#candidate|3760|(180,)|var|uint16
output = func_3757(var_3758,var_3759,var_3760,)
func_3761 = relay.Function([var_3758,var_3759,var_3760,], output)
mutated_mod['func_3761'] = func_3761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_3819 = func_2502_call()
call_3820 = func_2502_call()
func_2860_call = mod.get_global_var('func_2860')
func_2862_call = mutated_mod.get_global_var('func_2862')
call_3850 = relay.TupleGetItem(func_2860_call(), 0)
call_3851 = relay.TupleGetItem(func_2862_call(), 0)
output = relay.Tuple([call_3819,call_3850,])
output2 = relay.Tuple([call_3820,call_3851,])
func_3867 = relay.Function([], output)
mod['func_3867'] = func_3867
mod = relay.transform.InferType()(mod)
output = func_3867()
func_3868 = relay.Function([], output)
mutated_mod['func_3868'] = func_3868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3526_call = mod.get_global_var('func_3526')
func_3527_call = mutated_mod.get_global_var('func_3527')
call_3873 = relay.TupleGetItem(func_3526_call(), 9)
call_3874 = relay.TupleGetItem(func_3527_call(), 9)
func_3669_call = mod.get_global_var('func_3669')
func_3671_call = mutated_mod.get_global_var('func_3671')
call_3898 = relay.TupleGetItem(func_3669_call(), 3)
call_3899 = relay.TupleGetItem(func_3671_call(), 3)
func_1295_call = mod.get_global_var('func_1295')
func_1301_call = mutated_mod.get_global_var('func_1301')
const_3910 = relay.const([6.618044,-3.334688,-1.192559,9.871754,-4.832599,6.013840,6.756898,9.024099,6.279718,7.802598,9.008173,9.623246,2.086364,2.983890,-0.032568,-3.172865,0.061347,-4.717524,-7.736172,-4.119552,6.441400,-0.648694,7.150471,0.173655,3.242510,-4.178721,-2.896768,3.320074,5.492148,7.090197,7.989555,2.054789,-6.311500,7.261310,1.341505,5.522539,6.304497,0.932069,-4.897313,-4.399497,5.899008,-9.194743,-1.524339,0.259863,-3.677253,4.375939,-0.748873,-9.532558,-4.860697,-7.861663,-7.026801,-5.784544,9.040045,-7.696411,-9.832688,8.786676,0.576957,-5.511595,-7.635707,1.924526,-0.168492,-0.762424,-9.141382,3.066857,-5.787870,-9.149199,-3.945803,0.272310,2.148301,8.810894,-4.704124,0.082016,-2.316696,9.522188,-4.611566,-6.380333,5.969530,9.383091,8.509313,-1.809157,-9.446019,-7.852620,7.818014,2.293354,8.772158,9.611611,4.937476,2.070202,-4.172830,-7.310843,-4.506731,6.029200,-4.251268,4.024213,7.200713,6.980186,-7.461174,-7.936777,7.595252,-2.621527,-5.187185,-6.364411,0.265489,-0.704525,-5.820278,-1.579960,8.487305,-0.821722,-0.460893,8.416022,4.118724,-4.215451,1.484768,-1.990448,-8.869820,0.258739,-0.771049,-2.026141,-7.414399,4.043928,-1.186076,4.405496,6.578805,1.378535,4.715030,9.352000,8.659071,-0.632677,3.075475,-9.989286,-0.443154,-2.042153,2.556629,-4.059972,8.505722,9.190626,9.652657,4.685843,-2.469904,-2.470639,-9.803240,0.839151,2.236257,-8.098056,-2.665984,-5.833550,-0.426668,4.441285,-4.844354,0.168882,4.886310,0.974128,8.372678,0.042852,3.004205,5.997227,3.615460,4.959571,7.805634,4.099990,-8.477115,-4.681482,1.404564,2.295794,2.493191,5.866345,2.950743,5.580277,-0.574075,-4.805258,-7.021799,2.329875,-9.651705,2.730240,-6.048331,4.276750,-2.254120,7.477910,4.869029,3.829485,-5.625596,5.493365,2.996002,-8.209623,4.865427,5.413858,8.768561,-2.286093,-2.371840,7.306676,-3.102507,9.652906,-6.907329,-8.713572,6.838632,-9.848243,5.345207,9.721945,-2.783888,-6.538339,6.325047,1.344349,-4.656771,-4.548163,5.008226,8.331553,0.210946,7.197824,2.545199,2.735491,4.489890,-8.732248,-7.812476,-3.389717,-5.962129,-4.752114,-7.310238,-4.747398,4.250942,9.167680,-4.712634,4.784223,-9.525095,4.200097,-7.702022,-6.504403,-6.442519,-0.274045,0.164262,4.669027,8.494212,7.891688,4.708489,-4.225974,-9.548613,-6.854108,-5.585670,-5.321186,-2.124755,1.777609,6.998505,-2.018009,-2.596419,-3.388288,7.092160,3.753098,4.491524,7.944379,-6.298448,-4.776311,8.450612,0.186558,-2.248354,-2.778316,9.770955,1.354161,-1.594858,-9.119209,0.648986,-3.320808,-9.558134,1.052269,-6.746059,0.387164,1.794102,0.081477,-3.405971,-3.302047,3.813509,5.995430,-1.885622,4.611073,-0.468684,-6.871788,-8.951132,3.607642,-2.568214,-9.996756,0.875109,-4.681919,2.008367,8.736057,-4.094832,-2.949105,3.685755,9.469546], dtype = "float32")#candidate|3910|(286,)|const|float32
const_3911 = relay.const([10,-3,-7,10,10,-7,-9,-6,3,8,-9,4,1,3,7,4,-5,6,5,-10,-5,4,5,-10,-10,-8,7,2,-3,-1,-8,-10,1,7,-9,3,-7,9,-8,10,7,-8,-9,-4,9,5,-8,10,-10,-9,7,4,-8,-6,1,-8,-4,-5,-1,5,2,-7,4,4,-6,2,5,-7,-8,1,9,-10,-8,-3,-3,6,8,-8,1,-4,-4,-8,2,-2,-8,-10,2,7,-2,-6,-1,-2,8,-9,3,3,2,8,1,-2,5,-6,-9,-7,-5,10,9,-5,2,-3,-9,-4,-2,-5,-2,-1,-9,4,-2,-3,-5,-5,2,1,-5,-1,-3,-7,7,9,9,8,9,-7,2,9,2,-4,-5,-10,-9,5,8,-8,-4,-6,-9,4,-4,-10,-3,-8,7,1,4,2,-4,5,9,-7,-2,-9,-7,2,5,10,3,3,9,-1,9,4,10,-7,5,-5,7,2,8,7], dtype = "uint16")#candidate|3911|(180,)|const|uint16
var_3912 = relay.var("var_3912", dtype = "bool", shape = ())#candidate|3912|()|var|bool
var_3913 = relay.var("var_3913", dtype = "bool", shape = (1404,))#candidate|3913|(1404,)|var|bool
call_3909 = relay.TupleGetItem(func_1295_call(relay.reshape(const_3910.astype('float32'), [2, 13, 11]), relay.reshape(const_3911.astype('uint16'), [180,]), relay.reshape(var_3912.astype('bool'), []), relay.reshape(var_3913.astype('bool'), [12, 9, 13]), ), 1)
call_3914 = relay.TupleGetItem(func_1301_call(relay.reshape(const_3910.astype('float32'), [2, 13, 11]), relay.reshape(const_3911.astype('uint16'), [180,]), relay.reshape(var_3912.astype('bool'), []), relay.reshape(var_3913.astype('bool'), [12, 9, 13]), ), 1)
func_1120_call = mod.get_global_var('func_1120')
func_1125_call = mutated_mod.get_global_var('func_1125')
call_3915 = relay.TupleGetItem(func_1120_call(relay.reshape(call_3909.astype('float32'), [9, 1, 15]), relay.reshape(call_3898.astype('float32'), [1152,]), relay.reshape(const_3911.astype('uint16'), [180, 1]), ), 0)
call_3916 = relay.TupleGetItem(func_1125_call(relay.reshape(call_3909.astype('float32'), [9, 1, 15]), relay.reshape(call_3898.astype('float32'), [1152,]), relay.reshape(const_3911.astype('uint16'), [180, 1]), ), 0)
func_3226_call = mod.get_global_var('func_3226')
func_3230_call = mutated_mod.get_global_var('func_3230')
const_3919 = relay.const([-3.125420,4.127141,7.106207,-6.776151,-6.728516,-5.328834,-6.016538,-9.492360,-6.446278,-2.941658,2.101244,-2.492763,-6.041936,-7.277771,7.372362,0.972049,8.203018,5.649169,-5.398973,3.008207,-6.651450,8.506138,-1.013987,-9.292286,6.197720,1.491443,9.854416,9.357015,-5.834493,1.492820,3.148071,0.356494,6.839320,-5.482092,-8.952529,-7.727486,3.507379,2.412570,-2.560732,-9.209460,-6.922593,-2.095029,8.583626,-6.661770,-5.494529,-2.253798,-1.179236,-8.868435,-8.410142,5.636260,-2.333224,6.371146,8.249502,-8.486452,-5.925547,4.855125,-2.575164,-6.259482,4.003532,1.259658,8.692520,-4.337012,2.811410,1.597119,7.408600,2.511193,9.033855,6.276217,8.168830,-3.621838,-4.821883,0.892527,0.366139,2.727623,-6.915990,-3.056662,-3.848913,3.759533,-7.444256,3.483746,5.481297,0.963853,2.186897,5.059059,-6.361845,-7.009302,-7.452809,-5.905389,-8.700345,-3.605736,-4.178622,-7.928584,2.841736,4.111701,-2.755767,7.790548,2.124539,-5.452538,2.110742,5.914418,4.579293,0.370924,5.174083,-1.194334,3.295094,-9.501476,9.329712,-3.474439,-9.684018,-4.897873,-9.334501,-1.031182,2.062438,-0.436267,2.665238,-3.249117,4.214711,-7.422344,9.109502,-2.501980,4.020741,4.626453,0.953473,-7.901260,8.451176,8.221824,-5.313883,1.622428,-4.889913,0.452152,3.199593,5.298838,0.487922,-4.702816,-6.035106,4.272760,1.427611,-2.593899,-6.590264,1.285536,-4.566606,9.034318,-9.467572,-4.507077,-9.649411,-0.513437,2.200253,-0.412775,9.555147,-3.673384,-4.989702,-4.242350,-4.396439,-3.764475,4.741189,-8.773798,-4.557306,-2.416974,-9.380084,-3.540197,-0.238934,-5.249031,-6.593138,-4.854624,2.790603,9.045235,-6.377089,-8.714510,-0.512883,0.954940,-7.334850,1.111222,4.972388,6.719879,-5.978873,-4.966691,7.293183,5.930948,-1.401443,8.693897,-4.739166,2.113087,-4.650587,8.380933,-4.615051,-4.694591,-4.147450,-0.770710,-7.842197,0.797119,9.330243,4.203662,-7.200732,-5.433307,3.487280,6.972551,-0.898742,-5.155638,-8.975688,7.303554,3.124330,4.904474,-1.311890,4.946082,2.564341,2.518182,9.833241,2.925312,4.896812,-6.570598,-5.291730,-7.821098,-8.789426,6.030190,-7.055761,7.476666,2.442270,9.712492,-6.290038,-8.482900,0.101946,-6.501004,-5.290947,3.697179,4.663112,-9.118560,6.202157,-1.924794,-6.448448,-8.177683,4.491873,-0.406196,-6.953442,-9.074323,-1.434143,-1.334463,-7.441143,-9.675858,7.919440,7.202132,8.317904,-4.458212,-1.070161,-3.882129,-8.508866,-5.099258,5.862095,-0.047627,-7.283324,-2.052329,7.084633,4.106064,-9.196950,7.047925,9.769277,-5.453723,-3.119314,0.609800,-4.545558,8.256403,-2.806715,-0.381786,-9.551763,8.275955,4.730926,-2.071893,-7.396003,-4.136230,1.471154,-0.666886,-5.023729,-6.566616,6.596944,-2.392217,4.506517,0.869888,8.500531,5.289685,-9.467652,-7.170133,3.435929,0.845783,-6.658260,-2.356664,9.500113,-8.828520,1.763881,-3.662302,-8.301285,-4.413549,0.176439,7.545077,1.178096,-2.492449,4.854721,1.453363,4.683048,1.509002,4.088718,-4.261667,-6.428943,-9.584237,7.151581,6.577774,0.511599,7.629844,6.791082,4.178938,-6.215373,-1.072168,1.313158,-8.201821,-7.367632,-2.190206,0.524741,-0.797995,-3.485303,0.727360,-3.392309,3.569245,3.954620,-3.459243,-3.076472,9.355925,6.831580,-4.709456,-3.213545,-4.313080,-8.489920,-3.601645,8.127724,-5.434248,3.065411,2.941092,-3.315035,-9.195550,1.733977,-2.505828,-2.620776,-5.254149,0.027897,-3.239853,9.755410,5.726263,-8.125400,4.425717,-2.873278,1.255565,-8.610188,9.489338,9.660358,-6.187674,-9.052713,-4.564097,-7.613034,7.131083,-6.729461,6.352604,-5.078116,0.644995,-2.258933,-0.617695,-2.424042,9.791765,-2.023616,4.049068,-3.661549,-3.511008,-8.520564,9.361500,-5.675593,7.246047,2.209645,-5.239907,0.338241,-6.836239,3.071731,-1.478903,-5.871836,-7.148523,6.094806,-0.520531,4.904414,-9.530864,-9.508692,-1.980514,-9.154775,9.429130,3.521747,5.765666,5.471224,-1.780696,-1.169705,6.854113,-4.092497,5.998469,3.222078,4.611715,4.876617,2.162667,-9.071405,-0.526016,1.305866,-4.301740,6.399152,4.341161,4.333453,5.320637,-8.657319,-0.692400,-1.455703,-1.422729,8.604637,-2.968474,-8.926287,-1.550864,-4.234074,8.690888,-2.329400,-5.186910,-7.406109,4.849299,3.137340,6.706004,1.456743,7.897853,-6.926068,0.108288,8.157475,-5.115106,7.032224,-5.146555,0.337378,2.148869,8.088211,5.718043,1.379974,1.878928,-1.792972,0.169331,-8.740426,9.573041,-5.237947,5.678547,9.400809,4.860698,-3.246385,-7.350020,-8.886810,-9.472229,1.233968,4.367713,-1.896680,9.564386,4.933720,-2.762359,7.980707,-2.559611,-7.709702,-0.152270,4.833024,5.886344,6.394610,8.776409,2.693300,-2.309671,-6.593463,-0.952528,-5.560660,5.677272,-8.352497,-0.843053,2.942460,7.447338,-9.105644,7.444080,-5.718252,9.287645,-3.373801,0.424448,-2.838586,-9.541178,9.917333,1.730068,1.552835,6.325184,-1.474059,8.301549,0.556456,-7.434280,-6.771315,3.094933,-3.693578,2.117056,-1.282224,-3.227222,-6.438735,0.039148,2.573393,4.425886,8.460400,-4.486850,-2.723004,1.060480,6.674882,4.784250,-5.095008,-6.106365,-0.949818,6.513052,-5.856779,6.289790,0.411583,-9.575134,-6.464683,5.996103,-1.098046,9.807462,3.359340,-5.240008,-2.928983,8.964097,8.862936,4.464729,6.674162,-4.782238,0.097628,-0.785165,-8.683712,8.302014,-2.224565,-3.289096,3.087292,-8.687795,-2.592535,8.016736,-2.719407,5.024555,-4.000586,3.236272,-1.536897,7.071557,-1.634052,-2.472666,-3.059411,4.734568,-4.760184,9.095367,7.697007,-3.818290,2.789290,3.705071,-5.590344,1.358480,6.038170,-2.373214,-6.193322,2.087834,4.788714,1.794248,-6.427218,9.402877,-0.630777,-6.152877,-4.398692,0.157464,-4.030117,7.600842,-5.427611,8.144215,-3.224515,1.132939,9.722453,3.258809,-1.743454,-9.165798,3.986807,7.398356,-0.685391,0.412633,-6.113519,-5.972682,2.992516,-2.049012,-6.104294,-2.763100,2.016642,9.496399,-2.400693,-3.087180,9.229067,0.443345,-5.425223,-3.615086,-7.848481,2.025165,8.246826,5.025155,4.140548,-2.213299,0.763971,-4.949478,-2.437304,6.216980,-7.445220,0.725246,-3.163847,-5.224513,2.428776,-5.856266,3.925280,-9.261731,9.902139,6.901880,2.169052,5.368473,-9.123411,-7.998592,3.761932,-8.442466,2.248260,-1.786523,-4.509498,-3.013583,2.040832,-4.194060,-4.778751,6.043754,-3.066235,-4.548009,-4.225837,0.936754,-6.255172,4.056870,7.153900,8.506155,3.573724,9.730389,7.114764,0.903506,-4.646915,4.938142,7.961253,-4.077735,6.893107,6.926508,-4.093967,1.588751,-8.346842,3.359789,-8.801293,-4.593798,-2.645539,2.804625,8.047738,-5.952852,-0.780240,-8.598034,2.601862,-0.575958,-4.022165,-3.439857,-6.574835,8.174044,3.153956,-7.401743,1.738131,0.812796,-5.773024,9.785879,-3.005717,8.144210,5.879077,-6.224444,6.493410,-4.216650,-6.930087,-5.824136,-9.063259,-6.334961,-7.953212,4.541783,7.282007,1.090688,5.573683,-6.562804,6.905663,8.370323,4.924291,5.007219,-3.531738,-6.756858,-4.498321,6.133729,-0.328817,-2.729263,-7.840622,6.882803,3.954679,-5.626940,1.068178,-0.325490,-0.194949,-4.264708,8.875766,-1.830572,0.087031,-2.811899,-3.205195,-6.152882,8.043766,3.638508,-2.592537,-0.910490,-6.840916,-6.896054,3.959190,-7.451506,-7.784706,5.260243,-8.083301,9.709964,7.920299,1.611109,3.398761,-0.732526,2.637572,8.892106,-6.173753,4.472434,-2.080305,8.190216,-6.475858,1.090525,-4.064499,-7.575396,4.453121,-7.789221,4.894374,-8.460542,5.847158,-6.613022,-3.022331,-8.598091,5.328488,3.762452,1.727603,8.549164,-0.060221,0.467108,4.466222,8.032795,5.607489,7.820695,-4.104747,-2.954725,5.117432,-1.215460,-6.534042,-8.218483,-9.854723,3.724767,-7.827175,0.302253,0.217186,4.663861,-9.977157,3.968818,-1.892935,-2.515814,-8.904954,-7.727235,0.670407,-8.391010,9.163639,2.705694,-2.612979,-4.984509,1.413995,-3.764701,-2.689745,-6.091411,-7.284537,-6.893347,-5.769219,2.615215,3.895457,-0.644020,-4.105082,-2.484849,-9.048779,4.331724,-7.408366,8.992832,9.547318,7.814208,-5.458936,-2.854964,5.948729,6.754888,-0.437809,8.073491,9.685066,-6.346460,-0.546962,2.018005,7.575817,7.672863,-3.406074,8.420862,-7.222496,4.369695,-6.179190,-0.343244,1.400059,-8.212311,-4.156464,3.192681,2.941499,-8.847206,0.949407,-2.726254,-9.352812,-3.523431,6.208388,1.742080,-8.348810,-7.216213,-7.944185,1.200203,-4.366926,3.306506,7.726776,-9.200921,0.085506,-6.652306,9.153513,3.732602,-4.008992,-8.927503,6.397071,-1.320204,7.998542,2.842535,2.610681,0.199155,-1.280744,-9.488229,2.944500,-6.633549,9.604899,5.366631,-5.025218,5.602980,2.118403,-9.553197,7.580722,-8.912387,6.155351,-6.262633,-2.907017,-6.986589,9.507882,-7.966022,-7.696691,9.489052,0.995283,-3.707897,4.846470,8.629792,2.820791,9.464650,-0.870583,4.860843,8.653676,-6.776436,8.766481,-7.326097,3.203216,-3.936399,-7.005859,-5.782082,-0.188471,0.392760,-4.928265,-2.528973,-1.016074,-0.856363,-0.299513,-1.249750,9.650919,1.508283,7.168078,2.033091,5.947239,-3.739159,3.156939,1.429219,2.761320,4.751447,1.398430,-8.554484,-0.912898,-5.639700,-4.709574,-1.307719,4.885372,6.838481,-9.390383,-0.096878,-5.409573,2.303627,3.522595,9.936860,7.259219,-7.741315,2.100184,-7.234360,5.255628,-9.940344,4.748403,9.846438,-9.329839,0.951241,-4.324255,-9.019500,7.440714,-8.716752,8.605723,3.170605,6.413515,7.791792,-2.637496,-0.052319,2.621899,-9.286452,4.554444,9.035364,-3.728019,-7.553772,-7.373633,0.730309,-7.047587,-2.135796,0.820503,-4.628296,5.058098,0.214765,1.470857,1.202820,-9.041287,7.528702,-4.554970,-9.144765,-7.155246,2.234731,5.108123,-1.451848,-7.264293,3.319636,-1.088113,-7.234752,-2.652435,-8.470172,5.981360,-2.130429,5.432985,-5.298632,-3.070171,-2.053243,4.740153,-1.862601,-7.737723,6.531729,7.175277,-8.035002,-7.021828,-2.674584,0.655413,0.625898,-8.108527,-9.156200,9.414260,8.486692,9.032191,-7.108139,1.963618,-0.370514,5.428565,2.813906,-2.471650,1.960283,-5.094747,6.012659,-2.417898,2.469042,-5.808015,-2.479070,-2.311531,-3.190083,4.677262,-6.156104,5.842119,-8.517175,-7.561889,5.603528,9.378257,-0.011917,-9.714006,3.942336,-2.312184,-8.028336,4.183106,-3.418368,-5.995203,3.683126,-8.461622,9.854741,-4.565384,-2.659168,4.811082,-9.323685,-8.557125,-2.659628,-7.755394,4.847589,-9.049159,-3.848429,-9.193364,1.728131,8.630603,-8.708497,7.561557,7.160255,5.396186,-4.446971,3.070896,-4.667244,0.874513,9.084282], dtype = "float32")#candidate|3919|(1040,)|const|float32
call_3918 = relay.TupleGetItem(func_3226_call(relay.reshape(const_3919.astype('float32'), [13, 10, 8]), relay.reshape(call_3898.astype('float32'), [1152,]), ), 6)
call_3920 = relay.TupleGetItem(func_3230_call(relay.reshape(const_3919.astype('float32'), [13, 10, 8]), relay.reshape(call_3898.astype('float32'), [1152,]), ), 6)
func_3867_call = mod.get_global_var('func_3867')
func_3868_call = mutated_mod.get_global_var('func_3868')
call_3921 = relay.TupleGetItem(func_3867_call(), 1)
call_3922 = relay.TupleGetItem(func_3868_call(), 1)
uop_3929 = relay.exp(const_3910.astype('float64')) # shape=(286,)
func_3095_call = mod.get_global_var('func_3095')
func_3098_call = mutated_mod.get_global_var('func_3098')
call_3931 = relay.TupleGetItem(func_3095_call(relay.reshape(call_3918.astype('uint16'), [180,])), 0)
call_3932 = relay.TupleGetItem(func_3098_call(relay.reshape(call_3918.astype('uint16'), [180,])), 0)
output = relay.Tuple([call_3873,call_3898,call_3909,const_3911,var_3912,var_3913,call_3915,call_3918,const_3919,call_3921,uop_3929,call_3931,])
output2 = relay.Tuple([call_3874,call_3899,call_3914,const_3911,var_3912,var_3913,call_3916,call_3920,const_3919,call_3922,uop_3929,call_3932,])
func_3934 = relay.Function([var_3912,var_3913,], output)
mod['func_3934'] = func_3934
mod = relay.transform.InferType()(mod)
var_3935 = relay.var("var_3935", dtype = "bool", shape = ())#candidate|3935|()|var|bool
var_3936 = relay.var("var_3936", dtype = "bool", shape = (1404,))#candidate|3936|(1404,)|var|bool
output = func_3934(var_3935,var_3936,)
func_3937 = relay.Function([var_3935,var_3936,], output)
mutated_mod['func_3937'] = func_3937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_3977 = relay.TupleGetItem(func_2168_call(), 0)
call_3978 = relay.TupleGetItem(func_2169_call(), 0)
output = relay.Tuple([call_3977,])
output2 = relay.Tuple([call_3978,])
func_3981 = relay.Function([], output)
mod['func_3981'] = func_3981
mod = relay.transform.InferType()(mod)
output = func_3981()
func_3982 = relay.Function([], output)
mutated_mod['func_3982'] = func_3982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_4001 = func_2502_call()
call_4002 = func_2502_call()
uop_4009 = relay.tan(call_4001.astype('float64')) # shape=(12, 6, 10)
uop_4011 = relay.tan(call_4002.astype('float64')) # shape=(12, 6, 10)
bop_4023 = relay.logical_xor(uop_4009.astype('int16'), relay.reshape(call_4001.astype('int16'), relay.shape_of(uop_4009))) # shape=(12, 6, 10)
bop_4026 = relay.logical_xor(uop_4011.astype('int16'), relay.reshape(call_4002.astype('int16'), relay.shape_of(uop_4011))) # shape=(12, 6, 10)
func_631_call = mod.get_global_var('func_631')
func_636_call = mutated_mod.get_global_var('func_636')
var_4041 = relay.var("var_4041", dtype = "float32", shape = (1152,))#candidate|4041|(1152,)|var|float32
var_4042 = relay.var("var_4042", dtype = "uint16", shape = (180,))#candidate|4042|(180,)|var|uint16
call_4040 = relay.TupleGetItem(func_631_call(relay.reshape(var_4041.astype('float32'), [16, 12, 6]), relay.reshape(var_4042.astype('uint16'), [180,]), relay.reshape(var_4042.astype('uint16'), [5, 6, 6]), ), 3)
call_4043 = relay.TupleGetItem(func_636_call(relay.reshape(var_4041.astype('float32'), [16, 12, 6]), relay.reshape(var_4042.astype('uint16'), [180,]), relay.reshape(var_4042.astype('uint16'), [5, 6, 6]), ), 3)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_4049 = relay.TupleGetItem(func_261_call(relay.reshape(call_4040.astype('uint16'), [5, 6, 6])), 0)
call_4050 = relay.TupleGetItem(func_263_call(relay.reshape(call_4040.astype('uint16'), [5, 6, 6])), 0)
output = relay.Tuple([bop_4023,call_4040,var_4041,var_4042,call_4049,])
output2 = relay.Tuple([bop_4026,call_4043,var_4041,var_4042,call_4050,])
func_4058 = relay.Function([var_4041,var_4042,], output)
mod['func_4058'] = func_4058
mod = relay.transform.InferType()(mod)
var_4059 = relay.var("var_4059", dtype = "float32", shape = (1152,))#candidate|4059|(1152,)|var|float32
var_4060 = relay.var("var_4060", dtype = "uint16", shape = (180,))#candidate|4060|(180,)|var|uint16
output = func_4058(var_4059,var_4060,)
func_4061 = relay.Function([var_4059,var_4060,], output)
mutated_mod['func_4061'] = func_4061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_4069 = relay.TupleGetItem(func_2168_call(), 0)
call_4070 = relay.TupleGetItem(func_2169_call(), 0)
output = relay.Tuple([call_4069,])
output2 = relay.Tuple([call_4070,])
func_4071 = relay.Function([], output)
mod['func_4071'] = func_4071
mod = relay.transform.InferType()(mod)
output = func_4071()
func_4072 = relay.Function([], output)
mutated_mod['func_4072'] = func_4072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_4136 = relay.TupleGetItem(func_2131_call(), 0)
call_4137 = relay.TupleGetItem(func_2132_call(), 0)
func_3867_call = mod.get_global_var('func_3867')
func_3868_call = mutated_mod.get_global_var('func_3868')
call_4155 = relay.TupleGetItem(func_3867_call(), 0)
call_4156 = relay.TupleGetItem(func_3868_call(), 0)
output = relay.Tuple([call_4136,call_4155,])
output2 = relay.Tuple([call_4137,call_4156,])
func_4169 = relay.Function([], output)
mod['func_4169'] = func_4169
mod = relay.transform.InferType()(mod)
output = func_4169()
func_4170 = relay.Function([], output)
mutated_mod['func_4170'] = func_4170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3867_call = mod.get_global_var('func_3867')
func_3868_call = mutated_mod.get_global_var('func_3868')
call_4182 = relay.TupleGetItem(func_3867_call(), 0)
call_4183 = relay.TupleGetItem(func_3868_call(), 0)
output = relay.Tuple([call_4182,])
output2 = relay.Tuple([call_4183,])
func_4186 = relay.Function([], output)
mod['func_4186'] = func_4186
mod = relay.transform.InferType()(mod)
mutated_mod['func_4186'] = func_4186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4186_call = mutated_mod.get_global_var('func_4186')
call_4187 = func_4186_call()
output = call_4187
func_4188 = relay.Function([], output)
mutated_mod['func_4188'] = func_4188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_4228 = relay.TupleGetItem(func_2562_call(), 3)
call_4229 = relay.TupleGetItem(func_2563_call(), 3)
var_4235 = relay.var("var_4235", dtype = "uint16", shape = (180,))#candidate|4235|(180,)|var|uint16
bop_4236 = relay.multiply(call_4228.astype('uint8'), relay.reshape(var_4235.astype('uint8'), relay.shape_of(call_4228))) # shape=(180,)
bop_4239 = relay.multiply(call_4229.astype('uint8'), relay.reshape(var_4235.astype('uint8'), relay.shape_of(call_4229))) # shape=(180,)
func_4058_call = mod.get_global_var('func_4058')
func_4061_call = mutated_mod.get_global_var('func_4061')
const_4242 = relay.const([-4.173485,0.545591,-6.211584,6.875387,-0.218756,4.784434,0.620600,3.079634,-8.385077,-0.923488,-6.636242,-1.194805,-0.536576,4.166160,2.699003,1.106757,-6.212906,-1.969624,2.800670,4.297952,7.201049,-8.175190,-5.489616,6.534209,0.740139,5.681120,-2.679897,2.304007,-2.131459,7.155777,-2.782366,2.388933,8.012032,9.469922,5.763777,-5.521390,5.796666,5.166308,-3.997571,-1.572036,-0.808903,-5.158406,0.556946,-0.498335,-1.474962,3.720545,-9.008722,2.756232,-6.259902,-7.691893,0.897812,-8.212365,6.736490,-5.813439,-7.492679,0.561544,-5.290988,-0.943793,-5.790955,6.882574,-0.281800,3.127658,4.526411,-9.722456,0.592271,3.651445,3.809937,7.722503,9.869529,-1.866303,-2.298656,-0.013767,0.329908,-9.088075,5.684289,-6.334060,-3.877926,0.947848,-0.108239,5.040708,-8.065969,-2.031821,-0.322861,2.814184,4.229835,-6.477274,4.143662,-1.999241,1.704740,-8.313936,-4.968823,-6.400496,-7.704865,-6.110498,9.943722,-2.848069,-0.111318,0.118860,-0.594952,-9.677867,-6.657881,0.823827,-2.964166,5.166216,-9.154821,-1.343323,-4.806948,9.860521,-7.059922,-7.971724,1.761620,-6.091901,8.052061,6.930344,-1.907619,-1.036971,-2.914055,-2.354614,8.877541,-2.458259,-4.767510,1.586645,9.610829,5.478763,-7.126934,3.874473,0.015556,-1.058078,8.428321,-0.176742,3.876489,-3.335562,5.619942,-7.459411,-8.586152,-9.464953,-3.743326,-5.532567,9.616614,9.279528,4.601411,1.427811,-0.200890,5.947033,9.587445,8.368117,-5.768131,-3.312905,9.962066,7.648849,4.926192,-6.918368,5.783119,0.410117,-9.412067,-5.687054,9.201027,-4.869734,6.676524,2.316650,-8.246040,-2.262718,5.610261,-2.047718,2.977643,-4.029270,4.719398,-8.137323,0.165716,0.958403,5.764655,5.159138,-1.687768,-3.190273,-1.601920,-1.707024,4.033034,7.505771,-4.198203,3.162284,4.952953,-0.064453,-4.253490,4.651533,5.069834,2.239758,4.283854,0.377055,7.284267,5.333150,-7.279457,-4.329517,-2.924597,-1.991627,4.244046,9.992536,9.273414,8.895128,-6.436779,-5.279666,-3.594586,-1.797349,-9.201697,6.601292,-5.474224,8.700640,-6.039645,-4.399336,-7.534029,0.283617,-7.617118,-3.856640,0.633558,6.325648,6.002415,8.139767,6.133623,8.320766,6.283993,7.700604,9.733608,-4.286904,-8.738646,0.076858,7.782612,-3.138791,8.953673,-1.564853,0.377770,-3.924467,1.380576,-5.244692,-8.567772,-4.864903,-2.594802,2.499130,0.967043,1.782283,-7.137074,-8.783561,-1.207335,5.189138,7.030064,-0.358086,6.690746,1.318528,-3.935932,0.989059,9.421252,-9.183854,-6.412017,-2.838996,-8.781979,6.941261,-2.142838,-8.225798,0.350418,-8.654103,7.451299,2.519318,7.193877,9.970539,-7.607670,-8.561365,1.501771,5.120979,-9.288529,5.869907,7.216845,8.465325,-2.279475,-3.630814,8.153126,-2.744401,7.720036,3.123692,5.433580,-1.476474,-5.739996,9.818678,-9.301766,4.557249,-1.261148,8.463552,9.264564,1.480716,-9.276572,6.646638,-4.649318,0.719955,7.446785,1.076576,5.180012,-9.912291,-2.302832,8.892599,-8.401524,-2.397147,1.619437,2.047854,-5.727405,-0.565806,-1.944733,1.849297,-8.298485,4.734291,3.877554,-1.887651,-3.720245,-8.365303,-2.902475,4.688377,-9.507141,-1.587779,9.883577,1.428525,-7.055323,8.714342,8.818772,-0.522114,5.091063,-9.129159,-7.347227,3.128157,7.523439,2.955760,-2.322567,9.059032,-1.452782,-9.664731,1.307753,-3.140726,-2.649325,-3.029804,-5.198875,8.333576,-3.589045,-0.449161,-6.428309,-8.379921,-5.285705,3.251098,-9.496517,6.080091,-0.578711,5.278036,5.186065,-6.189786,4.851083,-7.037728,6.247394,6.520670,0.190267,-4.858641,3.775251,5.742035,-8.012171,-8.110548,0.179609,-7.327243,-5.328971,4.285123,4.318825,9.503253,5.589159,-7.925724,4.768151,-9.204436,3.864599,-4.239228,2.471037,-4.014167,-7.818752,6.800265,0.702082,-9.652543,7.505774,2.696001,3.740255,8.559273,-2.858387,6.572352,9.385973,-1.623570,-8.596451,0.333130,9.479483,3.514335,4.607622,1.475235,-4.039649,-8.348429,-1.304499,-4.628151,-3.721128,-2.007428,0.121340,-1.980244,9.756066,-6.785106,0.901163,-9.286638,1.101510,-2.425172,-1.217100,5.755331,4.154518,-2.131277,-0.143531,6.311936,-5.822860,8.935452,1.384710,-1.587681,2.295064,-2.956829,-0.805736,8.642215,9.397592,-8.836867,0.732391,-7.514919,4.387620,-0.442224,-4.905265,-1.110250,0.706977,-2.983880,3.392404,-4.126518,0.805282,0.687573,3.482636,-9.283829,5.536809,-2.133623,-9.588689,6.182725,0.533158,3.665950,-9.184610,-7.579651,-6.314432,-9.265349,9.186257,-9.930801,-4.092370,-1.551383,-5.455832,-2.374619,-2.023507,-4.852451,2.126032,-3.789204,-9.091242,-7.430314,-1.654667,-5.570053,-0.140512,-3.997151,8.368542,-2.237530,7.231329,2.154200,5.894892,7.119600,-6.198800,8.733237,2.858768,-0.270732,0.310789,-0.333263,4.410906,-3.901947,-9.901864,5.220468,3.629286,9.109497,2.956834,-6.359630,-3.038882,-9.753710,-0.389779,-6.843815,2.646389,2.647808,-7.559049,-6.105430,-0.866094,6.221344,-3.854150,1.630902,-7.551061,-7.054909,9.279610,7.186869,-9.037591,6.547532,2.403662,-0.394004,-1.745544,3.024984,-7.808351,2.131218,3.032276,4.041139,4.130940,5.314867,9.649403,1.981080,2.114827,-0.463883,-5.176820,-2.814830,8.716684,4.422619,-1.554608,-2.157135,-8.487519,4.601682,-9.064702,9.402960,0.891115,-5.887785,-8.690945,-5.752103,-6.303668,8.609380,-9.701870,-7.136231,0.281732,8.924644,-1.934334,-5.235146,5.587325,-7.390630,-5.610716,-2.805973,3.795723,-4.552480,-8.103080,0.152080,3.241610,-2.983250,-8.435121,3.863247,-5.333764,0.565922,7.622161,7.025664,5.030649,-8.450212,-2.372804,-7.944762,2.515853,2.128305,0.348623,-0.284569,-5.784602,-2.646762,9.290817,-5.040024,-9.653751,2.081406,3.509340,4.636162,-6.625482,-6.892820,-8.700714,-0.351079,4.169720,8.599959,-3.316448,6.504249,-8.703850,9.926804,6.035833,1.045684,2.830612,2.422677,-8.074856,-7.726275,5.791200,3.224053,5.354885,6.459679,9.845420,6.088377,4.099446,-5.760881,-7.909670,2.489490,9.134748,8.514349,2.009829,5.883316,0.223199,7.980161,-7.388451,-2.255369,-4.228980,-7.297345,1.763905,-1.470294,-4.599568,-6.313122,-5.232777,5.318451,7.088537,2.572843,8.544189,-9.893230,-5.138781,5.064980,-2.379982,-6.889239,-8.750780,-0.701179,-2.150613,-8.991152,-2.427258,9.657246,-4.670739,-4.809620,2.003888,5.534340,3.526828,-5.129959,4.212089,-1.625083,0.923746,-4.996269,-5.438165,4.517167,9.376082,0.983147,4.419471,0.080673,0.547866,5.998025,7.193103,-2.703966,-5.758234,-1.549581,-1.381195,6.002564,4.963099,7.705995,-3.745383,-3.609939,-5.848618,2.923360,-0.735386,-1.845742,3.444021,-6.471973,-6.754967,0.562068,8.577754,-1.087061,-0.025024,-2.028924,3.761725,0.311830,-0.113380,-4.290951,-7.112245,-5.932667,-7.937718,-9.061703,-8.390851,-1.573745,7.229592,2.228696,2.835355,5.930041,8.810724,0.581410,5.263867,1.715245,-3.525428,3.274175,8.720125,3.722891,-3.535886,4.811316,-8.997417,4.939562,8.650392,3.526614,-8.891356,0.121704,-5.430718,-4.974463,5.914598,3.350925,9.953516,-2.159311,8.932050,-0.798893,-5.211749,-5.506878,6.780892,-2.482166,7.160114,6.443680,-6.829119,3.466970,1.593313,7.534790,1.824445,-4.630661,2.636360,-6.552798,-1.960022,-1.138612,-8.129491,-7.369118,-0.494733,7.422098,-8.298604,8.889844,1.587912,6.705456,-2.241205,8.020157,6.116526,5.509550,5.936057,6.729047,-9.750720,-2.646457,0.028466,8.224323,4.194092,5.437587,1.629380,6.733550,2.164352,-6.456693,0.959917,-7.612484,1.016343,0.439709,5.025763,2.046868,-7.993205,-4.214972,-0.401531,1.037946,-9.021964,7.040514,4.824297,-3.036276,4.996100,-3.795483,1.882021,5.094432,-5.635970,1.721788,-6.778184,-1.810427,-1.036095,-7.866921,-8.825124,-8.310896,-7.288197,-3.259328,-0.851787,-1.611253,0.259916,-7.660854,1.794007,-5.951443,-9.005213,6.740515,-8.140956,5.115456,8.311535,1.095696,7.181492,-7.649134,4.126339,2.743665,-9.910930,8.286876,2.743963,-0.122961,4.319811,-1.980395,-4.498568,-2.989672,8.930157,3.124997,6.825513,-2.662617,-4.134860,-6.415541,-5.866692,-0.819315,-8.180186,-7.221123,2.082134,-0.432563,1.627106,9.412976,1.562872,-8.451929,7.443992,0.301803,-5.957582,-1.457774,-2.987037,-1.241191,-5.080495,4.648542,-9.858756,-3.367109,-2.728032,2.335070,-9.117768,8.483683,-7.741277,-4.077692,2.045877,5.584368,-2.026533,9.148911,-3.156577,0.851747,-6.142600,5.577048,-9.777696,-5.140258,1.635004,1.912398,-4.984319,4.171853,-6.903607,9.938588,1.227501,-1.996015,-3.291918,-2.663026,9.602389,6.550447,5.258527,5.325743,9.002415,-8.668644,5.767136,-2.364882,4.454405,-1.715079,3.384283,9.191349,-1.183052,-4.106622,0.693073,-3.291047,-9.265485,-5.088940,-3.881713,-1.366212,-8.181883,-4.580647,-6.836084,4.584473,-9.306044,5.473118,7.186564,-0.762194,-2.351430,-6.748743,-8.963379,8.583005,2.063198,-2.085124,5.620481,0.560650,5.863944,8.491391,-0.741460,4.544228,-9.023129,-3.566576,-4.092178,-4.177903,-8.114721,-2.271674,1.703114,1.257950,-7.259118,-9.215596,-5.081320,6.160995,-5.739193,3.687487,3.396721,0.873626,-8.185477,-3.987050,9.766226,3.715076,8.549114,-5.764261,0.005607,8.493001,0.468682,5.908651,8.702862,6.213440,0.047189,-4.725662,-2.129261,1.780157,-8.956541,8.067515,-1.314581,9.656094,-5.624752,-7.122559,7.025195,3.287204,3.868393,4.091069,6.669910,-9.580707,9.215002,-7.506143,4.912998,-8.154373,7.903433,9.095192,9.576143,7.889972,-8.096436,8.579046,-9.487134,-2.431045,-9.919053,-3.866042,-1.688409,-5.199071,-1.713979,4.728592,-8.439727,9.719988,5.332988,5.393970,4.796085,9.184495,-5.780416,2.187563,6.402164,6.896639,8.477091,-6.578980,-2.737033,-9.633092,5.686149,-1.552621,6.901905,5.488516,-5.372375,2.056346,3.328627,4.012425,-3.420510,-8.153544,-1.995416,0.172836,-0.861084,-1.198026,-5.879696,3.259679,-6.921585,-2.182574,7.139871,7.823096,-8.139124,8.097662,7.629873,-0.707087,8.926301,9.262479,-4.001270,-9.964788,-0.995263,7.010451,3.703682,-5.504512,7.006966,8.684394,-9.807191,-8.015789,-8.841208,8.772615,8.302603,5.092001,-0.453907,-5.229344,1.645294,8.429175,1.179544,-4.910053,8.674546,6.190667,1.010943,1.187874,7.230484,0.916274,7.626852,4.317288,-7.705770,-0.626776,9.162054,3.820105,8.186311,5.258499,5.767901,3.203589,-5.383535,2.531709,9.101907,-8.832727,6.665972,-5.778307,-6.408535,6.014112,-9.437983,6.233879,-0.489695,-6.389363,-1.055143,6.895589,-7.676140,-5.720618,8.393182,-1.535176,2.113700,4.889329,-3.910383,1.213856,3.866460,1.148527,-3.270479,1.241264,9.631703,-8.548045,3.939041,-0.942021,-1.016144,1.867734,-7.790049,8.660085,-5.508017,-5.093427,-4.823013,2.465194,-2.710861,-6.000929,3.945047,-9.054188,5.070027,-0.643371,-4.840675,-2.865650,-1.660606,-1.116421,-6.797506,-8.167989,-8.097900,2.306038,-8.763252,-6.670575,-8.313408,-4.997355,-6.532432,-7.884838,0.657980,5.693409,9.963524,7.357211,4.496840,3.332315,8.600649,-9.243041,-1.802490,-3.453839,-5.829009,-5.905716,8.476362,-0.621896,7.432805,-1.904063,-1.662073,-8.611153,0.925184,2.764804,5.962573,-5.228078,-0.532438,-9.491748,7.810508,8.769073,2.487007,-8.727220,-7.063565,-4.723117,3.993345,8.223298,-8.302049,-5.604230,7.380805,-9.943930,-8.307737,0.149916,3.546290,4.420032,-8.946719,-7.253634,-8.737693,9.224932,-8.675675,-9.874745,-2.795866,1.860001,3.940961,-2.120417,2.197179,5.568917,-3.438849,-3.941095,-5.177515,-9.218161,-4.863847,-5.302986,9.364131,-1.165804,-2.096383,9.309162,-7.099556,9.175674,-6.186769,-0.251066,3.541253,0.394468,-5.084202,8.772288,-6.416392,7.394099], dtype = "float32")#candidate|4242|(1152,)|const|float32
call_4241 = relay.TupleGetItem(func_4058_call(relay.reshape(const_4242.astype('float32'), [1152,]), relay.reshape(bop_4236.astype('uint16'), [180,]), ), 2)
call_4243 = relay.TupleGetItem(func_4061_call(relay.reshape(const_4242.astype('float32'), [1152,]), relay.reshape(bop_4236.astype('uint16'), [180,]), ), 2)
output = relay.Tuple([bop_4236,call_4241,const_4242,])
output2 = relay.Tuple([bop_4239,call_4243,const_4242,])
func_4254 = relay.Function([var_4235,], output)
mod['func_4254'] = func_4254
mod = relay.transform.InferType()(mod)
mutated_mod['func_4254'] = func_4254
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4255 = relay.var("var_4255", dtype = "uint16", shape = (180,))#candidate|4255|(180,)|var|uint16
func_4254_call = mutated_mod.get_global_var('func_4254')
call_4256 = func_4254_call(var_4255)
output = call_4256
func_4257 = relay.Function([var_4255], output)
mutated_mod['func_4257'] = func_4257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3526_call = mod.get_global_var('func_3526')
func_3527_call = mutated_mod.get_global_var('func_3527')
call_4284 = relay.TupleGetItem(func_3526_call(), 4)
call_4285 = relay.TupleGetItem(func_3527_call(), 4)
func_2883_call = mod.get_global_var('func_2883')
func_2884_call = mutated_mod.get_global_var('func_2884')
call_4288 = relay.TupleGetItem(func_2883_call(), 0)
call_4289 = relay.TupleGetItem(func_2884_call(), 0)
output = relay.Tuple([call_4284,call_4288,])
output2 = relay.Tuple([call_4285,call_4289,])
func_4291 = relay.Function([], output)
mod['func_4291'] = func_4291
mod = relay.transform.InferType()(mod)
mutated_mod['func_4291'] = func_4291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4291_call = mutated_mod.get_global_var('func_4291')
call_4292 = func_4291_call()
output = call_4292
func_4293 = relay.Function([], output)
mutated_mod['func_4293'] = func_4293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4071_call = mod.get_global_var('func_4071')
func_4072_call = mutated_mod.get_global_var('func_4072')
call_4339 = relay.TupleGetItem(func_4071_call(), 0)
call_4340 = relay.TupleGetItem(func_4072_call(), 0)
func_3595_call = mod.get_global_var('func_3595')
func_3599_call = mutated_mod.get_global_var('func_3599')
var_4345 = relay.var("var_4345", dtype = "float64", shape = (845,))#candidate|4345|(845,)|var|float64
const_4346 = relay.const([1,2,1,-8,-5,-3,10,5,-3,-1,4,-4,1,10,-9,7,-6,4,10,-6,-4,-7,-1,6,3,-4,1,-9,-10,-8,-8,1,-3,1,-8,-10,8,-7,-2,-2,-10,2,-6,8,10,7,10,-1,-4,8,-9,-6,-8,7,8,4,8,3,-9,-2,-6,8,-10,1,-1,-7,9,-9,-10,8,-6,10,-10,-9,-4,1,-3,-6,-8,-6,9,-1,-9,-7,7,-9,-8,8,-9,-9,2,-5,-9,-6,9,5,-5,6,9,5,1,-10,10,-6,-6,4,-5,3,-9,10,-10,7,3,1,9,7,-7,-6,4,-8,9,8,-2,-7,-9,2,-1,-5,2,-6,2,-8,8,-8,10,-3,-1,-2,-4,-7,-5,2,-7,2,-5,-10,-2,7,-4,4,-2,-2,10,5,4,-6,-10,5,-7,7,-5,-8,5,9,-10,-3,2,3,-1,7,-2,-4,-1,-2,-8,-10,-5,-2,-4,10], dtype = "uint16")#candidate|4346|(180,)|const|uint16
call_4344 = relay.TupleGetItem(func_3595_call(relay.reshape(var_4345.astype('float64'), [13, 5, 13]), relay.reshape(const_4346.astype('uint16'), [180,]), ), 0)
call_4347 = relay.TupleGetItem(func_3599_call(relay.reshape(var_4345.astype('float64'), [13, 5, 13]), relay.reshape(const_4346.astype('uint16'), [180,]), ), 0)
func_3595_call = mod.get_global_var('func_3595')
func_3599_call = mutated_mod.get_global_var('func_3599')
call_4348 = relay.TupleGetItem(func_3595_call(relay.reshape(call_4344.astype('float64'), [13, 5, 13]), relay.reshape(const_4346.astype('uint16'), [180,]), ), 3)
call_4349 = relay.TupleGetItem(func_3599_call(relay.reshape(call_4344.astype('float64'), [13, 5, 13]), relay.reshape(const_4346.astype('uint16'), [180,]), ), 3)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_4350 = relay.TupleGetItem(func_2131_call(), 0)
call_4351 = relay.TupleGetItem(func_2132_call(), 0)
output = relay.Tuple([call_4339,call_4344,var_4345,const_4346,call_4348,call_4350,])
output2 = relay.Tuple([call_4340,call_4347,var_4345,const_4346,call_4349,call_4351,])
func_4359 = relay.Function([var_4345,], output)
mod['func_4359'] = func_4359
mod = relay.transform.InferType()(mod)
var_4360 = relay.var("var_4360", dtype = "float64", shape = (845,))#candidate|4360|(845,)|var|float64
output = func_4359(var_4360)
func_4361 = relay.Function([var_4360], output)
mutated_mod['func_4361'] = func_4361
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4492 = relay.var("var_4492", dtype = "bool", shape = (5, 14, 7))#candidate|4492|(5, 14, 7)|var|bool
var_4493 = relay.var("var_4493", dtype = "bool", shape = (5, 14, 7))#candidate|4493|(5, 14, 7)|var|bool
bop_4494 = relay.logical_or(var_4492.astype('bool'), relay.reshape(var_4493.astype('bool'), relay.shape_of(var_4492))) # shape=(5, 14, 7)
func_3669_call = mod.get_global_var('func_3669')
func_3671_call = mutated_mod.get_global_var('func_3671')
call_4509 = relay.TupleGetItem(func_3669_call(), 1)
call_4510 = relay.TupleGetItem(func_3671_call(), 1)
func_3757_call = mod.get_global_var('func_3757')
func_3761_call = mutated_mod.get_global_var('func_3761')
var_4521 = relay.var("var_4521", dtype = "int32", shape = ())#candidate|4521|()|var|int32
const_4522 = relay.const([-1,5,3,3,-3,-5,2,2,7,3,7,3,-7,-6,-5,6,-9,1,-2,5,-3,10,4,-5,10,-6,5,-1,-10,-1,-6,-2,7,1,2,-7,-8,10,-9,-5,-2,7,8,2,-5,-4,-9,9,2,7,6,8,-3,8,-5,2,-1,7,-7,7,3,4,-10,9,-3,-5,-2,-4,3,-6,4,6,-7,7,3,7,-7,-1,5,8,-8,-8,-8,-7,6,-9,-1,8,-7,1,10,9,10,4,-10,5,9,-10,8,10,-1,6,4,-10,-8,-5,1,-6,2,8,6,1,1,-4,9,2,-5,-9,-2,-1,10,-1,-8,3,8,-5,9,4,5,6,4,-3,-8,-7,3,-3,2,5,-2,3,2,-6,3,-8,8,4,5,8,-2,-6,-2,10,-4,7,5,-5,9,-9,-3,-1,-2,2,2,3,-6,-1,-1,-4,7,-10,-3,-1,-8,3,9,2,-10,-1,6,-8,-6,-1,-9,-1,-8,1,5,4,-4,5,-2,7,1,6,-5,-8,-3,-7,5,3,6,-5,-7,4,-5,-7,6,-10,-3,4,1,8,-2,8,-10,5,4,6,-8,-5,1,-3,-7,4,7,9,-10,4,3,-1,3,-10,5,-10,-8,9,8,-6,5,6,-8,2,5,9,-7,2,8,7,-10,8,2,9,1,7,-5,-8,10,-10,3,3,-2,10,-7,-3,5,-4,1,9,9,8,8,9,-5,3,8,7,-10,-8,-5,-1,4,-7,1,7,-1,5,10,-7,3,-2,-5,1,-8,-2,1,5,-1,10,-10,1,1,-1,10,-3,-8,-3,6,8,-4,8,4,-3,-8,4,-10,-9,10,2,-8,2,2,8,-1,3,-9,-1,6,7,-6,10,-7,-1,-9,-7,-9,-2,6,2,-8,-3,8,1,9,-10,10,-5,10,-6,-8,-5,-5,10,7,-9,9,-6,-9,4,7,-4,-3,6,2,10,6,-9,-2,-10,-2,-8,4,-1,10,-10,-7,-6,1,4,1,-5,1,7,2,-6,8,-7,-7,5,4,-6,10,-1,-3,6,3,2,5,9,7,-4,-7,-9,-1,-6,2,6,-4,-4,-6,-1,-2,-2,2,-6,5,4,-5,8,1,-3,-6,6,-7,-8,-1,-9,2,1,1,3,-9,9,1,-10,-3,-5,1,2,-2,-1,9,-5,1,7,3,-9,-8,-4,10,-1,-8,-4,8,7,6,10,-5,-8,-10,10,8,6,10,5,6,4,2,3,4,9,-5,7,5,8,-4,-1,-8,6,-8,9,-7,-8,-1,-1,10,-6,1,4,-9,-3,1,-3,2,-8,-10,-4,1,8,-4,6,-8,-6,-4,-5,5,5,-4,6,10,6,-2,-9,-4,-5,-5,-2,-3,-2,-1,9,-6,3,-7,-8,4,6,-6,-10,-1,1,-6,-7,-1,6,-5,-9,1,3,-2,4,-4,-3,5,-3,10,10,-6,5,-7,9,-5,-5,10,-6,-8,10,1,4,-7,-2,-2,-3,9,-4,-8,-8,-1,3,2,6,2,-4,9,10,-9,-5,5,7,-7,-10,-6,-9,-3,2,6,5,-4,-2,9,9,4,-8,1,5,-8,2,-5,-3,-7,-4,-3,-2,10,-9,8,6,3,3,1,1,-2,5,8,-4,3,10,8,4,-6,6,3,5,10,-10,-5,10,6,3,-3,10,6,3,-2,2,2,-1,4,8,6,-4,-9,-10,-10,-10,1,-1,10,3,-3,-1,4,7,-9,-3,5,8,2,10,1,6,-9,-1,3,10,-8,10,-2,4,-5,8,4,3,-6,-1,10,10,-6,-8,-4,4,1,8,2,7,-8,-7,-3,-2,3,5,-3,-5,-6,8,5,-6,8,2,-5,-9,-3,9,7,4,-7,3,2,8,3,9,-8,4,10,-7,-4,10,-3,5,2,-9,-6,2,-2,-9,-6,1,-5,3,-1,-10,7,2,1,-9,7,-6,4,-5,8,-1,2,2,9,3,-6,-4,-5,2,-6,-10,10,-9,2,1,8,6,-6,-9,4,6,7,2,8,9,-4,10,3,-8,-3,-6,-3,-1,5,-5,-6,-8,2,-6,-3,-6,-3,10,-6,-2,-9,8,-5,2,-2,8,1,2,5,4,4,2,6,3,10,9,-4,-3,9,-8,6,9,-9,1,-3,-1,-4,-4,6,-4,-3,-10,-1,7,-10,-1,8,-6,-4,-2,-1,-4,9,-9,5,3,-8,4,-6,9,3,-4,3,9,-8,-2,5,6,-4,-9,10,-5,-7,-8,-2,-10,-9,8,-6,-7,8,-3,-5,-9,6,8,-1,2,3,-10,-7,2,7,-7,-6,9,-6,-9,3,-10,5,5,-2,-4,9,10,8,-3,1,-10,-8,3,1,-5,-7,3,4,9,-7,10,9,-3,3,4,7,3,4,7,7,10,-8,7,3,7,9,5,9,-6,3,8,-5,5,-8,-5,-6,-8,-9,8,9,1,5,7,-3,8,-5,6,-9,9,5,2,-8,8,5,9,-5,5,8,6,7,9,-2,3,-8,-3,-6,-4,7,-6,-2,-10,7,7,-7,9,8,-5,-5,-6,-1,-5,3,-5,-5,-3,-6,-2,-8,8,-3,-7,-5,3,-1,2,-7,-10,10,3,6,10,10,-7,-10,-2,-4,-6,-5,8,10,-9,8,-9,7,-2,9,7,6,8,8,1,-2,10,5,-3,-9,2,-4,-6,5,5,3,-5,-3,5,2,-3,2,-10,-3,-2,5,-10,6,-9,-7,7,6,7,3,-3,7,-1,-1,-5,-6,-7,-10,-2,-4,-9,7,10,-8,-5,8,-7,-5,-3,-1,-3,5,10,8,4,-2,2,9,-3,9,-7,7,2,-4,10,-3,-2,2,4,3,1,-2,-7,5,7,9,8,2,7,5,1,8,-6,7,-10,9,8,-2,-2,8,-10,-5,-2,-10,-3,6,-1,-9,-5,-9,9,-4,-9,5,-7,1,9,-8,3,9,1,1,-10,-2,-9,9,9,8,-4,-1,5,8,8,-6,-4,-8,-10,10,1,6,3,9,-3,-1,-9,9,4,7,-5,-4,8,5,-1,2,7,2,-5,3,8,-6,6,-3,3,4,-5,-5,2,-2,5,5,-2,-3,9,-5,-9,6,-6,-10,10,-5,4,-7,1,9,5,-9,4,4,-7,-10,1,4,6,-6,-7,9,-4,6,-8,-3,-1,-10,6,8,-6,-10,6,-6,-9,9,5,5,-6,5,10,-9,-10,-5,4,10,4,6,-5,2,-5,9,-1,-9,9,-1,2,9,-8,2,8,1,-3,3,1,3,-8,-6,-9,4,-1,-7,6,8,-10,7,2,3,-6,3,-2,3,-1,7,-6,-9,9,-3,-4,10,-3,4,-4,1,3,-7,-2,-5,1,-2,4,-7,9,-7,-3,7,-3,-9,9,-8,6,7,8,-1,-3,-8,-6,7,5,6,-10,-1,-5,-1,2,7,7,-8,-4,-3,-3,4,-6,-5,-7,-6,-6,-10,-1,3,2,-3,-4,3,-7,-6,7,-10,-3,1,-5,-6,8,-2,-9,-10,5,-8,-4,8,7,-2,6,-7,-8,-6,9,-6,8,-4,2,-7,-9,9,-6,-5,-1,-9,-10,5,-7,10,2,1,-3,10,10,4,2,1,10,-3,2,7,10,-9,-4,-3,3,8,-10,1,6,7,1,-8,-5,-2,-4,-8,-3,-1,4,-3,9,-4,2,7,5,5,-6,-4,5,8,7,2,-3,-6,9,5,-3,-5,8,-2,-9,-8,-2,-4,8,-4,5,2,-1,4,-8,-7,2,5,-3,-3,-5,-7,-3,4,2,4,-6,-7,7,-8,-2,7,7,6,-10,-4,9,-4,2,-4,5,-2,-6,-9,-10,-1,2,-6,1,-10,-10,8,6,2,9,2,3,5,1,-6,1,-3,5,-5,-3,9,-1,-3,-8,-7,-10,-1,1,6,-9,2,10,-6,-5,3,-8,-1,1,8,-10,8,-3,5,-4,5,3,-5,3,8,-4,5,-5,-9,-2,-6,1,4,-3,-8,-2,-10,10,-10,9,-10,10,5,4,2,2,-10,-1,6,7,-1,-7,-6,10,-2,3,-4,-7,-8,2,9,-9,-6,5,-6,-8,-3,-10,3,-4,-1,-7,10,3,-7,2,-10,6,1,9,-6,-4,1,-8,6,-9,9,-3,2,-10,2,8,1,7,5,-9,1,10,9,-8,7,3,5,-6,-3,-9,-6,-8,-1,1,9,7,-3,-3,4,-9,-9,9,-2,3,1,2,-9,6,-5,5,5,5,-2,2,10,-9,8,6,-2,5,3,3,-8,-1,4,-9,2,10,-2,10,-6,4,-6,3,-9,3,6,3,5,-6,-4,9,-9,-1,-3,-7,-9,-4,1,-5,6,4,4,-5,-3,-7,8,-2,6,1,4,2,-1,10,-4,4,-1,-1,6,-3,8,6,5,-4,1,2,-3,1,-1,-6,4,-6,-10,1,4,7,-3,10,10,8,-9,-9,5,8,10,10,6,10,-4,4,-6,-9,-3,-6,-3,8,-7,6,-8,-7,-8,2,-4,4,5,5,10,-8,-3,9,3,9,6,-3,10,5,-8,6,1,-1,7,-8,9,1,2,-7,-7,6,-2,10,-8,1,-3,-1,6,-3,-9,-9,6,-10,10,-7,6,10,10,-1,4,8,9,-4,-1,-8,-7,-9,-9,-5,-10,5,6,5,5,6,-10,-9,-4,-5,-1,7,2,-2,7,-1,10,3,1,-1,6,8,-4,4,-1,2,4,9,-5,8,-8,9,4,5,-9,-4,6,2,8,-7,-7,-10,-8,6,9,5,4,9,-5,-5,-1,-3,10,6,-1,8,1,8,6,5,9,-5,6,-1,6,-9,-7,-5,-8,-7,-3,-7,-5,-6,-1,6,-4,5,3,-3,3,8,-4,9,4,-1,2,-1,-4,-8,9,9,5,3,9,10,10,6,-3,-6,-10,3,-4,1,-3,-7,2,-6,-7,8,-7,-1,-6,-8,1,-5,-10,5,5,4,-6,10,4,-9,-7,10,-5,8,8,-10,10,2,-6,-6,6,10,-8,9,8,-6,5,6,6,1,2,7,-1,-3,-7,-9,-6,2,-9,7,-1,10,-8,-5,-2,2,-10,-7,-7,7,9,6,2,1,-1,9,-3,9,7,10,2,7,-1,10,-7,4,2,-1,-10,-8,-5,4,-7,-3,-8,-8,-5,2,-9,7,-9,2,-3,-8,9,5,-4,-4,-3,-9,-10,-3,4,-4,-8,-9,-4,-10,5,-9,5,-8,4,-2,-1,-9,-10,9,-8,6,-5,-2,-7,-5,10,9,-9,-4,1,1,-9,-4,-3,-4,5,6,5,9,10,-6,-2,-6,4,-6,-8,-10,7,9,-6,-2,10,-2,-8,1,-7,-10,4,9,-8,6,2,-4,-1,-1,-5,-9,-3,-4,-2,-10,-1,-5,6,6,9,-9,-9,1,9,6,-5,1,-6,8,9,4,-8,-9,-2,-8,7,5,-4,6,8,-7,9,-2,2,-10,8,3,4,8,-6,-9,6,1,-2,-1,-10,-5,6,-1,-7,-9,8,1,-3,8,-7,-2,-4,-3,1,7,4,-8,1,-7,2,-3,10,-2,5,2,-10,-5,9,-9,3,10,1,-6,-9,1,10,4,10,-3,-8,6,-9,-2,-10,9,-8,9,-8,2,-9,-1,-8,1,10,4,-8,6,3,8,-9,-5,5,-8,10,-10,-2,-1,5,10,-7,3,-5,5,-7,9,9,4,-9,-8,-10,-1,-1,-5,-8,2,-9,3,6,-2,-2,-8,9,6,4,-9,2,1,6,-10,10,10,-8,5,-10,6,2,-2,8,8,-1,10,-9,-7,-6,-9,-8,8,-1,-10,4,2], dtype = "int32")#candidate|4522|(2184,)|const|int32
call_4520 = relay.TupleGetItem(func_3757_call(relay.reshape(var_4521.astype('int32'), []), relay.reshape(const_4522.astype('int32'), [13, 14, 12]), relay.reshape(call_4509.astype('uint16'), [180,]), ), 3)
call_4523 = relay.TupleGetItem(func_3761_call(relay.reshape(var_4521.astype('int32'), []), relay.reshape(const_4522.astype('int32'), [13, 14, 12]), relay.reshape(call_4509.astype('uint16'), [180,]), ), 3)
func_4058_call = mod.get_global_var('func_4058')
func_4061_call = mutated_mod.get_global_var('func_4061')
const_4527 = relay.const([5.889597,-7.557084,-4.892579,-9.760654,-3.407058,9.961564,1.210077,5.394625,-4.106124,-7.117867,-1.890394,-4.835661,-3.524960,7.590032,-7.714258,4.621532,6.732541,7.172273,-3.735424,7.611301,-3.900595,-4.435310,2.126609,5.700473,-9.356485,9.176713,-3.249831,4.151549,-2.782700,-9.059447,0.466443,-1.702299,4.352996,5.048080,8.045599,-9.221824,8.439054,4.239056,4.075203,-6.933731,4.694545,-1.979639,1.108892,-5.057542,-0.759559,8.265527,6.852050,-2.013366,2.984613,-0.420329,-7.807791,-0.080490,5.985269,7.202037,-6.773984,-5.663124,9.029157,7.968916,-6.498787,-5.190816,-1.264040,6.321037,9.655865,-5.925128,7.313943,5.578238,8.055045,6.035300,9.155388,5.374529,-3.492472,6.481121,-1.805241,2.597191,2.207666,3.261458,7.374204,4.270218,-0.230409,1.253296,-7.803303,-7.629678,-3.961262,-6.267061,-3.567346,3.362377,9.803568,-8.865908,7.392721,-3.244979,7.110412,-3.277595,-0.548026,9.298421,0.214752,-7.948808,5.954045,2.693215,-0.572483,6.843494,-4.237639,-7.693622,-1.595493,9.987347,-6.161569,-6.297481,-0.718376,-5.281676,-4.175633,9.478263,-5.717518,8.102822,-4.288209,0.055059,-7.122721,0.193405,8.603785,-6.370050,-4.073537,7.742148,8.477637,-3.320520,-0.713155,7.902106,-8.980827,-7.700665,-1.574643,-7.391315,-6.786665,-9.541377,5.863874,3.627977,2.105058,-0.947049,-9.604607,-3.355375,7.745007,9.312577,8.083296,-3.892462,7.610545,-9.425215,-2.117714,0.914005,-3.651201,8.418815,7.673265,-9.761575,-6.825462,8.116276,-9.838292,-0.704832,-9.619068,0.828914,-1.002019,-6.521150,-9.210422,-3.972898,0.336660,1.010550,6.515972,0.656806,-1.005416,8.825855,-0.060317,4.185094,-7.487843,-6.796903,8.978433,-8.810504,7.442518,8.854808,2.395815,-7.806720,6.814285,-3.225781,-4.749460,-7.246494,2.393803,8.708082,-9.780082,-5.630281,5.034156,8.980704,-0.809781,-9.933643,-5.052801,5.431652,8.534820,0.515155,2.814655,1.107442,7.574965,-1.843903,1.910587,6.474474,-0.017792,-1.677465,-2.729847,-2.289737,7.256271,0.387283,0.519177,4.510165,-0.981110,2.855294,-1.898768,-1.372056,-1.399911,-6.331993,-8.090533,0.781873,3.809628,-6.737350,-3.822058,-7.488620,-1.985324,4.183114,-4.437284,-0.807500,4.067498,9.839954,2.836585,-1.842676,-3.840482,6.308500,-1.495845,-9.127884,2.011057,0.860324,0.495604,9.687655,4.688515,0.172042,-2.819454,8.778347,-2.829268,5.968877,-6.397046,6.798666,5.687801,6.892013,-4.032125,1.448509,0.686041,8.385817,4.503549,-1.991385,7.042866,-4.920565,2.800436,-2.964471,-0.420729,3.236543,7.865378,-6.424050,-1.382687,-4.760608,2.733292,-8.586879,-4.125446,1.096029,-2.300196,4.054122,-8.527132,5.289612,8.690340,9.387975,-9.148182,-2.904829,4.985236,-7.071039,-0.361576,-0.090690,-6.127629,-6.942457,-2.665026,-0.819736,9.104561,0.642881,-3.911682,-1.175265,-0.244672,4.301552,-0.058179,-6.355602,-5.219609,0.979410,1.537996,-9.381592,-9.404213,-2.972793,9.395644,-4.037121,-6.835789,-2.295638,-2.844522,-4.745225,-2.271065,1.447931,3.272704,-3.763736,-6.662839,2.968417,-2.663269,-3.294061,-0.399980,4.784567,0.710864,8.429559,0.318914,-5.609690,-3.292264,-7.779886,6.719178,2.966114,2.169542,-3.321217,-3.044464,6.329257,-2.261627,5.863223,2.347379,-8.964941,-2.585284,-1.878062,6.718818,-3.360556,-6.246677,-0.324012,-2.664959,-3.841548,9.129880,-0.025867,-0.391624,-8.878217,9.920715,-1.726906,4.210070,3.442500,-3.260611,5.558352,0.420900,4.214907,8.722360,3.546112,7.906031,7.635767,-8.514889,-1.030813,-3.567419,8.662412,4.039839,-1.362370,-0.051087,-2.580666,5.567670,-5.180982,3.257642,-7.749646,4.459861,7.268705,-0.436283,-5.181200,-2.164834,6.690906,9.595428,-8.429160,-3.860851,8.134524,-0.074844,7.032615,-4.060897,-2.285970,9.530854,-6.090026,-8.484878,-8.452124,-0.119460,-8.582918,5.559234,4.371833,-5.967816,5.387418,-4.164662,-2.882234,6.076058,7.050741,5.277565,1.307631,-6.768619,-8.146995,6.820212,5.858820,8.945393,-4.215608,-7.632508,9.127996,1.559508,0.809783,-5.123151,0.618766,-9.226104,8.704663,-1.857148,-6.254236,-3.848917,-1.547089,2.067903,1.391080,9.176993,-8.909138,-4.970665,-9.263462,-3.028382,5.342645,0.053509,-9.427735,8.035977,-9.381464,0.663101,9.216137,3.592979,5.421678,4.617922,2.893037,8.369779,-8.008851,8.336650,0.381206,7.406030,-1.760744,3.963451,-4.631660,-9.608652,0.283827,0.838399,2.540458,-6.753460,-9.530053,-2.961344,-5.894221,4.462483,8.666374,6.211804,-2.540179,4.075774,-1.580972,-4.166451,-3.470860,7.384683,-0.299585,-0.776182,9.449353,-2.130925,-7.884088,6.638790,-2.023614,-1.407369,6.757599,6.277039,-7.594190,0.509533,7.658729,0.363343,-7.412589,6.294301,4.837794,9.564197,-5.765759,-8.109326,-8.442675,4.063766,-9.830635,-5.630064,-9.046584,-6.431684,-3.769093,3.540118,5.895789,8.845203,6.861136,-2.148515,-4.880668,7.054194,6.665661,-0.217205,5.238875,1.865083,7.354633,5.244349,6.510481,-4.438504,9.170538,7.724742,-2.721843,9.559118,-8.065487,-8.042389,4.426519,1.383219,-1.473970,-3.320537,-4.897448,8.121293,9.095021,5.115822,-3.641109,-7.881284,9.430214,-3.838477,8.071945,5.784104,6.153939,-8.879589,1.221389,-7.832084,7.782786,7.440097,-4.381167,1.472784,7.486697,-4.405511,-9.845552,-4.374511,-1.232399,5.557088,-0.900658,0.012490,6.264048,-2.498664,-5.931781,-3.032055,6.628739,3.772787,-3.041255,3.919325,4.828171,-0.007894,-4.427414,6.863896,6.124192,-3.713362,9.622032,-4.315023,-9.672562,5.461165,1.922345,-4.534895,0.268947,-1.073754,5.578230,9.550260,1.618612,-9.662854,-7.993039,-1.541583,8.595921,0.949341,5.732046,1.924386,-2.341771,-6.051744,-5.390703,-6.108049,-4.207514,7.588202,-8.324154,-9.554607,-1.562032,-0.963963,-2.445525,1.216665,7.333823,-6.114270,-8.532767,-0.636638,-6.902977,-9.039093,-1.339998,-7.590546,0.831135,-4.948478,-7.403536,0.093446,2.552811,-7.693082,-9.268582,9.764029,-9.201504,-1.325629,5.780475,-3.256922,7.787295,-9.537778,9.827559,-9.203107,7.149593,5.022278,5.936552,-4.792243,-0.512679,-4.437192,-8.653727,-3.301868,4.798420,0.125134,-8.086241,-3.914466,-9.339092,9.367399,1.541386,-3.067208,-0.258039,1.342900,-3.543727,-4.122993,-1.319886,-6.553371,6.715894,6.659177,2.596331,5.117356,-6.002004,-6.695700,1.917486,8.795634,8.384847,8.677565,8.809182,-8.798705,-5.089763,-8.274412,5.746677,-5.006396,8.490385,-0.049901,-3.891763,-5.504710,5.384127,-2.519981,-3.742276,-9.200041,7.718533,5.983619,-3.598320,3.973364,7.176869,9.577121,-4.334574,9.701804,6.646935,-4.000372,6.968171,1.737363,2.991770,4.421524,6.091082,-8.442028,0.555473,4.932694,3.986962,0.307296,-5.961234,5.998063,-6.552954,-5.233924,-7.448458,0.130822,-9.969003,8.882644,-6.293957,7.640192,-2.443801,1.670130,-3.090357,6.633427,5.250003,-7.082071,4.356249,-5.427356,-1.451194,9.203250,6.237429,-0.386800,8.337119,-6.541744,1.823283,1.778524,0.258790,6.005073,5.789996,2.732101,2.886621,-5.338881,8.299719,-1.678035,-1.459983,8.852575,6.753152,7.358173,7.884288,-3.305336,5.638884,-2.145444,-4.579253,-5.892398,-4.113621,-5.137846,7.334698,-8.448045,7.813875,-1.507732,-5.327329,-2.959796,-3.760756,9.958454,9.916207,-4.002408,2.862971,5.721126,-0.862416,-1.958868,3.755200,4.106097,7.028322,7.672399,-8.434984,-1.050003,6.762238,-1.623313,-1.745796,9.028172,-6.599600,9.841223,-0.737996,7.760696,-0.231139,2.309206,1.821438,1.010119,-8.492973,7.676150,-8.368080,-3.345227,-7.859104,2.894714,-0.514184,-6.705596,-6.180245,-8.812271,-2.038316,-1.037532,3.189824,-1.734516,-4.003366,-5.795514,9.536858,3.973875,5.400939,0.229426,4.365760,7.180132,-2.334501,-9.726787,4.852860,3.110876,-7.577891,-9.346685,-5.904769,-3.784256,-6.620728,2.264249,7.893713,-6.019183,-4.655277,-0.189218,-8.633134,2.828826,-3.262654,-3.524108,0.026312,6.750422,2.157534,3.225523,3.086488,-7.490054,-6.076859,9.035114,-6.206558,5.032760,0.609663,-8.561923,3.465145,-1.855549,5.039124,7.277199,5.710701,4.673596,-3.422616,-4.045636,-2.656172,-2.684794,-4.335572,-3.342714,7.765150,-6.706065,-6.919114,-3.806555,-9.923438,5.067375,5.036715,-7.244466,3.881962,0.012735,9.148497,0.332496,-3.364238,-6.648880,9.115982,-4.263743,-8.723722,-7.483404,7.573975,-9.866844,9.495807,-1.872265,-1.314045,3.694564,-5.339952,-2.247150,-6.032025,0.654990,4.521788,-5.348272,6.147747,3.713928,5.783347,-8.424316,-1.426531,-2.422848,-3.497054,8.547118,-9.323223,-7.162998,0.218724,-0.689721,8.011218,9.924877,3.416445,9.750746,-8.728315,9.499738,-2.315678,-8.453175,-1.859131,8.799579,9.835072,-0.203070,8.750565,-1.870500,0.608531,2.113699,2.320407,7.151448,-5.956539,0.039601,1.265723,-9.425699,-0.945546,-0.506113,4.961695,7.822960,-4.328204,-1.757643,-0.147371,8.670725,7.311662,-5.352945,9.712271,-8.168088,0.304873,-3.550189,-6.777181,-8.076255,3.302788,4.356768,-2.517628,-3.142995,-2.545675,8.337971,5.779073,-4.906041,6.682454,5.239388,-8.321958,-1.940213,9.550358,-5.861303,9.566858,-6.349028,-6.136538,8.091798,-9.756020,7.079550,6.519278,-4.006140,5.378050,4.435966,6.934391,7.551460,-6.695346,6.139104,-5.495759,9.465919,1.390463,1.847174,-5.235394,-8.992261,-0.656251,5.681997,-9.405842,-0.798698,3.812056,-0.643630,8.076829,-8.345300,0.636687,1.106043,-9.612236,4.966571,2.848712,5.889300,-9.491662,-0.787698,1.341658,-6.279088,7.523226,-7.253849,-6.678512,-3.073713,-5.235593,-8.718605,-1.268197,-1.645032,-0.744839,-7.598475,-5.110228,4.568171,-7.007730,6.730624,-1.926253,8.945019,-4.292116,-9.556073,7.289257,-3.048510,3.236048,6.495687,0.069026,-0.256287,-5.709696,9.639745,-9.558595,4.796156,-1.706377,1.607684,-3.342916,4.373468,-6.624375,5.432926,-6.650004,4.062900,-8.616916,4.330941,-4.666010,-2.337233,9.948506,9.671381,-6.458649,-8.244889,5.944676,0.765030,-0.594152,7.145743,-3.618174,-2.926193,-7.449773,8.040829,7.254981,-9.054580,-1.621441,-5.551685,-2.886672,-9.287267,-0.169478,-2.796047,-4.743699,7.536443,-6.888110,2.259778,8.260197,9.830603,4.972945,2.934676,6.898722,6.303649,-5.952211,4.567839,0.833211,8.405436,-0.019586,-2.525745,-9.179861,-9.668644,-6.177805,2.476392,4.865448,9.360633,7.293054,4.442463,5.550485,4.647461,-6.985415,-4.982337,-1.572525,1.633038,4.773143,1.222943,8.624335,-1.874148,1.101134,-3.984367,-7.316194,5.353104,-2.610854,3.363176,5.592292,3.236594,2.579044,-1.388743,6.818076,0.275510,8.877865,-2.863045,-3.441534,-4.419603,7.802767,-5.139868,-9.862632,3.875811,8.443886,-5.925105,3.765750,-0.382108,-4.574126,-1.202306,8.389893,-6.177628,-3.530709,2.983894,-7.812773,-5.959388,-9.530226,0.851895,1.394365,3.073026,9.233455,9.539894,4.865997,-8.055809,-7.796161,-0.458559,-4.187476,-7.354431,9.415330,0.797413,3.208991,1.824883,-4.302535,6.188123,-0.898316,-1.562144,-1.903946,-0.092393,-1.790005,2.208800,-0.447523,-2.317813,8.247654,5.361223,-0.469860,-0.556073,5.562513,-6.703176,-4.706755,5.528255,-1.619075,2.334195,4.188312,1.089227,-6.912699,7.168218,-1.104839,8.827274,-0.334653,-2.931119,4.390057,7.593543,2.790759,-1.836701,3.355699,-5.002331,-1.152633,-8.785460,7.996517,8.587050,0.731560,-7.740714,-8.324144,1.679371,4.857199,7.969618,-8.009343,1.847473,-2.816043,8.540988,0.412658,-2.711542,1.113353,8.805533,-3.204676,-4.534890,5.195461,7.145800,-8.453596,6.312038,-1.103852,-3.139137,1.678219,-8.847124,-7.620211,2.870676,4.277696,9.172842,-3.398219,-3.439496,7.733232,-2.051807,9.139000,-6.064861,-7.438393], dtype = "float32")#candidate|4527|(1152,)|const|float32
call_4526 = relay.TupleGetItem(func_4058_call(relay.reshape(const_4527.astype('float32'), [1152,]), relay.reshape(call_4509.astype('uint16'), [180,]), ), 2)
call_4528 = relay.TupleGetItem(func_4061_call(relay.reshape(const_4527.astype('float32'), [1152,]), relay.reshape(call_4509.astype('uint16'), [180,]), ), 2)
func_3427_call = mod.get_global_var('func_3427')
func_3430_call = mutated_mod.get_global_var('func_3430')
call_4563 = relay.TupleGetItem(func_3427_call(relay.reshape(call_4509.astype('uint16'), [180,])), 0)
call_4564 = relay.TupleGetItem(func_3430_call(relay.reshape(call_4509.astype('uint16'), [180,])), 0)
func_3595_call = mod.get_global_var('func_3595')
func_3599_call = mutated_mod.get_global_var('func_3599')
var_4566 = relay.var("var_4566", dtype = "float64", shape = (845,))#candidate|4566|(845,)|var|float64
call_4565 = relay.TupleGetItem(func_3595_call(relay.reshape(var_4566.astype('float64'), [13, 5, 13]), relay.reshape(call_4520.astype('uint16'), [180,]), ), 2)
call_4567 = relay.TupleGetItem(func_3599_call(relay.reshape(var_4566.astype('float64'), [13, 5, 13]), relay.reshape(call_4520.astype('uint16'), [180,]), ), 2)
func_2247_call = mod.get_global_var('func_2247')
func_2249_call = mutated_mod.get_global_var('func_2249')
call_4568 = relay.TupleGetItem(func_2247_call(relay.reshape(const_4527.astype('float32'), [1152,])), 1)
call_4569 = relay.TupleGetItem(func_2249_call(relay.reshape(const_4527.astype('float32'), [1152,])), 1)
output = relay.Tuple([bop_4494,call_4509,call_4520,var_4521,const_4522,call_4526,const_4527,call_4563,call_4565,var_4566,call_4568,])
output2 = relay.Tuple([bop_4494,call_4510,call_4523,var_4521,const_4522,call_4528,const_4527,call_4564,call_4567,var_4566,call_4569,])
func_4572 = relay.Function([var_4492,var_4493,var_4521,var_4566,], output)
mod['func_4572'] = func_4572
mod = relay.transform.InferType()(mod)
var_4573 = relay.var("var_4573", dtype = "bool", shape = (5, 14, 7))#candidate|4573|(5, 14, 7)|var|bool
var_4574 = relay.var("var_4574", dtype = "bool", shape = (5, 14, 7))#candidate|4574|(5, 14, 7)|var|bool
var_4575 = relay.var("var_4575", dtype = "int32", shape = ())#candidate|4575|()|var|int32
var_4576 = relay.var("var_4576", dtype = "float64", shape = (845,))#candidate|4576|(845,)|var|float64
output = func_4572(var_4573,var_4574,var_4575,var_4576,)
func_4577 = relay.Function([var_4573,var_4574,var_4575,var_4576,], output)
mutated_mod['func_4577'] = func_4577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_4636 = relay.TupleGetItem(func_2131_call(), 0)
call_4637 = relay.TupleGetItem(func_2132_call(), 0)
func_2883_call = mod.get_global_var('func_2883')
func_2884_call = mutated_mod.get_global_var('func_2884')
call_4644 = relay.TupleGetItem(func_2883_call(), 0)
call_4645 = relay.TupleGetItem(func_2884_call(), 0)
output = relay.Tuple([call_4636,call_4644,])
output2 = relay.Tuple([call_4637,call_4645,])
func_4650 = relay.Function([], output)
mod['func_4650'] = func_4650
mod = relay.transform.InferType()(mod)
output = func_4650()
func_4651 = relay.Function([], output)
mutated_mod['func_4651'] = func_4651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4169_call = mod.get_global_var('func_4169')
func_4170_call = mutated_mod.get_global_var('func_4170')
call_4655 = relay.TupleGetItem(func_4169_call(), 1)
call_4656 = relay.TupleGetItem(func_4170_call(), 1)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_4664 = relay.TupleGetItem(func_2562_call(), 3)
call_4665 = relay.TupleGetItem(func_2563_call(), 3)
func_2263_call = mod.get_global_var('func_2263')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_4697 = relay.TupleGetItem(func_2263_call(relay.reshape(call_4664.astype('uint16'), [180,])), 3)
call_4698 = relay.TupleGetItem(func_2266_call(relay.reshape(call_4664.astype('uint16'), [180,])), 3)
output = relay.Tuple([call_4655,call_4664,call_4697,])
output2 = relay.Tuple([call_4656,call_4665,call_4698,])
func_4699 = relay.Function([], output)
mod['func_4699'] = func_4699
mod = relay.transform.InferType()(mod)
mutated_mod['func_4699'] = func_4699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4699_call = mutated_mod.get_global_var('func_4699')
call_4700 = func_4699_call()
output = call_4700
func_4701 = relay.Function([], output)
mutated_mod['func_4701'] = func_4701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3867_call = mod.get_global_var('func_3867')
func_3868_call = mutated_mod.get_global_var('func_3868')
call_4713 = relay.TupleGetItem(func_3867_call(), 1)
call_4714 = relay.TupleGetItem(func_3868_call(), 1)
output = relay.Tuple([call_4713,])
output2 = relay.Tuple([call_4714,])
func_4715 = relay.Function([], output)
mod['func_4715'] = func_4715
mod = relay.transform.InferType()(mod)
mutated_mod['func_4715'] = func_4715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4715_call = mutated_mod.get_global_var('func_4715')
call_4716 = func_4715_call()
output = call_4716
func_4717 = relay.Function([], output)
mutated_mod['func_4717'] = func_4717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_4742 = relay.TupleGetItem(func_2168_call(), 0)
call_4743 = relay.TupleGetItem(func_2169_call(), 0)
var_4746 = relay.var("var_4746", dtype = "float32", shape = (12, 6, 10))#candidate|4746|(12, 6, 10)|var|float32
bop_4747 = relay.logical_or(call_4742.astype('bool'), relay.reshape(var_4746.astype('bool'), relay.shape_of(call_4742))) # shape=(12, 6, 10)
bop_4750 = relay.logical_or(call_4743.astype('bool'), relay.reshape(var_4746.astype('bool'), relay.shape_of(call_4743))) # shape=(12, 6, 10)
func_2696_call = mod.get_global_var('func_2696')
func_2699_call = mutated_mod.get_global_var('func_2699')
const_4775 = relay.const([True,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,False,True,False,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True], dtype = "bool")#candidate|4775|(1404,)|const|bool
const_4776 = relay.const([[-1.383598,-4.263517,-3.883917,-8.626555,-0.235056,0.094319,-6.570261,3.578438,-3.137179,-8.318832,8.267026,-0.151917,-7.603697,-0.251037,1.519773,-9.711351,-9.080987,-0.332465,3.472938,-8.840161,4.411105,-0.454037,-1.765668,2.919741],[8.840673,1.408943,-5.212354,-0.931904,-6.085203,9.768799,-2.087727,8.675246,3.672279,6.766453,-2.149809,-4.381185,-3.643526,-9.081895,-6.559480,4.054432,6.726432,-6.412661,-9.558130,1.957627,-7.298178,7.475633,-7.177930,6.901078],[-0.698991,-4.177097,-6.787296,-6.714205,1.033115,4.475391,3.957596,6.033579,5.285169,-8.743974,8.747127,-0.170781,-2.079223,-6.473118,-1.492923,-0.698582,-9.036458,-9.246118,3.687329,9.952513,4.869386,-4.479474,9.192945,4.114279],[-7.393345,3.393513,0.641385,9.048975,4.846787,-2.887535,7.724862,-5.301644,3.177048,-9.890920,4.445018,3.284581,-2.576373,9.573162,-4.238334,-8.166990,-9.525162,-0.797916,-0.042605,-2.249036,2.809096,5.880055,7.809844,-3.096308],[-6.600645,-8.822762,4.148601,-6.875962,7.816906,2.061288,8.326112,-0.878196,8.808727,8.980423,-0.630103,8.104496,7.233948,-2.390910,-4.731280,7.010372,7.480911,7.975854,-7.718863,-7.074092,2.873528,0.401560,-8.033057,2.523884],[-3.228132,3.531303,-9.404841,-4.973626,7.448483,-1.830069,5.887132,0.136186,7.458108,3.560792,-1.499552,-7.132675,-1.135266,-7.453972,3.123990,-4.464659,1.790602,5.064728,1.938003,5.339962,-6.537600,-7.769434,0.962197,0.584745],[-2.706149,-2.495256,-2.312985,4.589988,-6.161823,1.035263,8.841343,8.888466,9.575020,-9.063980,-0.382531,-2.348203,2.848639,4.616801,-4.710521,-3.585174,3.747614,8.000197,6.853768,-1.417920,9.883137,2.859127,-4.311407,0.253377],[3.818269,-6.262868,1.948203,2.147609,3.015414,8.604084,3.289593,2.204192,4.040051,-6.625948,5.340462,-5.117836,4.066163,9.154595,8.440298,8.798704,-8.523697,-3.753851,-9.409760,-1.193789,-9.839342,8.658582,4.489099,2.208539],[-1.949436,1.689321,-0.763976,-8.630399,-4.626518,7.003299,-7.028974,-5.155887,-3.658823,-1.435061,-9.619098,6.179603,-5.100265,-8.627408,9.044438,-9.843041,-4.384835,6.385808,-2.497952,-8.515155,4.681423,-5.687988,-4.917056,-7.220766],[1.562004,-3.970723,6.863703,7.832599,-3.613416,-1.174865,1.159026,2.517293,-2.542043,-6.359946,-9.940274,2.397312,9.830982,7.781272,0.878282,-0.919704,-5.133044,-7.001157,-4.913727,-0.261317,-7.811606,-2.459287,4.945270,7.143174],[-7.775562,-3.120566,-2.827280,-2.347842,9.182133,1.763309,8.240069,-6.767425,-6.864842,-9.448517,-2.939966,-4.832307,1.484791,-8.556692,-2.653562,-2.403676,5.692238,-6.464656,9.516859,3.805882,-4.673027,7.961727,2.272633,-2.395695],[-9.808743,-1.714347,6.286003,4.224715,-9.655040,6.131821,0.793437,7.314996,5.764771,-7.536479,3.032823,8.164718,0.279593,1.132334,-5.013079,-7.569053,-7.655684,5.812793,0.756522,-6.530494,-6.174829,3.758216,-7.599863,4.288760],[-1.610465,-2.142381,1.115970,6.110881,-3.481985,4.293785,-1.021568,5.251760,1.302671,-7.972288,-5.351755,-1.915094,5.943522,-2.571283,-8.235608,8.601029,-8.398101,-3.173565,5.374701,-2.490618,1.997810,8.196042,7.264532,-6.289096],[4.420852,-7.147237,-7.916023,4.781773,-1.824873,8.791179,4.092962,5.838285,-5.883675,6.404283,8.046408,0.737474,-9.989945,1.348608,0.983061,-7.929589,-7.259853,-8.418446,7.461434,-5.671326,-1.115421,-5.818407,-4.748248,4.250908],[-2.219166,2.309174,-7.760711,-1.181393,2.502843,-2.975752,1.094998,7.162066,4.351872,-3.132174,8.169467,-4.507512,-1.910860,5.473695,-4.953659,9.044026,-2.793233,6.387010,1.118394,2.167030,9.921424,-6.701710,-6.960128,-8.822773],[5.358107,-6.158025,-4.577235,-1.142093,6.044531,4.867360,-4.872955,-6.970301,7.253059,0.070624,5.028729,1.928005,0.573305,-1.330292,-8.054230,5.230126,1.015437,-3.542926,1.194865,7.093257,3.708036,-4.227128,5.343139,-5.685599],[-3.784625,-5.064363,-0.923107,-4.338758,9.333923,8.270334,-9.132450,6.741354,-0.446485,6.585048,2.380155,-5.311380,3.536826,-2.415469,-9.178589,-5.824005,3.101076,-6.970126,-6.468816,5.996518,1.117477,6.392231,4.738817,-8.403971],[2.425436,5.596443,-0.803574,5.457545,5.198169,-7.878897,-1.036990,-5.202341,2.260444,8.797463,-1.746722,9.375545,6.258896,6.923981,-2.681679,-8.227354,8.096651,-8.740477,7.760296,3.955623,5.490645,-1.839239,-9.159755,4.446336],[-2.731497,-7.190995,9.022296,-6.936294,-1.137235,-5.358848,3.009129,-2.536335,-6.366418,-6.039989,-4.116649,-0.210213,-9.651313,0.036150,-1.774314,-2.737697,0.378175,2.782423,4.887201,1.894946,7.911157,-1.749475,-6.330577,3.938785],[4.126880,8.514275,5.884979,3.020393,-5.619990,3.636909,-5.556689,3.526159,-8.131644,-9.619370,1.534563,1.417067,3.415101,1.932769,6.379101,1.061530,2.379738,-6.748105,-8.011180,-0.283030,1.878049,4.421890,8.973333,0.867971],[2.635553,6.867354,-0.130818,2.859088,-5.091621,1.923924,7.764159,-0.656857,3.036737,-8.337565,8.878756,5.017085,-0.366201,-3.258709,4.817142,5.932175,5.215645,7.242813,6.672778,-1.336029,-9.110753,5.784003,-3.764975,-5.422205],[9.305018,7.277809,0.587419,4.507198,-9.567593,2.191056,1.703622,-1.730163,-4.834485,-5.903261,5.322561,0.697966,5.789893,7.360118,7.711839,0.908725,-2.726310,3.573309,8.338252,2.254498,-8.959926,-0.179468,8.160773,-5.783554],[-7.469968,-2.618996,2.424595,7.009496,-0.571984,-4.887968,-2.151522,-2.653832,1.004622,-1.587431,-1.249519,-6.929970,6.371951,4.358904,3.095124,-2.654888,-2.597399,3.826823,-6.994910,-3.610883,-2.483800,-8.836344,9.700125,9.688809],[-9.284450,2.447090,-8.983833,7.095402,-4.481298,-7.081694,8.282571,-7.743127,2.342041,6.219485,-7.922257,3.870313,3.543240,-8.224239,-8.604548,3.977963,8.494746,-2.755717,-7.983014,2.838696,-9.656352,-9.606927,-6.260120,5.738266],[2.358001,-1.025171,8.212406,-6.761142,2.808605,1.745057,-9.356976,8.068507,4.754881,5.906804,4.977447,2.845688,3.194964,7.470922,-9.513464,0.797399,-0.805155,5.614477,4.466558,-5.167741,-4.670316,9.204698,-1.736999,4.604167],[-0.667355,1.149310,4.695391,1.582645,-8.870719,5.211806,2.685462,-0.606604,-5.776244,9.408649,4.701980,-2.024545,4.790284,8.631191,-6.454702,-8.485892,2.401537,5.416547,-1.796491,3.722276,0.663315,0.609751,-0.422082,-0.576743],[7.356547,-7.344948,1.924442,2.417812,-6.080558,-3.104089,0.093004,9.098374,-1.994466,8.516405,2.140328,-8.545834,8.681400,-0.752314,3.537304,-3.221065,-8.952295,-4.926761,-6.272237,2.370894,-3.532010,3.790542,-4.058657,-2.216810],[8.684496,2.841025,8.989281,-4.185295,5.985410,-5.053050,2.776740,3.124536,4.377868,-5.712535,4.278688,4.629738,1.861561,7.411329,0.810270,1.108889,-0.527154,-8.208018,-5.020225,-9.236514,9.449527,-0.812792,-1.455311,-2.347133],[9.650763,8.953119,-2.987852,-9.044178,7.788809,2.480316,-3.683813,-4.614061,6.418712,-4.591918,7.759976,4.858260,8.377764,0.664588,-7.267154,0.560974,-9.766697,-9.731676,4.651307,4.308159,1.380323,-4.466177,5.226453,-7.967858],[0.424954,-7.164699,2.093208,5.618968,4.563362,-9.542041,-3.685769,-3.782558,-1.254813,-4.399030,0.454038,8.468653,-9.422670,-9.984772,-8.557716,6.454123,2.072663,-1.133888,9.204196,0.530356,-8.399934,-5.891468,-7.470502,-3.996342],[-0.534276,-0.596420,-1.533933,-8.107537,0.868022,-1.964462,6.608846,1.030765,3.221984,6.840348,2.564500,8.123915,2.550488,9.667404,-6.321665,-4.800630,-9.083146,6.765150,-0.212821,1.832076,-5.226600,2.475379,0.133747,6.394120],[-0.111074,-2.144740,6.976926,-8.551431,4.547132,-8.182514,7.827311,-1.433049,-3.802153,-1.132854,8.852460,-5.907314,8.261405,3.319819,4.662806,2.917724,-2.441622,5.476176,1.294473,-1.275110,4.604629,6.702821,3.264420,-6.151461],[2.869505,1.362719,4.120585,-1.167592,8.396399,5.713991,-8.718558,6.950394,-0.734577,4.044656,-4.398272,7.967336,-7.182827,-7.908504,-3.654033,4.429176,8.813409,6.857360,6.032406,2.454502,8.369591,8.857418,5.936145,-8.328077],[5.479689,3.649328,7.280774,-5.556440,8.731627,-0.421254,2.846354,5.074479,-7.891566,0.110376,1.177659,-3.564072,-6.767774,-3.349793,-3.497786,0.625609,-2.977385,9.312832,6.778308,-5.468188,-9.945848,8.030182,-4.872482,-3.829107],[6.787002,-3.160587,-6.189875,5.876194,-5.709031,-1.523131,8.666951,2.311127,4.061780,2.464079,-2.285911,2.297239,-5.989674,-5.277306,-3.295456,0.964664,5.124236,-6.420324,2.877512,-7.306254,4.832842,-5.598931,-1.923109,2.790024],[4.588249,9.041382,-7.851276,-8.608157,7.905844,3.536586,-6.588000,9.435929,5.814802,9.627740,2.756420,-5.633745,5.636923,0.980497,-8.986807,8.802339,-2.806770,5.276575,4.820506,2.482862,1.582900,-4.728652,-7.083332,6.039892],[6.466901,-5.459317,-9.667443,-8.610367,8.369119,9.922849,-3.910917,1.781539,2.655624,9.542738,4.940420,9.797708,3.582646,-6.549721,6.375637,2.311866,-8.580692,-6.942745,5.546901,-6.076612,-5.270805,-7.412941,-0.147351,4.802609],[3.194727,3.183322,-3.058426,8.598828,-4.805420,1.469734,6.741473,0.969857,-8.636895,-3.667859,-8.724738,-9.067226,-2.007364,1.279726,6.327418,4.763601,1.566759,7.488235,8.579152,7.274779,-7.283086,-3.798784,-8.590123,9.974751],[5.824403,-7.021363,5.142446,-3.788878,4.011449,-6.274315,5.229251,7.804974,-8.411398,-3.357337,0.273093,-6.206619,-0.905547,6.416781,-1.449083,0.479049,-8.168857,2.893495,-6.888160,-7.405670,0.438062,-7.460234,-5.633717,8.542005],[-7.220843,-8.487461,7.650642,7.790973,6.285281,-6.938558,-5.891131,3.138603,3.503550,-5.896347,7.631806,-8.293953,3.444843,0.782960,-8.164443,5.532410,-5.213599,0.776092,-5.215242,5.362643,0.361971,2.779708,0.052699,6.562778],[4.529010,-0.922948,-0.207024,8.206667,-4.531706,9.167302,7.952292,6.038949,-1.093456,5.941536,-3.221745,3.521909,1.803874,2.716991,7.047101,8.416893,-5.632308,5.745474,-9.981688,-3.227376,7.667058,-8.492848,-9.460253,-1.092797],[-1.760874,0.990057,-3.708024,-4.284887,1.687054,-9.895895,-6.900165,7.291232,-4.169903,5.039388,9.215379,6.784287,5.265390,6.196855,8.458339,3.029972,-2.280854,-6.709187,5.498024,-2.856948,-8.773409,5.083826,-4.099807,9.321246],[-2.183033,-3.042400,8.212288,-4.606670,2.787542,-7.424863,-0.718606,-5.686815,5.764425,4.126743,7.197282,6.102861,0.580560,6.785184,-2.142985,-4.364366,9.422263,-1.452304,-2.022279,-1.456639,5.270608,-2.047744,-9.245239,-0.159710],[-2.817136,-9.676301,7.417737,4.437870,-8.044837,-5.140312,-8.883393,8.338120,7.941213,-3.422118,6.019652,3.503266,0.315098,-8.411904,-7.748359,8.500708,-2.489000,4.767577,-3.336794,-9.764917,3.482075,6.858500,8.865509,8.622320],[-4.944059,-6.964757,-9.571892,-5.962140,-9.675106,5.697597,0.058399,7.488654,-0.945926,9.546186,5.293835,-1.850387,8.429545,-6.267578,-5.154537,9.857622,6.135805,-1.067398,-8.139965,-1.682050,5.855322,8.794303,-6.110817,8.323561],[8.615672,6.534559,-4.382111,5.154435,8.757579,0.492673,-7.295323,6.938063,-6.471317,4.934825,-8.350543,9.977351,-6.993194,9.029806,8.875999,8.501160,7.222044,-0.416800,-6.066188,9.779452,7.081048,-3.414457,-1.504259,-3.652435],[1.447889,9.772568,4.591891,-1.772615,8.115705,-9.121781,-6.925659,-7.002383,8.002675,4.236112,-7.282432,6.084378,4.413030,6.413637,2.140088,6.224210,-3.858799,1.244383,4.316143,5.315463,6.418504,-5.932565,8.972435,6.392815],[0.013780,9.065623,-3.613479,1.585848,-2.580345,4.931025,-7.826630,-1.125566,8.548318,-9.985982,1.036074,9.889802,-9.986181,-0.846097,-0.244119,-0.607614,0.407700,-5.994067,-2.533095,1.414919,-1.297886,3.489284,9.556756,7.907628]], dtype = "float32")#candidate|4776|(48, 24)|const|float32
call_4774 = relay.TupleGetItem(func_2696_call(relay.reshape(const_4775.astype('bool'), [1404,]), relay.reshape(const_4776.astype('float32'), [1152,]), ), 5)
call_4777 = relay.TupleGetItem(func_2699_call(relay.reshape(const_4775.astype('bool'), [1404,]), relay.reshape(const_4776.astype('float32'), [1152,]), ), 5)
func_4650_call = mod.get_global_var('func_4650')
func_4651_call = mutated_mod.get_global_var('func_4651')
call_4784 = relay.TupleGetItem(func_4650_call(), 1)
call_4785 = relay.TupleGetItem(func_4651_call(), 1)
func_3689_call = mod.get_global_var('func_3689')
func_3691_call = mutated_mod.get_global_var('func_3691')
call_4787 = func_3689_call()
call_4788 = func_3689_call()
func_2696_call = mod.get_global_var('func_2696')
func_2699_call = mutated_mod.get_global_var('func_2699')
call_4815 = relay.TupleGetItem(func_2696_call(relay.reshape(const_4775.astype('bool'), [1404,]), relay.reshape(const_4776.astype('float32'), [1152,]), ), 0)
call_4816 = relay.TupleGetItem(func_2699_call(relay.reshape(const_4775.astype('bool'), [1404,]), relay.reshape(const_4776.astype('float32'), [1152,]), ), 0)
bop_4835 = relay.bitwise_and(call_4774.astype('int64'), relay.reshape(const_4776.astype('int64'), relay.shape_of(call_4774))) # shape=(1152,)
bop_4838 = relay.bitwise_and(call_4777.astype('int64'), relay.reshape(const_4776.astype('int64'), relay.shape_of(call_4777))) # shape=(1152,)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_4839 = relay.TupleGetItem(func_2625_call(), 0)
call_4840 = relay.TupleGetItem(func_2626_call(), 0)
func_4715_call = mod.get_global_var('func_4715')
func_4717_call = mutated_mod.get_global_var('func_4717')
call_4852 = relay.TupleGetItem(func_4715_call(), 0)
call_4853 = relay.TupleGetItem(func_4717_call(), 0)
output = relay.Tuple([bop_4747,const_4775,call_4784,call_4787,call_4815,bop_4835,call_4839,call_4852,])
output2 = relay.Tuple([bop_4750,const_4775,call_4785,call_4788,call_4816,bop_4838,call_4840,call_4853,])
func_4858 = relay.Function([var_4746,], output)
mod['func_4858'] = func_4858
mod = relay.transform.InferType()(mod)
var_4859 = relay.var("var_4859", dtype = "float32", shape = (12, 6, 10))#candidate|4859|(12, 6, 10)|var|float32
output = func_4858(var_4859)
func_4860 = relay.Function([var_4859], output)
mutated_mod['func_4860'] = func_4860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4870 = relay.var("var_4870", dtype = "float32", shape = (8, 14, 15))#candidate|4870|(8, 14, 15)|var|float32
uop_4871 = relay.acosh(var_4870.astype('float32')) # shape=(8, 14, 15)
func_2696_call = mod.get_global_var('func_2696')
func_2699_call = mutated_mod.get_global_var('func_2699')
const_4876 = relay.const([False,True,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False], dtype = "bool")#candidate|4876|(1404,)|const|bool
const_4877 = relay.const([[-2.628956,0.620040,-3.043875,-7.098086],[8.252147,0.243451,-9.188396,8.057409],[-3.946909,5.584075,-2.945477,0.600094],[-1.569400,-3.521314,1.748591,-5.813261],[7.450948,1.178791,-6.065698,-9.847859],[-2.970793,-1.577075,9.587883,4.239520],[-8.270133,8.156289,-9.331052,-3.972758],[9.846341,3.461995,-0.255051,-2.032001],[0.473511,3.481248,7.683638,-8.422270],[1.939033,-0.780782,-3.814336,9.376873],[2.630817,5.732388,3.439427,-4.140825],[-5.052533,7.789394,-9.008112,2.218229],[7.200871,6.752435,-3.610045,-2.733255],[-7.360698,-9.839547,-1.058865,-0.357369],[-9.534556,5.638777,6.894670,-9.183784],[-8.834158,-6.790709,0.265682,-3.196047],[-1.836834,-6.049174,5.128099,0.399721],[3.822716,-6.616631,8.642214,3.719198],[2.476886,7.530753,6.956272,-5.733812],[5.979602,-0.609083,-6.957175,6.947845],[-2.110865,2.944543,-7.107399,-9.769604],[-0.112567,-9.656252,1.087442,5.713679],[-5.858837,6.997765,-6.934723,1.249792],[5.212733,9.931213,4.988182,-8.953502],[-0.209523,9.990993,-1.180991,-3.296743],[7.689513,-7.745527,7.961432,3.646600],[-5.659527,5.592602,-1.336401,-1.816149],[-7.552361,-5.895684,-1.796554,0.569159],[-9.234057,-3.274618,-0.758414,-0.469659],[4.525327,-9.071091,-2.257886,-3.415247],[1.652490,-6.503967,4.639330,7.905261],[-5.676365,4.745722,-6.741032,2.034532],[6.213840,-6.259629,-0.091840,4.778166],[0.305847,-3.970565,4.594191,7.561899],[-4.490101,6.017186,-9.426774,0.774280],[-8.729945,-8.427352,-3.048865,2.700880],[8.106590,9.821261,-0.868207,7.181692],[0.865758,-3.656513,-1.594115,7.566702],[9.793461,-7.468104,2.186923,-5.587826],[-5.970132,-7.888158,-7.317264,6.762893],[2.969571,6.942411,5.560514,-7.014313],[3.936067,-0.156808,-9.216432,-5.988899],[-2.549771,1.692236,7.663028,4.478623],[-8.095192,-5.033130,6.410098,-0.567230],[-1.582248,3.665074,-7.894045,-3.277299],[-4.353750,-6.066997,-9.681649,-6.633348],[6.316915,-4.580278,8.500411,9.032247],[-8.650874,-0.140909,6.816161,-4.215358],[-8.136501,3.483320,0.162547,-6.210897],[-2.267477,-3.945621,-5.966485,7.279201],[2.899209,-6.331646,2.962810,-2.355072],[7.290722,-1.494421,-1.770944,-3.632738],[-6.698386,1.302053,-3.299208,5.184339],[-6.753893,1.627058,-2.355768,1.430572],[0.207850,-9.417114,3.300431,-1.713661],[0.973847,6.139992,2.465465,-5.682874],[2.972687,-8.987414,-5.490387,5.332407],[9.565135,8.813216,1.125298,5.214817],[-5.038608,-5.641204,7.101598,-6.992952],[2.359856,-4.655450,5.088345,-4.434493],[-6.537403,-9.595488,-3.282062,-2.039210],[3.743585,6.444357,-9.941751,1.621276],[-0.308386,-1.066350,-8.502392,-0.963459],[-9.031706,-3.675835,0.001413,-4.056584],[4.481960,-5.897524,-5.777541,-5.290066],[-9.827550,7.110711,-7.587984,7.414006],[-5.141782,-0.380847,-4.747891,-1.843001],[0.412344,3.167162,2.734972,8.289403],[-7.471155,-3.968353,-2.490169,-1.681525],[-9.105988,5.324107,-0.379559,8.640968],[-1.182639,8.020928,-1.379608,4.838707],[0.913625,-9.435273,-8.572881,2.534008],[-4.915648,-1.992923,-1.217010,6.208272],[-3.166762,-5.095416,-8.898796,5.574913],[1.027329,1.357066,-3.818063,-9.396613],[4.281994,-1.170656,-1.971291,5.720852],[0.437808,8.614998,-1.887014,-4.876317],[4.039560,-5.802689,-9.189590,-1.678277],[-6.725773,0.781131,-0.877521,-3.108071],[-9.376365,7.456465,0.090261,0.965500],[-8.072519,-5.959176,-0.871433,0.998470],[8.749184,6.736346,8.860633,-0.334317],[2.659336,-6.657721,0.538928,-8.538819],[9.913422,-9.925332,-1.384612,7.591854],[-2.102238,6.143061,-6.840284,-3.666554],[-2.715350,8.294335,7.655433,-7.258279],[9.287073,-2.241464,6.650231,2.534728],[-4.512105,2.556611,0.443332,-7.707381],[0.041988,-6.590657,-3.791171,4.823796],[-4.174488,9.433348,-2.258755,9.316175],[-6.655239,-1.409929,-2.013144,2.807523],[9.120307,4.446139,6.126254,-8.714631],[8.863119,5.019804,9.371114,0.007815],[7.813708,0.449031,-4.632000,-1.770866],[-7.702370,-0.025808,-4.984471,-1.325575],[7.845523,-3.263075,3.082695,8.354492],[-8.823182,-5.315150,1.912731,1.870494],[-7.834142,4.624121,8.785023,-1.124307],[-3.369854,-3.757896,-6.745708,4.541853],[-3.151458,-1.248503,-1.103246,0.640275],[-8.061376,6.771119,3.531836,7.442305],[6.356044,-0.265964,-8.043851,5.345305],[4.112190,1.667103,-3.291595,5.886323],[-9.827872,-3.188624,3.700217,3.589255],[4.128093,-1.060817,-7.399919,5.792763],[-8.760652,-6.199725,-2.754681,2.783020],[-2.867447,2.695682,8.651498,3.962276],[-5.828130,9.257201,2.485139,-5.865928],[3.745195,7.873349,-8.151816,7.138490],[-7.861318,3.714355,5.856533,7.434578],[6.704113,-5.484682,1.716356,-9.824276],[0.940037,-3.249037,4.861320,-2.847179],[4.387603,-2.463891,-8.088145,-6.487582],[0.920861,2.033579,-2.523488,-4.050699],[0.441461,8.626048,9.651566,-2.899195],[7.767542,2.200769,9.303039,4.437990],[-3.158744,-4.290526,3.435290,9.240966],[-7.375683,-4.357207,2.227489,-4.942176],[1.412513,-5.863750,-4.217938,-8.288102],[1.869260,-0.144883,2.218358,4.507193],[6.812594,-1.410040,-8.964120,9.053685],[-6.951774,0.521305,3.423747,-7.041040],[4.179049,0.990883,6.501803,7.105249],[9.763826,-6.875438,4.549336,-9.214460],[4.775548,-6.371356,7.671631,0.030691],[7.543288,9.238877,-1.417112,7.687674],[-9.856154,4.293666,-6.996891,-8.836854],[-4.582656,-5.200853,-8.878334,-4.945162],[6.566910,2.830734,0.669591,-1.061426],[-7.123191,8.119299,2.661937,-1.591955],[2.857823,-6.504139,0.865372,2.180854],[2.254929,1.270394,5.174558,2.548742],[-6.883053,5.129680,9.614683,-6.220052],[1.521161,0.204385,3.747108,4.062323],[5.577333,-5.047659,-6.728424,8.367970],[-4.489102,-8.945237,-3.926796,-3.818462],[-9.811736,-8.288250,-5.794158,6.904696],[-5.868533,-5.602637,8.950085,-5.154321],[9.502626,1.494287,5.973910,5.414601],[2.448061,3.973352,-2.153258,1.504568],[0.414522,-6.491165,-9.321405,6.613103],[-7.988636,-2.608285,0.528937,7.919387],[-1.157967,4.233500,9.165299,2.241145],[-6.513999,-6.882733,-0.409124,8.344463],[-9.219880,9.622572,-2.255584,8.870925],[8.568880,-0.109521,6.484886,8.761453],[-9.448095,8.209649,-6.143618,-1.531581],[9.436542,1.182821,-8.342719,1.093747],[-1.813863,-8.793846,0.296371,-6.156607],[8.357285,-8.763339,-5.827146,-8.403001],[-7.329275,-7.577166,-0.018550,8.348249],[3.994052,-2.729704,5.586772,-6.632958],[-0.162345,-2.316588,2.595770,-5.336676],[6.478718,3.721966,4.344240,-0.527091],[7.558787,-5.043758,-6.052297,9.341138],[-7.817731,0.504136,0.299887,4.014264],[-2.325207,0.181922,-3.539675,8.686076],[-9.433693,5.414592,-6.751459,0.184279],[-4.447177,-7.005523,6.252887,4.233925],[1.492072,-4.745167,-6.446953,-5.411264],[0.224763,-6.095206,-2.328472,-5.078818],[-6.358698,-4.479742,1.796547,-7.693866],[5.943830,-7.597688,-4.145342,-8.694373],[1.938876,-5.188846,-2.516259,-0.478817],[0.526659,-1.624106,-6.480049,-2.406243],[-7.521902,-4.453781,4.836844,-8.171768],[9.361591,6.690555,-9.345364,0.955010],[-1.057894,9.002129,-4.408206,2.122028],[0.228007,3.630255,-1.315317,-8.968282],[-3.654370,-9.590062,-1.027404,-2.648621],[-1.460776,2.840013,0.820864,-4.038117],[1.495185,1.298302,7.376812,8.593633],[-0.184319,8.667395,-3.413590,8.051930],[-7.233246,-8.806047,-3.320493,-2.265840],[7.291775,0.473314,-6.296879,-2.317361],[-1.169285,6.142603,-7.584856,-0.902237],[-7.340501,5.584152,8.103681,4.942064],[9.424188,-3.885294,0.145379,-3.063340],[9.793154,2.793164,2.817195,1.149401],[4.701175,1.741244,7.993186,-7.255789],[3.594670,-8.345795,3.306681,-5.473937],[-6.061144,-1.294722,2.797614,-5.895177],[9.088999,-0.117118,1.539803,-8.826922],[4.201135,6.076054,4.931725,-6.134206],[3.201688,8.877242,-8.307765,4.115880],[5.256597,-9.466276,-4.332325,1.550381],[0.337968,-4.263658,7.007331,8.276257],[1.100860,4.977310,4.958882,1.347402],[-4.327824,5.126513,2.045138,7.263010],[-7.669213,4.297342,-2.189943,-7.546540],[7.360724,4.009815,8.625605,3.308797],[7.109768,4.402908,-6.768577,5.106127],[-3.440086,7.535400,-5.662552,-2.444971],[6.093443,2.808380,-2.010579,3.605313],[4.123960,-8.065329,4.243144,2.315487],[-8.689748,8.375812,2.744453,6.254175],[8.860907,8.194364,-3.472111,8.699265],[-7.020158,4.561760,-8.938660,-9.348164],[3.493184,5.346360,-4.061908,5.597382],[8.345989,4.922979,-1.471160,-2.643938],[2.157780,1.633851,5.655157,3.111116],[1.097034,-3.003678,4.082978,8.268940],[6.831580,-4.275747,2.778264,-2.811687],[-7.482845,-2.960303,4.605019,4.710833],[-5.786357,-6.880218,0.648066,9.799444],[-0.960594,-1.877338,-1.347984,8.402201],[-0.430443,3.521245,1.006999,5.735440],[7.370227,-7.195080,-8.910637,-7.451938],[-6.934126,6.102288,-0.267265,0.327207],[-8.699579,8.132016,3.908158,0.007936],[-7.246173,-6.875635,-3.281515,9.000159],[2.095223,-5.359088,7.990314,-8.594600],[3.175008,9.994862,5.737328,4.617730],[2.051537,-9.771513,8.400165,-2.438379],[2.100512,7.404345,-0.704602,3.927275],[2.340226,-3.540909,-5.932700,-0.053581],[-1.074632,-9.908748,-8.670231,5.278986],[-1.668900,2.014780,2.638982,8.790844],[-4.693946,0.557540,3.745646,-1.964968],[-9.888991,-6.560186,0.472698,9.503776],[-0.372420,5.263798,8.843507,-5.134267],[4.100083,0.913233,-4.808185,8.025842],[3.132169,1.249252,1.857999,4.541771],[-1.460522,7.379535,6.454056,8.966090],[-1.321935,-0.022218,-4.323134,7.615066],[-4.521780,-4.984510,4.071502,4.338700],[-4.975263,4.850322,-2.022603,-9.704957],[-3.594860,3.905520,-4.093623,-0.773802],[3.460852,-6.159841,1.812348,0.571927],[-5.729814,-6.763934,3.248489,-0.622617],[3.951743,-3.218133,3.087418,-1.274442],[-9.850707,9.682182,2.387547,2.406976],[-7.642026,-5.449411,0.984225,-6.033219],[7.629721,7.673294,-8.773359,5.412553],[6.654418,-2.724610,-1.570977,9.485190],[-0.879161,0.012291,-3.639669,-1.531220],[-7.730707,-3.069018,8.896690,7.637409],[-3.658164,1.245208,-0.754810,-6.661930],[-0.326485,-0.123213,4.233498,8.093583],[-4.831223,8.875212,5.611859,-3.673560],[-9.857771,5.545531,4.883884,0.136643],[7.133907,-7.033687,9.883690,-3.980267],[0.350603,-3.384367,-9.078963,-7.962710],[-3.318976,3.968324,-9.378091,2.469425],[-6.049904,-5.951764,9.285223,7.879831],[-7.590246,-3.995958,-7.624092,-2.982988],[-1.997576,7.160192,-7.526446,0.400645],[5.948723,6.912418,-6.998057,2.657491],[8.133637,-8.382943,7.982908,-0.582863],[-6.149772,5.421923,4.764843,-9.556257],[-7.725019,-0.683340,-0.553094,5.341808],[-3.267452,1.629911,5.443916,5.049647],[-0.960431,6.037169,-4.823734,9.680698],[-2.073961,1.133101,-2.079055,8.442133],[2.387131,-2.856957,-0.645418,-2.646319],[-0.947896,9.866478,-8.372820,-2.702218],[2.797467,-2.345405,8.942580,-3.105151],[-2.643615,0.325669,1.766463,4.671119],[-1.816712,-5.222676,0.499927,4.780391],[-8.653362,4.643762,-9.325424,1.211352],[1.992350,2.834684,-6.213019,-9.360235],[2.213290,2.565677,2.771444,-4.054500],[-4.089541,-2.242254,6.589769,8.671353],[-8.904423,-5.210116,5.376575,-3.981237],[6.400638,9.835620,3.365068,-6.037721],[-5.594750,-5.171272,-7.073051,1.397123],[6.954001,-7.909777,-3.911582,5.373595],[-3.990436,6.631190,4.265962,-9.993111],[3.250934,-0.995974,4.431768,1.466595],[2.203645,2.688286,-3.000489,-8.761631],[-7.598470,-3.364884,9.679535,-3.944272],[9.307717,8.195198,1.700843,2.465655],[1.554690,-4.386212,-5.196469,-1.388163],[2.810724,5.467031,8.404658,8.281486],[-3.974041,-8.619573,4.539294,5.897167],[-6.830179,-8.877217,-6.198854,-8.502956],[4.106441,1.767147,-6.282716,4.676708],[5.008361,-1.554377,5.427720,6.810069],[4.987143,0.986783,-9.321913,-7.676181],[8.739096,-8.400803,-6.467783,8.673771],[3.215303,-5.256024,3.939972,5.305145],[-8.752996,0.652994,-9.685347,-7.378462],[-1.859986,-3.208273,-7.715643,4.024756],[8.465993,-4.556545,-2.273768,-5.117398],[-6.247780,5.891621,-4.797170,-0.371600],[-7.134421,-2.427342,-5.210088,8.498574],[-4.817226,7.001408,-1.683061,-7.689611],[9.601209,4.116088,4.510139,5.479952]], dtype = "float32")#candidate|4877|(288, 4)|const|float32
call_4875 = relay.TupleGetItem(func_2696_call(relay.reshape(const_4876.astype('bool'), [1404,]), relay.reshape(const_4877.astype('float32'), [1152,]), ), 5)
call_4878 = relay.TupleGetItem(func_2699_call(relay.reshape(const_4876.astype('bool'), [1404,]), relay.reshape(const_4877.astype('float32'), [1152,]), ), 5)
func_2655_call = mod.get_global_var('func_2655')
func_2658_call = mutated_mod.get_global_var('func_2658')
var_4881 = relay.var("var_4881", dtype = "uint16", shape = (180,))#candidate|4881|(180,)|var|uint16
call_4880 = relay.TupleGetItem(func_2655_call(relay.reshape(var_4881.astype('uint16'), [180,])), 2)
call_4882 = relay.TupleGetItem(func_2658_call(relay.reshape(var_4881.astype('uint16'), [180,])), 2)
output = relay.Tuple([uop_4871,call_4875,const_4876,const_4877,call_4880,var_4881,])
output2 = relay.Tuple([uop_4871,call_4878,const_4876,const_4877,call_4882,var_4881,])
func_4883 = relay.Function([var_4870,var_4881,], output)
mod['func_4883'] = func_4883
mod = relay.transform.InferType()(mod)
var_4884 = relay.var("var_4884", dtype = "float32", shape = (8, 14, 15))#candidate|4884|(8, 14, 15)|var|float32
var_4885 = relay.var("var_4885", dtype = "uint16", shape = (180,))#candidate|4885|(180,)|var|uint16
output = func_4883(var_4884,var_4885,)
func_4886 = relay.Function([var_4884,var_4885,], output)
mutated_mod['func_4886'] = func_4886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4186_call = mod.get_global_var('func_4186')
func_4188_call = mutated_mod.get_global_var('func_4188')
call_4903 = relay.TupleGetItem(func_4186_call(), 0)
call_4904 = relay.TupleGetItem(func_4188_call(), 0)
output = relay.Tuple([call_4903,])
output2 = relay.Tuple([call_4904,])
func_4905 = relay.Function([], output)
mod['func_4905'] = func_4905
mod = relay.transform.InferType()(mod)
mutated_mod['func_4905'] = func_4905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4905_call = mutated_mod.get_global_var('func_4905')
call_4906 = func_4905_call()
output = call_4906
func_4907 = relay.Function([], output)
mutated_mod['func_4907'] = func_4907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3981_call = mod.get_global_var('func_3981')
func_3982_call = mutated_mod.get_global_var('func_3982')
call_4957 = relay.TupleGetItem(func_3981_call(), 0)
call_4958 = relay.TupleGetItem(func_3982_call(), 0)
func_4169_call = mod.get_global_var('func_4169')
func_4170_call = mutated_mod.get_global_var('func_4170')
call_4962 = relay.TupleGetItem(func_4169_call(), 0)
call_4963 = relay.TupleGetItem(func_4170_call(), 0)
uop_4979 = relay.log(call_4962.astype('float32')) # shape=(12, 6, 10)
uop_4981 = relay.log(call_4963.astype('float32')) # shape=(12, 6, 10)
output = relay.Tuple([call_4957,uop_4979,])
output2 = relay.Tuple([call_4958,uop_4981,])
func_4982 = relay.Function([], output)
mod['func_4982'] = func_4982
mod = relay.transform.InferType()(mod)
mutated_mod['func_4982'] = func_4982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4982_call = mutated_mod.get_global_var('func_4982')
call_4983 = func_4982_call()
output = call_4983
func_4984 = relay.Function([], output)
mutated_mod['func_4984'] = func_4984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_4994 = relay.TupleGetItem(func_2168_call(), 0)
call_4995 = relay.TupleGetItem(func_2169_call(), 0)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_4998 = relay.TupleGetItem(func_2168_call(), 0)
call_4999 = relay.TupleGetItem(func_2169_call(), 0)
func_631_call = mod.get_global_var('func_631')
func_636_call = mutated_mod.get_global_var('func_636')
const_5026 = relay.const([5.552787,4.639289,-3.311853,9.917944,-0.692312,0.203912,-8.317764,-7.172917,-4.748540,-7.903261,1.510479,-8.788598,5.943070,6.071003,-0.730824,1.183630,-3.129816,7.332877,-0.267254,-1.622810,9.156493,0.295604,-8.560425,-5.114478,8.347943,-6.212990,2.034350,-9.702357,6.471440,8.261342,-6.885127,7.006781,2.774111,-4.443028,0.296935,9.627745,-5.079100,-5.106239,-0.685935,-1.847898,0.929650,7.433925,6.485762,-1.078020,3.864881,-5.751899,-6.768593,4.322218,-2.587591,8.425844,-8.191128,8.636766,4.911648,8.896303,-8.381421,5.962006,-9.852410,-9.595680,1.192714,-4.735451,4.176767,-7.700117,-6.967734,3.449515,0.996188,-5.667118,2.284426,7.241639,0.024585,3.603603,-2.201353,-1.692157,7.985784,-2.582891,9.342693,9.607155,2.256353,-5.789161,0.690329,5.346143,-4.142402,-6.614672,1.077159,4.054244,0.491704,-1.266948,8.610382,-3.704330,-4.229892,5.441068,-7.855528,-9.903130,7.461335,2.127422,-4.350901,5.104086,8.689933,6.690829,9.247420,5.969067,2.354341,-8.224470,-8.777671,5.111271,3.829460,-8.713664,1.197306,-9.366354,7.001954,-4.982326,-7.620340,6.225658,0.452268,-8.063270,4.740553,1.665293,9.615112,4.053880,1.404023,-6.706851,-5.103867,-6.825429,2.978406,-1.193964,-6.924200,2.219295,-9.007532,-0.998762,2.105935,6.219437,8.555936,7.066119,-7.076962,-3.115973,2.784858,5.943876,-8.538874,5.414312,-4.329613,-8.198089,-8.329907,1.696025,-3.070833,8.323239,-4.849185,-6.108468,7.119464,-8.957280,2.601645,1.659869,-2.270521,-9.286228,-5.804172,-7.923283,1.039714,-0.928203,-8.440647,-9.955345,9.467312,-6.678983,-3.359896,9.425981,-8.636397,-5.830621,0.567814,-0.642949,-7.049191,-5.905887,6.751246,3.654634,8.077631,-7.282869,3.190768,9.579433,-6.730446,-5.982861,-4.783104,0.009200,3.233997,-1.687276,5.207020,-3.603378,7.697292,2.157967,-2.967184,8.228735,-9.479556,2.403768,8.271906,-1.463440,0.651070,-9.198914,9.418348,-3.400093,6.406645,4.746933,-4.364008,-8.839249,-9.184457,-6.874790,-9.592634,-3.097677,5.672268,-7.369467,-2.794389,8.719258,6.997373,-5.982643,9.028922,-1.725927,9.720586,8.851499,3.618448,-4.500998,6.481896,-0.449529,-2.548255,-0.897596,2.342554,-5.780076,-2.803209,4.927395,-2.481424,-0.918233,-9.240802,-4.638801,-0.751531,8.205430,-9.679706,5.173124,-2.899413,9.640208,-6.384264,6.177545,8.288069,-5.675766,5.331342,2.684340,8.105683,8.229300,-3.230243,7.758013,8.021298,4.422772,-0.141637,-8.783312,-0.608549,-5.162373,3.703820,-4.543567,9.326437,-1.624956,-9.110699,-9.297027,6.529628,-7.835511,-8.051333,-2.255851,-3.451499,0.662130,-2.336263,-8.097726,6.547881,-2.628656,-3.983525,5.009634,3.808618,-2.346720,-2.915702,4.684149,-2.298343,3.674083,6.113723,-3.643135,2.410792,4.199942,4.465619,2.703163,-8.256064,-4.892816,-2.019134,-7.182323,7.899881,-1.749513,-3.941100,-6.971949,7.318721,5.043505,6.916675,-7.920865,2.464985,4.309781,4.754354,2.534977,-7.308953,-1.227422,-7.538128,-4.382930,5.013320,1.809757,-0.583100,-2.933608,1.457016,-8.254155,-3.603853,-9.021794,-4.901187,-8.872727,-4.759050,3.440621,3.969070,5.493784,6.248189,-6.930873,-7.526602,-8.419379,6.314722,-5.171529,-8.624719,0.784141,-2.671038,-0.041118,0.365146,-6.759734,-8.561913,-5.371337,-1.510539,6.109700,3.767089,-4.092374,4.855048,-8.393059,-4.330348,-0.645292,-0.509438,9.677572,7.413419,1.668653,-0.871958,-0.986070,-1.438043,9.397060,-8.691981,-6.375494,-0.389817,-9.736133,7.995879,-1.557056,1.872822,-4.622363,-5.743846,-1.109398,3.342957,6.019077,-2.197549,-3.824614,-0.670436,3.771568,2.792516,3.917958,-8.623887,7.721762,-1.131970,4.455724,-1.716226,6.474901,8.489522,-3.017699,-1.245480,3.612462,3.175447,9.669250,8.034306,6.311474,-6.359479,-2.129411,-5.989076,-1.644986,1.105278,-7.445540,6.683186,-0.142230,-5.210728,1.264461,-1.027286,8.681962,-9.299862,-5.571083,3.332666,-2.218162,-8.120174,-0.722632,2.813424,3.197110,2.185635,-2.426958,-0.633842,9.998637,-2.317428,9.637844,7.169589,-7.487843,0.540554,3.896806,-3.941428,-6.711470,-4.231427,7.509075,0.986855,-8.105983,1.013818,8.663370,-2.627542,-9.074828,7.313192,9.950680,-1.909120,-9.904039,-6.511228,-7.900716,-5.774721,4.159906,7.629056,-8.995894,-2.021269,6.616778,4.478503,4.495315,-6.364334,-2.420631,6.968768,-2.718901,-4.221593,4.546207,7.912883,1.715744,-8.113282,-1.314214,-8.521123,-6.762312,-6.693321,-0.267779,-3.241034,0.823163,4.802714,-7.231491,4.440996,-6.218404,1.284509,7.359222,3.542155,-8.219671,9.186002,9.597139,1.396503,-2.673593,-7.226605,-5.428540,-6.129447,8.199353,7.070704,-0.532433,-3.268735,-4.253091,-5.075289,-5.122859,7.733862,9.859257,-8.186803,-6.229745,-8.466082,9.964208,9.447209,1.818866,0.942219,4.992726,-8.031877,3.192851,-1.780041,4.966088,5.631409,-3.247842,-1.178815,-8.257442,-1.066718,9.439069,6.645574,5.674417,-3.629653,0.320455,0.310829,-0.544618,-4.958366,5.234348,-3.081165,-0.424708,-9.001907,-2.709952,-9.453075,1.856362,5.503829,-0.893267,6.778506,5.988900,-8.256150,4.936201,2.420740,-8.501876,-9.551130,-7.041340,-9.182113,-2.397010,8.250499,0.633581,6.611985,-4.266278,1.554770,-9.717082,8.699666,-5.615978,-3.138329,5.835605,-6.448204,1.154755,1.630621,7.435282,-8.750066,6.577465,-3.723189,-8.251671,5.087946,-0.633475,1.372953,-6.047537,-6.123817,-1.249586,-8.225202,-3.229738,6.507704,9.750913,8.655805,-7.379375,2.249783,2.996329,2.665427,9.705887,-5.276062,6.044324,-0.794588,-5.149201,5.765950,8.601968,2.961155,-6.062837,-9.272504,1.007488,-3.323132,2.454771,8.770900,2.270975,-0.586236,-7.095571,-9.629109,-7.938480,7.694664,9.909107,-6.391440,-1.159270,-3.340686,-1.741245,6.420658,-9.060103,-9.226266,3.599997,-6.873692,-1.398080,6.410485,7.137887,-8.026666,7.596175,5.646098,-6.092629,3.597954,5.260235,0.211820,-2.044427,5.801632,-3.620981,2.604015,-1.449857,-4.828326,-1.906182,2.841652,1.850533,-9.011751,2.749134,5.164551,4.617067,-2.879886,-8.750086,-9.827515,-3.124787,8.648404,1.252165,-7.792864,-6.166941,-9.962420,4.238473,9.169141,-7.449207,6.153368,7.371883,2.007126,7.020310,4.529896,-2.809583,1.423952,7.481582,7.487192,6.835107,-3.141205,9.200751,-7.099375,-6.446986,7.253855,5.729411,-8.122518,-5.101607,3.437003,-8.622306,8.173997,3.216570,7.613902,-0.998851,6.989282,1.762925,7.552522,9.083804,0.336869,5.994097,-7.611644,5.397584,3.918107,-4.348023,3.293451,5.647675,2.552558,2.470025,-7.450453,-6.885258,4.601922,5.667327,-9.190711,0.748661,3.854039,-7.323231,4.429293,-8.028230,4.431183,-9.971850,8.167800,-8.195373,-1.463289,-7.116700,2.088729,-2.977956,-2.294739,5.643736,-0.231469,-6.892377,-4.349753,8.853247,-5.752148,-7.883879,3.166611,-1.108396,3.093496,5.498365,4.191880,-9.640087,-6.656228,9.486640,-7.935750,1.022285,5.807124,-1.891945,9.682851,-3.793914,-5.020555,2.421255,4.377870,-3.087603,-8.329386,-6.744298,3.627814,-8.374822,8.849276,-7.020104,2.131573,9.979019,3.913854,-3.108169,4.151101,-8.980741,2.808640,0.330509,-5.003513,8.945328,-1.493916,-6.100755,-9.701370,6.725717,-2.796962,-3.060851,-8.875736,9.061082,4.481380,-8.735343,-3.025534,-7.619456,-6.045639,-2.689167,-1.021985,-0.753597,6.247737,-4.148704,8.555222,2.881695,-2.820043,5.041651,1.542888,-3.408803,-4.067131,-3.281893,-0.956319,4.383433,-1.670066,2.501126,5.326334,4.632708,-8.011205,5.646836,-4.773366,3.540879,-9.495157,0.280103,1.732513,-6.903431,-9.066908,-1.764241,-5.400093,7.662022,3.460315,5.347863,-5.718064,3.694211,-9.173174,4.037328,-6.808740,9.817058,3.467244,-6.700264,7.822276,4.586869,6.783283,-6.720229,4.605213,6.815198,-4.430567,1.190027,0.611781,5.945600,2.669613,-3.959791,0.752168,-9.717920,-9.788526,-3.145197,-8.691550,0.216475,5.005781,3.326618,-3.933901,-1.765596,9.750315,0.996587,-0.265594,-3.400902,0.164337,5.173018,4.479145,-0.231425,2.197081,6.785056,-6.639791,9.617902,-3.493313,-9.288079,2.492566,4.646436,-8.782084,-6.198641,2.657075,6.364895,3.759938,9.800455,-8.974822,4.251957,-7.386194,1.903912,7.995702,3.380652,1.940348,-1.067877,-0.870627,6.551957,7.490644,3.361040,3.754798,5.395526,-6.711397,4.733466,-2.320846,-5.774202,0.416945,3.262443,-0.100815,-4.141471,-9.626613,9.047697,-0.910895,-8.226493,-4.328666,-7.987496,-0.416514,-5.387700,-7.727381,8.991218,-7.643461,-0.981931,-5.243035,3.426773,-5.125794,-9.125491,-8.670018,8.867854,7.387707,-0.707549,5.422552,2.612240,3.160204,-9.420802,7.353427,-5.405646,4.463354,2.720137,7.464561,9.952417,-4.816626,-7.776750,7.698098,6.100473,2.959955,-7.083890,-3.550074,-6.512044,1.300866,4.346730,5.910652,8.873965,-4.941304,-6.117823,7.029864,1.939493,9.209251,-9.577742,9.599871,2.355704,-3.792590,-4.883640,1.400034,-0.189562,3.922571,6.856493,8.430385,-6.991427,6.870724,6.660239,-8.169159,-4.243797,8.097580,-1.930328,-3.820465,7.441591,7.928432,5.471741,1.992054,4.385847,-3.053450,5.637591,4.861629,2.681708,-3.504668,6.817953,-1.599720,-0.395975,5.644438,-3.505598,0.973557,-6.560533,4.738556,6.977469,4.833062,-2.246544,-2.352375,0.866437,5.806158,-8.092950,-4.142738,-4.235056,-9.631455,-9.769040,3.664233,3.872166,-6.697207,8.892996,-7.834246,-8.290930,6.648058,3.149306,-7.985845,-1.073551,0.231048,1.937183,-8.993347,-8.165244,1.149367,-1.906280,-1.744289,7.587726,7.767373,-6.000063,0.926828,3.009102,2.708818,-0.670749,-6.652898,3.388738,-4.525406,7.118611,-8.972082,2.427425,-3.627144,-6.309804,7.194019,1.118387,-9.404571,-4.430948,0.871084,0.969235,-4.200340,-5.696748,-2.726799,3.254850,2.042218,7.124518,-6.337162,5.715559,2.754534,4.961670,3.831057,4.387752,4.187575,3.327017,-0.838536,8.582107,0.863479,6.281847,-4.321446,-7.097552,6.534667,6.010449,-5.195099,-2.649507,3.213566,-5.594835,-8.656716,-3.038110,-7.512818,-3.351012,-3.984075,4.305046,-2.656671,6.437839,5.153960,-5.600727,-6.536052,6.070976,-9.606562,-1.544970,2.415792,-0.369871,-0.290405,6.487644,-8.190544,7.099425,-8.474667,-4.152348,5.367357,2.392674,7.723985,9.481472,5.017569,-4.680174,-2.915440,8.077367,-1.939703,-9.162245,0.851353,7.162394,0.564315,-9.291097,8.900955,-6.719048,4.124563,-4.752322,7.491427,-1.832247,-2.932945,-8.662443,1.035689,-6.483101,1.175515,-5.199016,8.374904,0.645240,4.901823,-6.863593,-9.487880,6.361477,-1.187171,4.902670,-3.577945,-2.919764,-5.388274,6.432521,0.477024,8.911029,-9.829914,5.203961,5.414540,8.559523,-2.294957,-4.000027,-5.746689,-6.110194,6.678680,8.997143,0.755173,-8.202038,-1.164659,5.273979,2.253439,3.497277,4.795054,2.609029,5.171908,8.081998,-0.041308,-1.090901,0.883138,0.124776,-1.837253,-7.210002,2.344398,-6.443650,8.623678,9.302470,-6.448036,-5.619749,5.846559,9.650006,-6.262017,-2.422614,-8.918265,-9.769807,-7.851620,-3.429388,-6.750205,-3.541391,9.070142,1.014045,6.498332,3.799181,3.965878,5.937316,-5.251549,6.038368,3.879409,8.133375,4.784822,7.810044,-5.081334,-6.372914,4.192331,-5.594940,3.261736,3.962177,-9.065993,8.961347,-1.327517,-3.144072,7.069713,-6.622504,2.664052,-8.727006,8.532117,-6.796933,2.926683,-2.095206,-7.780757,7.164860,-4.580747,-6.370788,3.597570,1.490681,-2.876621,-3.223759,8.899684,-8.425900,7.437041,7.368696,-4.928671,-0.856052,0.749138,-3.495377,9.093099,5.280375,-0.520630,-4.594425,0.792645,-3.762496,3.341298,6.649064,5.645136,2.832391,-6.267941,9.384003,9.136536,-9.296099,-9.101849,-1.182653], dtype = "float32")#candidate|5026|(1152,)|const|float32
var_5027 = relay.var("var_5027", dtype = "uint16", shape = (180,))#candidate|5027|(180,)|var|uint16
call_5025 = relay.TupleGetItem(func_631_call(relay.reshape(const_5026.astype('float32'), [16, 12, 6]), relay.reshape(var_5027.astype('uint16'), [180,]), relay.reshape(var_5027.astype('uint16'), [5, 6, 6]), ), 11)
call_5028 = relay.TupleGetItem(func_636_call(relay.reshape(const_5026.astype('float32'), [16, 12, 6]), relay.reshape(var_5027.astype('uint16'), [180,]), relay.reshape(var_5027.astype('uint16'), [5, 6, 6]), ), 11)
uop_5047 = relay.asinh(call_4994.astype('float32')) # shape=(12, 6, 10)
uop_5049 = relay.asinh(call_4995.astype('float32')) # shape=(12, 6, 10)
func_4291_call = mod.get_global_var('func_4291')
func_4293_call = mutated_mod.get_global_var('func_4293')
call_5058 = relay.TupleGetItem(func_4291_call(), 1)
call_5059 = relay.TupleGetItem(func_4293_call(), 1)
output = relay.Tuple([call_4998,call_5025,const_5026,var_5027,uop_5047,call_5058,])
output2 = relay.Tuple([call_4999,call_5028,const_5026,var_5027,uop_5049,call_5059,])
func_5062 = relay.Function([var_5027,], output)
mod['func_5062'] = func_5062
mod = relay.transform.InferType()(mod)
var_5063 = relay.var("var_5063", dtype = "uint16", shape = (180,))#candidate|5063|(180,)|var|uint16
output = func_5062(var_5063)
func_5064 = relay.Function([var_5063], output)
mutated_mod['func_5064'] = func_5064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4071_call = mod.get_global_var('func_4071')
func_4072_call = mutated_mod.get_global_var('func_4072')
call_5075 = relay.TupleGetItem(func_4071_call(), 0)
call_5076 = relay.TupleGetItem(func_4072_call(), 0)
func_3427_call = mod.get_global_var('func_3427')
func_3430_call = mutated_mod.get_global_var('func_3430')
const_5089 = relay.const([3,-3,2,6,-7,7,2,-10,-7,6,3,7,-1,7,-3,3,-8,2,-10,-5,9,-8,2,-8,4,6,3,7,-8,-5,-1,-6,-3,-8,-9,1,6,9,-7,7,-10,-9,8,-9,4,-9,2,-1,-4,-1,-3,10,-2,-5,5,-2,-5,-10,-9,-9,-2,-8,-4,1,-10,-10,5,-10,1,7,9,3,-10,-9,1,-2,8,9,-8,7,-3,1,-7,6,-8,3,2,-5,10,-1,-4,6,-4,-4,-7,10,-10,-9,-2,4,-8,1,-7,-4,2,10,10,-10,2,7,-6,9,-8,4,3,-1,-9,5,-9,-2,6,-9,-7,3,2,9,6,6,8,3,-8,-6,-9,2,8,8,-6,-2,-5,-2,-2,-5,-1,-2,10,2,-2,-6,7,-8,4,3,-5,2,-8,7,7,10,-4,7,-8,6,7,-10,2,3,3,7,-9,-8,-5,-8,-6,10,-9,-3,-6,-8,1,-1], dtype = "uint16")#candidate|5089|(180,)|const|uint16
call_5088 = relay.TupleGetItem(func_3427_call(relay.reshape(const_5089.astype('uint16'), [180,])), 1)
call_5090 = relay.TupleGetItem(func_3430_call(relay.reshape(const_5089.astype('uint16'), [180,])), 1)
output = relay.Tuple([call_5075,call_5088,const_5089,])
output2 = relay.Tuple([call_5076,call_5090,const_5089,])
func_5093 = relay.Function([], output)
mod['func_5093'] = func_5093
mod = relay.transform.InferType()(mod)
output = func_5093()
func_5094 = relay.Function([], output)
mutated_mod['func_5094'] = func_5094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5112 = relay.var("var_5112", dtype = "uint32", shape = ())#candidate|5112|()|var|uint32
var_5113 = relay.var("var_5113", dtype = "uint32", shape = (4, 3, 13))#candidate|5113|(4, 3, 13)|var|uint32
bop_5114 = relay.subtract(var_5112.astype('uint32'), var_5113.astype('uint32')) # shape=(4, 3, 13)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
var_5125 = relay.var("var_5125", dtype = "uint16", shape = (180,))#candidate|5125|(180,)|var|uint16
call_5124 = relay.TupleGetItem(func_261_call(relay.reshape(var_5125.astype('uint16'), [5, 6, 6])), 0)
call_5126 = relay.TupleGetItem(func_263_call(relay.reshape(var_5125.astype('uint16'), [5, 6, 6])), 0)
uop_5136 = relay.sinh(call_5124.astype('float64')) # shape=(5, 6, 6)
uop_5138 = relay.sinh(call_5126.astype('float64')) # shape=(5, 6, 6)
var_5144 = relay.var("var_5144", dtype = "float64", shape = (5, 6, 6))#candidate|5144|(5, 6, 6)|var|float64
bop_5145 = relay.divide(uop_5136.astype('float32'), relay.reshape(var_5144.astype('float32'), relay.shape_of(uop_5136))) # shape=(5, 6, 6)
bop_5148 = relay.divide(uop_5138.astype('float32'), relay.reshape(var_5144.astype('float32'), relay.shape_of(uop_5138))) # shape=(5, 6, 6)
func_3427_call = mod.get_global_var('func_3427')
func_3430_call = mutated_mod.get_global_var('func_3430')
call_5151 = relay.TupleGetItem(func_3427_call(relay.reshape(var_5144.astype('uint16'), [180,])), 1)
call_5152 = relay.TupleGetItem(func_3430_call(relay.reshape(var_5144.astype('uint16'), [180,])), 1)
func_2131_call = mod.get_global_var('func_2131')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_5159 = relay.TupleGetItem(func_2131_call(), 1)
call_5160 = relay.TupleGetItem(func_2132_call(), 1)
func_4982_call = mod.get_global_var('func_4982')
func_4984_call = mutated_mod.get_global_var('func_4984')
call_5163 = relay.TupleGetItem(func_4982_call(), 1)
call_5164 = relay.TupleGetItem(func_4984_call(), 1)
func_3981_call = mod.get_global_var('func_3981')
func_3982_call = mutated_mod.get_global_var('func_3982')
call_5165 = relay.TupleGetItem(func_3981_call(), 0)
call_5166 = relay.TupleGetItem(func_3982_call(), 0)
output = relay.Tuple([bop_5114,var_5125,bop_5145,call_5151,call_5159,call_5163,call_5165,])
output2 = relay.Tuple([bop_5114,var_5125,bop_5148,call_5152,call_5160,call_5164,call_5166,])
func_5170 = relay.Function([var_5112,var_5113,var_5125,var_5144,], output)
mod['func_5170'] = func_5170
mod = relay.transform.InferType()(mod)
var_5171 = relay.var("var_5171", dtype = "uint32", shape = ())#candidate|5171|()|var|uint32
var_5172 = relay.var("var_5172", dtype = "uint32", shape = (4, 3, 13))#candidate|5172|(4, 3, 13)|var|uint32
var_5173 = relay.var("var_5173", dtype = "uint16", shape = (180,))#candidate|5173|(180,)|var|uint16
var_5174 = relay.var("var_5174", dtype = "float64", shape = (5, 6, 6))#candidate|5174|(5, 6, 6)|var|float64
output = func_5170(var_5171,var_5172,var_5173,var_5174,)
func_5175 = relay.Function([var_5171,var_5172,var_5173,var_5174,], output)
mutated_mod['func_5175'] = func_5175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4650_call = mod.get_global_var('func_4650')
func_4651_call = mutated_mod.get_global_var('func_4651')
call_5189 = relay.TupleGetItem(func_4650_call(), 1)
call_5190 = relay.TupleGetItem(func_4651_call(), 1)
var_5208 = relay.var("var_5208", dtype = "float32", shape = (12, 6, 10))#candidate|5208|(12, 6, 10)|var|float32
bop_5209 = relay.logical_and(call_5189.astype('bool'), relay.reshape(var_5208.astype('bool'), relay.shape_of(call_5189))) # shape=(12, 6, 10)
bop_5212 = relay.logical_and(call_5190.astype('bool'), relay.reshape(var_5208.astype('bool'), relay.shape_of(call_5190))) # shape=(12, 6, 10)
output = relay.Tuple([bop_5209,])
output2 = relay.Tuple([bop_5212,])
func_5222 = relay.Function([var_5208,], output)
mod['func_5222'] = func_5222
mod = relay.transform.InferType()(mod)
mutated_mod['func_5222'] = func_5222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5223 = relay.var("var_5223", dtype = "float32", shape = (12, 6, 10))#candidate|5223|(12, 6, 10)|var|float32
func_5222_call = mutated_mod.get_global_var('func_5222')
call_5224 = func_5222_call(var_5223)
output = call_5224
func_5225 = relay.Function([var_5223], output)
mutated_mod['func_5225'] = func_5225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_5288 = relay.TupleGetItem(func_2402_call(), 0)
call_5289 = relay.TupleGetItem(func_2404_call(), 0)
func_4858_call = mod.get_global_var('func_4858')
func_4860_call = mutated_mod.get_global_var('func_4860')
call_5290 = relay.TupleGetItem(func_4858_call(relay.reshape(call_5288.astype('float32'), [12, 6, 10])), 4)
call_5291 = relay.TupleGetItem(func_4860_call(relay.reshape(call_5288.astype('float32'), [12, 6, 10])), 4)
output = relay.Tuple([call_5288,call_5290,])
output2 = relay.Tuple([call_5289,call_5291,])
func_5298 = relay.Function([], output)
mod['func_5298'] = func_5298
mod = relay.transform.InferType()(mod)
mutated_mod['func_5298'] = func_5298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5298_call = mutated_mod.get_global_var('func_5298')
call_5299 = func_5298_call()
output = call_5299
func_5300 = relay.Function([], output)
mutated_mod['func_5300'] = func_5300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4169_call = mod.get_global_var('func_4169')
func_4170_call = mutated_mod.get_global_var('func_4170')
call_5506 = relay.TupleGetItem(func_4169_call(), 0)
call_5507 = relay.TupleGetItem(func_4170_call(), 0)
uop_5518 = relay.acosh(call_5506.astype('float32')) # shape=(12, 6, 10)
uop_5520 = relay.acosh(call_5507.astype('float32')) # shape=(12, 6, 10)
func_4982_call = mod.get_global_var('func_4982')
func_4984_call = mutated_mod.get_global_var('func_4984')
call_5526 = relay.TupleGetItem(func_4982_call(), 1)
call_5527 = relay.TupleGetItem(func_4984_call(), 1)
output = relay.Tuple([uop_5518,call_5526,])
output2 = relay.Tuple([uop_5520,call_5527,])
func_5541 = relay.Function([], output)
mod['func_5541'] = func_5541
mod = relay.transform.InferType()(mod)
output = func_5541()
func_5542 = relay.Function([], output)
mutated_mod['func_5542'] = func_5542
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5586 = relay.const([[[-10,-6,5,3,8,6,5],[-9,6,3,6,1,-7,-2],[3,-8,4,-5,1,-10,-3],[-4,-2,3,1,-10,-5,6],[-2,-6,2,9,9,-6,3],[3,4,-4,-10,-6,4,-9],[7,-3,-2,5,5,1,-9],[6,6,-5,7,-9,-8,-8],[-9,3,2,6,-5,9,4]],[[-3,8,-2,-9,5,8,-2],[6,-1,9,-2,10,-5,8],[4,-4,4,8,-6,-5,-2],[-4,-1,6,-7,8,6,-9],[4,4,9,6,-2,9,3],[1,-7,2,5,-4,5,-4],[-1,-1,-10,4,7,-5,6],[8,-8,-5,-2,-6,6,-9],[-1,1,6,8,1,7,2]],[[6,6,5,1,-10,10,-9],[-6,-9,-1,-1,-4,-5,1],[-4,4,8,4,-3,-7,9],[10,6,-8,5,5,8,-6],[-6,-5,-9,10,8,-3,10],[-5,-9,-9,-3,10,-8,-5],[-4,-1,8,-1,-4,6,-5],[-2,-1,4,-4,-5,-1,4],[-9,8,-1,-4,-5,-8,5]],[[1,-3,5,-4,5,3,4],[4,5,-8,-9,-4,-10,7],[7,9,2,-3,-7,-5,4],[2,-1,-7,-2,-1,-5,-3],[1,-10,1,-8,-3,-9,5],[-3,-3,-6,-1,-3,9,-3],[7,1,7,-8,-5,3,-7],[-8,-8,1,6,-8,-2,10],[-2,-10,-1,1,-4,-6,5]],[[-7,-4,7,6,5,-7,8],[3,3,-3,8,-5,3,8],[-8,-1,-7,2,10,2,-7],[-10,10,-3,3,-7,-3,8],[4,5,10,9,-4,-1,-8],[-10,2,1,5,7,1,7],[-6,10,-2,2,-3,-9,-1],[-9,-3,-5,1,9,10,-4],[-9,5,-7,-5,-9,2,9]]], dtype = "uint32")#candidate|5586|(5, 9, 7)|const|uint32
var_5587 = relay.var("var_5587", dtype = "uint32", shape = (5, 9, 7))#candidate|5587|(5, 9, 7)|var|uint32
bop_5588 = relay.logical_xor(const_5586.astype('uint32'), relay.reshape(var_5587.astype('uint32'), relay.shape_of(const_5586))) # shape=(5, 9, 7)
const_5594 = relay.const([[[2,8,-10,5,2,9,4],[-4,6,-2,-10,7,-8,-5],[-8,-9,-2,-6,-9,-2,-5],[-2,-2,-3,-10,-7,-3,-6],[-7,-2,-4,7,-7,-10,6],[-7,3,-1,6,5,-8,-10],[-9,2,9,-10,2,-9,-4],[7,-1,10,-4,10,2,9],[10,-1,-8,-6,4,10,-7]],[[6,7,9,8,1,8,-3],[1,-2,-3,-1,-5,-8,4],[4,-6,-1,6,1,9,7],[5,2,3,-6,-7,7,-5],[1,-4,9,7,-5,1,-6],[-7,-8,4,10,-3,6,-5],[-2,-10,8,-7,-6,-8,-7],[4,-7,-8,-7,6,2,4],[-9,-10,7,-3,-6,3,-7]],[[2,10,-9,10,4,2,5],[-9,-1,-5,-1,-5,-9,-9],[2,3,-9,-1,-2,8,8],[-7,-3,9,-7,6,-9,6],[-1,-2,10,8,-8,2,8],[7,-9,9,1,5,-2,-7],[2,-1,-10,-6,8,-2,3],[-8,3,8,-8,-3,5,-6],[-10,10,-8,-3,-5,7,-4]],[[-2,4,-7,3,-10,-2,-9],[-4,4,10,4,-6,-4,-7],[-4,3,-8,-6,-5,-2,-2],[-1,-3,-8,7,-4,5,1],[3,-10,10,3,-10,5,-7],[-4,3,-10,8,-5,5,9],[9,9,7,9,3,-5,10],[-2,-7,6,2,8,5,7],[5,1,-6,-6,-2,-8,8]],[[1,3,6,10,2,1,1],[5,9,-6,6,3,-4,-8],[1,8,-7,-5,-1,-7,6],[4,6,-9,-1,-7,8,-10],[6,-7,-5,9,5,5,1],[-2,-1,-8,8,-2,-2,-8],[1,-3,6,-4,-4,-5,10],[-9,-1,10,7,-1,-5,6],[3,10,-1,-1,-2,10,-1]]], dtype = "uint32")#candidate|5594|(5, 9, 7)|const|uint32
bop_5595 = relay.bitwise_xor(var_5587.astype('uint8'), relay.reshape(const_5594.astype('uint8'), relay.shape_of(var_5587))) # shape=(5, 9, 7)
bop_5600 = relay.minimum(const_5586.astype('uint16'), relay.reshape(bop_5595.astype('uint16'), relay.shape_of(const_5586))) # shape=(5, 9, 7)
output = relay.Tuple([bop_5588,bop_5600,])
output2 = relay.Tuple([bop_5588,bop_5600,])
func_5603 = relay.Function([var_5587,], output)
mod['func_5603'] = func_5603
mod = relay.transform.InferType()(mod)
mutated_mod['func_5603'] = func_5603
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5604 = relay.var("var_5604", dtype = "uint32", shape = (5, 9, 7))#candidate|5604|(5, 9, 7)|var|uint32
func_5603_call = mutated_mod.get_global_var('func_5603')
call_5605 = func_5603_call(var_5604)
output = call_5605
func_5606 = relay.Function([var_5604], output)
mutated_mod['func_5606'] = func_5606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4905_call = mod.get_global_var('func_4905')
func_4907_call = mutated_mod.get_global_var('func_4907')
call_5656 = relay.TupleGetItem(func_4905_call(), 0)
call_5657 = relay.TupleGetItem(func_4907_call(), 0)
output = call_5656
output2 = call_5657
func_5668 = relay.Function([], output)
mod['func_5668'] = func_5668
mod = relay.transform.InferType()(mod)
output = func_5668()
func_5669 = relay.Function([], output)
mutated_mod['func_5669'] = func_5669
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5686 = relay.var("var_5686", dtype = "bool", shape = (1, 2, 10))#candidate|5686|(1, 2, 10)|var|bool
var_5687 = relay.var("var_5687", dtype = "bool", shape = (10, 2, 10))#candidate|5687|(10, 2, 10)|var|bool
bop_5688 = relay.logical_and(var_5686.astype('bool'), var_5687.astype('bool')) # shape=(10, 2, 10)
func_3867_call = mod.get_global_var('func_3867')
func_3868_call = mutated_mod.get_global_var('func_3868')
call_5692 = relay.TupleGetItem(func_3867_call(), 0)
call_5693 = relay.TupleGetItem(func_3868_call(), 0)
output = relay.Tuple([bop_5688,call_5692,])
output2 = relay.Tuple([bop_5688,call_5693,])
func_5705 = relay.Function([var_5686,var_5687,], output)
mod['func_5705'] = func_5705
mod = relay.transform.InferType()(mod)
mutated_mod['func_5705'] = func_5705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5705_call = mutated_mod.get_global_var('func_5705')
var_5707 = relay.var("var_5707", dtype = "bool", shape = (1, 2, 10))#candidate|5707|(1, 2, 10)|var|bool
var_5708 = relay.var("var_5708", dtype = "bool", shape = (10, 2, 10))#candidate|5708|(10, 2, 10)|var|bool
call_5706 = func_5705_call(var_5707,var_5708,)
output = call_5706
func_5709 = relay.Function([var_5707,var_5708,], output)
mutated_mod['func_5709'] = func_5709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2860_call = mod.get_global_var('func_2860')
func_2862_call = mutated_mod.get_global_var('func_2862')
call_5725 = relay.TupleGetItem(func_2860_call(), 0)
call_5726 = relay.TupleGetItem(func_2862_call(), 0)
output = relay.Tuple([call_5725,])
output2 = relay.Tuple([call_5726,])
func_5727 = relay.Function([], output)
mod['func_5727'] = func_5727
mod = relay.transform.InferType()(mod)
output = func_5727()
func_5728 = relay.Function([], output)
mutated_mod['func_5728'] = func_5728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2883_call = mod.get_global_var('func_2883')
func_2884_call = mutated_mod.get_global_var('func_2884')
call_5805 = relay.TupleGetItem(func_2883_call(), 0)
call_5806 = relay.TupleGetItem(func_2884_call(), 0)
output = call_5805
output2 = call_5806
func_5807 = relay.Function([], output)
mod['func_5807'] = func_5807
mod = relay.transform.InferType()(mod)
output = func_5807()
func_5808 = relay.Function([], output)
mutated_mod['func_5808'] = func_5808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5668_call = mod.get_global_var('func_5668')
func_5669_call = mutated_mod.get_global_var('func_5669')
call_5818 = func_5668_call()
call_5819 = func_5668_call()
output = relay.Tuple([call_5818,])
output2 = relay.Tuple([call_5819,])
func_5830 = relay.Function([], output)
mod['func_5830'] = func_5830
mod = relay.transform.InferType()(mod)
output = func_5830()
func_5831 = relay.Function([], output)
mutated_mod['func_5831'] = func_5831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_5839 = relay.TupleGetItem(func_2168_call(), 0)
call_5840 = relay.TupleGetItem(func_2169_call(), 0)
uop_5841 = relay.log2(call_5839.astype('float64')) # shape=(12, 6, 10)
uop_5843 = relay.log2(call_5840.astype('float64')) # shape=(12, 6, 10)
func_3226_call = mod.get_global_var('func_3226')
func_3230_call = mutated_mod.get_global_var('func_3230')
var_5845 = relay.var("var_5845", dtype = "float32", shape = (1040,))#candidate|5845|(1040,)|var|float32
const_5846 = relay.const([[2.630498,-7.446775,-9.568357,-7.736036,0.506100,-7.820529,-6.585202,1.394999,6.763353,7.916830,-0.726941,3.028101,9.465509,-3.756825,-7.189136,-1.045747,-8.080761,0.817517,7.592070,-8.744537,1.440728,7.043610,-7.827391,-7.923808,0.472875,-2.275902,1.815555,5.582748,5.621702,-2.465882,-1.212695,9.017630,3.670908,6.805102,-8.835485,-4.169048,8.479455,5.760245,-0.114724,6.417545,-4.329075,6.557766,9.234496,-3.483168,0.010581,8.262966,1.692955,-2.986843,6.333727,9.870826,2.549251,-3.932547,9.599798,5.772763,7.790389,8.466097,-0.307259,-6.315877,-5.263467,-7.352977,8.303285,4.860935,-7.777333,-0.054708,1.089927,4.938294,0.474110,0.205388,-0.833313,-2.647942,-1.438859,1.265189,8.396368,-8.842963,-8.339228,5.538377,-8.888601,-6.349482,-3.689267,1.066531,-9.829823,-8.740501,-8.243427,-1.156424,-1.485779,-9.850035,0.044610,-7.013329,7.004816,-5.555069,7.806079,-7.603387,-6.954351,3.468582,6.107355,-2.215414,9.346431,0.450122,5.505697,-9.438032,-2.596600,-2.932730,-1.121786,-6.665691,0.128459,8.787210,-4.899198,1.277234,-0.122358,9.061441,8.442387,2.709190,6.453228,-0.956876,4.736151,-6.206580,7.058779,8.056638,8.279599,-7.685486,-2.021202,-1.036765,3.891110,0.114554,-0.060764,7.657504,-2.297913,-1.367032,6.630728,-7.990925,-0.575656,-5.839138,3.289264,2.470729,-3.520612,-4.094771,-4.719058,6.841202,-7.192836,3.486739,-7.247186,-5.163055,-4.581858,-2.424470,3.637209,-2.477009,2.875264,2.480111,-4.200650,-7.461033,-8.145871,3.164401,6.649292,-1.608984,6.151580,-8.739489,-0.852081,-4.131866,0.041200,-8.680371,-1.935614,-4.507330,-5.408566,-6.275499,0.972736,7.429974,3.124920,-8.160220,6.609358,-6.730737,-1.854181,-2.856246,3.639712,6.131404,6.174193,1.602012,-2.666698,-6.262559,-1.728607,3.161833,2.443088,0.803717,7.059099,5.081317,6.744249,8.012762,-3.833343,-4.680191,1.600266,-4.588505,-7.448204,-8.892346,-4.598334,6.447042,3.894682,-8.304023,5.613149,-3.567937,6.348110,5.890456,5.629016,-4.684234,6.810765,-9.986236,7.506337,9.747428,-2.066479,-2.359232,-3.252632,7.345685,9.723948,-3.267694,-0.918689,9.688098,-8.748437,-3.993631,-8.595787,1.451110,4.168606,-6.534119,2.737391,-6.144313,1.142173,-5.265485,-1.340794,0.233920,5.635561,-1.026098,-8.636773,9.644096,3.446176,5.234429,-2.373508,0.731696,-2.817543,-8.721540,6.115606,8.995764,-5.269703,2.729054,-7.806047,-6.239603,-1.164406,5.537028,-6.174466,-7.282451,-5.530428,7.044658,-7.006211,-7.304878,-9.342785,-7.025828,-0.546001,-2.235492,0.892113,5.049939,3.630711,0.609198,2.262945,-8.610839,6.973223,6.997205,-5.850414,5.654557,8.499696,6.908228,-1.664524,6.383809,-9.758838,7.341798,2.568000,5.792199,-0.284788,1.497337,7.584932,-8.952966,-2.837976,-2.582011,-3.773998,4.621731,8.361683,-4.297875,5.724126,-6.787598,4.264065,6.260386,4.176901,2.179630,-2.292196,8.656258,3.790234,-4.959642,7.419113,-6.496463,-2.467753,0.621688,1.269900,-5.118543,2.935679,-1.431261,-2.703423,-8.492992,-0.850811,-7.664772,-6.492374,-6.379091,6.824141,6.356685,7.855867,-7.261501,4.144200,1.839561,0.058517,0.064262,7.305067,-1.424659,-8.328792,7.653570,-5.266835,6.577556,2.797039,-7.243498,-4.537706,5.009908,-9.638789,-4.859787,8.270465,-3.986087,8.595437,5.756747,3.994485,-2.369288,-5.534806,-6.461081,6.637574,2.371298,5.850536,7.823907,2.846224,0.584025,9.266323,-9.709248,4.326114,4.634920,-5.616253,5.405700,-5.402198,0.636717,6.388440,-7.269251,1.469590,6.086266,6.061607,3.422524,7.453726,-0.940464,-0.520687,5.068351,3.922842,-8.339930,-6.620763,4.493567,7.476171,4.551049,-6.369447,-3.485276,-8.515498,-9.890936,-3.738371,-4.524435,-8.839834,-4.892145,3.900261,4.474057,5.008579,1.374092,3.404614,-6.312618,0.612442,-5.470708,4.205942,-8.299203,-8.247886,-4.676913,-4.075104,7.861720,9.680234,4.053107,6.056348,-6.347620,-6.811914,-3.051396,-8.530053,-7.706687,0.371098,-7.662170,1.253442,-2.866149,0.162004,4.798460,7.814305,5.770135,-1.405388,-1.436562,9.776550,-2.463738,-9.886005,5.174895,-7.950003,-1.997271,-6.010320,-5.167298,8.845391,-0.470811,9.739895,-8.986290,-9.096201,-1.294083,-8.880903,-0.621925,7.074856,4.281660,-3.339268,-9.095419,2.068084,-5.319926,3.940102,7.356147,0.415407,-0.110584,2.037235,6.671653,-3.014694,5.118883,-1.454610,-1.202039,-0.433957,5.551886,-1.471996,4.628559,4.697595,-2.331014,2.563811,7.413503,9.523370,8.709015,7.552725,-5.248201,-0.506172,-3.789548,2.446485,-0.980293,3.381017,-1.332973,-0.614768,6.685184,0.954851,-2.977158,6.262487,3.976448,4.207680,-8.900386,-1.919018,-3.247597,-1.362217,1.737823,5.371539,0.705277,-0.229018,8.076909,-5.963118,-4.319483,-6.158893,-8.643511,-8.383949,-1.799899,-2.746498,-6.843939,1.359000,-7.841080,-2.714196,4.374736,5.451700,-1.774412,2.106480,-3.645917,-1.417071,3.034814,-3.900783,-9.356308,-6.690215,-8.414696,6.259102,0.501557,-5.316179,-8.003362,5.459133,-5.554925,0.026944,-0.790867,-7.996231,-1.168571,7.520058,8.769446,7.809404,9.972873,-0.226522,-7.416582,-9.235369,-8.304678,8.901496,2.799321,2.803528,-9.022940,-3.334644,7.573025,4.316297,7.244429,1.810121,-5.944592,5.121550,-9.575590,-3.368344,5.422211,-6.534719,1.377599,3.279514,7.215773,-7.491419,9.671014,-7.862426,-7.392521,-5.418479,9.362338,-8.675651,-4.173277,8.147016,-2.921268,0.781278,-1.296111,6.484499,-2.309067,5.748762,1.257141,2.967057,-4.034512,3.960175,9.864751,9.684488,-2.531591,1.848555,6.327198,6.081772,-3.854667,8.513955,5.827256,-3.232804,1.433665,3.146297,3.244965,5.458897,-2.829831,-9.355662,-1.149756,-1.193622,-5.165868,0.752648,-1.855980,7.390674,-5.142592,-7.941833,9.986705,9.565091,-6.501168,-6.028257,4.944470,8.464801,-3.791263,3.042120,3.879878,7.961439,7.771503,4.803522,-4.192889,-5.969831,-0.467619,-0.148950,6.803123,-7.429977,-3.917806,-3.165518,9.428676,9.098470,7.319743,-2.055932,9.474947,-5.804816,1.868619,-5.807631,-2.591756,-8.486689,8.090199,8.599315,-6.583728,-4.569825,-9.562052,-1.327050,1.543309,0.978012,-2.940010,0.996085,-5.751922,1.875639,-0.102503,9.714098,-6.416912,5.514914,-4.968926,6.763540,-4.844246,6.297055,-5.478915,-1.147955,6.861655,-4.837605,-0.866933,1.444975,-6.574518,-6.135620,5.757312,8.594088,5.074947,7.541387,5.809424,-4.923744,9.213067,-4.300734,6.882427,0.848690,1.205873,-3.362919,6.511868,-2.610454,-5.074812,-7.518204,-1.727861,-6.310917,-6.810937,1.412421,-4.364904,-6.990524,9.865850,2.475951,6.714699,8.990017,-0.980923,-2.974623,-8.578893,2.229106,0.426263,-4.576243,-1.600764,0.620912,-1.074167,-8.870915,-8.978518,-5.828874,-3.183047,-8.345951,-3.233780,-5.074390,-1.426537,9.160618,2.060371,4.673700,-5.991749,-0.245599,-9.156206,-2.881690,-7.420656,1.240124,6.693880,-0.974537,6.391174,8.080049,-4.447056,9.856722,4.303209,9.792733,9.503680,3.800217,-6.180690,-1.835035,-6.547795,-8.202246,-7.283883,3.215446,8.122488,1.871837,1.214726,8.610086,-8.873088,-3.463746,3.719494,-0.454686,-6.373435,-9.320021,9.944162,-7.924397,9.825694,-2.986472,-1.739807,7.384893,6.068245,8.244173,-9.467857,-0.586469,9.100688,-0.385202,6.989856,0.051942,-5.252300,-6.634350,4.019114,8.617106,1.536489,-0.598192,-4.560763,-5.549483,-9.375468,-7.050983,-6.401295,9.450854,2.544277,-3.332745,-7.800718,-4.670320,0.862740,-6.636960,3.235561,-9.201568,3.875699,7.222094,-1.161583,2.829810,8.939553,4.886965,-7.195913,9.897821,-6.781043,-0.932305,4.735726,-7.586942,-1.687969,1.888183,-0.978801,-4.253481,-3.618713,2.875624,8.966584,3.559368,-2.922341,-1.354011,5.979848,-7.382964,7.048732,-6.977372,-2.219381,-4.448725,5.876127,-0.657133,9.230286,7.798778,-8.324216,-6.596985,9.722866,-0.393081,4.206280,3.902476,-1.875004,-1.445651,-5.254238,9.795697,0.139975,5.228518,5.663258,2.842748,4.608513,2.583833,6.383426,8.834511,9.903413,9.706674,7.386432,-1.462990,-4.027183,2.095382,3.292728,6.235976,-8.446473,-3.244170,7.692536,-8.142414,-7.295632,-2.643287,-4.077125,5.525129,-6.002782,-6.788634,8.323649,5.125683,1.241017,-2.872363,3.402029,-2.634919,5.929211,-4.777302,-1.458803,0.864419,-1.486912,-7.724438,2.930434,-2.041443,-4.195203,2.734076,1.755516,-5.353867,-9.080054,-9.363490,-6.577644,3.974204,7.172958,-0.594958,3.002776,-6.183754,-2.099819,-6.186329,-0.955593,1.460678,6.190209,-7.666427,7.195724,1.618606,-6.780179,-4.567060,-1.728667,-0.781108,6.281090,0.708087,-0.345174,-3.758350,1.274146,-8.084395,3.898178,-3.037585,4.166128,-3.624691,6.985659,-6.284647,8.222609,3.105034,-0.110235,8.281799,-8.454884,-1.553256,-8.824002,6.132047,1.554509,-1.030765,7.199362,6.424686,1.660764,-1.703240,-6.716097,-6.193341,3.650006,5.478466,4.817856,8.582814,-1.122561,-4.631961,-1.971402,-2.380674,-4.799118,-8.233446,0.880030,-9.228757,4.020456,-9.381394,4.624239,5.856800,-6.443358,-8.779830,7.185428,7.983514,-0.823009,1.138428,-7.743616,-1.721600,-0.504203,-1.120323,6.816289,-3.650163,0.040424,-2.906248,-8.404366,8.846938,-9.237250,-6.146556,6.884017,7.455427,-0.309695,-1.552904,-1.117018,7.309323,-7.831435,0.702698,-5.867616,-7.261497,-3.820575,-1.115156,5.543763,9.305776,5.150220,3.172670,8.227437,-9.260734,2.934921,-6.154569,-8.166898,-4.437910,-9.718563,-4.989187,-6.925371,-1.930263,8.271330,4.873549,1.007207,-8.214650,-2.244506,6.442927,8.819276,3.959736,0.200678,-4.897010,3.872941,-2.721625,-3.059328,-6.595548,5.417287,5.615210,7.752714,7.416889,3.689749,-5.318950,-1.675419,-4.139871,6.283026,-2.530885,2.902241,-5.605325,-2.786207,-3.537002,4.609033,2.003976,-7.713948,9.725720,6.556089,-1.069275,1.956169,-8.027789,-1.782858,0.450515,7.817454,-1.414057,-5.663930,6.217827,0.780686,-5.985986,6.930408,-4.067422,-9.932633,4.398292,-8.625464,0.617703,-3.507521,6.779336,-2.646074,2.337786,5.737873,-8.292270,-1.685628,-2.368573,-0.940873,0.884748,-9.838940,1.347322,1.959927,-6.848381,-7.463917,2.860010,1.539335,6.971865,4.085043,0.507540,3.305630,9.731462,-6.256041,2.643550,-6.769252,-9.269811,-6.317464,9.502415,-5.465436,-8.703806,3.992501,-1.651961,-9.603981,-1.842517,-4.134987,-3.921438,-1.299370,7.857200,0.474194,1.220533,1.740988,-9.035139,1.449611,-5.559886,8.530003,-3.942297,-7.602253,-4.086424,-5.066017,1.497635,-4.138125,-6.712306,9.651664,1.889742,8.776307,-2.462093,-8.071098,-3.351398,-5.643265,-7.810573,4.959014,4.736964,9.939008,2.987243,-8.358312,-1.357650,-7.737698,4.533278,-0.439853,4.186879,8.897415,7.896384,-6.937724,5.401159,-7.851847,1.588838,-8.400350,6.971299,-8.442174,-0.334493,5.293289,9.228427,4.938156,8.325670,-1.017146,1.099539,-0.921913,0.368687,0.506817,-7.080617,-0.207032,1.710285,-1.845600,-1.920108,3.561419,5.210560,8.648998,2.746811,-8.284193,8.255982,3.648620,-4.341723,1.967222,-4.204310,3.380491,-0.780434,-6.120078,-0.635135,-8.743194,6.928013,4.788327,0.234955,-6.672637,-8.781731,5.586125,5.531329,-1.925384,9.864866,3.173167,-0.563173,-6.383800,3.751137,8.778024,4.726866,-2.597528,6.706326,6.200054,0.135989,4.871834,-5.726033,2.841827,4.655366,-9.462613,1.396882,7.703324,-2.732249,-2.145841,-8.536219,0.072213,6.146992,3.077843,-6.102728,7.420362,-6.795841,4.154215,-0.243708,-3.081072,-8.830537,-8.897601,-6.557954,-5.281276,5.751747,-5.613485,-8.136793,2.844745,-2.237534,-7.798756,9.693343,-9.514059,1.253152,3.348386,-3.460001,0.840956,-8.426887,-7.509614,0.248766,4.756228]], dtype = "float32")#candidate|5846|(1, 1152)|const|float32
call_5844 = relay.TupleGetItem(func_3226_call(relay.reshape(var_5845.astype('float32'), [13, 10, 8]), relay.reshape(const_5846.astype('float32'), [1152,]), ), 6)
call_5847 = relay.TupleGetItem(func_3230_call(relay.reshape(var_5845.astype('float32'), [13, 10, 8]), relay.reshape(const_5846.astype('float32'), [1152,]), ), 6)
bop_5850 = relay.less(call_5839.astype('bool'), relay.reshape(uop_5841.astype('bool'), relay.shape_of(call_5839))) # shape=(12, 6, 10)
bop_5853 = relay.less(call_5840.astype('bool'), relay.reshape(uop_5843.astype('bool'), relay.shape_of(call_5840))) # shape=(12, 6, 10)
func_5668_call = mod.get_global_var('func_5668')
func_5669_call = mutated_mod.get_global_var('func_5669')
call_5857 = func_5668_call()
call_5858 = func_5668_call()
func_3595_call = mod.get_global_var('func_3595')
func_3599_call = mutated_mod.get_global_var('func_3599')
const_5877 = relay.const([[-9.134712,7.391606,-2.272363,6.449060,-3.614307,-3.095491,-2.380353,-8.675185,9.194299,-8.803826,7.215945,3.097455,6.670688],[9.671998,0.302085,-8.685304,-7.156682,3.352936,4.962192,5.471603,-1.814569,-2.347968,-7.147833,-3.602284,0.630068,3.093648],[3.524362,9.763610,6.776740,5.048658,9.590643,-3.087949,0.068343,-5.113628,-3.195265,-5.092694,4.938931,9.291723,9.444266],[9.280332,-4.414786,1.792789,3.014173,2.390239,6.527025,4.011498,-6.821652,6.339067,-8.211075,-5.367068,3.318271,3.608128],[8.550468,4.897382,-6.093386,-5.361043,3.725692,3.973681,-1.574428,-8.806886,0.588383,-9.124168,5.009494,0.066330,2.113511],[9.859048,-8.137259,6.919553,3.890602,-7.425657,4.842395,1.018709,5.042481,4.479863,3.829290,9.784381,-8.756449,-3.187583],[7.766005,7.826879,5.229633,-1.882315,5.849558,-2.725554,-9.419875,-6.673140,8.015539,-7.585349,-6.090160,-6.995046,5.225767],[-4.515178,2.460490,-7.339235,-7.011909,8.745675,-6.245448,3.744601,4.697966,-8.437809,1.083834,0.523421,-5.856403,4.562912],[7.402212,-3.739571,2.432012,-7.697554,6.259650,-2.142480,-7.825493,-8.619808,8.656067,-9.388453,8.267117,-5.037230,-2.453310],[4.435582,4.756647,8.616149,-9.780044,-8.239151,1.264488,-3.841456,6.833496,-2.007759,-4.226247,-9.874332,6.880644,-2.026844],[9.764849,7.439743,-0.240516,8.073820,5.997892,-4.397072,-9.408752,7.129572,-5.860483,3.242041,-0.319991,9.629407,-7.072452],[-2.057821,7.666542,-8.416105,0.024719,-1.667381,-1.882775,-8.268207,-1.714707,1.929173,6.258501,-4.576445,-7.110121,1.646051],[-1.809461,8.919962,-2.071925,-4.594136,-5.721339,-0.966478,-8.952509,9.984977,-2.337026,-3.551335,-1.512085,-2.434645,-3.163099],[8.490051,-4.065318,-2.457654,-1.890997,0.806652,1.212762,-8.483114,-5.028307,-6.636501,7.181038,2.754218,6.983773,-8.755153],[0.399300,8.660046,-9.465471,-9.483540,2.077627,7.820105,-9.740021,-8.317091,-4.850374,5.624725,8.646630,1.123914,9.225359],[3.961777,-4.786982,-6.843995,-3.845696,4.626285,7.612200,9.350457,-2.685110,-8.497977,6.453244,0.899320,8.757560,-6.479901],[-0.467615,9.051234,-4.761625,-2.324047,-3.487392,-1.408654,-9.491956,9.780580,9.058435,-4.491690,3.495757,-3.848353,7.456282],[-6.470591,-7.773806,5.348634,-2.109243,-2.879371,3.223118,9.882670,9.098251,-5.870131,-9.159847,1.917535,-0.497965,6.017222],[-4.819679,-3.365091,6.557944,-0.816501,0.782270,-7.139994,-6.457438,-6.225919,3.817602,-4.297213,2.416004,-2.729313,-4.915643],[4.164263,0.079592,8.421214,-9.955274,6.319260,-6.207162,9.855508,-3.927651,-4.933985,-8.590458,-0.051986,-1.059372,6.548033],[-3.589548,3.304218,0.599239,2.471630,-5.039218,7.724828,9.190057,-4.921776,-7.713557,8.069080,-8.469082,-7.614051,0.419122],[-2.046696,2.460930,6.026620,-5.884466,-5.670675,-7.960142,-5.781294,-2.904111,2.066201,6.942675,-9.396270,-5.769331,-1.340340],[7.799616,3.918535,7.189076,-2.268559,9.634785,-0.987462,4.743888,-2.294756,7.586579,-2.758281,-3.124228,7.222830,9.213999],[1.408786,0.464419,-8.534487,-1.659893,5.119551,-4.184153,-8.005253,-6.345368,3.234731,-3.618266,0.987116,-3.977716,5.615707],[4.608093,-9.834670,-1.502036,-3.539916,3.380192,-0.716668,2.055141,-0.186786,-6.634611,3.948346,9.208105,-0.197525,-9.221728],[9.505856,5.738972,6.242225,4.118352,1.864995,-5.717926,-0.647647,4.722838,0.509146,-7.113398,-7.779869,1.857022,2.141517],[-6.216168,-4.064806,2.003477,5.289669,-3.926412,-3.984135,5.421596,-5.039273,3.894174,6.116459,6.191132,1.230615,-4.793894],[-6.618397,-9.012072,7.834264,7.881839,9.169392,0.970026,9.922690,-2.595716,-7.087740,-5.876755,5.302835,8.625733,-8.689945],[6.887392,-3.270170,9.753577,8.831274,2.738921,-0.150024,-4.244724,1.660023,-1.240230,-4.479406,-9.635377,-3.273080,4.806192],[7.970923,7.942485,4.448974,5.604728,-3.786592,1.214247,-4.955832,-2.233977,6.731556,0.272831,7.145273,-1.562903,-4.685855],[-2.605933,3.388785,-4.361677,-2.085841,-3.766845,-9.396849,2.056556,-3.286512,6.100016,5.395152,5.133665,-3.644498,-4.384288],[-5.236725,8.467251,1.248132,-7.875612,7.908072,6.247366,-5.596006,-3.451503,-5.100317,0.823848,-5.492178,0.982300,2.086522],[-4.499749,9.163612,0.905420,9.409962,-3.498778,-9.362807,8.184198,4.575782,9.841533,-7.012824,8.667952,4.446237,7.168191],[8.594550,-6.560738,6.742256,-0.323537,9.175361,6.336159,6.537313,8.079796,-7.735807,0.140079,-2.442386,4.809281,-1.549804],[6.282040,9.047022,8.347823,1.807003,5.679302,2.765675,-5.509722,5.816557,8.430533,3.447722,-0.835279,-5.059884,-4.786640],[-6.689138,9.338183,-2.472208,7.995809,-4.268630,-3.789208,-4.473123,-0.661142,9.548515,-3.949758,-5.718750,0.308340,-8.234175],[5.542385,-4.884608,4.958377,6.894947,4.808194,2.518672,-4.103136,-3.561083,-2.452852,-4.624331,-2.380665,3.020932,9.447773],[-8.377215,6.582736,-1.915741,6.975799,-6.207446,-1.087480,-2.681923,3.823634,-7.397856,4.240307,-9.228409,4.219707,-4.335931],[3.785358,-2.503693,-5.007787,9.661322,2.293960,-6.492876,-5.975280,-4.991870,1.818876,7.454475,-9.060588,-5.439177,-5.589698],[0.488403,3.106436,6.684724,2.210394,1.093517,-4.793033,-1.701662,2.303664,1.667729,7.108236,-6.604204,-5.773700,-4.132247],[8.033263,-4.282095,3.668525,3.273985,4.033590,7.602368,-0.788306,-6.194067,-2.806538,-6.294396,-8.075069,1.258983,6.818278],[-2.708214,0.362763,5.361485,5.031095,-1.969498,9.531974,5.860402,-2.107889,-5.809566,-9.480593,-0.952751,5.170782,-9.151402],[-5.110135,9.476101,4.604730,0.554274,-6.317411,7.246760,-2.244379,8.794246,2.897728,-1.126014,0.120629,-8.217521,-6.918853],[-2.299915,4.884457,2.020736,5.743631,-2.906957,-0.819676,8.808255,-8.440575,-2.519122,8.447259,-7.163357,-5.943908,-8.301279],[3.904046,2.945583,1.462149,8.410181,-2.986709,-2.146749,-5.788811,-9.784837,-5.285540,0.930892,-9.719895,1.774781,2.872398],[-3.944504,4.515482,-0.109984,3.029007,-1.341520,7.508952,-5.535400,-3.173404,3.759717,7.201959,1.575813,-5.921987,-7.133832],[-3.103598,-2.184160,5.688524,7.542795,6.685931,-9.899897,-4.321708,-0.092470,-0.911405,8.265110,9.267282,6.342856,6.293585],[2.982814,-0.958420,-1.539985,8.360097,-1.756008,-5.622301,8.869481,8.753529,-6.421656,-4.547686,-1.037997,3.119157,6.835338],[-2.714596,7.582070,3.004814,7.135760,-8.140288,-8.032808,-8.685461,5.419944,3.329056,4.113099,-7.164812,-5.879040,-6.052987],[7.458524,-7.259192,-8.928679,-9.957829,-8.924250,-1.008481,0.087587,-2.588978,6.042930,-6.523956,2.835492,7.548986,6.162317],[-2.559171,1.655357,-2.823286,0.492308,1.217996,2.091276,8.548066,-5.287058,-3.321498,8.791707,6.443683,6.757796,2.445752],[5.902726,3.830029,-9.296308,-3.359367,-2.308492,-7.957970,-8.462473,-8.756783,1.122747,0.020647,8.027689,8.787305,-6.376386],[9.062340,5.737678,-9.741001,-4.645312,0.869836,-8.323312,-3.499716,-4.864139,-0.758259,-3.030264,-0.980513,-3.134254,0.761517],[3.141299,-5.366260,-7.198340,-8.543821,-2.558775,-0.407764,-4.594723,4.680551,-9.180555,-6.566789,7.482461,5.140244,1.672996],[3.760372,1.889479,6.285465,-4.712667,3.135753,-0.501307,-2.155826,-0.117697,4.577670,-6.346788,9.122254,-2.307368,9.715522],[-9.541269,9.219611,-7.273446,-6.683553,-9.293817,2.107414,8.306751,1.128783,-7.060036,3.070972,-1.990014,3.079511,5.527079],[4.242701,-2.589027,2.788283,2.089761,-1.580096,-9.204173,-8.480302,5.653305,9.457159,-0.018766,-3.595090,-7.444641,2.776020],[-7.577169,9.952404,-8.223228,8.861665,0.032318,7.825384,8.965484,-0.732997,-2.610251,-8.989312,-5.898167,2.269296,-0.127946],[0.387070,0.047050,-8.400141,-0.173833,9.568115,-5.579067,0.726345,-2.865727,2.174790,9.577422,5.428578,-7.745313,8.712054],[4.268768,5.363272,-7.977422,-7.965442,4.653809,6.553795,-4.670097,-1.024798,5.017738,-3.592596,8.846725,1.253409,4.964471],[-5.734492,6.393186,3.891602,-2.664635,-9.854541,6.737933,-0.555801,7.295960,-9.688027,5.923108,0.054499,9.090004,-7.441915],[1.028241,2.542734,-5.480053,-7.239095,2.187489,-3.218122,-6.550001,-7.226194,1.476860,-0.396792,-9.182907,-2.246978,-6.131023],[-3.637688,5.438595,-2.155590,-0.070674,7.856451,9.691148,-1.483774,4.792276,6.626021,-9.374792,-6.703915,-3.628506,-9.989416],[6.100804,-2.532424,-4.084138,7.276244,8.024144,-3.002326,4.921650,-0.413528,4.558026,2.403324,3.828898,-4.455984,-4.882699],[3.390519,-5.743538,3.277920,-4.291819,8.923972,-3.160225,-8.540436,-6.572944,-5.708615,6.473579,-1.394456,6.709859,2.490424]], dtype = "float64")#candidate|5877|(65, 13)|const|float64
call_5876 = relay.TupleGetItem(func_3595_call(relay.reshape(const_5877.astype('float64'), [13, 5, 13]), relay.reshape(call_5844.astype('uint16'), [180,]), ), 3)
call_5878 = relay.TupleGetItem(func_3599_call(relay.reshape(const_5877.astype('float64'), [13, 5, 13]), relay.reshape(call_5844.astype('uint16'), [180,]), ), 3)
func_3427_call = mod.get_global_var('func_3427')
func_3430_call = mutated_mod.get_global_var('func_3430')
call_5901 = relay.TupleGetItem(func_3427_call(relay.reshape(call_5876.astype('uint16'), [180,])), 1)
call_5902 = relay.TupleGetItem(func_3430_call(relay.reshape(call_5876.astype('uint16'), [180,])), 1)
func_3595_call = mod.get_global_var('func_3595')
func_3599_call = mutated_mod.get_global_var('func_3599')
call_5903 = relay.TupleGetItem(func_3595_call(relay.reshape(const_5877.astype('float64'), [13, 5, 13]), relay.reshape(call_5901.astype('uint16'), [180,]), ), 3)
call_5904 = relay.TupleGetItem(func_3599_call(relay.reshape(const_5877.astype('float64'), [13, 5, 13]), relay.reshape(call_5901.astype('uint16'), [180,]), ), 3)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_5907 = relay.TupleGetItem(func_2168_call(), 0)
call_5908 = relay.TupleGetItem(func_2169_call(), 0)
func_2263_call = mod.get_global_var('func_2263')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_5943 = relay.TupleGetItem(func_2263_call(relay.reshape(call_5903.astype('uint16'), [180,])), 1)
call_5944 = relay.TupleGetItem(func_2266_call(relay.reshape(call_5903.astype('uint16'), [180,])), 1)
func_4982_call = mod.get_global_var('func_4982')
func_4984_call = mutated_mod.get_global_var('func_4984')
call_5953 = relay.TupleGetItem(func_4982_call(), 0)
call_5954 = relay.TupleGetItem(func_4984_call(), 0)
output = relay.Tuple([call_5844,var_5845,const_5846,bop_5850,call_5857,call_5876,const_5877,call_5901,call_5903,call_5907,call_5943,call_5953,])
output2 = relay.Tuple([call_5847,var_5845,const_5846,bop_5853,call_5858,call_5878,const_5877,call_5902,call_5904,call_5908,call_5944,call_5954,])
func_5960 = relay.Function([var_5845,], output)
mod['func_5960'] = func_5960
mod = relay.transform.InferType()(mod)
var_5961 = relay.var("var_5961", dtype = "float32", shape = (1040,))#candidate|5961|(1040,)|var|float32
output = func_5960(var_5961)
func_5962 = relay.Function([var_5961], output)
mutated_mod['func_5962'] = func_5962
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5964 = relay.const([[[7,-3],[-4,4],[-8,5],[-10,-8],[5,-10],[-5,7],[6,-4],[3,4],[5,4],[-6,5],[7,6],[8,-2],[3,-1]],[[8,2],[7,-6],[-5,2],[-8,1],[5,2],[7,1],[1,-6],[7,7],[-7,-9],[6,-5],[-8,10],[1,3],[-9,-10]],[[-2,10],[6,10],[-5,-9],[5,-5],[5,-9],[-6,10],[2,7],[-8,-8],[10,4],[5,-1],[10,-3],[10,-5],[9,-8]],[[6,-6],[3,10],[10,10],[5,10],[-7,-10],[-1,-3],[10,-5],[-5,-4],[3,9],[-3,7],[-6,-5],[-10,-1],[-6,-5]],[[2,7],[7,1],[-7,3],[6,7],[-1,-5],[1,8],[-5,-10],[9,-7],[5,-5],[7,4],[-2,5],[-9,9],[7,6]],[[4,-1],[2,9],[7,2],[-1,4],[-4,2],[-7,6],[-9,7],[9,-6],[-7,1],[8,-1],[-7,7],[-2,5],[-3,-2]],[[4,-8],[4,-1],[-9,5],[3,5],[7,6],[-9,-3],[-6,-4],[7,-1],[5,4],[-7,10],[1,1],[-3,-7],[10,-6]],[[6,7],[10,-3],[9,-8],[5,2],[6,-7],[-1,-2],[5,-7],[-3,-4],[-6,3],[6,3],[-1,-10],[2,6],[7,-6]],[[2,-3],[7,1],[-4,-1],[8,6],[-1,9],[-1,-6],[-2,2],[6,6],[-8,-4],[-10,7],[10,6],[-3,3],[-5,-5]]], dtype = "int16")#candidate|5964|(9, 13, 2)|const|int16
var_5965 = relay.var("var_5965", dtype = "int16", shape = (9, 13, 2))#candidate|5965|(9, 13, 2)|var|int16
bop_5966 = relay.bitwise_xor(const_5964.astype('int16'), relay.reshape(var_5965.astype('int16'), relay.shape_of(const_5964))) # shape=(9, 13, 2)
const_5988 = relay.const([[[-9,-10],[-7,6],[-9,-10],[-1,-2],[-2,-10],[-4,2],[10,-5],[-1,-8],[-9,-5],[-9,2],[7,-6],[2,1],[-6,-8]],[[5,-8],[-7,-7],[3,3],[6,-10],[8,2],[5,-6],[-9,2],[5,-8],[10,-5],[-8,-9],[8,4],[-9,8],[8,3]],[[-9,2],[-3,3],[-4,10],[6,3],[6,4],[-4,-7],[-5,-10],[-4,-8],[-9,10],[5,-2],[4,-3],[7,-4],[-9,-8]],[[-9,6],[9,-10],[-9,9],[9,10],[3,-2],[-3,-7],[2,3],[2,-6],[6,8],[10,-10],[6,-6],[9,6],[-7,-10]],[[3,9],[1,-9],[-3,5],[-7,-5],[-8,-5],[-6,-9],[7,8],[-4,-2],[-10,-6],[-5,5],[10,-7],[10,5],[9,-4]],[[10,-2],[9,-1],[-2,3],[6,-4],[-4,8],[8,10],[-9,8],[6,-5],[-5,5],[8,-8],[9,-2],[-9,-5],[-3,7]],[[-10,1],[-4,7],[3,8],[10,-4],[7,7],[-1,2],[-5,-5],[10,2],[-10,1],[-4,-4],[2,-4],[5,-9],[10,-10]],[[-6,3],[9,-10],[9,-1],[6,3],[-10,-4],[-10,5],[8,8],[1,-1],[10,8],[1,8],[-1,8],[-9,-5],[7,1]],[[10,1],[-9,8],[-8,-7],[-2,-6],[3,2],[3,9],[-1,4],[6,5],[1,-5],[-6,-2],[-1,-3],[-4,-7],[-4,-10]]], dtype = "int16")#candidate|5988|(9, 13, 2)|const|int16
bop_5989 = relay.logical_or(bop_5966.astype('bool'), relay.reshape(const_5988.astype('bool'), relay.shape_of(bop_5966))) # shape=(9, 13, 2)
func_3258_call = mod.get_global_var('func_3258')
func_3261_call = mutated_mod.get_global_var('func_3261')
var_6009 = relay.var("var_6009", dtype = "float32", shape = (24, 48))#candidate|6009|(24, 48)|var|float32
call_6008 = relay.TupleGetItem(func_3258_call(relay.reshape(var_6009.astype('float32'), [1152,])), 5)
call_6010 = relay.TupleGetItem(func_3261_call(relay.reshape(var_6009.astype('float32'), [1152,])), 5)
func_4186_call = mod.get_global_var('func_4186')
func_4188_call = mutated_mod.get_global_var('func_4188')
call_6016 = relay.TupleGetItem(func_4186_call(), 0)
call_6017 = relay.TupleGetItem(func_4188_call(), 0)
uop_6041 = relay.acosh(const_5988.astype('float32')) # shape=(9, 13, 2)
output = relay.Tuple([bop_5989,call_6008,var_6009,call_6016,uop_6041,])
output2 = relay.Tuple([bop_5989,call_6010,var_6009,call_6017,uop_6041,])
func_6047 = relay.Function([var_5965,var_6009,], output)
mod['func_6047'] = func_6047
mod = relay.transform.InferType()(mod)
var_6048 = relay.var("var_6048", dtype = "int16", shape = (9, 13, 2))#candidate|6048|(9, 13, 2)|var|int16
var_6049 = relay.var("var_6049", dtype = "float32", shape = (24, 48))#candidate|6049|(24, 48)|var|float32
output = func_6047(var_6048,var_6049,)
func_6050 = relay.Function([var_6048,var_6049,], output)
mutated_mod['func_6050'] = func_6050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3561_call = mod.get_global_var('func_3561')
func_3562_call = mutated_mod.get_global_var('func_3562')
call_6057 = func_3561_call()
call_6058 = func_3561_call()
output = relay.Tuple([call_6057,])
output2 = relay.Tuple([call_6058,])
func_6068 = relay.Function([], output)
mod['func_6068'] = func_6068
mod = relay.transform.InferType()(mod)
output = func_6068()
func_6069 = relay.Function([], output)
mutated_mod['func_6069'] = func_6069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_6070 = func_2502_call()
call_6071 = func_2502_call()
func_5830_call = mod.get_global_var('func_5830')
func_5831_call = mutated_mod.get_global_var('func_5831')
call_6077 = relay.TupleGetItem(func_5830_call(), 0)
call_6078 = relay.TupleGetItem(func_5831_call(), 0)
func_3867_call = mod.get_global_var('func_3867')
func_3868_call = mutated_mod.get_global_var('func_3868')
call_6085 = relay.TupleGetItem(func_3867_call(), 0)
call_6086 = relay.TupleGetItem(func_3868_call(), 0)
func_5705_call = mod.get_global_var('func_5705')
func_5709_call = mutated_mod.get_global_var('func_5709')
const_6093 = relay.const([False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False], dtype = "bool")#candidate|6093|(20,)|const|bool
const_6094 = relay.const([[True,True,True,False],[False,False,False,True],[False,True,True,True],[False,False,False,False],[False,True,False,True],[False,False,True,False],[True,False,False,True],[True,True,True,False],[False,False,True,True],[False,True,False,False],[True,True,True,True],[True,True,True,True],[True,True,True,True],[True,False,True,True],[False,False,False,True],[True,True,False,False],[True,True,True,True],[False,True,True,True],[False,True,False,False],[False,False,True,True],[True,False,False,True],[False,False,False,True],[False,False,False,True],[False,False,True,True],[True,False,True,False],[True,False,True,False],[True,False,False,False],[False,True,True,True],[False,False,False,False],[False,False,True,False],[True,False,True,True],[False,True,False,False],[True,True,False,True],[False,True,True,True],[True,True,True,True],[False,True,True,False],[True,True,True,True],[False,False,True,True],[False,False,False,True],[True,False,True,True],[False,True,False,False],[False,True,True,False],[False,True,True,False],[False,False,True,True],[False,False,False,False],[False,True,True,True],[True,True,False,True],[True,True,False,True],[False,False,True,False],[True,True,False,True]], dtype = "bool")#candidate|6094|(50, 4)|const|bool
call_6092 = relay.TupleGetItem(func_5705_call(relay.reshape(const_6093.astype('bool'), [1, 2, 10]), relay.reshape(const_6094.astype('bool'), [10, 2, 10]), ), 1)
call_6095 = relay.TupleGetItem(func_5709_call(relay.reshape(const_6093.astype('bool'), [1, 2, 10]), relay.reshape(const_6094.astype('bool'), [10, 2, 10]), ), 1)
func_4169_call = mod.get_global_var('func_4169')
func_4170_call = mutated_mod.get_global_var('func_4170')
call_6100 = relay.TupleGetItem(func_4169_call(), 0)
call_6101 = relay.TupleGetItem(func_4170_call(), 0)
uop_6105 = relay.atan(call_6077.astype('float64')) # shape=(12, 6, 10)
uop_6107 = relay.atan(call_6078.astype('float64')) # shape=(12, 6, 10)
func_4982_call = mod.get_global_var('func_4982')
func_4984_call = mutated_mod.get_global_var('func_4984')
call_6128 = relay.TupleGetItem(func_4982_call(), 0)
call_6129 = relay.TupleGetItem(func_4984_call(), 0)
output = relay.Tuple([call_6070,call_6085,call_6092,const_6093,const_6094,call_6100,uop_6105,call_6128,])
output2 = relay.Tuple([call_6071,call_6086,call_6095,const_6093,const_6094,call_6101,uop_6107,call_6129,])
func_6158 = relay.Function([], output)
mod['func_6158'] = func_6158
mod = relay.transform.InferType()(mod)
output = func_6158()
func_6159 = relay.Function([], output)
mutated_mod['func_6159'] = func_6159
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6171 = relay.var("var_6171", dtype = "int8", shape = (3, 14, 2))#candidate|6171|(3, 14, 2)|var|int8
var_6172 = relay.var("var_6172", dtype = "int8", shape = (3, 14, 2))#candidate|6172|(3, 14, 2)|var|int8
bop_6173 = relay.multiply(var_6171.astype('int8'), relay.reshape(var_6172.astype('int8'), relay.shape_of(var_6171))) # shape=(3, 14, 2)
func_3095_call = mod.get_global_var('func_3095')
func_3098_call = mutated_mod.get_global_var('func_3098')
const_6188 = relay.const([9,7,9,4,-1,-5,-7,-10,-10,-3,7,-6,4,-9,10,6,-5,-9,-6,2,-1,-4,1,7,6,-4,6,1,-1,6,4,1,7,-4,2,2,5,2,-7,7,-1,-8,10,8,10,3,8,-5,-3,-7,5,8,5,-5,-1,8,5,10,5,-7,3,-3,5,5,-5,4,-4,-9,4,-1,-8,8,5,9,7,-9,7,1,-9,9,-1,-3,7,3,-8,8,-3,7,8,10,-1,6,-2,-9,3,7,5,8,6,3,4,-7,-2,7,-2,5,-9,-3,-8,-3,4,-5,-4,1,4,1,7,-7,6,-1,2,-4,-7,-1,1,7,6,4,-3,-7,9,5,7,7,5,-2,3,7,10,8,3,-9,-5,8,-8,-7,2,4,-5,3,-8,8,-8,5,2,-3,7,4,5,-2,-7,-1,-10,-8,-6,6,5,-5,-6,3,4,-4,8,-2,10,-7,2,7,10,6], dtype = "uint16")#candidate|6188|(180,)|const|uint16
call_6187 = relay.TupleGetItem(func_3095_call(relay.reshape(const_6188.astype('uint16'), [180,])), 2)
call_6189 = relay.TupleGetItem(func_3098_call(relay.reshape(const_6188.astype('uint16'), [180,])), 2)
output = relay.Tuple([bop_6173,call_6187,const_6188,])
output2 = relay.Tuple([bop_6173,call_6189,const_6188,])
func_6198 = relay.Function([var_6171,var_6172,], output)
mod['func_6198'] = func_6198
mod = relay.transform.InferType()(mod)
var_6199 = relay.var("var_6199", dtype = "int8", shape = (3, 14, 2))#candidate|6199|(3, 14, 2)|var|int8
var_6200 = relay.var("var_6200", dtype = "int8", shape = (3, 14, 2))#candidate|6200|(3, 14, 2)|var|int8
output = func_6198(var_6199,var_6200,)
func_6201 = relay.Function([var_6199,var_6200,], output)
mutated_mod['func_6201'] = func_6201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_6239 = relay.TupleGetItem(func_2625_call(), 1)
call_6240 = relay.TupleGetItem(func_2626_call(), 1)
func_6047_call = mod.get_global_var('func_6047')
func_6050_call = mutated_mod.get_global_var('func_6050')
var_6253 = relay.var("var_6253", dtype = "int16", shape = (234,))#candidate|6253|(234,)|var|int16
const_6254 = relay.const([[5.885080,0.735183],[0.715324,0.881084],[-9.964113,-8.712783],[-5.732623,7.042510],[7.772756,7.158922],[-5.827500,3.584402],[8.170781,-1.429550],[-3.789143,-8.607529],[-2.717726,2.841014],[-7.922560,0.418527],[-3.150649,4.077166],[-1.605757,2.608213],[2.530454,-3.510284],[-6.418009,-4.646654],[-3.827884,-3.655077],[-0.929120,-5.601247],[-2.580400,-1.677371],[-1.101678,7.444394],[3.240495,8.883385],[3.055741,-8.673578],[4.143528,0.672577],[-5.909998,-4.500784],[-9.248828,-0.135330],[1.862676,2.808501],[-2.538521,-2.021538],[-2.084272,6.001028],[-3.744188,9.586811],[2.519849,2.979722],[-6.733382,-5.122738],[-6.313766,0.519299],[9.197903,2.937875],[-1.986381,-6.043008],[-8.586478,-8.027631],[-2.760342,5.693056],[-0.048113,4.224249],[-0.782342,8.030749],[1.740387,3.065116],[-8.245489,-9.044439],[-9.491803,-1.771550],[0.299387,6.418222],[-4.495681,-9.230707],[9.729421,1.129979],[-7.658593,4.632684],[7.075330,-9.578068],[8.349354,-4.627151],[-2.780085,6.607596],[-8.859872,-5.266829],[6.618519,-3.348137],[2.367426,-0.119456],[-3.023537,-0.162541],[-7.794901,5.690127],[-1.183032,-9.095025],[3.474036,6.161721],[-3.255870,3.531359],[1.360014,-1.765650],[4.062013,-9.749438],[4.542205,-8.268822],[-6.766190,-6.168121],[-8.385993,6.472961],[9.597343,-7.111173],[-6.676040,3.945111],[6.702113,-9.582644],[-2.331457,2.454124],[3.110702,-7.317912],[-7.066996,-0.696939],[5.051286,-7.049675],[-6.311061,3.983885],[5.239463,-6.548557],[9.664380,-4.302164],[-1.502253,7.130282],[0.205973,9.160564],[-3.862000,5.849411],[-2.465733,-0.307149],[5.823337,6.469231],[-3.084630,0.342481],[3.004432,2.179825],[2.535942,1.616126],[-3.393306,-9.060462],[3.355314,-6.027310],[6.302948,-0.992208],[1.724083,-7.968892],[0.855422,-0.757873],[-8.301301,-7.736927],[-5.794809,-5.641992],[1.043435,7.702149],[5.781468,-4.308733],[6.064334,-3.161107],[-4.140701,-1.166890],[4.083748,-5.017862],[9.337361,-0.737101],[7.572514,2.563777],[0.147693,4.879632],[0.985640,-1.301583],[6.359341,8.963545],[-8.829289,9.415703],[-3.261981,-0.420091],[-9.630418,9.433024],[-3.908557,2.584890],[-3.529444,5.829457],[2.199192,-5.148240],[7.209541,7.678042],[7.937852,-2.272243],[-3.192462,7.040251],[0.748818,4.862839],[-8.000984,7.215712],[-8.314898,-1.050192],[2.447044,-7.145595],[4.894753,7.045640],[-3.591690,8.209899],[4.077601,3.301115],[0.158385,7.650072],[-5.547756,0.101552],[9.946724,4.749999],[0.101976,-3.436536],[0.473790,7.736763],[3.798938,-5.129575],[3.270802,-6.536888],[7.796356,4.000950],[-4.462935,3.385871],[4.036359,2.841758],[-7.579053,-0.671736],[2.325405,-5.574732],[-6.954722,3.034131],[8.375194,0.721756],[6.225390,7.063916],[6.424896,1.035799],[0.110693,-2.719906],[3.075741,0.765589],[0.723254,-5.148719],[-2.709593,2.605532],[-8.624471,4.428056],[-2.477679,2.829985],[-2.490895,-3.642096],[9.547922,5.795280],[2.445267,2.682863],[2.641614,-4.739254],[-5.695462,4.958611],[9.760970,9.261071],[4.966057,4.977452],[0.765551,2.690579],[-6.711075,2.266077],[-1.877819,-3.018724],[6.944553,-3.490168],[2.198354,2.470275],[6.738059,-0.079868],[5.794851,5.003919],[-7.949399,0.563177],[1.980892,5.264917],[-2.493961,1.573919],[0.201435,-8.173894],[1.290789,-6.630197],[3.457246,-3.990968],[-9.832509,-4.153863],[6.971456,6.155548],[-7.094863,3.026815],[0.418630,4.941899],[-0.035055,-2.320707],[3.831451,-0.903065],[-5.208284,9.720975],[-0.513557,-3.823596],[-3.701533,-2.477851],[-1.602332,-4.825769],[-5.730393,-1.172853],[-6.190712,-5.051488],[-2.205404,2.793576],[6.877712,-4.251998],[-0.508612,-4.043853],[-7.239399,7.506580],[7.069880,-7.393675],[8.048114,-5.912082],[-1.574927,-1.640684],[3.113672,8.703350],[3.267701,9.374893],[-8.524188,-0.938246],[4.943905,9.774531],[-5.556612,-5.171080],[3.327543,8.453816],[3.080466,-2.316958],[7.148517,0.003230],[2.825478,-4.047572],[7.710004,-3.347338],[-6.812750,-7.885725],[9.016388,9.110840],[-9.450995,0.348482],[-1.733972,8.891317],[-0.011049,7.036181],[-3.183278,-0.199356],[-1.192893,-9.226441],[-8.778599,5.724858],[-6.872049,-1.569014],[-8.467797,8.352379],[-2.086489,-9.975188],[2.396265,-9.928003],[2.384897,4.898723],[-5.080351,-2.668692],[7.088699,-6.475005],[5.330569,-1.906071],[7.459930,0.572679],[-4.827473,0.743548],[3.926572,7.057216],[5.621884,-8.346902],[7.820304,-6.340487],[-1.231914,-4.426895],[5.143283,4.770199],[8.569223,-2.154475],[5.388968,-4.828101],[-6.975664,-2.153394],[1.852556,7.775577],[2.425280,5.091950],[9.798130,6.450027],[-0.107767,2.167498],[-4.835588,-9.089303],[-3.052672,8.983561],[-7.065321,5.143439],[9.006255,-7.864255],[9.127788,3.333322],[-7.429972,-8.867669],[-1.971809,4.766279],[8.676327,-4.491589],[1.394007,7.708186],[-4.688041,7.537909],[-8.935572,2.161035],[-7.420515,-4.463023],[7.067672,3.971925],[0.095185,-1.085468],[4.822694,-0.735909],[-2.584947,-6.399287],[-5.060358,-0.538624],[-6.542226,4.318713],[-0.337253,-3.329608],[8.554344,7.760503],[-3.782761,-4.687960],[-6.305113,1.855159],[-4.234253,-4.651293],[3.558082,-9.357389],[2.419948,-0.187160],[2.545709,-8.804084],[-7.643843,-9.111830],[-3.947787,8.148751],[-4.226059,-5.526833],[-1.074165,-5.387790],[0.242503,2.799389],[-0.741738,-1.288709],[-2.157569,9.003190],[4.356815,-2.927390],[7.226050,3.453631],[-4.880993,-6.505232],[-6.026109,5.690834],[1.750419,8.507292],[-4.573972,9.298100],[-5.720310,-1.630331],[-1.445341,-3.370500],[-0.221479,4.565178],[-4.258944,0.305848],[0.810273,1.372789],[-5.949953,-1.341640],[1.630052,-9.147977],[0.253547,-3.754451],[-4.586703,-9.359693],[-9.121424,-3.677700],[2.365443,-2.955330],[-7.692661,-1.335988],[-7.936568,1.791404],[-0.362789,-6.420917],[5.091632,-5.821306],[-0.698101,-5.420630],[4.968458,4.616460],[-3.934687,-9.292739],[2.782449,2.330685],[-5.759840,-8.237285],[7.477368,2.361832],[0.245401,0.777434],[1.057079,3.576850],[-2.691605,-1.483769],[0.644300,-0.315145],[7.123067,3.606432],[1.312017,-8.803674],[9.191773,-6.832739],[-5.043386,-7.534051],[7.767705,-2.326793],[6.278172,-8.537630],[8.430765,-9.056780],[-6.675094,-3.657177],[8.068073,3.042347],[-6.475261,0.413094],[-3.379271,6.025330],[0.793090,-3.470418],[5.330922,6.249346],[9.708214,7.620746],[-2.502087,6.314165],[-7.607432,-9.980695],[7.111681,-2.386014],[1.697842,0.789774],[-5.052195,-1.351298],[3.550068,-3.575712],[6.108056,5.897762],[-2.066954,-9.443337],[-3.145559,5.629875],[2.136004,9.986761],[9.012841,1.175581],[9.783155,-7.347377],[8.981414,9.463451],[-9.860188,2.729076],[-4.524505,-8.673352],[2.252408,9.680630],[-0.660496,-4.832610],[0.721312,-3.234946],[-3.891021,5.717933],[2.301481,6.371832],[7.159948,3.692449],[-8.563364,8.500211],[9.878551,5.802480],[-6.461212,4.011392],[-0.234502,9.539164],[2.646614,-7.864537],[8.016914,8.422416],[-1.624954,6.376652],[9.944308,3.872538],[6.569052,-5.247940],[-7.785512,-3.351334],[0.123987,0.111750],[2.212094,6.070316],[-2.916058,-4.792648],[3.505310,-4.103078],[-1.356536,7.455004],[-3.806328,-0.334493],[-6.186030,1.913689],[-8.353638,8.705342],[8.671242,9.413029],[1.846823,6.134932],[7.742576,4.772949],[1.342018,-4.591871],[8.617007,8.085290],[-0.168281,-6.785239],[3.096938,1.952776],[6.512734,4.586663],[9.829700,1.695989],[9.530224,-2.945357],[0.346065,1.829942],[-6.325909,-8.523465],[-5.550070,0.317891],[2.732747,9.129804],[7.923071,5.119966],[9.332607,8.765577],[5.163415,-3.578980],[6.554627,0.767902],[-2.145533,8.810988],[-3.878480,1.044388],[-4.927734,7.909603],[-4.135716,-8.624784],[0.239464,-7.482881],[-3.871762,8.190229],[-1.812285,-3.855007],[0.670825,-7.291452],[-9.578767,-8.525626],[-8.392996,8.444963],[-2.746771,-4.762769],[8.337229,2.857898],[-0.447027,-9.266439],[9.994786,0.198052],[6.754914,-6.200622],[4.036158,-1.970734],[-3.118388,4.194995],[-2.910868,5.589406],[5.003522,5.545783],[-3.935593,-8.088477],[-1.550854,4.263052],[-4.768853,-4.035868],[-5.369878,-3.808482],[2.615814,-6.284748],[6.579624,-7.453889],[-4.396697,6.878041],[-5.615444,4.896749],[8.756187,1.272722],[-7.206961,4.802465],[4.704027,-6.258028],[-2.292598,-3.329446],[1.481820,-8.859838],[-1.994485,6.191276],[-4.717024,-2.755630],[7.941953,-9.782391],[0.277855,7.394929],[-7.458996,3.350817],[-2.508714,-4.663893],[-5.149841,-0.314736],[5.990133,6.274052],[-4.063762,-1.997141],[6.350971,3.801088],[-0.486560,2.858221],[6.499914,9.390057],[2.894577,-1.804653],[-0.659442,8.553863],[7.730071,7.936345],[-6.029027,-1.423877],[5.825466,1.688686],[8.422640,0.698422],[-0.600179,-5.869964],[5.652862,-3.175178],[-3.060573,-8.973889],[1.241531,3.541285],[-7.790527,1.406997],[7.599438,7.610889],[-2.376544,1.086624],[8.578658,-3.848813],[4.960621,1.655240],[-1.784726,-5.401354],[-9.072486,-1.674186],[-2.342707,-2.768290],[-4.502409,8.418394],[5.422941,-6.931462],[2.120164,-8.025528],[-7.035973,7.267230],[7.368664,8.526254],[-6.434358,-2.438850],[-8.511270,-6.137198],[-7.168311,7.078156],[-9.147488,5.887120],[2.161266,6.404611],[5.803591,5.044971],[-8.014868,-1.440483],[-5.063158,-0.822897],[3.101628,6.990442],[4.500162,-0.187153],[4.644914,-4.853119],[-6.961734,8.133450],[6.742236,-8.448022],[-6.496731,-2.181065],[-5.280117,-2.350307],[-7.330407,9.623794],[0.811185,-0.396811],[-4.310827,3.370428],[-4.334149,6.678022],[6.646260,1.065330],[-4.444896,4.120310],[9.073407,2.756455],[-2.524477,-5.510471],[-1.341548,-4.734341],[8.146269,-5.628999],[3.067709,1.685401],[4.664955,-8.275581],[4.911470,1.707406],[-6.196287,4.721953],[2.883580,9.591488],[-8.999206,-7.799926],[-0.893441,5.367025],[4.835526,1.252952],[3.431928,9.209467],[-2.819103,0.369682],[3.542696,3.885444],[5.762656,7.705380],[4.689134,2.373352],[8.278410,3.057654],[-8.149351,0.765903],[-5.062091,2.324211],[3.124074,1.622257],[-9.014285,4.476047],[3.869537,1.819555],[9.151703,1.950199],[-6.676137,9.677479],[6.209967,5.390770],[8.758497,7.072643],[9.993438,6.825601],[4.919950,-3.508822],[7.607596,2.466331],[-6.769655,9.567008],[-3.992603,7.555138],[8.861548,-1.499100],[9.011807,5.196659],[-0.661074,-4.402271],[6.755095,-8.858179],[-5.288889,-2.710545],[-0.197609,6.762500],[1.268354,3.897132],[5.622076,-8.272559],[6.220443,0.791315],[-6.154995,3.715744],[-9.823779,-1.122780],[2.796167,-3.038130],[-0.209229,1.592173],[8.947857,3.839845],[9.611667,-2.897869],[0.322009,-1.336406],[7.841142,1.157978],[-8.295999,-8.527622],[1.298837,-0.386790],[6.121145,-4.588393],[1.340640,-5.956264],[-2.045378,6.171257],[-1.572932,5.621369],[-1.612457,-2.401475],[2.638139,6.349260],[-2.957755,-6.503004],[0.861136,-5.087853],[-6.447053,-1.886863],[-9.767464,-0.472765],[-9.059761,2.808197],[5.837948,4.294821],[-1.316991,5.342214],[2.024809,7.832774],[-1.507837,9.057077],[-6.247419,-2.665407],[5.268383,-1.130156],[1.868404,-6.392131],[7.260044,6.245890],[-7.096480,-1.144290],[-9.649059,1.503430],[6.586877,-1.666984],[-3.625134,6.246529],[0.220830,7.329224],[-6.834448,6.749193],[-5.894481,2.093027],[5.695926,-2.770735],[6.803030,-0.598838],[-0.665277,-2.672599],[-5.386343,2.949777],[-3.603321,1.703677],[-9.740587,-3.966821],[-2.337917,4.742226],[-2.396239,-5.681830],[6.529233,9.753736],[-3.763439,-7.575540],[4.102403,-2.518797],[5.620823,8.357591],[-7.135031,-9.735663],[8.766362,1.823095],[-3.541618,0.079390],[6.614187,-5.770963],[-8.096655,-6.962186],[1.585013,-9.105078],[3.359535,-6.757322],[-7.812413,-7.412325],[-5.088545,-3.808551],[-8.372518,5.059770],[-0.075297,3.084204],[0.680562,-2.823285],[7.761676,-9.615989],[6.747798,-3.211520],[1.831710,-4.860655],[-9.378614,-7.751349],[2.808290,-4.298064],[-6.631727,-5.682088],[-4.199119,-7.227605],[2.757968,-7.271635],[0.094058,3.363766],[0.023089,8.914282],[-8.625755,-1.871638],[3.737966,2.396357],[9.253034,-8.080293],[1.700076,-3.264404],[-5.088154,2.844122],[5.699138,-6.983172],[-9.423190,-5.379098],[0.272373,-7.127527],[2.741254,-3.746307],[8.851476,7.918921],[-1.848547,-8.603319],[-7.245321,6.148806],[-8.023450,-5.389429],[-2.475388,-1.523684],[-6.996390,-6.361169],[3.815654,0.424848],[-9.127849,0.978410],[6.382423,-3.989507],[-1.957388,1.856896],[-9.777860,8.325223],[-5.739903,-3.705739],[-7.060475,2.671227],[3.208734,0.270661],[0.786246,9.559727],[-4.289352,2.416965],[9.714180,9.782815],[1.778719,-4.957160],[-7.971597,-3.876722],[8.964826,1.118323],[4.355371,-1.087927],[0.633307,9.544500]], dtype = "float32")#candidate|6254|(576, 2)|const|float32
call_6252 = relay.TupleGetItem(func_6047_call(relay.reshape(var_6253.astype('int16'), [9, 13, 2]), relay.reshape(const_6254.astype('float32'), [24, 48]), ), 4)
call_6255 = relay.TupleGetItem(func_6050_call(relay.reshape(var_6253.astype('int16'), [9, 13, 2]), relay.reshape(const_6254.astype('float32'), [24, 48]), ), 4)
bop_6269 = relay.less_equal(call_6252.astype('bool'), relay.reshape(var_6253.astype('bool'), relay.shape_of(call_6252))) # shape=(9, 13, 2)
bop_6272 = relay.less_equal(call_6255.astype('bool'), relay.reshape(var_6253.astype('bool'), relay.shape_of(call_6255))) # shape=(9, 13, 2)
func_6198_call = mod.get_global_var('func_6198')
func_6201_call = mutated_mod.get_global_var('func_6201')
const_6279 = relay.const([1,8,-2,6,1,-5,6,7,-9,8,-7,-7,9,6,-6,3,2,7,-2,-8,-2,5,8,3,-7,7,1,-9,-3,8,-1,-7,4,7,-6,8,7,-7,7,2,1,10,-3,-4,3,8,-5,-8,-8,3,-9,1,4,1,-7,9,-4,10,9,6,8,-5,8,9,8,9,3,-3,9,2,1,-4,2,4,9,-1,-5,-9,-10,8,-10,-5,-6,-4], dtype = "int8")#candidate|6279|(84,)|const|int8
call_6278 = relay.TupleGetItem(func_6198_call(relay.reshape(const_6279.astype('int8'), [3, 14, 2]), relay.reshape(const_6279.astype('int8'), [3, 14, 2]), ), 0)
call_6280 = relay.TupleGetItem(func_6201_call(relay.reshape(const_6279.astype('int8'), [3, 14, 2]), relay.reshape(const_6279.astype('int8'), [3, 14, 2]), ), 0)
uop_6284 = relay.sin(bop_6269.astype('float32')) # shape=(9, 13, 2)
uop_6286 = relay.sin(bop_6272.astype('float32')) # shape=(9, 13, 2)
func_4715_call = mod.get_global_var('func_4715')
func_4717_call = mutated_mod.get_global_var('func_4717')
call_6287 = relay.TupleGetItem(func_4715_call(), 0)
call_6288 = relay.TupleGetItem(func_4717_call(), 0)
func_631_call = mod.get_global_var('func_631')
func_636_call = mutated_mod.get_global_var('func_636')
const_6295 = relay.const([-2,-4,-9,-9,-2,10,7,9,-8,8,8,-7,-2,7,1,-9,-2,5,9,8,7,7,5,-10,7,-8,-1,1,8,-7,8,1,7,3,-1,7,-10,2,10,-2,-1,-3,7,-6,-4,3,9,3,-9,-3,-1,8,7,-9,-1,-6,-3,-5,-3,-3,-5,8,-10,1,-9,-2,7,2,-10,-10,3,-3,5,5,8,2,6,-9,-10,8,7,8,9,-5,-2,-2,-1,1,5,-3,-6,8,4,10,8,-5,-9,-6,-4,9,-9,3,8,-7,10,5,4,9,1,-4,-1,-3,-4,1,3,4,-3,-2,-2,3,9,-9,-3,1,-2,-2,-5,-3,5,7,-4,-10,9,-9,2,-3,1,-2,-2,10,-1,5,9,-7,2,4,6,-2,-7,5,4,-10,2,1,6,-8,-6,-5,2,9,5,-9,-7,-5,3,-4,10,4,-6,5,-8,3,5,9,9,9,-1,-6,-1,-5], dtype = "uint16")#candidate|6295|(180,)|const|uint16
call_6294 = relay.TupleGetItem(func_631_call(relay.reshape(const_6254.astype('float32'), [16, 12, 6]), relay.reshape(const_6295.astype('uint16'), [180,]), relay.reshape(const_6295.astype('uint16'), [5, 6, 6]), ), 3)
call_6296 = relay.TupleGetItem(func_636_call(relay.reshape(const_6254.astype('float32'), [16, 12, 6]), relay.reshape(const_6295.astype('uint16'), [180,]), relay.reshape(const_6295.astype('uint16'), [5, 6, 6]), ), 3)
output = relay.Tuple([call_6239,const_6254,call_6278,const_6279,uop_6284,call_6287,call_6294,const_6295,])
output2 = relay.Tuple([call_6240,const_6254,call_6280,const_6279,uop_6286,call_6288,call_6296,const_6295,])
func_6300 = relay.Function([var_6253,], output)
mod['func_6300'] = func_6300
mod = relay.transform.InferType()(mod)
mutated_mod['func_6300'] = func_6300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6301 = relay.var("var_6301", dtype = "int16", shape = (234,))#candidate|6301|(234,)|var|int16
func_6300_call = mutated_mod.get_global_var('func_6300')
call_6302 = func_6300_call(var_6301)
output = call_6302
func_6303 = relay.Function([var_6301], output)
mutated_mod['func_6303'] = func_6303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6158_call = mod.get_global_var('func_6158')
func_6159_call = mutated_mod.get_global_var('func_6159')
call_6311 = relay.TupleGetItem(func_6158_call(), 4)
call_6312 = relay.TupleGetItem(func_6159_call(), 4)
var_6314 = relay.var("var_6314", dtype = "bool", shape = (50, 4))#candidate|6314|(50, 4)|var|bool
bop_6315 = relay.logical_and(call_6311.astype('bool'), relay.reshape(var_6314.astype('bool'), relay.shape_of(call_6311))) # shape=(50, 4)
bop_6318 = relay.logical_and(call_6312.astype('bool'), relay.reshape(var_6314.astype('bool'), relay.shape_of(call_6312))) # shape=(50, 4)
output = relay.Tuple([bop_6315,])
output2 = relay.Tuple([bop_6318,])
func_6348 = relay.Function([var_6314,], output)
mod['func_6348'] = func_6348
mod = relay.transform.InferType()(mod)
var_6349 = relay.var("var_6349", dtype = "bool", shape = (50, 4))#candidate|6349|(50, 4)|var|bool
output = func_6348(var_6349)
func_6350 = relay.Function([var_6349], output)
mutated_mod['func_6350'] = func_6350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3689_call = mod.get_global_var('func_3689')
func_3691_call = mutated_mod.get_global_var('func_3691')
call_6398 = func_3689_call()
call_6399 = func_3689_call()
func_5603_call = mod.get_global_var('func_5603')
func_5606_call = mutated_mod.get_global_var('func_5606')
var_6408 = relay.var("var_6408", dtype = "uint32", shape = (315,))#candidate|6408|(315,)|var|uint32
call_6407 = relay.TupleGetItem(func_5603_call(relay.reshape(var_6408.astype('uint32'), [5, 9, 7])), 1)
call_6409 = relay.TupleGetItem(func_5606_call(relay.reshape(var_6408.astype('uint32'), [5, 9, 7])), 1)
func_6300_call = mod.get_global_var('func_6300')
func_6303_call = mutated_mod.get_global_var('func_6303')
const_6417 = relay.const([-3,9,3,-3,2,-3,-6,8,9,-4,-1,8,-8,-7,4,-5,6,-3,7,-7,7,1,6,-9,3,6,8,1,7,-4,-5,10,-6,-10,8,3,-5,9,6,-8,3,-2,-10,-8,-3,9,-5,9,3,6,7,9,6,5,5,-2,7,-1,8,-5,-6,-9,5,-4,-9,10,-4,8,-4,-3,-6,9,-8,2,2,7,2,-10,-5,-5,-7,-8,3,-10,-9,-8,-9,-10,-7,-2,-10,8,-6,10,3,6,10,2,10,-2,6,-5,9,1,-8,7,-4,1,-3,3,-6,-7,-3,-2,10,3,6,-8,-3,-2,-4,10,-6,-7,-4,9,9,8,5,-6,-4,1,-9,6,10,3,-9,-1,4,7,10,9,2,-5,7,-3,2,-2,5,-3,8,-10,-8,3,10,-1,-8,2,-8,-6,-10,-6,3,3,6,4,1,10,-4,1,-4,4,3,-1,-5,-5,-8,-7,-9,-8,6,10,7,-9,2,4,-4,-8,-6,-9,-8,6,-5,6,3,10,7,1,9,-4,3,9,-8,-6,7,-7,-10,-2,8,-1,-3,4,-3,3,-6,5,7,-5,-2,-3,-6,6,5,-9,6,-6,2,-9,5,-7,3,10,-5,-6], dtype = "int16")#candidate|6417|(234,)|const|int16
call_6416 = relay.TupleGetItem(func_6300_call(relay.reshape(const_6417.astype('int16'), [234,])), 6)
call_6418 = relay.TupleGetItem(func_6303_call(relay.reshape(const_6417.astype('int16'), [234,])), 6)
func_4650_call = mod.get_global_var('func_4650')
func_4651_call = mutated_mod.get_global_var('func_4651')
call_6448 = relay.TupleGetItem(func_4650_call(), 1)
call_6449 = relay.TupleGetItem(func_4651_call(), 1)
bop_6456 = relay.add(call_6407.astype('int8'), relay.reshape(var_6408.astype('int8'), relay.shape_of(call_6407))) # shape=(5, 9, 7)
bop_6459 = relay.add(call_6409.astype('int8'), relay.reshape(var_6408.astype('int8'), relay.shape_of(call_6409))) # shape=(5, 9, 7)
func_2883_call = mod.get_global_var('func_2883')
func_2884_call = mutated_mod.get_global_var('func_2884')
call_6460 = relay.TupleGetItem(func_2883_call(), 1)
call_6461 = relay.TupleGetItem(func_2884_call(), 1)
output = relay.Tuple([call_6398,call_6416,const_6417,call_6448,bop_6456,call_6460,])
output2 = relay.Tuple([call_6399,call_6418,const_6417,call_6449,bop_6459,call_6461,])
func_6490 = relay.Function([var_6408,], output)
mod['func_6490'] = func_6490
mod = relay.transform.InferType()(mod)
mutated_mod['func_6490'] = func_6490
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6491 = relay.var("var_6491", dtype = "uint32", shape = (315,))#candidate|6491|(315,)|var|uint32
func_6490_call = mutated_mod.get_global_var('func_6490')
call_6492 = func_6490_call(var_6491)
output = call_6492
func_6493 = relay.Function([var_6491], output)
mutated_mod['func_6493'] = func_6493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_6498 = relay.TupleGetItem(func_2625_call(), 1)
call_6499 = relay.TupleGetItem(func_2626_call(), 1)
uop_6502 = relay.erf(call_6498.astype('float64')) # shape=(12, 6, 10)
uop_6504 = relay.erf(call_6499.astype('float64')) # shape=(12, 6, 10)
output = relay.Tuple([uop_6502,])
output2 = relay.Tuple([uop_6504,])
func_6511 = relay.Function([], output)
mod['func_6511'] = func_6511
mod = relay.transform.InferType()(mod)
mutated_mod['func_6511'] = func_6511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6511_call = mutated_mod.get_global_var('func_6511')
call_6512 = func_6511_call()
output = call_6512
func_6513 = relay.Function([], output)
mutated_mod['func_6513'] = func_6513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4291_call = mod.get_global_var('func_4291')
func_4293_call = mutated_mod.get_global_var('func_4293')
call_6537 = relay.TupleGetItem(func_4291_call(), 0)
call_6538 = relay.TupleGetItem(func_4293_call(), 0)
func_5727_call = mod.get_global_var('func_5727')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_6553 = relay.TupleGetItem(func_5727_call(), 0)
call_6554 = relay.TupleGetItem(func_5728_call(), 0)
output = relay.Tuple([call_6537,call_6553,])
output2 = relay.Tuple([call_6538,call_6554,])
func_6570 = relay.Function([], output)
mod['func_6570'] = func_6570
mod = relay.transform.InferType()(mod)
output = func_6570()
func_6571 = relay.Function([], output)
mutated_mod['func_6571'] = func_6571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6511_call = mod.get_global_var('func_6511')
func_6513_call = mutated_mod.get_global_var('func_6513')
call_6572 = relay.TupleGetItem(func_6511_call(), 0)
call_6573 = relay.TupleGetItem(func_6513_call(), 0)
func_3049_call = mod.get_global_var('func_3049')
func_3055_call = mutated_mod.get_global_var('func_3055')
const_6578 = relay.const([4.861201,-4.975789,-7.920703,3.688549,6.192078,-7.479574,3.572125,-9.186403,-1.598725,-1.050208,-0.088310,-3.532303,3.916861,-0.298594,1.502169,-6.395804,4.962223,-9.699987,2.677720,-0.079348,1.878784,4.681507,-9.039921,-6.327949,-8.762350,9.557866,2.440734,2.018822,-7.679723,7.312041,1.396048,-6.360564,-2.159313,-4.123319,-0.769602,-9.631259,8.586364,-9.558588,-9.482067,-3.808202,2.220017,9.059926,8.730531,1.907366,-6.980102,-9.984009,-5.235481,0.027565,0.406282,-8.915546,-8.479113,3.754652,9.151302,6.887802,-8.066233,-7.797403,-6.761531,4.106749,2.629163,8.171764,5.895034,2.371557,-7.923246,5.828526,-1.008481,8.492928,-0.015565,-5.477685,9.094675,1.069610,8.206042,9.868142,-8.631642,9.144419,-4.568301,1.268796,-3.050442,3.105206,0.522640,5.177496,1.151584,7.453871,5.075302,1.590708,6.462090,6.506528,-8.259860,-2.037418,4.583686,-8.064612,-1.052112,3.711101,-5.714355,8.213992,8.765849,3.229795,-7.863461,7.434194,-3.750431,-7.628768,2.489785,-8.115850,-9.113660,-7.475509,0.184550,4.180954,3.080183,-5.933317,-7.010931,7.669187,-4.212481,-4.944694,2.883992,8.292572,-7.508919,-2.475584,8.997555,8.166555,6.880638,3.235078,7.352421,0.945781,6.251101,-1.335136,7.193102,-0.192111,0.610349,-1.088941,-2.403242,-1.116058,3.544067,-7.068313,-9.851901,4.148400,-7.267761,-0.059649,8.869260,-2.107117,0.400379,-5.917044,-2.616664,1.293434,5.895228,0.892965,2.813462,-9.219952,-0.415504,3.878852,8.118535,-3.022133,9.717753,3.881864,-0.537840,2.354515,-1.482700,1.494919,-1.764097,-3.012172,-5.040233,6.463597,-7.780762,0.220592,4.244381,0.194126,7.860230,-2.555058,-8.630793,5.618903,2.154689,-1.084427,2.100631,-4.923575,-0.228353,5.880090,-9.145922,-1.067203,1.569668,3.380611,-7.489004,3.293635,4.380497,-5.298097,9.797589,-6.058736,8.067585,-4.227218,-6.380238,-5.464835,-5.611527,-2.068728,5.829757,3.481830,-8.302665,8.101397,9.620906,-2.094607,-5.552835,-2.183869,-7.648805,-3.305671,1.561957,-6.572644,1.966911,2.179766,0.226020,5.368559,-7.131654,2.984944,6.291318,-4.038940,5.491387,7.255714,1.023677,7.035225,5.706031,6.999944,-6.300476,-9.403459,9.349323,4.320838,8.700425,7.562063,8.639864,-0.832313,7.997949,1.997250,9.083459,-1.975289,-0.504339,3.792154,8.519049,6.587973,-4.331571,5.745235,5.597174,-6.770685,4.512155,-9.644041,-6.154669,-7.508469,1.350333,-2.949064,-0.932862,-1.755572,-8.319403,-8.971629,-4.437277,-5.995859,-9.388324,-4.171109,-7.450199,-5.346573,-5.971454,1.845991,-8.236829,-9.918791,6.499960,-5.428227,8.615846,6.284481,-9.646064,1.928857,4.362504,-1.172514,-1.785344,8.180186,3.437720,-8.152872,-3.095810,4.965002,7.306545,7.067863,-7.550483,8.980683,-6.079075,-4.510519,-4.433254,7.257193,3.747783,0.353043,3.671065,-1.252563,4.169874,-4.857974,-1.093633,-0.622724,-6.106671,7.743795,1.596715,-4.674425,4.843247,5.647059,3.676907,2.348498,-9.071108,-1.987061,0.409320,-8.712338,0.274355,-9.325049,-8.136918,-3.923144,-5.920094,-3.975635,-8.999714,8.008040,1.774986,0.359308,-3.555453,6.873250,-9.281593,-6.630190,-1.062313,-8.469816,0.376782,-6.208097,6.695607,-0.890408,-0.130632,8.865271,-7.731655,-4.257613,4.746497,-2.779385,-4.569883,-3.490605,7.650734,-5.578279,-8.223823,8.362009,7.721796,0.628346,-1.354533,1.047950,-4.321674,6.058990,2.363413,-3.226861,-9.037461,-9.706516,-4.325489,6.613179,0.017800,-6.403567,-7.479501,-9.519317,0.540725,-9.498210,1.530175,-5.040926,-5.340808,-3.463259,4.513413,8.747618,9.318832,-1.432847,-4.629906,8.507401,5.543765,7.393574,-7.820793,1.618051,-0.194035,7.980411,1.754787,4.923437,-0.295057,-2.185315,6.791984,9.716762,2.414094,-9.941388,7.750518,-1.150710,7.635766,-9.779357,6.496264,2.882618,0.500770,8.230876,-1.252611,-1.696022,9.344045,-8.894433,-4.335813,1.947373,4.689932,-5.475676,-5.369680,5.752516,-0.128608,2.798181,-7.971937,8.051256,0.162240,-6.574607,-2.946114,-2.633124,2.485911,-5.097346,-3.286159,-5.320623,6.758119,-3.701644,9.088294,-5.935679,1.387697,1.251372,-2.200787,2.467831,5.370907,-5.965300,7.502518,2.269239,6.427303,-7.516279,-1.029234,-7.751334,9.905224,8.213556,-2.775029,3.988718,9.421099,4.851627,2.487965,9.741847,9.672181,-7.951293,5.644443,9.904390,8.569409,-8.490399,-1.340451,-9.780654,-6.093907,-9.661953,8.907422,-8.863060,-2.246238,-6.367761,2.571542,1.027470,8.024745,8.779772,8.158654,-9.271458,-5.920234,-8.808316,9.975118,7.111511,-1.561582,-6.183852,6.171693,-6.477477,7.887377,2.416921,4.188015,2.940664,0.929346,0.294827,4.738325,4.697453,-5.959015,2.937240,-7.934284,2.393147,-5.323719,-5.020673,4.129780,-8.990430,-7.485689,5.616187,-2.902675,-3.839121,8.402389,-5.466201,9.449947,-3.738582,-3.055456,7.449890,-5.771112,1.388665,4.392005,-0.450124,6.847018,2.807466,0.390421,0.855475,4.338844,3.948782,4.067862,1.735936,5.833780,-9.514573,2.120899,7.683204,6.278872,0.322392,-1.640794,3.706807,-3.979334,0.923782,5.358414,4.910449,7.559183,0.861787,-9.683448,2.716856,-1.244653,1.715162,-2.102816,-8.267868,-6.948915,-7.830318,7.877096,-4.346327,-1.952053,8.679442,-8.823928,-4.918919,6.777697,-8.895292,-7.953999,-7.218948,2.493046,5.432499,-5.859671,1.477655,1.529940,0.428965,6.121533,-9.159150,-1.126347,3.424280,-0.121045,-4.852916,2.413921,0.604881,-5.495159,1.202546,-1.357378,8.835626,-6.715568,6.770032,-3.888083,-9.117503,-6.106892,9.316526,2.714696,8.416199,-4.057675,2.109805,-5.118132,-2.156766,-1.305541,-7.051080,-0.050386,2.842379,8.385579,-6.752371,-2.703432,9.825453,6.687600,2.410780,-5.865436,-3.497952,-6.998728,-0.708800,-8.238562,3.626397,-5.801249,0.515848,-4.425313,9.062976,0.500382,5.357964,2.819996,-8.408765,-4.341645,4.524673,-0.870901,4.824112,5.397690,7.107763,-4.415090,2.848961,7.799881,8.024554,5.134562,4.992668,-7.405356,-5.362606,6.106943,-2.572849,-6.649459,-8.352296,9.230824,2.145159,-3.246868,9.751689,-3.031497,2.233139,0.638043,3.123056,-9.218081,-7.008170,2.356508,-2.158538,9.961264,-5.743904,-0.658528,5.664294,4.602059,-5.775158,7.798562,-8.061346,-2.883165,5.727809,0.480136,4.547908,6.670630,-5.297360,-0.399836,-1.343887,-4.147328,-8.122142,2.285978,-3.080212,-9.735241,-7.695049,-2.050018,2.272463,2.577394,1.851281,4.271797,-6.409552,-3.237110,-4.498857,6.367014,-5.284670,2.120328,-4.304039,-1.302989,8.562982,3.223791,2.221237,8.833141,3.228765,6.959573,3.096793,4.466766,-8.189777,-2.392813,-9.564400,1.409097,6.409838,1.898154,1.434732,5.727677,5.245966,3.004316,-2.159739,5.412485,9.108920,-2.948641,-7.637123,-5.408436,9.751613,4.331452,-0.114187,2.025704,3.829902,7.574515,-3.747910,-8.832049,1.480274,-3.643589,-8.820192,6.997493,6.470069,-5.962541,0.410516,-4.918790,7.666514,0.933484,-5.374435,-1.502681,0.296985,-6.522285,-1.683930,1.844678,-4.907555,6.368790,-2.894246,-5.097319,2.793144,1.543572,4.426337,4.824052,6.349002,-3.147571,0.797488,1.272049,-4.504381,7.695087,-3.809693,9.032185,-4.912798,7.887616,3.361785,-1.678490,-5.370135,-9.829665,8.647660,2.359428,-2.816716,-8.829839,-1.012908,-6.459975,-1.532964,5.130323,1.032037,1.423505,1.035395,-8.272773,3.517684,0.163064,-4.459006,6.904413,-7.707657,-1.154626,3.522504,-2.064872,-2.368609,-5.490951,-3.225365,-3.154038,-6.216754,-7.108741,-9.765767,8.539840,1.973413,-4.512896,-3.292327,-2.141675,-9.663706,4.112475,1.918342,0.627949,-1.661869,-3.614741,4.425527,-0.902797,6.416549,9.508117,2.210535,5.877772,-0.409895,-2.528354,1.189881,9.915248,3.632292,0.039870,-6.444270,7.568864,7.171338,-3.551364,-2.335537,-0.942635,9.557978,3.813494,-6.007908,2.939819,-4.907432,1.744771,-1.641378,0.709228,5.565503,9.766758,6.585924,6.095017,-6.680608,7.732612,-6.306562,-3.081799,-8.512575,6.657173,-1.380450,4.866941,-6.128625,3.152010,1.545376,8.802513,7.873139,-8.792711,0.318023,1.665524,6.905868,-4.472838,5.079569,9.871628,-4.660564,-1.969995,-5.306086,-1.339400,9.960671,1.232090,-8.921412,9.653425,0.677948,8.745812,8.680344,6.877852,1.785373,5.119318,-4.928944,-4.507714,7.067650,-7.138885,-8.117143,-4.677217,-5.089741,-4.489976,-1.473762,-0.322124,-6.940314,-7.961570,0.422609,-7.570395,6.269341,8.574521,5.947627,0.417225,-9.100502,-6.878956,-8.007775,-6.629173,-2.053670,0.304360,8.885458,7.901744,0.359520,2.167481,0.128665,-2.869597,1.908796,-3.005240,0.416990,8.009706,3.426922,7.446439,4.915025,-6.195641,-8.961848,-9.710781,-8.800065,0.184912,-7.303140,-0.524741,3.131549,-6.227317,-6.376212,1.085247,-7.246934,5.787569,-0.546783,2.969697,0.257936,1.192677,-8.216234,7.497723,8.001314,-1.173400,4.570377,2.025672,4.935271,-4.495672,7.941300,-1.745239,-4.015290,5.469842,-7.871403,-3.456471,1.935103,3.096922,-2.635468,-5.945937,-5.032984,4.788183,6.052170,-5.220747,-5.250004,-9.077841,-0.329458,-5.812338,-7.571166,5.780944,-8.592975,-3.046268,4.523334,3.735780,-1.136720,-1.654696,4.878366,5.128158,-9.578797,0.116207,-4.865930,-3.307565,-4.209302,4.550007,8.118555,9.221527,2.636259,3.388508,-7.770513,-3.567886,-2.212782,8.294760,-5.944353,-4.939790,-1.908012,6.031191,2.023799,9.695730,-6.084672,-5.891816,6.413912,-8.989969,-7.310340,2.338453,-2.312352,2.281976,-6.607479,-0.818889,1.843782,-2.861093,9.826777,-3.076352,6.085690,-1.477670,5.561377,6.259974,3.634649,0.984277,4.855764,-1.849561,-0.149076,-5.009200,-5.325306,3.978875,1.968151,1.856229,0.502767,1.915372,0.830529,5.551434,4.342549,9.629168,-2.510663,-5.193980,6.801805,9.399749,-8.691854,4.673230,5.075890,0.942843,-0.695645,5.657326,-9.736594,-5.288861,-9.377711,-6.435810,4.101776,-1.101294,-3.961374,2.960166,1.504219,6.558533,4.702790,-3.119841,0.924195,3.567050,-9.932299,-6.548993,-6.369425,-1.245945,-6.054930,-1.466436,-8.688625,3.653629,4.673259,9.546459,9.518796,-9.643791,0.621488,0.347371,-1.284624,-6.703548,6.071370,-8.649980,1.481166,9.527694,7.287569,4.961048,-7.531181,9.617535,-3.305197,8.851360,0.250584,-9.245891,-7.879751,-3.781220,-6.186628,-6.860265,7.943302,0.150749,6.182761,-5.737865,-5.864184,4.462310,-7.385016,-1.200595,7.793205,-4.876911,-7.725981,0.133121,9.727621,3.808558,-0.184149,8.025286,-8.044566,-2.059596,8.204088,4.390606,1.606139,1.324845,1.136490,-0.304058,3.435967,9.127706,9.467214,-8.830932,-7.854590,-9.544228,8.143790,-6.192543,5.119013,-3.786049,4.806978,-0.641342,-2.557164,-2.831855,-2.861136,-7.470814,-6.922055,1.744652,-4.241666,-8.814243,8.977777,2.056695,-6.109338,2.141820,-0.900741,4.583053,6.508867,-3.860049,2.331303,2.881065,2.614557,2.681576,4.262889,7.732043,-6.030597,9.418286,3.933040,5.143234,-7.306133,8.986519,-6.772051,0.699914,-2.377970,2.652876,-2.376524,8.863682,-1.321521,2.943925,7.137960,7.760566,-0.641105,-8.526554,1.634083,-6.062613,-4.115241,-8.537131,-3.385800,-3.841078,-4.862636,-7.035633,-8.783220,-7.832243,-0.939273,-3.864843,7.666764,3.598881,-5.615362,1.457410,9.455376,-3.289656,6.037929,-3.477750,-9.065522,-9.479063,-4.533480,1.887623,9.512967,8.949209,-3.185395,7.877056,7.442537,8.401902,-7.423587,5.113291,-9.323118,7.832355,8.559742,6.429317,-7.979668,-9.293532,-8.882499,8.109645,3.514363,6.833148,6.489951,9.506725,-3.859189,-5.053014,5.223238,-7.660372,0.614190,8.459183,-8.121963,-0.504337,3.708693,6.518172,4.460582,9.614784,-3.912272,-8.313468,4.027409,-1.468252,-4.889257], dtype = "float32")#candidate|6578|(1152,)|const|float32
const_6579 = relay.const([8,-7,-7,8,-4,1,1,1,-7,4,-2,-9,-9,10,-5,-5,3,6,10,3,-10,3,-6,-3,-9,-2,-3,-3,-9,-2,-10,-7,-10,4,-8,-3,-1,-4,-1,2,1,10,-5,6,7,-8,6,7,-8,-3,-8,-9,-3,10,1,3,-5,7,7,4,1,9,7,1,-9,-4,-5,9,-7,3,10,9,10,-3,-7,-10,-9,6,-7,1,-5,6,-9,9,2,1,7,-7,-6,-1,9,3,-2,-6,-10,-6,2,-7,5,-7,8,-10,8,10,-10,-6,4,-1,-10,5,3,-7,3,8,-7,-8,-2,10,8,3,2,-8,-3,-5,5,-5,3,-3,-5,8,-3,9,-5,-7,-8,10,2,-8,-9,7,3,10,3,4,-4,10,-7,5,7,-4,2,4,-3,8,3,4,9,-4,7,10,10,-1,8,-10,7,9,9,-5,4,-4,1,3,-4,-2,-4,-6,-4,-3,2,9,-7,-1,10,9,-9,10,-5,-10,1,1,6,-10,-4,-5,6,6,-2,2,-2,5,7,1,-10,10,7,-7,-1,-5,1,1,-4,5,-7,8,-9,1,10,-6,5,2,-9,6,9,5,1,-1,7,1,-2,-1,3,7,-6,-4,8,6,6,-7,1,-8,10,-9,5,10,10,8,-7,-5,-7,5,-6,3,3,10,4,6,5,-2,5,8,5,-9,3,5,-4,5,3,3,-10,10,8,1,-3,-6,6,4,-1,4,-8,4,-1,-1,9,-2,4,4,-10,-7,-7,-3,-6,4,1,-3,-7,8,-6,-4,-10,5,-10,8,-3,5,8,4,-5,1,-6,-5,-1,-3,-2,3,5,8,6,-5,10,10,-8,-2,-3,-8,-9,-4,-6,1,-5,-1,-2,-8,-6,-9,3,-6,4,-3,-5,3,-6,6,3,-9,2,1,-1,-2,3,7,1,-8,-3,9,4,2,1,9,5,-4,-1,3,-5,-1,8,-4,-3,-3,3,-6,6,-6,-8,-2,-4,2,-3,-9,9,7,-10,-6,5,-3,1,-5,9,-5,8,-2,4,-10,-6,-5,9,-2,-3,3,-8,-6,6,-8,-5,-2,10,7,-7,-1,6,-9,8,-5,10,8,-6,6,8,-9,-7,-5,-6,-1,9,-7,9,-1,5,-5,6,2,-8,6,-2,-8,-7,-6,-7,-7,10,-3,-7,-4,-2,9,4,2,2,7,-2,-3,-10,-3,7,-3,-1,5,-3,-10,10,3,-1,-6,-10,6,-8,2,-7,4,4,-10,8,-2,-4,5,2,-10,2,7,-8,5,-2,-5,3,-5,-1,-9,10,-9,4,10,2,10,-5,6,-9,-1,-10,-2,-10,-8,-1,9,10,8,1,-9,-10,-5,-5,-10,3,-5,-10,4,3,-8,-10,-8,4,-4,5,-8,-2,2,5,4,-3,-1,-8,-2,6,5,-8,6,-8,7,-2,10,9,5,-2,-3,8,8,6,6,2,10,6,-2,-4,8,5,4,-10,9,6,6,6,1,-6,6,10,-7,-1,1,-9,3,-8,9,4,7,4,7,9,-3,-6,-2,4,5,10,1,4,5,-1,-8,-6,6,-10,9,-2,6,-9,6,-10,1,6,9,-5,2,9,-2,6,-5,2,8,4,4,4,9,1,-2,-1,9,-5,4,2,9,6,8,5,4,2,5,9,8,3,1,10,1,-10,9,3,-9,1,-8,3,-6,-3,-1,-6,-4,-8,4,-4,3,-4,-5,-10,7,-4,-8,9,4,-6,4,-3,-10,5,10,10,3,-8,10,-3,-1,-2,-3,-4,10,-1,1,-5,4,-6,-9,-10,10,-1,7,-7,-10,-7,9,2,-3,-6,-7,-7,2,7,-2,6,-4,4,10,10,-10,4,10,9,-9,10,-7,-6,2,2,10,-8,4,6,3,3,6,-5,3,2,10,-7,10,-9,7,-8,9,1,-8,-9,-4,-8,-2,-9,-6,9,2,4,1,4,-5,5,8,9,-3,-9,-3,-9,10,1,6,4,6,-10,1,5,6,-4,-7,10,-3,7,6,10,4,1,-1,-10,3,6,-3,2,2,-4,10,9,1,-9,3,-2,-1,9,-6,-9,-8,-2,7,-2,1,7,8,-5,1,-7,-3,3,1,-6,-10,5,1,3,-5,-4,-1,-8,-9,1,8,6,6,-7,-1,6,-9,3,10,5,-1,2,2,-2,-2,10,-10,1,-8,-4,3,-2,3,-10,1,8,6,3,-9,-10,-9,-3,1,-8,-4,7,4,-8,5,10,5,8,-10,-3,8,-10,-6,-10,8,-3,2,-10,1,3,-7,-2,3,-4,-2,9,-10,9,-3,2,-6,-6,7,3,3,4,1,10,5,-4,-3,-7,4,-1,-4,2,10,-8,-1,4,1,4,3,3,-2,-5,9,-9,9,-4,5,-4,-4,-3,-7,9,-7,7,8,10,-6,4,8,-2,5,1,-2,8,-1,-10,-10,-6,1,8,3,7,2,7,-7,10,-7,-4,8,-4,3,-7,3,9,-7,5,-5,-1,6,-9,-1,4,10,6,8,-8,3,3,1,2,-8,-1,-1,-10,-2,-9,7,-10,1,-8,-3,-7,4,-4,1,4,-7,4,7,7,4,4,-9,-10,-10,9,-5,-2,8,3,-4,-1,-1,-10,-9,-2,3,4,-2,-4,3,6,2,6,-5,-9,5,1,5,8,6,-6,-8,3,-5,2,10,7,-7,-2,-1,3,-3,5,6,5,-5,-3,1,7,-4,-5,9,6,4,-8,3,2,8,5,3,5,10,5,5,7,-10,-4,6,-5,-10,-7,6,10,-9,5,-4,1,10,5,-7,5,-9,-6,-10,7,-4,4,6,-4,-8,8,-1,6,-5,9,7,9,4,3,4,6,6,10,2,8,4,2,7,1,2,5,-5,-7,8,2,10,4,6,10,7,-9,-4,-8,-8,-4,-8,-10,-3,-3,7,-5,-3,-4,2,-10,10,1,8,-8,10,-9,-10,5,-7,4,-4,-10,-7,-8,8,9,-5,5,-4,2,-4,-4,1,6,8,10,9,8,6,-7,4,-2,8,6,10,-6,8,-7,-1,-7,-4,-8,-8,-1,4,1,-5,1,-2,-5,-5,-5,3,2,-8,3,-5,-5,7,1,7,1,7,-3,-9,1,1,4,9,-10,-6,-9,1,-6,-1,4,-9,9,-7,2,3,7,-9,-10,1,-7,10,-8,9,3,-2,-9,-4,-6,-1,8,-4,-9,-7,3,-8,5,-4,1,8,5,-3,-1,-1,7,-5,-5,9,2,-3,-6,-5,9,5,-5,5,2,-2,-6,-2,-4,-9,6,3,6,6,6,-6,-3,4,3,-5,9,2,2,-8,10,5,5,-7,5,6,5,6,-10,-5,2,-2,9,6,-7,-8,-4,-5,5,4,5,1,10,9,10,7,-6,-2,-4,-8,7,-9,3,1,-8,-7,-3,-5,6,4,-10,5,-9,-10,-9,5,-6,-4,8,4,8,-1,10,5,1,-1,8,6,-6,2,7,-9,2,2,9,-6,-9,-2,-2,-6,-4,-6,2,-4,8,-4,-3,-8,6,-5,-5,-6,7,-5,2,-5,-6,-1,-1,-9,-10,6,3,10,-3,6,5,4,9,2,9,-8,-8,-5,3,-10,8,8,-9,3,-3,-1,1,10,-5,1,-2,10,7,1,-1,5,-8,-1,1,-8,-4,-3,-4,-5,9,-2,-5,1,8,-4,-4,8,-1,-8,6,-9,6,-5,6,9,8,-6,-4,6,2,2,-8,7,-3,4,-10,-8,-4,9,5,-7,1,-5,-2,-10,-3,-10,5,4,2,-7,-2,1,10,-8,-9,-9,10,-9,6,-9,-2,-2,6,-6,4,1,10,2,1,6,-6,-2,8,-9,9,-3,-8,-9,-9,-3,6,-8,5,8,-1,7,9,4,-1,2,-2,10,-10,-4,-3,1,-10,-8,9,4,10,9,-1,7,-7,-1,-3,-1,-1,1,4,5,-3,1,-7,-3,-6,-6,-5,-10,-1,-3,5,9,-3,-10,-4,-10,-8,-8,8,3,4,-5,-4,1,-8,-2,-2,-9,-3,9,5,-6,-2,9,-8,6,-4,10,5,-3,-8,4,-8,-5,3,2,-7,9,7,-1,-2,6,7,-4,-7,-7,-4,9,5,6,-1,-4,-9,8,-2,-10,6,-2,1,-7,-5,-7,7,-4,1,-10,8,-1,-8,-4,7,-7,-1,-6,-7,3,9,-2,8,-9,-5,1,3,-4,-8,1,4,8,9,6,-9,9,-10,6,-6,-7,6,-8,-10,9,-3,-3,10,-10,7,6,-6,-6,3,-4,-7,-4,1,-1,6,-8,2,-4,3,3,10,8,4,4,-3,10,1,4,-8,10,-9,-3,-10,-5,-10,4,10,8,3,-3,10,10,-7,-3,1,7,2,1,6,4,8,8,8,-2,-7,9,8,1,4,-8,-7,-7,4,10,7,6,2,1,-9,2,10,5,1,-1,2,-1,4,-8,7,-6,2,8,-3,3,-6,8,-8,-3,-1,-5,-4,1,-6,4,-9,-8,4,6,-8,9,-5,9,-2,-2,5,-5,4,6,-7,3,-3,-6,8,-6,2,-10,4,10,-2,-10,-8,7,-1,1,-5,3,-5,7,-2,10,8,-10,-9,-2,-3,-7,7,2,-7,7,7,-2,-10,6,1,5,7,-4,8,-9,-8,1,-2,-5,-5,-3,-10,-3,-3,4,8,-5,-7,-3,-7,-5,1,-10,8,-6,-8,5,3,10,-8,1,-4,-1,7,7,8,-9,-9,-6,6,9,-10,-4,4,-10,-8,10,-9,-2,-7,-10,-2,-6,8,7,-5,-8,5,-7,-3,1,9,-3,2,-5,-6,-4,4,9,-5,5,-7,2,-4,8,9,1,1,-6,-9,2,8,6,-9,3,3,1,-3,-9,5,6,-9,1,1,4,10,7,-3,1,8,-5,4,-9,10,-5,9,8,8,-9,7,-1,1,-7,1,-8,2,9,7,4,-8,-4,-10,-7,2,-9,1,-7,8,-7,-10,7,8,9,-6,5,-1,10,-1,-2,-3,3,-1,-6,-2,7,10,5,1,-3,4,10,-9,7,-9,5,9,8,6,-8,-9,-10,8,6,7,4,-9,9,7,8,-6,-8,8,-5,-9,3,-8,6,-10,5,4,-1,6,-1,-7,-6,9,-9,9,-3,7,-6,-1,-2,9,-8,-9,-5,10,-7,-4,-9,-9,2,-2,-6,-1,5,9,2,-5,10,-1,8,-3,-8,9,2,6,8,8,-9,8,-10,-1,4,5,1,-1,5,5,-10,1,-4,5,6,-6,4,-1,1,-9,10,-9,7,-2,-3,-8,-3,7,5,-1,-9,6,-3,8,-8,8,-2,-1,-8,-3,-9,-8,-9,10,-10,5,-8,-3,-9,-4,9,-7,3,-9,-8,-4,3,-7,-10,6,-8,9,3,6,4,-7,3,3,-1,-7,-7,5,-4,4,-1,-5,-1,-6,6,-4,-1,-3,-6,-8,-1,5,-7,-1,3,6,6,-3,-6,1,3,2,10,-8,-4,-3,-3,-6,-9,3,2,7,3,-7,1,10,-5,7,10,2,-4,-8,5,9,-10,-9,-2,-2,-6,-3,-9,10,9,-7,-3,-2,6,-3,-3,7,5,-10,2,-3,3,5,2,3,-3,10,-1,-2,-2,10,-9,1,-4,-4,-4,-5,6,-6,5,10,2,-5,-2,-2,4,-10,-10,1,-3,-8,-4,4,3,8,9,-6,-10,6,8,4,9,-6,-6,-2,-2,8,5,5,1,-6,3,-3,-4,3,-6,-7,3,-5,10,2,10,-9,-3,3,-8,-6,2,4,-10,-10,-7,3,-10,-3,-8,6,6,-2,-10,2,-3,-10,2,1,-2,8,9,9,2,2,6,7,-1,-10,-4,-10,-3,-2,-6,-6,-5,8,-8,3,-1,-1,3,9,-8,5,-3,1,-7,10,-7,2,1,-7,-8,-10,-7,6,-2,4,-5,-6,-5,-4,-9,6,9,9,7,-10,8,4,2,5,-6,-5,-7,-9,7,5,-8,-3,6,-8,2,7,-9,-7,-2,6,-9,-1,4,-9,3,-9,2,7,-6,2,-2,-9,-2,1,-7,4,-10,2,-2,6,-2,6,9,-3,-10,-2,-4,5,-7,1,-5,-10,9,2,-1,-9,-3,9,10,-6,7,-5,1,8,-8,2,6,-2,-1,6,-3,7,10,10,7,2,-6,-6,9,-4,3,-2,-5,-3,9,2,-2,9,-6,2,5,-7,3,7,-7,8,-7,10,5,10,-3,-7,1,7,-7,1,4,-4,-3], dtype = "uint16")#candidate|6579|(2340,)|const|uint16
var_6580 = relay.var("var_6580", dtype = "bool", shape = ())#candidate|6580|()|var|bool
call_6577 = relay.TupleGetItem(func_3049_call(relay.reshape(call_6572.astype('float32'), [12, 6, 10]), relay.reshape(const_6578.astype('float32'), [1152,]), relay.reshape(const_6579.astype('uint16'), [180, 13]), relay.reshape(var_6580.astype('bool'), []), ), 3)
call_6581 = relay.TupleGetItem(func_3055_call(relay.reshape(call_6572.astype('float32'), [12, 6, 10]), relay.reshape(const_6578.astype('float32'), [1152,]), relay.reshape(const_6579.astype('uint16'), [180, 13]), relay.reshape(var_6580.astype('bool'), []), ), 3)
func_1120_call = mod.get_global_var('func_1120')
func_1125_call = mutated_mod.get_global_var('func_1125')
const_6591 = relay.const([-9.784707,-7.336057,-7.321817,0.612095,0.201541,-8.086975,-3.335688,-9.372217,0.918201,2.023770,0.825234,-5.547272,-8.278227,-9.817343,-0.087329,-8.817681,0.838720,9.835231,-3.871080,-9.467144,1.922685,-6.090497,-9.937653,-2.354075,-3.490702,1.943751,-0.210262,8.041879,5.691686,-6.405952,-5.137607,9.551384,-4.963940,4.210877,8.171212,-7.608403,1.787720,5.102543,4.213144,1.342094,0.288702,2.323912,-2.259211,2.516012,-5.955833,-8.962660,-9.520784,1.415398,-8.165631,3.453887,-2.641777,-6.020733,-8.610239,-8.209280,-8.044120,-3.247261,-4.093193,7.397347,-6.856560,-1.429894,7.344389,2.435616,-7.785600,-4.572707,-8.099555,4.958160,7.224871,-3.936359,5.948518,8.704915,-5.458306,2.540099,-3.191761,-3.784104,7.172262,9.409094,7.549780,-8.528793,8.616579,-9.860386,-2.424755,8.011259,9.226166,-9.092331,-6.017431,-1.797851,3.960660,7.704583,5.659781,-3.890189,-6.294010,8.725810,-5.537234,-1.815130,-5.858148,1.781808,-0.546633,-1.150297,-2.869552,-5.273006,-9.338876,-1.438526,-7.059201,4.437187,0.303845,2.959372,-1.976769,7.663355,-8.616061,-8.578158,-1.749570,-7.114758,-7.131311,-0.081284,4.849638,3.948570,-8.763402,4.710311,3.045762,-8.022785,-6.579392,5.487234,-1.428952,7.097441,-6.433917,0.280238,-6.329186,5.034187,-7.591181,9.729038,-7.129518,1.886504,-2.624639,9.813498,-5.785891], dtype = "float32")#candidate|6591|(135,)|const|float32
const_6592 = relay.const([4,4,-6,-5,-6,2,5,-3,-5,-8,4,1,-1,-9,-8,10,-2,6,-9,-4,3,10,-3,2,9,-1,9,6,8,1,-8,10,3,7,-6,-9,-8,-6,2,-10,-9,6,4,-7,5,-8,9,2,-3,-6,-1,-9,-3,-1,4,-8,4,-8,3,-1,-3,1,9,6,4,5,6,-4,9,-6,9,-6,7,1,1,-8,5,8,5,-7,3,-4,-6,-10,4,-9,-1,5,-3,7,10,-10,-5,8,10,8,-9,-6,1,-1,-3,7,7,3,-10,-4,8,-5,2,-4,9,10,4,-3,4,-9,4,3,2,3,-8,2,3,-10,9,1,-8,7,7,-7,4,7,4,1,-8,7,1,6,5,1,2,5,3,9,2,10,-2,5,-7,-3,1,4,9,6,-6,9,8,-5,4,8,2,3,5,1,4,-8,5,-5,-2,8,9,-3,9,-8,3,-10,-6,-10,-1,-4], dtype = "uint16")#candidate|6592|(180,)|const|uint16
call_6590 = relay.TupleGetItem(func_1120_call(relay.reshape(const_6591.astype('float32'), [9, 1, 15]), relay.reshape(call_6577.astype('float32'), [1152,]), relay.reshape(const_6592.astype('uint16'), [180, 1]), ), 2)
call_6593 = relay.TupleGetItem(func_1125_call(relay.reshape(const_6591.astype('float32'), [9, 1, 15]), relay.reshape(call_6577.astype('float32'), [1152,]), relay.reshape(const_6592.astype('uint16'), [180, 1]), ), 2)
output = relay.Tuple([call_6572,call_6577,const_6578,const_6579,var_6580,call_6590,const_6591,const_6592,])
output2 = relay.Tuple([call_6573,call_6581,const_6578,const_6579,var_6580,call_6593,const_6591,const_6592,])
func_6594 = relay.Function([var_6580,], output)
mod['func_6594'] = func_6594
mod = relay.transform.InferType()(mod)
mutated_mod['func_6594'] = func_6594
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6595 = relay.var("var_6595", dtype = "bool", shape = ())#candidate|6595|()|var|bool
func_6594_call = mutated_mod.get_global_var('func_6594')
call_6596 = func_6594_call(var_6595)
output = call_6596
func_6597 = relay.Function([var_6595], output)
mutated_mod['func_6597'] = func_6597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3526_call = mod.get_global_var('func_3526')
func_3527_call = mutated_mod.get_global_var('func_3527')
call_6655 = relay.TupleGetItem(func_3526_call(), 6)
call_6656 = relay.TupleGetItem(func_3527_call(), 6)
func_4186_call = mod.get_global_var('func_4186')
func_4188_call = mutated_mod.get_global_var('func_4188')
call_6662 = relay.TupleGetItem(func_4186_call(), 0)
call_6663 = relay.TupleGetItem(func_4188_call(), 0)
output = relay.Tuple([call_6655,call_6662,])
output2 = relay.Tuple([call_6656,call_6663,])
func_6666 = relay.Function([], output)
mod['func_6666'] = func_6666
mod = relay.transform.InferType()(mod)
output = func_6666()
func_6667 = relay.Function([], output)
mutated_mod['func_6667'] = func_6667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mod.get_global_var('func_5807')
func_5808_call = mutated_mod.get_global_var('func_5808')
call_6706 = func_5807_call()
call_6707 = func_5807_call()
output = call_6706
output2 = call_6707
func_6710 = relay.Function([], output)
mod['func_6710'] = func_6710
mod = relay.transform.InferType()(mod)
output = func_6710()
func_6711 = relay.Function([], output)
mutated_mod['func_6711'] = func_6711
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6712 = relay.const([[[-3,-1,-2,-2,3,6,-2],[6,9,1,8,-1,-1,3],[-10,-1,7,-3,4,-8,1],[-9,-4,8,-6,-1,3,5],[8,3,-2,-3,8,-8,5],[1,1,9,-5,-9,8,-5],[1,6,-8,1,3,9,-2],[-6,-4,-5,7,10,-2,4],[8,10,9,-1,3,9,6],[9,-4,8,-10,-2,-8,-10],[9,10,-1,-9,6,-9,1],[-9,5,-8,-1,-6,-9,9],[-1,8,10,9,10,-6,-1]]], dtype = "int16")#candidate|6712|(1, 13, 7)|const|int16
var_6713 = relay.var("var_6713", dtype = "int16", shape = (3, 13, 7))#candidate|6713|(3, 13, 7)|var|int16
bop_6714 = relay.left_shift(const_6712.astype('int16'), var_6713.astype('int16')) # shape=(3, 13, 7)
func_1295_call = mod.get_global_var('func_1295')
func_1301_call = mutated_mod.get_global_var('func_1301')
var_6732 = relay.var("var_6732", dtype = "float32", shape = (286,))#candidate|6732|(286,)|var|float32
var_6733 = relay.var("var_6733", dtype = "uint16", shape = (180, 1))#candidate|6733|(180, 1)|var|uint16
const_6734 = relay.const(False, dtype = "bool")#candidate|6734|()|const|bool
const_6735 = relay.const([True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False], dtype = "bool")#candidate|6735|(1404,)|const|bool
call_6731 = relay.TupleGetItem(func_1295_call(relay.reshape(var_6732.astype('float32'), [2, 13, 11]), relay.reshape(var_6733.astype('uint16'), [180,]), relay.reshape(const_6734.astype('bool'), []), relay.reshape(const_6735.astype('bool'), [12, 9, 13]), ), 10)
call_6736 = relay.TupleGetItem(func_1301_call(relay.reshape(var_6732.astype('float32'), [2, 13, 11]), relay.reshape(var_6733.astype('uint16'), [180,]), relay.reshape(const_6734.astype('bool'), []), relay.reshape(const_6735.astype('bool'), [12, 9, 13]), ), 10)
bop_6738 = relay.right_shift(var_6733.astype('int64'), const_6735.astype('int64')) # shape=(180, 1404)
output = relay.Tuple([bop_6714,call_6731,var_6732,const_6734,bop_6738,])
output2 = relay.Tuple([bop_6714,call_6736,var_6732,const_6734,bop_6738,])
func_6741 = relay.Function([var_6713,var_6732,var_6733,], output)
mod['func_6741'] = func_6741
mod = relay.transform.InferType()(mod)
var_6742 = relay.var("var_6742", dtype = "int16", shape = (3, 13, 7))#candidate|6742|(3, 13, 7)|var|int16
var_6743 = relay.var("var_6743", dtype = "float32", shape = (286,))#candidate|6743|(286,)|var|float32
var_6744 = relay.var("var_6744", dtype = "uint16", shape = (180, 1))#candidate|6744|(180, 1)|var|uint16
output = func_6741(var_6742,var_6743,var_6744,)
func_6745 = relay.Function([var_6742,var_6743,var_6744,], output)
mutated_mod['func_6745'] = func_6745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4071_call = mod.get_global_var('func_4071')
func_4072_call = mutated_mod.get_global_var('func_4072')
call_6843 = relay.TupleGetItem(func_4071_call(), 0)
call_6844 = relay.TupleGetItem(func_4072_call(), 0)
func_5705_call = mod.get_global_var('func_5705')
func_5709_call = mutated_mod.get_global_var('func_5709')
var_6848 = relay.var("var_6848", dtype = "bool", shape = (20, 1))#candidate|6848|(20, 1)|var|bool
var_6849 = relay.var("var_6849", dtype = "bool", shape = (50, 4))#candidate|6849|(50, 4)|var|bool
call_6847 = relay.TupleGetItem(func_5705_call(relay.reshape(var_6848.astype('bool'), [1, 2, 10]), relay.reshape(var_6849.astype('bool'), [10, 2, 10]), ), 1)
call_6850 = relay.TupleGetItem(func_5709_call(relay.reshape(var_6848.astype('bool'), [1, 2, 10]), relay.reshape(var_6849.astype('bool'), [10, 2, 10]), ), 1)
func_2860_call = mod.get_global_var('func_2860')
func_2862_call = mutated_mod.get_global_var('func_2862')
call_6852 = relay.TupleGetItem(func_2860_call(), 0)
call_6853 = relay.TupleGetItem(func_2862_call(), 0)
func_5705_call = mod.get_global_var('func_5705')
func_5709_call = mutated_mod.get_global_var('func_5709')
call_6861 = relay.TupleGetItem(func_5705_call(relay.reshape(var_6848.astype('bool'), [1, 2, 10]), relay.reshape(var_6849.astype('bool'), [10, 2, 10]), ), 1)
call_6862 = relay.TupleGetItem(func_5709_call(relay.reshape(var_6848.astype('bool'), [1, 2, 10]), relay.reshape(var_6849.astype('bool'), [10, 2, 10]), ), 1)
output = relay.Tuple([call_6843,call_6847,var_6848,var_6849,call_6852,call_6861,])
output2 = relay.Tuple([call_6844,call_6850,var_6848,var_6849,call_6853,call_6862,])
func_6866 = relay.Function([var_6848,var_6849,], output)
mod['func_6866'] = func_6866
mod = relay.transform.InferType()(mod)
mutated_mod['func_6866'] = func_6866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6866_call = mutated_mod.get_global_var('func_6866')
var_6868 = relay.var("var_6868", dtype = "bool", shape = (20, 1))#candidate|6868|(20, 1)|var|bool
var_6869 = relay.var("var_6869", dtype = "bool", shape = (50, 4))#candidate|6869|(50, 4)|var|bool
call_6867 = func_6866_call(var_6868,var_6869,)
output = call_6867
func_6870 = relay.Function([var_6868,var_6869,], output)
mutated_mod['func_6870'] = func_6870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6710_call = mod.get_global_var('func_6710')
func_6711_call = mutated_mod.get_global_var('func_6711')
call_6887 = func_6710_call()
call_6888 = func_6710_call()
output = relay.Tuple([call_6887,])
output2 = relay.Tuple([call_6888,])
func_6911 = relay.Function([], output)
mod['func_6911'] = func_6911
mod = relay.transform.InferType()(mod)
output = func_6911()
func_6912 = relay.Function([], output)
mutated_mod['func_6912'] = func_6912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5668_call = mod.get_global_var('func_5668')
func_5669_call = mutated_mod.get_global_var('func_5669')
call_6936 = func_5668_call()
call_6937 = func_5668_call()
output = call_6936
output2 = call_6937
func_6945 = relay.Function([], output)
mod['func_6945'] = func_6945
mod = relay.transform.InferType()(mod)
output = func_6945()
func_6946 = relay.Function([], output)
mutated_mod['func_6946'] = func_6946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6666_call = mod.get_global_var('func_6666')
func_6667_call = mutated_mod.get_global_var('func_6667')
call_6952 = relay.TupleGetItem(func_6666_call(), 0)
call_6953 = relay.TupleGetItem(func_6667_call(), 0)
func_6348_call = mod.get_global_var('func_6348')
func_6350_call = mutated_mod.get_global_var('func_6350')
var_6955 = relay.var("var_6955", dtype = "bool", shape = (200,))#candidate|6955|(200,)|var|bool
call_6954 = relay.TupleGetItem(func_6348_call(relay.reshape(var_6955.astype('bool'), [50, 4])), 0)
call_6956 = relay.TupleGetItem(func_6350_call(relay.reshape(var_6955.astype('bool'), [50, 4])), 0)
func_2263_call = mod.get_global_var('func_2263')
func_2266_call = mutated_mod.get_global_var('func_2266')
var_6959 = relay.var("var_6959", dtype = "uint16", shape = (180,))#candidate|6959|(180,)|var|uint16
call_6958 = relay.TupleGetItem(func_2263_call(relay.reshape(var_6959.astype('uint16'), [180,])), 1)
call_6960 = relay.TupleGetItem(func_2266_call(relay.reshape(var_6959.astype('uint16'), [180,])), 1)
output = relay.Tuple([call_6952,call_6954,var_6955,call_6958,var_6959,])
output2 = relay.Tuple([call_6953,call_6956,var_6955,call_6960,var_6959,])
func_6969 = relay.Function([var_6955,var_6959,], output)
mod['func_6969'] = func_6969
mod = relay.transform.InferType()(mod)
mutated_mod['func_6969'] = func_6969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6969_call = mutated_mod.get_global_var('func_6969')
var_6971 = relay.var("var_6971", dtype = "bool", shape = (200,))#candidate|6971|(200,)|var|bool
var_6972 = relay.var("var_6972", dtype = "uint16", shape = (180,))#candidate|6972|(180,)|var|uint16
call_6970 = func_6969_call(var_6971,var_6972,)
output = call_6970
func_6973 = relay.Function([var_6971,var_6972,], output)
mutated_mod['func_6973'] = func_6973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_6978 = relay.TupleGetItem(func_4699_call(), 1)
call_6979 = relay.TupleGetItem(func_4701_call(), 1)
output = call_6978
output2 = call_6979
func_6996 = relay.Function([], output)
mod['func_6996'] = func_6996
mod = relay.transform.InferType()(mod)
output = func_6996()
func_6997 = relay.Function([], output)
mutated_mod['func_6997'] = func_6997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3981_call = mod.get_global_var('func_3981')
func_3982_call = mutated_mod.get_global_var('func_3982')
call_7029 = relay.TupleGetItem(func_3981_call(), 0)
call_7030 = relay.TupleGetItem(func_3982_call(), 0)
func_4982_call = mod.get_global_var('func_4982')
func_4984_call = mutated_mod.get_global_var('func_4984')
call_7031 = relay.TupleGetItem(func_4982_call(), 0)
call_7032 = relay.TupleGetItem(func_4984_call(), 0)
func_5830_call = mod.get_global_var('func_5830')
func_5831_call = mutated_mod.get_global_var('func_5831')
call_7033 = relay.TupleGetItem(func_5830_call(), 0)
call_7034 = relay.TupleGetItem(func_5831_call(), 0)
output = relay.Tuple([call_7029,call_7031,call_7033,])
output2 = relay.Tuple([call_7030,call_7032,call_7034,])
func_7039 = relay.Function([], output)
mod['func_7039'] = func_7039
mod = relay.transform.InferType()(mod)
mutated_mod['func_7039'] = func_7039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7039_call = mutated_mod.get_global_var('func_7039')
call_7040 = func_7039_call()
output = call_7040
func_7041 = relay.Function([], output)
mutated_mod['func_7041'] = func_7041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6511_call = mod.get_global_var('func_6511')
func_6513_call = mutated_mod.get_global_var('func_6513')
call_7075 = relay.TupleGetItem(func_6511_call(), 0)
call_7076 = relay.TupleGetItem(func_6513_call(), 0)
output = call_7075
output2 = call_7076
func_7077 = relay.Function([], output)
mod['func_7077'] = func_7077
mod = relay.transform.InferType()(mod)
output = func_7077()
func_7078 = relay.Function([], output)
mutated_mod['func_7078'] = func_7078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7039_call = mod.get_global_var('func_7039')
func_7041_call = mutated_mod.get_global_var('func_7041')
call_7087 = relay.TupleGetItem(func_7039_call(), 2)
call_7088 = relay.TupleGetItem(func_7041_call(), 2)
output = call_7087
output2 = call_7088
func_7089 = relay.Function([], output)
mod['func_7089'] = func_7089
mod = relay.transform.InferType()(mod)
output = func_7089()
func_7090 = relay.Function([], output)
mutated_mod['func_7090'] = func_7090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3669_call = mod.get_global_var('func_3669')
func_3671_call = mutated_mod.get_global_var('func_3671')
call_7091 = relay.TupleGetItem(func_3669_call(), 1)
call_7092 = relay.TupleGetItem(func_3671_call(), 1)
uop_7101 = relay.atan(call_7091.astype('float64')) # shape=(180,)
uop_7103 = relay.atan(call_7092.astype('float64')) # shape=(180,)
output = uop_7101
output2 = uop_7103
func_7110 = relay.Function([], output)
mod['func_7110'] = func_7110
mod = relay.transform.InferType()(mod)
mutated_mod['func_7110'] = func_7110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7110_call = mutated_mod.get_global_var('func_7110')
call_7111 = func_7110_call()
output = call_7111
func_7112 = relay.Function([], output)
mutated_mod['func_7112'] = func_7112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5668_call = mod.get_global_var('func_5668')
func_5669_call = mutated_mod.get_global_var('func_5669')
call_7126 = func_5668_call()
call_7127 = func_5668_call()
output = call_7126
output2 = call_7127
func_7129 = relay.Function([], output)
mod['func_7129'] = func_7129
mod = relay.transform.InferType()(mod)
mutated_mod['func_7129'] = func_7129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7129_call = mutated_mod.get_global_var('func_7129')
call_7130 = func_7129_call()
output = call_7130
func_7131 = relay.Function([], output)
mutated_mod['func_7131'] = func_7131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5830_call = mod.get_global_var('func_5830')
func_5831_call = mutated_mod.get_global_var('func_5831')
call_7134 = relay.TupleGetItem(func_5830_call(), 0)
call_7135 = relay.TupleGetItem(func_5831_call(), 0)
output = relay.Tuple([call_7134,])
output2 = relay.Tuple([call_7135,])
func_7142 = relay.Function([], output)
mod['func_7142'] = func_7142
mod = relay.transform.InferType()(mod)
mutated_mod['func_7142'] = func_7142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7142_call = mutated_mod.get_global_var('func_7142')
call_7143 = func_7142_call()
output = call_7143
func_7144 = relay.Function([], output)
mutated_mod['func_7144'] = func_7144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4071_call = mod.get_global_var('func_4071')
func_4072_call = mutated_mod.get_global_var('func_4072')
call_7186 = relay.TupleGetItem(func_4071_call(), 0)
call_7187 = relay.TupleGetItem(func_4072_call(), 0)
output = call_7186
output2 = call_7187
func_7199 = relay.Function([], output)
mod['func_7199'] = func_7199
mod = relay.transform.InferType()(mod)
mutated_mod['func_7199'] = func_7199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7199_call = mutated_mod.get_global_var('func_7199')
call_7200 = func_7199_call()
output = call_7200
func_7201 = relay.Function([], output)
mutated_mod['func_7201'] = func_7201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_7210 = func_7077_call()
call_7211 = func_7077_call()
func_7142_call = mod.get_global_var('func_7142')
func_7144_call = mutated_mod.get_global_var('func_7144')
call_7231 = relay.TupleGetItem(func_7142_call(), 0)
call_7232 = relay.TupleGetItem(func_7144_call(), 0)
output = relay.Tuple([call_7210,call_7231,])
output2 = relay.Tuple([call_7211,call_7232,])
func_7236 = relay.Function([], output)
mod['func_7236'] = func_7236
mod = relay.transform.InferType()(mod)
output = func_7236()
func_7237 = relay.Function([], output)
mutated_mod['func_7237'] = func_7237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6911_call = mod.get_global_var('func_6911')
func_6912_call = mutated_mod.get_global_var('func_6912')
call_7298 = relay.TupleGetItem(func_6911_call(), 0)
call_7299 = relay.TupleGetItem(func_6912_call(), 0)
output = relay.Tuple([call_7298,])
output2 = relay.Tuple([call_7299,])
func_7313 = relay.Function([], output)
mod['func_7313'] = func_7313
mod = relay.transform.InferType()(mod)
output = func_7313()
func_7314 = relay.Function([], output)
mutated_mod['func_7314'] = func_7314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7129_call = mod.get_global_var('func_7129')
func_7131_call = mutated_mod.get_global_var('func_7131')
call_7323 = func_7129_call()
call_7324 = func_7129_call()
output = relay.Tuple([call_7323,])
output2 = relay.Tuple([call_7324,])
func_7360 = relay.Function([], output)
mod['func_7360'] = func_7360
mod = relay.transform.InferType()(mod)
output = func_7360()
func_7361 = relay.Function([], output)
mutated_mod['func_7361'] = func_7361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7199_call = mod.get_global_var('func_7199')
func_7201_call = mutated_mod.get_global_var('func_7201')
call_7402 = func_7199_call()
call_7403 = func_7199_call()
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_7413 = func_2502_call()
call_7414 = func_2502_call()
output = relay.Tuple([call_7402,call_7413,])
output2 = relay.Tuple([call_7403,call_7414,])
func_7416 = relay.Function([], output)
mod['func_7416'] = func_7416
mod = relay.transform.InferType()(mod)
output = func_7416()
func_7417 = relay.Function([], output)
mutated_mod['func_7417'] = func_7417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3669_call = mod.get_global_var('func_3669')
func_3671_call = mutated_mod.get_global_var('func_3671')
call_7445 = relay.TupleGetItem(func_3669_call(), 3)
call_7446 = relay.TupleGetItem(func_3671_call(), 3)
output = call_7445
output2 = call_7446
func_7479 = relay.Function([], output)
mod['func_7479'] = func_7479
mod = relay.transform.InferType()(mod)
output = func_7479()
func_7480 = relay.Function([], output)
mutated_mod['func_7480'] = func_7480
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7509 = relay.var("var_7509", dtype = "float32", shape = ())#candidate|7509|()|var|float32
var_7510 = relay.var("var_7510", dtype = "float32", shape = (1, 10, 4))#candidate|7510|(1, 10, 4)|var|float32
bop_7511 = relay.maximum(var_7509.astype('float32'), var_7510.astype('float32')) # shape=(1, 10, 4)
func_6911_call = mod.get_global_var('func_6911')
func_6912_call = mutated_mod.get_global_var('func_6912')
call_7517 = relay.TupleGetItem(func_6911_call(), 0)
call_7518 = relay.TupleGetItem(func_6912_call(), 0)
func_6570_call = mod.get_global_var('func_6570')
func_6571_call = mutated_mod.get_global_var('func_6571')
call_7522 = relay.TupleGetItem(func_6570_call(), 1)
call_7523 = relay.TupleGetItem(func_6571_call(), 1)
uop_7553 = relay.sqrt(var_7510.astype('float32')) # shape=(1, 10, 4)
bop_7556 = relay.logical_and(uop_7553.astype('bool'), relay.reshape(bop_7511.astype('bool'), relay.shape_of(uop_7553))) # shape=(1, 10, 4)
output = relay.Tuple([call_7517,call_7522,bop_7556,])
output2 = relay.Tuple([call_7518,call_7523,bop_7556,])
func_7565 = relay.Function([var_7509,var_7510,], output)
mod['func_7565'] = func_7565
mod = relay.transform.InferType()(mod)
var_7566 = relay.var("var_7566", dtype = "float32", shape = ())#candidate|7566|()|var|float32
var_7567 = relay.var("var_7567", dtype = "float32", shape = (1, 10, 4))#candidate|7567|(1, 10, 4)|var|float32
output = func_7565(var_7566,var_7567,)
func_7568 = relay.Function([var_7566,var_7567,], output)
mutated_mod['func_7568'] = func_7568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4905_call = mod.get_global_var('func_4905')
func_4907_call = mutated_mod.get_global_var('func_4907')
call_7589 = relay.TupleGetItem(func_4905_call(), 0)
call_7590 = relay.TupleGetItem(func_4907_call(), 0)
func_4572_call = mod.get_global_var('func_4572')
func_4577_call = mutated_mod.get_global_var('func_4577')
var_7605 = relay.var("var_7605", dtype = "bool", shape = (7, 70))#candidate|7605|(7, 70)|var|bool
const_7606 = relay.const(-2, dtype = "int32")#candidate|7606|()|const|int32
const_7607 = relay.const([[-5.467184,6.924884,9.848143,4.878523,-2.074262,9.156798,-2.402347,-3.911101,8.616782,-7.072123,7.561344,-6.384511,3.051338],[-6.860512,9.434272,-4.272135,6.148660,-5.296848,5.833725,-6.876337,3.100240,3.903693,8.545290,8.540362,6.011170,-2.655896],[9.155888,-7.658706,-9.682231,-3.244903,-4.095410,5.715003,-7.173684,-0.957282,7.936858,8.690966,-0.358554,7.020994,3.305660],[-8.493038,-2.478666,1.510639,2.080427,2.098044,8.047655,5.765947,-8.527923,2.594299,6.735903,4.257966,-0.049457,7.425974],[5.418958,6.691516,8.060484,4.248647,-0.089660,4.482607,-3.833118,7.739151,-7.582234,6.948221,3.885934,-1.078748,4.631960],[7.313652,-3.647517,-3.934026,6.274427,-3.418910,-4.416288,7.279368,8.921591,-1.873214,2.977182,8.081380,3.295090,-3.308774],[4.727242,4.281701,-6.929876,0.347152,5.455127,-7.258298,0.182007,2.888280,-5.712535,-6.419991,-6.609287,7.156891,-7.952722],[1.992474,-2.725209,-0.166600,-2.431736,-8.842150,-0.840428,-5.449918,2.599842,4.320947,8.788794,-7.472741,2.019742,5.568051],[-2.866601,8.593769,6.202989,-7.422744,-2.400762,-5.840369,-9.047936,-7.982909,-1.850385,-6.509410,1.655509,-2.816128,-3.569401],[3.958002,5.485510,3.240283,1.708598,-9.048925,-7.478526,-8.613394,8.046690,2.489446,7.422965,-4.386147,-6.726278,-8.666938],[-9.912581,0.889886,5.258825,-6.999967,5.958865,-5.388172,-6.895282,-3.811391,3.488787,-5.452447,8.957743,-0.469100,9.848480],[-1.284104,1.584439,0.618112,2.088029,2.320588,2.346489,0.291439,0.421482,-5.046183,-8.407324,-8.319971,5.269377,-5.400767],[9.593178,-5.749633,0.476075,-6.803218,1.571846,6.457632,-8.338050,0.493464,-3.168284,6.524544,1.049394,-1.589880,-1.952450],[6.154845,9.576142,-8.567647,6.099660,3.122057,2.900426,4.989991,8.644042,5.824843,1.266060,-7.672561,6.896730,-4.229293],[5.662340,-5.254701,0.590459,0.694040,8.742022,7.813490,-1.885403,8.153644,8.121864,-6.908190,9.193237,-2.803105,0.519523],[2.838736,-8.472344,3.858678,-6.484671,2.498115,0.729943,-3.207185,-8.055368,9.167572,-8.382842,-5.464190,-8.633370,-1.867357],[-4.106679,-1.109745,1.317396,-4.658526,3.025519,9.417856,4.593095,-0.084850,-1.499320,3.561274,-0.902917,0.571996,-9.750420],[-6.986230,0.676187,-9.298460,-8.574451,9.587708,-8.535939,0.271381,6.297901,6.195263,-9.334170,8.629535,-3.743687,0.582805],[-9.880604,9.659296,2.977838,3.184667,2.583661,-0.445091,-8.702499,6.966502,-9.655795,9.635483,-5.612450,-9.486879,-5.355258],[3.490123,9.229581,1.729333,2.630463,-7.141022,7.807238,9.548850,1.061379,-9.866221,6.501185,7.317176,-4.431724,4.665930],[1.547129,8.976736,-8.055629,3.690063,-0.410674,5.572494,2.325061,-8.347709,7.119885,2.278857,1.881404,-2.916331,-9.171860],[-2.734945,-1.730725,5.572893,-5.816898,9.044286,3.960640,-0.733860,-4.808947,4.895863,1.951596,-9.165028,-0.881466,0.421739],[7.666086,-7.238228,4.463186,-0.922037,5.038374,-3.345063,1.665288,-9.381706,-8.236366,-8.345527,-9.808737,-8.922417,3.587305],[-4.153806,9.356058,7.901145,3.622541,-0.486446,3.520432,7.110874,-1.502040,-6.281444,8.809442,-3.845117,9.108953,-3.977936],[-4.433863,5.434487,7.348160,2.357876,3.830476,7.313554,9.742747,-1.865669,3.541674,2.840208,6.105919,1.813894,-3.189504],[-9.155721,-4.573259,5.711965,3.648923,-7.537835,-7.137311,8.975365,-3.101449,-8.703607,-7.263882,-2.717020,-4.577908,0.980903],[7.777068,6.334922,-3.846656,3.923501,-1.498083,-0.053918,5.267395,9.248832,-6.597576,-4.114934,8.802752,-5.258644,3.493052],[2.451247,-1.554604,7.303212,5.473117,3.788347,-6.478743,-1.058708,9.933480,-2.258275,3.606205,-0.434198,2.815162,5.314284],[-7.306814,-0.933660,-3.142079,9.537274,5.490941,9.422502,6.168275,-3.668017,6.255263,8.607685,8.483337,-3.656708,7.648705],[5.056964,6.254873,6.179107,-4.504481,9.175591,-0.037551,-7.696189,5.239285,-0.352793,-6.871391,-9.467219,-6.788985,5.602665],[6.001314,-7.024656,-2.733762,7.187001,-3.130939,1.454392,4.714634,-3.519016,-7.922148,9.932870,-6.883797,-3.221727,-1.762312],[-1.795756,-7.258492,2.112790,9.440617,-7.417928,2.359214,1.958153,8.720115,-6.707903,2.214074,-7.429934,1.356659,3.756782],[9.898814,4.843633,-6.110892,-0.527896,8.493222,2.888279,-8.444685,-6.906192,1.888231,4.983296,4.639234,2.914884,-4.608403],[-9.970810,4.499744,4.529235,3.521474,2.644005,7.299587,5.249891,8.871260,6.839451,-8.653784,7.339368,-0.574447,-3.696676],[-8.274066,-6.619187,5.177191,4.786240,5.541229,-2.479136,6.666866,-7.158107,7.502224,1.269324,-3.327239,-6.039377,-3.892342],[4.540759,0.948848,-8.881078,1.726207,-3.873391,2.877838,-1.069385,2.416550,-5.656239,-2.849121,4.931310,-6.905448,-4.954388],[9.069654,2.323855,-9.429377,-1.887110,2.478984,7.951033,-5.854512,5.870396,2.152271,-6.223607,-3.938355,7.577219,0.825185],[1.316009,0.606724,1.403839,-1.118927,9.040379,0.045187,-4.702941,-2.375183,7.068101,-3.271136,2.892295,-3.740479,-6.877609],[-1.067684,4.165846,-5.981963,7.445401,-3.242261,-2.790109,6.954093,6.558596,-7.105188,5.035248,-3.422536,4.050146,-4.616761],[-1.496565,-4.262202,8.726792,2.268363,-2.551369,6.294388,9.875276,-3.396905,1.507202,7.056529,-8.229369,-4.269207,9.986203],[6.782641,7.503540,4.014559,-0.984455,-3.531826,-0.169246,1.689149,3.185384,-9.323553,-0.154249,9.414418,-0.412240,1.143430],[-1.241837,8.208166,-1.470382,-8.864303,-8.084094,5.321311,9.405268,-5.262077,2.068704,-7.363882,5.124219,-9.584963,-0.154302],[0.159335,-2.728028,8.192756,-1.580868,-0.701547,3.209571,6.769648,-8.792458,0.191115,-0.580806,5.367710,4.662968,2.584828],[-3.463687,-0.503034,5.224844,-8.875856,-9.678359,-4.774345,-7.007825,2.483612,4.262092,2.591010,-2.036375,7.942953,-3.032839],[-1.461217,-7.970417,-0.309758,8.849167,0.791718,-5.688948,6.982113,-1.672138,-1.936608,-2.259214,-2.206209,-1.656767,-4.129245],[-0.485333,0.939093,-6.652619,-1.168929,7.219848,-2.887704,-4.542305,4.040691,4.072847,9.077376,-0.127685,-7.418859,-1.034516],[-6.515997,-0.931245,0.765460,-3.692058,9.037813,-9.377873,-7.353602,5.938652,6.526317,-4.410827,-4.200672,8.656516,7.172631],[0.135621,-1.347889,2.993931,-4.971414,8.510326,-2.465976,1.319181,5.304755,-0.253746,1.443835,-7.765425,6.400471,-6.701924],[-0.031063,5.649459,8.628198,3.109033,-2.653454,6.735816,-4.251780,-3.369593,-0.228411,-3.790902,-3.400368,6.461847,-6.211903],[-0.223176,8.287552,-9.766509,-7.545091,3.674689,-0.532465,1.162965,6.620356,-3.663928,-8.613189,5.517324,-0.012672,-7.952951],[-1.649235,-9.853215,8.528782,-4.694315,0.983368,-6.897838,-9.512422,-4.893083,-0.831543,-1.810841,-1.539808,2.970162,2.343405],[5.256027,-1.768323,-7.499933,-1.212830,-5.173524,4.991035,-4.252925,1.737909,-2.084433,-2.044501,-9.966204,0.448863,8.217049],[1.859972,-4.529508,2.339606,-9.555688,3.136013,-3.383164,-2.298764,3.014294,2.682802,-3.396784,-9.102391,-5.536008,9.138618],[9.446078,2.596152,-6.214430,7.880884,-5.746263,1.076901,-6.666016,0.446409,-2.910856,3.632057,-1.174531,8.701511,5.958066],[9.196782,-0.412901,8.110180,6.778205,-5.882258,4.411766,-2.551273,-7.125811,9.328314,-9.679079,7.409961,-2.911118,-7.470255],[8.127573,6.002485,3.057999,5.891322,-3.116869,0.920721,2.827137,5.609320,4.200217,-8.036245,8.362558,9.446520,4.151924],[-0.983598,6.117480,-4.916104,-9.038138,-3.061591,-9.351602,-2.286925,-7.172261,0.297561,1.775760,-6.833722,-2.004719,7.105409],[-9.696251,-9.764959,0.760131,8.555688,5.076500,-8.854822,-1.305588,-6.028949,-7.750305,7.871293,-5.203598,-0.610590,3.934704],[9.889701,-4.407042,-2.044136,0.157448,-8.415200,4.873988,0.980189,0.591311,2.541088,-3.141362,-0.928770,-1.975895,3.672553],[-3.537569,-4.220826,4.292256,-0.774155,-4.851372,-2.989258,1.751114,8.348160,8.871843,4.331012,-8.392892,-2.948298,-4.207558],[7.533243,-2.617028,-4.435754,-8.201816,-3.848297,-2.183428,1.321150,5.067358,-7.708213,-1.188001,-0.821320,-8.002821,-0.529195],[-1.098207,-1.534032,-9.443259,6.019420,-4.002428,9.085401,-4.427103,-5.573212,-0.805092,-0.935010,-0.899839,-9.652808,-3.999570],[-7.278386,2.408132,2.061878,0.070861,-0.090019,7.247132,-9.756375,9.408526,-1.742956,7.602455,-3.378198,8.710689,-3.171417],[8.067822,-0.406789,8.204013,5.544777,-5.520915,-6.538380,-9.959080,2.103767,-9.221548,2.567424,0.420053,2.399942,2.261240],[3.580499,-7.745266,-4.111793,-5.966334,2.359628,8.884326,-6.793336,6.544455,7.419246,-8.930167,1.361429,-9.659751,-2.536261]], dtype = "float64")#candidate|7607|(65, 13)|const|float64
call_7604 = relay.TupleGetItem(func_4572_call(relay.reshape(var_7605.astype('bool'), [5, 14, 7]), relay.reshape(var_7605.astype('bool'), [5, 14, 7]), relay.reshape(const_7606.astype('int32'), []), relay.reshape(const_7607.astype('float64'), [845,]), ), 9)
call_7608 = relay.TupleGetItem(func_4577_call(relay.reshape(var_7605.astype('bool'), [5, 14, 7]), relay.reshape(var_7605.astype('bool'), [5, 14, 7]), relay.reshape(const_7606.astype('int32'), []), relay.reshape(const_7607.astype('float64'), [845,]), ), 9)
var_7614 = relay.var("var_7614", dtype = "float64", shape = (845,))#candidate|7614|(845,)|var|float64
bop_7615 = relay.equal(call_7604.astype('bool'), relay.reshape(var_7614.astype('bool'), relay.shape_of(call_7604))) # shape=(845,)
bop_7618 = relay.equal(call_7608.astype('bool'), relay.reshape(var_7614.astype('bool'), relay.shape_of(call_7608))) # shape=(845,)
output = relay.Tuple([call_7589,var_7605,const_7606,const_7607,bop_7615,])
output2 = relay.Tuple([call_7590,var_7605,const_7606,const_7607,bop_7618,])
func_7624 = relay.Function([var_7605,var_7614,], output)
mod['func_7624'] = func_7624
mod = relay.transform.InferType()(mod)
var_7625 = relay.var("var_7625", dtype = "bool", shape = (7, 70))#candidate|7625|(7, 70)|var|bool
var_7626 = relay.var("var_7626", dtype = "float64", shape = (845,))#candidate|7626|(845,)|var|float64
output = func_7624(var_7625,var_7626,)
func_7627 = relay.Function([var_7625,var_7626,], output)
mutated_mod['func_7627'] = func_7627
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7629 = relay.var("var_7629", dtype = "float64", shape = (3, 3, 2))#candidate|7629|(3, 3, 2)|var|float64
uop_7630 = relay.rsqrt(var_7629.astype('float64')) # shape=(3, 3, 2)
bop_7632 = relay.not_equal(var_7629.astype('bool'), relay.reshape(uop_7630.astype('bool'), relay.shape_of(var_7629))) # shape=(3, 3, 2)
func_4715_call = mod.get_global_var('func_4715')
func_4717_call = mutated_mod.get_global_var('func_4717')
call_7647 = relay.TupleGetItem(func_4715_call(), 0)
call_7648 = relay.TupleGetItem(func_4717_call(), 0)
output = relay.Tuple([bop_7632,call_7647,])
output2 = relay.Tuple([bop_7632,call_7648,])
func_7659 = relay.Function([var_7629,], output)
mod['func_7659'] = func_7659
mod = relay.transform.InferType()(mod)
mutated_mod['func_7659'] = func_7659
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7660 = relay.var("var_7660", dtype = "float64", shape = (3, 3, 2))#candidate|7660|(3, 3, 2)|var|float64
func_7659_call = mutated_mod.get_global_var('func_7659')
call_7661 = func_7659_call(var_7660)
output = call_7661
func_7662 = relay.Function([var_7660], output)
mutated_mod['func_7662'] = func_7662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3669_call = mod.get_global_var('func_3669')
func_3671_call = mutated_mod.get_global_var('func_3671')
call_7670 = relay.TupleGetItem(func_3669_call(), 2)
call_7671 = relay.TupleGetItem(func_3671_call(), 2)
var_7674 = relay.var("var_7674", dtype = "float32", shape = (1152,))#candidate|7674|(1152,)|var|float32
bop_7675 = relay.mod(call_7670.astype('float32'), relay.reshape(var_7674.astype('float32'), relay.shape_of(call_7670))) # shape=(1152,)
bop_7678 = relay.mod(call_7671.astype('float32'), relay.reshape(var_7674.astype('float32'), relay.shape_of(call_7671))) # shape=(1152,)
output = relay.Tuple([bop_7675,])
output2 = relay.Tuple([bop_7678,])
func_7693 = relay.Function([var_7674,], output)
mod['func_7693'] = func_7693
mod = relay.transform.InferType()(mod)
var_7694 = relay.var("var_7694", dtype = "float32", shape = (1152,))#candidate|7694|(1152,)|var|float32
output = func_7693(var_7694)
func_7695 = relay.Function([var_7694], output)
mutated_mod['func_7695'] = func_7695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5298_call = mod.get_global_var('func_5298')
func_5300_call = mutated_mod.get_global_var('func_5300')
call_7719 = relay.TupleGetItem(func_5298_call(), 0)
call_7720 = relay.TupleGetItem(func_5300_call(), 0)
const_7736 = relay.const([[[6.075198,-6.749082,4.129883,2.817611,-3.997737,-9.589357,1.465006,-4.412650,8.003098,0.359366],[4.974707,-5.987731,2.022640,-8.175113,8.544403,5.822606,-7.670891,6.811341,4.832857,9.423731],[-6.540031,5.818889,-8.048095,-1.148181,4.280107,-2.595977,1.205333,9.082219,5.646369,8.078442],[3.761646,8.593581,9.863004,-0.555296,6.608865,-6.387405,2.157601,8.106677,3.923938,-8.227375],[-7.409592,8.119395,6.462079,-1.560420,1.976585,-6.181172,-2.573336,-8.196373,-5.628726,3.535139],[-6.451517,9.008193,9.969877,6.374434,9.795037,-6.858280,-9.925786,5.921974,-3.852829,-9.937439]],[[-6.049142,-0.582239,-1.730053,-9.251760,1.116194,3.862166,4.862729,-9.663698,0.328482,3.550947],[9.101101,-5.230104,4.739297,5.160150,-6.635130,4.971187,-2.200954,9.946906,-0.063626,2.409595],[4.763412,0.006764,-7.314341,-1.730274,-8.359584,-9.221127,6.544192,9.127458,-9.666946,-4.241750],[4.577840,2.108867,1.240746,-9.518755,-2.723253,-6.126577,-6.037073,-5.528271,5.897567,4.747741],[-7.954783,7.289211,-0.620791,4.374162,1.831193,2.623464,8.052865,5.922674,-8.107989,7.067795],[9.652693,-2.721557,8.531138,-5.089171,8.911623,-7.590883,2.430678,5.559680,0.968544,2.187737]],[[-1.356700,7.174580,0.404850,5.780583,-0.881605,8.567711,-5.910856,-6.305521,-0.313646,-5.742963],[-3.737712,-5.850983,-7.164396,5.776683,-0.253697,-7.285015,-8.952784,-1.328425,-4.186411,9.660384],[-9.682181,7.390354,-7.811051,6.230514,-1.649246,1.246920,-3.736260,2.257152,2.095714,-6.796517],[5.836913,0.112823,-0.593461,0.023448,7.038570,-4.021406,0.586150,-7.692707,6.827615,3.624377],[4.025636,-7.461268,-2.500806,-4.241347,-3.899381,1.621372,1.629551,0.452331,-5.150247,4.580712],[6.631549,-1.591531,8.046143,6.004341,-3.547753,-0.321338,1.027321,0.581897,-8.493935,4.294620]],[[0.414343,-2.565249,1.195973,-7.199390,4.030280,4.881994,0.103329,2.861601,-7.313290,3.101462],[4.577709,-7.355404,-9.898806,-8.081710,4.164342,-5.515435,-8.379587,-0.031821,-9.290033,-2.516352],[-5.917957,2.394627,1.309638,-1.010788,2.032580,-7.569706,1.084336,2.680856,-7.781395,5.629649],[2.381001,-6.691897,-7.501810,-6.154351,-3.633842,-5.220883,-0.507214,-9.919099,6.800149,-6.812112],[8.998881,8.740757,4.570251,-9.581157,2.602220,-3.315804,8.294755,-5.100543,1.203220,2.913525],[9.917395,-9.856590,9.522899,2.672998,2.449919,2.601883,-8.745750,2.481628,9.242192,-1.917061]],[[2.106121,2.366952,2.204013,0.796213,-5.799380,-2.529840,-8.040761,-1.236393,-3.373318,-0.550681],[9.659268,-4.690068,3.332772,8.349198,2.939871,3.896706,-1.424872,-8.501711,-3.478636,-4.671392],[-0.201012,5.215288,1.230130,-8.156990,6.489187,4.408484,-5.093965,5.501275,-8.041017,-8.317693],[-1.950848,-6.809730,-5.388608,-0.134023,-4.633650,-5.534596,-1.391404,-7.460223,9.503963,3.196875],[9.364846,5.992748,-7.607604,8.366150,7.346072,-5.348720,0.447180,6.517275,9.647761,2.927463],[-2.067549,-1.638280,9.080452,5.509384,1.797560,0.972525,9.412095,-1.594323,9.145433,-4.308819]],[[7.146725,-6.068456,-7.677163,1.008308,-5.162775,7.921916,-0.106870,4.155397,-1.191424,-0.043403],[5.090484,0.264813,-2.125627,-1.247517,9.810207,-0.536953,2.512183,-0.306800,-8.269570,-4.758216],[-1.900434,-2.450480,8.108187,-8.424700,-0.256178,-8.922920,-9.239836,-2.137200,7.384583,0.371771],[-6.336804,-7.659697,-1.045705,6.973707,-0.420548,9.820677,0.790576,5.184356,7.527181,8.076413],[-3.975633,1.732155,0.314704,1.229197,-4.621112,2.383672,-6.559419,8.868307,-6.925427,-9.456841],[-4.265235,2.394460,3.007112,-5.711763,-1.426949,-4.523779,0.687737,-3.858512,9.702420,-2.253441]],[[-4.236700,-5.041277,6.977264,6.661230,-8.473185,-1.154522,-2.520814,3.495241,-1.451322,-0.190046],[7.302345,8.593579,7.534579,9.721125,6.161835,-5.714024,2.361824,-1.686456,-8.142306,2.963279],[8.889569,7.504971,0.749334,6.387659,1.737550,2.300437,-1.551813,7.391735,-6.300052,7.334629],[-8.509106,7.268613,-6.167738,-3.288886,5.877522,-0.780876,0.317224,-2.688300,-6.065412,-2.849461],[-6.156733,-5.023150,-3.405580,-4.186128,-0.687932,-4.328189,2.946637,-0.127362,-8.123404,7.247885],[-8.900605,-1.308447,9.710798,6.430248,5.496679,6.664792,7.113328,-1.331471,-6.366288,-0.771712]],[[-9.032429,3.580270,-0.704560,-6.852585,0.311099,-7.034582,4.800174,3.969249,-7.421267,-4.172706],[6.919098,7.603082,2.407994,-7.231062,-3.449774,-9.984474,-1.138508,-9.944386,0.083326,3.138483],[-4.382392,6.182241,-1.413749,3.804965,8.117144,-7.253192,8.579451,8.333479,-4.288474,-4.474603],[-8.550877,3.075057,0.825760,5.664209,-6.607640,2.012847,-8.764198,-1.453838,1.509539,4.771826],[2.648944,3.255137,8.166992,6.796228,4.521059,-4.574379,-5.405505,-4.248577,-3.079232,7.496978],[-3.110132,5.676571,9.312500,9.916708,8.699584,9.999327,4.086724,-2.242989,1.938532,-6.470301]],[[4.603337,-4.953511,-9.508526,2.509730,-9.518200,-8.777178,1.616060,8.139149,8.582347,-7.596122],[-2.656303,-0.764962,-0.948647,-8.273811,-8.243529,-0.969446,-8.723565,-9.855112,2.677100,9.722535],[-2.668347,-2.199448,0.991059,-1.299274,1.207726,-1.120598,-3.495447,4.431825,1.193632,-6.225056],[-4.278840,0.932726,3.078147,2.257661,-7.902315,-1.368391,-9.841901,-9.994074,-0.525064,7.837011],[6.172877,1.681902,-6.917938,9.882897,7.777956,1.522529,-3.239450,-9.578081,-5.808887,9.011409],[-9.028305,7.892720,-4.005161,-0.655432,-5.546325,-1.821433,0.896571,9.564503,-1.329262,0.649856]],[[-8.057124,5.718836,-0.120162,-5.484635,-4.333155,0.183848,5.829592,0.859376,-8.427470,7.414842],[9.654632,4.160942,1.560038,-1.601661,9.558408,9.481654,4.149555,-6.083767,-4.542305,-9.770215],[-4.458606,8.138522,6.667409,-1.386468,1.528667,-7.407426,1.591792,8.898258,8.981913,0.644773],[-5.511404,-1.766979,6.524296,3.424890,-2.880864,-0.687381,9.790433,-1.335033,5.169840,-5.239873],[-5.025011,3.405140,-3.071343,9.754688,8.639237,-9.067011,7.277032,5.858026,-4.403098,7.641618],[-7.464740,1.211130,6.550634,-1.834390,-5.255732,5.895755,-6.335035,1.948923,-7.131679,-8.864986]],[[5.426278,4.645078,2.455259,0.438258,6.266507,-0.239137,9.196385,9.274586,-2.037703,3.539692],[-8.207349,6.068947,2.627957,-4.145369,1.327194,4.910430,2.442796,-0.634018,6.006480,-4.103569],[-4.313991,1.395136,1.327119,-5.027079,-4.000569,-5.775852,4.878787,2.889180,-1.327884,-8.990349],[-2.530998,-1.611571,-8.568166,4.017330,1.865249,-1.425706,-2.834785,0.487654,-8.775302,4.575213],[4.918434,7.482903,-0.087649,2.823654,-6.291412,-3.203070,-2.567246,4.310941,4.118735,-4.501543],[-3.545359,-4.870361,-0.340074,-1.396698,-4.768033,-2.373883,-1.909054,-7.944853,-1.763123,9.585356]],[[2.906955,-7.807634,8.609197,-7.279383,-3.456708,2.134149,1.645456,7.327605,3.394968,-0.843530],[-9.776606,6.702672,-2.773634,4.762764,3.888161,-5.309480,-0.766005,-8.013548,-3.847029,0.228465],[-6.302743,9.587060,-5.173034,6.962036,7.891834,6.990704,-6.360486,-6.987185,-5.792668,-8.493276],[-9.020808,-7.290016,7.363549,-1.024448,5.606441,-6.600281,-6.879867,8.772295,-2.117512,-7.059798],[-9.143888,4.466202,-5.595625,-3.704691,1.369327,4.321450,9.384645,4.493032,-6.888218,-0.402479],[6.100929,9.983531,-2.675680,-1.208744,-5.529900,-7.963924,5.442010,1.467970,9.441050,-8.454911]]], dtype = "float32")#candidate|7736|(12, 6, 10)|const|float32
bop_7737 = relay.bitwise_xor(call_7719.astype('uint64'), relay.reshape(const_7736.astype('uint64'), relay.shape_of(call_7719))) # shape=(12, 6, 10)
bop_7740 = relay.bitwise_xor(call_7720.astype('uint64'), relay.reshape(const_7736.astype('uint64'), relay.shape_of(call_7720))) # shape=(12, 6, 10)
output = bop_7737
output2 = bop_7740
func_7771 = relay.Function([], output)
mod['func_7771'] = func_7771
mod = relay.transform.InferType()(mod)
output = func_7771()
func_7772 = relay.Function([], output)
mutated_mod['func_7772'] = func_7772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3689_call = mod.get_global_var('func_3689')
func_3691_call = mutated_mod.get_global_var('func_3691')
call_7795 = func_3689_call()
call_7796 = func_3689_call()
output = relay.Tuple([call_7795,])
output2 = relay.Tuple([call_7796,])
func_7799 = relay.Function([], output)
mod['func_7799'] = func_7799
mod = relay.transform.InferType()(mod)
mutated_mod['func_7799'] = func_7799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7799_call = mutated_mod.get_global_var('func_7799')
call_7800 = func_7799_call()
output = call_7800
func_7801 = relay.Function([], output)
mutated_mod['func_7801'] = func_7801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4905_call = mod.get_global_var('func_4905')
func_4907_call = mutated_mod.get_global_var('func_4907')
call_7802 = relay.TupleGetItem(func_4905_call(), 0)
call_7803 = relay.TupleGetItem(func_4907_call(), 0)
func_2247_call = mod.get_global_var('func_2247')
func_2249_call = mutated_mod.get_global_var('func_2249')
var_7805 = relay.var("var_7805", dtype = "float32", shape = (1152,))#candidate|7805|(1152,)|var|float32
call_7804 = relay.TupleGetItem(func_2247_call(relay.reshape(var_7805.astype('float32'), [1152,])), 2)
call_7806 = relay.TupleGetItem(func_2249_call(relay.reshape(var_7805.astype('float32'), [1152,])), 2)
output = relay.Tuple([call_7802,call_7804,var_7805,])
output2 = relay.Tuple([call_7803,call_7806,var_7805,])
func_7811 = relay.Function([var_7805,], output)
mod['func_7811'] = func_7811
mod = relay.transform.InferType()(mod)
var_7812 = relay.var("var_7812", dtype = "float32", shape = (1152,))#candidate|7812|(1152,)|var|float32
output = func_7811(var_7812)
func_7813 = relay.Function([var_7812], output)
mutated_mod['func_7813'] = func_7813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3669_call = mod.get_global_var('func_3669')
func_3671_call = mutated_mod.get_global_var('func_3671')
call_7833 = relay.TupleGetItem(func_3669_call(), 3)
call_7834 = relay.TupleGetItem(func_3671_call(), 3)
uop_7854 = relay.atan(call_7833.astype('float32')) # shape=(1152,)
uop_7856 = relay.atan(call_7834.astype('float32')) # shape=(1152,)
output = uop_7854
output2 = uop_7856
func_7881 = relay.Function([], output)
mod['func_7881'] = func_7881
mod = relay.transform.InferType()(mod)
output = func_7881()
func_7882 = relay.Function([], output)
mutated_mod['func_7882'] = func_7882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2883_call = mod.get_global_var('func_2883')
func_2884_call = mutated_mod.get_global_var('func_2884')
call_7932 = relay.TupleGetItem(func_2883_call(), 0)
call_7933 = relay.TupleGetItem(func_2884_call(), 0)
func_3526_call = mod.get_global_var('func_3526')
func_3527_call = mutated_mod.get_global_var('func_3527')
call_7934 = relay.TupleGetItem(func_3526_call(), 8)
call_7935 = relay.TupleGetItem(func_3527_call(), 8)
var_7941 = relay.var("var_7941", dtype = "float32", shape = (1040,))#candidate|7941|(1040,)|var|float32
bop_7942 = relay.divide(call_7934.astype('float32'), relay.reshape(var_7941.astype('float32'), relay.shape_of(call_7934))) # shape=(1040,)
bop_7945 = relay.divide(call_7935.astype('float32'), relay.reshape(var_7941.astype('float32'), relay.shape_of(call_7935))) # shape=(1040,)
func_7039_call = mod.get_global_var('func_7039')
func_7041_call = mutated_mod.get_global_var('func_7041')
call_7948 = relay.TupleGetItem(func_7039_call(), 0)
call_7949 = relay.TupleGetItem(func_7041_call(), 0)
func_6710_call = mod.get_global_var('func_6710')
func_6711_call = mutated_mod.get_global_var('func_6711')
call_7959 = func_6710_call()
call_7960 = func_6710_call()
func_1295_call = mod.get_global_var('func_1295')
func_1301_call = mutated_mod.get_global_var('func_1301')
var_7969 = relay.var("var_7969", dtype = "float32", shape = (286,))#candidate|7969|(286,)|var|float32
const_7970 = relay.const([-3,-8,-8,-5,8,7,6,5,-9,1,-7,-9,3,-5,2,-9,-2,3,-2,1,8,1,8,-9,-10,-4,-5,5,9,-8,-7,-7,8,1,8,-3,3,-4,1,-9,-4,-7,-6,-6,4,7,3,-2,-3,2,-8,2,8,-2,9,-7,4,1,-8,-4,-1,6,4,6,5,-1,-2,2,-8,6,-6,8,10,-10,8,-3,-5,-4,8,-6,-7,-6,9,8,4,3,-10,-2,2,-9,5,1,10,7,-7,-3,-10,-5,6,-4,-9,10,8,8,-3,-2,8,6,-9,7,6,10,8,-2,-1,5,-5,-7,-7,5,-1,-8,-10,-8,7,-5,-5,10,-2,-10,-1,1,9,9,5,8,10,-5,-10,9,8,2,-9,-9,-7,4,-1,5,4,-10,9,5,1,2,-2,-9,-5,6,-5,6,1,9,-4,-3,-10,5,8,9,-1,1,1,6,2,1,4,-7,-7,8,-3,-10], dtype = "uint16")#candidate|7970|(180,)|const|uint16
var_7971 = relay.var("var_7971", dtype = "bool", shape = ())#candidate|7971|()|var|bool
var_7972 = relay.var("var_7972", dtype = "bool", shape = (1404,))#candidate|7972|(1404,)|var|bool
call_7968 = relay.TupleGetItem(func_1295_call(relay.reshape(var_7969.astype('float32'), [2, 13, 11]), relay.reshape(const_7970.astype('uint16'), [180,]), relay.reshape(var_7971.astype('bool'), []), relay.reshape(var_7972.astype('bool'), [12, 9, 13]), ), 9)
call_7973 = relay.TupleGetItem(func_1301_call(relay.reshape(var_7969.astype('float32'), [2, 13, 11]), relay.reshape(const_7970.astype('uint16'), [180,]), relay.reshape(var_7971.astype('bool'), []), relay.reshape(var_7972.astype('bool'), [12, 9, 13]), ), 9)
func_7199_call = mod.get_global_var('func_7199')
func_7201_call = mutated_mod.get_global_var('func_7201')
call_7985 = func_7199_call()
call_7986 = func_7199_call()
func_5603_call = mod.get_global_var('func_5603')
func_5606_call = mutated_mod.get_global_var('func_5606')
const_7989 = relay.const([[2,-4,-3],[3,-5,-8],[-1,10,10],[-8,5,4],[-3,3,-6],[4,-7,4],[1,6,4],[2,6,-9],[-10,-7,7],[5,8,9],[6,-3,2],[-3,-7,-6],[6,-8,-10],[7,6,-4],[-7,-4,-8],[-10,4,9],[3,10,2],[-2,-6,9],[9,-7,-1],[-9,-10,5],[4,2,1],[8,3,3],[-4,4,-5],[-7,10,-1],[-4,1,-1],[-4,4,-5],[-9,-8,-10],[10,5,-3],[8,7,5],[10,6,5],[-8,4,-5],[8,3,8],[8,-7,-5],[-3,2,2],[-6,7,4],[3,1,5],[-8,1,10],[5,1,-10],[2,-9,3],[-2,-4,3],[2,-1,3],[10,10,3],[3,7,-7],[10,10,4],[9,-2,-6],[2,-3,9],[-8,7,10],[-7,7,-9],[-10,-6,6],[-2,5,-9],[-1,6,-1],[-9,-6,6],[-8,1,8],[-2,6,-7],[-9,9,-4],[-6,9,-8],[9,-1,6],[2,-4,-1],[-2,-9,2],[-3,6,6],[2,7,-4],[-4,-4,9],[-6,-6,-6],[1,10,8],[-7,-7,-5],[-6,-5,-10],[10,3,3],[-4,6,1],[6,10,3],[2,-1,6],[-9,4,-3],[-4,-10,-7],[-10,-4,-2],[6,7,6],[6,-2,4],[-2,8,7],[-10,-6,-8],[5,-5,-4],[-6,-5,-8],[6,6,10],[6,2,-6],[9,2,8],[10,7,6],[4,-6,6],[-9,-8,2],[6,-10,6],[-9,-3,10],[-10,7,-8],[3,-5,-1],[2,5,9],[-10,5,-5],[-5,4,7],[7,8,9],[7,8,-8],[2,2,-10],[3,6,-9],[9,-7,-9],[-8,-2,-2],[-4,2,10],[-4,-9,-10],[-5,-10,-2],[-4,-2,5],[3,-10,2],[7,-1,-10],[10,3,-8]], dtype = "uint32")#candidate|7989|(105, 3)|const|uint32
call_7988 = relay.TupleGetItem(func_5603_call(relay.reshape(const_7989.astype('uint32'), [5, 9, 7])), 0)
call_7990 = relay.TupleGetItem(func_5606_call(relay.reshape(const_7989.astype('uint32'), [5, 9, 7])), 0)
func_6996_call = mod.get_global_var('func_6996')
func_6997_call = mutated_mod.get_global_var('func_6997')
call_7993 = func_6996_call()
call_7994 = func_6996_call()
uop_8003 = relay.exp(call_7934.astype('float32')) # shape=(1040,)
uop_8005 = relay.exp(call_7935.astype('float32')) # shape=(1040,)
uop_8007 = relay.cos(uop_8003.astype('float64')) # shape=(1040,)
uop_8009 = relay.cos(uop_8005.astype('float64')) # shape=(1040,)
output = relay.Tuple([call_7932,bop_7942,call_7948,call_7959,call_7968,var_7969,const_7970,var_7971,var_7972,call_7985,call_7988,const_7989,call_7993,uop_8007,])
output2 = relay.Tuple([call_7933,bop_7945,call_7949,call_7960,call_7973,var_7969,const_7970,var_7971,var_7972,call_7986,call_7990,const_7989,call_7994,uop_8009,])
func_8014 = relay.Function([var_7941,var_7969,var_7971,var_7972,], output)
mod['func_8014'] = func_8014
mod = relay.transform.InferType()(mod)
var_8015 = relay.var("var_8015", dtype = "float32", shape = (1040,))#candidate|8015|(1040,)|var|float32
var_8016 = relay.var("var_8016", dtype = "float32", shape = (286,))#candidate|8016|(286,)|var|float32
var_8017 = relay.var("var_8017", dtype = "bool", shape = ())#candidate|8017|()|var|bool
var_8018 = relay.var("var_8018", dtype = "bool", shape = (1404,))#candidate|8018|(1404,)|var|bool
output = func_8014(var_8015,var_8016,var_8017,var_8018,)
func_8019 = relay.Function([var_8015,var_8016,var_8017,var_8018,], output)
mutated_mod['func_8019'] = func_8019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5830_call = mod.get_global_var('func_5830')
func_5831_call = mutated_mod.get_global_var('func_5831')
call_8036 = relay.TupleGetItem(func_5830_call(), 0)
call_8037 = relay.TupleGetItem(func_5831_call(), 0)
func_1120_call = mod.get_global_var('func_1120')
func_1125_call = mutated_mod.get_global_var('func_1125')
const_8041 = relay.const([[-0.494398],[-7.137854],[-3.479633],[-1.557167],[8.151498],[-9.038145],[2.678563],[5.937305],[3.745086],[-3.902348],[2.102027],[-6.325512],[-0.397859],[3.090404],[2.900804],[-6.274483],[7.616451],[-9.644871],[9.744437],[-3.120255],[8.494012],[-2.650626],[7.791501],[2.010036],[6.190643],[6.114618],[-8.427249],[4.768656],[3.005396],[9.658841],[8.964089],[-6.519107],[-4.027063],[-4.889222],[8.219913],[7.519434],[5.549355],[0.435479],[3.747384],[6.231117],[9.207494],[-2.205620],[-0.946753],[-6.457888],[-8.149786],[-8.645481],[1.203023],[-2.630352],[8.179816],[1.720400],[3.956332],[-9.219549],[-3.021106],[8.727743],[-5.154654],[5.053904],[0.441724],[3.233830],[4.587828],[-9.701730],[3.535032],[2.316758],[8.770857],[-1.026799],[-3.879245],[-4.684900],[-9.379080],[-5.157716],[-2.489635],[7.692758],[-4.009511],[-9.088390],[-0.006260],[-1.373960],[-5.847967],[0.993692],[2.311152],[-5.408936],[-9.695183],[-0.556641],[7.049509],[-8.277646],[0.532089],[-3.194934],[-9.297392],[-1.308627],[-4.635912],[6.455229],[-2.981202],[6.605870],[-7.083015],[-8.014312],[6.012565],[-1.668345],[5.915277],[9.829331],[6.781833],[0.789606],[-7.512270],[5.919053],[8.948295],[-3.085625],[-2.556308],[-9.417640],[6.729601],[6.368522],[-6.251182],[2.799287],[6.676990],[8.457144],[-9.795396],[5.416596],[-4.422044],[-1.031506],[-1.252287],[5.723956],[9.701707],[-5.675988],[6.005897],[-5.985580],[-7.879234],[-7.791036],[8.762809],[-5.265479],[-9.313053],[-5.041643],[-0.266676],[-0.564225],[-8.187205],[-5.175342],[-4.116400],[-6.479767],[0.729264],[-7.823118],[1.942825]], dtype = "float32")#candidate|8041|(135, 1)|const|float32
const_8042 = relay.const([[2.449913,-9.942276,-7.791338,2.623576,-1.705761,2.637942,-1.851578,-2.848184,2.467600,7.209597,8.091813,-7.546956,-2.780816,-4.655672,3.816614,4.586336,2.843309,-5.909140,-8.824135,1.446532,-7.371209,9.201148,-4.853523,2.635284],[-1.761280,-3.078559,-3.588980,-2.579033,-8.268624,-4.843546,8.495459,-4.662027,6.184908,-0.264997,-1.064100,8.379944,-8.201226,-5.667472,-6.332678,-7.990601,-4.577508,-6.714756,6.524563,8.278540,4.755319,-9.454145,6.195073,1.809338],[0.377377,-1.045615,5.652200,-0.146997,-8.508633,-1.392826,0.360339,2.814447,0.223939,-1.698908,-4.964030,-7.882257,8.161825,-4.690028,-3.913948,-8.090917,9.534239,2.092745,-7.649186,-8.604663,-6.095211,0.878661,-3.436822,0.704630],[-1.685554,-1.130457,-9.657474,-6.747347,6.840387,-8.755365,-8.026215,-2.723746,-5.310835,7.783902,8.526307,3.084898,-2.484220,6.991203,-6.880044,5.746907,3.154718,7.776478,-6.594657,9.961961,2.457595,9.883211,-6.295220,1.835809],[-7.620608,4.508966,3.923243,4.895289,2.890516,-9.122580,-2.505450,-3.013164,4.640175,2.731599,8.345167,-2.858377,-0.320994,0.415210,6.557714,7.534512,1.390865,9.086354,-2.863424,-9.049817,-9.409228,9.843891,-8.312240,-0.286759],[0.418573,-6.691914,-2.922400,1.002887,-4.401097,-5.743038,-3.514672,4.383106,-0.735768,-2.629938,-9.698039,5.041387,5.870702,2.406890,-5.748985,9.049348,2.809381,9.720257,-2.747401,-1.915073,1.622521,-9.982403,8.067397,6.317575],[0.498049,-8.420072,-8.446349,-1.008729,-7.227363,-2.742643,0.423065,-2.139950,5.532629,-6.371452,5.571200,-7.700081,6.659856,-5.378278,8.388989,2.183328,8.785176,-0.080188,9.219937,3.169204,-5.810902,-1.269792,5.095557,-5.559883],[-3.790798,9.805123,6.522441,-8.871801,-3.475639,2.235532,-3.783050,-5.781868,-0.227217,-1.148678,2.281605,4.268099,8.635260,1.274836,4.466324,0.807589,6.891607,4.140182,-6.569391,8.072618,-8.622651,-8.989217,8.089504,-7.133149],[7.996488,8.230626,-5.980408,-5.161252,4.087220,-2.413889,9.632635,-6.055112,-2.621857,-2.090889,-6.064944,-3.818245,-2.557600,0.650436,1.869164,-4.177759,-4.176934,-0.421366,-7.200005,-0.254168,-9.799536,-1.437505,-0.818213,-3.952904],[-1.383069,-6.470624,3.845363,4.209267,6.911287,7.028555,-6.419260,-5.836690,-8.785040,5.376267,8.953087,-1.299463,0.292294,-0.285850,1.181097,-2.438427,9.844019,-2.585859,7.062136,-8.376842,6.745587,-8.405774,5.544498,-3.332499],[3.940602,0.677966,-8.164620,-8.262208,-8.454559,8.881007,-3.603730,-6.788369,-4.880719,-0.047418,-1.222000,9.808538,-3.226856,-5.278429,-5.610717,4.426264,-0.132168,-5.507009,-0.066473,-6.778931,5.414840,0.845643,-7.174817,7.438019],[-6.128671,-8.611693,2.248901,-7.662576,2.428643,7.486440,-0.758062,8.742022,1.840122,5.998959,7.666481,1.910023,8.042699,-9.984727,-4.530642,1.848129,1.265819,9.047625,7.754652,-7.539611,-4.203018,-9.182552,8.287792,-3.559924],[3.261885,-1.786680,3.251102,-9.881839,-4.347888,-2.403695,-1.746935,-8.165381,-1.125427,-8.739120,5.989179,-6.433615,6.462938,-0.607814,3.682508,1.268141,-6.145431,4.497410,1.378154,8.588589,-9.800775,-6.060373,7.127870,-4.815462],[2.533279,8.315688,0.141759,-0.145865,-1.394383,0.606050,4.634946,-3.613577,8.305480,-4.729464,4.883038,-8.460917,4.200966,2.764601,9.956259,-5.403559,-8.486580,-5.778174,-1.290694,-7.673492,8.771854,-7.908895,9.290386,5.580350],[-2.449479,4.284423,9.970716,3.593248,0.265830,2.580430,-5.236657,5.784577,7.093815,-8.716244,-6.637573,-0.677230,9.356132,8.769673,5.416684,3.629409,-6.178165,-3.145105,-3.271140,-5.983205,-6.937344,1.200694,-2.506672,3.807133],[-5.402036,8.534300,5.306481,-0.337306,-7.566894,3.602804,-5.849929,9.906388,1.891314,-3.844178,7.408103,2.162420,-9.308389,-0.702674,1.487771,-0.625749,3.006148,7.271318,7.315641,4.082968,9.267663,-0.869469,8.090484,-0.371422],[0.998399,4.352249,7.889062,-6.450390,6.402760,-5.789437,-6.316805,-6.831125,-2.136506,-1.265734,0.895446,5.071442,-7.805751,0.720109,0.950737,0.858918,-0.795897,8.560317,0.713690,-3.754384,-2.843437,-2.803115,9.653382,7.423242],[-2.142673,-9.735299,7.671096,-2.933711,2.848973,-0.965308,5.386532,6.901985,-3.692410,2.374994,-0.113709,-1.327591,2.768958,1.823580,5.269190,-6.585865,2.607083,0.146363,7.448192,-0.236229,9.268807,7.478604,-7.167758,1.696409],[-0.299481,9.283678,-0.763433,4.030162,-5.449817,-5.161268,7.634257,9.531004,6.867308,-1.080796,-7.151125,3.003050,7.823868,-9.467225,3.020831,-3.114362,-3.894053,-2.080998,8.607445,-0.303678,3.800555,0.621950,-6.244267,1.823681],[2.551187,-5.367745,-8.356461,-7.508305,-6.734967,-1.037911,-1.776410,9.771489,-6.792387,9.488987,-3.721196,5.882874,-9.730350,-0.684271,5.341228,0.355467,4.955923,-8.533778,0.180816,0.212540,2.340268,-6.458284,-1.416833,-4.755006],[7.567286,-8.890200,-1.685635,3.010758,-2.595002,1.953078,1.241855,0.732030,-8.255496,8.725267,-1.827215,5.351697,-2.615374,7.571018,-6.439594,8.458988,2.489558,9.199292,3.486802,-4.816416,-7.033973,5.042813,-8.602201,7.381385],[-4.777444,0.924359,6.027729,-5.342387,-4.066769,6.557951,2.049827,-1.293773,-9.490079,-0.016148,7.020754,-6.990018,-3.861419,2.765391,-2.613571,4.917428,4.691150,1.404103,-4.034385,-5.892275,3.928156,5.786519,-2.521235,9.375014],[6.139145,-8.770389,-9.044839,-6.650427,-0.506276,-5.496080,-9.522114,1.929350,-5.383941,1.212556,-6.321860,8.850036,0.594582,3.714881,-9.318792,-0.282359,-2.448654,-5.862241,8.341421,-9.900976,5.766799,-9.476637,-6.389255,6.935006],[-2.923046,6.683441,9.378008,-0.572013,9.802981,-1.367007,-7.649035,3.419662,-7.685999,-7.701744,8.368498,4.912949,7.940234,-7.217913,-6.560403,-8.943813,-4.569088,8.963149,-3.484837,-8.229703,0.957369,5.018957,-4.980298,9.283731],[3.395912,-5.072966,-5.838456,8.941385,-2.998094,4.243271,2.444473,4.642386,-2.355593,8.540716,6.040526,-7.166742,3.399874,-4.372561,0.448369,-7.214737,0.066902,2.494321,-8.574594,8.501134,-8.528729,8.273675,-6.577107,-6.058923],[-2.800357,5.637830,7.104314,-2.547819,-9.841098,-6.476590,-3.071373,-7.389354,-0.389479,8.149613,-4.462401,3.594086,-2.352965,-9.716409,6.081068,8.117384,0.582551,7.786557,-0.861208,0.948518,8.985604,-5.647573,-0.290130,8.396678],[-2.465126,8.415569,-3.479730,-8.661498,-7.498621,6.213546,9.170845,7.732671,-1.027723,0.320784,-7.643203,9.599691,4.944588,-3.580992,-6.120015,-4.608313,-7.561745,3.454024,-3.688335,2.388685,-5.624080,-0.192114,5.543442,-3.684029],[7.104395,6.853813,-9.950845,6.628213,-0.434110,1.084084,8.351541,-1.694235,-7.081400,-4.269488,0.382004,7.087962,9.973984,1.995190,0.214315,-5.895593,0.684956,-4.922681,-3.183281,1.859702,9.036458,1.103307,-0.909609,8.412663],[5.844746,3.221419,0.790378,-5.501851,1.841337,-0.826855,-6.428083,7.800932,-3.425070,2.278079,7.070270,5.493650,-1.389343,0.212402,-1.292078,8.731086,1.324321,-4.887721,7.095072,9.412487,-3.952327,6.529894,-0.009319,8.351236],[-1.650625,2.581008,4.177435,1.435147,9.698814,7.078632,5.554350,7.175366,4.304112,7.538366,-6.405425,7.258786,-5.320959,8.654815,5.312087,4.801892,-5.288638,4.217032,-5.252128,6.577271,-5.992086,0.980391,7.196958,-2.688351],[2.963241,3.169537,-6.355475,-4.788184,5.147804,7.799125,-6.931225,-7.306984,0.607876,9.195025,-3.511481,9.005466,8.699274,-4.244446,4.283449,5.582436,5.239943,-9.182797,-7.689424,-1.343028,4.871649,-0.712635,4.135582,-4.429274],[1.104863,-7.788965,-2.552455,-0.662995,-9.296156,-8.361216,6.766244,-8.312595,-0.122222,-7.922161,-6.510276,-2.599502,-8.010489,1.683449,0.556874,-1.181364,0.660138,8.510442,-0.867811,7.420806,-7.691395,-9.330441,-0.046831,-5.994559],[6.152423,5.922358,-0.416410,2.731839,-3.542764,-1.045547,-3.553264,-3.443763,5.464457,1.753602,4.350139,-0.117769,-8.045631,2.759851,-9.001840,0.875660,-3.542584,7.095035,-5.143825,1.766722,2.216963,0.689962,-0.971909,-7.988181],[0.619731,4.108135,-5.733717,-8.315902,-2.205300,6.144399,-3.875393,1.628535,6.708956,0.506736,8.051997,9.447273,-0.881307,2.918581,-8.447252,-2.632880,4.367244,2.309459,2.434552,4.198851,3.301803,-2.707324,8.049067,7.132653],[-7.702753,3.146806,6.702498,1.845149,7.487735,6.846383,-0.352590,9.303120,3.975882,5.057849,-8.947727,1.548979,-6.523064,6.576245,6.941259,-1.339355,2.927241,3.212819,-1.335040,-8.592385,0.347365,-4.950874,6.195843,-6.331157],[-2.934600,-6.372655,-0.507856,-9.231062,1.785377,-0.664323,-2.059888,6.333853,-3.953883,7.176657,4.673535,-0.777253,0.749137,-8.534882,-6.926997,3.026443,-9.995970,-1.570778,9.180186,8.831378,-3.492291,6.389806,3.317609,5.685980],[-8.139093,-2.140283,-6.531158,-4.732938,2.426151,5.381625,5.330198,-7.343100,-7.559320,-4.093874,-1.765160,-0.419939,-3.159182,0.702118,-0.741810,4.302790,7.097631,-2.384191,0.549078,1.904144,5.200166,-8.075263,-7.253851,1.788003],[2.103272,-0.467602,7.624075,6.561981,1.036924,4.833043,2.119328,-2.705810,6.436235,-4.004790,8.487256,3.569621,-9.792822,-6.269273,7.372599,5.775856,6.129490,-4.997911,1.382005,-4.023565,-0.660790,-0.485503,3.928711,0.448765],[-1.546552,0.234471,0.431565,-5.914210,-3.356334,-6.630931,-2.629416,3.275623,-9.075408,8.712027,6.142915,-7.495826,8.898722,8.252561,7.846781,3.720139,-6.544468,4.915375,-9.872492,-9.803766,-4.983163,-5.405654,-5.490291,5.486297],[4.696856,-1.887835,-4.551751,-6.600091,-5.142801,-3.659486,-9.257370,6.380386,-6.492298,8.760112,-2.360342,-4.699946,-7.306824,-4.460811,-9.216609,9.498443,-5.122825,-9.910878,-1.536038,-7.696860,-4.167771,-7.809770,3.662554,4.221588],[5.861194,-5.346034,-8.533114,-3.351733,5.473575,-3.777763,-2.259661,6.468986,4.721202,-9.179732,-7.468102,-5.260809,3.967140,-2.624970,-9.270266,1.895180,-0.541609,-4.297017,-8.132960,7.494233,4.782013,4.617352,-0.712289,-8.896989],[-1.356425,2.606085,4.389394,3.914889,4.113138,9.420619,6.051177,1.996718,-0.693931,7.409292,-1.141319,-2.361770,-9.776894,-6.996601,-6.279097,-5.396539,2.326584,-8.990673,-1.277108,4.626186,0.451911,8.851651,2.565504,-7.389576],[-6.317649,-3.328304,-6.388135,-5.647681,-8.362376,4.720765,2.352600,9.411988,-1.006287,-6.055329,8.396981,-8.256500,-1.861627,-3.780491,-3.256228,-2.905337,-7.183903,5.170414,2.388054,3.035622,-6.316278,7.847832,-9.290776,-8.833979],[-8.081720,0.899445,4.916266,-6.320423,-1.764189,1.599489,7.902263,8.968880,5.575341,-1.085009,7.847713,-8.746148,7.213134,7.915839,0.747262,-0.939309,-4.550757,6.095577,7.384549,-7.451503,-8.985129,-0.044390,7.203719,3.418308],[-8.346690,1.197017,5.744060,-3.600204,4.710628,1.012640,9.172508,-9.530602,9.969853,3.189957,8.746286,-6.852769,-6.510241,3.064567,3.951937,-8.423911,1.776341,7.568010,8.072988,2.754522,8.189500,0.755206,-0.287949,8.716120],[-5.971563,-8.199203,-8.711604,4.298802,1.442860,-9.332165,-1.043797,-5.985537,-4.131212,-4.215185,1.513073,3.061462,-7.508988,-4.737738,-3.962635,4.542977,-3.880456,1.170996,-2.525544,3.095288,5.932146,-9.625603,-9.493572,2.834823],[-9.057912,8.842451,6.826803,9.359629,2.539441,-5.457353,7.634373,-1.749195,5.525426,-4.528668,8.648814,1.241061,1.213354,-5.397557,3.162151,-4.473215,5.544892,9.417932,-1.330878,6.977653,-1.894037,-8.775688,6.212698,-5.438347],[-7.780873,-8.114076,-9.283069,-0.411047,-5.621378,-2.949764,7.501365,0.130077,-6.319906,5.051208,9.694794,-0.006684,1.764412,1.183426,-5.359695,4.568430,-1.156002,-0.313802,-6.496051,-2.692959,3.680033,-2.777927,-7.429036,9.517116]], dtype = "float32")#candidate|8042|(48, 24)|const|float32
var_8043 = relay.var("var_8043", dtype = "uint16", shape = (180,))#candidate|8043|(180,)|var|uint16
call_8040 = relay.TupleGetItem(func_1120_call(relay.reshape(const_8041.astype('float32'), [9, 1, 15]), relay.reshape(const_8042.astype('float32'), [1152,]), relay.reshape(var_8043.astype('uint16'), [180, 1]), ), 0)
call_8044 = relay.TupleGetItem(func_1125_call(relay.reshape(const_8041.astype('float32'), [9, 1, 15]), relay.reshape(const_8042.astype('float32'), [1152,]), relay.reshape(var_8043.astype('uint16'), [180, 1]), ), 0)
uop_8048 = relay.atan(call_8040.astype('float64')) # shape=(9, 1, 15)
uop_8050 = relay.atan(call_8044.astype('float64')) # shape=(9, 1, 15)
bop_8052 = relay.bitwise_and(uop_8048.astype('int8'), relay.reshape(const_8041.astype('int8'), relay.shape_of(uop_8048))) # shape=(9, 1, 15)
bop_8055 = relay.bitwise_and(uop_8050.astype('int8'), relay.reshape(const_8041.astype('int8'), relay.shape_of(uop_8050))) # shape=(9, 1, 15)
func_3669_call = mod.get_global_var('func_3669')
func_3671_call = mutated_mod.get_global_var('func_3671')
call_8057 = relay.TupleGetItem(func_3669_call(), 1)
call_8058 = relay.TupleGetItem(func_3671_call(), 1)
func_4715_call = mod.get_global_var('func_4715')
func_4717_call = mutated_mod.get_global_var('func_4717')
call_8072 = relay.TupleGetItem(func_4715_call(), 0)
call_8073 = relay.TupleGetItem(func_4717_call(), 0)
output = relay.Tuple([call_8036,const_8042,var_8043,bop_8052,call_8057,call_8072,])
output2 = relay.Tuple([call_8037,const_8042,var_8043,bop_8055,call_8058,call_8073,])
func_8076 = relay.Function([var_8043,], output)
mod['func_8076'] = func_8076
mod = relay.transform.InferType()(mod)
var_8077 = relay.var("var_8077", dtype = "uint16", shape = (180,))#candidate|8077|(180,)|var|uint16
output = func_8076(var_8077)
func_8078 = relay.Function([var_8077], output)
mutated_mod['func_8078'] = func_8078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6911_call = mod.get_global_var('func_6911')
func_6912_call = mutated_mod.get_global_var('func_6912')
call_8130 = relay.TupleGetItem(func_6911_call(), 0)
call_8131 = relay.TupleGetItem(func_6912_call(), 0)
output = relay.Tuple([call_8130,])
output2 = relay.Tuple([call_8131,])
func_8133 = relay.Function([], output)
mod['func_8133'] = func_8133
mod = relay.transform.InferType()(mod)
mutated_mod['func_8133'] = func_8133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8133_call = mutated_mod.get_global_var('func_8133')
call_8134 = func_8133_call()
output = call_8134
func_8135 = relay.Function([], output)
mutated_mod['func_8135'] = func_8135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7881_call = mod.get_global_var('func_7881')
func_7882_call = mutated_mod.get_global_var('func_7882')
call_8162 = func_7881_call()
call_8163 = func_7881_call()
output = relay.Tuple([call_8162,])
output2 = relay.Tuple([call_8163,])
func_8173 = relay.Function([], output)
mod['func_8173'] = func_8173
mod = relay.transform.InferType()(mod)
output = func_8173()
func_8174 = relay.Function([], output)
mutated_mod['func_8174'] = func_8174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mod.get_global_var('func_5807')
func_5808_call = mutated_mod.get_global_var('func_5808')
call_8212 = func_5807_call()
call_8213 = func_5807_call()
output = call_8212
output2 = call_8213
func_8223 = relay.Function([], output)
mod['func_8223'] = func_8223
mod = relay.transform.InferType()(mod)
output = func_8223()
func_8224 = relay.Function([], output)
mutated_mod['func_8224'] = func_8224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7360_call = mod.get_global_var('func_7360')
func_7361_call = mutated_mod.get_global_var('func_7361')
call_8242 = relay.TupleGetItem(func_7360_call(), 0)
call_8243 = relay.TupleGetItem(func_7361_call(), 0)
output = call_8242
output2 = call_8243
func_8248 = relay.Function([], output)
mod['func_8248'] = func_8248
mod = relay.transform.InferType()(mod)
output = func_8248()
func_8249 = relay.Function([], output)
mutated_mod['func_8249'] = func_8249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4650_call = mod.get_global_var('func_4650')
func_4651_call = mutated_mod.get_global_var('func_4651')
call_8256 = relay.TupleGetItem(func_4650_call(), 1)
call_8257 = relay.TupleGetItem(func_4651_call(), 1)
uop_8258 = relay.sin(call_8256.astype('float64')) # shape=(12, 6, 10)
uop_8260 = relay.sin(call_8257.astype('float64')) # shape=(12, 6, 10)
func_7142_call = mod.get_global_var('func_7142')
func_7144_call = mutated_mod.get_global_var('func_7144')
call_8327 = relay.TupleGetItem(func_7142_call(), 0)
call_8328 = relay.TupleGetItem(func_7144_call(), 0)
output = relay.Tuple([uop_8258,call_8327,])
output2 = relay.Tuple([uop_8260,call_8328,])
func_8339 = relay.Function([], output)
mod['func_8339'] = func_8339
mod = relay.transform.InferType()(mod)
mutated_mod['func_8339'] = func_8339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8339_call = mutated_mod.get_global_var('func_8339')
call_8340 = func_8339_call()
output = call_8340
func_8341 = relay.Function([], output)
mutated_mod['func_8341'] = func_8341
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8357 = relay.var("var_8357", dtype = "float32", shape = (4, 8))#candidate|8357|(4, 8)|var|float32
uop_8358 = relay.tan(var_8357.astype('float32')) # shape=(4, 8)
output = relay.Tuple([uop_8358,])
output2 = relay.Tuple([uop_8358,])
func_8367 = relay.Function([var_8357,], output)
mod['func_8367'] = func_8367
mod = relay.transform.InferType()(mod)
var_8368 = relay.var("var_8368", dtype = "float32", shape = (4, 8))#candidate|8368|(4, 8)|var|float32
output = func_8367(var_8368)
func_8369 = relay.Function([var_8368], output)
mutated_mod['func_8369'] = func_8369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_8382 = relay.TupleGetItem(func_2625_call(), 1)
call_8383 = relay.TupleGetItem(func_2626_call(), 1)
output = relay.Tuple([call_8382,])
output2 = relay.Tuple([call_8383,])
func_8392 = relay.Function([], output)
mod['func_8392'] = func_8392
mod = relay.transform.InferType()(mod)
mutated_mod['func_8392'] = func_8392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8392_call = mutated_mod.get_global_var('func_8392')
call_8393 = func_8392_call()
output = call_8393
func_8394 = relay.Function([], output)
mutated_mod['func_8394'] = func_8394
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8410 = relay.var("var_8410", dtype = "uint32", shape = ())#candidate|8410|()|var|uint32
var_8411 = relay.var("var_8411", dtype = "uint32", shape = (3, 11, 1))#candidate|8411|(3, 11, 1)|var|uint32
bop_8412 = relay.not_equal(var_8410.astype('bool'), var_8411.astype('bool')) # shape=(3, 11, 1)
var_8421 = relay.var("var_8421", dtype = "bool", shape = (3, 11, 7))#candidate|8421|(3, 11, 7)|var|bool
bop_8422 = relay.greater(bop_8412.astype('bool'), var_8421.astype('bool')) # shape=(3, 11, 7)
func_6158_call = mod.get_global_var('func_6158')
func_6159_call = mutated_mod.get_global_var('func_6159')
call_8428 = relay.TupleGetItem(func_6158_call(), 6)
call_8429 = relay.TupleGetItem(func_6159_call(), 6)
func_5727_call = mod.get_global_var('func_5727')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_8430 = relay.TupleGetItem(func_5727_call(), 0)
call_8431 = relay.TupleGetItem(func_5728_call(), 0)
output = relay.Tuple([bop_8422,call_8428,call_8430,])
output2 = relay.Tuple([bop_8422,call_8429,call_8431,])
func_8441 = relay.Function([var_8410,var_8411,var_8421,], output)
mod['func_8441'] = func_8441
mod = relay.transform.InferType()(mod)
mutated_mod['func_8441'] = func_8441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8441_call = mutated_mod.get_global_var('func_8441')
var_8443 = relay.var("var_8443", dtype = "uint32", shape = ())#candidate|8443|()|var|uint32
var_8444 = relay.var("var_8444", dtype = "uint32", shape = (3, 11, 1))#candidate|8444|(3, 11, 1)|var|uint32
var_8445 = relay.var("var_8445", dtype = "bool", shape = (3, 11, 7))#candidate|8445|(3, 11, 7)|var|bool
call_8442 = func_8441_call(var_8443,var_8444,var_8445,)
output = call_8442
func_8446 = relay.Function([var_8443,var_8444,var_8445,], output)
mutated_mod['func_8446'] = func_8446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3689_call = mod.get_global_var('func_3689')
func_3691_call = mutated_mod.get_global_var('func_3691')
call_8448 = func_3689_call()
call_8449 = func_3689_call()
output = relay.Tuple([call_8448,])
output2 = relay.Tuple([call_8449,])
func_8450 = relay.Function([], output)
mod['func_8450'] = func_8450
mod = relay.transform.InferType()(mod)
output = func_8450()
func_8451 = relay.Function([], output)
mutated_mod['func_8451'] = func_8451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6666_call = mod.get_global_var('func_6666')
func_6667_call = mutated_mod.get_global_var('func_6667')
call_8475 = relay.TupleGetItem(func_6666_call(), 0)
call_8476 = relay.TupleGetItem(func_6667_call(), 0)
output = relay.Tuple([call_8475,])
output2 = relay.Tuple([call_8476,])
func_8504 = relay.Function([], output)
mod['func_8504'] = func_8504
mod = relay.transform.InferType()(mod)
output = func_8504()
func_8505 = relay.Function([], output)
mutated_mod['func_8505'] = func_8505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8173_call = mod.get_global_var('func_8173')
func_8174_call = mutated_mod.get_global_var('func_8174')
call_8521 = relay.TupleGetItem(func_8173_call(), 0)
call_8522 = relay.TupleGetItem(func_8174_call(), 0)
output = relay.Tuple([call_8521,])
output2 = relay.Tuple([call_8522,])
func_8536 = relay.Function([], output)
mod['func_8536'] = func_8536
mod = relay.transform.InferType()(mod)
mutated_mod['func_8536'] = func_8536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8536_call = mutated_mod.get_global_var('func_8536')
call_8537 = func_8536_call()
output = call_8537
func_8538 = relay.Function([], output)
mutated_mod['func_8538'] = func_8538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_8552 = relay.TupleGetItem(func_2402_call(), 0)
call_8553 = relay.TupleGetItem(func_2404_call(), 0)
output = call_8552
output2 = call_8553
func_8556 = relay.Function([], output)
mod['func_8556'] = func_8556
mod = relay.transform.InferType()(mod)
mutated_mod['func_8556'] = func_8556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8556_call = mutated_mod.get_global_var('func_8556')
call_8557 = func_8556_call()
output = call_8557
func_8558 = relay.Function([], output)
mutated_mod['func_8558'] = func_8558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7479_call = mod.get_global_var('func_7479')
func_7480_call = mutated_mod.get_global_var('func_7480')
call_8670 = func_7479_call()
call_8671 = func_7479_call()
output = call_8670
output2 = call_8671
func_8675 = relay.Function([], output)
mod['func_8675'] = func_8675
mod = relay.transform.InferType()(mod)
output = func_8675()
func_8676 = relay.Function([], output)
mutated_mod['func_8676'] = func_8676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4186_call = mod.get_global_var('func_4186')
func_4188_call = mutated_mod.get_global_var('func_4188')
call_8707 = relay.TupleGetItem(func_4186_call(), 0)
call_8708 = relay.TupleGetItem(func_4188_call(), 0)
output = call_8707
output2 = call_8708
func_8756 = relay.Function([], output)
mod['func_8756'] = func_8756
mod = relay.transform.InferType()(mod)
output = func_8756()
func_8757 = relay.Function([], output)
mutated_mod['func_8757'] = func_8757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4071_call = mod.get_global_var('func_4071')
func_4072_call = mutated_mod.get_global_var('func_4072')
call_8825 = relay.TupleGetItem(func_4071_call(), 0)
call_8826 = relay.TupleGetItem(func_4072_call(), 0)
func_3595_call = mod.get_global_var('func_3595')
func_3599_call = mutated_mod.get_global_var('func_3599')
var_8868 = relay.var("var_8868", dtype = "float64", shape = (845,))#candidate|8868|(845,)|var|float64
var_8869 = relay.var("var_8869", dtype = "uint16", shape = (3, 60))#candidate|8869|(3, 60)|var|uint16
call_8867 = relay.TupleGetItem(func_3595_call(relay.reshape(var_8868.astype('float64'), [13, 5, 13]), relay.reshape(var_8869.astype('uint16'), [180,]), ), 3)
call_8870 = relay.TupleGetItem(func_3599_call(relay.reshape(var_8868.astype('float64'), [13, 5, 13]), relay.reshape(var_8869.astype('uint16'), [180,]), ), 3)
uop_8875 = relay.sinh(var_8868.astype('float64')) # shape=(845,)
func_8504_call = mod.get_global_var('func_8504')
func_8505_call = mutated_mod.get_global_var('func_8505')
call_8880 = relay.TupleGetItem(func_8504_call(), 0)
call_8881 = relay.TupleGetItem(func_8505_call(), 0)
func_3226_call = mod.get_global_var('func_3226')
func_3230_call = mutated_mod.get_global_var('func_3230')
const_8883 = relay.const([-8.466447,-5.812991,7.324793,-4.908257,-0.253317,-3.366709,1.018570,7.459207,9.780857,-7.611652,-2.069051,-2.243578,5.435411,4.964816,1.724132,5.457555,-9.806748,-1.694737,-1.740565,4.560173,4.239121,0.110297,-8.887395,-5.916117,-5.445698,-3.886035,2.627199,-3.946047,0.595510,4.973810,-8.308233,-1.712757,5.631222,-9.996120,-7.930995,-4.259419,9.612202,-4.735647,-2.302982,-5.125340,-2.698248,-2.304963,6.784497,-4.360480,-5.615596,1.282996,-3.175203,3.551047,-0.583622,5.909143,5.323294,-4.236871,8.234059,-8.997426,1.847133,-2.443639,9.186575,4.836940,4.476982,-7.737420,-2.944114,2.979161,1.000305,-0.462458,-3.323233,-3.875820,1.169240,0.443267,-3.613720,-6.280486,-4.106750,6.755627,3.103972,-3.067959,-5.472283,-6.951007,-1.426006,7.889568,6.963326,-6.134644,4.743232,7.826424,3.662484,-7.771796,6.353534,-2.412067,4.419243,4.288540,-3.045837,-6.771483,-5.040155,4.287729,-2.362511,3.137940,-2.378197,7.070388,-2.546393,-2.896006,1.962470,1.165843,-7.448649,-5.343744,8.223247,-6.439940,5.935216,-7.395867,-6.140371,9.631918,-8.728042,-8.536540,-0.125569,1.291461,-0.894500,-2.184578,-2.198832,-3.916830,2.821899,-5.857938,3.998007,5.440209,4.976964,-5.201369,1.258869,-4.598747,-0.281711,6.429037,3.261739,-3.825906,-1.103018,6.314483,-6.460223,6.684910,5.893654,0.038667,1.209988,0.453257,-3.985938,-5.446209,9.042580,-2.776360,3.171635,-3.526664,-2.243616,-8.172386,-0.354264,7.160155,-4.846918,-6.466446,-6.306524,-5.158779,-2.633321,1.506803,9.612551,9.299743,-4.381618,2.836939,7.836424,-9.335924,-8.923766,-5.853738,9.358820,4.231405,2.868900,5.160620,5.320843,1.460244,7.868653,2.918803,-8.279728,-5.732116,-5.701965,-2.405389,2.090875,0.126216,5.260060,-1.817337,9.131316,-2.576784,-8.007376,-2.021721,0.826736,8.507984,-2.317746,-7.494335,5.257484,-7.823342,-7.344286,8.536816,8.956661,9.767942,7.816646,8.073852,8.699463,8.117252,0.615483,-0.017698,9.882872,-7.842920,-9.184908,-0.288995,3.514965,5.715206,8.445176,8.190130,2.378616,4.749689,9.691739,2.285311,7.339924,-7.048466,-8.329339,5.852578,-7.873086,-9.225702,-2.715327,7.028524,6.446545,7.920222,6.708855,5.827516,4.896400,6.767211,-8.931987,-9.668725,4.168095,-6.999011,9.129999,4.626716,4.405040,-2.413287,-9.516529,6.149502,-3.210441,-2.698519,-0.437494,-7.663762,4.721853,-1.725164,-0.106925,2.962277,0.979452,5.670682,8.422784,-7.351838,-8.069123,9.013425,-5.099792,-7.392629,0.793725,6.679417,5.597272,-2.289547,1.680148,-8.022880,6.111112,-4.740529,5.683781,5.708514,-1.797697,-5.154237,-3.156535,-1.062986,-6.797908,1.120720,9.732582,7.010539,-7.218550,4.633513,-0.128532,2.458116,5.276320,-8.166081,7.307301,-4.078259,-5.749138,8.808907,-7.164814,8.808035,-9.287082,-0.971178,9.440577,-8.593678,9.174331,-4.561938,2.656146,6.726957,4.836258,-4.688914,8.333879,-7.218650,0.980505,-2.790794,0.759883,-6.731312,-3.619043,-4.276366,0.752607,2.017566,-9.189839,-8.731398,7.631211,6.757828,-7.928633,-1.135733,-7.419763,2.505643,-8.353392,5.151192,8.567623,1.246147,-1.855927,-1.224600,6.768545,9.829152,3.932493,1.602991,8.530536,3.089941,-0.106129,-4.078670,-7.149431,-3.165225,0.744666,6.612791,-3.934799,8.639718,-0.638241,-9.269140,3.617781,9.831554,4.153784,-5.460672,0.854547,-7.961552,2.505004,-8.159984,-2.260829,-5.402056,-0.873522,4.274043,-2.761127,-8.476876,-1.637383,-4.402296,-3.230354,-0.347213,3.022889,-4.031928,-8.107684,-1.116477,3.790947,9.097766,-4.817907,-7.784382,8.533141,6.169052,-1.281663,-0.655373,-9.840369,-2.239198,7.134477,-3.671582,7.513703,9.322667,-2.988642,0.146710,8.216953,6.027983,-0.901876,-1.387278,2.178965,-1.772580,3.705981,-6.272517,3.498519,-7.669695,2.983605,3.313989,-4.147026,-7.242313,6.011297,-0.751094,0.200581,-4.954663,0.487313,2.549811,-7.475953,-2.659689,7.002788,5.655975,-4.442308,3.620702,-5.449116,-3.871782,0.030271,3.984389,8.156934,2.052883,-2.313777,-8.777522,9.331844,-2.405219,0.689225,9.779509,-8.783444,-0.374091,5.432887,-7.571816,-6.300516,-8.288219,-4.522473,-2.112862,6.606076,-4.119800,0.247881,-8.577350,-0.674059,-0.974652,1.273432,-7.613810,-4.958006,-9.584432,-7.834563,-6.347705,-3.987763,9.426672,-7.542656,-1.259949,1.305404,0.012126,5.482883,3.236131,1.612852,-1.493835,-3.669822,-5.426098,5.097093,-6.016688,9.842334,-0.125542,4.643841,-0.779014,-3.911401,3.541909,5.179734,-7.859053,-3.857524,1.397488,-9.750332,5.568946,-1.093072,0.637537,-3.472372,-8.601135,-4.835638,7.787762,-7.123578,-4.174889,-2.876305,-2.926774,-4.377348,4.261775,3.807387,-0.784972,-2.799280,-2.249260,5.072781,-7.257663,7.125079,-6.191970,0.435670,3.113315,6.695703,-1.436443,9.885201,-5.520280,-2.736040,5.615996,-7.190414,9.496710,4.811032,9.454107,2.525190,-9.779227,-2.169954,1.987623,8.819682,1.585624,-6.617905,-8.766373,6.529689,8.263253,-0.615498,3.845804,4.327126,2.230778,-6.774792,4.829564,-0.488363,-1.709020,-5.661410,7.537640,-5.238478,3.719917,-4.971902,-1.122003,-0.270491,5.124850,-6.991113,8.255669,5.590843,-9.721562,8.267988,-0.106802,-4.189921,2.648279,-0.363585,-8.893739,3.101099,1.400269,1.979670,3.889494,7.171856,8.394101,0.879328,7.039847,2.454638,-8.259539,-5.244753,2.011640,3.147178,5.715145,0.899585,-9.932633,3.719056,-0.668497,-8.792979,-6.340965,7.069878,4.369694,-2.419726,8.242637,6.526737,1.899132,-2.319527,-7.488555,8.175647,1.511757,5.793900,1.541628,0.382375,6.714283,-1.196299,-7.945837,9.101476,-0.849782,-7.005140,-1.810965,-3.138396,5.068840,-3.228153,-4.154801,-7.577273,-3.820502,-4.004008,-7.679218,3.851433,0.010995,-0.607064,0.382586,8.656289,1.008808,-9.738851,3.716340,3.791252,1.525600,-4.362831,1.650764,-2.400380,-2.665986,-7.530740,-3.654637,7.141213,5.198179,6.846227,7.748103,-0.946228,5.082150,-3.145618,7.720221,1.629632,4.025493,3.726320,-8.623858,-0.686586,-6.086565,-2.617727,7.009612,-9.181260,1.243819,5.743843,-5.632311,1.728320,-8.393057,7.296080,-5.289986,6.329626,-3.424644,-8.471761,-0.887189,-3.299235,3.686095,4.053218,-1.302371,8.408402,-3.447467,-8.551277,6.710897,-2.924241,-4.830046,1.264254,-2.338812,-2.850646,9.376985,-8.418964,-8.564637,-3.509754,0.713838,-5.339928,7.165215,7.480810,-1.412987,6.229854,5.857202,-6.967134,1.838279,-9.912278,-0.816420,-2.370046,-4.740044,2.909954,2.488478,-6.047653,5.150450,-6.636351,6.660178,-1.679535,-0.032571,1.671062,7.267800,6.785708,1.953958,5.660410,-6.675161,-1.394171,-5.642357,4.750288,8.606815,-8.686623,-6.440743,-2.756575,-9.110899,-2.540600,-9.042529,-7.710626,3.499503,-1.270476,-0.811138,-8.552025,9.130342,2.073388,-0.470449,-9.088400,-7.963550,-5.885572,5.352861,-9.048254,-1.253575,-0.473593,-6.424190,-8.354473,-3.953075,7.181024,-2.041739,-8.633471,-6.266818,9.810495,-7.288101,-0.667921,-1.414313,-7.360244,2.238754,4.641809,6.179610,-3.159936,2.664111,7.028922,5.129706,-6.175266,-2.760665,-1.752125,-6.279101,2.707852,1.785503,3.161278,-0.005814,5.062206,2.644810,2.277995,8.260854,-8.359538,3.285738,-7.732284,-8.120230,-9.103832,7.832118,6.685951,8.990903,4.409940,7.819517,-6.802492,-0.225928,7.257506,0.054064,-1.234645,3.218828,9.251511,-8.713485,8.916119,-8.870844,6.539874,-9.583523,2.059125,9.638336,-8.150814,3.332264,-0.557742,6.519844,7.543977,3.664468,3.486757,0.393509,8.102683,-1.538402,-4.077825,-8.913147,6.866992,2.485628,-5.650298,5.029020,5.272222,-0.410987,-4.414966,1.108738,-8.249260,8.910347,9.713008,-4.500125,-2.412510,-4.391970,7.888249,-9.369616,7.527255,4.114136,-5.367538,8.089570,8.026533,7.732998,3.889704,-5.281719,3.365019,7.018093,-0.638353,2.137388,-4.677855,2.090934,5.269422,-9.589580,9.113511,-9.635628,-0.039010,1.345442,6.334648,1.688478,-8.370772,-7.538569,5.183388,-5.034274,3.305779,-8.183545,1.754830,0.398126,4.915614,-2.013011,6.005844,-0.925577,-5.925682,-8.336762,8.504459,-9.978778,3.002828,3.596627,-9.183246,-6.817242,-5.312271,0.328140,-3.912960,-4.069532,2.425814,6.268974,0.858389,-8.492904,9.666436,-3.733434,8.255952,-1.005762,5.604456,7.871808,-2.737545,-7.611324,9.671502,-4.927269,-2.428445,9.177150,5.805728,9.333099,0.742381,-4.804366,-0.179589,0.974530,6.861375,-5.616150,4.447505,-9.180030,6.915271,-6.150304,9.870012,-6.426495,5.611058,0.927851,-9.034271,-1.217372,-3.416217,7.851048,7.424161,-9.318753,-2.104442,9.864482,4.790093,7.711172,-7.118850,5.826850,7.688518,-1.896201,7.265490,9.208422,-7.026990,9.400969,1.253800,4.731070,2.696776,9.362534,-4.180407,-2.564966,7.600995,-7.086442,8.789443,3.035376,8.254529,-9.050339,8.569835,5.211106,3.072703,-6.175930,1.738062,0.581105,-0.445096,-5.988489,3.826831,-2.889283,3.583229,0.631700,-8.851353,0.364510,-1.917763,-9.034019,0.411712,9.277106,1.700397,6.989679,6.605017,1.429563,-8.367236,-2.918044,-7.847922,-8.599045,2.578781,4.961814,-0.371570,3.343432,-5.724387,-0.199448,0.058869,-9.846760,0.214952,9.662231,-1.543532,-5.117735,4.069854,-1.373719,4.650803,0.910041,-7.321032,-5.703731,9.255573,6.345251,-6.912213,3.379457,3.388034,-2.759948,-2.479568,0.338713,-4.876156,1.923288,-4.689809,-5.825521,-9.353719,-7.768602,-1.357077,5.017892,0.167579,0.254902,-4.639322,5.580174,-6.088675,-3.526445,-1.912994,9.513257,-4.577371,-6.869054,-9.687865,-7.990999,-5.853766,-5.149957,-4.199275,-8.296958,-4.295158,4.658085,-7.327357,3.289166,-1.810533,8.389774,2.628159,5.827710,2.386070,4.093868,-6.852341,-7.624682,-6.245335,5.490238,-4.184630,-1.747732,4.455433,6.123725,0.628779,-1.791842,0.188693,-6.491810,-1.545458,-6.566089,3.852694,-9.818554,0.748314,-3.264430,3.287954,-5.814639,7.145899,-1.476161,-8.008132,-5.059773,-9.378187,0.504472,8.400007,2.027207,-3.258022,5.937050,5.158570,9.668587,3.811488,-2.284863,-4.576898,-4.411386,-0.286144,-3.086828,9.087372,-9.410917,-7.536603,8.868547,9.684940,3.175830,-3.178461,4.905580,-3.398175,-4.717405,-9.757187,-5.375662,-0.528306,-2.738909,-1.089959,9.125688,6.513639,3.586447,-3.881423,7.290129,0.934143,5.626427,-5.317785,6.110659,1.537489,-2.233867,5.059142,-3.465430,6.062350,-5.321544,-3.442373,1.884984,0.569836,2.006665,2.786256,1.066459,0.217329,-1.805322,7.460786,0.309675,-0.905270,-7.633581,-5.214045,9.261081,9.520339,1.551047], dtype = "float32")#candidate|8883|(1040,)|const|float32
const_8884 = relay.const([-2.549882,-0.646800,-9.402700,-2.509516,-8.043824,6.236468,9.954999,6.490028,-1.981135,0.499811,-6.900611,-5.779635,-8.744171,4.361835,8.584898,-1.558068,1.948611,6.538337,-5.205521,-1.837334,6.503451,-8.521176,-3.826368,-2.862301,1.748465,1.738956,-1.128243,9.890023,-7.481762,-1.605568,7.549985,4.738126,-8.602070,-6.917312,-7.691912,7.660704,-6.357318,-2.318579,5.661501,7.510360,-1.533468,3.630400,4.971063,3.091649,3.199790,5.026300,-3.124473,-9.330509,1.470806,1.473163,0.631369,1.879696,-4.423642,-3.977366,-4.192808,-7.748075,-5.874313,1.899084,-5.361728,6.053989,0.796205,7.651492,9.141490,-1.221128,-8.887146,4.207683,-3.509615,-9.851316,-3.779316,7.495932,-2.936072,-2.870927,9.010435,-5.896106,-1.822824,5.033086,-0.990229,-1.726350,-4.551894,6.072755,-1.108931,-9.709040,3.447425,-1.684055,7.779682,0.233885,2.146191,1.543451,8.303762,5.730526,9.477449,7.953406,3.703520,-6.251594,-6.800824,-0.429086,-1.692313,-3.536884,8.637408,6.427725,-9.600035,1.143741,-2.751685,-7.013729,-6.361870,-8.892549,-2.365410,-3.439855,9.295162,-1.973607,-8.537789,-8.658230,7.233845,-3.210043,5.120073,-6.951817,-1.708896,-9.694258,-3.019965,2.276073,-4.316656,-6.460493,1.508150,-8.894519,2.480449,8.234300,7.101077,-3.841470,-5.497580,-6.336854,3.139208,6.866358,-4.745369,-4.289284,-2.609261,3.494966,4.023028,6.210887,-2.949766,2.596001,-7.810418,0.338786,4.192895,8.972079,8.444686,7.671369,-5.387159,-6.635810,-5.377332,0.091648,-3.075308,5.617580,-4.554157,5.695165,-1.971403,1.385034,8.859006,5.156963,-5.483899,-4.215532,-3.569751,-8.671874,-8.951685,5.033629,-1.497784,9.225703,9.823519,-0.551966,5.852728,7.902686,7.678873,0.179938,9.559099,8.599335,5.444494,9.889597,7.399568,-6.365279,1.579325,8.847874,-9.257529,-5.199255,0.344477,2.992336,-5.887115,5.205655,2.412608,-8.124467,5.132789,8.685882,1.130314,-8.311834,-3.091774,-7.621610,-9.205554,6.662526,-9.608456,-1.199376,5.945918,0.158013,-5.375829,2.098600,8.452813,6.198003,9.402463,7.309958,1.783700,3.333066,-8.758013,3.719374,3.763667,6.026118,3.865637,-6.494819,7.185271,-4.363043,-6.573253,-6.279794,-0.795291,-7.353524,-5.035233,-8.405873,1.180695,6.194643,-0.741379,-0.125767,-9.651596,4.702572,1.158184,-9.241942,4.450530,9.973479,-4.961490,5.463357,8.342806,-8.943806,0.421169,7.744916,-0.439297,-6.771036,-0.926266,0.063970,-2.330309,-1.167102,-1.989241,7.096126,4.338411,6.467650,-2.639104,-5.761037,-8.933436,3.683026,-0.123454,-9.961514,8.902568,4.054836,4.325276,-3.711261,5.120672,6.156920,4.171824,-7.878889,8.987123,-8.122041,-8.800801,9.554243,4.526161,1.640243,-5.044772,2.764337,-2.128264,9.235888,6.878738,-4.497278,-1.001754,-5.325730,-0.965451,-3.571849,-9.774468,1.872312,-5.190267,5.150787,8.890267,5.679819,-3.540061,5.216104,9.526343,-4.043437,5.624439,9.711768,-9.588168,9.926789,-7.962337,4.527240,4.247207,-7.050062,0.358901,4.589958,-7.401096,-4.264895,4.025846,9.628468,-9.627094,9.949930,-1.479496,7.660013,-4.990968,8.553842,6.985408,0.688761,4.848898,-3.614821,3.835019,7.160420,-4.597779,-4.789675,-3.877542,-4.029506,8.925562,-1.365221,-6.262788,0.656093,-2.704056,-9.245578,0.799953,-2.874686,4.860472,5.691303,7.517457,-3.032313,9.964223,5.363113,-0.881747,-8.795371,-0.896248,-7.455723,0.986049,7.833724,-0.477349,1.520043,-6.947183,4.333805,-1.673391,-1.251498,2.012079,1.899070,-2.735419,-2.134554,-0.394982,-5.522440,1.332105,3.597102,-8.887442,1.006395,-7.694984,-8.166646,-2.292615,-6.375879,8.655310,-4.255702,6.437327,5.872109,5.152062,2.557950,-0.099470,-3.112302,-4.950883,-5.751617,-2.632535,3.997117,-2.673968,7.555363,9.070929,0.793886,5.566586,-5.533027,8.737694,-4.682501,1.344118,-1.855875,0.183711,-8.296605,5.523824,4.591201,-8.368818,-0.295699,-1.521406,6.336423,-4.416421,-9.614347,6.530216,-5.839693,-2.435262,4.414181,-8.725768,-4.164606,-8.998406,0.457845,6.924605,4.266127,-5.216934,9.711086,-3.949506,-5.279539,7.283401,-0.913779,0.115829,-7.170578,0.835729,-8.438292,7.512628,7.399104,6.842169,0.246601,6.325188,-9.841578,7.112651,2.656500,-2.820611,-8.405019,-3.423925,-3.134554,2.078252,-4.919538,-7.586616,0.852771,0.189138,6.051958,6.926596,1.976177,-7.503669,-5.099355,2.752229,0.797933,-3.993543,-7.853899,-0.973455,-8.565325,9.132235,-4.013810,5.539508,3.856184,-0.789996,9.617792,-3.636159,2.070688,-0.983597,-5.183472,8.578217,-3.255751,5.340586,-1.409639,4.777010,3.480075,8.489006,4.544992,6.916529,2.937848,8.115348,-6.923863,-0.139773,-8.091097,1.742506,-6.558338,-4.796514,-4.058673,0.688293,1.416951,-5.321707,1.557880,-7.443917,-9.612334,-8.956783,-7.218898,2.284023,8.474850,-2.867362,-3.499355,-6.549436,-5.245796,8.749215,-9.715398,7.588534,-9.541417,-0.164374,-0.754725,-4.041475,8.217811,-3.193632,-0.175514,-3.889964,4.414052,-2.599987,-7.968435,9.981126,1.620369,-0.812479,4.817744,-0.433926,1.569703,-3.936577,9.640627,-5.413219,0.477591,-4.570510,-7.204487,7.171594,5.080075,-8.165226,-3.167526,-1.747105,-3.958324,5.678327,4.532536,4.110180,-9.931012,-8.486573,-6.799935,-5.517538,3.374749,-7.416094,0.443691,-3.532766,2.132219,5.057728,-4.194529,3.457719,-3.356464,-4.157540,-3.617393,-3.287505,6.017014,8.058521,5.168095,1.661940,-1.983962,9.634269,6.847439,2.847167,-4.908244,-1.182201,-0.539367,3.602481,-4.824316,-1.934477,-5.597332,-8.624408,0.375344,7.819761,2.384805,-2.507134,-5.857706,-6.284785,2.116770,-2.175000,-4.993237,-0.527087,5.776357,4.178316,7.842255,-5.493585,-3.879929,-5.275286,-9.909574,-0.708049,-1.168700,-1.496799,-7.326762,1.055468,-6.873451,1.562189,-1.442034,7.675821,-7.721416,-0.216273,9.739484,7.223362,4.625089,8.642442,2.980592,4.701733,-9.029077,9.031522,-5.669733,-9.897244,-3.793942,9.462459,9.309579,-6.438419,6.239347,-3.034948,-0.454412,-2.518383,9.130502,2.297035,-9.410137,-5.739234,-2.062904,3.466849,-0.444429,9.621935,-6.496162,-0.943253,-9.054033,7.831854,3.290937,-7.497239,6.389667,1.758184,-5.166057,3.736095,0.457427,-9.094956,7.975503,7.783181,8.242676,9.437604,5.899950,-7.578368,-6.394670,-5.702786,1.184027,0.511067,7.756641,6.360848,-5.024053,-0.095166,-8.694721,8.864423,2.551041,-4.471589,-6.725149,-1.868412,7.009383,4.470839,-3.003511,5.412282,-0.175166,-1.816008,9.299669,3.478176,-4.454781,9.962073,-3.993506,0.676116,2.330013,9.403557,6.488956,-0.451618,-2.509697,-5.473358,0.098940,-5.576972,6.379225,5.004482,-6.721700,-7.674785,7.191456,9.201389,-7.876253,0.949013,-3.119738,4.428467,-0.597359,-8.838236,7.495188,7.514259,-8.062800,-0.773612,-2.616316,-4.514668,7.341525,3.718324,0.994209,-5.542978,8.259161,6.645133,-1.189345,1.349155,-7.428419,7.115794,4.498908,-2.648640,-4.903767,9.260712,7.566167,4.993876,-2.587171,8.040381,-1.254391,7.710233,4.162676,2.018765,-8.506146,-7.658201,2.031151,-8.366086,-2.529952,-7.411945,-6.399123,1.478565,-0.820631,-5.599606,1.703726,-8.471186,3.138264,-2.427579,-5.795199,9.605065,-8.518692,-3.714279,7.668549,-0.838240,1.948177,6.030397,-6.121598,7.231944,3.744628,1.427364,0.352941,-0.064877,-7.286134,9.052387,7.616439,6.660209,-1.440790,1.619893,-5.968085,8.521484,-7.255097,2.512574,7.390826,1.405294,-4.782702,-0.579183,-9.930854,9.394921,1.661746,-1.143131,0.453746,-5.049983,4.900464,3.303679,-5.859282,8.105328,6.487549,9.543834,-2.252305,-5.226340,-4.671300,-1.086348,7.949227,7.279321,0.768585,0.823631,3.307323,-4.007111,3.221457,-3.745485,0.408464,9.594408,6.338853,9.539632,0.534403,-7.106634,-3.965729,4.113539,-8.497719,-2.142108,-1.899903,-7.960989,-7.881770,-5.888086,4.953177,5.206043,-4.820236,1.696926,9.750846,4.658493,-8.672420,-0.074873,5.109860,7.640712,-1.705104,2.579876,4.073481,-2.208266,-6.332732,-7.472289,-9.655391,-4.674343,-8.760147,-3.204380,7.239223,-2.957864,2.148285,-8.370804,-9.291844,2.862536,-0.895618,3.978995,-2.704049,6.020831,-1.002683,-5.200871,4.553349,-1.844896,6.285234,6.106186,-5.684077,-4.257376,9.974240,-7.273126,-0.174529,-3.443147,-5.142695,0.983947,-3.352169,-7.940613,-9.190897,6.312049,9.115148,5.447828,-3.690198,2.829526,-6.515695,-0.056235,5.027914,-5.380522,-8.726379,-3.637805,-5.177681,-9.343231,-7.194358,-7.784979,9.745454,-0.349347,9.450335,1.512308,-8.488925,-6.485159,6.363967,-7.315929,-6.092105,-2.586502,-6.532901,0.696585,-7.631333,7.086939,-3.935551,8.895394,5.530892,3.290291,4.819358,-5.039479,5.801020,1.930685,2.188664,0.509434,-9.852922,2.669145,-5.563465,8.979239,-5.696209,1.975343,-5.715903,-3.414311,-5.453351,-8.669136,2.023670,-9.726104,-0.962495,8.026591,3.840768,6.748316,-2.032885,-4.064655,3.648852,-5.506698,-6.155758,4.519237,-1.494432,-9.000130,4.040099,1.089469,2.583024,2.147416,0.973756,-9.331223,-8.757733,-4.779508,-8.556271,3.215418,-5.522787,7.896273,-8.818834,-5.218763,-0.588304,3.153441,5.935603,-1.776919,-8.622780,-4.528967,-0.608357,5.787711,-3.442297,-9.046491,-7.897215,7.386300,3.922120,-8.400912,7.166690,-5.838763,6.748940,8.404486,-0.187159,-3.849616,3.828744,-3.469726,2.843637,-5.834850,4.722834,-9.580339,1.781361,5.172029,-1.947188,-2.869437,-1.132825,8.151340,-1.215041,-2.506569,1.294104,-4.480561,-2.394605,-2.441643,-4.530889,6.102665,4.596226,4.213999,7.337637,1.495304,-3.066174,9.059324,4.394052,8.766315,0.408116,-5.540507,-7.615014,-0.828651,-5.844118,-3.149688,4.484341,-5.377077,5.217593,9.948728,-2.214675,-8.302234,-1.941785,6.914074,-7.550577,-2.853994,6.695346,-0.405883,5.714545,-3.889028,-2.580793,-1.882250,-4.530721,-7.431551,-6.361401,8.284572,9.156212,-6.816992,4.466192,5.258490,-7.396218,-1.185693,-6.694246,8.661109,0.006250,7.519164,-9.948183,5.201315,0.888426,-1.727803,-8.954143,-4.096086,2.467294,3.694217,6.885096,-3.985662,-6.739131,8.236438,-4.449719,-4.102722,-2.860296,0.530752,0.565732,0.545317,-5.459026,7.189212,0.988122,-2.354825,-5.754972,-5.849031,-6.284197,6.016805,1.256609,-6.312883,0.694322,3.306718,-7.230135,-0.372284,5.007307,-0.153643,5.042174,-1.283463,-3.376800,3.387498,7.800690,-7.396619,-7.353314,-6.266341,-4.366385,3.423235,-0.248494,4.253801,1.842301,-0.708035,4.605196,2.024766,-6.784109,-2.901654,-9.930239,4.522246,0.361888,-6.366414,7.232500,8.032390,9.951511,3.288878,5.379187,-7.150025,-2.000564,7.890081,-6.794258,-9.818297,6.216122,0.458225,-0.020342,6.267916,-2.568401,-9.747217,-4.112305,4.265643,-6.907051,6.585486,0.089653,2.159133,2.050874,1.825046,6.471451,-3.237220,-9.290334,-0.743322,9.520063,-4.916660,7.480449,9.446862,-0.065547,2.381261,-7.244896,-9.236815,2.427781,5.178777,4.913156,-4.125872,1.439650,2.634252,-0.222473,-2.065012,5.706744,6.909467,0.093370,-1.099266,0.778077,4.809111,5.816499,0.427348,5.681296,3.528436,1.488941,7.400691,-4.564267,6.028114,-8.433910,-4.170566,-1.854734,1.038084,2.393487,-0.655125,6.015578,-0.682588,6.243172,9.385752,-3.233186,0.196764,-8.532383,-1.501738,2.709152,3.935089,-0.462960,4.494219,2.362290,-6.403560,8.721353,4.884473,-1.158790,6.766434,4.500700,-0.040401,2.066843,-4.116261,-5.029731,-0.272317,-4.617640,-8.415011,-2.874729,7.923604,-4.545979,-6.603276,-5.369928,-3.175420,0.077581,5.484809,9.093207,-0.159831,1.496017,-6.116865,-0.895304,-1.151477,0.810296,5.531467,-8.788007,5.743898,-8.113736,-0.960880,-8.209882,-2.599146,-0.581006,-9.051856,1.918975], dtype = "float32")#candidate|8884|(1152,)|const|float32
call_8882 = relay.TupleGetItem(func_3226_call(relay.reshape(const_8883.astype('float32'), [13, 10, 8]), relay.reshape(const_8884.astype('float32'), [1152,]), ), 5)
call_8885 = relay.TupleGetItem(func_3230_call(relay.reshape(const_8883.astype('float32'), [13, 10, 8]), relay.reshape(const_8884.astype('float32'), [1152,]), ), 5)
func_7039_call = mod.get_global_var('func_7039')
func_7041_call = mutated_mod.get_global_var('func_7041')
call_8892 = relay.TupleGetItem(func_7039_call(), 2)
call_8893 = relay.TupleGetItem(func_7041_call(), 2)
var_8898 = relay.var("var_8898", dtype = "float64", shape = (845,))#candidate|8898|(845,)|var|float64
bop_8899 = relay.less(uop_8875.astype('bool'), relay.reshape(var_8898.astype('bool'), relay.shape_of(uop_8875))) # shape=(845,)
output = relay.Tuple([call_8825,call_8867,var_8869,call_8880,call_8882,const_8883,const_8884,call_8892,bop_8899,])
output2 = relay.Tuple([call_8826,call_8870,var_8869,call_8881,call_8885,const_8883,const_8884,call_8893,bop_8899,])
func_8903 = relay.Function([var_8868,var_8869,var_8898,], output)
mod['func_8903'] = func_8903
mod = relay.transform.InferType()(mod)
var_8904 = relay.var("var_8904", dtype = "float64", shape = (845,))#candidate|8904|(845,)|var|float64
var_8905 = relay.var("var_8905", dtype = "uint16", shape = (3, 60))#candidate|8905|(3, 60)|var|uint16
var_8906 = relay.var("var_8906", dtype = "float64", shape = (845,))#candidate|8906|(845,)|var|float64
output = func_8903(var_8904,var_8905,var_8906,)
func_8907 = relay.Function([var_8904,var_8905,var_8906,], output)
mutated_mod['func_8907'] = func_8907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4186_call = mod.get_global_var('func_4186')
func_4188_call = mutated_mod.get_global_var('func_4188')
call_8940 = relay.TupleGetItem(func_4186_call(), 0)
call_8941 = relay.TupleGetItem(func_4188_call(), 0)
func_6996_call = mod.get_global_var('func_6996')
func_6997_call = mutated_mod.get_global_var('func_6997')
call_8949 = func_6996_call()
call_8950 = func_6996_call()
uop_8978 = relay.sigmoid(call_8940.astype('float64')) # shape=(12, 6, 10)
uop_8980 = relay.sigmoid(call_8941.astype('float64')) # shape=(12, 6, 10)
func_1120_call = mod.get_global_var('func_1120')
func_1125_call = mutated_mod.get_global_var('func_1125')
const_8985 = relay.const([6.577938,3.018405,-6.217740,-4.109388,-2.062184,-0.609823,7.697375,-4.151742,-9.774494,5.525659,-5.323883,-3.459618,-1.710159,-6.457396,-2.382752,9.327344,1.456362,-2.346630,-1.245783,2.758998,-6.176096,-4.638901,1.529057,0.835811,0.839745,-5.810616,3.343886,-2.811975,-2.264987,3.890752,5.179793,-7.333029,6.086074,-1.053174,2.450479,7.780606,6.001914,7.354541,-7.347688,-0.273891,7.208721,-6.104814,-2.075454,-4.511280,8.414700,0.306475,5.330646,6.124028,4.911825,-6.063680,-6.678121,-6.786357,8.546370,-6.908146,4.351393,-3.102581,-0.107667,9.784903,7.784075,3.271998,5.759987,0.602606,-1.936079,-9.293882,4.805107,-2.838403,-0.421165,8.046247,-6.075411,6.902661,8.212180,1.839358,-9.990378,-9.640370,-5.306827,-9.109169,-0.152757,-5.645550,8.517068,-0.926754,0.317918,-6.726687,-2.246796,-8.096237,0.122674,-2.008389,9.171518,-4.375039,-3.367400,0.295592,-9.904417,-9.948178,3.302098,3.919213,0.109614,8.492934,-0.115389,-0.390735,-1.328967,-1.780592,9.333256,-1.828588,-1.567952,-0.821994,5.471240,7.824174,-2.589619,-3.640739,1.107549,-5.436434,-5.830660,0.008974,1.176725,5.336947,-8.158614,6.882481,-7.498232,-8.869230,8.431176,7.961071,-1.540514,-0.157184,-4.097691,4.535775,3.154047,6.798377,2.041066,-6.190333,-3.989107,-8.034777,6.899476,-4.258434,3.050983,-7.722374,-2.623239], dtype = "float32")#candidate|8985|(135,)|const|float32
const_8986 = relay.const([1.836453,1.391678,4.499308,-5.113838,-7.162942,8.645816,-6.136740,-2.408147,0.862358,-4.723291,6.021540,-6.410607,-5.531693,3.431368,-9.374190,-0.784710,-3.217477,-8.163025,-3.595133,-0.600423,-4.105625,5.288495,-6.467508,-5.660784,-1.448759,4.634031,-3.630652,2.382764,-6.784776,8.342041,4.062888,-7.163897,1.673247,4.065434,2.480780,-5.894101,-9.136711,-2.959232,0.424353,-9.296002,-9.758910,1.331776,1.152247,8.340662,9.286653,-4.811952,-4.218561,-2.211334,0.278498,6.701675,-7.912860,1.663351,-8.292502,7.543706,-8.119858,9.015160,9.928419,5.011551,9.183980,1.756778,4.099075,-9.929103,-8.315093,7.584619,-7.360658,3.996702,-3.094436,1.892721,-5.185902,-8.702121,-5.567290,3.269040,-2.100949,7.935988,-9.641155,-1.413466,-2.094532,6.999247,-6.551699,9.961494,-6.409600,9.347615,2.919160,2.853011,2.719003,-2.350659,7.461285,9.162830,-7.292062,3.231974,6.660918,0.073385,-5.827780,2.425041,3.917046,-3.519129,3.766348,6.878812,-0.799838,-2.415557,-7.076692,-8.132586,6.337408,-3.413423,-4.318159,-4.710407,8.914407,1.679350,-9.750843,-2.749376,9.922482,7.804793,-7.302035,2.919614,3.520025,-0.638503,-8.531394,7.551661,9.409841,-5.382369,-9.768968,9.055071,-5.644523,4.935646,4.743400,-9.140284,-4.852602,4.996006,-2.229310,-9.637517,0.834877,-2.837068,7.126573,8.232903,7.711871,-6.584800,-1.107634,4.250557,-2.645014,9.250370,5.525234,4.499371,-8.098907,-4.772703,2.016444,-7.493662,-9.305896,3.577272,6.245005,-4.453046,-5.822307,-4.717147,-7.963506,3.656343,-0.607789,0.803741,-2.121688,-1.259993,2.581319,-8.106060,9.837946,1.382037,4.896140,5.921329,0.950993,8.375146,-8.947994,-5.185398,2.816769,9.646277,1.498495,8.791348,2.734504,-0.938020,6.992572,-6.041542,1.365677,-6.476729,-6.472402,4.177829,6.589668,0.490552,-8.241538,-2.280505,0.045867,-9.966449,-2.059579,-7.285545,1.724703,7.457716,2.983344,9.209999,1.282527,3.308218,5.007520,-2.510886,4.546828,-9.413691,0.185503,-8.142762,-3.323861,7.892232,-0.679415,7.204257,-0.736272,-1.143151,-2.939291,2.993650,0.067006,2.217499,1.516061,9.031844,7.419016,2.506707,5.960940,2.828847,-7.576039,-2.575019,-7.095889,-9.232197,-3.630047,5.924014,-9.720736,8.313844,0.518964,-0.494212,-0.166301,-7.638627,2.416717,-0.441078,5.881446,-5.482399,0.784941,-3.357395,-4.999430,-3.713021,-6.873170,2.915685,-8.048145,-7.843526,2.258440,3.650788,4.087345,8.254590,7.322649,6.197303,1.175447,-9.370642,-7.749299,0.155491,6.335523,-7.236678,3.072653,-4.941589,-3.030567,8.784192,8.196109,4.216907,-7.948017,9.709721,-8.251286,-0.551141,-7.203485,-2.188364,-0.610654,-8.992655,-7.157824,1.307271,-1.142157,6.331556,-1.419539,8.863220,1.838789,-6.089248,6.230119,0.845147,-7.134641,-0.136224,-3.572473,-8.923527,-4.269380,-2.622763,1.162443,-9.169330,8.213764,-9.439855,-3.620919,1.408261,-1.705861,-9.081991,7.769939,6.741111,9.482772,7.499187,6.688089,-7.163891,-5.179875,-0.788428,-5.284963,0.907177,-2.180571,-6.009049,5.891237,8.509554,1.438051,-5.281907,9.862150,8.401884,8.849519,8.000438,-9.584982,-4.857375,-2.298117,-3.681388,5.201604,2.849790,5.826247,-1.036497,4.633528,-5.424450,0.375079,-7.815908,-4.772836,-0.888627,-1.425188,-5.824794,6.461185,9.406327,3.791744,1.371833,4.320562,0.919454,-6.701249,-3.044412,5.782732,-0.689092,0.816935,8.331647,-7.996177,3.217049,0.494910,8.215292,-6.897204,9.630812,-4.550410,-0.103221,5.480623,-2.859010,6.160755,6.476724,5.512197,-3.599576,-2.042072,5.195360,1.324051,7.388906,-2.512183,1.853589,1.895527,3.287464,4.145050,-8.636731,3.273155,-9.880978,6.349716,2.693335,-2.928491,0.945026,7.304283,6.875656,1.626689,-2.481407,-4.475143,-8.708573,-5.939851,9.939535,8.602649,-8.483307,1.354599,3.584686,-0.805841,1.074096,-1.064283,-9.993694,8.958302,-8.153524,-7.824546,8.755636,7.698770,5.199669,9.799935,9.256655,-0.103384,4.906363,0.549475,-3.428265,6.621389,-3.339642,-4.790613,0.190396,-5.729485,-6.877664,-3.697100,8.189779,4.334920,5.020384,-6.533444,4.752741,-6.330849,-7.408407,5.894645,-6.221738,-8.288882,6.352786,3.028154,9.123821,-7.888913,-6.431377,5.302696,-4.177761,-9.277310,0.036817,3.660919,1.376656,7.962497,4.810711,-6.002425,6.154869,-3.970361,7.647124,4.134726,3.612516,-7.655169,2.499549,-6.870368,-2.076198,4.818764,6.078097,-0.188428,1.143260,-2.082525,8.222013,-8.538247,8.784389,1.266557,-5.230425,0.700013,-5.363140,7.096538,3.937883,-4.188096,1.852597,1.671218,-9.509273,1.363359,7.499792,-3.577747,2.269491,5.589007,5.489127,1.929811,-7.668003,7.518304,0.347796,-6.910548,-4.889652,-0.994797,-8.066665,-2.510634,-1.947774,-8.149926,3.785836,-3.676046,0.688770,-8.743297,-8.301581,-7.431703,-6.720476,5.794326,5.492525,8.017373,-9.540552,9.897458,3.684641,5.571937,4.919125,-3.190750,-1.275951,9.617589,-2.914396,-9.691509,-9.318801,5.306616,7.075926,-5.646946,-4.257925,-8.168435,9.905202,-1.826612,-6.471775,-3.062592,7.708126,-2.695839,4.794211,-7.397798,1.360086,-1.003686,5.097969,2.482887,4.617708,3.661946,1.245868,-5.093359,1.149677,6.974298,5.934737,-2.536004,-9.119819,-0.973673,-8.862138,-7.395748,-0.854631,8.619831,-3.839384,-7.678489,-2.774476,-6.750787,9.176179,0.310820,4.130818,-9.593925,-4.479632,6.643515,-1.058612,7.652607,-7.871916,-0.675685,-6.856021,4.529387,-8.350042,-0.869059,4.589601,-8.855678,-2.217440,-7.410781,2.333102,-7.905345,4.785649,-7.762855,4.501103,-1.439223,3.518190,-6.043398,3.317583,2.687532,5.028928,-9.533697,-0.194376,-0.815887,-8.448639,-8.971768,5.806479,-3.841031,-9.387301,-9.726806,-2.284785,-3.944307,-3.587313,7.021066,-2.940903,6.813919,9.754845,-4.907941,2.006381,-5.598653,3.929005,7.785033,8.307704,6.095246,-7.856892,4.221186,0.997564,2.403493,4.586629,7.131471,1.527883,4.334236,-3.334965,-8.297613,-3.492202,-0.942685,6.350133,4.935673,8.075521,-9.564548,-6.585003,-1.775171,1.509367,2.572647,-7.904048,-2.164779,-0.262689,-8.383028,-6.135196,-6.115960,5.423879,-7.527907,-3.104647,6.166121,0.002065,5.455018,-0.928876,4.301822,1.123559,-6.913890,2.126355,2.940792,-3.152486,-5.085921,-5.786904,-9.766459,6.116769,-6.758127,-4.400946,8.877394,-7.013259,2.575851,-8.151180,-5.209093,-7.961650,-6.484569,-7.444299,8.332577,8.969076,9.872552,-6.455030,-6.885711,-8.227348,9.915785,-9.011986,-7.454674,0.888894,8.154434,-0.094567,-4.734747,-4.838147,-3.404189,-0.121528,-3.631154,-6.430197,-3.428864,9.807451,-0.001325,5.024434,-2.958968,8.668329,-6.358270,-6.912787,-2.122181,-5.346671,7.110277,7.688759,2.374324,6.132215,-9.823270,9.877679,-3.227506,6.260627,-6.751820,-4.734926,-8.240867,-4.564442,2.717417,4.070333,9.198108,-2.492054,-9.589794,8.642791,3.625574,7.142162,-8.599368,-5.757194,6.355590,6.679463,8.320497,-3.429953,8.361457,-3.442742,-9.038959,9.923354,3.761126,-5.035987,5.618908,6.504425,4.350348,-0.589215,6.511897,-1.784050,-5.127653,5.252013,-7.638783,-6.720224,-6.291853,-6.290769,-5.684385,-4.979192,5.493367,6.998745,-3.435950,6.540969,-9.220274,0.342714,0.379165,-6.099955,-1.237603,1.976838,-0.501207,-1.452608,-0.381543,5.756653,-6.306845,3.697452,-3.793829,9.049370,5.918955,-9.534488,-7.311551,-9.251793,-9.734822,-8.557813,-5.936637,2.649850,1.427429,7.850262,-5.721540,-4.144898,-4.913291,-6.271132,-8.631273,-5.567612,-4.271287,7.005465,-4.853292,-5.928370,2.222758,1.413933,-2.408258,-0.973450,9.440672,-5.311161,-6.317890,-3.463108,-7.360246,4.498024,-4.065718,-9.617845,2.743710,-5.807244,5.616236,-2.354033,2.754717,-7.900337,-0.104756,6.626477,-6.251970,3.423758,-4.322723,-0.967673,-1.573504,6.409015,4.133249,0.142639,-5.723946,-0.783672,9.961387,-6.391499,6.390953,-7.136006,9.080237,7.154590,8.953532,-3.357893,-4.100310,-8.058120,-6.884749,-0.424610,-2.924197,-9.069241,7.833279,-3.531941,6.358567,5.701106,-4.450077,-3.538696,8.959755,6.944272,-4.859225,-7.859495,-2.800837,8.452059,-7.247037,-0.627973,-0.387201,7.477503,-0.979529,-0.928503,-0.230145,-1.021869,5.463575,-2.163316,-7.243648,-9.119663,5.751498,8.276297,2.236082,5.440140,-4.882403,-5.147373,-3.860231,-2.893836,-9.473341,4.183923,-5.603233,8.238172,-9.267345,-3.046142,1.062022,-3.981243,5.056678,3.031013,-9.976946,1.164010,-8.835254,1.280028,8.484414,4.426029,-8.495612,2.445011,-6.505325,8.732444,-7.972999,1.592986,-1.912117,2.953201,-2.612393,-6.231029,9.109003,7.023688,-7.027606,-2.366027,5.902059,2.024414,-6.073665,-2.732497,4.003816,-6.534457,-3.281705,2.764783,8.381330,-7.845823,2.050666,-3.987039,-6.304760,0.993539,3.068657,2.411433,4.081347,-4.554807,6.513596,3.764039,-0.499179,-7.554065,9.503953,3.958573,-5.947811,-9.750330,0.496255,-2.360095,3.961079,-9.174880,-0.637776,7.973332,-9.371250,1.887007,-0.477076,-9.827597,-7.898222,7.962641,-1.171721,-5.637315,9.604701,3.726019,-3.483591,-4.948888,4.127756,-7.891461,-8.287386,0.954230,5.305271,-2.028286,6.679980,5.994341,-0.544050,-9.252042,6.640181,7.635692,0.819511,5.703419,2.988404,7.270552,-9.559695,-7.417063,1.997372,6.429603,-3.150188,3.950529,-3.053016,-0.312233,6.207328,-1.059064,8.263424,2.676893,-8.099663,-5.906058,3.446890,-5.007777,1.929606,-9.625768,-3.681551,-2.132620,-0.617231,6.423759,-9.979249,5.447914,-0.445499,-9.707403,6.116069,-7.410719,7.372295,6.659110,9.807010,-6.835109,-7.651301,0.309169,2.464704,-9.053436,8.733946,-7.655231,6.814973,-5.930455,2.079577,5.837790,-0.113872,-6.666284,6.138392,-5.955225,8.894690,1.107463,-0.853737,5.273263,-5.682072,0.404846,4.411311,0.967830,4.955974,-1.683236,9.732806,1.252616,7.128043,4.125202,-1.615332,1.581795,-3.636385,6.996092,-9.494414,-9.188727,-4.200835,-2.545806,-5.955819,-9.293387,2.926954,-1.365368,3.096405,3.513866,-8.865430,8.899009,-9.703425,-3.652906,1.662911,1.715607,-0.030619,6.699148,0.117411,-6.984655,6.629412,7.263214,3.054190,5.498368,-6.321649,-5.685330,0.562824,5.746744,-8.009274,7.580678,4.941074,1.736088,-0.251556,2.894901,0.029385,4.283902,-7.254132,6.507286,9.908589,-4.856519,3.516874,-1.956000,-0.130011,5.251274,9.827139,3.084333,6.951091,1.875197,6.039928,-8.591417,-6.673359,3.486860,-3.905923,9.712251,-8.743440,4.798328,-4.897983,-6.759032,6.295980,7.654103,-2.209200,-1.930249,-1.936252,-1.762927,-6.968211,-0.402657,-5.262853,5.270521,-4.796859,-7.724990,0.140901,1.257573,4.673460,-2.088915,6.573104,-6.704210,-6.816123,3.910055,-1.559896,-4.767703,-6.338892,4.189236,7.802606,-5.570209,3.594710,-9.862620,-1.685849,-5.254442,9.967876,6.536705,2.538329,1.938601,-5.888180,-6.600706,-6.442946,0.774453,2.002089,5.466414,3.519374,-3.882408,0.488354,7.890118,-7.677593,5.165563,9.538564,-7.842538,-8.722712,-4.999669,3.522096,3.225524,-0.038276,-2.129754,-5.259474,-6.886030,3.811434,-7.659385,5.441862,0.734905,-3.145396,6.765384,7.560268,-1.569890,8.937348,-8.213174,7.869069,-2.741435,-8.599553,5.539002,4.288268,-1.319099,-8.482562,5.624964,1.093888,-0.023591,6.395582,0.087033,4.271292,5.280051,-9.302819,4.378150,5.347959,0.446725,4.403154,-6.409744,-0.174286,4.658718,-8.915520,-2.944612,6.660336,1.952640,6.147736,1.945978,-2.038284,5.462769,-7.268394,-1.260594,3.662729,5.719793,-1.237112,7.714716,9.439593,9.507106,7.509244,7.016218,-4.230679,0.510830,5.504204,2.408300,8.691740,-1.545187,5.031512,-4.309709,4.529221,4.934311,1.513538,-5.284696,-8.364057,-0.570013], dtype = "float32")#candidate|8986|(1152,)|const|float32
call_8984 = relay.TupleGetItem(func_1120_call(relay.reshape(const_8985.astype('float32'), [9, 1, 15]), relay.reshape(const_8986.astype('float32'), [1152,]), relay.reshape(call_8949.astype('uint16'), [180, 1]), ), 3)
call_8987 = relay.TupleGetItem(func_1125_call(relay.reshape(const_8985.astype('float32'), [9, 1, 15]), relay.reshape(const_8986.astype('float32'), [1152,]), relay.reshape(call_8949.astype('uint16'), [180, 1]), ), 3)
uop_8992 = relay.asinh(const_8986.astype('float32')) # shape=(1152,)
output = relay.Tuple([call_8949,uop_8978,call_8984,const_8985,uop_8992,])
output2 = relay.Tuple([call_8950,uop_8980,call_8987,const_8985,uop_8992,])
func_8995 = relay.Function([], output)
mod['func_8995'] = func_8995
mod = relay.transform.InferType()(mod)
mutated_mod['func_8995'] = func_8995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8995_call = mutated_mod.get_global_var('func_8995')
call_8996 = func_8995_call()
output = call_8996
func_8997 = relay.Function([], output)
mutated_mod['func_8997'] = func_8997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6570_call = mod.get_global_var('func_6570')
func_6571_call = mutated_mod.get_global_var('func_6571')
call_9004 = relay.TupleGetItem(func_6570_call(), 0)
call_9005 = relay.TupleGetItem(func_6571_call(), 0)
output = relay.Tuple([call_9004,])
output2 = relay.Tuple([call_9005,])
func_9011 = relay.Function([], output)
mod['func_9011'] = func_9011
mod = relay.transform.InferType()(mod)
mutated_mod['func_9011'] = func_9011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9011_call = mutated_mod.get_global_var('func_9011')
call_9012 = func_9011_call()
output = call_9012
func_9013 = relay.Function([], output)
mutated_mod['func_9013'] = func_9013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3981_call = mod.get_global_var('func_3981')
func_3982_call = mutated_mod.get_global_var('func_3982')
call_9020 = relay.TupleGetItem(func_3981_call(), 0)
call_9021 = relay.TupleGetItem(func_3982_call(), 0)
output = relay.Tuple([call_9020,])
output2 = relay.Tuple([call_9021,])
func_9036 = relay.Function([], output)
mod['func_9036'] = func_9036
mod = relay.transform.InferType()(mod)
mutated_mod['func_9036'] = func_9036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9036_call = mutated_mod.get_global_var('func_9036')
call_9037 = func_9036_call()
output = call_9037
func_9038 = relay.Function([], output)
mutated_mod['func_9038'] = func_9038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8556_call = mod.get_global_var('func_8556')
func_8558_call = mutated_mod.get_global_var('func_8558')
call_9098 = func_8556_call()
call_9099 = func_8556_call()
output = relay.Tuple([call_9098,])
output2 = relay.Tuple([call_9099,])
func_9116 = relay.Function([], output)
mod['func_9116'] = func_9116
mod = relay.transform.InferType()(mod)
mutated_mod['func_9116'] = func_9116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9116_call = mutated_mod.get_global_var('func_9116')
call_9117 = func_9116_call()
output = call_9117
func_9118 = relay.Function([], output)
mutated_mod['func_9118'] = func_9118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8173_call = mod.get_global_var('func_8173')
func_8174_call = mutated_mod.get_global_var('func_8174')
call_9150 = relay.TupleGetItem(func_8173_call(), 0)
call_9151 = relay.TupleGetItem(func_8174_call(), 0)
output = call_9150
output2 = call_9151
func_9155 = relay.Function([], output)
mod['func_9155'] = func_9155
mod = relay.transform.InferType()(mod)
mutated_mod['func_9155'] = func_9155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9155_call = mutated_mod.get_global_var('func_9155')
call_9156 = func_9155_call()
output = call_9156
func_9157 = relay.Function([], output)
mutated_mod['func_9157'] = func_9157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_9158 = relay.TupleGetItem(func_2625_call(), 0)
call_9159 = relay.TupleGetItem(func_2626_call(), 0)
output = call_9158
output2 = call_9159
func_9171 = relay.Function([], output)
mod['func_9171'] = func_9171
mod = relay.transform.InferType()(mod)
output = func_9171()
func_9172 = relay.Function([], output)
mutated_mod['func_9172'] = func_9172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5727_call = mod.get_global_var('func_5727')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_9203 = relay.TupleGetItem(func_5727_call(), 0)
call_9204 = relay.TupleGetItem(func_5728_call(), 0)
output = call_9203
output2 = call_9204
func_9208 = relay.Function([], output)
mod['func_9208'] = func_9208
mod = relay.transform.InferType()(mod)
output = func_9208()
func_9209 = relay.Function([], output)
mutated_mod['func_9209'] = func_9209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7416_call = mod.get_global_var('func_7416')
func_7417_call = mutated_mod.get_global_var('func_7417')
call_9224 = relay.TupleGetItem(func_7416_call(), 0)
call_9225 = relay.TupleGetItem(func_7417_call(), 0)
output = call_9224
output2 = call_9225
func_9230 = relay.Function([], output)
mod['func_9230'] = func_9230
mod = relay.transform.InferType()(mod)
output = func_9230()
func_9231 = relay.Function([], output)
mutated_mod['func_9231'] = func_9231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2502_call = mod.get_global_var('func_2502')
func_2504_call = mutated_mod.get_global_var('func_2504')
call_9234 = func_2502_call()
call_9235 = func_2502_call()
func_7624_call = mod.get_global_var('func_7624')
func_7627_call = mutated_mod.get_global_var('func_7627')
const_9240 = relay.const([True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,True], dtype = "bool")#candidate|9240|(490,)|const|bool
var_9241 = relay.var("var_9241", dtype = "float64", shape = (1, 845))#candidate|9241|(1, 845)|var|float64
call_9239 = relay.TupleGetItem(func_7624_call(relay.reshape(const_9240.astype('bool'), [7, 70]), relay.reshape(var_9241.astype('float64'), [845,]), ), 0)
call_9242 = relay.TupleGetItem(func_7627_call(relay.reshape(const_9240.astype('bool'), [7, 70]), relay.reshape(var_9241.astype('float64'), [845,]), ), 0)
func_8014_call = mod.get_global_var('func_8014')
func_8019_call = mutated_mod.get_global_var('func_8019')
const_9248 = relay.const([-1.349220,5.190825,-2.238619,1.801225,0.094343,-7.055183,3.431033,-1.137371,-8.946327,-7.424800,5.704455,7.182508,-5.954107,-7.192452,6.622443,1.429809,7.138890,5.080174,-9.792488,3.248600,0.685622,8.511195,-5.588661,3.435457,2.003320,1.109397,3.060017,-1.970623,5.444742,-9.923573,-9.750639,5.322088,-7.747148,-8.345950,8.286214,-3.099998,5.307547,-3.099778,6.162606,-8.259459,9.398833,8.090825,-9.221449,0.854708,-8.128775,-0.742396,8.387706,-8.443659,-3.258954,-8.486865,3.570605,-8.831528,-4.816595,-4.469889,-2.115779,7.384092,-7.378904,4.429158,-8.065671,0.409878,-3.350995,7.645948,8.975933,5.930852,-8.674863,2.003534,-3.175196,-7.724231,-5.826556,8.960957,9.360489,4.118590,2.901663,-3.192786,5.172717,4.096417,0.465612,2.997448,-4.448783,-0.591113,3.062947,-1.455535,-0.152228,-4.633839,8.119163,3.368062,-1.466171,4.863633,9.638835,4.327270,9.631022,-0.710978,-0.601840,8.069580,-1.767043,4.165514,8.914444,-8.189670,3.083571,1.060467,-7.251136,1.338799,6.635433,-2.528757,2.818490,6.204091,-1.660184,7.465245,2.039901,-1.047460,1.548741,8.199118,8.804942,-5.435301,8.927841,-9.167624,-8.670179,-0.876084,-4.390523,5.715474,8.360164,-8.573940,-5.549766,-5.360464,-5.691370,-4.880861,-7.745138,-2.045771,2.677181,-2.975485,-7.195143,-1.355157,5.469214,-1.305643,2.828222,1.498617,-0.864479,4.084551,4.867003,1.787632,-2.673230,6.992513,6.194338,-3.926856,-9.257909,0.292905,2.518082,-9.438214,0.499835,-5.178274,-1.208153,1.698346,6.185995,1.643189,-0.852815,-6.963800,-2.053361,3.449576,-8.989316,-3.467361,2.937852,0.275552,9.696528,5.045121,7.137227,-8.668865,5.224661,-9.894520,-9.389215,7.152411,-3.028628,7.251387,-1.214386,9.935891,-1.393393,6.611531,3.835439,0.675304,-8.915142,1.934104,-6.677942,0.963417,1.045678,7.564090,-4.350803,-6.745327,-5.017894,4.111695,8.059435,1.438336,3.732683,3.371021,-3.513916,1.290325,7.009655,-7.581292,-1.997342,2.024470,8.473387,2.715232,5.868345,2.934548,4.526488,-7.340693,5.302096,7.338923,0.936564,3.825486,0.214878,-5.790385,-6.953459,-9.318191,9.360836,-9.194936,-3.945993,-4.353911,-4.822188,-5.634948,-0.069676,-9.776674,-4.373901,-5.145044,-1.111979,3.441142,9.149515,-6.977407,-6.186712,-7.070243,-1.575937,6.524964,2.637546,-2.916597,7.253139,2.580840,-9.043106,8.173983,9.375872,-2.619213,1.680038,7.271361,1.709342,-4.130347,1.229747,4.305306,-3.022209,-2.735214,-0.143935,6.120962,0.915922,-5.836272,-3.633896,7.841600,2.859021,8.437852,2.097253,2.387220,-5.946258,7.621985,3.446096,9.101910,6.458497,9.699190,-9.204812,7.514050,6.750551,0.259551,3.752212,-0.671609,-3.018751,4.296476,-0.315437,8.634543,5.895161,-6.460266,5.814541,-0.710767,-2.046886,2.867703,-4.390594,-5.492218,-8.363694,1.892017,-6.862439,-1.013619,4.651648,7.885104,4.670564,-0.900711,6.907516,9.610641,-3.474739,4.047051,9.732342,3.301964,3.007061,6.726845,-6.322653,4.033356,-7.877517,0.654898,5.634243,-7.376503,2.106568,4.379162,8.533574,-3.194649,-2.781575,-2.628778,-2.214570,7.546796,-2.942997,4.476267,6.622177,8.790097,-5.321825,5.535504,1.950651,-5.906350,-5.673972,9.241017,-2.074242,0.350934,4.523467,-4.584081,-0.422286,4.228440,2.376967,7.909527,5.761156,-3.542859,5.055294,-1.373335,5.345985,-1.153590,-7.811153,-3.360487,3.414676,-7.179368,0.804060,-1.417943,-5.945835,-3.592358,-1.237910,1.671853,9.989642,5.689239,4.954208,4.742943,3.251288,9.801316,-9.091173,-1.818173,9.366800,-7.996528,-0.914407,-5.965368,3.916344,-7.409431,-0.678763,3.836934,9.368608,7.011794,-3.331791,-1.312678,-7.950622,-1.686418,8.539000,-7.415159,2.760710,6.441436,9.273790,-6.567225,6.184479,-7.906859,-7.497887,6.595205,-5.964695,5.059503,0.429765,-3.507334,0.936346,-3.478390,-6.602610,2.836807,-9.739268,0.970829,1.189680,-1.679272,-2.411994,-5.833278,-1.018272,-9.190198,-7.552132,-2.855310,7.490474,9.562571,5.282043,7.736612,-4.584684,2.902969,-6.366154,-7.174207,-0.680730,-2.139535,3.509190,-6.539068,-5.434543,7.890391,-7.208264,-4.184180,-6.464834,-3.246980,-8.543564,5.588703,-4.898078,1.461418,7.058649,-8.862079,-8.322612,-2.020974,-0.402622,3.419076,-4.749061,5.993905,-4.715458,-8.643533,-0.636288,-8.550554,5.297861,1.368432,-5.363936,-9.752416,2.941710,-6.405659,4.628269,4.521249,8.101850,-5.441371,6.104685,-9.533927,5.565880,3.544785,5.309903,-6.381701,9.552296,-4.377153,-2.370952,-8.038237,-3.153861,0.406683,9.769347,3.068136,-3.637047,-5.266637,3.217807,7.519538,-7.088612,-8.943162,6.212431,-8.185013,8.170958,-7.481278,1.678648,7.736380,4.498633,1.241334,3.809395,6.557440,-7.959084,-9.991479,-0.658523,-6.636715,-8.643054,-2.344670,-3.104245,-6.245994,-5.210252,6.329665,3.463159,0.325003,-0.306765,-4.649125,4.129519,5.734909,5.819916,7.805163,2.279534,-8.652062,4.723136,0.869663,7.507784,8.077595,9.980329,5.576007,2.997715,3.349236,3.779514,6.636359,-0.281273,-8.340231,-7.320054,4.734982,-0.286074,4.163548,0.335656,9.403855,0.658879,-2.895878,6.194505,6.338364,-8.767197,-9.694222,-7.689486,-0.875440,-4.526173,0.040663,-0.449267,3.156887,-7.095396,-0.916533,4.188132,2.495687,-5.728996,6.361677,7.242795,-3.224327,-6.502003,-0.076177,1.722332,4.777727,6.795240,-1.528636,2.400546,-0.489748,2.131593,5.010597,-6.423215,3.359948,-3.768041,7.990334,0.249574,5.973629,-0.463613,8.688420,-5.523475,-5.922927,6.226133,-0.802895,-8.927615,-4.463928,7.964987,-7.383768,-5.174155,4.356498,3.761580,9.474679,-5.474904,-7.910600,-5.218180,-3.985930,-1.730474,-8.811144,-4.569400,-2.483934,-1.117330,-6.327689,4.814795,3.910268,-8.793645,-1.579120,7.625385,-6.336302,2.671047,7.869067,-7.952460,-8.429664,-1.216281,-9.426073,3.942638,0.197108,-5.810641,-4.971905,-9.134717,2.068882,-1.085381,-4.946670,0.530795,4.481136,9.690398,-9.084976,4.773599,-3.382935,-1.389973,-8.809505,-7.045681,5.618573,2.447252,-5.263947,8.441624,-1.533301,2.172906,-8.357731,4.145536,4.320422,-7.409579,3.133675,8.745215,2.787422,-9.143670,9.984725,7.877671,5.436059,-2.456234,-1.006189,-7.275001,2.973185,-0.545146,-4.608170,-3.323270,-7.185939,-3.311385,-7.814254,-9.348988,4.577083,7.352963,4.711601,3.684928,9.433319,-7.689802,3.184021,-6.563646,-5.135548,-8.144565,-4.685709,1.592855,8.476020,-4.419092,6.747409,4.679312,-1.067873,6.441919,7.325320,-9.163049,3.315600,2.664648,1.626357,3.112128,-8.520617,2.602265,-2.996873,8.356172,-4.453823,8.706722,-9.213473,-6.494039,1.810390,-2.885101,-6.878221,7.563581,8.933595,-9.365542,-4.848595,6.567684,-2.886734,-3.072604,3.746831,-9.493409,0.695713,0.377083,7.335674,-8.696193,9.177402,9.982805,-4.721770,2.601007,0.224214,-9.046230,-2.295049,-7.531486,-8.670697,8.806421,1.144845,1.231958,-7.993302,-8.189014,-1.537946,-7.354556,-1.711113,6.436134,9.541720,-8.438505,3.718914,-6.910255,-8.968019,-9.986322,1.444376,-1.489730,7.587953,-2.738842,-5.736699,5.232647,4.451844,9.548230,-8.238654,-3.026064,4.971517,-8.884635,-5.252082,-9.484667,-5.567270,8.003836,4.187352,-8.082523,-1.770538,-9.866967,1.816621,0.818298,6.905535,-7.661638,-2.745888,0.974475,-5.951777,-8.572571,5.048257,4.902763,3.531544,4.791254,8.953703,9.174631,-1.207073,-0.511034,-0.862534,3.157886,-4.086210,7.355109,-1.403055,1.531539,-8.514958,5.736715,-2.273989,8.631239,-6.078355,-6.680175,-7.185377,3.967829,2.350035,2.998378,4.274408,-1.064926,-1.386033,-1.878564,-3.425060,5.854588,7.959794,-9.563741,-8.366698,3.074474,5.679419,-5.953287,-7.731504,-6.743713,3.757218,4.602658,-3.078399,1.269038,4.615108,-3.210698,0.598630,-5.627669,-0.951775,-6.080170,6.223972,2.821238,-7.887983,-8.754149,3.729510,-8.343531,-8.149155,-0.019952,3.619137,-3.341644,7.003319,4.564185,-9.772475,-3.086673,-0.757655,6.683805,-5.044096,-6.838975,-0.598176,0.041695,-6.153223,6.315223,9.396186,6.892771,3.108257,7.527713,-8.252991,0.012909,6.864528,-5.664714,-4.533868,6.513166,-3.195801,6.016852,-8.319814,6.159119,8.690696,-3.100431,-1.171776,4.976545,7.410183,-8.389196,9.819082,-5.516713,9.684985,4.925387,9.727950,5.248629,-8.260837,-1.096125,7.476512,1.854446,-8.933514,-5.572594,-0.950531,-9.651040,-5.633757,7.608824,-6.260157,-8.397018,-4.061691,-4.662741,-2.195084,-4.320733,-8.310490,-7.871824,-1.094616,-7.235046,7.282076,2.721914,4.052794,5.990477,-2.998274,7.861946,-3.938876,4.801490,2.033984,-7.389804,7.732309,3.743063,-5.145462,5.095718,6.539244,8.618123,-0.976172,-7.371095,0.523087,-1.068881,8.280729,-0.889251,5.473508,-0.988267,7.714886,0.711030,1.090151,9.905726,-3.938230,-2.851202,-7.087174,-0.387681,-7.949691,-3.377875,-2.214728,-3.285583,0.865979,6.223208,-3.371827,4.289598,0.464113,-8.691255,0.093738,-9.414581,-9.770645,-8.941324,-2.604088,-2.221266,6.678712,-9.384135,1.488040,4.614966,-5.190423,1.110944,7.933650,-7.297304,8.311603,2.419972,-2.351289,-6.771530,0.876803,-0.624667,6.427751,-0.246092,9.542033,-9.056671,8.475505,2.551594,2.378771,-0.944048,-4.876714,9.615282,6.005305,-0.224594,-4.577310,9.430475,3.381881,2.088049,-9.046868,-2.966726,8.754808,-0.271224,-6.036931,-8.003844,-6.606693,-1.236057,8.531150,2.062846,7.811435,8.157170,-9.488084,7.688209,-1.510368,4.869112,-1.415070,-8.911794,-9.356412,1.230846,3.294180,-6.208857,-5.649353,-4.384395,-6.196506,0.557519,5.512221,0.434924,4.928381,-7.531733,-0.457977,-1.541774,6.229121,-0.470377,7.129602,-1.709670,6.546938,-1.053015,-9.163259,6.812606,-5.164350,-3.841347,1.039304,-4.126082,-1.696402,-8.767932,-2.440132,7.115774,-9.215910,7.810054,5.739123,-3.617471,2.734143,7.329261,6.190811,-6.305003,6.597922,0.181713,5.341242,5.791463,-3.942992,-4.751299,-6.602914,-1.836725,6.033158,-1.513216,-6.268841,4.744158,6.853403,9.362568,8.346154,7.683922,-3.712401,-0.317541,-3.635082,2.887842,2.566286,4.413446,1.054510,-0.491641,5.787684,-5.764905,7.436531,9.719336,-0.953633,7.412268,6.113899,-2.670666,-5.981232,7.175983,-4.625657,4.323629,-0.197197,4.635961,4.627845,-4.936781,-7.244339,-2.611001,-8.530167,-5.942127,-7.030780,-2.503584,-1.224602,4.889916,9.271280,3.264719,2.203381,-8.082442,2.338996,7.729302,2.194117,-7.007491,-3.200994,-5.615023,-4.315293,0.328957,-6.489826,-6.614725,-7.470075,2.186639,-8.055539,1.724374,-9.137344], dtype = "float32")#candidate|9248|(1040,)|const|float32
const_9249 = relay.const([-5.112238,-9.812520,-4.438871,2.240352,2.946389,-7.704451,-6.506920,8.355169,9.084018,-3.368045,1.268489,-3.101558,-7.074872,-8.127537,-4.189990,-1.151164,1.172972,1.596611,-5.658989,-2.565839,2.042218,-4.197578,8.405765,-8.062538,-9.266044,-7.116498,-4.413022,-5.831681,6.626801,-0.794858,1.712829,-8.683894,-0.134078,-2.505904,-1.348480,-9.820792,0.627503,1.573423,-7.917757,-1.236591,-4.725434,6.145283,9.129391,9.894438,-8.586058,-1.125186,-2.670539,-7.124304,8.885149,7.880732,7.791586,0.735079,4.620668,-9.002592,-6.430191,-3.042714,7.289760,8.709032,0.152439,4.472084,5.409232,8.932144,-9.272495,-3.899830,5.278976,9.467437,7.015253,2.054027,4.396570,8.699047,-7.603452,-9.727108,5.695509,-6.664049,-7.349737,-5.895401,-7.192922,3.439898,-0.709910,-9.209116,-7.559443,-4.121043,-6.047452,-5.615744,9.455740,0.299832,9.557958,9.501584,-6.118717,2.028816,9.774901,-6.518676,-3.198127,-9.488394,0.095402,-9.529506,-6.180362,2.485759,-4.481550,-5.818299,9.839107,-7.626665,5.600771,7.172107,2.346159,-6.344281,3.291671,-8.826652,1.495915,-6.834902,3.335507,-1.776072,4.122339,-3.375623,3.269427,-8.866536,3.192957,1.377004,-2.630971,-3.505709,3.352327,5.208167,2.416007,-6.562069,-3.164434,3.501257,7.191775,-3.376828,6.513759,0.647541,9.409214,-3.561312,-3.072925,-5.803043,-8.974825,-0.359271,0.134074,-9.587596,-2.618315,5.001367,9.358137,-0.431661,-7.503954,-8.929546,-9.602104,-8.485536,0.447399,-1.555767,-4.545599,-1.562271,3.702350,5.708833,-7.005080,2.985647,-1.021342,-9.079212,0.223651,8.333870,3.064627,6.346460,2.490994,6.751447,-1.399932,-4.861381,-9.208912,-6.928695,3.542490,1.167958,5.795649,-3.631062,3.509681,-4.819570,-2.160876,1.576100,5.594626,8.572881,-0.123088,8.115860,-2.668628,-3.596714,-5.041119,-2.947036,-4.980463,-5.206537,-5.208603,0.641794,9.822091,-8.063021,2.968439,9.954676,-3.695400,0.948400,9.672589,-7.514122,-0.855654,9.067511,6.609719,3.486011,6.963821,3.231038,-3.079922,5.940932,-5.679228,5.659358,6.165526,-2.522958,7.561722,4.220146,-4.600874,-9.486913,-8.844223,-7.905890,3.169054,5.449594,4.139811,-9.415322,4.394160,6.582522,1.265683,-7.641932,9.594171,9.924574,-9.165474,6.039600,-9.013039,-7.878102,2.468685,-8.871290,-9.069543,5.971045,-0.059639,8.740011,-1.382749,-8.602858,-5.368755,-3.632723,8.691761,-6.729476,-0.529265,5.385882,-8.583830,2.292481,-5.368374,-4.789427,2.204379,-8.969439,-7.157262,-0.255501,-2.490008,-0.257399,1.353268,-9.903772,-3.623076,-8.582992,-6.646258,9.554868,3.686197,5.094642,-7.236014,-9.150743,7.883853,-6.971105,8.620322,-7.087546,6.905642,-6.315597,-6.789640,2.509310,7.256630,1.615007,8.191133,-6.377741,-4.454795,-1.050163,-3.192373,-0.754086,7.809185,4.125827,8.246142,-8.495091,-6.072873,4.948727,2.640770,-3.062577,7.340218,7.616708], dtype = "float32")#candidate|9249|(286,)|const|float32
var_9250 = relay.var("var_9250", dtype = "bool", shape = ())#candidate|9250|()|var|bool
const_9251 = relay.const([True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False], dtype = "bool")#candidate|9251|(1404,)|const|bool
call_9247 = relay.TupleGetItem(func_8014_call(relay.reshape(const_9248.astype('float32'), [1040,]), relay.reshape(const_9249.astype('float32'), [286,]), relay.reshape(var_9250.astype('bool'), []), relay.reshape(const_9251.astype('bool'), [1404,]), ), 2)
call_9252 = relay.TupleGetItem(func_8019_call(relay.reshape(const_9248.astype('float32'), [1040,]), relay.reshape(const_9249.astype('float32'), [286,]), relay.reshape(var_9250.astype('bool'), []), relay.reshape(const_9251.astype('bool'), [1404,]), ), 2)
uop_9260 = relay.log2(const_9248.astype('float32')) # shape=(1040,)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_9266 = relay.TupleGetItem(func_4699_call(), 0)
call_9267 = relay.TupleGetItem(func_4701_call(), 0)
func_8450_call = mod.get_global_var('func_8450')
func_8451_call = mutated_mod.get_global_var('func_8451')
call_9276 = relay.TupleGetItem(func_8450_call(), 0)
call_9277 = relay.TupleGetItem(func_8451_call(), 0)
func_8536_call = mod.get_global_var('func_8536')
func_8538_call = mutated_mod.get_global_var('func_8538')
call_9288 = relay.TupleGetItem(func_8536_call(), 0)
call_9289 = relay.TupleGetItem(func_8538_call(), 0)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_9301 = relay.TupleGetItem(func_4699_call(), 0)
call_9302 = relay.TupleGetItem(func_4701_call(), 0)
func_4186_call = mod.get_global_var('func_4186')
func_4188_call = mutated_mod.get_global_var('func_4188')
call_9304 = relay.TupleGetItem(func_4186_call(), 0)
call_9305 = relay.TupleGetItem(func_4188_call(), 0)
output = relay.Tuple([call_9234,call_9239,const_9240,var_9241,call_9247,const_9249,var_9250,const_9251,uop_9260,call_9266,call_9276,call_9288,call_9301,call_9304,])
output2 = relay.Tuple([call_9235,call_9242,const_9240,var_9241,call_9252,const_9249,var_9250,const_9251,uop_9260,call_9267,call_9277,call_9289,call_9302,call_9305,])
func_9335 = relay.Function([var_9241,var_9250,], output)
mod['func_9335'] = func_9335
mod = relay.transform.InferType()(mod)
var_9336 = relay.var("var_9336", dtype = "float64", shape = (1, 845))#candidate|9336|(1, 845)|var|float64
var_9337 = relay.var("var_9337", dtype = "bool", shape = ())#candidate|9337|()|var|bool
output = func_9335(var_9336,var_9337,)
func_9338 = relay.Function([var_9336,var_9337,], output)
mutated_mod['func_9338'] = func_9338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7089_call = mod.get_global_var('func_7089')
func_7090_call = mutated_mod.get_global_var('func_7090')
call_9362 = func_7089_call()
call_9363 = func_7089_call()
func_5807_call = mod.get_global_var('func_5807')
func_5808_call = mutated_mod.get_global_var('func_5808')
call_9377 = func_5807_call()
call_9378 = func_5807_call()
func_2696_call = mod.get_global_var('func_2696')
func_2699_call = mutated_mod.get_global_var('func_2699')
var_9425 = relay.var("var_9425", dtype = "bool", shape = (1404,))#candidate|9425|(1404,)|var|bool
var_9426 = relay.var("var_9426", dtype = "float32", shape = (1152,))#candidate|9426|(1152,)|var|float32
call_9424 = relay.TupleGetItem(func_2696_call(relay.reshape(var_9425.astype('bool'), [1404,]), relay.reshape(var_9426.astype('float32'), [1152,]), ), 2)
call_9427 = relay.TupleGetItem(func_2699_call(relay.reshape(var_9425.astype('bool'), [1404,]), relay.reshape(var_9426.astype('float32'), [1152,]), ), 2)
output = relay.Tuple([call_9362,call_9377,call_9424,var_9425,var_9426,])
output2 = relay.Tuple([call_9363,call_9378,call_9427,var_9425,var_9426,])
func_9432 = relay.Function([var_9425,var_9426,], output)
mod['func_9432'] = func_9432
mod = relay.transform.InferType()(mod)
var_9433 = relay.var("var_9433", dtype = "bool", shape = (1404,))#candidate|9433|(1404,)|var|bool
var_9434 = relay.var("var_9434", dtype = "float32", shape = (1152,))#candidate|9434|(1152,)|var|float32
output = func_9432(var_9433,var_9434,)
func_9435 = relay.Function([var_9433,var_9434,], output)
mutated_mod['func_9435'] = func_9435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8556_call = mod.get_global_var('func_8556')
func_8558_call = mutated_mod.get_global_var('func_8558')
call_9451 = func_8556_call()
call_9452 = func_8556_call()
output = relay.Tuple([call_9451,])
output2 = relay.Tuple([call_9452,])
func_9473 = relay.Function([], output)
mod['func_9473'] = func_9473
mod = relay.transform.InferType()(mod)
mutated_mod['func_9473'] = func_9473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9473_call = mutated_mod.get_global_var('func_9473')
call_9474 = func_9473_call()
output = call_9474
func_9475 = relay.Function([], output)
mutated_mod['func_9475'] = func_9475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6945_call = mod.get_global_var('func_6945')
func_6946_call = mutated_mod.get_global_var('func_6946')
call_9494 = func_6945_call()
call_9495 = func_6945_call()
output = relay.Tuple([call_9494,])
output2 = relay.Tuple([call_9495,])
func_9506 = relay.Function([], output)
mod['func_9506'] = func_9506
mod = relay.transform.InferType()(mod)
mutated_mod['func_9506'] = func_9506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9506_call = mutated_mod.get_global_var('func_9506')
call_9507 = func_9506_call()
output = call_9507
func_9508 = relay.Function([], output)
mutated_mod['func_9508'] = func_9508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_9512 = func_7077_call()
call_9513 = func_7077_call()
output = call_9512
output2 = call_9513
func_9527 = relay.Function([], output)
mod['func_9527'] = func_9527
mod = relay.transform.InferType()(mod)
mutated_mod['func_9527'] = func_9527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9527_call = mutated_mod.get_global_var('func_9527')
call_9528 = func_9527_call()
output = call_9528
func_9529 = relay.Function([], output)
mutated_mod['func_9529'] = func_9529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9473_call = mod.get_global_var('func_9473')
func_9475_call = mutated_mod.get_global_var('func_9475')
call_9559 = relay.TupleGetItem(func_9473_call(), 0)
call_9560 = relay.TupleGetItem(func_9475_call(), 0)
output = call_9559
output2 = call_9560
func_9562 = relay.Function([], output)
mod['func_9562'] = func_9562
mod = relay.transform.InferType()(mod)
mutated_mod['func_9562'] = func_9562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9562_call = mutated_mod.get_global_var('func_9562')
call_9563 = func_9562_call()
output = call_9563
func_9564 = relay.Function([], output)
mutated_mod['func_9564'] = func_9564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9230_call = mod.get_global_var('func_9230')
func_9231_call = mutated_mod.get_global_var('func_9231')
call_9605 = func_9230_call()
call_9606 = func_9230_call()
func_8339_call = mod.get_global_var('func_8339')
func_8341_call = mutated_mod.get_global_var('func_8341')
call_9624 = relay.TupleGetItem(func_8339_call(), 1)
call_9625 = relay.TupleGetItem(func_8341_call(), 1)
output = relay.Tuple([call_9605,call_9624,])
output2 = relay.Tuple([call_9606,call_9625,])
func_9643 = relay.Function([], output)
mod['func_9643'] = func_9643
mod = relay.transform.InferType()(mod)
mutated_mod['func_9643'] = func_9643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9643_call = mutated_mod.get_global_var('func_9643')
call_9644 = func_9643_call()
output = call_9644
func_9645 = relay.Function([], output)
mutated_mod['func_9645'] = func_9645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_9688 = relay.TupleGetItem(func_2625_call(), 1)
call_9689 = relay.TupleGetItem(func_2626_call(), 1)
output = relay.Tuple([call_9688,])
output2 = relay.Tuple([call_9689,])
func_9692 = relay.Function([], output)
mod['func_9692'] = func_9692
mod = relay.transform.InferType()(mod)
output = func_9692()
func_9693 = relay.Function([], output)
mutated_mod['func_9693'] = func_9693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7416_call = mod.get_global_var('func_7416')
func_7417_call = mutated_mod.get_global_var('func_7417')
call_9700 = relay.TupleGetItem(func_7416_call(), 1)
call_9701 = relay.TupleGetItem(func_7417_call(), 1)
func_5298_call = mod.get_global_var('func_5298')
func_5300_call = mutated_mod.get_global_var('func_5300')
call_9711 = relay.TupleGetItem(func_5298_call(), 1)
call_9712 = relay.TupleGetItem(func_5300_call(), 1)
func_4359_call = mod.get_global_var('func_4359')
func_4361_call = mutated_mod.get_global_var('func_4361')
const_9722 = relay.const([5.932182,1.664508,9.409448,-2.784322,8.940803,-8.017578,-6.493995,2.979472,-3.126608,9.131730,-5.853299,-1.587147,-0.250076,7.803803,-1.625600,-2.922601,-2.099754,-0.978337,-7.974347,-5.634891,9.131946,-1.669751,5.441985,5.086027,-9.851471,-0.518842,-6.224312,-9.776397,5.904253,-8.771972,-4.962933,0.227898,-9.280496,-2.881256,4.359873,-9.369646,3.376237,-6.493641,-2.491950,-0.267923,-0.531165,4.201330,1.897196,-1.060904,5.414791,3.006461,7.744008,-1.078224,-5.256396,-4.909176,9.732443,4.285992,-2.095104,4.915387,9.972764,0.050181,8.182724,-8.896879,-8.059102,2.226650,6.605887,3.669606,5.836821,-1.670182,-6.294784,7.044789,6.505939,-0.273334,-9.457959,-2.833835,-9.320744,-5.488263,-4.862689,-0.144254,2.648828,-5.832729,-7.349344,6.629738,-2.830091,-8.237022,-2.962779,-1.691034,-4.330870,8.963390,9.857282,-7.562446,9.523504,7.626550,-3.249832,-0.943237,9.976117,-4.187519,-2.914779,3.136406,-9.357679,8.986275,-5.668701,-8.444134,2.652105,7.161452,-0.211410,-0.428503,-1.244539,3.641615,3.032006,-1.153332,7.507238,5.220283,-5.330483,-8.358465,-0.793724,-2.018689,3.002860,4.265017,-7.603154,5.974075,-1.025727,5.821146,3.449379,0.163477,-4.377616,8.624233,9.234814,-6.268039,-0.944028,-5.875384,-0.940063,1.774534,9.416607,-6.758285,6.293937,-4.948193,9.736805,7.442370,4.531717,-4.176813,-8.845955,6.675633,-1.704264,-4.062265,-8.612122,3.712053,4.503393,-7.673336,4.495514,-7.335914,9.067395,-5.045298,-8.842565,8.732336,4.690152,-6.635760,-5.751378,7.136980,1.411600,0.567736,-9.611516,-8.364615,2.742395,-4.188695,-8.944997,3.511736,-7.731262,-3.880579,0.216318,-3.378141,2.869184,3.037228,-2.954969,-1.374543,-5.761881,7.542462,-2.677942,-8.044446,-8.734500,-8.814205,6.542852,-9.162073,-1.250744,9.992389,8.142471,-2.490138,-2.175762,-8.963529,-9.292002,-8.343801,-4.727792,9.983545,3.339923,-8.110620,-7.988589,-3.643312,-2.493639,3.936689,-1.004255,8.529473,-7.343572,-4.016159,4.759537,9.615724,-5.270065,-4.034769,9.541233,3.559328,5.165378,7.760217,4.187246,2.451392,-1.395305,-5.356327,7.243713,-7.485002,6.522300,-7.558428,9.251703,-1.396073,8.942189,-8.722600,-4.332433,-7.468748,3.834185,6.410626,8.033415,4.380980,-1.172401,-4.573438,6.028167,7.181407,-1.427716,8.950683,-4.223580,2.612023,-4.934622,-8.646778,7.340742,-3.205896,-9.470823,6.697025,-0.544613,-8.890504,-1.389330,2.262093,6.279942,-8.646174,-1.972374,-2.488013,8.321225,3.186909,9.550451,-9.198881,-1.315025,-4.669715,8.202546,-3.306880,-4.112747,-7.262979,-8.940435,-9.520285,-8.328289,3.536795,-5.821037,3.590409,1.825397,8.911895,6.417467,6.465423,-7.199406,-2.879463,-7.928435,8.836906,8.849094,5.242830,2.108198,-9.444539,2.064404,9.607188,6.901153,3.177321,1.910969,3.120231,0.741050,-1.071352,-2.949608,9.133391,4.001429,0.061878,-3.923439,-6.768614,-4.591941,9.675134,-3.490801,3.297967,-6.433277,-1.615887,3.355799,-9.920728,2.374267,-2.630206,8.135077,-0.406568,8.643177,-0.386368,-6.598875,1.032154,5.086664,-2.417417,6.465744,8.488286,4.379606,0.229567,9.903267,6.978610,-3.850250,4.596338,9.379104,6.968901,6.199649,-7.449198,-5.592989,6.748613,-1.471330,-0.158886,5.789261,7.213910,2.583968,-8.259193,-3.892322,6.607755,0.590336,7.436238,-7.460586,7.417672,-3.342981,-5.365970,-8.042949,-8.757125,3.279979,-8.406862,-9.106407,7.815832,8.869346,-4.756790,2.117210,-6.534114,-0.408307,9.489028,-5.258238,0.267781,-0.986674,-7.193932,9.234303,-7.644824,8.210380,4.773241,-3.592139,0.721098,-3.099564,-9.555517,-7.046357,0.004215,-1.238276,3.086443,0.235106,2.657534,-2.211003,-0.359543,-8.609778,6.375036,-8.810297,9.885114,4.256477,-3.444615,-1.805282,-1.566549,6.292494,-1.820540,-3.210872,5.895369,-0.838867,-6.556458,-4.526536,-9.242240,1.864545,-9.913685,-8.708400,-6.196114,-0.496278,-0.001895,6.884591,3.182627,-6.101320,-1.189932,-4.088755,-2.348952,-2.115149,5.988191,-2.612593,7.464611,0.057068,6.470679,7.073563,-4.695987,-7.111229,8.918780,2.622856,-9.085024,-9.903223,-3.344342,-6.014489,2.440035,7.140782,4.739304,-5.480479,5.579876,-2.025888,0.928322,2.659665,-2.969174,-9.651092,3.690479,-8.177284,1.898569,5.417265,8.019718,3.371162,-3.610236,-2.088594,-5.265621,5.517536,-9.384427,-1.339749,0.250600,5.920689,5.478499,3.500424,8.981493,-5.531318,-2.284205,4.546492,-9.750106,-2.434580,0.284448,-2.202733,2.895198,-1.161391,-0.708426,-0.251309,-6.830922,0.609531,9.596320,-4.776662,-5.133444,-3.060155,-4.192679,7.460111,-2.886061,-6.643974,-7.428089,7.629241,-7.130284,0.800142,-4.012754,-1.665640,-6.879003,-9.043799,1.744927,-7.604276,7.667667,-9.668920,-3.954866,-5.605792,-0.926112,8.823001,-5.185773,-9.760638,-2.772502,5.724156,0.011520,0.925216,8.067103,-6.178016,-9.268931,-7.308869,1.579671,-8.459011,-6.139531,-0.227819,7.379999,8.431939,-2.508723,-2.027398,-3.903809,4.923659,9.408511,6.215331,-4.136800,0.057038,-2.706036,-7.649868,8.124474,-6.196099,-8.983803,-5.112653,-7.402734,8.014568,3.263939,8.515912,6.911693,-3.178739,8.610175,0.270074,2.041900,-5.324111,-8.387663,2.002383,9.952391,-1.513606,-4.567685,7.709483,-8.065519,4.873625,-9.841896,5.475615,3.231009,6.799610,0.182861,-4.800979,2.849953,8.496162,3.855331,3.771193,-8.558901,-0.632299,-7.596772,2.054963,-6.715290,9.308177,4.666989,-3.424175,-9.551218,3.470640,-2.255576,-1.500637,-2.820221,-7.429223,-8.231286,0.590079,7.360834,7.045091,7.838889,-0.223222,2.216149,0.305713,6.467161,5.088244,9.090373,4.974134,-0.509687,6.900899,6.148633,-7.052170,-0.359050,-7.128453,-4.792051,0.894528,-7.099512,1.173557,9.471414,-4.279313,6.160859,-2.067927,-1.100033,-8.542117,7.872121,-3.651562,7.322010,-1.126768,-6.104201,8.661130,-5.021147,-6.768988,2.496462,-5.483683,-0.357842,4.827384,-7.567589,-6.896799,2.422913,9.190348,6.472156,-5.043366,5.269915,-2.723647,5.268938,-7.930703,-8.687162,6.052693,-0.953018,6.139490,-8.009315,-6.750044,-8.040514,-0.640369,-0.599693,5.238745,6.551117,-6.844789,-1.420466,-2.024807,0.644161,-2.633729,9.116219,6.715558,2.491606,3.981211,8.895703,4.833750,-9.634952,2.088827,9.681841,-3.260896,-0.038409,8.641628,5.368882,3.837239,-0.905989,2.456848,6.628194,-5.292544,6.024139,-4.471896,0.009761,-2.352558,3.150374,-0.846575,-7.390571,4.628272,-8.183654,-4.097168,-7.864928,-6.390161,1.248992,8.512136,-3.967325,9.828836,4.222823,-5.523149,4.085075,-6.189791,-4.418725,-8.915243,-5.176731,-0.799475,-8.189935,-0.772715,-4.419415,-8.020703,-7.325598,-6.581976,6.081714,-2.209817,6.942020,2.044477,-9.643450,-0.847995,1.377068,5.182102,-0.221697,-9.620510,-3.663361,-4.488777,8.378733,-7.098077,-5.266375,-9.206354,9.634532,-2.251616,5.914562,0.456304,2.931741,-2.023553,-1.356117,-6.884303,3.645785,-7.783688,-1.187328,-8.978420,5.547882,6.567442,3.339761,2.551200,5.916201,-9.862451,3.960020,-2.639446,4.581469,5.336910,-9.129095,-9.570928,-4.027844,-4.188238,0.902022,-2.723147,0.087466,-7.748682,6.476749,2.646650,0.528432,9.111793,-2.790067,-3.143104,5.893938,7.507609,9.144307,3.752459,-1.207243,-6.205330,2.099592,-7.912612,2.235507,3.535239,-7.376633,0.427869,-9.586494,9.925677,-0.190362,-4.043454,2.073046,6.088022,-3.907326,4.120232,-5.246962,-0.064609,-0.455458,7.442426,-5.773652,8.419982,2.697129,-9.357956,7.636625,-0.661171,2.983482,9.647080,6.096902,-8.085388,-3.953787,-9.403127,2.284828,-1.763683,-3.950114,7.456238,-4.709623,2.857202,0.032969,-2.317805,8.302485,-8.764762,3.237010,-4.972099,9.982086,-0.653612,-0.762909,-8.231887,-1.760627,7.512332,-7.315670,9.695009,2.265100,7.768857,-2.744121,-7.941168,-1.787356,4.794835,-3.514361,-0.731566,-0.888503,5.962422,-6.045421,-2.429156,-7.402981,1.015815,4.017358,-6.205391,5.692004,1.927848,9.186705,-7.061217,0.097322,2.177686,1.603068,8.789017,6.255642,-5.389354,-3.989193,-3.423756,-4.050893,-8.515015,-7.153833,7.682401,-8.960351,0.390278,-4.794911,1.390322,3.229557,3.880816,2.387375,-4.801852,-9.437013,-7.474581,-0.988684,1.260079,-5.947237,-1.791473,-4.001231,-8.087250,-1.011302,-4.269545,0.609204,-9.454101,6.598263,2.538082,-8.891553,2.993956,-3.401368,-1.530932,-3.590434,-3.999479,0.930737,7.400579,-1.198400,-4.902319,9.650534,3.420829,-2.010012,-1.800622,8.426965,-7.098210,3.999480,-9.911411,6.264041,-3.750898,2.618528,-0.474304,8.850419,-4.358872], dtype = "float64")#candidate|9722|(845,)|const|float64
call_9721 = relay.TupleGetItem(func_4359_call(relay.reshape(const_9722.astype('float64'), [845,])), 0)
call_9723 = relay.TupleGetItem(func_4361_call(relay.reshape(const_9722.astype('float64'), [845,])), 0)
func_6511_call = mod.get_global_var('func_6511')
func_6513_call = mutated_mod.get_global_var('func_6513')
call_9726 = relay.TupleGetItem(func_6511_call(), 0)
call_9727 = relay.TupleGetItem(func_6513_call(), 0)
output = relay.Tuple([call_9700,call_9711,call_9721,const_9722,call_9726,])
output2 = relay.Tuple([call_9701,call_9712,call_9723,const_9722,call_9727,])
func_9732 = relay.Function([], output)
mod['func_9732'] = func_9732
mod = relay.transform.InferType()(mod)
output = func_9732()
func_9733 = relay.Function([], output)
mutated_mod['func_9733'] = func_9733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_9759 = relay.TupleGetItem(func_4699_call(), 2)
call_9760 = relay.TupleGetItem(func_4701_call(), 2)
func_8450_call = mod.get_global_var('func_8450')
func_8451_call = mutated_mod.get_global_var('func_8451')
call_9769 = relay.TupleGetItem(func_8450_call(), 0)
call_9770 = relay.TupleGetItem(func_8451_call(), 0)
func_3258_call = mod.get_global_var('func_3258')
func_3261_call = mutated_mod.get_global_var('func_3261')
const_9780 = relay.const([[0.118726,4.126055,-9.750313,9.702933],[7.197982,-6.875982,-0.321218,-0.959951],[2.972555,-2.725332,-0.700054,4.451207],[-9.997515,-3.424354,0.207596,1.013295],[-5.029823,6.033114,-8.047928,1.964893],[7.050605,-0.491610,3.833726,-7.327641],[2.754152,-9.287016,-1.546582,-8.772394],[-8.698587,2.097238,-3.492240,-4.034315],[9.840904,0.137652,-1.608147,9.664947],[-2.308341,5.819380,-8.472570,-6.528834],[4.739733,3.009731,3.225775,-9.515338],[5.703149,0.510191,-3.883577,-2.113824],[3.340550,9.301658,4.326272,-5.988593],[-5.895895,2.335345,2.311132,6.521903],[-7.708977,-7.308231,-2.549569,0.163313],[6.289755,2.238799,-1.874878,2.906959],[1.753078,-1.110836,-5.754364,-2.380030],[-9.561698,9.899509,-5.224282,-7.185921],[-4.509478,-2.685835,8.393631,-5.577000],[-0.354207,5.976571,1.030799,-6.147260],[7.813557,6.414219,6.741339,1.535552],[-3.948667,-1.489577,4.605325,4.662214],[5.645029,-1.456646,-1.792169,3.082718],[5.167247,9.969434,-0.362280,7.769718],[-8.825955,2.315550,7.043133,-3.171769],[1.514296,-0.436117,2.790823,-1.922142],[9.484422,-1.336313,9.259913,-3.186660],[-9.415164,-5.845098,9.083005,-8.849327],[-5.630762,-4.033571,-4.694320,2.326359],[2.270599,-8.495021,-5.853077,3.272665],[-4.491439,9.316666,-1.820195,-9.310883],[4.523136,0.420512,-9.264955,0.436219],[9.960078,-4.266179,-1.091729,7.670047],[8.416905,-1.009122,3.505394,7.505379],[6.982079,8.550433,-5.895068,-8.794739],[-1.961602,6.817099,-8.888209,-0.751138],[-4.554560,5.648034,-7.859075,-9.348638],[7.668185,0.409413,-6.869402,-1.927694],[3.113092,4.532059,9.320895,-1.259184],[0.701945,-4.009620,-6.503034,7.436114],[-7.779491,2.900126,-8.374275,-9.338456],[-4.776687,-5.734924,6.364357,7.018436],[-0.126412,-9.090036,-3.504761,-2.949574],[-2.803130,1.841461,2.003767,3.758009],[-2.309962,-7.022671,-7.916131,-1.362375],[0.488428,-4.122767,4.691960,8.175177],[-6.329386,9.066545,-9.042177,5.785790],[-9.145299,8.676664,7.738431,0.283915],[5.894002,-0.894095,2.888268,3.750646],[5.248095,9.020449,3.161755,6.411217],[-7.929417,-4.793572,-7.584442,-9.757166],[3.915665,-4.126657,-7.722038,-6.256302],[8.457470,-0.502953,5.601649,9.103414],[5.374569,3.951607,-0.312371,-1.839246],[8.855000,3.171635,-2.093914,-5.259697],[-7.162799,8.975426,8.306572,-9.210377],[-9.833335,0.143867,-7.144153,6.157759],[9.540443,-9.574047,6.536923,-3.942051],[-2.768775,-7.147612,6.416936,-2.947371],[7.270810,7.098409,3.675025,9.940428],[-1.830687,9.055512,-3.234015,-5.471654],[1.278287,5.939183,7.909013,5.115360],[5.115969,2.323230,-6.856896,-0.281638],[8.634916,-4.096032,-3.183701,-8.219758],[-6.887768,5.328668,-5.926314,-4.565387],[1.136800,-1.398712,-5.043609,-5.517335],[6.271920,-7.128091,9.796621,2.784526],[-9.146200,9.514653,-6.438185,5.076589],[6.770465,0.453942,-1.610885,2.748292],[2.737723,3.037785,3.701802,1.611488],[1.734468,-3.846841,3.506229,3.949530],[-2.754279,-2.068398,-7.726919,3.385729],[-8.713197,-8.338225,4.271388,-6.230665],[1.777730,-6.499015,8.164643,-7.641556],[9.961705,6.219054,-7.854923,2.311327],[4.732040,5.259202,0.799263,6.639639],[1.311376,6.310695,7.468829,4.908961],[3.292537,2.286177,-9.369009,4.553571],[8.318183,-3.710634,4.342361,-4.545537],[8.142558,-6.059724,-2.659073,-0.301636],[4.244824,-9.279665,-9.043268,-1.320518],[4.795794,-3.498645,4.450315,-5.322303],[8.207580,-4.591890,-3.789112,3.038667],[2.344005,-0.498161,-5.186638,7.011969],[-0.424488,-3.371515,-0.276919,-1.147493],[0.626040,0.063093,-2.179092,9.922049],[-3.032781,-1.260705,-7.743919,-5.862470],[-6.712194,3.874016,5.562690,-3.331862],[2.219550,-2.169448,2.495275,0.441268],[-0.578436,4.803860,-1.931096,-0.870953],[2.094280,2.714193,-4.219051,3.129534],[7.638686,8.943944,9.403536,-3.483947],[8.169772,-8.090469,-0.064072,4.906774],[-1.833049,5.850111,2.866717,2.518288],[4.854029,-6.158971,-5.623512,-9.766821],[-9.324866,1.801466,6.922535,-8.191401],[-3.405293,-5.571091,4.906608,9.231681],[-9.991334,-1.120422,-7.182577,-0.062452],[9.195277,-8.111626,-7.518777,8.169442],[-6.767922,3.211405,-7.442332,-4.289473],[-5.668880,0.781086,-7.623215,-1.025423],[-4.155432,-2.808648,-5.567706,-0.521347],[5.654142,-9.325144,2.269267,8.638258],[-5.929657,8.009066,-8.655245,1.574402],[-5.254489,-4.161922,-2.011657,-0.465149],[-7.395688,0.050702,0.386410,-0.348186],[-7.804816,7.040219,-9.365437,-4.009445],[4.540035,3.741423,3.105425,-3.847455],[-9.489838,3.459342,1.500694,8.449227],[-1.969876,4.629607,-7.228358,4.947666],[-6.682225,-5.051398,9.961308,7.875215],[-5.988496,-3.677339,5.598872,-0.262161],[-5.074572,-5.249876,4.861704,5.166777],[6.533237,2.377711,-2.829151,-2.555662],[2.233751,2.187638,6.540028,9.142820],[4.555538,-7.385946,1.543926,-4.848484],[-4.412037,5.267898,-9.525322,2.840739],[8.543650,3.075567,7.525592,-7.838359],[-2.743155,6.691445,-0.313181,-0.543159],[9.241775,6.205302,1.747213,-7.987191],[-1.513852,6.715327,-6.998589,-4.506011],[8.488764,8.805150,-2.190963,-8.408103],[3.854100,-2.899771,-7.093430,8.371317],[5.793269,-4.317791,8.496566,-8.741952],[3.309362,-7.596278,1.276987,0.624762],[5.761081,3.474163,7.081810,-9.465720],[-8.711020,-7.739736,2.456604,-2.527953],[-7.710945,7.182580,2.796005,-0.799113],[4.810950,-3.675771,9.867474,-9.124158],[-4.253087,-1.572360,9.932681,-8.609760],[-2.944391,-0.747732,-6.137253,-7.868267],[-5.687962,-7.835931,-4.609200,-9.203246],[-0.758653,-1.427663,-7.077353,-9.026099],[-0.039261,-7.516380,2.309211,4.994091],[-9.881037,-4.801582,-5.152585,5.389781],[-8.649658,-8.872146,-9.654013,3.553527],[0.471153,5.870456,-5.126380,-3.860875],[-3.003715,-8.746809,6.389208,0.558978],[0.317738,7.682865,7.585543,-1.933173],[-0.105569,-0.229660,8.384506,8.365967],[0.564054,7.522371,-3.492647,-0.955058],[-5.570447,5.092573,8.725617,4.401574],[-0.820793,-8.199707,-1.732226,3.284086],[-8.674943,2.639441,8.883801,-4.441338],[0.636411,-5.962091,-5.303886,5.844172],[0.319227,-9.743011,0.819886,-2.415008],[-8.597474,6.470162,1.133009,-8.276736],[-6.608848,-1.455637,-7.895323,-9.883153],[-6.413825,-8.883035,-5.276065,0.859413],[-3.315242,-9.168791,-7.884023,2.315091],[9.628811,6.376257,5.021709,-1.642771],[0.517068,-1.783106,-8.107409,-1.795707],[4.988271,0.498924,-2.627778,-4.886795],[-6.496462,-6.910927,9.878073,-4.610553],[7.168280,6.327543,8.262345,-4.337388],[-8.394959,-5.789282,-7.648438,5.778106],[4.621799,4.366598,-9.940352,-0.087640],[-0.627614,5.545249,-9.125028,-5.781471],[6.445510,2.599632,-5.206024,4.878821],[-0.521544,8.801034,-7.495336,-0.143454],[7.256655,6.467794,9.222380,-2.285194],[6.937413,9.757733,0.540232,4.927573],[-4.456068,3.271481,-7.100311,6.188778],[1.101833,6.008913,-0.515464,0.067475],[9.624772,9.051420,7.107137,-5.282162],[0.207935,-6.236406,-0.801810,3.049222],[-8.373079,2.618125,7.732593,9.637469],[7.516934,4.802176,5.153058,6.008998],[9.758801,7.692318,-7.399795,1.321145],[-7.009873,7.901863,8.365725,3.268385],[8.876273,8.267738,0.309623,4.465304],[5.082890,-2.366234,-5.968885,-0.787761],[-3.350130,-8.670274,1.728984,-2.903927],[4.646353,-6.077576,-7.772554,1.585558],[-0.276814,0.480038,1.411182,-1.410064],[0.833232,2.109135,-0.589553,7.850033],[-4.593179,-6.859703,-5.369415,3.998838],[-6.460091,-9.059830,6.205503,-3.022211],[-1.960476,4.078748,8.154153,4.220076],[9.958421,-4.298208,-6.003200,-2.956463],[1.226852,-0.737982,-8.409776,8.782626],[-3.196089,9.877334,2.871066,6.530931],[1.693656,-2.983433,2.486307,0.753801],[-6.688818,-6.654479,-6.306997,8.629623],[2.264391,5.124651,9.887494,-2.618447],[-9.121729,9.435752,-2.108895,-6.934976],[-7.424700,-5.495875,-2.003770,-8.783859],[1.517450,0.209011,3.705978,7.958658],[-1.198562,-7.667616,9.321900,5.158857],[9.287682,-2.754292,-1.773714,1.838383],[6.919498,-6.070837,-5.353871,-3.053492],[6.432080,4.950473,7.977191,-6.606075],[4.752863,7.823180,7.210691,-1.272428],[-6.682605,-3.325785,5.932539,0.996928],[0.404466,-9.412509,-5.494997,8.323689],[-1.815570,-0.055817,3.375610,-1.342715],[-9.524351,-4.571913,-3.106195,-1.299393],[5.133554,6.603006,-1.641865,2.440802],[-0.912392,5.378328,-8.309416,9.599908],[3.325468,-2.572207,-9.634188,9.752100],[2.361475,-9.071689,0.880068,-0.318338],[-0.961198,0.749619,-3.040265,-3.379212],[9.601611,0.538106,3.647258,-5.732292],[-3.810555,0.618775,2.847070,3.561574],[-6.712204,5.450869,-3.932179,-7.546140],[1.341671,-1.220342,-9.909189,5.885995],[-2.424782,-3.448176,2.013099,1.597430],[8.569626,-3.433535,8.223557,4.524597],[9.639224,7.360514,-2.099406,-4.986709],[-6.102878,1.906598,-1.095692,-2.090665],[5.401222,-0.676497,8.433009,5.907794],[-7.815906,-1.174061,5.021568,-6.603388],[-8.986973,0.957727,6.234496,-3.342094],[-7.110936,8.579811,-6.126053,0.728755],[-5.926333,-3.168027,7.149580,-0.041569],[9.252985,-5.916099,2.656467,-6.295075],[-4.333718,-0.374660,3.370905,9.902400],[2.785143,-1.316103,-4.862497,4.364156],[4.732155,0.416058,6.510343,5.026953],[-9.654078,-5.143375,-5.696409,9.290845],[-5.866078,-0.160849,-9.743202,5.977783],[-4.561034,-9.914918,2.178557,6.562928],[2.839313,-5.545470,7.784493,-3.295824],[4.438833,3.107734,2.942393,-4.055188],[-5.184490,3.976233,9.485088,-1.203672],[4.925766,-8.926465,9.784348,3.146781],[-6.026738,8.643904,6.890901,8.119684],[-6.535947,-0.941075,5.229049,4.724038],[-6.372378,8.948286,7.246007,1.624373],[-0.990520,-0.324491,-5.005105,-3.744614],[2.155453,-6.400372,6.695380,1.941012],[-6.274162,9.219912,-1.316107,1.367570],[-9.286221,-6.736728,0.177657,-2.704648],[-9.814506,6.939898,-7.690243,0.375360],[4.955732,1.096871,-5.398240,5.401817],[-7.895079,-1.468605,9.147878,7.687592],[-7.020823,-9.791338,-8.559807,2.504482],[9.893639,3.373149,7.466062,5.363325],[-2.333492,7.101047,4.463938,8.173924],[-4.883756,-7.439840,7.918651,4.787934],[-0.577101,9.903380,-8.505702,0.899543],[3.403716,4.962565,6.637188,-3.741095],[3.547361,-6.184777,-2.167196,2.809373],[-6.019679,-0.404163,9.663518,2.047677],[7.120075,-6.171033,-7.801191,5.979740],[-9.911347,-5.249517,9.267056,2.951449],[-1.449921,6.046238,1.736709,0.784120],[7.118586,-4.955082,4.923115,-7.774096],[-3.763443,-8.336600,-9.611010,0.536898],[9.215588,-0.896347,-8.863118,3.842668],[-8.928789,2.896851,6.260813,9.790850],[-6.756110,-9.770763,9.017495,8.635899],[9.550182,-7.000623,9.936509,4.660939],[5.031475,-2.232862,6.931939,1.197387],[-7.741712,-9.814791,6.476146,-2.464047],[2.377794,-9.395571,6.581562,-4.746424],[8.056738,-7.527401,-0.948327,5.000456],[-6.117320,1.974979,-7.937078,6.822996],[4.331414,-5.451326,7.387069,6.435252],[5.535185,1.785339,2.800198,-3.227334],[0.469481,5.181079,-4.480615,3.041608],[-0.478556,-1.602358,7.961965,-6.011919],[3.330152,-3.107622,7.857235,2.288092],[9.748063,-2.713355,2.952402,3.504194],[0.257633,-5.595590,-5.488432,-9.465216],[0.489598,3.707935,-0.580384,4.421703],[-2.932367,-2.497223,8.085791,5.028894],[4.287928,1.525457,-6.792153,2.903234],[-0.935620,4.773409,1.145811,9.473328],[-2.721158,-5.258630,-7.980820,3.853852],[4.711896,6.701194,5.684938,4.567601],[-4.712388,7.844478,3.807735,-0.100141],[6.791863,-3.366579,-6.728767,4.625654],[-1.665829,8.470561,6.730753,-2.845078],[9.141405,-1.896643,-3.513288,2.899959],[-7.518257,6.589789,1.588251,9.244154],[1.727749,7.914592,-9.867073,-1.153175],[-9.393066,5.160224,-8.331500,-8.813265],[0.999618,1.917842,-0.719078,-5.818119],[4.322917,5.422381,-9.311158,6.592413],[-7.839703,1.510759,2.612462,-4.316954],[4.727308,-8.607296,8.174623,0.306997],[9.620806,-6.200682,4.131636,-2.669588],[-5.440242,1.942285,1.714499,-1.761379],[-3.773573,-0.402083,6.986033,2.753961],[-7.624751,3.298845,7.928317,1.052323],[4.451604,-6.769300,-4.876865,5.971201],[-9.272154,2.843531,-3.929918,-3.265420]], dtype = "float32")#candidate|9780|(288, 4)|const|float32
call_9779 = relay.TupleGetItem(func_3258_call(relay.reshape(const_9780.astype('float32'), [1152,])), 3)
call_9781 = relay.TupleGetItem(func_3261_call(relay.reshape(const_9780.astype('float32'), [1152,])), 3)
func_5705_call = mod.get_global_var('func_5705')
func_5709_call = mutated_mod.get_global_var('func_5709')
var_9783 = relay.var("var_9783", dtype = "bool", shape = (20,))#candidate|9783|(20,)|var|bool
const_9784 = relay.const([False,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True], dtype = "bool")#candidate|9784|(200,)|const|bool
call_9782 = relay.TupleGetItem(func_5705_call(relay.reshape(var_9783.astype('bool'), [1, 2, 10]), relay.reshape(const_9784.astype('bool'), [10, 2, 10]), ), 0)
call_9785 = relay.TupleGetItem(func_5709_call(relay.reshape(var_9783.astype('bool'), [1, 2, 10]), relay.reshape(const_9784.astype('bool'), [10, 2, 10]), ), 0)
func_4169_call = mod.get_global_var('func_4169')
func_4170_call = mutated_mod.get_global_var('func_4170')
call_9798 = relay.TupleGetItem(func_4169_call(), 0)
call_9799 = relay.TupleGetItem(func_4170_call(), 0)
func_6300_call = mod.get_global_var('func_6300')
func_6303_call = mutated_mod.get_global_var('func_6303')
var_9802 = relay.var("var_9802", dtype = "int16", shape = (234,))#candidate|9802|(234,)|var|int16
call_9801 = relay.TupleGetItem(func_6300_call(relay.reshape(var_9802.astype('int16'), [234,])), 6)
call_9803 = relay.TupleGetItem(func_6303_call(relay.reshape(var_9802.astype('int16'), [234,])), 6)
func_6047_call = mod.get_global_var('func_6047')
func_6050_call = mutated_mod.get_global_var('func_6050')
call_9810 = relay.TupleGetItem(func_6047_call(relay.reshape(var_9802.astype('int16'), [9, 13, 2]), relay.reshape(const_9780.astype('float32'), [24, 48]), ), 0)
call_9811 = relay.TupleGetItem(func_6050_call(relay.reshape(var_9802.astype('int16'), [9, 13, 2]), relay.reshape(const_9780.astype('float32'), [24, 48]), ), 0)
const_9818 = relay.const([[1.033299,-7.481679,5.166053,1.519204,-8.113367,0.993381,4.965283,1.080955,-3.943975,6.497973,6.522573,4.806592,-0.912607,3.589045,0.704174,-3.315793,4.498793,-9.914749,8.007419,-1.810769,0.861755,-9.359169,-0.832654,-2.268362,5.840339,0.455177],[8.975150,3.387543,-9.735550,-7.551451,-6.441140,9.761838,0.439407,-8.028765,5.360680,-4.259463,-5.759932,4.501032,-7.421178,-2.515740,-3.995381,-1.956547,-9.525227,8.461366,6.217484,-5.780180,-2.147794,0.590750,-9.431875,-7.177963,-8.351702,-5.240319],[1.552530,8.020108,8.523379,-1.453477,-9.226477,8.338076,-6.145609,2.744351,-7.471762,2.158600,7.577524,9.261474,2.169464,6.507679,-2.968116,-2.872874,-5.503880,-7.468802,0.044867,5.439966,3.552681,-2.651575,0.549766,0.682392,-8.606328,-1.878749],[7.678149,5.702218,-3.235546,8.476756,-6.381981,-6.970637,2.203416,-0.852961,4.423414,-9.288131,5.534251,5.125907,6.887005,-5.048089,4.492833,9.999294,-5.693517,7.504462,-0.952437,-8.261318,2.726539,8.617904,8.085747,5.322336,4.772349,4.749037],[4.985558,5.649237,-7.822468,-6.923250,-8.249892,-6.363508,-4.630425,6.597455,-2.371466,2.827572,9.953636,0.486311,-4.492953,3.513316,-9.669639,-9.149290,6.685758,-3.479432,-5.447448,-1.324686,6.518910,7.283030,-1.834529,-9.158938,-9.641712,-5.333497],[-7.056476,-9.361359,8.371766,-2.668361,4.560317,9.058335,-3.574714,-7.427786,-4.128810,9.700871,1.964646,3.666252,-9.526606,4.636052,2.871360,-6.619234,6.969405,-4.331232,-1.759428,-6.973031,-8.045420,4.733598,-7.727556,3.638785,-3.899690,-3.370130],[4.237131,9.309228,6.953822,9.918378,7.713041,-8.123540,-9.148136,6.265075,7.833836,-7.397517,0.119393,-3.381855,5.712460,-3.550285,-4.480922,-0.740919,-5.883497,2.096471,-9.784857,-7.340435,-1.582422,-7.925900,6.864255,-1.703846,5.316498,-2.685358],[-1.165191,-2.427439,-9.774750,8.690863,3.904411,6.936757,9.322415,2.663405,1.767436,8.610404,-9.671311,-3.395245,0.937639,-4.086525,-6.773309,1.659986,7.279474,-2.755369,-4.456304,8.311110,9.253112,2.780310,8.845611,-9.459074,-5.296010,2.270870],[0.953452,1.433502,-5.686574,-8.778775,-6.508453,5.822556,6.633983,-9.124194,4.801066,-6.549022,-2.657357,4.600028,-7.343623,-0.174099,-6.306849,-0.379735,9.014184,-8.940453,3.148201,-3.187945,4.577535,-1.743460,-4.535925,-8.927363,-3.020054,-3.028798],[8.414562,-3.496665,-3.107982,-0.825775,-8.461314,-5.923436,-9.033072,9.491859,5.640198,-6.316474,4.499037,-1.704692,1.524716,6.186976,0.784547,-8.208420,-7.051923,-1.344212,3.488607,9.818303,1.037549,3.055991,-7.912465,-4.380410,6.597784,-2.569407],[0.335067,-7.413205,-3.336953,-2.112931,8.972071,-2.148525,6.671853,-6.555870,5.484923,2.581637,-0.368113,4.204543,2.765264,-4.280093,-6.036194,-3.732133,2.277877,-6.626028,-4.573319,9.215950,8.285893,6.635923,3.943136,2.572725,2.726498,5.259836],[1.007642,2.774350,-3.403020,7.609483,-1.764912,-2.581187,-4.861843,3.011889,2.582498,5.470984,-2.493496,-3.771400,-9.013834,5.670344,-5.679909,0.912378,2.522605,-8.531532,8.643269,-4.051882,1.132845,3.438255,5.513182,9.100928,-1.809677,2.185263],[1.803845,-0.790404,1.958755,-4.412532,-1.878188,7.008705,-2.445185,-2.931957,-2.986670,4.770177,0.873488,6.055253,-4.335410,-8.583432,9.091954,8.799870,1.126517,9.091351,6.538941,-8.234969,0.213355,3.237316,7.962298,9.578360,-8.249110,-4.063103],[-5.380773,-2.730076,-3.354738,8.613288,-8.952429,-2.558160,-3.012924,-7.915237,5.004818,2.546410,1.063341,-6.200851,-1.859252,-4.569802,9.037548,3.956687,-3.286333,-7.450042,-2.415548,8.240290,-6.692006,-2.240136,5.949670,5.076911,3.543190,4.549992],[5.629077,9.990495,-6.773053,3.475682,-5.068346,4.763797,-7.642350,0.830729,2.743789,-4.134741,0.752993,-5.957290,1.030712,2.425741,-9.750083,8.850774,9.542993,-3.132268,-3.464575,7.388482,-8.656401,-6.915243,-6.361301,2.770857,-9.635822,5.556581],[-5.459801,-1.993726,9.815943,-6.459083,-1.041786,-9.496203,-6.335410,5.061821,-9.753708,-6.773317,8.847227,8.615193,-4.539103,3.028281,-6.438110,-9.601407,-9.837510,9.158948,0.049168,-7.981235,1.409453,5.386895,5.526881,0.973831,4.893148,-8.192231],[-7.884883,-5.236678,-5.570878,4.614996,-9.302675,9.625025,-8.597372,5.648405,-5.372235,3.436696,-8.539583,4.464541,-5.432432,4.220739,-3.118097,-4.033442,6.441674,-7.680839,0.259333,5.966375,6.879703,-9.593489,0.888460,2.623520,4.333028,1.025637],[9.642865,1.360973,8.109640,4.633809,-8.499993,-8.313657,-8.328849,7.398838,-9.012547,-8.927669,0.630346,7.672301,-3.813838,-6.837516,-5.797459,5.975645,9.140107,4.907842,4.304170,-4.170758,-9.714579,7.271882,3.596649,-8.481332,2.646582,-7.876430],[-8.004793,6.733825,-5.108473,-8.417034,-0.133241,9.408580,2.825379,-9.724584,6.167472,-6.747109,-1.133949,6.021274,8.089133,8.204503,-4.269096,7.777975,-0.637303,4.131924,7.606200,6.095639,7.094684,1.692605,2.432644,4.979506,-2.945759,-1.919148],[0.995557,4.071641,-9.947635,-3.171497,-9.712950,6.490286,-4.166003,6.934096,-2.136024,0.197397,9.041247,-1.180261,4.334437,-0.289132,-5.593970,-6.237619,-9.496654,-3.388364,-1.089443,8.131251,-0.352566,8.167457,1.538637,-8.940232,9.070023,5.502346],[-6.874985,5.387391,9.309861,-2.658417,2.776406,9.173841,-5.841572,-8.921965,-4.939823,7.763714,-0.743752,-1.943857,6.615620,3.038272,-0.751628,-9.873596,2.689773,-2.152131,7.088593,-5.404270,1.860000,-5.518962,9.393593,6.926050,-0.194834,-6.892424],[2.478761,-7.345386,-8.610840,-4.959172,-3.099047,5.709344,-3.549289,-9.924729,-6.197673,-3.010249,-8.232428,1.271561,7.787014,-9.868206,7.781065,-0.061388,2.326418,-7.661459,2.922156,-4.473539,2.353914,5.857990,-6.086845,4.021149,-8.172098,-3.584907],[-4.378909,-6.981646,-4.335357,3.493916,6.678442,2.593857,-5.211545,-5.654826,-9.887912,5.628288,5.343285,7.177213,-5.579285,-8.319582,1.323315,1.696142,3.387593,5.681781,-7.850860,9.484760,7.327034,-0.979246,-5.570747,4.639664,-7.810275,-0.874892],[6.427790,0.874083,-4.464473,-9.282295,-1.460565,2.335222,4.278422,-3.777899,6.528808,1.707527,-6.568951,-4.253766,5.462655,4.966530,-6.285839,0.374654,2.743028,0.952776,-3.802560,6.035398,-3.499038,-0.043268,-7.668294,6.693192,9.160306,-4.458475],[1.022402,-4.007281,-4.031441,-7.784951,-2.167442,-3.542189,-8.588803,0.464330,4.667238,3.335038,-4.298179,9.021908,-0.727968,-6.626916,8.652577,3.833721,-6.163747,7.742182,1.893215,4.274451,4.237963,-1.459807,-5.080525,4.623044,-2.613357,1.224697],[-7.337468,8.702488,3.702286,-2.382964,-2.123333,3.931251,-8.688659,6.782503,-3.249325,0.554016,-0.261830,5.576386,0.697674,-5.473042,-4.144164,-1.352749,-5.573182,9.507926,-1.614104,5.312518,-8.301029,7.992674,0.737802,-3.012394,9.199017,-7.870831],[7.583526,-8.654492,-5.048555,9.881781,-0.370315,1.928510,5.299020,9.350313,6.643306,8.081063,3.262335,-2.763930,4.025844,4.727043,-9.492535,0.417847,8.311888,-1.852233,-7.056000,-6.522303,-2.611182,-4.118075,0.344585,2.288443,-5.239179,-2.394488],[9.485254,-0.059305,2.287107,0.440530,7.414610,-4.601582,0.024989,-7.175226,-0.127941,-1.227837,7.176180,-4.337300,-2.105892,6.768533,-0.282032,4.545668,-6.841470,5.630348,5.835884,3.038311,1.561336,3.566258,-2.408985,-7.911065,7.942911,6.157103],[2.964627,1.939945,4.514088,-8.699572,-5.515499,3.973597,-8.282768,-2.582235,-0.328917,-9.334257,7.501651,-0.739833,-1.466975,-7.848926,2.683517,-5.423914,-5.101203,7.466714,-8.120750,9.960734,5.528154,0.280349,3.352445,6.545087,9.883582,6.082569],[3.524349,-4.775745,5.139191,7.411302,2.648487,0.792116,5.487223,8.313513,4.371824,-4.381252,-0.257328,-4.488444,-8.395484,2.970126,7.503828,-2.285064,-9.862048,-0.283986,-4.560439,-6.918400,5.300096,5.551706,-0.835917,-3.264642,6.022270,-5.453603],[-6.701886,-8.031393,-0.179657,-0.192806,-5.884466,1.760343,-7.282154,-8.139655,8.479582,-7.363011,0.702480,-3.838447,-2.135527,8.658576,5.230860,3.449881,-3.517669,-0.691207,7.778732,-1.149615,-4.002282,-1.658732,-9.385203,4.028618,-7.655506,-4.430405],[4.943978,6.116153,-3.192674,1.362594,1.495504,7.860306,-8.247884,-5.742828,1.727612,-1.824919,-1.508402,-8.694711,8.717608,0.274156,2.360841,7.830317,-0.273790,-4.294988,5.869521,-3.691877,5.773707,-3.393733,-8.334968,9.528476,-1.954519,6.818536],[9.528979,0.640056,8.816386,-5.064766,-9.406366,5.425503,-0.909819,6.138101,0.994212,-6.461442,-2.217589,3.817007,-6.157080,-7.865401,-9.647281,0.827126,5.142904,-3.652130,4.191860,1.616368,1.002724,-3.476897,-6.204171,1.300182,-8.274981,-4.623064],[6.119648,0.475864,9.829708,-1.791616,4.644349,6.246739,-1.696438,1.900255,-2.157815,1.612418,2.487232,6.157098,-6.615325,0.313588,5.019995,2.708785,3.599035,-5.892911,-6.942583,-5.457895,-6.443913,-4.425411,-8.446875,1.175004,-2.437750,-8.111500],[-8.573647,8.172466,-6.724776,7.670542,1.300257,-6.359625,8.259036,1.101043,2.573928,7.498354,4.045646,-6.559533,6.638155,-2.786055,7.681732,4.311251,-9.207505,-4.509512,-1.759139,-5.642905,-5.745232,-8.642361,2.784277,2.852882,-7.348877,1.444798],[-1.957649,0.689532,2.513310,6.968362,-4.662023,-4.184453,6.467345,0.071467,5.655492,2.289220,9.554376,6.890503,1.135282,1.518273,-3.700209,6.771308,2.976963,-8.090899,-8.412077,6.135469,2.986436,-5.731116,-2.146310,-7.789093,6.210033,1.463491],[2.466778,-9.342587,7.804438,-5.293343,-4.897203,-8.613505,-8.974285,-4.769097,-2.574299,7.967618,9.696535,-9.854702,-1.577391,5.973833,2.952811,-8.522187,-6.375668,9.063238,-7.076504,0.093618,-2.790092,-9.525910,-1.410723,5.634029,-0.249924,-3.415731],[-9.709701,1.161899,8.163426,6.375913,7.056008,-2.361951,-7.843093,7.988780,9.826051,2.834150,-4.808744,7.651113,-9.056236,3.535773,7.980264,-7.496447,7.246010,-6.360854,9.673313,3.773864,1.003920,-8.181493,0.144341,9.285072,-4.293046,-2.261491],[-2.187796,5.589286,5.399550,-9.582471,8.643950,-8.830962,-2.453269,6.161375,-6.246153,0.203933,-3.003942,2.365942,6.388092,1.441177,0.760507,1.498332,3.942407,-5.486979,5.138983,5.142221,-7.433416,1.027746,0.365083,-1.033647,8.611499,1.240016],[7.065572,-1.662309,7.346104,-5.267079,5.310860,6.474523,-1.394359,6.299240,-6.796929,-4.474467,5.067875,2.382551,1.231651,-1.417335,4.417143,-5.050540,0.687987,-3.371160,-4.431233,3.512606,-9.060898,-9.577802,0.417873,-6.642433,5.621138,-5.707409]], dtype = "float32")#candidate|9818|(40, 26)|const|float32
bop_9819 = relay.mod(call_9779.astype('float64'), relay.reshape(const_9818.astype('float64'), relay.shape_of(call_9779))) # shape=(40, 26)
bop_9822 = relay.mod(call_9781.astype('float64'), relay.reshape(const_9818.astype('float64'), relay.shape_of(call_9781))) # shape=(40, 26)
func_3757_call = mod.get_global_var('func_3757')
func_3761_call = mutated_mod.get_global_var('func_3761')
const_9831 = relay.const(-7, dtype = "int32")#candidate|9831|()|const|int32
var_9832 = relay.var("var_9832", dtype = "int32", shape = (2, 1092))#candidate|9832|(2, 1092)|var|int32
call_9830 = relay.TupleGetItem(func_3757_call(relay.reshape(const_9831.astype('int32'), []), relay.reshape(var_9832.astype('int32'), [13, 14, 12]), relay.reshape(call_9801.astype('uint16'), [180,]), ), 3)
call_9833 = relay.TupleGetItem(func_3761_call(relay.reshape(const_9831.astype('int32'), []), relay.reshape(var_9832.astype('int32'), [13, 14, 12]), relay.reshape(call_9801.astype('uint16'), [180,]), ), 3)
func_7089_call = mod.get_global_var('func_7089')
func_7090_call = mutated_mod.get_global_var('func_7090')
call_9834 = func_7089_call()
call_9835 = func_7089_call()
func_8441_call = mod.get_global_var('func_8441')
func_8446_call = mutated_mod.get_global_var('func_8446')
const_9862 = relay.const([-9,5,2,7,7,-1,6,10,-10,2,-9,3,-5,4,-10,-5,8,2,-7,9,-10,4,4,-2,3,4,-10,8,9,-1,-7,-7,8], dtype = "uint32")#candidate|9862|(33,)|const|uint32
var_9863 = relay.var("var_9863", dtype = "bool", shape = (231,))#candidate|9863|(231,)|var|bool
call_9861 = relay.TupleGetItem(func_8441_call(relay.reshape(const_9831.astype('uint32'), []), relay.reshape(const_9862.astype('uint32'), [3, 11, 1]), relay.reshape(var_9863.astype('bool'), [3, 11, 7]), ), 2)
call_9864 = relay.TupleGetItem(func_8446_call(relay.reshape(const_9831.astype('uint32'), []), relay.reshape(const_9862.astype('uint32'), [3, 11, 1]), relay.reshape(var_9863.astype('bool'), [3, 11, 7]), ), 2)
bop_9875 = relay.greater_equal(call_9779.astype('bool'), relay.reshape(const_9818.astype('bool'), relay.shape_of(call_9779))) # shape=(40, 26)
bop_9878 = relay.greater_equal(call_9781.astype('bool'), relay.reshape(const_9818.astype('bool'), relay.shape_of(call_9781))) # shape=(40, 26)
func_5830_call = mod.get_global_var('func_5830')
func_5831_call = mutated_mod.get_global_var('func_5831')
call_9882 = relay.TupleGetItem(func_5830_call(), 0)
call_9883 = relay.TupleGetItem(func_5831_call(), 0)
var_9893 = relay.var("var_9893", dtype = "int16", shape = (234,))#candidate|9893|(234,)|var|int16
bop_9894 = relay.mod(var_9802.astype('float64'), relay.reshape(var_9893.astype('float64'), relay.shape_of(var_9802))) # shape=(234,)
output = relay.Tuple([call_9759,call_9769,const_9780,call_9782,var_9783,const_9784,call_9798,call_9801,call_9810,bop_9819,call_9830,const_9831,var_9832,call_9834,call_9861,const_9862,var_9863,bop_9875,call_9882,bop_9894,])
output2 = relay.Tuple([call_9760,call_9770,const_9780,call_9785,var_9783,const_9784,call_9799,call_9803,call_9811,bop_9822,call_9833,const_9831,var_9832,call_9835,call_9864,const_9862,var_9863,bop_9878,call_9883,bop_9894,])
func_9898 = relay.Function([var_9783,var_9802,var_9832,var_9863,var_9893,], output)
mod['func_9898'] = func_9898
mod = relay.transform.InferType()(mod)
mutated_mod['func_9898'] = func_9898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9898_call = mutated_mod.get_global_var('func_9898')
var_9900 = relay.var("var_9900", dtype = "bool", shape = (20,))#candidate|9900|(20,)|var|bool
var_9901 = relay.var("var_9901", dtype = "int16", shape = (234,))#candidate|9901|(234,)|var|int16
var_9902 = relay.var("var_9902", dtype = "int32", shape = (2, 1092))#candidate|9902|(2, 1092)|var|int32
var_9903 = relay.var("var_9903", dtype = "bool", shape = (231,))#candidate|9903|(231,)|var|bool
var_9904 = relay.var("var_9904", dtype = "int16", shape = (234,))#candidate|9904|(234,)|var|int16
call_9899 = func_9898_call(var_9900,var_9901,var_9902,var_9903,var_9904,)
output = call_9899
func_9905 = relay.Function([var_9900,var_9901,var_9902,var_9903,var_9904,], output)
mutated_mod['func_9905'] = func_9905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6996_call = mod.get_global_var('func_6996')
func_6997_call = mutated_mod.get_global_var('func_6997')
call_9931 = func_6996_call()
call_9932 = func_6996_call()
output = relay.Tuple([call_9931,])
output2 = relay.Tuple([call_9932,])
func_9943 = relay.Function([], output)
mod['func_9943'] = func_9943
mod = relay.transform.InferType()(mod)
mutated_mod['func_9943'] = func_9943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9943_call = mutated_mod.get_global_var('func_9943')
call_9944 = func_9943_call()
output = call_9944
func_9945 = relay.Function([], output)
mutated_mod['func_9945'] = func_9945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9230_call = mod.get_global_var('func_9230')
func_9231_call = mutated_mod.get_global_var('func_9231')
call_9972 = func_9230_call()
call_9973 = func_9230_call()
output = call_9972
output2 = call_9973
func_9975 = relay.Function([], output)
mod['func_9975'] = func_9975
mod = relay.transform.InferType()(mod)
output = func_9975()
func_9976 = relay.Function([], output)
mutated_mod['func_9976'] = func_9976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7360_call = mod.get_global_var('func_7360')
func_7361_call = mutated_mod.get_global_var('func_7361')
call_9983 = relay.TupleGetItem(func_7360_call(), 0)
call_9984 = relay.TupleGetItem(func_7361_call(), 0)
output = call_9983
output2 = call_9984
func_9985 = relay.Function([], output)
mod['func_9985'] = func_9985
mod = relay.transform.InferType()(mod)
output = func_9985()
func_9986 = relay.Function([], output)
mutated_mod['func_9986'] = func_9986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5830_call = mod.get_global_var('func_5830')
func_5831_call = mutated_mod.get_global_var('func_5831')
call_10015 = relay.TupleGetItem(func_5830_call(), 0)
call_10016 = relay.TupleGetItem(func_5831_call(), 0)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_10017 = func_7077_call()
call_10018 = func_7077_call()
func_7624_call = mod.get_global_var('func_7624')
func_7627_call = mutated_mod.get_global_var('func_7627')
var_10032 = relay.var("var_10032", dtype = "bool", shape = (490,))#candidate|10032|(490,)|var|bool
const_10033 = relay.const([-2.732569,-5.926838,-5.013496,-0.875513,0.968484,-2.231216,-1.194702,2.353376,-5.739292,1.133631,7.434542,6.358884,3.509520,-4.238475,9.776782,8.181870,-2.853321,0.078116,-9.744533,6.856803,-9.157189,-8.802215,-1.767349,0.273807,-0.936810,0.436351,4.829394,0.433695,-3.200542,0.152227,1.906673,4.299027,-2.461308,-5.026381,1.224381,-5.291168,7.098019,-5.152530,-6.386495,-0.474264,-2.691619,-5.082994,1.290371,4.879955,-8.441556,5.165375,0.575865,7.143173,1.305934,-8.490406,1.985571,-7.979155,-2.144747,5.431263,-1.091256,1.524713,1.050168,-3.506384,2.925129,-0.148425,-1.532336,0.384018,5.409095,6.124500,-4.759960,0.812132,-2.180284,-4.597241,-7.269432,2.280312,-8.570508,-9.881497,9.861974,-9.733792,-3.865879,-1.335456,-1.427596,-7.509372,-9.583564,-3.336784,-8.488361,-6.112676,4.165546,8.535880,-9.317143,2.020176,2.365751,1.706295,-6.381415,8.483653,-0.556294,-7.914642,5.781784,-8.929924,-6.963169,-3.377238,-8.288682,-2.908019,1.327648,-9.248408,-2.241617,-8.338754,7.314285,-4.029012,4.647036,-2.425802,4.421049,-9.712924,6.958220,-8.808961,4.591687,-2.471030,-3.009956,-8.449133,-5.277420,3.689738,-6.415567,-5.055698,9.961577,8.577523,-5.544667,1.119317,-4.581455,-6.569895,-2.323301,-7.340482,5.410454,-3.712074,6.546092,-0.693646,7.494848,-2.209076,1.200828,6.968196,-4.189630,-5.417766,-5.899104,-7.716367,6.696717,-7.010538,-6.411166,-7.071355,-4.924457,3.744562,2.170525,0.458825,6.892135,-3.592929,5.642998,-5.861666,-6.668877,-0.993916,-1.688234,-5.482298,-6.706670,6.184564,1.308349,-1.753455,-3.674604,0.837690,6.409941,-0.114057,-5.947506,-7.353400,-7.107041,6.920607,7.541933,7.099034,4.913890,4.534089,2.503121,-7.747530,-7.673504,-0.362507,-7.256460,-6.894596,-2.188171,-6.307174,2.641216,-3.110456,3.710720,5.789498,-2.676179,-9.021662,-4.943800,3.949451,7.263774,-5.407027,-2.879832,-7.084514,-8.831739,6.719628,-4.695130,6.129473,-4.311343,3.300038,-2.291556,-1.334068,-6.878186,-5.641503,-4.608258,-0.541904,1.049092,-8.996352,8.279938,-9.660098,9.098588,-0.457961,3.813954,-3.782223,-4.841249,-5.236117,-2.899963,5.136877,8.242744,1.169131,6.336856,6.655431,-2.945614,-3.145402,1.090576,8.302460,-8.360365,-5.697158,9.260852,8.044959,-2.594687,-8.676644,-5.938529,3.414225,9.630473,-3.460501,-8.133499,5.838695,5.840019,-6.636046,-8.520448,0.420802,-9.455611,2.526987,-4.031984,6.749252,-1.279816,9.788622,2.174061,-0.504607,0.417067,9.510356,3.142431,-9.423589,-7.159790,7.074873,-8.587395,-7.840423,-1.668695,8.208462,-4.221018,9.130483,-9.238389,-5.193586,-0.929917,1.441783,1.589001,8.245223,5.405966,1.551037,3.307452,6.860627,3.872708,-3.656490,7.846171,4.518609,-7.991049,-1.527514,1.331794,-9.562942,5.821041,-2.286090,-8.385005,4.267922,3.517596,4.327402,1.651465,6.045668,-7.053172,-4.812195,3.408808,-1.040026,0.311555,-2.708663,4.473503,-0.739499,-7.872339,0.074065,-6.881789,8.413549,1.621382,-3.833358,6.887237,4.394800,1.387520,4.636347,7.711067,-7.397139,-8.439825,-2.511252,3.904669,-5.800191,3.664895,-6.412613,1.467583,7.206892,4.825302,1.766076,5.846975,-0.522791,2.132856,2.039012,0.421573,0.659085,4.075148,7.186358,-5.246463,-4.175291,9.846317,9.182372,-2.070650,0.764125,4.191985,-2.503889,-4.411221,1.401001,-0.264644,-4.162840,9.237502,3.789521,5.366922,4.797657,4.721069,5.253731,5.616790,5.439314,-7.971724,4.359436,6.208440,-7.162235,-4.505985,9.554374,9.790803,6.970018,1.540753,7.208526,5.247094,-9.357811,-4.595266,-7.566347,8.290961,-4.751640,-2.293376,6.278842,8.617688,3.506635,0.823987,6.601012,2.130569,9.804244,6.891276,5.206262,-5.244303,6.345501,-4.987132,-5.126452,7.915958,8.901181,-5.252005,-1.883543,-8.681110,1.457999,-8.523638,-7.699025,6.815909,8.355910,-3.676761,-4.448322,-9.381917,-7.342890,6.712955,-0.534566,3.914372,-1.525559,-7.089059,8.469578,6.217929,5.338116,0.061653,0.667598,2.701295,-5.781153,2.314754,-5.843625,-5.826454,-1.110582,0.027179,6.238656,-9.898927,-1.067731,-3.797308,-7.811386,9.992692,6.325234,1.313128,3.155004,5.185154,2.186987,-5.770327,9.107051,-7.331445,-2.517003,-0.749084,-4.487930,-5.692276,-3.368167,-7.159892,-3.129680,-4.909855,6.014401,-6.303237,-4.310701,-9.289482,-1.369607,-4.031783,7.155594,-2.860018,-6.615514,2.145666,8.535348,-3.744203,-5.444999,-0.706988,-4.596992,8.130468,9.119148,-9.360246,8.417222,0.693933,-9.216773,0.154730,-9.246426,2.239979,6.800910,4.996818,-5.284853,-9.284405,-8.021432,7.216623,7.341257,-2.765573,-5.674535,-1.104496,3.046231,-8.405243,3.719687,-0.906969,4.636409,4.287555,-9.046216,0.130965,-4.859398,-5.899855,4.488147,4.929864,-2.887451,7.065217,-1.443672,-5.798348,0.776499,9.972716,5.222048,-9.685333,-0.127752,9.610435,-0.355069,5.151041,-8.970333,7.086035,-1.038430,-2.839493,8.511657,7.938384,3.188738,6.738978,-3.680944,-0.518143,-7.487407,-4.864269,-1.064226,-0.328501,9.516283,4.123711,7.365321,5.691892,7.788179,-2.395838,6.673355,-5.955572,0.676898,1.361403,8.832161,3.120480,-2.824536,-2.237594,9.851046,8.063593,-6.181592,-4.994588,2.392583,0.455489,5.047218,2.694995,-6.852605,-7.064890,-7.294191,6.485358,6.237701,4.303633,4.055126,-8.921917,-7.395125,7.431932,-2.228441,-8.881471,7.009997,-7.667536,1.001367,8.939207,8.531346,-1.176530,7.093554,0.511736,-5.634510,-6.742809,-8.858411,7.061910,-6.314114,-6.802179,-2.014181,-2.579693,-0.286403,5.645819,3.456184,7.534192,-1.582133,-1.324562,-0.724126,-6.484491,-9.035314,-5.075083,0.902523,-3.461283,-5.459622,-9.067717,5.173397,-4.069776,4.217220,-9.152661,-3.824435,1.049156,4.305798,-2.196411,-4.412360,-6.358576,9.647295,1.764569,-4.927029,-2.264935,-1.064170,-5.041779,3.816698,-9.567915,-6.778760,6.843922,-1.369060,1.676827,-3.707222,0.624173,-9.884237,-2.360007,-9.523078,-3.379340,0.788837,4.518788,2.505383,0.475000,-4.679551,2.811419,-6.921282,1.728127,6.733902,-4.549464,-0.061290,-6.061928,-6.121726,-3.920663,5.193872,8.111690,7.951895,-9.997496,-0.577325,-5.131662,3.902072,6.830331,-3.492532,9.745768,5.516769,-0.707203,6.299027,-4.519917,4.801243,2.897375,3.438975,4.328864,4.984188,7.138506,1.044787,2.883527,3.955639,4.149313,3.825117,-1.216742,-4.132976,9.332542,8.380841,4.886590,-8.837313,2.275078,-1.385096,0.792445,0.232421,0.989760,-8.688562,4.937583,-8.899894,4.839500,6.337761,-6.676333,-7.777822,-0.380524,-3.513543,-0.190213,-4.486674,-7.869982,-7.122174,-8.986870,3.968794,6.204916,-5.225064,1.581627,6.390242,7.564855,-4.216877,-7.762334,6.743047,6.515812,4.577782,-2.566517,0.532879,-7.699482,-1.528930,6.184807,-5.636342,3.636571,-6.192403,9.124685,-5.531507,-7.206683,7.919811,3.635766,1.894090,-0.362195,2.919866,-9.040489,4.193533,-0.966881,-5.920205,3.144460,-4.670038,5.249855,-5.965821,-1.102354,5.834997,0.353467,-2.794431,9.193855,1.617726,-4.550361,6.615855,-5.999818,0.767265,-6.690346,-9.636231,-6.965849,9.831410,9.530382,6.361125,-0.216053,7.878321,4.352056,-2.178892,8.821976,-5.472356,-6.122482,5.821099,-0.255803,-0.348316,-3.057365,9.759483,5.175796,-2.180684,-0.529873,0.968493,1.487688,-3.804442,-7.716257,7.529671,1.649353,2.454725,9.937395,-7.575654,8.896332,9.177702,2.623432,-8.825766,4.682898,-9.791706,-2.743965,-1.469677,-5.828421,-2.269540,7.312746,-5.828119,3.252776,4.209003,-7.044733,5.364472,-0.429794,1.383278,8.211960,-2.118089,3.805981,-4.837993,-3.171897,8.052704,9.846337,4.308328,1.142066,0.805928,4.553084,-4.711430,-8.879975,6.519056,-8.929890,9.566638,9.253534,-3.828652,-7.187272,-9.428144,8.256078,8.338247,-0.223259,5.876362,-9.211217,-2.019417,4.916430,-6.254145,-7.471270,-9.798195,-1.615333,-5.242688,-6.829095,-3.925779,8.982050,8.787815,-2.313041,-7.204318,-9.259503,1.751006,-3.785528,-3.721824,-8.581227,-3.286485,0.886942,2.039231,-0.490950,0.422130,-0.627609,8.984141,-9.132286,-4.214204,1.359824,0.428734,-3.340233,-3.866379,0.060327,2.207871,7.833733,-4.533152,-9.389588,0.329354,-1.922857,9.691604,-1.632744,-2.043281,-0.744034,-0.821628,9.431003,9.611368,-9.290234,8.559810,-7.791332,1.848480,-8.789239,-9.085578,3.239020,6.797928,-7.718518,-5.283691,5.594381,-1.956371,7.834240,6.417290,-8.049769,-6.026519,-8.628839,-9.690006,-2.530130,9.371688,-6.556321,-2.776430,9.885682,7.541551,-3.499767,-9.979402,-1.425621,5.910577,8.902281], dtype = "float64")#candidate|10033|(845,)|const|float64
call_10031 = relay.TupleGetItem(func_7624_call(relay.reshape(var_10032.astype('bool'), [7, 70]), relay.reshape(const_10033.astype('float64'), [845,]), ), 1)
call_10034 = relay.TupleGetItem(func_7627_call(relay.reshape(var_10032.astype('bool'), [7, 70]), relay.reshape(const_10033.astype('float64'), [845,]), ), 1)
func_7479_call = mod.get_global_var('func_7479')
func_7480_call = mutated_mod.get_global_var('func_7480')
call_10049 = func_7479_call()
call_10050 = func_7479_call()
output = relay.Tuple([call_10015,call_10017,call_10031,var_10032,const_10033,call_10049,])
output2 = relay.Tuple([call_10016,call_10018,call_10034,var_10032,const_10033,call_10050,])
func_10054 = relay.Function([var_10032,], output)
mod['func_10054'] = func_10054
mod = relay.transform.InferType()(mod)
mutated_mod['func_10054'] = func_10054
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10055 = relay.var("var_10055", dtype = "bool", shape = (490,))#candidate|10055|(490,)|var|bool
func_10054_call = mutated_mod.get_global_var('func_10054')
call_10056 = func_10054_call(var_10055)
output = call_10056
func_10057 = relay.Function([var_10055], output)
mutated_mod['func_10057'] = func_10057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6068_call = mod.get_global_var('func_6068')
func_6069_call = mutated_mod.get_global_var('func_6069')
call_10062 = relay.TupleGetItem(func_6068_call(), 0)
call_10063 = relay.TupleGetItem(func_6069_call(), 0)
func_2696_call = mod.get_global_var('func_2696')
func_2699_call = mutated_mod.get_global_var('func_2699')
var_10067 = relay.var("var_10067", dtype = "bool", shape = (18, 78))#candidate|10067|(18, 78)|var|bool
const_10068 = relay.const([[0.577552,-5.270934,6.584740,7.007224,9.432113,9.052987,-1.475295,3.421436,-5.619490,0.217075,-9.100639,-3.822847,4.071112,-2.551992,-2.034365,-2.153935,-1.664024,-9.156815,0.627485,1.940983,-1.662189,-4.871715,4.927291,-4.424578,-7.731033,-4.614208,-3.302074,-0.360970,6.266651,7.700907,-7.649044,2.595622,-7.140399,-0.047935,1.551954,4.555669,-4.521814,2.912338,6.338802,-1.267017,1.519144,7.030876,4.030269,-7.372870,-4.632424,-6.189322,3.880023,-7.166856,4.728679,8.720118,-3.980481,7.496290,-7.844699,-5.166331,-9.197517,-6.186036,-4.292573,3.378099,1.779298,-4.284564,8.530926,-3.907463,-6.813739,7.704685,0.563812,-6.705958,6.512661,3.725023,-8.404159,9.511383,-8.338957,5.244570,6.089729,-0.730922,-1.773462,9.352791,7.367704,-2.759240,-3.836412,9.909194,0.620197,9.469726,7.258758,-5.370798,0.509658,2.299284,5.937887,-9.677057,2.289862,5.039053,2.917524,-9.291066,-0.402048,-0.538589,-9.395349,7.684096,8.587547,-7.412187,4.058677,0.491406,-8.752256,-7.361447,2.238921,3.859204,3.773973,-6.580636,7.891342,9.704425,4.367578,-6.680116,9.028139,9.381669,-7.859670,-4.470889,6.547052,-2.935856,-9.665407,2.071607,6.414038,-5.261134,-8.236004,0.118457,3.802043,9.128092,-9.073117,-5.108382,1.204078,2.727632,9.053235,4.290991,4.667281,9.622240,-4.690790,2.017280,9.033451,-3.339357,-8.634579,8.543240,-9.683191,-7.318239,-1.648638,3.986751,4.261434,7.644619,-4.396938,8.499743,9.627719,0.397665,9.680246,6.017080,-1.828248,-8.076745,-1.901249,0.840500,8.098897,7.762007,-1.384363,4.732905,2.204599,2.475047,-1.297670,9.566238,5.899280,3.883167,6.772212,7.090372,4.456910,-5.291913,6.370107,-6.454867,-0.681052,-4.623376,-1.613902,-6.986302,-9.554484,9.481974,-0.707165,-8.810320,3.718384,-9.862314,9.000019,4.392985,-9.211867,-2.896315,7.934641,-8.762205,-9.283176,-8.187751,-9.400005,1.325548,-4.731249,3.750125,6.044925,-0.699179,-5.430718,-2.058623,-2.693848,-2.250103,7.706537,-7.313586,9.826478,-2.284490,9.657758,9.541897,7.531104,3.314056,2.545427,-6.683707,-4.076079,-5.472950,-3.127451,-7.478510,-6.199097,7.868152,4.157688,-7.870889,-3.812799,3.230961,2.011325,1.062049,8.407522,6.122565,-2.105923,8.951899,-0.744120,2.648760,-6.829734,-6.226881,-2.502450,4.513191,3.507345,-4.413585,-6.576811,-5.919207,-4.650241,8.003661,-7.310934,2.935649,-7.878502,6.276762,-2.115546,1.327939,0.828677,1.721256,3.232070,8.808749,-2.803519,-5.738127,5.780715,-9.367823,5.381169,7.937465,-1.825026,-4.583479,-0.357785,-2.790616,-8.934447,9.466247,2.131380,1.454191,4.770192,1.024224,-6.433393,2.350499,-5.368872,-8.159984,9.855965,8.372361,-0.994393,-2.860032,-0.186826,7.349745,1.428128,-9.166247,6.223008,4.898518,-5.577230,-8.324479,8.238622,5.982786,1.998533,6.071643,7.140042,9.620118,-3.784759,-2.839343,-3.617267,6.731387],[1.282447,-3.290624,2.414843,2.185081,-6.189289,-0.059894,1.313120,-7.920553,1.726429,5.453495,-4.700232,-8.332384,9.911939,1.598843,-6.565398,5.993536,-1.530284,-4.146564,8.029669,-7.472487,4.459155,8.155276,-6.147810,-2.661363,3.380361,-7.055184,-4.782883,-0.990845,-0.305674,1.669780,-2.483579,-7.238378,-5.410716,-8.163390,-3.196250,9.498330,-3.070409,6.184616,-2.093035,-1.773575,7.319692,-9.582502,-8.541784,8.812069,-3.138280,6.007025,6.069162,-5.885455,4.977922,-5.048442,1.627658,9.475998,-2.260443,-8.094227,-3.990635,3.846928,7.656375,5.791794,-2.003352,-8.303046,6.135088,-4.629760,2.191841,-2.057437,8.863478,0.480277,5.634336,-5.979857,7.437223,-2.725103,-3.564437,5.136799,0.360848,4.005373,-6.689738,7.992227,4.286476,-5.919320,-4.184867,3.194432,7.815951,-8.576958,-8.960007,8.353352,3.586513,7.899983,6.670183,0.262992,-3.016047,-8.060053,7.383362,-0.029786,3.501381,6.908879,-6.870290,-8.288203,8.836195,-7.773561,2.445010,5.050800,6.286463,-3.174967,-5.306909,-7.969886,-5.675904,5.800275,-5.346531,6.179517,-0.391363,0.442127,4.606072,0.269886,-3.836159,-5.403922,1.753877,-9.934616,7.758264,7.455149,-7.663307,-3.600097,-2.753276,-1.004808,0.933150,5.469799,5.642586,-6.048589,-4.347641,1.384609,4.305688,-3.600522,-4.113334,-3.749754,-2.860432,8.181500,5.821156,3.031310,0.314773,-9.634755,7.882447,-5.953626,-9.001210,-7.635844,-4.731879,8.306225,5.647369,-3.529327,-0.994496,1.720596,-5.934643,6.993988,-6.877054,-7.545921,6.885371,8.172592,-4.049926,6.392291,-5.721415,0.236785,9.064226,8.491797,-1.304439,-7.202651,-8.310706,3.907172,-9.193124,-2.333140,-3.671648,-2.351491,8.240512,-2.245154,-8.021272,-6.637814,8.447136,8.893648,-6.547998,-9.170033,1.521993,7.390566,-6.212195,-3.883109,7.091603,-2.298059,2.248768,9.650310,-3.131238,-2.402371,8.513922,9.387172,-8.155042,-5.098943,9.160720,-0.688434,9.195129,-6.537504,-1.119455,0.462366,9.093519,5.112940,-1.737563,2.330934,8.455728,3.547946,-9.115995,2.087327,-4.311420,4.567257,-3.618745,-9.259935,9.187565,-9.102332,2.902893,-1.585786,2.897029,-7.928660,-5.388607,-7.116467,7.871381,2.079146,-9.031802,2.252201,-5.133030,8.256523,-0.348312,-3.273208,-8.495970,9.073836,-0.576902,2.229518,-5.515376,-8.349593,6.337028,-2.265644,-0.814294,3.369626,-6.948693,4.007829,7.785789,-4.956534,-5.589915,-0.097357,1.654968,5.493073,4.752669,8.876606,-7.175753,-5.810579,-7.276615,-2.867592,-0.233545,5.504452,-7.962873,6.451802,3.219484,4.073129,2.645501,9.397405,-5.182074,-6.845830,6.471424,7.582368,4.977155,1.492015,-0.548237,7.866595,9.042808,3.231679,4.856487,-8.309922,-0.097328,9.083491,2.244577,-7.613191,1.544120,3.901128,-1.940197,-9.417619,-4.202516,4.345009,8.941088,-0.393740,-7.966988,7.668910,-3.049590,-6.150154,2.307179,-2.584910,-2.925655,-7.294970],[-6.854344,-7.789545,-0.458073,-7.036330,7.771768,5.818964,-3.622355,4.821647,-0.061498,2.038906,-3.371544,5.667795,5.343296,-5.103023,9.385013,7.471053,-9.344150,-0.285697,-1.494868,-0.405726,1.130142,-6.506902,5.478874,-5.298288,-9.670090,-3.873938,2.232279,8.543191,-4.869544,1.907256,-3.942541,6.172775,-9.624627,-2.972663,-5.738259,-7.195343,-5.519039,-3.164927,9.833634,7.280175,-8.886961,-6.946919,-5.626642,-5.040602,-2.981413,-0.815742,-8.183849,4.961131,6.140003,3.104236,-0.764455,1.745510,-8.339116,-9.821098,-8.489837,-9.752342,-0.543492,9.958364,-6.942552,9.872556,2.465705,5.887276,3.871592,-1.271410,-1.320430,-0.804672,-4.761989,-5.837063,8.621263,-6.693240,-2.401693,-7.259198,5.166626,9.236136,1.597911,-8.130361,-3.141444,-3.107465,1.969957,1.879532,-5.070720,-1.237877,5.177537,-1.950046,-2.848339,0.662203,8.832720,8.847684,1.717787,-5.262142,6.298903,4.209629,-3.840512,8.337920,-2.059035,-9.782377,-7.676204,3.227332,1.165116,4.783311,-3.013706,-9.088951,-0.502468,1.397289,8.725749,1.126110,-5.532574,-6.559256,-3.757371,-4.735619,-7.960746,-4.501768,-3.204511,2.723793,2.043870,1.382337,4.856958,5.154533,6.828825,0.638501,-7.122602,7.598953,2.728137,0.118140,3.220944,-9.596007,-0.456451,-7.175232,7.945170,-1.688184,-3.058911,-7.203074,-8.927152,-0.375896,-6.602138,-9.748677,-9.497643,-2.683491,9.292635,3.605221,1.195077,8.527349,-8.242407,-4.964911,6.513431,-1.107848,-1.405515,5.936611,-3.739199,-7.909749,2.878823,9.842435,-1.842231,3.550338,-4.347595,-5.573643,-0.305470,1.228776,-3.991556,-3.260775,3.967707,9.983530,-6.697274,-4.153735,-6.658701,3.701666,4.455776,3.861345,-4.074518,7.066669,-2.311615,1.712958,2.078375,9.119494,-9.819958,7.565606,6.125098,-5.561988,0.859742,-2.875009,0.093972,4.337406,0.709235,6.206225,6.693048,-5.543829,-9.672319,7.533579,-8.721551,5.437385,-0.279181,-1.997755,-9.900427,3.293906,5.274854,6.692531,-4.015781,8.224296,-6.262814,1.615832,-2.049099,1.349629,3.744975,-8.287580,0.614498,7.744237,2.786439,6.407327,-1.976617,9.377973,3.106807,-7.107500,-6.997158,2.872405,-1.591690,-6.200654,-7.380028,-2.456255,-4.766118,9.806668,-9.388946,-6.132875,8.419590,8.115446,-3.542878,3.822815,-0.826259,2.073211,-5.237312,0.711311,-0.932643,3.077733,4.282723,-4.108848,-2.995342,4.500086,-7.949362,-2.492276,-3.944459,9.712531,1.101062,-7.122573,8.087251,-5.768935,-4.962549,-8.473079,4.296882,0.924100,7.533275,9.744732,1.310506,1.658247,-7.936756,2.055419,8.228544,7.842480,-5.486297,-4.708268,-1.959525,2.503991,-0.844995,9.156497,8.849796,-8.122378,-3.475123,-8.547408,8.464721,-6.515523,-4.093761,-9.442524,-0.103100,-0.066074,8.615249,-1.387909,6.374122,-0.217902,-5.012878,3.733876,-0.589779,-1.701113,1.552279,-5.103277,-3.625897,-2.548678,8.165203,7.864332,4.168771,-8.043168],[-7.621531,-9.393912,-2.785603,-9.351525,-5.135471,-6.527250,9.531522,4.505865,5.736362,6.924755,-3.741066,-2.782548,-0.076662,-0.565305,4.069709,-5.519802,0.886927,0.876941,3.928524,-1.759639,-8.254228,-6.997167,-8.761845,-0.477742,-8.079263,8.704136,-1.767873,-1.917463,0.300508,-0.907119,2.028326,9.240933,9.182943,-3.093469,-8.926727,-3.876159,2.240502,-6.103313,-6.562715,5.457506,3.494789,-9.760915,7.279634,-9.624585,2.101891,6.558280,-6.894800,6.334444,-0.539175,-1.338282,1.375601,0.994280,-1.564696,-9.590829,-2.290794,1.071262,-7.254054,4.137519,-7.347001,4.819461,-0.036392,-5.641400,0.967659,-8.878716,0.554600,-8.222524,3.649485,5.068101,1.937788,1.759890,7.443023,3.176825,-3.925359,6.811915,4.936210,-6.365334,-2.978325,-1.856025,-7.789769,4.534805,2.804117,-1.995516,7.783000,-0.856872,9.641667,-7.033355,-1.283738,8.021295,5.456713,3.207817,7.170572,-9.936991,-5.802556,0.231371,-4.855826,-3.624770,-6.032843,-6.277196,-9.703838,-3.157984,-0.651866,0.372435,5.780742,3.484482,0.986610,9.206494,-1.315713,-4.618107,-3.068205,-6.514166,-6.243973,-1.761263,3.507038,-2.474890,-7.533840,-8.372642,-2.208848,0.480659,-1.652903,-2.581048,-3.236284,-3.671123,5.954505,5.849847,-5.012801,-3.196603,5.146345,2.054513,-6.661025,-6.083765,-5.950869,5.694118,-8.394521,-5.582238,-2.650161,6.201116,-7.528585,0.544853,-3.745262,9.422953,-5.228164,-0.384060,3.207134,1.757613,4.711323,-3.547645,-5.785807,-6.944636,-5.742766,7.736512,1.551533,0.882627,-9.029488,-8.513796,-4.181899,8.170534,8.290500,-0.318564,9.813409,-2.064245,7.413808,-3.163517,7.896461,1.677826,-9.958980,-4.165395,2.212616,5.944086,-7.862369,-5.908051,-9.899188,-2.292173,5.200212,-0.916928,-3.148767,-2.770469,0.451024,1.416420,7.930738,-2.250691,1.046689,-8.441728,2.691804,-8.554799,3.418323,-8.822343,-9.557256,3.906120,8.694436,-2.516209,9.900900,4.598016,4.443535,6.947351,1.675831,-8.566048,-8.670921,1.945832,7.553599,8.954538,8.467757,-3.325381,-4.722645,8.704030,6.767664,8.835399,-7.669578,8.091205,5.341260,1.179105,-5.521315,2.923954,-5.386967,-6.487438,-3.438823,-1.527141,0.624936,0.717667,-2.495913,9.952431,-8.831170,-5.148631,-3.322326,9.227566,-7.856822,-2.660313,-1.414621,0.774583,4.874564,-0.459167,-6.776120,7.706007,4.132995,2.958456,2.143573,9.450873,-9.995941,3.963904,1.768552,-1.993818,0.005681,0.540605,1.441045,-3.551034,-4.500149,-8.039056,9.590871,6.586629,7.880016,-1.019630,1.939928,-3.798584,-3.196905,-5.781529,-7.546577,1.337011,-7.638209,-2.654581,-8.084058,-5.192630,2.885064,0.571944,-2.348364,-4.949779,4.264785,-3.121302,-7.063247,-3.019099,-2.522314,7.368754,-8.885131,-8.712878,2.634760,-3.375902,1.763996,-0.554520,9.257855,3.337857,-9.767919,8.719018,9.638469,7.967534,4.669947,-6.474353,-3.756318,-0.112191,-3.794998,6.541390]], dtype = "float32")#candidate|10068|(4, 288)|const|float32
call_10066 = relay.TupleGetItem(func_2696_call(relay.reshape(var_10067.astype('bool'), [1404,]), relay.reshape(const_10068.astype('float32'), [1152,]), ), 0)
call_10069 = relay.TupleGetItem(func_2699_call(relay.reshape(var_10067.astype('bool'), [1404,]), relay.reshape(const_10068.astype('float32'), [1152,]), ), 0)
output = relay.Tuple([call_10062,call_10066,var_10067,const_10068,])
output2 = relay.Tuple([call_10063,call_10069,var_10067,const_10068,])
func_10072 = relay.Function([var_10067,], output)
mod['func_10072'] = func_10072
mod = relay.transform.InferType()(mod)
var_10073 = relay.var("var_10073", dtype = "bool", shape = (18, 78))#candidate|10073|(18, 78)|var|bool
output = func_10072(var_10073)
func_10074 = relay.Function([var_10073], output)
mutated_mod['func_10074'] = func_10074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7039_call = mod.get_global_var('func_7039')
func_7041_call = mutated_mod.get_global_var('func_7041')
call_10082 = relay.TupleGetItem(func_7039_call(), 1)
call_10083 = relay.TupleGetItem(func_7041_call(), 1)
func_3757_call = mod.get_global_var('func_3757')
func_3761_call = mutated_mod.get_global_var('func_3761')
const_10099 = relay.const(-8, dtype = "int32")#candidate|10099|()|const|int32
const_10100 = relay.const([10,-8,10,-1,-7,1,-5,7,3,5,5,-5,-9,8,-10,5,-4,2,10,-9,8,-8,-9,2,-1,2,-3,8,-2,9,5,3,-6,3,10,-2,-4,-3,7,2,4,-1,3,-9,8,-8,-2,4,7,6,1,-8,-10,7,6,-3,-5,7,6,2,4,8,-10,5,-10,-7,-1,-6,-5,8,2,2,-6,7,5,-7,-9,4,-5,-9,2,-8,2,-5,6,-10,7,-10,-3,6,-6,4,5,-7,8,7,-5,-6,8,-5,7,7,-9,8,1,7,-4,-3,10,-1,-7,10,-3,8,-8,-8,-8,10,9,9,-1,-9,7,5,-1,6,5,7,-2,1,-8,8,3,3,-7,4,-9,2,7,3,-4,-6,-7,-6,10,3,-6,5,-1,1,-3,6,10,-7,-7,-4,3,9,7,-1,5,-6,-6,-2,9,7,-10,1,-2,8,-1,10,4,-4,-7,7,-2,4,-2,-7,10,3,8,2,4,-9,4,-1,-1,9,-1,-1,-9,-2,-3,-4,-4,5,-4,-2,-8,-5,2,-1,10,-10,-6,7,8,-8,10,-8,-10,-8,1,-3,3,-1,4,8,10,7,9,-1,3,9,-3,10,9,10,-8,-9,10,7,-10,10,-1,7,-2,8,-10,-9,-6,-10,6,5,2,-6,3,-8,8,-4,6,-10,2,4,-9,-6,-1,-9,6,-1,-9,-1,-2,-7,9,-1,5,-5,-3,8,1,6,10,-1,9,-5,10,-1,8,-7,1,4,-1,-2,6,-8,-6,1,8,-4,-5,-5,6,-1,6,-1,-6,-3,-2,3,7,-8,-4,10,-2,-10,3,2,-1,-4,-1,-2,-10,3,-1,3,-8,2,-10,5,-7,7,-10,9,-3,6,8,10,6,1,10,7,2,1,4,-4,-2,-10,1,4,2,10,10,7,3,-5,-1,10,-4,7,-8,-6,1,3,-5,8,6,9,-9,-6,-6,7,3,-3,10,-2,9,9,4,-2,8,8,1,4,6,6,8,9,3,-8,-10,-1,8,8,3,-5,-1,9,-2,4,2,10,-3,3,1,-9,2,1,-4,-6,-1,10,-3,6,1,-3,-1,-4,2,-10,-1,-5,1,-6,4,-1,-2,9,-9,3,6,-4,-1,-1,8,-7,2,-1,-7,-7,-9,-6,-9,-8,-9,-10,-9,1,-1,-4,-6,7,4,-1,6,-1,-6,8,3,6,7,8,10,-7,-4,1,1,-7,7,5,6,10,7,9,-4,-4,3,-8,-3,-4,-5,6,1,10,-1,-1,2,-1,9,-9,-7,5,-4,10,7,4,-9,7,-4,-7,-3,4,-2,-4,-4,-6,-5,10,-4,-7,-6,-3,3,-4,7,4,2,5,10,6,10,5,-3,-5,7,9,4,6,-4,-6,2,10,5,-9,-5,-1,5,2,-2,8,-10,-3,-1,-4,9,-7,-10,-6,-2,-2,-8,-2,10,4,3,-1,10,-9,-5,7,5,-5,-1,-1,-6,10,5,-10,7,7,5,-5,4,-6,-1,2,-7,2,-10,2,4,-1,-5,-4,-4,-4,-10,5,-7,2,-6,-3,-1,-2,7,-6,-4,-2,7,-5,8,3,-10,-4,1,-4,-10,9,-3,-4,-3,-3,-7,-9,-2,9,-4,2,3,3,-1,1,6,-7,-1,1,-9,-4,-9,5,7,-5,-6,-7,2,3,8,7,3,3,4,1,-8,2,-8,-3,10,-8,-3,-7,8,8,-3,-10,-10,-4,8,-8,10,6,-8,5,-4,-6,1,-4,5,-4,9,-9,-6,-3,-6,-1,-4,4,-5,-2,3,8,3,-2,-5,9,10,-5,8,-1,3,-3,-10,-1,-10,-5,-2,9,-6,6,-9,7,2,6,-2,-8,-10,1,10,6,-4,-4,-4,4,6,-1,-4,2,10,7,4,6,8,5,-9,9,2,10,6,5,-3,-5,-5,-4,-5,-9,-8,-5,2,6,1,-5,-9,-8,-8,-7,1,9,-8,-5,5,4,-8,-2,10,-2,-5,3,-1,-1,8,-3,9,-7,4,-2,3,-4,4,1,-6,-5,9,7,3,-10,-3,7,4,8,5,1,-5,-1,3,-5,5,3,9,6,5,2,1,-1,3,-7,1,-8,-2,-7,1,7,-1,-1,-8,4,-3,5,-6,-8,-8,-9,2,-5,-6,-1,-4,4,9,-8,10,-4,8,6,-8,3,1,4,9,10,-2,4,-9,1,-4,7,-3,-9,-10,3,3,-1,7,-10,5,-2,10,4,6,9,6,-6,-5,-8,-3,-3,6,-1,-1,9,-8,4,-9,-9,-6,9,-2,-1,-1,6,-3,-10,-2,1,-9,-1,3,7,6,9,4,-5,2,-7,-8,-6,-1,9,-7,-9,3,5,7,-8,-10,8,4,4,1,8,4,10,2,1,10,-6,-9,-8,5,-1,2,2,-3,1,-8,3,5,-9,1,-6,9,-5,-3,7,7,-6,9,5,4,6,-5,6,-10,-6,-5,3,4,-4,-9,6,9,4,-8,10,5,4,2,-9,-6,-5,-7,7,-6,-8,-2,-2,-6,10,7,8,5,9,1,-2,-3,8,-7,1,5,-8,-4,9,9,6,7,-6,-5,2,3,2,2,7,-6,3,-8,10,3,3,-9,6,2,-10,8,-2,-5,8,6,-7,4,6,2,5,5,5,-9,-10,2,-10,2,-3,8,-6,-7,-9,-4,-2,-2,10,-6,-3,-8,10,5,-10,1,5,5,8,-6,-2,3,-7,-2,4,3,-7,-10,-1,-6,-3,-6,-8,2,2,2,-8,-9,-10,1,-3,1,5,6,8,7,-10,-10,2,6,-1,10,-3,-4,2,-9,2,-4,1,1,3,-3,-8,3,6,-6,8,-6,-6,6,-8,2,4,6,-9,7,4,-5,2,4,7,-4,-7,4,9,-1,4,6,3,-3,9,-4,-9,-7,7,8,-5,-7,-1,8,-2,8,4,3,-7,10,6,1,3,6,-1,-5,9,9,-4,3,-5,1,-6,-9,-1,-3,2,-2,-3,-6,5,1,5,3,8,-7,-6,4,-5,8,-1,2,-6,8,-5,4,-10,-3,8,4,3,-8,-2,-4,5,-10,5,-8,8,-8,4,4,-10,9,-6,-5,6,1,-6,-4,9,7,-10,2,-5,-3,-6,-5,4,6,8,-1,7,-6,-7,5,-6,9,-9,4,-3,5,3,-8,3,-9,7,9,1,8,6,3,6,-8,5,1,8,-7,-5,8,-1,10,6,-2,7,-7,3,-4,4,-6,-3,-4,2,-2,8,-4,6,7,-7,10,-10,4,-7,-2,10,9,-2,4,6,-10,7,-5,10,-6,-2,-1,-3,6,3,10,-6,9,-2,4,1,4,8,3,-1,6,-5,-6,2,-6,-1,-2,-5,-5,-6,-7,-10,6,-8,7,8,-5,-2,9,4,-1,-4,-2,-4,8,-5,-8,3,5,5,-5,7,5,-10,5,4,10,1,-8,8,-6,8,8,-1,7,6,8,9,-5,10,4,6,-3,-6,3,-5,-7,-4,-6,-7,-9,-2,-8,-2,1,-5,-7,1,-7,1,10,-8,8,-1,4,-7,3,-2,2,4,-10,-10,-9,9,7,7,-5,-4,6,7,-5,7,-6,7,-4,3,9,3,4,7,1,9,-8,6,10,7,10,1,2,-3,-10,-2,-10,8,-6,-5,8,2,-7,-1,-4,2,2,-1,3,1,-2,2,-8,6,-7,1,-3,1,-1,-8,-3,-10,-6,-1,5,-10,-7,-7,-7,8,-3,9,-2,-7,5,10,8,6,1,10,-9,10,-7,10,-1,-5,-7,-10,5,6,5,-1,-7,4,2,3,6,-7,4,4,6,-2,6,-6,1,2,-9,6,9,6,-6,3,4,-5,-9,-8,10,10,1,-8,9,8,-2,5,-6,3,10,4,-9,-6,9,5,-1,-7,2,-7,-5,10,9,9,4,7,-1,2,1,-8,10,-2,-10,-5,4,3,7,5,9,-1,-7,9,-1,-7,8,5,-9,-3,5,1,-2,-7,8,-4,7,9,8,-3,10,-3,7,10,-6,5,3,-1,10,3,-1,6,6,5,5,5,7,-6,8,10,-9,3,3,-8,-1,3,-9,1,6,9,3,-9,-4,7,-2,-3,-4,-4,2,1,10,7,-5,-7,6,2,-2,4,-7,7,7,-10,-8,-9,-4,-4,-4,-8,-3,10,2,1,-5,9,5,1,6,5,6,2,4,-6,1,7,-8,-3,1,4,8,-7,-9,-7,10,9,-7,5,9,10,-7,3,-4,-6,10,-10,-3,-5,7,-7,7,-2,9,6,3,9,2,7,-8,-10,3,1,7,10,8,-1,-5,9,-4,-3,2,-7,2,2,-7,10,-10,-7,5,-3,5,9,-8,-4,-5,9,7,-4,2,-10,-8,-10,-9,7,2,-8,3,7,-6,-4,-7,10,1,-4,-10,1,-5,8,5,10,5,-6,-7,-2,3,-4,8,-4,-8,9,1,5,8,1,-1,3,-9,6,2,-9,-3,3,8,8,6,-3,-7,4,-4,-1,4,-2,-4,10,-6,9,3,9,-1,-7,-4,5,-9,-7,2,9,-5,-10,7,5,9,3,7,-3,-8,-7,-1,2,-9,-4,-8,-8,1,-1,8,-2,-9,-10,6,7,4,-6,6,6,6,8,-10,-6,4,9,-3,-10,-7,-9,4,9,-9,4,3,-3,-7,-5,-9,7,-10,7,1,-4,-8,3,8,-1,-7,2,-4,-8,-8,-9,6,2,6,9,-7,-6,-5,-4,-1,10,1,-7,-9,-7,8,5,3,9,-9,7,-1,-8,9,9,-8,-7,3,5,9,-10,-9,10,-4,-3,9,-8,2,9,9,-3,-9,7,4,-1,-3,1,-7,6,-2,-4,-7,-3,8,10,10,-6,6,8,-5,-5,1,10,7,-1,5,1,-10,2,-6,5,8,6,5,1,6,-8,-2,-7,6,-9,3,-2,-4,-1,7,-10,-9,8,-2,-4,7,-7,10,-7,2,-7,3,10,-4,-2,10,7,-10,-5,-3,3,1,-8,-4,9,-8,4,6,3,-8,-2,-8,-8,-3,1,2,-8,3,-5,-9,-4,-1,-10,-4,-8,7,1,-8,-4,-3,-8,10,-9,-2,-2,9,9,6,-6,4,5,3,-7,-8,-3,-7,-8,-7,-1,-1,9,1,-9,-9,9,10,-5,3,-5,4,-2,9,9,6,4,-5,9,-2,4,5,5,9,-8,1,-1,-1,7,2,-5,-9,8,-1,9,5,-7,7,6,1,10,9,-10,-4,-10,6,-7,-4,9,1,-3,1,7,-1,6,8,7,-7,10,3,-2,-7,1,3,9,8,-10,-1,9,-1,5,10,9,-8,-1,-10,9,1,1,10,9,3,8,-8,7,9,9,5,-9,8,3,2,-7,3,-8,-9,2,-8,-7,5,-8,-7,8,-6,4,-4,5,-10,8,2,6,-4,-5,-1,1,-6,2,9,-5,6,10,-6,-5,-7,10,10,-1,6,-9,8,-3,-10,-8,-7,-3,-2,-3,7,-9,-5,-6,-6,-1,4,-9,9,-9,-1,9,1,10,-6,6,-3,10,3,-2,4,1,-3,-10,-4,-3,-7,-2,-6,-6,7,8,6,-9,5,-7,-5,6,-7,-2,7,-6,6,5,-2,4,4,9,-3,8,-10,-6,-1,6,-7,1,-2,10,-6,-1,7,-6,-9,-10,5,-10,-5,1,7,6,-6,1,5,-5,6,9,-3,-4,-2,-7,-4,-2,-3,5,-2,7,-1,3,8,8,6,-7,2,3,6,1,-7,9,7,2,-8,-7,-5,-4,10,7,9,9,3,-7,4,-1,2,10,5,-1,1,1,-10,-9,8,10,-9,-1], dtype = "int32")#candidate|10100|(2184,)|const|int32
const_10101 = relay.const([-5,8,7,-7,3,1,6,-4,9,5,8,-5,-3,9,1,3,-8,-2,-3,6,-3,-2,10,-8,-1,9,6,-10,-2,-2,1,-9,-8,-8,1,1,-2,3,-8,-2,-1,10,7,-6,-1,10,-8,2,1,1,5,-6,-2,8,-9,10,-1,9,2,-7,-8,4,-7,3,8,1,-3,-10,-7,6,-1,8,-9,-2,-4,4,9,7,-6,-5,4,10,5,4,-10,-8,9,7,-2,-10,9,8,4,3,6,6,5,5,8,2,2,-1,3,-10,6,-1,8,2,-3,-1,2,-6,3,-7,-3,-9,6,-7,-7,-5,-10,9,-4,-9,-5,-7,-10,-5,6,-6,-8,5,6,-6,10,-7,8,8,6,-10,-8,9,9,10,4,6,2,10,3,2,-5,-4,6,4,9,-2,-10,6,-3,-7,-4,-10,4,4,-6,-3,-5,4,10,3,4,8,-6,-3,3,-7,3,-3,9,-6], dtype = "uint16")#candidate|10101|(180,)|const|uint16
call_10098 = relay.TupleGetItem(func_3757_call(relay.reshape(const_10099.astype('int32'), []), relay.reshape(const_10100.astype('int32'), [13, 14, 12]), relay.reshape(const_10101.astype('uint16'), [180,]), ), 4)
call_10102 = relay.TupleGetItem(func_3761_call(relay.reshape(const_10099.astype('int32'), []), relay.reshape(const_10100.astype('int32'), [13, 14, 12]), relay.reshape(const_10101.astype('uint16'), [180,]), ), 4)
output = relay.Tuple([call_10082,call_10098,const_10099,const_10100,const_10101,])
output2 = relay.Tuple([call_10083,call_10102,const_10099,const_10100,const_10101,])
func_10106 = relay.Function([], output)
mod['func_10106'] = func_10106
mod = relay.transform.InferType()(mod)
mutated_mod['func_10106'] = func_10106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10106_call = mutated_mod.get_global_var('func_10106')
call_10107 = func_10106_call()
output = call_10107
func_10108 = relay.Function([], output)
mutated_mod['func_10108'] = func_10108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5727_call = mod.get_global_var('func_5727')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_10206 = relay.TupleGetItem(func_5727_call(), 0)
call_10207 = relay.TupleGetItem(func_5728_call(), 0)
output = call_10206
output2 = call_10207
func_10216 = relay.Function([], output)
mod['func_10216'] = func_10216
mod = relay.transform.InferType()(mod)
output = func_10216()
func_10217 = relay.Function([], output)
mutated_mod['func_10217'] = func_10217
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10220 = relay.const([[[False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,False],[True,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False],[True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False],[True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False],[True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True],[True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False],[False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False],[False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False],[True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False],[True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False],[False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True],[True,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True],[True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False],[False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False],[False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False],[True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True]],[[True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False],[False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False],[True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True],[True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True],[True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,False],[True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False],[False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True],[False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True],[True,False,False,False,True,True,False,False,True,True,False,False,True,False,True,True],[True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,False],[True,False,True,False,True,True,False,False,False,False,False,True,False,False,False,True],[True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True],[False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True],[False,False,True,False,True,True,True,False,False,False,True,False,True,True,True,True],[False,True,True,False,False,False,False,True,False,True,False,False,False,True,False,True],[False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True]],[[False,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True],[False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True],[False,False,True,False,False,False,False,True,False,False,True,True,True,False,False,True],[True,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True],[True,True,True,True,False,True,True,False,True,False,True,False,True,True,True,False],[True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,True],[False,True,True,False,False,False,False,False,False,True,False,True,False,False,True,False],[True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False],[False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True],[False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True],[False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False],[False,True,False,True,False,True,True,False,True,False,False,True,False,True,False,False],[True,False,True,False,True,True,False,False,False,False,False,False,False,True,True,False],[False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False],[False,True,False,False,False,False,False,False,True,False,True,True,True,False,True,True],[True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False]],[[False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False],[True,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False],[False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,False],[True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False],[True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True],[False,True,False,True,True,False,False,False,True,True,True,True,False,True,True,True],[False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False],[True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False],[False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False],[False,True,True,False,True,False,False,True,True,False,True,True,False,False,True,False],[True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True],[True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False],[False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False],[False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True],[True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True],[True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True]],[[True,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False],[True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False],[True,True,True,False,False,False,False,False,False,False,False,True,False,True,True,True],[False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True],[False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False],[True,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True],[True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False],[True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False],[False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,False],[False,True,False,True,False,True,True,False,True,True,False,False,False,False,False,False],[False,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False],[False,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False],[True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True],[True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False],[False,False,False,False,False,False,True,False,True,True,False,False,False,False,False,True],[False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False]],[[False,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False],[False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False],[True,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True],[True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False],[False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True],[False,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False],[False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,True],[True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True],[True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False],[False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,True],[False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True],[False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True],[False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True],[False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True],[True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False],[True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False]],[[False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True],[True,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True],[True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True],[True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False],[True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True],[False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False],[True,False,False,True,False,True,True,True,True,False,False,True,True,False,False,False],[False,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True],[False,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True],[False,False,False,False,False,True,True,True,True,True,False,True,False,True,False,False],[False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False],[False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,True],[True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False],[True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False],[True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False],[True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False]],[[True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False],[False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False],[True,False,False,False,False,False,False,False,False,False,False,False,False,True,False,True],[True,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True],[False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False],[False,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False],[True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,True],[False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False],[False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False],[True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,True],[False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False],[False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,False],[False,True,True,False,False,False,True,True,False,False,True,True,False,False,False,False],[True,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False],[False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False],[False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False]],[[True,True,True,False,True,True,True,False,False,True,False,False,False,False,False,False],[False,True,False,False,True,True,False,True,False,False,False,False,False,True,False,True],[False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False],[False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True],[False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False],[False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False],[False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False],[True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False],[False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,True],[False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False],[False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,True],[True,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False],[True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True],[True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,False],[False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True],[True,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False]],[[True,False,False,False,True,True,False,True,False,True,True,False,False,False,True,True],[True,True,True,False,True,True,False,True,True,True,True,False,False,False,False,False],[False,False,False,True,False,False,False,False,False,True,False,False,True,True,True,False],[False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False],[False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False],[True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False],[False,True,True,True,True,True,False,True,False,True,True,True,False,True,True,True],[True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,True],[True,True,True,False,False,True,False,False,True,True,False,True,False,True,False,True],[False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,False],[True,False,False,True,True,False,False,False,True,False,True,True,True,False,True,False],[True,True,False,False,False,False,True,True,True,True,False,True,True,True,True,False],[True,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False],[True,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False],[True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True],[True,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False]],[[True,True,False,False,False,False,False,False,False,False,True,False,False,False,True,False],[True,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True],[True,False,True,True,False,True,True,False,True,False,False,False,False,False,False,True],[True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True],[False,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False],[False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False],[True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False],[True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,False],[False,False,False,True,False,True,False,True,True,True,True,True,False,False,False,True],[False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,False],[True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,False],[True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False],[False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True],[False,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False],[True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True],[True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True]],[[True,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True],[True,True,True,False,False,True,False,False,True,False,True,True,False,False,False,True],[True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False],[True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False],[True,False,True,True,False,True,True,False,True,True,True,True,True,False,True,True],[False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False],[False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False],[True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True],[False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True],[True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False],[False,True,False,False,True,False,False,True,True,True,True,True,True,True,False,False],[False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True],[False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False],[False,True,True,False,False,True,False,True,False,False,False,True,True,True,False,False],[False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,False],[False,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False]],[[True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False],[True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True],[False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,True],[False,True,False,True,True,False,False,False,True,True,True,True,False,True,False,False],[True,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False],[False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True],[True,True,True,False,False,True,False,False,False,True,True,False,False,True,False,False],[True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True],[True,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True],[True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True],[False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True],[False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,True],[False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False],[False,True,False,False,True,True,True,True,False,True,False,True,True,True,False,True],[False,True,True,False,True,True,False,True,False,True,True,False,False,False,False,False],[False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,False]],[[True,True,False,False,False,True,True,False,False,True,False,False,True,False,True,True],[False,False,True,True,False,True,True,True,False,False,False,True,True,True,True,False],[False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True],[True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False],[True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False],[False,True,True,True,False,True,False,False,False,False,True,False,True,False,False,True],[False,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True],[True,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True],[True,False,False,False,True,True,False,True,False,False,True,True,False,False,False,True],[True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,True],[False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True],[False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True],[False,True,True,False,False,True,True,False,True,True,True,True,True,False,True,True],[False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False],[True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False],[True,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False]]], dtype = "bool")#candidate|10220|(14, 16, 16)|const|bool
const_10221 = relay.const([[[True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False],[True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,True],[True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,False],[True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False],[True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,True],[False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False],[False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False],[True,False,False,False,True,False,True,False,False,False,False,True,False,False,True,True],[True,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True],[True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,True],[True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True],[False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,True],[False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True],[False,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False],[False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True],[True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True]],[[False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,False],[False,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False],[False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,False],[False,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True],[False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,True],[False,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False],[True,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False],[True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True],[True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,False],[True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False],[True,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False],[False,False,False,False,False,False,False,True,True,False,False,False,False,False,True,True],[False,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True],[True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True],[False,False,False,True,True,True,True,True,True,True,False,False,False,False,True,True],[True,False,False,True,True,False,False,True,False,True,False,False,False,True,True,False]],[[True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False],[True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False],[True,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True],[True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False],[True,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False],[True,True,False,True,False,False,True,True,False,True,True,False,False,True,False,True],[True,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False],[True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False],[False,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False],[False,False,True,False,False,False,True,False,True,False,True,False,False,True,False,False],[False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False],[True,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False],[False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,False],[True,False,False,True,False,False,True,True,True,False,False,True,False,False,True,False],[False,True,True,True,False,True,True,False,False,False,True,True,False,False,False,True],[False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True]],[[False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False],[True,False,True,True,False,True,False,True,True,False,True,False,True,False,True,False],[False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False],[False,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True],[True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True],[True,False,False,True,True,False,True,False,False,False,False,True,True,True,True,False],[False,False,False,False,False,True,True,False,False,False,True,True,False,False,False,False],[False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True],[False,True,True,False,False,True,False,False,True,True,True,True,True,True,True,True],[False,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False],[False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,True],[True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True],[True,False,True,False,True,True,True,False,False,False,True,False,True,False,True,False],[False,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True],[False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,True],[True,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True]],[[True,False,False,False,False,False,True,True,False,False,True,True,True,False,False,True],[False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True],[False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False],[False,False,True,True,False,False,False,False,True,False,False,True,False,True,False,True],[False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True],[True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True],[False,False,True,True,True,True,True,True,True,False,False,False,True,False,False,False],[False,False,True,True,True,True,False,False,True,True,False,False,True,False,False,True],[True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,False],[True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,False],[False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True],[True,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False],[True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False],[True,False,False,False,True,True,True,False,True,True,True,False,False,True,False,True],[True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,True],[False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True]],[[True,True,False,False,True,False,False,True,False,True,True,False,False,True,True,False],[True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,True],[False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False],[False,True,True,False,False,False,False,False,True,False,False,True,True,True,False,False],[False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,False],[False,True,False,False,True,False,True,False,False,True,True,True,True,False,True,True],[False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False],[True,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True],[False,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True],[False,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True],[True,True,False,True,True,True,True,True,False,True,False,True,True,False,False,True],[False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True],[False,False,False,True,True,True,False,True,False,True,True,True,True,True,False,True],[False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True],[False,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False],[True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True]],[[False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False],[False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True],[True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True],[True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,False],[True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False],[False,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True],[True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,True],[False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False],[False,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True],[False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False],[True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,True],[False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,False],[False,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False],[False,False,False,False,False,True,True,False,True,True,True,False,False,True,False,False],[False,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True],[False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True]],[[True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False],[False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True],[False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True],[True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False],[True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False],[False,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False],[False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True],[True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True],[False,True,False,False,False,True,False,False,True,True,True,False,True,False,True,False],[False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True],[False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,False],[False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True],[False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,False],[False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True],[True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True],[False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,False]],[[True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False],[False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False],[False,False,True,False,False,True,True,True,False,True,True,False,True,False,True,True],[True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True],[False,False,True,False,True,True,True,True,False,True,False,True,True,True,False,True],[True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False],[False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True],[False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,False],[True,False,False,False,False,False,True,True,True,True,False,False,False,True,True,False],[False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False],[False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,False],[True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False],[True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True],[False,False,False,False,False,True,True,True,True,False,False,False,False,True,False,True],[True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False],[True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,True]],[[True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True],[False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False],[False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,True],[True,False,True,False,True,True,False,False,True,True,False,False,False,False,False,False],[False,False,False,False,True,True,False,False,True,False,False,False,False,False,True,False],[False,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False],[False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False],[True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True],[True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False],[True,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True],[True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True],[False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True],[True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True],[True,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False],[True,True,True,False,False,True,False,True,False,True,True,True,False,False,False,False],[False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,True]],[[True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False],[True,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True],[True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False],[True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True],[True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False],[True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False],[True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,True],[False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False],[True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False],[False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False],[False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True],[False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,True],[False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True],[True,True,False,False,False,True,False,True,False,False,False,True,True,False,True,True],[True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False],[True,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False]],[[True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False],[True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True],[False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True],[True,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True],[True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,True],[True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,True],[True,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False],[True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False],[True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False],[False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,False],[True,False,False,True,True,True,True,False,True,True,False,False,True,True,False,True],[True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False],[True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True],[True,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False],[False,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False],[False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False]],[[True,False,False,False,False,True,True,False,True,True,False,False,True,True,True,True],[True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False],[True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,False],[True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False],[True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,True],[False,True,False,False,False,False,True,False,False,False,True,True,False,True,True,True],[False,True,False,True,False,True,True,False,False,True,False,False,True,False,True,True],[True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,False],[False,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False],[False,True,True,False,False,True,True,True,False,True,False,True,False,False,True,True],[False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True],[True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False],[False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False],[True,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False],[False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False],[False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False]],[[False,False,True,True,False,True,False,False,False,False,True,True,True,False,True,True],[True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True],[False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True],[True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True],[True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True],[True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,False],[True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,False],[False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False],[False,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True],[True,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True],[False,True,True,False,False,False,False,True,False,True,True,False,False,True,True,False],[False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True],[False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,True],[False,False,False,False,False,False,True,True,False,False,False,True,True,False,False,True],[True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,False],[True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False]]], dtype = "bool")#candidate|10221|(14, 16, 16)|const|bool
bop_10222 = relay.logical_or(const_10220.astype('bool'), relay.reshape(const_10221.astype('bool'), relay.shape_of(const_10220))) # shape=(14, 16, 16)
var_10236 = relay.var("var_10236", dtype = "bool", shape = (14, 16, 16))#candidate|10236|(14, 16, 16)|var|bool
bop_10237 = relay.right_shift(const_10221.astype('uint8'), relay.reshape(var_10236.astype('uint8'), relay.shape_of(const_10221))) # shape=(14, 16, 16)
uop_10244 = relay.tan(bop_10222.astype('float32')) # shape=(14, 16, 16)
func_10054_call = mod.get_global_var('func_10054')
func_10057_call = mutated_mod.get_global_var('func_10057')
var_10261 = relay.var("var_10261", dtype = "bool", shape = (1, 490))#candidate|10261|(1, 490)|var|bool
call_10260 = relay.TupleGetItem(func_10054_call(relay.reshape(var_10261.astype('bool'), [490,])), 5)
call_10262 = relay.TupleGetItem(func_10057_call(relay.reshape(var_10261.astype('bool'), [490,])), 5)
uop_10263 = relay.erf(const_10220.astype('float64')) # shape=(14, 16, 16)
func_1120_call = mod.get_global_var('func_1120')
func_1125_call = mutated_mod.get_global_var('func_1125')
const_10270 = relay.const([-2.787754,-2.020573,4.675870,2.478887,5.649508,-0.792812,-4.510567,6.890367,7.665506,-3.753069,8.740837,-7.918746,-5.867104,8.691789,6.837705,6.759577,-4.197552,4.357274,-3.808436,-0.167234,4.196793,-1.459063,-1.693184,9.057527,-8.014033,-6.847802,9.083186,2.111145,6.277925,-5.652345,1.595808,-6.055837,0.879928,-1.772670,1.721843,1.318492,3.529853,-2.383803,-9.386508,9.532853,-9.474034,-3.847966,9.775914,3.022301,-6.498487,0.395241,1.595249,4.386705,7.255919,-6.521921,-9.113564,4.397219,4.999901,4.897375,7.005131,-0.871712,-7.832320,-9.953507,2.907621,6.895344,8.165516,3.477961,-5.632023,8.042372,-8.009452,-5.832927,6.633701,0.261020,-3.209758,-3.374672,6.253733,9.228753,9.099170,7.337494,8.248799,4.749814,7.013367,2.239065,6.840577,5.727123,4.884656,5.877557,0.153025,6.079263,4.740063,-0.556702,1.772438,8.162472,4.212197,4.711909,7.154512,7.948602,5.745961,-4.772933,1.487814,1.039532,-0.656475,4.421440,4.334356,1.447021,0.165706,5.639215,7.892788,5.321899,-9.580479,5.291663,4.882147,-4.096170,9.529530,-9.018342,3.116062,7.280898,-2.133576,5.662410,-4.957811,-3.938555,-8.920165,-8.713971,-3.653029,-8.725312,-2.551531,-1.746266,-8.867617,-7.829013,-2.033734,-0.421458,-9.156638,6.988602,5.448439,-8.928620,7.939634,4.932816,6.813954,3.845101,5.887029], dtype = "float32")#candidate|10270|(135,)|const|float32
const_10271 = relay.const([9,7,-10,6,9,8,3,-6,4,-2,-5,7,6,-9,10,1,10,1,-8,5,-5,3,-4,4,5,6,6,8,-1,9,7,-3,10,6,-5,7,3,-7,-1,6,-9,-5,-6,-1,8,-2,-9,-1,-3,7,5,7,8,-6,6,-4,-6,2,-10,3,-2,-4,-2,-10,-9,2,-4,3,-2,8,2,-3,-1,-2,-9,-10,10,3,-6,-8,1,8,-10,7,9,-1,9,1,10,-2,8,1,-5,-3,-9,-9,-2,8,-7,5,-10,9,10,-7,3,1,-3,-1,-9,3,-5,8,9,-1,-1,-4,-3,-8,5,5,-7,9,-9,10,5,5,6,-9,-9,1,9,1,-2,-4,8,-5,4,-7,-8,-2,-2,5,10,1,6,-1,1,6,-3,-10,-8,8,-3,-8,3,6,-4,-3,6,-4,-10,-9,9,4,-6,6,3,9,-10,9,-4,1,5,-4,10,5,-5,10,-10,7], dtype = "uint16")#candidate|10271|(180,)|const|uint16
call_10269 = relay.TupleGetItem(func_1120_call(relay.reshape(const_10270.astype('float32'), [9, 1, 15]), relay.reshape(call_10260.astype('float32'), [1152,]), relay.reshape(const_10271.astype('uint16'), [180, 1]), ), 1)
call_10272 = relay.TupleGetItem(func_1125_call(relay.reshape(const_10270.astype('float32'), [9, 1, 15]), relay.reshape(call_10260.astype('float32'), [1152,]), relay.reshape(const_10271.astype('uint16'), [180, 1]), ), 1)
func_5298_call = mod.get_global_var('func_5298')
func_5300_call = mutated_mod.get_global_var('func_5300')
call_10273 = relay.TupleGetItem(func_5298_call(), 0)
call_10274 = relay.TupleGetItem(func_5300_call(), 0)
func_7881_call = mod.get_global_var('func_7881')
func_7882_call = mutated_mod.get_global_var('func_7882')
call_10286 = func_7881_call()
call_10287 = func_7881_call()
output = relay.Tuple([bop_10237,uop_10244,call_10260,var_10261,uop_10263,call_10269,const_10270,const_10271,call_10273,call_10286,])
output2 = relay.Tuple([bop_10237,uop_10244,call_10262,var_10261,uop_10263,call_10272,const_10270,const_10271,call_10274,call_10287,])
func_10300 = relay.Function([var_10236,var_10261,], output)
mod['func_10300'] = func_10300
mod = relay.transform.InferType()(mod)
mutated_mod['func_10300'] = func_10300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10300_call = mutated_mod.get_global_var('func_10300')
var_10302 = relay.var("var_10302", dtype = "bool", shape = (14, 16, 16))#candidate|10302|(14, 16, 16)|var|bool
var_10303 = relay.var("var_10303", dtype = "bool", shape = (1, 490))#candidate|10303|(1, 490)|var|bool
call_10301 = func_10300_call(var_10302,var_10303,)
output = call_10301
func_10304 = relay.Function([var_10302,var_10303,], output)
mutated_mod['func_10304'] = func_10304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8756_call = mod.get_global_var('func_8756')
func_8757_call = mutated_mod.get_global_var('func_8757')
call_10359 = func_8756_call()
call_10360 = func_8756_call()
func_7799_call = mod.get_global_var('func_7799')
func_7801_call = mutated_mod.get_global_var('func_7801')
call_10363 = relay.TupleGetItem(func_7799_call(), 0)
call_10364 = relay.TupleGetItem(func_7801_call(), 0)
output = relay.Tuple([call_10359,call_10363,])
output2 = relay.Tuple([call_10360,call_10364,])
func_10373 = relay.Function([], output)
mod['func_10373'] = func_10373
mod = relay.transform.InferType()(mod)
output = func_10373()
func_10374 = relay.Function([], output)
mutated_mod['func_10374'] = func_10374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9506_call = mod.get_global_var('func_9506')
func_9508_call = mutated_mod.get_global_var('func_9508')
call_10389 = relay.TupleGetItem(func_9506_call(), 0)
call_10390 = relay.TupleGetItem(func_9508_call(), 0)
output = call_10389
output2 = call_10390
func_10403 = relay.Function([], output)
mod['func_10403'] = func_10403
mod = relay.transform.InferType()(mod)
mutated_mod['func_10403'] = func_10403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10403_call = mutated_mod.get_global_var('func_10403')
call_10404 = func_10403_call()
output = call_10404
func_10405 = relay.Function([], output)
mutated_mod['func_10405'] = func_10405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10416 = relay.var("var_10416", dtype = "int32", shape = (5, 12, 8))#candidate|10416|(5, 12, 8)|var|int32
const_10417 = relay.const([[[-1,-6,-5,-10,-4,8,-5,7],[-2,-1,8,6,2,-9,-4,-2],[-1,1,-7,-4,1,8,3,-5],[-8,5,-4,-3,6,3,-6,-5],[5,-2,1,5,10,-8,-9,-7],[7,2,-3,-10,-10,1,1,-2],[3,1,1,-4,9,5,4,4],[6,-7,-2,9,1,7,-5,-10],[-4,2,7,10,1,6,1,-9],[8,7,-2,-2,-6,6,-10,2],[7,3,4,-4,1,10,-9,-1],[6,9,-6,-2,-9,-8,5,5]],[[7,-8,1,6,1,6,-9,-9],[6,-3,-8,-7,-3,8,-6,-2],[10,4,3,5,-7,5,7,1],[1,-6,-8,6,9,-3,-4,5],[-6,-7,-8,4,3,-3,3,-6],[9,1,-6,-1,10,9,1,-10],[-5,-8,9,-10,1,-5,-9,-7],[6,6,-7,-8,-10,-1,-2,-10],[9,-10,9,-3,7,-3,10,5],[-9,7,-9,-1,3,-2,4,-10],[9,1,3,-8,-3,-7,2,10],[-4,-5,3,3,-9,-1,-6,-6]],[[-2,-3,-1,3,2,7,-1,-3],[-4,-7,-6,3,5,8,6,6],[-1,2,10,5,7,-5,-1,-5],[-9,-3,3,10,-1,-9,2,-2],[-4,6,2,-5,-3,7,-9,10],[5,4,-9,-5,-5,-7,2,2],[6,10,-7,-6,5,6,-6,-3],[10,-8,-4,-9,-1,-5,-8,9],[-3,1,-3,-4,-10,4,7,-6],[7,-5,-1,9,3,-5,1,4],[-4,-5,9,7,2,-5,3,7],[9,2,-8,-4,-4,-3,-4,10]],[[9,-6,7,-10,-9,9,10,5],[-7,1,-7,-8,5,-8,8,8],[-5,8,10,-2,-6,-2,-4,6],[-3,7,-4,-4,6,-10,2,-2],[4,9,-1,-4,4,1,-2,-1],[6,4,-5,-2,10,5,-2,9],[10,-10,10,8,-10,2,-8,5],[-3,5,-7,8,9,-9,4,-6],[7,5,-10,3,-2,1,10,-3],[7,10,6,-3,-3,7,2,10],[-1,-1,8,2,1,-9,1,3],[-1,-4,-2,6,-1,1,-6,5]],[[7,-10,-9,6,-6,-10,-6,-7],[-7,8,7,-3,4,-2,-6,-10],[2,-8,10,9,-9,-5,2,-4],[2,-8,-3,-7,-4,9,-3,-1],[-7,-6,-4,-5,3,-8,1,-6],[3,3,-5,-4,7,-9,2,-7],[-10,6,-7,-7,-10,-7,-8,-5],[9,10,6,2,-7,8,-2,8],[8,-6,-6,7,-1,-8,-1,3],[-1,-3,6,4,8,-3,-7,-2],[7,-1,-4,-9,-7,5,10,-8],[-10,-9,10,-10,-5,9,-5,8]]], dtype = "int32")#candidate|10417|(5, 12, 8)|const|int32
bop_10418 = relay.subtract(var_10416.astype('int32'), relay.reshape(const_10417.astype('int32'), relay.shape_of(var_10416))) # shape=(5, 12, 8)
output = bop_10418
output2 = bop_10418
func_10423 = relay.Function([var_10416,], output)
mod['func_10423'] = func_10423
mod = relay.transform.InferType()(mod)
var_10424 = relay.var("var_10424", dtype = "int32", shape = (5, 12, 8))#candidate|10424|(5, 12, 8)|var|int32
output = func_10423(var_10424)
func_10425 = relay.Function([var_10424], output)
mutated_mod['func_10425'] = func_10425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6068_call = mod.get_global_var('func_6068')
func_6069_call = mutated_mod.get_global_var('func_6069')
call_10427 = relay.TupleGetItem(func_6068_call(), 0)
call_10428 = relay.TupleGetItem(func_6069_call(), 0)
output = relay.Tuple([call_10427,])
output2 = relay.Tuple([call_10428,])
func_10429 = relay.Function([], output)
mod['func_10429'] = func_10429
mod = relay.transform.InferType()(mod)
mutated_mod['func_10429'] = func_10429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10429_call = mutated_mod.get_global_var('func_10429')
call_10430 = func_10429_call()
output = call_10430
func_10431 = relay.Function([], output)
mutated_mod['func_10431'] = func_10431
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10452 = relay.const([[[-3,-10,-5,-3,10,-7,4,10,-4,-6,7,1,7],[4,6,-1,-2,-5,10,3,-2,8,-2,10,9,-3],[9,-4,-5,2,6,2,4,6,-3,-6,9,-1,-4],[7,6,10,5,4,2,1,9,7,-1,7,-2,-1],[9,-2,-4,4,10,-5,-10,4,5,2,-1,7,-2],[7,9,4,1,-1,-6,7,3,-4,-1,2,6,-9]],[[-3,-10,-3,8,7,2,-8,5,9,4,5,4,-6],[3,-10,-8,1,7,-7,5,-7,-3,9,-10,1,-2],[-10,2,3,-8,10,-10,-6,-4,-2,-8,-6,-5,-3],[7,7,-10,-6,-2,10,5,-6,2,2,6,6,4],[-8,-9,3,7,-5,-8,-3,-1,-10,4,1,-1,-1],[8,2,-9,10,3,4,-5,7,2,-4,5,-9,-2]],[[-3,3,10,1,-5,4,10,9,7,7,-7,-6,-1],[-5,-7,3,1,-6,-9,-5,-1,10,-6,9,2,9],[-2,10,-5,-6,-3,-4,6,5,1,8,1,-5,-6],[2,8,-7,6,8,2,4,2,10,-2,-3,-9,4],[10,6,-2,6,-8,2,2,-5,-3,-2,1,-5,10],[-3,-1,-6,-6,7,-1,-8,7,4,2,-6,10,-2]],[[-1,-1,4,-10,3,-4,-10,-7,-5,9,6,5,-3],[-3,-10,-4,-3,-4,1,10,1,2,-8,-2,3,8],[5,9,4,-10,8,-5,-1,6,4,7,-3,-7,-10],[-5,-2,-6,6,-4,-7,3,2,-6,9,-6,-9,8],[-4,4,-6,10,-4,7,-10,-8,-7,2,-1,2,-2],[2,-1,-5,7,-2,-10,3,9,-4,10,7,3,9]],[[-10,5,-9,-3,-7,-7,10,9,4,-4,1,3,9],[1,9,-7,8,1,9,8,-2,10,6,2,3,-2],[-3,6,-5,6,-4,3,7,1,-7,1,8,1,-3],[6,8,-10,3,5,-2,3,5,2,-1,-9,-4,10],[-4,-7,-4,2,-1,3,8,-3,8,-8,4,-7,3],[-5,-8,8,-6,8,-8,-1,3,-4,-3,-3,4,6]],[[-1,5,10,-2,5,-10,-5,-2,-9,3,-9,4,5],[-5,-1,7,7,-6,3,7,8,-10,6,-7,9,8],[8,-1,1,9,8,-4,1,-2,-7,-2,-8,1,8],[-8,9,-4,10,-7,-1,5,-6,4,8,-10,7,-2],[-8,-9,-1,3,5,-5,3,7,10,-3,10,4,5],[3,-7,9,5,4,-4,-6,-4,-5,-4,-1,4,-3]],[[-3,-2,-10,-2,-7,-4,8,-2,5,-3,-10,-6,-1],[-1,2,9,8,6,6,4,-7,-8,8,-7,-8,2],[9,4,-8,6,10,7,-7,-7,9,8,2,2,8],[1,-2,-5,4,10,6,-1,-3,6,1,5,-5,-7],[9,-4,-1,-4,-1,-1,-10,-6,8,5,-8,-3,2],[-1,1,3,9,6,2,10,-10,-8,-5,9,4,7]],[[2,-2,-8,-3,-3,6,4,10,5,-9,3,5,4],[3,5,1,-8,6,-8,-4,5,-2,3,5,6,-2],[5,-6,9,-6,-9,-4,2,4,8,2,7,4,-10],[9,5,4,9,9,-1,-4,4,1,9,9,-3,-3],[-6,2,6,-3,-3,10,-1,9,4,4,3,-5,3],[2,-6,6,-3,-10,-10,-1,4,-4,-10,6,-6,3]],[[10,-4,3,-6,-2,-1,-3,-6,-7,-5,-8,-5,3],[4,4,1,-5,-6,2,7,6,-10,2,1,5,-10],[6,3,9,-9,5,6,6,8,3,1,-5,8,9],[7,-5,8,4,-1,9,5,-9,-3,4,2,-7,9],[-3,9,4,5,5,-3,5,2,-3,9,10,8,3],[3,2,-2,-9,-9,7,4,-7,10,10,-9,1,-6]],[[10,-6,3,-3,-3,4,-3,7,-6,3,10,7,-7],[5,-4,10,-7,7,8,-9,-2,-1,3,-9,10,2],[5,-10,-6,4,-7,4,-1,-6,-8,9,5,8,-9],[6,-9,7,-8,8,-3,-1,-9,4,3,-8,-2,-4],[-9,4,-9,5,-9,-2,9,-8,-4,-5,-6,-2,9],[-2,9,2,8,3,-6,-3,-9,1,-5,-4,-2,2]],[[8,-6,4,-1,-4,10,-9,-9,-9,2,-7,8,6],[3,-1,-3,-10,7,9,-8,1,6,9,6,8,-8],[5,-9,7,8,-8,8,-1,4,3,2,-8,-5,-4],[4,1,8,-7,-8,10,4,-8,-8,7,1,-1,-5],[3,-5,3,8,-1,-1,-5,7,-4,7,-3,-2,-8],[4,8,-10,1,8,7,9,4,10,-8,7,8,-5]]], dtype = "int32")#candidate|10452|(11, 6, 13)|const|int32
var_10453 = relay.var("var_10453", dtype = "int32", shape = (11, 6, 13))#candidate|10453|(11, 6, 13)|var|int32
bop_10454 = relay.right_shift(const_10452.astype('int32'), relay.reshape(var_10453.astype('int32'), relay.shape_of(const_10452))) # shape=(11, 6, 13)
output = relay.Tuple([bop_10454,])
output2 = relay.Tuple([bop_10454,])
func_10466 = relay.Function([var_10453,], output)
mod['func_10466'] = func_10466
mod = relay.transform.InferType()(mod)
mutated_mod['func_10466'] = func_10466
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10467 = relay.var("var_10467", dtype = "int32", shape = (11, 6, 13))#candidate|10467|(11, 6, 13)|var|int32
func_10466_call = mutated_mod.get_global_var('func_10466')
call_10468 = func_10466_call(var_10467)
output = call_10468
func_10469 = relay.Function([var_10467], output)
mutated_mod['func_10469'] = func_10469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2883_call = mod.get_global_var('func_2883')
func_2884_call = mutated_mod.get_global_var('func_2884')
call_10478 = relay.TupleGetItem(func_2883_call(), 0)
call_10479 = relay.TupleGetItem(func_2884_call(), 0)
func_9208_call = mod.get_global_var('func_9208')
func_9209_call = mutated_mod.get_global_var('func_9209')
call_10519 = func_9208_call()
call_10520 = func_9208_call()
func_7771_call = mod.get_global_var('func_7771')
func_7772_call = mutated_mod.get_global_var('func_7772')
call_10526 = func_7771_call()
call_10527 = func_7771_call()
output = relay.Tuple([call_10478,call_10519,call_10526,])
output2 = relay.Tuple([call_10479,call_10520,call_10527,])
func_10529 = relay.Function([], output)
mod['func_10529'] = func_10529
mod = relay.transform.InferType()(mod)
mutated_mod['func_10529'] = func_10529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10529_call = mutated_mod.get_global_var('func_10529')
call_10530 = func_10529_call()
output = call_10530
func_10531 = relay.Function([], output)
mutated_mod['func_10531'] = func_10531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_10609 = relay.TupleGetItem(func_4699_call(), 1)
call_10610 = relay.TupleGetItem(func_4701_call(), 1)
output = call_10609
output2 = call_10610
func_10613 = relay.Function([], output)
mod['func_10613'] = func_10613
mod = relay.transform.InferType()(mod)
output = func_10613()
func_10614 = relay.Function([], output)
mutated_mod['func_10614'] = func_10614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4291_call = mod.get_global_var('func_4291')
func_4293_call = mutated_mod.get_global_var('func_4293')
call_10648 = relay.TupleGetItem(func_4291_call(), 0)
call_10649 = relay.TupleGetItem(func_4293_call(), 0)
uop_10651 = relay.cos(call_10648.astype('float32')) # shape=(180,)
uop_10653 = relay.cos(call_10649.astype('float32')) # shape=(180,)
output = uop_10651
output2 = uop_10653
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
