import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_19 = relay.var("var_19", dtype = "uint8", shape = (12, 12, 2))#candidate|19|(12, 12, 2)|var|uint8
var_20 = relay.var("var_20", dtype = "uint8", shape = (12, 12, 2))#candidate|20|(12, 12, 2)|var|uint8
bop_21 = relay.bitwise_and(var_19.astype('uint8'), relay.reshape(var_20.astype('uint8'), relay.shape_of(var_19))) # shape=(12, 12, 2)
output = relay.Tuple([bop_21,])
output2 = relay.Tuple([bop_21,])
func_33 = relay.Function([var_19,var_20,], output)
mod['func_33'] = func_33
mod = relay.transform.InferType()(mod)
mutated_mod['func_33'] = func_33
mutated_mod = relay.transform.InferType()(mutated_mod)
func_33_call = mutated_mod.get_global_var('func_33')
var_35 = relay.var("var_35", dtype = "uint8", shape = (12, 12, 2))#candidate|35|(12, 12, 2)|var|uint8
var_36 = relay.var("var_36", dtype = "uint8", shape = (12, 12, 2))#candidate|36|(12, 12, 2)|var|uint8
call_34 = func_33_call(var_35,var_36,)
output = call_34
func_37 = relay.Function([var_35,var_36,], output)
mutated_mod['func_37'] = func_37
mutated_mod = relay.transform.InferType()(mutated_mod)
var_72 = relay.var("var_72", dtype = "float32", shape = (4, 4, 5))#candidate|72|(4, 4, 5)|var|float32
uop_73 = relay.cosh(var_72.astype('float32')) # shape=(4, 4, 5)
func_33_call = mod.get_global_var('func_33')
func_37_call = mutated_mod.get_global_var('func_37')
var_85 = relay.var("var_85", dtype = "uint8", shape = (288,))#candidate|85|(288,)|var|uint8
call_84 = relay.TupleGetItem(func_33_call(relay.reshape(var_85.astype('uint8'), [12, 12, 2]), relay.reshape(var_85.astype('uint8'), [12, 12, 2]), ), 0)
call_86 = relay.TupleGetItem(func_37_call(relay.reshape(var_85.astype('uint8'), [12, 12, 2]), relay.reshape(var_85.astype('uint8'), [12, 12, 2]), ), 0)
uop_87 = relay.acos(uop_73.astype('float32')) # shape=(4, 4, 5)
func_33_call = mod.get_global_var('func_33')
func_37_call = mutated_mod.get_global_var('func_37')
call_106 = relay.TupleGetItem(func_33_call(relay.reshape(var_85.astype('uint8'), [12, 12, 2]), relay.reshape(var_85.astype('uint8'), [12, 12, 2]), ), 0)
call_107 = relay.TupleGetItem(func_37_call(relay.reshape(var_85.astype('uint8'), [12, 12, 2]), relay.reshape(var_85.astype('uint8'), [12, 12, 2]), ), 0)
output = relay.Tuple([call_84,var_85,uop_87,call_106,])
output2 = relay.Tuple([call_86,var_85,uop_87,call_107,])
func_110 = relay.Function([var_72,var_85,], output)
mod['func_110'] = func_110
mod = relay.transform.InferType()(mod)
var_111 = relay.var("var_111", dtype = "float32", shape = (4, 4, 5))#candidate|111|(4, 4, 5)|var|float32
var_112 = relay.var("var_112", dtype = "uint8", shape = (288,))#candidate|112|(288,)|var|uint8
output = func_110(var_111,var_112,)
func_113 = relay.Function([var_111,var_112,], output)
mutated_mod['func_113'] = func_113
mutated_mod = relay.transform.InferType()(mutated_mod)
var_147 = relay.var("var_147", dtype = "float32", shape = (10, 14, 11))#candidate|147|(10, 14, 11)|var|float32
var_148 = relay.var("var_148", dtype = "float32", shape = (10, 14, 11))#candidate|148|(10, 14, 11)|var|float32
bop_149 = relay.floor_mod(var_147.astype('float32'), relay.reshape(var_148.astype('float32'), relay.shape_of(var_147))) # shape=(10, 14, 11)
output = bop_149
output2 = bop_149
func_164 = relay.Function([var_147,var_148,], output)
mod['func_164'] = func_164
mod = relay.transform.InferType()(mod)
mutated_mod['func_164'] = func_164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_164_call = mutated_mod.get_global_var('func_164')
var_166 = relay.var("var_166", dtype = "float32", shape = (10, 14, 11))#candidate|166|(10, 14, 11)|var|float32
var_167 = relay.var("var_167", dtype = "float32", shape = (10, 14, 11))#candidate|167|(10, 14, 11)|var|float32
call_165 = func_164_call(var_166,var_167,)
output = call_165
func_168 = relay.Function([var_166,var_167,], output)
mutated_mod['func_168'] = func_168
mutated_mod = relay.transform.InferType()(mutated_mod)
const_170 = relay.const([[[7.440556],[1.279231],[8.903746],[-8.952502],[-3.449658],[-1.985879],[-3.777412],[-9.770516],[4.190610]],[[-3.175060],[2.214252],[-2.645518],[3.457654],[7.084877],[9.016367],[-4.989886],[-4.540927],[9.295387]],[[-8.571692],[5.021698],[-5.802683],[-6.301203],[-6.474316],[-8.914158],[2.863596],[1.300993],[-0.450470]],[[-0.914750],[0.805077],[-0.360120],[-9.007065],[-9.835930],[-3.765543],[-0.432844],[6.621000],[6.325255]]], dtype = "float32")#candidate|170|(4, 9, 1)|const|float32
uop_171 = relay.asin(const_170.astype('float32')) # shape=(4, 9, 1)
output = uop_171
output2 = uop_171
func_194 = relay.Function([], output)
mod['func_194'] = func_194
mod = relay.transform.InferType()(mod)
output = func_194()
func_195 = relay.Function([], output)
mutated_mod['func_195'] = func_195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_238 = func_194_call()
call_239 = func_194_call()
var_242 = relay.var("var_242", dtype = "float32", shape = (4, 9, 11))#candidate|242|(4, 9, 11)|var|float32
bop_243 = relay.bitwise_and(call_238.astype('int8'), var_242.astype('int8')) # shape=(4, 9, 11)
bop_246 = relay.bitwise_and(call_239.astype('int8'), var_242.astype('int8')) # shape=(4, 9, 11)
uop_259 = relay.sinh(var_242.astype('float32')) # shape=(4, 9, 11)
output = relay.Tuple([bop_243,uop_259,])
output2 = relay.Tuple([bop_246,uop_259,])
func_280 = relay.Function([var_242,], output)
mod['func_280'] = func_280
mod = relay.transform.InferType()(mod)
var_281 = relay.var("var_281", dtype = "float32", shape = (4, 9, 11))#candidate|281|(4, 9, 11)|var|float32
output = func_280(var_281)
func_282 = relay.Function([var_281], output)
mutated_mod['func_282'] = func_282
mutated_mod = relay.transform.InferType()(mutated_mod)
var_307 = relay.var("var_307", dtype = "float64", shape = ())#candidate|307|()|var|float64
var_308 = relay.var("var_308", dtype = "float64", shape = (1, 14))#candidate|308|(1, 14)|var|float64
bop_309 = relay.less_equal(var_307.astype('bool'), var_308.astype('bool')) # shape=(1, 14)
output = bop_309
output2 = bop_309
func_313 = relay.Function([var_307,var_308,], output)
mod['func_313'] = func_313
mod = relay.transform.InferType()(mod)
var_314 = relay.var("var_314", dtype = "float64", shape = ())#candidate|314|()|var|float64
var_315 = relay.var("var_315", dtype = "float64", shape = (1, 14))#candidate|315|(1, 14)|var|float64
output = func_313(var_314,var_315,)
func_316 = relay.Function([var_314,var_315,], output)
mutated_mod['func_316'] = func_316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_371 = func_194_call()
call_372 = func_194_call()
func_164_call = mod.get_global_var('func_164')
func_168_call = mutated_mod.get_global_var('func_168')
var_374 = relay.var("var_374", dtype = "float32", shape = (154, 10))#candidate|374|(154, 10)|var|float32
call_373 = func_164_call(relay.reshape(var_374.astype('float32'), [10, 14, 11]), relay.reshape(var_374.astype('float32'), [10, 14, 11]), )
call_375 = func_164_call(relay.reshape(var_374.astype('float32'), [10, 14, 11]), relay.reshape(var_374.astype('float32'), [10, 14, 11]), )
func_33_call = mod.get_global_var('func_33')
func_37_call = mutated_mod.get_global_var('func_37')
const_379 = relay.const([[-10,-6,9,8,-9,4,3,-4,4,-3,10,-4,5,4,5,-1,-5,5,-7,7,-2,-3,10,-10,-5,-3,-8,-7,-2,-8,-6,-1,-8,-3,1,-2,-1,-2,4,-7,4,3,6,3,-2,-4,4,9,2,-8,2,-10,4,-5,-1,-5,-2,-6,-8,-6,-2,1,8,7,-2,4,2,8,-3,4,5,10],[-8,8,5,-8,-6,4,-9,-3,5,-4,1,-5,-4,10,-6,9,-7,10,10,-3,-7,2,8,-6,3,10,-3,-10,-3,6,-3,3,-1,5,3,10,5,-7,-7,3,-6,-6,9,-5,6,-2,-6,10,10,-1,-3,4,-2,8,7,-1,-6,3,1,-8,7,8,6,1,3,-8,4,2,-6,-7,-2,7],[5,5,-8,-3,-4,-8,-8,6,-2,8,10,-4,-10,1,-9,-2,-10,10,-4,3,-5,8,-2,5,-1,-2,2,-7,-6,4,9,-10,7,-5,3,6,-8,3,1,6,2,-10,5,-5,-8,-8,7,5,8,-4,9,2,6,-9,-3,6,-4,-10,-8,2,5,2,-10,7,-7,10,1,-3,-7,-4,9,6],[10,4,2,-3,-8,3,2,-5,-1,4,8,10,2,-6,8,4,-7,-6,-4,7,2,1,10,-2,2,-6,5,-6,2,6,1,5,-8,-10,-10,6,9,-7,-5,1,-8,10,2,10,5,3,-8,5,-1,-10,-3,4,-6,-2,-3,10,9,5,-3,7,-3,-3,3,8,-6,7,-7,-1,6,-3,6,8]], dtype = "uint8")#candidate|379|(4, 72)|const|uint8
call_378 = relay.TupleGetItem(func_33_call(relay.reshape(const_379.astype('uint8'), [12, 12, 2]), relay.reshape(const_379.astype('uint8'), [12, 12, 2]), ), 0)
call_380 = relay.TupleGetItem(func_37_call(relay.reshape(const_379.astype('uint8'), [12, 12, 2]), relay.reshape(const_379.astype('uint8'), [12, 12, 2]), ), 0)
output = relay.Tuple([call_371,call_373,var_374,call_378,const_379,])
output2 = relay.Tuple([call_372,call_375,var_374,call_380,const_379,])
func_381 = relay.Function([var_374,], output)
mod['func_381'] = func_381
mod = relay.transform.InferType()(mod)
mutated_mod['func_381'] = func_381
mutated_mod = relay.transform.InferType()(mutated_mod)
var_382 = relay.var("var_382", dtype = "float32", shape = (154, 10))#candidate|382|(154, 10)|var|float32
func_381_call = mutated_mod.get_global_var('func_381')
call_383 = func_381_call(var_382)
output = call_383
func_384 = relay.Function([var_382], output)
mutated_mod['func_384'] = func_384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_391 = func_194_call()
call_392 = func_194_call()
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_414 = func_194_call()
call_415 = func_194_call()
output = relay.Tuple([call_391,call_414,])
output2 = relay.Tuple([call_392,call_415,])
func_429 = relay.Function([], output)
mod['func_429'] = func_429
mod = relay.transform.InferType()(mod)
mutated_mod['func_429'] = func_429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_429_call = mutated_mod.get_global_var('func_429')
call_430 = func_429_call()
output = call_430
func_431 = relay.Function([], output)
mutated_mod['func_431'] = func_431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_509 = func_194_call()
call_510 = func_194_call()
output = call_509
output2 = call_510
func_514 = relay.Function([], output)
mod['func_514'] = func_514
mod = relay.transform.InferType()(mod)
output = func_514()
func_515 = relay.Function([], output)
mutated_mod['func_515'] = func_515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_429_call = mod.get_global_var('func_429')
func_431_call = mutated_mod.get_global_var('func_431')
call_528 = relay.TupleGetItem(func_429_call(), 1)
call_529 = relay.TupleGetItem(func_431_call(), 1)
func_110_call = mod.get_global_var('func_110')
func_113_call = mutated_mod.get_global_var('func_113')
const_544 = relay.const([7.972692,4.430458,-3.117375,3.893643,-7.132411,7.341942,4.133567,-5.210697,6.498470,-9.728674,-5.261137,7.176077,-6.009433,6.914860,6.590527,4.997261,-4.217467,-4.276403,-3.774425,-9.899021,-4.963485,-6.098906,-9.569121,2.127913,4.001508,-0.614439,-4.314681,3.315665,-2.500337,-7.879292,7.519692,-7.557665,-5.763704,4.236886,-6.342083,4.732330,7.863497,-6.864717,-7.041400,0.656392,-7.640996,5.734443,3.867333,4.552538,9.929131,7.232639,-6.486100,6.001158,-1.734562,1.782096,-8.264193,-9.218520,-7.525878,-3.490987,-6.900284,7.776721,9.648617,4.259481,3.459521,-9.711049,-3.227145,6.540002,1.121237,2.134917,4.650889,5.161700,7.139923,0.874989,-2.186064,-7.823726,0.691286,0.509489,-5.557237,0.569727,-0.595962,-5.300733,3.763424,2.744008,-2.713353,6.261243], dtype = "float32")#candidate|544|(80,)|const|float32
const_545 = relay.const([4,9,5,1,-2,-9,-2,-10,-10,5,-4,7,-9,9,-10,6,-2,-3,4,10,-8,6,-7,10,-5,-3,3,5,2,7,-4,7,1,-4,5,-2,-5,2,3,1,6,-8,-6,3,7,-2,-7,9,-9,3,-9,7,-1,7,-9,-5,2,6,-6,-10,8,-6,-10,-3,7,5,10,9,-8,-7,-5,-4,6,7,-8,5,-10,3,5,1,1,-10,-7,-2,7,4,2,1,7,-9,6,2,-6,-5,2,-5,-3,2,5,-5,-3,-4,-6,-2,4,1,-7,5,-10,4,-8,5,-5,-3,2,1,-6,2,-2,8,-8,-6,-2,8,-1,5,3,-5,6,-9,6,6,6,6,2,4,3,-7,-8,10,-1,-3,5,-3,5,-1,-1,-3,-5,-5,-2,-9,8,1,-4,7,6,-8,-9,-3,-4,-7,1,3,10,-3,8,9,-9,-2,-1,-8,3,5,-8,8,3,6,7,10,-7,10,-6,-1,-9,-9,4,-5,-3,10,-1,3,4,-7,-9,6,1,-3,-7,3,-9,-4,10,-3,4,-6,2,8,-9,6,-6,-5,-10,-4,-5,1,-1,-1,8,8,7,-6,1,2,-3,-7,-3,-5,-3,10,-8,-5,9,4,10,-9,3,-6,9,4,6,-10,6,-4,4,8,-6,-5,-9,-2,8,-7,-7,7,1,-10,7,-8,3,3,-5,-1,5,7,4,4,1,5,4,-5,-5,4,3,4,-3,7,-9,-10,-4,-8,-6,-2,-8,4,9,9,-4,-4], dtype = "uint8")#candidate|545|(288,)|const|uint8
call_543 = relay.TupleGetItem(func_110_call(relay.reshape(const_544.astype('float32'), [4, 4, 5]), relay.reshape(const_545.astype('uint8'), [288,]), ), 2)
call_546 = relay.TupleGetItem(func_113_call(relay.reshape(const_544.astype('float32'), [4, 4, 5]), relay.reshape(const_545.astype('uint8'), [288,]), ), 2)
func_514_call = mod.get_global_var('func_514')
func_515_call = mutated_mod.get_global_var('func_515')
call_548 = func_514_call()
call_549 = func_514_call()
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_558 = func_194_call()
call_559 = func_194_call()
bop_560 = relay.power(call_528.astype('float32'), relay.reshape(call_558.astype('float32'), relay.shape_of(call_528))) # shape=(4, 9, 1)
bop_563 = relay.power(call_529.astype('float32'), relay.reshape(call_559.astype('float32'), relay.shape_of(call_529))) # shape=(4, 9, 1)
bop_566 = relay.left_shift(call_548.astype('int8'), const_545.astype('int8')) # shape=(4, 9, 288)
bop_569 = relay.left_shift(call_549.astype('int8'), const_545.astype('int8')) # shape=(4, 9, 288)
func_164_call = mod.get_global_var('func_164')
func_168_call = mutated_mod.get_global_var('func_168')
const_573 = relay.const([[3.670176,-2.509447,-1.724172,1.831979,3.170687,-6.958793,-3.106454,0.204969,5.596909,2.694938,-1.321138,5.375992,-3.150226,-8.744200,2.185898,7.011941,7.593378,4.309144,-8.821903,-5.817713,0.126322,-2.576322,-2.645301,7.870969,-2.289251,8.666344,-8.758489,-8.905644,9.123998,8.792648,4.897456,9.476991,-1.298746,6.988833,1.911610,-3.955786,-8.002925,-2.780605,-8.237380,-2.806785,4.879512,3.897850,-9.910743,-9.887354,-0.595386,5.317523,-4.242913,2.430092,8.427108,-0.488735,-5.875784,2.139923,3.625693,5.998820,-9.383779,8.515347,3.033347,5.704066,-6.973024,4.683324,8.305042,3.778296,-9.684515,-5.297541,3.203515,-7.315356,-7.605072,-6.239911,-2.363223,3.502015,-7.565421,-5.710677,-5.338470,9.980072,9.977682,4.538297,7.341456,-7.078705,2.740619,-2.400700,8.959135,-6.475813,-3.057724,-6.022943,3.193863,1.189391,-6.029580,6.689492,4.173767,2.441201,-4.823695,8.941217,1.856431,0.119876,2.231313,5.145434,-9.874859,-4.266902,8.089509,5.503049,-2.868087,-7.738094,-8.850714,2.235344,-7.520365,-2.210925,-7.642117,4.225033,-4.040420,-3.677674,-8.105926,-4.620254,-2.267566,3.546333,7.242597,-7.873320,-0.776032,-2.730459,-2.623780,-0.976251,2.104732,6.765332,3.824702,1.778354,7.795473,1.449424,-6.213744,8.397641,-4.463598,-1.561238,0.346110,2.991830,4.946556,4.063024,-1.051477,-1.079352,-6.908765,6.943206,-8.350229,8.131132,-1.115133,1.906666,8.674992,3.813687,-9.729852,4.350580,-9.842932,3.506983,5.448659,-9.046051,-7.702144,6.665432,-2.375692,-3.003970,2.733954,4.029353,-0.560403,-7.898760,2.299834,4.638983,7.954268,4.603928,-3.859162,6.337582,6.778425,6.206307,4.593062,3.850577,5.643923,-8.368364,0.677432,-7.986454,6.734666,6.810906,5.060347,-4.462217,-5.370103,-9.731047,-7.026365,-0.526702,9.133339,8.425999,-1.103616,0.328050,6.948765,-3.816552,8.749546,-6.561413,-8.366233,5.574857,3.248045,-7.182777,4.532692,-2.932346,6.659445,-3.981772,-9.639010,8.638784,-7.885519,-7.788605,-6.661365,-0.553777,4.311637,-9.550359,7.564220,5.246129,4.760252,-8.601499,8.065039,-9.287274,0.645901,1.275943,5.287275,-3.528975,3.497886,6.638108,0.735486,2.767487,-2.636601,-2.508163],[8.369211,-7.042509,-6.489247,-6.130571,5.151712,-0.544610,2.335391,-4.747850,-3.519579,-3.199139,9.873373,2.933170,8.965610,-6.028751,1.797686,9.599066,-3.483166,8.321988,-4.949853,-9.400444,1.952984,-3.942966,6.088422,4.202091,1.256315,7.158649,0.538658,-0.871548,-5.323416,-9.375470,3.515861,-6.230187,-1.106890,-6.038642,8.606548,-8.386919,2.109330,4.388951,-6.647813,-8.353955,-1.073237,-0.552628,9.878654,1.376643,8.385197,9.365587,9.766647,6.494343,5.967828,7.714978,-1.002989,2.981935,-5.154046,-0.044843,2.074700,1.612516,5.690733,7.715044,-9.457705,-8.385456,6.934425,-5.405873,0.050845,-4.320670,-6.075490,-8.428606,2.337815,-6.958533,-2.713536,-9.738634,-2.511521,-1.583488,-7.645191,-5.827865,-7.361889,-7.761223,-5.471350,-7.041259,-9.894292,-1.800556,-7.801133,-2.313644,4.052701,-9.368086,5.965913,0.634383,-1.449684,8.358972,-1.070700,5.208424,-6.733451,-6.266049,-3.169573,4.608146,3.278236,1.451281,-3.266352,8.720304,9.694498,9.337310,9.281679,-3.242989,-3.749147,-3.150122,7.191943,4.560949,0.080929,-9.348993,2.498603,0.268540,8.293810,-9.954588,-3.613219,7.100302,0.842768,-8.311419,-9.488446,-7.765361,6.383833,5.298555,-9.347495,-9.374972,-9.988875,-6.203563,-2.877120,-1.989025,-6.996230,2.494590,-2.236224,-1.195847,-4.127573,-0.261536,6.875307,9.153419,2.179042,7.100037,-6.383050,-5.398850,-4.499908,-5.235145,-3.617494,8.778101,8.515355,9.606820,0.167532,-3.582525,-6.298713,-8.400641,2.165163,-1.308534,-0.594339,8.183504,-6.112622,5.286973,-7.165513,5.727897,-5.656409,5.357611,-9.442657,-2.240383,5.051195,3.790960,7.168440,4.374473,4.650766,-5.163590,-9.133938,-9.844557,1.977291,1.901676,7.703739,-1.073562,0.841887,-8.188785,-8.408232,-1.368914,3.078568,7.810021,9.275637,2.858260,9.673538,3.178514,0.918885,-9.016423,0.403040,-1.306424,-4.668452,8.409599,9.355840,7.317176,-0.545960,9.093343,4.432209,-1.621859,1.197514,-1.187926,1.401078,-6.732115,7.982254,2.853703,9.568757,-9.510918,-9.919164,9.467419,4.621626,2.456569,-2.312363,5.408210,-5.411325,8.576650,5.970214,-8.473114,7.204728,-3.160205,6.430799,4.910414,3.223262,-1.362381,0.956946,2.798490],[7.905322,-6.907126,3.613446,1.813592,-4.626286,-7.930564,-1.582374,-1.225968,7.279784,2.716119,9.116028,5.470258,-7.764596,-0.132004,-6.448214,-4.518316,4.191490,7.527122,-8.371582,-7.744962,5.113776,-6.675693,5.302877,5.907433,0.507545,4.356802,-6.423529,-6.406857,-8.287357,-8.299024,-4.016020,-5.705535,-4.062680,3.885567,9.708568,9.828973,-8.171585,-4.188330,-2.735617,-9.642966,-4.646476,-5.118729,9.808461,6.038919,-3.890947,-4.879245,-8.710663,-7.834103,-5.867010,8.914476,9.317358,3.708862,3.471776,9.765504,7.034675,3.369887,7.991980,-3.851723,-8.388700,-3.794623,-0.698278,-9.789176,-1.373786,9.574330,-7.693546,-1.048601,5.516118,8.201632,5.572895,-1.635513,-6.545150,7.138884,-4.640898,-2.425886,3.241722,5.511288,4.653372,0.289504,-8.578148,8.740140,8.415272,-6.210948,5.351221,2.164545,-4.163304,9.905912,-1.529411,-3.401236,3.931059,2.030709,8.511621,-3.825570,-4.833012,-4.481351,-5.403829,7.567543,6.240373,-7.278954,8.973210,-2.097698,6.420539,6.672772,-8.016648,-2.066905,-4.082220,-7.567894,-1.960796,3.119141,-8.948330,3.026871,5.869749,5.496441,-1.654471,2.660652,4.918746,5.639259,2.676405,-2.074929,-2.514083,4.147904,7.316656,1.048350,-5.645577,-7.771474,-1.057363,9.453845,2.354816,3.193590,-7.939279,8.974790,-8.692155,6.748396,1.426913,2.817549,-5.211204,9.343893,-8.906212,-2.263539,1.810375,-4.522193,-7.375777,4.926946,-2.603893,-7.291059,6.005107,-3.011456,-4.764240,5.107731,-4.448018,-3.484933,-9.130884,-3.182786,-6.191458,3.657238,9.478844,2.910094,-3.139480,1.469316,6.117188,1.915786,-4.613301,-6.790245,4.024332,-0.810521,-8.785655,3.653749,-9.572208,-6.085760,-4.162155,-1.447731,4.773312,7.862846,-7.641030,-2.459720,-1.524025,-7.700926,6.715481,-2.581862,1.147095,-9.004107,3.533194,-4.410414,8.848742,-0.573890,-7.640628,-4.367836,-8.230055,5.695730,-4.663127,8.453779,-2.708065,0.608108,-5.184526,-5.256485,1.465353,-9.851410,-1.540340,-2.880545,2.342063,7.095917,-9.653590,2.906155,-8.939830,5.242388,-5.254838,5.111436,8.333082,-0.462433,-8.416167,0.106619,-3.656186,-5.959998,-4.921025,-2.243849,1.001594,7.730975,8.917882,2.974848,-1.246895,5.896011],[7.502680,4.279630,0.383413,-3.279904,-0.027728,1.576808,3.594116,-6.290833,4.594590,7.625719,-4.910938,-6.231111,2.166143,5.836346,-3.402456,-1.646208,-6.647778,-2.690320,-0.802535,2.011695,-1.715295,9.484457,8.976182,7.913256,-3.448222,5.930254,-2.883180,9.530735,4.699479,1.203955,0.866870,6.234811,3.102902,2.797499,2.135542,-2.836025,-9.073495,2.730841,7.419260,-4.997641,-9.517696,3.329862,6.798592,-9.563302,7.471938,-6.918764,-5.591811,-5.088966,-7.623771,2.291095,3.270640,0.144995,5.231969,3.183626,-3.984571,-6.532557,8.502567,1.647822,-3.660553,-1.861761,1.010091,-1.543724,-7.456751,1.401862,4.526869,-4.046055,-5.164398,-3.881208,1.520297,4.269262,7.779177,-4.026164,9.219371,2.167863,3.605470,6.343365,-5.947595,-8.266627,5.407425,7.987603,-6.677578,3.664122,-4.968137,-7.798000,8.816353,6.297160,-6.699666,3.781380,6.003227,4.466719,-1.123146,1.020236,0.235679,-6.008615,8.724822,2.850332,0.933312,-9.985255,-0.097324,7.182653,-0.076749,-7.172658,-6.868965,-4.550803,-7.732544,5.635408,5.879115,7.153720,-4.538059,7.861135,-3.376152,-8.234009,7.296750,6.263923,2.696156,2.493234,2.476745,-8.286734,7.206527,3.288810,2.273287,3.010626,2.715642,8.479351,-1.757934,1.545209,9.497861,-3.249886,-5.695462,-2.139863,3.758050,-8.416706,3.172709,-6.273820,6.151778,-8.102023,-3.176082,0.939418,-2.668348,-0.891886,8.927398,2.900066,0.812480,8.803408,3.910278,2.720754,1.201377,7.131197,4.064701,-5.010378,9.122168,0.073164,-3.418729,3.351740,8.016373,2.187667,2.230504,3.669360,-4.155623,2.708238,-5.045911,-7.603167,-6.591056,-0.819333,-0.138959,-1.956807,3.872718,4.575724,8.796502,-1.850898,-2.091796,3.381403,1.411871,-3.599162,-2.075560,2.004637,5.277259,-2.401663,-2.087046,1.264776,6.170253,-2.746238,6.516869,-2.508428,0.458935,8.082265,-5.235357,8.247764,9.311861,-4.526196,9.300461,-6.741174,6.858441,-1.899493,7.491754,-3.860296,-0.009283,2.883099,8.767220,-6.737313,-6.978246,-6.213989,-0.591962,-9.054792,-2.162811,2.355529,4.806906,-0.608185,7.507992,-1.331083,-1.216459,2.323939,6.059905,-1.470540,2.694065,4.247851,-7.269503,-4.713290,-3.903281,-9.044042],[2.780683,-5.005682,6.666784,-9.520361,-5.695629,6.745684,4.081805,0.802756,2.659470,9.073302,-9.397693,-0.988697,5.671973,1.630908,-6.514340,-0.312307,-5.299230,-1.613347,0.703492,-9.788146,8.655617,-9.850681,-9.394973,4.731282,5.056376,-0.002211,-6.423448,-5.389181,-3.633097,0.666166,8.192394,-3.549401,-1.108048,9.144132,5.663430,9.370441,4.303585,-5.191568,3.091025,6.988899,-8.587011,-4.291081,-0.784440,-9.024488,4.495211,1.987428,2.451330,-8.380251,-6.686842,4.285854,6.389858,-9.070511,-1.282602,-2.262023,8.533204,-8.282140,-8.404863,-1.699796,6.548692,9.132598,-2.687405,4.649501,-9.489634,3.078841,8.330674,2.348755,-0.019883,5.407036,-7.762007,-9.455987,5.110954,1.098782,-1.367646,3.983262,8.523506,-0.724213,3.567779,2.872522,1.781157,0.874247,-8.240600,9.507568,-5.616821,9.342860,-5.820193,-6.130847,0.436873,1.356858,8.863282,5.773260,0.295743,-7.720644,-8.139843,1.063670,9.280119,-5.243042,5.848171,-4.301657,0.086967,-5.058004,5.754139,0.450260,-6.516622,-7.832040,7.331576,-0.054433,2.702844,-5.968107,0.060688,7.591894,-1.990850,-1.309869,5.705411,0.214444,-3.185099,8.247892,1.932232,-5.820482,8.144050,2.882539,1.991306,-6.447156,1.389093,-3.654478,-2.093043,4.529216,0.354329,-4.128568,-0.591737,8.498743,3.851970,-7.211961,-7.672076,-1.230263,-7.091664,-9.827012,-2.848952,-5.713175,4.620992,-4.863907,0.970279,-7.261736,1.498822,8.615640,4.438418,-1.163291,8.395912,5.554328,-7.676884,-1.068589,2.937079,-0.977075,2.957109,1.223247,6.288031,-0.599852,4.804749,7.001944,6.100783,-0.954501,-5.631222,4.365163,-6.072649,5.731285,-2.688234,7.454013,-9.738332,1.608978,-2.689535,7.600928,-9.338110,-2.412304,-8.339473,-3.167840,1.857903,-1.728752,-0.113729,1.912768,-9.236107,0.006574,-6.224340,5.616363,-3.339573,-6.713365,0.786655,-7.641618,9.646759,-2.173823,-7.769822,2.122119,1.497205,2.127182,0.241654,-2.455822,3.048759,2.965198,-9.495250,3.043279,2.638941,-2.261241,3.441427,1.043458,1.308913,-8.642428,-3.031801,6.312969,-9.695186,9.538050,-6.251208,3.569058,9.976449,0.594047,6.458042,-7.453496,6.767429,-2.381232,7.747764,4.770419,9.915224,9.433900],[-7.625078,1.024813,7.391875,-5.750532,8.767782,-8.605547,-2.521040,-1.125457,-9.790800,6.064119,6.512425,-4.087707,0.820235,-6.689845,1.307361,-9.453007,-0.314582,-3.959188,5.830737,5.738351,7.217085,1.732884,-0.580053,2.499744,5.524636,-6.627794,-0.691766,8.660803,-3.043437,-6.116539,2.124052,2.134152,4.789004,-6.998622,4.352224,1.562250,3.939495,-6.962627,-8.098615,-0.258654,-7.005617,7.763097,6.657370,-0.164238,-9.933813,8.126159,-8.408338,8.205338,3.113172,-7.576279,-9.668833,9.220977,-7.507720,2.229207,7.686028,-2.487831,-1.455102,4.217581,1.980749,6.502521,-2.964889,8.544397,-7.403078,-4.899589,-1.203379,-6.544366,-5.969026,-4.934041,7.484303,-9.702057,6.956930,1.084891,-9.420975,4.639318,-1.159910,1.579458,-4.839246,1.741736,4.796038,-6.975399,-2.711926,-8.202060,-4.827326,-7.535701,-7.183353,-3.048898,2.381431,4.732545,-5.807028,6.550539,-1.419863,-0.967393,-2.177529,8.656768,8.774159,1.674880,-5.821704,5.074458,2.297218,-1.382555,-6.966457,2.247925,-9.459334,5.020907,-9.808108,-7.021799,3.131769,9.884595,-9.188029,5.752937,-7.361330,-3.756683,3.478782,7.495070,0.873098,-7.250408,-3.374388,3.162350,3.563070,-9.627487,-8.271015,-0.661575,2.804045,4.442474,-8.983432,6.064920,4.178012,7.306384,2.272698,0.185251,-8.860946,-5.446270,-9.025753,-9.957746,-8.962102,3.542628,9.417601,-3.186801,9.562405,-0.431369,4.045246,-0.253532,1.561063,0.600179,-8.613966,9.553619,-9.077764,9.900066,-6.141879,-3.865599,-5.300257,5.826462,0.458760,-1.244281,0.307023,-1.663818,2.110730,6.953001,-9.495115,8.597083,-7.307275,-9.200526,9.392014,1.760914,1.693796,-0.426175,9.628528,0.053276,-2.479711,6.631505,-3.069576,-4.683153,-1.642974,2.065667,-2.208394,3.599652,4.058280,8.032772,5.193621,-0.481401,4.551004,6.624516,-3.041045,8.763463,-6.635335,-7.148836,5.448367,-5.508949,2.604789,-7.326174,9.245279,-4.665661,1.906836,6.101944,-4.899122,5.957174,-8.846578,-9.427557,4.216989,0.777846,-1.451058,6.448150,-1.341681,5.826137,4.947648,8.507314,2.243767,4.156527,-6.480735,7.342192,7.189280,-2.791698,1.886248,-6.620051,-9.600529,0.414904,-0.068438,-2.646538,-7.623331,-8.705276],[-1.351420,-0.933533,4.320118,-0.847202,-1.944498,-1.032179,0.302254,-1.477188,2.114691,2.897812,-3.049440,-3.267409,1.084030,-1.203270,-8.824418,3.699199,-5.245928,-7.573030,-8.455031,7.944241,-2.777728,-8.021060,-2.950601,9.684053,3.117725,-0.224629,2.042654,-1.889801,9.640252,-4.128566,3.595067,-8.542082,-0.810999,6.444854,-8.056525,9.817174,-8.311392,-3.813350,-1.852225,-2.237086,-3.366990,-0.131788,9.084401,1.662818,5.828167,-8.251896,3.141510,-0.685807,5.824757,-7.550728,7.445096,3.474031,8.848141,-2.122412,5.343260,-3.622101,7.394081,6.464505,1.657143,-8.075930,-1.268242,-7.214805,7.630495,2.777399,-5.105836,-2.072712,-0.730556,-4.945184,1.112628,4.064577,7.429743,4.516027,-6.367896,-0.479870,4.586978,-4.222421,8.159166,4.786212,-2.950629,-6.904080,2.594969,-2.952220,-8.133276,2.651977,0.206287,-7.362350,-3.783970,-1.943398,-6.008003,0.185422,1.554632,1.658204,-1.679805,2.644765,-7.099283,8.996642,3.504267,9.585860,-3.293666,4.619753,2.354292,8.233704,7.884697,8.784974,-2.559136,4.957104,-1.965236,-6.087699,-2.524302,8.975652,1.095798,-5.842652,-1.846374,-7.047540,-9.481838,4.509450,2.382154,-2.041257,-9.870412,-3.006376,-6.972179,-5.953590,5.066963,4.898324,-1.034280,-9.381433,5.290739,-1.933615,-3.631551,8.961705,2.603776,-0.128583,9.921843,7.879230,-7.648964,-3.715614,-8.843465,-1.604745,5.523554,1.758590,-1.181854,-7.934675,-1.341101,-0.827950,3.386134,9.335218,-4.792887,-9.615198,-2.929189,6.311948,0.522240,0.769852,-0.670668,0.346979,9.675278,8.971974,-1.558608,-7.346136,9.468177,9.927522,-2.020602,8.815800,6.112063,-9.478212,8.179575,-9.214475,6.438587,-7.917343,5.567536,8.478187,-4.884807,9.664723,-5.416555,1.446396,-3.811951,1.707981,-4.801196,7.831187,-4.746253,2.543000,4.227037,-8.104886,-0.338788,-9.315736,7.289183,-1.519809,-6.368936,-2.435163,3.206258,-0.674663,6.632259,-3.080959,-3.192299,1.285592,7.413511,2.989026,-4.116454,5.074568,-2.326927,7.499624,-2.617447,-3.675097,7.731234,4.870924,-3.186131,-5.520980,0.832829,4.768995,-3.634955,-9.082329,-6.372949,-7.016021,-1.534402,6.011302,2.394956,-3.406735,-1.301875,-1.974933,3.099634,8.416375]], dtype = "float32")#candidate|573|(7, 220)|const|float32
call_572 = func_164_call(relay.reshape(const_573.astype('float32'), [10, 14, 11]), relay.reshape(const_573.astype('float32'), [10, 14, 11]), )
call_574 = func_164_call(relay.reshape(const_573.astype('float32'), [10, 14, 11]), relay.reshape(const_573.astype('float32'), [10, 14, 11]), )
output = relay.Tuple([call_543,const_544,bop_560,bop_566,call_572,const_573,])
output2 = relay.Tuple([call_546,const_544,bop_563,bop_569,call_574,const_573,])
func_577 = relay.Function([], output)
mod['func_577'] = func_577
mod = relay.transform.InferType()(mod)
mutated_mod['func_577'] = func_577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mutated_mod.get_global_var('func_577')
call_578 = func_577_call()
output = call_578
func_579 = relay.Function([], output)
mutated_mod['func_579'] = func_579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_620 = relay.TupleGetItem(func_577_call(), 5)
call_621 = relay.TupleGetItem(func_579_call(), 5)
func_164_call = mod.get_global_var('func_164')
func_168_call = mutated_mod.get_global_var('func_168')
call_642 = func_164_call(relay.reshape(call_620.astype('float32'), [10, 14, 11]), relay.reshape(call_620.astype('float32'), [10, 14, 11]), )
call_643 = func_164_call(relay.reshape(call_620.astype('float32'), [10, 14, 11]), relay.reshape(call_620.astype('float32'), [10, 14, 11]), )
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_650 = func_194_call()
call_651 = func_194_call()
output = relay.Tuple([call_620,call_642,call_650,])
output2 = relay.Tuple([call_621,call_643,call_651,])
func_653 = relay.Function([], output)
mod['func_653'] = func_653
mod = relay.transform.InferType()(mod)
output = func_653()
func_654 = relay.Function([], output)
mutated_mod['func_654'] = func_654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_693 = relay.TupleGetItem(func_577_call(), 4)
call_694 = relay.TupleGetItem(func_579_call(), 4)
func_514_call = mod.get_global_var('func_514')
func_515_call = mutated_mod.get_global_var('func_515')
call_698 = func_514_call()
call_699 = func_514_call()
output = relay.Tuple([call_693,call_698,])
output2 = relay.Tuple([call_694,call_699,])
func_700 = relay.Function([], output)
mod['func_700'] = func_700
mod = relay.transform.InferType()(mod)
mutated_mod['func_700'] = func_700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_700_call = mutated_mod.get_global_var('func_700')
call_701 = func_700_call()
output = call_701
func_702 = relay.Function([], output)
mutated_mod['func_702'] = func_702
mutated_mod = relay.transform.InferType()(mutated_mod)
var_719 = relay.var("var_719", dtype = "float32", shape = (12, 2, 3))#candidate|719|(12, 2, 3)|var|float32
var_720 = relay.var("var_720", dtype = "float32", shape = (12, 2, 3))#candidate|720|(12, 2, 3)|var|float32
bop_721 = relay.less(var_719.astype('bool'), relay.reshape(var_720.astype('bool'), relay.shape_of(var_719))) # shape=(12, 2, 3)
bop_741 = relay.right_shift(var_720.astype('int32'), relay.reshape(var_719.astype('int32'), relay.shape_of(var_720))) # shape=(12, 2, 3)
func_429_call = mod.get_global_var('func_429')
func_431_call = mutated_mod.get_global_var('func_431')
call_757 = relay.TupleGetItem(func_429_call(), 1)
call_758 = relay.TupleGetItem(func_431_call(), 1)
uop_765 = relay.erf(bop_721.astype('float32')) # shape=(12, 2, 3)
output = relay.Tuple([bop_741,call_757,uop_765,])
output2 = relay.Tuple([bop_741,call_758,uop_765,])
func_773 = relay.Function([var_719,var_720,], output)
mod['func_773'] = func_773
mod = relay.transform.InferType()(mod)
var_774 = relay.var("var_774", dtype = "float32", shape = (12, 2, 3))#candidate|774|(12, 2, 3)|var|float32
var_775 = relay.var("var_775", dtype = "float32", shape = (12, 2, 3))#candidate|775|(12, 2, 3)|var|float32
output = func_773(var_774,var_775,)
func_776 = relay.Function([var_774,var_775,], output)
mutated_mod['func_776'] = func_776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_874 = func_194_call()
call_875 = func_194_call()
func_429_call = mod.get_global_var('func_429')
func_431_call = mutated_mod.get_global_var('func_431')
call_890 = relay.TupleGetItem(func_429_call(), 1)
call_891 = relay.TupleGetItem(func_431_call(), 1)
func_164_call = mod.get_global_var('func_164')
func_168_call = mutated_mod.get_global_var('func_168')
var_915 = relay.var("var_915", dtype = "float32", shape = (1540,))#candidate|915|(1540,)|var|float32
call_914 = func_164_call(relay.reshape(var_915.astype('float32'), [10, 14, 11]), relay.reshape(var_915.astype('float32'), [10, 14, 11]), )
call_916 = func_164_call(relay.reshape(var_915.astype('float32'), [10, 14, 11]), relay.reshape(var_915.astype('float32'), [10, 14, 11]), )
output = relay.Tuple([call_874,call_890,call_914,var_915,])
output2 = relay.Tuple([call_875,call_891,call_916,var_915,])
func_926 = relay.Function([var_915,], output)
mod['func_926'] = func_926
mod = relay.transform.InferType()(mod)
mutated_mod['func_926'] = func_926
mutated_mod = relay.transform.InferType()(mutated_mod)
var_927 = relay.var("var_927", dtype = "float32", shape = (1540,))#candidate|927|(1540,)|var|float32
func_926_call = mutated_mod.get_global_var('func_926')
call_928 = func_926_call(var_927)
output = call_928
func_929 = relay.Function([var_927], output)
mutated_mod['func_929'] = func_929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_514_call = mod.get_global_var('func_514')
func_515_call = mutated_mod.get_global_var('func_515')
call_951 = func_514_call()
call_952 = func_514_call()
output = call_951
output2 = call_952
func_959 = relay.Function([], output)
mod['func_959'] = func_959
mod = relay.transform.InferType()(mod)
output = func_959()
func_960 = relay.Function([], output)
mutated_mod['func_960'] = func_960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_997 = relay.TupleGetItem(func_577_call(), 3)
call_998 = relay.TupleGetItem(func_579_call(), 3)
var_1010 = relay.var("var_1010", dtype = "int8", shape = (4, 9, 288))#candidate|1010|(4, 9, 288)|var|int8
bop_1011 = relay.right_shift(call_997.astype('uint16'), relay.reshape(var_1010.astype('uint16'), relay.shape_of(call_997))) # shape=(4, 9, 288)
bop_1014 = relay.right_shift(call_998.astype('uint16'), relay.reshape(var_1010.astype('uint16'), relay.shape_of(call_998))) # shape=(4, 9, 288)
uop_1015 = relay.acosh(bop_1011.astype('float32')) # shape=(4, 9, 288)
uop_1017 = relay.acosh(bop_1014.astype('float32')) # shape=(4, 9, 288)
bop_1018 = relay.logical_xor(uop_1015.astype('int32'), relay.reshape(bop_1011.astype('int32'), relay.shape_of(uop_1015))) # shape=(4, 9, 288)
bop_1021 = relay.logical_xor(uop_1017.astype('int32'), relay.reshape(bop_1014.astype('int32'), relay.shape_of(uop_1017))) # shape=(4, 9, 288)
uop_1027 = relay.atanh(bop_1018.astype('float64')) # shape=(4, 9, 288)
uop_1029 = relay.atanh(bop_1021.astype('float64')) # shape=(4, 9, 288)
output = relay.Tuple([uop_1027,])
output2 = relay.Tuple([uop_1029,])
func_1033 = relay.Function([var_1010,], output)
mod['func_1033'] = func_1033
mod = relay.transform.InferType()(mod)
var_1034 = relay.var("var_1034", dtype = "int8", shape = (4, 9, 288))#candidate|1034|(4, 9, 288)|var|int8
output = func_1033(var_1034)
func_1035 = relay.Function([var_1034], output)
mutated_mod['func_1035'] = func_1035
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1042 = relay.var("var_1042", dtype = "bool", shape = (16, 15, 9))#candidate|1042|(16, 15, 9)|var|bool
var_1043 = relay.var("var_1043", dtype = "bool", shape = (16, 15, 9))#candidate|1043|(16, 15, 9)|var|bool
bop_1044 = relay.logical_or(var_1042.astype('bool'), relay.reshape(var_1043.astype('bool'), relay.shape_of(var_1042))) # shape=(16, 15, 9)
output = relay.Tuple([bop_1044,])
output2 = relay.Tuple([bop_1044,])
func_1076 = relay.Function([var_1042,var_1043,], output)
mod['func_1076'] = func_1076
mod = relay.transform.InferType()(mod)
mutated_mod['func_1076'] = func_1076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1076_call = mutated_mod.get_global_var('func_1076')
var_1078 = relay.var("var_1078", dtype = "bool", shape = (16, 15, 9))#candidate|1078|(16, 15, 9)|var|bool
var_1079 = relay.var("var_1079", dtype = "bool", shape = (16, 15, 9))#candidate|1079|(16, 15, 9)|var|bool
call_1077 = func_1076_call(var_1078,var_1079,)
output = call_1077
func_1080 = relay.Function([var_1078,var_1079,], output)
mutated_mod['func_1080'] = func_1080
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1095 = relay.var("var_1095", dtype = "float32", shape = (8, 11, 9))#candidate|1095|(8, 11, 9)|var|float32
uop_1096 = relay.cosh(var_1095.astype('float32')) # shape=(8, 11, 9)
output = relay.Tuple([uop_1096,])
output2 = relay.Tuple([uop_1096,])
func_1100 = relay.Function([var_1095,], output)
mod['func_1100'] = func_1100
mod = relay.transform.InferType()(mod)
mutated_mod['func_1100'] = func_1100
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1101 = relay.var("var_1101", dtype = "float32", shape = (8, 11, 9))#candidate|1101|(8, 11, 9)|var|float32
func_1100_call = mutated_mod.get_global_var('func_1100')
call_1102 = func_1100_call(var_1101)
output = call_1102
func_1103 = relay.Function([var_1101], output)
mutated_mod['func_1103'] = func_1103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_1172 = relay.TupleGetItem(func_653_call(), 2)
call_1173 = relay.TupleGetItem(func_654_call(), 2)
output = call_1172
output2 = call_1173
func_1179 = relay.Function([], output)
mod['func_1179'] = func_1179
mod = relay.transform.InferType()(mod)
output = func_1179()
func_1180 = relay.Function([], output)
mutated_mod['func_1180'] = func_1180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_1184 = relay.TupleGetItem(func_653_call(), 2)
call_1185 = relay.TupleGetItem(func_654_call(), 2)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_1196 = relay.TupleGetItem(func_577_call(), 3)
call_1197 = relay.TupleGetItem(func_579_call(), 3)
var_1200 = relay.var("var_1200", dtype = "int8", shape = (4, 9, 288))#candidate|1200|(4, 9, 288)|var|int8
bop_1201 = relay.power(call_1196.astype('float32'), relay.reshape(var_1200.astype('float32'), relay.shape_of(call_1196))) # shape=(4, 9, 288)
bop_1204 = relay.power(call_1197.astype('float32'), relay.reshape(var_1200.astype('float32'), relay.shape_of(call_1197))) # shape=(4, 9, 288)
output = relay.Tuple([call_1184,bop_1201,])
output2 = relay.Tuple([call_1185,bop_1204,])
func_1216 = relay.Function([var_1200,], output)
mod['func_1216'] = func_1216
mod = relay.transform.InferType()(mod)
mutated_mod['func_1216'] = func_1216
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1217 = relay.var("var_1217", dtype = "int8", shape = (4, 9, 288))#candidate|1217|(4, 9, 288)|var|int8
func_1216_call = mutated_mod.get_global_var('func_1216')
call_1218 = func_1216_call(var_1217)
output = call_1218
func_1219 = relay.Function([var_1217], output)
mutated_mod['func_1219'] = func_1219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_429_call = mod.get_global_var('func_429')
func_431_call = mutated_mod.get_global_var('func_431')
call_1228 = relay.TupleGetItem(func_429_call(), 0)
call_1229 = relay.TupleGetItem(func_431_call(), 0)
uop_1230 = relay.atanh(call_1228.astype('float64')) # shape=(4, 9, 1)
uop_1232 = relay.atanh(call_1229.astype('float64')) # shape=(4, 9, 1)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_1235 = relay.TupleGetItem(func_577_call(), 4)
call_1236 = relay.TupleGetItem(func_579_call(), 4)
bop_1250 = relay.floor_mod(uop_1230.astype('float64'), relay.reshape(call_1228.astype('float64'), relay.shape_of(uop_1230))) # shape=(4, 9, 1)
bop_1253 = relay.floor_mod(uop_1232.astype('float64'), relay.reshape(call_1229.astype('float64'), relay.shape_of(uop_1232))) # shape=(4, 9, 1)
uop_1254 = relay.erf(uop_1230.astype('float64')) # shape=(4, 9, 1)
uop_1256 = relay.erf(uop_1232.astype('float64')) # shape=(4, 9, 1)
uop_1257 = relay.sinh(bop_1250.astype('float32')) # shape=(4, 9, 1)
uop_1259 = relay.sinh(bop_1253.astype('float32')) # shape=(4, 9, 1)
func_959_call = mod.get_global_var('func_959')
func_960_call = mutated_mod.get_global_var('func_960')
call_1260 = func_959_call()
call_1261 = func_959_call()
func_1100_call = mod.get_global_var('func_1100')
func_1103_call = mutated_mod.get_global_var('func_1103')
const_1288 = relay.const([1.895719,5.113541,6.157846,1.328935,-9.686425,4.203186,8.472076,3.783434,-6.635034,9.005778,-7.923390,-1.799636,-8.240609,7.107326,3.620043,3.998243,-4.123724,-1.062101,4.433091,1.989382,7.756752,6.971335,-8.084321,-4.588751,9.253462,-4.270490,9.010513,-6.167042,-1.133912,5.593930,0.711785,9.734617,-4.453460,-5.638756,1.807909,6.745628,-8.752340,4.529961,8.104347,-7.186135,8.197682,5.889407,6.804895,9.903040,8.251230,1.005742,8.085767,-5.003959,-4.974560,8.519621,-3.732362,-9.208240,3.517407,6.567431,9.871331,-9.757087,-9.831924,8.835499,4.806042,-8.295041,-7.588041,-5.254482,-3.230295,6.698855,2.596791,-7.612471,0.748961,-9.808964,-4.528448,2.990287,1.222246,4.187216,5.182866,4.768480,2.115064,-2.524293,1.253854,6.313907,9.780748,6.537468,-6.476668,5.925983,-4.144004,-7.706536,2.953429,6.898937,2.478129,5.936189,4.298590,-0.473243,-7.623186,-0.101836,7.100122,2.229607,-3.262461,9.264994,-2.024740,-9.042475,-2.043758,6.843671,7.999052,8.119665,3.464625,7.844237,6.698756,9.706251,-7.389015,-2.270117,-3.660124,7.844942,-3.812361,2.944697,7.472024,6.272163,-8.784949,3.198768,1.368214,3.579502,8.444852,-6.460143,-3.586181,-6.595081,5.132983,-7.008848,-7.747870,2.012083,-6.343532,9.460509,-2.755676,5.931872,-5.213121,-7.343038,6.297934,-8.818259,4.552663,-2.087780,0.151533,-8.465839,2.934541,-0.435326,-3.208377,-0.802932,-8.673972,-2.189521,-8.463348,6.528984,8.572913,4.704826,7.500570,8.283302,-9.915710,-7.962977,5.514118,-8.907839,2.007585,-5.281396,-8.497372,-1.564038,8.527279,-8.141380,4.601051,-6.435344,6.804011,6.166796,2.975566,0.375322,-4.937237,4.968096,9.560345,-9.172500,-3.050277,-2.156866,0.203251,0.378201,-2.706923,3.353211,-6.454060,-9.290117,3.195367,-2.505557,-7.429499,-9.150922,-7.249110,-2.943299,5.615995,-9.758404,-1.770375,9.403525,-8.839546,-8.352862,-7.680389,-0.769781,1.114812,-4.117230,-4.672193,7.907325,9.892579,-5.069027,-3.120506,9.512767,9.974666,4.719949,-8.666468,-2.601733,-6.159065,4.555750,-3.328984,7.034377,-3.183930,-0.480212,-8.435221,-9.988866,9.053259,7.674139,6.829288,5.593228,2.607729,-1.427366,8.798464,-6.911811,1.695532,-1.596956,4.320627,4.067372,-9.850502,-3.510929,-4.449511,-9.499839,1.725847,5.472867,-1.991281,-4.259685,3.455412,2.742334,8.319556,-7.172267,-7.776578,-3.415497,-9.376479,5.913396,2.572856,-7.631516,-1.320293,4.587859,-0.996667,9.447952,3.125330,-0.855892,-6.225900,-6.919385,0.013210,6.355240,9.751166,6.636977,8.237453,-7.255615,0.709522,-5.828669,7.543904,8.084863,-9.999968,-8.579670,-1.168105,1.766192,6.125549,-9.952549,-4.073265,-3.995476,5.646028,-6.063639,-4.287130,1.448496,6.507613,-8.046379,3.746052,-4.040418,-3.471620,-6.302687,-4.257646,1.677728,3.339361,-9.960038,5.015924,9.464151,4.876737,-6.843830,7.080658,3.201336,2.363342,6.240750,0.406528,9.921336,0.604428,7.135956,1.614751,1.485301,-6.010508,-0.030890,-8.968102,2.540220,8.576074,9.269087,1.341151,6.712369,-9.726156,-5.086274,4.701387,2.186975,8.800431,-0.120876,-0.612802,7.267108,3.648288,-8.583188,8.622308,8.964280,9.151802,3.475056,0.645078,-7.473235,-8.073939,-0.505634,-7.811103,-8.181291,-6.015571,-7.791858,-7.150443,8.516876,6.391174,4.249824,4.441033,-4.012572,1.305721,-1.586586,-8.985933,6.228230,6.857652,-8.854593,8.451191,9.493768,0.990656,-3.552089,2.120981,-5.210865,-2.471699,2.965833,-6.564752,-8.587391,-3.140602,9.976296,1.199065,9.355045,-0.518277,-7.870911,-4.940988,5.397520,0.187101,4.889185,9.860603,-0.319266,5.049434,-1.417250,2.069222,2.932975,8.329830,-0.162941,6.726201,7.345420,-5.068131,-5.220092,2.329305,-3.698978,7.577417,6.068338,0.930052,-9.479476,0.408037,0.133689,-9.389387,-3.217563,0.190741,-8.347299,-5.300723,-1.146542,-2.527042,8.856988,-8.010654,-8.390319,0.947363,-8.239153,1.951556,1.002968,5.323093,0.972057,-5.291670,6.360436,3.266199,-3.455160,4.207101,-7.156234,7.662358,5.980941,4.178895,-5.709507,6.285060,-5.724546,4.205266,-4.142738,-0.817746,-9.925160,6.560143,-5.862943,-1.036946,4.510964,9.013792,1.273793,5.762574,-2.864351,-4.741256,-2.081909,5.724078,1.422122,-1.093049,-9.798691,8.369038,8.138132,-7.920939,1.559306,4.627690,2.455731,-7.067012,7.821782,0.158896,0.103179,-5.309827,-8.842626,-4.926406,5.129092,3.995019,7.785303,-5.656202,3.018669,-3.670044,4.239875,5.886070,-8.800042,7.669996,-4.835585,5.662263,5.814721,6.598464,3.213397,2.058659,-4.452942,-4.779020,4.919523,5.843668,-6.429034,-6.955173,3.290168,-6.842297,0.656506,4.835799,-4.762663,5.559204,4.515823,7.083810,-2.143267,4.258366,2.482037,-8.517652,-0.820465,-0.569856,6.257436,2.264513,-6.348071,-5.949344,4.640916,0.794293,-5.639336,2.931034,5.740067,0.687135,8.818445,1.358576,-2.204673,-4.947154,2.141074,6.278117,5.274915,7.097277,-8.392300,7.924304,4.604955,-3.080823,-9.960224,5.760121,-5.719073,7.983192,2.359323,4.734201,0.929596,4.100502,-3.519382,6.272157,5.834753,2.843100,6.850768,6.970945,-1.400489,-7.382126,-9.806035,-2.374144,-5.241042,-4.437984,-3.713876,-4.937435,1.468083,-4.305274,-5.030061,3.259823,-3.262994,-8.759548,-1.502404,2.981535,4.216838,2.602942,2.808527,-1.539981,3.742489,-9.728467,-9.302953,1.462455,-2.214184,0.811442,-4.874333,-1.760311,-9.811561,-5.796803,-5.946724,7.717067,9.042922,7.378119,-7.088773,0.563117,6.928619,-3.447963,-6.917487,1.407168,0.408562,5.706818,-7.888929,6.708351,-0.608889,5.941865,3.823179,-3.159323,4.405829,5.124897,-1.081241,9.924184,-4.661101,3.683668,-2.086409,3.092621,-2.164515,8.028078,-2.855114,4.483003,-9.389470,-2.331882,8.159494,-2.568213,-2.639886,-3.080863,-3.909161,-2.444525,6.269575,7.829872,4.064374,-1.723932,-3.431355,-5.551622,-8.500268,2.685181,-3.051002,-1.756565,4.822558,-6.317366,-3.903268,-3.569486,-8.409770,-9.092217,-8.065615,0.329732,-6.919091,1.658589,3.100894,-1.631201,9.238009,-5.740238,5.799458,3.764594,-9.775730,-3.860707,8.940670,5.317563,-6.973454,4.574260,-1.873399,-6.967449,-8.130719,2.094924,2.477953,9.905430,0.042522,-6.331345,-8.671188,0.668316,9.784095,-2.612309,-5.059191,-7.661716,2.812381,-4.553223,5.106232,-0.276721,-4.632018,2.069809,6.232079,4.307940,4.030730,8.267875,1.986395,-4.895507,0.202827,7.521681,-6.496137,-9.341820,-6.694715,0.748714,5.113677,2.948452,3.808699,2.857031,-9.522295,-5.866124,-0.616268,4.660832,-2.741253,-7.083298,-7.305711,-0.450376,6.375371,-9.609568,5.885874,3.457356,-3.201151,-4.024710,-0.749409,-1.898011,-6.948172,-9.790697,5.792036,4.842897,4.387429,4.901373,9.799978,-9.005712,-4.371215,-5.006388,6.977746,-7.320092,6.585312,3.231292,-3.485257,-0.781149,-8.513371,4.813655,-3.129889,-1.760185,-7.176544,-8.484487,7.462629,-9.127946,3.023355,2.202015,0.518507,-5.859539,-8.825541,-6.604724,-8.693846,-8.025436,5.085521,-1.082622,-8.108659,1.979276,-9.134212,-3.866469,-4.418555,7.133403,-7.441275,-8.936624,-3.080669,-9.359437,4.153456,1.483749,9.095264,-1.023857,4.482059,-7.239937,6.156749,-2.392965,5.865438,6.441476,4.486708,-6.175579,3.135522,4.024454,0.067563,8.365766,-8.121145,-7.838217,-7.021572,-9.078294,9.926627,9.590633,-8.260824,-7.367157,-2.606939,-9.667976,-8.538641,0.453762,0.340183,0.705639,-2.823391,1.156106,6.649029,-5.161764,5.708281,4.407446,-5.379562,3.225149,-4.718727,-8.217734,-0.352703,6.076390,1.303551,-5.822293,9.870888,-4.255980,-5.296492,1.549931,8.986617,9.725140,-4.520611,-7.048372,3.038078,-2.719895,2.813544,5.793032,9.682555,0.956905,6.040319,2.086279,2.431220,1.259539,-5.116145,-2.361758,-1.138935,-0.273302,-6.459122,9.417036,-4.842218,-2.184678,7.446809,6.234385,-4.705990,8.827295,2.938493,-9.518455,-7.666607,-9.049849,-6.007032,2.172595,2.556610,-6.018715,-9.604982,2.590612,2.960945,-9.290271,5.144718], dtype = "float32")#candidate|1288|(792,)|const|float32
call_1287 = relay.TupleGetItem(func_1100_call(relay.reshape(const_1288.astype('float32'), [8, 11, 9])), 0)
call_1289 = relay.TupleGetItem(func_1103_call(relay.reshape(const_1288.astype('float32'), [8, 11, 9])), 0)
func_959_call = mod.get_global_var('func_959')
func_960_call = mutated_mod.get_global_var('func_960')
call_1292 = func_959_call()
call_1293 = func_959_call()
output = relay.Tuple([call_1235,uop_1254,uop_1257,call_1260,call_1287,const_1288,call_1292,])
output2 = relay.Tuple([call_1236,uop_1256,uop_1259,call_1261,call_1289,const_1288,call_1293,])
func_1311 = relay.Function([], output)
mod['func_1311'] = func_1311
mod = relay.transform.InferType()(mod)
mutated_mod['func_1311'] = func_1311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1311_call = mutated_mod.get_global_var('func_1311')
call_1312 = func_1311_call()
output = call_1312
func_1313 = relay.Function([], output)
mutated_mod['func_1313'] = func_1313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1318 = relay.var("var_1318", dtype = "bool", shape = (6, 12, 16))#candidate|1318|(6, 12, 16)|var|bool
const_1319 = relay.const([[[True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,True],[False,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False],[False,False,True,True,False,False,False,True,True,True,False,True,True,False,False,True],[True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,True],[True,True,True,True,True,True,False,False,True,False,True,False,True,True,False,False],[True,False,False,True,False,False,False,True,True,True,False,True,False,False,False,True],[True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,True],[True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False],[False,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True],[True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False],[False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,True],[False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False]],[[False,True,True,True,True,False,False,True,False,True,True,False,True,False,False,False],[True,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False],[True,True,True,False,False,True,False,False,False,True,True,False,False,True,False,True],[True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,True],[False,False,False,False,False,False,True,False,True,False,False,True,True,False,True,False],[True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,False],[True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False],[True,False,False,True,True,False,True,True,True,False,True,True,True,False,False,True],[False,True,False,True,True,False,False,True,True,True,False,False,False,True,False,True],[False,False,False,True,False,True,False,False,False,True,True,True,False,True,False,False],[False,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False],[False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False]],[[False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True],[False,False,False,True,False,True,False,False,False,False,True,False,True,True,False,True],[False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True],[False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True],[True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,True],[False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,True],[False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False],[False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,True],[True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True],[True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False],[True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False],[True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,True]],[[False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,True],[False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,False],[False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True],[True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False],[False,True,False,False,False,True,False,True,True,False,True,False,False,True,True,True],[False,True,True,True,False,False,False,False,True,True,True,False,True,True,False,True],[False,True,True,False,False,False,True,True,False,True,False,False,False,True,False,False],[True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True],[False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,False],[True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False],[False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False],[False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True]],[[False,False,False,False,True,True,True,False,False,True,False,True,False,True,True,False],[False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False],[False,True,False,True,False,True,True,True,True,True,False,True,True,False,True,True],[False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True],[False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False],[True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False],[False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,False],[False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,True],[False,True,False,True,True,True,True,True,False,True,True,False,False,True,False,False],[True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False],[False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False],[True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False]],[[True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False],[False,True,False,True,True,False,False,False,True,True,True,False,True,True,False,True],[True,False,True,False,False,True,False,False,True,False,True,False,False,False,False,False],[True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True],[True,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True],[False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False],[False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False],[False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,True],[False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True],[False,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True],[False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,True],[False,True,True,False,True,True,False,False,False,True,True,True,False,False,False,True]]], dtype = "bool")#candidate|1319|(6, 12, 16)|const|bool
bop_1320 = relay.logical_and(var_1318.astype('bool'), relay.reshape(const_1319.astype('bool'), relay.shape_of(var_1318))) # shape=(6, 12, 16)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_1343 = relay.TupleGetItem(func_653_call(), 0)
call_1344 = relay.TupleGetItem(func_654_call(), 0)
output = relay.Tuple([bop_1320,call_1343,])
output2 = relay.Tuple([bop_1320,call_1344,])
func_1350 = relay.Function([var_1318,], output)
mod['func_1350'] = func_1350
mod = relay.transform.InferType()(mod)
mutated_mod['func_1350'] = func_1350
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1351 = relay.var("var_1351", dtype = "bool", shape = (6, 12, 16))#candidate|1351|(6, 12, 16)|var|bool
func_1350_call = mutated_mod.get_global_var('func_1350')
call_1352 = func_1350_call(var_1351)
output = call_1352
func_1353 = relay.Function([var_1351], output)
mutated_mod['func_1353'] = func_1353
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1368 = relay.var("var_1368", dtype = "int16", shape = (8, 9, 13))#candidate|1368|(8, 9, 13)|var|int16
const_1369 = relay.const([[[-7,5,-3,-2,9,9,-7,9,4,6,-1,2,4],[-1,-1,-10,-9,2,7,7,7,1,-8,-9,-10,-8],[-1,-8,-10,5,-5,-2,9,-8,-9,4,2,-3,4],[5,-6,6,5,4,1,7,-4,2,-4,-2,7,10],[-1,-2,-4,10,3,-9,10,-6,-5,-6,-3,-2,1],[9,-10,-1,-9,-8,1,-4,6,7,-9,6,7,2],[-2,-6,-8,3,1,1,-7,4,10,6,-3,3,-5],[5,3,-1,-10,8,-9,8,-4,-1,-1,-3,-7,7],[2,-4,-9,9,4,6,5,6,6,-6,-4,-3,6]],[[-5,5,-2,2,-3,5,-2,2,-7,-2,10,6,8],[5,-4,-9,3,-9,-2,3,1,-9,-8,-10,7,5],[-10,5,10,1,-10,-3,6,-10,-4,-8,-10,9,-10],[-3,1,-8,1,-10,5,7,2,10,3,-10,4,3],[7,-4,-10,-5,6,-5,7,8,-5,-7,4,-6,-9],[3,4,-7,-7,-7,-7,2,-6,-10,10,-6,2,3],[3,4,-8,5,-2,-3,3,-8,4,4,6,-4,-2],[1,-6,-2,6,10,1,-7,8,-4,2,9,-3,-8],[7,-3,-4,4,1,-8,-10,-2,-4,7,-9,-2,4]],[[-6,6,-4,-6,3,1,10,1,-10,6,5,-1,1],[3,10,5,-2,2,6,-3,9,-6,10,7,-10,4],[-1,6,-4,5,6,-3,-5,-6,-2,9,7,-10,-3],[-6,10,-6,4,2,3,-3,-1,1,1,6,8,-7],[-1,1,6,4,-7,6,4,-1,-9,-8,-1,6,-6],[-7,8,-9,-3,-2,8,-4,6,-6,7,-9,-4,-7],[-8,8,7,-8,9,5,-8,8,3,-10,-1,-1,-6],[7,7,-4,8,9,-5,-2,4,4,-6,-5,6,8],[-2,6,-9,-7,-6,1,10,1,7,-10,5,-1,8]],[[-10,1,-4,6,2,-4,2,-7,5,-5,5,-2,-10],[-10,-5,-9,5,-4,-5,-8,8,4,-3,4,-10,-4],[10,-9,2,3,8,-4,-4,-3,-1,-5,-4,-8,2],[4,-1,-7,6,-3,-5,-8,10,7,10,-2,10,9],[-8,10,-9,4,-3,-2,6,7,-4,6,7,-10,5],[8,-1,1,4,-1,-4,-2,3,5,-1,-5,-5,1],[-6,9,-4,9,5,-7,9,-3,-1,1,-1,5,9],[7,1,-6,-6,10,-5,7,7,1,10,-1,9,4],[8,-9,9,3,-3,-9,-5,1,8,-1,10,2,-6]],[[-10,7,-4,-3,-2,-1,2,-3,5,10,1,3,-2],[4,2,9,8,6,-10,6,-1,6,-3,4,10,-3],[3,-3,-9,-1,10,5,-3,-9,-9,-7,-4,-2,6],[6,-2,-7,6,-2,-6,8,-10,-1,3,9,4,2],[9,-6,4,10,-10,-2,6,1,-4,7,3,10,9],[10,3,3,8,8,-1,7,-5,10,-3,-3,-2,-1],[-10,5,-10,3,8,7,5,-7,2,-10,5,8,8],[4,-2,7,8,1,8,1,-10,-4,-2,1,-7,2],[-8,-1,-4,10,-10,9,-10,5,-4,6,7,-9,10]],[[-4,3,-2,-8,1,6,7,-10,-5,5,-10,10,-3],[5,5,-5,4,-5,-3,9,-3,5,2,-4,-8,1],[-10,-4,-6,-8,-6,-10,-3,7,7,7,-1,-10,10],[2,-7,-7,-3,-1,-2,2,1,8,-6,-9,-1,3],[-1,-4,8,-2,-8,1,2,10,10,3,3,-5,-6],[-2,-3,10,-7,-8,2,-10,-10,2,1,-7,-6,-2],[2,8,6,-7,-6,-4,1,7,-1,-4,8,-3,9],[-9,10,4,3,-4,-3,-5,-9,-1,10,-4,7,-9],[7,3,2,3,-5,6,10,-6,-10,-1,1,-9,-3]],[[1,-4,-4,-2,7,1,6,6,6,1,-10,-5,9],[-4,-7,3,7,-8,-8,-8,-4,4,6,3,7,-4],[-6,7,-4,-6,-10,-9,-8,-7,-7,9,5,3,-5],[-5,-2,-9,-9,4,9,-4,-10,-5,-10,-3,9,-8],[9,-8,-8,7,4,-6,4,6,-1,4,5,-10,-4],[-10,8,7,-9,-2,-10,7,-4,-6,-5,4,5,9],[-7,-3,-5,4,-2,3,-8,8,-3,-9,-10,-7,-7],[10,7,10,-10,7,-7,-9,1,-10,-6,-6,-5,-5],[-2,-9,1,1,-9,-6,-5,4,-5,10,-4,7,-1]],[[8,8,1,6,-8,-9,9,-1,9,-7,7,6,7],[8,-10,7,-6,-1,-4,7,4,-3,4,-7,10,-3],[-5,4,1,-8,-4,-10,1,-5,6,8,-8,4,-5],[-4,-4,-3,8,-5,-1,1,-7,6,-2,-4,5,-2],[-3,4,5,6,-4,10,-6,4,-7,5,-8,3,-1],[10,-9,8,7,3,-1,3,7,1,10,3,10,5],[-8,-6,7,7,-8,-1,9,7,2,7,-7,3,2],[7,3,-8,2,9,1,7,-1,2,-2,-1,-3,6],[-5,-5,4,-8,6,7,3,-7,-2,-2,3,-4,-7]]], dtype = "int16")#candidate|1369|(8, 9, 13)|const|int16
bop_1370 = relay.subtract(var_1368.astype('int16'), relay.reshape(const_1369.astype('int16'), relay.shape_of(var_1368))) # shape=(8, 9, 13)
func_1100_call = mod.get_global_var('func_1100')
func_1103_call = mutated_mod.get_global_var('func_1103')
const_1376 = relay.const([-3.777690,6.295629,-9.076849,4.122377,-4.272069,-7.550655,-2.939948,9.616135,7.353114,2.684194,-4.741011,9.435156,7.891336,9.166015,9.136658,8.904869,-0.607369,0.993610,4.903527,0.254049,5.833750,-6.707769,6.527110,5.318185,5.297000,4.495631,9.255146,-5.072342,-8.228984,1.963438,4.205402,4.523515,-0.245841,-0.756094,6.711810,1.229539,0.277066,-1.873771,2.857462,-3.044320,-7.179375,-3.146565,-2.494114,7.249139,-2.634983,-9.179893,0.480074,8.799923,1.075909,-3.255166,5.157429,4.640617,4.247684,-8.778274,1.161142,4.995228,-9.416647,9.776208,-1.392527,9.362247,-0.711004,-1.781543,7.636462,0.301536,3.450004,-0.520270,8.811121,-5.359007,7.135856,1.069712,4.333079,7.393546,-6.718808,-6.597701,8.807464,2.857972,-6.613061,1.746179,4.899566,-2.875792,-0.073806,-8.342405,-4.036662,-4.666867,2.734422,-2.434869,-2.452392,-1.087424,2.167605,-6.543688,-9.665778,-9.113590,8.374044,-6.078267,-5.940796,-8.005086,4.721958,-2.083556,6.873883,-7.613924,-7.472236,2.267465,-2.660835,8.121114,-0.022462,-6.736350,9.315005,6.848273,-4.771007,1.411184,-4.490732,-5.633727,-9.875709,5.321840,2.633793,-1.910744,6.564059,0.025815,4.609814,5.831768,-4.772320,-7.482776,-3.871830,-2.816521,-9.203696,3.106463,9.475488,-9.759433,-0.110617,6.465526,9.666219,3.631408,8.081584,-9.929277,6.393264,8.864030,6.121180,4.044452,6.350110,7.215934,1.971791,4.846164,-4.450106,4.533422,9.721171,-9.628855,-2.581629,9.158710,-2.034133,6.790127,2.600165,6.036780,-0.402169,-7.628253,4.121561,4.354382,-7.486929,3.768491,6.093226,0.090686,-5.507032,0.991938,5.104285,-6.049999,7.031775,1.891070,-7.916202,2.171497,7.693762,0.223174,7.394900,-7.598617,5.931931,-7.158943,-1.134780,5.159176,-6.992978,0.762644,-4.037872,0.535335,8.722592,-1.592946,-8.171076,6.555730,-9.009241,-4.451954,4.546474,0.094056,-3.651821,7.702113,-2.864884,8.781145,-5.723173,-8.544606,4.268040,-8.002814,2.557142,-8.072951,-9.807435,7.600208,-0.147707,6.165185,-5.337185,-0.024952,-2.009997,0.414399,1.299117,9.033294,-1.606769,-8.861637,-3.989661,-5.220712,8.045818,7.337037,-4.526021,-6.376279,-1.836617,1.569489,7.776513,0.044050,9.914947,-8.453384,-6.333904,-5.245876,6.388390,-2.615098,3.297026,7.537560,3.108008,4.004412,-4.835390,5.216803,4.761495,1.308093,-7.184371,-2.285685,-6.216159,-9.929601,3.973954,2.230211,2.147959,-8.583435,-5.494470,-2.331272,-4.983274,-6.849470,4.162156,5.820342,-7.632072,8.876244,4.055112,-0.347457,-8.808188,-3.679258,-9.515670,8.661202,5.657056,-6.505971,6.381719,-8.539255,-9.658128,-0.096887,-5.898233,-3.401372,8.900964,8.772300,-9.945682,-7.774448,8.271288,-9.729941,-3.523213,7.520501,6.587163,9.095003,-2.241272,-6.648547,-4.244417,6.194639,-0.510628,2.444564,4.392332,-0.386113,1.791885,6.464263,-7.056791,-2.321701,2.795568,-7.837503,9.218942,0.851797,1.894249,8.028634,8.656059,-2.846010,-2.351997,5.913855,6.662091,4.094129,-2.943602,6.882203,-2.045165,4.086486,7.889850,-3.906953,7.392506,5.278653,5.103587,8.695190,9.909248,-7.212924,0.669901,1.746340,-5.627810,3.257828,5.402132,3.610261,-2.279131,2.994252,-8.683539,4.504077,-8.258123,4.723108,8.018647,-8.587000,-7.106844,-3.422727,-8.485442,-2.882187,6.245573,5.821446,-3.364379,-6.735516,3.578899,7.207005,-3.955907,2.157586,1.077009,-4.728955,0.444624,8.683704,-4.733164,-9.871390,1.516235,8.904731,-1.306172,-2.192107,1.346483,-8.301310,-8.994923,-7.110024,-2.024667,1.861486,-5.632216,-8.778607,-0.703770,-8.804286,1.714766,9.585850,4.634166,5.317055,7.939417,5.315661,6.449076,5.966401,4.123346,-3.712102,-9.003035,6.160702,9.852385,-3.750852,6.565318,-1.999295,9.315778,3.427337,-1.503756,6.836756,-0.424049,-6.217961,-9.732335,-7.973145,-2.533619,7.392499,-2.609106,8.598748,-6.223102,-1.547012,-0.870585,-1.519314,-7.569706,1.939450,0.113161,3.331910,5.257619,0.300774,2.270296,8.495820,-5.671499,-6.731736,9.165940,-5.741886,-1.864277,9.654342,-9.217677,-8.367152,3.067929,6.113432,-1.978491,6.875084,6.233044,4.281963,-7.800656,-5.104240,1.505974,1.162608,-8.866647,-5.130113,-0.317212,-6.235296,-9.178762,-1.199808,-3.769896,-8.264168,-7.193503,-9.659871,-0.164812,-1.605988,-9.243433,7.036151,-3.805050,-6.575047,-2.876806,5.410095,-8.938539,7.476544,-6.368934,-9.209682,-7.256124,-4.099915,-6.968869,-1.858567,-5.039343,7.811484,4.289016,2.296112,-2.538180,-0.636056,-8.157697,3.187435,8.058362,3.082710,-4.291845,-3.571271,-4.313095,0.144490,7.490980,7.226981,7.382627,-6.947354,7.174721,-3.631351,8.227953,3.524123,-6.852752,-3.056748,8.604416,5.627317,-4.249612,-3.317753,-3.860312,1.889372,3.232285,-2.295483,-8.189107,1.652972,-0.543337,4.683094,1.055140,0.853701,6.269864,7.864236,-0.677476,0.273054,6.340445,6.385656,4.328107,2.603330,-5.923574,9.138642,8.554847,-4.536818,-6.358806,0.799168,-0.517388,3.461852,1.457834,8.839458,-9.613010,-3.270979,-4.697535,7.231078,-1.021262,2.630943,-9.820723,6.700468,6.965538,7.982661,2.437975,9.685219,-6.629819,-0.938568,-2.128094,6.563350,-9.818323,-5.364836,4.822747,-1.774244,-1.662386,-7.496965,5.585021,-4.991641,-0.339618,-3.275321,5.820524,2.590092,7.308554,4.585285,5.339546,-5.006658,-9.617824,9.383443,-8.612264,5.299872,4.083981,-8.778026,-4.786772,3.467834,-6.838965,-4.072506,-4.582139,1.165205,1.926575,8.524923,7.932652,-7.047578,-0.931168,-6.068492,-1.428018,2.889074,3.852662,-1.812736,2.502765,-1.064908,6.377919,5.777204,6.933612,8.043879,9.476862,5.760503,-3.599600,-2.878129,0.652536,-3.331961,-8.621102,4.343926,3.255953,3.949593,-4.903117,-9.461917,0.669712,4.586870,1.757937,3.410409,1.440648,6.735502,4.110961,-9.498964,-6.456153,-1.370979,-9.512354,7.310143,2.402665,-1.119634,-2.327743,5.510773,-0.237780,-8.102301,-5.517776,-6.383839,8.672581,3.985013,1.693132,3.208405,-3.490833,2.831031,-6.290991,-5.672347,2.101626,0.129903,-2.840070,8.812727,1.607380,-2.877917,-8.287460,9.081531,-9.379156,-2.753865,-3.619998,-0.812708,1.207590,0.518318,-1.962961,7.411170,0.945055,1.315173,5.227298,-3.144793,0.312318,-4.397666,-5.101117,8.524683,9.527629,-3.334262,1.744892,-0.095660,-2.500702,-4.685010,-3.922765,9.910621,-9.749875,3.348385,7.811531,-4.666273,-8.431803,-2.907152,-4.524408,7.170931,5.250132,0.788275,-8.415770,8.757644,-8.895438,2.829878,3.282828,-2.721084,-0.957476,-2.106361,5.505587,-9.373457,5.170230,-9.773045,-6.117676,2.134248,-9.039806,-3.328979,6.023974,5.790378,-8.513364,-4.867653,9.198283,8.095393,-0.927822,-1.321432,1.122532,8.699153,2.595636,-1.033775,7.677223,-1.425512,5.543937,1.715193,-0.372176,-9.721849,9.029937,1.777379,7.623358,-8.396325,-9.314302,9.891639,2.790375,-6.114011,8.494673,-0.141750,2.082317,-2.165611,-3.822819,9.618436,-6.348602,6.265386,-7.848818,0.005635,9.525941,9.054063,-7.465702,7.509686,8.174786,-7.260786,5.863724,3.449456,6.303767,0.004339,2.808703,6.224422,-7.537495,-4.079454,1.827546,-8.288007,9.469329,-4.188990,-6.277867,-9.891565,1.714879,-7.339514,8.048049,9.670156,8.276346,-8.798869,7.751696,4.359084,-2.349062,-6.352755,2.454660,6.702127,-1.622303,-2.302501,1.790283,-4.966018,9.987644,3.504653,4.198542,-8.257670,6.213432,9.701200,-6.819848,-5.280812,-6.919430,-7.837472,3.708444,7.635532,3.715501,1.285229,-7.521527,5.337356,-5.689073,-0.195870,-1.211814,9.342948,-9.246688,-2.671943,5.717956,0.847583,-1.125563,2.642642,4.291318,3.605350,-3.803885,-2.130118,4.914584,-7.737843,-5.192762,9.824150,5.120078,7.602820,3.046382,-8.272336,-2.265941,5.195374,7.073516,8.081806,2.596056,2.915458,2.695916,-6.926853,-4.264857,-0.262162,9.997597,5.706318,-8.238526,-4.032081,-6.478800,-0.061456,9.293011,1.780564,-9.943454,8.446273,-8.666429,5.717227,-9.050311,-5.100313,3.631862,-1.628064,-2.907524,9.246824], dtype = "float32")#candidate|1376|(792,)|const|float32
call_1375 = relay.TupleGetItem(func_1100_call(relay.reshape(const_1376.astype('float32'), [8, 11, 9])), 0)
call_1377 = relay.TupleGetItem(func_1103_call(relay.reshape(const_1376.astype('float32'), [8, 11, 9])), 0)
output = relay.Tuple([bop_1370,call_1375,const_1376,])
output2 = relay.Tuple([bop_1370,call_1377,const_1376,])
func_1413 = relay.Function([var_1368,], output)
mod['func_1413'] = func_1413
mod = relay.transform.InferType()(mod)
var_1414 = relay.var("var_1414", dtype = "int16", shape = (8, 9, 13))#candidate|1414|(8, 9, 13)|var|int16
output = func_1413(var_1414)
func_1415 = relay.Function([var_1414], output)
mutated_mod['func_1415'] = func_1415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_959_call = mod.get_global_var('func_959')
func_960_call = mutated_mod.get_global_var('func_960')
call_1492 = func_959_call()
call_1493 = func_959_call()
const_1494 = relay.const([[[2.077635,3.215800,4.655993,1.909375,7.882655,5.846400,8.446440,0.620686,-0.744939,7.627964,-1.500143,6.915590,-7.684443,0.641248],[1.038992,-9.652381,-7.786641,-9.755694,-4.739105,0.728522,-4.037644,9.712021,-3.090556,0.959490,2.262383,-9.857915,2.319010,-2.381323],[-1.142984,-7.389208,-9.272667,8.432127,8.930013,-2.390579,5.862255,9.210923,2.970944,1.067666,2.166959,-5.752017,-5.831580,-7.345887],[-5.264628,8.188864,-4.500784,1.074371,-2.795159,-5.136443,-9.312459,-7.059650,-6.881485,-7.485261,-3.459040,8.382603,-0.405569,-8.541050],[9.712388,-1.846341,2.865090,-3.715331,-5.003421,7.751444,-6.704996,-2.577290,-7.841976,8.232866,-6.272743,-7.070706,6.375170,3.633346],[-8.772889,-2.536330,-0.614517,5.567241,-5.055950,-0.184491,5.343260,-4.915773,1.950184,3.044188,8.098019,-5.337920,-0.993134,-9.536921],[-8.257556,1.049091,0.345613,-2.916106,-3.370477,0.337186,-9.953353,4.420705,3.188372,6.161631,-5.036092,0.521096,3.218377,-4.020828],[-4.779450,-9.213055,-9.031855,8.828312,8.669149,5.449839,-3.930450,3.668055,-9.359511,-7.018340,-2.757171,-7.819047,-5.297122,-6.264828],[0.872818,1.912082,5.104124,4.339368,9.174515,9.455563,-8.606221,5.903969,5.318117,3.928485,6.212560,-4.391946,-6.271635,8.312507]],[[-8.043703,-6.901206,-5.703266,5.478340,1.997542,5.064372,-1.521335,-3.486365,8.964273,3.986593,-6.969061,7.237493,-7.004034,3.168608],[-6.288759,-8.542112,-8.142846,7.184388,-5.309298,-0.276185,9.683001,3.454301,-1.512717,-1.277664,0.933112,-2.624071,4.796174,5.788145],[0.001963,-6.360698,6.794178,-5.477931,6.847965,-9.092169,8.964911,-6.078470,-2.304595,-1.496083,4.976040,5.849507,-0.443314,-4.009751],[8.496832,3.866133,-0.216361,-2.235923,-9.001623,5.791325,-8.966313,-3.085730,-8.072448,-7.909098,-2.143371,0.959955,-9.359797,-2.096714],[-2.884320,-3.154914,-9.482470,8.379807,0.271870,5.082920,-4.454648,3.467367,-6.470032,-5.946743,-8.275004,-0.798385,9.905928,-6.865507],[-6.491554,-3.023697,6.819266,-4.634560,4.273660,-9.206254,7.815383,-2.229447,-8.407936,8.687111,4.766537,4.422908,-1.283943,-4.279146],[4.040322,3.004293,7.322689,3.771416,-8.366809,9.172576,3.367909,-9.810863,3.587182,-7.115981,9.957778,-9.800794,-3.288635,-4.152417],[2.666146,-0.231105,-3.773170,-2.184405,-6.862346,-0.695287,6.387584,-2.863060,-7.271601,-3.287668,3.103759,5.047719,-1.787012,-2.816427],[-7.352799,9.572980,9.953674,-2.271327,-3.327577,-3.863529,-2.722781,3.094971,-0.952365,-3.859810,4.035127,-2.982174,-9.430424,6.839500]],[[3.281377,7.268880,-1.460715,-0.050584,-9.957137,6.022391,7.126616,4.708134,6.929702,-4.165666,-6.439420,-8.394590,3.661250,1.880686],[-3.546109,-4.403390,-1.941158,1.577971,-9.339412,-4.287870,4.491852,3.422689,5.846129,-7.415305,-7.835279,-1.505966,-2.821566,-2.258136],[5.198330,7.030819,-2.621038,-6.057389,2.542136,5.373439,1.468491,-1.127518,-8.945478,9.907545,3.409954,-9.135266,-6.671531,-1.029905],[2.061565,-9.813395,-7.281423,-3.233600,0.696653,6.850143,1.248308,1.508039,0.683648,8.955888,3.768375,4.571813,-9.927917,-6.819905],[0.621111,5.894045,7.094074,5.303512,6.894625,-3.344037,-6.728817,8.398910,5.518731,-4.534101,4.146595,-8.279117,0.125276,1.102992],[7.110220,-4.527312,-2.225346,5.986445,-8.878632,-3.900211,-5.775038,-9.836605,-4.712632,-0.540620,-9.190912,-7.913647,-6.355784,4.737964],[3.034700,-5.693769,-3.397177,5.559735,-5.829643,1.705753,6.855183,3.858729,-4.237099,0.134117,4.642609,-9.923819,-5.759285,7.098267],[4.306613,-6.990521,8.077996,7.097473,-2.574982,5.946290,0.360956,0.779140,-3.889095,1.055858,-2.920890,3.095032,-9.280421,-9.185591],[2.184032,-0.393874,-4.642119,8.598170,7.849942,0.689983,1.192798,-1.175723,1.475329,1.936150,-4.721957,2.781448,1.737617,7.933951]],[[-9.711129,2.769244,9.722449,2.482569,-2.478945,-2.960038,9.322591,4.248754,-5.528390,-7.441214,4.814658,0.847087,-3.256467,7.187846],[9.085402,6.190253,-6.628887,3.651971,-1.140256,3.688436,2.356832,-2.483398,7.255063,6.030788,-7.994381,-1.654171,-2.829560,8.171182],[-7.695341,-1.482875,9.871768,2.880429,-9.617615,-5.146146,2.929272,-0.755004,1.436469,-3.530016,-9.182049,-8.209884,6.200860,9.056227],[-7.498289,-3.499427,7.447049,-5.521602,-1.677295,-9.076692,8.738798,-8.744137,-3.106027,0.923113,3.146992,-9.722741,-1.821451,-6.408002],[0.031536,9.497779,6.080606,-1.735459,-1.848168,6.388940,9.391439,-5.850877,-7.278887,1.523759,9.652675,-2.187385,-6.237035,-0.721639],[2.940293,-3.619165,-7.223458,-8.139687,3.462923,-5.890020,-7.718267,3.332222,0.497985,-1.219348,-1.430073,-2.843589,-7.023567,-5.493838],[-4.717828,6.295126,-9.194746,-9.189771,9.173586,-9.648453,-9.373775,1.833197,-6.126137,-0.906936,-0.162920,-0.962773,-8.859135,-0.587635],[8.694722,-5.015812,2.579257,-8.862235,4.897374,1.140263,5.576115,-8.039596,-9.609407,-6.164577,-8.928649,7.209712,3.402866,2.339571],[-5.982739,7.373496,-8.875920,4.526928,7.978378,1.616477,2.464222,-3.000141,-1.713552,-3.933948,-3.026948,-7.463371,5.073430,8.125156]]], dtype = "float32")#candidate|1494|(4, 9, 14)|const|float32
bop_1495 = relay.greater_equal(call_1492.astype('bool'), const_1494.astype('bool')) # shape=(4, 9, 14)
bop_1498 = relay.greater_equal(call_1493.astype('bool'), const_1494.astype('bool')) # shape=(4, 9, 14)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_1503 = relay.TupleGetItem(func_577_call(), 2)
call_1504 = relay.TupleGetItem(func_579_call(), 2)
func_280_call = mod.get_global_var('func_280')
func_282_call = mutated_mod.get_global_var('func_282')
var_1508 = relay.var("var_1508", dtype = "float32", shape = (6, 66))#candidate|1508|(6, 66)|var|float32
call_1507 = relay.TupleGetItem(func_280_call(relay.reshape(var_1508.astype('float32'), [4, 9, 11])), 1)
call_1509 = relay.TupleGetItem(func_282_call(relay.reshape(var_1508.astype('float32'), [4, 9, 11])), 1)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_1526 = relay.TupleGetItem(func_577_call(), 4)
call_1527 = relay.TupleGetItem(func_579_call(), 4)
uop_1538 = relay.atan(call_1526.astype('float32')) # shape=(10, 14, 11)
uop_1540 = relay.atan(call_1527.astype('float32')) # shape=(10, 14, 11)
uop_1546 = relay.sin(uop_1538.astype('float32')) # shape=(10, 14, 11)
uop_1548 = relay.sin(uop_1540.astype('float32')) # shape=(10, 14, 11)
uop_1551 = relay.log10(uop_1538.astype('float32')) # shape=(10, 14, 11)
uop_1553 = relay.log10(uop_1540.astype('float32')) # shape=(10, 14, 11)
output = relay.Tuple([bop_1495,call_1503,call_1507,var_1508,uop_1546,uop_1551,])
output2 = relay.Tuple([bop_1498,call_1504,call_1509,var_1508,uop_1548,uop_1553,])
func_1556 = relay.Function([var_1508,], output)
mod['func_1556'] = func_1556
mod = relay.transform.InferType()(mod)
mutated_mod['func_1556'] = func_1556
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1557 = relay.var("var_1557", dtype = "float32", shape = (6, 66))#candidate|1557|(6, 66)|var|float32
func_1556_call = mutated_mod.get_global_var('func_1556')
call_1558 = func_1556_call(var_1557)
output = call_1558
func_1559 = relay.Function([var_1557], output)
mutated_mod['func_1559'] = func_1559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_1592 = relay.TupleGetItem(func_653_call(), 1)
call_1593 = relay.TupleGetItem(func_654_call(), 1)
const_1594 = relay.const([[[-3.266425,4.054645,8.206349,6.053371,5.825534,-6.961239,3.728409,-0.296422,3.998794,-0.507501,-6.773918],[-5.873653,-8.740096,3.086136,2.162904,8.346809,-6.619961,-6.167496,0.557822,5.742285,-2.285864,-1.506656],[3.525085,8.501370,-9.643980,5.377192,-0.569495,5.979290,-0.759145,0.867965,0.826487,0.069197,9.339050],[9.601974,-4.114395,7.813594,-0.162017,-2.791508,-8.118752,-6.953508,7.397136,-4.159870,-3.943525,-6.022224],[-1.260732,-2.904900,-4.581074,7.993232,8.193329,5.936147,-5.776101,6.018913,-8.939716,-3.325908,6.061322],[2.603960,-4.653225,-6.459654,-0.211030,-6.784153,-9.179042,-8.845150,-6.808309,-9.680942,5.646472,9.679670],[-4.278497,-2.033223,-2.291403,6.686148,-0.267481,6.080132,-5.495340,9.337377,-3.794881,8.478702,-5.834154],[-6.517334,-3.179590,4.367139,-5.381530,1.811839,2.284825,3.902539,-5.719858,9.370683,-6.764443,3.303391],[-8.328407,5.013351,-2.780279,4.739237,-4.894316,-8.264533,-7.895174,-3.424465,-3.478582,4.737146,-5.037948],[-3.227627,1.598367,4.698288,-4.434383,8.664206,1.089638,7.321892,8.846924,-8.872156,-7.634292,-9.420554],[-8.863021,4.509389,-3.001445,-4.426294,-1.354032,7.167470,-2.267440,5.732190,-7.348491,8.747679,3.308820],[8.405788,5.645401,-9.507351,-8.519661,-6.135556,-7.220532,-4.920510,-7.851311,9.450457,7.221271,1.350949],[3.148474,-0.701979,3.075197,4.733971,-8.727875,2.210276,-5.848883,-8.867194,2.310379,-8.596576,-0.692454],[-5.416306,1.488639,4.549749,6.576616,4.062402,1.417146,-7.802475,3.468975,3.130829,-8.764063,-1.904342]],[[8.736129,-1.989799,9.398281,-5.911379,3.659119,8.538544,-9.015199,8.607616,3.101995,-3.566394,-1.998640],[1.893897,-1.566652,6.854245,0.090676,8.225774,-0.602011,6.169256,-9.832725,-3.158605,7.578205,8.047257],[-4.776222,7.675039,1.429855,3.229544,-5.793505,6.861139,9.176445,0.364393,-9.716064,7.435820,-0.403470],[3.374447,-7.934729,-6.960187,2.403805,9.594273,-9.824535,5.523461,-0.866629,4.502936,2.937721,6.663352],[-0.817702,4.311656,-1.432629,2.359254,-0.055961,5.111108,-4.417349,-0.621245,0.252324,-9.076888,-5.789019],[6.330804,-6.219843,2.309834,-6.912115,-3.288683,9.361921,4.049863,8.177469,9.694501,9.393499,-0.661757],[-1.573234,3.604108,2.285400,-5.463759,7.663119,-3.179477,-1.635007,1.444569,5.278724,8.211396,-7.090742],[-1.839715,-3.157520,7.567635,-2.243587,9.103852,-8.288232,5.209294,-2.709705,2.207547,4.744286,8.834761],[3.023624,-7.298031,3.209556,0.867579,3.671311,2.245344,8.830276,5.054076,-2.746276,7.674867,-8.012389],[-2.074241,-5.997929,-5.407696,-0.132577,5.429053,8.072537,-2.552540,-7.366779,-4.416182,9.163616,1.727076],[-2.707606,-1.804139,2.418047,7.183351,-8.297001,4.529224,8.003502,9.469715,0.447065,2.921125,-3.773440],[4.517279,0.074749,-5.072950,5.214807,-2.413284,0.701899,1.789418,-0.214009,-7.025667,-1.030544,2.395855],[9.078868,8.543779,8.079196,3.238460,-1.182624,-7.996085,-9.259094,-2.469759,-0.928710,6.169928,-6.139238],[7.137341,6.493398,3.465709,9.678844,7.179992,2.624381,0.691143,8.680598,5.582993,-7.928762,-3.869923]],[[-3.672338,-4.524238,1.011973,-9.676051,-5.452032,-4.895057,8.330128,-9.715227,-5.368405,-8.265188,-8.072327],[-0.570709,-9.417464,-7.664922,-2.361806,-5.953759,8.123572,0.203463,-6.844354,-4.073555,8.902603,3.704290],[5.138263,1.408173,2.851962,9.819908,-6.634762,-9.958528,5.708460,3.498682,1.455886,9.530568,-1.393664],[1.059453,-0.234440,-3.357529,-0.885621,2.370296,4.411329,2.167638,-6.781166,-0.913077,-0.858427,4.204367],[0.185391,7.039792,-1.233598,-4.365008,-1.248785,-0.631324,3.192796,-2.297003,-0.208552,1.035954,3.467168],[-8.010991,-8.776879,-7.869521,3.472372,-7.006624,-7.867218,6.325809,-3.611332,8.466873,9.421078,-4.509327],[-4.733512,-3.321375,-7.338973,-6.108715,-2.827696,5.230114,-4.100741,-7.497391,4.483002,-6.734243,-6.170372],[1.590363,2.948121,4.896785,-6.191882,-6.045770,4.192232,9.615487,-5.488276,7.105986,-8.663713,4.360560],[-8.920234,9.645027,6.128243,9.468625,2.380389,-5.057414,5.731973,-6.573289,0.965151,3.974293,1.297903],[-5.882189,-7.074311,7.330915,-1.863887,8.923955,-7.274629,4.094122,1.583284,7.462782,0.196179,4.084483],[-2.285542,-8.524168,-6.036692,-6.744287,-0.936307,-0.894576,-2.185900,1.578500,-4.113268,2.782717,2.668763],[-4.683782,1.178896,-5.411741,-4.359776,0.537193,9.710842,-3.544395,1.955495,2.827335,-8.864386,3.321216],[4.370550,4.571108,4.171038,-7.903173,2.361846,5.753523,5.751172,9.639171,-2.760809,-6.811242,-0.184050],[0.871994,3.009557,2.893643,-0.402681,-6.380587,-1.277417,-5.257125,-6.337736,-2.572890,8.063782,-3.159226]],[[0.798117,-2.493117,-2.724816,0.971419,-5.705793,5.550709,-7.877380,6.889883,0.515820,-3.785223,9.961395],[3.713059,-6.261352,-6.217773,-4.945979,-6.928037,-7.740931,3.108526,4.504548,-4.309782,8.989321,0.307757],[-0.432007,6.521908,-4.900594,2.618504,-7.563688,1.541768,9.530821,-8.797897,-4.933719,0.110124,-3.940743],[0.326001,-6.562051,2.119218,3.145615,2.266990,4.549208,3.907591,-1.665772,8.210510,-0.836064,7.231853],[-0.583892,9.181795,-4.419012,-7.932571,0.715367,-6.027109,3.516985,9.708948,-3.965974,-5.727046,1.111463],[4.985551,5.596459,-3.168701,4.847924,5.181274,-4.254610,-7.211761,6.100169,0.201032,8.603068,-3.504162],[0.998106,4.926578,-1.718241,9.624622,-4.079940,-9.706786,5.069840,5.533430,-5.379185,8.037491,9.206981],[-2.251663,-0.204308,9.984833,5.179259,-6.958710,2.830399,7.200999,0.190959,-5.564863,7.823038,9.569035],[6.149219,-5.466016,4.819366,-5.122269,9.531536,-1.009676,-2.655859,4.335941,4.552696,-6.609400,-0.515982],[7.453335,-0.502497,0.896978,-0.317840,6.976133,4.126040,3.849450,2.410327,0.249819,-8.520546,-5.635228],[8.103846,6.207897,7.606782,7.478999,6.301467,9.086600,-6.306353,3.856866,-3.537595,8.640115,-0.157617],[-2.351571,-2.983719,9.118245,1.195937,-2.862188,7.379437,-2.641835,7.094042,-1.502603,-0.079936,0.919677],[-6.653355,8.122362,1.519705,-9.441556,4.656655,5.818805,-6.908316,2.532308,-4.555854,-7.253727,3.265268],[-0.279842,0.048200,5.142868,-4.966627,-5.950085,9.777673,1.979312,-9.454995,3.286436,8.257317,-2.491198]],[[1.683805,3.357406,2.251639,2.878708,-3.827877,0.889985,9.868736,1.674573,0.688817,-7.675502,9.431743],[2.815953,-3.918578,-7.977831,5.147055,3.329018,-2.398332,-4.392962,0.862494,-1.447053,9.949440,9.633240],[-4.614348,1.835203,-7.131734,-1.188457,5.833542,-6.701554,-0.148188,0.886346,7.344073,-6.823418,-5.628278],[6.701618,6.184220,1.805588,3.966297,1.279344,-4.221105,-9.289825,-1.428720,-8.357585,-0.821500,8.658218],[3.565536,9.983870,-1.225032,-5.548371,-4.371470,-1.065467,0.736730,3.851468,-3.001747,-7.468657,8.236833],[4.914702,-8.721850,6.059384,-6.507594,3.690708,-7.785894,-2.265373,8.738285,8.291840,-7.638611,1.093035],[8.083545,4.566393,1.924974,-7.918077,-2.915248,-1.590875,-2.868264,5.687812,5.050304,-4.246910,1.655933],[-5.889459,-0.406052,5.417207,0.236068,-5.451275,8.472355,-8.073705,-1.909781,3.566809,-2.984996,3.551653],[3.058957,-5.348960,5.658100,-5.257507,0.732482,5.909527,-8.476706,4.279575,2.518250,3.151870,0.526196],[2.844888,-3.570347,-1.523123,5.975169,8.896706,-4.092870,6.557061,1.376904,8.826687,-9.049791,-8.929395],[7.726525,-9.666373,7.848663,9.007451,4.618242,-2.151858,2.782995,-3.002608,-6.852446,0.073350,5.819081],[6.573719,0.809762,-0.080393,4.881919,-8.674310,-9.015554,-1.536695,-2.280211,-0.443874,-7.113604,-5.628878],[8.454585,-2.741822,-0.627421,-4.998178,-0.806303,-1.323056,-1.260985,6.677232,7.877876,-0.588860,-0.759275],[-3.463891,-6.578281,-8.438889,2.230987,-5.267715,-3.442473,8.019251,8.259237,-8.308075,7.505154,7.263253]],[[7.075703,8.541328,-3.698469,-9.617717,-9.059606,-1.675749,2.612176,-5.754740,9.175379,3.891489,6.815538],[-5.951273,1.818879,5.781641,-1.357319,-6.135695,1.876363,-8.205179,-7.270643,2.587434,8.725209,0.261239],[-5.612816,-4.789215,0.009043,7.048545,-7.007375,9.961332,2.782996,-0.453197,9.324583,1.499634,-3.209088],[-6.706283,9.050210,-2.933126,1.435330,3.839550,2.443035,5.705409,-5.861904,3.283195,7.036750,-3.068780],[4.229570,-4.195200,9.217243,-8.620386,0.772237,-5.175658,-2.625375,-1.616765,6.459101,6.889744,3.529580],[3.311079,-0.423442,-1.485351,9.420678,-3.266100,8.700271,9.516930,-1.810813,-4.426729,-2.263507,-5.471527],[0.467887,1.951559,3.958425,6.991440,1.821237,-8.285170,-0.754072,1.823351,8.239837,-0.579537,-9.471929],[9.925043,9.547869,6.836974,9.608278,-8.916830,-9.603959,5.935053,9.359590,-3.465305,0.258095,-0.822448],[8.235881,2.836171,4.067046,2.011127,7.576560,-5.029021,-4.197190,-9.813922,-8.541706,4.522032,-3.705578],[-4.929625,5.736019,7.180295,6.570042,-6.084167,1.133888,0.384080,-9.699273,7.433956,7.022044,-9.337670],[4.850127,3.937969,-0.906792,-4.436079,1.002311,-6.856578,0.839986,0.156944,2.482511,9.253060,5.888345],[9.715031,4.138273,4.423306,-0.073352,-3.190786,8.780509,5.326546,-1.728993,-5.163881,-8.571869,5.632434],[-4.243389,-3.037638,-2.817447,0.792595,-5.960974,2.535448,3.225138,1.200303,2.030220,8.079440,1.309250],[-8.564877,-1.184469,-1.983865,5.153413,-6.708362,-2.327763,4.096430,-0.181810,6.806326,4.555596,-2.011728]],[[1.158422,-3.924578,6.900664,4.070479,2.499033,0.800124,5.269598,-0.849972,4.200244,-8.766822,-0.711990],[-6.719284,-1.196748,5.800051,8.982515,-4.725833,8.023255,1.801373,-9.303856,-2.078711,-5.375585,4.867154],[0.323937,-9.874553,-6.637062,-8.888454,-3.206912,6.251688,-3.101419,-2.592263,-7.148801,0.916359,0.429856],[2.557808,9.527050,2.249702,3.556032,4.755693,7.224396,2.560327,7.773657,-2.141615,-8.137857,-4.903596],[-9.437692,-7.620034,-1.590400,0.498803,-2.862493,1.509673,-8.792734,6.427047,-3.280837,-3.659183,-3.352640],[9.126487,3.730168,7.273608,-7.592159,6.596412,-9.797703,0.885805,3.146291,0.897882,5.856451,8.958987],[5.827899,4.227124,-0.647367,3.001448,0.748906,-5.971751,-7.917932,0.253953,4.637850,-6.133349,-6.354116],[-4.999221,-2.659959,-2.656325,3.698483,6.748916,-6.766790,-2.072167,-3.423928,-9.032862,-2.054209,-9.445720],[-6.741157,7.562574,-4.769909,-6.478191,-5.968472,-8.097283,-2.739759,-3.270703,6.134416,-4.667176,5.791130],[-5.735149,7.723448,0.869745,2.116200,-6.063512,2.756447,7.432282,7.393418,3.673873,9.263970,-2.196490],[-8.762886,9.413643,-2.885315,8.225447,-7.913724,3.437213,-7.553496,0.660129,4.358515,-1.630753,-1.379226],[-1.917308,9.284840,7.279364,-1.410693,-4.368791,-4.106881,-2.002850,8.246563,-8.661979,1.684281,6.057572],[1.370473,9.049493,5.201241,8.760284,1.266135,9.209504,1.481477,0.062307,6.649906,-8.248028,5.027921],[-2.036347,5.080656,-5.275212,7.857802,-7.340583,3.383471,6.709097,3.906341,-1.655677,-6.781365,4.215722]],[[-6.239918,7.402901,-0.793663,4.901304,-6.261509,5.157730,9.615133,-5.560312,6.615450,8.407071,-1.794609],[4.092438,9.209722,2.303036,-4.117741,-4.117221,7.301973,-3.037905,9.487831,-2.503763,9.394464,8.348425],[5.728191,0.087840,9.287424,4.016573,0.363625,0.559692,-3.771079,2.354133,-2.617162,6.007650,5.453840],[2.791254,-8.179753,1.155731,5.413174,-0.521234,-5.517799,-0.951349,-9.639199,-4.343438,-8.292834,-2.924729],[-2.744047,1.298577,8.493377,-1.210691,-6.395033,-6.526477,2.544148,8.687201,-3.622638,-3.498582,1.634721],[-2.263187,-4.348512,-6.255425,5.360352,-3.028783,-1.392999,-7.548448,-1.985462,-1.121413,-0.191892,9.593763],[-3.254010,7.551026,-1.999528,-4.498246,-4.813757,1.835150,2.182043,9.752087,3.820595,-8.420305,-6.946420],[1.634397,6.710071,0.789592,-0.649761,-5.984406,2.782444,-8.827006,7.696440,-9.881207,7.962699,-8.302248],[3.495765,3.781339,7.863450,-7.809790,-0.480631,7.627787,0.127430,-9.587014,3.063569,9.028240,-6.047211],[9.805323,-9.166606,0.613037,8.404639,-0.610019,3.018962,0.005186,2.625745,-0.044497,-4.429230,2.428134],[8.950711,2.646532,-0.281822,3.509096,-8.993330,-0.634048,-0.772515,8.037166,-8.176865,-1.969818,7.219482],[-5.294209,7.536972,1.304865,-7.522448,-7.503303,-4.793677,6.895746,-4.086113,2.170970,0.674254,7.362620],[8.446735,1.246586,-2.867746,9.483909,-1.425205,-7.547119,2.079759,0.285404,-6.049872,3.962333,8.331147],[-8.337745,4.321775,9.658908,4.338164,7.004319,7.636213,-6.627917,-2.620050,5.944717,-9.260626,0.020722]],[[7.827201,9.745013,-9.190493,-5.041691,7.987543,4.040074,-0.314968,1.827364,6.280750,-1.035291,-9.171805],[-4.852620,8.135822,7.604681,0.255820,9.684824,7.248014,-2.827581,8.284936,8.334904,8.950322,9.122579],[3.926990,-2.305404,0.961139,3.135996,2.385376,3.454305,-5.641103,-5.665388,4.189049,-7.299456,5.022357],[-7.737753,-2.985416,0.404739,-9.006893,7.922790,-2.715448,-6.020965,8.383261,9.682787,1.315322,1.563356],[2.716338,4.642243,7.706819,8.772658,-8.125322,0.390875,7.798102,4.596074,2.148717,-1.663481,-1.481339],[-7.065225,-7.867521,-6.888338,-4.620227,1.508682,-3.923893,-4.888570,2.361567,-5.703265,4.165586,-8.910447],[-8.906002,-3.425354,-2.619512,1.810162,2.423993,-2.072504,2.974387,5.704392,-8.563403,2.321682,0.108268],[-1.536813,9.803656,-3.745250,-5.228348,-3.297035,-6.127176,4.894558,4.217160,1.811683,-7.084870,-9.837059],[2.339598,1.079519,0.468974,-6.881101,-5.190833,5.628950,5.784565,-1.624839,-8.331134,-6.726628,5.965211],[1.452692,9.241886,5.904324,8.084128,8.529406,5.492008,-5.755975,-3.756216,9.366436,-1.703062,-9.281952],[-2.770288,9.211642,8.009775,-4.419025,5.920954,4.675585,-8.126589,-0.078584,8.044930,-7.109111,-2.129449],[5.340219,6.834361,4.518863,3.571677,8.581377,-5.222019,-6.081196,7.075743,-3.468855,-3.791934,0.339092],[-1.422947,-0.964174,0.612588,-3.170920,-1.775933,-5.342075,-7.258545,5.574383,-2.686640,-8.754661,9.866484],[-8.496312,4.378672,-8.688194,1.118899,-2.713506,9.207390,9.286924,-3.852612,3.121510,2.913842,-2.009755]],[[6.881244,3.266486,4.551698,5.243167,-8.722823,4.084211,-5.481746,8.952926,0.910597,-5.307957,6.042729],[3.814603,2.734725,-3.026401,3.408602,7.482845,-8.122549,-7.909646,-4.655171,-8.696833,4.594419,-3.238909],[0.321741,6.409227,7.270198,-2.022799,5.045224,-7.093393,-3.352428,6.829108,-4.430689,-7.455671,6.278394],[-5.956420,-9.159664,-8.897674,-2.485423,-0.696249,2.969927,-6.638721,5.796047,6.233004,-7.484555,1.865617],[-2.917457,-3.689153,8.765203,0.293849,2.983045,-3.866581,-7.089051,-5.100088,3.982121,4.721885,-0.139090],[-1.395315,-7.993949,8.629569,8.500539,1.943773,1.127257,-5.294112,-2.427143,-1.941631,0.246509,-8.032433],[5.569634,-9.436196,0.388138,7.714824,5.905626,7.714318,2.984532,5.489077,5.102659,-5.316014,-7.999829],[-7.029460,-5.173816,2.948620,0.825777,-9.712716,-6.298903,-7.284927,-7.915824,2.054244,2.919661,4.339434],[2.605638,0.032204,7.611122,-5.921193,5.040368,-3.569234,5.493216,9.713544,8.420837,9.637462,3.378141],[6.410834,-6.756254,6.906432,1.687283,-2.668344,8.956348,-6.372151,-2.218708,7.544644,6.235784,6.976567],[5.610634,5.052337,-7.331133,-2.354547,-7.471503,8.564619,-1.624908,-6.613635,1.931095,2.415118,0.571505],[2.853089,-3.410007,9.703301,0.857506,-9.877083,0.563134,4.288674,-3.054038,7.226127,-6.644196,6.505869],[-6.120298,-3.905166,7.101745,-1.698487,6.953019,-5.209146,-7.107124,6.942816,-1.474569,-9.762534,-5.725334],[-0.682339,6.231764,0.522715,-3.673665,9.500166,2.396506,1.599493,4.326941,6.194774,3.509648,-6.048937]]], dtype = "float32")#candidate|1594|(10, 14, 11)|const|float32
bop_1595 = relay.logical_xor(call_1592.astype('uint8'), relay.reshape(const_1594.astype('uint8'), relay.shape_of(call_1592))) # shape=(10, 14, 11)
bop_1598 = relay.logical_xor(call_1593.astype('uint8'), relay.reshape(const_1594.astype('uint8'), relay.shape_of(call_1593))) # shape=(10, 14, 11)
func_1311_call = mod.get_global_var('func_1311')
func_1313_call = mutated_mod.get_global_var('func_1313')
call_1603 = relay.TupleGetItem(func_1311_call(), 3)
call_1604 = relay.TupleGetItem(func_1313_call(), 3)
uop_1605 = relay.sqrt(call_1592.astype('float32')) # shape=(10, 14, 11)
uop_1607 = relay.sqrt(call_1593.astype('float32')) # shape=(10, 14, 11)
output = relay.Tuple([bop_1595,call_1603,uop_1605,])
output2 = relay.Tuple([bop_1598,call_1604,uop_1607,])
func_1617 = relay.Function([], output)
mod['func_1617'] = func_1617
mod = relay.transform.InferType()(mod)
output = func_1617()
func_1618 = relay.Function([], output)
mutated_mod['func_1618'] = func_1618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_1670 = func_194_call()
call_1671 = func_194_call()
output = relay.Tuple([call_1670,])
output2 = relay.Tuple([call_1671,])
func_1684 = relay.Function([], output)
mod['func_1684'] = func_1684
mod = relay.transform.InferType()(mod)
output = func_1684()
func_1685 = relay.Function([], output)
mutated_mod['func_1685'] = func_1685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1617_call = mod.get_global_var('func_1617')
func_1618_call = mutated_mod.get_global_var('func_1618')
call_1688 = relay.TupleGetItem(func_1617_call(), 0)
call_1689 = relay.TupleGetItem(func_1618_call(), 0)
const_1694 = relay.const([[[-6,9,-3,4,-4,4,-6,9,4,-4,-9],[6,9,-8,-1,-4,-1,-9,-9,-8,-7,-9],[5,3,-3,-4,8,-8,10,-3,-6,10,-9],[2,1,1,2,8,-7,-7,-10,3,-2,4],[7,-5,-6,10,3,3,4,1,-5,-3,2],[3,4,-1,-8,-10,-4,-10,1,6,-4,7],[5,3,-9,-4,-8,-4,-4,-9,-9,9,-4],[-2,1,-1,8,-2,-6,-5,-1,7,-8,10],[-3,8,9,-5,-8,-10,-6,-1,-8,7,8],[-10,-3,-6,5,4,-6,2,-10,8,6,5],[8,-6,1,-10,-5,7,5,-8,-1,2,5],[-5,-1,-2,-1,-8,-5,5,8,-6,-4,-1],[-4,3,3,5,1,4,-2,-8,-5,4,-1],[-7,-2,1,6,9,3,7,7,-8,1,10]],[[-2,8,9,9,-1,-8,-1,-1,3,9,1],[-5,-8,-9,-9,-2,-1,8,2,-9,-6,-8],[-10,-6,-10,-10,-10,3,2,-9,-3,9,3],[4,-7,-8,4,1,-6,6,1,7,2,1],[2,-4,1,10,3,9,9,-4,-5,8,2],[-7,1,-6,6,9,-7,4,6,-4,-8,-10],[2,1,-9,-1,2,-5,4,5,7,9,-7],[-2,4,4,8,-8,-8,-2,-7,-9,2,9],[-3,7,8,-6,8,-8,5,-4,-5,-5,-3],[-3,9,1,-6,-9,-7,-3,-4,-10,8,-5],[-1,5,-5,-1,9,-1,6,2,-2,-2,-7],[4,3,-4,-3,1,-9,-1,9,5,8,8],[9,7,-1,2,4,-1,-1,10,-5,-1,-9],[1,4,8,3,7,8,-5,5,-8,5,-7]],[[-4,4,8,-4,-6,7,-2,-6,-2,6,7],[8,-1,10,-6,4,-4,1,-4,10,-9,-3],[-3,5,2,-7,5,10,4,5,6,1,-10],[3,7,-5,10,7,-7,-1,4,-7,-3,-8],[-6,8,2,4,-2,-5,2,-5,-8,-6,-5],[-5,4,9,-8,6,-1,7,-4,5,-10,4],[2,4,2,-6,-8,-5,2,2,2,-3,-2],[8,1,-3,6,5,-7,-10,9,-3,7,-9],[-3,-9,9,-1,2,9,1,-8,-9,4,10],[-4,-10,-5,-6,-9,5,7,-2,9,6,-9],[9,-5,-10,6,-3,-8,7,3,10,-6,10],[3,10,7,-9,4,-6,8,-7,6,5,4],[-9,-9,9,-6,-7,-10,-8,-4,5,-6,-6],[-5,-1,5,-6,1,-6,-4,4,-5,-8,1]],[[-3,-4,-4,9,7,4,-4,-7,10,6,6],[2,-10,4,-1,6,1,-2,4,-6,-5,10],[-1,-2,3,-6,7,-3,-4,-9,-4,-9,-6],[-10,2,1,6,7,-8,-6,-6,-2,-10,-2],[-5,-9,5,-4,1,-3,-7,10,-6,1,-5],[-7,-9,4,7,6,-8,-9,-5,5,-6,-8],[-3,-8,-5,-4,-6,-1,-1,8,4,10,-1],[4,3,-1,-8,-3,5,-3,-10,1,10,-5],[-9,-1,-7,5,-9,3,10,10,-2,10,-4],[-8,-10,4,-10,-2,-4,-4,-1,8,-7,3],[-6,5,6,5,-8,6,-1,7,1,-2,10],[5,-4,5,-5,-1,1,-9,3,7,-7,9],[-7,-7,6,3,-5,9,-3,-3,3,3,1],[-9,6,-6,-2,10,3,-10,-9,5,3,-3]],[[8,-7,1,-5,2,7,-1,-2,9,-4,9],[9,7,2,-8,6,-3,7,5,-6,-5,6],[7,-2,-7,-9,10,-4,2,9,-1,7,10],[-5,5,1,-4,9,2,-8,-8,5,6,7],[5,9,-10,7,-10,4,-6,7,-9,-3,-10],[2,-9,7,6,3,-9,7,-7,-1,9,-4],[8,6,10,10,2,7,9,-7,8,-8,2],[-6,10,-10,3,-5,-5,-10,-10,-4,-2,-6],[-3,-8,4,-5,1,-9,-1,3,1,4,-9],[-1,-7,-1,-4,-2,9,7,7,-2,-7,3],[-10,-1,2,-6,-2,-2,-4,9,-10,-6,-10],[6,6,6,-9,-1,-5,1,-10,10,6,2],[-5,-9,-2,5,7,-9,-9,6,4,-8,-10],[6,-6,5,-8,-3,7,-7,-8,-3,4,-9]],[[9,-3,-3,-3,10,6,-8,9,7,9,5],[-7,6,7,1,5,3,2,8,2,5,-5],[8,-8,-7,1,1,-2,-7,9,7,8,1],[-8,5,9,6,2,-8,-1,5,7,-1,5],[10,-5,-9,8,3,8,-6,8,1,-7,10],[3,9,5,9,-5,-5,7,-3,5,3,-4],[2,-10,-3,1,-3,1,4,-2,-6,-1,9],[-7,5,10,5,6,7,-10,10,-4,-6,7],[-8,3,9,-7,4,-3,-5,-6,9,10,7],[-4,1,-4,-2,-9,1,6,-3,-8,-6,5],[-6,-2,2,-10,-1,-8,2,-1,2,-5,-9],[-2,-4,1,-5,-9,-9,5,2,2,10,8],[-9,-6,-7,5,2,10,2,-5,-8,-6,-9],[8,-6,7,-10,8,1,2,5,-6,5,-6]],[[-9,-3,-7,-6,2,8,-6,-4,9,8,5],[10,7,10,3,-10,7,1,-2,10,1,-4],[4,-5,-9,3,-1,8,8,-2,4,-3,-5],[6,-1,3,-6,-1,4,-3,7,9,-8,9],[-4,7,5,10,-6,9,-3,-9,9,9,-6],[-6,-8,-4,-3,10,-6,-7,9,-10,4,-2],[10,-5,-3,-2,-9,-5,-7,-1,4,8,-2],[-8,4,8,7,-4,1,-6,6,-5,-10,1],[-9,-6,8,10,10,-3,-8,-10,-8,2,6],[6,-7,8,-1,-5,-5,-3,6,5,3,-10],[-6,8,7,-5,-9,6,4,-5,4,5,-10],[4,-4,-10,4,10,2,-4,-7,3,-4,1],[-2,-2,6,-8,8,10,9,-8,2,3,-5],[3,9,-7,-3,-10,-5,-3,-2,7,3,1]],[[-7,-2,-9,3,3,-6,-1,3,1,1,6],[9,7,9,1,-9,-2,-7,8,-7,-5,-5],[-5,-10,-4,6,-7,9,1,1,7,-2,2],[10,-9,-3,9,3,-8,4,-6,-1,7,8],[-7,10,10,5,-1,-4,-3,7,6,-9,4],[6,6,-4,7,-9,-10,8,-10,4,9,2],[-8,3,-10,10,-6,4,6,-2,-10,7,1],[2,10,3,-7,-1,-3,-8,-9,-6,7,-6],[6,5,-3,7,-10,5,6,-1,-10,-5,9],[7,6,-2,3,-7,9,6,6,6,-2,-10],[-7,-9,-5,4,-2,3,-4,10,-6,8,-10],[-7,-10,6,2,-10,9,7,-8,10,-2,5],[-10,7,5,-9,-2,3,9,-3,5,1,-5],[-8,1,-10,-10,3,3,4,-5,-2,1,-10]],[[5,1,-7,6,3,6,1,-7,2,-1,-9],[-4,1,-1,1,3,5,8,8,-5,-7,5],[6,10,-3,6,9,-6,5,-3,9,6,3],[7,7,4,-4,1,2,-1,-4,9,-6,-6],[-2,-9,6,-8,-9,-10,-8,10,3,3,5],[-4,-8,4,6,7,8,1,-3,-3,-4,9],[-7,-6,-2,-10,3,-10,5,-7,6,10,-1],[-10,-10,9,5,-7,-8,-5,-2,-1,-8,-5],[7,-5,5,-6,6,3,10,3,-9,-10,-5],[-9,-9,-1,-1,2,-10,8,-2,-4,-2,-6],[6,-8,2,-1,-2,-4,-1,9,-3,8,8],[1,-4,-8,-1,-1,-6,3,6,6,6,-10],[-7,9,-2,7,4,-7,4,-5,2,3,4],[7,-10,9,-5,3,9,-3,-8,8,8,-10]],[[-5,-7,-2,6,-6,7,7,4,-4,3,-8],[2,-9,-9,10,-1,-8,-1,-1,-8,9,3],[-1,8,-3,-7,-9,8,-3,-7,6,-7,8],[-7,-6,-4,-10,3,-5,5,1,-10,4,10],[-4,-10,5,-7,7,2,6,-8,-6,-6,-1],[-10,4,5,-5,-5,4,-9,3,3,-7,3],[2,2,4,8,10,2,-5,3,-3,-9,6],[-5,-6,-10,3,8,9,-3,7,-10,7,-2],[8,4,-6,8,3,-10,6,-1,5,4,1],[-7,-9,7,9,-10,-7,-8,-7,6,4,8],[7,-8,-1,6,-2,-10,10,-8,-9,5,3],[10,4,10,3,7,-7,2,-1,-10,1,-5],[9,9,-4,-5,-8,8,2,-9,8,-3,-4],[5,-3,-8,6,5,-9,-3,-9,-3,-5,8]]], dtype = "uint8")#candidate|1694|(10, 14, 11)|const|uint8
bop_1695 = relay.greater(call_1688.astype('bool'), relay.reshape(const_1694.astype('bool'), relay.shape_of(call_1688))) # shape=(10, 14, 11)
bop_1698 = relay.greater(call_1689.astype('bool'), relay.reshape(const_1694.astype('bool'), relay.shape_of(call_1689))) # shape=(10, 14, 11)
func_1413_call = mod.get_global_var('func_1413')
func_1415_call = mutated_mod.get_global_var('func_1415')
var_1701 = relay.var("var_1701", dtype = "int16", shape = (936,))#candidate|1701|(936,)|var|int16
call_1700 = relay.TupleGetItem(func_1413_call(relay.reshape(var_1701.astype('int16'), [8, 9, 13])), 1)
call_1702 = relay.TupleGetItem(func_1415_call(relay.reshape(var_1701.astype('int16'), [8, 9, 13])), 1)
output = relay.Tuple([bop_1695,call_1700,var_1701,])
output2 = relay.Tuple([bop_1698,call_1702,var_1701,])
func_1710 = relay.Function([var_1701,], output)
mod['func_1710'] = func_1710
mod = relay.transform.InferType()(mod)
mutated_mod['func_1710'] = func_1710
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1711 = relay.var("var_1711", dtype = "int16", shape = (936,))#candidate|1711|(936,)|var|int16
func_1710_call = mutated_mod.get_global_var('func_1710')
call_1712 = func_1710_call(var_1711)
output = call_1712
func_1713 = relay.Function([var_1711], output)
mutated_mod['func_1713'] = func_1713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_959_call = mod.get_global_var('func_959')
func_960_call = mutated_mod.get_global_var('func_960')
call_1732 = func_959_call()
call_1733 = func_959_call()
func_280_call = mod.get_global_var('func_280')
func_282_call = mutated_mod.get_global_var('func_282')
const_1772 = relay.const([-2.160276,8.896613,4.481852,-0.454562,-0.529202,9.842326,8.663191,-2.638790,4.400571,-0.424529,-1.957828,-4.302830,5.272186,7.166186,6.912878,-4.125200,0.266650,-9.415096,1.356524,3.081391,-5.050055,1.018499,0.713955,3.343322,-2.160293,8.136170,9.814645,-3.666773,-4.957476,9.581265,5.162636,5.558159,5.867050,0.712662,6.862523,-2.979292,5.295503,8.844427,1.098857,-3.092511,-7.119063,-1.926574,3.817103,-9.655576,1.440987,6.141953,-6.554358,9.691164,-1.174477,-9.368267,-2.381465,-0.817181,-8.593654,-1.035385,-8.830695,-2.812316,-3.942696,-5.173966,0.359925,-1.542127,-1.249684,5.989515,-2.356884,-2.161652,-8.351467,-4.052807,-9.522802,-6.504865,-9.240964,-4.642825,3.874136,-6.377713,-2.669559,7.149282,2.405202,-2.079316,1.986265,-9.486253,-1.826256,2.748466,1.413798,2.329459,-9.125023,5.830082,-4.429662,2.346549,-4.315939,-4.844485,8.646021,-4.628815,3.624731,-7.198558,-2.868289,-5.965347,-3.057012,8.496954,-1.646552,3.555748,6.436265,1.769767,-3.316275,3.205873,-8.153111,7.166356,-5.631947,8.168973,-0.156473,-1.566201,-7.133569,-0.838086,-2.395223,0.384721,-2.097532,3.624964,5.839715,-3.929696,-0.683655,-7.331469,0.491433,-9.962617,3.253644,2.890740,2.415148,-1.687292,-7.873571,-1.104585,0.584878,3.853216,-5.405175,4.735679,-7.674340,-6.889673,9.039348,4.774139,-3.202242,-0.873671,0.954474,-5.890258,-0.271328,4.309001,0.529521,9.892887,1.154056,-3.944222,-1.388542,3.890344,3.532605,5.952040,-5.117914,8.953838,-8.948715,-0.203137,9.815757,-0.484959,6.445538,9.049177,-3.574668,6.912442,9.011174,7.311448,6.922398,-6.976273,-8.957542,-0.450019,5.629638,-5.917967,4.402712,6.449963,9.214846,-2.791830,8.631133,1.636339,0.916298,9.573950,-3.880184,-1.341636,1.196051,0.220332,-1.115912,-2.485826,0.876561,5.153840,3.758626,-2.818244,-9.441105,-8.456432,-5.981906,6.061208,-0.734828,-9.879061,-1.313405,6.399310,-8.552677,3.190595,-0.662186,-0.783524,-1.676963,-8.247186,-9.494313,-6.644477,-7.021658,2.747256,-6.382711,-0.773559,3.571897,-3.041410,5.327234,-8.932262,-9.342909,-1.135751,1.609404,-1.029226,-8.746008,-7.063667,1.808075,7.622188,8.480088,-8.873404,-4.953259,-3.303095,-9.211317,2.012113,-0.093234,6.747673,0.051119,7.308022,-3.958587,5.965172,4.019399,8.913663,-7.362115,-2.625586,6.488783,-4.416321,1.060061,-8.282808,4.130752,6.060529,4.895041,-5.198012,-4.286875,0.264271,7.580732,5.006819,-2.084640,-0.288328,6.079723,-8.238933,6.194596,-7.854954,-2.002406,-3.974291,-5.882477,4.448971,-3.526476,5.325266,-5.677376,4.741475,2.240771,-6.343627,-7.307893,-5.652528,5.478348,-5.808348,2.006188,7.178892,9.850171,2.435472,0.823144,0.204762,-9.217929,-2.306206,-4.156540,9.529932,-4.988277,3.129243,-6.735011,-6.700827,3.150599,-8.804741,-3.687638,-6.551293,-1.486575,5.957446,-2.450090,5.263752,0.825804,9.120874,-4.405525,8.616313,-0.892173,0.209224,0.198728,-9.092866,-7.619551,2.114386,-9.574306,7.632091,-4.987346,-8.148365,7.102656,7.707147,9.832725,-2.400167,1.854843,-6.201972,3.995174,-0.228516,-8.408777,9.410755,-1.795711,5.937482,-3.488171,8.605131,0.165123,1.786545,6.327813,-6.403464,-3.582382,-1.839050,-0.564284,4.536699,-6.855292,-3.544445,9.937836,-0.782871,7.227721,-4.953360,-1.952152,-0.616946,-8.562210,-3.544872,-9.652017,-1.366869,-2.250617,6.443243,-1.896954,-0.410273,-4.922265,6.257885,-8.710257,9.960224,0.160472,4.416148,1.622564,1.073030,3.535980,-1.403755,-7.663148,-2.174838,9.993054,-1.386190,6.750679,5.112155,8.594984,1.507421,-0.506145,9.837136,-1.467796,3.338121,-8.720340,8.464468,-8.869934,-8.606526,2.178616,6.266818,-7.694778,-3.434337,-1.237905,1.226193,-5.921876,7.837125,-5.006672,-7.928757,3.851779,-5.199959,-1.183600,-7.035794,0.348333,-4.868309,0.813460,-6.661408,8.393261,5.570867,-2.274611,5.522597,9.734236,0.517627,-7.946063,4.835177,7.423266,2.651334,4.424473,-9.494353,-6.309047,4.741700], dtype = "float32")#candidate|1772|(396,)|const|float32
call_1771 = relay.TupleGetItem(func_280_call(relay.reshape(const_1772.astype('float32'), [4, 9, 11])), 1)
call_1773 = relay.TupleGetItem(func_282_call(relay.reshape(const_1772.astype('float32'), [4, 9, 11])), 1)
var_1777 = relay.var("var_1777", dtype = "float32", shape = (4, 9, 5))#candidate|1777|(4, 9, 5)|var|float32
bop_1778 = relay.power(call_1732.astype('float64'), var_1777.astype('float64')) # shape=(4, 9, 5)
bop_1781 = relay.power(call_1733.astype('float64'), var_1777.astype('float64')) # shape=(4, 9, 5)
func_1311_call = mod.get_global_var('func_1311')
func_1313_call = mutated_mod.get_global_var('func_1313')
call_1782 = relay.TupleGetItem(func_1311_call(), 2)
call_1783 = relay.TupleGetItem(func_1313_call(), 2)
func_926_call = mod.get_global_var('func_926')
func_929_call = mutated_mod.get_global_var('func_929')
const_1785 = relay.const([[-4.997120,9.426716,-5.508418,9.908250,-1.842796,-9.834627,-7.956885,1.595365,-4.994867,-9.425038],[-0.169548,-1.241910,9.712034,8.958396,-4.461341,6.521703,4.513899,-6.608316,-4.495121,0.151338],[-8.653987,-9.464884,-6.825741,9.495885,-7.764622,3.927254,-9.299839,-3.165278,0.417925,-3.042906],[-0.738907,3.448833,-0.508399,4.454221,3.377346,6.465012,-7.347427,-3.372480,5.435806,4.946376],[6.382284,7.343710,0.768565,3.390654,9.797621,-7.002567,-9.081780,-4.313784,4.098853,1.256056],[-4.033387,-2.424061,5.305135,7.806566,2.736424,-6.032916,-5.505413,-6.401785,-2.476073,-2.884822],[7.120454,7.364747,-0.742911,-2.804272,3.741745,-0.368677,8.356615,6.029092,6.382403,0.116312],[1.574544,7.334180,8.490656,8.572747,-7.420551,-4.098473,-1.776670,3.692457,4.206796,-1.683416],[2.032605,-0.176019,-5.919156,3.523133,1.806051,-6.036400,6.138946,-8.265650,0.191597,-0.302840],[4.901842,-3.172918,-2.115109,5.341515,8.913567,-8.225091,-4.143505,4.126982,-0.912475,6.773278],[-3.801564,4.824889,8.974193,-3.095196,7.127846,-2.923673,0.506764,9.727588,-6.076969,3.881212],[-3.357938,9.948451,0.810453,6.093238,5.011838,9.611956,-9.994377,6.905531,-2.376978,2.710062],[-9.858989,-1.945500,-9.134919,2.316549,-6.398401,-3.342925,1.418444,-0.443428,1.987126,-0.772706],[-2.336471,-3.247763,-0.367520,-9.871801,4.381260,4.181791,-2.195111,-6.402038,2.056747,2.582151],[-2.399127,-4.850919,2.439416,-4.055797,9.453602,-9.646430,-5.244409,-9.848770,-0.006871,8.752501],[-3.904243,-1.536974,8.252529,2.333063,-7.801320,-5.516487,0.136333,-9.931991,2.815212,6.296587],[-2.055293,-5.091453,-9.224238,9.218909,-8.955232,-0.382083,9.233350,9.598553,7.699956,8.094972],[0.744948,5.130186,1.236383,-1.579067,-4.358217,4.865524,7.303483,-1.517436,-0.173185,-1.139347],[-1.895689,-3.821592,3.843633,-7.654035,-7.154046,1.435400,-2.565101,-6.139757,-0.930515,-8.688243],[-0.068333,2.767079,-2.084531,4.133495,-7.797724,4.127802,4.954311,-4.430276,8.228635,7.843845],[7.255894,9.289175,3.255579,9.056188,-7.747689,1.708564,5.158095,-8.725565,-4.775122,-4.315883],[-2.707346,4.950669,2.202047,-5.375834,1.033693,5.792683,-1.919450,-2.890852,-4.424601,-0.336133],[2.081987,-0.829553,-0.870294,-2.445615,-2.300732,6.182390,-5.222663,-2.086412,9.478984,-5.837185],[8.022171,2.765536,6.221148,0.791173,0.581128,-4.885730,3.417267,4.195340,-8.182808,-4.026352],[-7.374550,3.245321,8.753046,9.781046,-2.421249,1.975118,1.106754,-1.880928,-5.013587,-5.860014],[8.452851,-2.353484,8.996681,-0.745972,-6.718498,2.373768,5.173425,9.457849,-3.898388,8.042909],[4.259180,-7.669963,2.987399,1.615205,9.968206,8.611102,-2.385093,1.989325,8.225405,8.246398],[4.922896,-9.939604,6.178727,3.111202,-7.930745,7.328086,8.928007,-7.816063,-8.567787,-6.804768],[-2.355475,-1.443667,0.755318,-8.651563,8.894885,-5.527193,-5.454270,2.480446,8.590347,-2.021541],[4.254470,7.993650,6.556476,4.622369,3.827151,0.970928,1.958511,-7.479028,-5.515458,2.863601],[8.113826,-0.709211,4.006273,4.881074,-1.252687,-7.132977,7.007411,-6.599498,-6.130810,-6.170385],[8.747740,3.204669,5.512536,4.439987,-0.777340,-6.132156,4.149999,-2.818954,-0.949866,8.630000],[8.002332,6.552448,8.280022,1.736734,6.664823,8.845285,-6.738597,-6.332026,-5.263939,5.186595],[-7.881729,-2.892973,-8.466004,-7.541023,3.827027,5.244453,-3.372706,1.994859,-0.926338,5.923161],[0.739037,-4.003037,1.735308,1.864267,-5.202235,-2.856366,-5.921321,-2.619638,8.399098,-2.482654],[-0.836310,5.323220,-0.346912,-0.078613,-7.731706,-7.008559,-0.906130,9.794001,1.421140,-6.608655],[7.989085,8.952542,2.402254,-8.464789,-9.759815,7.651846,-5.197966,0.382454,-5.523628,3.331638],[7.472043,-8.367400,-5.630855,2.335902,-4.322169,9.248498,8.994217,-7.639717,1.043723,9.775887],[5.312697,-0.737766,-6.829683,-5.484058,-1.921455,7.433651,3.677401,0.094300,0.199003,-5.042018],[-7.800881,7.020190,-5.938410,5.059334,-3.771560,9.648947,1.514195,7.353451,-2.149932,-0.530794],[5.669906,-7.502211,6.198431,-2.450056,4.471602,8.599909,-5.068772,5.993101,-9.307399,-5.922661],[4.510823,-4.237786,-6.953711,-1.308704,4.987569,7.944810,-8.401384,0.404308,3.208112,-9.172267],[-0.501596,0.712816,-7.472686,9.728606,7.904347,9.665303,-9.620889,8.014450,6.787760,5.186769],[4.528198,2.530708,-2.203474,9.589358,-7.201048,-5.292348,9.562295,-3.408015,-8.571036,-4.152982],[4.822335,0.411135,5.853817,-0.207378,-6.120569,0.215254,-2.936320,-2.100791,-2.197581,8.069448],[8.508674,4.058085,3.425441,1.412154,-6.582417,6.711673,8.499924,3.833811,0.752603,-3.977429],[2.815460,6.213805,-1.412069,-9.122697,-8.846865,-7.885302,-3.868943,-8.803235,5.706946,2.677460],[-5.697606,7.589536,5.885786,-3.133326,3.583076,8.737062,5.109810,-0.241879,-4.184524,-1.076117],[-4.885793,-1.973428,-4.048938,-4.874610,-6.914151,6.548440,-4.372592,7.571506,7.782813,9.398956],[-8.769450,1.659800,0.970586,0.976606,3.731259,-5.474384,-6.189518,-7.689207,-9.507712,-5.907910],[-7.252668,3.730515,6.731279,4.368125,-7.888225,9.023773,2.911729,-3.765533,-8.755842,-5.859534],[8.754573,-8.121028,2.924153,6.772103,2.891879,8.558471,9.885610,1.998349,9.336323,-6.010692],[6.758637,-6.838046,-4.484687,3.460527,-5.007624,-3.536031,6.700273,-0.436862,4.540545,-1.515145],[4.929060,4.512066,-4.105087,5.553327,3.439944,7.046867,5.516536,1.854154,3.423041,5.565068],[-9.393935,7.042778,-3.168966,-8.534366,5.516825,-5.420407,-8.926645,-8.894723,-7.201406,-5.213086],[9.487709,-8.904468,8.500945,-9.073728,6.003234,6.528890,-1.199035,9.278943,-0.389650,-1.123689],[-7.875750,-2.603641,-6.590649,8.706723,0.278141,-5.534650,7.233339,1.591400,-0.464441,9.832322],[3.164028,3.574126,-2.769447,-1.509615,0.192956,-2.459014,-0.553552,-4.677176,9.772273,0.586491],[-0.755270,6.351389,0.595144,-2.042421,9.723852,6.381942,-7.380567,-3.488337,7.115270,3.782297],[9.503095,-4.493093,3.175710,8.534138,-7.428517,8.606565,-2.111416,-4.949080,4.231773,-0.710228],[0.222074,-7.489196,-6.678771,-6.185871,4.518714,-6.848912,3.516147,-9.564338,-5.508821,-3.935715],[3.347029,2.672559,-1.127182,7.236689,-3.266850,-8.399741,6.323210,-9.042215,3.557063,1.773948],[-7.991696,-0.331530,-4.240385,-1.450261,-5.852782,0.689492,-9.977310,6.061125,-3.055705,0.667841],[-7.131723,-0.410858,-6.708585,-9.390904,5.519282,-1.757973,9.678825,-3.273605,-2.177475,-8.167597],[9.408706,-4.086723,-7.636212,-1.664031,-5.621409,-5.280111,-3.402295,-9.175993,3.606186,-7.680949],[-9.037534,-7.049252,1.615009,1.872660,-9.894897,-4.636355,1.494118,0.735320,9.626657,-6.133961],[7.511345,-0.442110,-9.134716,-4.935584,2.679453,-1.017404,-6.472970,-0.708111,9.760066,9.649386],[7.572686,4.943624,-7.069094,5.329816,2.570181,5.393912,-5.367087,-5.808872,-9.353940,-8.242843],[7.269235,9.169761,6.641125,-1.789274,8.088456,-4.783313,2.670921,0.366727,3.846252,2.943831],[-4.739191,4.552920,4.273007,3.583227,3.268430,4.298633,0.468849,-3.820870,-2.576743,6.775434],[-3.688552,4.158822,-8.387707,2.011830,3.888718,-6.262957,1.563784,-6.719246,5.532523,-9.713507],[7.135327,8.619602,-9.974781,2.919750,-2.402534,-7.537251,1.858234,1.120076,-0.219463,3.199334],[5.255827,4.151100,1.530271,9.717167,-4.900625,2.057987,-3.260785,-7.601730,-9.283262,9.650666],[-4.394131,1.855661,0.830888,6.740231,8.362998,6.178511,-1.669000,6.304548,-3.614132,-7.291732],[-9.985831,-2.017124,3.492490,3.978103,2.985839,-9.962952,-6.276232,8.705262,-0.447792,0.727868],[2.953422,4.469026,-3.989258,8.447142,2.549580,3.353857,-0.527148,-5.970045,-3.772009,3.606271],[6.206773,5.727877,-3.576324,0.155806,-1.126668,-2.516404,-3.085041,4.370656,8.677917,4.911340],[4.605559,-7.284049,2.579829,6.502011,5.600110,1.199217,-3.699074,-6.317753,0.557855,-3.390838],[7.491357,7.155794,-8.943016,-3.144080,2.130294,-4.513852,-8.972256,-8.249970,-8.045673,5.052483],[2.910412,-2.724431,1.120607,-3.129667,-2.410966,-6.518632,4.661455,8.987039,2.459766,8.781204],[-7.003294,9.802376,7.626980,-0.004707,7.730535,4.545967,-2.794162,-0.288809,-9.417501,-0.968388],[5.305718,-2.519437,-7.916333,-0.167502,2.260110,-6.134148,-3.464315,-9.605543,-7.553354,7.150269],[-8.888547,-9.220625,-4.159172,2.277692,1.413689,7.466617,-6.613328,2.202798,-5.830069,-1.578748],[-0.603595,4.776108,-3.489963,-1.044124,-9.250240,-3.465719,-3.315746,9.190736,-8.369161,0.233090],[-4.845876,-1.776048,8.703430,5.872415,-4.048808,5.403308,-7.469298,9.884975,8.180774,3.597850],[8.411545,-5.036631,-1.001328,-1.250888,-8.358318,-9.182715,-3.801919,-9.042142,4.616804,8.943684],[5.347642,-6.923820,4.296619,4.929330,4.472763,-7.222947,-7.531839,-6.765141,-4.150653,5.788572],[-4.215099,1.499035,8.575038,-0.148752,7.848363,-1.735469,2.412469,6.148321,-7.970082,8.251923],[4.535122,-7.802712,-6.034100,8.048020,1.040599,-9.151187,-7.403543,-0.885412,8.016687,-3.680556],[9.363567,6.074287,6.937526,1.891535,1.189012,5.536854,8.668956,4.997162,-6.304919,-8.949685],[0.192321,-9.991537,5.410058,0.547555,0.471650,0.757723,-2.224458,8.423566,5.788665,2.679312],[9.184418,-1.350772,-7.629069,1.226060,-3.458424,-8.463721,-3.609791,9.230570,-7.310174,-3.392016],[7.003007,-5.864120,-9.153975,3.786270,-3.412355,2.945897,-4.099690,-8.360126,9.673821,0.762573],[-6.270403,2.886272,-7.495313,-7.636099,-6.082622,4.146596,-8.319329,7.954307,3.667835,6.018077],[-3.770311,-8.320620,-3.757213,2.258292,-4.196740,8.190899,2.739264,2.283850,2.226507,-5.376317],[-1.063872,7.557779,0.119566,0.266694,-3.386567,-5.267908,7.993200,6.618340,-9.315988,8.997689],[1.488794,9.116201,-1.262393,1.182140,-9.635731,7.144116,4.087529,2.406243,3.696769,8.042866],[1.915719,-3.239560,-3.726063,-1.946128,8.366990,2.105456,-8.131310,0.013036,2.083517,3.216981],[-7.928616,-5.784346,4.068141,-3.252026,9.150073,-0.057284,9.832805,8.482760,-1.843697,-6.689501],[-9.848872,4.713072,-8.401410,0.988325,1.979683,6.796654,3.142976,8.701127,-0.128255,2.786196],[1.588830,-6.010816,4.200507,1.657883,-1.744885,7.493442,0.672704,8.443202,3.937596,-2.733557],[6.072554,-9.130918,8.964608,-4.973536,8.959626,6.323480,0.649290,0.801764,-2.206314,5.766671],[7.599541,3.425417,6.717926,-0.520212,7.983494,9.030329,8.126194,4.953154,7.348782,-2.771466],[1.687903,5.437107,1.931784,2.664900,7.664783,-4.183327,9.965545,-5.350309,5.700279,1.379954],[7.363542,4.826799,-1.506534,8.188897,-8.476801,-6.379911,-3.127059,3.793641,0.047621,1.228134],[9.775985,8.376322,3.462298,6.257276,-8.352042,7.875909,5.397343,-0.058686,4.292111,2.205468],[3.483537,5.121704,3.836495,-4.063751,-5.170930,-7.555868,0.523075,-7.198213,9.813610,3.656710],[2.370499,4.821335,-5.017033,-7.713352,4.478060,3.841398,-7.554753,-9.022472,0.471370,-2.495561],[-1.807440,1.532814,-7.587288,-3.120727,2.694123,6.218220,-9.628038,7.024134,2.914536,-2.501358],[9.528253,2.259315,4.073627,-6.220109,-7.703986,-5.474004,5.231330,7.122329,2.750754,7.464112],[1.780476,6.919987,6.653670,-7.403125,9.614532,6.876261,5.942125,-7.638524,7.767945,2.024990],[0.598048,-8.602887,-3.367085,-0.736063,-2.484329,-6.296585,-4.755570,5.190502,9.391740,-6.980697],[1.448570,5.866471,3.315082,2.574470,-6.795605,-9.051943,-7.005479,-6.588385,-1.797257,-5.324224],[-3.032502,8.723772,6.211560,-2.053301,-3.959963,1.392586,6.387847,-1.716427,-3.093884,5.011954],[2.968966,-6.169619,-7.427712,-1.535411,4.085648,3.572727,1.760504,-6.004197,-2.266123,7.472782],[-4.294994,-3.883544,-5.122247,-0.172133,-6.646689,9.410404,6.121809,1.092077,0.662251,9.026612],[-5.565957,-7.866598,0.797114,-9.076486,-9.731915,-2.003596,-7.789081,-5.998412,-1.572047,6.115303],[-1.229438,-1.934916,-5.301935,4.743374,9.857333,-7.194967,-0.634255,3.667088,-3.094161,2.846837],[-1.827898,4.788499,-1.062364,1.973341,-7.234555,2.398922,4.692465,-2.681754,4.906869,7.246503],[-8.413402,-9.832288,5.538344,-3.918585,-4.890710,-6.260168,-4.911136,3.481485,4.512001,4.625951],[-5.301779,-8.751291,-9.168798,3.702104,-1.858437,-0.896510,9.095288,8.631972,-0.357868,-6.655033],[4.848702,3.776305,-8.514707,-6.292211,7.849264,0.537138,-4.787805,-4.221797,-1.731430,-5.164647],[-3.876013,-4.475026,-8.847178,-9.584087,0.227868,4.155260,4.719580,-9.811352,1.405491,7.407924],[-5.555810,-3.869951,-8.341739,1.567837,5.039057,-8.426229,-1.574441,6.490290,-9.434982,-4.879524],[-7.221680,7.881036,-9.990829,0.307953,-5.565083,3.362961,7.898336,-5.029151,-1.968396,-2.461511],[3.265394,1.334573,0.438668,-8.965929,0.134384,-2.533022,-8.374265,0.862851,1.745544,0.439605],[-4.210044,4.878833,-3.423680,6.050296,9.836717,-5.370797,-9.428633,3.871766,-5.605323,-6.474289],[-6.004929,5.365354,-4.211131,1.354083,7.516834,8.867705,7.489713,6.060767,-0.544725,-8.850038],[8.229170,3.464553,2.038265,2.726023,-4.094130,8.844442,-7.835155,-8.732828,0.191562,3.847763],[-4.397747,-3.520706,8.570049,4.998452,9.118936,7.930380,9.459802,-0.902790,0.327416,-3.294609],[1.853137,-2.770344,3.480019,-7.432130,1.208648,7.647037,1.896026,2.845180,-0.245563,-8.386185],[8.351566,-2.595090,-8.201590,9.328338,-3.688665,-1.679621,5.627715,-9.004320,9.163873,8.525169],[-9.791973,-8.182549,7.728734,-0.683469,-1.758060,8.296827,-2.216252,-5.975240,-2.355527,0.351294],[-3.086686,6.558405,-3.803575,-4.084031,-3.402555,-3.172657,-1.196441,-7.149519,8.437205,9.202589],[-0.197180,7.236237,-6.530511,9.980489,8.549974,-8.331634,-6.769018,7.997379,8.629952,-3.805876],[7.193363,-8.706192,7.993666,0.650416,8.734246,2.437113,6.234984,-9.941218,-4.776918,0.044513],[-3.498666,4.372697,2.665977,-3.237987,-9.699335,-5.382455,6.283219,-1.004562,-7.514698,5.483085],[-9.387191,5.932553,1.174361,-2.228654,3.875551,8.133143,9.335336,5.405428,5.479943,6.911336],[-4.693143,-8.674274,-8.404057,5.800816,-9.930474,-4.768222,6.488174,8.663254,3.954251,-4.178970],[3.057863,2.065060,0.816987,4.560736,-7.582861,-0.349361,-2.959151,-1.857581,6.887414,2.390361],[3.552199,5.275410,4.287062,8.121964,-2.931997,-5.728539,-2.381963,-6.327089,-7.290628,-3.480455],[-1.264872,3.859597,7.905130,8.462724,3.242366,1.202346,-5.040556,0.259472,6.682539,-0.217883],[8.856023,2.242345,-0.296936,1.134040,5.612421,8.425849,-7.965331,-1.416101,1.106131,6.159792],[5.750832,4.814938,1.076566,6.180109,9.249288,-4.165612,-8.948088,-3.116258,8.974657,9.759890],[-8.034664,-4.087474,-5.355503,-0.601040,-4.209145,-9.957827,-4.953967,4.307130,4.051135,-6.598309],[-2.077084,9.804062,-9.742726,-2.246937,4.067091,-7.953308,-1.743362,-7.587155,-9.955841,-0.478748],[-6.103452,-1.334945,-4.236600,-5.722787,-1.317898,3.427740,1.462358,-8.347859,-7.761991,6.586095],[-0.375572,2.031820,-0.927216,5.236462,2.420736,6.161648,1.582644,-4.826794,1.100767,7.106322],[-8.118889,4.412458,1.771578,5.950906,-8.789055,0.988036,6.940202,6.173331,-8.403016,-4.733622],[4.613548,-8.686086,8.485816,-9.079638,6.657436,-9.586691,-1.891378,-7.936647,0.462357,-9.341608],[-6.232879,7.989819,-0.205289,-1.961403,8.352982,-2.548374,-0.076798,5.266278,-5.913608,8.637767],[2.077415,0.782532,1.295465,5.278513,7.602346,-3.464645,8.917707,6.344015,-3.002445,8.515256],[-4.239127,-4.276204,-8.082518,-3.032648,-8.731260,-5.596938,-1.177258,5.734552,1.059352,-9.986456],[-3.684998,0.705436,-4.106454,-6.220552,-8.500004,4.044377,8.050530,6.734180,0.685934,-1.680559]], dtype = "float32")#candidate|1785|(154, 10)|const|float32
call_1784 = relay.TupleGetItem(func_926_call(relay.reshape(const_1785.astype('float32'), [1540,])), 0)
call_1786 = relay.TupleGetItem(func_929_call(relay.reshape(const_1785.astype('float32'), [1540,])), 0)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_1800 = func_194_call()
call_1801 = func_194_call()
uop_1816 = relay.sinh(var_1777.astype('float64')) # shape=(4, 9, 5)
func_1033_call = mod.get_global_var('func_1033')
func_1035_call = mutated_mod.get_global_var('func_1035')
var_1830 = relay.var("var_1830", dtype = "int8", shape = (10368,))#candidate|1830|(10368,)|var|int8
call_1829 = relay.TupleGetItem(func_1033_call(relay.reshape(var_1830.astype('int8'), [4, 9, 288])), 0)
call_1831 = relay.TupleGetItem(func_1035_call(relay.reshape(var_1830.astype('int8'), [4, 9, 288])), 0)
bop_1843 = relay.bitwise_or(uop_1816.astype('int64'), relay.reshape(bop_1778.astype('int64'), relay.shape_of(uop_1816))) # shape=(4, 9, 5)
bop_1846 = relay.bitwise_or(uop_1816.astype('int64'), relay.reshape(bop_1781.astype('int64'), relay.shape_of(uop_1816))) # shape=(4, 9, 5)
bop_1856 = relay.floor_divide(var_1830.astype('float32'), call_1732.astype('float32')) # shape=(4, 9, 10368)
bop_1859 = relay.floor_divide(var_1830.astype('float32'), call_1733.astype('float32')) # shape=(4, 9, 10368)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_1874 = func_194_call()
call_1875 = func_194_call()
uop_1878 = relay.sigmoid(uop_1816.astype('float32')) # shape=(4, 9, 5)
func_959_call = mod.get_global_var('func_959')
func_960_call = mutated_mod.get_global_var('func_960')
call_1889 = func_959_call()
call_1890 = func_959_call()
func_1684_call = mod.get_global_var('func_1684')
func_1685_call = mutated_mod.get_global_var('func_1685')
call_1898 = relay.TupleGetItem(func_1684_call(), 0)
call_1899 = relay.TupleGetItem(func_1685_call(), 0)
func_1710_call = mod.get_global_var('func_1710')
func_1713_call = mutated_mod.get_global_var('func_1713')
var_1906 = relay.var("var_1906", dtype = "int16", shape = (936,))#candidate|1906|(936,)|var|int16
call_1905 = relay.TupleGetItem(func_1710_call(relay.reshape(var_1906.astype('int16'), [936,])), 1)
call_1907 = relay.TupleGetItem(func_1713_call(relay.reshape(var_1906.astype('int16'), [936,])), 1)
func_514_call = mod.get_global_var('func_514')
func_515_call = mutated_mod.get_global_var('func_515')
call_1921 = func_514_call()
call_1922 = func_514_call()
bop_1934 = relay.logical_and(uop_1878.astype('bool'), call_1889.astype('bool')) # shape=(4, 9, 5)
bop_1937 = relay.logical_and(uop_1878.astype('bool'), call_1890.astype('bool')) # shape=(4, 9, 5)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_1938 = relay.TupleGetItem(func_653_call(), 1)
call_1939 = relay.TupleGetItem(func_654_call(), 1)
var_1941 = relay.var("var_1941", dtype = "float32", shape = (4, 9, 12))#candidate|1941|(4, 9, 12)|var|float32
bop_1942 = relay.maximum(call_1889.astype('uint16'), var_1941.astype('uint16')) # shape=(4, 9, 12)
bop_1945 = relay.maximum(call_1890.astype('uint16'), var_1941.astype('uint16')) # shape=(4, 9, 12)
func_1556_call = mod.get_global_var('func_1556')
func_1559_call = mutated_mod.get_global_var('func_1559')
call_1960 = relay.TupleGetItem(func_1556_call(relay.reshape(const_1772.astype('float32'), [6, 66])), 2)
call_1961 = relay.TupleGetItem(func_1559_call(relay.reshape(const_1772.astype('float32'), [6, 66])), 2)
func_926_call = mod.get_global_var('func_926')
func_929_call = mutated_mod.get_global_var('func_929')
call_1968 = relay.TupleGetItem(func_926_call(relay.reshape(call_1938.astype('float32'), [1540,])), 2)
call_1969 = relay.TupleGetItem(func_929_call(relay.reshape(call_1938.astype('float32'), [1540,])), 2)
output = relay.Tuple([call_1771,const_1772,call_1782,call_1784,const_1785,call_1800,call_1829,bop_1843,bop_1856,call_1874,call_1898,call_1905,var_1906,call_1921,bop_1934,call_1938,bop_1942,call_1960,call_1968,])
output2 = relay.Tuple([call_1773,const_1772,call_1783,call_1786,const_1785,call_1801,call_1831,bop_1846,bop_1859,call_1875,call_1899,call_1907,var_1906,call_1922,bop_1937,call_1939,bop_1945,call_1961,call_1969,])
func_1972 = relay.Function([var_1777,var_1830,var_1906,var_1941,], output)
mod['func_1972'] = func_1972
mod = relay.transform.InferType()(mod)
mutated_mod['func_1972'] = func_1972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1972_call = mutated_mod.get_global_var('func_1972')
var_1974 = relay.var("var_1974", dtype = "float32", shape = (4, 9, 5))#candidate|1974|(4, 9, 5)|var|float32
var_1975 = relay.var("var_1975", dtype = "int8", shape = (10368,))#candidate|1975|(10368,)|var|int8
var_1976 = relay.var("var_1976", dtype = "int16", shape = (936,))#candidate|1976|(936,)|var|int16
var_1977 = relay.var("var_1977", dtype = "float32", shape = (4, 9, 12))#candidate|1977|(4, 9, 12)|var|float32
call_1973 = func_1972_call(var_1974,var_1975,var_1976,var_1977,)
output = call_1973
func_1978 = relay.Function([var_1974,var_1975,var_1976,var_1977,], output)
mutated_mod['func_1978'] = func_1978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_1982 = relay.TupleGetItem(func_577_call(), 0)
call_1983 = relay.TupleGetItem(func_579_call(), 0)
func_514_call = mod.get_global_var('func_514')
func_515_call = mutated_mod.get_global_var('func_515')
call_1996 = func_514_call()
call_1997 = func_514_call()
output = relay.Tuple([call_1982,call_1996,])
output2 = relay.Tuple([call_1983,call_1997,])
func_2002 = relay.Function([], output)
mod['func_2002'] = func_2002
mod = relay.transform.InferType()(mod)
mutated_mod['func_2002'] = func_2002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2002_call = mutated_mod.get_global_var('func_2002')
call_2003 = func_2002_call()
output = call_2003
func_2004 = relay.Function([], output)
mutated_mod['func_2004'] = func_2004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2002_call = mod.get_global_var('func_2002')
func_2004_call = mutated_mod.get_global_var('func_2004')
call_2005 = relay.TupleGetItem(func_2002_call(), 1)
call_2006 = relay.TupleGetItem(func_2004_call(), 1)
func_164_call = mod.get_global_var('func_164')
func_168_call = mutated_mod.get_global_var('func_168')
var_2012 = relay.var("var_2012", dtype = "float32", shape = (1540,))#candidate|2012|(1540,)|var|float32
call_2011 = func_164_call(relay.reshape(var_2012.astype('float32'), [10, 14, 11]), relay.reshape(var_2012.astype('float32'), [10, 14, 11]), )
call_2013 = func_164_call(relay.reshape(var_2012.astype('float32'), [10, 14, 11]), relay.reshape(var_2012.astype('float32'), [10, 14, 11]), )
func_1100_call = mod.get_global_var('func_1100')
func_1103_call = mutated_mod.get_global_var('func_1103')
const_2020 = relay.const([[5.789327,-5.546965,-5.755440,-6.325530,-8.159606,-1.272126,-3.082248,3.504438,4.402096,-1.694624,6.620271,2.287558,-3.306968,-2.384499,3.117618,-9.426438,-4.028376,7.060170,-3.924768,-2.362363,-1.125043,5.556023],[-4.867741,1.785617,1.980618,7.406427,9.052335,9.750434,-9.020357,-3.887402,9.020328,-9.627214,7.393061,-0.157786,8.636216,-6.985558,6.301814,-6.079104,-3.910811,-6.699340,-5.434400,-8.803155,-0.818957,4.149886],[6.608171,-4.521114,-1.126514,-1.534487,-9.627983,-5.745710,7.208067,5.383126,-2.078013,3.078089,4.776440,-3.991819,8.251936,-7.961754,0.181411,-7.707592,3.827739,9.253924,-3.741587,-0.039698,-9.274958,-2.319462],[9.368770,0.116892,-4.439804,3.464002,-6.890817,6.016824,-4.636877,7.849566,6.327961,1.460018,-3.340176,-6.128993,-8.349601,0.194741,0.327704,7.534366,-0.661095,9.446114,1.858326,-8.152677,-6.988943,6.810672],[9.542987,-6.991530,9.928367,-2.331254,-7.937312,-0.958226,4.451980,-3.168013,5.809611,8.235160,-2.641361,-4.846221,2.672393,9.376656,-8.657120,0.390307,0.767462,-5.914297,1.741213,-5.724230,-1.583112,-4.343272],[-2.900280,-8.506285,-3.065804,7.887236,-7.869890,-0.446551,6.321081,-3.773380,4.061449,7.448578,4.007179,5.717636,-2.016363,7.003413,-8.830856,-6.300022,-2.866180,-8.859093,0.471374,8.776922,-3.746841,4.794377],[6.793424,5.502146,3.461984,0.491670,0.264023,6.442272,-7.815412,-2.221512,6.098936,9.005049,7.356329,-2.422197,-3.257226,0.489402,-4.033521,-1.714389,-6.610357,-5.097212,-1.521931,-9.525000,-0.969549,-1.613772],[-4.285546,3.655504,8.061591,9.345675,-9.468264,6.745609,5.224172,7.757663,-5.982627,0.318103,-0.329635,-3.053588,6.905800,-6.307957,7.135806,-2.204128,7.947098,0.053552,8.956142,1.886766,-7.359637,-9.715894],[5.254224,8.631122,8.577939,-7.744773,-8.987634,-4.644857,-1.322924,4.718782,8.082969,5.880169,8.864028,-8.998040,-5.224145,6.584656,-3.629960,-9.190385,2.428855,9.777407,0.172447,-5.973522,3.790422,7.093671],[2.796489,1.119568,3.194102,9.158961,8.736444,2.102689,-4.578807,-6.874657,-4.496559,-9.599973,0.637296,-1.200265,-9.529826,-3.461602,7.271201,4.391980,4.146759,-1.526753,8.962540,8.398811,2.104127,-5.280075],[6.373724,-2.106845,-1.351340,-8.328414,3.760456,-2.541810,1.262821,6.711442,-8.288680,-3.803109,5.340860,-6.708668,-8.666790,6.773693,-6.345632,3.906423,-9.528274,5.574479,9.478794,-1.632564,-7.338760,-5.832911],[-2.788613,3.527654,-6.051416,-5.811837,-7.260928,-9.692376,-0.519285,-1.319310,-8.594780,9.183058,1.889238,2.425469,-4.361068,7.967204,-3.939728,-0.310957,5.874066,4.722821,8.135056,4.167007,1.013021,9.999943],[3.260718,-4.354818,7.138371,7.744153,7.187731,9.580037,-6.349418,-6.937144,-0.563423,0.776961,-5.821705,6.884859,-4.189392,2.286550,1.387054,-9.906312,-4.424407,-6.737285,-0.584395,4.314943,-3.673063,6.259573],[6.338990,5.763778,-0.373126,-1.307791,1.566854,4.826191,-4.536172,1.339073,0.021444,0.483089,7.435395,9.100202,9.398741,0.230175,-8.737713,-0.532982,-0.062683,6.966344,9.975990,-9.321402,-5.851832,-0.996310],[-5.613051,-4.384797,8.541876,-6.888834,4.198256,-5.889399,-8.008604,-3.886010,-7.921953,-9.161362,-5.375129,-7.199503,3.469274,-1.258359,-3.750197,7.501700,0.435533,-6.885984,7.392486,3.980151,-2.379158,9.056593],[1.529224,4.772845,-7.771273,-9.286510,-3.190108,-3.025321,8.721795,8.013209,-5.588638,0.850685,-5.804499,-1.718050,-7.991608,-4.579731,-0.556265,9.302883,4.890868,6.403159,-8.245554,-6.590916,-2.628262,6.518109],[7.417559,5.298885,3.642584,7.253374,-6.983122,1.435963,1.462429,-6.217647,5.832127,7.714626,-6.468877,-8.658628,2.818560,3.666990,-5.325524,7.056102,4.075697,3.774182,6.862551,-4.278511,-6.140583,-3.610572],[1.581506,2.542199,-1.461227,3.833836,-5.694930,-9.471906,-6.763070,8.074179,-0.701162,3.604879,-5.795239,-7.050638,8.864177,0.412559,-8.613949,-2.855848,-3.707803,-0.767491,-5.942383,-6.236165,2.206746,-9.956562],[-8.205154,-8.748043,2.085283,1.215249,-1.854770,5.984438,-5.420397,-5.522739,1.705762,4.520681,-6.655652,-6.998238,2.553911,2.541100,0.069292,4.706478,-8.234682,-5.422575,5.705846,7.666055,8.692530,6.663207],[0.975672,-3.083063,-2.250905,7.884004,5.456999,-1.918644,-9.553279,-9.279749,9.259362,6.661135,8.147879,2.197072,1.484284,5.877960,-2.571323,9.085112,-5.748616,-0.626107,6.131103,1.225475,1.148310,9.033060],[-3.075698,-3.460419,7.091535,5.641625,9.888588,5.008421,6.290598,-3.357962,-6.053806,6.429086,6.591762,7.071214,6.954690,-2.942615,-4.558298,-8.165361,3.663721,4.494480,1.666795,1.266670,1.844733,9.270510],[5.141712,-6.007494,6.926830,-6.590392,3.197103,4.262090,0.201469,-1.521035,-3.696379,-5.786822,9.269376,-4.161107,-1.021756,3.281777,4.698452,-9.687783,-7.207871,-3.219533,-6.268574,9.546953,-4.042543,2.860754],[-6.436816,-8.055455,-6.719668,-4.302849,-0.708876,-5.147899,-7.810753,-0.478432,2.567757,5.826953,-0.944109,4.165615,-6.515113,-8.352167,-7.758171,-2.559657,5.492184,8.160842,9.409500,6.250195,-4.032464,-7.442031],[-0.433846,-2.208346,1.549875,1.101858,4.053178,9.065927,7.022825,9.044582,6.446870,-5.022248,-6.247768,-7.176245,6.262227,8.473508,-0.547111,7.231431,-3.994710,-8.522428,4.882272,7.639163,-5.632978,-6.336686],[9.119231,8.318705,-0.735102,0.811149,3.085750,-3.087028,-8.197150,7.431356,-4.031544,9.104023,-8.962149,-4.944682,4.069238,8.097472,-5.203531,-7.601670,9.489007,-0.023225,0.907433,-8.981643,-3.206270,-2.970448],[-4.412839,2.426606,-9.760696,7.561521,-9.689399,-4.881029,-0.026965,3.261737,9.560615,-4.332973,-9.072417,-9.998769,-0.852997,-6.708032,-4.936002,8.032749,-3.745974,6.064373,9.827136,-0.488022,-7.488297,-3.029608],[-4.173754,-9.897432,7.423437,-5.355333,6.393263,7.294665,6.745451,-5.907241,-4.476323,-4.146873,-3.152251,7.935109,-6.866864,4.348927,-0.736202,0.438990,-6.049913,6.968987,-6.163168,9.475106,-8.229116,-4.039355],[-3.374447,7.426672,-6.119202,-9.434458,0.379661,0.557825,4.420859,7.395295,-2.217509,-7.126758,-3.890749,-4.894798,2.018610,-1.022994,-1.130553,4.686806,-1.357594,-6.375610,-9.058922,2.225060,-8.340357,5.168367],[-9.658218,-5.100790,-5.395739,9.244839,-6.232342,4.033621,1.071991,6.928993,-0.608731,-7.123343,-7.244301,-7.753376,4.869510,-6.680851,-6.079119,8.641319,-7.348876,4.716479,-3.766254,7.480800,-7.096661,-5.894991],[7.125695,6.924091,-2.430781,-3.288760,-7.831078,8.586474,-0.231574,-4.827784,-8.272927,2.220705,3.441400,5.757258,8.040263,-8.934564,4.561071,6.307637,-9.517269,9.430867,0.323515,1.111985,-7.750716,6.512046],[5.678309,1.905963,-6.203999,-0.269374,7.604825,6.120269,6.328551,-3.634393,3.023346,8.802883,-6.295666,-6.593343,-3.676796,-0.398863,5.344057,1.204713,8.691143,-0.398855,-8.218037,6.363624,-9.592553,-4.456066],[-0.136413,-7.176373,8.858004,5.956182,-6.408729,1.672508,-3.678271,6.796534,4.127583,-9.484258,6.894041,-9.143475,2.970694,5.267103,5.516619,7.901710,-6.478045,6.197016,9.011584,-5.676850,-9.418167,-5.289982],[0.601847,-5.839697,1.796767,2.601206,4.106540,-3.908668,5.792102,-0.052657,7.410861,-2.117896,-8.909696,5.690918,-1.431210,7.422927,4.400411,2.869105,-8.160154,-5.121027,-6.584990,-8.688749,2.648501,2.675836],[8.878052,7.113696,1.485501,-5.410774,9.800720,-3.743233,0.803158,6.357475,1.091011,8.063438,-4.692956,6.686682,9.503411,8.709606,-5.428342,3.006513,-8.095745,4.397526,-7.091739,1.219093,1.802804,-3.875261],[-2.240624,-7.312848,-9.216926,6.558528,8.287419,-6.686067,-0.137971,4.907818,-8.571282,-2.725531,-9.946100,-5.612188,-1.900878,-1.308705,5.004149,-0.487227,-2.126465,-0.377692,0.543309,-4.833409,-9.654837,4.770129],[-9.326437,-1.570408,-8.800087,8.109154,-3.799597,6.911367,-9.236621,-8.679692,-7.713452,2.090521,6.149911,-6.372838,2.933368,4.256405,0.902890,-0.876538,-1.036997,-1.958103,-4.981272,3.661198,7.447569,9.143306]], dtype = "float32")#candidate|2020|(36, 22)|const|float32
call_2019 = relay.TupleGetItem(func_1100_call(relay.reshape(const_2020.astype('float32'), [8, 11, 9])), 0)
call_2021 = relay.TupleGetItem(func_1103_call(relay.reshape(const_2020.astype('float32'), [8, 11, 9])), 0)
func_280_call = mod.get_global_var('func_280')
func_282_call = mutated_mod.get_global_var('func_282')
var_2032 = relay.var("var_2032", dtype = "float32", shape = (396,))#candidate|2032|(396,)|var|float32
call_2031 = relay.TupleGetItem(func_280_call(relay.reshape(var_2032.astype('float32'), [4, 9, 11])), 0)
call_2033 = relay.TupleGetItem(func_282_call(relay.reshape(var_2032.astype('float32'), [4, 9, 11])), 0)
func_1556_call = mod.get_global_var('func_1556')
func_1559_call = mutated_mod.get_global_var('func_1559')
call_2035 = relay.TupleGetItem(func_1556_call(relay.reshape(var_2032.astype('float32'), [6, 66])), 0)
call_2036 = relay.TupleGetItem(func_1559_call(relay.reshape(var_2032.astype('float32'), [6, 66])), 0)
func_926_call = mod.get_global_var('func_926')
func_929_call = mutated_mod.get_global_var('func_929')
call_2040 = relay.TupleGetItem(func_926_call(relay.reshape(var_2012.astype('float32'), [1540,])), 1)
call_2041 = relay.TupleGetItem(func_929_call(relay.reshape(var_2012.astype('float32'), [1540,])), 1)
output = relay.Tuple([call_2005,call_2011,var_2012,call_2019,const_2020,call_2031,var_2032,call_2035,call_2040,])
output2 = relay.Tuple([call_2006,call_2013,var_2012,call_2021,const_2020,call_2033,var_2032,call_2036,call_2041,])
func_2045 = relay.Function([var_2012,var_2032,], output)
mod['func_2045'] = func_2045
mod = relay.transform.InferType()(mod)
var_2046 = relay.var("var_2046", dtype = "float32", shape = (1540,))#candidate|2046|(1540,)|var|float32
var_2047 = relay.var("var_2047", dtype = "float32", shape = (396,))#candidate|2047|(396,)|var|float32
output = func_2045(var_2046,var_2047,)
func_2048 = relay.Function([var_2046,var_2047,], output)
mutated_mod['func_2048'] = func_2048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1684_call = mod.get_global_var('func_1684')
func_1685_call = mutated_mod.get_global_var('func_1685')
call_2061 = relay.TupleGetItem(func_1684_call(), 0)
call_2062 = relay.TupleGetItem(func_1685_call(), 0)
output = relay.Tuple([call_2061,])
output2 = relay.Tuple([call_2062,])
func_2063 = relay.Function([], output)
mod['func_2063'] = func_2063
mod = relay.transform.InferType()(mod)
mutated_mod['func_2063'] = func_2063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2063_call = mutated_mod.get_global_var('func_2063')
call_2064 = func_2063_call()
output = call_2064
func_2065 = relay.Function([], output)
mutated_mod['func_2065'] = func_2065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_2090 = relay.TupleGetItem(func_653_call(), 1)
call_2091 = relay.TupleGetItem(func_654_call(), 1)
output = relay.Tuple([call_2090,])
output2 = relay.Tuple([call_2091,])
func_2108 = relay.Function([], output)
mod['func_2108'] = func_2108
mod = relay.transform.InferType()(mod)
mutated_mod['func_2108'] = func_2108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2108_call = mutated_mod.get_global_var('func_2108')
call_2109 = func_2108_call()
output = call_2109
func_2110 = relay.Function([], output)
mutated_mod['func_2110'] = func_2110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2108_call = mod.get_global_var('func_2108')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_2160 = relay.TupleGetItem(func_2108_call(), 0)
call_2161 = relay.TupleGetItem(func_2110_call(), 0)
uop_2163 = relay.log2(call_2160.astype('float64')) # shape=(10, 14, 11)
uop_2165 = relay.log2(call_2161.astype('float64')) # shape=(10, 14, 11)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_2169 = relay.TupleGetItem(func_577_call(), 3)
call_2170 = relay.TupleGetItem(func_579_call(), 3)
output = relay.Tuple([uop_2163,call_2169,])
output2 = relay.Tuple([uop_2165,call_2170,])
func_2172 = relay.Function([], output)
mod['func_2172'] = func_2172
mod = relay.transform.InferType()(mod)
mutated_mod['func_2172'] = func_2172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2172_call = mutated_mod.get_global_var('func_2172')
call_2173 = func_2172_call()
output = call_2173
func_2174 = relay.Function([], output)
mutated_mod['func_2174'] = func_2174
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2210 = relay.var("var_2210", dtype = "uint16", shape = (4, 7, 10))#candidate|2210|(4, 7, 10)|var|uint16
var_2211 = relay.var("var_2211", dtype = "uint16", shape = (4, 7, 10))#candidate|2211|(4, 7, 10)|var|uint16
bop_2212 = relay.less_equal(var_2210.astype('bool'), relay.reshape(var_2211.astype('bool'), relay.shape_of(var_2210))) # shape=(4, 7, 10)
uop_2223 = relay.sqrt(bop_2212.astype('float32')) # shape=(4, 7, 10)
var_2232 = relay.var("var_2232", dtype = "uint16", shape = (4, 7, 10))#candidate|2232|(4, 7, 10)|var|uint16
bop_2233 = relay.greater(var_2210.astype('bool'), relay.reshape(var_2232.astype('bool'), relay.shape_of(var_2210))) # shape=(4, 7, 10)
uop_2238 = relay.sigmoid(uop_2223.astype('float64')) # shape=(4, 7, 10)
bop_2243 = relay.power(uop_2238.astype('float64'), relay.reshape(var_2211.astype('float64'), relay.shape_of(uop_2238))) # shape=(4, 7, 10)
output = relay.Tuple([bop_2233,bop_2243,])
output2 = relay.Tuple([bop_2233,bop_2243,])
func_2246 = relay.Function([var_2210,var_2211,var_2232,], output)
mod['func_2246'] = func_2246
mod = relay.transform.InferType()(mod)
var_2247 = relay.var("var_2247", dtype = "uint16", shape = (4, 7, 10))#candidate|2247|(4, 7, 10)|var|uint16
var_2248 = relay.var("var_2248", dtype = "uint16", shape = (4, 7, 10))#candidate|2248|(4, 7, 10)|var|uint16
var_2249 = relay.var("var_2249", dtype = "uint16", shape = (4, 7, 10))#candidate|2249|(4, 7, 10)|var|uint16
output = func_2246(var_2247,var_2248,var_2249,)
func_2250 = relay.Function([var_2247,var_2248,var_2249,], output)
mutated_mod['func_2250'] = func_2250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1311_call = mod.get_global_var('func_1311')
func_1313_call = mutated_mod.get_global_var('func_1313')
call_2254 = relay.TupleGetItem(func_1311_call(), 6)
call_2255 = relay.TupleGetItem(func_1313_call(), 6)
func_2063_call = mod.get_global_var('func_2063')
func_2065_call = mutated_mod.get_global_var('func_2065')
call_2266 = relay.TupleGetItem(func_2063_call(), 0)
call_2267 = relay.TupleGetItem(func_2065_call(), 0)
uop_2282 = relay.sigmoid(call_2266.astype('float32')) # shape=(4, 9, 1)
uop_2284 = relay.sigmoid(call_2267.astype('float32')) # shape=(4, 9, 1)
func_2002_call = mod.get_global_var('func_2002')
func_2004_call = mutated_mod.get_global_var('func_2004')
call_2285 = relay.TupleGetItem(func_2002_call(), 1)
call_2286 = relay.TupleGetItem(func_2004_call(), 1)
func_2246_call = mod.get_global_var('func_2246')
func_2250_call = mutated_mod.get_global_var('func_2250')
const_2297 = relay.const([5,3,-10,8,3,-9,-4,4,-3,-3,8,-6,10,-2,-8,-10,-10,-10,1,8,9,-10,6,8,3,-8,-9,-1,-4,1,-6,6,5,8,-3,-1,-4,5,5,9,5,8,-2,2,1,-8,6,5,-2,-9,-9,-7,-1,3,4,-3,-9,-4,9,-7,-1,9,10,3,7,7,4,9,6,3,-3,-10,9,-3,10,-1,6,-2,-4,-8,-9,-8,-1,-10,8,9,-10,-2,-3,-9,5,-7,2,7,4,-8,4,-8,3,-4,-1,-10,1,2,-9,8,3,-6,7,-10,1,-6,3,10,3,-5,-6,-5,-9,1,-10,-5,-8,-5,-4,-6,2,-10,5,9,3,-2,8,-5,6,8,-7,-8,-2,10,7,-3,-5,2,-4,-9,4,5,9,-3,-6,-3,-2,9,-6,-3,2,-2,8,8,4,8,-9,1,3,-6,-5,-3,2,2,-1,-10,1,-2,7,-1,-9,10,2,-7,5,5,2,8,1,3,5,5,-7,-6,-8,7,6,5,-9,4,-6,6,6,-4,-4,-9,2,6,10,6,-1,-5,-8,-6,3,-3,-8,6,2,2,-9,-6,2,10,6,-2,-9,-3,-1,4,-8,4,-7,-3,-2,-7,-4,10,7,-2,8,-9,2,3,-10,9,5,5,4,5,2,7,-6,-2,8,7,7,-4,5,-4,6,4,-7,-5,8,-6,-3,6,1,4,3,7,7,-3,-9,-9,2,-6,4,-9,3,-3,-10,6], dtype = "uint16")#candidate|2297|(280,)|const|uint16
call_2296 = relay.TupleGetItem(func_2246_call(relay.reshape(const_2297.astype('uint16'), [4, 7, 10]), relay.reshape(const_2297.astype('uint16'), [4, 7, 10]), relay.reshape(const_2297.astype('uint16'), [4, 7, 10]), ), 0)
call_2298 = relay.TupleGetItem(func_2250_call(relay.reshape(const_2297.astype('uint16'), [4, 7, 10]), relay.reshape(const_2297.astype('uint16'), [4, 7, 10]), relay.reshape(const_2297.astype('uint16'), [4, 7, 10]), ), 0)
output = relay.Tuple([call_2254,uop_2282,call_2285,call_2296,const_2297,])
output2 = relay.Tuple([call_2255,uop_2284,call_2286,call_2298,const_2297,])
func_2299 = relay.Function([], output)
mod['func_2299'] = func_2299
mod = relay.transform.InferType()(mod)
mutated_mod['func_2299'] = func_2299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2299_call = mutated_mod.get_global_var('func_2299')
call_2300 = func_2299_call()
output = call_2300
func_2301 = relay.Function([], output)
mutated_mod['func_2301'] = func_2301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_959_call = mod.get_global_var('func_959')
func_960_call = mutated_mod.get_global_var('func_960')
call_2331 = func_959_call()
call_2332 = func_959_call()
output = relay.Tuple([call_2331,])
output2 = relay.Tuple([call_2332,])
func_2344 = relay.Function([], output)
mod['func_2344'] = func_2344
mod = relay.transform.InferType()(mod)
output = func_2344()
func_2345 = relay.Function([], output)
mutated_mod['func_2345'] = func_2345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1617_call = mod.get_global_var('func_1617')
func_1618_call = mutated_mod.get_global_var('func_1618')
call_2396 = relay.TupleGetItem(func_1617_call(), 0)
call_2397 = relay.TupleGetItem(func_1618_call(), 0)
output = call_2396
output2 = call_2397
func_2404 = relay.Function([], output)
mod['func_2404'] = func_2404
mod = relay.transform.InferType()(mod)
output = func_2404()
func_2405 = relay.Function([], output)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_2420 = relay.TupleGetItem(func_653_call(), 0)
call_2421 = relay.TupleGetItem(func_654_call(), 0)
output = call_2420
output2 = call_2421
func_2445 = relay.Function([], output)
mod['func_2445'] = func_2445
mod = relay.transform.InferType()(mod)
output = func_2445()
func_2446 = relay.Function([], output)
mutated_mod['func_2446'] = func_2446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1684_call = mod.get_global_var('func_1684')
func_1685_call = mutated_mod.get_global_var('func_1685')
call_2457 = relay.TupleGetItem(func_1684_call(), 0)
call_2458 = relay.TupleGetItem(func_1685_call(), 0)
output = call_2457
output2 = call_2458
func_2477 = relay.Function([], output)
mod['func_2477'] = func_2477
mod = relay.transform.InferType()(mod)
mutated_mod['func_2477'] = func_2477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2477_call = mutated_mod.get_global_var('func_2477')
call_2478 = func_2477_call()
output = call_2478
func_2479 = relay.Function([], output)
mutated_mod['func_2479'] = func_2479
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2552 = relay.var("var_2552", dtype = "float64", shape = (5, 10, 10))#candidate|2552|(5, 10, 10)|var|float64
var_2553 = relay.var("var_2553", dtype = "float64", shape = (5, 10, 10))#candidate|2553|(5, 10, 10)|var|float64
bop_2554 = relay.floor_divide(var_2552.astype('float64'), relay.reshape(var_2553.astype('float64'), relay.shape_of(var_2552))) # shape=(5, 10, 10)
uop_2562 = relay.sin(var_2553.astype('float64')) # shape=(5, 10, 10)
uop_2584 = relay.cosh(bop_2554.astype('float32')) # shape=(5, 10, 10)
func_2045_call = mod.get_global_var('func_2045')
func_2048_call = mutated_mod.get_global_var('func_2048')
const_2587 = relay.const([[-9.426240,-7.056957,7.608120,5.735266,-3.871993,-6.418732,-3.951685,-9.353700,-3.470301,1.044386,3.528333,4.077353,6.326757,1.437660,-2.750154,-6.889705,-5.667040,-1.771720,-1.484254,-7.364941,-3.912672,4.417539,-2.129970,1.362597,3.830020,-9.995309,-2.607707,-0.957192,3.573624,1.349549,4.259699,-1.380755,-3.382844,-0.975130,-5.233736,9.010039,1.890192,7.604192,-5.687207,-3.789703,5.217368,9.151527,-1.515700,9.645290,3.742354,1.293899,-1.106159,-3.647069,-5.738023,3.371007,-0.351972,6.254267,1.939274,2.084186,9.855457,-5.671202,1.112200,-1.911847,7.872111,7.479877,5.829165,-2.571074,-1.866710,-3.638133,4.038969,7.159196,8.727694,4.939260,9.275072,-8.540186,-7.472275,3.889106,-4.045504,5.282858,-1.264799,-5.256885,0.185431,6.315108,-9.598046,4.334714,-6.981039,6.358564,8.453620,-7.158054,1.136951,-2.032068,4.041176,9.146258,5.909095,-1.981897,3.591563,8.877213,2.791930,-9.159887,0.543200,5.911119,-8.775651,8.523013,7.113154,-2.954906,-8.753506,-6.815812,0.943208,-7.209331,-1.045740,-5.111681,7.851091,-8.514234,-7.966794,-4.472406,-8.466155,8.121244,-7.219484,4.221834,6.587993,1.789133,-2.260545,8.083946,9.245509,-1.790172,-3.675716,-5.457444,2.597700,-6.233601,5.134329,1.805215,-5.234833,0.566114,5.900668,-9.508849,-2.942559,-5.091402,5.611476,-9.892524,2.916956,-8.076000,1.343315,-4.883955,-1.158267,0.829396,8.523952,6.897403,5.889333,6.041315,3.299661,0.253305,6.716424,-2.793904,-2.094535,8.364909,-6.755030,7.755528,-5.004138,-6.188381,7.412054,7.622233,-4.280920,-5.456418,2.687493,-7.605113,-2.002873,-3.626481,6.069431,-2.928546,-4.969018,-7.558915,-5.723417,-6.448720,7.272416,2.535517,-8.427561,8.733055,6.002822,4.611575,9.764480,-0.589529,8.918123,5.356028,0.555615,-9.735436,-5.362564,-4.764027,9.841179,8.819354,5.547666,3.614835,8.915375,-7.579341,-1.501866,7.824119,4.910957,6.447444,1.094360,-4.559408,3.288645,-0.717607,5.715735,-3.474791,8.639224,7.927867,-5.716135,8.788794,5.416866,-0.326885,7.068302,-5.973158,9.076731,0.816926,-0.275571,-1.072074,5.938249,9.063642,0.245601,4.470663,-2.978012,-9.469598,6.023723,-7.599998,0.694149,-7.466645],[6.642731,-4.078554,5.481297,8.995369,8.672842,3.590350,-3.284811,1.677162,-9.084808,-2.096196,9.979330,0.364264,-0.898680,4.252812,-0.627661,-4.139557,-4.197476,5.701069,7.467656,-4.452903,-4.506536,1.945738,-1.498985,-7.067083,5.800870,7.463470,5.325225,1.787551,3.974017,-7.995069,-5.375933,4.907286,6.916251,-9.734964,4.227318,6.076307,-0.625821,-0.885869,9.229179,3.185611,9.985096,2.561474,9.843812,4.664480,5.691782,3.865957,-1.385657,7.062260,6.742355,-9.958697,-3.147425,-3.053754,-0.243220,2.551631,1.670671,-5.873114,-1.798511,-2.633797,-2.819107,-4.670755,2.672412,-0.463067,-1.280869,2.513553,6.453209,-0.665895,3.042401,4.518642,0.692380,7.836621,8.716251,4.458333,2.351884,-7.134046,5.943747,8.110809,-7.391891,5.288993,3.225152,-4.814329,-5.107078,-4.825276,4.269513,-6.001995,1.123312,4.464230,8.200138,-3.616788,-4.845793,3.028318,5.264042,-3.170456,-1.849216,-7.456754,-5.660487,-5.718360,5.412140,-7.518692,-4.880737,0.368613,-3.295778,5.861957,1.448232,-8.005728,-9.988786,-8.987535,8.106579,4.287334,-6.068018,5.403959,-6.107733,2.936881,6.044112,-4.413262,-4.544583,4.551021,-8.734745,4.584757,-1.054994,-5.701845,2.236125,-8.814371,8.436114,-5.365023,0.984854,1.836676,2.628400,9.144969,-8.474844,4.369727,6.899045,-3.094788,2.539953,1.590113,1.325803,-8.087424,-6.327968,3.930821,-1.567219,3.052862,-4.189969,9.814311,-8.188424,-5.223992,-6.613283,3.726298,-8.146994,4.186665,6.671383,4.991596,-4.473345,8.829308,-6.297859,1.779754,-7.280620,-7.787201,0.730140,1.941600,-3.238272,-3.179001,2.241678,-3.767078,6.348007,8.701496,-2.515276,-2.853601,-9.441547,-6.518160,-8.928757,6.205043,-0.256221,4.943315,6.513342,6.415431,-1.937116,-0.199010,-9.951955,0.824703,-9.367459,-5.629780,4.072967,-0.395351,8.979664,-4.042874,-2.150722,-2.191041,8.336323,-7.702999,-7.022705,-0.526471,0.329388,-8.103336,3.697395,-4.148847,-6.941688,7.871599,6.061897,0.707117,-9.755495,-8.393015,3.233772,8.852426,8.832619,6.115081,-8.928438,-9.020405,-7.883842,4.410536,5.251134,-2.905309,-6.490273,0.900005,1.123301,-9.441522,6.661575,-7.816035,-2.755470,6.664207,2.328210,4.225532],[9.856963,3.552743,4.906994,7.093939,-3.944253,-0.349698,0.979891,-0.250347,9.150562,-4.568604,-7.765481,8.326199,1.427627,-2.028933,-5.212827,-5.403161,4.674070,7.260540,-3.760474,8.477492,-7.496461,8.686010,-6.542060,-7.699354,2.246124,-6.200722,7.420447,-4.819593,-9.708379,5.746803,-7.083039,-3.592441,-9.899409,-9.947235,1.343164,6.304556,-8.572253,8.480349,7.744543,-1.157266,5.525923,-8.607691,-3.922907,2.308754,6.601162,0.657056,-3.822343,3.645201,-0.229695,6.040077,-2.621803,7.777900,3.537482,7.560832,9.770808,0.689357,-2.249000,9.499728,-6.932149,5.176385,-1.852396,-9.957880,1.028061,9.696372,0.892031,9.642151,6.748015,-2.667579,9.030557,9.562887,8.327497,5.325699,-5.262973,7.716008,7.441739,-0.740936,4.849927,-2.727536,7.406020,-8.731957,-7.589737,-3.346190,3.571440,7.379522,-9.261226,1.867805,6.086464,4.131965,9.099157,1.884526,0.776951,-8.978428,-5.128392,6.529706,-9.700858,-4.394324,4.667772,6.340680,-3.109176,-1.885660,0.084970,-0.157095,-3.386806,2.674921,-4.781407,5.550597,-7.885515,1.597105,-8.672599,-6.457802,-4.440315,-0.299428,5.854774,-3.675522,-2.390853,-0.517230,-6.783457,-0.196202,-0.981208,5.810793,-6.091457,6.112482,-9.711781,3.724917,1.756342,-2.356354,7.689261,-8.383054,-2.547338,-4.988602,6.483658,-1.591789,8.541371,-8.478713,-3.054314,2.585722,-4.719081,-5.054924,6.257018,-2.365947,9.905954,-6.323610,4.489743,-0.133821,-0.159600,-1.046977,2.401302,0.683595,3.196601,7.067262,4.815242,3.354075,1.159106,1.812901,5.168672,2.485852,-7.904212,1.446110,-2.307784,8.603921,-5.416758,-7.929918,-5.236813,6.452554,-3.224613,-8.551623,1.708779,1.695375,3.006539,2.147516,-0.836870,3.358959,-9.601593,-1.159474,-0.941525,0.843415,5.633678,4.326004,-3.503526,-6.996592,1.664384,-1.387234,-0.546785,0.458756,-6.589998,-8.863075,5.044064,9.033557,2.122733,7.205119,4.250990,-1.327920,-5.443449,1.387325,-9.186291,6.990762,-0.889665,-1.695730,-3.356303,-4.709660,-9.946332,7.305595,-3.607028,-6.505333,5.049731,-4.199135,-3.985542,8.963054,-6.403921,6.723913,-5.440951,-3.075333,8.434884,4.402436,-4.930658,-3.682527,1.781551,-6.447548,5.453841,2.953978],[-7.451946,3.086059,-7.825755,-9.840156,7.336546,-1.779776,-6.836207,-6.957161,3.412848,1.294800,9.885937,2.447424,-7.099578,8.395470,-6.663133,-2.583906,-5.426727,1.840817,-6.765791,1.928996,-0.336984,-4.600443,-2.264466,-4.225052,-9.182511,4.190279,8.285925,-5.814619,-7.519697,7.731240,-9.143340,-6.114294,-8.850764,-9.878831,9.542275,-9.905704,0.748168,-0.559878,-1.390802,6.728245,0.308513,-0.762569,2.594742,-5.755314,-3.166164,-6.483518,8.298625,8.816750,2.463628,-4.924842,5.005316,-4.090520,5.591635,-3.212219,5.929133,9.820979,-1.835642,3.660646,-8.090774,-5.463732,-7.529791,-5.176932,2.007850,8.688938,5.325683,7.920592,-5.726493,6.214811,-7.229141,4.082083,8.604193,-4.703197,7.864986,-6.613875,7.026015,-0.803214,5.315337,3.994426,1.453071,8.395796,9.247122,2.400145,-6.410838,4.972620,7.745736,-8.797435,6.645732,-2.080567,2.346237,0.096141,3.814849,-2.321375,-5.238313,0.725143,-0.345327,-1.026065,4.698015,4.263400,-5.206906,6.099938,-5.681484,-2.242135,-4.713700,-2.706049,8.993608,1.377476,3.520579,-4.728151,5.777681,5.814339,-5.499560,6.517064,-2.945636,-9.990731,-1.447793,-9.544306,1.685726,-0.676200,7.081544,1.206714,-7.313281,-3.473024,-6.515916,8.668990,-9.005324,3.006624,-8.888860,6.650503,-2.019982,1.727558,1.570617,3.742152,3.310927,-8.181918,-5.209819,8.391456,-5.575398,-6.298561,-1.921222,2.824724,4.857738,-7.843619,6.928780,-5.406678,4.321120,-3.735413,6.576559,5.005671,-5.419551,6.250991,-6.258198,2.565941,-3.705229,2.219865,-6.885111,-1.102216,-0.286849,1.080584,-3.462078,7.681100,-6.188425,-4.014460,3.229388,-1.683409,5.971897,-1.694104,-1.090820,9.610371,8.840111,-4.043934,8.881320,7.394441,9.366995,8.330991,-9.861460,5.284615,2.514557,-1.454042,3.623916,-6.309906,4.942426,-9.681737,-7.878574,-0.716915,3.380554,3.328303,3.302731,-6.569698,-6.586448,-8.665494,-4.667267,6.792323,3.268737,-4.268725,-1.262136,-4.811496,1.844817,1.688517,-9.027531,6.360974,-9.531525,-8.984534,-1.447389,-2.706714,-6.206676,2.697025,-2.074226,-9.174465,6.214808,9.088390,3.142451,6.622120,-6.876528,3.548834,-7.899843,-0.998092,6.237080,5.599587,6.057448,-8.371160],[-1.298612,-2.220358,-9.544952,9.841347,3.759188,1.432424,-0.283856,9.812967,-9.599646,7.958738,-9.345376,0.929468,-8.399526,5.843550,7.517805,8.588096,6.933523,-0.411352,0.039592,7.305426,-1.772041,0.947410,2.172385,-9.181771,7.164069,7.972326,2.717111,-4.155680,7.342825,-7.629779,2.453830,-8.076667,3.392570,3.463307,-1.073006,-1.763705,2.501094,4.384936,-4.382170,-9.071571,6.122506,0.248139,4.359091,-0.438561,8.284168,0.394707,8.464470,-4.627301,-1.044423,6.412945,-8.240710,-9.124423,6.601736,1.767532,0.732503,-0.513944,2.557634,0.159466,4.120100,1.095921,-5.128186,7.748539,-6.222866,5.219019,8.970239,-6.081701,-8.595167,-4.887565,-0.368236,7.477398,3.463891,4.420978,-0.524930,5.073967,-0.090548,-5.045042,7.564121,-8.333738,7.034087,6.019662,-3.083012,0.460822,-2.727319,8.457716,8.712322,-3.219191,-9.721546,0.101484,-6.171059,-2.217316,6.124633,-2.728928,-0.031908,-3.021467,-0.056099,4.153238,0.498970,8.706165,-7.827579,1.541300,8.084587,-6.130415,8.550265,-2.336362,0.380139,-3.725517,-3.135252,5.846248,-5.194647,-1.118860,1.550674,1.397863,-1.366849,-9.829936,2.104805,-9.825117,7.881500,-5.746415,-9.292010,6.352559,5.631663,-6.781496,-0.004097,6.699904,-5.100795,5.981325,4.158465,-0.022633,1.670483,-2.124738,-1.139072,1.345524,6.768725,-0.243869,8.737244,8.601643,-4.329476,-3.142400,-9.097101,1.482250,4.416979,-3.362449,8.970294,6.902496,-1.557632,-5.400635,-4.794549,-6.548923,9.148201,-9.879221,-2.493978,-6.050871,2.734032,3.414322,-2.364369,-4.792768,4.107165,-6.757454,-5.752999,9.620061,1.562974,4.160688,-7.953882,9.224644,5.424756,-3.994409,-1.644649,-5.360341,6.010630,6.680174,-7.608194,7.113458,-8.483065,-6.339760,8.966790,1.728382,0.381582,4.682171,6.200476,-9.804578,-5.412175,-7.512557,3.667411,-5.494677,8.448736,-0.676418,-0.625167,8.743772,1.320360,5.612771,-6.790560,5.660330,1.759765,4.542704,2.391041,3.380011,-2.769098,-0.966800,-5.826130,-0.426556,-2.381489,2.842990,-2.076085,-2.807994,3.636375,5.708015,-0.801271,5.698538,9.268550,-9.719724,-8.575455,-7.161441,-7.239705,-0.479304,1.080370,-9.487121,2.332014,-6.133423,-9.813828,9.680244],[-9.540228,0.960719,3.291216,5.043035,5.549054,-6.935145,4.191883,-1.063756,8.942644,0.183770,8.701841,3.868005,0.045063,1.097146,-8.782296,7.375991,2.097164,6.535959,-8.083144,1.210464,5.782318,7.339573,-6.498527,-5.732324,3.725677,-0.853904,6.427360,1.589954,-2.122413,-0.126904,-3.439459,3.895628,8.074082,-0.250443,2.742552,5.478399,1.149412,-2.241655,2.549054,-5.152511,-5.510408,7.587521,-3.648872,-3.131099,0.022576,5.905287,5.429505,6.412633,3.545695,-2.804903,2.216555,2.147376,-5.106411,-7.811236,-7.220605,-0.414615,-7.647093,-5.289919,0.609209,2.758897,-5.530902,-0.500369,8.785154,-6.345911,2.497541,-1.140692,-3.009931,-2.479876,9.971831,-1.352972,8.947238,-1.158638,1.100818,-5.611324,3.163650,8.460575,-0.056001,8.074889,-1.439807,-7.355854,-5.210383,-0.359910,3.916129,-8.821410,-2.083851,-1.940415,7.548553,6.904773,-5.863789,4.243378,8.928743,7.897208,-4.572638,5.096625,-9.590101,4.195802,-3.655442,6.563633,-5.702408,-8.416944,4.282805,-0.453104,9.541587,6.479197,4.437456,-7.293560,1.044658,-7.627579,-0.715177,-9.955751,3.812660,-4.967316,-7.779198,0.714361,0.225434,1.851935,1.438672,3.515064,0.059178,-5.615578,-5.765168,7.229102,-9.839573,1.826709,1.921362,8.744021,6.582183,0.950757,2.358998,-9.513941,-3.007406,0.056168,6.635596,6.451231,2.840845,6.461288,-3.088098,-8.772218,-8.814986,4.751846,8.051186,8.419754,-6.540558,-2.612103,0.894525,-7.768859,-7.289626,4.724042,0.365498,-8.816325,-4.659421,-4.772959,-7.044511,5.883280,-1.681211,5.237617,8.610190,9.755724,9.730913,-1.639018,-2.091756,-8.649420,-6.960612,2.903146,-4.264361,1.035994,1.587755,0.504577,-2.591445,8.500987,-0.928472,-8.172141,8.464554,7.438331,-1.074419,8.948822,1.220505,9.895961,-8.957136,8.169541,1.014212,0.148832,-7.752613,-7.264531,-9.061529,4.470243,-9.435030,-8.982555,3.562462,-1.272518,3.828254,7.879547,-8.230784,0.387176,3.195296,0.962332,3.830883,7.679407,-8.133968,-5.395259,9.586200,7.350153,8.968436,5.675386,7.928358,-9.143031,-7.636127,4.049766,3.316395,6.649031,3.880216,0.952280,5.753690,-8.395220,-6.521358,-8.616627,1.788041,-2.458123,-7.816558,6.827863],[7.794605,-0.216010,6.455026,-4.334474,-7.252140,7.943411,9.010827,-7.433228,-4.101031,-2.429247,5.097800,-7.923242,-9.117580,-0.125832,2.159049,-1.255724,7.611217,-4.517836,2.383194,4.942828,-4.689621,8.141879,0.861267,-7.052898,9.827891,8.853115,-6.239914,5.354194,-2.444166,8.434085,6.164321,-4.559607,-6.194005,-1.341465,-1.540064,-8.856206,-7.885164,-3.730034,1.861078,4.392515,9.857769,-3.256308,4.771915,-6.334390,5.867615,0.651739,7.864782,5.064160,-9.270832,9.777132,-6.799995,9.099281,-3.861779,-0.574082,-4.288183,-6.538105,-4.208782,8.169969,-7.654777,1.861029,1.633423,-0.584709,3.354195,9.595666,5.250931,-4.308278,-5.514209,4.642321,4.636271,-6.665370,6.948200,8.864232,8.488059,6.514741,-4.262974,4.160792,9.717983,-5.116629,-6.658195,-5.568634,7.396289,6.157612,-3.523796,-1.211745,-7.723128,-8.882660,3.601635,-2.324021,-8.125221,-5.806462,-1.056286,3.254855,1.914050,-5.351281,0.002474,-1.451599,6.709236,-9.147749,-5.396792,2.014527,0.735410,-9.936279,8.019460,-0.387872,4.164236,-1.841811,-6.918882,7.918661,-6.289515,6.963349,5.548594,-1.385385,1.234276,-5.528517,7.208260,9.911476,8.849957,3.066647,-2.375575,2.170791,-9.158026,3.585056,5.622394,-5.787486,0.202549,2.138133,7.888138,4.205293,-7.762124,-5.573196,-1.922319,-6.309940,-4.893867,-6.952619,5.187688,-9.603873,-7.108871,7.941934,-0.714579,3.727206,3.858535,-6.041855,-5.429494,-6.767648,-5.014614,-9.082505,-6.099897,-2.929874,-8.602631,9.436140,-8.433647,5.401556,5.333203,-9.316652,-8.786545,5.005840,-9.177237,8.562851,-1.697146,8.070532,-9.930121,0.110599,2.475495,9.663232,-5.878937,3.391559,-3.309498,2.058189,6.483320,-3.234190,5.877249,-8.604411,3.198819,-8.483678,7.175721,-6.070626,1.530993,-3.699833,-3.458117,-9.154086,-4.646068,0.321999,-4.680271,-9.912193,4.983155,-8.128638,4.340503,-1.602072,-7.550287,-4.678906,1.898045,2.039291,-5.723894,2.714708,-5.494751,9.695890,2.385711,0.618328,-8.380167,-8.577453,-0.059563,-2.599074,7.286284,7.716180,-7.938779,0.490639,-8.510690,-7.523654,-3.462367,9.148174,-5.453135,6.987764,-0.684739,9.584247,-2.656433,-1.962102,-5.144345,-2.734458,3.295447,3.642082]], dtype = "float32")#candidate|2587|(7, 220)|const|float32
const_2588 = relay.const([-7.944319,-0.379596,1.548556,1.792717,5.886348,-6.143550,0.864369,-9.662160,4.579560,3.916865,1.186243,0.861656,6.412592,-5.243432,9.077579,-3.592192,-8.251353,-0.255173,2.408006,7.847022,-4.785247,-0.600202,1.528909,4.105089,0.365444,9.819167,8.757626,8.509434,9.225437,8.990102,-5.670563,-6.861633,5.278386,-3.532003,-7.953275,9.323523,8.444122,2.564361,-1.028959,4.353539,6.277123,-6.472743,5.733633,8.985895,-0.492083,2.783529,-0.848378,5.877732,-0.271314,-0.010939,4.788171,6.575533,1.999524,7.325159,-8.092607,4.478883,2.345453,-8.312305,-7.685745,-9.731846,-5.014052,8.401558,3.995485,-1.566710,-4.671100,6.558517,-1.197502,0.411391,1.352053,9.639403,1.194588,1.173031,6.546557,-5.985101,6.910163,-3.012409,-7.313218,-2.560585,-2.853391,-3.050811,-8.232570,-3.227933,-0.373848,-8.735576,-0.602047,1.434120,8.184713,1.440330,-0.915449,-5.424102,-0.083933,-7.223853,-1.867424,-3.383415,7.528853,8.386905,-2.017401,6.896194,2.446123,-9.781697,0.362409,-4.010181,-1.879260,4.125885,3.297418,-3.855423,-4.965069,-0.614546,-7.788980,1.859419,8.924041,1.610203,-0.457374,3.745383,-8.270924,-1.990374,6.269354,-8.305069,-0.233508,4.943351,3.210120,2.653529,-7.262877,-0.939118,-8.149342,-3.038877,9.115708,-6.758436,-1.757579,4.571104,2.096829,2.321253,-4.226528,2.825099,0.318642,-5.285378,-8.582971,8.952368,-7.622389,3.632596,3.788563,-7.588518,7.947100,1.797087,-3.272280,1.273205,-1.186535,7.706371,-6.820159,8.172487,4.672880,7.745987,1.017749,-9.580808,-7.707344,-6.195495,9.470549,-6.211293,0.872104,2.495466,4.573151,-9.515935,2.713386,-6.552508,-3.045421,3.378472,-4.427867,8.959233,8.525911,5.183547,-6.705124,-0.325361,-9.737888,-8.979724,-6.354696,-0.694844,-7.082045,3.338970,-4.713709,-8.776357,9.031091,-2.948394,-7.778812,1.054419,6.044794,3.459270,-8.795555,4.205445,1.696964,1.676531,3.071135,6.750382,-8.513181,8.393133,-1.959069,1.510388,-8.074194,8.849054,8.230529,-2.843731,1.379013,-2.941532,3.019732,9.064575,-2.354142,-9.198251,-2.308572,9.189617,-9.088733,9.912214,-0.277495,-5.337691,-7.917191,8.534162,-3.835192,-8.210929,-1.587233,-0.711600,-5.536592,-8.332787,-5.268434,8.812753,-1.191077,1.806143,8.993966,6.074410,7.889418,-9.573756,-5.557307,6.743450,-9.437272,-5.967655,4.931945,-4.345316,-8.243790,-1.405425,-8.673629,3.255387,-2.275245,8.069516,6.418297,-9.921282,7.839806,-3.142475,-5.938212,-4.259437,4.773101,9.768889,1.949279,9.057400,-8.051996,-0.094189,9.262455,2.984599,-7.412374,6.243016,-3.151733,-8.786520,9.349472,4.284389,9.925530,-6.432272,-1.685923,9.194698,2.048136,-1.357780,-9.028021,-4.112274,-9.602360,3.510496,6.720495,2.367295,-0.308535,1.814875,-1.518838,-7.243319,-5.617245,6.876811,-7.548821,3.408768,5.595673,-5.013452,-7.663850,0.095159,-6.545480,-2.672727,8.967018,6.401585,5.826891,0.777842,7.457993,2.575906,-3.511474,9.723490,9.023222,4.563720,-4.633199,-9.076422,-6.192079,3.368089,5.491378,-8.919844,7.385395,-0.014705,-9.865334,9.179088,9.277140,-8.245322,9.889868,0.094974,-1.836384,6.849190,-9.613895,0.121850,4.118068,4.590638,-7.828015,6.987106,-8.831704,7.477036,-0.802051,-2.887035,8.667577,4.528631,-5.298507,-2.289428,4.509397,9.239955,9.492230,1.796748,-0.482437,4.634482,-0.974702,-1.206426,2.959416,-3.343215,-4.961894,0.836573,4.188605,-0.239239,7.332264,-7.019348,-1.232354,-6.132418,-6.080620,-4.188245,3.309100,-1.446226,5.412705,-4.555255,-4.334499,-0.370727,5.128750,-5.858246,-6.271426,3.006032,5.107314,9.479103,0.099744,-0.624973,7.128970,-4.303264,-7.618878,-3.717105,-0.873837,-8.552100,4.206384,8.784683,9.538750,9.347408,1.077830,7.262965,-6.517944,-7.698328,4.229679,-1.665084,-3.406527,2.209553,7.110409,-8.593507,-8.269095,-4.573886,4.662066,-2.246483,2.708078,-5.467997,-4.462830,-0.551402,-9.934042,0.260338,4.153041,-9.190962,-7.363413,-3.366065,-2.297349,4.382990], dtype = "float32")#candidate|2588|(396,)|const|float32
call_2586 = relay.TupleGetItem(func_2045_call(relay.reshape(const_2587.astype('float32'), [1540,]), relay.reshape(const_2588.astype('float32'), [396,]), ), 4)
call_2589 = relay.TupleGetItem(func_2048_call(relay.reshape(const_2587.astype('float32'), [1540,]), relay.reshape(const_2588.astype('float32'), [396,]), ), 4)
uop_2603 = relay.cos(uop_2562.astype('float64')) # shape=(5, 10, 10)
uop_2619 = relay.tan(var_2552.astype('float32')) # shape=(5, 10, 10)
func_1972_call = mod.get_global_var('func_1972')
func_1978_call = mutated_mod.get_global_var('func_1978')
var_2624 = relay.var("var_2624", dtype = "float32", shape = (180,))#candidate|2624|(180,)|var|float32
const_2625 = relay.const([[3,-8,-10,8,-5,10,-6,-3,-2,1,-2,5,1,-4,5,9,8,10,8,-9,9,-2,-2,7,-5,7,-1,-3,-8,-9,-5,-1,-8,2,1,10,3,-2,6,-7,2,-10,-8,3,-2,-1,3,-1,-2,-8,6,-2,-9,-2,-6,7,4,-10,2,10,-8,-10,-2,-3,-6,9,8,-9,-4,3,3,-9,-5,9,4,1,10,-4,-4,7,9,-4,-7,-5,7,2,-6,-6,10,10,7,-6,5,-9,1,1,-4,-9,9,2,2,3,-7,-2,-6,-10,4,-10,-10,-7,7,-10,-2,-3,-3,-8,-1,4,2,4,6,1,-2,8,9,10,3,10,9,8,-10,-6,7,-8,5,7,6,3,8,-9,-7,5,-8,-5,10,-8,10,-1,3,-10,-3,-10,-4,8,-4,-10,-7,1,10,2,-1,-10,4,10,3,6,6,5,-10,-3,-2,-5,8,4,-4,-7,9,-6,1,2,5,-7,5,4,-9,-2,-7,-9,5,-4,4,-1,-1,7,2,-3,1,-1,-6,-4,1,-5,4,-5,7,-5,-1,5,-3,1,4,-4,5,-3,-10,5],[4,-10,-4,-7,-4,-4,-9,6,-1,-9,2,2,-1,-10,4,4,5,-6,9,-2,6,-8,2,8,3,-10,3,4,-7,-6,-2,-8,-4,-8,8,8,5,-8,1,2,-5,1,-4,-3,1,-3,10,2,8,1,-1,7,-8,-2,-2,5,7,-3,-8,6,-8,4,2,5,7,5,4,3,8,-3,2,-6,-1,-1,-7,-10,-6,4,10,6,-5,5,-5,-3,6,1,-1,6,-8,-3,-6,2,7,9,-5,-5,8,-10,-10,3,-9,1,-3,-2,-6,8,7,-3,5,-2,-7,-9,-6,-5,3,2,6,10,2,2,8,-9,1,-9,-4,-7,7,5,6,-10,9,9,-5,7,-4,7,-1,6,8,6,-8,2,-10,9,-8,7,10,5,6,5,10,-1,-10,-1,-6,-2,-4,10,-3,2,-5,-9,4,2,-3,-1,1,-4,-2,-1,5,-3,-8,-3,-9,2,-3,-2,-4,-8,-3,2,10,7,2,-2,-1,-8,-7,2,7,3,3,-6,10,-4,2,9,3,-5,3,-3,-2,3,-3,7,-9,9,-4,8,8,6,-1,3,-10,8],[8,8,-4,9,-8,-7,-7,-8,3,6,2,-3,-9,-5,-7,-2,8,-2,3,-2,-8,-7,-7,-7,-10,2,-4,-5,1,2,4,-2,-6,-7,-8,1,1,-2,-2,9,-1,-6,-7,-8,10,8,-3,-8,-5,-1,5,-10,1,-3,10,-7,-6,-5,-3,-1,2,6,-10,-8,7,-9,-3,-9,10,9,5,-2,-8,-3,-10,3,4,7,2,-10,-5,3,7,-4,3,8,1,10,8,10,8,2,-3,-7,-6,-7,-5,1,-2,8,8,7,9,-9,-1,-7,-4,-2,-7,3,-7,4,-1,-3,-8,10,8,-5,5,5,5,-6,8,6,-8,-9,-9,6,-6,5,-1,-1,-2,-7,2,-2,2,6,5,-7,2,9,-7,-1,5,10,-1,-6,-9,10,5,-8,10,-8,7,8,-9,9,2,-10,8,-5,-1,1,-2,-1,3,-3,-5,-7,-4,10,-2,1,2,2,-1,6,8,2,-8,-6,-4,3,-9,10,5,-9,10,2,-1,-2,3,-4,7,10,1,-8,4,4,10,-1,5,-2,9,-9,-10,3,-8,4,-5,1,-10,-10,-10,10],[-2,7,-10,-4,-4,-9,3,10,9,9,8,-9,-10,-5,-5,10,-7,-7,-7,5,-6,-8,6,-2,-3,8,-2,-2,-6,-1,-3,8,-10,-8,-6,10,9,2,-7,-10,-7,2,3,-2,-2,-10,7,-6,5,-8,10,4,6,-5,-2,3,-3,-3,-8,7,-1,6,7,7,-7,2,10,7,3,1,6,9,9,-6,-6,-7,-2,-4,-7,10,5,1,7,3,9,7,8,-5,-7,-3,3,-9,5,3,-4,5,-4,-7,6,3,6,1,6,-10,-4,-8,-5,4,-2,-1,10,8,-4,-5,4,6,-9,-3,-10,8,6,-4,2,-10,-5,-1,-8,-8,-3,-3,-2,7,3,-8,3,-8,1,1,-10,-10,-3,-1,-1,3,4,2,-4,-1,1,1,-5,-4,-3,-2,7,1,4,-2,2,10,1,6,-3,4,4,9,-6,-6,7,3,1,-5,-7,3,-2,7,-6,-1,-8,4,-8,-3,-5,5,-8,-7,4,7,9,-1,4,-6,-1,-1,2,2,8,6,6,-5,-2,7,-6,-9,4,-8,8,-9,3,-9,-5,4,-8,-9,2,1],[8,-9,-2,-9,-8,5,3,6,-3,-2,10,6,-6,2,-10,-3,-1,-3,1,-9,9,7,-9,-1,-10,5,-8,-7,5,-4,2,-3,8,-6,-6,-7,3,10,-7,-4,-1,-6,-9,3,2,-1,5,-9,-10,3,4,-2,4,-6,-10,-9,-3,-9,-9,8,-2,-8,-3,-1,4,8,5,-4,1,-9,2,3,4,8,6,5,-7,6,-9,-4,10,2,3,4,6,6,-3,5,-2,-3,3,8,-10,-1,-3,4,6,-9,-2,2,8,9,-8,1,7,10,-1,-9,5,1,-4,1,3,-6,3,-4,-5,-4,-7,-3,-8,-4,3,9,-5,8,-5,7,9,2,3,-4,-1,3,3,2,-9,10,4,-2,8,-6,8,-1,-1,10,-1,4,5,1,3,1,2,8,3,-2,-9,-5,6,-6,1,2,-4,-5,4,-9,9,-3,-3,6,-10,-8,9,-7,-9,3,-3,-3,1,-6,-6,-4,-6,6,7,-5,2,-7,7,7,9,8,-5,10,1,-3,-2,-1,-5,8,-1,-8,-6,-6,-8,-1,-5,2,-9,7,10,-4,8,-1,-4,-4],[3,10,6,-4,-2,-3,3,-10,8,2,-9,10,-4,2,-1,-5,-2,-4,4,5,3,5,-5,-8,-2,3,-7,-1,-6,-8,-1,1,-1,-2,-1,3,6,9,2,-4,-6,-6,-2,3,-1,-6,8,-6,2,-6,-4,8,6,1,5,-4,6,5,8,7,8,2,3,-5,-7,-10,1,-10,7,6,-1,-4,-10,-5,6,-8,7,2,-9,7,-9,4,4,8,-9,3,3,-7,6,-1,-3,-9,-10,-2,-2,-2,5,1,-4,-1,3,3,3,9,1,4,-3,-6,-7,-2,7,-10,-2,4,-9,-10,-8,8,-2,-3,-9,9,-1,4,3,-7,-10,5,-7,9,-3,-8,-2,4,-5,9,3,7,10,4,-7,-8,-5,10,-3,7,6,8,-4,-3,9,-7,9,8,7,-5,-10,-3,5,6,10,3,-1,-5,-3,-7,10,5,-8,-9,5,-9,-8,-10,4,10,-3,2,-5,-10,5,1,9,-7,8,-2,-1,-8,3,-3,-7,-3,-7,2,-1,-10,-10,-4,-6,-6,6,-7,-8,5,4,10,-10,-10,7,-10,-6,5,-1,5,-9,-2],[-10,1,6,1,3,-9,-4,1,-3,-10,-9,-7,3,10,4,6,-2,1,-2,-8,-4,7,8,-9,-8,9,3,10,7,-9,-3,-4,9,-3,-10,5,7,-3,-9,3,-1,-5,-10,10,6,-10,-4,1,4,4,4,9,3,-4,6,10,-4,2,3,-5,1,5,2,1,-2,1,6,7,3,2,1,-7,-8,-10,10,9,1,-9,1,-10,-4,-1,10,-10,1,2,-3,-8,-5,3,2,-9,5,7,-7,-9,5,-1,-7,-9,10,-10,-8,5,5,-1,9,1,7,8,-4,-4,6,-7,4,-1,5,1,-8,-1,4,1,1,7,-1,-3,-3,-7,10,-4,-7,-3,6,8,-8,-8,-10,-8,-4,-10,-10,-1,7,4,9,-6,-2,-9,-10,-2,-7,-5,-1,9,-7,-10,3,2,9,-9,-3,-5,3,5,4,-2,-10,-9,9,8,-8,-5,-2,-8,4,-9,4,3,-9,-9,-6,3,9,8,-9,-5,5,-5,8,7,-5,-8,2,6,-10,6,7,3,-1,-5,-5,7,-2,-8,8,-4,-4,1,6,9,2,3,5,7,-4,8],[5,-1,10,9,5,-2,-6,4,8,-7,9,10,-5,-3,1,10,9,-5,3,8,9,-8,10,-8,-9,1,-4,-3,-9,-10,8,-8,-5,5,-1,7,-2,5,-1,2,-8,8,-3,-5,-7,-5,-6,1,8,-9,-10,8,-3,4,8,4,7,1,4,4,-10,-8,2,8,-7,10,3,-7,-1,-10,5,6,-9,3,3,-7,-6,1,-4,7,-4,-9,5,3,7,6,9,-5,10,-2,-5,8,-3,9,-6,1,5,6,7,7,-5,9,6,-4,4,-1,-6,10,6,9,10,-1,-3,5,8,-6,-9,-9,-9,-3,-9,-1,1,-6,-3,-8,-8,-7,8,1,-6,-9,9,9,-8,-10,7,4,3,7,-5,-6,-4,4,-7,-7,9,7,1,8,10,-8,7,5,10,-5,-8,9,-6,-5,-7,3,8,8,7,9,-1,-4,-9,-8,2,-5,4,2,9,2,-10,4,6,7,5,1,-5,6,-4,2,-8,6,-2,-4,8,9,-1,-7,-4,-10,-2,-6,-4,8,9,-5,8,-10,4,3,2,-1,4,1,2,-8,-2,9,9,5],[-9,4,6,10,-2,1,3,-8,-7,5,-10,-4,-9,10,2,3,-8,1,-5,-1,1,10,3,3,6,-1,-2,9,-8,7,-6,3,1,7,4,2,1,1,9,4,-1,2,-2,5,3,1,-4,3,-10,-9,8,4,-3,-3,-9,8,6,5,4,-7,2,4,4,-9,-8,3,-2,-5,-1,7,-9,-2,-6,10,-9,-7,-5,-6,8,5,6,2,-2,2,7,-5,-6,-1,6,-4,-8,-7,-4,4,-10,8,7,-5,10,4,9,-6,-8,1,8,-10,-8,1,-4,6,4,-2,-5,-1,6,-2,7,-2,-5,-9,-10,-1,-10,2,5,-7,-3,1,-6,5,-10,-7,-7,3,1,4,3,-2,8,-6,-2,-4,-10,5,9,-7,6,-7,-2,2,-2,-7,-6,9,-10,6,8,9,7,5,1,-5,8,8,2,-5,10,3,-10,-7,9,-6,-7,8,-6,-10,-7,-4,6,-8,3,5,7,9,-2,10,4,-10,-9,-5,-1,4,9,-4,-1,5,6,-9,-10,10,7,-3,6,-1,2,-1,-8,-3,-4,-2,-9,-3,9,-8,10,-10],[10,7,-9,-10,-4,-3,8,1,-3,1,2,-7,-3,9,-6,2,4,-9,-8,5,-2,6,6,-3,10,3,7,-2,-6,8,2,6,-9,-3,6,9,-8,-9,10,-3,8,-2,-7,-9,-7,-5,-5,7,9,-1,7,2,-6,-10,-5,-9,-1,7,-7,-1,3,5,10,-2,-3,-4,6,8,7,8,-2,-4,-10,-3,9,-3,-1,-2,2,7,-8,8,9,6,3,-7,-3,-2,-3,-9,-10,-7,-1,-1,3,-8,1,7,-1,5,8,-3,-4,-3,-1,-1,7,9,7,10,-9,2,-4,9,3,1,5,-4,8,-10,-2,-7,9,6,9,-7,-4,-8,2,-4,-1,-8,-9,-9,-10,6,-10,-10,3,6,-1,2,-5,-6,8,-2,6,-9,-10,2,7,-1,-4,-5,-8,3,-7,-9,-5,-9,-4,4,-9,-5,-3,-1,8,7,-7,-1,5,-6,-8,5,9,-6,5,3,5,4,-4,8,9,3,8,-2,-9,5,5,-1,-4,-7,9,2,5,-3,3,10,7,-1,-1,-9,-1,-10,-4,1,9,8,6,-3,-8,-2,10,-6,-9,-3],[9,-1,-6,-7,3,10,-3,-2,-8,10,3,-8,5,-1,2,5,6,10,-8,-4,-4,-4,5,-6,1,1,-9,7,5,-10,-2,8,10,1,4,10,-2,-5,-8,-1,8,-5,3,4,-1,-6,-9,2,10,-9,3,-4,-4,3,1,-3,6,-7,1,6,6,-7,-6,-4,6,-5,-5,-3,8,-10,-8,8,-2,-2,6,7,1,5,-4,-4,-4,-7,-7,-5,4,4,2,-5,-6,-9,4,2,-9,3,-6,2,-7,9,9,9,-1,7,-4,10,-1,10,-7,3,9,-9,-4,-7,2,-4,-9,-6,9,-6,6,-3,-6,-4,-7,-9,2,5,1,-6,-7,-3,7,-9,-3,-9,2,7,7,1,8,-4,9,6,-1,-2,5,7,5,6,2,6,-7,5,6,-10,7,-5,-5,-6,-3,5,2,-8,9,-4,9,-8,-6,-2,9,5,8,-2,-10,9,5,-9,-9,5,-3,10,2,8,-3,8,-4,9,4,-5,10,-8,-2,-5,8,-9,-10,10,-9,7,1,-5,10,-7,5,-1,-9,-3,7,-10,-7,-5,9,8,6,-1,3,-1],[10,-9,1,-2,-8,9,-3,10,9,-9,-1,-6,6,-5,1,-4,-4,-6,1,-5,-2,-6,-7,-5,4,-3,-2,-3,6,7,-1,-8,4,-2,-3,5,3,-10,-8,7,10,-6,-8,-1,6,-2,9,-2,6,-9,10,4,-5,-6,-1,6,2,4,-2,6,4,-5,-2,7,10,8,-10,-5,-9,10,3,-1,-2,9,-1,2,-5,-8,3,-4,1,-6,4,-6,4,5,5,-4,-3,1,-10,-9,9,3,-5,6,8,-7,-3,7,2,-5,-8,-2,-6,4,5,2,-3,7,-1,-3,4,3,-4,7,4,3,-4,4,-9,5,-2,-9,1,10,-8,3,5,-3,8,-9,3,8,-8,-7,-1,-2,-9,-7,-4,2,-1,5,-1,-9,8,5,9,-9,6,-3,-8,9,5,-8,4,-4,-7,3,7,10,9,9,7,-2,-5,9,3,1,-3,-8,10,-1,10,4,-5,7,10,-1,-5,9,1,3,5,1,-2,-2,-2,-7,7,2,-6,8,-4,-2,-2,-8,8,-7,5,10,7,-8,-4,-3,-6,5,-3,-9,-1,-7,3,-8,-7,5],[-10,-9,-6,-8,-2,1,6,-2,-10,6,-6,-6,10,-2,-6,-1,2,7,-7,-8,6,6,7,2,3,-9,-3,-9,-9,-2,-10,3,-2,-1,5,-7,9,6,-5,3,6,-6,7,2,6,10,6,1,-4,-7,2,-4,9,-8,6,-2,-3,1,-6,5,8,10,-7,-2,-3,-1,-2,7,5,-8,9,3,-8,2,-1,6,10,-1,-8,1,-1,6,7,9,-3,1,6,-3,-2,8,2,3,3,3,9,1,-6,5,4,-3,10,-6,2,1,-6,7,5,4,-6,-7,10,-4,7,-10,-3,8,1,-10,-5,6,9,9,-5,-2,-1,5,9,10,1,8,4,-9,-10,-7,7,-4,1,10,10,9,1,3,-5,7,-2,2,-1,-1,10,-5,3,5,7,-2,-7,6,-6,9,1,-9,-3,9,2,6,-9,-10,2,-6,9,6,10,-6,-1,8,-3,7,8,1,-7,3,-7,8,-6,-8,4,-5,-6,-1,-7,10,-7,-7,4,-6,-6,5,-2,5,-7,7,7,-6,-2,-9,-7,1,8,1,-8,3,8,9,2,1,7,3],[-9,-6,-7,10,-5,-9,10,7,9,-4,-1,-10,-7,2,-1,5,-5,1,-5,5,-3,-7,6,-3,-5,3,-9,8,-6,-7,5,-6,-4,-2,9,3,4,7,3,5,6,-5,-5,-1,5,-7,-2,1,-2,-7,2,7,9,6,-5,-1,2,-5,10,7,6,6,-9,-5,1,3,1,1,-5,1,9,10,9,8,3,-5,-9,6,9,10,3,-5,-5,-4,3,-10,-7,-4,8,-6,-7,-2,1,6,-1,-1,-10,-1,-5,5,10,2,6,6,10,-8,4,-3,8,-6,-4,5,5,8,1,-8,9,-2,6,10,1,-2,8,1,-5,-6,6,-4,5,3,-7,9,-2,10,9,3,10,5,3,5,-5,-10,2,3,7,-5,10,-8,-3,10,10,1,1,9,2,-3,-5,-9,6,-2,10,7,1,2,-8,7,-8,-10,-6,4,-1,6,-9,-10,-9,-9,-2,-10,-6,9,5,-1,-4,-1,-8,-10,-1,4,1,4,-10,10,-1,-5,1,10,9,8,-10,6,3,8,4,1,-10,7,9,-2,-8,-7,2,-6,9,-6,4,-9],[-2,8,-1,-3,-7,2,10,6,2,8,3,5,-9,-10,-7,-9,-6,-4,7,9,-10,1,5,-9,-3,1,10,-5,-8,-1,2,5,6,-6,-9,-8,-7,10,-6,-1,3,-2,-7,-1,2,2,-1,-3,-8,-9,-7,7,-7,8,-5,2,-8,-2,-3,-3,-6,-10,-4,1,3,7,10,4,1,1,-10,6,9,-4,-3,-9,2,6,-2,7,1,-5,-10,-8,-2,8,4,-1,-6,-9,-2,9,-8,1,2,-3,-2,3,1,4,2,5,-8,3,3,-2,-10,10,-6,6,-9,-2,-1,-4,8,-6,-9,-8,-9,-10,5,-7,3,-3,-10,-8,1,-3,-4,-5,-6,3,-1,-2,-6,-3,6,-5,9,7,-10,2,2,-4,-2,-1,1,4,8,2,-10,-4,9,5,-9,9,9,1,-5,-10,-5,5,-6,7,7,-8,8,-5,-1,-5,5,2,-5,7,-9,9,7,-9,5,7,-7,8,6,10,-4,-10,9,2,4,-4,-6,8,-8,-8,-2,2,-9,5,-2,3,-2,-4,4,4,5,2,2,-7,-4,3,10,-7,6,2,-9,-5],[-7,-1,-6,8,3,-5,7,-7,-6,9,4,5,-10,-9,4,-9,2,10,4,-9,8,-6,-7,6,-1,-9,2,6,-1,-10,-8,5,-10,-8,-5,-3,-3,7,-2,-3,-9,8,4,-5,7,-3,-6,-5,-5,1,1,2,5,-4,-2,7,-7,5,7,10,5,10,-2,-8,-7,-7,-4,-2,8,-5,-1,4,-9,1,8,1,5,-7,-6,3,5,-4,7,-10,-4,-5,-1,-4,7,6,9,9,9,-2,-10,-2,3,5,-6,4,4,-4,8,3,7,1,5,1,-5,-2,-8,-9,2,10,1,-5,-7,7,-1,3,10,-4,-3,10,10,2,-6,-8,6,-4,5,-3,-10,-8,-3,-7,-2,-7,-9,-2,10,-8,4,5,-7,-9,8,-5,-2,-9,3,-7,10,1,-2,-10,-6,7,8,1,10,-8,-2,9,5,9,6,2,-10,5,5,-4,-8,10,-4,-1,-3,-5,3,8,-5,-7,-5,-7,1,6,-1,-6,1,5,1,10,-7,6,2,-10,-5,8,-6,-4,8,5,-10,8,-9,7,-1,3,-5,-7,-4,-3,-4,8,5,8],[-2,5,-6,-3,8,-4,-8,-6,-5,-1,-2,10,5,-7,-10,8,-10,1,-7,-10,6,-5,-10,-1,-4,7,-7,3,5,-4,6,4,-6,1,-1,2,6,6,-8,2,7,9,6,-8,3,5,-6,9,-6,-5,3,8,5,-5,9,5,7,-10,8,-6,-9,-4,2,7,4,-8,-9,6,10,-7,9,5,-7,-10,4,-10,9,-8,-9,-2,6,10,6,-1,7,7,1,-1,8,7,-9,7,-3,10,1,-3,-2,4,10,6,3,-3,-5,5,6,-7,9,5,-10,-1,7,-8,8,-8,-7,-8,-10,-5,7,-10,1,10,-1,9,-7,2,4,-2,-10,-5,-7,-7,5,-1,3,-5,-9,4,7,-3,4,8,-5,-4,-3,4,-3,-6,-5,9,8,-2,-9,9,10,2,-9,-3,3,9,-8,5,-4,-8,-7,8,-2,-10,-9,-9,-3,4,-1,8,8,-9,2,6,6,6,-4,7,-5,9,10,-4,8,6,-8,-3,-2,1,-10,-10,2,10,-10,-1,7,-10,7,9,5,5,10,10,-2,-5,-9,-1,-1,-8,-9,8,1,3],[4,-3,9,-10,8,2,2,-4,-4,-1,-7,8,10,-4,-1,-6,10,4,9,-10,-6,7,-2,7,8,-1,-9,-1,-4,-9,-1,-2,8,4,-9,-4,-9,-1,4,6,-9,6,-7,-8,-1,6,4,7,-3,9,5,7,4,6,-9,9,1,-6,4,1,-3,-9,4,-10,7,9,3,-8,5,7,6,9,-3,8,-1,3,6,4,10,-7,5,8,9,9,10,7,3,-5,-3,4,-2,9,-10,7,10,6,-7,5,2,1,1,-10,-4,-1,-8,10,-1,-7,3,-1,-8,-8,5,3,1,-9,-2,5,4,10,10,-1,10,-1,1,-5,3,6,-9,3,-4,10,-3,-1,-2,8,-2,2,4,4,9,6,3,8,-2,-1,7,-2,10,-9,8,-4,-4,-2,-4,-8,6,-5,-8,2,-7,-6,-6,-7,4,1,-3,2,-3,-10,1,-10,-1,-5,-9,1,-9,10,-7,-4,-3,3,-9,-3,-9,9,-10,8,-5,2,-9,-10,2,-8,7,10,-6,-5,-7,-9,-3,8,-9,-5,-9,-10,2,1,-2,-2,10,10,-6,2,5,-2],[2,-2,-8,7,3,-8,-7,-10,-7,-7,-8,-4,4,-10,9,-7,-3,2,-5,-9,-4,5,7,10,10,10,4,2,1,-7,5,-9,-3,10,-10,8,7,5,1,-5,-3,-10,-2,-5,6,3,-5,10,5,-8,8,-9,1,8,-1,6,-1,-1,1,-5,-9,8,3,4,5,-3,9,-1,-7,-4,-3,2,-9,6,10,-6,-10,-3,-10,10,-10,-2,4,9,10,10,4,-7,7,-2,7,-6,-2,-9,-7,-8,2,5,-3,9,-6,9,3,4,1,6,3,4,-4,-6,2,9,-5,-3,-9,-4,-3,6,10,5,5,9,7,3,-8,4,4,5,-10,-10,1,5,-8,10,-10,-9,-10,4,4,1,-6,-2,-10,4,3,6,-9,-8,1,-2,6,-9,2,4,-1,-7,-9,9,-6,-7,8,-5,-6,3,4,2,9,-6,3,8,-4,10,6,3,2,-2,-7,9,-3,-3,-10,-7,-4,-1,-3,-2,-5,-10,-2,4,-7,6,5,-7,6,5,7,-6,-5,10,9,4,-4,7,-9,2,9,-2,-1,-5,1,4,2,-8,10,-4],[2,3,4,4,10,1,-1,-4,-2,-1,8,10,7,10,10,6,-4,9,-8,-1,-6,10,5,-10,-4,1,-8,6,3,-5,-10,4,-10,1,-4,10,7,9,-5,-3,2,3,-7,7,4,10,3,-5,-6,2,-1,2,-2,1,2,8,-8,-5,-1,2,4,-7,-7,-3,3,7,-8,1,1,-9,8,6,2,10,4,7,5,9,10,-6,-5,-6,-5,-5,1,-9,5,4,7,-1,5,10,-5,3,-9,8,-4,-1,1,5,-1,-10,2,-6,-5,1,-4,-1,10,-4,-3,-4,-7,5,-2,10,5,-2,4,-5,2,1,6,4,-4,-6,-1,3,7,5,-8,-1,-7,-9,10,1,1,7,-4,5,1,6,-4,-9,-6,-8,-3,9,-3,-10,4,4,-5,-5,6,-6,3,-9,10,-8,6,3,5,1,10,-3,-5,2,-2,9,-8,4,-9,-8,5,-7,2,-2,10,6,-7,6,6,1,4,-3,-5,6,2,-2,2,9,9,-10,5,1,-3,-5,5,-4,-6,-3,-7,-6,3,-7,-9,-6,8,-9,1,8,-9,2,8,2],[4,6,4,-2,2,-1,-6,1,-4,8,10,-9,8,2,-7,10,10,5,-10,1,6,4,3,-5,-4,2,10,3,-3,4,9,-3,1,-5,7,-4,-9,5,4,9,-7,-3,4,-5,-1,9,4,-1,2,-6,1,3,8,4,-10,-9,-7,5,8,-10,-10,3,1,-9,-9,3,6,-1,-4,8,1,-4,-2,10,9,-1,9,3,7,4,-8,5,2,10,-5,3,-8,4,4,-9,6,-3,3,6,7,-5,8,9,-8,-10,-7,-8,-8,4,8,6,-3,-10,5,6,9,-7,1,-1,-6,1,3,-10,-6,4,8,-10,7,7,8,-3,3,6,-7,3,7,9,-7,-9,-3,-7,-3,2,-8,3,2,-5,-8,-1,7,8,-1,-1,6,-1,5,2,4,-9,4,-10,-7,-5,7,10,1,-7,-5,-3,10,-1,-10,2,-6,-8,-4,9,5,-6,2,-6,4,-7,10,1,2,5,-5,-9,10,3,8,-5,8,5,9,-4,3,-3,1,-4,-6,-8,8,1,-5,-9,-10,7,-8,-7,4,-2,-3,9,-1,-9,-2,7,2,-7],[4,-1,-2,2,1,-7,-3,1,3,9,4,8,-5,-5,5,-6,-10,5,7,10,-9,2,-3,7,4,-10,6,-4,5,7,-3,-10,2,-3,-3,7,-9,3,4,9,-7,-6,-7,5,-2,-1,-7,-6,-4,-10,-3,8,-7,-5,10,1,-1,4,7,-9,2,-4,10,-10,10,-1,8,-6,-10,-8,-4,-2,7,-4,-5,-3,-4,-8,8,1,7,-4,3,9,-10,-6,7,-1,3,-1,8,-5,-3,-7,10,-1,-9,-1,-5,-6,9,-1,-1,3,8,10,7,10,-8,-1,4,5,-6,-8,9,8,-9,6,-1,-3,2,5,-9,-9,2,3,-3,3,-7,2,8,-3,9,6,10,-9,3,2,-10,6,1,10,-10,-3,8,10,-5,3,-6,-6,-8,-1,-8,10,-3,2,8,10,-6,4,10,10,-10,-1,-1,3,1,-8,-6,-9,-5,-5,-4,2,9,6,9,-9,8,-5,9,8,-1,-3,5,6,-4,4,5,9,-1,7,10,8,8,-7,-1,-6,-9,7,-10,5,-3,3,-6,-4,-5,8,-7,-3,2,-9,-3,5,-6,8],[-7,-2,-4,8,7,-9,-5,8,-3,-4,-1,8,-1,-9,-7,-5,-2,7,-3,-7,9,3,-1,5,-3,1,-5,9,-3,-3,7,-7,8,-6,10,-9,9,2,-4,6,-5,3,-5,6,-3,10,-8,1,-2,-4,10,1,7,9,-8,1,1,3,-8,-6,7,-1,7,-10,-8,-3,-2,-10,-8,2,-4,-1,-7,-3,-3,-6,-6,-7,10,6,-6,10,3,-8,-7,-9,5,7,6,7,-10,-2,-1,-1,-10,2,-6,-5,10,-2,-4,-1,-4,-1,8,-2,2,-7,6,-5,-7,-2,9,3,-1,-8,9,5,8,4,5,-6,-1,-1,5,1,3,6,-1,9,6,-8,-7,-8,1,10,-7,3,1,5,10,-9,-1,2,4,5,-3,4,-6,-2,2,2,-10,9,1,-7,-10,-3,-1,-3,10,-4,-1,-2,1,-3,-8,4,2,-9,-7,-3,5,10,-4,-1,-2,-9,3,1,5,-9,-9,-1,8,5,10,-2,5,-1,6,-5,-6,1,-6,-5,6,-2,-7,-7,4,-10,-9,9,6,-7,1,1,6,9,4,-3,-8,-7,-9,-1],[6,9,-6,3,6,6,-2,7,1,-2,-9,-5,-9,5,-9,-2,8,2,8,7,7,-3,2,-9,-5,-8,-7,3,-7,5,-5,-1,-6,10,-10,2,-2,-8,-7,7,-1,8,8,-3,2,-1,5,-3,-6,-7,-1,6,3,10,-3,4,2,2,-3,-4,-3,3,8,-6,-8,3,-3,-3,-4,-8,9,-3,-2,-8,-7,2,-9,5,1,-2,-8,8,-3,-8,3,-6,-8,3,1,4,6,-10,-1,2,10,-10,-6,-10,9,-8,5,-7,10,-10,-1,-2,2,-2,9,-4,-8,7,-3,5,-6,6,-6,2,-3,10,9,-9,-4,-4,4,9,-4,-8,-3,3,-7,-1,-4,-10,5,8,-1,-5,-9,5,-10,-7,-3,5,9,7,7,-8,9,7,-9,-8,-4,-3,-3,-6,3,7,-8,3,-10,-1,6,-9,9,-9,-3,-7,9,9,8,-4,9,-8,4,2,10,1,7,1,6,-4,-6,-5,3,-6,7,4,1,-3,-3,-9,2,-1,9,-5,-3,-3,2,-5,-10,-7,-10,7,5,8,-6,-5,8,7,9,6,9,-10,-7,-7],[5,-8,-7,8,-4,1,7,8,1,7,-5,1,-2,8,-5,8,7,5,-10,5,3,-6,4,-8,-9,-7,5,2,-9,9,-3,2,-5,-5,3,-1,-8,7,-10,8,-9,6,3,5,8,5,-1,3,-5,-2,-10,7,1,1,10,-3,-8,-6,8,-2,3,8,-4,1,1,2,-8,9,-2,1,4,2,2,3,-9,-6,2,-8,7,10,5,-1,-10,2,-3,-5,-4,10,-6,6,8,10,6,-10,9,4,1,-9,-6,-2,-2,7,-5,2,8,9,-9,-7,8,1,7,-5,9,-9,5,-3,10,4,8,9,5,-3,-6,1,-10,-3,-6,-5,-2,-9,6,3,5,-9,3,-9,5,-3,4,9,6,9,10,-6,-8,1,-10,-8,-2,-8,-7,5,8,-7,2,4,-7,10,9,-2,-5,-1,-7,-10,7,8,-4,10,-3,-4,-2,-4,5,8,2,-1,5,1,-10,-3,-10,5,-5,8,1,-2,-4,3,10,3,3,8,5,-10,-2,-4,-3,6,3,6,8,10,-4,-9,-6,6,-6,5,-4,6,7,8,-10,-10,10,8],[5,8,-3,-4,9,8,6,7,-10,8,5,-9,-2,-8,8,8,6,-3,-5,7,8,-1,9,-6,3,6,10,4,8,-4,-10,10,-10,-6,-9,-1,8,-3,2,-8,5,-4,3,7,-2,10,5,1,-10,-10,-1,9,-3,-8,4,-1,-2,-4,-6,8,3,-9,5,-2,8,7,-3,9,-9,-2,-5,-9,-1,-3,3,-3,7,-5,-4,9,-2,-1,1,2,9,10,-10,-2,-2,-8,-6,3,4,6,-8,-2,-1,5,5,3,-3,9,-4,4,7,2,2,-9,-7,8,1,-6,-5,6,2,3,2,1,-4,-3,7,-6,-3,7,1,-5,-7,5,-4,1,2,-1,5,-2,9,2,1,6,3,1,-1,6,-7,-8,-4,9,3,2,-4,-1,-2,-8,10,-4,-7,7,-3,-6,6,3,2,-7,4,7,6,10,8,8,1,-3,10,8,4,4,-7,9,-1,-6,-8,4,8,9,-1,8,-2,2,-10,3,-2,4,-6,-9,-9,-3,-10,10,-10,-6,9,-4,-4,1,7,-7,-3,-10,-4,-7,6,2,8,3,-3,8,4,3],[8,-1,-7,6,1,-10,-5,-2,8,6,-7,3,-10,4,-3,-2,-10,-8,3,-9,-7,9,-8,2,6,4,-7,-3,-10,-10,3,-5,-5,2,-6,2,9,-5,4,-5,-7,4,-7,-10,-6,-1,-4,-4,1,9,-6,-1,6,-4,-7,-3,-9,8,-3,-5,1,-10,4,8,-1,-3,9,3,-3,-8,-5,3,-5,4,-1,9,-6,-9,-4,-6,-3,3,4,-9,-1,7,9,4,3,4,-6,8,-3,-2,5,3,8,1,-9,1,1,-8,10,-4,1,-8,10,-8,-4,-1,10,-6,9,-10,-2,-10,1,-1,1,5,-3,8,-1,-6,9,-4,3,-7,1,-1,-8,-6,-1,1,2,4,3,7,-2,-8,2,10,-6,-8,-4,-10,9,5,-2,-2,4,-8,-1,10,-1,4,4,1,-3,-7,-7,1,-2,6,3,-6,7,6,10,1,6,-7,1,10,-4,-1,3,-8,8,-7,-5,10,9,-10,-3,10,-8,2,4,3,1,10,-8,9,2,1,-8,-9,-8,-6,10,4,5,-7,-10,-9,-6,4,-7,4,-6,-9,5,-3,-7,-3],[7,6,3,-2,-6,3,10,-8,8,-6,-4,-1,3,1,5,8,1,-5,-7,-9,-8,5,-10,4,-4,4,-7,8,-9,3,-2,5,5,2,-8,5,3,-3,2,3,-2,-7,-2,-1,1,-4,-5,8,10,1,1,4,-5,-9,6,4,-8,7,3,2,3,9,-4,7,-5,2,4,9,2,-8,-1,8,-3,-3,4,2,-9,7,-8,-9,-5,-8,-6,-10,-9,9,-1,1,-2,2,-10,-5,-7,-6,9,5,-6,-4,-2,-3,5,10,6,9,10,6,-10,-10,-7,10,-2,1,10,2,-2,-4,4,-10,-7,-10,4,6,-1,1,-1,-4,-7,-10,-10,10,7,8,10,-4,9,-4,4,-9,6,-2,10,-1,1,-6,6,-3,-10,6,9,6,4,2,-4,2,10,9,10,-9,-3,-9,10,4,3,9,10,1,-9,-3,-6,5,8,8,-3,-6,1,-7,-7,1,1,-3,9,-6,-9,-3,1,-4,9,-5,-10,-3,6,2,-3,5,-4,6,4,-4,-8,-9,3,7,5,6,-5,-6,1,6,10,-9,-4,8,8,1,6,-6],[-1,-3,-7,2,10,-4,-4,6,-6,8,1,-7,7,4,8,-4,-2,-7,-6,2,-7,-8,1,-6,-8,-6,-2,9,-3,-5,-4,1,-6,7,-9,9,-9,10,-8,6,5,-6,-9,8,-9,-2,-4,8,-5,-3,6,-4,-8,3,-3,3,-3,4,-7,3,-7,-8,1,-2,-1,-3,-8,9,3,3,3,3,8,-9,2,-8,8,-2,2,-7,1,-7,9,7,10,-8,-8,10,-10,9,-2,3,-3,-2,2,-7,1,4,-9,-4,10,3,-4,-2,-3,-8,-9,6,-9,8,-10,-6,8,3,-10,-8,8,8,4,8,-2,2,-1,-5,9,-2,8,-9,6,6,8,6,-5,2,6,-9,-8,10,-1,8,10,-10,7,-7,-1,1,-8,7,-3,5,9,-10,4,6,6,-5,3,-5,5,5,4,7,-3,5,5,7,-3,3,-6,-1,3,1,1,8,7,-4,-9,4,5,-10,-1,-6,-4,10,-8,-4,-8,10,-10,-5,-4,-1,10,-7,-7,7,5,-2,4,3,-2,-4,-2,10,-3,-3,6,1,9,4,6,4,7,-4,-10,3],[-4,4,3,9,1,-4,4,-6,3,1,-1,5,-2,9,4,4,10,3,2,-1,4,1,-9,10,-6,5,7,3,7,-1,-5,6,-3,-1,2,9,5,1,8,10,-4,9,-3,1,6,8,7,9,6,6,-1,-2,-6,4,8,-5,-7,6,-7,-9,-8,-6,-2,6,6,5,-8,8,10,7,-6,-2,7,4,-4,-10,-9,-9,1,10,-9,7,-2,3,-6,1,3,4,1,7,-10,-10,-3,-1,-6,4,-8,5,7,-3,8,-5,-9,-2,-9,-8,6,-8,-6,-3,-2,8,-9,9,8,-9,7,-7,4,-7,-8,2,10,1,10,8,3,1,6,-8,-1,-3,10,5,9,9,-6,9,2,3,4,-4,-7,8,3,10,-2,4,-2,8,-10,7,9,-1,-8,2,6,-8,1,6,2,1,6,-6,2,-10,-2,-8,2,3,-4,1,-3,2,-7,-9,4,-2,3,9,-3,-10,5,-7,9,-9,7,4,-1,3,5,-6,1,-9,6,-2,8,-4,-9,-2,-3,1,10,-9,4,-6,3,9,-10,8,8,-4,1,-9,-1,1],[1,1,9,-10,-1,3,-10,7,1,-5,5,-5,-7,1,7,-9,5,-10,1,9,-10,-5,-3,10,8,-4,3,1,6,-8,-3,-5,-1,5,7,-4,-6,-7,1,-4,-3,4,-8,7,-9,10,4,-2,-2,-6,1,-8,-7,8,4,-7,-2,4,5,5,8,6,5,-8,-5,8,2,-2,2,-9,4,3,6,-6,-9,-5,-10,-1,-8,-2,1,8,-5,-4,-10,1,-8,10,2,-5,8,-9,10,3,-9,1,-2,-5,9,4,-4,-5,-9,-4,-10,-5,-8,5,4,-6,-3,-5,5,-2,1,6,-10,8,4,4,3,-2,-2,9,-7,1,3,4,7,-4,1,6,9,-3,-7,8,-4,1,9,6,-6,-3,4,-8,-3,-3,-2,-6,-2,5,3,9,6,-3,-9,-9,7,-5,9,-4,-4,5,-4,9,9,7,-9,-9,-6,8,-3,-2,8,1,-1,-10,-10,2,-5,1,-5,5,-3,-7,-7,6,-1,-10,6,-8,4,1,-2,-7,-2,-2,7,8,-2,-10,-9,8,-5,-1,-8,7,7,-6,-8,8,3,6,-7,-1,1,-5],[10,-2,-2,5,4,-1,-9,-1,-2,-9,-7,7,1,-3,1,-5,-3,-7,2,4,5,8,-4,1,6,-1,6,8,-5,-10,-1,9,-3,-7,-10,10,8,-9,5,-8,-1,5,-8,7,-6,-2,-3,8,-9,1,-8,7,1,10,-8,-8,-9,8,-7,-3,-3,9,7,-2,-4,10,-5,2,2,1,-2,9,-3,-9,2,-5,-8,-1,-4,3,-5,2,9,4,-5,9,6,-9,5,-9,-1,-3,9,-3,-6,-10,9,-1,-7,-10,-1,-10,-7,8,-10,-2,-3,7,9,-6,-8,6,-10,8,3,8,6,-3,-10,6,7,-8,-5,2,-6,-10,5,-4,4,-2,9,-1,9,-8,4,-8,6,-9,2,-4,10,-5,-2,1,10,-3,3,-3,-9,-3,7,-1,-7,3,-4,10,-2,2,-3,-2,-6,3,8,-2,-9,9,6,10,-2,1,-1,-1,-5,1,-6,4,-7,-9,-2,-3,8,8,1,5,2,-9,-8,-8,-3,-4,1,9,4,-2,-1,-9,6,-2,5,10,3,10,2,-6,-8,-4,-8,-6,2,-1,4,3,7,-7,-1,10],[8,9,10,5,-6,9,-3,-8,-3,-10,-9,7,8,-8,10,-5,10,8,-9,-9,1,1,-3,7,-8,-2,-9,2,-2,-8,-2,3,-9,1,-2,-7,8,-5,8,6,-10,-2,-9,8,-9,-8,-1,3,9,-10,-6,-4,-4,5,2,8,2,-4,-6,-4,1,6,-2,4,2,-2,10,3,6,5,-9,-1,5,-4,8,-8,2,10,10,5,7,-10,-7,10,3,3,-10,-5,-10,8,6,8,9,-4,-4,-4,-10,8,9,1,5,4,-8,2,7,-9,-7,3,-7,-8,-7,3,-7,5,1,10,9,3,2,-7,-5,-3,3,10,-6,4,3,1,8,-7,-1,5,10,7,-3,-4,3,5,-5,8,5,5,9,7,-3,8,-1,5,-3,5,9,6,-9,7,-6,-5,9,9,9,7,2,7,-8,-5,7,7,-1,5,4,4,-9,2,-3,5,-9,-6,-8,4,-5,7,3,7,10,4,6,-5,10,-2,-8,-5,-1,-10,3,-5,3,10,9,-1,-1,-3,4,-3,-3,5,4,-2,10,2,-4,-4,10,-6,-3,-5,10,3],[-4,-8,1,-2,-5,8,6,1,-6,10,10,4,-1,-10,-7,-6,-9,-1,10,-5,-10,2,-4,6,9,7,-10,-5,-10,-3,-7,-1,3,-7,5,-10,7,-1,-7,1,4,9,9,-6,-8,9,8,-4,-1,-6,6,-3,9,4,-2,-4,-2,-10,-7,-1,5,-2,9,-8,10,-9,1,7,-8,6,5,6,-2,-8,5,6,1,-7,-8,1,8,-2,3,-8,10,1,-3,5,-5,6,4,2,-4,6,-3,-7,8,-9,-1,-2,-1,10,-9,-1,8,6,1,-7,-8,-6,9,-3,5,10,9,10,-4,-3,-3,-9,2,-3,5,10,1,6,9,1,-1,1,10,1,-2,-8,1,-8,-3,9,-10,-1,3,5,7,6,-4,10,-10,9,-9,1,-2,-4,9,-3,2,-2,-5,7,-2,2,1,1,4,5,4,-5,4,-3,3,-4,2,-10,-6,9,-9,3,4,3,-1,-3,-4,-3,-8,-3,-2,5,-6,3,1,9,4,10,-5,7,-3,5,9,-8,-4,-7,10,2,-9,10,-10,10,3,3,-6,6,-1,7,-8,-6,-5,-1],[-8,-5,-10,7,-5,4,-10,6,7,3,4,7,-4,4,-7,8,-8,2,-9,-9,-7,-10,10,-3,9,-5,8,3,-7,5,4,1,8,1,4,10,3,-10,-8,-1,1,-10,-10,-2,1,-10,1,-6,-7,-4,7,4,-8,2,-9,4,9,-10,-8,3,-8,-6,-6,-5,9,4,7,-5,-4,10,-10,-7,8,-7,8,6,4,-4,-4,5,-10,1,-9,-10,-5,-10,5,-5,3,-9,-1,8,7,-10,-10,-6,4,-6,4,-9,8,-6,-7,6,-3,2,10,-3,-9,-9,8,9,-3,-6,-1,-7,-4,-2,4,-10,4,2,1,2,8,1,5,7,-5,6,-8,6,6,3,-7,8,7,5,5,8,-9,7,-6,-1,-7,-8,-9,-7,2,4,4,-9,2,-7,-1,10,3,-3,2,-2,2,6,-2,-6,-2,4,-4,7,8,3,-10,-9,-2,3,-8,-5,-5,-4,3,-3,-2,-2,-1,2,-6,1,10,10,4,-8,-10,-5,-3,2,-8,-2,4,-7,-5,-4,-6,9,-5,-7,-4,-1,7,9,-4,-7,-8,5,1,6,-4,8],[-5,5,-8,1,1,-8,8,10,2,6,-4,-1,6,-2,-10,-10,9,-9,2,-1,-1,-1,8,-3,-7,-10,2,8,3,-10,-4,9,8,10,-7,-10,10,7,3,8,-9,-2,10,-2,-2,5,1,-9,6,-8,10,1,-1,10,8,-3,6,9,7,-10,-2,-7,3,-3,-5,9,-10,7,-9,-5,-5,-6,-6,-9,-6,4,-4,-4,-6,5,9,9,6,-9,3,4,2,10,-2,-3,-8,8,-9,-10,-9,-6,-8,-8,-1,9,-10,-5,-2,-4,-4,5,-7,5,-5,-3,-9,-5,-6,-3,-9,-2,-5,5,1,-2,-6,8,-9,-9,9,1,1,-7,8,-3,-2,5,-1,5,-10,7,-5,1,-8,-10,-2,-5,8,1,1,2,10,-1,8,1,4,-5,-2,4,-7,-5,7,4,-1,1,9,-5,3,-10,-3,-10,-8,7,9,10,-4,-5,-4,-6,3,6,3,3,-9,-8,3,-1,-2,2,10,9,6,6,-4,2,-4,-1,4,-2,6,-7,-7,-3,9,-10,7,4,3,3,4,7,6,4,2,4,5,1,2,-9,-9,-1],[-8,2,-4,-1,2,6,-5,-9,6,7,5,-3,1,-7,1,-9,-2,2,-7,4,-10,9,-1,-4,-2,-10,8,3,5,4,-7,-9,-5,4,-6,3,-1,1,3,-10,-6,-1,4,-8,3,7,4,-10,6,2,4,-8,-10,-8,-6,-5,1,-9,-9,3,6,1,-7,8,6,-7,-7,-5,6,9,4,-2,-1,9,7,-1,6,-2,4,-6,2,-3,8,8,-3,-6,3,1,9,4,-4,9,-9,-2,-3,-5,4,7,-6,-8,2,-8,-1,8,1,-6,-7,6,7,2,8,8,5,-8,8,2,1,4,-8,-2,4,-3,-6,-10,-7,-5,-10,-9,-6,-8,4,-6,-9,-4,5,-6,-7,-4,8,-6,-4,9,5,9,-6,8,6,-4,-6,-1,-8,4,6,8,9,10,-8,7,9,-5,-2,9,-6,-4,3,7,-4,9,-8,5,-3,-1,4,-4,-6,1,1,6,3,2,-5,9,10,9,-5,5,9,-10,-6,9,-3,-9,-10,-2,7,3,4,3,-8,-4,-7,2,9,-3,8,8,-2,-6,4,-9,5,-4,2,5,-10,-4],[9,6,-9,4,1,-9,-9,-7,-4,-5,-6,7,8,7,-2,6,-8,1,1,5,7,5,8,8,-8,-2,-4,10,3,-10,2,-10,10,8,-9,5,6,2,2,7,-3,-4,-7,8,6,9,-4,8,2,-5,-8,7,-10,7,8,-4,10,7,4,9,5,-8,7,-3,10,8,-10,-10,-3,-6,1,-2,-8,10,6,2,7,10,-3,-3,-3,-1,-9,5,9,2,1,-1,-3,-3,-10,10,-6,-3,5,6,-10,-3,9,10,-1,-8,-6,-3,7,10,4,7,2,1,-10,7,3,9,-10,-1,-1,3,-5,-6,4,-2,-8,8,-10,9,-5,2,-6,1,-1,-9,9,-10,10,-9,-4,5,-9,-3,-4,-1,-7,-9,5,1,10,8,3,4,-6,10,-3,3,9,-2,-6,-4,-7,10,-10,-8,2,-10,6,8,8,-3,6,2,1,8,9,2,2,-8,2,5,-3,-1,-10,2,-9,-6,2,10,-3,3,-2,-8,9,-9,1,7,8,3,-6,-3,-4,10,10,-1,10,-5,-1,9,8,-2,-3,-4,-4,-8,-4,5,-1,-5],[-9,-3,2,-3,2,4,-1,10,-3,4,1,-10,-2,-4,4,-3,-6,1,-6,-3,-8,8,-3,-5,3,6,1,1,-4,8,2,8,8,6,-6,2,-5,-5,-1,7,-10,-7,10,6,-1,-2,6,3,-1,-9,7,1,4,-4,-6,8,-5,-9,-5,1,-1,-10,-2,10,1,10,-1,-4,1,-9,-9,5,3,9,2,3,10,8,-8,7,8,-9,-10,-3,9,8,-6,-9,8,7,7,-3,7,1,10,5,5,8,-7,8,10,5,10,6,-4,-10,-7,10,-4,1,10,5,-2,-3,-1,-6,-7,-10,-6,7,-1,3,-1,4,-5,-1,-3,-10,-7,-3,-4,-1,3,-7,8,-9,4,9,-6,-9,9,7,6,6,-2,2,-9,6,6,1,9,5,3,-7,8,-3,7,9,-9,7,-4,-7,5,7,7,3,9,1,1,-2,-5,-6,-6,6,-9,-9,3,8,-1,7,-2,-6,-10,4,5,2,2,2,2,5,10,-4,2,-9,6,3,-8,-2,5,2,3,-2,2,5,2,7,4,5,5,8,-1,3,9,-10,9,-6],[5,-9,2,5,4,3,7,-3,-3,-6,-4,-4,2,9,7,6,-3,-1,9,-8,9,-10,-1,-9,-5,-7,-3,10,-6,-1,-4,4,-1,4,-2,2,6,-8,-6,9,5,8,10,5,1,-10,-2,4,-1,5,3,-7,-1,5,-3,9,-4,-7,-9,2,-10,-4,-9,6,-1,5,10,2,-6,-1,3,8,10,-4,8,10,-10,-10,7,9,9,-1,-6,4,-9,-1,-8,-2,2,9,1,10,6,-8,-10,-10,-3,-9,3,8,-10,-6,8,9,1,-2,9,-4,5,-7,-1,3,-7,4,8,2,1,-8,-6,-10,5,1,-5,-9,7,5,-5,3,-3,-4,10,-10,-5,-1,5,8,-3,-4,-4,-1,10,-10,-4,-9,-1,-9,10,-2,-10,-4,2,5,-2,6,-1,-8,2,-8,-2,-5,-1,-6,6,3,-10,-10,-10,-10,3,10,-2,5,-8,-10,9,5,-2,8,-6,-3,-10,1,-8,-6,-8,3,5,-3,10,-3,-1,-8,9,10,-10,4,-5,-2,7,-4,-4,-2,-6,4,-8,-4,5,-1,-1,-2,5,-1,-10,-3,-2,-1],[-3,-5,-9,4,6,-6,3,7,-2,5,4,8,-8,2,-10,-6,5,-4,2,2,8,-3,9,7,9,-9,-7,-9,-9,-6,-4,-4,6,5,-5,-6,-9,8,-8,-9,4,-2,-4,5,-1,-10,3,-6,-1,-5,-2,-3,-1,-8,3,-8,5,7,10,-1,-3,10,7,5,8,6,2,-10,-8,3,-6,-10,2,8,-9,7,-2,-8,-2,6,-2,2,2,10,-10,3,6,5,-1,2,-4,4,5,-4,4,8,10,3,-2,2,-7,-6,-8,-3,-5,-1,-3,6,4,6,8,7,6,2,2,-7,-10,-2,-7,-9,9,3,2,3,-9,-5,4,9,-3,-5,-4,6,9,-4,2,-9,1,6,-3,-9,-5,-1,10,9,8,8,8,10,1,-4,-5,-7,-8,2,-9,4,-9,5,3,-1,-7,7,-5,5,-8,1,5,-4,1,2,6,6,-1,3,4,-6,-4,-8,-9,5,3,3,-5,1,-2,8,9,3,4,5,-3,8,-6,-6,-1,-2,-8,4,-1,-1,-8,-1,10,8,-4,-1,5,-4,-8,-4,3,3,1,5,10,5],[5,-6,1,-9,8,2,1,-4,6,8,-4,-1,6,-8,-3,6,-8,3,8,-4,3,-2,10,5,-4,5,4,6,3,-10,-5,-4,-1,-2,-10,7,-10,10,-5,-8,-10,8,9,5,5,8,-2,-5,-7,3,-3,1,-9,5,-7,-2,4,-10,5,-4,-1,-2,-5,7,6,-9,10,4,4,3,2,10,-7,-10,-8,-3,-9,3,6,7,-9,10,-8,-7,4,6,5,-2,6,5,8,-2,-6,10,6,1,4,5,6,6,3,-5,-8,3,9,-8,7,-4,9,-5,1,-10,-9,-1,-6,4,9,-8,-6,-10,8,-2,10,-7,9,-3,8,-9,6,-2,5,2,7,10,10,10,10,2,-7,-8,-3,-9,2,-7,-6,-1,-9,6,2,1,7,-9,-1,-6,9,7,5,-2,3,-5,2,-1,-8,7,6,1,7,-10,-10,9,10,-3,1,4,-7,-5,5,-10,-5,-5,6,4,-8,4,-3,-1,-6,-10,10,-10,-2,-5,-1,2,-3,8,-4,3,-7,2,-9,-4,7,-3,-5,3,-8,-4,5,-8,4,-8,-8,-2,9,6],[-7,6,-2,1,3,-7,-2,1,-9,-8,5,-1,8,-8,9,8,4,-2,-2,-4,-6,-6,-3,6,8,-7,9,-5,-1,-7,-9,-8,6,7,-10,-2,5,-7,-7,-2,-6,-7,7,5,7,10,-6,6,6,-1,-8,5,3,2,4,4,-3,6,-4,-7,2,8,-4,9,10,8,-4,-1,-4,6,7,7,-2,-9,5,-9,3,-4,-2,9,-6,-1,-2,7,7,4,-5,3,6,-8,-8,-10,6,10,-9,-1,-7,-5,-7,3,-6,-8,-9,-10,3,-6,5,-3,-9,9,1,-3,4,-5,10,3,-6,9,-1,10,7,6,1,-10,-4,10,-1,-4,-3,-4,-1,-3,7,4,-10,-4,10,8,-1,4,9,1,-7,5,-7,4,-7,7,-8,-3,-5,5,9,1,-4,-5,8,-5,2,6,-10,-7,7,2,-5,4,-2,-9,2,10,2,-1,1,7,5,-5,4,-9,-6,-6,5,-4,9,-9,1,9,7,6,-5,5,4,4,-10,9,-5,10,5,9,5,-6,-9,10,6,-8,-8,-2,1,-10,-8,-8,4,-3,1,-2,9,-3],[-5,-8,10,4,7,10,-2,10,9,-3,7,1,-5,4,-3,4,-1,-10,8,-1,-2,4,1,-3,3,3,-9,8,9,2,9,1,10,-5,7,-3,4,4,3,-8,-3,-4,5,-10,4,-6,8,4,-1,4,2,-9,-9,4,10,6,-2,8,2,4,10,8,-9,3,1,8,-9,4,9,7,9,-5,-6,10,2,4,4,-7,-6,3,-10,-3,-7,6,-4,-7,8,3,6,-10,7,-10,7,4,-10,1,7,10,10,9,-8,-6,-8,-8,4,3,-3,-4,10,4,-6,-1,-8,4,6,-1,-10,3,-7,2,-1,5,-8,6,9,-10,-4,8,2,9,5,-4,-8,3,-8,-9,10,4,-4,-5,-10,-10,6,6,9,-5,5,1,4,9,9,-2,-1,-6,-7,-10,8,1,5,1,3,10,3,1,3,1,7,2,10,-5,-1,-5,-4,-2,-4,-4,-6,4,4,-1,5,-3,-5,-10,-3,5,-9,-4,9,-1,6,1,-10,5,2,4,-6,-10,10,-10,-5,10,5,7,7,-6,-5,-8,2,8,-7,-1,-9,-6,3,3],[-10,3,6,-9,8,-9,2,8,9,10,-8,9,-2,-8,2,2,-6,-9,-5,-7,-6,5,-4,-4,9,-8,-4,6,-3,-10,8,9,7,8,6,4,-2,10,4,-8,7,-1,3,7,-4,3,1,7,9,1,-1,-7,-5,-8,10,-1,-1,10,-2,2,-7,9,8,-7,1,2,2,4,8,-6,1,-7,-10,8,7,-9,6,2,3,-9,-5,6,-2,-7,-6,1,10,10,9,1,10,8,-7,-8,-8,-5,-9,2,-5,6,-2,1,-6,-10,-10,9,-1,4,9,-8,-10,-2,8,-2,3,-4,-4,-4,5,5,7,3,-3,5,10,9,-8,9,-2,-9,-9,-9,8,-5,-7,8,4,-1,-10,-9,2,10,-8,8,-10,-5,1,-3,-7,-2,9,-8,5,4,-6,6,10,9,-5,-7,5,-3,8,-5,-6,-9,9,2,7,-9,-8,10,-1,7,8,-10,-8,9,-10,-2,1,3,-1,4,-10,8,8,-7,8,6,8,9,8,3,-2,6,10,-1,-6,-6,8,6,3,8,5,-9,9,-8,-6,4,-10,1,-2,1,-7,-4],[-1,4,4,-7,-5,2,4,2,-3,-10,-9,-2,-3,-6,-10,-9,1,-6,7,-3,-2,8,-5,8,7,2,10,6,9,-6,-4,-9,-8,1,-2,8,9,10,8,-5,-7,-2,1,10,2,8,-9,-3,5,4,10,1,-10,5,-10,-3,-7,4,3,-9,-10,-10,-5,-7,9,-10,-5,-8,2,3,4,-1,-10,-1,10,7,7,8,4,-4,9,2,3,-9,7,-8,-7,-4,-3,2,-2,-3,8,-1,-9,5,-7,3,9,8,5,9,-5,1,-5,-3,-1,8,-10,-2,-3,10,-4,-1,-5,10,-5,4,-1,9,-7,5,-1,-7,-1,1,-6,4,-1,4,4,-8,3,10,-6,-2,-1,10,1,2,-8,7,-1,-3,-8,10,1,2,9,-9,-8,9,9,1,9,-1,-6,1,9,-10,1,10,10,-7,3,6,-7,3,2,-6,-9,8,-5,-3,-2,-1,2,6,-3,-1,-9,8,-1,3,-6,6,6,-9,2,-5,-4,9,8,-10,-8,-9,-7,4,7,1,6,9,1,3,1,-8,-6,2,2,-7,2,-9,3,7,3,-5],[7,-1,5,2,3,10,-8,-3,4,-3,6,-7,7,2,2,-9,3,-7,-5,4,-10,-7,-9,-9,10,1,-5,-6,-2,10,-6,-5,10,-9,3,-3,10,-1,10,-3,-3,-8,-5,-1,-5,-5,10,3,-3,5,6,9,9,4,-4,-10,3,5,6,-7,7,-3,-1,8,-7,-2,-4,6,2,3,-6,3,2,-9,6,-9,-7,3,-7,6,6,8,8,3,5,-6,-6,-2,8,7,9,-6,-8,-6,10,2,9,-5,-5,9,-2,-3,-3,-9,8,3,-3,4,10,6,-4,-5,8,2,-10,-3,5,5,3,-6,-1,8,8,5,6,7,2,4,5,3,-8,-8,-6,-8,-8,-2,3,-4,6,10,-3,-1,-10,4,3,-9,-8,2,1,-5,-4,9,-8,8,-10,-3,5,7,1,9,3,-4,8,-6,-6,9,7,7,8,-7,-6,-3,-6,-4,-6,-10,-4,1,-10,10,-8,-8,-4,-10,2,3,2,9,-8,5,-8,2,-7,4,10,3,-1,-4,-6,1,4,8,-10,3,9,-2,1,1,-7,-5,-8,-6,1,-6,-4,7],[-1,-5,-1,10,4,-1,4,-5,6,7,-8,3,-2,-8,-7,6,9,10,-10,2,-10,1,4,6,-5,1,7,5,-4,8,8,-9,5,-7,-10,9,1,-8,7,2,-9,9,9,-7,-7,-4,9,3,5,-9,10,-4,9,5,-8,-9,-4,-4,2,-5,8,-7,-5,1,10,-4,7,3,-2,3,9,-6,2,-7,-3,7,-4,-8,-3,-10,8,-7,-3,-2,-1,4,9,-3,2,-7,-4,8,-7,8,5,6,1,-10,-4,-9,9,4,-5,-9,9,-4,10,-1,-8,6,-7,7,-6,10,9,-6,5,6,-1,9,-3,-4,-6,-10,4,-6,-10,8,-1,-7,-10,-9,-5,6,-4,-5,-9,1,-4,8,9,-10,8,-7,8,1,9,2,-9,-9,3,-1,2,8,5,5,-1,-2,-5,-9,-5,1,-10,-9,3,-3,1,-9,-8,-1,2,-6,5,3,9,4,-2,-1,10,-3,-7,9,10,2,-6,10,1,2,-6,-5,-7,-10,-6,3,-10,-10,5,-6,7,5,-1,3,3,-9,10,-3,-4,6,-3,-5,7,9,-5,9,2,-7]], dtype = "int8")#candidate|2625|(48, 216)|const|int8
var_2626 = relay.var("var_2626", dtype = "int16", shape = (936,))#candidate|2626|(936,)|var|int16
var_2627 = relay.var("var_2627", dtype = "float32", shape = (12, 36))#candidate|2627|(12, 36)|var|float32
call_2623 = relay.TupleGetItem(func_1972_call(relay.reshape(var_2624.astype('float32'), [4, 9, 5]), relay.reshape(const_2625.astype('int8'), [10368,]), relay.reshape(var_2626.astype('int16'), [936,]), relay.reshape(var_2627.astype('float32'), [4, 9, 12]), ), 14)
call_2628 = relay.TupleGetItem(func_1978_call(relay.reshape(var_2624.astype('float32'), [4, 9, 5]), relay.reshape(const_2625.astype('int8'), [10368,]), relay.reshape(var_2626.astype('int16'), [936,]), relay.reshape(var_2627.astype('float32'), [4, 9, 12]), ), 14)
output = relay.Tuple([uop_2584,call_2586,const_2587,const_2588,uop_2603,uop_2619,call_2623,var_2624,const_2625,var_2626,var_2627,])
output2 = relay.Tuple([uop_2584,call_2589,const_2587,const_2588,uop_2603,uop_2619,call_2628,var_2624,const_2625,var_2626,var_2627,])
func_2634 = relay.Function([var_2552,var_2553,var_2624,var_2626,var_2627,], output)
mod['func_2634'] = func_2634
mod = relay.transform.InferType()(mod)
mutated_mod['func_2634'] = func_2634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2634_call = mutated_mod.get_global_var('func_2634')
var_2636 = relay.var("var_2636", dtype = "float64", shape = (5, 10, 10))#candidate|2636|(5, 10, 10)|var|float64
var_2637 = relay.var("var_2637", dtype = "float64", shape = (5, 10, 10))#candidate|2637|(5, 10, 10)|var|float64
var_2638 = relay.var("var_2638", dtype = "float32", shape = (180,))#candidate|2638|(180,)|var|float32
var_2639 = relay.var("var_2639", dtype = "int16", shape = (936,))#candidate|2639|(936,)|var|int16
var_2640 = relay.var("var_2640", dtype = "float32", shape = (12, 36))#candidate|2640|(12, 36)|var|float32
call_2635 = func_2634_call(var_2636,var_2637,var_2638,var_2639,var_2640,)
output = call_2635
func_2641 = relay.Function([var_2636,var_2637,var_2638,var_2639,var_2640,], output)
mutated_mod['func_2641'] = func_2641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1311_call = mod.get_global_var('func_1311')
func_1313_call = mutated_mod.get_global_var('func_1313')
call_2696 = relay.TupleGetItem(func_1311_call(), 3)
call_2697 = relay.TupleGetItem(func_1313_call(), 3)
output = relay.Tuple([call_2696,])
output2 = relay.Tuple([call_2697,])
func_2698 = relay.Function([], output)
mod['func_2698'] = func_2698
mod = relay.transform.InferType()(mod)
output = func_2698()
func_2699 = relay.Function([], output)
mutated_mod['func_2699'] = func_2699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2299_call = mod.get_global_var('func_2299')
func_2301_call = mutated_mod.get_global_var('func_2301')
call_2739 = relay.TupleGetItem(func_2299_call(), 2)
call_2740 = relay.TupleGetItem(func_2301_call(), 2)
uop_2760 = relay.atan(call_2739.astype('float64')) # shape=(4, 9, 1)
uop_2762 = relay.atan(call_2740.astype('float64')) # shape=(4, 9, 1)
output = uop_2760
output2 = uop_2762
func_2773 = relay.Function([], output)
mod['func_2773'] = func_2773
mod = relay.transform.InferType()(mod)
mutated_mod['func_2773'] = func_2773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2773_call = mutated_mod.get_global_var('func_2773')
call_2774 = func_2773_call()
output = call_2774
func_2775 = relay.Function([], output)
mutated_mod['func_2775'] = func_2775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1179_call = mod.get_global_var('func_1179')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_2844 = func_1179_call()
call_2845 = func_1179_call()
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_2860 = func_194_call()
call_2861 = func_194_call()
func_773_call = mod.get_global_var('func_773')
func_776_call = mutated_mod.get_global_var('func_776')
const_2868 = relay.const([-8.489706,0.831518,-7.069951,3.552397,8.941664,-0.285871,5.157159,-4.379366,-7.734247,-3.080341,-1.098237,9.884305,-4.601141,-6.986468,-9.949931,5.800675,2.954599,-9.727620,-7.852663,9.309929,0.363560,-6.438452,-3.373654,-6.823879,-9.139125,-2.052953,9.850320,-6.155417,9.680691,3.277277,8.500670,-5.442394,-0.060470,-9.303969,2.959750,-7.299523,0.613889,5.600963,-2.127808,-7.422534,-0.946406,1.513636,-5.749135,5.928860,-4.858868,6.713766,-0.843893,-9.909471,6.020232,6.262128,-3.080925,1.546462,-2.352879,7.992539,6.596657,7.207301,9.124085,2.100415,0.655614,9.503152,-2.012460,4.999567,2.922913,1.729167,2.659292,8.714296,-4.864401,1.069926,0.160414,2.666297,0.993612,-3.652011], dtype = "float32")#candidate|2868|(72,)|const|float32
call_2867 = relay.TupleGetItem(func_773_call(relay.reshape(const_2868.astype('float32'), [12, 2, 3]), relay.reshape(const_2868.astype('float32'), [12, 2, 3]), ), 1)
call_2869 = relay.TupleGetItem(func_776_call(relay.reshape(const_2868.astype('float32'), [12, 2, 3]), relay.reshape(const_2868.astype('float32'), [12, 2, 3]), ), 1)
func_514_call = mod.get_global_var('func_514')
func_515_call = mutated_mod.get_global_var('func_515')
call_2872 = func_514_call()
call_2873 = func_514_call()
uop_2882 = relay.cosh(call_2860.astype('float64')) # shape=(4, 9, 1)
uop_2884 = relay.cosh(call_2861.astype('float64')) # shape=(4, 9, 1)
const_2885 = relay.const([[[1.564046,-9.224608,-0.604491,-9.668556,1.111454,5.106800,-0.668898,1.871147,4.519546,-0.118826,0.510374,3.036916],[-7.900320,-3.694100,4.075766,-1.090579,-5.651232,6.459914,8.850248,-7.195634,-2.827128,-8.192095,-4.674428,-3.706300],[2.469154,-0.544576,-6.042427,8.683487,6.791649,5.107346,-3.618774,-5.021453,-4.297342,4.476543,6.504451,-9.898127],[1.570724,-2.441228,1.354794,2.677168,0.111421,6.919404,-9.043087,-5.114672,-4.032782,-8.966772,-7.488676,-6.937046],[-7.231115,-2.478632,8.853147,8.277902,4.220945,-3.260676,7.325929,3.274889,6.677877,-2.835802,-6.812401,4.213663],[-1.192208,0.626413,-1.987209,5.670055,9.204915,-8.988028,-7.808542,-1.780143,-6.696936,-2.135202,-2.215726,-8.124053],[-1.915860,2.282608,-7.333110,-9.791983,-8.552970,8.855017,5.819849,-0.465567,-0.156821,5.426861,-9.806793,-3.752461],[-9.120630,-7.768499,-0.906738,-9.135670,7.212610,4.688498,-3.743575,-5.165657,7.222610,-0.025801,-6.806607,-6.498479],[0.953657,-2.042953,7.819590,-3.676690,9.071292,-4.425987,-6.798466,3.962290,1.607079,0.210878,-5.569984,-6.651941]],[[0.932297,-7.558911,2.738049,-1.516148,-6.545724,1.055863,8.908693,7.805723,-2.008436,-2.547646,-2.715171,3.689538],[9.502810,8.842467,-8.636586,7.903559,-0.847780,-2.134878,-7.882258,4.167417,4.143091,-9.881071,-6.261078,9.079494],[-9.423589,7.206119,4.832132,-5.501581,5.428176,-2.982688,4.015981,3.318712,1.485776,-7.901297,-2.429897,-3.443504],[-7.850836,-0.574845,-1.127285,8.984404,-1.229617,4.949580,8.359401,-3.387596,-7.053814,7.559578,-2.667558,2.381855],[-6.272511,-0.273365,4.939714,-2.913091,3.880324,0.931987,-9.491822,-7.639066,3.159195,1.499668,3.077431,-7.328412],[-7.513250,-4.467527,-3.629201,1.461193,6.391395,-4.233572,-1.758986,-9.591094,1.185741,-9.629190,-7.198133,-5.955039],[-1.383215,1.388128,6.805275,8.879479,3.029675,1.639217,-3.763255,-7.583821,-0.517067,-9.506929,9.748994,-7.634100],[-8.001601,-6.272073,-6.758926,4.518563,-1.604585,-4.676886,-9.997783,-9.760595,2.959303,7.914773,-9.633424,6.939261],[-8.801069,4.352331,-0.740977,6.654844,-1.281081,-8.982578,-7.664591,-5.146094,-7.420749,2.730248,-4.059778,-6.766454]],[[2.734703,6.618112,5.182430,-7.391551,6.988028,8.092367,7.344042,-3.124081,-6.216185,-8.816626,-4.484354,-0.035585],[-6.819191,6.096509,3.144716,-0.903591,-1.268283,-7.186311,9.039440,4.783735,-1.345170,-7.548041,1.445368,-1.919804],[4.996583,3.730576,1.388082,-5.742601,3.771760,-8.198549,5.280286,3.446862,4.020766,6.601881,-2.069810,6.647112],[9.550590,-2.609799,-2.972062,7.497938,-0.610487,-3.490260,-2.182102,8.960087,-5.692551,-6.124301,-8.846574,7.194364],[9.443774,-8.120891,-4.019865,-0.355176,-2.141380,-5.244021,5.338410,-2.245157,-4.453582,6.678409,-8.203003,-7.770174],[5.789777,-6.486089,-0.291826,5.695799,1.785150,2.893081,3.310617,7.717460,1.025622,-5.579262,3.886116,-7.814313],[3.089884,-5.357445,-8.674952,6.880481,8.560012,0.112181,6.803975,8.116148,6.048206,-6.168529,2.363509,-0.278286],[-4.165446,8.487222,0.125926,3.062932,-8.558991,-1.441759,7.844989,-3.973651,-7.545837,-2.631483,-8.736020,-0.774238],[5.984068,-2.360026,-6.368922,6.023390,7.275746,9.442901,-8.455337,-0.451842,-8.638788,0.486556,-8.729012,7.867004]],[[6.331917,-8.080886,5.705078,6.082386,-0.783029,0.431706,-4.212059,3.378812,-7.505621,5.009233,2.816543,5.073686],[-6.992208,6.441177,-3.950160,8.376271,5.626916,3.078024,-7.468054,7.227336,-4.438135,-2.605292,8.493596,-6.187200],[-6.480970,-3.574821,3.918686,6.311690,-4.036427,-1.416595,3.407889,-3.760034,-6.549473,-5.917234,1.796114,6.965841],[-5.118641,-8.310580,9.514239,0.662650,-8.954567,5.352055,5.708301,-6.236498,-6.156382,-9.649331,-0.179518,-3.891613],[-5.076360,-5.265088,-0.782162,4.162943,4.917345,-3.945900,7.798302,-8.992587,2.261839,9.673021,-1.475789,-5.857001],[0.225774,0.203933,6.071639,-0.735408,-5.557349,2.603791,-9.083007,3.702715,4.487364,-2.991699,-1.657794,-8.750693],[-7.484745,-9.054659,4.009377,3.232654,-0.171761,2.651493,-0.751411,7.870140,-2.945981,7.200829,-9.122807,-4.675255],[-3.386722,-9.050502,4.624723,-5.416851,-1.225439,-7.508368,6.416016,-1.012858,-6.548346,-6.744806,6.454079,6.331616],[-3.859680,-7.522952,-6.218129,-8.051821,9.573860,9.276690,-3.262119,4.410381,-9.263436,-9.955300,7.376772,4.695769]]], dtype = "float64")#candidate|2885|(4, 9, 12)|const|float64
bop_2886 = relay.bitwise_or(uop_2882.astype('int8'), const_2885.astype('int8')) # shape=(4, 9, 12)
bop_2889 = relay.bitwise_or(uop_2884.astype('int8'), const_2885.astype('int8')) # shape=(4, 9, 12)
uop_2920 = relay.rsqrt(uop_2882.astype('float32')) # shape=(4, 9, 1)
uop_2922 = relay.rsqrt(uop_2884.astype('float32')) # shape=(4, 9, 1)
func_1413_call = mod.get_global_var('func_1413')
func_1415_call = mutated_mod.get_global_var('func_1415')
var_2926 = relay.var("var_2926", dtype = "int16", shape = (936,))#candidate|2926|(936,)|var|int16
call_2925 = relay.TupleGetItem(func_1413_call(relay.reshape(var_2926.astype('int16'), [8, 9, 13])), 1)
call_2927 = relay.TupleGetItem(func_1415_call(relay.reshape(var_2926.astype('int16'), [8, 9, 13])), 1)
func_1100_call = mod.get_global_var('func_1100')
func_1103_call = mutated_mod.get_global_var('func_1103')
call_2928 = relay.TupleGetItem(func_1100_call(relay.reshape(call_2925.astype('float32'), [8, 11, 9])), 0)
call_2929 = relay.TupleGetItem(func_1103_call(relay.reshape(call_2925.astype('float32'), [8, 11, 9])), 0)
bop_2948 = relay.not_equal(uop_2920.astype('bool'), var_2926.astype('bool')) # shape=(4, 9, 936)
bop_2951 = relay.not_equal(uop_2922.astype('bool'), var_2926.astype('bool')) # shape=(4, 9, 936)
func_1179_call = mod.get_global_var('func_1179')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_2954 = func_1179_call()
call_2955 = func_1179_call()
output = relay.Tuple([call_2844,call_2867,const_2868,call_2872,bop_2886,call_2925,call_2928,bop_2948,call_2954,])
output2 = relay.Tuple([call_2845,call_2869,const_2868,call_2873,bop_2889,call_2927,call_2929,bop_2951,call_2955,])
func_2971 = relay.Function([var_2926,], output)
mod['func_2971'] = func_2971
mod = relay.transform.InferType()(mod)
var_2972 = relay.var("var_2972", dtype = "int16", shape = (936,))#candidate|2972|(936,)|var|int16
output = func_2971(var_2972)
func_2973 = relay.Function([var_2972], output)
mutated_mod['func_2973'] = func_2973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_3013 = relay.TupleGetItem(func_653_call(), 0)
call_3014 = relay.TupleGetItem(func_654_call(), 0)
uop_3017 = relay.atanh(call_3013.astype('float32')) # shape=(7, 220)
uop_3019 = relay.atanh(call_3014.astype('float32')) # shape=(7, 220)
var_3021 = relay.var("var_3021", dtype = "float32", shape = (7, 220))#candidate|3021|(7, 220)|var|float32
bop_3022 = relay.divide(uop_3017.astype('float32'), relay.reshape(var_3021.astype('float32'), relay.shape_of(uop_3017))) # shape=(7, 220)
bop_3025 = relay.divide(uop_3019.astype('float32'), relay.reshape(var_3021.astype('float32'), relay.shape_of(uop_3019))) # shape=(7, 220)
bop_3029 = relay.power(var_3021.astype('float32'), relay.reshape(bop_3022.astype('float32'), relay.shape_of(var_3021))) # shape=(7, 220)
bop_3032 = relay.power(var_3021.astype('float32'), relay.reshape(bop_3025.astype('float32'), relay.shape_of(var_3021))) # shape=(7, 220)
output = bop_3029
output2 = bop_3032
func_3043 = relay.Function([var_3021,], output)
mod['func_3043'] = func_3043
mod = relay.transform.InferType()(mod)
mutated_mod['func_3043'] = func_3043
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3044 = relay.var("var_3044", dtype = "float32", shape = (7, 220))#candidate|3044|(7, 220)|var|float32
func_3043_call = mutated_mod.get_global_var('func_3043')
call_3045 = func_3043_call(var_3044)
output = call_3045
func_3046 = relay.Function([var_3044], output)
mutated_mod['func_3046'] = func_3046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2699_call = mutated_mod.get_global_var('func_2699')
call_3079 = relay.TupleGetItem(func_2698_call(), 0)
call_3080 = relay.TupleGetItem(func_2699_call(), 0)
func_1972_call = mod.get_global_var('func_1972')
func_1978_call = mutated_mod.get_global_var('func_1978')
const_3082 = relay.const([9.923212,8.434273,5.891091,-4.173081,6.560949,-2.110619,-9.306778,6.456247,-3.916556,-0.059468,1.154248,-5.798672,4.955351,-3.203442,-8.007707,-7.170460,-4.915977,-6.052087,5.444397,-4.046560,-4.200571,-1.479527,-1.385565,-3.861811,4.327723,8.001320,3.771051,-7.580284,-2.550271,4.226703,-9.941274,-4.593291,-6.606434,-6.188918,-4.540916,-3.273120,6.998954,6.568893,2.794218,-7.504107,-4.992890,5.888553,3.009904,6.327977,-1.205403,0.138785,-4.934084,0.027466,-6.294543,-3.349724,-6.286411,0.360442,-7.783934,-1.913060,-0.567715,-5.172687,-6.820480,9.351590,5.112850,1.723246,1.480025,-3.782910,-6.060175,-3.968672,1.653163,3.135749,-8.579662,5.523090,-9.145303,-7.470038,9.705293,5.845935,-8.164809,3.625340,6.229280,7.704774,3.914508,-4.981650,-1.436801,-8.555307,-4.924020,0.514844,-6.540849,2.984496,-8.467894,-8.570652,-5.939190,9.405585,-1.351451,-6.102814,7.951058,-5.587138,0.801727,7.950614,-1.450900,6.427725,2.491373,3.165976,7.605502,-3.623013,-8.489175,8.414057,4.425907,3.527338,-4.389265,5.732755,1.809532,-6.615813,7.175842,-0.627164,-3.336198,-5.745360,8.054978,0.630220,-6.800547,-5.133700,-9.487219,6.891644,3.905963,9.375399,-9.135082,8.652065,5.303859,-2.945385,4.699138,-5.213261,-4.436099,-1.457962,-5.230559,-8.037033,1.465537,5.166743,8.015337,9.212210,1.783395,-9.325094,-4.069257,9.912522,9.257923,-5.493444,1.894879,-6.193105,5.350942,3.576706,3.121468,-6.640290,-2.063121,-2.360913,-2.260242,-6.809589,7.711630,3.345248,0.835705,2.956838,-4.928905,4.874017,-7.912153,8.052536,-7.084732,5.532433,-5.070834,5.914925,7.968226,-7.419107,8.810799,5.981174,0.060715,-1.323668,8.818404,-7.618570,9.477425,4.818863,4.599160,4.651855,1.163175,7.853544,-0.850162,7.249197,2.548298,7.077390], dtype = "float32")#candidate|3082|(180,)|const|float32
var_3083 = relay.var("var_3083", dtype = "int8", shape = (10368,))#candidate|3083|(10368,)|var|int8
const_3084 = relay.const([[8,-4],[-2,-8],[10,-9],[-4,4],[3,9],[-7,5],[6,-3],[-6,2],[2,-1],[-2,5],[2,10],[9,1],[-1,-3],[9,-2],[-4,3],[-6,3],[2,2],[2,-7],[-3,4],[2,5],[-6,-2],[6,1],[1,-1],[-6,6],[-8,-1],[6,-9],[-6,1],[6,9],[-4,-8],[-7,2],[2,6],[10,5],[8,10],[-5,-5],[2,9],[1,2],[1,8],[1,-7],[-5,-1],[4,-5],[-4,-8],[-6,2],[-8,5],[-8,-5],[-9,8],[-4,2],[-7,6],[-9,-4],[8,5],[-5,-3],[7,4],[-7,4],[-3,7],[-7,-1],[-2,-6],[10,5],[3,3],[7,3],[-5,7],[8,-9],[4,-10],[-5,-7],[-8,9],[4,7],[5,5],[9,6],[-7,-6],[-6,9],[9,3],[10,2],[-3,-9],[6,-2],[9,3],[-9,10],[3,4],[8,-9],[3,-2],[2,-3],[6,9],[8,-3],[3,5],[-6,-8],[10,8],[5,7],[-1,-1],[5,-7],[-5,-3],[10,-2],[-5,-2],[1,-1],[4,-10],[-9,5],[10,-3],[9,5],[6,9],[-7,6],[-7,4],[2,10],[7,5],[1,-7],[5,3],[10,7],[8,-2],[6,-7],[-8,-4],[6,-4],[-6,-10],[8,-5],[7,-6],[9,-3],[-9,2],[-2,-2],[-1,9],[-2,2],[-4,4],[-10,-7],[-10,2],[-6,6],[9,-3],[-10,9],[3,9],[-5,-3],[5,-2],[-10,-10],[2,2],[8,-3],[8,7],[-5,9],[8,-3],[-1,3],[8,1],[-4,10],[6,4],[-10,10],[-5,7],[-5,7],[-6,-6],[7,-5],[5,-4],[-8,5],[-6,7],[-5,7],[-5,-7],[-3,-4],[5,10],[-7,8],[2,1],[8,-3],[2,-2],[8,-7],[6,-3],[-10,-9],[-5,8],[5,-6],[-8,6],[-10,10],[-10,10],[-6,1],[3,-10],[-1,8],[10,-9],[-2,2],[1,-7],[7,-4],[-4,5],[3,1],[-7,9],[-1,-3],[-4,8],[9,-7],[-9,1],[4,3],[4,-7],[3,3],[10,-10],[-10,4],[7,-10],[-5,7],[3,-10],[-5,-8],[-10,-6],[-4,2],[2,5],[-7,5],[-4,-10],[-4,-10],[5,8],[2,9],[-1,-2],[-3,-7],[8,-6],[-2,9],[-10,2],[6,-4],[4,10],[-6,-6],[5,1],[6,-4],[1,-7],[3,-8],[5,-8],[4,1],[-4,3],[-2,-8],[-1,-7],[-9,1],[-1,3],[-6,-8],[3,-1],[7,-6],[-5,-2],[2,-5],[9,9],[-1,7],[1,-7],[-3,8],[-2,-2],[9,2],[8,10],[-2,-10],[7,8],[-2,-1],[7,9],[-4,3],[-4,-6],[4,8],[2,10],[4,-6],[3,-8],[-10,-7],[-8,6],[-1,-5],[5,-9],[-9,-1],[-6,-6],[2,1],[7,10],[10,-6],[-4,-8],[5,-2],[-7,1],[10,9],[-4,-8],[7,2],[9,-3],[9,-7],[4,-8],[1,9],[-4,3],[2,-2],[9,3],[-7,1],[-8,7],[4,10],[9,6],[1,7],[-6,9],[-4,-6],[-9,8],[5,6],[-4,1],[-6,7],[-1,5],[-8,7],[-5,-4],[7,2],[9,6],[1,-9],[2,6],[-3,5],[-6,7],[-3,10],[1,8],[5,6],[2,-10],[-1,-2],[9,2],[3,-5],[8,-4],[6,-2],[9,-7],[-10,10],[4,-8],[7,1],[-8,-7],[2,9],[-3,2],[9,8],[-4,2],[-9,-7],[-2,-1],[5,-6],[-7,-3],[6,1],[-8,-1],[-9,-5],[-6,-6],[-1,2],[-7,2],[-5,4],[-3,2],[-2,-9],[6,-5],[10,7],[-9,3],[-5,3],[5,4],[6,-3],[9,-6],[-8,1],[-4,-8],[-8,-10],[-7,7],[7,-4],[5,-4],[9,10],[3,-9],[1,-5],[-6,-9],[8,-1],[2,7],[-10,-4],[10,-8],[7,7],[3,3],[3,9],[10,4],[-7,1],[5,-1],[-10,1],[-4,8],[-4,1],[10,1],[1,3],[-8,-9],[3,6],[-9,-4],[3,8],[-2,-9],[3,6],[-6,-5],[7,-10],[6,-9],[9,-7],[-6,7],[6,-9],[4,-7],[-1,-10],[-7,6],[4,8],[5,-7],[7,-5],[6,-2],[-9,-1],[10,10],[8,-10],[5,-1],[-4,-9],[8,-5],[3,-8],[4,-9],[3,-8],[7,-6],[-7,2],[-2,3],[3,5],[9,6],[10,10],[4,-8],[9,-1],[1,-1],[-2,4],[-7,-2],[-8,-4],[6,10],[-6,1],[10,-8],[-3,-5],[-4,5],[-9,-4],[6,9],[-2,5],[-4,4],[-7,-1],[-4,8],[-6,4],[-9,-8],[7,-7],[7,-1],[10,4],[10,4],[-5,-4],[4,8],[5,1],[-10,2],[-2,-4],[-6,5],[8,-10],[9,8],[8,5],[-4,-1],[-5,-2],[-3,4],[-5,2],[3,5],[-9,10],[8,-6],[-1,-10],[5,5],[4,-7],[-4,-2],[-1,-8],[4,-6],[10,-4],[5,7],[-2,1],[8,9],[5,-1],[-1,8],[9,-8],[1,9],[1,10],[-3,2],[-3,5],[8,5],[4,-2],[9,6],[-8,-5],[8,2],[7,-3],[-10,8],[-7,7],[8,3],[-8,-6],[-7,-6],[-7,-5],[3,4],[3,10],[4,9],[2,-9],[7,-2],[-8,-1],[1,9],[-8,-4],[-4,-3],[-8,10],[-3,-3],[6,5],[5,8],[8,-8],[9,-10],[2,2],[-4,4],[-9,4],[-5,7],[3,7],[-3,-3],[8,-1],[-9,-6],[5,-8],[2,-1],[-8,5],[3,9],[5,-4],[-2,-9],[-8,-7],[-1,9],[-2,3]], dtype = "int16")#candidate|3084|(468, 2)|const|int16
const_3085 = relay.const([2.778628,-9.873859,-1.195861,8.581848,-7.456757,-2.222518,2.049858,-8.743945,6.177254,7.237451,-3.690239,-1.505056,-2.923362,-8.202230,1.301699,5.542656,0.922348,3.362986,-5.852316,6.814264,-3.833459,-5.407019,5.905740,8.221975,0.003607,-6.752259,-3.118385,0.335683,0.337584,-0.034464,3.757073,0.932016,-0.899853,-1.674976,6.544858,6.624957,8.834886,2.502682,8.125701,7.215065,7.855472,-5.828607,-2.732892,3.596556,5.875039,1.289497,1.450035,8.036819,5.426616,-1.560459,-3.512198,-3.051914,6.192663,-7.091925,-5.572594,1.503910,1.026970,-8.929417,5.819018,7.576212,2.181298,5.482573,8.265163,-1.682091,-3.488630,7.642871,7.983611,3.355562,3.164513,8.069456,2.287444,-4.612945,-2.456170,5.827844,-9.336845,7.531063,6.957526,-7.962308,2.570654,1.122198,8.674941,-3.264145,-9.063085,2.655454,7.064095,-5.212298,-9.738566,-2.252720,2.616024,-4.098676,-1.410139,2.746517,7.740227,3.052405,8.724261,-2.573975,3.522890,3.502036,-4.475168,-6.276051,5.628740,9.964375,5.676984,-1.616735,9.138361,-1.789288,-6.290308,8.379110,1.378095,8.172511,5.239991,3.395405,-0.322832,-5.760002,5.567264,2.635744,3.185399,-2.827418,-2.713691,9.120364,-6.611897,1.565923,-6.163761,-8.620733,7.412383,-1.600526,0.950409,-0.910114,-0.645933,4.817832,3.258590,-3.930442,8.827752,5.705879,3.869295,6.710652,-2.835103,7.490575,5.344400,-3.802669,6.831616,2.326165,-5.122917,-0.444825,-1.150854,-3.887660,-8.126880,5.596995,-0.610053,5.344265,2.413124,8.082106,-3.910073,-3.101304,-3.871675,-3.269163,1.234509,-0.397210,2.060018,-4.957788,-0.171487,5.097062,7.351145,-2.075898,2.409500,-2.436081,-6.283530,-3.975936,-4.523980,-7.997987,8.969182,-1.144313,-7.903242,-6.612821,7.290799,-8.057434,-7.487589,0.391502,-2.869050,1.391661,9.621874,-8.301695,7.840370,-8.649383,-4.343349,-5.309864,-8.332030,-8.683815,0.899526,-4.901372,-4.511883,5.768468,9.999664,-0.661475,-8.727504,5.919614,4.183484,-4.110015,3.768356,-5.478535,8.381819,7.139065,9.956581,3.061490,4.916045,-1.721819,-4.822948,-1.204403,-0.080236,0.084173,-0.243300,-8.155414,-0.249160,-3.482020,-5.727928,7.609965,8.663963,0.880514,2.493751,3.052016,-3.016945,-3.414566,5.977584,-6.984849,6.638451,7.662663,8.488417,-7.142885,-3.060156,5.122222,2.019540,-1.101880,1.638828,-5.798540,-5.648582,3.684058,1.885792,0.736228,-9.383201,-2.949649,1.026021,0.411200,3.564350,8.099509,-6.985189,-7.008491,5.703503,-0.479345,-8.575317,2.480456,0.177637,-6.156774,-8.594113,0.383009,7.893070,3.170907,9.850677,6.744801,-2.228043,-3.035985,8.664974,-6.158811,-7.894974,-0.295505,3.206590,0.067432,-4.523761,4.970095,-5.024222,-9.283150,-8.952288,-3.592455,-7.453579,1.399351,-6.812988,-8.542003,-4.241794,5.241465,5.862950,-2.319332,8.962045,9.088165,8.592344,6.644214,-5.913303,1.600080,1.024019,-8.302687,-1.958200,-6.247571,-2.545483,-9.559333,3.941659,0.386246,2.794354,-4.729028,9.723224,6.647263,-6.176072,-3.363753,-3.865674,-1.264025,-1.016551,4.782050,-3.673682,2.607192,-8.234235,4.946338,6.682797,3.179708,-0.922689,-8.416288,0.366277,-6.040024,-0.983405,-3.555606,4.757468,-8.568679,-2.115012,-2.045465,2.877750,4.595419,4.828708,3.804892,3.108604,-2.211114,-6.131058,6.912512,-5.739975,-6.869351,5.334573,1.978221,8.696823,-3.446085,6.002902,-1.542432,-5.131698,4.403781,-8.728686,5.708798,9.054934,-9.323886,-3.840152,1.122334,9.808891,6.867644,3.997373,6.452344,-1.336631,-3.774607,-0.540560,-5.736553,-1.830372,1.574860,-1.709202,-6.347817,-9.515135,-6.892671,-9.693438,3.326047,3.297538,-5.223403,2.092720,4.044817,7.919636,1.040468,-0.483212,1.846331,0.583447,3.490571,1.985571,4.267316,-4.303580,-8.577245,-5.220855,8.592525,-4.877649,-0.424900,7.619556,0.442612,7.745728,1.892124,-3.964139,-9.853123,9.593390,2.743980,8.302684,-6.311541,-2.890783,-8.121786,-3.029826,-6.850567,-9.584797,-1.209382,-8.603685,-6.830921,-0.686547,3.415199,-4.552797,0.413662,-3.888850,-8.229559,1.169399,4.557963,0.305577,-8.039969,7.883175,-8.896264,7.437410,-8.952128,-2.939387,5.912665,-5.630307,4.305225,-7.467637,-4.247835,-8.624406,-1.429115,0.899276,1.286009,-3.490187,-2.333516,4.076215,4.686755,4.184948,-4.689692,-9.900604,-1.936121,7.590855,-6.933758,-3.094544,-9.290913], dtype = "float32")#candidate|3085|(432,)|const|float32
call_3081 = relay.TupleGetItem(func_1972_call(relay.reshape(const_3082.astype('float32'), [4, 9, 5]), relay.reshape(var_3083.astype('int8'), [10368,]), relay.reshape(const_3084.astype('int16'), [936,]), relay.reshape(const_3085.astype('float32'), [4, 9, 12]), ), 15)
call_3086 = relay.TupleGetItem(func_1978_call(relay.reshape(const_3082.astype('float32'), [4, 9, 5]), relay.reshape(var_3083.astype('int8'), [10368,]), relay.reshape(const_3084.astype('int16'), [936,]), relay.reshape(const_3085.astype('float32'), [4, 9, 12]), ), 15)
output = relay.Tuple([call_3079,call_3081,const_3082,var_3083,const_3084,const_3085,])
output2 = relay.Tuple([call_3080,call_3086,const_3082,var_3083,const_3084,const_3085,])
func_3113 = relay.Function([var_3083,], output)
mod['func_3113'] = func_3113
mod = relay.transform.InferType()(mod)
mutated_mod['func_3113'] = func_3113
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3114 = relay.var("var_3114", dtype = "int8", shape = (10368,))#candidate|3114|(10368,)|var|int8
func_3113_call = mutated_mod.get_global_var('func_3113')
call_3115 = func_3113_call(var_3114)
output = call_3115
func_3116 = relay.Function([var_3114], output)
mutated_mod['func_3116'] = func_3116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1617_call = mod.get_global_var('func_1617')
func_1618_call = mutated_mod.get_global_var('func_1618')
call_3147 = relay.TupleGetItem(func_1617_call(), 0)
call_3148 = relay.TupleGetItem(func_1618_call(), 0)
func_1311_call = mod.get_global_var('func_1311')
func_1313_call = mutated_mod.get_global_var('func_1313')
call_3161 = relay.TupleGetItem(func_1311_call(), 0)
call_3162 = relay.TupleGetItem(func_1313_call(), 0)
output = relay.Tuple([call_3147,call_3161,])
output2 = relay.Tuple([call_3148,call_3162,])
func_3165 = relay.Function([], output)
mod['func_3165'] = func_3165
mod = relay.transform.InferType()(mod)
output = func_3165()
func_3166 = relay.Function([], output)
mutated_mod['func_3166'] = func_3166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1684_call = mod.get_global_var('func_1684')
func_1685_call = mutated_mod.get_global_var('func_1685')
call_3187 = relay.TupleGetItem(func_1684_call(), 0)
call_3188 = relay.TupleGetItem(func_1685_call(), 0)
output = call_3187
output2 = call_3188
func_3204 = relay.Function([], output)
mod['func_3204'] = func_3204
mod = relay.transform.InferType()(mod)
mutated_mod['func_3204'] = func_3204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3204_call = mutated_mod.get_global_var('func_3204')
call_3205 = func_3204_call()
output = call_3205
func_3206 = relay.Function([], output)
mutated_mod['func_3206'] = func_3206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1179_call = mod.get_global_var('func_1179')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_3219 = func_1179_call()
call_3220 = func_1179_call()
func_1413_call = mod.get_global_var('func_1413')
func_1415_call = mutated_mod.get_global_var('func_1415')
var_3229 = relay.var("var_3229", dtype = "int16", shape = (936,))#candidate|3229|(936,)|var|int16
call_3228 = relay.TupleGetItem(func_1413_call(relay.reshape(var_3229.astype('int16'), [8, 9, 13])), 0)
call_3230 = relay.TupleGetItem(func_1415_call(relay.reshape(var_3229.astype('int16'), [8, 9, 13])), 0)
func_164_call = mod.get_global_var('func_164')
func_168_call = mutated_mod.get_global_var('func_168')
const_3238 = relay.const([-4.985108,1.537642,2.223598,6.380074,2.087952,9.992243,-7.005819,8.569197,9.788408,-7.523096,-1.076115,3.395830,-2.954345,-2.570377,5.189861,-0.009865,-1.916332,4.950239,-0.690269,3.241548,2.951468,-2.078804,-9.925103,-1.258147,2.915503,7.884172,-2.064815,0.112146,-7.004522,-4.831951,7.194130,-0.142009,4.418779,-2.504350,-3.146563,6.248018,-7.806765,-4.235303,7.316577,-2.811582,7.705930,-9.049028,-2.295174,8.098053,1.349730,4.516858,-5.107948,-0.449605,7.236838,-3.401816,6.114330,6.472322,2.696943,-6.780326,-8.742002,6.917039,-1.039008,-3.309579,0.991196,5.241732,5.105036,5.707028,-7.253628,2.803615,-6.469594,-0.506331,4.132439,4.607435,0.710440,5.670775,-8.775847,4.052937,-4.312803,-5.351244,2.107448,8.904023,-6.941052,3.956396,-2.688022,-0.571584,-5.360240,-6.538054,-1.978381,-6.965451,7.185595,-9.625514,-4.077120,-5.445594,1.003620,-6.884279,5.920662,2.141553,-7.952406,-7.421728,-4.068786,-1.699635,5.581531,-4.900084,-2.328116,6.946371,0.528519,-3.408815,-0.776234,-2.241569,9.663784,-6.834347,-0.188987,-5.457140,-0.205674,-2.875521,5.645194,9.440191,1.776193,-7.011338,-3.817131,-4.427122,1.061119,9.328939,1.454379,8.056162,-4.801221,0.542424,-9.798997,-0.257733,0.376973,6.883243,7.475341,7.519902,-7.340575,-7.931688,-9.469439,-3.941387,1.215503,5.246263,-8.317625,6.505640,-4.267561,4.178665,-4.451840,-2.002531,-4.599040,-8.384931,-4.126217,3.683918,-2.534668,-1.107171,-8.653855,-6.756212,-2.212633,-6.733368,6.628258,-2.653108,0.856528,-3.471003,7.724921,6.916027,-4.932081,4.882928,2.142244,3.262475,-6.017842,-5.551320,5.228136,9.728552,-7.536177,-8.576343,4.367715,-9.581649,-8.582646,7.369307,9.190629,-7.144071,-3.968468,-5.962200,-3.861029,7.593369,5.396380,2.491052,3.944242,9.772141,-1.164768,5.938603,-4.422269,-0.438195,-6.204267,-0.876333,-4.951306,6.934571,-9.445695,1.991046,4.577071,8.683285,-6.830982,0.486785,8.953011,-8.832557,-4.368897,-4.915692,1.985361,-7.644201,-8.767689,3.240933,6.793555,9.546405,-0.848263,-8.379601,-9.922987,2.349439,-7.815264,-7.464448,2.886513,7.340888,-1.155803,-7.040986,1.546736,6.246817,3.684443,-2.112011,5.498879,-7.833304,-7.707059,4.489291,-0.252694,-3.550412,-2.753356,7.029392,8.881040,8.620441,-1.823524,6.218377,-6.776899,1.527244,5.644792,-0.463667,2.857521,-7.648771,6.520156,-1.098528,-1.343412,-1.171836,5.004002,-2.959232,9.700873,-6.541842,7.064074,8.121775,-2.567757,4.138375,-7.934918,-1.708198,-6.747795,-3.182424,8.464222,-1.004537,8.785427,-3.003145,-5.099710,9.945970,-9.311757,7.999950,4.645978,-6.551679,6.058362,7.540396,8.305819,1.515230,-1.551489,-7.801822,0.715023,-6.338881,6.604933,7.406421,1.670751,2.181742,1.352958,-4.862169,5.531252,-1.469098,-4.100880,3.313567,-3.539395,-4.971349,-4.455329,-2.901415,2.840513,-1.787767,9.792183,-1.166873,-7.921524,-1.213596,-5.435019,-8.439051,5.168656,-1.319972,-3.117888,-6.376633,-5.675625,1.245264,2.440436,-8.163374,-6.066498,0.157788,9.885610,7.963956,-0.756595,6.564047,-3.998358,-8.827408,-5.738021,3.745746,-1.013279,2.248731,-5.408686,2.665681,-4.120601,-3.830151,-3.361162,-0.493824,3.220875,8.713395,-4.162369,-4.020233,-8.157134,-5.422262,2.983105,5.034003,7.457815,0.410543,-2.610612,5.658713,-8.410504,1.219351,-2.017090,-3.563687,6.727109,5.030685,-3.673185,-0.257520,-5.096925,-3.185157,7.472615,-6.975867,-7.520228,-6.463623,-2.073570,-6.585169,-5.714739,-2.625770,7.667651,-2.520026,-1.728218,-4.641866,-2.585155,-3.017236,-4.665982,-0.286951,-3.508003,-7.835775,-6.141961,5.386303,0.995338,-7.256113,-0.004218,-9.990192,4.514036,-5.246434,-8.710372,2.937630,-5.247854,5.305750,-6.300102,-6.875109,-4.712868,4.273684,6.076900,-9.737054,-3.281869,-6.107385,8.873145,8.962258,-2.158580,-6.978728,-3.290680,4.850776,1.540907,7.973107,-4.282186,3.062753,0.868427,-9.030891,2.976755,6.162743,0.990978,-2.573859,-7.890687,8.224908,-6.079362,9.869203,8.332801,4.255833,8.639590,-4.967931,-5.967786,6.343371,2.225410,-1.531541,-1.081475,-7.628526,-1.833129,-7.593475,-7.976073,6.462170,7.397462,-9.834718,2.203970,-6.529573,-6.595277,-1.964275,-5.322480,-2.940941,7.059400,-8.818073,-6.333369,7.383422,-2.746634,4.520947,-7.748267,8.323021,9.296251,-9.483591,3.198464,-2.613719,-7.644784,-5.864868,-5.233979,-5.876295,6.024205,6.290096,9.524114,-8.481134,-6.514028,9.425516,-0.565085,-9.153933,-4.763465,-7.278359,1.488583,9.939850,-4.916453,-0.454123,6.497581,-0.221654,-7.726159,-4.323700,0.910047,3.343275,2.370654,-8.284233,8.876506,3.698913,7.782485,5.875090,-2.612864,-5.102668,-7.128488,5.513865,9.245368,-6.220829,2.936954,-9.438653,-7.353619,-0.203103,-6.754450,2.727019,-5.714085,6.252318,1.324666,-4.013554,6.012587,-8.405284,-3.798060,0.446016,0.042505,8.032661,0.313419,0.180305,3.858325,4.695380,-0.861180,4.485349,4.619057,0.972980,6.538507,0.171397,-9.610914,-3.473584,8.114122,7.119139,5.485531,-7.670305,-2.974734,-8.981508,6.465462,6.592328,2.874433,-8.707304,3.033963,1.328435,-3.837611,3.560722,-4.593812,8.042159,-8.819126,-4.953027,1.458381,-9.685395,1.633946,0.124006,-2.825282,-3.944117,4.331898,-9.788713,-9.848927,0.097494,-7.627182,-3.224800,-8.827036,9.115754,-4.770595,-7.290977,-6.696555,5.707642,-4.410873,-6.666543,6.134949,-0.945575,-7.246746,3.044463,-4.479998,0.612074,4.077064,0.927890,7.317164,-9.830737,-5.371369,6.192533,2.222977,-3.519720,1.698155,-4.789389,-0.414921,1.305084,-3.587883,8.047025,3.579983,0.036362,-7.315656,-5.877959,8.372195,6.955437,7.672236,-1.476156,5.469422,-4.851485,-4.410997,2.199486,6.021117,7.958846,4.744569,-6.557217,4.199937,-7.308695,-9.123346,1.248803,1.659291,-1.402598,5.095679,-9.581928,2.064667,0.777758,3.258293,-2.242985,8.528266,-1.154783,4.032095,9.556482,7.431076,-5.428805,-0.866826,6.267329,7.227909,-5.523160,0.907971,1.134211,-0.713423,-0.147171,-5.472763,-0.504289,-0.226953,-0.435855,-2.879596,-3.454950,9.395968,2.392735,-1.988854,-7.100079,-5.130229,-0.985310,1.473438,4.499524,-1.162473,4.383978,-9.603125,-7.593634,2.867605,-1.811868,-0.454414,6.940699,-9.623070,9.627353,2.397017,-6.910023,-6.276788,8.455446,-0.287696,4.417635,-5.187880,5.888651,1.825878,4.265673,4.117567,-7.947866,-5.572355,4.719485,-1.999524,1.672393,-9.753700,-7.298259,-2.617859,-4.375325,-1.883133,8.176930,3.832893,4.121141,-0.301505,9.760086,2.402738,7.997893,2.979959,-5.773638,0.753884,1.310716,7.335590,8.391515,-2.307363,-8.861804,4.889179,5.025465,9.414315,3.203942,-7.146029,0.409325,-7.236144,9.753830,4.000941,-2.166153,-1.947961,4.531193,1.730098,9.430087,-8.526433,-2.367142,-7.036608,-9.921422,-1.335784,9.419510,-0.730719,-9.954572,-7.401416,-7.299204,0.719828,-9.185580,1.912580,4.907747,-9.659181,-0.237536,2.007701,4.976647,-9.363838,9.073724,6.008341,1.180557,6.319111,9.053824,-6.639200,7.564886,-8.016267,5.439178,6.832744,-2.796681,4.065873,6.408685,7.512621,-4.669637,-6.537914,-7.352584,8.469772,-8.953841,-3.772217,-4.703645,4.742720,-3.948502,7.137097,5.013090,8.801594,4.707809,-2.169141,1.307920,1.808177,-6.774581,7.177664,8.897384,-9.405001,1.768400,9.891840,9.514221,4.736145,-2.593857,6.125033,-2.214440,6.505762,-0.156443,-9.020578,0.767776,5.824242,4.731139,9.943572,6.211321,-7.028228,-2.430647,-9.687102,7.628641,5.998972,8.526630,5.081610,9.282874,0.032853,3.429109,2.750318,2.506400,-6.683803,9.631536,0.034730,5.280566,7.754807,-5.425079,-8.308020,-6.362928,0.994195,-8.952150,3.856234,-3.083231,2.031092,-5.625058,-3.945501,-3.253456,-7.191852,-2.699027,-6.315095,-9.780268,3.903452,-6.083379,-1.767518,-9.106691,-4.687829,-0.338360,-8.325218,-6.712248,-9.788599,5.349334,-2.807701,0.869987,1.529296,-2.966017,-8.004167,-1.841339,0.638989,9.531166,6.429675,-4.542003,-3.617399,6.928032,5.136983,8.357586,-5.092543,-3.514683,-5.447097,2.661996,-5.511944,7.267403,-5.138528,-3.249241,-6.932215,2.855078,2.507039,4.536127,3.830259,3.173584,-7.496068,-6.816213,9.792003,0.644117,0.910773,9.398962,6.788503,-4.093491,-8.241312,7.203877,-4.058242,-3.991430,-2.846166,2.989755,-5.142156,-6.993411,5.855104,8.467914,-0.998403,-4.913614,-4.189248,1.757565,7.372056,5.111299,-8.067923,-8.647797,-3.321150,8.822841,3.600661,-9.809505,9.093782,-6.649400,8.130282,2.307936,2.543355,0.189844,1.693621,1.187353,-7.059846,9.008990,9.464767,9.898635,-3.550522,4.354660,-1.755528,-0.642711,-9.729208,-3.666896,-7.389089,7.119928,-2.819078,3.446136,0.716469,-9.257110,-9.960582,2.706951,6.933863,2.919100,7.133757,8.947885,-8.285278,9.113569,3.550596,-6.603514,2.540293,3.534832,9.535420,3.295788,8.790768,-3.187035,4.567594,6.144818,9.093924,8.231990,2.083229,-0.050774,-2.685671,3.648226,2.615481,4.878767,1.097670,-0.117022,-7.938683,-9.044277,3.275281,0.675683,-9.016019,-7.776906,9.120014,-0.785926,-8.392136,-8.323094,-1.874367,-1.079510,3.971478,-6.102876,-4.294753,2.503625,-3.454852,-1.299199,8.599830,7.038053,2.734060,7.591892,2.200918,3.743912,-8.784287,-5.991397,1.848277,-1.970202,-7.726338,-6.459380,-1.273349,9.711393,2.121046,-9.652013,2.675221,-9.903418,7.293417,0.872468,0.342356,7.953886,-2.373950,-1.755407,-2.359580,1.940712,0.558068,-6.328476,5.789199,-2.795819,7.775716,5.936926,-3.098694,9.866921,8.398168,-1.434453,-0.829971,-7.105507,0.365699,-0.959403,-2.181007,8.234669,1.020479,1.171800,8.311000,9.483753,-7.967585,-0.335946,-0.635299,8.157790,-1.086535,-1.057170,6.664169,-9.491385,2.486596,-6.215249,-3.473990,5.964109,0.314423,-9.737751,9.754865,-6.299309,6.792678,-7.767624,-6.759561,8.238228,-6.900411,3.920871,9.161771,-9.629394,0.849473,-3.147873,-4.400527,8.276298,-9.753687,6.274366,-4.246598,5.001170,-5.614141,9.800571,5.277162,3.692892,1.559966,2.517241,-4.930193,9.386271,5.427355,3.544215,-1.948504,3.854096,2.852883,-8.883322,-0.789723,8.930807,6.092490,-1.107013,6.233799,-6.711855,-9.870636,7.897742,-7.381595,-5.996755,-4.642959,3.216749,1.513745,3.322374,1.950240,-6.151294,-2.131968,-0.412709,-5.810862,-2.703451,9.570414,-8.916919,2.632441,-9.321556,4.930986,2.788367,2.508819,-8.076127,2.842780,2.523302,4.462305,2.067435,2.220586,0.974363,-6.486905,7.258883,6.480268,9.156221,-8.162923,-6.807206,5.406432,7.438866,-4.484672,8.868560,-8.701971,5.624178,-4.392577,5.433737,-1.221367,5.629830,-9.558261,-3.102790,8.906963,-3.678001,-4.075786,7.287890,-2.814828,-7.484882,-7.986199,9.890441,-5.237002,-9.325973,5.120249,-0.929196,-5.365235,-6.382553,-1.907091,-3.800929,-3.156772,3.938238,8.053734,-0.143653,-5.131171,1.066357,-0.461284,1.321745,4.622238,3.191141,6.456294,-1.072247,-2.862060,-3.019724,-9.202362,-6.458177,-1.471306,5.416068,-4.664157,2.752270,-4.758620,6.085096,3.162695,4.617535,-5.749503,2.644574,-3.647468,5.648653,-5.607312,8.267154,1.282179,-2.726523,-5.412226,7.386259,3.593894,4.147743,0.871777,2.603934,4.224889,7.841420,7.532761,0.651104,3.752282,-9.279590,-6.686629,-1.346538,5.918771,0.644596,-6.453880,-1.548456,-2.052796,0.852555,-0.534957,-5.617240,9.942171,5.608746,4.318502,-7.437774,-4.508302,-7.195130,-0.638414,-4.777941,7.326657,2.574343,-9.484831,-5.199293,7.074099,0.560221,-7.764680,5.303998,9.786635,-4.374799,0.037659,3.358167,-8.761114,9.426434,-8.409395,-7.582386,4.318236,3.034634,-1.093017,-5.680005,3.363183,9.625238,-5.172462,4.279199,-1.287771,-0.455032,-6.804530,1.617395,8.483625,-9.019286,-6.246860,-9.987275,-8.482231,4.694667,4.695300,3.549551,7.469616,-4.809764,6.491027,-9.100984,3.504545,-2.277680,-0.387808,-4.705106,-6.891025,-1.872134,-9.671806,-1.369657,-0.339935,8.309447,-3.496414,2.783200,7.691107,6.944771,4.724377,-1.099382,-6.474996,5.973414,-0.596590,-3.850708,-5.612573,6.095088,1.137167,0.884798,-7.558599,3.011732,1.425976,-6.470059,-1.401527,-5.472076,1.595863,5.541251,4.352609,6.213118,-5.254017,-1.670314,-4.344766,0.660523,9.619706,3.767523,1.570048,-6.441591,8.820142,-3.159127,-2.126412,-1.531510,8.894259,3.712113,-3.088927,5.929877,5.904384,1.972664,8.666317,6.774821,1.167029,-7.597033,-9.552401,-1.811504,-9.736481,1.565528,9.255406,-7.208703,1.584972,1.059956,-0.031515,8.149235,-5.410413,3.312920,0.865204,-5.184702,-6.554120,-2.258108,-8.642750,-1.248744,0.238126,0.652443,3.007741,4.833539,-0.786181,-0.884316,5.776118,-7.763819,-7.361906,-1.169028,-5.363962,1.835906,7.449266,2.075954,-7.041220,-1.732531,-4.542228,-8.456680,-8.208840,-5.415791,-8.927619,1.016052,-1.080471,3.379468,-0.595064,5.348168,-6.770917,6.087287,-7.677312,5.130001,-6.901044,-3.926207,-2.875071,3.166183,-5.332045,7.514858,-0.124388,3.333986,-4.810701,-2.313300,-6.226676,8.422859,-6.594445,-6.080764,-5.182552,3.389456,-9.925090,8.851032,-6.134618,7.124067,-0.676930,9.209924,7.862091,-2.518828,4.788338,-5.499607,-8.000888,-3.729357,-0.933782,7.934795,5.691647,-8.687053,-5.889814,-0.074739,-9.305097,6.761067,-8.891302,8.146738,5.426445,3.369258,-9.687185,-3.902622,9.343396,1.054697,-1.874084,-7.126527,1.914686,4.078715,-5.782505,-1.879408,1.108644,-6.022681,-8.585841,7.262837,7.158248,-9.930408,2.444229,-8.443940,-1.726420,-1.074250,-2.366549,-6.113268,3.629630,7.460247,0.985553,-7.303295,8.400949,-7.238334,2.035842,-0.409514,-1.216851,-3.146868,5.958206,-8.578277,1.630859,-3.799365,-7.741447,4.202087,-8.963598,1.192712,7.273048,-6.236083,-8.198393,-2.524404,3.726747,-7.836024,-6.527768,4.553886,9.890858,8.415268,-6.741732,-1.038281,-7.623989,5.840561,-6.778703,-0.276417,-2.998732,8.232168,7.746618,-0.091524,-4.881817,-9.126735,-2.703666,-1.512902,7.039627,-9.692568,-3.412838,-1.781453,-6.542298,1.980477,1.935745,-2.947535,0.410610,-3.361620,-4.419600,9.298221,-0.279038,2.445243,7.045231,-8.836946,1.433250,-1.489085,-9.579252,-6.976593,-2.961734,3.146150,7.061340,-0.850645,3.232881,9.537504,5.546779,-8.895380,-5.899858,-2.924368,-8.836191,-4.246133,2.429329,6.318695,-2.722993,6.327654,0.550022,-1.324422,-3.853642,5.003577,9.080605,2.101633,4.369555,-9.261897,2.403143,4.915289,-6.275233,8.684544,2.814088,2.742861,-6.859706,-5.445373,6.284400,-4.674632,7.012257,-8.047805,-0.502677,-1.863426,0.625000,5.653077,2.630879,-2.385511,9.727335,-0.738421,-1.491481,-5.641414,-2.510200,8.245212,6.982625,9.842761,0.117108,7.046508,-5.706302,-1.861112,5.701793,-6.335178,-3.930885,-9.946435,9.230134,-2.854706,-3.619711,-6.914333,-9.564078,-2.084425,-5.793123,-4.987766,1.477956,3.028331,9.101756,-3.212499,-4.716898,-0.490711,4.397599,-0.309888,6.503768,5.592717,0.411436,-0.793641,7.341577,8.603414,-0.427268,7.784836,2.685163,7.172224,-3.124515,2.636271,5.304707,-2.177054,-4.988213,4.089803,5.532239,3.119953,-0.698435,-2.180410,7.653367,7.347167,-2.859473,5.549423,-2.142051,-5.493966,-1.827660,5.723758,1.275282,5.851339,-0.891869,8.113912,5.270123,-2.605989,-9.243216,3.997137,-6.981230,-8.622052,9.036338,-8.301461,-5.932741,4.708103,3.318071,-1.722527,-6.087187,-6.570418,-0.776969,-5.693593,0.364903,-6.870311,-7.531341,4.236549,-1.733705,2.874381,9.126592,2.664621,-7.667185,4.704226,1.714805,6.452436,9.874329,-7.360240,4.191800,2.594556,6.374297,5.646816,5.909142,-8.893300], dtype = "float32")#candidate|3238|(1540,)|const|float32
call_3237 = func_164_call(relay.reshape(const_3238.astype('float32'), [10, 14, 11]), relay.reshape(const_3238.astype('float32'), [10, 14, 11]), )
call_3239 = func_164_call(relay.reshape(const_3238.astype('float32'), [10, 14, 11]), relay.reshape(const_3238.astype('float32'), [10, 14, 11]), )
output = relay.Tuple([call_3219,call_3228,var_3229,call_3237,const_3238,])
output2 = relay.Tuple([call_3220,call_3230,var_3229,call_3239,const_3238,])
func_3244 = relay.Function([var_3229,], output)
mod['func_3244'] = func_3244
mod = relay.transform.InferType()(mod)
var_3245 = relay.var("var_3245", dtype = "int16", shape = (936,))#candidate|3245|(936,)|var|int16
output = func_3244(var_3245)
func_3246 = relay.Function([var_3245], output)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2299_call = mod.get_global_var('func_2299')
func_2301_call = mutated_mod.get_global_var('func_2301')
call_3326 = relay.TupleGetItem(func_2299_call(), 2)
call_3327 = relay.TupleGetItem(func_2301_call(), 2)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_3334 = relay.TupleGetItem(func_653_call(), 0)
call_3335 = relay.TupleGetItem(func_654_call(), 0)
func_1216_call = mod.get_global_var('func_1216')
func_1219_call = mutated_mod.get_global_var('func_1219')
var_3337 = relay.var("var_3337", dtype = "int8", shape = (10368,))#candidate|3337|(10368,)|var|int8
call_3336 = relay.TupleGetItem(func_1216_call(relay.reshape(var_3337.astype('int8'), [4, 9, 288])), 1)
call_3338 = relay.TupleGetItem(func_1219_call(relay.reshape(var_3337.astype('int8'), [4, 9, 288])), 1)
func_1710_call = mod.get_global_var('func_1710')
func_1713_call = mutated_mod.get_global_var('func_1713')
const_3341 = relay.const([2,7,5,-3,1,4,1,-3,-1,-5,8,-10,2,10,9,-4,-3,7,6,-2,-5,6,6,-2,8,5,7,8,-5,1,-2,-5,7,-4,3,-4,2,-6,-1,5,-8,-9,8,-6,-4,6,-3,2,6,3,-1,10,8,4,-4,1,1,-9,-5,-1,2,-4,10,-5,1,-6,6,8,1,3,2,9,2,-2,5,-6,3,-1,8,-1,-5,-3,-2,5,4,-9,2,2,8,-2,9,7,10,5,8,-6,3,-6,-10,-10,-8,3,-9,-5,8,7,5,-7,5,-2,-10,-8,8,9,6,4,-2,-6,-1,9,8,5,1,-10,-6,3,-3,-10,-6,8,-10,-6,9,-3,-4,-10,-8,10,8,10,-4,-1,-4,7,10,2,8,-10,1,-9,-8,9,-3,7,-1,-7,-10,4,-7,-3,-6,7,-2,-1,4,8,-9,8,-8,-5,-4,5,-1,7,10,7,7,-8,-2,-4,10,-6,10,1,1,-6,10,-8,-10,1,8,-4,1,-6,2,9,1,-1,3,9,-9,8,6,-10,-4,-6,6,-7,-3,-2,-2,-7,8,2,-9,5,7,7,3,2,6,-10,-10,-1,-10,8,-6,5,-4,-7,-9,10,8,-1,-5,-8,1,-5,-5,-3,-3,-8,-9,-5,1,5,6,8,-5,7,-2,-10,1,3,4,-10,1,6,-1,1,4,-4,3,4,-10,7,6,-2,-5,-2,5,7,-9,3,5,2,2,-10,5,-3,7,-7,-9,9,-6,-4,2,-6,-6,1,-5,-1,-6,-9,6,-7,2,-3,5,-7,-2,3,-4,-5,7,2,-6,8,5,-6,-1,-2,-9,4,-9,-4,-1,7,5,6,7,-4,4,-8,1,-7,-6,-5,-8,-8,1,-9,8,-10,9,7,-5,-10,4,7,1,6,-5,-2,-2,-1,4,-5,-6,-7,10,-1,-6,-5,9,6,8,-7,4,7,4,9,5,-10,9,-8,-3,6,-1,10,3,-2,-9,-3,10,9,7,2,3,5,-1,-3,-3,4,9,6,9,2,-6,-10,-6,-10,8,5,4,-5,2,-9,-6,10,8,-7,5,6,-4,-8,7,3,10,9,7,-10,2,5,4,-3,-3,-9,8,8,2,-6,5,-6,-7,-10,-1,-1,-10,2,2,-6,4,1,-1,-7,6,3,1,6,-4,-10,7,-9,10,10,-5,-6,2,-2,-8,-7,10,-6,9,1,-8,-10,4,1,9,7,10,4,3,-6,-4,-5,-2,7,5,-5,-9,-8,-4,-9,2,8,1,5,-9,5,5,8,-3,1,3,8,2,-6,-5,-1,3,1,3,-8,-9,6,2,-5,10,-10,-3,6,-6,-2,-9,8,-2,8,6,-10,8,1,1,-3,-2,-6,3,2,4,10,7,-7,-8,-4,2,9,1,8,-8,5,-5,-6,-2,-10,10,-10,-2,6,6,6,6,-6,7,-1,4,-4,-6,9,-7,-4,1,-6,3,-4,-3,-6,6,-8,-5,-8,6,10,-2,-9,10,-8,7,3,-7,10,-7,-3,-8,6,1,-2,5,8,-1,-8,8,1,1,7,2,10,-4,2,3,3,3,-10,7,8,4,-8,-2,-8,-4,-1,-10,6,3,6,-8,-1,-6,3,-10,3,7,-6,4,-3,9,-5,-6,-7,-10,8,-1,3,3,-3,7,9,-9,6,-1,2,-5,-2,-7,-4,9,-7,1,10,-5,7,8,9,-2,-1,-4,-4,-9,1,-5,-4,-7,7,-2,3,9,-3,-7,4,-7,-2,-7,9,-3,3,7,2,-2,-1,-3,4,-6,9,-1,-3,-8,-9,-1,3,1,10,5,2,-9,2,1,6,-4,1,7,-4,-6,2,-1,1,-10,2,1,3,-8,5,-10,7,5,-1,-9,-7,-8,-4,5,1,-6,-1,8,8,8,7,4,5,-9,2,-1,-7,-10,-8,-6,-2,-3,-9,8,6,3,-5,-7,-8,7,8,-1,-7,-6,7,3,4,2,-6,5,6,7,-6,-2,-3,-4,-6,-6,5,-7,5,2,3,-7,6,-3,1,-4,4,-3,4,8,10,5,7,10,10,-1,7,4,-9,4,6,-9,5,-5,-9,2,-8,-7,-7,-5,8,-3,-6,-6,5,7,1,2,-7,-6,-2,8,-5,5,1,-10,7,-5,2,10,-3,-1,-2,-10,-9,-7,-5,1,9,2,5,10,7,7,-7,1,3,-4,-2,-5,-3,4,-9,-9,-10,-8,-5,8,-4,-5,1,10,-7,-8,3,2,6,-5,10,3,3,6,10,1,-1,2,10,4,10,-6,5,-6,-5,-8,-5,6,2,7,8,-5,-4,-10,1,-2,8,-2,10,-6,3,8,6,-5,8,10,9,6,4,-8,4,8,1,-6,1,4,7,9,7,-2,5,-2,9,8,6,10,7,1,-7,-7,-9,10,4,-1,-5,-6,7,5,-6,3,10,-1,1,-4,-8,-7,-1,-5,8,6,9,4,-1,-3,-3,-8,-10,-1,-10], dtype = "int16")#candidate|3341|(936,)|const|int16
call_3340 = relay.TupleGetItem(func_1710_call(relay.reshape(const_3341.astype('int16'), [936,])), 0)
call_3342 = relay.TupleGetItem(func_1713_call(relay.reshape(const_3341.astype('int16'), [936,])), 0)
bop_3361 = relay.floor_divide(call_3336.astype('float64'), relay.reshape(var_3337.astype('float64'), relay.shape_of(call_3336))) # shape=(4, 9, 288)
bop_3364 = relay.floor_divide(call_3338.astype('float64'), relay.reshape(var_3337.astype('float64'), relay.shape_of(call_3338))) # shape=(4, 9, 288)
output = relay.Tuple([call_3326,call_3334,call_3340,const_3341,bop_3361,])
output2 = relay.Tuple([call_3327,call_3335,call_3342,const_3341,bop_3364,])
func_3367 = relay.Function([var_3337,], output)
mod['func_3367'] = func_3367
mod = relay.transform.InferType()(mod)
mutated_mod['func_3367'] = func_3367
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3368 = relay.var("var_3368", dtype = "int8", shape = (10368,))#candidate|3368|(10368,)|var|int8
func_3367_call = mutated_mod.get_global_var('func_3367')
call_3369 = func_3367_call(var_3368)
output = call_3369
func_3370 = relay.Function([var_3368], output)
mutated_mod['func_3370'] = func_3370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2445_call = mod.get_global_var('func_2445')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_3380 = func_2445_call()
call_3381 = func_2445_call()
output = relay.Tuple([call_3380,])
output2 = relay.Tuple([call_3381,])
func_3392 = relay.Function([], output)
mod['func_3392'] = func_3392
mod = relay.transform.InferType()(mod)
output = func_3392()
func_3393 = relay.Function([], output)
mutated_mod['func_3393'] = func_3393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2477_call = mod.get_global_var('func_2477')
func_2479_call = mutated_mod.get_global_var('func_2479')
call_3440 = func_2477_call()
call_3441 = func_2477_call()
func_1710_call = mod.get_global_var('func_1710')
func_1713_call = mutated_mod.get_global_var('func_1713')
var_3458 = relay.var("var_3458", dtype = "int16", shape = (1, 936))#candidate|3458|(1, 936)|var|int16
call_3457 = relay.TupleGetItem(func_1710_call(relay.reshape(var_3458.astype('int16'), [936,])), 2)
call_3459 = relay.TupleGetItem(func_1713_call(relay.reshape(var_3458.astype('int16'), [936,])), 2)
uop_3463 = relay.atan(var_3458.astype('float64')) # shape=(1, 936)
output = relay.Tuple([call_3440,call_3457,uop_3463,])
output2 = relay.Tuple([call_3441,call_3459,uop_3463,])
func_3465 = relay.Function([var_3458,], output)
mod['func_3465'] = func_3465
mod = relay.transform.InferType()(mod)
mutated_mod['func_3465'] = func_3465
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3466 = relay.var("var_3466", dtype = "int16", shape = (1, 936))#candidate|3466|(1, 936)|var|int16
func_3465_call = mutated_mod.get_global_var('func_3465')
call_3467 = func_3465_call(var_3466)
output = call_3467
func_3468 = relay.Function([var_3466], output)
mutated_mod['func_3468'] = func_3468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2063_call = mod.get_global_var('func_2063')
func_2065_call = mutated_mod.get_global_var('func_2065')
call_3517 = relay.TupleGetItem(func_2063_call(), 0)
call_3518 = relay.TupleGetItem(func_2065_call(), 0)
output = call_3517
output2 = call_3518
func_3523 = relay.Function([], output)
mod['func_3523'] = func_3523
mod = relay.transform.InferType()(mod)
output = func_3523()
func_3524 = relay.Function([], output)
mutated_mod['func_3524'] = func_3524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_959_call = mod.get_global_var('func_959')
func_960_call = mutated_mod.get_global_var('func_960')
call_3541 = func_959_call()
call_3542 = func_959_call()
output = relay.Tuple([call_3541,])
output2 = relay.Tuple([call_3542,])
func_3543 = relay.Function([], output)
mod['func_3543'] = func_3543
mod = relay.transform.InferType()(mod)
output = func_3543()
func_3544 = relay.Function([], output)
mutated_mod['func_3544'] = func_3544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2699_call = mutated_mod.get_global_var('func_2699')
call_3571 = relay.TupleGetItem(func_2698_call(), 0)
call_3572 = relay.TupleGetItem(func_2699_call(), 0)
func_33_call = mod.get_global_var('func_33')
func_37_call = mutated_mod.get_global_var('func_37')
const_3587 = relay.const([1,8,8,6,8,4,-4,-5,10,-8,4,10,-5,-6,-5,7,5,-5,-5,-2,-5,-3,9,1,3,-8,-9,7,-1,4,7,3,-5,7,-1,5,5,-4,5,-6,5,7,2,-9,-10,2,4,-1,2,-1,7,1,-3,6,10,-10,6,10,-3,5,-2,1,10,5,10,-9,9,8,-4,-1,6,9,9,4,-8,5,5,4,-8,1,4,-4,7,6,-6,-6,-10,-6,2,-3,10,10,6,3,4,1,-2,-2,8,-2,9,-7,-1,-8,-5,-5,8,10,-1,7,5,-5,6,-9,7,7,9,5,-8,-7,3,-6,9,-7,9,10,-6,2,-2,4,-2,5,8,-3,2,-9,-2,-8,-3,3,-10,5,-8,8,9,1,-7,-5,8,-1,-8,7,-5,10,3,7,8,1,-2,8,-5,5,9,6,7,-10,-6,-4,-6,-7,10,2,10,2,4,-1,10,10,-5,-7,-2,9,5,-8,-8,10,3,-5,-7,2,8,-10,-1,-6,-7,-1,1,8,3,-7,-5,10,2,10,2,-3,-7,-7,-5,5,7,2,7,-3,10,-3,8,-4,9,-10,-3,-9,5,-9,10,-4,-1,4,10,2,7,6,1,6,1,-10,10,-7,9,7,1,8,-10,3,10,-2,1,4,10,-1,-9,-7,2,4,-1,3,-4,7,-3,-8,4,-2,9,-8,-8,-10,-1,4,5,7,10,-10,-10,10,7,-4,7,-7,-2,5,-5,-6,6,-2,-1,6,10,8], dtype = "uint8")#candidate|3587|(288,)|const|uint8
call_3586 = relay.TupleGetItem(func_33_call(relay.reshape(const_3587.astype('uint8'), [12, 12, 2]), relay.reshape(const_3587.astype('uint8'), [12, 12, 2]), ), 0)
call_3588 = relay.TupleGetItem(func_37_call(relay.reshape(const_3587.astype('uint8'), [12, 12, 2]), relay.reshape(const_3587.astype('uint8'), [12, 12, 2]), ), 0)
output = relay.Tuple([call_3571,call_3586,const_3587,])
output2 = relay.Tuple([call_3572,call_3588,const_3587,])
func_3595 = relay.Function([], output)
mod['func_3595'] = func_3595
mod = relay.transform.InferType()(mod)
mutated_mod['func_3595'] = func_3595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3595_call = mutated_mod.get_global_var('func_3595')
call_3596 = func_3595_call()
output = call_3596
func_3597 = relay.Function([], output)
mutated_mod['func_3597'] = func_3597
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3637 = relay.var("var_3637", dtype = "bool", shape = (7, 16, 10))#candidate|3637|(7, 16, 10)|var|bool
var_3638 = relay.var("var_3638", dtype = "bool", shape = (7, 16, 10))#candidate|3638|(7, 16, 10)|var|bool
bop_3639 = relay.logical_or(var_3637.astype('bool'), relay.reshape(var_3638.astype('bool'), relay.shape_of(var_3637))) # shape=(7, 16, 10)
output = bop_3639
output2 = bop_3639
func_3645 = relay.Function([var_3637,var_3638,], output)
mod['func_3645'] = func_3645
mod = relay.transform.InferType()(mod)
mutated_mod['func_3645'] = func_3645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3645_call = mutated_mod.get_global_var('func_3645')
var_3647 = relay.var("var_3647", dtype = "bool", shape = (7, 16, 10))#candidate|3647|(7, 16, 10)|var|bool
var_3648 = relay.var("var_3648", dtype = "bool", shape = (7, 16, 10))#candidate|3648|(7, 16, 10)|var|bool
call_3646 = func_3645_call(var_3647,var_3648,)
output = call_3646
func_3649 = relay.Function([var_3647,var_3648,], output)
mutated_mod['func_3649'] = func_3649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1179_call = mod.get_global_var('func_1179')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_3664 = func_1179_call()
call_3665 = func_1179_call()
func_926_call = mod.get_global_var('func_926')
func_929_call = mutated_mod.get_global_var('func_929')
var_3673 = relay.var("var_3673", dtype = "float32", shape = (1540,))#candidate|3673|(1540,)|var|float32
call_3672 = relay.TupleGetItem(func_926_call(relay.reshape(var_3673.astype('float32'), [1540,])), 2)
call_3674 = relay.TupleGetItem(func_929_call(relay.reshape(var_3673.astype('float32'), [1540,])), 2)
uop_3675 = relay.cos(call_3672.astype('float32')) # shape=(10, 14, 11)
uop_3677 = relay.cos(call_3674.astype('float32')) # shape=(10, 14, 11)
bop_3679 = relay.mod(call_3664.astype('float64'), var_3673.astype('float64')) # shape=(4, 9, 1540)
bop_3682 = relay.mod(call_3665.astype('float64'), var_3673.astype('float64')) # shape=(4, 9, 1540)
func_3367_call = mod.get_global_var('func_3367')
func_3370_call = mutated_mod.get_global_var('func_3370')
var_3691 = relay.var("var_3691", dtype = "int8", shape = (10368,))#candidate|3691|(10368,)|var|int8
call_3690 = relay.TupleGetItem(func_3367_call(relay.reshape(var_3691.astype('int8'), [10368,])), 4)
call_3692 = relay.TupleGetItem(func_3370_call(relay.reshape(var_3691.astype('int8'), [10368,])), 4)
func_514_call = mod.get_global_var('func_514')
func_515_call = mutated_mod.get_global_var('func_515')
call_3737 = func_514_call()
call_3738 = func_514_call()
output = relay.Tuple([uop_3675,bop_3679,call_3690,var_3691,call_3737,])
output2 = relay.Tuple([uop_3677,bop_3682,call_3692,var_3691,call_3738,])
func_3742 = relay.Function([var_3673,var_3691,], output)
mod['func_3742'] = func_3742
mod = relay.transform.InferType()(mod)
mutated_mod['func_3742'] = func_3742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3742_call = mutated_mod.get_global_var('func_3742')
var_3744 = relay.var("var_3744", dtype = "float32", shape = (1540,))#candidate|3744|(1540,)|var|float32
var_3745 = relay.var("var_3745", dtype = "int8", shape = (10368,))#candidate|3745|(10368,)|var|int8
call_3743 = func_3742_call(var_3744,var_3745,)
output = call_3743
func_3746 = relay.Function([var_3744,var_3745,], output)
mutated_mod['func_3746'] = func_3746
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3783 = relay.const(-6.370227, dtype = "float64")#candidate|3783|()|const|float64
var_3784 = relay.var("var_3784", dtype = "float64", shape = (16, 1, 10))#candidate|3784|(16, 1, 10)|var|float64
bop_3785 = relay.not_equal(const_3783.astype('bool'), var_3784.astype('bool')) # shape=(16, 1, 10)
func_3645_call = mod.get_global_var('func_3645')
func_3649_call = mutated_mod.get_global_var('func_3649')
const_3789 = relay.const([True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,True], dtype = "bool")#candidate|3789|(1120,)|const|bool
call_3788 = func_3645_call(relay.reshape(const_3789.astype('bool'), [7, 16, 10]), relay.reshape(const_3789.astype('bool'), [7, 16, 10]), )
call_3790 = func_3645_call(relay.reshape(const_3789.astype('bool'), [7, 16, 10]), relay.reshape(const_3789.astype('bool'), [7, 16, 10]), )
func_2445_call = mod.get_global_var('func_2445')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_3801 = func_2445_call()
call_3802 = func_2445_call()
func_110_call = mod.get_global_var('func_110')
func_113_call = mutated_mod.get_global_var('func_113')
const_3804 = relay.const([-3.008805,0.958398,-0.023523,-8.201448,1.564120,2.918367,3.866282,3.053051,-4.778414,-4.115892,-9.265287,-4.952942,2.392722,-2.225766,-8.768900,7.509797,-1.646419,-4.161035,7.266018,2.432588,3.155751,-9.835338,2.747056,-7.337228,7.150097,-6.337855,-6.451271,-5.651001,-2.484821,-3.871408,2.130356,6.893623,-0.940299,-2.820205,4.644715,3.832651,2.859929,0.225885,4.312947,-7.247909,-4.708880,7.741607,4.372690,0.871854,-4.296950,-6.903636,9.533641,5.112384,-4.345134,5.949510,5.020261,-7.553592,-6.365600,2.203953,1.417276,-7.261557,4.830306,-7.722808,0.047614,-5.115362,-5.870455,2.365602,-8.453628,7.258807,3.486507,-5.949105,2.305410,4.696673,0.599330,-9.319557,-8.038045,-9.896410,-9.651510,-8.812482,-8.477817,4.513761,7.131799,-3.435228,6.886782,-5.601436], dtype = "float32")#candidate|3804|(80,)|const|float32
var_3805 = relay.var("var_3805", dtype = "uint8", shape = (144, 2))#candidate|3805|(144, 2)|var|uint8
call_3803 = relay.TupleGetItem(func_110_call(relay.reshape(const_3804.astype('float32'), [4, 4, 5]), relay.reshape(var_3805.astype('uint8'), [288,]), ), 1)
call_3806 = relay.TupleGetItem(func_113_call(relay.reshape(const_3804.astype('float32'), [4, 4, 5]), relay.reshape(var_3805.astype('uint8'), [288,]), ), 1)
output = relay.Tuple([bop_3785,call_3788,const_3789,call_3801,call_3803,const_3804,var_3805,])
output2 = relay.Tuple([bop_3785,call_3790,const_3789,call_3802,call_3806,const_3804,var_3805,])
func_3807 = relay.Function([var_3784,var_3805,], output)
mod['func_3807'] = func_3807
mod = relay.transform.InferType()(mod)
var_3808 = relay.var("var_3808", dtype = "float64", shape = (16, 1, 10))#candidate|3808|(16, 1, 10)|var|float64
var_3809 = relay.var("var_3809", dtype = "uint8", shape = (144, 2))#candidate|3809|(144, 2)|var|uint8
output = func_3807(var_3808,var_3809,)
func_3810 = relay.Function([var_3808,var_3809,], output)
mutated_mod['func_3810'] = func_3810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2108_call = mod.get_global_var('func_2108')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_3824 = relay.TupleGetItem(func_2108_call(), 0)
call_3825 = relay.TupleGetItem(func_2110_call(), 0)
func_1100_call = mod.get_global_var('func_1100')
func_1103_call = mutated_mod.get_global_var('func_1103')
const_3846 = relay.const([[-1.149449,5.692825,-8.862598,7.145034,-5.222180,2.550401,2.298465,0.695579,9.406786,5.034673,9.777053,-8.205818,8.596342,-5.906537,-6.207477,7.201011,-8.354354,1.718037,-3.835880,-4.167652,0.103782,8.266400,8.675883,0.755767,3.024581,4.832427,-8.163208,8.230582,-2.440025,4.985291,3.686423,0.918487,7.528468,-7.773769,9.429766,-4.758065,-1.370508,-6.159174,-4.931079,-6.154221,-8.444348,-6.712126,5.729907,-0.965344,0.391652,-8.093138,-9.622060,9.174337,8.315087,7.688704,-5.235672,1.740106,-5.005198,-6.731048,0.963665,-6.992508,6.805883,-8.328154,-6.191880,-2.705483,-1.321739,-3.283033,-1.771127,1.136816,1.315530,-3.068137],[-4.683278,8.773543,2.860250,-1.969548,-6.943179,-3.404829,8.062126,3.725650,-8.228757,-3.489794,-4.557427,9.314369,-7.793065,-1.657215,-1.476396,1.133501,3.622801,9.225414,-7.234333,0.456533,-1.901348,-4.802420,9.659916,-7.527747,4.231561,-6.512743,3.603580,-0.363861,-5.022400,-0.134928,-5.747642,-7.907029,-0.718030,-3.532412,4.796330,1.314638,-2.960380,1.023676,4.169419,6.977805,-3.642105,1.504919,1.538403,7.714027,-3.960681,-6.381868,9.733610,-1.900687,-4.624813,3.436354,6.136473,-5.102251,-3.138960,2.242687,9.750254,5.482536,-6.062835,7.457311,-2.437631,-1.159395,-4.849507,9.197977,5.595853,6.123441,0.095013,1.067668],[-0.286415,-8.411462,6.802251,-1.091565,-1.357371,7.992656,-2.839786,-3.888943,9.935183,-6.857859,-3.877870,-4.576371,0.404229,5.898076,-6.315829,9.737836,-9.930988,4.538103,9.366722,-4.965749,1.813595,4.025235,2.492023,3.524053,-1.058975,-6.725326,6.964404,-3.357812,6.087094,5.181907,-9.696232,-3.133084,-9.105670,-8.144431,4.919456,8.789440,-1.939011,9.343215,8.212789,4.207853,-7.866588,-6.762832,-8.800686,-6.996287,-0.783075,9.558133,0.781913,-7.062361,3.209618,8.099997,7.222800,-1.080604,2.056004,0.913390,-5.767823,-8.245601,7.692351,-8.837366,9.368457,5.049798,2.303664,-5.031655,-8.361005,-0.986837,-5.662738,-6.800431],[5.294482,6.510641,-3.652651,5.904333,0.835724,5.938420,-7.320838,-8.526193,5.046069,1.870751,-5.681997,9.801525,-5.037143,9.919834,8.703393,7.107761,-0.408223,-2.878327,4.774707,3.574992,0.224258,5.614871,-4.902904,-7.755316,7.652297,-9.725513,1.903904,-6.382796,-7.679184,-8.230837,-5.502840,-0.137172,0.437558,8.673423,-4.954448,9.294970,-8.348607,1.368267,2.794092,-3.498382,3.917474,-3.604347,-3.891092,7.921857,-1.640679,-6.241836,6.329437,9.813687,1.469969,5.563709,6.074048,-6.502164,-4.740638,2.222206,3.558837,-1.036399,-2.358425,4.302116,-2.591936,9.962517,4.858586,9.250207,-5.592238,5.839903,9.524449,8.149527],[6.443162,-7.735635,9.134235,4.130884,1.619386,-5.471157,5.107602,-8.034742,-9.802426,-7.865460,-5.329730,-2.328457,8.040977,-0.720556,-7.243275,8.247814,1.399028,4.062075,3.295262,8.727299,3.618254,6.040775,-9.091628,-5.898262,3.461202,-6.460738,-5.540800,3.774852,-0.483858,-4.465612,3.007088,-8.872622,-2.419959,-2.391069,1.255132,-8.975663,1.277775,6.404588,-8.415657,-6.149498,-5.839650,2.833721,0.593518,-7.649443,-1.010365,-2.424679,2.016739,4.270848,9.194426,0.637364,1.765751,7.487852,7.244866,-6.505811,-6.586855,-0.445900,5.607727,7.755993,-0.722715,-6.834504,-2.979315,-6.463451,-2.295416,1.832118,7.157055,-1.438064],[1.765569,9.281543,-0.130505,-7.853601,-5.855590,8.720409,-2.943395,-8.666004,4.049847,2.211682,-5.314208,4.688505,4.001161,-1.456114,5.117569,-3.429790,-8.697773,-8.889653,0.995869,5.317760,8.895569,-4.586385,3.572661,-9.617483,8.285433,-1.477079,4.622437,-4.944576,1.741783,-6.116430,9.554877,3.050171,-9.630817,-3.244031,-0.548208,-8.957365,6.652856,7.715317,2.509592,4.061763,4.895242,-0.468981,4.069540,-2.498616,7.329301,1.659581,7.499628,-3.379697,-5.996234,2.759139,-8.697757,-7.249686,-3.168036,-0.326909,5.894713,8.107529,-5.269546,-2.710154,-1.176044,-4.531427,9.980457,0.509999,-0.313480,-0.677798,-3.028956,7.044791],[8.878702,-6.453054,7.141508,-5.232936,-1.346448,2.904255,1.663275,-0.382824,-0.467730,-8.991163,7.218489,-1.002834,9.097383,-4.413089,4.874475,4.799865,-4.824539,-9.983380,-1.468126,-7.393535,-7.044819,0.547386,8.372248,-8.088777,-3.682428,7.955340,-1.052654,2.425928,0.677180,8.084058,7.968217,0.753932,3.984916,5.573060,-1.542086,-2.333328,-9.211471,7.505860,-8.998455,2.236788,-1.543668,-0.758862,1.162229,-8.754161,0.549005,6.734339,-5.515156,-0.582355,-3.071257,-7.559343,-1.558235,-4.789217,-6.928706,-4.493926,2.242145,-1.685856,8.537890,-3.685773,-4.636635,8.630438,-4.629816,0.499109,0.992413,-8.251296,0.819139,1.255884],[-2.895843,-9.046522,4.534103,7.313621,7.882806,-0.665704,-2.075088,7.326013,9.598762,-0.311762,0.012552,3.005308,-7.982379,-9.540999,-5.423745,8.241693,7.457747,1.523424,-9.115377,9.115246,-5.145470,-5.267119,-5.929489,-2.204853,-9.295198,-7.106380,-1.279980,8.813982,7.988697,-0.710991,9.075165,-4.817766,-2.095783,4.395007,-4.925989,-1.125096,-7.637906,8.563379,-6.022977,-5.525287,4.353986,-7.183465,-9.327438,-3.457504,0.055985,3.399618,-7.165851,-9.775178,-5.557608,9.983103,-7.693558,7.774093,4.079125,-7.173972,-2.042962,-8.964374,8.382680,8.036667,-5.953481,7.051694,2.411983,-0.296387,1.973479,-2.213328,-6.226020,-8.624456],[0.763149,6.637180,4.824586,-3.512078,2.079494,9.893047,1.516194,-4.281021,-7.211794,0.612154,4.429050,1.777423,-0.840172,-1.664045,8.764090,-2.230970,-2.586764,7.390157,3.462930,-1.713815,1.210177,0.663840,-2.510846,-4.353109,7.828985,-5.610891,-7.592203,4.144667,5.632227,6.585794,3.246688,7.279656,-4.814937,7.733167,-3.640760,-6.218318,8.144196,-7.695504,3.556305,-0.675944,0.349023,4.752455,-0.342140,-2.713135,-5.142940,-4.818270,0.856073,-2.314238,0.792028,8.784946,9.908409,6.280390,3.854097,-1.145742,-1.371768,-1.918491,-3.082726,0.872482,-5.239037,-2.776608,-8.661651,-3.050433,4.183101,3.824181,-7.434134,-5.484922],[-4.505698,-4.938002,-0.095867,-6.257919,2.668276,-4.569782,9.820852,-4.003360,6.900481,-1.329843,-3.571058,-2.742769,1.729049,-1.916192,-2.596735,8.545551,-4.128841,9.127439,6.047498,7.488302,-1.684896,-5.827380,-7.599318,4.881920,7.844960,5.398970,0.874633,4.666380,0.981654,-9.669705,8.070871,-7.838655,-1.371861,-8.235054,6.895343,-0.691192,7.266419,5.653024,-0.901445,0.400850,7.829777,5.975202,-7.086202,6.184787,-2.374829,-9.638731,-7.213959,3.113877,-2.185198,-5.417648,0.290499,4.190767,1.915867,-8.358339,5.754718,9.388692,-2.753027,8.021922,-8.351908,-0.220455,5.977086,-4.670104,4.698499,-5.102649,0.347895,-2.959200],[0.578639,3.924323,-3.892027,-7.255249,2.324236,-1.841732,-0.119532,3.610313,7.973019,8.728596,-5.797774,-7.126295,3.109395,2.575763,2.136133,-2.884791,9.130718,8.705281,9.663069,0.221340,0.123418,4.324249,-9.178301,-6.591185,-1.207789,-9.795215,6.024861,7.887324,1.823142,1.906704,-5.109590,3.215768,1.790668,5.729124,5.080382,-2.364990,0.566279,-8.869237,-8.582705,7.480443,5.932457,0.741336,-4.328364,5.584421,9.705267,-6.950749,-3.124478,4.630964,-1.614988,6.476569,0.160173,-0.098823,4.049360,-1.682502,-3.905629,-2.835901,3.524911,-6.557703,-1.919013,2.901145,8.133136,5.056055,-0.158711,5.942282,-9.995717,-6.506440],[-8.883604,-8.758029,3.714743,2.145249,-2.191945,5.036013,9.564463,1.247348,-7.073048,4.240531,-9.264789,4.739266,7.157338,4.144067,6.210563,-0.134170,-8.024948,7.932358,3.552322,8.088621,2.126054,-5.699549,9.606291,-5.272741,-8.073907,8.425696,9.516337,8.033390,1.455306,-7.315237,-6.311986,9.631971,0.190188,2.248775,2.770982,-7.340244,7.667808,-6.527645,-3.054691,-4.520286,-6.639478,5.373422,4.123770,4.401607,6.919180,6.691258,-6.137739,-7.459758,-1.122396,-1.513537,1.295410,-7.862032,7.706940,6.834190,9.604430,3.559559,3.933190,8.388180,1.354677,6.696528,-9.064562,2.812442,7.017784,-7.462414,6.680258,-9.753256]], dtype = "float32")#candidate|3846|(12, 66)|const|float32
call_3845 = relay.TupleGetItem(func_1100_call(relay.reshape(const_3846.astype('float32'), [8, 11, 9])), 0)
call_3847 = relay.TupleGetItem(func_1103_call(relay.reshape(const_3846.astype('float32'), [8, 11, 9])), 0)
uop_3850 = relay.sin(const_3846.astype('float64')) # shape=(12, 66)
output = relay.Tuple([call_3824,call_3845,uop_3850,])
output2 = relay.Tuple([call_3825,call_3847,uop_3850,])
func_3863 = relay.Function([], output)
mod['func_3863'] = func_3863
mod = relay.transform.InferType()(mod)
mutated_mod['func_3863'] = func_3863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3863_call = mutated_mod.get_global_var('func_3863')
call_3864 = func_3863_call()
output = call_3864
func_3865 = relay.Function([], output)
mutated_mod['func_3865'] = func_3865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3523_call = mod.get_global_var('func_3523')
func_3524_call = mutated_mod.get_global_var('func_3524')
call_3868 = func_3523_call()
call_3869 = func_3523_call()
func_33_call = mod.get_global_var('func_33')
func_37_call = mutated_mod.get_global_var('func_37')
var_3890 = relay.var("var_3890", dtype = "uint8", shape = (288,))#candidate|3890|(288,)|var|uint8
call_3889 = relay.TupleGetItem(func_33_call(relay.reshape(var_3890.astype('uint8'), [12, 12, 2]), relay.reshape(var_3890.astype('uint8'), [12, 12, 2]), ), 0)
call_3891 = relay.TupleGetItem(func_37_call(relay.reshape(var_3890.astype('uint8'), [12, 12, 2]), relay.reshape(var_3890.astype('uint8'), [12, 12, 2]), ), 0)
output = relay.Tuple([call_3868,call_3889,var_3890,])
output2 = relay.Tuple([call_3869,call_3891,var_3890,])
func_3893 = relay.Function([var_3890,], output)
mod['func_3893'] = func_3893
mod = relay.transform.InferType()(mod)
var_3894 = relay.var("var_3894", dtype = "uint8", shape = (288,))#candidate|3894|(288,)|var|uint8
output = func_3893(var_3894)
func_3895 = relay.Function([var_3894], output)
mutated_mod['func_3895'] = func_3895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2344_call = mod.get_global_var('func_2344')
func_2345_call = mutated_mod.get_global_var('func_2345')
call_3919 = relay.TupleGetItem(func_2344_call(), 0)
call_3920 = relay.TupleGetItem(func_2345_call(), 0)
output = relay.Tuple([call_3919,])
output2 = relay.Tuple([call_3920,])
func_3953 = relay.Function([], output)
mod['func_3953'] = func_3953
mod = relay.transform.InferType()(mod)
mutated_mod['func_3953'] = func_3953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3953_call = mutated_mod.get_global_var('func_3953')
call_3954 = func_3953_call()
output = call_3954
func_3955 = relay.Function([], output)
mutated_mod['func_3955'] = func_3955
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3997 = relay.var("var_3997", dtype = "float64", shape = (14, 10, 11))#candidate|3997|(14, 10, 11)|var|float64
uop_3998 = relay.log(var_3997.astype('float64')) # shape=(14, 10, 11)
func_3807_call = mod.get_global_var('func_3807')
func_3810_call = mutated_mod.get_global_var('func_3810')
const_4001 = relay.const([[-0.185740,-5.727063],[-5.594757,-3.998195],[0.002624,5.195243],[4.879285,1.451666],[-6.005224,0.799465],[8.543119,-4.928970],[5.497362,1.819043],[4.344667,-1.225521],[-9.368111,-8.695066],[-3.996294,6.682211],[9.488070,1.617784],[7.873391,-6.491397],[2.740530,-7.216722],[-5.348931,7.470483],[-6.047795,-7.619398],[-1.447786,8.921352],[0.221535,8.764483],[4.516549,-2.252590],[-5.447380,7.969031],[-0.082532,9.083205],[-7.699926,8.183028],[-7.802235,-1.467267],[0.444625,6.462367],[3.733153,-5.178521],[-2.726944,-7.753786],[1.515345,-6.567624],[9.234829,7.509705],[3.211495,0.039033],[-0.287901,2.055739],[-8.697197,0.150871],[-4.431609,4.904336],[-4.592746,-3.871680],[8.544029,-9.146727],[2.463781,-9.754776],[-8.142289,1.626004],[-4.926296,8.603871],[3.320471,-9.437440],[-6.820843,1.718660],[-2.295539,-3.489742],[6.921941,3.130712],[-8.415707,7.691453],[-9.900667,-6.343266],[1.291322,-3.383164],[-3.183650,2.719167],[-4.403375,9.236115],[5.984407,1.180336],[7.482272,-2.744166],[2.975616,-1.100982],[1.637316,7.150136],[4.021869,2.994966],[7.515542,5.534864],[4.598692,5.074206],[-3.724147,3.354223],[-5.039073,0.941014],[-2.771038,-0.788003],[6.598271,2.517828],[-0.202020,-8.678830],[-1.503979,-2.391557],[9.358019,-2.360494],[-9.749585,3.526220],[-3.835925,1.506352],[2.338196,8.453236],[-9.388935,9.854495],[-0.256360,1.636694],[-1.533780,-4.657443],[1.349402,-4.829876],[-1.148974,5.094384],[0.527325,6.894558],[6.945040,-9.012220],[9.954861,3.828113],[7.999730,7.507698],[8.556202,-7.236128],[-0.131252,1.686027],[1.471794,7.415515],[-5.972963,0.787221],[4.099517,7.496842],[0.850877,4.776594],[1.183587,-9.878424],[-1.631619,-3.876733],[-8.064604,4.818274]], dtype = "float64")#candidate|4001|(80, 2)|const|float64
var_4002 = relay.var("var_4002", dtype = "uint8", shape = (2, 144))#candidate|4002|(2, 144)|var|uint8
call_4000 = relay.TupleGetItem(func_3807_call(relay.reshape(const_4001.astype('float64'), [16, 1, 10]), relay.reshape(var_4002.astype('uint8'), [144, 2]), ), 3)
call_4003 = relay.TupleGetItem(func_3810_call(relay.reshape(const_4001.astype('float64'), [16, 1, 10]), relay.reshape(var_4002.astype('uint8'), [144, 2]), ), 3)
bop_4011 = relay.minimum(call_4000.astype('int64'), relay.reshape(var_3997.astype('int64'), relay.shape_of(call_4000))) # shape=(7, 220)
bop_4014 = relay.minimum(call_4003.astype('int64'), relay.reshape(var_3997.astype('int64'), relay.shape_of(call_4003))) # shape=(7, 220)
output = relay.Tuple([uop_3998,const_4001,var_4002,bop_4011,])
output2 = relay.Tuple([uop_3998,const_4001,var_4002,bop_4014,])
func_4020 = relay.Function([var_3997,var_4002,], output)
mod['func_4020'] = func_4020
mod = relay.transform.InferType()(mod)
mutated_mod['func_4020'] = func_4020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4020_call = mutated_mod.get_global_var('func_4020')
var_4022 = relay.var("var_4022", dtype = "float64", shape = (14, 10, 11))#candidate|4022|(14, 10, 11)|var|float64
var_4023 = relay.var("var_4023", dtype = "uint8", shape = (2, 144))#candidate|4023|(2, 144)|var|uint8
call_4021 = func_4020_call(var_4022,var_4023,)
output = call_4021
func_4024 = relay.Function([var_4022,var_4023,], output)
mutated_mod['func_4024'] = func_4024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2699_call = mutated_mod.get_global_var('func_2699')
call_4082 = relay.TupleGetItem(func_2698_call(), 0)
call_4083 = relay.TupleGetItem(func_2699_call(), 0)
const_4100 = relay.const([[[7.323498,2.967971,-1.568008,4.711181,2.825970],[-6.953394,-5.013417,6.405758,9.557653,-1.824298],[6.318212,3.410726,6.796520,2.380450,-0.426538],[9.364077,-2.009719,-9.505437,-9.319736,-6.400913],[-5.129866,6.524229,-2.419714,-0.712526,-1.005772],[-8.002016,6.993972,-7.931601,1.011306,0.544055],[6.589427,6.681128,2.982436,-8.519343,0.362669],[-7.855637,2.746551,-1.509545,-6.146040,1.477099],[-9.220988,-9.302000,2.834852,-6.355460,-0.821857]],[[5.340004,-5.854524,-6.241134,-4.789219,-5.773285],[7.525941,9.582848,-2.278927,-6.754923,-7.931283],[3.587110,-0.365917,-7.643252,0.157317,-6.969137],[4.137556,8.445736,-1.651350,6.307339,-5.733528],[-9.919129,-4.218020,-8.990760,2.364262,3.592594],[-0.068151,-1.718962,-6.950732,-8.998322,0.760352],[-5.014627,-5.545826,1.626021,2.613785,-2.520500],[-1.878933,3.358808,-2.856952,4.994567,1.168473],[-2.514588,0.332953,-6.249073,5.300700,6.559011]],[[6.865071,1.243912,6.256520,-8.902766,-8.245352],[-1.392901,8.697608,5.516491,2.513992,2.734709],[-3.271365,-2.876585,6.320137,3.270315,-8.557719],[3.157025,-1.812149,6.558919,9.406750,-3.310147],[-1.393846,-2.364751,7.524134,-4.498061,-3.188402],[2.794655,6.200065,2.105370,-1.884045,4.356197],[1.914689,-3.400345,-6.450930,-0.089278,3.374118],[0.801317,1.498622,8.159714,2.077570,-4.547978],[6.839037,-8.454903,0.781436,9.622920,1.351459]],[[-3.261976,-9.055511,-4.183990,4.715757,-8.615679],[-8.212496,-3.347825,-2.100172,-9.955783,6.854520],[3.406633,-3.492305,2.844322,9.129693,2.248090],[-2.594725,-0.485513,-0.541072,9.542705,6.610026],[-4.690184,7.958633,2.898090,-0.274678,2.394120],[-9.784509,-8.074134,2.617793,3.111106,0.373246],[1.872098,-6.789885,-0.807394,-6.745944,-9.876447],[7.774233,8.237260,-0.409068,-3.653401,-5.668177],[-0.807883,3.960042,2.566567,3.036120,1.516446]]], dtype = "float32")#candidate|4100|(4, 9, 5)|const|float32
bop_4101 = relay.maximum(call_4082.astype('uint32'), const_4100.astype('uint32')) # shape=(4, 9, 5)
bop_4104 = relay.maximum(call_4083.astype('uint32'), const_4100.astype('uint32')) # shape=(4, 9, 5)
var_4107 = relay.var("var_4107", dtype = "uint32", shape = (4, 9, 5))#candidate|4107|(4, 9, 5)|var|uint32
bop_4108 = relay.left_shift(bop_4101.astype('uint64'), relay.reshape(var_4107.astype('uint64'), relay.shape_of(bop_4101))) # shape=(4, 9, 5)
bop_4111 = relay.left_shift(bop_4104.astype('uint64'), relay.reshape(var_4107.astype('uint64'), relay.shape_of(bop_4104))) # shape=(4, 9, 5)
output = bop_4108
output2 = bop_4111
func_4124 = relay.Function([var_4107,], output)
mod['func_4124'] = func_4124
mod = relay.transform.InferType()(mod)
mutated_mod['func_4124'] = func_4124
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4125 = relay.var("var_4125", dtype = "uint32", shape = (4, 9, 5))#candidate|4125|(4, 9, 5)|var|uint32
func_4124_call = mutated_mod.get_global_var('func_4124')
call_4126 = func_4124_call(var_4125)
output = call_4126
func_4127 = relay.Function([var_4125], output)
mutated_mod['func_4127'] = func_4127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3523_call = mod.get_global_var('func_3523')
func_3524_call = mutated_mod.get_global_var('func_3524')
call_4221 = func_3523_call()
call_4222 = func_3523_call()
func_1684_call = mod.get_global_var('func_1684')
func_1685_call = mutated_mod.get_global_var('func_1685')
call_4235 = relay.TupleGetItem(func_1684_call(), 0)
call_4236 = relay.TupleGetItem(func_1685_call(), 0)
bop_4244 = relay.multiply(call_4221.astype('int16'), relay.reshape(call_4235.astype('int16'), relay.shape_of(call_4221))) # shape=(4, 9, 1)
bop_4247 = relay.multiply(call_4222.astype('int16'), relay.reshape(call_4236.astype('int16'), relay.shape_of(call_4222))) # shape=(4, 9, 1)
bop_4248 = relay.floor_divide(call_4221.astype('float64'), relay.reshape(call_4235.astype('float64'), relay.shape_of(call_4221))) # shape=(4, 9, 1)
bop_4251 = relay.floor_divide(call_4222.astype('float64'), relay.reshape(call_4236.astype('float64'), relay.shape_of(call_4222))) # shape=(4, 9, 1)
func_1033_call = mod.get_global_var('func_1033')
func_1035_call = mutated_mod.get_global_var('func_1035')
const_4256 = relay.const([-7,-1,8,6,-3,6,8,9,7,5,2,-3,-9,-8,2,-5,-4,4,2,1,2,-7,3,2,-2,1,-5,8,7,-1,5,-9,-4,-10,4,-2,-9,7,-5,-6,-6,-10,1,4,-3,-6,3,-7,10,-3,-1,1,6,-3,-8,9,-6,-6,-6,-5,-5,9,-8,-7,4,-1,9,-6,-1,-5,8,3,-2,10,-9,-10,6,4,-6,2,-5,4,6,-8,-8,4,-8,1,7,-9,-8,1,-8,8,10,-3,-5,-8,8,-8,10,6,10,-7,1,-3,6,-3,-1,-8,2,-5,-2,-8,10,1,-9,-7,4,-7,-1,-6,-6,-1,9,-7,3,-10,4,7,3,3,5,-2,-3,6,9,1,8,-2,3,1,-1,3,8,-1,-8,-2,4,1,-3,1,8,7,4,-6,7,5,6,-5,-7,-5,1,-9,-3,4,9,10,-9,-5,4,-2,-9,-1,2,-1,-4,-6,-8,-10,5,-9,-1,-4,-5,3,-2,-2,-9,-10,-3,-2,9,-10,2,8,-5,-6,5,5,10,-9,3,5,-8,-5,-6,-6,6,2,9,9,-6,-10,-4,-10,5,5,3,-1,5,-10,6,7,-5,2,-10,7,6,6,-2,-2,-6,-6,9,7,-5,8,-4,-3,-6,2,6,2,5,-1,2,6,4,-4,9,-10,10,-4,-5,-5,2,6,5,1,6,8,9,6,6,-8,-5,9,-6,-10,-10,3,2,-9,7,-8,-3,-3,-2,6,2,5,10,-1,-7,-9,-7,10,-2,-8,-10,-4,-3,-5,-7,-7,3,-4,-7,1,-9,-2,5,-6,2,7,-10,-3,7,2,-7,1,-10,-4,2,-3,-8,-7,-7,-1,9,-1,9,4,1,10,-6,1,7,-4,-3,-10,-2,-5,2,-9,3,9,-3,-8,10,6,2,-1,3,10,2,6,-8,2,6,-10,1,-1,-4,-1,-8,2,4,-8,9,-2,9,5,-8,7,10,3,9,-6,-2,9,3,9,-5,4,-7,6,-4,-3,-10,8,-10,-3,-6,3,-5,-9,2,-6,5,10,4,-5,-7,-3,-3,-8,4,3,10,8,-6,6,5,4,9,9,2,-4,-6,-9,-7,-1,8,-1,-10,6,7,4,3,9,6,7,-4,8,-9,-9,5,5,4,4,6,9,-3,5,-3,-9,-4,8,9,-10,-4,-3,10,4,8,9,-1,7,-3,9,-7,-6,7,1,-9,-4,-1,-4,7,-7,8,-8,4,3,8,-3,2,-5,3,-3,-8,-7,-6,-8,-1,-9,-10,-7,2,10,-4,4,2,3,7,8,-4,2,8,-2,-6,-7,8,1,-6,10,5,5,5,-5,-5,8,1,-7,4,9,10,8,-2,8,1,-9,1,-8,-2,-1,-9,4,2,9,3,-6,4,3,-3,5,8,-2,9,-9,4,-6,10,-3,5,6,9,-3,8,-10,-6,6,-10,4,10,-10,3,7,8,-6,1,-1,6,3,9,-4,10,-10,10,-2,9,-5,8,6,2,-8,-3,-1,-4,-2,2,9,-8,4,5,8,-6,6,7,-9,-5,-9,-10,7,7,-9,5,-10,-7,1,-10,3,6,-1,3,-9,1,-5,8,-4,-1,-3,1,1,10,9,3,-8,-3,-9,9,5,5,10,3,-8,7,3,7,-5,6,-6,7,-9,3,9,5,3,-3,1,8,-10,-3,2,-7,-6,2,3,8,-2,-9,6,-4,-5,-3,-2,-8,-6,7,10,7,-8,-9,-2,4,-9,-6,10,5,6,-4,1,-3,2,8,-6,7,6,9,-3,2,8,7,8,3,-2,-6,-8,1,-1,-1,4,2,-4,-7,-4,8,-9,-9,-1,-2,-9,7,9,9,-6,8,-8,1,-1,-10,-9,6,7,4,-10,-10,-7,8,4,-6,8,2,4,10,2,-10,-10,9,-2,5,9,10,-2,-2,6,7,-3,1,-2,3,-1,-7,1,-8,8,4,-7,-5,-7,-5,6,8,-3,-9,10,-3,4,1,5,-8,-3,2,1,10,4,-10,9,2,-4,9,2,4,3,3,5,2,-6,-7,-2,4,4,10,1,-5,2,1,-7,2,-10,-7,6,2,-6,10,8,7,7,5,-9,5,4,5,-10,-1,-10,5,10,10,8,5,4,-8,-7,-1,3,8,-1,-1,10,1,-4,7,-6,9,7,-10,6,-1,2,9,-9,5,2,3,9,3,2,7,-9,2,2,8,-1,-1,3,8,-1,-2,-10,6,-8,-3,10,-8,6,-8,1,6,-5,7,-9,7,-10,2,3,9,6,4,2,9,-2,-8,-3,7,1,5,8,9,-3,8,-8,9,-9,-2,-7,-10,-9,5,1,9,5,4,-8,-3,-6,8,8,-8,4,-1,-2,-1,-7,3,8,2,10,7,10,10,1,-10,7,9,1,-2,8,5,2,7,-4,3,6,-1,-2,-4,10,3,5,9,-1,-10,8,6,5,-10,-2,-10,-5,-7,-3,9,7,1,3,10,2,-4,-5,-2,4,7,7,6,-10,8,-6,-7,10,-6,9,-8,6,-5,4,9,-7,6,8,5,-7,-3,3,-7,-9,7,-1,-3,9,-5,-3,-1,-3,-4,10,-8,6,1,3,-2,5,10,-4,-10,-9,6,-1,2,-5,-4,-10,4,-6,-3,5,1,5,-3,-6,-2,7,-9,-4,-2,-9,-3,-3,-3,10,-9,-3,4,-4,5,-1,7,4,8,-8,6,-9,6,-4,2,-7,10,3,-8,-2,-9,1,-10,-1,-2,9,6,-4,1,-3,3,-5,-2,8,5,4,-2,-9,1,-3,9,-10,1,7,-6,-6,-10,2,9,-3,-2,8,3,8,-7,8,4,-3,6,8,10,-10,5,6,6,10,-8,9,6,-7,10,-1,7,-9,5,6,-3,8,10,4,3,1,-2,3,2,3,7,-6,9,9,5,1,-2,8,5,10,-7,9,3,-7,6,-7,-7,9,-2,-2,-4,7,-4,-9,-8,-8,10,-4,3,-10,-3,-2,-1,8,9,-10,-3,-10,1,-7,-6,4,4,9,-9,-4,7,5,-7,1,1,1,-8,2,-10,-2,3,2,-4,-5,-1,9,5,6,-7,1,10,-3,-5,-2,5,3,10,7,10,10,1,1,-1,9,6,7,6,-6,4,-5,-10,9,6,5,-6,-7,-4,2,-5,-5,-4,7,-10,-8,1,-5,4,2,-10,5,-1,4,9,3,10,7,8,-4,6,-5,7,-9,-6,2,9,-5,-8,-8,-6,4,-6,-1,-4,-3,7,7,-7,-7,-9,-8,-4,9,-3,-2,-5,-6,5,5,10,-2,-3,-1,7,-3,4,-3,6,4,-10,-8,-3,7,-10,9,-10,7,10,-6,-5,-3,4,-9,9,-10,10,-3,-4,10,3,-6,-10,6,10,-7,3,-3,-4,-7,-6,2,-9,-8,3,9,-7,9,-5,-7,9,9,2,10,2,10,8,-3,-7,10,-9,6,-1,3,-9,2,-6,1,10,-5,9,-2,9,4,6,-6,2,-1,6,-10,6,-5,2,10,7,8,-3,5,-6,10,2,7,9,-6,1,1,7,-10,4,-2,-5,1,1,-2,2,8,-7,9,-2,10,-10,-1,-9,-7,-10,5,9,5,-9,-6,-8,-8,-9,10,9,-7,1,7,8,2,-3,3,-3,2,7,5,-2,2,-10,-5,10,-10,-9,-10,3,4,9,9,-8,-3,9,-2,-1,-2,-7,-1,-10,-8,10,-3,10,-10,-7,-10,-2,-1,3,1,8,-6,-4,-3,-8,1,-1,-10,2,-1,-2,3,5,4,9,-1,-3,-3,-4,9,-7,9,-7,-10,-2,7,1,-8,5,-4,1,3,-4,1,3,1,2,-10,10,7,1,6,7,-10,-9,-9,2,4,-8,-6,-7,-3,-9,-10,-2,-1,-1,7,-4,-10,-3,-3,1,-3,-4,-10,-7,2,7,-5,8,-4,-6,9,-7,-10,8,-5,3,-9,-10,8,3,3,1,-1,-7,-8,-5,2,-5,-4,8,-3,-9,7,-3,-7,4,-8,-2,-4,3,2,8,-2,6,8,-5,-4,7,-4,-6,-7,-10,7,-6,-3,-4,7,-8,-7,-4,10,-9,-2,8,5,6,8,10,10,-8,-5,7,-6,-2,1,1,-3,-8,7,2,3,5,-4,7,-3,8,-9,1,-9,-2,6,4,4,-4,-1,2,-4,5,3,5,-7,3,7,-3,4,-1,-7,-10,8,-9,-2,-2,7,6,7,8,-2,10,-5,-10,-6,-1,-5,-3,7,-9,-4,-7,8,3,-3,-1,-9,8,4,5,6,-5,9,3,2,6,5,-7,7,10,10,-6,-10,5,2,-6,-5,1,-10,9,6,-10,-9,6,6,5,-5,4,-7,1,-8,10,-9,7,-5,3,-4,-4,9,-8,-6,-10,-5,-8,5,4,8,9,6,7,4,5,-3,10,1,-9,-4,7,7,-4,5,-8,-3,-10,-2,-8,-9,6,-4,-5,8,-1,7,2,3,6,5,3,-10,-4,-10,-1,-7,-2,-5,5,3,4,6,-3,3,9,3,3,-4,6,-1,-4,5,-1,-5,4,4,9,5,1,1,-3,3,-8,4,5,-2,-8,-7,7,-7,1,2,-5,3,-4,-7,9,-4,-1,10,6,4,-10,4,2,-10,-5,2,9,6,-10,-10,-7,7,-5,-3,-10,6,6,7,1,1,-2,-6,10,4,-8,-8,-1,2,-1,-6,10,1,1,-5,7,-8,1,-10,7,1,-8,-10,-4,-2,5,-8,-1,-2,8,5,-5,4,7,9,6,1,8,1,-4,-9,-3,6,5,-8,-7,-8,-6,-2,-4,8,8,-6,-3,-8,-1,5,-3,10,1,1,-1,-2,-1,9,-3,7,-8,-8,1,-9,-5,8,7,6,-6,-4,5,-1,10,2,-8,-7,-4,-1,-2,-9,5,5,-5,-8,7,7,1,8,9,5,1,-8,-8,1,-9,9,6,-6,6,-2,-9,4,-9,9,2,-9,-7,-7,-8,-7,7,-1,-1,-5,-2,-9,-8,-10,5,8,5,-10,6,9,8,-1,3,9,10,8,-3,-2,10,-9,-1,-2,-4,-1,2,4,-8,-4,-6,3,-8,-7,-8,1,3,2,-7,-2,-9,-3,3,-10,4,-9,8,6,5,-7,6,-10,6,-3,-8,-3,-10,-5,-6,5,8,10,-8,-2,-2,5,-4,7,8,-4,6,1,-6,10,-1,1,9,-7,-8,9,9,9,8,5,7,10,9,-9,10,-8,-2,-2,10,7,10,1,-7,-3,6,1,-7,5,2,2,5,5,-7,-8,8,-9,1,-8,-8,-5,10,6,-7,-5,6,3,7,1,-4,-3,6,3,-9,10,-3,-2,1,4,10,10,-9,9,2,-10,-9,-1,4,-4,4,-10,1,3,1,-1,-7,9,6,1,-10,-4,-1,-5,8,8,5,2,2,-7,3,6,-9,-7,4,2,-9,4,1,7,-9,1,4,2,-9,3,-7,3,5,-2,7,5,-10,8,-8,-9,9,-3,-5,1,3,7,2,-7,-1,-7,3,-6,1,-2,-8,-6,-3,10,-5,4,-4,8,-3,2,-6,-2,-1,3,2,-10,10,-7,-6,-3,-1,-7,-9,10,1,-6,1,9,-8,-3,-10,3,1,-3,1,8,-4,-7,-1,7,-9,1,2,-3,2,5,2,-2,-7,8,10,10,-10,-8,-3,4,-7,3,7,-4,-5,3,-4,-8,1,-3,-3,-6,9,5,9,4,-6,-7,-5,4,-9,-7,3,8,-3,-6,3,9,-5,3,-6,10,-8,-5,-2,-4,9,6,7,7,-4,-6,2,-10,-10,3,-4,7,1,-4,4,-4,9,4,-5,-6,1,-7,-5,-2,-1,-2,9,6,3,3,-8,-10,-8,-3,-3,-1,8,9,-4,-10,-7,2,4,-6,-6,6,-9,-10,-9,9,1,6,7,-5,-8,9,-9,-3,-7,-2,9,10,2,-4,-5,3,-2,-5,8,-3,-7,4,-3,1,-8,-6,10,-5,-6,-5,4,6,9,-7,3,3,-4,8,-6,7,1,-10,-9,-7,-6,5,2,-5,7,8,-6,2,2,7,-8,-9,-10,-1,-4,4,-1,-9,4,-4,10,1,-6,5,-2,3,7,-8,-3,-5,-9,6,-10,3,-8,3,10,3,-8,2,-9,9,-1,2,-7,-8,6,4,-8,7,3,-8,-5,-7,-9,2,-7,5,-7,-1,-4,9,-4,5,2,-2,4,-8,-10,4,5,7,-9,2,-1,-10,-2,8,-6,8,5,-2,9,-9,-4,-8,1,3,-2,-5,7,-10,8,5,-1,1,4,-8,-3,1,2,-8,-7,-2,-7,-1,-4,-1,1,8,8,9,-3,4,1,-3,7,7,-4,4,-6,4,-8,-4,-1,-8,-2,-3,-1,10,4,-9,7,-6,3,-10,5,-10,-1,1,-9,-10,-5,3,-10,1,8,-7,-4,-6,5,7,-2,-2,-5,2,1,2,-7,-3,2,10,-4,5,-2,-6,-8,4,3,-10,8,-2,-6,-6,-1,-7,-2,3,6,5,-10,2,5,-8,3,-9,-10,1,-5,-6,-5,-3,3,-5,5,-6,3,5,-5,8,-10,10,-8,-3,-9,3,-5,-5,2,7,1,6,-1,-2,3,6,-9,-1,-9,-3,-7,-6,-5,-9,10,6,-9,-3,-3,-9,-7,10,-3,-4,-7,-3,-5,7,8,7,-3,-9,-5,-5,9,7,-10,3,-9,-6,-6,-3,7,-1,5,5,2,2,-8,8,-2,-5,-1,8,7,-6,-4,-6,-8,-8,-4,1,-8,-5,-2,4,-7,8,9,-8,1,-9,-5,-8,1,-8,-8,3,3,-10,1,9,-5,6,3,10,9,1,-4,7,-2,2,-3,5,3,9,3,1,-4,-2,8,3,1,1,2,3,-2,-5,2,-3,9,-8,-1,-10,6,4,-2,-3,-10,8,-4,-5,6,3,1,-2,7,3,-10,3,-5,-2,-3,-1,9,2,-2,2,-6,-5,-1,7,10,-8,-3,8,7,4,-7,10,6,-1,-8,6,8,-2,2,-8,1,5,-6,-3,-5,2,4,1,-3,-8,-5,-8,-8,5,2,-2,-9,9,2,-8,-9,-2,-2,2,-5,-10,-5,-5,-9,-2,-4,-3,5,-10,-4,-7,-9,-3,-10,-10,-5,7,-9,4,-3,-8,-3,1,3,-7,10,-9,3,-3,8,9,-4,-5,9,8,6,-10,-6,-8,-4,7,9,4,9,6,-1,-3,1,5,-5,-3,-8,1,6,7,4,-4,2,-6,5,10,-9,10,-3,2,-7,-1,10,1,9,7,-3,-8,-1,8,8,-4,5,7,-9,5,5,-1,6,-2,1,2,-2,-1,-7,-9,-8,-2,-6,-10,9,1,9,-1,-5,4,2,-1,6,-7,2,-8,10,-5,10,-3,1,2,-7,7,-6,9,-8,-4,2,-9,-7,5,8,6,-5,6,-5,6,-1,-6,-5,-7,-7,7,-2,4,-3,1,-8,7,7,9,-4,-8,7,4,-10,7,5,5,-10,9,7,-3,8,-10,7,-9,-6,6,2,7,4,-7,8,6,-2,-9,6,6,6,-9,9,2,6,9,1,-7,-10,1,8,-5,-4,-9,-10,4,-5,9,-2,7,10,-5,-4,5,9,-3,5,7,-2,-8,5,8,-5,-4,-9,-5,9,-1,4,-6,-2,-10,-4,-6,5,-1,-8,-10,8,-1,5,8,-8,4,7,-5,-8,7,3,-10,-9,-1,-2,1,-3,8,8,9,-7,8,-4,4,-9,3,6,10,-6,2,2,-1,6,2,-7,10,5,-9,-10,-8,-6,10,-6,-7,3,-2,5,-9,-1,4,3,4,-3,-8,8,1,9,-7,-4,-7,6,-2,-1,1,-4,-1,-3,7,-10,9,1,3,3,-2,4,4,9,10,-8,1,10,-1,9,-8,-10,-8,-7,10,-2,-7,-4,-6,-8,10,-9,-10,-6,-1,6,3,-6,-9,-5,5,3,-2,2,9,-6,5,-3,4,3,-4,7,-7,10,10,-6,3,-4,8,2,-5,10,4,5,1,-7,7,4,-9,-1,-2,-3,-6,-7,-2,-4,9,-6,-5,3,9,5,-6,-1,3,-3,10,-9,2,3,-7,2,8,1,9,3,7,-5,7,7,1,-5,7,-7,2,-4,4,-6,-4,-10,-4,2,-1,2,6,-9,9,-5,-10,7,10,-10,7,-1,-5,-5,-3,10,-5,-3,-2,-7,-6,9,-7,-5,-10,-5,1,10,-4,4,-4,-3,-7,-2,-9,-1,-5,1,1,-1,3,7,-2,1,-4,5,-1,6,5,8,1,10,-4,-8,-9,3,6,7,9,-4,-2,8,7,3,4,-7,1,-10,8,-9,6,-8,-3,10,2,-4,3,10,-8,4,-2,-8,10,-9,8,7,1,-6,-10,-8,-2,-7,-8,7,-7,9,-5,4,9,-4,-3,-10,-6,-3,-5,-9,7,2,-2,-1,-1,10,-9,1,-2,-2,-8,1,1,2,-7,2,8,9,-4,-1,-1,3,7,-8,3,-4,-4,-6,-1,10,-9,3,-6,-9,1,9,1,1,-10,-5,-1,-3,-5,10,5,-5,-10,-6,-3,1,5,5,4,3,5,4,-8,2,3,-1,-2,7,-7,10,-7,3,1,-7,-3,8,8,-5,10,-10,-9,-3,7,3,-4,3,6,-3,-3,-3,-9,-6,4,1,-7,6,2,-7,1,3,4,7,4,-8,-10,-5,1,-6,-1,8,-10,5,6,-2,-1,4,-3,-5,1,-5,-2,10,10,-10,-4,8,-5,-7,5,9,4,-1,-2,-5,-8,6,9,-7,3,-9,-10,-5,1,7,1,2,-7,2,9,-4,8,-1,9,5,7,-1,2,-1,7,-1,-4,-4,7,-10,-3,-7,8,9,8,-9,9,-4,-7,-6,-5,-3,-1,7,2,6,4,8,1,-9,-1,-6,8,1,-6,-10,-5,9,-9,-4,6,10,-3,-3,-6,-7,-1,-9,-4,-6,9,-1,-10,-10,9,-2,4,-8,-2,3,-5,7,5,5,-6,10,-7,-10,3,6,4,8,1,6,9,1,2,-8,-4,4,5,7,-7,1,-9,-2,8,-2,8,-2,9,-8,1,-8,2,5,8,-1,1,4,10,2,10,5,-3,-4,2,3,-10,8,-5,-9,-7,7,-4,-7,-1,-10,-6,-6,4,1,-3,-9,7,5,2,-6,-6,-8,-8,-3,-5,-7,-10,10,-4,-9,-7,-8,-6,8,-8,-9,-9,-5,4,-3,2,10,2,5,-2,3,-5,-4,5,-2,-6,9,8,2,1,2,7,5,-3,5,9,5,-10,-6,2,-10,-9,-6,1,2,5,-7,-6,-2,-5,4,-7,-7,-1,4,2,-4,10,-9,-9,-5,5,-9,-4,-9,9,10,-6,7,-1,9,-2,4,4,-7,6,-9,3,1,-8,6,-6,7,7,-7,4,2,2,2,-9,7,10,-8,4,2,-10,3,-7,7,-6,-2,4,-8,10,-10,-6,6,-5,-9,-4,4,9,9,10,4,10,-6,-10,1,-4,-10,-8,-8,-3,-3,-8,-10,-4,7,-4,-2,6,1,4,-7,2,1,-4,-4,-6,3,-6,4,-9,-6,1,9,7,5,-1,2,-10,5,3,-2,-8,4,-7,6,9,-10,1,10,-9,-1,-7,-6,-9,-4,10,-1,2,-2,6,-6,-1,9,-8,-2,-4,-9,-10,-2,6,9,-2,4,-8,5,-6,2,7,-9,-10,4,-8,9,-10,4,6,1,6,4,-2,9,-9,-5,-4,-3,-9,-10,-4,2,-9,9,10,7,-5,-9,9,-7,2,-7,8,1,-1,-2,-10,-8,-1,-6,8,8,-4,2,-6,6,-1,-4,-4,-8,-4,9,-7,2,-5,10,2,7,-4,1,-8,-9,9,9,8,10,8,-5,10,2,8,7,9,-7,-2,6,-7,-8,8,-4,5,-8,7,7,-5,-1,10,-4,-3,-3,-1,-7,-3,7,-4,-10,6,1,3,9,6,8,9,8,-3,8,-1,-4,-2,8,3,7,5,-1,8,4,-9,2,6,-1,-1,7,-6,6,2,-5,1,-4,-10,3,-4,-1,-1,4,-3,8,-6,5,6,9,7,-2,-6,3,3,1,2,2,-7,3,-1,-3,6,8,-1,-9,-3,-5,1,-4,-3,-2,8,-10,-2,4,-4,10,-5,3,9,6,-6,10,10,-10,8,-10,5,1,5,-1,-10,-10,-3,-5,-6,2,-4,9,-6,-9,-10,1,8,-3,5,3,-6,4,-5,-10,2,5,6,-9,1,-7,6,-6,-9,-9,-2,-4,5,-10,9,-3,3,6,-10,-4,-5,-3,8,-5,-8,-1,-9,3,-5,4,2,-4,7,-8,4,-9,-2,10,-4,7,1,6,-5,4,1,-1,-7,-10,4,3,-10,9,-7,-2,-3,-4,-6,-6,9,-10,-10,-3,-5,-3,-3,-7,1,6,4,-10,6,-3,4,5,1,-4,-6,8,-10,-10,-9,7,-4,1,-1,-7,7,-9,-1,-6,10,1,-5,-7,4,-1,8,-5,10,-2,-7,10,-1,6,-5,-4,10,-1,6,3,7,5,9,10,5,4,1,5,3,3,4,3,5,-1,3,-3,6,-8,5,8,-9,2,-4,-1,-10,7,4,-8,-5,1,4,8,9,7,-3,-6,5,2,6,-10,-10,2,6,-2,-10,-9,-7,4,-5,2,4,-10,-9,-2,-6,1,9,9,-3,6,-3,8,2,-6,3,-6,-9,9,9,-2,4,-10,-9,8,-1,7,-9,-6,9,9,1,10,-2,-9,-10,5,-6,-7,-5,9,9,-9,-5,3,-6,-5,-8,10,-5,10,-10,9,1,3,1,1,9,2,7,-7,8,2,8,7,-3,-9,3,10,-4,-9,6,8,-1,9,-6,1,-10,-9,6,-2,-4,-1,8,10,-6,-8,-10,-8,-7,-9,3,4,-4,4,8,7,6,8,1,6,8,8,10,-10,-4,7,-10,3,-5,-2,-2,6,10,1,-3,-9,-1,-2,-4,8,-3,7,10,-5,-6,10,9,5,-2,-1,3,8,6,7,-2,7,-3,-7,4,-6,3,8,1,-9,10,-8,9,-9,5,2,2,-5,4,6,5,6,-9,10,-8,3,-1,10,-6,-3,-6,2,-6,3,-8,8,2,-3,-10,10,-4,-5,3,-2,-4,-2,2,8,-1,-10,1,-6,3,3,4,3,-8,10,-4,10,9,-8,-8,-3,-9,-1,10,-3,-7,-8,2,9,-10,9,3,-1,5,-7,10,-5,-10,7,-4,-5,-9,-3,6,8,1,7,-1,8,2,1,3,10,10,7,10,-6,7,-7,-1,9,4,-6,8,1,9,-1,5,10,-1,-1,1,7,7,2,-10,-2,7,-1,3,-5,3,-7,-7,6,-3,8,-6,-1,10,-3,-4,-9,4,-8,-2,-9,8,5,-10,5,10,7,-8,-1,4,3,10,9,-1,-8,9,-10,-3,4,8,9,3,-7,6,1,3,-8,-7,-6,-5,3,-2,-2,-10,8,-8,-9,3,-3,-4,-9,-10,10,5,6,-10,3,-2,9,-3,-9,4,-3,-3,-7,3,-2,4,-2,7,6,-7,-1,4,-10,-7,-8,-8,-9,7,6,2,3,-3,3,-3,9,-8,8,2,-10,6,9,9,4,4,6,-9,9,5,2,-1,-9,-3,4,4,4,2,-5,3,-8,9,-10,6,2,3,1,-7,4,7,7,4,1,-7,8,6,-9,-2,5,10,1,-9,7,3,6,-1,-3,-4,-10,3,-5,4,3,-2,-5,-4,-4,-9,1,-4,5,-1,10,-3,10,-6,4,-6,-7,-5,-1,-9,4,-5,3,3,5,-6,-3,3,4,6,-3,-7,3,3,1,-8,-1,1,10,-1,1,-10,-6,-6,4,10,-8,-8,-7,4,4,-6,-3,-10,-4,-10,8,-7,-4,-7,-9,-8,2,-10,8,10,4,-6,2,3,-8,-10,4,-3,2,-7,-4,10,10,6,1,-7,-1,-5,-2,8,-3,6,-6,6,-8,-1,-7,-10,-10,-2,-2,10,-5,-6,-3,-6,-3,-6,3,8,-2,-4,9,-5,-10,-2,9,6,6,10,6,-10,10,9,5,-3,-4,7,10,-4,10,-3,-7,2,2,-7,-9,9,-10,-5,4,1,6,3,9,-6,-5,-7,-9,10,-2,-10,-1,-2,-7,-7,4,1,7,6,3,-6,-1,3,-3,-1,-9,7,2,-2,-6,-2,-6,-2,10,10,2,-4,-8,-2,9,5,4,7,-1,7,-9,-10,5,-7,-4,10,2,8,10,-10,-5,8,-6,7,5,7,-4,-10,-10,2,3,-9,-6,4,9,9,-8,-3,-4,-4,-6,-5,-7,-7,-2,-3,3,-2,9,8,-10,1,-4,6,7,-10,-10,-1,-10,6,-9,8,10,-2,-6,6,7,-7,4,-2,-1,5,-7,-8,7,10,-2,-10,10,3,4,5,-9,-4,-4,-5,7,8,-6,-1,-10,-1,-1,7,6,-9,-1,2,7,-2,-2,-9,9,-5,4,10,-8,10,-3,-3,9,9,-8,-10,7,-9,-1,2,-4,4,2,3,4,-1,10,-6,-10,7,-6,-5,8,-3,-2,8,-1,-3,-6,-5,10,7,-2,9,6,9,4,6,-10,3,-6,-8,-5,10,-9,-10,-2,9,10,7,-5,-9,-2,10,-5,-4,4,-8,2,8,6,10,-7,-2,-6,-6,-5,9,1,9,-10,9,-4,-3,-6,6,3,7,-5,-10,10,-2,-10,-4,10,-8,-8,-6,-3,-9,-2,-8,2,-8,8,10,1,-5,-4,-5,-6,-5,-10,-9,10,2,6,8,7,7,-3,3,8,8,-1,-6,-5,-3,2,10,3,-5,-1,-9,10,-6,-10,6,1,3,4,-10,2,6,7,-7,7,1,6,8,3,-6,3,4,3,-5,-7,-8,8,5,9,10,-4,3,1,6,5,9,-4,-3,10,-6,5,-8,-9,10,4,3,3,8,9,-7,5,-4,1,-6,9,2,5,7,-4,1,9,6,9,-5,7,5,-10,-9,-8,5,-6,-9,8,6,-5,8,10,-7,7,9,5,-5,3,-7,-8,8,1,4,5,1,-6,7,2,-7,5,-4,8,-5,-3,3,7,5,1,7,-1,8,-7,3,9,2,-6,2,6,-8,-10,-10,10,-4,5,7,-10,-3,-9,10,-8,2,7,-1,-1,-1,8,9,7,9,7,-7,-2,-7,9,-1,-8,-3,6,1,1,-10,3,8,-5,3,-4,10,-3,7,4,8,-10,8,-5,1,1,6,1,8,-3,-7,-3,1,3,7,7,-9,6,-2,8,-8,7,7,-10,-3,5,-7,6,-4,9,4,7,-2,-3,-4,10,-10,-8,2,-1,10,-4,6,-9,8,-2,-4,8,-9,-2,1,-7,-8,9,2,4,6,10,-1,2,7,-4,10,10,-4,-4,-6,-8,-5,-4,-7,-10,-10,6,-1,1,-2,-10,-8,4,5,-8,3,5,3,7,-10,2,9,-1,6,-8,-6,3,-1,9,8,-8,5,9,5,-9,-4,4,1,-6,7,7,2,-1,-6,-10,-10,-5,2,-5,1,1,-7,1,-2,4,10,-5,1,7,6,4,-6,1,5,6,-9,5,3,3,2,-5,9,7,5,9,-3,-9,2,-8,7,-4,10,4,5,1,5,2,-7,5,-4,5,-9,-6,-6,9,8,-10,5,6,-1,9,-4,-1,-3,4,5,5,-6,5,7,3,-9,8,9,6,-10,8,-10,-4,9,8,-7,-6,-6,-3,4,10,3,9,-1,-3,-2,4,4,-4,-8,-7,-7,-8,-5,-10,10,-4,8,-6,10,2,4,5,6,1,2,-6,2,-6,6,-5,5,-1,7,-4,9,-1,1,-9,5,-10,-9,-8,2,-5,9,7,3,7,-3,7,4,-3,3,-4,3,5,-10,-2,-8,-1,8,9,3,-1,6,10,-5,-6,6,-7,2,2,7,-4,-2,-2,-2,2,-8,4,3,3,-7,-10,-7,-6,1,10,-2,4,9,4,8,9,-3,9,6,-7,1,10,4,-6,3,-4,-2,9,-6,-3,3,2,6,1,1,7,-3,9,-10,-2,-5,-8,-5,-8,-3,7,4,9,9,2,-6,-4,-3,-8,-2,-5,-9,3,1,-6,4,-8,3,8,7,-3,-8,-6,2,5,-4,-10,-5,-8,-4,-3,-8,-9,-10,2,-7,-4,2,10,-4,5,-7,-3,-7,1,5,-10,-6,-1,-5,6,8,1,-10,3,5,-1,2,-5,5,2,1,-1,2,5,-7,-1,1,-4,-2,4,-4,10,-1,6,-10,-3,2,-5,-8,-2,-1,1,-7,-4,3,-6,7,4,10,1,10,-8,10,5,-6,-6,-9,3,-3,5,-9,2,9,-1,5,9,-7,-6,-4,6,7,9,8,-2,-8,-6,1,2,-1,-1,6,2,8,-2,-8,-4,-2,-10,4,-1,10,9,5,-3,4,-5,-3,4,4,6,4,-6,3,-7,2,9,-7,-5,-10,1,2,4,2,9,-4,7,-6,-4,-2,4,-1,6,-1,-2,-9,5,-8,7,9,-7,2,8,-10,-5,-3,4,3,-2,1,7,9,-9,3,9,1,-2,2,1,4,2,-8,-1,-8,-5,-9,1,6,-6,-6,-10,3,-2,-4,6,-10,7,-7,-8,3,6,-8,3,6,3,-4,-3,-7,-1,9,-8,8,-8,4,-1,-1,-3,5,3,3,7,8,-6,6,-5,7,-7,-1,-1,3,3,1,5,2,-1,-3,-6,-10,-8,-2,-3,-8,-3,7,3,-5,6,-4,6,-8,-5,-5,3,-3,-2,-4,3,7,-1,1,-6,4,-6,10,6,-9,10,2,-9,-4,2,-8,-2,-3,1,10,-2,-9,3,-8,-9,2,1,3,-10,1,-7,-9,7,-5,-5,6,-7,4,4,3,-9,3,10,9,4,-4,-2,1,2,-6,1,4,6,-2,-2,-4,-7,-2,-4,8,1,-1,4,2,10,-5,-1,10,9,-8,6,-1,-2,1,3,3,1,9,-8,1,9,10,5,7,-4,6,-8,3,9,3,-3,-10,-4,10,-9,9,-9,8,-1,-9,-10,2,-1,6,-9,3,-9,8,1,-5,-1,8,5,3,3,-8,-6,-10,7,8,-7,10,6,-9,-8,-7,1,6,-3,2,10,10,-2,2,6,-7,-2,1,7,-5,6,-3,-9,-3,-7,-10,-2,-2,1,-6,-7,-2,-10,-7,4,-3,5,-7,2,-9,-2,-7,-9,1,-4,-9,-9,-9,5,-7,7,-9,-5,-7,6,-7,4,5,2,5,4,-8,6,-2,-3,-10,-1,5,9,5,9,-6,-6,8,10,6,9,6,1,-6,9,7,9,5,5,3,-2,6,-1,-5,-10,-4,-5,6,-8,-10,-10,-8,10,-9,5,-10,-3,6,3,-5,-4,-3,9,5,-2,6,-4,5,10,-1,-7,2,7,4,-7,4,1,-10,-9,-10,2,4,-2,9,2,5,-3,9,-2,2,3,-3,-7,5,-10,6,-2,-5,9,6,-6,-1,7,10,3,1,10,-10,-8,1,-1,7,7,-10,8,8,-7,4,8,-3,6,7,-9,2,-4,-5,-2,-10,6,7,-6,-9,-3,6,7,-2,-5,-10,6,2,-9,-8,-9,1,-10,9,-3,-8,-1,10,4,-2,1,-3,-6,-10,2,-5,6,-6,6,10,-6,-8,5,-7,-1,9,-3,-10,7,-3,6,2,5,8,-5,-3,-9,10,-8,-4,-9,3,-5,-2,-3,-1,-4,2,-3,3,9,1,-6,5,-1,4,-1,-2,8,-7,9,-9,-3,4,-1,3,2,1,4,-3,2,5,-4,8,-10,-4,-4,-4,6,-2,7,-7,7,9,4,6,-9,9,-7,7,3,8,4,6,-2,-7,2,-9,1,-2,-2,-3,1,-6,1,8,5,-5,10,9,10,10,-9,4,-9,-7,7,3,1,8,5,8,-4,8,-2,3,-2,-5,3,3,6,-2,9,2,-9,4,6,3,-2,-3,10,8,10,3,5,-5,3,5,-5,3,-5,7,6,-3,-10,5,-4,-2,-8,-8,-8,-5,8,-6,-7,6,-6,7,-2,-2,-9,-2,2,7,-10,7,6,10,4,-9,-7,-4,10,6,-2,-4,-7,-1,-4,-1,3,-2,-9,-5,10,-3,2,1,7,-4,8,-9,8,-6,-10,5,-6,-4,-9,8,-6,-8,8,-10,7,-5,4,9,-6,4,-3,-1,4,-4,6,-4,-6,-1,-10,-1,-7,-1,4,2,-7,8,-5,-9,-4,-4,8,1,10,8,2,-8,-8,9,9,4,10,-7,8,-4,10,3,7,10,7,-7,9,-10,-4,-1,-2,10,4,5,-5,6,-8,-3,-6,-10,3,4,5,-9,4,-4,4,8,-3,-1,3,-6,-8,-4,4,-7,-3,8,-6,-9,-6,7,-8,7,-8,-2,8,2,4,2,1,-4,-2,-4,-9,7,5,5,-8,5,-3,-7,-2,8,-4,-6,2,3,4,2,-2,9,2,-3,8,-6,-6,5,3,-5,-6,4,-5,-1,4,-2,-2,-6,-7,-5,-8,10,-8,-1,8,8,9,1,-8,-2,-6,1,-7,2,-7,-1,-2,6,-5,8,4,-7,-7,8,-3,-10,-5,6,-1,8,-7,-2,9,8,-6,7,-2,5,-5,7,-3,6,9,2,2,9,-6,-8,-10,8,5,-7,10,-6,-3,2,1,6,9,9,5,-1,-8,7,-7,5,-2,9,-4,-6,10,-5,-7,-1,8,-8,-8,5,7,-8,-8,-6,-5,2,-10,10,-8,8,-5,-2,9,-7,8,-6,3,3,7,2,4,3,4,-3,8,8,2,-8,1,-1,7,-5,-1,4,8,10,-1,8,-6,-10,6,-10,9,1,-1,-10,-10,-1,-5,-1,-2,-7,-5,8,7,8,7,4,-3,-7,-7,-5,4,-10,-10,2,-3,4,-5,1,-2,7,-8,5,-4,-8,-9,-10,10,2,2,-1,-4,-4,7,2,6,-7,8,6,6,5,-8,8,6,7,5,-2,2,9,3,9,1,-6,9,3,7,-1,-4,4,-9,7,-8,3,6,7,3,1,-3,-5,10,-8,-5,-3,-7,8,-7,-10,-5,-4,6,10,-9,-5,9,-5,-5,5,1,10,4,-4,4,-5,10,2,3,7,-5,2,-2,1,9,1,4,10,1,1,9,-6,5,6,10,-10,6,8,-1,7,-7,-2,10,-10,-5,8,-7,2,2,2,1,-6,-3,7,5,6,10,6,-9,1,-5,7,-1,6,8,5,7,8,-8,-6,7,-9,-9,7,9,-9,4,8,6,9,9,3,7,-8,6,-8,-5,10,-9,-1,4,5,-7,-3,5,6,8,-2,1,-8,3,8,2,-3,6,1,5,7,-9,6,2,7,-1,5,-8,-7,-10,10,-6,6,10,-1,3,8,6,-5,-6,-10,-3,7,9,-4,-2,2,-1,7,4,-6,-5,1,8,2,2,1,9,9,-3,-7,-1,-10,-7,-4,6,-10,-6,-2,8,-10,-10,-8,-8,-6,-9,-3,-4,-5,-1,-4,10,-10,6,5,-8,6,6,6,8,7,9,-10,-5,5,-5,-5,-2,3,8,2,3,-5,-10,6,-5,9,-3,8,-5,5,2,5,6,-2,6,-2,1,-9,-10,-1,8,-10,1,8,-1,-4,-5,-6,6,7,1,-10,-9,-5,6,6,6,-4,2,-2,6,-5,-4,-4,-7,2,-10,-10,3,-10,1,-2,1,-5,1,5,1,10,1,6,5,-5,10,8,1,4,-5,9,4,9,1,-7,-4,-10,3,4,-3,4,4,-9,-9,7,9,10,-9,-3,2,5,-6,-2,10,-8,-3,-8,-4,4,-8,-9,-6,-2,-5,5,4,-5,2,1,1,5,-2,5,-10,1,-7,-6,-9,-7,-5,2,-2,-2,-2,8,-4,1,8,6,-2,-5,-7,-1,-3,-1,-1,-8,9,1,6,-7,2,10,4,7,3,5,5,6,-6,-6,9,-4,-5,2,-2,-4,6,4,10,-6,-5,4,-10,-8,9,-5,-8,-9,-2,6,1,-10,-8,9,-8,-2,7,-3,-8,3,-4,8,-7,-7,-7,5,-5,-4,-1,-10,7,4,-9,3,7,-7,-4,3,1,2,-4,-7,-4,-1,-4,-8,6,7,8,-3,5,7,4,-3,-1,4,-6,4,1,-8,10,-8,-7,-2,-6,-1,-6,4,-10,4,4,7,-6,-1,-10,-4,5,9,-8,7,7,-6,-8,-10,7,-2,-1,-2,-3,3,-2,-6,-8,8,-7,1,7,-4,8,-5,-7,10,7,-4,-7,-6,4,7,-8,-10,-4,-6,8,7,-5,3,-1,-9,-6,-1,-1,-1,8,7,-5,-10,7,9,7,1,10,1,8,-10,-4,-7,-7,-10,-8,-2,5,1,7,7,-8,3,6,-9,-5,-9,1,5,-6,-4,3,7,-7,10,-10,5,9,6,-1,2,-6,-6,8,-7,-6,9,7,7,-4,-6,-6,-2,9,2,5,-8,6,-7,5,1,5,9,3,7,-3,-2,6,-7,6,-4,5,1,6,-8,-2,-10,-6,-10,-7,8,2,10,-8,2,8,4,-8,5,-2,4,-3,-4,7,9,3,-3,-9,-2,2,10,1,-3,8,-4,-4,-6,-5,5,-4,-6,-4,-3,-4,2,10,7,-6,2,-2,-4,-7,1,-1,-3,-3,-6,-8,3,-4,9,7,-9,8,-4,-10,-5,1,6,-4,-8,8,7,-3,-7,3,4,3,2,-5,-4,-5,9,-6,-7,-5,-9,-1,10,-5,2,4,10,7,3,-8,-6,-3,-10,-3,-1,-4,-3,7,10,10,-3,-7,-4,-7,-8,-1,10,1,-4,7,-3,6,-7,-9,4,-8,-6,2,-1,6,-3,-4,-4,3,9,5,-2,-10,-3,-7,-8,6,1,-3,-6,-2,9,-2,-2,1,6,7,-7,8,-6,1,-1,8,-4,4,2,-8,5,4,-4,1,10,-9,-5,-1,1,4,8,4,5,-3,-6,-7,-1,-8,-5,7,9,6,-3,6,8,8,4,-9,1,-7,1,8,7,6,-9,7,9,1,-2,-7,-8,6,8,2,-7,6,5,9,4,-1,-8,-8,-6,8,7,-6,-10,-7,-10,-6,8,-5,8,4,-9,4,5,-4,-2,-7,-6,5,9,-2,3,-6,-2,5,-4,3,-3,-3,-8,1,9,-2,-3,3,-1,9,-5,-6,-5,-8,-9,4,-7,-4,6,-6,3,2,-2,-6,-1,6,1,4,4,-6,-4,-9,-9,-5,-6,10,8,-3,-8,-5,7,7,-5,5,5,-4,-2,-2,-4,6,2,9,-1,-10,5,-7,7,10,7,3,7,-4,10,9,-7,-6,-2,-6,-1,-1,-2,-9,-4,-2,6,-6,-3,-3,-8,-7,-9,1,9,-6,6,9,8,8,8,-7,-7,9,-3,5,7,4,6,-9,7,-7,5,-2,5,6,-3,-10,-6,-2,-3,8,-8,6,-2,-3,2,-3,-8,-9,6,-6,8,9,5,3,-8,-8,5,-2,-10,-7,5,-1,-6,5,8,1,5,2,-3,8,5,-8,9,-1,-7,3,-8,-6,-5,-8,-10,10,1,5,-6,5,-8,-4,-7,8,-3,7,-5,8,1,4,-5,9,6,-1,-9,-6,1,6,6,1,6,3,-8,1,6,-5,10,8,9,8,4,-7,-5,3,8,1,2,5,-4,1,2,1,-9,-7,8,8,-1,-9,9,-8,-7,-1,2,9,2,3,8,-7,-5,-7,4,-7,10,3,-9,6,-9,-5,5,-4,5,-5,3,2,-6,5,6,-7,9,6,9,3,3,7,-1,-6,-10,9,-3,-5,10,1,9,2,5,5,-2,-2,-6,2,1,4,-9,7,4,10,-10,-9,6,9,1,-5,-2,-7,-7,-6,9,10,-2,9,-6,9,-10,7,2,-9,-7,8,-3,-10,6,-9,-7,-2,-5,-5,9,-9,2,5,1,9,-10,9,-5,-2,-6,-7,-1,2,-9,-10,-10,-7,4,-10,-8,3,7,-9,-1,-5,-5,10,1,-3,8,9,2,-2,-10,3,1,-3,-10,-3,7,-7,-10,8,6,2,-5,-2,6,5,-6,3,-6,10,-3,4,10,-2,-8,-2,2,-10,4,3,-8,8,-7,-3,-1,7,-5,4,4,-6,6,9,-1,-2,1,-6,4,-4,7,3,10,2,3,-1,-1,1,6,-3,9,9,-1,-10,9,5,1,1,-10,-9,8,1,-8,7,2,-8,-7,10,3,4,-4,-7,-1,-8,-3,5,6,3,8,-9,-3,-3,5,-10,-5,-2,7,4,10,-8,-9,-6,-9,-3,2,9,-9,6,6,-6,-2,8,8,7,5,2,-8,-9,1,2,-3,9,-3,-8,2,-10,2,6,-1,9,8,-10,-4,-3,-10,-8,-8,-5,-3,10,6,-2,9,8,10,-7,-1,-7,5,-7,7,-10,-6,5,-7,-5,-6,-1,4,8,7,6,-4,10,-3,6,6,-4,-10,-10,-6,10,-3,-9,-10,-4,-4,-4,3,10,3,-9,-2,1,-2,1,-7,1,1,10,-9,-10,-5,1,-10,-8,-7,-2,-10,2,-6,-9,3,-5,-10,-10,7,1,-6,-4,5,9,-6,2,-6,9,7,-4,-8,9,-2,-8,-8,-3,-5,-1,8,4,-3,-2,-1,10,9,-2,-1,-6,1,1,6,6,-2,2,6,-4,10,-7,-6,-3,-9,3,-8,-2,-4,-8,1,-2,10,-3,-7,5,-2,10,-9,5,10,1,-7,-6,-8,-1,-10,-1,6,7,10,3,-6,2,-8,5,-2,-7,-9,-2,-9,7,-8,8,-2,-7,6,-4,3,-8,-2,-10,-1,-5,-9,-1,-10,6,7,-9,-8,1,6,-8,3,9,-3,10,-5,-4,2,1,-4,-7,2,9,-4,-5,6,-9,-3,4,9,-8,1,-9,9,-2,-8,3,-6,-9,5,-1,1,-1,10,8,1,6,-10,-2,4,4,-4,-1,3,1,5,-10,1,9,-7,3,-5,-10,3,-5,-10,10,-10,-4,-8,-1,-4,9,2,-1,9,9,-4,-10,-4,5,-6,6,5,-8,-3,-7,-10,6,-8,-1,2,8,2,4,-5,-8,5,6,3,4,3,-7,-10,4,-2,3,-8,10,1,4,7,6,5,2,5,8,-5,-2,-9,-3,3,5,-6,-9,-10,-2,6,-9,-9,-1,-6,4,-5,8,-5,5,6,-1,-4,1,5,3,1,-2,-4,5,-3,3,7,10,-2,-2,-4,1,3,-5,5,-10,1,-7,7,7,2,6,1,3,-4,2,-8,-7,4,3,-10,-6,-7,10,-8,3,-6,1,-8,3,-1,-7,5,-4,-6,8,10,-10,8,10,-6,-8,-2,2,-3,-10,-9,5,-3,-4,-4,6,8,-10,6,4,2,6,9,4,4,-8,2,-8,-2,3,-5,-9,-3,-9,10,-2,-3,8,6,-8,7,5,9,4,6,-7,-6,-3,-7,9,6,-4,10,5,-6,-8,8,2,-9,-9,6,7,4,3,4,1,-3,-3,8,9,-10,7,-2,-5,5,-5,10,5,4,5,1,-8,-2,-7,8,4,-7,-3,-10,-10,-2,8,-9,-8,-2,-10,1,-7,-8,5,2,-1,-2,8,3,-7,-4,-1,-9,-7,1,3,-3,7,7,-7,-3,10,3,5,5,-2,-10,-6,-1,-1,-8,6,-5,5,5,2,10,-3,-9,8,-4,-5,-5,-3,-3,1,-9,7,10,-7,-5,4,1,6,-8,4,-7,6,1,10,-6,-7,10,10,-7,-8,7,8,1,-6,8,-3,-8,-9,-10,2,2,10,5,-5,-8,7,-6,1,-6,-8,-8,1,2,6,-1,-8,10,-6,-8,9,5,-9,-8,-6,-9,3,5,-5,4,-9,-10,7,-2,6,5,6,-1,8,-9,-8,-1,8,-4,3,2,2,-8,1,5,10,3,9,4,5,-4,-2,3,2,-2,-5,6,6,8,4,3,3,-1,-1,-10,6,9,-10,9,8,-5,-4,10,-7,-7,2,-4,-7,-5,-9,5,10,7,-6,10,-6,7,-7,9,-5,-4,6,10,-4,2,-2,3,10,-2,4,8,-6,-1,-4,-9,-7,-6,5,-6,2,4,-4,-6,9,-9,-9,-5,4,1,4,-6,5,6,7,10,-2,5,-3,10,-10,-5,10,3,-5,3,-4,-10,1,10,-8,9,-7,5,7,4,-6,4,8,-9,4,2,-1,9,-10,1,-1,7,-7,8,10,1,10,4,-5,-2,-7,6,-9,-9,6,-7,2,-5,-8,3,4,6,9,5,-4,-2,-9,8,-5,-7,9,-8,-7,10,-7,-5,-6,6,-2,-9,7,-7,2,-4,-4,-10,4,6,10,-7,8,9,-3,-1,-5,1,-4,8,-4,4,5,1,-1,-1,2,9,9,3,-2,-7,5,-1,-6,6,3,-6,-6,-8,-3,-10,-8,-4,-7,-1,3,6,-5,8,5,-1,-6,9,-3,8,7,-2,7,1,5,2,9,-8,6,8,-2,2,-6,-1,-9,9,-9,10,-7,1,-3,1,-3,-10,7,-2,7,-8,-6,-5,1,10,5,7,1,7,1,7,7,2,-7,2,10,-8,10,-3,9,3,3,7,8,-9,-2,-10,6,-10,8,-7,-1,-7,10,3,3,-5,-6,2,8,2,8,8,5,6,-9,4,-8,2,2,9,-3,-4,7,-4,7,-5,-7,-10,-1,6,7,-10,2,3,9,-1,-6,-3,3,8,-3,-7,-7,3,-3,-8,2,5,9,-9,-2,3,7,1,-3,-2,-5,7,5,-10,2,1,5,7,6,4,-6,5,5,5,-8,-6,-5,-5,-4,1,10,-1,7,-10,-4,2,3,5,-5,8,7,-6,-7,-5,3,-9,9,9,8,1,-6,-3,-2,9,-1,3,-8,-2,-10,-8,-4,-8,-8,9,8,7,-2,-5,1,4,-10,1,5,-5,-2,-8,1,-1,6,-3,9,10,-2,-8,8,6,8,-8,-3,-6,5,5,-3,-2,-6,3,7,-1,-8,-4,10,6,9,10,6,-1,3,6,-2,-5,3,8,-1,1,-9,-10,6,8,2,9,6,-1,-6,5,5,-8,7,-10,-4,-2,9,1,-7,-3,7,-9,2,1,6,7,5,-2,1,5,-5,8,8,-1,10,-6,-6,1,-6,5,10,5,-7,-2,-9,4,1,-9,-5,5,-4,6,5,-7,2,5,6,-9,-7,1,-7,1,1,8,10,-3,2,4,7,-2,-3,-2,5,2,-4,7,2,-9,7,10,9,-4,1,2,-1,-8,9,5,-3,7,2,7,3,-10,3,10,1,7,-5,-1,-3,-1,9,10,3,-7,3,-2,2,-9,-9,-9,6,-4,4,5,6,-2,2,-7,1,-1,-10,3,2,-8,-2,3,4,-8,5,-8,1,-8,-1,-5,10,7,8,3,3,-1,2,-4,1,5,-7,-9,-2,-9,-3,-5,2,-5,3,10,-1,10,5,10,-6,-4,-7,-1,-3,3,-7,-8,-2,9,1,1,10,-7,-5,-3,-1,4,-3,8,5,9,-4,1,10,-3,-9,4,6,-6,-6,2,7,7,10,3,9,-9,9,-8,10,-9,-6,2,-4,-10,7,-10,-9,4,2,-7,1,3,6,8,-3,-8,-2,10,1,8,4,-4,-5,-4,-6,-8,-9,-7,-4,-2,6,7,-2,-5,7,-1,-9,3,3,-1,-8,-8,-3,3,-1,-6,7,-6,2,-2,-3,1,-9,-8,-2,3,-1,9,7,-1,7,7,5,-2,5,6,-8,1,-1,-10,-9,7,6,-4,-7,3,-4,-7,6,-6,5,10,-10,9,-4,-8,-3,-5,-10,4,-5,1,-9,-10,10,-7,-1,8,-2,5,-7,-10,-8,9,-5,-5,-10,-2,5,-6,-2,-9,4,4,-6,1,-4,4,-10,-9,-8,7,-1,8,3,-10,-9,-5,8,-8,-2,8,1,-9,-6,6,-5,5,2,-1,-9,9,3,10,7,6,6,5,-5,-10,3,9,1,-3,7,-9,6,-2,-3,-10,10,-8,-1,6,7,9,6,-9,1,-1,9,-3,-7,6,9,10,4,-8,3,1,1,-4,-9,3,7,8,-3,3,-8,-2,4,6,4,-3,7,-8,5,5,-5,3,2,9,2,7,-8,-7,-5,-2,-9,5,-8,-4,5,6,10,3,1,-9,-4,5,7,6,-6,-8,-3,1,-6,-6,-4,8,-4,-8,-2,9,1,-8,5,10,-4,6,-1,-1,-10,5,-9,-10,3,9,-2,1,-2,4,5,-9,-2,6,-10,8,2,-7,-4,6,-6,-5,3,4,5,3,3,8,-8,7,-9,-9,-6,-6,5,10,-6,2,10,-3,5,6,-9,-1,7,7,3,-1,-4,9,-8,1,-5,1,10,-10,-3,2,1,1,3,7,3,5,4,7,5,6,-2,5,5,6,4,-10,-5,-4,-8,-4,-7,-10,-5,3,-8,1,-7,1,-2,10,7,10,2,10,-2,-2,-5,2,-1,1,-7,9,-9,-6,9,6,5,-8,9,-6,2,4,2,9,-4,-5,3,2,4,2,3,9,-3,4,5,-4,10,6,5,-9,6,-9,8,10,9,-7,-9,2,-5,5,-8,9,-9,4,-10,3,7,-6,3,-10,9,9,-6,-1,7,5,7,5,-8,-9,10,-8,-4,-3,-2,3,10,3,-3,1,2,-5,-9,-2,9,-7,3,-7,2,8,-3,-9,-3,1,7,-7,-7,6,5,2,1,-3,7,-3,-2,-4,4,-7,6,-4,-1,3,-5,3,9,4,-7,6,8,2,2,4,1,-2,1,-1,-9,2,3,2,1,2,2,1,-9,10,2,5,5,-10,5,1,-6,-6,8,-1,-5,-6,-2,8,1,3,2,-7,-7,-5,8,8,3,-3,3,2,8,6,-7,3,2,3,4,-3,9,-5,8,-1,7,-1,-9,-10,-3,8,1,-9,-5,-7,4,-10,-9,-10,-8,7,-6,-10,1,3,-8,-3,-10,2,-7,-4,10,-4,1,-8,-8,6,3,-10,-6,10,3,5,-6,-9,-7,-5,-9,7,-4,8,-2,-7,-2,3,9,-4,-5,-6,-5,7,9,10,-1,-9,4,1,6,2,5,6,9,10,8,-6,-2,4,4,-1,-10,2,-2,1,10,-3,-1,3,-10,3,-9,-10,3,-2,7,2,8,3,-8,7,10,-7,3,-10,-2,-1,-1,2,5,10,1,-9,-7,-10,-7,-5,9,7,-3,-4,-7,6,6,-3,-5,-2,5,9,2,-9,6,-5,7,6,-6,-4,5,-4,-1,-9,9,5,3,-10,-3,3,4,-4,-9,-2,3,1,-8,-7,1,5,9,8,6,-6,-8,6,-10,-4,3,5,1,-3,10,-8,-10,-5,-5,-1,-10,9,10,9,-8,-9,10,-6,-10,10,1,-5,2,-7,4,9,-9,-3,4,6,-6,2,9,-6,8,-2,-5,7,-8,8,6,-5,6,1,1,-3,-4,-2,-2,3,4,9,2,-9,-10,-2,6,1,-7,-3,2,3,10,9,4,4,-7,7,8,-2,3,-7,3,-1,10,7,2,8,-7,-6,6,7,4,3,-2,-10,-8,5,5,-2,-4,7,-10,7,-9,-6,-6,10,-1,-10,7,9,7,7,-4,8,-9,-3,9,4,-5,-7,-7,1,-10,-10,-2,-4,-5,-2,-1,6,-5,-7,-8,-6,-5,-6,-10,10,-9,-6,-1,10,3,-4,4,2,-6,-6,4,-9,-7,-9,1,6,10,-9,-2,7,-2,-10,1,-8,5,-5,-7,5,-9,-10,4,10,-8,4,-9,7,-2,-2,9,3,-3,2,-1,6,1,-10,-10,8,-9,-9,-1,-4,1,7,-3,5,-9,7,-4,-9,9,-10,10,-8,-8,7,-3,-4,6,-6,4,-4,10,2,-6,-9,-10,3,-6,-9,8,-6,9,-5,3,-4,7,-9,-1,3,2,2,2,4,-6,2,10,-3,10,-4,1,10,-7,-5,10,8,1,-5,-5,10,-3,5,2,4,6,-5,-7,-3,3,-7,-5,4,6,10,10,5,4,-9,-6,10,-3,8,-9,-8,-8,-5,1,10,1,-1,10,6,-3,-2,-2,-2,-9,-6,-1,3,9,-4,-7,8,-6,1,-4,-2,6,8,8,2,10,6,-4,3,-8,4,3,5,10,5,-5,-10,1,-10,10,6,1,5,2,-9,-5,6,-4,9,-9,7,-3,6,7,-3,-9,10,3,-5,3,5,-4,8,-6,-1,1,-10,7,8,-3,2,2,-1,-9,-9,-10,-10,9,-2,5,9,-3,10,-4,-3,-9,-8,9,3,-8,10,-9,2,-10,-5,10,-3,-3,-3,9,-6,1,7,-5,-9,5,9,-2,3,5,-9,2,-8,-4,1,-6,-2,-3,10,9,9,9,-9,-10,4,-2,10,6,-10,10,-4,10,-7,4,1,7,1,-9,-6,5,-2,-5,-3,-4,-3,-4,-3,4,-7,9,4,-9,9,-5,5,-7,9,3,4,4,-2,-6,-5,6,9,-2,-9,-9,-7,5,4,-2,3,4,-3,-3,-7,1,-9,5,-2,2,8,-2,-6,8,9,3,-7,7,5,4,-1,3,-2,8,5,-5,-1,-9,-8,-7,9,8,8,4,7,5,-1,-10,7,6,7,-7,2,5,3,4,-3,5,-10,-3,7,5,-6,-2,2,-7,1,1,-7,1,10,9,-10,5,3,6,-7,9,-7,-8,-9,10,-6,3,-9,3,-2,3,7,1,-7,2,-8,-9,2,-4,10,-10,6,10,-8,5,5,1,7,4,8,9,-6,1,-6,10,-10,4,4,1,9,1,5,8,3,-7,-9,-7,9,-3,-4,2,-3,-9,-4,-8,-8,9,-10,-7,-10,-6,-5,3,2,8,1,7,10,-3,-8,-7,10,10,-4,7,-3,2,5,-1,-1,10,-1,-8,-6,-3,-9,-1,-6,-3,1,-4,-2,-2,2,-3,-2,-7,-3,-4,-3,3,9,3,8,6,7,-4,8,5,9,3,2,-4,2,-5,-5,8,-4,-9,-8,-10,7,-3,9,-5,5,-10,7,-3,-2,-5,-7,-2,4,3,-8,-7,8,2,-8,-6,4,-2,-7,-1,5,7,8,5,3,-6,-3,-10,4,8,8,7,-7,-4,-7,-5,-8,6,-6,-8,9,1,-8,2,-2,4,-4,3,-1,8,-9,-10,-9,-3,-7,3,-4,7,7,1,-10,9,-7,5,-9,-6,8,-5,2,2,-8,5,-1,-3,-10,6,-3,-3,-9,-8,1,-7,2,4,10,3,-10,2,-1,-10,1,-10,-2,5,-1,-10,-9,-1,-8,4,2,-6,6,-6,4,7,-3,-2,-1,-6,1,7,2,-2,-5,-8,6,9,-1,8,-10,-3,-3,6,1,8,-10,6,5,4,-6,4,6,3,-8,-5,5,9,-2,-4,1,-6,9,4,-2,3,-9,-8,-10,-4,-2,-7,6,7,-3,10,-4,-4,10,8,-4,-10,10,10,10,10,-5,-3,3,9,-2,1,-7,1,-2,-9,-2,1,-8,-1,9,10,-10,-4,-2,10,-6,-2,-5,2,5,-4,-2,-8,10,-9,-3,-10,2,8,1,-2,9,9,10,-1,-3,-2,2,5,1,8,3,-9,-5,2,4,-10,9,-9,1,2,5,-8,5,-8,7,4,-7,6,-1,8,2,10,-7,10,7,1,7,-10,3,1,-7,2,10,-5,-6,-8,-1], dtype = "int8")#candidate|4256|(10368,)|const|int8
call_4255 = relay.TupleGetItem(func_1033_call(relay.reshape(const_4256.astype('int8'), [4, 9, 288])), 0)
call_4257 = relay.TupleGetItem(func_1035_call(relay.reshape(const_4256.astype('int8'), [4, 9, 288])), 0)
output = relay.Tuple([bop_4244,bop_4248,call_4255,const_4256,])
output2 = relay.Tuple([bop_4247,bop_4251,call_4257,const_4256,])
func_4263 = relay.Function([], output)
mod['func_4263'] = func_4263
mod = relay.transform.InferType()(mod)
mutated_mod['func_4263'] = func_4263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4263_call = mutated_mod.get_global_var('func_4263')
call_4264 = func_4263_call()
output = call_4264
func_4265 = relay.Function([], output)
mutated_mod['func_4265'] = func_4265
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4286 = relay.var("var_4286", dtype = "int32", shape = (10, 14, 7))#candidate|4286|(10, 14, 7)|var|int32
const_4287 = relay.const([[[-1,4,8,4,-9,9,-10],[-2,-7,-10,-7,5,-4,-8],[-6,-8,5,8,-2,-1,3],[-2,5,8,3,10,-10,7],[-6,4,3,-9,-4,2,-9],[-8,3,7,-7,1,2,2],[-8,6,4,-6,-2,7,-3],[-9,-4,-7,10,-4,-9,-7],[-8,-1,-7,-10,6,10,-10],[1,8,6,-8,8,6,-5],[8,-6,-8,-3,-3,-6,9],[-5,4,4,6,5,-4,-4],[-6,-7,-8,3,9,10,8],[-9,3,8,9,-1,-2,9]],[[-9,8,9,-2,-8,4,10],[7,2,-7,-9,-4,6,3],[4,-4,4,-8,7,3,-4],[3,9,-4,-8,-5,5,-5],[-9,-9,-10,-5,6,1,-5],[1,9,3,-3,-10,7,8],[-7,5,1,8,-6,8,-6],[5,3,-1,9,-2,-3,5],[-10,-6,-6,-2,4,8,4],[-1,-7,4,-4,2,-10,-6],[-9,-5,-4,5,-1,-4,-8],[4,-10,-2,3,7,-10,-1],[-5,5,7,-10,-2,-10,-1],[-7,-1,-1,-8,-8,-9,-8]],[[-3,-1,-5,-2,-8,-7,7],[-5,-4,-9,7,-7,-3,6],[9,-2,5,3,-2,6,7],[-2,1,-5,2,-1,2,-4],[1,8,5,4,-3,-2,4],[-5,-1,7,4,6,-6,3],[-5,6,8,-7,1,-5,-2],[7,4,9,7,-5,10,7],[10,-7,-8,10,4,-6,-1],[-9,-7,9,8,-7,5,-8],[-5,4,-6,10,-3,-7,-10],[-4,-6,-5,1,4,-3,-6],[5,5,10,7,8,9,8],[10,1,-10,-7,1,1,9]],[[8,-2,1,3,5,-9,-7],[-8,-6,-4,2,-5,-9,7],[2,3,1,-3,3,8,-5],[-4,-7,7,9,-2,5,10],[-4,5,-2,5,4,-8,3],[-4,2,3,8,-5,-1,-8],[4,4,6,3,-8,1,-6],[8,2,-2,-7,6,-4,4],[5,6,1,-7,-9,-5,1],[-8,5,-10,7,-3,-4,-2],[9,-6,2,-6,-9,-2,-5],[7,2,-5,-3,-6,-5,-7],[-10,-7,-6,3,-2,1,-2],[-2,-9,-3,6,8,2,-2]],[[-6,6,-7,-5,6,1,7],[-3,-6,-7,6,7,-7,5],[-10,-6,3,2,-5,-5,5],[10,1,-10,-8,3,7,10],[-5,-5,10,-3,3,7,2],[-8,-7,8,4,6,-7,8],[8,-1,-2,10,-10,-9,8],[-1,-7,9,9,-3,-7,7],[-7,-9,-2,6,7,-10,-8],[-1,2,-9,3,4,-5,-7],[5,8,8,4,8,-5,-7],[3,3,-4,-6,-5,-10,2],[-3,8,2,7,3,-1,-3],[-5,1,-6,2,9,-2,8]],[[1,-7,-1,-4,3,5,5],[9,2,8,4,8,-3,-5],[-9,-7,6,-9,-3,2,-4],[-3,2,-9,-8,8,9,9],[2,9,10,4,-1,3,-3],[1,-9,-8,-8,5,-4,-9],[6,-6,-5,-10,10,9,6],[-5,-6,-10,-3,-5,-7,-9],[3,3,8,-10,4,-6,-5],[-4,-8,3,7,8,-4,-3],[3,-2,-9,-8,6,-8,7],[3,-10,2,-7,-1,-8,8],[-1,-3,-10,3,-1,6,6],[-6,-9,-4,7,8,-2,-2]],[[-7,-4,-9,3,3,-3,-6],[2,5,4,8,-7,-5,-10],[-4,-7,3,9,8,3,9],[-6,5,6,7,-5,7,1],[-7,-1,3,3,-9,8,-6],[1,-7,10,-6,-1,6,9],[8,-9,8,7,6,-7,-4],[-6,-8,-8,3,-4,-6,-3],[10,8,-9,6,-5,-3,5],[-9,7,-9,-10,7,-7,-6],[7,-5,-1,-9,-2,-10,-8],[-1,2,-1,-3,3,9,1],[-2,-9,6,8,-1,-8,9],[-9,2,1,-7,-5,3,8]],[[-10,2,-5,3,-6,-9,-7],[7,6,5,7,-1,8,-7],[-6,7,-5,1,9,-1,6],[-2,-6,1,7,9,-3,8],[-10,2,-1,3,-5,6,-10],[-9,-9,-1,9,9,1,-10],[10,-6,5,6,9,2,6],[10,-4,-6,9,10,-1,-6],[6,-7,-5,7,-2,-6,4],[5,-5,-10,1,4,3,-9],[-2,9,2,6,-10,7,-8],[3,2,-6,10,-10,9,-2],[-7,-1,8,6,-9,-9,-7],[-2,-1,9,-2,2,10,-4]],[[5,3,9,-2,-5,8,3],[2,-6,-5,9,2,-10,3],[6,8,3,5,7,-2,-6],[-6,-8,8,-3,10,-8,3],[-7,-5,4,-4,7,3,-7],[-6,-5,-3,-3,6,-6,9],[-9,2,-1,-8,-2,-3,4],[-5,-9,5,5,7,-10,3],[-9,10,7,5,2,-2,-8],[5,1,4,-3,5,8,6],[-7,6,1,6,-9,-5,-4],[7,-4,-3,-4,-6,-7,-5],[-5,5,-1,-9,-8,-2,8],[9,-6,4,-1,-6,6,-2]],[[-5,10,-9,3,7,-4,-9],[-3,4,10,8,-2,3,-6],[10,-3,-6,-4,-1,6,-10],[-4,-7,-7,9,-2,3,8],[10,6,1,-4,4,5,-6],[5,1,7,4,-8,-3,-2],[2,10,-5,3,-6,4,-8],[7,-9,-2,-10,10,-4,9],[-9,-2,4,-5,10,4,9],[-8,-6,-3,-7,-7,3,-3],[4,-4,6,5,8,6,10],[-6,7,-5,10,9,-2,-4],[-4,4,8,2,-4,3,-7],[-1,-10,-7,10,-1,-2,8]]], dtype = "int32")#candidate|4287|(10, 14, 7)|const|int32
bop_4288 = relay.bitwise_xor(var_4286.astype('int32'), relay.reshape(const_4287.astype('int32'), relay.shape_of(var_4286))) # shape=(10, 14, 7)
uop_4296 = relay.erf(bop_4288.astype('float32')) # shape=(10, 14, 7)
output = uop_4296
output2 = uop_4296
func_4298 = relay.Function([var_4286,], output)
mod['func_4298'] = func_4298
mod = relay.transform.InferType()(mod)
mutated_mod['func_4298'] = func_4298
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4299 = relay.var("var_4299", dtype = "int32", shape = (10, 14, 7))#candidate|4299|(10, 14, 7)|var|int32
func_4298_call = mutated_mod.get_global_var('func_4298')
call_4300 = func_4298_call(var_4299)
output = call_4300
func_4301 = relay.Function([var_4299], output)
mutated_mod['func_4301'] = func_4301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2299_call = mod.get_global_var('func_2299')
func_2301_call = mutated_mod.get_global_var('func_2301')
call_4336 = relay.TupleGetItem(func_2299_call(), 0)
call_4337 = relay.TupleGetItem(func_2301_call(), 0)
output = call_4336
output2 = call_4337
func_4342 = relay.Function([], output)
mod['func_4342'] = func_4342
mod = relay.transform.InferType()(mod)
output = func_4342()
func_4343 = relay.Function([], output)
mutated_mod['func_4343'] = func_4343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3953_call = mod.get_global_var('func_3953')
func_3955_call = mutated_mod.get_global_var('func_3955')
call_4346 = relay.TupleGetItem(func_3953_call(), 0)
call_4347 = relay.TupleGetItem(func_3955_call(), 0)
output = relay.Tuple([call_4346,])
output2 = relay.Tuple([call_4347,])
func_4355 = relay.Function([], output)
mod['func_4355'] = func_4355
mod = relay.transform.InferType()(mod)
mutated_mod['func_4355'] = func_4355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4355_call = mutated_mod.get_global_var('func_4355')
call_4356 = func_4355_call()
output = call_4356
func_4357 = relay.Function([], output)
mutated_mod['func_4357'] = func_4357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_700_call = mod.get_global_var('func_700')
func_702_call = mutated_mod.get_global_var('func_702')
call_4374 = relay.TupleGetItem(func_700_call(), 1)
call_4375 = relay.TupleGetItem(func_702_call(), 1)
func_2634_call = mod.get_global_var('func_2634')
func_2641_call = mutated_mod.get_global_var('func_2641')
var_4392 = relay.var("var_4392", dtype = "float64", shape = (50, 10))#candidate|4392|(50, 10)|var|float64
const_4393 = relay.const([3.813615,8.484308,-8.648265,6.373766,-0.608703,7.967298,-1.830162,1.309708,-4.715175,4.905183,-9.424987,6.768020,1.615596,-6.478537,5.877286,0.473690,-6.358871,-1.527608,-3.074664,-8.983148,8.028281,-3.080602,2.937425,-6.206837,5.864684,-1.083553,8.124678,-3.977627,6.537120,-9.956345,-3.886328,-2.852726,-3.120461,-6.894302,-3.970581,-4.904338,-9.751422,8.876905,-3.330176,4.889609,2.564314,9.852769,-0.113213,1.770971,-5.608386,-4.980251,-0.736009,-6.792910,2.917665,4.710422,6.021268,4.031735,-1.882876,6.105417,-8.801536,0.957072,-5.136982,9.647269,-5.763809,7.949302,-7.011981,-4.888776,-0.727416,7.112163,1.096102,2.710742,-9.809125,-7.448915,-9.800569,-4.868818,-9.364917,-2.834783,-1.607179,2.234331,5.613944,-2.863631,-3.287608,-5.530521,1.314261,6.479079,-3.561505,5.181532,5.578036,-7.144293,-7.505300,2.574375,-1.819384,9.809744,4.433872,3.535568,7.664169,-4.467983,-4.739469,-7.654316,-8.337569,-2.603487,3.977063,-8.886835,7.070646,-5.629176,7.040518,3.518046,1.541485,-2.815895,9.124438,7.361854,5.752934,6.454022,-2.976850,4.923230,6.413590,-5.373293,-0.442444,5.254319,8.264891,6.497981,3.938882,-3.024749,2.275012,3.439007,-2.875153,-0.925259,-8.093201,-4.587489,3.673512,-6.176293,0.505582,4.638774,1.187813,-5.152069,-5.728833,7.093993,-7.825762,3.556463,-6.938434,-2.977601,4.979394,4.059158,-7.133140,1.083753,5.698947,-3.395249,-0.170967,-1.840317,3.410821,-4.658658,-5.343338,2.287962,6.354541,3.999755,-9.554678,-6.593160,-4.107260,4.955566,4.584967,-1.423661,-0.149426,-1.425137,7.929435,-0.774845,3.012764,-8.728047,-3.414794,-2.042065,-9.823920,-2.172736,9.972259,0.201346,-2.238647,1.713172,5.606679,-9.513650,-0.177471,-8.448616,-2.169364,-9.487268,9.518824,6.222005,3.524594,1.580561], dtype = "float32")#candidate|4393|(180,)|const|float32
const_4394 = relay.const([[-4,-7,-8,10,2,3,-9,3,9,-5,-9,-3,-6,-4,10,-7,1,-9,-10,8,-2,-7,-3,2,-10,-1,9,-6,6,-1,-8,-3,2,-9,-2,4,10,-7,-2,3,8,-1,-7,2,-8,2,-3,6,-8,8,4,5,3,-4,-3,-9,10,7,-6,3,-4,-2,1,-2,3,-10,-2,-8,7,2,-1,-10,-2,10,-6,3,-7,6,-1,10,8,10,5,7,-1,3,-1,-5,-9,-10,-6,-6,-6,-5,-1,-2,5,1,3,3,8,-6,-2,-9,-5,-8,9,-6,-8,-5,-5,10,-2,-9,10,9,-1,-4,-7,4,1,3,-5,9,1,4,3,-6,-4,10,-9,1,-5,3,-9,3,8,-4,-6,-8,-8,-3,-6,-8,3,6,8,-4,-4,4,-3,-7,-3,-5,3,6],[-8,4,7,4,-1,-4,10,3,-4,-9,-6,-9,5,-9,-9,-2,3,1,-2,-2,7,-4,-3,-1,8,5,6,6,-7,-4,2,-3,3,-7,-1,10,4,-7,2,5,7,5,-3,7,-6,6,6,-2,-5,6,7,-6,-9,-7,10,-5,3,2,-1,-6,9,-6,3,-6,9,6,9,7,6,10,-8,-5,-5,7,-8,-6,4,4,1,6,3,8,-6,1,-10,10,-8,-1,1,-10,10,6,9,1,-1,2,9,-5,6,8,8,6,-10,8,6,2,3,1,-9,2,9,5,5,-4,-7,4,10,-1,6,4,7,-9,-8,-4,3,9,1,2,4,-6,-10,-6,2,-3,-7,2,6,8,-10,-1,10,6,3,-9,6,8,6,8,-1,8,-9,4,2,9,4,-6],[1,-6,-10,3,-10,5,7,6,6,6,4,3,1,9,-4,-8,7,-1,-10,-4,-5,10,2,-10,10,6,-7,2,-2,3,-6,-3,8,-9,-8,1,-9,5,-5,-2,2,-2,8,9,5,-6,-3,-1,2,-9,10,-6,-1,4,8,2,5,-1,8,-5,-1,1,9,-5,1,-3,-6,-1,10,2,1,-1,9,-1,1,-1,6,-6,-5,10,-7,-8,2,9,-5,1,8,-6,4,-6,-3,7,9,8,4,-10,1,-5,7,4,-6,2,6,9,-7,-5,1,4,5,4,10,-10,1,-1,-9,4,1,-7,4,-9,2,3,-7,-3,-7,-2,2,7,9,-4,2,-4,-4,1,9,-10,5,-6,10,-5,-8,-5,10,4,9,-10,5,-5,-4,-6,-6,6,2,4,-3,1],[7,-2,10,-8,3,2,-1,5,-3,10,1,-3,-10,-7,7,6,5,-2,-3,2,10,2,-10,9,-9,-5,7,-3,6,-3,9,-6,7,-7,-2,-4,4,-6,-2,10,-7,4,-4,2,9,2,5,10,7,2,-10,-4,2,-1,-6,-10,7,-9,-2,-2,8,-9,-3,5,-8,-9,-3,3,4,2,4,-5,5,-3,-4,-8,-8,-5,5,10,9,4,-4,-7,-10,10,-10,-6,-8,-4,3,-7,8,-3,-4,-8,6,-4,8,1,-10,-3,-8,7,-9,10,-2,6,-1,-3,-4,9,-3,-2,-2,-3,6,5,5,1,3,-8,8,-5,3,-5,10,-6,-7,-8,-3,-3,4,-2,10,-5,-5,-9,4,-4,-3,3,5,8,10,-10,4,-10,1,-1,7,7,-8,-5,-2,1],[-9,1,-6,5,5,-6,1,1,-10,-5,10,-9,8,-3,6,-6,-10,1,7,9,3,5,3,-6,-10,-2,-2,-7,6,3,-5,6,-7,9,-5,6,-6,-10,8,-4,6,7,8,10,-5,7,-1,3,-2,-10,3,-2,8,9,-7,-4,-10,1,-6,-1,4,-1,1,-1,-8,-9,-10,9,-1,5,3,1,2,-9,-2,9,10,-9,6,3,4,5,3,1,4,3,7,1,5,8,-2,-3,9,-3,-5,-8,-10,-2,-1,-8,1,4,-5,-9,-5,-10,-4,-9,-7,7,-9,-1,-10,-2,8,-7,1,-8,4,-7,-4,6,-9,2,-7,10,-6,7,-3,-8,-10,1,6,-10,-9,-1,-3,5,-4,-10,8,9,8,-3,-8,6,-5,1,-8,-4,-7,10,-4,4,1,-8],[-1,-4,-4,1,-7,-4,-4,6,6,-9,-4,5,-5,5,10,-7,-10,-1,8,-10,1,-9,-9,-8,-4,-9,5,8,2,8,-5,-6,-5,-3,9,2,-5,4,6,8,9,2,-3,6,4,-1,8,-7,-2,-8,2,-10,10,3,-8,-10,10,2,2,1,1,-6,9,2,4,2,-9,-4,-10,7,-10,6,-8,-5,8,8,-10,-10,10,8,-3,1,-7,-3,4,5,-4,7,-1,4,-8,1,-9,-7,-5,4,-7,10,-1,-1,2,2,6,7,2,7,4,-10,-8,-3,-1,-9,-3,2,-3,-1,-10,-10,-2,4,-10,4,8,10,-10,-7,1,9,8,-8,-6,-5,-1,3,-3,5,-9,-1,4,4,-4,5,8,9,-7,6,-5,-2,-7,-10,-5,8,-6,2,2,-4]], dtype = "int16")#candidate|4394|(6, 156)|const|int16
const_4395 = relay.const([-7.652399,-7.757929,-3.989223,-9.212286,9.286992,5.009944,-6.152374,-9.297131,9.307621,-8.074696,-5.172126,-1.956467,3.752772,-7.429137,4.507371,-6.507750,1.113893,5.732517,-1.717113,-3.606622,9.866107,7.203425,-6.991239,-5.881820,5.127384,1.979756,-9.431644,-0.023894,-0.114557,-6.246555,0.205497,4.719212,-2.631189,4.699331,6.570074,-7.958569,9.744146,-8.655464,5.257042,1.145387,6.949526,-3.406930,-5.285743,-9.053769,-6.042146,-6.462183,8.619912,-0.963004,-0.105573,-0.105501,-3.755918,-8.326054,-1.161325,0.804907,7.087364,5.445150,9.413374,-0.679522,-5.227000,6.184837,-1.677267,5.852581,5.766708,2.038259,2.956502,4.986015,-9.741275,2.507986,-3.135144,-6.718238,7.294137,5.876539,-2.564524,-0.756631,-3.943371,2.307609,6.305768,-8.109613,-2.133419,-2.670920,-8.466900,4.034025,6.280931,3.195599,6.081917,8.509001,5.168459,-9.330950,-4.904786,5.993856,-3.793951,0.002867,0.910532,-0.651639,5.027826,7.384325,3.140706,-9.773565,4.968741,-6.645516,-3.127078,1.515792,-2.110280,9.892470,-0.441082,6.880145,0.583381,-8.332808,8.272000,-1.879769,6.862566,-8.014626,8.902416,1.230886,-1.275332,3.519224,8.989525,4.045270,-4.942541,-2.286624,0.776793,2.088827,9.291685,7.668219,5.217447,6.695350,4.814388,0.964130,0.343971,6.524461,-8.714444,-0.818452,9.500296,-5.624968,-9.370262,-9.276136,-3.013503,-1.286371,1.153966,-9.360943,2.857621,0.034186,7.398740,5.984655,5.470984,8.496811,-0.045870,2.532977,1.677627,0.125858,-7.941550,9.971035,-4.080684,-7.005837,1.555704,-7.668657,3.703762,3.315892,-0.310752,0.704979,9.671820,3.182656,-4.140625,5.193546,-4.030261,5.627554,-6.116429,-7.972486,-8.391947,-3.454437,4.619249,-9.234247,-2.574939,-6.316406,7.213134,-8.535056,-1.768651,-7.891664,-1.541502,-3.843087,-9.071822,8.108123,-3.037004,6.177579,7.463065,-0.542070,-7.238728,5.596996,-4.506871,0.447398,4.274819,-0.999193,-2.945134,-5.033871,-7.862282,3.035347,-6.918687,3.429029,-0.653242,3.993878,-3.138551,1.155559,-6.908781,4.671758,-7.872414,-6.678924,-3.024937,5.040210,4.175065,7.943833,-9.230866,3.310115,9.992995,3.885072,9.090625,0.014882,-9.916635,7.081287,8.343631,8.779714,1.099070,8.783129,-9.150251,-6.603325,-6.753858,6.189347,9.658696,1.760099,9.168129,-1.718134,7.934282,-6.207694,-4.282901,3.748549,-3.466967,1.614079,-3.422766,0.577871,8.702782,6.797572,7.887785,-9.234367,7.721452,2.541012,-0.093393,8.393819,-1.498496,0.066597,7.463343,-0.459996,0.706679,-6.154296,5.665404,-5.021050,7.223277,-4.109483,-6.852773,5.853934,5.477293,-1.564305,5.305624,1.874966,2.734119,-3.646250,7.946727,-9.530113,5.729036,2.602855,-6.510705,8.419827,4.705624,-0.878809,8.967805,7.251058,3.213400,-5.220858,6.192105,-3.376244,8.639520,-3.118203,4.379522,0.448664,6.951410,3.909797,9.328644,2.455067,0.388737,-2.679079,-4.696759,0.906770,-8.498344,-6.795178,9.381716,-9.161740,1.943286,-3.835705,-0.143100,3.401032,-9.406343,5.840898,-0.341702,-3.461530,3.753412,-9.236649,-3.855091,9.335016,3.901096,-7.841311,-5.548401,6.962493,1.340564,-3.340859,-0.408350,0.532776,3.593984,-8.448026,-7.323142,4.645754,6.014734,9.247275,1.653952,-4.470374,-5.191582,3.730691,-8.833434,-9.116398,-6.748369,0.107775,4.536112,2.085339,4.145430,-3.804965,-8.696077,5.493367,8.164101,6.386108,4.681585,1.388996,8.420609,-5.353794,-5.761564,9.167986,-0.747404,0.810779,-3.279367,-3.196842,-6.894168,4.212890,-0.089855,-8.576712,6.677201,-3.258114,-7.550360,-9.441073,-1.424605,7.056722,9.063338,-9.107418,8.573110,0.648942,-1.395001,0.744667,-2.700570,-8.506089,-4.459420,-1.568456,-4.065243,-4.295018,9.143867,-1.972631,-3.040060,-3.510125,9.784683,4.166791,-1.148796,-1.807618,-8.367724,9.925259,-9.738376,3.434424,-3.057214,-4.640045,-1.018484,4.233129,6.275426,8.531405,8.522295,6.515942,-1.698439,2.720743,-6.496844,-1.636987,-8.305239,7.751935,9.533166,5.080292,1.304857,-5.764345,-7.823584,9.207776,-5.039439,5.924970,-3.401091,-3.823596,9.749484,8.898354,3.231664,-8.604552,4.830035,-6.343401,-0.864356,-5.757536,2.882785,6.333714,4.964261,7.666902,-0.421757,2.179299,2.754917,8.857182,-6.504749,-6.223588,-3.270843,0.123111,2.842560,-2.281444,3.176755,2.688225,-9.310813,-5.448923,9.654171,7.594309], dtype = "float32")#candidate|4395|(432,)|const|float32
call_4391 = relay.TupleGetItem(func_2634_call(relay.reshape(var_4392.astype('float64'), [5, 10, 10]), relay.reshape(var_4392.astype('float64'), [5, 10, 10]), relay.reshape(const_4393.astype('float32'), [180,]), relay.reshape(const_4394.astype('int16'), [936,]), relay.reshape(const_4395.astype('float32'), [12, 36]), ), 10)
call_4396 = relay.TupleGetItem(func_2641_call(relay.reshape(var_4392.astype('float64'), [5, 10, 10]), relay.reshape(var_4392.astype('float64'), [5, 10, 10]), relay.reshape(const_4393.astype('float32'), [180,]), relay.reshape(const_4394.astype('int16'), [936,]), relay.reshape(const_4395.astype('float32'), [12, 36]), ), 10)
func_4355_call = mod.get_global_var('func_4355')
func_4357_call = mutated_mod.get_global_var('func_4357')
call_4397 = relay.TupleGetItem(func_4355_call(), 0)
call_4398 = relay.TupleGetItem(func_4357_call(), 0)
output = relay.Tuple([call_4374,call_4391,var_4392,const_4393,const_4394,const_4395,call_4397,])
output2 = relay.Tuple([call_4375,call_4396,var_4392,const_4393,const_4394,const_4395,call_4398,])
func_4401 = relay.Function([var_4392,], output)
mod['func_4401'] = func_4401
mod = relay.transform.InferType()(mod)
var_4402 = relay.var("var_4402", dtype = "float64", shape = (50, 10))#candidate|4402|(50, 10)|var|float64
output = func_4401(var_4402)
func_4403 = relay.Function([var_4402], output)
mutated_mod['func_4403'] = func_4403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3543_call = mod.get_global_var('func_3543')
func_3544_call = mutated_mod.get_global_var('func_3544')
call_4493 = relay.TupleGetItem(func_3543_call(), 0)
call_4494 = relay.TupleGetItem(func_3544_call(), 0)
output = call_4493
output2 = call_4494
func_4500 = relay.Function([], output)
mod['func_4500'] = func_4500
mod = relay.transform.InferType()(mod)
mutated_mod['func_4500'] = func_4500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4500_call = mutated_mod.get_global_var('func_4500')
call_4501 = func_4500_call()
output = call_4501
func_4502 = relay.Function([], output)
mutated_mod['func_4502'] = func_4502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1179_call = mod.get_global_var('func_1179')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_4587 = func_1179_call()
call_4588 = func_1179_call()
func_1617_call = mod.get_global_var('func_1617')
func_1618_call = mutated_mod.get_global_var('func_1618')
call_4596 = relay.TupleGetItem(func_1617_call(), 2)
call_4597 = relay.TupleGetItem(func_1618_call(), 2)
output = relay.Tuple([call_4587,call_4596,])
output2 = relay.Tuple([call_4588,call_4597,])
func_4598 = relay.Function([], output)
mod['func_4598'] = func_4598
mod = relay.transform.InferType()(mod)
mutated_mod['func_4598'] = func_4598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4598_call = mutated_mod.get_global_var('func_4598')
call_4599 = func_4598_call()
output = call_4599
func_4600 = relay.Function([], output)
mutated_mod['func_4600'] = func_4600
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4601 = relay.const(6, dtype = "uint16")#candidate|4601|()|const|uint16
var_4602 = relay.var("var_4602", dtype = "uint16", shape = (12, 2, 1))#candidate|4602|(12, 2, 1)|var|uint16
bop_4603 = relay.multiply(const_4601.astype('uint16'), var_4602.astype('uint16')) # shape=(12, 2, 1)
output = relay.Tuple([bop_4603,])
output2 = relay.Tuple([bop_4603,])
func_4610 = relay.Function([var_4602,], output)
mod['func_4610'] = func_4610
mod = relay.transform.InferType()(mod)
var_4611 = relay.var("var_4611", dtype = "uint16", shape = (12, 2, 1))#candidate|4611|(12, 2, 1)|var|uint16
output = func_4610(var_4611)
func_4612 = relay.Function([var_4611], output)
mutated_mod['func_4612'] = func_4612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4263_call = mod.get_global_var('func_4263')
func_4265_call = mutated_mod.get_global_var('func_4265')
call_4634 = relay.TupleGetItem(func_4263_call(), 2)
call_4635 = relay.TupleGetItem(func_4265_call(), 2)
output = call_4634
output2 = call_4635
func_4637 = relay.Function([], output)
mod['func_4637'] = func_4637
mod = relay.transform.InferType()(mod)
mutated_mod['func_4637'] = func_4637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mutated_mod.get_global_var('func_4637')
call_4638 = func_4637_call()
output = call_4638
func_4639 = relay.Function([], output)
mutated_mod['func_4639'] = func_4639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3953_call = mod.get_global_var('func_3953')
func_3955_call = mutated_mod.get_global_var('func_3955')
call_4664 = relay.TupleGetItem(func_3953_call(), 0)
call_4665 = relay.TupleGetItem(func_3955_call(), 0)
output = call_4664
output2 = call_4665
func_4668 = relay.Function([], output)
mod['func_4668'] = func_4668
mod = relay.transform.InferType()(mod)
mutated_mod['func_4668'] = func_4668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4668_call = mutated_mod.get_global_var('func_4668')
call_4669 = func_4668_call()
output = call_4669
func_4670 = relay.Function([], output)
mutated_mod['func_4670'] = func_4670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4668_call = mod.get_global_var('func_4668')
func_4670_call = mutated_mod.get_global_var('func_4670')
call_4733 = func_4668_call()
call_4734 = func_4668_call()
output = call_4733
output2 = call_4734
func_4757 = relay.Function([], output)
mod['func_4757'] = func_4757
mod = relay.transform.InferType()(mod)
output = func_4757()
func_4758 = relay.Function([], output)
mutated_mod['func_4758'] = func_4758
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4767 = relay.var("var_4767", dtype = "float64", shape = (9, 10, 14))#candidate|4767|(9, 10, 14)|var|float64
uop_4768 = relay.asinh(var_4767.astype('float64')) # shape=(9, 10, 14)
uop_4795 = relay.cos(uop_4768.astype('float64')) # shape=(9, 10, 14)
func_3863_call = mod.get_global_var('func_3863')
func_3865_call = mutated_mod.get_global_var('func_3865')
call_4797 = relay.TupleGetItem(func_3863_call(), 0)
call_4798 = relay.TupleGetItem(func_3865_call(), 0)
func_4298_call = mod.get_global_var('func_4298')
func_4301_call = mutated_mod.get_global_var('func_4301')
var_4815 = relay.var("var_4815", dtype = "int32", shape = (14, 70))#candidate|4815|(14, 70)|var|int32
call_4814 = func_4298_call(relay.reshape(var_4815.astype('int32'), [10, 14, 7]))
call_4816 = func_4298_call(relay.reshape(var_4815.astype('int32'), [10, 14, 7]))
output = relay.Tuple([uop_4795,call_4797,call_4814,var_4815,])
output2 = relay.Tuple([uop_4795,call_4798,call_4816,var_4815,])
func_4823 = relay.Function([var_4767,var_4815,], output)
mod['func_4823'] = func_4823
mod = relay.transform.InferType()(mod)
var_4824 = relay.var("var_4824", dtype = "float64", shape = (9, 10, 14))#candidate|4824|(9, 10, 14)|var|float64
var_4825 = relay.var("var_4825", dtype = "int32", shape = (14, 70))#candidate|4825|(14, 70)|var|int32
output = func_4823(var_4824,var_4825,)
func_4826 = relay.Function([var_4824,var_4825,], output)
mutated_mod['func_4826'] = func_4826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1684_call = mod.get_global_var('func_1684')
func_1685_call = mutated_mod.get_global_var('func_1685')
call_4983 = relay.TupleGetItem(func_1684_call(), 0)
call_4984 = relay.TupleGetItem(func_1685_call(), 0)
output = relay.Tuple([call_4983,])
output2 = relay.Tuple([call_4984,])
func_4985 = relay.Function([], output)
mod['func_4985'] = func_4985
mod = relay.transform.InferType()(mod)
mutated_mod['func_4985'] = func_4985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4985_call = mutated_mod.get_global_var('func_4985')
call_4986 = func_4985_call()
output = call_4986
func_4987 = relay.Function([], output)
mutated_mod['func_4987'] = func_4987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_5040 = func_2773_call()
call_5041 = func_2773_call()
var_5048 = relay.var("var_5048", dtype = "float64", shape = (4, 9, 10))#candidate|5048|(4, 9, 10)|var|float64
bop_5049 = relay.logical_and(call_5040.astype('bool'), var_5048.astype('bool')) # shape=(4, 9, 10)
bop_5052 = relay.logical_and(call_5041.astype('bool'), var_5048.astype('bool')) # shape=(4, 9, 10)
output = relay.Tuple([bop_5049,])
output2 = relay.Tuple([bop_5052,])
func_5053 = relay.Function([var_5048,], output)
mod['func_5053'] = func_5053
mod = relay.transform.InferType()(mod)
mutated_mod['func_5053'] = func_5053
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5054 = relay.var("var_5054", dtype = "float64", shape = (4, 9, 10))#candidate|5054|(4, 9, 10)|var|float64
func_5053_call = mutated_mod.get_global_var('func_5053')
call_5055 = func_5053_call(var_5054)
output = call_5055
func_5056 = relay.Function([var_5054], output)
mutated_mod['func_5056'] = func_5056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_514_call = mod.get_global_var('func_514')
func_515_call = mutated_mod.get_global_var('func_515')
call_5109 = func_514_call()
call_5110 = func_514_call()
func_3043_call = mod.get_global_var('func_3043')
func_3046_call = mutated_mod.get_global_var('func_3046')
const_5120 = relay.const([6.568556,8.250679,-7.810339,-1.303393,-4.836406,-1.226602,-6.325426,0.017783,4.333451,2.144415,2.307979,-7.691022,6.735759,-5.997151,6.970938,9.710581,0.918869,0.391245,8.708148,-7.134527,-4.317878,-2.420617,-2.725506,6.335656,-4.317503,8.184768,2.440639,1.942100,-2.008316,2.048842,6.423988,-4.884956,2.165379,-6.039133,2.010025,-4.908044,-2.686173,0.950938,9.267557,-6.973716,1.573038,8.758963,-7.067283,5.323552,-2.426526,-7.187390,4.767292,-4.912037,-7.038363,-3.940714,-9.632948,5.743499,7.667024,3.808869,3.005452,5.904456,0.833793,8.565320,3.249471,-0.376398,-1.780233,-2.878703,1.544876,-2.375174,1.746960,-7.394435,-2.989858,-4.869318,-3.326861,-4.232772,-0.073136,-2.900051,-7.385177,7.712542,-0.114207,0.935440,-0.530796,-4.913328,-1.725467,5.731082,3.293530,8.837422,4.831712,-7.362388,1.823911,9.518825,-8.756286,2.777204,-7.843880,-8.704049,-9.138827,8.146237,3.797386,5.720534,-0.621815,-1.449885,-5.221931,4.328333,7.928637,8.908580,-9.914682,-0.236746,-5.822875,3.168133,-2.427689,9.048000,1.410540,9.451200,-9.709928,8.295451,5.516810,8.594179,3.814196,8.978103,-8.345060,-7.882411,-8.579221,4.037160,-9.785371,4.132673,-7.881439,-4.513104,2.209096,5.853304,-7.939190,-6.237405,-9.912011,1.617637,7.628398,-5.877734,5.543833,-3.095983,-7.730188,-3.916202,3.852592,1.508766,-3.172914,6.747660,-1.892278,0.052305,3.762556,-8.119004,8.216010,-8.839489,3.452897,-1.935170,7.993964,-7.304438,-4.897524,-5.841340,-0.826706,-3.124427,1.117378,-0.099395,-5.424315,-1.628598,3.660407,5.324872,-6.167007,7.291035,-9.665582,-3.686704,2.489374,4.587523,3.714290,9.729833,-9.016019,-0.907620,4.687763,2.583142,5.760438,-7.655659,-0.812490,3.118893,0.992004,-2.035426,5.243460,9.075342,0.659685,-6.896508,-7.470435,-4.714342,8.158529,1.852145,9.609946,-5.503120,-5.726309,-2.109807,-6.862359,-7.788848,-9.035279,-1.027230,5.599224,-5.839627,-1.142634,-8.330770,-3.372493,1.640976,1.320184,0.795814,3.943578,3.466770,-1.325116,0.752785,-8.082938,-6.154847,-7.393795,-0.405335,-5.984626,5.168064,9.033575,6.562027,-4.610701,-8.454632,4.373088,2.273130,9.396795,0.956075,-1.327187,8.426088,-4.144000,6.913649,-5.209604,-2.110570,6.142161,0.280880,5.284794,-6.576812,-4.063653,-0.135769,-3.301257,-8.302618,-4.340761,3.733548,-5.801414,6.486411,-9.552481,-4.557310,-9.249274,2.248600,-8.811532,2.759178,-5.427311,2.828071,-2.508094,-4.701267,9.988763,-4.593802,-9.364420,-8.918013,-8.772615,2.556774,8.608975,6.085833,0.008733,4.048807,-0.641230,2.371497,-4.216966,9.453021,-2.425105,-4.952642,-4.857419,-1.809067,-2.141407,-8.218395,-8.414563,-8.802619,3.011897,-9.887287,-5.071543,-2.817988,-4.437583,0.441664,-5.288388,3.486375,9.357467,0.272632,-8.503870,-4.092572,-7.682718,-5.656371,8.001087,-1.014878,-6.093591,5.885649,-3.297698,3.822888,7.196091,-9.005297,6.452173,1.699818,5.429830,6.452009,-6.107345,-1.599057,-3.536184,5.984859,0.716682,-0.712256,-4.110981,8.676198,2.922657,0.323368,8.182510,-7.255195,9.071683,0.930581,-6.925622,9.092025,8.173822,-6.177134,-2.869280,0.460129,7.986748,1.453276,3.438004,8.645714,-9.736737,1.773704,-6.036229,-7.311422,7.378239,-9.014704,-2.888341,-3.402727,2.361030,3.164739,6.285015,-0.601052,-1.355400,-3.433319,-7.286775,-5.044808,5.574157,-5.252852,-2.943409,2.474224,2.672696,7.696644,0.210882,2.450321,-4.787584,-6.356945,3.751810,8.573195,5.394408,7.415000,0.546882,-5.648538,2.940933,-9.537915,6.116208,-7.793772,2.335385,4.957019,8.329250,8.774812,8.396721,6.487050,-5.499900,5.175338,1.196008,4.253950,-0.614277,7.622232,6.082038,3.013150,8.158126,4.885265,-7.176623,-8.130774,9.752428,8.718037,7.700610,4.128654,0.478196,4.201837,9.433537,3.188398,-4.846995,3.201228,-0.186545,3.853066,-1.046182,-7.701640,1.000685,3.944295,6.247689,7.429986,1.358800,-0.195341,8.306760,6.678074,7.158896,1.824874,7.293468,7.265708,4.521891,-0.738720,6.987968,-6.314202,7.125846,8.418391,6.728053,7.438064,3.575671,2.157858,-2.559477,3.663447,-9.616739,4.954208,7.528735,9.716842,0.281214,0.683993,1.615408,6.010846,3.662852,1.219695,-9.063307,9.810330,-3.520806,-2.126290,-7.117720,-8.535051,-4.784452,-5.546601,-5.270697,6.021229,3.890361,-7.952711,-4.972286,2.791466,-0.431506,-9.852126,-2.837709,-2.062190,4.040957,4.979839,-3.045072,-6.225891,4.520915,3.381163,-5.136126,-2.568793,5.638320,-4.374528,-4.960401,6.841013,-7.499401,7.164611,3.559569,-1.760277,0.588756,-3.833839,2.713030,-1.039094,-8.074427,2.619302,-6.632864,-3.550664,-3.072015,-0.416164,2.820632,-7.806519,6.822865,-6.071113,0.076134,1.095544,-1.756691,8.818426,-8.330334,-6.726741,5.188079,-1.076278,9.112096,8.034179,6.798362,3.637462,8.782874,6.184747,1.538774,0.378721,-8.955987,4.346766,3.743025,-1.815119,3.057335,-5.976104,-4.087821,-7.109682,5.701098,-7.570595,5.656032,3.570986,6.704650,-6.959295,-1.315864,1.469143,-5.168620,5.700512,6.362948,-5.344265,6.760763,5.767380,7.480717,0.795504,2.733302,2.667612,0.616354,4.245197,1.590824,-3.427410,-6.016872,-8.405717,-7.530229,-5.528991,-6.805963,-6.864807,6.837778,2.571724,-0.013590,1.312160,-6.694689,-4.230799,-7.863526,-3.866283,8.585248,0.634229,6.544222,5.535226,-0.608750,7.748108,-2.721740,-6.242837,-3.705020,-1.978389,-4.555786,-8.591571,-3.555035,3.487494,1.880899,5.223761,-8.714772,-1.792594,-9.268770,0.393364,6.614500,0.439434,3.230401,3.412916,-3.675315,-2.699307,4.864004,2.771090,9.327410,-6.657846,7.302151,-7.903941,7.667687,7.981595,-9.698244,-2.732222,4.882841,5.830147,9.827262,-4.352567,-5.393882,-2.767060,-4.133142,2.204319,-6.417147,-4.963510,0.395802,0.145805,2.864093,5.998178,-6.792631,1.757135,9.391955,-3.455534,4.742953,-0.973771,3.219345,3.535997,9.076357,4.424031,5.198426,2.039174,-9.706738,8.511162,1.921340,3.071224,-3.928468,6.687697,1.058486,-3.433535,2.379570,-7.770500,7.941053,-4.050858,7.534323,4.012449,9.804022,7.936620,4.758490,7.661464,3.541361,-8.364610,1.870358,-9.868345,6.243599,7.542207,4.799501,3.733178,2.789370,0.761141,-0.152249,9.514640,8.236930,5.954483,6.029739,0.568619,-8.332948,-8.198862,-5.071253,-4.578235,6.631649,-1.546952,-8.872039,-8.819544,9.823665,-7.393794,-9.976362,1.002767,-5.406150,-4.283786,0.394459,6.932817,-1.262522,2.086584,-6.773904,-7.913665,3.969736,-2.883103,6.579940,2.743728,6.651972,-8.673583,-9.013550,0.952116,-6.865593,-2.859753,-1.095392,2.920481,-3.600660,0.701126,5.211715,-2.601390,-3.695864,-8.226733,1.776274,-7.335923,8.222994,-4.351476,-9.440052,-3.546481,-0.371865,-6.887372,-9.374746,5.446827,-3.340866,3.949957,-0.921317,-1.557653,8.439920,-8.118672,-7.544569,8.290313,2.244844,2.982588,9.495443,9.015621,4.154935,-8.089526,4.021597,-5.365633,-4.699261,0.002132,2.701212,3.690113,-1.352806,-4.480534,-1.548841,-6.845726,6.331137,8.710995,-8.688806,-8.052736,-6.091209,3.460195,-4.225854,7.976410,-8.373712,-4.275160,-5.725782,-1.319411,5.202264,-4.399486,-5.165585,-4.188987,-7.574170,-0.108072,-0.162957,-5.529141,-1.891832,-4.627734,1.247928,1.316679,5.680984,-8.963798,-1.683771,-7.390478,3.995776,5.082365,-2.233819,7.788448,-3.705314,7.753902,0.796002,6.088128,6.194446,-4.059366,-1.355100,-4.700452,7.705258,6.734360,3.348865,-6.834572,-1.206644,-2.919360,1.859655,-2.968450,-6.773791,-2.039246,8.216525,3.847660,1.653590,-2.061146,8.774714,6.116133,5.043510,-8.065153,7.633628,0.991334,1.895594,-7.447865,4.043768,-8.180743,-7.483780,5.659214,-8.616851,-3.148895,8.482853,9.832733,-0.928601,4.010155,-5.111969,-0.420592,-5.861411,2.592223,-4.037267,-7.936816,-7.965717,8.892875,4.232808,8.710884,1.822245,-6.768284,-4.704439,9.663868,-0.545224,-8.866997,5.336076,-7.815081,-0.182343,0.088672,1.604067,-7.401240,-0.373840,-4.878225,0.275941,1.827322,-3.990999,1.126033,-6.330797,8.640266,8.814344,8.801996,-7.451089,6.113135,0.549636,1.807193,-9.899491,4.428951,3.025107,1.343882,8.873488,4.030100,-2.962170,-7.764070,-6.661731,4.104075,3.738687,-3.857194,3.063793,-5.338959,-7.563510,6.918739,0.060173,5.787306,1.537393,1.365081,8.850564,-6.763711,7.477788,-8.588355,-0.731765,-3.405938,-9.822944,2.602368,-0.530539,3.701544,-8.850321,6.383023,1.215507,-1.944792,4.284648,6.450672,4.622363,-8.591633,-3.934290,-4.246697,7.733850,-5.096999,4.441228,2.004854,3.742825,-3.085275,3.098632,5.007549,-6.500379,5.964780,-9.507430,-2.498923,-1.819675,-2.449174,-7.620050,5.926849,9.030590,9.061776,-5.431741,-7.164045,0.737496,5.737197,4.510872,4.962246,-5.187514,7.099693,9.095236,-1.731990,9.474042,-9.886996,6.595511,4.682759,2.695036,0.626350,5.200175,9.783148,-4.422147,7.512438,-5.350297,3.845469,-0.872595,4.959548,9.771688,0.499660,-5.726473,-0.859384,-2.759909,2.590995,-4.878312,0.349872,-2.747546,9.612667,3.970511,-8.490465,7.754808,-0.349149,2.021474,-2.711432,-6.117953,8.839983,2.454560,-3.605762,8.256494,-3.538921,3.364215,1.239122,-4.407899,-4.826565,3.647534,0.464606,8.625216,-0.287699,4.225411,8.453871,2.738445,1.695433,-2.083160,-6.319546,6.046925,5.506945,-3.478158,-5.668428,2.619887,-4.791288,-2.387032,-0.189420,1.585553,-2.640146,6.161779,-4.972845,-9.118573,0.458106,-3.919747,-5.247806,-0.410043,-9.788181,-4.255929,-0.596378,2.547944,-5.366294,-0.785041,9.685332,-1.333859,2.052862,3.928981,-2.237957,0.498176,-0.142641,9.117254,0.965336,7.151220,-0.455874,-0.953464,6.763375,1.457159,3.808256,-6.192534,6.184537,-8.329725,-8.155942,6.482941,9.847179,0.564306,-4.870951,-4.847523,-9.369313,1.493213,5.361292,9.732065,5.432384,3.325400,1.009418,-6.341353,-2.069132,7.429527,-6.515432,9.073711,0.755867,-2.597856,2.404903,1.372451,-0.279585,-9.450120,-1.169979,-1.645145,-6.284748,7.463756,-4.198562,-6.010269,-1.230820,0.542921,-5.946135,7.971634,8.316198,7.014044,-1.408447,1.915974,3.119984,8.338479,4.746691,-4.105196,7.179465,7.627540,0.440345,-8.549043,3.242292,-7.187005,-7.466095,0.815481,3.707606,-1.175110,0.493916,-1.277899,9.594979,1.933318,-8.251002,-1.444895,5.110500,3.522256,0.983082,-1.225967,8.441085,1.519127,-3.200734,-2.650683,7.209911,-2.504422,-9.893393,-8.248049,-2.563348,-8.233077,7.889981,-5.898867,6.509210,1.558499,0.193784,5.048492,-1.106296,-0.502333,-1.356658,8.330100,2.798860,-5.724839,-4.594389,1.392566,-3.984206,8.261533,-5.192269,-9.896442,2.862504,-0.762895,-9.163346,-6.148656,-6.614683,0.422783,0.325910,2.582002,-9.952066,-8.784578,-5.256227,9.687290,4.351355,-2.275620,-1.047598,9.939124,-2.304317,-3.360746,-1.442718,8.153481,0.249580,2.150300,6.450700,5.739496,-2.281664,6.869777,3.767848,-6.708181,4.143044,-0.984330,5.181642,-8.643625,-3.429015,-8.462009,0.233484,0.433311,4.513697,5.725022,6.039561,-8.244556,-9.255157,-3.755901,6.817648,-9.235037,5.773601,-5.733351,6.418236,-3.541391,-6.986995,-8.267811,5.198547,-0.566033,-1.860352,1.030856,8.254651,3.501675,4.872515,7.345215,-6.437245,-0.179621,0.436193,5.357229,5.768775,-5.290379,-5.465496,5.421667,-9.307231,-3.708117,1.834223,3.264814,-0.776102,-4.573475,-3.245241,-0.303004,2.442941,7.140041,2.437598,4.315665,-2.170099,-8.062086,-6.937098,-7.574341,-3.275306,4.384567,3.250300,-4.270588,-3.362847,7.924289,-8.152044,4.019112,-0.934457,-7.195836,7.633006,-0.955909,0.802851,0.381051,-7.553936,7.947482,-0.441209,-6.866578,4.496961,0.145062,1.705587,-0.134367,-9.660274,-8.930845,-9.468325,7.746838,-5.856169,-9.480242,-2.023869,-9.424530,9.618915,5.296613,-3.260174,7.190908,-0.229397,9.646506,-8.689440,-4.508934,-2.230786,4.327743,4.309220,-4.681686,1.004047,-3.074090,-9.607899,-8.411935,-8.741258,-3.869196,-1.876402,-9.119057,-4.720109,-8.968866,1.044248,-3.874854,1.405053,4.906500,-1.755602,5.955647,-8.907410,7.823251,-5.127273,-5.625165,-7.652721,5.064365,7.855520,0.732770,-6.456251,-3.308251,-3.524598,2.152891,-9.753044,2.442786,-3.191540,-5.833795,-4.757570,-3.826887,-1.826193,1.768176,2.611416,0.146774,-6.516294,-3.975748,-9.605969,-0.666244,3.382490,4.317872,-6.653462,-8.241668,2.759223,9.034554,9.148048,-0.981859,0.772414,-3.955205,-6.544947,4.264482,-4.362166,5.175987,-3.620666,-2.306473,8.735030,6.890537,-6.208602,9.529218,8.432169,4.347637,-0.528000,-0.624065,1.659152,-9.514449,-3.307967,-2.333548,5.011945,1.590967,3.763085,-5.287476,5.865832,5.607546,1.572370,9.252554,2.312957,1.921011,-9.960036,7.102550,-5.625108,-6.962300,6.412796,-4.310561,-8.897371,-2.453689,7.395977,0.379217,6.950348,-6.050397,0.131128,7.678006,-5.615703,-7.426941,-7.935728,-7.149210,4.765611,4.545291,3.937883,0.532009,3.749619,3.356197,-4.531438,-3.951055,6.046889,6.892715,-7.636415,-5.483116,8.050879,-6.574342,-1.793046,7.743520,1.752899,5.810045,-4.195977,-0.921313,-4.246683,-5.803235,-0.379316,-0.397160,0.994125,-2.149140,-1.590054,-2.819236,1.494649,5.380280,0.208705,1.772897,5.323537,9.715817,-6.735835,-1.164980,8.010527,5.205593,5.118975,-2.778544,3.062952,-9.833759,4.984213,-1.919820,9.456896,-8.800014,-0.914773,4.877138,-7.937794,5.508198,6.754132,-0.821902,-7.069622,-0.469683,0.234085,-3.212319,-9.466318,0.013112,7.877840,-8.159392,7.379789,9.245488,3.261595,-1.525705,7.686411,-3.876529,4.171565,3.064394,-7.792909,1.243192,-5.378449,8.351440,-3.008663,-4.159353,-4.192445,0.307902,-5.327632,9.866841,2.473912,2.015116,5.385427,5.601643,-6.766422,-8.560762,7.688188,3.977130,8.542635,-1.493495,9.777995,7.488702,1.592245,6.503252,8.676320,0.124971,-9.350395,5.823442,-5.261320,-2.281737,5.766427,-4.732494,-2.421796,8.361217,-2.871883,-4.184845,-8.971339,9.616238,-3.264192,4.951496,8.274945,-2.288017,-8.183620,0.552544,3.203469,3.938355,-5.632506,1.774859,7.933214,-7.298660,-0.626788,3.488938,-6.463334,-4.074474,-0.616527,-7.132163,2.942249,6.600238,-7.728700,-2.524435,7.316220,-5.990402,4.509447,-9.319842,-0.489062,-0.382566,9.312530,-6.068304,-7.321006,-8.994261,-5.367672,-7.799767,-7.185263,1.218538,-2.573562,-4.936077,-2.337894,2.459421,-0.591093,-2.411385,-0.656723,8.043167,3.372252,0.272969,-7.770811,-3.997834,-2.915074,-7.885350,-8.466815,4.269934,-5.656934,-4.309234,5.523100,-0.082646,-3.521986,-3.933719,-8.664714,-3.723813,5.877589,4.795081,-1.668255,7.592966,0.244560,9.207374,6.657245,-8.478922,-1.531970,-0.940509,6.305276,2.120050,-5.404069,-9.905548,4.842612,-9.228465,7.948763,-5.582299,4.636581,-8.686643,-2.293183,-7.033657,3.284176,7.791035,-9.881946,7.678846,-1.666180,0.832450,-3.397027,1.359422,-9.144596,4.617527,-7.444056,1.830118,6.645628,-2.668992,4.586232,9.306746,2.326297,-6.715438,4.785309,7.291432,-2.470242,-0.767893,1.323288,-9.301955,3.823562,8.489133,-4.533088,9.991868,-0.487932,7.269014,-0.888162,-8.447536,3.721783,6.464570,-5.496156,-4.622404,2.023405,-2.399515,1.850519,4.980773,-3.264333,-8.119036,0.109862,-5.792859,2.442399,-4.108764,-4.437133,6.185225,2.736036,-8.371433,-1.535979,7.338016,9.132038,-1.547641,-9.019407,0.727205,-1.915288,1.140247,8.090335,9.528107,6.521764,6.360375,4.701349,5.952299,1.041020,-4.952989,7.946049,-7.625006,2.834370,9.670470,-3.513027,-1.529225,-4.522679,-7.776260,5.378862,-9.053960,7.970129], dtype = "float32")#candidate|5120|(1540,)|const|float32
call_5119 = func_3043_call(relay.reshape(const_5120.astype('float32'), [7, 220]))
call_5121 = func_3043_call(relay.reshape(const_5120.astype('float32'), [7, 220]))
output = relay.Tuple([call_5109,call_5119,const_5120,])
output2 = relay.Tuple([call_5110,call_5121,const_5120,])
func_5127 = relay.Function([], output)
mod['func_5127'] = func_5127
mod = relay.transform.InferType()(mod)
output = func_5127()
func_5128 = relay.Function([], output)
mutated_mod['func_5128'] = func_5128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4355_call = mod.get_global_var('func_4355')
func_4357_call = mutated_mod.get_global_var('func_4357')
call_5156 = relay.TupleGetItem(func_4355_call(), 0)
call_5157 = relay.TupleGetItem(func_4357_call(), 0)
func_926_call = mod.get_global_var('func_926')
func_929_call = mutated_mod.get_global_var('func_929')
var_5170 = relay.var("var_5170", dtype = "float32", shape = (1540,))#candidate|5170|(1540,)|var|float32
call_5169 = relay.TupleGetItem(func_926_call(relay.reshape(var_5170.astype('float32'), [1540,])), 1)
call_5171 = relay.TupleGetItem(func_929_call(relay.reshape(var_5170.astype('float32'), [1540,])), 1)
func_1972_call = mod.get_global_var('func_1972')
func_1978_call = mutated_mod.get_global_var('func_1978')
var_5178 = relay.var("var_5178", dtype = "float32", shape = (180,))#candidate|5178|(180,)|var|float32
var_5179 = relay.var("var_5179", dtype = "int8", shape = (10368,))#candidate|5179|(10368,)|var|int8
const_5180 = relay.const([[7,-10,-1,-10,6,-1,4,-2,-10,3,1,-9,8,-10,7,4,-1,10,5,5,1,-6,5,4,-7,1,3,-2,6,-7,7,-9,-6,-2,-3,4,-7,7,-8,-9,7,2,-2,3,6,2,-1,-4,2,-10,7,8,-4,-7,-5,-7,8,4,-2,7,7,3,-4,7,-7,10,-10,-9,3,-9,2,-3,-3,-10,4,-5,1,-2,-7,1,-5,7,9,-2,-1,3,6,6,2,4,-7,8,-7,1,9,-9,2,10,1,6,-2,7,-4,7,1,2,2,-4,-10,4,-8,2,8,-5,-5,-1,9,-6,3,9,-7,-9,-8,-8,1,-8,5,-1,3,2,-9,8,2,-1,7,8,10,3,-2,6,2,-2,-5,2,1,7,-6,7,7,3,-9,-10,-8,-7,-5,-6,9,6,3,2,-9,-5,4,-4,-2,-8,8,10,-2,-8,1,4,2,-4,9,10,-6,4,6,10,-5,-9,-6,-10,-7,5,-2,6,2,-10,7,-8,4,-1,-2,-8,-1,1,-7,8,-9,2,6,7,9,7,-9,6,-9,-6,10,-7,3,8,8,4,1,-1,3,4,-7,-5,-10,-2,8,9,1,8,-3,-4,4,-8,-5,3,9,9,10,4,6,8,-3,-3,10,-10,8,4,5,7,1,7,7,5,3,7,5,-5,-10,-7,-10,5,-3,1,1,8,-10,-1,3,4,5,-5,-9,-3,9,-3,-6,-8,-9,7,-7,-1,9,3,8,-8,-1,5,1,10,7,8,2,-2,-5,9,3,-6,-4,4,8,-6,5,8,-9,-6,2,10,2,-2,-3,8,3,-10,-4,-8,6,-1,5,-9,-10,3,-10,3,-6,-10,8,-5,-1,5,-9,8,-6,8,-10,6,-1,1,1,-5,9,-4,-3,-7,3,-10,4,8,8,-1,-3,8,5,5,-1,3,-6,-8,-7,3,-6,2,4,-10,-8,-9,-8,-6,4,9,2,9,8,-8,10,-4,-6,-6,10,3,9,-10,-10,-1,8,2,-1,-1,-8,-5,10,-5,-10,7,9,8,1,-4,-4,5,-5,3,10,9,3,-8,-5,-9,6,-5,-5,2,2,-7,10,-10,1,-3,9,10,-5,-5,1,-7,10,-1,-6,-1,8,-5,-1,5,8,6,-1,-7,3,9,6,1,10,8,-5,-4,-8,3,-2,5,8,5,-8,-6,-6,6,-2,5,9,8,6,-8,1,-6,-10,2,2,5,-2,10,-7,10,-3,3,-8,-7,3,9,-7,-4,7,2,5,-1,10,7,-8,-9,9,5,3,4,-7,7,-1,10,-8,9,-2,2,-10,3,3,-8,-6,-2,5,4,-10,-6,5,-8,10,8,-6,6,-9,-5,-1,-7,-6,-3,-6,4,9,8,8,6,-5,-10,5,8,-4,-8,-6,1,3,-4,2,-8,10,4,-4,-5,-5,8,10,-3,9,-9,-6,8,4,-2,-9,-7,6,6,10,-7,-6,-4,-2,-1,10,-7,-10,-10,6,1,10,-6,-7,-4,-4,3,-7,6,-6,10,9,-4,2,-3,6,6,10,-2,-4,6,-9,-8,6,6,5,7,3,2,7,-4,7,-9,-1,6,9,-5,-8,3,-9,5,-4,7,-4,-3,-2,4,-6,-8,3,-6,5,9,4,-9,-2,6,-7,-5,2,3,-4,5,9,-1,-9,-5,6,-2,-7,-5,7,8,6,8,1,4,-10,7,4,2,-5,-10,10,-3,-2,9,-2,5,8,6,5,-5,8,-2,10,-8,10,7,-1,-10,-1,-4,4,8,1,1,3,8,-8,6,8,-4,-3,10,-3,8,-7,-6,-10,-5,10,8,4,5,-8,-1,-4,-5,-9,-10,5,-6,-10,5,9,-2,8,2,-6,3,7,-10,-10,-9,-2,-1,7,-3,-2,-7,-10,9,9,-7,8,10,-5,-6,7,-6,-4,-8,-6,8,-9,10,3,7,-1,-8,-4,4,-9,6,6,5,-9,-1,-3,-7,-3,2,-8,-10,3,8,6,-9,-2,1,7,8,-8,-4,-9,1,-10,7,-2,-9,-5,-2,-10,-6,-8,-2,2,2,10,-8,7,-10,2,6,-4,-9,-3,2,4,6,4,6,8,3,-3,9,-10,-8,-6,-8,-1,-1,-8,8,2,3,-1,-1,6,-9,5,-9,-4,-9,3,-3,6,7,-7,-7,8,-5,10,8,-10,-3,4,1,-10,10,-10,6,-7,2,-9,-4,-1,-7,-5,-5,3,-1,1,-7,-4,4,2,-2,6,-4,2,-3,-9,4,-5,-10,-8,-5,4,-1,1,-4,7,1,-1,10,4,-8,4,-8,8,9,-10,-6,8,-3,-3,1,3,3,10,-9,7,-9,7,1,-7,3,5,-2,-5,4,-1,7,-1,-2,-6,-5,-8,3,6,-1,4,-2,3,4,10,5,-4,-9,-5,-6,-10,1,9,-3,9,8,10,-4,8,1,7,1,-10,-6,1,-5,3,9,1,-7,-8,6,6,10,-8,-2,-7,-8]], dtype = "int16")#candidate|5180|(1, 936)|const|int16
const_5181 = relay.const([-8.510951,-8.951742,-7.349598,-9.150504,5.103918,-7.725017,7.039411,5.046563,4.297612,9.835293,-8.090441,1.255392,-8.051527,4.093693,-2.349832,7.199651,3.863405,0.544036,-7.570042,-6.501953,-7.627645,3.590721,-0.977088,2.089209,-9.581092,-4.813137,-6.563718,-3.546647,5.494645,1.420457,1.298613,-0.797759,-3.044723,-4.956508,-3.734965,-5.988970,-3.881647,-3.181223,9.724372,-9.043251,-2.957476,-1.884589,-5.740070,-6.892859,-2.291629,6.970218,-3.682276,-4.801517,5.359036,5.593365,9.103970,-9.875780,0.937852,-1.732832,-3.274763,9.510574,4.475689,-7.760680,-6.947713,-9.870117,-7.892230,-6.777873,7.522491,7.962270,7.231997,-4.699808,-3.596495,-7.994955,5.087014,-6.223675,5.038467,3.616265,5.536980,-0.794726,-8.829423,-3.674358,-7.541333,8.973658,3.665138,4.505198,-5.160252,-6.841807,-0.654101,-6.021855,2.416157,-6.121495,-0.329124,-9.614156,9.703206,2.144917,5.928149,-7.637047,-1.716440,5.263703,-0.001446,6.610195,7.620272,8.938281,-3.358250,6.184540,8.611125,2.383039,8.219270,1.401014,-7.266175,-5.811745,6.491328,-0.972852,9.093760,0.526543,-7.727631,-5.348245,-1.806357,0.175313,2.863975,7.956823,-9.954077,7.204966,-8.212057,-5.739009,6.224859,-2.404011,9.617432,3.242248,-0.218793,-5.567508,1.666684,-1.742139,7.027155,-6.420279,6.828764,4.675289,-1.442658,9.045714,0.684713,-8.673828,5.202316,7.523484,6.706134,0.215662,-6.790953,-8.111281,-5.971160,9.850163,-4.789139,-0.412937,9.500388,-0.999127,-8.222939,-5.873205,9.747137,5.888301,8.971606,-6.662562,8.281855,3.527707,7.868363,1.891968,-6.840004,8.126815,-1.233480,-0.768928,8.299202,-2.473507,0.650158,-2.683314,1.853184,9.978772,-0.825934,3.049933,2.592625,8.271990,-4.339424,-8.883948,-2.037891,4.355243,3.350493,-1.103783,-3.858149,0.775568,-5.812513,6.739426,1.308499,-9.926518,-7.597834,7.388198,-8.327408,-7.117844,4.695636,-3.350482,9.859273,-4.526601,7.828144,4.184768,7.468993,5.164160,-5.496645,4.455733,4.946088,-6.879969,7.079486,9.954620,-5.350855,-9.350912,-3.484749,0.277799,3.603433,0.553787,9.708074,-1.739935,4.284152,-1.811039,-8.898185,6.311728,0.620068,7.617087,1.560303,9.826926,1.950865,0.739234,-1.474457,6.523794,-6.430408,-8.022943,0.722108,6.890589,6.170014,5.203270,7.815433,9.760928,-8.793254,-8.082606,-4.626492,1.199161,7.518409,7.242824,-4.004445,9.605589,3.125513,-3.275133,2.759624,7.302232,3.526782,-2.006543,5.277420,1.674996,1.638138,4.598047,7.543543,9.131918,9.644998,-7.877060,7.173994,8.229614,-0.199146,4.473584,5.220000,-6.313794,5.340569,0.251632,-1.691815,-5.522170,-7.721364,5.591526,9.311082,6.280902,-7.908847,-2.291137,0.939038,-4.583008,4.282701,5.495100,9.186180,3.438883,6.814656,5.930514,1.777618,8.355579,-8.425752,-1.012891,6.573287,-3.353367,6.830484,5.186847,-0.565994,-0.248403,2.149787,-8.805578,1.905582,-8.762310,4.345139,3.997687,4.819903,-6.399023,5.853114,6.110633,-3.221861,-7.825523,-1.713171,4.220503,-9.567278,-4.732765,4.412646,-4.631742,-1.236332,7.023805,-9.017003,0.955195,1.419056,6.508092,-5.752430,8.537469,8.827669,-1.593889,3.179181,-2.718701,-3.785027,-0.746644,-8.745950,-4.894709,9.856542,-8.142885,-7.963840,2.450578,7.110903,4.473713,-1.567803,6.270535,-5.580430,2.347503,9.828808,1.303271,0.531783,0.293071,-8.300716,-6.309964,-9.620319,-6.107083,-3.276972,-4.867808,-3.710883,6.109926,2.440927,-9.251842,4.859564,8.151226,-6.137190,-0.110784,-0.679046,5.103516,9.698686,-3.185570,-3.336970,1.820402,1.131137,-1.408833,1.743244,-3.405965,-3.622804,-3.453700,-9.112871,-5.069775,4.509777,-4.534989,0.790034,-4.757813,-3.404689,-2.732536,9.446145,6.782470,4.234676,5.345926,-7.731596,3.778159,-5.221166,-1.470576,-9.346451,0.875771,2.648733,9.508035,5.060006,1.643185,8.597665,-7.652521,6.384766,8.304966,-6.191368,9.566476,-1.442466,3.908550,5.570408,8.044653,4.115485,8.444736,6.736538,8.283194,-9.566420,-7.612534,-4.671615,0.584321,-4.404406,-9.876694,3.293307,2.880322,6.887831,-2.821773,-9.482637,-4.356936,1.556911,-7.624888,-4.070039,1.574015,7.630191,-3.587198,4.093884,3.717332,-8.239604,-3.850351,-1.470667,4.300759,-9.725623,-6.206835,-7.513906,-3.799915,-2.636034,-2.954670,-9.496703,6.841897,1.317315,4.115348,8.563011,-8.364452], dtype = "float32")#candidate|5181|(432,)|const|float32
call_5177 = relay.TupleGetItem(func_1972_call(relay.reshape(var_5178.astype('float32'), [4, 9, 5]), relay.reshape(var_5179.astype('int8'), [10368,]), relay.reshape(const_5180.astype('int16'), [936,]), relay.reshape(const_5181.astype('float32'), [4, 9, 12]), ), 8)
call_5182 = relay.TupleGetItem(func_1978_call(relay.reshape(var_5178.astype('float32'), [4, 9, 5]), relay.reshape(var_5179.astype('int8'), [10368,]), relay.reshape(const_5180.astype('int16'), [936,]), relay.reshape(const_5181.astype('float32'), [4, 9, 12]), ), 8)
func_4985_call = mod.get_global_var('func_4985')
func_4987_call = mutated_mod.get_global_var('func_4987')
call_5183 = relay.TupleGetItem(func_4985_call(), 0)
call_5184 = relay.TupleGetItem(func_4987_call(), 0)
var_5185 = relay.var("var_5185", dtype = "float32", shape = (4, 9, 10368))#candidate|5185|(4, 9, 10368)|var|float32
bop_5186 = relay.mod(call_5177.astype('float64'), relay.reshape(var_5185.astype('float64'), relay.shape_of(call_5177))) # shape=(4, 9, 10368)
bop_5189 = relay.mod(call_5182.astype('float64'), relay.reshape(var_5185.astype('float64'), relay.shape_of(call_5182))) # shape=(4, 9, 10368)
output = relay.Tuple([call_5156,call_5169,var_5170,var_5178,var_5179,const_5180,const_5181,call_5183,bop_5186,])
output2 = relay.Tuple([call_5157,call_5171,var_5170,var_5178,var_5179,const_5180,const_5181,call_5184,bop_5189,])
func_5195 = relay.Function([var_5170,var_5178,var_5179,var_5185,], output)
mod['func_5195'] = func_5195
mod = relay.transform.InferType()(mod)
mutated_mod['func_5195'] = func_5195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5195_call = mutated_mod.get_global_var('func_5195')
var_5197 = relay.var("var_5197", dtype = "float32", shape = (1540,))#candidate|5197|(1540,)|var|float32
var_5198 = relay.var("var_5198", dtype = "float32", shape = (180,))#candidate|5198|(180,)|var|float32
var_5199 = relay.var("var_5199", dtype = "int8", shape = (10368,))#candidate|5199|(10368,)|var|int8
var_5200 = relay.var("var_5200", dtype = "float32", shape = (4, 9, 10368))#candidate|5200|(4, 9, 10368)|var|float32
call_5196 = func_5195_call(var_5197,var_5198,var_5199,var_5200,)
output = call_5196
func_5201 = relay.Function([var_5197,var_5198,var_5199,var_5200,], output)
mutated_mod['func_5201'] = func_5201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5127_call = mod.get_global_var('func_5127')
func_5128_call = mutated_mod.get_global_var('func_5128')
call_5252 = relay.TupleGetItem(func_5127_call(), 1)
call_5253 = relay.TupleGetItem(func_5128_call(), 1)
func_3523_call = mod.get_global_var('func_3523')
func_3524_call = mutated_mod.get_global_var('func_3524')
call_5270 = func_3523_call()
call_5271 = func_3523_call()
var_5276 = relay.var("var_5276", dtype = "float32", shape = (7, 220))#candidate|5276|(7, 220)|var|float32
bop_5277 = relay.logical_xor(call_5252.astype('uint64'), relay.reshape(var_5276.astype('uint64'), relay.shape_of(call_5252))) # shape=(7, 220)
bop_5280 = relay.logical_xor(call_5253.astype('uint64'), relay.reshape(var_5276.astype('uint64'), relay.shape_of(call_5253))) # shape=(7, 220)
uop_5286 = relay.tan(bop_5277.astype('float64')) # shape=(7, 220)
uop_5288 = relay.tan(bop_5280.astype('float64')) # shape=(7, 220)
uop_5289 = relay.acos(var_5276.astype('float64')) # shape=(7, 220)
output = relay.Tuple([call_5270,uop_5286,uop_5289,])
output2 = relay.Tuple([call_5271,uop_5288,uop_5289,])
func_5293 = relay.Function([var_5276,], output)
mod['func_5293'] = func_5293
mod = relay.transform.InferType()(mod)
mutated_mod['func_5293'] = func_5293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5294 = relay.var("var_5294", dtype = "float32", shape = (7, 220))#candidate|5294|(7, 220)|var|float32
func_5293_call = mutated_mod.get_global_var('func_5293')
call_5295 = func_5293_call(var_5294)
output = call_5295
func_5296 = relay.Function([var_5294], output)
mutated_mod['func_5296'] = func_5296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4757_call = mod.get_global_var('func_4757')
func_4758_call = mutated_mod.get_global_var('func_4758')
call_5327 = func_4757_call()
call_5328 = func_4757_call()
var_5329 = relay.var("var_5329", dtype = "float32", shape = (4, 9, 4))#candidate|5329|(4, 9, 4)|var|float32
bop_5330 = relay.power(call_5327.astype('float32'), var_5329.astype('float32')) # shape=(4, 9, 4)
bop_5333 = relay.power(call_5328.astype('float32'), var_5329.astype('float32')) # shape=(4, 9, 4)
bop_5345 = relay.greater(var_5329.astype('bool'), call_5327.astype('bool')) # shape=(4, 9, 4)
bop_5348 = relay.greater(var_5329.astype('bool'), call_5328.astype('bool')) # shape=(4, 9, 4)
func_5293_call = mod.get_global_var('func_5293')
func_5296_call = mutated_mod.get_global_var('func_5296')
const_5359 = relay.const([[-6.725930],[7.940692],[-4.338317],[-9.686875],[6.983727],[4.745560],[-3.955115],[-7.043919],[3.155961],[-2.505142],[0.581623],[-5.619824],[4.448849],[7.228477],[2.737085],[-4.877675],[8.283661],[-8.281209],[5.697137],[6.436332],[-7.373213],[0.661363],[0.561334],[6.837935],[8.013626],[-7.388673],[-0.283800],[-2.045502],[-0.118318],[4.202661],[4.973271],[9.514754],[5.468397],[9.018299],[3.571904],[8.974821],[7.028434],[-7.919249],[-2.745257],[1.462105],[-5.554996],[-3.732505],[-8.755302],[-7.976157],[-4.297613],[1.900872],[6.188787],[9.592812],[-7.834496],[9.047333],[3.391110],[8.625127],[8.523490],[2.696148],[-3.583543],[2.597200],[7.970586],[8.904094],[-0.344264],[-6.852249],[-5.646572],[9.688946],[3.763640],[-0.034614],[5.488224],[0.612620],[6.674805],[8.745736],[-9.951274],[-1.307838],[8.146687],[1.503910],[-9.443927],[1.156705],[-5.674227],[2.445668],[4.925458],[-1.968656],[9.473679],[-3.177545],[-9.627621],[-2.559933],[-0.339864],[0.603946],[-7.747494],[2.812414],[5.372185],[-8.492002],[-9.502339],[2.667276],[-6.958119],[2.674423],[0.103975],[-4.521796],[-7.571555],[5.457418],[-0.893252],[-2.989273],[2.405406],[2.132868],[-5.291844],[4.317763],[-8.863878],[2.444235],[5.262996],[9.157694],[2.099647],[1.580243],[8.861765],[-8.444951],[-1.610501],[-6.822795],[5.640847],[-4.187688],[-5.180707],[-9.459898],[-0.660905],[7.580202],[-1.461200],[4.712828],[3.010368],[2.224365],[7.128174],[4.812568],[-9.236413],[4.084276],[7.197714],[7.543654],[-2.166241],[1.779480],[1.409359],[4.083247],[7.278373],[-6.309148],[2.105199],[-8.609357],[4.500923],[-7.793376],[-5.739021],[4.824256],[3.031748],[-1.595525],[-3.500762],[4.044434],[1.315901],[-7.572350],[-5.407248],[-5.945386],[-9.280618],[5.570390],[7.269077],[-2.179182],[9.021057],[1.496628],[-7.564540],[-0.197334],[7.997847],[-1.167292],[-7.012048],[4.374353],[-1.770111],[1.538988],[1.562555],[-4.569951],[-1.379301],[-9.210745],[3.597726],[-6.638651],[0.309408],[9.635764],[-7.738820],[7.890470],[-4.327901],[-3.080863],[3.746797],[-9.380283],[0.527992],[-1.575874],[4.074445],[-0.030082],[6.466941],[1.817566],[5.659850],[8.000043],[-0.835085],[-2.853711],[4.270117],[-1.203838],[3.027835],[-3.516053],[-8.555255],[-0.555650],[-0.089355],[3.725303],[6.652387],[-1.954432],[-8.026734],[-4.138734],[2.704499],[-5.515197],[-2.280126],[2.976788],[-4.063418],[4.647217],[-7.118536],[-5.379034],[-6.984966],[-7.905671],[2.777905],[-2.773336],[4.822372],[9.879010],[4.088035],[6.511214],[-4.566511],[-6.622198],[-7.369066],[-5.724486],[4.088519],[-4.580223],[0.229974],[5.525145],[0.410220],[6.379176],[5.991807],[9.635919],[-1.047766],[-6.574950],[-0.848498],[-6.330485],[8.441390],[9.742340],[-4.758030],[-6.301034],[0.353835],[5.138884],[9.927856],[-1.557002],[-8.966834],[0.495889],[-7.484530],[-6.345536],[-4.072432],[-9.993407],[-7.254647],[3.318554],[4.306140],[4.464319],[-8.435487],[2.002175],[-6.375139],[-3.505854],[2.688652],[-6.099757],[-3.153915],[8.970101],[4.343088],[6.555440],[-2.232491],[-6.074600],[9.515077],[-0.875613],[9.226223],[-3.569607],[8.621914],[3.216507],[0.788437],[2.398709],[7.358062],[-2.706786],[-5.008373],[-6.490203],[-2.551261],[1.052677],[1.549186],[8.436925],[5.402745],[5.331795],[-3.557937],[-2.245942],[0.327186],[6.024193],[3.167138],[-9.081196],[8.490119],[9.565580],[-6.606445],[2.883037],[9.136739],[-8.933527],[-4.549322],[6.566165],[8.320122],[-3.924278],[6.028557],[-8.169707],[6.820032],[8.941925],[-3.268313],[7.449740],[-6.330732],[4.230955],[-4.018132],[6.746857],[5.310595],[-0.073745],[-1.779568],[5.958974],[-1.565672],[8.835915],[-4.047051],[-8.636897],[4.371340],[6.681705],[5.190166],[3.549647],[9.960733],[7.233187],[2.902843],[7.454666],[-1.702013],[1.869278],[-2.006335],[-0.479448],[-1.616518],[-3.571790],[4.103639],[-3.279293],[-7.218615],[4.976882],[-8.286046],[0.145621],[7.827274],[4.216136],[-6.511032],[-6.574277],[-6.520624],[3.192524],[-1.258706],[6.374835],[3.204007],[-0.442862],[3.481824],[9.710917],[-4.580393],[9.967491],[-5.552140],[-0.959837],[4.143380],[-3.802153],[-7.048055],[-4.848922],[-5.331890],[1.072042],[-5.251188],[-1.455959],[-0.240141],[-2.673996],[3.387768],[0.238352],[-8.894785],[9.791870],[-4.246113],[7.979018],[6.303030],[2.495553],[-3.454765],[8.666002],[8.476362],[7.051955],[1.035828],[7.682061],[-9.650284],[7.116092],[2.675169],[0.545694],[-2.507654],[-4.343184],[-7.019283],[-6.113280],[-8.237863],[-4.311085],[-5.003341],[6.536411],[-4.718452],[6.483540],[-0.341601],[-3.344503],[-8.745476],[5.506032],[-4.668862],[-9.842195],[6.243159],[9.598941],[-9.966113],[9.759296],[4.553606],[4.820650],[0.310617],[0.009224],[2.095011],[-2.686145],[3.100550],[6.555686],[-1.351719],[-8.970470],[4.838039],[5.970485],[0.194472],[4.835714],[0.836667],[-2.320504],[-1.001685],[-9.686648],[2.360482],[4.045053],[-5.379885],[-3.581200],[-1.511601],[5.573240],[-6.846204],[-4.568825],[-7.308311],[-0.377803],[-8.277019],[2.214709],[0.106872],[6.109571],[0.054395],[4.103333],[7.944815],[-3.658835],[-1.584253],[-6.915733],[-0.360625],[-2.356810],[9.307743],[-0.173349],[-6.444496],[4.503884],[-2.623821],[-6.932202],[8.355645],[5.335604],[1.107706],[9.052386],[-7.806363],[-7.578698],[-2.950410],[5.102729],[1.331741],[-9.340375],[-1.670633],[-9.385692],[1.213679],[-2.580781],[6.707585],[6.507056],[-1.850536],[3.991331],[-4.551419],[-7.276205],[-3.478662],[9.903260],[8.135654],[5.341756],[-8.370295],[3.720479],[3.001913],[-4.399183],[-6.963651],[-7.263331],[4.455560],[-6.139985],[2.587350],[-7.155338],[-4.449574],[-6.395326],[0.018456],[0.280584],[-5.002356],[8.916935],[-8.859812],[-6.491889],[3.878323],[3.469462],[4.417609],[4.621987],[1.221738],[-8.413082],[2.777513],[-9.279339],[5.240890],[0.342969],[2.499924],[-3.942140],[3.137542],[-4.417342],[-1.788017],[3.468497],[2.528591],[8.388668],[5.870919],[-4.360462],[-4.663640],[1.405787],[3.822186],[3.827515],[-3.059475],[8.775399],[-8.304089],[1.185464],[-5.332432],[2.246189],[-1.446132],[-4.225962],[0.862487],[-9.597804],[-8.824781],[-3.420859],[5.488045],[-8.976412],[7.135829],[-1.532847],[-6.675508],[4.062347],[7.766630],[0.730324],[7.058494],[-9.909283],[6.137884],[6.968831],[2.387799],[5.228539],[-5.219170],[-6.507657],[0.352198],[-1.929636],[9.500453],[-0.237104],[6.211751],[-2.707927],[7.653059],[-1.539338],[-0.110772],[-6.961724],[2.551632],[6.511145],[-6.047396],[-6.389478],[-0.127414],[-2.313345],[6.866023],[-3.739950],[8.512686],[0.691818],[2.496946],[4.949580],[3.269681],[2.418810],[5.208042],[9.566827],[5.833819],[0.082979],[-4.013185],[5.466870],[-4.006333],[-9.284166],[-3.991849],[-5.651689],[-8.246593],[-2.473560],[2.195293],[-5.384533],[6.083464],[4.590550],[8.057273],[9.344086],[0.190520],[-3.210845],[-6.306579],[-3.197009],[-6.600192],[9.112899],[2.390661],[-1.022980],[2.289179],[4.607812],[8.058210],[3.662049],[7.484160],[7.346322],[9.005656],[-8.309227],[4.229194],[-8.193413],[-5.712333],[-5.286672],[-1.877489],[2.221054],[-2.843154],[6.392017],[6.608609],[-1.000343],[-8.078717],[5.454848],[-4.832076],[-7.746057],[-6.527396],[-1.382692],[-3.225799],[2.265396],[9.074696],[1.343870],[4.878174],[-8.547490],[-0.160176],[0.601415],[-4.402986],[-2.334830],[7.275691],[7.097947],[-0.729018],[-5.174729],[-3.480370],[-0.777515],[3.444468],[4.144742],[-2.825140],[-2.830477],[6.054012],[4.530637],[-0.221656],[8.527489],[-3.246656],[2.545245],[-6.271326],[-2.714568],[8.439722],[5.080698],[5.321419],[-5.607578],[3.267272],[-5.560350],[-6.864391],[-4.047560],[3.894889],[5.875911],[-4.690199],[-0.090780],[7.209391],[8.849124],[-1.491534],[-3.265504],[-5.504293],[5.214153],[-2.167188],[-5.445524],[6.800292],[5.690902],[-4.614830],[-8.692899],[7.566161],[7.973563],[-2.913184],[-6.068036],[-6.728027],[3.667804],[0.678442],[-5.862367],[4.469469],[-9.374525],[7.199712],[-5.164980],[7.258866],[-5.695083],[7.663987],[1.817836],[-1.734895],[-9.465990],[-6.113443],[-2.134111],[-8.624324],[-2.703188],[-2.396546],[1.721885],[-6.536335],[7.705408],[5.098817],[0.855814],[9.315251],[-9.528867],[-6.270201],[7.235491],[-2.067733],[4.988248],[-8.961695],[0.428008],[-6.926692],[4.508176],[-9.658127],[-7.223780],[-9.312318],[-3.524897],[7.937145],[-1.153566],[1.029173],[1.072072],[-8.211972],[6.409562],[3.031669],[4.881569],[-7.022064],[-5.129362],[-8.063126],[4.254292],[6.616813],[-4.189823],[2.219698],[8.203362],[-0.141509],[3.032382],[-3.281454],[8.230134],[2.453313],[6.248459],[3.876963],[7.519919],[-3.320265],[-4.976840],[7.884746],[9.797002],[-9.270529],[-4.302349],[2.772236],[-8.572277],[2.443048],[1.697560],[3.101041],[-7.414351],[3.110193],[8.523517],[-0.313665],[7.058107],[-6.540958],[-5.449077],[3.195602],[-8.646923],[9.335242],[-2.514152],[-7.979123],[-9.162551],[-5.270439],[2.587669],[-3.297293],[3.235530],[-6.136321],[-5.983149],[4.099006],[6.186858],[-8.202042],[9.200605],[2.925287],[2.598972],[-1.317578],[9.717200],[-6.807599],[-1.482427],[-4.488759],[-5.320148],[9.572826],[-6.920784],[-8.681488],[-7.709368],[-3.526913],[-0.901876],[9.784516],[3.117945],[9.186582],[1.166317],[-7.853065],[1.993448],[-3.554785],[0.493521],[0.590789],[5.199108],[2.796042],[-8.345714],[7.015094],[2.829404],[-7.295905],[-3.806180],[6.850382],[5.364413],[-9.879513],[-0.059708],[1.110707],[3.244423],[4.448689],[-4.303825],[9.506978],[8.270824],[-3.651409],[-7.248380],[4.944695],[9.748615],[3.915206],[2.713536],[8.350054],[-4.782067],[-5.053977],[-9.630550],[-8.273298],[5.762798],[7.387567],[-3.764099],[-4.533328],[3.236579],[-3.959246],[-4.868318],[-2.380570],[9.596721],[8.573946],[-0.167893],[1.838024],[-8.537123],[-6.785122],[-0.371202],[-3.849558],[-5.891813],[6.259881],[-6.595711],[6.171290],[-4.981589],[-4.316893],[7.118436],[1.512994],[-4.560608],[6.494467],[4.193743],[7.350475],[-6.678025],[2.309621],[-4.213180],[1.584662],[7.376200],[-0.807362],[-8.493215],[1.371528],[9.647833],[0.477874],[-5.392325],[2.751202],[1.968776],[-1.784504],[-8.824839],[-5.653061],[5.872253],[1.986020],[1.337613],[-2.785450],[7.247819],[1.339079],[-5.714258],[0.729199],[-4.337956],[-1.546666],[7.247961],[9.482596],[8.555107],[9.476645],[-8.967923],[-1.300199],[4.151361],[1.129200],[-2.170363],[7.590505],[-5.087570],[3.198495],[-1.360280],[-1.219130],[8.374190],[8.146638],[1.748120],[0.473595],[-8.323482],[-3.614899],[-3.816127],[-1.869651],[-7.721067],[5.576369],[-6.999482],[-1.530099],[6.695611],[7.037071],[-8.984231],[-9.956379],[3.286000],[-9.862680],[-7.046904],[3.226385],[6.561431],[5.527744],[-6.840870],[1.825777],[-9.761236],[-7.178892],[-8.757033],[0.619551],[-6.276246],[9.837644],[7.914986],[8.191176],[1.323180],[4.570082],[3.793654],[0.804101],[-7.337721],[1.101819],[-6.338960],[2.135094],[2.788688],[1.950507],[-6.325042],[2.533412],[-6.503952],[-3.335560],[-6.940429],[-1.695908],[4.875530],[6.508099],[-3.226082],[5.682327],[-8.025257],[6.063281],[-1.674992],[1.060883],[-3.184442],[5.696159],[0.559846],[-6.611138],[9.430074],[4.345599],[-8.676401],[7.633223],[2.781131],[-6.449575],[7.799955],[-3.876622],[-4.241949],[5.691286],[-6.996197],[-0.393187],[8.988435],[-3.888267],[-8.392938],[-7.156444],[6.853255],[7.430179],[9.135165],[3.184429],[-7.697803],[-8.413951],[-9.488874],[9.559305],[8.937898],[6.984975],[9.571232],[-0.707247],[6.093866],[6.289691],[2.839235],[5.897958],[-1.734895],[-8.282586],[0.503063],[-6.869965],[-0.106436],[-5.393646],[-3.492442],[5.648864],[-1.071037],[2.830688],[5.150907],[-9.638321],[-3.573788],[-8.594127],[-2.175048],[-7.920930],[1.370844],[-5.181923],[8.560739],[-3.774634],[-8.386125],[-6.395445],[-7.852174],[-2.217863],[-8.965451],[-7.447620],[7.726231],[-7.123828],[-2.423961],[-9.822004],[-8.299956],[2.726470],[4.864357],[-2.234848],[2.289190],[-6.814731],[6.812085],[-0.181848],[4.624012],[-0.898842],[-0.892657],[0.953975],[-6.600061],[-3.069332],[-1.133599],[0.044434],[0.232359],[-6.622194],[-3.225151],[1.910845],[0.043028],[9.588570],[-0.644783],[-0.006559],[-3.849057],[5.025080],[1.473378],[5.730090],[-2.517713],[7.185755],[-2.709972],[9.554284],[2.868154],[-0.279115],[0.248998],[1.838790],[-6.961099],[7.743317],[-3.192859],[-2.284003],[2.804437],[-4.160578],[-9.963516],[-4.586393],[2.636124],[3.830697],[-2.628611],[4.122832],[5.106581],[0.520151],[-7.602057],[3.613311],[-4.649065],[4.343220],[0.235238],[7.368705],[-7.615010],[7.463159],[5.370035],[1.695464],[8.908132],[-4.452092],[-6.682847],[-8.870963],[-8.693729],[-7.114683],[-4.677228],[1.139246],[-6.373544],[-6.941774],[-5.756846],[-9.642305],[4.195080],[8.048104],[9.234522],[4.356118],[5.477493],[-3.091163],[7.107590],[3.525941],[9.528235],[-7.301199],[-5.270458],[-3.959522],[7.557950],[-9.774907],[-6.612695],[-5.360569],[-5.259837],[2.109354],[-3.245660],[1.089386],[-0.857687],[3.389592],[-8.095325],[2.050933],[-5.469504],[4.146521],[0.177602],[-7.119564],[-3.792819],[-8.224118],[8.087607],[-1.974524],[-3.283738],[-4.220239],[-2.913304],[6.954482],[1.208692],[7.968160],[7.777005],[4.217229],[-8.441362],[-7.504404],[-2.279426],[-7.879560],[9.091304],[-6.620585],[3.797929],[2.819569],[-1.164414],[6.856617],[6.547554],[8.501411],[0.269870],[-8.174606],[-3.925049],[2.289537],[-3.268176],[-4.630721],[-7.315991],[-2.055889],[-0.710325],[-8.193416],[7.550282],[4.610791],[3.968780],[8.371493],[1.107665],[-6.790992],[1.812681],[-0.441396],[-5.611795],[-4.323764],[1.625151],[-9.923218],[-6.113916],[-7.090828],[6.535686],[-4.419031],[-1.588737],[-5.017285],[-4.376206],[-4.930379],[-2.042528],[8.476304],[8.390303],[4.595227],[8.421132],[-4.133805],[8.181806],[-5.565332],[7.236001],[-8.515009],[0.626446],[-3.712930],[-4.195799],[-2.531146],[-9.580537],[9.085191],[2.761415],[-0.724284],[-9.683034],[-0.820441],[1.778977],[-6.826067],[7.224738],[-0.575721],[5.083537],[1.109995],[-1.854068],[-5.899148],[-4.298880],[5.775680],[0.333010],[-5.542706],[1.955151],[3.242841],[-8.042328],[4.042649],[9.838878],[-6.105782],[-6.392580],[2.904703],[7.328856],[3.753849],[-5.484073],[5.904412],[-4.728500],[5.107869],[8.372487],[-3.708339],[-5.264471],[-8.515616],[7.706176],[7.813840],[5.821741],[-4.231873],[-8.533313],[-4.598889],[-1.277140],[9.544159],[5.825961],[-8.733407],[-2.386719],[-2.778328],[9.138428],[-1.536606],[-0.373611],[-2.911173],[2.181307],[-7.446279],[-6.181920],[-3.915640],[3.093241],[-1.393780],[-2.051261],[-5.700556],[-2.600240],[0.574603],[8.637711],[-5.579748],[-9.108922],[-7.677190],[4.936964],[8.023884],[-3.531628],[-8.295834],[-5.465176],[-3.808684],[9.706829],[9.004107],[-7.402935],[1.642976],[-5.184973],[8.562684],[-5.883918],[-0.879371],[8.340184],[-2.124074],[-7.187160],[5.532632],[7.607999],[3.237950],[-8.454959],[3.218156],[-0.906106],[-1.165777],[7.179954],[-9.747265],[-1.674318],[8.913963],[3.760766],[-1.774047],[-6.137800],[-9.575263],[-2.454395],[-0.974645],[0.309359],[4.632195],[1.742382],[2.671267],[2.192072],[-8.947118],[9.235810],[7.203554],[9.741271],[2.881730],[-4.366475],[9.773997],[-6.220503],[5.189231],[1.506462],[-1.181201],[2.248184],[-8.740252],[4.660923],[4.896325],[8.642472],[9.520968],[-6.622813],[7.802812],[4.014191],[-1.940254],[-6.402086],[-7.328914],[4.524909],[7.208804],[1.464550],[6.034624],[9.087424],[7.318525],[6.608796],[3.305324],[6.563988],[-4.584161],[6.248323],[7.911388],[-5.053593],[2.086271],[2.348627],[7.505967],[1.672420],[0.355619],[-1.314950],[-5.858017],[-0.358648],[-2.611670],[-8.728891],[8.408109],[-4.178465],[6.343257],[8.829845],[-3.389157],[-0.218327],[-9.351348],[-0.428016],[2.125682],[-4.303470],[-8.108459],[0.855658],[-9.566931],[4.438695],[-8.878344],[-5.354579],[1.617826],[3.634915],[5.424804],[8.392335],[-4.894227],[9.854015],[6.502943],[-5.138441],[6.998135],[2.718368],[0.390474],[-9.145162],[-5.257171],[3.335848],[8.128289],[-8.809399],[-6.023383],[6.742018],[-7.270119],[-8.722470],[2.655555],[8.258235],[5.259298],[9.608145],[-4.163323],[-9.568518],[8.410863],[2.503390],[-5.961117],[-9.934532],[1.815933],[-6.274795],[-3.035208],[2.438710],[-9.227856],[2.030858],[8.931145],[-2.318705],[-2.419027],[6.597621],[-6.778088],[4.998575],[1.283446],[-2.713733],[1.627568],[8.201037],[9.378598],[-1.936838],[-5.632049],[2.201317],[8.667358],[-8.384377],[0.970618],[8.324320],[-8.056393],[7.472170],[8.194085],[-1.724576],[3.031772],[-4.582363],[-1.498350],[1.584531],[-3.206918],[8.355470],[4.689946],[9.613218],[-6.144075],[6.102393],[6.193856],[1.287810],[-1.706168],[-1.874971],[6.936516],[-6.044624],[2.748257],[4.120670],[-6.671717],[-0.629701],[4.210739],[4.834946],[-8.138035],[3.233994],[-7.540599],[-7.314184],[-9.168340],[8.417834],[-9.472852],[-3.039322],[0.311473],[7.327977],[9.969253],[-8.284266],[5.717620],[-4.234670],[-3.565148],[-8.318038],[5.806007],[5.034447],[-1.713874],[3.974298],[-2.959183],[4.423626],[-1.431090],[-1.407387],[-5.088723],[7.383593],[6.411684],[-6.678766],[-3.457860],[4.112708],[-0.754574],[5.198467],[6.518722],[-8.181853],[-5.256523],[-3.893603],[-3.804296],[-5.950637],[0.761382],[-4.298112],[-9.224586],[-4.141487],[4.609729],[-6.781611],[9.854917],[8.558808],[8.239494],[6.659352],[8.188395],[8.169920],[0.235992],[-9.162306],[4.724636],[7.978434],[-5.649537],[1.206108],[6.860767],[-9.763875],[-8.354933],[-6.025350],[-6.298438],[1.825775],[-4.751155],[-0.153927],[-3.893981],[8.101135],[-8.939144],[-5.215045],[-4.512629],[-3.582069],[7.086972],[8.327183],[1.251808],[-6.814803],[5.447054],[-2.297511],[-8.875227],[1.852658],[-6.331617],[-6.508664],[0.300184],[2.318752],[-9.318930],[-7.119154],[2.918554],[7.072103],[-2.098989],[6.441380],[-7.495850],[9.321900],[-8.143789],[0.595108],[2.395012],[7.050073],[-0.259471],[8.735331],[5.718924],[1.601893],[-9.991837],[0.331478],[2.320215],[-4.183293],[2.430646],[4.017300],[6.154631],[4.764293],[-7.756126],[-0.084600],[-7.926269],[-2.830642],[-4.224103],[-5.479485],[-0.686732],[0.721673],[4.490350],[-2.647252],[8.081058],[-7.832911],[-2.639506],[-5.910294],[-4.853555],[2.449336]], dtype = "float32")#candidate|5359|(1540, 1)|const|float32
call_5358 = relay.TupleGetItem(func_5293_call(relay.reshape(const_5359.astype('float32'), [7, 220])), 0)
call_5360 = relay.TupleGetItem(func_5296_call(relay.reshape(const_5359.astype('float32'), [7, 220])), 0)
uop_5373 = relay.rsqrt(bop_5330.astype('float32')) # shape=(4, 9, 4)
uop_5375 = relay.rsqrt(bop_5333.astype('float32')) # shape=(4, 9, 4)
func_3863_call = mod.get_global_var('func_3863')
func_3865_call = mutated_mod.get_global_var('func_3865')
call_5379 = relay.TupleGetItem(func_3863_call(), 2)
call_5380 = relay.TupleGetItem(func_3865_call(), 2)
uop_5406 = relay.erf(uop_5373.astype('float32')) # shape=(4, 9, 4)
uop_5408 = relay.erf(uop_5375.astype('float32')) # shape=(4, 9, 4)
var_5417 = relay.var("var_5417", dtype = "float32", shape = (4, 9, 4))#candidate|5417|(4, 9, 4)|var|float32
bop_5418 = relay.left_shift(uop_5406.astype('int32'), relay.reshape(var_5417.astype('int32'), relay.shape_of(uop_5406))) # shape=(4, 9, 4)
bop_5421 = relay.left_shift(uop_5408.astype('int32'), relay.reshape(var_5417.astype('int32'), relay.shape_of(uop_5408))) # shape=(4, 9, 4)
output = relay.Tuple([bop_5345,call_5358,const_5359,call_5379,bop_5418,])
output2 = relay.Tuple([bop_5348,call_5360,const_5359,call_5380,bop_5421,])
func_5422 = relay.Function([var_5329,var_5417,], output)
mod['func_5422'] = func_5422
mod = relay.transform.InferType()(mod)
mutated_mod['func_5422'] = func_5422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5422_call = mutated_mod.get_global_var('func_5422')
var_5424 = relay.var("var_5424", dtype = "float32", shape = (4, 9, 4))#candidate|5424|(4, 9, 4)|var|float32
var_5425 = relay.var("var_5425", dtype = "float32", shape = (4, 9, 4))#candidate|5425|(4, 9, 4)|var|float32
call_5423 = func_5422_call(var_5424,var_5425,)
output = call_5423
func_5426 = relay.Function([var_5424,var_5425,], output)
mutated_mod['func_5426'] = func_5426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2445_call = mod.get_global_var('func_2445')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_5476 = func_2445_call()
call_5477 = func_2445_call()
func_2477_call = mod.get_global_var('func_2477')
func_2479_call = mutated_mod.get_global_var('func_2479')
call_5478 = func_2477_call()
call_5479 = func_2477_call()
func_1617_call = mod.get_global_var('func_1617')
func_1618_call = mutated_mod.get_global_var('func_1618')
call_5480 = relay.TupleGetItem(func_1617_call(), 2)
call_5481 = relay.TupleGetItem(func_1618_call(), 2)
output = relay.Tuple([call_5476,call_5478,call_5480,])
output2 = relay.Tuple([call_5477,call_5479,call_5481,])
func_5482 = relay.Function([], output)
mod['func_5482'] = func_5482
mod = relay.transform.InferType()(mod)
mutated_mod['func_5482'] = func_5482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5482_call = mutated_mod.get_global_var('func_5482')
call_5483 = func_5482_call()
output = call_5483
func_5484 = relay.Function([], output)
mutated_mod['func_5484'] = func_5484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_5485 = relay.TupleGetItem(func_577_call(), 2)
call_5486 = relay.TupleGetItem(func_579_call(), 2)
output = relay.Tuple([call_5485,])
output2 = relay.Tuple([call_5486,])
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
func_5127_call = mod.get_global_var('func_5127')
func_5128_call = mutated_mod.get_global_var('func_5128')
call_5509 = relay.TupleGetItem(func_5127_call(), 0)
call_5510 = relay.TupleGetItem(func_5128_call(), 0)
output = call_5509
output2 = call_5510
func_5518 = relay.Function([], output)
mod['func_5518'] = func_5518
mod = relay.transform.InferType()(mod)
output = func_5518()
func_5519 = relay.Function([], output)
mutated_mod['func_5519'] = func_5519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1311_call = mod.get_global_var('func_1311')
func_1313_call = mutated_mod.get_global_var('func_1313')
call_5520 = relay.TupleGetItem(func_1311_call(), 4)
call_5521 = relay.TupleGetItem(func_1313_call(), 4)
var_5536 = relay.var("var_5536", dtype = "float32", shape = (8, 11, 9))#candidate|5536|(8, 11, 9)|var|float32
bop_5537 = relay.add(call_5520.astype('int16'), relay.reshape(var_5536.astype('int16'), relay.shape_of(call_5520))) # shape=(8, 11, 9)
bop_5540 = relay.add(call_5521.astype('int16'), relay.reshape(var_5536.astype('int16'), relay.shape_of(call_5521))) # shape=(8, 11, 9)
func_2299_call = mod.get_global_var('func_2299')
func_2301_call = mutated_mod.get_global_var('func_2301')
call_5547 = relay.TupleGetItem(func_2299_call(), 1)
call_5548 = relay.TupleGetItem(func_2301_call(), 1)
output = relay.Tuple([bop_5537,call_5547,])
output2 = relay.Tuple([bop_5540,call_5548,])
func_5557 = relay.Function([var_5536,], output)
mod['func_5557'] = func_5557
mod = relay.transform.InferType()(mod)
mutated_mod['func_5557'] = func_5557
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5558 = relay.var("var_5558", dtype = "float32", shape = (8, 11, 9))#candidate|5558|(8, 11, 9)|var|float32
func_5557_call = mutated_mod.get_global_var('func_5557')
call_5559 = func_5557_call(var_5558)
output = call_5559
func_5560 = relay.Function([var_5558], output)
mutated_mod['func_5560'] = func_5560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_5590 = relay.TupleGetItem(func_653_call(), 2)
call_5591 = relay.TupleGetItem(func_654_call(), 2)
output = relay.Tuple([call_5590,])
output2 = relay.Tuple([call_5591,])
func_5598 = relay.Function([], output)
mod['func_5598'] = func_5598
mod = relay.transform.InferType()(mod)
output = func_5598()
func_5599 = relay.Function([], output)
mutated_mod['func_5599'] = func_5599
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5623 = relay.const([[[2,-6,8,-6,1,7,-6,9,9,-3,5],[7,-6,10,9,-9,-9,3,-4,6,10,9],[4,-7,7,-9,-1,2,5,9,-5,-6,-5],[10,7,-7,1,10,-3,-8,8,1,-8,-7],[8,9,-8,6,4,-5,3,-8,5,2,9],[-8,-1,-6,-3,10,-3,-5,-3,-4,-6,-10],[8,-5,-9,3,-9,3,-10,-9,-4,-6,-7],[7,9,-1,-10,-8,-10,-3,2,-5,7,-2],[-8,1,9,8,8,10,-7,-6,9,-5,-9]],[[-7,6,-3,-9,1,-8,-9,10,5,-3,7],[5,6,5,4,-2,4,-1,1,6,5,-4],[2,-2,-4,-3,6,2,1,-5,-3,4,-7],[6,4,9,7,4,9,-6,2,6,9,-1],[-7,-5,-5,10,5,9,-10,-9,-4,-6,-8],[10,4,-7,3,-3,-4,1,-9,-1,-8,6],[-1,-5,-7,-9,-5,-4,-4,2,-8,-8,-5],[-4,-1,-1,-7,7,1,2,4,4,2,-10],[10,2,9,2,8,-8,-1,7,5,6,7]],[[5,-1,3,-8,8,5,6,9,-7,2,-7],[6,2,10,-9,-8,-10,-5,2,4,-1,-1],[2,-3,-8,-4,-1,-3,-2,-1,-1,7,-5],[4,6,-9,-6,2,-10,-7,-3,5,3,-6],[-2,8,-3,-5,-7,-8,-7,-10,7,5,10],[-6,-4,6,1,-4,9,6,-7,2,10,-7],[-7,3,10,1,-9,4,10,-3,-1,5,9],[2,2,9,6,-2,4,6,1,-7,-6,6],[-8,8,5,9,-5,-9,-7,-3,-4,-5,-8]],[[6,10,-2,2,-2,-10,-4,-6,-9,6,-9],[6,-5,7,-3,-2,-6,2,-9,-9,-9,-5],[-4,-5,-1,-2,-5,4,-1,9,6,2,-6],[-2,-3,7,-10,4,-3,-6,2,-5,-6,-7],[10,8,-9,-9,-7,1,-2,1,-1,3,-5],[-8,-6,-4,-4,9,10,1,10,-6,1,-8],[-6,-4,-5,10,-7,-7,-3,-7,-3,-2,-6],[2,-3,4,4,6,2,-8,6,-4,-8,7],[-1,10,-1,-7,-5,2,9,-1,-7,-4,4]],[[3,-10,2,10,-1,4,-7,4,-3,-6,7],[10,-8,-5,-5,4,9,-8,2,-10,9,2],[10,-1,-7,9,-10,-3,7,3,-7,1,9],[-4,-7,3,10,-1,3,5,-9,-5,-5,-9],[6,-4,7,6,-7,6,-7,-10,-6,9,-5],[9,-1,4,3,-6,-3,10,8,-7,-6,-8],[2,2,-3,7,-7,3,-1,6,10,2,4],[3,-8,8,-3,-9,-8,-5,3,-10,-8,-2],[10,2,-2,5,-6,10,9,10,-6,-1,1]],[[5,9,6,-8,8,-6,2,-5,-6,5,7],[-3,8,-5,4,-6,-9,6,-4,-6,4,3],[4,1,10,-5,2,1,9,-10,1,-4,2],[-8,4,-9,9,-6,-9,-2,-5,-6,-5,8],[3,9,-5,-6,4,-5,1,-9,-5,3,2],[-5,-2,-5,-7,1,10,-6,2,5,-10,-4],[-4,3,-10,3,4,10,-8,3,7,-7,-3],[-3,7,-2,-8,-9,-1,-2,-1,-4,5,-10],[-8,-8,6,-1,10,-7,4,5,-8,-4,7]],[[2,5,2,10,2,-5,-3,8,2,-10,5],[8,5,4,-7,-9,10,6,5,4,-6,-10],[9,-4,5,10,9,-10,6,-6,-9,-5,-9],[1,-7,-1,-1,3,-8,1,-3,3,-10,6],[7,2,-7,4,-8,-1,-9,9,3,2,-10],[-5,5,-5,-1,5,-3,5,-4,7,4,-10],[-10,7,-2,7,3,3,9,6,-8,-7,8],[2,-1,-5,-7,-1,5,-2,-6,-8,-8,8],[-10,-9,-3,-1,8,-4,-2,-7,-5,6,6]],[[-8,-7,-1,1,4,4,-2,-10,10,6,-1],[5,7,-6,-2,3,5,10,6,-7,-3,-4],[2,5,5,7,2,-4,4,4,-4,-7,8],[7,9,6,7,-4,-5,-10,-2,4,1,-3],[-10,10,-7,-5,4,-10,-7,4,6,4,1],[-2,3,9,6,6,10,-1,4,-3,-9,-3],[9,2,-7,9,-8,-3,6,4,3,-9,-5],[9,8,10,-6,4,10,3,10,-7,2,1],[9,2,-7,-6,-5,4,8,-3,-6,-10,-2]],[[-6,-6,5,3,7,-3,-6,2,-3,-7,-2],[-8,1,-1,10,5,-8,-9,8,8,5,-4],[2,-3,5,-1,-6,10,-4,-8,4,2,-4],[-4,-4,6,6,10,-6,-4,-4,-7,-3,-8],[8,3,1,4,6,-6,2,10,1,-7,-5],[-7,-3,1,-1,-5,7,3,-3,1,-6,-2],[2,8,3,2,6,9,6,-9,9,8,-4],[-3,-7,-8,3,3,3,-9,-7,-6,-2,4],[3,5,-7,-7,3,8,4,4,8,-5,9]],[[9,4,-8,-10,-4,-4,-6,-1,2,3,-5],[5,-6,-7,6,-6,-1,-10,-9,-3,-3,10],[-10,2,-7,1,4,1,1,-3,-3,1,1],[7,4,-1,-9,-6,-3,2,-5,-2,-10,-1],[1,9,-2,10,-4,1,8,-4,-4,7,-9],[7,-1,3,10,-2,7,-4,4,4,2,-5],[-7,7,-9,1,3,-6,-7,-4,4,-9,-9],[-1,9,-10,-1,3,-6,-1,7,5,-10,-4],[1,-5,8,-5,6,-8,1,8,-5,-2,-5]],[[5,5,-2,2,-1,8,5,9,-10,6,-2],[8,-1,-4,3,5,1,-8,4,-1,-1,2],[-4,6,8,4,2,-3,-6,-5,-6,6,10],[-2,-4,-1,3,-2,6,1,-1,5,10,6],[7,-6,10,10,-6,4,7,-6,9,-7,8],[-9,6,4,-4,-1,-2,3,9,-3,8,-6],[5,5,-9,-8,-4,-8,5,-6,2,7,4],[-5,-3,-9,-6,-8,-6,4,7,4,3,4],[4,6,-9,10,-4,8,5,-10,10,-1,-1]],[[2,9,1,-8,1,-7,9,-9,-9,6,-10],[-5,-10,-6,-1,-8,-7,1,-2,-5,2,-7],[7,-10,6,-4,-4,7,-5,-9,-2,-1,5],[-8,-2,7,4,3,-9,-6,8,3,10,-10],[-5,-3,-3,5,-8,-6,-6,4,-6,-1,-1],[-1,-10,3,-4,-7,1,5,6,-3,-5,-7],[-1,-4,10,-3,2,-4,-10,-2,-1,5,-9],[-5,2,-1,6,-1,9,-5,9,-1,-3,5],[1,10,-8,-3,5,2,-5,-6,1,7,3]],[[10,-1,-4,6,-10,9,-1,2,2,10,-5],[-8,-6,-8,-8,5,10,-9,-10,6,-3,7],[9,-8,7,6,-2,2,-5,1,9,3,1],[6,6,1,-6,-7,-10,-8,4,-10,10,6],[-4,1,4,5,-4,9,4,3,-10,6,5],[10,8,6,4,5,9,-1,8,8,-8,5],[-9,-3,9,1,-1,-3,-3,-7,3,4,8],[4,-3,9,1,3,-4,-9,6,-9,2,-6],[-3,9,6,7,-1,1,3,-5,-4,4,-7]],[[-1,4,-9,-1,9,-7,9,4,-9,-7,8],[8,4,-6,-2,-3,5,4,-4,-7,1,1],[-9,-8,-1,9,-4,-7,-1,-9,3,7,-9],[-1,7,6,-4,-10,4,-1,10,6,-7,2],[-5,2,-3,5,-9,7,-6,4,1,-3,1],[-2,6,-4,-3,2,7,6,-4,-6,-9,8],[7,5,7,5,-6,8,-8,-6,1,9,-3],[-2,9,-9,-10,-6,-3,4,-1,-10,7,8],[2,-8,-3,3,-3,-2,-2,3,-1,8,1]]], dtype = "uint8")#candidate|5623|(14, 9, 11)|const|uint8
var_5624 = relay.var("var_5624", dtype = "uint8", shape = (14, 9, 11))#candidate|5624|(14, 9, 11)|var|uint8
bop_5625 = relay.less(const_5623.astype('bool'), relay.reshape(var_5624.astype('bool'), relay.shape_of(const_5623))) # shape=(14, 9, 11)
func_1556_call = mod.get_global_var('func_1556')
func_1559_call = mutated_mod.get_global_var('func_1559')
const_5634 = relay.const([8.986830,-8.603808,9.912844,4.039169,-7.815137,-2.008318,2.522976,2.075834,-5.011854,-8.242572,0.705701,6.675115,9.209991,2.958032,-6.014875,-4.529831,5.381256,5.157062,-3.395249,-9.085859,-6.310083,1.900159,-7.026264,8.824666,-4.998990,4.077100,1.631270,4.322525,5.096767,8.543350,-3.451198,6.926169,-5.591074,-4.431317,0.269616,7.273685,4.922792,-6.223676,4.465047,-3.554774,5.686880,4.637561,-9.827027,7.502707,-1.298376,6.690657,-4.386692,-9.995845,0.276521,9.012670,8.951134,-9.486951,9.286443,-7.713120,5.033172,-2.589838,1.478081,8.891234,3.854198,8.960683,9.451689,-7.724987,2.551669,-7.047698,3.623011,-6.033058,-8.337360,1.529326,0.428641,-0.434376,-2.261764,3.883316,-2.975408,1.980486,6.337821,2.818308,-2.697689,8.304584,-3.583393,-8.527507,4.984125,9.627468,-5.004362,-7.418484,-5.284278,-1.182254,6.216393,-2.020732,-4.712936,5.885848,-7.151318,-5.440598,-0.837584,6.183410,3.095631,-6.186233,-6.606856,-7.537048,-3.048281,-9.685884,2.708719,0.272071,-3.676662,-5.797777,-3.967640,-8.545858,2.459780,6.154945,-4.129227,-7.242926,-0.425049,1.272109,-0.021827,1.614683,-9.104659,-5.644022,-1.940210,-7.364691,6.619189,9.340408,6.686004,8.806816,-1.626674,-0.446605,2.175006,-1.704414,-0.106196,-1.672368,3.505133,5.029952,3.537311,3.595704,-4.268087,-7.366212,7.263940,0.719288,4.040833,4.120548,8.596468,4.333642,-0.863792,-5.229521,8.618342,-3.987937,0.007600,-8.280020,2.680606,-4.305855,5.214751,5.817866,5.340579,0.459433,7.728274,-0.124438,6.363417,8.045911,-0.823294,-1.040712,-4.324893,-1.417104,-7.384604,-7.539063,7.728201,5.049791,2.147258,8.074302,9.888191,-2.928238,4.992010,4.406381,-6.560347,-7.461706,8.571506,-5.395530,7.643204,1.202231,1.562514,4.318591,-4.564400,7.159467,-0.986443,-2.663431,-1.785503,-5.367443,-2.336795,-9.614353,0.666979,5.260018,6.819522,-3.350528,-7.266834,-1.340844,-0.132012,-1.705385,9.089666,-8.734963,-4.262660,0.590447,3.918023,-6.039937,-7.839667,-2.190253,-0.443832,-1.828948,1.179503,-8.299201,-3.154751,4.713686,2.546814,7.889882,-5.089910,-5.941167,3.040306,2.726697,4.582884,-8.817337,-7.963149,3.408806,-1.064753,-8.805718,1.138644,5.075720,5.607485,-0.928785,3.787773,0.527365,0.656851,-7.984055,-9.246669,-4.995448,-1.606115,5.603013,1.500995,7.938988,-2.899450,-5.506860,-9.731366,1.407654,-1.575791,-0.647312,6.461393,2.740459,0.013404,3.382835,9.875214,-5.676755,-6.752177,-2.943370,-5.165692,7.819043,4.095886,-7.301994,-8.545565,-3.182796,7.396148,-4.712973,-7.638320,-5.813711,4.501452,9.038272,0.402327,-2.079105,7.011601,8.475433,-7.241719,-7.712081,-8.976608,-6.648815,-3.482947,-6.872559,9.368279,1.487290,-8.532814,-9.169492,1.768360,4.480835,2.857663,9.410601,-3.483478,-9.901553,0.779060,8.822955,-8.926874,-2.580249,-5.184984,-6.517571,4.488864,6.510730,0.896828,-1.442948,-8.993589,7.138697,1.176342,-9.926476,-0.429267,4.501789,-2.134953,5.992248,-7.512134,8.389712,-3.071997,-5.772124,7.235202,-1.775264,4.222869,-8.129882,-3.595194,6.468533,-3.829459,3.019297,0.134271,-5.431562,1.423376,-5.361383,-5.962277,-7.926947,6.716941,-6.151818,2.011557,-2.067193,9.144621,-7.770200,-7.475661,-5.855955,3.368719,0.661296,-1.737235,-8.466869,-1.147446,4.081433,0.105726,4.484952,-0.621276,6.638184,-6.414572,8.293183,-0.884373,2.136472,9.269898,2.304737,-4.138194,3.656798,5.980053,-3.398690,-5.507093,-7.215705,-9.609251,6.419951,2.957191,-8.699705,-5.178967,-2.211425,1.954960,6.064370,4.523340,8.639135,-5.877035,-7.830181,8.546242,1.563537,-7.301902,6.561701,2.782045,6.003462,8.695377,0.138840,4.694303,0.543836,9.802824,-2.667099,7.647936,-9.233944,-9.042232,5.214449,-7.878701,-9.442284,-2.459597,7.065188,-2.712455,9.402887,-3.556158,2.702345,-9.480622,-2.756623,5.598385,-3.646202,-1.925411,-4.399574,7.500842,-0.454973,-9.827224,-0.129444,-7.226607,7.169117,-0.038052,8.009416], dtype = "float32")#candidate|5634|(396,)|const|float32
call_5633 = relay.TupleGetItem(func_1556_call(relay.reshape(const_5634.astype('float32'), [6, 66])), 1)
call_5635 = relay.TupleGetItem(func_1559_call(relay.reshape(const_5634.astype('float32'), [6, 66])), 1)
func_1311_call = mod.get_global_var('func_1311')
func_1313_call = mutated_mod.get_global_var('func_1313')
call_5642 = relay.TupleGetItem(func_1311_call(), 6)
call_5643 = relay.TupleGetItem(func_1313_call(), 6)
uop_5644 = relay.asin(var_5624.astype('float64')) # shape=(14, 9, 11)
output = relay.Tuple([bop_5625,call_5633,const_5634,call_5642,uop_5644,])
output2 = relay.Tuple([bop_5625,call_5635,const_5634,call_5643,uop_5644,])
func_5657 = relay.Function([var_5624,], output)
mod['func_5657'] = func_5657
mod = relay.transform.InferType()(mod)
mutated_mod['func_5657'] = func_5657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5658 = relay.var("var_5658", dtype = "uint8", shape = (14, 9, 11))#candidate|5658|(14, 9, 11)|var|uint8
func_5657_call = mutated_mod.get_global_var('func_5657')
call_5659 = func_5657_call(var_5658)
output = call_5659
func_5660 = relay.Function([var_5658], output)
mutated_mod['func_5660'] = func_5660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3392_call = mod.get_global_var('func_3392')
func_3393_call = mutated_mod.get_global_var('func_3393')
call_5715 = relay.TupleGetItem(func_3392_call(), 0)
call_5716 = relay.TupleGetItem(func_3393_call(), 0)
uop_5717 = relay.log(call_5715.astype('float64')) # shape=(7, 220)
uop_5719 = relay.log(call_5716.astype('float64')) # shape=(7, 220)
output = relay.Tuple([uop_5717,])
output2 = relay.Tuple([uop_5719,])
func_5721 = relay.Function([], output)
mod['func_5721'] = func_5721
mod = relay.transform.InferType()(mod)
output = func_5721()
func_5722 = relay.Function([], output)
mutated_mod['func_5722'] = func_5722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2404_call = mod.get_global_var('func_2404')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_5754 = func_2404_call()
call_5755 = func_2404_call()
func_4263_call = mod.get_global_var('func_4263')
func_4265_call = mutated_mod.get_global_var('func_4265')
call_5762 = relay.TupleGetItem(func_4263_call(), 0)
call_5763 = relay.TupleGetItem(func_4265_call(), 0)
output = relay.Tuple([call_5754,call_5762,])
output2 = relay.Tuple([call_5755,call_5763,])
func_5765 = relay.Function([], output)
mod['func_5765'] = func_5765
mod = relay.transform.InferType()(mod)
mutated_mod['func_5765'] = func_5765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5765_call = mutated_mod.get_global_var('func_5765')
call_5766 = func_5765_call()
output = call_5766
func_5767 = relay.Function([], output)
mutated_mod['func_5767'] = func_5767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5482_call = mod.get_global_var('func_5482')
func_5484_call = mutated_mod.get_global_var('func_5484')
call_5773 = relay.TupleGetItem(func_5482_call(), 0)
call_5774 = relay.TupleGetItem(func_5484_call(), 0)
output = relay.Tuple([call_5773,])
output2 = relay.Tuple([call_5774,])
func_5783 = relay.Function([], output)
mod['func_5783'] = func_5783
mod = relay.transform.InferType()(mod)
mutated_mod['func_5783'] = func_5783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5783_call = mutated_mod.get_global_var('func_5783')
call_5784 = func_5783_call()
output = call_5784
func_5785 = relay.Function([], output)
mutated_mod['func_5785'] = func_5785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2477_call = mod.get_global_var('func_2477')
func_2479_call = mutated_mod.get_global_var('func_2479')
call_5822 = func_2477_call()
call_5823 = func_2477_call()
func_926_call = mod.get_global_var('func_926')
func_929_call = mutated_mod.get_global_var('func_929')
var_5838 = relay.var("var_5838", dtype = "float32", shape = (1540,))#candidate|5838|(1540,)|var|float32
call_5837 = relay.TupleGetItem(func_926_call(relay.reshape(var_5838.astype('float32'), [1540,])), 2)
call_5839 = relay.TupleGetItem(func_929_call(relay.reshape(var_5838.astype('float32'), [1540,])), 2)
output = relay.Tuple([call_5822,call_5837,var_5838,])
output2 = relay.Tuple([call_5823,call_5839,var_5838,])
func_5842 = relay.Function([var_5838,], output)
mod['func_5842'] = func_5842
mod = relay.transform.InferType()(mod)
mutated_mod['func_5842'] = func_5842
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5843 = relay.var("var_5843", dtype = "float32", shape = (1540,))#candidate|5843|(1540,)|var|float32
func_5842_call = mutated_mod.get_global_var('func_5842')
call_5844 = func_5842_call(var_5843)
output = call_5844
func_5845 = relay.Function([var_5843], output)
mutated_mod['func_5845'] = func_5845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_429_call = mod.get_global_var('func_429')
func_431_call = mutated_mod.get_global_var('func_431')
call_5866 = relay.TupleGetItem(func_429_call(), 1)
call_5867 = relay.TupleGetItem(func_431_call(), 1)
output = call_5866
output2 = call_5867
func_5868 = relay.Function([], output)
mod['func_5868'] = func_5868
mod = relay.transform.InferType()(mod)
mutated_mod['func_5868'] = func_5868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5868_call = mutated_mod.get_global_var('func_5868')
call_5869 = func_5868_call()
output = call_5869
func_5870 = relay.Function([], output)
mutated_mod['func_5870'] = func_5870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1311_call = mod.get_global_var('func_1311')
func_1313_call = mutated_mod.get_global_var('func_1313')
call_5879 = relay.TupleGetItem(func_1311_call(), 1)
call_5880 = relay.TupleGetItem(func_1313_call(), 1)
const_5884 = relay.const([[[-3.278978,7.158600,4.993356,6.005639,1.372283,6.499165,2.700264,-5.073224,-1.321899,-0.035193,-5.117711,8.482389],[-6.040282,6.701973,4.147156,5.246656,6.834386,-5.316720,-7.531901,-7.029942,9.131320,-2.752783,-1.216056,-7.938000],[-1.654794,-6.151773,-7.139826,0.990974,-0.662527,-2.060392,1.355205,8.095516,-7.708024,0.986279,-5.268636,-0.511434],[5.135705,-7.406022,6.232855,-4.123213,5.898051,-3.759448,9.040147,-4.960210,-4.251594,7.787768,-7.984653,-2.354512],[-2.273441,-6.107289,-8.469240,-1.528514,7.705376,3.062560,-9.063193,-0.736557,-1.177960,1.174937,-6.306948,-4.472064],[-9.225497,-0.381712,-0.291124,4.228128,-9.989592,7.187109,-6.073690,-6.757564,-5.688019,-6.486494,-6.689336,5.655588],[3.206568,-0.918261,-4.225737,-0.326358,-2.406446,-6.334499,-4.736468,5.490242,5.528272,3.256966,-3.122129,3.607105],[0.224900,7.673994,7.896411,-7.443430,-5.502335,-1.734898,9.039466,1.480349,-9.374767,4.508702,-0.548650,3.991848],[5.724260,5.702759,9.640684,7.931623,2.043202,-9.859168,9.626540,3.812900,6.377675,-4.253328,5.864873,-5.937855]],[[0.945049,-5.453831,-3.488261,6.807742,-2.908518,1.178386,-3.643690,-8.501912,-9.333726,-2.908525,6.609872,8.974311],[3.741386,-0.063117,4.579296,-4.980537,-5.621855,-2.763497,5.095752,-1.025487,0.670491,6.805505,-3.384104,6.106199],[-6.658775,-5.174305,1.984349,-3.441011,-2.167515,8.282458,0.134534,-6.066693,-9.793020,-4.728128,8.379469,4.091668],[-8.575118,-2.581330,-8.432146,3.818146,5.183871,5.382883,3.118795,5.846890,-3.482656,-9.018313,6.706594,7.029652],[6.888988,6.978910,-1.840259,7.896560,2.938590,-4.866178,0.469504,-8.050311,1.547531,-8.080094,7.740855,-8.781057],[-1.915105,4.778906,-0.115115,-9.204242,-7.752596,-7.569110,-5.997956,5.998018,5.397359,-0.412220,-8.047433,8.259615],[-1.919038,-9.673614,4.407737,8.416573,5.255866,7.498265,9.467246,-2.779144,4.260551,-5.979807,-9.709758,6.259464],[0.127342,5.612347,-7.178877,-5.845872,-0.876833,-0.119603,8.108772,4.570457,-0.290290,-4.669454,-0.756677,0.288225],[8.482323,-6.794343,-9.018176,3.336309,3.080060,8.595211,5.620220,-3.216071,-5.951751,-7.489812,-7.594138,0.141532]],[[-8.084252,-4.675845,-4.279144,6.526638,3.586892,6.241072,3.258559,-8.258701,7.377816,8.576245,5.165816,-4.693876],[-2.262325,8.377396,7.179524,-2.695877,5.174996,-0.123074,-2.444833,7.276718,1.634499,6.051800,-7.742224,9.269002],[1.501480,-7.118648,-6.665447,7.167951,9.441782,1.105457,8.924450,8.457137,-3.731657,-7.958953,2.064149,1.063847],[-4.919770,7.563497,-1.546549,1.479084,2.425960,-3.523629,-5.388754,6.486313,-2.126157,-3.203622,-9.501346,-9.874310],[-1.644389,2.998105,7.664449,-7.424329,-8.950176,-3.638824,1.585873,-3.038995,6.584967,-7.424227,-0.218331,-2.599959],[5.699620,-3.398122,-9.606397,-7.716491,8.389262,-2.708589,-0.305331,8.865713,-4.130950,2.761124,8.294223,4.342045],[-7.824214,-5.807160,7.289856,-8.132439,-2.607587,-7.551674,5.534976,8.803501,-3.498338,1.068999,-4.327010,7.182716],[-4.997746,-7.716165,8.549451,6.700288,-2.159147,-8.523276,-1.513014,-7.313146,-2.418313,6.085568,0.928922,-6.526411],[-8.506191,9.637187,-2.680433,5.115087,9.172941,-9.168819,4.051905,3.609876,-5.073712,2.623375,-1.565833,9.546418]],[[-2.651376,-8.896542,6.337978,-4.475981,7.256445,-4.166625,-2.171858,-3.045223,-8.205871,-9.540438,-1.088693,5.516331],[-8.745711,1.848589,-1.327179,9.655419,5.731879,-5.794436,-9.133892,-1.765479,-4.990303,-2.025532,8.582367,5.514476],[1.851787,5.554932,4.652891,-5.203139,-6.755519,-5.168959,-1.260520,3.135687,7.143963,-9.439328,-1.401457,2.274211],[-5.471685,-8.409595,9.621024,4.369497,1.331787,-3.731135,0.615915,-1.833166,9.916470,-2.933959,-3.356574,5.840956],[5.157551,-8.492642,4.858052,7.273938,7.118067,4.167722,7.505628,9.695648,4.891865,6.139971,6.318954,-0.852729],[-7.346676,-6.291973,4.114817,-5.932490,-8.689795,-2.576599,7.876888,4.458309,6.059787,9.022817,8.630073,-8.987248],[-6.434463,9.004479,2.236523,-5.857834,-1.332196,7.168415,5.088724,-0.389158,-2.127023,2.952829,-3.899769,-3.235485],[3.401216,-6.251684,-6.017321,4.257108,-6.526011,-7.774877,2.320536,2.327300,-9.218548,7.369863,1.401458,9.111860],[-2.828652,1.184129,6.008057,6.770063,6.057225,7.326450,-1.727853,-6.963890,2.962750,-1.489696,-2.075437,-0.231196]]], dtype = "float64")#candidate|5884|(4, 9, 12)|const|float64
bop_5885 = relay.subtract(call_5879.astype('int16'), const_5884.astype('int16')) # shape=(4, 9, 12)
bop_5888 = relay.subtract(call_5880.astype('int16'), const_5884.astype('int16')) # shape=(4, 9, 12)
output = relay.Tuple([bop_5885,])
output2 = relay.Tuple([bop_5888,])
func_5892 = relay.Function([], output)
mod['func_5892'] = func_5892
mod = relay.transform.InferType()(mod)
output = func_5892()
func_5893 = relay.Function([], output)
mutated_mod['func_5893'] = func_5893
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5894 = relay.var("var_5894", dtype = "float32", shape = (4, 8, 14))#candidate|5894|(4, 8, 14)|var|float32
var_5895 = relay.var("var_5895", dtype = "float32", shape = (4, 8, 14))#candidate|5895|(4, 8, 14)|var|float32
bop_5896 = relay.greater_equal(var_5894.astype('bool'), relay.reshape(var_5895.astype('bool'), relay.shape_of(var_5894))) # shape=(4, 8, 14)
uop_5901 = relay.log(var_5894.astype('float64')) # shape=(4, 8, 14)
output = relay.Tuple([bop_5896,uop_5901,])
output2 = relay.Tuple([bop_5896,uop_5901,])
func_5912 = relay.Function([var_5894,var_5895,], output)
mod['func_5912'] = func_5912
mod = relay.transform.InferType()(mod)
var_5913 = relay.var("var_5913", dtype = "float32", shape = (4, 8, 14))#candidate|5913|(4, 8, 14)|var|float32
var_5914 = relay.var("var_5914", dtype = "float32", shape = (4, 8, 14))#candidate|5914|(4, 8, 14)|var|float32
output = func_5912(var_5913,var_5914,)
func_5915 = relay.Function([var_5913,var_5914,], output)
mutated_mod['func_5915'] = func_5915
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5937 = relay.var("var_5937", dtype = "float64", shape = (7, 5, 10))#candidate|5937|(7, 5, 10)|var|float64
uop_5938 = relay.sin(var_5937.astype('float64')) # shape=(7, 5, 10)
func_1033_call = mod.get_global_var('func_1033')
func_1035_call = mutated_mod.get_global_var('func_1035')
const_5943 = relay.const([-4,2,-4,10,-9,-10,-5,-10,8,-3,2,10,-2,-7,4,1,-2,9,-3,3,-3,3,-1,-6,8,3,-3,-1,7,-1,3,-6,-5,10,-1,10,-3,6,5,-4,1,5,2,10,-4,-8,-3,2,9,-5,-5,6,7,4,4,-9,5,3,-9,-5,-4,-10,7,-2,-3,7,-2,-8,7,-5,9,-7,7,2,-3,-9,-9,-1,-10,-3,1,-3,-4,-6,-2,-1,-6,-7,-8,-10,-5,-7,7,-3,2,10,-7,-6,3,-2,-4,9,-1,2,-5,-10,1,-7,5,5,-9,9,-9,6,1,-8,1,5,-4,-1,1,-9,1,3,7,3,3,1,1,4,7,4,-1,-10,-10,-2,-6,-5,9,3,6,-4,-8,-2,4,8,10,-1,-5,-6,6,5,-10,-9,10,7,-5,-6,-5,3,-6,3,5,9,-5,-4,-4,10,-3,5,10,9,2,-10,6,6,-4,-10,-3,10,7,-8,7,6,-9,-3,-4,4,-10,3,-10,1,-10,-3,-1,8,9,8,-5,5,-9,1,-1,-9,1,-10,-3,-5,2,-3,-2,-1,-8,-8,7,-5,4,-8,-2,7,-1,6,-7,-6,-10,-4,-3,-7,5,-3,1,-7,-5,9,3,5,-4,-7,-4,2,5,8,10,-8,1,5,1,-6,-6,8,-10,3,-5,-6,3,-5,-1,-6,-10,-6,-8,-2,3,-7,-2,10,9,-5,4,-5,9,-5,3,-3,-8,4,10,-6,6,5,10,8,-9,-6,-4,9,-9,4,-8,6,6,1,-8,10,-10,-9,-10,-10,2,9,-6,-9,-3,-8,-2,6,-2,5,-1,1,-9,2,9,-8,9,-7,8,-8,1,-1,-10,-2,-3,2,1,7,-6,-1,2,-6,-9,-4,10,-7,9,3,-6,-2,1,2,9,-2,-8,-2,2,-1,-2,9,6,3,7,-5,-3,1,8,4,5,-4,8,-5,-5,-3,-9,9,10,3,1,10,2,8,5,1,9,-4,3,-9,-4,-7,7,-2,-9,-4,-2,4,6,-8,-5,2,4,3,5,-8,-6,-6,1,2,3,-10,-2,3,-8,2,1,9,2,-3,-4,8,5,5,-1,6,4,-3,2,-6,-8,-4,-2,4,-5,-3,-9,-2,-4,-8,5,3,10,8,3,-2,2,-9,1,10,-10,8,3,-4,7,4,-6,1,-2,-9,5,-5,1,3,7,9,-6,7,-7,8,2,5,-8,7,-7,6,-2,-9,7,7,5,1,3,3,-8,-3,3,-10,6,3,-4,5,2,-8,-6,-2,1,2,-9,5,6,-8,9,9,3,-9,3,-2,-8,5,-5,4,-10,1,3,-7,-7,-7,-4,10,-10,-6,-2,9,9,3,1,-2,-4,-10,-1,8,-3,4,3,7,-4,-8,1,8,1,6,1,-5,-2,-3,-4,-3,-6,-6,-3,-4,-4,-7,2,-7,-9,9,10,4,-6,7,8,7,-6,-6,-6,8,-5,-4,-10,-1,3,-8,1,7,9,-9,1,-2,1,-8,8,-6,10,-1,-3,9,2,9,9,5,9,8,4,-8,8,1,-3,3,8,-4,-6,-7,4,4,-3,3,4,1,-1,-2,-7,9,9,3,-5,8,-2,10,10,-9,-2,4,-6,-4,4,-10,-7,10,10,-5,10,6,10,-10,-9,-5,3,-9,-4,8,6,-10,-8,1,2,2,-1,6,4,4,-4,6,-6,-10,5,10,-7,-6,-1,-2,-5,6,3,-7,-7,2,-10,1,-5,-8,-1,4,1,1,-7,8,7,9,-6,-9,-7,-6,-3,-5,-10,-1,-1,8,-4,-5,-2,-6,7,-1,2,-9,2,8,-4,6,-3,-4,-1,-10,1,-8,10,-4,-9,-1,-4,10,6,3,-10,-6,3,1,2,1,-7,-6,2,4,-4,2,7,-6,-1,-5,-8,-6,-8,-5,8,-4,4,2,2,9,2,4,5,-2,-8,7,-7,7,10,8,9,-1,-3,-10,10,1,-3,1,4,4,2,8,-4,5,-8,-2,-4,-1,-7,-2,-2,-8,9,-5,-5,-6,2,-4,-10,2,1,-6,-8,-4,10,1,10,-1,1,3,-6,-10,-5,-5,-3,-5,-1,-1,-10,4,-2,5,6,-2,-1,10,-4,-6,-5,3,9,4,1,-1,-2,-4,-1,8,-3,4,-7,-3,-7,1,-1,-9,4,-4,-1,-9,-1,-9,10,-10,8,-8,2,-6,-10,8,3,4,5,4,5,10,4,8,7,-10,-4,1,-10,5,-6,-3,-4,-4,-7,4,-2,7,4,-4,3,-7,2,5,5,-2,-2,-7,4,-5,2,2,-4,1,-4,10,-7,-4,-4,-1,-8,-9,-9,-7,10,3,-1,-5,6,4,1,7,2,-8,-10,-5,-3,-1,1,-7,-9,-2,-7,-7,4,-5,7,4,-3,8,-3,-4,-5,1,2,-6,8,1,-6,-10,-10,-7,7,8,4,-5,-9,3,3,-2,2,6,-8,5,3,-6,2,-2,5,-1,8,-5,-5,10,4,3,-10,6,-3,-3,10,-1,-5,3,5,-10,-10,-7,-5,2,-9,-7,-3,-8,-6,5,4,-8,1,8,3,-8,-5,7,3,1,-6,2,1,-8,-5,-3,-10,-8,10,8,6,-8,4,10,5,-1,10,-10,5,8,-10,-9,-1,5,6,9,-1,2,-2,-5,6,8,7,-6,6,2,-6,8,9,1,7,7,6,-5,4,3,-6,-5,-9,-7,9,-10,-10,4,-2,-5,4,-8,1,-9,5,-4,-5,6,-4,-10,2,-7,10,2,-6,-10,-8,3,6,-4,-3,4,9,-3,-10,-5,-3,-7,-4,5,-7,-2,-5,-4,-8,4,9,1,-7,-1,7,1,10,1,6,-6,10,6,5,-8,10,-4,1,7,10,-5,7,7,2,1,-3,-9,-5,2,-8,-2,-4,7,4,1,3,-10,-10,6,-4,-9,4,-4,6,-8,6,-3,8,4,-4,-5,1,-9,-2,-4,-2,5,-5,-4,5,-5,1,9,-10,1,-8,-2,4,9,-6,4,7,5,-10,-3,2,4,-8,5,6,3,-4,10,-6,-4,1,4,7,10,-10,-10,10,8,-9,-7,8,-8,5,-8,6,-5,10,-6,9,-4,-8,-3,-10,-8,3,3,-5,4,8,1,6,2,-5,4,-4,-5,5,-1,-1,6,-4,7,-10,9,5,-2,8,-6,10,-9,8,-7,3,10,4,-8,-4,10,-8,-10,1,-3,-5,1,10,-2,-3,-5,-4,10,10,-8,5,-8,7,5,1,-6,-10,2,7,10,10,4,-10,-3,2,-5,-7,9,3,1,-3,-8,4,-3,-3,-8,-8,-8,9,-9,3,10,-8,-6,-5,7,-4,9,7,6,4,-5,-10,-1,4,-2,5,-9,-10,-8,-1,-1,9,4,3,-6,-6,9,3,5,-1,6,-8,1,-9,-3,1,9,5,6,3,-4,10,-7,3,-2,-10,2,-3,-5,1,5,3,2,7,-5,9,-1,3,1,1,-10,-2,-8,5,-7,1,-10,6,-2,1,3,-7,8,2,5,5,-6,-10,-1,-8,-1,10,5,3,-7,5,4,-4,-1,4,-2,1,-5,2,6,-2,-3,10,8,-7,10,5,-5,6,7,-2,-8,-9,-4,7,-5,6,-3,5,-2,6,-6,3,2,-7,-1,10,-2,10,-1,5,-8,-1,-9,-10,-1,-2,9,-10,7,2,6,7,2,-5,4,7,5,1,-8,-7,-9,-6,4,-9,-3,1,4,1,-3,9,8,-9,7,7,3,4,2,-8,8,-9,10,-2,8,-2,-10,10,8,1,9,9,-3,-4,3,-1,-1,1,2,8,7,-3,-1,-4,-2,4,-2,-5,-6,-10,-1,1,5,5,-5,7,5,8,-3,-4,-7,8,3,-4,2,-9,9,9,2,-1,-9,9,-8,-1,-9,-6,5,-6,9,5,-8,-8,-4,10,1,3,2,5,10,1,-10,8,4,2,-7,-7,-3,3,10,-1,7,-2,-7,6,-2,7,-7,7,-10,-3,8,-2,-4,6,8,-6,3,-1,6,8,-8,2,-1,-5,6,5,-7,-4,-2,7,-10,-5,3,-5,-7,1,-7,9,9,-8,3,8,-2,2,-5,-6,-2,-9,-8,7,7,-1,8,4,-5,4,-8,7,-7,4,8,6,-10,6,-9,-5,1,-5,-9,8,-3,-1,7,9,-9,-7,-10,6,7,-9,-6,-5,2,8,10,3,-2,-4,-4,-4,-7,-9,-1,-8,8,-7,2,3,-5,-3,-1,-10,-5,-2,9,-2,-7,3,6,8,-9,-10,10,-4,6,-10,8,-10,4,1,-7,10,-4,4,6,-5,9,-5,9,-4,1,-4,3,1,5,3,-5,-8,9,10,-5,8,10,-3,-5,6,10,-4,-3,2,-8,-9,-1,-3,-10,4,8,9,7,7,-8,9,-2,-3,-9,2,-2,-2,10,3,-8,5,-3,2,-6,-4,-1,-4,-8,-7,-4,6,-1,-2,4,1,4,-6,10,-7,-8,-3,-5,-3,8,4,10,-9,-10,2,-6,-6,8,-7,1,-9,6,9,10,8,5,-1,4,5,-3,-8,9,1,-5,10,-6,-4,-10,6,8,-10,-8,7,3,3,-1,6,2,-9,-10,2,7,-8,2,9,-8,2,-1,7,5,1,1,-3,-9,-2,1,-2,-2,5,4,4,4,7,7,1,-4,-5,4,-9,-2,1,-7,-4,-3,10,5,-9,-10,-6,2,8,-4,2,2,-10,-6,-2,3,-1,6,-4,-5,-4,3,3,-9,-3,5,10,1,-4,2,10,-1,-2,10,2,10,2,5,-1,6,7,1,9,-1,7,-10,-9,-7,9,-6,5,-6,1,4,-8,-6,-4,-6,9,7,-1,2,-7,10,6,-9,-5,-10,8,8,8,3,-1,6,-4,-5,-1,6,7,6,-3,-6,1,5,-4,5,9,4,7,-9,5,8,4,-4,10,-6,-4,-1,10,4,1,6,7,1,1,5,-5,-10,6,9,3,-9,10,1,10,-6,7,2,-3,10,-4,-8,9,-9,1,3,5,-2,-5,-5,-10,-7,-2,-5,-1,-10,1,5,7,6,-6,-3,-2,6,-10,10,1,-9,6,1,-8,-6,9,10,7,-6,-7,-4,6,4,-10,-5,2,7,5,-9,8,-3,-7,3,-1,7,-9,-6,-10,10,5,-2,-7,-8,6,9,-1,1,7,1,4,-7,6,2,4,-7,-7,-9,-9,-1,2,-9,2,10,5,-7,-9,5,-8,3,-7,2,-1,-10,-5,7,1,-2,-7,2,6,-2,6,2,4,-5,-10,-7,-7,3,-8,-9,8,3,8,9,7,-10,-1,-6,-10,6,-9,10,1,-7,-4,9,-10,7,-8,-1,-10,-7,-5,-5,-5,6,-5,-9,10,7,-2,5,-9,-9,3,-1,5,5,10,-5,-3,8,-7,-8,10,-2,2,-6,4,-1,7,9,9,-2,-5,3,-9,-10,7,-7,3,-1,1,-7,5,1,9,6,5,8,-6,-8,1,5,-5,-7,4,-3,-7,7,10,6,9,1,9,-1,-10,1,-10,1,1,-4,-10,-7,9,1,-3,3,6,-3,3,1,7,-5,10,-2,6,3,3,2,-5,3,9,-9,10,-9,8,-6,-2,1,9,-3,7,2,6,-4,-9,1,5,-1,2,7,2,6,-4,-5,8,9,-4,7,-5,2,-10,-9,5,-9,4,8,9,9,10,-8,4,6,-6,-9,-6,4,6,-10,-5,-7,-4,4,-8,9,-1,-8,4,-2,-9,-3,1,-10,3,7,10,9,-8,9,10,-6,7,-5,-8,-3,-7,1,-6,-7,4,8,-10,7,-2,8,4,-2,-5,-6,-3,1,7,-7,4,1,10,1,-8,1,-3,-3,-10,2,3,10,6,3,-3,6,8,7,-9,-9,-7,9,7,10,1,5,-9,8,-8,9,-5,3,4,-1,-10,-2,-1,8,-4,-9,2,9,-1,-7,9,-2,-2,-10,-5,-9,-1,2,1,2,-8,-10,-5,2,-5,-6,-6,3,-1,4,1,-1,-4,6,4,-3,-7,5,-2,-9,-7,-3,3,-2,-6,10,-2,2,5,5,4,-4,-9,-6,-5,7,-1,-6,6,-9,-6,2,2,-8,-1,-8,9,9,-10,-10,-1,-6,9,5,10,2,4,4,9,3,-4,-7,3,-2,3,6,1,6,-6,9,-6,-1,-4,-4,-8,-5,10,-5,9,5,-1,6,5,-6,-5,-6,-4,9,2,1,2,10,7,4,5,10,10,-10,9,5,-8,3,6,2,-7,7,8,-5,5,2,1,-5,-7,-8,-10,-8,-4,2,5,1,6,5,-5,10,-2,-9,-2,3,-1,6,6,2,5,3,8,5,-9,-2,3,-6,4,-5,10,-8,1,-10,7,8,-8,3,-2,-1,-1,7,7,-6,-9,-9,-2,-7,2,1,-1,-1,-9,-4,3,4,-2,-7,-6,-10,-7,-1,-8,4,-10,-7,-6,-2,3,8,3,1,4,-4,2,-5,-5,-9,-9,-2,10,9,-10,-8,9,10,-9,7,10,4,-7,2,-7,4,-6,4,6,9,-6,-8,5,7,10,7,-7,-3,-4,-6,-7,-9,-7,-8,-6,-8,6,-7,7,-4,10,-6,-4,1,5,9,8,-5,-10,-9,-10,1,4,-6,4,7,-3,10,3,7,9,-9,5,3,9,-6,-10,6,6,4,-5,-3,5,10,-5,5,7,2,-10,-9,-8,1,-1,1,-2,-9,-7,7,-4,-9,6,-2,9,-6,10,1,10,3,10,3,8,-1,2,6,-7,-6,10,-7,-5,-8,-10,-10,-1,-4,-8,3,8,-2,3,8,-4,4,-6,3,-4,4,-9,4,1,1,6,-5,9,5,-5,2,9,3,7,-5,-6,4,-7,-5,8,-8,-1,9,10,4,6,7,3,1,6,2,-6,7,-7,-2,8,1,4,-1,-3,2,-2,7,8,5,3,-6,-6,-4,5,7,-7,5,8,6,1,-3,6,8,7,10,3,-2,-8,1,4,7,6,-1,-7,10,-4,3,-4,-3,-6,-2,8,-9,2,-10,-8,8,-8,-10,7,-3,4,2,-6,-8,10,3,-8,6,2,6,2,6,6,-7,8,5,-7,-8,4,7,-8,3,5,-5,5,7,-9,9,8,10,7,8,4,9,3,-3,-8,-8,4,-2,-7,6,1,-1,1,-7,-7,-4,-4,-9,9,-10,8,2,3,1,-2,-8,-4,5,10,-4,8,10,-1,1,-2,-8,8,2,-3,-3,-2,1,-10,1,-10,-7,-3,2,-7,-5,-1,7,3,3,4,3,7,-10,-8,-4,-8,-7,-1,6,-2,-7,1,4,-5,10,-5,5,-4,-6,8,3,5,6,10,4,-10,-5,-4,5,-8,-9,5,-2,1,-3,1,2,7,2,9,-9,4,1,3,-7,10,-3,-10,-6,-6,-9,-7,3,-10,-1,-8,9,4,-1,-6,9,6,1,-8,8,-5,1,9,-4,-6,9,7,7,8,10,8,-7,1,10,-4,3,5,-9,-5,-3,-2,-6,-2,10,-3,-3,-8,-5,8,-8,4,-2,-5,-3,-6,3,1,-4,-4,-3,5,-8,-6,-1,8,1,-5,1,3,-2,4,-6,-9,-10,-7,2,8,-4,-2,-3,6,-4,-4,-1,-3,-8,2,-2,8,-4,4,6,5,-8,-7,-1,4,6,-2,-7,-1,10,10,-4,3,-3,3,8,-1,7,7,1,-1,9,5,8,10,-9,1,9,9,-10,-1,-10,-7,10,-5,3,-7,9,8,-8,-5,-1,8,10,-9,-2,1,3,-1,9,-4,-1,-7,-5,-10,-5,9,1,5,-9,-4,-7,4,-4,-10,8,7,7,2,1,4,-6,4,-2,-1,-3,9,1,-9,8,-7,-3,8,10,-1,-1,-7,-8,6,-9,-9,1,2,3,6,1,10,8,6,-9,7,4,6,-6,-3,9,-9,2,-2,-5,8,2,3,-7,5,8,5,9,-5,6,-2,-10,7,6,-8,-10,8,6,1,10,1,-2,-1,10,6,4,2,2,-7,-1,-9,1,4,-1,-3,10,1,10,3,-10,7,8,9,3,8,8,6,7,9,4,8,-5,8,-3,-7,-9,-6,-6,-8,-10,4,6,-7,9,-10,7,-6,9,10,-4,-6,1,-3,6,7,-8,3,-10,-6,8,9,5,2,1,7,-8,10,4,10,5,-7,-10,-8,5,-9,-9,10,6,-10,-3,2,-2,1,-6,-8,-8,-3,-9,9,4,-7,-6,8,9,1,-7,-3,5,-4,5,-1,9,3,6,10,-2,2,-5,2,-2,-6,-5,-9,5,3,-5,4,10,-4,1,-6,-2,-3,-1,-1,-7,4,-7,4,6,1,2,7,-5,8,-4,1,3,3,8,-8,2,-6,-5,-1,6,2,9,9,2,-2,-2,-4,-6,8,2,8,8,-3,4,3,5,-9,-7,-8,8,5,2,4,8,-3,-9,-2,-5,-9,-10,1,10,-10,2,5,-8,1,-2,10,-8,8,-4,-4,7,9,10,3,-4,6,-10,6,-5,-10,4,7,-4,9,7,-8,1,-4,-9,-8,1,-9,-8,1,-3,-8,-4,9,10,-6,5,5,-3,-4,7,5,9,1,10,9,-4,10,-4,5,-1,2,7,10,8,2,8,-3,3,2,-5,-5,-10,6,6,-7,-2,-2,8,-7,-8,2,-8,2,-7,3,7,-1,-4,10,-8,-6,-8,9,10,4,7,-3,1,4,-10,-1,4,-6,1,-8,-5,-9,-5,-10,-6,-5,2,-6,3,-10,9,-2,5,1,5,5,8,-2,-4,-7,1,-3,-10,-6,1,8,9,-2,7,10,-5,-2,1,-5,10,-5,-4,2,9,6,3,-7,3,7,-3,4,2,-10,-9,9,-6,10,3,3,9,-2,-3,-7,8,-6,10,10,5,-6,6,-4,10,-4,6,-6,7,9,7,-8,-1,8,4,5,8,6,9,-8,-3,-5,-10,-8,-1,8,-5,4,1,-7,-10,6,6,-3,1,-7,4,5,-4,-2,10,-2,-8,-10,8,6,10,5,-2,-2,-10,7,-10,9,-5,-9,-2,-1,9,9,-7,-3,-7,-4,9,-1,-4,4,-1,9,7,-3,1,1,-3,7,-7,8,1,2,7,-10,2,-8,8,-8,-7,5,-5,8,-9,10,7,10,10,-7,-5,-10,2,9,5,-6,10,-10,8,-5,-5,10,4,2,-10,-1,-8,2,-8,10,8,-6,5,-3,6,-7,4,-4,7,-2,-5,-4,5,2,6,-7,-6,-3,10,4,-4,6,-10,6,-6,-6,3,-5,5,4,-9,-6,-5,-6,4,1,-2,-6,9,10,2,10,6,-8,3,4,4,-7,-10,-5,4,4,3,8,4,7,2,5,-3,10,-6,7,6,-10,6,3,-1,6,7,-6,-10,10,2,-3,-8,-10,9,6,-3,4,-2,-1,-3,7,-1,-2,-5,6,-8,2,-1,-2,-2,-8,7,-8,8,-1,6,-3,-10,9,-7,-3,-3,-3,-7,-9,-3,6,8,8,3,8,-9,6,6,-5,2,10,-10,4,-7,-8,7,-2,-8,-4,2,-10,-3,-10,-4,3,-10,-3,-5,-10,9,5,-2,2,7,-8,-8,-2,7,-9,7,-8,5,9,-8,2,-5,-3,2,-6,3,-10,4,-1,3,3,4,-7,1,-8,-3,8,7,-6,9,10,7,3,1,4,4,4,-7,8,4,-8,-6,6,8,-4,5,-10,-3,6,5,-10,7,8,2,3,3,5,-10,5,-5,6,3,6,9,2,4,-6,5,-5,9,2,-1,-1,8,-10,5,6,-4,-3,-4,6,8,-7,5,9,1,-7,-10,5,6,-4,-1,-8,3,-5,-8,-3,4,-9,-5,4,4,8,2,6,9,1,-2,-5,2,-10,-3,-9,6,-6,8,6,-1,-10,10,-3,5,8,-2,-2,3,7,8,4,3,4,-10,-7,-7,-6,-10,5,-2,5,-6,-10,-1,-6,4,3,-10,1,5,2,5,-8,-8,2,-6,8,8,-2,7,-7,9,-8,-7,10,-9,4,2,-8,-5,-4,9,-4,10,-5,-5,5,4,-1,-4,-3,-5,4,-10,-10,3,7,-6,1,6,-2,-2,-5,2,-5,8,9,6,-1,-8,-3,-4,4,-1,5,-3,-10,-6,1,-2,-4,6,-2,-9,-9,3,-9,-2,7,10,-5,-9,-9,-2,2,-7,-4,2,-7,8,-1,10,6,-2,7,6,-6,7,-9,6,-2,-2,7,-2,-8,-10,9,-6,2,-9,2,1,10,1,-8,5,-1,-8,-10,3,-1,4,3,-7,1,-3,1,9,3,-3,9,3,-4,8,-1,1,-4,-4,-8,-3,8,10,-2,-3,2,-8,-5,-3,-1,-2,-10,6,1,-2,-2,-7,-2,10,-7,9,-8,-10,-9,9,-4,4,-7,9,-2,-6,-5,-5,-10,-1,7,-6,-8,-5,1,-6,-6,-10,-3,-10,9,1,8,1,10,-7,-1,-1,1,-5,-1,-9,9,9,-6,7,6,-9,6,2,-1,3,4,-2,-10,-9,-8,-8,-8,9,10,1,-5,-10,-2,7,3,-9,7,-4,-8,8,3,-3,6,7,1,10,10,-9,2,10,-9,2,10,-3,-9,6,-8,3,2,-10,7,1,1,10,7,1,-8,-9,9,9,-4,1,6,8,3,-3,9,8,3,3,7,-5,7,5,6,5,1,-2,10,-6,-7,3,-2,-5,-8,-4,-4,-4,-3,-8,-5,10,1,-4,3,3,-9,-7,-7,6,5,-2,9,2,5,4,7,7,-10,-6,-2,-5,5,-2,8,-8,7,4,4,-1,-9,8,-1,-1,-9,-3,8,-4,4,7,-5,7,-5,-10,-8,-9,-6,-3,5,7,3,-4,10,5,-3,5,7,2,4,2,-4,1,1,6,-7,7,5,-10,9,-8,-8,-10,9,-9,-5,7,4,-9,3,1,10,-2,9,-9,-9,-1,-2,-2,-7,3,3,-1,-9,4,-8,2,4,5,7,-2,-1,-3,-7,3,7,-4,-6,-7,-9,-7,-7,7,4,-5,-5,7,-3,10,-7,-2,9,-5,4,1,5,10,-8,5,8,5,8,-1,4,9,-4,-6,-8,1,-6,-5,2,-5,2,-2,-10,6,-1,-7,8,-8,8,7,-6,-9,-1,-3,10,3,8,4,4,-5,9,-2,7,-1,-6,10,5,4,4,8,9,-7,7,-4,5,8,1,-3,9,-3,10,-7,-3,-2,-2,2,-2,-8,-2,1,-4,-3,6,3,-10,10,-2,-7,-10,3,-9,-3,5,9,-8,7,7,6,4,1,-8,3,10,4,-1,5,-1,1,2,5,8,1,-2,3,6,9,8,1,-6,-9,-1,4,-3,-10,-5,-4,-9,-10,-1,6,-8,-1,-8,4,9,-10,-10,-4,9,9,-1,7,-7,8,2,7,-10,6,-3,2,6,2,-6,8,-10,-9,9,10,5,-5,-3,-8,-3,9,-7,-5,4,-10,4,8,-4,-5,-5,2,-3,8,1,7,2,-9,-10,1,-4,6,8,1,3,8,9,1,-9,9,6,-4,-3,-7,-7,-9,-9,8,1,1,3,1,9,5,-10,8,10,4,4,8,-10,-2,-4,-6,8,-6,-5,5,10,10,4,-7,9,-10,5,-4,-7,-1,7,-5,-5,7,9,-3,-4,2,-2,-4,2,-4,6,-1,-8,-3,2,-1,-8,-4,-2,7,-10,4,7,3,-4,8,8,-2,-2,1,-2,8,3,-8,-8,1,-3,2,-4,9,3,-9,-7,-5,-7,-2,1,10,3,-10,-2,-1,-7,5,7,3,-1,10,5,-6,4,-5,9,10,3,5,3,10,-10,-3,-9,6,1,8,1,-2,4,-1,-3,5,3,3,5,-5,-6,-1,-7,7,-2,7,10,10,7,9,4,-5,-3,2,2,2,-10,-5,9,-6,-8,4,-10,-4,-6,6,6,-7,-2,6,8,3,10,-4,1,-9,3,-7,-10,10,3,-5,9,-5,-5,-4,10,1,-9,-10,-7,9,4,2,8,-1,-10,-9,10,-10,6,8,-3,-5,-7,3,4,3,10,4,-1,-1,1,8,6,8,3,-10,-6,9,2,9,-3,-5,-10,-3,4,-2,3,-8,-9,3,-4,-6,-7,-6,-6,4,9,-4,-8,2,2,9,-3,6,-5,3,1,-2,6,-9,4,4,5,-4,7,-7,7,6,-2,3,-1,-7,-6,5,8,6,7,7,8,-7,7,-5,7,-6,4,-6,-6,9,3,-5,8,-5,1,-9,3,-5,-9,5,-2,4,-10,2,5,-1,-5,-1,10,-10,-8,-2,-6,-9,9,-10,5,-8,-8,5,4,-4,-4,6,9,-7,-4,7,-9,-4,10,-1,9,2,-2,1,-4,-8,7,4,-9,-4,1,-2,6,9,9,-3,-9,-4,-5,-10,-9,7,2,2,2,2,-5,-4,-2,1,2,10,10,-4,-10,-3,-3,-4,4,4,-2,-3,-5,-2,-1,6,6,5,-9,-2,-5,7,9,-5,-7,-1,7,6,1,7,-10,5,9,5,-3,9,5,-6,-7,-7,9,-1,-4,-10,-6,8,2,-5,5,2,-6,6,7,6,-4,-6,3,-1,6,-3,-10,10,6,4,-5,9,-7,5,-8,8,5,5,1,6,-1,2,2,3,9,-9,-6,-10,-3,7,-7,1,8,2,6,-7,-9,-8,2,6,1,-8,2,-9,2,-6,10,-2,5,-8,-4,-8,5,-1,-9,8,2,6,1,-1,-3,3,6,10,1,-4,4,-5,10,-3,1,-9,-7,-7,2,3,-4,-7,-2,-2,8,6,-10,8,-5,8,-4,10,-4,8,-6,-1,7,-3,-6,2,10,5,-8,-9,6,2,-4,9,-3,2,-10,-2,-1,-6,7,-3,7,-9,1,-2,5,6,8,5,-2,1,-2,-9,-7,1,6,-2,-4,-9,-1,1,-7,-3,-2,-8,-7,-6,-3,1,-1,-3,8,9,-8,-6,-3,5,6,7,-8,2,-8,-4,5,-1,8,3,-3,8,5,10,-3,-8,-5,-4,-1,-8,-5,10,-10,6,6,5,-6,-3,-7,8,10,-8,10,7,8,-10,8,1,-10,-5,8,6,-5,4,-3,-3,-6,-5,-2,-8,8,1,8,5,3,-4,1,5,-10,7,1,4,10,-6,4,1,1,-9,8,-5,-3,1,1,-10,-5,4,-7,-5,-10,7,2,7,2,2,-7,10,-8,-3,-7,1,10,-7,-6,5,-3,1,2,1,-1,3,-10,9,2,-8,-5,-10,-4,5,1,-7,2,-2,-5,8,3,-7,4,2,8,-6,9,-1,5,5,5,2,2,-2,6,7,1,4,-10,1,6,-2,-3,10,-10,-8,8,4,6,9,8,-1,9,-4,2,8,5,5,-4,10,1,-1,-9,-1,3,-7,5,7,3,-5,-9,3,3,-3,-4,-5,10,3,10,-2,-3,3,-7,4,-4,-5,9,6,-9,-3,2,7,3,-9,6,-8,-2,-7,-1,-1,9,5,-7,2,-10,6,-2,-3,-4,7,-4,9,6,-7,8,-10,-5,4,10,7,-10,3,7,-6,6,3,10,8,-9,-3,-4,-5,-1,-2,-7,-10,-3,9,-7,-2,-8,-5,-6,-4,-1,-3,1,-5,-9,3,9,2,-6,-3,-6,8,-10,2,-7,1,3,-2,-4,-9,7,8,5,7,1,-4,4,8,-4,-10,-7,8,6,6,-8,-2,9,10,-10,-5,6,-5,-3,4,5,10,-6,-4,10,-4,-7,7,8,9,-6,-6,-6,-5,-4,-10,-3,-1,-1,-3,6,-3,-4,6,10,8,2,10,-5,-10,-4,-9,3,7,-6,-6,8,5,2,5,-9,-5,9,10,10,6,-10,-10,7,-6,-10,7,-4,1,8,-5,9,9,-7,3,-6,-1,3,9,1,-5,8,10,-8,9,4,-2,-5,-10,-7,10,-1,-2,-2,-4,-6,5,-5,-7,5,7,-9,-2,-10,-7,-7,-4,7,3,-7,-2,6,-9,2,3,4,-7,-9,-7,5,-9,10,1,7,7,-10,9,8,-8,5,-10,-1,10,-9,-10,3,-9,1,10,-5,-6,-8,1,-2,-8,10,6,8,1,6,-2,-3,2,10,-5,-1,-9,5,-6,-1,-6,6,-2,9,-2,9,4,4,7,7,10,-1,8,-1,3,-1,-4,-10,-1,-2,-5,-6,2,-2,5,-8,-1,6,-5,6,-10,8,5,-10,10,-1,2,2,7,-2,-5,-1,-1,8,3,-7,-2,-7,-4,5,-9,-7,-4,-7,-2,7,-1,-6,5,-2,7,-1,4,-9,-3,10,-3,-4,-5,9,-10,-7,-5,7,8,-8,7,-5,5,7,10,-1,6,7,-6,3,5,9,4,1,3,8,-9,1,8,-4,-7,9,-10,-7,7,2,-1,-3,9,8,1,2,-8,4,2,4,2,-5,2,-9,-3,10,-6,-8,4,6,1,-7,-2,-4,-10,-4,-2,7,10,-4,8,6,6,8,-9,7,-2,-8,7,9,-10,10,-1,-9,-4,3,-6,6,2,-4,-8,-10,5,-7,1,10,10,-5,-6,1,7,1,-2,5,-3,-4,10,-3,1,9,-5,-3,-8,5,3,3,-9,-3,-3,2,5,-9,9,10,-2,-4,-6,2,-5,10,-3,10,-9,-3,-9,-10,-1,9,-1,-2,8,9,-10,9,-10,-7,-4,-6,-8,-7,6,-1,-8,-6,9,-1,-3,10,5,-3,10,9,5,-9,4,9,-3,6,-1,10,2,7,-6,-1,10,-4,-1,4,-8,-10,9,4,-10,-5,3,-2,-9,-2,-10,3,-6,10,-2,5,9,4,-5,-10,-9,7,-2,-8,-10,5,-5,7,7,-9,4,-1,-1,9,-5,10,-5,5,8,8,8,-5,2,-2,-1,-10,-7,6,-5,-4,5,4,3,-9,5,-6,-9,-3,4,1,-8,-8,9,-3,-10,-5,-10,-9,8,-3,-3,7,-9,6,8,9,-6,1,5,-2,-10,4,-5,5,10,8,7,9,6,1,1,-9,9,4,3,-10,2,5,6,-1,-5,2,-4,8,-6,-3,-9,4,10,3,-4,6,-9,-3,10,1,-3,-7,-6,9,6,-7,-4,-4,-10,10,9,10,-9,-3,7,6,9,-8,-10,6,-9,-10,5,9,-10,1,-7,7,2,-6,-6,-10,6,1,-5,2,2,-6,6,4,6,-7,-6,10,-6,8,7,-10,-6,-10,10,4,6,8,-7,9,-2,8,-1,-8,3,1,-6,4,2,2,8,3,-7,-5,7,-10,10,-7,-4,-10,-4,6,1,-3,-6,4,-2,7,10,-6,7,6,-1,8,9,-2,-8,5,10,2,-5,-1,5,-8,1,-4,7,-6,4,-6,4,7,6,-1,2,-6,2,-5,5,-6,7,-5,-1,-7,-8,7,10,-4,-8,5,-10,6,-8,3,-4,2,-8,-10,-9,-1,7,-9,-3,-3,9,10,1,-5,7,-4,6,4,2,-10,-8,-6,-2,4,-7,8,-7,7,-2,-8,-10,-10,8,-8,-8,1,-3,5,-1,3,-5,6,-7,9,7,10,10,4,6,6,2,1,4,1,4,5,-4,9,-6,-1,-6,10,3,-1,6,2,-7,-5,9,-8,9,2,8,5,2,7,-8,-1,3,-9,-3,8,4,-1,-1,-7,4,-4,-3,-6,-6,10,-2,-7,6,5,-5,-7,8,5,9,-10,3,3,4,8,4,5,10,-10,-8,-6,-10,5,3,5,-1,-2,10,10,-7,-5,-8,-5,-4,7,-2,6,-5,9,-8,7,9,6,7,3,-6,-2,-9,-5,6,7,-4,-1,2,7,4,3,-5,3,7,-5,4,-1,8,8,-9,-3,7,-2,-4,1,4,3,5,1,-4,6,8,3,-5,-10,-7,7,-9,-5,7,2,9,3,1,-5,2,3,1,6,8,-8,8,-10,-4,9,10,7,7,3,-3,3,2,-7,-3,-8,-10,-7,-4,7,-4,1,8,-5,-5,-2,-9,-8,-10,-5,-2,3,9,-10,7,-1,4,4,10,-8,8,-5,-3,-9,2,6,-6,3,9,10,-3,-8,5,-10,1,-9,-7,7,9,-5,-1,4,9,5,-3,5,-6,-4,5,5,5,7,10,4,-2,-2,-9,10,-4,-8,-8,6,6,-8,-7,10,-8,-1,-3,-10,3,9,8,2,2,10,2,7,-7,2,-7,5,-9,4,1,-8,5,8,5,-5,9,1,3,-3,5,4,8,-7,-6,-9,-4,3,2,-3,3,-6,-5,-8,-6,-9,-6,3,4,1,1,-9,6,-4,-5,-7,-5,3,-1,8,-1,8,-2,1,1,6,-3,8,-8,10,-1,4,-2,-6,7,2,-1,-3,-1,8,10,5,10,-5,-6,-4,3,-5,-4,-10,4,-6,2,7,8,7,-1,1,6,2,2,10,-3,-10,3,7,-10,4,6,7,-9,4,-7,-3,-3,-4,10,-10,-9,1,10,1,3,-4,-7,5,-3,7,-5,2,5,3,-2,-10,5,4,9,7,-1,3,2,-5,8,-7,-4,1,7,-7,-8,9,-8,1,8,-1,1,-8,-3,-1,7,-4,-9,2,-2,4,-8,3,3,5,-2,-2,-10,7,5,4,6,-5,-4,10,8,6,-6,-1,-5,-2,-3,-9,7,4,-3,-8,-8,-3,-9,-8,6,2,5,1,-10,-6,-9,3,10,-10,8,2,-8,-8,-10,4,2,-8,-9,-6,1,-3,-6,6,6,1,-3,-9,9,-10,4,5,-1,-3,-1,1,-1,-4,-1,-5,6,2,-10,-10,8,10,-3,-8,-7,5,9,9,10,-9,4,1,-1,-9,4,1,-9,-4,5,7,10,-9,-9,1,2,4,3,5,-8,4,-4,-4,8,-3,7,-5,3,-7,2,2,7,7,-1,3,-7,-1,-4,3,-4,-6,-8,9,-5,-2,6,9,1,-5,-10,-2,-7,-1,-10,4,-1,-5,1,10,4,-1,9,-6,-9,3,-1,-10,7,-1,4,-1,8,-5,3,5,1,-10,9,1,8,7,6,-10,-9,-2,-10,9,10,-7,3,-2,1,5,7,7,-7,-7,-2,-7,-1,5,1,-7,9,-6,7,5,8,-7,-5,2,-9,-8,-7,-3,4,-8,-1,10,3,10,-3,-10,-6,-8,1,6,1,4,-9,-6,6,-1,-3,7,-6,5,-4,10,2,-5,-10,-7,-3,10,-10,8,-2,-3,8,10,8,3,2,6,-3,-9,9,5,8,5,-2,6,-2,1,-10,3,-8,-4,10,-2,-10,-8,-8,-3,8,4,3,-4,-8,4,-5,8,3,-2,1,-8,7,-9,10,-3,2,-6,7,7,-4,7,-7,-1,-6,-3,-6,-9,-10,-10,-10,9,-10,4,-5,-7,3,-8,-9,-9,1,6,-7,-2,3,7,3,-5,1,2,-2,4,-3,4,-1,-8,8,-10,7,2,-4,-3,-5,9,10,1,-2,-7,-7,-6,-7,3,-8,-10,4,7,1,4,8,1,7,-10,-6,4,10,-4,-4,-2,-9,-7,4,-1,-4,2,-8,-2,2,-6,10,4,9,7,-4,-6,-1,5,9,-10,-1,-6,5,6,1,8,1,1,1,-5,-7,7,6,-3,2,-7,-8,-3,-5,2,2,-7,-1,5,10,-6,-1,-5,9,-1,3,-3,4,-4,7,-5,6,-4,-2,-9,-10,-9,2,-7,4,-3,7,8,1,8,-7,-9,-5,-10,-3,-1,-5,-4,-4,9,9,5,-7,-7,4,-8,-8,-4,9,4,-10,-5,-3,4,-7,7,5,4,-6,10,-6,-3,-5,-1,-8,6,-8,-6,7,-10,3,2,3,9,7,-1,8,-1,-10,7,7,-7,4,8,3,8,7,-5,-8,-10,-6,1,-7,-10,5,7,1,-7,-9,-6,2,10,4,10,4,8,-2,-7,-9,6,-4,-6,-8,2,7,-2,2,8,9,-9,-9,4,-5,-10,8,10,10,-9,-8,-6,8,4,9,-5,2,-3,10,4,-10,2,2,-2,-8,9,-3,-3,-10,-1,10,7,-2,5,-10,9,-3,10,3,-6,-6,-8,-9,-7,9,7,-6,1,9,-9,-5,10,9,3,-3,-4,-3,7,-5,-2,6,4,-8,-7,-3,3,-7,7,-5,10,9,-9,8,8,-4,-6,2,10,4,-4,-6,-6,1,2,4,-4,-8,9,10,-7,-6,5,-4,-7,-4,7,7,4,-7,-4,10,5,-2,4,-10,6,-6,5,6,8,10,-10,9,6,10,-8,-9,-8,5,-3,-3,-2,-10,8,-6,3,-2,-4,-7,-8,10,7,8,2,-7,8,-4,10,-5,7,3,-7,3,7,-2,4,2,3,9,3,10,10,4,-7,6,-10,4,-5,1,-4,10,6,3,2,-7,-2,8,3,9,1,-4,6,10,-6,5,5,9,-7,-1,6,4,6,-7,-4,-9,-4,7,2,1,-10,7,2,-7,10,-10,7,-4,7,-2,-10,5,-3,-5,-10,2,-3,-5,4,-5,-9,1,-8,7,-8,6,1,3,-2,8,3,3,-8,2,-8,6,-4,3,4,7,10,-10,-3,-4,9,8,-1,-1,-9,3,-2,7,8,5,-10,3,-6,-3,-4,-5,-9,9,5,-1,3,-4,-4,8,-10,3,-7,-2,-9,-3,1,8,-10,2,-4,-2,10,1,-6,6,-6,-4,7,-8,-10,-9,-7,-3,-3,4,9,-6,1,-2,8,1,-9,9,-4,10,7,6,-6,3,-3,9,-5,2,-2,-5,4,-6,-2,9,-1,-9,-10,-2,-4,-8,-4,-3,-1,6,-1,8,6,8,-9,3,8,6,-9,-4,5,-9,10,7,7,9,-6,-3,10,-2,8,7,-9,2,3,-10,2,7,-1,7,10,8,-2,-10,-2,-1,8,-4,5,7,-6,6,6,1,-10,7,-4,-7,4,9,10,6,-10,-8,-10,2,-10,3,-4,3,-3,-3,3,-3,7,-5,-4,8,-3,8,9,-9,-8,5,7,5,8,6,8,-10,-1,-4,8,-8,8,2,6,8,-4,-6,-1,-2,9,-2,-9,-1,-7,-5,7,-6,9,-2,-1,-9,-3,7,-7,5,-9,2,9,-8,8,-1,-9,8,5,3,2,1,10,-1,9,5,-3,5,10,-10,7,3,-8,-3,3,-9,9,-10,1,6,-7,7,-7,6,6,-6,-7,10,-10,-8,-9,5,10,9,-7,1,-5,8,1,-9,-9,-3,-2,2,5,4,-1,-4,-6,-2,7,1,-4,-5,-4,-3,9,-1,-8,-4,5,7,-9,-6,-5,2,-6,7,3,-4,-6,9,-4,10,-3,4,-4,-3,3,2,2,1,6,-7,-10,5,9,-5,6,4,10,7,-9,9,-4,10,-2,3,9,-6,-10,-6,6,-1,-5,-2,-2,-10,-1,-5,-9,-2,-7,10,4,6,-8,-4,-4,-7,-1,7,-9,-6,-6,-7,5,-10,6,-10,-8,6,-1,-2,-7,-5,1,-4,8,3,1,3,-1,10,-2,8,9,8,6,4,-1,4,10,2,-7,4,-7,6,9,-5,-8,-1,-9,-6,10,-2,10,5,-5,-8,4,-2,10,-10,6,9,10,-3,-2,-6,1,-3,4,-1,-7,-3,2,3,-5,-2,-8,-7,3,-7,-10,-7,-1,-2,-10,-5,-1,-9,4,-6,7,-10,-8,-3,-8,6,-3,1,-5,10,5,4,4,8,9,8,1,-1,6,10,4,6,-10,3,1,3,-1,-1,-4,6,4,-9,2,3,-6,6,10,-9,-10,-8,-10,-6,-1,7,-7,-9,4,5,10,8,1,-7,-7,-3,-3,-7,-3,-3,7,10,-10,4,-6,4,6,-3,-7,10,-1,10,-6,-6,-7,3,-6,9,-3,3,-1,-7,-10,-4,3,2,6,7,-10,-3,9,-2,-1,4,-3,3,-6,1,-3,7,-10,1,3,-8,-10,-10,6,-7,-3,1,9,-10,-4,-3,7,-4,-8,-2,4,4,10,-4,-7,5,3,-8,10,9,10,-3,-1,3,-2,4,5,-10,3,-5,-9,2,6,4,9,-2,-5,-7,3,-10,7,1,-10,-10,8,-5,6,9,-7,-10,6,9,-8,-10,8,-8,-1,-8,-1,-6,-4,6,-8,1,-7,6,-2,5,-1,3,-4,-8,-9,8,7,-8,6,-10,-8,2,10,9,2,4,-10,5,-7,10,1,3,-3,8,7,-4,7,-10,-3,-2,4,8,-2,-9,10,-2,-7,-9,-10,-10,5,1,9,2,2,-8,-10,2,3,-1,-3,2,-2,10,9,6,-3,7,-10,-3,3,-3,-10,-4,-8,-4,10,9,-10,-1,-9,5,5,4,-3,2,-10,8,9,1,-7,-6,-2,10,-6,-10,-9,6,7,3,-9,-5,-7,-7,4,-2,2,9,-5,-5,-9,7,-10,-4,-5,8,-2,-10,-3,-5,-4,8,-7,3,6,-4,-5,-5,-5,3,-7,-3,3,8,-10,-2,2,-4,1,-2,7,3,10,-8,-8,5,1,2,1,9,3,-8,3,5,-9,-10,4,8,-1,8,-7,-3,-1,2,7,5,-3,6,-5,2,9,-2,-7,-8,7,10,-1,2,-9,5,-6,-7,-3,8,5,2,6,-8,4,-3,-4,-7,-5,-6,-5,-2,1,-1,6,2,3,-7,10,10,-5,-7,6,-3,-4,7,2,-10,1,-7,3,10,5,-5,-7,1,7,-1,3,-4,-3,-4,-10,-7,-6,-10,6,-6,-1,6,-5,-10,-4,-7,-2,-1,2,9,-10,5,-3,-6,6,9,-5,5,-3,-4,5,5,-4,4,4,10,-2,-1,-1,-5,10,-4,1,5,-4,3,10,-9,-4,2,8,1,8,-6,-8,-6,5,1,9,1,5,-5,10,1,6,-2,-5,6,-3,-2,1,9,-6,-3,-6,-8,-6,8,-6,-10,2,9,-4,-3,-7,-8,-1,-4,9,3,10,6,4,-4,3,-5,7,-4,-10,10,10,-6,6,9,7,-1,-3,7,-3,2,-6,-2,-2,5,-3,-1,-2,-5,7,4,-8,-5,3,2,2,3,10,4,-2,-6,-4,10,-4,-6,1,-6,-6,1,2,7,-7,5,-6,1,-8,4,6,9,1,2,9,4,-1,-7,10,9,2,7,5,-5,7,-6,-5,4,4,1,-3,9,10,7,9,7,3,1,-2,-10,8,-3,-1,-1,10,-6,-7,-9,2,4,3,5,5,-4,2,5,8,-5,2,1,7,9,6,-8,-3,2,-6,-3,-2,-8,-9,-4,-9,-5,4,7,5,5,3,2,10,3,10,6,1,6,-5,6,-1,8,-6,9,10,-7,-9,-6,-2,6,-5,5,4,-5,-4,-6,-3,-10,-9,2,-3,10,-7,-3,-5,2,1,7,9,-6,-4,-7,7,6,6,-3,7,3,10,-5,-6,9,4,-5,-8,7,-5,9,-4,8,-2,-3,4,5,3,-3,8,-10,-5,-7,-8,-5,3,-7,-8,10,-5,1,8,-5,7,-2,9,-7,-7,-7,3,1,5,-4,2,5,5,-9,1,4,4,-2,9,7,-6,-2,8,6,1,8,-3,3,6,-3,-7,-4,-4,-4,-6,9,-7,2,6,1,-7,3,10,10,-1,3,-9,-1,-3,-3,7,-4,3,-2,-3,8,-9,-2,10,-5,4,-9,4,5,6,-10,-10,-9,-10,3,1,-5,-4,-9,8,5,3,6,-3,-7,-1,-2,-1,7,2,-5,3,7,-7,-2,-2,1,-1,3,10,-5,-8,5,9,-1,3,-6,-5,4,1,7,2,-9,4,7,1,-8,-8,-8,-2,10,6,2,10,1,3,-3,7,10,-3,9,10,4,-8,-6,3,8,1,9,7,3,2,-4,9,2,2,7,-7,-9,5,-7,-1,-8,-6,-4,-8,2,-4,-1,-2,-4,-4,-4,1,-6,-7,5,-10,10,1,-9,-2,1,7,6,2,-2,10,7,-7,10,-10,4,7,5,10,6,-3,8,8,-7,-4,9,5,7,-3,-10,3,2,-9,-7,9,3,-2,-1,-4,5,1,4,-1,10,10,-4,5,3,3,7,7,3,10,4,-6,2,10,-5,-8,3,-6,-1,5,7,7,-7,3,-6,7,4,6,3,1,8,-3,-7,2,-10,-3,-2,-10,-7,-2,-3,-2,4,-3,7,-7,3,-8,8,8,6,4,6,-6,4,-5,-6,-4,-8,-9,10,1,-5,2,10,1,5,-1,-9,1,6,-10,4,3,10,-6,8,-4,8,-6,7,-4,3,1,-4,-5,10,-3,9,8,-9,-2,4,10,1,10,-3,8,10,8,-6,6,-8,2,-6,1,-5,-4,8,-10,-2,-4,-3,-3,-6,8,-5,7,3,3,8,-7,-8,1,-7,-2,1,7,10,8,-2,7,-1,1,4,3,9,-6,-1,10,9,-8,-7,6,-7,-3,-3,4,-3,-7,-10,-10,10,-5,-2,-8,8,1,5,3,4,-8,-4,-8,-9,5,-5,10,8,6,-2,-3,2,-4,-1,-8,-2,-9,-1,7,-4,-9,7,2,-5,-7,3,-5,-4,-4,9,10,-8,-10,-10,9,7,-2,-7,10,-3,1,9,-4,7,7,-10,7,-10,7,4,-3,-3,-5,-9,6,-6,-9,3,5,3,-7,-3,-3,3,-2,-5,8,-9,-2,-2,10,3,10,-7,7,-10,-3,1,3,-5,1,-1,-1,1,-9,-2,-10,10,-3,6,-7,6,-7,-7,3,7,-3,2,-9,5,-6,6,-2,-6,5,6,-6,3,3,6,-1,9,-1,6,-4,7,10,7,-2,-8,3,-1,10,4,2,-7,-5,5,-7,-6,-5,-2,8,8,2,-7,4,8,1,-7,-4,-6,-3,2,5,3,-3,-5,-6,-1,3,-3,-7,2,3,-1,-4,-3,-9,6,-7,3,6,2,-3,10,4,-4,6,-1,3,-5,10,-3,7,2,-10,3,-3,10,10,1,-5,5,10,10,7,-2,5,5,-7,-5,1,3,-5,-7,2,8,-6,-9,-8,-2,4,3,1,1,-4,3,6,-9,-10,5,6,-1,6,-9,-1,-1,-6,6,2,-3,4,4,-3,-3,9,7,1,8,-10,-4,-7,-5,7,10,9,-8,1,-4,-2,7,5,7,-2,5,-9,2,-2,-10,-8,-10,4,-1,9,9,-2,-5,2,5,6,-7,-7,-2,6,1,4,1,1,-3,9,6,-10,-10,-2,8,3,4,2,2,-9,2,-6,1,6,2,8,7,-8,2,-2,-9,-4,6,8,-4,2,-10,10,6,7,-9,5,-7,-1,-4,-7,-7,-5,-9,-2,3,10,2,7,3,-5,1,8,-2,6,3,8,-6,-4,9,-7,-2,6,-6,2,-8,-2,7,-6,-1,5,-6,4,8,-7,8,7,-3,-1,-7,8,10,-4,-10,-3,3,-4,1,-2,-8,3,-7,5,5,-8,-9,-8,6,3,10,-8,-4,-3,2,1,6,-7,8,2,-8,-6,7,-3,5,3,-1,-10,5,9,1,-9,-8,10,8,9,-4,-2,-10,6,-10,1,-9,-8,4,-2,-1,-4,9,3,7,3,7,-2,2,-2,-8,6,4,2,3,-5,-6,3,4,-5,8,-2,-5,3,4,-10,8,10,1,-2,-7,-9,7,-10,-10,1,7,4,-8,9,-2,-6,6,4,9,2,-4,-1,-4,3,-8,-1,-8,6,4,9,6,-8,-1,-8,8,-6,-2,5,-10,8,-3,-4,6,6,-7,5,10,6,6,4,5,-8,9,-2,2,-8,1,-3,-1,-6,-3,4,4,5,-5,4,8,-6,5,-5,-10,-1,2,7,-2,6,3,9,9,7,-2,3,-3,9,8,5,5,-8,-10,4,7,-7,7,10,-9,-9,10,-5,4,-10,-7,10,-9,-1,-3,-10,3,3,-3,-8,-1,-7,3,-1,5,-9,6,-4,-10,-3,10,-7,3,6,4,10,3,4,1,-2,9,-1,-5,-10,-10,9,-8,-4,8,-7,-4,-8,6,2,1,8,-7,5,-3,-8,9,4,6,6,-10,8,10,2,8,-5,-9,-9,1,-10,-10,-9,6,4,-5,-7,1,-10,1,-9,7,-8,-9,7,-2,4,5,-8,-9,4,3,1,-7,5,5,7,-9,10,-5,-8,4,-8,9,4,8,-4,-1,5,5,8,-5,4,1,4,3,-2,5,-7,-5,2,9,4,-2,10,10,-9,-4,-1,-9,2,6,-10,-3,5,10,-1,5,10,4,-7,9,-9,9,9,-4,1,-6,-1,9,-7,5,-9,5,8,-1,-6,-10,-5,-7,-8,-7,9,9,-2,-5,-9,-9,1,-8,-5,-5,-1,-8,-4,3,5,1,3,3,-10,4,-9,10,7,10,-6,7,-9,-6,-9,5,8,8,-9,5,-9,1,-2,-7,-8,4,-9,-3,-5,1,7,8,5,-5,4,4,-10,9,-5,-4,-3,-8,9,-1,10,8,10,-3,9,7,-9,-7,7,3,-4,6,-5,-10,-6,9,-2,3,3,5,3,7,5,1,2,4,10,3,-4,8,-3,6,-3,7,5,8,-6,-2,-9,-4,6,8,8,9,-4,4,5,-3,8,-6,2,3,-1,2,9,-2,4,10,9,5,-10,1,8,-4,3,-1,4,-4,8,-6,2,1,5,-7,5,-10,-1,-10,4,-5,-4,2,10,-4,4,7,-5,9,2,-6,9,1,8,9,5,-9,-10,-8,6,1,1,5,6,10,1,-4,4,2,-5,4,-7,-1,-1,-9,3,1,6,4,2,-10,9,-5,7,7,-8,-6,-1,2,-7,2,-1,-6,9,-8,3,7,-2,-7,10,5,-2,-5,-7,8,9,4,5,6,-9,6,-2,3,7,-3,3,-7,6,-9,-2,-6,9,9,-9,9,-9,7,-9,-3,10,3,3,-8,3,-1,8,-6,-7,-2,-9,-2,7,-10,-4,3,1,9,6,-3,7,-6,3,-2,6,-7,-5,5,-2,8,-10,-10,-7,-4,-6,-3,-3,10,10,6,-7,5,6,4,7,-4,3,9,-2,-2,-10,-5,-4,8,-8,4,-1,-7,-8,-3,-3,1,10,5,-3,-4,1,-5,-4,-3,-9,-8,-3,-5,6,-6,-6,6,-9,2,7,4,-5,3,1,-10,2,-1,2,5,-8,10,2,-4,6,-2,1,-1,4,-6,1,-7,3,-7,6,7,-7,-9,-3,-7,-10,2,-4,8,8,-4,9,1,9,-8,-9,10,2,-4,-2,-3,-1,-4,1,-4,-5,7,8,-7,-5,-2,2,2,-1,10,-7,-8,2,-3,5,2,-6,5,9,10,10,10,-4,-7,-9,8,2,4,7,4,7,-3,9,4,1,3,6,3,-6,-4,-7,-10,-8,10,-4,-9,-2,-1,-10,8,10,1,5,-7,4,7,-4,8,-3,-9,-3,-5,1,-8,2,-10,-7,10,7,-2,-9,-10,-6,-8,5,4,-8,-4,7,-9,8,-5,2,-5,-5,8,6,8,6,-10,3,-10,-5,9,-8,4,8,1,5,9,-4,3,-4,-1,6,1,7,8,8,5,6,2,-9,1,10,3,6,-4,-6,3,8,1,7,-7,-9,-3,-4,-6,-9,-6,-9,-10,6,7,9,-5,-4,-4,6,-6,-6,9,-3,2,3,10,8,7,4,-7,4,1,8,8,7,-10,-2,-2,3,-8,3,-10,-10,6,-1,-8,-6,-2,4,-8,-6,3,-9,-5,-10,-1,-3,-5,-8,-6,3,5,-2,-4,8,7,-2,2,-7,4,-1,10,5,-8,6,3,7,1,-6,-6,-6,-10,5,-8,10,10,8,-9,7,6,-1,-5,5,-8,8,7,8,2,1,6,5,-5,9,-4,1,-2,-6,-1,-2,6,-4,3,10,7,-9,-3,2,5,-1,-8,8,-5,6,9,-4,5,8,1,-7,-1,3,1,3,-7,-5,-9,4,1,-9,-5,5,-10,-1,-3,1,-5,10,-10,-1,9,1,-1,1,2,-4,2,8,-2,-5,7,1,-2,9,-5,-8,-8,-2,3,-3,-1,3,-6,-7,2,-5,8,3,10,4,10,-8,3,7,3,-3,7,-10,-1,-1,-7,-9,6,-6,4,10,2,-2,9,-2,-1,7,-3,1,3,4,-10,-8,-7,-3,-4,4,-10,-2,-10,-1,9,1,4,7,-5,9,8,-4,-2,5,-7,-4,9,-5,-8,10,-4,-1,-10,-8,-1,-2,4,3,2,-4,9,5,-1,5,-9,-9,3,-5,-10,1,2,10,9,4,1,10,3,8,-8,-5,7,1,-6,6,-9,-9,10,9,-1,1,-10,-2,8,8,2,-4,9,-2,2,-5,6,-4,-3,8,-5,-6,1,9,-7,-5,4,1,-5,-10,-2,7,-1,4,3,8,10,4,-1,1,4,8,-3,1,1,-4,8,-8,-2,3,-4,-5,2,-6,-4,2,10,6,-8,-3,8,-1,-9,-7,3,6,8,10,1,-6,2,3,-7,-9,-5,5,8,-2,-7,7,1,-5,-7,1,-2,4,-5,8,-5,-7,7,-6,10,-3,-8,-4,8,-8,-4,-4,5,2,7,2,-7,2,2,1,5,6,-8,2,2,10,8,4,-4,-5,-6,-2,-7,7,2,1,5,3,-10,9,5,-7,5,-8,8,9,8,9,6,5,5,7,5,-3,-5,6,4,-4,-5,-10,-4,8,-2,9,2,-10,-2,-9,9,2,6,5,-1,3,-9,-10,-5,9,5,7,-4,6,-4,-2,9,-6,-10,-9,7,-7,-6,-1,5,-8,10,2,2,9,-5,6,3,-10,-10,3,2,6,-7,9,-9,-4,2,-10,-4,-8,-7,4,6,-4,5,-6,7,5,8,-6,10,-3,-6,7,-1,-8,1,2,-5,6,4,-7,3,-5,-5,-8,-10,7,6,-5,-1,7,2,1,-6,7,8,-2,-3,2,7,5,10,3,-8,-3,1,2,1,-1,2,-6,-10,-1,-5,-3,4,-2,-1,-10,-5,-9,5,10,-7,-3,-8,9,-9,-3,3,9,-5,2,7,-5,7,9,-5,9,9,-1,5,5,10,10,-5,3,-1,-5,8,-1,4,-8,6,-5,1,9,7,2,3,3,3,9,-10,2,-6,5,-10,1,2,10,1,1,-5,-5,5,8,3,-1,2,5,4,-8,-4,-10,-4,-2,-4,-4,8,-9,9,-2,-5,-7,6,-2,1,5,-8,2,9,-8,-8,2,-2,-8,8,-3,-3,-7,4,9,1,3,-3,1,10,5,-4,4,7,8,4,-10,4,5,-9,5,8,-9,-2,3,10,2,4,-1,-9,-8,-10,9,-8,-4,-9,-6,7,-8,-6,3,-8,1,10,-4,-8,-2,-3,-4,5,7,-7,3,-8,4,-3,-1,3,-4,1,4,10,-10,8,3,2,-9,3,-4,2,-7,7,7,-8,-3,-9,-10,4,4,-6,7,-9,8,8,-4,-9,7,-7,-6,-7,5,7,-7,-7,-4,1,2,8,1,1,-10,8,-8,4,-1,-4,-7,2,-5,6,-6,1,-7,10,-8,-5,1,6,8,3,10,-6,2,2,10,5,5,4,6,9,-4,10,8,5,7,7,-7,4,-2,-7,4,-8,9,-10,7,8,-4,7,6,9,-1,-1,-3,10,-3,10,10,-8,-2,-3,-8,8,-9,3,8,1,2,2,10,1,-10,3,-8,8,-9,-9,-9,-8,-4,8,-3,-5,-2,10,-10,5,1,9,-9,1,7,-7], dtype = "int8")#candidate|5943|(10368,)|const|int8
call_5942 = relay.TupleGetItem(func_1033_call(relay.reshape(const_5943.astype('int8'), [4, 9, 288])), 0)
call_5944 = relay.TupleGetItem(func_1035_call(relay.reshape(const_5943.astype('int8'), [4, 9, 288])), 0)
output = relay.Tuple([uop_5938,call_5942,const_5943,])
output2 = relay.Tuple([uop_5938,call_5944,const_5943,])
func_5945 = relay.Function([var_5937,], output)
mod['func_5945'] = func_5945
mod = relay.transform.InferType()(mod)
var_5946 = relay.var("var_5946", dtype = "float64", shape = (7, 5, 10))#candidate|5946|(7, 5, 10)|var|float64
output = func_5945(var_5946)
func_5947 = relay.Function([var_5946], output)
mutated_mod['func_5947'] = func_5947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3595_call = mod.get_global_var('func_3595')
func_3597_call = mutated_mod.get_global_var('func_3597')
call_5999 = relay.TupleGetItem(func_3595_call(), 0)
call_6000 = relay.TupleGetItem(func_3597_call(), 0)
output = relay.Tuple([call_5999,])
output2 = relay.Tuple([call_6000,])
func_6011 = relay.Function([], output)
mod['func_6011'] = func_6011
mod = relay.transform.InferType()(mod)
mutated_mod['func_6011'] = func_6011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6011_call = mutated_mod.get_global_var('func_6011')
call_6012 = func_6011_call()
output = call_6012
func_6013 = relay.Function([], output)
mutated_mod['func_6013'] = func_6013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4355_call = mod.get_global_var('func_4355')
func_4357_call = mutated_mod.get_global_var('func_4357')
call_6057 = relay.TupleGetItem(func_4355_call(), 0)
call_6058 = relay.TupleGetItem(func_4357_call(), 0)
func_1556_call = mod.get_global_var('func_1556')
func_1559_call = mutated_mod.get_global_var('func_1559')
var_6071 = relay.var("var_6071", dtype = "float32", shape = (396,))#candidate|6071|(396,)|var|float32
call_6070 = relay.TupleGetItem(func_1556_call(relay.reshape(var_6071.astype('float32'), [6, 66])), 4)
call_6072 = relay.TupleGetItem(func_1559_call(relay.reshape(var_6071.astype('float32'), [6, 66])), 4)
output = relay.Tuple([call_6057,call_6070,var_6071,])
output2 = relay.Tuple([call_6058,call_6072,var_6071,])
func_6081 = relay.Function([var_6071,], output)
mod['func_6081'] = func_6081
mod = relay.transform.InferType()(mod)
mutated_mod['func_6081'] = func_6081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6082 = relay.var("var_6082", dtype = "float32", shape = (396,))#candidate|6082|(396,)|var|float32
func_6081_call = mutated_mod.get_global_var('func_6081')
call_6083 = func_6081_call(var_6082)
output = call_6083
func_6084 = relay.Function([var_6082], output)
mutated_mod['func_6084'] = func_6084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_429_call = mod.get_global_var('func_429')
func_431_call = mutated_mod.get_global_var('func_431')
call_6086 = relay.TupleGetItem(func_429_call(), 1)
call_6087 = relay.TupleGetItem(func_431_call(), 1)
func_5657_call = mod.get_global_var('func_5657')
func_5660_call = mutated_mod.get_global_var('func_5660')
const_6092 = relay.const([5,-2,3,8,9,2,5,8,-6,-6,9,-2,5,-1,-7,1,-8,-8,7,2,7,-3,-7,-10,1,3,5,8,7,6,4,5,10,-2,3,-2,-10,-5,-8,-10,-3,1,-2,-10,10,4,5,7,-5,2,-5,-8,-1,-3,-10,-8,-10,4,9,3,-2,-5,-8,-4,-3,1,-1,4,6,1,-2,10,9,4,-10,7,-5,8,-7,8,-9,8,2,3,1,3,-2,-5,-6,1,7,-7,2,-8,8,-9,-7,-8,-2,6,-3,-7,1,-10,-3,3,8,-6,7,-9,2,-3,-8,-9,-2,-4,-1,1,-4,-8,-1,9,-3,10,-1,-7,1,-5,1,-9,-8,-7,1,10,1,2,-1,1,-10,-5,4,-5,10,-3,-3,-1,3,-9,-7,2,6,-10,-9,-2,4,9,7,-10,-3,9,5,-6,-9,-5,-3,-2,2,-6,3,-9,5,-2,1,3,-6,1,-2,10,-1,6,3,-5,-2,-8,-10,1,-5,10,-6,10,-5,1,-10,-7,-7,7,2,7,-4,8,-1,9,-3,-10,4,-1,2,4,-5,5,5,2,-3,-3,1,8,4,8,8,4,-9,-9,-7,5,6,-3,-9,2,1,8,1,-6,7,10,-1,7,1,2,-3,-9,-4,-1,7,-6,1,4,2,-6,-3,4,5,3,9,4,-2,-2,7,-9,9,5,-1,-3,-9,2,7,6,-9,-6,4,-2,-6,3,8,-10,-9,-6,-5,3,-9,-6,1,6,2,-10,-5,3,5,-5,-7,-1,-9,5,5,10,3,10,-9,-5,10,7,6,-7,3,-5,8,-7,2,-2,1,2,-9,7,-1,-9,6,8,-4,-6,-8,9,8,2,-9,-10,8,2,6,-5,4,8,10,3,-5,-2,1,-9,-9,-8,9,9,-9,3,2,2,2,7,8,-7,-10,-5,2,9,-9,2,-4,3,1,9,-6,1,-1,-1,10,-1,6,-3,-10,-2,7,6,4,-5,9,-10,2,-4,-2,1,4,-4,6,1,-8,-6,8,8,-3,-8,-6,-7,10,1,-8,-3,2,5,7,-7,-2,1,7,3,-2,-4,9,-7,5,-10,10,-9,3,4,1,-4,-4,-4,-6,-5,-8,-5,10,-6,9,2,-9,4,5,3,-9,3,-4,6,-6,8,-10,10,6,9,-10,-7,-1,5,8,6,-7,-1,-5,-10,-10,4,-3,1,10,5,10,1,2,9,-3,5,3,-2,-5,-1,1,4,-2,3,3,-2,-9,-4,10,-1,6,5,-4,-10,-9,3,-6,4,-1,10,5,7,-6,7,2,-10,-3,-8,2,-7,8,-3,-8,2,3,1,5,-6,-9,-8,-8,-9,-3,-10,-6,-8,-9,-9,-5,4,5,10,5,5,-8,5,1,-8,5,-9,-5,3,5,10,-5,2,4,-3,9,-5,9,10,5,4,6,-1,10,6,8,-7,-4,4,-2,-7,3,5,-1,1,5,-8,-9,-5,-4,4,8,-4,2,-8,-3,5,-6,-9,7,7,-5,6,-5,-3,-1,9,-10,-2,1,9,7,-3,6,2,-1,-7,5,2,-2,6,-4,3,-10,-8,-6,-6,-1,-8,10,-10,10,-9,3,-4,6,10,-7,-6,9,9,-3,10,5,-10,-9,-7,-10,-5,-8,7,1,6,2,6,-5,9,-3,1,9,4,-6,9,7,-8,-3,1,-6,-3,-6,-10,-5,1,7,7,-7,-4,-3,-8,6,-7,5,-4,-2,9,-7,3,7,-1,9,-2,2,9,10,-8,-5,7,5,-1,8,7,9,9,-5,2,-2,-10,2,-2,9,9,8,-4,-7,10,-2,-3,10,-7,-4,-10,-7,3,-2,-2,-6,4,6,7,-2,-9,5,-7,3,9,-5,4,-9,-1,-1,-1,5,10,-3,5,3,2,-7,10,-3,7,-8,-3,-9,10,-9,-6,-8,8,-5,-9,-10,-6,-9,6,7,-3,-8,4,1,7,6,-6,2,-6,-10,7,7,6,-2,-10,-8,6,9,3,-5,-2,6,5,-6,6,7,6,7,-10,6,7,-2,10,-4,-1,-3,-10,-5,-8,-6,-6,6,-7,-4,1,6,6,3,-9,-10,6,5,4,-2,10,-5,-3,6,5,6,2,5,9,-3,-7,-9,8,-10,6,3,8,-10,-2,-10,8,4,-9,7,9,6,-3,-6,3,-3,5,-2,-5,-5,-1,-3,-4,-1,8,-1,-8,-10,4,-3,-1,5,-2,3,1,4,5,-3,6,2,-1,-10,9,-1,-5,1,9,-4,-3,10,-6,-6,-4,2,2,-6,6,-2,-4,-10,-7,5,-7,9,-7,-3,-3,-8,7,-9,-5,-4,8,7,-10,1,10,-5,6,-4,-5,9,-6,-7,8,-6,8,3,-5,-10,-9,-2,8,3,-3,10,-4,6,-8,4,6,9,9,3,-4,9,-5,-4,10,8,6,9,-9,-9,5,-2,-5,-8,5,-8,-4,6,-10,2,-8,1,-8,-4,-5,-3,8,5,8,-8,3,-6,3,-6,-10,2,9,-2,6,-6,-8,-3,-8,-10,2,-1,-3,3,7,-8,-8,-7,-4,5,-2,10,4,6,4,8,3,-2,-4,-2,-2,10,-3,-8,5,-6,6,8,-9,-10,10,10,5,2,5,-2,6,-9,-10,-5,-2,-1,7,6,4,1,-4,-1,-1,2,-9,-2,-8,-4,-10,3,-10,-8,-4,2,-2,5,-2,-9,-1,8,5,3,-3,-2,-7,-4,-9,-3,9,-4,6,1,8,-2,10,7,2,-1,-8,-9,-7,-4,-7,1,10,-1,5,-8,-3,-1,10,10,-7,-8,-5,-4,2,-9,4,-7,5,5,-9,2,3,4,-1,-7,7,-7,-4,5,8,-5,5,-9,9,10,-4,9,-6,-3,9,-7,-7,1,5,9,1,6,-5,6,-8,1,9,-9,3,3,-4,-2,-7,2,8,-7,-5,-7,-9,-6,7,9,7,2,2,4,8,-6,-9,-8,2,-8,-10,9,5,-6,-1,10,-5,-8,8,2,9,2,6,7,-5,5,9,5,-9,10,-6,-8,1,-9,-1,6,8,-8,-5,-2,-9,6,-3,5,3,-4,4,-1,9,5,-8,-9,-6,-1,-9,5,-4,-7,-3,-10,6,5,-5,6,-6,-5,-1,-3,1,-1,-10,10,7,-2,-10,7,6,7,-10,-7,-7,3,7,6,-1,-8,-3,-5,-6,3,7,3,1,7,6,-8,-6,-10,6,-9,-2,7,5,-8,-7,6,-10,-1,8,2,2,4,2,1,9,4,8,1,-3,4,-1,-8,-9,1,5,-1,5,4,-1,-5,4,-4,-1,6,5,4,8,6,-8,-5,2,1,5,-5,10,-7,-1,7,-9,6,10,-9,-1,-8,-1,6,-2,1,2,-2,-7,-7,3,10,4,3,7,6,8,-9,-8,-2,-1,6,8,6,-8,-4,6,10,-2,-5,6,9,5,2,-4,-4,5,10,9,-9,-8,5,-8,5,-9,-1,4,-10,9,-4,4,7,9,5,3,4,-8,7,-5,10,-5,-10,2,-9,10,1,5,-7,3,-4,-5,-10,-7,-3,-9,8,-3,-2,6,5,9,4,-3,-8,-1,5,-1,3,1,-10,-6,-6,-7,-5,2,-3,-5,4,-7,4,-5,6,-5,-3,2,7,-4,-10,-3,-5,4,-5,4,6,-2,-9,-1,-2,-3,-3,8,4,4,2,8,10,5,2,-7], dtype = "uint8")#candidate|6092|(1386,)|const|uint8
call_6091 = relay.TupleGetItem(func_5657_call(relay.reshape(const_6092.astype('uint8'), [14, 9, 11])), 1)
call_6093 = relay.TupleGetItem(func_5660_call(relay.reshape(const_6092.astype('uint8'), [14, 9, 11])), 1)
bop_6108 = relay.greater_equal(const_6092.astype('bool'), call_6086.astype('bool')) # shape=(4, 9, 1386)
bop_6111 = relay.greater_equal(const_6092.astype('bool'), call_6087.astype('bool')) # shape=(4, 9, 1386)
func_4823_call = mod.get_global_var('func_4823')
func_4826_call = mutated_mod.get_global_var('func_4826')
const_6136 = relay.const([4.070027,-3.498382,7.953276,3.173365,-9.936947,5.874539,3.417915,6.717393,-1.472627,4.058242,4.028207,8.986493,4.524428,-8.954427,-2.380473,1.627286,-3.236553,8.831919,-3.596457,7.709036,-1.168141,-5.608482,-9.069383,6.621963,9.365137,6.627562,-1.209647,3.731142,-1.589191,-6.831924,7.477508,-1.898983,5.924905,5.652444,-0.009898,-5.721905,0.172914,7.733210,7.512029,0.270343,5.144309,4.861728,4.228842,1.298026,-0.985631,3.401015,6.550846,-4.678094,8.643418,-3.837369,-0.377965,-5.808316,-2.397091,3.298653,-8.695766,-1.051024,2.883007,2.898078,-4.040316,-8.604462,-9.814880,-7.377327,5.563426,-3.383521,3.986793,4.200375,-5.704039,1.595684,4.782314,-8.375483,8.361763,2.176526,-9.629530,-4.452955,3.035884,7.312889,-9.904000,0.668255,-1.733037,-5.514626,4.148403,1.416469,8.611174,-2.101582,2.425772,-1.965308,1.055400,-1.339998,-4.202964,8.259502,0.302029,8.398702,-1.461159,-1.767656,-6.403714,-1.262736,-4.615932,5.802452,2.955976,-1.356316,-7.576602,2.159808,-0.990986,9.056499,-2.613067,-4.364348,-1.306047,8.290420,-4.045409,6.299950,-8.850525,-9.531869,-1.192241,-6.200537,4.588314,-9.052758,3.382715,-8.386032,7.816064,-2.299755,-9.251029,-0.641549,-6.379287,3.985207,4.454581,-4.716972,4.565806,-9.604650,-3.411522,0.487055,7.912941,-7.249950,2.175617,-4.755266,-8.711200,7.168128,4.015641,4.880899,9.205523,-0.418754,-7.309165,2.502612,-5.260272,0.008695,-3.543429,-7.821734,-1.900268,8.161544,5.441091,7.165697,-7.292989,-2.485897,-8.144613,-7.200505,0.396334,-1.524021,0.364943,6.014725,7.611281,-0.079169,5.458710,2.823032,5.828260,5.767391,-4.059034,6.315435,7.753176,-1.915319,7.599675,-9.674725,5.865227,-1.313362,-3.259935,-0.998645,-9.060540,8.497420,-9.800465,-5.524081,7.393969,-6.504411,-2.555459,3.747273,-9.361707,7.641807,-4.161755,-4.484507,-1.831675,-6.504348,-6.950268,-9.396608,7.298173,-3.346028,-0.879315,-6.757276,-4.612499,5.482191,-8.968311,9.346117,-1.276789,-2.215911,-5.147815,-1.975102,-5.643464,7.052025,-2.438220,1.537674,4.994779,8.454155,-9.354173,-1.843450,-2.068848,1.677440,-5.393113,8.951357,3.865110,3.723519,-0.747376,-3.812421,-4.615983,4.681994,1.158419,-1.820344,-4.257669,-5.845229,1.599896,-7.669596,-7.389978,-4.953650,-8.259749,9.946794,-9.432769,4.440211,8.839709,5.376857,7.333450,-2.913749,4.142127,7.768149,-5.700730,0.007601,-5.647525,0.645659,9.772077,4.203628,-8.072523,-3.766951,5.856223,5.207634,9.922486,-9.452158,-2.649783,-4.629010,-7.616090,7.060183,5.033751,-9.955518,-3.301944,6.239228,-3.519951,0.432024,5.641705,2.992360,0.186430,1.990415,1.040862,6.809379,-7.726598,1.658061,-6.231557,4.715898,8.934885,5.780798,-1.575119,-1.599963,-6.395575,8.080622,0.969777,-7.214529,2.357509,5.926826,-1.707473,-8.388722,-6.953254,3.716928,3.579867,4.971012,-4.540043,-6.391990,0.616393,7.038234,6.994861,5.532104,7.717602,7.882368,-6.927856,5.360596,-9.388796,4.586802,-1.427634,0.618083,-9.186956,-9.880615,5.313073,5.865530,7.557005,-6.096208,4.630219,3.283215,-6.308022,3.537657,-4.942675,9.586698,7.347828,5.152942,9.610733,7.355286,5.239454,-4.288474,-5.838364,0.664894,5.338226,-4.212940,-6.551415,8.351157,1.117775,7.433182,-5.852498,-0.412265,3.938737,9.367295,-1.193997,-2.725035,-9.193385,-4.119264,-4.887142,2.510933,-9.743074,-6.306917,3.443099,0.574255,1.508803,-1.984819,6.733396,3.159118,0.158561,6.495044,2.777866,9.798078,-7.997627,-4.491421,-4.717346,-4.459745,-4.379707,7.787839,0.529310,-3.626553,6.348997,-6.030375,2.809419,9.649641,-6.534997,-9.186375,1.062954,2.462990,0.995856,-2.074002,6.830286,-1.051361,-5.505518,-5.772259,-9.187997,-3.786615,4.315119,-0.107059,-3.804278,3.567216,-0.816410,-1.235929,-2.965792,-6.223642,4.512394,8.992617,3.320649,-7.096328,6.239770,6.323359,6.274413,1.339440,-6.506243,3.506518,4.992475,8.892772,-6.870204,5.260598,-7.544890,3.910981,3.266066,-4.130449,-4.607648,-2.813700,7.847014,-5.512325,5.101739,-8.660721,0.683662,-4.888798,-7.716184,6.707915,9.634936,4.328857,-2.914149,5.993207,0.321020,-0.881182,9.911513,1.141049,2.651918,8.193946,4.425505,-8.888633,-5.682944,-5.012989,7.506853,8.789369,-5.083823,-7.749971,4.192037,-8.716930,6.228321,7.024627,7.310786,-6.216769,-2.793730,4.850419,3.490125,-4.600161,-4.968514,-7.960580,-6.306100,-1.379828,7.309985,9.562193,2.589362,2.086758,8.221386,1.381636,-3.594570,3.539074,3.647418,-2.032075,-5.040054,-8.085459,2.610752,-0.058334,1.917059,2.665417,1.226365,5.691538,-3.498072,-7.339236,5.448544,6.217559,1.736467,-5.970477,4.938325,5.233576,-9.744460,5.420414,-6.093370,0.534193,-5.246671,-3.234737,-8.623337,-8.417880,5.884675,-4.736740,-0.621048,-9.570667,-4.266486,8.407921,1.459159,3.216277,-3.564915,-7.093693,5.214311,-9.547431,-1.726622,3.392291,4.537272,5.266786,-9.876781,7.032394,0.587072,-5.414628,5.581628,-0.810460,-7.066056,-2.300672,-2.119776,-2.466660,-0.049054,4.451977,2.229001,5.172400,8.151618,6.364593,-3.928351,-1.232762,-0.485350,9.587140,-7.018532,8.611567,-8.888932,-3.929136,-8.441863,-7.357432,5.546989,5.794013,-9.438761,0.650294,7.171558,-4.166922,-6.405931,-3.895204,6.408622,-6.243678,9.597594,1.745083,9.108903,-9.253442,-1.731792,-1.932675,-2.921056,-9.695847,3.968401,-1.216239,1.199420,-7.810919,-6.608791,-1.971721,5.973957,5.573837,-0.645256,-7.618647,-6.330941,5.651694,6.501235,8.215574,6.082240,-3.654271,1.207549,-9.591239,1.227444,-7.270578,5.896423,-3.809997,4.150092,5.467233,-0.262971,9.265003,-8.605168,1.578064,3.111806,5.638286,-1.546608,4.693405,5.560825,-2.174689,-5.619965,-2.651358,-3.148677,-3.868185,-7.749497,2.514206,1.721037,-7.229638,-6.682706,1.626517,-7.000640,-4.010647,1.012757,-0.027012,5.642693,1.895774,-0.965758,5.821666,-9.468488,-4.214923,3.885235,4.133164,4.213108,-0.416704,1.515299,6.900684,4.353510,3.583039,3.252219,3.589885,-9.081326,-7.302884,-1.804015,0.257000,-0.183158,7.605106,-7.105273,-0.238549,-0.437120,8.769140,5.741547,1.052648,-1.972750,7.755098,3.166953,9.681245,2.466238,-8.780325,4.088841,9.904451,6.707632,-6.912484,7.065565,2.815238,9.056785,-8.205259,9.390520,7.902650,-3.098009,4.424656,9.510453,2.724313,7.170966,-6.564520,-2.839709,-6.379777,0.251735,7.205303,4.520795,-2.716041,5.128160,0.130412,8.748341,-5.696114,4.496044,4.467348,-9.008950,-8.605837,-0.386248,3.110883,-8.085560,-7.934039,-6.807792,-3.525314,6.452613,-5.647367,1.780067,3.178125,1.246860,-4.596003,-1.440643,1.984963,9.249159,-6.313821,4.953814,-6.345633,3.971979,9.128034,-0.272077,4.175064,-1.408922,-5.090306,-8.147393,-0.304596,7.484249,-4.623753,-5.275458,5.074753,2.820173,7.925312,3.878367,-6.623786,4.251613,-1.151423,-7.397065,7.160450,4.707969,-6.231158,0.239898,5.301311,-0.306426,-9.419986,-7.403152,-0.583910,9.263428,-3.837579,1.221904,0.417171,-1.465980,-9.633407,-6.877217,8.743052,5.656851,7.801727,7.461155,1.873911,-0.623423,-3.185571,9.147452,1.840447,7.030362,5.712586,-9.593968,5.720938,-5.315148,8.427345,6.413383,4.687033,3.089509,0.756411,6.313034,-6.844559,5.507914,-9.669488,2.974314,6.098739,3.095543,5.658483,-0.683844,-1.186753,-2.287719,5.476780,8.905679,-1.751953,2.056943,9.885581,-7.078406,-1.993262,-6.771443,9.084059,-3.344714,-2.934649,7.984176,-7.888180,-6.065702,0.153333,-3.272057,-5.090784,0.619587,-8.925127,9.041630,6.131954,4.130104,0.716174,4.689394,5.797831,9.042129,3.255630,7.454303,-0.732439,6.929816,-1.437681,-0.448275,3.245247,9.571079,-5.235132,2.729299,0.483889,-8.261378,-9.999119,6.988078,4.685328,-3.271231,1.065830,-3.035240,5.542397,5.477003,-4.582515,5.069767,7.856093,9.294344,7.722542,-9.391685,-4.949312,0.807251,-4.588065,-6.042167,7.749824,-9.835347,3.161135,5.476139,-2.828993,-0.971917,-1.886212,-3.961583,7.768593,-1.305972,-2.422827,6.454220,1.017250,-6.359970,1.822822,8.821017,7.591399,7.129432,8.537586,9.963668,-4.828755,-3.649379,9.832039,-4.849870,-7.214909,8.812457,9.334135,4.289908,9.323648,-5.054869,8.698663,-6.188988,-2.056756,6.406866,-7.351019,9.332898,-3.455949,6.868686,0.967514,-5.738796,-4.415612,-8.673187,-0.319461,-0.682907,6.507825,-5.788599,9.509825,2.494748,5.344227,0.465358,-3.722655,-3.676841,-1.641467,-8.109377,0.003884,0.730699,7.474307,-3.882393,-8.169313,2.171439,3.534452,-3.507568,-3.048813,-1.409848,-3.099691,2.128366,1.033844,3.829017,-7.472468,0.754198,9.025648,7.667356,-1.998110,-7.307661,0.745935,0.058971,-0.975344,9.487729,0.396637,-6.891713,1.542434,-2.845312,9.342345,-8.730038,-0.172183,0.037113,-8.097654,-7.597360,-3.464093,6.402250,-2.923761,1.844768,-7.645910,-4.812437,-6.805786,8.067564,-9.435890,-1.631501,-9.888023,6.059540,-9.623323,-0.333374,-7.004277,-0.606502,4.274434,-7.012163,-8.196874,-3.734823,-7.920460,-9.398010,3.147000,-9.539007,-2.574816,0.895797,8.241876,6.145183,-3.951742,-2.382133,-5.836788,5.157304,3.383716,0.966670,0.819331,-9.073581,-8.803107,4.083277,6.530426,-6.913066,-7.842684,-7.037356,-0.165569,-7.645621,8.194748,3.157625,3.775867,0.689751,-2.990293,-7.313373,3.053191,3.345797,4.000057,9.188857,-6.095471,-1.036994,-6.154060,-0.426424,-3.641000,7.986240,-4.150576,5.487168,9.266260,-6.732443,-5.213222,-4.376087,2.275963,7.876619,-1.113644,8.547805,-0.216477,0.065392,-5.850271,-9.165822,-2.310314,-1.957886,-3.733263,-6.082405,8.703171,-1.456130,5.413725,8.977120,-0.186520,-3.401006,2.540088,-9.290124,1.349809,-6.817342,0.116720,7.037241,-2.538586,-9.264004,5.193808,3.519001,5.237267,-6.698521,-4.083713,-3.027337,3.882259,6.485031,-8.336690,-4.259174,4.571550,-3.719495,7.471855,3.828139,0.660045,3.968552,-9.788586,0.791385,-1.248875,7.152210,3.831967,4.934918,-9.057461,-8.689417,-2.412938,-3.038720,3.102973,0.440003,-8.196542,1.512961,-8.815605,8.433374,3.726364,0.188281,-3.060841,-6.979168,-1.380109,-9.738223,-4.488431,8.758936,-1.185107,-1.670829,-8.609112,-3.919629,-0.180289,4.164482,-3.798367,-6.447502,9.564853,7.440547,-3.818935,-4.475589,-2.473169,6.268621,6.703257,4.387508,-5.667084,4.450917,4.542938,-8.119907,4.977716,6.400767,-2.425730,6.405833,5.587711,3.142826,-5.319981,-0.141230,2.153494,3.339059,-7.379495,-3.276963,5.663805,-1.083956,2.428333,-2.570755,-3.124492,0.581741,8.845067,-6.839509,3.611838,-0.958531,5.223288,-0.372690,-5.112672,0.465654,7.740028,-2.633205,-4.617569,7.120587,3.060026,-5.749576,4.604162,-7.327575,9.325000,5.606662,-9.407059,-7.246103,-9.053098,-0.065020,0.087451,-5.996406,2.081810,2.452218,1.832680,-5.161804,-4.784367,-6.642730,-9.293009,0.469354,8.189123,-7.293586,-3.890195,-2.005489,-7.984760,-1.042371,-0.707544,-0.044690,4.941832,4.583684,-4.113805,8.818088,2.009091,8.915068,-6.315314,5.739125,9.397945,0.023230,-4.701222,8.468507,0.947888,-1.540636,-5.949580,1.363396,-8.858936,-7.389706,-9.782138,-6.679650,3.785473,7.463311,-9.466229,8.198867,2.103291,3.490836,-8.725503,-5.779358,-5.432079,-8.771030,1.007677,-6.116893,-0.349354,-2.272479,-4.526665,-1.027297,-0.198079,3.961212,-7.117718,0.402167,-4.372251,-3.494094,5.899758,-2.253404,3.918258,-9.247571,-3.795048,3.836364,6.875351,-5.533800,-4.045901,5.062972,-1.527321,1.368630,6.799278,-5.281558,2.204480,7.613015,2.773540,4.623056,-2.128125,4.012228,-5.510374,6.133095,2.037441,-9.498523,4.702619,-3.466274,-6.315414,-2.456968,-4.203182,1.695429,8.545399,-1.600443,-9.953102,-8.831802,1.994966,-7.462099,-6.114134,8.715741,6.611394,8.714329,7.862129,-6.952166,1.932217,-9.386108,-4.208478,6.232127,-1.218883,-3.044056,7.252036,6.484503,7.213663,4.663801,0.350271,6.732337,-2.019386,5.035575,-9.872638,9.496531,1.263146,-5.456775,-0.127089,0.600396,6.926770,6.939088,-9.748354,-2.236839,-5.217721,8.307361,-3.234244,-8.855620,7.392798,4.538729,-0.103633,8.485546,-8.189675,9.425386,-9.489371,4.434912,-3.674833,-1.641338,2.390709,-2.532735,-4.733538,9.678131,-8.554912,1.273416,-8.940640,-3.765490,-2.982199,-6.436660,0.773846,3.949607,-7.104964,8.277946,3.438816,-3.182812,-7.555182,0.036634,-0.889832,-0.557989,-7.366922,6.052135,-8.157156,9.433502,7.389053,0.025099,1.520162,-4.905963,6.838359,6.606538,-8.081312,7.861836,-5.329415,4.765641,7.964313,-2.757686,-1.828062,-8.273542,3.899404,9.880010,6.356360,7.022196,6.222562,9.383349,0.961901,5.069504,-9.801415,2.715032,3.389330,5.096240,-1.173377,0.628425,3.726997,6.806113,7.882085], dtype = "float64")#candidate|6136|(1260,)|const|float64
var_6137 = relay.var("var_6137", dtype = "int32", shape = (980,))#candidate|6137|(980,)|var|int32
call_6135 = relay.TupleGetItem(func_4823_call(relay.reshape(const_6136.astype('float64'), [9, 10, 14]), relay.reshape(var_6137.astype('int32'), [14, 70]), ), 0)
call_6138 = relay.TupleGetItem(func_4826_call(relay.reshape(const_6136.astype('float64'), [9, 10, 14]), relay.reshape(var_6137.astype('int32'), [14, 70]), ), 0)
output = relay.Tuple([call_6091,bop_6108,call_6135,const_6136,var_6137,])
output2 = relay.Tuple([call_6093,bop_6111,call_6138,const_6136,var_6137,])
func_6146 = relay.Function([var_6137,], output)
mod['func_6146'] = func_6146
mod = relay.transform.InferType()(mod)
var_6147 = relay.var("var_6147", dtype = "int32", shape = (980,))#candidate|6147|(980,)|var|int32
output = func_6146(var_6147)
func_6148 = relay.Function([var_6147], output)
mutated_mod['func_6148'] = func_6148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5482_call = mod.get_global_var('func_5482')
func_5484_call = mutated_mod.get_global_var('func_5484')
call_6163 = relay.TupleGetItem(func_5482_call(), 2)
call_6164 = relay.TupleGetItem(func_5484_call(), 2)
func_3204_call = mod.get_global_var('func_3204')
func_3206_call = mutated_mod.get_global_var('func_3206')
call_6167 = func_3204_call()
call_6168 = func_3204_call()
func_5518_call = mod.get_global_var('func_5518')
func_5519_call = mutated_mod.get_global_var('func_5519')
call_6177 = func_5518_call()
call_6178 = func_5518_call()
func_4355_call = mod.get_global_var('func_4355')
func_4357_call = mutated_mod.get_global_var('func_4357')
call_6190 = relay.TupleGetItem(func_4355_call(), 0)
call_6191 = relay.TupleGetItem(func_4357_call(), 0)
uop_6210 = relay.acos(call_6163.astype('float64')) # shape=(10, 14, 11)
uop_6212 = relay.acos(call_6164.astype('float64')) # shape=(10, 14, 11)
func_2477_call = mod.get_global_var('func_2477')
func_2479_call = mutated_mod.get_global_var('func_2479')
call_6219 = func_2477_call()
call_6220 = func_2477_call()
uop_6226 = relay.asinh(call_6219.astype('float64')) # shape=(4, 9, 1)
uop_6228 = relay.asinh(call_6220.astype('float64')) # shape=(4, 9, 1)
output = relay.Tuple([call_6167,call_6177,call_6190,uop_6210,uop_6226,])
output2 = relay.Tuple([call_6168,call_6178,call_6191,uop_6212,uop_6228,])
func_6229 = relay.Function([], output)
mod['func_6229'] = func_6229
mod = relay.transform.InferType()(mod)
output = func_6229()
func_6230 = relay.Function([], output)
mutated_mod['func_6230'] = func_6230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1617_call = mod.get_global_var('func_1617')
func_1618_call = mutated_mod.get_global_var('func_1618')
call_6282 = relay.TupleGetItem(func_1617_call(), 1)
call_6283 = relay.TupleGetItem(func_1618_call(), 1)
output = call_6282
output2 = call_6283
func_6292 = relay.Function([], output)
mod['func_6292'] = func_6292
mod = relay.transform.InferType()(mod)
mutated_mod['func_6292'] = func_6292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6292_call = mutated_mod.get_global_var('func_6292')
call_6293 = func_6292_call()
output = call_6293
func_6294 = relay.Function([], output)
mutated_mod['func_6294'] = func_6294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_6295 = func_4637_call()
call_6296 = func_4637_call()
uop_6315 = relay.asinh(call_6295.astype('float64')) # shape=(4, 9, 288)
uop_6317 = relay.asinh(call_6296.astype('float64')) # shape=(4, 9, 288)
output = relay.Tuple([uop_6315,])
output2 = relay.Tuple([uop_6317,])
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
