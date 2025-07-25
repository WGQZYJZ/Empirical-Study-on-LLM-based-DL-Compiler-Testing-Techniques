import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_24 = relay.const([[[True,False,True,False,True,False],[False,True,False,True,True,False],[False,True,False,True,False,True],[True,False,True,True,False,False]],[[True,True,True,True,False,False],[True,False,False,False,False,False],[True,False,True,True,False,False],[True,False,False,True,False,False]],[[True,True,False,False,False,False],[False,True,False,True,True,False],[True,False,False,False,True,False],[False,False,True,True,True,True]],[[False,False,True,False,False,True],[False,True,True,False,True,True],[False,False,True,False,True,False],[True,True,False,True,True,True]],[[False,True,True,True,False,False],[False,False,True,True,False,True],[True,False,False,False,False,True],[True,True,True,False,True,True]],[[False,False,False,True,False,True],[False,False,False,False,True,False],[False,True,True,True,False,True],[False,True,False,False,True,False]],[[False,True,True,True,True,True],[False,False,True,False,True,True],[True,True,True,True,True,False],[False,False,True,True,True,False]],[[False,False,True,False,False,True],[True,False,False,False,False,True],[True,False,True,True,True,False],[False,False,False,False,False,True]],[[False,False,True,False,True,True],[False,True,True,True,False,True],[False,True,False,False,True,False],[False,True,False,True,False,True]]], dtype = "bool")#candidate|24|(9, 4, 6)|const|bool
const_25 = relay.const([[[False,False,False,False,False,True],[True,False,True,True,True,False],[True,False,True,False,False,False],[True,True,False,True,True,False]],[[True,False,True,True,False,False],[True,False,False,True,True,False],[False,False,False,True,True,True],[True,False,False,False,False,False]],[[True,True,False,True,True,True],[False,False,True,True,True,True],[True,False,True,False,True,False],[False,False,False,True,True,True]],[[False,True,True,False,True,False],[True,False,True,True,False,False],[False,False,True,True,True,False],[False,False,True,True,False,False]],[[False,True,False,False,False,False],[False,False,True,True,True,False],[True,False,True,True,True,True],[True,True,True,False,False,False]],[[True,False,False,False,True,True],[False,True,False,True,False,False],[True,False,False,False,True,True],[False,True,True,True,False,False]],[[False,True,True,True,False,True],[True,True,True,False,True,True],[True,True,False,True,False,False],[True,True,False,True,True,False]],[[True,False,True,False,True,True],[True,False,False,False,True,False],[False,True,True,True,True,False],[False,False,False,True,True,False]],[[True,False,False,False,True,True],[False,False,True,True,True,True],[False,False,True,False,False,False],[True,False,True,False,False,False]]], dtype = "bool")#candidate|25|(9, 4, 6)|const|bool
bop_26 = relay.logical_and(const_24.astype('bool'), relay.reshape(const_25.astype('bool'), relay.shape_of(const_24))) # shape=(9, 4, 6)
output = bop_26
output2 = bop_26
func_39 = relay.Function([], output)
mod['func_39'] = func_39
mod = relay.transform.InferType()(mod)
mutated_mod['func_39'] = func_39
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mutated_mod.get_global_var('func_39')
call_40 = func_39_call()
output = call_40
func_41 = relay.Function([], output)
mutated_mod['func_41'] = func_41
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_50 = func_39_call()
call_51 = func_39_call()
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_52 = func_39_call()
call_53 = func_39_call()
output = relay.Tuple([call_50,call_52,])
output2 = relay.Tuple([call_51,call_53,])
func_55 = relay.Function([], output)
mod['func_55'] = func_55
mod = relay.transform.InferType()(mod)
output = func_55()
func_56 = relay.Function([], output)
mutated_mod['func_56'] = func_56
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_74 = func_39_call()
call_75 = func_39_call()
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_82 = func_39_call()
call_83 = func_39_call()
output = relay.Tuple([call_74,call_82,])
output2 = relay.Tuple([call_75,call_83,])
func_84 = relay.Function([], output)
mod['func_84'] = func_84
mod = relay.transform.InferType()(mod)
output = func_84()
func_85 = relay.Function([], output)
mutated_mod['func_85'] = func_85
mutated_mod = relay.transform.InferType()(mutated_mod)
var_147 = relay.var("var_147", dtype = "float32", shape = (6, 4, 7))#candidate|147|(6, 4, 7)|var|float32
var_148 = relay.var("var_148", dtype = "float32", shape = (6, 4, 7))#candidate|148|(6, 4, 7)|var|float32
bop_149 = relay.not_equal(var_147.astype('bool'), relay.reshape(var_148.astype('bool'), relay.shape_of(var_147))) # shape=(6, 4, 7)
func_55_call = mod.get_global_var('func_55')
func_56_call = mutated_mod.get_global_var('func_56')
call_162 = relay.TupleGetItem(func_55_call(), 0)
call_163 = relay.TupleGetItem(func_56_call(), 0)
bop_178 = relay.logical_or(var_148.astype('bool'), relay.reshape(var_147.astype('bool'), relay.shape_of(var_148))) # shape=(6, 4, 7)
output = relay.Tuple([bop_149,call_162,bop_178,])
output2 = relay.Tuple([bop_149,call_163,bop_178,])
func_188 = relay.Function([var_147,var_148,], output)
mod['func_188'] = func_188
mod = relay.transform.InferType()(mod)
var_189 = relay.var("var_189", dtype = "float32", shape = (6, 4, 7))#candidate|189|(6, 4, 7)|var|float32
var_190 = relay.var("var_190", dtype = "float32", shape = (6, 4, 7))#candidate|190|(6, 4, 7)|var|float32
output = func_188(var_189,var_190,)
func_191 = relay.Function([var_189,var_190,], output)
mutated_mod['func_191'] = func_191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_246 = func_39_call()
call_247 = func_39_call()
func_55_call = mod.get_global_var('func_55')
func_56_call = mutated_mod.get_global_var('func_56')
call_251 = relay.TupleGetItem(func_55_call(), 1)
call_252 = relay.TupleGetItem(func_56_call(), 1)
uop_255 = relay.log10(call_251.astype('float64')) # shape=(9, 4, 6)
uop_257 = relay.log10(call_252.astype('float64')) # shape=(9, 4, 6)
func_188_call = mod.get_global_var('func_188')
func_191_call = mutated_mod.get_global_var('func_191')
const_264 = relay.const([-9.641636,-7.417743,-4.478229,8.956128,4.629698,2.018072,7.886139,3.117675,6.397312,-0.870809,3.406200,5.446731,-1.307345,-4.470147,-5.443454,3.588917,-4.195676,9.265258,9.947055,-6.628590,-1.709730,-4.551167,1.696412,4.898198,6.811012,-6.988018,-9.770656,-8.415586,4.321215,-2.566603,8.153651,-1.044665,-8.302704,-9.492413,6.998309,-2.739705,9.460239,6.751482,-4.031243,9.720476,-2.718904,-7.398073,9.071633,8.560953,3.827873,4.698360,4.659128,-7.988643,4.102679,4.669463,5.459467,-9.190976,-5.574009,-8.917930,-2.958524,-0.355146,8.713973,1.671650,-1.782436,-0.573650,7.270733,-6.839918,0.047640,-6.290180,4.131042,1.207676,5.166025,3.089161,4.154828,-9.628263,6.422640,-0.989255,-9.170750,-5.039005,-9.986745,-2.833692,-0.631811,1.184293,-3.412609,-9.824766,1.694533,-4.321585,-5.096967,3.072181,3.538567,5.919971,-7.274456,-5.654586,-7.430484,6.800329,9.170400,-9.488187,-6.903097,7.337832,5.094232,8.694163,-5.426612,2.984789,8.794072,-8.562322,-4.673302,-7.563254,-6.232783,0.856846,9.668310,0.301738,2.277455,-3.822778,9.526632,-8.852480,7.440962,-0.440377,1.077710,-6.691931,-4.480900,-1.731659,8.935814,0.606780,8.894428,-9.628814,-2.730748,6.780528,1.309320,0.719983,6.035618,3.677610,7.904846,-7.124698,7.892545,-8.835436,-0.048145,-0.389934,2.854977,0.647901,9.108911,8.173886,9.469450,8.817211,-5.024185,-6.872840,-6.516342,-2.168597,4.323810,-1.082778,-1.277699,-1.900327,5.014423,-6.276337,-1.693025,0.295036,7.067224,8.160791,7.466074,5.808609,-0.720665,-4.602673,1.593664,-1.553426,1.276195,6.178829,1.707878,-0.046057,-5.311390,7.424700,-0.808971,-1.019552,6.209795,5.879240], dtype = "float32")#candidate|264|(168,)|const|float32
call_263 = relay.TupleGetItem(func_188_call(relay.reshape(const_264.astype('float32'), [6, 4, 7]), relay.reshape(const_264.astype('float32'), [6, 4, 7]), ), 0)
call_265 = relay.TupleGetItem(func_191_call(relay.reshape(const_264.astype('float32'), [6, 4, 7]), relay.reshape(const_264.astype('float32'), [6, 4, 7]), ), 0)
output = relay.Tuple([call_246,uop_255,call_263,const_264,])
output2 = relay.Tuple([call_247,uop_257,call_265,const_264,])
func_272 = relay.Function([], output)
mod['func_272'] = func_272
mod = relay.transform.InferType()(mod)
mutated_mod['func_272'] = func_272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_272_call = mutated_mod.get_global_var('func_272')
call_273 = func_272_call()
output = call_273
func_274 = relay.Function([], output)
mutated_mod['func_274'] = func_274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_84_call = mod.get_global_var('func_84')
func_85_call = mutated_mod.get_global_var('func_85')
call_286 = relay.TupleGetItem(func_84_call(), 1)
call_287 = relay.TupleGetItem(func_85_call(), 1)
output = relay.Tuple([call_286,])
output2 = relay.Tuple([call_287,])
func_288 = relay.Function([], output)
mod['func_288'] = func_288
mod = relay.transform.InferType()(mod)
mutated_mod['func_288'] = func_288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_288_call = mutated_mod.get_global_var('func_288')
call_289 = func_288_call()
output = call_289
func_290 = relay.Function([], output)
mutated_mod['func_290'] = func_290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_288_call = mod.get_global_var('func_288')
func_290_call = mutated_mod.get_global_var('func_290')
call_294 = relay.TupleGetItem(func_288_call(), 0)
call_295 = relay.TupleGetItem(func_290_call(), 0)
func_188_call = mod.get_global_var('func_188')
func_191_call = mutated_mod.get_global_var('func_191')
const_316 = relay.const([6.924627,1.996719,-0.630739,-5.750271,4.723725,9.123423,-6.663612,3.628366,-1.722959,3.873280,-0.762195,-1.180293,-6.738452,-4.424174,-7.836380,-2.126047,1.331330,-7.088154,-9.016570,3.371574,1.560515,-8.670499,3.589422,1.790817,-9.232892,2.291156,-0.889071,-6.967809,1.001597,-7.096616,-4.632878,0.875933,-3.675920,-2.971869,6.988374,-5.505085,-1.923493,-2.360710,-0.527952,3.135407,-8.865594,-1.657806,-4.239810,-3.965965,4.772690,7.445384,0.874117,4.945956,-3.832354,-5.639644,3.566341,-1.905353,7.339744,2.121209,-7.488986,2.490064,-1.350570,9.964739,-8.068922,-2.799699,-0.578811,8.505846,-6.962893,-8.630659,-0.060266,-9.015604,0.670646,8.020936,5.640759,1.906228,7.192054,4.059753,-0.367273,-8.913779,-2.105231,-1.069082,-9.810692,-0.764717,-0.092681,6.102050,-1.481283,9.462739,-3.373853,-9.475078,6.724045,-3.700818,-3.634643,-7.799293,-5.569143,5.676269,3.808027,-3.804179,-9.004850,5.446499,5.458233,5.659010,-7.445385,2.530800,-7.650422,9.652934,3.510949,-9.011112,3.426533,-3.705535,-7.687841,-1.573915,7.314408,4.562145,5.284846,6.116148,-6.631638,-6.017865,2.930836,8.352106,-4.795105,8.667603,-8.907676,1.045635,3.359286,-3.616144,-2.222326,3.190871,5.371275,4.324318,4.129221,6.994124,3.285387,1.771488,4.566249,-7.744148,6.821614,-3.140911,-3.412864,8.119069,9.607692,0.441621,-2.572117,-9.071084,6.493227,-8.588761,-4.539773,-2.924494,-2.137078,-9.096457,0.304824,0.735218,-7.859718,-6.302831,6.632120,-8.621173,9.152437,-0.393370,7.373781,7.062412,-1.861427,0.401780,0.046671,9.048456,6.078445,-2.126275,-1.172870,2.980060,8.701710,4.710105,7.349225,8.484476,0.111258,-2.798160], dtype = "float32")#candidate|316|(168,)|const|float32
call_315 = relay.TupleGetItem(func_188_call(relay.reshape(const_316.astype('float32'), [6, 4, 7]), relay.reshape(const_316.astype('float32'), [6, 4, 7]), ), 2)
call_317 = relay.TupleGetItem(func_191_call(relay.reshape(const_316.astype('float32'), [6, 4, 7]), relay.reshape(const_316.astype('float32'), [6, 4, 7]), ), 2)
output = relay.Tuple([call_294,call_315,const_316,])
output2 = relay.Tuple([call_295,call_317,const_316,])
func_319 = relay.Function([], output)
mod['func_319'] = func_319
mod = relay.transform.InferType()(mod)
mutated_mod['func_319'] = func_319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mutated_mod.get_global_var('func_319')
call_320 = func_319_call()
output = call_320
func_321 = relay.Function([], output)
mutated_mod['func_321'] = func_321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_414 = func_39_call()
call_415 = func_39_call()
const_416 = relay.const([[[False,True,True,False,True,True],[True,False,False,False,True,False],[False,False,True,False,True,True],[True,True,True,True,False,True]],[[False,False,True,True,True,True],[False,True,False,True,True,True],[False,True,True,True,True,True],[True,True,True,True,True,False]],[[False,False,False,True,False,False],[True,False,True,False,True,False],[True,True,False,False,False,True],[True,True,False,True,False,True]],[[False,True,False,True,False,True],[False,False,False,False,False,False],[False,True,False,True,True,True],[False,True,True,False,True,True]],[[True,False,False,False,True,False],[True,True,False,False,True,False],[True,True,True,True,True,True],[True,True,False,True,True,True]],[[True,True,False,False,True,True],[True,False,False,False,False,True],[False,False,True,False,False,False],[True,True,True,False,True,False]],[[True,False,True,True,False,False],[False,True,True,True,True,False],[False,False,True,False,False,True],[False,True,True,True,True,True]],[[True,False,True,False,False,False],[False,True,False,True,False,False],[False,True,True,True,False,False],[False,False,True,True,True,True]],[[False,True,False,False,False,False],[True,True,False,False,True,True],[False,True,False,True,False,True],[True,False,False,True,False,False]]], dtype = "bool")#candidate|416|(9, 4, 6)|const|bool
bop_417 = relay.floor_divide(call_414.astype('float64'), relay.reshape(const_416.astype('float64'), relay.shape_of(call_414))) # shape=(9, 4, 6)
bop_420 = relay.floor_divide(call_415.astype('float64'), relay.reshape(const_416.astype('float64'), relay.shape_of(call_415))) # shape=(9, 4, 6)
output = bop_417
output2 = bop_420
func_427 = relay.Function([], output)
mod['func_427'] = func_427
mod = relay.transform.InferType()(mod)
output = func_427()
func_428 = relay.Function([], output)
mutated_mod['func_428'] = func_428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_432 = relay.var("var_432", dtype = "float32", shape = (15, 4, 6))#candidate|432|(15, 4, 6)|var|float32
uop_433 = relay.sigmoid(var_432.astype('float32')) # shape=(15, 4, 6)
output = uop_433
output2 = uop_433
func_455 = relay.Function([var_432,], output)
mod['func_455'] = func_455
mod = relay.transform.InferType()(mod)
mutated_mod['func_455'] = func_455
mutated_mod = relay.transform.InferType()(mutated_mod)
var_456 = relay.var("var_456", dtype = "float32", shape = (15, 4, 6))#candidate|456|(15, 4, 6)|var|float32
func_455_call = mutated_mod.get_global_var('func_455')
call_457 = func_455_call(var_456)
output = call_457
func_458 = relay.Function([var_456], output)
mutated_mod['func_458'] = func_458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_427_call = mod.get_global_var('func_427')
func_428_call = mutated_mod.get_global_var('func_428')
call_547 = func_427_call()
call_548 = func_427_call()
func_427_call = mod.get_global_var('func_427')
func_428_call = mutated_mod.get_global_var('func_428')
call_563 = func_427_call()
call_564 = func_427_call()
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_566 = relay.TupleGetItem(func_319_call(), 0)
call_567 = relay.TupleGetItem(func_321_call(), 0)
func_455_call = mod.get_global_var('func_455')
func_458_call = mutated_mod.get_global_var('func_458')
const_578 = relay.const([2.872346,8.635337,-4.784449,-3.853196,-5.276474,9.139145,-6.352694,9.009016,5.251373,2.485080,5.923758,3.801388,3.196755,-3.886614,-7.847546,-3.956757,3.483762,5.680716,1.966707,-1.539968,-9.871219,-5.588546,5.972107,2.501297,9.789514,-4.676279,0.992179,0.160810,4.559823,4.630900,-8.894813,3.855078,7.755003,5.978995,-8.022293,-1.420926,-5.583343,0.407010,7.400460,-1.414175,-3.354365,4.401046,8.223862,-8.760029,-9.608269,-1.778003,0.890175,3.536511,-5.737265,-4.840163,-3.576567,-9.277545,9.219049,-5.695803,-1.700119,-4.207058,7.047235,-0.113934,-9.569999,-5.998835,-3.961017,-4.572326,-2.113085,-9.678989,-1.221462,-5.610555,-3.850491,3.729270,-1.066641,-7.107366,5.267472,9.744948,-8.782475,1.294844,1.130070,6.622673,-2.967363,0.751219,8.828529,8.022062,-3.139949,2.949718,-4.539493,3.535326,-4.931228,5.437132,-8.316636,4.090465,-1.255237,6.482604,-4.062861,8.452870,-2.044248,0.584586,8.202574,-5.045239,-8.750208,-0.315923,-7.751176,-6.247364,8.379967,-2.014265,-1.981360,-8.898208,-5.430986,-0.589124,-4.560022,8.081949,9.409534,5.559333,-8.890412,-2.792885,4.563407,6.599389,-8.349847,-5.085124,-0.686242,6.699517,-0.842394,9.739315,-9.221846,1.132197,-2.108962,8.466495,-1.004155,-2.970303,-6.044779,4.345565,1.894450,-3.246827,-9.046752,6.042534,8.105773,-3.977868,-3.493133,4.906867,6.103746,7.518404,2.283008,0.375365,2.058579,-5.221729,0.344579,2.038158,2.829608,-8.072818,1.979653,-0.652882,0.021686,-2.914362,-8.478321,-7.354276,4.533271,7.255144,-5.540006,-9.037047,-1.159612,-5.766655,-0.738939,-1.835298,9.152291,-3.140323,-1.227107,0.367883,6.609098,6.105184,0.757423,0.924921,-2.422473,-9.196109,-7.411472,-4.515108,0.184705,-9.447981,0.821240,5.542158,6.878508,2.229087,-1.194059,9.608540,-7.160575,-1.388010,-0.891706,-2.804149,-3.991169,-7.153838,0.241712,-0.609910,1.773752,0.651784,8.440844,7.569239,-4.342624,6.623818,9.542814,-6.616687,3.962916,-8.581721,-7.028879,-5.542918,2.946816,1.518926,-9.658311,3.172679,-4.603833,-1.202393,-9.729783,7.519634,-4.501867,4.347802,2.275526,4.907104,-6.904358,7.185265,1.392064,-1.050665,-2.400665,9.377172,6.524664,-9.800712,4.394773,1.323934,-3.724458,-1.969826,0.303976,-7.227302,7.075188,-5.399645,7.488741,5.653908,3.743918,6.943288,1.060149,-3.756900,-9.723292,9.755124,6.477027,4.192348,6.621270,-8.231495,3.548373,9.624270,9.098545,5.426450,7.959106,2.851443,-6.236225,-1.014602,7.788626,-5.620860,8.275622,-3.182846,-6.466707,-0.030460,5.659836,7.454544,-1.000789,-7.095155,-9.057308,-1.934143,-4.552412,-8.790449,4.115477,-8.014374,-6.955104,-9.150484,-7.647624,-0.519658,-2.836865,-1.717031,-3.490132,-4.135416,7.896626,-8.464397,-6.390358,1.760192,-0.902713,9.682497,8.487233,-3.315023,-1.087660,8.667844,6.341480,-3.742153,8.646147,-7.062389,-6.376518,-1.344186,6.397500,6.667227,3.004826,-9.934093,-2.963961,4.636969,2.273624,0.470472,-1.257840,4.341619,1.626003,5.678530,-1.390729,-1.556681,5.284081,-1.824362,1.200183,-3.377944,8.659642,-2.008649,5.326981,4.213011,0.392874,-1.166979,0.952519,-2.195974,1.795171,4.534961,6.183262,-5.782681,-1.432866,5.321735,-0.563862,8.445493,-2.114626,-9.148651,5.130357,-8.543167,-5.893474,7.630240,-1.582277,-2.462343,4.919275,-8.495590,5.421930,1.734586,5.401714,6.542508,4.051621,5.913233,-7.219264,8.183758,5.786720,7.019988,-9.148116,-0.433265,-3.450429,4.455901,-4.326639,-2.679569,-4.706944,-1.219844,-8.885319,-5.014242,-4.197679,7.728639,2.597887,-4.572240,-2.493138,-9.963398,-8.697785,-9.065419], dtype = "float32")#candidate|578|(360,)|const|float32
call_577 = func_455_call(relay.reshape(const_578.astype('float32'), [15, 4, 6]))
call_579 = func_455_call(relay.reshape(const_578.astype('float32'), [15, 4, 6]))
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_590 = relay.TupleGetItem(func_319_call(), 1)
call_591 = relay.TupleGetItem(func_321_call(), 1)
output = relay.Tuple([call_547,call_563,call_566,call_577,const_578,call_590,])
output2 = relay.Tuple([call_548,call_564,call_567,call_579,const_578,call_591,])
func_603 = relay.Function([], output)
mod['func_603'] = func_603
mod = relay.transform.InferType()(mod)
mutated_mod['func_603'] = func_603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_603_call = mutated_mod.get_global_var('func_603')
call_604 = func_603_call()
output = call_604
func_605 = relay.Function([], output)
mutated_mod['func_605'] = func_605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_614 = relay.TupleGetItem(func_319_call(), 1)
call_615 = relay.TupleGetItem(func_321_call(), 1)
var_619 = relay.var("var_619", dtype = "bool", shape = (6, 4, 7))#candidate|619|(6, 4, 7)|var|bool
bop_620 = relay.right_shift(call_614.astype('int8'), relay.reshape(var_619.astype('int8'), relay.shape_of(call_614))) # shape=(6, 4, 7)
bop_623 = relay.right_shift(call_615.astype('int8'), relay.reshape(var_619.astype('int8'), relay.shape_of(call_615))) # shape=(6, 4, 7)
func_288_call = mod.get_global_var('func_288')
func_290_call = mutated_mod.get_global_var('func_290')
call_632 = relay.TupleGetItem(func_288_call(), 0)
call_633 = relay.TupleGetItem(func_290_call(), 0)
output = relay.Tuple([bop_620,call_632,])
output2 = relay.Tuple([bop_623,call_633,])
func_635 = relay.Function([var_619,], output)
mod['func_635'] = func_635
mod = relay.transform.InferType()(mod)
mutated_mod['func_635'] = func_635
mutated_mod = relay.transform.InferType()(mutated_mod)
var_636 = relay.var("var_636", dtype = "bool", shape = (6, 4, 7))#candidate|636|(6, 4, 7)|var|bool
func_635_call = mutated_mod.get_global_var('func_635')
call_637 = func_635_call(var_636)
output = call_637
func_638 = relay.Function([var_636], output)
mutated_mod['func_638'] = func_638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_647 = relay.TupleGetItem(func_272_call(), 0)
call_648 = relay.TupleGetItem(func_274_call(), 0)
func_288_call = mod.get_global_var('func_288')
func_290_call = mutated_mod.get_global_var('func_290')
call_668 = relay.TupleGetItem(func_288_call(), 0)
call_669 = relay.TupleGetItem(func_290_call(), 0)
bop_670 = relay.bitwise_xor(call_647.astype('int8'), relay.reshape(call_668.astype('int8'), relay.shape_of(call_647))) # shape=(9, 4, 6)
bop_673 = relay.bitwise_xor(call_648.astype('int8'), relay.reshape(call_669.astype('int8'), relay.shape_of(call_648))) # shape=(9, 4, 6)
func_84_call = mod.get_global_var('func_84')
func_85_call = mutated_mod.get_global_var('func_85')
call_678 = relay.TupleGetItem(func_84_call(), 1)
call_679 = relay.TupleGetItem(func_85_call(), 1)
bop_689 = relay.floor_mod(call_647.astype('float32'), relay.reshape(call_678.astype('float32'), relay.shape_of(call_647))) # shape=(9, 4, 6)
bop_692 = relay.floor_mod(call_648.astype('float32'), relay.reshape(call_679.astype('float32'), relay.shape_of(call_648))) # shape=(9, 4, 6)
bop_714 = relay.less_equal(bop_670.astype('bool'), relay.reshape(bop_689.astype('bool'), relay.shape_of(bop_670))) # shape=(9, 4, 6)
bop_717 = relay.less_equal(bop_673.astype('bool'), relay.reshape(bop_692.astype('bool'), relay.shape_of(bop_673))) # shape=(9, 4, 6)
output = relay.Tuple([bop_714,])
output2 = relay.Tuple([bop_717,])
func_723 = relay.Function([], output)
mod['func_723'] = func_723
mod = relay.transform.InferType()(mod)
output = func_723()
func_724 = relay.Function([], output)
mutated_mod['func_724'] = func_724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_752 = relay.TupleGetItem(func_603_call(), 1)
call_753 = relay.TupleGetItem(func_605_call(), 1)
func_188_call = mod.get_global_var('func_188')
func_191_call = mutated_mod.get_global_var('func_191')
var_772 = relay.var("var_772", dtype = "float32", shape = (168,))#candidate|772|(168,)|var|float32
call_771 = relay.TupleGetItem(func_188_call(relay.reshape(var_772.astype('float32'), [6, 4, 7]), relay.reshape(var_772.astype('float32'), [6, 4, 7]), ), 2)
call_773 = relay.TupleGetItem(func_191_call(relay.reshape(var_772.astype('float32'), [6, 4, 7]), relay.reshape(var_772.astype('float32'), [6, 4, 7]), ), 2)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_777 = relay.TupleGetItem(func_319_call(), 0)
call_778 = relay.TupleGetItem(func_321_call(), 0)
output = relay.Tuple([call_752,call_771,var_772,call_777,])
output2 = relay.Tuple([call_753,call_773,var_772,call_778,])
func_782 = relay.Function([var_772,], output)
mod['func_782'] = func_782
mod = relay.transform.InferType()(mod)
var_783 = relay.var("var_783", dtype = "float32", shape = (168,))#candidate|783|(168,)|var|float32
output = func_782(var_783)
func_784 = relay.Function([var_783], output)
mutated_mod['func_784'] = func_784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_860 = func_39_call()
call_861 = func_39_call()
var_863 = relay.var("var_863", dtype = "bool", shape = (9, 4, 6))#candidate|863|(9, 4, 6)|var|bool
bop_864 = relay.mod(call_860.astype('float32'), relay.reshape(var_863.astype('float32'), relay.shape_of(call_860))) # shape=(9, 4, 6)
bop_867 = relay.mod(call_861.astype('float32'), relay.reshape(var_863.astype('float32'), relay.shape_of(call_861))) # shape=(9, 4, 6)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_877 = func_39_call()
call_878 = func_39_call()
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
var_891 = relay.var("var_891", dtype = "float32", shape = (168,))#candidate|891|(168,)|var|float32
call_890 = relay.TupleGetItem(func_782_call(relay.reshape(var_891.astype('float32'), [168,])), 2)
call_892 = relay.TupleGetItem(func_784_call(relay.reshape(var_891.astype('float32'), [168,])), 2)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_900 = relay.TupleGetItem(func_272_call(), 3)
call_901 = relay.TupleGetItem(func_274_call(), 3)
uop_907 = relay.sqrt(bop_864.astype('float64')) # shape=(9, 4, 6)
uop_909 = relay.sqrt(bop_867.astype('float64')) # shape=(9, 4, 6)
output = relay.Tuple([call_877,call_890,var_891,call_900,uop_907,])
output2 = relay.Tuple([call_878,call_892,var_891,call_901,uop_909,])
func_924 = relay.Function([var_863,var_891,], output)
mod['func_924'] = func_924
mod = relay.transform.InferType()(mod)
var_925 = relay.var("var_925", dtype = "bool", shape = (9, 4, 6))#candidate|925|(9, 4, 6)|var|bool
var_926 = relay.var("var_926", dtype = "float32", shape = (168,))#candidate|926|(168,)|var|float32
output = func_924(var_925,var_926,)
func_927 = relay.Function([var_925,var_926,], output)
mutated_mod['func_927'] = func_927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_950 = relay.TupleGetItem(func_272_call(), 3)
call_951 = relay.TupleGetItem(func_274_call(), 3)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_971 = relay.TupleGetItem(func_782_call(relay.reshape(call_950.astype('float32'), [168,])), 2)
call_972 = relay.TupleGetItem(func_784_call(relay.reshape(call_950.astype('float32'), [168,])), 2)
func_723_call = mod.get_global_var('func_723')
func_724_call = mutated_mod.get_global_var('func_724')
call_977 = relay.TupleGetItem(func_723_call(), 0)
call_978 = relay.TupleGetItem(func_724_call(), 0)
output = relay.Tuple([call_950,call_971,call_977,])
output2 = relay.Tuple([call_951,call_972,call_978,])
func_980 = relay.Function([], output)
mod['func_980'] = func_980
mod = relay.transform.InferType()(mod)
mutated_mod['func_980'] = func_980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_980_call = mutated_mod.get_global_var('func_980')
call_981 = func_980_call()
output = call_981
func_982 = relay.Function([], output)
mutated_mod['func_982'] = func_982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_84_call = mod.get_global_var('func_84')
func_85_call = mutated_mod.get_global_var('func_85')
call_995 = relay.TupleGetItem(func_84_call(), 1)
call_996 = relay.TupleGetItem(func_85_call(), 1)
func_188_call = mod.get_global_var('func_188')
func_191_call = mutated_mod.get_global_var('func_191')
var_1004 = relay.var("var_1004", dtype = "float32", shape = (168,))#candidate|1004|(168,)|var|float32
call_1003 = relay.TupleGetItem(func_188_call(relay.reshape(var_1004.astype('float32'), [6, 4, 7]), relay.reshape(var_1004.astype('float32'), [6, 4, 7]), ), 2)
call_1005 = relay.TupleGetItem(func_191_call(relay.reshape(var_1004.astype('float32'), [6, 4, 7]), relay.reshape(var_1004.astype('float32'), [6, 4, 7]), ), 2)
func_723_call = mod.get_global_var('func_723')
func_724_call = mutated_mod.get_global_var('func_724')
call_1012 = relay.TupleGetItem(func_723_call(), 0)
call_1013 = relay.TupleGetItem(func_724_call(), 0)
uop_1021 = relay.acosh(call_995.astype('float64')) # shape=(9, 4, 6)
uop_1023 = relay.acosh(call_996.astype('float64')) # shape=(9, 4, 6)
func_635_call = mod.get_global_var('func_635')
func_638_call = mutated_mod.get_global_var('func_638')
call_1056 = relay.TupleGetItem(func_635_call(relay.reshape(call_1003.astype('bool'), [6, 4, 7])), 0)
call_1057 = relay.TupleGetItem(func_638_call(relay.reshape(call_1003.astype('bool'), [6, 4, 7])), 0)
uop_1059 = relay.tan(uop_1021.astype('float64')) # shape=(9, 4, 6)
uop_1061 = relay.tan(uop_1023.astype('float64')) # shape=(9, 4, 6)
output = relay.Tuple([call_1003,var_1004,call_1012,call_1056,uop_1059,])
output2 = relay.Tuple([call_1005,var_1004,call_1013,call_1057,uop_1061,])
func_1077 = relay.Function([var_1004,], output)
mod['func_1077'] = func_1077
mod = relay.transform.InferType()(mod)
var_1078 = relay.var("var_1078", dtype = "float32", shape = (168,))#candidate|1078|(168,)|var|float32
output = func_1077(var_1078)
func_1079 = relay.Function([var_1078], output)
mutated_mod['func_1079'] = func_1079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_1095 = relay.TupleGetItem(func_272_call(), 2)
call_1096 = relay.TupleGetItem(func_274_call(), 2)
uop_1100 = relay.sin(call_1095.astype('float32')) # shape=(6, 4, 7)
uop_1102 = relay.sin(call_1096.astype('float32')) # shape=(6, 4, 7)
func_455_call = mod.get_global_var('func_455')
func_458_call = mutated_mod.get_global_var('func_458')
var_1104 = relay.var("var_1104", dtype = "float32", shape = (1, 360))#candidate|1104|(1, 360)|var|float32
call_1103 = func_455_call(relay.reshape(var_1104.astype('float32'), [15, 4, 6]))
call_1105 = func_455_call(relay.reshape(var_1104.astype('float32'), [15, 4, 6]))
output = relay.Tuple([uop_1100,call_1103,var_1104,])
output2 = relay.Tuple([uop_1102,call_1105,var_1104,])
func_1109 = relay.Function([var_1104,], output)
mod['func_1109'] = func_1109
mod = relay.transform.InferType()(mod)
var_1110 = relay.var("var_1110", dtype = "float32", shape = (1, 360))#candidate|1110|(1, 360)|var|float32
output = func_1109(var_1110)
func_1111 = relay.Function([var_1110], output)
mutated_mod['func_1111'] = func_1111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mod.get_global_var('func_723')
func_724_call = mutated_mod.get_global_var('func_724')
call_1113 = relay.TupleGetItem(func_723_call(), 0)
call_1114 = relay.TupleGetItem(func_724_call(), 0)
uop_1122 = relay.cosh(call_1113.astype('float64')) # shape=(9, 4, 6)
uop_1124 = relay.cosh(call_1114.astype('float64')) # shape=(9, 4, 6)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
call_1131 = relay.TupleGetItem(func_980_call(), 1)
call_1132 = relay.TupleGetItem(func_982_call(), 1)
output = relay.Tuple([uop_1122,call_1131,])
output2 = relay.Tuple([uop_1124,call_1132,])
func_1137 = relay.Function([], output)
mod['func_1137'] = func_1137
mod = relay.transform.InferType()(mod)
output = func_1137()
func_1138 = relay.Function([], output)
mutated_mod['func_1138'] = func_1138
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1154 = relay.var("var_1154", dtype = "float64", shape = (9, 12, 10))#candidate|1154|(9, 12, 10)|var|float64
uop_1155 = relay.atanh(var_1154.astype('float64')) # shape=(9, 12, 10)
func_427_call = mod.get_global_var('func_427')
func_428_call = mutated_mod.get_global_var('func_428')
call_1166 = func_427_call()
call_1167 = func_427_call()
var_1183 = relay.var("var_1183", dtype = "float64", shape = (9, 12, 10))#candidate|1183|(9, 12, 10)|var|float64
bop_1184 = relay.equal(var_1154.astype('bool'), relay.reshape(var_1183.astype('bool'), relay.shape_of(var_1154))) # shape=(9, 12, 10)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
call_1206 = relay.TupleGetItem(func_980_call(), 2)
call_1207 = relay.TupleGetItem(func_982_call(), 2)
output = relay.Tuple([uop_1155,call_1166,bop_1184,call_1206,])
output2 = relay.Tuple([uop_1155,call_1167,bop_1184,call_1207,])
func_1210 = relay.Function([var_1154,var_1183,], output)
mod['func_1210'] = func_1210
mod = relay.transform.InferType()(mod)
mutated_mod['func_1210'] = func_1210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1210_call = mutated_mod.get_global_var('func_1210')
var_1212 = relay.var("var_1212", dtype = "float64", shape = (9, 12, 10))#candidate|1212|(9, 12, 10)|var|float64
var_1213 = relay.var("var_1213", dtype = "float64", shape = (9, 12, 10))#candidate|1213|(9, 12, 10)|var|float64
call_1211 = func_1210_call(var_1212,var_1213,)
output = call_1211
func_1214 = relay.Function([var_1212,var_1213,], output)
mutated_mod['func_1214'] = func_1214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_1224 = relay.TupleGetItem(func_319_call(), 2)
call_1225 = relay.TupleGetItem(func_321_call(), 2)
output = call_1224
output2 = call_1225
func_1230 = relay.Function([], output)
mod['func_1230'] = func_1230
mod = relay.transform.InferType()(mod)
mutated_mod['func_1230'] = func_1230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1230_call = mutated_mod.get_global_var('func_1230')
call_1231 = func_1230_call()
output = call_1231
func_1232 = relay.Function([], output)
mutated_mod['func_1232'] = func_1232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_1266 = func_39_call()
call_1267 = func_39_call()
output = relay.Tuple([call_1266,])
output2 = relay.Tuple([call_1267,])
func_1270 = relay.Function([], output)
mod['func_1270'] = func_1270
mod = relay.transform.InferType()(mod)
mutated_mod['func_1270'] = func_1270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1270_call = mutated_mod.get_global_var('func_1270')
call_1271 = func_1270_call()
output = call_1271
func_1272 = relay.Function([], output)
mutated_mod['func_1272'] = func_1272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1137_call = mod.get_global_var('func_1137')
func_1138_call = mutated_mod.get_global_var('func_1138')
call_1273 = relay.TupleGetItem(func_1137_call(), 0)
call_1274 = relay.TupleGetItem(func_1138_call(), 0)
func_455_call = mod.get_global_var('func_455')
func_458_call = mutated_mod.get_global_var('func_458')
var_1288 = relay.var("var_1288", dtype = "float32", shape = (360,))#candidate|1288|(360,)|var|float32
call_1287 = func_455_call(relay.reshape(var_1288.astype('float32'), [15, 4, 6]))
call_1289 = func_455_call(relay.reshape(var_1288.astype('float32'), [15, 4, 6]))
func_1210_call = mod.get_global_var('func_1210')
func_1214_call = mutated_mod.get_global_var('func_1214')
const_1292 = relay.const([-4.401091,5.242116,-5.532923,6.457408,-0.891286,4.996545,5.073844,-9.504146,6.479267,-5.980843,7.716700,-0.102617,5.346466,3.839967,0.490452,-3.185959,-7.422403,6.914313,0.437967,1.702512,-3.688610,-6.384623,8.148884,7.767422,7.064851,4.270398,-9.513300,-1.899187,1.698305,-6.208203,-9.611529,-9.369417,0.973250,3.926352,-8.566207,-7.981696,-0.838469,-7.374391,6.373473,-0.180018,7.805862,1.326145,8.204633,4.519239,-4.126408,2.808782,7.272069,3.872180,5.871389,6.677789,1.894396,-0.796499,-5.059493,-0.274956,-0.421224,2.330646,-9.839620,-1.589820,-4.568411,1.788680,4.957847,-4.256013,-6.141318,1.806431,-5.779311,-0.090194,-7.159325,3.563518,0.279344,-8.170265,-4.614648,-8.355812,4.773155,-7.268106,-5.330371,-8.002656,-6.998352,-7.384893,-8.802782,-6.620497,-3.522908,-0.604523,5.898495,-3.893550,0.283415,6.151724,-5.799563,9.077322,-6.456032,6.372455,6.785211,-3.284049,-8.767817,-9.622216,0.657957,-4.424764,2.570989,-0.023539,-7.210702,-9.760277,-8.859531,-4.937279,5.120954,-8.859853,8.399262,-5.992838,1.402881,7.037628,-5.450247,-1.071463,-7.256464,1.999247,3.204988,0.439165,-4.853190,-9.616627,3.268494,4.712924,-7.215221,-5.532816,-2.456004,-9.446753,4.313016,5.587300,3.195894,4.878210,-8.667626,-6.948922,4.081181,-7.970215,9.681255,-3.554705,3.260579,1.068300,6.610181,5.720539,-7.111607,9.479701,2.691254,7.808679,-5.645497,3.838731,-6.150046,-4.498818,0.447130,4.635162,6.382282,0.636328,-8.719497,-0.862885,-7.793138,8.722766,2.729755,-8.581434,6.567850,-0.578323,8.577821,3.549018,1.126299,2.969014,-8.982209,5.784830,-1.657900,-8.065548,9.316031,-5.874952,-3.086907,-7.553059,-1.091714,1.673088,1.199623,0.869017,9.991241,-9.976255,-3.021856,9.031430,-4.792098,3.102452,0.156962,9.116991,-0.924171,-9.712196,2.655631,4.577516,0.261333,-0.812274,-0.710672,2.957756,-6.322786,-0.544645,6.237279,6.426073,-2.058245,-4.976984,-2.100002,-2.213823,3.766010,1.091697,8.845230,-3.180107,3.637682,0.890007,-4.821457,7.958386,-7.476661,-9.842033,4.405567,-3.926151,-5.995190,5.477572,-0.176961,6.353951,-9.760836,6.557233,9.654858,6.028541,-2.274526,-5.646928,2.885369,1.241116,4.035431,-7.639964,8.500834,-1.612764,1.814786,-2.094541,2.555590,-1.854939,-0.339525,-9.179116,5.069129,1.010145,-4.011093,3.780806,7.357171,-0.929331,-8.875215,-3.102510,0.681041,7.753204,-6.351667,-5.212923,8.874632,-9.107094,-9.496118,-5.817918,-9.083380,8.336958,7.211226,-8.257675,6.228288,-5.144390,2.738509,4.744906,9.447911,-9.299752,-4.836371,-8.384385,9.202277,-2.727064,8.719848,9.261049,-1.316185,-8.219133,1.432469,-8.136583,1.120637,-4.410091,5.765115,0.814516,-0.988382,2.844078,0.386102,3.473250,-9.499090,-2.373874,-7.890779,7.823739,1.421313,-0.165659,-8.257790,8.075922,5.015877,5.607314,-0.689748,-0.603469,-7.231850,5.027870,3.186073,-6.663003,-1.545346,6.059295,-3.516995,5.805068,-3.267752,2.411563,5.274189,8.753032,-7.492670,9.776632,1.827588,-7.922481,6.791526,3.824878,-8.566689,-9.518157,7.688577,3.222398,-0.069770,8.108821,-0.910865,-8.211452,1.045297,8.836100,-7.794311,-2.602753,-4.370092,5.234557,1.495117,-3.622023,-1.570628,-4.659643,-2.631344,9.886880,8.857560,0.403032,7.011998,6.555884,6.677743,5.563889,2.618438,-4.414687,-7.058915,-8.072427,-6.314675,4.442762,2.628864,-8.667202,0.700515,7.568917,-4.459452,-1.963531,-0.770543,6.568616,-4.917495,4.406546,-3.800423,2.418367,9.504046,-5.018098,-1.476304,-3.767875,-6.994369,4.845519,-0.794889,-7.078909,-3.938800,3.982566,-2.352107,-9.896065,9.647271,-4.197322,6.903358,-4.526662,0.904716,2.292702,-8.283376,-5.659564,-9.352711,-8.116211,-9.022321,-9.856167,5.105799,8.186751,-8.996625,6.190609,1.803901,7.364311,5.857850,8.400104,9.096918,0.142640,-4.728029,-3.742644,4.391173,2.458013,4.773317,-1.189947,2.695144,-6.123853,-0.997074,6.292162,3.145846,-9.644656,-3.253844,-7.347925,-1.000029,8.773715,8.893366,-6.673956,-7.344076,-9.096179,2.367215,1.245398,-8.655531,-0.631017,4.565490,-7.604205,-7.244578,8.691660,-7.312825,-9.871669,7.974638,9.756836,5.995186,-0.339271,1.436797,4.213146,0.568311,-0.085827,-5.383600,-6.082215,-7.336485,8.286868,-9.007902,-0.422764,-2.958488,3.144468,-1.025354,-8.540167,-4.233921,-4.601798,6.020617,-5.944272,-3.674478,-3.803093,4.879916,-7.233937,7.819018,3.522100,-7.720713,-0.863712,-7.946275,3.614317,-5.557386,1.953226,-0.827897,-0.740597,5.361931,-1.137056,2.098459,9.862332,-2.578558,1.376479,0.219731,2.108760,-8.455012,-3.269694,4.620486,3.687711,5.061349,4.948346,-6.331789,4.128463,-2.475003,4.369391,-7.437091,6.465166,-1.024480,-8.025993,2.830651,-9.979243,2.627989,-3.429315,-1.355653,-8.881525,-6.353614,9.498799,0.187663,3.693722,-2.635519,-7.731694,4.111632,9.746674,-3.711287,3.715984,7.539420,8.689565,-8.518917,-0.846362,8.434918,-3.831423,-2.153161,0.691357,-5.832210,4.914552,6.913314,1.578782,0.596320,6.408143,-4.438531,6.793661,-9.088793,-4.025230,5.821740,6.493695,2.423931,-2.291929,3.350894,6.891804,-9.605281,-6.999574,-5.639941,-7.141538,6.472457,5.119307,-2.068100,2.409463,5.521682,7.903664,-3.696286,-2.589156,-3.863915,7.256837,-3.128676,7.909206,-4.260104,-2.314247,4.837360,-4.989341,-7.670645,-3.191631,3.385908,7.366567,8.445025,5.260680,6.496001,6.055618,-8.522701,6.537019,-2.304959,-4.371093,7.281974,1.777237,0.552018,0.058303,-1.940834,1.104672,2.571113,-8.114817,5.059167,8.744981,5.636503,2.646494,7.487507,-0.955465,9.356299,-9.874919,-2.476133,-3.352005,-5.926256,5.546754,9.806519,-0.216033,-1.143243,-3.371224,-6.577482,-5.479496,-0.943902,8.244639,6.633144,1.728583,-3.107188,4.618397,-9.047241,8.863168,3.971829,5.644952,1.926716,4.754640,-6.398434,8.453375,8.058188,1.355417,4.393095,-4.480219,-9.623979,-2.709733,2.568641,6.068669,2.406101,-4.318170,-1.986188,6.594400,0.249694,0.874418,-5.521289,-1.552720,-1.167072,-2.015183,3.006435,-8.184983,-0.711542,-4.636366,-9.208604,3.005318,-2.095621,-9.177156,3.196418,-5.452970,6.370737,1.727297,1.399702,4.482057,2.373726,6.190063,-3.154423,-6.275564,-4.686290,0.183071,2.289981,-2.053787,-0.656098,-3.908229,4.747922,4.210271,-9.764150,-3.760813,-8.617563,2.689429,5.813069,-6.756129,8.958274,5.436575,-0.434602,-6.043636,5.164626,5.333124,-7.451938,-8.286159,2.002642,-5.583021,-7.523407,0.951690,-6.331336,-7.238122,8.020740,-5.419872,2.799845,5.865517,-7.957252,2.309756,-2.287545,0.861654,-1.230545,-0.708177,1.096505,5.394427,-8.942434,6.903852,-1.654253,-4.598153,-2.446069,-2.434121,-1.027342,9.738935,2.578254,1.806507,-0.633244,-5.613613,-1.162196,-7.279048,4.887051,4.197568,-1.498785,4.816923,-9.916960,-1.820899,-6.420180,-1.193965,-2.841557,9.067226,0.225442,-5.414883,8.123554,-7.010133,7.623860,-8.771774,4.202607,-3.261084,-3.856328,-2.267406,-1.194429,0.137711,3.259550,0.573848,-0.949689,7.067728,2.625662,7.353603,5.296548,-2.013736,-7.459400,9.350489,-7.674012,3.718061,8.277824,1.708992,-0.040538,-4.466211,8.430955,-0.048629,-2.401293,6.671444,6.111463,9.395254,-4.707453,5.657737,-7.529627,-6.546021,8.369810,5.577441,2.368409,-5.507976,4.518191,3.519086,-7.673047,-4.765128,-1.803494,4.091329,-0.369677,-5.110418,-2.633554,3.667812,-1.193276,-4.007468,6.338300,1.275981,-9.398456,2.528251,-5.820461,-4.255681,-4.197434,-6.534580,-2.587667,-7.569801,-8.303356,-3.746468,-5.831198,9.792583,5.021465,-2.225102,5.542355,-6.171667,5.030355,7.388556,-8.593988,9.905125,7.420994,8.663795,1.486766,-3.914988,-6.643092,-2.092213,4.960043,-9.626726,3.725927,7.714316,-7.567967,1.913305,7.665741,7.171688,-8.722319,-2.397834,-9.862178,-1.348984,4.469763,8.247237,3.367926,1.130819,3.321155,9.361725,-0.360160,7.798771,-7.078399,4.001077,-9.360274,-4.987428,9.490031,-6.642166,-5.171526,3.222929,2.959256,-0.024701,-1.298677,0.243079,3.829687,1.056403,-4.825934,-9.815011,0.344086,-4.594743,-4.052533,-7.968025,-7.913440,-4.257432,2.265369,-1.139658,-2.695328,7.005833,-0.074210,6.360623,-3.582654,-1.099673,5.119336,7.305490,-7.629578,-3.539558,-3.705546,-4.176221,4.468630,-7.183108,-8.484004,-4.728176,0.809396,4.213079,-2.143035,6.263932,0.894392,6.486535,-5.331686,4.514245,6.073490,1.400575,6.286432,-4.018367,-2.348101,8.934074,4.617665,-7.643515,-6.330709,4.081293,-1.950656,3.753549,-3.120337,-6.463134,3.805178,8.058870,-4.550082,3.530933,-6.004165,-9.370329,-0.623411,7.454282,8.176187,-3.675803,9.856167,0.546260,-6.101565,-1.230982,8.692278,9.429304,-7.695002,4.801460,9.524695,-2.290694,-6.030213,8.792063,5.181140,0.765217,-7.767162,-3.709913,7.830155,5.702563,-6.456505,-8.664962,-8.729713,-6.085442,-7.813389,4.462260,-3.303916,3.159958,1.006440,7.964794,9.142333,2.902475,-9.957684,2.872878,4.611121,6.273415,-4.071583,-3.999594,0.982222,-6.251285,-5.213218,-8.332057,7.607066,-1.804349,-5.955368,4.453969,-6.686136,5.868043,-3.756961,-9.915344,2.614057,3.807099,3.467159,-9.738774,6.754826,-8.790411,8.239700,-3.975324,-6.800400,7.152077,6.198237,-1.778347,7.640501,-7.129176,-6.779158,-0.377906,7.836230,-9.142377,0.267429,2.569747,6.607202,-0.444816,-8.063352,5.358495,4.985120,5.356518,-8.273619,-2.873364,5.283611,7.840525,9.750977,1.654591,-5.215493,9.935341,1.950298,-2.722212,-9.224456,1.340902,6.021326,2.740394,4.072368,6.643279,-9.470782,6.527255,0.826002,-4.087429,-4.073063,1.228349,3.137516,-8.345910,1.059885,0.970745,-4.564912,3.995223,2.831224,-2.139155,6.041426,-5.702941,-6.570787,-4.207053,1.616321,-8.326681,-0.456382,-3.211043,8.875188,-5.295996,1.884817,-1.350210,-8.764595,6.351144,2.842812,-4.372033,-2.233414,-6.150766,9.923198,-1.725377,5.146577,-7.918962,-3.323627,9.999871,-7.189110,-0.068178,2.314027,9.187277,-9.964813,-3.099748,-9.910855,8.151111,5.186403,0.740266,-7.772168,8.100990,8.469713,4.822810,-4.279853,5.598114,6.338923,-3.347665,-0.816058,-9.763751,8.762694,-2.546374,-1.039220,-4.009367,-5.475428,-9.816262,7.966882,-3.442528,1.408496,-8.100249,1.822637,-0.140428,8.615692,2.017820,-8.122440,2.245978,-7.463866,-6.798672,2.566250,1.343594,-3.818352,-5.172604,1.296215,-8.405006,-3.398690,2.753283,-2.928938,-1.823336,-8.010126,-5.406489,-6.826550,-3.354818,1.389519,5.228015,0.287967,-2.138401,-8.494445,4.359365,-4.333155,-8.064539,-4.763432,-5.463996,-5.201869,9.315977,-3.860441,6.126204,6.245374,-8.379037,-7.641648,0.916433,-8.851764,-7.788428,-8.050209,-1.542205,7.185316,2.112317,-0.081787,3.110270,6.344414,-2.266693,-3.154672,-0.668441,9.398173,-3.697210,-4.395801,-4.223748,-8.732241,7.799865,-9.048123,9.250558,-9.157678,-5.267296,-6.041257,4.690948,-1.920233,7.336350], dtype = "float64")#candidate|1292|(1080,)|const|float64
call_1291 = relay.TupleGetItem(func_1210_call(relay.reshape(const_1292.astype('float64'), [9, 12, 10]), relay.reshape(const_1292.astype('float64'), [9, 12, 10]), ), 0)
call_1293 = relay.TupleGetItem(func_1214_call(relay.reshape(const_1292.astype('float64'), [9, 12, 10]), relay.reshape(const_1292.astype('float64'), [9, 12, 10]), ), 0)
func_455_call = mod.get_global_var('func_455')
func_458_call = mutated_mod.get_global_var('func_458')
call_1300 = func_455_call(relay.reshape(call_1287.astype('float32'), [15, 4, 6]))
call_1301 = func_455_call(relay.reshape(call_1287.astype('float32'), [15, 4, 6]))
output = relay.Tuple([call_1273,call_1287,var_1288,call_1291,const_1292,call_1300,])
output2 = relay.Tuple([call_1274,call_1289,var_1288,call_1293,const_1292,call_1301,])
func_1302 = relay.Function([var_1288,], output)
mod['func_1302'] = func_1302
mod = relay.transform.InferType()(mod)
mutated_mod['func_1302'] = func_1302
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1303 = relay.var("var_1303", dtype = "float32", shape = (360,))#candidate|1303|(360,)|var|float32
func_1302_call = mutated_mod.get_global_var('func_1302')
call_1304 = func_1302_call(var_1303)
output = call_1304
func_1305 = relay.Function([var_1303], output)
mutated_mod['func_1305'] = func_1305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_1325 = relay.TupleGetItem(func_272_call(), 3)
call_1326 = relay.TupleGetItem(func_274_call(), 3)
output = call_1325
output2 = call_1326
func_1336 = relay.Function([], output)
mod['func_1336'] = func_1336
mod = relay.transform.InferType()(mod)
mutated_mod['func_1336'] = func_1336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1336_call = mutated_mod.get_global_var('func_1336')
call_1337 = func_1336_call()
output = call_1337
func_1338 = relay.Function([], output)
mutated_mod['func_1338'] = func_1338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mod.get_global_var('func_723')
func_724_call = mutated_mod.get_global_var('func_724')
call_1346 = relay.TupleGetItem(func_723_call(), 0)
call_1347 = relay.TupleGetItem(func_724_call(), 0)
output = relay.Tuple([call_1346,])
output2 = relay.Tuple([call_1347,])
func_1388 = relay.Function([], output)
mod['func_1388'] = func_1388
mod = relay.transform.InferType()(mod)
output = func_1388()
func_1389 = relay.Function([], output)
mutated_mod['func_1389'] = func_1389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_55_call = mod.get_global_var('func_55')
func_56_call = mutated_mod.get_global_var('func_56')
call_1393 = relay.TupleGetItem(func_55_call(), 1)
call_1394 = relay.TupleGetItem(func_56_call(), 1)
func_1210_call = mod.get_global_var('func_1210')
func_1214_call = mutated_mod.get_global_var('func_1214')
var_1423 = relay.var("var_1423", dtype = "float64", shape = (1080,))#candidate|1423|(1080,)|var|float64
call_1422 = relay.TupleGetItem(func_1210_call(relay.reshape(var_1423.astype('float64'), [9, 12, 10]), relay.reshape(var_1423.astype('float64'), [9, 12, 10]), ), 1)
call_1424 = relay.TupleGetItem(func_1214_call(relay.reshape(var_1423.astype('float64'), [9, 12, 10]), relay.reshape(var_1423.astype('float64'), [9, 12, 10]), ), 1)
output = relay.Tuple([call_1393,call_1422,var_1423,])
output2 = relay.Tuple([call_1394,call_1424,var_1423,])
func_1435 = relay.Function([var_1423,], output)
mod['func_1435'] = func_1435
mod = relay.transform.InferType()(mod)
var_1436 = relay.var("var_1436", dtype = "float64", shape = (1080,))#candidate|1436|(1080,)|var|float64
output = func_1435(var_1436)
func_1437 = relay.Function([var_1436], output)
mutated_mod['func_1437'] = func_1437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_1479 = relay.TupleGetItem(func_603_call(), 3)
call_1480 = relay.TupleGetItem(func_605_call(), 3)
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_1481 = func_1336_call()
call_1482 = func_1336_call()
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_1483 = relay.TupleGetItem(func_319_call(), 1)
call_1484 = relay.TupleGetItem(func_321_call(), 1)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_1511 = relay.TupleGetItem(func_272_call(), 0)
call_1512 = relay.TupleGetItem(func_274_call(), 0)
output = relay.Tuple([call_1479,call_1481,call_1483,call_1511,])
output2 = relay.Tuple([call_1480,call_1482,call_1484,call_1512,])
func_1515 = relay.Function([], output)
mod['func_1515'] = func_1515
mod = relay.transform.InferType()(mod)
mutated_mod['func_1515'] = func_1515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1515_call = mutated_mod.get_global_var('func_1515')
call_1516 = func_1515_call()
output = call_1516
func_1517 = relay.Function([], output)
mutated_mod['func_1517'] = func_1517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_1533 = func_39_call()
call_1534 = func_39_call()
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
var_1550 = relay.var("var_1550", dtype = "float32", shape = (168,))#candidate|1550|(168,)|var|float32
call_1549 = relay.TupleGetItem(func_782_call(relay.reshape(var_1550.astype('float32'), [168,])), 2)
call_1551 = relay.TupleGetItem(func_784_call(relay.reshape(var_1550.astype('float32'), [168,])), 2)
func_924_call = mod.get_global_var('func_924')
func_927_call = mutated_mod.get_global_var('func_927')
call_1556 = relay.TupleGetItem(func_924_call(relay.reshape(call_1533.astype('bool'), [9, 4, 6]), relay.reshape(call_1549.astype('float32'), [168,]), ), 0)
call_1557 = relay.TupleGetItem(func_927_call(relay.reshape(call_1533.astype('bool'), [9, 4, 6]), relay.reshape(call_1549.astype('float32'), [168,]), ), 0)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
call_1563 = relay.TupleGetItem(func_980_call(), 1)
call_1564 = relay.TupleGetItem(func_982_call(), 1)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_1587 = relay.TupleGetItem(func_272_call(), 1)
call_1588 = relay.TupleGetItem(func_274_call(), 1)
output = relay.Tuple([call_1533,call_1549,var_1550,call_1556,call_1563,call_1587,])
output2 = relay.Tuple([call_1534,call_1551,var_1550,call_1557,call_1564,call_1588,])
func_1597 = relay.Function([var_1550,], output)
mod['func_1597'] = func_1597
mod = relay.transform.InferType()(mod)
mutated_mod['func_1597'] = func_1597
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1598 = relay.var("var_1598", dtype = "float32", shape = (168,))#candidate|1598|(168,)|var|float32
func_1597_call = mutated_mod.get_global_var('func_1597')
call_1599 = func_1597_call(var_1598)
output = call_1599
func_1600 = relay.Function([var_1598], output)
mutated_mod['func_1600'] = func_1600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_1608 = relay.TupleGetItem(func_603_call(), 5)
call_1609 = relay.TupleGetItem(func_605_call(), 5)
const_1611 = relay.const([[[True,True,False,True,False,True,False],[True,False,False,False,True,True,False],[True,False,False,False,True,False,False],[True,True,False,True,False,True,False]],[[False,False,False,True,True,False,False],[False,False,True,True,False,True,True],[True,True,True,False,True,False,False],[True,False,False,False,True,True,True]],[[False,False,True,False,False,True,False],[False,False,False,False,False,True,True],[False,True,True,True,False,False,False],[True,False,False,False,False,True,False]],[[False,False,False,False,False,True,False],[True,True,False,True,True,True,True],[True,False,False,True,True,True,False],[True,False,False,True,False,True,True]],[[True,False,False,True,False,False,True],[False,True,True,True,False,False,False],[True,True,True,False,True,False,True],[True,True,False,False,True,False,True]],[[False,True,True,True,True,True,False],[True,True,True,False,False,False,True],[True,False,False,False,True,True,True],[True,True,False,False,True,False,False]]], dtype = "bool")#candidate|1611|(6, 4, 7)|const|bool
bop_1612 = relay.minimum(call_1608.astype('uint16'), relay.reshape(const_1611.astype('uint16'), relay.shape_of(call_1608))) # shape=(6, 4, 7)
bop_1615 = relay.minimum(call_1609.astype('uint16'), relay.reshape(const_1611.astype('uint16'), relay.shape_of(call_1609))) # shape=(6, 4, 7)
func_188_call = mod.get_global_var('func_188')
func_191_call = mutated_mod.get_global_var('func_191')
call_1616 = relay.TupleGetItem(func_188_call(relay.reshape(const_1611.astype('float32'), [6, 4, 7]), relay.reshape(const_1611.astype('float32'), [6, 4, 7]), ), 0)
call_1617 = relay.TupleGetItem(func_191_call(relay.reshape(const_1611.astype('float32'), [6, 4, 7]), relay.reshape(const_1611.astype('float32'), [6, 4, 7]), ), 0)
func_924_call = mod.get_global_var('func_924')
func_927_call = mutated_mod.get_global_var('func_927')
var_1621 = relay.var("var_1621", dtype = "bool", shape = (216,))#candidate|1621|(216,)|var|bool
call_1620 = relay.TupleGetItem(func_924_call(relay.reshape(var_1621.astype('bool'), [9, 4, 6]), relay.reshape(call_1616.astype('float32'), [168,]), ), 4)
call_1622 = relay.TupleGetItem(func_927_call(relay.reshape(var_1621.astype('bool'), [9, 4, 6]), relay.reshape(call_1616.astype('float32'), [168,]), ), 4)
output = relay.Tuple([bop_1612,call_1616,call_1620,var_1621,])
output2 = relay.Tuple([bop_1615,call_1617,call_1622,var_1621,])
func_1626 = relay.Function([var_1621,], output)
mod['func_1626'] = func_1626
mod = relay.transform.InferType()(mod)
var_1627 = relay.var("var_1627", dtype = "bool", shape = (216,))#candidate|1627|(216,)|var|bool
output = func_1626(var_1627)
func_1628 = relay.Function([var_1627], output)
mutated_mod['func_1628'] = func_1628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_427_call = mod.get_global_var('func_427')
func_428_call = mutated_mod.get_global_var('func_428')
call_1674 = func_427_call()
call_1675 = func_427_call()
func_1515_call = mod.get_global_var('func_1515')
func_1517_call = mutated_mod.get_global_var('func_1517')
call_1721 = relay.TupleGetItem(func_1515_call(), 1)
call_1722 = relay.TupleGetItem(func_1517_call(), 1)
func_288_call = mod.get_global_var('func_288')
func_290_call = mutated_mod.get_global_var('func_290')
call_1740 = relay.TupleGetItem(func_288_call(), 0)
call_1741 = relay.TupleGetItem(func_290_call(), 0)
output = relay.Tuple([call_1674,call_1721,call_1740,])
output2 = relay.Tuple([call_1675,call_1722,call_1741,])
func_1743 = relay.Function([], output)
mod['func_1743'] = func_1743
mod = relay.transform.InferType()(mod)
mutated_mod['func_1743'] = func_1743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1743_call = mutated_mod.get_global_var('func_1743')
call_1744 = func_1743_call()
output = call_1744
func_1745 = relay.Function([], output)
mutated_mod['func_1745'] = func_1745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_1753 = func_39_call()
call_1754 = func_39_call()
uop_1755 = relay.acos(call_1753.astype('float64')) # shape=(9, 4, 6)
uop_1757 = relay.acos(call_1754.astype('float64')) # shape=(9, 4, 6)
output = uop_1755
output2 = uop_1757
func_1763 = relay.Function([], output)
mod['func_1763'] = func_1763
mod = relay.transform.InferType()(mod)
output = func_1763()
func_1764 = relay.Function([], output)
mutated_mod['func_1764'] = func_1764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_1767 = relay.TupleGetItem(func_603_call(), 4)
call_1768 = relay.TupleGetItem(func_605_call(), 4)
output = call_1767
output2 = call_1768
func_1774 = relay.Function([], output)
mod['func_1774'] = func_1774
mod = relay.transform.InferType()(mod)
mutated_mod['func_1774'] = func_1774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1774_call = mutated_mod.get_global_var('func_1774')
call_1775 = func_1774_call()
output = call_1775
func_1776 = relay.Function([], output)
mutated_mod['func_1776'] = func_1776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_84_call = mod.get_global_var('func_84')
func_85_call = mutated_mod.get_global_var('func_85')
call_1780 = relay.TupleGetItem(func_84_call(), 1)
call_1781 = relay.TupleGetItem(func_85_call(), 1)
var_1784 = relay.var("var_1784", dtype = "bool", shape = (9, 4, 6))#candidate|1784|(9, 4, 6)|var|bool
bop_1785 = relay.not_equal(call_1780.astype('bool'), relay.reshape(var_1784.astype('bool'), relay.shape_of(call_1780))) # shape=(9, 4, 6)
bop_1788 = relay.not_equal(call_1781.astype('bool'), relay.reshape(var_1784.astype('bool'), relay.shape_of(call_1781))) # shape=(9, 4, 6)
output = relay.Tuple([bop_1785,])
output2 = relay.Tuple([bop_1788,])
func_1805 = relay.Function([var_1784,], output)
mod['func_1805'] = func_1805
mod = relay.transform.InferType()(mod)
var_1806 = relay.var("var_1806", dtype = "bool", shape = (9, 4, 6))#candidate|1806|(9, 4, 6)|var|bool
output = func_1805(var_1806)
func_1807 = relay.Function([var_1806], output)
mutated_mod['func_1807'] = func_1807
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1811 = relay.var("var_1811", dtype = "float32", shape = (13, 9, 1))#candidate|1811|(13, 9, 1)|var|float32
uop_1812 = relay.log10(var_1811.astype('float32')) # shape=(13, 9, 1)
uop_1814 = relay.acos(uop_1812.astype('float64')) # shape=(13, 9, 1)
func_1515_call = mod.get_global_var('func_1515')
func_1517_call = mutated_mod.get_global_var('func_1517')
call_1820 = relay.TupleGetItem(func_1515_call(), 3)
call_1821 = relay.TupleGetItem(func_1517_call(), 3)
output = relay.Tuple([uop_1814,call_1820,])
output2 = relay.Tuple([uop_1814,call_1821,])
func_1834 = relay.Function([var_1811,], output)
mod['func_1834'] = func_1834
mod = relay.transform.InferType()(mod)
var_1835 = relay.var("var_1835", dtype = "float32", shape = (13, 9, 1))#candidate|1835|(13, 9, 1)|var|float32
output = func_1834(var_1835)
func_1836 = relay.Function([var_1835], output)
mutated_mod['func_1836'] = func_1836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1763_call = mod.get_global_var('func_1763')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_1896 = func_1763_call()
call_1897 = func_1763_call()
func_1834_call = mod.get_global_var('func_1834')
func_1836_call = mutated_mod.get_global_var('func_1836')
const_1901 = relay.const([5.095633,-1.706638,8.476518,6.395698,4.814829,-0.668373,2.339334,7.470130,7.592931,-8.282747,-1.319417,9.275848,-7.334240,-3.208641,-0.365851,1.838739,6.403969,9.494375,-7.484939,-6.759907,-8.877620,-3.955107,-5.264761,-1.296039,-9.261150,6.063659,-4.630667,-9.373625,-1.825351,-0.800671,5.435738,-1.007115,0.032725,7.531242,-3.971165,4.599724,2.662895,-7.760061,-7.892501,7.917589,9.976398,8.154785,9.327851,-8.162145,6.420158,-4.547895,5.209924,5.062462,4.314138,-3.006630,-5.340335,-9.351362,-5.762614,3.755730,3.684493,5.902558,3.095626,-0.099215,0.348420,-2.403891,-5.486741,8.454281,6.740811,-6.615405,0.269833,7.490281,7.756338,1.327155,-9.666227,-8.322579,8.254266,7.207164,-3.814607,-1.670435,-3.607271,-4.120132,5.694205,-2.318037,-4.892889,6.464778,-3.849610,6.558396,2.513748,7.566299,-3.463017,6.694974,3.394297,-2.065429,7.411818,0.741816,-4.675430,-5.844484,1.445884,-1.959248,8.803248,-0.128471,-0.975950,0.818460,-9.649358,-5.656223,-1.274711,9.342181,-9.509854,-6.067423,-0.039533,2.644556,4.851540,-1.557942,5.038340,9.893842,4.326838,-2.400335,5.060632,3.341628,-3.169117,-5.892151,8.768994], dtype = "float32")#candidate|1901|(117,)|const|float32
call_1900 = relay.TupleGetItem(func_1834_call(relay.reshape(const_1901.astype('float32'), [13, 9, 1])), 1)
call_1902 = relay.TupleGetItem(func_1836_call(relay.reshape(const_1901.astype('float32'), [13, 9, 1])), 1)
var_1903 = relay.var("var_1903", dtype = "float64", shape = (9, 4, 6))#candidate|1903|(9, 4, 6)|var|float64
bop_1904 = relay.minimum(call_1896.astype('uint16'), relay.reshape(var_1903.astype('uint16'), relay.shape_of(call_1896))) # shape=(9, 4, 6)
bop_1907 = relay.minimum(call_1897.astype('uint16'), relay.reshape(var_1903.astype('uint16'), relay.shape_of(call_1897))) # shape=(9, 4, 6)
output = relay.Tuple([call_1900,const_1901,bop_1904,])
output2 = relay.Tuple([call_1902,const_1901,bop_1907,])
func_1908 = relay.Function([var_1903,], output)
mod['func_1908'] = func_1908
mod = relay.transform.InferType()(mod)
mutated_mod['func_1908'] = func_1908
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1909 = relay.var("var_1909", dtype = "float64", shape = (9, 4, 6))#candidate|1909|(9, 4, 6)|var|float64
func_1908_call = mutated_mod.get_global_var('func_1908')
call_1910 = func_1908_call(var_1909)
output = call_1910
func_1911 = relay.Function([var_1909], output)
mutated_mod['func_1911'] = func_1911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_1927 = relay.TupleGetItem(func_1270_call(), 0)
call_1928 = relay.TupleGetItem(func_1272_call(), 0)
func_1077_call = mod.get_global_var('func_1077')
func_1079_call = mutated_mod.get_global_var('func_1079')
var_1942 = relay.var("var_1942", dtype = "float32", shape = (168, 1))#candidate|1942|(168, 1)|var|float32
call_1941 = relay.TupleGetItem(func_1077_call(relay.reshape(var_1942.astype('float32'), [168,])), 1)
call_1943 = relay.TupleGetItem(func_1079_call(relay.reshape(var_1942.astype('float32'), [168,])), 1)
func_455_call = mod.get_global_var('func_455')
func_458_call = mutated_mod.get_global_var('func_458')
const_1945 = relay.const([-0.757260,-9.069779,6.215956,-2.424860,7.198596,2.765496,-7.673097,0.047709,0.148330,5.645897,-8.249942,8.714137,1.894275,-3.604694,-7.359396,3.303619,9.248334,7.189395,-1.931492,0.613744,-8.212262,6.540157,-4.422234,4.277830,-0.982505,3.923086,-6.874531,0.116477,6.788551,6.076331,-8.875690,-8.313220,-5.680894,-2.243908,-3.637076,-0.052489,1.563170,0.096594,6.112882,6.624542,7.024117,-1.091848,9.283886,9.870536,7.214952,-3.106036,5.291166,-0.759697,-3.497075,-9.733614,-7.422723,9.330651,-7.246557,-8.461196,5.375482,-2.799706,-9.669892,2.100262,-7.758152,6.025008,7.045359,2.455210,-2.483036,-0.607259,-1.775400,4.355105,9.020575,-9.545121,6.276832,9.176294,2.280655,5.581128,-6.794333,7.953406,6.057446,8.840622,6.724774,0.283617,-9.571258,-6.394528,-4.436835,7.935884,8.989720,-2.089368,-6.596121,1.556043,1.835811,-5.041706,2.414608,-2.884395,-4.996574,6.440856,-3.899993,4.053133,-1.189232,8.232402,-2.240101,8.658855,3.845289,-0.065421,8.611839,2.558616,8.686438,1.787128,4.967018,6.963078,3.577294,6.250468,-4.425511,-0.375355,7.871085,1.280383,-3.826866,8.712939,-0.078369,-2.626839,7.895595,-0.995850,0.427768,-2.609135,2.176096,-6.308503,-4.365557,-2.359607,-3.055020,-1.129054,5.852595,9.497815,-2.885378,6.671846,0.371178,-5.293277,8.487883,2.279074,-2.171688,2.697286,5.652517,-8.068590,-0.181190,-8.674830,8.166789,-4.536207,7.297830,0.620174,-0.144566,-5.957943,-2.948663,-4.915328,-4.671297,-2.071156,6.178456,-0.081316,9.684679,1.395111,-8.659505,-3.331340,-5.810757,-4.880485,8.514830,5.933942,-1.873791,4.503825,-4.542140,-2.117146,3.541777,-1.744935,-7.213133,1.534266,4.222561,8.670200,2.332589,-1.473101,-0.409819,3.777756,-3.609129,3.143626,-3.374630,5.614406,1.851189,7.168051,-2.742405,3.958966,8.091438,-2.246507,7.819683,-1.385293,6.791167,-9.333216,5.813753,4.331456,-0.906739,-3.517101,2.729577,-2.779057,7.666475,9.743340,9.682478,-2.732816,-3.356298,5.468783,8.640089,-2.882336,-7.641740,-8.180747,-1.139106,8.729012,9.590234,3.110589,5.399758,9.720052,-6.315427,-5.641310,8.226271,-6.158439,2.961664,-4.016770,5.025261,-7.578322,9.667640,4.306808,-4.557474,7.431832,-7.620207,3.260629,-4.178604,-4.352182,0.347291,-8.664659,0.480896,-3.438505,-6.834989,2.597390,6.991032,-8.068426,8.005013,-9.985428,-3.764613,6.585804,2.190168,6.921036,5.686259,-9.299101,-8.023299,4.971734,7.904696,3.358588,-0.740447,5.926760,-0.032840,4.434139,6.087497,4.086423,2.022512,-7.129985,9.948071,-1.302563,4.121273,-0.060102,6.903154,8.881497,1.404830,-8.434828,-4.870951,-5.173164,8.554543,-7.754452,9.418073,3.102519,-8.024892,6.980427,6.302731,-4.836900,-5.696162,-4.258230,-3.437788,-1.152356,-4.855469,-9.787553,-7.258661,1.374458,-5.769054,-9.906648,-6.485057,-4.861748,0.733864,-9.624839,3.712627,8.771380,7.330297,8.330025,-7.844096,-0.740376,-7.674310,8.850420,4.868689,3.513385,-2.865000,1.908186,0.727762,0.528851,-8.550931,1.871580,-7.562807,1.149748,-2.862846,4.328993,7.983326,-0.251959,-3.631130,-5.497167,-9.375088,1.436300,-5.848353,2.720971,-8.472126,-1.030641,5.909620,-9.008217,1.210654,4.667739,-9.258670,-9.096264,-8.411361,-8.036294,-8.825671,-1.934433,-7.959542,2.181453,7.667384,-7.049096,4.734404,-9.798452,-0.373183,-8.756793,-8.824164,8.375809,-4.862299,-2.123675,-9.741744,-0.112669,-6.854284,-1.229317,-6.552905,2.998951,-8.894078,-1.366183,-9.592846,-1.792270,4.674102,-4.434871,1.741183,8.353877,4.193649,-6.429410,-3.023717,-5.107864,-1.666488,7.625624,-1.866738,-3.669537], dtype = "float32")#candidate|1945|(360,)|const|float32
call_1944 = func_455_call(relay.reshape(const_1945.astype('float32'), [15, 4, 6]))
call_1946 = func_455_call(relay.reshape(const_1945.astype('float32'), [15, 4, 6]))
func_1302_call = mod.get_global_var('func_1302')
func_1305_call = mutated_mod.get_global_var('func_1305')
call_1947 = relay.TupleGetItem(func_1302_call(relay.reshape(const_1945.astype('float32'), [360,])), 4)
call_1948 = relay.TupleGetItem(func_1305_call(relay.reshape(const_1945.astype('float32'), [360,])), 4)
output = relay.Tuple([call_1927,call_1941,var_1942,call_1944,const_1945,call_1947,])
output2 = relay.Tuple([call_1928,call_1943,var_1942,call_1946,const_1945,call_1948,])
func_1960 = relay.Function([var_1942,], output)
mod['func_1960'] = func_1960
mod = relay.transform.InferType()(mod)
var_1961 = relay.var("var_1961", dtype = "float32", shape = (168, 1))#candidate|1961|(168, 1)|var|float32
output = func_1960(var_1961)
func_1962 = relay.Function([var_1961], output)
mutated_mod['func_1962'] = func_1962
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1983 = relay.const([[[7.770293,-1.513221,1.292190,6.393974,5.322435,-6.483327,8.868681,-5.830061,4.003361,9.173146,-8.310912],[8.972707,-2.169953,3.245139,-5.319924,-8.452130,-5.908718,6.819184,1.222685,7.035426,-4.716121,-6.354446],[7.028181,2.866858,-1.455646,-4.191448,-8.737734,-2.239117,-8.094366,5.940474,-0.505967,5.531329,-4.918256],[8.019716,1.677755,8.025224,-2.421079,8.256868,-3.442996,-3.924270,-3.808998,4.614516,-2.490431,5.885488],[1.431626,9.627393,-2.996488,3.129536,-1.277868,-7.784525,3.343530,8.913728,-4.652712,-4.486048,5.353589],[4.379234,9.686757,-9.581593,-2.439910,6.428773,-5.287020,5.882294,5.527921,-9.304737,8.268811,2.212586],[-1.103844,4.526259,-8.343758,0.692302,-8.291332,8.614298,6.965022,-1.810837,6.511910,8.058001,-0.923028],[-9.683595,3.416234,1.935199,-8.986960,-0.819973,7.617362,4.626168,9.670007,5.991361,4.166459,6.834977],[1.945419,-7.633133,1.536178,-0.869763,-8.069497,4.512402,3.351395,8.432919,-7.790878,-1.281840,2.731810],[6.914952,-4.559021,-5.212521,1.978902,-9.399013,6.415640,9.959693,7.502812,0.659750,-4.519027,7.768113],[7.104113,1.659234,-9.149641,-8.979233,9.124593,-6.297732,-5.608460,3.754419,9.443339,-0.966386,-5.989913],[5.549445,-6.511868,-6.539345,-6.354849,-9.166906,-6.331156,7.599808,-5.857785,-4.576006,7.462946,5.498257],[3.998650,7.009584,4.910723,-7.718646,2.575112,5.498799,-3.030542,-8.659792,9.454913,-7.844827,1.515756]]], dtype = "float32")#candidate|1983|(1, 13, 11)|const|float32
uop_1984 = relay.log2(const_1983.astype('float32')) # shape=(1, 13, 11)
func_288_call = mod.get_global_var('func_288')
func_290_call = mutated_mod.get_global_var('func_290')
call_1989 = relay.TupleGetItem(func_288_call(), 0)
call_1990 = relay.TupleGetItem(func_290_call(), 0)
uop_1992 = relay.exp(call_1989.astype('float32')) # shape=(9, 4, 6)
uop_1994 = relay.exp(call_1990.astype('float32')) # shape=(9, 4, 6)
func_188_call = mod.get_global_var('func_188')
func_191_call = mutated_mod.get_global_var('func_191')
const_2001 = relay.const([[-8.737971,-3.200458,0.204587,-5.495067,1.244064,-1.188455,-6.702592,0.448138,0.004044,-3.890446,0.339457,8.231978,7.114298,3.851319,4.933542,-6.051715,5.503862,6.973426,-6.385030,8.514215,-8.817681,6.385410,-6.560010,-5.623390,2.983505,-2.299400,-7.252729,-6.573059],[-3.578913,7.083736,-9.235711,-3.274362,-3.081951,-0.743251,6.514026,-9.968238,7.077558,0.620201,5.595206,3.735913,-5.225372,7.795515,0.059781,-1.048025,1.372395,-6.137406,1.990170,4.609569,-5.928160,-2.530794,0.104651,9.437510,-1.176157,-6.926106,-9.273874,-3.046274],[-0.962888,1.874071,5.009628,7.496201,1.053476,-4.229652,-8.813220,-1.818111,9.544555,7.147808,-9.943563,-1.190653,5.454345,-6.002310,-5.133037,-0.853931,-6.464183,7.130492,3.294867,7.591504,-9.487118,9.492427,0.025987,2.660246,-0.571875,-0.938090,-1.958414,7.900790],[2.193552,0.698039,-7.240502,-8.733409,-1.563345,-1.913665,3.694851,-0.337719,1.395405,-4.402738,-1.688668,2.468999,-3.510510,7.679085,-6.639495,-0.988069,-6.147507,-2.854333,2.339055,8.152167,-0.697803,9.296935,0.377098,5.941158,8.502307,-4.885281,3.326796,-6.298952],[1.034079,-1.836757,-4.451708,5.163538,0.925778,0.673677,4.693104,-2.618345,-0.907281,9.581094,4.694968,-8.385209,-3.263104,-8.602067,9.595796,-1.609507,-6.284896,-6.253207,0.199073,7.060954,1.477373,-3.884646,-6.988237,-2.045882,-8.127826,-7.530792,-3.690483,6.765057],[0.530575,7.613011,-9.606819,2.448225,-6.417843,-5.173943,-4.941446,-9.681150,-7.698399,-7.370215,5.628701,-4.518846,-6.686647,-8.519938,0.597667,5.537859,8.278073,6.887844,-6.203462,2.545819,5.158908,6.013032,8.206750,7.434980,-8.866523,-7.188931,0.142640,2.231559]], dtype = "float32")#candidate|2001|(6, 28)|const|float32
call_2000 = relay.TupleGetItem(func_188_call(relay.reshape(const_2001.astype('float32'), [6, 4, 7]), relay.reshape(const_2001.astype('float32'), [6, 4, 7]), ), 0)
call_2002 = relay.TupleGetItem(func_191_call(relay.reshape(const_2001.astype('float32'), [6, 4, 7]), relay.reshape(const_2001.astype('float32'), [6, 4, 7]), ), 0)
bop_2006 = relay.less_equal(uop_1984.astype('bool'), relay.reshape(const_1983.astype('bool'), relay.shape_of(uop_1984))) # shape=(1, 13, 11)
output = relay.Tuple([uop_1992,call_2000,const_2001,bop_2006,])
output2 = relay.Tuple([uop_1994,call_2002,const_2001,bop_2006,])
func_2010 = relay.Function([], output)
mod['func_2010'] = func_2010
mod = relay.transform.InferType()(mod)
output = func_2010()
func_2011 = relay.Function([], output)
mutated_mod['func_2011'] = func_2011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_2023 = func_1336_call()
call_2024 = func_1336_call()
func_1626_call = mod.get_global_var('func_1626')
func_1628_call = mutated_mod.get_global_var('func_1628')
const_2031 = relay.const([True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False], dtype = "bool")#candidate|2031|(216,)|const|bool
call_2030 = relay.TupleGetItem(func_1626_call(relay.reshape(const_2031.astype('bool'), [216,])), 2)
call_2032 = relay.TupleGetItem(func_1628_call(relay.reshape(const_2031.astype('bool'), [216,])), 2)
func_1805_call = mod.get_global_var('func_1805')
func_1807_call = mutated_mod.get_global_var('func_1807')
call_2089 = relay.TupleGetItem(func_1805_call(relay.reshape(const_2031.astype('bool'), [9, 4, 6])), 0)
call_2090 = relay.TupleGetItem(func_1807_call(relay.reshape(const_2031.astype('bool'), [9, 4, 6])), 0)
func_1077_call = mod.get_global_var('func_1077')
func_1079_call = mutated_mod.get_global_var('func_1079')
call_2091 = relay.TupleGetItem(func_1077_call(relay.reshape(call_2023.astype('float32'), [168,])), 4)
call_2092 = relay.TupleGetItem(func_1079_call(relay.reshape(call_2023.astype('float32'), [168,])), 4)
output = relay.Tuple([call_2023,call_2030,const_2031,call_2089,call_2091,])
output2 = relay.Tuple([call_2024,call_2032,const_2031,call_2090,call_2092,])
func_2094 = relay.Function([], output)
mod['func_2094'] = func_2094
mod = relay.transform.InferType()(mod)
mutated_mod['func_2094'] = func_2094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2094_call = mutated_mod.get_global_var('func_2094')
call_2095 = func_2094_call()
output = call_2095
func_2096 = relay.Function([], output)
mutated_mod['func_2096'] = func_2096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_2113 = func_39_call()
call_2114 = func_39_call()
output = call_2113
output2 = call_2114
func_2118 = relay.Function([], output)
mod['func_2118'] = func_2118
mod = relay.transform.InferType()(mod)
mutated_mod['func_2118'] = func_2118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2118_call = mutated_mod.get_global_var('func_2118')
call_2119 = func_2118_call()
output = call_2119
func_2120 = relay.Function([], output)
mutated_mod['func_2120'] = func_2120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1774_call = mod.get_global_var('func_1774')
func_1776_call = mutated_mod.get_global_var('func_1776')
call_2135 = func_1774_call()
call_2136 = func_1774_call()
func_1908_call = mod.get_global_var('func_1908')
func_1911_call = mutated_mod.get_global_var('func_1911')
const_2140 = relay.const([-1.789800,5.822807,2.507687,1.907226,7.467973,-9.974031,-7.066724,1.644254,-8.161846,7.521844,-0.850377,-3.805772,-1.078483,-9.003455,9.348536,1.927542,-0.015728,2.511565,9.558340,9.568687,1.801438,2.082001,-3.478589,1.522256,-3.111238,1.228190,1.260259,6.145763,3.661695,2.372621,-9.928347,-6.125788,-2.153089,-6.419491,-6.773550,-2.564609,4.173186,4.410405,-5.157471,8.952013,5.580778,2.792304,-9.285779,-2.412133,-1.053801,-7.309861,5.545727,-0.937982,9.474504,1.640014,-7.986927,1.532377,4.196936,7.978403,5.315716,-5.607282,2.117890,-3.427723,7.949494,5.844822,-3.981380,-0.543862,-9.444982,0.942732,8.638317,0.270733,-6.634184,-1.591724,-4.680699,7.075763,-1.768044,-3.902832,-6.061292,7.833639,-7.596253,4.468081,1.641023,-2.166423,-4.506140,5.165377,-9.719284,1.809376,9.203701,1.283339,-7.064622,4.147910,-8.159449,-6.843244,-4.652495,-9.907011,6.892627,-3.006784,0.766177,-1.894448,-7.459653,-0.337486,5.262483,-9.222311,3.151037,-7.998916,-3.006314,-7.866606,4.860319,1.791236,-7.671963,-5.973160,-0.494097,-9.000192,5.666927,2.711323,-9.316664,2.212331,-6.924186,-0.291241,9.060920,1.766310,0.928502,-0.167041,-6.407937,-8.281438,-9.452357,-7.520055,5.738724,-8.626011,-3.103478,4.396529,7.192189,-9.469047,-9.542543,9.402271,0.718918,1.884901,-3.791546,7.636628,-2.772999,-5.040673,2.007190,4.955055,3.798095,0.500913,4.198329,9.309547,5.523580,-5.032824,-0.002093,9.262051,-1.898596,-1.741058,6.654952,-7.400038,-2.726403,-6.482122,1.977710,-9.375140,8.208606,-2.262278,-9.230015,-0.037188,9.779259,7.949723,-7.276796,9.068434,-5.556084,-9.711020,-2.081125,5.412215,1.466414,-9.174575,5.347484,4.555418,-0.077270,1.217144,3.737827,9.960552,2.202678,2.359773,6.164451,-0.112425,-7.470217,6.486287,3.229617,8.914087,-5.656298,-9.717822,2.891188,1.868744,0.052731,-1.141503,-0.811469,-1.531058,7.943163,9.851965,-5.321682,-7.491498,-8.457763,6.846526,-3.908788,-4.487950,-7.113625,-7.106856,7.605124,-4.996707,-3.327816,0.908690,-7.861589,-1.146912,9.951133,-8.515218,-0.687078,6.005733,3.307643,-6.775571,8.987830,-6.973822,2.170979,8.121733], dtype = "float64")#candidate|2140|(216,)|const|float64
call_2139 = relay.TupleGetItem(func_1908_call(relay.reshape(const_2140.astype('float64'), [9, 4, 6])), 0)
call_2141 = relay.TupleGetItem(func_1911_call(relay.reshape(const_2140.astype('float64'), [9, 4, 6])), 0)
func_1805_call = mod.get_global_var('func_1805')
func_1807_call = mutated_mod.get_global_var('func_1807')
call_2147 = relay.TupleGetItem(func_1805_call(relay.reshape(const_2140.astype('bool'), [9, 4, 6])), 0)
call_2148 = relay.TupleGetItem(func_1807_call(relay.reshape(const_2140.astype('bool'), [9, 4, 6])), 0)
bop_2165 = relay.power(call_2147.astype('float32'), relay.reshape(const_2140.astype('float32'), relay.shape_of(call_2147))) # shape=(9, 4, 6)
bop_2168 = relay.power(call_2148.astype('float32'), relay.reshape(const_2140.astype('float32'), relay.shape_of(call_2148))) # shape=(9, 4, 6)
func_1515_call = mod.get_global_var('func_1515')
func_1517_call = mutated_mod.get_global_var('func_1517')
call_2169 = relay.TupleGetItem(func_1515_call(), 2)
call_2170 = relay.TupleGetItem(func_1517_call(), 2)
output = relay.Tuple([call_2135,call_2139,bop_2165,call_2169,])
output2 = relay.Tuple([call_2136,call_2141,bop_2168,call_2170,])
func_2173 = relay.Function([], output)
mod['func_2173'] = func_2173
mod = relay.transform.InferType()(mod)
mutated_mod['func_2173'] = func_2173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mutated_mod.get_global_var('func_2173')
call_2174 = func_2173_call()
output = call_2174
func_2175 = relay.Function([], output)
mutated_mod['func_2175'] = func_2175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_2193 = relay.TupleGetItem(func_2173_call(), 1)
call_2194 = relay.TupleGetItem(func_2175_call(), 1)
output = call_2193
output2 = call_2194
func_2211 = relay.Function([], output)
mod['func_2211'] = func_2211
mod = relay.transform.InferType()(mod)
output = func_2211()
func_2212 = relay.Function([], output)
mutated_mod['func_2212'] = func_2212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_84_call = mod.get_global_var('func_84')
func_85_call = mutated_mod.get_global_var('func_85')
call_2230 = relay.TupleGetItem(func_84_call(), 1)
call_2231 = relay.TupleGetItem(func_85_call(), 1)
output = call_2230
output2 = call_2231
func_2264 = relay.Function([], output)
mod['func_2264'] = func_2264
mod = relay.transform.InferType()(mod)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2264_call = mutated_mod.get_global_var('func_2264')
call_2265 = func_2264_call()
output = call_2265
func_2266 = relay.Function([], output)
mutated_mod['func_2266'] = func_2266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_2267 = relay.TupleGetItem(func_603_call(), 4)
call_2268 = relay.TupleGetItem(func_605_call(), 4)
func_288_call = mod.get_global_var('func_288')
func_290_call = mutated_mod.get_global_var('func_290')
call_2285 = relay.TupleGetItem(func_288_call(), 0)
call_2286 = relay.TupleGetItem(func_290_call(), 0)
func_635_call = mod.get_global_var('func_635')
func_638_call = mutated_mod.get_global_var('func_638')
var_2300 = relay.var("var_2300", dtype = "bool", shape = (1, 168))#candidate|2300|(1, 168)|var|bool
call_2299 = relay.TupleGetItem(func_635_call(relay.reshape(var_2300.astype('bool'), [6, 4, 7])), 0)
call_2301 = relay.TupleGetItem(func_638_call(relay.reshape(var_2300.astype('bool'), [6, 4, 7])), 0)
output = relay.Tuple([call_2267,call_2285,call_2299,var_2300,])
output2 = relay.Tuple([call_2268,call_2286,call_2301,var_2300,])
func_2306 = relay.Function([var_2300,], output)
mod['func_2306'] = func_2306
mod = relay.transform.InferType()(mod)
mutated_mod['func_2306'] = func_2306
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2307 = relay.var("var_2307", dtype = "bool", shape = (1, 168))#candidate|2307|(1, 168)|var|bool
func_2306_call = mutated_mod.get_global_var('func_2306')
call_2308 = func_2306_call(var_2307)
output = call_2308
func_2309 = relay.Function([var_2307], output)
mutated_mod['func_2309'] = func_2309
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2321 = relay.const([[[3,-6,-9,10,-5,3,-7,7,-5,-8],[8,-4,-3,-1,-8,-6,-2,-9,5,9],[10,-7,9,4,-2,-3,-8,-9,7,-2],[8,-8,-10,-3,8,-6,6,-7,9,8],[-6,2,-1,4,10,3,-4,10,9,9]],[[-7,-6,-10,7,8,3,-8,5,5,-7],[5,-4,-2,5,10,-1,-2,-10,-1,4],[-4,-1,-1,4,-8,-2,1,-6,-2,8],[-4,9,-5,-10,7,8,-10,-6,7,-6],[10,-10,6,8,6,10,-5,7,9,8]],[[1,1,-5,10,-8,-9,-8,1,-6,4],[5,3,4,-9,7,-10,3,8,10,-10],[-8,-5,7,-10,5,4,-7,-1,8,5],[7,-4,9,-6,1,5,4,-8,8,-3],[-4,-4,-7,4,-4,1,-4,-4,6,-2]],[[-6,8,9,-3,6,1,-5,10,1,-7],[3,-8,10,10,2,7,-10,-1,3,-3],[8,-6,10,-6,10,-6,9,9,-6,7],[2,-9,9,9,-2,10,10,-4,1,-9],[-3,-5,-9,-2,-5,4,-5,10,-2,5]]], dtype = "uint32")#candidate|2321|(4, 5, 10)|const|uint32
const_2322 = relay.const([[[4,-5,-8,2,-2,-1,-8,8,5,8],[-8,1,5,-2,9,-1,1,5,-8,1],[9,8,7,3,-9,-9,7,6,-5,7],[6,-8,-1,-6,-10,-10,-9,8,4,9],[-2,10,-10,1,5,-9,7,5,10,8]],[[-8,-1,-9,-4,10,-6,-4,4,-3,7],[-5,8,-4,2,8,-4,-8,-5,3,10],[5,-10,4,-10,8,-6,6,7,-1,-1],[-8,-5,-9,-5,-10,-8,5,-3,-1,-8],[4,4,-2,-7,-9,-1,-5,-7,-7,-9]],[[-1,3,4,-5,-10,-3,-8,4,9,4],[10,-9,2,-3,8,7,10,5,7,-8],[4,-1,2,4,-7,-9,2,5,-4,2],[-10,-3,-8,-4,-8,-1,-6,5,-10,-9],[-7,-5,6,4,6,-4,-4,7,-5,6]],[[1,-8,-2,7,3,-8,-4,-3,10,-2],[5,5,5,3,10,5,-9,-2,-5,-10],[3,-1,10,9,1,-8,-9,8,-4,-6],[-2,-8,4,-1,-9,9,8,8,4,-8],[1,5,-1,-6,6,1,-4,1,1,9]]], dtype = "uint32")#candidate|2322|(4, 5, 10)|const|uint32
bop_2323 = relay.greater_equal(const_2321.astype('bool'), relay.reshape(const_2322.astype('bool'), relay.shape_of(const_2321))) # shape=(4, 5, 10)
uop_2326 = relay.cos(bop_2323.astype('float64')) # shape=(4, 5, 10)
output = uop_2326
output2 = uop_2326
func_2328 = relay.Function([], output)
mod['func_2328'] = func_2328
mod = relay.transform.InferType()(mod)
output = func_2328()
func_2329 = relay.Function([], output)
mutated_mod['func_2329'] = func_2329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2264_call = mod.get_global_var('func_2264')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_2359 = func_2264_call()
call_2360 = func_2264_call()
var_2367 = relay.var("var_2367", dtype = "bool", shape = (9, 4, 6))#candidate|2367|(9, 4, 6)|var|bool
bop_2368 = relay.multiply(call_2359.astype('uint16'), relay.reshape(var_2367.astype('uint16'), relay.shape_of(call_2359))) # shape=(9, 4, 6)
bop_2371 = relay.multiply(call_2360.astype('uint16'), relay.reshape(var_2367.astype('uint16'), relay.shape_of(call_2360))) # shape=(9, 4, 6)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_2373 = relay.TupleGetItem(func_1270_call(), 0)
call_2374 = relay.TupleGetItem(func_1272_call(), 0)
func_1805_call = mod.get_global_var('func_1805')
func_1807_call = mutated_mod.get_global_var('func_1807')
call_2382 = relay.TupleGetItem(func_1805_call(relay.reshape(call_2359.astype('bool'), [9, 4, 6])), 0)
call_2383 = relay.TupleGetItem(func_1807_call(relay.reshape(call_2359.astype('bool'), [9, 4, 6])), 0)
uop_2384 = relay.cos(call_2373.astype('float32')) # shape=(9, 4, 6)
uop_2386 = relay.cos(call_2374.astype('float32')) # shape=(9, 4, 6)
output = relay.Tuple([bop_2368,call_2382,uop_2384,])
output2 = relay.Tuple([bop_2371,call_2383,uop_2386,])
func_2392 = relay.Function([var_2367,], output)
mod['func_2392'] = func_2392
mod = relay.transform.InferType()(mod)
var_2393 = relay.var("var_2393", dtype = "bool", shape = (9, 4, 6))#candidate|2393|(9, 4, 6)|var|bool
output = func_2392(var_2393)
func_2394 = relay.Function([var_2393], output)
mutated_mod['func_2394'] = func_2394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
call_2409 = relay.TupleGetItem(func_980_call(), 1)
call_2410 = relay.TupleGetItem(func_982_call(), 1)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_2411 = relay.TupleGetItem(func_1270_call(), 0)
call_2412 = relay.TupleGetItem(func_1272_call(), 0)
func_1137_call = mod.get_global_var('func_1137')
func_1138_call = mutated_mod.get_global_var('func_1138')
call_2415 = relay.TupleGetItem(func_1137_call(), 1)
call_2416 = relay.TupleGetItem(func_1138_call(), 1)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_2423 = relay.TupleGetItem(func_2010_call(), 3)
call_2424 = relay.TupleGetItem(func_2011_call(), 3)
func_1210_call = mod.get_global_var('func_1210')
func_1214_call = mutated_mod.get_global_var('func_1214')
var_2426 = relay.var("var_2426", dtype = "float64", shape = (1080,))#candidate|2426|(1080,)|var|float64
call_2425 = relay.TupleGetItem(func_1210_call(relay.reshape(var_2426.astype('float64'), [9, 12, 10]), relay.reshape(var_2426.astype('float64'), [9, 12, 10]), ), 2)
call_2427 = relay.TupleGetItem(func_1214_call(relay.reshape(var_2426.astype('float64'), [9, 12, 10]), relay.reshape(var_2426.astype('float64'), [9, 12, 10]), ), 2)
output = relay.Tuple([call_2409,call_2411,call_2415,call_2423,call_2425,var_2426,])
output2 = relay.Tuple([call_2410,call_2412,call_2416,call_2424,call_2427,var_2426,])
func_2428 = relay.Function([var_2426,], output)
mod['func_2428'] = func_2428
mod = relay.transform.InferType()(mod)
var_2429 = relay.var("var_2429", dtype = "float64", shape = (1080,))#candidate|2429|(1080,)|var|float64
output = func_2428(var_2429)
func_2430 = relay.Function([var_2429], output)
mutated_mod['func_2430'] = func_2430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_2439 = relay.TupleGetItem(func_319_call(), 2)
call_2440 = relay.TupleGetItem(func_321_call(), 2)
output = call_2439
output2 = call_2440
func_2453 = relay.Function([], output)
mod['func_2453'] = func_2453
mod = relay.transform.InferType()(mod)
output = func_2453()
func_2454 = relay.Function([], output)
mutated_mod['func_2454'] = func_2454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
call_2476 = relay.TupleGetItem(func_980_call(), 1)
call_2477 = relay.TupleGetItem(func_982_call(), 1)
func_1774_call = mod.get_global_var('func_1774')
func_1776_call = mutated_mod.get_global_var('func_1776')
call_2480 = func_1774_call()
call_2481 = func_1774_call()
output = relay.Tuple([call_2476,call_2480,])
output2 = relay.Tuple([call_2477,call_2481,])
func_2485 = relay.Function([], output)
mod['func_2485'] = func_2485
mod = relay.transform.InferType()(mod)
mutated_mod['func_2485'] = func_2485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2485_call = mutated_mod.get_global_var('func_2485')
call_2486 = func_2485_call()
output = call_2486
func_2487 = relay.Function([], output)
mutated_mod['func_2487'] = func_2487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_2493 = relay.TupleGetItem(func_2173_call(), 2)
call_2494 = relay.TupleGetItem(func_2175_call(), 2)
func_1763_call = mod.get_global_var('func_1763')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_2509 = func_1763_call()
call_2510 = func_1763_call()
func_84_call = mod.get_global_var('func_84')
func_85_call = mutated_mod.get_global_var('func_85')
call_2515 = relay.TupleGetItem(func_84_call(), 0)
call_2516 = relay.TupleGetItem(func_85_call(), 0)
bop_2523 = relay.subtract(call_2515.astype('int8'), relay.reshape(call_2493.astype('int8'), relay.shape_of(call_2515))) # shape=(9, 4, 6)
bop_2526 = relay.subtract(call_2516.astype('int8'), relay.reshape(call_2494.astype('int8'), relay.shape_of(call_2516))) # shape=(9, 4, 6)
func_2211_call = mod.get_global_var('func_2211')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_2532 = func_2211_call()
call_2533 = func_2211_call()
output = relay.Tuple([call_2509,bop_2523,call_2532,])
output2 = relay.Tuple([call_2510,bop_2526,call_2533,])
func_2547 = relay.Function([], output)
mod['func_2547'] = func_2547
mod = relay.transform.InferType()(mod)
mutated_mod['func_2547'] = func_2547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2547_call = mutated_mod.get_global_var('func_2547')
call_2548 = func_2547_call()
output = call_2548
func_2549 = relay.Function([], output)
mutated_mod['func_2549'] = func_2549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_427_call = mod.get_global_var('func_427')
func_428_call = mutated_mod.get_global_var('func_428')
call_2550 = func_427_call()
call_2551 = func_427_call()
func_2306_call = mod.get_global_var('func_2306')
func_2309_call = mutated_mod.get_global_var('func_2309')
var_2555 = relay.var("var_2555", dtype = "bool", shape = (168,))#candidate|2555|(168,)|var|bool
call_2554 = relay.TupleGetItem(func_2306_call(relay.reshape(var_2555.astype('bool'), [1, 168])), 0)
call_2556 = relay.TupleGetItem(func_2309_call(relay.reshape(var_2555.astype('bool'), [1, 168])), 0)
output = relay.Tuple([call_2550,call_2554,var_2555,])
output2 = relay.Tuple([call_2551,call_2556,var_2555,])
func_2564 = relay.Function([var_2555,], output)
mod['func_2564'] = func_2564
mod = relay.transform.InferType()(mod)
var_2565 = relay.var("var_2565", dtype = "bool", shape = (168,))#candidate|2565|(168,)|var|bool
output = func_2564(var_2565)
func_2566 = relay.Function([var_2565], output)
mutated_mod['func_2566'] = func_2566
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2596 = relay.const([[[-7,-2,3,4,9,10,1],[-8,7,7,-2,1,-6,10],[-4,-3,-8,-5,-2,-8,-1]],[[7,-6,-8,-8,9,2,7],[-4,7,7,-10,-6,10,4],[-1,8,8,4,9,10,3]],[[9,-10,-8,-2,9,-2,6],[5,1,8,7,-3,1,4],[-9,3,-6,10,2,-10,5]],[[5,5,-3,9,4,-7,-6],[9,2,-8,4,10,9,8],[-2,-1,-4,1,3,-1,4]],[[5,10,4,10,9,-6,-7],[-2,4,8,2,-4,-1,3],[-5,2,10,2,4,-4,7]],[[3,-4,-1,-10,4,2,7],[4,-5,-6,8,9,-8,3],[7,1,-6,-4,3,-5,-7]],[[4,10,1,-8,-6,-5,-8],[7,6,-1,-3,-3,-3,2],[5,5,-1,-9,4,-3,6]],[[3,-2,5,-6,8,3,-10],[-10,-4,-10,-6,6,5,-5],[-10,6,-4,6,8,-6,-5]],[[8,7,6,4,-2,10,8],[-8,4,5,-3,-10,-8,3],[3,-5,3,-10,3,8,-4]],[[3,-4,6,-1,9,8,3],[6,-2,-5,-1,-6,1,6],[-5,8,4,-1,9,9,-3]],[[7,-5,-3,-3,3,-7,6],[-10,-9,-1,-5,10,-5,-5],[9,3,6,-9,6,-5,6]]], dtype = "uint64")#candidate|2596|(11, 3, 7)|const|uint64
var_2597 = relay.var("var_2597", dtype = "uint64", shape = (11, 3, 7))#candidate|2597|(11, 3, 7)|var|uint64
bop_2598 = relay.right_shift(const_2596.astype('uint64'), relay.reshape(var_2597.astype('uint64'), relay.shape_of(const_2596))) # shape=(11, 3, 7)
func_2453_call = mod.get_global_var('func_2453')
func_2454_call = mutated_mod.get_global_var('func_2454')
call_2602 = func_2453_call()
call_2603 = func_2453_call()
uop_2606 = relay.sqrt(bop_2598.astype('float64')) # shape=(11, 3, 7)
func_427_call = mod.get_global_var('func_427')
func_428_call = mutated_mod.get_global_var('func_428')
call_2610 = func_427_call()
call_2611 = func_427_call()
func_1388_call = mod.get_global_var('func_1388')
func_1389_call = mutated_mod.get_global_var('func_1389')
call_2613 = relay.TupleGetItem(func_1388_call(), 0)
call_2614 = relay.TupleGetItem(func_1389_call(), 0)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_2622 = relay.TupleGetItem(func_2173_call(), 0)
call_2623 = relay.TupleGetItem(func_2175_call(), 0)
func_723_call = mod.get_global_var('func_723')
func_724_call = mutated_mod.get_global_var('func_724')
call_2624 = relay.TupleGetItem(func_723_call(), 0)
call_2625 = relay.TupleGetItem(func_724_call(), 0)
output = relay.Tuple([call_2602,uop_2606,call_2610,call_2613,call_2622,call_2624,])
output2 = relay.Tuple([call_2603,uop_2606,call_2611,call_2614,call_2623,call_2625,])
func_2632 = relay.Function([var_2597,], output)
mod['func_2632'] = func_2632
mod = relay.transform.InferType()(mod)
mutated_mod['func_2632'] = func_2632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2633 = relay.var("var_2633", dtype = "uint64", shape = (11, 3, 7))#candidate|2633|(11, 3, 7)|var|uint64
func_2632_call = mutated_mod.get_global_var('func_2632')
call_2634 = func_2632_call(var_2633)
output = call_2634
func_2635 = relay.Function([var_2633], output)
mutated_mod['func_2635'] = func_2635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1774_call = mod.get_global_var('func_1774')
func_1776_call = mutated_mod.get_global_var('func_1776')
call_2663 = func_1774_call()
call_2664 = func_1774_call()
output = call_2663
output2 = call_2664
func_2668 = relay.Function([], output)
mod['func_2668'] = func_2668
mod = relay.transform.InferType()(mod)
output = func_2668()
func_2669 = relay.Function([], output)
mutated_mod['func_2669'] = func_2669
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2714 = relay.var("var_2714", dtype = "float32", shape = (13, 10, 11))#candidate|2714|(13, 10, 11)|var|float32
var_2715 = relay.var("var_2715", dtype = "float32", shape = (13, 10, 11))#candidate|2715|(13, 10, 11)|var|float32
bop_2716 = relay.floor_divide(var_2714.astype('float32'), relay.reshape(var_2715.astype('float32'), relay.shape_of(var_2714))) # shape=(13, 10, 11)
output = relay.Tuple([bop_2716,])
output2 = relay.Tuple([bop_2716,])
func_2748 = relay.Function([var_2714,var_2715,], output)
mod['func_2748'] = func_2748
mod = relay.transform.InferType()(mod)
mutated_mod['func_2748'] = func_2748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2748_call = mutated_mod.get_global_var('func_2748')
var_2750 = relay.var("var_2750", dtype = "float32", shape = (13, 10, 11))#candidate|2750|(13, 10, 11)|var|float32
var_2751 = relay.var("var_2751", dtype = "float32", shape = (13, 10, 11))#candidate|2751|(13, 10, 11)|var|float32
call_2749 = func_2748_call(var_2750,var_2751,)
output = call_2749
func_2752 = relay.Function([var_2750,var_2751,], output)
mutated_mod['func_2752'] = func_2752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_2800 = relay.TupleGetItem(func_272_call(), 1)
call_2801 = relay.TupleGetItem(func_274_call(), 1)
func_1743_call = mod.get_global_var('func_1743')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_2817 = relay.TupleGetItem(func_1743_call(), 1)
call_2818 = relay.TupleGetItem(func_1745_call(), 1)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
call_2838 = relay.TupleGetItem(func_980_call(), 2)
call_2839 = relay.TupleGetItem(func_982_call(), 2)
func_1960_call = mod.get_global_var('func_1960')
func_1962_call = mutated_mod.get_global_var('func_1962')
call_2844 = relay.TupleGetItem(func_1960_call(relay.reshape(call_2817.astype('float32'), [168, 1])), 1)
call_2845 = relay.TupleGetItem(func_1962_call(relay.reshape(call_2817.astype('float32'), [168, 1])), 1)
func_2485_call = mod.get_global_var('func_2485')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_2848 = relay.TupleGetItem(func_2485_call(), 1)
call_2849 = relay.TupleGetItem(func_2487_call(), 1)
output = relay.Tuple([call_2800,call_2817,call_2838,call_2844,call_2848,])
output2 = relay.Tuple([call_2801,call_2818,call_2839,call_2845,call_2849,])
func_2855 = relay.Function([], output)
mod['func_2855'] = func_2855
mod = relay.transform.InferType()(mod)
mutated_mod['func_2855'] = func_2855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2855_call = mutated_mod.get_global_var('func_2855')
call_2856 = func_2855_call()
output = call_2856
func_2857 = relay.Function([], output)
mutated_mod['func_2857'] = func_2857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1388_call = mod.get_global_var('func_1388')
func_1389_call = mutated_mod.get_global_var('func_1389')
call_2866 = relay.TupleGetItem(func_1388_call(), 0)
call_2867 = relay.TupleGetItem(func_1389_call(), 0)
output = call_2866
output2 = call_2867
func_2871 = relay.Function([], output)
mod['func_2871'] = func_2871
mod = relay.transform.InferType()(mod)
mutated_mod['func_2871'] = func_2871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2871_call = mutated_mod.get_global_var('func_2871')
call_2872 = func_2871_call()
output = call_2872
func_2873 = relay.Function([], output)
mutated_mod['func_2873'] = func_2873
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2893 = relay.var("var_2893", dtype = "int64", shape = ())#candidate|2893|()|var|int64
var_2894 = relay.var("var_2894", dtype = "int64", shape = (15, 8, 15))#candidate|2894|(15, 8, 15)|var|int64
bop_2895 = relay.bitwise_or(var_2893.astype('int64'), var_2894.astype('int64')) # shape=(15, 8, 15)
const_2900 = relay.const([[[-3,7,2,4,-6,6,-4,2,-7,-10,-9,-10,10,2,5],[7,4,-9,-9,10,5,-1,-7,2,-9,6,5,-3,-3,1],[2,-5,-4,-5,-5,-10,-10,-9,3,4,-8,-2,-6,8,-9],[-5,-8,9,5,5,-10,-2,8,-9,5,-3,-2,5,-9,5],[-1,8,3,1,5,7,5,-6,-3,3,8,2,-10,-8,-10],[-6,-5,10,4,-5,-9,6,4,-6,9,-4,5,7,-2,6],[-7,-3,-7,-2,6,1,2,1,9,4,7,5,3,-1,6],[-7,10,-7,4,-1,9,-8,-9,-8,6,-8,-9,7,4,8]],[[-3,-5,6,-1,1,1,-4,-2,5,5,3,4,-8,-7,9],[4,-10,-7,9,5,2,2,4,-10,6,-10,-9,-3,7,9],[5,10,-2,-2,-6,3,-4,3,10,6,-1,5,3,6,7],[-6,1,-10,2,4,-10,4,-1,-1,-2,-7,3,2,-1,6],[8,-2,5,-1,-1,-4,1,4,-7,-3,2,-4,3,1,-8],[1,8,-4,3,-1,-2,7,3,5,8,10,9,5,2,5],[-6,8,10,-8,-9,1,-1,5,2,5,2,-10,-1,-3,4],[5,-6,3,-6,1,7,7,2,4,-3,-4,6,6,-10,2]],[[-8,-3,9,10,-4,-1,5,-2,9,1,-7,-7,-10,10,-3],[-7,1,-7,5,-6,-10,-1,-6,-2,-9,8,-9,-10,-9,2],[-5,5,8,-6,1,1,2,8,4,-2,-4,-10,-5,-5,-1],[6,-5,-1,5,3,1,7,5,9,5,4,-2,-2,5,3],[4,3,2,-2,1,-3,9,-6,-5,-6,10,8,6,-1,9],[8,-5,3,-5,6,-10,8,9,6,3,-2,3,5,2,-2],[-9,-6,-1,4,4,2,7,3,-8,-7,2,5,1,-5,-5],[-6,9,-1,-1,-6,2,-8,2,4,10,-2,-3,8,-7,7]],[[-9,-8,-2,-9,-3,7,7,-4,-7,-8,2,-9,-6,-8,-9],[-5,-7,7,2,-2,2,-10,-5,7,-5,-8,6,-3,-4,5],[6,-2,-1,-2,-4,5,6,-7,2,-4,9,-5,9,7,-10],[7,-2,-1,-9,-5,-9,-10,-8,9,-9,8,-5,4,4,9],[6,2,-6,-1,5,-9,10,1,-4,-9,-3,4,-1,-4,-2],[9,-9,-7,3,2,-6,4,8,-6,-8,-9,2,-9,-4,8],[-5,5,7,3,-2,7,5,5,-7,-8,-6,5,2,2,8],[1,6,-1,10,4,8,9,5,7,-5,-6,-3,10,7,-3]],[[-10,10,2,1,-5,3,8,-5,6,-4,8,-3,-3,8,2],[8,-6,10,-10,-10,-7,8,-7,-6,-6,5,2,-7,-10,6],[-6,8,3,-2,10,-9,6,-2,-4,-5,1,-6,-1,-8,10],[5,-6,-8,10,3,-1,-6,-4,10,-9,8,-9,2,9,-1],[2,5,-10,1,2,-9,-8,1,-7,10,6,-5,2,4,-7],[-10,-2,9,7,-1,5,3,-9,5,-5,-2,-1,-7,4,6],[-8,-10,-9,-4,10,5,-7,9,3,2,9,9,10,-4,-7],[6,7,8,7,-2,5,-2,-8,-10,7,8,-5,7,-5,10]],[[1,7,-3,4,7,9,-5,-6,-6,-3,8,8,-10,-1,-5],[-7,8,-6,1,3,8,-9,6,6,-4,4,10,-7,8,5],[10,2,6,-1,10,4,-7,-10,10,7,-5,-6,-5,-7,-1],[-6,4,9,8,8,3,7,-7,-4,-3,9,-2,-4,7,9],[4,9,3,-10,7,10,-2,-9,-6,-3,4,8,6,2,-5],[-1,6,9,-7,10,-6,3,9,-6,5,-5,-3,4,9,5],[6,-3,6,-2,10,9,4,6,2,-10,5,-5,-10,-10,-4],[3,10,4,7,-1,10,4,1,-7,6,-1,3,-9,-4,4]],[[-3,2,2,-1,4,7,-1,-7,-3,-7,-4,-1,-4,-1,-9],[-6,9,-8,-4,1,1,1,9,6,2,2,-10,2,3,-2],[-8,7,-6,10,3,7,9,8,6,1,-5,-4,6,-9,-1],[5,9,9,-8,7,-2,7,-2,9,-7,6,3,-9,7,-10],[-10,10,-9,-7,9,10,10,-3,2,-10,2,3,9,-4,3],[-9,-1,4,-9,6,-7,-1,4,9,6,7,9,-3,3,7],[3,10,-4,-5,7,2,10,3,7,-9,3,-1,7,5,1],[-7,9,-10,2,-7,-9,-3,10,2,-7,-10,-7,7,5,6]],[[-5,10,-10,6,-10,-9,9,9,-9,9,-3,8,-2,-6,6],[-2,-4,-4,7,-4,-2,7,8,-3,8,-3,-4,1,-8,4],[-6,7,-1,2,-1,-6,-1,6,-10,6,-2,-8,-2,4,-3],[-5,3,9,-3,3,-1,-6,-3,-4,1,10,1,-2,7,2],[-2,-1,9,10,-4,5,-3,8,3,-8,1,10,8,-4,5],[4,-5,4,-6,-5,9,-4,10,8,-3,10,8,8,9,10],[-2,-3,9,10,-2,-6,4,3,1,9,-2,1,-6,-4,3],[-3,8,9,-3,-5,-3,-8,-10,-2,6,8,-10,-6,8,-3]],[[5,5,4,-3,2,-4,8,3,-6,-10,4,-10,6,3,7],[-4,-4,8,-4,4,8,2,-3,3,-8,4,2,10,-2,-4],[9,-3,-7,-10,1,-7,-4,-2,-4,8,9,-7,6,9,-8],[-8,10,-1,-2,10,-7,-10,-7,-9,9,-4,1,-7,9,-6],[-10,-4,-6,9,-6,-1,7,-3,6,-7,1,-3,-3,9,8],[-8,10,9,9,-3,-9,7,8,2,3,-10,1,5,4,7],[-9,-10,-7,4,9,10,-4,5,6,-7,-9,3,8,5,4],[-4,8,-2,5,2,3,-3,8,10,-5,5,4,5,8,4]],[[3,4,3,8,-4,-1,10,-6,2,-4,-3,-3,9,-8,10],[-8,3,-4,-10,4,1,-2,9,-3,6,-8,-8,-5,-8,3],[-9,1,-3,-8,-7,10,8,-3,2,8,3,6,-6,6,3],[4,-10,-4,1,-9,-2,10,-1,-7,-9,2,10,1,8,-1],[-9,-5,-1,-6,-8,-3,-2,-2,-6,-7,-3,-6,6,10,9],[6,-8,8,9,6,-9,-10,3,-5,5,5,2,1,-1,3],[-4,-7,-10,-6,9,8,2,-8,-2,-4,-6,4,-10,-7,8],[8,-8,8,10,-7,-5,-6,3,-10,8,3,-4,-1,4,5]],[[5,-5,10,3,5,-10,4,-7,-1,-5,2,-2,-5,-3,8],[-10,-3,8,-8,5,10,6,-5,-3,2,5,4,-2,-10,-7],[-3,1,-1,9,-9,-5,-4,-1,5,-5,-1,-1,-10,5,8],[-8,8,6,10,9,2,8,-6,-4,4,8,-2,2,3,-1],[7,3,3,-5,5,-4,-9,-4,1,5,-9,-1,-5,-2,8],[1,-5,3,2,-2,-3,7,-9,8,-10,5,10,-10,-7,-3],[-6,-4,-7,-10,6,-7,10,-2,4,7,7,-5,8,-9,-8],[1,5,6,4,-10,-9,1,10,6,-7,9,-7,-8,10,9]],[[2,-3,-7,8,6,-6,-8,4,-2,3,5,3,8,4,-3],[-7,3,1,-8,5,-8,9,-8,3,3,-9,-9,10,-6,-7],[-7,3,6,-2,-2,8,-6,7,10,-3,-7,1,7,-7,-6],[-1,1,-3,-7,-1,3,-8,-8,4,6,-3,10,-2,7,-1],[4,-8,-7,1,-7,2,4,1,-6,2,-10,6,10,10,-5],[-2,4,-3,-10,-4,5,-9,5,-10,2,-2,6,-6,-6,-4],[7,2,-4,2,-7,3,10,2,-1,-6,-6,-7,8,9,-10],[-7,-8,8,-3,-8,-7,-6,-2,-4,-3,-5,-1,-9,8,7]],[[10,-6,-4,-10,7,7,8,2,-2,-2,7,3,-2,10,-2],[-7,-10,1,-7,1,9,-7,3,-9,-6,-1,-2,4,9,-5],[1,-7,5,7,1,8,-7,-8,-6,7,-10,8,5,6,-6],[-8,3,1,3,3,-7,-3,10,5,8,10,2,-10,10,2],[-8,-4,-4,-10,5,9,6,6,-3,2,3,-1,-9,-2,8],[-4,2,9,5,3,5,-1,3,-5,-8,-10,-10,-6,2,6],[9,6,10,-7,5,6,-1,-10,-4,-3,-3,-3,-1,-10,4],[3,-9,-7,4,-3,-6,-10,-8,3,5,-4,6,1,-6,-2]],[[-10,6,-4,8,8,9,-2,1,9,-2,10,5,3,5,1],[-10,2,10,-10,4,-2,2,-3,-4,8,9,1,-6,-1,4],[8,-5,-3,-6,5,-2,4,1,-8,-10,-10,-4,2,-7,-1],[-7,6,-1,8,1,7,10,-9,9,-7,-6,7,-2,-2,-1],[10,3,-9,5,2,-1,-1,-2,-6,-10,1,4,7,-6,2],[1,-5,-10,-9,-4,-10,9,7,-4,4,8,1,3,5,-7],[7,3,-4,-8,5,-3,-6,10,4,8,9,5,-7,8,-8],[-1,6,-10,-4,-3,-10,-7,9,-4,3,-2,8,-2,8,7]],[[8,-2,1,-5,10,-7,4,-9,-3,-7,4,9,-9,-7,1],[-2,3,3,7,10,-8,8,-10,5,1,-10,-5,7,7,10],[9,9,7,-7,-2,2,5,-1,8,-8,10,-3,6,1,-5],[3,5,7,6,8,2,-7,1,-2,6,7,-10,2,-2,9],[-4,-3,-6,10,-6,-9,8,7,-6,8,9,-9,-8,4,4],[7,-6,4,3,-4,-4,-1,-1,-2,5,10,-9,-4,-9,-7],[2,8,8,-9,-8,2,-8,-4,1,-9,-8,-2,-7,4,-7],[-7,-8,-6,-9,-7,-10,8,-4,-8,-8,1,5,5,-2,-5]]], dtype = "int64")#candidate|2900|(15, 8, 15)|const|int64
bop_2901 = relay.greater(bop_2895.astype('bool'), relay.reshape(const_2900.astype('bool'), relay.shape_of(bop_2895))) # shape=(15, 8, 15)
output = relay.Tuple([bop_2901,])
output2 = relay.Tuple([bop_2901,])
func_2916 = relay.Function([var_2893,var_2894,], output)
mod['func_2916'] = func_2916
mod = relay.transform.InferType()(mod)
var_2917 = relay.var("var_2917", dtype = "int64", shape = ())#candidate|2917|()|var|int64
var_2918 = relay.var("var_2918", dtype = "int64", shape = (15, 8, 15))#candidate|2918|(15, 8, 15)|var|int64
output = func_2916(var_2917,var_2918,)
func_2919 = relay.Function([var_2917,var_2918,], output)
mutated_mod['func_2919'] = func_2919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_84_call = mod.get_global_var('func_84')
func_85_call = mutated_mod.get_global_var('func_85')
call_3004 = relay.TupleGetItem(func_84_call(), 1)
call_3005 = relay.TupleGetItem(func_85_call(), 1)
func_1230_call = mod.get_global_var('func_1230')
func_1232_call = mutated_mod.get_global_var('func_1232')
call_3028 = func_1230_call()
call_3029 = func_1230_call()
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_3037 = relay.TupleGetItem(func_319_call(), 2)
call_3038 = relay.TupleGetItem(func_321_call(), 2)
output = relay.Tuple([call_3004,call_3028,call_3037,])
output2 = relay.Tuple([call_3005,call_3029,call_3038,])
func_3050 = relay.Function([], output)
mod['func_3050'] = func_3050
mod = relay.transform.InferType()(mod)
output = func_3050()
func_3051 = relay.Function([], output)
mutated_mod['func_3051'] = func_3051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2547_call = mod.get_global_var('func_2547')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_3073 = relay.TupleGetItem(func_2547_call(), 0)
call_3074 = relay.TupleGetItem(func_2549_call(), 0)
func_1908_call = mod.get_global_var('func_1908')
func_1911_call = mutated_mod.get_global_var('func_1911')
call_3080 = relay.TupleGetItem(func_1908_call(relay.reshape(call_3073.astype('float64'), [9, 4, 6])), 0)
call_3081 = relay.TupleGetItem(func_1911_call(relay.reshape(call_3073.astype('float64'), [9, 4, 6])), 0)
output = relay.Tuple([call_3073,call_3080,])
output2 = relay.Tuple([call_3074,call_3081,])
func_3089 = relay.Function([], output)
mod['func_3089'] = func_3089
mod = relay.transform.InferType()(mod)
output = func_3089()
func_3090 = relay.Function([], output)
mutated_mod['func_3090'] = func_3090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3115 = relay.var("var_3115", dtype = "float64", shape = (3, 6, 16))#candidate|3115|(3, 6, 16)|var|float64
uop_3116 = relay.asin(var_3115.astype('float64')) # shape=(3, 6, 16)
func_2094_call = mod.get_global_var('func_2094')
func_2096_call = mutated_mod.get_global_var('func_2096')
call_3119 = relay.TupleGetItem(func_2094_call(), 0)
call_3120 = relay.TupleGetItem(func_2096_call(), 0)
bop_3121 = relay.equal(uop_3116.astype('bool'), relay.reshape(var_3115.astype('bool'), relay.shape_of(uop_3116))) # shape=(3, 6, 16)
output = relay.Tuple([call_3119,bop_3121,])
output2 = relay.Tuple([call_3120,bop_3121,])
func_3124 = relay.Function([var_3115,], output)
mod['func_3124'] = func_3124
mod = relay.transform.InferType()(mod)
mutated_mod['func_3124'] = func_3124
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3125 = relay.var("var_3125", dtype = "float64", shape = (3, 6, 16))#candidate|3125|(3, 6, 16)|var|float64
func_3124_call = mutated_mod.get_global_var('func_3124')
call_3126 = func_3124_call(var_3125)
output = call_3126
func_3127 = relay.Function([var_3125], output)
mutated_mod['func_3127'] = func_3127
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3164 = relay.var("var_3164", dtype = "float64", shape = (13, 4, 15))#candidate|3164|(13, 4, 15)|var|float64
uop_3165 = relay.cosh(var_3164.astype('float64')) # shape=(13, 4, 15)
output = relay.Tuple([uop_3165,])
output2 = relay.Tuple([uop_3165,])
func_3168 = relay.Function([var_3164,], output)
mod['func_3168'] = func_3168
mod = relay.transform.InferType()(mod)
mutated_mod['func_3168'] = func_3168
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3169 = relay.var("var_3169", dtype = "float64", shape = (13, 4, 15))#candidate|3169|(13, 4, 15)|var|float64
func_3168_call = mutated_mod.get_global_var('func_3168')
call_3170 = func_3168_call(var_3169)
output = call_3170
func_3171 = relay.Function([var_3169], output)
mutated_mod['func_3171'] = func_3171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_3193 = relay.TupleGetItem(func_2173_call(), 0)
call_3194 = relay.TupleGetItem(func_2175_call(), 0)
output = call_3193
output2 = call_3194
func_3198 = relay.Function([], output)
mod['func_3198'] = func_3198
mod = relay.transform.InferType()(mod)
output = func_3198()
func_3199 = relay.Function([], output)
mutated_mod['func_3199'] = func_3199
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3212 = relay.var("var_3212", dtype = "float32", shape = (8, 7, 1))#candidate|3212|(8, 7, 1)|var|float32
uop_3213 = relay.asinh(var_3212.astype('float32')) # shape=(8, 7, 1)
uop_3221 = relay.cosh(var_3212.astype('float32')) # shape=(8, 7, 1)
var_3232 = relay.var("var_3232", dtype = "float32", shape = (8, 7, 5))#candidate|3232|(8, 7, 5)|var|float32
bop_3233 = relay.logical_and(uop_3221.astype('bool'), var_3232.astype('bool')) # shape=(8, 7, 5)
func_1626_call = mod.get_global_var('func_1626')
func_1628_call = mutated_mod.get_global_var('func_1628')
var_3237 = relay.var("var_3237", dtype = "bool", shape = (216,))#candidate|3237|(216,)|var|bool
call_3236 = relay.TupleGetItem(func_1626_call(relay.reshape(var_3237.astype('bool'), [216,])), 2)
call_3238 = relay.TupleGetItem(func_1628_call(relay.reshape(var_3237.astype('bool'), [216,])), 2)
func_1743_call = mod.get_global_var('func_1743')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_3239 = relay.TupleGetItem(func_1743_call(), 0)
call_3240 = relay.TupleGetItem(func_1745_call(), 0)
bop_3241 = relay.greater(uop_3213.astype('bool'), var_3232.astype('bool')) # shape=(8, 7, 5)
func_2453_call = mod.get_global_var('func_2453')
func_2454_call = mutated_mod.get_global_var('func_2454')
call_3255 = func_2453_call()
call_3256 = func_2453_call()
bop_3260 = relay.multiply(bop_3241.astype('uint32'), uop_3221.astype('uint32')) # shape=(8, 7, 5)
output = relay.Tuple([bop_3233,call_3236,var_3237,call_3239,call_3255,bop_3260,])
output2 = relay.Tuple([bop_3233,call_3238,var_3237,call_3240,call_3256,bop_3260,])
func_3268 = relay.Function([var_3212,var_3232,var_3237,], output)
mod['func_3268'] = func_3268
mod = relay.transform.InferType()(mod)
mutated_mod['func_3268'] = func_3268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3268_call = mutated_mod.get_global_var('func_3268')
var_3270 = relay.var("var_3270", dtype = "float32", shape = (8, 7, 1))#candidate|3270|(8, 7, 1)|var|float32
var_3271 = relay.var("var_3271", dtype = "float32", shape = (8, 7, 5))#candidate|3271|(8, 7, 5)|var|float32
var_3272 = relay.var("var_3272", dtype = "bool", shape = (216,))#candidate|3272|(216,)|var|bool
call_3269 = func_3268_call(var_3270,var_3271,var_3272,)
output = call_3269
func_3273 = relay.Function([var_3270,var_3271,var_3272,], output)
mutated_mod['func_3273'] = func_3273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2668_call = mod.get_global_var('func_2668')
func_2669_call = mutated_mod.get_global_var('func_2669')
call_3275 = func_2668_call()
call_3276 = func_2668_call()
output = call_3275
output2 = call_3276
func_3304 = relay.Function([], output)
mod['func_3304'] = func_3304
mod = relay.transform.InferType()(mod)
output = func_3304()
func_3305 = relay.Function([], output)
mutated_mod['func_3305'] = func_3305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_3326 = relay.TupleGetItem(func_603_call(), 0)
call_3327 = relay.TupleGetItem(func_605_call(), 0)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_3330 = func_39_call()
call_3331 = func_39_call()
uop_3335 = relay.asinh(call_3330.astype('float32')) # shape=(9, 4, 6)
uop_3337 = relay.asinh(call_3331.astype('float32')) # shape=(9, 4, 6)
output = relay.Tuple([call_3326,uop_3335,])
output2 = relay.Tuple([call_3327,uop_3337,])
func_3343 = relay.Function([], output)
mod['func_3343'] = func_3343
mod = relay.transform.InferType()(mod)
output = func_3343()
func_3344 = relay.Function([], output)
mutated_mod['func_3344'] = func_3344
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3350 = relay.var("var_3350", dtype = "uint16", shape = (15, 2, 6))#candidate|3350|(15, 2, 6)|var|uint16
var_3351 = relay.var("var_3351", dtype = "uint16", shape = (15, 2, 6))#candidate|3351|(15, 2, 6)|var|uint16
bop_3352 = relay.bitwise_and(var_3350.astype('uint16'), relay.reshape(var_3351.astype('uint16'), relay.shape_of(var_3350))) # shape=(15, 2, 6)
bop_3356 = relay.right_shift(var_3350.astype('int64'), relay.reshape(bop_3352.astype('int64'), relay.shape_of(var_3350))) # shape=(15, 2, 6)
func_1435_call = mod.get_global_var('func_1435')
func_1437_call = mutated_mod.get_global_var('func_1437')
const_3361 = relay.const([-7.128037,-1.012031,9.185251,9.500813,7.551865,-5.159715,-1.823510,-0.334502,-0.054812,9.880033,7.555793,6.843148,-9.860663,5.703791,7.910273,3.580821,3.574021,5.843002,-4.008063,-4.253074,-5.119625,-9.503377,2.881438,-5.902023,-1.817623,-5.355196,-0.666113,-6.329838,-7.572566,-3.789762,2.089463,7.889213,7.090351,0.659973,-2.901174,3.302617,-1.236655,6.074253,-6.283121,5.314894,-7.161803,1.824885,9.808858,5.004148,0.469084,-4.516996,0.717692,-0.026547,-5.481670,-5.216807,1.080525,-4.870464,-1.678383,1.922934,7.728046,6.332342,-7.658692,-0.237423,-6.494455,4.770702,4.483092,-2.384535,-2.383295,0.804027,6.390393,2.913634,8.063699,-7.664260,2.433803,-0.439666,3.803808,-0.847123,-9.882949,9.703268,2.132781,0.173810,-6.576314,8.820719,-8.692453,-2.206118,9.356507,-0.357444,7.524351,-7.907348,1.149240,0.173604,-5.132669,-3.084746,-1.197423,7.796477,3.756353,-7.934979,-8.564983,-2.117096,-5.080475,-5.317753,-5.405952,-5.355560,-7.222837,-3.974165,6.402467,-0.727571,-9.379999,0.588011,-0.693465,-2.749865,2.187122,-9.351319,-4.446166,-4.297494,7.823566,-6.463632,7.887610,6.893421,8.237406,9.177820,8.504428,-7.850184,4.894297,-2.134437,-5.808518,1.497954,7.804485,-6.528265,-8.295282,-4.827991,7.834600,7.613662,8.899934,-6.824240,-3.712390,1.179638,2.273019,7.713552,3.763922,5.907704,-9.653088,9.260555,-9.894112,-3.923831,-9.816145,-7.473815,1.027222,8.540136,-5.116793,-8.859161,4.653921,-3.366963,0.731256,1.697040,1.236594,5.495110,8.264377,9.619973,-2.896509,-4.909075,-7.376102,-1.393550,-0.955788,-6.085950,-5.757848,-2.911585,-5.889533,-1.654715,-4.165417,6.261487,-1.780851,-1.045569,9.722901,6.676406,2.098485,6.940537,-9.721033,0.684306,2.362611,8.997474,-1.023057,1.919436,-0.338846,9.097665,-1.699965,-0.057675,6.188273,-1.073467,-8.417730,-7.015719,-7.130547,2.991800,4.460954,5.939186,-0.003171,-8.721473,-1.028390,-3.341509,-7.983588,-2.042597,-0.628266,2.191746,3.222948,-8.598541,-3.484699,4.801438,-2.323661,0.533167,8.057454,-6.583820,-6.074113,4.099808,7.082276,5.930767,1.283708,-5.501289,6.312511,2.517619,3.863419,-8.320765,-8.492399,-3.335515,8.699989,-4.430037,5.436216,-0.529889,-1.629769,-1.679038,0.616090,7.399490,7.640889,-4.825164,1.959687,3.813427,-6.635181,-1.515535,0.689927,4.953958,0.079625,-1.860916,1.833393,-6.645187,-0.675768,8.391285,-9.808671,-8.322503,-0.420922,-8.903398,-3.595250,-3.630041,-2.313731,4.352575,-9.058467,-2.514048,-6.879349,-1.583290,7.495361,0.499976,1.013750,-1.542553,0.924589,-4.770133,7.797767,-6.739335,-8.096892,-0.190080,4.857511,3.904514,9.166247,5.674873,-5.264076,8.634983,-4.252764,1.987838,0.951180,-1.768033,-1.119567,-7.467445,6.451530,3.950838,1.153732,-2.988580,9.538329,-1.725934,9.288923,-2.616474,7.930608,-7.159609,8.438153,-3.097951,4.971090,9.754945,5.745491,1.357200,-6.048301,-1.190934,8.360127,2.908797,-5.968860,8.938195,1.452776,9.851668,6.289894,7.524575,6.182275,9.701633,-5.167764,-1.021975,-2.949131,-0.371336,-7.211646,-8.648000,-8.468974,-3.240196,-2.427910,-7.977163,-0.472505,-2.505497,5.436892,-3.981349,7.023437,8.137896,-8.272977,2.299533,-9.699952,-7.524152,9.006838,-5.454642,-1.878288,-1.168615,-8.421812,-5.984323,8.074169,-8.942581,-6.784754,1.825182,-9.856112,5.807017,5.375132,6.617479,2.962433,-1.262124,-3.374669,-7.577889,-2.874069,2.021624,2.296966,7.801174,8.439504,-6.033822,-3.054023,2.098437,-5.976634,9.302363,-8.493814,0.557230,-6.358671,-0.687178,-6.612211,2.429299,2.958243,1.748340,3.192470,5.228666,-0.642879,-9.303243,-2.244522,3.777534,3.297407,-8.081419,4.054865,7.729379,7.115620,6.453118,-1.491358,-2.627462,1.472867,-3.060366,-0.389134,8.304026,1.078263,2.716201,-5.142289,5.748573,-8.198022,3.171513,0.721328,6.912531,-5.291872,9.128144,-2.715595,-1.958318,9.902800,-6.393942,0.326829,0.640099,4.882719,-8.175693,6.662761,1.087596,7.015805,-7.032258,6.881481,3.001944,-5.393417,-0.618344,8.053097,-3.796289,-5.077004,-0.725139,8.436123,-3.377778,7.059188,-6.287847,-5.904028,-2.396294,-0.811833,4.359550,-3.929605,1.246876,3.064443,6.200516,-0.081438,3.533370,-5.055408,-9.134712,7.924704,3.543750,2.599256,-1.069231,0.885814,9.750231,9.367851,-2.517058,-1.332072,-1.851524,0.457075,-3.580238,3.075403,-1.030273,3.451294,2.064221,-1.883909,6.317794,-7.595010,3.631767,-6.277524,0.266889,1.193360,-7.059953,2.689702,2.113831,-8.137309,6.793934,-1.907666,-1.212866,-8.173345,-0.254938,-8.128885,5.180834,8.579515,-5.334620,2.793667,4.313146,0.146626,-0.308527,-8.543892,-1.768483,4.964254,6.858453,0.378464,-8.160378,2.736165,-8.787003,-8.802410,1.543959,9.215237,-4.777259,4.906925,4.602266,8.449558,-9.128568,-8.215125,-3.227611,-9.564489,8.753506,2.310976,7.873887,-7.570618,-2.556164,5.053493,7.786530,-3.573477,-7.511323,6.323507,-4.800805,4.073642,1.879731,0.073982,-4.263767,6.187726,-7.719313,1.451587,2.101277,9.684411,-4.333923,9.134303,9.182449,6.910995,-7.169084,-0.222712,3.375525,5.207308,4.383045,1.623341,-9.090344,0.439290,0.196574,-1.947460,-7.943054,4.841020,0.030188,-2.735967,-6.019304,-5.369665,8.769169,7.809708,-4.881055,1.811736,-9.359670,0.376789,8.470779,9.580797,0.250551,0.328202,8.036466,2.591876,-1.214284,-6.500340,0.885187,2.734724,6.904296,-5.729597,9.649984,1.345293,-1.888059,-7.024856,8.551438,-9.160852,5.683523,-5.575727,-6.587332,3.359662,-1.443325,1.580881,-0.080122,-1.176302,-5.387325,-1.992681,-4.964283,5.013383,-9.416493,-0.111824,2.295113,8.858663,-2.638485,8.569977,8.589799,3.411210,-9.408567,6.031511,0.448413,-8.908896,-1.788768,4.783355,-7.753625,9.437044,-1.298930,-8.008020,2.867571,6.255165,-8.906246,-8.740067,6.035502,0.754774,6.208933,7.571536,-1.910088,-7.070849,-2.317947,6.362607,-8.259945,3.232438,-6.108205,-7.314284,4.780554,9.894100,-9.230317,1.187993,-9.900888,-8.501775,-2.433716,-3.366650,2.494526,1.233366,1.772933,9.736534,-5.978626,-9.254018,-8.117639,-0.133558,-5.576867,5.959112,1.538797,2.945941,7.450239,0.329805,4.524313,-5.555530,-4.970204,-7.290086,-4.006832,3.688431,-1.789733,5.380222,-6.172936,7.272414,-8.770124,-1.337850,5.872381,9.923775,4.876159,-8.374523,-5.270511,6.060285,8.692848,-9.919885,9.916738,-4.929539,-0.373078,7.810278,7.806937,6.183596,6.046069,3.514346,1.245561,-4.130148,-0.063919,5.896420,0.478987,3.477451,-7.579714,2.075302,-8.140126,-8.728336,3.869433,1.286165,-5.279430,-8.953101,-2.624179,-0.670935,-3.562192,-3.186951,-8.303448,-8.855041,6.650533,-0.596813,7.745442,6.926905,2.373250,-4.599009,7.824680,8.212044,5.588185,-5.799067,8.597473,5.720876,0.735689,-4.674910,-2.674997,5.606681,3.611675,8.805868,3.942792,-3.305310,-0.194798,-4.674567,-7.821095,6.316554,0.476581,-9.789489,0.855082,3.370614,3.594743,-3.480022,-8.918134,5.153805,0.465046,-6.290866,-1.690459,8.102202,-3.247032,-2.508379,5.437961,-1.175338,8.271041,5.113883,-5.649058,6.114124,6.218445,6.432810,-0.057531,8.835050,-2.286265,-0.656682,-6.320249,1.046449,0.021185,7.690292,-9.684563,-8.158207,-9.474578,-2.959134,-0.771418,0.371624,5.881474,4.735998,7.559160,4.638377,-6.195122,-8.971144,5.768280,4.300696,-4.465302,4.068420,-1.935971,-0.133302,2.045560,-3.090473,1.280427,3.794335,-3.364237,-0.813168,3.184167,2.092987,2.022293,-9.535350,-7.404069,-7.883367,9.403500,5.662156,5.410793,-3.945586,-3.965479,-8.730005,-8.864470,-2.532999,-7.396948,7.437902,-3.302615,4.966128,-6.345848,-3.276329,-2.055713,1.748260,-8.524104,4.214280,1.194572,-4.404249,-0.033681,2.578604,3.130034,-2.898157,-3.002213,0.408933,-5.516625,-2.534665,0.175799,0.429215,0.318276,7.088633,4.241732,8.237966,-8.719998,-5.090702,-2.094482,-5.297061,0.106196,7.282232,-8.637257,-4.405732,-0.553621,9.507385,0.304224,0.617612,-1.924508,-8.284033,6.214577,-8.890894,-7.644957,5.610012,-8.159880,-9.772439,-9.455769,4.731541,-9.105355,0.864024,-2.472140,-9.808830,-1.861265,7.224670,-1.695159,-2.744273,4.256529,-1.199053,-5.129611,7.332797,0.702081,-2.671460,0.881676,-4.064562,-8.581284,-7.378851,-0.482192,-6.269622,-1.438409,3.122000,-3.974313,3.602978,-7.371436,9.008597,5.779066,3.023161,-6.059065,-9.799912,9.160908,9.338028,-0.194014,8.515176,3.901887,0.521240,8.547195,-1.188689,2.020265,5.827398,1.774375,-9.834208,2.231521,5.522285,4.241231,-7.487339,-4.550824,-3.386759,8.879820,-4.728646,-5.701271,2.611247,-6.247883,0.423753,0.113523,-9.355391,9.397826,9.634428,-8.623947,-1.899136,-3.221137,5.724712,-5.382476,2.863310,2.896904,-8.576251,-0.038102,3.218729,-1.507291,-2.819761,0.585268,-2.634991,1.599549,-7.960176,5.721189,1.565494,8.571520,-8.493303,6.124266,3.490306,9.734774,-0.586050,1.997742,5.384136,-7.435845,9.107071,-2.376027,-7.180745,7.327004,7.706093,9.948759,-0.317795,7.210534,-0.891180,6.345966,3.446957,-9.094740,-4.963395,2.801456,8.842215,4.397812,-8.906074,-3.345259,8.970371,6.300030,-5.324945,6.500721,6.140757,-1.632223,9.012953,7.029402,-8.361515,-6.213087,-7.977809,-8.275066,2.911601,-8.517587,5.864670,-0.618921,2.169461,-9.950595,-6.081929,-4.762541,-2.474634,-6.524459,-9.156167,1.881916,4.594514,9.097459,3.598812,6.978905,7.006309,-8.510858,-7.471624,6.763768,-5.236449,-5.208515,-5.176324,-8.620365,4.165442,-6.933880,7.106781,-0.192160,-5.010816,-2.926752,-7.151092,-1.753129,2.049047,-1.296925,-2.305413,3.313480,9.618113,6.799182,4.536698,2.014619,-7.846809,-2.580040,2.219422,-3.019057,4.523169,4.907575,-1.119466,4.703191,4.930761,-2.440108,-9.612475,-4.093344,4.191332,6.667858,-5.194152,6.871570,-8.805391,-9.887642,-6.983115,7.570015,1.761767,5.272961,0.373807,6.226405,4.603322,-4.301855,-0.586218,2.556102,-9.413578,-7.452452,5.327750,-1.488803,0.969758,3.025180,7.599621,5.652721,-3.454461,4.517049,-8.937811,-1.439717,-5.733885,2.680283,1.012522,-0.427125,9.058893,-2.515031,-9.665918,-9.523728,2.225453,8.333485,9.637280,0.635223,-4.925849,1.325136,-2.573686,-1.902858,-3.961244,6.287810,-8.630838,7.287615,-2.750223,0.449579,-5.535531,-1.271567,1.979286,8.736582,6.456041,-0.941377,6.910397,-4.910570,9.901146,-4.213515,-9.610302,-6.063758,4.105849,-9.267440,1.100861,-4.468532,0.759288,-0.655619,-3.486813,6.047840,-6.335087,5.092419,2.244163,0.448140,-3.672441,-0.268358,2.338273,-1.615273,3.794302,-2.347638,-8.357191,-3.387415,-9.329271,-1.723515,-6.635299,-1.843438,-8.166233,-6.534652,0.640859,-9.572571,6.061766,-7.231209,1.052900,3.401376,3.335931,-4.690751,-2.771502,8.827616,8.801946,-7.199607,-7.441224,-6.136064,-3.451746,-4.433433,3.749105,-1.510087,-8.621570,0.883663,7.934232,-1.407122,1.696092,-2.193531], dtype = "float64")#candidate|3361|(1080,)|const|float64
call_3360 = relay.TupleGetItem(func_1435_call(relay.reshape(const_3361.astype('float64'), [1080,])), 1)
call_3362 = relay.TupleGetItem(func_1437_call(relay.reshape(const_3361.astype('float64'), [1080,])), 1)
bop_3382 = relay.equal(bop_3352.astype('bool'), relay.reshape(var_3350.astype('bool'), relay.shape_of(bop_3352))) # shape=(15, 2, 6)
func_1210_call = mod.get_global_var('func_1210')
func_1214_call = mutated_mod.get_global_var('func_1214')
call_3385 = relay.TupleGetItem(func_1210_call(relay.reshape(const_3361.astype('float64'), [9, 12, 10]), relay.reshape(const_3361.astype('float64'), [9, 12, 10]), ), 3)
call_3386 = relay.TupleGetItem(func_1214_call(relay.reshape(const_3361.astype('float64'), [9, 12, 10]), relay.reshape(const_3361.astype('float64'), [9, 12, 10]), ), 3)
output = relay.Tuple([bop_3356,call_3360,const_3361,bop_3382,call_3385,])
output2 = relay.Tuple([bop_3356,call_3362,const_3361,bop_3382,call_3386,])
func_3387 = relay.Function([var_3350,var_3351,], output)
mod['func_3387'] = func_3387
mod = relay.transform.InferType()(mod)
var_3388 = relay.var("var_3388", dtype = "uint16", shape = (15, 2, 6))#candidate|3388|(15, 2, 6)|var|uint16
var_3389 = relay.var("var_3389", dtype = "uint16", shape = (15, 2, 6))#candidate|3389|(15, 2, 6)|var|uint16
output = func_3387(var_3388,var_3389,)
func_3390 = relay.Function([var_3388,var_3389,], output)
mutated_mod['func_3390'] = func_3390
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3401 = relay.const([[[9,7,-7,4,9,-5,9,1,-2,6,7,-6,4],[3,10,-7,-2,-1,-9,-6,-7,5,-7,-5,-7,2],[7,-8,-8,4,2,6,-6,-2,4,-3,-9,8,-9],[6,-1,9,-8,10,-7,-5,8,3,-10,8,5,4],[2,-9,-4,6,-7,7,3,3,-4,10,-2,5,-10],[-8,6,8,-6,10,5,-9,-2,-10,-4,4,-3,-1],[7,-9,-10,-3,-10,8,-9,-8,-4,-7,-3,-9,9],[-4,-8,-1,2,-4,-8,-1,-8,-4,7,1,9,8],[-4,7,-2,10,-8,7,-1,-2,-7,-5,2,-10,-1],[2,1,-10,-9,-10,9,-5,1,7,-2,-10,2,4],[7,4,-6,-8,8,-2,6,-10,-6,-4,-6,10,9]],[[-8,7,6,-7,2,9,-10,9,-4,8,1,-8,8],[5,-5,-7,-5,7,8,4,-7,1,1,-1,-4,8],[10,2,3,7,-10,-3,9,-8,5,-7,6,10,-8],[2,-10,9,8,8,-7,-9,9,3,3,-5,3,3],[-1,-9,-3,-3,3,3,-3,3,5,-10,8,-2,-3],[1,10,7,6,2,-7,4,-7,1,7,-4,8,7],[-5,8,8,6,-1,1,9,7,-8,-3,-8,-7,-8],[5,2,3,3,-7,-9,10,8,-7,5,-2,-5,-10],[-1,7,-5,-7,-6,-6,2,-1,8,10,5,2,3],[4,1,2,10,-1,-2,4,9,-9,5,9,-3,9],[10,9,7,3,9,2,-3,-4,9,4,-8,-8,-5]],[[8,8,8,-1,1,-2,10,8,-9,-4,7,-1,-1],[6,-3,6,8,1,2,-3,-3,-7,-4,-4,-7,8],[-2,-7,-9,2,-3,-5,4,7,9,-1,4,-5,3],[3,-8,4,-9,4,-3,10,-7,-6,-1,9,2,-4],[7,5,1,-10,9,10,4,-4,10,-10,10,-2,-9],[-3,-2,-7,8,-1,-2,-7,-4,10,1,-4,9,2],[9,10,-6,9,2,8,-10,9,9,-4,5,10,8],[-10,7,-6,-7,-4,-3,-10,-9,-5,7,-10,9,9],[9,-1,5,-6,5,-9,-10,3,6,-8,-2,-3,-6],[5,-8,-3,-6,-4,8,-3,3,3,-5,-9,-2,3],[2,2,10,5,-6,4,5,-2,9,-3,-7,8,-5]],[[-10,-3,-8,10,3,1,-7,8,-8,-3,-5,-6,-5],[-5,7,-9,6,2,5,5,-4,-5,3,2,8,2],[8,-2,-2,-7,8,6,7,7,1,-9,-10,6,10],[5,-5,-1,-4,9,9,-7,-3,-10,-2,-2,3,-10],[6,8,-5,-5,-9,-5,-9,-1,2,7,10,6,6],[-6,9,-4,1,-2,5,7,6,-9,6,-7,-7,-4],[2,10,7,-9,-6,-3,6,-5,5,-5,6,9,-3],[10,9,-8,3,-10,-7,-9,5,10,-7,2,-7,-6],[10,-4,-10,-4,10,1,-1,-6,-2,-1,-6,8,-6],[-7,7,7,-9,-2,-5,7,2,9,-10,4,-9,-1],[-8,10,7,-8,-3,4,5,-10,-6,-8,-6,2,5]],[[8,-10,10,-7,-1,-8,-1,-3,-4,4,-3,-2,9],[-9,3,-6,7,-1,-4,-7,-3,4,-9,-10,9,6],[4,-4,-5,-3,-8,-1,-3,-4,-9,1,-8,-7,-6],[-10,2,-9,-4,-9,-6,7,-9,9,-1,2,3,-3],[10,10,8,3,5,-6,4,10,-8,-4,-5,3,-5],[5,8,-1,-7,-6,-10,-5,-2,-6,4,6,2,1],[10,-5,-6,-5,8,5,-6,2,-2,2,8,10,-3],[6,-4,-5,10,1,10,-10,-9,-6,6,2,-7,-1],[2,6,6,3,10,6,5,6,1,-6,1,-7,1],[6,-4,2,-8,3,2,-6,1,-2,9,-6,4,-1],[5,3,-7,-6,5,7,8,-7,-4,-3,-7,5,-3]],[[-6,-2,-1,7,3,-2,-3,6,-8,9,-5,10,-10],[-4,-3,-4,3,6,-3,7,-6,-4,6,8,4,-3],[10,8,-2,-5,-1,-4,6,-8,4,4,6,9,-8],[8,-4,-3,-6,-4,-7,-3,-7,1,-6,2,-4,-10],[-6,2,3,8,-1,-6,5,-3,-1,9,3,1,8],[-1,-2,3,-7,-4,7,2,4,-4,7,9,6,-6],[-9,2,2,2,-4,4,1,4,9,-5,3,1,-9],[-8,10,5,2,-7,-1,-2,5,6,3,2,-7,4],[8,-2,8,1,-7,-9,4,-5,6,-9,3,-5,-9],[-10,-5,8,2,10,3,9,-10,9,4,-10,-1,-1],[6,3,-4,4,7,-3,-4,-2,4,7,10,9,-7]],[[-6,10,3,5,3,-8,9,7,-6,-4,-9,10,4],[9,-5,2,5,1,10,-5,-5,8,-8,-5,7,5],[-10,2,-4,-9,7,2,-3,-1,1,6,9,-8,-10],[-1,4,4,10,10,-7,7,-10,8,-4,-8,7,8],[7,-2,1,-7,1,9,-7,7,7,10,3,-1,-8],[-1,-5,2,-7,1,10,-2,-1,-2,9,-4,3,2],[-1,4,-3,6,-8,-10,-3,-2,10,3,5,2,5],[8,10,-6,6,2,-9,-7,-9,9,-1,6,-6,-5],[-2,-5,-2,7,-5,-3,-4,-10,3,7,6,5,-8],[-9,8,5,2,9,5,4,-8,10,-1,-3,8,10],[8,3,4,2,7,-6,-7,1,-2,1,3,1,4]],[[2,-6,7,-6,1,4,6,3,10,-8,2,-7,7],[6,6,4,3,-10,5,3,-8,1,6,-7,-4,9],[-2,-10,-8,8,8,4,3,4,-2,4,-3,5,9],[-8,-6,8,3,8,6,-7,-2,-8,7,-3,-10,-8],[-1,2,6,2,7,1,-10,1,-8,2,9,3,3],[-4,2,-4,6,7,-8,-5,1,-4,8,-8,-6,-6],[-2,3,-4,6,9,-3,10,9,10,-2,4,1,5],[-8,-2,8,-3,7,7,7,7,-3,1,4,7,-2],[4,-5,-5,-10,7,-10,8,-10,-3,1,9,5,-7],[1,5,-7,9,9,-4,10,8,4,7,3,4,-10],[-9,5,3,1,1,8,9,5,-6,-9,-5,2,-8]],[[4,8,-5,8,-2,7,-1,-1,-10,6,-8,-10,-9],[-9,-9,-6,6,-6,1,-2,4,-8,8,2,4,3],[2,-6,-8,-4,9,-9,-3,8,8,-1,-9,-5,-8],[7,7,-3,-1,2,3,8,3,1,-2,-2,-10,3],[1,6,-5,3,-3,10,5,-5,5,4,-1,-6,5],[5,10,-3,-6,-10,4,-2,10,-4,4,-5,5,9],[-4,10,4,5,3,-4,-8,7,-10,10,-3,-4,6],[-5,1,-4,2,6,-9,-9,8,-1,-10,8,-9,9],[-5,-6,4,-9,-9,4,8,5,-1,-2,-10,5,3],[-9,4,-2,-10,-1,4,-3,-6,4,5,3,-6,4],[10,-3,5,-3,9,-1,8,7,-3,-4,-5,2,8]],[[7,2,9,3,5,5,8,-5,-4,10,-4,-10,-9],[-9,-7,8,-2,-7,4,-4,-7,-7,2,3,-7,-9],[-5,1,6,-7,-6,6,7,8,3,-10,-10,7,-1],[10,-5,-8,8,6,-9,6,2,-3,5,-10,-5,9],[9,7,-8,9,6,4,7,5,-7,-3,-2,7,10],[-6,-2,-10,2,-3,4,4,7,1,1,2,-8,-6],[3,-8,5,-8,10,7,5,10,10,-7,-1,-3,-6],[-10,-1,-5,-2,-7,-8,3,3,7,8,5,-3,-4],[-3,-9,-3,-5,7,-9,2,7,1,7,-10,9,-4],[-5,-9,3,8,-2,3,5,7,1,10,-1,-8,2],[-5,-5,9,5,-8,1,2,-5,1,7,6,9,-5]],[[-4,1,2,-10,4,-6,-7,-9,8,-4,-8,-5,-4],[2,6,8,-2,-7,-2,3,6,6,2,4,9,-7],[4,2,4,3,-3,9,9,-4,-4,-8,-4,4,10],[-10,-5,-5,-8,8,3,1,4,3,-7,-8,-4,1],[-1,-6,4,-1,2,9,5,9,9,-5,-9,8,-7],[-8,5,9,-6,-8,-2,3,-4,-1,10,-6,9,5],[10,-7,-10,-6,-6,-10,1,-7,6,6,-10,1,-6],[-2,6,6,-9,-3,-9,5,-7,8,-4,10,4,-3],[2,6,-9,-6,4,-5,6,-5,8,-10,6,2,2],[-3,9,-1,-10,-2,7,-7,1,-5,9,-3,1,-1],[-1,10,-6,-2,-9,-7,-1,-9,8,-9,-6,-7,-6]],[[2,-2,-6,-6,8,9,5,2,6,-3,-2,-1,-8],[-5,3,-5,-7,-8,2,9,-5,2,6,-4,-7,-9],[5,-8,-8,10,-2,-6,4,4,-9,-7,-1,4,3],[10,-4,9,-1,-6,9,2,-1,-4,4,4,-1,8],[10,-7,-2,4,-8,-9,9,-9,1,2,10,8,4],[-7,-3,-6,1,-7,-4,10,4,-10,5,1,-1,-10],[9,-4,10,-9,-8,-7,2,-1,6,10,-5,3,2],[-7,-9,1,-3,-4,-8,-7,9,7,-9,-10,4,-7],[10,8,-5,2,-10,-3,-2,7,9,-8,9,2,6],[2,-1,6,8,3,6,7,-2,10,-7,-2,2,-5],[-7,-8,-8,-10,9,10,9,3,1,-3,2,5,-2]],[[-6,-8,5,5,-8,-6,-1,6,4,-7,3,9,-8],[-1,10,1,8,-6,-5,-8,5,-3,1,-10,-7,4],[-2,7,-3,3,2,1,3,4,-8,5,8,-10,9],[4,4,9,-10,-7,7,-10,4,-8,7,-9,6,-8],[1,-1,-7,-8,2,6,6,-7,-5,-9,-8,-8,-10],[-2,10,-9,8,-3,7,-6,1,-3,7,-9,8,-1],[-6,1,-7,-2,-5,-10,-1,7,-4,-8,-5,1,10],[-4,9,-5,6,1,-1,10,2,-8,-3,-4,8,-4],[-3,-6,-5,3,8,9,6,-7,2,4,9,10,6],[9,-4,-8,-7,9,-7,-8,-10,8,8,4,5,4],[1,6,-6,3,9,8,-6,-10,9,9,-8,5,2]],[[-5,-9,-1,-3,-8,-3,2,10,9,-4,10,-8,3],[6,1,-9,-7,5,9,-6,-8,5,10,-7,5,10],[7,6,4,-1,-2,-3,-1,4,6,-8,-8,6,10],[8,9,3,-6,7,1,-6,10,-9,-8,2,4,2],[-3,-1,-2,-10,-7,-6,-4,-4,2,-7,1,-7,2],[5,-9,9,3,-9,-10,-7,-4,1,-7,2,-5,4],[-6,7,10,3,8,5,1,-8,3,-10,-8,4,4],[-7,-2,6,-3,3,4,-5,7,4,6,-8,7,5],[-9,-3,2,3,-10,-3,2,6,-3,8,5,-7,-6],[-9,5,10,-2,6,-10,1,7,-3,-9,7,-4,-1],[9,-7,4,-7,1,-10,8,-8,-4,10,-2,-2,-6]]], dtype = "int32")#candidate|3401|(14, 11, 13)|const|int32
var_3402 = relay.var("var_3402", dtype = "int32", shape = (14, 11, 13))#candidate|3402|(14, 11, 13)|var|int32
bop_3403 = relay.less_equal(const_3401.astype('bool'), relay.reshape(var_3402.astype('bool'), relay.shape_of(const_3401))) # shape=(14, 11, 13)
output = bop_3403
output2 = bop_3403
func_3407 = relay.Function([var_3402,], output)
mod['func_3407'] = func_3407
mod = relay.transform.InferType()(mod)
var_3408 = relay.var("var_3408", dtype = "int32", shape = (14, 11, 13))#candidate|3408|(14, 11, 13)|var|int32
output = func_3407(var_3408)
func_3409 = relay.Function([var_3408], output)
mutated_mod['func_3409'] = func_3409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_3411 = relay.TupleGetItem(func_2173_call(), 0)
call_3412 = relay.TupleGetItem(func_2175_call(), 0)
func_2485_call = mod.get_global_var('func_2485')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_3421 = relay.TupleGetItem(func_2485_call(), 1)
call_3422 = relay.TupleGetItem(func_2487_call(), 1)
func_2306_call = mod.get_global_var('func_2306')
func_2309_call = mutated_mod.get_global_var('func_2309')
const_3425 = relay.const([[True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False],[False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False],[True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True],[False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False],[True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,False,False,False],[True,True,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False]], dtype = "bool")#candidate|3425|(6, 28)|const|bool
call_3424 = relay.TupleGetItem(func_2306_call(relay.reshape(const_3425.astype('bool'), [1, 168])), 2)
call_3426 = relay.TupleGetItem(func_2309_call(relay.reshape(const_3425.astype('bool'), [1, 168])), 2)
func_2547_call = mod.get_global_var('func_2547')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_3431 = relay.TupleGetItem(func_2547_call(), 0)
call_3432 = relay.TupleGetItem(func_2549_call(), 0)
func_2211_call = mod.get_global_var('func_2211')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_3440 = func_2211_call()
call_3441 = func_2211_call()
uop_3443 = relay.exp(call_3424.astype('float32')) # shape=(6, 4, 7)
uop_3445 = relay.exp(call_3426.astype('float32')) # shape=(6, 4, 7)
output = relay.Tuple([call_3411,call_3421,const_3425,call_3431,call_3440,uop_3443,])
output2 = relay.Tuple([call_3412,call_3422,const_3425,call_3432,call_3441,uop_3445,])
func_3447 = relay.Function([], output)
mod['func_3447'] = func_3447
mod = relay.transform.InferType()(mod)
output = func_3447()
func_3448 = relay.Function([], output)
mutated_mod['func_3448'] = func_3448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3531 = relay.var("var_3531", dtype = "float64", shape = (12, 3, 16))#candidate|3531|(12, 3, 16)|var|float64
uop_3532 = relay.log(var_3531.astype('float64')) # shape=(12, 3, 16)
func_2392_call = mod.get_global_var('func_2392')
func_2394_call = mutated_mod.get_global_var('func_2394')
var_3536 = relay.var("var_3536", dtype = "bool", shape = (216,))#candidate|3536|(216,)|var|bool
call_3535 = relay.TupleGetItem(func_2392_call(relay.reshape(var_3536.astype('bool'), [9, 4, 6])), 0)
call_3537 = relay.TupleGetItem(func_2394_call(relay.reshape(var_3536.astype('bool'), [9, 4, 6])), 0)
const_3551 = relay.const([[[9.140985,-9.936353,-5.328532,-0.620089,6.252252,-2.538067,1.211046,-9.372873,-6.570192,8.160519,7.157955,9.580221,4.900455,3.163889,0.147343,6.738954],[-7.321314,3.696846,-3.142929,-1.581165,-7.177365,-9.998792,3.128677,-4.380801,2.365561,9.852450,-1.770618,0.173248,-3.207521,9.753736,6.410006,-4.422242],[-2.194437,-6.677205,5.302536,-7.541462,-7.317969,-0.926251,6.373084,7.893874,-5.899386,-7.122520,-5.334087,-1.910927,-8.669234,-2.014315,5.466980,9.172916]],[[-3.720837,-6.142186,-4.514148,0.264256,2.793675,-8.236319,-0.703092,7.311670,-7.420142,-4.216403,2.742707,8.698358,-7.726893,2.275652,8.032476,8.280430],[-4.105914,5.373890,-0.805212,1.838515,-1.797101,-9.435702,-1.257687,-4.393093,7.719266,8.151252,6.210306,-8.472618,-8.178604,0.980775,-3.758069,-5.929643],[-1.542135,7.832505,-8.369868,-7.093477,-7.747616,-4.372555,-2.544332,2.376703,5.821822,-3.939813,-5.129670,-6.608343,-4.327472,-1.138866,-4.149976,-7.513601]],[[-3.385928,8.388261,-5.780064,-3.597545,-5.150609,8.659500,2.860818,1.207713,6.740330,1.749322,-5.401500,1.016958,-6.069843,-7.165747,-7.732177,6.631943],[-8.987806,4.630902,4.549479,-1.975425,-1.979645,-2.151807,-6.550060,-2.357710,-2.968961,5.638534,0.847316,9.753262,-5.914452,-7.680975,-2.582328,-8.241068],[-7.854024,-5.888668,1.693213,-4.596561,-4.838110,0.496066,-0.733591,9.585976,4.196559,3.266645,7.604557,-1.226447,-0.316803,-1.386682,0.235057,-9.968089]],[[-3.419742,1.887321,4.065649,-9.529077,-5.048572,-2.661810,9.753050,8.557704,5.167635,-9.247500,-4.228324,-8.078057,8.245064,4.433311,1.085897,2.453411],[-5.609923,3.746413,-4.197054,-2.454345,8.507767,1.924047,-0.917822,-7.920786,8.509283,-6.413365,9.638246,5.306583,9.113446,4.296299,-5.599551,-2.193454],[6.107161,-0.439345,8.476929,6.004827,0.984499,-6.594293,9.372254,7.472998,2.844716,-0.562773,5.409532,1.377394,5.258796,5.125437,2.744223,-3.189761]],[[-6.564861,-8.921657,9.886311,-2.884253,-7.660792,-9.164326,2.425977,6.672539,9.562090,-2.001710,9.021120,4.741316,-6.809422,-2.649413,0.210568,1.499210],[1.847152,4.117281,9.771605,7.072263,-0.713672,5.731316,-5.905127,-5.222720,7.394624,-2.160850,4.592903,5.010023,-0.727998,4.755212,-5.197923,2.749328],[4.697967,2.071147,2.271192,-9.366839,-8.452071,6.548584,-8.783230,7.571944,-1.058987,-4.828582,0.821982,-5.192472,5.076760,0.754625,-7.208347,3.902490]],[[-6.708438,-8.221208,-0.945852,1.678634,-9.990157,8.759592,5.814206,-6.048368,-6.504718,6.829818,-9.293217,4.886282,6.980658,-4.833311,-8.475828,5.821121],[-2.249039,-3.296931,7.374749,4.420258,-4.316090,-7.829274,1.785503,-8.678629,-9.637242,-6.509910,3.347754,-5.345697,-0.890178,-9.260570,7.548333,7.163966],[0.862625,-4.688379,-9.669219,-1.022128,-6.335787,-2.458573,-9.777158,9.372804,-0.223054,5.632796,8.041656,-4.865710,-4.270376,-8.052544,4.846362,8.223951]],[[4.804740,7.380700,-6.034251,3.420043,-0.015266,-7.826798,-4.394546,2.323869,6.341237,-2.596622,3.086091,8.130353,6.515581,7.288190,3.114279,5.465001],[-4.021167,-2.602614,-0.622067,7.240219,9.420920,1.087640,0.534223,-9.033980,-2.690767,1.389312,-8.893548,6.030551,2.886845,-2.651930,-5.028718,8.650508],[-3.196262,1.976073,0.872578,5.444635,-3.616998,-0.403168,-8.257341,8.096164,5.593495,-5.117583,2.762141,0.411686,-9.761902,7.542650,6.692075,6.506485]],[[5.434931,8.781657,8.628366,1.270426,6.897280,6.010995,1.613706,-8.687311,8.178526,-0.024771,9.576791,8.639818,9.011716,-3.018656,-0.955889,-5.298150],[-1.638928,-3.394704,-0.567234,4.966392,-2.495902,3.742288,8.461601,-8.410113,-9.224682,3.328749,4.918055,8.829646,-0.089056,0.384137,0.147259,-1.937302],[1.416602,3.745545,-7.040211,-7.147485,4.961945,-1.749578,8.691838,-7.301736,2.447837,0.674082,-3.444738,6.570998,-6.073612,0.650495,-7.113952,9.170659]],[[2.144482,-1.146812,-0.455629,-1.097035,-6.561481,-6.819449,8.111727,-9.735679,8.343819,9.544469,-5.785669,-0.873381,-8.780273,6.285709,6.799674,-8.602270],[5.486741,-5.584718,5.047757,-2.924834,-7.304897,-8.743286,7.452249,-5.113826,-1.914778,-4.436292,4.541663,-0.506496,1.819662,-3.703451,-2.354295,0.863494],[0.766237,1.978398,-8.979201,5.206619,7.150567,-3.297189,-2.197245,8.865665,2.062936,5.056297,-4.398170,-9.610623,5.589641,-8.331578,5.022231,-7.664884]],[[9.184946,-4.639556,8.892349,-4.677484,4.428009,2.424467,-6.144342,-7.936071,-9.958799,-6.762161,3.952959,-1.132497,0.468603,7.074290,-8.076783,-0.434367],[4.200607,8.954154,-3.295208,5.339280,7.249330,9.345538,7.576925,1.954819,1.198216,-0.575920,-1.828571,-6.106474,3.187677,-3.405168,3.318770,-1.390748],[9.192170,9.714659,8.673968,8.516448,0.586573,-3.625677,8.503684,-3.746931,8.930136,3.707061,-2.148381,-8.231487,3.443317,3.553856,6.671372,-2.215171]],[[-2.538386,-3.309247,-0.987665,-0.765378,-9.385541,8.626503,-1.107138,-3.801396,-0.032371,3.674585,0.475433,5.892696,-6.180574,6.686118,-2.614460,8.838840],[2.003035,-7.374976,1.367981,0.015956,-5.865854,5.171810,0.424851,-6.970429,-9.817154,-7.792671,6.703948,-0.772337,-1.476068,9.845008,7.938280,0.184009],[-3.997834,9.269791,-7.255712,3.121491,8.337846,9.416053,8.377763,-5.804944,2.203432,2.109063,-1.984495,0.548889,-5.867879,3.312800,3.191834,-1.998830]],[[9.124753,0.935985,8.456519,-9.812500,-5.193455,4.692954,6.104862,6.865213,-3.677427,-6.057267,-6.668398,3.210108,-3.467314,3.299560,-4.209512,-8.912462],[2.843012,6.156644,-7.822685,9.439394,-7.437336,-0.569436,-2.270326,-9.660667,0.557718,-6.893812,-8.549120,-0.412794,-4.277343,-0.989973,3.258986,-0.186116],[2.067185,6.312741,1.407850,-0.371228,9.410300,-5.155725,-9.475076,-0.619361,6.414857,9.461553,0.622216,-7.315608,7.646160,-8.662108,0.384505,0.895073]]], dtype = "float64")#candidate|3551|(12, 3, 16)|const|float64
bop_3552 = relay.add(uop_3532.astype('uint32'), relay.reshape(const_3551.astype('uint32'), relay.shape_of(uop_3532))) # shape=(12, 3, 16)
func_3050_call = mod.get_global_var('func_3050')
func_3051_call = mutated_mod.get_global_var('func_3051')
call_3560 = relay.TupleGetItem(func_3050_call(), 2)
call_3561 = relay.TupleGetItem(func_3051_call(), 2)
output = relay.Tuple([call_3535,var_3536,bop_3552,call_3560,])
output2 = relay.Tuple([call_3537,var_3536,bop_3552,call_3561,])
func_3567 = relay.Function([var_3531,var_3536,], output)
mod['func_3567'] = func_3567
mod = relay.transform.InferType()(mod)
mutated_mod['func_3567'] = func_3567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3567_call = mutated_mod.get_global_var('func_3567')
var_3569 = relay.var("var_3569", dtype = "float64", shape = (12, 3, 16))#candidate|3569|(12, 3, 16)|var|float64
var_3570 = relay.var("var_3570", dtype = "bool", shape = (216,))#candidate|3570|(216,)|var|bool
call_3568 = func_3567_call(var_3569,var_3570,)
output = call_3568
func_3571 = relay.Function([var_3569,var_3570,], output)
mutated_mod['func_3571'] = func_3571
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3581 = relay.var("var_3581", dtype = "float32", shape = (5, 13, 7))#candidate|3581|(5, 13, 7)|var|float32
uop_3582 = relay.log(var_3581.astype('float32')) # shape=(5, 13, 7)
uop_3584 = relay.acos(uop_3582.astype('float64')) # shape=(5, 13, 7)
bop_3593 = relay.right_shift(uop_3584.astype('uint16'), relay.reshape(uop_3582.astype('uint16'), relay.shape_of(uop_3584))) # shape=(5, 13, 7)
output = bop_3593
output2 = bop_3593
func_3601 = relay.Function([var_3581,], output)
mod['func_3601'] = func_3601
mod = relay.transform.InferType()(mod)
var_3602 = relay.var("var_3602", dtype = "float32", shape = (5, 13, 7))#candidate|3602|(5, 13, 7)|var|float32
output = func_3601(var_3602)
func_3603 = relay.Function([var_3602], output)
mutated_mod['func_3603'] = func_3603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1774_call = mod.get_global_var('func_1774')
func_1776_call = mutated_mod.get_global_var('func_1776')
call_3624 = func_1774_call()
call_3625 = func_1774_call()
output = relay.Tuple([call_3624,])
output2 = relay.Tuple([call_3625,])
func_3662 = relay.Function([], output)
mod['func_3662'] = func_3662
mod = relay.transform.InferType()(mod)
output = func_3662()
func_3663 = relay.Function([], output)
mutated_mod['func_3663'] = func_3663
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3731 = relay.var("var_3731", dtype = "float32", shape = (1, 12, 4))#candidate|3731|(1, 12, 4)|var|float32
uop_3732 = relay.erf(var_3731.astype('float32')) # shape=(1, 12, 4)
output = uop_3732
output2 = uop_3732
func_3739 = relay.Function([var_3731,], output)
mod['func_3739'] = func_3739
mod = relay.transform.InferType()(mod)
mutated_mod['func_3739'] = func_3739
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3740 = relay.var("var_3740", dtype = "float32", shape = (1, 12, 4))#candidate|3740|(1, 12, 4)|var|float32
func_3739_call = mutated_mod.get_global_var('func_3739')
call_3741 = func_3739_call(var_3740)
output = call_3741
func_3742 = relay.Function([var_3740], output)
mutated_mod['func_3742'] = func_3742
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3757 = relay.var("var_3757", dtype = "int16", shape = (9, 7, 13))#candidate|3757|(9, 7, 13)|var|int16
var_3758 = relay.var("var_3758", dtype = "int16", shape = (9, 7, 13))#candidate|3758|(9, 7, 13)|var|int16
bop_3759 = relay.logical_xor(var_3757.astype('int16'), relay.reshape(var_3758.astype('int16'), relay.shape_of(var_3757))) # shape=(9, 7, 13)
bop_3767 = relay.minimum(var_3757.astype('uint64'), relay.reshape(bop_3759.astype('uint64'), relay.shape_of(var_3757))) # shape=(9, 7, 13)
const_3787 = relay.const([[[-3,5,-2,-1,-2,4,8,-5,-1,1,-5,10,-4],[8,6,6,-8,7,2,10,9,-6,-4,-1,-3,4],[-1,1,-9,-1,-4,4,6,4,9,1,-10,5,7],[-10,2,10,10,-9,2,-4,7,-10,9,-2,-8,6],[-2,-3,-1,-1,8,-6,-5,-9,-7,5,1,8,7],[-10,-4,4,-9,7,1,3,-1,8,-4,-5,10,-6],[3,-4,-3,-5,9,1,8,10,-5,-1,-9,-4,-7]],[[-7,-9,9,4,-2,8,-2,-1,-6,2,-10,-6,5],[1,-2,10,-5,-10,-1,-10,1,-2,-4,9,-4,6],[2,-5,1,8,-4,3,-7,6,9,-1,-3,-7,-10],[8,9,-7,8,-8,10,10,-4,5,-8,-9,6,-7],[-5,-7,1,8,-1,-1,-7,-6,4,-2,1,-10,-6],[-5,-9,5,-9,8,10,-1,10,-8,10,-5,1,5],[-3,-2,1,5,-2,-3,-3,-10,-6,-1,-3,-3,-2]],[[9,6,-7,8,9,-7,-1,-5,7,-7,8,-9,2],[-8,7,3,-5,-2,7,-2,-1,-3,7,9,3,-2],[-1,-9,-7,8,-1,1,-10,-8,7,5,10,-2,-5],[10,7,8,7,1,-8,-7,9,-3,-5,8,-3,-9],[3,10,2,-6,4,-9,3,4,-8,-8,-10,-8,6],[-4,2,-1,-5,-5,-1,-6,-4,7,-6,1,-1,-10],[2,6,5,6,-1,2,-10,-3,-7,7,5,-1,4]],[[-6,10,7,-6,-1,-1,8,-6,10,-9,-8,-5,10],[-8,2,4,8,-3,-8,-8,-10,8,4,10,1,-8],[-6,3,-4,8,4,3,-5,-8,5,-4,8,-3,-9],[8,-2,8,-1,5,-1,-1,-6,8,1,8,4,1],[5,4,-6,-3,-1,8,9,7,-8,-6,3,8,8],[9,8,-5,3,7,2,-8,1,4,9,2,10,-4],[2,8,-9,-3,5,2,-5,-7,-10,-1,1,3,-7]],[[-1,-4,3,-6,5,5,4,4,-10,-6,-10,-4,-7],[8,-6,6,-3,2,-6,6,6,9,-3,-6,6,10],[8,6,-10,7,9,-3,6,10,-6,3,-8,-3,-7],[-4,1,-8,-9,-8,9,4,1,-4,-5,-10,3,-4],[-10,-9,-6,-10,8,-9,2,-3,3,3,-7,4,3],[2,9,-6,2,6,10,-6,3,3,-1,10,-6,-9],[-2,-4,6,3,-1,-4,6,-1,-5,-3,2,-6,6]],[[6,-1,-6,7,9,5,9,-1,-1,5,3,10,-10],[4,5,4,-2,6,7,8,-9,8,-1,2,-5,-3],[-9,-4,5,-5,-8,2,3,9,-3,7,-10,-9,5],[-2,-10,-1,-9,-8,-3,-3,-3,4,-2,7,10,7],[-9,2,2,4,-8,-1,-10,-1,5,7,-10,-5,5],[-10,-7,6,5,-10,9,-1,1,-6,-2,-5,1,-4],[-4,-3,-2,-4,2,-5,-6,-6,-2,-4,8,3,6]],[[-8,1,-10,-2,4,8,4,-5,-6,5,8,8,10],[1,-7,-3,-6,8,1,-8,5,4,5,8,2,5],[9,-1,1,-4,1,-5,4,-4,5,-2,10,-8,5],[8,7,5,-7,9,-10,-8,8,1,-9,7,-9,-2],[4,5,6,-7,5,3,10,-1,4,-5,-5,4,-1],[9,3,10,3,-9,9,4,-9,7,10,2,-1,6],[-3,-1,-5,-6,-2,-6,-4,-4,10,-8,-8,10,6]],[[9,9,3,-8,-6,-7,-1,-1,-3,-3,-9,-6,2],[3,-9,-4,-6,8,4,-6,-10,5,1,10,2,-1],[-6,9,1,10,2,-2,6,2,5,10,-2,-7,-2],[6,-10,-6,-6,-6,10,-8,-7,-5,-10,3,-4,1],[8,8,6,-6,5,-5,-1,-9,-5,5,9,5,4],[3,10,5,-1,-10,9,5,1,4,-9,3,1,-7],[8,10,-1,2,-8,-1,-10,-7,-8,2,10,-1,8]],[[-4,2,9,-3,-1,-3,-8,-10,1,-2,10,1,-1],[-5,-2,6,3,-5,-5,-3,-5,-1,-9,-3,-2,7],[5,1,8,8,-2,4,-2,10,-1,6,-1,-10,10],[1,6,-2,-7,-9,-3,-5,-5,10,1,-7,-5,10],[-1,-8,-2,3,-6,-3,9,8,-10,7,-3,3,9],[6,-6,-1,5,-8,-8,-8,-5,9,-4,-8,-9,2],[-3,6,6,7,-8,-8,10,3,8,-4,2,-9,-10]]], dtype = "int16")#candidate|3787|(9, 7, 13)|const|int16
bop_3788 = relay.subtract(var_3757.astype('uint16'), relay.reshape(const_3787.astype('uint16'), relay.shape_of(var_3757))) # shape=(9, 7, 13)
func_2264_call = mod.get_global_var('func_2264')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_3791 = func_2264_call()
call_3792 = func_2264_call()
func_1597_call = mod.get_global_var('func_1597')
func_1600_call = mutated_mod.get_global_var('func_1600')
const_3822 = relay.const([-6.067398,1.900221,-8.466701,8.434594,-0.825841,-6.613976,-4.964857,-1.126563,4.890020,4.018248,-7.140145,1.759681,-1.854289,-9.036393,8.685874,0.647544,4.824239,-5.823554,-6.594049,-2.921879,6.308206,-5.652572,2.185656,2.546531,-4.754392,-3.391691,4.248392,8.205310,-9.905671,9.569847,2.265061,7.993049,8.144160,-6.024537,-9.915889,-1.962301,-4.163768,9.492335,-4.546910,-3.364672,-7.095346,5.855413,-9.195162,4.851623,-4.278037,7.431824,0.011474,-2.139765,-5.111861,8.544355,9.563596,4.238857,-0.622295,0.868733,0.826507,-0.302752,2.737834,3.730108,-6.605039,-5.089195,3.143628,-5.611359,-6.558809,-5.789477,4.555849,9.295279,9.837530,-4.967907,-1.052970,-1.903962,0.999044,2.242280,-2.199727,9.698706,6.420582,7.181615,0.651714,7.775635,-5.835336,-2.219957,8.913387,-9.879298,-5.284510,9.806704,0.211762,-8.867115,-8.859180,0.458047,-4.875735,3.268702,-1.877099,5.078381,-8.811223,7.042893,-2.100435,-5.220772,-1.642112,-2.682573,-2.734303,8.729508,-7.412235,-0.673330,8.792219,8.235128,-3.933762,5.898074,-3.579700,-3.520722,4.339252,1.273103,-8.301795,-4.564417,1.447142,2.845768,-3.414325,3.027284,3.252745,6.601753,4.522173,-1.764100,4.860177,-4.919086,-1.895917,-5.932770,-5.500597,9.566639,4.037207,3.235846,9.682297,-4.554156,5.701982,-9.753407,-7.453455,5.582792,-5.016368,4.391032,0.395578,5.763701,1.518296,-3.075886,-9.490229,-9.655376,4.898884,-5.803838,-7.215714,-7.593229,-4.828180,-3.967472,-8.435783,-1.952047,-8.732174,-7.140555,5.172841,8.463579,0.598713,-4.883015,-3.497017,1.283258,1.007737,-5.844694,3.352076,9.470144,9.317121,-5.441214,-7.004395,-7.909846,-1.376888,-1.008339], dtype = "float32")#candidate|3822|(168,)|const|float32
call_3821 = relay.TupleGetItem(func_1597_call(relay.reshape(const_3822.astype('float32'), [168,])), 3)
call_3823 = relay.TupleGetItem(func_1600_call(relay.reshape(const_3822.astype('float32'), [168,])), 3)
bop_3826 = relay.right_shift(bop_3767.astype('int32'), relay.reshape(var_3758.astype('int32'), relay.shape_of(bop_3767))) # shape=(9, 7, 13)
uop_3845 = relay.asin(const_3822.astype('float64')) # shape=(168,)
func_1210_call = mod.get_global_var('func_1210')
func_1214_call = mutated_mod.get_global_var('func_1214')
const_3852 = relay.const([8.800743,-8.235373,-0.884161,6.361726,7.313668,6.987198,-7.890873,6.262907,0.441028,-8.591281,-0.476071,-1.045655,-2.612269,4.395235,8.813332,0.386909,-0.952517,-3.309585,-4.048542,-0.687986,0.850666,-9.704758,-0.370965,-7.611933,-2.410822,1.652434,-3.110973,-4.782990,8.661350,-8.325991,-5.152970,5.031815,2.635614,6.109023,-2.517477,-5.825768,6.460958,4.589693,-3.678905,4.601042,2.871491,1.488260,5.024286,-1.120551,8.692725,2.908265,-3.576009,-9.841498,-5.487482,-2.022006,2.229554,-7.188950,5.550050,-1.637497,8.929256,-1.666464,-0.900198,-8.055065,-3.033402,-1.675942,9.196219,0.387304,5.515023,-5.438592,-7.899782,-7.831963,9.825547,-7.893020,-1.440129,-6.911759,2.695525,-2.298452,-1.555627,7.170313,1.902978,-3.935289,1.755676,7.056960,2.393443,-2.185135,-7.374847,0.047676,4.570684,-5.624874,-7.925145,-3.685393,7.371734,2.290017,9.593706,-0.403034,-9.506074,-1.933717,6.814966,-1.319964,9.647549,-7.414095,3.048347,6.347386,9.404235,5.758278,-1.673547,4.757064,-2.513624,9.544938,0.586177,3.177982,-2.564879,4.322413,1.332383,-0.467987,-0.159451,-4.835541,-9.273947,3.921806,3.624745,8.142597,-3.392407,8.705345,5.195416,-4.586363,5.317391,-2.176317,3.926914,1.028716,-6.345574,5.177005,-9.389112,-1.226388,4.109537,-3.765255,-1.579919,-8.689771,7.402995,-8.089354,-8.680593,4.471060,-9.492164,3.362036,-0.922079,-4.010479,-0.953588,8.168856,6.573626,9.747189,6.573669,2.383021,9.290377,-1.399608,2.312384,4.545109,-0.231547,8.775311,8.878819,-5.972966,3.841018,-4.122917,5.160892,-2.616491,4.519938,9.141804,-2.118086,0.987187,6.855674,-5.511824,-5.995619,-8.909266,-3.252492,4.405582,6.979398,5.764083,-9.765692,-5.999157,-1.018673,-4.739136,6.360971,-5.623252,-2.677577,5.960671,-0.745702,-1.804860,-7.534813,4.593254,4.828784,-6.137663,-5.519802,8.866364,0.040574,-9.696599,2.701620,7.317301,8.518531,-3.497300,1.335599,1.867126,2.504641,-0.064182,-1.275932,-3.900697,-4.074494,-4.358346,2.940364,3.551203,-6.562716,-5.277188,-9.384753,-0.962896,9.107310,5.858542,-0.296470,-5.091056,3.225859,2.756531,-1.783180,6.488620,-6.607629,-3.646660,0.991868,-4.186964,8.424297,7.389976,6.473009,3.970971,-0.218003,8.829205,0.882640,-7.657044,3.960367,6.355059,-1.484150,-4.543433,-9.306201,-1.433463,5.760052,0.425176,2.180878,-3.251112,-3.263898,3.283668,0.818876,-1.498083,2.877491,9.931005,-4.599743,-3.926451,2.682338,-6.589626,8.663833,9.041089,2.788596,-8.781172,-5.006556,3.202527,-2.822714,1.845936,-4.862601,1.286655,0.077867,-3.258234,8.688942,-5.315618,6.383947,-7.738682,5.960275,4.047332,1.057508,3.294187,2.405449,-0.447011,2.287202,9.899795,6.212366,8.576987,6.212938,7.252624,2.852338,9.401243,-2.069123,6.647975,9.357312,-3.434448,-3.838158,-8.636773,3.791029,-2.662439,6.846395,-6.348853,-8.547109,2.318330,8.626983,-9.880915,-2.392691,1.582404,8.388570,-0.348577,-8.715967,3.622419,-3.344419,-7.927323,4.032787,-9.649260,-7.682614,3.611464,1.700866,-1.177725,7.875654,2.915675,-7.628244,-6.708642,3.546184,-4.602621,-5.523993,7.144352,-5.748189,-5.043012,-8.180253,-0.700788,4.314693,7.490985,-3.028961,2.944279,-8.931578,4.158026,7.778410,-9.067225,-7.567747,-6.148824,8.446410,9.294447,4.970295,6.136783,-5.840244,-6.213810,5.125954,-9.715701,0.492129,-6.136107,-0.553557,-3.623378,9.750357,7.404170,-3.815116,-3.056914,8.027339,5.364813,9.668709,-6.678220,-2.576848,8.286703,-9.985852,6.502702,1.278845,2.392593,6.963545,-5.631773,-6.603340,-9.383055,9.245785,-2.391861,-3.693412,-5.352415,-0.024892,4.712741,7.972466,4.235921,5.204045,-4.760546,-9.923405,-5.424867,9.152029,-0.600425,-5.360739,-8.572832,-5.238412,-0.382922,-9.768122,-9.444101,5.843634,8.309924,1.016614,-0.483300,1.855300,3.454748,-4.917564,6.971745,-2.676335,-5.974005,-0.307037,1.304839,8.794934,2.911915,-5.575943,4.763349,-6.963386,-5.444263,5.875376,-2.044538,4.908894,-4.262466,0.099259,-9.240342,6.746648,2.382232,4.223395,-9.861494,-7.464614,3.588596,-5.230000,0.285701,8.715396,-5.254733,-1.441170,-1.630738,-5.934621,-8.023210,-7.812771,-9.619384,4.014027,-7.596447,-7.843302,4.816945,-6.264580,3.071126,5.211206,3.439980,-1.116477,6.219863,-5.460293,7.245339,-5.171435,9.273301,-3.733245,1.173121,8.963218,-3.342852,-0.633615,-4.640575,-1.924485,1.663745,-3.239660,4.554797,-6.086233,-7.497615,-6.139317,-5.582459,4.482645,8.220250,2.168510,9.132578,-8.780573,-6.093890,8.320773,-1.594459,-2.314942,-1.257836,-2.728853,7.881808,-2.057230,-7.570962,2.855131,-2.879852,-4.260032,-0.210481,-6.397987,-8.346627,-0.237296,5.599191,3.723528,4.672753,-1.071625,3.448262,3.373075,8.694119,-1.521108,-9.933849,-2.497837,-1.958504,7.058085,-2.761617,-7.209407,-3.740508,6.844021,-8.533129,0.344234,-1.567522,9.721253,1.206796,2.760276,8.186008,-3.825682,0.829444,-1.604134,9.560568,5.814732,8.997333,-9.525002,-4.941175,8.314971,-3.084595,-4.358214,-0.495081,-2.585886,8.645981,5.302773,8.537381,-9.029498,-3.086290,-0.869174,-9.777194,-9.357303,5.800910,-8.951911,-6.379786,5.216567,-2.680359,-8.281418,7.634089,-9.991133,-8.960249,9.325120,8.342617,-5.654563,-0.412562,4.407998,-5.097104,-0.359641,-2.427135,4.932632,3.046912,-3.860478,3.047529,-6.300726,5.435381,7.822081,-8.135170,-3.585498,-2.777713,-9.396725,9.758652,-2.208411,3.895157,-8.968275,8.988381,-9.896227,-7.864229,-3.362224,7.549496,-2.478923,-4.895055,-8.491023,9.550067,-3.314116,-9.660129,-5.009628,0.399323,2.435471,-3.062829,-5.918587,-0.986605,-2.738772,7.046328,-6.998896,4.892294,-0.989112,-0.075624,9.202632,4.171331,7.331364,-1.339295,3.840765,-2.229743,-6.296174,-9.226506,-9.090004,4.195366,6.936425,-2.811167,-7.555536,1.616908,9.431912,6.224721,2.897186,-1.630245,-6.921165,-7.530958,-9.981952,2.827806,6.419853,-9.917548,-1.117289,-1.215170,-7.601368,8.234962,7.182325,6.770773,-9.286512,7.697723,6.110384,-3.967616,-8.482685,-8.498331,-1.450632,8.245752,9.393053,5.961225,3.782543,-3.078482,-3.390827,-2.481771,-4.514086,-2.435752,6.222360,-5.863720,-9.605500,-8.578658,4.364020,4.885099,-9.416675,-0.349495,-4.680849,5.285244,1.385527,-0.375958,8.280490,2.255862,-8.926350,-9.711239,9.260560,4.607011,-4.634277,-2.650179,-7.698032,7.326953,-0.623934,-8.079624,7.662287,0.390439,6.162796,5.128424,-1.202881,-2.506413,-9.651547,-6.809610,9.296901,7.525842,-7.960961,-9.255618,-0.714509,3.555619,5.414068,2.120521,-8.245607,2.153663,-7.725134,-7.135140,-0.970684,-5.636988,-4.379634,-8.526862,-5.496448,8.748037,-6.833946,3.036185,2.135840,4.449255,-5.291404,4.876718,1.710546,4.045399,3.205487,4.298685,-4.466122,4.692422,-5.340326,3.002390,5.136403,4.598318,-6.651189,-5.013519,-2.600034,-5.885035,3.063400,7.353982,-1.327255,-0.639169,-6.236421,2.696930,2.765985,1.458976,9.637621,-0.594617,0.805978,-4.569777,-9.592083,6.457994,-3.734300,-3.924399,-0.532580,3.982768,-9.379888,-7.672290,5.725815,2.887158,-4.305676,-5.236667,4.236823,8.673708,6.997182,-8.636073,-3.877215,-3.378771,4.181794,-1.130195,-2.367824,3.997908,-3.411802,5.350253,6.178039,-0.098730,-3.644722,0.096036,-3.957786,-1.298439,-6.111321,4.451408,3.672776,-6.536772,-8.966002,-3.499634,-5.468854,9.527456,7.877892,-6.752289,-4.318267,6.587819,6.121297,-2.537582,3.321258,3.055231,-5.024137,-6.681923,-1.235178,-8.649883,-5.002628,4.571350,-5.791184,2.966016,-9.549448,0.122610,-0.739374,9.805601,7.682626,1.981181,-6.404857,4.251927,-7.740626,-5.183944,-6.046292,5.907433,0.185043,1.503221,-6.195259,-8.853851,-8.047490,6.181634,-5.800325,-4.448764,-3.195473,-0.028745,3.623952,7.481683,4.891788,-9.056519,8.337838,-3.191897,2.452157,-0.194450,-6.931610,-7.298210,-5.741522,-4.489094,-7.591672,3.714919,-2.779793,3.601658,4.873708,4.076019,5.705368,-7.354121,-4.602948,0.456095,-6.384248,8.859963,-8.940750,5.818138,7.929999,4.628227,-5.292550,-7.032740,-8.843181,-3.534847,3.545709,8.323778,-8.247205,1.645269,-3.537322,-8.664822,-0.141019,-9.562420,7.885740,-0.512137,6.646315,-1.632624,-0.841951,-8.961406,-3.531122,-5.792331,1.818721,-3.283310,8.461612,-9.230974,4.744995,-0.704795,-9.792147,-5.346487,-5.387997,-4.506527,3.232128,8.423480,1.004442,-7.084596,0.620288,3.866533,-4.245698,-9.059110,4.634186,-2.290022,8.805319,1.439533,5.019164,2.880376,-0.542076,4.177982,-5.593116,4.526669,-4.696630,1.242327,-1.254329,-3.683920,2.606934,-7.798650,9.507250,1.482968,4.842571,-1.383789,-8.044722,-9.216566,5.367980,-9.245451,-8.607443,-4.297262,-7.097245,-4.625776,-9.798148,1.852012,6.811624,9.561030,-5.967834,4.000374,1.318972,-3.868189,9.334793,-1.154972,-8.204411,-6.222154,-1.514516,-6.915052,2.016130,4.534797,8.672432,3.934510,-0.445654,-4.002897,4.492477,-8.611745,1.526896,-0.338284,7.494623,-9.327948,-3.359096,-8.189077,6.905667,0.439022,-6.685251,-7.773696,5.620061,-9.881509,-5.773235,6.320909,7.379426,-8.515073,-5.309855,5.996952,6.219711,-1.354696,5.555316,-6.433201,3.382289,2.024408,-9.697078,5.607424,7.069189,6.916792,-8.280005,5.933296,-2.382524,9.340620,-2.749151,-2.726354,-5.017208,7.065780,-4.317366,-0.147726,1.359590,3.540370,5.870127,-8.168163,-7.063971,1.343290,-4.353564,-5.991604,-8.439827,6.024130,2.653210,9.927343,-9.701989,7.407676,-3.599672,-0.657661,3.946088,-1.640992,0.377698,4.897392,-5.156450,-9.685155,3.956164,-8.451891,-0.730544,-8.356324,9.447013,2.868816,4.994077,-8.969334,-5.825495,4.811911,-2.129227,5.164198,-0.153243,-8.573757,3.954229,8.476004,6.915157,-4.851281,-8.227845,1.689462,-7.935523,8.987517,2.411032,-4.318886,6.802336,8.191936,7.830033,3.644319,7.209254,-3.253327,-6.422610,5.518224,5.372270,-1.540298,2.242704,-0.258187,-0.670952,6.924065,4.481474,-9.190892,5.448585,3.472830,-9.963273,7.902457,-8.325454,-0.985107,2.853599,-8.831238,1.389713,-6.579847,8.473280,6.679274,8.076904,0.353645,-8.365939,6.270307,-9.835139,-5.182936,2.029149,-2.809830,6.884707,-0.646303,8.042787,-8.377020,2.387506,8.257701,0.968136,6.688384,5.894591,3.228763,-5.896720,1.028519,3.507455,2.311352,5.210469,-5.750733,-7.826642,-5.645251,-8.638900,-3.062267,7.188474,-9.518275,-1.785360,1.917968,-3.622811,9.661058,1.045709,7.534779,-9.756828,5.012299,8.296277,2.750861,3.429887,4.497325,-7.647163,8.949691,5.683671,-0.370955,7.316621,2.818780,-1.688745,-6.304218,0.428994,8.418975,-5.093250,-4.772217,-6.447567,5.928082,4.222077,1.454254,6.062378,0.479847,-7.378623,-5.365145,-8.196550,-4.911542,5.989249,-3.401545,-8.191033,-7.817629,7.374801,-7.108572,-2.814626,2.933029,-3.252655,3.167394,9.377846,-6.980032,-0.586745,-2.096962,-4.594362,-8.843909,5.449448,0.986479,-7.254486,2.446675], dtype = "float64")#candidate|3852|(1080,)|const|float64
call_3851 = relay.TupleGetItem(func_1210_call(relay.reshape(const_3852.astype('float64'), [9, 12, 10]), relay.reshape(const_3852.astype('float64'), [9, 12, 10]), ), 0)
call_3853 = relay.TupleGetItem(func_1214_call(relay.reshape(const_3852.astype('float64'), [9, 12, 10]), relay.reshape(const_3852.astype('float64'), [9, 12, 10]), ), 0)
func_2306_call = mod.get_global_var('func_2306')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_3868 = relay.TupleGetItem(func_2306_call(relay.reshape(const_3822.astype('bool'), [1, 168])), 2)
call_3869 = relay.TupleGetItem(func_2309_call(relay.reshape(const_3822.astype('bool'), [1, 168])), 2)
output = relay.Tuple([bop_3788,call_3791,call_3821,bop_3826,uop_3845,call_3851,const_3852,call_3868,])
output2 = relay.Tuple([bop_3788,call_3792,call_3823,bop_3826,uop_3845,call_3853,const_3852,call_3869,])
func_3877 = relay.Function([var_3757,var_3758,], output)
mod['func_3877'] = func_3877
mod = relay.transform.InferType()(mod)
var_3878 = relay.var("var_3878", dtype = "int16", shape = (9, 7, 13))#candidate|3878|(9, 7, 13)|var|int16
var_3879 = relay.var("var_3879", dtype = "int16", shape = (9, 7, 13))#candidate|3879|(9, 7, 13)|var|int16
output = func_3877(var_3878,var_3879,)
func_3880 = relay.Function([var_3878,var_3879,], output)
mutated_mod['func_3880'] = func_3880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3304_call = mod.get_global_var('func_3304')
func_3305_call = mutated_mod.get_global_var('func_3305')
call_4013 = func_3304_call()
call_4014 = func_3304_call()
func_1077_call = mod.get_global_var('func_1077')
func_1079_call = mutated_mod.get_global_var('func_1079')
const_4044 = relay.const([8.982808,-7.308890,-8.455624,-3.443184,-0.120702,-8.695776,-9.143304,5.483120,6.980110,7.165653,-4.318363,8.594363,7.942217,3.919222,-9.675041,4.671477,5.867244,-3.642055,-9.663418,-3.404409,-7.759355,0.674517,-8.910794,-5.689792,9.158820,-0.322758,-4.151410,-8.746961,-5.785064,-0.391015,4.569967,-2.577506,7.155097,-2.039745,-8.259764,-7.837100,-1.295080,3.845395,7.912511,-6.325258,8.840393,-6.084240,-7.394632,0.393641,1.925229,5.470134,-1.410783,6.420541,-4.744260,7.307582,-8.689922,1.437980,7.860750,7.962045,-5.633979,2.979720,-0.488692,-0.921691,-7.596127,-9.937031,4.227711,-6.706473,4.777289,-4.782400,-3.028131,-9.783754,0.174554,1.785675,-6.041780,1.858168,-1.660787,3.790993,7.628017,0.509099,9.093417,8.265400,1.426318,-8.385501,0.279134,-8.249357,8.005779,-0.361287,-4.358076,5.252260,2.991992,3.412422,-6.597874,-2.677581,-2.576688,9.429371,3.275246,4.832113,2.768963,-5.717071,-6.122009,-9.159252,5.938093,-7.260832,-6.230868,5.463512,1.392563,4.077999,4.992760,4.594197,0.759907,9.486147,1.748649,2.043070,6.540444,8.248540,-4.695260,2.113510,-0.834886,0.048793,7.247617,-7.917895,9.826509,-7.126118,-6.396109,3.389670,5.439365,-3.134076,6.146994,3.095936,0.194469,-5.090569,-6.806122,-0.436308,5.980060,2.990006,-0.985288,1.053199,7.934493,-7.699903,5.358636,5.597735,-1.791276,7.571690,7.192480,-3.704010,8.771724,-7.903500,-3.175441,6.990154,-1.256486,3.292760,-1.438187,-5.490712,-1.362282,9.156973,-3.431813,-6.905493,8.977919,-6.380258,-9.104214,1.281991,0.843817,9.881691,-9.505924,-5.097974,7.380096,7.149541,-7.875051,3.308248,-4.942371,1.214081,0.475103,-8.002185], dtype = "float32")#candidate|4044|(168,)|const|float32
call_4043 = relay.TupleGetItem(func_1077_call(relay.reshape(const_4044.astype('float32'), [168,])), 0)
call_4045 = relay.TupleGetItem(func_1079_call(relay.reshape(const_4044.astype('float32'), [168,])), 0)
output = relay.Tuple([call_4013,call_4043,const_4044,])
output2 = relay.Tuple([call_4014,call_4045,const_4044,])
func_4047 = relay.Function([], output)
mod['func_4047'] = func_4047
mod = relay.transform.InferType()(mod)
mutated_mod['func_4047'] = func_4047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4047_call = mutated_mod.get_global_var('func_4047')
call_4048 = func_4047_call()
output = call_4048
func_4049 = relay.Function([], output)
mutated_mod['func_4049'] = func_4049
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4087 = relay.const([[[10],[-7]],[[-1],[1]],[[1],[-9]],[[-8],[-2]],[[9],[1]],[[5],[-8]],[[5],[-9]],[[10],[3]],[[5],[-1]],[[9],[10]]], dtype = "uint8")#candidate|4087|(10, 2, 1)|const|uint8
var_4088 = relay.var("var_4088", dtype = "uint8", shape = (10, 2, 7))#candidate|4088|(10, 2, 7)|var|uint8
bop_4089 = relay.add(const_4087.astype('uint8'), var_4088.astype('uint8')) # shape=(10, 2, 7)
func_2564_call = mod.get_global_var('func_2564')
func_2566_call = mutated_mod.get_global_var('func_2566')
const_4093 = relay.const([[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False]], dtype = "bool")#candidate|4093|(168, 1)|const|bool
call_4092 = relay.TupleGetItem(func_2564_call(relay.reshape(const_4093.astype('bool'), [168,])), 2)
call_4094 = relay.TupleGetItem(func_2566_call(relay.reshape(const_4093.astype('bool'), [168,])), 2)
func_3124_call = mod.get_global_var('func_3124')
func_3127_call = mutated_mod.get_global_var('func_3127')
const_4097 = relay.const([[-6.617027,2.811331,-1.593304,4.804195],[2.202561,9.139323,-7.699824,-0.151910],[7.490884,2.462886,-2.563766,7.549151],[7.544460,-4.728254,8.407236,-9.905656],[-6.228481,-8.867638,-6.815315,-4.860881],[2.989072,-9.307065,-0.892355,-5.000826],[3.397243,-9.221005,9.282238,7.179037],[6.930037,-3.206305,-6.789459,-5.093751],[-3.433978,4.305695,-8.571173,3.609359],[-9.923402,1.505282,-9.152778,-9.634618],[-7.065140,6.163370,2.932580,-0.307845],[-6.780000,5.635686,1.905633,0.016809],[-9.677481,-2.156540,-2.609063,-6.770953],[8.405423,-9.025798,-5.961812,-8.481368],[6.575342,-3.682157,-0.089560,8.076415],[-8.268392,0.206738,-5.612019,8.965763],[5.369574,3.889965,1.850177,-7.834030],[-4.493306,-8.391053,-4.318857,3.566082],[-3.087039,-1.290458,-9.708942,7.147184],[-7.109903,4.436325,8.443802,1.487465],[-8.103481,5.687089,-6.702454,0.032098],[-4.080694,8.970133,-0.939237,-8.371062],[4.542050,6.114286,6.580624,-8.057485],[9.090866,-5.241236,-7.526379,4.719272],[8.757804,4.887652,0.954784,-5.577632],[-6.444085,-5.862752,-7.046399,-6.491059],[2.311462,2.394436,-5.701374,-8.521147],[4.069708,6.002584,-5.339578,0.190605],[0.654761,1.254406,8.598893,-6.102172],[-3.554989,-8.810869,2.364207,-0.911396],[-7.461828,0.195920,1.490106,-7.682490],[6.160814,-7.580992,-6.953343,2.406900],[-1.343940,-1.417449,-6.938619,-0.212270],[7.780615,4.275863,5.654703,0.502793],[4.394765,-1.142872,-5.303643,-2.629472],[-6.245624,8.033140,-2.118565,-1.309168],[-5.770695,-2.077742,4.272151,1.763198],[2.951003,-1.542436,-5.739781,-8.162799],[-3.381503,-5.568153,3.882143,-8.132512],[2.671970,-0.038239,-7.577597,2.908767],[-0.337738,8.308468,-4.465846,-6.410206],[9.980968,-4.739525,0.317165,-8.808928],[2.870467,-0.736109,4.951582,7.930786],[3.604717,-0.400218,-0.913112,-2.422406],[6.355238,1.446959,-5.142076,8.369024],[-8.430907,0.117658,-1.444234,7.218034],[-4.327551,-2.903705,2.531741,-9.593270],[7.475608,-2.444099,-3.449434,-6.691068],[5.413345,5.866117,-7.330279,1.859030],[-4.983530,-0.697613,-8.738812,5.067349],[7.674868,-0.174086,6.988644,1.098831],[2.469690,-4.712013,-2.790447,8.619240],[-5.238415,7.476372,7.442906,1.625684],[7.082138,-6.407526,-3.144994,-4.574669],[9.105372,-4.455462,-4.990889,-2.520665],[7.794262,6.862586,9.474707,3.680118],[-2.164292,-8.944672,-2.712802,9.180054],[3.508893,1.308819,7.524338,-9.886721],[0.530048,7.433050,-6.618461,4.142074],[0.050654,-7.008642,-4.736543,-3.192451],[-3.269535,-8.312694,1.756234,7.524334],[-0.877564,-1.825872,-4.025351,-7.201625],[9.870545,2.203281,9.174565,7.660404],[-2.778168,-0.479283,-5.740242,4.458422],[9.224516,1.704533,3.960492,-6.471811],[0.544844,-8.119976,1.046403,3.971089],[-8.513135,-7.722651,-3.709408,-6.889963],[9.584195,3.055864,-8.466294,2.578867],[-8.885306,-8.474383,6.668272,5.525234],[1.964489,-7.268516,9.699530,2.606756],[9.279906,8.502198,2.225413,-9.806993],[-5.808455,-9.650679,-0.917382,7.184364]], dtype = "float64")#candidate|4097|(72, 4)|const|float64
call_4096 = relay.TupleGetItem(func_3124_call(relay.reshape(const_4097.astype('float64'), [3, 6, 16])), 1)
call_4098 = relay.TupleGetItem(func_3127_call(relay.reshape(const_4097.astype('float64'), [3, 6, 16])), 1)
func_3124_call = mod.get_global_var('func_3124')
func_3127_call = mutated_mod.get_global_var('func_3127')
call_4113 = relay.TupleGetItem(func_3124_call(relay.reshape(const_4097.astype('float64'), [3, 6, 16])), 1)
call_4114 = relay.TupleGetItem(func_3127_call(relay.reshape(const_4097.astype('float64'), [3, 6, 16])), 1)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
call_4117 = relay.TupleGetItem(func_980_call(), 1)
call_4118 = relay.TupleGetItem(func_982_call(), 1)
func_3601_call = mod.get_global_var('func_3601')
func_3603_call = mutated_mod.get_global_var('func_3603')
const_4122 = relay.const([[-6.549792,7.853261,2.579598,2.283922,9.264352,-1.498412,0.069789],[7.093522,-1.140208,-2.170366,-7.683682,-5.941556,-9.501299,0.788258],[5.156251,2.231958,8.314011,-3.407036,-7.139801,-4.677464,9.878609],[4.424886,-2.606947,4.811123,1.054302,6.873316,8.873182,-5.579285],[9.237223,5.594425,8.275079,-3.022878,5.616994,1.236459,1.260275],[7.691068,-5.437864,0.855810,6.574545,8.165390,-6.401742,-4.315447],[-4.162563,9.360828,-6.384694,6.141881,5.034429,3.987472,-0.067570],[-3.394246,-3.371992,-9.985852,8.435997,0.604597,7.256159,4.076909],[-2.083468,2.539782,-2.541011,-4.461414,8.848782,-8.508274,-6.520854],[9.885519,-1.700975,-0.746040,-1.922604,5.175362,-6.733800,-6.369002],[0.247184,8.756787,-1.896157,2.255322,4.448595,8.344162,0.859324],[9.845048,6.349756,-2.158548,-7.677902,-3.895287,-7.020611,-4.051551],[5.265119,-2.366885,-7.454969,-4.279222,-8.365704,-6.796956,9.841470],[7.440661,4.563841,-0.804647,7.482676,1.284201,6.995645,-9.253148],[2.050676,-2.100842,-1.018526,-8.900300,-1.347195,0.647734,-0.747262],[-5.531324,5.261119,-7.960747,-3.777408,-6.857490,6.933990,-6.262538],[6.376520,-9.285111,8.948077,1.695457,6.037832,5.012562,-0.702152],[9.836326,-1.275801,3.123303,8.203293,-4.717541,-7.418369,7.035290],[-6.667188,7.727343,0.763289,5.262581,-7.348604,-1.833572,-2.353915],[-0.820705,-8.206508,9.875047,4.573828,-9.041724,-9.253861,8.487684],[4.006431,-8.516668,-9.259087,-0.574929,-3.818941,-8.815609,-1.360815],[-6.489867,-4.329341,-9.541987,-8.841975,1.313048,-8.294231,-0.186112],[7.910860,2.463977,1.065247,-1.903398,9.469276,7.911547,-2.631939],[5.949796,-4.662622,2.104484,-7.484568,9.846843,7.811774,-5.550628],[-5.866391,-1.434821,-2.264440,2.414400,-4.336251,9.103636,-0.956410],[6.176984,9.062205,3.791589,-9.173480,-9.107846,-2.437509,-9.550076],[6.552200,1.877670,7.204059,7.297116,-4.966906,3.279931,-6.189521],[-5.727743,7.870799,-0.045664,-1.440694,-6.056332,-7.199987,1.996575],[-9.934860,5.827235,3.573460,-8.751548,-3.517922,-2.482445,-2.882632],[1.857165,9.801003,1.007722,8.865112,1.106386,9.394728,2.310787],[-5.357846,5.343276,-4.804601,-2.510242,2.669097,-1.468100,-5.819650],[-9.980043,6.473327,-8.783914,-7.384835,2.744709,4.050191,3.241564],[7.454511,-9.513480,-7.253381,-0.122066,-4.816136,-5.656362,8.218554],[-2.142521,1.708994,-7.291852,-9.815088,1.049507,-4.805295,4.252863],[0.813463,4.225603,6.209603,0.034553,8.990981,-7.347295,-9.882475],[0.344798,3.265954,-8.012983,6.136486,3.773941,6.821825,-7.308529],[-2.066142,6.287616,-5.038112,-1.904383,-5.605379,2.002196,5.256457],[-4.042836,-0.851317,-2.413439,3.247983,6.623740,6.893491,-0.655606],[7.910269,6.664881,-7.057087,-8.790649,7.680881,-4.893911,-1.143888],[1.624863,7.937127,1.019387,7.314286,-3.782375,-9.540666,2.470596],[-3.372675,-1.099256,-5.062670,4.391971,-6.049527,-6.655564,-9.810146],[-8.821164,-3.169117,8.119091,9.020716,-5.902309,-0.165737,0.828398],[-4.786329,-8.049665,-0.390349,-8.168568,-9.749998,-5.213450,6.799896],[-8.236824,2.193390,-4.122386,-6.819395,-7.800814,0.904457,0.810010],[1.807141,-2.388594,5.420432,-6.571851,-8.536907,9.204291,8.966172],[8.816349,-0.036501,-8.380591,-0.193020,9.772844,-6.290031,-1.673904],[-3.819249,0.618251,-7.548420,6.278835,4.081078,-6.607728,1.828446],[-9.280975,9.140896,8.165539,-5.300474,1.544319,5.303011,5.981351],[-2.854348,3.296817,5.908425,-6.221695,-6.749079,-3.144737,-3.349170],[4.089511,-4.746291,-0.589286,-0.179530,0.150142,9.967561,8.188269],[0.386266,9.359870,7.443935,9.757565,7.120444,-0.383971,3.887044],[7.440991,3.384313,1.450979,9.185178,1.334422,-1.188544,-0.505111],[-0.071337,-8.229269,-1.608779,7.988734,-6.151921,5.592725,4.007013],[9.048396,-5.495811,-4.108580,-6.984297,0.898913,8.374205,4.113550],[6.312251,4.565335,7.182866,8.274823,3.704600,1.908126,0.151235],[-7.216584,6.908376,-5.843750,-6.874591,8.466180,-7.658610,-9.360654],[-3.871067,4.730850,1.603224,8.116257,-0.148253,9.377746,1.239646],[0.868902,7.327116,3.640791,-0.227097,-1.376295,-5.740830,1.531612],[-5.951763,-9.751487,3.530897,-8.846079,3.940866,6.244746,-3.467739],[3.895113,-3.533334,4.679814,-3.017285,-3.649002,-4.747572,-4.000761],[-8.534511,1.222321,6.644326,2.631873,-8.405805,-5.451392,7.777294],[3.498530,-4.997182,-1.427119,-2.374900,-8.829992,-7.282897,0.159710],[0.324813,-9.268266,0.477975,-0.974211,0.943209,2.741781,3.859463],[8.037188,6.505579,-6.043478,-3.780974,-8.210152,-5.971466,8.649620],[9.928239,5.833213,-4.741140,9.187803,-6.811583,7.578572,9.795747]], dtype = "float32")#candidate|4122|(65, 7)|const|float32
call_4121 = func_3601_call(relay.reshape(const_4122.astype('float32'), [5, 13, 7]))
call_4123 = func_3601_call(relay.reshape(const_4122.astype('float32'), [5, 13, 7]))
bop_4127 = relay.right_shift(const_4093.astype('uint64'), relay.reshape(call_4117.astype('uint64'), relay.shape_of(const_4093))) # shape=(168, 1)
bop_4130 = relay.right_shift(const_4093.astype('uint64'), relay.reshape(call_4118.astype('uint64'), relay.shape_of(const_4093))) # shape=(168, 1)
output = relay.Tuple([bop_4089,call_4092,call_4096,const_4097,call_4113,call_4121,const_4122,bop_4127,])
output2 = relay.Tuple([bop_4089,call_4094,call_4098,const_4097,call_4114,call_4123,const_4122,bop_4130,])
func_4143 = relay.Function([var_4088,], output)
mod['func_4143'] = func_4143
mod = relay.transform.InferType()(mod)
var_4144 = relay.var("var_4144", dtype = "uint8", shape = (10, 2, 7))#candidate|4144|(10, 2, 7)|var|uint8
output = func_4143(var_4144)
func_4145 = relay.Function([var_4144], output)
mutated_mod['func_4145'] = func_4145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_4156 = relay.TupleGetItem(func_2010_call(), 2)
call_4157 = relay.TupleGetItem(func_2011_call(), 2)
output = call_4156
output2 = call_4157
func_4162 = relay.Function([], output)
mod['func_4162'] = func_4162
mod = relay.transform.InferType()(mod)
mutated_mod['func_4162'] = func_4162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mutated_mod.get_global_var('func_4162')
call_4163 = func_4162_call()
output = call_4163
func_4164 = relay.Function([], output)
mutated_mod['func_4164'] = func_4164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
call_4198 = relay.TupleGetItem(func_980_call(), 2)
call_4199 = relay.TupleGetItem(func_982_call(), 2)
output = relay.Tuple([call_4198,])
output2 = relay.Tuple([call_4199,])
func_4214 = relay.Function([], output)
mod['func_4214'] = func_4214
mod = relay.transform.InferType()(mod)
output = func_4214()
func_4215 = relay.Function([], output)
mutated_mod['func_4215'] = func_4215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3662_call = mod.get_global_var('func_3662')
func_3663_call = mutated_mod.get_global_var('func_3663')
call_4275 = relay.TupleGetItem(func_3662_call(), 0)
call_4276 = relay.TupleGetItem(func_3663_call(), 0)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_4296 = relay.TupleGetItem(func_603_call(), 3)
call_4297 = relay.TupleGetItem(func_605_call(), 3)
output = relay.Tuple([call_4275,call_4296,])
output2 = relay.Tuple([call_4276,call_4297,])
func_4320 = relay.Function([], output)
mod['func_4320'] = func_4320
mod = relay.transform.InferType()(mod)
mutated_mod['func_4320'] = func_4320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4320_call = mutated_mod.get_global_var('func_4320')
call_4321 = func_4320_call()
output = call_4321
func_4322 = relay.Function([], output)
mutated_mod['func_4322'] = func_4322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2855_call = mod.get_global_var('func_2855')
func_2857_call = mutated_mod.get_global_var('func_2857')
call_4335 = relay.TupleGetItem(func_2855_call(), 0)
call_4336 = relay.TupleGetItem(func_2857_call(), 0)
output = relay.Tuple([call_4335,])
output2 = relay.Tuple([call_4336,])
func_4345 = relay.Function([], output)
mod['func_4345'] = func_4345
mod = relay.transform.InferType()(mod)
mutated_mod['func_4345'] = func_4345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4345_call = mutated_mod.get_global_var('func_4345')
call_4346 = func_4345_call()
output = call_4346
func_4347 = relay.Function([], output)
mutated_mod['func_4347'] = func_4347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2668_call = mod.get_global_var('func_2668')
func_2669_call = mutated_mod.get_global_var('func_2669')
call_4350 = func_2668_call()
call_4351 = func_2668_call()
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_4361 = relay.TupleGetItem(func_1270_call(), 0)
call_4362 = relay.TupleGetItem(func_1272_call(), 0)
const_4375 = relay.const([[[True,False,False,False,True,True],[True,True,True,False,True,True],[True,True,True,False,True,True],[False,True,True,True,False,False]],[[False,False,False,True,True,False],[True,True,True,True,True,False],[False,False,True,True,False,False],[False,False,True,False,False,False]],[[True,False,True,True,True,False],[True,False,False,True,True,False],[True,False,True,False,True,False],[True,False,True,False,True,True]],[[True,False,True,False,False,True],[True,True,False,False,False,True],[False,True,True,True,False,False],[True,False,False,False,False,False]],[[False,True,False,True,False,True],[True,True,True,False,True,True],[False,False,True,False,True,True],[True,True,True,True,False,True]],[[True,True,True,False,True,False],[False,False,True,False,True,True],[True,False,False,True,True,False],[False,True,False,True,True,True]],[[True,False,True,False,True,True],[True,True,True,True,True,False],[True,True,False,False,True,False],[False,False,False,False,True,True]],[[False,False,False,True,True,True],[False,False,False,True,False,True],[True,False,False,False,True,True],[False,False,False,True,False,True]],[[True,False,False,True,True,True],[True,True,True,True,False,True],[True,True,True,True,False,False],[False,True,False,True,True,True]]], dtype = "bool")#candidate|4375|(9, 4, 6)|const|bool
bop_4376 = relay.greater(call_4361.astype('bool'), relay.reshape(const_4375.astype('bool'), relay.shape_of(call_4361))) # shape=(9, 4, 6)
bop_4379 = relay.greater(call_4362.astype('bool'), relay.reshape(const_4375.astype('bool'), relay.shape_of(call_4362))) # shape=(9, 4, 6)
output = relay.Tuple([call_4350,bop_4376,])
output2 = relay.Tuple([call_4351,bop_4379,])
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
func_2485_call = mod.get_global_var('func_2485')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_4434 = relay.TupleGetItem(func_2485_call(), 0)
call_4435 = relay.TupleGetItem(func_2487_call(), 0)
func_3124_call = mod.get_global_var('func_3124')
func_3127_call = mutated_mod.get_global_var('func_3127')
var_4463 = relay.var("var_4463", dtype = "float64", shape = (288,))#candidate|4463|(288,)|var|float64
call_4462 = relay.TupleGetItem(func_3124_call(relay.reshape(var_4463.astype('float64'), [3, 6, 16])), 1)
call_4464 = relay.TupleGetItem(func_3127_call(relay.reshape(var_4463.astype('float64'), [3, 6, 16])), 1)
func_3343_call = mod.get_global_var('func_3343')
func_3344_call = mutated_mod.get_global_var('func_3344')
call_4481 = relay.TupleGetItem(func_3343_call(), 0)
call_4482 = relay.TupleGetItem(func_3344_call(), 0)
func_1388_call = mod.get_global_var('func_1388')
func_1389_call = mutated_mod.get_global_var('func_1389')
call_4487 = relay.TupleGetItem(func_1388_call(), 0)
call_4488 = relay.TupleGetItem(func_1389_call(), 0)
func_1908_call = mod.get_global_var('func_1908')
func_1911_call = mutated_mod.get_global_var('func_1911')
call_4498 = relay.TupleGetItem(func_1908_call(relay.reshape(call_4481.astype('float64'), [9, 4, 6])), 1)
call_4499 = relay.TupleGetItem(func_1911_call(relay.reshape(call_4481.astype('float64'), [9, 4, 6])), 1)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_4520 = func_39_call()
call_4521 = func_39_call()
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_4527 = relay.TupleGetItem(func_603_call(), 3)
call_4528 = relay.TupleGetItem(func_605_call(), 3)
output = relay.Tuple([call_4434,call_4462,var_4463,call_4481,call_4487,call_4498,call_4520,call_4527,])
output2 = relay.Tuple([call_4435,call_4464,var_4463,call_4482,call_4488,call_4499,call_4521,call_4528,])
func_4548 = relay.Function([var_4463,], output)
mod['func_4548'] = func_4548
mod = relay.transform.InferType()(mod)
var_4549 = relay.var("var_4549", dtype = "float64", shape = (288,))#candidate|4549|(288,)|var|float64
output = func_4548(var_4549)
func_4550 = relay.Function([var_4549], output)
mutated_mod['func_4550'] = func_4550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2547_call = mod.get_global_var('func_2547')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_4560 = relay.TupleGetItem(func_2547_call(), 2)
call_4561 = relay.TupleGetItem(func_2549_call(), 2)
func_2264_call = mod.get_global_var('func_2264')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_4562 = func_2264_call()
call_4563 = func_2264_call()
func_3268_call = mod.get_global_var('func_3268')
func_3273_call = mutated_mod.get_global_var('func_3273')
var_4572 = relay.var("var_4572", dtype = "float32", shape = (56,))#candidate|4572|(56,)|var|float32
var_4573 = relay.var("var_4573", dtype = "float32", shape = (280,))#candidate|4573|(280,)|var|float32
call_4571 = relay.TupleGetItem(func_3268_call(relay.reshape(var_4572.astype('float32'), [8, 7, 1]), relay.reshape(var_4573.astype('float32'), [8, 7, 5]), relay.reshape(call_4560.astype('bool'), [216,]), ), 0)
call_4574 = relay.TupleGetItem(func_3273_call(relay.reshape(var_4572.astype('float32'), [8, 7, 1]), relay.reshape(var_4573.astype('float32'), [8, 7, 5]), relay.reshape(call_4560.astype('bool'), [216,]), ), 0)
func_1763_call = mod.get_global_var('func_1763')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_4582 = func_1763_call()
call_4583 = func_1763_call()
output = relay.Tuple([call_4560,call_4562,call_4571,var_4572,var_4573,call_4582,])
output2 = relay.Tuple([call_4561,call_4563,call_4574,var_4572,var_4573,call_4583,])
func_4586 = relay.Function([var_4572,var_4573,], output)
mod['func_4586'] = func_4586
mod = relay.transform.InferType()(mod)
var_4587 = relay.var("var_4587", dtype = "float32", shape = (56,))#candidate|4587|(56,)|var|float32
var_4588 = relay.var("var_4588", dtype = "float32", shape = (280,))#candidate|4588|(280,)|var|float32
output = func_4586(var_4587,var_4588,)
func_4589 = relay.Function([var_4587,var_4588,], output)
mutated_mod['func_4589'] = func_4589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_4601 = func_4162_call()
call_4602 = func_4162_call()
output = relay.Tuple([call_4601,])
output2 = relay.Tuple([call_4602,])
func_4619 = relay.Function([], output)
mod['func_4619'] = func_4619
mod = relay.transform.InferType()(mod)
mutated_mod['func_4619'] = func_4619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4619_call = mutated_mod.get_global_var('func_4619')
call_4620 = func_4619_call()
output = call_4620
func_4621 = relay.Function([], output)
mutated_mod['func_4621'] = func_4621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_427_call = mod.get_global_var('func_427')
func_428_call = mutated_mod.get_global_var('func_428')
call_4679 = func_427_call()
call_4680 = func_427_call()
output = relay.Tuple([call_4679,])
output2 = relay.Tuple([call_4680,])
func_4682 = relay.Function([], output)
mod['func_4682'] = func_4682
mod = relay.transform.InferType()(mod)
output = func_4682()
func_4683 = relay.Function([], output)
mutated_mod['func_4683'] = func_4683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1743_call = mod.get_global_var('func_1743')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_4702 = relay.TupleGetItem(func_1743_call(), 2)
call_4703 = relay.TupleGetItem(func_1745_call(), 2)
func_723_call = mod.get_global_var('func_723')
func_724_call = mutated_mod.get_global_var('func_724')
call_4706 = relay.TupleGetItem(func_723_call(), 0)
call_4707 = relay.TupleGetItem(func_724_call(), 0)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_4708 = func_39_call()
call_4709 = func_39_call()
output = relay.Tuple([call_4702,call_4706,call_4708,])
output2 = relay.Tuple([call_4703,call_4707,call_4709,])
func_4713 = relay.Function([], output)
mod['func_4713'] = func_4713
mod = relay.transform.InferType()(mod)
mutated_mod['func_4713'] = func_4713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4713_call = mutated_mod.get_global_var('func_4713')
call_4714 = func_4713_call()
output = call_4714
func_4715 = relay.Function([], output)
mutated_mod['func_4715'] = func_4715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_4716 = relay.TupleGetItem(func_2010_call(), 2)
call_4717 = relay.TupleGetItem(func_2011_call(), 2)
func_2306_call = mod.get_global_var('func_2306')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_4720 = relay.TupleGetItem(func_2306_call(relay.reshape(call_4716.astype('bool'), [1, 168])), 3)
call_4721 = relay.TupleGetItem(func_2309_call(relay.reshape(call_4716.astype('bool'), [1, 168])), 3)
bop_4722 = relay.logical_xor(call_4716.astype('int64'), relay.reshape(call_4720.astype('int64'), relay.shape_of(call_4716))) # shape=(6, 28)
bop_4725 = relay.logical_xor(call_4717.astype('int64'), relay.reshape(call_4721.astype('int64'), relay.shape_of(call_4717))) # shape=(6, 28)
output = relay.Tuple([bop_4722,])
output2 = relay.Tuple([bop_4725,])
func_4730 = relay.Function([], output)
mod['func_4730'] = func_4730
mod = relay.transform.InferType()(mod)
mutated_mod['func_4730'] = func_4730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4730_call = mutated_mod.get_global_var('func_4730')
call_4731 = func_4730_call()
output = call_4731
func_4732 = relay.Function([], output)
mutated_mod['func_4732'] = func_4732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3304_call = mod.get_global_var('func_3304')
func_3305_call = mutated_mod.get_global_var('func_3305')
call_4752 = func_3304_call()
call_4753 = func_3304_call()
func_1626_call = mod.get_global_var('func_1626')
func_1628_call = mutated_mod.get_global_var('func_1628')
const_4759 = relay.const([True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,True,False], dtype = "bool")#candidate|4759|(216,)|const|bool
call_4758 = relay.TupleGetItem(func_1626_call(relay.reshape(const_4759.astype('bool'), [216,])), 0)
call_4760 = relay.TupleGetItem(func_1628_call(relay.reshape(const_4759.astype('bool'), [216,])), 0)
func_1435_call = mod.get_global_var('func_1435')
func_1437_call = mutated_mod.get_global_var('func_1437')
const_4792 = relay.const([[-2.049688],[6.160612],[5.454303],[-5.809251],[-8.814885],[-8.282190],[-5.755220],[2.148375],[4.790367],[-7.231465],[-2.944681],[-9.629519],[1.007066],[-5.637390],[6.154521],[-4.642949],[2.465770],[-0.825197],[-1.181148],[-6.953046],[3.670283],[7.250219],[0.689246],[9.688863],[5.614893],[3.210648],[0.603400],[8.895261],[1.794285],[2.710339],[-8.806096],[-3.043266],[4.094713],[-1.894761],[8.876233],[-3.723716],[1.560770],[2.409983],[-4.879970],[-0.637103],[-6.817615],[1.214649],[3.392176],[-0.407529],[-9.785865],[9.017318],[3.907039],[4.054101],[-9.897680],[9.204658],[-2.120844],[-4.661754],[9.151787],[-5.160496],[-2.970954],[-2.760939],[-6.705919],[5.023308],[-8.036631],[0.543844],[7.959154],[0.591559],[-0.856621],[2.017499],[-1.599809],[8.311532],[-8.042370],[-3.971823],[7.635984],[-6.055755],[9.493112],[-1.157690],[-1.964107],[3.998722],[-9.753057],[-1.301419],[9.072847],[-6.355543],[-6.452220],[-2.667558],[-9.981321],[4.591751],[-4.741552],[8.706985],[-3.819545],[9.299506],[-9.721290],[-1.024540],[0.053792],[7.394561],[-9.789393],[9.027721],[3.946652],[1.107724],[2.607816],[-3.556183],[2.565462],[3.820101],[8.707973],[2.720636],[-8.981086],[-8.633510],[4.710484],[8.508160],[-9.657648],[-9.534859],[-3.870250],[0.984562],[9.015847],[7.746208],[-8.775368],[6.655565],[4.892900],[5.129313],[0.304502],[5.614414],[-2.506125],[-7.969877],[-9.290187],[-7.621270],[-9.321766],[9.672628],[2.812054],[-6.034962],[6.655320],[4.120922],[1.858958],[-9.302443],[0.515113],[1.520355],[-1.885888],[-5.584925],[-5.523469],[-6.670506],[7.056326],[-8.366822],[7.797581],[-3.692053],[-5.687823],[-2.818617],[9.079504],[4.616838],[-5.749899],[4.599560],[-9.168525],[-6.931244],[2.882660],[7.020695],[0.940656],[-6.331743],[-4.756725],[-5.406591],[-0.048831],[-3.961272],[7.222277],[3.742416],[9.864331],[9.572646],[-8.203766],[7.472484],[4.143168],[7.597128],[7.460079],[7.409217],[2.692715],[9.027863],[-5.099801],[1.021893],[-3.889190],[8.421723],[-5.290832],[-4.782055],[8.544142],[4.748536],[8.344907],[-8.047133],[-8.358184],[0.516963],[-3.131686],[-2.136270],[4.811688],[-2.616326],[4.193340],[-0.604255],[6.550848],[7.113351],[-0.287116],[2.873430],[3.908609],[3.056550],[-5.278936],[-6.958529],[-2.694990],[-1.943691],[-8.990307],[-6.289673],[-9.139594],[6.500575],[-1.897305],[1.647459],[3.780574],[-7.982600],[7.765069],[0.839663],[-5.210902],[8.068200],[2.454689],[-8.432439],[0.811267],[-0.761682],[0.181905],[9.320593],[6.276415],[-5.937956],[7.369251],[-3.555340],[-5.875096],[-1.397805],[-3.598734],[7.664690],[3.860036],[2.336689],[-6.440931],[-4.361238],[-1.909340],[2.781658],[2.790484],[1.169865],[3.932877],[-7.990479],[-7.471971],[8.405048],[9.859477],[-0.479289],[5.189684],[5.226413],[-7.067576],[4.264815],[-3.220965],[-2.239856],[0.250724],[-6.794282],[6.387309],[2.101698],[5.879072],[1.481180],[-5.488272],[2.911981],[-5.479428],[-0.719323],[2.207644],[-8.707840],[-8.230112],[-6.943933],[9.210902],[-9.633435],[-4.011031],[6.593561],[-8.788711],[-6.435104],[2.026958],[7.313304],[-6.081119],[8.207396],[-8.152953],[-4.371744],[6.540063],[3.958061],[7.545725],[-7.376781],[5.111608],[1.704671],[-9.826025],[2.873374],[4.326080],[-0.265093],[0.970485],[9.801784],[-4.188064],[-3.495114],[-7.623204],[-4.609638],[-4.356817],[9.476135],[7.776059],[-3.327637],[-1.894634],[-8.512309],[6.572013],[-5.058690],[5.049283],[6.751603],[-1.279492],[-2.400029],[5.478431],[-1.414425],[-4.666871],[-9.050650],[-1.108208],[-9.751454],[5.826463],[-9.381672],[-8.716902],[-4.220984],[-3.463885],[-8.468945],[-6.719630],[-6.510479],[-1.451566],[9.403036],[-2.315842],[9.927212],[5.117520],[9.206889],[-6.975165],[2.107722],[-0.214304],[6.449294],[0.876172],[-8.949569],[-9.884513],[1.122193],[-8.559493],[-0.161026],[9.552026],[8.388305],[7.394236],[-9.120186],[-6.526409],[-3.425043],[5.883818],[-3.968235],[-3.480003],[-9.877227],[-6.965144],[4.706039],[3.999445],[0.403298],[4.722271],[5.805962],[1.783098],[-0.771771],[3.415151],[3.695510],[-8.145591],[-3.317388],[-3.754636],[7.587422],[3.285813],[-6.747258],[6.373862],[-7.154488],[-0.119330],[-2.841035],[3.789407],[-5.690316],[-5.064122],[2.032030],[0.666153],[6.365128],[6.422538],[3.955081],[6.438299],[-3.199973],[-6.578882],[-8.007908],[-4.644207],[9.996192],[-8.535413],[-4.737200],[4.172294],[-8.929199],[7.899593],[8.262096],[9.815975],[-6.115474],[9.216354],[-3.046540],[8.610430],[1.901029],[5.999026],[6.467205],[-5.595295],[-6.894281],[-4.640072],[1.003016],[-7.574487],[-7.283869],[0.027848],[-7.220681],[-9.992059],[9.503102],[3.734110],[-6.906146],[-3.718983],[-5.038758],[4.341413],[-6.586786],[-9.642171],[-2.104975],[0.074460],[-6.378473],[-5.258131],[-9.410536],[7.927145],[-3.630666],[8.272360],[9.217189],[6.889211],[9.171054],[0.759014],[3.380681],[3.423042],[-8.478800],[-2.220791],[0.490752],[-3.078576],[7.304689],[-9.408613],[6.136926],[6.369533],[5.705530],[0.323834],[1.917116],[7.708664],[6.923402],[-7.818259],[5.792713],[-0.056317],[-3.514727],[6.168638],[-7.558056],[5.664646],[-7.985431],[9.553696],[2.285996],[3.609242],[-7.151043],[2.909549],[4.113069],[-6.586282],[0.270027],[7.619112],[9.639892],[7.968827],[-8.194781],[2.159735],[-9.560091],[9.535142],[-2.809924],[-5.426809],[1.944559],[-3.336010],[0.321409],[4.645689],[-5.314656],[9.607599],[-5.840446],[2.451169],[-6.766609],[6.996004],[5.712592],[8.197579],[-2.304796],[-5.277460],[-9.511752],[-9.310702],[-8.750340],[9.560412],[5.671923],[-8.561827],[-5.416314],[1.798152],[-8.994159],[-3.579006],[4.466749],[0.052000],[-4.624231],[1.816337],[8.827040],[7.748033],[-6.595971],[6.499543],[2.287667],[-5.354676],[3.271631],[-7.960971],[-5.835934],[7.689086],[-2.031142],[0.155034],[6.761572],[-7.140480],[-6.559152],[-7.828639],[6.492756],[5.202499],[-0.630574],[-5.779591],[7.260071],[-9.451107],[4.290502],[-3.787690],[-2.888422],[-8.241541],[-4.026353],[9.163952],[1.883483],[0.965444],[0.369474],[3.105898],[-8.830768],[-6.806233],[-9.596867],[-3.409987],[-8.648609],[-3.484170],[0.157545],[4.341704],[-1.506318],[1.742580],[-9.851471],[7.762409],[-7.787032],[1.356723],[-7.319136],[0.148450],[5.670558],[7.622251],[-4.601210],[5.410661],[-9.196233],[2.322224],[-3.739440],[-0.976675],[-7.608077],[2.034688],[-8.483517],[-3.387637],[-5.376491],[-6.739317],[5.299146],[7.687563],[3.961248],[-2.341906],[-7.113415],[-6.089422],[6.117494],[-6.983392],[2.679754],[8.626229],[-5.095998],[-5.051838],[9.644149],[-8.670457],[-1.284012],[-4.810155],[-5.933155],[-8.227495],[5.452561],[0.333067],[-7.321527],[-2.455633],[4.767133],[7.977804],[3.703361],[4.722540],[-2.335253],[-3.175445],[-6.780113],[9.756148],[5.440843],[-8.498206],[4.872899],[-2.218516],[4.927969],[-7.187224],[7.184300],[-3.294951],[1.343620],[6.214145],[-9.019212],[0.779869],[-0.448967],[-7.621634],[-2.565684],[1.712991],[9.096148],[3.461188],[-4.575346],[3.413310],[2.020043],[3.746165],[0.541563],[-0.934434],[-1.560249],[1.487699],[-5.271457],[7.344549],[9.658713],[5.614076],[1.252990],[2.852205],[8.760898],[3.920056],[-0.646438],[1.221126],[-5.198249],[4.477205],[-7.043410],[-7.598508],[0.203129],[0.715763],[-0.231065],[4.209729],[-1.767348],[9.535498],[7.825249],[2.213267],[3.412717],[7.209492],[6.035705],[-3.417260],[9.016575],[6.913052],[4.227794],[-3.062649],[-3.294525],[-9.960248],[-6.094490],[-7.963374],[-6.002655],[-9.194417],[-1.748782],[-2.572825],[-5.933805],[-7.298262],[5.009395],[2.316475],[-0.190809],[-6.420605],[0.950205],[-6.706407],[8.049335],[-7.437690],[-8.662883],[-9.650042],[8.379887],[1.329615],[-8.356392],[8.706600],[9.547575],[8.153595],[-6.985079],[7.916564],[1.740991],[-9.193192],[6.425107],[-2.818055],[4.451138],[-8.228744],[5.503525],[8.667702],[-9.550557],[1.555327],[-6.003791],[7.608945],[-5.707901],[-3.298420],[-1.909710],[6.267044],[-2.062660],[-4.980728],[-0.965507],[-2.522215],[3.271789],[-4.547237],[3.434673],[4.866378],[-3.703083],[1.399466],[-5.139595],[-1.534264],[7.160943],[8.799404],[-1.937407],[5.474537],[0.009992],[-1.449082],[4.401353],[8.269504],[-0.337906],[4.347730],[4.924864],[6.187775],[6.952414],[5.816142],[9.567553],[-0.999483],[-3.956161],[-7.763216],[-6.859852],[8.797554],[9.260376],[-4.505237],[-6.395678],[-3.302713],[5.537925],[5.855219],[-5.200000],[-0.499116],[5.437822],[4.664175],[4.017092],[6.947012],[-8.535883],[-6.313785],[2.091472],[-7.021416],[-1.781482],[1.130520],[-4.687267],[5.521182],[-9.514293],[6.779544],[6.649361],[-5.852151],[4.583564],[4.955020],[-7.731369],[-9.615241],[1.240146],[5.124152],[4.406134],[3.285025],[-2.806115],[-4.758918],[-6.034270],[-6.459311],[-4.806162],[-6.024628],[8.612308],[-6.636533],[-5.822913],[7.202300],[-0.738003],[8.115627],[5.097496],[3.795635],[-1.667859],[-4.172428],[0.412845],[-0.862374],[-2.322411],[-4.586943],[-4.073994],[-4.761200],[-4.971245],[-1.935638],[-8.429070],[2.117684],[9.611979],[-1.170640],[3.678710],[4.073059],[3.454447],[5.371024],[4.254348],[-6.041440],[-9.970958],[-0.610695],[8.754397],[1.905794],[-9.342225],[8.186151],[8.511414],[9.038327],[8.769787],[1.080596],[3.054326],[6.404740],[-7.507825],[-8.487258],[-7.520738],[7.969604],[7.165992],[0.273717],[-9.492241],[-8.117121],[-1.272526],[-7.497369],[-4.836717],[-0.082589],[0.047894],[0.934587],[2.235538],[4.862975],[1.261964],[8.220270],[7.153843],[-2.007024],[-4.080859],[8.843953],[-4.978275],[7.673602],[9.638332],[0.711870],[-6.457134],[-9.957279],[0.237153],[-9.420025],[-2.213578],[4.506176],[8.304837],[8.814342],[0.679135],[-3.766447],[5.365536],[9.608153],[5.841035],[-1.734604],[-1.308209],[3.028018],[6.798454],[-8.100541],[0.640512],[1.124630],[7.218080],[3.294297],[7.084687],[1.617492],[-2.597933],[5.916566],[1.931520],[-2.023366],[1.345396],[-3.031260],[-7.841896],[-7.421146],[1.519443],[-2.546553],[-6.769815],[-8.870382],[-0.082337],[-4.071303],[-5.639393],[9.256441],[0.615122],[-5.013081],[2.496831],[-0.623664],[3.386897],[-3.494792],[-3.901526],[9.282795],[9.260596],[-9.711676],[-4.539905],[8.261985],[-5.585172],[-5.306798],[1.774863],[1.026692],[-0.726594],[-7.619545],[-0.131838],[8.125156],[3.859509],[7.437038],[-0.194173],[2.623115],[2.881164],[9.309330],[-7.516264],[-4.542835],[2.809415],[6.262437],[-7.544544],[9.235933],[-9.387460],[-3.984440],[-6.726145],[-0.933687],[1.141990],[4.386233],[-8.959569],[-6.181673],[-6.639232],[6.473226],[-1.935056],[6.577020],[9.270755],[1.481458],[-2.108071],[-1.656534],[-5.056342],[8.754614],[-9.686850],[-7.385476],[-1.091752],[-9.302792],[-7.212489],[-6.711915],[-3.992097],[8.238128],[3.023619],[-1.112843],[8.487235],[8.437216],[3.527239],[-9.602117],[-2.626636],[-6.477904],[3.997612],[1.129694],[7.604511],[-6.514721],[-4.672515],[-2.096548],[2.180788],[3.508675],[1.094195],[6.106999],[5.379734],[-7.198405],[-2.663756],[-5.884811],[-3.977719],[-3.071901],[6.050472],[8.060468],[2.318618],[-8.426183],[-5.560897],[-1.413018],[-6.378302],[2.258901],[-7.180116],[-2.939015],[7.328732],[-1.903359],[4.421644],[-2.706157],[5.804643],[9.433859],[-6.020592],[0.290408],[9.799712],[2.562488],[4.289861],[7.850818],[-9.556928],[5.976572],[2.392683],[-3.307781],[-2.763762],[-9.929091],[-7.952630],[3.121372],[7.673474],[-0.323404],[-8.931451],[7.061401],[-5.091962],[5.629255],[4.816920],[5.519187],[4.269269],[-6.957672],[2.352829],[7.667124],[2.490300],[3.134110],[4.037345],[4.810238],[-1.075517],[-4.949769],[-5.333427],[-0.123950],[2.963267],[-2.310880],[-9.085872],[-2.752308],[-7.946382],[-3.729626],[9.813972],[9.380543],[4.161277],[-0.762436],[7.414273],[-2.622648],[-1.325498],[-3.569454],[-0.028414],[8.342418],[1.158156],[-7.865991],[8.953457],[8.919488],[5.311017],[3.181546],[-1.059646],[3.806576],[-9.228448],[-0.058417],[-2.687310],[6.311083],[4.748858],[3.014693],[-1.409437],[0.397223],[-9.696929],[7.519595],[-3.607168],[0.566363],[-1.982181],[4.112648],[5.088799],[-3.449226],[-1.574968],[7.534924],[8.676554],[5.751784],[3.649540],[1.900840],[4.136428],[1.522760],[-1.692634],[-9.019805],[0.538757],[7.790811],[-0.044868],[-6.541906],[0.565993],[7.203201],[2.281425],[-8.404150],[1.923154],[-6.542812],[-5.175944],[-1.034245],[-0.937302],[6.119514],[-6.678716],[-1.675376],[6.014509],[6.480108],[-5.260832],[8.828933],[3.193926],[2.321862],[-9.862781],[7.465285],[-9.248182],[-5.734906],[5.348092],[-6.820722],[-0.404815],[6.135368],[3.602434],[-5.981205],[5.224045],[1.160811],[-6.050690],[9.427523],[8.879616],[-3.595305],[4.820731],[-5.662021],[8.995248],[-6.772911],[3.934474],[2.274870],[8.433298],[1.731621],[-2.499757],[0.798374],[1.520513],[3.408789],[-9.841516]], dtype = "float64")#candidate|4792|(1080, 1)|const|float64
call_4791 = relay.TupleGetItem(func_1435_call(relay.reshape(const_4792.astype('float64'), [1080,])), 1)
call_4793 = relay.TupleGetItem(func_1437_call(relay.reshape(const_4792.astype('float64'), [1080,])), 1)
output = relay.Tuple([call_4752,call_4758,const_4759,call_4791,const_4792,])
output2 = relay.Tuple([call_4753,call_4760,const_4759,call_4793,const_4792,])
func_4796 = relay.Function([], output)
mod['func_4796'] = func_4796
mod = relay.transform.InferType()(mod)
output = func_4796()
func_4797 = relay.Function([], output)
mutated_mod['func_4797'] = func_4797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4730_call = mod.get_global_var('func_4730')
func_4732_call = mutated_mod.get_global_var('func_4732')
call_4800 = relay.TupleGetItem(func_4730_call(), 0)
call_4801 = relay.TupleGetItem(func_4732_call(), 0)
output = call_4800
output2 = call_4801
func_4805 = relay.Function([], output)
mod['func_4805'] = func_4805
mod = relay.transform.InferType()(mod)
output = func_4805()
func_4806 = relay.Function([], output)
mutated_mod['func_4806'] = func_4806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1763_call = mod.get_global_var('func_1763')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_4807 = func_1763_call()
call_4808 = func_1763_call()
output = call_4807
output2 = call_4808
func_4835 = relay.Function([], output)
mod['func_4835'] = func_4835
mod = relay.transform.InferType()(mod)
output = func_4835()
func_4836 = relay.Function([], output)
mutated_mod['func_4836'] = func_4836
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4840 = relay.var("var_4840", dtype = "int64", shape = (3, 1, 7))#candidate|4840|(3, 1, 7)|var|int64
var_4841 = relay.var("var_4841", dtype = "int64", shape = (3, 11, 7))#candidate|4841|(3, 11, 7)|var|int64
bop_4842 = relay.equal(var_4840.astype('bool'), var_4841.astype('bool')) # shape=(3, 11, 7)
func_3168_call = mod.get_global_var('func_3168')
func_3171_call = mutated_mod.get_global_var('func_3171')
const_4850 = relay.const([4.925623,-1.136432,2.062863,0.973148,8.336281,-2.654022,9.204829,1.453681,7.110136,-0.738794,-7.429906,-2.449892,-3.086040,-3.053445,-6.105079,7.771242,-5.183030,-6.809718,7.047870,-8.793863,-0.842642,-6.680519,9.752273,-4.415715,-4.519454,-6.461345,-2.095485,-2.404238,-4.111122,-4.964324,-2.351604,-1.659696,7.780266,-7.253826,9.251838,8.866705,0.173702,1.529277,9.689557,-3.780168,-3.354811,0.840390,9.940219,-9.361803,-7.369502,-3.617696,-9.404013,-6.053562,3.982654,5.501957,2.692717,-5.089710,-4.981267,2.775949,7.093507,6.675742,-7.500337,-1.105319,-0.656788,3.445400,1.795988,2.271213,6.637831,3.899373,-5.590981,1.200846,-0.190336,-9.289778,8.377427,-4.839831,1.628379,1.800912,-0.605205,8.818959,-0.742050,-8.039400,-1.896026,5.471410,4.482039,-1.704756,7.782786,3.527679,7.911878,-9.657650,-1.379977,0.074631,-3.023032,2.806236,-0.133956,4.930213,-2.329152,-5.219157,8.994558,-6.939846,8.170567,-3.711903,-7.741604,-0.942047,-9.749753,-4.803563,6.124579,-2.047732,-3.363797,2.909194,3.949267,7.912071,-8.429097,-8.459342,-8.692063,-2.531016,-7.184043,-7.354022,-6.419997,-2.625838,-7.179401,7.040655,0.049083,9.073189,-9.873056,-5.015279,-5.340089,4.239473,-1.972653,-0.026054,-8.190602,-8.543006,-7.757651,8.460371,6.473194,6.238875,-3.611524,4.762515,-1.198108,-9.354448,8.466564,-5.044409,-1.505615,-5.580371,-8.364777,9.585447,6.779636,0.076029,5.225541,6.838330,-6.353731,-2.250336,6.388206,-7.729433,-1.048502,-2.157735,-9.997849,2.281660,-5.761724,3.595438,7.835756,8.539044,-1.486519,-1.641108,2.143433,-0.564620,-5.538119,4.740166,-0.965588,8.809581,-1.899206,3.869916,4.686043,9.229463,-0.582239,-1.169004,-4.158634,9.400240,-7.861966,-8.876586,0.981603,8.232536,4.961231,6.533276,6.312280,-0.871964,0.749490,-3.234082,0.212486,-4.045001,-9.951758,1.254326,9.771003,1.132425,-0.413264,4.419471,-0.075635,1.857737,6.370510,4.387499,9.374699,-2.156098,1.996720,6.338868,0.456418,3.554331,-8.583497,-6.877616,3.137354,4.534834,3.611932,3.427312,-8.102024,4.244927,2.626731,-9.660319,-6.596047,3.860301,7.274030,-0.874312,6.221786,-6.804800,-5.741735,8.195124,-1.975191,6.115711,6.566302,9.238826,1.128796,-5.575617,8.474873,-6.465444,6.558147,-4.474774,-3.125385,1.743967,-2.611634,-5.765142,-8.510674,-2.275023,-3.331719,-5.330013,-2.701486,2.615357,-5.436489,-9.874250,-5.260946,-9.816603,7.751048,-2.337930,0.779216,1.610738,4.173278,7.374888,2.496690,-6.880187,6.543944,3.002207,-9.781279,-6.100847,-4.574281,3.399689,2.016404,4.794124,-7.324312,-3.431111,5.945872,5.585688,2.682923,5.617504,-0.072431,1.492705,-3.803682,6.054760,8.015972,-3.581946,-3.392342,6.888602,4.699448,-2.011845,-2.255075,3.439481,-8.040358,9.735439,6.462583,-9.630936,-4.188261,-0.478797,2.174528,-2.830993,7.324831,-2.012852,-3.745199,3.849022,-4.235127,2.413106,-2.920079,0.980349,9.546419,9.751706,0.621107,-1.289142,1.544854,-3.626445,-4.935464,2.861530,8.213673,9.774651,4.918035,9.617775,0.032313,8.044844,-2.742439,-6.479760,7.159002,-1.739574,-1.945492,-7.710681,2.375599,-1.418603,7.711557,5.546429,3.232745,-2.790639,6.745112,4.813444,-0.777036,6.072076,6.337030,-8.923738,9.185601,0.341964,7.910246,3.639381,-6.653977,-9.345775,2.793248,6.973917,7.473323,-5.506240,2.493549,2.423322,-9.275988,-3.719238,-6.054511,-8.853175,-6.396245,1.124417,4.620448,-2.490616,-1.381020,-5.765872,9.721972,7.009307,8.130657,8.218753,2.509672,5.994660,2.679797,7.188509,-9.875230,9.166602,6.375753,4.051664,9.261643,-4.506487,-9.965191,-5.580688,-2.691362,-5.538275,6.320014,2.434899,-9.987638,-0.230849,-9.192166,-9.642326,7.287960,6.396879,-5.871798,5.070000,8.856205,-2.598885,-8.682403,5.301160,-5.106661,0.321988,2.688114,-7.397755,2.653669,-6.279817,-0.267017,-3.440414,-5.715836,-2.697901,-1.522752,4.967227,0.383469,-1.794975,-9.828908,5.941359,9.942280,-3.767099,2.208894,5.369308,6.689373,-1.671569,-4.944593,8.321080,8.811309,2.327811,3.643736,6.823015,-5.052086,2.597711,6.737496,2.320491,9.126632,2.443724,-4.879245,7.096607,-1.469785,9.611976,-1.982194,-2.374854,-0.545367,-2.637402,-4.455155,1.670707,3.880826,2.465855,1.124447,4.669146,-6.608179,0.801633,8.374479,-5.715229,-2.477997,-9.336926,-9.507238,-5.241094,2.186015,-1.313310,-7.382096,-8.593698,-2.794243,-3.120508,5.622215,-8.001668,7.731181,-1.551262,-8.831257,-3.247276,0.876881,-1.020204,5.402873,-0.911836,7.608339,-3.395718,-8.298173,6.735142,-4.626066,-5.224876,1.375643,3.267809,-7.859309,-5.965277,-7.842380,-1.149913,8.398224,1.881092,9.739491,8.368063,7.093565,4.126692,2.782378,-7.221233,-8.488296,9.437126,-8.894605,-5.842491,-0.882268,1.578201,-0.417962,-3.688860,-0.978341,-7.940223,-6.746899,-3.281755,-2.265714,1.380747,-7.767965,3.031787,6.740515,1.908901,-7.280383,-0.615189,-3.183652,3.377637,5.295545,-9.428571,-3.676409,-9.905606,1.697553,-7.280616,-4.591199,8.373185,9.523093,0.083948,2.746006,-2.825827,0.516832,-7.342389,7.859116,-1.634879,-1.796551,-7.084479,4.137306,9.239057,-8.824520,-8.341539,0.562214,2.444612,7.842680,8.070836,5.388644,-5.019970,4.707983,-4.126434,-9.415520,2.867155,-3.321380,1.465513,-6.244464,-2.372164,-3.441442,3.983473,-8.395427,2.436567,-4.384245,-0.528817,-3.960648,-2.180865,3.682268,-5.364549,1.634768,-2.966045,-8.084169,5.917785,-2.870607,0.009548,0.510395,5.931906,9.639977,9.258761,5.068456,-7.642622,-8.511737,7.103674,7.044851,2.934195,-5.844691,-2.598771,-6.872731,4.029161,6.064879,7.807841,-1.839125,-2.227451,7.742880,0.417572,5.576602,6.320102,-3.283045,-7.937544,-5.935017,-9.191121,3.452338,2.386293,-3.856096,8.085739,3.329516,-0.351872,6.985310,-1.515450,-9.696487,3.405049,1.493411,9.001834,-5.956508,2.818067,-3.139217,1.680022,8.407636,5.860835,2.525492,6.122834,2.871761,-1.072186,5.178961,-6.399095,-9.136755,6.832232,-5.718646,1.216902,-7.924675,3.984413,-9.835548,6.460092,-0.341215,-5.366808,8.509942,-9.879770,1.427623,9.880461,1.575333,2.559579,6.393911,3.470112,3.274446,-4.252947,-2.096867,-4.680337,-0.496858,-3.512161,-1.658978,4.479975,-9.926467,0.638519,-3.286020,-0.116898,-4.581713,-1.602657,6.965851,5.489121,-4.373394,-0.304979,3.945723,-9.370395,-9.838021,-4.099148,8.111439,-5.716771,-5.827362,8.175821,-0.824626,-8.651031,0.472800,1.977324,7.101833,-9.938698,-2.556345,-5.756810,2.143822,-0.094618,3.161398,1.946431,-8.005314,-7.731777,4.326116,1.188880,-8.599447,-1.830247,-2.699828,-2.107733,-7.830397,-1.978467,5.195225,-1.697049,9.829316,1.390438,-8.721926,2.807637,-1.035031,9.764493,6.681924,-9.564946,-5.261411,-7.432241,-0.671146,-0.472962,1.723878,2.296900,2.899749,4.964568,-5.944512,6.889044,5.257829,6.547112,6.080331,7.224043,-2.361405,-6.785221,-3.871355,4.951902,5.521654,2.556433,-0.693836,2.200166,8.013253,-2.766435,7.207629,-9.069981,-3.384100,6.463716,-3.805785,7.759295,-5.106158,4.558185,-0.361103,5.462235,9.967205,-1.045264,7.967933,9.149763,-5.542395,2.524586,-2.204699,1.434131,1.626467,-2.005776,9.447567,-3.706569,4.005330,4.114084,1.858539,6.009281,1.742917,-2.037621,0.825241,0.607366,-4.598391,-4.955900,-6.477535,5.390648,-4.901618,9.054908,4.909059,5.515407,-8.112049,-5.147482,3.812624,-8.027299,6.563154,6.275603,-8.830278,7.786967,6.725328,4.045940,5.716276,-5.825782,-3.710041,0.343811,9.147868,-6.321455,5.725379,8.833512,-1.179371,-3.375235,8.338247,5.101384,-0.819013,-5.630418,-9.863977,-4.365167,-7.030004,8.008921,-5.019049,4.900273,1.607972,1.873759,-8.369857,9.157654,-0.478313,6.666357,6.070311,-1.173850,7.437793,-2.859401,-1.622870,6.254680,2.002387,-3.075234,8.297022,3.342505,3.930347,-5.720101], dtype = "float64")#candidate|4850|(780,)|const|float64
call_4849 = relay.TupleGetItem(func_3168_call(relay.reshape(const_4850.astype('float64'), [13, 4, 15])), 0)
call_4851 = relay.TupleGetItem(func_3171_call(relay.reshape(const_4850.astype('float64'), [13, 4, 15])), 0)
func_1435_call = mod.get_global_var('func_1435')
func_1437_call = mutated_mod.get_global_var('func_1437')
const_4859 = relay.const([-1.762346,0.099148,5.989687,-6.454000,-2.498022,7.020897,7.325540,4.713595,4.845157,0.364326,-1.059353,-5.045824,-2.492410,5.929057,-5.065941,2.166750,-9.598153,8.921608,-5.360731,5.560780,4.413566,3.893555,9.480581,3.705240,-4.562290,-6.671122,4.060262,1.069380,-2.017306,4.586076,3.766575,4.788825,1.235840,1.767251,-3.377517,-1.532001,-5.546640,0.045765,-6.349811,-9.983846,0.089064,8.595123,0.493639,-9.772946,8.619410,-3.554479,-7.340525,-5.523607,-2.668785,3.590506,-1.337964,4.682641,3.434541,7.181650,9.419264,-0.649622,-0.064459,1.520248,-4.329574,-0.239791,8.271865,5.010522,-8.896829,8.107523,6.207321,-0.362999,-4.749220,-0.319935,-9.828684,3.127596,-6.004858,-2.536206,5.610341,-5.956534,2.368349,9.470881,-2.782891,-1.728487,-6.421258,7.885020,-4.774615,-2.328408,7.999900,-2.477591,-1.662350,3.845488,1.703051,9.455993,7.760595,7.634111,-6.944357,9.838613,7.171930,-7.868907,3.308910,4.040859,3.163452,-8.887559,7.767076,-1.967812,-6.317278,-6.810040,1.274770,-4.723388,2.941752,2.930941,-6.900712,-3.949368,-5.767694,-5.816191,6.685627,1.114149,5.995642,7.471637,-5.664099,-3.126407,-3.606163,-0.453944,-9.735959,-1.888369,-4.477416,-7.078308,3.662098,-5.249329,4.436464,3.449554,1.481704,6.746574,7.863636,0.380049,-8.742939,-8.079897,-4.195021,-6.184232,-4.324934,-6.746773,-8.116139,5.413019,-9.649656,1.906421,-0.460913,-0.608778,3.372281,-8.942695,-8.645060,-6.519468,7.705249,7.310789,5.839336,2.037429,0.646171,4.989242,-0.586894,6.896358,-2.443761,-7.960908,4.904120,-8.691676,-9.168365,3.521085,-2.851301,1.886295,2.865641,7.363356,-8.848372,-7.801954,0.644763,1.447690,-5.401799,-6.480623,7.162385,-4.408407,9.763397,1.857009,5.589520,-7.806365,-1.046060,-8.218478,8.306526,-8.058569,-6.457197,6.685285,-6.324099,6.627197,1.864647,-4.535478,-7.245557,9.813851,6.487047,9.370594,-8.093336,5.445665,9.548973,-2.869746,0.297590,-4.701726,6.067323,1.965667,-4.813989,-4.993632,-1.657011,-8.420646,4.452269,-0.045162,-6.035237,-4.609760,-3.820434,6.949811,7.875551,-7.512474,-4.036075,-5.305866,-7.713737,-7.841472,-7.633661,-7.185855,9.373014,2.164402,-2.165828,7.101330,2.636403,8.264789,4.711631,1.964353,-5.254535,-8.339144,-0.883012,-1.878123,-1.878248,1.667180,-4.835807,-7.528480,-3.306315,-6.296380,3.120778,1.424236,5.044972,-0.310128,1.907955,0.206650,9.448023,-9.404298,-1.051716,-9.233226,6.606386,6.109708,9.705359,4.886257,7.592236,1.200640,-6.556223,4.556517,7.535304,-3.855685,5.487786,8.874901,2.713168,-6.195946,-0.618894,7.244589,-5.820187,6.374248,-7.543130,7.306073,9.749496,-0.592420,3.265765,2.017248,-4.263888,2.920067,-6.458291,-5.738410,8.615667,1.157832,-9.486578,0.504104,-7.424690,-3.944299,-0.586665,-5.872871,-1.159641,6.749270,8.205764,8.306205,-8.190275,0.241912,8.616641,5.907296,2.758850,-1.645016,1.045758,-0.915608,0.571453,-4.771374,6.638544,3.835213,6.226778,2.810364,7.666445,-5.513461,-5.056772,-5.820089,-6.576311,-1.425948,2.943842,9.315948,-1.075786,-4.442480,-5.793391,0.638790,6.324214,-5.812741,7.563000,1.115809,-0.266995,5.102174,-3.588248,-5.458844,2.651561,-2.886535,4.148551,1.401624,9.789123,5.641481,-9.397142,4.693099,0.531448,-5.293934,-6.220015,-5.610867,-8.059239,5.532253,3.899476,8.126124,-2.136774,9.956192,2.451449,8.208179,-7.488626,-7.502581,-7.614765,3.924246,9.856630,-6.151131,4.234897,-1.150650,-7.184659,-5.160932,8.472550,-6.017799,1.552120,-4.063983,-9.623579,-9.439219,-7.818167,5.944017,-2.634306,6.786904,7.709402,0.301033,-7.648928,-0.102235,6.067369,-6.789465,-7.540491,-9.325988,2.153032,-0.964015,6.979981,-3.710506,1.104334,-5.319005,-6.120119,-4.786386,0.994702,5.592941,1.151796,7.284494,-7.327843,-2.630837,-3.614340,4.801952,0.444512,-3.880670,-2.727684,-6.916957,-0.385849,8.200169,-8.671882,-1.497724,-4.183671,5.677814,6.299772,-8.732014,3.965627,-1.098715,-1.724525,4.104268,1.648600,-4.631918,-2.141375,-8.369015,6.833536,-6.529275,2.047386,7.136812,-7.315059,0.457003,9.482470,1.206276,-6.628809,8.413186,8.829143,-6.795798,-0.107021,-9.054865,-6.387694,3.610770,2.616233,5.691058,5.175556,-6.339613,-6.885608,8.220860,5.626550,-9.316848,0.827426,-8.618662,-4.191628,7.368527,0.615144,7.183987,-3.072267,2.098014,-9.420080,-1.755076,-0.281519,3.278829,2.459361,-3.149679,-3.685392,-3.699282,-9.780285,-9.238928,-2.947534,5.813910,-1.008729,3.396490,-2.517733,-2.664748,3.070243,-1.495064,5.371268,-0.014395,-2.861627,4.726410,9.071675,-2.272631,3.648378,-4.934644,6.570509,3.181341,9.580626,-3.863747,-6.807188,-8.097601,-9.057153,2.822065,8.477403,-9.561473,-9.352220,-0.348929,5.065010,-7.018624,5.847914,-9.339314,-3.225984,-6.885305,-8.577745,7.863079,0.729094,8.355086,-2.422525,5.984964,-3.908626,-4.879445,-8.915781,8.186270,8.094188,-7.340381,-8.676877,5.562493,-7.919748,-2.500865,9.662050,4.262332,-5.181640,-3.391883,8.130466,-9.589284,5.125333,3.282035,4.899488,8.272375,-6.135652,9.650492,4.730215,0.039044,1.993505,-6.601232,-7.137464,0.661274,-1.352950,3.018014,-3.075953,-9.095618,-8.910006,4.724038,-9.286316,4.531343,-7.674861,8.709789,6.514199,3.657858,6.032974,4.225349,-3.320956,-6.227830,-5.692529,-9.644077,8.370822,-2.779140,-4.049232,5.023282,0.669534,3.744762,6.944203,7.969373,-7.303911,4.644441,-2.072151,7.868202,-1.329258,-8.592116,6.115589,3.597003,5.285173,0.984308,9.551883,-8.747556,9.815080,-6.551810,-1.729778,6.974047,-5.235612,-9.712861,-7.269887,1.885375,0.264293,6.780603,3.312474,4.468671,8.949198,-2.444182,9.671230,1.702472,6.192123,-7.708111,4.803751,-5.081641,-5.015416,-0.480321,-8.901978,6.808324,7.892834,-9.403877,6.873707,6.259882,-9.286718,0.095435,-4.075758,-7.966108,-8.146857,-4.736137,1.483417,-5.308914,6.365531,-9.635194,-4.540836,-8.747311,-0.861948,-4.667150,-0.580239,-7.325314,-3.953153,7.333083,-4.963115,-0.295252,-5.472945,-8.278693,8.079051,7.311355,-5.414184,-6.197472,-5.773760,-4.904739,9.313191,-0.371376,3.961192,3.617299,3.206889,-6.556447,-5.105445,-6.098067,9.338224,-0.655299,1.899715,-5.397672,4.593011,9.666141,9.818215,8.168612,-2.544608,-0.960172,-0.873281,7.717823,-5.782411,-6.618852,-8.327665,4.871996,3.382249,-5.152365,-6.172816,-4.885310,8.314508,0.826053,-9.822035,-9.264805,-7.833251,-6.889122,-7.744138,-9.644561,1.228528,5.172844,-2.708820,-8.364597,1.571909,-4.756374,1.140809,4.719115,-7.932306,8.510429,1.661296,-9.754966,-9.968448,0.957107,-4.465203,-9.312459,-2.666626,-9.698034,-4.208024,-7.307505,4.672533,2.616661,-4.601782,-2.106501,1.237675,2.467610,7.077161,1.769545,-6.508664,-9.033254,-9.985483,-4.639126,-1.623188,1.924773,5.972552,-4.455435,6.038870,9.578331,3.788050,-2.369603,0.243775,6.527771,3.176411,5.521697,0.614412,1.155276,-0.134789,-6.449873,-0.908497,4.851175,-2.268981,-1.543754,-6.923232,8.619893,4.606864,-5.041423,1.378683,7.217220,-3.674542,-5.547707,-1.359297,-9.308989,0.976588,-7.853020,-4.841155,-6.637327,5.507959,-4.537600,-7.612765,4.380610,-1.798090,4.412682,-9.672459,-7.555749,1.259122,-1.454449,-7.710610,-8.513516,-6.949319,7.639900,-5.723840,6.736853,1.199200,9.329651,1.766733,1.678136,9.105479,9.398235,-3.192898,-7.588169,-7.853385,4.665682,8.726086,-9.979704,-3.886837,5.082498,0.502228,9.356348,-4.197001,2.855560,6.778471,4.033475,2.408173,-0.317379,2.158011,6.013974,-1.450641,-2.089706,-8.810634,1.257124,6.070352,6.016922,7.369882,6.807540,-6.022488,0.348417,8.594352,-6.730778,2.988015,-4.159343,5.110356,-7.308208,6.152833,-7.753911,7.053107,-5.762714,-4.162823,-9.494402,-4.814019,1.752123,-2.162428,8.453242,-4.055401,-6.334453,-9.090020,-8.252607,-3.379340,5.566011,7.716591,3.528098,5.463657,8.287155,9.471181,5.268808,3.710785,-8.019121,2.778952,-3.130867,4.068929,2.519166,3.068301,-9.744894,-6.908577,4.327918,9.460085,9.324726,9.110934,-8.187017,-8.186405,-8.598546,-5.433852,8.805434,-3.351481,2.638862,-8.023348,-6.409203,-3.439311,7.106957,-8.184353,0.421088,6.724008,4.973471,2.469010,4.863082,5.204968,-9.547316,1.165741,-0.753167,3.250897,9.207565,-8.453755,3.963992,-8.751197,-0.406740,-9.383254,-4.225601,-4.937031,-1.873123,2.038421,6.404093,9.494796,2.886754,7.676148,9.937377,9.919233,-9.584327,-2.379856,1.472272,-4.878208,6.392087,8.879587,-8.731867,6.489618,8.450278,-9.912828,-0.236846,-8.433278,-6.550912,9.070692,-5.998563,6.206674,-9.583155,1.043333,-1.697661,5.271011,-2.000732,-5.442615,-8.207052,1.358070,-7.030577,-7.094154,0.742521,-2.386946,-8.752856,3.049549,5.937254,1.143803,-0.244563,1.143268,-2.790497,8.579111,4.566095,6.150848,3.195962,8.977756,5.453428,-6.440863,4.458477,-0.094479,-9.345383,-8.948528,-9.152683,-8.912659,-9.460864,-5.973162,-7.866530,5.734835,7.159533,-4.891931,0.377977,-0.153608,2.473809,-0.963694,-2.662178,8.695876,-1.202890,-1.348879,8.673359,-4.379618,-6.046002,2.888505,-7.373926,-1.031073,4.312381,-7.950972,-5.513143,9.495574,-3.192967,-8.215366,3.905348,3.205265,-1.152126,-1.396603,-5.115346,1.913463,7.834834,-8.173958,-0.589008,3.590425,3.668700,-1.206935,0.006288,4.660574,1.590577,-8.220313,1.332589,3.057060,2.018504,-5.208523,-9.334464,-6.707229,-4.956879,2.603987,8.042776,-0.114759,-7.263372,-7.315268,8.456042,4.797157,-9.195810,2.454859,-8.427918,4.411575,-9.373958,8.331296,8.857075,3.795586,-8.273616,-4.556742,7.206956,-6.558594,-4.100703,0.760306,5.479473,-8.706337,-7.255619,6.629961,-4.337205,-3.353765,-8.493924,2.588971,2.790014,3.526336,3.214560,5.648973,4.034241,8.188134,0.441048,7.595566,9.850362,-3.320682,6.696966,-0.736296,-2.910041,-9.857989,1.023638,-0.446489,-0.642703,-0.155753,-4.036002,0.435011,-1.630914,0.985703,2.506677,-4.884442,-9.720377,8.768653,-9.199047,-5.914342,-8.038394,-6.006360,-8.710354,4.146144,-2.208952,6.839730,2.711456,-0.458487,9.534092,4.441763,-1.683654,1.370812,-8.650512,-4.671205,1.787926,1.949039,-5.588280,7.167765,6.902020,5.617329,-7.461360,-8.364917,9.908153,1.574733,-5.023347,-9.479049,-2.631941,2.869934,-8.160075,-6.734793,-8.122093,0.078093,5.469696,-3.928783,4.859012,-2.989150,-1.711471,-0.464453,-7.744409,-5.935691,-9.135442,2.272734,-8.970387,-3.652270,7.386073,-2.204012,-8.185241,-3.712047,-9.769215,-0.235368,-3.518957,-9.639637,6.140636,4.326688,-3.515489,-6.535983,-6.934530,-7.816908,1.270829,4.561541,6.132078,-2.075786,1.362908,1.340505,9.335653,-8.560168,-4.069003,-8.529030,2.134455,5.959596,6.878511,-8.442666,-6.066548,5.792660,9.171114,-1.381210,-1.119952,8.609089,7.172056,-8.958079,-4.816639,-9.819356,1.044911,3.939104,-2.960600,-5.301192,-3.821956,8.289048,1.819228], dtype = "float64")#candidate|4859|(1080,)|const|float64
call_4858 = relay.TupleGetItem(func_1435_call(relay.reshape(const_4859.astype('float64'), [1080,])), 0)
call_4860 = relay.TupleGetItem(func_1437_call(relay.reshape(const_4859.astype('float64'), [1080,])), 0)
output = relay.Tuple([bop_4842,call_4849,const_4850,call_4858,const_4859,])
output2 = relay.Tuple([bop_4842,call_4851,const_4850,call_4860,const_4859,])
func_4864 = relay.Function([var_4840,var_4841,], output)
mod['func_4864'] = func_4864
mod = relay.transform.InferType()(mod)
mutated_mod['func_4864'] = func_4864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4864_call = mutated_mod.get_global_var('func_4864')
var_4866 = relay.var("var_4866", dtype = "int64", shape = (3, 1, 7))#candidate|4866|(3, 1, 7)|var|int64
var_4867 = relay.var("var_4867", dtype = "int64", shape = (3, 11, 7))#candidate|4867|(3, 11, 7)|var|int64
call_4865 = func_4864_call(var_4866,var_4867,)
output = call_4865
func_4868 = relay.Function([var_4866,var_4867,], output)
mutated_mod['func_4868'] = func_4868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2094_call = mod.get_global_var('func_2094')
func_2096_call = mutated_mod.get_global_var('func_2096')
call_4889 = relay.TupleGetItem(func_2094_call(), 4)
call_4890 = relay.TupleGetItem(func_2096_call(), 4)
output = relay.Tuple([call_4889,])
output2 = relay.Tuple([call_4890,])
func_4900 = relay.Function([], output)
mod['func_4900'] = func_4900
mod = relay.transform.InferType()(mod)
output = func_4900()
func_4901 = relay.Function([], output)
mutated_mod['func_4901'] = func_4901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2485_call = mod.get_global_var('func_2485')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_4933 = relay.TupleGetItem(func_2485_call(), 1)
call_4934 = relay.TupleGetItem(func_2487_call(), 1)
output = relay.Tuple([call_4933,])
output2 = relay.Tuple([call_4934,])
func_4953 = relay.Function([], output)
mod['func_4953'] = func_4953
mod = relay.transform.InferType()(mod)
output = func_4953()
func_4954 = relay.Function([], output)
mutated_mod['func_4954'] = func_4954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_4955 = func_1336_call()
call_4956 = func_1336_call()
func_1210_call = mod.get_global_var('func_1210')
func_1214_call = mutated_mod.get_global_var('func_1214')
const_4958 = relay.const([-9.432770,2.412947,1.105518,0.562436,-3.819229,5.042198,9.118263,-2.286546,0.003318,4.430477,-1.302320,0.104941,-5.275491,-8.942764,7.922822,-3.029767,-3.525941,-4.597387,-3.138895,5.263870,-3.550914,-7.093221,9.685630,1.488182,-6.097282,-7.696908,4.563351,2.940639,2.543612,3.234307,0.880423,-1.459141,0.966042,-9.890460,2.770996,-3.034226,-0.946416,1.150850,4.219240,-7.043041,3.641589,-1.965446,-4.121169,-6.039926,-4.362592,-1.067908,1.745970,0.308196,-4.406538,-1.990443,4.870013,6.464920,-0.871967,1.273744,2.107175,3.515093,2.945500,-7.933221,4.595154,4.161515,-8.140403,-7.974890,1.686894,5.927236,3.648520,7.840012,-8.042343,-7.836891,3.397979,8.321893,4.149296,4.280891,-4.150819,0.526639,3.042032,9.107708,-2.606905,1.659293,4.886256,4.057846,4.216169,-2.374502,5.482772,-7.839009,-8.301381,-6.586480,-0.822211,-3.482798,5.487145,1.237467,8.665588,-3.349634,-5.663847,7.008623,-5.840078,-8.347223,0.241993,-3.846047,1.111132,6.681605,-9.134951,3.650676,2.529635,1.232440,9.239383,3.156217,-2.050975,9.707370,-0.099354,-5.547929,6.656279,-8.906546,4.606003,-9.553329,7.530688,9.389929,1.549768,-3.038093,-5.842565,0.720264,-3.369325,-6.611169,-9.998783,0.713893,-3.574131,-3.587352,-4.813913,-4.447367,2.769559,-8.981451,-9.437062,-8.488873,0.037846,2.081203,-4.979868,2.588686,5.556579,6.663581,3.488281,-0.006940,7.172441,-3.621917,1.528417,1.439640,6.761675,0.348900,4.876100,4.454851,7.191320,6.957732,0.741644,-9.327978,-7.613444,-5.593027,8.430294,-6.383147,2.898078,-0.290137,3.567221,8.149070,-1.359966,0.300377,-2.044526,-2.427607,5.682851,-4.039827,-4.294167,8.245616,-4.659921,3.864764,4.966976,-9.372094,-9.870913,0.290378,8.041234,-5.451198,-7.655423,1.404252,-3.201161,-9.292802,1.709557,-6.957076,1.056589,7.661434,7.112366,7.636896,-4.893112,-5.274698,1.483270,-4.073904,-8.214367,-5.769072,-0.846457,-7.798996,5.885784,-3.894291,9.911019,-0.217482,0.199197,-2.573870,-3.552562,8.617920,-3.064655,1.274838,2.136900,-8.581634,-0.549451,-6.209826,-5.102680,8.399314,2.789892,4.830641,-0.589537,-2.078708,5.014290,1.174475,-6.859940,-9.448700,-0.073390,-0.245401,5.123381,6.602766,8.636050,7.169596,-1.832869,0.862192,-0.194378,-7.509083,3.114219,-8.448803,-1.004852,-6.091154,-1.399300,7.684680,2.923523,5.986311,-9.648220,-5.400797,-4.152842,1.840244,2.271399,1.970021,1.856585,-5.371924,-2.832791,5.317974,-7.482339,5.205384,-9.368507,0.454092,0.424951,0.087770,-0.959544,9.686019,9.326576,4.780213,-0.437690,-2.505118,8.132957,-6.445803,-6.895465,-7.688890,7.600870,8.718047,-1.839159,2.661098,0.291454,3.908593,3.653821,8.069574,2.389462,4.674788,6.185206,-9.071427,-4.619644,-7.101955,-1.926913,-6.837735,-8.862308,-2.392760,-3.319964,-2.985523,-0.537836,1.417467,5.743596,-9.831361,-7.704540,-0.283344,7.585458,-9.919106,0.422679,-1.755176,1.244483,7.079105,3.765250,-6.575238,-6.154645,7.079386,-2.076173,-9.385391,4.761405,-5.474304,-5.603835,8.261070,8.003128,1.123788,-2.502471,8.293969,-1.504598,-9.495904,-7.888127,-9.613164,1.410937,3.878587,-8.638716,3.149094,-7.545508,4.584197,-1.454997,-4.097086,-6.969142,-8.749299,-4.751939,-8.073498,1.050456,-6.364204,4.336260,-2.656949,-4.197607,-8.181343,5.799594,1.842135,-8.246326,-3.905146,5.395263,-1.645189,-4.409348,1.478923,-7.313195,-3.947462,-1.649200,0.458463,7.463608,-4.712274,2.279810,-3.093814,9.976466,-5.462814,9.262994,-6.869376,-2.090741,-5.076093,-1.978716,1.111820,-2.249311,-2.862127,-4.569511,-0.927125,9.837878,3.760239,-6.739949,0.557129,5.458579,6.575930,-1.917600,-8.669591,-9.570817,9.957091,-4.224854,-0.820583,-4.408177,0.025348,-6.945710,-3.832695,-5.729008,6.676972,-0.658780,-9.751594,-2.664438,-4.435918,-3.622721,1.310977,0.052632,2.891254,5.547044,-6.275889,-3.036160,-3.319348,-4.493272,-7.139623,3.714931,9.163711,-4.054242,3.086138,3.282379,0.449748,-7.708254,-4.467265,5.890123,0.938904,8.050859,8.498066,5.410189,4.558423,-8.646679,9.590831,9.108581,4.823391,-8.500091,-2.927755,-6.403687,9.305296,6.841342,8.050021,7.109580,8.573442,-0.625648,-2.455672,5.515699,1.023467,1.438740,5.114294,7.659519,-3.139897,6.964255,0.397640,-2.975430,5.104793,2.904754,6.623324,0.744706,3.206085,7.573606,-6.532760,9.072054,-6.609213,-6.690914,0.415206,2.506941,1.577738,2.127219,-3.502362,-0.669372,4.372215,-7.300038,-8.301212,4.018399,-6.428592,-3.435620,6.655676,-7.103570,-2.998341,5.601312,4.868325,-6.770968,-0.800336,2.437856,0.897282,-8.747896,6.967262,4.906307,-8.709061,-1.919314,5.949067,6.380835,-8.293847,0.130415,-5.075170,7.103871,3.262541,9.322813,2.202909,-1.121505,-1.817073,4.975567,-4.643055,4.133815,4.066240,2.256445,-4.153618,-4.276071,-5.725696,-1.047525,-6.033771,-9.379245,3.999737,4.264787,1.022221,3.456169,-6.393665,9.327823,-0.547517,-1.041618,-7.034456,-2.641020,-1.123110,-8.553185,-4.583824,-8.674784,-1.401688,-5.796424,-3.113730,-3.537619,-3.174585,1.303276,-6.018384,9.567187,5.599604,-0.555488,2.075514,7.492656,6.273118,-3.286196,-5.713714,3.744092,-8.941287,-0.773715,6.030732,-0.806289,-3.460470,8.670805,-0.711493,2.665653,-2.385487,-1.321598,9.971010,1.555340,0.846201,-0.214115,-4.648151,-6.187696,-1.701075,7.106957,2.723455,7.006249,0.068797,-9.409057,5.667781,-7.472504,0.749794,9.374959,-7.795853,-6.693964,-0.875695,0.716407,-8.993289,0.064458,-3.727606,-5.732162,-9.753001,3.114732,-4.181763,-1.329877,-2.623733,6.594501,0.296438,-4.367092,-2.709811,3.978179,9.523705,3.444525,-6.025667,-3.324248,-4.684377,-6.947374,-9.240305,-9.556309,0.670912,-9.386878,0.401586,4.859316,-7.997181,-4.098068,-2.364683,-8.946487,-8.960611,0.659348,-6.492625,0.016116,4.831800,-5.030780,-4.727607,-1.360708,3.076441,4.689487,0.584582,4.584209,-3.300672,-4.389582,9.388481,-6.044151,-0.326590,-0.651132,-1.749618,0.429215,4.797062,1.771806,0.992250,2.412575,3.125359,8.416877,0.653228,-8.745763,1.215832,2.700287,8.508835,-1.796520,1.085713,9.003236,8.300619,1.491503,-8.792004,-5.256134,5.058667,-2.591571,-3.636539,7.871742,-9.902756,1.276581,-4.545304,-7.991128,-3.357054,0.065046,4.465956,8.451660,-5.369181,8.341543,-2.906344,-3.995577,7.531694,-5.659927,-7.100056,2.419033,4.366500,-4.146037,1.750363,-0.276061,-9.356941,-3.602971,-9.484577,-3.942612,-1.964298,2.279112,5.459255,-1.084634,-4.684119,-1.862136,-3.020689,2.712720,-7.200244,9.104170,-4.854482,2.852785,-7.389077,-6.485312,-0.442243,9.989846,-5.569513,5.089037,-7.743374,-7.352876,-5.694505,1.090481,-8.689921,-7.176392,3.300356,7.009198,4.364437,-5.617631,-5.082559,-3.396164,3.598584,2.634346,-1.218958,8.475528,2.710289,1.764070,-7.585694,-4.810703,6.965149,5.966743,4.078067,-6.557983,3.553637,-8.634946,0.262327,-9.310170,-7.803814,-2.933465,-3.444825,6.308246,5.563951,7.992920,7.643139,1.266642,8.243193,7.622646,7.944011,2.143162,-2.173542,-4.156307,0.723898,-6.238189,-2.782616,-0.690412,-8.469544,-0.169684,9.479846,5.641425,-9.025774,4.606753,4.933959,-9.380634,6.492027,-8.033967,0.087145,4.098702,9.016444,-1.026204,7.873685,2.256910,-6.322783,5.808698,3.689401,-1.601054,5.429121,3.876264,6.040622,3.880931,-0.117570,-8.294011,-9.748538,-3.451294,-6.585712,-6.279179,8.808878,5.258950,4.881131,8.374156,-6.493532,-7.458805,-1.239178,-7.392009,2.755487,-8.131254,6.587083,7.187317,-3.507316,-1.836456,-1.880660,-7.626127,-1.872819,8.934391,3.086784,-5.514701,0.244337,0.606917,6.140131,1.483656,-7.611941,-3.437905,-1.536299,1.715268,8.482579,1.706758,-2.678236,2.837963,-3.052190,7.791871,-5.132563,6.881548,-2.107350,5.622933,-3.148211,9.516502,-1.434445,4.905729,1.179572,6.460678,-0.372077,1.873970,6.380495,3.462068,5.885817,6.166587,-3.329788,0.500182,2.508801,-6.704335,3.762138,-4.130601,9.221593,9.278318,7.506699,0.488810,1.742903,-5.576758,-9.600700,-3.534871,-9.900105,9.458450,-2.458634,-2.901701,6.906774,-3.861886,-9.537698,-3.078964,-3.665834,-8.643525,-8.390963,3.304207,-1.749903,-2.971873,4.185137,5.706397,-7.722897,-0.196914,4.546161,1.837457,-4.641399,-6.106552,-5.877622,-1.391934,-3.074155,-7.458316,6.222546,-1.966929,-6.986247,-5.722604,-4.763490,8.299776,-1.217178,1.135307,-4.216170,-8.543127,-3.795246,8.895344,9.144597,4.254743,7.081743,-6.044799,5.739819,-8.151363,-5.572552,7.493566,-8.723641,3.231086,5.711648,0.267784,1.382099,-0.566860,-5.766970,8.628211,1.442606,3.145848,-5.966631,9.237676,-0.184492,2.847525,-9.718732,7.898428,-3.498469,6.976964,-5.052173,8.568419,-7.536225,3.413899,-7.276744,-5.099450,-0.530668,-4.915651,-5.075743,-9.113149,7.286442,8.879278,3.243048,8.991531,6.126283,9.763978,9.829466,-5.331152,-3.795622,-3.282770,-6.523332,-3.046113,-4.389466,3.051009,0.683604,2.392516,-5.213902,-8.743942,-5.770041,1.235028,7.374061,0.643861,8.913698,-7.223966,3.575329,-9.660951,-8.470131,-4.081048,4.513212,2.811946,-6.728503,-7.901799,6.995937,-5.321571,-8.839297,4.930454,-2.121551,-0.622149,-2.088248,4.139722,8.259872,2.964616,-6.133988,-2.320615,-5.671533,-1.545034,-0.249386,2.205830,-6.427247,0.208460,7.583990,-1.331287,3.844744,0.701722,2.558021,-0.411016,7.807521,-3.032269,6.180745,1.221403,-6.045321,-3.850237,-6.726748,-0.517990,1.390033,0.009530,6.882251,-6.176601,-4.218374,-5.207829,-0.975010,-2.039072,3.666961,-8.260548,5.042741,-7.897707,3.228971,4.725582,-4.169947,-5.450952,8.360219,-2.271719,3.885073,-8.535017,-5.753115,-7.224892,5.901067,-3.676881,8.915486,3.308974,8.545439,1.551003,1.051514,-9.380664,-0.027808,4.609949,5.491796,-9.488524,1.331859,-5.726057,-4.302231,-8.896041,-0.029010,-1.344975,8.635235,-5.192478,3.883785,-9.010412,-1.771761,-6.015099,9.616901,3.470506,1.776132,-1.584299,-6.417909,-0.682645,9.287315,-5.656084,-3.553656,1.184099,-2.629591,-6.516214,6.052548,-1.664008,3.772075,3.514296,1.616322,1.743718,-7.117513,3.853983,1.931839,4.267890,-1.438703,-8.279032,-1.855845,6.818533,6.388213,-2.006797,-3.838467,3.223009,6.019280,-2.999841,5.869666,6.480478,3.175162,-9.334058,5.583975,9.021224,6.520596,-1.810048,-1.169423,-2.800747,8.534505,-1.248301,-1.946659,7.412236,-2.720118,-4.167935,-8.827113,-1.089348,-4.179589,-2.612205,-8.330118,6.774025,4.003035,-6.024379,8.631803,3.072490,7.486432,-5.728027,6.104076,-9.377955,-7.698077,1.184708,-1.854390,-5.731218,-0.688836,-6.761314,3.479144,-9.083873,7.070580,-2.084231,-2.198973,1.369152,5.028122,2.675060,-5.571498,8.356847,-0.177318,2.664431,-8.404206,1.252817,-7.872810,4.894997,2.092939,-0.338701,-3.919889,-3.217369,-7.592578,3.798790,9.296245,1.020765,-4.416434,-1.540249,9.317375,0.341541,-4.797889], dtype = "float64")#candidate|4958|(1080,)|const|float64
call_4957 = relay.TupleGetItem(func_1210_call(relay.reshape(const_4958.astype('float64'), [9, 12, 10]), relay.reshape(const_4958.astype('float64'), [9, 12, 10]), ), 3)
call_4959 = relay.TupleGetItem(func_1214_call(relay.reshape(const_4958.astype('float64'), [9, 12, 10]), relay.reshape(const_4958.astype('float64'), [9, 12, 10]), ), 3)
func_3877_call = mod.get_global_var('func_3877')
func_3880_call = mutated_mod.get_global_var('func_3880')
const_4983 = relay.const([7,6,3,-2,10,8,3,10,3,-4,-6,-2,-1,-4,10,-1,-9,3,-9,-10,10,-4,6,-2,-4,5,5,-2,6,9,1,-4,-8,-6,-3,6,2,6,-4,9,7,9,-1,-8,-6,4,-8,-2,5,-5,-2,-2,1,-2,-8,-2,-5,7,-3,-5,-4,10,7,-2,8,3,-8,-4,-4,-5,-9,7,1,2,-1,-5,-5,-8,-7,-7,8,6,-6,7,1,2,1,6,5,6,-6,-10,-7,7,9,-10,-5,-2,-9,1,-1,9,-2,1,-6,3,9,-7,2,-10,-8,-7,-9,4,-6,-7,7,8,-5,-9,8,-3,5,-1,3,-7,4,-4,1,-10,-2,-5,-4,-8,-1,-10,-9,4,-4,-1,10,8,10,-8,1,-9,6,-1,4,-9,-6,-4,1,-1,4,-10,9,-10,-1,9,6,-4,-1,-3,4,-2,9,7,3,-3,-9,-3,2,-7,-2,4,6,2,-10,-2,5,7,9,3,2,-1,10,9,-9,-4,3,-1,-7,6,-8,-4,-4,6,-4,5,3,-7,2,-5,-2,-4,-9,4,9,-5,-10,-7,-7,6,-10,-7,9,-7,2,3,-3,1,-1,-7,-6,-5,-1,-9,-7,-2,-7,1,-5,-8,10,-4,-8,4,1,2,-4,-4,-1,-5,-1,5,-6,-6,5,-1,-7,8,10,-7,-3,-10,7,-4,-8,-7,6,7,-8,-2,-8,8,7,-3,9,-8,10,-1,-2,7,6,9,6,3,-10,9,-9,5,4,-3,-9,-5,-10,8,-5,-4,-9,-2,-2,10,-1,9,-7,-6,-2,4,-9,-10,9,-3,-5,5,3,-10,2,4,-1,1,-7,1,-5,1,-5,-5,1,9,6,-9,-1,3,-8,-7,9,-7,5,6,-4,-4,-9,5,8,7,10,-4,-4,-6,-3,1,1,10,7,-5,-4,2,-9,-5,-3,-4,6,-5,6,-3,2,-1,-6,-8,9,-6,2,6,6,-10,-4,1,-4,-10,-8,7,1,-5,-1,1,-6,-2,-6,-10,2,1,-4,-5,1,-9,2,-10,-6,-9,-8,8,9,2,2,8,-2,9,-1,6,-2,10,-3,-7,7,-9,-10,1,-8,-5,-5,-6,1,-6,-2,4,-9,9,7,2,-6,1,7,5,6,-8,2,9,1,-6,8,-6,4,-9,-1,-5,2,-3,1,-6,8,8,-10,-3,-2,2,7,-9,3,-10,-8,3,4,-1,-4,1,-1,-1,-6,9,-1,8,-9,9,-4,10,7,-6,-9,-5,1,4,7,-10,8,-10,10,-9,6,5,-6,-6,8,3,6,-10,-5,9,-8,4,-8,-6,-4,-1,2,2,9,-10,-9,-2,-2,4,-7,-1,1,4,10,2,-5,-6,-7,5,-8,2,-10,4,9,1,-10,4,8,5,-9,3,7,3,2,1,4,9,8,-8,-3,6,3,-9,7,10,8,-2,-5,-3,2,6,7,-2,3,3,-10,1,8,-6,-1,-3,-10,-8,-9,-3,-4,8,6,-4,1,7,8,-7,-6,-3,1,-10,2,-7,8,3,1,-1,1,-6,-5,-6,-10,9,-7,-7,-8,-1,-4,1,-10,-3,-6,-8,4,-1,-8,3,-1,-6,-5,-9,9,-5,-10,-6,-3,-1,-7,-7,-4,9,-7,-10,5,9,10,-4,9,3,-8,-10,-9,-9,2,7,-6,10,9,4,-7,-5,-2,-5,10,8,6,-6,-3,-3,-1,-2,9,2,3,3,8,8,-8,-1,-10,6,-9,5,9,8,10,-9,-2,-6,-7,-7,-6,-7,8,3,-6,-8,-1,-8,8,-10,-6,7,10,-6,-4,-1,8,7,5,7,-8,8,-5,10,4,4,-1,-9,4,-7,8,1,8,-3,-5,-8,-3,-2,5,-4,6,-9,8,-7,1,3,3,-7,-9,8,1,8,-2,-6,4,4,-7,6,-10,10,-8,3,6,-4,2,-8,6,9,-8,-3,-5,4,-1,-9,-5,4,-3,-5,-9,-1,-1,-4,-7,-4,-9,9,7,8,-4,-1,-8,-2,-4,-10,-8,-3,-2,-5,-3,-5,-8,-8,10,3,5,-4,-8,5,-7,-4,6,3,6,8,-1,-2,1,-3,8,-6,-9,7,9,9,7,-1,3,-2,6,-8,4,5,4,6,-4,-4,-3,10,4,-9,3,5,-6,4,-6,-8,-6,6,10,1,-6,-7,-7,2,6,-6,3,-4,-6], dtype = "int16")#candidate|4983|(819,)|const|int16
call_4982 = relay.TupleGetItem(func_3877_call(relay.reshape(const_4983.astype('int16'), [9, 7, 13]), relay.reshape(const_4983.astype('int16'), [9, 7, 13]), ), 2)
call_4984 = relay.TupleGetItem(func_3880_call(relay.reshape(const_4983.astype('int16'), [9, 7, 13]), relay.reshape(const_4983.astype('int16'), [9, 7, 13]), ), 2)
func_3343_call = mod.get_global_var('func_3343')
func_3344_call = mutated_mod.get_global_var('func_3344')
call_4996 = relay.TupleGetItem(func_3343_call(), 1)
call_4997 = relay.TupleGetItem(func_3344_call(), 1)
func_1960_call = mod.get_global_var('func_1960')
func_1962_call = mutated_mod.get_global_var('func_1962')
call_4998 = relay.TupleGetItem(func_1960_call(relay.reshape(call_4955.astype('float32'), [168, 1])), 1)
call_4999 = relay.TupleGetItem(func_1962_call(relay.reshape(call_4955.astype('float32'), [168, 1])), 1)
output = relay.Tuple([call_4955,call_4957,const_4958,call_4982,const_4983,call_4996,call_4998,])
output2 = relay.Tuple([call_4956,call_4959,const_4958,call_4984,const_4983,call_4997,call_4999,])
func_5003 = relay.Function([], output)
mod['func_5003'] = func_5003
mod = relay.transform.InferType()(mod)
mutated_mod['func_5003'] = func_5003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5003_call = mutated_mod.get_global_var('func_5003')
call_5004 = func_5003_call()
output = call_5004
func_5005 = relay.Function([], output)
mutated_mod['func_5005'] = func_5005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3050_call = mod.get_global_var('func_3050')
func_3051_call = mutated_mod.get_global_var('func_3051')
call_5014 = relay.TupleGetItem(func_3050_call(), 0)
call_5015 = relay.TupleGetItem(func_3051_call(), 0)
func_3343_call = mod.get_global_var('func_3343')
func_3344_call = mutated_mod.get_global_var('func_3344')
call_5026 = relay.TupleGetItem(func_3343_call(), 0)
call_5027 = relay.TupleGetItem(func_3344_call(), 0)
func_1626_call = mod.get_global_var('func_1626')
func_1628_call = mutated_mod.get_global_var('func_1628')
call_5029 = relay.TupleGetItem(func_1626_call(relay.reshape(call_5014.astype('bool'), [216,])), 2)
call_5030 = relay.TupleGetItem(func_1628_call(relay.reshape(call_5014.astype('bool'), [216,])), 2)
func_288_call = mod.get_global_var('func_288')
func_290_call = mutated_mod.get_global_var('func_290')
call_5032 = relay.TupleGetItem(func_288_call(), 0)
call_5033 = relay.TupleGetItem(func_290_call(), 0)
func_188_call = mod.get_global_var('func_188')
func_191_call = mutated_mod.get_global_var('func_191')
const_5037 = relay.const([[5.127007,6.121751],[9.188324,-6.348482],[7.232286,2.874785],[9.640438,-6.037083],[6.147742,4.177396],[-9.554753,-6.520367],[-6.036168,7.363064],[9.610618,-7.769623],[-8.258857,-9.013649],[8.575424,8.867417],[-5.171078,-6.354432],[7.517614,8.058627],[-2.467181,3.451356],[-4.582129,-1.637752],[5.013556,-7.138497],[4.705346,7.974021],[-5.510593,3.535493],[-5.272609,5.769566],[-1.684963,-1.357965],[-1.225956,-3.546925],[-7.557210,-4.481926],[3.954074,4.769767],[-6.782675,-7.646400],[-2.987243,8.201640],[1.604895,9.530711],[-1.940334,8.481692],[-8.896076,-3.241486],[7.446703,7.097796],[-7.903554,8.629066],[2.013858,-6.525230],[-6.280375,4.168455],[-7.966903,6.693302],[1.644032,3.729852],[6.427053,-8.474608],[1.972525,0.287696],[2.586086,-8.950408],[-8.951982,-6.997835],[3.003772,5.943643],[6.808987,-7.711167],[-0.314523,3.590733],[-1.845926,8.223568],[0.716193,-9.762433],[-8.173324,-1.063684],[-4.562711,-5.187221],[-0.494062,-1.389619],[1.452600,6.384418],[-6.626129,3.020689],[4.140344,8.678355],[1.762233,-3.456044],[-3.788887,4.058829],[-6.301680,7.684645],[0.279509,8.315420],[-7.117393,5.398793],[8.259522,-8.174440],[-9.291902,-2.053399],[-7.662182,-5.137528],[-1.661113,0.281338],[7.527094,-6.279321],[-6.693454,-5.467550],[3.615803,1.850979],[-7.400569,5.193859],[2.660649,7.830433],[6.768829,6.649261],[2.130756,-4.607732],[-1.173970,3.604922],[-2.570053,2.443029],[0.049557,-4.630477],[7.154938,-9.074999],[-5.348469,-5.129860],[7.563565,-3.224393],[0.931392,-4.542395],[4.179019,6.540717],[-8.698739,8.738065],[-3.488497,2.669720],[-1.790846,-6.771710],[9.909593,8.296565],[-5.560297,4.068606],[-2.824435,7.408253],[-2.574142,-9.178720],[-9.316435,7.531702],[-6.924260,6.594876],[-0.390080,-9.639086],[2.541008,-2.290639],[0.204466,-8.943077]], dtype = "float32")#candidate|5037|(84, 2)|const|float32
call_5036 = relay.TupleGetItem(func_188_call(relay.reshape(const_5037.astype('float32'), [6, 4, 7]), relay.reshape(const_5037.astype('float32'), [6, 4, 7]), ), 0)
call_5038 = relay.TupleGetItem(func_191_call(relay.reshape(const_5037.astype('float32'), [6, 4, 7]), relay.reshape(const_5037.astype('float32'), [6, 4, 7]), ), 0)
func_3601_call = mod.get_global_var('func_3601')
func_3603_call = mutated_mod.get_global_var('func_3603')
const_5043 = relay.const([[3.845864],[7.760583],[-2.364644],[-9.310938],[0.534650],[1.147833],[2.164358],[-2.001334],[9.054856],[7.448180],[-6.632848],[5.889859],[-7.436648],[-1.180398],[-1.593705],[5.843189],[0.106616],[-4.789473],[6.155432],[-8.994617],[3.030136],[-6.845074],[-1.660279],[7.696575],[-7.930700],[9.613497],[-0.309452],[-0.136770],[-8.475172],[5.362122],[-9.794428],[-7.994960],[6.884800],[1.845549],[-9.106426],[7.421820],[5.813440],[-5.164247],[1.604605],[3.651228],[-1.952089],[-1.023840],[-6.718433],[3.146442],[4.524138],[4.591639],[0.857842],[-9.916777],[-1.213366],[-1.620886],[6.874628],[-8.477248],[4.656345],[0.955562],[7.283585],[-8.401082],[6.105804],[-2.777993],[7.137991],[-4.338936],[-9.782731],[-1.062651],[-3.481552],[-8.251375],[-2.048495],[7.371320],[-4.931003],[1.442271],[-2.977759],[-7.723971],[2.538826],[5.467506],[7.485263],[-8.882845],[2.659446],[-7.039344],[-9.577698],[-0.701577],[4.214791],[3.302753],[5.826303],[1.706494],[6.469209],[0.675067],[0.658930],[3.621741],[-8.541929],[-4.962255],[-9.512624],[-5.809882],[9.790918],[0.158311],[-7.207146],[-2.896827],[-8.582729],[2.022060],[-4.912232],[9.887067],[0.882999],[6.578701],[6.005331],[-8.930192],[4.820092],[1.599904],[6.668182],[-7.576295],[-5.735246],[9.971785],[3.981120],[-3.479955],[7.032178],[3.456641],[0.436976],[3.095394],[3.880932],[9.756392],[0.661761],[-9.982168],[-2.367138],[-9.717066],[4.220080],[1.315983],[-0.377016],[-7.128670],[-4.390968],[1.578957],[0.432451],[-4.217074],[-0.989302],[3.396277],[-2.387508],[-7.710699],[-7.742132],[9.075497],[-2.443062],[4.260961],[-7.873488],[-2.364744],[8.776014],[-9.176466],[2.243270],[9.954684],[-8.474352],[5.634640],[-5.314465],[-0.193351],[-6.519306],[-0.337869],[1.909227],[8.222222],[-8.821408],[5.827833],[3.058949],[1.304536],[9.953495],[7.976262],[-7.890759],[5.589446],[-1.478782],[8.133231],[2.081450],[3.919734],[-8.084229],[2.647968],[8.856024],[2.532349],[9.966951],[-6.378095],[-8.769664],[2.396944],[9.225983],[2.460420],[1.079520],[-5.622930],[6.813694],[-4.254868],[2.536172],[-8.819992],[-7.855366],[2.438611],[8.418851],[0.004505],[-4.376588],[3.637141],[7.907369],[-9.088957],[3.604382],[-1.917117],[-9.994748],[-1.234091],[-8.561434],[-7.700486],[0.126134],[8.408639],[-8.221191],[4.928061],[-6.870215],[-4.427793],[9.681259],[3.180468],[-8.936833],[1.201650],[6.590078],[0.095655],[9.102562],[-9.759861],[-6.001848],[3.701810],[3.040867],[5.270107],[-0.815764],[8.677489],[5.273708],[0.735995],[-9.450268],[-1.780652],[-9.746154],[-7.754163],[5.439759],[6.140644],[-6.116005],[0.793287],[-7.791732],[-2.422728],[8.282159],[-1.562315],[-4.774451],[-9.336300],[3.693499],[-8.676072],[2.132822],[4.046379],[2.857353],[3.169731],[0.682657],[1.899519],[-9.387783],[-8.618930],[4.317062],[0.898372],[2.332697],[-1.036260],[9.850910],[7.942459],[-0.675330],[-7.580065],[-5.748899],[8.044711],[-0.139987],[7.028099],[2.124953],[2.133138],[2.200913],[6.485041],[-5.231467],[6.279092],[-8.319573],[3.037380],[9.502085],[-2.992021],[9.606713],[0.974755],[-2.915324],[7.237922],[9.619427],[-3.130526],[9.219553],[9.985256],[-5.392652],[5.536374],[9.410194],[-7.092341],[2.629119],[8.188711],[-5.725865],[-1.764174],[4.887308],[-6.949766],[1.196765],[-9.761834],[-3.545410],[6.970436],[-4.009247],[-4.663835],[7.018102],[6.695732],[-3.085066],[-2.443417],[9.114812],[-0.618770],[-2.729559],[6.200141],[-7.474242],[8.497782],[5.796331],[9.311763],[0.715998],[6.225200],[7.022055],[-1.001822],[-9.427924],[5.597629],[4.754873],[-5.574511],[1.534063],[-6.829736],[9.374338],[0.708262],[9.149825],[2.572329],[-9.640196],[-4.206391],[-5.448115],[7.395260],[4.222623],[-0.017251],[4.371251],[5.060268],[-3.759623],[-5.435507],[-5.779894],[5.828678],[-2.541929],[-8.007827],[8.982769],[0.046321],[-7.530481],[7.032278],[1.776621],[-7.107372],[-2.095808],[-9.561232],[-6.274652],[-9.515976],[8.956944],[-9.216582],[-2.303148],[-2.842398],[4.393315],[-9.281155],[-3.339102],[-3.679140],[-0.335650],[6.842958],[7.076527],[-3.989478],[9.499900],[9.464024],[-8.883791],[-5.023057],[-8.493766],[-4.630549],[-3.300787],[-1.017568],[8.468835],[-7.031187],[-1.736103],[-4.071794],[9.168417],[-2.605600],[6.569355],[-9.969113],[-6.404849],[-7.663647],[-7.013152],[-3.048730],[2.705797],[8.372193],[1.767703],[2.452118],[-0.772352],[1.345556],[3.314667],[3.904710],[3.831991],[8.179125],[9.293898],[8.995763],[0.141468],[-7.412753],[-5.668930],[4.352123],[6.270392],[0.421745],[-8.345637],[5.975112],[7.604692],[7.355537],[-9.463521],[7.333533],[-9.419742],[-3.376441],[-4.647503],[3.000152],[1.644708],[3.474115],[5.497386],[-7.869004],[9.002657],[1.427627],[-8.935339],[2.435859],[0.134782],[-3.192849],[2.353441],[-3.087216],[-3.295398],[4.875735],[-0.677881],[9.573130],[2.345198],[-7.098337],[1.198269],[8.430730],[-6.096117],[-1.175735],[-7.641876],[-9.130542],[-7.830834],[8.758370],[-9.131661],[1.174644],[1.713880],[-6.729033],[-7.241881],[1.288085],[-5.259671],[-2.770381],[-7.096712],[5.493488],[-6.851144],[-5.106605],[2.344993],[2.271699],[2.683495],[2.176873],[-9.812387],[5.485866],[-5.589740],[7.064633],[9.701573],[-2.498107],[-8.953842],[1.291506],[-0.744102],[-3.739616],[-9.480172],[6.105270],[7.982201],[1.064634],[-4.338405],[3.585384],[5.213932],[-3.756735],[-3.264816]], dtype = "float32")#candidate|5043|(455, 1)|const|float32
call_5042 = func_3601_call(relay.reshape(const_5043.astype('float32'), [5, 13, 7]))
call_5044 = func_3601_call(relay.reshape(const_5043.astype('float32'), [5, 13, 7]))
func_188_call = mod.get_global_var('func_188')
func_191_call = mutated_mod.get_global_var('func_191')
call_5046 = relay.TupleGetItem(func_188_call(relay.reshape(const_5037.astype('float32'), [6, 4, 7]), relay.reshape(const_5037.astype('float32'), [6, 4, 7]), ), 0)
call_5047 = relay.TupleGetItem(func_191_call(relay.reshape(const_5037.astype('float32'), [6, 4, 7]), relay.reshape(const_5037.astype('float32'), [6, 4, 7]), ), 0)
bop_5058 = relay.greater_equal(const_5043.astype('bool'), relay.reshape(call_5042.astype('bool'), relay.shape_of(const_5043))) # shape=(455, 1)
bop_5061 = relay.greater_equal(const_5043.astype('bool'), relay.reshape(call_5044.astype('bool'), relay.shape_of(const_5043))) # shape=(455, 1)
output = relay.Tuple([call_5014,call_5026,call_5029,call_5032,call_5036,const_5037,call_5046,bop_5058,])
output2 = relay.Tuple([call_5015,call_5027,call_5030,call_5033,call_5038,const_5037,call_5047,bop_5061,])
func_5063 = relay.Function([], output)
mod['func_5063'] = func_5063
mod = relay.transform.InferType()(mod)
output = func_5063()
func_5064 = relay.Function([], output)
mutated_mod['func_5064'] = func_5064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2118_call = mod.get_global_var('func_2118')
func_2120_call = mutated_mod.get_global_var('func_2120')
call_5095 = func_2118_call()
call_5096 = func_2118_call()
output = call_5095
output2 = call_5096
func_5099 = relay.Function([], output)
mod['func_5099'] = func_5099
mod = relay.transform.InferType()(mod)
mutated_mod['func_5099'] = func_5099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5099_call = mutated_mod.get_global_var('func_5099')
call_5100 = func_5099_call()
output = call_5100
func_5101 = relay.Function([], output)
mutated_mod['func_5101'] = func_5101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2668_call = mod.get_global_var('func_2668')
func_2669_call = mutated_mod.get_global_var('func_2669')
call_5110 = func_2668_call()
call_5111 = func_2668_call()
func_55_call = mod.get_global_var('func_55')
func_56_call = mutated_mod.get_global_var('func_56')
call_5119 = relay.TupleGetItem(func_55_call(), 1)
call_5120 = relay.TupleGetItem(func_56_call(), 1)
output = relay.Tuple([call_5110,call_5119,])
output2 = relay.Tuple([call_5111,call_5120,])
func_5122 = relay.Function([], output)
mod['func_5122'] = func_5122
mod = relay.transform.InferType()(mod)
output = func_5122()
func_5123 = relay.Function([], output)
mutated_mod['func_5123'] = func_5123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_5130 = relay.TupleGetItem(func_603_call(), 2)
call_5131 = relay.TupleGetItem(func_605_call(), 2)
func_4422_call = mod.get_global_var('func_4422')
func_4424_call = mutated_mod.get_global_var('func_4424')
call_5134 = relay.TupleGetItem(func_4422_call(), 0)
call_5135 = relay.TupleGetItem(func_4424_call(), 0)
output = relay.Tuple([call_5130,call_5134,])
output2 = relay.Tuple([call_5131,call_5135,])
func_5136 = relay.Function([], output)
mod['func_5136'] = func_5136
mod = relay.transform.InferType()(mod)
mutated_mod['func_5136'] = func_5136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5136_call = mutated_mod.get_global_var('func_5136')
call_5137 = func_5136_call()
output = call_5137
func_5138 = relay.Function([], output)
mutated_mod['func_5138'] = func_5138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2855_call = mod.get_global_var('func_2855')
func_2857_call = mutated_mod.get_global_var('func_2857')
call_5157 = relay.TupleGetItem(func_2855_call(), 2)
call_5158 = relay.TupleGetItem(func_2857_call(), 2)
func_3387_call = mod.get_global_var('func_3387')
func_3390_call = mutated_mod.get_global_var('func_3390')
const_5168 = relay.const([[-3,-8,6,6,-7,-5,10,8,-9,-7,5,6,1,-2,5,-10,2,5,-3,-8,-8,9,-4,-4,-3,3,-4,-7,-1,6,4,-4,-8,-6,10,1,8,-7,-8,-7,-2,9,1,3,-5,-6,8,7,9,-7,9,8,-10,2,-8,9,9,-7,5,2,10,-1,10,-4,-3,-9,-1,-10,3,-10,-10,10,6,10,9,3,10,8,2,-10,-5,7,-7,10,8,-1,-7,-8,8,8,7,-7,-3,-8,10,-10,-8,-2,4,5,2,-10,6,-3,5,-4,-1,1,7,-1,-7,4,9,-8,-8,7,-8,-8,-5,9,-4,-2,3,1,3,8,6,-5,8,10,-8,-7,-3,9,7,8,10,-6,-5,4,10,8,-4,3,-6,-7,9,1,8,-10,9,-6,-1,-3,-1,2,10,9,1,-3,4,-3,5,-5,-3,8,6,-2,-8,1,3,1,3,7,-2,3,2,9,10,-10]], dtype = "uint16")#candidate|5168|(1, 180)|const|uint16
call_5167 = relay.TupleGetItem(func_3387_call(relay.reshape(const_5168.astype('uint16'), [15, 2, 6]), relay.reshape(const_5168.astype('uint16'), [15, 2, 6]), ), 2)
call_5169 = relay.TupleGetItem(func_3390_call(relay.reshape(const_5168.astype('uint16'), [15, 2, 6]), relay.reshape(const_5168.astype('uint16'), [15, 2, 6]), ), 2)
output = relay.Tuple([call_5157,call_5167,const_5168,])
output2 = relay.Tuple([call_5158,call_5169,const_5168,])
func_5184 = relay.Function([], output)
mod['func_5184'] = func_5184
mod = relay.transform.InferType()(mod)
mutated_mod['func_5184'] = func_5184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5184_call = mutated_mod.get_global_var('func_5184')
call_5185 = func_5184_call()
output = call_5185
func_5186 = relay.Function([], output)
mutated_mod['func_5186'] = func_5186
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5187 = relay.var("var_5187", dtype = "float64", shape = (10, 16, 8))#candidate|5187|(10, 16, 8)|var|float64
uop_5188 = relay.acos(var_5187.astype('float64')) # shape=(10, 16, 8)
uop_5194 = relay.sqrt(uop_5188.astype('float32')) # shape=(10, 16, 8)
func_3198_call = mod.get_global_var('func_3198')
func_3199_call = mutated_mod.get_global_var('func_3199')
call_5197 = func_3198_call()
call_5198 = func_3198_call()
bop_5208 = relay.less(uop_5194.astype('bool'), relay.reshape(uop_5188.astype('bool'), relay.shape_of(uop_5194))) # shape=(10, 16, 8)
uop_5219 = relay.sigmoid(uop_5188.astype('float64')) # shape=(10, 16, 8)
output = relay.Tuple([call_5197,bop_5208,uop_5219,])
output2 = relay.Tuple([call_5198,bop_5208,uop_5219,])
func_5235 = relay.Function([var_5187,], output)
mod['func_5235'] = func_5235
mod = relay.transform.InferType()(mod)
mutated_mod['func_5235'] = func_5235
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5236 = relay.var("var_5236", dtype = "float64", shape = (10, 16, 8))#candidate|5236|(10, 16, 8)|var|float64
func_5235_call = mutated_mod.get_global_var('func_5235')
call_5237 = func_5235_call(var_5236)
output = call_5237
func_5238 = relay.Function([var_5236], output)
mutated_mod['func_5238'] = func_5238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_5287 = relay.TupleGetItem(func_603_call(), 1)
call_5288 = relay.TupleGetItem(func_605_call(), 1)
const_5301 = relay.const([[[4.224415,4.001515,-1.315271,2.915341,-6.529466,-2.022581],[-4.384577,-8.069221,-9.893110,-2.391244,-7.558672,-8.017045],[2.050190,-0.695900,-4.286429,5.135131,-1.313591,8.116101],[3.089015,-7.889955,2.752344,7.224344,-0.217606,2.328129]],[[8.280907,2.363836,-3.307788,6.971510,-3.166659,3.585959],[8.085276,2.490217,-4.266799,-7.897559,6.622840,5.810432],[-0.822273,-3.633928,-6.349594,1.093680,-3.614008,7.172204],[-5.206273,-2.209038,3.004245,-2.331903,-6.583615,-1.846309]],[[-2.190280,-4.936855,-9.632217,7.608832,6.112693,9.041421],[1.991208,7.169300,9.783791,-5.670991,8.202679,-2.495332],[-8.577705,9.077461,-6.793431,5.346995,-0.647692,4.248151],[7.177242,1.772344,-4.900952,-6.517414,-9.836675,7.085132]],[[2.778133,4.261863,8.356742,0.282301,-9.136995,-5.790140],[-3.260453,-8.841889,-3.258423,8.226453,-1.807794,-6.581251],[5.776172,-0.942703,-1.828694,7.501829,8.973531,-8.766442],[6.155919,-4.020014,-6.406229,-5.680654,8.280792,0.549295]],[[-7.246887,4.256670,-6.016551,-1.098158,2.597669,8.005239],[-8.157082,5.679914,6.856374,-1.178966,1.126475,5.695478],[-7.373328,-5.754671,-0.183084,5.922437,2.368184,2.179541],[-3.874739,6.166403,-3.711123,3.887661,-6.915925,-3.883106]],[[-3.344178,-4.574337,0.646204,3.911524,0.082647,9.136975],[5.922805,1.922520,-5.511296,-1.148283,-9.526482,-9.363902],[-9.497381,6.746267,-8.995377,2.978950,8.466355,-2.342924],[3.389367,-6.414900,0.514614,-1.615942,-1.490830,8.062737]],[[-4.463680,8.743414,-6.653890,9.135511,2.902546,5.238150],[-0.935210,-8.188410,-9.975084,-1.230206,-0.554842,-5.277467],[8.118843,-9.729272,-5.711528,-7.064668,-8.384015,3.959115],[3.107286,6.537087,-6.938777,-3.542729,0.230694,-1.833632]],[[5.332265,2.400450,3.069680,0.662684,-8.800044,-3.393729],[-4.346413,7.469252,-4.903795,4.872636,7.323886,-9.971686],[9.612195,-6.826803,3.445733,-7.980538,-0.507430,-5.470465],[9.689585,-2.440051,9.040695,4.367031,1.494010,-6.645956]],[[6.553254,4.241440,1.870209,-7.599605,-7.308331,9.291906],[3.966417,-0.921909,-6.958341,2.446989,-9.335343,2.245970],[-2.432813,7.304157,-6.898528,8.595195,2.447312,-6.504616],[-4.669397,6.630040,-5.310036,-4.447739,-3.156756,6.111509]]], dtype = "float64")#candidate|5301|(9, 4, 6)|const|float64
bop_5302 = relay.bitwise_or(call_5287.astype('uint8'), relay.reshape(const_5301.astype('uint8'), relay.shape_of(call_5287))) # shape=(9, 4, 6)
bop_5305 = relay.bitwise_or(call_5288.astype('uint8'), relay.reshape(const_5301.astype('uint8'), relay.shape_of(call_5288))) # shape=(9, 4, 6)
func_2094_call = mod.get_global_var('func_2094')
func_2096_call = mutated_mod.get_global_var('func_2096')
call_5314 = relay.TupleGetItem(func_2094_call(), 1)
call_5315 = relay.TupleGetItem(func_2096_call(), 1)
output = relay.Tuple([bop_5302,call_5314,])
output2 = relay.Tuple([bop_5305,call_5315,])
func_5329 = relay.Function([], output)
mod['func_5329'] = func_5329
mod = relay.transform.InferType()(mod)
mutated_mod['func_5329'] = func_5329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5329_call = mutated_mod.get_global_var('func_5329')
call_5330 = func_5329_call()
output = call_5330
func_5331 = relay.Function([], output)
mutated_mod['func_5331'] = func_5331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5063_call = mod.get_global_var('func_5063')
func_5064_call = mutated_mod.get_global_var('func_5064')
call_5370 = relay.TupleGetItem(func_5063_call(), 1)
call_5371 = relay.TupleGetItem(func_5064_call(), 1)
func_3601_call = mod.get_global_var('func_3601')
func_3603_call = mutated_mod.get_global_var('func_3603')
const_5380 = relay.const([[-5.826167],[0.778782],[-1.973923],[-5.742955],[-7.283877],[-4.144596],[8.269223],[2.325205],[2.134804],[-7.133153],[-9.358492],[-8.769164],[-1.246640],[7.962356],[-4.012476],[-9.720041],[-1.649074],[8.313735],[9.747501],[6.736576],[-4.950344],[9.209665],[1.984078],[-7.635450],[-4.376625],[0.527579],[0.970352],[-9.507537],[3.588812],[-4.634926],[4.289627],[0.909296],[-1.884991],[-8.398649],[-8.160762],[-4.621841],[-5.245473],[-8.367588],[-3.282707],[-1.182504],[2.639607],[2.970310],[7.897583],[6.611996],[0.510537],[-2.529518],[-4.649759],[-3.304793],[-2.181712],[7.970659],[-1.348494],[8.571684],[0.623905],[-3.237040],[-6.975252],[9.910204],[5.957597],[7.091771],[-4.157011],[0.044983],[-1.323526],[-2.190023],[5.314250],[-7.250442],[7.106988],[-5.402359],[2.951848],[-5.290239],[-6.693574],[-0.387051],[-6.174099],[-3.589087],[-9.783367],[-4.417588],[-8.525342],[-3.830259],[-9.683128],[-0.985127],[3.425447],[2.849878],[-5.497315],[-1.620190],[-0.233269],[-7.078957],[6.434802],[3.039134],[-6.881751],[9.389983],[1.160939],[7.484783],[-3.465195],[1.205789],[-7.199321],[-2.178718],[-7.555509],[2.367154],[-1.431941],[-7.869468],[-1.611304],[5.270265],[7.002496],[6.292225],[-3.656767],[-6.649728],[6.057564],[-5.529327],[9.391227],[-7.585891],[3.375791],[6.133217],[-4.407081],[-6.149112],[-7.823073],[5.687877],[7.710728],[-1.999402],[-7.360639],[0.734224],[2.137949],[-2.397831],[3.028710],[-8.377627],[-9.834700],[8.286751],[7.204551],[7.543137],[9.617496],[-0.139362],[-1.307747],[-2.191759],[-2.829483],[-1.733705],[5.767783],[-3.984616],[3.151883],[5.620330],[8.058319],[4.844174],[-4.763149],[7.011237],[6.073762],[8.114077],[-0.814258],[-3.281679],[-5.881041],[-5.275901],[-8.675394],[8.381084],[-5.820358],[-5.011883],[-0.423667],[3.457928],[0.544204],[-1.467340],[1.902813],[1.033765],[-0.611999],[8.795351],[4.091272],[-0.931484],[-2.277919],[-1.068955],[9.012886],[-4.812024],[8.110850],[-4.755980],[-8.477321],[7.243105],[-6.479178],[9.146359],[9.189725],[6.103364],[-7.680977],[-9.250070],[-3.279338],[2.161922],[-2.175785],[1.619496],[4.231257],[7.805717],[-7.604103],[-9.230996],[4.058605],[-9.777815],[7.842113],[6.376393],[3.095625],[0.945866],[9.127918],[5.869914],[-4.171296],[5.998474],[-4.149418],[-3.249211],[-0.290531],[3.422856],[0.794331],[-6.979238],[1.376471],[6.552959],[-7.389238],[-2.587713],[9.227094],[6.761757],[0.034707],[-2.394455],[6.605410],[-5.128493],[5.573572],[5.491624],[7.100580],[-1.298556],[9.069623],[2.167192],[-6.117650],[7.989923],[-7.125823],[-5.862754],[2.815188],[-3.045698],[-0.587961],[-3.605649],[-1.856708],[8.171848],[-7.715034],[-5.893823],[6.403305],[-4.262843],[3.404522],[-4.795916],[-0.763554],[-2.141981],[2.752756],[-0.372136],[6.152274],[3.532437],[-1.241777],[2.196650],[1.240414],[-0.598381],[-9.837865],[6.027328],[7.190237],[-0.508944],[3.036689],[-3.888774],[-8.170111],[-7.064939],[5.482578],[5.437114],[-5.227994],[-4.428331],[-3.640554],[9.342908],[8.010288],[4.106027],[-6.856082],[3.588969],[7.749110],[-0.704861],[-2.155863],[-6.609699],[-4.716094],[-8.014427],[-0.084122],[-7.038164],[7.754473],[6.154941],[-6.025143],[2.294168],[-9.308173],[4.340009],[2.584755],[-3.294939],[-1.371880],[6.606678],[-1.213906],[-9.064850],[4.045406],[-1.172088],[-2.972416],[-6.846378],[-2.550728],[2.285754],[-7.510703],[-6.954454],[-3.488650],[-3.558105],[-0.146124],[-5.652537],[0.662615],[-0.367036],[3.882663],[-6.432849],[4.413147],[-1.441677],[7.526197],[2.148006],[-8.332312],[3.041382],[3.470535],[2.063969],[8.814545],[8.330687],[4.435506],[4.064265],[-6.449025],[-4.103874],[-9.935678],[-7.802692],[5.857397],[5.405006],[0.869614],[-1.426017],[7.990471],[-6.797921],[5.007992],[-2.455238],[0.137799],[7.872019],[6.040250],[-1.324075],[-9.602790],[-5.098952],[0.879156],[-3.213663],[1.356631],[-9.439024],[4.765939],[9.430621],[-1.811097],[0.475987],[2.297209],[-3.820019],[-1.440456],[7.201809],[-0.909775],[5.542006],[-5.815935],[6.581042],[-3.743810],[5.436159],[3.796953],[-6.412814],[-9.741531],[-3.440784],[4.215129],[0.515927],[5.499004],[-0.710150],[5.840244],[-1.138675],[5.842304],[-4.297591],[7.879044],[7.881933],[1.936951],[5.696596],[-0.129929],[4.701813],[0.082152],[0.184652],[-5.917018],[-8.925873],[6.581564],[1.917665],[-8.366210],[-3.714396],[9.067496],[-8.283517],[6.764955],[-8.767529],[-0.306111],[1.652347],[7.492123],[3.571082],[-7.984344],[2.887019],[0.477849],[5.769977],[-8.601656],[4.578882],[-3.293292],[-1.598741],[-2.550942],[-9.827875],[2.146290],[2.675748],[-0.603534],[-6.196148],[5.627348],[4.690302],[2.251666],[-6.216554],[-5.362911],[2.324216],[-9.403256],[2.093528],[-4.653084],[-5.508609],[-8.780771],[-1.300931],[0.223160],[4.904344],[2.244846],[9.214957],[-8.415494],[-6.812124],[-1.151278],[-5.875305],[-1.164174],[3.727898],[9.977812],[8.094590],[9.181617],[-1.555999],[-7.399667],[8.178700],[-8.937027],[-5.664204],[-0.405639],[8.749266],[-2.158217],[-7.055080],[-3.870776],[5.522919],[-2.142832],[-9.198975],[2.343196],[-0.709324],[6.180449],[2.624642],[0.270877],[-7.254784],[1.026594],[0.562633],[-6.858260],[-9.314503],[5.024608],[3.982801],[-9.348457],[-5.630741],[-6.774857],[-3.372168],[8.606728],[-2.756279],[6.093574],[-9.676423],[-8.514642],[3.905115],[4.668263],[7.196237],[4.428861],[-7.891639],[3.744156]], dtype = "float32")#candidate|5380|(455, 1)|const|float32
call_5379 = func_3601_call(relay.reshape(const_5380.astype('float32'), [5, 13, 7]))
call_5381 = func_3601_call(relay.reshape(const_5380.astype('float32'), [5, 13, 7]))
output = relay.Tuple([call_5370,call_5379,const_5380,])
output2 = relay.Tuple([call_5371,call_5381,const_5380,])
func_5389 = relay.Function([], output)
mod['func_5389'] = func_5389
mod = relay.transform.InferType()(mod)
mutated_mod['func_5389'] = func_5389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5389_call = mutated_mod.get_global_var('func_5389')
call_5390 = func_5389_call()
output = call_5390
func_5391 = relay.Function([], output)
mutated_mod['func_5391'] = func_5391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4900_call = mod.get_global_var('func_4900')
func_4901_call = mutated_mod.get_global_var('func_4901')
call_5399 = relay.TupleGetItem(func_4900_call(), 0)
call_5400 = relay.TupleGetItem(func_4901_call(), 0)
output = call_5399
output2 = call_5400
func_5412 = relay.Function([], output)
mod['func_5412'] = func_5412
mod = relay.transform.InferType()(mod)
output = func_5412()
func_5413 = relay.Function([], output)
mutated_mod['func_5413'] = func_5413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3089_call = mod.get_global_var('func_3089')
func_3090_call = mutated_mod.get_global_var('func_3090')
call_5425 = relay.TupleGetItem(func_3089_call(), 0)
call_5426 = relay.TupleGetItem(func_3090_call(), 0)
output = call_5425
output2 = call_5426
func_5446 = relay.Function([], output)
mod['func_5446'] = func_5446
mod = relay.transform.InferType()(mod)
mutated_mod['func_5446'] = func_5446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5446_call = mutated_mod.get_global_var('func_5446')
call_5447 = func_5446_call()
output = call_5447
func_5448 = relay.Function([], output)
mutated_mod['func_5448'] = func_5448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5412_call = mod.get_global_var('func_5412')
func_5413_call = mutated_mod.get_global_var('func_5413')
call_5460 = func_5412_call()
call_5461 = func_5412_call()
func_2094_call = mod.get_global_var('func_2094')
func_2096_call = mutated_mod.get_global_var('func_2096')
call_5462 = relay.TupleGetItem(func_2094_call(), 0)
call_5463 = relay.TupleGetItem(func_2096_call(), 0)
output = relay.Tuple([call_5460,call_5462,])
output2 = relay.Tuple([call_5461,call_5463,])
func_5489 = relay.Function([], output)
mod['func_5489'] = func_5489
mod = relay.transform.InferType()(mod)
output = func_5489()
func_5490 = relay.Function([], output)
mutated_mod['func_5490'] = func_5490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5184_call = mod.get_global_var('func_5184')
func_5186_call = mutated_mod.get_global_var('func_5186')
call_5516 = relay.TupleGetItem(func_5184_call(), 2)
call_5517 = relay.TupleGetItem(func_5186_call(), 2)
output = call_5516
output2 = call_5517
func_5518 = relay.Function([], output)
mod['func_5518'] = func_5518
mod = relay.transform.InferType()(mod)
mutated_mod['func_5518'] = func_5518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5518_call = mutated_mod.get_global_var('func_5518')
call_5519 = func_5518_call()
output = call_5519
func_5520 = relay.Function([], output)
mutated_mod['func_5520'] = func_5520
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5540 = relay.var("var_5540", dtype = "float32", shape = (15, 3, 4))#candidate|5540|(15, 3, 4)|var|float32
uop_5541 = relay.log10(var_5540.astype('float32')) # shape=(15, 3, 4)
func_5389_call = mod.get_global_var('func_5389')
func_5391_call = mutated_mod.get_global_var('func_5391')
call_5551 = relay.TupleGetItem(func_5389_call(), 2)
call_5552 = relay.TupleGetItem(func_5391_call(), 2)
func_1908_call = mod.get_global_var('func_1908')
func_1911_call = mutated_mod.get_global_var('func_1911')
const_5554 = relay.const([9.191023,9.327896,6.155708,8.015966,-5.290464,-3.371198,-3.202951,-7.206676,-4.025001,-2.511016,2.427286,-4.281027,9.984549,-5.019723,0.124266,7.422921,-7.230153,4.835525,-6.345303,7.826031,-5.477350,-3.608182,-3.455414,-2.682230,-3.319259,5.843712,-4.467624,4.256131,5.960562,-8.563809,8.756835,1.869656,5.373315,6.562507,8.074817,-4.983238,-7.005347,8.155553,7.710127,-0.320726,-0.029652,-8.086647,6.576297,-1.602375,1.345606,2.050210,-5.109585,3.722277,5.803001,-5.270800,2.238801,9.173532,0.636366,9.547500,-0.302139,-0.427341,8.402156,0.455842,8.802147,3.542556,7.061108,0.794233,-6.870547,3.931412,-1.410488,-7.508953,-6.415839,9.752772,-7.965529,-4.842154,-1.864145,7.884317,8.470749,-6.624335,-4.880816,-8.719060,4.418407,-9.384123,-0.564344,8.825990,1.103565,-5.474910,9.688562,0.701885,-8.303257,7.305988,7.463729,6.536644,1.813689,8.359883,0.963014,5.594237,7.772603,-4.390095,2.569609,-1.641703,-3.102812,-2.919674,1.391615,8.655026,-0.507512,-0.992784,-0.772911,-8.009865,-2.484370,6.506261,9.217162,-6.502192,-8.743889,-3.882068,-4.918656,-1.381577,-8.961246,1.926880,2.160014,7.752421,2.266573,0.738757,0.806375,0.005505,6.379877,-7.154066,-6.383580,3.248467,2.615614,-4.261515,4.577676,-9.373836,-4.017418,6.193018,9.301860,4.059636,-8.485552,-1.998215,-0.927242,8.565938,-0.749056,7.325312,-0.705033,-0.045799,-3.276417,-4.971467,9.561658,8.323556,-1.302577,4.804520,-3.663923,-6.913867,2.450991,-2.663430,-2.007973,4.264312,9.979507,1.042052,-4.462974,-7.802408,3.390795,-6.390479,6.816515,-6.492979,-1.286646,2.992421,-1.294240,8.386233,-9.962660,2.595968,-3.720221,-3.014200,6.322370,7.359772,9.252247,8.110089,-3.306087,9.120508,8.819837,9.431546,-2.404093,-6.072761,-2.458841,-7.605850,-5.805494,-1.519663,7.858118,-8.650855,-5.102233,-7.127271,0.143616,-2.806540,9.731182,-2.004780,3.702433,-4.635017,-8.384318,-0.303209,-6.113092,-8.433951,6.082045,4.006569,5.937159,2.479360,-0.745762,4.870854,4.213109,4.146297,7.608189,-4.663695,-5.071558,-6.654208,3.061606,9.567734,-7.338962,-2.249982,-0.703981,-8.740541,-3.521055,-7.948910], dtype = "float64")#candidate|5554|(216,)|const|float64
call_5553 = relay.TupleGetItem(func_1908_call(relay.reshape(const_5554.astype('float64'), [9, 4, 6])), 2)
call_5555 = relay.TupleGetItem(func_1911_call(relay.reshape(const_5554.astype('float64'), [9, 4, 6])), 2)
output = relay.Tuple([uop_5541,call_5551,call_5553,const_5554,])
output2 = relay.Tuple([uop_5541,call_5552,call_5555,const_5554,])
func_5569 = relay.Function([var_5540,], output)
mod['func_5569'] = func_5569
mod = relay.transform.InferType()(mod)
mutated_mod['func_5569'] = func_5569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5570 = relay.var("var_5570", dtype = "float32", shape = (15, 3, 4))#candidate|5570|(15, 3, 4)|var|float32
func_5569_call = mutated_mod.get_global_var('func_5569')
call_5571 = func_5569_call(var_5570)
output = call_5571
func_5572 = relay.Function([var_5570], output)
mutated_mod['func_5572'] = func_5572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2547_call = mod.get_global_var('func_2547')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_5640 = relay.TupleGetItem(func_2547_call(), 2)
call_5641 = relay.TupleGetItem(func_2549_call(), 2)
func_1388_call = mod.get_global_var('func_1388')
func_1389_call = mutated_mod.get_global_var('func_1389')
call_5655 = relay.TupleGetItem(func_1388_call(), 0)
call_5656 = relay.TupleGetItem(func_1389_call(), 0)
output = relay.Tuple([call_5640,call_5655,])
output2 = relay.Tuple([call_5641,call_5656,])
func_5692 = relay.Function([], output)
mod['func_5692'] = func_5692
mod = relay.transform.InferType()(mod)
mutated_mod['func_5692'] = func_5692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5692_call = mutated_mod.get_global_var('func_5692')
call_5693 = func_5692_call()
output = call_5693
func_5694 = relay.Function([], output)
mutated_mod['func_5694'] = func_5694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_5702 = func_4162_call()
call_5703 = func_4162_call()
const_5709 = relay.const([[-6.399092,9.142446,7.880800,-2.142769,1.706048,0.433288,5.769670,-6.935237,2.885378,-4.881182,-1.575483,-1.985290,-2.686184,-0.529694,-7.558947,8.490095,-8.053904,3.001942,-9.535071,5.287424,7.123691,-7.984473,-7.816961,5.727940,8.051879,-5.898336,9.768709,-7.312153],[4.869535,-9.994382,-1.578485,6.351860,-2.010102,-3.492005,-3.203745,-8.910547,-3.707002,3.709600,-8.686260,-2.422214,-4.167581,0.749847,1.144230,0.247296,-1.722882,-6.726737,3.711745,4.005742,-6.113229,-0.138328,2.042379,1.945353,-7.348000,6.046313,7.211481,-8.445036],[-0.085080,5.396958,1.725221,-2.496706,-1.555234,-1.292170,-6.928239,2.626317,1.825148,-9.880589,5.512167,0.354935,-3.057347,-1.083504,-6.646477,3.449989,-7.566270,6.957744,8.272179,0.230786,-4.470920,7.175496,2.126837,-0.721705,9.927756,-3.456930,-5.628103,-9.074820],[-2.694228,-2.726819,2.563359,5.355020,7.011733,5.416426,-8.318114,-3.906135,-1.480815,-0.313652,5.002898,-1.818334,6.018372,4.453645,-7.179698,-7.682718,-3.533373,-3.201375,-3.631934,6.478233,-4.174399,-8.722295,9.468611,3.943929,-6.485454,4.403874,-2.595753,-8.450233],[-4.191112,1.645008,2.278149,0.947228,7.120633,1.095069,5.972222,1.182008,5.813326,0.115074,-2.305849,-0.304745,-4.666338,-0.805214,-2.003188,-7.852374,-6.044293,1.788031,6.474960,8.685372,-4.308062,-8.569730,7.124808,5.483074,4.703007,7.169749,-4.047343,-4.796865],[-5.787561,7.330319,-3.885298,1.671637,-9.302773,-9.510321,-6.943693,-8.189081,5.332118,-6.179862,-4.931271,3.153521,-1.056871,5.185494,0.954842,9.014133,0.776547,-1.101352,-7.172663,-3.274618,-0.837728,-1.447591,8.835807,-6.698737,1.930383,7.430437,-3.759949,9.739682]], dtype = "float32")#candidate|5709|(6, 28)|const|float32
bop_5710 = relay.divide(call_5702.astype('float32'), relay.reshape(const_5709.astype('float32'), relay.shape_of(call_5702))) # shape=(6, 28)
bop_5713 = relay.divide(call_5703.astype('float32'), relay.reshape(const_5709.astype('float32'), relay.shape_of(call_5703))) # shape=(6, 28)
output = bop_5710
output2 = bop_5713
func_5717 = relay.Function([], output)
mod['func_5717'] = func_5717
mod = relay.transform.InferType()(mod)
mutated_mod['func_5717'] = func_5717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5717_call = mutated_mod.get_global_var('func_5717')
call_5718 = func_5717_call()
output = call_5718
func_5719 = relay.Function([], output)
mutated_mod['func_5719'] = func_5719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_55_call = mod.get_global_var('func_55')
func_56_call = mutated_mod.get_global_var('func_56')
call_5727 = relay.TupleGetItem(func_55_call(), 0)
call_5728 = relay.TupleGetItem(func_56_call(), 0)
func_2118_call = mod.get_global_var('func_2118')
func_2120_call = mutated_mod.get_global_var('func_2120')
call_5796 = func_2118_call()
call_5797 = func_2118_call()
output = relay.Tuple([call_5727,call_5796,])
output2 = relay.Tuple([call_5728,call_5797,])
func_5798 = relay.Function([], output)
mod['func_5798'] = func_5798
mod = relay.transform.InferType()(mod)
mutated_mod['func_5798'] = func_5798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5798_call = mutated_mod.get_global_var('func_5798')
call_5799 = func_5798_call()
output = call_5799
func_5800 = relay.Function([], output)
mutated_mod['func_5800'] = func_5800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3662_call = mod.get_global_var('func_3662')
func_3663_call = mutated_mod.get_global_var('func_3663')
call_5881 = relay.TupleGetItem(func_3662_call(), 0)
call_5882 = relay.TupleGetItem(func_3663_call(), 0)
output = call_5881
output2 = call_5882
func_5886 = relay.Function([], output)
mod['func_5886'] = func_5886
mod = relay.transform.InferType()(mod)
output = func_5886()
func_5887 = relay.Function([], output)
mutated_mod['func_5887'] = func_5887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5798_call = mod.get_global_var('func_5798')
func_5800_call = mutated_mod.get_global_var('func_5800')
call_5903 = relay.TupleGetItem(func_5798_call(), 1)
call_5904 = relay.TupleGetItem(func_5800_call(), 1)
output = relay.Tuple([call_5903,])
output2 = relay.Tuple([call_5904,])
func_5910 = relay.Function([], output)
mod['func_5910'] = func_5910
mod = relay.transform.InferType()(mod)
mutated_mod['func_5910'] = func_5910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5910_call = mutated_mod.get_global_var('func_5910')
call_5911 = func_5910_call()
output = call_5911
func_5912 = relay.Function([], output)
mutated_mod['func_5912'] = func_5912
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5976 = relay.var("var_5976", dtype = "bool", shape = (16, 4, 2))#candidate|5976|(16, 4, 2)|var|bool
var_5977 = relay.var("var_5977", dtype = "bool", shape = (16, 4, 2))#candidate|5977|(16, 4, 2)|var|bool
bop_5978 = relay.logical_or(var_5976.astype('bool'), relay.reshape(var_5977.astype('bool'), relay.shape_of(var_5976))) # shape=(16, 4, 2)
output = relay.Tuple([bop_5978,])
output2 = relay.Tuple([bop_5978,])
func_5985 = relay.Function([var_5976,var_5977,], output)
mod['func_5985'] = func_5985
mod = relay.transform.InferType()(mod)
var_5986 = relay.var("var_5986", dtype = "bool", shape = (16, 4, 2))#candidate|5986|(16, 4, 2)|var|bool
var_5987 = relay.var("var_5987", dtype = "bool", shape = (16, 4, 2))#candidate|5987|(16, 4, 2)|var|bool
output = func_5985(var_5986,var_5987,)
func_5988 = relay.Function([var_5986,var_5987,], output)
mutated_mod['func_5988'] = func_5988
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6008 = relay.var("var_6008", dtype = "float64", shape = (10, 3, 13))#candidate|6008|(10, 3, 13)|var|float64
var_6009 = relay.var("var_6009", dtype = "float64", shape = (10, 3, 13))#candidate|6009|(10, 3, 13)|var|float64
bop_6010 = relay.mod(var_6008.astype('float64'), relay.reshape(var_6009.astype('float64'), relay.shape_of(var_6008))) # shape=(10, 3, 13)
func_1908_call = mod.get_global_var('func_1908')
func_1911_call = mutated_mod.get_global_var('func_1911')
var_6014 = relay.var("var_6014", dtype = "float64", shape = (12, 18))#candidate|6014|(12, 18)|var|float64
call_6013 = relay.TupleGetItem(func_1908_call(relay.reshape(var_6014.astype('float64'), [9, 4, 6])), 2)
call_6015 = relay.TupleGetItem(func_1911_call(relay.reshape(var_6014.astype('float64'), [9, 4, 6])), 2)
output = relay.Tuple([bop_6010,call_6013,var_6014,])
output2 = relay.Tuple([bop_6010,call_6015,var_6014,])
func_6018 = relay.Function([var_6008,var_6009,var_6014,], output)
mod['func_6018'] = func_6018
mod = relay.transform.InferType()(mod)
var_6019 = relay.var("var_6019", dtype = "float64", shape = (10, 3, 13))#candidate|6019|(10, 3, 13)|var|float64
var_6020 = relay.var("var_6020", dtype = "float64", shape = (10, 3, 13))#candidate|6020|(10, 3, 13)|var|float64
var_6021 = relay.var("var_6021", dtype = "float64", shape = (12, 18))#candidate|6021|(12, 18)|var|float64
output = func_6018(var_6019,var_6020,var_6021,)
func_6022 = relay.Function([var_6019,var_6020,var_6021,], output)
mutated_mod['func_6022'] = func_6022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2668_call = mod.get_global_var('func_2668')
func_2669_call = mutated_mod.get_global_var('func_2669')
call_6024 = func_2668_call()
call_6025 = func_2668_call()
func_2871_call = mod.get_global_var('func_2871')
func_2873_call = mutated_mod.get_global_var('func_2873')
call_6026 = func_2871_call()
call_6027 = func_2871_call()
func_1210_call = mod.get_global_var('func_1210')
func_1214_call = mutated_mod.get_global_var('func_1214')
const_6056 = relay.const([[9.612446,-3.704011,-2.295804,-2.203486,-3.456888,4.412479,8.571002,3.360668,-2.876042,-2.152605,-3.664989,7.160512,-9.140410,7.967788,-3.666548,8.993997,-8.360469,-7.308736,1.262559,-3.715753,-8.347930,-0.818723,8.490286,-4.108119,-0.057426,-2.511414,-5.985876,-1.938883,-4.557078,8.836775,3.600503,-4.046384,3.256215,9.437983,-9.722752,-4.839463,7.978518,-1.100668,8.027674,-1.044960,7.706865,-5.119324,6.912463,-9.662272,8.605082,-6.530514,-0.489954,-6.665049,7.006883,-5.759681,-9.662293,-7.504706,9.647479,-6.269522,-6.135387,-0.403106,-6.467510,1.772836,7.038894,9.984314],[-3.943603,-9.448272,5.056639,-5.627918,-9.067379,-8.204478,6.963397,-5.270447,3.700377,9.013615,8.216318,9.397548,3.978709,1.081765,-7.687172,7.100651,-4.668368,8.286445,-4.232980,4.214397,-9.500342,6.337297,-9.345880,-6.874364,8.202330,7.096808,4.941920,-3.242810,-5.209001,0.148901,-4.941320,0.933877,-3.119771,-6.633550,-2.729682,1.573520,9.684844,-1.624625,-8.769450,2.995962,0.901359,1.008123,1.789401,3.903196,6.340043,-4.093649,1.455338,0.815052,-6.605606,-9.573316,5.982750,4.344554,0.327251,-1.167115,-4.523505,0.280168,5.308322,-1.751074,-4.946312,-9.512913],[1.135712,4.375064,-7.551057,-4.756604,4.007899,1.531789,4.081511,9.256722,-5.630839,-4.302291,-1.409355,-9.934634,-5.098286,-7.197042,-2.696284,3.473043,-1.315246,-0.862464,6.866629,4.118728,-5.434673,7.383748,-0.234860,-3.561187,-5.872774,9.412225,-2.713853,-9.908884,5.462649,4.809250,3.470730,8.367838,9.916316,-2.394803,-8.599822,3.398881,-4.626074,-5.642319,-2.613547,-9.569283,-2.629002,3.290003,9.766060,8.257532,-7.442361,8.884658,3.562604,2.953679,-7.631393,1.268537,-8.947761,8.201375,7.575636,2.918656,-8.923798,2.157595,2.436063,7.614792,-6.792212,1.692626],[6.384376,1.439406,4.825330,-6.989695,-5.615948,7.176772,-6.298925,-5.301269,-7.856343,6.151205,5.193990,0.410324,8.257268,2.077259,-5.533669,2.283899,8.800746,-8.739023,4.177952,5.208196,6.808859,-7.621124,0.199146,9.781512,-5.898902,1.454485,6.881735,3.535847,1.938877,5.300085,8.609857,-7.587616,6.867808,-4.025932,3.697155,-2.701601,-1.562575,-0.528806,5.859978,0.936610,5.600357,4.714795,-9.076081,6.714999,-9.981221,6.267500,5.918174,-4.461781,-1.440005,-2.873672,-9.355060,-1.780512,9.600254,6.185980,8.161652,5.389283,6.845404,1.765174,3.259952,8.452502],[6.604160,3.166859,-2.310985,6.017615,-5.507815,-1.295280,6.423968,8.321072,-9.052855,1.504997,-8.073396,-1.934037,-3.997090,3.778345,-8.517298,3.486653,7.487974,8.011247,-4.122896,-1.043176,-6.832413,-0.903390,-1.869241,-1.917428,-1.863179,-3.074947,-7.255261,-1.550190,-9.234015,-3.443438,-4.417643,3.256229,3.788818,-1.885880,7.825644,-0.290087,1.553835,1.933732,4.924094,-5.858357,-2.539529,-1.181313,9.408909,5.397515,-1.259472,8.488469,6.620343,-9.683345,0.889976,-7.355972,3.211729,-8.817443,9.650394,-5.027202,5.000716,-4.227526,6.078554,7.443880,2.296596,9.323560],[-8.406603,8.347917,8.812981,-5.635791,-2.136588,1.813443,-6.630310,-5.592531,-3.842056,-1.943533,-2.734253,8.456798,9.308865,-5.032977,5.980609,-6.822232,-7.447048,1.363862,3.922677,-7.624096,-8.998419,6.958207,6.108045,0.171023,6.921044,-4.758876,-1.477869,9.383840,-3.399100,3.684375,9.848250,1.820049,2.427192,3.603268,7.758593,-8.602401,-4.431245,-1.483090,6.099102,4.408113,0.840931,-0.699302,3.429551,5.798679,-3.656526,0.938548,-2.016512,9.322355,4.287642,-6.148438,6.045003,-4.031215,-3.825008,4.410083,-6.032121,-7.482949,-8.014703,-5.262467,3.936685,2.925294],[-0.876494,5.450663,-6.116103,-7.693924,-0.732248,-6.245521,1.759445,5.482100,7.830360,8.279071,4.758973,5.431940,7.302847,5.616861,5.821086,-8.373040,1.179460,-4.937356,-9.855590,3.986219,8.258328,-2.137324,-9.039498,-3.813493,2.444462,-9.433614,-6.438413,-2.009486,4.961629,-5.137671,4.478273,-5.693826,-8.090633,-9.264156,7.775789,9.137041,2.476576,9.725900,0.852315,8.525684,4.860303,6.830955,8.959407,5.841317,2.311790,2.766638,-0.128624,3.926300,-9.508443,-0.289881,1.586992,-1.427460,5.621528,6.408745,4.413548,5.817311,-1.963545,-5.157297,2.570839,-5.001472],[9.643423,9.953556,1.101102,3.256704,-3.807072,8.582343,0.017669,-1.395103,6.471585,-4.571456,-8.735277,2.026294,-8.939821,-5.739097,-8.530206,2.874983,-2.447984,8.726418,2.789710,4.043197,-8.397687,-8.120881,-5.320040,5.955787,-9.005079,-4.418665,8.714363,7.073079,-4.469586,4.470768,-0.571595,-9.005344,7.599874,-8.319887,-6.537417,-6.082099,-0.173661,7.027588,9.711084,-4.053707,-5.929633,-9.893322,-9.900154,9.689556,6.483195,2.231069,1.292954,-4.473739,-4.278238,-8.108887,-6.958452,2.582425,4.644323,4.893090,8.652385,-4.917550,1.530547,-8.420983,-5.238515,-2.668968],[-8.175806,9.027379,5.017905,2.735518,-6.951948,6.852489,-1.774858,3.398971,5.542827,8.551986,-9.398671,-2.960942,-7.023230,4.998555,-1.693169,4.806026,-9.277805,8.453292,-1.517375,5.190716,-6.916992,-6.266150,5.688388,-7.366011,-2.919465,-4.463477,0.725729,-3.797473,6.921010,-4.651105,8.127439,-9.751138,-3.275847,-3.796608,-4.833824,6.402034,-4.255968,-9.469930,5.432834,-8.474588,-8.148765,-8.539618,6.166599,4.807067,-6.841157,-8.994629,7.385812,5.041470,-6.286621,3.161179,2.878214,4.396614,-5.793405,-2.765485,-1.285330,5.096545,9.696475,-0.931497,6.157493,9.935460],[1.076861,7.512875,-3.671225,-9.536641,-9.751966,-4.047373,-1.366408,1.311388,8.056413,-1.469367,-4.415954,-3.083050,3.469792,-8.599927,-9.207356,2.311117,-1.730417,4.754162,3.953619,1.391322,0.652563,-4.284484,-4.077562,-0.279462,6.946315,0.337819,-4.157545,4.066314,2.281393,-1.486547,1.726852,8.742962,4.966325,-0.438068,7.424082,-5.939080,8.469914,-5.920316,2.727554,4.977297,-0.909652,-6.578752,-2.731892,-8.604237,-3.297951,-0.533473,-8.082273,5.966676,-1.658190,9.827414,5.677072,-1.840664,-1.675274,-3.381897,3.160456,-5.129813,1.553789,-1.449282,-1.424348,4.315467],[-0.813361,-7.741168,1.997928,-0.130943,9.669223,4.459634,8.928482,-8.094536,9.534728,4.636407,-0.381518,-4.936889,1.401437,-5.247564,2.166644,-9.461741,6.569778,8.625135,-2.738241,-7.810448,5.403698,-4.695961,8.781258,-0.236292,-6.592488,8.961597,2.128233,-0.059773,-7.606529,-1.238031,-9.858267,1.398428,7.701440,-9.157284,-8.173577,4.147239,0.248274,7.274937,-9.625423,8.630772,2.464063,-8.400340,-9.867376,3.507356,7.747816,-0.595527,-6.496963,9.530023,-1.060705,9.042100,-8.408755,-2.684585,0.701861,-3.011234,6.291676,-1.989027,-1.260670,6.478831,1.354263,0.460999],[-7.431924,-7.532622,-8.854860,-1.621733,6.195736,0.454771,6.471194,4.370680,0.419122,-9.127093,2.739160,-5.309496,2.810866,-9.896234,-8.827156,2.186573,-7.830358,-6.799342,9.441547,6.455541,-0.223700,-6.583264,0.736021,-6.748097,3.289569,0.759095,1.769989,-6.521301,-8.036336,8.693433,1.698653,5.031692,-9.917536,-6.835995,1.210711,4.045986,-1.592544,5.811961,9.287173,5.711543,-5.717030,-4.067586,-1.329710,7.789395,4.060834,9.512685,3.790826,-0.324459,-5.840935,-9.163917,6.648380,-0.901244,2.828045,5.095385,5.746082,-8.672085,5.791316,-7.483634,6.990192,-9.867734],[-9.636951,9.241223,5.483414,-7.905668,-7.342768,0.807232,-1.946299,-5.780684,9.370094,-5.405311,-5.103666,-6.363386,0.309119,6.609524,-2.519338,-5.630144,9.410419,6.783315,2.773470,4.072958,-6.976998,4.682429,-7.760957,-1.136543,3.441162,-6.666971,8.296351,-7.682210,7.671420,-1.359897,6.025330,0.593794,-1.993702,6.259206,-6.327910,-6.336367,1.472838,3.674174,9.561019,3.442211,-5.651747,-5.260444,0.532368,1.412482,-9.778621,-3.628942,-4.886092,-0.931388,-3.405087,-1.005710,-9.060329,4.725082,2.211103,1.661713,9.324328,6.124291,0.320746,0.414701,-3.342739,1.635073],[-0.035856,1.402571,7.861270,-5.610208,0.046865,-0.883461,9.669815,-4.391264,-6.676043,2.287325,-4.084957,-8.865255,-9.018634,-4.281345,-6.171949,1.590630,-4.758897,5.978787,-8.495659,3.367867,-4.773070,-2.501307,-3.237205,-6.796002,-7.925481,-5.633015,1.748949,-4.465433,-9.445612,-4.496051,2.196945,-2.745645,-1.480492,7.789980,2.795123,6.531701,7.509599,3.319992,-1.709447,-2.619138,3.868928,1.507932,3.679568,-9.742717,8.381256,-3.098818,-0.550464,-1.051849,-5.166042,5.345933,-8.373623,-7.791361,-6.121439,0.915983,6.481807,-4.710734,-9.829790,2.706410,8.880729,-4.969531],[9.651315,0.358591,4.305177,-3.408944,-1.913144,0.620588,-9.238598,-5.330087,7.467761,6.702108,2.479334,6.500924,-1.681168,-6.574148,-6.255857,-2.216144,1.100868,5.352393,2.704272,6.960764,4.561105,-3.903533,-1.831138,1.223584,4.739865,-2.162129,-8.547997,-5.936711,1.379108,-6.160664,3.149657,5.543132,3.611506,1.522013,-3.411885,-4.874803,9.478881,-7.182476,3.677969,1.669109,-3.328956,5.115315,9.374148,9.081933,-6.090998,-9.534678,-1.072554,3.901634,-0.343727,-4.438895,6.747269,9.618347,-1.441747,-8.219709,5.478948,-3.097194,1.894600,-9.789871,7.702177,7.982639],[3.552400,-2.085237,6.750300,0.926934,-4.561851,6.070325,-7.591687,8.534073,-9.904485,-9.806054,4.482028,1.933380,6.375010,-1.976434,-1.162693,-4.129358,4.559123,0.192156,-6.156642,8.785930,2.642359,-3.944419,0.316766,-3.169734,6.326058,7.172158,9.397867,-5.903987,-4.351499,5.258309,-6.606607,-5.594791,-8.205146,1.878346,5.824403,-3.239415,0.007824,-4.923953,-0.279219,-1.044864,-8.690867,-8.959924,-0.294571,-4.427282,5.271633,7.658189,9.817863,-5.573410,-3.785739,3.227808,-2.998873,-4.784758,-1.236640,-8.239127,3.917487,2.668996,-2.981794,4.012426,-2.387476,4.454934],[8.530397,4.824160,-6.821361,6.737509,4.642081,-4.741369,-1.003466,2.160318,-5.891240,6.370471,-6.229226,3.411639,-7.763163,-0.417484,-5.568488,4.994950,-3.219452,-9.880607,-3.841644,4.664956,-9.280904,1.227747,-8.694289,-7.875504,-6.681160,-3.740388,-5.425479,5.795297,-4.475970,3.557929,5.942237,0.262344,6.874570,-4.984350,5.867949,-9.728068,-6.489664,-6.275261,-1.391977,3.733736,-7.409283,-9.286135,5.148167,8.901428,5.035760,-8.764775,8.530771,-7.035749,3.342121,-6.877794,3.505217,0.109660,-3.602059,-7.264841,-4.351722,1.689302,-1.288690,7.029578,5.532797,8.495525],[3.139625,5.953890,2.471762,1.494064,6.165202,1.894827,-0.645070,-3.118760,-5.026548,-6.322428,-5.149261,6.758549,1.588162,-8.440530,-5.198098,3.423668,9.971383,-7.083555,-3.820523,0.322767,-4.428028,-2.507056,7.539197,6.484218,-1.147863,-6.877296,-5.625201,2.794658,-4.061575,-5.555208,0.054970,-6.078479,5.579365,-0.657384,5.229938,3.162037,-7.145691,-9.789882,-9.342054,-3.581206,2.651673,3.802735,-0.180547,4.755417,-5.270592,7.440453,1.770580,-6.675507,1.295728,6.926687,-3.115522,-8.634851,-2.176640,1.687678,-3.140580,0.612281,-1.135164,7.430488,1.309194,-7.168616]], dtype = "float64")#candidate|6056|(18, 60)|const|float64
call_6055 = relay.TupleGetItem(func_1210_call(relay.reshape(const_6056.astype('float64'), [9, 12, 10]), relay.reshape(const_6056.astype('float64'), [9, 12, 10]), ), 2)
call_6057 = relay.TupleGetItem(func_1214_call(relay.reshape(const_6056.astype('float64'), [9, 12, 10]), relay.reshape(const_6056.astype('float64'), [9, 12, 10]), ), 2)
func_2748_call = mod.get_global_var('func_2748')
func_2752_call = mutated_mod.get_global_var('func_2752')
const_6076 = relay.const([[-0.165039],[4.016913],[2.389102],[6.499063],[-8.430497],[4.294895],[4.655298],[-1.052896],[-9.455616],[3.676682],[-6.517089],[-3.335529],[-1.055566],[4.427786],[-2.904204],[-6.106735],[-2.859770],[5.980132],[8.663392],[-0.773542],[-6.891416],[-9.276415],[9.415433],[-1.360600],[-4.163648],[-2.265859],[1.451483],[-3.101438],[2.098129],[-7.396611],[-1.046031],[-0.780272],[6.609858],[-7.215425],[-3.253725],[-3.823418],[-0.896932],[-7.694754],[1.314128],[3.265794],[8.193496],[-5.170996],[5.145917],[-6.284931],[9.300040],[-9.551498],[2.871024],[-5.754060],[-8.432751],[-9.462663],[4.340133],[5.938855],[5.185890],[2.819090],[-1.594935],[-1.873960],[7.961911],[-0.219929],[9.139254],[3.656333],[4.346198],[-2.786382],[-5.114876],[0.729990],[6.775851],[5.719492],[1.895794],[5.645419],[8.580088],[6.132618],[5.587008],[7.178243],[9.069213],[1.772851],[-3.593030],[5.073091],[-9.237156],[6.423703],[-2.843957],[3.847001],[-0.615378],[-5.303862],[8.504069],[-4.160319],[-3.182663],[-5.836602],[5.768469],[-5.454944],[3.599490],[6.762849],[-4.816410],[-8.748347],[-2.581939],[6.848596],[-2.115204],[-6.672413],[-1.127563],[-6.505549],[-6.267719],[-0.054095],[3.177182],[2.762756],[-2.421104],[6.758736],[4.584360],[7.804824],[0.831118],[2.636412],[8.342234],[-1.554595],[5.877739],[-0.286009],[4.427973],[-3.553055],[3.706001],[-1.363178],[6.647074],[8.632569],[-7.214426],[-0.141708],[5.986629],[0.123994],[5.813309],[-7.655956],[-6.439292],[-5.074332],[-5.714201],[1.075700],[-5.045486],[4.361736],[-9.157062],[-0.284103],[6.444261],[3.928068],[-8.268989],[-8.828184],[0.139830],[-0.707407],[-2.260886],[-0.216993],[1.056714],[-5.740392],[3.231339],[3.483310],[1.024945],[-3.439183],[-4.942534],[-9.374058],[-2.911793],[6.266759],[9.858655],[8.133381],[-9.650624],[3.306505],[-3.725248],[3.561649],[-9.830387],[6.479204],[2.103033],[4.916766],[-6.127385],[-3.575090],[-6.732980],[-5.514893],[-2.046583],[6.898770],[0.628899],[-2.525781],[-8.806478],[-3.823359],[9.604151],[-5.089927],[-7.666222],[-6.793809],[-6.294637],[-9.870064],[3.142285],[-1.358655],[3.406840],[-4.558004],[-6.023011],[4.465072],[-7.775713],[9.736282],[9.624769],[-1.676971],[2.329787],[1.986844],[-0.122557],[7.904205],[4.453767],[2.359523],[-3.069073],[3.940392],[3.381093],[7.383981],[9.723474],[1.567520],[7.858837],[5.529691],[6.485415],[4.233835],[-1.602826],[-4.502594],[-8.979776],[-1.853376],[2.802412],[-5.304949],[6.030700],[-1.792154],[-7.871312],[-9.354718],[-2.602288],[1.047094],[7.720837],[0.859957],[-5.582313],[8.700521],[5.426070],[-0.103238],[-0.553138],[9.613699],[-9.525522],[5.246268],[6.646022],[-0.140319],[-1.792657],[-2.007604],[2.521521],[-8.402750],[-0.766912],[4.678472],[-1.773946],[9.143499],[-5.334774],[-0.138107],[-8.534528],[-3.295295],[3.729277],[-4.877415],[2.800371],[-8.689916],[-2.043223],[9.342674],[7.168417],[-6.789256],[3.926359],[-3.985633],[-4.084730],[0.918781],[4.427159],[4.146618],[7.457567],[1.999868],[-4.961594],[-4.379608],[-1.933490],[8.459344],[3.610377],[-7.450615],[-6.273740],[-2.575602],[-4.100916],[3.837224],[-8.498387],[0.451303],[-3.321135],[-7.699929],[2.358791],[1.933403],[5.967581],[9.206706],[-8.124860],[-4.654569],[4.360367],[-7.297070],[2.982219],[5.051522],[-3.049296],[6.772500],[1.282803],[-4.806381],[4.514361],[-6.882479],[-3.587346],[-4.151077],[0.976035],[-6.055059],[-7.393880],[4.590493],[9.071342],[3.370931],[-8.957529],[4.411570],[-3.941155],[9.640111],[6.036300],[0.049755],[-8.868558],[1.667407],[7.571167],[2.865273],[-2.240304],[1.425966],[-2.922267],[-8.214596],[-6.558828],[3.039167],[0.183047],[2.146952],[3.043383],[5.511310],[3.489275],[9.875977],[-1.033683],[-6.399000],[2.464665],[-4.290201],[3.755227],[-9.347394],[-3.069260],[-0.304846],[9.679073],[3.366840],[-4.268594],[-4.484692],[-7.929664],[-6.983606],[-2.984918],[2.493111],[1.348547],[5.889025],[8.933227],[-1.526195],[8.422000],[4.213778],[9.510559],[-1.006565],[0.141650],[4.887976],[6.278937],[4.747568],[-1.411348],[1.204161],[5.589272],[8.679950],[-5.505344],[9.587430],[9.820563],[7.769967],[7.807245],[-4.422125],[-7.393113],[5.987913],[5.847612],[9.391209],[-3.810881],[-8.658509],[-5.355228],[5.391265],[-4.329422],[-3.191767],[6.333149],[1.559015],[4.867691],[5.362625],[3.006699],[-6.433116],[5.889763],[9.189491],[-4.755224],[5.813432],[5.713444],[3.103218],[2.464659],[6.321266],[-2.694788],[-9.393423],[-4.437188],[-3.175189],[-4.154632],[-8.437784],[3.097139],[3.629165],[-1.217488],[8.719489],[7.283998],[9.663655],[-7.366659],[5.447613],[0.433274],[-2.192931],[-7.796103],[-6.917085],[-2.514264],[5.726958],[-6.884037],[-1.032190],[-2.684373],[-7.327084],[-2.515737],[1.186930],[-5.077498],[-7.382186],[-4.906679],[-2.990161],[-6.148530],[6.182149],[-2.089431],[2.719235],[-3.416576],[6.095652],[-8.877664],[-8.118889],[-2.471790],[5.851889],[5.296491],[-3.213224],[3.865887],[-9.452775],[-1.242234],[-7.502165],[0.385079],[-7.890308],[3.231670],[-1.851607],[-8.048790],[-8.288434],[8.287451],[8.353467],[-9.722393],[-8.743719],[4.791817],[2.372150],[0.881116],[-0.425647],[8.711611],[2.961927],[-0.415910],[-9.356561],[5.460006],[1.233833],[-8.169745],[6.222017],[9.237057],[2.895560],[2.407852],[4.469146],[3.770740],[-4.910229],[-1.377388],[-3.523246],[0.254352],[6.948287],[3.425084],[8.543552],[-2.943487],[-5.086712],[-5.267397],[8.601609],[-0.470246],[3.173882],[-7.746809],[7.972395],[-9.875722],[5.303689],[-2.757081],[-1.826007],[3.484044],[-4.021159],[4.064586],[7.060976],[-9.718122],[-1.333730],[9.688548],[-9.762207],[8.968840],[-5.645752],[-0.668546],[1.632971],[6.346817],[-1.588233],[-1.111913],[9.667614],[-3.682401],[7.886965],[4.683225],[1.978612],[-8.589812],[-4.378758],[6.913453],[-9.727119],[7.503512],[2.958677],[-9.059748],[-1.649647],[4.943329],[9.309058],[5.997845],[6.597826],[-8.746643],[2.848248],[6.849836],[-8.982608],[-3.873251],[-6.486838],[3.716580],[-8.636666],[1.568329],[1.653445],[-3.179916],[4.940267],[-4.392788],[-8.203913],[8.808969],[4.869306],[-5.623648],[3.186631],[7.173691],[9.710786],[-8.336182],[-8.829051],[-2.055298],[-3.394511],[-7.565663],[6.579346],[8.224952],[-8.829344],[-8.412784],[0.383309],[-4.864051],[8.048309],[4.566139],[-5.386105],[-1.171241],[3.321229],[1.123215],[9.373826],[-5.439370],[0.637161],[6.712158],[-6.255202],[5.144332],[-3.835988],[8.011585],[7.415873],[-7.236304],[-1.998320],[7.400049],[-7.563049],[-6.195859],[8.207848],[9.870616],[-5.810272],[-6.973444],[-8.956278],[-1.141895],[6.551185],[0.268300],[0.552836],[7.023762],[-7.813579],[-8.758194],[-4.301776],[-3.330005],[5.775375],[-4.895158],[-3.151882],[4.254055],[4.559052],[6.402257],[6.818617],[-3.030176],[8.870744],[-1.016758],[-6.796951],[-3.021004],[8.378195],[6.184765],[-4.561897],[1.052565],[5.044887],[-9.152604],[5.953949],[-2.929765],[-0.079817],[7.163018],[1.350771],[-5.679751],[0.628856],[-0.296304],[-8.836550],[1.943257],[9.408147],[5.908915],[-6.922275],[5.910106],[-3.976107],[8.596230],[-2.001476],[0.980093],[0.782539],[-9.929627],[-7.961493],[-6.956355],[-1.697602],[-2.232071],[1.505092],[-6.206781],[-3.029192],[-8.270890],[-4.947971],[-3.999359],[-9.487586],[6.871115],[7.591104],[5.358227],[7.749314],[-0.953390],[-9.093328],[1.108431],[2.200529],[3.373886],[6.646675],[6.216888],[-6.740541],[-4.148166],[4.823680],[6.380858],[3.744781],[-8.985313],[4.847249],[6.384659],[-3.841869],[4.783480],[-6.363208],[0.435091],[-8.746691],[-0.385851],[-4.872124],[1.839714],[-3.548357],[-5.447648],[7.129913],[5.219071],[-8.078260],[8.762707],[5.485674],[-8.362704],[-7.950679],[-4.102597],[-2.395430],[-9.931031],[-4.327941],[5.474280],[-7.664133],[0.439001],[-0.581928],[2.452518],[-8.364447],[-7.267865],[-6.603008],[-7.933157],[5.145926],[2.999975],[-5.600857],[-2.990346],[9.219787],[3.328205],[-9.819533],[4.188763],[-4.650304],[3.086526],[-7.538433],[-4.948685],[8.060384],[3.501991],[-9.476618],[3.559444],[-9.990960],[-1.695746],[-7.910531],[7.621047],[4.901366],[7.023968],[8.004945],[9.153262],[-8.029142],[7.979778],[7.376397],[0.256777],[-7.257267],[-2.514947],[-0.339041],[-4.267334],[4.724321],[-4.693084],[-0.682815],[2.984559],[-5.261655],[5.558455],[5.923151],[3.829958],[2.195563],[-5.352038],[-4.000081],[0.477168],[-6.807692],[-5.601513],[5.478801],[9.926905],[5.288033],[-5.713446],[-0.466345],[5.859277],[-6.376781],[-4.920741],[7.269900],[3.860483],[-1.014838],[6.807303],[1.721256],[-5.525499],[9.832022],[0.042769],[7.727623],[8.594173],[-9.174375],[-1.397312],[5.868008],[4.594776],[-8.884488],[-6.863097],[-6.114849],[-0.249463],[2.804848],[1.732274],[-8.424667],[2.805869],[-1.304385],[-8.049281],[3.438332],[-0.081813],[3.911058],[-3.588051],[2.718318],[0.960818],[-8.451023],[0.346953],[1.224537],[3.231845],[-2.009719],[-5.955769],[-2.242848],[-8.219825],[-6.508829],[9.971492],[-3.861395],[4.289221],[-9.968999],[-2.506725],[6.417686],[-7.163279],[8.515935],[-5.911697],[8.264371],[-2.593958],[0.357501],[5.615931],[-5.457509],[-1.322853],[-7.563414],[-6.726208],[-1.575056],[1.343372],[-6.696377],[-4.659132],[0.769523],[5.817021],[-5.583774],[7.846448],[9.378998],[2.039600],[-5.084960],[8.727608],[-6.791856],[1.619518],[6.218845],[7.751420],[7.505229],[-7.913678],[0.472525],[-2.398699],[2.614304],[8.838091],[1.744715],[-3.221808],[-2.699679],[7.608468],[-3.498050],[3.424625],[1.755440],[4.808350],[4.803026],[-0.650748],[0.159351],[-9.189829],[0.338056],[6.569153],[-7.673161],[-5.665672],[-9.178638],[-9.479734],[4.137380],[5.133283],[-7.384792],[-2.301347],[-9.431549],[-9.951912],[5.586691],[-8.964481],[-6.753874],[9.092862],[8.455938],[-4.895153],[8.625356],[-9.138113],[2.669304],[3.151537],[-1.157861],[-4.731123],[0.487604],[-1.297920],[1.478859],[0.520069],[1.595774],[8.163745],[-1.654935],[8.763747],[-4.069377],[0.942298],[1.652715],[3.903834],[3.959784],[5.970508],[6.480566],[-5.503535],[-1.251324],[-3.493135],[-8.455203],[-1.040294],[-3.050428],[9.800102],[-9.621306],[-7.166540],[-0.007172],[9.187590],[7.341620],[0.005209],[8.846720],[2.916035],[-2.690519],[0.747550],[-2.887898],[-2.705106],[-6.607345],[4.994934],[4.366517],[2.214692],[7.945330],[-8.269097],[-2.492998],[0.306198],[-2.824818],[-5.384167],[3.897804],[-2.871851],[3.957704],[6.295628],[-4.130349],[-0.899437],[-8.278793],[9.887797],[-4.819938],[-6.864750],[-6.799269],[-7.033200],[-4.342146],[2.870940],[-9.231360],[-2.214877],[4.141721],[0.762875],[-3.800136],[-1.260307],[1.417319],[4.851222],[-9.469660],[8.745479],[-8.771981],[6.997121],[-8.497029],[9.695797],[9.547609],[0.766269],[-4.232987],[-3.924816],[-1.499941],[-4.548194],[-0.402651],[5.279935],[-2.900651],[3.844807],[7.679751],[6.942414],[-8.298159],[3.889145],[-0.857768],[8.085981],[8.261164],[2.552683],[-0.867115],[5.363140],[-0.448681],[-5.007552],[-6.530556],[-6.967075],[-9.942573],[-8.741304],[-4.241819],[5.738867],[-8.073825],[8.017464],[4.344948],[-4.539713],[0.192141],[-5.069023],[7.945190],[-9.535107],[-6.279725],[-4.786728],[9.650714],[2.760463],[6.610174],[4.548363],[6.624299],[-5.559460],[0.541690],[8.989930],[0.756974],[4.464740],[1.165020],[-3.285646],[5.818733],[-1.872081],[5.010153],[5.212516],[0.600462],[8.675161],[-9.199565],[-1.285204],[4.122522],[8.735686],[-7.868439],[-9.027667],[-6.537581],[-5.292194],[9.049743],[9.357574],[-8.305848],[-8.123716],[-2.132517],[-9.184694],[-9.554374],[-0.491023],[-3.820273],[5.153976],[-6.673938],[3.418956],[3.186204],[-5.845179],[0.546275],[2.466179],[8.774263],[-9.663970],[5.323116],[-2.159139],[-0.116258],[3.469732],[-2.937615],[7.215169],[3.536136],[-3.889253],[4.158808],[-9.233486],[4.331560],[-5.478719],[-3.169983],[-9.296685],[-4.167753],[2.147243],[2.743548],[-4.402229],[-4.066802],[4.708144],[6.570959],[7.752593],[0.746839],[-4.159982],[0.287917],[5.674930],[2.998633],[-1.161315],[7.631430],[-4.212554],[6.446206],[2.297057],[1.949464],[-9.638986],[-0.928263],[-9.314463],[-9.915356],[-0.462987],[0.397787],[-1.828093],[0.429993],[-3.597372],[5.089799],[-1.825307],[4.028514],[4.971147],[-6.852510],[5.547061],[-7.904060],[9.531415],[5.885090],[-7.523372],[-3.608659],[5.377682],[-2.492887],[-3.446323],[6.476166],[-6.074586],[9.903787],[-2.518145],[7.746843],[2.027449],[-4.392102],[3.548322],[-9.927798],[2.264096],[-7.440952],[6.105287],[-7.750289],[7.043191],[-6.722454],[4.725538],[-8.320292],[5.984686],[-7.069785],[-8.452479],[6.254962],[-5.287606],[-3.866410],[-6.403763],[-1.505312],[6.920452],[7.099581],[1.496223],[0.028089],[-2.805437],[5.461544],[-1.657775],[-8.743922],[5.116676],[9.167827],[-8.084859],[-1.156092],[-0.294164],[5.208904],[8.757640],[4.908602],[-5.960418],[-5.531269],[-2.773380],[-2.490228],[9.811995],[-8.815450],[8.077138],[4.355903],[-3.329238],[-9.802669],[4.801227],[0.436538],[-2.520802],[-0.281249],[-1.134804],[-9.933908],[2.314018],[6.099201],[-4.100269],[-9.595518],[2.682326],[8.200603],[6.439102],[1.316858],[4.053776],[1.151731],[-9.358499],[2.418774],[9.645989],[4.967167],[0.120663],[-9.204218],[-9.484867],[-0.633213],[-7.107228],[-8.397223],[-5.051873],[-4.909696],[5.241502],[6.205210],[-4.770635],[0.755411],[8.398156],[9.782380],[0.358381],[-2.251766],[-4.346889],[8.960517],[-0.190378],[3.397339],[-2.531507],[-5.703654],[-7.184611],[8.402291],[5.404893],[-8.601074],[2.017545],[-5.399181],[-9.138847],[0.754461],[-3.910138],[-3.414745],[-2.191369],[2.986534],[-7.475498],[5.183796],[2.481595],[9.806122],[3.102888],[8.019875],[2.479696],[-1.235179],[5.574119],[3.969334],[-0.680620],[9.570790],[-8.630001],[6.488950],[3.705581],[-3.129233],[2.718700],[0.301503],[0.697292],[-0.084042],[0.365874],[5.694422],[-8.204229],[1.125711],[4.287644],[2.357237],[3.756540],[-5.045990],[7.356973],[-9.769649],[1.998554],[-7.556053],[2.590831],[0.458073],[-4.521522],[0.143234],[1.836814],[-9.555357],[-0.318556],[3.190708],[-7.123702],[9.454136],[-4.555636],[3.594788],[7.436600],[-5.608283],[-6.024017],[0.640521],[-8.866736],[1.598795],[2.778113],[-0.769367],[2.069430],[-4.712609],[-7.096861],[2.226717],[-2.185459],[-7.380329],[7.437421],[-2.619306],[-2.465693],[5.619176],[5.148583],[-0.122760],[8.555410],[-1.283326],[-0.274651],[3.604867],[1.003096],[0.507044],[3.636682],[-2.976275],[0.230346],[-9.302742],[6.286722],[2.889362],[-1.223348],[-5.750479],[2.904090],[3.448498],[-7.494165],[2.273805],[4.882781],[0.011125],[-4.954444],[-9.313310],[5.468646],[-5.342270],[-5.075425],[1.560929],[0.611796],[3.731596],[7.777678],[-0.843905],[-3.250135],[9.845188],[5.419584],[5.773475],[2.363301],[-2.352588],[1.357601],[-8.032871],[6.524751],[8.502451],[5.900211],[2.984279],[6.580843],[-0.329953],[1.657384],[5.777803],[5.870717],[-8.305122],[-4.106782],[3.884402],[-1.537688],[4.934198],[-2.447459],[0.548694],[-7.987125],[3.798061],[1.095493],[0.994849],[5.504958],[-8.946396],[-8.902549],[-8.482150],[-4.888124],[-6.603700],[-7.985106],[2.275513],[7.685174],[-5.560359],[-7.273574],[-9.711971],[-0.980461],[-5.767751],[-3.513374],[-3.644589],[-0.700389],[-9.846604],[3.581054],[-5.007367],[-1.729356],[-0.787533],[-7.114885],[2.861063],[-6.267268],[4.214714],[6.320398],[-0.185179],[-8.994601],[-9.970670],[-9.157917],[-0.444476],[1.473560],[6.639545],[-5.108946],[-0.341900],[-9.735870],[6.778657],[-8.001092],[2.506179],[7.331296],[2.033294],[-0.190961],[-7.395913],[0.296881],[8.052929],[-5.542257],[-8.209054],[4.313376],[-8.551500],[7.923540],[-3.004160],[3.681850],[-2.597548],[-4.324190],[-7.636263],[-0.101358],[6.847141],[1.175916],[8.916321],[-5.097373],[-3.106607],[8.910939],[-5.588425],[-2.066818],[-7.675823],[8.415972],[-2.953023],[-9.965000],[3.872214],[-1.062476],[-3.110052],[8.860104],[4.559436],[-9.762260],[3.608377],[3.189753],[7.175229],[-4.040439],[7.260953],[-3.369135],[-8.428323],[-5.608179],[-6.890943],[2.329419],[-2.726030],[4.611400],[6.531937],[-5.750894],[-1.899268],[6.792851],[2.531680],[1.054311],[2.880636],[-1.452954],[7.313281],[-0.967894],[-3.387165],[-8.910374],[-1.307991],[-0.580421],[0.608769],[9.693710],[6.246599],[8.843093],[-7.007376],[1.685678],[1.703141],[-8.684959],[7.693446],[-7.925803],[5.760919],[-3.166879],[3.797556],[-2.381219],[2.766303],[-7.937985],[0.519901],[7.439746],[3.126099],[-6.366455],[4.557483],[3.291550],[-4.252584],[-0.069569],[-2.619577],[-5.750343],[1.549754],[-3.247023],[4.733617],[-6.633517],[5.682144],[8.665316],[2.628850],[0.254371],[4.182402],[-5.964040],[-0.070198],[-0.123386],[-2.571994],[-8.580714],[8.238177],[-3.179535],[6.449737],[3.173251],[-0.503429],[2.159933],[2.270675],[-2.441964],[4.482191],[5.955214],[8.443627],[-3.929175],[-7.598147],[-1.621705],[8.153417],[2.124318],[-2.838611],[4.869357],[-1.729594],[-6.003305],[9.595357]], dtype = "float32")#candidate|6076|(1430, 1)|const|float32
call_6075 = relay.TupleGetItem(func_2748_call(relay.reshape(const_6076.astype('float32'), [13, 10, 11]), relay.reshape(const_6076.astype('float32'), [13, 10, 11]), ), 0)
call_6077 = relay.TupleGetItem(func_2752_call(relay.reshape(const_6076.astype('float32'), [13, 10, 11]), relay.reshape(const_6076.astype('float32'), [13, 10, 11]), ), 0)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
call_6080 = relay.TupleGetItem(func_980_call(), 1)
call_6081 = relay.TupleGetItem(func_982_call(), 1)
func_2094_call = mod.get_global_var('func_2094')
func_2096_call = mutated_mod.get_global_var('func_2096')
call_6086 = relay.TupleGetItem(func_2094_call(), 4)
call_6087 = relay.TupleGetItem(func_2096_call(), 4)
func_2668_call = mod.get_global_var('func_2668')
func_2669_call = mutated_mod.get_global_var('func_2669')
call_6088 = func_2668_call()
call_6089 = func_2668_call()
output = relay.Tuple([call_6024,call_6026,call_6055,const_6056,call_6075,const_6076,call_6080,call_6086,call_6088,])
output2 = relay.Tuple([call_6025,call_6027,call_6057,const_6056,call_6077,const_6076,call_6081,call_6087,call_6089,])
func_6092 = relay.Function([], output)
mod['func_6092'] = func_6092
mod = relay.transform.InferType()(mod)
mutated_mod['func_6092'] = func_6092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6092_call = mutated_mod.get_global_var('func_6092')
call_6093 = func_6092_call()
output = call_6093
func_6094 = relay.Function([], output)
mutated_mod['func_6094'] = func_6094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6126 = relay.var("var_6126", dtype = "float32", shape = (10, 8, 5))#candidate|6126|(10, 8, 5)|var|float32
uop_6127 = relay.exp(var_6126.astype('float32')) # shape=(10, 8, 5)
output = uop_6127
output2 = uop_6127
func_6129 = relay.Function([var_6126,], output)
mod['func_6129'] = func_6129
mod = relay.transform.InferType()(mod)
var_6130 = relay.var("var_6130", dtype = "float32", shape = (10, 8, 5))#candidate|6130|(10, 8, 5)|var|float32
output = func_6129(var_6130)
func_6131 = relay.Function([var_6130], output)
mutated_mod['func_6131'] = func_6131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_55_call = mod.get_global_var('func_55')
func_56_call = mutated_mod.get_global_var('func_56')
call_6133 = relay.TupleGetItem(func_55_call(), 1)
call_6134 = relay.TupleGetItem(func_56_call(), 1)
output = relay.Tuple([call_6133,])
output2 = relay.Tuple([call_6134,])
func_6168 = relay.Function([], output)
mod['func_6168'] = func_6168
mod = relay.transform.InferType()(mod)
mutated_mod['func_6168'] = func_6168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6168_call = mutated_mod.get_global_var('func_6168')
call_6169 = func_6168_call()
output = call_6169
func_6170 = relay.Function([], output)
mutated_mod['func_6170'] = func_6170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4422_call = mod.get_global_var('func_4422')
func_4424_call = mutated_mod.get_global_var('func_4424')
call_6202 = relay.TupleGetItem(func_4422_call(), 1)
call_6203 = relay.TupleGetItem(func_4424_call(), 1)
func_5798_call = mod.get_global_var('func_5798')
func_5800_call = mutated_mod.get_global_var('func_5800')
call_6212 = relay.TupleGetItem(func_5798_call(), 0)
call_6213 = relay.TupleGetItem(func_5800_call(), 0)
func_4548_call = mod.get_global_var('func_4548')
func_4550_call = mutated_mod.get_global_var('func_4550')
const_6216 = relay.const([[-0.151559,5.382703,-5.984388,-5.069357,4.811800,-2.163431,9.257993,-7.320152,8.497345,1.700363,-3.287145,3.961188],[-5.701718,3.275203,-2.109142,-2.717299,2.071563,1.802419,6.519726,-3.748483,2.101167,-5.180153,-9.926442,-6.419767],[-0.753788,6.987449,0.069017,-4.448630,1.653329,-4.102507,-4.963037,-0.349069,-2.410544,0.453142,5.283301,-0.162995],[2.997712,-0.048987,1.204712,1.269808,-3.092514,-8.537481,6.959170,-3.426705,6.350044,-7.271749,1.370505,6.617555],[-3.822484,8.506109,-8.008217,-3.108043,-3.321683,-1.585395,-7.614900,7.719305,-1.268184,-0.775320,-9.127318,0.298079],[6.013543,2.792305,-7.546363,-2.381196,-6.278158,3.691495,1.815339,-7.305066,-1.204625,-0.860973,-0.246921,3.451672],[1.720378,-5.108373,-6.293524,0.780652,9.426675,-9.234612,-5.950094,-8.280615,-1.153558,3.342084,4.985406,6.051570],[-1.565406,-6.911460,1.844597,-6.484930,7.389826,-7.990359,-8.596465,0.425436,9.248885,4.843579,-5.237884,-5.241700],[2.668517,6.408580,8.784542,-7.414700,-8.965561,-2.250456,6.811782,-9.966506,9.624375,-8.466305,0.677097,8.355874],[-8.746374,-3.433785,-2.613821,5.165167,-7.655465,-4.606289,-4.551931,-6.670345,-8.397014,-0.577416,8.970448,-5.450054],[-1.346333,-7.230832,6.685103,-5.262111,-5.201975,-1.905326,9.337028,8.893007,-6.981377,6.999153,-2.349710,9.113375],[-8.327864,-0.095377,9.229030,-9.622903,-5.670504,4.501012,-5.366251,1.829665,-5.322224,7.430972,2.177779,6.355430],[-8.409267,-2.541216,-5.540823,1.853944,-1.904935,-1.768772,1.646096,3.771663,0.751040,4.766622,-9.340385,1.722483],[-8.339819,-0.452855,5.822354,-0.704033,-4.266062,-8.448505,-4.349778,0.448531,-4.111181,-9.205192,-5.917042,8.940494],[-8.998704,8.848869,6.374468,8.622450,6.608769,4.889402,-7.699726,-4.336343,7.866662,6.955600,2.126459,-9.383263],[5.595163,0.829433,-5.513702,1.281661,7.270809,0.063422,1.114061,-4.642183,-0.107622,1.356180,2.104948,9.745187],[6.939927,8.617545,9.267422,-2.501481,-8.634019,-6.796090,-7.424114,-8.638081,-7.542812,-9.800085,-0.056912,-6.538563],[-7.989859,6.120102,8.061552,-6.434112,-8.376231,6.712948,9.295948,-7.000392,5.496966,-3.266941,-7.982235,0.186006],[-2.501164,2.454063,7.056253,3.792141,4.824236,5.514145,6.492873,2.771303,3.851697,4.543337,-8.563897,6.367300],[-6.188115,7.241282,-7.009788,3.175710,-2.667324,9.569979,-3.001540,-7.227848,-9.109147,5.964157,8.225170,5.914229],[7.033449,-0.067002,-9.298107,-7.073110,0.393862,8.553859,-8.681050,2.543822,9.715143,-8.567748,3.171125,-1.568094],[1.652359,-3.323754,-3.597595,8.340126,-4.121907,-0.229792,2.991570,-8.269028,-4.196466,-7.168009,-3.780480,-1.407989],[4.617942,-7.129113,2.771521,-6.410477,-4.492343,5.858381,-8.537646,-6.958049,-6.841226,7.624971,8.596292,4.773214],[8.860129,4.951739,3.529307,-0.805489,-5.913008,0.623849,9.856111,-3.997792,-3.466287,-1.737280,0.584651,-6.538448]], dtype = "float64")#candidate|6216|(24, 12)|const|float64
call_6215 = relay.TupleGetItem(func_4548_call(relay.reshape(const_6216.astype('float64'), [288,])), 2)
call_6217 = relay.TupleGetItem(func_4550_call(relay.reshape(const_6216.astype('float64'), [288,])), 2)
output = relay.Tuple([call_6202,call_6212,call_6215,const_6216,])
output2 = relay.Tuple([call_6203,call_6213,call_6217,const_6216,])
func_6220 = relay.Function([], output)
mod['func_6220'] = func_6220
mod = relay.transform.InferType()(mod)
output = func_6220()
func_6221 = relay.Function([], output)
mutated_mod['func_6221'] = func_6221
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6238 = relay.var("var_6238", dtype = "uint8", shape = (16, 12, 3))#candidate|6238|(16, 12, 3)|var|uint8
var_6239 = relay.var("var_6239", dtype = "uint8", shape = (16, 12, 3))#candidate|6239|(16, 12, 3)|var|uint8
bop_6240 = relay.right_shift(var_6238.astype('uint8'), relay.reshape(var_6239.astype('uint8'), relay.shape_of(var_6238))) # shape=(16, 12, 3)
output = relay.Tuple([bop_6240,])
output2 = relay.Tuple([bop_6240,])
func_6253 = relay.Function([var_6238,var_6239,], output)
mod['func_6253'] = func_6253
mod = relay.transform.InferType()(mod)
var_6254 = relay.var("var_6254", dtype = "uint8", shape = (16, 12, 3))#candidate|6254|(16, 12, 3)|var|uint8
var_6255 = relay.var("var_6255", dtype = "uint8", shape = (16, 12, 3))#candidate|6255|(16, 12, 3)|var|uint8
output = func_6253(var_6254,var_6255,)
func_6256 = relay.Function([var_6254,var_6255,], output)
mutated_mod['func_6256'] = func_6256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3050_call = mod.get_global_var('func_3050')
func_3051_call = mutated_mod.get_global_var('func_3051')
call_6304 = relay.TupleGetItem(func_3050_call(), 2)
call_6305 = relay.TupleGetItem(func_3051_call(), 2)
output = call_6304
output2 = call_6305
func_6310 = relay.Function([], output)
mod['func_6310'] = func_6310
mod = relay.transform.InferType()(mod)
mutated_mod['func_6310'] = func_6310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6310_call = mutated_mod.get_global_var('func_6310')
call_6311 = func_6310_call()
output = call_6311
func_6312 = relay.Function([], output)
mutated_mod['func_6312'] = func_6312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_6373 = func_39_call()
call_6374 = func_39_call()
output = relay.Tuple([call_6373,])
output2 = relay.Tuple([call_6374,])
func_6375 = relay.Function([], output)
mod['func_6375'] = func_6375
mod = relay.transform.InferType()(mod)
output = func_6375()
func_6376 = relay.Function([], output)
mutated_mod['func_6376'] = func_6376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4730_call = mod.get_global_var('func_4730')
func_4732_call = mutated_mod.get_global_var('func_4732')
call_6433 = relay.TupleGetItem(func_4730_call(), 0)
call_6434 = relay.TupleGetItem(func_4732_call(), 0)
uop_6435 = relay.atanh(call_6433.astype('float32')) # shape=(6, 28)
uop_6437 = relay.atanh(call_6434.astype('float32')) # shape=(6, 28)
func_5099_call = mod.get_global_var('func_5099')
func_5101_call = mutated_mod.get_global_var('func_5101')
call_6439 = func_5099_call()
call_6440 = func_5099_call()
uop_6446 = relay.sigmoid(uop_6435.astype('float32')) # shape=(6, 28)
uop_6448 = relay.sigmoid(uop_6437.astype('float32')) # shape=(6, 28)
func_2547_call = mod.get_global_var('func_2547')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_6449 = relay.TupleGetItem(func_2547_call(), 0)
call_6450 = relay.TupleGetItem(func_2549_call(), 0)
bop_6454 = relay.multiply(uop_6446.astype('int64'), relay.reshape(call_6433.astype('int64'), relay.shape_of(uop_6446))) # shape=(6, 28)
bop_6457 = relay.multiply(uop_6448.astype('int64'), relay.reshape(call_6434.astype('int64'), relay.shape_of(uop_6448))) # shape=(6, 28)
output = relay.Tuple([call_6439,call_6449,bop_6454,])
output2 = relay.Tuple([call_6440,call_6450,bop_6457,])
func_6458 = relay.Function([], output)
mod['func_6458'] = func_6458
mod = relay.transform.InferType()(mod)
output = func_6458()
func_6459 = relay.Function([], output)
mutated_mod['func_6459'] = func_6459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_84_call = mod.get_global_var('func_84')
func_85_call = mutated_mod.get_global_var('func_85')
call_6500 = relay.TupleGetItem(func_84_call(), 1)
call_6501 = relay.TupleGetItem(func_85_call(), 1)
func_5063_call = mod.get_global_var('func_5063')
func_5064_call = mutated_mod.get_global_var('func_5064')
call_6502 = relay.TupleGetItem(func_5063_call(), 0)
call_6503 = relay.TupleGetItem(func_5064_call(), 0)
func_6168_call = mod.get_global_var('func_6168')
func_6170_call = mutated_mod.get_global_var('func_6170')
call_6506 = relay.TupleGetItem(func_6168_call(), 0)
call_6507 = relay.TupleGetItem(func_6170_call(), 0)
output = relay.Tuple([call_6500,call_6502,call_6506,])
output2 = relay.Tuple([call_6501,call_6503,call_6507,])
func_6509 = relay.Function([], output)
mod['func_6509'] = func_6509
mod = relay.transform.InferType()(mod)
output = func_6509()
func_6510 = relay.Function([], output)
mutated_mod['func_6510'] = func_6510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4047_call = mod.get_global_var('func_4047')
func_4049_call = mutated_mod.get_global_var('func_4049')
call_6617 = relay.TupleGetItem(func_4047_call(), 0)
call_6618 = relay.TupleGetItem(func_4049_call(), 0)
output = call_6617
output2 = call_6618
func_6630 = relay.Function([], output)
mod['func_6630'] = func_6630
mod = relay.transform.InferType()(mod)
output = func_6630()
func_6631 = relay.Function([], output)
mutated_mod['func_6631'] = func_6631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4953_call = mod.get_global_var('func_4953')
func_4954_call = mutated_mod.get_global_var('func_4954')
call_6634 = relay.TupleGetItem(func_4953_call(), 0)
call_6635 = relay.TupleGetItem(func_4954_call(), 0)
func_55_call = mod.get_global_var('func_55')
func_56_call = mutated_mod.get_global_var('func_56')
call_6636 = relay.TupleGetItem(func_55_call(), 1)
call_6637 = relay.TupleGetItem(func_56_call(), 1)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_6648 = relay.TupleGetItem(func_2173_call(), 3)
call_6649 = relay.TupleGetItem(func_2175_call(), 3)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_6664 = relay.TupleGetItem(func_782_call(relay.reshape(call_6648.astype('float32'), [168,])), 1)
call_6665 = relay.TupleGetItem(func_784_call(relay.reshape(call_6648.astype('float32'), [168,])), 1)
output = relay.Tuple([call_6634,call_6636,call_6648,call_6664,])
output2 = relay.Tuple([call_6635,call_6637,call_6649,call_6665,])
func_6687 = relay.Function([], output)
mod['func_6687'] = func_6687
mod = relay.transform.InferType()(mod)
output = func_6687()
func_6688 = relay.Function([], output)
mutated_mod['func_6688'] = func_6688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4047_call = mod.get_global_var('func_4047')
func_4049_call = mutated_mod.get_global_var('func_4049')
call_6702 = relay.TupleGetItem(func_4047_call(), 2)
call_6703 = relay.TupleGetItem(func_4049_call(), 2)
func_924_call = mod.get_global_var('func_924')
func_927_call = mutated_mod.get_global_var('func_927')
const_6725 = relay.const([False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,False,True,False], dtype = "bool")#candidate|6725|(216,)|const|bool
call_6724 = relay.TupleGetItem(func_924_call(relay.reshape(const_6725.astype('bool'), [9, 4, 6]), relay.reshape(call_6702.astype('float32'), [168,]), ), 3)
call_6726 = relay.TupleGetItem(func_927_call(relay.reshape(const_6725.astype('bool'), [9, 4, 6]), relay.reshape(call_6702.astype('float32'), [168,]), ), 3)
func_2428_call = mod.get_global_var('func_2428')
func_2430_call = mutated_mod.get_global_var('func_2430')
const_6735 = relay.const([[7.479139,0.793011,-6.604019,-0.170281,1.016983,-1.496465,-4.766702,8.416732,3.960966,-0.559337,4.439388,-5.384115],[-4.738025,0.017813,0.843533,6.816735,-8.828792,-5.929142,8.060452,8.226478,3.876034,8.989986,3.991099,-4.829469],[-9.973592,0.308980,-1.809183,-5.867120,8.575851,-1.940458,-8.303978,-7.644890,-5.415540,7.457715,7.736973,-7.138862],[-8.588269,-0.374862,-8.960322,-0.291473,0.498840,-5.517858,4.153243,7.800655,-2.741998,9.605966,8.350693,2.415312],[-4.787101,-2.593424,-5.638270,-2.856254,-9.845574,-1.880440,-1.045132,5.829251,-4.800047,7.084612,-7.791011,-3.577369],[-3.442782,8.472535,7.184129,8.219798,2.021479,8.795218,-7.153741,-2.029496,4.392212,-0.013822,7.835269,8.588687],[7.148110,8.919818,3.596136,9.014413,3.960331,-6.001387,9.820972,6.645963,0.999978,-4.896575,-5.294119,-5.151961],[0.604149,9.028161,-2.179399,-8.292963,-5.019028,-3.402912,-3.539631,8.511528,-1.240001,-8.821676,-8.062902,6.698195],[3.058049,9.138517,-7.639955,3.703906,-3.570290,1.962352,3.372007,0.567756,3.121943,-2.598424,7.001384,-7.422875],[4.454250,8.875724,-5.733927,9.971657,4.680109,9.603125,-1.477653,7.872173,-5.689205,5.198413,1.697964,8.129076],[-9.422524,-0.682990,6.637902,-7.770539,8.404985,-1.810136,-1.264508,4.492644,6.785729,2.956573,5.696160,-9.365588],[3.568860,-7.407197,-7.562072,-8.152524,0.793766,-3.748961,3.993982,2.831048,3.506105,-0.906209,6.240651,9.955262],[-8.512526,-1.046881,8.913201,3.745595,-2.538420,3.731350,2.581404,-9.967796,-4.097104,-6.195209,6.802091,2.544365],[1.535506,-3.096337,1.039683,4.328417,-2.701874,-7.174615,8.994782,6.855118,8.878298,-7.965492,-6.757217,5.954900],[-3.683492,-3.730822,4.620442,-3.696631,3.745008,4.560367,-9.451498,-3.516738,-4.092591,-3.358369,3.085546,3.938000],[5.047515,2.277895,-6.435263,-0.073372,-3.436628,-5.158262,-8.464854,5.814607,3.607303,5.504929,2.804401,5.909372],[-6.699116,2.417608,4.894660,-4.380900,9.094844,-8.393797,-0.927128,-3.856164,0.260613,-0.146110,7.202209,8.088781],[-4.170513,-8.137947,-7.418915,8.528480,1.721757,-9.273406,4.722507,8.271878,2.576465,8.202455,8.937941,-1.536458],[-5.927231,-5.507134,-0.266335,3.543531,-0.475220,3.086673,3.874895,1.688960,7.809394,3.017001,-4.581581,9.016676],[-8.463945,6.337141,-3.552775,-3.608852,-1.936977,-4.802280,-9.003000,6.590873,6.977595,0.393656,7.845920,-0.629760],[1.803073,-0.301444,-7.421574,8.806632,-9.061542,-9.236395,-1.061174,0.276640,-1.355967,-3.413099,3.500462,4.422436],[-2.942607,9.408904,-4.066288,-0.794890,7.497585,0.723279,0.203807,-5.234436,-9.001735,-9.986037,9.724950,0.841883],[-5.696292,-4.254630,-1.512716,-4.700273,7.615170,-4.376545,7.317853,7.905236,7.802182,7.735945,0.334893,-0.267745],[-3.867923,-7.145918,4.036815,7.918266,3.271407,7.723271,-1.626626,-3.917304,-5.629758,6.868337,-1.941934,-1.945198],[8.810685,-8.520928,-0.953409,-7.936375,2.939824,-4.994379,5.192580,-6.247385,-8.015028,-3.508452,-6.781162,-1.915667],[7.834753,-8.112749,-3.176510,-9.334078,-1.522498,-3.020919,7.284925,-0.971656,7.402500,0.415303,-2.449804,-3.840020],[-7.112961,6.524302,2.552871,4.772759,3.333321,-3.502001,-7.955693,-8.592364,2.213158,8.646542,4.863642,-0.582671],[6.790475,3.307022,4.038438,-0.478769,-2.597095,-8.030311,3.437849,6.275018,-0.550129,-2.982707,-9.020823,7.011322],[2.844041,-7.720959,-0.905287,9.145353,9.885584,-4.999683,-8.394740,-1.127201,-6.164591,2.291589,-1.615233,2.038000],[-1.986617,9.171627,-8.632084,3.520034,-6.797731,-2.832675,-5.080041,-3.031552,6.898779,-8.610930,0.138406,-8.366072],[-6.713205,7.256017,-2.828092,2.806152,-9.929661,4.091495,3.360741,-7.033363,2.554118,4.144492,-3.002186,3.519214],[-0.204807,-0.652414,-5.737939,3.622540,-9.916036,0.659124,8.514819,8.690479,9.845137,-7.151819,9.735209,-8.882934],[-9.419358,-4.152513,9.018478,-9.139268,-9.285343,5.405347,2.008921,0.757238,5.610566,2.788707,9.889589,-4.540966],[4.545676,1.849442,9.493365,2.095491,1.818681,6.696457,5.412648,-6.269586,-0.275684,-7.350148,0.346803,6.541244],[-1.773286,1.016188,7.739839,5.560426,0.335900,-3.022168,-6.356423,-1.101564,7.261712,3.381646,0.504838,-8.559806],[9.730954,1.745888,-7.673789,-0.706847,0.059034,-6.124026,9.998256,-5.324604,4.585757,-8.640138,-3.727410,7.874375],[-3.671123,0.771068,3.597018,8.241676,-4.262413,7.586353,4.654099,-1.142969,3.260745,0.982443,-2.762941,6.132734],[-4.265353,1.002906,-3.202950,4.073138,6.626451,-6.554608,-8.881727,-2.411246,4.740565,-7.187873,8.893091,2.981323],[9.745690,5.507146,-4.190316,7.562410,-6.273441,-2.030293,-7.473177,9.576188,-2.941089,-8.385073,7.268173,8.808818],[-4.615955,9.788533,-4.829787,-6.245521,-7.681544,5.663479,9.966168,5.173222,-6.370334,-9.666475,8.542360,-2.859137],[-2.483234,0.718855,2.564873,-1.912008,-7.413761,0.910088,-9.760527,-0.435085,-8.307390,-3.053277,6.185264,7.729958],[9.499700,-6.311448,-3.949590,-7.489530,6.735610,-9.501728,-4.850494,-7.087814,4.173130,-9.596043,0.808232,-9.720878],[-7.814036,1.171714,-3.816765,6.188297,3.713472,9.265306,4.799442,-2.692867,0.421630,9.952774,5.136209,-8.773451],[-9.074504,-4.406103,9.719580,6.155593,1.109120,0.405326,4.884184,1.010486,-6.855809,-9.737207,-7.493865,-4.952238],[-9.601163,-8.603376,7.902046,-1.430894,6.163500,-1.727257,6.100900,-9.007733,-9.506235,-1.889079,8.578674,-6.609258],[-7.015369,0.857003,0.027496,-0.342215,5.116005,0.985120,7.387808,-7.848531,9.812928,-9.186625,-5.505059,1.078835],[-5.494855,7.443824,-2.780892,-4.864890,-4.751674,2.405636,2.831446,3.538585,-3.869594,-1.552713,-8.709371,-4.005608],[1.075365,-3.576389,-7.317740,-4.766194,-2.198953,-1.606149,-2.363567,3.930516,-5.318318,-1.350893,3.250921,-0.357167],[8.030891,4.095817,-3.597701,2.488736,-2.401710,5.038733,1.131547,-6.642215,6.765185,-4.305659,5.823472,2.990985],[6.473571,3.919976,4.077572,-0.929470,-7.563436,6.785552,-7.084482,-3.528733,-0.416883,5.400109,-2.954484,9.757882],[-9.993047,3.134816,-6.909677,0.316022,-2.597616,-0.263295,-6.774472,-5.336668,-9.428684,2.259794,-5.974666,-6.432706],[-2.106625,4.933526,1.370621,-3.374734,-1.291347,7.038027,-9.361346,-7.598899,1.135811,0.522574,-1.090849,1.763963],[6.142179,0.200470,-7.574038,-9.226506,0.849141,4.288258,2.865774,-4.254656,8.801439,-6.376441,-7.989506,3.742525],[9.467469,8.896746,-1.692493,-0.876296,-4.399244,-8.590584,3.372566,0.253169,-4.822038,1.432311,-1.492613,2.112500],[3.105561,-0.469170,1.076050,-5.618440,-4.985868,-4.492785,-4.501735,-5.828558,-5.135609,2.839659,5.922020,-3.408222],[-5.673690,8.166964,4.182134,-3.841386,-9.421667,-8.322399,-1.275645,-3.992517,-4.734185,-5.922273,-8.524169,8.696006],[8.830499,-6.291831,9.195988,-8.382147,2.302467,2.501877,-1.669725,3.711443,-7.933159,-2.354710,-3.197399,0.321522],[2.740951,6.054958,-4.521055,-2.913776,-5.840983,-2.748610,1.274051,5.293911,8.205322,2.628428,-8.787687,-3.183620],[-5.171895,-5.454525,-6.998300,-6.949012,9.108003,9.157082,-8.197254,5.091924,-8.991874,2.110296,-6.668072,-7.328677],[8.412272,8.854643,1.278464,-4.441114,6.930500,-1.167093,-1.207111,4.677468,1.987195,4.963601,9.442743,-6.464299],[-6.979117,5.759379,-0.236123,-2.479038,-8.628661,7.823546,-3.629319,8.455339,-8.680956,6.283846,-3.830196,-0.834827],[0.168769,-0.950081,-4.033512,-6.465284,-3.404722,4.020425,-4.117107,-6.094184,-9.911548,-6.715969,4.651538,-5.443221],[5.036372,-8.520015,-8.125269,5.323691,-7.297052,-2.964573,-3.937011,0.986530,3.392939,6.874526,0.424636,-1.326360],[-3.995312,-8.522204,-3.908177,7.519249,-2.236631,-1.005695,2.765594,-7.547414,9.163232,-4.115660,7.069507,-9.855111],[1.664817,-1.695615,3.130793,-6.007073,3.561063,2.926652,2.869447,-0.663258,-9.969358,-0.941428,-1.213910,9.375117],[-9.279924,-6.763624,7.632405,-8.469211,-9.075595,0.297108,8.868118,2.497838,-1.457123,-8.055114,-4.923146,2.865592],[2.921360,-5.798127,-6.019709,6.606809,0.517572,9.529715,-6.511188,9.359741,-0.073312,-6.075149,-3.372560,1.566401],[-8.695645,-3.252437,-6.622866,5.544464,-6.324963,3.401408,0.739902,2.702955,-9.088927,-6.829802,-7.264474,-9.664556],[-3.774584,-0.995402,-5.602282,-8.317921,1.126238,8.552449,-4.871130,-8.660960,-4.634848,-5.927691,-1.480392,7.753536],[-5.800131,-1.020911,4.139176,0.898363,1.087303,3.387908,9.265751,5.419739,-6.525026,-3.599639,9.250278,3.689097],[7.747180,-0.749600,2.733493,-3.581431,3.790224,-2.693543,5.453135,-4.642540,0.319681,1.691025,4.419366,-8.591370],[6.760721,0.019695,3.607327,9.628665,-9.210315,-5.929557,5.312786,8.763019,9.575971,6.567808,7.869252,-3.083705],[4.551128,-4.836561,-9.891115,8.803386,4.050972,-5.933012,5.286501,2.379810,9.869171,-5.565013,3.728465,6.854579],[5.824632,3.263686,1.659521,-1.756516,0.670754,0.566832,9.411466,-3.329389,7.281005,0.555153,-5.276466,-6.331028],[-0.738130,-4.119662,-7.468753,0.176063,-9.222453,6.034063,-3.329589,1.085469,-0.342379,1.243468,6.249463,-6.814352],[-6.154707,2.351078,0.033700,6.254575,-9.114744,5.928501,8.457771,6.457106,7.620487,9.545697,-1.603760,-1.534356],[-2.240624,-6.055229,0.321052,-2.082082,-1.466145,-3.890104,-4.584929,8.870872,8.931980,9.291059,2.314209,-6.802120],[4.989358,-1.679678,-1.222574,-2.356932,-3.920138,-5.700751,-4.597264,-6.637132,4.743740,-4.335613,-5.455381,-4.748271],[-5.495143,-2.397004,-9.929552,-9.922574,3.787716,4.656898,2.379464,-4.075937,-3.480420,6.636129,0.278291,4.882482],[-9.962184,-9.040107,-8.155427,-1.017601,5.939846,-5.790707,-9.822413,8.706055,-4.749138,0.689506,6.977990,8.621546],[2.922380,-9.011485,-7.710791,6.751024,3.769969,8.703904,-4.727087,-1.818136,3.690365,-9.753703,7.034283,9.022575],[-5.701491,-6.185385,-6.871182,-8.424123,-1.564340,-2.001240,-1.528106,-0.192187,-2.194492,5.372054,2.438785,-8.681283],[7.774228,-6.711671,-7.539184,-0.074050,5.006546,-4.248658,-6.442303,7.273771,0.475936,-3.112624,4.977325,5.331900],[-5.884212,-7.721479,-9.056990,-0.131896,6.512018,2.948212,-9.341770,3.592148,-6.062664,4.053656,-0.742732,0.151496],[3.140264,6.191071,-5.467443,-0.214213,-7.484408,9.467344,4.953432,-4.638638,-3.187595,-2.651006,0.567667,-7.480866],[-4.470965,-2.864908,-4.648682,-1.324070,8.589196,-5.351628,2.585744,7.213367,-5.983605,-1.629113,-3.863771,-1.829395],[-3.099611,-2.275531,-7.183291,0.943128,-9.643994,0.062819,-2.207655,-2.664046,-6.860166,9.594111,0.923022,3.318961],[4.609834,7.233783,-5.730480,6.575976,1.203605,-5.521540,-8.740373,-3.082695,9.087062,-5.031338,8.474496,-4.348039],[4.077843,7.187603,-7.242788,-7.806672,7.008782,5.514857,-4.332676,-9.728329,-7.354810,0.473770,2.448788,-7.455403],[-5.220927,-9.479319,1.813003,0.561186,-6.447930,-9.239700,4.148054,5.990201,-3.011718,-9.635871,3.361430,-3.607945]], dtype = "float64")#candidate|6735|(90, 12)|const|float64
call_6734 = relay.TupleGetItem(func_2428_call(relay.reshape(const_6735.astype('float64'), [1080,])), 5)
call_6736 = relay.TupleGetItem(func_2430_call(relay.reshape(const_6735.astype('float64'), [1080,])), 5)
func_4214_call = mod.get_global_var('func_4214')
func_4215_call = mutated_mod.get_global_var('func_4215')
call_6752 = relay.TupleGetItem(func_4214_call(), 0)
call_6753 = relay.TupleGetItem(func_4215_call(), 0)
output = relay.Tuple([call_6702,call_6724,const_6725,call_6734,const_6735,call_6752,])
output2 = relay.Tuple([call_6703,call_6726,const_6725,call_6736,const_6735,call_6753,])
func_6770 = relay.Function([], output)
mod['func_6770'] = func_6770
mod = relay.transform.InferType()(mod)
mutated_mod['func_6770'] = func_6770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6770_call = mutated_mod.get_global_var('func_6770')
call_6771 = func_6770_call()
output = call_6771
func_6772 = relay.Function([], output)
mutated_mod['func_6772'] = func_6772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2118_call = mod.get_global_var('func_2118')
func_2120_call = mutated_mod.get_global_var('func_2120')
call_6815 = func_2118_call()
call_6816 = func_2118_call()
output = call_6815
output2 = call_6816
func_6826 = relay.Function([], output)
mod['func_6826'] = func_6826
mod = relay.transform.InferType()(mod)
output = func_6826()
func_6827 = relay.Function([], output)
mutated_mod['func_6827'] = func_6827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_84_call = mod.get_global_var('func_84')
func_85_call = mutated_mod.get_global_var('func_85')
call_6830 = relay.TupleGetItem(func_84_call(), 1)
call_6831 = relay.TupleGetItem(func_85_call(), 1)
output = relay.Tuple([call_6830,])
output2 = relay.Tuple([call_6831,])
func_6848 = relay.Function([], output)
mod['func_6848'] = func_6848
mod = relay.transform.InferType()(mod)
output = func_6848()
func_6849 = relay.Function([], output)
mutated_mod['func_6849'] = func_6849
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6872 = relay.var("var_6872", dtype = "float64", shape = (12, 10, 1))#candidate|6872|(12, 10, 1)|var|float64
const_6873 = relay.const([[[9.253845,4.785956,-4.002936,2.033273,-8.179721,-5.089737,-1.694549,-7.286482,-9.192227,1.428563],[-3.375568,9.271576,-5.389418,3.075769,-2.915688,1.199927,4.735180,-8.778069,-5.229599,6.896495],[1.041701,-3.328440,4.384930,7.670272,4.883090,-5.001784,8.920766,-6.863161,-6.722234,-6.106935],[-7.277818,6.112854,-3.185627,1.689093,3.122903,4.890988,7.147477,-6.494891,-2.056778,-4.179885],[-7.091100,7.453562,-8.883707,1.900875,0.096814,7.633557,-4.030449,-8.316564,1.418795,4.879025],[-4.076704,3.686551,-9.728725,-9.962086,7.886825,6.320805,0.752908,4.510763,-2.116022,2.843755],[4.986928,0.123575,8.368937,-8.075852,5.395144,8.779127,0.395575,3.546069,-3.704221,-6.812587],[-4.047360,2.620488,4.872427,-5.061053,-3.873367,9.734515,-2.059192,4.728640,-0.649373,-6.388726],[2.434914,3.932244,-1.382832,1.996957,-8.152906,5.414363,4.571482,2.063018,8.781650,-5.013953],[2.631595,7.970488,-2.050880,0.382745,2.633894,-5.123339,7.763226,6.768477,8.780031,-0.782189]],[[-8.491774,-9.367828,-0.984482,-7.815365,8.707273,1.381508,2.206942,5.009441,3.447742,-7.038551],[-3.486553,-6.056092,1.066257,-8.043697,-1.528563,-9.784240,-5.123542,-7.099321,-4.239591,-8.930446],[9.872855,-8.274639,5.444567,-3.865285,-7.303889,4.805931,8.020574,-1.751486,3.290161,6.646492],[9.059545,-4.550467,8.914841,6.766656,-3.749125,8.602905,7.390058,-8.495440,1.105695,-9.768412],[3.303795,0.764084,4.761890,0.293361,-9.854466,-6.958670,5.385564,9.463931,2.413836,-3.118406],[-5.128184,7.877402,-4.607155,-1.098520,-0.445313,2.445784,-9.261751,-3.652320,1.096185,-8.591936],[4.679284,4.953389,-8.677144,7.065827,7.844072,1.857899,5.378067,-4.205266,-9.253236,-2.541057],[3.224134,-3.486534,-2.010521,7.254844,4.162914,2.440498,-7.352926,6.657699,9.564244,-2.678197],[-1.877954,-2.400271,-7.438016,1.168613,-9.441946,5.226386,-2.739041,8.286418,-1.766939,-6.499589],[0.155257,-7.405385,-8.484780,-1.174075,-8.722271,9.758974,-6.481146,1.777667,-9.015147,2.451708]],[[-7.469952,-3.852098,-7.663954,9.177480,-1.219572,-0.312673,2.038049,2.346371,-6.047895,0.029988],[-6.014103,-6.322433,-1.994502,0.111923,-0.034537,9.419662,0.912820,0.742030,-0.650412,-7.959297],[-2.456814,-8.315981,-4.444833,-4.486025,3.530136,1.789388,-7.144128,-6.854922,3.996681,0.824455],[-6.865444,-6.320472,-6.304273,9.351980,-3.969065,7.492238,0.208492,-9.077325,4.996452,-9.716086],[-7.347363,-0.229476,0.922054,-1.438144,-6.552689,2.552357,-4.100114,-9.042256,2.798471,1.088753],[8.768620,5.931189,-0.199877,-8.860184,-2.730390,-1.349576,8.745924,6.126023,9.464209,4.093976],[5.872941,-7.567118,7.445424,-8.358098,1.362561,-7.336463,-2.090403,0.825621,-0.129488,-0.943506],[-1.398772,5.802426,0.164858,5.449445,-6.246907,-8.490635,7.172753,-6.728626,0.502397,9.441047],[-2.446790,9.307395,0.289071,-4.959658,6.084088,-7.826060,6.913478,2.577740,-6.541665,-3.364346],[0.268917,-8.417295,1.994381,5.900578,2.282988,0.100069,6.020571,-6.640518,1.598383,-6.082951]],[[2.587053,4.853182,-5.990619,1.931960,9.665666,-2.045666,-3.807727,0.020949,8.654269,-2.977323],[8.497858,-7.526198,8.135333,-1.727039,1.557055,4.459558,5.176960,-6.726971,5.263352,5.937441],[7.015127,1.034973,-8.836491,5.801641,-2.881618,7.495402,-9.482509,-0.270682,-9.119295,-8.227542],[4.155973,4.399651,-8.792940,-3.997524,9.000787,-5.328404,5.452843,5.385974,-6.991187,0.509502],[-7.302336,9.820374,9.637456,-4.952847,-1.202991,3.833705,-7.697880,-1.510749,-1.388565,-2.899779],[-5.917503,-0.914319,7.604949,-8.170463,8.647390,-5.075013,-1.937683,-1.318701,4.561942,2.575914],[3.516533,8.703913,8.696380,2.340743,-8.928654,-4.820289,-0.516361,0.324100,-1.063700,-0.990919],[9.057536,6.007764,-2.656044,5.739267,1.173517,5.986495,-9.898530,-8.547183,-3.402867,8.127173],[-9.123625,-3.485690,6.426810,-0.869026,0.121174,0.095635,3.576255,-7.093950,-3.106058,1.309111],[-2.120568,-2.562762,7.263168,2.939137,-2.222531,-1.774608,-1.246371,-0.543281,-3.003943,2.892078]],[[1.251543,9.657164,1.511685,-2.525696,7.828990,6.990282,-8.799598,-3.678326,0.274077,1.611620],[2.613514,-3.283781,-3.578343,8.925582,5.463853,-7.457372,4.033249,6.295034,0.692736,-5.843699],[2.941093,2.159286,5.687307,4.128026,2.591975,3.663093,-5.042926,-0.509196,-7.902627,-4.245090],[-7.328735,-7.512635,-1.367291,-6.386973,7.116536,-0.846501,9.711434,-0.133288,-7.296930,4.366914],[-0.852109,-6.210757,-3.595947,-0.202281,-3.168344,-3.284642,0.480505,-3.339845,-2.013961,-5.993353],[1.214998,-7.871167,-1.236970,1.991133,-5.499409,-4.884934,5.582082,3.478147,3.052147,-1.522928],[-3.803435,-9.818375,5.430145,5.001446,8.707421,2.427520,9.162886,9.973320,-8.638059,-1.925203],[4.971927,-8.643314,9.171589,-1.734746,5.658806,-3.493852,6.734648,6.538570,5.257552,-1.349291],[-4.268748,9.405912,2.778928,1.890965,7.514048,-2.253352,-1.967905,-7.313773,8.807759,-1.432950],[2.787539,-6.599989,8.621849,-5.307006,5.220646,-1.925425,-3.863672,6.615317,-3.382931,-2.162610]],[[-7.037807,8.558248,1.960234,-7.892256,-7.641157,5.515127,6.813681,8.100009,1.191446,6.052473],[-6.947267,7.309831,0.897525,8.854932,0.791928,1.691270,-3.543584,5.643107,-4.384107,-7.797194],[-9.857640,0.134264,-1.858812,6.552408,-4.712577,-9.687698,-6.733453,9.733877,-3.835502,4.500136],[-7.028205,0.406736,4.513249,-9.520092,-4.187840,1.625128,-3.051545,-1.067812,0.099500,9.163855],[-7.923024,-5.881257,4.647253,-4.131597,-3.785840,5.816640,-0.424950,-8.090382,8.215024,-3.398898],[6.748672,5.786674,-2.522664,-8.453578,1.077151,3.642530,6.892264,-2.300890,1.820954,-9.048897],[-8.398494,0.060530,-6.400969,1.874242,-8.664699,4.361786,7.496966,-9.281878,-6.791663,9.351795],[-3.220969,7.953737,-4.565692,-5.093889,-8.668334,-1.819965,-1.977952,-5.249271,3.156928,7.877903],[8.550682,4.375393,9.204222,-7.157672,4.441923,9.832249,-4.973660,2.101753,-6.257924,-5.879746],[3.191782,2.557026,-5.632176,-5.921874,0.326618,-5.437278,5.376041,9.616731,9.161751,-4.707817]],[[9.009099,-9.235614,5.459156,5.204669,4.600319,-8.587003,-2.575639,-2.087479,9.372764,-6.067706],[-3.058396,3.623529,-3.793827,-9.224381,-7.934297,-9.432260,-4.132178,1.611357,4.871548,0.123904],[5.986681,0.716316,-3.811069,-8.507224,-4.420317,-1.798544,0.537768,-5.056636,5.396572,0.385853],[-3.698099,9.901764,-6.212022,-7.622148,9.861886,-4.055768,7.641460,-6.806992,-5.552025,-6.722786],[0.922753,2.402100,-1.246042,1.862550,2.295383,-2.121053,-3.610938,-5.634650,-9.283787,-2.948751],[9.458624,-4.079408,-0.380575,-6.818413,-0.755244,-0.329429,9.403754,-9.487359,5.982364,8.358371],[9.590987,-0.200136,-2.734422,-6.230579,0.998800,-2.467665,-0.826411,-9.038200,-5.310018,3.602687],[7.354493,-2.444345,6.658948,-5.629168,-3.740927,7.723391,3.845949,-7.252471,2.918859,6.660934],[2.727656,6.053462,-4.242539,9.125267,-1.948849,9.081326,-0.862265,-6.369084,5.228664,-0.380599],[9.196724,2.544678,-5.996125,-1.465625,-1.722343,-3.833716,1.746038,5.010611,4.557555,-2.029207]],[[3.511639,9.839398,-6.882180,-6.551167,4.399333,1.327348,-8.808442,9.376581,-3.284516,-3.826649],[9.375632,7.161261,-4.524587,1.712097,8.387305,7.096856,3.755659,-6.328725,1.226618,3.742905],[7.215536,3.299237,9.877524,-7.436824,-5.722078,4.130786,-5.109021,-7.300878,3.564565,-0.602933],[-8.503667,-0.304306,6.911807,5.143299,5.924181,2.051329,6.784971,-9.553258,0.489100,2.245874],[-5.668614,-9.663265,6.700354,0.864254,-7.877364,1.169252,-8.061239,-7.724496,-1.875321,-4.710776],[8.750884,-7.115036,-7.356259,9.272472,-0.191382,5.021761,4.757357,5.785143,-0.393187,-1.090861],[-7.820034,3.016281,4.861157,-6.894067,5.124937,9.776883,-1.288250,-0.657637,-4.787163,2.608394],[-0.606592,1.602559,-7.984284,-6.217366,-9.497560,0.833411,-2.934623,1.199274,-5.687070,2.928970],[-3.777852,-1.392904,-1.433039,2.926029,9.323239,0.121466,3.964033,9.418195,1.094239,-6.673822],[-0.328512,2.709680,9.179072,-7.151470,-9.094290,3.001472,-9.475134,-6.940909,-5.111412,-1.854883]],[[-3.279004,0.160520,-2.510458,1.165065,-7.379164,3.911277,4.969770,6.511526,6.490962,-0.597934],[7.289643,-3.403789,-0.347152,9.749072,-7.439940,-0.896335,8.049204,-2.650301,-1.211051,-4.716501],[-9.882306,-9.900170,-5.675964,-4.877823,8.077909,4.140255,-2.806556,5.355212,-7.887637,-3.157475],[-6.216885,3.089293,-2.589394,1.857721,2.438246,-5.859387,-7.566006,3.681269,-9.914378,-1.253796],[9.845025,0.858754,-8.919900,-8.159873,9.267230,6.615729,1.453933,4.800619,3.950700,-5.269420],[-5.611971,-9.368619,4.487537,4.027226,2.202158,-5.247689,-3.531363,-2.142594,-4.313874,8.193485],[3.869464,6.398432,-1.738907,3.209448,1.035088,-9.517305,-5.647006,-4.575260,1.476624,1.553941],[-5.629932,0.159514,2.161545,4.468726,-1.110116,8.166302,2.562217,-5.537517,-4.866461,6.464634],[4.579582,5.186656,-8.107785,-5.590909,-3.862816,-3.163704,4.741599,0.686823,-0.541251,-9.906787],[0.389420,-2.566556,-4.871177,-0.532659,-1.664240,-9.182096,-4.516702,2.618780,-3.944615,-2.943834]],[[-0.777426,6.422516,-2.155057,-5.723073,2.900327,3.311037,5.838137,3.138476,-1.907224,-5.593781],[-8.850002,-4.359749,-7.167125,2.293204,8.033595,1.563022,6.542694,9.427812,4.538426,-4.360692],[-1.672516,-2.867646,4.274472,8.164354,2.402590,7.355213,4.549124,-9.359802,0.015995,-2.986643],[0.748632,-9.370831,-3.615217,-1.947641,-9.866782,-0.917049,-0.028241,-6.743341,-4.957510,7.709009],[8.688993,9.191924,4.504699,-7.915029,-1.376911,9.222646,1.821436,-0.860331,-1.719573,3.504187],[0.743476,6.031719,-7.329691,9.264802,-5.519311,7.236421,1.997550,-2.013077,-3.903381,-0.356865],[1.095527,3.508665,8.347789,-8.396733,-3.837104,-9.851800,3.687495,-6.733996,3.450296,-9.527260],[-6.490200,4.969762,5.470123,-5.837791,8.840813,-9.637162,2.457522,6.899889,4.823140,-5.549009],[2.900859,1.110917,-1.922492,2.059254,5.149554,7.338520,8.950253,-7.937172,-2.341056,-1.793665],[1.649054,-2.355615,-8.954000,4.836021,7.624873,-0.789438,2.897242,4.082397,1.057926,8.128067]],[[5.545110,-7.720451,-0.887697,1.403765,-0.848529,-3.042509,-2.126052,-6.186279,-0.600883,-8.366219],[0.367265,-0.907462,-9.996537,-1.397125,-5.613940,-1.623320,7.264446,-3.692536,9.094528,-6.048758],[-7.980604,4.871469,-7.148374,0.536606,-4.198339,-1.497551,-3.345522,-2.634772,0.310127,-0.007225],[-7.720323,5.624995,-1.685459,6.404969,7.380681,0.406901,-8.065274,-9.812644,-1.951469,7.855999],[4.389505,-0.207129,2.828238,-5.643616,2.579913,-9.551197,4.237727,5.684356,-4.878274,-2.350972],[6.105071,2.802547,-2.793359,-9.748875,8.386859,9.101981,4.366247,2.416228,-7.254520,2.526683],[-0.974153,-4.042658,4.577880,2.433419,-2.412333,8.563737,7.488415,-1.071354,-4.898224,-9.936864],[-3.167013,-5.365867,7.012785,-9.832688,0.135491,-9.859377,-7.209219,-2.566285,-1.934017,7.036203],[1.154140,-1.200829,6.993699,-2.060779,2.109669,5.506380,9.792648,-8.652673,2.748511,-2.443100],[-7.556031,5.916383,4.025148,0.688176,1.631859,4.264192,5.349653,-7.251648,-9.223692,9.243629]],[[5.017684,1.054090,-5.108537,-3.379600,9.484709,2.125207,6.101455,-6.007812,-7.279222,-5.202053],[-6.256308,-8.679317,-2.405547,-3.420555,3.699397,-0.419906,-4.700550,7.791313,3.736529,9.822081],[2.743537,9.520017,2.248903,6.153027,1.574410,6.780053,6.813847,1.767973,-3.761239,-1.331198],[4.980795,6.461122,3.343559,4.090046,-4.927482,2.827224,3.807622,-3.442589,-9.251061,-4.879938],[5.202665,6.485910,0.529201,-1.898585,-9.942247,5.912263,-8.229101,1.072643,-6.859206,-2.257823],[1.515788,-7.386900,-4.342778,8.549902,-7.719912,-9.859948,-6.276706,4.787899,9.532734,0.846205],[-9.125926,2.323710,2.313911,-2.707813,2.558623,-4.565967,-0.530215,8.565757,0.961197,5.117688],[-1.615200,-0.197322,4.938713,-4.719476,6.707392,-8.807812,8.105881,-4.971878,2.252474,-4.062674],[-2.328166,4.729256,6.857103,1.893027,-8.307197,-9.377623,2.092978,3.992068,-5.031211,4.777900],[3.651771,-7.996735,5.760474,-9.291433,8.928125,-2.408168,8.360828,0.304324,-6.279929,-9.759481]]], dtype = "float64")#candidate|6873|(12, 10, 10)|const|float64
bop_6874 = relay.floor_mod(var_6872.astype('float64'), const_6873.astype('float64')) # shape=(12, 10, 10)
output = bop_6874
output2 = bop_6874
func_6877 = relay.Function([var_6872,], output)
mod['func_6877'] = func_6877
mod = relay.transform.InferType()(mod)
var_6878 = relay.var("var_6878", dtype = "float64", shape = (12, 10, 1))#candidate|6878|(12, 10, 1)|var|float64
output = func_6877(var_6878)
func_6879 = relay.Function([var_6878], output)
mutated_mod['func_6879'] = func_6879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_6930 = relay.TupleGetItem(func_272_call(), 1)
call_6931 = relay.TupleGetItem(func_274_call(), 1)
output = call_6930
output2 = call_6931
func_6932 = relay.Function([], output)
mod['func_6932'] = func_6932
mod = relay.transform.InferType()(mod)
output = func_6932()
func_6933 = relay.Function([], output)
mutated_mod['func_6933'] = func_6933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5389_call = mod.get_global_var('func_5389')
func_5391_call = mutated_mod.get_global_var('func_5391')
call_6945 = relay.TupleGetItem(func_5389_call(), 0)
call_6946 = relay.TupleGetItem(func_5391_call(), 0)
output = call_6945
output2 = call_6946
func_6947 = relay.Function([], output)
mod['func_6947'] = func_6947
mod = relay.transform.InferType()(mod)
output = func_6947()
func_6948 = relay.Function([], output)
mutated_mod['func_6948'] = func_6948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_6972 = relay.TupleGetItem(func_1270_call(), 0)
call_6973 = relay.TupleGetItem(func_1272_call(), 0)
func_6848_call = mod.get_global_var('func_6848')
func_6849_call = mutated_mod.get_global_var('func_6849')
call_6996 = relay.TupleGetItem(func_6848_call(), 0)
call_6997 = relay.TupleGetItem(func_6849_call(), 0)
output = relay.Tuple([call_6972,call_6996,])
output2 = relay.Tuple([call_6973,call_6997,])
func_7019 = relay.Function([], output)
mod['func_7019'] = func_7019
mod = relay.transform.InferType()(mod)
mutated_mod['func_7019'] = func_7019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7019_call = mutated_mod.get_global_var('func_7019')
call_7020 = func_7019_call()
output = call_7020
func_7021 = relay.Function([], output)
mutated_mod['func_7021'] = func_7021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6375_call = mod.get_global_var('func_6375')
func_6376_call = mutated_mod.get_global_var('func_6376')
call_7055 = relay.TupleGetItem(func_6375_call(), 0)
call_7056 = relay.TupleGetItem(func_6376_call(), 0)
output = relay.Tuple([call_7055,])
output2 = relay.Tuple([call_7056,])
func_7080 = relay.Function([], output)
mod['func_7080'] = func_7080
mod = relay.transform.InferType()(mod)
mutated_mod['func_7080'] = func_7080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7080_call = mutated_mod.get_global_var('func_7080')
call_7081 = func_7080_call()
output = call_7081
func_7082 = relay.Function([], output)
mutated_mod['func_7082'] = func_7082
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7093 = relay.const(-4.542819, dtype = "float64")#candidate|7093|()|const|float64
var_7094 = relay.var("var_7094", dtype = "float64", shape = (16, 9, 9))#candidate|7094|(16, 9, 9)|var|float64
bop_7095 = relay.subtract(const_7093.astype('float64'), var_7094.astype('float64')) # shape=(16, 9, 9)
output = bop_7095
output2 = bop_7095
func_7098 = relay.Function([var_7094,], output)
mod['func_7098'] = func_7098
mod = relay.transform.InferType()(mod)
mutated_mod['func_7098'] = func_7098
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7099 = relay.var("var_7099", dtype = "float64", shape = (16, 9, 9))#candidate|7099|(16, 9, 9)|var|float64
func_7098_call = mutated_mod.get_global_var('func_7098')
call_7100 = func_7098_call(var_7099)
output = call_7100
func_7101 = relay.Function([var_7099], output)
mutated_mod['func_7101'] = func_7101
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7125 = relay.var("var_7125", dtype = "float32", shape = (15, 9, 3))#candidate|7125|(15, 9, 3)|var|float32
uop_7126 = relay.cosh(var_7125.astype('float32')) # shape=(15, 9, 3)
output = relay.Tuple([uop_7126,])
output2 = relay.Tuple([uop_7126,])
func_7130 = relay.Function([var_7125,], output)
mod['func_7130'] = func_7130
mod = relay.transform.InferType()(mod)
var_7131 = relay.var("var_7131", dtype = "float32", shape = (15, 9, 3))#candidate|7131|(15, 9, 3)|var|float32
output = func_7130(var_7131)
func_7132 = relay.Function([var_7131], output)
mutated_mod['func_7132'] = func_7132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2855_call = mod.get_global_var('func_2855')
func_2857_call = mutated_mod.get_global_var('func_2857')
call_7144 = relay.TupleGetItem(func_2855_call(), 0)
call_7145 = relay.TupleGetItem(func_2857_call(), 0)
func_6826_call = mod.get_global_var('func_6826')
func_6827_call = mutated_mod.get_global_var('func_6827')
call_7153 = func_6826_call()
call_7154 = func_6826_call()
func_3567_call = mod.get_global_var('func_3567')
func_3571_call = mutated_mod.get_global_var('func_3571')
var_7171 = relay.var("var_7171", dtype = "float64", shape = (576, 1))#candidate|7171|(576, 1)|var|float64
call_7170 = relay.TupleGetItem(func_3567_call(relay.reshape(var_7171.astype('float64'), [12, 3, 16]), relay.reshape(call_7144.astype('bool'), [216,]), ), 0)
call_7172 = relay.TupleGetItem(func_3571_call(relay.reshape(var_7171.astype('float64'), [12, 3, 16]), relay.reshape(call_7144.astype('bool'), [216,]), ), 0)
output = relay.Tuple([call_7144,call_7153,call_7170,var_7171,])
output2 = relay.Tuple([call_7145,call_7154,call_7172,var_7171,])
func_7175 = relay.Function([var_7171,], output)
mod['func_7175'] = func_7175
mod = relay.transform.InferType()(mod)
var_7176 = relay.var("var_7176", dtype = "float64", shape = (576, 1))#candidate|7176|(576, 1)|var|float64
output = func_7175(var_7176)
func_7177 = relay.Function([var_7176], output)
mutated_mod['func_7177'] = func_7177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4805_call = mod.get_global_var('func_4805')
func_4806_call = mutated_mod.get_global_var('func_4806')
call_7194 = func_4805_call()
call_7195 = func_4805_call()
func_5136_call = mod.get_global_var('func_5136')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_7203 = relay.TupleGetItem(func_5136_call(), 1)
call_7204 = relay.TupleGetItem(func_5138_call(), 1)
const_7210 = relay.const([[3,5,10,7,5,3,-9,-4,3,2,-9,-4,-1,-4,-4,3,4,7,3,8,-5,-5,-5,-1,-1,2,-5,-6],[-1,-1,5,-4,3,-2,3,-6,3,3,8,-6,-8,1,-7,2,-7,4,-7,8,-8,-6,-10,-1,4,1,-9,3],[5,1,-2,1,5,1,4,4,2,6,4,5,1,-2,-2,8,-10,3,-1,1,-10,10,2,7,-5,5,8,9],[-7,2,7,-9,6,-1,6,2,6,9,7,-1,-7,-4,-8,6,8,-5,7,-4,-5,9,8,-7,-5,-2,2,-7],[-10,6,7,-3,10,-10,1,-2,-10,10,-4,4,-5,4,-10,6,3,9,-4,3,-10,2,8,2,5,-7,10,10],[8,1,-4,-1,9,-7,4,-6,4,10,2,-9,3,-5,9,-8,-9,8,-8,-2,-1,-9,-8,1,-2,1,2,-10]], dtype = "int64")#candidate|7210|(6, 28)|const|int64
bop_7211 = relay.bitwise_or(call_7194.astype('int32'), relay.reshape(const_7210.astype('int32'), relay.shape_of(call_7194))) # shape=(6, 28)
bop_7214 = relay.bitwise_or(call_7195.astype('int32'), relay.reshape(const_7210.astype('int32'), relay.shape_of(call_7195))) # shape=(6, 28)
var_7215 = relay.var("var_7215", dtype = "int64", shape = (6, 28))#candidate|7215|(6, 28)|var|int64
bop_7216 = relay.floor_divide(call_7194.astype('float32'), relay.reshape(var_7215.astype('float32'), relay.shape_of(call_7194))) # shape=(6, 28)
bop_7219 = relay.floor_divide(call_7195.astype('float32'), relay.reshape(var_7215.astype('float32'), relay.shape_of(call_7195))) # shape=(6, 28)
bop_7226 = relay.less(bop_7211.astype('bool'), relay.reshape(const_7210.astype('bool'), relay.shape_of(bop_7211))) # shape=(6, 28)
bop_7229 = relay.less(bop_7214.astype('bool'), relay.reshape(const_7210.astype('bool'), relay.shape_of(bop_7214))) # shape=(6, 28)
output = relay.Tuple([call_7203,bop_7216,bop_7226,])
output2 = relay.Tuple([call_7204,bop_7219,bop_7229,])
func_7230 = relay.Function([var_7215,], output)
mod['func_7230'] = func_7230
mod = relay.transform.InferType()(mod)
var_7231 = relay.var("var_7231", dtype = "int64", shape = (6, 28))#candidate|7231|(6, 28)|var|int64
output = func_7230(var_7231)
func_7232 = relay.Function([var_7231], output)
mutated_mod['func_7232'] = func_7232
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7282 = relay.var("var_7282", dtype = "float64", shape = (4, 14, 13))#candidate|7282|(4, 14, 13)|var|float64
uop_7283 = relay.log(var_7282.astype('float64')) # shape=(4, 14, 13)
output = relay.Tuple([uop_7283,])
output2 = relay.Tuple([uop_7283,])
func_7294 = relay.Function([var_7282,], output)
mod['func_7294'] = func_7294
mod = relay.transform.InferType()(mod)
mutated_mod['func_7294'] = func_7294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7295 = relay.var("var_7295", dtype = "float64", shape = (4, 14, 13))#candidate|7295|(4, 14, 13)|var|float64
func_7294_call = mutated_mod.get_global_var('func_7294')
call_7296 = func_7294_call(var_7295)
output = call_7296
func_7297 = relay.Function([var_7295], output)
mutated_mod['func_7297'] = func_7297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5389_call = mod.get_global_var('func_5389')
func_5391_call = mutated_mod.get_global_var('func_5391')
call_7301 = relay.TupleGetItem(func_5389_call(), 2)
call_7302 = relay.TupleGetItem(func_5391_call(), 2)
var_7304 = relay.var("var_7304", dtype = "float32", shape = (455, 7))#candidate|7304|(455, 7)|var|float32
bop_7305 = relay.bitwise_or(call_7301.astype('uint16'), var_7304.astype('uint16')) # shape=(455, 7)
bop_7308 = relay.bitwise_or(call_7302.astype('uint16'), var_7304.astype('uint16')) # shape=(455, 7)
bop_7310 = relay.less(call_7301.astype('bool'), var_7304.astype('bool')) # shape=(455, 7)
bop_7313 = relay.less(call_7302.astype('bool'), var_7304.astype('bool')) # shape=(455, 7)
uop_7315 = relay.log2(call_7301.astype('float32')) # shape=(455, 1)
uop_7317 = relay.log2(call_7302.astype('float32')) # shape=(455, 1)
output = relay.Tuple([bop_7305,bop_7310,uop_7315,])
output2 = relay.Tuple([bop_7308,bop_7313,uop_7317,])
func_7322 = relay.Function([var_7304,], output)
mod['func_7322'] = func_7322
mod = relay.transform.InferType()(mod)
var_7323 = relay.var("var_7323", dtype = "float32", shape = (455, 7))#candidate|7323|(455, 7)|var|float32
output = func_7322(var_7323)
func_7324 = relay.Function([var_7323], output)
mutated_mod['func_7324'] = func_7324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3662_call = mod.get_global_var('func_3662')
func_3663_call = mutated_mod.get_global_var('func_3663')
call_7345 = relay.TupleGetItem(func_3662_call(), 0)
call_7346 = relay.TupleGetItem(func_3663_call(), 0)
func_2428_call = mod.get_global_var('func_2428')
func_2430_call = mutated_mod.get_global_var('func_2430')
const_7353 = relay.const([0.191861,-3.021339,-9.705579,6.020217,0.496984,-6.199272,2.289465,-5.110645,6.725467,7.608100,8.331788,2.141462,9.957405,-2.271537,2.101460,4.549691,-2.089269,4.702830,5.032570,2.871419,0.422458,2.483343,3.848558,-1.419325,-8.280604,1.741518,-7.713154,7.501083,8.622143,-9.298648,-6.123719,4.568830,-7.460057,8.316666,-9.154147,-7.329487,-2.076436,-9.689376,7.395386,0.099166,8.772494,8.788209,1.979504,0.454926,-7.131239,-3.502275,3.213779,0.995130,-9.437003,4.187264,0.867668,-2.183828,-8.977947,2.945553,1.683745,0.268599,-7.769565,-4.962796,5.412281,-0.118899,-2.299856,-4.819372,6.640142,5.423505,-7.740914,-1.793660,-3.517359,-8.620260,0.363055,-4.110631,-3.852607,9.555053,-1.736512,-7.195968,-1.778761,8.566835,4.996509,-2.365921,-5.285757,7.466560,6.456736,-2.578299,-4.377546,-9.039070,7.443848,0.469938,-3.724865,-5.508231,-1.691395,9.532397,2.164990,5.559127,-8.079777,5.689181,4.668178,-9.067811,-9.292945,-4.629411,4.501715,9.543686,6.119411,-2.214140,1.602045,-7.344115,7.077176,-2.589861,3.408095,-4.054684,-5.234260,-5.957332,-7.316182,-0.550046,0.673041,4.784968,6.756301,6.697860,9.826160,-7.987038,-6.357328,2.951175,-3.315491,4.329865,9.068059,-5.204631,0.879771,-2.675277,1.907449,4.504123,3.773337,9.282866,1.517436,-2.709506,-0.232720,0.705496,7.105295,-3.717677,0.664474,4.488160,1.856761,-5.884841,-2.746499,-1.377541,7.597990,0.073797,2.804320,4.839953,1.179946,6.101908,-7.622007,3.289504,5.770943,-3.640112,2.843868,-0.437160,3.125835,5.527311,7.799627,7.237385,8.242925,9.348911,7.905124,4.233549,-3.668077,-6.078971,-6.464619,0.241533,5.045642,-3.076221,7.365056,-5.640364,4.155839,1.833018,0.290764,1.954478,5.283092,0.658352,3.038419,8.450195,-5.762450,-4.663325,0.806471,-0.372770,0.729815,7.647542,1.902523,3.263310,-0.519834,3.502537,8.733527,-1.634903,-4.268761,6.886132,2.046606,8.164244,-1.256135,-3.184729,4.141797,0.723472,4.805810,-7.253172,-0.878265,6.056593,-0.535613,-2.870307,4.118714,-2.678270,2.385130,7.390555,-1.404421,-8.203163,-5.478029,0.531896,1.810539,8.913917,4.563315,-6.893165,5.412513,-2.759389,-8.702339,-9.764657,-6.792108,8.443082,-4.112021,-6.084319,-1.487172,-6.372861,5.682354,-6.904138,-6.934069,1.499451,5.448418,2.491740,9.599186,-6.447786,-7.691056,6.269932,8.298041,-0.267561,2.571642,4.797403,5.324568,-3.351664,7.747365,-3.873051,-7.310613,2.133241,6.914095,6.302819,1.865398,-2.366560,-5.480840,-5.046059,0.368431,6.525248,9.572428,-9.413789,-2.337716,0.225928,1.669481,8.591744,7.113581,-7.303010,8.857468,6.675771,5.306657,6.049539,8.039591,-9.619386,-8.521336,9.683883,-0.056229,1.087679,-2.509823,-2.966810,-4.343280,-1.983200,-6.155695,-4.473706,-8.204334,-7.861390,7.197513,9.537744,0.202592,4.296943,5.305918,8.493076,-7.349189,6.089277,5.000163,3.986132,9.331716,2.492937,-2.968652,-2.554690,2.090771,-0.856136,-7.341227,7.021498,1.346352,3.625495,2.332979,-1.288863,6.962274,1.056145,4.199843,-7.935319,-9.319139,5.015203,5.293459,2.637175,-1.742467,-4.587133,8.695808,9.891840,-1.653947,4.979371,6.522999,-3.922721,6.090892,-9.572572,-0.461384,-8.238085,-5.295323,7.150683,0.490174,5.646780,-4.820697,-4.489859,6.944116,0.078777,-7.962094,-7.538090,-7.461783,2.833325,-9.665968,7.268006,-3.684520,4.419180,1.871623,8.811090,5.866932,-0.855070,-7.693837,2.270940,-5.266403,5.540066,4.225931,6.405315,-1.119447,-0.477562,-0.083379,6.558771,7.792576,2.067136,0.143856,8.098713,2.045272,9.404745,-7.708880,-9.554833,9.361791,7.854482,2.816341,-4.168130,2.247071,-6.234212,-2.324485,8.139840,-8.592767,-0.192879,9.788792,-1.436145,-9.948945,-6.945595,-5.208098,1.003483,-9.469509,-4.160043,5.312041,-2.406986,4.830371,-1.635476,-6.553713,8.531658,6.606983,4.802392,7.104960,1.867971,0.774284,-9.331890,-0.503225,9.064053,7.269776,-8.143163,-2.817394,4.212366,6.623497,-3.791653,4.942311,-8.880809,4.266877,6.682197,3.176082,-9.504774,-0.803001,-9.058735,9.461047,-2.042385,-5.251435,7.476120,9.567537,-0.338377,4.919545,-0.174850,3.536303,1.124196,-5.660342,7.796585,2.235978,-3.422611,9.036825,0.966959,-1.155089,9.906599,-6.802387,-6.491932,8.230089,7.140701,2.263952,-2.639175,-8.868703,0.185276,-9.133419,5.348357,7.102132,-8.591028,-1.152117,1.282875,2.471345,7.256152,7.619041,1.850359,8.153690,0.715524,-2.561983,9.726256,9.447194,-5.190996,1.697213,-4.028939,8.120380,5.090280,-0.138137,5.668472,5.438091,1.054916,-3.615833,-0.672587,5.919110,-8.528232,6.702820,9.119862,-7.788665,-1.803224,9.224180,-2.342838,4.758501,-5.652053,-7.595845,0.673087,2.634525,8.806881,8.836399,6.547930,2.711317,0.197942,1.631140,-8.198502,-0.374090,5.782881,2.020985,-4.179443,-9.186623,-9.047455,-5.841407,-6.826951,-7.556334,1.642270,8.066425,6.037964,-8.519139,7.415856,9.995510,-7.618100,6.066194,5.905186,6.578622,6.541783,-1.129239,5.098409,-5.189582,-4.024439,7.569559,-2.555912,-0.642664,8.826968,-9.429925,-1.622910,-9.133627,6.770483,1.537926,-5.203915,7.295839,-4.083247,3.009988,-8.820653,4.916622,9.883823,8.102085,-4.709288,4.375458,-2.745010,-2.497317,0.815468,7.285083,-6.583982,3.037918,-5.148312,3.388780,-7.942219,-2.511496,-1.971624,-9.828522,-0.604772,7.729744,9.313228,-1.131396,0.881219,2.011118,-5.543348,0.213260,4.336296,6.993139,8.071168,-4.372499,-6.784649,0.018903,-4.610435,-5.018667,6.318973,1.864093,-9.789206,-3.204077,2.289208,-7.816398,6.019793,-5.182891,-9.451847,-7.788275,-9.024102,4.174684,6.755590,5.522964,-9.359697,-9.754552,-8.717196,5.680765,3.916493,-8.996731,6.875765,-2.332273,-1.030342,9.981529,4.597986,3.616551,-4.192765,-7.207309,1.774803,7.284282,0.472117,4.144105,-8.495588,-3.027356,-5.877002,-5.975667,9.252983,-9.478409,4.317485,-7.316692,2.119423,3.486231,-6.925293,7.135363,8.073497,-1.074140,-0.559229,-8.198880,-1.852562,2.064752,7.673708,-8.980692,-4.104609,8.143400,-9.064005,-3.742646,4.551089,1.918659,5.340515,7.594691,1.206345,9.529049,7.783187,-4.691828,-3.712007,-8.838862,5.658442,-1.098518,-2.308965,-2.508002,9.473470,-1.996178,-6.696213,6.626126,5.246050,-2.738257,-0.658296,-0.816774,-2.152369,5.209111,-2.958213,-0.550813,-5.436601,-9.506856,-1.870245,1.826943,7.136172,-8.100624,8.229960,-4.834257,-4.559959,6.589292,-0.634150,-2.737497,9.559921,-1.395198,-2.884819,8.408457,7.659994,5.210773,-9.864837,-3.137943,-7.062205,5.592195,-5.389427,-1.199919,8.539242,1.213328,-3.243419,-9.045319,1.977216,2.056316,6.372488,-1.211996,-6.288747,2.181335,-2.071411,9.316815,-7.125196,-1.703326,-8.303480,-3.841054,-8.441069,9.127333,6.431054,-7.224771,-8.935869,-3.300091,2.170095,8.787420,-7.300833,-8.547783,-8.299579,-2.817754,3.989301,7.573104,0.136912,5.198121,7.928678,-7.891376,-5.012164,0.578207,5.660203,-5.493823,-4.512898,-4.920606,-2.115077,8.139620,-1.211528,-1.743487,-9.054475,0.901368,4.255647,5.933511,-8.044729,3.710679,5.507999,6.841799,0.595459,8.521339,2.119670,-4.766248,-2.327595,-8.341368,1.246183,-3.364588,-7.495429,-2.369552,-7.647746,-8.244547,2.332128,0.563999,-2.483885,9.884588,7.804099,8.594590,9.344239,-0.462187,4.545414,-4.646746,2.091563,-9.750575,5.490694,1.860465,5.894349,-4.996632,-1.985449,2.957796,-6.171008,-1.379352,0.021692,6.182111,6.399861,-2.741292,-0.657636,-7.469469,-6.919042,-6.924751,4.765738,6.688101,2.070893,6.270496,-2.185181,9.535773,-2.577222,-0.697917,9.054200,-5.451288,1.467147,-4.712502,6.096231,-4.556855,9.613366,6.761442,-4.261275,2.995276,-2.027868,9.868067,6.539729,-6.423940,-5.577309,5.989163,-7.913373,6.826029,0.182976,5.114020,-3.857763,-2.806469,-0.334263,-7.547975,-6.061438,5.640619,-1.796914,8.259501,4.323827,9.914961,-7.175448,1.250919,-7.854931,0.199899,-0.371096,4.253086,-8.054096,0.773152,1.922792,7.875359,6.814823,9.218781,-7.413811,-0.402493,-9.139011,3.149215,-2.523582,0.590659,1.810198,-8.088634,8.934558,-1.381326,6.288802,1.819202,9.017049,0.779697,7.320398,9.591170,3.853079,5.826337,8.266303,6.547576,3.106152,3.327950,4.325385,7.702172,7.935216,-7.392834,8.268720,0.216798,-3.221315,9.685158,9.013096,7.871958,-6.074121,-0.361561,-6.609560,-9.085258,-8.353851,-1.899127,1.130025,5.260530,-7.035424,-8.899272,2.364193,-0.355446,-0.969660,7.836233,-3.613927,-0.862505,2.552247,1.494592,-0.055178,4.535210,0.452557,-1.984972,7.163464,6.645688,1.577351,0.572242,8.288750,6.786020,-2.237517,-3.636591,3.626473,9.545023,7.057201,-9.015242,-7.567553,1.685172,-0.418111,9.400907,4.502296,9.347101,-9.076191,6.280045,-4.503236,4.184878,6.023567,-0.396998,-5.783705,6.039072,-2.526006,-0.708606,0.274353,-8.259415,2.523346,-9.379328,-4.102221,-3.117048,-8.154358,-2.772691,-6.036117,8.320990,5.880398,-8.886160,-4.543317,-2.611167,-3.613366,5.075227,-7.949076,0.017795,2.059163,-1.947700,4.746884,-3.910966,-1.206711,-4.539511,-3.413955,-5.077348,2.424602,-8.046100,-8.002203,-9.355902,0.414601,-3.156622,4.825789,4.956540,3.999844,-6.602996,-3.945060,0.122589,-7.862966,2.874307,9.748460,-5.299379,2.971559,-1.130391,3.605017,-3.539458,2.401373,-5.859180,-3.978219,7.133715,5.075662,-1.587407,8.617682,-4.095650,3.614813,-2.712177,6.856407,-9.335815,3.561700,-0.645217,8.866813,7.540177,-4.195774,-3.141708,-1.948089,-0.702082,4.123451,0.189882,-9.870294,-2.439007,-8.974494,7.266594,-3.965469,-6.200208,-2.716872,-1.167347,1.668818,-7.768287,-6.162110,-6.164584,2.901638,-9.805476,8.318876,8.953890,-5.879909,2.730683,-6.026003,-4.636379,-7.107894,2.259257,-9.838845,9.150659,3.405688,0.436164,-4.616633,-0.991493,-9.366381,-1.649514,0.795679,-0.067719,-6.421948,-7.908281,-8.874622,1.468756,5.080357,5.094474,-4.320823,3.288868,2.191833,2.707000,-8.665091,0.622157,4.384605,-2.668099,8.440161,-1.338144,-9.605674,-6.181428,7.869349,-5.251971,-6.734790,-9.818518,-1.416666,3.592975,-4.061394,7.412162,-4.233899,-6.636986,-2.482118,-9.005815,9.618705,6.401491,8.578996,-9.914579,4.764680,9.342080,-8.999415,4.977200,6.771891,-9.654542,2.919066,-1.280947,-9.978175,0.153721,4.863518,-8.476566,-1.932669,9.153147,-0.785982,8.194503,-7.189872,7.698598,-7.274165,7.979127,9.999019,-3.448332,4.742478,4.823475,0.513140,-8.154673,-1.612938,5.042083,1.464349,7.229180,-3.379448,2.005977,8.925189,5.952081,2.345617,-9.649362,1.846555,-0.598837,0.542443,-8.460918,-8.779510,-1.849346,-2.991585,-8.370362,-4.012846,2.049795,-4.038929,4.044731,7.541212,5.455981,2.020162,-2.156876,-6.243309,5.107509,-1.426057,-3.767683,-4.786512,0.508749,-7.422892,-8.940958,0.343492,6.740437,6.695400,-6.007807,-3.460725,3.919628,5.172214], dtype = "float64")#candidate|7353|(1080,)|const|float64
call_7352 = relay.TupleGetItem(func_2428_call(relay.reshape(const_7353.astype('float64'), [1080,])), 2)
call_7354 = relay.TupleGetItem(func_2430_call(relay.reshape(const_7353.astype('float64'), [1080,])), 2)
output = relay.Tuple([call_7345,call_7352,const_7353,])
output2 = relay.Tuple([call_7346,call_7354,const_7353,])
func_7370 = relay.Function([], output)
mod['func_7370'] = func_7370
mod = relay.transform.InferType()(mod)
mutated_mod['func_7370'] = func_7370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7370_call = mutated_mod.get_global_var('func_7370')
call_7371 = func_7370_call()
output = call_7371
func_7372 = relay.Function([], output)
mutated_mod['func_7372'] = func_7372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4835_call = mod.get_global_var('func_4835')
func_4836_call = mutated_mod.get_global_var('func_4836')
call_7384 = func_4835_call()
call_7385 = func_4835_call()
func_4864_call = mod.get_global_var('func_4864')
func_4868_call = mutated_mod.get_global_var('func_4868')
var_7392 = relay.var("var_7392", dtype = "int64", shape = (21,))#candidate|7392|(21,)|var|int64
const_7393 = relay.const([3,6,6,-8,-6,-5,-2,4,1,6,6,9,5,-8,2,-5,-5,-10,2,-8,-3,-9,5,-2,-9,-4,8,-10,5,-10,-9,6,8,5,-6,-8,7,3,-1,8,-1,6,6,-4,3,-2,9,-6,-3,-6,-5,7,10,-6,3,10,8,5,1,7,-3,8,-6,-10,-7,-8,-1,-4,3,3,-4,1,-10,-8,-6,-6,-5,-3,-1,1,-9,8,-4,-10,-4,4,-9,-2,1,-1,6,-10,-4,-5,3,-2,-5,-2,-5,-7,-7,-9,-5,-5,-10,7,-4,10,-7,-4,8,-5,-8,-1,9,-4,-8,3,3,-2,-4,2,6,-7,-6,5,7,-7,7,10,6,4,-6,-7,-5,-5,-8,7,6,6,5,5,3,6,2,6,9,-3,-7,7,1,-10,-6,2,-1,5,-2,-7,-4,5,-9,5,-10,-7,1,10,-6,1,-9,6,-3,-7,3,2,-7,3,-9,-5,9,8,8,9,8,7,-5,7,-6,-7,-8,-8,5,10,2,-4,9,-8,-8,2,9,3,-2,3,7,-9,-8,-10,10,8,-7,-2,4,3,9,10,-5,-3,7,7,6,7,-4,-9,-6,6,-1,10,-10,-9,-8,-10,-4], dtype = "int64")#candidate|7393|(231,)|const|int64
call_7391 = relay.TupleGetItem(func_4864_call(relay.reshape(var_7392.astype('int64'), [3, 1, 7]), relay.reshape(const_7393.astype('int64'), [3, 11, 7]), ), 3)
call_7394 = relay.TupleGetItem(func_4868_call(relay.reshape(var_7392.astype('int64'), [3, 1, 7]), relay.reshape(const_7393.astype('int64'), [3, 11, 7]), ), 3)
func_3877_call = mod.get_global_var('func_3877')
func_3880_call = mutated_mod.get_global_var('func_3880')
var_7405 = relay.var("var_7405", dtype = "int16", shape = (819,))#candidate|7405|(819,)|var|int16
call_7404 = relay.TupleGetItem(func_3877_call(relay.reshape(var_7405.astype('int16'), [9, 7, 13]), relay.reshape(var_7405.astype('int16'), [9, 7, 13]), ), 3)
call_7406 = relay.TupleGetItem(func_3880_call(relay.reshape(var_7405.astype('int16'), [9, 7, 13]), relay.reshape(var_7405.astype('int16'), [9, 7, 13]), ), 3)
uop_7409 = relay.sinh(call_7404.astype('float32')) # shape=(9, 7, 13)
uop_7411 = relay.sinh(call_7406.astype('float32')) # shape=(9, 7, 13)
output = relay.Tuple([call_7384,call_7391,var_7392,const_7393,var_7405,uop_7409,])
output2 = relay.Tuple([call_7385,call_7394,var_7392,const_7393,var_7405,uop_7411,])
func_7421 = relay.Function([var_7392,var_7405,], output)
mod['func_7421'] = func_7421
mod = relay.transform.InferType()(mod)
mutated_mod['func_7421'] = func_7421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7421_call = mutated_mod.get_global_var('func_7421')
var_7423 = relay.var("var_7423", dtype = "int64", shape = (21,))#candidate|7423|(21,)|var|int64
var_7424 = relay.var("var_7424", dtype = "int16", shape = (819,))#candidate|7424|(819,)|var|int16
call_7422 = func_7421_call(var_7423,var_7424,)
output = call_7422
func_7425 = relay.Function([var_7423,var_7424,], output)
mutated_mod['func_7425'] = func_7425
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7451 = relay.var("var_7451", dtype = "float64", shape = ())#candidate|7451|()|var|float64
var_7452 = relay.var("var_7452", dtype = "float64", shape = (2, 13, 2))#candidate|7452|(2, 13, 2)|var|float64
bop_7453 = relay.power(var_7451.astype('float64'), var_7452.astype('float64')) # shape=(2, 13, 2)
output = relay.Tuple([bop_7453,])
output2 = relay.Tuple([bop_7453,])
func_7460 = relay.Function([var_7451,var_7452,], output)
mod['func_7460'] = func_7460
mod = relay.transform.InferType()(mod)
var_7461 = relay.var("var_7461", dtype = "float64", shape = ())#candidate|7461|()|var|float64
var_7462 = relay.var("var_7462", dtype = "float64", shape = (2, 13, 2))#candidate|7462|(2, 13, 2)|var|float64
output = func_7460(var_7461,var_7462,)
func_7463 = relay.Function([var_7461,var_7462,], output)
mutated_mod['func_7463'] = func_7463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5886_call = mod.get_global_var('func_5886')
func_5887_call = mutated_mod.get_global_var('func_5887')
call_7557 = func_5886_call()
call_7558 = func_5886_call()
output = relay.Tuple([call_7557,])
output2 = relay.Tuple([call_7558,])
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
func_1388_call = mod.get_global_var('func_1388')
func_1389_call = mutated_mod.get_global_var('func_1389')
call_7586 = relay.TupleGetItem(func_1388_call(), 0)
call_7587 = relay.TupleGetItem(func_1389_call(), 0)
output = call_7586
output2 = call_7587
func_7588 = relay.Function([], output)
mod['func_7588'] = func_7588
mod = relay.transform.InferType()(mod)
output = func_7588()
func_7589 = relay.Function([], output)
mutated_mod['func_7589'] = func_7589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2211_call = mod.get_global_var('func_2211')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_7598 = func_2211_call()
call_7599 = func_2211_call()
func_188_call = mod.get_global_var('func_188')
func_191_call = mutated_mod.get_global_var('func_191')
const_7603 = relay.const([-0.431000,-1.188235,-1.920770,-2.944281,-9.573007,-0.668120,-6.206903,3.420233,-8.649582,-9.480235,5.783705,-3.076911,5.740271,-5.410920,-5.167804,5.430604,-1.545535,-7.227230,-2.551111,-8.641154,-3.288970,-9.807303,-9.112544,0.569815,-5.402634,-0.141300,4.923739,3.907082,-7.936818,9.969524,-8.967662,5.031979,-7.165263,4.334360,-4.686294,3.089176,3.346442,1.664752,9.850287,-8.495111,-9.081462,7.531052,7.029961,-2.092610,0.959116,1.288309,-1.907477,-4.992751,-2.261017,-7.133953,8.262207,1.256435,3.131449,-5.200915,5.935058,-7.373766,2.812252,6.590628,0.718418,-4.512930,-3.088122,-1.346526,-7.860593,8.760636,-5.988739,-5.907967,-5.308663,-0.967158,-1.760590,-9.945944,-5.063992,-0.450649,5.286875,-3.707617,7.016993,2.668785,-0.139442,8.718899,-9.973160,2.183054,-4.211612,7.862375,9.538533,-6.902566,-7.696075,-1.480962,-2.940094,0.929095,-0.595898,-7.413234,-1.207307,6.980454,1.655930,-9.783858,-1.512610,-1.269597,5.590825,8.557000,-8.120901,-9.509585,-4.707960,8.674785,8.526465,-8.084528,-8.436252,-0.961722,-8.837223,-2.075321,-6.711659,-5.828194,-6.546066,4.205337,-1.331344,7.051673,-9.791174,8.189540,-4.740558,8.444105,6.204990,8.357651,-4.702932,0.235519,-3.038883,-3.314135,-6.532794,3.238263,-8.703708,-1.330332,5.703143,9.891733,1.965087,-5.756846,1.676966,-0.127496,-8.015113,-3.460314,3.497795,9.450840,6.037169,-3.313867,-3.564243,8.031110,-2.541634,1.708893,3.196164,5.220434,-7.538123,-4.117717,-3.236087,-3.292248,-2.592935,8.147089,-7.235938,8.770276,2.197874,7.537049,7.393861,-0.480075,-6.708617,2.168613,-2.067341,3.408429,5.415868,-5.013485,-2.224394,-5.365134,1.661242,-8.344845], dtype = "float32")#candidate|7603|(168,)|const|float32
call_7602 = relay.TupleGetItem(func_188_call(relay.reshape(const_7603.astype('float32'), [6, 4, 7]), relay.reshape(const_7603.astype('float32'), [6, 4, 7]), ), 0)
call_7604 = relay.TupleGetItem(func_191_call(relay.reshape(const_7603.astype('float32'), [6, 4, 7]), relay.reshape(const_7603.astype('float32'), [6, 4, 7]), ), 0)
output = relay.Tuple([call_7598,call_7602,const_7603,])
output2 = relay.Tuple([call_7599,call_7604,const_7603,])
func_7606 = relay.Function([], output)
mod['func_7606'] = func_7606
mod = relay.transform.InferType()(mod)
output = func_7606()
func_7607 = relay.Function([], output)
mutated_mod['func_7607'] = func_7607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6630_call = mod.get_global_var('func_6630')
func_6631_call = mutated_mod.get_global_var('func_6631')
call_7631 = func_6630_call()
call_7632 = func_6630_call()
output = call_7631
output2 = call_7632
func_7634 = relay.Function([], output)
mod['func_7634'] = func_7634
mod = relay.transform.InferType()(mod)
output = func_7634()
func_7635 = relay.Function([], output)
mutated_mod['func_7635'] = func_7635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5518_call = mod.get_global_var('func_5518')
func_5520_call = mutated_mod.get_global_var('func_5520')
call_7752 = func_5518_call()
call_7753 = func_5518_call()
const_7756 = relay.const([[-6,1,7,-4,8,1,8,10,-1,4,6,-4,-10,9,3,8,-2,-3,-4,-3,-10,4,8,1,10,5,-3,-5,3,-5,-3,8,-3,8,9,2,6,9,-9,-5,10,-5,9,5,7,8,4,7,6,7,-7,-7,2,-8,8,1,3,8,7,4,5,6,-8,9,6,-1,2,7,6,6,-9,2,5,6,5,-8,9,-2,-4,-3,6,5,-2,3,-8,-1,-7,2,3,6,5,-8,5,-3,10,3,-10,5,1,-1,8,9,-7,9,-9,9,8,-10,9,6,-1,-5,-7,6,-10,-10,-1,6,-2,-7,2,4,-5,-5,-2,-4,-9,-6,1,6,-1,10,5,-9,10,9,3,-2,-10,1,-9,4,3,-6,-4,-6,9,6,-9,-3,2,-1,-5,-1,3,6,-6,1,4,4,10,-2,3,4,-4,2,-9,1,9,9,-4,3,-9,7,-4,1,10,-2,3,6]], dtype = "uint16")#candidate|7756|(1, 180)|const|uint16
bop_7757 = relay.bitwise_and(call_7752.astype('uint8'), relay.reshape(const_7756.astype('uint8'), relay.shape_of(call_7752))) # shape=(1, 180)
bop_7760 = relay.bitwise_and(call_7753.astype('uint8'), relay.reshape(const_7756.astype('uint8'), relay.shape_of(call_7753))) # shape=(1, 180)
output = bop_7757
output2 = bop_7760
func_7770 = relay.Function([], output)
mod['func_7770'] = func_7770
mod = relay.transform.InferType()(mod)
output = func_7770()
func_7771 = relay.Function([], output)
mutated_mod['func_7771'] = func_7771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5389_call = mod.get_global_var('func_5389')
func_5391_call = mutated_mod.get_global_var('func_5391')
call_7812 = relay.TupleGetItem(func_5389_call(), 0)
call_7813 = relay.TupleGetItem(func_5391_call(), 0)
func_1210_call = mod.get_global_var('func_1210')
func_1214_call = mutated_mod.get_global_var('func_1214')
const_7815 = relay.const([-9.528983,-8.376049,6.473743,-1.692122,-1.235074,8.582765,8.610872,-5.397080,4.380866,-7.216648,0.952736,-2.380194,2.532610,5.458252,2.274497,-7.963869,-9.551495,3.817228,6.110198,-4.136398,5.234155,-7.562583,-0.180957,4.238207,-7.473648,4.380262,5.565585,-3.908215,8.496015,-1.577617,-8.497917,-7.208174,1.849644,-4.127711,-1.246153,-0.225897,-0.996521,-1.526616,9.596068,-9.082183,-1.225446,-5.786099,-0.913256,-0.999908,-5.960430,-5.678261,0.933101,2.977463,-5.164815,-5.656954,0.521280,1.434687,1.266144,-4.952567,3.511048,-2.642531,5.588787,-1.335450,-1.027330,9.634970,1.695263,1.407244,-4.455406,9.653570,-5.983218,0.500571,1.820006,-4.811614,0.424517,7.555061,7.732398,-2.502231,-8.063153,-8.746795,8.204744,-6.767360,-5.775360,8.716083,-6.192779,1.633888,-7.028291,-3.201501,1.806042,7.178165,-9.339915,-8.819333,-2.497869,-9.749446,8.699314,1.027443,-1.389362,7.211420,0.469359,1.582977,4.245471,9.885396,-9.740016,5.672375,-5.992879,-9.517635,-4.929751,-0.975328,2.242402,6.966445,-2.236347,3.151013,-3.796684,5.047226,8.482702,-8.267228,7.902061,3.016206,2.284566,-3.468129,5.509757,-5.469714,8.810800,-8.638775,3.039728,3.583999,7.847458,-8.483902,9.415231,6.676974,8.056376,5.171359,4.881150,-6.177647,-2.986640,-4.967618,0.979626,0.663292,-5.660530,6.270319,6.222874,5.404142,7.750374,3.515060,4.918645,8.685939,-0.808214,2.248025,7.591748,-9.016834,-8.884005,2.474229,-0.052550,-8.515916,1.871864,-3.678616,-1.044902,6.757313,-3.956463,-8.562933,4.805713,-2.067188,6.522486,-8.605769,3.222851,-1.301462,3.079301,8.848687,-6.721100,-1.117378,1.893097,-9.283106,-6.129470,9.314137,-6.897936,-0.257244,3.490609,9.283257,5.383748,-0.110828,8.269099,-7.571262,-6.720125,-8.779274,-0.469543,-8.807314,8.281551,0.008791,-7.359806,-7.141070,8.464375,1.985666,2.639379,1.632104,-1.542499,5.636408,-4.894641,-5.306547,6.984087,2.244801,-6.966793,1.865495,-9.963309,3.845214,9.535312,-0.317002,0.136094,-0.362838,-7.399943,9.213121,4.859931,-0.595970,-9.479443,-0.275846,8.064692,6.666869,-1.579215,-0.427849,-5.415709,5.436793,3.983190,-8.972647,0.926514,-8.849714,-4.720490,-5.463045,-1.337720,3.565873,-7.536925,9.293213,6.923861,0.521442,2.741259,-2.637529,2.762541,-8.447702,5.046060,9.566960,7.565102,9.350527,1.026748,6.038929,-4.083198,6.830350,-9.333433,5.496627,2.554811,8.514219,-7.307751,-5.548015,-1.127968,-1.244861,0.634823,-2.133246,1.510951,-0.704401,-0.160158,5.338212,-1.168949,1.903406,2.884758,-3.760246,9.076211,4.402541,-9.046316,9.888818,-3.070924,-4.765670,-0.284328,-5.865094,-7.672956,-4.507560,-1.329610,-8.722754,-2.466999,-1.029524,-3.346690,2.099759,-0.177975,8.000616,-9.952932,9.353989,-1.247605,5.553198,4.891825,9.661906,-5.894926,-6.414400,9.035956,-3.540495,-7.283224,1.652630,4.762099,-5.748604,7.779135,-5.050241,-7.859350,5.037338,-1.126085,2.739732,-7.411222,7.686328,6.506993,-1.767900,-3.749615,-7.784753,6.591810,5.477695,-7.923624,-0.350272,3.639235,-0.126023,9.628325,0.490927,-4.844188,9.020368,7.012985,9.472716,-0.927349,2.510997,-1.466494,6.592904,1.468707,5.961743,-0.829036,9.029591,-2.443507,5.831854,3.288532,5.246637,-0.574716,1.126846,-4.216674,-0.582836,-9.507337,2.749810,9.667182,-5.671403,-9.981914,9.879906,9.344929,-9.686283,-5.973975,3.411600,-9.733632,2.351831,9.821283,-8.577958,8.513452,-5.113353,-9.146416,1.974523,-4.476654,-0.447576,7.514321,2.640837,5.758695,-1.457429,-6.744929,7.497108,8.823214,2.160534,6.468614,-1.120981,-7.417893,-8.731144,-8.469177,-9.448412,1.623888,1.527740,-5.353453,-0.939398,3.503639,1.376869,-9.466713,-1.420639,9.760554,4.339191,-6.331143,-9.311579,-5.413066,9.605612,-5.491489,-4.399617,3.926585,-6.989352,-2.681052,5.579265,9.093638,6.630360,6.762099,9.609883,1.098261,-0.621599,-9.571626,-4.096158,9.268258,-6.693121,-4.601123,-2.513014,-5.892454,7.268552,3.804095,-5.471252,-2.621026,-8.556460,-1.803508,-2.034970,-6.874213,9.128473,5.055363,-9.083541,6.849491,-6.047971,8.531952,1.160314,7.787440,-5.286271,8.281439,-9.163775,0.941695,-5.240344,-8.409560,6.643501,4.314365,-6.128014,2.475289,7.987434,3.773923,-1.331313,-9.413352,-7.113148,-6.450056,-8.096426,-7.748897,8.060041,-3.800853,1.118245,1.774458,0.128098,6.138474,4.798445,-4.903866,7.428591,0.303416,-8.790809,-9.750997,1.554246,-1.128682,-0.316902,-6.612603,-9.861496,8.297948,-3.802925,-1.974790,1.288554,5.865712,-3.123347,-2.227522,0.221931,1.826006,0.987091,-8.330214,2.463804,7.524262,0.569846,5.413862,-0.255306,9.516781,0.527102,-0.213871,7.964860,-3.295375,-7.233580,-6.997951,-2.589335,4.174962,4.943856,-8.175575,-4.686955,-6.727248,-3.813026,6.514658,7.927981,3.294433,3.883015,5.126345,9.767306,-3.341890,-5.815107,6.901324,6.275722,7.534277,-0.816062,2.036089,3.677565,8.669125,0.267170,-4.208243,1.502894,-3.536168,3.928142,-3.707723,8.329819,-2.635713,5.060203,-4.885362,6.547719,5.197670,9.820069,-9.056047,-8.934540,-7.460108,0.537810,-8.652645,-0.173784,9.734467,4.796809,-6.813749,-6.871496,-6.066999,-6.672889,-0.166245,-4.972989,-2.518090,-9.082349,-9.541471,-1.108772,8.264853,3.294185,-8.800080,-7.071917,-5.885645,7.503562,-6.335507,2.380254,2.859510,2.199890,1.134666,6.884279,9.131267,8.466525,4.561610,2.447796,4.571070,-8.456791,-6.004252,6.573393,-2.946479,-0.793159,-2.162543,-9.221805,9.735733,-0.278287,6.323808,-7.473959,2.931526,9.336163,1.970338,4.141085,3.296188,7.907986,-4.289378,-1.330857,6.646674,6.069229,3.433367,-4.737448,6.399524,3.962468,-4.175645,-4.179393,1.805688,-9.295782,-5.886300,5.475885,-0.484408,4.789334,6.914493,7.226192,-3.676714,8.252920,-2.292675,1.606159,-9.397336,0.190082,-2.253457,-4.216263,4.278424,6.792208,5.060789,0.449928,0.125412,-6.668008,8.393913,4.299264,9.264118,6.876865,-1.064074,8.372099,1.184335,-7.643746,-4.078717,-7.815257,6.496617,2.001467,-8.802230,-1.433939,-9.040335,6.519879,5.757395,5.724848,4.145583,-1.029767,9.763488,-8.884173,-7.147278,4.606625,6.134735,-2.909473,1.306286,1.782243,1.113405,4.832373,7.224751,2.382821,9.511312,7.422111,5.025951,9.132424,7.168317,5.139619,-8.135426,0.735769,-3.591381,-0.726321,3.512233,-3.490567,-2.300550,-1.760710,-0.496693,-2.587746,3.554450,-0.346985,8.828008,9.607666,8.746507,3.027030,6.232759,2.774488,-4.597618,9.716753,-1.580107,-0.390077,6.859452,-2.059596,-5.395051,-0.023620,-8.482772,-7.372328,-4.896672,-6.468206,4.023983,3.228280,-7.254384,-2.671069,-5.661025,5.864701,7.802005,7.770394,-6.389916,-4.192493,-2.593449,-9.796750,6.417913,3.465725,7.395078,4.588101,8.690853,5.488498,-5.198574,-7.823452,-9.934872,9.084078,-3.451167,-9.686614,-2.585934,4.022411,8.766257,7.670659,3.545862,-2.743722,-8.387894,2.653319,-4.511419,-1.369091,-6.718031,-7.301101,-1.517317,2.001796,-1.999716,1.746468,-5.005217,-2.648797,5.426457,3.671138,-4.543636,5.196821,1.993922,-9.213187,7.533083,-7.952177,7.669436,-4.447561,-7.913381,-3.753133,-4.363165,9.702525,7.988364,-7.463125,6.327316,0.053591,-2.722578,7.445576,6.091592,0.818901,-9.770176,-9.948891,-4.272931,3.959810,-4.606929,-2.316442,9.011502,-3.602267,2.286580,9.335435,-3.233046,-6.323384,9.093818,-6.242363,8.253836,-1.754093,-0.385213,1.264254,4.473019,9.666936,9.689347,-9.753662,-7.154227,6.886057,-9.975757,-4.995811,8.138662,8.341973,-5.082769,7.203035,3.605480,2.993573,-6.704460,4.401783,2.026709,-3.954174,-2.823379,-8.354015,4.314827,-8.629991,-1.551195,-8.317144,2.042893,0.823083,1.603032,6.558264,-6.159630,-6.982611,5.713796,-9.234677,5.816743,8.609505,-3.895891,-7.714524,6.542049,3.450249,2.303349,4.516962,7.461911,4.615565,4.726808,5.743743,2.748833,4.999609,6.691668,-0.859633,-0.469663,-8.808640,3.592344,-7.582592,1.255258,-8.080481,4.849712,7.416905,-6.561253,1.486969,7.969207,5.258252,0.683252,-3.316793,4.617280,6.783243,-3.401054,-2.802919,-6.650116,2.651822,-7.909759,-6.508485,8.632201,-4.435536,-2.335847,-2.375323,-9.966094,2.321613,-0.884946,0.732174,-4.832809,7.546250,-2.817668,-2.781541,-7.809212,7.403672,0.600257,-8.570789,3.538831,5.527534,-7.382788,-1.371231,3.624863,-8.932173,7.757788,4.822408,-6.729095,-1.976036,-0.122049,9.581990,-8.312919,5.120368,4.048702,1.337841,-8.235913,-7.996958,-0.927171,-2.355015,-6.041564,6.759110,-5.281464,0.907673,2.601513,8.532338,-2.753183,-7.755179,5.434477,4.783355,3.832961,-3.611157,3.818096,-2.570954,3.299925,5.321190,-7.932347,6.161519,-3.062571,3.189961,-2.973454,6.591173,-0.579675,-5.670437,-8.754862,-9.617157,-8.799564,2.642481,4.918543,4.461120,-2.139577,8.195335,0.137429,5.072030,6.429255,0.169644,-5.379838,7.451189,-4.751746,-3.821146,5.806353,-2.817357,8.920598,4.828263,2.688848,9.854208,8.466424,-2.216330,5.411053,-5.406325,4.051354,8.569939,6.980770,-7.709529,-5.994670,-0.675558,5.311826,9.103638,-5.134536,4.569853,6.082400,-3.950108,2.758884,8.050245,-7.058717,-8.427792,7.533784,1.742613,-5.423359,-9.724565,8.057185,-1.505962,5.518790,0.403040,-0.505617,9.047440,-0.902195,-2.315302,9.858343,-8.174240,-1.813344,4.394277,-7.311383,-4.096264,-4.149868,2.475689,3.882972,-2.353855,5.287679,-8.153727,-4.921643,8.315021,1.793923,6.137800,1.480555,7.001974,-7.378143,3.092736,0.110315,7.839778,-5.227430,3.119410,-5.532809,-9.835225,-9.662213,4.837971,6.416174,1.143993,-1.500345,3.871020,-3.556944,8.156316,5.048478,-5.297417,-7.191333,-5.570115,-6.345365,-8.032550,3.380818,3.811954,-6.926234,-1.984029,2.541442,-0.703613,-4.588780,-9.535816,-5.857550,4.900435,-1.067838,7.744956,2.586002,-4.070321,0.041562,-7.769118,4.680448,-2.144501,-7.851313,5.802567,-2.721626,-7.263921,5.301140,-6.387047,-6.783696,2.231569,7.450256,-0.661809,-4.877480,-1.301789,5.948997,-8.716658,-6.179410,-0.072861,-1.713766,3.039579,-1.990775,4.554954,-4.097037,2.398772,-1.019700,1.050066,4.259236,-4.831993,-2.820482,-4.795684,-3.409475,3.430234,1.590352,5.125050,3.170200,8.642192,-1.381795,-8.206853,-0.877238,-7.221100,-7.894760,-3.141168,8.901498,-2.706639,4.831128,1.398797,8.906972,7.205470,7.357757,-3.381290,8.863647,-8.642574,5.817534,-0.589536,-1.847115,-5.848562,-6.381400,9.500008,6.523232,-9.307518,-8.969873,-3.978626,-1.644314,-1.950426,3.356358,-5.566999,-6.188236,-2.824739,0.751948,5.036144,6.115458,7.081928,-6.044228,2.843963,-9.664785,9.547933,-0.294863,-3.069139,0.666145,-5.417036,-0.893388,6.940923,7.705761,-3.263629,-1.095376,-1.240873,0.353088,6.831308,-1.681046,9.944133,-7.215139,9.869011,7.427510,0.615968,1.981403,8.596213,5.109904,-1.738391,-7.149887,4.023718,4.346180,9.206313], dtype = "float64")#candidate|7815|(1080,)|const|float64
call_7814 = relay.TupleGetItem(func_1210_call(relay.reshape(const_7815.astype('float64'), [9, 12, 10]), relay.reshape(const_7815.astype('float64'), [9, 12, 10]), ), 3)
call_7816 = relay.TupleGetItem(func_1214_call(relay.reshape(const_7815.astype('float64'), [9, 12, 10]), relay.reshape(const_7815.astype('float64'), [9, 12, 10]), ), 3)
var_7822 = relay.var("var_7822", dtype = "float64", shape = (1080,))#candidate|7822|(1080,)|var|float64
bop_7823 = relay.floor_mod(const_7815.astype('float32'), relay.reshape(var_7822.astype('float32'), relay.shape_of(const_7815))) # shape=(1080,)
output = relay.Tuple([call_7812,call_7814,bop_7823,])
output2 = relay.Tuple([call_7813,call_7816,bop_7823,])
func_7833 = relay.Function([var_7822,], output)
mod['func_7833'] = func_7833
mod = relay.transform.InferType()(mod)
var_7834 = relay.var("var_7834", dtype = "float64", shape = (1080,))#candidate|7834|(1080,)|var|float64
output = func_7833(var_7834)
func_7835 = relay.Function([var_7834], output)
mutated_mod['func_7835'] = func_7835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7370_call = mod.get_global_var('func_7370')
func_7372_call = mutated_mod.get_global_var('func_7372')
call_7839 = relay.TupleGetItem(func_7370_call(), 2)
call_7840 = relay.TupleGetItem(func_7372_call(), 2)
output = relay.Tuple([call_7839,])
output2 = relay.Tuple([call_7840,])
func_7858 = relay.Function([], output)
mod['func_7858'] = func_7858
mod = relay.transform.InferType()(mod)
output = func_7858()
func_7859 = relay.Function([], output)
mutated_mod['func_7859'] = func_7859
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7868 = relay.var("var_7868", dtype = "float32", shape = (16, 10, 13))#candidate|7868|(16, 10, 13)|var|float32
uop_7869 = relay.sqrt(var_7868.astype('float32')) # shape=(16, 10, 13)
output = relay.Tuple([uop_7869,])
output2 = relay.Tuple([uop_7869,])
func_7877 = relay.Function([var_7868,], output)
mod['func_7877'] = func_7877
mod = relay.transform.InferType()(mod)
mutated_mod['func_7877'] = func_7877
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7878 = relay.var("var_7878", dtype = "float32", shape = (16, 10, 13))#candidate|7878|(16, 10, 13)|var|float32
func_7877_call = mutated_mod.get_global_var('func_7877')
call_7879 = func_7877_call(var_7878)
output = call_7879
func_7880 = relay.Function([var_7878], output)
mutated_mod['func_7880'] = func_7880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6630_call = mod.get_global_var('func_6630')
func_6631_call = mutated_mod.get_global_var('func_6631')
call_7926 = func_6630_call()
call_7927 = func_6630_call()
output = call_7926
output2 = call_7927
func_7947 = relay.Function([], output)
mod['func_7947'] = func_7947
mod = relay.transform.InferType()(mod)
mutated_mod['func_7947'] = func_7947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7947_call = mutated_mod.get_global_var('func_7947')
call_7948 = func_7947_call()
output = call_7948
func_7949 = relay.Function([], output)
mutated_mod['func_7949'] = func_7949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1774_call = mod.get_global_var('func_1774')
func_1776_call = mutated_mod.get_global_var('func_1776')
call_7966 = func_1774_call()
call_7967 = func_1774_call()
func_2632_call = mod.get_global_var('func_2632')
func_2635_call = mutated_mod.get_global_var('func_2635')
var_7971 = relay.var("var_7971", dtype = "uint64", shape = (231, 1))#candidate|7971|(231, 1)|var|uint64
call_7970 = relay.TupleGetItem(func_2632_call(relay.reshape(var_7971.astype('uint64'), [11, 3, 7])), 0)
call_7972 = relay.TupleGetItem(func_2635_call(relay.reshape(var_7971.astype('uint64'), [11, 3, 7])), 0)
func_1763_call = mod.get_global_var('func_1763')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_7974 = func_1763_call()
call_7975 = func_1763_call()
func_2916_call = mod.get_global_var('func_2916')
func_2919_call = mutated_mod.get_global_var('func_2919')
var_7988 = relay.var("var_7988", dtype = "int64", shape = ())#candidate|7988|()|var|int64
var_7989 = relay.var("var_7989", dtype = "int64", shape = (1800,))#candidate|7989|(1800,)|var|int64
call_7987 = relay.TupleGetItem(func_2916_call(relay.reshape(var_7988.astype('int64'), []), relay.reshape(var_7989.astype('int64'), [15, 8, 15]), ), 0)
call_7990 = relay.TupleGetItem(func_2919_call(relay.reshape(var_7988.astype('int64'), []), relay.reshape(var_7989.astype('int64'), [15, 8, 15]), ), 0)
func_272_call = mod.get_global_var('func_272')
func_274_call = mutated_mod.get_global_var('func_274')
call_7991 = relay.TupleGetItem(func_272_call(), 0)
call_7992 = relay.TupleGetItem(func_274_call(), 0)
output = relay.Tuple([call_7966,call_7970,var_7971,call_7974,call_7987,var_7988,var_7989,call_7991,])
output2 = relay.Tuple([call_7967,call_7972,var_7971,call_7975,call_7990,var_7988,var_7989,call_7992,])
func_7995 = relay.Function([var_7971,var_7988,var_7989,], output)
mod['func_7995'] = func_7995
mod = relay.transform.InferType()(mod)
var_7996 = relay.var("var_7996", dtype = "uint64", shape = (231, 1))#candidate|7996|(231, 1)|var|uint64
var_7997 = relay.var("var_7997", dtype = "int64", shape = ())#candidate|7997|()|var|int64
var_7998 = relay.var("var_7998", dtype = "int64", shape = (1800,))#candidate|7998|(1800,)|var|int64
output = func_7995(var_7996,var_7997,var_7998,)
func_7999 = relay.Function([var_7996,var_7997,var_7998,], output)
mutated_mod['func_7999'] = func_7999
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8037 = relay.var("var_8037", dtype = "int16", shape = (15, 2, 6))#candidate|8037|(15, 2, 6)|var|int16
var_8038 = relay.var("var_8038", dtype = "int16", shape = (15, 2, 6))#candidate|8038|(15, 2, 6)|var|int16
bop_8039 = relay.minimum(var_8037.astype('int16'), relay.reshape(var_8038.astype('int16'), relay.shape_of(var_8037))) # shape=(15, 2, 6)
output = relay.Tuple([bop_8039,])
output2 = relay.Tuple([bop_8039,])
func_8050 = relay.Function([var_8037,var_8038,], output)
mod['func_8050'] = func_8050
mod = relay.transform.InferType()(mod)
var_8051 = relay.var("var_8051", dtype = "int16", shape = (15, 2, 6))#candidate|8051|(15, 2, 6)|var|int16
var_8052 = relay.var("var_8052", dtype = "int16", shape = (15, 2, 6))#candidate|8052|(15, 2, 6)|var|int16
output = func_8050(var_8051,var_8052,)
func_8053 = relay.Function([var_8051,var_8052,], output)
mutated_mod['func_8053'] = func_8053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5003_call = mod.get_global_var('func_5003')
func_5005_call = mutated_mod.get_global_var('func_5005')
call_8064 = relay.TupleGetItem(func_5003_call(), 1)
call_8065 = relay.TupleGetItem(func_5005_call(), 1)
func_603_call = mod.get_global_var('func_603')
func_605_call = mutated_mod.get_global_var('func_605')
call_8089 = relay.TupleGetItem(func_603_call(), 0)
call_8090 = relay.TupleGetItem(func_605_call(), 0)
output = relay.Tuple([call_8064,call_8089,])
output2 = relay.Tuple([call_8065,call_8090,])
func_8120 = relay.Function([], output)
mod['func_8120'] = func_8120
mod = relay.transform.InferType()(mod)
output = func_8120()
func_8121 = relay.Function([], output)
mutated_mod['func_8121'] = func_8121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_41_call = mutated_mod.get_global_var('func_41')
call_8129 = func_39_call()
call_8130 = func_39_call()
output = call_8129
output2 = call_8130
func_8147 = relay.Function([], output)
mod['func_8147'] = func_8147
mod = relay.transform.InferType()(mod)
output = func_8147()
func_8148 = relay.Function([], output)
mutated_mod['func_8148'] = func_8148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7019_call = mod.get_global_var('func_7019')
func_7021_call = mutated_mod.get_global_var('func_7021')
call_8149 = relay.TupleGetItem(func_7019_call(), 1)
call_8150 = relay.TupleGetItem(func_7021_call(), 1)
func_7858_call = mod.get_global_var('func_7858')
func_7859_call = mutated_mod.get_global_var('func_7859')
call_8153 = relay.TupleGetItem(func_7858_call(), 0)
call_8154 = relay.TupleGetItem(func_7859_call(), 0)
func_3601_call = mod.get_global_var('func_3601')
func_3603_call = mutated_mod.get_global_var('func_3603')
var_8173 = relay.var("var_8173", dtype = "float32", shape = (13, 35))#candidate|8173|(13, 35)|var|float32
call_8172 = func_3601_call(relay.reshape(var_8173.astype('float32'), [5, 13, 7]))
call_8174 = func_3601_call(relay.reshape(var_8173.astype('float32'), [5, 13, 7]))
func_5569_call = mod.get_global_var('func_5569')
func_5572_call = mutated_mod.get_global_var('func_5572')
var_8176 = relay.var("var_8176", dtype = "float32", shape = (180,))#candidate|8176|(180,)|var|float32
call_8175 = relay.TupleGetItem(func_5569_call(relay.reshape(var_8176.astype('float32'), [15, 3, 4])), 0)
call_8177 = relay.TupleGetItem(func_5572_call(relay.reshape(var_8176.astype('float32'), [15, 3, 4])), 0)
var_8181 = relay.var("var_8181", dtype = "float64", shape = (1080,))#candidate|8181|(1080,)|var|float64
bop_8182 = relay.floor_divide(call_8153.astype('float64'), relay.reshape(var_8181.astype('float64'), relay.shape_of(call_8153))) # shape=(1080,)
bop_8185 = relay.floor_divide(call_8154.astype('float64'), relay.reshape(var_8181.astype('float64'), relay.shape_of(call_8154))) # shape=(1080,)
output = relay.Tuple([call_8149,call_8172,var_8173,call_8175,var_8176,bop_8182,])
output2 = relay.Tuple([call_8150,call_8174,var_8173,call_8177,var_8176,bop_8185,])
F = relay.Function([var_8173,var_8176,var_8181,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8173,var_8176,var_8181,], output2)
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
