import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_344 = relay.var("var_344", dtype = "uint8", shape = (6, 1, 15))#candidate|344|(6, 1, 15)|var|uint8
const_345 = relay.const([[[3,1,-4,-5,8,6,4,6,-5,6,-3,-5,-1,6,-3],[7,6,10,-4,-10,4,6,3,9,-7,1,1,5,-10,-2],[-5,-9,-7,-4,1,-5,9,-4,-3,10,10,-2,-9,5,-9],[-10,-5,7,7,5,5,-4,3,-7,-3,-6,10,5,6,7],[-6,2,-8,-5,10,5,-2,-10,-7,1,5,4,-7,3,9],[-1,-10,8,9,5,3,-5,-6,-2,-1,4,2,9,9,5],[5,4,-6,-3,6,-6,-7,6,5,8,-10,-10,-2,-4,-3],[10,-4,3,-7,-8,-6,3,-5,-9,-6,-4,1,1,-5,4],[-3,-9,-9,10,1,-10,-2,2,-2,8,8,-4,-8,-2,-9],[4,-3,10,5,9,-6,5,-1,-5,-6,9,-7,-2,-8,-9],[-3,1,-7,-7,1,-10,-4,-6,10,8,-4,-9,-1,-7,7],[8,-10,5,9,2,9,-6,-7,-8,4,2,-4,-1,5,-4]],[[6,2,10,-5,-1,-7,-9,5,-7,-2,10,9,8,-9,-9],[-3,4,1,3,2,-3,6,6,-9,-6,-2,-8,2,-2,-6],[3,-6,-7,10,-2,-5,5,-10,-5,-2,1,-9,8,2,-2],[10,10,-2,-2,-6,-7,1,2,-3,-10,10,-2,10,-10,-9],[-3,-8,3,-1,-2,-9,-7,3,2,8,2,3,9,-3,8],[-3,-8,-3,1,-8,-10,-4,-7,-10,-2,3,8,-7,1,-6],[-1,-7,10,-2,5,-3,-8,6,1,-6,-4,-6,-5,9,-4],[-3,4,4,4,-2,-7,-6,4,-10,-7,8,7,6,-1,-8],[-10,10,4,7,-9,9,-5,-10,-8,-4,9,10,9,10,3],[-3,-2,8,-6,-4,-3,2,9,-7,-4,-3,2,-1,-1,9],[8,8,6,5,-8,-10,3,9,1,2,4,10,-1,6,-1],[-6,10,8,10,1,-6,9,10,3,1,-9,-1,2,8,-3]],[[-5,-8,5,-5,3,2,-5,-9,8,-10,-7,3,-8,1,-3],[6,5,6,-2,-6,-7,4,-9,10,-5,4,7,-4,-4,-2],[-9,-8,-2,8,-5,1,-1,5,8,-7,4,-8,1,-8,7],[4,6,-4,-4,2,-5,3,-10,7,-4,2,8,-2,2,-5],[-10,6,-9,-4,-3,4,1,-5,6,8,8,1,-2,6,3],[-4,8,-6,-10,-10,9,10,-1,-1,-7,-8,-1,-3,-2,-6],[10,-7,-9,7,-5,2,-3,6,-7,3,-7,1,2,10,2],[-10,-5,-3,1,-6,9,10,2,5,2,5,1,-7,1,10],[5,-8,-8,-7,-10,-5,2,-10,3,2,-3,7,3,10,3],[-7,-1,-9,7,8,-10,6,-10,4,2,-9,5,1,-9,-1],[-3,1,5,-3,-7,-10,3,8,-2,7,10,-9,9,2,2],[-8,-4,-9,8,-1,-10,-3,9,-8,-4,5,10,-9,-5,-7]],[[-4,2,-6,7,2,1,3,6,-5,-2,-1,5,2,-8,-4],[-4,10,6,-8,9,5,1,-4,-9,-3,-10,-10,4,10,7],[-9,-2,-8,6,-1,3,7,-3,2,1,-5,-10,7,-6,-9],[1,-5,-8,9,-6,-9,8,4,-8,-7,2,4,-6,-7,8],[-7,-2,1,-3,4,-5,-2,-10,6,3,-8,5,6,-3,-4],[-6,1,3,-8,4,-10,6,2,6,-3,-1,-3,-3,8,9],[8,-4,3,-2,-6,4,5,-5,5,7,2,9,6,2,9],[-7,7,9,-1,-3,-9,-4,-7,3,2,-10,-10,10,2,-10],[-5,1,2,-4,-2,1,-1,10,-4,10,5,-10,8,10,4],[-4,-9,-3,-6,6,-1,1,-2,2,4,-1,1,-5,-5,-2],[5,8,-2,4,7,7,-7,-9,-9,-6,-2,-5,10,5,-3],[6,2,3,-6,-1,-9,8,7,4,10,-3,6,-9,-6,-4]],[[9,8,-4,5,-9,3,-7,3,-10,-1,8,-5,10,5,-8],[6,8,9,6,-4,-4,-3,7,2,5,-10,-7,-9,10,-6],[2,-8,-7,-4,2,-10,-6,7,10,-3,-5,8,-1,-1,-1],[-1,-9,5,5,9,-9,6,-1,-1,2,-6,8,-1,4,-9],[-8,-10,-9,-5,6,6,2,-3,4,-5,-7,-5,6,-3,7],[5,-6,4,-10,2,2,3,9,-10,1,1,-6,-4,-2,5],[3,-9,-5,-6,4,4,7,4,5,-1,9,6,-8,-10,-9],[4,-4,-1,-7,-7,5,7,-9,8,-4,2,-10,-1,-7,3],[-5,-10,-7,2,-7,5,10,-4,4,5,-2,3,3,4,-4],[-10,1,10,10,-4,-10,-9,-10,1,8,3,-3,3,8,-8],[2,1,-7,-3,-2,-1,5,-5,4,10,10,-1,-8,8,2],[8,3,9,-2,-4,7,-1,7,7,9,-5,-1,-1,3,-6]],[[-7,-2,6,10,-2,-6,-2,-1,-10,4,8,-8,8,-9,-1],[9,-9,-8,-10,5,-3,-1,8,7,2,7,1,-10,-7,1],[6,-5,10,-2,-2,-4,-9,-1,9,-5,9,3,-9,10,-4],[5,-2,-4,6,3,-4,2,-2,-8,-2,3,5,3,1,-2],[-4,-4,9,-9,6,10,10,1,6,-4,2,-2,-3,3,-8],[-6,1,-9,2,5,3,-7,-9,7,-10,6,8,1,2,-3],[10,-3,3,-3,-1,10,4,-6,-8,10,4,9,5,1,-7],[-10,-6,-8,-6,-2,9,-8,1,-8,7,-4,8,-10,7,-2],[8,1,-6,10,2,-6,6,-8,10,-4,5,-7,-5,-8,10],[7,4,9,9,-10,3,-5,-4,6,8,10,-9,-6,5,7],[4,3,-1,7,-4,-4,7,-8,10,-4,3,2,4,-6,-4],[4,6,7,2,9,5,4,3,-2,5,3,-3,-10,7,-3]]], dtype = "uint8")#candidate|345|(6, 12, 15)|const|uint8
bop_346 = relay.logical_xor(var_344.astype('uint8'), const_345.astype('uint8')) # shape=(6, 12, 15)
uop_361 = relay.log(bop_346.astype('float64')) # shape=(6, 12, 15)
bop_383 = relay.divide(uop_361.astype('float64'), var_344.astype('float64')) # shape=(6, 12, 15)
uop_387 = relay.rsqrt(bop_346.astype('float32')) # shape=(6, 12, 15)
output = relay.Tuple([bop_383,uop_387,])
output2 = relay.Tuple([bop_383,uop_387,])
func_406 = relay.Function([var_344,], output)
mod['func_406'] = func_406
mod = relay.transform.InferType()(mod)
mutated_mod['func_406'] = func_406
mutated_mod = relay.transform.InferType()(mutated_mod)
var_407 = relay.var("var_407", dtype = "uint8", shape = (6, 1, 15))#candidate|407|(6, 1, 15)|var|uint8
func_406_call = mutated_mod.get_global_var('func_406')
call_408 = func_406_call(var_407)
output = call_408
func_409 = relay.Function([var_407], output)
mutated_mod['func_409'] = func_409
mutated_mod = relay.transform.InferType()(mutated_mod)
var_547 = relay.var("var_547", dtype = "float64", shape = (15, 3, 6))#candidate|547|(15, 3, 6)|var|float64
var_548 = relay.var("var_548", dtype = "float64", shape = (15, 3, 6))#candidate|548|(15, 3, 6)|var|float64
bop_549 = relay.floor_divide(var_547.astype('float64'), relay.reshape(var_548.astype('float64'), relay.shape_of(var_547))) # shape=(15, 3, 6)
output = bop_549
output2 = bop_549
func_568 = relay.Function([var_547,var_548,], output)
mod['func_568'] = func_568
mod = relay.transform.InferType()(mod)
var_569 = relay.var("var_569", dtype = "float64", shape = (15, 3, 6))#candidate|569|(15, 3, 6)|var|float64
var_570 = relay.var("var_570", dtype = "float64", shape = (15, 3, 6))#candidate|570|(15, 3, 6)|var|float64
output = func_568(var_569,var_570,)
func_571 = relay.Function([var_569,var_570,], output)
mutated_mod['func_571'] = func_571
mutated_mod = relay.transform.InferType()(mutated_mod)
var_689 = relay.var("var_689", dtype = "float64", shape = ())#candidate|689|()|var|float64
const_690 = relay.const([[[4.059149,-5.738559,-5.188892,-2.912701,-2.500945,0.370801,5.440021,-1.889515,-3.507980]],[[3.197841,8.022567,8.942368,6.936770,-6.324973,-3.670112,1.369955,-0.164106,-9.476632]],[[4.170594,3.599143,-0.379144,1.122759,5.779065,-8.764803,1.952690,5.945912,9.685858]],[[-2.972142,7.094040,-3.302312,8.155394,8.649468,6.268767,-6.636682,6.654331,-1.013318]],[[-4.571189,3.533053,7.114883,8.761660,-2.487730,9.579589,6.022084,-0.479524,-2.383108]],[[7.496374,1.313468,-1.604841,-0.472706,9.852643,-6.845256,-6.148166,5.195326,0.365630]],[[9.755533,-8.339544,0.396133,-4.844989,9.841261,3.616415,3.777303,2.731828,-4.696124]],[[5.268225,-0.766583,-2.460728,-2.516629,6.858090,-9.355594,-6.153363,8.076071,5.074308]],[[0.581483,-3.529876,3.655196,-1.055512,-5.705760,1.264558,0.701095,4.938033,7.368441]],[[4.161420,-9.583028,2.821815,1.346932,9.586949,-8.029513,4.261230,-7.961944,0.486473]],[[3.326360,-9.000280,3.853672,-7.353062,-7.334760,0.323348,1.597721,3.774215,8.939671]],[[8.619209,-5.423043,-4.967570,6.763202,-9.393395,7.775343,9.409416,-8.607502,-3.867423]],[[3.174120,-9.793881,-5.259604,1.732359,-8.206986,-5.482673,-7.034656,-7.887721,-9.749648]],[[8.515160,-4.123525,0.367991,1.147514,1.648778,-0.021759,-3.720715,-7.682869,9.835214]]], dtype = "float64")#candidate|690|(14, 1, 9)|const|float64
bop_691 = relay.greater_equal(var_689.astype('bool'), const_690.astype('bool')) # shape=(14, 1, 9)
output = bop_691
output2 = bop_691
func_694 = relay.Function([var_689,], output)
mod['func_694'] = func_694
mod = relay.transform.InferType()(mod)
var_695 = relay.var("var_695", dtype = "float64", shape = ())#candidate|695|()|var|float64
output = func_694(var_695)
func_696 = relay.Function([var_695], output)
mutated_mod['func_696'] = func_696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_741 = relay.var("var_741", dtype = "int16", shape = ())#candidate|741|()|var|int16
var_742 = relay.var("var_742", dtype = "int16", shape = (1, 7))#candidate|742|(1, 7)|var|int16
bop_743 = relay.right_shift(var_741.astype('int16'), var_742.astype('int16')) # shape=(1, 7)
func_568_call = mod.get_global_var('func_568')
func_571_call = mutated_mod.get_global_var('func_571')
const_758 = relay.const([[7.154682,-9.853240,2.599971,4.329510,2.678718,-3.033063,9.797125,-3.901680,-5.880083,-1.711687,-6.167727,-7.753854,-9.524103,-4.657861,-1.392646,8.252638,-4.644250,-9.784490,-0.001041,-6.484914,2.058630,6.958808,-9.713715,-7.894039,8.938101,-7.498103,5.222076,-9.186494,-1.790521,-7.719013,2.651724,-9.861452,-7.632992,-7.034641,-7.493390,-6.334868,9.736733,4.052266,4.243710,9.664714,-1.006914,-2.853354,-7.416768,6.349406,4.393237,0.001351,-2.773262,3.804142,-4.830046,3.937584,-6.954846,-7.460329,8.689023,-8.351411,-1.255063,2.285164,3.646959,-4.945515,7.087629,9.292812,-0.782206,1.607341,-5.806865,1.980105,-4.800480,-8.024163,-1.937307,8.909212,-0.676527,-6.130935,3.913672,1.546672,7.229559,-2.292690,-1.401655,6.022143,4.881435,3.910146,5.889527,-9.360772,5.831916,9.648580,-2.122659,-0.193135,-6.228592,2.651772,-9.673372,-5.446317,-9.565520,-4.912512],[-6.360816,7.103818,3.402444,-7.195205,7.175803,-0.569866,4.206467,-2.944692,-3.100239,-7.321421,6.381258,-8.511483,-9.554885,0.022609,-5.540419,1.877498,-6.872577,-2.319059,7.429511,-5.194443,4.542711,-1.370926,-9.372181,-0.052748,6.105083,6.520103,-2.879512,-2.526060,3.822148,-2.649532,-3.366714,-2.118255,-7.407727,-2.460216,5.459925,2.139416,1.815579,2.911719,-5.682713,3.571053,-2.092100,8.244753,-6.563725,-0.952998,9.151775,7.041016,-7.417912,-0.134749,-5.785991,4.550273,-7.765268,7.480257,-6.446015,6.215457,-3.083088,-8.643979,-5.632909,-3.617921,6.765601,-5.919697,6.290250,-2.727989,2.058579,-8.727681,3.454789,-9.857842,-4.892246,-9.856548,-9.832839,-2.769631,-5.926405,-1.013384,-4.687688,0.182902,0.649455,-4.460249,-5.109619,-1.507371,-7.786290,1.676630,-1.264706,8.645199,9.131981,2.722965,3.571931,9.622236,-7.807169,-5.708634,-2.896956,1.922554],[3.867157,-3.846811,-0.210732,-2.831378,0.480891,4.778305,3.547490,9.783092,-2.105226,-4.254075,-7.508444,3.189298,5.218656,2.170669,0.767742,1.871652,-9.175247,-0.630189,5.222308,4.647090,8.551223,-6.575355,7.060048,8.917021,1.490808,-4.584226,2.226260,-6.052067,4.553097,-0.980443,-8.381973,-5.805953,9.477711,-9.430677,7.749496,-6.884418,-9.270533,8.585994,-9.393744,6.121409,-4.998039,5.475026,5.753026,5.066636,7.866909,5.523652,7.352360,-5.441896,2.268403,9.481212,0.968745,1.032393,3.952259,8.058125,1.011292,8.485046,-2.011868,-8.187816,-6.910756,0.745081,6.140706,-1.617187,-2.423206,-3.348320,2.934388,-6.351305,7.145296,-6.229048,-4.907369,-6.940971,-6.647097,5.473549,-5.549421,-3.652423,1.395377,-0.882108,-6.704235,-4.993923,5.081592,-7.697716,-7.888630,4.233106,-0.850649,-2.328085,-0.514965,9.476395,-7.807996,7.337078,-4.207538,-1.817534]], dtype = "float64")#candidate|758|(3, 90)|const|float64
call_757 = func_568_call(relay.reshape(const_758.astype('float64'), [15, 3, 6]), relay.reshape(const_758.astype('float64'), [15, 3, 6]), )
call_759 = func_568_call(relay.reshape(const_758.astype('float64'), [15, 3, 6]), relay.reshape(const_758.astype('float64'), [15, 3, 6]), )
output = relay.Tuple([bop_743,call_757,const_758,])
output2 = relay.Tuple([bop_743,call_759,const_758,])
func_767 = relay.Function([var_741,var_742,], output)
mod['func_767'] = func_767
mod = relay.transform.InferType()(mod)
mutated_mod['func_767'] = func_767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_767_call = mutated_mod.get_global_var('func_767')
var_769 = relay.var("var_769", dtype = "int16", shape = ())#candidate|769|()|var|int16
var_770 = relay.var("var_770", dtype = "int16", shape = (1, 7))#candidate|770|(1, 7)|var|int16
call_768 = func_767_call(var_769,var_770,)
output = call_768
func_771 = relay.Function([var_769,var_770,], output)
mutated_mod['func_771'] = func_771
mutated_mod = relay.transform.InferType()(mutated_mod)
var_865 = relay.var("var_865", dtype = "float32", shape = (2, 9, 3))#candidate|865|(2, 9, 3)|var|float32
uop_866 = relay.asinh(var_865.astype('float32')) # shape=(2, 9, 3)
func_406_call = mod.get_global_var('func_406')
func_409_call = mutated_mod.get_global_var('func_409')
const_872 = relay.const([5,8,10,-2,-6,7,8,8,-8,3,5,5,-1,2,6,10,1,7,-6,8,-7,-5,-2,-2,-6,-10,-1,2,9,2,7,-1,1,-8,6,-10,10,2,8,2,9,4,8,3,-10,-5,10,3,-3,-10,-8,5,-6,10,1,8,4,1,8,9,3,-4,1,4,-10,-4,5,-8,6,-4,10,8,-6,7,-7,3,-2,2,-4,-9,3,5,-5,-10,3,-8,6,8,-7,5], dtype = "uint8")#candidate|872|(90,)|const|uint8
call_871 = relay.TupleGetItem(func_406_call(relay.reshape(const_872.astype('uint8'), [6, 1, 15])), 0)
call_873 = relay.TupleGetItem(func_409_call(relay.reshape(const_872.astype('uint8'), [6, 1, 15])), 0)
func_767_call = mod.get_global_var('func_767')
func_771_call = mutated_mod.get_global_var('func_771')
const_902 = relay.const(7, dtype = "int16")#candidate|902|()|const|int16
const_903 = relay.const([9,-9,-2,3,3,4,1], dtype = "int16")#candidate|903|(7,)|const|int16
call_901 = relay.TupleGetItem(func_767_call(relay.reshape(const_902.astype('int16'), []), relay.reshape(const_903.astype('int16'), [1, 7]), ), 1)
call_904 = relay.TupleGetItem(func_771_call(relay.reshape(const_902.astype('int16'), []), relay.reshape(const_903.astype('int16'), [1, 7]), ), 1)
bop_912 = relay.not_equal(uop_866.astype('bool'), const_902.astype('bool')) # shape=(2, 9, 3)
output = relay.Tuple([call_871,const_872,call_901,const_903,bop_912,])
output2 = relay.Tuple([call_873,const_872,call_904,const_903,bop_912,])
func_924 = relay.Function([var_865,], output)
mod['func_924'] = func_924
mod = relay.transform.InferType()(mod)
mutated_mod['func_924'] = func_924
mutated_mod = relay.transform.InferType()(mutated_mod)
var_925 = relay.var("var_925", dtype = "float32", shape = (2, 9, 3))#candidate|925|(2, 9, 3)|var|float32
func_924_call = mutated_mod.get_global_var('func_924')
call_926 = func_924_call(var_925)
output = call_926
func_927 = relay.Function([var_925], output)
mutated_mod['func_927'] = func_927
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1293 = relay.var("var_1293", dtype = "int8", shape = (10, 4, 15))#candidate|1293|(10, 4, 15)|var|int8
var_1294 = relay.var("var_1294", dtype = "int8", shape = (10, 4, 15))#candidate|1294|(10, 4, 15)|var|int8
bop_1295 = relay.less_equal(var_1293.astype('bool'), relay.reshape(var_1294.astype('bool'), relay.shape_of(var_1293))) # shape=(10, 4, 15)
output = relay.Tuple([bop_1295,])
output2 = relay.Tuple([bop_1295,])
func_1303 = relay.Function([var_1293,var_1294,], output)
mod['func_1303'] = func_1303
mod = relay.transform.InferType()(mod)
mutated_mod['func_1303'] = func_1303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1303_call = mutated_mod.get_global_var('func_1303')
var_1305 = relay.var("var_1305", dtype = "int8", shape = (10, 4, 15))#candidate|1305|(10, 4, 15)|var|int8
var_1306 = relay.var("var_1306", dtype = "int8", shape = (10, 4, 15))#candidate|1306|(10, 4, 15)|var|int8
call_1304 = func_1303_call(var_1305,var_1306,)
output = call_1304
func_1307 = relay.Function([var_1305,var_1306,], output)
mutated_mod['func_1307'] = func_1307
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1331 = relay.const([[[-2,-4,-2,3,3,2],[-4,-4,5,5,-10,7],[6,-9,-6,10,1,-3],[3,2,-3,-3,-5,3],[-4,5,-5,-8,-10,8],[7,-5,4,-5,4,-4],[-2,-4,-3,9,7,3],[-4,5,-9,-1,-2,7],[4,2,9,-7,-4,8],[-1,-7,10,-2,-1,10],[1,8,-8,9,5,4],[-9,5,-3,1,1,-4]],[[-7,5,3,-10,7,-8],[-1,10,10,1,4,-3],[8,-3,-1,10,-3,-6],[10,-1,-3,5,3,1],[-9,3,8,-4,-9,5],[-2,-7,-2,1,10,1],[8,7,-1,-7,1,-8],[5,5,-9,-3,7,-5],[-7,-1,8,-10,7,-10],[-8,-1,-6,-9,-10,-4],[-7,9,-10,-5,5,-4],[9,1,-5,-4,-9,-3]],[[-5,5,-7,6,5,1],[2,-2,3,1,-2,-8],[5,-10,-9,1,-7,1],[5,-9,-5,-6,8,5],[6,3,-8,6,3,10],[-1,9,-7,-2,-10,-5],[-3,1,10,1,1,5],[5,5,-7,3,5,-6],[2,7,10,6,-2,5],[4,8,-1,5,4,7],[4,-9,-2,3,4,-8],[3,-10,-3,-7,-2,-4]],[[-7,1,8,5,6,3],[1,-1,-10,-9,-3,6],[-3,-4,-7,8,-7,7],[4,9,6,-9,-2,1],[-9,4,9,-7,2,-7],[-10,-5,1,4,4,7],[-9,-6,-7,2,-7,-8],[-6,-9,8,9,9,9],[-8,5,-8,3,-9,8],[-5,-1,-7,-9,6,1],[-3,4,-6,4,-5,9],[3,3,-10,9,-1,8]],[[-9,-1,6,-9,-4,-3],[-5,8,7,-7,7,4],[9,5,-4,-10,-3,-8],[-2,-7,9,9,-8,7],[-4,6,2,-1,1,-3],[-10,-8,3,-1,2,-3],[10,6,-9,-5,-7,4],[-9,2,-2,7,-7,6],[-10,5,5,-2,10,-6],[2,3,2,-1,-4,-3],[10,-10,-4,9,3,5],[-3,-6,-4,3,-2,7]],[[6,7,1,-8,-9,-7],[5,8,-1,-8,7,-9],[-6,8,9,-4,-1,6],[-10,-2,3,3,-7,-7],[-3,3,9,-2,4,-3],[-5,-9,7,-8,-10,-5],[2,-2,-8,-9,4,-10],[4,9,1,-3,10,-3],[-9,-3,3,-1,-5,-8],[-10,3,-9,-10,-4,2],[-3,-2,-9,2,-5,-7],[5,5,-9,-3,10,-6]],[[1,-3,-4,-10,10,-2],[6,8,-8,-2,-1,3],[10,10,3,8,-9,-1],[-3,-2,3,-5,7,-2],[6,-10,-9,-6,10,-8],[9,9,6,-5,-10,-4],[-10,-4,2,-3,-8,-5],[5,-7,-7,-8,-2,8],[-6,4,9,-9,-9,-5],[-6,7,-3,-2,-6,-3],[-5,-3,9,-2,-4,9],[8,-2,10,6,-8,-10]]], dtype = "uint16")#candidate|1331|(7, 12, 6)|const|uint16
var_1332 = relay.var("var_1332", dtype = "uint16", shape = (7, 12, 6))#candidate|1332|(7, 12, 6)|var|uint16
bop_1333 = relay.greater_equal(const_1331.astype('bool'), relay.reshape(var_1332.astype('bool'), relay.shape_of(const_1331))) # shape=(7, 12, 6)
uop_1338 = relay.sigmoid(bop_1333.astype('float32')) # shape=(7, 12, 6)
func_406_call = mod.get_global_var('func_406')
func_409_call = mutated_mod.get_global_var('func_409')
var_1341 = relay.var("var_1341", dtype = "uint8", shape = (90,))#candidate|1341|(90,)|var|uint8
call_1340 = relay.TupleGetItem(func_406_call(relay.reshape(var_1341.astype('uint8'), [6, 1, 15])), 0)
call_1342 = relay.TupleGetItem(func_409_call(relay.reshape(var_1341.astype('uint8'), [6, 1, 15])), 0)
uop_1351 = relay.log(uop_1338.astype('float32')) # shape=(7, 12, 6)
output = relay.Tuple([call_1340,var_1341,uop_1351,])
output2 = relay.Tuple([call_1342,var_1341,uop_1351,])
func_1365 = relay.Function([var_1332,var_1341,], output)
mod['func_1365'] = func_1365
mod = relay.transform.InferType()(mod)
var_1366 = relay.var("var_1366", dtype = "uint16", shape = (7, 12, 6))#candidate|1366|(7, 12, 6)|var|uint16
var_1367 = relay.var("var_1367", dtype = "uint8", shape = (90,))#candidate|1367|(90,)|var|uint8
output = func_1365(var_1366,var_1367,)
func_1368 = relay.Function([var_1366,var_1367,], output)
mutated_mod['func_1368'] = func_1368
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1505 = relay.var("var_1505", dtype = "float64", shape = (3, 14, 9))#candidate|1505|(3, 14, 9)|var|float64
uop_1506 = relay.log2(var_1505.astype('float64')) # shape=(3, 14, 9)
uop_1512 = relay.rsqrt(uop_1506.astype('float32')) # shape=(3, 14, 9)
bop_1524 = relay.floor_divide(uop_1512.astype('float64'), relay.reshape(uop_1506.astype('float64'), relay.shape_of(uop_1512))) # shape=(3, 14, 9)
output = bop_1524
output2 = bop_1524
func_1527 = relay.Function([var_1505,], output)
mod['func_1527'] = func_1527
mod = relay.transform.InferType()(mod)
var_1528 = relay.var("var_1528", dtype = "float64", shape = (3, 14, 9))#candidate|1528|(3, 14, 9)|var|float64
output = func_1527(var_1528)
func_1529 = relay.Function([var_1528], output)
mutated_mod['func_1529'] = func_1529
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1646 = relay.const([[[-8,7,9,4,2,-1,-5],[8,-10,4,-5,3,6,-4],[-5,-1,5,-6,-1,-10,6],[-10,4,4,6,6,-10,-7],[7,1,4,4,-1,6,3],[-5,-9,-2,2,-7,-4,10],[-3,10,10,-9,5,-6,4],[-8,-1,-5,-7,3,5,-10],[2,10,-6,-5,-4,-1,-10],[5,2,-2,-6,3,-6,-5],[-6,-7,-4,6,-1,-6,-7],[-4,-7,-2,4,-10,-1,-6]],[[-9,5,7,-6,2,2,-4],[8,9,-8,-3,-3,-4,-9],[-8,-1,7,4,1,6,-3],[7,-9,9,-9,2,9,8],[2,10,4,9,-9,-7,5],[6,-2,-5,9,8,-3,9],[8,5,7,-10,-9,2,3],[8,3,-8,-6,7,-7,3],[-7,-9,-2,-5,-4,-9,5],[10,-9,8,4,-6,-8,-6],[-7,-4,1,-9,10,1,-2],[-6,2,-7,-6,-2,10,9]],[[-2,-3,-5,-5,-10,1,-10],[-5,-3,-9,7,-5,-2,3],[8,10,-8,8,9,2,-10],[1,-5,2,9,4,-9,9],[9,-3,-4,4,-5,-7,-10],[6,-2,-9,5,-7,-3,10],[-4,-3,-1,-10,7,-10,8],[1,-6,7,-3,-7,8,-3],[-6,4,4,-3,-2,-3,-6],[-5,10,-6,2,6,-2,6],[-6,-2,3,-2,-3,-1,9],[8,-7,-4,9,-3,3,-6]]], dtype = "int16")#candidate|1646|(3, 12, 7)|const|int16
var_1647 = relay.var("var_1647", dtype = "int16", shape = (3, 12, 7))#candidate|1647|(3, 12, 7)|var|int16
bop_1648 = relay.bitwise_and(const_1646.astype('int16'), relay.reshape(var_1647.astype('int16'), relay.shape_of(const_1646))) # shape=(3, 12, 7)
uop_1669 = relay.tan(var_1647.astype('float32')) # shape=(3, 12, 7)
func_568_call = mod.get_global_var('func_568')
func_571_call = mutated_mod.get_global_var('func_571')
const_1682 = relay.const([5.404479,7.744399,-0.748097,-2.672252,6.026105,0.077421,1.039578,-4.038424,-4.211864,0.632780,9.550422,-9.081403,0.263915,1.378580,-9.753241,8.921202,-4.598978,8.676623,2.133316,-8.213401,-6.638111,-2.667844,-4.799637,-7.669148,-5.333922,5.989599,8.710351,6.497055,-6.506778,4.535379,8.661679,3.503320,0.936427,1.710717,-6.702800,6.788686,6.873714,-4.263175,-6.204395,-1.228650,-4.079632,-8.233986,7.165292,-6.543329,-0.240009,6.040624,4.040103,-7.381677,7.980762,2.513121,3.176950,-8.685740,-8.082451,-4.622074,-2.518178,1.602659,-2.242625,-8.022383,-2.449981,-6.690817,-7.009694,-2.023507,-0.585606,-4.470333,-5.590673,2.326682,-5.266329,-9.251464,-2.792918,9.924675,-7.648829,7.171600,0.084214,-1.772646,-7.823763,-1.239227,-7.083744,-2.212561,9.333868,9.388602,8.604011,1.878907,-5.152114,-0.862963,-8.720602,7.144629,0.089006,-0.702802,-0.835906,-4.509661,7.585067,6.058175,8.036602,-6.859054,-9.024241,4.103808,-8.906234,4.557757,-6.683269,5.137223,-8.243758,8.415052,0.669898,-9.607099,6.148178,-7.865806,1.294321,-0.737592,-5.018605,-0.855654,-0.034791,-9.440352,-2.129648,-5.586171,2.256569,-6.459944,-0.539078,5.876059,3.573343,-5.992664,-2.306681,0.571307,-0.631670,0.249767,-0.694072,-3.656999,9.842658,5.296217,-5.154293,-4.590461,6.232492,8.660890,2.023687,3.962367,-5.481805,0.079951,-1.191770,1.900928,-8.034831,9.173735,-2.874916,-6.838957,-3.849529,3.948480,9.577882,3.571266,-4.774816,-0.688716,2.855796,-4.828009,7.251934,2.806621,-1.855299,0.470942,8.020417,2.095374,-1.158727,0.245229,7.530814,8.690604,-2.488134,6.208407,-6.367893,-5.642064,1.777791,1.898193,-6.955928,0.096247,8.959725,-0.104459,0.478022,-0.076582,0.608307,8.284606,0.968428,2.727667,4.382018,-9.096985,-6.202328,3.017073,-9.373265,3.332082,8.208400,3.352690,3.203901,5.853339,-0.855867,-4.537545,4.338645,-1.889324,-2.305330,9.097993,1.152879,7.389608,-0.072764,4.662020,-7.255587,-8.500258,7.327182,-0.146826,4.875239,-8.913186,-8.766221,1.185804,-3.883726,-2.358277,1.780916,-8.290719,6.122583,-1.633855,-4.122719,-1.377887,-7.756550,5.927677,5.421423,-3.012171,5.125431,-5.869421,7.849783,-1.522288,8.791231,0.866060,-0.670463,0.540218,2.352548,5.055139,-0.448673,-3.164700,-6.388747,-6.674612,-8.212899,-9.926491,9.108981,3.309897,-2.592209,-1.990925,-6.418308,-6.562317,3.825453,-9.391037,-3.514669,9.165046,-3.551979,1.734189,6.693379,-2.432376,5.394709,8.130412,0.767141,1.082519,-7.214528,1.608843,3.886429,7.002103,-7.013440,-1.968237,-0.554879,4.786244,0.480032,1.604783,-0.057825,-0.953425,2.652821,4.313228,-0.666454,-3.485539,-0.527737,6.412971,-8.271832,4.329242], dtype = "float64")#candidate|1682|(270,)|const|float64
call_1681 = func_568_call(relay.reshape(const_1682.astype('float64'), [15, 3, 6]), relay.reshape(const_1682.astype('float64'), [15, 3, 6]), )
call_1683 = func_568_call(relay.reshape(const_1682.astype('float64'), [15, 3, 6]), relay.reshape(const_1682.astype('float64'), [15, 3, 6]), )
output = relay.Tuple([bop_1648,uop_1669,call_1681,const_1682,])
output2 = relay.Tuple([bop_1648,uop_1669,call_1683,const_1682,])
func_1697 = relay.Function([var_1647,], output)
mod['func_1697'] = func_1697
mod = relay.transform.InferType()(mod)
mutated_mod['func_1697'] = func_1697
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1698 = relay.var("var_1698", dtype = "int16", shape = (3, 12, 7))#candidate|1698|(3, 12, 7)|var|int16
func_1697_call = mutated_mod.get_global_var('func_1697')
call_1699 = func_1697_call(var_1698)
output = call_1699
func_1700 = relay.Function([var_1698], output)
mutated_mod['func_1700'] = func_1700
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1730 = relay.var("var_1730", dtype = "int32", shape = (9, 7, 10))#candidate|1730|(9, 7, 10)|var|int32
const_1731 = relay.const([[[-6,-5,1,-1,10,2,8,1,2,-10],[-1,-3,-10,-8,-10,9,7,-5,8,1],[-6,9,-3,-1,-4,-7,8,7,5,-3],[8,-10,-7,-3,-1,-1,1,2,4,-8],[-4,3,-5,10,-4,6,6,-6,3,6],[-8,-4,10,-3,-9,1,6,-7,-4,2],[9,-1,5,10,9,-5,-6,5,5,10]],[[-9,-9,-7,-9,-3,-9,10,-1,-9,5],[6,4,9,8,9,1,-9,4,-7,4],[-3,-4,5,8,-6,-10,4,-6,7,-8],[2,-4,-10,-6,1,-8,-5,7,-10,1],[-9,8,-9,8,-8,10,-6,10,3,2],[6,-8,4,8,-2,10,2,-7,-2,-4],[-9,-10,-9,10,4,5,6,10,9,-4]],[[1,-4,-3,3,-6,-6,1,2,4,-1],[-6,10,-10,-1,-2,-1,10,3,8,9],[-3,1,-10,-6,-6,5,-3,-3,-7,1],[-3,10,8,9,1,10,-4,10,3,-8],[-4,1,10,-10,2,6,-6,1,4,-1],[-9,-9,-1,4,-6,3,7,-7,1,4],[9,-1,8,8,-3,7,10,-4,6,7]],[[2,1,-7,6,6,-1,2,9,-5,4],[-7,-9,-6,10,-3,-3,6,-4,-10,10],[4,10,-5,-8,7,-10,10,3,-4,-5],[9,-4,1,7,10,-9,1,2,10,10],[-9,-4,-2,4,-2,-5,-8,6,-6,-3],[2,-3,-1,1,-3,1,-1,-3,-3,-1],[10,4,2,9,4,-6,-4,-9,4,-8]],[[-1,2,-5,-5,4,3,-1,-1,-8,-2],[-2,9,9,-3,-10,-3,2,-2,-2,7],[-4,-9,-9,9,3,-2,-2,-5,10,6],[-10,10,-4,-1,3,2,8,4,4,-5],[-5,-3,9,-5,-5,9,-10,1,3,-10],[-2,6,4,9,1,6,-10,-10,7,8],[-8,1,-5,-4,6,7,-6,8,-2,9]],[[-1,-1,2,-2,1,-4,6,-9,-8,1],[8,-2,4,-6,8,-2,-8,2,6,-2],[-5,-8,-2,3,-1,-5,-4,-5,10,-5],[-5,-9,-1,5,-6,-6,3,-3,-2,-6],[1,-2,-2,-3,6,-1,8,6,-3,-9],[-9,-10,-1,-9,9,6,9,-5,4,-3],[8,3,-6,-7,1,-5,-3,3,10,-8]],[[9,9,1,1,3,-4,-10,7,6,-4],[-10,-7,6,8,2,-8,-10,-1,10,6],[7,-4,-9,-4,5,-1,-7,-9,-8,2],[4,3,7,-7,-7,10,-3,5,-5,6],[-7,6,-7,8,3,7,1,3,5,5],[-1,8,-1,-5,-1,8,-9,-1,-1,-2],[-10,4,-9,9,5,8,1,9,10,-10]],[[-6,-7,5,9,-9,-4,10,-2,3,4],[9,3,9,-4,7,-8,-2,-7,-4,-7],[-9,-6,7,7,3,-9,3,-2,5,9],[-8,6,-3,1,9,-2,8,-7,-8,-8],[-8,-1,8,-5,-9,-6,3,-9,5,4],[9,-4,6,4,8,4,9,-8,1,4],[8,-7,4,-5,-7,4,-7,-4,10,6]],[[2,-3,-7,9,-4,8,-3,-1,10,-5],[-7,4,7,-6,8,4,-1,-10,-10,6],[2,-6,-8,9,2,-6,2,2,10,6],[-7,-7,-1,-9,-7,-5,-9,-1,7,-5],[-5,10,3,-7,-8,-2,-7,-7,7,9],[1,3,6,-6,-6,-4,4,-10,-5,-1],[-2,-2,-1,5,-5,3,10,-7,-2,9]]], dtype = "int32")#candidate|1731|(9, 7, 10)|const|int32
bop_1732 = relay.bitwise_or(var_1730.astype('int32'), relay.reshape(const_1731.astype('int32'), relay.shape_of(var_1730))) # shape=(9, 7, 10)
output = relay.Tuple([bop_1732,])
output2 = relay.Tuple([bop_1732,])
func_1735 = relay.Function([var_1730,], output)
mod['func_1735'] = func_1735
mod = relay.transform.InferType()(mod)
mutated_mod['func_1735'] = func_1735
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1736 = relay.var("var_1736", dtype = "int32", shape = (9, 7, 10))#candidate|1736|(9, 7, 10)|var|int32
func_1735_call = mutated_mod.get_global_var('func_1735')
call_1737 = func_1735_call(var_1736)
output = call_1737
func_1738 = relay.Function([var_1736], output)
mutated_mod['func_1738'] = func_1738
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2014 = relay.var("var_2014", dtype = "float32", shape = (16, 10, 14))#candidate|2014|(16, 10, 14)|var|float32
var_2015 = relay.var("var_2015", dtype = "float32", shape = (16, 10, 14))#candidate|2015|(16, 10, 14)|var|float32
bop_2016 = relay.mod(var_2014.astype('float32'), relay.reshape(var_2015.astype('float32'), relay.shape_of(var_2014))) # shape=(16, 10, 14)
output = relay.Tuple([bop_2016,])
output2 = relay.Tuple([bop_2016,])
func_2021 = relay.Function([var_2014,var_2015,], output)
mod['func_2021'] = func_2021
mod = relay.transform.InferType()(mod)
var_2022 = relay.var("var_2022", dtype = "float32", shape = (16, 10, 14))#candidate|2022|(16, 10, 14)|var|float32
var_2023 = relay.var("var_2023", dtype = "float32", shape = (16, 10, 14))#candidate|2023|(16, 10, 14)|var|float32
output = func_2021(var_2022,var_2023,)
func_2024 = relay.Function([var_2022,var_2023,], output)
mutated_mod['func_2024'] = func_2024
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2115 = relay.var("var_2115", dtype = "uint8", shape = (4, 14, 6))#candidate|2115|(4, 14, 6)|var|uint8
var_2116 = relay.var("var_2116", dtype = "uint8", shape = (4, 14, 6))#candidate|2116|(4, 14, 6)|var|uint8
bop_2117 = relay.greater_equal(var_2115.astype('bool'), relay.reshape(var_2116.astype('bool'), relay.shape_of(var_2115))) # shape=(4, 14, 6)
uop_2122 = relay.log(var_2116.astype('float32')) # shape=(4, 14, 6)
func_568_call = mod.get_global_var('func_568')
func_571_call = mutated_mod.get_global_var('func_571')
var_2136 = relay.var("var_2136", dtype = "float64", shape = (30, 9))#candidate|2136|(30, 9)|var|float64
call_2135 = func_568_call(relay.reshape(var_2136.astype('float64'), [15, 3, 6]), relay.reshape(var_2136.astype('float64'), [15, 3, 6]), )
call_2137 = func_568_call(relay.reshape(var_2136.astype('float64'), [15, 3, 6]), relay.reshape(var_2136.astype('float64'), [15, 3, 6]), )
uop_2141 = relay.atan(uop_2122.astype('float32')) # shape=(4, 14, 6)
func_694_call = mod.get_global_var('func_694')
func_696_call = mutated_mod.get_global_var('func_696')
var_2144 = relay.var("var_2144", dtype = "float64", shape = ())#candidate|2144|()|var|float64
call_2143 = func_694_call(relay.reshape(var_2144.astype('float64'), []))
call_2145 = func_694_call(relay.reshape(var_2144.astype('float64'), []))
output = relay.Tuple([bop_2117,call_2135,var_2136,uop_2141,call_2143,var_2144,])
output2 = relay.Tuple([bop_2117,call_2137,var_2136,uop_2141,call_2145,var_2144,])
func_2147 = relay.Function([var_2115,var_2116,var_2136,var_2144,], output)
mod['func_2147'] = func_2147
mod = relay.transform.InferType()(mod)
var_2148 = relay.var("var_2148", dtype = "uint8", shape = (4, 14, 6))#candidate|2148|(4, 14, 6)|var|uint8
var_2149 = relay.var("var_2149", dtype = "uint8", shape = (4, 14, 6))#candidate|2149|(4, 14, 6)|var|uint8
var_2150 = relay.var("var_2150", dtype = "float64", shape = (30, 9))#candidate|2150|(30, 9)|var|float64
var_2151 = relay.var("var_2151", dtype = "float64", shape = ())#candidate|2151|()|var|float64
output = func_2147(var_2148,var_2149,var_2150,var_2151,)
func_2152 = relay.Function([var_2148,var_2149,var_2150,var_2151,], output)
mutated_mod['func_2152'] = func_2152
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2348 = relay.var("var_2348", dtype = "float64", shape = (1, 13, 7))#candidate|2348|(1, 13, 7)|var|float64
uop_2349 = relay.acosh(var_2348.astype('float64')) # shape=(1, 13, 7)
uop_2352 = relay.cos(uop_2349.astype('float32')) # shape=(1, 13, 7)
func_2147_call = mod.get_global_var('func_2147')
func_2152_call = mutated_mod.get_global_var('func_2152')
const_2357 = relay.const([[6,-2,7,-2,-5,-2,8,10,1,-5,8,8,2,-3,-7,7,-2,6,-6,-10,9,8,9,5,3,-4,5,-5,7,-2,-4,-2,7,6,8,6,9,5,9,10,3,7,8,-4,9,-1,-4,9,-3,-7,-10,-8,-7,9,-4,-2,-4,6,-8,-7,6,-1,-3,4,-5,6,-3,6,-7,10,5,2,-10,9,9,-6,-4,-5,-7,-2,9,-10,2,6,3,3,-9,-5,-3,6,10,5,9,2,1,10,4,6,-6,-5,10,6,5,8,-6,8,-6,-2,4,-3,-8,9,-3,-7,-1,9,-2,-3,-6,3,-5,8,3,-10,-3,-6,-6,-4,3,-9,4,8,-10,-3,9,-8,6,-10,5,-9,-1,-9,1,-7,5,-9,-1,-4,-7,9,4,2,3,-8,10,-7,4,9,1,10,-1,4,-5,4,7,7,1,1],[3,-4,-9,-5,7,6,1,4,6,-3,10,2,1,9,3,5,1,9,10,-3,-10,-7,-7,-3,10,-4,3,8,-7,5,-8,6,-10,1,8,9,5,1,6,6,1,-6,6,-8,10,-3,-4,8,-3,-7,3,1,1,-1,-7,5,-5,-2,-3,-5,4,1,-6,-3,10,-10,-6,-2,-6,-6,-7,10,-1,4,3,-9,7,4,-1,-2,8,3,-4,3,-7,2,-1,8,7,6,-1,-8,4,-2,10,5,6,4,-4,-2,7,7,-10,-7,-6,8,7,8,7,-6,3,-7,-3,3,-7,2,-10,-9,3,7,1,7,-3,-9,4,-9,1,8,-4,-3,5,-6,-4,5,-3,5,2,-1,-8,5,-8,-10,10,-2,8,-7,1,-10,-8,-2,-7,-4,10,4,-6,1,3,2,9,8,-9,10,8,-7,-5,7,6,3]], dtype = "uint8")#candidate|2357|(2, 168)|const|uint8
var_2358 = relay.var("var_2358", dtype = "float64", shape = (270, 1))#candidate|2358|(270, 1)|var|float64
const_2359 = relay.const(-4.702009, dtype = "float64")#candidate|2359|()|const|float64
call_2356 = relay.TupleGetItem(func_2147_call(relay.reshape(const_2357.astype('uint8'), [4, 14, 6]), relay.reshape(const_2357.astype('uint8'), [4, 14, 6]), relay.reshape(var_2358.astype('float64'), [30, 9]), relay.reshape(const_2359.astype('float64'), []), ), 4)
call_2360 = relay.TupleGetItem(func_2152_call(relay.reshape(const_2357.astype('uint8'), [4, 14, 6]), relay.reshape(const_2357.astype('uint8'), [4, 14, 6]), relay.reshape(var_2358.astype('float64'), [30, 9]), relay.reshape(const_2359.astype('float64'), []), ), 4)
output = relay.Tuple([uop_2352,call_2356,const_2357,var_2358,const_2359,])
output2 = relay.Tuple([uop_2352,call_2360,const_2357,var_2358,const_2359,])
func_2361 = relay.Function([var_2348,var_2358,], output)
mod['func_2361'] = func_2361
mod = relay.transform.InferType()(mod)
var_2362 = relay.var("var_2362", dtype = "float64", shape = (1, 13, 7))#candidate|2362|(1, 13, 7)|var|float64
var_2363 = relay.var("var_2363", dtype = "float64", shape = (270, 1))#candidate|2363|(270, 1)|var|float64
output = func_2361(var_2362,var_2363,)
func_2364 = relay.Function([var_2362,var_2363,], output)
mutated_mod['func_2364'] = func_2364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2408 = relay.var("var_2408", dtype = "float32", shape = (6, 8, 9))#candidate|2408|(6, 8, 9)|var|float32
var_2409 = relay.var("var_2409", dtype = "float32", shape = (6, 8, 9))#candidate|2409|(6, 8, 9)|var|float32
bop_2410 = relay.less(var_2408.astype('bool'), relay.reshape(var_2409.astype('bool'), relay.shape_of(var_2408))) # shape=(6, 8, 9)
uop_2418 = relay.log(bop_2410.astype('float32')) # shape=(6, 8, 9)
func_1527_call = mod.get_global_var('func_1527')
func_1529_call = mutated_mod.get_global_var('func_1529')
var_2424 = relay.var("var_2424", dtype = "float64", shape = (378,))#candidate|2424|(378,)|var|float64
call_2423 = func_1527_call(relay.reshape(var_2424.astype('float64'), [3, 14, 9]))
call_2425 = func_1527_call(relay.reshape(var_2424.astype('float64'), [3, 14, 9]))
output = relay.Tuple([uop_2418,call_2423,var_2424,])
output2 = relay.Tuple([uop_2418,call_2425,var_2424,])
func_2427 = relay.Function([var_2408,var_2409,var_2424,], output)
mod['func_2427'] = func_2427
mod = relay.transform.InferType()(mod)
var_2428 = relay.var("var_2428", dtype = "float32", shape = (6, 8, 9))#candidate|2428|(6, 8, 9)|var|float32
var_2429 = relay.var("var_2429", dtype = "float32", shape = (6, 8, 9))#candidate|2429|(6, 8, 9)|var|float32
var_2430 = relay.var("var_2430", dtype = "float64", shape = (378,))#candidate|2430|(378,)|var|float64
output = func_2427(var_2428,var_2429,var_2430,)
func_2431 = relay.Function([var_2428,var_2429,var_2430,], output)
mutated_mod['func_2431'] = func_2431
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2728 = relay.var("var_2728", dtype = "int32", shape = (16, 2, 16))#candidate|2728|(16, 2, 16)|var|int32
var_2729 = relay.var("var_2729", dtype = "int32", shape = (16, 2, 16))#candidate|2729|(16, 2, 16)|var|int32
bop_2730 = relay.not_equal(var_2728.astype('bool'), relay.reshape(var_2729.astype('bool'), relay.shape_of(var_2728))) # shape=(16, 2, 16)
bop_2733 = relay.floor_mod(var_2729.astype('float32'), relay.reshape(var_2728.astype('float32'), relay.shape_of(var_2729))) # shape=(16, 2, 16)
output = relay.Tuple([bop_2730,bop_2733,])
output2 = relay.Tuple([bop_2730,bop_2733,])
func_2742 = relay.Function([var_2728,var_2729,], output)
mod['func_2742'] = func_2742
mod = relay.transform.InferType()(mod)
var_2743 = relay.var("var_2743", dtype = "int32", shape = (16, 2, 16))#candidate|2743|(16, 2, 16)|var|int32
var_2744 = relay.var("var_2744", dtype = "int32", shape = (16, 2, 16))#candidate|2744|(16, 2, 16)|var|int32
output = func_2742(var_2743,var_2744,)
func_2745 = relay.Function([var_2743,var_2744,], output)
mutated_mod['func_2745'] = func_2745
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2861 = relay.var("var_2861", dtype = "float64", shape = (5, 8, 15))#candidate|2861|(5, 8, 15)|var|float64
uop_2862 = relay.sigmoid(var_2861.astype('float64')) # shape=(5, 8, 15)
output = relay.Tuple([uop_2862,])
output2 = relay.Tuple([uop_2862,])
func_2879 = relay.Function([var_2861,], output)
mod['func_2879'] = func_2879
mod = relay.transform.InferType()(mod)
mutated_mod['func_2879'] = func_2879
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2880 = relay.var("var_2880", dtype = "float64", shape = (5, 8, 15))#candidate|2880|(5, 8, 15)|var|float64
func_2879_call = mutated_mod.get_global_var('func_2879')
call_2881 = func_2879_call(var_2880)
output = call_2881
func_2882 = relay.Function([var_2880], output)
mutated_mod['func_2882'] = func_2882
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2969 = relay.var("var_2969", dtype = "float64", shape = (1, 8, 13))#candidate|2969|(1, 8, 13)|var|float64
var_2970 = relay.var("var_2970", dtype = "float64", shape = (16, 8, 13))#candidate|2970|(16, 8, 13)|var|float64
bop_2971 = relay.power(var_2969.astype('float64'), var_2970.astype('float64')) # shape=(16, 8, 13)
output = bop_2971
output2 = bop_2971
func_2976 = relay.Function([var_2969,var_2970,], output)
mod['func_2976'] = func_2976
mod = relay.transform.InferType()(mod)
var_2977 = relay.var("var_2977", dtype = "float64", shape = (1, 8, 13))#candidate|2977|(1, 8, 13)|var|float64
var_2978 = relay.var("var_2978", dtype = "float64", shape = (16, 8, 13))#candidate|2978|(16, 8, 13)|var|float64
output = func_2976(var_2977,var_2978,)
func_2979 = relay.Function([var_2977,var_2978,], output)
mutated_mod['func_2979'] = func_2979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3042 = relay.var("var_3042", dtype = "float32", shape = (12, 10, 8))#candidate|3042|(12, 10, 8)|var|float32
uop_3043 = relay.sinh(var_3042.astype('float32')) # shape=(12, 10, 8)
func_2427_call = mod.get_global_var('func_2427')
func_2431_call = mutated_mod.get_global_var('func_2431')
var_3054 = relay.var("var_3054", dtype = "float32", shape = (108, 4))#candidate|3054|(108, 4)|var|float32
var_3055 = relay.var("var_3055", dtype = "float64", shape = (378,))#candidate|3055|(378,)|var|float64
call_3053 = relay.TupleGetItem(func_2427_call(relay.reshape(var_3054.astype('float32'), [6, 8, 9]), relay.reshape(var_3054.astype('float32'), [6, 8, 9]), relay.reshape(var_3055.astype('float64'), [378,]), ), 0)
call_3056 = relay.TupleGetItem(func_2431_call(relay.reshape(var_3054.astype('float32'), [6, 8, 9]), relay.reshape(var_3054.astype('float32'), [6, 8, 9]), relay.reshape(var_3055.astype('float64'), [378,]), ), 0)
output = relay.Tuple([uop_3043,call_3053,var_3054,var_3055,])
output2 = relay.Tuple([uop_3043,call_3056,var_3054,var_3055,])
func_3057 = relay.Function([var_3042,var_3054,var_3055,], output)
mod['func_3057'] = func_3057
mod = relay.transform.InferType()(mod)
mutated_mod['func_3057'] = func_3057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3057_call = mutated_mod.get_global_var('func_3057')
var_3059 = relay.var("var_3059", dtype = "float32", shape = (12, 10, 8))#candidate|3059|(12, 10, 8)|var|float32
var_3060 = relay.var("var_3060", dtype = "float32", shape = (108, 4))#candidate|3060|(108, 4)|var|float32
var_3061 = relay.var("var_3061", dtype = "float64", shape = (378,))#candidate|3061|(378,)|var|float64
call_3058 = func_3057_call(var_3059,var_3060,var_3061,)
output = call_3058
func_3062 = relay.Function([var_3059,var_3060,var_3061,], output)
mutated_mod['func_3062'] = func_3062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3089 = relay.var("var_3089", dtype = "int64", shape = (10, 11, 10))#candidate|3089|(10, 11, 10)|var|int64
const_3090 = relay.const([[[1,-1,-7,9,2,-8,4,8,-1,9],[-2,2,-7,2,-9,9,4,-7,10,6],[-3,-6,-4,-8,3,-10,-6,-1,-3,7],[5,1,8,10,-5,2,1,-4,-4,2],[2,4,-4,-3,8,-10,5,-10,-1,-3],[-9,2,-6,-4,1,-10,10,10,-1,-5],[-10,1,4,10,-4,-2,9,2,2,-6],[4,5,3,1,8,-4,9,-6,9,-10],[9,7,-10,5,-6,7,10,7,-7,9],[4,-4,1,8,7,4,-2,6,-1,-5],[4,7,2,-7,-2,-4,2,-9,-9,-2]],[[7,-2,8,-2,-9,-3,7,-4,6,9],[10,2,3,-6,10,-9,-5,-5,-7,9],[4,-8,6,3,7,-7,5,-8,3,-1],[3,10,-10,-8,-2,4,1,-8,-6,-8],[-2,10,6,-8,-4,-4,10,3,-8,7],[-10,-7,-3,-9,-3,3,-9,3,-3,-6],[1,-3,3,10,-9,-1,-8,-1,3,-3],[4,-2,-9,10,-7,10,-8,10,1,3],[7,-10,-2,7,10,4,5,10,-2,-7],[-9,-10,10,-8,-7,10,3,-8,-2,2],[6,9,-1,-5,-1,3,-9,-7,-2,7]],[[-4,-3,8,5,8,-3,3,-6,-1,7],[-3,-4,-5,1,-5,-7,7,9,-5,7],[-2,-8,4,-7,-6,9,-7,2,-3,9],[3,-9,10,-8,-2,8,7,7,1,6],[-8,-7,-7,9,3,-10,-6,7,-6,-10],[-9,-10,-4,8,3,-3,1,8,-8,-10],[6,7,8,9,6,2,-8,2,1,9],[5,5,-1,-6,1,-2,-5,-3,1,-4],[-1,-2,9,5,3,-6,-8,-4,5,10],[3,6,-10,-8,-1,8,1,3,6,-1],[-3,-7,7,10,9,-1,3,-2,-6,-4]],[[5,9,3,-7,1,8,-7,5,-4,8],[-6,-8,8,-3,-10,-1,10,2,-3,4],[7,10,-5,-7,-9,-4,8,7,10,10],[7,-7,-5,-2,-6,-4,8,-8,-8,-6],[2,3,2,5,10,-3,1,5,7,-6],[-6,9,-6,-9,-1,-3,-2,4,6,7],[-7,4,10,-3,7,-1,2,6,-6,2],[9,2,-2,7,-6,-6,3,-10,-9,10],[-6,10,-3,-6,1,-8,-5,-4,-9,-7],[-5,7,-2,3,-3,9,5,7,-6,-1],[-3,9,-1,5,4,-4,-2,9,1,-7]],[[-6,-4,-6,1,6,-8,10,6,-10,1],[10,5,10,10,-7,-6,3,-5,2,8],[-9,6,-4,3,3,10,-1,7,-10,-3],[-4,-1,10,6,2,-10,2,2,-10,10],[9,9,6,3,3,-4,-4,5,-10,6],[5,-5,-5,3,-2,-1,4,4,7,5],[-3,8,5,-1,-4,-7,6,6,-8,9],[1,-2,-1,4,-4,-8,9,4,9,8],[-6,-2,8,-4,-6,-8,-4,-1,-7,-2],[5,9,6,-9,1,-6,-4,-9,-6,-9],[-9,-9,-7,7,7,-8,9,-8,1,8]],[[7,-10,4,-3,4,7,1,6,8,4],[3,8,9,7,-5,3,10,-3,3,-9],[10,-10,-1,10,2,-5,-8,-8,-10,9],[1,7,5,8,-8,9,-4,-10,5,-4],[-4,3,5,10,-6,1,1,9,-10,8],[-7,-7,-5,-5,6,9,-10,3,2,1],[2,-7,3,-1,-4,-2,-5,1,-5,10],[8,3,-10,5,2,3,-1,-9,6,-7],[10,-3,-8,2,-3,-5,2,2,8,5],[5,-8,-6,-1,8,5,7,10,2,-9],[6,7,5,9,7,5,-2,10,-9,-2]],[[-9,4,5,-1,8,2,-5,-2,-8,-4],[-5,-7,-10,-6,-8,-8,7,4,6,9],[-9,-7,-9,3,-10,-4,-5,-1,-8,6],[5,-6,3,-4,-9,-4,3,-1,2,2],[2,-4,-7,-2,2,-4,1,1,9,-7],[-8,5,2,-4,1,-6,-1,9,-7,-4],[10,-8,-7,-7,6,-5,4,-6,7,1],[-7,10,-7,-8,10,3,-2,-3,2,5],[5,-2,9,5,7,3,-3,4,4,6],[5,-3,4,6,-5,6,3,9,6,-10],[-10,-9,-8,6,-2,-3,2,6,2,-2]],[[4,-9,5,-9,-9,-6,-1,-3,5,-10],[-2,5,-1,-1,-4,-1,10,5,7,-8],[4,5,-6,-4,-10,7,-7,5,5,2],[9,-10,-5,-6,-1,-9,6,-8,-4,3],[-9,5,7,6,8,-1,-3,-5,6,-1],[6,1,3,6,4,-1,-10,-10,8,8],[4,-2,2,7,1,-6,5,-10,-7,-6],[-4,5,-5,2,1,-9,3,3,-1,7],[6,8,1,2,2,10,-6,1,-9,7],[5,4,9,5,-6,9,-6,-5,-3,-4],[4,-1,8,-4,-5,7,-6,7,-6,3]],[[-7,-8,-9,1,-2,7,10,8,7,4],[-10,-1,-2,2,-3,2,9,-4,-4,2],[-9,-2,6,6,2,7,-3,-10,9,2],[9,3,-5,10,-9,5,-1,6,9,-1],[3,4,-8,-8,-8,-8,-4,7,-7,9],[9,-5,-1,8,-2,2,6,-1,10,-1],[2,5,10,5,1,5,-8,-10,9,8],[6,-9,5,9,3,-4,-9,1,5,9],[2,7,2,8,7,5,7,8,-5,-7],[-4,3,2,-5,10,4,-5,1,-10,9],[6,-9,-9,4,3,-4,4,2,-1,-4]],[[8,4,-9,-1,5,-4,-5,1,1,9],[7,-1,-1,7,-10,5,-9,1,4,-6],[-3,10,-5,-3,-6,-2,-6,-2,-8,8],[-9,3,-2,5,8,6,2,-9,-7,-5],[5,-4,2,7,-8,-7,-10,5,7,-9],[-9,-6,9,10,-10,-8,4,-7,9,-8],[10,4,-6,-1,6,7,5,8,1,-9],[-5,-7,9,7,9,-7,-1,-1,9,-7],[4,-10,-7,2,-6,-8,-9,2,-10,-8],[-6,-8,-5,1,2,8,-2,-4,7,-7],[-10,6,2,7,-8,-1,-9,1,-9,-7]]], dtype = "int64")#candidate|3090|(10, 11, 10)|const|int64
bop_3091 = relay.maximum(var_3089.astype('int64'), relay.reshape(const_3090.astype('int64'), relay.shape_of(var_3089))) # shape=(10, 11, 10)
output = bop_3091
output2 = bop_3091
func_3094 = relay.Function([var_3089,], output)
mod['func_3094'] = func_3094
mod = relay.transform.InferType()(mod)
mutated_mod['func_3094'] = func_3094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3095 = relay.var("var_3095", dtype = "int64", shape = (10, 11, 10))#candidate|3095|(10, 11, 10)|var|int64
func_3094_call = mutated_mod.get_global_var('func_3094')
call_3096 = func_3094_call(var_3095)
output = call_3096
func_3097 = relay.Function([var_3095], output)
mutated_mod['func_3097'] = func_3097
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3110 = relay.const([[[0.372496,-3.837644,-1.332382],[-6.057836,-0.664397,-8.597112],[-9.353637,3.548074,9.440342],[-2.258326,-8.098154,-3.818738],[-6.929443,3.398794,3.606445],[4.912326,3.603652,3.582161],[-2.930378,-8.443837,-1.541664],[4.858542,-6.816251,5.695340],[-6.373461,4.204376,-6.684393],[-2.092101,-5.720856,9.511051],[-5.854729,1.641680,-4.590904],[9.721509,-2.551962,-1.322936]],[[6.709472,-9.368818,-7.913796],[1.306018,1.874954,1.307131],[-5.967923,-6.992888,-7.882280],[-2.900605,7.841591,-8.923004],[-2.716717,-5.098314,9.157623],[5.272070,3.647657,-5.330362],[6.833805,-5.649387,-7.718520],[7.753798,9.734867,-2.117954],[6.748227,-9.622570,-0.522405],[-9.754957,-3.256887,9.724305],[6.441418,-8.407717,-2.741263],[-0.890585,-2.444081,4.689539]],[[0.394577,3.485381,-6.110466],[-5.991613,-5.732612,-2.709683],[2.722252,7.601255,-1.765142],[2.055493,4.414414,-5.180669],[8.979768,-6.768039,5.579026],[-3.435992,-8.167577,8.574812],[4.595329,-9.665988,-5.758077],[-8.581670,2.764206,3.164021],[7.608224,-4.768709,0.883124],[-2.925247,7.779528,-3.496395],[-3.659640,1.016888,2.324870],[-7.888364,-2.436600,-4.834260]]], dtype = "float32")#candidate|3110|(3, 12, 3)|const|float32
uop_3111 = relay.sin(const_3110.astype('float32')) # shape=(3, 12, 3)
uop_3117 = relay.asinh(const_3110.astype('float64')) # shape=(3, 12, 3)
output = relay.Tuple([uop_3111,uop_3117,])
output2 = relay.Tuple([uop_3111,uop_3117,])
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
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3143 = relay.TupleGetItem(func_3129_call(), 0)
call_3144 = relay.TupleGetItem(func_3131_call(), 0)
output = relay.Tuple([call_3143,])
output2 = relay.Tuple([call_3144,])
func_3147 = relay.Function([], output)
mod['func_3147'] = func_3147
mod = relay.transform.InferType()(mod)
mutated_mod['func_3147'] = func_3147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mutated_mod.get_global_var('func_3147')
call_3148 = func_3147_call()
output = call_3148
func_3149 = relay.Function([], output)
mutated_mod['func_3149'] = func_3149
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3179 = relay.var("var_3179", dtype = "float64", shape = (16, 7, 16))#candidate|3179|(16, 7, 16)|var|float64
uop_3180 = relay.acos(var_3179.astype('float64')) # shape=(16, 7, 16)
func_1697_call = mod.get_global_var('func_1697')
func_1700_call = mutated_mod.get_global_var('func_1700')
var_3183 = relay.var("var_3183", dtype = "int16", shape = (252,))#candidate|3183|(252,)|var|int16
call_3182 = relay.TupleGetItem(func_1697_call(relay.reshape(var_3183.astype('int16'), [3, 12, 7])), 2)
call_3184 = relay.TupleGetItem(func_1700_call(relay.reshape(var_3183.astype('int16'), [3, 12, 7])), 2)
var_3185 = relay.var("var_3185", dtype = "float64", shape = (16, 7, 16))#candidate|3185|(16, 7, 16)|var|float64
bop_3186 = relay.left_shift(uop_3180.astype('uint16'), relay.reshape(var_3185.astype('uint16'), relay.shape_of(uop_3180))) # shape=(16, 7, 16)
uop_3191 = relay.atanh(uop_3180.astype('float32')) # shape=(16, 7, 16)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_3200 = relay.TupleGetItem(func_3147_call(), 0)
call_3201 = relay.TupleGetItem(func_3149_call(), 0)
func_1365_call = mod.get_global_var('func_1365')
func_1368_call = mutated_mod.get_global_var('func_1368')
const_3206 = relay.const([9,6,-7,4,-5,4,7,-8,-10,1,-1,9,5,-9,4,-10,9,6,8,7,6,9,-7,-2,-9,4,-7,2,-1,-7,-5,9,-5,-10,-4,-6,-8,-6,1,1,2,2,10,-3,4,-5,9,1,-8,-6,-9,3,-9,-2,10,2,1,-1,-7,2,-4,-10,-3,-6,-3,-3,7,10,6,6,-7,8,-4,9,-5,5,-1,4,-6,-5,3,3,-4,5,5,6,2,10,-2,9,1,9,-7,-6,-3,3,-8,5,-9,2,2,6,9,-9,-6,-10,-10,-10,10,-3,-8,-9,5,8,6,10,7,1,-3,-9,-1,-7,-6,10,-7,-10,-1,1,5,-2,1,-9,9,4,-2,-2,-10,4,7,5,-10,9,2,-7,-3,-7,10,-1,-6,2,6,1,-2,5,2,5,2,3,-8,-2,9,3,5,-8,-9,-1,4,-4,-8,10,-8,1,-1,-6,3,1,-9,-3,10,-7,4,7,-7,-6,1,-4,1,1,-8,-4,-6,6,9,2,-1,-10,5,4,-8,9,-6,-8,-10,2,7,10,-9,1,-6,-9,1,3,-5,-2,-7,2,-5,2,-1,-3,10,-4,-2,9,9,4,-7,8,5,-5,-10,-8,1,-10,4,-3,-7,-3,1,6,2,-9,-8,-1,4,5,-6,9,-3,-10,-10,-1,-9,7,-8,9,4,9,3,-5,5,-1,3,8,8,-10,10,-7,-8,8,-1,6,-5,7,6,-6,-2,-3,8,-8,9,5,1,-10,-10,5,-7,7,9,-9,6,5,6,-2,9,-1,9,-10,1,1,8,5,8,-7,-5,-1,4,8,4,-6,-9,-1,-6,3,9,-1,2,2,9,9,6,7,-6,1,5,10,6,-6,-2,-2,-3,-8,8,-6,-1,-2,-3,-8,4,-8,7,-6,-1,7,-1,4,1,-10,-4,-5,1,2,6,4,9,10,-10,-1,9,4,-7,6,10,7,4,9,-1,1,10,9,7,-5,6,-10,6,-4,10,-10,-8,4,-1,7,-1,9,-4,-1,8,8,4,8,1,2,4,2,1,3,-7,3,-9,-1,3,-3,-8,6,10,1,-7,-1,-6,-4,6,-8,10,-3,6,-1,6,9,-7,-3,10,-6,-8,10,1,1,-1,-2,-10,9,9,-4,-6,-6,-1,-9,6,8,4,7,9,-3,-7,-1,-10,-5,-10,3,-6,-8,1,-8,3,-8,-1,2,-5,10,10,10,-2,8,-8,6,1,10,1,6,3,1,-10,-4,8,6,-7,-9,-5,-1,-9,6,-2,1,-6,7,2,3,-3,-9,-3,2,-3,-1,7,1,8,5,8,3,-2,5,-2,-9,5,7], dtype = "uint16")#candidate|3206|(504,)|const|uint16
const_3207 = relay.const([10,-9,8,2,1,9,-1,-1,-2,7,-10,6,-4,-9,1,-10,-2,3,-5,9,8,-2,-8,-3,10,8,9,-1,-4,-5,-2,7,4,-4,-6,6,5,-3,3,-5,-8,-2,6,-1,4,7,-1,-10,4,-5,-10,-4,-9,10,-3,-4,8,9,1,-6,5,1,-10,2,-8,6,-8,-5,-7,10,9,-10,-1,-1,-8,9,4,3,4,10,4,10,-6,10,1,1,3,-7,10,-1], dtype = "uint8")#candidate|3207|(90,)|const|uint8
call_3205 = relay.TupleGetItem(func_1365_call(relay.reshape(const_3206.astype('uint16'), [7, 12, 6]), relay.reshape(const_3207.astype('uint8'), [90,]), ), 1)
call_3208 = relay.TupleGetItem(func_1368_call(relay.reshape(const_3206.astype('uint16'), [7, 12, 6]), relay.reshape(const_3207.astype('uint8'), [90,]), ), 1)
output = relay.Tuple([call_3182,var_3183,bop_3186,uop_3191,call_3200,call_3205,const_3206,const_3207,])
output2 = relay.Tuple([call_3184,var_3183,bop_3186,uop_3191,call_3201,call_3208,const_3206,const_3207,])
func_3223 = relay.Function([var_3179,var_3183,var_3185,], output)
mod['func_3223'] = func_3223
mod = relay.transform.InferType()(mod)
var_3224 = relay.var("var_3224", dtype = "float64", shape = (16, 7, 16))#candidate|3224|(16, 7, 16)|var|float64
var_3225 = relay.var("var_3225", dtype = "int16", shape = (252,))#candidate|3225|(252,)|var|int16
var_3226 = relay.var("var_3226", dtype = "float64", shape = (16, 7, 16))#candidate|3226|(16, 7, 16)|var|float64
output = func_3223(var_3224,var_3225,var_3226,)
func_3227 = relay.Function([var_3224,var_3225,var_3226,], output)
mutated_mod['func_3227'] = func_3227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_3313 = relay.TupleGetItem(func_3147_call(), 0)
call_3314 = relay.TupleGetItem(func_3149_call(), 0)
func_406_call = mod.get_global_var('func_406')
func_409_call = mutated_mod.get_global_var('func_409')
var_3317 = relay.var("var_3317", dtype = "uint8", shape = (90,))#candidate|3317|(90,)|var|uint8
call_3316 = relay.TupleGetItem(func_406_call(relay.reshape(var_3317.astype('uint8'), [6, 1, 15])), 1)
call_3318 = relay.TupleGetItem(func_409_call(relay.reshape(var_3317.astype('uint8'), [6, 1, 15])), 1)
output = relay.Tuple([call_3313,call_3316,var_3317,])
output2 = relay.Tuple([call_3314,call_3318,var_3317,])
func_3323 = relay.Function([var_3317,], output)
mod['func_3323'] = func_3323
mod = relay.transform.InferType()(mod)
var_3324 = relay.var("var_3324", dtype = "uint8", shape = (90,))#candidate|3324|(90,)|var|uint8
output = func_3323(var_3324)
func_3325 = relay.Function([var_3324], output)
mutated_mod['func_3325'] = func_3325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3399 = relay.TupleGetItem(func_3129_call(), 0)
call_3400 = relay.TupleGetItem(func_3131_call(), 0)
output = call_3399
output2 = call_3400
func_3408 = relay.Function([], output)
mod['func_3408'] = func_3408
mod = relay.transform.InferType()(mod)
output = func_3408()
func_3409 = relay.Function([], output)
mutated_mod['func_3409'] = func_3409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3432 = relay.TupleGetItem(func_3129_call(), 0)
call_3433 = relay.TupleGetItem(func_3131_call(), 0)
func_3057_call = mod.get_global_var('func_3057')
func_3062_call = mutated_mod.get_global_var('func_3062')
const_3437 = relay.const([[6.170654,-1.596956,-2.004807,-3.854644,9.571110,-6.825756,7.506196,2.509819],[5.487882,2.523135,0.324264,-2.245986,-9.857036,-9.973201,-2.249374,6.209915],[-5.364372,-0.104983,6.530044,-0.613349,-1.556948,0.889455,-4.932298,7.908532],[6.227762,-7.193721,-0.900489,-0.547335,-9.660037,-7.188260,-0.702649,2.434108],[2.553448,6.181312,-8.674471,6.926228,3.230684,7.213905,0.381846,9.285274],[6.293514,8.208905,3.731858,-3.701265,1.900462,-6.207969,-5.684724,-6.609087],[-0.594318,-3.889427,3.953463,0.207281,-3.400495,-0.846007,4.097382,7.121301],[-3.346714,2.055844,-8.798679,4.622438,-1.850575,-0.404315,5.974266,-9.991701],[-0.799989,7.384309,-6.083321,-9.266714,9.097066,3.283271,9.468551,7.581631],[6.741378,6.852507,-0.808482,9.502994,-6.564133,2.946547,-4.464048,0.387626],[7.820572,4.787972,-5.726883,-1.184100,-6.027043,-0.648143,-1.027787,8.627263],[-6.772609,-7.308599,-3.331527,5.812003,3.237171,-3.401066,-0.105153,-7.933742],[-5.884044,-2.946035,-3.663925,-5.654893,-2.213459,-6.987861,-9.898451,-7.261305],[-5.462757,5.076260,3.338103,3.918663,-5.299357,-8.820759,-7.929542,-2.044872],[-5.770186,6.042149,6.236207,-3.743018,-6.836258,6.811430,-7.803398,-9.519213],[-1.419121,4.070853,-4.384271,-6.072106,3.781005,-6.377910,1.235619,-3.508329],[6.301062,-9.874459,-5.732512,-4.506285,8.077174,4.153605,3.902748,-5.292787],[-9.492180,6.273398,0.563544,7.048849,0.937247,-0.796420,-7.205988,-0.668243],[-0.365300,-7.059191,2.487300,9.351249,-2.433029,2.271321,-0.531987,2.815271],[6.550552,-4.047459,-1.635268,4.438618,1.176720,2.402308,5.341767,5.026105],[-4.106899,-9.494806,-5.803857,0.473389,-5.338129,-4.647628,-9.539011,9.215476],[8.887061,-7.149529,4.387385,9.888258,1.350749,-8.381518,-1.100123,-6.699558],[-2.426371,6.951824,4.023245,1.347347,1.525383,-2.376024,-6.720923,7.166531],[9.076758,9.807463,-0.840998,5.606700,1.410464,-7.972313,6.892068,6.240953],[7.618726,-5.304745,9.167726,-3.826390,-3.546706,-7.640134,8.676416,-2.980269],[-3.257424,1.117947,-2.773955,-4.684348,7.636344,8.676987,-0.094340,-0.283105],[6.513880,-3.442188,-0.081782,5.819937,5.887852,4.516129,-8.733135,-6.172894],[-8.149701,4.364351,-1.518910,-4.813238,-4.613808,6.314171,-5.427618,-0.282958],[-6.534178,-5.373994,9.259882,7.747621,-5.349653,6.155249,-8.852653,6.793730],[-1.970961,6.512109,-0.514011,-6.700071,-9.457672,7.111735,5.304043,-1.294066],[-4.845176,-1.036912,0.359568,9.117145,4.493403,-2.281439,-5.113047,-7.286696],[-0.145930,8.596492,5.684531,3.017705,5.166537,5.274298,-2.184104,5.550581],[-8.084777,-5.791069,1.611588,0.671812,8.948353,7.001394,6.956954,-5.859751],[9.218685,6.322048,4.144465,-9.773351,8.458770,0.588349,-3.306089,7.519244],[-2.585688,-8.917664,8.721958,-5.115260,7.881972,-3.644835,5.740135,-8.932184],[-3.960908,-1.339213,-2.393110,1.194202,-0.172428,3.967212,8.519134,4.480651],[-0.752529,8.508724,-4.014392,-7.981947,0.241346,-1.472723,5.700592,-6.620906],[-6.337372,6.764722,4.766233,9.975762,4.005596,-4.323042,1.082760,6.620180],[4.499154,4.349860,-8.422286,9.810689,-0.252074,2.062770,-9.632214,5.895555],[-5.252804,4.129364,3.854742,8.123558,2.235455,8.081477,9.410981,8.208579],[-4.035022,-8.376847,-3.712749,-6.647211,-3.167621,0.116998,2.423029,1.864784],[6.315397,-4.902572,3.014005,-6.081489,7.365654,3.712871,-9.979917,-3.715273],[3.121220,4.201169,-6.677051,-2.505301,3.211816,-2.338632,0.677094,-6.707990],[-2.453596,6.194264,-6.963616,4.052718,-1.154272,0.007009,4.136159,8.847570],[-7.119954,-7.869108,-4.981158,2.083068,-1.856962,2.674031,-6.777533,5.391700],[-5.691245,-4.247704,-4.959298,-7.976155,5.033097,6.569925,5.709159,8.821315],[5.385418,4.899640,7.677949,-4.541870,-4.383065,6.189991,6.640676,5.236976],[6.209576,0.688732,8.491344,-5.150064,4.388032,7.134936,-5.854228,-6.116193],[2.355554,-1.023108,3.464725,-0.379684,-7.229733,-6.331330,-4.188628,3.121224],[6.715777,1.149670,-6.271691,8.478417,6.041019,8.974729,-3.762923,-1.133240],[6.236141,-2.432152,6.016129,-9.843206,-3.997521,1.607073,-7.688941,-5.160926],[3.652635,6.195917,-1.269594,2.117030,1.615058,5.820310,8.148395,3.092758],[-1.162442,0.475736,4.082822,9.086670,-0.978415,-4.168359,3.422650,-8.997014],[1.072517,7.216598,3.305817,4.541124,4.931132,-9.106680,-1.841701,3.208723],[3.041815,-3.822128,-5.926629,-6.667434,9.493924,8.636723,0.715502,7.582823],[2.312594,-2.194610,-3.357245,-7.206754,4.727401,-7.793374,-5.206052,-3.673252],[-3.435846,-6.756968,3.338468,6.758255,-7.042020,1.395824,-6.140302,-9.906994],[2.225091,-9.110471,-5.916020,7.582305,6.703366,-9.830094,0.830568,2.767201],[8.372037,-6.878154,-2.651159,7.627136,5.736595,2.296995,-8.435769,9.551768],[-3.373047,7.691567,-1.359041,-0.455481,-8.822287,-8.335746,-4.984829,4.639681],[1.592371,-3.427360,4.895852,-9.384102,-8.398380,-1.046054,2.286169,9.459512],[-1.960106,0.416138,7.259783,-0.545311,-1.690498,-8.862586,9.187054,-2.495663],[7.663796,-6.625498,5.195355,7.391918,-7.382181,-2.204554,-8.983428,-8.346481],[-8.324936,4.714996,3.876667,5.934913,-2.738008,-2.973337,4.182731,2.770111],[5.851303,8.355954,-9.543871,9.240471,-2.095300,3.791739,4.604758,8.132946],[4.778959,4.997337,9.287465,-4.929565,-4.872530,4.116775,5.778626,7.328653],[-4.420658,9.020616,4.066669,-5.674158,-9.936559,-9.522800,1.081045,7.601902],[6.614832,4.817939,3.933662,-7.246245,1.217856,8.318693,-0.846748,7.139117],[9.154649,-7.590628,4.428934,8.289148,-4.470651,8.129421,2.585263,-1.044552],[-5.901534,9.121206,9.374701,9.888861,5.042466,3.803201,5.002437,2.690983],[-0.028120,-8.703592,-1.486420,1.918491,1.472639,-2.562730,-4.711632,9.805624],[-1.097700,-6.253103,1.601204,-7.106426,0.010092,-0.648034,7.933242,7.851818],[1.182950,2.669281,0.859874,-3.414918,-4.247113,-4.877113,0.131212,6.250177],[-1.675893,4.425110,2.478878,5.309939,-9.231171,-0.297527,0.808219,7.247474],[0.467351,-7.641462,7.426218,5.921739,4.653713,-6.874027,-6.653681,-7.572365],[-1.861785,-3.596827,-5.075821,-9.484646,1.296148,-0.795128,-0.560832,-0.675398],[-0.339531,6.923987,7.947967,8.509925,-7.517663,-1.230902,5.394938,7.163046],[-3.870685,-2.113517,2.036241,9.392463,7.699884,0.294647,2.090468,8.001422],[-6.797605,-2.417981,5.735059,-7.325743,6.337672,-1.627417,-2.560071,-8.745314],[5.730767,5.566487,3.004591,-9.094606,-1.239755,3.217246,1.459608,5.295241],[5.686778,5.158676,-0.703835,-6.366748,-8.673946,-0.967181,-0.461210,-8.968169],[5.866107,6.574374,-4.958114,5.990184,9.392343,8.246581,0.796897,1.016695],[-5.988363,-9.993553,-8.527617,-3.399425,8.386919,4.945615,-9.050035,-2.659715],[5.185797,-0.023827,3.483748,-8.153456,-3.244016,4.843362,8.158688,-2.254542],[2.436832,-1.967954,4.354002,0.023398,3.115769,5.415574,-8.721862,-7.885291],[8.815275,9.733972,-6.057123,3.829040,0.937388,3.568710,6.936719,-5.144612],[-2.872812,2.728542,-2.791946,-3.749585,5.772425,0.555438,5.318278,-9.939297],[-4.957367,2.833228,9.233191,-6.321051,5.120013,4.709920,0.715847,-0.230866],[-6.985764,-4.864279,-4.431909,7.222317,-2.902575,1.831908,-3.026565,-5.204615],[9.500726,1.929755,-1.784240,-2.941354,7.817266,4.587121,9.338288,-2.963099],[8.922409,-1.738675,-6.368198,5.671535,-1.445559,-3.378675,-4.909259,-0.252133],[1.076447,3.461170,9.789565,7.415249,0.397775,5.587528,-5.514348,1.935040],[-5.768286,5.883642,4.800207,0.387263,0.486311,-9.396714,-2.886598,-6.295611],[-2.750457,-2.862781,3.996104,1.045039,-6.918701,5.536592,-0.019808,-6.708752],[3.509991,7.279759,-5.430956,-7.746840,8.025552,-2.027917,0.882206,2.830872],[-4.217493,3.995697,7.852386,-7.691034,-1.308265,1.966910,-9.699770,2.284035],[5.809989,-3.568060,-9.389286,-5.320057,0.088097,9.905826,6.455549,6.682080],[-3.175566,7.799194,8.801806,6.348986,1.725794,-2.848872,-0.768939,7.103438],[6.126198,-7.067478,2.428009,2.188634,0.982419,1.692395,9.975447,-0.711017],[-6.397577,1.913734,3.366996,3.512529,7.887018,9.055007,4.965587,-9.076553],[-2.059345,-4.092453,1.564931,6.175347,8.363513,8.185591,0.067354,-2.288102],[7.655747,5.377797,5.906668,5.918818,-5.318945,-9.078458,-9.898240,-5.787690],[4.788172,-5.525781,-7.585486,6.929930,-5.608446,-7.453708,-4.309535,7.035905],[7.932979,8.378442,5.529774,2.617888,5.702907,-3.544085,-6.480728,-6.300180],[0.004764,-8.115662,-0.526713,9.981223,-3.155385,-7.587970,3.068536,-0.009393],[-5.279190,6.138513,6.383198,-8.516348,-5.300863,-7.737672,5.252792,0.155456],[2.041760,9.722798,2.215899,-5.478990,-4.565658,2.122255,3.229100,-3.318465],[1.680578,7.761140,8.191403,2.852305,-5.109730,-4.147723,-6.710386,1.048639],[-8.752395,-6.489624,0.912647,0.618377,1.510881,6.945386,5.822851,7.328773],[9.629599,2.190665,-6.083011,5.149953,-8.403591,-9.671789,2.605514,-0.329212],[-8.093404,9.122330,9.516647,-8.963852,9.378877,3.553157,9.444548,7.763428],[-6.200866,9.962501,5.919045,8.624371,5.383543,5.976207,4.881840,-3.140448],[-9.505069,-8.885400,-5.794029,-2.974026,-9.050462,-3.951269,-6.035327,2.625072],[-1.952162,9.628025,9.211197,0.224732,1.763441,6.163255,-4.049745,-7.946621],[7.437092,6.451559,2.225814,-3.512104,9.387542,-2.241077,-1.968916,-3.921415],[-8.512193,5.426230,3.883420,-1.716258,0.340422,4.187829,0.059166,-6.690569],[-4.272322,4.381807,0.173039,-6.185517,-1.084632,7.264919,-2.568917,-0.861207],[2.785211,-4.433150,-8.306831,4.773300,-1.337801,-8.589504,1.381921,-8.996916],[-6.153521,7.217199,6.261136,-4.954892,-8.270981,8.661891,-6.122120,-5.321438],[4.695904,-4.969919,3.188147,1.106750,-6.752109,-5.286440,-1.904687,-8.342683]], dtype = "float32")#candidate|3437|(120, 8)|const|float32
var_3438 = relay.var("var_3438", dtype = "float32", shape = (4, 108))#candidate|3438|(4, 108)|var|float32
const_3439 = relay.const([[-9.379806,0.651111,9.771740,-7.321026,8.896348,-9.826287,0.697568,5.699730,3.289215],[-9.040382,-3.858040,-2.248854,4.897666,8.920095,-9.284643,-4.506993,-6.972387,-8.053848],[1.896005,4.134393,-5.767719,8.006776,-3.683114,7.406250,-5.092663,4.977863,-9.485250],[-8.411904,6.728190,-8.157180,7.654884,5.699475,-3.364871,9.176168,-5.930905,-9.983392],[-0.677885,-7.546471,5.506491,-8.088843,8.402010,-5.296857,2.994326,0.444789,-6.843119],[-8.212421,7.435017,-4.306437,1.330242,4.915478,-0.299005,-4.140331,0.942706,9.094258],[-4.462208,-0.126976,5.278298,-9.028742,0.002655,0.855460,1.489522,7.762277,7.299433],[-4.373164,2.817625,-7.602333,9.296832,-6.753811,8.901541,7.446810,-4.018347,2.004724],[-1.011656,-3.881854,-6.119422,-1.529894,-4.176896,-0.040123,8.770179,-1.754454,-6.596827],[-5.516743,-1.038807,6.746738,-5.451534,5.531063,-7.458881,-4.770791,-5.545573,7.012740],[-4.563408,-1.055288,7.287932,4.361723,1.106195,-4.031297,-6.076745,-2.715416,3.942742],[1.765399,-9.204902,-5.071071,3.466392,-5.397058,-1.037140,-6.119280,4.664309,9.517849],[8.217808,4.435487,-2.424088,8.198803,-8.082298,5.626902,4.594415,7.801126,-8.872721],[-3.438774,-1.661541,2.699694,-3.019032,2.160015,2.624523,7.682576,5.658993,1.676116],[-8.946479,7.225572,-1.897360,-8.233394,2.015442,-7.392588,-1.514326,6.457558,4.345308],[3.930610,3.705507,9.733151,4.908452,1.268036,3.402204,-7.613547,6.781251,-2.158789],[7.893842,1.337141,-9.106667,-3.765690,7.993761,0.027888,-2.834791,-6.297383,9.958391],[-2.821390,-4.075526,-2.423205,6.861426,2.702840,-5.977007,-4.384190,9.548956,-6.998539],[9.563404,-0.870297,-1.582682,6.085664,-3.842786,-2.029382,6.899038,-6.484362,3.237938],[4.087380,1.133493,0.140154,-7.463756,9.477581,-3.907216,3.328193,-4.246187,-5.520221],[2.183212,-4.803395,5.271208,-2.099504,6.304813,9.621625,9.513271,1.891076,1.068861],[-2.594950,0.593284,8.982986,6.100168,2.123447,-0.035578,-6.435902,-4.938440,9.925807],[-5.232199,-7.925576,-6.037160,-3.152435,1.988793,9.615529,-9.398329,-6.043898,2.864424],[8.373962,1.550182,1.330460,-9.788807,5.132210,-7.463266,7.034395,-8.920757,-0.519921],[4.181922,-5.926677,7.970148,4.886574,5.141803,7.581424,-6.492512,0.433409,6.432391],[7.726513,2.059244,-2.853999,-4.946042,-5.466630,-3.908032,9.905156,0.825637,-2.177994],[4.407107,-1.874371,4.816897,-4.991100,1.183667,8.969773,-1.798638,-8.317934,-8.356895],[2.111269,-3.181721,9.010117,-9.832916,-5.005815,6.893033,-5.031545,8.183647,6.620893],[-5.960035,-4.654498,-6.386866,8.499226,-4.113596,-3.681638,-8.758375,0.018525,0.487535],[8.494760,-4.802300,3.475486,-6.037326,-8.767361,-7.415530,2.068861,4.172972,-5.199304],[4.755775,-4.188227,-5.911784,-7.193654,-2.377359,2.722403,4.061314,-3.145120,5.558124],[1.674787,7.619763,8.950449,6.523405,5.564535,-3.211292,-1.961752,5.504812,7.985988],[6.089605,-0.729157,-8.011756,4.952964,9.404455,8.212654,5.809479,-7.604972,-2.221851],[9.111843,-3.496678,9.383419,-9.280359,0.643858,-6.653587,9.355488,-9.181224,-6.449853],[-8.793259,-6.255122,8.343352,-9.255571,-4.752412,4.507263,-3.384583,7.406431,8.180139],[8.088101,-2.479497,6.251540,3.765534,6.787946,8.867398,-3.916514,5.268216,4.895520],[-6.974117,-8.471797,-5.045664,-5.065298,-6.307777,-9.559093,-5.414126,6.951352,-7.559909],[1.203523,-8.661666,3.821003,-1.944317,5.306343,2.242465,-8.772449,-3.135073,-4.648491],[9.070054,4.464543,-0.945137,3.896151,7.034625,-8.445800,-6.720625,2.721851,-6.576167],[-4.713811,6.282585,-0.492666,-6.611389,-1.276687,4.580021,3.696298,3.829153,-3.552211],[-8.404588,-5.551020,6.372044,6.307381,9.074130,-3.854538,-6.417993,-0.141909,-0.429663],[-6.582673,-2.008673,4.217852,1.729786,-4.316137,2.259460,9.265339,-8.408460,1.572246]], dtype = "float64")#candidate|3439|(42, 9)|const|float64
call_3436 = relay.TupleGetItem(func_3057_call(relay.reshape(const_3437.astype('float32'), [12, 10, 8]), relay.reshape(var_3438.astype('float32'), [108, 4]), relay.reshape(const_3439.astype('float64'), [378,]), ), 1)
call_3440 = relay.TupleGetItem(func_3062_call(relay.reshape(const_3437.astype('float32'), [12, 10, 8]), relay.reshape(var_3438.astype('float32'), [108, 4]), relay.reshape(const_3439.astype('float64'), [378,]), ), 1)
const_3444 = relay.const([[[3.161375,1.825667,7.427681,6.705905,3.388235,-0.502507,-8.432383,2.017916,6.833845],[-7.776418,9.875789,0.131206,-9.263748,4.481223,-2.022446,-3.453892,6.328021,-9.788534],[3.883553,-0.739054,7.363768,7.143057,3.742754,-9.511713,1.571910,3.663105,-1.530456],[5.877289,6.738105,-9.260931,7.871953,4.995512,5.682100,0.968674,8.058210,3.010226],[-3.177147,-8.121193,6.084082,8.499856,1.439333,-9.941729,3.543081,-4.074609,-7.205129],[8.520158,6.022160,-2.859526,-0.755631,6.903461,1.241499,0.624022,2.501721,7.226241],[-1.161354,3.191309,1.441364,8.800534,-9.987006,0.779306,8.881650,-0.283388,0.099722],[0.759610,4.770089,3.234944,3.367357,-4.690284,-9.879031,-7.821483,-8.243011,-0.527747]],[[7.503542,6.636461,2.987841,-0.986347,6.183544,-0.108098,3.366176,-7.403409,-5.409761],[5.275287,-6.126737,9.614684,0.475180,8.770483,0.662339,-0.439341,-8.905451,-8.587083],[-2.543798,-4.377648,-9.187034,1.288635,-4.788134,-6.832897,7.396838,-6.037234,8.930852],[5.999947,3.438725,6.314920,-0.693643,3.965951,8.210289,6.812981,-4.398306,6.508691],[-8.216879,-9.762896,-5.673048,2.423742,-5.285915,-5.494388,2.790973,0.263069,-3.091168],[-7.270788,-8.204108,2.700107,0.163271,3.544439,-0.008289,-8.937150,3.129132,4.299751],[9.564078,-6.458814,1.738020,-5.144726,-3.173962,4.853952,-3.165145,9.066095,-6.748552],[-4.090391,5.466094,9.595332,-9.659315,-3.368040,1.078467,6.310747,4.392579,-7.153708]],[[-3.976762,2.550904,-2.610506,-5.508981,-8.126187,3.461377,-0.392085,4.169858,-4.279639],[-9.283277,-7.975596,-1.411855,-8.741853,4.032816,7.793483,-6.371480,-9.168360,-5.176993],[7.381523,9.721207,6.311619,-0.901921,-7.138951,8.496950,-9.505479,1.307035,1.935302],[-4.508577,6.216005,7.241758,-3.955247,3.587177,2.306014,0.692703,-1.338522,1.546845],[-0.734644,2.527457,9.295902,9.154619,-6.148023,-3.461878,-2.175674,-8.377187,-8.424514],[3.771583,7.923851,1.943880,-0.722417,0.324374,9.395819,-9.850907,-4.149827,-9.455670],[3.165898,-2.034105,-0.404503,5.370899,3.236471,3.837941,6.732714,-7.602433,9.401925],[8.153345,1.066567,-0.553328,8.220039,-3.383403,-1.257387,5.729980,-2.141158,-6.115609]],[[3.974826,0.037520,2.596718,-4.515555,3.258067,1.574408,0.594618,5.353072,-6.587101],[6.412713,-6.866019,2.987420,1.609921,-4.813904,-4.645203,-3.990187,-7.015846,5.296022],[-8.641044,-0.529923,-3.987239,-8.328909,2.160639,-8.746566,6.351989,9.404086,1.367142],[3.379440,-0.941571,-7.064025,-1.329401,-7.096717,7.283976,-2.601424,5.928112,9.368428],[-0.050385,6.693047,7.215988,2.063105,-7.575254,7.222765,-3.603022,-6.405368,-6.135536],[3.934175,9.905759,-4.021607,5.020774,4.822483,3.853211,0.877322,-7.585940,4.206251],[-0.870364,6.664525,-1.427263,0.235683,4.852279,6.051392,-6.295586,-8.066204,-4.713774],[-5.812929,5.887704,-5.148957,9.572104,-1.591174,7.011912,4.793295,9.299352,-2.999795]],[[3.054574,-5.667690,7.882975,4.542841,-4.859293,4.960957,-9.320563,0.782668,2.601795],[-4.590055,3.449658,4.090991,3.328558,-0.012258,7.438556,-8.513460,-3.120875,4.001600],[-6.831461,-6.547505,-5.385324,2.449386,8.045073,-8.738558,-8.814660,8.809881,4.334297],[-5.821453,-0.508556,4.452616,6.024471,-8.311572,-6.240726,1.492320,-1.221842,-1.379654],[-4.562592,6.976677,-6.427315,-0.766442,8.114793,-7.223001,-9.080266,5.751746,8.000790],[-7.142846,-3.120159,2.653166,-6.908559,3.187700,-4.822401,8.048008,6.653594,-1.025700],[-1.757205,-8.279922,6.747332,4.603997,-2.951509,-8.771299,2.384478,-2.237218,9.025579],[8.177150,5.472065,4.068611,-0.406941,-5.633838,2.957923,4.125444,8.929827,2.249353]],[[-2.555950,4.073699,3.028537,-7.652429,-0.483333,-2.952113,-4.987292,-7.125292,-0.824771],[3.568425,-7.266393,-4.064789,5.798853,-1.903325,-8.937206,6.050484,-3.565690,5.962863],[-6.562026,-4.250989,-1.570779,-5.144335,-5.061095,-3.597814,-0.557574,6.865554,8.440201],[5.971755,0.288995,-4.235609,3.401548,-2.982332,-7.556599,-5.701538,-8.610521,1.536617],[9.101807,3.161003,-4.939420,5.414513,-3.683127,-3.232257,-6.771088,-7.144102,1.193571],[2.733814,-2.122646,-8.603327,8.586868,3.868666,1.396628,1.987348,-8.248022,7.606345],[-9.032788,-9.473598,4.712275,4.501071,-0.631013,-1.161048,-9.438068,-6.381486,0.460180],[0.633746,6.744470,-1.470044,4.962425,-0.573960,8.820216,7.067821,-2.961009,-9.603190]]], dtype = "float32")#candidate|3444|(6, 8, 9)|const|float32
bop_3445 = relay.right_shift(call_3436.astype('int8'), relay.reshape(const_3444.astype('int8'), relay.shape_of(call_3436))) # shape=(6, 8, 9)
bop_3448 = relay.right_shift(call_3440.astype('int8'), relay.reshape(const_3444.astype('int8'), relay.shape_of(call_3440))) # shape=(6, 8, 9)
func_2021_call = mod.get_global_var('func_2021')
func_2024_call = mutated_mod.get_global_var('func_2024')
const_3458 = relay.const([[3.466953],[-5.265764],[-7.617820],[-8.478629],[-3.552574],[5.443774],[-3.600327],[-5.409084],[-1.228669],[-1.787881],[4.753994],[0.343604],[6.173910],[-5.524288],[-0.960558],[-7.662326],[9.151375],[-4.459292],[-9.147854],[5.091094],[6.538512],[9.845330],[-4.244338],[-0.144668],[-8.907867],[-5.167685],[-5.480698],[6.033073],[-0.789625],[3.566637],[1.472341],[3.464985],[-6.657651],[-4.116544],[-2.540404],[1.272046],[-2.859514],[9.818611],[3.404088],[-4.108283],[-0.436927],[2.579888],[-0.652834],[-8.392495],[-1.412780],[0.135989],[1.011339],[-8.267188],[-6.674993],[-4.984121],[3.156886],[-7.295633],[-6.114151],[-6.862115],[-3.083589],[4.872759],[1.888865],[3.069336],[-0.579791],[9.325119],[-0.203245],[-5.325250],[8.110740],[5.593331],[7.201761],[-5.335605],[-0.404691],[2.602444],[-3.778051],[-4.587805],[-0.544310],[0.473747],[-7.355174],[3.377477],[-6.953841],[2.417327],[2.959730],[-4.617085],[5.235614],[-2.717390],[7.420299],[4.729928],[6.916994],[-8.283931],[-2.387871],[-5.317100],[-4.833080],[3.939865],[6.830623],[3.104922],[8.981100],[-5.036178],[-0.053768],[5.679854],[-9.655675],[5.249781],[-7.141118],[8.700783],[5.970340],[1.807552],[-1.372505],[-5.374454],[6.066383],[0.601121],[-3.862671],[-2.296103],[-6.559337],[-0.832458],[8.784548],[-6.189583],[9.330749],[4.780507],[-6.552270],[5.082456],[-9.149359],[8.028828],[1.785066],[2.478283],[0.686442],[2.498609],[-0.303180],[1.616988],[-5.676554],[8.003142],[7.362128],[2.616295],[5.710129],[-3.130189],[-8.105226],[8.232852],[-9.127987],[2.937932],[-9.634205],[-2.916179],[-8.282560],[3.745671],[6.386668],[6.737754],[-1.362411],[2.319864],[-0.443115],[-4.395295],[2.397886],[7.763532],[8.521619],[-2.478522],[3.084090],[4.866773],[1.287764],[-3.974482],[6.754450],[-3.924866],[-6.292713],[-1.066329],[-3.768238],[2.381479],[-1.301040],[5.767132],[-9.519274],[1.938399],[7.173711],[-5.977379],[-8.496636],[1.898316],[5.180961],[0.013405],[8.605188],[-3.038115],[3.227901],[8.214269],[-1.116819],[-8.168832],[-8.213507],[0.097265],[-3.774794],[-1.224561],[-0.914252],[-6.531695],[-4.934261],[-9.454604],[2.974656],[-9.583950],[9.313887],[2.346278],[4.031624],[7.541873],[1.653960],[8.293329],[3.970777],[-0.818649],[1.489820],[7.739842],[9.404988],[-7.344087],[4.033340],[-8.919802],[-5.062261],[-8.893126],[6.378383],[-1.252761],[-1.614988],[-0.967281],[7.262861],[6.353711],[-8.141220],[-6.553024],[9.251110],[-7.834031],[-9.295740],[-0.721936],[3.025969],[-7.069074],[-2.796355],[-6.434820],[-2.672276],[-1.445727],[-3.346728],[-8.782025],[-7.223100],[-2.007905],[-9.090618],[3.035295],[-7.830409],[-9.684134],[-5.899640],[8.092215],[8.287296],[-0.822776],[-7.918264],[4.636518],[6.407953],[2.890514],[4.922633],[-0.518686],[1.779856],[-3.843635],[0.213438],[5.960214],[0.844416],[-6.099757],[5.454540],[-2.147097],[-8.208541],[-5.105294],[2.108232],[8.090650],[1.190323],[-4.035872],[2.995226],[4.048366],[0.074230],[-7.761773],[3.620735],[-3.727709],[9.257887],[-6.138036],[-4.932925],[-4.362567],[0.361700],[3.489121],[-2.013354],[-5.072432],[2.579613],[-4.166226],[1.449648],[-3.456276],[-8.788769],[9.362641],[-6.122144],[-8.375274],[5.549614],[-3.262287],[8.973521],[-0.534415],[0.192492],[0.299970],[-4.068547],[-0.995626],[-9.395370],[-7.549840],[-3.470631],[-4.939928],[1.087267],[-8.724162],[-5.252143],[-1.235045],[3.387283],[2.035161],[9.697869],[-8.295261],[-5.148071],[-0.080487],[3.475649],[-4.105393],[-6.241273],[7.999795],[9.571924],[9.342147],[7.113439],[9.667812],[-2.615892],[0.726711],[-9.077421],[9.978629],[-2.505919],[0.593434],[9.393946],[-4.247632],[-7.748329],[3.062518],[1.399706],[8.102445],[-4.983028],[-5.341447],[-7.153858],[5.830012],[7.812490],[-0.394245],[-5.826344],[4.240922],[0.911733],[1.854190],[-9.973471],[7.554469],[-8.805262],[5.531887],[2.799122],[1.152787],[8.957108],[-0.759248],[4.231844],[3.478380],[-3.847230],[-6.406557],[7.426304],[-7.757674],[-9.152001],[8.487152],[1.696767],[6.476205],[1.710042],[0.990431],[3.171769],[1.820854],[-5.519624],[-5.930384],[3.128966],[-6.620849],[-9.533220],[-6.352972],[-6.108299],[-1.567827],[-5.257194],[-4.061043],[2.128306],[-3.452492],[-3.058805],[2.832796],[-6.451382],[2.296290],[-7.962465],[-1.719178],[6.128924],[-0.271471],[1.293472],[5.326890],[2.474223],[1.052405],[9.935262],[7.673689],[1.051494],[-9.595176],[3.148280],[-0.077702],[-7.208659],[2.908075],[5.849290],[-2.882362],[-3.259790],[-7.005143],[-0.398141],[-7.261676],[-4.518394],[6.498918],[6.971588],[-9.497464],[-1.948815],[-3.014774],[-2.449209],[8.000176],[-6.571995],[-5.678360],[-1.358247],[-5.632411],[7.433269],[0.477852],[-7.837439],[9.875379],[9.163688],[5.880156],[9.700629],[8.985777],[-4.740704],[4.047245],[-6.882609],[2.214841],[1.026918],[2.146189],[-9.243086],[3.057698],[-5.873782],[8.489598],[-9.358074],[3.046608],[-0.541000],[-8.373414],[-7.386354],[6.668050],[9.761846],[-0.957948],[-3.805963],[9.959418],[5.932442],[4.291787],[-6.075100],[9.355396],[7.821318],[-1.047262],[4.295127],[8.775697],[-5.671474],[3.279498],[-5.613602],[8.855461],[4.949663],[2.413574],[6.382685],[-1.032060],[7.586616],[-2.813595],[-9.148680],[1.036506],[8.422977],[5.207338],[0.929283],[-3.111769],[-3.217712],[1.867688],[-1.540406],[-7.761393],[-2.404490],[8.312807],[-8.903903],[-3.395320],[-0.206893],[-8.903932],[-3.658504],[-6.614292],[2.634545],[-2.382172],[7.173870],[-9.284382],[-9.519921],[-3.210773],[-7.226318],[-9.062958],[-2.021822],[-8.191084],[8.179694],[0.216136],[7.476380],[-1.203179],[7.502618],[1.798842],[-6.861451],[7.058233],[-8.977078],[8.028140],[7.115419],[-8.117498],[4.149341],[-4.057478],[-1.328655],[-5.419214],[7.352351],[4.509489],[1.886366],[-8.380251],[2.512036],[2.077074],[6.830846],[1.235763],[-7.976825],[-5.743005],[-9.904142],[6.815279],[-7.246665],[0.018033],[-6.848445],[-5.440007],[2.903829],[3.453897],[-6.016930],[1.717744],[6.241196],[9.442816],[-2.356743],[5.024695],[-5.396762],[-7.971666],[-3.967804],[-8.536010],[-9.610794],[1.156932],[3.278321],[-5.372554],[-1.803001],[-4.296580],[-4.524041],[-2.780818],[-6.624425],[-4.223671],[-7.447484],[-7.709258],[-1.865561],[1.517809],[-7.698516],[1.503119],[8.289653],[-9.377222],[-3.889188],[-0.981961],[-5.654168],[8.653610],[-9.941936],[-2.349549],[-0.358434],[5.892725],[-2.426950],[1.885043],[5.166151],[4.593712],[-8.968665],[-1.511636],[-2.171661],[-4.059272],[7.192763],[5.977122],[6.479665],[-0.398556],[-5.167157],[6.697115],[-9.599517],[1.910751],[-0.098226],[2.391845],[3.518568],[4.391167],[4.797910],[1.859104],[-4.862232],[-3.823972],[-8.731809],[7.593205],[4.185984],[-7.117426],[6.191282],[-3.248742],[-6.666419],[-1.457876],[-6.315539],[-4.510323],[5.635052],[2.637468],[7.366622],[-1.141738],[-6.554749],[-4.450838],[-6.939028],[6.776886],[2.075999],[9.629579],[0.211238],[-6.819345],[2.219613],[-7.657813],[-1.777659],[8.218240],[-9.162758],[-2.049300],[3.185399],[-1.128951],[-6.243413],[0.231554],[-1.832351],[-1.914264],[-4.383541],[-3.290624],[5.274505],[0.923705],[-7.872970],[-4.057086],[6.767343],[-1.746713],[-2.748757],[4.821237],[3.646042],[2.654044],[-2.425703],[-5.784393],[7.742614],[0.779349],[-3.275158],[3.517116],[-0.423785],[-4.191214],[-4.017501],[-7.169762],[-8.830340],[-2.274785],[7.298476],[-3.410541],[5.007821],[-5.627107],[-9.749284],[-2.608511],[1.042274],[5.608271],[-0.776568],[7.905884],[-7.765847],[7.995158],[-0.743302],[-4.473283],[-9.280380],[9.095815],[-5.845500],[-3.503252],[-2.304130],[-4.629809],[9.111109],[-8.037487],[-0.673403],[-1.505453],[5.071795],[1.643712],[3.655617],[-5.161141],[-5.217461],[-4.873298],[8.429105],[8.107506],[6.577144],[0.828742],[-1.535712],[4.889097],[1.669352],[7.544508],[7.271193],[-5.798175],[6.998877],[-4.369721],[-2.780732],[9.805845],[5.170759],[7.056384],[1.393800],[3.557117],[-8.042160],[-2.377529],[-5.524328],[-8.842456],[-4.849068],[2.968576],[7.053836],[-5.425366],[2.366890],[0.034763],[4.793009],[9.006508],[-4.620770],[-0.235907],[0.593862],[-3.564123],[-4.351852],[-8.146944],[-5.080757],[-0.610036],[-1.791115],[8.320730],[9.082343],[6.344221],[-0.480884],[-2.449262],[7.590630],[6.268868],[-3.142691],[7.744800],[6.989770],[7.376482],[5.444146],[-7.818020],[-7.077463],[-4.140934],[-5.541521],[-2.381682],[6.944828],[-3.315637],[-1.492244],[5.359247],[-0.238277],[8.448251],[-0.133164],[-8.689615],[4.859501],[-3.942497],[-4.962335],[-8.574002],[1.842948],[1.773437],[-9.917763],[-8.071239],[9.528223],[-7.139606],[7.494290],[7.181842],[-8.929849],[3.992998],[-1.974478],[-1.062793],[7.293592],[-4.802924],[0.096380],[7.924554],[4.504396],[-6.791970],[-3.941071],[7.541202],[7.869868],[-5.433622],[1.153773],[1.000734],[-7.103655],[2.007910],[-6.240635],[-5.922609],[-9.853781],[9.839460],[-1.364407],[-9.776553],[-7.842335],[0.380357],[2.328357],[-8.818754],[-1.458183],[-7.673876],[7.147049],[7.162545],[-6.768050],[-4.259232],[-8.489502],[-1.461402],[4.928259],[-8.833747],[-1.019383],[9.881737],[5.759609],[-5.492913],[9.117782],[-2.725748],[0.812555],[7.599289],[-1.927203],[-6.433722],[3.031971],[2.464874],[-8.616082],[-3.192061],[-4.619064],[9.584018],[-4.984507],[3.186824],[4.604645],[-6.029907],[-0.086376],[1.242652],[0.203558],[-9.464458],[3.805894],[-8.109867],[8.764487],[7.244881],[-5.179737],[6.311322],[-9.858755],[5.520023],[4.467114],[9.522631],[-2.707655],[6.066368],[-3.477745],[-8.040650],[-5.513748],[5.224405],[-4.086122],[-2.961127],[4.621727],[1.538185],[-5.150830],[-5.939132],[6.592488],[3.609983],[-9.947829],[1.317255],[-6.735598],[-7.412948],[2.426702],[2.596117],[2.983166],[-6.528935],[-2.461361],[-5.787183],[-6.962603],[0.111093],[-6.778819],[8.179762],[-5.981981],[6.689525],[9.130963],[4.853655],[6.853562],[-5.159648],[0.723095],[-8.287568],[-6.457640],[-6.556264],[-2.758823],[0.978216],[-7.615178],[1.290177],[-5.610034],[-4.364343],[0.817033],[-8.960031],[-0.745790],[-5.244050],[5.696185],[8.820926],[-3.435701],[0.736601],[-5.551475],[-5.494037],[-6.016156],[5.706254],[-8.558696],[-6.699348],[6.091281],[0.160238],[-9.583348],[-7.369676],[-5.904908],[-3.700784],[5.093515],[-0.382414],[-3.005234],[7.357788],[2.432793],[6.948491],[6.292028],[-3.760807],[7.225794],[-3.286431],[5.981675],[4.499408],[4.235054],[-6.735590],[-6.178366],[5.525194],[-6.758870],[-6.611311],[-3.179460],[9.029134],[1.786237],[4.352277],[7.266382],[-4.833947],[-7.735460],[-8.734495],[9.047778],[8.398263],[3.267877],[-4.273937],[3.923899],[9.050385],[2.961477],[-7.314979],[2.495612],[6.273360],[-0.814244],[5.360796],[-8.724260],[-8.369657],[9.522737],[-7.561804],[-3.957222],[7.985763],[5.758574],[1.387795],[-9.981791],[6.248598],[-9.783005],[9.115914],[6.172403],[-7.834942],[9.835203],[-3.631617],[-1.772136],[3.068537],[9.979268],[-3.323904],[6.149323],[3.636084],[7.787716],[4.033750],[0.915716],[6.074407],[-7.027108],[-1.487657],[4.761591],[2.439788],[-1.279271],[-6.604603],[-4.089825],[-6.933795],[8.479505],[5.877618],[4.984829],[9.367614],[-8.746487],[-7.731789],[0.769819],[4.442528],[-9.022223],[-0.666959],[4.971325],[-4.978184],[2.594165],[-4.356351],[-5.804712],[7.773331],[9.386934],[1.599098],[3.021922],[0.054364],[9.062280],[2.955175],[2.866170],[2.205504],[-6.904688],[0.147959],[9.053929],[-6.735039],[-3.839560],[1.258316],[5.821417],[-6.523915],[9.987507],[5.646728],[-0.540600],[-1.459550],[-1.860189],[7.203705],[5.892892],[9.212069],[-2.660676],[9.973057],[8.932090],[-1.457764],[-2.079938],[-9.198703],[-4.942211],[-4.043088],[-3.236331],[-9.548283],[-4.826377],[0.240278],[-4.389453],[-2.681742],[1.631244],[-1.715987],[-7.323115],[1.412232],[1.142010],[7.792621],[6.675726],[7.772443],[-8.639922],[-2.676638],[-8.396851],[2.224827],[3.759850],[4.323416],[5.725835],[9.947098],[-9.075919],[-8.596730],[1.718374],[-1.743572],[6.663401],[-1.398275],[1.442612],[-8.173274],[3.296656],[9.954373],[9.436309],[-2.796072],[1.503002],[6.172586],[8.735171],[4.222186],[-5.674590],[-9.652207],[0.048255],[-3.594343],[-6.375637],[-6.126927],[-0.253888],[7.834208],[8.579513],[2.458242],[-0.195852],[2.551853],[-4.171598],[-0.719074],[-1.835184],[3.443282],[-2.367047],[-3.634384],[-3.444938],[-4.502282],[-4.119379],[-2.530245],[-9.886329],[-6.102439],[-2.516168],[-2.499770],[-4.782318],[-2.190562],[-1.111234],[-6.218045],[-0.576079],[8.031273],[-2.659960],[9.084469],[-4.336992],[8.376382],[-6.075231],[-7.335799],[-2.711749],[-4.967517],[-7.819471],[2.442965],[-9.691979],[3.782381],[-4.785563],[3.665034],[4.885911],[3.163140],[0.581508],[-1.206711],[6.040252],[-0.622724],[-9.998955],[-6.625750],[0.236857],[8.996779],[7.084394],[-4.692688],[6.234715],[4.072385],[-6.616188],[-0.928764],[2.431426],[2.310014],[-0.286510],[7.143440],[1.253546],[7.985327],[-7.836006],[-6.595756],[-8.500108],[8.298712],[-9.438841],[-2.864754],[-8.660193],[-5.594641],[-3.199169],[-5.768577],[-1.230827],[-9.693603],[-6.951495],[-1.714146],[1.832758],[9.844602],[3.608874],[-2.193321],[3.946739],[-2.618584],[6.423866],[0.034713],[-9.122884],[-9.553229],[7.458044],[-5.045414],[-6.878504],[-1.243015],[-0.752220],[9.474414],[5.229304],[0.652188],[-9.367884],[-6.933305],[-3.784732],[-0.525577],[4.485551],[5.382413],[0.519733],[8.969310],[-4.299209],[-3.737706],[-8.197736],[8.391019],[-7.509843],[0.920617],[1.966652],[-1.104620],[-0.520262],[-7.970704],[4.747652],[-3.451676],[-1.121963],[-3.728219],[-6.202345],[-6.185337],[-4.798736],[4.974353],[-7.969016],[0.157157],[1.004972],[-4.959947],[-7.422455],[6.603870],[1.606196],[6.245239],[-8.778978],[-0.761543],[1.116331],[-2.883008],[-1.803719],[-4.237947],[6.094213],[3.933310],[6.996263],[-4.036729],[8.989540],[0.577257],[-2.246127],[-2.279518],[-6.273577],[-8.831678],[-8.005207],[-0.868617],[-3.610277],[7.498840],[6.153889],[4.596603],[6.422218],[-3.036165],[9.795525],[-0.559621],[1.009209],[-1.966443],[-0.298865],[-3.657748],[-4.730282],[8.947848],[7.479685],[-3.336274],[-1.501152],[-6.453153],[-7.393685],[-1.247240],[-0.736592],[-7.871142],[-7.971970],[8.752273],[-9.083594],[5.914507],[-6.448060],[-5.253898],[-5.465230],[2.273982],[1.344941],[3.952049],[3.264909],[4.506276],[4.852121],[-1.068696],[6.062178],[-0.158953],[2.326091],[9.283688],[8.757603],[-8.734181],[-7.822099],[1.233237],[-1.628379],[-7.506781],[-8.079597],[0.608173],[7.452060],[1.248748],[-1.743982],[0.360610],[-4.375575],[8.965994],[1.417294],[-1.287420],[3.912426],[-9.858660],[2.174069],[8.218656],[9.760679],[3.260894],[9.270123],[0.809668],[9.062348],[-7.379398],[-5.230647],[9.771327],[1.794303],[-8.233489],[-5.154729],[7.928072],[0.148330],[8.127361],[0.303460],[-8.356183],[4.117700],[7.152972],[-1.820840],[8.517215],[2.568293],[-2.775744],[7.437979],[0.274361],[-1.396684],[4.261845],[-3.292023],[4.940008],[7.767842],[-5.564579],[5.094165],[9.946511],[-1.971230],[5.507078],[9.680559],[-1.671807],[-9.239363],[7.836835],[8.097293],[-1.712079],[-8.067210],[-0.460877],[3.510971],[5.785262],[-1.743802],[6.903766],[-5.324753],[-0.811862],[2.006635],[-3.451176],[3.264407],[-0.334083],[9.478919],[4.423590],[-1.706181],[-6.329433],[-1.369998],[3.232178],[-0.161761],[-3.712335],[-6.946370],[-6.464159],[-2.443390],[7.474918],[3.037246],[-3.228161],[-2.048321],[-8.652823],[-9.699120],[-2.532211],[-6.252573],[-6.518134],[7.790539],[-4.631458],[-0.354217],[9.064099],[-4.101274],[4.173083],[-5.105279],[8.409957],[-9.515158],[-8.530604],[-6.100400],[-0.931942],[6.821150],[7.633689],[-0.365134],[-4.874543],[4.297882],[3.716363],[3.426853],[-3.288053],[8.317724],[-1.919789],[-5.834109],[5.523060],[4.898452],[0.023646],[-3.698204],[2.707284],[9.260511],[6.767205],[-2.372639],[9.077679],[-0.840336],[0.567553],[1.228608],[-1.825852],[3.070702],[5.885938],[-8.041723],[5.814384],[-0.782360],[9.033197],[-5.409378],[-6.780974],[7.394647],[4.379547],[1.471826],[7.594877],[-4.157775],[3.205548],[-2.323715],[-7.586413],[-9.732198],[7.025527],[-9.002205],[6.822133],[9.428904],[4.636470],[2.156839],[8.733938],[-7.182622],[-8.240543],[-7.497387],[8.579373],[-5.858645],[-5.074610],[-9.046662],[-6.416395],[-1.717630],[6.387382],[-8.566619],[-5.816052],[4.005233],[-0.343713],[4.744751],[6.923833],[-6.649355],[-5.015319],[8.767028],[1.354892],[-8.473189],[-2.745311],[-1.361739],[-9.150791],[-3.540760],[1.352283],[-4.703763],[3.899253],[-4.945021],[-7.354081],[9.828405],[8.309840],[7.791215],[-3.110840],[2.741643],[-2.415259],[-0.111180],[8.888649],[2.149710],[0.946048],[7.162328],[8.830561],[-3.117965],[-2.278426],[-3.228866],[3.208631],[-6.119461],[3.751867],[-5.726577],[5.583882],[-7.403047],[2.411531],[-8.759124],[8.172810],[-9.332866],[-3.003904],[-4.993602],[0.735663],[-6.614482],[8.820413],[-6.964037],[-1.345818],[0.950961],[-9.696844],[-7.890760],[5.447202],[0.833152],[4.856935],[0.140186],[-5.675314],[3.505870],[-0.539152],[-9.390054],[3.950792],[4.060844],[9.794075],[3.453736],[-2.129341],[0.021904],[-3.761883],[-6.515950],[-0.390785],[-5.600727],[-7.621178],[1.433715],[-8.983078],[8.753126],[-6.943923],[-1.019371],[-8.992393],[-7.670560],[-2.282768],[1.834774],[-6.247427],[3.952494],[-4.884219],[-7.171239],[-4.687564],[-6.239393],[6.097846],[0.835819],[8.298208],[-8.748440],[-1.034825],[2.260788],[-6.863279],[-2.077623],[0.120488],[7.994952],[-4.129315],[-1.209456],[5.981119],[-8.142456],[9.015317],[-9.685865],[-7.685557],[-8.371306],[-9.210125],[4.623885],[-1.184537],[6.827549],[-1.478305],[3.103534],[9.377023],[5.040755],[1.570638],[7.211827],[-8.096871],[-0.603390],[-2.875122],[-0.130392],[-0.835966],[-5.549128],[2.873325],[5.940907],[-6.836134],[-8.084635],[-8.147821],[-2.919373],[4.893109],[-4.754512],[1.232394],[8.602394],[2.201623],[-9.689027],[-5.563179],[-4.363544],[9.962312],[8.874876],[-1.880493],[-9.296667],[8.748530],[8.269913],[-0.659925],[3.488141],[0.895628],[8.131078],[1.778335],[-2.239925],[-7.458222],[9.782185],[-8.554316],[-5.306016],[-8.930369],[-9.150036],[-4.153113],[-2.351613],[-7.208345],[-3.030330],[2.487915],[-9.495692],[8.903650],[-4.812220],[-6.955775],[0.137865],[8.926737],[7.630065],[-8.948151],[7.765026],[1.621180],[9.802520],[6.411982],[5.252317],[7.270579],[-5.826406],[3.581368],[1.315371],[-3.243272],[-0.586993],[-5.462906],[-4.318781],[-3.628324],[2.658541],[9.904167],[7.947093],[7.818260],[-8.732491],[-9.900585],[-2.592511],[4.253553],[1.149835],[8.344756],[0.430824],[-9.242324],[-6.023966],[1.403430],[-9.812545],[-9.994895],[-8.625648],[-0.809297],[-9.640519],[-6.943806],[-0.879465],[-2.035587],[-0.481705],[-4.589060],[-4.645652],[-4.332826],[4.413577],[7.674075],[-3.660476],[-6.912179],[-6.748008],[-3.469509],[-1.925263],[6.655374],[-5.589102],[-8.796484],[-5.393627],[2.569798],[-7.717772],[-4.285660],[3.813964],[5.181906],[8.895240],[-2.153065],[7.463159],[-5.277164],[6.112770],[3.002641],[-7.389235],[-1.322209],[-8.607104],[8.130718],[3.470852],[-4.837883],[-1.496785],[0.443372],[9.550916],[5.004199],[4.049576],[-6.379819],[-8.113756],[4.422539],[-4.748112],[-8.009015],[9.902053],[6.451933],[6.987182],[-1.653280],[-4.125018],[-1.308183],[-3.021886],[-1.349638],[-8.281628],[-2.269882],[-8.422842],[9.998782],[-3.012240],[-4.180829],[3.413483],[2.410616],[-9.686918],[-1.131318],[3.187425],[-4.968874],[4.014195],[9.221931],[-1.316396],[-9.808647],[4.864437],[3.355476],[0.364471],[-7.085188],[0.242205],[-6.682510],[9.114881],[1.318452],[8.297639],[1.602871],[-5.466906],[-3.413773],[6.322789],[8.272023],[7.184083],[-4.107926],[8.072664],[-9.573729],[-3.063616],[-0.684088],[-9.616305],[-6.746416],[-4.541500],[1.803849],[-8.000155],[-4.956257],[-8.869290],[-1.793890],[-0.951662],[-7.690414],[5.373879],[-9.753636],[-3.652884],[-9.561822],[-7.915052],[-8.573455],[9.782138],[-5.716143],[-8.415880],[4.793764],[8.916010],[6.004033],[-4.450747],[3.751965],[-1.952319],[4.890400],[-5.568784],[-7.993239],[-2.697943],[-5.871770],[1.619734],[7.660405],[3.875993],[-2.090784],[5.473384],[-8.325343],[0.578805],[6.688016],[-3.499096],[7.802513],[-8.535298],[-4.967091],[-6.738067],[1.517183],[9.897269],[5.161904],[-1.090725],[-3.585175],[7.317610],[4.263450],[-1.128778],[3.611481],[7.222618],[-0.226542],[1.954227],[-0.359965],[-7.062044],[-9.682776],[3.843829],[6.552730],[9.184419],[0.560802],[-9.865205],[-4.933686],[-5.049198],[-2.481026],[3.236850],[6.768207],[-7.587931],[-5.392928],[5.021029],[6.631693],[-7.666301],[-2.402406],[1.641925],[-2.697522],[8.055325],[-0.253266],[2.955448],[6.964614],[-3.295407],[1.263320],[7.217457],[1.353784],[-1.717335],[4.340901],[-4.300653],[6.497291],[-4.035815],[2.920561],[9.925058],[5.933280],[0.482629],[-2.519896],[-0.165514],[0.146000],[-6.435398],[-6.910768],[3.392631],[7.527883],[-5.490180],[1.136200],[-5.869392],[1.734923],[-8.053714],[-3.657391],[-6.264937],[-1.539494],[-7.807493],[5.729675],[-9.039235],[5.900106],[5.437225],[-2.946635],[6.228807],[-0.876207],[-3.291194],[9.860741],[-2.747220],[-3.565031],[2.763757],[-5.382988],[-1.906049],[6.648864],[-6.847998],[2.336022],[2.233955],[1.060365],[-2.108960],[2.716814],[4.445258],[2.960350],[3.108368],[-4.735852],[7.076797],[5.503582],[-9.014076],[6.954667],[-1.488685],[4.790748],[4.904410],[-5.597844],[8.720504],[3.456578],[3.313538],[-5.836799],[-3.490124],[5.394244],[-3.646679],[8.038019],[-9.636286],[-8.750440],[-7.450093],[4.711749],[-1.876229],[5.361633],[8.500831],[9.954401],[0.213552],[-8.514957],[7.720396],[-2.550526],[9.865134],[-8.161084],[2.013260],[6.214938],[-4.472294],[-2.121937],[1.412665],[0.309622],[-3.729832],[3.585204],[-8.493515],[5.637210],[1.325429],[8.841796],[-8.823002],[-0.778150],[3.395065],[9.293611],[-0.568692],[-3.840930],[-1.493812],[-4.943570],[-7.395018],[5.850358],[-1.630907],[-6.366819],[8.759819],[2.249734],[0.356543],[-8.545592],[-1.167240],[7.028792],[9.501178],[-9.272514],[-2.828551],[-3.596927],[-4.285310],[-3.110470],[-8.702337],[4.013287],[4.533079],[-8.645450],[1.723426],[7.826695],[-9.284301],[-0.724808],[9.060509],[-4.684465],[-8.436531],[-0.157016],[5.067079],[6.807338],[4.094524],[-1.347620],[-6.327781],[4.475261],[3.035259],[-7.100802],[2.305849],[5.176538],[1.309887],[-7.449107],[-2.942946],[0.918978],[6.902562],[4.758928],[-6.280906],[-6.632972],[-1.703190],[-4.732671],[7.230175],[-0.361991],[2.083347],[4.281654],[1.596422],[-8.225808],[8.161781],[5.632862],[4.389831],[-2.642166],[-7.318946],[8.727888],[8.243150],[1.216925],[-6.222324],[-1.232516],[7.691267],[-3.787073],[3.798243],[1.171548],[-4.553419],[-2.060517],[-2.342762],[7.701595],[-0.787974],[-0.383885],[6.024946],[-0.829983],[-1.825958],[4.439832],[9.617316],[-8.543127],[-6.816205],[5.911725],[-2.745215],[-2.910779],[-1.466271],[-2.266362],[-0.541427],[-8.973118],[-4.519652],[-5.512950],[-4.498243],[-5.953834],[-9.436505],[6.774413],[7.368364],[-8.439996],[-8.517070],[1.079452],[-8.922438],[4.843708],[-7.629976],[2.209037],[-6.939570],[-2.474981],[-0.768889],[-0.722848],[1.310672],[9.895759],[-6.367857],[8.198736],[-4.292518],[-9.703191],[0.311845],[-3.736170],[9.857929],[-0.892026],[0.506828],[8.231292],[4.352847],[-5.295799],[-0.623781],[-8.385905],[5.572713],[6.613616],[-4.386208],[0.403227],[-0.489549],[9.485596],[-5.317008],[7.327504],[6.442058],[6.166789],[8.619830],[-9.383299],[-2.457773],[-5.413222],[-9.903056],[-0.299207],[5.208345],[5.799357],[-8.452158],[-9.849391],[-3.687872],[-3.603327],[9.713233],[9.528601],[2.378209],[-6.653394],[7.007214],[3.650160],[1.954813],[-6.763665],[-3.706638],[-8.029543],[-8.752147],[1.186469],[-6.084601],[0.858552],[5.207628],[2.112817],[0.750676],[-9.081539],[-5.760428],[3.014841],[5.652130],[5.705670],[-8.581442],[-6.168659],[9.236407],[-2.714930],[8.498271],[-4.809593],[-7.956761],[-3.482752],[-3.685348],[-0.074121],[-0.997576],[-8.344989],[6.578719],[-0.578687],[2.143330],[-6.167599],[7.601220],[-5.001821],[8.544959],[-7.844001],[2.567776],[-4.516925],[-1.008136],[5.917651],[5.494778],[-0.742527],[-9.244605],[-3.112752],[-0.244894],[4.818690],[-6.955316],[-2.583316],[-6.888990],[-7.766822],[3.784055],[-7.659060],[-7.484255],[-6.916398],[-6.718099],[2.830966],[-0.014550],[9.679922],[-3.749146],[-3.120971],[8.922247],[-8.343066],[1.600621],[1.250838],[-7.120928],[1.008728],[5.138440],[-9.733960],[1.575843],[-3.924578],[-1.555538],[6.094493],[-5.571530],[-7.351954],[-7.837997],[5.698762],[-7.670937],[0.843860],[-9.933411],[6.015499],[9.992460],[2.026047],[6.516334],[-7.784591],[-5.193557],[-7.103616],[-7.070499],[6.108511],[-3.358832],[2.555502],[3.232903],[-9.488698],[2.078342],[5.652548],[0.424734],[-1.340372],[-7.069494],[4.916159],[1.072019],[-0.150534],[-4.312247],[-2.308508],[-9.132664],[1.844225],[5.504605],[5.175256],[-9.213971],[-2.384433],[4.039320],[7.360958],[6.964920],[8.347118],[8.267580],[9.183939],[-9.381373],[6.594693],[-5.002569],[1.876788],[1.674566],[8.527496],[-3.851169],[3.864494],[0.703082],[-6.765680],[-9.264397],[3.323995],[2.835759],[9.403022],[2.967062],[4.271044],[-2.499156],[-2.511780],[-7.769057],[6.685201],[6.834783],[4.270892],[8.394514],[-5.449403],[-0.465852],[4.377167],[-8.333280],[-1.151901],[-3.772879],[3.891763],[-3.584471],[3.574114],[3.704894],[7.109454],[-6.957123],[9.656648],[-0.800969],[3.327020],[-6.991858],[-2.977800],[-7.767179],[8.454482],[-8.104495],[-6.848457],[9.044949],[-6.217813],[-2.413455],[-0.390128],[3.529777],[2.126334],[-6.098486],[9.781599],[7.909312],[-3.086402],[-0.532903],[2.313696],[-6.199429],[-8.144109],[-3.292644],[5.236955],[-4.381005],[-0.750105],[-3.862126],[-8.888047],[-5.838168],[4.831347],[-0.653446],[8.644206],[6.225035],[9.082137],[-7.560934],[-5.087747],[5.774971],[3.880893],[1.083833],[5.438929],[-2.227787],[-8.714387],[-6.821365],[5.219843],[-1.077152],[0.891508],[4.228414],[3.788186],[-4.178982],[9.786917],[5.137435],[-1.551883],[-0.641692],[-8.253728],[-3.206434],[5.161109],[8.368232],[8.685373],[-5.951214],[6.178972],[8.574874],[1.064514],[8.437253],[1.141844],[-2.635232],[0.285489],[-6.490360],[-7.738000],[4.544248],[-7.020604],[2.090517],[4.641735],[0.187748],[-5.489358],[0.774040],[3.440472],[6.893896],[0.934792],[6.987797],[-0.486464],[6.927384],[0.543082],[5.942133],[-1.897329],[-1.734015],[3.199029],[-0.470233],[0.899269],[2.619385],[6.067737],[2.637406],[-6.400691]], dtype = "float32")#candidate|3458|(2240, 1)|const|float32
call_3457 = relay.TupleGetItem(func_2021_call(relay.reshape(const_3458.astype('float32'), [16, 10, 14]), relay.reshape(const_3458.astype('float32'), [16, 10, 14]), ), 0)
call_3459 = relay.TupleGetItem(func_2024_call(relay.reshape(const_3458.astype('float32'), [16, 10, 14]), relay.reshape(const_3458.astype('float32'), [16, 10, 14]), ), 0)
output = relay.Tuple([call_3432,const_3437,var_3438,const_3439,bop_3445,call_3457,const_3458,])
output2 = relay.Tuple([call_3433,const_3437,var_3438,const_3439,bop_3448,call_3459,const_3458,])
func_3463 = relay.Function([var_3438,], output)
mod['func_3463'] = func_3463
mod = relay.transform.InferType()(mod)
var_3464 = relay.var("var_3464", dtype = "float32", shape = (4, 108))#candidate|3464|(4, 108)|var|float32
output = func_3463(var_3464)
func_3465 = relay.Function([var_3464], output)
mutated_mod['func_3465'] = func_3465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_3477 = relay.TupleGetItem(func_3147_call(), 0)
call_3478 = relay.TupleGetItem(func_3149_call(), 0)
uop_3488 = relay.asin(call_3477.astype('float64')) # shape=(3, 12, 3)
uop_3490 = relay.asin(call_3478.astype('float64')) # shape=(3, 12, 3)
output = relay.Tuple([uop_3488,])
output2 = relay.Tuple([uop_3490,])
func_3508 = relay.Function([], output)
mod['func_3508'] = func_3508
mod = relay.transform.InferType()(mod)
mutated_mod['func_3508'] = func_3508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mutated_mod.get_global_var('func_3508')
call_3509 = func_3508_call()
output = call_3509
func_3510 = relay.Function([], output)
mutated_mod['func_3510'] = func_3510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3408_call = mod.get_global_var('func_3408')
func_3409_call = mutated_mod.get_global_var('func_3409')
call_3516 = func_3408_call()
call_3517 = func_3408_call()
uop_3520 = relay.log(call_3516.astype('float64')) # shape=(3, 12, 3)
uop_3522 = relay.log(call_3517.astype('float64')) # shape=(3, 12, 3)
output = uop_3520
output2 = uop_3522
func_3525 = relay.Function([], output)
mod['func_3525'] = func_3525
mod = relay.transform.InferType()(mod)
mutated_mod['func_3525'] = func_3525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3525_call = mutated_mod.get_global_var('func_3525')
call_3526 = func_3525_call()
output = call_3526
func_3527 = relay.Function([], output)
mutated_mod['func_3527'] = func_3527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_3551 = relay.TupleGetItem(func_3508_call(), 0)
call_3552 = relay.TupleGetItem(func_3510_call(), 0)
func_1303_call = mod.get_global_var('func_1303')
func_1307_call = mutated_mod.get_global_var('func_1307')
const_3554 = relay.const([-7,-3,-9,-7,2,5,-3,10,-3,-8,-10,7,-8,10,-10,-3,5,-3,-9,-5,8,-5,-2,-5,-3,-10,-3,-9,-7,-2,-9,6,-4,-10,-7,-6,-4,-6,-7,5,-3,10,-1,6,9,5,-4,4,9,-1,-9,-3,-9,9,-1,5,-9,-9,-6,-8,-4,5,-7,-6,-2,-5,7,4,-9,1,9,-4,-2,9,-8,5,2,-2,10,7,8,-3,-2,-10,-9,-10,8,7,9,-10,-4,10,6,7,9,-7,6,1,-4,10,3,-4,-8,-3,-10,3,-9,-2,-5,8,-4,1,5,-9,-5,6,3,-9,2,5,4,-6,10,-7,-8,9,1,2,-5,7,-4,-8,-3,-5,8,7,-7,-6,-10,4,-9,9,-6,-6,-4,1,-3,4,-5,-1,8,-6,10,5,-8,-9,3,-8,9,-10,-6,10,9,7,2,6,7,-6,-7,-8,-8,-1,-5,2,3,-6,2,-2,1,-4,9,-2,3,5,6,6,-10,-9,-5,8,2,1,-1,6,2,4,1,8,-3,7,-8,-5,9,5,4,6,-9,-1,-7,2,-8,-1,-2,6,-1,7,5,8,-8,2,6,8,-4,-6,6,10,-6,-5,-9,-6,-4,-2,4,5,-4,-4,2,6,10,8,-1,10,-1,-6,5,-3,-4,10,-4,10,9,-10,5,-8,9,-3,-6,8,9,8,-5,-5,-5,-6,9,8,-9,10,4,1,5,4,6,-9,-7,8,-7,10,7,2,2,-3,-6,-7,2,4,1,-1,1,1,-6,-9,-2,-4,4,7,5,9,5,-4,3,6,-7,10,-8,3,9,-6,10,2,-7,-10,-10,-6,6,-4,9,2,1,-3,2,-3,-9,-4,1,2,6,2,2,3,-9,6,8,-5,1,-8,-5,6,9,10,-7,-8,4,-8,-8,-4,-9,7,10,8,10,-6,4,7,-3,3,-1,10,-1,-4,3,-7,10,-2,6,2,6,2,-2,-5,-8,-5,-9,4,5,-8,6,3,-9,-4,4,2,-6,4,-3,-4,-7,-10,6,-6,-10,1,10,-9,8,-4,3,-4,10,8,-9,6,3,-4,-8,10,-7,-5,5,-5,-1,-7,7,-3,1,4,-8,-8,4,10,4,-1,2,-9,-2,-2,-5,5,-10,1,-2,3,-3,10,5,-1,-3,2,-2,4,5,-7,5,-2,-2,8,8,-5,4,-10,7,-10,8,6,2,4,-6,-8,4,-7,3,-2,1,-3,3,4,7,-10,5,-4,6,4,10,-4,-4,-3,-8,-9,4,-2,5,9,-1,8,-5,-4,-2,-2,2,7,6,-2,-4,-1,-1,5,2,-10,3,10,-2,-8,3,-5,5,-1,-1,-5,-2,-3,-3,10,4,-8,-10,6,3,4,-3,10,-2,-1,2,10,-6,6,3,5,-8,8,-3,7,8,9,4,-1,10,1,-10,5,-6,-7,7,-8,-9,2,-1,-8,-2,-10,8,-3,3,-8,5,-3,4,-9,4,-7,-6,-4,8,3,9,-4,-3,5,1,3,9,-6,-3,-6,-4,9,2,4,5,1,9,3,2,-1,3,8,7,-5,-9,-9,-3,-3,-4,-6,4,-7,5,-6,9,-2], dtype = "int8")#candidate|3554|(600,)|const|int8
call_3553 = relay.TupleGetItem(func_1303_call(relay.reshape(const_3554.astype('int8'), [10, 4, 15]), relay.reshape(const_3554.astype('int8'), [10, 4, 15]), ), 0)
call_3555 = relay.TupleGetItem(func_1307_call(relay.reshape(const_3554.astype('int8'), [10, 4, 15]), relay.reshape(const_3554.astype('int8'), [10, 4, 15]), ), 0)
output = relay.Tuple([call_3551,call_3553,const_3554,])
output2 = relay.Tuple([call_3552,call_3555,const_3554,])
func_3567 = relay.Function([], output)
mod['func_3567'] = func_3567
mod = relay.transform.InferType()(mod)
mutated_mod['func_3567'] = func_3567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3567_call = mutated_mod.get_global_var('func_3567')
call_3568 = func_3567_call()
output = call_3568
func_3569 = relay.Function([], output)
mutated_mod['func_3569'] = func_3569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3573 = relay.var("var_3573", dtype = "uint64", shape = (10, 3, 4))#candidate|3573|(10, 3, 4)|var|uint64
var_3574 = relay.var("var_3574", dtype = "uint64", shape = (10, 3, 4))#candidate|3574|(10, 3, 4)|var|uint64
bop_3575 = relay.greater_equal(var_3573.astype('bool'), relay.reshape(var_3574.astype('bool'), relay.shape_of(var_3573))) # shape=(10, 3, 4)
func_2976_call = mod.get_global_var('func_2976')
func_2979_call = mutated_mod.get_global_var('func_2979')
const_3582 = relay.const([[3.893914,-4.144346],[5.549210,-1.827188],[5.276409,7.670009],[4.607532,-9.041913],[-2.836211,-7.606176],[-1.183351,6.120939],[-7.230809,-0.330215],[-4.335785,-8.812521],[-9.105919,-7.314937],[5.542121,9.085749],[3.644661,-8.767033],[3.896427,6.642968],[-9.504522,6.674844],[-9.319871,-3.302454],[-9.159752,6.428424],[0.829478,-7.484055],[-2.547986,4.527032],[8.949140,9.497209],[3.029371,-5.459628],[-9.077302,-6.827488],[4.201413,0.345322],[-3.939070,-1.475179],[-8.789861,1.445369],[9.194801,-5.737124],[3.290250,-5.580767],[-5.779981,5.728832],[3.436151,-1.683618],[-6.051693,-8.241591],[0.372988,9.582554],[-3.756524,-3.057486],[9.116346,-5.137864],[6.344528,-1.453151],[-4.644347,2.320984],[-0.789572,0.584070],[-4.009034,-5.197235],[-5.480073,-7.132401],[-2.635278,-5.827769],[-1.611113,-1.230495],[-7.431656,-0.396164],[9.948327,-2.388616],[8.684709,-1.024992],[4.156481,2.682591],[-7.601182,-6.024046],[3.604792,-0.886199],[-7.944390,-9.509113],[5.670580,-9.694981],[0.247761,3.908793],[7.029478,-4.404957],[3.435261,6.623529],[-0.253588,2.412586],[-8.329381,-0.770831],[-9.155251,4.735639]], dtype = "float64")#candidate|3582|(52, 2)|const|float64
const_3583 = relay.const([-3.011482,-1.904720,8.846884,-9.559786,-6.305342,5.321907,-8.890394,-7.824846,-9.960896,5.709185,8.674746,-9.587220,-2.032596,-1.025582,1.361352,-1.829637,9.177319,8.031564,-6.368759,5.106503,-4.743147,-3.918630,4.548104,-1.503290,-0.399291,-4.565257,5.001710,-3.593209,6.596535,4.961775,-2.443768,-6.002901,-5.517022,-8.367271,-1.332361,0.938456,9.298628,1.474869,-5.475050,-9.525147,0.886194,-2.079678,6.365877,-1.905758,9.507095,1.171251,3.244308,1.388239,9.973386,-2.993244,-9.583328,-0.891853,4.882252,-8.136265,1.862253,7.547236,-7.781619,3.332330,-2.206077,-6.491703,8.651379,4.644094,2.256983,2.332762,0.204136,-4.644091,1.595122,8.276482,-5.831969,0.447507,-1.590277,-1.625325,-6.731006,-5.325134,7.843724,0.288388,-7.849170,0.751577,6.651822,-9.983284,-1.498660,-0.449670,6.686811,1.485700,-4.015275,-1.524420,5.046917,7.580136,-3.028758,-1.069421,-7.007546,5.603366,-5.025516,-6.084073,8.326126,-5.748321,-4.687177,2.421916,-0.879156,6.541861,2.146566,5.641721,4.265143,5.568370,-1.498610,1.251205,7.540720,2.131519,-2.484111,1.029919,-4.059580,3.097523,5.212925,3.586196,4.258979,-2.604386,-9.155625,2.802287,-2.787877,0.303122,-0.149054,3.706258,3.139485,-6.260895,-4.199576,2.654681,7.876962,1.263945,-9.318852,7.231091,-0.921804,-5.131367,9.485012,-4.260954,-2.525565,7.226313,-1.983456,-3.676133,6.698664,1.758339,8.273643,3.015919,-2.022996,7.320783,3.897698,-5.067858,-2.164261,-8.196427,1.629106,0.047513,-7.329020,-7.853193,5.548593,7.375075,3.898524,-2.240786,4.437639,-0.382553,9.920077,-6.084829,-5.798662,-7.674439,-6.553113,-3.093344,4.741366,5.996284,-3.036861,-9.240577,9.793689,3.841850,0.238173,1.488240,2.057311,-3.587051,8.043447,4.359686,0.378965,-3.216441,-1.479292,6.033695,-1.376182,3.090558,9.793826,-1.697722,8.312265,9.227113,3.640526,-3.436535,-1.334760,7.476098,8.419115,3.404014,-5.230351,-0.573914,8.542499,-1.814474,3.286436,-0.626368,-2.946032,4.712606,-3.508751,-3.208614,1.534197,-2.196948,3.538272,4.735969,-5.127972,6.133235,-5.541735,4.129461,-9.075237,5.076618,-4.975888,-8.645452,-8.959716,-2.211783,-4.058326,-9.186078,6.010531,-9.293320,3.060903,-6.830504,-1.188302,-0.962782,2.470393,-9.035357,-2.188876,5.001423,-5.158117,3.296524,2.847398,4.674987,-3.130893,4.832210,3.762784,-7.275674,7.251847,-0.819409,-1.605508,-3.154481,0.092216,6.598138,-8.073327,-2.177100,-6.968189,6.612548,5.662171,-8.405846,5.667898,-7.008090,8.847012,3.698395,8.655323,-8.139934,-8.720074,7.651839,-1.969003,7.258359,-4.959377,6.762613,8.291261,-6.661056,2.590267,-9.525434,5.914966,6.048479,8.024642,4.240596,6.246749,8.547320,3.511642,3.122756,3.962867,-4.251370,-2.236847,7.650872,3.914016,-1.199901,-1.958825,6.919191,3.264134,-3.948303,6.311863,2.330623,3.087713,-1.702852,-1.115966,-8.511636,3.376237,8.292708,-3.394040,6.127270,-4.433839,9.998291,7.049148,-0.555422,7.250120,6.592488,5.641820,0.095990,2.345422,5.815701,9.759661,-9.204512,-9.143858,-6.596016,-0.475193,-6.538688,-5.171835,5.893366,-0.847973,-4.911406,-3.028583,-1.862703,7.897380,-9.886316,-5.391576,-3.566412,-0.635793,-7.621055,-5.447049,9.729681,-5.823125,8.844432,3.214330,-7.859364,7.289112,-2.835294,2.693363,6.582806,-5.856828,4.884150,0.768778,2.060030,-6.850078,-5.555078,-0.508053,4.038716,-4.391345,1.220052,9.103034,3.078574,7.648311,-5.180544,3.519783,7.255969,-6.662101,-1.489765,-2.146909,2.019345,3.135283,6.737720,2.381417,-8.166688,2.321410,-3.235764,-0.679384,5.028882,7.735112,-1.678842,6.710323,-9.865909,-5.473800,4.591748,-2.013457,-9.163529,3.226089,-0.143982,-0.988865,-5.087699,-4.776556,0.277890,-6.520804,-3.211131,-9.938732,-5.742355,-0.545204,8.263532,8.029904,0.332196,5.217290,4.434060,5.672401,-8.481173,1.179987,-2.668589,0.087018,-2.469059,-4.726482,4.186571,7.265653,2.785530,-9.047783,-4.399845,8.116375,-1.415528,3.120587,0.789493,2.033122,2.637949,-1.527716,-5.273108,1.349367,-6.688914,-0.025227,-0.876729,8.966677,9.405882,7.251696,-1.814432,-6.347089,3.430962,-2.289009,-7.165167,-5.263065,-0.005064,3.864651,-5.962470,8.016903,2.784112,-5.206954,0.053042,4.691978,-1.021776,8.536271,2.606699,0.288874,2.870466,-6.019669,2.247305,1.310464,7.612281,-5.995256,9.007515,-9.358733,4.554162,9.499367,5.672554,-8.847157,3.327037,-2.497481,0.062255,6.272845,7.950993,-9.890746,5.419240,9.654649,4.763681,-6.897988,4.873158,8.432634,-4.259735,-1.579092,1.512350,7.011754,-8.424111,0.474843,0.964810,-2.492795,-4.530443,6.395184,7.297609,5.159421,-4.243517,5.150328,-0.336796,2.612906,8.965889,-7.998330,-0.554860,8.345840,2.186518,-7.786591,-7.346132,-1.790037,9.327571,-2.543800,-8.134569,5.098713,2.315655,-7.600524,6.989665,-1.633608,7.762316,6.496778,-5.918824,-6.155314,-7.832103,-4.920725,-2.630356,1.150417,-7.794201,-4.904382,7.649109,-7.654062,-0.409703,5.385158,-6.387595,8.988107,-3.559876,8.757428,6.690057,3.691983,-3.908312,-4.638322,-3.941664,-2.353904,7.547981,6.915728,6.272085,-8.929629,-0.483484,2.775193,3.537109,5.632956,-4.845357,7.587532,-0.569046,3.560115,-4.449033,4.185619,8.983250,-7.676127,-8.435542,-3.991869,1.924546,-1.212399,-7.155326,-3.826820,-9.263594,1.874308,-7.911269,-8.967315,7.113611,1.668105,-6.799095,-1.388859,-6.930613,-8.789757,-3.960378,-0.928482,6.199345,-4.272356,9.136156,-2.319196,-7.701538,-5.809132,-1.342643,3.464525,-0.757488,4.105797,-7.245209,-7.784788,-2.573530,1.475386,8.217055,-2.700842,-4.437093,-5.044164,3.082448,1.918805,5.422163,-6.184379,5.099591,3.704242,-1.999457,-2.736385,8.186304,-3.763881,8.388563,-1.642574,5.350642,-2.243162,9.136356,2.640362,8.970476,-3.780247,-5.004413,-9.517690,1.583326,8.125265,-9.306128,-9.888472,9.870207,-6.201897,-6.813429,8.117950,4.231142,-3.633883,6.100923,-1.457062,-6.956912,3.580412,0.619901,-5.171411,9.674947,7.221372,0.827171,4.572167,-8.182217,-9.667737,3.558239,-7.743578,0.955050,5.462756,9.908380,4.412165,0.400263,-0.679026,-8.789427,3.159539,3.975053,1.388120,-9.774054,5.229898,-2.888388,8.932094,5.202493,8.804690,-3.016957,2.902716,-4.424945,-4.085109,6.623142,-7.112220,6.121954,-6.676057,-8.692756,-7.088303,-1.196007,6.114363,1.414356,-3.652326,1.357720,0.711218,0.933350,6.562201,7.519667,0.880939,-6.344566,-8.054878,7.799877,-0.344179,-6.052638,-3.770672,-8.922414,-6.441508,-7.375802,3.147414,-0.142474,-8.113504,1.039692,7.263958,3.526327,-0.511562,-8.352911,0.791000,9.954784,-5.908586,-3.572099,-2.966955,-1.779177,-0.412416,-0.866326,-8.588401,-6.881709,-0.945265,-9.128094,-7.737142,-5.319871,-0.453904,5.735519,-0.383995,9.640685,9.925201,6.872379,7.040660,-5.893359,-1.840051,9.077594,5.261211,5.540514,1.768571,1.781876,9.468270,-7.503620,-9.757789,-8.287976,-3.257316,0.742993,3.127864,-8.149002,5.692061,9.368838,4.162745,-5.583402,-2.522192,-7.070874,-3.739739,-6.473089,7.585620,2.485774,-6.336779,-3.322969,7.713510,-8.880036,-0.014195,2.513708,4.928566,9.649061,7.641676,1.058846,-1.113567,-6.746605,1.033445,-2.580264,3.664822,6.251675,2.896257,8.472597,9.943047,-1.306463,-6.331700,1.115778,-9.920478,-7.273730,7.422365,4.890390,7.405029,-9.948340,-2.916876,0.463548,-0.607791,-3.463069,-4.065879,-4.937565,7.833052,0.815986,4.348155,-5.213427,6.537604,8.583794,-7.793222,-0.448619,-2.307286,1.120669,-8.694464,3.850717,4.408837,-0.556772,6.024877,7.811511,6.883373,-9.358361,-6.925723,-9.452643,1.683269,-4.460210,8.925688,5.759760,9.190111,-5.089587,1.622555,-1.223301,0.237839,-5.986089,3.674562,-0.781788,-6.214472,8.947506,9.226617,-3.995203,-7.291498,-1.962633,-8.865701,7.604286,-0.151094,6.747176,5.326103,-8.866405,-4.510247,1.809076,7.392733,7.539751,-0.318100,-9.476509,-1.087124,-2.333609,4.173297,-0.748205,-2.318489,7.191421,-3.662867,-1.421058,-0.715315,-0.289352,2.492393,-1.157210,4.624561,-3.425001,7.962230,9.755840,-0.454978,-0.577399,4.375787,6.693513,-1.883339,-4.165944,1.574210,4.605388,-0.662468,-8.896306,0.489575,-5.682164,-2.878326,2.252963,8.865608,-5.880562,-2.234858,0.297268,7.372785,-0.689728,8.142611,-0.411712,8.946374,-2.270638,-0.541360,-3.498177,1.710189,-3.518208,7.214671,1.414440,0.021676,-3.658422,-0.759710,6.146070,-1.181004,-9.262357,-0.329124,-0.287104,-4.794272,6.088224,-0.162498,-2.904544,-9.090395,5.787426,-3.274438,-4.598968,-5.963167,-0.533925,-0.138488,8.223975,2.649056,-3.689075,-6.812562,9.380476,4.085205,6.205683,-6.675787,-0.679855,0.524537,9.035377,-2.115803,0.664418,-5.980385,-9.818223,8.955288,-7.020287,2.833325,-9.545481,5.421124,-6.417320,9.602921,-4.460085,9.839221,-8.513653,9.422753,4.718392,-4.469166,-0.541317,-8.542899,0.393194,-7.866691,-9.792920,3.879416,-4.593516,-9.472354,4.762077,-5.579949,-7.161893,-6.538587,-9.194892,-5.827455,-9.772122,-7.449061,7.693443,9.548072,-2.704362,-5.148377,8.380113,-8.136816,8.128076,-2.701314,-9.336395,-7.118880,-9.513440,7.426574,-1.190621,-7.254393,-0.972159,-8.460439,4.122199,9.506796,1.076298,-1.734095,5.892091,-8.380106,-5.404567,7.677325,-6.472753,8.504703,5.483330,1.220252,-2.975194,-4.837921,5.385143,-1.510926,-0.790714,-3.916679,-7.987740,-2.941758,4.967192,-0.889528,7.222628,-5.868156,6.653984,-3.503059,1.898929,5.028778,-6.523503,-4.345811,-3.391828,-0.008794,-9.408587,-4.732917,-8.294478,-7.199583,-9.908475,3.754131,7.960764,9.610881,8.414070,2.406760,7.642650,-0.197707,-5.757971,0.519612,5.944084,2.576978,5.958566,-5.898049,-1.854102,5.752154,8.726659,-9.133946,2.945644,-5.494529,3.086404,0.404846,-1.484456,-6.427544,-4.114352,4.657058,-9.300183,-0.882839,-9.954362,7.252084,5.760320,1.662554,8.605333,9.557159,5.409877,3.133780,7.108934,-7.866157,-5.923566,-4.051018,-9.523489,-8.820015,-2.048150,-2.169155,-2.800849,4.565212,9.020245,-6.621077,-4.545447,2.459494,3.374555,7.444910,6.118990,-0.247612,-5.910910,-8.773987,-6.167565,0.306324,8.220047,-5.251402,9.742488,-4.710971,-8.663541,6.150120,-4.002325,1.495194,3.090058,3.512304,-2.852002,-3.412480,-0.685678,7.282129,-8.752094,-7.860012,7.555988,1.707579,-6.075945,2.761947,-4.116818,-9.268810,6.283959,2.403121,-3.364760,9.983107,-7.808174,1.830480,-8.223524,-8.700493,-0.044523,8.261246,2.702403,-1.929270,-5.633119,-4.348718,5.255033,6.750894,-8.615563,2.490131,3.069918,8.375610,6.207112,2.127007,-4.230843,-3.569335,-1.913395,-6.470500,-5.775935,8.699531,-6.278303,5.240053,-6.073125,-1.745566,4.401333,4.677964,-3.340543,8.978655,-1.644685,8.428712,-7.540364,8.643695,1.657124,-3.360653,-4.041148,-6.542155,8.705414,-9.335942,0.121380,0.170364,5.123482,9.765151,6.755412,6.796545,7.393855,-1.060093,-0.920963,-3.099069,9.808895,0.230678,9.003018,-9.424471,4.044047,-1.127417,5.656618,-9.006980,9.046990,-0.187873,-7.566503,-8.352969,5.526526,3.416433,-6.938491,1.429235,-4.047503,2.009414,5.505034,-7.335947,0.761622,2.478678,-0.011186,2.867096,5.097557,7.767122,9.304569,-1.751365,-3.123526,-4.366590,0.238430,6.401105,-9.812231,8.304613,-6.729673,-8.778426,1.927340,3.272975,7.340748,4.514136,-9.254171,-2.492679,-1.593648,-9.860480,-2.148235,7.600913,4.393736,8.988186,1.344474,9.235513,6.304046,1.336801,3.469691,-2.397727,5.621998,0.048245,-8.497782,9.390814,-9.263665,-6.018860,-4.681026,7.269386,-2.086614,9.721612,8.212597,9.312841,8.242030,2.502567,4.287362,8.408923,3.917129,5.004676,4.664589,-0.988306,-2.980081,-9.697539,-2.914458,-3.682445,9.786430,5.850900,-2.496379,6.530164,0.096219,-4.200838,-8.566322,-3.478631,0.205643,-4.492038,-4.824603,-9.338914,4.178711,-7.124589,-8.977329,-0.598919,-4.632204,5.116376,-7.353794,-4.142391,0.003393,2.345090,6.238662,-0.686383,9.534900,6.960459,9.615438,-3.409026,-2.521527,4.618192,-1.599475,-2.668056,4.419995,6.119932,-7.070020,6.631586,7.855220,-0.549931,-4.468326,0.835778,8.057797,-5.390511,-1.938536,2.924830,8.725541,-2.337514,-9.181309,-3.756071,-0.825321,8.296446,-3.810370,-2.241078,1.388737,-4.933145,1.260480,3.768452,-4.765617,-9.556038,9.601772,7.828535,-1.033825,-0.692328,5.100448,-4.351217,-9.460403,-0.444205,-8.128953,-5.116525,8.149381,-5.020265,-5.660043,3.996128,6.120039,-4.006442,8.357737,5.990325,3.257174,-4.330233,-7.870488,-7.940060,8.682547,4.390019,8.401878,3.403429,-8.072290,-7.416119,-7.206356,1.301510,2.897359,-4.041339,-3.053281,-6.171265,8.098318,-8.224685,1.677901,-6.233246,2.391054,-1.797751,-0.053386,-2.396414,1.820693,5.921731,-3.511711,3.772650,-3.148817,7.659781,6.032641,-5.921148,-8.468892,6.754309,9.739853,-8.016538,2.787948,-9.410676,6.173711,1.477881,2.098380,-5.786769,0.890520,1.787911,6.198935,-3.907479,-5.422257,9.061670,4.264566,-4.780304,-2.846420,-9.707717,9.299193,5.920049,5.855377,-5.710882,-6.915510,-7.823892,-7.395803,9.562005,-7.251869,6.578646,8.213198,-7.740444,2.742364,5.330251,4.989814,8.144099,-6.804362,1.459294,1.776642,-3.114672,-7.844116,-1.148270,-2.086593,-4.976075,0.144761,4.695455,-2.685341,-6.938285,-1.992021,-1.280132,4.520624,3.390625,-9.711110,9.158362,-1.980211,7.531600,-9.122905,8.339199,-1.079742,-3.040564,0.769187,-0.340240,0.501958,5.722093,-2.415973,8.753229,-2.221333,-9.834328,-6.515310,-1.352898,5.813015,4.671621,7.347004,2.436306,4.119684,-6.458748,1.954244,-4.964379,2.548041,8.800945,0.696308,0.832417,5.314465,9.244948,1.344497,-7.599870,8.173781,-5.334039,-8.967352,-7.502103,5.873306,4.856517,1.160923,7.621872,8.992242,7.651056,-3.171131,-0.364985,-9.812169,4.277869,-4.467793,-6.117452,3.997905,-5.749768,-2.503211,6.361142,0.992902,2.476144,4.066422,1.341426,9.469538,4.068371,2.975720,4.415300,9.397051,7.203300,-6.648170,-8.796745,0.424672,9.127928,8.343865,1.946907,9.024120,-3.198048,-6.141790,-7.802127,-9.961528,5.898756,2.012803,2.446411,1.781134,-0.033033,-8.984719,0.614030,-5.730713,-1.646381,-8.381032,-2.731066,-7.567801,-5.342286,6.978162,-0.099624,-3.655032,7.506784,-7.741292,2.018489,-3.022434,5.415902,-0.218695,-0.697405,8.588155,-8.425695,-1.503413,-7.561686,9.975358,8.449772,4.399775,-8.513860,1.429758,0.139762,-8.171915,1.277109,4.004734,-2.761624,-0.810881,-7.549323,7.688907,8.292573,2.791510,-6.227392,-9.108379,7.281360,6.000845,6.558357,-6.542587,-5.185536,0.157733,6.056982,-2.638801,-5.166962,-6.946899,-9.969094,-3.631565,5.683152,6.339274,-3.076536,-2.029439,3.646894,-4.386556,-7.158795,-1.407353,6.454987,4.099621,-8.710355,-2.082663,-1.384260,0.209824,-4.385815,-2.267820,9.209062,8.521735,9.528796,-6.650948,6.646118,8.308165,2.066465,-0.133302,-3.228956,3.146833,9.641246,2.171236,-3.927911,0.954335,-7.559670,-8.300372,7.228325,-0.238563,7.217156,-9.698252,7.417109,9.205775,8.430577,0.322619,1.648733,-3.557637,2.830661,-6.079777,-0.382348,-4.558928,8.856154,-8.090509,1.927702,3.661251,2.407927,0.491994,4.390748,5.585443,1.256682,-0.085197,6.552679,2.185866,5.146154,-0.504558,1.962818,-0.612460,-1.483233,-2.177051,5.794445,-0.503383,9.586203,3.919288,-9.569628,5.968537,-4.271002,-5.239319,-3.863423,-5.651589,6.094530,8.326070,6.446001,8.968592,-9.705866,3.381803,7.191196,1.108997,-3.108080,-7.104062,5.742661,-5.827232,8.278370,-2.643173,-1.637364,8.776844,6.486321,7.707658,3.139321,-3.823102,-8.037060,7.350412,-6.169414,-5.836618,-3.726711,4.066921,-8.131137,1.990285,4.894706,4.412868,-4.451274,1.172571,9.543652,-0.774025,-6.424236,-8.432474,8.652726,-4.802054,-5.096427,-3.027814,4.047797,9.006474,1.481245,-2.887666,-2.780863,-0.036174,-6.887518,-9.349601,-5.134346,-1.537847,-1.916703,8.398647,7.575598,9.131420,-0.950577,-7.163644,5.270694,8.846062,-1.691426,9.591956,1.223165,8.301976,-2.142512,8.541085,-6.524003,0.430003,4.525057,-6.041017,-3.048633,-6.829523,9.469002,7.238273,-1.372502,4.435863,-2.366039,4.467190,9.753028,2.265498,5.908811,-2.287511,9.473293,-9.774848,8.041634,9.025107,-6.916465,-7.004643,-8.635505,-2.318955,2.004987,5.096882,7.258185,8.607134,4.119732,-0.658731,-5.603363,-1.490688,-4.586494,-6.559565,-8.847089,9.577890,4.331662,-9.958439,2.527517,6.510596,0.195347,-1.336888,5.571458,3.050307,8.773658,5.236293,-6.922133,9.367301,-4.872153,-7.952585,4.914730,8.052264,-3.545831,-4.883537,2.945275,-4.980167,-2.825366,2.938206,-1.991607,-8.616515,-9.322996,8.008846,6.839130,3.929533,-3.673404,-7.804678,4.733715,3.560739,-6.964694,-8.336840,5.693234,-9.493451,7.865952,2.331351], dtype = "float64")#candidate|3583|(1664,)|const|float64
call_3581 = func_2976_call(relay.reshape(const_3582.astype('float64'), [1, 8, 13]), relay.reshape(const_3583.astype('float64'), [16, 8, 13]), )
call_3584 = func_2976_call(relay.reshape(const_3582.astype('float64'), [1, 8, 13]), relay.reshape(const_3583.astype('float64'), [16, 8, 13]), )
output = relay.Tuple([bop_3575,call_3581,const_3582,const_3583,])
output2 = relay.Tuple([bop_3575,call_3584,const_3582,const_3583,])
func_3593 = relay.Function([var_3573,var_3574,], output)
mod['func_3593'] = func_3593
mod = relay.transform.InferType()(mod)
mutated_mod['func_3593'] = func_3593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3593_call = mutated_mod.get_global_var('func_3593')
var_3595 = relay.var("var_3595", dtype = "uint64", shape = (10, 3, 4))#candidate|3595|(10, 3, 4)|var|uint64
var_3596 = relay.var("var_3596", dtype = "uint64", shape = (10, 3, 4))#candidate|3596|(10, 3, 4)|var|uint64
call_3594 = func_3593_call(var_3595,var_3596,)
output = call_3594
func_3597 = relay.Function([var_3595,var_3596,], output)
mutated_mod['func_3597'] = func_3597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3608 = relay.TupleGetItem(func_3129_call(), 0)
call_3609 = relay.TupleGetItem(func_3131_call(), 0)
func_2361_call = mod.get_global_var('func_2361')
func_2364_call = mutated_mod.get_global_var('func_2364')
const_3617 = relay.const([2.494680,9.669145,5.432929,-9.627822,4.521635,-9.023707,9.568759,6.705806,3.361436,-0.288884,4.691858,-6.077266,-6.220527,-4.427855,-2.478099,4.543244,4.578566,-8.371259,6.140062,8.085899,3.135420,4.295969,4.696773,-6.265155,-6.539763,3.915783,5.159847,4.991270,4.858705,2.252270,1.669918,-2.176482,5.765207,2.777578,3.629606,-3.704838,1.796662,8.872385,-6.367681,6.300459,-0.263022,-7.069893,1.192341,6.378543,3.578505,-4.025475,-6.339796,6.473588,3.319274,-3.947417,7.448638,-8.768751,2.173982,2.831385,0.430507,-9.420539,-8.187236,9.525008,-1.658155,-0.554603,-9.391195,8.530848,7.345773,-5.580213,6.164975,0.044557,0.191160,0.786638,3.524557,-3.383025,-0.915503,-8.314423,8.894294,-1.325286,8.035837,7.958711,8.911880,-5.342796,9.532964,6.397902,6.363901,0.238976,-4.220395,6.969352,-9.638815,2.440655,-2.625257,1.069004,6.078480,-4.473093,-9.690899], dtype = "float64")#candidate|3617|(91,)|const|float64
var_3618 = relay.var("var_3618", dtype = "float64", shape = (270,))#candidate|3618|(270,)|var|float64
call_3616 = relay.TupleGetItem(func_2361_call(relay.reshape(const_3617.astype('float64'), [1, 13, 7]), relay.reshape(var_3618.astype('float64'), [270, 1]), ), 0)
call_3619 = relay.TupleGetItem(func_2364_call(relay.reshape(const_3617.astype('float64'), [1, 13, 7]), relay.reshape(var_3618.astype('float64'), [270, 1]), ), 0)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3622 = relay.TupleGetItem(func_3129_call(), 1)
call_3623 = relay.TupleGetItem(func_3131_call(), 1)
output = relay.Tuple([call_3608,call_3616,const_3617,var_3618,call_3622,])
output2 = relay.Tuple([call_3609,call_3619,const_3617,var_3618,call_3623,])
func_3624 = relay.Function([var_3618,], output)
mod['func_3624'] = func_3624
mod = relay.transform.InferType()(mod)
var_3625 = relay.var("var_3625", dtype = "float64", shape = (270,))#candidate|3625|(270,)|var|float64
output = func_3624(var_3625)
func_3626 = relay.Function([var_3625], output)
mutated_mod['func_3626'] = func_3626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3567_call = mod.get_global_var('func_3567')
func_3569_call = mutated_mod.get_global_var('func_3569')
call_3633 = relay.TupleGetItem(func_3567_call(), 2)
call_3634 = relay.TupleGetItem(func_3569_call(), 2)
func_3525_call = mod.get_global_var('func_3525')
func_3527_call = mutated_mod.get_global_var('func_3527')
call_3646 = func_3525_call()
call_3647 = func_3525_call()
func_568_call = mod.get_global_var('func_568')
func_571_call = mutated_mod.get_global_var('func_571')
const_3653 = relay.const([[-5.969307,-4.211684,8.476593,3.950513,-6.048795,-2.623224,-3.319400,0.003065,9.397264,-7.601118,-9.083356,-7.894022,-5.999873,7.604630,-7.571175,-6.615680,2.041818,2.250281,-0.510232,3.898067,7.309609,2.635607,-8.947448,2.345414,2.464946,-1.861653,-7.742566,-8.507413,-2.942622,3.529046,-4.474667,-4.260325,-7.304246,-7.157782,-2.991122,-7.606600,1.396313,3.652223,-7.976419,-0.229417,-1.010319,9.042214,3.020187,9.967185,4.972033],[6.024700,-9.451621,-5.600242,9.578344,-2.537658,-5.533115,7.747084,-4.174033,3.268165,0.838889,-7.850695,3.955475,-4.037489,4.418337,-3.953868,5.025225,-8.418401,4.070927,-1.541555,2.703268,-9.409890,8.947744,-1.332492,-4.151799,6.532097,7.008673,7.773342,8.562388,6.253612,-4.484071,-9.619995,5.657449,5.427993,8.231369,9.520070,-4.791946,-2.657981,-9.689656,-1.024225,9.573432,-3.955169,7.702641,5.751844,-4.331902,-8.528001],[-4.877674,-0.732091,9.606799,6.135360,1.666387,-9.534098,-2.693356,-0.933942,8.667686,-6.203021,-1.469117,5.978151,-5.757247,-1.005473,3.609216,3.356886,3.090728,-3.566340,-7.016109,5.903881,-6.799594,1.597800,3.865876,2.658688,-2.267833,0.978439,4.428083,1.886662,0.101566,-6.383193,-5.033612,-3.655681,9.271564,-0.533349,-0.006756,6.962499,3.025735,-9.753416,-9.630416,3.256238,6.609335,7.157059,5.982554,-8.732739,0.622839],[-1.846145,3.735248,0.386853,0.591871,-9.125274,-5.232514,-6.773541,-5.220640,-7.189815,8.113850,-1.678560,-4.781009,4.463414,-4.452875,-5.643937,-5.482336,3.398653,8.254202,-6.377216,-6.687852,9.760597,-6.588300,2.144596,-3.686593,-6.370511,0.160226,-2.956963,-5.032638,-8.975943,7.495602,-2.619304,7.553954,1.333692,5.064868,0.628585,-1.567601,-9.607017,-8.568681,-6.796509,1.394568,-5.562838,0.378951,-6.403052,-3.108876,-8.753651],[4.886611,8.430585,-2.740759,3.209865,-3.648740,7.333706,1.843986,-5.824198,5.538513,-6.882443,6.952893,-4.150578,6.445238,-9.347972,3.181675,-7.064852,-1.929842,3.186963,-5.774467,-4.872661,5.393523,-5.479250,3.677738,-5.941039,6.081956,6.482579,-1.740520,2.581816,-9.741298,2.307430,-0.251786,-9.232222,-6.782679,8.618892,-3.150020,9.931106,9.920657,2.489744,-2.614677,-6.629978,-2.182113,-3.091722,1.264833,3.440307,-6.329765],[5.946609,-0.179175,2.708616,5.761415,6.183971,-1.369859,8.631976,-7.695021,-9.060554,-6.968757,-1.740277,-3.531810,1.105701,-8.061489,4.880365,-8.884735,8.071332,-1.285802,6.628263,8.500160,8.169268,7.711191,-5.855787,3.502700,8.166124,4.712070,5.793389,-9.096166,9.872913,6.484690,1.130276,1.992773,-6.830674,3.740115,6.871039,-5.797174,-3.021800,6.295142,-2.270115,2.237490,-5.052011,5.971340,-2.787213,8.797957,9.188729]], dtype = "float64")#candidate|3653|(6, 45)|const|float64
call_3652 = func_568_call(relay.reshape(const_3653.astype('float64'), [15, 3, 6]), relay.reshape(const_3653.astype('float64'), [15, 3, 6]), )
call_3654 = func_568_call(relay.reshape(const_3653.astype('float64'), [15, 3, 6]), relay.reshape(const_3653.astype('float64'), [15, 3, 6]), )
uop_3660 = relay.rsqrt(call_3633.astype('float64')) # shape=(600,)
uop_3662 = relay.rsqrt(call_3634.astype('float64')) # shape=(600,)
output = relay.Tuple([call_3646,call_3652,const_3653,uop_3660,])
output2 = relay.Tuple([call_3647,call_3654,const_3653,uop_3662,])
func_3664 = relay.Function([], output)
mod['func_3664'] = func_3664
mod = relay.transform.InferType()(mod)
mutated_mod['func_3664'] = func_3664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3664_call = mutated_mod.get_global_var('func_3664')
call_3665 = func_3664_call()
output = call_3665
func_3666 = relay.Function([], output)
mutated_mod['func_3666'] = func_3666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_3722 = relay.TupleGetItem(func_3147_call(), 0)
call_3723 = relay.TupleGetItem(func_3149_call(), 0)
func_2427_call = mod.get_global_var('func_2427')
func_2431_call = mutated_mod.get_global_var('func_2431')
const_3725 = relay.const([[1.800296],[5.880276],[-4.280519],[9.942477],[8.883549],[7.700767],[7.431067],[-3.473642],[-5.294137],[-7.879751],[5.059888],[-4.903157],[9.284441],[-2.834754],[-2.595517],[-9.762097],[6.424470],[-8.058658],[-5.092959],[-2.892353],[1.055151],[0.107669],[4.315144],[-6.034133],[-9.025756],[8.527249],[-5.638280],[-1.058958],[-7.393298],[7.263867],[8.065341],[-3.316739],[-9.502214],[-8.358587],[-2.902394],[-5.643552],[-3.589570],[-1.323076],[5.633915],[-0.019916],[9.302657],[-9.292804],[4.507621],[1.019521],[8.013965],[-7.075176],[-3.566032],[0.073601],[0.802522],[-0.562793],[-2.579969],[9.279086],[-6.218387],[-8.477051],[-5.493843],[-7.683004],[0.341952],[-6.282870],[2.755761],[-9.889944],[-5.208152],[4.109179],[5.486343],[8.423553],[-5.950285],[-9.643051],[4.521457],[4.380381],[0.489305],[1.094590],[-5.499136],[4.816495],[-8.959781],[-5.852583],[4.481158],[7.335933],[-5.672254],[1.034451],[4.304156],[-0.269945],[-5.748614],[2.075369],[2.092264],[9.699432],[-6.281794],[-1.472824],[-2.468520],[-5.393964],[7.283010],[-2.693772],[9.682730],[7.690343],[-5.484936],[2.145049],[5.713998],[3.533622],[-3.974013],[6.015650],[-2.502956],[-3.457161],[-5.737723],[1.215469],[-9.891148],[8.178540],[6.497646],[6.840393],[2.615973],[-7.529970],[0.575568],[-0.969471],[1.247657],[-4.093787],[-4.394182],[8.529222],[-4.113438],[3.669164],[9.759216],[-0.566909],[3.844211],[4.802250],[4.686191],[3.539352],[4.978216],[7.183134],[-7.023206],[-2.075081],[8.897445],[4.243728],[-3.371934],[-6.510023],[5.465008],[0.901430],[0.748144],[-2.132442],[-4.391398],[1.785335],[-6.380489],[-4.077153],[-6.343187],[-3.530828],[0.213252],[-6.843914],[4.141350],[-2.916888],[0.079039],[2.404118],[9.959369],[9.478769],[-4.165274],[2.992762],[3.473423],[-2.664771],[3.624730],[-1.070253],[-5.922912],[-5.473344],[3.126115],[5.891737],[3.471386],[-6.443654],[-0.226839],[6.242128],[8.144272],[-9.811680],[-8.594964],[-4.364526],[-6.799845],[-1.480936],[3.250006],[7.152729],[1.540683],[-6.077248],[1.703732],[-0.542117],[0.702641],[3.153303],[-9.731728],[9.926959],[8.266333],[5.237453],[1.878959],[7.192363],[-2.004969],[-5.899879],[-1.036387],[-7.967495],[8.461540],[-3.163507],[-0.276982],[1.784771],[-4.227096],[1.266547],[2.741191],[-7.878290],[2.995191],[4.186393],[3.987915],[-8.113175],[-5.598244],[3.717855],[3.577201],[-4.016427],[-8.215223],[0.101831],[7.896318],[8.276584],[7.145624],[-1.668911],[4.901859],[2.914924],[-7.189511],[-2.109232],[6.830675],[-5.252229],[0.821347],[9.404361],[6.426420],[4.630004],[-2.087272],[-5.825742],[-0.167353],[9.990559],[-1.111600],[-9.936348],[-6.802535],[-4.761532],[-7.138477],[-7.855892],[-1.485876],[3.503693],[9.477405],[-8.166916],[4.289860],[-7.601686],[-9.075507],[5.980140],[-7.224932],[-2.917704],[0.589352],[5.701655],[-9.646046],[-3.037377],[-4.918863],[-6.716776],[9.630330],[-3.824951],[-9.160591],[0.925101],[-7.156433],[-3.365080],[-3.893228],[5.951679],[-1.314413],[-4.503332],[3.864101],[-0.286674],[0.589085],[-4.515925],[8.079623],[-4.758127],[3.247337],[7.400338],[0.474221],[6.109748],[6.574316],[-6.029846],[5.638600],[-2.178226],[3.142123],[1.157106],[-5.639163],[-7.266484],[2.556346],[7.173275],[-7.557806],[9.807950],[-4.804504],[7.531408],[-5.184502],[-6.109293],[-6.724587],[8.504688],[-7.076613],[-5.444558],[-4.203073],[-8.220649],[7.513583],[1.348794],[-2.712593],[0.026284],[-7.055306],[-7.405978],[-1.369440],[8.501392],[-5.037410],[-2.379484],[-4.971566],[-5.298132],[2.653357],[9.851934],[6.941556],[1.746373],[-1.838965],[4.166157],[6.835328],[8.849730],[6.669405],[5.841689],[-3.075924],[-4.343363],[-9.057480],[5.484121],[3.152231],[7.857153],[-4.502977],[-0.833449],[2.806243],[-3.469532],[-8.814900],[-6.995521],[4.129670],[-7.150918],[7.859230],[-3.650402],[-9.540437],[-0.014311],[4.615145],[1.688157],[5.275332],[7.216573],[3.434890],[7.641981],[1.296445],[3.125584],[7.699224],[-3.296907],[4.140459],[-1.347246],[-5.325404],[-8.387328],[6.439436],[6.859607],[9.828288],[7.726291],[8.020792],[-1.318567],[5.655741],[4.536102],[-4.967013],[-3.879398],[-9.130752],[-3.579982],[1.226597],[-2.598365],[2.692605],[-4.542299],[6.780166],[6.885344],[7.339896],[-2.607666],[3.083040],[8.018421],[-1.894014],[-7.322254],[4.361708],[4.354483],[0.368493],[-6.534808],[-4.338930],[-6.936810],[3.033023],[-6.723207],[-3.324944],[5.108941],[7.942413],[-9.688566],[7.930238],[0.132631],[4.933193],[-9.906683],[-1.905733],[-3.155969],[8.981818],[0.076030],[-5.669362],[6.218415],[-4.588308],[-5.660562],[5.094167],[-0.757966],[3.501756],[8.069418],[1.241039],[9.088598],[-6.011606],[9.395294],[2.746799],[-3.141322],[-7.869702],[-5.351143],[5.171318],[2.017430],[9.440152],[-0.539948],[7.879876],[4.616678],[-8.842819],[8.797620],[6.870490],[-5.297377],[-1.991802],[0.649336],[6.739324],[-1.635142],[4.672571],[-5.255429],[-5.652195],[-2.041609],[-8.859854],[-9.929722],[-7.112996],[-3.447360],[2.608553],[-2.695445],[-8.692489],[-3.366938],[-5.228501],[-9.905570],[-4.629043],[-0.301421],[1.997674],[-1.113617]], dtype = "float32")#candidate|3725|(432, 1)|const|float32
var_3726 = relay.var("var_3726", dtype = "float64", shape = (378,))#candidate|3726|(378,)|var|float64
call_3724 = relay.TupleGetItem(func_2427_call(relay.reshape(const_3725.astype('float32'), [6, 8, 9]), relay.reshape(const_3725.astype('float32'), [6, 8, 9]), relay.reshape(var_3726.astype('float64'), [378,]), ), 0)
call_3727 = relay.TupleGetItem(func_2431_call(relay.reshape(const_3725.astype('float32'), [6, 8, 9]), relay.reshape(const_3725.astype('float32'), [6, 8, 9]), relay.reshape(var_3726.astype('float64'), [378,]), ), 0)
uop_3732 = relay.log(const_3725.astype('float32')) # shape=(432, 1)
output = relay.Tuple([call_3722,call_3724,var_3726,uop_3732,])
output2 = relay.Tuple([call_3723,call_3727,var_3726,uop_3732,])
func_3740 = relay.Function([var_3726,], output)
mod['func_3740'] = func_3740
mod = relay.transform.InferType()(mod)
mutated_mod['func_3740'] = func_3740
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3741 = relay.var("var_3741", dtype = "float64", shape = (378,))#candidate|3741|(378,)|var|float64
func_3740_call = mutated_mod.get_global_var('func_3740')
call_3742 = func_3740_call(var_3741)
output = call_3742
func_3743 = relay.Function([var_3741], output)
mutated_mod['func_3743'] = func_3743
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3760 = relay.const([[[-9.232823],[1.257492],[-1.093139],[4.377912],[4.433543],[-5.247825],[0.759536],[-2.129246],[-7.488120]],[[-8.013993],[-8.707129],[1.242789],[1.423462],[-2.224846],[-9.628462],[9.385043],[-2.694322],[7.616537]],[[-4.963930],[9.064425],[-4.002637],[-1.136755],[4.355051],[-1.409684],[-4.098183],[-3.428674],[3.381894]],[[4.009892],[-6.843810],[0.553441],[8.257812],[-1.555428],[2.644040],[-1.409555],[-5.479084],[0.788325]],[[-5.730288],[-1.917006],[-8.952967],[0.198200],[4.642113],[6.381804],[-0.449650],[5.056252],[-0.616627]],[[9.769089],[7.218015],[4.888193],[2.331335],[7.397204],[8.711779],[-6.813061],[-5.514862],[-4.296956]],[[6.518119],[4.801102],[0.652928],[2.189853],[6.403436],[-8.350835],[8.813298],[0.653541],[4.523590]],[[-0.879107],[2.900805],[-8.495576],[-5.221731],[-6.599220],[5.811756],[-0.698779],[-6.438603],[-8.349194]],[[-5.198159],[3.233908],[-8.536361],[-9.331877],[1.364873],[7.762547],[-4.258997],[8.788606],[8.996564]],[[0.369729],[3.711585],[-6.543655],[-0.176027],[3.470657],[4.093182],[-5.433972],[-3.051799],[1.980044]]], dtype = "float64")#candidate|3760|(10, 9, 1)|const|float64
uop_3761 = relay.sqrt(const_3760.astype('float64')) # shape=(10, 9, 1)
output = relay.Tuple([uop_3761,])
output2 = relay.Tuple([uop_3761,])
func_3771 = relay.Function([], output)
mod['func_3771'] = func_3771
mod = relay.transform.InferType()(mod)
mutated_mod['func_3771'] = func_3771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3771_call = mutated_mod.get_global_var('func_3771')
call_3772 = func_3771_call()
output = call_3772
func_3773 = relay.Function([], output)
mutated_mod['func_3773'] = func_3773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3408_call = mod.get_global_var('func_3408')
func_3409_call = mutated_mod.get_global_var('func_3409')
call_3794 = func_3408_call()
call_3795 = func_3408_call()
output = relay.Tuple([call_3794,])
output2 = relay.Tuple([call_3795,])
func_3796 = relay.Function([], output)
mod['func_3796'] = func_3796
mod = relay.transform.InferType()(mod)
mutated_mod['func_3796'] = func_3796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3796_call = mutated_mod.get_global_var('func_3796')
call_3797 = func_3796_call()
output = call_3797
func_3798 = relay.Function([], output)
mutated_mod['func_3798'] = func_3798
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3799 = relay.var("var_3799", dtype = "int16", shape = (12, 8, 9))#candidate|3799|(12, 8, 9)|var|int16
var_3800 = relay.var("var_3800", dtype = "int16", shape = (12, 8, 9))#candidate|3800|(12, 8, 9)|var|int16
bop_3801 = relay.greater(var_3799.astype('bool'), relay.reshape(var_3800.astype('bool'), relay.shape_of(var_3799))) # shape=(12, 8, 9)
uop_3818 = relay.sigmoid(var_3799.astype('float64')) # shape=(12, 8, 9)
func_2147_call = mod.get_global_var('func_2147')
func_2152_call = mutated_mod.get_global_var('func_2152')
var_3821 = relay.var("var_3821", dtype = "uint8", shape = (336,))#candidate|3821|(336,)|var|uint8
var_3822 = relay.var("var_3822", dtype = "float64", shape = (270,))#candidate|3822|(270,)|var|float64
const_3823 = relay.const(-0.727369, dtype = "float64")#candidate|3823|()|const|float64
call_3820 = relay.TupleGetItem(func_2147_call(relay.reshape(var_3821.astype('uint8'), [4, 14, 6]), relay.reshape(var_3821.astype('uint8'), [4, 14, 6]), relay.reshape(var_3822.astype('float64'), [30, 9]), relay.reshape(const_3823.astype('float64'), []), ), 4)
call_3824 = relay.TupleGetItem(func_2152_call(relay.reshape(var_3821.astype('uint8'), [4, 14, 6]), relay.reshape(var_3821.astype('uint8'), [4, 14, 6]), relay.reshape(var_3822.astype('float64'), [30, 9]), relay.reshape(const_3823.astype('float64'), []), ), 4)
output = relay.Tuple([bop_3801,uop_3818,call_3820,var_3821,var_3822,const_3823,])
output2 = relay.Tuple([bop_3801,uop_3818,call_3824,var_3821,var_3822,const_3823,])
func_3839 = relay.Function([var_3799,var_3800,var_3821,var_3822,], output)
mod['func_3839'] = func_3839
mod = relay.transform.InferType()(mod)
var_3840 = relay.var("var_3840", dtype = "int16", shape = (12, 8, 9))#candidate|3840|(12, 8, 9)|var|int16
var_3841 = relay.var("var_3841", dtype = "int16", shape = (12, 8, 9))#candidate|3841|(12, 8, 9)|var|int16
var_3842 = relay.var("var_3842", dtype = "uint8", shape = (336,))#candidate|3842|(336,)|var|uint8
var_3843 = relay.var("var_3843", dtype = "float64", shape = (270,))#candidate|3843|(270,)|var|float64
output = func_3839(var_3840,var_3841,var_3842,var_3843,)
func_3844 = relay.Function([var_3840,var_3841,var_3842,var_3843,], output)
mutated_mod['func_3844'] = func_3844
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3846 = relay.const([[[-5,5,4,-5,-6,-1,5,-9,5,10,2,1,2,-10],[8,-10,-8,10,5,-10,-10,5,9,6,9,1,7,-9],[2,7,-5,7,-4,-7,4,-1,-10,-2,10,6,5,-3],[1,-3,-3,-7,9,-4,-2,-3,-8,-3,-1,-1,2,-2],[-5,9,-9,1,3,2,1,-7,7,-9,4,-5,-6,8],[4,-5,5,2,-6,-5,10,-1,3,4,-9,5,3,-10],[6,7,10,-8,-5,8,-5,10,-10,6,10,3,1,3],[-8,4,-5,-6,2,9,-4,9,-9,5,-4,3,9,3],[4,5,-3,7,-10,10,-7,-9,5,8,-1,-5,4,-6],[4,6,-7,1,9,-7,-1,3,5,6,-2,-6,-9,-5],[-1,-7,-2,4,-3,-1,-2,-3,3,-8,-8,10,1,2],[-9,5,9,4,3,3,2,8,2,7,-9,-6,1,8],[4,-4,-8,2,8,-3,5,-7,-1,2,-8,1,-4,-4],[-4,7,-4,-2,9,-2,-3,10,-2,-6,-3,6,-7,-9]],[[-3,6,-7,7,5,4,5,-4,2,8,-2,8,-3,9],[3,-1,-2,6,-1,9,-2,1,-10,8,9,-5,-8,-6],[-7,-3,2,-7,-10,-4,-5,8,-9,-7,-3,10,-8,-3],[-5,-9,4,3,7,-2,2,-9,-2,-4,-5,-9,-5,10],[-3,-2,-2,3,5,3,7,-9,3,5,5,8,10,8],[-6,1,-1,-8,-3,8,6,-2,-9,1,10,-9,7,7],[-7,-5,3,-2,6,-7,2,1,-9,2,-3,-1,-1,8],[-2,-5,7,-3,5,-7,7,4,-3,9,5,1,-2,-8],[5,-1,8,5,8,-10,-3,-6,4,10,-4,-9,-8,-6],[5,5,2,4,-2,9,-6,4,7,8,1,-9,6,-3],[-10,-7,7,-4,8,10,6,-3,-8,2,7,5,9,-1],[1,1,7,6,-10,4,8,-1,1,9,-10,-5,2,-3],[5,5,-1,9,2,1,-6,3,9,2,-9,9,1,-4],[-5,3,-2,8,-3,-1,-2,9,9,4,8,-8,-7,6]],[[-3,1,7,10,2,-3,2,-10,-6,4,4,1,-6,-9],[-8,-10,-5,-8,7,-2,-5,4,8,-4,4,2,-10,10],[-4,8,5,-2,1,5,-10,-8,3,-2,5,-7,-8,7],[-2,3,-9,5,-6,-6,-6,6,-9,1,-6,3,3,-10],[-7,-8,-7,4,-9,-2,5,-4,1,9,6,-10,-4,-4],[2,-5,-5,7,-3,8,9,9,-9,7,4,-10,5,-5],[-2,6,-6,-3,6,-5,-9,3,4,-2,-4,3,-4,-2],[-2,9,-9,7,10,8,-10,-6,-5,-6,10,4,-4,4],[1,-8,3,8,-4,7,7,-1,8,3,-8,-6,7,-2],[8,-1,-10,-5,-8,-6,10,-8,9,-3,9,-2,-6,-5],[8,-4,-1,-9,-3,7,7,-4,5,3,1,2,-1,9],[3,-10,1,-1,-8,5,-5,5,-4,-9,10,6,8,-3],[4,-6,-6,-10,-2,-9,-1,4,-7,-8,-7,-3,-6,8],[6,-3,-3,-7,-7,6,-10,-10,9,7,-2,-10,-9,-3]],[[1,1,5,10,-4,7,-6,1,-9,-8,-4,6,-9,2],[-9,-5,8,-10,1,-1,8,6,-4,-9,7,-1,2,6],[4,-1,5,-5,-3,8,-4,-1,-8,8,4,-4,7,-4],[1,-10,8,-9,-9,-9,-9,8,-5,-10,6,6,-5,2],[4,-1,-6,1,4,8,-6,8,4,-1,-7,-4,6,4],[8,3,2,6,-5,-1,-9,-4,7,-10,-2,-10,3,3],[-3,3,4,3,10,-3,8,-5,2,10,3,-10,3,3],[3,-5,4,-8,-4,4,10,-8,-1,3,-2,5,-7,2],[5,5,-3,6,8,6,5,-5,-7,-1,-6,2,-9,5],[1,5,-3,6,1,-5,-8,-1,1,5,-9,-8,3,4],[6,10,-9,5,-5,9,-5,-7,7,3,5,8,6,-10],[-6,1,-8,-1,-7,-8,-7,10,-3,-2,-4,8,3,-5],[2,8,-2,9,-1,6,7,10,-2,4,7,8,1,1],[2,6,1,-3,4,-4,4,-5,-3,5,-5,-3,-4,-4]],[[-6,2,-2,5,2,-10,-10,3,2,5,3,5,8,10],[10,1,-10,-6,-1,10,9,-2,-2,-4,-3,4,-8,3],[6,2,-7,1,-5,-2,10,-2,1,7,-10,-10,10,6],[2,6,3,3,10,-7,-5,-3,-10,3,2,-5,-10,3],[10,10,1,1,5,-1,-1,1,-9,10,-3,1,2,-6],[-4,4,10,-7,1,4,5,2,4,-10,2,-2,-3,-10],[2,9,9,-1,9,-2,7,10,-9,-6,8,8,7,6],[-7,-5,6,-5,9,-6,2,-3,-1,-1,-5,-7,-4,-6],[-7,1,1,-10,-1,-2,9,-9,5,3,4,8,2,4],[-10,-7,3,8,-3,8,3,4,-9,6,6,-10,1,10],[3,9,4,-10,-3,8,-7,2,10,4,3,-3,-7,-9],[-3,4,-3,-9,9,4,8,-2,10,-8,1,10,-2,-3],[6,-9,-3,4,6,-4,5,-8,2,9,-5,-2,9,-2],[-3,-1,-1,7,-3,-9,-6,-5,3,-3,5,-6,-1,1]],[[-8,-2,-10,-3,3,-4,-3,-7,-7,8,-10,-4,-5,7],[9,-7,-1,-2,-9,-1,-5,1,9,6,2,6,7,7],[2,-9,2,-10,2,-3,6,-5,10,-8,-4,4,8,-6],[-2,6,-6,7,-10,2,-8,5,10,5,-6,6,-7,5],[-10,10,-5,8,-1,1,1,-3,8,-2,-8,8,-2,-3],[5,-4,-1,1,-3,7,-5,5,-2,4,6,8,-3,-7],[1,3,10,-4,-4,-6,5,10,2,3,-4,5,5,4],[-10,-4,-3,-10,6,3,-1,6,-2,4,-4,7,-6,-9],[-6,8,6,-8,8,-3,3,4,-4,-10,1,-10,10,4],[-2,8,6,5,-7,2,-2,-10,10,1,-6,-2,-4,1],[-2,2,10,3,6,-9,-2,10,3,-10,-4,8,-1,-9],[3,-1,-7,-10,-2,2,-10,3,-1,5,-3,-8,8,-8],[-8,-4,-7,7,-7,-2,1,-1,4,-4,-6,-10,6,5],[5,2,10,-4,10,-4,10,10,-9,-4,-4,9,-1,-9]],[[6,10,-9,3,-10,-10,-8,-9,-10,10,9,-4,4,5],[10,-2,-9,-6,-7,-2,7,7,-6,-2,5,-6,7,9],[3,7,-7,-10,1,9,-6,-7,2,-8,2,7,-3,-4],[-4,2,-7,9,-5,-2,-6,8,-3,4,-9,-6,-2,8],[7,-6,3,6,-6,-3,5,-9,10,2,-2,-9,-1,-10],[9,10,10,-4,-3,-2,-7,-10,-4,-3,6,-8,-4,-9],[-3,9,7,-5,-5,-1,-1,-5,-9,9,4,10,9,-10],[6,-9,-6,-10,-8,-1,7,-1,-4,5,3,-9,-7,-9],[-8,1,-6,-2,9,-9,-10,-9,-2,-3,7,2,-3,-7],[1,-7,4,-2,6,-7,9,-1,-6,-3,-1,7,-6,9],[3,8,-1,2,2,-8,-1,5,-10,-6,-9,7,9,9],[4,-3,-4,-10,7,-2,9,7,-6,-9,-9,5,5,-9],[7,-10,-5,-9,-5,6,2,-10,10,10,-2,-4,-3,10],[-4,-4,6,-3,8,-2,2,4,-5,-6,4,1,-4,-6]],[[6,9,-4,1,9,-2,10,2,1,-6,2,9,8,1],[-7,-3,4,2,-6,-7,1,-4,5,-2,3,3,10,3],[-6,-3,3,5,-7,5,-4,-10,6,-7,-1,-9,7,-4],[-6,8,-3,-4,-9,6,-7,-1,3,-5,7,-10,-1,5],[-1,-6,5,-8,6,-7,-10,-1,1,-8,-3,-5,-7,1],[4,-7,-4,-3,-8,7,4,9,4,10,1,-2,-1,9],[2,7,5,-2,-6,7,-7,-7,8,-2,5,-10,10,-5],[10,10,-1,9,-10,4,-7,9,5,2,2,-8,8,5],[3,-10,3,7,10,1,-9,5,6,-10,9,-4,8,2],[-1,3,-9,7,6,8,-9,5,6,4,3,2,-5,-7],[-10,8,-5,5,7,-8,3,-10,-4,2,4,-1,1,-3],[2,1,8,-1,-2,7,-8,4,-10,6,9,6,-6,-2],[-2,5,-4,4,-8,5,3,9,8,3,-8,-3,-8,2],[-8,3,1,4,8,7,4,6,-7,-9,10,4,4,7]],[[-8,6,-3,-8,10,-10,-9,-2,3,10,-5,-5,-2,5],[6,-8,10,2,4,8,1,10,-4,-1,-2,-7,2,4],[-10,-10,10,3,-1,-3,-5,10,-8,-4,-5,-1,7,-6],[1,3,-10,8,-2,-1,-3,9,-7,6,1,2,-6,-5],[-3,2,-4,5,-9,-3,1,-3,10,4,2,5,-9,-1],[1,10,8,8,-10,-3,6,-9,2,3,7,-9,7,-4],[10,5,-1,5,-8,9,-8,6,-2,10,8,-4,-1,6],[7,-8,3,-8,6,-4,-10,2,-9,1,3,3,-5,6],[2,-5,2,-7,7,-1,-1,-7,8,-9,8,-6,1,2],[-8,3,-2,10,4,-1,5,3,-7,-8,-2,1,7,10],[-9,-6,-3,-1,-7,-1,8,-1,-5,10,-5,-6,5,6],[7,10,8,-6,-4,8,-6,4,2,-9,-8,-9,-5,-9],[-4,-2,10,-8,-9,9,-9,-5,-5,-1,4,6,-8,4],[-1,6,9,6,-2,-8,-9,4,-6,-5,10,2,7,-6]],[[2,-10,5,6,-4,5,-9,8,-2,5,1,-2,7,7],[-9,-1,-2,-4,7,-3,4,-8,1,-2,8,2,9,-2],[-6,-2,-1,6,4,-2,-1,3,-5,8,-8,-10,10,-6],[5,-5,9,8,10,3,5,6,-2,-1,9,4,2,4],[5,-10,1,1,-5,-8,-4,-1,-8,-5,6,-9,7,-4],[5,-8,-9,-1,4,-8,3,-5,9,-6,-3,-7,-6,5],[8,-10,-7,-3,9,-9,-6,-3,5,5,-6,-10,1,9],[4,9,-1,-4,1,9,3,-4,-4,-7,-7,-2,-3,-3],[10,2,-3,-5,-1,-7,8,4,-1,-8,7,4,10,-8],[-6,7,-2,9,1,-2,-3,-7,-4,-10,-9,-1,-6,2],[-1,-10,3,5,6,3,-6,-10,-3,-9,7,-3,10,3],[-9,3,-9,-6,-10,-10,-5,-4,7,9,10,-8,-7,-3],[4,-2,-3,2,-8,8,1,4,2,-6,-1,-10,5,10],[-10,-7,-9,9,6,5,2,-1,1,9,-3,-4,-2,-7]],[[-4,-8,-10,-3,6,10,-5,-7,10,4,-3,-7,-9,-3],[5,9,7,-6,-4,5,-2,3,1,8,8,-3,4,9],[10,6,4,-7,-3,-7,3,-9,6,-4,-2,8,-2,-4],[2,-10,5,-8,-1,1,9,3,1,-6,-3,-6,3,-6],[-7,-1,-4,-1,-9,10,-5,8,-9,5,2,-9,-2,-10],[10,-9,-6,4,-5,1,-4,-8,1,3,6,4,-1,-2],[9,-9,-2,4,1,10,-4,10,1,9,3,-6,1,-8],[2,-7,-4,7,-5,3,-2,-1,-5,4,-10,-10,4,3],[-5,-10,-1,-5,3,2,-7,-5,-10,-5,1,1,-4,-6],[8,-6,10,-9,4,7,-7,7,-6,5,1,10,-1,3],[3,-4,1,-1,5,-4,-5,-6,10,8,-8,-9,-5,8],[10,-9,-5,4,-4,-6,7,8,9,-4,-1,-4,-7,5],[3,-8,-9,8,2,7,-6,-5,-3,5,-10,4,3,-10],[2,-2,1,10,9,-1,7,-8,-2,-6,-7,8,9,-9]]], dtype = "int32")#candidate|3846|(11, 14, 14)|const|int32
const_3847 = relay.const([[[8,-10,-8,4,-5,9,-2,-9,-7,4,9,-7,9,1],[-5,10,10,6,-8,-7,3,6,-8,6,8,-7,10,-10],[-10,-8,5,-8,-10,2,7,1,-7,5,4,1,1,-10],[3,-9,10,-10,5,-1,4,-3,7,9,2,9,5,-7],[9,-9,-9,7,-6,-6,7,-8,-3,10,-6,3,-4,4],[-4,8,-10,6,-3,-9,-2,-10,2,-7,-10,6,7,5],[-2,1,-4,9,-5,-3,2,7,-7,-2,-6,8,10,-3],[-1,-10,-9,-1,9,-5,7,-3,2,-2,1,-1,-4,5],[1,1,-6,7,2,-6,-7,7,1,-2,4,-3,1,3],[3,9,8,7,3,-7,3,-9,-8,-6,-8,3,6,6],[2,-3,9,-10,-4,-9,3,3,3,8,-8,-10,5,-8],[-9,-6,-4,-5,-1,-8,-4,-3,4,2,-9,9,-5,6],[10,10,-6,10,7,3,-2,4,-9,-2,-6,2,-5,7],[-10,1,-4,-9,9,-2,-7,-4,-7,5,-9,3,-1,1]],[[8,9,10,5,-1,4,-6,-8,-1,-3,5,6,-7,7],[6,8,-7,-9,5,1,-10,9,1,-2,2,-5,-5,8],[2,4,5,-9,6,-9,3,8,5,3,5,-2,-1,3],[-8,10,6,7,3,-4,-5,10,3,3,-5,5,2,-8],[-4,10,2,1,3,9,-3,7,-8,-6,-6,8,-7,-5],[10,-3,2,6,3,-2,-5,-4,-4,8,9,2,5,9],[4,-3,5,1,-9,-3,-4,1,-8,10,8,-5,-2,-2],[-8,10,-5,10,-9,1,-10,10,-3,-5,-6,2,-5,-10],[-5,-3,-3,9,-6,-2,-10,2,-9,-3,-3,-1,5,2],[-4,6,-5,4,-4,8,2,6,2,3,10,4,-6,4],[-2,-1,9,8,10,3,-5,-3,-2,-2,-7,-8,10,-2],[-8,-8,-3,9,-8,-5,8,-2,9,-3,-6,-7,-7,4],[6,-4,4,-9,2,-8,-4,9,-3,9,10,-4,7,1],[-4,-3,-3,-9,8,-4,5,-1,7,2,-2,-1,-5,1]],[[6,-5,-9,5,5,8,9,2,-6,-4,4,2,-9,10],[-9,5,3,8,-8,3,-4,-7,-5,-8,1,-3,-9,2],[-7,1,1,1,-6,5,1,-7,1,9,-2,-6,-10,9],[3,7,-2,-5,-4,9,7,-6,-4,-3,-7,-2,9,4],[-6,-9,4,8,-6,-1,1,-2,3,-7,1,1,-2,8],[10,1,5,-2,9,5,3,8,5,4,-10,-5,3,-10],[1,-6,-10,-7,-8,3,1,3,-5,1,2,6,-8,-4],[8,-4,10,2,-9,-6,-1,4,-9,7,-9,4,4,5],[2,3,-1,-1,-8,-2,1,4,9,4,-7,3,-1,-9],[-8,9,2,-2,-10,8,5,7,-10,-9,-10,-8,-4,-5],[8,10,-8,8,10,5,-4,-9,4,6,-8,-2,8,7],[1,-8,6,6,8,4,-5,-9,-3,-9,-6,-1,-10,5],[5,1,-4,6,9,-3,-8,-5,7,2,-4,-9,6,5],[4,-7,1,-6,8,-4,6,4,-6,6,6,-5,9,-3]],[[5,2,-9,8,-8,5,-8,3,-8,-7,9,-2,-1,5],[3,6,5,7,8,4,-2,2,-9,4,-5,4,6,6],[2,-1,9,-3,7,8,5,-3,-10,7,-1,7,-5,9],[6,1,9,5,9,-4,-9,-4,-6,-3,4,-6,-4,3],[3,-1,9,8,-5,-8,4,5,-8,-10,-5,-9,-5,-6],[-7,6,-2,8,2,1,-3,-4,-3,-10,7,3,1,3],[-8,-2,-9,-4,9,10,10,-9,-10,-9,1,4,-9,1],[3,-5,4,-4,10,-2,2,8,-5,6,-9,10,6,9],[-3,3,-6,-6,10,5,-10,6,-3,3,-3,-5,5,2],[9,5,2,9,10,2,7,-9,4,-6,-2,-5,9,-7],[5,-6,-1,-8,2,-4,-5,2,2,9,-7,-5,6,-3],[-9,-1,-8,-9,-1,3,-8,-6,1,-5,7,1,8,10],[5,1,4,8,-1,2,-4,5,-1,-5,7,7,5,-8],[3,7,3,-2,1,8,7,-6,-4,4,-2,-10,-10,-2]],[[5,6,-10,-8,2,-8,1,7,-6,8,-1,-7,-3,1],[4,-6,5,-8,8,8,9,-5,1,-8,-2,-9,1,6],[-3,-7,4,5,-7,6,3,5,9,-2,-1,-9,9,6],[6,-5,-10,-3,6,-6,2,-8,6,-7,-5,-7,-1,7],[-6,1,-6,-10,-9,-1,-2,-9,8,9,3,9,7,4],[4,-8,-6,-4,-7,7,7,2,6,6,-1,8,-1,1],[4,-5,-9,-9,-2,-5,9,-5,-3,-8,10,-5,-8,-2],[9,-8,1,1,4,6,5,5,5,-2,6,-9,1,5],[6,-10,-5,10,-10,7,-3,10,-4,1,4,2,-3,-6],[5,-6,1,8,2,3,10,-6,4,-8,10,10,5,3],[2,-2,1,10,4,9,9,-8,3,-10,3,-7,-9,8],[-8,-2,10,-9,-2,4,-10,-1,-6,-6,6,-8,-3,-1],[-2,8,10,2,4,3,-2,-1,10,1,-3,-9,-2,8],[-1,-10,2,3,-8,3,6,-7,3,-3,1,2,-1,-5]],[[-5,-10,5,-1,8,8,9,-7,9,7,1,6,-4,-8],[-7,-9,5,1,9,-7,-6,-4,-8,3,-4,-9,10,9],[-4,-10,9,7,9,5,2,7,-9,-4,-4,4,9,5],[9,-5,10,-5,-9,2,-10,7,9,9,-7,-6,-2,-8],[-6,-10,8,7,5,4,6,-1,5,8,4,-3,-2,3],[-1,-3,-6,1,2,-2,2,10,-4,-4,-1,-2,-10,7],[5,-6,-2,3,-3,4,2,4,-3,-4,5,5,-10,2],[-3,-2,10,-7,8,-4,4,-8,-5,-2,7,3,-2,10],[5,-4,1,-9,5,-7,3,3,9,-4,4,-3,10,2],[4,5,-4,-2,-4,-9,-4,-9,-6,-6,4,1,8,10],[10,1,4,7,-3,-6,-7,-6,-9,-2,9,-2,-10,2],[7,-5,4,4,1,7,-8,3,-7,-8,5,-3,-10,7],[10,-7,1,-5,-7,4,-8,-4,-5,-4,5,9,4,4],[7,-3,1,3,1,1,-6,-5,-8,-3,-3,5,2,10]],[[8,-1,3,1,3,10,-3,-1,-5,-5,3,-6,-6,-6],[7,-6,10,-9,3,-9,-5,2,9,6,10,-7,-9,1],[3,4,5,-4,-9,-10,-4,-9,-7,6,-4,9,2,-9],[6,6,9,-1,10,-1,-10,-1,9,5,3,-1,-4,3],[6,-6,-3,-4,-2,9,2,-5,1,9,8,-4,-7,-1],[5,6,-7,-6,7,-3,4,-3,1,1,3,-10,5,-3],[-10,3,8,9,-2,-6,-2,9,10,-2,-9,-1,-4,5],[-6,2,-5,-1,4,10,4,6,4,2,7,-5,9,-3],[8,2,10,-7,-7,-10,8,-9,-6,8,10,6,-8,-6],[-6,9,6,-7,3,1,-4,-3,1,-7,-4,-8,7,-2],[4,1,6,5,1,-10,10,6,-2,-8,-8,-1,2,-9],[-3,5,8,9,-5,-7,8,1,-1,-2,6,8,-7,-8],[-8,9,7,-1,9,10,4,-2,-7,10,2,10,4,-3],[7,-1,8,8,-3,10,-9,-9,2,-5,6,6,9,-5]],[[-6,-5,10,9,5,3,6,-3,-6,8,-2,6,10,8],[-1,-6,1,-3,-9,-9,2,4,7,-3,-8,10,5,9],[-1,-7,-10,-3,-6,4,-9,-2,6,8,-5,-6,-1,-4],[6,2,-2,2,-3,7,-1,7,-5,-10,-4,4,-9,-2],[-1,-7,-4,4,9,10,-1,3,7,2,6,-2,-10,10],[1,10,-10,6,-7,8,8,-7,-4,-3,-8,-2,6,-5],[-4,-6,6,-6,-4,-8,5,-4,-5,-4,-1,1,-1,-4],[-9,-3,-3,-10,6,5,8,-8,3,-8,3,9,-8,-5],[-3,5,-7,9,-9,1,2,-5,3,-5,-5,5,4,4],[-6,10,8,-5,6,-7,10,-2,5,-5,1,3,3,-4],[3,9,-6,1,4,9,8,7,-3,10,-8,-6,-5,5],[-10,4,-8,5,2,2,-1,-8,-6,-9,-5,8,-6,-2],[-5,10,7,-9,9,-3,-9,6,5,-1,8,1,-8,9],[-5,-6,10,-4,-2,-6,-6,-1,-3,6,-9,-10,-6,-2]],[[-1,-8,-2,5,-10,10,3,-2,-2,-5,-8,-4,8,5],[4,8,-6,10,-1,-9,3,3,-5,4,-8,4,-1,-4],[-10,-3,-8,-10,7,4,6,-9,5,6,6,7,10,-1],[-8,10,-6,4,3,-8,-5,-10,-6,-1,-10,-8,6,2],[5,-7,-8,4,-9,6,4,2,-6,2,1,2,-8,-2],[6,-2,-9,7,-5,3,-9,6,5,-5,-2,3,-8,-7],[-5,-3,-6,3,4,-5,9,3,-9,1,6,-6,-3,-2],[-4,-9,1,-2,-9,-4,-5,1,9,1,-2,-3,-8,-7],[-10,2,-1,4,5,10,-1,8,-3,9,3,-1,2,-3],[5,-3,-10,-8,8,-4,-6,-8,9,10,-4,-4,-8,-2],[-1,5,5,-10,5,-8,9,-7,-6,-1,-10,7,-1,1],[-7,2,-7,3,-4,-9,-10,1,8,-4,2,9,8,6],[-6,1,-7,9,-1,-8,-5,6,-3,-3,-7,-5,-2,-3],[-10,-10,-5,8,-3,7,-9,-8,9,10,-3,3,1,8]],[[-4,-6,9,9,-6,-5,-5,-2,7,-1,-6,-10,-7,6],[3,-3,-7,1,4,10,-8,8,9,-10,-2,5,-3,6],[10,-7,-7,9,-1,10,2,-7,4,6,7,-2,-10,-6],[3,-2,-3,-5,-1,-4,7,-8,-3,3,-10,3,-6,6],[-5,8,4,3,1,8,4,-4,8,-4,-9,-10,-6,8],[-1,10,7,-4,-10,-10,4,-2,-2,3,-10,-2,-4,8],[7,-3,-10,-4,3,-10,4,-3,-8,1,3,1,-9,-2],[7,-4,-8,5,-10,-7,-9,-5,8,5,4,7,8,-1],[-3,1,-3,-4,-1,-8,-10,-5,3,5,-9,9,-4,1],[8,-2,-4,-1,-9,-7,6,3,-2,6,-10,1,9,5],[10,-7,9,-7,4,2,-5,-4,-6,-6,5,8,-2,7],[8,-7,1,5,5,2,4,-1,-3,-9,-1,-9,-6,4],[-3,9,4,-2,-10,-4,10,2,-10,-2,-9,-3,-3,-7],[-9,-7,3,-6,10,1,-6,4,-2,10,9,-8,3,9]],[[4,-7,8,-7,-1,-9,2,2,-6,4,3,4,7,10],[-3,-10,-6,2,-2,-8,-4,8,6,4,6,-2,3,1],[-7,-2,4,7,-8,6,8,4,1,-7,-2,1,-8,-7],[8,-1,-2,5,-4,6,9,-3,-5,8,9,-5,6,-8],[-8,5,4,-10,8,2,6,-5,9,-4,3,4,-7,2],[2,8,-7,-5,9,-7,1,-1,7,-3,-2,-5,-1,10],[6,3,-3,8,-4,-1,8,-9,9,-7,-8,5,9,8],[10,2,-9,6,6,10,-8,-2,-10,5,-5,-6,-3,2],[2,4,5,10,10,3,-1,-5,-5,5,-2,-5,-5,7],[-1,-1,-8,-8,10,-6,-3,8,6,-3,2,6,-10,-10],[-9,2,7,-6,-8,-7,-2,1,-6,9,2,-10,-10,8],[-7,-5,-7,-8,-8,-9,-9,-5,3,-6,2,-10,-7,-9],[-9,9,9,-2,-8,-1,7,3,10,6,-3,-2,-6,-1],[3,2,-9,7,2,4,-10,-6,-7,-2,6,-10,-8,6]]], dtype = "int32")#candidate|3847|(11, 14, 14)|const|int32
bop_3848 = relay.logical_xor(const_3846.astype('int32'), relay.reshape(const_3847.astype('int32'), relay.shape_of(const_3846))) # shape=(11, 14, 14)
func_3593_call = mod.get_global_var('func_3593')
func_3597_call = mutated_mod.get_global_var('func_3597')
const_3853 = relay.const([4,-1,-4,2,2,-10,9,-9,-6,3,4,-1,-1,10,4,5,7,2,3,-1,4,-5,-1,-1,-7,10,-6,-4,-3,-6,-8,-2,-7,10,8,6,5,6,8,-6,-2,6,-7,-6,5,-5,2,-1,4,8,-3,6,6,5,-9,-8,-7,-8,5,3,5,4,-7,-6,-4,-5,-9,-6,-4,8,2,-4,-10,-3,8,4,6,-1,-1,-4,-1,4,9,-6,1,-6,-10,3,-3,-3,-2,4,-5,1,-2,-4,3,5,-8,-6,-3,-3,3,2,-2,-6,-4,-2,-5,-8,9,10,-10,5,3,8,-6,-10,-8,-4], dtype = "uint64")#candidate|3853|(120,)|const|uint64
call_3852 = relay.TupleGetItem(func_3593_call(relay.reshape(const_3853.astype('uint64'), [10, 3, 4]), relay.reshape(const_3853.astype('uint64'), [10, 3, 4]), ), 2)
call_3854 = relay.TupleGetItem(func_3597_call(relay.reshape(const_3853.astype('uint64'), [10, 3, 4]), relay.reshape(const_3853.astype('uint64'), [10, 3, 4]), ), 2)
output = relay.Tuple([bop_3848,call_3852,const_3853,])
output2 = relay.Tuple([bop_3848,call_3854,const_3853,])
func_3860 = relay.Function([], output)
mod['func_3860'] = func_3860
mod = relay.transform.InferType()(mod)
mutated_mod['func_3860'] = func_3860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3860_call = mutated_mod.get_global_var('func_3860')
call_3861 = func_3860_call()
output = call_3861
func_3862 = relay.Function([], output)
mutated_mod['func_3862'] = func_3862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_3878 = relay.TupleGetItem(func_3147_call(), 0)
call_3879 = relay.TupleGetItem(func_3149_call(), 0)
func_3664_call = mod.get_global_var('func_3664')
func_3666_call = mutated_mod.get_global_var('func_3666')
call_3880 = relay.TupleGetItem(func_3664_call(), 3)
call_3881 = relay.TupleGetItem(func_3666_call(), 3)
var_3889 = relay.var("var_3889", dtype = "float32", shape = (3, 12, 3))#candidate|3889|(3, 12, 3)|var|float32
bop_3890 = relay.maximum(call_3878.astype('int16'), relay.reshape(var_3889.astype('int16'), relay.shape_of(call_3878))) # shape=(3, 12, 3)
bop_3893 = relay.maximum(call_3879.astype('int16'), relay.reshape(var_3889.astype('int16'), relay.shape_of(call_3879))) # shape=(3, 12, 3)
output = relay.Tuple([call_3880,bop_3890,])
output2 = relay.Tuple([call_3881,bop_3893,])
func_3911 = relay.Function([var_3889,], output)
mod['func_3911'] = func_3911
mod = relay.transform.InferType()(mod)
mutated_mod['func_3911'] = func_3911
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3912 = relay.var("var_3912", dtype = "float32", shape = (3, 12, 3))#candidate|3912|(3, 12, 3)|var|float32
func_3911_call = mutated_mod.get_global_var('func_3911')
call_3913 = func_3911_call(var_3912)
output = call_3913
func_3914 = relay.Function([var_3912], output)
mutated_mod['func_3914'] = func_3914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_3951 = relay.TupleGetItem(func_3508_call(), 0)
call_3952 = relay.TupleGetItem(func_3510_call(), 0)
func_1735_call = mod.get_global_var('func_1735')
func_1738_call = mutated_mod.get_global_var('func_1738')
var_3957 = relay.var("var_3957", dtype = "int32", shape = (630,))#candidate|3957|(630,)|var|int32
call_3956 = relay.TupleGetItem(func_1735_call(relay.reshape(var_3957.astype('int32'), [9, 7, 10])), 0)
call_3958 = relay.TupleGetItem(func_1738_call(relay.reshape(var_3957.astype('int32'), [9, 7, 10])), 0)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_3969 = relay.TupleGetItem(func_3147_call(), 0)
call_3970 = relay.TupleGetItem(func_3149_call(), 0)
output = relay.Tuple([call_3951,call_3956,var_3957,call_3969,])
output2 = relay.Tuple([call_3952,call_3958,var_3957,call_3970,])
func_3972 = relay.Function([var_3957,], output)
mod['func_3972'] = func_3972
mod = relay.transform.InferType()(mod)
mutated_mod['func_3972'] = func_3972
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3973 = relay.var("var_3973", dtype = "int32", shape = (630,))#candidate|3973|(630,)|var|int32
func_3972_call = mutated_mod.get_global_var('func_3972')
call_3974 = func_3972_call(var_3973)
output = call_3974
func_3975 = relay.Function([var_3973], output)
mutated_mod['func_3975'] = func_3975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3771_call = mod.get_global_var('func_3771')
func_3773_call = mutated_mod.get_global_var('func_3773')
call_3977 = relay.TupleGetItem(func_3771_call(), 0)
call_3978 = relay.TupleGetItem(func_3773_call(), 0)
output = call_3977
output2 = call_3978
func_3982 = relay.Function([], output)
mod['func_3982'] = func_3982
mod = relay.transform.InferType()(mod)
mutated_mod['func_3982'] = func_3982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3982_call = mutated_mod.get_global_var('func_3982')
call_3983 = func_3982_call()
output = call_3983
func_3984 = relay.Function([], output)
mutated_mod['func_3984'] = func_3984
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3990 = relay.const([[[-2.674450,-4.221736,-0.238018,3.702749,4.112215,-1.079988,-1.928180,6.267030,3.419886],[2.104902,-6.311951,1.258684,-3.344258,3.600623,-6.055785,-9.839775,9.872338,-6.997375],[3.878112,6.468499,-8.903674,2.552359,8.493232,3.990204,9.518928,9.487851,-7.559198],[6.321752,-0.766298,-0.157353,0.614461,2.022026,-9.022634,-5.118145,-1.584357,-3.411165],[-7.899179,2.134937,-0.770748,-8.359365,2.100134,0.912821,-7.173879,-5.454992,5.064283],[-5.895528,1.677461,-6.249769,6.411904,7.215451,-4.665349,-0.405461,2.956413,-2.991645],[2.277964,7.949635,-8.700894,-8.288062,8.658214,3.262157,-3.803009,7.950507,-3.956977],[2.460273,9.452088,7.836572,-2.183758,-6.590308,0.378681,8.767259,3.542382,9.834154]],[[7.255962,-8.782995,-6.280054,0.910405,8.031436,-3.491768,-5.692226,6.442464,-5.965007],[-9.162790,1.746853,-6.769674,2.199250,2.872229,-9.214040,5.358053,-8.367275,0.055639],[7.692793,8.564833,6.200821,-5.044695,3.766003,3.997761,-3.904362,-9.395516,-1.485817],[-0.869295,-7.606902,-0.664332,-5.255316,-8.863067,-8.163608,4.587817,9.917949,-1.500081],[-3.687550,-2.787846,1.232027,3.468261,8.490567,9.614212,-7.376416,-2.092936,1.116834],[-6.585589,-3.723830,-3.002978,-2.274569,-1.915016,7.549238,-3.581487,-0.744189,8.611514],[3.373183,7.299352,6.305777,-2.320553,8.840050,-1.162059,-2.726470,-2.233822,-2.179778],[3.654868,2.638502,-4.595641,-4.422931,-4.890122,9.072825,-5.956663,2.145362,-2.036276]]], dtype = "float64")#candidate|3990|(2, 8, 9)|const|float64
uop_3991 = relay.sigmoid(const_3990.astype('float64')) # shape=(2, 8, 9)
output = relay.Tuple([uop_3991,])
output2 = relay.Tuple([uop_3991,])
func_3994 = relay.Function([], output)
mod['func_3994'] = func_3994
mod = relay.transform.InferType()(mod)
output = func_3994()
func_3995 = relay.Function([], output)
mutated_mod['func_3995'] = func_3995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3771_call = mod.get_global_var('func_3771')
func_3773_call = mutated_mod.get_global_var('func_3773')
call_4034 = relay.TupleGetItem(func_3771_call(), 0)
call_4035 = relay.TupleGetItem(func_3773_call(), 0)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_4051 = relay.TupleGetItem(func_3508_call(), 0)
call_4052 = relay.TupleGetItem(func_3510_call(), 0)
func_767_call = mod.get_global_var('func_767')
func_771_call = mutated_mod.get_global_var('func_771')
var_4073 = relay.var("var_4073", dtype = "int16", shape = ())#candidate|4073|()|var|int16
const_4074 = relay.const([-7,-6,-4,-6,-8,-2,-9], dtype = "int16")#candidate|4074|(7,)|const|int16
call_4072 = relay.TupleGetItem(func_767_call(relay.reshape(var_4073.astype('int16'), []), relay.reshape(const_4074.astype('int16'), [1, 7]), ), 1)
call_4075 = relay.TupleGetItem(func_771_call(relay.reshape(var_4073.astype('int16'), []), relay.reshape(const_4074.astype('int16'), [1, 7]), ), 1)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_4084 = relay.TupleGetItem(func_3508_call(), 0)
call_4085 = relay.TupleGetItem(func_3510_call(), 0)
func_406_call = mod.get_global_var('func_406')
func_409_call = mutated_mod.get_global_var('func_409')
call_4091 = relay.TupleGetItem(func_406_call(relay.reshape(call_4034.astype('uint8'), [6, 1, 15])), 1)
call_4092 = relay.TupleGetItem(func_409_call(relay.reshape(call_4034.astype('uint8'), [6, 1, 15])), 1)
uop_4094 = relay.atan(call_4091.astype('float32')) # shape=(6, 12, 15)
uop_4096 = relay.atan(call_4092.astype('float32')) # shape=(6, 12, 15)
func_3593_call = mod.get_global_var('func_3593')
func_3597_call = mutated_mod.get_global_var('func_3597')
var_4107 = relay.var("var_4107", dtype = "uint64", shape = (120,))#candidate|4107|(120,)|var|uint64
call_4106 = relay.TupleGetItem(func_3593_call(relay.reshape(var_4107.astype('uint64'), [10, 3, 4]), relay.reshape(var_4107.astype('uint64'), [10, 3, 4]), ), 3)
call_4108 = relay.TupleGetItem(func_3597_call(relay.reshape(var_4107.astype('uint64'), [10, 3, 4]), relay.reshape(var_4107.astype('uint64'), [10, 3, 4]), ), 3)
output = relay.Tuple([call_4034,call_4051,call_4072,var_4073,const_4074,call_4084,uop_4094,call_4106,var_4107,])
output2 = relay.Tuple([call_4035,call_4052,call_4075,var_4073,const_4074,call_4085,uop_4096,call_4108,var_4107,])
func_4111 = relay.Function([var_4073,var_4107,], output)
mod['func_4111'] = func_4111
mod = relay.transform.InferType()(mod)
var_4112 = relay.var("var_4112", dtype = "int16", shape = ())#candidate|4112|()|var|int16
var_4113 = relay.var("var_4113", dtype = "uint64", shape = (120,))#candidate|4113|(120,)|var|uint64
output = func_4111(var_4112,var_4113,)
func_4114 = relay.Function([var_4112,var_4113,], output)
mutated_mod['func_4114'] = func_4114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3982_call = mod.get_global_var('func_3982')
func_3984_call = mutated_mod.get_global_var('func_3984')
call_4123 = func_3982_call()
call_4124 = func_3982_call()
output = relay.Tuple([call_4123,])
output2 = relay.Tuple([call_4124,])
func_4141 = relay.Function([], output)
mod['func_4141'] = func_4141
mod = relay.transform.InferType()(mod)
mutated_mod['func_4141'] = func_4141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4141_call = mutated_mod.get_global_var('func_4141')
call_4142 = func_4141_call()
output = call_4142
func_4143 = relay.Function([], output)
mutated_mod['func_4143'] = func_4143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4141_call = mod.get_global_var('func_4141')
func_4143_call = mutated_mod.get_global_var('func_4143')
call_4184 = relay.TupleGetItem(func_4141_call(), 0)
call_4185 = relay.TupleGetItem(func_4143_call(), 0)
output = relay.Tuple([call_4184,])
output2 = relay.Tuple([call_4185,])
func_4213 = relay.Function([], output)
mod['func_4213'] = func_4213
mod = relay.transform.InferType()(mod)
output = func_4213()
func_4214 = relay.Function([], output)
mutated_mod['func_4214'] = func_4214
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4215 = relay.var("var_4215", dtype = "int32", shape = (12, 4, 1))#candidate|4215|(12, 4, 1)|var|int32
const_4216 = relay.const([[[5,-5,-5,8,7,-10,2,-1,2],[8,8,-10,6,-3,-10,-10,-4,-3],[-7,8,-6,-1,2,3,-9,9,4],[-2,-7,3,3,2,10,8,-4,-3]],[[5,-1,6,-2,-4,4,2,10,1],[9,-9,-5,4,-6,10,-1,3,-3],[-5,-6,9,8,-8,-1,4,-6,8],[-3,5,-5,9,1,7,3,-2,-2]],[[10,10,-10,8,-10,-8,4,-5,1],[5,3,9,1,-3,-10,-3,6,-8],[-6,-10,-1,-7,2,-3,9,10,-3],[5,3,-6,-2,3,4,-4,-10,-7]],[[5,-3,7,9,-5,1,7,1,-3],[-3,7,2,-1,-10,-1,9,4,-2],[-9,6,-9,1,2,-8,-10,9,-8],[7,-5,8,5,-3,-1,-9,-5,6]],[[3,-10,1,9,8,9,8,5,4],[-3,-5,9,9,-8,-6,-8,6,-5],[5,-10,-3,-9,6,6,1,2,-6],[-2,10,1,6,4,-7,-9,-4,-3]],[[8,8,8,-6,5,-5,-9,-6,-6],[-7,-6,2,-10,6,-10,1,-3,-1],[-4,3,7,2,4,-6,-7,-3,-4],[8,8,9,5,5,10,-2,-5,6]],[[3,-7,-8,-7,6,9,7,-5,1],[2,-4,5,-10,-8,10,-6,-4,9],[-8,6,-8,-7,2,9,-5,-9,-5],[3,-1,-2,-7,-3,-5,-2,9,-8]],[[-2,-4,-8,8,-4,-4,-1,-8,-10],[-3,-1,9,-9,1,-2,6,6,8],[3,-5,5,7,6,8,8,-4,-10],[-6,-7,-8,6,3,-6,-3,-9,7]],[[10,9,1,-4,1,-7,5,1,-10],[1,4,5,-4,-10,-1,-4,3,8],[1,5,2,-2,-7,8,-1,-1,-10],[-5,-7,7,2,-8,5,10,-8,9]],[[-9,8,3,1,-5,-10,-1,1,-2],[7,-10,-10,10,2,-7,9,-3,1],[-1,1,-7,2,8,7,2,7,-10],[8,8,-8,-2,-10,4,-2,-6,-2]],[[5,-10,-5,-6,-2,10,9,9,-9],[-2,-6,7,-6,6,3,-4,1,-5],[10,5,4,3,1,-1,-1,-5,-7],[-8,3,-4,1,9,9,-8,5,2]],[[-7,3,7,10,8,6,8,-6,-7],[9,8,7,2,-8,-7,8,-3,3],[6,-9,-9,-8,6,-9,-6,-10,6],[2,1,7,-10,3,8,5,-1,10]]], dtype = "int32")#candidate|4216|(12, 4, 9)|const|int32
bop_4217 = relay.add(var_4215.astype('int32'), const_4216.astype('int32')) # shape=(12, 4, 9)
bop_4230 = relay.greater_equal(bop_4217.astype('bool'), var_4215.astype('bool')) # shape=(12, 4, 9)
func_3911_call = mod.get_global_var('func_3911')
func_3914_call = mutated_mod.get_global_var('func_3914')
const_4234 = relay.const([4.621504,-9.583774,7.019820,8.333920,-3.487724,7.612617,9.400948,1.651256,-7.923015,2.424610,-8.620131,-0.820897,7.282907,5.090277,-0.224189,4.307934,1.351444,6.759252,-0.283685,-5.412865,-9.083415,2.260648,4.889942,-6.394383,2.198678,-4.516213,-3.763753,6.922490,-5.851950,-7.471076,3.451433,-3.090168,2.289988,8.459258,0.486944,5.156723,2.979897,9.161993,7.929839,-8.369516,6.579088,-0.877036,-8.464326,6.170994,-6.651527,0.996477,5.814712,-2.849116,-7.901762,-6.325690,3.815526,6.396525,-7.567109,6.269271,-3.985107,1.804319,9.319634,0.106409,6.571344,-3.937116,-3.251420,0.698305,3.877814,5.204679,3.921018,2.562613,8.299296,7.608459,-7.925460,7.677382,-5.083723,-1.359362,-2.197184,9.878549,9.161066,-2.391212,-8.235024,6.790502,5.648148,6.657902,5.963996,-4.726120,8.569782,-8.816933,-7.405375,-4.253733,-7.219209,-0.359325,8.574666,-0.689390,8.783550,-5.350149,-8.863575,-5.726474,-0.245232,-6.807492,-4.796089,-0.089106,-2.166387,9.785433,-9.224392,-5.939502,9.276699,-2.557687,-7.396181,5.953119,4.453043,1.813637], dtype = "float32")#candidate|4234|(108,)|const|float32
call_4233 = relay.TupleGetItem(func_3911_call(relay.reshape(const_4234.astype('float32'), [3, 12, 3])), 1)
call_4235 = relay.TupleGetItem(func_3914_call(relay.reshape(const_4234.astype('float32'), [3, 12, 3])), 1)
func_1303_call = mod.get_global_var('func_1303')
func_1307_call = mutated_mod.get_global_var('func_1307')
const_4239 = relay.const([-10,2,-3,-3,-3,7,1,4,-3,7,-2,-8,-8,-1,1,-6,-10,-1,5,10,-4,7,-4,-1,1,4,6,-6,-10,7,6,-2,-4,-1,-8,-8,1,-6,-8,1,8,-3,-9,9,3,-1,-9,-9,-8,3,3,-6,9,-9,-2,-6,-8,-3,7,6,-5,-3,10,9,-2,3,4,-10,-3,9,7,-6,-6,2,10,-5,7,-1,-8,6,-3,-5,-10,9,2,-1,-5,6,7,-5,9,3,-8,4,5,5,-1,-4,-5,-8,-10,8,7,7,3,2,1,-6,10,-6,2,-4,4,-5,2,6,4,7,7,7,5,-1,-3,-7,9,-9,-7,-5,2,9,-5,5,-10,-3,6,8,7,10,-8,-4,-10,-9,9,-7,-6,-6,5,2,-4,4,-3,3,-4,10,10,1,9,9,6,9,-4,4,-6,5,-1,4,-3,-4,10,1,9,1,3,-8,-6,10,-3,9,1,1,-3,6,2,5,5,5,9,6,6,3,-2,-3,-9,4,6,-2,10,5,9,7,9,9,-8,1,10,7,9,5,-10,-8,4,-5,9,6,1,1,5,-7,-7,-6,-4,-7,1,-1,-2,-7,-10,-1,-2,6,-10,5,-8,-8,-5,-2,-7,4,-4,1,5,-2,-10,-7,-8,10,-1,-5,9,6,8,-5,-10,3,3,9,1,6,-2,8,5,2,-2,4,10,7,9,-3,8,-10,1,10,1,-7,-8,-3,-10,-8,-1,6,-4,9,5,-2,-9,6,4,-4,-4,7,6,3,-6,8,3,9,9,3,-2,-8,9,-3,-2,7,-9,-5,6,-1,-9,10,-5,1,6,9,-9,9,3,-1,8,-10,-2,-2,-7,9,-1,9,-7,-1,6,-1,9,3,1,-8,9,7,-6,-10,-1,-8,9,10,8,8,-5,9,8,-7,-5,9,-4,-7,-7,-1,7,3,-7,-9,6,8,-6,-5,-10,-5,-7,9,1,10,-3,6,-10,-4,-2,3,2,-1,-10,-3,3,3,2,-1,-6,-1,-4,8,6,3,5,-9,-7,5,1,8,-8,1,-3,-5,5,-9,-2,5,9,7,-3,-2,9,10,7,-1,10,-7,6,3,7,-10,-1,1,4,3,-6,-10,4,2,-9,-8,-7,-2,-8,-4,-9,8,-1,9,6,-3,-8,-7,4,-6,4,-1,-1,-4,10,-8,4,10,-4,3,2,4,10,2,1,-8,-2,-6,10,3,-1,8,8,3,6,2,3,-7,7,8,7,-3,-4,1,-10,-3,-9,6,-10,9,-4,-5,-7,1,-10,-2,-4,-6,-3,-2,5,-3,10,-10,-8,-8,10,-1,-4,2,1,2,10,-6,7,5,-5,4,8,6,3,-10,7,-1,-4,-6,-9,-2,6,-4,-6,-5,-9,-8,3,5,-10,-10,-6,6,5,5,-10,-5,-7,-9,7,-5,5,3,9,-5,-5,-4,7,1,1,6,-4,-8,-9,3,-5,2,4,-7,5,10,6,-1,3,4,7,-7,-2,-2,-4,-9,-5,-8,-8,10,6,5,3,6,7,3,-2,7,-5,-7,5,-9,-8,-9,-1,-2,-10,-10,3,10,8,6,-4,-5,3,10,-9,8], dtype = "int8")#candidate|4239|(600,)|const|int8
call_4238 = relay.TupleGetItem(func_1303_call(relay.reshape(const_4239.astype('int8'), [10, 4, 15]), relay.reshape(const_4239.astype('int8'), [10, 4, 15]), ), 0)
call_4240 = relay.TupleGetItem(func_1307_call(relay.reshape(const_4239.astype('int8'), [10, 4, 15]), relay.reshape(const_4239.astype('int8'), [10, 4, 15]), ), 0)
func_3839_call = mod.get_global_var('func_3839')
func_3844_call = mutated_mod.get_global_var('func_3844')
const_4251 = relay.const([[1,7,3,8,-10,-4,-3,-8,9,-8,-10,7,4,6,1,8,-1,1,1,-9,-8,-9,-5,-3,6,1,2,7,-9,10,2,-5,6,-9,5,-9,9,4,-4,-2,-2,-8,8,-8,10,-10,-9,5,9,2,10,-9,-1,6,-9,8,1,6,3,10,-4,-4,-3,10,-5,-8,-6,-7,-9,4,3,-1],[-10,-6,1,-4,6,9,1,3,-2,2,-9,6,-3,-8,-4,1,-4,-7,-6,-1,3,4,-9,-1,-2,-10,-3,1,-9,-2,-7,-7,1,7,6,-2,8,-4,-4,10,7,7,8,-6,8,-10,-1,10,-2,1,-7,-9,-8,-3,-8,-8,-3,-5,-4,10,8,-9,-8,1,5,1,5,-6,5,-5,2,-9],[10,-8,4,-4,-9,-1,1,-8,-6,-8,-1,5,-6,8,-6,5,-1,-8,-2,-7,-7,-7,-2,7,-5,8,1,-1,-6,5,4,-7,2,1,-10,-2,-9,-7,7,9,-9,8,-10,9,8,9,-3,-8,-4,6,9,2,10,-9,5,6,4,-6,-3,-2,8,-4,10,5,-10,7,-2,7,2,6,5,3],[-10,-6,5,-5,-1,-3,10,4,-10,1,-4,3,-8,3,-3,-3,-7,-5,8,3,-8,10,-6,-1,-9,-8,5,-9,10,-4,-10,5,5,8,-9,-1,-9,6,9,-4,2,-9,1,7,10,6,8,5,-1,-5,6,-9,10,2,5,-6,-6,-3,3,-2,-3,4,8,-5,4,1,-9,-7,-8,-8,5,-3],[9,9,7,-8,10,4,-1,8,10,-7,2,7,3,4,-9,8,-2,-1,-10,1,-1,7,3,-9,-5,-1,-10,-6,4,-2,8,1,9,-10,1,7,6,3,-9,4,9,-10,6,6,7,-4,-8,-2,-9,3,6,3,6,-3,8,-1,-5,-10,7,4,3,-7,-5,7,-5,-5,2,3,3,5,5,2],[8,-2,9,-9,6,-5,-8,6,-5,-4,-8,-9,5,6,-1,-2,2,4,-2,6,-2,8,5,3,4,9,4,-6,-1,9,-1,-2,4,4,10,3,-3,2,-4,8,-2,-3,4,-5,2,-8,6,-5,6,6,3,8,2,-4,4,-6,8,3,9,-8,4,3,5,-10,-9,-9,-8,8,8,6,-3,-10],[-2,-4,5,-1,9,-8,-1,-7,7,-5,-4,4,-5,8,3,-1,-5,5,7,8,1,2,6,-4,-7,9,4,-7,-4,-6,-5,3,10,-7,-5,4,-2,-7,8,-5,-4,6,10,4,-8,-4,-7,-10,-4,-5,5,4,-8,8,-4,-10,-9,-6,-10,6,1,1,-6,7,10,-6,5,-2,3,-8,-5,7],[5,-7,-4,-2,-5,-4,-4,9,-5,8,-7,3,-4,-8,9,5,7,-8,-6,-7,-5,-10,-2,-4,-5,4,-7,-1,8,-8,-5,1,-6,4,-1,-3,-3,-7,1,1,6,-10,-4,1,-2,-1,5,-10,2,3,6,2,-6,-4,10,4,3,-10,7,-1,2,6,3,-8,-10,8,6,5,9,-10,-5,9],[-2,-6,-8,-8,8,-10,1,-6,9,-9,6,-7,-3,5,3,7,1,-4,2,-3,-7,-1,-9,1,3,-10,-4,-5,4,-5,4,-2,-5,7,-10,8,-1,8,-10,-7,9,-3,6,9,5,-1,-8,-5,-9,10,3,9,-1,-4,-5,3,2,-8,1,10,-3,-9,6,-6,8,-6,-6,-5,-9,-7,1,10],[-7,4,8,-7,7,-4,10,7,5,-9,6,9,4,-2,9,10,2,3,-10,-3,-6,9,4,-6,-9,2,-10,3,-9,8,-8,-2,-2,8,-7,8,-7,-9,-3,2,9,-9,4,-2,-8,-1,-1,-7,-1,-5,-6,-2,-2,-6,8,-6,3,-8,9,10,-10,-4,-5,4,-5,-6,3,-8,1,-9,1,9],[-3,10,7,-1,-4,-10,5,-7,-4,-5,-1,4,-6,-2,-2,-2,-10,-9,4,-5,-5,9,6,4,7,9,-2,-9,-7,5,3,-4,-10,9,-3,2,7,1,5,5,5,-9,6,5,-10,1,-6,6,8,-9,10,-10,-5,4,8,-4,-3,10,-3,-3,3,-6,-10,6,2,10,9,10,-3,-3,-4,-2],[10,-6,-6,7,4,-2,-8,4,-4,-1,-4,-6,-5,-6,6,6,1,-10,-3,-8,-10,3,9,-9,10,5,-3,1,-9,-7,-4,-10,4,-3,9,-4,-4,-9,4,5,10,-10,-2,-2,-5,-4,1,5,6,-10,9,-3,3,-5,2,3,-3,-6,1,4,7,8,-3,-3,10,5,-9,4,2,1,1,-7]], dtype = "int16")#candidate|4251|(12, 72)|const|int16
var_4252 = relay.var("var_4252", dtype = "uint8", shape = (336,))#candidate|4252|(336,)|var|uint8
var_4253 = relay.var("var_4253", dtype = "float64", shape = (270,))#candidate|4253|(270,)|var|float64
call_4250 = relay.TupleGetItem(func_3839_call(relay.reshape(const_4251.astype('int16'), [12, 8, 9]), relay.reshape(const_4251.astype('int16'), [12, 8, 9]), relay.reshape(var_4252.astype('uint8'), [336,]), relay.reshape(var_4253.astype('float64'), [270,]), ), 5)
call_4254 = relay.TupleGetItem(func_3844_call(relay.reshape(const_4251.astype('int16'), [12, 8, 9]), relay.reshape(const_4251.astype('int16'), [12, 8, 9]), relay.reshape(var_4252.astype('uint8'), [336,]), relay.reshape(var_4253.astype('float64'), [270,]), ), 5)
func_3994_call = mod.get_global_var('func_3994')
func_3995_call = mutated_mod.get_global_var('func_3995')
call_4257 = relay.TupleGetItem(func_3994_call(), 0)
call_4258 = relay.TupleGetItem(func_3995_call(), 0)
output = relay.Tuple([bop_4230,call_4233,const_4234,call_4238,const_4239,call_4250,const_4251,var_4252,var_4253,call_4257,])
output2 = relay.Tuple([bop_4230,call_4235,const_4234,call_4240,const_4239,call_4254,const_4251,var_4252,var_4253,call_4258,])
func_4262 = relay.Function([var_4215,var_4252,var_4253,], output)
mod['func_4262'] = func_4262
mod = relay.transform.InferType()(mod)
mutated_mod['func_4262'] = func_4262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4262_call = mutated_mod.get_global_var('func_4262')
var_4264 = relay.var("var_4264", dtype = "int32", shape = (12, 4, 1))#candidate|4264|(12, 4, 1)|var|int32
var_4265 = relay.var("var_4265", dtype = "uint8", shape = (336,))#candidate|4265|(336,)|var|uint8
var_4266 = relay.var("var_4266", dtype = "float64", shape = (270,))#candidate|4266|(270,)|var|float64
call_4263 = func_4262_call(var_4264,var_4265,var_4266,)
output = call_4263
func_4267 = relay.Function([var_4264,var_4265,var_4266,], output)
mutated_mod['func_4267'] = func_4267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3567_call = mod.get_global_var('func_3567')
func_3569_call = mutated_mod.get_global_var('func_3569')
call_4278 = relay.TupleGetItem(func_3567_call(), 0)
call_4279 = relay.TupleGetItem(func_3569_call(), 0)
var_4281 = relay.var("var_4281", dtype = "float64", shape = (3, 12, 3))#candidate|4281|(3, 12, 3)|var|float64
bop_4282 = relay.less_equal(call_4278.astype('bool'), relay.reshape(var_4281.astype('bool'), relay.shape_of(call_4278))) # shape=(3, 12, 3)
bop_4285 = relay.less_equal(call_4279.astype('bool'), relay.reshape(var_4281.astype('bool'), relay.shape_of(call_4279))) # shape=(3, 12, 3)
func_3860_call = mod.get_global_var('func_3860')
func_3862_call = mutated_mod.get_global_var('func_3862')
call_4303 = relay.TupleGetItem(func_3860_call(), 1)
call_4304 = relay.TupleGetItem(func_3862_call(), 1)
output = relay.Tuple([bop_4282,call_4303,])
output2 = relay.Tuple([bop_4285,call_4304,])
func_4308 = relay.Function([var_4281,], output)
mod['func_4308'] = func_4308
mod = relay.transform.InferType()(mod)
mutated_mod['func_4308'] = func_4308
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4309 = relay.var("var_4309", dtype = "float64", shape = (3, 12, 3))#candidate|4309|(3, 12, 3)|var|float64
func_4308_call = mutated_mod.get_global_var('func_4308')
call_4310 = func_4308_call(var_4309)
output = call_4310
func_4311 = relay.Function([var_4309], output)
mutated_mod['func_4311'] = func_4311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4213_call = mod.get_global_var('func_4213')
func_4214_call = mutated_mod.get_global_var('func_4214')
call_4326 = relay.TupleGetItem(func_4213_call(), 0)
call_4327 = relay.TupleGetItem(func_4214_call(), 0)
uop_4331 = relay.asin(call_4326.astype('float64')) # shape=(10, 9, 1)
uop_4333 = relay.asin(call_4327.astype('float64')) # shape=(10, 9, 1)
uop_4338 = relay.sigmoid(uop_4331.astype('float64')) # shape=(10, 9, 1)
uop_4340 = relay.sigmoid(uop_4333.astype('float64')) # shape=(10, 9, 1)
func_3593_call = mod.get_global_var('func_3593')
func_3597_call = mutated_mod.get_global_var('func_3597')
const_4342 = relay.const([-2,2,3,-10,-9,-2,-4,-8,2,3,-7,7,-9,-9,9,7,-7,9,-4,-2,10,5,6,-4,1,10,-2,1,3,-4,-8,-6,-1,-6,4,1,-2,1,2,-6,3,-10,10,6,-1,-6,5,-5,-8,5,-9,-9,-3,-6,-6,-7,-8,-5,10,4,6,-10,3,-9,-6,-7,1,3,6,10,-6,10,5,4,7,-7,-7,3,-4,-5,9,5,-7,5,-2,3,1,1,1,9,3,-2,-3,-2,-9,7,-8,7,5,-9,6,-4,-7,3,10,5,-10,-6,2,-1,-7,-9,3,10,-8,6,1,3,4,-6], dtype = "uint64")#candidate|4342|(120,)|const|uint64
call_4341 = relay.TupleGetItem(func_3593_call(relay.reshape(const_4342.astype('uint64'), [10, 3, 4]), relay.reshape(const_4342.astype('uint64'), [10, 3, 4]), ), 3)
call_4343 = relay.TupleGetItem(func_3597_call(relay.reshape(const_4342.astype('uint64'), [10, 3, 4]), relay.reshape(const_4342.astype('uint64'), [10, 3, 4]), ), 3)
var_4346 = relay.var("var_4346", dtype = "float64", shape = (10, 9, 3))#candidate|4346|(10, 9, 3)|var|float64
bop_4347 = relay.power(uop_4331.astype('float64'), var_4346.astype('float64')) # shape=(10, 9, 3)
bop_4350 = relay.power(uop_4333.astype('float64'), var_4346.astype('float64')) # shape=(10, 9, 3)
var_4351 = relay.var("var_4351", dtype = "float64", shape = (10, 9, 3))#candidate|4351|(10, 9, 3)|var|float64
bop_4352 = relay.mod(bop_4347.astype('float32'), relay.reshape(var_4351.astype('float32'), relay.shape_of(bop_4347))) # shape=(10, 9, 3)
bop_4355 = relay.mod(bop_4350.astype('float32'), relay.reshape(var_4351.astype('float32'), relay.shape_of(bop_4350))) # shape=(10, 9, 3)
uop_4360 = relay.cos(uop_4338.astype('float32')) # shape=(10, 9, 1)
uop_4362 = relay.cos(uop_4340.astype('float32')) # shape=(10, 9, 1)
output = relay.Tuple([call_4341,const_4342,bop_4352,uop_4360,])
output2 = relay.Tuple([call_4343,const_4342,bop_4355,uop_4362,])
func_4366 = relay.Function([var_4346,var_4351,], output)
mod['func_4366'] = func_4366
mod = relay.transform.InferType()(mod)
var_4367 = relay.var("var_4367", dtype = "float64", shape = (10, 9, 3))#candidate|4367|(10, 9, 3)|var|float64
var_4368 = relay.var("var_4368", dtype = "float64", shape = (10, 9, 3))#candidate|4368|(10, 9, 3)|var|float64
output = func_4366(var_4367,var_4368,)
func_4369 = relay.Function([var_4367,var_4368,], output)
mutated_mod['func_4369'] = func_4369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4213_call = mod.get_global_var('func_4213')
func_4214_call = mutated_mod.get_global_var('func_4214')
call_4402 = relay.TupleGetItem(func_4213_call(), 0)
call_4403 = relay.TupleGetItem(func_4214_call(), 0)
const_4405 = relay.const([[[4.394339],[8.426966],[2.325168],[-4.829677],[8.924094],[3.948406],[-1.841745],[-0.421272],[-0.870704]],[[3.657566],[4.587136],[3.413111],[-4.838179],[1.312591],[-1.257252],[-0.197282],[4.241117],[-3.444443]],[[5.926940],[4.043432],[-8.422946],[2.586280],[-1.439415],[-4.597198],[8.981623],[5.669033],[4.720060]],[[-1.784579],[-0.805745],[9.824470],[-4.485462],[-1.690282],[-8.536118],[-6.450376],[2.311981],[-5.686809]],[[-0.804696],[2.703693],[3.121378],[5.219069],[1.436369],[6.576106],[-6.957553],[4.319648],[8.690062]],[[9.219332],[-8.037422],[6.807975],[-0.855299],[-6.864615],[-0.247792],[-6.809024],[0.813021],[4.575829]],[[5.258250],[5.976057],[4.734959],[8.521737],[-2.481993],[1.949394],[5.716986],[7.671636],[-3.168740]],[[-8.942426],[-8.097722],[6.259754],[-8.531714],[-1.297344],[1.061801],[-8.558330],[-1.830555],[2.012332]],[[0.068972],[3.135938],[5.039048],[5.721070],[-8.847715],[1.682386],[-1.800043],[5.431448],[-4.067271]],[[3.831120],[-0.122976],[-9.272877],[4.974408],[-2.874553],[5.816414],[8.433015],[-7.777264],[-9.469443]]], dtype = "float64")#candidate|4405|(10, 9, 1)|const|float64
bop_4406 = relay.less_equal(call_4402.astype('bool'), relay.reshape(const_4405.astype('bool'), relay.shape_of(call_4402))) # shape=(10, 9, 1)
bop_4409 = relay.less_equal(call_4403.astype('bool'), relay.reshape(const_4405.astype('bool'), relay.shape_of(call_4403))) # shape=(10, 9, 1)
output = bop_4406
output2 = bop_4409
func_4411 = relay.Function([], output)
mod['func_4411'] = func_4411
mod = relay.transform.InferType()(mod)
mutated_mod['func_4411'] = func_4411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4411_call = mutated_mod.get_global_var('func_4411')
call_4412 = func_4411_call()
output = call_4412
func_4413 = relay.Function([], output)
mutated_mod['func_4413'] = func_4413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_4453 = relay.TupleGetItem(func_3129_call(), 0)
call_4454 = relay.TupleGetItem(func_3131_call(), 0)
func_3223_call = mod.get_global_var('func_3223')
func_3227_call = mutated_mod.get_global_var('func_3227')
var_4470 = relay.var("var_4470", dtype = "float64", shape = (1792,))#candidate|4470|(1792,)|var|float64
const_4471 = relay.const([-4,-4,6,-7,4,1,-5,-3,-9,-9,8,-6,8,2,-6,3,4,6,-5,-2,-2,-10,-8,-7,7,-7,-5,-1,6,10,2,1,-3,8,1,-8,1,-1,10,-7,5,4,-8,4,8,-5,7,8,4,-9,-6,-9,4,7,9,1,-9,-3,-1,10,-2,2,10,3,-8,10,-1,10,-10,-9,2,-2,-8,7,-3,-1,-9,-8,4,4,4,-5,-2,2,1,-2,3,3,8,-1,6,-7,4,5,-7,-10,-10,7,10,-5,-1,6,-10,5,9,-10,5,-10,-5,7,-4,4,-1,-8,-2,-6,2,7,10,-10,6,-6,9,2,-2,5,-5,10,2,9,-10,7,4,4,5,-7,-5,-6,10,6,6,-8,10,8,-3,-6,-9,-5,-6,-1,2,-6,10,9,1,-3,-9,-9,-6,-3,-4,-4,-1,-10,-7,-1,-10,5,-10,-1,2,-7,5,-1,5,-2,4,-3,-6,-3,-5,-1,3,6,-10,4,3,4,9,8,3,2,9,-2,10,5,10,-10,-2,6,-5,8,2,-3,9,-5,-5,-10,4,-7,-7,-10,8,2,6,4,10,7,-5,-5,6,-9,-8,-5,-10,5,-5,-8,4,-5,-10,2,-2,-2,-3,-1,8,10,-8,-6,-5,8,5,5,6,10,10,5,-2,10,7,-4], dtype = "int16")#candidate|4471|(252,)|const|int16
call_4469 = relay.TupleGetItem(func_3223_call(relay.reshape(var_4470.astype('float64'), [16, 7, 16]), relay.reshape(const_4471.astype('int16'), [252,]), relay.reshape(var_4470.astype('float64'), [16, 7, 16]), ), 6)
call_4472 = relay.TupleGetItem(func_3227_call(relay.reshape(var_4470.astype('float64'), [16, 7, 16]), relay.reshape(const_4471.astype('int16'), [252,]), relay.reshape(var_4470.astype('float64'), [16, 7, 16]), ), 6)
output = relay.Tuple([call_4453,call_4469,var_4470,const_4471,])
output2 = relay.Tuple([call_4454,call_4472,var_4470,const_4471,])
func_4492 = relay.Function([var_4470,], output)
mod['func_4492'] = func_4492
mod = relay.transform.InferType()(mod)
mutated_mod['func_4492'] = func_4492
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4493 = relay.var("var_4493", dtype = "float64", shape = (1792,))#candidate|4493|(1792,)|var|float64
func_4492_call = mutated_mod.get_global_var('func_4492')
call_4494 = func_4492_call(var_4493)
output = call_4494
func_4495 = relay.Function([var_4493], output)
mutated_mod['func_4495'] = func_4495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3567_call = mod.get_global_var('func_3567')
func_3569_call = mutated_mod.get_global_var('func_3569')
call_4513 = relay.TupleGetItem(func_3567_call(), 1)
call_4514 = relay.TupleGetItem(func_3569_call(), 1)
uop_4517 = relay.cos(call_4513.astype('float64')) # shape=(10, 4, 15)
uop_4519 = relay.cos(call_4514.astype('float64')) # shape=(10, 4, 15)
output = uop_4517
output2 = uop_4519
func_4527 = relay.Function([], output)
mod['func_4527'] = func_4527
mod = relay.transform.InferType()(mod)
mutated_mod['func_4527'] = func_4527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4527_call = mutated_mod.get_global_var('func_4527')
call_4528 = func_4527_call()
output = call_4528
func_4529 = relay.Function([], output)
mutated_mod['func_4529'] = func_4529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4141_call = mod.get_global_var('func_4141')
func_4143_call = mutated_mod.get_global_var('func_4143')
call_4543 = relay.TupleGetItem(func_4141_call(), 0)
call_4544 = relay.TupleGetItem(func_4143_call(), 0)
output = relay.Tuple([call_4543,])
output2 = relay.Tuple([call_4544,])
func_4552 = relay.Function([], output)
mod['func_4552'] = func_4552
mod = relay.transform.InferType()(mod)
mutated_mod['func_4552'] = func_4552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4552_call = mutated_mod.get_global_var('func_4552')
call_4553 = func_4552_call()
output = call_4553
func_4554 = relay.Function([], output)
mutated_mod['func_4554'] = func_4554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3796_call = mod.get_global_var('func_3796')
func_3798_call = mutated_mod.get_global_var('func_3798')
call_4557 = relay.TupleGetItem(func_3796_call(), 0)
call_4558 = relay.TupleGetItem(func_3798_call(), 0)
uop_4562 = relay.log2(call_4557.astype('float32')) # shape=(3, 12, 3)
uop_4564 = relay.log2(call_4558.astype('float32')) # shape=(3, 12, 3)
bop_4572 = relay.logical_and(uop_4562.astype('bool'), relay.reshape(call_4557.astype('bool'), relay.shape_of(uop_4562))) # shape=(3, 12, 3)
bop_4575 = relay.logical_and(uop_4564.astype('bool'), relay.reshape(call_4558.astype('bool'), relay.shape_of(uop_4564))) # shape=(3, 12, 3)
const_4588 = relay.const([[[False,True,False],[True,True,True],[True,True,True],[False,False,False],[True,False,True],[False,True,False],[False,True,True],[True,False,True],[False,False,True],[True,True,True],[True,False,False],[False,True,False]],[[True,True,True],[True,True,False],[True,False,False],[True,False,True],[True,True,True],[False,False,True],[True,False,True],[True,True,False],[False,True,False],[True,True,False],[True,False,True],[False,True,False]],[[False,True,False],[True,False,False],[False,True,True],[True,True,True],[False,False,True],[True,True,True],[False,False,False],[False,True,True],[False,False,True],[True,False,True],[True,True,False],[True,False,False]]], dtype = "bool")#candidate|4588|(3, 12, 3)|const|bool
bop_4589 = relay.power(bop_4572.astype('float64'), relay.reshape(const_4588.astype('float64'), relay.shape_of(bop_4572))) # shape=(3, 12, 3)
bop_4592 = relay.power(bop_4575.astype('float64'), relay.reshape(const_4588.astype('float64'), relay.shape_of(bop_4575))) # shape=(3, 12, 3)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_4593 = relay.TupleGetItem(func_3508_call(), 0)
call_4594 = relay.TupleGetItem(func_3510_call(), 0)
uop_4615 = relay.cos(bop_4572.astype('float32')) # shape=(3, 12, 3)
uop_4617 = relay.cos(bop_4575.astype('float32')) # shape=(3, 12, 3)
bop_4637 = relay.divide(uop_4615.astype('float64'), relay.reshape(const_4588.astype('float64'), relay.shape_of(uop_4615))) # shape=(3, 12, 3)
bop_4640 = relay.divide(uop_4617.astype('float64'), relay.reshape(const_4588.astype('float64'), relay.shape_of(uop_4617))) # shape=(3, 12, 3)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
const_4658 = relay.const([4.710876,3.045994,6.511619,1.942598,-3.062269,-1.061271,-6.715739,2.966167,-7.493175,-3.104748,-6.290462,6.423458,-0.731625,0.073759,6.573481,3.364707,4.341089,8.366528,-5.346389,8.344715,2.442939,4.608748,-1.011583,8.558085,-2.071207,-7.067442,1.315595,4.598571,-1.032687,2.071860,6.963968,-8.434278,6.640558,0.568630,7.398389,-1.753677,2.850222,-4.281993,-2.434772,-2.734909,5.351654,9.793494,-4.384497,-5.751367,0.666798,-3.749776,-3.481644,9.594443,-9.457634,-3.000440,-8.648233,4.859017,-2.906639,9.484431,8.230515,-8.393020,0.014236,6.408698,-2.129218,-9.594822,5.484942,-9.945970,-1.872968,5.921152,-0.906698,-7.937358,-9.830938,-1.160999,8.969465,5.236382,2.966364,1.744930,7.878683,-1.426136,-8.591612,3.153803,-8.753697,-5.550829,-9.850233,5.308521,5.298580,0.664400,8.496112,-7.392178,5.089077,-3.896867,3.040708,7.567753,-4.470107,-2.481923,8.493588,0.641371,7.991525,-6.422577,8.266591,1.861084,8.726583,8.658611,-1.452459,0.292083,6.038398,1.563895,8.880413,-9.832385,-5.537994,-4.560812,-9.502189,8.569590,1.881521,9.637120,-6.030369,8.182845,0.573219,-8.224863,2.275214,-5.939991,5.967395,7.130447,-8.287857,8.477473,5.656870,-4.325094,4.617947,3.159478,2.486860,6.043607,8.582391,6.289065,6.090445,2.143579,3.970710,-3.756608,0.373809,7.040375,4.745596,-8.907643,1.219390,-6.615298,0.129431,9.212171,4.117873,-9.771721,-6.179515,1.808319,9.485981,-8.160192,-6.490037,-8.782576,-9.380718,-6.238302,-1.372644,-6.953636,4.261651,-8.671344,0.104057,-7.366263,-0.511668,4.409194,-0.105764,6.604563,5.821527,9.529667,-2.806405,5.817384,7.477624,-3.105939,8.528067,5.444080,2.001651,1.361318,-7.302036,7.526330,-1.986053,5.878532,-2.631580,-0.331244,-1.358033,7.556474,1.983929,0.277292,-5.550455,-1.562465,0.270375,3.335213,0.557543,7.312525,-8.921327,3.185650,7.186167,6.705780,6.810325,-8.692446,6.056192,-0.451467,-2.144084,-5.324987,2.584364,-6.894126,-7.452670,8.365853,-1.340020,6.119068,-2.416441,4.974317,5.616779,4.509484,0.974263,-8.154741,4.974101,8.099590,7.400775,5.246520,0.885111,5.470180,2.354567,8.205204,1.544028,-0.191084,3.455447,6.036094,-4.006347,6.408489,-9.763287,4.861605,-7.627915,-4.383303,-1.419469,-3.799948,0.994606,5.616769,8.284435,8.934941,-8.541243,-3.069863,6.378414,-6.619218,-5.351216,3.784827,-6.592647,-2.708259,-4.212271,-0.610059,-0.621543,-1.422714,-3.076711,-9.823895,-4.091798,-1.319591,6.767017,1.002851,-9.842530,8.572572,6.766309,-2.330787,1.392026,2.850679,4.167016,-1.038445,-0.107189,0.123188,-6.217683,-8.365939,1.446025,1.931836,1.065170,-4.331081,6.479403,-5.531975,-2.336312,-0.919417,-7.065416,9.572698,4.911474,5.889485,-2.335259,-8.037132,7.708688,-3.938831,7.195600,4.167731,-2.819875,-3.278840,8.803030,-2.916744,1.956507,9.810306,-3.470857,1.477928,-0.764021,-6.351828,-2.182807,-4.851115,7.127208,-1.699627,-3.884034,-7.231405,5.630514,-0.562180,3.497880,4.148359,8.493590,-1.164149,1.038994,9.336428,8.609279,5.062367,-6.892520,3.582407,-2.284065,-7.442944,1.247441,2.419410,-0.653038,-8.906936,-7.260393,-9.933232,-8.296984,-1.094449,1.736241,-8.198966,8.003376,-1.097735,2.416334,6.772118,7.093718,-9.649302,-6.049638,-6.907237,-5.223749,4.696657,-6.152015,-7.247511,-9.161582,-7.247227,2.196059,-2.858558,-3.715881,-4.797963,-1.840753,5.342667,-8.588130,6.193937,5.730827,1.141001,-9.924393,1.937807,-9.804420,6.654513,-9.866390,-8.708533,-7.888223,-8.025086,2.033213,-1.374796,-0.321884,-9.373528,-7.996771,-9.252628,4.673550,8.627987,-1.276557,-9.344747,-1.496378,7.866560,6.290573,-6.620480,7.546888,6.664510,-8.225354,-8.728245,3.987041,8.253260,-3.594557,-5.900417,3.110058,9.915151,-5.494881,-8.649830,-7.857302,2.028221,-4.157214,3.344386,-1.095101,-8.771799,0.032346,7.566278,0.300486,-2.883353,-6.614012,4.901748,-7.125095,6.006626,-5.783819,9.552570,-0.775153,6.721909,8.657806,-8.969416,9.155192,-6.431953,0.837759,2.878338,-3.802984,7.930785,-1.311747,-5.666424,0.776336,4.226404,0.274699,-9.177618,7.776106,-9.232790,1.099860,-5.404086,-4.020700,1.856609,7.169445,-5.795360,-1.515186,-9.846650,0.556432,3.456552,3.152882,-0.794000,6.616897,-2.711511,-6.168550,3.239295,3.084376,-5.226549,-2.984034,7.996844], dtype = "float32")#candidate|4658|(432,)|const|float32
call_4657 = relay.TupleGetItem(func_3463_call(relay.reshape(const_4658.astype('float32'), [4, 108])), 0)
call_4659 = relay.TupleGetItem(func_3465_call(relay.reshape(const_4658.astype('float32'), [4, 108])), 0)
func_4411_call = mod.get_global_var('func_4411')
func_4413_call = mutated_mod.get_global_var('func_4413')
call_4660 = func_4411_call()
call_4661 = func_4411_call()
output = relay.Tuple([bop_4589,call_4593,bop_4637,call_4657,const_4658,call_4660,])
output2 = relay.Tuple([bop_4592,call_4594,bop_4640,call_4659,const_4658,call_4661,])
func_4664 = relay.Function([], output)
mod['func_4664'] = func_4664
mod = relay.transform.InferType()(mod)
output = func_4664()
func_4665 = relay.Function([], output)
mutated_mod['func_4665'] = func_4665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3982_call = mod.get_global_var('func_3982')
func_3984_call = mutated_mod.get_global_var('func_3984')
call_4682 = func_3982_call()
call_4683 = func_3982_call()
output = call_4682
output2 = call_4683
func_4698 = relay.Function([], output)
mod['func_4698'] = func_4698
mod = relay.transform.InferType()(mod)
output = func_4698()
func_4699 = relay.Function([], output)
mutated_mod['func_4699'] = func_4699
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4822 = relay.var("var_4822", dtype = "float64", shape = (10, 16))#candidate|4822|(10, 16)|var|float64
uop_4823 = relay.rsqrt(var_4822.astype('float64')) # shape=(10, 16)
func_2976_call = mod.get_global_var('func_2976')
func_2979_call = mutated_mod.get_global_var('func_2979')
var_4838 = relay.var("var_4838", dtype = "float64", shape = (1, 104))#candidate|4838|(1, 104)|var|float64
const_4839 = relay.const([8.891779,-5.127598,3.098317,3.845609,7.813490,6.253534,-8.533514,6.129978,6.945358,7.430727,2.829351,5.787387,-9.733759,-9.668309,-1.845850,2.078269,3.515557,4.288884,9.570088,-8.439909,-0.242753,-9.218817,1.912256,-6.308034,-8.171588,4.557998,2.245941,-7.519602,1.172490,1.886205,-3.289644,-7.832984,-4.959534,-8.425576,-9.154644,-9.796310,-5.656842,-6.263951,5.556268,0.193011,-0.549342,1.623289,3.511015,7.055652,-7.579942,-1.118835,1.159362,-8.343577,9.355402,5.988715,2.518029,-4.167445,-1.777376,2.288523,9.573675,6.233271,-6.078487,-6.042699,-8.871666,-4.279561,-4.987426,2.999514,7.867277,-3.239896,-4.468462,5.143147,5.814349,-5.826861,-9.912641,9.447278,-4.674744,0.198410,-6.854011,-3.855282,2.086638,4.827666,0.955709,0.481963,6.088602,4.499025,8.918446,1.159721,8.982909,-6.095714,-4.190299,8.716798,-8.974905,1.112327,-5.227441,-8.632036,-6.466091,-2.199071,-2.931351,0.170782,4.871231,-7.352179,2.071973,4.157972,1.732324,-6.146054,-2.521910,-4.310619,-4.741213,7.186087,9.670636,-1.111891,6.578050,9.371194,-7.583824,0.638178,-3.336835,-4.539453,-7.849460,-7.093507,6.501013,6.237323,-9.331773,-7.390543,9.228959,-7.678240,1.672878,-8.475560,7.472718,5.097604,-3.348028,1.157284,-0.623757,-6.843375,1.398388,-1.936590,0.179722,-0.788945,7.591171,-0.456966,-7.736396,6.655726,8.926648,6.637644,3.763460,-8.552669,7.008238,-2.454418,4.466927,-4.888075,4.940045,8.226705,-8.225021,2.814926,8.583435,-0.159577,-7.261339,7.857808,-5.012831,-4.412734,7.187708,6.625847,-6.740511,-6.946625,6.055073,-2.031610,7.433171,5.053233,-8.895437,9.073335,7.094167,1.008902,7.997324,0.016052,9.313505,-3.761034,7.466395,-2.638293,8.585580,7.212009,3.516084,-1.203336,-5.197559,5.006724,-3.424963,-3.854871,-7.440037,8.926885,-6.073399,2.118159,-5.572421,8.182421,-6.988456,0.728393,-8.654580,-8.817004,-4.081036,1.010058,-2.884530,4.479139,1.814581,-0.395743,-8.791509,-4.701616,3.825688,-1.440223,9.523541,0.276994,7.887099,3.888495,0.730393,-3.654706,-9.691815,-8.009004,-3.369341,8.788018,9.008379,3.066101,8.616705,8.981074,-0.188615,-9.714550,1.163075,3.268200,-4.565645,-9.309793,-0.679840,-9.114987,-2.350993,5.715960,-1.345562,1.117806,4.286231,5.944510,-7.632640,9.699836,1.871127,-7.908480,1.775970,8.418413,-2.687079,1.375003,-7.243800,-6.382341,7.133261,1.578083,-7.603188,8.272548,-2.649814,8.920392,6.094227,7.622635,-5.240628,2.153462,6.389645,-6.034837,5.559064,-0.878557,7.582871,-6.933089,-5.019168,-2.106891,-8.731630,-7.441991,2.744933,8.403080,-2.227057,5.450748,-6.258804,-7.335695,4.736590,-3.492438,6.270982,7.089394,3.820960,4.486232,6.834946,-8.863554,5.877235,-8.434541,-0.204940,-7.325907,-7.617923,-5.881060,-9.462116,-5.491739,1.072941,-4.747812,0.494128,7.279678,-7.521272,0.690214,-1.660411,3.111502,-6.686913,-3.302302,-9.000367,-5.263749,-1.745260,0.982374,5.769760,2.045706,-0.813166,6.740619,5.110474,-8.101634,7.650930,0.702382,-3.920049,-9.850002,7.472023,2.731836,0.756267,-5.567538,-5.193811,-3.742282,-4.219998,-2.321996,-8.163923,-0.283592,-9.072433,6.627622,-1.602424,-0.822942,9.617016,-9.495257,1.908266,-5.630176,9.921137,0.737203,5.250216,5.928639,9.105492,-6.953940,-1.075017,1.913390,-6.013761,-3.290949,2.761349,3.077537,5.950149,8.593726,6.656708,6.018682,3.702734,5.301451,7.503495,-9.032668,-9.540561,-1.103327,3.436290,-9.106614,-3.905010,2.567634,1.731793,-1.100403,-5.712325,0.465596,-7.338079,-1.133991,1.144272,-4.040986,-7.204591,0.492098,6.871411,0.433546,5.878239,-9.534053,0.180381,-6.454562,-0.072406,9.905323,-6.105518,1.577904,-3.742969,-4.339118,3.991388,-0.012881,5.596817,-6.933241,9.595684,-1.775791,1.775237,-0.333890,-2.027492,7.074099,7.724394,2.345169,-7.353608,-8.603124,-9.803588,-8.770957,9.971884,7.636544,3.786978,-1.991931,-5.243823,8.949184,1.723049,-6.344735,-9.552870,9.665787,-5.758982,-1.920124,3.896440,6.912803,6.495365,5.842171,-8.401760,-6.306778,-6.091142,-0.489980,5.625209,5.413201,6.371038,-6.173499,2.533849,-0.101525,-8.077225,-4.689193,9.481195,6.446182,-7.302724,-5.174812,6.251554,-5.613178,4.043328,-4.966744,-2.912885,7.917070,3.211891,-7.845180,4.448244,8.012590,7.958872,0.333370,7.990267,6.173479,0.821230,7.896643,-0.732969,7.530533,-6.330836,-0.735748,8.348508,2.483602,6.592139,3.715918,-4.177765,-9.118157,6.866497,-6.179890,-5.668930,-0.810308,9.168280,0.883014,8.247195,6.294086,-4.551416,-6.289980,-6.920403,2.582166,3.794708,-6.318849,9.935066,9.031907,7.763209,2.945309,-3.618066,7.293807,3.985014,7.374629,7.000592,2.138853,8.934449,2.085494,4.639720,0.143248,-8.120871,-1.883039,9.032018,-3.340092,7.114767,-5.070991,7.564315,-2.055467,-6.844306,7.252083,-4.224332,-0.476216,-6.266101,3.017502,-5.650287,5.991466,2.482426,-2.672718,3.068325,7.013136,-9.245665,-4.161436,1.515394,2.537753,5.778415,-6.070876,8.803913,8.552800,-0.757905,3.634155,6.867375,3.724279,-8.126548,9.436864,-7.429530,-9.043503,6.364988,-0.520480,3.820729,-2.582207,-3.997252,1.466791,0.284988,-3.868430,0.010085,-8.059772,-6.646168,9.477193,5.969933,-2.697561,0.845396,7.599236,-7.805355,-7.673282,2.485237,-1.251477,8.835061,3.388602,-1.768989,-4.429624,5.854681,-3.400662,0.854478,-6.423740,0.239894,-7.228736,4.325138,1.363896,-8.602480,-3.031359,-9.533023,4.808196,-0.160548,0.963675,-3.402235,-9.187935,-3.460862,3.010590,6.284347,4.870534,2.829629,4.688974,0.063045,-5.250804,-1.703498,9.996892,4.205032,-3.964056,4.968668,-0.371925,-6.857754,4.430736,8.912284,-0.089098,-4.088925,5.246259,3.130119,-5.318596,1.099497,-0.768996,3.392996,4.985704,9.722287,-7.975462,4.210673,-2.161528,-1.923647,-4.550639,9.668712,-9.792872,-3.994263,3.568035,-9.321676,-1.226765,-5.910373,-0.189782,-7.564145,-8.677019,8.057254,-8.164051,6.023018,-9.503467,-8.500738,2.563412,3.736217,4.435444,-6.235782,-8.582053,1.761295,-8.092594,4.524480,2.340612,-0.280501,1.951309,9.132411,-7.453542,9.466102,-6.046261,-2.210840,4.636600,1.352330,6.662752,4.915785,-3.867103,3.800079,-0.577134,7.000434,-3.923519,2.141400,-5.146128,-5.347796,0.410714,8.035342,8.740773,9.263997,-9.156095,-7.830007,-4.170724,3.460340,-9.822425,-0.678065,2.530873,-0.688925,1.042070,-4.001412,-7.662682,9.311801,-1.664802,1.150337,-7.356178,-3.582080,7.542554,-3.298175,-6.919197,9.879928,-7.923187,0.434171,0.398144,-3.061748,2.174218,-3.416719,8.173615,3.094671,3.598136,3.092998,4.953728,-9.977518,-4.736808,0.845025,-2.283147,0.447322,-6.172313,-5.031495,7.166171,-3.951468,6.036589,-8.984429,-7.317748,-6.798139,9.862549,3.712496,0.695058,5.899773,7.395023,-4.509897,2.705998,-9.378656,-7.525799,-3.929688,7.039073,-0.284806,3.378525,3.742845,-2.885506,8.018774,-9.573798,1.200449,-7.011067,6.748931,3.608782,2.699865,-9.504923,-7.052001,2.654284,-1.100873,3.953142,7.308822,8.853636,0.290189,4.683695,3.960531,9.375340,9.300341,-5.895009,0.779578,8.278686,-4.109914,8.865665,-5.803633,6.160508,0.385526,-8.458512,-2.016399,-0.530535,8.488635,-2.300242,8.978251,5.251293,-6.423024,8.964628,9.979878,-8.323451,-2.285577,-0.748090,-2.843189,3.263714,5.806862,4.868384,-4.186265,7.340062,9.928991,-3.780077,8.370753,8.843658,8.303074,-2.218282,4.386547,1.375662,-2.545996,1.622406,3.588754,-1.193873,-6.158369,-0.934501,8.693500,-5.844351,-6.102076,2.484282,1.574143,5.018282,-1.747525,9.702078,-9.644551,2.456325,4.421404,-6.117688,-6.421357,8.468167,-9.982772,1.220660,4.101006,-8.148858,-8.827773,7.253434,-5.993707,3.662563,-2.738996,2.001560,6.223229,9.885787,9.288067,7.817696,3.244846,-5.524021,8.460854,6.644515,3.254080,-0.767040,-3.188327,3.971142,-3.893533,0.622784,-9.377752,5.317033,8.026584,-3.170071,-5.194956,-6.431105,-0.017432,5.887596,-9.490399,-5.231471,-7.118155,-2.667396,-0.163804,-8.739544,-0.286593,-8.658936,-8.896602,-2.583004,-4.433233,-7.874013,-0.061938,-4.109687,9.904831,-4.475554,9.724686,3.011102,6.827888,-7.593869,-7.262340,-3.961402,-0.388154,6.735453,0.963172,-3.772834,-8.009115,-5.344762,-2.654328,9.495967,6.914394,9.924544,-5.243045,-2.658693,-1.680097,3.029296,5.104604,5.725749,-6.015187,-1.139595,-0.446514,-2.918666,6.502548,-6.112006,5.639552,8.180825,0.817860,1.089926,-2.748321,-5.966231,-5.784299,4.785043,8.740955,6.313180,4.633013,2.010337,8.944902,-2.628315,7.774347,-4.055714,-9.071963,5.344346,-3.542620,7.080699,-9.380339,-8.058099,5.403797,9.734611,-5.535884,2.547706,-8.159824,-7.713906,-2.380521,1.250770,9.785915,-7.138584,6.546854,0.658275,6.212393,-9.029426,-5.642755,-2.800939,-8.913341,4.118951,7.575993,-5.849336,0.396987,4.042592,7.840601,7.054809,-3.470271,-2.121842,6.973404,6.398180,-9.303413,5.975979,-7.066984,2.773302,3.583314,-7.376682,5.809590,-6.086039,1.086487,-4.120067,-9.009026,5.378158,3.520945,7.719867,3.252703,2.517087,-3.295153,9.132368,9.119888,-4.387956,3.438952,5.241961,8.438059,7.742723,7.240490,-8.328975,-8.754497,-9.790609,8.389821,-5.361552,-2.114142,1.069079,-5.357412,-1.944641,7.816372,-8.674036,5.412224,1.798292,-2.212227,0.895162,-1.962568,4.549676,6.677165,-6.403261,1.822368,2.082835,6.854805,1.297568,1.655993,9.406624,-1.315629,5.090078,3.604971,-5.343433,-3.356564,5.344055,0.143617,8.086430,-0.051932,-5.815767,-7.309119,5.504533,-2.339152,-8.254210,-2.572682,-9.730312,0.561593,-5.944760,-9.619451,-8.717916,-3.513724,9.718100,4.725906,-7.388837,-8.962854,7.482816,8.276044,-7.811812,7.768154,0.808389,-4.410921,-8.993070,-2.375788,-8.274043,-5.311026,4.539943,-2.697292,-0.762913,8.735766,9.138564,9.634160,-6.439481,-4.124699,-9.988268,6.734318,7.954049,7.394337,-6.990017,0.079461,-7.806771,1.524966,-1.516536,-4.209287,3.780366,-1.046511,-7.742708,-0.441677,-3.646992,7.544613,-3.878283,-0.995939,2.616788,-4.249901,4.835383,-6.463483,6.405797,7.655388,-4.113816,-7.156868,1.761043,-5.194787,2.769259,1.107336,6.044921,-8.517983,3.603976,-0.167490,3.927783,-8.699441,-2.504040,-6.503238,8.510809,6.945713,-5.057545,8.600658,-2.231862,8.879436,-5.977342,1.947788,7.963959,-6.696021,6.850275,5.328886,5.137462,1.669895,7.694786,4.175400,-1.723430,-1.416521,-5.851059,-6.102973,4.921616,-2.295202,-1.312908,-3.394991,-4.480372,0.070256,6.979342,-8.230705,-8.617050,-2.558482,1.417588,-9.478134,-2.310705,-3.619039,2.182233,-3.442788,-7.772871,-6.850193,-2.005566,6.168467,1.932365,-8.087065,2.077417,2.419851,0.988952,4.171855,2.204685,-9.322485,-2.455814,8.455462,8.259120,4.203985,-4.603021,4.504988,-5.829081,7.559017,6.742223,-9.897605,-3.632112,-6.099201,7.023161,5.864585,-6.602228,-5.688205,-9.058386,-9.008612,8.888403,-3.247778,9.788666,3.900231,-5.456028,-6.922378,-8.528028,-2.261027,-0.808062,-4.723524,7.997496,1.222085,4.205044,-0.447711,9.949869,-6.267742,-1.132227,-8.212697,-8.924854,8.649275,5.971103,-6.191713,-7.756506,-8.206334,1.512991,-9.378868,-7.052693,-4.508036,-1.977995,-3.474967,0.424651,-9.509759,3.268676,-6.168203,-0.548453,-6.849078,4.228107,-9.476261,7.628962,-4.191695,1.334669,4.535920,-8.749913,-5.926682,0.494285,-4.762071,6.736885,-8.947927,-6.187331,-2.624028,0.846185,-9.756867,3.196768,-8.290097,7.141924,8.614247,-0.022640,7.834371,3.621318,5.964709,-4.003393,2.555436,-5.578451,-8.058953,-1.621357,-0.410798,8.348282,-5.119683,0.895568,3.765367,-8.765284,1.970668,-0.407521,5.498884,-1.785796,-5.192064,8.683562,-5.241072,7.585990,-2.011981,9.943278,9.463065,9.085795,7.972083,8.091450,5.880232,-2.559113,-9.786437,0.879205,-6.554745,-2.497479,-6.008013,-6.116688,5.634186,6.661848,-8.450516,-9.734619,7.903822,0.859171,-8.666987,-7.491067,-9.914810,1.845368,0.157799,5.916207,-1.874585,-8.155735,8.562912,-0.009000,-5.358207,-5.388366,-0.827712,5.072998,-8.531384,8.439581,5.459772,-3.619878,-2.593298,-2.071840,2.327406,2.547516,4.894472,-1.879233,-8.340220,1.741909,9.420827,4.688898,5.336934,7.578857,-3.034303,-6.375778,-7.958587,1.309660,-4.623893,-5.196847,5.709694,-2.729403,5.075927,3.068935,9.564664,3.982803,-4.622210,-6.233119,5.536817,9.693893,-6.417650,0.494261,6.489315,5.594199,-5.251745,3.659166,0.123411,-5.834959,-7.959303,6.002799,-7.900463,-7.966358,4.266963,-1.249089,1.134385,-0.493361,-5.900019,-6.113772,1.514258,4.806213,-7.432049,8.752055,-3.502260,-9.432587,-4.887011,-5.773048,-6.189406,9.848080,-9.958910,-6.258129,-8.944836,3.437158,-0.788995,-3.461415,-6.716484,4.716366,-1.145939,-3.369727,-1.122497,6.738545,-7.429402,-3.889731,8.071824,6.774417,7.984042,6.004635,-1.263176,-9.990270,-5.707382,-0.953306,4.786135,3.956952,3.632110,-5.674733,1.146230,-7.046036,-4.251741,-9.227276,-3.537580,0.195640,-0.379547,9.683895,6.146235,0.674552,-1.940679,-0.435704,-2.870213,1.980519,-4.432775,4.343721,-1.751965,3.315576,-9.480680,-0.122767,4.559273,5.329186,-8.398091,7.288242,-5.921859,0.104778,-5.615188,-1.438337,-9.127385,-3.737341,-8.255733,-3.348373,7.274945,4.441734,1.874763,3.311115,2.475896,-3.777106,7.860322,5.232031,6.113186,3.299971,8.095689,-4.228564,2.828536,-8.232095,-3.768294,-7.182127,-6.153308,-1.411991,2.040150,1.433232,-7.245381,-1.739584,9.974187,5.811686,9.712062,-9.598282,0.922196,-7.434755,-8.512571,-5.505711,7.419320,-0.660046,-9.845997,9.551161,-8.294644,-8.838322,3.828674,0.525783,-1.309631,1.764335,0.757360,-7.015514,-5.300269,5.538750,8.007742,2.011538,5.472567,6.226883,-4.311488,3.034493,3.120789,3.051301,7.212220,6.511858,-9.795237,6.082083,-5.129316,-1.086096,-1.288455,5.672017,8.004200,-6.353973,8.521826,-8.265754,-1.140319,-7.668715,3.166183,-6.762951,-0.460610,-4.751054,-8.370212,-0.219309,-1.557973,0.978942,6.143839,-7.660703,-5.497783,8.345294,-3.008753,0.865390,2.619787,-3.837639,-8.796981,9.320850,-1.996271,6.084937,0.256581,-7.337244,-4.276107,-5.767049,-0.588387,-2.180785,6.336392,-2.867755,4.889982,3.861887,-9.886740,7.968648,-1.195208,0.219953,-6.305658,-1.522714,0.837366,3.132585,-5.376924,7.845081,5.261471,3.882597,3.391144,-4.344868,-8.610220,2.369237,-8.063717,1.490676,-4.380609,5.264780,1.383243,-8.500120,-6.485852,-5.852624,-1.092169,-2.582372,6.289663,-2.228867,0.144118,4.612270,-4.130766,-5.387845,1.875127,-9.937404,3.784093,-7.002161,9.666917,3.796208,5.922201,-0.403554,3.744212,8.780497,5.385127,7.342436,-2.289540,-5.302743,6.220640,0.264101,-5.664148,-8.404102,-2.429826,-0.642259,-6.086027,3.911972,6.408240,9.800247,-4.093710,1.781497,-5.572280,8.772969,6.421006,-0.989372,-5.815874,7.536996,2.273618,-9.647578,-5.854618,7.443031,-1.438219,-3.064249,-4.807547,-4.677547,-8.453061,-3.001726,-4.037859,-3.763624,8.644445,1.337663,-4.040188,-0.231543,-7.844000,2.100597,3.803081,9.916698,-6.275157,3.342690,6.238860,3.897740,1.105290,6.482122,9.646563,3.178858,-5.641664,2.489311,2.640473,-1.731946,-8.999038,9.807228,-3.669871,-6.976754,-7.050063,6.244657,9.685123,-4.356467,1.712072,4.086121,5.677801,7.576027,8.595078,-4.431803,4.607959,-1.431513,3.232826,8.331782,0.543748,-6.752404,-2.193371,2.340108,-1.843841,-9.032833,7.161854,1.218907,0.808371,-7.350387,6.943656,3.478571,0.800976,-7.408024,3.185473,-7.235092,4.210878,4.360006,9.319810,-5.158635,-9.163551,8.824279,-5.504025,-6.678408,0.774490,-7.936910,3.980092,5.859097,2.633350,0.580232,-3.475905,1.094304,-2.021413,6.723527,-9.322195,-3.918525,-7.080754,-8.268388,-9.842004,-7.650014,-0.990921,-2.283377,4.898574,-8.742027,4.679165,0.045640,-4.221823,-7.018177,3.859835,-0.711531,1.345734,-2.451038,-3.303068,-1.044261,2.495586,-6.787380,4.323143,-0.088402,3.229431,1.594528,-1.511650,-4.194260,-6.237761,-3.109203,-2.154760,0.084137,7.100230,0.861548,-8.178999,-8.020129,2.092229,0.018862,9.208411,0.720143,7.287239,0.171347,3.849083,-7.507188,-1.046126,-8.319462,1.323417,-0.986438,7.756920,-8.330873,2.234268,-6.557929,1.310993,4.743997,4.797546,7.424135,-2.497760,-7.109921,-8.392837,4.919236,6.565477,4.770296,8.572988,6.731668,-1.411955,-8.139823,-4.790214,-2.761968,1.737802,-6.781370,-4.889686,7.937088,9.797624,-7.953850,-0.762567,-2.812394,8.375176,-5.613762,-7.476725,-7.318133,9.183310,-7.918475,1.048789,9.462020,4.819009,9.834975,-2.991893,-7.450569,-9.652402,9.252037,-0.573784,2.773433,-7.492330,-4.642772,1.069452,2.720219,1.401246,7.243592,-1.924964,8.176589,-8.401868,3.715404,3.136632,-5.688117,-5.928500,-9.234099], dtype = "float64")#candidate|4839|(1664,)|const|float64
call_4837 = func_2976_call(relay.reshape(var_4838.astype('float64'), [1, 8, 13]), relay.reshape(const_4839.astype('float64'), [16, 8, 13]), )
call_4840 = func_2976_call(relay.reshape(var_4838.astype('float64'), [1, 8, 13]), relay.reshape(const_4839.astype('float64'), [16, 8, 13]), )
uop_4855 = relay.log10(call_4837.astype('float64')) # shape=(16, 8, 13)
uop_4857 = relay.log10(call_4840.astype('float64')) # shape=(16, 8, 13)
uop_4860 = relay.acosh(uop_4855.astype('float32')) # shape=(16, 8, 13)
uop_4862 = relay.acosh(uop_4857.astype('float32')) # shape=(16, 8, 13)
func_767_call = mod.get_global_var('func_767')
func_771_call = mutated_mod.get_global_var('func_771')
var_4877 = relay.var("var_4877", dtype = "int16", shape = ())#candidate|4877|()|var|int16
var_4878 = relay.var("var_4878", dtype = "int16", shape = (7,))#candidate|4878|(7,)|var|int16
call_4876 = relay.TupleGetItem(func_767_call(relay.reshape(var_4877.astype('int16'), []), relay.reshape(var_4878.astype('int16'), [1, 7]), ), 2)
call_4879 = relay.TupleGetItem(func_771_call(relay.reshape(var_4877.astype('int16'), []), relay.reshape(var_4878.astype('int16'), [1, 7]), ), 2)
output = relay.Tuple([uop_4823,var_4838,const_4839,uop_4860,call_4876,var_4877,var_4878,])
output2 = relay.Tuple([uop_4823,var_4838,const_4839,uop_4862,call_4879,var_4877,var_4878,])
func_4886 = relay.Function([var_4822,var_4838,var_4877,var_4878,], output)
mod['func_4886'] = func_4886
mod = relay.transform.InferType()(mod)
mutated_mod['func_4886'] = func_4886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4886_call = mutated_mod.get_global_var('func_4886')
var_4888 = relay.var("var_4888", dtype = "float64", shape = (10, 16))#candidate|4888|(10, 16)|var|float64
var_4889 = relay.var("var_4889", dtype = "float64", shape = (1, 104))#candidate|4889|(1, 104)|var|float64
var_4890 = relay.var("var_4890", dtype = "int16", shape = ())#candidate|4890|()|var|int16
var_4891 = relay.var("var_4891", dtype = "int16", shape = (7,))#candidate|4891|(7,)|var|int16
call_4887 = func_4886_call(var_4888,var_4889,var_4890,var_4891,)
output = call_4887
func_4892 = relay.Function([var_4888,var_4889,var_4890,var_4891,], output)
mutated_mod['func_4892'] = func_4892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4141_call = mod.get_global_var('func_4141')
func_4143_call = mutated_mod.get_global_var('func_4143')
call_4903 = relay.TupleGetItem(func_4141_call(), 0)
call_4904 = relay.TupleGetItem(func_4143_call(), 0)
func_3911_call = mod.get_global_var('func_3911')
func_3914_call = mutated_mod.get_global_var('func_3914')
const_4911 = relay.const([[2.548075,5.495246],[9.250112,3.026489],[-6.540404,4.650259],[-4.180315,-0.780434],[9.151486,8.553728],[9.542208,-7.351356],[7.810229,7.960263],[-3.098088,0.502119],[-8.567550,6.957772],[-0.584488,-1.480014],[-3.299367,8.133227],[-2.545669,-4.159736],[5.759035,-2.264600],[3.735643,1.101662],[-6.358775,-2.955318],[8.808311,-2.966128],[8.339149,7.583963],[-4.134929,-2.950674],[6.969846,-9.665875],[6.148138,-6.923990],[-0.870405,9.414340],[9.448770,-5.021508],[-3.249933,0.280056],[-8.683124,2.298398],[2.566093,2.009481],[-3.915638,-3.020987],[4.971358,-7.700604],[7.160256,-9.036071],[0.884695,5.140316],[-1.117445,-2.767455],[3.455522,9.351369],[-3.507691,0.905343],[7.157207,6.461883],[-6.367084,-8.883469],[-2.828567,2.816184],[0.655279,-3.129307],[4.985667,1.913764],[3.965229,-2.198114],[7.936879,2.747554],[-1.443980,3.551463],[3.371772,-6.905955],[0.112913,-1.187010],[9.812987,0.004943],[8.026437,2.528767],[-0.051921,-4.123122],[-0.921800,-8.312663],[-6.220564,1.407619],[-1.107847,2.842574],[-0.636383,9.011839],[-3.066588,2.919838],[1.002121,-1.504625],[-2.282144,-7.528233],[-7.176948,2.006818],[5.484034,2.974111]], dtype = "float32")#candidate|4911|(54, 2)|const|float32
call_4910 = relay.TupleGetItem(func_3911_call(relay.reshape(const_4911.astype('float32'), [3, 12, 3])), 0)
call_4912 = relay.TupleGetItem(func_3914_call(relay.reshape(const_4911.astype('float32'), [3, 12, 3])), 0)
uop_4941 = relay.tan(const_4911.astype('float32')) # shape=(54, 2)
bop_4944 = relay.logical_and(uop_4941.astype('bool'), relay.reshape(const_4911.astype('bool'), relay.shape_of(uop_4941))) # shape=(54, 2)
func_3408_call = mod.get_global_var('func_3408')
func_3409_call = mutated_mod.get_global_var('func_3409')
call_4948 = func_3408_call()
call_4949 = func_3408_call()
uop_4950 = relay.tan(call_4910.astype('float32')) # shape=(600,)
uop_4952 = relay.tan(call_4912.astype('float32')) # shape=(600,)
func_4366_call = mod.get_global_var('func_4366')
func_4369_call = mutated_mod.get_global_var('func_4369')
const_4955 = relay.const([9.265086,2.592602,-3.797813,4.914184,2.648839,1.732590,-9.031179,-9.654514,-7.195061,1.453333,7.749606,-1.089373,-0.814073,2.775973,9.355809,-9.739157,-0.737655,-7.308179,-7.527432,3.117840,-7.195882,-1.722663,-9.807972,0.706327,-0.842957,5.397345,-9.347323,0.157107,-2.591042,-9.455321,1.763214,-1.928077,-1.138795,-3.278349,-1.355704,-5.843254,-0.632073,3.067029,1.726144,-0.386754,-2.647178,1.138574,8.079889,1.116868,-8.719902,-8.697598,9.218336,4.313155,6.875014,-2.584750,1.456933,-8.894492,8.561281,-2.605204,-0.936283,0.957118,-4.085642,8.311077,7.779585,4.733275,-1.611441,9.966896,-3.277690,-3.193707,-2.700204,7.302697,9.563110,-6.481152,-3.272051,-1.226419,1.072399,2.512003,-6.889840,3.514350,7.258623,0.548065,-7.571331,5.037636,3.047697,-8.138227,-2.807187,7.824487,-6.969966,3.403259,-5.519076,7.331022,3.068721,-9.099399,-6.238894,1.870246,-0.755009,6.070909,-6.393078,-0.079312,-6.244544,2.145798,-7.036895,6.473379,-9.586267,5.544481,-2.087162,-6.329383,8.600790,0.480300,6.974814,-9.338762,-1.272521,-4.447579,-3.157064,-6.985720,-3.342812,-6.474201,5.343479,2.757721,-5.772739,-2.069343,4.784219,-2.363827,8.877065,-4.499415,-8.328161,4.573342,5.836353,6.296985,-0.409703,-6.903864,-6.238098,6.811853,-8.774188,5.076656,-1.044107,0.492438,6.411399,-9.007546,-0.949634,4.973376,0.781345,2.732131,-5.907846,0.226318,-4.895108,0.543706,-4.883868,-4.175685,4.480284,8.797701,-0.381083,-1.453385,-9.347759,-1.829581,4.452892,9.307976,-4.468537,8.622251,-5.068216,4.325982,7.041837,4.843697,-3.907571,-9.542445,4.961175,2.531791,0.722063,9.225797,-3.649469,-4.032109,5.671105,2.470606,-7.506475,9.076899,0.183795,1.587454,0.063642,-5.412362,5.188287,-7.582580,-7.452972,-2.648036,4.477021,2.043715,9.832504,8.586234,3.194131,2.596855,-2.728875,-9.671188,3.424390,-0.785347,-5.397800,-4.377864,7.255461,3.238724,-8.886943,8.188407,9.100209,-1.016214,-2.354087,-1.008515,-6.371751,6.452181,-7.394597,-9.085202,-9.543638,-9.799872,9.836690,-1.041864,7.793716,-1.163832,2.228814,0.561027,-3.864683,3.206696,-8.615357,-8.143358,4.698197,9.904749,-3.787160,-5.907918,-2.620760,2.950664,2.479908,-3.569638,1.710718,3.339674,8.107763,-6.533511,-6.159755,-2.511826,8.658329,3.350068,1.015783,-6.344688,-2.309045,-9.525587,9.218209,-9.290305,7.536698,-7.178475,1.143488,3.053095,-5.343308,-0.934582,3.470204,6.673830,6.904544,-2.663748,6.617429,-1.597575,5.130205,-4.102253,1.412206,9.743310,-1.890063,5.022310,7.799078,-1.359883,-4.904231,-2.985997,6.797752,-0.361419,-5.678186,5.209051,2.803193,2.831408,-2.277907,-0.315615,-7.070562,-9.458932,6.046954,-9.753665], dtype = "float64")#candidate|4955|(270,)|const|float64
call_4954 = relay.TupleGetItem(func_4366_call(relay.reshape(const_4955.astype('float64'), [10, 9, 3]), relay.reshape(const_4955.astype('float64'), [10, 9, 3]), ), 2)
call_4956 = relay.TupleGetItem(func_4369_call(relay.reshape(const_4955.astype('float64'), [10, 9, 3]), relay.reshape(const_4955.astype('float64'), [10, 9, 3]), ), 2)
output = relay.Tuple([call_4903,bop_4944,call_4948,uop_4950,call_4954,const_4955,])
output2 = relay.Tuple([call_4904,bop_4944,call_4949,uop_4952,call_4956,const_4955,])
func_4961 = relay.Function([], output)
mod['func_4961'] = func_4961
mod = relay.transform.InferType()(mod)
mutated_mod['func_4961'] = func_4961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4961_call = mutated_mod.get_global_var('func_4961')
call_4962 = func_4961_call()
output = call_4962
func_4963 = relay.Function([], output)
mutated_mod['func_4963'] = func_4963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_5010 = relay.TupleGetItem(func_3147_call(), 0)
call_5011 = relay.TupleGetItem(func_3149_call(), 0)
uop_5012 = relay.acosh(call_5010.astype('float64')) # shape=(3, 12, 3)
uop_5014 = relay.acosh(call_5011.astype('float64')) # shape=(3, 12, 3)
output = uop_5012
output2 = uop_5014
func_5023 = relay.Function([], output)
mod['func_5023'] = func_5023
mod = relay.transform.InferType()(mod)
mutated_mod['func_5023'] = func_5023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5023_call = mutated_mod.get_global_var('func_5023')
call_5024 = func_5023_call()
output = call_5024
func_5025 = relay.Function([], output)
mutated_mod['func_5025'] = func_5025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_5073 = relay.TupleGetItem(func_3147_call(), 0)
call_5074 = relay.TupleGetItem(func_3149_call(), 0)
output = call_5073
output2 = call_5074
func_5075 = relay.Function([], output)
mod['func_5075'] = func_5075
mod = relay.transform.InferType()(mod)
output = func_5075()
func_5076 = relay.Function([], output)
mutated_mod['func_5076'] = func_5076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_5077 = relay.TupleGetItem(func_3508_call(), 0)
call_5078 = relay.TupleGetItem(func_3510_call(), 0)
func_4213_call = mod.get_global_var('func_4213')
func_4214_call = mutated_mod.get_global_var('func_4214')
call_5085 = relay.TupleGetItem(func_4213_call(), 0)
call_5086 = relay.TupleGetItem(func_4214_call(), 0)
output = relay.Tuple([call_5077,call_5085,])
output2 = relay.Tuple([call_5078,call_5086,])
func_5093 = relay.Function([], output)
mod['func_5093'] = func_5093
mod = relay.transform.InferType()(mod)
output = func_5093()
func_5094 = relay.Function([], output)
mutated_mod['func_5094'] = func_5094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5114 = relay.var("var_5114", dtype = "float64", shape = (11, 8, 14))#candidate|5114|(11, 8, 14)|var|float64
uop_5115 = relay.tan(var_5114.astype('float64')) # shape=(11, 8, 14)
output = relay.Tuple([uop_5115,])
output2 = relay.Tuple([uop_5115,])
func_5127 = relay.Function([var_5114,], output)
mod['func_5127'] = func_5127
mod = relay.transform.InferType()(mod)
var_5128 = relay.var("var_5128", dtype = "float64", shape = (11, 8, 14))#candidate|5128|(11, 8, 14)|var|float64
output = func_5127(var_5128)
func_5129 = relay.Function([var_5128], output)
mutated_mod['func_5129'] = func_5129
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5136 = relay.var("var_5136", dtype = "float64", shape = (11, 11, 7))#candidate|5136|(11, 11, 7)|var|float64
uop_5137 = relay.asin(var_5136.astype('float64')) # shape=(11, 11, 7)
uop_5156 = relay.atan(var_5136.astype('float64')) # shape=(11, 11, 7)
output = relay.Tuple([uop_5137,uop_5156,])
output2 = relay.Tuple([uop_5137,uop_5156,])
func_5163 = relay.Function([var_5136,], output)
mod['func_5163'] = func_5163
mod = relay.transform.InferType()(mod)
var_5164 = relay.var("var_5164", dtype = "float64", shape = (11, 11, 7))#candidate|5164|(11, 11, 7)|var|float64
output = func_5163(var_5164)
func_5165 = relay.Function([var_5164], output)
mutated_mod['func_5165'] = func_5165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_5170 = relay.TupleGetItem(func_3508_call(), 0)
call_5171 = relay.TupleGetItem(func_3510_call(), 0)
func_5127_call = mod.get_global_var('func_5127')
func_5129_call = mutated_mod.get_global_var('func_5129')
const_5173 = relay.const([4.134498,-8.590506,3.266524,-4.346305,-0.940527,-9.717084,-3.201268,-1.867304,-5.362319,3.157879,-3.841922,-3.751428,-8.487883,-1.093265,-5.086915,-4.756650,-2.815264,5.165318,-1.283648,1.784205,-5.332414,-3.668213,2.320459,-0.678247,3.087460,-3.861368,-1.428981,5.715858,0.701033,7.543852,7.353193,-9.322231,-8.480366,5.566249,0.526599,5.408297,-4.658907,-3.604719,-9.884820,9.430449,-2.067212,6.732110,-1.956344,-7.666891,6.515872,-3.986351,1.864446,-8.397683,-7.141987,1.182853,-0.073696,3.032787,-8.265500,-0.173684,-2.225128,-2.033656,3.973457,-4.792600,-6.668396,-0.040597,-9.228793,-3.337186,4.277834,7.164262,-4.073227,6.524627,5.384904,-6.551254,4.514452,8.933478,-2.963836,-3.355805,2.438594,-5.733242,4.580793,4.029511,7.075149,-4.886466,-8.075127,-6.707757,-4.694569,-1.568502,-2.291112,3.935649,7.542510,-7.142768,-4.846175,-8.090998,7.953482,-0.790465,8.012507,-8.041083,0.957320,6.816858,-8.782814,7.055584,3.682243,-3.410702,-7.095395,2.022656,-9.501302,8.193826,1.185160,7.947902,-3.648030,2.004768,1.836408,-8.623963,-1.841598,1.017297,0.307568,3.165782,-1.376110,6.836046,0.701225,-5.619507,-7.071236,4.275180,9.407527,-7.266039,-7.454705,5.981180,4.620453,-6.409517,8.704697,-1.940235,-6.409757,-2.768698,1.701147,3.805490,-0.297729,6.644738,-9.671476,-5.030028,9.094548,8.816408,5.952647,6.551021,3.890738,-5.163126,0.810645,1.008914,5.036901,-5.054891,8.054951,3.559268,-6.423691,-6.256595,6.786806,-8.231509,0.149029,-8.262364,0.785164,8.333791,-9.953656,1.922294,-7.325315,6.153409,-3.640260,2.843858,-8.071249,-3.202028,0.565730,6.482768,5.681746,8.843064,6.337936,6.746457,3.739735,6.217686,3.088917,-0.200638,-0.373733,5.377978,8.791227,-6.779229,8.262212,-8.304442,-0.453818,-0.872335,-1.920990,-4.388018,1.251707,-9.429177,2.090639,-6.232839,-9.546680,-3.819977,5.041525,-7.849744,-2.847829,-1.670385,1.777110,-1.590207,-7.987851,7.019480,-3.074680,-3.416807,-1.350246,5.218513,7.984505,-9.764969,-1.099854,-3.068758,-3.199802,-5.732216,4.681287,-3.346786,-7.678735,-4.744920,1.499576,8.844143,-2.230619,-0.776321,-4.021411,-0.653270,8.392358,6.426648,8.877193,7.498672,-6.441708,1.755283,-4.436492,-6.675699,-6.822677,7.721205,4.625778,-7.112060,9.964963,-6.374425,-1.839504,4.694633,2.682438,6.141266,-1.716196,-2.257386,-5.941531,-7.091928,6.294673,8.421444,-1.647187,-9.037882,7.972862,8.494966,6.952194,-6.754057,-4.579997,3.961596,9.492450,-6.384511,-4.027125,-6.149755,-3.926279,9.678294,-2.223543,-2.224407,-0.971848,-2.513960,9.164097,-1.607017,7.182158,-7.152777,-1.786892,4.815444,-5.023100,8.026144,-8.648908,2.551691,-4.942872,-9.474714,-8.117346,5.513836,8.136692,-1.349641,4.693468,7.836124,-0.261798,-6.484936,-1.038847,-4.416022,-2.174743,9.958038,7.744486,8.886969,5.926155,-9.203375,-4.892534,-0.248237,0.733380,-9.199837,0.530269,9.151682,9.210758,-9.159159,2.295616,-0.615100,-0.620567,-2.135443,9.583504,-4.341364,-1.522105,-8.534934,-8.513167,-8.472635,4.392608,9.275476,5.162807,-2.994619,-6.530757,-1.376198,5.628744,0.295268,-5.448200,-1.427230,-3.880605,-2.849606,2.982172,1.456479,-8.851113,-2.591674,4.649969,-7.131518,-3.979275,9.880092,-3.934093,6.487369,9.592969,0.945265,-7.438787,6.174202,-2.842350,3.895744,-9.912644,-3.209877,4.166837,-3.730831,-7.314390,8.024404,-6.566054,8.125331,-2.164945,-0.232452,-2.509026,8.035248,3.328116,5.640706,-0.996726,-6.158973,2.029928,8.664493,5.388805,1.887221,0.348121,-5.598427,-7.286017,-5.720075,-3.680733,-9.728040,-3.999360,-9.765552,-0.203195,-6.844450,-1.280861,3.753617,1.130254,-1.695218,-5.889472,-6.080473,-6.550151,5.665686,-7.450419,9.086346,2.445938,5.019090,3.595141,9.005458,7.408011,1.167781,-0.312091,-5.335509,5.059942,-5.213156,-8.561373,2.725724,-1.518739,6.234562,-8.011336,0.274130,-8.729419,-8.701629,-7.665206,2.015909,3.939234,-0.058447,0.155314,2.547423,5.889848,2.178962,-4.312549,8.742649,7.128404,1.232982,7.120055,4.451227,-7.242053,-2.079172,-9.957619,-0.355134,-4.757388,4.844980,0.754321,-3.997257,2.973451,3.917462,8.068659,-5.132548,7.503883,-6.644712,-9.736790,7.649903,7.488140,-9.020494,1.232353,1.455863,8.609518,-3.944622,0.727978,0.653406,-5.013921,-0.113494,0.218998,-2.099767,1.705086,-5.145852,0.888927,-1.330560,5.813773,-1.280836,1.500937,-0.010864,-0.140142,-8.073714,0.248451,-1.137827,-4.876663,3.836058,2.539216,-1.866386,4.138329,1.669596,-8.277786,2.141943,-3.376032,0.408951,-4.698425,-6.255700,-4.291110,-7.671760,-1.926883,2.861707,-7.604124,8.860231,-8.529056,-7.077088,-7.963990,-7.350988,1.227796,-5.382040,3.845059,0.381602,2.582441,9.123843,-7.301867,3.132471,-1.548028,7.542587,-1.014695,2.359455,9.011076,-9.135510,9.625698,-3.867875,-8.175843,-4.056705,-6.551442,4.363832,2.861162,6.378852,3.204977,-7.331695,5.543285,-4.521822,-0.349620,4.244062,6.727181,3.744036,-6.001131,5.792431,-4.480455,1.338953,3.759470,-3.871411,2.527214,1.040227,2.312976,-5.560275,8.715546,-8.996380,-9.768529,9.071205,3.854622,-4.729825,8.643370,-5.379467,0.757404,-7.908222,9.319115,3.316075,5.058172,2.113116,1.993232,6.238579,-7.193767,-3.260860,1.696390,-4.033973,9.024937,5.940989,-7.922741,-0.208306,8.790521,-1.326142,-0.654005,4.631810,-8.455890,-0.164292,-4.577120,1.480264,5.026043,-0.728087,4.060625,7.073457,7.411180,8.950299,-4.035929,-8.857728,6.315265,-0.745104,-2.780996,2.678673,-8.664904,-6.985415,1.288649,1.512372,-7.795945,-9.086341,-5.874279,-8.802123,-9.984167,7.866350,2.024590,-4.718995,6.626107,-4.005098,-0.756591,-6.823401,3.977921,1.345294,-0.971596,5.137312,-1.091792,4.326529,9.452807,7.384958,6.635219,7.122306,-3.679785,3.234995,-5.856952,2.170871,7.712392,-1.547647,2.848474,-8.484180,-1.241219,-1.883509,7.921779,-7.349239,9.546978,-5.802122,-2.304234,8.225339,5.032680,-3.055209,8.681481,-4.842510,-6.459749,4.961545,-3.716250,3.687677,-1.412351,-2.913221,2.695618,-3.584717,-7.951767,-3.254061,-3.423145,9.194604,-1.342561,-4.379037,4.729462,6.978576,9.245076,5.925884,-9.957860,-7.643742,-7.580384,-3.075656,3.420780,-3.562194,2.173343,6.816409,9.399732,9.169594,-5.064491,4.864540,-6.053612,6.995331,1.069855,4.169180,-6.378238,-7.598103,-7.945188,-2.540406,-9.128572,5.657584,4.926193,1.283480,6.985891,7.026774,-1.415208,-2.586361,0.219393,-7.999627,-5.942557,-9.975042,-5.053977,-3.287039,4.459436,-9.126537,4.013092,1.895384,-9.583711,2.826331,8.978290,-6.391424,1.293003,-8.202477,-1.601445,-8.992720,-2.926606,8.722851,2.932710,-2.706249,0.156605,-3.772357,-0.492093,8.090233,2.172786,9.630971,4.742287,-6.077760,-8.420373,5.318874,-7.663354,6.186749,-8.924141,7.205900,-6.947149,-7.627938,-0.099588,9.786107,-2.550038,-8.733974,0.654388,-4.088954,8.582503,-3.902637,1.190263,-5.045788,6.383968,6.911782,6.190591,3.487383,-0.938739,1.994889,7.235884,1.719810,7.614221,5.836895,2.120798,-9.032597,-8.590855,-9.124963,-1.503153,4.161422,2.704776,-3.663361,2.275854,-1.875159,2.061353,4.982414,-7.494984,8.411552,-2.971493,4.038935,-1.629994,-0.150840,-8.476206,7.879577,5.789096,-2.623000,7.712983,9.245705,-6.304516,-9.528153,0.396827,-7.246740,-7.297426,-2.342950,-8.676306,3.451882,6.078984,-5.577249,-9.216629,-7.051144,-0.617200,-5.945148,9.105713,2.962529,-3.937978,-0.774284,0.588070,9.458590,-5.737065,-3.982766,1.815864,1.967903,8.166476,-2.427278,1.374200,2.490948,0.265579,4.736443,-7.177943,6.206004,-8.676796,-2.697054,-5.263877,-2.393305,3.463079,-1.975811,-3.749527,5.864954,7.782706,7.636909,9.007719,-3.827455,1.443478,6.721827,-8.935093,-1.764347,-5.929656,-0.762786,-4.458997,3.047911,2.345719,3.138496,-4.315302,5.070055,-9.347365,-3.963718,-8.225446,5.101460,2.311252,1.369990,0.569055,-1.466962,-0.492517,-7.721926,2.927410,9.108313,5.343535,-9.443321,1.991423,4.732890,9.711332,7.683279,8.620719,6.697101,-7.114712,-5.205083,-7.291305,7.775993,-8.541937,9.310206,-1.719292,-3.843897,5.246034,9.162746,8.833564,5.039860,-2.686884,-8.057526,4.012619,-9.214352,-6.767628,5.859949,-8.595975,6.780421,-3.138834,-1.442996,6.627345,0.720908,-7.195035,-7.568808,4.574417,-1.933796,-1.575106,4.909294,-4.114689,2.116340,1.607764,8.977267,-6.739268,-0.592210,6.762852,4.637176,3.363399,-0.288429,4.175584,2.966458,-9.471510,-1.196000,-2.911285,-4.723482,-3.967408,1.186106,-3.693437,6.447933,-5.213517,0.726593,-1.058670,-3.592620,7.801897,6.561155,1.160919,-6.777622,-2.488776,8.024124,-3.351986,4.183873,1.572275,-5.331626,8.685800,-6.575140,8.061613,-8.913018,-7.424985,-6.692083,0.536912,-8.148042,-9.209104,-8.092872,-7.371056,-6.123490,1.166610,6.402991,-3.718281,-2.048391,4.982058,3.855248,-7.025868,-1.904196,2.675809,7.788226,2.517133,1.586162,-7.610259,-0.779466,6.123280,9.548778,0.185439,-9.995954,0.226534,4.419381,7.936265,0.206232,-6.820557,6.156116,-3.651064,-7.564279,-3.674023,-7.757032,5.968451,4.485031,5.661332,7.174812,0.358441,-8.961327,-4.942879,7.539067,6.936498,-9.012886,5.541157,5.729153,-8.585429,5.183955,8.608609,3.480635,-6.974487,-2.272035,7.360128,-9.253764,5.766705,4.507714,4.613780,2.318872,-8.199231,-0.432145,9.310400,7.502362,-3.684524,6.856270,-3.403678,-1.581683,1.631375,-3.374881,6.702497,-0.134419,-3.115615,-6.364548,-0.069916,-7.934741,6.880385,-5.239794,-8.263012,-0.207440,-1.133509,-5.631138,-3.269929,-4.330142,6.618124,2.993993,8.836477,4.644888,3.761085,4.149765,-9.635274,-2.309542,5.510627,-7.807274,2.655036,-5.385026,-6.727706,-2.788427,9.753874,3.734360,-8.960971,4.160154,-9.729342,6.535519,0.106474,4.734403,-3.937011,8.239782,6.451385,5.059478,7.659328,-8.062787,-0.569104,-9.383016,6.861133,3.965240,-5.907363,-4.089305,3.379190,9.079522,-2.951042,-7.192535,-5.412708,-0.296609,-7.264965,-5.496772,2.550272,4.115475,-5.305232,-1.620113,1.186161,8.490393,-7.409955,-4.430620,9.673761,-4.032018,3.967003,-8.902136,4.488132,8.704494,-3.837078,8.829319,-4.969891,1.601270,-9.041702,5.819613,6.526568,-4.253920,-0.847674,-2.210037,-1.528739,3.866730,8.470916,8.065187,0.562009,-6.526902,7.773806,1.673833,7.804452,-0.172647,-0.312086,6.814584,-4.913463,-4.517691,0.814863,-9.971654,7.057249,8.186052,3.315401,8.675323,3.136049,-7.701155,9.841667,-3.580050,-8.677377,7.082746,-8.419179,9.098389,-1.082446,1.799751,-9.550501,6.349879,-8.129233,-3.903092,9.293355,-8.447604,-8.494350,3.458092,-8.818204,-9.548963,-7.315973,-3.599270,-1.388520,7.756095,7.581376,-9.216116,-9.719409,5.857962,-3.715904,-0.298962,-2.192456,-7.056378,6.866336,-1.775620,-2.738367,3.850167,-3.054554,9.923731,1.170915,2.125861,-3.348576,-8.709166,5.073562,9.750632,7.101801,-7.361130,-0.465979,-6.606377,-1.758788,7.709146,3.036598,-5.858288,-9.769470,8.478366,-8.161908,-1.732117,-9.209775,-1.174995,5.664617,-4.112399,5.321324,-2.034799,7.713381,-6.764019,9.099247,-7.358512,-4.254113,3.690808,4.927174,-2.718507,4.018511,-8.234319,8.810869,-1.417276,-7.293278,1.139548,7.274304,7.499922,1.587648,-4.689781,9.273898,1.705104,0.052025,0.811400,6.249432,3.126641,-4.052742,1.329230,-0.906172,-7.740358,-1.717264,-6.723068,7.063617,-1.958054,9.225080,-5.989467,-7.551020,-8.548539,-5.344117,-1.316921,3.871213,-5.944241,8.829082,4.090151,7.858512,-4.589384,-8.267157,9.696057,-9.204473,-5.172317,5.045809,-0.802529,-1.664563,2.988757,-6.439357,8.871866,5.805059,-5.329297,4.095105,-7.528876,5.064608,-0.136770,-7.685643,-0.711049,2.959583,-1.288260,8.361322,-7.590162,-5.748946,-9.450959,3.678126,-8.913335,3.956509,2.843695,5.818892,-8.221044,-2.987310,-8.772635,-8.224369,0.244297,4.793880,-9.174254,8.273366,-4.840646,7.338375,-8.362976,-8.172385,3.442098,8.734482,-2.956095,3.430125,-9.539093,1.082043,-7.948423,5.758854,-6.407990,8.848999,8.275332,0.327267,-4.831090,-7.300600,-7.503204,-0.849662,-9.338242,-7.003234,-2.427679,7.838899,-5.025568,4.332824,5.518769,-9.449081,9.106661,-6.882064,-1.068780,-8.940351,-7.178195,-0.351233,-7.354421,3.366621,-8.901827,2.370402,5.706696,2.925368,-3.278995,-6.262461,9.099958,9.178210,-6.293061,7.804779,2.598839,-4.648841,-8.275489,-0.678849,9.413523], dtype = "float64")#candidate|5173|(1232,)|const|float64
call_5172 = relay.TupleGetItem(func_5127_call(relay.reshape(const_5173.astype('float64'), [11, 8, 14])), 0)
call_5174 = relay.TupleGetItem(func_5129_call(relay.reshape(const_5173.astype('float64'), [11, 8, 14])), 0)
func_5023_call = mod.get_global_var('func_5023')
func_5025_call = mutated_mod.get_global_var('func_5025')
call_5187 = func_5023_call()
call_5188 = func_5023_call()
output = relay.Tuple([call_5170,call_5172,const_5173,call_5187,])
output2 = relay.Tuple([call_5171,call_5174,const_5173,call_5188,])
func_5191 = relay.Function([], output)
mod['func_5191'] = func_5191
mod = relay.transform.InferType()(mod)
output = func_5191()
func_5192 = relay.Function([], output)
mutated_mod['func_5192'] = func_5192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_5225 = relay.TupleGetItem(func_3508_call(), 0)
call_5226 = relay.TupleGetItem(func_3510_call(), 0)
var_5227 = relay.var("var_5227", dtype = "float64", shape = (3, 12, 3))#candidate|5227|(3, 12, 3)|var|float64
bop_5228 = relay.equal(call_5225.astype('bool'), relay.reshape(var_5227.astype('bool'), relay.shape_of(call_5225))) # shape=(3, 12, 3)
bop_5231 = relay.equal(call_5226.astype('bool'), relay.reshape(var_5227.astype('bool'), relay.shape_of(call_5226))) # shape=(3, 12, 3)
output = relay.Tuple([bop_5228,])
output2 = relay.Tuple([bop_5231,])
func_5253 = relay.Function([var_5227,], output)
mod['func_5253'] = func_5253
mod = relay.transform.InferType()(mod)
mutated_mod['func_5253'] = func_5253
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5254 = relay.var("var_5254", dtype = "float64", shape = (3, 12, 3))#candidate|5254|(3, 12, 3)|var|float64
func_5253_call = mutated_mod.get_global_var('func_5253')
call_5255 = func_5253_call(var_5254)
output = call_5255
func_5256 = relay.Function([var_5254], output)
mutated_mod['func_5256'] = func_5256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3982_call = mod.get_global_var('func_3982')
func_3984_call = mutated_mod.get_global_var('func_3984')
call_5300 = func_3982_call()
call_5301 = func_3982_call()
uop_5304 = relay.log2(call_5300.astype('float32')) # shape=(10, 9, 1)
uop_5306 = relay.log2(call_5301.astype('float32')) # shape=(10, 9, 1)
func_4262_call = mod.get_global_var('func_4262')
func_4267_call = mutated_mod.get_global_var('func_4267')
var_5310 = relay.var("var_5310", dtype = "int32", shape = (48,))#candidate|5310|(48,)|var|int32
var_5311 = relay.var("var_5311", dtype = "uint8", shape = (4, 84))#candidate|5311|(4, 84)|var|uint8
var_5312 = relay.var("var_5312", dtype = "float64", shape = (3, 90))#candidate|5312|(3, 90)|var|float64
call_5309 = relay.TupleGetItem(func_4262_call(relay.reshape(var_5310.astype('int32'), [12, 4, 1]), relay.reshape(var_5311.astype('uint8'), [336,]), relay.reshape(var_5312.astype('float64'), [270,]), ), 3)
call_5313 = relay.TupleGetItem(func_4267_call(relay.reshape(var_5310.astype('int32'), [12, 4, 1]), relay.reshape(var_5311.astype('uint8'), [336,]), relay.reshape(var_5312.astype('float64'), [270,]), ), 3)
output = relay.Tuple([uop_5304,call_5309,var_5310,var_5311,var_5312,])
output2 = relay.Tuple([uop_5306,call_5313,var_5310,var_5311,var_5312,])
func_5325 = relay.Function([var_5310,var_5311,var_5312,], output)
mod['func_5325'] = func_5325
mod = relay.transform.InferType()(mod)
var_5326 = relay.var("var_5326", dtype = "int32", shape = (48,))#candidate|5326|(48,)|var|int32
var_5327 = relay.var("var_5327", dtype = "uint8", shape = (4, 84))#candidate|5327|(4, 84)|var|uint8
var_5328 = relay.var("var_5328", dtype = "float64", shape = (3, 90))#candidate|5328|(3, 90)|var|float64
output = func_5325(var_5326,var_5327,var_5328,)
func_5329 = relay.Function([var_5326,var_5327,var_5328,], output)
mutated_mod['func_5329'] = func_5329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5093_call = mod.get_global_var('func_5093')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_5351 = relay.TupleGetItem(func_5093_call(), 0)
call_5352 = relay.TupleGetItem(func_5094_call(), 0)
output = call_5351
output2 = call_5352
func_5366 = relay.Function([], output)
mod['func_5366'] = func_5366
mod = relay.transform.InferType()(mod)
output = func_5366()
func_5367 = relay.Function([], output)
mutated_mod['func_5367'] = func_5367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3567_call = mod.get_global_var('func_3567')
func_3569_call = mutated_mod.get_global_var('func_3569')
call_5403 = relay.TupleGetItem(func_3567_call(), 1)
call_5404 = relay.TupleGetItem(func_3569_call(), 1)
var_5412 = relay.var("var_5412", dtype = "bool", shape = (10, 4, 15))#candidate|5412|(10, 4, 15)|var|bool
bop_5413 = relay.logical_or(call_5403.astype('bool'), relay.reshape(var_5412.astype('bool'), relay.shape_of(call_5403))) # shape=(10, 4, 15)
bop_5416 = relay.logical_or(call_5404.astype('bool'), relay.reshape(var_5412.astype('bool'), relay.shape_of(call_5404))) # shape=(10, 4, 15)
output = relay.Tuple([bop_5413,])
output2 = relay.Tuple([bop_5416,])
func_5418 = relay.Function([var_5412,], output)
mod['func_5418'] = func_5418
mod = relay.transform.InferType()(mod)
var_5419 = relay.var("var_5419", dtype = "bool", shape = (10, 4, 15))#candidate|5419|(10, 4, 15)|var|bool
output = func_5418(var_5419)
func_5420 = relay.Function([var_5419], output)
mutated_mod['func_5420'] = func_5420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3771_call = mod.get_global_var('func_3771')
func_3773_call = mutated_mod.get_global_var('func_3773')
call_5425 = relay.TupleGetItem(func_3771_call(), 0)
call_5426 = relay.TupleGetItem(func_3773_call(), 0)
output = relay.Tuple([call_5425,])
output2 = relay.Tuple([call_5426,])
func_5431 = relay.Function([], output)
mod['func_5431'] = func_5431
mod = relay.transform.InferType()(mod)
output = func_5431()
func_5432 = relay.Function([], output)
mutated_mod['func_5432'] = func_5432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4411_call = mod.get_global_var('func_4411')
func_4413_call = mutated_mod.get_global_var('func_4413')
call_5433 = func_4411_call()
call_5434 = func_4411_call()
output = call_5433
output2 = call_5434
func_5437 = relay.Function([], output)
mod['func_5437'] = func_5437
mod = relay.transform.InferType()(mod)
output = func_5437()
func_5438 = relay.Function([], output)
mutated_mod['func_5438'] = func_5438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5437_call = mod.get_global_var('func_5437')
func_5438_call = mutated_mod.get_global_var('func_5438')
call_5497 = func_5437_call()
call_5498 = func_5437_call()
var_5514 = relay.var("var_5514", dtype = "bool", shape = (10, 9, 6))#candidate|5514|(10, 9, 6)|var|bool
bop_5515 = relay.minimum(call_5497.astype('uint8'), var_5514.astype('uint8')) # shape=(10, 9, 6)
bop_5518 = relay.minimum(call_5498.astype('uint8'), var_5514.astype('uint8')) # shape=(10, 9, 6)
bop_5520 = relay.divide(var_5514.astype('float32'), relay.reshape(bop_5515.astype('float32'), relay.shape_of(var_5514))) # shape=(10, 9, 6)
bop_5523 = relay.divide(var_5514.astype('float32'), relay.reshape(bop_5518.astype('float32'), relay.shape_of(var_5514))) # shape=(10, 9, 6)
func_5325_call = mod.get_global_var('func_5325')
func_5329_call = mutated_mod.get_global_var('func_5329')
var_5548 = relay.var("var_5548", dtype = "int32", shape = (48,))#candidate|5548|(48,)|var|int32
const_5549 = relay.const([-10,-2,-5,-6,-3,2,1,3,4,-4,-2,-7,4,6,-8,2,-5,3,-9,1,-9,6,-6,5,6,9,6,8,9,-9,-6,-5,7,3,8,10,8,1,-4,6,-8,1,-10,5,4,6,-4,2,-8,-7,-8,8,-4,2,7,-9,2,10,-10,1,8,-5,10,-6,-10,-7,-2,4,3,-4,-5,-7,5,-1,2,-1,3,3,-3,10,-1,-2,1,9,-6,-6,7,10,-3,-9,6,5,5,-1,-6,10,1,2,-1,-7,5,-6,9,6,-8,6,4,3,9,6,8,-5,-1,10,10,-7,-3,1,10,3,-4,-3,-10,8,2,-7,1,7,10,3,5,9,2,9,7,1,-2,-8,1,-6,-9,1,-6,1,6,-8,-4,8,-4,10,-2,3,-3,8,6,-5,6,4,-4,8,10,10,2,10,6,7,10,2,10,7,6,10,10,6,2,-4,1,-6,4,8,5,6,7,9,9,-3,10,7,-9,3,-6,-4,3,-9,-6,-6,2,8,-1,-7,5,-5,5,-4,-4,6,6,-8,-9,-5,-2,10,3,5,7,4,4,-8,1,3,-10,9,8,4,-2,4,8,-2,-2,-4,-1,-10,8,-1,-1,-6,3,9,-3,-1,-2,1,-7,-2,9,9,-6,4,8,-5,-10,-1,8,-4,-5,-6,-8,-8,1,7,7,2,4,7,1,-2,-5,-4,5,4,3,-6,8,-9,5,8,9,-5,-6,-6,6,-8,10,-2,1,2,5,-6,-1,9,-10,-8,-7,-3,-7,9,-6,-4,10,9,1,5,9,-10,-6,-8,8,-7,-1,9,1,1,7,-2,-3,-8,2,2,-5,-4,3,-9,-8,-7,1,6,4,-9,-5,7,4,4,-9,9,-1,6], dtype = "uint8")#candidate|5549|(336,)|const|uint8
const_5550 = relay.const([3.519325,-3.900211,-3.159933,4.225724,8.572327,-3.158276,-2.740601,-6.396181,-1.350239,7.535266,-9.695710,4.439816,-0.286550,-5.195612,-6.563009,-2.855430,1.127148,1.618198,-3.677520,-9.244328,-0.477805,-4.873572,9.964360,-7.829837,-3.997962,3.450544,-5.704704,-1.188792,-3.534463,-3.349952,-1.782751,-7.721269,4.504868,2.352649,-4.982539,4.418040,-1.148018,5.096527,-7.882998,8.900066,6.565416,-4.114866,1.686980,-9.091054,6.918113,4.434844,-8.473810,1.664925,7.553352,6.659463,8.048391,-0.070499,8.937304,3.309497,-3.348002,-9.902756,-7.517468,7.901464,9.002733,1.824426,-4.749452,-9.753416,-7.210304,-2.519095,-7.896467,9.445823,-8.372279,7.999968,-3.204194,2.251787,-8.467872,-8.670696,-2.550039,-7.778176,-6.757573,7.693290,-2.995789,1.793010,1.345871,1.936488,8.546389,8.012657,-5.576976,4.753356,-1.088466,5.346253,2.792535,0.421478,8.370333,7.447783,8.689951,-8.753316,0.146685,-3.597764,5.450623,-2.780668,-4.362913,-0.616776,8.131308,0.835357,8.301115,-5.020767,0.984671,-2.361121,1.032867,-6.736557,-9.396527,9.587645,-6.918953,0.388152,0.792574,-1.187040,6.630625,-3.807255,6.369394,-3.471719,4.301811,6.159716,-5.146702,7.093697,6.057808,-9.716393,7.073922,9.742161,7.041990,9.629676,6.232283,3.073264,9.982095,6.860388,1.297923,2.190292,-7.278273,3.661028,-8.736554,-1.621435,-4.620110,-5.473570,-0.480245,6.333291,-5.983280,-5.188373,6.865834,-6.428234,-0.991874,1.450298,-0.469494,-6.281191,5.679710,9.455320,-3.063591,2.927566,2.049325,-1.387330,-9.455649,9.192371,7.260716,-9.663149,1.244370,1.076444,-5.117889,-4.314485,9.193453,2.410833,-5.501189,-2.272525,-7.053448,-3.882916,7.037697,-0.890588,-4.791729,-2.050660,7.327827,-0.398322,-6.599678,-0.779330,-0.947110,7.642305,6.735831,-0.570780,4.594717,0.102740,2.915103,9.691244,-5.485624,-1.861422,-7.491589,-4.284099,5.276467,-6.150544,-2.225759,-6.566916,4.492185,-1.632916,-9.467257,3.413537,-1.890710,8.260533,-6.312867,-4.644130,-2.443985,9.586624,-5.385463,8.320663,8.828630,9.278062,-5.443589,-3.628232,3.338963,2.247501,-5.193081,1.835855,9.895347,-8.219731,-0.647930,-4.768321,7.025387,7.267351,-2.944268,7.850559,-9.358252,0.170844,-6.039581,4.511264,0.164585,8.567606,2.514967,-7.577095,6.928504,-4.127408,8.995229,3.437695,-6.368102,-7.867494,3.820478,-2.309971,-0.017290,-4.315815,-4.269911,-2.950817,-9.365487,7.822047,6.904014,-9.579212,-5.073036,-2.247755,-9.938048,-1.612514,-9.023109,1.305561,-0.171328,0.543089,4.830959,4.294393,0.026304,2.655911,6.894370,0.699747,-3.332730,4.943823,-1.363245,5.687197,8.373163,-3.761701,-9.223950,5.750213,7.760810,-5.984875,5.430952,-5.169159], dtype = "float64")#candidate|5550|(270,)|const|float64
call_5547 = relay.TupleGetItem(func_5325_call(relay.reshape(var_5548.astype('int32'), [48,]), relay.reshape(const_5549.astype('uint8'), [4, 84]), relay.reshape(const_5550.astype('float64'), [3, 90]), ), 3)
call_5551 = relay.TupleGetItem(func_5329_call(relay.reshape(var_5548.astype('int32'), [48,]), relay.reshape(const_5549.astype('uint8'), [4, 84]), relay.reshape(const_5550.astype('float64'), [3, 90]), ), 3)
output = relay.Tuple([bop_5520,call_5547,var_5548,const_5549,const_5550,])
output2 = relay.Tuple([bop_5523,call_5551,var_5548,const_5549,const_5550,])
func_5554 = relay.Function([var_5514,var_5548,], output)
mod['func_5554'] = func_5554
mod = relay.transform.InferType()(mod)
mutated_mod['func_5554'] = func_5554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5554_call = mutated_mod.get_global_var('func_5554')
var_5556 = relay.var("var_5556", dtype = "bool", shape = (10, 9, 6))#candidate|5556|(10, 9, 6)|var|bool
var_5557 = relay.var("var_5557", dtype = "int32", shape = (48,))#candidate|5557|(48,)|var|int32
call_5555 = func_5554_call(var_5556,var_5557,)
output = call_5555
func_5558 = relay.Function([var_5556,var_5557,], output)
mutated_mod['func_5558'] = func_5558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4664_call = mod.get_global_var('func_4664')
func_4665_call = mutated_mod.get_global_var('func_4665')
call_5570 = relay.TupleGetItem(func_4664_call(), 5)
call_5571 = relay.TupleGetItem(func_4665_call(), 5)
output = call_5570
output2 = call_5571
func_5572 = relay.Function([], output)
mod['func_5572'] = func_5572
mod = relay.transform.InferType()(mod)
output = func_5572()
func_5573 = relay.Function([], output)
mutated_mod['func_5573'] = func_5573
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5574 = relay.const([[[-3,5,7,9,-9,-4,-2,-9,2,4,-8],[-6,-1,9,7,9,3,3,10,-3,7,-5],[10,9,-1,-10,4,-7,8,-10,4,-4,3],[-8,7,3,1,-2,1,2,6,3,9,-4],[-6,1,4,-6,3,10,-7,6,9,6,-1],[2,-2,7,4,6,6,9,-5,4,9,1],[-7,2,5,5,-8,-3,-3,10,2,7,-7],[7,-9,3,-5,4,1,7,5,4,-1,6],[7,-1,-5,-6,-3,6,4,-2,4,-2,-1],[1,-2,-3,-1,-9,4,9,6,-2,10,3],[-7,-6,10,-6,-10,-8,1,7,10,-2,6],[6,1,-3,7,-7,-10,7,-3,-2,9,5],[-3,2,8,10,9,8,-5,1,6,10,10],[-9,-2,4,-2,1,-3,1,-1,5,-8,-10],[-3,-6,-6,8,-6,9,-7,9,-1,-7,7],[6,-10,8,6,-2,6,10,4,7,5,8]],[[-8,3,7,-6,7,-2,6,4,5,-1,-4],[4,8,-10,9,7,4,1,-10,-6,10,6],[8,-8,-8,6,9,-1,-3,-2,-10,-10,-8],[6,9,-7,-1,-6,4,6,2,-3,-3,-8],[7,9,-8,2,1,4,-9,8,3,-3,-8],[9,10,-1,-8,7,8,3,-4,-1,-2,-4],[7,4,-8,7,3,-7,9,6,-8,5,1],[-1,-4,2,1,-8,10,8,-7,5,2,5],[-2,1,5,6,-3,-3,-1,-2,10,1,-1],[7,4,2,-6,9,9,5,-3,2,-8,-4],[9,-1,7,-7,1,-8,8,10,6,-9,9],[-3,-5,-10,-9,1,-2,6,-6,-10,9,-1],[10,10,-1,5,4,-2,-10,-1,-9,-8,9],[-2,7,2,-4,4,4,-1,4,5,-1,-9],[1,1,-4,-1,-3,10,7,-7,-6,-4,-6],[5,9,7,1,1,8,2,-1,7,-7,5]],[[10,6,4,6,3,9,5,1,4,8,4],[-3,6,-8,-8,9,-4,4,5,7,3,-1],[3,-4,6,8,5,-6,3,4,-8,1,-9],[1,5,3,3,6,-8,5,-4,5,-6,10],[6,1,10,5,7,5,-3,1,2,3,10],[5,3,-5,10,6,-3,7,1,3,9,9],[4,-9,-1,-10,2,-9,5,4,1,-1,-9],[6,-2,7,6,-3,-7,-1,-5,-1,6,4],[2,-7,7,9,-6,-5,5,10,-9,-2,-5],[5,3,9,-4,1,10,-2,5,5,6,2],[4,-1,-6,7,7,3,10,9,6,3,-7],[-3,4,-6,7,-2,-3,-4,-7,2,5,-3],[-9,10,-2,1,7,2,1,-4,7,1,-10],[-8,-8,-10,-6,-7,-5,2,1,7,-7,-9],[-10,-1,8,6,9,-2,4,9,7,9,-4],[-1,2,10,10,10,-2,-6,2,-6,-6,7]],[[2,-4,-1,-5,1,9,8,5,-9,-8,3],[-1,6,8,-6,5,-9,1,1,-5,3,-8],[-5,9,-5,7,10,4,3,-9,-7,1,3],[-7,7,7,-8,-1,5,7,6,9,-9,-4],[-7,5,9,-9,7,7,10,4,-8,-10,-2],[4,-10,3,-5,6,-2,-5,7,3,2,8],[1,-7,-4,3,-4,5,9,-7,-7,-6,2],[-9,-7,-2,10,8,-9,-2,4,10,-10,3],[-5,4,1,-10,-3,-3,9,9,5,-1,-4],[9,8,-5,-6,-8,7,2,3,-5,1,7],[5,-9,3,7,5,-5,-9,1,-7,8,-8],[5,4,-8,-10,-5,2,7,6,-5,2,-3],[-8,-6,-3,8,5,-5,-3,-6,-7,-10,-6],[6,-1,-4,9,-1,4,-2,2,-8,-3,-7],[-5,1,-5,3,-8,-7,10,-3,1,-5,-3],[-3,7,3,-6,10,5,-5,4,6,-9,-2]],[[-4,-9,9,3,-3,7,10,1,10,7,-5],[-10,2,-1,-6,-3,8,-9,-6,-10,-9,-8],[-7,-4,2,-4,4,4,-7,1,9,-8,-4],[7,9,10,2,-8,-8,-6,4,7,-4,-7],[7,-8,10,7,-3,5,-10,2,6,3,-4],[6,10,7,-4,9,-10,10,-3,3,1,-9],[-6,5,5,-8,8,7,7,6,-6,-5,-3],[6,1,-3,-1,5,7,1,-9,-1,3,7],[-9,3,9,2,2,8,-1,-6,-5,-2,-1],[6,-4,-9,2,6,8,-7,-7,8,10,3],[-9,6,1,8,-4,4,-1,2,-8,5,10],[-4,2,4,-10,-5,-7,-4,-10,-10,7,2],[-6,1,5,-9,-7,-9,5,-3,2,3,-1],[-6,9,7,10,6,-4,-10,-5,3,2,-3],[7,1,5,9,-8,9,2,3,-5,-10,8],[-7,8,4,-4,-6,-4,2,-10,-5,9,6]],[[-10,-3,-10,4,-2,-10,3,-10,-1,-9,3],[4,6,2,3,-5,8,6,3,-7,-2,-5],[3,1,-2,-10,-4,6,2,-5,7,8,2],[-5,-5,-1,-1,10,-2,9,3,-8,-2,7],[4,10,4,7,3,10,-6,5,-7,-1,-7],[-4,-10,7,9,-9,-8,8,-9,7,-9,-10],[-7,-2,9,3,6,6,10,-1,9,-5,10],[-10,-8,-1,-5,-10,3,7,7,-7,9,-10],[-9,9,-10,-7,-10,7,6,-5,-8,-5,10],[4,4,-8,-7,2,-9,3,9,-8,-9,-9],[5,-7,-2,8,6,7,3,3,-6,-5,-9],[-4,8,-7,9,1,-1,-10,3,-3,10,-9],[7,-3,10,-10,8,-7,-8,-5,-2,4,7],[6,-2,8,-1,4,-10,5,-7,-9,10,3],[-10,-4,7,6,2,3,-3,5,-10,5,6],[-10,-4,-7,-2,-2,-1,7,-4,1,6,-1]],[[8,6,5,-8,1,3,6,10,2,-4,-10],[-8,-5,2,4,-2,-1,10,10,-8,-7,-6],[3,-3,-10,6,8,-4,-5,-6,-4,-3,7],[-3,-3,-7,4,-3,1,-1,-3,-1,-5,3],[5,-2,8,-6,-1,1,1,-4,1,-1,-3],[3,3,6,1,7,1,-5,-5,5,9,9],[5,-5,1,1,2,10,10,-1,-9,8,-6],[-8,-5,6,-10,6,-8,-4,-10,-3,-10,6],[-10,2,-5,-9,5,-3,-2,-8,6,8,6],[-3,8,7,-8,10,1,-7,-2,9,-4,2],[3,-8,4,1,9,-6,-9,-7,-7,-4,6],[-5,8,10,6,7,1,-6,-1,-7,-2,-9],[8,-9,2,-5,5,-1,-4,4,-4,-1,6],[2,-8,-10,-1,-1,-7,-4,-4,-9,9,-3],[-10,6,9,9,-5,-5,-1,3,-3,1,-7],[-9,5,1,8,8,-2,-2,-10,-8,-5,9]]], dtype = "int16")#candidate|5574|(7, 16, 11)|const|int16
const_5575 = relay.const([[[4,10,-7,-7,-8,9,8,-4,-1,-3,-5],[-5,-4,10,-2,2,3,7,2,-3,10,8],[5,8,-4,10,-8,6,-7,9,-1,7,-4],[-4,-8,-7,-2,-6,-6,3,-7,-9,8,-8],[2,-6,10,-9,-10,1,3,-6,-2,9,5],[7,-5,-9,-10,1,4,-6,-3,-9,9,8],[-7,-4,5,6,-7,3,1,-8,1,-2,-7],[1,5,-10,9,4,-4,-6,4,-10,7,7],[-9,9,-4,-5,3,-8,6,-1,-8,3,-3],[-1,-3,2,-6,9,3,5,3,8,-4,2],[-4,4,-8,-4,-6,-2,7,10,-2,-1,9],[4,-6,7,1,-9,-4,9,-2,5,-9,8],[10,1,8,-8,-8,10,7,3,9,-4,-8],[5,7,7,-4,4,-6,-5,-7,-3,7,10],[-3,3,8,4,-2,6,-8,7,-10,7,6],[-10,7,1,-9,2,-5,-3,-4,-8,6,8]],[[-9,-6,-6,4,-5,8,-10,-7,-9,2,-4],[6,1,-6,10,-9,-9,-7,-9,8,7,-7],[-2,-7,-5,-6,3,-9,-5,-1,1,3,6],[4,1,1,-7,-7,5,1,-5,9,8,-4],[4,-10,-7,2,3,1,9,1,2,-4,-6],[-5,3,-10,-3,-6,2,-10,8,-4,-2,-4],[9,-7,-5,-6,-8,-3,6,-2,2,5,-3],[-4,-9,-2,5,1,1,-5,-9,-1,-3,-5],[-10,7,4,-7,-7,8,9,-8,-5,-6,-5],[5,1,10,-10,4,-4,3,3,5,-1,9],[-4,-4,-3,5,3,-1,-8,10,-8,10,-5],[9,7,1,10,9,4,1,6,-7,-8,3],[1,-5,-8,-8,2,-5,3,6,-6,7,8],[9,-6,3,7,1,1,-7,-3,-4,-4,1],[-6,3,1,2,-10,3,7,1,4,-4,-1],[4,7,8,-10,1,7,-6,5,-10,-10,10]],[[-3,-3,-4,9,-7,-9,2,6,-8,8,2],[-6,1,-10,2,-10,3,-9,-10,4,3,2],[3,-9,-4,6,8,-10,9,4,2,-6,5],[3,8,-3,-1,8,2,4,-2,-1,-2,3],[-5,-5,-9,1,10,3,1,9,-2,5,4],[-1,8,9,7,3,1,8,-1,-7,-2,9],[6,-5,-4,-2,10,5,7,9,-9,5,-4],[-9,-1,6,-5,-9,2,9,6,4,-7,5],[-6,10,-9,-3,-8,-8,1,6,-10,6,9],[-7,9,1,2,-9,-10,-4,-4,4,1,4],[-7,-7,5,6,-1,1,6,-5,7,9,-5],[-10,9,-4,7,10,8,8,1,7,9,-1],[9,-5,3,8,6,8,4,-8,10,3,-5],[1,-7,9,8,2,9,-6,5,10,-3,-9],[-2,6,-4,10,-1,7,-1,5,10,7,-7],[4,8,-5,2,-6,10,-6,2,-6,-9,1]],[[3,9,3,5,-10,4,-2,-9,-3,-9,-6],[9,-3,10,-10,-1,-5,6,-6,-10,9,4],[-2,-6,-7,-10,-1,2,-4,3,-3,6,-5],[-8,5,-7,1,-8,2,8,10,-2,-8,3],[7,7,10,-8,8,-8,-3,1,-6,-6,2],[10,3,3,8,-5,-3,5,-8,10,10,-10],[3,-6,10,-9,-6,-6,-3,-10,6,8,-10],[5,-7,-3,-5,9,-6,-8,6,3,-8,-3],[-10,2,10,7,2,-5,9,7,3,-1,-2],[7,8,-2,-1,-5,-7,8,6,5,-7,6],[-10,-1,10,4,-3,-10,3,5,-8,-4,9],[2,7,-5,10,2,6,-5,-5,8,1,9],[1,-7,-6,2,1,5,5,-2,-3,7,8],[-6,10,-9,10,-5,1,8,1,5,7,-1],[9,-7,8,2,5,-6,-9,-8,-4,2,4],[-5,1,10,1,10,3,-2,1,-6,9,-1]],[[-9,-9,-1,10,-10,-4,-8,-9,-4,-9,-6],[9,-5,2,-8,-4,4,-4,2,-2,-1,-3],[1,-8,-3,-5,9,6,10,10,5,-9,-7],[3,6,-2,-2,-8,9,9,6,-10,-7,-1],[-8,-6,-4,9,-7,1,-10,4,7,6,-1],[-7,10,-2,-8,5,-1,-9,6,-6,-2,8],[-9,-3,-6,2,3,-2,1,-9,6,-4,-5],[-4,1,-5,7,5,8,2,-7,1,6,-5],[9,3,-10,-4,2,-7,8,-7,7,-10,-10],[-1,7,-8,-5,-7,9,-10,8,3,10,4],[3,-4,3,-5,6,-1,8,-3,6,-7,-9],[3,9,-9,7,-8,3,1,5,1,2,2],[3,4,5,-4,8,-6,-5,-7,-8,-3,8],[9,1,-5,-1,-4,-4,4,10,8,5,-5],[8,-5,9,-9,3,10,-7,-9,-4,5,-9],[-1,-6,7,2,-4,-3,9,6,-9,-6,-4]],[[-6,5,4,-9,-8,-4,-9,6,2,-4,-8],[7,2,4,6,5,1,-3,-10,1,-5,2],[7,-7,-7,-4,-7,8,8,9,10,-6,-4],[9,1,9,5,2,-9,-1,-2,-1,7,-8],[1,-10,1,-5,5,6,2,-4,9,8,-4],[6,5,5,-7,8,-10,3,4,-6,-2,5],[-8,-2,4,6,-1,2,-10,-8,1,6,-2],[-3,-9,-5,1,-6,8,9,7,10,6,4],[10,-2,5,2,-9,4,-6,-8,9,-10,-1],[1,-2,6,2,5,-1,2,-7,3,-1,-5],[-4,-6,6,-1,4,-4,2,8,1,5,10],[-8,-2,-4,-6,10,9,-4,-1,-3,7,-5],[9,-3,5,-2,5,-4,9,-10,5,6,5],[1,4,-4,1,-10,-3,1,-10,4,1,2],[6,-6,1,4,-1,-5,1,8,9,2,-2],[9,-6,-7,1,-8,3,-7,-5,2,8,-10]],[[7,2,-5,-7,9,-9,8,-3,-9,-5,4],[-7,-3,-4,-6,-9,-2,8,-7,-4,-10,-3],[-3,7,-7,4,-2,-2,-2,5,1,-3,-7],[10,-8,10,9,6,10,-4,4,10,-3,-1],[9,4,-10,-2,-2,10,-7,9,4,8,9],[-2,-1,10,-5,10,-7,-3,-3,-5,-7,4],[7,-10,9,8,-1,4,1,8,5,9,10],[10,-6,8,-1,-7,-8,-3,4,-8,10,-9],[-3,6,-2,-1,-8,8,5,-9,-2,7,5],[8,1,-6,-7,-1,-9,10,5,-6,2,9],[3,6,-8,5,2,5,-1,-2,6,-1,-4],[6,2,-2,-9,-4,1,-8,-10,4,-8,3],[10,10,-3,-8,-1,4,-10,10,7,10,1],[-9,-2,-2,2,2,3,7,-2,-2,-1,10],[3,1,-1,2,-10,2,-3,-2,2,-8,-5],[-10,10,-4,8,-4,-2,-3,-7,-7,-5,9]]], dtype = "int16")#candidate|5575|(7, 16, 11)|const|int16
bop_5576 = relay.less(const_5574.astype('bool'), relay.reshape(const_5575.astype('bool'), relay.shape_of(const_5574))) # shape=(7, 16, 11)
func_3223_call = mod.get_global_var('func_3223')
func_3227_call = mutated_mod.get_global_var('func_3227')
const_5588 = relay.const([[-1.767779,4.575822,-6.443700,-2.048969,-0.043078,8.366842,-2.551647,8.567299,-1.650660,-7.651119,-7.072610,-0.333202,-5.787885,-1.953524,-7.550205,-7.912160,5.068575,-1.670270,-8.676306,8.947075,6.527283,7.236972,7.901230,1.748718,8.071179,6.778843,-0.350059,9.887474,-5.589334,7.524715,-5.181720,3.898776,7.822260,9.126163,-3.661945,3.642044,9.386837,-4.813500,5.617569,-5.308733,5.981211,-0.308303,3.747703,9.353011,0.270978,-7.982434,-6.134375,5.077804,-8.616129,5.540382,3.652086,-1.677478,1.705728,7.692045,-5.099834,-1.505069],[-6.577886,3.137160,-3.344382,0.511710,8.529195,2.237045,3.680212,9.936677,-7.536953,2.526035,9.087160,-8.326907,-1.060323,0.471469,-1.286732,-0.141131,-6.425053,-5.297936,-0.547248,3.664794,-8.467074,8.870893,9.822100,1.896363,8.764043,-2.866954,-6.235094,-9.741534,-9.399206,2.404071,6.956137,2.996375,4.786552,-5.783085,4.225247,5.938860,-6.078796,-4.582346,1.903468,3.399108,-9.519029,-0.974332,3.452269,5.697477,-3.422501,-6.860069,-5.665178,-2.986826,6.268393,-0.676282,-6.823237,-7.296647,-6.388951,-2.473826,-0.792093,6.115935],[1.065122,5.890179,-8.698731,4.869823,5.226601,-0.522107,7.481819,3.100328,1.528684,-0.213482,5.201532,-3.039051,4.600388,-6.556002,0.170358,-3.737517,2.668195,2.185072,-6.031502,-1.127738,-9.203608,2.891109,9.257976,-3.721704,-4.824853,-1.756994,-5.238375,-2.824985,-5.936589,3.718829,-9.770108,-7.764261,-1.803150,6.560949,-2.458924,-4.087302,-9.975340,5.757543,3.122332,-4.143937,-0.796163,4.931421,1.799435,-4.059087,-7.881253,8.709845,3.474061,-0.060580,6.275417,-7.554498,-3.362930,-4.030204,-5.374675,-5.737219,-1.145971,-9.264164],[-7.953316,3.803462,4.523299,2.628025,8.153197,-6.019977,-6.530008,-3.442906,-6.463948,-1.409881,-5.525891,7.236740,-6.998130,-1.158076,-8.264943,8.763037,-4.127035,-3.454894,-2.715336,-5.266383,5.953776,-6.923234,5.072066,3.218746,3.261400,-3.743305,2.897702,-8.556088,-5.399247,-5.841662,9.227175,0.782797,-2.113573,8.803599,8.820288,-4.298745,-4.521596,-0.981668,-7.662429,8.965496,3.731238,1.404994,5.049296,-8.359097,-6.222344,-4.592615,-0.019747,8.971801,-1.029787,0.281442,-3.956191,-8.893277,-3.589349,6.148451,-4.895388,-9.742963],[-1.315199,-1.399922,-1.577431,6.037100,3.353484,-5.705270,6.850898,-1.125669,3.367532,7.821011,-8.698508,-0.841352,8.223165,8.302298,7.946010,4.717069,0.408969,5.146533,1.339074,-6.502314,5.122632,-0.069122,-6.899741,-0.406245,7.397554,-4.141020,0.334134,-1.651369,-2.444754,-8.248261,-6.973470,2.863989,-4.253732,0.672105,-8.752845,-9.550802,-4.207606,-4.642125,-1.784316,-0.516040,3.526831,6.392414,-4.109277,8.541557,8.733922,-3.395777,8.380610,8.772327,-1.948144,1.462450,-8.447388,-2.266206,8.736507,6.486238,8.045338,8.900554],[-2.344531,5.509955,-0.992901,5.219292,4.725345,8.733236,-6.188587,-5.947687,1.699960,0.408257,8.065663,3.494453,-8.265367,-5.391091,-3.857252,-5.214022,-3.925687,2.025450,-4.263620,-0.968813,-2.587165,2.963789,-9.818037,-1.724513,9.812956,8.710924,9.226957,7.204567,-1.047186,-4.303933,8.392659,4.652541,-9.372520,3.485619,-2.919281,-4.145265,0.625429,2.964608,4.671891,-5.581394,3.795790,-2.529877,-6.295941,-8.692636,8.658090,6.533193,-6.379843,1.965723,-7.635960,8.787200,-9.217341,6.461747,2.424972,-3.028476,-2.701636,-5.950148],[-4.095099,7.641117,-9.616830,7.634144,-2.661519,4.088354,-3.663050,3.472214,8.331708,6.402738,9.160401,3.941162,4.395545,7.793771,-0.468996,8.357434,-1.548450,0.637242,-3.344998,9.844600,-2.629483,3.624698,5.476183,0.490341,-9.365213,-4.956096,1.147554,-4.681319,8.639575,9.502887,2.146769,6.359701,3.440590,5.164294,6.984311,-5.925871,0.938864,-8.552787,-0.897256,4.167305,-7.857338,-1.413863,1.024625,-1.752577,2.550637,9.430306,-0.790262,-2.791274,3.010343,-0.576041,-3.347877,-1.162137,-6.765897,-2.342170,-3.368537,4.704295],[-3.842116,2.785750,4.465121,-8.820318,2.093130,2.973797,-9.457593,8.532739,2.076774,3.184265,-3.476916,9.877149,-9.812925,7.358623,7.658401,-7.751773,6.525330,-1.059697,8.234540,3.062654,-7.294872,6.555710,-3.314030,-0.057420,-8.694079,-3.673155,-7.401463,5.447712,7.566224,1.540034,-0.177044,-4.168444,5.518951,-9.291760,-1.764602,7.598284,-3.927170,0.307398,3.958488,2.287774,9.877743,-9.156295,6.898386,7.704529,0.359250,-4.813751,-8.226992,0.113397,3.727125,-9.514290,6.449795,-0.084223,-6.540834,-9.864619,1.368951,0.633518],[0.639960,-6.713854,-0.868774,-3.693627,3.726602,3.860649,3.741798,7.458588,-5.362369,-0.659573,-2.918297,9.889766,9.315624,-1.096218,3.673737,2.264575,-6.559189,-8.519776,5.447035,-7.526038,1.596684,-9.743793,-4.527992,9.747098,-4.625733,-5.861424,-6.853798,8.335691,3.145971,-6.559469,-0.070279,-7.563351,-5.722039,0.607627,2.093688,-8.706829,0.033403,7.095550,-5.813206,-0.608732,2.209837,7.173762,-2.440155,8.097214,1.465057,1.366192,8.770414,-2.984846,-4.180411,-8.268246,2.081447,-9.163752,2.031101,-9.040843,-8.372387,-9.975209],[5.186153,7.251894,0.141474,5.065600,-8.519401,-4.648256,-3.601253,0.993879,-5.960299,-5.757780,-0.811152,-7.542196,3.985504,-3.718737,6.464723,5.525104,-8.521550,-5.602149,8.827048,-6.676106,-4.590541,2.743911,2.434190,4.877509,-3.597096,6.873932,-0.364570,6.658206,-1.426822,5.018734,-4.947867,-7.716966,5.052378,-2.476048,0.946069,8.332945,2.889471,-0.696466,8.948969,-4.830560,-0.615183,9.966259,2.722010,-1.159457,-7.555180,8.693046,-9.866343,5.013840,2.821286,-9.643684,8.710486,-0.767740,-8.660697,1.893116,7.793426,-9.229196],[-4.251282,-7.877846,-1.100739,2.076271,9.174979,4.531309,1.085215,7.423243,6.505831,3.120201,7.828607,7.378759,-5.731335,-9.921049,3.416355,8.198313,-6.811050,4.799882,-2.727767,9.554222,-1.874990,7.683227,7.978967,-8.913156,-4.241817,4.408178,4.924089,-5.372505,-7.805971,8.060518,9.541823,7.809190,9.464409,-7.747667,4.925660,5.788362,-4.530915,3.233068,6.470261,-2.303457,5.562496,-7.268925,0.587780,6.335605,0.035885,6.544943,2.012861,-0.620288,4.971607,2.360869,-1.734409,-1.018365,0.361731,-6.050161,7.777506,2.935049],[6.861669,-7.148324,-3.665830,-6.949391,-2.219924,-5.177360,-4.220618,-5.358118,2.540849,-9.759581,-3.667508,-0.979972,8.284742,7.959537,-8.414168,6.376417,-3.407218,-7.668859,0.611831,-9.832945,-2.244911,-7.603125,9.303997,-6.149411,-2.081451,-6.282960,-9.015063,-8.101744,0.799195,-5.710468,-3.727704,1.730396,2.450742,0.499955,-5.053028,2.282078,-6.825373,9.288369,-8.424031,-5.951432,3.964191,-4.584396,-1.112843,7.908295,-7.850827,9.556523,8.705755,7.622096,-7.383269,-3.951781,-2.794210,3.915980,6.878079,-4.460921,-3.011873,-7.634870],[0.597064,6.878480,8.822353,6.161306,6.572690,5.893738,-5.282801,0.955652,2.365183,3.158927,9.384164,9.910299,-6.489421,5.897891,-9.252459,-8.846171,-2.024930,2.850462,-1.446251,5.045427,4.586739,-1.957272,7.892222,-4.464630,9.025253,-5.429755,-9.108929,0.256426,0.080563,-8.513423,-8.292271,3.779151,-6.732904,2.065821,5.143714,-9.176599,3.533364,-6.315622,2.944381,8.910632,4.277014,4.584819,9.600107,-6.982146,6.620165,4.444080,0.796922,-7.067727,7.547000,-5.127739,-8.980281,-8.934194,1.685059,-4.854215,9.495343,-5.756618],[6.509014,9.006320,-0.778202,2.477949,-2.712337,-6.276993,2.566513,0.526519,-1.557390,-7.117449,4.337944,-8.973773,9.920471,2.292270,-7.013574,8.462356,9.675330,8.546890,-5.861503,-2.162094,6.960958,-3.010738,4.731621,8.200092,5.532062,4.610087,-4.305845,-3.031058,-4.546946,7.858329,9.480040,0.752192,0.144614,-3.766490,8.620177,-5.952988,9.331947,-5.786524,-8.811448,-8.082617,4.825154,-4.231878,5.362052,2.224225,-8.347193,7.066962,-7.628229,8.052430,8.389905,5.081820,-8.475141,6.243555,1.215823,-3.326724,0.902121,4.932147],[-1.734960,6.175515,-4.281094,-1.483267,4.169842,-1.319571,-2.684666,4.647218,-7.751701,-2.991286,-1.522839,-1.867865,0.355973,9.822721,-0.049126,0.503352,6.522024,-7.130595,-4.710087,-6.979099,-5.874249,3.271726,-9.613453,-5.908843,9.986415,4.698513,-9.609635,4.319873,5.830580,9.376939,-2.167578,-1.430893,6.261474,8.705576,5.118073,5.913823,0.016077,-2.924914,2.353677,-5.243718,-7.434455,-9.735894,3.681466,-7.454665,-7.157093,-0.565738,5.155456,-9.020746,-7.836267,-6.605873,-9.241198,2.871286,-7.428585,3.286896,8.314609,-7.855425],[-3.538006,-0.479950,2.994355,-4.791148,-3.397231,-0.278101,7.846516,-2.256024,-8.973756,-9.177740,-9.937040,-5.226719,4.241784,-4.880557,5.859587,-5.007409,5.663641,-0.033745,-4.796111,1.326481,1.184913,-9.132502,-2.645095,-7.589489,8.462133,8.382682,6.898866,-9.635420,-5.335707,0.803748,2.729961,1.907709,-4.943395,1.266619,-0.608608,-8.002089,-8.490664,-1.778154,5.618565,-2.126798,3.488294,8.163746,3.285054,-9.937734,-8.420016,-7.616490,7.765786,4.557894,8.877941,-7.659161,4.946407,8.290202,4.230464,-1.635055,4.424336,8.287623],[7.131684,1.595485,-5.275575,-3.754985,7.699891,9.236094,-9.681294,-9.762582,4.084846,7.892826,9.772350,9.106297,-4.662361,-2.002219,-4.599465,1.422516,-8.841269,-6.525586,-4.594780,9.526718,6.449753,-6.022822,7.008274,7.177408,-5.390312,9.525564,-1.230823,-2.319373,4.898837,-9.070040,9.513069,9.852942,-3.243597,-3.787049,-3.456063,-4.905400,-0.944404,5.362229,3.889130,0.422111,3.164987,-5.393485,4.292686,-1.041238,7.547376,-4.412325,-4.905033,-1.902168,6.563269,8.754738,-4.323298,-8.523253,5.530938,1.275906,-4.926226,-1.946019],[7.600358,8.032077,9.720838,8.445318,-3.283541,8.916384,3.651229,3.625438,5.101152,-3.232866,-3.775095,-6.865013,-4.173087,1.394862,-6.082409,-6.634477,-5.643606,-3.193018,-4.963792,-1.800186,1.433165,6.922559,5.403800,-4.283939,-6.727564,-5.740905,5.657560,-8.682650,-1.098613,-0.633321,7.074075,6.198646,7.213999,0.347700,9.869092,-4.013419,-5.680400,-5.148213,8.425864,-6.831824,8.528854,-6.857451,5.069513,4.798492,-2.978623,2.704094,-7.301387,5.832481,-1.415818,9.467952,-3.314340,2.392731,-6.359870,-4.390727,-1.518484,3.204724],[-6.307036,-6.135812,-6.862100,9.694637,1.716386,-8.604368,4.274186,2.487580,-6.187311,-5.136211,4.939494,1.977148,1.835510,1.470903,-2.855993,2.134867,-5.229201,4.025544,2.578366,-3.802431,1.239318,5.203347,-3.496318,-6.142747,9.083014,-1.060170,-6.858404,-6.418251,5.206865,8.378115,-9.514945,-9.002447,-0.859073,9.548283,2.785323,4.451099,-3.956483,5.234508,8.564081,-8.943714,-9.117275,5.462142,-7.490490,-9.274137,7.869620,-9.156504,5.739436,9.784692,-6.374134,6.729697,-0.597924,-0.352248,0.187031,5.215248,7.343871,-5.134214],[-8.840377,9.200045,8.247414,7.700392,0.817815,5.965001,-0.890705,3.159692,0.329318,-9.329653,5.402355,8.590919,0.806306,6.368559,-5.178348,-8.403144,-0.654517,9.273174,-3.563710,-4.504589,-2.079201,-8.142474,-0.094898,5.948691,-5.057382,4.990839,-3.785516,6.118938,-5.598876,8.751060,-0.304252,5.351662,8.556815,-7.925045,9.251284,0.751258,-5.222567,3.262364,6.179279,7.023964,-4.318146,7.745091,4.274837,-2.373979,-4.974415,-9.619478,-0.009906,8.115020,-8.761153,0.668880,-9.865568,-2.519757,-8.445412,-0.132848,-5.988881,5.207992],[-7.581187,-6.933083,4.079719,5.621159,-7.137882,-9.853052,-6.608142,-0.395560,-9.640486,-0.672219,-5.913500,2.025990,-7.667516,1.187332,1.301274,-3.170543,5.039270,0.060336,2.311309,-1.317058,-9.758475,-0.763406,-0.725514,-5.999035,-2.490273,-8.400089,6.733953,8.467249,1.577995,-2.191747,-3.768614,-8.384353,8.433736,-0.517938,2.199342,-8.952348,-1.005269,-7.184927,8.356669,0.246602,6.445283,6.759020,0.093084,4.206065,0.874993,-6.918435,-8.787365,4.635629,-3.569138,-3.274035,3.706990,-2.363619,-1.251168,-0.602393,0.531233,9.247540],[4.670206,3.599483,-2.701640,7.929767,-5.007897,1.357758,0.112676,8.100045,-4.208157,6.352654,-1.984135,9.130654,-0.665914,3.117099,1.308119,-8.233995,0.566471,-4.155727,-0.819613,0.269714,7.955776,4.484420,0.212973,-5.925850,2.638319,1.834028,0.480881,-3.934329,2.778399,6.709697,-3.521516,1.972740,6.501264,5.315326,-3.368968,3.453579,8.058707,-0.879986,2.695891,3.944324,-2.636033,-4.353818,9.292093,6.206929,-9.133035,-3.633347,-6.739962,-2.202784,9.808311,-8.363310,-3.820598,4.055279,-2.117215,0.513347,-1.670433,-6.571453],[8.132936,0.157070,5.233328,8.251536,1.058103,1.075042,-6.327787,-4.936606,5.853524,3.004066,-4.263962,-4.377429,-9.071390,-3.558567,-9.448064,4.310141,8.697450,-7.457327,7.533705,2.264741,0.960471,-3.117963,-4.974466,0.673033,9.700785,-1.794172,6.709101,9.101844,-4.513628,7.964782,-3.028924,-9.214368,6.237427,4.967126,4.831321,7.817205,8.530226,-1.123174,-4.761939,6.794404,-3.338583,5.686813,-3.001630,5.658574,-4.182366,4.831872,5.628254,2.609640,8.949132,8.843619,8.060373,2.657196,-6.345650,-3.682182,-2.198938,3.514536],[1.083810,-8.783643,2.224104,-2.004010,-5.155568,-2.524951,-2.605780,-5.283092,-2.874667,-8.158422,9.160252,-8.616443,9.548966,-4.904393,5.339986,-5.335945,6.309881,-3.319354,-7.750711,-1.461658,5.108142,-2.830761,-1.863397,6.463177,-0.585426,-0.627519,4.336232,8.450357,-0.256519,-2.564528,3.411278,-1.867641,-8.776945,0.983947,-9.014499,0.364718,7.922762,0.258616,5.115209,-0.972731,-7.693631,0.125506,-3.026376,-1.159839,-3.475566,-8.494696,0.267158,-9.763828,5.740159,-8.582223,-1.174531,6.602330,0.517791,4.265076,6.559633,-7.479035],[9.277320,-4.784893,-0.544389,-9.118066,2.060703,5.778456,5.699645,-7.053429,9.357022,-3.103649,7.269870,8.510973,-3.002432,7.147836,8.351545,4.947959,8.714020,-2.132983,-6.877275,-7.080712,5.214416,-6.686323,-9.730757,7.801940,7.316062,8.250581,-7.493694,3.450209,7.047306,-4.416297,-8.229142,7.087218,7.930733,-1.555287,-7.861092,-7.134707,-7.283485,6.804896,1.734526,-7.932106,-1.103495,4.742037,8.608423,-5.223306,1.817145,2.939579,-7.136719,2.515787,-5.934758,-1.877017,1.102871,-4.354685,7.601888,-1.024778,-2.516624,-2.999197],[-4.420864,7.759537,-2.074832,-2.336371,7.223984,-4.652900,8.185004,1.912379,8.984484,-4.291542,-1.692118,-4.399005,-8.598805,8.801598,3.678382,-1.261394,0.169958,8.217397,2.914402,-3.280556,4.479855,-0.051464,-4.527535,-4.249314,7.791695,-9.928331,8.431172,-0.597952,6.279518,4.009616,6.274143,-4.874377,9.730660,-5.189156,-5.354709,0.664450,8.849123,-7.177160,-8.503902,3.028575,0.976128,6.080887,-4.758420,1.425066,6.517136,9.936226,-1.592663,-5.174580,1.709558,-3.675687,1.337707,-0.982923,0.538579,-3.165821,6.570526,-9.018121],[-6.153114,-4.091491,0.716488,-3.969369,-2.569725,4.119532,-9.035983,-1.836045,-7.413706,3.934494,5.358659,9.027708,-8.497201,-0.472188,1.694973,-2.779506,-9.197180,6.519220,-2.542750,6.754944,6.442746,6.328166,-7.143072,7.496196,-1.904215,-9.694213,-2.701019,5.168674,3.540665,4.615006,-8.996272,-8.199309,-6.145801,-6.789622,-1.909693,1.949218,-6.666719,4.750330,-9.781216,4.884339,2.282852,-0.911671,5.037018,-7.931546,9.232338,-8.102139,0.621328,3.384078,-2.550259,6.889952,7.122251,-4.491739,0.804475,-3.469292,-5.538951,2.930864],[3.910290,-3.151856,0.632539,3.865615,-1.225070,-5.110200,2.779585,5.654011,1.822581,-1.755968,1.886546,-1.794916,-6.969616,-0.658090,-5.102485,-8.882594,-9.377675,1.715542,3.136369,-2.737399,-2.111901,7.511840,-3.306359,6.770068,8.241287,-1.724659,-3.204340,-8.187468,0.670854,0.823231,-4.128135,4.964482,-9.652580,-9.258125,-1.569660,8.961589,4.113128,-1.164338,1.365230,0.175562,3.607659,2.476076,-8.010958,-7.172736,9.649033,7.335036,4.904162,-1.090373,3.605542,9.837976,1.117334,-2.031515,6.174309,6.852732,-8.246933,-4.820434],[-4.780980,8.363229,3.094451,9.422234,-6.114580,-9.641236,6.786464,8.316287,4.559706,-0.575316,-7.773220,0.484216,4.697557,-4.980033,9.802500,9.689127,7.774909,-3.552177,-8.043855,6.813737,-7.752373,-4.058590,-5.065347,0.913737,-7.874860,-1.661439,-6.177819,4.094160,-3.562453,-4.622002,-7.844546,-7.314097,-9.414287,-8.833570,-0.716179,6.242685,9.455494,-9.961088,-9.988581,1.003667,-1.244925,4.643757,9.628414,-7.925109,-0.711168,1.200970,7.552147,-0.377929,-4.541299,-7.926100,-8.089647,9.795639,-1.264012,9.298833,6.415624,7.738840],[4.068238,3.916511,5.453287,-6.294837,-3.460093,-5.092454,4.425793,2.368106,3.495140,-3.549785,-7.969101,5.605124,-7.431737,7.231838,7.509168,7.090953,9.470505,3.890500,-0.408291,-8.650345,5.054248,-0.857438,-4.946981,-1.437618,-5.548238,1.517276,2.470123,6.123645,-0.744933,2.675069,7.432821,-9.326797,1.149577,-6.779231,8.553643,-8.169844,2.675487,-7.281153,1.854720,-0.326886,0.033515,-7.324883,-2.911006,-7.989122,-7.271909,1.886727,-4.741004,-4.515460,7.306544,-8.167118,4.514997,-3.413019,9.816881,-0.726046,9.235891,-0.039943],[1.774428,1.283397,-6.172400,-4.300472,-2.113745,4.626759,7.866156,-4.518290,-4.655996,6.925311,-9.711690,-1.387950,-0.160545,-8.104728,7.857539,3.392074,2.428578,7.941378,-3.639288,-5.350889,0.802401,-7.919786,3.894504,9.421210,2.527214,4.499617,-4.908523,4.253803,4.877274,7.202241,9.295963,0.632371,7.320729,-9.061222,-4.579159,-7.266917,-8.621971,-9.970650,-9.952054,4.442938,-5.789090,4.655486,4.371967,-9.250870,-9.228381,1.599687,-7.162288,-9.005124,7.533122,7.814027,3.634455,4.537140,-6.693438,4.942087,-8.451037,-9.999689],[6.473271,4.468232,7.956626,2.848260,1.365613,7.902600,2.856704,-2.339244,-7.136620,-0.279207,4.154270,-9.489366,5.940089,-2.887405,-0.535414,3.621538,-9.334717,-8.032178,-5.710069,3.850855,2.297572,8.953787,-3.822732,5.673988,1.625278,-9.382978,-6.188076,6.703789,-2.445414,5.383494,-2.947625,3.990658,4.024090,-8.250222,3.978119,-6.030915,-2.190126,-5.424735,4.128377,-4.672243,7.100669,0.991327,2.774215,-7.917568,4.095529,-9.189532,-5.378788,-5.424931,-1.425389,8.059612,9.548773,-8.873241,4.542541,-8.098928,-7.252402,6.448547]], dtype = "float64")#candidate|5588|(32, 56)|const|float64
var_5589 = relay.var("var_5589", dtype = "int16", shape = (252,))#candidate|5589|(252,)|var|int16
call_5587 = relay.TupleGetItem(func_3223_call(relay.reshape(const_5588.astype('float64'), [16, 7, 16]), relay.reshape(var_5589.astype('int16'), [252,]), relay.reshape(const_5588.astype('float64'), [16, 7, 16]), ), 3)
call_5590 = relay.TupleGetItem(func_3227_call(relay.reshape(const_5588.astype('float64'), [16, 7, 16]), relay.reshape(var_5589.astype('int16'), [252,]), relay.reshape(const_5588.astype('float64'), [16, 7, 16]), ), 3)
uop_5595 = relay.asin(const_5588.astype('float64')) # shape=(32, 56)
uop_5611 = relay.tan(const_5575.astype('float64')) # shape=(7, 16, 11)
var_5613 = relay.var("var_5613", dtype = "float64", shape = (7, 16, 11))#candidate|5613|(7, 16, 11)|var|float64
bop_5614 = relay.bitwise_or(uop_5611.astype('int16'), relay.reshape(var_5613.astype('int16'), relay.shape_of(uop_5611))) # shape=(7, 16, 11)
output = relay.Tuple([bop_5576,call_5587,var_5589,uop_5595,bop_5614,])
output2 = relay.Tuple([bop_5576,call_5590,var_5589,uop_5595,bop_5614,])
func_5622 = relay.Function([var_5589,var_5613,], output)
mod['func_5622'] = func_5622
mod = relay.transform.InferType()(mod)
var_5623 = relay.var("var_5623", dtype = "int16", shape = (252,))#candidate|5623|(252,)|var|int16
var_5624 = relay.var("var_5624", dtype = "float64", shape = (7, 16, 11))#candidate|5624|(7, 16, 11)|var|float64
output = func_5622(var_5623,var_5624,)
func_5625 = relay.Function([var_5623,var_5624,], output)
mutated_mod['func_5625'] = func_5625
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5634 = relay.var("var_5634", dtype = "float32", shape = (1, 2, 10))#candidate|5634|(1, 2, 10)|var|float32
const_5635 = relay.const([[[-7.757756,-4.508096,-6.201164,9.289093,9.014305,-1.104011,1.810596,-2.179860,-8.367032,-3.669420],[-5.781747,-2.551615,-3.813498,-2.786678,-2.888348,-1.434463,0.793306,2.725278,-5.466870,0.123339]],[[0.018205,1.456258,-3.283852,4.627511,5.977034,-7.015270,-6.682346,-2.839507,-7.639321,7.555413],[-6.886783,-6.520094,-1.121028,1.297930,-2.907887,-5.409138,-5.968005,-0.668061,7.300599,4.911535]],[[-7.285936,-0.738045,0.463826,4.170277,0.653714,-0.928579,-1.341210,3.846555,-6.657798,6.550286],[-3.929413,0.205255,-7.913381,9.973522,2.742329,-6.034989,-3.206213,-2.469561,2.645573,-3.352026]],[[-8.720307,-0.287071,0.531834,4.834135,-7.983241,-7.855912,-9.195158,4.231864,-3.391831,-6.564486],[4.112645,6.216818,7.752723,0.401947,7.965711,9.925905,-0.664850,-4.790268,-7.150568,-0.430039]],[[-5.012702,9.780535,-7.204163,0.538448,0.641199,-1.734924,-5.342710,-2.734735,4.600080,-0.100810],[0.690333,-9.965492,6.148218,2.177335,-3.315119,-0.745820,3.362624,2.245788,-5.302872,-4.436840]],[[-1.371002,3.212822,-8.666153,-3.745700,3.575707,-7.490293,-6.424283,7.812474,1.587317,5.452591],[-6.698670,-5.440399,9.322640,4.712697,6.213669,9.773999,-6.685357,-4.325485,3.091052,-0.480181]],[[-3.343819,8.483268,2.977968,-5.162175,-6.390299,-9.420068,-0.846583,-1.732917,-3.552069,3.884334],[7.960026,4.682903,1.092436,-2.369928,-7.136132,-4.051317,2.297796,5.342111,-2.661951,4.923403]],[[-2.140004,9.006107,-2.185782,-8.289771,8.132868,-2.605180,5.017176,-7.639042,-9.462172,9.489971],[4.287763,9.008135,5.838882,0.117486,-5.434638,-6.144096,-7.042889,0.521934,9.470396,2.688988]],[[-9.528214,4.176347,3.523608,-2.538296,-6.761925,-4.760587,9.235106,-4.971093,-0.436056,-0.105878],[-0.549171,9.494373,-8.096365,-8.318806,2.581064,-9.658672,6.911139,1.234492,5.652810,-0.785561]],[[8.277108,5.056660,-4.615593,4.137216,5.296141,-6.777391,3.691676,-4.218668,-9.166286,4.288334],[-6.225631,6.092557,-5.811805,-3.345362,5.830727,0.619366,7.914288,8.549050,0.987780,8.554556]]], dtype = "float32")#candidate|5635|(10, 2, 10)|const|float32
bop_5636 = relay.floor_divide(var_5634.astype('float32'), const_5635.astype('float32')) # shape=(10, 2, 10)
output = bop_5636
output2 = bop_5636
func_5639 = relay.Function([var_5634,], output)
mod['func_5639'] = func_5639
mod = relay.transform.InferType()(mod)
var_5640 = relay.var("var_5640", dtype = "float32", shape = (1, 2, 10))#candidate|5640|(1, 2, 10)|var|float32
output = func_5639(var_5640)
func_5641 = relay.Function([var_5640], output)
mutated_mod['func_5641'] = func_5641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4213_call = mod.get_global_var('func_4213')
func_4214_call = mutated_mod.get_global_var('func_4214')
call_5689 = relay.TupleGetItem(func_4213_call(), 0)
call_5690 = relay.TupleGetItem(func_4214_call(), 0)
func_5325_call = mod.get_global_var('func_5325')
func_5329_call = mutated_mod.get_global_var('func_5329')
var_5702 = relay.var("var_5702", dtype = "int32", shape = (48,))#candidate|5702|(48,)|var|int32
const_5703 = relay.const([5,10,-6,2,10,6,8,-2,-3,-4,-9,2,3,-10,-6,-2,6,-4,8,-10,3,6,-7,2,7,9,-4,1,-7,-4,-3,3,-8,-4,2,-7,-9,6,-5,7,6,-5,-9,8,9,-6,-10,-4,5,-7,1,1,8,9,8,3,-2,-4,7,4,6,10,8,-4,-1,1,6,-5,1,-6,-8,5,-1,10,3,-8,5,-4,-2,-7,1,9,1,-10,8,3,8,7,-9,1,-2,-2,7,-9,6,3,5,5,-6,8,4,9,1,3,-4,5,-3,2,-5,-8,8,-2,-3,-10,-3,-2,-2,-1,8,5,10,7,-7,3,9,-4,-3,3,3,-7,-2,5,10,6,-2,10,-1,5,-6,-9,-2,-4,-1,-2,-10,3,6,7,4,5,-4,-7,-2,2,-3,-4,6,-9,-7,-3,10,1,4,3,3,5,5,-4,-8,-6,7,-7,8,-2,-7,-3,1,-4,-4,-6,-6,-4,-6,-9,-5,7,-5,-5,-10,-9,1,5,-6,10,7,6,-8,-6,1,1,10,-7,10,-7,10,7,-8,7,3,-3,-5,6,3,10,-9,9,-8,-2,10,-9,7,-4,-10,8,-8,4,2,-9,-5,-1,1,-2,8,-5,7,-9,-2,7,3,3,-8,7,10,7,6,-8,7,3,-7,-2,-4,7,3,6,-9,9,10,7,1,-5,-1,-3,-4,2,7,-6,-6,-7,-6,8,5,-3,3,-7,6,-3,-7,-5,-5,4,2,4,-10,-10,-7,-4,-6,-7,10,5,-6,-3,7,5,7,-5,-7,9,-4,-8,9,-3,-10,4,-6,6,-9,6,6,-7,1,2,-5,-9,-1,-9,-8,5,-7,-8,10,-7,-2,5,6,-3,-6,-5,7,9,1,-8,4,-9,-2,6], dtype = "uint8")#candidate|5703|(336,)|const|uint8
var_5704 = relay.var("var_5704", dtype = "float64", shape = (6, 45))#candidate|5704|(6, 45)|var|float64
call_5701 = relay.TupleGetItem(func_5325_call(relay.reshape(var_5702.astype('int32'), [48,]), relay.reshape(const_5703.astype('uint8'), [4, 84]), relay.reshape(var_5704.astype('float64'), [3, 90]), ), 4)
call_5705 = relay.TupleGetItem(func_5329_call(relay.reshape(var_5702.astype('int32'), [48,]), relay.reshape(const_5703.astype('uint8'), [4, 84]), relay.reshape(var_5704.astype('float64'), [3, 90]), ), 4)
func_4141_call = mod.get_global_var('func_4141')
func_4143_call = mutated_mod.get_global_var('func_4143')
call_5719 = relay.TupleGetItem(func_4141_call(), 0)
call_5720 = relay.TupleGetItem(func_4143_call(), 0)
bop_5734 = relay.logical_and(call_5689.astype('bool'), var_5702.astype('bool')) # shape=(10, 9, 48)
bop_5737 = relay.logical_and(call_5690.astype('bool'), var_5702.astype('bool')) # shape=(10, 9, 48)
func_3860_call = mod.get_global_var('func_3860')
func_3862_call = mutated_mod.get_global_var('func_3862')
call_5743 = relay.TupleGetItem(func_3860_call(), 2)
call_5744 = relay.TupleGetItem(func_3862_call(), 2)
bop_5745 = relay.multiply(bop_5734.astype('int32'), call_5719.astype('int32')) # shape=(10, 9, 48)
bop_5748 = relay.multiply(bop_5737.astype('int32'), call_5720.astype('int32')) # shape=(10, 9, 48)
uop_5751 = relay.atanh(call_5719.astype('float64')) # shape=(10, 9, 1)
uop_5753 = relay.atanh(call_5720.astype('float64')) # shape=(10, 9, 1)
output = relay.Tuple([call_5701,const_5703,var_5704,call_5743,bop_5745,uop_5751,])
output2 = relay.Tuple([call_5705,const_5703,var_5704,call_5744,bop_5748,uop_5753,])
func_5756 = relay.Function([var_5702,var_5704,], output)
mod['func_5756'] = func_5756
mod = relay.transform.InferType()(mod)
mutated_mod['func_5756'] = func_5756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5756_call = mutated_mod.get_global_var('func_5756')
var_5758 = relay.var("var_5758", dtype = "int32", shape = (48,))#candidate|5758|(48,)|var|int32
var_5759 = relay.var("var_5759", dtype = "float64", shape = (6, 45))#candidate|5759|(6, 45)|var|float64
call_5757 = func_5756_call(var_5758,var_5759,)
output = call_5757
func_5760 = relay.Function([var_5758,var_5759,], output)
mutated_mod['func_5760'] = func_5760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5191_call = mod.get_global_var('func_5191')
func_5192_call = mutated_mod.get_global_var('func_5192')
call_5776 = relay.TupleGetItem(func_5191_call(), 1)
call_5777 = relay.TupleGetItem(func_5192_call(), 1)
func_2021_call = mod.get_global_var('func_2021')
func_2024_call = mutated_mod.get_global_var('func_2024')
const_5784 = relay.const([-1.751346,1.752090,-3.349713,5.698398,1.299109,4.335536,-0.475847,-2.123712,-7.951139,-2.406660,2.085103,-3.210905,2.560202,-6.332930,-4.225244,-1.564022,-7.896929,8.069581,-5.022263,5.546274,9.015166,-3.038053,-0.248146,8.729159,2.353883,-5.305765,6.686156,8.195348,9.182671,8.964375,-6.739101,-0.669215,8.623118,-3.887986,-1.677791,-6.971630,-0.913328,7.348687,7.248487,8.602820,-5.249282,-0.766065,-2.824137,-2.365851,5.088604,-4.806880,-6.330192,-2.126492,-2.817815,6.424078,4.016633,-9.551353,-8.653271,-1.201288,7.518518,0.640778,6.426819,3.054600,6.625531,9.175653,7.969229,-9.804920,-2.297937,-8.340656,8.034871,1.392360,3.582879,3.256972,1.400700,4.209516,8.964383,7.774292,-5.182156,9.534813,-4.239362,2.632156,-0.194791,9.732207,-4.953387,1.368883,-7.357814,-7.066179,4.436480,5.606296,-1.579795,4.926991,0.870312,-8.877808,5.716765,1.737312,5.572893,9.556874,5.859042,-7.634173,-3.981410,8.991534,6.394215,-2.632246,0.221419,1.802364,1.608343,-2.443009,4.112966,-7.036351,-2.889387,9.364873,-2.019469,1.621699,1.801274,-3.403872,5.665141,-9.519801,0.434336,6.990634,6.804054,-1.268756,3.857132,9.709945,-5.565351,8.445685,-2.495221,-8.724091,-8.302481,-3.637937,6.532824,9.926841,-3.017109,6.527757,7.913201,1.074200,-3.132087,1.415796,-5.547559,-3.792366,-6.315657,1.425869,-8.109212,-7.951417,3.517848,1.194388,8.467590,1.133208,-7.361986,0.639769,-6.679762,-4.583284,5.843939,-6.597224,3.844584,-3.023956,3.940270,-6.775955,3.898676,-8.958457,0.549749,9.366516,-0.553027,-0.251789,-3.202381,-9.365204,-4.302216,8.504996,-2.454263,0.927463,-7.698076,-8.843188,0.036505,-1.725754,5.314583,9.601246,-3.129417,1.206893,-1.768335,5.130792,4.955369,0.770482,5.937332,2.016126,-2.977831,3.806896,-5.926017,-5.060735,-1.705484,-9.301787,0.004663,-6.998621,4.612233,7.129180,7.518256,-6.068957,-8.228938,5.766310,-6.428834,-5.907933,7.479804,3.996576,8.675999,-8.427722,-0.057286,5.868258,-9.050391,6.276610,4.333740,7.649692,-0.234188,5.135763,0.643076,-6.751857,-0.508902,8.174602,-6.773418,7.523448,-3.130083,8.325992,9.611002,8.206070,-6.864055,7.610236,4.396731,-7.745598,-6.308546,-5.428972,-7.015211,0.532280,9.702711,8.201543,2.227637,3.548895,-6.685970,4.360835,3.835038,7.653500,0.642317,9.332251,-0.427487,-6.656463,-9.494842,-7.680434,1.102926,2.066091,-4.538169,-1.566745,1.158937,-5.486646,-1.459820,8.854891,-1.030208,8.360457,3.561020,-9.703668,3.435862,-7.736369,5.513151,-7.513238,-0.967891,-3.790473,-4.502369,8.857785,-6.877914,1.210353,0.319742,6.378170,-0.457810,5.281372,5.569181,1.160447,4.194484,-0.355264,-2.173783,3.114896,-4.985118,-1.212330,0.714701,7.452509,7.771549,-8.020402,0.217281,-4.961064,7.067431,-8.408577,0.597248,3.959636,7.256695,5.547203,-0.182908,3.799866,-0.428934,-6.867838,3.758748,-2.992652,-9.176321,5.115276,-3.706953,6.139854,8.434786,-5.144575,1.788226,8.878320,-6.642314,7.377336,-7.795299,7.945339,-6.498960,-5.911780,0.805650,-4.964997,1.831208,-7.005476,9.523071,5.464094,1.493795,7.764174,8.412859,8.897292,9.982983,7.583540,7.678336,2.109850,-8.945814,0.325418,-1.300332,9.359274,7.578824,1.646847,-8.152263,-4.902693,-3.240202,-3.847479,-8.231685,1.491203,-5.836513,2.330245,-9.545539,3.028259,-1.265360,-0.705463,-5.935071,8.295190,2.265699,-3.850670,6.673104,0.032397,-7.721058,-7.460764,-2.251245,3.735659,-3.812982,-8.054748,3.199869,4.352370,4.844342,-5.210444,7.526784,4.730956,-1.336331,-9.570132,-9.626357,0.398010,-4.433059,-5.494696,-8.817224,2.830322,-3.072155,9.769101,-6.013277,-0.652018,-0.080433,9.203750,-2.166134,2.738407,8.124707,-8.081353,9.308006,-6.012732,8.409821,-2.136799,-6.519606,-8.789708,-3.636816,-3.237342,-8.543496,-9.541789,6.851533,9.137234,-6.226594,-6.353206,-9.647721,-8.384180,7.917297,1.394209,4.812641,-4.023670,-1.023764,-9.979233,-7.369654,9.980787,4.575426,7.103777,6.849939,-2.986995,8.372613,8.906915,-0.367093,-4.575027,9.751427,-2.652454,3.663820,-2.666279,-0.914260,-0.115742,-5.017776,9.385182,1.954419,-9.432343,2.147452,8.042827,-1.380356,4.650280,-0.785642,-5.581430,9.612612,-2.588861,2.806534,-1.766662,6.469594,-7.676776,-2.234920,-9.989450,-2.101393,2.055378,0.571458,1.512382,3.186142,-8.613186,-6.719534,7.249543,-1.206443,-0.403339,9.565954,7.686396,-6.281980,-3.842540,9.363485,-1.326658,7.849691,-7.567380,-3.645642,-2.703931,-5.633650,6.020883,4.915624,-5.008065,-5.626612,1.316958,-2.143604,2.515517,-4.561089,9.568588,-5.120219,-1.683099,9.620587,-7.133915,-2.367249,-7.461896,-5.133475,2.578067,-4.354813,9.694484,-5.078953,-3.681912,5.786914,4.620784,9.102557,1.028786,9.443268,-4.085568,-3.422462,-9.152656,2.181878,2.586456,4.115710,-2.564616,7.422082,-6.381475,-0.202696,-6.242366,-6.013221,-5.621118,-3.460696,4.067243,0.239960,0.749063,7.584017,-3.655137,-8.844880,-9.728048,-3.196059,5.862911,-3.398724,7.787175,5.311806,-5.357371,-5.700249,0.808307,-4.570532,-4.024739,-1.560758,-1.929885,7.443012,7.054956,-6.235883,0.778407,-0.141199,-8.733888,3.801152,1.236235,5.801081,-9.146884,-5.087853,9.430357,7.150166,-5.971260,2.317849,9.707658,0.494432,-0.891465,-8.121387,-7.473913,-1.062545,5.788376,7.731988,-2.738251,-6.159186,-2.336814,7.901030,3.063508,7.557339,-4.568112,-1.644772,7.406745,-2.502862,-3.194188,-4.461906,1.941054,4.353598,-2.416718,-2.466595,-3.325465,8.321466,2.490309,-2.041669,1.226595,5.650606,-0.785632,3.910102,2.187827,1.791485,-0.756767,7.167556,-4.613757,-6.221156,8.669924,-2.129907,5.431044,-0.521241,-7.769979,-1.898758,-4.139397,9.357599,8.085588,-1.792442,8.342917,-6.852497,2.021520,0.752181,2.154351,-6.032176,-5.500827,-0.548867,5.816643,2.474198,2.877091,3.121783,1.850132,-5.372168,-6.067219,8.683492,-4.275350,6.801551,2.158772,3.520869,0.115769,6.047359,-5.851942,5.819230,-0.889266,6.175737,-3.102418,6.739677,-2.845776,3.350655,8.371812,-0.335419,-7.047149,7.575755,-5.653856,-1.133677,0.692426,-4.585492,9.492400,7.148759,-5.951566,3.667067,6.418105,-9.243648,-1.958808,-6.311679,-8.677277,2.606199,4.080949,7.442701,-3.379574,4.653109,6.314772,5.398435,2.235003,0.033372,-5.345274,6.605188,8.283898,3.719514,7.021066,5.238079,-8.024014,-5.641692,-2.183754,0.031772,-7.287047,-4.135863,-6.153113,-5.643070,-6.599052,4.848424,9.830383,-6.441291,-1.933328,-1.389399,-0.086417,-9.324866,0.467797,-9.064157,-0.193292,-7.389398,-0.462801,-1.766183,-4.732901,-8.336061,-3.708959,9.934914,-1.459581,6.174940,7.565013,-3.607675,6.291079,-9.810059,-1.035179,-9.537034,6.167000,0.861182,0.170613,-3.753739,-9.125685,-9.995080,7.897091,-1.282579,-0.206213,-4.375449,-4.291464,9.332576,6.725234,-6.581986,-1.784586,-8.466193,5.840323,5.384995,-2.578999,-4.798441,-6.047146,8.997025,9.002310,-6.564098,1.357491,9.512621,3.194008,-4.547973,0.383236,-7.575787,5.122166,1.854016,-2.441809,-8.956457,-5.926346,-4.824355,4.629615,-8.981423,2.767222,-0.064938,-3.568380,-4.940967,-3.204424,-7.206551,9.046245,9.632397,-7.428402,6.016075,3.023993,5.469761,0.694369,2.545395,9.339876,9.002542,-8.604346,-9.514794,6.515665,-0.105359,6.509161,5.261270,-4.256827,5.587274,3.440408,2.914122,-9.227805,7.644527,-0.198522,8.555079,-2.595773,3.559435,-3.022052,8.233657,-2.332569,-7.075903,1.548936,2.875847,-1.711316,-3.245564,6.237894,3.486904,-3.950817,8.191001,1.134798,-4.576236,2.089366,-3.580058,6.847465,-7.441132,1.206420,0.980558,-0.785592,-3.366569,-6.507447,2.526490,0.871806,7.907072,7.298768,-6.619043,8.661987,-7.550815,-3.257304,0.033345,2.095825,-6.561807,-0.653646,8.159512,-6.179927,6.836366,-9.559822,-0.998962,6.148414,1.138766,5.926099,6.222215,-3.439754,3.720916,-5.121566,0.299335,-1.226927,5.194863,6.601541,-7.681441,-7.961674,-1.888576,-2.356645,-0.984741,3.559736,-1.142965,-2.065621,9.078841,6.531676,5.386704,1.301682,3.976644,-1.921699,-5.789606,5.694017,3.216495,3.200988,-2.544817,8.805215,3.926320,-8.122764,4.985593,-4.801816,-4.457184,9.120175,4.941872,-8.241646,9.961487,6.908587,-7.544253,-6.481425,1.577433,-7.870421,3.685889,-5.082009,-5.997512,-6.518141,6.903210,-4.805680,-4.904064,-4.799946,7.937541,9.400918,0.340267,-7.449571,2.856785,-7.416371,-7.215560,6.014425,-2.400117,6.536252,-0.204240,-3.803677,-8.577202,3.945036,-2.006720,-4.124164,-0.231696,-5.563277,8.727971,-2.024818,9.831816,2.137054,2.246962,8.939989,-9.311596,-0.351714,-0.268299,0.083452,1.046541,-0.692992,-8.426839,3.424094,-4.689014,-0.994948,1.264001,-5.484664,5.516193,-9.435632,-9.789436,-6.505806,-2.321119,-0.271256,4.791269,4.569993,-6.695275,4.806843,6.254478,-8.187483,-1.983587,1.303558,3.078660,9.087732,5.675011,0.493670,7.022373,-8.272141,-5.938476,1.318019,-4.325094,-6.935096,-3.576424,5.489588,5.861937,2.863495,7.929945,1.285661,-2.760994,4.912836,-3.919145,-0.373087,6.556100,-6.095622,0.859668,4.553622,-8.630835,-2.920671,9.109129,-9.224820,3.428862,6.813480,-5.781833,4.956963,1.592355,-5.438417,4.316422,1.719091,-3.846606,-7.100597,9.063994,2.597781,-9.124576,-9.769313,-3.800717,-7.912374,-7.097477,-5.337092,-1.699139,-8.398553,-2.772953,5.458272,2.314336,-0.767237,-1.249968,3.616995,2.973454,-8.903234,-9.609907,9.533085,3.478820,8.452377,4.621709,5.500756,8.470034,0.190158,-0.082375,-2.801743,-4.783294,2.894132,4.966826,-3.937196,-2.807346,-3.437822,-1.748045,8.868496,3.664605,5.918427,-3.711287,-4.017905,-6.910599,9.472426,4.000786,-2.082837,6.797670,-1.658341,-5.585951,9.624566,6.463858,-4.664383,5.143541,-5.317414,-8.695929,-0.716136,-1.513632,-2.410851,-5.839242,7.855022,3.549227,1.907068,-3.429288,-4.683003,4.608494,0.659416,5.306290,-8.784622,9.205194,-6.862652,-2.948516,-8.042866,0.808628,-8.986043,-0.126721,2.058628,5.372017,-8.491816,6.037563,3.315196,-7.764029,3.973265,-1.787950,8.054348,-4.777650,6.212057,-7.801867,4.930668,-6.925971,5.853680,-4.669882,7.934434,-5.667503,9.625034,-5.282739,-7.658128,8.186336,-9.129937,5.057239,4.273525,2.802763,-7.326049,-2.188510,-6.003272,7.901618,0.912761,-4.536132,-2.083462,3.338209,-1.443683,-0.903330,-7.664068,3.790291,9.322823,-3.940622,-1.235565,9.252075,9.251646,7.972283,-6.186894,-6.287326,-1.109247,-4.689690,7.826018,-4.785963,1.569576,-0.830958,-3.236980,6.280969,-1.873917,-8.250418,3.708702,0.123472,8.348406,-3.364359,-6.665206,1.376855,-4.195803,2.071562,1.936898,5.526415,-1.129161,5.810431,0.875012,-2.338381,-3.161517,6.875132,-3.934222,7.070905,2.399407,4.041503,-1.646650,-6.128958,7.972335,-7.615712,7.857724,5.262617,5.915934,-4.116216,3.759699,-4.744221,7.240231,-3.977835,-8.433377,2.347402,3.614107,4.178234,8.317046,-1.530161,0.661114,-9.186220,6.828070,-4.098724,-5.086508,5.211623,5.012953,6.067602,0.345001,-6.783615,1.747414,3.836178,9.179813,-7.380908,-4.095411,6.510501,3.452285,-8.596166,1.555621,4.353613,8.933435,-8.827342,-1.531608,1.668081,2.691304,-8.709556,9.065918,5.915277,-0.564706,-6.191245,7.794351,2.597221,8.630583,0.754134,-6.574762,-7.774571,4.783285,7.260261,-0.530569,-9.739255,-1.429118,3.643261,-5.229460,-1.596296,-4.971666,-8.050573,-2.503886,7.049062,1.891818,6.958209,5.036395,-2.848102,-3.155911,8.033181,-8.705506,-8.513810,-2.089776,4.798070,-5.359424,9.526353,-3.400074,-6.939506,3.269566,-6.263854,-1.018102,6.167561,9.246937,5.015863,9.479439,-0.135248,-2.013074,-4.752081,-9.725839,0.069334,-6.858599,-9.899589,-1.331974,4.419201,-5.212800,7.594434,5.931006,-3.059066,-2.830051,-7.255726,-1.041493,8.864239,4.854200,2.180812,7.403135,2.971922,-9.268714,-5.704026,-0.821713,-4.826932,4.700975,-5.875259,-8.732273,5.192016,-8.957497,-9.205878,5.879742,5.959844,-7.165597,-5.912462,6.631983,5.257073,6.537805,5.171142,9.915014,-4.004598,1.385323,-7.588785,-1.134241,-7.883792,1.372564,9.815045,-3.089815,-8.247073,-8.487999,5.830238,-5.016056,7.323898,-9.984159,9.667466,-9.957734,3.884797,-8.055725,-4.461996,2.152500,3.361112,0.885792,4.732075,7.023071,-3.164896,6.360017,-0.132011,-9.143206,4.426885,-5.876934,2.665104,3.445671,-2.588313,-7.643121,-4.222598,7.393388,-5.313004,-4.150752,-5.837780,3.692785,9.000673,-1.067294,-7.612428,4.147274,-9.209962,1.773856,4.413365,-9.167170,-0.259389,-5.987477,-3.747316,0.371637,-4.873028,4.281173,9.994255,-1.872287,2.505724,-8.508451,6.812128,6.808229,8.626486,0.756322,3.784465,-4.036760,-9.781335,-6.904137,-4.474781,-7.521100,-5.645768,-5.853305,-0.348379,-2.424155,3.425534,-0.775039,3.900354,-7.889393,-5.644030,7.143509,2.721846,1.568642,-9.976919,1.358759,1.676110,0.420180,5.033788,-6.203372,-5.337824,2.583896,7.956511,5.195492,9.580805,-0.685760,3.133012,-1.001349,2.762138,1.808045,1.006180,8.113139,-0.679696,-7.847899,-7.997588,5.013303,-1.245371,-8.571805,-1.840115,-7.017926,-7.922081,8.265919,-6.856369,-4.286148,-9.373965,8.152060,-9.323745,-5.170094,5.061630,-0.163966,1.015936,1.320761,-7.869238,-0.251024,6.782723,3.673373,9.749562,5.058000,-0.315084,1.416737,9.065966,-5.744495,2.444548,-9.424704,-0.806191,-3.329421,0.795178,9.991895,-2.456061,-9.617333,-3.791145,9.171610,8.617426,3.434625,-4.074350,-1.099255,4.791542,-0.052630,6.216769,4.738300,8.172064,-0.129556,1.946000,6.673646,7.455633,0.133316,2.123373,5.333202,-2.372893,-9.133354,8.554079,-8.217396,7.840162,-6.952548,-1.843308,-6.278733,5.223408,-3.937742,-9.683322,-0.103168,4.197188,4.358388,-6.570072,5.294928,2.196066,-4.770588,-2.240923,1.574759,6.237793,6.335378,-5.450959,9.887024,-3.611022,-7.448059,9.812655,-1.872860,2.922372,5.949885,-1.506513,-8.261507,-2.187916,-4.207311,3.843439,2.151250,3.364132,-5.634917,-6.628629,-5.403982,2.272652,-7.407769,1.758626,-7.497229,-2.587388,2.731532,-5.719880,2.804854,-5.835908,-8.988954,6.542405,-1.023312,-6.230689,-3.035129,-2.135381,1.940675,-3.508384,4.144676,-0.595500,-5.879728,9.238163,5.346213,0.076610,6.729366,-9.962990,2.165983,7.636104,4.711567,6.733316,-6.233287,-7.551079,0.692167,6.176593,-1.211324,-8.828759,9.424724,-3.411061,-4.828130,3.411871,1.993200,3.738125,4.648026,-2.040487,-6.783131,6.374091,-2.609654,-4.212267,-5.603250,-6.830210,7.233712,7.804326,-9.316510,8.261461,4.214998,-9.686730,-3.045229,5.026555,-2.444262,-4.354924,9.841560,-2.818343,9.790558,-6.407562,-3.602641,4.164682,7.338850,-0.719037,-7.785518,-5.367448,-3.538278,1.645602,-8.971370,6.021248,-2.609532,1.538301,6.903736,8.299637,-9.405850,-7.521644,-3.833171,-1.329437,-8.246551,-9.462341,-8.014665,-7.495713,8.692388,-0.216396,-6.830726,3.097402,1.117446,5.012539,-4.678884,-2.648790,-5.243163,0.902239,-9.531336,-5.362191,6.284453,7.348488,-5.658769,-9.091820,3.948050,7.811878,-7.791571,3.070038,-1.348869,-4.644172,5.327149,0.581706,4.947583,2.841326,9.920993,-6.135749,-8.624034,-9.931134,0.298207,-4.915436,9.187977,8.611605,-3.029505,-5.556202,9.768499,0.282117,1.962449,-7.944302,-0.341739,-0.055705,3.525385,-0.878552,-2.097054,-7.699408,7.476833,9.359748,1.415249,2.777071,8.010619,-4.777218,-3.993661,3.373624,-2.564292,7.935855,3.263820,-0.555001,-4.668111,-1.422832,-5.206735,0.947210,-3.649393,-0.442934,0.033486,0.823810,3.913031,3.192342,-4.337531,4.233829,-5.344017,2.710503,-2.954968,-8.999952,-5.995498,-1.642274,-4.963969,-0.894148,-7.954209,-1.237311,-5.525271,-5.926731,7.922365,-1.080466,-7.107006,-1.678776,-5.636496,1.191446,-0.222789,9.320949,-1.057789,7.506713,9.655805,6.028563,-7.747387,8.497129,-2.898945,7.849662,0.197526,8.459218,6.797321,-3.812698,2.541265,2.506595,-3.670467,-2.930807,-3.878275,3.997926,4.593491,5.124300,-5.219567,7.367893,-1.685890,-5.823520,-0.058549,8.948869,0.193513,3.955661,5.323701,-9.962668,0.651078,8.170569,-6.957780,-5.979161,5.529508,-7.164432,-6.984523,-3.465429,-7.873384,2.423975,-3.965051,-0.643106,-6.179615,-9.784330,-7.167253,9.290735,1.273202,5.861118,7.325668,-5.719071,2.236083,-5.996879,-8.962094,-6.516597,8.817888,3.676879,0.738616,-3.081597,1.337500,8.279949,6.008281,8.838827,4.860578,8.755031,-0.720565,-2.706046,-7.723998,-2.488802,2.661488,0.316187,-7.157187,1.468251,-9.416488,2.105582,-7.141941,-0.398647,-8.576960,0.991736,-8.984303,-0.875780,-3.315980,4.883047,-6.814010,3.793822,-4.252594,-1.445750,9.374811,-2.879903,7.864142,4.478989,5.405809,-9.064650,3.698648,7.842280,-5.700893,3.744784,-0.209708,8.135039,-0.835441,1.851279,1.230400,2.401387,4.821884,-6.312070,8.116514,-3.398716,4.936831,-4.755330,-7.280590,6.377185,-0.233371,0.789285,5.049063,9.158181,6.576400,-7.363951,-0.947751,7.127629,-0.453124,1.596025,3.444675,-3.035234,-4.230643,-2.261579,-4.558090,5.965228,-2.440506,-0.697318,6.205796,8.451056,-8.564401,6.784996,1.547502,-1.356479,-8.200891,5.468850,8.898825,4.954167,8.470181,5.122680,8.032017,-3.774772,9.763994,0.442365,-0.521419,-7.363445,-9.325476,4.050748,-7.241642,2.486098,6.702704,2.170859,-0.807231,-0.793658,-3.504148,-8.342279,-0.468494,5.442731,1.816890,-2.300881,9.803915,-1.068819,-7.427980,0.720973,0.112972,-3.638200,2.702556,8.498790,-7.677480,3.916373,0.746579,-3.584352,-9.521722,-9.546036,-8.816308,5.043485,5.654577,6.004709,-8.569031,-0.976652,-3.710661,-0.478049,-9.920560,9.768422,-4.246510,8.069461,-7.878373,9.390676,7.474953,-1.935764,9.533581,7.873419,6.875688,-7.924019,7.411067,0.838674,0.346703,-8.295963,-4.899453,-5.586214,-5.702117,-3.309581,1.379985,-5.604731,1.156460,-0.522795,-2.570873,3.262745,1.891409,9.053282,0.988293,-2.169770,9.736180,-6.234184,-6.901745,-6.182385,5.523073,-1.268284,-8.942390,6.148085,6.951581,-9.611438,-9.894804,-1.123390,-8.409419,-2.041466,-7.504038,-8.561147,9.474120,6.385179,-1.294550,4.302072,4.340885,-5.664991,-2.454161,9.485289,-1.984582,8.654325,-6.160851,-2.380761,-6.103401,-0.443405,2.779892,-3.597899,7.973952,-4.624159,9.856521,0.736312,5.391510,-4.640080,-2.614069,-8.663794,-2.389019,5.169635,2.374652,0.254398,-7.980530,-6.412066,-0.427832,3.423884,4.125644,2.976287,1.319674,3.446813,0.417001,-1.996832,6.169615,-6.427888,-4.707119,-5.583747,7.660559,9.896564,5.349451,6.040203,-8.267829,-4.192272,-7.317064,-1.540945,-9.683572,9.206604,-0.915869,2.619500,-5.983784,0.939769,0.110023,-8.441235,4.964591,1.733161,3.250752,-3.533240,0.885880,9.633153,8.520432,5.607040,2.128488,2.855052,-2.607849,-3.959110,-0.417448,8.684341,4.521345,-7.624417,-0.624586,-1.085828,-4.084001,1.198110,6.619108,6.668578,4.711674,-0.956430,0.162609,-3.179633,4.995062,-2.892099,-8.567456,6.468570,1.051125,-1.214916,2.556420,-8.789006,4.629775,2.134862,-5.872459,9.666290,8.461588,0.576696,5.384975,-0.030407,-1.720649,-7.896746,2.119011,-0.792544,9.456580,-3.624875,9.919636,-6.516339,-5.614506,7.762735,8.331543,-5.204921,0.519833,8.068513,4.283543,1.570645,3.987451,-1.115312,5.468901,3.335369,2.278412,-5.520026,-9.106961,-7.721106,-5.610987,-8.112732,-8.449215,5.480794,-9.933841,3.391146,-8.903287,6.388268,-9.789884,-0.460319,-7.074509,6.780984,5.803891,0.417414,-2.290239,8.164620,1.944157,-0.385862,-6.810752,0.406470,6.700646,8.909858,3.595712,3.158975,-6.327298,-1.639197,7.011086,3.149733,1.600096,3.570952,-2.618581,-9.019390,-0.207719,4.570153,-9.691721,4.766700,3.757123,-5.007302,2.728333,5.570435,6.526383,-8.848805,8.800823,-4.127940,-6.847637,-4.075919,-2.195988,1.474456,-2.069339,9.561323,4.493704,-6.342755,9.998703,-1.703542,-8.889613,4.526516,6.021304,-6.447949,3.100123,1.688412,-5.164811,-0.402413,-3.495331,9.515012,-9.354878,-4.974736,7.742941,1.619350,4.597813,1.890361,4.864467,9.772565,3.723051,4.520184,-3.488370,-3.258625,-8.451239,2.914082,-6.848723,9.266895,-4.867315,6.323782,-9.606455,-4.889514,-6.893843,4.053973,-7.823910,-5.649643,1.606416,-8.521265,-4.883545,-2.176917,0.175865,4.698542,2.482748,5.111709,-5.375281,9.526805,7.214135,-4.962468,-0.458845,9.221483,1.639718,-9.668493,3.844550,-6.837406,6.656700,-0.606644,3.367407,7.593380,3.880719,-4.036261,4.933448,-0.951618,2.515147,-7.494539,0.370274,1.983512,5.715985,2.791367,-9.545910,-5.121625,-3.913359,0.434313,-9.387404,-5.972771,3.778235,-1.886519,1.798182,1.257816,2.803353,-4.884657,5.441276,6.485355,1.757115,7.570372,7.760008,7.305505,-9.583526,1.451585,6.516907,-3.608525,-3.514367,4.915430,-8.051604,-0.185331,-8.420777,-2.601774,-1.278366,-8.727277,-7.249319,-9.688540,7.163772,1.065727,-8.428717,7.000019,7.565793,-8.711241,-3.155758,5.493853,-1.777536,-5.742353,-6.167502,-6.883696,6.967338,-3.738836,-4.679236,0.335911,-2.080115,3.013008,9.519345,4.579908,6.770653,-2.554287,2.447411,-2.530513,0.352015,5.744512,3.348973,2.231753,-8.532572,-0.493583,-9.815343,6.583931,-5.848285,6.993581,6.546079,-1.467018,-9.074364,-8.262069,-7.782727,9.947882,6.491125,7.193560,-5.306843,1.302768,-3.736605,4.179247,0.642511,-5.985128,4.649865,4.660529,-4.327485,4.482774,-4.663627,-5.577936,-0.788230,6.657363,-6.149003,-0.763961,7.242824,-8.635673,9.395466,-8.204271,-1.892218,5.212970,-9.407401,-1.699735,-1.445719,5.333767,2.887248,-1.702047,1.446171,7.682432,-9.894850,-7.189005,-7.577878,-0.433122,-9.886883,-2.425272,4.461689,-8.158996,3.131725,-3.808666,2.935341,-7.425053,6.565475,-3.489107,-0.499706,8.334285,-0.702867,-6.091324,-7.310852,-0.006485,2.979132,5.064122,-3.891121,-9.083931,-1.542921,-3.132039,-3.259446,-4.754019,9.596671,-1.267179,-3.922583,-2.122341,3.650264,6.394026,0.259896,-6.000364,1.118017,1.685948,-9.953761,8.467398,-3.122094,-8.255222,-6.537150,7.534626,8.354182,-9.950588,2.299384,-0.182755,3.966535,-4.286348,-7.441578,-3.643380,-2.717379,7.972084,2.319639,9.565426,-1.429636,9.381596,-1.608867,-9.883498,-0.740650,7.795821,-7.105711,7.042635,-9.169206,-5.753715,-0.950903,-8.800129,6.747272,8.153320,-1.702353,-6.462778,-4.080223,9.234706,-5.646512,2.535099,-2.044912,-3.051650,-6.722614,2.791925,3.685121,7.102387,-4.431572,-6.868996,-4.696901,-5.073185,-0.746987,5.253930,-1.038939,7.604626,9.867392,-5.888693,-3.223974,-5.831165,-4.768320,8.608179,3.358066,5.584749,-2.960443,0.093509,-0.805655], dtype = "float32")#candidate|5784|(2240,)|const|float32
call_5783 = relay.TupleGetItem(func_2021_call(relay.reshape(const_5784.astype('float32'), [16, 10, 14]), relay.reshape(const_5784.astype('float32'), [16, 10, 14]), ), 0)
call_5785 = relay.TupleGetItem(func_2024_call(relay.reshape(const_5784.astype('float32'), [16, 10, 14]), relay.reshape(const_5784.astype('float32'), [16, 10, 14]), ), 0)
var_5791 = relay.var("var_5791", dtype = "float64", shape = (11, 8, 14))#candidate|5791|(11, 8, 14)|var|float64
bop_5792 = relay.not_equal(call_5776.astype('bool'), relay.reshape(var_5791.astype('bool'), relay.shape_of(call_5776))) # shape=(11, 8, 14)
bop_5795 = relay.not_equal(call_5777.astype('bool'), relay.reshape(var_5791.astype('bool'), relay.shape_of(call_5777))) # shape=(11, 8, 14)
bop_5801 = relay.power(const_5784.astype('float64'), relay.reshape(call_5783.astype('float64'), relay.shape_of(const_5784))) # shape=(2240,)
bop_5804 = relay.power(const_5784.astype('float64'), relay.reshape(call_5785.astype('float64'), relay.shape_of(const_5784))) # shape=(2240,)
uop_5805 = relay.asinh(call_5776.astype('float64')) # shape=(11, 8, 14)
uop_5807 = relay.asinh(call_5777.astype('float64')) # shape=(11, 8, 14)
output = relay.Tuple([bop_5792,bop_5801,uop_5805,])
output2 = relay.Tuple([bop_5795,bop_5804,uop_5807,])
func_5809 = relay.Function([var_5791,], output)
mod['func_5809'] = func_5809
mod = relay.transform.InferType()(mod)
var_5810 = relay.var("var_5810", dtype = "float64", shape = (11, 8, 14))#candidate|5810|(11, 8, 14)|var|float64
output = func_5809(var_5810)
func_5811 = relay.Function([var_5810], output)
mutated_mod['func_5811'] = func_5811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3567_call = mod.get_global_var('func_3567')
func_3569_call = mutated_mod.get_global_var('func_3569')
call_5835 = relay.TupleGetItem(func_3567_call(), 2)
call_5836 = relay.TupleGetItem(func_3569_call(), 2)
func_1697_call = mod.get_global_var('func_1697')
func_1700_call = mutated_mod.get_global_var('func_1700')
const_5872 = relay.const([-9,-7,-7,1,5,2,-5,3,-10,3,9,5,-4,-1,6,-10,-2,-2,-4,-2,-4,-6,-3,-1,9,-3,7,6,-4,4,8,5,-1,-10,3,3,-8,-8,-10,-6,-4,9,-4,3,-5,-9,3,2,2,10,-4,3,-3,-3,-2,4,-7,-7,2,-10,-9,10,5,-9,-2,4,-3,7,10,9,-10,-7,-7,-7,-4,-6,6,-6,-7,-7,3,4,8,10,-5,7,-1,2,9,-9,-6,6,2,-10,9,8,7,-8,7,-3,8,-10,4,-10,-1,8,7,-7,7,8,5,8,1,-8,-5,-3,-1,-5,-2,10,6,-1,1,2,5,4,9,3,7,10,-4,-6,-5,2,7,-3,1,6,9,-1,-7,6,6,-7,5,-6,8,4,4,3,1,4,7,5,5,2,-1,-1,-2,-8,4,3,-6,7,6,-1,5,8,-5,-10,9,6,2,6,6,8,8,1,-10,-7,-10,5,6,-7,-8,-3,9,-6,-9,-3,-6,4,-4,-1,-5,5,7,-9,3,5,-3,8,-2,-2,-7,-5,-8,1,3,-10,-10,-4,-3,1,-10,-5,7,-6,-8,-9,3,-9,2,-7,-2,3,-10,-1,1,8,10,-6,-9,-5,9,3,5,-7,4,2,-10,9,4,-4,-2,6,-8,-9,3,5,8,-5], dtype = "int16")#candidate|5872|(252,)|const|int16
call_5871 = relay.TupleGetItem(func_1697_call(relay.reshape(const_5872.astype('int16'), [3, 12, 7])), 0)
call_5873 = relay.TupleGetItem(func_1700_call(relay.reshape(const_5872.astype('int16'), [3, 12, 7])), 0)
func_5023_call = mod.get_global_var('func_5023')
func_5025_call = mutated_mod.get_global_var('func_5025')
call_5876 = func_5023_call()
call_5877 = func_5023_call()
func_5127_call = mod.get_global_var('func_5127')
func_5129_call = mutated_mod.get_global_var('func_5129')
var_5884 = relay.var("var_5884", dtype = "float64", shape = (616, 2))#candidate|5884|(616, 2)|var|float64
call_5883 = relay.TupleGetItem(func_5127_call(relay.reshape(var_5884.astype('float64'), [11, 8, 14])), 0)
call_5885 = relay.TupleGetItem(func_5129_call(relay.reshape(var_5884.astype('float64'), [11, 8, 14])), 0)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
const_5896 = relay.const([[-2.992669],[-3.892880],[9.060582],[-3.093627],[3.186995],[9.044363],[0.033582],[7.493114],[-4.437353],[8.795076],[8.605969],[0.350405],[-8.845980],[7.924334],[0.131179],[4.006190],[8.680789],[2.164055],[-0.859186],[-1.616376],[9.357199],[7.011481],[6.766052],[-7.571493],[-8.996638],[-2.394779],[-9.191820],[6.141018],[3.476824],[2.989178],[-7.657957],[-0.090617],[-5.765095],[7.055504],[2.067971],[-2.793429],[1.998953],[8.686042],[0.368555],[-8.999996],[0.190611],[2.944368],[-3.439015],[-6.283787],[-5.181041],[-8.776081],[-7.182165],[-4.845917],[-0.810138],[2.891368],[1.035429],[-9.816376],[6.556468],[1.831282],[2.522390],[7.409596],[-2.092781],[3.957074],[6.303206],[-6.485953],[2.501806],[-4.035960],[2.541392],[0.408245],[-2.752374],[4.434449],[-8.764120],[-2.197704],[1.808377],[-1.841473],[1.905115],[8.407380],[4.320350],[-9.421054],[-4.519497],[-1.112067],[4.955101],[-8.820945],[5.995141],[-0.782305],[-2.602298],[6.498353],[-0.404609],[6.683658],[1.337889],[-5.646870],[1.336828],[-2.715345],[-5.801317],[4.711678],[-2.538033],[3.772417],[-4.777415],[-5.321418],[7.947313],[-5.712269],[4.874366],[-9.835642],[1.553337],[8.112882],[-6.802807],[-6.782507],[-5.495612],[-2.451632],[7.503032],[5.891573],[7.382682],[-7.611780],[-1.349442],[6.828869],[0.016230],[-5.804822],[4.029418],[-8.676824],[-7.306271],[3.247158],[-1.374530],[-1.815142],[-3.999602],[6.736395],[-6.175992],[6.812248],[8.627761],[7.817907],[6.223375],[1.718827],[-8.383265],[2.866642],[9.333836],[6.821251],[3.145232],[-6.664431],[-9.018359],[-4.067954],[4.628111],[-1.535776],[5.779922],[8.069090],[7.929574],[-8.117395],[3.530088],[-2.673254],[7.153281],[7.306486],[2.245789],[-3.585869],[8.333517],[-1.604363],[9.264761],[-4.212059],[2.345552],[-3.036450],[7.134999],[3.931837],[1.304719],[0.854629],[-9.847580],[-2.901982],[9.322246],[-1.426618],[-5.745008],[8.337850],[8.632299],[9.090670],[9.125586],[6.738963],[6.776050],[2.447576],[7.516658],[3.600571],[-4.293801],[8.993450],[-8.460527],[2.776012],[9.360561],[8.105377],[-8.387250],[0.238627],[-8.396194],[2.968036],[-0.673571],[-6.872162],[-3.290926],[-6.013003],[4.597762],[-0.870005],[-8.810214],[-3.978833],[-6.604818],[-4.119094],[9.254827],[8.595094],[3.320662],[4.549927],[-8.813743],[5.920672],[1.691852],[-4.693370],[0.464566],[3.364300],[-7.711816],[-5.838974],[7.369013],[-9.276429],[-6.767753],[3.583619],[-2.176192],[-5.709971],[7.677659],[7.985816],[-8.990335],[-6.939554],[4.988990],[2.614928],[-0.556970],[8.185905],[8.443089],[7.300796],[-3.634721],[-8.572103],[5.766156],[-5.257325],[-5.932224],[0.052503],[-9.915508],[8.035449],[2.603214],[-3.230216],[-6.840948],[5.253933],[-9.548292],[-3.864141],[-1.992859],[-7.745169],[2.454343],[-0.001204],[-4.115856],[-8.144292],[4.906142],[-1.775160],[-1.676162],[-0.015714],[0.729113],[-1.411097],[-0.948813],[-4.387646],[-1.576138],[-6.207453],[9.332449],[0.710207],[2.358099],[3.233486],[-8.878722],[0.534647],[6.940156],[6.602506],[4.536315],[8.802796],[-2.948420],[0.625737],[7.134506],[3.916893],[-2.608214],[-7.739283],[-0.933844],[-8.844395],[4.694160],[0.625179],[4.406692],[0.974054],[-7.339254],[-7.318027],[-8.015586],[9.155235],[-8.232330],[-7.542366],[-9.201268],[2.314142],[9.016131],[-7.060213],[-3.612302],[-1.435390],[-7.403531],[4.707140],[-3.364766],[-7.448125],[-6.718074],[-6.671173],[-0.260790],[4.000402],[-3.660488],[-1.900636],[-9.879478],[3.973859],[-4.012810],[0.453078],[-8.402950],[-3.191589],[-6.615279],[-2.800607],[0.371028],[6.214726],[-1.813345],[-4.845949],[0.338034],[8.457814],[0.970623],[8.310818],[3.792559],[-2.933938],[-8.663027],[-6.305744],[3.537584],[-5.285370],[8.186666],[-9.140447],[6.958612],[-7.907701],[8.096432],[1.964131],[-0.559153],[1.085267],[-3.809015],[8.963213],[7.631468],[5.707145],[-4.822423],[3.681270],[5.053749],[5.973912],[-8.449935],[0.124470],[0.433422],[9.704021],[-1.625730],[-2.914605],[2.869980],[2.922798],[-0.148636],[-9.451188],[-0.027198],[2.989084],[0.723100],[-2.638766],[-7.480083],[7.974607],[6.814797],[1.979698],[-6.812695],[9.298595],[8.320377],[-7.185900],[4.077020],[-8.388450],[-8.299832],[-5.407754],[6.731399],[6.036552],[-1.322710],[2.497301],[1.699342],[0.709915],[3.558491],[-8.783459],[-8.903844],[-5.195609],[5.663568],[-1.843313],[-3.696216],[-5.906783],[0.379619],[2.699541],[-1.412980],[-6.526593],[-9.943236],[-7.763566],[-3.949293],[-4.217692],[-9.512708],[-2.172770],[2.049412],[-9.123053],[1.244642],[1.359170],[6.037616],[-1.465249],[-0.468057],[5.867132],[4.447762],[3.117471],[1.575132],[9.664380],[-3.436847],[3.073061],[-2.534243],[4.234920],[3.938403],[-4.084778],[-3.619257],[-3.427664],[7.287095],[8.171152],[5.997799],[7.967524],[-9.424310],[-0.436700],[-3.919421],[5.241787],[-0.492991],[5.300500],[-1.842720],[-3.120026],[-1.813992],[-1.468684],[-4.319206],[-0.895225],[-2.803508],[-4.370665],[8.012244],[-9.406515],[-1.094743],[7.220753],[-1.778907],[0.490949],[-9.897458],[-7.525723],[4.322780],[-0.930627],[1.641695],[6.153130],[7.574945],[-4.178645]], dtype = "float32")#candidate|5896|(432, 1)|const|float32
call_5895 = relay.TupleGetItem(func_3463_call(relay.reshape(const_5896.astype('float32'), [4, 108])), 5)
call_5897 = relay.TupleGetItem(func_3465_call(relay.reshape(const_5896.astype('float32'), [4, 108])), 5)
bop_5913 = relay.floor_divide(call_5835.astype('float32'), const_5896.astype('float32')) # shape=(432, 600)
bop_5916 = relay.floor_divide(call_5836.astype('float32'), const_5896.astype('float32')) # shape=(432, 600)
bop_5918 = relay.less(bop_5913.astype('bool'), call_5835.astype('bool')) # shape=(432, 600)
bop_5921 = relay.less(bop_5916.astype('bool'), call_5836.astype('bool')) # shape=(432, 600)
func_4141_call = mod.get_global_var('func_4141')
func_4143_call = mutated_mod.get_global_var('func_4143')
call_5926 = relay.TupleGetItem(func_4141_call(), 0)
call_5927 = relay.TupleGetItem(func_4143_call(), 0)
output = relay.Tuple([call_5871,const_5872,call_5876,call_5883,var_5884,call_5895,bop_5918,call_5926,])
output2 = relay.Tuple([call_5873,const_5872,call_5877,call_5885,var_5884,call_5897,bop_5921,call_5927,])
func_5963 = relay.Function([var_5884,], output)
mod['func_5963'] = func_5963
mod = relay.transform.InferType()(mod)
var_5964 = relay.var("var_5964", dtype = "float64", shape = (616, 2))#candidate|5964|(616, 2)|var|float64
output = func_5963(var_5964)
func_5965 = relay.Function([var_5964], output)
mutated_mod['func_5965'] = func_5965
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5975 = relay.var("var_5975", dtype = "float64", shape = (8, 10, 8))#candidate|5975|(8, 10, 8)|var|float64
uop_5976 = relay.asin(var_5975.astype('float64')) # shape=(8, 10, 8)
output = relay.Tuple([uop_5976,])
output2 = relay.Tuple([uop_5976,])
func_5980 = relay.Function([var_5975,], output)
mod['func_5980'] = func_5980
mod = relay.transform.InferType()(mod)
mutated_mod['func_5980'] = func_5980
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5981 = relay.var("var_5981", dtype = "float64", shape = (8, 10, 8))#candidate|5981|(8, 10, 8)|var|float64
func_5980_call = mutated_mod.get_global_var('func_5980')
call_5982 = func_5980_call(var_5981)
output = call_5982
func_5983 = relay.Function([var_5981], output)
mutated_mod['func_5983'] = func_5983
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6094 = relay.var("var_6094", dtype = "float32", shape = (12, 6, 13))#candidate|6094|(12, 6, 13)|var|float32
const_6095 = relay.const([[[9.551967,0.456867,-4.563963,6.309090,3.370792,4.982388,-7.379890,4.926145,9.589805,-0.446588,-3.327077,7.521032,-4.923780],[-6.698759,-1.985548,-2.138600,-4.414303,7.140655,-7.619531,-2.788377,5.959011,3.548276,-6.921141,4.346071,-9.447231,5.643610],[0.573385,3.902671,0.044165,-2.034423,-8.166639,0.881770,-9.941478,2.951062,3.594145,-7.870895,6.626228,9.967873,6.620239],[6.924349,-9.121795,-0.492225,3.513555,0.266154,-5.237328,5.458578,-5.232167,1.784356,5.142026,-3.441284,-9.547294,7.793046],[-9.482071,6.984453,-1.840011,6.384609,-2.250517,-7.550155,4.541866,-5.431554,0.740636,-2.560068,7.166997,-0.353817,-7.963808],[3.008560,6.601528,3.817010,2.909008,3.719079,0.992056,-0.384485,3.378051,-8.104399,-0.682222,-4.892028,-5.230316,-9.492807]],[[-4.225643,-7.683095,5.262297,9.101994,-1.558116,-8.618932,-7.618956,5.714010,-7.745189,4.029024,-5.471463,-4.816779,-0.983728],[-1.973008,-9.715916,-8.015005,1.911327,9.399037,4.650934,-7.685817,7.873014,7.704853,-5.436653,-9.920140,3.874749,-3.596629],[3.082808,-9.114337,5.050178,-6.560202,7.785114,-7.870541,4.283527,2.777110,4.440499,-5.749616,-0.441985,-0.454405,0.402073],[7.416705,-3.726726,-0.131944,3.741681,3.414588,-5.355120,-8.304323,9.691830,-4.383235,-0.248817,6.836419,8.926806,4.145735],[2.878008,3.178659,-3.192805,4.584510,-1.642934,-8.285897,3.032422,3.424866,2.143825,5.022499,-7.778714,5.171600,-3.504796],[-1.355702,-9.956570,2.380029,0.507488,-5.146059,-5.087680,-0.344268,-8.396733,-8.670266,4.319902,1.192520,0.673053,7.093404]],[[-9.622278,-9.460409,6.060893,4.359785,-4.557506,3.332712,4.939321,1.730555,-9.981977,-5.417203,-9.899925,-3.360153,-5.539718],[-1.567961,-9.256241,-5.413334,-4.118248,1.274917,2.576577,-6.907727,-0.475806,-4.307471,5.175375,2.930778,8.959906,-6.759319],[-5.323536,5.714489,-7.917226,-2.882765,6.347807,-9.712952,7.054371,2.935155,-8.329983,2.618992,-6.741072,-6.423590,2.652167],[5.166845,5.234115,9.815311,-3.517581,3.337442,-7.666724,7.847210,-8.120859,-0.200225,-8.878269,-4.063500,3.715088,9.863386],[3.127056,5.932978,7.196325,-9.435270,2.339625,-0.003972,-4.831550,-2.881318,9.413714,6.358315,6.511732,2.794463,3.352318],[-6.681792,9.514159,-4.702940,8.893157,-8.239069,-2.138357,-2.311416,-2.660668,1.669335,-6.524436,1.382068,-9.776176,6.931543]],[[-5.311018,0.380341,-8.245686,-0.046824,5.736574,8.458872,8.965762,5.425267,-6.573904,5.061728,-6.537434,9.830816,-6.520432],[-2.945791,1.540785,5.385673,-4.949679,-6.205463,-0.938633,6.177979,4.097855,7.884576,-7.978485,1.694468,-4.969576,0.609460],[2.518844,0.203991,8.464077,-9.657657,6.012019,4.291987,-1.881725,-5.937040,-6.473613,-3.307710,-0.319905,-8.047286,-4.038725],[3.809915,-6.911963,6.471649,-9.680759,-6.991546,-5.984243,-7.348526,-2.126080,-6.916289,7.757059,1.178840,-4.821548,-7.206583],[9.698885,3.066630,-0.315926,-0.963011,6.015388,-2.657409,-5.307417,3.744516,-8.069119,-2.543135,3.750054,2.649195,-2.931525],[4.156923,7.743530,3.449680,-2.153134,-5.425672,-0.697252,-6.712516,2.920363,6.506941,8.388677,-2.052547,-3.081330,-1.590095]],[[0.898151,1.944249,-7.154638,-2.801460,-1.600945,1.923209,-3.861853,9.185763,-7.899742,-2.100823,-3.510418,-8.213999,4.563808],[9.348285,2.619990,2.654201,-1.765436,-1.458520,0.980968,-3.272786,3.393922,8.574284,0.830793,-2.779520,-2.148976,0.099111],[-7.815877,-8.945777,9.120541,0.569413,9.763280,8.069861,5.355505,-7.847297,2.783951,-7.220244,-9.915662,-4.836720,-8.850205],[-4.429233,-1.795158,-2.034672,6.904092,-5.323255,-4.965340,5.990710,-0.441693,8.607927,6.917332,6.039686,-0.301694,7.026862],[0.796328,7.454500,-9.882350,-0.842426,2.473328,7.232411,7.149912,8.962945,8.646035,7.381382,-1.362104,-7.280360,-4.054500],[-8.736272,7.215067,-3.201929,6.618263,9.922387,4.488832,-2.346788,-0.839607,3.495905,0.033829,0.395264,8.856667,4.262592]],[[-5.150608,1.888997,3.075639,6.973296,7.727024,8.366291,5.823004,-3.055228,-9.460850,-5.025120,-8.416959,-1.601605,-4.750765],[8.599487,-5.813535,3.511388,-4.436224,6.069339,-4.627723,-4.707847,-9.669565,9.218877,-5.197437,-1.581135,-2.823552,0.676361],[-2.929571,4.117302,-2.588560,3.834727,4.310905,5.845765,3.893532,7.537515,2.937297,-4.989136,2.492707,-9.189527,9.383751],[-9.674700,9.035566,6.191340,8.253115,-4.644721,6.101279,-2.562868,0.952992,-5.871974,-5.817018,-0.101403,9.058952,-9.104834],[-8.432620,9.976360,7.041301,-5.575272,1.412324,7.922508,-0.393825,-7.593036,2.087046,-4.268066,-3.942830,1.987705,-8.337072],[2.482151,-5.352441,-3.536787,-2.190555,9.256399,8.812760,-6.944122,2.800764,1.238170,4.817487,9.145754,-0.075429,5.944219]],[[-2.597959,4.425801,3.156088,-6.482175,-0.175285,-1.084625,-3.756653,1.638133,2.641985,0.191319,0.038220,-9.231197,-6.342234],[7.910732,1.298726,-9.425589,2.929754,-4.294736,-9.224525,0.252004,1.552914,3.350477,4.745536,7.202699,-5.237991,1.921551],[0.381827,-0.499232,4.258052,-7.204414,3.188836,-7.931130,5.295556,1.772348,1.352775,-5.692773,-4.805437,4.589270,-2.125648],[6.640765,3.376002,-0.629437,-8.011962,-0.647328,-1.881575,7.972891,1.715020,6.343517,-3.242539,-8.525935,0.295995,1.051091],[-8.700762,0.466297,2.609064,7.967229,6.513501,-0.499753,1.789627,3.794825,7.866406,8.099438,-5.158025,5.457298,6.849889],[-0.319925,6.920249,-0.004394,-3.432891,-2.942311,-2.666792,-8.022772,-6.334665,-3.382744,-1.635528,7.264517,-2.287458,-1.466957]],[[9.208752,0.568855,-2.626524,8.646343,6.097889,6.206578,9.305130,-5.440531,-9.436994,0.048106,4.197011,-1.940277,5.428333],[2.868959,-8.509523,-1.313786,-8.248501,-5.219935,-3.399435,-5.371167,2.275905,5.029605,4.982108,0.788822,5.277087,-0.129971],[-5.254972,-3.466834,6.180870,0.595249,9.824363,2.538484,0.002646,-5.627118,-8.925606,-7.693536,5.146365,-2.726773,2.286324],[-5.532692,8.875112,5.867754,6.027048,6.763676,7.617532,-1.847359,7.733735,-3.348903,1.857300,-3.237231,2.110372,1.719406],[-2.465999,-1.648894,9.855701,-9.984263,6.505583,-4.388747,3.728603,4.472595,-3.933268,-8.598651,-9.096373,3.423144,8.775771],[1.128534,-2.541823,7.909567,-2.277122,-2.080212,-0.105349,-0.004604,-3.649650,-7.760367,5.766380,-5.027394,4.603641,6.540496]],[[-3.299556,2.377652,-1.464279,-8.807806,-0.182329,9.081906,2.844570,-1.491676,4.770601,-3.333960,-6.649281,5.829757,-7.807097],[7.262226,-0.577089,2.068324,7.918822,9.521772,1.633126,-6.041301,0.347216,3.593292,1.609633,6.047690,-5.506818,-0.466549],[-9.840408,-5.683244,-8.552114,1.647788,-4.965532,1.815058,1.067560,7.432020,-0.176990,-0.755106,-1.034394,9.997500,-1.159678],[-7.856612,-4.815136,9.073542,-7.860776,4.857545,3.294020,-5.172245,-4.722015,-8.191397,-8.600073,-8.374623,1.330837,-8.761493],[-1.609784,-5.528192,-3.671763,-2.493950,7.208797,-1.154250,9.010553,-3.505364,-1.121177,0.045949,-6.212594,-7.365149,1.445330],[-9.221454,-0.256982,-1.969264,-5.627495,7.793624,6.491981,9.123392,0.659929,5.160586,4.855519,2.725903,-4.185874,-5.431833]],[[-0.098796,0.403121,-4.591026,1.947312,-7.921920,8.393694,-0.229506,-7.186401,-0.665118,-7.450797,4.400917,7.368954,-0.978615],[-6.388230,8.186355,3.071488,1.958112,3.031324,-7.949919,-7.008494,4.499212,1.545025,-3.481633,4.214217,8.690325,-9.067432],[1.535429,-4.468517,8.158403,-9.287594,9.628010,-0.440373,-1.776554,-7.180657,-2.411173,-0.261908,7.684496,9.431227,4.646241],[-8.456284,9.058653,9.192188,-6.592956,-0.308312,-8.937497,-6.092697,-2.982901,-5.042367,1.719958,-5.391564,-2.465994,9.946990],[-8.921738,2.988629,9.793757,4.898541,2.248997,-3.577670,-8.040471,2.848698,9.093644,-4.035625,-9.290487,7.687608,-7.225455],[-7.017026,-8.944313,-2.784036,-2.488763,-7.269452,5.472388,-2.017679,-5.485234,0.341645,3.184734,7.928893,-5.678234,0.897940]],[[-3.288060,-1.798184,-9.149701,5.334252,-4.522453,4.755855,-1.382297,2.514758,0.861616,-2.481758,-2.590589,-5.468522,-3.504943],[-1.785656,-0.274409,3.508655,-6.550070,3.007512,-1.902373,4.398172,-7.981233,-9.520142,-0.298514,-6.604940,1.551531,4.774676],[-9.208332,-1.953421,8.753149,-2.944801,-2.597404,6.547661,4.534959,5.173483,8.003915,1.535635,0.322055,-1.375608,5.114084],[-9.887328,1.491488,-5.195922,6.143609,-3.829525,9.586668,-4.653617,8.421924,9.282618,-6.884888,-9.450140,7.839208,3.086322],[1.302895,3.003712,1.060622,-4.649533,4.815517,-8.165755,7.595698,-1.810089,2.193231,-3.704029,-5.596677,-4.565425,-0.701106],[-1.130914,-3.955548,-3.079174,-8.271701,-7.042555,6.581612,-3.089615,2.067666,-7.544938,-8.374231,9.861787,5.168390,-1.049896]],[[0.266631,2.288335,2.414192,-7.508379,2.329354,-6.254714,-3.464198,0.162522,0.004264,-7.161641,8.016234,9.560952,4.120007],[7.723279,-9.948467,-0.750293,-8.412350,8.652188,-7.493376,2.796722,-1.497665,1.759948,-3.233057,1.395746,-5.441148,-9.349533],[-4.628497,1.593422,1.124568,-3.316618,-2.151663,3.487869,-4.616659,6.159094,-0.646835,6.080583,-1.095554,6.058701,5.538266],[-3.100555,8.557892,3.978047,-7.825640,1.824836,-5.994394,7.095363,0.621000,9.797407,6.199395,-2.375857,-9.131290,-4.943983],[-9.619114,5.847828,-5.413379,5.810807,7.738571,1.705902,-2.261962,2.258121,8.464658,3.454927,0.203048,-2.053857,1.038508],[1.996732,-4.125348,-7.499021,1.384524,4.290832,9.185106,2.935721,0.997610,-2.518806,-4.671795,-1.876637,-5.141787,-7.591371]]], dtype = "float32")#candidate|6095|(12, 6, 13)|const|float32
bop_6096 = relay.divide(var_6094.astype('float32'), relay.reshape(const_6095.astype('float32'), relay.shape_of(var_6094))) # shape=(12, 6, 13)
uop_6100 = relay.cos(var_6094.astype('float32')) # shape=(12, 6, 13)
func_5639_call = mod.get_global_var('func_5639')
func_5641_call = mutated_mod.get_global_var('func_5641')
const_6105 = relay.const([2.392553,1.458251,7.502557,-7.870330,0.310958,1.868166,-6.955249,-5.370552,-5.742643,1.966518,5.583819,-9.445123,-6.493119,3.615595,5.020391,5.913080,-1.626574,-9.885065,-6.202157,-5.294253], dtype = "float32")#candidate|6105|(20,)|const|float32
call_6104 = func_5639_call(relay.reshape(const_6105.astype('float32'), [1, 2, 10]))
call_6106 = func_5639_call(relay.reshape(const_6105.astype('float32'), [1, 2, 10]))
output = relay.Tuple([bop_6096,uop_6100,call_6104,const_6105,])
output2 = relay.Tuple([bop_6096,uop_6100,call_6106,const_6105,])
func_6118 = relay.Function([var_6094,], output)
mod['func_6118'] = func_6118
mod = relay.transform.InferType()(mod)
mutated_mod['func_6118'] = func_6118
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6119 = relay.var("var_6119", dtype = "float32", shape = (12, 6, 13))#candidate|6119|(12, 6, 13)|var|float32
func_6118_call = mutated_mod.get_global_var('func_6118')
call_6120 = func_6118_call(var_6119)
output = call_6120
func_6121 = relay.Function([var_6119], output)
mutated_mod['func_6121'] = func_6121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3771_call = mod.get_global_var('func_3771')
func_3773_call = mutated_mod.get_global_var('func_3773')
call_6125 = relay.TupleGetItem(func_3771_call(), 0)
call_6126 = relay.TupleGetItem(func_3773_call(), 0)
var_6135 = relay.var("var_6135", dtype = "float64", shape = (10, 9, 12))#candidate|6135|(10, 9, 12)|var|float64
bop_6136 = relay.logical_or(call_6125.astype('bool'), var_6135.astype('bool')) # shape=(10, 9, 12)
bop_6139 = relay.logical_or(call_6126.astype('bool'), var_6135.astype('bool')) # shape=(10, 9, 12)
output = bop_6136
output2 = bop_6139
func_6143 = relay.Function([var_6135,], output)
mod['func_6143'] = func_6143
mod = relay.transform.InferType()(mod)
var_6144 = relay.var("var_6144", dtype = "float64", shape = (10, 9, 12))#candidate|6144|(10, 9, 12)|var|float64
output = func_6143(var_6144)
func_6145 = relay.Function([var_6144], output)
mutated_mod['func_6145'] = func_6145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4552_call = mod.get_global_var('func_4552')
func_4554_call = mutated_mod.get_global_var('func_4554')
call_6286 = relay.TupleGetItem(func_4552_call(), 0)
call_6287 = relay.TupleGetItem(func_4554_call(), 0)
output = relay.Tuple([call_6286,])
output2 = relay.Tuple([call_6287,])
func_6289 = relay.Function([], output)
mod['func_6289'] = func_6289
mod = relay.transform.InferType()(mod)
mutated_mod['func_6289'] = func_6289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6289_call = mutated_mod.get_global_var('func_6289')
call_6290 = func_6289_call()
output = call_6290
func_6291 = relay.Function([], output)
mutated_mod['func_6291'] = func_6291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3525_call = mod.get_global_var('func_3525')
func_3527_call = mutated_mod.get_global_var('func_3527')
call_6335 = func_3525_call()
call_6336 = func_3525_call()
func_1365_call = mod.get_global_var('func_1365')
func_1368_call = mutated_mod.get_global_var('func_1368')
const_6340 = relay.const([-1,-5,6,2,-8,6,-4,-3,6,9,3,-8,-3,-8,-10,-10,8,3,3,-5,-4,10,-3,8,-10,9,-10,6,3,2,7,-4,7,-10,-1,-1,8,-4,-6,-8,9,10,8,5,-9,5,-8,2,6,-8,-9,-3,4,-5,10,-7,-3,-10,-2,-2,-3,7,-6,9,-1,9,9,6,-7,-4,-6,-8,7,-2,5,9,1,-9,7,6,-8,9,-5,1,-7,1,-5,4,8,-10,-10,-3,7,7,-2,3,8,-9,8,-8,-4,-8,-9,10,10,2,-1,2,-9,-3,2,2,9,-4,1,1,1,6,-2,9,6,-2,8,-4,-3,-9,2,-6,3,5,-3,1,6,6,-4,9,-8,-7,-7,3,-6,6,6,-9,5,4,10,4,5,-3,-6,-8,-5,1,4,3,-8,9,2,-2,-2,7,-4,-8,-2,7,-3,-2,-10,2,9,-5,6,-3,-2,5,1,-3,-2,3,2,-2,3,-7,9,6,-7,-6,-6,1,-4,-9,-8,-2,-3,-6,3,2,-2,-10,8,-8,10,8,-1,-4,-5,1,-5,-6,6,-7,-10,8,8,2,7,-3,-3,10,9,-10,7,8,2,4,3,-8,10,4,5,8,-5,-6,-1,2,-2,-4,4,3,-3,-6,8,-9,2,-8,9,-7,-8,-3,-3,1,-9,-4,-7,1,-6,8,2,6,-3,9,2,-8,-2,9,8,-9,-7,2,-4,5,9,-7,3,5,8,7,3,-10,6,10,-1,1,-4,1,-5,9,8,-6,-7,-6,-6,-7,-10,-6,6,10,-5,-5,-1,6,-3,-9,10,3,-8,-6,-3,5,-10,10,7,5,-9,10,9,8,-2,4,-4,-3,5,9,2,1,-7,10,-9,7,-7,9,-4,9,-6,9,-9,4,-4,2,-9,8,2,-1,4,8,-4,9,-8,3,1,-5,8,2,4,-8,7,-8,-5,-9,-6,10,7,-7,8,-8,4,7,5,-2,5,10,7,10,-9,-8,-7,-5,8,9,2,2,3,7,-9,4,10,-6,4,-6,-5,7,3,-6,4,4,5,1,5,3,-7,-8,3,-4,9,9,4,-6,8,7,-9,7,9,1,5,8,3,9,-9,2,-2,-2,6,3,-1,-7,1,6,1,-4,5,10,-7,3,-3,3,-7,2,-2,9,-3,-4,10,4,9,-10,9,2,1,3,-2,9,-3,3,6,-9,-8,-5,4,2,9,-8,3,4,7,8,-4,-7,8,2,-1,4,5,8,9,5,-1,6,-4,8,8,9,2,8,-5,3,3,-5,-7,10,-2,-3,9,-9,-10,4,-2,9,-10,-4,-7,-3,4,-9], dtype = "uint16")#candidate|6340|(504,)|const|uint16
const_6341 = relay.const([[2,-1,3,-4,2,-2,2,-8,9,-9,4,6,2,-5,-5,-9,8,-3,-3,-9,-10,5,-1,9,1,-4,-5,8,-6,-10,-5,-7,-3,7,1,3,1,3,3,1,-10,-6,5,-2,6,-3,-5,7,3,5,1,3,-6,-3,8,4,9,3,-5,-7,9,5,2,-3,5,9,4,6,-10,-10,3,6,-3,5,6,-10,-4,10,-6,-1,10,6,3,5,-3,4,8,-7,1,-10]], dtype = "uint8")#candidate|6341|(1, 90)|const|uint8
call_6339 = relay.TupleGetItem(func_1365_call(relay.reshape(const_6340.astype('uint16'), [7, 12, 6]), relay.reshape(const_6341.astype('uint8'), [90,]), ), 2)
call_6342 = relay.TupleGetItem(func_1368_call(relay.reshape(const_6340.astype('uint16'), [7, 12, 6]), relay.reshape(const_6341.astype('uint8'), [90,]), ), 2)
output = relay.Tuple([call_6335,call_6339,const_6340,const_6341,])
output2 = relay.Tuple([call_6336,call_6342,const_6340,const_6341,])
func_6343 = relay.Function([], output)
mod['func_6343'] = func_6343
mod = relay.transform.InferType()(mod)
mutated_mod['func_6343'] = func_6343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6343_call = mutated_mod.get_global_var('func_6343')
call_6344 = func_6343_call()
output = call_6344
func_6345 = relay.Function([], output)
mutated_mod['func_6345'] = func_6345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6343_call = mod.get_global_var('func_6343')
func_6345_call = mutated_mod.get_global_var('func_6345')
call_6370 = relay.TupleGetItem(func_6343_call(), 1)
call_6371 = relay.TupleGetItem(func_6345_call(), 1)
const_6372 = relay.const([[[-5.795717,-3.142949,2.397106,9.432398,-1.179032,4.874891],[5.454061,-1.930570,-2.881841,-1.869618,-7.564413,-5.385993],[-5.321861,3.014843,5.774067,7.485475,0.331330,-1.083910],[2.687157,3.754031,-5.817460,-4.083216,1.485263,6.957231],[-2.915425,6.236921,-2.873798,-5.502300,3.151099,6.284998],[-6.213243,-7.816935,-5.088702,-6.016183,-9.733790,-3.551712],[-4.781312,-8.226833,9.791887,5.778963,-2.475529,-5.272684],[5.837449,9.425791,6.959504,3.608872,-4.787289,7.448435],[-3.651929,-1.831328,8.374073,1.140232,4.419048,-3.832993],[8.228469,-2.674477,-6.903784,-8.181874,5.553171,-0.534075],[-5.284929,2.024693,2.369771,-4.126508,-7.949376,-8.379528],[6.662577,-6.525556,-9.272788,1.506189,-2.197050,0.901323]],[[0.988379,-8.804893,7.851478,9.823147,7.434875,-9.627803],[1.925793,-1.998846,1.068902,4.409405,8.878851,-9.376630],[-1.943421,5.964006,4.061839,-2.606363,0.064958,-4.386597],[9.150867,-7.522676,-5.556697,-2.527261,9.239999,2.924570],[8.746286,0.731877,-8.103167,-4.586272,-9.045065,-9.114524],[-5.846155,-4.486063,8.998655,1.792521,-1.028484,5.822481],[-9.751650,-1.798348,3.921756,3.583290,-2.183412,8.985689],[-9.392830,-5.320349,3.797474,-8.074846,3.187947,1.103677],[5.184010,3.533673,3.207229,-7.623792,-9.937190,0.799880],[3.718123,9.817440,-7.110744,-4.761698,-6.035353,0.971784],[5.715707,-7.927655,-8.775230,-5.637417,-0.215865,5.852857],[-8.564599,0.344549,-2.080547,-8.075058,3.420328,1.620644]],[[-8.749781,-9.737510,-3.118399,0.212026,-0.534447,-6.287516],[8.796018,-7.611495,4.386412,1.983322,-8.229486,-0.010941],[-2.991061,-2.909635,-4.568985,7.037284,8.945395,-6.775959],[3.432622,-9.437082,2.206177,-2.178125,2.941443,-1.370139],[-0.632385,-2.075222,-6.092146,2.866180,-7.262541,8.592291],[3.299386,0.911200,-5.745132,2.929345,6.720418,0.556390],[-7.718106,-1.106428,5.904076,-9.281420,-6.282394,-5.859045],[-3.882992,5.258342,7.951432,4.304776,5.144485,0.390753],[-7.118091,8.541946,-0.707534,-3.434657,-3.160233,-9.595759],[5.868147,1.264832,-8.422192,0.445128,7.584743,5.288692],[3.517129,-7.891674,5.519179,-4.491806,-8.521739,-7.138668],[4.755874,2.497761,3.743203,9.776996,8.647355,-8.379008]],[[-0.546661,-9.979158,0.295591,-1.310859,-0.253323,6.653439],[-4.142805,-1.233102,-8.076771,-2.938114,4.086563,1.200034],[9.265195,-1.574162,-2.754755,-8.050160,-8.549278,-1.543473],[-2.122376,-4.549773,2.787264,7.434714,5.684899,-7.972148],[-3.335977,3.896216,5.556899,-0.912254,8.212636,0.846468],[7.871624,-6.170142,-6.290773,8.973469,5.292570,4.428070],[-8.913661,4.074821,-2.951416,2.787514,-6.717011,2.521828],[8.726676,-0.309037,-8.858070,-5.720097,-9.065203,6.960309],[-2.426045,3.629969,-8.142303,-3.720743,1.621386,-3.327845],[-1.247635,-3.170069,1.140418,-9.625636,9.892998,9.952102],[-1.760464,-8.556653,2.358582,8.306919,-1.458934,6.094404],[9.032257,8.107008,1.373223,9.355609,9.862977,-3.274092]],[[4.038665,-1.099090,-3.985863,-0.149926,0.627456,0.367409],[-6.830949,-6.850422,6.467171,9.031119,-3.791413,-4.316543],[-0.029200,6.086621,3.716316,-0.165246,-7.936172,-0.553073],[0.320836,3.256267,1.322270,5.447408,6.724082,-7.567824],[3.268333,0.568734,5.209016,-1.268181,0.261389,0.234432],[7.407963,3.466138,-5.519289,-4.603612,-8.787747,7.911957],[-7.495012,7.638054,-1.565443,5.611588,0.444183,1.060449],[-9.993873,0.117739,4.034351,-1.829125,-1.470542,-6.828827],[8.976283,-1.231584,-9.110348,8.984402,-1.916213,-9.793394],[9.502454,1.454492,9.621485,6.596860,-1.298754,7.295394],[3.945553,-4.040762,-7.826289,5.803696,-5.294463,7.698947],[1.954856,8.730808,-3.036451,-2.853478,7.810064,-1.030239]],[[2.404033,-0.233376,-1.416872,8.949789,-9.425111,-6.106290],[3.489256,-4.404963,0.860158,-9.498108,7.460101,6.822445],[-2.809983,9.177219,4.454110,-2.411826,9.973464,-7.886780],[-3.401898,3.647970,1.940317,2.125726,6.847662,-1.917716],[-2.013861,2.061010,4.169200,1.238707,8.575042,9.306820],[-8.964954,8.982737,0.288691,-2.838371,4.943793,-4.095867],[2.536468,2.817269,4.512161,6.311822,3.739708,1.427665],[0.011157,-8.639949,0.017083,3.533951,8.910830,9.614469],[-2.857715,-6.724617,-4.103731,4.592307,4.843053,-1.530014],[-4.915742,-0.804428,2.806148,-4.795781,-2.054215,9.939044],[6.197718,0.969435,5.839792,1.715632,-2.782670,7.467364],[-8.430368,-5.032953,-3.624563,-3.815790,2.661567,-2.578038]],[[5.641990,4.893076,7.817581,4.966116,-0.225432,3.265348],[-7.568319,1.503328,-1.599362,7.372502,9.650983,-2.455596],[-1.804012,2.657570,5.909623,-9.080845,-1.185108,-3.977440],[-7.014766,-9.135398,0.569546,-2.103408,-6.409819,-5.105896],[6.720818,0.614938,-9.793316,-1.899465,6.212422,-0.995472],[7.752746,5.430284,-2.159786,5.123602,5.803033,2.420955],[5.552527,-7.389412,-6.351501,-8.387771,-8.603098,-6.893938],[-0.049855,-9.101010,-9.291083,-5.587563,2.862749,-5.587130],[-3.978292,6.937937,2.003983,-4.834676,-8.921964,8.982140],[2.021086,-6.932984,7.298099,-7.408790,8.491161,7.091015],[9.819324,4.601867,9.604187,3.399871,4.528005,-4.525279],[4.233299,2.039643,3.264231,-7.552296,7.023825,5.203458]]], dtype = "float32")#candidate|6372|(7, 12, 6)|const|float32
bop_6373 = relay.minimum(call_6370.astype('uint16'), relay.reshape(const_6372.astype('uint16'), relay.shape_of(call_6370))) # shape=(7, 12, 6)
bop_6376 = relay.minimum(call_6371.astype('uint16'), relay.reshape(const_6372.astype('uint16'), relay.shape_of(call_6371))) # shape=(7, 12, 6)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_6380 = relay.TupleGetItem(func_3508_call(), 0)
call_6381 = relay.TupleGetItem(func_3510_call(), 0)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
var_6388 = relay.var("var_6388", dtype = "float32", shape = (432,))#candidate|6388|(432,)|var|float32
call_6387 = relay.TupleGetItem(func_3463_call(relay.reshape(var_6388.astype('float32'), [4, 108])), 4)
call_6389 = relay.TupleGetItem(func_3465_call(relay.reshape(var_6388.astype('float32'), [4, 108])), 4)
output = relay.Tuple([bop_6373,call_6380,call_6387,var_6388,])
output2 = relay.Tuple([bop_6376,call_6381,call_6389,var_6388,])
func_6390 = relay.Function([var_6388,], output)
mod['func_6390'] = func_6390
mod = relay.transform.InferType()(mod)
mutated_mod['func_6390'] = func_6390
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6391 = relay.var("var_6391", dtype = "float32", shape = (432,))#candidate|6391|(432,)|var|float32
func_6390_call = mutated_mod.get_global_var('func_6390')
call_6392 = func_6390_call(var_6391)
output = call_6392
func_6393 = relay.Function([var_6391], output)
mutated_mod['func_6393'] = func_6393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5366_call = mod.get_global_var('func_5366')
func_5367_call = mutated_mod.get_global_var('func_5367')
call_6443 = func_5366_call()
call_6444 = func_5366_call()
uop_6447 = relay.atan(call_6443.astype('float32')) # shape=(3, 12, 3)
uop_6449 = relay.atan(call_6444.astype('float32')) # shape=(3, 12, 3)
output = uop_6447
output2 = uop_6449
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
