import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_40 = relay.var("var_40", dtype = "int16", shape = (12, 8, 2))#candidate|40|(12, 8, 2)|var|int16
const_41 = relay.const([[[-4,3],[-3,2],[-3,-7],[-2,-5],[9,-9],[-8,3],[10,10],[10,4]],[[-2,8],[9,1],[7,-4],[-3,3],[-4,8],[5,1],[5,-5],[-3,-8]],[[5,-10],[-6,-8],[-1,1],[5,5],[8,3],[-7,1],[8,-4],[7,7]],[[10,8],[-8,-10],[-1,4],[6,-5],[-1,8],[-3,-9],[-6,-3],[6,7]],[[-7,5],[-1,6],[-9,8],[-8,-10],[1,8],[-8,8],[-9,-9],[9,5]],[[10,1],[9,3],[-8,3],[-4,-4],[10,3],[-8,-2],[-2,-3],[6,8]],[[10,-7],[-9,-6],[1,-10],[10,-4],[-7,-6],[7,-1],[10,1],[4,2]],[[-9,2],[9,-4],[5,7],[-9,4],[7,-8],[-2,5],[-4,8],[6,-9]],[[-10,4],[9,10],[-1,7],[-6,-5],[-5,-7],[-3,-6],[9,-5],[5,9]],[[-7,5],[-10,-7],[-1,-2],[-7,10],[-1,6],[-1,2],[-10,4],[-3,1]],[[5,-3],[2,-5],[-6,8],[3,5],[6,7],[6,5],[8,-1],[2,8]],[[-9,-2],[3,-2],[4,10],[7,-1],[-7,-10],[10,8],[7,-9],[-1,-8]]], dtype = "int16")#candidate|41|(12, 8, 2)|const|int16
bop_42 = relay.equal(var_40.astype('bool'), relay.reshape(const_41.astype('bool'), relay.shape_of(var_40))) # shape=(12, 8, 2)
uop_49 = relay.atanh(const_41.astype('float64')) # shape=(12, 8, 2)
bop_61 = relay.right_shift(const_41.astype('int16'), relay.reshape(var_40.astype('int16'), relay.shape_of(const_41))) # shape=(12, 8, 2)
output = relay.Tuple([bop_42,uop_49,bop_61,])
output2 = relay.Tuple([bop_42,uop_49,bop_61,])
func_64 = relay.Function([var_40,], output)
mod['func_64'] = func_64
mod = relay.transform.InferType()(mod)
var_65 = relay.var("var_65", dtype = "int16", shape = (12, 8, 2))#candidate|65|(12, 8, 2)|var|int16
output = func_64(var_65)
func_66 = relay.Function([var_65], output)
mutated_mod['func_66'] = func_66
mutated_mod = relay.transform.InferType()(mutated_mod)
var_245 = relay.var("var_245", dtype = "float32", shape = (2, 15, 10))#candidate|245|(2, 15, 10)|var|float32
uop_246 = relay.sin(var_245.astype('float32')) # shape=(2, 15, 10)
output = uop_246
output2 = uop_246
func_250 = relay.Function([var_245,], output)
mod['func_250'] = func_250
mod = relay.transform.InferType()(mod)
mutated_mod['func_250'] = func_250
mutated_mod = relay.transform.InferType()(mutated_mod)
var_251 = relay.var("var_251", dtype = "float32", shape = (2, 15, 10))#candidate|251|(2, 15, 10)|var|float32
func_250_call = mutated_mod.get_global_var('func_250')
call_252 = func_250_call(var_251)
output = call_252
func_253 = relay.Function([var_251], output)
mutated_mod['func_253'] = func_253
mutated_mod = relay.transform.InferType()(mutated_mod)
var_336 = relay.var("var_336", dtype = "bool", shape = (3, 9, 8))#candidate|336|(3, 9, 8)|var|bool
var_337 = relay.var("var_337", dtype = "bool", shape = (3, 9, 8))#candidate|337|(3, 9, 8)|var|bool
bop_338 = relay.logical_and(var_336.astype('bool'), relay.reshape(var_337.astype('bool'), relay.shape_of(var_336))) # shape=(3, 9, 8)
bop_350 = relay.right_shift(bop_338.astype('int16'), relay.reshape(var_336.astype('int16'), relay.shape_of(bop_338))) # shape=(3, 9, 8)
func_250_call = mod.get_global_var('func_250')
func_253_call = mutated_mod.get_global_var('func_253')
const_354 = relay.const([0.242437,-0.999602,3.009710,4.802270,-4.810875,1.522307,8.946586,4.455968,-8.713471,3.957537,-0.140097,-2.602293,8.388822,3.580025,-4.541106,-1.464960,-9.874224,-4.937111,9.483418,3.838463,7.171162,-9.111404,-8.770446,0.573154,6.718774,-9.370859,1.973863,-4.323772,8.844324,9.128760,-0.022238,2.797239,-9.198659,-6.869326,6.387591,3.852280,4.034364,1.745661,8.586452,-0.184426,0.837185,-6.009710,7.377720,8.696491,-9.932901,-5.377648,3.888757,5.335408,7.291067,6.123136,-2.422440,8.757214,-1.773201,2.503097,-7.867174,4.863628,-0.971611,-9.407713,-6.142312,-5.346000,-5.000165,-2.522091,-9.797829,7.521133,2.147895,-9.842884,2.869900,5.677220,-7.893723,4.372129,-5.554415,0.240364,-4.398645,-0.497612,0.274687,-8.723670,-1.438161,5.507718,-5.707400,-7.546323,-9.408418,2.499362,2.191125,5.859174,3.157069,-4.562942,7.542050,-8.803473,1.176656,3.927993,0.827844,-5.099750,-4.638551,-8.105731,-5.696178,-7.897901,4.212075,-3.936221,8.345178,9.242775,-3.940989,-2.510473,8.970394,2.897181,-4.973115,4.639519,-7.449764,6.761589,-8.053795,-9.536951,-1.189361,9.390308,-5.007335,-5.474685,4.548187,4.168370,9.851506,-4.529920,-2.974714,7.192380,-7.324657,6.410244,-8.306465,4.358779,-3.346872,9.817941,-7.935762,7.009453,-1.291590,-2.157701,5.000848,7.476199,-8.228414,2.531599,-7.101894,2.826768,3.390935,6.924889,3.802963,-8.057035,-4.492798,-6.776290,-4.920645,-0.402940,-8.745318,7.845107,-7.685389,-6.121444,-9.905016,2.873405,1.850212,5.305188,9.947963,-1.482809,9.065458,6.384566,3.363820,-6.121592,3.866627,-1.408658,-9.019719,0.028703,3.785188,4.832622,1.453581,-7.412690,5.615640,3.871910,-7.435677,3.407772,2.458512,-0.893293,-2.470805,-6.443413,5.102694,4.473214,-5.858156,-8.078683,3.863666,2.469008,-2.588704,9.156535,0.992993,7.021942,-4.652426,3.237397,9.352932,-5.272774,0.175124,0.911045,-2.091348,-5.440972,8.347872,-2.311514,-2.361744,2.422122,1.117762,-7.170076,6.510083,-4.743418,-4.915796,9.747145,2.243913,2.300228,0.111978,1.295021,-8.431256,-3.681997,-3.787837,-9.910472,8.456005,-7.505394,-3.131691,4.256432,-4.570937,8.981250,-7.080508,-3.934969,5.009348,-9.060673,-2.537963,-3.744355,4.830666,-0.929191,3.317711,-0.887785,-1.213463,8.396384,5.942379,-1.589577,-9.030976,-5.021299,9.088890,0.840030,-1.846689,5.735274,4.989431,7.304231,-9.265873,8.454760,-7.404802,-6.162413,-9.583669,6.720875,4.766781,2.594449,-2.531369,-5.504484,-2.148198,-0.678854,6.922828,7.885250,4.478484,2.596095,-0.579346,9.349308,-4.686604,0.277302,3.857576,-5.048897,-1.166483,-8.327985,5.315333,-7.629901,-4.386046,-7.582886,-2.330634,6.556050,0.321477,-4.391526,8.890944,-1.160080,7.301272,-2.668619,4.026604,8.599741,-5.302324,-9.948017,-6.279980,8.540146,3.502484,-6.536493,6.859944,1.712188,-9.551226,-8.595547,3.850191,0.150957,-0.986438,6.181039,-9.277456,7.018346,-1.660670,-8.911126,3.383099,-0.428897,-8.033947,-8.900525,-0.680823,-6.042879], dtype = "float32")#candidate|354|(300,)|const|float32
call_353 = func_250_call(relay.reshape(const_354.astype('float32'), [2, 15, 10]))
call_355 = func_250_call(relay.reshape(const_354.astype('float32'), [2, 15, 10]))
uop_368 = relay.asin(call_353.astype('float64')) # shape=(2, 15, 10)
uop_370 = relay.asin(call_355.astype('float64')) # shape=(2, 15, 10)
output = relay.Tuple([bop_350,const_354,uop_368,])
output2 = relay.Tuple([bop_350,const_354,uop_370,])
func_373 = relay.Function([var_336,var_337,], output)
mod['func_373'] = func_373
mod = relay.transform.InferType()(mod)
mutated_mod['func_373'] = func_373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_373_call = mutated_mod.get_global_var('func_373')
var_375 = relay.var("var_375", dtype = "bool", shape = (3, 9, 8))#candidate|375|(3, 9, 8)|var|bool
var_376 = relay.var("var_376", dtype = "bool", shape = (3, 9, 8))#candidate|376|(3, 9, 8)|var|bool
call_374 = func_373_call(var_375,var_376,)
output = call_374
func_377 = relay.Function([var_375,var_376,], output)
mutated_mod['func_377'] = func_377
mutated_mod = relay.transform.InferType()(mutated_mod)
var_745 = relay.var("var_745", dtype = "int32", shape = (1, 5, 9))#candidate|745|(1, 5, 9)|var|int32
var_746 = relay.var("var_746", dtype = "int32", shape = (4, 5, 9))#candidate|746|(4, 5, 9)|var|int32
bop_747 = relay.greater(var_745.astype('bool'), var_746.astype('bool')) # shape=(4, 5, 9)
output = relay.Tuple([bop_747,])
output2 = relay.Tuple([bop_747,])
func_767 = relay.Function([var_745,var_746,], output)
mod['func_767'] = func_767
mod = relay.transform.InferType()(mod)
mutated_mod['func_767'] = func_767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_767_call = mutated_mod.get_global_var('func_767')
var_769 = relay.var("var_769", dtype = "int32", shape = (1, 5, 9))#candidate|769|(1, 5, 9)|var|int32
var_770 = relay.var("var_770", dtype = "int32", shape = (4, 5, 9))#candidate|770|(4, 5, 9)|var|int32
call_768 = func_767_call(var_769,var_770,)
output = call_768
func_771 = relay.Function([var_769,var_770,], output)
mutated_mod['func_771'] = func_771
mutated_mod = relay.transform.InferType()(mutated_mod)
const_852 = relay.const([[[-7.772451],[-8.653405],[-3.976083],[5.712324]],[[-3.674187],[4.828296],[-9.936066],[-2.119520]],[[-4.866169],[1.160468],[1.640789],[6.295771]],[[-1.831364],[-9.179198],[-6.835229],[2.252621]],[[0.829978],[-2.407912],[0.652126],[-7.247109]]], dtype = "float64")#candidate|852|(5, 4, 1)|const|float64
uop_853 = relay.log(const_852.astype('float64')) # shape=(5, 4, 1)
uop_881 = relay.tan(uop_853.astype('float32')) # shape=(5, 4, 1)
bop_887 = relay.equal(uop_881.astype('bool'), relay.reshape(uop_853.astype('bool'), relay.shape_of(uop_881))) # shape=(5, 4, 1)
uop_891 = relay.cos(bop_887.astype('float64')) # shape=(5, 4, 1)
uop_895 = relay.cosh(const_852.astype('float32')) # shape=(5, 4, 1)
uop_902 = relay.asin(uop_891.astype('float64')) # shape=(5, 4, 1)
func_767_call = mod.get_global_var('func_767')
func_771_call = mutated_mod.get_global_var('func_771')
var_917 = relay.var("var_917", dtype = "int32", shape = (45,))#candidate|917|(45,)|var|int32
const_918 = relay.const([[-2,-6,-2,2,9,-1,6,6,-3,7,-7,-1,-1,-7,-2,2,-1,-4,-7,3,2,4,3,9,-8,-3,1,-7,4,7],[10,-1,10,-4,-4,2,10,-5,9,-8,-2,4,-6,-6,-7,-4,4,8,3,-10,8,6,-9,8,6,-7,-8,2,9,2],[-2,-3,-4,-8,-4,5,-4,7,-1,-3,2,5,-8,1,6,-5,2,3,-10,4,-3,5,1,1,8,8,2,7,-2,-9],[-4,9,4,-5,-6,8,9,5,9,3,-9,-7,-6,-3,5,-1,8,-8,-1,-7,-3,6,-10,3,8,7,6,-10,-8,-3],[7,-5,-1,7,5,10,-9,-1,9,10,-9,5,-3,-8,-8,-6,-2,-9,-4,-8,10,-9,6,10,4,-5,9,10,6,2],[8,8,9,-6,6,5,4,5,-6,7,4,-4,-3,2,-2,-3,4,-2,-1,-7,-2,2,-8,6,-1,5,7,10,-6,7]], dtype = "int32")#candidate|918|(6, 30)|const|int32
call_916 = relay.TupleGetItem(func_767_call(relay.reshape(var_917.astype('int32'), [1, 5, 9]), relay.reshape(const_918.astype('int32'), [4, 5, 9]), ), 0)
call_919 = relay.TupleGetItem(func_771_call(relay.reshape(var_917.astype('int32'), [1, 5, 9]), relay.reshape(const_918.astype('int32'), [4, 5, 9]), ), 0)
output = relay.Tuple([uop_895,uop_902,call_916,var_917,const_918,])
output2 = relay.Tuple([uop_895,uop_902,call_919,var_917,const_918,])
func_935 = relay.Function([var_917,], output)
mod['func_935'] = func_935
mod = relay.transform.InferType()(mod)
mutated_mod['func_935'] = func_935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_936 = relay.var("var_936", dtype = "int32", shape = (45,))#candidate|936|(45,)|var|int32
func_935_call = mutated_mod.get_global_var('func_935')
call_937 = func_935_call(var_936)
output = call_937
func_938 = relay.Function([var_936], output)
mutated_mod['func_938'] = func_938
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1210 = relay.var("var_1210", dtype = "int16", shape = (9, 7, 4))#candidate|1210|(9, 7, 4)|var|int16
var_1211 = relay.var("var_1211", dtype = "int16", shape = (9, 7, 4))#candidate|1211|(9, 7, 4)|var|int16
bop_1212 = relay.subtract(var_1210.astype('int16'), relay.reshape(var_1211.astype('int16'), relay.shape_of(var_1210))) # shape=(9, 7, 4)
func_373_call = mod.get_global_var('func_373')
func_377_call = mutated_mod.get_global_var('func_377')
const_1221 = relay.const([[True,False,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True],[True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,True]], dtype = "bool")#candidate|1221|(2, 108)|const|bool
call_1220 = relay.TupleGetItem(func_373_call(relay.reshape(const_1221.astype('bool'), [3, 9, 8]), relay.reshape(const_1221.astype('bool'), [3, 9, 8]), ), 0)
call_1222 = relay.TupleGetItem(func_377_call(relay.reshape(const_1221.astype('bool'), [3, 9, 8]), relay.reshape(const_1221.astype('bool'), [3, 9, 8]), ), 0)
func_250_call = mod.get_global_var('func_250')
func_253_call = mutated_mod.get_global_var('func_253')
const_1231 = relay.const([6.130959,8.799139,-7.063715,5.580848,4.826792,9.354510,-9.767041,7.396740,-3.968271,2.104613,-1.607992,8.757458,4.033807,-4.421863,2.619138,5.489203,1.090507,-3.566896,-9.411703,5.456964,-7.814354,2.631695,8.858072,-1.740914,6.742123,6.834870,3.628488,-2.999171,-8.174782,1.727426,7.098705,2.098669,-0.363956,-1.435291,4.043486,-9.729461,-7.678596,-2.555669,-3.562057,-3.847485,-8.584979,-5.356858,-2.042444,-9.953565,7.275829,-6.984701,-6.682905,0.828377,3.640545,3.474283,9.995285,-7.762859,0.846699,2.781207,7.659098,-2.638028,1.026274,8.544907,0.158114,2.620603,-9.025580,4.227486,6.790766,0.995593,-3.795661,2.799566,-4.096314,-8.618583,-0.135539,-1.471807,0.846463,4.736027,3.463669,-3.405862,-8.396731,1.051031,-4.002730,0.619895,8.834051,-7.018590,4.791982,3.751829,-5.475161,4.122737,-7.446766,-0.897901,-3.540835,-0.075235,8.532422,5.294249,-3.030809,-5.836162,0.415368,-0.007248,-5.352484,8.056458,-5.616468,6.115358,-5.520049,8.963621,-0.526284,-8.008570,8.094741,-9.239087,1.195891,-9.943422,-5.474092,-1.151117,-0.483423,-8.644784,-9.020091,-1.778730,3.109559,9.366364,5.440113,-9.189886,-8.963529,-7.884277,8.387992,-3.025087,-1.828223,8.103788,7.131462,9.094627,-8.377986,-8.342909,0.640209,-7.931847,8.897389,-7.235878,-1.173666,-9.464832,2.514569,4.436236,-5.869633,4.840862,-0.632764,1.574678,3.507363,-7.656725,4.154152,-9.893182,8.682280,9.425528,-7.822024,2.599246,-1.894618,3.757551,1.339908,-6.347319,8.588450,-2.438528,-8.219218,5.772054,-5.779039,-0.653941,9.367640,-7.800529,0.343559,4.288231,5.382933,-5.941528,-0.943900,7.390371,-7.909305,8.093902,-0.936966,-2.038881,-1.986231,-6.741430,4.849153,-0.735209,5.097637,6.103248,-0.569515,-7.363402,-9.298640,2.704633,-5.148124,-5.258025,-6.028613,-5.922524,3.731553,-3.115088,9.482684,1.207356,4.717904,1.824328,-7.364613,9.266487,6.015601,5.054076,-5.693473,-5.040840,0.111072,-2.716838,8.898277,-8.075123,0.253524,-9.709335,8.866197,7.099857,7.761683,1.504610,7.895701,-7.094103,-7.102161,-6.279261,-4.243037,-4.078294,2.136599,7.289051,4.865228,-7.612245,-2.715847,7.084402,-7.120617,-4.203458,2.899561,6.054094,-8.146708,1.678347,4.549707,-9.674819,4.762205,-1.303293,4.761286,6.170666,3.697796,2.741079,-3.320110,-3.666324,0.585331,-1.159092,-5.226010,6.362925,8.104709,-9.269540,2.216784,-3.170630,7.467460,8.328377,-9.546730,0.974944,-7.641284,-4.543574,-3.080271,6.923892,5.148220,-9.635332,-8.643066,6.334556,5.949294,-1.783225,-9.284686,2.471835,1.759685,-3.197980,9.168069,-6.640810,-5.269082,-8.888288,7.760228,-5.670394,6.702290,-3.407860,-2.288625,4.233179,6.184939,-6.741291,-9.270480,1.916930,3.622721,6.929618,-6.447435,-0.307049,-8.621930,3.353589,1.099573,3.852613,-7.427360,-8.273497,8.136918,-4.960444,5.815617,-3.807183,-6.902584,-6.313095,5.730218,-3.347633,7.648253,-2.966423,4.269985,0.448840,9.603279,0.939020,-9.373434,-2.818101,8.650267,8.733966], dtype = "float32")#candidate|1231|(300,)|const|float32
call_1230 = func_250_call(relay.reshape(const_1231.astype('float32'), [2, 15, 10]))
call_1232 = func_250_call(relay.reshape(const_1231.astype('float32'), [2, 15, 10]))
output = relay.Tuple([bop_1212,call_1220,const_1221,call_1230,const_1231,])
output2 = relay.Tuple([bop_1212,call_1222,const_1221,call_1232,const_1231,])
func_1233 = relay.Function([var_1210,var_1211,], output)
mod['func_1233'] = func_1233
mod = relay.transform.InferType()(mod)
var_1234 = relay.var("var_1234", dtype = "int16", shape = (9, 7, 4))#candidate|1234|(9, 7, 4)|var|int16
var_1235 = relay.var("var_1235", dtype = "int16", shape = (9, 7, 4))#candidate|1235|(9, 7, 4)|var|int16
output = func_1233(var_1234,var_1235,)
func_1236 = relay.Function([var_1234,var_1235,], output)
mutated_mod['func_1236'] = func_1236
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1264 = relay.var("var_1264", dtype = "float32", shape = (15, 12))#candidate|1264|(15, 12)|var|float32
uop_1265 = relay.log10(var_1264.astype('float32')) # shape=(15, 12)
output = uop_1265
output2 = uop_1265
func_1271 = relay.Function([var_1264,], output)
mod['func_1271'] = func_1271
mod = relay.transform.InferType()(mod)
mutated_mod['func_1271'] = func_1271
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1272 = relay.var("var_1272", dtype = "float32", shape = (15, 12))#candidate|1272|(15, 12)|var|float32
func_1271_call = mutated_mod.get_global_var('func_1271')
call_1273 = func_1271_call(var_1272)
output = call_1273
func_1274 = relay.Function([var_1272], output)
mutated_mod['func_1274'] = func_1274
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1555 = relay.var("var_1555", dtype = "float64", shape = (8, 15, 6))#candidate|1555|(8, 15, 6)|var|float64
uop_1556 = relay.acos(var_1555.astype('float64')) # shape=(8, 15, 6)
uop_1577 = relay.atan(var_1555.astype('float64')) # shape=(8, 15, 6)
output = relay.Tuple([uop_1556,uop_1577,])
output2 = relay.Tuple([uop_1556,uop_1577,])
func_1587 = relay.Function([var_1555,], output)
mod['func_1587'] = func_1587
mod = relay.transform.InferType()(mod)
mutated_mod['func_1587'] = func_1587
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1588 = relay.var("var_1588", dtype = "float64", shape = (8, 15, 6))#candidate|1588|(8, 15, 6)|var|float64
func_1587_call = mutated_mod.get_global_var('func_1587')
call_1589 = func_1587_call(var_1588)
output = call_1589
func_1590 = relay.Function([var_1588], output)
mutated_mod['func_1590'] = func_1590
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1617 = relay.var("var_1617", dtype = "float64", shape = (9, 5, 2))#candidate|1617|(9, 5, 2)|var|float64
var_1618 = relay.var("var_1618", dtype = "float64", shape = (9, 5, 2))#candidate|1618|(9, 5, 2)|var|float64
bop_1619 = relay.less(var_1617.astype('bool'), relay.reshape(var_1618.astype('bool'), relay.shape_of(var_1617))) # shape=(9, 5, 2)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
const_1628 = relay.const([[-5,7,-5,-6],[4,1,3,10],[8,-1,8,6],[9,-9,-9,-7],[-9,2,-3,4],[6,9,-3,-1],[-6,-7,-6,6],[-8,-10,-6,-1],[1,-3,-6,2],[-4,-1,-9,-9],[7,-9,-10,10],[2,5,7,6],[-1,-4,6,9],[6,-9,4,-10],[-4,6,6,4],[-6,-7,-6,2],[-2,6,-2,-7],[7,-3,-4,2],[4,5,-3,-9],[7,5,10,3],[-4,1,-4,-4],[6,1,-10,9],[-2,5,3,-8],[1,6,-1,-5],[-9,-2,-7,-5],[-4,3,3,10],[-6,3,-9,10],[4,-5,-6,-1],[9,10,-10,8],[-3,-9,-5,-2],[-4,-10,5,4],[7,-4,10,-2],[9,-4,8,2],[-5,8,8,10],[-6,-4,2,2],[-7,-4,2,-5],[-9,9,-3,9],[-9,-9,-10,10],[1,6,-2,-3],[-5,-8,-5,7],[4,-1,6,-8],[-8,4,7,-3],[8,2,-6,-8],[5,9,9,-4],[-1,-1,-7,-3],[-5,3,9,-8],[5,-6,6,3],[2,-1,-7,5]], dtype = "int16")#candidate|1628|(48, 4)|const|int16
call_1627 = relay.TupleGetItem(func_64_call(relay.reshape(const_1628.astype('int16'), [12, 8, 2])), 0)
call_1629 = relay.TupleGetItem(func_66_call(relay.reshape(const_1628.astype('int16'), [12, 8, 2])), 0)
func_373_call = mod.get_global_var('func_373')
func_377_call = mutated_mod.get_global_var('func_377')
var_1631 = relay.var("var_1631", dtype = "bool", shape = (216,))#candidate|1631|(216,)|var|bool
call_1630 = relay.TupleGetItem(func_373_call(relay.reshape(var_1631.astype('bool'), [3, 9, 8]), relay.reshape(var_1631.astype('bool'), [3, 9, 8]), ), 0)
call_1632 = relay.TupleGetItem(func_377_call(relay.reshape(var_1631.astype('bool'), [3, 9, 8]), relay.reshape(var_1631.astype('bool'), [3, 9, 8]), ), 0)
bop_1636 = relay.bitwise_xor(const_1628.astype('uint64'), relay.reshape(call_1627.astype('uint64'), relay.shape_of(const_1628))) # shape=(48, 4)
bop_1639 = relay.bitwise_xor(const_1628.astype('uint64'), relay.reshape(call_1629.astype('uint64'), relay.shape_of(const_1628))) # shape=(48, 4)
func_1587_call = mod.get_global_var('func_1587')
func_1590_call = mutated_mod.get_global_var('func_1590')
const_1645 = relay.const([-6.861356,3.058505,-7.954085,7.477457,8.894475,9.642312,3.298788,5.153316,-9.361654,-8.633160,-7.409088,-1.207249,-4.584040,-8.687415,-0.988780,-4.027303,-3.518387,-3.784682,6.104565,-5.153580,-2.605068,1.361277,-8.334626,1.312840,8.327520,1.218688,2.775042,-0.289280,2.751414,9.718358,5.521464,3.570403,-3.687465,-2.680438,2.941540,-0.174529,7.437697,-2.200818,7.940602,-0.749804,0.003281,-2.929215,4.744071,-4.394007,-1.771531,9.894998,9.438341,7.076763,-1.040180,7.769387,-1.267486,0.392816,-9.748414,-9.923207,4.664833,-3.603871,-1.611230,5.103495,4.334215,9.655701,-2.637701,5.333656,9.353786,0.414915,-9.259631,9.872859,-1.023550,-5.135566,-8.028891,-9.859532,6.647325,1.827800,-0.373083,-6.679784,-2.349632,6.307290,-6.995737,4.173838,0.254686,0.263364,3.514778,-7.078435,3.975352,-8.083998,0.410076,0.079239,5.721027,9.718187,-3.400571,0.870494,4.554146,0.972256,4.560683,3.437813,4.612314,8.112587,2.694223,-6.952059,-4.354300,9.272655,-9.050726,3.581033,4.379576,7.083791,-9.495969,-5.710970,6.366436,2.316405,-1.961054,2.392745,5.755489,1.436098,-4.596642,4.339604,-8.483487,7.168131,0.248574,3.816775,6.591289,-6.066554,8.251021,8.390137,-8.177974,-1.509634,6.866127,-2.458423,-9.203081,5.137752,-5.160869,0.544005,9.978942,4.326377,3.008695,2.992053,4.110261,-5.658095,0.007587,5.052985,-9.861113,-2.733548,4.154045,-2.639628,-0.822696,-1.608033,-9.009881,-2.062997,-7.224372,5.340918,-6.398353,-7.820192,-3.586484,-9.579789,-0.167915,-6.051379,5.328545,-3.924589,8.120949,-2.311612,2.666237,-7.865529,1.306502,5.276431,-3.064711,6.128132,-1.696868,-6.334734,7.400070,-3.530680,-9.202564,-2.494084,0.238882,-7.595918,-8.609805,8.283807,-4.415463,7.639369,-6.255590,8.883501,4.467174,1.755621,0.390564,2.109548,-7.803165,-9.334177,-3.178794,0.202060,-2.219249,-4.400574,-0.718499,-2.350023,-0.595617,-2.412758,-2.401524,7.815399,1.381787,0.396595,8.125070,5.427051,-3.412792,-4.581479,-8.249492,7.927113,-9.850680,0.083062,6.578533,1.513466,-3.956968,-1.321205,5.993580,-2.684269,-1.744378,1.272275,-2.831153,2.518496,7.509103,8.261881,6.568532,-7.012192,3.736676,0.190025,6.758526,-4.084459,-3.188198,-4.166399,-2.004022,-6.144117,5.298833,-3.541280,-3.986034,-3.455447,-8.509746,-9.980050,-5.798768,1.998726,-9.232921,-3.184669,7.479190,0.192111,0.592149,2.657075,1.079737,-7.245543,-4.619017,-0.257755,8.020897,-1.769692,4.941860,4.795551,3.188816,2.321824,2.435247,9.007047,-0.413629,0.238021,-6.436211,2.891477,-5.579219,-1.861842,7.547053,-8.220921,-7.910631,-9.203735,0.245862,7.656437,-7.865269,-9.338198,5.221082,-3.452622,4.218836,7.915377,-1.736190,4.473734,8.051736,4.994461,-0.864652,7.493686,-9.338432,-7.645849,8.848900,-9.494843,-1.471908,-8.446499,-7.572776,9.046723,-1.422292,-6.979444,-3.648128,3.425333,9.609314,-8.666728,-5.018014,-7.582979,2.938099,-5.426872,6.063711,-5.569881,-0.454823,6.127518,3.776776,-8.979338,7.915548,-7.616717,-3.027378,0.336029,7.279219,4.304616,4.482896,-5.983120,9.068065,-1.601463,-8.347965,-5.598320,2.603515,8.234540,9.473294,-4.433315,-3.454168,-8.718630,-3.100577,6.667333,3.734329,-4.684594,-0.211255,2.718067,5.868319,-2.511584,-5.546898,-1.329563,-8.936065,-4.804744,2.506995,8.861661,3.668851,-1.449811,4.664308,3.786382,9.804526,-9.633151,1.812657,9.122820,7.166925,-0.506911,-9.488153,8.515708,-9.096663,-6.125271,-9.090458,-7.796262,2.316018,2.519845,-7.163624,2.406318,-0.886348,3.042487,1.461383,8.866650,6.772118,-2.926965,-3.006935,-4.890536,8.364312,4.069055,-5.612641,-7.782276,-5.272798,2.391123,-5.670652,-1.618876,-2.239465,-7.485538,-4.183402,-3.833502,5.840225,-2.654780,-0.552170,6.033353,3.104316,6.912379,-0.545596,-2.325775,1.086914,9.067821,-0.006358,1.489042,3.523000,8.509478,2.940713,9.081446,-0.785943,-2.616004,4.242626,9.751876,-7.095324,-1.088897,-7.035114,-4.818142,-9.601468,4.354266,5.252516,4.773836,1.274052,0.957930,-2.586477,2.501561,-0.610932,8.474776,8.705497,-2.823590,6.455927,-0.078881,2.903393,-2.867788,-4.491928,8.539335,-8.307941,7.137655,0.749948,-1.966306,9.066620,-9.584555,6.209131,9.482128,-6.490767,4.284125,0.312858,1.335392,-3.733265,-5.211628,-5.108948,-9.217939,6.903028,-1.962692,-6.252310,-1.854445,-6.083293,9.641974,4.541061,3.666436,8.175395,0.743973,-0.422852,6.330621,-1.384819,-2.409184,2.607152,5.023362,-0.904074,2.157954,-7.387444,-7.147139,1.892555,2.168533,9.349609,-6.596686,2.322896,7.069120,3.397737,-5.574519,-2.570019,-5.928269,6.963534,-2.498145,6.229267,9.801591,-2.286507,-5.878471,1.067613,-2.902793,-7.098479,3.007379,-1.282997,-2.228043,-8.692971,-0.364400,3.493334,-7.410934,-6.486981,-4.252904,0.316813,-3.228092,2.572347,7.845277,-2.628515,9.972614,-4.009204,-3.354197,4.076195,-1.852120,5.935620,9.816266,0.832903,1.719940,-8.659301,6.788751,4.925150,5.870096,9.329426,-4.489028,-6.694796,-1.066900,-4.031611,-4.932781,3.248734,9.689569,3.754323,2.196184,9.221152,-6.235330,-5.458676,1.648538,7.239639,9.401051,6.118441,-1.061454,6.183924,-9.645861,0.334734,-6.403689,-9.449491,8.389944,-7.977593,-5.230282,-5.313181,7.737156,0.637620,-3.407964,-8.009588,5.400991,4.189922,1.682762,-0.985444,5.588802,-6.972905,8.227492,3.936662,-8.972369,0.115162,4.737828,-8.775562,4.112565,0.606282,-0.061941,6.476652,2.765505,-1.548509,7.055859,9.369207,-8.198633,-6.039871,-6.934479,0.556746,4.852873,9.313866,-0.202274,-1.143644,8.003778,9.317680,5.645016,1.090950,-7.444814,8.868005,8.794078,-0.963852,2.407799,5.783072,-9.689033,-4.220976,8.638787,1.379334,6.612145,1.359942,0.736674,4.513403,5.906967,-0.540718,-8.453439,-2.713068,-4.728220,5.754123,5.326470,3.349446,8.101793,-9.974478,0.125774,-5.383393,2.028755,-3.982788,3.424037,3.105982,-8.778496,-9.670579,6.820359,-8.482207,1.305615,2.117470,-5.449778,-6.801010,2.038359,2.235845,-5.471612,1.888614,9.017900,5.696183,6.291363,-9.588186,-8.118057,-5.350681,8.867327,4.230508,6.221254,5.285640,0.149183,0.511389,-4.357929,8.009867,9.959936,-1.458975,-6.562694,9.316362,-6.256524,-0.762676,-8.947366,7.674809,6.752784,-5.594651,3.665214,6.731090,2.816083,1.259986,9.735961,9.394860,-0.911788,2.949837,0.184019,-9.908326,-1.592533,-5.010985,-6.565260,-6.309116,-4.904763,-9.870127,7.647097,-9.330394,-5.014038,-2.983193,-5.436740,-7.018331,-4.257727,-4.141109,-6.861207,8.490701,8.979466,2.801893,4.479817,7.888270,-9.085837,-6.000139,5.180552,1.253126,-7.711368,1.135401,0.939082,5.618763,-3.753668,2.280459,6.979190,5.534454,-8.556524,-1.505521,8.664391,6.757977,6.607382,9.657440,-3.341264,-4.790984,-2.543470,6.940027,-4.732600,0.489353,-4.256608,4.318753,-6.878222,-3.447339,-5.648151,-3.063764,1.163490,7.354863,9.006250,7.607035,5.404437,4.331437,-6.655950,1.284373,1.607709,2.122479,9.174742,5.131177,4.593224,-0.298887,-3.032258,7.887447,-3.370519,-3.505488,4.662409,0.626829,-9.332296,5.259047,-2.122795,8.897701,0.413709,2.285612,8.002966,-8.393730,0.122301,-4.223724,-8.858946,8.829829,4.509624,-2.771953,8.429749], dtype = "float64")#candidate|1645|(720,)|const|float64
call_1644 = relay.TupleGetItem(func_1587_call(relay.reshape(const_1645.astype('float64'), [8, 15, 6])), 0)
call_1646 = relay.TupleGetItem(func_1590_call(relay.reshape(const_1645.astype('float64'), [8, 15, 6])), 0)
output = relay.Tuple([bop_1619,call_1630,var_1631,bop_1636,call_1644,const_1645,])
output2 = relay.Tuple([bop_1619,call_1632,var_1631,bop_1639,call_1646,const_1645,])
func_1647 = relay.Function([var_1617,var_1618,var_1631,], output)
mod['func_1647'] = func_1647
mod = relay.transform.InferType()(mod)
var_1648 = relay.var("var_1648", dtype = "float64", shape = (9, 5, 2))#candidate|1648|(9, 5, 2)|var|float64
var_1649 = relay.var("var_1649", dtype = "float64", shape = (9, 5, 2))#candidate|1649|(9, 5, 2)|var|float64
var_1650 = relay.var("var_1650", dtype = "bool", shape = (216,))#candidate|1650|(216,)|var|bool
output = func_1647(var_1648,var_1649,var_1650,)
func_1651 = relay.Function([var_1648,var_1649,var_1650,], output)
mutated_mod['func_1651'] = func_1651
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1656 = relay.var("var_1656", dtype = "float64", shape = (6, 1, 5))#candidate|1656|(6, 1, 5)|var|float64
uop_1657 = relay.sqrt(var_1656.astype('float64')) # shape=(6, 1, 5)
bop_1661 = relay.greater_equal(uop_1657.astype('bool'), relay.reshape(var_1656.astype('bool'), relay.shape_of(uop_1657))) # shape=(6, 1, 5)
func_935_call = mod.get_global_var('func_935')
func_938_call = mutated_mod.get_global_var('func_938')
const_1669 = relay.const([-3,-5,6,-7,-2,5,-5,8,7,2,5,2,1,7,3,10,-9,-9,7,-9,-2,-5,-9,-4,-8,-6,6,-4,-9,4,8,-6,-8,-1,-10,6,-7,1,-3,-2,1,-3,-7,-3,-1], dtype = "int32")#candidate|1669|(45,)|const|int32
call_1668 = relay.TupleGetItem(func_935_call(relay.reshape(const_1669.astype('int32'), [45,])), 1)
call_1670 = relay.TupleGetItem(func_938_call(relay.reshape(const_1669.astype('int32'), [45,])), 1)
func_1647_call = mod.get_global_var('func_1647')
func_1651_call = mutated_mod.get_global_var('func_1651')
var_1675 = relay.var("var_1675", dtype = "float64", shape = (90,))#candidate|1675|(90,)|var|float64
var_1676 = relay.var("var_1676", dtype = "bool", shape = (216,))#candidate|1676|(216,)|var|bool
call_1674 = relay.TupleGetItem(func_1647_call(relay.reshape(var_1675.astype('float64'), [9, 5, 2]), relay.reshape(var_1675.astype('float64'), [9, 5, 2]), relay.reshape(var_1676.astype('bool'), [216,]), ), 1)
call_1677 = relay.TupleGetItem(func_1651_call(relay.reshape(var_1675.astype('float64'), [9, 5, 2]), relay.reshape(var_1675.astype('float64'), [9, 5, 2]), relay.reshape(var_1676.astype('bool'), [216,]), ), 1)
bop_1680 = relay.floor_divide(bop_1661.astype('float64'), relay.reshape(uop_1657.astype('float64'), relay.shape_of(bop_1661))) # shape=(6, 1, 5)
func_373_call = mod.get_global_var('func_373')
func_377_call = mutated_mod.get_global_var('func_377')
call_1692 = relay.TupleGetItem(func_373_call(relay.reshape(call_1674.astype('bool'), [3, 9, 8]), relay.reshape(var_1676.astype('bool'), [3, 9, 8]), ), 1)
call_1693 = relay.TupleGetItem(func_377_call(relay.reshape(call_1674.astype('bool'), [3, 9, 8]), relay.reshape(var_1676.astype('bool'), [3, 9, 8]), ), 1)
bop_1699 = relay.equal(bop_1661.astype('bool'), relay.reshape(bop_1680.astype('bool'), relay.shape_of(bop_1661))) # shape=(6, 1, 5)
uop_1706 = relay.asinh(uop_1657.astype('float64')) # shape=(6, 1, 5)
uop_1711 = relay.sinh(uop_1706.astype('float64')) # shape=(6, 1, 5)
output = relay.Tuple([call_1668,const_1669,call_1674,var_1675,var_1676,call_1692,bop_1699,uop_1711,])
output2 = relay.Tuple([call_1670,const_1669,call_1677,var_1675,var_1676,call_1693,bop_1699,uop_1711,])
func_1721 = relay.Function([var_1656,var_1675,var_1676,], output)
mod['func_1721'] = func_1721
mod = relay.transform.InferType()(mod)
mutated_mod['func_1721'] = func_1721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1721_call = mutated_mod.get_global_var('func_1721')
var_1723 = relay.var("var_1723", dtype = "float64", shape = (6, 1, 5))#candidate|1723|(6, 1, 5)|var|float64
var_1724 = relay.var("var_1724", dtype = "float64", shape = (90,))#candidate|1724|(90,)|var|float64
var_1725 = relay.var("var_1725", dtype = "bool", shape = (216,))#candidate|1725|(216,)|var|bool
call_1722 = func_1721_call(var_1723,var_1724,var_1725,)
output = call_1722
func_1726 = relay.Function([var_1723,var_1724,var_1725,], output)
mutated_mod['func_1726'] = func_1726
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1770 = relay.var("var_1770", dtype = "float32", shape = (3, 6, 7))#candidate|1770|(3, 6, 7)|var|float32
uop_1771 = relay.rsqrt(var_1770.astype('float32')) # shape=(3, 6, 7)
uop_1782 = relay.asin(uop_1771.astype('float32')) # shape=(3, 6, 7)
output = relay.Tuple([uop_1782,])
output2 = relay.Tuple([uop_1782,])
func_1791 = relay.Function([var_1770,], output)
mod['func_1791'] = func_1791
mod = relay.transform.InferType()(mod)
var_1792 = relay.var("var_1792", dtype = "float32", shape = (3, 6, 7))#candidate|1792|(3, 6, 7)|var|float32
output = func_1791(var_1792)
func_1793 = relay.Function([var_1792], output)
mutated_mod['func_1793'] = func_1793
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1869 = relay.var("var_1869", dtype = "float32", shape = (15, 9, 10))#candidate|1869|(15, 9, 10)|var|float32
uop_1870 = relay.acos(var_1869.astype('float32')) # shape=(15, 9, 10)
func_250_call = mod.get_global_var('func_250')
func_253_call = mutated_mod.get_global_var('func_253')
var_1883 = relay.var("var_1883", dtype = "float32", shape = (50, 6))#candidate|1883|(50, 6)|var|float32
call_1882 = func_250_call(relay.reshape(var_1883.astype('float32'), [2, 15, 10]))
call_1884 = func_250_call(relay.reshape(var_1883.astype('float32'), [2, 15, 10]))
uop_1887 = relay.acosh(uop_1870.astype('float32')) # shape=(15, 9, 10)
func_373_call = mod.get_global_var('func_373')
func_377_call = mutated_mod.get_global_var('func_377')
const_1907 = relay.const([False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,False], dtype = "bool")#candidate|1907|(216,)|const|bool
call_1906 = relay.TupleGetItem(func_373_call(relay.reshape(const_1907.astype('bool'), [3, 9, 8]), relay.reshape(const_1907.astype('bool'), [3, 9, 8]), ), 0)
call_1908 = relay.TupleGetItem(func_377_call(relay.reshape(const_1907.astype('bool'), [3, 9, 8]), relay.reshape(const_1907.astype('bool'), [3, 9, 8]), ), 0)
output = relay.Tuple([call_1882,var_1883,uop_1887,call_1906,const_1907,])
output2 = relay.Tuple([call_1884,var_1883,uop_1887,call_1908,const_1907,])
func_1912 = relay.Function([var_1869,var_1883,], output)
mod['func_1912'] = func_1912
mod = relay.transform.InferType()(mod)
var_1913 = relay.var("var_1913", dtype = "float32", shape = (15, 9, 10))#candidate|1913|(15, 9, 10)|var|float32
var_1914 = relay.var("var_1914", dtype = "float32", shape = (50, 6))#candidate|1914|(50, 6)|var|float32
output = func_1912(var_1913,var_1914,)
func_1915 = relay.Function([var_1913,var_1914,], output)
mutated_mod['func_1915'] = func_1915
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2040 = relay.const([[[10,-2,8,3],[10,-7,-9,-7],[2,3,6,9],[2,-5,-5,-4],[-8,3,-6,2],[-4,-7,7,-1],[-9,-2,-6,1]],[[2,5,-6,-2],[9,8,2,1],[8,-6,1,7],[6,7,10,-10],[-3,-10,5,-1],[5,-2,-1,2],[-3,8,10,6]],[[-5,-5,-2,-9],[-9,-1,-9,1],[-4,-3,-7,8],[-5,-4,2,-8],[4,1,-8,10],[-9,4,-5,-4],[-1,8,3,-8]],[[2,1,3,-8],[3,-4,2,-10],[4,9,-2,-10],[1,9,-2,10],[10,-8,1,1],[-9,-6,-8,2],[-2,-3,3,5]],[[1,-7,2,1],[-1,4,-6,7],[-1,-4,9,3],[6,-6,-1,-4],[7,-9,9,1],[-8,-3,2,-8],[10,2,-10,3]],[[-4,5,-1,10],[-10,-7,9,-10],[-2,1,-2,-7],[-3,-4,-7,-8],[-9,6,6,8],[-5,7,-10,10],[2,6,-10,-6]],[[5,7,10,-2],[-2,9,-4,-4],[-9,-2,-9,-10],[6,7,-2,-1],[5,-8,-5,6],[-9,-3,-9,2],[7,-6,8,9]]], dtype = "int8")#candidate|2040|(7, 7, 4)|const|int8
var_2041 = relay.var("var_2041", dtype = "int8", shape = (7, 7, 4))#candidate|2041|(7, 7, 4)|var|int8
bop_2042 = relay.left_shift(const_2040.astype('int8'), relay.reshape(var_2041.astype('int8'), relay.shape_of(const_2040))) # shape=(7, 7, 4)
output = relay.Tuple([bop_2042,])
output2 = relay.Tuple([bop_2042,])
func_2046 = relay.Function([var_2041,], output)
mod['func_2046'] = func_2046
mod = relay.transform.InferType()(mod)
var_2047 = relay.var("var_2047", dtype = "int8", shape = (7, 7, 4))#candidate|2047|(7, 7, 4)|var|int8
output = func_2046(var_2047)
func_2048 = relay.Function([var_2047], output)
mutated_mod['func_2048'] = func_2048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2182 = relay.var("var_2182", dtype = "float32", shape = (8, 14, 15))#candidate|2182|(8, 14, 15)|var|float32
uop_2183 = relay.acos(var_2182.astype('float32')) # shape=(8, 14, 15)
func_1587_call = mod.get_global_var('func_1587')
func_1590_call = mutated_mod.get_global_var('func_1590')
var_2191 = relay.var("var_2191", dtype = "float64", shape = (720,))#candidate|2191|(720,)|var|float64
call_2190 = relay.TupleGetItem(func_1587_call(relay.reshape(var_2191.astype('float64'), [8, 15, 6])), 1)
call_2192 = relay.TupleGetItem(func_1590_call(relay.reshape(var_2191.astype('float64'), [8, 15, 6])), 1)
uop_2202 = relay.atan(var_2182.astype('float32')) # shape=(8, 14, 15)
output = relay.Tuple([uop_2183,call_2190,var_2191,uop_2202,])
output2 = relay.Tuple([uop_2183,call_2192,var_2191,uop_2202,])
func_2206 = relay.Function([var_2182,var_2191,], output)
mod['func_2206'] = func_2206
mod = relay.transform.InferType()(mod)
var_2207 = relay.var("var_2207", dtype = "float32", shape = (8, 14, 15))#candidate|2207|(8, 14, 15)|var|float32
var_2208 = relay.var("var_2208", dtype = "float64", shape = (720,))#candidate|2208|(720,)|var|float64
output = func_2206(var_2207,var_2208,)
func_2209 = relay.Function([var_2207,var_2208,], output)
mutated_mod['func_2209'] = func_2209
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2532 = relay.const([[[2.340569,1.230690,3.917769,2.272021],[4.169442,-7.128862,2.014049,-6.343241],[-5.295293,-0.566097,-7.940312,2.703389],[2.936004,-0.715750,-8.722608,0.698372],[-9.849732,-3.876019,4.901466,3.964953]],[[-4.769270,4.536257,-9.471870,-5.883652],[4.626355,-9.204427,2.574916,-1.590180],[6.232497,-0.486180,-8.258558,8.392585],[4.027198,0.938582,9.283011,5.703046],[-1.170295,2.358016,6.090091,7.076805]],[[4.759756,-7.083115,0.564460,1.486760],[0.713187,-0.888630,4.639917,8.389135],[3.312515,-4.436110,8.519696,0.328753],[-2.224944,-7.927338,-0.385519,-3.761814],[-5.584421,-5.975526,2.254036,-6.089056]],[[-9.893180,-7.803599,-4.973640,-4.611098],[-4.943701,-4.860898,-2.556432,-8.675679],[-9.696655,-1.896121,-1.827460,-9.662039],[4.605542,1.159479,5.160977,-4.832504],[-2.849425,9.158773,-2.543825,9.504204]],[[-7.731548,-1.900284,6.020578,1.820980],[9.554003,-8.610515,-0.838462,-5.820010],[5.102011,-2.929981,0.101110,-2.821935],[-1.859586,-9.875652,2.825517,0.214093],[7.785023,8.885859,-3.331866,7.571164]],[[-9.660337,-0.363460,-9.074247,8.526007],[-7.488021,-9.503571,-0.944547,7.720221],[2.045047,0.567156,7.580006,-8.695093],[-1.243230,1.254286,2.913422,-4.869397],[-3.544394,-1.205540,-0.252380,1.854364]]], dtype = "float64")#candidate|2532|(6, 5, 4)|const|float64
uop_2533 = relay.sigmoid(const_2532.astype('float64')) # shape=(6, 5, 4)
func_935_call = mod.get_global_var('func_935')
func_938_call = mutated_mod.get_global_var('func_938')
var_2541 = relay.var("var_2541", dtype = "int32", shape = (45,))#candidate|2541|(45,)|var|int32
call_2540 = relay.TupleGetItem(func_935_call(relay.reshape(var_2541.astype('int32'), [45,])), 4)
call_2542 = relay.TupleGetItem(func_938_call(relay.reshape(var_2541.astype('int32'), [45,])), 4)
output = relay.Tuple([uop_2533,call_2540,var_2541,])
output2 = relay.Tuple([uop_2533,call_2542,var_2541,])
func_2546 = relay.Function([var_2541,], output)
mod['func_2546'] = func_2546
mod = relay.transform.InferType()(mod)
mutated_mod['func_2546'] = func_2546
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2547 = relay.var("var_2547", dtype = "int32", shape = (45,))#candidate|2547|(45,)|var|int32
func_2546_call = mutated_mod.get_global_var('func_2546')
call_2548 = func_2546_call(var_2547)
output = call_2548
func_2549 = relay.Function([var_2547], output)
mutated_mod['func_2549'] = func_2549
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2698 = relay.var("var_2698", dtype = "int32", shape = (5, 13, 14))#candidate|2698|(5, 13, 14)|var|int32
const_2699 = relay.const([[[-5,-10,5,8,3,-2,8,-8,-10,1,-1,-9,7,6],[6,-9,10,8,1,7,-7,-7,-10,8,-7,5,-1,-5],[-2,2,6,-9,-3,6,-2,8,-1,-6,9,2,-1,8],[-9,-4,-3,1,10,-10,6,6,8,-7,8,-3,-5,5],[-9,-2,5,1,2,1,-3,-6,-8,9,8,-6,-9,-5],[3,-4,2,-3,2,7,8,-6,1,-2,-4,-5,-6,9],[10,-2,6,5,10,7,4,5,-3,4,3,-3,8,-1],[6,10,6,7,7,-1,2,10,3,-9,-8,-10,-1,-10],[-8,-5,-3,-2,-8,2,-3,-4,-1,2,-10,10,-3,1],[-5,7,3,10,7,-6,3,2,-1,10,1,-5,2,-10],[-10,-3,3,-10,9,6,-4,-5,-2,-2,3,4,5,-8],[-9,-3,1,-3,5,-5,-5,-2,-3,5,-4,-6,-2,-5],[-2,-3,-3,-9,4,1,7,-4,4,3,-3,-3,-7,7]],[[1,-6,5,3,10,2,-8,-1,-8,-9,-3,2,-3,4],[-5,-1,3,9,-9,-3,8,2,10,-1,10,-5,-4,-8],[3,9,5,6,7,3,10,6,-3,4,-2,6,-6,-5],[-9,7,7,1,6,-7,3,-1,-7,-10,3,-8,10,-7],[4,-7,4,-6,-10,10,-4,-8,-6,1,6,-6,7,6],[-7,-6,-6,3,-6,1,-7,1,8,2,8,1,-5,3],[-10,-3,-3,-7,1,8,-10,5,-10,1,-8,5,-6,-8],[-1,5,9,8,7,10,5,9,-5,-3,3,-2,-6,-6],[3,-3,4,-6,8,-6,9,-6,2,-8,-10,-1,-4,5],[-1,-2,5,-9,-5,-4,10,7,6,2,9,-4,-2,3],[9,7,8,-4,-7,4,9,3,1,-9,-5,4,4,2],[-4,-3,2,-3,-1,7,-2,-8,-2,2,-2,10,-5,-9],[4,-4,-6,-3,9,3,5,-6,3,-9,4,8,-4,1]],[[-3,-8,-2,7,-9,8,-8,-8,1,3,-5,-8,-4,4],[3,7,8,4,8,-7,4,7,-6,-9,6,-10,-4,1],[-3,8,-2,3,-10,9,-2,5,2,2,-6,5,-10,-4],[-1,2,3,1,5,-5,-5,-3,1,-5,-1,-8,-5,-8],[8,-9,10,-5,1,8,2,-1,6,-5,1,9,-4,-8],[2,6,-9,-10,-8,1,3,-7,1,-5,1,3,8,5],[-8,3,-6,-1,5,3,-8,-5,2,-9,2,-1,2,7],[5,-3,3,-7,4,6,-9,3,5,-8,1,-1,1,-6],[-7,4,4,-9,3,10,1,-7,8,8,9,2,5,-5],[-7,-1,5,-8,-3,8,2,5,5,-4,5,6,-9,-6],[-2,-3,1,5,9,4,10,-10,-1,4,9,9,-1,10],[3,-6,-6,-4,-3,2,2,-6,10,-3,-4,-9,8,-9],[-4,10,-4,10,5,8,5,-2,5,-9,7,-10,-2,4]],[[-8,10,-1,-7,7,6,5,2,3,9,5,7,-2,10],[5,-6,6,-2,6,-1,-9,7,-2,-4,-4,-3,10,8],[6,-8,2,3,-9,5,4,-8,-5,-7,-3,-2,-3,-7],[-6,7,-5,-2,-10,-6,-9,4,-7,8,-5,-10,7,9],[-8,5,1,5,-6,4,-9,-4,-1,4,9,3,7,4],[5,6,-10,-5,-2,9,-7,-3,-5,-5,-5,6,10,-10],[1,3,-9,-9,-1,-2,-7,10,-5,-10,-3,-7,-5,4],[10,-4,-10,-9,7,8,6,-10,10,-7,-4,3,6,-6],[3,-6,-4,6,-7,-2,6,-2,-7,-5,2,-2,-1,-6],[7,9,3,-4,8,-10,-8,-1,2,5,6,8,4,-6],[5,3,3,-3,-7,-3,7,-2,-8,9,4,1,4,8],[9,2,-6,-7,6,7,-5,10,6,10,3,-3,-3,-9],[-6,-6,10,9,4,-7,6,-6,4,6,6,-3,-3,-5]],[[1,-5,10,-1,9,8,-8,4,9,-6,5,-5,7,-7],[-4,-9,8,-3,-5,-9,-6,10,4,-9,-5,7,6,9],[10,6,-2,-1,8,7,10,-10,4,2,5,2,6,-9],[1,-8,6,7,8,8,-1,1,-2,-10,2,-4,-3,6],[6,-2,5,-10,-3,-1,-2,-10,4,8,4,-4,-8,-3],[5,-10,7,9,-3,5,3,-8,-6,2,10,6,8,10],[8,-8,-5,7,-10,5,5,-9,7,7,-8,3,-9,-3],[9,-4,9,4,-10,-7,7,-4,-4,-5,4,4,1,9],[-6,-8,8,-6,1,2,-2,2,10,4,-10,-3,-10,-6],[4,-2,10,9,-9,-6,6,-4,4,8,1,-8,-2,7],[9,3,-1,-6,-5,8,2,6,1,-4,5,10,5,-1],[8,9,1,3,-8,-2,7,-7,-3,7,-5,10,-5,8],[-6,-9,6,4,-1,-9,9,2,-3,-3,5,2,-2,-2]]], dtype = "int32")#candidate|2699|(5, 13, 14)|const|int32
bop_2700 = relay.multiply(var_2698.astype('int32'), relay.reshape(const_2699.astype('int32'), relay.shape_of(var_2698))) # shape=(5, 13, 14)
func_250_call = mod.get_global_var('func_250')
func_253_call = mutated_mod.get_global_var('func_253')
const_2715 = relay.const([-9.151767,-9.993374,7.972198,-7.923525,-8.369965,8.361438,-1.927769,5.053989,9.780235,4.588897,3.419009,1.223619,0.564617,1.002242,-6.603806,6.717030,8.975030,3.424773,-2.293202,4.719979,9.953713,-0.455892,-4.818066,0.864619,-4.879234,8.910591,2.149200,6.169719,-2.034247,9.946966,-5.465693,4.169947,-6.437381,7.186424,-3.331346,8.322892,5.711621,5.470195,-4.309973,2.885183,-2.014320,-0.223143,2.305613,-8.081823,-3.069346,-1.487735,-7.631822,-6.650220,8.210379,-2.597485,5.812051,8.552553,5.092874,-4.646561,5.470660,-5.298550,0.420527,1.478045,-6.768545,-0.317698,9.901446,-8.207611,7.595761,-8.484752,-2.857020,-0.889128,0.234235,-2.898147,7.344404,-2.134528,-0.351770,-3.008191,2.393667,7.945162,1.412416,-4.313119,-9.982895,2.988065,-3.992716,-0.125539,-1.679665,-3.988419,-2.833636,-0.358493,1.920017,0.369656,-6.171505,2.579654,3.837561,1.450174,4.456095,-6.843125,-5.243923,8.542953,4.252166,5.715220,-5.146660,9.188468,-5.888505,-2.812152,-2.721610,-2.920514,9.176518,-4.267161,-6.724479,-5.570570,-3.208373,1.323317,-0.522852,5.504997,0.436498,5.876797,-0.732715,-2.574153,-1.795343,-9.708072,-0.450304,0.800757,5.560033,2.860061,-8.994385,0.947069,-5.317949,7.981507,7.907728,-3.314755,-6.675800,-2.580070,0.674968,1.757415,-7.638624,-2.509755,-6.137499,-3.730276,-0.154644,2.226574,3.335530,5.345222,-9.500625,-7.553052,4.099287,-9.819484,-3.263302,-7.613688,0.193669,-4.331326,7.767489,5.991792,-9.946679,9.273828,4.234680,6.579567,5.125041,-9.743597,-6.516059,9.513336,2.381243,3.258397,7.227119,7.099011,8.992626,-7.276776,2.706127,7.756872,7.069056,-1.425238,2.017364,-3.743217,-4.029677,-9.822471,7.670096,-8.583782,6.960498,4.346156,0.594009,-3.915130,-2.038810,7.596208,-5.038313,3.698364,-6.430419,-4.788364,-5.415797,-9.684660,0.641830,3.171209,2.414056,8.912985,5.043530,2.414728,-3.775774,0.028684,-8.341867,-3.062471,0.155104,-7.897880,7.389139,-8.394974,6.803623,-8.134389,2.715270,-7.073986,4.370524,-5.974522,-9.521211,1.522544,6.240915,6.645022,2.523771,-8.237680,7.244304,-1.563054,7.613159,-6.776208,-8.185324,6.335566,-6.542127,-0.032510,1.380582,-0.262075,-0.897094,-7.576688,7.448040,8.651844,9.589955,8.247116,-1.712843,8.920346,-3.657266,0.457912,-8.305468,2.199646,-2.133050,-1.174303,-2.874926,1.232204,-9.823539,-4.043464,2.766669,0.372342,4.162872,2.535892,-5.050735,6.760781,5.807600,9.623388,3.272158,-8.417246,-8.029787,4.654029,-8.225010,6.001037,3.173110,-8.088093,9.462495,5.417467,-3.058844,5.023808,-1.770141,-5.408813,8.351359,1.782948,-1.966466,-5.684299,3.792951,7.237448,-9.585185,-7.267798,-4.411661,-1.310501,-3.574433,-5.985033,-0.992447,-3.541833,-6.371319,-8.246384,-5.724264,-6.385419,-2.501413,-4.377984,-1.196504,9.425895,-1.936030,-7.773174,-1.299666,1.501510,5.591606,5.770932,9.654091,-3.213752,-9.667275,2.950477,-0.657221,6.063186,-9.694676,-3.301432,0.721097,6.779426,-1.213769,-7.058646], dtype = "float32")#candidate|2715|(300,)|const|float32
call_2714 = func_250_call(relay.reshape(const_2715.astype('float32'), [2, 15, 10]))
call_2716 = func_250_call(relay.reshape(const_2715.astype('float32'), [2, 15, 10]))
output = relay.Tuple([bop_2700,call_2714,const_2715,])
output2 = relay.Tuple([bop_2700,call_2716,const_2715,])
func_2721 = relay.Function([var_2698,], output)
mod['func_2721'] = func_2721
mod = relay.transform.InferType()(mod)
mutated_mod['func_2721'] = func_2721
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2722 = relay.var("var_2722", dtype = "int32", shape = (5, 13, 14))#candidate|2722|(5, 13, 14)|var|int32
func_2721_call = mutated_mod.get_global_var('func_2721')
call_2723 = func_2721_call(var_2722)
output = call_2723
func_2724 = relay.Function([var_2722], output)
mutated_mod['func_2724'] = func_2724
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2748 = relay.const([[[6.973035,-5.456342,8.696955,-0.464198,9.708301,0.540549,-1.074383,6.088479,6.361316,7.490187,6.833476,0.691423,5.605724,-0.423847]],[[-0.536580,1.908818,3.496973,6.242757,-6.080436,6.997869,-1.702014,-2.068189,9.197582,-4.074309,5.807680,4.161794,8.060499,-5.029046]],[[5.124697,-9.253349,-4.748161,3.036287,7.746224,0.488397,5.444333,9.182138,7.881608,-3.568173,8.819320,3.030433,3.666575,-4.514883]],[[-8.856526,1.141884,0.689214,2.050657,5.898917,1.958838,-4.062771,1.884888,0.795549,0.324798,-9.200276,1.069796,-7.822244,-8.278126]],[[2.032888,-9.340864,-0.054071,-1.902420,-6.223065,7.524018,-6.391510,-1.706143,9.066736,-7.831210,4.012507,3.574442,-3.018344,8.356317]],[[-6.637883,-4.209779,-4.865748,3.340211,-2.571703,-8.250583,6.871281,-8.928064,-4.071300,-0.932572,-5.808529,-9.759691,7.514582,5.062787]],[[7.629583,-0.294553,3.948439,2.033397,-0.196828,-6.182794,-0.739832,3.760401,-3.283181,-5.278277,-8.793656,5.058030,6.436765,-1.247901]],[[6.987486,-2.175116,7.947856,-0.660625,7.245498,-6.875213,-0.553061,-3.777791,-3.458408,7.128379,-7.603898,0.957286,-5.258374,1.143010]],[[3.889068,-7.409642,-4.793747,3.395934,-5.913937,-0.454184,2.383676,3.252074,2.711392,6.623341,7.913011,-0.279219,-1.534894,-3.889246]],[[-6.705685,-3.419756,-0.503163,6.313927,-8.109331,-4.888024,-9.184546,-1.405156,0.611117,-8.522208,-8.980134,-9.113603,-7.168874,7.806704]],[[0.062467,9.569792,3.114118,9.783018,9.150756,-1.070432,1.705040,-8.317168,4.570743,5.025384,-5.400553,9.241602,1.971913,-6.443084]],[[1.874139,-1.099967,6.487930,-8.852936,-6.081209,-2.414741,-4.904757,2.462624,6.291921,-3.609134,-5.567527,-1.666645,9.200149,3.695277]],[[9.988123,-8.987577,5.254035,7.100117,-3.405723,-3.173997,0.578412,-2.782349,9.569763,5.271028,1.370643,-5.062233,-5.659141,-7.615085]],[[-5.963317,-8.460931,5.759626,-1.647734,-8.835648,-3.649092,-8.319946,5.122198,4.157833,7.645224,1.431771,-9.266032,-9.790269,-1.610202]]], dtype = "float32")#candidate|2748|(14, 1, 14)|const|float32
uop_2749 = relay.acos(const_2748.astype('float32')) # shape=(14, 1, 14)
uop_2752 = relay.sin(uop_2749.astype('float64')) # shape=(14, 1, 14)
output = uop_2752
output2 = uop_2752
func_2754 = relay.Function([], output)
mod['func_2754'] = func_2754
mod = relay.transform.InferType()(mod)
mutated_mod['func_2754'] = func_2754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2754_call = mutated_mod.get_global_var('func_2754')
call_2755 = func_2754_call()
output = call_2755
func_2756 = relay.Function([], output)
mutated_mod['func_2756'] = func_2756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2754_call = mod.get_global_var('func_2754')
func_2756_call = mutated_mod.get_global_var('func_2756')
call_2761 = func_2754_call()
call_2762 = func_2754_call()
uop_2765 = relay.tan(call_2761.astype('float64')) # shape=(14, 1, 14)
uop_2767 = relay.tan(call_2762.astype('float64')) # shape=(14, 1, 14)
bop_2776 = relay.bitwise_xor(uop_2765.astype('int8'), relay.reshape(call_2761.astype('int8'), relay.shape_of(uop_2765))) # shape=(14, 1, 14)
bop_2779 = relay.bitwise_xor(uop_2767.astype('int8'), relay.reshape(call_2762.astype('int8'), relay.shape_of(uop_2767))) # shape=(14, 1, 14)
bop_2780 = relay.mod(uop_2765.astype('float32'), relay.reshape(bop_2776.astype('float32'), relay.shape_of(uop_2765))) # shape=(14, 1, 14)
bop_2783 = relay.mod(uop_2767.astype('float32'), relay.reshape(bop_2779.astype('float32'), relay.shape_of(uop_2767))) # shape=(14, 1, 14)
uop_2789 = relay.sigmoid(bop_2776.astype('float64')) # shape=(14, 1, 14)
uop_2791 = relay.sigmoid(bop_2779.astype('float64')) # shape=(14, 1, 14)
output = relay.Tuple([bop_2780,uop_2789,])
output2 = relay.Tuple([bop_2783,uop_2791,])
func_2798 = relay.Function([], output)
mod['func_2798'] = func_2798
mod = relay.transform.InferType()(mod)
output = func_2798()
func_2799 = relay.Function([], output)
mutated_mod['func_2799'] = func_2799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2798_call = mod.get_global_var('func_2798')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_2844 = relay.TupleGetItem(func_2798_call(), 1)
call_2845 = relay.TupleGetItem(func_2799_call(), 1)
output = relay.Tuple([call_2844,])
output2 = relay.Tuple([call_2845,])
func_2852 = relay.Function([], output)
mod['func_2852'] = func_2852
mod = relay.transform.InferType()(mod)
output = func_2852()
func_2853 = relay.Function([], output)
mutated_mod['func_2853'] = func_2853
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2854 = relay.const([[[2,9,-7,-2,10,-4,9],[-2,-10,10,3,-8,-3,-7],[-1,-4,-8,-5,-5,-2,10],[9,-4,6,10,-5,-8,-1],[-7,5,-5,-3,1,10,4],[-2,-9,-4,2,7,10,4],[-7,10,-5,4,-5,5,-4],[3,-6,-4,3,-8,-10,6],[6,-7,-7,7,-5,4,-7],[-5,3,-10,-2,-3,-2,2],[5,3,8,-6,-8,-6,3],[10,-8,-2,-2,9,-9,-9],[-5,-5,8,4,10,10,-3],[1,-6,-10,6,3,-6,-4]],[[-5,8,-3,-2,4,7,-6],[-10,-3,8,3,-4,-10,9],[-1,3,-5,8,5,-8,-6],[3,-2,-2,3,6,8,5],[9,3,6,-8,6,-8,5],[-2,-1,-4,7,9,8,5],[5,5,5,-6,4,3,-7],[3,-7,5,-9,2,-7,-5],[6,4,-2,-7,-4,8,-4],[-10,-2,-7,7,10,10,-1],[2,-5,-5,-2,-5,4,10],[9,-2,9,1,6,5,-1],[7,6,-7,-8,10,-9,-8],[6,4,-4,-6,2,-8,-3]],[[-4,9,-8,9,-6,8,-8],[10,-10,6,4,2,-2,7],[-5,-2,-7,-8,-8,2,7],[-1,-9,-1,-9,-4,-6,3],[1,7,-10,-2,-1,-6,9],[-2,-10,-3,6,-9,-10,8],[-7,5,2,-1,10,1,-6],[-10,-5,-1,-9,-5,8,-10],[4,8,2,1,-5,6,8],[9,-6,-8,5,-5,6,9],[-3,6,-8,1,8,-4,4],[2,-1,3,2,-6,3,-3],[-3,-4,-1,6,-5,-1,-8],[-5,7,4,10,5,1,1]],[[5,4,6,6,6,-9,8],[-3,-7,9,-8,3,-10,-10],[-10,-4,4,-4,-6,10,-10],[-5,8,-5,6,10,6,-2],[10,7,4,6,1,-8,10],[-1,6,-1,1,1,9,-5],[-5,-1,-8,8,10,-10,3],[8,-8,4,-2,-10,10,-4],[5,5,-4,-6,5,-6,7],[5,-6,1,-9,-9,9,-6],[3,1,-9,9,-3,10,8],[-2,-2,4,8,-3,10,10],[3,2,7,-5,2,-2,10],[2,7,-2,-8,8,-2,7]],[[-5,5,4,-6,-3,-9,-7],[-7,-4,5,-2,2,-5,-10],[-1,1,3,-6,3,1,-6],[-10,-5,10,-5,-1,-3,-9],[-3,-5,5,2,4,-6,-1],[5,-9,-10,2,-4,-6,4],[-7,-8,-1,9,-1,-3,-1],[1,5,-1,1,-9,-3,9],[-7,7,-5,6,-7,3,6],[-2,4,10,9,4,-3,2],[5,5,6,5,8,9,-6],[5,6,-2,-1,2,4,-2],[8,-4,7,4,-3,5,8],[-9,6,-10,-1,5,-3,-2]],[[2,5,-9,-4,10,10,-4],[-7,8,-1,-9,-9,1,2],[10,4,-5,-1,-10,1,-2],[5,5,-8,-7,-9,10,-9],[-3,-7,-5,2,-10,6,-9],[-9,-7,5,-6,7,4,2],[-6,-4,-3,2,2,8,9],[1,1,9,4,-2,-8,4],[6,5,8,-3,-10,7,-10],[-3,8,-7,4,9,-1,-8],[9,-3,7,-9,9,6,-6],[1,-9,-5,8,6,-9,8],[5,10,-8,-8,-1,10,8],[1,-8,-2,-9,-3,-10,-7]],[[-5,10,2,3,3,7,-8],[-3,-4,2,9,10,-10,2],[-4,-2,7,1,4,-1,5],[10,-6,8,9,5,-4,3],[8,6,6,4,-2,3,9],[2,4,7,-6,4,-7,-3],[-2,4,2,5,-2,3,4],[-9,-2,8,2,9,-2,-3],[-2,7,3,-7,5,-4,10],[10,-5,-8,-9,-4,4,9],[8,3,6,-5,3,-3,3],[5,7,7,4,9,-4,4],[-8,-1,3,-6,6,-8,-5],[-9,-10,-2,-10,7,6,7]],[[8,-7,-4,-3,-4,8,2],[1,6,-6,4,3,8,-10],[-5,4,10,-10,-2,1,-3],[8,-4,-5,-8,-9,10,6],[2,-2,-3,-2,8,7,-4],[5,-9,3,1,6,-8,2],[6,7,4,-7,-6,9,-1],[-3,7,2,-3,9,-10,1],[-9,7,-1,-5,4,1,3],[3,6,-8,-5,7,5,2],[-3,7,-6,-9,-1,-1,8],[-4,-1,8,-4,-8,-9,9],[-3,9,-5,-7,-1,9,3],[-6,1,-4,8,10,8,-2]]], dtype = "int32")#candidate|2854|(8, 14, 7)|const|int32
const_2855 = relay.const([[[2,9,1,-8,3,-8,-8],[-2,-7,9,-7,4,-9,9],[-8,3,6,4,7,-4,-1],[-9,3,-8,-4,-8,-7,2],[-9,-5,-6,9,-10,9,6],[-6,-8,-6,6,3,10,-2],[-6,-4,-5,-4,-7,3,7],[-3,-7,-1,-5,6,-2,1],[2,8,8,-5,-3,4,-3],[7,2,6,-10,4,4,7],[1,-8,3,-1,2,-6,6],[-2,8,2,9,9,2,7],[3,4,1,-7,1,-5,-5],[-7,10,1,-1,8,-10,1]],[[8,10,9,-7,9,7,3],[3,5,-10,-9,3,-3,-2],[-7,5,-1,1,10,-2,-10],[-6,-1,3,-1,10,-4,-2],[7,-10,-6,-2,-1,-7,-10],[7,-6,-5,6,-4,10,6],[9,1,-1,10,7,2,-6],[-8,-8,8,-9,-4,8,-1],[1,2,-7,-6,5,6,10],[9,-9,-4,-3,-2,3,7],[-1,2,8,-4,9,3,-7],[-8,-9,5,-6,-4,3,-9],[-1,10,7,-5,-7,9,-8],[2,1,2,-6,7,-8,-9]],[[8,-7,-6,-2,10,9,-6],[-5,-1,10,4,-2,-9,-2],[-2,7,-1,-1,-1,2,-10],[-1,7,3,-3,-10,4,-9],[10,9,-2,-2,-1,10,5],[5,2,6,-4,-9,-1,-5],[-10,-10,-8,4,5,5,-8],[10,-8,3,-3,-9,-7,5],[7,4,6,8,3,6,-10],[6,5,-3,10,-2,4,-9],[2,-2,-6,6,10,-10,8],[3,-6,-5,-4,5,-6,-7],[10,5,2,1,-4,1,-5],[-9,6,10,-2,4,-7,9]],[[8,6,-2,2,-8,3,3],[10,-5,-8,2,5,-5,9],[10,5,-4,9,-4,9,5],[-8,5,4,-8,3,4,-5],[8,3,1,-7,-1,-10,-9],[-10,8,3,-5,-3,3,4],[-3,8,-2,9,-9,8,-5],[8,7,8,-6,-9,2,-6],[10,-2,-7,-4,1,2,-4],[-3,-1,2,-7,-3,5,-5],[-6,2,9,8,-6,4,-8],[9,-1,2,3,7,-6,4],[2,8,10,-3,4,4,-4],[7,-7,7,-1,9,2,-6]],[[8,-10,1,8,6,8,-1],[-7,-3,10,-1,9,3,-5],[-3,3,-3,2,9,-3,1],[4,-6,-10,5,8,-6,-9],[-4,-4,-7,10,10,-2,-4],[-5,-8,9,-9,-2,7,-2],[10,2,8,-3,-4,3,-9],[-4,-3,7,5,-7,5,1],[-3,6,6,7,5,7,5],[5,8,-8,-8,2,3,10],[-1,9,-3,5,-3,3,2],[-1,-3,-2,6,4,5,9],[-7,5,9,-10,-8,-4,-7],[3,9,8,-2,5,-2,-4]],[[-4,6,-2,-7,-6,-3,-4],[-9,6,-4,-6,6,-5,-6],[9,8,2,5,7,-5,3],[-7,-5,-9,8,5,-6,-4],[6,-9,-1,-8,-1,7,7],[10,9,6,-6,6,-8,10],[6,6,5,6,-4,-10,-9],[2,-10,5,-2,7,8,1],[-6,2,6,-5,3,8,-8],[-2,-7,3,9,-9,1,-10],[-9,6,4,1,-6,-5,-8],[6,-3,-10,-5,2,-3,8],[6,4,8,3,8,6,-10],[2,-3,-1,9,1,-8,-1]],[[-3,-6,6,6,-2,6,5],[-5,-2,-3,7,5,9,1],[8,-6,-2,2,4,10,9],[7,9,-10,-9,7,-9,2],[-10,-3,7,-1,-4,5,-3],[6,-4,-7,-5,5,10,-7],[-8,-4,2,-7,9,-7,3],[2,10,7,3,6,-10,9],[7,-8,-5,-3,4,-7,10],[-7,-6,8,-9,10,10,9],[1,2,5,2,6,8,-7],[-2,-9,-9,-10,-10,3,-2],[-8,-5,-10,-6,6,-9,-3],[-2,-2,-7,-3,-5,-5,-1]],[[-7,-3,5,-3,-2,-2,-6],[1,-7,-2,-7,-9,7,-3],[-3,3,1,-6,-4,3,-9],[-6,-7,-8,2,-5,-1,9],[-10,-2,-1,4,1,-8,8],[-10,-8,4,5,-10,-2,-6],[-9,10,-9,4,-7,4,8],[-2,-3,5,-1,7,-3,-1],[-1,-7,-1,-2,9,-4,4],[-4,-10,-1,1,6,-5,5],[7,-2,-4,9,-5,-10,8],[-1,-10,7,1,4,-1,3],[-1,-3,-8,-7,5,-10,8],[7,1,-8,-4,2,-2,9]]], dtype = "int32")#candidate|2855|(8, 14, 7)|const|int32
bop_2856 = relay.left_shift(const_2854.astype('int32'), relay.reshape(const_2855.astype('int32'), relay.shape_of(const_2854))) # shape=(8, 14, 7)
output = relay.Tuple([bop_2856,])
output2 = relay.Tuple([bop_2856,])
func_2866 = relay.Function([], output)
mod['func_2866'] = func_2866
mod = relay.transform.InferType()(mod)
output = func_2866()
func_2867 = relay.Function([], output)
mutated_mod['func_2867'] = func_2867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_2876 = relay.TupleGetItem(func_2866_call(), 0)
call_2877 = relay.TupleGetItem(func_2867_call(), 0)
func_1647_call = mod.get_global_var('func_1647')
func_1651_call = mutated_mod.get_global_var('func_1651')
var_2879 = relay.var("var_2879", dtype = "float64", shape = (90,))#candidate|2879|(90,)|var|float64
var_2880 = relay.var("var_2880", dtype = "bool", shape = (216,))#candidate|2880|(216,)|var|bool
call_2878 = relay.TupleGetItem(func_1647_call(relay.reshape(var_2879.astype('float64'), [9, 5, 2]), relay.reshape(var_2879.astype('float64'), [9, 5, 2]), relay.reshape(var_2880.astype('bool'), [216,]), ), 1)
call_2881 = relay.TupleGetItem(func_1651_call(relay.reshape(var_2879.astype('float64'), [9, 5, 2]), relay.reshape(var_2879.astype('float64'), [9, 5, 2]), relay.reshape(var_2880.astype('bool'), [216,]), ), 1)
func_2721_call = mod.get_global_var('func_2721')
func_2724_call = mutated_mod.get_global_var('func_2724')
const_2890 = relay.const([5,-4,4,-8,6,-6,-10,1,9,5,-3,4,7,-10,-2,1,-10,4,10,10,-5,2,-5,5,7,5,2,-7,-5,-4,-1,4,-3,-7,10,10,-6,-3,5,7,9,-1,-1,2,5,-5,-4,-8,-9,3,-4,9,5,-3,9,4,1,-10,2,-8,-9,-3,-4,-1,6,4,-7,2,-4,-4,-4,-10,-2,5,2,2,10,4,6,7,-9,4,4,8,10,1,-8,6,3,7,9,-9,-7,-3,10,7,-10,5,-8,2,-5,-1,-3,-7,2,-4,-5,10,-5,5,2,5,2,10,5,7,4,-4,-8,-5,-5,3,-9,-2,-5,-2,-6,3,-10,-7,2,4,-5,-4,1,5,-8,8,9,-6,6,5,6,1,8,1,-5,7,5,-2,3,-2,6,-10,9,-1,-3,-6,-4,-3,6,-4,8,10,-5,10,10,10,-2,-2,6,6,10,6,-1,-6,-4,-8,4,-8,10,8,7,-7,6,-10,3,-10,9,6,-9,-7,-5,-5,-4,-9,-8,4,2,-6,1,3,-5,-6,10,-4,-6,-2,-9,9,10,6,4,-7,3,7,3,-7,-4,1,-5,-3,-10,-2,-3,-10,1,-3,8,-3,3,-5,9,-3,5,7,2,10,6,-9,-5,2,-5,-10,4,5,3,-4,-2,-7,4,6,5,-8,-8,-10,5,8,6,4,3,-7,-9,-1,9,-7,-4,-9,-9,-10,3,7,-1,-8,2,6,1,-4,-4,1,-4,8,-3,7,-5,6,-4,-6,9,1,-7,-9,-10,-9,9,-2,10,1,1,5,2,6,8,2,-7,1,9,2,-4,-6,3,-5,9,8,3,-6,9,-2,3,4,-6,5,6,7,-10,-2,2,-8,3,-1,-9,1,8,-5,-5,2,-6,9,6,-2,2,1,-1,-4,-3,1,1,-2,-3,-1,-5,-4,-2,3,-10,4,8,7,-4,-6,-8,-3,-8,10,-1,2,4,9,8,5,6,1,7,-5,-8,10,-7,5,-7,9,-5,-5,6,6,5,-3,3,7,1,-8,5,7,10,-9,6,-4,8,2,3,-9,1,1,7,1,4,-9,9,2,7,-4,-9,3,-8,-1,-5,1,-2,8,-4,9,10,6,-3,9,-8,-2,1,-4,4,-2,-8,3,-7,9,-9,7,6,9,10,1,2,8,-3,-4,10,4,-9,7,-7,7,-7,-7,8,4,7,9,-9,3,-9,-6,5,6,8,-1,-4,-3,3,-5,10,-10,-5,6,-3,-5,-8,-1,3,-8,-5,-8,-7,9,2,10,1,9,-8,1,4,4,-9,6,4,-4,4,5,2,-1,8,-8,-3,7,2,3,-4,-7,-1,6,8,4,4,3,-7,-10,-8,-6,-5,-4,-10,2,-3,-8,3,-2,8,1,9,-7,10,1,-8,-1,-1,2,2,-7,5,1,-3,-9,3,2,5,8,1,-5,8,3,-1,-3,9,9,-7,-1,5,1,1,-10,7,4,-9,6,-5,9,2,-10,-1,-2,-9,-1,3,10,9,2,10,-1,-5,10,-6,7,-2,8,5,-4,-4,-9,-8,3,-1,-3,-3,3,3,-9,2,-6,2,-10,5,3,10,6,-3,7,-6,-6,-5,8,-10,-9,-4,9,-1,4,2,3,1,1,-10,5,-9,6,8,3,2,2,-9,1,1,-3,-5,6,6,10,-8,-2,8,2,-2,5,9,10,-10,5,8,-4,-4,1,-10,8,5,-4,7,-8,10,-5,-3,-6,-7,4,-9,-8,-1,-3,-9,-8,10,-9,5,-10,-1,6,1,8,-3,1,3,4,-10,6,9,-6,-3,8,2,-4,4,-10,-2,-10,3,4,5,-1,-7,8,10,-5,-1,-2,2,8,8,10,6,-4,5,6,-7,7,-5,-8,-9,7,-5,-2,5,-10,8,2,1,-5,-3,6,-10,-2,6,-10,-2,-4,4,-1,-6,1,-2,-7,8,-9,5,-10,8,1,-3,-10,8,1,2,2,-4,1,7,-1,4,-5,-7,3,1,3,7,-1,9,-8,6,10,-4,-8,-1,-3,10,3,4,-7,1,9,5,-2,1,-7,9,-7,-8,-3,5,-3,5,4,-1,-6,-3,10,-4,2,2,2,-5,-4,5,2,-3,-5,-1,10,2,-6,-1,-2,-9,-10,-2,-2,-3,-9,-4,-8,-8,-7,-4,2,-3,2,5,6,-6,6,-1,6,5,-10,-8,7,-1,-6,-3,4,9,9,10,9,-4,-6,1,6,-9,6,5,5,10,-3,-2,-9,5,-4,-3,-2,7,-9,2,-8,-2,-10,10,4,-9,-2,-6,-3,-7,5,-1,5,5,-8,-9,-7,1,-1,3,8,4,4,-9,2,-3,5,4,-1,4,-5,6,-8,-7,5,-4,-3,-4,-8,-3,10,9,-9,-5,-1,2,6,8,-4,-10,-7,3,-3], dtype = "int32")#candidate|2890|(910,)|const|int32
call_2889 = relay.TupleGetItem(func_2721_call(relay.reshape(const_2890.astype('int32'), [5, 13, 14])), 1)
call_2891 = relay.TupleGetItem(func_2724_call(relay.reshape(const_2890.astype('int32'), [5, 13, 14])), 1)
bop_2901 = relay.equal(call_2878.astype('bool'), relay.reshape(var_2880.astype('bool'), relay.shape_of(call_2878))) # shape=(3, 9, 8)
bop_2904 = relay.equal(call_2881.astype('bool'), relay.reshape(var_2880.astype('bool'), relay.shape_of(call_2881))) # shape=(3, 9, 8)
func_2754_call = mod.get_global_var('func_2754')
func_2756_call = mutated_mod.get_global_var('func_2756')
call_2905 = func_2754_call()
call_2906 = func_2754_call()
output = relay.Tuple([call_2876,var_2879,call_2889,const_2890,bop_2901,call_2905,])
output2 = relay.Tuple([call_2877,var_2879,call_2891,const_2890,bop_2904,call_2906,])
func_2911 = relay.Function([var_2879,var_2880,], output)
mod['func_2911'] = func_2911
mod = relay.transform.InferType()(mod)
var_2912 = relay.var("var_2912", dtype = "float64", shape = (90,))#candidate|2912|(90,)|var|float64
var_2913 = relay.var("var_2913", dtype = "bool", shape = (216,))#candidate|2913|(216,)|var|bool
output = func_2911(var_2912,var_2913,)
func_2914 = relay.Function([var_2912,var_2913,], output)
mutated_mod['func_2914'] = func_2914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2754_call = mod.get_global_var('func_2754')
func_2756_call = mutated_mod.get_global_var('func_2756')
call_2925 = func_2754_call()
call_2926 = func_2754_call()
output = relay.Tuple([call_2925,])
output2 = relay.Tuple([call_2926,])
func_2930 = relay.Function([], output)
mod['func_2930'] = func_2930
mod = relay.transform.InferType()(mod)
output = func_2930()
func_2931 = relay.Function([], output)
mutated_mod['func_2931'] = func_2931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_2932 = relay.TupleGetItem(func_2930_call(), 0)
call_2933 = relay.TupleGetItem(func_2931_call(), 0)
func_2798_call = mod.get_global_var('func_2798')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_2940 = relay.TupleGetItem(func_2798_call(), 0)
call_2941 = relay.TupleGetItem(func_2799_call(), 0)
func_2911_call = mod.get_global_var('func_2911')
func_2914_call = mutated_mod.get_global_var('func_2914')
var_2945 = relay.var("var_2945", dtype = "float64", shape = (90,))#candidate|2945|(90,)|var|float64
var_2946 = relay.var("var_2946", dtype = "bool", shape = (108, 2))#candidate|2946|(108, 2)|var|bool
call_2944 = relay.TupleGetItem(func_2911_call(relay.reshape(var_2945.astype('float64'), [90,]), relay.reshape(var_2946.astype('bool'), [216,]), ), 2)
call_2947 = relay.TupleGetItem(func_2914_call(relay.reshape(var_2945.astype('float64'), [90,]), relay.reshape(var_2946.astype('bool'), [216,]), ), 2)
func_2911_call = mod.get_global_var('func_2911')
func_2914_call = mutated_mod.get_global_var('func_2914')
call_2954 = relay.TupleGetItem(func_2911_call(relay.reshape(var_2945.astype('float64'), [90,]), relay.reshape(var_2946.astype('bool'), [216,]), ), 3)
call_2955 = relay.TupleGetItem(func_2914_call(relay.reshape(var_2945.astype('float64'), [90,]), relay.reshape(var_2946.astype('bool'), [216,]), ), 3)
var_2957 = relay.var("var_2957", dtype = "int32", shape = (910,))#candidate|2957|(910,)|var|int32
bop_2958 = relay.not_equal(call_2954.astype('bool'), relay.reshape(var_2957.astype('bool'), relay.shape_of(call_2954))) # shape=(910,)
bop_2961 = relay.not_equal(call_2955.astype('bool'), relay.reshape(var_2957.astype('bool'), relay.shape_of(call_2955))) # shape=(910,)
func_767_call = mod.get_global_var('func_767')
func_771_call = mutated_mod.get_global_var('func_771')
const_2975 = relay.const([8,9,1,5,8,9,3,-7,2,6,-7,-9,-3,-7,-2,8,-4,-2,-8,-8,-2,-6,-6,7,-8,-10,-9,-3,3,9,8,7,-6,-8,5,-3,-7,-2,-3,-9,-2,-5,9,-3,-7], dtype = "int32")#candidate|2975|(45,)|const|int32
var_2976 = relay.var("var_2976", dtype = "int32", shape = (180,))#candidate|2976|(180,)|var|int32
call_2974 = relay.TupleGetItem(func_767_call(relay.reshape(const_2975.astype('int32'), [1, 5, 9]), relay.reshape(var_2976.astype('int32'), [4, 5, 9]), ), 0)
call_2977 = relay.TupleGetItem(func_771_call(relay.reshape(const_2975.astype('int32'), [1, 5, 9]), relay.reshape(var_2976.astype('int32'), [4, 5, 9]), ), 0)
uop_2994 = relay.atan(var_2946.astype('float64')) # shape=(108, 2)
output = relay.Tuple([call_2932,call_2940,call_2944,var_2945,bop_2958,call_2974,const_2975,var_2976,uop_2994,])
output2 = relay.Tuple([call_2933,call_2941,call_2947,var_2945,bop_2961,call_2977,const_2975,var_2976,uop_2994,])
func_2999 = relay.Function([var_2945,var_2946,var_2957,var_2976,], output)
mod['func_2999'] = func_2999
mod = relay.transform.InferType()(mod)
mutated_mod['func_2999'] = func_2999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2999_call = mutated_mod.get_global_var('func_2999')
var_3001 = relay.var("var_3001", dtype = "float64", shape = (90,))#candidate|3001|(90,)|var|float64
var_3002 = relay.var("var_3002", dtype = "bool", shape = (108, 2))#candidate|3002|(108, 2)|var|bool
var_3003 = relay.var("var_3003", dtype = "int32", shape = (910,))#candidate|3003|(910,)|var|int32
var_3004 = relay.var("var_3004", dtype = "int32", shape = (180,))#candidate|3004|(180,)|var|int32
call_3000 = func_2999_call(var_3001,var_3002,var_3003,var_3004,)
output = call_3000
func_3005 = relay.Function([var_3001,var_3002,var_3003,var_3004,], output)
mutated_mod['func_3005'] = func_3005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_3035 = relay.TupleGetItem(func_2866_call(), 0)
call_3036 = relay.TupleGetItem(func_2867_call(), 0)
output = call_3035
output2 = call_3036
func_3065 = relay.Function([], output)
mod['func_3065'] = func_3065
mod = relay.transform.InferType()(mod)
mutated_mod['func_3065'] = func_3065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mutated_mod.get_global_var('func_3065')
call_3066 = func_3065_call()
output = call_3066
func_3067 = relay.Function([], output)
mutated_mod['func_3067'] = func_3067
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3089 = relay.var("var_3089", dtype = "float64", shape = (6, 3, 9))#candidate|3089|(6, 3, 9)|var|float64
uop_3090 = relay.sigmoid(var_3089.astype('float64')) # shape=(6, 3, 9)
func_2798_call = mod.get_global_var('func_2798')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_3097 = relay.TupleGetItem(func_2798_call(), 1)
call_3098 = relay.TupleGetItem(func_2799_call(), 1)
uop_3099 = relay.sinh(call_3097.astype('float64')) # shape=(14, 1, 14)
uop_3101 = relay.sinh(call_3098.astype('float64')) # shape=(14, 1, 14)
output = relay.Tuple([uop_3090,uop_3099,])
output2 = relay.Tuple([uop_3090,uop_3101,])
func_3103 = relay.Function([var_3089,], output)
mod['func_3103'] = func_3103
mod = relay.transform.InferType()(mod)
var_3104 = relay.var("var_3104", dtype = "float64", shape = (6, 3, 9))#candidate|3104|(6, 3, 9)|var|float64
output = func_3103(var_3104)
func_3105 = relay.Function([var_3104], output)
mutated_mod['func_3105'] = func_3105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mod.get_global_var('func_3065')
func_3067_call = mutated_mod.get_global_var('func_3067')
call_3203 = func_3065_call()
call_3204 = func_3065_call()
func_1647_call = mod.get_global_var('func_1647')
func_1651_call = mutated_mod.get_global_var('func_1651')
var_3222 = relay.var("var_3222", dtype = "float64", shape = (90,))#candidate|3222|(90,)|var|float64
const_3223 = relay.const([True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,False,True], dtype = "bool")#candidate|3223|(216,)|const|bool
call_3221 = relay.TupleGetItem(func_1647_call(relay.reshape(var_3222.astype('float64'), [9, 5, 2]), relay.reshape(var_3222.astype('float64'), [9, 5, 2]), relay.reshape(const_3223.astype('bool'), [216,]), ), 0)
call_3224 = relay.TupleGetItem(func_1651_call(relay.reshape(var_3222.astype('float64'), [9, 5, 2]), relay.reshape(var_3222.astype('float64'), [9, 5, 2]), relay.reshape(const_3223.astype('bool'), [216,]), ), 0)
func_2999_call = mod.get_global_var('func_2999')
func_3005_call = mutated_mod.get_global_var('func_3005')
const_3231 = relay.const([-6,-4,-1,10,5,1,4,4,6,4,3,7,-4,-1,-5,-9,-1,-8,3,-8,-4,8,-9,-5,4,-5,7,9,6,-10,-8,2,1,4,5,-4,-10,-7,5,-4,-3,-7,10,4,8,6,2,-5,-7,-8,-10,-1,7,1,-2,-10,-3,-7,-5,-10,-4,6,4,8,-10,-6,-1,3,7,-9,-9,5,-7,5,-3,2,-3,3,2,1,-10,-4,-5,10,-1,2,7,9,2,-4,1,2,6,1,9,-2,10,1,-3,7,9,1,9,-9,-8,-5,1,-4,3,7,-9,2,-4,-3,5,2,-1,9,5,-10,1,3,-3,10,-2,9,-7,9,7,10,-3,-3,7,6,-9,4,-2,-3,4,2,-10,5,5,1,-7,-1,3,-5,-5,4,-7,-6,-7,-5,-2,-5,1,2,-4,-5,3,-1,1,9,-9,2,1,-7,6,-7,1,1,-4,8,-3,10,3,2,-9,2,4,-4,-3,-3,-2,-5,4,7,-8,-5,9,9,-7,8,2,4,3,2,6,4,6,1,7,10,-2,-10,-10,-5,-10,5,-2,-9,-6,2,6,9,9,-4,7,-4,8,-2,-3,-7,1,-4,-2,9,-3,9,-8,3,-8,6,10,-4,5,7,4,-8,8,9,4,8,-10,-9,3,8,9,-7,-3,7,9,-6,2,10,-6,1,-7,-1,6,-5,-2,-10,-8,-1,-8,-1,-6,9,-10,7,-8,-8,-7,-9,-9,-2,1,5,9,-10,-6,-5,7,10,5,-3,-6,-5,2,-6,2,5,9,3,-5,6,-4,-4,5,10,1,-2,-6,2,4,-2,-7,2,-4,4,9,-3,-1,6,10,7,-9,2,7,-5,3,9,-4,-6,7,-10,-9,9,-9,-7,9,4,-2,-5,-2,4,-10,5,-6,-4,10,7,-8,-1,-1,8,2,-10,-8,-5,-7,-6,-4,1,-4,10,1,-5,-6,-6,5,-7,-5,1,-1,-4,7,-5,2,8,-3,4,-8,2,7,10,-1,-9,3,-10,6,3,5,-4,-4,-7,-3,-2,9,-6,2,-8,-3,1,-7,-2,-6,-8,-3,-10,-5,5,-5,2,10,2,-3,7,5,6,9,-5,-3,6,5,4,-10,-9,-5,-2,-8,9,3,1,-3,2,-5,7,-1,-3,-8,8,5,6,10,-8,-10,-4,-2,3,-2,-9,3,4,-10,2,-5,9,-10,3,-3,-10,6,8,-9,-5,-9,7,-10,-7,9,10,10,5,4,-1,6,2,3,2,-4,-2,-9,4,-1,2,2,3,1,3,-5,4,4,-3,-7,-9,-2,-1,-10,-10,8,1,4,-2,-4,-10,-9,-10,10,2,-10,8,3,-1,-6,6,-5,-4,2,3,2,7,-8,6,2,-7,8,4,-7,-6,8,-9,-8,-1,10,8,-7,-5,4,5,9,10,-9,1,-9,-7,9,-1,8,7,8,-1,-2,2,-8,-2,10,4,-6,3,2,-2,7,-7,-7,-4,4,10,4,2,2,8,-7,1,-9,-9,-8,3,-6,2,-9,-8,6,8,1,-1,-3,-5,3,-4,-4,-5,-5,10,3,3,-10,2,1,3,10,-5,3,5,-9,8,1,-6,4,-8,-7,6,3,3,-7,-6,-2,-2,-4,-1,-6,-6,2,3,-7,-10,1,-2,-3,-8,3,1,-8,10,-8,5,-8,10,3,4,6,4,10,-4,3,7,-10,1,9,-8,-10,2,-1,6,10,6,5,-5,-8,-10,-3,-6,5,-8,7,-3,8,5,-10,7,-2,-5,-3,-2,9,9,-10,6,-2,-10,-2,-4,-10,4,-9,-9,-2,-9,-5,5,4,-8,8,-8,8,-9,-10,-1,-3,10,5,-4,4,-3,4,-2,1,1,-2,2,-8,10,-4,-10,-7,-9,-10,1,-6,-2,4,1,4,7,-2,7,9,-9,8,10,-10,10,-3,3,-7,2,-10,7,6,9,-2,-9,4,2,7,-9,-2,-6,-10,-6,5,8,-2,9,-6,7,5,-9,-4,-2,4,8,10,10,-5,9,-6,-5,-2,6,5,8,-7,-10,7,-2,1,8,3,1,6,-10,-7,-9,-1,8,8,5,-10,-10,5,9,-1,-9,-7,-4,10,-3,9,7,1,-6,-9,6,-6,-10,8,8,6,-6,8,6,-6,-7,5,4,9,-4,-3,-10,9,-9,-9,6,4,10,4,2,-5,4,4,5,-10,-4,1,1,5,-7,-8,-2,7,-6,8,-2,8,-4,-7,-8,7,-1,9,6,-1,8,6,-4,2,7,-10,2,6,-2,2,-10,-3,7,3,6,6,7,-4,8,-1,-3,-3,-8,-8,4,10,10,6,-7,-1,-7,7,-3,-3,6,-6,-4,3,-10,10,-4,9,-6,-1,4,-8,-1,4,-5,-4,2,9,1,-6,4,6,-10,1,-7,-1,-4,-3,3,8,-6], dtype = "int32")#candidate|3231|(910,)|const|int32
var_3232 = relay.var("var_3232", dtype = "int32", shape = (180,))#candidate|3232|(180,)|var|int32
call_3230 = relay.TupleGetItem(func_2999_call(relay.reshape(call_3221.astype('float64'), [90,]), relay.reshape(const_3223.astype('bool'), [108, 2]), relay.reshape(const_3231.astype('int32'), [910,]), relay.reshape(var_3232.astype('int32'), [180,]), ), 2)
call_3233 = relay.TupleGetItem(func_3005_call(relay.reshape(call_3221.astype('float64'), [90,]), relay.reshape(const_3223.astype('bool'), [108, 2]), relay.reshape(const_3231.astype('int32'), [910,]), relay.reshape(var_3232.astype('int32'), [180,]), ), 2)
output = relay.Tuple([call_3203,call_3221,var_3222,const_3223,call_3230,const_3231,var_3232,])
output2 = relay.Tuple([call_3204,call_3224,var_3222,const_3223,call_3233,const_3231,var_3232,])
func_3267 = relay.Function([var_3222,var_3232,], output)
mod['func_3267'] = func_3267
mod = relay.transform.InferType()(mod)
var_3268 = relay.var("var_3268", dtype = "float64", shape = (90,))#candidate|3268|(90,)|var|float64
var_3269 = relay.var("var_3269", dtype = "int32", shape = (180,))#candidate|3269|(180,)|var|int32
output = func_3267(var_3268,var_3269,)
func_3270 = relay.Function([var_3268,var_3269,], output)
mutated_mod['func_3270'] = func_3270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_3311 = relay.TupleGetItem(func_2930_call(), 0)
call_3312 = relay.TupleGetItem(func_2931_call(), 0)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_3315 = relay.TupleGetItem(func_2930_call(), 0)
call_3316 = relay.TupleGetItem(func_2931_call(), 0)
func_2999_call = mod.get_global_var('func_2999')
func_3005_call = mutated_mod.get_global_var('func_3005')
var_3326 = relay.var("var_3326", dtype = "float64", shape = (90,))#candidate|3326|(90,)|var|float64
const_3327 = relay.const([False,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True], dtype = "bool")#candidate|3327|(216,)|const|bool
const_3328 = relay.const([4,9,9,-7,-1,-1,-10,1,3,1,5,-9,-6,-2,-10,4,-10,-10,-6,2,-3,6,-1,7,2,5,-8,6,5,-5,-3,-9,-3,4,5,5,-8,-9,9,-2,6,2,-10,-9,6,-10,-4,6,7,5,3,-9,-4,-9,-8,5,6,7,-6,1,-2,-5,-9,2,-8,-9,8,3,8,-4,-2,-2,8,6,-8,8,-9,6,1,-3,4,1,10,5,-5,-6,-10,5,8,10,8,5,10,-5,-9,9,10,9,-1,8,1,-2,2,9,-9,-9,-8,4,6,-8,-8,2,4,-8,4,-2,1,8,-1,7,-5,-7,-1,-10,10,3,2,8,7,-4,3,5,-1,-1,-9,2,-5,6,10,4,-3,-2,4,-2,5,1,-3,-5,-1,-7,-7,4,-8,9,-6,9,-3,4,-10,-8,4,6,8,-4,-8,-9,9,-8,-4,6,1,9,6,-1,2,3,1,-7,-1,-9,-1,-5,-4,7,1,7,-9,-7,-4,3,-10,-3,-8,-1,1,-1,2,1,10,-3,-1,4,-1,-7,9,-10,-10,9,3,-10,-4,7,6,4,-7,-8,9,10,-5,4,9,-3,7,9,-6,6,-10,7,-2,4,6,-10,8,-7,-7,8,-3,6,-5,-1,6,10,-8,-1,-8,10,1,-10,-9,9,-8,-5,8,-10,-8,5,-6,-9,-3,-9,-7,6,-10,-6,-3,-7,4,1,-3,6,-2,5,-7,6,-7,3,-3,-2,3,-4,-3,-9,-4,10,1,-9,6,-5,-10,-4,-6,-1,-6,-4,10,-7,-10,1,-7,1,6,3,6,8,-8,1,1,-5,-4,6,-6,1,1,9,-5,-6,-10,7,-4,10,-9,-6,-2,7,-9,-9,8,-2,-4,-7,-9,9,9,-5,-1,6,7,-8,10,-4,10,3,-5,-9,6,-5,-8,-6,10,-3,-8,1,-9,-4,-6,-10,-6,-6,-8,10,-10,10,-1,6,-8,2,-6,-3,4,3,-8,6,-8,4,5,1,-9,3,7,-1,8,1,8,8,1,-2,6,4,-8,9,10,-1,1,1,5,1,7,7,7,-7,-9,-9,7,-9,2,2,-10,-3,9,6,-5,-1,-10,8,-6,-8,-4,-1,10,7,2,6,-2,-10,2,-9,5,-1,-8,4,4,10,1,-2,-3,-5,-6,-6,1,-1,2,-1,-8,1,1,-10,7,4,3,-9,5,-3,6,-1,-5,-9,2,3,-2,8,10,-8,-1,-7,8,-3,1,-4,-5,-3,7,7,-3,1,-5,-7,-10,3,7,6,-7,8,4,6,-7,10,-2,3,-7,1,7,4,4,1,-9,-9,-3,-4,-7,6,1,7,-5,9,9,2,9,-5,5,-4,-2,-1,-8,-2,7,-10,-6,-2,-1,2,2,-8,-2,-3,1,-3,10,8,9,4,9,-4,3,7,10,6,3,-4,6,-4,-5,-10,9,3,-5,3,3,1,7,1,-7,-9,8,-5,-1,3,-6,-10,-8,-2,-8,-1,4,8,-1,-9,4,9,3,8,5,-9,4,-5,-2,7,3,2,9,-1,7,-9,1,-2,-5,8,4,2,-9,-2,5,-3,-9,-8,-3,1,10,-10,1,5,4,8,5,6,9,6,-9,-4,2,-9,2,4,1,5,5,7,-7,7,-5,7,1,7,10,10,-3,8,10,-7,5,-2,4,-10,-4,-3,10,-2,1,4,-1,5,5,9,-5,-6,-10,1,-8,5,9,-9,-5,-3,10,-10,-2,-5,8,4,-10,-4,-9,-4,-9,8,-6,1,8,8,1,-1,4,-2,9,6,6,-2,8,-1,5,-6,-6,2,9,4,-9,5,-10,-6,2,-8,5,-5,-6,-9,-6,1,10,-6,5,-10,-4,8,3,2,-9,6,-8,6,-7,-4,9,-5,-9,9,2,8,6,1,-1,7,-1,3,-5,-3,3,-5,3,1,-2,7,10,1,1,-5,5,4,6,5,-8,6,-8,-4,-3,-4,-5,-3,6,3,6,-4,2,6,5,3,-2,7,-2,-10,5,-1,4,-9,8,2,2,8,3,-3,-7,-4,-5,-10,9,1,-3,8,8,10,7,-3,-7,2,5,8,4,-5,-10,-8,-5,5,-5,7,-8,1,-10,-6,-7,5,-6,6,-5,-10,5,4,-9,8,-1,9,-4,7,-5,1,1,-4,8,-8,-2,-8,8,-7,-10,-3,9,-2,-2,-7,4,-1,-3,-2,8,4,10,-6,-3,-7,5,-7,4,7,10,5,1,9,-2,5,-10,-7,-2,-1,6,-9,2,5,-7,1,8,1,1,-3,10,-2,-6,3,4,2,-3,-8,9,8,8,1,-7,-5,-2,-3,6,-3,4,10,-9,5,5,5,-9,-8,-4,2,1,2,-6,6,-8,-4,-4,-10,7,6,-1,4,6,6,10,3,-7,-7,-8,5,-3,-10], dtype = "int32")#candidate|3328|(910,)|const|int32
const_3329 = relay.const([1,-10,-2,8,10,7,-3,-7,-10,-1,-7,3,9,-9,2,-1,-2,8,1,-9,7,8,2,-10,10,-3,-2,-7,10,-10,-9,-3,-4,-4,-6,-6,6,-7,-9,-5,8,-4,-4,-3,-8,-7,8,8,3,-4,5,-4,-4,-1,9,2,2,10,-8,2,-10,4,1,7,-6,-4,1,-9,-10,9,-6,9,-8,6,5,-3,5,2,-9,-1,-2,-5,-3,-9,7,-4,-9,-1,-3,-3,4,-1,1,-6,-2,9,-10,-6,-9,7,3,8,-6,8,-5,6,-7,8,-10,-2,1,-4,-4,-5,-5,10,6,1,9,9,-10,-3,2,7,-8,-4,-8,2,-1,8,9,-8,-8,-9,8,-10,3,-7,9,-8,-1,-7,-3,3,-4,-3,-9,-10,-8,3,-6,-6,8,-7,7,5,-10,-7,1,-8,-8,-10,2,5,10,7,1,-9,7,10,-3,-2,-7,-7,-8,3,-8,5,6,9], dtype = "int32")#candidate|3329|(180,)|const|int32
call_3325 = relay.TupleGetItem(func_2999_call(relay.reshape(var_3326.astype('float64'), [90,]), relay.reshape(const_3327.astype('bool'), [108, 2]), relay.reshape(const_3328.astype('int32'), [910,]), relay.reshape(const_3329.astype('int32'), [180,]), ), 8)
call_3330 = relay.TupleGetItem(func_3005_call(relay.reshape(var_3326.astype('float64'), [90,]), relay.reshape(const_3327.astype('bool'), [108, 2]), relay.reshape(const_3328.astype('int32'), [910,]), relay.reshape(const_3329.astype('int32'), [180,]), ), 8)
output = relay.Tuple([call_3311,call_3315,call_3325,var_3326,const_3327,const_3328,const_3329,])
output2 = relay.Tuple([call_3312,call_3316,call_3330,var_3326,const_3327,const_3328,const_3329,])
func_3333 = relay.Function([var_3326,], output)
mod['func_3333'] = func_3333
mod = relay.transform.InferType()(mod)
mutated_mod['func_3333'] = func_3333
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3334 = relay.var("var_3334", dtype = "float64", shape = (90,))#candidate|3334|(90,)|var|float64
func_3333_call = mutated_mod.get_global_var('func_3333')
call_3335 = func_3333_call(var_3334)
output = call_3335
func_3336 = relay.Function([var_3334], output)
mutated_mod['func_3336'] = func_3336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_3353 = relay.TupleGetItem(func_2866_call(), 0)
call_3354 = relay.TupleGetItem(func_2867_call(), 0)
func_2206_call = mod.get_global_var('func_2206')
func_2209_call = mutated_mod.get_global_var('func_2209')
var_3363 = relay.var("var_3363", dtype = "float32", shape = (1680,))#candidate|3363|(1680,)|var|float32
var_3364 = relay.var("var_3364", dtype = "float64", shape = (720,))#candidate|3364|(720,)|var|float64
call_3362 = relay.TupleGetItem(func_2206_call(relay.reshape(var_3363.astype('float32'), [8, 14, 15]), relay.reshape(var_3364.astype('float64'), [720,]), ), 2)
call_3365 = relay.TupleGetItem(func_2209_call(relay.reshape(var_3363.astype('float32'), [8, 14, 15]), relay.reshape(var_3364.astype('float64'), [720,]), ), 2)
func_2798_call = mod.get_global_var('func_2798')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_3386 = relay.TupleGetItem(func_2798_call(), 0)
call_3387 = relay.TupleGetItem(func_2799_call(), 0)
output = relay.Tuple([call_3353,call_3362,var_3363,var_3364,call_3386,])
output2 = relay.Tuple([call_3354,call_3365,var_3363,var_3364,call_3387,])
func_3397 = relay.Function([var_3363,var_3364,], output)
mod['func_3397'] = func_3397
mod = relay.transform.InferType()(mod)
mutated_mod['func_3397'] = func_3397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3397_call = mutated_mod.get_global_var('func_3397')
var_3399 = relay.var("var_3399", dtype = "float32", shape = (1680,))#candidate|3399|(1680,)|var|float32
var_3400 = relay.var("var_3400", dtype = "float64", shape = (720,))#candidate|3400|(720,)|var|float64
call_3398 = func_3397_call(var_3399,var_3400,)
output = call_3398
func_3401 = relay.Function([var_3399,var_3400,], output)
mutated_mod['func_3401'] = func_3401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_3420 = relay.TupleGetItem(func_2930_call(), 0)
call_3421 = relay.TupleGetItem(func_2931_call(), 0)
output = relay.Tuple([call_3420,])
output2 = relay.Tuple([call_3421,])
func_3423 = relay.Function([], output)
mod['func_3423'] = func_3423
mod = relay.transform.InferType()(mod)
output = func_3423()
func_3424 = relay.Function([], output)
mutated_mod['func_3424'] = func_3424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_3562 = relay.TupleGetItem(func_2930_call(), 0)
call_3563 = relay.TupleGetItem(func_2931_call(), 0)
func_3267_call = mod.get_global_var('func_3267')
func_3270_call = mutated_mod.get_global_var('func_3270')
var_3587 = relay.var("var_3587", dtype = "float64", shape = (15, 6))#candidate|3587|(15, 6)|var|float64
const_3588 = relay.const([3,-5,-3,-10,-1,-10,-8,2,1,-1,8,-2,-10,-7,5,-6,8,-1,4,-1,10,-7,-10,8,-9,-8,2,4,-9,10,-1,-4,10,9,7,-10,-3,7,-4,-7,-1,-1,-5,5,-4,-5,3,-5,5,8,5,-2,7,-4,-2,5,3,8,-1,-1,-10,-1,6,-8,9,6,8,-4,7,7,8,5,-9,1,-6,4,-9,-10,10,-9,-8,3,-2,4,-7,-9,4,-10,6,3,-4,-9,2,1,1,-1,4,6,10,-7,10,4,1,9,7,-1,-8,5,10,-4,-5,-2,8,9,8,7,-6,-4,-6,4,4,4,6,6,7,-8,2,5,8,7,2,7,-6,-4,-3,-4,4,3,-9,-5,-6,1,3,-9,8,10,-2,7,-8,-8,9,-10,-4,-2,-9,-9,4,-4,-6,9,-8,3,3,-8,10,2,10,4,-4,-6,5,-1,-7,-5,7,-6,-2,5,-10,-6], dtype = "int32")#candidate|3588|(180,)|const|int32
call_3586 = relay.TupleGetItem(func_3267_call(relay.reshape(var_3587.astype('float64'), [90,]), relay.reshape(const_3588.astype('int32'), [180,]), ), 3)
call_3589 = relay.TupleGetItem(func_3270_call(relay.reshape(var_3587.astype('float64'), [90,]), relay.reshape(const_3588.astype('int32'), [180,]), ), 3)
var_3603 = relay.var("var_3603", dtype = "float64", shape = (14, 1, 14))#candidate|3603|(14, 1, 14)|var|float64
bop_3604 = relay.less(call_3562.astype('bool'), relay.reshape(var_3603.astype('bool'), relay.shape_of(call_3562))) # shape=(14, 1, 14)
bop_3607 = relay.less(call_3563.astype('bool'), relay.reshape(var_3603.astype('bool'), relay.shape_of(call_3563))) # shape=(14, 1, 14)
func_1912_call = mod.get_global_var('func_1912')
func_1915_call = mutated_mod.get_global_var('func_1915')
const_3613 = relay.const([-1.959216,5.269023,-4.706581,-6.568983,-4.866768,4.317298,-8.666477,-3.653322,6.391279,-0.130092,-4.637637,2.103917,-4.903120,-5.289234,0.538708,-5.898939,6.299899,5.603491,3.591586,1.144212,-5.216899,-1.981235,6.991790,7.761819,-4.764033,-7.526409,-6.435008,-9.030343,2.546827,-0.839007,-4.369626,-5.712672,-5.769135,-0.547804,-3.712303,9.772591,-3.828321,2.640562,-3.720678,-1.233838,-6.297294,-3.962237,3.242945,7.914959,4.704249,5.018545,-7.318193,-8.375455,5.926891,6.589229,-8.678815,5.340811,-3.414556,-8.619012,5.679838,2.537912,-2.707209,-7.745493,-9.153484,-0.293011,7.057376,-2.319964,-9.047314,-7.028252,1.234316,1.577712,-5.150990,-0.255335,6.750969,0.298234,1.175072,-8.236386,-5.399226,9.423234,-7.379317,7.409893,-0.959089,-0.741477,-6.756503,-1.092042,-1.670969,9.121956,-2.623379,8.089793,8.918516,-3.090713,-7.856983,-7.822797,9.023452,6.155002,8.463839,4.875795,-7.296500,-5.153435,-2.090993,-2.879240,-0.282705,2.637974,9.857065,-4.749019,-8.768216,-1.019049,3.843191,6.596827,-1.670210,7.420936,8.154662,0.995864,-5.190178,-5.772896,0.987947,5.437926,0.436848,-0.271717,2.726564,3.383262,-8.408426,-4.993512,-8.636447,-5.381559,6.286972,-6.720148,3.367396,-7.120212,-6.541797,-1.931853,-7.612974,9.103988,8.544753,-7.505553,2.283120,-7.059145,7.880718,9.006456,-2.518091,2.273958,1.654024,7.260427,6.094685,-9.382704,-6.220437,2.985797,-3.184941,-9.937012,0.601186,1.629590,-1.976245,-2.976569,-3.715199,7.970709,0.575823,-7.178767,6.555286,7.411911,-8.643045,-4.419583,5.256149,6.680003,-5.130365,8.807331,-9.396182,-7.584316,-1.431816,0.176139,6.032305,9.569972,6.483998,5.081411,3.168763,3.797883,1.676003,4.851389,-7.306450,-3.781807,-4.950835,-2.627172,-0.209552,-4.232827,5.099333,-5.965880,-8.923719,4.237911,1.797559,-2.586296,-7.177119,-1.175606,5.066901,-8.852897,-0.484019,7.026056,-9.660630,-1.491030,-8.016159,1.295275,-1.640334,-7.992989,2.581089,-4.022351,8.691686,-4.207021,-6.099390,3.280415,-3.149148,3.642351,-2.940531,1.797462,-7.403292,-3.957875,-2.337267,-8.573938,8.401670,-2.293242,1.624912,0.254514,3.855641,-6.125033,5.151253,-8.589419,8.922997,-1.031856,-8.277870,-1.562351,1.091824,4.280650,-8.893836,-4.575272,3.428558,-7.694206,0.002601,0.546432,6.078154,3.905574,1.738756,-4.929493,0.558965,-0.806084,2.580832,8.259244,4.008825,-5.951391,-8.450189,9.017584,4.973336,-4.960290,-7.708038,-6.362310,7.673889,-2.876667,7.525931,6.809876,7.438171,-3.893510,-9.075192,-1.084083,-2.675936,9.575856,3.432024,-5.816857,2.281634,-0.876576,-7.214765,8.562379,-1.619709,-6.046106,6.822643,-8.824892,-5.371431,2.326271,-0.206632,-4.091264,-8.720482,-2.749759,6.575515,9.971936,2.703267,-5.649472,-1.767580,-7.228051,0.502137,-7.706485,-8.988942,0.415329,2.450376,-8.838183,-6.017243,-1.079153,-1.540201,7.559878,-9.704881,-6.665805,-6.778697,9.467713,3.018837,6.823085,3.938173,4.558123,-3.874919,-1.195618,4.752285,-5.642973,0.381513,-2.359323,9.393924,5.023670,-7.867818,5.245240,-4.290393,6.917549,-5.469321,-6.341314,-4.116933,-9.550825,2.313892,-9.943592,6.729148,-4.617654,-8.230282,-9.074946,-6.503857,4.454753,-6.771894,9.215931,2.647212,-1.518854,2.695738,7.177843,-4.906134,1.599549,-8.290851,-0.359379,-0.858062,9.060807,9.628905,-6.414180,7.815761,6.892700,-8.010671,3.183459,6.119525,-9.749524,-8.219881,5.303666,7.298273,-9.259800,-1.103190,6.093173,-5.336064,1.838642,-9.788652,1.443865,7.837069,2.794632,-6.708267,-2.839782,-0.420303,-7.356798,-1.953611,1.759297,-4.311616,-0.997383,-7.663678,6.753512,-1.385171,9.353794,-4.343741,-6.511458,7.658647,-3.885666,-3.577817,1.428051,4.463422,-9.703938,6.082343,4.290940,6.131175,2.723870,1.882718,-9.103127,7.794450,-7.387170,8.671766,-1.782271,6.468891,-4.499272,9.057340,-2.476472,3.644827,-6.901572,5.304993,7.590792,1.530799,-7.894737,7.226473,-3.867933,-3.437526,5.188982,-5.671581,-2.390877,-5.649868,8.435151,1.991563,-0.338942,-0.660555,6.570280,-3.942467,4.572068,2.194589,-5.037803,-4.618140,-8.945479,0.216815,-2.929379,4.981041,7.770200,6.952639,1.053662,2.290679,-1.055471,-7.348869,5.648227,-8.103545,4.033832,-3.495680,-1.585008,-6.637896,-7.388746,-3.466033,8.283395,8.173612,5.959149,-6.599968,0.794010,-2.697636,4.726888,-7.136527,6.744337,8.439782,-2.409946,-5.025152,6.341330,9.842438,8.466492,-0.391670,5.651050,1.671620,1.985457,5.310714,1.964882,-0.315727,6.693544,1.482784,7.742844,7.648717,4.392120,-6.565986,-6.284860,-8.316139,-6.814737,8.325087,-3.215016,-4.596065,-7.785662,7.689485,-2.252938,-2.258502,-6.644309,-9.131020,3.747575,0.367183,-8.097659,5.603837,-2.277687,-6.339757,-1.614582,-8.434842,-3.810912,-4.092472,0.380615,5.496408,5.358425,6.337004,1.109065,3.215362,7.054866,6.046538,1.539967,-5.774352,-8.062441,-7.451076,-7.640521,-4.274278,6.747585,8.664965,-9.764173,-2.425366,5.091455,5.667006,-7.527126,1.685749,8.723272,7.732513,8.113887,-5.238519,-4.585395,-4.987726,-0.822443,0.066905,-9.427482,-6.223288,3.988500,-4.601820,-0.045130,-5.673114,4.337465,-6.038817,-4.652519,7.643953,9.177133,-5.558185,-8.338610,3.993162,3.834532,-0.121880,9.273280,-8.204709,-2.360184,0.383271,-9.885970,2.845833,1.274177,-9.309617,0.407907,4.743671,-8.713795,-9.404023,1.002462,5.089122,-2.014354,-3.788151,-4.415614,1.015942,1.152212,4.872130,-2.482153,3.644857,-3.562970,8.715124,3.166169,-4.517553,-3.079248,-7.572451,-1.610268,-5.147750,-7.821654,5.351233,1.863681,3.700620,4.617410,-8.891893,0.773543,-0.086973,-0.021181,0.079897,-2.881693,7.978843,-5.596875,-0.579521,5.735752,4.519876,1.703345,-8.746513,3.876742,-6.682727,-4.534647,-7.081967,-2.922379,8.144098,4.468886,1.758428,-6.857336,-6.177563,-2.061138,-0.675982,-6.599342,9.975346,-2.235083,-8.188594,6.171696,-6.769729,-8.197665,4.996691,3.597239,9.766645,3.545191,0.454993,0.019313,-0.801992,-1.493642,2.266871,5.979619,1.700809,-3.898165,4.488902,-2.894459,1.079914,8.626978,0.134927,8.169975,4.093096,9.095795,-5.057301,-8.656758,1.678509,1.036974,8.204268,0.545418,-1.979861,0.206433,-4.806634,-6.450819,-3.789374,-4.970970,-5.505634,-9.833152,9.554292,-5.558309,-1.299354,-0.298851,-1.196464,-5.268398,-0.120820,-7.990992,6.017890,8.698096,9.481582,5.540105,7.730132,6.661705,3.551730,1.166969,-5.223370,-4.569927,-8.378087,-1.564424,8.882901,2.806987,-2.778768,-7.863411,5.722818,9.039799,6.867897,-3.567161,6.097467,0.724990,2.675472,7.742113,-7.048344,-3.451352,-6.310042,0.097858,1.001255,-4.588068,-4.186720,1.585200,-2.443729,-7.822067,9.547983,-2.229765,9.050304,9.670815,-4.258836,-9.105977,-0.265739,2.405920,0.579401,-5.935462,6.018089,-3.699407,-5.133860,0.458878,3.730639,-2.969710,-2.112840,8.932273,-5.037238,-0.093918,8.127319,-8.520856,5.097962,-3.427615,-4.963094,5.854481,5.401782,-8.928839,7.758346,-1.302502,4.405525,8.655906,2.811452,6.975228,9.113190,-9.741060,-0.626124,8.521457,1.559349,-6.019337,-7.197660,7.359172,-0.872562,3.193374,-0.033936,-9.631500,2.177101,2.417799,-3.995049,-5.731539,0.891506,-1.359963,3.894000,6.850406,9.268195,3.270379,-3.337130,-1.618149,-8.921856,-0.282434,9.298048,-5.760359,4.657382,-6.481164,1.749683,1.277622,0.766583,-8.193838,7.134184,8.852986,-9.537455,4.219168,-5.743169,8.748189,4.975542,7.980859,-1.051579,1.994505,9.078148,7.143768,4.928844,7.309044,-9.634714,1.629695,-2.066695,-0.819858,2.513691,9.939001,7.289366,-8.166055,-2.026999,-3.354469,-1.062583,-3.973616,5.130153,-7.305633,0.379759,5.631333,8.632052,6.507070,-8.886798,-1.650411,0.255977,5.551023,-8.654182,-5.954210,4.702460,4.510275,-0.837973,2.395843,3.562621,-9.937860,-0.510533,-3.009526,7.485670,0.032877,-9.274500,7.249907,2.369477,-8.294765,1.017325,-6.862924,5.558386,-3.622018,-1.952272,6.279621,8.117387,-2.195245,-5.152722,8.646092,-4.746118,4.859818,1.676237,7.771411,0.041234,-3.932949,-3.034591,6.664636,8.598086,1.231468,3.632723,3.465157,3.845354,-7.087445,9.730216,7.285775,-7.077633,-8.195926,4.498616,-6.902009,3.613971,7.662954,-8.887137,-0.192400,-3.552805,1.074424,-2.050191,-9.825312,-1.491305,9.755124,6.252711,2.220806,8.248994,5.657323,9.692214,4.193125,-1.771769,-2.741296,4.182441,-2.678234,4.598281,-6.096520,3.796839,9.944724,5.304542,7.036285,8.240657,2.493850,-7.428136,1.582761,-9.699962,-7.521613,-1.734569,8.498837,3.853486,9.015154,2.545970,2.454521,6.331839,-7.596181,4.304769,6.460620,6.706069,-9.910157,4.142443,8.410414,-5.568596,-5.973344,7.446673,2.542766,-8.533552,3.095486,-8.441959,-6.022144,4.269293,-3.229382,-3.853436,8.807764,-7.722090,8.286722,0.393171,-2.626979,-5.323869,-9.430876,-5.532027,0.043425,7.818836,5.378299,4.182678,2.887640,-3.355484,0.558484,7.367358,-4.894000,-4.387628,0.702687,4.414023,-8.957300,-5.802733,0.946692,-1.796570,7.322282,4.490265,8.757358,-2.000979,5.523661,-9.218356,9.063627,1.801205,-4.323484,3.792241,2.922627,8.368385,9.905804,2.504871,-1.767519,6.932705,7.835877,-0.833219,4.455334,2.176542,-3.020238,7.228511,8.939210,7.261387,2.609153,1.776297,2.161860,-0.224930,-5.816951,5.257530,8.709496,8.530638,0.061175,3.017861,-7.879667,5.764097,-0.106839,8.427287,7.871981,6.519060,6.315072,-5.217419,7.042168,0.084743,-8.767326,3.509626,9.858507,-8.765455,-7.474289,5.912005,-3.039470,3.562058,-9.324645,-3.180481,-5.429688,-4.629855,-9.818271,-0.842302,5.110181,7.505692,7.233960,2.627250,0.744246,7.740255,9.406036,5.517686,-0.572057,-8.061639,3.809781,-2.366556,6.599488,7.311370,0.786463,1.294585,-0.750219,-2.739285,4.643217,-3.824657,6.280045,0.612231,1.834793,-1.166553,0.300678,-1.034757,3.643680,-0.957631,3.233712,-6.459727,-2.730533,8.345593,5.925352,-2.717140,8.227141,0.568478,-0.582779,1.757828,0.649739,6.224922,-9.611285,0.957414,0.529170,-7.408097,-7.567204,2.713855,6.152361,5.210066,5.311799,3.172422,-8.534584,3.100366,6.980084,-5.505583,1.866473,-4.306507,7.280458,6.930357,5.581682,6.367368,1.344727,-5.769183,6.092488,3.470232,0.468512,1.338973,0.313657,0.081273,8.889477,-1.483761,3.568515,7.016434,-0.322440,9.961352,-2.403525,1.052503,-1.750107,-0.796133,4.896527,-9.932419,1.648158,6.332392,-3.799079,7.019556,-3.187921,-6.354270,-5.978891,6.556727,5.155114,7.055813,7.761118,6.046118,-1.309384,-7.726798,1.306866,2.039352,-0.223462,2.931546,6.977045,9.719090,-9.412327,6.287035,9.659668,-5.418007,-9.823824,-0.610070,-8.726015,0.193834,-8.051016,1.735388,-5.163455,-8.473269,5.141865,1.611286,-3.251515,-2.830891,2.660703,-7.027712,-7.920857,2.893630,-6.852730,2.264167,5.017177,6.675719,-9.572510,8.206733,4.780449,0.501799,8.928637,4.180424,3.510486,8.854129,-9.847393,4.945511,-0.173958,4.728402,1.803235,1.059701,8.825008,-7.439081,5.339576,-0.798495,6.917247,2.470405,-7.516260,-7.012006,8.088215,-8.015970,6.626419,-8.130291,-2.897453,-5.102586,-3.386834,-9.020912,9.225398,6.826690,-4.902936,4.794880,-8.754129,3.855526,-9.884942,-5.836554,6.541115,1.477244,8.106556,-4.477218,9.576212,2.468057,-0.430784,1.296184,-1.713281,1.334951,-7.969700,-0.114457,3.182068,4.770301,4.143532,3.145267,4.909096,-1.125780,3.366549,-2.493683,5.031612,-2.675065,-6.554537,6.143863,1.813500,8.847057,-0.930905,-1.344962,1.067305,2.606789,5.641013,1.594114,9.814526,5.592634,-5.443319,9.050383,8.631831,-2.540784,7.464698,-9.467360,-9.019403,-2.744659,3.895651,-0.536450,-9.195254,-6.072566,4.675298,-4.472905,4.643113,6.339005,-3.671527,4.333444,-6.198306,6.094366,-2.019974,-0.549892,5.175495,0.931118,0.577579,-8.926653,0.863810,-2.198814,-4.907140,8.391933,-2.366629,-1.500575,1.141926,2.251710,5.741169,6.716012,-0.731025,-8.059337,-8.008634,7.728651,8.527592,6.841309,-7.103157,0.192195,9.926036,-0.676198,4.461491,-2.870381,-0.315934,4.862836,-0.213375,8.529758,-7.314766,-3.525584,6.288668,6.876382,8.497832,6.354305,-4.646871,8.369129,5.849350,6.808501,-6.923810,3.975414,7.503044,-5.935880,5.357179,8.236152,8.564806,-7.450424,8.316205,4.515784,9.344046,-7.383002,-9.933105,5.531515,0.234810,-5.231699,-6.245832,-0.549600,-3.626330,7.627661,3.388851,-7.713782,-5.595612,2.063489,-2.257787,4.595477,-3.755034,6.237439,8.726448,-2.333700,5.684485,-6.485662,3.231977,-8.132048,1.615686,0.367314,-0.025896,9.284140,1.443085,-8.520722,9.815097,9.853639,3.979208,-6.183424,2.742649,2.390932,-2.099955,-2.914470,-0.038109,3.874287,-2.347209,-0.701645,-6.467825,1.733042,7.622634,1.019601,1.438918,-4.851218,4.344535,0.296364,9.643892,-3.880078,-8.672494,9.020438,9.776257,-6.774196,-1.456598,-0.470760,-5.737872,-7.284008,8.085104,8.010487,-4.576867,3.142470,-2.288036,-5.115360,6.014835,5.731208,7.661468,-2.825394,-9.655211,-2.690164,-0.519199,4.033609,-1.214946,-8.673961,-1.738849,0.517416,9.941412,-1.379004,7.930527,9.853234,4.791423,5.330075,-9.368856,1.087897,-8.827860,1.240760,-0.520417,-6.777229,-2.998803,-7.264433,-5.993396,1.494121,-8.155463,8.855219,-5.443612,-5.870344,-9.030491,-0.536168,-3.343348,8.317567,8.867525,3.894856,8.168485,-6.140650,-1.608176,-5.634819,-5.851897,-5.062963,-1.362741,3.868280,-1.198638,-3.114899,8.536883,8.301592,0.434663,-7.912106,0.145593,-5.833094,1.469297,-7.748791,-0.529379,-3.549584,-3.015758,9.919705,9.169911], dtype = "float32")#candidate|3613|(1350,)|const|float32
const_3614 = relay.const([-5.563341,-9.645369,-1.448276,-5.946322,-6.690918,-0.515565,-2.285927,-8.819513,7.474411,-4.705482,3.988410,-0.088092,3.609963,8.381357,5.479724,-2.908655,0.183315,-4.977761,-8.576629,9.646207,-4.174213,-9.045917,4.681013,-9.809224,7.514162,1.819330,5.385238,3.201570,1.932982,-0.816150,3.731452,-8.324450,4.627768,-3.806480,2.603251,7.090670,9.963071,-6.303506,-5.354382,0.230730,4.577122,-1.128086,-3.460454,7.190206,8.114190,2.043540,5.103778,0.144563,-2.348833,-9.621367,3.177507,6.960812,7.154580,-3.598749,-9.899158,1.668240,-2.209446,2.425263,-5.529620,-6.710848,-5.549508,-9.604577,0.591072,-0.085329,-8.937457,7.620259,-3.245163,-2.905308,-1.836839,5.045638,8.822955,2.773724,9.968918,-3.745396,9.708509,9.045661,-9.723443,6.516340,6.185284,8.676655,7.839089,-3.161064,-9.463304,7.742120,8.551410,3.540149,-5.643278,-3.480678,4.381868,9.769157,0.082432,-0.064082,-9.285085,5.033680,-8.964123,8.166694,2.118754,2.856480,5.485247,-6.489059,-6.086054,3.783736,-1.967318,-2.865595,-4.016320,1.434869,-9.352915,-6.868418,4.603064,-6.575977,-3.285730,1.905110,1.152990,2.117189,-1.314971,6.024677,-3.105958,0.931947,-9.403087,-9.390009,0.779370,-3.738530,-5.197016,-4.938191,-6.681696,8.615795,8.087122,-9.666161,7.114141,3.918216,-9.480375,-9.961192,8.416999,4.653600,0.327674,-3.119142,4.581345,-8.176279,1.545700,-1.666716,-4.355283,8.408615,-9.345126,-1.947940,9.261575,1.912683,0.706414,-6.119541,1.423874,-4.551958,-5.858581,6.938246,-6.542715,1.507965,2.600267,3.576735,4.513659,7.689629,6.318851,5.888036,3.935253,-2.756692,6.391104,6.146385,-0.354069,4.379171,-8.669501,3.053047,5.161322,9.877134,-6.780082,-1.936954,5.064437,1.642986,6.156291,5.644267,-3.863363,4.645592,1.612505,-8.248901,6.654450,-2.817419,7.297657,-2.489478,-3.962282,5.673095,-1.235462,-6.063075,1.914336,-7.124000,-8.544914,0.219317,1.169386,-5.025233,7.030153,5.207591,8.153205,-5.729875,4.094954,1.798346,-8.980860,-2.571313,-1.394057,-2.607902,-4.979835,-4.879802,4.155663,2.051677,7.664215,1.357988,0.138452,8.540619,-0.880924,6.032261,-5.887408,5.588137,5.986825,6.259951,-4.778892,1.865212,3.240585,4.790342,8.319903,3.819132,9.850202,6.343491,3.731711,8.176550,-6.627693,6.638073,5.785942,-6.480586,-9.660204,-3.443540,2.736797,-0.178380,9.379570,7.804961,-1.343928,7.800452,8.661272,-2.000260,2.662378,-8.234521,-2.482869,-8.907926,-1.891716,-3.693586,8.721539,1.651062,-1.080403,8.726700,-1.061909,-8.030528,2.426640,-1.503274,-6.246383,-3.789353,-5.774512,-4.102279,-6.827638,-9.078164,1.909969,-5.978044,3.827364,6.895119,0.213750,4.875240,-4.312743,-2.315090,-5.772387,-0.114154,-8.207255,-6.574381,-9.754898,0.240921,-6.123560,4.151976,7.018858,-9.591803,-9.936294,-2.051592,-3.193308,5.305148,-5.265669,-5.437635,-9.180037,7.666415,9.405824,4.844735,-7.711107,0.320294,-5.583240,-5.281853,-8.897613,-5.331708,9.639750,-8.534149,-9.238439,-4.681908], dtype = "float32")#candidate|3614|(300,)|const|float32
call_3612 = relay.TupleGetItem(func_1912_call(relay.reshape(const_3613.astype('float32'), [15, 9, 10]), relay.reshape(const_3614.astype('float32'), [50, 6]), ), 1)
call_3615 = relay.TupleGetItem(func_1915_call(relay.reshape(const_3613.astype('float32'), [15, 9, 10]), relay.reshape(const_3614.astype('float32'), [50, 6]), ), 1)
output = relay.Tuple([call_3586,var_3587,const_3588,bop_3604,call_3612,const_3613,const_3614,])
output2 = relay.Tuple([call_3589,var_3587,const_3588,bop_3607,call_3615,const_3613,const_3614,])
func_3616 = relay.Function([var_3587,var_3603,], output)
mod['func_3616'] = func_3616
mod = relay.transform.InferType()(mod)
mutated_mod['func_3616'] = func_3616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3616_call = mutated_mod.get_global_var('func_3616')
var_3618 = relay.var("var_3618", dtype = "float64", shape = (15, 6))#candidate|3618|(15, 6)|var|float64
var_3619 = relay.var("var_3619", dtype = "float64", shape = (14, 1, 14))#candidate|3619|(14, 1, 14)|var|float64
call_3617 = func_3616_call(var_3618,var_3619,)
output = call_3617
func_3620 = relay.Function([var_3618,var_3619,], output)
mutated_mod['func_3620'] = func_3620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2754_call = mod.get_global_var('func_2754')
func_2756_call = mutated_mod.get_global_var('func_2756')
call_3622 = func_2754_call()
call_3623 = func_2754_call()
output = relay.Tuple([call_3622,])
output2 = relay.Tuple([call_3623,])
func_3626 = relay.Function([], output)
mod['func_3626'] = func_3626
mod = relay.transform.InferType()(mod)
output = func_3626()
func_3627 = relay.Function([], output)
mutated_mod['func_3627'] = func_3627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2798_call = mod.get_global_var('func_2798')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_3678 = relay.TupleGetItem(func_2798_call(), 1)
call_3679 = relay.TupleGetItem(func_2799_call(), 1)
output = relay.Tuple([call_3678,])
output2 = relay.Tuple([call_3679,])
func_3682 = relay.Function([], output)
mod['func_3682'] = func_3682
mod = relay.transform.InferType()(mod)
output = func_3682()
func_3683 = relay.Function([], output)
mutated_mod['func_3683'] = func_3683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3423_call = mod.get_global_var('func_3423')
func_3424_call = mutated_mod.get_global_var('func_3424')
call_3724 = relay.TupleGetItem(func_3423_call(), 0)
call_3725 = relay.TupleGetItem(func_3424_call(), 0)
output = relay.Tuple([call_3724,])
output2 = relay.Tuple([call_3725,])
func_3746 = relay.Function([], output)
mod['func_3746'] = func_3746
mod = relay.transform.InferType()(mod)
output = func_3746()
func_3747 = relay.Function([], output)
mutated_mod['func_3747'] = func_3747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3746_call = mod.get_global_var('func_3746')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_3777 = relay.TupleGetItem(func_3746_call(), 0)
call_3778 = relay.TupleGetItem(func_3747_call(), 0)
const_3783 = relay.const([[[-0.511550,3.996587,7.009119,4.642413,4.044146,-0.005056,-8.052629,5.325277,7.538132,2.222556,7.699206,3.653743,0.600376,6.858728],[-1.908227,-9.066456,-8.759245,5.026005,5.761974,0.807140,-4.393076,3.778908,-5.889766,-9.829063,9.634862,-8.288390,-3.879157,5.038455],[-8.119897,-8.826394,0.100107,3.247485,-5.674332,-2.366974,5.755354,-2.303815,5.410477,-6.478868,6.143968,-5.476249,-7.166934,5.594750]],[[-2.177482,-3.084385,3.969939,7.565989,5.918089,4.543400,0.178236,3.266423,6.432423,-1.460034,7.595516,-4.644791,7.240648,9.746907],[5.111402,8.483675,2.623365,-5.203020,-5.910806,-4.339163,-3.093995,-4.491839,0.159483,-8.920265,0.910983,3.651479,2.519555,5.896421],[-1.535777,-4.221496,7.830203,8.157133,3.396131,-2.740532,3.690082,9.337370,-4.438745,4.064703,-2.339591,-8.341893,9.496340,-2.908708]],[[9.549950,5.065078,2.346090,1.450925,0.263853,2.573868,2.000709,5.311785,-8.957021,-2.566614,-2.338230,-6.371639,-2.464198,-0.751830],[4.983124,-5.429006,8.807312,-9.731581,-1.743085,3.085854,6.922207,-3.252864,-8.666585,6.121295,0.804782,7.533732,-6.495434,-5.505848],[-8.303186,-1.990092,3.254304,-9.136981,-2.982713,5.212177,3.277680,3.109847,-1.725282,3.273308,9.877525,6.143658,-9.245780,-9.458976]],[[9.534485,1.386362,3.618315,9.967282,0.264009,7.347506,-9.010795,-5.020068,-3.382550,-8.981031,7.016773,2.976743,1.313197,2.058971],[-3.103301,-0.600025,-5.554525,3.025858,3.035292,1.275873,3.863232,-6.821514,4.570515,0.874016,-2.044920,-8.446302,2.392830,-6.982345],[9.630603,-7.222664,2.225417,4.953548,8.232867,-0.961248,8.224660,8.395837,-1.354526,-2.034989,-2.591894,6.851607,-6.481504,-1.788214]],[[-4.312628,-4.610287,6.969137,2.423818,5.627307,-2.645056,4.396398,4.320516,-8.509382,6.563720,-4.678747,2.632479,6.515140,-1.097464],[-5.992236,4.645346,2.501057,-7.042258,2.516356,-3.791019,-7.355261,8.931937,2.795774,-4.291846,8.676936,-3.685403,-1.280323,-8.640062],[5.167202,4.625114,9.040990,-7.464181,-8.430371,9.090776,-7.795946,-9.002329,9.556781,-2.166182,-1.916314,-2.965227,1.298958,1.765304]],[[-4.545074,1.385603,-4.009841,-3.773054,-0.092643,9.008016,7.253487,-6.784765,-6.779069,8.652297,-3.555973,-4.443482,-9.267227,-1.542890],[3.280480,0.674959,0.637689,3.477353,1.529989,8.529144,-4.908081,-1.352813,-8.890244,8.127238,3.889737,-7.776223,7.817324,-6.368445],[8.807473,0.169097,9.164975,9.395997,2.830634,-1.513798,-4.343040,-9.071924,-6.461425,-6.887783,0.832585,8.431780,-3.975716,-8.452213]],[[-9.404411,-5.188515,7.134782,7.443506,-1.692587,6.268550,3.060943,5.605807,-0.730674,3.010034,-1.555397,2.827562,9.045222,3.405301],[-3.775502,6.028067,-7.624248,-3.636840,4.293920,-0.618356,-2.142026,-0.432184,-8.792298,4.095535,3.276519,3.658361,6.016145,-4.275764],[-5.776633,-4.779696,0.495622,8.771394,4.244268,-0.511958,1.306479,5.045952,-7.817723,-2.779770,4.610193,8.245067,-9.743806,-9.229463]],[[8.813878,-3.406119,-1.325498,-3.850893,1.197203,-7.878825,-4.176095,5.433148,4.938774,6.608914,-5.515590,-6.378464,-6.076301,8.368347],[9.199994,-2.455672,-8.333601,-3.976001,4.918675,-4.019979,-9.164271,-1.862821,9.871451,6.236791,-6.153065,9.803244,-4.243821,-8.410340],[3.606362,1.649230,2.214799,-9.991996,-7.779390,4.516994,7.475697,-7.009761,-2.148882,-3.980878,5.549317,-1.141725,4.166632,-6.919804]],[[-9.814505,-5.569393,-0.411032,-2.912783,0.257411,9.831096,8.460346,7.077641,5.682254,-4.077054,-0.312699,6.756590,-2.267755,9.076128],[7.004043,6.544307,-1.760219,-7.191365,9.661641,0.693087,3.167462,6.538418,4.380430,3.613334,-4.808106,-2.399700,8.082369,-9.252787],[4.286312,7.625736,-9.266912,-0.900996,-7.824571,0.026876,5.903897,-5.488808,-3.221012,4.200494,-2.860508,-5.604783,9.664577,-4.583578]],[[-8.566660,-2.922742,-7.463389,3.128223,6.507218,-7.571939,-0.380685,1.943526,-6.331365,-2.545963,3.321010,-1.107727,-1.307595,5.225737],[4.180858,-1.636396,-8.875731,8.216642,-2.206617,4.008555,5.983560,8.286104,-9.671047,2.267312,-0.231967,6.207152,-0.459789,-0.847393],[-2.166793,-9.338947,5.253441,2.383423,0.492408,-1.738546,3.901001,0.120783,4.941540,-6.087166,-9.121330,-5.222027,5.133394,-8.344302]],[[6.743052,4.045372,-9.464805,2.782110,-5.525160,-9.541146,-1.710347,-1.367467,-4.859365,-9.812928,-3.165621,4.764541,-7.383561,-2.911256],[4.331936,8.679134,1.715458,-1.929137,-1.520864,4.235583,1.968315,2.592169,-0.698888,2.289857,7.454609,0.914202,1.470135,-0.082246],[-5.880668,6.836431,-7.644685,8.428772,1.326726,3.554580,8.929973,0.278374,-4.093620,-9.384031,-2.676655,-7.606675,0.410436,5.651732]],[[-7.082611,1.787984,-3.364897,4.739845,8.875815,-8.707428,-4.598950,1.412256,-5.684250,-1.786618,7.840460,-0.530341,6.937468,0.750266],[-0.484114,7.372168,8.800654,2.634191,2.038177,-4.535752,6.013231,-6.114756,-8.760388,-9.545881,-3.746604,-6.567927,1.526779,4.015311],[1.103399,-1.154128,2.116879,-9.048825,-4.422034,3.123972,-8.190347,-0.772066,-0.099834,-8.114466,-5.889580,-4.292143,6.436924,-8.596878]],[[5.569945,3.753526,7.335478,-1.362191,9.975936,4.970558,-4.744394,-5.110861,-3.775145,5.070227,8.909369,3.349093,-0.259249,-9.487303],[-0.582506,-8.635395,-5.808074,-7.476684,7.836589,-4.938699,-8.308267,-5.785161,-9.744676,5.921924,-3.364839,-2.538202,-9.262306,3.198663],[9.217796,5.125023,3.053667,8.465090,1.127408,4.736467,-1.210910,-4.096012,1.870641,6.679263,7.849498,-2.108788,4.235857,4.787789]],[[-1.274332,-9.431508,-2.684374,-6.192096,-8.924976,1.284987,8.795746,-9.222437,-0.296391,-2.266622,-9.416376,-7.783536,9.861423,6.050611],[5.514034,-3.475572,4.811342,7.622052,-6.571293,3.279113,8.139012,6.638163,3.362817,-6.469761,-6.018869,9.824993,-2.632345,-5.661514],[-0.202841,9.350712,-6.733819,-9.845466,-3.762811,9.063127,0.299660,8.639384,1.506697,0.991455,2.502591,-0.119910,7.522948,-0.966695]]], dtype = "float64")#candidate|3783|(14, 3, 14)|const|float64
bop_3784 = relay.greater_equal(call_3777.astype('bool'), const_3783.astype('bool')) # shape=(14, 3, 14)
bop_3787 = relay.greater_equal(call_3778.astype('bool'), const_3783.astype('bool')) # shape=(14, 3, 14)
output = bop_3784
output2 = bop_3787
func_3789 = relay.Function([], output)
mod['func_3789'] = func_3789
mod = relay.transform.InferType()(mod)
output = func_3789()
func_3790 = relay.Function([], output)
mutated_mod['func_3790'] = func_3790
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3898 = relay.var("var_3898", dtype = "uint64", shape = (7, 2, 1))#candidate|3898|(7, 2, 1)|var|uint64
var_3899 = relay.var("var_3899", dtype = "uint64", shape = (7, 2, 14))#candidate|3899|(7, 2, 14)|var|uint64
bop_3900 = relay.bitwise_and(var_3898.astype('uint64'), var_3899.astype('uint64')) # shape=(7, 2, 14)
func_2546_call = mod.get_global_var('func_2546')
func_2549_call = mutated_mod.get_global_var('func_2549')
const_3931 = relay.const([-4,-5,-5,-10,9,8,6,5,-4,-5,5,10,-9,-1,8,8,-6,4,-1,4,6,5,10,5,-4,-10,-4,6,-7,-2,1,-7,-2,-8,3,-4,-6,4,8,3,10,2,-6,-7,-7], dtype = "int32")#candidate|3931|(45,)|const|int32
call_3930 = relay.TupleGetItem(func_2546_call(relay.reshape(const_3931.astype('int32'), [45,])), 1)
call_3932 = relay.TupleGetItem(func_2549_call(relay.reshape(const_3931.astype('int32'), [45,])), 1)
bop_3934 = relay.greater_equal(var_3898.astype('bool'), const_3931.astype('bool')) # shape=(7, 2, 45)
output = relay.Tuple([bop_3900,call_3930,bop_3934,])
output2 = relay.Tuple([bop_3900,call_3932,bop_3934,])
func_3937 = relay.Function([var_3898,var_3899,], output)
mod['func_3937'] = func_3937
mod = relay.transform.InferType()(mod)
var_3938 = relay.var("var_3938", dtype = "uint64", shape = (7, 2, 1))#candidate|3938|(7, 2, 1)|var|uint64
var_3939 = relay.var("var_3939", dtype = "uint64", shape = (7, 2, 14))#candidate|3939|(7, 2, 14)|var|uint64
output = func_3937(var_3938,var_3939,)
func_3940 = relay.Function([var_3938,var_3939,], output)
mutated_mod['func_3940'] = func_3940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2754_call = mod.get_global_var('func_2754')
func_2756_call = mutated_mod.get_global_var('func_2756')
call_3957 = func_2754_call()
call_3958 = func_2754_call()
func_1587_call = mod.get_global_var('func_1587')
func_1590_call = mutated_mod.get_global_var('func_1590')
const_3960 = relay.const([-2.649861,-0.687676,-4.321847,-6.271190,-4.397897,8.527918,-0.513875,2.650462,0.498880,-5.132334,1.543781,4.955010,9.597457,8.921118,8.520616,3.746578,3.994942,-3.343000,7.530369,-2.625294,5.999238,7.406730,-7.325916,-9.984163,3.824728,2.282189,-9.300336,-4.982298,3.667977,-2.960059,-1.090604,-5.503219,8.317028,-2.923128,7.556484,-4.779537,-3.957255,-8.113594,7.063339,-4.276764,-0.300077,4.725603,-8.765047,-0.235246,1.486940,4.862829,9.035269,-2.866093,-7.554258,9.934009,7.483107,-1.407732,0.411876,-3.245333,9.071099,2.641967,-6.328082,6.472135,-2.168822,-7.543690,-5.263228,-7.665323,4.505875,3.301594,7.736757,0.303435,-4.525791,-5.742965,6.996278,-1.369763,-0.569657,-6.568875,9.061942,6.697765,5.504394,2.231295,3.238055,9.098848,-2.311662,4.221860,8.171886,-6.217545,-2.734362,8.555873,7.015011,8.161655,6.954474,2.286962,1.929078,6.011781,-4.424851,-2.034419,-0.842131,7.781954,-1.191472,-4.348955,5.334669,-1.298625,7.109662,5.759785,9.023490,-7.362249,-3.706074,2.436201,1.521551,1.226446,-7.849141,5.186916,6.485936,9.614703,1.618036,-8.353568,8.119390,9.866053,-6.708298,8.128960,3.295652,5.737857,2.209916,2.767079,3.534314,9.913055,-8.475686,-3.547918,0.300915,-3.961245,6.039153,4.973377,4.353205,5.420061,-9.624773,8.647072,0.272226,7.536552,-4.717104,5.722046,2.525940,9.737143,3.196502,-1.798560,8.457111,-4.813392,1.650774,0.085522,-4.614065,-5.639620,-3.059578,-1.540109,-6.307252,-8.415565,-0.249439,-9.887559,-8.717286,8.704445,5.132652,-7.679046,-7.109586,2.706343,1.785914,-8.732158,-5.385430,-2.682094,1.685045,-3.464784,-7.361635,-9.356468,-3.178377,8.117799,-0.672249,-1.669865,-5.762182,-1.935428,1.288168,-6.808216,6.374653,-1.386689,0.671089,-8.359499,4.510267,0.590159,2.157885,-0.103623,-0.704507,0.039465,3.642305,5.878883,-5.785417,-6.862973,9.405789,-9.250977,-5.332529,-2.382210,5.936686,-5.035968,7.957382,9.198429,6.989066,-9.815140,9.465669,-9.998771,-6.778021,-7.864026,2.152231,-8.433884,8.794927,3.907935,-2.211905,5.595534,-3.536473,-3.100308,4.988485,9.253346,-6.881354,6.670573,3.645466,-0.798522,8.681332,-3.751629,3.561081,2.955952,-0.140051,-7.594994,4.116509,-4.510309,3.483028,0.251527,-9.993225,0.950484,9.801549,-8.378076,-4.860361,-1.099264,3.658159,6.319893,0.833091,7.303281,0.188215,-4.107563,-6.343630,4.503675,-7.917825,-8.548348,4.072970,8.350214,-9.310398,0.324271,-7.216821,-6.714229,-1.321782,-3.663932,1.631986,2.122491,-9.738666,7.574938,7.465076,-0.453709,2.649462,-5.141401,9.797867,4.778483,-9.579538,-8.735241,-8.408944,-6.696098,-9.996736,1.950770,7.573702,6.747390,-6.131043,-1.670682,9.479852,2.837917,9.528166,5.597623,4.950933,2.258327,4.047798,-2.109805,-4.397534,-4.842976,-3.400266,-5.824496,0.152323,8.584218,-8.591845,0.761044,-9.423340,4.779822,-3.501606,-5.187010,4.534827,9.036798,-3.302714,5.914346,8.454467,3.597050,1.819001,6.858081,0.135072,-1.270624,-3.649067,2.727023,9.154976,-9.638221,6.679963,4.942553,-5.187128,2.618724,8.568411,-4.729387,1.128445,-0.007934,9.040006,8.161452,-2.256817,6.628118,9.669634,2.890130,9.753555,-3.983586,7.689403,4.751966,4.716516,-0.380997,1.852268,1.757203,-5.972562,7.598395,1.520656,4.266838,9.043348,-4.902542,2.819572,6.823589,5.754748,-0.915016,5.560325,3.153027,-0.701510,2.608839,-0.133132,-2.648841,-5.316476,-3.324449,-3.580030,5.008800,-1.593156,-2.191217,-4.048890,-3.396179,-8.741415,-2.153596,5.477388,-6.688816,8.026104,7.956502,-8.418389,-4.236992,-2.965454,-4.693088,-6.376313,-8.093466,8.389293,3.734925,-5.375003,8.882572,-7.841641,-0.291779,2.124388,7.728908,5.540902,-8.844294,6.739913,-4.066192,-7.929122,-2.280786,0.764912,7.515783,-5.183912,-7.694193,6.244858,2.423226,4.936086,3.898620,-4.289605,8.706277,6.547329,5.922825,-1.130461,-9.302399,-7.273685,-8.956935,6.949132,-7.174834,-3.514583,-1.173960,-9.064593,7.396331,-3.518700,1.328700,5.243862,-2.947113,-0.713352,6.272161,8.777836,5.135228,2.135948,8.954253,-1.246552,-5.241438,-3.412878,-1.837448,-7.909723,-6.790761,-0.561688,4.495282,-6.150309,-8.063253,1.954695,-8.716936,-8.750045,-6.572030,0.641063,-2.291195,1.638922,-2.764948,-9.994307,-8.047830,-5.893691,0.064902,-7.865400,-1.686168,-7.340004,-3.417555,5.684645,-6.890864,-2.761274,0.743362,4.580390,9.489886,-9.291113,-1.334448,-4.296250,1.502450,-3.410228,1.129515,0.237728,3.500138,7.802989,5.918025,-2.857661,-9.932654,-1.590675,-1.154118,0.224618,-2.346203,2.499191,-9.576642,6.914579,-4.910929,-0.398830,7.540397,-0.723644,7.310385,-6.417006,-8.972110,1.506975,3.201665,-9.808239,5.503786,-9.719962,0.912011,-9.679150,4.766611,6.787244,5.805178,-3.166273,9.880565,-3.262349,-1.073356,7.074588,0.211308,2.330801,-4.486383,9.835540,6.860608,0.669889,1.193140,7.968576,6.081777,4.563980,-3.582367,8.912438,-1.805012,3.647549,-8.000005,1.965106,3.656737,1.734548,-6.965796,0.233171,-0.607881,-8.238646,-7.186585,-0.827406,-9.066839,2.515895,6.623777,-0.929221,-7.383127,-3.430533,-9.658611,-6.695364,-8.381925,3.356254,-2.724291,2.880625,7.023589,9.680412,2.568485,8.931761,9.151568,-6.493704,-0.560153,-7.000167,-2.854882,3.651833,-7.527268,-9.243005,3.685707,6.452447,-9.293572,-7.257244,-5.641005,-0.122166,-0.394409,9.654009,-0.076922,-1.835410,-9.759024,5.207196,-3.768747,1.501117,-2.870557,0.399252,3.243836,-1.137576,7.584696,4.742296,-3.074857,2.333054,9.119852,-5.437069,5.527467,-3.968841,2.785137,-3.077907,4.159369,-3.373843,-2.725101,5.015154,-2.690604,4.322491,9.070181,2.816303,-9.000397,-6.730276,0.508030,3.020342,5.495270,-2.339995,7.604571,-6.271052,-4.415173,6.458201,2.665135,-0.707206,-0.845955,0.096133,-7.744827,8.669022,-0.283073,-5.949007,-4.467200,-7.757063,-8.533854,-3.333478,5.349027,-6.893345,5.287784,-4.017559,-5.661993,-1.294258,9.685467,-3.652968,-8.321928,-8.590739,6.995131,-0.494722,0.977410,-8.505144,9.259787,3.988152,8.362124,-2.064695,3.299295,9.745818,4.348572,-3.126476,-8.140307,-4.856654,-2.756081,6.137754,2.324337,5.869921,-7.122025,-1.633929,-9.524480,-2.205450,6.544071,-2.159780,-5.741161,4.826921,4.506341,-2.779133,-1.963953,-2.558992,1.742352,2.485636,4.558246,1.542326,-1.595165,2.947225,-4.588988,-3.899405,-9.046864,-8.043404,4.831773,-6.933978,-5.655234,-0.565657,8.254681,4.681389,-9.075621,-6.581058,-3.134058,4.388382,0.745429,6.842871,-5.553289,-3.006015,0.529150,5.455105,-7.903420,0.161318,-9.760570,2.284233,8.825048,9.789557,3.032286,9.262468,7.092349,-8.512493,-5.863410,-0.577004,-7.137567,4.532398,-6.919777,-4.852544,8.122903,2.340500,2.742525,7.885198,6.928442,-4.431077,-4.474308,-5.151248,-7.321594,3.575908,5.482179,4.211042,-8.115641,3.484843,-8.501123,6.855271,4.908702,7.978829,5.003986,6.461519,2.459164,-2.847287,-7.600571,-7.359368,1.254400,2.894027,6.577896,-4.152926,3.283587,-2.321364,0.820070,2.340143,-7.757698,9.071531,-7.510208,8.907450,-0.444651,3.900927,-4.624017,2.143313,5.356633,-5.576560,-0.268439,-8.453386,-1.105553,8.876644,-8.173323,9.414472,5.401539,7.127937,2.439995], dtype = "float64")#candidate|3960|(720,)|const|float64
call_3959 = relay.TupleGetItem(func_1587_call(relay.reshape(const_3960.astype('float64'), [8, 15, 6])), 1)
call_3961 = relay.TupleGetItem(func_1590_call(relay.reshape(const_3960.astype('float64'), [8, 15, 6])), 1)
func_2206_call = mod.get_global_var('func_2206')
func_2209_call = mutated_mod.get_global_var('func_2209')
var_3969 = relay.var("var_3969", dtype = "float32", shape = (1680,))#candidate|3969|(1680,)|var|float32
call_3968 = relay.TupleGetItem(func_2206_call(relay.reshape(var_3969.astype('float32'), [8, 14, 15]), relay.reshape(call_3959.astype('float64'), [720,]), ), 1)
call_3970 = relay.TupleGetItem(func_2209_call(relay.reshape(var_3969.astype('float32'), [8, 14, 15]), relay.reshape(call_3959.astype('float64'), [720,]), ), 1)
output = relay.Tuple([call_3957,call_3959,const_3960,call_3968,var_3969,])
output2 = relay.Tuple([call_3958,call_3961,const_3960,call_3970,var_3969,])
func_3975 = relay.Function([var_3969,], output)
mod['func_3975'] = func_3975
mod = relay.transform.InferType()(mod)
mutated_mod['func_3975'] = func_3975
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3976 = relay.var("var_3976", dtype = "float32", shape = (1680,))#candidate|3976|(1680,)|var|float32
func_3975_call = mutated_mod.get_global_var('func_3975')
call_3977 = func_3975_call(var_3976)
output = call_3977
func_3978 = relay.Function([var_3976], output)
mutated_mod['func_3978'] = func_3978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2798_call = mod.get_global_var('func_2798')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_3989 = relay.TupleGetItem(func_2798_call(), 1)
call_3990 = relay.TupleGetItem(func_2799_call(), 1)
func_1721_call = mod.get_global_var('func_1721')
func_1726_call = mutated_mod.get_global_var('func_1726')
var_3994 = relay.var("var_3994", dtype = "float64", shape = (30,))#candidate|3994|(30,)|var|float64
const_3995 = relay.const([[-6.960934,6.847106,-4.025982,7.095988,1.209139,8.304885],[-9.781041,1.466213,-2.975654,7.930534,9.548704,-9.091217],[3.327990,-2.443251,-0.103363,1.657102,0.154519,-3.401248],[-1.298504,-4.828530,-2.751547,-8.749813,9.484940,-3.088294],[1.199318,-2.336476,1.588869,8.825575,-3.250992,-1.309358],[-4.366568,2.959470,-9.243342,7.527306,9.392506,9.324278],[5.457024,-0.564422,4.108627,2.984278,-0.649402,7.023190],[-8.887235,5.113812,-6.174365,3.977163,2.202121,3.357580],[-4.681949,-0.685265,-1.976783,6.441729,2.679580,-8.147564],[-6.254770,0.573354,0.389804,-3.677528,-9.380175,-1.483107],[4.508496,0.571295,-7.195465,1.707168,6.160891,5.565892],[8.979463,-0.610846,-5.671047,1.520798,-4.592411,-5.094407],[1.924757,5.945590,-3.235625,-9.391583,9.504922,-5.831242],[-3.519334,-2.567133,-2.290704,7.894477,-5.875938,-2.641499],[-3.823577,5.258215,6.372092,-7.585365,-1.224126,-7.847168]], dtype = "float64")#candidate|3995|(15, 6)|const|float64
const_3996 = relay.const([True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,True], dtype = "bool")#candidate|3996|(216,)|const|bool
call_3993 = relay.TupleGetItem(func_1721_call(relay.reshape(var_3994.astype('float64'), [6, 1, 5]), relay.reshape(const_3995.astype('float64'), [90,]), relay.reshape(const_3996.astype('bool'), [216,]), ), 3)
call_3997 = relay.TupleGetItem(func_1726_call(relay.reshape(var_3994.astype('float64'), [6, 1, 5]), relay.reshape(const_3995.astype('float64'), [90,]), relay.reshape(const_3996.astype('bool'), [216,]), ), 3)
func_3975_call = mod.get_global_var('func_3975')
func_3978_call = mutated_mod.get_global_var('func_3978')
var_4008 = relay.var("var_4008", dtype = "float32", shape = (1680,))#candidate|4008|(1680,)|var|float32
call_4007 = relay.TupleGetItem(func_3975_call(relay.reshape(var_4008.astype('float32'), [1680,])), 2)
call_4009 = relay.TupleGetItem(func_3978_call(relay.reshape(var_4008.astype('float32'), [1680,])), 2)
output = relay.Tuple([call_3989,call_3993,var_3994,const_3995,const_3996,call_4007,var_4008,])
output2 = relay.Tuple([call_3990,call_3997,var_3994,const_3995,const_3996,call_4009,var_4008,])
func_4030 = relay.Function([var_3994,var_4008,], output)
mod['func_4030'] = func_4030
mod = relay.transform.InferType()(mod)
var_4031 = relay.var("var_4031", dtype = "float64", shape = (30,))#candidate|4031|(30,)|var|float64
var_4032 = relay.var("var_4032", dtype = "float32", shape = (1680,))#candidate|4032|(1680,)|var|float32
output = func_4030(var_4031,var_4032,)
func_4033 = relay.Function([var_4031,var_4032,], output)
mutated_mod['func_4033'] = func_4033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3746_call = mod.get_global_var('func_3746')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_4041 = relay.TupleGetItem(func_3746_call(), 0)
call_4042 = relay.TupleGetItem(func_3747_call(), 0)
var_4055 = relay.var("var_4055", dtype = "float64", shape = (14, 4, 14))#candidate|4055|(14, 4, 14)|var|float64
bop_4056 = relay.less(call_4041.astype('bool'), var_4055.astype('bool')) # shape=(14, 4, 14)
bop_4059 = relay.less(call_4042.astype('bool'), var_4055.astype('bool')) # shape=(14, 4, 14)
var_4061 = relay.var("var_4061", dtype = "float64", shape = (14, 4, 14))#candidate|4061|(14, 4, 14)|var|float64
bop_4062 = relay.logical_or(call_4041.astype('bool'), var_4061.astype('bool')) # shape=(14, 4, 14)
bop_4065 = relay.logical_or(call_4042.astype('bool'), var_4061.astype('bool')) # shape=(14, 4, 14)
bop_4066 = relay.mod(bop_4062.astype('float32'), relay.reshape(var_4061.astype('float32'), relay.shape_of(bop_4062))) # shape=(14, 4, 14)
bop_4069 = relay.mod(bop_4065.astype('float32'), relay.reshape(var_4061.astype('float32'), relay.shape_of(bop_4065))) # shape=(14, 4, 14)
func_373_call = mod.get_global_var('func_373')
func_377_call = mutated_mod.get_global_var('func_377')
const_4085 = relay.const([[True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False]], dtype = "bool")#candidate|4085|(1, 216)|const|bool
call_4084 = relay.TupleGetItem(func_373_call(relay.reshape(const_4085.astype('bool'), [3, 9, 8]), relay.reshape(const_4085.astype('bool'), [3, 9, 8]), ), 0)
call_4086 = relay.TupleGetItem(func_377_call(relay.reshape(const_4085.astype('bool'), [3, 9, 8]), relay.reshape(const_4085.astype('bool'), [3, 9, 8]), ), 0)
output = relay.Tuple([bop_4056,bop_4066,call_4084,const_4085,])
output2 = relay.Tuple([bop_4059,bop_4069,call_4086,const_4085,])
func_4088 = relay.Function([var_4055,var_4061,], output)
mod['func_4088'] = func_4088
mod = relay.transform.InferType()(mod)
var_4089 = relay.var("var_4089", dtype = "float64", shape = (14, 4, 14))#candidate|4089|(14, 4, 14)|var|float64
var_4090 = relay.var("var_4090", dtype = "float64", shape = (14, 4, 14))#candidate|4090|(14, 4, 14)|var|float64
output = func_4088(var_4089,var_4090,)
func_4091 = relay.Function([var_4089,var_4090,], output)
mutated_mod['func_4091'] = func_4091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3746_call = mod.get_global_var('func_3746')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_4093 = relay.TupleGetItem(func_3746_call(), 0)
call_4094 = relay.TupleGetItem(func_3747_call(), 0)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_4111 = func_3789_call()
call_4112 = func_3789_call()
output = relay.Tuple([call_4093,call_4111,])
output2 = relay.Tuple([call_4094,call_4112,])
func_4130 = relay.Function([], output)
mod['func_4130'] = func_4130
mod = relay.transform.InferType()(mod)
mutated_mod['func_4130'] = func_4130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4130_call = mutated_mod.get_global_var('func_4130')
call_4131 = func_4130_call()
output = call_4131
func_4132 = relay.Function([], output)
mutated_mod['func_4132'] = func_4132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3746_call = mod.get_global_var('func_3746')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_4241 = relay.TupleGetItem(func_3746_call(), 0)
call_4242 = relay.TupleGetItem(func_3747_call(), 0)
output = call_4241
output2 = call_4242
func_4252 = relay.Function([], output)
mod['func_4252'] = func_4252
mod = relay.transform.InferType()(mod)
output = func_4252()
func_4253 = relay.Function([], output)
mutated_mod['func_4253'] = func_4253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4252_call = mod.get_global_var('func_4252')
func_4253_call = mutated_mod.get_global_var('func_4253')
call_4275 = func_4252_call()
call_4276 = func_4252_call()
output = call_4275
output2 = call_4276
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
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_4339 = func_3789_call()
call_4340 = func_3789_call()
var_4346 = relay.var("var_4346", dtype = "bool", shape = (14, 3, 14))#candidate|4346|(14, 3, 14)|var|bool
bop_4347 = relay.greater(call_4339.astype('bool'), relay.reshape(var_4346.astype('bool'), relay.shape_of(call_4339))) # shape=(14, 3, 14)
bop_4350 = relay.greater(call_4340.astype('bool'), relay.reshape(var_4346.astype('bool'), relay.shape_of(call_4340))) # shape=(14, 3, 14)
func_3397_call = mod.get_global_var('func_3397')
func_3401_call = mutated_mod.get_global_var('func_3401')
var_4354 = relay.var("var_4354", dtype = "float32", shape = (1680,))#candidate|4354|(1680,)|var|float32
var_4355 = relay.var("var_4355", dtype = "float64", shape = (720,))#candidate|4355|(720,)|var|float64
call_4353 = relay.TupleGetItem(func_3397_call(relay.reshape(var_4354.astype('float32'), [1680,]), relay.reshape(var_4355.astype('float64'), [720,]), ), 2)
call_4356 = relay.TupleGetItem(func_3401_call(relay.reshape(var_4354.astype('float32'), [1680,]), relay.reshape(var_4355.astype('float64'), [720,]), ), 2)
var_4361 = relay.var("var_4361", dtype = "bool", shape = (14, 3, 14))#candidate|4361|(14, 3, 14)|var|bool
bop_4362 = relay.mod(bop_4347.astype('float32'), relay.reshape(var_4361.astype('float32'), relay.shape_of(bop_4347))) # shape=(14, 3, 14)
bop_4365 = relay.mod(bop_4350.astype('float32'), relay.reshape(var_4361.astype('float32'), relay.shape_of(bop_4350))) # shape=(14, 3, 14)
output = relay.Tuple([call_4353,var_4354,var_4355,bop_4362,])
output2 = relay.Tuple([call_4356,var_4354,var_4355,bop_4365,])
func_4366 = relay.Function([var_4346,var_4354,var_4355,var_4361,], output)
mod['func_4366'] = func_4366
mod = relay.transform.InferType()(mod)
var_4367 = relay.var("var_4367", dtype = "bool", shape = (14, 3, 14))#candidate|4367|(14, 3, 14)|var|bool
var_4368 = relay.var("var_4368", dtype = "float32", shape = (1680,))#candidate|4368|(1680,)|var|float32
var_4369 = relay.var("var_4369", dtype = "float64", shape = (720,))#candidate|4369|(720,)|var|float64
var_4370 = relay.var("var_4370", dtype = "bool", shape = (14, 3, 14))#candidate|4370|(14, 3, 14)|var|bool
output = func_4366(var_4367,var_4368,var_4369,var_4370,)
func_4371 = relay.Function([var_4367,var_4368,var_4369,var_4370,], output)
mutated_mod['func_4371'] = func_4371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3423_call = mod.get_global_var('func_3423')
func_3424_call = mutated_mod.get_global_var('func_3424')
call_4391 = relay.TupleGetItem(func_3423_call(), 0)
call_4392 = relay.TupleGetItem(func_3424_call(), 0)
var_4396 = relay.var("var_4396", dtype = "float64", shape = (14, 9, 14))#candidate|4396|(14, 9, 14)|var|float64
bop_4397 = relay.equal(call_4391.astype('bool'), var_4396.astype('bool')) # shape=(14, 9, 14)
bop_4400 = relay.equal(call_4392.astype('bool'), var_4396.astype('bool')) # shape=(14, 9, 14)
output = relay.Tuple([bop_4397,])
output2 = relay.Tuple([bop_4400,])
func_4419 = relay.Function([var_4396,], output)
mod['func_4419'] = func_4419
mod = relay.transform.InferType()(mod)
mutated_mod['func_4419'] = func_4419
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4420 = relay.var("var_4420", dtype = "float64", shape = (14, 9, 14))#candidate|4420|(14, 9, 14)|var|float64
func_4419_call = mutated_mod.get_global_var('func_4419')
call_4421 = func_4419_call(var_4420)
output = call_4421
func_4422 = relay.Function([var_4420], output)
mutated_mod['func_4422'] = func_4422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_4430 = func_3789_call()
call_4431 = func_3789_call()
uop_4440 = relay.sin(call_4430.astype('float64')) # shape=(14, 3, 14)
uop_4442 = relay.sin(call_4431.astype('float64')) # shape=(14, 3, 14)
func_3616_call = mod.get_global_var('func_3616')
func_3620_call = mutated_mod.get_global_var('func_3620')
var_4445 = relay.var("var_4445", dtype = "float64", shape = (90,))#candidate|4445|(90,)|var|float64
const_4446 = relay.const([2.350304,-3.705712,-1.179854,-3.078834,-5.427831,4.123588,6.973909,-2.669477,-3.991836,-1.618052,-2.146019,-6.738050,4.823135,-7.822735,-7.796784,8.188480,1.385692,9.538479,2.096919,5.912262,-0.889301,7.987676,6.931038,0.762250,6.963044,-4.047826,-8.319626,-3.665132,8.251007,-4.497412,-9.717196,9.948920,0.534731,0.033811,5.586717,-8.974160,9.323958,0.713342,9.256987,8.052555,-7.221851,3.530119,-3.762771,-5.172750,-9.988890,5.017821,0.914190,-2.796227,4.597788,3.157713,-6.874070,-2.279285,-5.918380,5.942265,-0.964894,-2.563011,-2.499968,9.359340,-3.972805,-6.426359,-0.540458,4.972985,1.590446,-0.763038,7.805701,7.504325,6.833863,3.270709,5.111060,-9.990708,6.861064,-9.248822,-8.430451,-0.967657,-6.217539,6.483566,-6.070863,-5.668163,-2.105833,0.095686,-5.940400,1.388067,-6.435501,4.000266,8.403594,-3.797140,3.333417,4.266421,-9.613823,-5.537171,-7.062572,-6.711622,-4.023994,-2.709088,0.123143,-7.978238,-2.389936,-6.228023,-8.765320,-1.390929,8.524327,2.216344,-6.728927,-9.701124,-3.625162,6.944687,-2.385648,-9.535370,-1.073974,8.234355,-8.391397,9.785818,5.161028,4.960752,-0.289161,-9.836087,-3.538072,-1.094530,-9.941933,-3.149391,6.924133,2.597070,8.623382,-4.543155,4.080788,7.262366,9.647080,-6.180888,-9.378317,-5.324401,-4.296213,-0.780509,-8.290360,3.376841,1.171759,-8.290658,6.657338,-1.342975,6.467912,-9.007822,-8.816329,-2.610973,-5.647923,4.157506,-1.556513,1.031762,-7.880825,-4.899094,-9.516005,0.142428,7.771978,-8.245519,9.868030,8.870684,9.878155,7.410632,3.693987,8.128029,5.067330,0.112870,1.725849,-0.212340,-2.556594,-7.688905,-8.312253,7.287956,1.076335,-5.602130,-5.791770,3.058243,8.825062,-8.864257,-3.232868,-7.147616,-2.450265,-8.942155,4.366574,6.667939,2.717731,-4.965088,0.339256,3.983662,-3.439319,2.754428,2.512074,-3.018802,-6.257236,6.331645,8.927729,-7.607743,8.444746,8.558278,1.588976,7.693792,-1.613517,-1.257456], dtype = "float64")#candidate|4446|(196,)|const|float64
call_4444 = relay.TupleGetItem(func_3616_call(relay.reshape(var_4445.astype('float64'), [15, 6]), relay.reshape(const_4446.astype('float64'), [14, 1, 14]), ), 3)
call_4447 = relay.TupleGetItem(func_3620_call(relay.reshape(var_4445.astype('float64'), [15, 6]), relay.reshape(const_4446.astype('float64'), [14, 1, 14]), ), 3)
func_4366_call = mod.get_global_var('func_4366')
func_4371_call = mutated_mod.get_global_var('func_4371')
const_4455 = relay.const([0.066620,3.002840,1.756306,1.163608,-3.891683,3.958296,-5.108063,7.697874,-9.556833,2.523886,9.952237,-8.436467,8.469401,1.051338,3.317423,-1.116813,-9.874966,2.499037,-8.341803,8.583986,5.590048,2.481999,1.691556,9.550571,0.198383,3.618698,-4.525398,-7.615766,7.323008,-9.053014,-7.182941,7.144375,-7.823217,-9.574076,-8.012126,6.253978,-7.414047,7.606508,0.597204,-2.107065,8.114441,-2.938308,1.265800,3.726809,-5.243300,-9.007226,3.603847,9.886402,-3.428088,-0.238912,5.603614,-2.310542,-5.512015,-5.086742,-3.655906,-9.557675,-8.129076,0.754132,4.380121,-2.764227,-4.745599,-5.138799,-5.922720,4.544989,-5.106280,0.725829,3.535903,8.271075,1.312048,-8.301702,-1.224892,7.028468,5.261623,5.725264,-6.258895,-7.929583,-7.442801,-5.284410,-2.198231,1.109099,2.712075,-4.182216,-4.090197,-8.436926,7.506556,2.685242,-4.212888,-6.771834,-4.017468,-7.364528,9.908001,6.177484,-4.312766,0.202729,-5.309306,2.329937,4.566676,-2.619510,2.435870,-7.621544,4.916312,2.837088,-0.095027,0.297113,4.322394,6.133331,-0.860860,-5.960288,-5.979549,4.117166,-0.628486,-0.392416,3.672003,3.283704,-7.255676,1.685546,0.932367,8.458574,3.131275,-5.602954,-8.671211,8.022372,7.471488,3.663738,5.864468,-0.070205,0.099061,-5.540403,8.957682,-4.685730,1.129975,-6.710896,-8.046585,-8.658083,-5.965411,-3.275333,1.381315,-1.985312,0.781033,-6.054420,-5.790562,-1.660858,-8.401435,-0.449212,-4.662976,4.823274,6.321070,-9.794998,0.218735,8.821369,-9.583559,-3.690489,5.114210,-4.506715,7.119906,-4.843780,7.901674,9.933780,6.546735,9.391074,-2.513821,9.014735,-6.826898,4.710366,-0.069965,-9.312426,-6.661473,-8.353338,3.961248,-9.261873,-0.471726,-9.742498,0.565076,2.600063,-8.916173,-6.778941,7.323283,-4.988092,-5.469524,8.007613,-5.778960,3.064571,-8.686689,-2.039929,-9.149205,-6.962651,4.658963,-6.992125,9.517677,9.069631,-2.852396,-6.185554,8.847514,-8.973860,0.972691,5.435421,6.046640,-8.934519,-0.664525,1.729481,-9.570831,8.115116,-5.842809,-2.239616,5.898077,7.783887,-8.531866,4.032144,-7.554330,8.049440,8.648336,9.342568,5.159717,4.523227,9.891077,-7.077322,-8.210015,8.704722,0.397709,-5.442564,-6.969769,-1.519954,-6.010091,-0.902748,1.165914,-5.565678,-3.035414,1.542054,1.190197,-4.195430,6.568425,-4.677733,-3.411760,7.776914,-2.506130,4.000779,9.611313,3.083319,2.962178,1.261228,5.121612,-0.068217,1.840281,0.472946,-9.333159,8.485335,-9.266594,2.577121,-8.171977,-1.608782,8.343664,5.985728,2.923042,-9.894428,-8.899772,-3.483193,6.269944,-8.533353,-0.651674,5.077047,6.882826,1.825583,4.165206,-2.136841,0.872664,-6.961809,-7.007143,2.242783,-6.101557,1.698636,1.632020,-9.046371,-7.793992,-5.750601,-4.321837,3.229179,-3.062074,9.657572,8.494747,0.948982,-7.976432,8.035853,1.342286,-2.561009,-8.665627,8.786656,0.285170,-3.164292,-7.601991,9.062712,3.522622,-2.449016,9.180613,2.337090,0.106394,3.263135,-3.907409,9.436342,2.305314,7.682253,4.847330,-0.881482,-0.173808,-0.275274,6.639354,2.010328,-7.785031,-6.509232,2.114338,-4.585560,3.892330,-3.957235,1.162713,8.808287,1.229225,-2.786929,1.323814,-8.016456,-6.931854,-4.950886,-5.816541,-5.353079,9.543084,-8.309523,-2.745023,-5.779245,-3.259005,8.542690,-4.150317,-2.121192,2.075857,-4.145580,8.895880,-0.491174,6.645980,3.885684,-3.107249,-0.839667,3.995214,-8.991302,3.876960,5.548620,2.151266,4.588003,0.170040,6.957761,8.927139,-5.659244,-5.986325,-2.701509,1.546869,6.897106,7.204007,-1.544254,-7.769426,-0.283940,8.176518,7.083504,-7.921830,-2.957317,4.332792,-2.659388,4.488298,0.768987,2.838077,8.600247,-9.942416,-3.695761,-6.533221,-4.354556,2.561273,-5.470402,-0.536786,3.533710,4.906387,-3.053206,8.136925,6.831409,6.798374,3.519070,-5.389121,-6.702752,1.689032,-5.606586,9.621192,3.126120,6.872959,8.286224,2.223086,-4.051523,-1.621025,1.328238,1.022488,-9.978743,-3.373530,7.597761,-5.919659,8.227245,-1.952814,2.827237,-6.066090,-3.553060,-8.261458,6.737247,-5.883213,-3.496038,-7.480495,-2.114919,-8.690441,0.879814,-1.691363,9.386381,-3.854854,0.727753,-4.526614,-8.405603,1.073076,-6.515825,-0.147614,2.825716,7.434884,9.580160,-6.783763,1.747637,-7.012080,5.801903,1.645515,2.850320,5.406486,-1.995409,6.848643,-0.705593,5.171696,-1.144392,-2.097240,-1.887485,-6.994836,9.757194,-1.263567,0.354585,2.894955,4.662734,-4.522403,-4.239749,5.533313,9.258839,8.010989,8.733452,1.465525,-5.918661,-5.078333,5.638539,-7.250871,8.085508,-0.475814,8.340634,4.750580,-2.799382,7.448980,5.787319,-3.369479,9.600385,-9.733348,-3.600327,2.072711,0.924716,-7.904308,-5.724000,2.268270,0.757801,-5.776936,-5.141750,3.151069,6.174799,8.451841,-2.160964,-4.007652,-4.022659,-1.597944,-3.302874,6.045297,7.041945,-2.992850,4.995692,3.421271,7.672120,0.228085,6.468194,0.487632,-5.067333,2.419306,-9.243992,-1.376464,-6.911822,2.398022,-2.142035,-8.753470,-9.604644,3.730038,4.758505,-5.576776,2.907179,-3.787158,6.564653,9.985235,-4.708028,-2.507028,-5.590399,3.527071,0.843366,1.930156,-0.245097,-4.774281,1.438026,-6.295610,-3.494882,5.436542,-6.981160,5.044581,2.462088,6.570255,3.048044,-6.755406,4.133076,6.140465,7.897178,-6.921072,-8.377688,-4.868718,3.308046,-7.255792,-9.977068,2.750109,1.673502,-6.051238,9.119094,0.563912,4.392808,4.277960,4.439429,8.416474,7.213611,-4.972284,-3.787495,2.153753,5.464292,-1.239248,-3.308292,9.605893,-4.571535,-7.333458,6.132539,-6.536672,-7.112186,0.015908,-3.327713,-8.626206,0.440119,-9.944490,7.374851,0.620384,0.753517,-8.847244,1.361114,-8.735792,4.658400,9.747191,-3.197987,6.925744,4.565894,-8.353936,-9.841621,-6.019119,-5.834318,3.341568,-1.238512,-2.420056,-8.220627,2.035008,-5.523288,6.873549,3.275481,2.002493,6.226211,-7.951276,7.174138,-5.716597,4.424074,9.110466,6.243492,9.930532,9.065980,-2.862327,6.957093,2.659315,7.969315,8.873139,-6.292969,-0.160059,-2.485825,-2.274485,0.050557,0.613481,7.177690,-1.616849,0.533895,1.243277,-6.810133,5.402140,7.066720,6.558508,2.296009,5.669406,7.994120,4.598850,-2.362922,-0.804026,5.378714,-9.229436,-3.705666,8.706487,4.927809,6.160353,-0.386615,5.705506,2.585646,-4.130994,0.313911,-1.932414,2.162847,-8.083894,-9.793391,-6.314852,-0.792814,-0.101355,0.330607,4.370238,-9.732421,-5.374649,4.826891,1.159451,6.668279,3.706424,8.375232,3.186728,-0.141257,0.344383,-9.013301,-6.637843,-0.151248,-2.911064,-4.301741,-0.645696,-8.479836,-5.008258,-6.506923,-7.756208,7.080008,8.402110,-4.239002,-6.903239,-0.885498,1.690911,2.883395,-1.515048,-3.436006,3.166184,-7.705811,-7.677805,4.719600,-8.223405,-2.487378,2.730423,-2.548116,-4.344262,8.508175,3.200295,-8.733173,0.647036,-7.377483,-9.460013,-8.352932,-3.788130,0.638280,6.540383,7.740053,8.258927,-1.448077,0.478114,8.305045,8.910033,-2.029257,-8.158383,1.658880,-9.281634,2.602404,3.961204,4.936181,-4.848814,-0.870686,9.942225,0.523630,9.480399,9.825045,3.625740,-6.408975,5.473282,9.981708,-0.029148,7.399859,1.550595,2.013956,-3.319174,-7.244938,2.666481,-5.721551,-7.060600,2.360411,-1.652032,-4.443023,3.408491,-3.243797,-6.970921,0.462902,9.213521,7.334354,2.706183,2.229305,7.530772,8.211662,-2.792189,6.785950,6.436644,-9.399712,8.990192,3.429926,4.494826,-5.255141,-5.783876,-3.128303,-4.578043,-7.708768,-6.488694,-6.108720,0.276842,5.804555,0.719723,-2.747501,6.055942,-1.850781,1.952192,-0.252761,-7.287997,-7.516748,-6.738409,-9.361425,4.161862,-2.951435,-0.373764,4.053744,-9.511456,7.893772,-3.870029,4.806075,-7.246278,-9.260404,7.835643,-2.997927,4.663616,-8.717422,-6.921907,3.484770,2.759843,7.832090,-3.717599,1.536385,9.280663,-8.416224,-6.580188,-6.807190,-0.143902,9.069177,1.598304,7.419305,-2.308250,-6.065414,-3.435599,-5.087846,3.345498,5.687685,2.578264,2.351849,6.580649,-2.636411,7.476909,-6.927952,0.235841,2.265410,6.900273,-6.730950,8.782351,-3.328924,-1.221748,8.338923,7.163127,8.001157,-8.398727,8.595008,-6.502654,1.877641,-7.965597,3.809730,7.361333,-1.793868,8.939344,3.081063,5.423753,-5.900372,-0.835911,-0.896214,-4.788109,-9.036282,-8.896821,-5.776403,9.046398,-8.600338,6.972234,-9.419523,-4.346361,-1.120137,7.011522,-5.555518,9.262645,-7.606330,9.414309,8.791204,-6.264609,-3.349106,-3.628034,3.072660,-6.290673,3.656373,-6.454505,2.403902,8.522309,-6.399099,0.796590,8.385989,-5.386470,-1.008518,-1.771815,8.358558,-6.824622,8.376265,0.528484,-7.650252,-7.273790,8.946341,7.902564,-4.926875,-6.049598,5.578491,5.845360,6.914241,-4.185083,2.506007,6.917189,7.243563,-8.891256,-6.110885,-5.262992,-4.364567,7.326794,9.031829,-8.010796,2.685331,-1.781007,-2.833620,3.621969,8.127549,0.797010,9.209813,-3.795324,-0.244970,3.670146,-2.084611,-1.591115,6.170854,-2.399746,-5.712844,-9.766767,-6.139531,7.956332,-3.518381,-7.404698,-2.508736,8.880531,-7.361189,1.831477,-6.528754,-2.879364,-9.392683,2.723657,-0.815100,-1.843253,-0.899140,-3.360425,8.163878,2.171916,-0.056617,-0.060847,-2.812447,-4.667795,5.350597,9.202278,3.838518,-4.773641,-2.930989,0.237456,0.572283,-1.457816,-4.741972,-6.731461,-5.892423,2.018727,9.755778,7.000196,1.312506,0.418245,1.452658,0.117457,-1.335198,-6.282902,1.525441,7.364346,2.514625,0.248544,-6.780720,-5.263779,1.588114,7.703748,2.806374,-0.419309,8.709498,5.690531,8.714811,1.309278,-5.241561,-9.528818,2.541646,-5.673556,5.652722,-6.506481,-9.732031,-3.351089,-0.927945,-8.845961,8.396273,2.002995,-6.039849,4.902868,3.402360,6.336614,5.424604,8.112536,1.242499,0.519212,7.678841,-9.315759,-9.877984,-8.624444,3.097903,-8.408984,4.184819,2.392321,-8.293566,2.138649,9.063890,8.371072,3.859280,7.347870,5.184437,3.483973,-2.840198,-5.171762,5.693585,0.621003,4.514522,0.166972,0.337730,3.834263,2.856322,5.779349,6.978184,4.847401,-9.363624,-2.300055,-1.091645,-5.454749,5.650248,3.749219,8.496853,4.698684,2.937769,-2.830455,9.075157,-0.589790,-8.331861,9.143792,0.329144,-3.678718,9.951426,6.600228,6.409491,-7.761481,-2.399842,1.492614,4.800504,-9.611146,6.579444,1.031817,-3.958083,9.716836,-0.872946,8.286193,-4.957380,7.096335,-4.002723,6.741149,-6.780791,-5.219072,6.873974,8.473905,2.060022,6.517768,-3.157766,8.955554,9.388679,0.355238,-0.713059,3.323010,5.458053,-6.373336,9.164449,5.959979,-1.633745,-5.803254,5.568717,-8.306231,4.031057,8.792654,-7.695254,1.832225,6.194571,7.926517,8.346943,-4.091741,7.646326,-6.295601,-8.883427,6.709658,9.009649,3.918641,8.332066,4.738622,5.964844,-2.543514,-8.365750,0.934895,-3.229717,8.498212,4.953273,-9.288062,-9.772463,1.704030,-1.039368,3.063629,-8.240516,-0.797334,-1.050376,9.825485,-4.516717,-0.785187,2.694155,1.495185,-9.579470,6.709127,-9.261853,6.334134,-7.197534,-4.492282,6.413172,-7.245495,-8.018778,9.889484,2.962409,-3.191966,-6.712657,-9.359705,2.153196,9.927591,-2.916779,9.331923,0.851460,3.492489,-9.293486,-6.308382,-7.225677,3.028873,-0.303622,3.876057,1.499512,5.195700,-3.502196,4.892369,1.680838,-8.975055,5.580060,0.060697,-4.336044,-6.281213,-2.215035,-3.601173,-0.512294,8.684632,-3.795733,-6.603408,-0.537108,4.356771,3.302432,-8.862907,5.766945,-2.677748,9.380997,9.839228,-5.405287,-2.137958,0.693077,6.150044,-5.207416,-0.806357,-4.783855,1.922444,-9.890844,6.880673,9.383425,0.143688,-9.995699,-5.503609,4.891849,1.551614,8.781798,-7.733569,-4.846995,-3.253999,-1.347210,4.700864,4.043895,1.100488,3.924454,4.114569,9.334232,-4.341847,-3.923381,8.424534,-2.173534,-1.282729,-9.841638,-1.973568,-8.370256,3.480051,6.083872,0.577320,8.635284,4.092043,-0.872909,-5.152188,1.527494,6.979584,0.784337,1.415053,-0.510160,7.741310,-2.691616,6.587341,8.946213,1.987530,-2.533890,6.840873,2.189953,-8.801141,-5.481655,4.956355,5.480482,4.960708,0.989250,6.471420,-1.299903,-9.251742,-4.827039,-3.104630,3.625915,0.130351,-9.375831,1.050198,4.429478,7.003521,-7.892623,0.634970,-8.289027,-4.646971,9.646749,9.947242,6.797403,-7.246803,2.194162,9.830437,-7.403542,-5.996250,5.518391,-5.132640,-7.798754,-7.833197,0.555611,-0.246287,4.985137,1.592270,-6.786447,-6.751239,3.404174,-4.172051,9.068746,0.672325,-2.802924,2.314009,7.769913,-9.610915,9.449341,2.133484,-4.812474,-4.888487,-3.883439,-2.508336,-5.541966,-2.515604,2.781753,9.803844,-5.593710,-9.622256,-9.400716,0.435299,5.115186,9.293016,-9.035712,4.946632,7.931426,-0.275851,-0.750433,-3.702489,-4.012100,-7.759543,1.111283,-2.579805,-7.737860,-7.873365,-1.758371,-1.335987,3.175110,1.349506,-3.013548,-2.940138,-6.233209,-8.572356,9.655300,-3.147063,6.723423,1.874517,-8.275770,8.448128,-4.101622,7.579037,8.014678,4.025748,-6.706177,-8.028991,5.612262,-1.854337,-4.681297,-4.992727,5.983965,1.148494,4.831303,-2.685731,-1.767265,-5.478069,6.194163,-3.566695,-0.855461,-3.234578,-9.436163,7.605646,1.717106,4.908608,-5.380156,-3.928872,-3.829607,2.688917,-8.777888,4.830350,0.646884,-2.835223,-8.910000,0.351357,-7.573612,2.673749,-3.176027,-3.126695,-9.774514,5.338759,-9.554597,-0.159083,5.943052,-6.885885,1.041359,7.945945,-2.637739,-2.865662,-4.889818,2.951648,6.156221,9.456358,3.201323,3.668581,7.283337,5.430398,-4.973580,2.783028,3.153154,-8.776030,9.302554,0.507314,4.769389,-2.947775,6.940904,-4.296135,-8.934627,-8.972053,7.538065,4.520116,2.680549,-8.212882,4.242510,2.484666,-2.987790,7.889081,0.787383,7.964448,-6.305364,-8.879253,8.489758,-4.739210,-4.190715,9.189830,7.816880,2.897714,6.556641,-4.002527,7.234404,3.917317,7.151612,6.512751,0.755944,0.808938,9.071475,7.476765,-5.524443,-6.822416,2.591878,1.193303,8.676786,3.114756,-7.575879,5.401125,3.001036,6.524061,6.670800,-0.427167,0.289928,0.554231,2.575014,6.899343,-8.377649,0.021174,-0.931261,-2.491851,6.228466,-2.344861,-3.423291,0.548451,1.404744,-4.573946,3.668447,8.853622,9.559124,3.886163,-9.519791,-0.684812,0.246393,-1.643652,-1.512382,0.026893,-6.972988,-9.460718,6.941882,-2.955632,-7.072066,0.682715,1.135028,6.417355,4.029166,-7.543541,6.024906,2.941530,-7.411879,-7.041715,-6.546820,-2.588878,-0.881781,0.259610,-8.661041,-0.158868,5.958478,-4.660902,-2.537162,0.987191,6.791224,2.151908,-7.187244,1.308673,-8.957109,-5.539280,6.166317,9.071383,9.318825,2.339288,7.489102,-0.121432,4.138120,4.487203,-5.200246,-1.035283,-5.216420,7.943202,-9.488430,5.954225,-2.807152,3.512890,-2.203756,1.902012,-8.972044,4.033933,-6.032655,-7.829792,4.014358,-8.407998,-3.493810,7.662348,-4.401574,5.109244,2.197098,-1.980008,-6.005478,1.680197,-3.646543,-9.007293,3.257536,-5.791467,-9.729935,5.306084,7.373261,5.674349,-9.687048,-4.610192,2.069944,2.931196,1.253841,1.864197,-0.790849,-6.018072,0.356053,0.041905,1.071964,6.993185,-3.986548,2.742690,-9.816683,8.346719,0.465490,7.126696,4.063328,3.456506,-8.992769,6.200738,1.282937,-4.633858,-2.336542,9.318593,6.433884,0.584917,6.460221,1.374955,-8.151499,2.291159,2.901444,-8.338779,9.079319,4.017201,-4.108290,-8.980024,-8.508141,0.861473,-2.254500,-2.817610,9.539908,9.062358,-1.657788,-2.170594,0.420774,-2.637614,-3.765066,-6.539584,-1.795984,-6.232040,-6.072615,-7.414494,5.168717,9.239089,-9.771050,5.375845,-7.245393,0.476776,-5.444667,1.568270,2.189222,-3.301723,-9.637974,0.071707,-5.233585,-7.405320,1.354663,1.390448,-2.889131,-4.189694,0.415954,-9.761374,0.089912,-6.989919,2.418986,6.173598,-6.680647,-8.564668,-3.443541,3.025231,3.734766,3.720061,9.676621,5.757956,-5.536514,-3.239755,-4.560617,1.354810,-1.802899,3.285282,2.925002,-9.367164,-1.430774,-1.278178,3.102375,1.895535,8.597348,4.362286,8.663212,-1.917966,-0.139186,5.837568,9.208397,-3.554966,9.787009,8.664297,0.155902,-5.090260,1.053890,-1.460998,-0.489690,3.105941,3.035249,-8.475429,-9.558187,-0.712115,-3.954682,0.934939,-8.647673,1.146918,8.188217,-9.062839,3.041503,-8.500779,1.778905,3.700179,-3.652488,-0.582204,5.659256,-9.162305,8.884717,-9.696024,2.321157,-5.130263,-8.552914,2.564522,-2.840569,-0.683244,-7.461845,-0.360223,8.126766,0.973302,3.492146,3.275917,6.093442,-2.123406,-6.529151,-5.062627,-4.683255,4.213629,-3.140362,-4.399402,-8.797688,-8.956153,3.288835,3.798950,-0.662018,-8.366052,-2.190961,-1.866252,8.338089,-2.922087,-5.540267,1.564719,7.296534,0.240399,7.047584,2.910450,-4.435421,-6.499977,-6.945750,-1.015723,0.895242,-4.743944,8.451743,3.456168,7.284660,-2.892479,-8.254614,-2.265948,7.744769,4.302859,8.047455,-9.524739,8.657648,3.402252,-4.926680,-3.071905,-7.694570,0.820157,-2.210110,3.322624,6.632138,9.220537,5.307007,9.917235,3.830036], dtype = "float32")#candidate|4455|(1680,)|const|float32
var_4456 = relay.var("var_4456", dtype = "float64", shape = (720,))#candidate|4456|(720,)|var|float64
call_4454 = relay.TupleGetItem(func_4366_call(relay.reshape(call_4430.astype('bool'), [14, 3, 14]), relay.reshape(const_4455.astype('float32'), [1680,]), relay.reshape(var_4456.astype('float64'), [720,]), relay.reshape(uop_4440.astype('bool'), [14, 3, 14]), ), 1)
call_4457 = relay.TupleGetItem(func_4371_call(relay.reshape(call_4430.astype('bool'), [14, 3, 14]), relay.reshape(const_4455.astype('float32'), [1680,]), relay.reshape(var_4456.astype('float64'), [720,]), relay.reshape(uop_4440.astype('bool'), [14, 3, 14]), ), 1)
output = relay.Tuple([uop_4440,call_4444,var_4445,const_4446,call_4454,const_4455,var_4456,])
output2 = relay.Tuple([uop_4442,call_4447,var_4445,const_4446,call_4457,const_4455,var_4456,])
func_4458 = relay.Function([var_4445,var_4456,], output)
mod['func_4458'] = func_4458
mod = relay.transform.InferType()(mod)
mutated_mod['func_4458'] = func_4458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4458_call = mutated_mod.get_global_var('func_4458')
var_4460 = relay.var("var_4460", dtype = "float64", shape = (90,))#candidate|4460|(90,)|var|float64
var_4461 = relay.var("var_4461", dtype = "float64", shape = (720,))#candidate|4461|(720,)|var|float64
call_4459 = func_4458_call(var_4460,var_4461,)
output = call_4459
func_4462 = relay.Function([var_4460,var_4461,], output)
mutated_mod['func_4462'] = func_4462
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4484 = relay.var("var_4484", dtype = "float64", shape = (14, 5, 4))#candidate|4484|(14, 5, 4)|var|float64
uop_4485 = relay.log2(var_4484.astype('float64')) # shape=(14, 5, 4)
output = uop_4485
output2 = uop_4485
func_4489 = relay.Function([var_4484,], output)
mod['func_4489'] = func_4489
mod = relay.transform.InferType()(mod)
mutated_mod['func_4489'] = func_4489
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4490 = relay.var("var_4490", dtype = "float64", shape = (14, 5, 4))#candidate|4490|(14, 5, 4)|var|float64
func_4489_call = mutated_mod.get_global_var('func_4489')
call_4491 = func_4489_call(var_4490)
output = call_4491
func_4492 = relay.Function([var_4490], output)
mutated_mod['func_4492'] = func_4492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3682_call = mod.get_global_var('func_3682')
func_3683_call = mutated_mod.get_global_var('func_3683')
call_4525 = relay.TupleGetItem(func_3682_call(), 0)
call_4526 = relay.TupleGetItem(func_3683_call(), 0)
output = relay.Tuple([call_4525,])
output2 = relay.Tuple([call_4526,])
func_4528 = relay.Function([], output)
mod['func_4528'] = func_4528
mod = relay.transform.InferType()(mod)
output = func_4528()
func_4529 = relay.Function([], output)
mutated_mod['func_4529'] = func_4529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_4627 = relay.TupleGetItem(func_4130_call(), 1)
call_4628 = relay.TupleGetItem(func_4132_call(), 1)
var_4629 = relay.var("var_4629", dtype = "bool", shape = (14, 3, 14))#candidate|4629|(14, 3, 14)|var|bool
bop_4630 = relay.subtract(call_4627.astype('float64'), relay.reshape(var_4629.astype('float64'), relay.shape_of(call_4627))) # shape=(14, 3, 14)
bop_4633 = relay.subtract(call_4628.astype('float64'), relay.reshape(var_4629.astype('float64'), relay.shape_of(call_4628))) # shape=(14, 3, 14)
output = relay.Tuple([bop_4630,])
output2 = relay.Tuple([bop_4633,])
func_4638 = relay.Function([var_4629,], output)
mod['func_4638'] = func_4638
mod = relay.transform.InferType()(mod)
mutated_mod['func_4638'] = func_4638
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4639 = relay.var("var_4639", dtype = "bool", shape = (14, 3, 14))#candidate|4639|(14, 3, 14)|var|bool
func_4638_call = mutated_mod.get_global_var('func_4638')
call_4640 = func_4638_call(var_4639)
output = call_4640
func_4641 = relay.Function([var_4639], output)
mutated_mod['func_4641'] = func_4641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3746_call = mod.get_global_var('func_3746')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_4652 = relay.TupleGetItem(func_3746_call(), 0)
call_4653 = relay.TupleGetItem(func_3747_call(), 0)
func_1647_call = mod.get_global_var('func_1647')
func_1651_call = mutated_mod.get_global_var('func_1651')
var_4663 = relay.var("var_4663", dtype = "float64", shape = (90,))#candidate|4663|(90,)|var|float64
const_4664 = relay.const([False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False], dtype = "bool")#candidate|4664|(216,)|const|bool
call_4662 = relay.TupleGetItem(func_1647_call(relay.reshape(var_4663.astype('float64'), [9, 5, 2]), relay.reshape(var_4663.astype('float64'), [9, 5, 2]), relay.reshape(const_4664.astype('bool'), [216,]), ), 2)
call_4665 = relay.TupleGetItem(func_1651_call(relay.reshape(var_4663.astype('float64'), [9, 5, 2]), relay.reshape(var_4663.astype('float64'), [9, 5, 2]), relay.reshape(const_4664.astype('bool'), [216,]), ), 2)
var_4666 = relay.var("var_4666", dtype = "float64", shape = (14, 10, 14))#candidate|4666|(14, 10, 14)|var|float64
bop_4667 = relay.floor_mod(call_4652.astype('float32'), var_4666.astype('float32')) # shape=(14, 10, 14)
bop_4670 = relay.floor_mod(call_4653.astype('float32'), var_4666.astype('float32')) # shape=(14, 10, 14)
func_3682_call = mod.get_global_var('func_3682')
func_3683_call = mutated_mod.get_global_var('func_3683')
call_4674 = relay.TupleGetItem(func_3682_call(), 0)
call_4675 = relay.TupleGetItem(func_3683_call(), 0)
uop_4676 = relay.cos(bop_4667.astype('float32')) # shape=(14, 10, 14)
uop_4678 = relay.cos(bop_4670.astype('float32')) # shape=(14, 10, 14)
func_373_call = mod.get_global_var('func_373')
func_377_call = mutated_mod.get_global_var('func_377')
call_4682 = relay.TupleGetItem(func_373_call(relay.reshape(const_4664.astype('bool'), [3, 9, 8]), relay.reshape(const_4664.astype('bool'), [3, 9, 8]), ), 1)
call_4683 = relay.TupleGetItem(func_377_call(relay.reshape(const_4664.astype('bool'), [3, 9, 8]), relay.reshape(const_4664.astype('bool'), [3, 9, 8]), ), 1)
func_3975_call = mod.get_global_var('func_3975')
func_3978_call = mutated_mod.get_global_var('func_3978')
const_4686 = relay.const([-6.004940,8.509944,-8.434686,6.564864,6.215478,-1.245673,-0.532938,2.202083,-6.838366,-8.616758,-8.212418,-0.630395,0.944436,-2.830502,-6.665311,4.162189,-2.205498,-7.043879,0.900135,5.436761,-7.815410,-0.445059,-7.099680,-9.229103,-8.012950,7.192102,-9.322279,-5.490647,5.557052,-7.518043,-8.330031,-3.103962,1.451714,4.021349,-3.138456,8.921753,-8.934171,1.235207,7.887297,0.382599,-3.656242,-4.190395,6.972671,-8.689542,2.144233,-6.372321,3.047313,-3.387754,-6.592393,7.925619,-1.203961,1.856149,1.235342,3.528973,-8.488643,-5.616746,5.700811,7.653807,7.947185,4.938300,0.665407,7.995483,-4.633779,9.911646,9.014551,8.615047,9.828229,4.773447,5.762383,5.480128,6.782759,-6.266164,-6.224599,9.933333,-4.502677,-7.496585,7.126718,-5.232035,9.605452,-7.665200,-5.094933,7.426891,-5.617081,-7.661230,1.684842,4.259227,1.085202,-9.139240,1.064490,-2.753088,-1.729117,7.991054,-4.316582,-5.371808,7.532526,-7.058616,-0.433824,7.681544,-6.219675,1.245495,9.030885,5.685045,-1.138209,-9.413162,9.351960,8.619042,4.630694,0.713103,-4.411949,-6.277375,-8.515808,-1.931302,-7.966767,2.336683,2.464433,-7.590991,3.943409,-1.225176,3.579945,-0.687671,0.060334,6.672611,-3.145960,-0.757823,-3.081603,3.421198,5.092584,3.258321,0.193950,1.996040,4.441120,-8.609438,5.391019,8.015450,5.686893,7.363023,4.513034,-1.865721,-9.651727,0.129637,8.314413,7.558859,-2.496735,-9.310753,-0.597611,-9.687010,9.662761,-5.945066,9.522434,-3.143285,9.041389,6.736902,-6.737078,8.635068,-5.884508,3.520223,9.003301,4.565411,9.211991,6.795286,3.777827,-3.007307,-4.839873,9.982785,-3.892884,3.363792,5.050559,-0.105559,-6.280952,-4.547796,-3.356198,-0.565372,7.605631,9.873421,8.853355,-0.089468,9.063386,3.377281,3.654117,8.668495,-1.841606,-1.364974,-8.506600,6.910081,-1.054324,2.245652,9.413237,-9.029641,4.280225,-9.927329,-4.121205,5.223200,6.465597,-6.612560,7.771656,-4.588245,-8.274303,-0.914416,1.860892,3.619122,3.339098,7.872908,-0.252857,0.737365,2.433540,-5.436099,-2.065585,8.472765,-5.109453,6.477290,-8.550328,-8.061593,-6.314712,4.048761,-2.102412,5.103160,9.794462,1.560546,-0.522411,-0.532102,-8.810965,1.762644,-8.467048,-6.938182,-6.579669,6.280802,3.140198,1.935770,-2.439594,8.910467,1.301569,-1.935914,9.371860,-0.068520,1.274080,-4.737569,8.031284,-1.094378,-9.376286,7.562882,-3.509784,5.358754,-9.370922,0.006247,2.751266,0.739707,6.311619,-9.205183,1.802428,-9.870801,5.093070,-1.612226,6.066221,-8.358780,9.125246,-7.569274,-4.271618,7.801508,8.379639,9.889731,-5.142941,3.668368,9.911306,-5.603165,7.195442,3.362300,8.745771,2.362299,-6.399208,8.088861,9.517226,-7.136886,9.416688,-9.932887,-8.674405,-4.075320,2.130517,4.536633,8.396849,7.709018,-9.879193,0.428616,1.079941,-5.954238,-8.271948,1.731373,-3.020534,-5.225702,-1.965946,-5.670591,-7.413607,9.816223,-5.778606,-9.486958,-1.086414,-4.042507,-4.493565,5.470658,4.146494,-3.125866,3.930212,9.280271,4.077011,5.301884,2.862962,-3.245588,-5.901936,6.357912,-4.164740,-9.515816,3.022183,-4.977043,-4.760549,6.956154,2.066706,-4.852234,-9.416061,-6.764103,4.434931,1.817683,1.623944,-1.559869,3.307096,8.732094,-3.873166,-5.306429,-5.577060,1.845725,-2.211678,-4.047326,-3.303861,-9.121113,2.300325,-7.990093,7.615601,9.482233,-6.077739,-0.889632,9.121409,4.160015,-2.810926,4.460560,-7.947439,3.675356,-1.733804,6.208840,-6.501919,5.831345,-1.564772,-0.866999,8.664086,0.634271,-6.758852,7.447872,2.058798,4.650324,-6.152706,-1.761605,8.436605,-8.609161,-8.113033,1.072029,0.728453,-5.959252,-3.353135,6.572245,-7.056907,8.270925,3.050200,-4.498863,-6.833261,-4.545215,-3.984599,0.776276,-7.752769,5.119092,9.759451,-4.637618,6.302332,0.664533,0.534663,0.452154,7.696810,-8.327359,6.570693,4.476839,-6.935032,6.597131,-9.575365,6.684256,-9.979265,8.676263,4.097103,-1.838283,-2.185234,-4.886386,0.915221,4.459969,2.466900,8.009197,-4.703399,-6.279094,-4.310562,-8.074467,-7.530897,8.257882,-1.165979,0.574909,-4.352439,9.925165,3.935367,1.113517,9.239501,6.742010,-1.368156,-5.345776,6.156126,-5.064412,-7.711526,-4.978810,-9.646039,1.745166,8.804365,-2.415892,-3.959998,-7.627335,1.808098,-6.507961,0.111601,5.353300,-8.592976,-4.292442,-5.061710,9.091548,1.603680,-4.639986,-9.791653,8.183642,-0.070821,5.210065,8.353856,-7.026404,2.161046,8.765687,-2.714309,8.918606,-0.557445,-9.962719,-1.492042,2.063194,2.632572,0.966245,4.705161,4.684353,-6.910604,6.531396,1.341662,-8.121618,-1.677766,6.080088,2.912579,-0.909227,-6.576609,-2.772395,-7.124091,0.897682,6.709648,9.705797,3.700092,-9.135578,-5.524671,7.008868,0.530904,-1.974093,9.515333,-4.784944,-7.219843,6.922954,9.333996,3.943456,8.182231,-5.927554,6.925482,-2.284820,-3.208781,-2.010786,-8.696992,-1.492201,-5.267778,6.102053,-3.038869,-7.670130,-2.402090,-7.341597,2.783030,-0.846239,-7.336860,-4.226277,-1.891753,-8.207139,2.207920,4.053433,-1.294048,-1.343571,1.395332,-4.095148,9.663163,-9.717835,-1.958575,-2.219335,5.559119,1.888697,5.212584,1.985183,-0.952814,-1.841206,9.964694,6.945757,-6.637549,-7.164885,7.923426,1.217966,7.282890,6.999122,-6.163295,7.372353,-6.344327,0.352065,-7.936341,4.048480,-7.618952,7.278729,-2.915341,6.562574,-9.024284,-7.773770,6.782192,-0.864144,1.193972,-8.978029,8.897531,6.738501,-7.901850,6.706146,-6.605436,2.937703,6.843639,-6.885039,9.551730,-6.245547,7.958915,-7.272755,-2.911105,4.100505,-2.127292,-8.965150,4.492875,2.938588,-8.224326,6.109006,7.930836,-6.053977,3.205274,-6.660622,-3.042634,-8.032663,3.314768,-7.697670,3.649535,-3.043340,-7.600934,-3.028320,-6.007648,6.914590,-1.979595,4.294888,-2.928557,-1.140686,-0.939694,-9.506306,1.387304,-7.330443,3.169217,6.581597,-0.320213,-5.447504,-7.098941,3.267885,-3.618954,8.020045,3.254136,3.055880,-8.313597,1.393852,-3.324972,-8.363819,-3.922487,1.157778,9.415255,-3.349906,-9.302875,-0.737455,5.293344,0.026578,8.339796,7.606069,-1.713595,-2.725266,-5.273152,4.150872,6.480943,3.073060,7.364362,-0.486059,6.284154,-6.475959,9.179873,-4.756671,-2.217318,6.769935,-6.189616,-7.550201,6.558725,-5.517863,-8.958753,-0.510481,1.648010,3.818885,-8.467862,1.214029,4.237960,9.690840,6.965605,9.709377,-0.432211,6.455028,5.539149,5.958688,-4.495747,3.995556,4.535503,-2.238530,1.415740,7.384455,6.632955,7.987097,0.632019,-1.962718,-9.346483,-4.677756,-6.702926,6.124036,-0.812424,-6.388890,-0.185024,6.450138,3.192718,-5.310433,-9.233994,4.193108,5.773804,-3.718517,8.616712,3.260849,-5.609084,-7.806472,9.955780,9.456514,-5.355335,-1.915733,4.738448,2.666628,1.068967,4.758418,1.394702,-1.862176,8.512177,2.188272,0.466955,-2.358643,1.243111,-7.227045,-5.466213,-5.580777,8.850515,-8.885636,-5.709841,4.480288,7.393370,1.054515,3.953755,7.332398,-5.834101,-6.373193,2.945418,-4.510273,6.368282,3.111010,-6.686156,4.632530,-7.673233,-2.917845,8.792735,4.098877,-1.889765,9.372129,-7.011552,-3.900355,-8.969984,-6.417851,9.413536,-0.317221,9.240770,-9.701735,8.988570,5.207461,4.526606,-0.212137,1.216508,-9.478670,8.223327,-3.059742,-4.694164,-2.659350,5.123587,7.526681,6.804758,8.557297,7.934837,-3.528431,4.804401,3.281245,1.761022,4.142629,3.463991,-8.673371,-9.278907,-6.521738,1.723088,9.503321,9.443270,3.826687,-0.287581,8.718945,2.448226,-1.647079,4.964490,3.160129,7.795032,0.933720,-3.395100,6.825286,-1.506235,-2.806761,5.884971,-2.796321,-9.948571,0.269320,2.941574,-3.107962,4.672268,2.760229,-3.027960,9.267554,-7.382259,-7.264463,8.520642,3.833550,7.114020,4.136173,5.053553,3.865380,-1.249204,-1.408362,7.867123,-4.738570,4.041870,5.181693,-1.128355,7.940628,-4.162773,-9.602155,-9.140508,1.605562,9.718310,-9.743603,9.527123,-1.303304,-6.946117,5.189342,6.837848,-0.293886,5.791461,7.532664,7.194348,-6.749118,-4.251977,7.854200,-5.613340,2.495736,2.436707,-5.376633,0.041283,-1.457636,9.399386,-3.712888,3.180596,3.269225,-0.007269,7.822483,-0.464347,5.042985,-3.188149,3.539349,-7.974746,-0.786413,-1.111788,-6.792603,4.845078,8.888654,-0.504484,9.577393,3.991940,-0.843808,7.271136,4.519448,-8.422374,5.542993,6.050269,1.172797,1.600318,4.237338,6.824937,1.399273,1.333580,0.102000,-5.497576,7.052031,-6.280053,-9.459615,9.794144,9.018997,-2.156810,-8.930327,3.036675,8.369984,1.576386,-8.271470,-5.550742,1.948707,-9.994998,4.561513,-3.902514,-9.389095,8.176430,-7.473634,-5.048080,-4.814936,-1.227327,-7.170187,-4.059592,-1.743651,9.800191,-5.980178,3.278294,5.533853,2.263116,-6.649723,6.717391,-9.128964,2.854956,-8.114468,-9.289282,1.384048,6.175965,-9.811733,2.949984,-8.535882,9.196022,2.220563,-3.130060,-9.325858,0.397341,1.394162,-7.050657,3.611774,3.308858,0.245820,-8.087935,-7.140940,6.371908,-3.184442,-2.888268,2.676760,1.612063,-3.381890,4.330804,3.958286,6.242102,1.160609,-1.276029,-0.735514,-0.137884,2.049954,-5.834061,2.901588,-4.766813,-9.733501,-6.412662,-4.612691,-2.165809,5.924528,-6.615314,9.701519,-4.694524,4.239085,1.704855,-6.239425,4.470908,0.412570,3.869420,8.523734,-1.696251,-6.071036,8.583595,-6.611072,4.258310,1.027741,0.240263,-8.764977,-1.486541,-6.730270,0.419644,9.716803,2.484962,-3.553614,3.527180,-0.160701,4.888355,-2.407266,-2.355627,4.503868,3.296030,8.954175,0.903246,-2.450263,5.900907,5.840140,4.449601,6.189352,0.060671,6.321225,-6.122532,-2.581347,1.380113,-7.928662,-1.238202,8.941289,6.559451,-4.801861,-1.613607,-1.973961,3.891900,-8.327899,-7.876432,4.040337,6.736090,2.798852,3.530945,-4.207953,-7.551039,-9.584364,-7.660531,-2.757054,-5.336666,-2.899302,3.735576,-1.411735,-5.998623,1.030131,-0.627391,3.568211,-8.261435,7.716050,-6.699947,-0.370937,9.715006,6.577817,-1.807470,7.330575,-7.334838,-7.365386,-3.789600,4.724407,8.181792,7.890115,1.755008,-1.609080,6.732480,0.412040,0.131918,5.150780,-4.761742,-1.365704,-1.722756,8.932958,1.779920,8.091998,-6.216343,-8.735195,7.787409,-6.631730,-1.063813,-9.637054,-5.261983,-6.433835,4.501328,-9.658614,-7.890328,3.312147,-6.987482,-1.430900,-7.629946,2.572473,-7.495250,-2.181033,-3.523529,-2.545853,4.402504,-9.982588,4.974781,6.060359,-3.865896,-4.724945,-5.148266,-3.581980,8.582542,-6.435036,-6.845864,-2.654360,-4.138736,-4.804554,8.124662,6.470368,-1.132670,4.334547,-6.346233,-4.351742,-4.213779,-0.791124,-6.830573,-8.515902,3.769493,0.890373,-6.583564,-2.975567,6.686050,6.203551,1.465570,0.612034,4.960992,2.123296,-4.370504,-1.861183,2.040917,0.452933,4.520112,0.616263,7.939055,-0.928376,-4.873507,-7.149578,-9.359214,8.984283,-6.311113,1.216400,3.842899,-0.879499,-3.646321,-5.639670,1.063284,-2.026083,9.965963,4.165547,-8.177258,8.925477,-9.901925,-9.715525,2.962492,-0.703360,4.250134,7.841706,9.681176,-6.446530,2.940758,6.547072,-1.583770,9.044473,5.245697,-1.749129,8.668532,-6.841840,0.303259,-9.101103,-3.585625,4.988601,-8.015808,-0.995284,-8.500268,9.939132,-8.302738,-0.236883,-3.325002,-2.514554,-7.502569,-7.516892,-7.603069,7.784975,4.132246,5.833887,-9.717572,5.836280,1.565613,-1.906882,-2.359556,7.665560,-5.796780,-6.077368,-8.967740,-7.770970,3.641746,-1.978715,-8.902762,-3.767881,6.953816,6.598262,-9.964421,-6.783280,9.669566,9.892676,-2.086166,-7.987908,-3.668263,-3.403584,5.522642,7.148476,7.404148,8.226159,6.698910,6.932832,6.491116,-9.109879,-5.116074,5.142372,-9.459531,3.165359,-2.747274,0.405051,-2.142727,8.742283,7.743720,0.300949,-7.207108,-1.348797,-0.220237,-9.384337,-4.860574,3.000191,1.739282,-7.524835,1.796459,-2.216640,9.060324,-2.470856,0.424141,-5.236105,-0.923419,3.685559,-6.659573,-5.925897,-2.795393,-3.141846,7.086935,8.743928,-4.532531,-3.992059,0.641339,2.929154,2.102363,3.136468,6.941081,0.888211,6.139873,-9.186163,-1.390714,-7.378827,6.071631,9.538340,-2.842334,4.714397,9.028805,-3.242842,9.274277,8.463548,5.655643,6.263526,-0.454528,-5.773832,-6.589051,5.905002,8.292800,2.974002,-6.712578,9.822105,5.420058,-3.964081,2.384692,0.326230,-0.894159,5.470919,0.928065,6.352387,7.531177,4.409980,-5.046490,-1.028974,-1.285207,5.983256,-9.042338,0.163455,9.658872,-9.712226,-6.351930,3.364507,4.791532,-2.615357,-0.984199,-9.349808,5.083965,2.858695,5.942258,6.953889,2.232985,-5.756930,-4.632629,2.585415,6.403568,-9.266859,0.701371,9.188851,-2.468767,-5.897164,4.535238,-5.838924,-3.909461,-5.840814,0.836185,-6.807602,-0.161125,-2.865885,-6.857562,3.206329,-5.118065,-6.230479,7.674498,-1.397079,2.036130,-1.352333,2.060505,-1.899822,-0.693396,7.829999,-8.183267,-9.426474,8.973702,3.602043,-1.075591,4.468417,-2.857212,4.381100,3.648050,4.570727,-4.315710,0.728011,-0.376393,1.986984,0.823493,-0.316360,-4.266979,-8.009279,-1.629690,-2.842210,-8.669978,2.340438,5.376541,6.136555,-0.608953,4.182521,-9.429855,-7.284224,-6.719677,-6.211976,4.517553,-0.344836,3.297445,7.136799,-0.855548,1.188205,4.747913,-6.875122,9.600391,-4.737247,-8.752633,-0.098696,-0.561797,-2.713816,-0.527903,-8.952771,1.087604,-2.069903,-2.917959,-9.055300,4.415804,7.058578,-5.828418,7.413294,3.197264,2.860707,1.739553,5.531198,2.948563,9.483517,-2.558228,0.465163,-9.588809,-2.838394,8.231377,3.530021,-1.515037,6.581787,-6.555835,-6.107997,-9.648011,-4.716631,6.749551,-5.036081,4.666377,3.347706,6.081659,2.041089,-7.636133,-6.002049,7.960524,-2.255516,7.478985,-5.462936,-4.743495,4.260012,8.978887,-0.501715,2.722883,2.413920,-8.480120,-6.187966,9.246081,0.217109,-7.402830,2.939268,-9.895132,4.706078,0.439945,0.988460,9.724799,6.697000,-7.832124,9.122943,-6.742496,-5.171540,2.492183,-0.433173,7.168044,-3.871494,-9.849750,8.658042,0.167947,-3.452536,-7.900368,-5.851707,-8.083226,-1.774593,-8.347273,8.808955,-1.863340,2.747395,-2.542049,-4.240908,-3.616546,2.736067,-1.230625,7.706856,-6.099988,3.957005,0.521352,-9.550163,9.721879,8.104341,-1.095277,-8.002235,-2.533160,7.612557,4.368140,-8.141566,-3.316650,-3.913209,-1.579446,3.009335,6.043928,-3.472428,-4.909472,3.888606,2.162675,0.702476,1.511768,8.585341,-2.552453,-2.292233,-2.290382,5.199594,8.691933,-3.622347,1.219826,-4.509618,-4.019048,7.736153,8.852033,-6.122391,8.394832,-4.158610,8.062303,6.452217,-0.016139,7.650349,-7.120288,-8.297681,8.580482,-6.085547,-9.639239,3.104547,0.282910,5.342243,8.415259,1.201688,-0.383511,6.245067,5.475086,0.937636,0.140492,7.596726,1.719610,4.733277,-4.091551,8.744968,-0.818819,9.186506,9.899804,-7.461891,-5.693775,-1.283345,0.859336,-7.741050,-0.090555,4.134597,-1.556118,9.469211,-0.492482,-9.683293,-3.833118,2.000438,2.706575,-7.981277,8.883782,3.087166,9.359499,-8.247067,-3.258412,7.089854,-2.821595,-2.336712,6.573477,-1.902186,-4.396242,-3.855312,-0.513259,1.973045,-8.380730,6.410499,-3.193191,3.537349,-6.018396,-8.387370,-1.005573,2.284411,-7.710610,-3.692610,5.705264,1.365733,5.099453,9.798206,8.949161,1.185795,-3.870296,-5.342671,-1.264044,-6.588278,1.696436,1.832130,5.094451,8.970605,-6.442105,7.397497,-2.465248,0.655302,4.570814,-2.417047,1.092601,-2.004344,-5.181264,-9.019158,9.719705,2.080938,9.013416,-7.760923,2.261154,3.862651,6.742412,4.793635,2.551784,-8.940990,5.813805,-0.552414,-2.533182,5.238223,5.266726,8.947904,-0.616466,8.264252,2.413075,-0.322404,1.501004,-1.758728,2.967747,4.354106,-9.702883,2.045319,-9.673558,-4.394231,-7.542188,1.145169,1.659823,-3.241661,6.585377,-8.286133,-0.544392,7.001796,-5.554238,-0.412556,5.043153,-1.926974,9.619421,-5.375919,4.133636,4.870937,-8.456201,0.567022,0.371160,3.743221,-3.975990,-4.237524,2.276249,-1.521396,9.555023,7.447145,-6.097973,4.439337,1.672053,4.193142,-6.304609,-1.025043,5.300417,3.469246,-0.877162,8.263889,-7.907835,7.256743,1.114794,0.340694,-4.972609,-4.956128,-4.411308,9.744356,5.207568,6.371647,7.524939,-2.016157,0.449392,8.184755,-5.687937,-7.891930,-2.929379,-4.302497,-7.028915,2.166327,-2.259256,5.569399,7.303137,-2.803731,-1.630945,-4.808715,-5.489056,-6.278642,-0.826094,8.564850,3.643965,1.738054,4.727941,2.515488,0.282508,-5.637895,-8.977958,6.040753,-9.725007,-4.483629,5.944079,-9.691875,0.650854,8.854458,4.333517,3.235865,9.776586,-2.028878,-0.911642,-8.115983,-2.452052,-2.388393,-9.234443,-6.725424,8.299614,6.622749,-6.735992,-4.072525,4.847243,7.135632,-5.267338,6.502676,-7.895445,-7.590813,5.464448,-6.277771,-2.498576,0.793818,-2.520158,9.449498,-1.664805,-1.943175,1.382435,8.837028,7.336387,9.240823,7.215272,1.649123,-4.233415,-6.931004,-7.407209,-0.125690,7.116044,5.985633,1.761473,-0.568820,-5.816048,-2.282119], dtype = "float32")#candidate|4686|(1680,)|const|float32
call_4685 = relay.TupleGetItem(func_3975_call(relay.reshape(const_4686.astype('float32'), [1680,])), 3)
call_4687 = relay.TupleGetItem(func_3978_call(relay.reshape(const_4686.astype('float32'), [1680,])), 3)
output = relay.Tuple([call_4662,var_4663,const_4664,call_4674,uop_4676,call_4682,call_4685,const_4686,])
output2 = relay.Tuple([call_4665,var_4663,const_4664,call_4675,uop_4678,call_4683,call_4687,const_4686,])
func_4702 = relay.Function([var_4663,var_4666,], output)
mod['func_4702'] = func_4702
mod = relay.transform.InferType()(mod)
mutated_mod['func_4702'] = func_4702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4702_call = mutated_mod.get_global_var('func_4702')
var_4704 = relay.var("var_4704", dtype = "float64", shape = (90,))#candidate|4704|(90,)|var|float64
var_4705 = relay.var("var_4705", dtype = "float64", shape = (14, 10, 14))#candidate|4705|(14, 10, 14)|var|float64
call_4703 = func_4702_call(var_4704,var_4705,)
output = call_4703
func_4706 = relay.Function([var_4704,var_4705,], output)
mutated_mod['func_4706'] = func_4706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_4716 = relay.TupleGetItem(func_2930_call(), 0)
call_4717 = relay.TupleGetItem(func_2931_call(), 0)
uop_4720 = relay.log(call_4716.astype('float64')) # shape=(14, 1, 14)
uop_4722 = relay.log(call_4717.astype('float64')) # shape=(14, 1, 14)
uop_4725 = relay.sqrt(uop_4720.astype('float64')) # shape=(14, 1, 14)
uop_4727 = relay.sqrt(uop_4722.astype('float64')) # shape=(14, 1, 14)
func_4366_call = mod.get_global_var('func_4366')
func_4371_call = mutated_mod.get_global_var('func_4371')
var_4733 = relay.var("var_4733", dtype = "bool", shape = (588,))#candidate|4733|(588,)|var|bool
var_4734 = relay.var("var_4734", dtype = "float32", shape = (1680,))#candidate|4734|(1680,)|var|float32
var_4735 = relay.var("var_4735", dtype = "float64", shape = (4, 180))#candidate|4735|(4, 180)|var|float64
call_4732 = relay.TupleGetItem(func_4366_call(relay.reshape(var_4733.astype('bool'), [14, 3, 14]), relay.reshape(var_4734.astype('float32'), [1680,]), relay.reshape(var_4735.astype('float64'), [720,]), relay.reshape(var_4733.astype('bool'), [14, 3, 14]), ), 2)
call_4736 = relay.TupleGetItem(func_4371_call(relay.reshape(var_4733.astype('bool'), [14, 3, 14]), relay.reshape(var_4734.astype('float32'), [1680,]), relay.reshape(var_4735.astype('float64'), [720,]), relay.reshape(var_4733.astype('bool'), [14, 3, 14]), ), 2)
bop_4741 = relay.less_equal(uop_4720.astype('bool'), relay.reshape(uop_4725.astype('bool'), relay.shape_of(uop_4720))) # shape=(14, 1, 14)
bop_4744 = relay.less_equal(uop_4722.astype('bool'), relay.reshape(uop_4727.astype('bool'), relay.shape_of(uop_4722))) # shape=(14, 1, 14)
bop_4756 = relay.right_shift(uop_4720.astype('int32'), relay.reshape(call_4716.astype('int32'), relay.shape_of(uop_4720))) # shape=(14, 1, 14)
bop_4759 = relay.right_shift(uop_4722.astype('int32'), relay.reshape(call_4717.astype('int32'), relay.shape_of(uop_4722))) # shape=(14, 1, 14)
bop_4762 = relay.equal(bop_4756.astype('bool'), relay.reshape(uop_4720.astype('bool'), relay.shape_of(bop_4756))) # shape=(14, 1, 14)
bop_4765 = relay.equal(bop_4759.astype('bool'), relay.reshape(uop_4722.astype('bool'), relay.shape_of(bop_4759))) # shape=(14, 1, 14)
uop_4769 = relay.asin(uop_4725.astype('float32')) # shape=(14, 1, 14)
uop_4771 = relay.asin(uop_4727.astype('float32')) # shape=(14, 1, 14)
bop_4779 = relay.bitwise_and(uop_4725.astype('uint8'), relay.reshape(bop_4762.astype('uint8'), relay.shape_of(uop_4725))) # shape=(14, 1, 14)
bop_4782 = relay.bitwise_and(uop_4727.astype('uint8'), relay.reshape(bop_4765.astype('uint8'), relay.shape_of(uop_4727))) # shape=(14, 1, 14)
func_2798_call = mod.get_global_var('func_2798')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_4812 = relay.TupleGetItem(func_2798_call(), 0)
call_4813 = relay.TupleGetItem(func_2799_call(), 0)
bop_4815 = relay.subtract(bop_4756.astype('uint16'), relay.reshape(bop_4762.astype('uint16'), relay.shape_of(bop_4756))) # shape=(14, 1, 14)
bop_4818 = relay.subtract(bop_4759.astype('uint16'), relay.reshape(bop_4765.astype('uint16'), relay.shape_of(bop_4759))) # shape=(14, 1, 14)
output = relay.Tuple([call_4732,var_4733,var_4734,var_4735,bop_4741,uop_4769,bop_4779,call_4812,bop_4815,])
output2 = relay.Tuple([call_4736,var_4733,var_4734,var_4735,bop_4744,uop_4771,bop_4782,call_4813,bop_4818,])
func_4821 = relay.Function([var_4733,var_4734,var_4735,], output)
mod['func_4821'] = func_4821
mod = relay.transform.InferType()(mod)
mutated_mod['func_4821'] = func_4821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mutated_mod.get_global_var('func_4821')
var_4823 = relay.var("var_4823", dtype = "bool", shape = (588,))#candidate|4823|(588,)|var|bool
var_4824 = relay.var("var_4824", dtype = "float32", shape = (1680,))#candidate|4824|(1680,)|var|float32
var_4825 = relay.var("var_4825", dtype = "float64", shape = (4, 180))#candidate|4825|(4, 180)|var|float64
call_4822 = func_4821_call(var_4823,var_4824,var_4825,)
output = call_4822
func_4826 = relay.Function([var_4823,var_4824,var_4825,], output)
mutated_mod['func_4826'] = func_4826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4252_call = mod.get_global_var('func_4252')
func_4253_call = mutated_mod.get_global_var('func_4253')
call_4840 = func_4252_call()
call_4841 = func_4252_call()
output = call_4840
output2 = call_4841
func_4858 = relay.Function([], output)
mod['func_4858'] = func_4858
mod = relay.transform.InferType()(mod)
output = func_4858()
func_4859 = relay.Function([], output)
mutated_mod['func_4859'] = func_4859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2798_call = mod.get_global_var('func_2798')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_4860 = relay.TupleGetItem(func_2798_call(), 0)
call_4861 = relay.TupleGetItem(func_2799_call(), 0)
output = relay.Tuple([call_4860,])
output2 = relay.Tuple([call_4861,])
func_4888 = relay.Function([], output)
mod['func_4888'] = func_4888
mod = relay.transform.InferType()(mod)
output = func_4888()
func_4889 = relay.Function([], output)
mutated_mod['func_4889'] = func_4889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mod.get_global_var('func_3065')
func_3067_call = mutated_mod.get_global_var('func_3067')
call_4917 = func_3065_call()
call_4918 = func_3065_call()
const_4924 = relay.const([[[6,2,3,3,-2,2,-7],[-8,9,4,-3,-9,-8,-5],[1,-8,4,-2,-3,-10,-8],[-9,-1,6,9,1,-4,10],[-1,10,4,3,-7,-6,-2],[7,3,6,1,5,-1,-1],[-5,6,5,-2,-5,-9,-9],[-7,3,2,-8,-9,-8,10],[-9,4,-3,3,-8,8,-7],[-10,-2,-9,8,3,8,8],[8,-7,10,-2,4,2,-10],[7,-7,-8,-1,6,-8,9],[2,-4,-5,7,4,8,-7],[-10,-1,8,4,-7,-1,-6]],[[3,-7,-3,3,-3,3,2],[-3,-4,-7,10,2,-9,8],[-5,1,2,-3,10,-4,8],[8,1,-10,6,1,-3,1],[4,-6,-6,7,4,2,5],[6,-5,5,8,2,-3,2],[-8,9,-2,10,-1,-5,-4],[10,-7,3,1,-10,3,4],[7,-1,-1,-6,5,-3,3],[-3,9,8,-8,-7,-9,7],[-1,8,-9,2,1,-2,-5],[5,5,5,-9,-9,4,-5],[5,4,7,5,-5,5,-8],[-4,-4,-9,7,2,-6,3]],[[8,-2,-4,-10,-2,-4,-5],[-3,-5,-6,-6,-7,-8,8],[-3,4,9,-6,-6,-3,-5],[-3,5,3,-5,-1,3,-3],[-9,7,-2,-3,8,-5,8],[-1,4,-5,-4,-10,-9,-9],[9,5,4,1,-2,-8,-6],[5,2,8,3,-6,-2,-3],[9,3,-7,7,-10,-9,5],[-5,2,-6,7,10,-5,-5],[7,8,-4,-4,-9,2,1],[2,-9,-8,6,-5,8,-10],[-4,-2,5,-6,10,9,3],[9,-1,4,7,-10,8,5]],[[-1,-8,4,-7,-9,7,3],[9,5,3,-8,-7,1,-9],[3,2,2,10,-2,-4,-9],[8,-7,1,-4,2,-3,8],[-6,-10,4,-4,6,2,-10],[6,-7,5,-3,8,1,1],[6,-8,10,-3,4,9,-9],[5,-7,-3,9,-10,2,-2],[-5,9,-6,-8,-6,1,6],[1,2,9,9,6,7,2],[2,-4,-9,-2,1,3,1],[-9,-3,6,-6,-5,-6,3],[-6,3,-1,9,-2,-6,3],[10,3,-2,-10,4,-3,1]],[[9,-3,10,-5,4,10,-4],[-9,-8,-10,-8,9,-9,2],[-1,1,8,7,9,9,-5],[-9,7,-8,7,-8,-10,-1],[-8,-3,7,-1,6,-2,-9],[10,10,-4,9,2,10,1],[4,9,6,-3,5,-7,-9],[8,8,3,-9,-4,9,-4],[-5,6,-6,3,8,6,-9],[6,2,7,4,-9,-7,1],[9,2,10,-3,-5,-10,-4],[6,-9,-3,-6,2,-8,-3],[4,-10,1,8,10,-10,10],[7,8,7,-4,10,-1,-10]],[[-3,-6,8,3,6,3,-5],[-10,-4,-10,10,10,10,-6],[2,1,-10,6,3,-1,1],[6,6,-10,2,-3,-7,-6],[2,-7,-7,-2,5,7,7],[6,2,3,-7,8,-3,2],[3,9,10,-10,4,6,-9],[-7,10,6,5,-2,4,-4],[1,1,5,-9,-5,4,10],[9,4,8,1,-8,5,1],[-9,8,-4,-4,-6,6,4],[1,1,-5,-7,-8,9,5],[7,-3,2,6,8,-4,5],[-6,-1,2,6,-4,-2,-1]],[[2,5,1,-4,7,10,-2],[-10,4,5,-2,7,4,-2],[8,7,9,-9,-8,-5,5],[-10,2,1,5,-1,-2,-6],[-2,5,2,-9,-4,1,-1],[8,-4,10,-8,1,-6,-2],[-3,-7,7,-4,-3,-7,-9],[-8,-7,-4,-5,-6,-7,8],[-1,4,-9,10,4,-2,-7],[4,9,6,-10,-8,7,10],[3,9,-10,-10,5,-6,2],[-6,9,4,-3,8,5,10],[2,-5,-10,8,7,-3,-8],[1,-7,8,6,5,-6,-5]],[[-9,-2,5,-5,-2,-6,-3],[-1,-8,-10,9,10,-3,7],[8,-10,-4,-9,10,5,8],[-10,2,3,-6,-4,4,10],[-9,-7,-8,-5,7,-1,-7],[-8,-10,10,-4,2,10,6],[-10,-1,3,9,5,4,-5],[1,-3,-8,1,-5,-3,-4],[-2,6,7,4,-7,3,-4],[-6,-4,-2,-5,-10,-10,-1],[9,-3,6,-5,-9,4,10],[8,6,5,-10,-7,-7,3],[-1,10,10,2,-5,10,8],[9,-3,1,8,9,3,5]]], dtype = "int32")#candidate|4924|(8, 14, 7)|const|int32
bop_4925 = relay.add(call_4917.astype('float32'), relay.reshape(const_4924.astype('float32'), relay.shape_of(call_4917))) # shape=(8, 14, 7)
bop_4928 = relay.add(call_4918.astype('float32'), relay.reshape(const_4924.astype('float32'), relay.shape_of(call_4918))) # shape=(8, 14, 7)
output = bop_4925
output2 = bop_4928
func_4932 = relay.Function([], output)
mod['func_4932'] = func_4932
mod = relay.transform.InferType()(mod)
mutated_mod['func_4932'] = func_4932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4932_call = mutated_mod.get_global_var('func_4932')
call_4933 = func_4932_call()
output = call_4933
func_4934 = relay.Function([], output)
mutated_mod['func_4934'] = func_4934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_4943 = relay.TupleGetItem(func_2930_call(), 0)
call_4944 = relay.TupleGetItem(func_2931_call(), 0)
output = relay.Tuple([call_4943,])
output2 = relay.Tuple([call_4944,])
func_4951 = relay.Function([], output)
mod['func_4951'] = func_4951
mod = relay.transform.InferType()(mod)
mutated_mod['func_4951'] = func_4951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4951_call = mutated_mod.get_global_var('func_4951')
call_4952 = func_4951_call()
output = call_4952
func_4953 = relay.Function([], output)
mutated_mod['func_4953'] = func_4953
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4985 = relay.var("var_4985", dtype = "bool", shape = (6, 8, 14))#candidate|4985|(6, 8, 14)|var|bool
var_4986 = relay.var("var_4986", dtype = "bool", shape = (6, 8, 14))#candidate|4986|(6, 8, 14)|var|bool
bop_4987 = relay.logical_or(var_4985.astype('bool'), relay.reshape(var_4986.astype('bool'), relay.shape_of(var_4985))) # shape=(6, 8, 14)
func_1721_call = mod.get_global_var('func_1721')
func_1726_call = mutated_mod.get_global_var('func_1726')
const_5005 = relay.const([3.124692,5.843139,2.025457,4.722175,-4.398620,-0.975636,0.776340,0.178156,-2.605362,0.816425,2.658115,-9.722526,1.411197,4.647972,2.281152,2.423115,4.295768,-7.697113,-5.643537,-6.235951,5.873912,-7.563345,4.780217,6.849810,1.071303,9.593576,-9.414898,5.262043,-9.368976,9.613868], dtype = "float64")#candidate|5005|(30,)|const|float64
const_5006 = relay.const([5.945958,5.367887,9.518093,-7.985534,-2.052935,3.570317,-1.865219,0.528267,0.080917,-0.757550,-2.837475,-3.022425,-9.257411,-0.176800,-5.424241,-1.216811,-7.479969,7.511001,-3.099205,-1.191452,8.660501,-7.155536,-0.646518,6.303202,1.254801,-3.417437,6.718020,-1.075223,-5.963001,7.620182,-4.250565,-6.186114,4.515047,-4.503456,9.346612,-3.382573,0.567762,-6.670330,-4.938692,9.529098,2.091190,-4.734216,-3.236128,1.492429,6.422196,5.430025,-8.645579,-6.906293,-9.551099,3.953326,2.941054,-1.320223,3.705250,6.092117,-3.659531,4.138521,-3.340334,8.912527,-0.814167,4.333824,0.558496,-7.377554,-8.093389,-5.536293,2.511389,-2.984669,7.777226,3.014376,7.116348,6.873051,-6.392672,7.820455,-7.028945,7.936798,4.313064,-7.236573,-4.335135,2.048666,-9.819029,5.895519,2.287603,-4.604133,-7.389658,5.883074,-5.256079,0.289162,6.529548,9.934112,7.052428,4.382062], dtype = "float64")#candidate|5006|(90,)|const|float64
const_5007 = relay.const([True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True], dtype = "bool")#candidate|5007|(216,)|const|bool
call_5004 = relay.TupleGetItem(func_1721_call(relay.reshape(const_5005.astype('float64'), [6, 1, 5]), relay.reshape(const_5006.astype('float64'), [90,]), relay.reshape(const_5007.astype('bool'), [216,]), ), 1)
call_5008 = relay.TupleGetItem(func_1726_call(relay.reshape(const_5005.astype('float64'), [6, 1, 5]), relay.reshape(const_5006.astype('float64'), [90,]), relay.reshape(const_5007.astype('bool'), [216,]), ), 1)
output = relay.Tuple([bop_4987,call_5004,const_5005,const_5006,const_5007,])
output2 = relay.Tuple([bop_4987,call_5008,const_5005,const_5006,const_5007,])
func_5012 = relay.Function([var_4985,var_4986,], output)
mod['func_5012'] = func_5012
mod = relay.transform.InferType()(mod)
var_5013 = relay.var("var_5013", dtype = "bool", shape = (6, 8, 14))#candidate|5013|(6, 8, 14)|var|bool
var_5014 = relay.var("var_5014", dtype = "bool", shape = (6, 8, 14))#candidate|5014|(6, 8, 14)|var|bool
output = func_5012(var_5013,var_5014,)
func_5015 = relay.Function([var_5013,var_5014,], output)
mutated_mod['func_5015'] = func_5015
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5017 = relay.var("var_5017", dtype = "float64", shape = (10, 14, 7))#candidate|5017|(10, 14, 7)|var|float64
uop_5018 = relay.cos(var_5017.astype('float64')) # shape=(10, 14, 7)
func_4702_call = mod.get_global_var('func_4702')
func_4706_call = mutated_mod.get_global_var('func_4706')
var_5036 = relay.var("var_5036", dtype = "float64", shape = (90,))#candidate|5036|(90,)|var|float64
const_5037 = relay.const([3.146323,-9.156672,-1.108791,-3.357144,3.116937,4.214557,6.091365,-5.071647,0.447806,2.057578,-9.771247,1.345127,-7.584527,1.696829,6.895624,9.865333,3.026711,-2.397100,-0.417306,-1.140007,0.134599,2.138205,3.055813,-1.619884,5.269980,1.475692,-1.693871,-2.700945,3.974916,4.482133,1.116065,8.759906,-0.001544,-8.843436,4.532348,-2.640425,1.420132,3.657832,4.646835,8.719655,5.623899,-2.592674,5.168521,-3.482594,9.710578,-5.282824,-7.097928,3.408872,5.850709,9.603379,-6.976417,9.205708,7.104029,-3.041545,-6.710144,-5.419186,-4.156531,-6.268015,2.411323,-2.413638,-5.092312,6.071524,0.331579,8.422369,0.932640,3.821516,-0.710329,2.828131,9.775608,-4.240991,8.523538,3.137655,-9.457160,3.546135,-3.266854,-5.111472,-0.306388,2.995613,-0.374492,5.653053,9.878095,6.603915,2.075372,-4.351111,-1.892297,0.898997,0.428279,-8.594012,-0.959528,8.965402,0.809033,1.497720,-0.584002,5.348439,1.314712,-5.348647,4.113455,-4.565685,-2.310856,5.461932,6.727671,-8.914413,8.155093,-5.887486,-1.213009,-9.011012,5.869791,-8.905278,-6.871924,-3.807466,-0.807843,2.288982,-6.790205,-8.632194,-8.971418,-6.872724,-7.060700,-0.373926,5.781766,8.610710,-2.134002,7.510201,8.529580,1.497656,-5.300973,2.578719,-6.953204,-5.599106,-5.320031,5.642791,3.864513,6.797050,-1.943390,8.954917,-3.591108,-4.900527,6.044470,1.854770,2.010615,-1.365589,-7.133537,-9.956787,-2.552494,-7.946471,5.400684,9.991392,0.006568,4.837787,-2.790399,2.456069,6.162619,-7.798811,9.720577,-3.581513,-4.769812,-9.725350,-0.056008,-5.972526,-0.418334,-1.057022,-8.055747,-7.182085,-3.337915,-7.702096,-4.908327,5.308981,1.132769,-2.757785,7.874604,1.675412,-0.622291,8.294533,-0.381775,0.500034,-0.891546,-5.271171,-6.603822,-1.242562,-0.234609,5.658650,-0.660153,1.913675,-9.775252,-6.559950,-4.747523,-2.964169,-5.181959,8.503364,6.375478,2.025759,-2.458815,-5.112372,-3.642733,3.607689,8.271711,9.053832,-6.032226,0.072364,4.207905,-6.362229,5.297951,-2.825419,-9.335271,-5.797436,-6.527892,7.873528,-4.160111,9.610773,-1.222185,3.779292,-0.342380,5.951818,8.555825,8.252171,9.156831,-0.868185,-1.256225,-8.664825,8.255883,-8.650775,-8.324224,-6.532015,-8.768031,6.564862,3.582646,-8.293262,2.130357,-2.951339,6.461357,6.820888,0.789181,3.268984,-1.882747,1.741595,8.324855,-1.253800,5.853303,-2.663708,-7.066897,0.996332,-7.123153,1.879940,2.240770,7.352461,-1.611579,2.182603,-3.101672,5.289536,-9.568880,-5.163857,9.308640,7.074197,-8.521963,-3.142769,4.509109,-0.329040,2.774261,-4.525447,6.892060,4.158929,-8.485536,6.113813,-1.026274,-6.128095,2.026861,-0.652723,1.619128,-0.246582,9.221352,-5.233830,-1.973516,-2.723922,2.098947,-8.139863,-3.141402,-8.290482,6.238141,-2.906838,-5.993140,-7.442703,4.003280,-3.592970,1.738997,-9.437512,0.870287,8.909844,9.665454,-1.582038,-6.083107,9.191876,-4.468011,-8.981068,-0.761584,8.056602,4.334191,-0.590209,-9.094158,5.030538,7.419669,-1.718268,-7.136110,-5.894456,-2.425426,-5.375375,-9.820454,9.352891,9.902385,-1.912551,-8.772024,2.961647,2.639221,0.212533,-5.698742,1.719860,-9.183885,2.414557,-7.554610,1.659356,-5.894557,6.124079,5.613378,2.076980,-9.692444,-0.738390,-3.443783,-1.521603,-6.291554,7.217475,-6.391344,-3.518337,3.618656,-3.504138,-5.519488,-8.586660,1.682027,6.621404,-5.243211,-1.211172,-3.665823,-6.919692,-4.079341,-1.805226,-8.507464,1.843280,4.995985,1.849060,7.267906,-0.444775,3.056930,-0.402145,-6.651524,-3.664491,0.989279,-0.006478,0.833402,-4.919604,1.221076,-1.477039,-6.244407,1.112949,-3.040842,-3.422454,-6.750102,7.420770,8.559140,-2.942214,5.574262,0.164869,8.265566,-3.861526,-3.609550,-7.582090,8.736023,8.046212,1.930920,8.520199,0.749704,1.161670,-1.467838,-6.045215,3.155937,-7.357774,6.327933,7.794950,7.590963,6.161814,-6.262552,2.723852,9.934396,9.063711,3.853257,-0.962255,6.316000,-3.711769,-6.485893,0.976318,-9.053741,-8.876354,4.539155,-2.717003,5.004791,-4.856210,-9.971514,1.021635,-7.696399,-6.706220,-7.223524,5.185417,-7.568103,7.828610,-4.282581,-5.450469,-5.738050,-8.187581,-3.126248,-8.005617,-7.692382,1.768992,1.714482,-8.799277,-4.897636,0.918935,3.372524,-3.324749,8.746543,-9.409546,-9.029975,-2.494919,5.867983,3.766586,6.389873,3.534907,-9.363745,-6.768889,-0.018383,-4.189085,9.476101,3.836597,-0.297574,3.425815,0.489087,4.180188,-8.542152,9.778233,-1.878846,-3.855429,-2.218351,7.955327,-2.624905,-1.149007,7.220180,4.073321,9.896716,0.198079,-7.778559,4.328914,6.417049,-0.770807,-3.420492,3.584315,-0.978222,-9.148017,-1.744219,5.890431,-2.360525,6.452876,-1.888508,-2.737568,7.941648,3.513784,-2.356480,1.243573,4.353086,-7.007011,0.362762,-3.006219,4.097280,5.692945,4.458204,-0.537648,-8.793640,7.674376,0.388795,-8.496174,1.201887,-0.695576,-6.100279,9.824028,1.195861,9.449613,-9.107349,-7.148535,4.462324,3.047801,5.667221,-9.308048,7.375680,-2.296535,6.800051,3.608613,5.374596,5.635948,8.403447,9.562173,-3.605080,-0.569800,0.896260,-1.713900,-5.242129,0.758471,7.029079,5.494137,5.191965,0.793595,6.671710,4.117936,9.653489,-5.978108,-1.943448,1.419065,3.135339,6.739728,5.607235,5.540950,1.856619,0.359537,-1.139286,7.840507,-3.397200,-5.207275,5.410124,-7.199276,-8.508027,0.852342,4.839850,9.195831,-5.185656,4.809012,-8.953580,9.041163,1.737069,7.762601,-1.663292,7.342456,3.910339,-7.038853,2.678471,9.149961,8.066560,-8.769605,-9.767915,8.448184,-5.844658,-9.248756,1.685538,-3.763207,-4.468151,-7.549882,-5.818100,2.401416,-2.165332,-9.441354,4.169153,1.101025,2.156081,6.067673,-4.258095,-6.946124,0.276319,1.522207,0.549597,8.903913,7.392306,-9.256664,1.950483,-8.283082,0.307041,5.039466,-9.408867,2.259990,9.020147,3.988093,-1.209772,-0.598729,-6.239436,-6.918217,-2.085132,4.141347,-1.016162,4.570456,-3.183706,8.693963,3.610974,-8.935417,9.043861,1.974920,-1.099054,-2.885753,-6.876163,-5.961585,5.265256,-3.427986,-1.818577,2.854768,4.880051,-2.434900,-8.265810,7.548296,-4.947954,-1.778059,-9.156633,-0.124012,-1.107367,7.226209,-1.626826,-2.931274,-3.788901,5.853802,-7.255797,9.724328,6.146648,9.400413,7.652603,3.476219,-9.819384,-9.289004,6.556737,3.061982,5.366037,7.353640,-1.847633,4.841870,-6.285818,0.663263,-0.936166,6.706700,-7.280932,4.975467,2.377192,-2.078899,-2.698886,-8.580632,0.018757,-0.943996,-8.047983,-1.231490,8.606641,-7.755823,-0.807580,-1.522583,-3.712423,7.911838,8.845103,9.135902,0.274609,-7.509677,-6.938210,-5.742187,6.484282,-1.604537,-7.058881,-9.884660,5.232143,5.066604,0.318553,-4.961891,1.287844,-3.011702,-0.572816,-7.713374,9.095657,-1.775066,1.655123,-5.570331,3.581178,3.060774,3.629508,9.941624,-0.626286,2.275578,-0.517936,0.520818,5.371500,-2.395361,1.690730,6.006972,-6.368329,-6.882257,-6.505331,-7.923027,-3.337079,1.592667,4.327712,-1.987245,-6.615817,9.603335,5.430342,-1.507460,1.754572,-1.734600,4.994578,4.112312,0.029937,-2.705142,-1.685841,9.235279,-9.763220,8.390429,6.013203,6.874537,5.755960,2.439508,2.513150,2.525557,-3.171631,-0.236120,9.385375,4.814967,1.343940,7.017318,-2.052389,-2.494182,3.672812,2.048661,8.419758,-6.760555,9.551747,4.777391,-0.512125,3.242664,2.020873,-3.005890,-2.407486,6.970661,1.261455,8.407601,-9.950283,-2.327104,4.633044,-7.077394,-3.969280,2.830751,-9.956306,3.947417,9.364062,-8.879913,-9.058570,-4.421523,-6.859583,-8.250998,-8.587004,-9.314620,-5.615643,-3.106365,-3.180613,-1.238847,-8.410776,-3.328575,8.121265,9.577482,0.148721,2.136938,-0.861587,-1.029496,9.609351,4.128838,-4.673188,-8.111882,-1.048080,2.019207,-6.104638,-2.400266,3.197835,3.887002,-1.574800,-3.889492,-2.170798,7.423133,1.763367,-5.723700,-7.669043,-2.818047,0.924962,9.584566,5.938158,-1.951861,4.169262,-9.211647,2.309564,2.656883,-4.928033,8.324163,3.116693,-4.134632,-9.410789,3.871747,-5.385828,-2.732763,5.550518,1.510052,-4.361920,-5.147109,-4.396096,-9.169996,-3.314276,9.019230,7.563612,-3.093680,3.462982,8.152067,0.301153,8.864627,-7.757011,6.649248,9.872705,5.492408,-6.851386,0.549420,-0.458148,-1.478770,7.013086,-3.902760,2.205498,2.455882,9.691173,-4.260757,-1.255997,-8.046873,4.021836,-8.449603,-1.590663,-8.357682,5.115236,-7.907119,-0.798582,-6.892233,-2.851958,-7.544660,8.643831,4.066102,8.301504,0.923115,9.698373,-3.101473,3.799287,5.592810,-4.180506,-9.612301,-1.264692,-2.980634,-2.762322,-6.539323,3.696326,-8.747202,5.152800,0.207144,6.414361,-9.668968,-9.033779,-0.499252,8.529967,2.130755,3.731799,0.944435,-9.099168,-7.228742,-6.901396,-1.238769,-2.598555,2.763119,-6.394525,-6.289249,5.322506,-5.379115,7.998473,-4.119526,-3.123980,3.779378,9.118573,7.299666,-7.311171,-1.895594,5.618560,-9.045477,1.964920,6.950565,-0.645391,-9.229352,-9.417378,7.493066,5.973800,-7.088432,3.149261,3.200578,-0.790281,6.589274,1.890607,2.352388,-4.953079,-0.695271,9.480048,7.629813,8.155084,-2.891128,-8.545484,5.376572,4.597639,0.443780,1.092038,9.794501,-4.425297,-6.527631,0.173905,-3.128471,9.626111,6.021002,-5.092474,-8.753269,-1.491764,5.865068,-5.260498,-4.682239,-2.661770,9.978590,7.410136,0.868341,6.459788,3.101131,9.359211,-1.921893,-9.661407,-7.332780,-5.491568,-6.691428,5.770074,6.325895,-4.150005,0.555746,5.679065,7.118292,2.995482,-2.086890,-8.311857,0.797713,1.941194,8.122247,-9.571820,-3.057862,-5.948450,4.863979,-2.395467,-0.293363,8.876153,6.237924,-0.644471,6.607959,2.437994,-8.235249,1.475099,-4.332267,7.721827,-6.140248,0.419071,-2.658170,6.871475,2.573459,-4.144176,-2.726174,8.642735,-0.296234,-6.837408,0.123322,-7.561300,-6.348600,-0.408934,-1.210709,-5.148464,0.261480,-8.143445,2.693052,7.757069,0.424193,-9.676910,6.539128,-5.343173,9.275861,3.240424,-6.674576,-9.306483,1.799138,3.008600,-8.950554,-4.952751,9.169822,6.258652,-8.172609,1.081049,-3.245906,-0.676139,3.087690,-3.859413,2.139863,-7.260852,5.718473,-0.564480,1.717964,-7.776365,5.036756,2.604592,2.842199,-7.496363,1.142539,-4.292363,7.001011,-4.742197,1.581214,-8.184164,-8.219067,-8.505681,3.936206,0.045475,5.191436,6.224666,-5.561929,5.354482,1.247155,-4.172064,-6.227915,8.901118,1.387072,-6.558826,-6.451580,2.985919,3.115663,-5.949780,8.263477,1.632145,6.408430,1.107106,0.847070,-4.185656,-7.851542,-1.716234,8.963741,8.632402,6.424942,5.051306,-5.002471,-9.846599,-1.134944,-6.706290,-0.004412,-6.484781,-5.965370,-8.608852,7.076666,1.756953,4.590110,-8.953990,9.510716,2.413599,1.761472,-9.906128,7.601277,-1.963067,1.460591,8.444218,-7.952648,8.488807,-8.385859,3.912106,-3.038636,6.641088,-8.087752,-2.947528,1.393973,-0.023953,-2.770633,-1.027499,2.474065,-5.242023,-8.030728,0.652233,6.901848,6.254716,-5.658352,9.838845,6.702971,-4.428551,-3.068422,9.502424,-9.503755,5.085648,-7.488023,-1.606446,-9.942917,-0.193758,7.601512,8.306959,7.833146,-5.225741,2.370191,-5.108832,-8.939292,-0.575047,-2.782541,9.144228,1.493876,8.411572,-7.429058,-5.236822,-6.070203,6.031147,-2.327412,2.268012,-0.568178,1.206818,2.837212,-8.828913,-8.148948,3.116114,7.272851,7.258159,9.489593,-0.598673,-9.001052,-7.218248,-9.436949,-3.438796,-7.726242,-3.293176,5.589536,1.192231,9.922398,2.013821,-6.662177,-1.376477,2.094479,4.910932,9.422865,-8.568654,-3.221583,-4.026014,0.081334,0.050626,-3.868561,-8.723169,9.195008,6.219871,9.159400,-6.600907,9.387740,1.666289,-8.633528,3.206003,0.093697,3.668814,-9.014825,-0.747115,0.025800,7.549168,5.405635,5.482820,2.226369,6.541427,9.439020,6.565566,6.685246,0.904160,8.648924,0.710000,0.130436,-0.241410,-6.501405,3.885734,-0.907791,-5.927105,-1.399541,-6.208832,-3.964205,-4.770949,7.358690,-3.341296,7.380731,-0.755671,-7.321599,0.951250,-2.074186,1.855249,-2.104306,-3.105632,3.734441,-1.125129,6.199119,-4.463777,-0.320579,9.692851,-5.725547,-1.519117,-8.120743,-3.228553,-8.738648,-0.603921,5.198531,-9.455164,-5.974727,-4.203754,8.775508,1.598050,2.690610,-7.509863,-0.864985,3.945029,7.536944,-0.219224,-1.443391,-8.376818,-9.207879,4.303170,-4.624610,1.004892,7.579606,-6.580207,-4.009422,7.221183,4.913662,-3.660485,7.873826,-2.499460,8.179710,-5.220902,0.206589,4.552550,1.435456,0.445778,-0.797776,-7.796344,-6.881762,-4.980872,-8.735360,-1.048462,8.512268,-3.763483,-6.235975,4.924231,9.888293,8.554937,-7.583897,4.482082,-0.010784,7.265743,1.256672,-5.941690,-0.912727,1.570028,-0.316201,3.283314,-2.425755,-4.401272,-3.652230,-2.254393,-8.129415,0.734577,-9.024197,-0.506600,4.421736,1.203321,-6.990551,4.795602,-0.044768,3.624177,-4.780177,-8.397987,-8.592276,-9.819911,-8.084953,9.314126,-1.517348,8.543235,5.315851,3.011523,3.538260,4.879607,-0.151518,4.582807,9.481111,4.729356,0.327584,-4.474007,0.962682,-5.672140,-0.005336,-5.883113,-5.323947,5.627170,0.960556,6.847836,-6.165724,-3.979633,5.094521,7.014314,2.260483,-1.132922,2.970206,-0.119345,5.907302,-5.119140,-3.185401,3.902541,5.662101,-8.062565,6.706992,9.239075,8.813348,9.368067,0.440274,3.628581,8.042017,3.191573,1.439710,3.310018,2.491171,-5.850244,-9.825226,-6.886915,-6.894982,0.371394,-7.170164,3.302479,-0.209215,-3.028679,-9.896553,-5.461128,-3.715150,-0.806904,-6.884348,-6.828386,0.858856,6.870391,-8.157249,5.582865,7.748072,0.785306,-5.463431,5.404512,1.132359,-8.092015,4.931848,9.913344,4.410100,0.266762,-7.944824,2.981721,-7.098232,6.126749,-1.899071,-4.700438,6.133729,-3.929221,-0.240556,1.832312,5.542718,0.195633,-2.595835,-8.948676,-1.617517,5.245009,-5.667269,2.343158,-3.977944,7.205913,7.293137,-4.858082,3.081724,-5.845365,-8.432213,2.905093,-5.449661,-2.581152,-2.722540,-0.429111,0.538849,1.284682,-6.204411,-5.395132,5.042546,0.275919,9.163875,-0.828176,-1.394273,2.472573,-3.875177,0.267893,2.830900,1.764866,-0.020014,1.877936,-7.271513,8.093691,3.234851,0.014415,-1.886117,0.679105,-9.997098,-0.033333,9.152908,4.585015,1.807764,-5.054346,-0.405941,-5.897323,8.402918,-1.154744,-6.590065,-6.279915,-2.176972,-8.506759,-9.776886,-3.876317,8.502043,-8.876494,-7.113827,-9.921319,-7.750516,7.079564,9.107774,0.785312,8.256573,-2.510373,-3.684681,5.776582,-1.536370,7.870505,6.327726,6.706261,-9.248745,9.588017,0.096933,-5.717067,-2.830243,-4.634701,5.925526,-3.226663,-2.748448,-5.752534,4.087976,5.597961,-0.017695,2.796079,-2.276742,-9.611023,-4.417321,-3.037886,-8.841449,4.846324,-7.224522,-7.758357,7.484677,-5.551617,1.229476,-5.815362,-2.489502,-4.775180,-7.726289,-4.906056,-5.354793,-0.929489,8.781125,-8.369018,9.103668,-4.642408,4.804818,-8.386530,-7.014053,-2.789013,4.060063,-7.155276,-6.034407,-8.117139,-8.253770,-6.645026,-9.998186,8.410242,8.404928,2.147516,7.921147,-0.183819,-1.560319,-7.530248,0.792758,-9.778275,9.352915,-1.143572,0.380047,5.244278,2.808091,-5.582748,-3.791536,7.049679,6.589724,-6.678193,2.138277,5.918956,5.058547,-6.154331,0.286189,-2.264657,7.825442,-2.973253,2.886258,0.272218,7.377316,-3.323799,7.938318,8.508704,-8.412655,-7.784866,-9.505605,3.561874,1.548443,-8.009807,-8.176548,3.212399,8.126498,-2.098421,8.625547,-8.434976,2.861194,-3.269383,-6.456614,8.816608,-2.015319,-0.017435,-2.374154,-4.316098,1.881387,-1.199618,2.911817,-4.057068,9.745919,-6.554901,-5.720039,-8.280695,6.759123,-2.983102,-9.150319,1.190782,4.094975,-1.321910,0.638671,6.588790,6.751164,3.487410,-6.461287,-8.041586,-8.025201,-6.093899,8.020657,6.956497,-6.596223,-7.960924,8.026905,6.801837,-0.465542,-4.604566,-5.725262,-7.482166,9.967882,9.146408,7.706725,-2.120679,-0.751511,-6.708062,9.717878,-5.555121,-1.470454,-1.929747,-2.772825,-5.265908,6.104920,1.509093,0.675935,-6.593243,2.762392,-2.043242,0.296699,-5.464191,6.331638,5.330732,-1.233799,-1.511861,-7.126753,6.233441,-7.095961,0.436998,-4.858152,-6.534949,5.298268,9.971164,-7.070584,4.097156,-0.253780,8.943398,6.638580,-3.598750,-4.371566,-6.606839,8.739246,-6.748157,3.736215,-4.987442,-4.649386,1.519420,1.484275,-0.017676,-7.042002,0.598764,8.595201,1.407369,0.849553,2.005093,-3.263416,-1.033287,4.325671,-0.009873,5.855291,-2.121909,1.431717,6.612972,-8.143432,-3.670141,1.870242,1.896532,-8.077432,3.946700,-5.009886,7.374380,-5.941326,2.740513,-0.598131,5.561849,-0.973564,2.508113,8.834283,-4.490204,-2.185553,0.365235,-2.284074,3.985449,7.196697,-8.844293,5.986122,-5.477221,0.379986,5.355065,6.580207,0.766932,-9.254028,4.305799,1.774517,-0.604879,-2.414541,-2.088512,-6.632309,1.573589,-1.827722,-5.828057,-2.290041,-6.575206,-6.016530,1.660058,-2.377206,9.321587,-6.350134,-8.957143,-4.998042,1.264434,-2.597073,7.337748,0.540641,-7.035838,-4.080629,8.965305,-5.965327,-9.517332,3.204900,-5.550256,5.551792,9.915569,3.522484,5.855493,-1.058963,-4.784124,-8.808054,5.817337,5.508807,-6.158089,-2.712208,-4.092201,7.484432,2.791262,-4.192786,-7.050478,9.820673,0.044087,6.149116,-7.684468,-2.044965,5.787388,-8.299068,-4.443445,-2.571065,2.761856,0.707650,9.139858,3.312042,8.818675,3.272680,6.366581,8.720463,2.401596,8.646286,-8.841758,-2.532968,4.512555,1.089028,-5.990279,-9.174101,-0.535452,4.525018,-3.517241,8.081108,8.829323,9.560305,1.892205,7.587380,5.496772,8.897386,-5.182743,7.105603,-4.272401,-0.863698,4.398512,6.017621,-9.140792,0.727843,0.017376,-8.246544,6.635114,1.370406,4.038759,5.259855,0.641532,-4.421425,0.565674,1.404457,-9.630356,-4.899244,-0.983911,-6.385981,4.955631,2.799488,-9.848025,0.298280,9.272088,-4.366065,7.666841,-2.104014,-2.740365,1.054514,-3.130786,-7.078929,-7.828177,-8.870639,-8.454906,2.773901,5.962235,-3.613346,-8.223383,2.773632,-4.150030,-2.542841,-8.522039,-6.918293,-3.783840,-0.752841,1.294670,1.236199,1.720958,-9.467766,-3.448129,6.790838,0.927834,2.399781,2.416379,2.237592,0.396991,-9.137498,-5.212090,-4.694340,-8.698439,-3.067635,5.945435,4.136286,9.773429,-5.887032,5.555981,5.053986,4.896166,-0.855418,-7.717464,-8.620251,-6.645391,5.572222,-3.253201,4.849747,-6.251089,-3.244061,2.875717,-4.057760,9.960639,9.438267,1.560597,1.480305,3.438513,4.793489,-3.303603,9.682402,-1.623727,5.183752,7.993068,3.635710,-2.916878,6.749015,5.260191,0.105742,1.802713,7.277092,3.310500,6.986331,0.884610,-1.057171,7.148106,-5.650296,-5.118547,-9.577676,-3.252889,9.582010,2.560431,-9.445183,6.339261,5.844497,-6.087773,5.061235,-1.140024,7.979927,2.470502,9.463411,3.352590,8.006600,6.412645,3.526321,6.587868,1.365738,-6.651129,-7.127113,5.862663,-5.284320,-7.296656,7.877585,-9.811740,-6.143198,2.941677,-0.210849,3.775812,-7.711179,7.474840,-7.273484,1.649003,7.518306,-3.554445,5.225544,-2.270358,1.075401,6.306203,9.727213,5.979214,8.032957,0.631643,-5.748934,4.318528,9.818223,-2.591683,-7.772056,4.799422,1.400255,5.716150,9.506773,-3.638452,-7.741215,-2.891193,-5.810579,-2.340589,-6.867518,5.343411,-8.854332,7.123661,-4.501859,-7.795568,9.293056,-3.681011,9.802792,2.709246,6.592379,0.567395,6.357383,7.312933,-3.669963,-7.791671,3.927269,6.882985,-6.829029,-4.900847,-7.112782,3.653973,-1.861577,5.143995,3.278173,2.165846,-9.979843,8.415647,-2.962995,9.192411,-8.965025,9.269397,-9.133464,9.959444,0.167150,1.943405,-8.464633,-4.793483,-5.062926,-5.688496,-0.908430,6.892951,4.486012,5.873170,8.927571,-8.770503,-0.612705,-1.234548,-0.234360,5.523225,0.907751,0.553686,-4.749309,-8.817815,5.597739,-8.488635,-4.211103], dtype = "float64")#candidate|5037|(1960,)|const|float64
call_5035 = relay.TupleGetItem(func_4702_call(relay.reshape(var_5036.astype('float64'), [90,]), relay.reshape(const_5037.astype('float64'), [14, 10, 14]), ), 6)
call_5038 = relay.TupleGetItem(func_4706_call(relay.reshape(var_5036.astype('float64'), [90,]), relay.reshape(const_5037.astype('float64'), [14, 10, 14]), ), 6)
output = relay.Tuple([uop_5018,call_5035,var_5036,const_5037,])
output2 = relay.Tuple([uop_5018,call_5038,var_5036,const_5037,])
func_5043 = relay.Function([var_5017,var_5036,], output)
mod['func_5043'] = func_5043
mod = relay.transform.InferType()(mod)
mutated_mod['func_5043'] = func_5043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5043_call = mutated_mod.get_global_var('func_5043')
var_5045 = relay.var("var_5045", dtype = "float64", shape = (10, 14, 7))#candidate|5045|(10, 14, 7)|var|float64
var_5046 = relay.var("var_5046", dtype = "float64", shape = (90,))#candidate|5046|(90,)|var|float64
call_5044 = func_5043_call(var_5045,var_5046,)
output = call_5044
func_5047 = relay.Function([var_5045,var_5046,], output)
mutated_mod['func_5047'] = func_5047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_5078 = relay.TupleGetItem(func_4130_call(), 1)
call_5079 = relay.TupleGetItem(func_4132_call(), 1)
var_5089 = relay.var("var_5089", dtype = "bool", shape = (14, 3, 14))#candidate|5089|(14, 3, 14)|var|bool
bop_5090 = relay.bitwise_xor(call_5078.astype('uint32'), relay.reshape(var_5089.astype('uint32'), relay.shape_of(call_5078))) # shape=(14, 3, 14)
bop_5093 = relay.bitwise_xor(call_5079.astype('uint32'), relay.reshape(var_5089.astype('uint32'), relay.shape_of(call_5079))) # shape=(14, 3, 14)
output = bop_5090
output2 = bop_5093
func_5103 = relay.Function([var_5089,], output)
mod['func_5103'] = func_5103
mod = relay.transform.InferType()(mod)
mutated_mod['func_5103'] = func_5103
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5104 = relay.var("var_5104", dtype = "bool", shape = (14, 3, 14))#candidate|5104|(14, 3, 14)|var|bool
func_5103_call = mutated_mod.get_global_var('func_5103')
call_5105 = func_5103_call(var_5104)
output = call_5105
func_5106 = relay.Function([var_5104], output)
mutated_mod['func_5106'] = func_5106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_5108 = relay.TupleGetItem(func_4130_call(), 1)
call_5109 = relay.TupleGetItem(func_4132_call(), 1)
output = call_5108
output2 = call_5109
func_5115 = relay.Function([], output)
mod['func_5115'] = func_5115
mod = relay.transform.InferType()(mod)
mutated_mod['func_5115'] = func_5115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5115_call = mutated_mod.get_global_var('func_5115')
call_5116 = func_5115_call()
output = call_5116
func_5117 = relay.Function([], output)
mutated_mod['func_5117'] = func_5117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
call_5226 = func_5115_call()
call_5227 = func_5115_call()
output = relay.Tuple([call_5226,])
output2 = relay.Tuple([call_5227,])
func_5236 = relay.Function([], output)
mod['func_5236'] = func_5236
mod = relay.transform.InferType()(mod)
mutated_mod['func_5236'] = func_5236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5236_call = mutated_mod.get_global_var('func_5236')
call_5237 = func_5236_call()
output = call_5237
func_5238 = relay.Function([], output)
mutated_mod['func_5238'] = func_5238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2754_call = mod.get_global_var('func_2754')
func_2756_call = mutated_mod.get_global_var('func_2756')
call_5252 = func_2754_call()
call_5253 = func_2754_call()
output = relay.Tuple([call_5252,])
output2 = relay.Tuple([call_5253,])
func_5279 = relay.Function([], output)
mod['func_5279'] = func_5279
mod = relay.transform.InferType()(mod)
output = func_5279()
func_5280 = relay.Function([], output)
mutated_mod['func_5280'] = func_5280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4951_call = mod.get_global_var('func_4951')
func_4953_call = mutated_mod.get_global_var('func_4953')
call_5319 = relay.TupleGetItem(func_4951_call(), 0)
call_5320 = relay.TupleGetItem(func_4953_call(), 0)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_5325 = relay.TupleGetItem(func_4130_call(), 1)
call_5326 = relay.TupleGetItem(func_4132_call(), 1)
output = relay.Tuple([call_5319,call_5325,])
output2 = relay.Tuple([call_5320,call_5326,])
func_5350 = relay.Function([], output)
mod['func_5350'] = func_5350
mod = relay.transform.InferType()(mod)
output = func_5350()
func_5351 = relay.Function([], output)
mutated_mod['func_5351'] = func_5351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_5380 = func_3789_call()
call_5381 = func_3789_call()
output = relay.Tuple([call_5380,])
output2 = relay.Tuple([call_5381,])
func_5384 = relay.Function([], output)
mod['func_5384'] = func_5384
mod = relay.transform.InferType()(mod)
output = func_5384()
func_5385 = relay.Function([], output)
mutated_mod['func_5385'] = func_5385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2754_call = mod.get_global_var('func_2754')
func_2756_call = mutated_mod.get_global_var('func_2756')
call_5435 = func_2754_call()
call_5436 = func_2754_call()
output = relay.Tuple([call_5435,])
output2 = relay.Tuple([call_5436,])
func_5437 = relay.Function([], output)
mod['func_5437'] = func_5437
mod = relay.transform.InferType()(mod)
output = func_5437()
func_5438 = relay.Function([], output)
mutated_mod['func_5438'] = func_5438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5442 = relay.var("var_5442", dtype = "int8", shape = (9, 4, 3))#candidate|5442|(9, 4, 3)|var|int8
var_5443 = relay.var("var_5443", dtype = "int8", shape = (9, 4, 3))#candidate|5443|(9, 4, 3)|var|int8
bop_5444 = relay.minimum(var_5442.astype('int8'), relay.reshape(var_5443.astype('int8'), relay.shape_of(var_5442))) # shape=(9, 4, 3)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_5481 = relay.TupleGetItem(func_4130_call(), 0)
call_5482 = relay.TupleGetItem(func_4132_call(), 0)
output = relay.Tuple([bop_5444,call_5481,])
output2 = relay.Tuple([bop_5444,call_5482,])
func_5485 = relay.Function([var_5442,var_5443,], output)
mod['func_5485'] = func_5485
mod = relay.transform.InferType()(mod)
var_5486 = relay.var("var_5486", dtype = "int8", shape = (9, 4, 3))#candidate|5486|(9, 4, 3)|var|int8
var_5487 = relay.var("var_5487", dtype = "int8", shape = (9, 4, 3))#candidate|5487|(9, 4, 3)|var|int8
output = func_5485(var_5486,var_5487,)
func_5488 = relay.Function([var_5486,var_5487,], output)
mutated_mod['func_5488'] = func_5488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5437_call = mod.get_global_var('func_5437')
func_5438_call = mutated_mod.get_global_var('func_5438')
call_5496 = relay.TupleGetItem(func_5437_call(), 0)
call_5497 = relay.TupleGetItem(func_5438_call(), 0)
func_3423_call = mod.get_global_var('func_3423')
func_3424_call = mutated_mod.get_global_var('func_3424')
call_5502 = relay.TupleGetItem(func_3423_call(), 0)
call_5503 = relay.TupleGetItem(func_3424_call(), 0)
func_4419_call = mod.get_global_var('func_4419')
func_4422_call = mutated_mod.get_global_var('func_4422')
const_5505 = relay.const([-8.089552,-4.036527,4.166540,-7.565140,5.921177,9.363595,5.063855,-3.186123,-3.169846,-0.902618,-5.185347,9.722115,-3.717500,-6.417102,-0.164746,2.558841,6.922996,2.013701,-0.520362,-7.931522,6.678249,7.624853,5.073089,4.206599,5.380943,-0.030730,-8.767491,-1.065351,0.990055,-4.478861,-6.123966,-2.234634,7.584546,-4.214722,0.893802,0.629991,-2.158797,9.593680,-7.104708,-5.072031,-9.904996,0.968220,-7.683775,-3.498977,-6.597403,5.822831,-2.655632,9.240700,-1.362374,6.833580,-3.723757,-1.157023,3.394915,-1.208746,7.961330,3.799480,5.433328,-4.081441,-8.095362,1.682615,2.923901,6.815194,-4.732645,1.094256,-2.053591,8.077311,2.862230,-0.134345,2.892230,-2.585455,0.295398,6.821464,-5.454919,-0.806440,-6.429448,3.063740,6.126461,3.368955,2.444537,-2.398973,2.698330,2.175599,4.371783,8.029847,-6.433133,9.633356,9.359508,9.717912,-2.142499,-2.361659,5.305711,-1.169425,-7.026938,4.494023,-7.294409,8.894299,7.008332,-3.139989,-4.584752,1.878425,5.565073,-9.539524,6.809672,-8.776833,-5.018368,-1.113569,1.286733,-0.288961,-8.954815,5.236971,7.328524,-5.927298,2.907755,5.031751,-8.444909,9.611375,-9.402118,-9.821580,1.624859,9.674421,9.090414,7.280791,5.806811,-5.316748,4.435540,-8.693288,2.537077,9.394434,-0.781944,-7.826370,-9.532482,-5.187723,-1.491750,-4.717812,-3.080573,8.640611,-3.078361,-1.974989,-0.634175,8.037374,-4.906617,-7.093341,5.123897,5.484844,-5.712768,-9.551434,7.683598,6.373441,-6.460412,6.399114,-7.577920,-3.297945,4.478584,-2.689810,-7.297682,-3.751513,4.939608,-4.583717,-5.458183,-2.209431,8.100459,4.534426,-9.481868,-8.948727,0.471775,0.860669,-3.008423,-6.067969,-1.963133,9.836630,-9.000147,3.571056,-7.782239,-4.668369,9.386839,-0.648268,-3.346858,4.688060,-3.886133,0.471526,4.300795,3.617792,-5.264238,-2.895818,-3.136128,5.264527,7.390898,1.064067,-9.390981,-8.649156,-6.213082,0.661000,0.259845,0.732090,-4.955929,3.548391,4.797519,-3.134761,-3.375335,-2.773012,-9.045382,9.574437,8.545495,-0.675773,7.458267,9.817368,9.220351,-3.788206,-2.047541,-7.626003,-4.778111,-4.162892,1.275352,0.763837,8.421706,-4.420816,-0.082382,3.473911,-0.808355,5.146253,7.562228,-6.849956,7.620716,6.619048,-8.191356,9.849698,8.106096,3.630387,-1.745159,-9.956335,-0.947022,7.993315,-6.322210,-4.002245,-6.508080,-4.365624,2.758748,-9.907548,2.022795,-9.444634,-1.334792,-7.530246,1.048088,-6.553577,7.836390,-0.720708,1.059995,-2.382971,-7.912277,4.540008,-6.841419,-5.027499,-8.180601,6.472483,-6.387612,5.915182,8.130162,-3.458917,3.452709,-5.429268,5.230563,8.988818,-5.673511,7.341259,-7.476918,-3.061519,-0.424179,-1.035877,4.210272,2.556004,1.277550,-0.591778,-3.578923,-4.092074,0.674259,-0.615993,9.840604,-9.654139,8.616992,-7.144363,-0.828371,2.640680,-8.502752,3.336001,1.640034,3.871555,3.087224,8.184233,2.292085,-7.457302,-6.689466,0.986477,-4.932590,2.598446,8.319927,1.421698,-1.252163,6.941705,2.454495,0.841213,4.608429,9.769639,-4.646620,-8.169875,-0.161556,7.788749,-6.333145,-5.155462,-8.432137,-4.734965,-2.475435,4.433975,-6.483894,6.871754,3.620396,-8.035605,9.428419,1.023084,-5.012845,5.303896,-6.665090,6.828810,-0.412005,1.496073,-3.018030,-0.218671,-7.559416,2.332295,-0.500521,-9.751307,3.467292,-1.747293,-9.160129,3.637777,-9.548037,-8.909651,2.591271,7.891315,8.410090,-9.130335,-5.624112,-1.427422,-5.867960,-3.361020,-7.236986,-6.584578,9.471609,2.348587,-0.654206,3.666373,5.807301,-5.407016,1.412945,-5.077755,-9.462249,-8.879192,-6.315819,3.800469,4.327007,9.533366,-6.708811,0.050180,9.738083,-4.463829,1.286367,-6.019064,7.001828,4.895473,-5.376793,8.704979,-6.349289,5.229580,3.112131,8.082216,-9.323130,-9.961091,-6.131848,0.462012,-8.001256,-4.901233,9.334649,7.448488,2.960591,4.623579,-6.340917,-2.916052,1.022218,0.723686,9.861902,2.135820,-2.055126,-9.444196,9.689464,-5.024476,7.010114,-9.099844,2.968933,2.663553,-7.352485,-2.636178,-5.399605,-9.295001,-5.466244,-1.272983,-7.509229,-1.685431,8.616744,-3.587459,-4.691422,5.913905,2.858883,-2.287454,2.020042,8.947024,-0.202924,-6.472438,-0.598710,-8.240828,8.595897,-9.593913,-6.943498,-5.077307,-3.811766,2.454769,1.361497,-9.913969,-8.728412,6.704960,4.572837,1.043356,-6.533387,-0.774378,-3.091270,7.699165,6.626166,-7.076214,-0.358819,8.042376,5.469015,4.010624,5.324536,8.589862,-7.362172,2.323813,3.347849,-9.817726,4.264358,-3.988569,1.715869,7.731519,-7.698325,6.803719,-3.798848,7.859549,3.313995,-8.222061,-1.798216,-3.071084,-8.588697,-3.100172,-5.366819,3.487836,6.999689,-0.646454,9.815190,0.978550,7.650061,5.139477,-1.279467,6.295057,6.881042,-0.313210,8.119331,6.393517,3.386082,9.444464,-9.662923,6.144985,-7.256497,-7.404414,1.042933,9.983733,-4.681594,-7.574968,5.627412,-5.062405,5.642844,7.197421,3.489828,-6.894560,-3.390083,0.015356,-9.486430,8.788643,-0.218949,-0.535153,0.042595,-9.679183,-2.902361,-4.819896,-0.269194,9.622990,-0.931200,-9.186579,1.723466,-6.357431,-6.758312,-2.822486,-6.531130,7.692899,2.976465,-1.950001,-2.716755,4.112478,3.736558,-9.709617,-6.433565,4.051405,-7.098727,7.274123,-6.228377,-9.926261,1.940027,6.300831,-8.042583,-0.165783,-3.712354,-0.023543,6.163378,-8.418933,-8.768487,-8.277523,-9.881838,3.390571,8.461900,-8.639500,-4.133258,-9.598179,8.537031,8.669349,-5.062582,6.833349,-8.114791,9.389201,6.783750,-9.291194,0.113311,1.602125,-8.058929,-9.959249,9.515462,2.055624,9.817211,6.769882,5.169752,-3.274497,-7.957366,-4.100291,-6.195244,-9.243315,7.850353,9.129552,2.531235,-3.290461,3.032737,0.940891,9.257119,-5.846815,-3.909208,1.701351,-8.710887,1.732392,-9.662317,2.262119,-1.169181,-0.647997,-3.961064,-9.571991,-2.172410,3.889644,1.868048,-0.748080,4.645854,-3.336830,-1.127417,3.551967,9.741020,3.288272,-5.162190,-2.591970,-5.954084,8.970316,-8.402145,-3.382535,-8.296867,-3.869990,-4.981352,6.090354,7.676227,5.664214,4.738202,-4.584679,-3.504032,-8.619411,-3.846673,5.303402,-4.839295,9.907879,-7.905842,0.301704,2.002026,-0.011123,9.354503,1.826404,7.078691,-1.495253,0.696525,-0.644478,8.558336,7.921588,8.210172,-9.868439,5.223247,6.952999,-4.237922,-7.010321,-7.246901,0.055695,-1.605420,9.424539,-7.162568,0.720308,-6.239710,0.518219,-8.974459,-8.929622,5.571140,1.551289,-9.922640,-5.789087,-4.863487,1.146816,0.168136,-0.971251,8.711990,-5.122455,2.266714,-7.594486,0.066481,8.367867,-6.904953,2.288728,5.432684,-6.693121,9.715225,-9.934703,1.931114,6.919921,-5.967844,8.675902,8.896867,0.950872,2.448099,-4.313708,5.220728,-3.587894,7.255202,7.667446,2.124135,5.602091,-3.161688,-6.905729,3.345702,3.102435,9.156014,9.211700,-6.436459,7.049852,-9.810620,-7.681013,-1.065306,7.303035,-5.684753,-8.628272,-4.083599,1.355834,3.267247,7.773670,8.153385,-0.063943,9.614360,8.493830,5.145088,6.281860,-6.222874,4.870379,-4.424441,7.145534,-2.726681,-9.411680,7.878806,4.590827,1.256829,4.625798,0.246044,0.550716,5.043517,-1.085026,-9.691868,8.144602,1.233919,5.409686,7.299933,7.473697,-4.854872,2.221855,2.331890,-0.485196,4.929606,7.346471,6.577469,5.648034,1.565498,9.373004,1.031377,-4.305521,-2.183122,-4.730850,-8.074178,6.987521,-7.376195,-2.895058,8.509921,-6.698170,-7.746301,-5.789679,6.134725,6.758068,1.030278,-0.861189,0.721979,-6.933212,-8.967136,3.373117,-7.422439,1.425218,9.820634,-7.324924,-5.810564,1.765320,-1.431122,-7.688601,5.398217,-2.206838,8.226507,2.258678,6.400828,-8.068722,7.876525,9.154427,-0.827312,-2.374108,-0.487519,-6.252653,7.528846,-6.324872,2.198918,6.475562,-7.321243,-6.259206,-7.523347,-4.700812,4.275583,9.647484,-5.139477,-4.452145,0.193961,8.835198,2.123973,-8.742659,1.575608,-4.714174,-3.015699,-3.664157,2.240729,-7.202517,-9.653012,9.436396,0.903533,-7.510018,8.344419,-6.442315,9.190582,2.256838,7.680504,-7.990355,-4.590182,-5.984481,-4.621471,4.186275,7.110605,-9.061701,-5.442533,1.236905,-6.168259,8.266111,-3.157500,3.100781,2.562513,-2.991511,-7.620631,-1.934350,2.343923,2.420692,4.053751,5.327769,-3.804128,-0.921386,2.265708,-7.355997,-0.637837,-5.362724,3.101893,-9.724438,-9.962060,-8.826207,7.734892,6.574558,0.709388,2.892747,8.661171,0.093600,-9.124457,-6.185945,8.868608,5.520113,-0.510530,-4.667721,1.130253,0.095207,2.653653,6.824952,-6.050919,4.526569,1.576511,-2.937962,0.069699,5.789407,8.408799,1.362199,-4.697312,-0.685028,-5.817733,0.812040,-1.973100,4.683832,-2.075116,-4.059419,4.041037,-7.576437,-4.357504,0.508676,-1.546766,8.885936,-6.494111,-2.334648,-7.323958,-7.550459,4.901344,-7.772331,-2.335170,4.751397,-5.885292,7.981139,9.486729,1.403622,-1.392398,1.177485,7.824876,-1.290158,1.064657,-8.273596,-7.983528,2.647443,-1.830919,8.595254,9.517364,9.751672,-2.007434,-3.516491,-5.976788,-0.207098,-2.872505,3.916036,-4.469686,-1.152396,-7.159627,5.391270,2.438687,-5.341408,4.464174,-1.086809,-5.504202,-9.995283,-9.432743,-3.929220,-2.676806,1.708554,-0.864527,-4.517783,-9.241731,6.996798,-8.416565,8.357891,3.904940,6.132132,2.157812,1.007519,-8.451178,8.847997,-1.234706,0.064101,-7.139043,-1.551567,-4.830100,6.047367,7.953181,6.715523,-5.407077,9.786379,7.976528,-3.346333,-2.932185,-7.556094,5.893159,7.283713,-3.265711,2.650310,5.065478,5.165888,-8.493633,-0.825721,5.955680,4.930980,7.560756,3.493455,-9.271903,9.042409,-1.151498,3.879803,8.785068,8.517833,2.512515,-3.331248,-9.641636,-7.806415,0.779499,-0.866183,2.886555,-9.745236,-5.437732,0.843947,9.025803,3.775416,-4.992657,3.728273,6.111802,0.849209,2.063348,9.932346,-0.191832,6.521505,3.233947,-1.129520,1.835118,2.238900,0.047057,-6.735284,3.087792,-5.988624,-3.145647,-2.891896,-5.217585,2.734904,8.461853,-2.739160,-3.352778,3.782996,9.468492,-2.071347,-5.486458,2.312367,-7.301024,-8.939967,4.818893,-9.211927,1.991342,-5.268188,-0.736854,2.267613,-1.945525,3.114095,4.498270,-6.983203,6.985327,-7.086129,-9.528849,8.088265,2.906551,3.560617,-0.934412,7.472096,-7.320362,4.884549,9.297424,-4.277150,-8.306439,-8.271955,3.448087,0.450106,-2.446868,-7.638158,6.766367,7.727578,-4.542556,2.414820,-4.614641,-0.735988,-9.857631,-2.404121,-4.552069,-3.502387,-9.857415,6.817852,0.657895,-2.748565,-2.241504,8.073257,-0.617968,-3.413055,0.241042,8.466956,-9.195474,-2.933824,-4.084551,-1.304833,5.516070,3.177405,-2.822588,3.721806,4.483964,5.057113,2.757671,2.977054,5.300246,-1.654968,-0.114937,4.824456,1.612888,6.936060,-0.834545,-3.041824,-1.565735,6.707635,-9.039131,5.408758,4.596611,6.873254,9.456011,-6.043339,6.681161,7.611536,6.362821,-6.233928,-0.699784,-2.330091,-0.055047,-3.554349,-8.920311,2.813530,6.100521,6.799456,8.624601,3.502337,1.464798,2.299709,-6.349462,-7.074228,9.650744,-7.546132,3.390730,-9.271579,1.224321,-6.655745,5.877484,1.081625,-0.138145,5.506967,1.639983,-6.537036,-1.676333,9.540497,-1.045103,-3.305966,6.077046,8.040887,8.630157,-7.638327,7.555835,4.603653,-2.996556,2.926378,1.352040,-9.792318,2.212208,4.546514,-1.657525,-4.160656,7.955848,3.424801,1.861978,0.146322,-1.732041,9.561076,-3.753815,-5.987223,4.819059,-0.240444,-0.840115,-4.267278,9.746785,-4.088304,-2.476185,5.519048,6.532644,-2.483320,8.373812,-4.981019,7.086929,5.585733,-9.568114,-4.132414,0.167753,-4.230769,5.431311,5.270497,-8.751088,5.945131,-9.231355,-5.062659,0.250618,-4.490119,-1.541115,-0.862078,2.206400,-0.086510,-7.196434,2.243998,6.784389,3.188370,-8.918851,8.685106,-8.794934,-1.418469,4.495292,4.846337,5.557587,-3.101116,-0.946815,-2.118765,-3.685141,6.065134,0.917707,9.751191,-6.865485,-6.371812,6.442383,7.849519,-9.781779,8.148995,3.320733,-5.847286,-3.990662,-1.522276,9.658683,-9.015234,2.797081,-9.002459,8.226865,4.143240,6.443581,-0.932941,-1.077280,-9.082063,1.614295,-4.657148,-8.009523,-3.717340,3.538389,3.734253,2.257176,9.100046,3.151453,2.207013,2.067531,-4.932035,-6.915490,1.459990,2.693457,5.681163,7.095082,2.375571,-8.575849,1.643310,-7.281158,0.779305,-3.027533,0.721018,-1.793413,-4.845461,5.587990,-4.924342,-3.972030,-3.996114,-5.221957,-4.042848,-4.589434,5.253971,3.942499,-5.445568,-0.269518,7.579352,-3.061157,-2.567195,-3.676497,-7.428266,-7.479293,2.689447,5.917963,-0.265800,-4.102559,1.457689,-4.433091,8.038133,0.158814,1.604068,7.811110,0.832446,7.672558,3.338314,-4.244937,-6.195683,-5.723702,2.846078,1.740530,8.171469,6.936269,-7.402911,-7.242434,9.703007,-4.589618,7.204667,-0.635128,3.690613,-1.180725,4.558892,0.369695,8.330601,3.744142,1.461057,-3.275834,-3.383300,6.675297,6.446004,6.353891,-1.298094,-0.315924,1.455684,-9.041444,-3.867365,3.656541,8.636098,3.182800,1.678935,-1.215114,-1.993015,6.117706,-0.254503,2.968576,-6.358689,-7.212816,-1.531938,-0.236889,2.206230,8.275317,-2.862417,4.594973,5.741520,-7.310094,-0.302310,4.590333,-5.974709,2.210698,9.979745,-8.864144,1.528342,-6.657843,3.035537,-2.013604,4.440737,8.353198,-0.142334,-1.680715,0.694727,-5.068760,6.753761,-5.807886,6.284876,-9.548553,6.684756,-4.424311,1.722718,-3.773673,-1.635463,-0.595475,-4.120368,8.510497,-8.795527,-2.303252,-4.977853,7.999149,-0.164768,7.240125,-7.631014,5.547894,3.293837,-4.692130,-0.636863,1.850658,7.197517,1.659713,1.662233,0.792667,-1.857215,-6.168897,-6.448009,-0.521321,1.436736,-1.292924,4.489021,5.927878,-4.660199,6.079195,1.294829,7.938128,-6.450735,-9.584531,1.863116,-3.825157,-0.295701,-8.028994,-2.695582,0.603064,8.032656,4.581010,3.693572,2.718802,5.885869,0.501860,2.223912,1.799664,5.088127,-7.110224,6.195718,-8.567055,2.213912,2.326350,7.116095,0.404918,-4.494955,8.004080,-5.319012,1.762781,2.668757,-1.521148,0.792425,7.974891,4.887817,8.718638,-8.134372,-9.815388,3.157282,7.786657,0.395176,4.214555,-6.247801,4.813594,5.849448,-3.026866,2.276389,8.005425,-6.987108,0.529223,-7.502603,3.868835,-7.265461,-3.848690,3.301061,-8.100704,2.411290,-3.193960,-8.737478,-2.780156,4.778648,6.013011,6.479227,6.375475,9.107977,9.867422,-3.896291,-3.831785,1.489745,-2.898165,-3.926116,6.412255,-0.927893,7.146820,9.484392,-2.893616,-2.562317,-3.726921,-8.376483,-3.512695,-7.395111,-0.773786,-0.069360,-7.615540,3.837881,-9.983168,2.749387,1.421824,9.019295,2.715060,-8.448148,7.723155,3.788783,-7.075415,-9.351697,6.643655,2.717117,6.419944,-9.678984,1.281231,-1.857296,6.427305,2.786032,0.518350,-6.646543,1.754340,-1.596548,0.386532,-6.828318,8.831904,-9.719900,-5.403798,-4.907365,5.809922,7.741481,2.131838,-8.092468,0.453616,4.897612,2.248251,0.520388,7.068589,0.568498,8.290182,-4.656880,-5.059268,5.370372,-2.895254,-5.905623,-7.712366,-3.071742,5.818802,0.753903,-5.779214,5.539886,-0.460802,2.028809,-5.694467,-3.397754,-9.452653,5.487970,-6.157399,4.092327,-6.097244,-9.943645,4.747141,-9.963764,-9.419316,-3.438137,6.170310,-0.046198,-0.771904,3.106187,-7.746049,6.049046,-0.036678,-4.967414,9.694090,-5.948314,0.674548,0.478275,2.069265,-6.162296,1.198190,4.638294,-2.252194,-8.684380,1.032936,-2.687089,1.667842,-8.636419,-1.737123,-1.244783,0.833260,7.500643,-4.234925,1.079995,4.649549,9.824687,-4.685020,9.392831,-8.417659,-4.381039,6.279698,5.821256,-6.722525,-7.681862,-7.406259,-3.251010,6.925036,3.441355,-6.437832,-9.402996,-2.079091,-9.322401,-6.892595,6.047208,8.292189,-0.666717,-5.728100,-0.744706,9.200137,6.727202,9.763214,9.719357,-9.471340,-5.360401,-7.461540,-2.481852,-6.521112,7.628510,-1.260367,4.686033,-2.288599,-4.671157,-3.141107,1.882099,9.547842,0.695060,4.472467,-1.697358,3.532053,-8.597210,6.203619,-1.758800,-1.568792,-9.733148,5.761321,-2.767476,7.544031,-5.200716,8.672037,8.345161,9.270936,-3.517428,-7.544485,-8.698833,0.272802,8.412672,6.458963,9.315660,3.388033,-0.391349,4.033213,6.767249,4.418809,-3.049403,9.566017,8.929267,8.986220,9.637111,-5.048771,9.181236,8.003264,-3.821169,8.470137,-3.793250,8.375786,6.138157,2.525172,1.747112,-2.277383,-5.533457,-1.665112,-3.888253,1.467296,4.610224,3.598022,1.757953,2.661236,8.255605,7.499335,5.433795,-5.585840,-9.064552,4.157513,-4.963779,5.685762,-3.660496,2.411232,7.849216,-7.499778,-9.879129,-5.303933,-6.850181,-7.474288,-4.522108,5.298471,-2.219650,-8.077126,-4.758170,2.105416,0.711657,1.367597,-4.264365,7.559142,1.822282,-3.497800,5.409777,0.344512,-4.190273,-5.643503,-0.072127,-7.831753,0.557755,0.353805,9.820338,3.648118,7.903439,-4.361286,8.383301,-0.524828,7.386056,-5.262298,2.507270,0.099485,2.977027,-7.236762,5.522770,1.827369,6.018524,-1.289806,5.781682,7.523725,-6.562133,-6.171326,8.009303,-4.056471,5.254558,-7.718215,2.314273,-8.002643,6.400385,-7.877537,3.131837,5.358656,-7.686608,5.310218,3.514832,-5.444470,-9.645503,9.951308,4.113188,3.238761,2.824164,0.467855,9.465251,3.774723,-8.070289,2.861454,4.840689,-2.533367,5.235131,2.184188,7.197763,-7.627704,-9.395228,8.233336,-1.471790,-4.098112,-6.119123,-8.820638,8.351119,-2.210641,6.590468,-4.815835,3.146069,-6.732640,-3.148632,7.640446,1.822214,-6.273485,-5.103471,-0.315917,-2.959123,-4.039550,-5.282011,-8.948901,-5.473205,-8.964228,-3.750905,1.764949,7.599554,-9.743222,3.054339,2.306223,-6.030060,2.432796,-9.553702,8.423333,-1.111580,1.338508,-0.588242,0.405553,6.615595,-1.859276,-0.472836,3.656407,3.891857,1.100133,6.847105,9.899891,-5.027754,-9.487762,-1.329647,6.949084,4.187275,-9.837105,-5.166903,0.661357,2.436742], dtype = "float64")#candidate|5505|(1764,)|const|float64
call_5504 = relay.TupleGetItem(func_4419_call(relay.reshape(const_5505.astype('float64'), [14, 9, 14])), 0)
call_5506 = relay.TupleGetItem(func_4422_call(relay.reshape(const_5505.astype('float64'), [14, 9, 14])), 0)
output = relay.Tuple([call_5496,call_5502,call_5504,const_5505,])
output2 = relay.Tuple([call_5497,call_5503,call_5506,const_5505,])
func_5509 = relay.Function([], output)
mod['func_5509'] = func_5509
mod = relay.transform.InferType()(mod)
mutated_mod['func_5509'] = func_5509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mutated_mod.get_global_var('func_5509')
call_5510 = func_5509_call()
output = call_5510
func_5511 = relay.Function([], output)
mutated_mod['func_5511'] = func_5511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_5534 = func_3789_call()
call_5535 = func_3789_call()
func_1912_call = mod.get_global_var('func_1912')
func_1915_call = mutated_mod.get_global_var('func_1915')
var_5539 = relay.var("var_5539", dtype = "float32", shape = (1350,))#candidate|5539|(1350,)|var|float32
var_5540 = relay.var("var_5540", dtype = "float32", shape = (300,))#candidate|5540|(300,)|var|float32
call_5538 = relay.TupleGetItem(func_1912_call(relay.reshape(var_5539.astype('float32'), [15, 9, 10]), relay.reshape(var_5540.astype('float32'), [50, 6]), ), 2)
call_5541 = relay.TupleGetItem(func_1915_call(relay.reshape(var_5539.astype('float32'), [15, 9, 10]), relay.reshape(var_5540.astype('float32'), [50, 6]), ), 2)
func_1233_call = mod.get_global_var('func_1233')
func_1236_call = mutated_mod.get_global_var('func_1236')
var_5543 = relay.var("var_5543", dtype = "int16", shape = (1, 252))#candidate|5543|(1, 252)|var|int16
call_5542 = relay.TupleGetItem(func_1233_call(relay.reshape(var_5543.astype('int16'), [9, 7, 4]), relay.reshape(var_5543.astype('int16'), [9, 7, 4]), ), 0)
call_5544 = relay.TupleGetItem(func_1236_call(relay.reshape(var_5543.astype('int16'), [9, 7, 4]), relay.reshape(var_5543.astype('int16'), [9, 7, 4]), ), 0)
func_3746_call = mod.get_global_var('func_3746')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_5547 = relay.TupleGetItem(func_3746_call(), 0)
call_5548 = relay.TupleGetItem(func_3747_call(), 0)
uop_5549 = relay.sin(call_5538.astype('float64')) # shape=(15, 9, 10)
uop_5551 = relay.sin(call_5541.astype('float64')) # shape=(15, 9, 10)
func_935_call = mod.get_global_var('func_935')
func_938_call = mutated_mod.get_global_var('func_938')
var_5558 = relay.var("var_5558", dtype = "int32", shape = (45,))#candidate|5558|(45,)|var|int32
call_5557 = relay.TupleGetItem(func_935_call(relay.reshape(var_5558.astype('int32'), [45,])), 3)
call_5559 = relay.TupleGetItem(func_938_call(relay.reshape(var_5558.astype('int32'), [45,])), 3)
func_4489_call = mod.get_global_var('func_4489')
func_4492_call = mutated_mod.get_global_var('func_4492')
var_5566 = relay.var("var_5566", dtype = "float64", shape = (280,))#candidate|5566|(280,)|var|float64
call_5565 = func_4489_call(relay.reshape(var_5566.astype('float64'), [14, 5, 4]))
call_5567 = func_4489_call(relay.reshape(var_5566.astype('float64'), [14, 5, 4]))
output = relay.Tuple([call_5534,var_5539,var_5540,call_5542,var_5543,call_5547,uop_5549,call_5557,var_5558,call_5565,var_5566,])
output2 = relay.Tuple([call_5535,var_5539,var_5540,call_5544,var_5543,call_5548,uop_5551,call_5559,var_5558,call_5567,var_5566,])
func_5568 = relay.Function([var_5539,var_5540,var_5543,var_5558,var_5566,], output)
mod['func_5568'] = func_5568
mod = relay.transform.InferType()(mod)
mutated_mod['func_5568'] = func_5568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5568_call = mutated_mod.get_global_var('func_5568')
var_5570 = relay.var("var_5570", dtype = "float32", shape = (1350,))#candidate|5570|(1350,)|var|float32
var_5571 = relay.var("var_5571", dtype = "float32", shape = (300,))#candidate|5571|(300,)|var|float32
var_5572 = relay.var("var_5572", dtype = "int16", shape = (1, 252))#candidate|5572|(1, 252)|var|int16
var_5573 = relay.var("var_5573", dtype = "int32", shape = (45,))#candidate|5573|(45,)|var|int32
var_5574 = relay.var("var_5574", dtype = "float64", shape = (280,))#candidate|5574|(280,)|var|float64
call_5569 = func_5568_call(var_5570,var_5571,var_5572,var_5573,var_5574,)
output = call_5569
func_5575 = relay.Function([var_5570,var_5571,var_5572,var_5573,var_5574,], output)
mutated_mod['func_5575'] = func_5575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2798_call = mod.get_global_var('func_2798')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_5582 = relay.TupleGetItem(func_2798_call(), 0)
call_5583 = relay.TupleGetItem(func_2799_call(), 0)
var_5586 = relay.var("var_5586", dtype = "float32", shape = (14, 6, 14))#candidate|5586|(14, 6, 14)|var|float32
bop_5587 = relay.right_shift(call_5582.astype('uint16'), var_5586.astype('uint16')) # shape=(14, 6, 14)
bop_5590 = relay.right_shift(call_5583.astype('uint16'), var_5586.astype('uint16')) # shape=(14, 6, 14)
func_4858_call = mod.get_global_var('func_4858')
func_4859_call = mutated_mod.get_global_var('func_4859')
call_5592 = func_4858_call()
call_5593 = func_4858_call()
bop_5596 = relay.power(bop_5587.astype('float64'), call_5592.astype('float64')) # shape=(14, 6, 14)
bop_5599 = relay.power(bop_5590.astype('float64'), call_5593.astype('float64')) # shape=(14, 6, 14)
output = bop_5596
output2 = bop_5599
func_5602 = relay.Function([var_5586,], output)
mod['func_5602'] = func_5602
mod = relay.transform.InferType()(mod)
mutated_mod['func_5602'] = func_5602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5603 = relay.var("var_5603", dtype = "float32", shape = (14, 6, 14))#candidate|5603|(14, 6, 14)|var|float32
func_5602_call = mutated_mod.get_global_var('func_5602')
call_5604 = func_5602_call(var_5603)
output = call_5604
func_5605 = relay.Function([var_5603], output)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4528_call = mod.get_global_var('func_4528')
func_4529_call = mutated_mod.get_global_var('func_4529')
call_5607 = relay.TupleGetItem(func_4528_call(), 0)
call_5608 = relay.TupleGetItem(func_4529_call(), 0)
output = call_5607
output2 = call_5608
func_5618 = relay.Function([], output)
mod['func_5618'] = func_5618
mod = relay.transform.InferType()(mod)
mutated_mod['func_5618'] = func_5618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5618_call = mutated_mod.get_global_var('func_5618')
call_5619 = func_5618_call()
output = call_5619
func_5620 = relay.Function([], output)
mutated_mod['func_5620'] = func_5620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5618_call = mod.get_global_var('func_5618')
func_5620_call = mutated_mod.get_global_var('func_5620')
call_5641 = func_5618_call()
call_5642 = func_5618_call()
func_5043_call = mod.get_global_var('func_5043')
func_5047_call = mutated_mod.get_global_var('func_5047')
const_5648 = relay.const([5.169625,-3.299757,0.214609,0.368453,9.966324,-0.742446,-5.778664,6.371719,-6.745143,-6.805659,-7.190936,6.278058,6.768600,4.360385,-8.696499,1.651147,-0.898762,-8.812935,-1.433025,2.021283,8.985344,3.122045,-1.210442,-0.794590,0.373199,-7.274452,-0.697884,-0.811969,-5.631581,-4.807084,-3.424925,-3.857749,-4.219443,-1.422154,-1.427399,-3.511704,-2.008023,5.227969,9.767095,2.251084,-4.134470,-6.146969,-7.573133,0.709756,-7.567219,1.861781,8.565282,3.634195,-9.910098,3.567050,0.682176,-6.671328,0.122172,6.998106,-0.020774,7.880926,-3.046449,0.166317,-2.825848,-3.748632,2.911367,3.211163,3.207953,-0.130881,-4.379857,2.519090,4.815945,2.102837,7.125767,6.771228,-1.435429,4.344429,-0.062020,3.097580,4.227673,7.923744,7.767149,8.286836,6.457484,6.145681,6.769601,-9.575186,-9.745315,7.297463,-1.259506,9.218890,1.836876,8.344066,-8.606917,-0.940316,-9.737161,-7.236043,-7.465259,4.965066,1.076972,-6.175831,4.183560,4.160328,-2.608523,4.790391,-3.440688,5.130925,3.083256,2.658368,3.075835,8.511367,-6.133842,-3.411431,-3.218937,-3.449219,-2.310896,-7.146003,4.427019,4.507038,1.402362,-5.105133,-5.707002,9.853413,8.595124,8.436243,4.910773,-4.458248,-9.144347,-7.635437,-1.466377,-2.289150,9.503893,-4.744247,-3.653722,3.207804,1.368344,5.100000,1.042142,5.949461,-8.395840,-7.796214,-1.833373,6.628440,9.438554,1.008948,-7.032944,-3.601289,-8.703743,7.297032,-0.655241,-6.366989,-6.445542,2.684248,5.801933,-7.716615,9.199764,9.174726,-2.845873,-4.983654,-6.162526,3.477731,8.282102,1.111226,2.799545,9.267245,9.455833,6.821925,6.269061,6.401001,0.929794,-9.985752,-6.086872,-1.176980,-7.938464,-4.970514,-9.669018,-5.723052,9.399276,-3.679925,-9.735885,5.167383,2.585471,5.978028,0.313491,2.059621,4.158062,-8.046603,0.497153,-9.096537,9.929864,3.752782,-0.496687,-7.952205,9.352263,-7.676368,-6.083199,2.641024,-5.699436,-8.706210,9.215622,5.863819,-2.772290,4.018875,-7.340660,1.452241,-1.315848,-6.153018,-4.084289,3.943081,0.286621,7.824732,9.929115,0.068892,-2.617101,9.725076,-8.164846,-3.378218,-9.546368,-6.980617,6.287097,0.634822,-5.896355,-2.442116,-4.322879,-8.707557,-7.759917,8.036348,-7.079698,6.924909,-8.982888,4.055296,7.050379,4.373440,2.009965,3.127851,-5.882857,-8.539485,-3.380632,3.506241,-3.360990,-2.753728,-7.188306,-4.627444,-7.353866,6.416072,6.516334,7.092860,-5.117049,-7.843958,1.315436,-1.373701,-1.655537,-3.191157,6.680635,9.844123,-4.399960,-9.603864,3.763736,0.405032,0.486810,8.540453,6.685296,3.733691,9.842596,3.921072,2.333441,-4.106369,9.918043,-1.741762,7.031418,-6.908810,4.932425,-2.382602,-3.876892,3.042528,-9.462309,-4.975687,0.501252,5.663238,6.108282,4.496202,-0.516386,2.452043,7.548367,-7.501768,5.604124,-5.223273,-3.458850,-3.826060,-2.842860,-1.821455,-5.398168,9.590897,-7.026475,-3.202860,9.677755,9.863273,-9.489094,3.594928,-8.201709,-6.291945,5.616780,9.913994,4.948674,-0.026952,5.256430,-8.350961,1.296300,5.685296,-8.306621,0.308699,-6.325564,6.762761,3.410140,-2.238840,-7.919779,-3.785193,9.990297,6.706652,9.211606,-1.793918,-2.956839,-2.858054,-6.181123,-2.447617,9.062446,1.378274,-5.166601,-5.562337,2.693956,4.811509,7.326171,8.340207,1.287339,3.449916,-5.124399,1.632715,-8.322708,-6.926501,-4.638213,7.171249,9.378621,0.646050,7.988347,4.207140,-0.102705,4.480280,-7.139171,-5.163202,7.651536,-0.603114,9.803650,0.749472,7.929628,5.587386,-1.642045,-3.761439,7.967704,5.657190,2.894679,2.151432,1.475828,-4.762584,-0.827762,-5.824594,-9.404913,4.693818,-1.568058,-6.470734,0.329665,0.746100,-7.054467,8.532587,9.042202,3.006006,0.467727,-8.097922,8.864436,6.806882,3.786972,2.147779,-5.580738,-7.910314,5.913678,9.608828,-9.130731,-0.893474,-7.287753,-3.360026,-4.095406,-2.980036,-4.408986,3.407237,0.848279,5.690010,-5.634494,6.219356,-6.101399,8.927919,-6.008253,-4.202580,-6.251791,2.796425,-9.796583,-3.884869,0.023924,-2.036350,-8.126204,0.934893,-0.937301,-7.638636,-0.881961,-1.320703,2.596915,-3.146310,-3.976067,-6.630742,-4.270498,7.610874,3.485889,2.896203,-1.231680,4.361286,6.201709,6.403911,8.140251,-4.249689,1.159109,-4.772364,3.167803,-2.727168,4.842541,-1.438548,-1.019212,-7.200254,1.939071,4.636440,-3.458721,-0.379487,3.721324,5.981430,-4.786158,-6.676267,-7.542077,-5.244246,-8.030542,5.664474,-7.143343,8.591121,3.747693,-2.815431,9.981555,9.243262,-2.885664,-7.709797,2.466812,6.733786,8.117904,1.818078,-0.303200,0.535953,-0.374149,1.356404,-5.624006,8.054365,-1.161210,6.195120,0.737566,8.265026,-7.341335,-6.687951,-4.247371,3.673876,7.217087,9.928531,2.047482,-6.563775,-2.865571,-0.060232,-1.578877,-7.200053,9.343538,0.181392,-2.008983,6.599304,-0.871270,-8.486519,9.387006,-0.946591,-5.065571,-1.241321,1.691079,9.983224,-9.107060,-2.953677,-5.247522,-3.233202,-5.612855,-9.182330,-7.532268,-8.934927,4.263640,2.522772,-2.453168,-5.040408,-4.033923,-4.888387,3.853083,8.766454,4.234978,2.790586,-0.888929,-5.481976,0.708140,-2.448369,-7.119514,-3.545798,6.955645,-1.134260,4.169670,8.448437,0.859126,2.515208,1.718784,3.418255,0.622191,-6.189052,-2.373070,-8.456176,-0.920341,5.436115,6.646226,-4.810922,-3.954995,6.232769,5.049759,5.503007,-3.914211,-4.239599,3.548906,1.963097,-6.328822,-5.092646,-2.621472,-4.613587,3.244132,6.639747,9.053925,-6.331845,-4.982008,8.678992,-2.118331,-9.141100,-6.037958,-5.640014,-5.229328,-5.507507,-0.205028,6.116168,7.876077,7.258916,-9.960612,-6.089844,-6.841463,0.207203,-1.398269,1.418088,5.954792,7.216411,-5.189677,2.431799,8.504116,3.444928,-6.234505,-2.889956,-3.428760,4.313067,-3.765827,-6.832609,-2.305669,7.846709,-7.143606,1.580647,1.456568,4.950864,-7.778387,-1.737841,-8.353497,1.753313,1.000228,0.180429,0.777541,-3.041565,-3.476043,6.609489,-1.782572,1.458459,3.871961,-3.697181,4.252118,-7.473926,-3.842510,-0.375761,-3.947066,5.721241,2.816394,2.595642,8.743546,6.556865,-1.845203,-7.292011,7.967293,9.943175,-2.356857,8.631829,-0.779059,-3.800033,6.167885,2.850414,-9.662312,0.634219,0.440963,0.084491,-1.786501,-5.597495,3.002982,7.126993,-4.111701,3.543705,-3.984895,1.849201,-3.920639,8.840093,-5.593517,2.191056,5.220507,-8.318665,8.722984,-0.275394,-0.736636,-8.913685,3.037186,0.339111,-5.324627,2.344569,6.786605,9.741712,-8.773092,2.806965,-6.861578,9.541018,0.026949,-6.663098,5.153660,-9.144998,-1.338162,8.172666,-4.959623,0.348396,9.989629,4.990923,4.888561,-7.078933,3.454502,-5.062445,-4.453979,-0.690261,-9.210534,-1.801145,9.288532,5.919426,1.943729,2.828268,9.204357,4.825000,7.217649,-6.016618,5.601077,-0.621548,-1.560788,-2.004152,2.876187,6.784901,-1.516624,2.143081,-6.681526,9.342941,-5.299979,-7.870999,3.770479,-7.915562,-6.092335,-4.311186,-9.432594,2.987621,9.514211,9.371402,-1.756296,-0.689027,7.175962,-2.045064,1.080265,6.786932,-4.480197,3.913349,2.879725,7.363886,-0.910169,-9.436000,-9.885421,-8.736713,1.503887,-9.066823,-7.244497,-2.912020,9.290840,7.031173,-3.412219,-2.395276,-2.114469,4.757534,8.935484,-1.699341,-1.731488,-1.741793,-2.621440,-4.368787,0.052396,1.750913,-3.817837,4.239340,-8.953713,-0.163151,8.334423,9.279990,-5.337645,-0.128560,6.385535,-2.876542,1.516206,9.464429,2.328119,6.262656,-1.626316,-5.403278,1.486392,-5.799138,-7.398743,-8.466072,1.010955,-8.353927,-8.074762,-7.054229,2.258204,9.367228,0.299580,-7.732345,0.024477,9.616348,-1.839536,-3.191663,3.227880,7.959943,2.475521,-4.288571,9.590932,-8.897148,7.669088,-2.322633,7.067636,9.597438,-8.192261,5.471761,8.184591,5.493346,-8.363236,1.690901,2.242286,-0.684931,0.058637,2.992320,1.710688,-0.042550,-6.148596,0.784630,5.206412,6.440731,-7.702052,8.818199,4.921938,1.728462,-2.032870,-9.722509,0.105262,-9.918030,9.675491,4.451021,1.261757,5.886158,-1.613401,-4.824407,2.931990,5.350126,-9.880084,3.139257,-3.940744,-8.335413,-9.811105,-5.361551,3.381929,-2.923421,-7.577273,1.687771,0.753172,-8.097682,4.949857,4.866583,-3.279368,-1.436126,5.500963,-7.203237,-7.238419,-9.572883,5.757606,-9.278917,4.815036,6.048313,-9.880418,-6.272337,4.899762,-7.353364,5.515723,1.686271,-4.166131,-3.505344,-4.773343,7.344909,6.642734,7.018143,-5.850565,1.649798,-3.053705,-7.729820,1.375299,-9.683184,2.517023,4.800848,3.703646,-6.220544,-4.392067,8.526701,6.770075,7.339920,5.362554,-2.420847,-5.758698,2.470834,-8.557893,-9.790517,-9.875111,6.084397,6.153254,-0.393565,5.710628,-9.267327,-6.658181,-6.209777,1.575577,-7.818979,-9.656504,-0.893938,6.164944,8.979762,7.859642,4.675371,4.242655,4.998178,-5.477304,3.762150,-1.671084,9.759587,4.251062,2.232506,-2.748846,6.491917,-1.280045,4.806447,-3.472051,1.549130,-3.301510,4.872747,0.935763,-7.733550,2.378944,-2.173955,-7.911210,-1.613681,1.453236,-7.626429,4.433349,6.769520,0.810323,9.987859,9.452977,-8.634418,-6.097876,1.377145,-3.573249,4.826457,3.242022,-0.494392,6.481578,-5.088763,-3.879550,-7.487682,-5.743741,5.771104,2.104842,2.231149,1.160572,-5.459542,-1.024668,-2.968896,-4.160761,-3.197968,1.720982,8.072616,4.922535,0.086426,-8.604534,3.985844,5.194932,-6.999401,-9.958637,-6.299871,8.416635,9.124928,-7.355477,3.422500,6.516808,6.829594,-6.169864,2.943092,-5.960998,7.203743,7.164197,1.376783,3.754730,2.083558,-9.792465,6.643113,-6.355346,4.911385,-1.276410,6.013776,-5.815743,-4.183614,1.827841,-4.225017,0.703545,-4.625268,-6.729822,2.511078,-1.275674,0.349732,-0.933686,-0.659412,8.748840,-8.680901,-5.008585,6.811571,-1.045015,9.931890,-3.462638,8.316123,5.259073,-7.049300,1.956774,7.444064,-5.827233,-6.232992,-1.706797,6.818288,-8.924019,6.848955], dtype = "float64")#candidate|5648|(980,)|const|float64
var_5649 = relay.var("var_5649", dtype = "float64", shape = (90,))#candidate|5649|(90,)|var|float64
call_5647 = relay.TupleGetItem(func_5043_call(relay.reshape(const_5648.astype('float64'), [10, 14, 7]), relay.reshape(var_5649.astype('float64'), [90,]), ), 0)
call_5650 = relay.TupleGetItem(func_5047_call(relay.reshape(const_5648.astype('float64'), [10, 14, 7]), relay.reshape(var_5649.astype('float64'), [90,]), ), 0)
output = relay.Tuple([call_5641,call_5647,const_5648,var_5649,])
output2 = relay.Tuple([call_5642,call_5650,const_5648,var_5649,])
func_5652 = relay.Function([var_5649,], output)
mod['func_5652'] = func_5652
mod = relay.transform.InferType()(mod)
var_5653 = relay.var("var_5653", dtype = "float64", shape = (90,))#candidate|5653|(90,)|var|float64
output = func_5652(var_5653)
func_5654 = relay.Function([var_5653], output)
mutated_mod['func_5654'] = func_5654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4951_call = mod.get_global_var('func_4951')
func_4953_call = mutated_mod.get_global_var('func_4953')
call_5686 = relay.TupleGetItem(func_4951_call(), 0)
call_5687 = relay.TupleGetItem(func_4953_call(), 0)
output = call_5686
output2 = call_5687
func_5691 = relay.Function([], output)
mod['func_5691'] = func_5691
mod = relay.transform.InferType()(mod)
mutated_mod['func_5691'] = func_5691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5691_call = mutated_mod.get_global_var('func_5691')
call_5692 = func_5691_call()
output = call_5692
func_5693 = relay.Function([], output)
mutated_mod['func_5693'] = func_5693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_5694 = relay.TupleGetItem(func_5509_call(), 1)
call_5695 = relay.TupleGetItem(func_5511_call(), 1)
var_5709 = relay.var("var_5709", dtype = "float64", shape = (14, 16, 14))#candidate|5709|(14, 16, 14)|var|float64
bop_5710 = relay.power(call_5694.astype('float32'), var_5709.astype('float32')) # shape=(14, 16, 14)
bop_5713 = relay.power(call_5695.astype('float32'), var_5709.astype('float32')) # shape=(14, 16, 14)
output = relay.Tuple([bop_5710,])
output2 = relay.Tuple([bop_5713,])
func_5716 = relay.Function([var_5709,], output)
mod['func_5716'] = func_5716
mod = relay.transform.InferType()(mod)
var_5717 = relay.var("var_5717", dtype = "float64", shape = (14, 16, 14))#candidate|5717|(14, 16, 14)|var|float64
output = func_5716(var_5717)
func_5718 = relay.Function([var_5717], output)
mutated_mod['func_5718'] = func_5718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_5748 = func_3789_call()
call_5749 = func_3789_call()
func_5384_call = mod.get_global_var('func_5384')
func_5385_call = mutated_mod.get_global_var('func_5385')
call_5755 = relay.TupleGetItem(func_5384_call(), 0)
call_5756 = relay.TupleGetItem(func_5385_call(), 0)
output = relay.Tuple([call_5748,call_5755,])
output2 = relay.Tuple([call_5749,call_5756,])
func_5757 = relay.Function([], output)
mod['func_5757'] = func_5757
mod = relay.transform.InferType()(mod)
output = func_5757()
func_5758 = relay.Function([], output)
mutated_mod['func_5758'] = func_5758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5384_call = mod.get_global_var('func_5384')
func_5385_call = mutated_mod.get_global_var('func_5385')
call_5764 = relay.TupleGetItem(func_5384_call(), 0)
call_5765 = relay.TupleGetItem(func_5385_call(), 0)
uop_5766 = relay.cosh(call_5764.astype('float32')) # shape=(14, 3, 14)
uop_5768 = relay.cosh(call_5765.astype('float32')) # shape=(14, 3, 14)
uop_5769 = relay.erf(uop_5766.astype('float32')) # shape=(14, 3, 14)
uop_5771 = relay.erf(uop_5768.astype('float32')) # shape=(14, 3, 14)
uop_5777 = relay.sinh(uop_5766.astype('float64')) # shape=(14, 3, 14)
uop_5779 = relay.sinh(uop_5768.astype('float64')) # shape=(14, 3, 14)
output = relay.Tuple([uop_5769,uop_5777,])
output2 = relay.Tuple([uop_5771,uop_5779,])
func_5782 = relay.Function([], output)
mod['func_5782'] = func_5782
mod = relay.transform.InferType()(mod)
mutated_mod['func_5782'] = func_5782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5782_call = mutated_mod.get_global_var('func_5782')
call_5783 = func_5782_call()
output = call_5783
func_5784 = relay.Function([], output)
mutated_mod['func_5784'] = func_5784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mod.get_global_var('func_3065')
func_3067_call = mutated_mod.get_global_var('func_3067')
call_5805 = func_3065_call()
call_5806 = func_3065_call()
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
const_5814 = relay.const([[-6,-7,-5,-6,9,8,-10,-9,9,-8,10,1,10,5,-2,1,-10,-10,3,1,-5,7,-1,-10,8,5,9,10,-4,1,-6,1,-9,10,8,-6,-10,8,-9,2,-8,3,-5,-7,10,2,-8,-9,-7,-1,-10,-7,7,-4,6,4,-2,-1,2,5,-6,5,3,3,4,-4,10,-7,-7,-5,-6,6,8,7,5,-9,3,5,9,-6,3,-9,9,1,-8,8,-9,-6,-2,-4,-6,-6,-8,-5,-10,-2,-8,5,1,-3,6,5,-6,10,-3,-2,9,8,-2,6,1,-2,-3,6,7,-2,-1,-8,-7,4,5,7,-6,3,7,10,9,6,-1,3,4,-10,-2,3,-9,7,2,7,-10,-8,10,-4,-1,9,3,-1,9,3,2,-1,10,2,-4,4,9,-1,-1,6,-5,6,-10,6,-10,1,4,10,9,-10,3,7,7,9,-4,9,-3,-1,4,2,-8,-4,2,6,8,-4,-9,2,-8,-5,-9,4,-1,-5]], dtype = "int16")#candidate|5814|(1, 192)|const|int16
call_5813 = relay.TupleGetItem(func_64_call(relay.reshape(const_5814.astype('int16'), [12, 8, 2])), 0)
call_5815 = relay.TupleGetItem(func_66_call(relay.reshape(const_5814.astype('int16'), [12, 8, 2])), 0)
output = relay.Tuple([call_5805,call_5813,const_5814,])
output2 = relay.Tuple([call_5806,call_5815,const_5814,])
func_5816 = relay.Function([], output)
mod['func_5816'] = func_5816
mod = relay.transform.InferType()(mod)
output = func_5816()
func_5817 = relay.Function([], output)
mutated_mod['func_5817'] = func_5817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5691_call = mod.get_global_var('func_5691')
func_5693_call = mutated_mod.get_global_var('func_5693')
call_5818 = func_5691_call()
call_5819 = func_5691_call()
var_5824 = relay.var("var_5824", dtype = "float64", shape = (14, 6, 14))#candidate|5824|(14, 6, 14)|var|float64
bop_5825 = relay.equal(call_5818.astype('bool'), var_5824.astype('bool')) # shape=(14, 6, 14)
bop_5828 = relay.equal(call_5819.astype('bool'), var_5824.astype('bool')) # shape=(14, 6, 14)
output = relay.Tuple([bop_5825,])
output2 = relay.Tuple([bop_5828,])
func_5833 = relay.Function([var_5824,], output)
mod['func_5833'] = func_5833
mod = relay.transform.InferType()(mod)
var_5834 = relay.var("var_5834", dtype = "float64", shape = (14, 6, 14))#candidate|5834|(14, 6, 14)|var|float64
output = func_5833(var_5834)
func_5835 = relay.Function([var_5834], output)
mutated_mod['func_5835'] = func_5835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2754_call = mod.get_global_var('func_2754')
func_2756_call = mutated_mod.get_global_var('func_2756')
call_5854 = func_2754_call()
call_5855 = func_2754_call()
output = call_5854
output2 = call_5855
func_5868 = relay.Function([], output)
mod['func_5868'] = func_5868
mod = relay.transform.InferType()(mod)
output = func_5868()
func_5869 = relay.Function([], output)
mutated_mod['func_5869'] = func_5869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_5873 = func_3789_call()
call_5874 = func_3789_call()
output = relay.Tuple([call_5873,])
output2 = relay.Tuple([call_5874,])
func_5879 = relay.Function([], output)
mod['func_5879'] = func_5879
mod = relay.transform.InferType()(mod)
mutated_mod['func_5879'] = func_5879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5879_call = mutated_mod.get_global_var('func_5879')
call_5880 = func_5879_call()
output = call_5880
func_5881 = relay.Function([], output)
mutated_mod['func_5881'] = func_5881
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5884 = relay.var("var_5884", dtype = "float32", shape = (2, 7, 12))#candidate|5884|(2, 7, 12)|var|float32
uop_5885 = relay.rsqrt(var_5884.astype('float32')) # shape=(2, 7, 12)
output = relay.Tuple([uop_5885,])
output2 = relay.Tuple([uop_5885,])
func_5894 = relay.Function([var_5884,], output)
mod['func_5894'] = func_5894
mod = relay.transform.InferType()(mod)
var_5895 = relay.var("var_5895", dtype = "float32", shape = (2, 7, 12))#candidate|5895|(2, 7, 12)|var|float32
output = func_5894(var_5895)
func_5896 = relay.Function([var_5895], output)
mutated_mod['func_5896'] = func_5896
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5898 = relay.var("var_5898", dtype = "float32", shape = (6, 5, 12))#candidate|5898|(6, 5, 12)|var|float32
uop_5899 = relay.acosh(var_5898.astype('float32')) # shape=(6, 5, 12)
func_2754_call = mod.get_global_var('func_2754')
func_2756_call = mutated_mod.get_global_var('func_2756')
call_5906 = func_2754_call()
call_5907 = func_2754_call()
uop_5918 = relay.log(uop_5899.astype('float64')) # shape=(6, 5, 12)
func_3103_call = mod.get_global_var('func_3103')
func_3105_call = mutated_mod.get_global_var('func_3105')
const_5921 = relay.const([-2.415688,-4.888260,-0.946452,4.153289,-6.100194,6.008460,-2.098461,2.692120,-2.003155,2.471908,-2.164800,-2.630279,-3.366185,-4.056696,-4.359316,-5.870826,9.961972,7.413333,-9.689281,-2.871550,9.017203,-9.214189,8.819261,7.033382,-6.041864,-5.858519,-2.276370,0.926759,7.703112,-7.133003,3.126272,-7.489517,-3.537985,6.768058,-5.487105,3.627555,5.253255,9.799409,6.227285,-2.656933,9.602317,-5.666231,3.948488,4.507834,8.145920,-0.573690,-0.015360,0.503394,-1.204916,7.258428,5.645736,-1.268228,0.854072,9.554853,-2.232914,-2.722816,-2.372709,2.775027,3.601715,7.311852,0.489387,5.876369,-6.567610,-8.973890,1.635401,-0.540843,-5.403926,-0.580511,-5.366074,-8.874696,8.128989,6.446338,7.921360,-4.596059,8.309170,0.191165,7.369787,-3.685653,6.070769,8.003549,-0.065260,3.175662,-3.198946,-5.189392,7.488724,-3.178957,-3.321293,2.906508,-1.771000,-6.940356,6.803659,-1.188420,-5.952125,-8.923299,2.566318,0.417702,6.967625,-9.621035,-1.381341,1.608562,5.879181,-5.754600,4.676765,4.575902,1.132330,7.527970,9.190281,-0.651683,-7.375436,-4.148321,-6.116625,0.588782,-1.846460,1.266257,9.359591,9.556665,-8.690915,-6.143361,4.055943,-8.819507,9.450773,6.055145,1.618186,-9.523006,-6.271205,-9.256556,-9.135082,5.583780,1.615861,1.217715,4.730289,-6.756802,0.211466,2.390569,-2.460115,2.181599,2.309535,0.998385,-6.849883,-3.257192,-8.892639,1.326479,-7.929422,3.962335,-7.154086,-0.694737,6.945418,6.097777,5.799946,8.922489,-0.492690,8.462296,6.545733,3.808141,8.521191,1.153219,-2.933255,-2.595769,3.149654,-8.863540,6.991355,4.391602], dtype = "float64")#candidate|5921|(162,)|const|float64
call_5920 = relay.TupleGetItem(func_3103_call(relay.reshape(const_5921.astype('float64'), [6, 3, 9])), 1)
call_5922 = relay.TupleGetItem(func_3105_call(relay.reshape(const_5921.astype('float64'), [6, 3, 9])), 1)
func_5103_call = mod.get_global_var('func_5103')
func_5106_call = mutated_mod.get_global_var('func_5106')
var_5929 = relay.var("var_5929", dtype = "bool", shape = (588,))#candidate|5929|(588,)|var|bool
call_5928 = func_5103_call(relay.reshape(var_5929.astype('bool'), [14, 3, 14]))
call_5930 = func_5103_call(relay.reshape(var_5929.astype('bool'), [14, 3, 14]))
uop_5932 = relay.sin(uop_5918.astype('float32')) # shape=(6, 5, 12)
bop_5937 = relay.subtract(uop_5918.astype('int16'), relay.reshape(uop_5932.astype('int16'), relay.shape_of(uop_5918))) # shape=(6, 5, 12)
uop_5940 = relay.erf(bop_5937.astype('float32')) # shape=(6, 5, 12)
bop_5948 = relay.floor_mod(uop_5899.astype('float64'), relay.reshape(uop_5940.astype('float64'), relay.shape_of(uop_5899))) # shape=(6, 5, 12)
bop_5955 = relay.equal(uop_5918.astype('bool'), relay.reshape(bop_5937.astype('bool'), relay.shape_of(uop_5918))) # shape=(6, 5, 12)
uop_5961 = relay.tan(bop_5948.astype('float32')) # shape=(6, 5, 12)
output = relay.Tuple([call_5906,call_5920,const_5921,call_5928,var_5929,bop_5955,uop_5961,])
output2 = relay.Tuple([call_5907,call_5922,const_5921,call_5930,var_5929,bop_5955,uop_5961,])
func_5963 = relay.Function([var_5898,var_5929,], output)
mod['func_5963'] = func_5963
mod = relay.transform.InferType()(mod)
mutated_mod['func_5963'] = func_5963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5963_call = mutated_mod.get_global_var('func_5963')
var_5965 = relay.var("var_5965", dtype = "float32", shape = (6, 5, 12))#candidate|5965|(6, 5, 12)|var|float32
var_5966 = relay.var("var_5966", dtype = "bool", shape = (588,))#candidate|5966|(588,)|var|bool
call_5964 = func_5963_call(var_5965,var_5966,)
output = call_5964
func_5967 = relay.Function([var_5965,var_5966,], output)
mutated_mod['func_5967'] = func_5967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_5991 = func_3789_call()
call_5992 = func_3789_call()
uop_6006 = relay.atan(call_5991.astype('float32')) # shape=(14, 3, 14)
uop_6008 = relay.atan(call_5992.astype('float32')) # shape=(14, 3, 14)
func_3103_call = mod.get_global_var('func_3103')
func_3105_call = mutated_mod.get_global_var('func_3105')
var_6015 = relay.var("var_6015", dtype = "float64", shape = (18, 9))#candidate|6015|(18, 9)|var|float64
call_6014 = relay.TupleGetItem(func_3103_call(relay.reshape(var_6015.astype('float64'), [6, 3, 9])), 1)
call_6016 = relay.TupleGetItem(func_3105_call(relay.reshape(var_6015.astype('float64'), [6, 3, 9])), 1)
func_2546_call = mod.get_global_var('func_2546')
func_2549_call = mutated_mod.get_global_var('func_2549')
const_6025 = relay.const([10,-6,-2,2,1,-9,-10,-4,-9,8,-1,5,8,6,-5,-2,3,-6,8,-10,9,4,8,2,6,9,-8,-7,2,-2,2,-3,-3,-9,8,9,-9,-7,-10,-8,8,4,-2,6,6], dtype = "int32")#candidate|6025|(45,)|const|int32
call_6024 = relay.TupleGetItem(func_2546_call(relay.reshape(const_6025.astype('int32'), [45,])), 0)
call_6026 = relay.TupleGetItem(func_2549_call(relay.reshape(const_6025.astype('int32'), [45,])), 0)
uop_6031 = relay.asinh(uop_6006.astype('float32')) # shape=(14, 3, 14)
uop_6033 = relay.asinh(uop_6008.astype('float32')) # shape=(14, 3, 14)
bop_6042 = relay.less_equal(uop_6031.astype('bool'), relay.reshape(uop_6006.astype('bool'), relay.shape_of(uop_6031))) # shape=(14, 3, 14)
bop_6045 = relay.less_equal(uop_6033.astype('bool'), relay.reshape(uop_6008.astype('bool'), relay.shape_of(uop_6033))) # shape=(14, 3, 14)
output = relay.Tuple([call_6014,var_6015,call_6024,const_6025,bop_6042,])
output2 = relay.Tuple([call_6016,var_6015,call_6026,const_6025,bop_6045,])
func_6048 = relay.Function([var_6015,], output)
mod['func_6048'] = func_6048
mod = relay.transform.InferType()(mod)
mutated_mod['func_6048'] = func_6048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6049 = relay.var("var_6049", dtype = "float64", shape = (18, 9))#candidate|6049|(18, 9)|var|float64
func_6048_call = mutated_mod.get_global_var('func_6048')
call_6050 = func_6048_call(var_6049)
output = call_6050
func_6051 = relay.Function([var_6049], output)
mutated_mod['func_6051'] = func_6051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_6060 = func_3789_call()
call_6061 = func_3789_call()
func_5963_call = mod.get_global_var('func_5963')
func_5967_call = mutated_mod.get_global_var('func_5967')
const_6085 = relay.const([-9.074965,2.211338,8.375516,-3.234520,1.203310,2.816838,7.501928,7.643720,5.696078,7.466565,9.927573,6.790799,1.720191,-6.111956,7.676169,-5.663690,1.618336,4.989433,-0.378367,7.119194,-8.550486,-8.641882,5.565235,-9.396678,3.010930,-5.083244,-1.256704,-4.496765,6.771629,-4.225761,-5.225681,-0.093687,-5.818661,7.220591,-9.383971,4.502659,6.652597,-9.597023,6.476794,-6.927091,-2.914786,-5.103001,-9.278779,-9.465410,7.194472,-9.445180,-1.432745,5.994549,-5.258509,4.703621,5.817316,-3.484342,-0.875816,5.713752,4.963671,-6.648005,-2.533286,-7.597760,2.991004,-8.757007,4.037934,-2.915597,-5.953015,2.663670,-8.157474,2.183519,6.844108,4.367779,-3.649385,0.364482,-5.159565,0.176672,-1.500712,6.225917,-0.691744,-9.246948,-2.555259,5.024239,-4.437122,-5.900171,2.410036,-2.495753,8.410355,-9.738969,-5.197917,9.223076,4.327438,9.779874,-2.245965,6.897873,5.555693,-5.180682,2.931881,-3.070643,-2.061709,-8.403735,-2.970353,-3.412501,-6.066591,2.044647,4.276575,1.418778,0.540014,-0.130478,2.796767,-6.011205,-1.004372,0.961494,4.897819,9.760467,-0.702189,2.286277,6.334717,-8.525004,0.988473,-3.044686,-8.021231,0.027252,3.127853,4.417265,-0.251478,0.945427,-3.026590,-3.606415,-8.873430,-0.492439,3.020681,9.848535,0.885337,9.439044,6.359038,6.383058,2.516609,8.412253,8.806785,-0.620546,-2.895355,-6.380924,-6.251965,-4.987048,-9.798643,0.192238,3.965119,-1.509855,-3.634102,6.770764,-6.702008,1.699025,7.603027,-5.548604,9.951008,-8.496177,-5.782837,-7.242639,5.391092,8.720408,3.972794,-6.116734,0.597128,-8.138394,-2.022670,6.371811,-8.215625,-3.119323,9.542938,-6.550492,6.749620,-2.469980,1.445223,-6.488796,-9.675631,8.460507,-4.527819,-2.557127,-7.020378,9.186966,-0.479154,0.597850,6.203414,-8.513329,-0.131960,9.919624,-5.365797,1.613290,2.622157,-1.514193,1.873895,7.441659,1.676770,6.493332,-0.630049,-3.054033,1.257727,-7.190598,-4.978978,4.441950,9.793590,-6.707709,7.117160,-8.972293,-7.445743,-8.611751,-6.593418,7.546307,0.774158,7.218271,-3.907601,-1.584266,-7.552507,-6.468394,9.953947,2.589564,1.899001,-4.164172,-9.618157,6.963824,-7.666227,-9.086688,5.079441,-2.987516,0.806067,2.998206,-8.875483,3.562466,-3.663439,4.491434,-2.024587,-4.669894,-9.327325,-7.913503,8.445859,5.958367,7.314302,-6.529508,-2.388795,9.209993,8.467832,6.269450,-7.242848,-1.199020,-8.279446,-9.162967,-7.779269,-1.539451,-1.309885,3.028505,-8.788799,1.626617,8.309575,3.820686,-9.035418,5.613571,0.647972,3.529040,6.192908,-6.160098,0.516878,-8.353473,2.054130,6.145595,2.707093,-0.379375,1.793535,3.318797,7.291780,-2.392243,1.158979,2.963983,-8.821115,-3.099442,-6.942568,-3.625041,-2.971208,-1.302145,0.448646,4.513017,-9.490304,7.382227,1.101203,-7.667189,8.937378,-2.916560,-9.491246,2.315425,0.161791,0.091266,-4.501185,7.807784,-0.072930,-0.045518,5.901661,4.606335,9.079724,-2.340075,3.720753,-3.598826,9.268343,-7.255972,-2.596583,7.698979,8.338674,-2.144094,-9.223083,-7.480121,9.496832,-2.125641,-3.269107,-2.075082,-7.040633,-6.054883,-4.683578,-6.199660,-2.824999,3.118424,-7.430589,-8.835791,3.756224,3.385772,-8.535503,6.689331,0.116541,1.845497,9.193090,7.785269,-8.244478,7.944589,-9.615866,-5.255960,-8.320742,-5.603332,-2.841448,3.170032,7.312332,0.476986,-9.765499,1.476139,7.105126,-3.233526,-8.527184,-6.418713,2.626212,9.140344,-5.916652,-3.392559,-7.779174,1.097018,7.686594,-9.939167,-2.492666,0.014163,-2.140838,-4.233169,9.321999,-5.402679,-6.136319,-4.812307,8.378828,-5.308209,2.685298,-3.337863], dtype = "float32")#candidate|6085|(360,)|const|float32
call_6084 = relay.TupleGetItem(func_5963_call(relay.reshape(const_6085.astype('float32'), [6, 5, 12]), relay.reshape(call_6060.astype('bool'), [588,]), ), 6)
call_6086 = relay.TupleGetItem(func_5967_call(relay.reshape(const_6085.astype('float32'), [6, 5, 12]), relay.reshape(call_6060.astype('bool'), [588,]), ), 6)
output = relay.Tuple([call_6060,call_6084,const_6085,])
output2 = relay.Tuple([call_6061,call_6086,const_6085,])
func_6108 = relay.Function([], output)
mod['func_6108'] = func_6108
mod = relay.transform.InferType()(mod)
mutated_mod['func_6108'] = func_6108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6108_call = mutated_mod.get_global_var('func_6108')
call_6109 = func_6108_call()
output = call_6109
func_6110 = relay.Function([], output)
mutated_mod['func_6110'] = func_6110
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6186 = relay.var("var_6186", dtype = "float64", shape = (11, 12, 4))#candidate|6186|(11, 12, 4)|var|float64
uop_6187 = relay.cos(var_6186.astype('float64')) # shape=(11, 12, 4)
output = uop_6187
output2 = uop_6187
func_6192 = relay.Function([var_6186,], output)
mod['func_6192'] = func_6192
mod = relay.transform.InferType()(mod)
var_6193 = relay.var("var_6193", dtype = "float64", shape = (11, 12, 4))#candidate|6193|(11, 12, 4)|var|float64
output = func_6192(var_6193)
func_6194 = relay.Function([var_6193], output)
mutated_mod['func_6194'] = func_6194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3423_call = mod.get_global_var('func_3423')
func_3424_call = mutated_mod.get_global_var('func_3424')
call_6229 = relay.TupleGetItem(func_3423_call(), 0)
call_6230 = relay.TupleGetItem(func_3424_call(), 0)
var_6239 = relay.var("var_6239", dtype = "float64", shape = (14, 10, 14))#candidate|6239|(14, 10, 14)|var|float64
bop_6240 = relay.logical_xor(call_6229.astype('int8'), var_6239.astype('int8')) # shape=(14, 10, 14)
bop_6243 = relay.logical_xor(call_6230.astype('int8'), var_6239.astype('int8')) # shape=(14, 10, 14)
output = relay.Tuple([bop_6240,])
output2 = relay.Tuple([bop_6243,])
func_6248 = relay.Function([var_6239,], output)
mod['func_6248'] = func_6248
mod = relay.transform.InferType()(mod)
var_6249 = relay.var("var_6249", dtype = "float64", shape = (14, 10, 14))#candidate|6249|(14, 10, 14)|var|float64
output = func_6248(var_6249)
func_6250 = relay.Function([var_6249], output)
mutated_mod['func_6250'] = func_6250
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6254 = relay.var("var_6254", dtype = "float32", shape = (5, 15))#candidate|6254|(5, 15)|var|float32
uop_6255 = relay.atanh(var_6254.astype('float32')) # shape=(5, 15)
output = uop_6255
output2 = uop_6255
func_6260 = relay.Function([var_6254,], output)
mod['func_6260'] = func_6260
mod = relay.transform.InferType()(mod)
mutated_mod['func_6260'] = func_6260
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6261 = relay.var("var_6261", dtype = "float32", shape = (5, 15))#candidate|6261|(5, 15)|var|float32
func_6260_call = mutated_mod.get_global_var('func_6260')
call_6262 = func_6260_call(var_6261)
output = call_6262
func_6263 = relay.Function([var_6261], output)
mutated_mod['func_6263'] = func_6263
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6265 = relay.const([[[-7.685271,-4.454183,-9.838094,-6.744076,-0.421341,9.381574,9.424338,9.994821,-9.508875,-3.190676,0.100260,7.330727,-9.621940],[-9.945382,0.408871,8.943768,-4.136517,1.823152,5.987845,3.057871,3.113432,8.114994,7.068912,2.105114,3.022386,5.684955],[-0.305606,-8.406851,-8.199074,5.178894,-9.138591,6.986269,-3.339842,-4.984163,3.067500,3.129694,-0.706569,1.051040,7.101594],[7.702238,9.646107,4.782870,1.739065,-6.824953,7.700217,-2.410545,5.670585,-0.149330,-3.754624,7.628269,-4.926573,8.077035],[0.107475,8.819543,1.226311,-3.287236,0.582294,0.183221,3.893281,-4.954628,5.726530,-6.560840,7.805316,-5.629731,4.026952],[9.042345,-0.667435,-9.968167,9.998493,2.222850,-2.324621,7.681139,4.336843,7.224093,9.055890,2.570329,-8.315862,3.286276],[-5.411540,9.531027,1.163094,-4.739906,0.947071,8.034731,-3.426806,-4.410590,-7.454637,-9.624461,-2.603162,-3.267700,8.513263],[-3.655461,-0.197433,5.911563,2.188682,-6.862180,3.432308,-2.668292,-2.703797,-4.696007,-9.713091,6.584510,-3.990557,6.577877]],[[8.077248,-8.345728,9.998579,-4.876163,-6.441736,5.149394,5.299128,-8.101796,-3.558308,3.864101,9.219719,5.859637,-0.490692],[-5.198808,-3.622131,8.071425,-2.047139,-5.794998,-4.652730,1.836130,6.092398,-3.254309,-4.248039,9.391233,-2.866644,6.532318],[-0.468528,3.428258,-3.428489,-7.393488,3.125320,-5.987319,6.300433,-0.374565,-6.571453,3.619424,-5.597146,-6.473902,-9.521642],[3.151742,-8.038593,-8.176447,9.723180,-0.742022,-9.451802,-2.968155,-4.508027,8.352336,3.726820,-9.395582,9.483896,3.367358],[8.573961,-6.478911,-5.907132,-6.613473,0.117816,7.288047,3.621070,-3.902502,-5.652288,3.194627,0.717178,0.306704,-0.124353],[-9.419847,4.032414,1.129000,1.241436,-4.695939,4.493027,9.290345,-4.231804,1.924293,-6.115204,9.709827,-1.127338,5.482842],[3.626391,8.060092,-9.683162,3.866128,7.271647,6.065749,-0.166207,-7.967254,-0.532364,-2.315095,5.880238,-5.771064,2.330116],[-0.103735,8.554582,-8.819693,-1.476491,-9.112567,4.570237,-9.673850,5.792452,-2.532158,-6.640184,6.644546,-3.014735,2.410446]],[[-7.454411,8.248646,8.267712,0.513106,1.317623,8.684691,8.712267,0.066365,6.706054,-2.646058,6.041086,-3.739892,0.118748],[-6.887826,-4.539378,7.494166,-0.012560,-1.906906,7.902097,-2.634552,4.944009,-5.925715,0.070048,-4.109809,-2.847375,6.300772],[8.968671,8.249572,-0.186169,-0.463733,8.265752,6.271975,-8.776051,8.829023,2.387391,-5.815080,9.353276,-7.210347,-3.877240],[8.365531,4.450718,-1.550297,-9.110696,5.356616,-5.957651,3.653457,-0.952672,1.255636,8.611635,-3.906850,-8.424726,4.702414],[2.166578,-9.494613,-8.364380,-8.190523,6.772912,-9.214672,-9.438703,-4.694033,4.441520,-7.946821,-9.002099,-3.255556,-0.243889],[-7.700967,-7.685368,-7.702967,0.990432,2.864627,-0.835327,4.156767,3.498762,-4.251858,-5.986628,-5.718105,-6.317247,4.482000],[-5.544226,-9.320002,-0.028686,2.870527,0.935854,-4.821977,-1.468167,-5.080029,-8.738927,-9.153508,-4.091576,7.435204,2.582101],[-3.755311,7.027629,-3.908814,-4.672620,-1.827499,-4.679681,1.425545,-0.064560,-9.272277,9.610789,0.967363,0.544903,2.914386]],[[-2.371027,-5.942058,-7.073015,-6.143993,-9.344772,8.250134,0.214743,7.674164,6.474335,1.780793,-5.379708,3.878239,6.197394],[3.901787,-5.496377,-9.934498,-1.907263,5.971780,8.423580,-5.140626,-2.355592,-7.693883,3.866465,0.691669,-4.675488,-7.499459],[8.402110,0.108581,6.571154,4.744711,6.246139,-0.734222,-5.835548,7.782132,7.914201,6.216697,0.323913,-9.531373,5.098599],[-7.792456,-8.350134,-4.913536,-7.695398,-3.833627,7.798064,1.245031,6.840863,-5.273707,9.271310,-9.614660,1.664944,7.115604],[5.546372,3.832755,3.812407,1.780692,8.683906,9.208892,3.703820,5.532368,1.390177,5.941990,-7.963959,-5.513753,0.037758],[6.272282,-6.218258,-6.660046,-4.566218,-2.371359,6.262670,4.425058,-5.183417,-3.584323,5.882765,-1.304410,-2.231217,5.146120],[7.200640,4.095983,-8.558476,5.850466,5.848488,7.827646,7.058472,8.332829,6.095696,9.373416,-6.733519,0.318064,5.021426],[-8.039335,0.683886,4.684924,-5.843098,-2.552655,0.420539,0.413395,9.866889,-7.860114,5.131962,4.497407,-0.966626,-8.057189]],[[-4.613001,-9.891758,2.569506,6.244589,4.502797,6.167321,0.996447,-2.639955,4.171074,4.804527,-4.608922,0.268521,-3.997907],[-4.225897,-0.885103,4.102945,-8.626878,-2.607416,-9.004733,4.718103,-1.446080,0.682542,-1.250958,-5.117879,-9.513345,-3.900807],[0.155049,-0.368721,-4.749104,2.610324,9.693134,5.046097,-7.708606,3.831696,4.229185,-7.748455,1.736936,-2.285903,-3.791087],[5.504774,-2.544714,9.185319,6.602654,1.789760,2.581653,-2.462010,3.208610,-1.875139,-3.808274,9.914730,-3.359778,1.309767],[5.346772,1.287830,6.162394,-4.832160,-5.743754,5.620494,0.063144,7.749819,2.011966,2.534189,9.761050,9.296369,2.322038],[-5.368699,-2.501681,3.080849,6.970068,5.624524,0.663793,-9.111428,-0.788211,-9.753073,1.462494,-3.769942,4.166333,6.159281],[7.044327,-7.993751,7.997281,3.721194,1.086147,-9.023954,9.806259,8.260198,2.493649,9.669988,9.736267,-4.226501,5.296594],[-3.449551,-0.467270,-4.406320,-6.222423,9.840052,3.075752,1.461243,3.834370,7.676012,-2.075951,-5.319795,-2.361868,9.190743]],[[6.720669,-3.895383,-5.463515,3.564821,8.875903,-0.376283,2.519734,0.310331,-4.293635,7.318949,-7.599424,5.432685,8.022942],[8.440387,7.001785,0.625927,-1.098560,2.369712,-4.247869,3.162420,-1.734548,7.804447,1.261420,-2.294550,-9.135540,-4.773636],[-9.820834,9.814280,7.565680,-5.679221,5.411558,7.170177,1.968987,-8.560277,7.380620,9.772209,5.672604,6.647071,-9.209519],[3.370373,3.808278,3.110862,5.288057,8.853598,3.856644,0.027133,-7.290799,-2.742830,6.466359,0.652076,7.142752,8.960307],[-5.885909,4.825322,-4.434325,6.770111,-1.138991,-0.337842,1.103991,-1.860335,6.823722,1.583374,-9.906143,8.598942,-0.947642],[2.539193,-9.624097,-5.941300,4.606781,1.769042,-2.309867,-8.047835,5.300548,-5.248630,-5.486881,-0.357050,-1.400100,7.510772],[4.410802,2.771765,-7.596970,0.371181,1.022216,7.096501,-9.886955,-1.383619,6.844907,9.491643,9.271852,3.312172,1.231892],[3.232938,1.199192,-5.835336,-8.123538,-6.603695,-2.691280,2.612777,6.590996,9.492488,4.452943,9.813671,-2.084513,4.764205]],[[-2.930551,9.724718,-6.930130,-8.028222,-8.773305,6.193304,-2.365342,2.599522,7.402409,-6.986532,6.681159,-8.080377,7.885046],[9.774854,5.859447,-0.897404,4.085692,3.075893,-3.543737,8.198516,-3.863209,2.910615,-4.172744,-7.572958,6.851008,-5.540547],[-1.722382,1.677636,-5.006983,4.888648,-1.797446,-1.742407,0.035739,6.111057,9.950812,-2.242608,3.381640,-8.295108,-8.100206],[-0.635985,5.696557,-9.353439,6.922087,3.337678,-1.145463,6.422375,-4.448957,-8.723841,9.836217,-9.287567,-6.015411,8.036621],[-2.681091,1.656356,-9.370287,8.263582,8.099896,3.304047,4.922018,-5.589260,0.958175,-6.979345,7.542142,5.552231,1.041958],[1.004046,3.212900,7.762733,-2.311396,-1.953229,-9.334367,-5.243250,-9.329400,7.356855,8.293788,6.738202,5.194141,-4.216360],[5.744348,-2.223764,9.820193,-5.731035,-0.950877,6.132831,1.062781,0.520990,4.648209,3.464271,2.003184,4.107628,-6.887657],[9.035948,3.133074,8.534022,1.641331,6.041888,9.432474,7.042902,1.669637,0.454700,9.866109,9.470164,-8.188822,-0.095206]]], dtype = "float32")#candidate|6265|(7, 8, 13)|const|float32
var_6266 = relay.var("var_6266", dtype = "float32", shape = (7, 8, 13))#candidate|6266|(7, 8, 13)|var|float32
bop_6267 = relay.maximum(const_6265.astype('float32'), relay.reshape(var_6266.astype('float32'), relay.shape_of(const_6265))) # shape=(7, 8, 13)
output = relay.Tuple([bop_6267,])
output2 = relay.Tuple([bop_6267,])
func_6285 = relay.Function([var_6266,], output)
mod['func_6285'] = func_6285
mod = relay.transform.InferType()(mod)
mutated_mod['func_6285'] = func_6285
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6286 = relay.var("var_6286", dtype = "float32", shape = (7, 8, 13))#candidate|6286|(7, 8, 13)|var|float32
func_6285_call = mutated_mod.get_global_var('func_6285')
call_6287 = func_6285_call(var_6286)
output = call_6287
func_6288 = relay.Function([var_6286], output)
mutated_mod['func_6288'] = func_6288
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6292 = relay.var("var_6292", dtype = "int16", shape = (6, 7, 1))#candidate|6292|(6, 7, 1)|var|int16
var_6293 = relay.var("var_6293", dtype = "int16", shape = (6, 7, 12))#candidate|6293|(6, 7, 12)|var|int16
bop_6294 = relay.right_shift(var_6292.astype('int16'), var_6293.astype('int16')) # shape=(6, 7, 12)
output = bop_6294
output2 = bop_6294
F = relay.Function([var_6292,var_6293,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6292,var_6293,], output2)
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
