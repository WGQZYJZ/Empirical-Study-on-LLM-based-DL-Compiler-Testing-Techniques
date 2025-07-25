import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_561 = relay.var("var_561", dtype = "uint16", shape = (4, 11, 8))#candidate|561|(4, 11, 8)|var|uint16
var_562 = relay.var("var_562", dtype = "uint16", shape = (4, 11, 8))#candidate|562|(4, 11, 8)|var|uint16
bop_563 = relay.add(var_561.astype('uint16'), relay.reshape(var_562.astype('uint16'), relay.shape_of(var_561))) # shape=(4, 11, 8)
output = bop_563
output2 = bop_563
func_566 = relay.Function([var_561,var_562,], output)
mod['func_566'] = func_566
mod = relay.transform.InferType()(mod)
mutated_mod['func_566'] = func_566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_566_call = mutated_mod.get_global_var('func_566')
var_568 = relay.var("var_568", dtype = "uint16", shape = (4, 11, 8))#candidate|568|(4, 11, 8)|var|uint16
var_569 = relay.var("var_569", dtype = "uint16", shape = (4, 11, 8))#candidate|569|(4, 11, 8)|var|uint16
call_567 = func_566_call(var_568,var_569,)
output = call_567
func_570 = relay.Function([var_568,var_569,], output)
mutated_mod['func_570'] = func_570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_992 = relay.var("var_992", dtype = "float64", shape = (16, 6, 12))#candidate|992|(16, 6, 12)|var|float64
uop_993 = relay.acos(var_992.astype('float64')) # shape=(16, 6, 12)
func_566_call = mod.get_global_var('func_566')
func_570_call = mutated_mod.get_global_var('func_570')
const_997 = relay.const([-7,6,5,4,1,-10,-10,1,9,-4,-3,-2,9,-6,1,9,-2,-3,9,6,3,-6,-8,2,4,10,2,4,-5,8,2,3,-4,-2,4,-2,3,-10,5,-10,8,6,-9,3,3,-9,-1,-10,7,-6,1,7,-6,-6,-1,-1,4,10,10,-9,-5,7,-9,8,8,-8,-4,4,2,-4,-4,-3,-2,6,-4,-2,-1,4,-5,-7,-8,3,-10,5,-5,-6,-2,1,-1,6,10,-6,-7,5,3,-5,7,-5,5,10,9,-10,6,-4,8,6,-8,-3,3,8,-9,8,-1,4,5,5,-1,-4,6,-6,10,4,-4,-4,4,2,-5,9,3,1,7,-1,-10,-7,-3,-3,-7,-2,4,8,7,1,-8,9,4,-9,-3,1,-5,10,-3,2,9,-1,-1,-3,8,-2,4,8,-1,-1,9,-8,2,4,-10,-5,2,2,-6,-4,8,-1,-7,-4,-7,-3,-9,-5,-8,4,7,6,7,5,-4,-8,-4,9,-9,10,-8,-6,-3,-5,10,-8,3,6,-6,5,-9,4,-3,5,-6,10,7,8,-5,-10,6,-1,5,-9,10,1,-9,3,8,2,2,-7,-7,8,9,6,7,6,-5,-1,9,4,-6,7,-6,9,4,8,10,3,3,9,-5,10,-8,-2,-2,6,-5,6,-4,9,1,-9,-3,-2,-10,-6,6,4,6,2,4,8,10,1,8,-4,-7,-10,5,-7,-5,-9,-9,-6,3,-3,-5,-6,-6,1,-9,5,-7,-6,-8,-7,-8,-3,-3,9,6,-3,-6,8,-8,-10,-5,2,-9,-6,3,-2,-4,-7,-6,3,10,-5,-6,10,1,2,-4,-9,5,2,3,-1,10,3,4,-8,-3,1,-5,7,3,-3,4,-10,1,8,-5,-8,5,-9,-9,-3,1,6,-5,3,4,4,1,-8,-3,4], dtype = "uint16")#candidate|997|(352,)|const|uint16
call_996 = func_566_call(relay.reshape(const_997.astype('uint16'), [4, 11, 8]), relay.reshape(const_997.astype('uint16'), [4, 11, 8]), )
call_998 = func_566_call(relay.reshape(const_997.astype('uint16'), [4, 11, 8]), relay.reshape(const_997.astype('uint16'), [4, 11, 8]), )
output = relay.Tuple([uop_993,call_996,const_997,])
output2 = relay.Tuple([uop_993,call_998,const_997,])
func_1000 = relay.Function([var_992,], output)
mod['func_1000'] = func_1000
mod = relay.transform.InferType()(mod)
var_1001 = relay.var("var_1001", dtype = "float64", shape = (16, 6, 12))#candidate|1001|(16, 6, 12)|var|float64
output = func_1000(var_1001)
func_1002 = relay.Function([var_1001], output)
mutated_mod['func_1002'] = func_1002
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1241 = relay.var("var_1241", dtype = "float32", shape = (8, 1, 16))#candidate|1241|(8, 1, 16)|var|float32
const_1242 = relay.const([[[2.787441,-0.004504,-3.451650,-8.924232,-0.672228,-2.533906,-9.108225,-9.407455,-4.134767,3.594547,6.521854,-3.950966,2.119992,2.017323,5.596578,6.529154],[5.498340,-8.842792,5.556656,-7.760777,-6.290393,-7.981626,-4.804693,7.392437,-2.961099,-8.104653,9.435259,2.997867,-8.150551,-7.356649,8.909129,-8.896027],[-3.699514,-0.537418,5.189412,9.716934,-1.077506,-1.818700,-2.493545,5.294704,-8.545719,-3.986608,-6.650409,4.818133,3.949818,-4.715549,3.234805,1.447188],[6.083256,8.037077,-8.713119,-2.599052,-6.415903,-8.541822,2.249713,6.974321,5.101344,3.520135,6.455550,-8.099340,7.974437,-2.801099,0.560361,-5.555898],[3.154904,2.539645,-3.323884,-1.547684,3.923320,-8.114308,3.975135,-0.812041,6.755227,-3.455722,-6.432264,1.278834,-5.508475,-0.892524,-5.815973,-7.904261],[-3.658912,2.230642,-4.358125,-2.629936,-0.806617,-0.853478,-2.152454,-8.541828,-6.634214,9.810918,9.441274,-6.960713,-7.825826,4.752977,5.057971,-9.704686]],[[-0.305594,7.943508,-7.291995,-3.142920,-1.301936,-8.545220,3.665846,-6.193364,3.111603,9.546154,1.252565,-6.326153,-6.671692,-9.704190,-8.524060,-5.200764],[-3.374514,5.228322,5.135355,-7.117727,-5.903526,-4.934121,2.083526,0.725754,-7.753807,-4.211259,8.173296,0.536751,-2.012677,5.150798,1.944270,4.348969],[1.209002,-2.100326,-0.575883,-5.219732,4.972220,8.688354,-0.079488,0.251026,4.791526,-1.397135,8.127184,-6.765581,5.036440,-4.009390,1.843340,-2.698608],[-2.360047,8.285457,7.376337,8.948160,2.028374,-0.405130,6.771495,-5.459112,2.536393,4.732358,0.718839,-7.309568,-7.674221,7.944812,7.299078,-4.302821],[-2.922344,-4.153034,-0.929860,-0.947895,-3.204947,3.896227,-0.864438,-9.345545,-7.932295,-2.230424,-7.260805,-8.844702,0.890652,-7.971519,9.999497,-2.488247],[4.544787,-0.264039,-4.888533,9.031496,3.617317,2.168580,-8.192060,9.700991,8.070045,-4.171859,-7.637478,-2.151751,-0.808890,-4.338091,-1.106365,1.766018]],[[-2.396740,5.976549,-2.543355,1.562576,9.327383,-8.900355,1.989309,-5.069640,7.699264,-6.288134,5.212318,-9.358578,8.136540,4.594572,2.865549,2.317308],[-8.450635,3.607983,9.689324,-1.686075,1.057772,6.065911,-1.721047,5.129406,-7.807520,-9.048597,7.932557,-6.485760,1.057539,-5.413779,-5.043488,-5.556135],[-5.924615,-6.789504,2.010975,-2.837715,5.769727,0.803844,3.288807,8.573796,-1.850929,0.677434,-7.495561,-4.602401,6.063917,6.309186,6.035257,5.034240],[9.579938,2.610207,-0.587148,1.264343,6.486461,-5.807381,9.488363,9.559351,7.408713,7.045996,-1.972856,3.790043,-6.198719,1.427015,4.081183,6.255531],[-5.727690,5.136565,-7.060415,-7.763662,1.012798,-8.991355,5.352556,-9.687097,-8.427398,-6.297495,3.637845,3.770466,-7.428902,9.203018,8.996768,-6.637487],[-5.605133,-4.982734,-8.470840,-6.470859,9.927837,8.209645,-8.663603,2.154366,9.227412,4.925774,-6.230209,5.482053,-1.495010,-1.745205,4.924120,9.884072]],[[-2.789826,0.828616,9.213976,-9.320538,-1.916590,7.778402,3.629511,-7.112436,-0.307042,7.891225,-0.989553,-9.109867,-5.068932,-7.881728,0.591421,8.571793],[6.634626,2.199867,-2.248518,-7.772534,4.805373,-1.311373,-2.909310,0.164864,-5.942246,5.318085,3.322762,1.521185,-1.391635,-9.805568,-1.738521,1.813414],[-9.721677,-2.271506,-1.803155,8.604208,-1.089506,-9.962924,-2.317654,8.482009,6.252034,8.386210,-5.429309,-1.356100,-6.280768,9.219176,-4.805738,0.502246],[8.912898,2.320949,-8.731345,6.788057,-7.279911,6.455961,0.903313,-2.903456,-5.966066,-8.889633,-2.130410,1.936820,7.533789,8.361821,-0.528099,-1.237228],[-3.429107,8.703723,-1.229470,6.017807,1.420935,-0.011296,-1.679092,2.969388,-4.948721,5.791495,-2.099029,-6.541545,6.681177,0.230314,-9.263703,4.627783],[0.786999,2.416148,4.145211,6.043019,9.790214,-3.395722,-1.888357,-1.138266,9.043603,5.811816,2.445408,9.743226,-4.852288,-0.561917,-0.480224,2.479437]],[[-1.811140,7.765889,-6.034573,-4.051411,-3.377324,1.583031,-6.454784,-2.776662,2.764084,4.248332,8.717890,-0.584228,2.773476,-6.877066,-7.227095,-7.366927],[-5.362031,3.236752,-0.673842,-1.766424,-8.149059,2.299861,-2.899061,-7.753135,3.045991,-2.877966,-5.340590,-9.724367,3.993836,4.995662,4.731747,-5.470713],[1.137215,-1.779161,-4.967773,7.160524,-2.823008,7.745025,-7.190916,-2.445343,-5.150977,-7.470999,6.480071,-8.817409,2.495156,5.940922,0.435328,-9.606453],[0.134737,-6.546095,5.504352,-0.257087,-6.070978,-1.913689,5.014813,2.898698,8.366138,-9.644308,-3.460066,2.610831,-5.775135,-1.859298,5.281295,-6.524902],[8.910788,-8.731735,-0.169945,-4.694306,-6.874537,6.716212,-3.839303,6.046983,-3.822248,-8.817474,5.921304,-8.204843,-7.401280,2.952770,6.771554,-9.760502],[4.309807,-1.802926,2.231898,-0.172967,6.916664,2.078552,-3.574346,-3.555229,-3.742535,-7.740392,-5.337683,3.062724,4.470628,-9.601524,9.072831,-9.740086]],[[0.577859,-5.382320,4.583652,3.295603,8.627258,-1.824960,6.667716,-5.869366,-6.025899,8.129616,-2.711181,1.462007,-7.963834,-6.820561,8.456750,-3.613971],[7.285345,9.541615,0.851298,-6.281975,-1.216976,8.011921,7.107784,2.103668,-9.022256,-6.883037,-2.140471,-4.640653,-0.961754,-8.460268,2.420595,-9.976742],[8.991516,-5.299296,-7.938701,0.998953,9.220374,7.397587,4.258698,-0.749557,5.650313,-2.499330,8.421311,-3.356729,1.493144,2.812989,7.805347,-8.376785],[5.328241,-9.251469,4.177790,-7.236949,-1.247800,8.873067,3.896243,8.946545,-6.168778,-1.610385,-5.972039,4.005708,4.542718,2.432948,1.467804,6.559756],[-4.075654,-8.037757,-5.983548,-8.410070,-6.907423,-6.424079,-8.688077,6.049239,3.067287,-5.102009,-7.147025,2.567803,-5.884966,5.980933,-2.721890,-3.641508],[-4.476073,-1.789439,-4.978335,6.798362,-6.546592,-8.387282,3.190490,-8.324263,1.358499,-8.611237,-4.925030,8.735630,-6.207343,-9.518623,0.055708,0.897880]],[[-6.929734,-4.501438,5.739354,9.753770,4.112649,-8.854942,8.796675,4.234460,1.217633,3.177264,-9.779647,-7.558331,1.343686,6.018547,0.394423,-7.286288],[0.324685,-5.451989,-4.940942,-9.093000,6.439226,-0.135548,3.879735,9.881516,7.179138,3.829651,8.922059,4.434839,-2.208430,-8.447323,9.408102,5.925073],[9.964798,1.136749,-2.641116,-8.279129,-2.929319,-7.801320,-8.286388,-0.747480,-2.497893,1.020006,4.644357,-4.942622,-7.304202,-8.154253,1.827707,-1.401330],[9.708480,-4.369620,3.676987,-4.515085,5.871828,-8.941041,-0.262480,-7.988087,-0.205501,3.352007,-1.424785,0.923125,-2.120835,-6.398099,-8.574792,-8.824931],[9.228965,5.045306,9.449409,-0.488184,-9.484397,0.990375,-5.357549,-9.562247,4.933629,-9.238176,9.828165,-8.857470,5.563084,-5.306876,3.267983,-0.952022],[9.476878,-0.897429,6.855441,-9.869303,3.119203,-1.316242,4.039421,-0.397914,-9.016481,-1.216798,-0.951036,4.796294,6.019421,6.149680,3.525049,6.146082]],[[6.897201,2.916617,0.652923,8.677092,5.769125,-3.127091,-1.523099,-1.527698,4.186278,-5.278648,5.883947,-9.654898,6.372459,-1.363618,1.514449,-2.214686],[0.847508,5.103163,8.516198,0.512284,-8.947520,6.189767,-5.977953,-6.126315,-6.761043,2.338210,-1.151797,-9.477910,-8.090839,-5.986929,6.183714,-0.019245],[7.531393,7.660163,-9.021680,3.319125,-4.350008,5.528534,-1.878597,-7.842691,0.415246,9.995448,1.907204,6.446063,-5.601677,5.558352,-9.973438,-7.203468],[8.324789,-0.812560,-5.431192,1.955440,-8.738024,0.363495,-3.803343,7.893066,0.954340,6.424233,3.613661,-8.203269,5.895380,1.941059,-9.761872,7.703377],[9.974464,7.061166,8.172218,-5.839771,-2.534023,0.687467,5.228367,-1.218285,8.403989,-9.114660,-7.609699,-2.085054,-0.223881,-9.943652,2.525927,5.219083],[9.962765,-7.293776,0.208593,7.906113,-8.371917,-6.501026,6.464712,-4.186284,-0.612728,8.950566,-0.709690,-4.780856,3.904775,0.320592,-6.322965,2.755909]]], dtype = "float32")#candidate|1242|(8, 6, 16)|const|float32
bop_1243 = relay.floor_mod(var_1241.astype('float32'), const_1242.astype('float32')) # shape=(8, 6, 16)
output = bop_1243
output2 = bop_1243
func_1253 = relay.Function([var_1241,], output)
mod['func_1253'] = func_1253
mod = relay.transform.InferType()(mod)
mutated_mod['func_1253'] = func_1253
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1254 = relay.var("var_1254", dtype = "float32", shape = (8, 1, 16))#candidate|1254|(8, 1, 16)|var|float32
func_1253_call = mutated_mod.get_global_var('func_1253')
call_1255 = func_1253_call(var_1254)
output = call_1255
func_1256 = relay.Function([var_1254], output)
mutated_mod['func_1256'] = func_1256
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1731 = relay.var("var_1731", dtype = "float64", shape = (11, 2, 4))#candidate|1731|(11, 2, 4)|var|float64
uop_1732 = relay.sinh(var_1731.astype('float64')) # shape=(11, 2, 4)
uop_1734 = relay.erf(var_1731.astype('float32')) # shape=(11, 2, 4)
output = relay.Tuple([uop_1732,uop_1734,])
output2 = relay.Tuple([uop_1732,uop_1734,])
func_1748 = relay.Function([var_1731,], output)
mod['func_1748'] = func_1748
mod = relay.transform.InferType()(mod)
var_1749 = relay.var("var_1749", dtype = "float64", shape = (11, 2, 4))#candidate|1749|(11, 2, 4)|var|float64
output = func_1748(var_1749)
func_1750 = relay.Function([var_1749], output)
mutated_mod['func_1750'] = func_1750
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2589 = relay.var("var_2589", dtype = "float64", shape = (5, 7, 4))#candidate|2589|(5, 7, 4)|var|float64
uop_2590 = relay.asin(var_2589.astype('float64')) # shape=(5, 7, 4)
func_566_call = mod.get_global_var('func_566')
func_570_call = mutated_mod.get_global_var('func_570')
const_2610 = relay.const([-1,5,2,1,-7,-3,6,4,3,8,-4,9,-3,-1,2,-5,5,-10,-8,-10,-6,9,-2,-7,6,4,2,3,8,-2,-10,-3,7,-1,4,9,6,-1,-9,-1,6,5,1,-5,4,1,-4,-10,-8,5,2,-2,-2,-5,3,-5,3,9,10,5,9,9,-10,4,1,2,3,-2,-10,5,-4,4,-2,3,5,7,6,9,6,8,5,1,-5,-3,9,-8,-10,-2,5,4,5,-6,-7,9,-10,-1,6,-3,4,-5,5,5,8,-6,5,3,-1,-3,7,4,-8,2,-6,4,-10,2,-6,1,-4,-7,8,1,2,-10,7,-4,-10,10,1,7,-6,-9,7,6,-10,2,-4,9,-10,-3,-4,3,-5,-3,8,-10,-10,5,-2,9,-4,9,-4,2,-9,1,3,-9,-9,-5,-4,-9,5,-10,-7,-8,-9,-8,7,-7,6,10,-3,10,-3,9,1,2,4,-4,2,-3,-10,6,-1,-4,2,-8,4,7,4,-7,-3,-4,2,9,1,4,1,1,-2,10,-8,1,8,-3,5,9,8,7,1,-3,6,-8,-7,2,3,-5,2,-4,5,5,7,8,-7,-5,-8,5,-8,-4,9,8,8,4,9,-2,-7,-4,3,2,-6,-2,-7,-10,-7,2,8,9,-3,-8,1,9,-9,2,7,-5,1,7,4,5,-2,9,-6,8,1,4,-5,2,7,9,-10,-7,10,10,-3,-7,-1,5,-5,9,-8,-2,7,9,7,-8,-2,9,10,8,-4,8,-1,5,5,-4,6,-8,-9,6,4,-5,10,-10,3,6,3,3,7,2,1,-7,-3,1,-1,-7,3,-3,6,-7,-1,6,-7,8,6,-9,7,7,10,-1,7,6,-2,2,2,6,-2,-7,-1,6,8,-6,9,4,-1,10,3,-7,5,-2,1,-2], dtype = "uint16")#candidate|2610|(352,)|const|uint16
call_2609 = func_566_call(relay.reshape(const_2610.astype('uint16'), [4, 11, 8]), relay.reshape(const_2610.astype('uint16'), [4, 11, 8]), )
call_2611 = func_566_call(relay.reshape(const_2610.astype('uint16'), [4, 11, 8]), relay.reshape(const_2610.astype('uint16'), [4, 11, 8]), )
output = relay.Tuple([uop_2590,call_2609,const_2610,])
output2 = relay.Tuple([uop_2590,call_2611,const_2610,])
func_2616 = relay.Function([var_2589,], output)
mod['func_2616'] = func_2616
mod = relay.transform.InferType()(mod)
var_2617 = relay.var("var_2617", dtype = "float64", shape = (5, 7, 4))#candidate|2617|(5, 7, 4)|var|float64
output = func_2616(var_2617)
func_2618 = relay.Function([var_2617], output)
mutated_mod['func_2618'] = func_2618
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2674 = relay.const(-8, dtype = "uint16")#candidate|2674|()|const|uint16
const_2675 = relay.const([[[-9,2,-7,10,6,-9,-9]],[[-8,6,4,6,-5,-8,-7]],[[-5,2,-5,3,9,-4,-9]],[[9,-5,8,2,-1,-1,9]],[[-1,2,9,10,-8,-10,6]],[[-3,6,5,-6,-5,7,7]],[[4,9,-10,-1,-3,-7,-6]],[[2,-10,9,7,-9,10,-1]],[[2,5,4,1,-5,5,3]],[[-10,8,3,7,3,-7,-6]]], dtype = "uint16")#candidate|2675|(10, 1, 7)|const|uint16
bop_2676 = relay.less_equal(const_2674.astype('bool'), const_2675.astype('bool')) # shape=(10, 1, 7)
output = relay.Tuple([bop_2676,])
output2 = relay.Tuple([bop_2676,])
func_2698 = relay.Function([], output)
mod['func_2698'] = func_2698
mod = relay.transform.InferType()(mod)
mutated_mod['func_2698'] = func_2698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mutated_mod.get_global_var('func_2698')
call_2699 = func_2698_call()
output = call_2699
func_2700 = relay.Function([], output)
mutated_mod['func_2700'] = func_2700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_2765 = relay.TupleGetItem(func_2698_call(), 0)
call_2766 = relay.TupleGetItem(func_2700_call(), 0)
func_566_call = mod.get_global_var('func_566')
func_570_call = mutated_mod.get_global_var('func_570')
const_2768 = relay.const([[-4],[-9],[-4],[-6],[-1],[-6],[2],[8],[-4],[-6],[2],[-9],[-3],[5],[-8],[4],[-1],[-6],[-5],[-8],[1],[-3],[-9],[-5],[-4],[5],[2],[-6],[-4],[10],[1],[2],[7],[9],[-2],[-10],[10],[-8],[-4],[1],[3],[3],[7],[2],[-4],[3],[-6],[-9],[5],[-5],[-6],[10],[8],[-4],[-10],[-10],[10],[10],[-5],[-1],[5],[-4],[1],[4],[-3],[2],[3],[5],[1],[-6],[6],[-6],[7],[6],[-8],[-1],[-2],[-4],[8],[6],[-6],[-1],[2],[2],[7],[6],[4],[-2],[10],[5],[6],[1],[-10],[-1],[-2],[10],[-7],[8],[-8],[5],[-10],[1],[-5],[-5],[2],[10],[-3],[-7],[5],[-1],[-5],[4],[-5],[1],[3],[-9],[9],[5],[4],[6],[9],[7],[9],[6],[4],[-1],[-10],[10],[7],[9],[9],[3],[9],[-1],[-9],[10],[-5],[9],[-10],[7],[2],[-2],[-1],[10],[-8],[-8],[-10],[-5],[10],[-1],[-3],[6],[-7],[-1],[1],[3],[-4],[-10],[1],[-4],[10],[6],[-2],[8],[-8],[-10],[9],[10],[-4],[4],[-9],[-1],[-4],[-9],[-2],[4],[5],[-1],[-4],[9],[-7],[5],[-9],[-3],[-10],[-10],[-6],[3],[3],[-4],[6],[-6],[-7],[-8],[-5],[5],[9],[9],[6],[3],[-9],[-4],[-6],[-2],[10],[-6],[4],[-7],[-1],[4],[-5],[-8],[-8],[4],[-9],[2],[2],[2],[5],[-8],[1],[-1],[-6],[-8],[5],[-2],[2],[7],[-9],[5],[-8],[5],[-3],[9],[-2],[-2],[1],[-10],[2],[-3],[-1],[-9],[7],[2],[-7],[-3],[6],[-6],[-6],[8],[1],[2],[3],[-8],[-1],[4],[-8],[-6],[7],[10],[-9],[-10],[2],[3],[-10],[-7],[-10],[5],[-3],[10],[6],[10],[5],[10],[6],[-9],[-4],[7],[4],[5],[2],[8],[-2],[-7],[6],[1],[-9],[9],[-6],[9],[10],[6],[-6],[1],[4],[5],[9],[-10],[-6],[8],[-4],[5],[1],[-1],[-2],[1],[-8],[-5],[2],[6],[1],[4],[5],[-1],[-10],[-5],[9],[10],[-6],[6],[-1],[10],[-6],[6],[3],[3],[-3],[4],[-10],[-1],[5],[5],[-7],[-3],[-7],[-1],[-8],[10],[7],[1],[7],[-4],[1],[-10],[-4],[-1],[8],[10],[-2],[8],[-3],[-8]], dtype = "uint16")#candidate|2768|(352, 1)|const|uint16
call_2767 = func_566_call(relay.reshape(const_2768.astype('uint16'), [4, 11, 8]), relay.reshape(const_2768.astype('uint16'), [4, 11, 8]), )
call_2769 = func_566_call(relay.reshape(const_2768.astype('uint16'), [4, 11, 8]), relay.reshape(const_2768.astype('uint16'), [4, 11, 8]), )
output = relay.Tuple([call_2765,call_2767,const_2768,])
output2 = relay.Tuple([call_2766,call_2769,const_2768,])
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
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_2813 = relay.TupleGetItem(func_2698_call(), 0)
call_2814 = relay.TupleGetItem(func_2700_call(), 0)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_2815 = relay.TupleGetItem(func_2698_call(), 0)
call_2816 = relay.TupleGetItem(func_2700_call(), 0)
uop_2819 = relay.exp(call_2813.astype('float32')) # shape=(10, 1, 7)
uop_2821 = relay.exp(call_2814.astype('float32')) # shape=(10, 1, 7)
output = relay.Tuple([call_2815,uop_2819,])
output2 = relay.Tuple([call_2816,uop_2821,])
func_2848 = relay.Function([], output)
mod['func_2848'] = func_2848
mod = relay.transform.InferType()(mod)
output = func_2848()
func_2849 = relay.Function([], output)
mutated_mod['func_2849'] = func_2849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_2878 = relay.TupleGetItem(func_2698_call(), 0)
call_2879 = relay.TupleGetItem(func_2700_call(), 0)
func_1000_call = mod.get_global_var('func_1000')
func_1002_call = mutated_mod.get_global_var('func_1002')
var_2881 = relay.var("var_2881", dtype = "float64", shape = (1152,))#candidate|2881|(1152,)|var|float64
call_2880 = relay.TupleGetItem(func_1000_call(relay.reshape(var_2881.astype('float64'), [16, 6, 12])), 2)
call_2882 = relay.TupleGetItem(func_1002_call(relay.reshape(var_2881.astype('float64'), [16, 6, 12])), 2)
output = relay.Tuple([call_2878,call_2880,var_2881,])
output2 = relay.Tuple([call_2879,call_2882,var_2881,])
func_2892 = relay.Function([var_2881,], output)
mod['func_2892'] = func_2892
mod = relay.transform.InferType()(mod)
mutated_mod['func_2892'] = func_2892
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2893 = relay.var("var_2893", dtype = "float64", shape = (1152,))#candidate|2893|(1152,)|var|float64
func_2892_call = mutated_mod.get_global_var('func_2892')
call_2894 = func_2892_call(var_2893)
output = call_2894
func_2895 = relay.Function([var_2893], output)
mutated_mod['func_2895'] = func_2895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_3009 = relay.TupleGetItem(func_2698_call(), 0)
call_3010 = relay.TupleGetItem(func_2700_call(), 0)
output = call_3009
output2 = call_3010
func_3017 = relay.Function([], output)
mod['func_3017'] = func_3017
mod = relay.transform.InferType()(mod)
output = func_3017()
func_3018 = relay.Function([], output)
mutated_mod['func_3018'] = func_3018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mod.get_global_var('func_2848')
func_2849_call = mutated_mod.get_global_var('func_2849')
call_3066 = relay.TupleGetItem(func_2848_call(), 1)
call_3067 = relay.TupleGetItem(func_2849_call(), 1)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_3116 = relay.TupleGetItem(func_2773_call(), 0)
call_3117 = relay.TupleGetItem(func_2775_call(), 0)
func_2848_call = mod.get_global_var('func_2848')
func_2849_call = mutated_mod.get_global_var('func_2849')
call_3130 = relay.TupleGetItem(func_2848_call(), 0)
call_3131 = relay.TupleGetItem(func_2849_call(), 0)
uop_3153 = relay.rsqrt(call_3066.astype('float32')) # shape=(10, 1, 7)
uop_3155 = relay.rsqrt(call_3067.astype('float32')) # shape=(10, 1, 7)
var_3157 = relay.var("var_3157", dtype = "bool", shape = (10, 7, 7))#candidate|3157|(10, 7, 7)|var|bool
bop_3158 = relay.right_shift(call_3130.astype('int64'), var_3157.astype('int64')) # shape=(10, 7, 7)
bop_3161 = relay.right_shift(call_3131.astype('int64'), var_3157.astype('int64')) # shape=(10, 7, 7)
func_2848_call = mod.get_global_var('func_2848')
func_2849_call = mutated_mod.get_global_var('func_2849')
call_3162 = relay.TupleGetItem(func_2848_call(), 0)
call_3163 = relay.TupleGetItem(func_2849_call(), 0)
output = relay.Tuple([call_3116,uop_3153,bop_3158,call_3162,])
output2 = relay.Tuple([call_3117,uop_3155,bop_3161,call_3163,])
func_3171 = relay.Function([var_3157,], output)
mod['func_3171'] = func_3171
mod = relay.transform.InferType()(mod)
mutated_mod['func_3171'] = func_3171
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3172 = relay.var("var_3172", dtype = "bool", shape = (10, 7, 7))#candidate|3172|(10, 7, 7)|var|bool
func_3171_call = mutated_mod.get_global_var('func_3171')
call_3173 = func_3171_call(var_3172)
output = call_3173
func_3174 = relay.Function([var_3172], output)
mutated_mod['func_3174'] = func_3174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_3203 = relay.TupleGetItem(func_2698_call(), 0)
call_3204 = relay.TupleGetItem(func_2700_call(), 0)
output = call_3203
output2 = call_3204
func_3228 = relay.Function([], output)
mod['func_3228'] = func_3228
mod = relay.transform.InferType()(mod)
mutated_mod['func_3228'] = func_3228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3228_call = mutated_mod.get_global_var('func_3228')
call_3229 = func_3228_call()
output = call_3229
func_3230 = relay.Function([], output)
mutated_mod['func_3230'] = func_3230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_3267 = relay.TupleGetItem(func_2773_call(), 1)
call_3268 = relay.TupleGetItem(func_2775_call(), 1)
func_2616_call = mod.get_global_var('func_2616')
func_2618_call = mutated_mod.get_global_var('func_2618')
var_3281 = relay.var("var_3281", dtype = "float64", shape = (140,))#candidate|3281|(140,)|var|float64
call_3280 = relay.TupleGetItem(func_2616_call(relay.reshape(var_3281.astype('float64'), [5, 7, 4])), 2)
call_3282 = relay.TupleGetItem(func_2618_call(relay.reshape(var_3281.astype('float64'), [5, 7, 4])), 2)
output = relay.Tuple([call_3267,call_3280,var_3281,])
output2 = relay.Tuple([call_3268,call_3282,var_3281,])
func_3285 = relay.Function([var_3281,], output)
mod['func_3285'] = func_3285
mod = relay.transform.InferType()(mod)
mutated_mod['func_3285'] = func_3285
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3286 = relay.var("var_3286", dtype = "float64", shape = (140,))#candidate|3286|(140,)|var|float64
func_3285_call = mutated_mod.get_global_var('func_3285')
call_3287 = func_3285_call(var_3286)
output = call_3287
func_3288 = relay.Function([var_3286], output)
mutated_mod['func_3288'] = func_3288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_3296 = relay.TupleGetItem(func_2773_call(), 0)
call_3297 = relay.TupleGetItem(func_2775_call(), 0)
func_3171_call = mod.get_global_var('func_3171')
func_3174_call = mutated_mod.get_global_var('func_3174')
var_3301 = relay.var("var_3301", dtype = "bool", shape = (490,))#candidate|3301|(490,)|var|bool
call_3300 = relay.TupleGetItem(func_3171_call(relay.reshape(var_3301.astype('bool'), [10, 7, 7])), 0)
call_3302 = relay.TupleGetItem(func_3174_call(relay.reshape(var_3301.astype('bool'), [10, 7, 7])), 0)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
var_3319 = relay.var("var_3319", dtype = "float64", shape = (88, 1))#candidate|3319|(88, 1)|var|float64
call_3318 = relay.TupleGetItem(func_1748_call(relay.reshape(var_3319.astype('float64'), [11, 2, 4])), 0)
call_3320 = relay.TupleGetItem(func_1750_call(relay.reshape(var_3319.astype('float64'), [11, 2, 4])), 0)
output = relay.Tuple([call_3296,call_3300,var_3301,call_3318,var_3319,])
output2 = relay.Tuple([call_3297,call_3302,var_3301,call_3320,var_3319,])
func_3337 = relay.Function([var_3301,var_3319,], output)
mod['func_3337'] = func_3337
mod = relay.transform.InferType()(mod)
mutated_mod['func_3337'] = func_3337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3337_call = mutated_mod.get_global_var('func_3337')
var_3339 = relay.var("var_3339", dtype = "bool", shape = (490,))#candidate|3339|(490,)|var|bool
var_3340 = relay.var("var_3340", dtype = "float64", shape = (88, 1))#candidate|3340|(88, 1)|var|float64
call_3338 = func_3337_call(var_3339,var_3340,)
output = call_3338
func_3341 = relay.Function([var_3339,var_3340,], output)
mutated_mod['func_3341'] = func_3341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_3349 = relay.TupleGetItem(func_2698_call(), 0)
call_3350 = relay.TupleGetItem(func_2700_call(), 0)
uop_3364 = relay.atanh(call_3349.astype('float64')) # shape=(10, 1, 7)
uop_3366 = relay.atanh(call_3350.astype('float64')) # shape=(10, 1, 7)
uop_3368 = relay.cos(call_3349.astype('float64')) # shape=(10, 1, 7)
uop_3370 = relay.cos(call_3350.astype('float64')) # shape=(10, 1, 7)
uop_3374 = relay.cosh(uop_3364.astype('float32')) # shape=(10, 1, 7)
uop_3376 = relay.cosh(uop_3366.astype('float32')) # shape=(10, 1, 7)
output = relay.Tuple([uop_3368,uop_3374,])
output2 = relay.Tuple([uop_3370,uop_3376,])
func_3385 = relay.Function([], output)
mod['func_3385'] = func_3385
mod = relay.transform.InferType()(mod)
mutated_mod['func_3385'] = func_3385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3385_call = mutated_mod.get_global_var('func_3385')
call_3386 = func_3385_call()
output = call_3386
func_3387 = relay.Function([], output)
mutated_mod['func_3387'] = func_3387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3385_call = mod.get_global_var('func_3385')
func_3387_call = mutated_mod.get_global_var('func_3387')
call_3472 = relay.TupleGetItem(func_3385_call(), 1)
call_3473 = relay.TupleGetItem(func_3387_call(), 1)
output = relay.Tuple([call_3472,])
output2 = relay.Tuple([call_3473,])
func_3498 = relay.Function([], output)
mod['func_3498'] = func_3498
mod = relay.transform.InferType()(mod)
mutated_mod['func_3498'] = func_3498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3498_call = mutated_mod.get_global_var('func_3498')
call_3499 = func_3498_call()
output = call_3499
func_3500 = relay.Function([], output)
mutated_mod['func_3500'] = func_3500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3228_call = mod.get_global_var('func_3228')
func_3230_call = mutated_mod.get_global_var('func_3230')
call_3634 = func_3228_call()
call_3635 = func_3228_call()
output = call_3634
output2 = call_3635
func_3640 = relay.Function([], output)
mod['func_3640'] = func_3640
mod = relay.transform.InferType()(mod)
mutated_mod['func_3640'] = func_3640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3640_call = mutated_mod.get_global_var('func_3640')
call_3641 = func_3640_call()
output = call_3641
func_3642 = relay.Function([], output)
mutated_mod['func_3642'] = func_3642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3228_call = mod.get_global_var('func_3228')
func_3230_call = mutated_mod.get_global_var('func_3230')
call_3675 = func_3228_call()
call_3676 = func_3228_call()
output = call_3675
output2 = call_3676
func_3684 = relay.Function([], output)
mod['func_3684'] = func_3684
mod = relay.transform.InferType()(mod)
output = func_3684()
func_3685 = relay.Function([], output)
mutated_mod['func_3685'] = func_3685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3684_call = mod.get_global_var('func_3684')
func_3685_call = mutated_mod.get_global_var('func_3685')
call_3695 = func_3684_call()
call_3696 = func_3684_call()
func_1253_call = mod.get_global_var('func_1253')
func_1256_call = mutated_mod.get_global_var('func_1256')
var_3714 = relay.var("var_3714", dtype = "float32", shape = (128,))#candidate|3714|(128,)|var|float32
call_3713 = func_1253_call(relay.reshape(var_3714.astype('float32'), [8, 1, 16]))
call_3715 = func_1253_call(relay.reshape(var_3714.astype('float32'), [8, 1, 16]))
output = relay.Tuple([call_3695,call_3713,var_3714,])
output2 = relay.Tuple([call_3696,call_3715,var_3714,])
func_3718 = relay.Function([var_3714,], output)
mod['func_3718'] = func_3718
mod = relay.transform.InferType()(mod)
mutated_mod['func_3718'] = func_3718
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3719 = relay.var("var_3719", dtype = "float32", shape = (128,))#candidate|3719|(128,)|var|float32
func_3718_call = mutated_mod.get_global_var('func_3718')
call_3720 = func_3718_call(var_3719)
output = call_3720
func_3721 = relay.Function([var_3719], output)
mutated_mod['func_3721'] = func_3721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3017_call = mod.get_global_var('func_3017')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_3758 = func_3017_call()
call_3759 = func_3017_call()
output = relay.Tuple([call_3758,])
output2 = relay.Tuple([call_3759,])
func_3761 = relay.Function([], output)
mod['func_3761'] = func_3761
mod = relay.transform.InferType()(mod)
mutated_mod['func_3761'] = func_3761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3761_call = mutated_mod.get_global_var('func_3761')
call_3762 = func_3761_call()
output = call_3762
func_3763 = relay.Function([], output)
mutated_mod['func_3763'] = func_3763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3640_call = mod.get_global_var('func_3640')
func_3642_call = mutated_mod.get_global_var('func_3642')
call_3833 = func_3640_call()
call_3834 = func_3640_call()
output = relay.Tuple([call_3833,])
output2 = relay.Tuple([call_3834,])
func_3836 = relay.Function([], output)
mod['func_3836'] = func_3836
mod = relay.transform.InferType()(mod)
mutated_mod['func_3836'] = func_3836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3836_call = mutated_mod.get_global_var('func_3836')
call_3837 = func_3836_call()
output = call_3837
func_3838 = relay.Function([], output)
mutated_mod['func_3838'] = func_3838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3836_call = mod.get_global_var('func_3836')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_3905 = relay.TupleGetItem(func_3836_call(), 0)
call_3906 = relay.TupleGetItem(func_3838_call(), 0)
var_3909 = relay.var("var_3909", dtype = "bool", shape = (10, 1, 7))#candidate|3909|(10, 1, 7)|var|bool
bop_3910 = relay.logical_or(call_3905.astype('bool'), relay.reshape(var_3909.astype('bool'), relay.shape_of(call_3905))) # shape=(10, 1, 7)
bop_3913 = relay.logical_or(call_3906.astype('bool'), relay.reshape(var_3909.astype('bool'), relay.shape_of(call_3906))) # shape=(10, 1, 7)
output = relay.Tuple([bop_3910,])
output2 = relay.Tuple([bop_3913,])
func_3917 = relay.Function([var_3909,], output)
mod['func_3917'] = func_3917
mod = relay.transform.InferType()(mod)
mutated_mod['func_3917'] = func_3917
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3918 = relay.var("var_3918", dtype = "bool", shape = (10, 1, 7))#candidate|3918|(10, 1, 7)|var|bool
func_3917_call = mutated_mod.get_global_var('func_3917')
call_3919 = func_3917_call(var_3918)
output = call_3919
func_3920 = relay.Function([var_3918], output)
mutated_mod['func_3920'] = func_3920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3640_call = mod.get_global_var('func_3640')
func_3642_call = mutated_mod.get_global_var('func_3642')
call_3927 = func_3640_call()
call_3928 = func_3640_call()
output = call_3927
output2 = call_3928
func_3961 = relay.Function([], output)
mod['func_3961'] = func_3961
mod = relay.transform.InferType()(mod)
output = func_3961()
func_3962 = relay.Function([], output)
mutated_mod['func_3962'] = func_3962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3761_call = mod.get_global_var('func_3761')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_3977 = relay.TupleGetItem(func_3761_call(), 0)
call_3978 = relay.TupleGetItem(func_3763_call(), 0)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_3986 = relay.TupleGetItem(func_2698_call(), 0)
call_3987 = relay.TupleGetItem(func_2700_call(), 0)
output = relay.Tuple([call_3977,call_3986,])
output2 = relay.Tuple([call_3978,call_3987,])
func_3990 = relay.Function([], output)
mod['func_3990'] = func_3990
mod = relay.transform.InferType()(mod)
output = func_3990()
func_3991 = relay.Function([], output)
mutated_mod['func_3991'] = func_3991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3761_call = mod.get_global_var('func_3761')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_4052 = relay.TupleGetItem(func_3761_call(), 0)
call_4053 = relay.TupleGetItem(func_3763_call(), 0)
var_4056 = relay.var("var_4056", dtype = "bool", shape = (10, 2, 7))#candidate|4056|(10, 2, 7)|var|bool
bop_4057 = relay.equal(call_4052.astype('bool'), var_4056.astype('bool')) # shape=(10, 2, 7)
bop_4060 = relay.equal(call_4053.astype('bool'), var_4056.astype('bool')) # shape=(10, 2, 7)
output = bop_4057
output2 = bop_4060
func_4067 = relay.Function([var_4056,], output)
mod['func_4067'] = func_4067
mod = relay.transform.InferType()(mod)
var_4068 = relay.var("var_4068", dtype = "bool", shape = (10, 2, 7))#candidate|4068|(10, 2, 7)|var|bool
output = func_4067(var_4068)
func_4069 = relay.Function([var_4068], output)
mutated_mod['func_4069'] = func_4069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3836_call = mod.get_global_var('func_3836')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_4157 = relay.TupleGetItem(func_3836_call(), 0)
call_4158 = relay.TupleGetItem(func_3838_call(), 0)
var_4174 = relay.var("var_4174", dtype = "bool", shape = (10, 2, 7))#candidate|4174|(10, 2, 7)|var|bool
bop_4175 = relay.floor_divide(call_4157.astype('float32'), var_4174.astype('float32')) # shape=(10, 2, 7)
bop_4178 = relay.floor_divide(call_4158.astype('float32'), var_4174.astype('float32')) # shape=(10, 2, 7)
func_3017_call = mod.get_global_var('func_3017')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_4187 = func_3017_call()
call_4188 = func_3017_call()
func_3017_call = mod.get_global_var('func_3017')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_4195 = func_3017_call()
call_4196 = func_3017_call()
func_566_call = mod.get_global_var('func_566')
func_570_call = mutated_mod.get_global_var('func_570')
const_4199 = relay.const([5,-9,6,5,4,8,-8,3,-6,-2,-1,4,-6,-2,-4,-2,-6,-2,-10,2,-10,-7,3,-2,4,-8,2,8,-4,4,1,7,-6,8,5,10,-10,-6,7,-4,1,-6,5,8,-4,7,10,-3,-4,2,2,-7,-7,9,-10,-6,6,3,-8,3,7,9,6,2,2,-1,6,-9,2,8,1,-4,-10,8,-10,-9,-3,-4,10,-8,2,9,1,10,3,5,3,-1,-8,10,2,-5,-10,3,-5,-2,-4,2,8,7,1,7,3,7,-9,-9,10,5,3,10,10,-6,3,-10,-1,2,10,5,7,5,3,-6,-8,-1,-2,-2,2,-9,-5,6,5,-7,7,-10,-6,-10,-9,-1,1,9,-4,-6,-8,-3,-3,8,-9,4,-8,10,-9,4,9,6,-1,3,-7,-4,-5,7,-8,-9,1,4,-10,-7,7,9,-9,7,-2,-5,-1,-2,-6,8,6,-2,1,-8,10,-9,7,4,3,-7,-4,-3,-3,-3,6,4,9,8,-4,2,-2,-3,-1,6,-10,8,-9,-7,6,1,1,1,-5,-1,-5,-3,4,-7,-2,-8,8,-4,-6,9,-5,3,10,-8,-5,2,-10,9,2,6,9,-6,-9,-5,-5,7,7,-6,4,-9,-10,8,-7,-3,-3,3,-4,-8,-1,-10,-7,8,4,8,7,6,-2,1,-3,8,-5,7,-2,-6,10,-3,10,-1,-5,-4,-8,-4,-7,10,9,-8,-3,-8,2,1,-10,8,-6,-4,-8,5,-9,6,4,-7,-8,-9,-2,7,3,-3,-2,10,-10,9,5,3,5,-1,7,-3,-3,-7,3,8,-2,6,-3,-2,-3,8,6,-3,1,3,-1,5,1,8,6,8,8,1,-2,-2,-5,4,-2,-4,8,4,-4,-3,3,-10,9,8,-2,9,-4,-1,-5,-10,-10,1,4,7], dtype = "uint16")#candidate|4199|(352,)|const|uint16
call_4198 = func_566_call(relay.reshape(const_4199.astype('uint16'), [4, 11, 8]), relay.reshape(const_4199.astype('uint16'), [4, 11, 8]), )
call_4200 = func_566_call(relay.reshape(const_4199.astype('uint16'), [4, 11, 8]), relay.reshape(const_4199.astype('uint16'), [4, 11, 8]), )
bop_4220 = relay.greater_equal(call_4195.astype('bool'), relay.reshape(call_4187.astype('bool'), relay.shape_of(call_4195))) # shape=(10, 1, 7)
bop_4223 = relay.greater_equal(call_4196.astype('bool'), relay.reshape(call_4188.astype('bool'), relay.shape_of(call_4196))) # shape=(10, 1, 7)
output = relay.Tuple([bop_4175,call_4198,const_4199,bop_4220,])
output2 = relay.Tuple([bop_4178,call_4200,const_4199,bop_4223,])
func_4228 = relay.Function([var_4174,], output)
mod['func_4228'] = func_4228
mod = relay.transform.InferType()(mod)
var_4229 = relay.var("var_4229", dtype = "bool", shape = (10, 2, 7))#candidate|4229|(10, 2, 7)|var|bool
output = func_4228(var_4229)
func_4230 = relay.Function([var_4229], output)
mutated_mod['func_4230'] = func_4230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_4232 = relay.TupleGetItem(func_2773_call(), 2)
call_4233 = relay.TupleGetItem(func_2775_call(), 2)
uop_4238 = relay.asin(call_4232.astype('float32')) # shape=(352, 1)
uop_4240 = relay.asin(call_4233.astype('float32')) # shape=(352, 1)
uop_4245 = relay.sin(uop_4238.astype('float32')) # shape=(352, 1)
uop_4247 = relay.sin(uop_4240.astype('float32')) # shape=(352, 1)
output = relay.Tuple([uop_4245,])
output2 = relay.Tuple([uop_4247,])
func_4248 = relay.Function([], output)
mod['func_4248'] = func_4248
mod = relay.transform.InferType()(mod)
mutated_mod['func_4248'] = func_4248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4248_call = mutated_mod.get_global_var('func_4248')
call_4249 = func_4248_call()
output = call_4249
func_4250 = relay.Function([], output)
mutated_mod['func_4250'] = func_4250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3228_call = mod.get_global_var('func_3228')
func_3230_call = mutated_mod.get_global_var('func_3230')
call_4263 = func_3228_call()
call_4264 = func_3228_call()
func_3990_call = mod.get_global_var('func_3990')
func_3991_call = mutated_mod.get_global_var('func_3991')
call_4273 = relay.TupleGetItem(func_3990_call(), 0)
call_4274 = relay.TupleGetItem(func_3991_call(), 0)
output = relay.Tuple([call_4263,call_4273,])
output2 = relay.Tuple([call_4264,call_4274,])
func_4280 = relay.Function([], output)
mod['func_4280'] = func_4280
mod = relay.transform.InferType()(mod)
mutated_mod['func_4280'] = func_4280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mutated_mod.get_global_var('func_4280')
call_4281 = func_4280_call()
output = call_4281
func_4282 = relay.Function([], output)
mutated_mod['func_4282'] = func_4282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3761_call = mod.get_global_var('func_3761')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_4285 = relay.TupleGetItem(func_3761_call(), 0)
call_4286 = relay.TupleGetItem(func_3763_call(), 0)
uop_4288 = relay.sqrt(call_4285.astype('float64')) # shape=(10, 1, 7)
uop_4290 = relay.sqrt(call_4286.astype('float64')) # shape=(10, 1, 7)
output = uop_4288
output2 = uop_4290
func_4296 = relay.Function([], output)
mod['func_4296'] = func_4296
mod = relay.transform.InferType()(mod)
mutated_mod['func_4296'] = func_4296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4296_call = mutated_mod.get_global_var('func_4296')
call_4297 = func_4296_call()
output = call_4297
func_4298 = relay.Function([], output)
mutated_mod['func_4298'] = func_4298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3385_call = mod.get_global_var('func_3385')
func_3387_call = mutated_mod.get_global_var('func_3387')
call_4324 = relay.TupleGetItem(func_3385_call(), 0)
call_4325 = relay.TupleGetItem(func_3387_call(), 0)
var_4331 = relay.var("var_4331", dtype = "float64", shape = (10, 1, 7))#candidate|4331|(10, 1, 7)|var|float64
bop_4332 = relay.bitwise_or(call_4324.astype('int32'), relay.reshape(var_4331.astype('int32'), relay.shape_of(call_4324))) # shape=(10, 1, 7)
bop_4335 = relay.bitwise_or(call_4325.astype('int32'), relay.reshape(var_4331.astype('int32'), relay.shape_of(call_4325))) # shape=(10, 1, 7)
func_3718_call = mod.get_global_var('func_3718')
func_3721_call = mutated_mod.get_global_var('func_3721')
var_4347 = relay.var("var_4347", dtype = "float32", shape = (128,))#candidate|4347|(128,)|var|float32
call_4346 = relay.TupleGetItem(func_3718_call(relay.reshape(var_4347.astype('float32'), [128,])), 2)
call_4348 = relay.TupleGetItem(func_3721_call(relay.reshape(var_4347.astype('float32'), [128,])), 2)
func_4067_call = mod.get_global_var('func_4067')
func_4069_call = mutated_mod.get_global_var('func_4069')
const_4350 = relay.const([True,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,True,True], dtype = "bool")#candidate|4350|(140,)|const|bool
call_4349 = func_4067_call(relay.reshape(const_4350.astype('bool'), [10, 2, 7]))
call_4351 = func_4067_call(relay.reshape(const_4350.astype('bool'), [10, 2, 7]))
output = relay.Tuple([bop_4332,call_4346,var_4347,call_4349,const_4350,])
output2 = relay.Tuple([bop_4335,call_4348,var_4347,call_4351,const_4350,])
func_4361 = relay.Function([var_4331,var_4347,], output)
mod['func_4361'] = func_4361
mod = relay.transform.InferType()(mod)
var_4362 = relay.var("var_4362", dtype = "float64", shape = (10, 1, 7))#candidate|4362|(10, 1, 7)|var|float64
var_4363 = relay.var("var_4363", dtype = "float32", shape = (128,))#candidate|4363|(128,)|var|float32
output = func_4361(var_4362,var_4363,)
func_4364 = relay.Function([var_4362,var_4363,], output)
mutated_mod['func_4364'] = func_4364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4248_call = mod.get_global_var('func_4248')
func_4250_call = mutated_mod.get_global_var('func_4250')
call_4447 = relay.TupleGetItem(func_4248_call(), 0)
call_4448 = relay.TupleGetItem(func_4250_call(), 0)
var_4449 = relay.var("var_4449", dtype = "float32", shape = (352, 6))#candidate|4449|(352, 6)|var|float32
bop_4450 = relay.logical_or(call_4447.astype('bool'), var_4449.astype('bool')) # shape=(352, 6)
bop_4453 = relay.logical_or(call_4448.astype('bool'), var_4449.astype('bool')) # shape=(352, 6)
bop_4455 = relay.logical_xor(call_4447.astype('int16'), var_4449.astype('int16')) # shape=(352, 6)
bop_4458 = relay.logical_xor(call_4448.astype('int16'), var_4449.astype('int16')) # shape=(352, 6)
output = relay.Tuple([bop_4450,bop_4455,])
output2 = relay.Tuple([bop_4453,bop_4458,])
func_4460 = relay.Function([var_4449,], output)
mod['func_4460'] = func_4460
mod = relay.transform.InferType()(mod)
var_4461 = relay.var("var_4461", dtype = "float32", shape = (352, 6))#candidate|4461|(352, 6)|var|float32
output = func_4460(var_4461)
func_4462 = relay.Function([var_4461], output)
mutated_mod['func_4462'] = func_4462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_4484 = relay.TupleGetItem(func_2698_call(), 0)
call_4485 = relay.TupleGetItem(func_2700_call(), 0)
output = relay.Tuple([call_4484,])
output2 = relay.Tuple([call_4485,])
func_4497 = relay.Function([], output)
mod['func_4497'] = func_4497
mod = relay.transform.InferType()(mod)
output = func_4497()
func_4498 = relay.Function([], output)
mutated_mod['func_4498'] = func_4498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4248_call = mod.get_global_var('func_4248')
func_4250_call = mutated_mod.get_global_var('func_4250')
call_4612 = relay.TupleGetItem(func_4248_call(), 0)
call_4613 = relay.TupleGetItem(func_4250_call(), 0)
const_4614 = relay.const([[-6.004368,-5.930579,9.824038,-0.166474,-7.123741],[6.778157,-2.442831,-3.846053,-2.593885,-2.115646],[4.549250,5.969105,-8.047484,1.123032,-5.431317],[0.549120,-4.535540,6.044027,0.843871,3.659217],[6.536548,7.815144,-1.329692,-9.368860,-0.137036],[-5.909657,8.644836,-1.175937,5.462539,8.449747],[-5.616734,-1.047100,-9.789689,-8.596525,1.773807],[4.365522,-3.989515,-9.444871,-1.680591,7.945300],[4.860990,-6.557965,5.199364,8.925368,-4.900339],[2.962632,8.934517,-3.629392,9.529483,-8.472355],[-0.485533,4.247806,-0.929930,1.979766,-5.509892],[-9.921780,-1.564564,-3.940721,1.277594,-5.949908],[-7.596567,-5.504338,-2.548133,0.888158,1.605348],[-7.874476,8.894810,-1.241870,-0.724658,-3.932239],[-1.709422,-3.379259,9.629748,1.650479,-5.771804],[9.306262,4.511937,9.302670,-7.811726,4.452730],[-8.322759,5.105879,-9.022440,8.036938,9.061346],[5.231966,-6.001498,-7.324522,2.880808,-0.651389],[0.554222,-4.990381,2.551323,-6.864661,8.376012],[9.741038,-8.641946,3.001331,-4.120946,7.799626],[1.930107,-9.480264,-2.513934,5.831584,-1.998895],[-5.573942,5.700039,-4.017460,-5.848077,-5.697341],[-6.928423,0.897952,-4.886870,4.753696,1.646379],[-6.664080,-0.256406,4.133367,0.659847,-5.452240],[-5.990907,-7.835134,7.794545,1.576315,1.860081],[9.174719,8.279229,-4.272897,-4.098307,2.248756],[-7.750281,-0.533741,-8.340334,-6.944615,-9.221985],[2.068546,1.126605,5.099756,-8.064461,-3.980008],[-8.433013,7.012394,-8.045741,-6.442134,-8.123076],[-3.544713,7.612939,7.511459,-4.867706,-4.191131],[-5.458332,-3.646134,5.766065,-0.409892,-0.261062],[9.656847,8.624244,-0.730475,7.568590,-2.140539],[-5.861780,-6.535334,6.936791,1.548691,4.131988],[-3.621331,8.266213,9.639345,-3.943371,-1.967779],[-5.188605,-0.360244,8.469777,4.981745,8.233618],[-0.251356,7.137723,4.261094,-9.356506,-7.353825],[-8.406822,1.898201,8.709474,-8.954636,-6.037869],[-4.750141,0.798735,-8.585458,-8.901249,7.199157],[4.276483,1.244928,-3.373845,3.323292,-4.232284],[6.041541,7.351877,-9.214046,0.525102,-8.380871],[-2.164607,1.162571,4.011216,-8.424481,6.917505],[1.525444,5.563626,9.561322,-5.456111,-0.625177],[1.309275,5.228776,-0.868672,9.407716,6.488406],[2.409455,4.719510,3.342920,7.876965,-4.815324],[7.621485,4.205909,-5.316428,-6.708765,-9.971524],[4.236952,-2.671824,-8.128116,5.726530,1.771823],[9.544543,-4.694713,4.950366,-8.046942,7.348417],[1.023068,-3.062071,8.982494,-3.821794,7.957101],[-3.749365,-1.881567,-3.364518,5.206253,-6.184989],[-9.817439,4.983488,-3.984488,-0.882320,0.014774],[3.501408,-0.092314,-3.130050,0.167841,7.232456],[6.205299,2.224710,1.982096,-5.244132,4.355035],[7.134633,-3.031013,-8.487087,6.876272,4.783150],[-3.497686,1.100915,0.475003,-9.117215,-7.080149],[9.933202,1.355349,6.635992,-4.790747,7.248155],[9.182114,3.951448,-7.336885,-6.857615,-9.148730],[-8.994703,6.430178,6.236366,9.957185,6.995799],[-6.110653,6.848926,7.933420,-5.857288,-5.528659],[-9.696568,-9.123603,-7.705651,9.041578,-7.067125],[-4.458446,4.506378,-5.320266,-2.654758,-7.078387],[-4.281517,8.670353,3.737157,-1.634728,-6.007422],[4.725112,-5.366617,0.515189,-4.281377,-1.816615],[-7.288572,-7.030714,-9.253529,5.894452,-5.555234],[-7.047235,-9.027013,6.979155,-8.995288,8.975590],[-3.775672,0.859167,-5.577557,9.083804,-0.029131],[1.549982,9.443666,-1.495352,-1.147531,-5.539698],[2.292024,8.217392,-5.065850,8.182002,4.708193],[-2.562466,-2.182431,-5.781234,-1.888187,8.447312],[8.270063,0.694967,-7.287344,-2.833039,9.380713],[-7.847817,2.642675,-3.175701,-5.584134,4.167052],[-9.019966,7.811173,5.116821,4.003361,-3.953287],[-7.594995,7.073567,-3.084941,5.958024,9.395004],[5.506514,-3.577358,3.012679,5.196788,-9.233049],[9.147154,-1.829861,4.794053,3.351502,0.846422],[-3.451865,6.079038,9.472912,5.125982,0.462392],[-9.480375,-8.512803,6.014860,1.590100,5.395808],[7.651539,1.998167,-1.288890,-0.470236,5.020202],[4.846476,2.086890,-3.705075,-9.686422,-5.797137],[-6.627660,-8.322039,6.104309,-1.739250,-4.694975],[-3.009817,7.531449,3.107282,2.317604,4.905214],[9.211312,-9.611199,5.002660,-5.182757,-1.180542],[9.031180,3.051337,-2.411163,-9.833722,3.963742],[-1.384631,-8.187557,4.698625,8.123858,2.016504],[-6.790310,9.251121,-4.128601,7.146848,-8.727067],[8.383729,-5.008271,-4.775587,5.943434,5.403315],[2.677049,-7.800055,4.994054,-2.797893,-6.275602],[1.310261,-3.780893,6.970071,-3.834808,9.939356],[9.101477,-4.983344,4.525881,-8.877176,2.747013],[-2.600123,5.548415,7.472495,-7.986094,-4.375798],[3.852327,3.652685,-0.897395,-5.092963,8.326945],[-0.707572,-9.988720,-9.096197,9.914834,-9.500425],[8.814769,5.265727,-5.408620,7.008694,-5.047003],[5.885689,-4.138557,-0.116533,-7.386680,1.366786],[-7.315339,-0.028209,-5.962172,3.748959,5.896754],[8.082541,-4.319388,2.907204,0.553415,2.445382],[-1.145457,8.951396,-3.506443,-4.362311,2.167535],[-9.926361,1.253475,-1.872724,-4.402961,2.854714],[-0.159004,-4.241845,0.655772,9.210532,-1.579655],[4.392162,7.676242,6.986710,-1.758789,-8.743925],[2.174839,2.053438,2.716763,2.452630,4.156079],[0.407535,9.117906,-6.676392,-5.797385,8.771538],[7.105032,2.516317,9.963017,-2.132798,-4.387987],[2.430622,8.057166,-5.571409,5.451772,-0.293421],[-8.760859,-2.730147,7.581274,2.292021,-4.431758],[3.567243,1.891482,-1.575016,7.342162,-9.831651],[-6.915203,-5.966538,-2.984955,-7.755318,-2.373190],[9.356223,9.740486,-1.361398,-3.700510,-1.319484],[-2.582410,-6.448404,-7.944511,-1.106243,9.297382],[-5.082166,1.884919,-8.195798,7.626655,7.567674],[7.220475,4.628214,-3.596844,-8.570856,0.229990],[2.946163,-9.899943,4.840779,-9.567927,-9.122349],[-0.022353,3.893918,7.385067,5.004974,5.106085],[-8.800369,3.277865,6.456270,5.433315,0.198975],[-4.124398,-8.653237,-4.669054,2.516867,-2.109034],[2.945219,-4.657056,-9.016371,-7.429893,0.748879],[-0.046950,-2.112966,7.212604,9.840703,4.363574],[9.880100,7.699236,-7.541375,0.446287,-3.250287],[-6.736031,-6.912540,3.239965,-0.714799,-2.804604],[9.541024,-7.768160,5.909069,8.663442,-6.226621],[7.393908,-8.985306,-1.941107,-7.439146,-9.741247],[0.890320,-7.868233,-3.375939,-4.661707,9.611248],[-0.757692,6.967709,5.852238,-4.293770,3.774419],[1.337819,-7.135612,5.587187,6.804506,-5.960348],[-4.553561,-4.571099,7.804806,-9.086151,1.485666],[-1.417423,-6.702387,-4.405205,-1.154577,-7.308962],[-7.767105,-7.116651,9.397313,6.217943,-4.563899],[7.567665,8.768120,1.877352,-0.472928,-3.309625],[-6.803503,0.739109,-5.275031,-0.214485,-1.256729],[-7.914482,-8.408520,4.415794,-5.455939,-0.253267],[-7.765629,2.067658,9.972102,-0.052088,0.393553],[-5.761593,4.689099,-7.068706,9.335029,7.513161],[-4.799591,-2.129260,-9.204086,-1.255101,-6.974028],[9.106558,-0.412095,-5.532633,-5.345043,3.221780],[9.322395,0.858933,1.241447,-4.608162,-4.869017],[-0.551831,3.416100,5.942249,-9.636779,-4.973315],[2.412367,9.391063,6.481230,6.397606,-8.801871],[9.670387,-6.430091,3.630053,-9.192625,9.346935],[0.640162,8.958246,-8.223287,-6.918856,1.164486],[-1.216889,7.427556,-4.390635,3.006544,-1.197937],[1.840812,-0.969312,-9.136863,6.874701,0.969429],[4.300772,0.765457,-4.869600,0.789325,-7.289731],[9.973343,8.034744,0.098310,0.557828,-5.149046],[-7.900988,2.286238,8.766223,-5.480331,4.294448],[5.816922,-3.458182,6.479307,5.382475,-6.410379],[7.131366,-2.346034,-0.047260,0.921971,-6.512846],[6.596536,2.982537,9.197049,-4.433170,6.863697],[-9.951695,-7.400365,7.003336,1.411694,-7.231505],[7.694925,7.981538,4.338280,1.885531,-8.738661],[-4.455102,-8.276598,-6.967454,-5.879917,-5.503228],[-5.502258,9.343396,2.107047,8.169317,5.371826],[-4.737809,8.936186,-4.262507,3.168256,3.520296],[2.897027,3.977154,8.057208,-5.632536,-6.453094],[-5.790426,6.395444,5.640655,-2.959200,4.877919],[9.610357,-9.153395,6.488406,8.824692,-4.805694],[-8.305642,-9.776262,-4.848706,-0.315442,0.213655],[3.768682,9.094384,7.018550,2.881516,3.654614],[7.833942,8.099150,-0.843275,-0.598106,9.967404],[-6.492479,4.002267,-3.214051,8.990338,-4.583668],[9.764486,-7.788765,-8.875326,-8.146028,0.709869],[-2.189075,-2.613189,2.582010,-0.189649,-6.891395],[-0.615877,-0.844798,0.809859,7.841615,0.878210],[5.838801,8.903756,9.538627,-6.121321,-0.649841],[-7.208693,-9.268436,-7.866472,2.621882,-4.793558],[-2.001771,-5.653943,-4.756328,4.900998,-0.097407],[5.126695,-7.745063,1.384946,-8.872835,9.046331],[-6.700581,1.123324,-8.303584,-9.994684,-7.630909],[9.755919,4.943573,0.855808,2.231501,-0.649177],[4.743392,0.095838,-0.395219,-8.683814,-6.303146],[9.993931,1.477732,-3.065732,-7.996200,4.528548],[9.940049,-2.366563,-8.360207,-1.708418,-6.881077],[-6.479402,-3.646778,2.162538,-8.286442,7.647265],[7.109909,4.865770,1.642694,-5.974144,-4.418533],[-8.255877,-6.012526,4.520350,6.587965,-0.448819],[-1.072185,7.252534,1.654100,2.838095,-5.682691],[-6.001865,-9.739001,-3.853744,2.948380,3.756401],[-3.029375,7.402442,-8.168865,-9.176250,-9.710174],[-3.580426,9.142954,7.353323,-6.933409,-6.200099],[0.995399,9.238644,3.427354,9.933281,-6.073698],[-6.230168,1.404809,-1.771998,-5.120505,8.506158],[7.969338,6.816641,9.360951,4.640136,-0.272827],[8.635534,0.197316,4.188373,-0.735000,4.694138],[5.026743,-2.927687,-1.427996,1.861875,1.161368],[2.605980,-9.855497,1.238906,-2.545889,3.496584],[-6.304596,-7.456969,6.815549,-2.230217,8.477035],[6.027652,-6.179833,6.834834,-5.326885,6.615504],[3.089024,-7.039583,-8.003417,7.823857,4.663735],[1.771903,3.597206,9.626269,0.336343,0.190297],[1.732542,8.583662,-0.769966,-6.267105,1.516253],[-8.186604,3.017768,-3.548387,-0.935632,-2.430759],[3.275069,8.958739,2.109739,9.956198,4.154786],[0.554183,1.496729,-3.170160,3.059812,-6.792424],[-1.708720,7.348355,-1.229576,4.331514,-8.925797],[-1.988152,6.655715,-6.137076,-4.465748,5.303745],[-7.746531,-5.371532,-4.526929,3.878008,-4.267721],[-4.845683,-9.696489,-9.347596,-1.140227,9.201202],[6.807493,-4.752816,-1.227839,0.095796,-0.163600],[-9.389437,-3.989907,9.690137,3.350805,-4.105310],[-6.866771,-5.968305,6.980947,2.941578,2.325226],[-6.282600,-0.653801,9.904643,0.177484,1.281183],[-1.341855,7.728980,1.655218,9.631244,1.955472],[-8.318011,-0.391383,1.649139,0.692777,7.040614],[8.938705,7.756799,-2.895157,-4.361380,1.617159],[-1.389890,5.297180,-0.046157,-0.791972,2.589500],[-0.838246,5.934314,8.101543,-8.737944,-3.235452],[5.718296,9.593731,7.650330,0.758672,6.208667],[-5.357670,-8.624101,5.231857,-7.202718,-1.617565],[-6.040185,9.509378,-5.673310,-7.701964,1.299242],[-0.769721,-9.255268,7.360002,-4.074872,-1.620261],[8.228986,1.125446,-8.812712,1.918993,-9.480251],[8.148585,-8.939345,-4.340956,0.028084,9.969783],[5.717052,5.783121,8.586464,-2.455492,8.488321],[9.496387,6.997933,4.316285,-2.762914,-7.248294],[-8.369489,6.115527,-9.703662,3.897039,-7.711505],[-7.365089,1.836698,6.526661,-8.369862,-8.601775],[-6.115657,-5.118892,-2.412313,-2.304741,-3.648025],[2.492946,-0.738433,9.674255,-7.555806,-6.155209],[5.129522,2.677970,-8.804750,8.300563,-1.927642],[-0.702557,-5.792433,-4.004614,-7.010555,7.084970],[9.548917,-0.784318,2.796117,-7.823045,-5.598758],[-6.175148,3.590995,-7.847439,-9.702335,-4.544140],[8.459731,-1.090679,8.829542,-0.497135,5.909711],[1.499063,-8.578257,-5.631726,1.665126,-5.279195],[8.970439,-0.893310,-7.892556,-3.526815,-7.648735],[1.116122,4.619899,5.217506,-9.494534,7.105007],[4.992679,-0.407931,-8.719619,6.973476,2.489812],[8.070016,-3.359919,2.628197,4.503973,-3.151190],[-6.768351,3.793344,9.871862,-9.222702,4.935365],[5.279700,-1.424802,-4.613591,-5.286854,4.567927],[2.672946,-7.174468,-7.790161,-6.906774,1.592505],[0.687343,-2.961109,5.928687,-2.484674,2.358365],[9.130049,-0.504133,-3.791139,-0.697170,6.513778],[-4.973639,1.824264,-5.145654,-0.239781,7.255861],[8.889975,9.687696,8.619251,0.633154,3.523133],[7.481415,4.803839,-9.754356,2.438733,-8.593915],[-2.245803,1.562753,2.965985,6.946904,6.756967],[5.004871,-5.232787,-2.120374,-2.455217,8.733415],[1.987356,-6.300367,-1.202454,-9.354459,-5.583927],[-2.527469,-6.022774,-1.254035,-6.589636,8.221814],[-4.225128,-5.273550,-8.374631,-0.298635,9.175487],[-7.677197,1.181096,8.890517,7.899049,6.886593],[6.595126,7.023596,6.884859,9.240935,0.810859],[3.637780,-3.449663,-6.387687,8.345640,3.704267],[-3.065701,4.291732,-8.355998,-7.672275,-2.457474],[9.869727,9.233874,3.591497,-5.480354,-3.274215],[-8.563395,6.572569,-2.066288,8.469476,4.656494],[-0.092969,-3.479496,1.736571,-1.836158,-5.819878],[3.368435,-4.686688,-0.483699,6.598401,8.012231],[3.543944,-7.729781,-7.060476,-8.977701,-3.196124],[-6.670606,-8.508843,-6.452808,1.495385,8.222731],[2.504580,-3.145199,1.892076,-9.355094,1.411737],[9.271270,1.102176,-5.898476,-5.102289,2.203399],[-7.693099,0.190789,-3.782058,-5.464597,-9.507800],[8.356077,-6.209285,-5.234203,4.310786,-8.456113],[-1.029913,5.679299,7.131471,3.816701,-4.513488],[-2.371817,-2.764686,8.508718,2.084317,-8.381289],[6.822249,-6.821339,4.236689,-7.550439,0.519460],[-4.836055,-9.136547,9.651916,0.451557,6.810988],[2.035423,-8.378146,4.498577,-6.701057,7.014666],[-1.711152,-3.783767,-6.400061,4.708556,-3.353417],[0.213690,-6.563008,-3.511111,-8.903606,-2.806955],[-1.490598,6.213179,4.100998,-6.154388,-8.865974],[8.557465,2.319819,9.152669,3.665190,-3.008579],[2.773548,-0.970933,1.935372,6.916851,-5.079245],[7.408027,1.992391,9.698813,9.702836,-7.112328],[9.921094,-9.553845,9.323009,-3.014519,9.832247],[9.197769,5.329553,-8.537541,-5.351912,-3.205645],[-4.040820,9.956549,-7.486784,-0.490817,6.736364],[1.989664,-4.030513,5.948733,9.070733,9.138325],[-4.669263,4.372538,-0.955494,-0.830811,1.714986],[-5.102560,-5.707606,6.260513,-2.069151,-0.092378],[-4.759025,9.911671,0.737948,6.684857,-6.792277],[5.478136,3.085123,-2.009166,9.631018,-5.350671],[3.734712,-2.943290,1.276724,9.764177,3.099292],[1.301362,0.983912,4.643121,2.855524,-2.940738],[1.360309,-1.260562,-7.986655,-8.127776,5.904134],[6.738980,5.863413,-9.218900,7.335919,9.995340],[2.532983,0.080335,3.817600,2.412891,7.944011],[-4.566654,-9.604114,1.553585,-0.785610,-0.706972],[-4.979478,-8.522410,5.852917,-9.604987,-1.925911],[2.706870,-8.384440,4.375608,4.762602,-6.734896],[-7.110767,4.481669,6.550583,6.572251,3.724328],[0.033451,6.885238,4.675712,-1.474707,-2.590850],[6.836842,-7.017321,-3.152317,7.388352,1.464134],[-3.419716,9.944715,-1.694131,-1.711376,-2.285019],[3.902099,5.831613,6.032968,9.268723,5.577504],[5.323576,8.538913,-6.887434,8.937045,-2.835452],[-0.411345,-9.486171,-3.174968,-8.604056,-9.160474],[-6.930462,4.276505,0.225324,1.636861,-7.339553],[-5.019380,9.871384,-1.566809,8.146678,-6.276460],[-3.620523,-2.144017,-6.295165,3.274496,6.112598],[8.469279,1.508702,5.337379,2.617019,4.506699],[7.681577,7.522857,0.827439,3.433497,0.373307],[-6.358466,-4.058227,-3.250119,-1.732053,2.137824],[-4.816767,7.567662,7.532042,-0.221409,7.507668],[3.414264,0.526647,-2.257022,-5.601189,7.436105],[3.101196,0.058709,-4.874663,-2.072181,2.569887],[-3.862640,-3.466583,2.586089,-1.094683,-8.611626],[1.767604,2.966913,3.059269,0.748505,5.740382],[7.533779,2.635628,-5.074979,1.233122,-3.255755],[-7.410010,-6.551620,-7.131389,8.307286,4.129264],[4.523242,4.360683,6.242126,-6.703769,-7.652253],[0.498608,-0.336556,-2.701309,-2.982460,2.988559],[-1.161010,9.877229,-9.336784,-1.344452,-8.235439],[6.825247,-0.614723,-0.482954,2.663885,-5.427974],[-0.389944,-0.330982,-3.644559,7.401355,-5.503599],[9.149451,0.117494,8.564864,4.375584,2.364944],[2.389639,4.953461,0.559106,9.720772,-5.803879],[-5.558369,4.842168,6.137541,4.258184,-9.523538],[7.928934,-5.956372,-1.879244,-0.022926,5.935487],[5.796774,-8.959122,-7.691231,2.242344,4.863320],[3.043903,-7.961574,-9.115925,8.184847,4.220881],[9.708282,2.006755,2.174855,0.810474,1.181974],[0.608542,5.229878,3.395711,3.467048,7.197605],[-3.462574,-6.942660,2.003402,-4.691272,-3.259244],[-5.283468,-4.324654,4.673176,0.285235,7.031935],[6.918575,4.344772,5.966158,-6.735811,8.424439],[5.478612,-1.750445,9.618273,-7.645356,-8.807685],[0.946767,-1.971416,4.246716,1.829703,-0.134628],[3.090845,4.883722,-9.132685,-9.515351,7.949417],[-9.385974,8.009994,-2.852479,-0.032857,3.889171],[3.444009,5.123798,-9.012473,9.914514,2.787486],[7.288927,5.701224,4.538009,5.902206,-5.143340],[-8.713106,9.163186,2.571324,-0.999958,-0.107334],[3.457604,-0.753073,9.138903,7.482942,-0.901554],[-0.985750,6.105341,-7.340190,1.735111,-4.989303],[-9.282653,-2.014923,4.627672,7.522937,6.713361],[9.086895,9.855556,8.643422,-9.956777,8.630756],[1.827881,-5.687793,9.086427,5.599001,-7.331097],[-6.067952,-1.080693,-1.846034,-2.696697,9.140865],[2.505763,-4.728063,-9.921554,2.183732,-0.092434],[6.683315,-4.516610,3.529883,-0.605245,-4.400559],[-8.129982,0.843470,6.132516,-8.727018,8.233761],[5.403792,-4.368583,7.796067,6.852258,-1.063937],[4.132154,6.278399,0.084648,1.753284,-8.503836],[3.801261,-1.900551,7.076227,-9.378163,-2.742323],[-1.537640,6.703558,6.766531,6.583636,5.548264],[9.239519,-2.880235,5.640546,7.689295,0.451813],[-9.114938,-3.981229,-1.877607,0.173878,-8.331772],[-9.604766,5.919088,0.221082,2.194723,-0.043100],[-5.481496,5.779769,-2.181208,3.568753,-9.090275],[1.575907,5.219319,8.769640,-3.285626,-0.576169],[-9.401144,9.599785,-9.225332,7.806213,4.094000],[0.884299,5.807479,-0.529520,2.061256,3.317738],[1.706915,-2.169627,-3.193751,-1.818701,-1.653046],[2.832656,5.842378,5.072399,-9.453492,8.385956],[-8.905424,6.496460,-4.491334,3.926340,0.964159],[4.034078,-7.181801,9.513525,5.497145,1.634732],[2.793105,4.204559,5.678676,-7.799591,3.154567],[0.006551,-1.284008,8.395214,1.060202,-0.426573],[3.557031,6.832260,-6.536405,-8.419063,-3.761950],[1.748383,8.378039,-8.197249,7.579046,-2.749668],[3.223242,-9.994677,-7.914823,-6.944939,3.077446]], dtype = "float32")#candidate|4614|(352, 5)|const|float32
bop_4615 = relay.logical_or(call_4612.astype('bool'), const_4614.astype('bool')) # shape=(352, 5)
bop_4618 = relay.logical_or(call_4613.astype('bool'), const_4614.astype('bool')) # shape=(352, 5)
output = relay.Tuple([bop_4615,])
output2 = relay.Tuple([bop_4618,])
func_4622 = relay.Function([], output)
mod['func_4622'] = func_4622
mod = relay.transform.InferType()(mod)
output = func_4622()
func_4623 = relay.Function([], output)
mutated_mod['func_4623'] = func_4623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mod.get_global_var('func_4280')
func_4282_call = mutated_mod.get_global_var('func_4282')
call_4740 = relay.TupleGetItem(func_4280_call(), 1)
call_4741 = relay.TupleGetItem(func_4282_call(), 1)
output = call_4740
output2 = call_4741
func_4744 = relay.Function([], output)
mod['func_4744'] = func_4744
mod = relay.transform.InferType()(mod)
output = func_4744()
func_4745 = relay.Function([], output)
mutated_mod['func_4745'] = func_4745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3498_call = mod.get_global_var('func_3498')
func_3500_call = mutated_mod.get_global_var('func_3500')
call_4749 = relay.TupleGetItem(func_3498_call(), 0)
call_4750 = relay.TupleGetItem(func_3500_call(), 0)
output = call_4749
output2 = call_4750
func_4751 = relay.Function([], output)
mod['func_4751'] = func_4751
mod = relay.transform.InferType()(mod)
mutated_mod['func_4751'] = func_4751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4751_call = mutated_mod.get_global_var('func_4751')
call_4752 = func_4751_call()
output = call_4752
func_4753 = relay.Function([], output)
mutated_mod['func_4753'] = func_4753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_4793 = func_3961_call()
call_4794 = func_3961_call()
output = call_4793
output2 = call_4794
func_4803 = relay.Function([], output)
mod['func_4803'] = func_4803
mod = relay.transform.InferType()(mod)
mutated_mod['func_4803'] = func_4803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mutated_mod.get_global_var('func_4803')
call_4804 = func_4803_call()
output = call_4804
func_4805 = relay.Function([], output)
mutated_mod['func_4805'] = func_4805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3640_call = mod.get_global_var('func_3640')
func_3642_call = mutated_mod.get_global_var('func_3642')
call_4824 = func_3640_call()
call_4825 = func_3640_call()
uop_4853 = relay.log(call_4824.astype('float32')) # shape=(10, 1, 7)
uop_4855 = relay.log(call_4825.astype('float32')) # shape=(10, 1, 7)
func_4622_call = mod.get_global_var('func_4622')
func_4623_call = mutated_mod.get_global_var('func_4623')
call_4866 = relay.TupleGetItem(func_4622_call(), 0)
call_4867 = relay.TupleGetItem(func_4623_call(), 0)
output = relay.Tuple([uop_4853,call_4866,])
output2 = relay.Tuple([uop_4855,call_4867,])
func_4878 = relay.Function([], output)
mod['func_4878'] = func_4878
mod = relay.transform.InferType()(mod)
mutated_mod['func_4878'] = func_4878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4878_call = mutated_mod.get_global_var('func_4878')
call_4879 = func_4878_call()
output = call_4879
func_4880 = relay.Function([], output)
mutated_mod['func_4880'] = func_4880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3990_call = mod.get_global_var('func_3990')
func_3991_call = mutated_mod.get_global_var('func_3991')
call_4891 = relay.TupleGetItem(func_3990_call(), 1)
call_4892 = relay.TupleGetItem(func_3991_call(), 1)
uop_4933 = relay.sigmoid(call_4891.astype('float64')) # shape=(10, 1, 7)
uop_4935 = relay.sigmoid(call_4892.astype('float64')) # shape=(10, 1, 7)
bop_4936 = relay.not_equal(uop_4933.astype('bool'), relay.reshape(call_4891.astype('bool'), relay.shape_of(uop_4933))) # shape=(10, 1, 7)
bop_4939 = relay.not_equal(uop_4935.astype('bool'), relay.reshape(call_4892.astype('bool'), relay.shape_of(uop_4935))) # shape=(10, 1, 7)
func_3385_call = mod.get_global_var('func_3385')
func_3387_call = mutated_mod.get_global_var('func_3387')
call_4982 = relay.TupleGetItem(func_3385_call(), 0)
call_4983 = relay.TupleGetItem(func_3387_call(), 0)
func_4228_call = mod.get_global_var('func_4228')
func_4230_call = mutated_mod.get_global_var('func_4230')
var_4988 = relay.var("var_4988", dtype = "bool", shape = (5, 28))#candidate|4988|(5, 28)|var|bool
call_4987 = relay.TupleGetItem(func_4228_call(relay.reshape(var_4988.astype('bool'), [10, 2, 7])), 3)
call_4989 = relay.TupleGetItem(func_4230_call(relay.reshape(var_4988.astype('bool'), [10, 2, 7])), 3)
output = relay.Tuple([bop_4936,call_4982,call_4987,var_4988,])
output2 = relay.Tuple([bop_4939,call_4983,call_4989,var_4988,])
func_4991 = relay.Function([var_4988,], output)
mod['func_4991'] = func_4991
mod = relay.transform.InferType()(mod)
var_4992 = relay.var("var_4992", dtype = "bool", shape = (5, 28))#candidate|4992|(5, 28)|var|bool
output = func_4991(var_4992)
func_4993 = relay.Function([var_4992], output)
mutated_mod['func_4993'] = func_4993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_5027 = relay.TupleGetItem(func_2773_call(), 1)
call_5028 = relay.TupleGetItem(func_2775_call(), 1)
output = relay.Tuple([call_5027,])
output2 = relay.Tuple([call_5028,])
func_5044 = relay.Function([], output)
mod['func_5044'] = func_5044
mod = relay.transform.InferType()(mod)
output = func_5044()
func_5045 = relay.Function([], output)
mutated_mod['func_5045'] = func_5045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3761_call = mod.get_global_var('func_3761')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_5046 = relay.TupleGetItem(func_3761_call(), 0)
call_5047 = relay.TupleGetItem(func_3763_call(), 0)
output = call_5046
output2 = call_5047
func_5048 = relay.Function([], output)
mod['func_5048'] = func_5048
mod = relay.transform.InferType()(mod)
mutated_mod['func_5048'] = func_5048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5048_call = mutated_mod.get_global_var('func_5048')
call_5049 = func_5048_call()
output = call_5049
func_5050 = relay.Function([], output)
mutated_mod['func_5050'] = func_5050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5154 = relay.var("var_5154", dtype = "int8", shape = (14, 3, 4))#candidate|5154|(14, 3, 4)|var|int8
const_5155 = relay.const([[[4,-2,-2,-8],[6,-9,-9,10],[-10,-9,-5,-3]],[[-10,-1,-8,5],[-3,-8,9,-5],[-8,-7,-1,-8]],[[-8,-9,-9,-5],[5,-6,-1,8],[-7,10,-2,9]],[[9,9,-7,-2],[6,-5,-4,-4],[6,-6,10,-2]],[[10,-2,-7,2],[-1,8,2,2],[-3,-4,9,8]],[[5,-4,-7,1],[6,-2,6,-1],[-7,-4,10,6]],[[5,10,8,-1],[1,-10,-10,6],[6,-1,3,1]],[[4,10,3,9],[8,4,-9,-8],[8,7,-1,-6]],[[-2,-1,-2,7],[-10,-9,-3,-5],[-10,-4,3,7]],[[4,-1,-10,3],[-5,-9,9,-2],[10,-5,2,1]],[[-6,8,1,-1],[1,9,1,5],[8,-5,-7,7]],[[-8,10,2,-9],[10,-8,-5,5],[4,-9,-8,1]],[[6,3,2,-3],[-4,-8,8,-5],[-7,1,-3,-9]],[[-2,2,-3,-6],[-10,4,-10,-2],[-4,9,10,-4]]], dtype = "int8")#candidate|5155|(14, 3, 4)|const|int8
bop_5156 = relay.add(var_5154.astype('int8'), relay.reshape(const_5155.astype('int8'), relay.shape_of(var_5154))) # shape=(14, 3, 4)
var_5177 = relay.var("var_5177", dtype = "int8", shape = (14, 3, 4))#candidate|5177|(14, 3, 4)|var|int8
bop_5178 = relay.multiply(const_5155.astype('float32'), relay.reshape(var_5177.astype('float32'), relay.shape_of(const_5155))) # shape=(14, 3, 4)
func_3761_call = mod.get_global_var('func_3761')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_5189 = relay.TupleGetItem(func_3761_call(), 0)
call_5190 = relay.TupleGetItem(func_3763_call(), 0)
func_4744_call = mod.get_global_var('func_4744')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_5191 = func_4744_call()
call_5192 = func_4744_call()
func_3684_call = mod.get_global_var('func_3684')
func_3685_call = mutated_mod.get_global_var('func_3685')
call_5206 = func_3684_call()
call_5207 = func_3684_call()
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
var_5219 = relay.var("var_5219", dtype = "float32", shape = (2112,))#candidate|5219|(2112,)|var|float32
call_5218 = relay.TupleGetItem(func_4460_call(relay.reshape(var_5219.astype('float32'), [352, 6])), 0)
call_5220 = relay.TupleGetItem(func_4462_call(relay.reshape(var_5219.astype('float32'), [352, 6])), 0)
func_3017_call = mod.get_global_var('func_3017')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_5225 = func_3017_call()
call_5226 = func_3017_call()
output = relay.Tuple([bop_5156,bop_5178,call_5189,call_5191,call_5206,call_5218,var_5219,call_5225,])
output2 = relay.Tuple([bop_5156,bop_5178,call_5190,call_5192,call_5207,call_5220,var_5219,call_5226,])
func_5228 = relay.Function([var_5154,var_5177,var_5219,], output)
mod['func_5228'] = func_5228
mod = relay.transform.InferType()(mod)
var_5229 = relay.var("var_5229", dtype = "int8", shape = (14, 3, 4))#candidate|5229|(14, 3, 4)|var|int8
var_5230 = relay.var("var_5230", dtype = "int8", shape = (14, 3, 4))#candidate|5230|(14, 3, 4)|var|int8
var_5231 = relay.var("var_5231", dtype = "float32", shape = (2112,))#candidate|5231|(2112,)|var|float32
output = func_5228(var_5229,var_5230,var_5231,)
func_5232 = relay.Function([var_5229,var_5230,var_5231,], output)
mutated_mod['func_5232'] = func_5232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3498_call = mod.get_global_var('func_3498')
func_3500_call = mutated_mod.get_global_var('func_3500')
call_5236 = relay.TupleGetItem(func_3498_call(), 0)
call_5237 = relay.TupleGetItem(func_3500_call(), 0)
func_4878_call = mod.get_global_var('func_4878')
func_4880_call = mutated_mod.get_global_var('func_4880')
call_5255 = relay.TupleGetItem(func_4878_call(), 1)
call_5256 = relay.TupleGetItem(func_4880_call(), 1)
output = relay.Tuple([call_5236,call_5255,])
output2 = relay.Tuple([call_5237,call_5256,])
func_5263 = relay.Function([], output)
mod['func_5263'] = func_5263
mod = relay.transform.InferType()(mod)
mutated_mod['func_5263'] = func_5263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5263_call = mutated_mod.get_global_var('func_5263')
call_5264 = func_5263_call()
output = call_5264
func_5265 = relay.Function([], output)
mutated_mod['func_5265'] = func_5265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4622_call = mod.get_global_var('func_4622')
func_4623_call = mutated_mod.get_global_var('func_4623')
call_5266 = relay.TupleGetItem(func_4622_call(), 0)
call_5267 = relay.TupleGetItem(func_4623_call(), 0)
uop_5268 = relay.tan(call_5266.astype('float32')) # shape=(352, 5)
uop_5270 = relay.tan(call_5267.astype('float32')) # shape=(352, 5)
bop_5274 = relay.bitwise_xor(call_5266.astype('uint32'), relay.reshape(uop_5268.astype('uint32'), relay.shape_of(call_5266))) # shape=(352, 5)
bop_5277 = relay.bitwise_xor(call_5267.astype('uint32'), relay.reshape(uop_5270.astype('uint32'), relay.shape_of(call_5267))) # shape=(352, 5)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_5278 = relay.TupleGetItem(func_2773_call(), 1)
call_5279 = relay.TupleGetItem(func_2775_call(), 1)
uop_5280 = relay.acosh(call_5266.astype('float64')) # shape=(352, 5)
uop_5282 = relay.acosh(call_5267.astype('float64')) # shape=(352, 5)
uop_5286 = relay.cosh(bop_5274.astype('float64')) # shape=(352, 5)
uop_5288 = relay.cosh(bop_5277.astype('float64')) # shape=(352, 5)
bop_5300 = relay.logical_and(uop_5286.astype('bool'), relay.reshape(bop_5274.astype('bool'), relay.shape_of(uop_5286))) # shape=(352, 5)
bop_5303 = relay.logical_and(uop_5288.astype('bool'), relay.reshape(bop_5277.astype('bool'), relay.shape_of(uop_5288))) # shape=(352, 5)
bop_5320 = relay.logical_xor(call_5266.astype('int64'), relay.reshape(bop_5274.astype('int64'), relay.shape_of(call_5266))) # shape=(352, 5)
bop_5323 = relay.logical_xor(call_5267.astype('int64'), relay.reshape(bop_5277.astype('int64'), relay.shape_of(call_5267))) # shape=(352, 5)
func_4622_call = mod.get_global_var('func_4622')
func_4623_call = mutated_mod.get_global_var('func_4623')
call_5324 = relay.TupleGetItem(func_4622_call(), 0)
call_5325 = relay.TupleGetItem(func_4623_call(), 0)
func_5048_call = mod.get_global_var('func_5048')
func_5050_call = mutated_mod.get_global_var('func_5050')
call_5331 = func_5048_call()
call_5332 = func_5048_call()
uop_5336 = relay.atan(bop_5300.astype('float32')) # shape=(352, 5)
uop_5338 = relay.atan(bop_5303.astype('float32')) # shape=(352, 5)
output = relay.Tuple([call_5278,uop_5280,bop_5320,call_5324,call_5331,uop_5336,])
output2 = relay.Tuple([call_5279,uop_5282,bop_5323,call_5325,call_5332,uop_5338,])
func_5343 = relay.Function([], output)
mod['func_5343'] = func_5343
mod = relay.transform.InferType()(mod)
mutated_mod['func_5343'] = func_5343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mutated_mod.get_global_var('func_5343')
call_5344 = func_5343_call()
output = call_5344
func_5345 = relay.Function([], output)
mutated_mod['func_5345'] = func_5345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4622_call = mod.get_global_var('func_4622')
func_4623_call = mutated_mod.get_global_var('func_4623')
call_5422 = relay.TupleGetItem(func_4622_call(), 0)
call_5423 = relay.TupleGetItem(func_4623_call(), 0)
const_5424 = relay.const([[True,False,False,False,False],[False,True,True,True,False],[False,True,True,False,False],[False,False,False,False,False],[False,True,False,True,True],[False,True,True,True,False],[True,True,False,True,True],[True,True,False,False,True],[False,False,False,False,False],[True,False,True,True,False],[True,True,True,True,False],[True,True,True,False,True],[True,True,False,False,False],[True,True,False,True,True],[True,True,False,True,True],[False,False,True,True,False],[False,False,True,True,True],[False,False,True,True,False],[False,True,True,False,True],[False,True,False,False,False],[True,True,True,True,False],[True,False,True,False,True],[True,False,False,False,False],[True,False,False,False,False],[True,False,True,False,False],[False,False,True,False,False],[True,True,True,True,True],[False,False,True,True,False],[False,False,True,False,False],[True,False,True,True,False],[True,False,True,False,True],[True,False,True,True,False],[False,False,True,True,True],[False,True,True,True,False],[False,False,False,True,False],[True,False,False,False,True],[True,True,False,False,True],[True,True,True,False,False],[True,False,True,False,False],[False,True,True,False,False],[False,False,False,False,True],[True,True,True,True,True],[False,False,False,False,False],[True,True,False,False,False],[False,True,False,True,False],[False,False,True,False,False],[True,False,False,False,False],[True,True,False,False,False],[True,False,True,False,True],[True,True,False,True,False],[False,False,True,True,True],[True,True,True,False,True],[True,False,True,True,False],[False,False,True,False,False],[True,True,True,False,True],[False,False,True,False,True],[True,True,True,False,False],[True,False,True,False,False],[True,False,False,False,True],[False,False,False,True,False],[False,True,False,True,True],[True,True,True,False,False],[True,True,True,False,False],[True,True,False,False,False],[False,True,False,True,False],[True,True,False,True,True],[True,False,False,True,True],[True,False,True,True,True],[True,False,False,False,False],[False,True,False,False,True],[False,True,True,False,False],[True,True,True,True,True],[False,False,True,False,True],[False,False,False,True,True],[True,False,True,True,False],[True,False,True,True,False],[True,True,True,False,True],[True,True,True,True,False],[False,True,True,True,False],[False,True,False,False,True],[True,True,True,False,True],[False,True,True,True,True],[True,False,False,True,False],[False,False,True,True,True],[False,True,True,True,False],[True,True,True,True,False],[False,False,True,False,False],[False,False,True,True,True],[False,True,False,True,False],[False,True,False,False,False],[False,False,True,True,True],[True,False,False,False,True],[False,True,True,False,True],[True,False,True,False,False],[False,True,True,False,False],[True,True,True,True,True],[True,True,True,False,False],[False,True,False,False,True],[True,True,False,False,True],[True,True,True,False,False],[True,True,True,False,True],[True,True,False,False,True],[True,True,False,False,True],[True,False,False,True,True],[True,True,False,False,True],[True,True,True,False,False],[True,False,True,False,False],[False,True,False,True,True],[True,False,False,True,True],[True,False,True,True,False],[False,False,True,False,False],[False,True,False,True,False],[False,False,False,True,False],[False,True,True,False,False],[False,True,True,False,True],[False,True,True,True,False],[True,False,True,False,False],[True,True,False,True,False],[False,True,True,False,False],[True,False,False,True,True],[False,True,False,True,False],[True,True,True,True,True],[False,False,True,True,True],[True,False,False,True,False],[False,True,True,True,True],[False,True,False,False,False],[True,False,True,True,False],[True,True,True,True,False],[False,True,False,True,False],[True,True,False,True,False],[False,False,False,False,True],[True,False,False,True,False],[False,False,False,False,False],[False,True,True,False,False],[True,False,True,True,False],[True,True,True,False,False],[True,False,False,True,False],[False,True,False,False,False],[False,True,True,True,True],[True,True,False,False,True],[True,True,False,False,False],[False,False,True,True,False],[False,False,False,False,False],[True,False,True,True,True],[True,False,False,False,True],[True,True,False,True,True],[False,False,False,False,True],[True,False,True,False,True],[True,False,True,True,True],[True,False,True,False,False],[False,False,False,False,False],[True,True,False,True,True],[True,True,True,False,True],[False,True,True,True,True],[False,False,False,False,False],[True,True,False,False,False],[False,True,False,False,True],[False,True,True,False,True],[False,False,False,True,False],[False,False,True,True,True],[False,False,False,False,False],[False,True,True,False,False],[True,True,True,True,True],[False,False,True,True,False],[False,True,False,False,True],[False,False,True,True,False],[False,False,False,False,False],[False,False,False,True,True],[False,True,False,True,False],[True,True,False,False,True],[True,False,False,True,True],[True,False,True,False,True],[True,True,True,True,True],[False,True,False,False,True],[True,False,False,True,True],[False,False,False,True,True],[True,False,True,False,True],[False,True,True,False,False],[True,True,True,False,True],[False,False,False,False,False],[True,True,False,True,False],[True,False,True,False,True],[False,True,True,True,True],[False,False,True,False,False],[True,True,True,False,True],[False,False,False,True,True],[False,False,False,True,False],[True,False,False,False,False],[True,False,False,False,True],[True,False,True,False,False],[True,True,True,True,True],[True,True,False,True,False],[True,True,True,True,False],[True,False,True,True,False],[True,False,False,True,False],[False,True,False,True,True],[True,True,True,False,False],[False,True,True,False,False],[False,True,False,True,True],[False,False,True,True,True],[False,True,True,False,False],[True,False,True,True,False],[True,False,True,False,True],[True,False,False,False,True],[True,False,False,True,True],[True,True,True,True,True],[False,True,False,True,True],[False,False,False,False,False],[False,True,False,True,True],[True,False,True,False,False],[False,True,True,True,False],[False,False,True,False,True],[False,False,False,False,False],[False,True,False,False,True],[False,False,False,True,True],[True,False,True,False,False],[True,True,True,False,False],[True,True,False,True,True],[False,True,True,False,False],[True,False,True,False,False],[False,False,False,False,True],[True,True,False,False,True],[False,False,False,False,False],[False,True,True,True,False],[False,True,False,False,True],[False,True,False,True,True],[False,True,False,True,True],[True,False,False,True,True],[True,False,True,False,False],[True,False,True,True,True],[False,True,False,False,True],[False,False,True,False,True],[False,False,False,False,True],[True,False,False,True,True],[True,False,True,False,False],[True,True,True,True,False],[False,True,False,True,True],[True,True,True,False,True],[False,True,True,False,True],[True,True,True,True,False],[True,False,False,False,False],[True,False,True,False,True],[False,False,False,False,True],[True,True,False,False,False],[True,False,True,True,False],[False,False,True,False,True],[True,True,True,True,True],[True,False,True,False,False],[False,False,True,False,False],[False,True,False,True,True],[False,False,True,True,True],[True,True,True,False,True],[False,True,False,True,True],[False,False,True,True,True],[False,False,True,True,False],[False,True,False,False,False],[True,False,True,True,True],[False,False,False,False,True],[False,False,False,False,False],[True,False,False,True,False],[True,True,False,True,False],[False,True,True,False,True],[False,False,True,True,True],[False,True,True,False,True],[False,False,False,True,True],[False,False,True,False,True],[True,False,False,True,True],[False,False,False,False,False],[True,False,False,False,True],[True,False,False,True,False],[False,True,True,False,False],[False,False,True,True,False],[False,True,False,True,False],[True,True,False,True,True],[True,False,True,True,False],[False,True,False,True,False],[True,True,True,False,True],[False,False,True,True,True],[True,True,False,False,False],[True,True,False,True,True],[True,False,True,True,False],[False,True,True,False,False],[True,True,True,False,True],[False,False,True,True,True],[True,True,True,True,True],[True,False,False,True,False],[True,True,False,True,False],[False,True,True,True,True],[False,False,True,True,True],[False,False,True,False,True],[True,True,False,False,False],[True,True,True,False,True],[True,True,False,True,False],[False,False,True,True,True],[True,True,False,False,True],[True,False,True,False,False],[False,True,True,True,True],[False,False,True,True,False],[False,False,False,False,True],[False,False,True,False,True],[True,True,True,True,True],[False,False,True,True,False],[False,True,False,True,False],[True,True,True,False,False],[True,False,False,True,False],[False,False,False,True,False],[False,False,True,True,True],[False,True,True,True,False],[False,True,True,False,True],[False,True,False,True,False],[True,False,False,True,False],[True,True,False,True,True],[False,True,True,True,False],[True,True,True,False,False],[True,False,False,True,False],[True,True,False,True,False],[False,False,False,False,False],[False,True,True,False,True],[False,False,False,False,True],[True,True,False,False,True],[True,False,False,True,True],[False,False,False,False,True],[False,False,False,False,True],[False,True,False,True,True],[True,False,False,False,False],[True,True,True,False,True],[False,True,True,False,False],[False,True,False,False,True],[True,False,False,True,True],[True,True,False,True,True],[True,True,True,True,True],[True,True,False,False,True],[True,False,False,True,True],[False,True,False,False,False],[True,True,False,True,True],[True,False,False,True,False],[True,True,True,False,False],[False,True,True,False,True],[False,True,False,False,False],[True,False,False,True,False],[False,False,False,False,False],[True,False,False,True,True],[False,True,False,True,True],[True,True,True,False,True],[False,True,True,False,True],[True,True,False,True,False],[False,True,True,False,False],[True,True,False,True,True],[True,False,False,False,True],[True,True,True,False,True],[False,True,False,True,True],[False,True,True,False,False]], dtype = "bool")#candidate|5424|(352, 5)|const|bool
bop_5425 = relay.floor_divide(call_5422.astype('float64'), relay.reshape(const_5424.astype('float64'), relay.shape_of(call_5422))) # shape=(352, 5)
bop_5428 = relay.floor_divide(call_5423.astype('float64'), relay.reshape(const_5424.astype('float64'), relay.shape_of(call_5423))) # shape=(352, 5)
output = bop_5425
output2 = bop_5428
func_5433 = relay.Function([], output)
mod['func_5433'] = func_5433
mod = relay.transform.InferType()(mod)
mutated_mod['func_5433'] = func_5433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5433_call = mutated_mod.get_global_var('func_5433')
call_5434 = func_5433_call()
output = call_5434
func_5435 = relay.Function([], output)
mutated_mod['func_5435'] = func_5435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_5535 = func_4803_call()
call_5536 = func_4803_call()
output = relay.Tuple([call_5535,])
output2 = relay.Tuple([call_5536,])
func_5550 = relay.Function([], output)
mod['func_5550'] = func_5550
mod = relay.transform.InferType()(mod)
mutated_mod['func_5550'] = func_5550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5550_call = mutated_mod.get_global_var('func_5550')
call_5551 = func_5550_call()
output = call_5551
func_5552 = relay.Function([], output)
mutated_mod['func_5552'] = func_5552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3836_call = mod.get_global_var('func_3836')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_5583 = relay.TupleGetItem(func_3836_call(), 0)
call_5584 = relay.TupleGetItem(func_3838_call(), 0)
func_4622_call = mod.get_global_var('func_4622')
func_4623_call = mutated_mod.get_global_var('func_4623')
call_5590 = relay.TupleGetItem(func_4622_call(), 0)
call_5591 = relay.TupleGetItem(func_4623_call(), 0)
func_2892_call = mod.get_global_var('func_2892')
func_2895_call = mutated_mod.get_global_var('func_2895')
const_5597 = relay.const([[-8.409020,6.498715,4.713527,1.939971],[-4.072069,1.868914,6.059628,-8.677943],[-6.717705,-3.280749,4.661592,-2.497686],[-2.343120,-2.479407,-2.984952,-2.114429],[-8.527695,6.908860,9.129241,6.849901],[-5.210009,-3.375264,-3.451581,0.428710],[-6.313376,0.082318,-4.492137,2.603423],[1.356278,5.985773,-8.221265,-5.166540],[7.149841,-0.565624,-2.249153,-3.639786],[-7.009859,-2.656462,-4.304903,0.597977],[4.536594,-3.729360,-5.867907,-7.551017],[9.487435,-7.517672,9.824712,-5.153619],[-5.711105,3.377667,3.516903,9.468290],[7.986151,-2.430518,3.002808,-8.956945],[-3.004235,-3.540567,-1.797908,0.236548],[-4.011481,-0.851098,-6.234217,5.799602],[4.578294,-5.403207,-1.265962,1.997835],[2.992167,7.520298,6.578981,-7.961610],[-7.683544,0.055728,6.770532,-0.626885],[-8.857240,-9.937642,-1.743696,4.400183],[-7.849730,-6.088144,6.052410,-7.987885],[1.479824,5.048703,7.502914,-8.913747],[-4.476295,5.559675,-3.598911,6.621901],[-4.027783,-1.646970,6.843048,-7.341737],[4.196817,3.615238,-2.087790,8.763666],[4.994472,5.688649,-8.282674,6.378777],[6.199417,4.244351,-2.508013,-0.566660],[-5.594884,3.920641,-6.240625,2.618251],[-2.050688,-0.279561,8.395064,-7.963923],[-0.336739,4.261344,-2.707013,5.551952],[1.102314,1.784424,3.224622,-2.687363],[-8.236272,-0.531493,-5.286678,-7.909455],[-5.568009,9.632402,2.131190,-5.136082],[2.440492,-2.950849,-1.814959,1.209493],[-5.232338,-9.476165,-9.603969,9.750637],[-6.063094,5.885242,-1.905422,-6.929923],[-0.299613,-2.570197,1.660119,0.754915],[-0.219898,-5.418682,2.570106,1.325795],[7.578970,-3.437515,-7.931108,-5.159174],[5.193880,5.194286,-4.590584,-4.431557],[-1.018950,-3.868013,5.981630,-5.577062],[1.096333,8.607326,5.584675,9.530091],[-8.962912,-5.291376,4.881998,1.266726],[0.964205,-9.467888,-7.212356,-5.185246],[4.034788,5.345496,8.766412,9.837504],[-3.990181,9.965294,3.395289,-8.630777],[-1.188991,-2.295713,-2.551363,-2.289282],[2.919948,4.962519,1.756945,-4.870206],[-0.177118,-0.786862,6.860195,-2.637451],[-2.864303,2.303332,-7.499084,4.751085],[7.858383,4.722743,3.707983,4.166409],[-4.886960,5.354227,-9.413306,2.746505],[2.445875,-2.080138,7.917552,-8.497434],[1.469146,5.297549,-9.033323,-3.915932],[-8.897547,0.658351,-2.977443,-3.430527],[3.696933,-8.635832,3.320942,-4.349347],[7.592942,-4.858430,0.560650,-7.768757],[-3.813350,9.361481,-2.764407,-4.380052],[3.765723,2.678041,-4.161214,-1.334544],[1.350588,-4.190568,-5.215006,2.667012],[0.863132,-1.645006,-8.690216,7.186208],[-8.333114,2.529936,3.089100,-6.163446],[3.823149,-0.433689,2.258570,0.042089],[0.719081,-9.702792,-0.881102,-9.691156],[1.203921,4.109089,2.863324,-2.679084],[7.600656,0.562672,-7.940255,2.813894],[2.828197,0.315025,-7.553725,1.110125],[-8.417087,-6.992726,1.608910,0.250013],[0.816977,-2.114705,3.849376,5.831445],[0.572121,4.030003,-9.363971,5.311629],[-4.780551,-9.218897,-8.116137,7.896024],[8.118779,4.702826,-5.938449,3.668414],[5.805433,-8.522821,4.699730,9.460745],[-6.975845,-7.574472,6.762723,-4.373843],[-8.438795,0.118853,-0.107063,-6.835904],[-9.420314,-4.576398,-0.757782,-6.669972],[-6.307980,-9.905006,-4.990886,-0.032229],[8.938192,6.661008,-8.223405,-3.886958],[1.085992,5.876408,-4.024126,9.055692],[-0.520160,6.955903,-4.792668,-2.870095],[7.132849,-7.643376,0.448468,-8.704759],[3.291098,6.148925,-9.826914,-6.196632],[5.890578,6.160017,9.946029,-5.673895],[7.381268,-1.389117,-7.187307,-7.948345],[-4.781703,2.551810,4.458134,-0.682561],[-1.622822,-9.030725,3.911361,-0.041933],[0.300238,6.654316,-7.787852,-5.148170],[3.357753,4.521335,9.161555,4.338068],[-9.844897,1.978583,5.781546,-1.377206],[-4.490034,-7.643329,-7.796593,-3.905355],[-7.836570,-5.773369,-8.756503,-7.027851],[-7.149182,5.647208,0.279187,8.131908],[7.128135,3.263349,-6.323680,-2.720427],[3.685351,-2.299118,6.954442,8.105105],[-0.120932,6.072588,-3.610703,2.182726],[0.137129,-6.691521,3.063508,7.401199],[4.376084,9.533414,-6.409532,-2.170550],[-4.658743,3.433674,9.165414,-0.562720],[4.778018,-2.422335,6.460942,-4.580606],[-9.842233,-2.165749,-9.239178,6.206155],[-0.612762,0.070380,-5.348618,-0.700332],[-1.031769,5.143414,-2.240136,-4.234359],[6.345938,8.100553,-3.803990,2.834959],[1.197476,-1.643242,6.240572,0.529383],[2.945064,0.422749,-8.099317,-3.061440],[1.965968,-2.397991,7.840831,6.169113],[-6.873773,-9.098623,-0.535584,6.875676],[0.793563,7.384954,2.064893,-5.130047],[2.894764,8.130588,-6.122186,4.505039],[5.086067,6.176151,-6.615695,4.890377],[-1.265404,6.508764,2.554735,-7.302961],[-4.409025,-8.741565,-7.248310,-8.711624],[-2.624676,9.922029,-6.742024,-5.390751],[-1.505656,-8.211272,9.718862,8.999468],[1.602701,-7.548160,-9.966349,1.931124],[0.787312,-1.232211,7.160572,5.218975],[-6.827872,-0.437153,6.592938,-0.646149],[-0.233478,-5.174272,-6.038068,5.360557],[-5.212138,6.036312,-6.900625,-2.590850],[-6.044009,7.222241,5.216418,1.116922],[9.198394,-2.754572,-6.867399,9.198185],[-2.468677,-4.694508,1.782036,-5.495836],[-6.029946,-6.005828,7.471400,-5.958890],[-5.971800,1.999912,-0.576938,8.198356],[-1.627862,0.763293,7.115150,0.073272],[-1.350899,-1.491532,-2.855829,-8.135249],[-6.064636,4.657254,4.454885,1.928801],[-4.174725,2.686018,6.272969,-9.731855],[0.747662,5.344929,-8.737976,-5.452548],[-7.012095,3.731029,9.455776,4.524388],[-3.834914,1.379410,-5.952299,3.192681],[5.314978,-8.081740,-9.974186,-2.836511],[-7.872635,-9.254536,3.470196,5.915961],[3.779863,-5.752744,-8.008638,0.205030],[-1.858461,-5.684417,4.370040,3.908039],[6.300664,-5.590362,8.458125,9.010423],[-4.016394,-1.216090,-0.023518,3.428158],[-6.770250,-3.258729,-7.872252,-7.861435],[7.478489,6.828323,-2.330336,0.526450],[-8.353472,0.052420,8.887229,4.097243],[-3.076909,8.691985,-5.368750,2.459033],[-8.091355,5.749531,2.088772,6.939713],[1.605173,6.991479,-3.444565,9.170214],[-3.362547,-4.561217,6.522548,6.014202],[5.480552,-7.981024,-8.407584,3.428037],[2.629090,4.105101,-9.411974,2.019683],[0.921436,0.207357,-4.863075,1.134849],[-4.006154,-5.006059,6.718606,1.084772],[-6.387950,-2.792921,2.508910,4.148341],[7.070183,3.907062,1.865835,8.381754],[-0.211851,-3.185795,6.263070,6.020023],[9.298428,1.291915,-8.253871,-5.902053],[-9.157132,4.066253,-7.229356,-0.768755],[5.246561,5.924518,3.491644,3.535314],[5.775785,-9.247536,8.076924,-0.131924],[0.345029,-9.390274,4.925173,-6.592976],[8.726663,2.693799,-7.845706,9.856691],[-9.272967,-9.600845,9.582270,6.000491],[-4.476164,7.484279,2.949286,-4.665907],[7.228067,-2.567951,0.657414,-0.193062],[-5.399254,-8.616366,-4.853212,-0.852231],[-3.007013,-0.233262,9.977878,5.043236],[9.523547,2.139395,-3.513776,6.524424],[-1.840542,-5.598439,-7.009379,5.965091],[1.231258,5.275421,5.700222,-6.543518],[-6.919779,-6.355901,-1.224912,4.518958],[-1.104370,-7.202670,3.123044,6.413195],[-4.636423,3.635181,-2.903031,3.859807],[7.464835,5.002031,3.686752,-9.097204],[-3.171980,6.515077,-4.595879,-4.256446],[3.938281,-2.255764,-5.082547,6.788014],[5.602639,0.903105,9.812787,6.592576],[9.489591,0.837957,-8.179273,8.823831],[-7.194843,9.824644,2.784881,-8.387859],[2.997621,7.288285,-3.406463,-3.400393],[-7.523857,6.035740,-9.313946,-7.351732],[-1.170296,-8.975056,2.968616,9.338582],[-2.357510,8.926547,4.682832,7.632422],[-8.378831,-3.365392,8.050814,-9.064031],[6.474097,7.727081,5.062184,8.222305],[5.246392,-0.291823,7.121553,2.211987],[1.300776,-6.416388,-8.611066,6.251757],[-4.211503,5.790869,-2.779103,7.451834],[1.157749,9.017430,-4.283441,-8.267650],[6.337028,3.211056,0.641609,-9.385617],[5.562054,8.299632,-7.673846,-4.917014],[-4.082280,-6.212815,6.767402,-6.649813],[-2.666497,9.673815,4.818452,3.377978],[5.928042,2.681365,8.657711,0.983819],[-4.284664,-7.047910,7.774854,-2.049401],[-6.187762,-1.357697,-9.898145,-8.373360],[-4.818195,-2.163481,-6.840990,-7.275382],[-6.297246,-6.317540,-1.987619,-6.357837],[-9.041644,7.990767,7.159300,2.389905],[3.508175,8.767558,6.284828,-5.648834],[-8.819447,4.569373,-8.759699,-4.074881],[2.236602,-2.844865,-8.850667,8.313063],[0.549887,-5.574477,-8.666094,-9.943091],[9.112536,1.409224,-6.252223,-2.280020],[-6.568434,3.846777,-1.752798,7.431201],[-4.348876,3.220680,-0.643714,0.219130],[1.401236,-9.808144,3.471015,6.826570],[7.755284,2.574177,1.374193,-3.142114],[2.553172,-2.421315,5.710426,-2.851112],[-7.775286,-3.340791,-4.302250,-7.198033],[3.225939,7.039339,-4.682649,4.106969],[8.737357,7.168721,-1.092652,5.713571],[6.821346,1.725240,1.961382,-6.050737],[9.931390,3.324266,-7.719005,-8.068072],[-6.031210,-9.028326,-6.215537,-8.593379],[6.692158,-4.093022,5.743408,7.407125],[-1.631576,7.175258,-0.415280,6.842339],[-9.318651,3.256948,-6.410721,-3.308980],[9.850836,3.088881,-7.959892,-3.910386],[2.430827,-7.434362,-4.206408,4.575376],[-3.360206,-8.912475,-6.904111,8.909784],[-9.537352,1.324246,-9.310849,-6.969062],[8.451817,3.840235,6.643208,4.135669],[8.622988,-7.065096,1.408498,-3.280822],[-4.082961,3.495134,-9.559772,-8.799731],[1.313691,0.149823,0.414457,-8.529232],[-9.156097,0.547538,3.947490,-8.776881],[-9.040315,-7.367264,5.716656,0.253798],[1.452878,-1.502944,7.278097,4.146811],[8.615594,-3.540984,-0.849022,7.743092],[5.077099,-8.110649,3.166159,2.332212],[3.146996,6.690167,-8.642010,7.463102],[2.470564,6.454174,-4.306390,-1.056261],[0.610605,-9.749575,0.634890,-4.651486],[-3.633536,3.978918,-5.145954,2.699960],[-6.956670,-1.783523,-9.446852,-9.947825],[9.476726,-9.302508,-5.102766,7.548228],[-1.645114,2.691385,9.305191,-9.838404],[3.693793,7.208991,-2.426442,1.601001],[-6.978574,7.745331,2.776851,-5.396247],[4.128733,-8.017816,5.541191,2.602248],[-6.409052,9.065105,4.262010,7.306500],[5.251027,-0.461244,-0.947344,-1.515560],[5.165641,4.963115,-7.526107,1.131254],[-3.428723,1.452801,-8.653359,9.651309],[-0.986908,-6.587809,-5.880541,-5.412841],[4.111930,1.197803,-7.101576,-3.883683],[7.851753,2.772209,5.488891,7.299539],[-7.072687,-4.473360,-2.721577,6.440616],[-4.452301,-6.339143,-7.088922,1.793870],[2.351245,8.461641,-1.448340,1.494504],[5.529672,2.930603,7.461647,-4.857568],[-1.110394,-0.149110,1.987485,9.711914],[-7.225803,-1.757366,-2.492270,-9.325902],[1.825399,2.203598,8.742993,7.230364],[4.220155,6.726026,-4.231684,1.591277],[-2.027230,7.069635,9.237496,-8.933361],[-1.233525,-0.860534,-7.699316,-9.684166],[-4.031928,1.681457,-8.858608,-1.709254],[-9.605766,-9.769974,-8.649178,7.860286],[-2.315734,-0.707045,4.582730,1.555369],[8.517214,-8.144274,-0.585912,0.937068],[-3.315234,-7.506395,-2.565151,5.526476],[-7.917029,5.439218,5.454155,-6.344702],[1.467788,2.457161,2.959052,-3.369796],[9.865731,-5.910754,2.968777,-9.355163],[-6.306198,-4.140829,-6.138630,5.115963],[6.292241,2.331332,7.330824,-6.281206],[-1.942433,8.558366,-8.731592,-1.868629],[-4.102971,2.160407,8.454515,-8.002891],[-7.783381,-1.022344,-5.084470,-7.560168],[-2.595844,-7.444067,6.058650,-2.737892],[-2.057215,9.004980,5.302544,-5.506138],[-3.206522,0.534076,-7.223190,7.335128],[-5.425824,5.492378,-2.818918,-7.624474],[2.339762,-3.638974,-0.049442,-8.859048],[0.543330,5.567771,4.231537,-0.262402],[-5.598240,2.258595,4.787516,7.209804],[-2.339776,-2.479550,-8.403277,1.069213],[7.252535,-4.291093,-6.819328,4.454294],[-2.746008,-5.762034,-8.505124,0.494846],[-9.479153,9.546697,-1.027696,8.672270],[5.247776,0.806368,0.769735,2.813518],[-3.252787,-8.867728,-1.657939,-9.883821],[-1.255808,4.517793,-1.204425,6.644070],[8.676146,-3.737443,-0.540979,1.253175],[-9.684183,6.849682,0.875521,-1.197546],[1.147738,8.991931,-5.155714,-1.496945],[-3.070182,-0.472326,9.464848,-6.485606],[-2.702348,-2.062483,-2.349096,8.008963],[-4.857520,-9.261777,3.091801,1.478853],[0.487744,5.843870,6.031952,0.037786],[8.345001,-2.150870,5.856169,7.546307]], dtype = "float64")#candidate|5597|(288, 4)|const|float64
call_5596 = relay.TupleGetItem(func_2892_call(relay.reshape(const_5597.astype('float64'), [1152,])), 0)
call_5598 = relay.TupleGetItem(func_2895_call(relay.reshape(const_5597.astype('float64'), [1152,])), 0)
func_5550_call = mod.get_global_var('func_5550')
func_5552_call = mutated_mod.get_global_var('func_5552')
call_5606 = relay.TupleGetItem(func_5550_call(), 0)
call_5607 = relay.TupleGetItem(func_5552_call(), 0)
func_5433_call = mod.get_global_var('func_5433')
func_5435_call = mutated_mod.get_global_var('func_5435')
call_5615 = func_5433_call()
call_5616 = func_5433_call()
func_3917_call = mod.get_global_var('func_3917')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_5643 = relay.TupleGetItem(func_3917_call(relay.reshape(call_5606.astype('bool'), [10, 1, 7])), 0)
call_5644 = relay.TupleGetItem(func_3920_call(relay.reshape(call_5606.astype('bool'), [10, 1, 7])), 0)
func_5433_call = mod.get_global_var('func_5433')
func_5435_call = mutated_mod.get_global_var('func_5435')
call_5649 = func_5433_call()
call_5650 = func_5433_call()
output = relay.Tuple([call_5583,call_5590,call_5596,const_5597,call_5606,call_5615,call_5643,call_5649,])
output2 = relay.Tuple([call_5584,call_5591,call_5598,const_5597,call_5607,call_5616,call_5644,call_5650,])
func_5652 = relay.Function([], output)
mod['func_5652'] = func_5652
mod = relay.transform.InferType()(mod)
output = func_5652()
func_5653 = relay.Function([], output)
mutated_mod['func_5653'] = func_5653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mod.get_global_var('func_2848')
func_2849_call = mutated_mod.get_global_var('func_2849')
call_5672 = relay.TupleGetItem(func_2848_call(), 1)
call_5673 = relay.TupleGetItem(func_2849_call(), 1)
output = call_5672
output2 = call_5673
func_5679 = relay.Function([], output)
mod['func_5679'] = func_5679
mod = relay.transform.InferType()(mod)
output = func_5679()
func_5680 = relay.Function([], output)
mutated_mod['func_5680'] = func_5680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3836_call = mod.get_global_var('func_3836')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_5688 = relay.TupleGetItem(func_3836_call(), 0)
call_5689 = relay.TupleGetItem(func_3838_call(), 0)
func_3640_call = mod.get_global_var('func_3640')
func_3642_call = mutated_mod.get_global_var('func_3642')
call_5717 = func_3640_call()
call_5718 = func_3640_call()
bop_5724 = relay.maximum(call_5688.astype('int16'), relay.reshape(call_5717.astype('int16'), relay.shape_of(call_5688))) # shape=(10, 1, 7)
bop_5727 = relay.maximum(call_5689.astype('int16'), relay.reshape(call_5718.astype('int16'), relay.shape_of(call_5689))) # shape=(10, 1, 7)
output = bop_5724
output2 = bop_5727
func_5743 = relay.Function([], output)
mod['func_5743'] = func_5743
mod = relay.transform.InferType()(mod)
output = func_5743()
func_5744 = relay.Function([], output)
mutated_mod['func_5744'] = func_5744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5679_call = mod.get_global_var('func_5679')
func_5680_call = mutated_mod.get_global_var('func_5680')
call_5841 = func_5679_call()
call_5842 = func_5679_call()
func_4744_call = mod.get_global_var('func_4744')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_5860 = func_4744_call()
call_5861 = func_4744_call()
output = relay.Tuple([call_5841,call_5860,])
output2 = relay.Tuple([call_5842,call_5861,])
func_5863 = relay.Function([], output)
mod['func_5863'] = func_5863
mod = relay.transform.InferType()(mod)
mutated_mod['func_5863'] = func_5863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5863_call = mutated_mod.get_global_var('func_5863')
call_5864 = func_5863_call()
output = call_5864
func_5865 = relay.Function([], output)
mutated_mod['func_5865'] = func_5865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_5911 = func_4803_call()
call_5912 = func_4803_call()
output = call_5911
output2 = call_5912
func_5926 = relay.Function([], output)
mod['func_5926'] = func_5926
mod = relay.transform.InferType()(mod)
output = func_5926()
func_5927 = relay.Function([], output)
mutated_mod['func_5927'] = func_5927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_5946 = func_4803_call()
call_5947 = func_4803_call()
output = relay.Tuple([call_5946,])
output2 = relay.Tuple([call_5947,])
func_5948 = relay.Function([], output)
mod['func_5948'] = func_5948
mod = relay.transform.InferType()(mod)
output = func_5948()
func_5949 = relay.Function([], output)
mutated_mod['func_5949'] = func_5949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5652_call = mod.get_global_var('func_5652')
func_5653_call = mutated_mod.get_global_var('func_5653')
call_5973 = relay.TupleGetItem(func_5652_call(), 7)
call_5974 = relay.TupleGetItem(func_5653_call(), 7)
func_3228_call = mod.get_global_var('func_3228')
func_3230_call = mutated_mod.get_global_var('func_3230')
call_5975 = func_3228_call()
call_5976 = func_3228_call()
output = relay.Tuple([call_5973,call_5975,])
output2 = relay.Tuple([call_5974,call_5976,])
func_5980 = relay.Function([], output)
mod['func_5980'] = func_5980
mod = relay.transform.InferType()(mod)
output = func_5980()
func_5981 = relay.Function([], output)
mutated_mod['func_5981'] = func_5981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5652_call = mod.get_global_var('func_5652')
func_5653_call = mutated_mod.get_global_var('func_5653')
call_6003 = relay.TupleGetItem(func_5652_call(), 0)
call_6004 = relay.TupleGetItem(func_5653_call(), 0)
output = relay.Tuple([call_6003,])
output2 = relay.Tuple([call_6004,])
func_6007 = relay.Function([], output)
mod['func_6007'] = func_6007
mod = relay.transform.InferType()(mod)
output = func_6007()
func_6008 = relay.Function([], output)
mutated_mod['func_6008'] = func_6008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3990_call = mod.get_global_var('func_3990')
func_3991_call = mutated_mod.get_global_var('func_3991')
call_6026 = relay.TupleGetItem(func_3990_call(), 1)
call_6027 = relay.TupleGetItem(func_3991_call(), 1)
output = call_6026
output2 = call_6027
func_6071 = relay.Function([], output)
mod['func_6071'] = func_6071
mod = relay.transform.InferType()(mod)
output = func_6071()
func_6072 = relay.Function([], output)
mutated_mod['func_6072'] = func_6072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3017_call = mod.get_global_var('func_3017')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_6107 = func_3017_call()
call_6108 = func_3017_call()
func_2892_call = mod.get_global_var('func_2892')
func_2895_call = mutated_mod.get_global_var('func_2895')
const_6122 = relay.const([7.542092,7.354874,-0.874411,-0.086675,0.347753,1.338498,-1.013740,-1.610016,7.868710,-7.822166,-3.930346,2.078647,-7.713407,3.574169,0.213523,8.823401,7.305256,0.303260,4.405305,7.491149,-5.188591,7.559109,-5.358450,-7.340813,-8.767603,-5.471064,-6.005111,-5.099146,-8.092789,-1.580736,-2.657452,7.871574,9.500497,9.285541,-7.607861,6.014817,0.865128,3.101707,6.610361,-7.826162,-7.871032,-0.086228,-0.652642,0.260604,6.711277,3.817304,-7.232464,8.817973,2.462231,-0.083510,0.124866,-6.194116,-5.490338,-7.182579,4.770203,2.771940,-5.697635,1.637688,1.904007,6.792939,-0.773926,-1.632906,4.399451,-4.888892,5.018423,3.516646,7.297653,1.703267,1.026085,8.318742,-2.436682,5.564015,-6.104683,-8.169620,2.492947,-7.096189,-2.338944,-8.876919,-0.473738,-1.431492,3.544342,-7.796067,8.396315,-5.006906,-3.876458,-9.047290,8.212937,9.041670,-2.847482,9.421431,1.673115,0.666308,-7.501444,-2.225885,9.585418,-7.050560,-8.185471,7.048442,8.314249,-9.762287,6.198793,-1.349878,-3.028226,-5.535873,5.961255,3.172868,-6.343927,-1.966170,-2.368585,2.722624,0.100166,9.653918,6.336010,-9.996032,-6.053643,-6.407363,8.511588,-7.267905,-9.840452,-5.315821,-6.397135,-2.613681,-8.448128,-2.994513,9.489309,-2.206811,0.438878,-2.805622,-3.166773,9.097633,-4.171207,-2.569822,1.744988,4.980495,-2.027257,9.212656,6.246978,0.387569,5.948253,5.967778,5.987944,7.528973,5.119927,6.985058,-7.990921,-1.093394,-2.495548,-2.062124,-8.611409,3.257221,9.821597,4.418904,9.426737,5.865338,-8.202602,7.320824,-9.034624,2.081651,4.105795,-7.175799,7.840180,-4.128688,5.363189,5.655617,-4.030592,-1.477912,-3.248990,7.536364,-1.979210,-3.846792,6.381973,4.942354,-2.396308,4.632945,2.893061,-7.671485,-8.761961,5.988811,9.574957,9.432591,3.159413,-4.767831,-1.716037,5.201756,-3.164795,4.167646,-2.164213,1.564108,6.180895,-0.290038,-9.993534,-0.061604,3.325922,7.423706,-4.966109,-7.423795,-8.849539,1.039177,-1.878332,-8.251659,-0.551746,-7.913043,-7.999076,-1.954947,-2.110851,-8.566592,6.469136,-1.192762,-6.089765,8.773045,-2.183961,7.107175,-5.262740,4.543048,1.669364,8.900360,-1.848835,-6.904657,-6.195200,-3.991197,0.049496,0.212992,1.437523,6.230334,8.299230,1.531817,1.192202,9.880044,1.648232,-4.314433,-1.938752,8.299848,-5.416853,3.356083,-9.037335,0.214773,-3.660586,-0.124638,-5.721299,-2.101294,-8.959559,-9.259693,-2.994907,-6.032166,-3.886266,-1.509098,-7.268773,9.622085,-3.469503,6.223217,1.526304,-4.543793,-1.008288,2.665059,0.678161,-6.612982,5.833006,2.683252,-2.552534,-6.137969,-3.580013,2.368196,-3.592581,4.796369,9.620645,7.106590,-5.367186,7.631866,-2.898002,2.460279,-0.688544,2.155552,-9.594499,1.940151,-5.349377,-6.497599,-7.466015,-7.956186,-6.149162,5.927974,-0.756590,-3.731851,4.402515,0.526289,5.715193,6.655113,4.452061,6.841402,5.499919,-2.860841,-9.228776,-4.100199,4.796849,1.606572,5.650780,3.609706,7.358492,-3.218294,5.065081,-3.558519,-4.348041,-2.200662,2.982816,-8.534923,-6.840338,-2.935025,6.551645,-0.515130,3.429814,-6.353857,-9.715960,1.422327,-1.039213,-7.660234,2.901026,-4.180017,-6.139017,4.310010,-8.090750,-1.161277,2.467411,-1.721153,-7.357979,9.974335,-9.404943,-2.015998,2.703725,1.234770,8.120843,-1.079305,-3.182122,-5.774459,9.357971,-5.946526,1.386701,9.546632,-6.013209,0.671921,-7.056826,-0.495529,3.708282,9.792709,-5.770065,-2.940802,0.368359,5.608266,8.032564,-5.186274,4.014776,-9.451010,-3.017259,5.314514,9.467815,3.361816,6.482183,5.279892,-5.873158,-7.647229,9.903007,-5.873489,9.223160,-4.002245,7.214669,4.442950,-9.253923,-8.145083,9.985099,3.500216,-8.888309,-4.835537,-2.240528,-3.866444,6.582250,-4.538753,0.192884,9.456561,-4.825611,8.898542,-1.440789,-2.605594,9.570477,5.646661,9.932581,2.840484,7.425984,5.465811,2.888832,-6.612399,-0.937100,3.248113,4.899031,-7.577461,8.770488,-7.747613,7.318555,-2.742012,7.837059,3.315354,-5.405787,-2.159533,5.551734,8.391092,-2.570128,1.568678,-9.841274,-8.662048,3.901488,0.645073,5.513179,-1.139842,1.597480,9.999676,7.652948,0.333361,4.988932,5.364386,4.732179,-3.626406,4.864193,8.376148,-7.745002,6.395954,-7.515894,-6.309314,-3.787448,-4.413507,8.428577,-6.978115,4.418219,-1.696500,-3.194381,2.597747,1.717557,3.886971,6.285296,-5.102963,-0.603771,5.687191,7.431854,-0.160688,-3.187812,3.031874,-4.235969,-3.140052,8.459669,3.458989,2.815835,6.135836,-3.097322,0.910929,2.465521,6.340699,4.428875,3.428510,8.143583,6.228517,-4.217575,0.635151,-2.227714,-0.643434,2.196630,5.743510,-8.683058,6.839536,4.413370,-8.894052,-5.942433,3.599090,-5.620507,-8.643035,-2.060230,-0.573136,-1.636396,-2.235947,1.365026,-5.572268,-4.228497,0.981397,1.279729,3.739750,6.873383,7.369178,3.559971,-2.438602,6.521938,8.515577,-1.032256,2.723864,-0.507856,2.140503,-7.350388,-4.291953,-8.759677,-0.241329,-7.562843,-1.025831,1.235080,0.179848,-0.010163,5.720281,5.528858,-7.992909,-0.331992,-8.154721,9.748077,-3.777253,-4.630436,-9.312553,7.841097,-6.971865,-7.683023,1.727001,-7.199479,-0.443263,-3.389460,9.576365,5.893049,2.064302,1.507518,-7.040619,-1.543232,-5.796223,6.004718,1.844575,0.444746,-1.724484,-5.169653,-0.973858,-4.660387,-8.574073,-8.030236,-4.158137,7.200420,4.211872,-7.581076,0.368468,-0.376885,2.129095,-8.759419,-3.215618,-2.862861,8.254643,4.508265,8.452872,-7.260214,-7.632597,1.894553,-6.911675,0.838649,6.487164,4.206742,-6.731183,8.892088,3.894438,-2.758829,0.103041,-5.631811,5.950962,-2.079648,-2.548190,-9.791669,9.968890,4.991595,-3.262262,7.361217,-1.688099,-4.359034,0.527911,-3.716349,9.988117,-7.360383,6.891990,9.370827,-0.201488,-3.137128,9.682559,-2.993600,-8.852517,-7.534852,-3.593623,1.933569,3.612035,9.073675,7.460662,7.673482,-8.002409,0.423138,8.075057,-6.936659,7.536160,-1.047169,-3.092504,1.146232,-5.091385,5.757387,-3.544718,-3.425073,5.433034,-8.076558,4.797934,9.961982,1.073183,-3.408142,-3.063864,2.254724,9.509865,-1.934379,-1.436974,-0.188328,9.312058,6.576332,-2.380163,3.608643,6.920393,-7.272948,-0.848630,-1.114908,6.178003,-6.981703,1.674902,9.198933,6.529412,-7.086238,8.128111,-8.039462,9.267972,-7.307273,3.215231,6.611605,8.244494,-7.312824,4.093151,-9.589823,7.747029,-5.733269,-0.540480,1.373261,7.137536,9.033317,-6.979805,-7.936888,1.391064,-9.042311,-9.473627,3.232374,9.534474,0.497927,-8.368704,5.803566,-1.888223,-6.218958,5.260472,-4.091813,-8.044254,-9.994783,-9.735938,-1.957940,1.301643,-6.192715,-6.901778,-6.883455,9.566284,-7.876804,0.136749,7.057689,-2.725874,-4.093178,8.055024,-1.329292,-8.695019,5.781889,8.572615,-2.237675,-6.425575,6.198511,-9.415029,-7.028720,7.299710,4.505196,7.896818,7.192611,-1.406596,4.423214,-4.047083,8.682249,-2.499838,3.881313,-3.954092,6.339446,8.359091,6.232209,-0.404541,8.085252,8.422716,-1.548550,-5.426325,-1.778185,2.518543,-2.057030,1.026658,-4.446961,-3.870530,-1.165827,8.705458,0.965281,-8.098381,-8.333422,9.387396,-2.730171,-9.422992,2.216376,-9.569079,4.018951,3.563572,-6.483229,-8.804254,5.787756,-6.189449,2.134518,6.818917,-8.389508,-3.718909,-7.872138,0.711620,-7.223454,4.766262,-1.827472,0.873016,9.357552,4.723752,2.056817,-6.457475,9.872562,-5.421706,-0.180862,2.122993,0.632305,6.440073,1.129027,6.469591,-5.902700,4.109392,-3.049384,-8.108326,-3.988409,6.180032,6.994937,-9.333964,9.408070,-5.831130,-8.284669,-5.220047,9.396310,7.030942,-3.647604,-1.820200,5.062603,0.797236,-3.804767,4.451748,-1.188655,-7.727926,-8.063504,-5.579086,-1.339323,9.894398,-5.741177,-6.118437,6.080144,4.810332,-1.338338,-3.274277,5.745422,-0.934521,1.651131,-3.068338,-0.148738,-7.233372,1.463089,-4.861483,2.941938,-5.403737,-5.477585,8.704533,-3.591465,7.493902,-9.979376,-2.937813,-4.559248,2.076430,-1.940196,8.112623,-4.952865,1.956178,-3.067513,0.090927,3.064027,9.159706,9.684709,4.359723,6.798821,-7.070822,-8.211941,-2.993216,4.683700,3.667828,5.584585,0.466033,-5.486274,-8.948708,-0.132587,-9.231625,0.467016,8.026847,-7.258605,8.069657,-7.222499,3.958636,-6.013548,7.981421,2.958594,-6.510016,3.926884,-6.300468,-6.959550,-4.294365,9.772166,0.949749,-0.808443,6.034143,4.367175,1.095402,-7.509847,0.661941,-3.942058,2.480549,2.278148,-3.946495,0.979114,-2.271965,0.520432,-2.889468,6.241723,-6.978185,9.761062,-9.977194,-5.573747,-2.813988,-8.058780,6.688405,-1.818594,-8.649454,-9.755598,-1.502061,6.709753,-2.834344,7.589996,2.922417,-4.381636,-6.514859,1.955989,-9.702445,-6.322550,8.089348,-9.934194,3.010744,9.026500,-3.488090,1.738706,0.319246,1.539606,6.671067,-7.968950,4.196231,-2.009563,-9.205570,-9.802352,5.852504,0.807405,2.740851,-2.793575,-8.751231,-0.422254,0.237675,0.433148,3.551540,-6.566934,8.188438,4.579532,2.980821,0.319286,-7.023219,7.910905,-0.866653,-4.277051,-6.963635,1.920273,-9.145397,-9.738249,6.389619,-3.157326,-1.792323,7.764676,3.837875,4.646280,3.377145,6.283664,-9.971106,4.751385,9.262365,5.037493,-4.818246,7.552553,-3.651848,5.921710,1.780315,-0.146226,-7.239123,-8.144860,9.038872,8.052084,-3.757124,-4.610447,3.241568,3.833783,3.225197,-5.037712,5.900200,-4.110532,6.668552,1.244725,9.670691,4.308628,-5.852425,9.752803,2.268346,-5.520991,1.143107,-4.307632,-7.739828,-4.437659,-5.625855,-4.571458,-8.907010,-4.984230,-3.710439,-0.147841,2.990399,8.049890,3.644957,2.189662,2.790995,-9.796021,-2.048059,5.970523,8.196606,-7.466254,5.661529,9.864582,3.516365,4.075192,-5.775327,4.249850,1.338994,8.224324,-5.362530,9.934324,-7.503157,-2.261688,1.757182,0.697564,5.431650,-7.038090,-5.626095,-0.378670,1.279118,9.317278,-3.947958,-0.963767,-3.858874,-0.723627,-0.670877,-2.341441,-5.523418,-2.702854,3.167870,-1.974556,4.958889,7.022157,-0.039162,-2.410419,2.143430,5.330765,-1.258333,-0.543335,6.065762,2.862308,-6.492957,-5.391202,3.941368,-8.623944,1.011770,9.672247,-0.548263,-0.738596,0.780260,-4.582173,9.941819,-1.700029,6.959035,-1.330596,8.670810,8.832812,4.548943,-5.127475,-9.727997,1.900455,3.387720,-3.780448,8.661307,8.509722,8.237995,-7.485887,1.050346,8.340477,3.510299,-8.977459,2.447015,-9.372635,9.098107,3.365218,-3.177512,0.468374,-8.762474,3.293566,6.674586,-8.609024,-9.030775,0.115763,4.782728,4.151273,-6.192820,6.326755,5.277287,-1.539997,6.899987,-8.528035,4.128163,5.412396,1.755846,1.361577,4.596434,-2.823741,-8.215797,-4.105538,-0.853976,-8.385645,0.244721,-2.051134,-8.045131,4.630664,0.697208,7.698468,-3.107203,-6.730112,7.168224,-8.105117,5.861862,-5.245154,-3.690053,9.118207,-8.707542,3.599884,6.202004,-9.192938,-0.411483,3.830357,3.515800,-5.263568,-3.544679,-9.562417,8.631769,-2.937502,2.839450,-1.884752,1.019743,-3.577748,-5.454229,0.478832,7.851869,1.233452,-2.539613,6.132001,7.206001,9.914777,-1.632082,4.972668,-6.488902,-5.079392,-2.816823,6.711171,-2.397119,-3.818611,0.934619,1.971041,3.860663,-7.272055,7.798733,-0.784448,-9.479119,-2.818318,4.083912,-3.822242,-3.584027,4.554571,7.034198,-5.684639,-7.510496,-7.737402,0.471218,-7.335371,-4.360713,-0.846881,4.438379,-8.740359,-2.950865,-6.506149,-9.494540,7.467874,-2.716179,-3.337616,7.924131,4.535933,1.222352,5.399224,7.831782,9.857549,-5.781107,-8.499185,-1.130115,0.934010,1.406718,-5.671977,-5.457640,-5.437432,-3.877165,3.461342,-8.712972,0.475780,-4.707940,-0.170921,5.682549], dtype = "float64")#candidate|6122|(1152,)|const|float64
call_6121 = relay.TupleGetItem(func_2892_call(relay.reshape(const_6122.astype('float64'), [1152,])), 1)
call_6123 = relay.TupleGetItem(func_2895_call(relay.reshape(const_6122.astype('float64'), [1152,])), 1)
output = relay.Tuple([call_6107,call_6121,const_6122,])
output2 = relay.Tuple([call_6108,call_6123,const_6122,])
func_6126 = relay.Function([], output)
mod['func_6126'] = func_6126
mod = relay.transform.InferType()(mod)
output = func_6126()
func_6127 = relay.Function([], output)
mutated_mod['func_6127'] = func_6127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5948_call = mod.get_global_var('func_5948')
func_5949_call = mutated_mod.get_global_var('func_5949')
call_6128 = relay.TupleGetItem(func_5948_call(), 0)
call_6129 = relay.TupleGetItem(func_5949_call(), 0)
func_3917_call = mod.get_global_var('func_3917')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_6147 = relay.TupleGetItem(func_3917_call(relay.reshape(call_6128.astype('bool'), [10, 1, 7])), 0)
call_6148 = relay.TupleGetItem(func_3920_call(relay.reshape(call_6128.astype('bool'), [10, 1, 7])), 0)
output = relay.Tuple([call_6128,call_6147,])
output2 = relay.Tuple([call_6129,call_6148,])
func_6154 = relay.Function([], output)
mod['func_6154'] = func_6154
mod = relay.transform.InferType()(mod)
output = func_6154()
func_6155 = relay.Function([], output)
mutated_mod['func_6155'] = func_6155
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6156 = relay.var("var_6156", dtype = "int64", shape = (5, 11, 12))#candidate|6156|(5, 11, 12)|var|int64
var_6157 = relay.var("var_6157", dtype = "int64", shape = (5, 11, 12))#candidate|6157|(5, 11, 12)|var|int64
bop_6158 = relay.equal(var_6156.astype('bool'), relay.reshape(var_6157.astype('bool'), relay.shape_of(var_6156))) # shape=(5, 11, 12)
func_3017_call = mod.get_global_var('func_3017')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_6161 = func_3017_call()
call_6162 = func_3017_call()
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
var_6164 = relay.var("var_6164", dtype = "float64", shape = (88, 1))#candidate|6164|(88, 1)|var|float64
call_6163 = relay.TupleGetItem(func_1748_call(relay.reshape(var_6164.astype('float64'), [11, 2, 4])), 0)
call_6165 = relay.TupleGetItem(func_1750_call(relay.reshape(var_6164.astype('float64'), [11, 2, 4])), 0)
bop_6166 = relay.equal(call_6161.astype('bool'), var_6164.astype('bool')) # shape=(10, 88, 7)
bop_6169 = relay.equal(call_6162.astype('bool'), var_6164.astype('bool')) # shape=(10, 88, 7)
var_6177 = relay.var("var_6177", dtype = "int64", shape = (5, 11, 12))#candidate|6177|(5, 11, 12)|var|int64
bop_6178 = relay.not_equal(var_6156.astype('bool'), relay.reshape(var_6177.astype('bool'), relay.shape_of(var_6156))) # shape=(5, 11, 12)
bop_6189 = relay.add(bop_6166.astype('int16'), call_6161.astype('int16')) # shape=(10, 88, 7)
bop_6192 = relay.add(bop_6169.astype('int16'), call_6162.astype('int16')) # shape=(10, 88, 7)
output = relay.Tuple([bop_6158,call_6163,bop_6178,bop_6189,])
output2 = relay.Tuple([bop_6158,call_6165,bop_6178,bop_6192,])
func_6193 = relay.Function([var_6156,var_6157,var_6164,var_6177,], output)
mod['func_6193'] = func_6193
mod = relay.transform.InferType()(mod)
mutated_mod['func_6193'] = func_6193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6193_call = mutated_mod.get_global_var('func_6193')
var_6195 = relay.var("var_6195", dtype = "int64", shape = (5, 11, 12))#candidate|6195|(5, 11, 12)|var|int64
var_6196 = relay.var("var_6196", dtype = "int64", shape = (5, 11, 12))#candidate|6196|(5, 11, 12)|var|int64
var_6197 = relay.var("var_6197", dtype = "float64", shape = (88, 1))#candidate|6197|(88, 1)|var|float64
var_6198 = relay.var("var_6198", dtype = "int64", shape = (5, 11, 12))#candidate|6198|(5, 11, 12)|var|int64
call_6194 = func_6193_call(var_6195,var_6196,var_6197,var_6198,)
output = call_6194
func_6199 = relay.Function([var_6195,var_6196,var_6197,var_6198,], output)
mutated_mod['func_6199'] = func_6199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3990_call = mod.get_global_var('func_3990')
func_3991_call = mutated_mod.get_global_var('func_3991')
call_6201 = relay.TupleGetItem(func_3990_call(), 1)
call_6202 = relay.TupleGetItem(func_3991_call(), 1)
output = relay.Tuple([call_6201,])
output2 = relay.Tuple([call_6202,])
func_6213 = relay.Function([], output)
mod['func_6213'] = func_6213
mod = relay.transform.InferType()(mod)
output = func_6213()
func_6214 = relay.Function([], output)
mutated_mod['func_6214'] = func_6214
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6324 = relay.const(-7.764386, dtype = "float32")#candidate|6324|()|const|float32
const_6325 = relay.const([[[7.084788,-7.319066,-0.513535,6.537533,5.397006,5.382077,-1.259881,-5.941230,-6.458434]]], dtype = "float32")#candidate|6325|(1, 1, 9)|const|float32
bop_6326 = relay.power(const_6324.astype('float32'), const_6325.astype('float32')) # shape=(1, 1, 9)
func_4991_call = mod.get_global_var('func_4991')
func_4993_call = mutated_mod.get_global_var('func_4993')
var_6335 = relay.var("var_6335", dtype = "bool", shape = (140,))#candidate|6335|(140,)|var|bool
call_6334 = relay.TupleGetItem(func_4991_call(relay.reshape(var_6335.astype('bool'), [5, 28])), 2)
call_6336 = relay.TupleGetItem(func_4993_call(relay.reshape(var_6335.astype('bool'), [5, 28])), 2)
bop_6342 = relay.right_shift(bop_6326.astype('uint64'), const_6324.astype('uint64')) # shape=(1, 1, 9)
func_3171_call = mod.get_global_var('func_3171')
func_3174_call = mutated_mod.get_global_var('func_3174')
var_6365 = relay.var("var_6365", dtype = "bool", shape = (490,))#candidate|6365|(490,)|var|bool
call_6364 = relay.TupleGetItem(func_3171_call(relay.reshape(var_6365.astype('bool'), [10, 7, 7])), 3)
call_6366 = relay.TupleGetItem(func_3174_call(relay.reshape(var_6365.astype('bool'), [10, 7, 7])), 3)
output = relay.Tuple([call_6334,var_6335,bop_6342,call_6364,var_6365,])
output2 = relay.Tuple([call_6336,var_6335,bop_6342,call_6366,var_6365,])
func_6370 = relay.Function([var_6335,var_6365,], output)
mod['func_6370'] = func_6370
mod = relay.transform.InferType()(mod)
mutated_mod['func_6370'] = func_6370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6370_call = mutated_mod.get_global_var('func_6370')
var_6372 = relay.var("var_6372", dtype = "bool", shape = (140,))#candidate|6372|(140,)|var|bool
var_6373 = relay.var("var_6373", dtype = "bool", shape = (490,))#candidate|6373|(490,)|var|bool
call_6371 = func_6370_call(var_6372,var_6373,)
output = call_6371
func_6374 = relay.Function([var_6372,var_6373,], output)
mutated_mod['func_6374'] = func_6374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mod.get_global_var('func_6126')
func_6127_call = mutated_mod.get_global_var('func_6127')
call_6415 = relay.TupleGetItem(func_6126_call(), 0)
call_6416 = relay.TupleGetItem(func_6127_call(), 0)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_6422 = func_3961_call()
call_6423 = func_3961_call()
func_3285_call = mod.get_global_var('func_3285')
func_3288_call = mutated_mod.get_global_var('func_3288')
const_6444 = relay.const([2.424598,7.864656,5.365218,-3.935193,-9.010569,7.814335,9.362754,-9.134619,-7.232760,-8.842056,-8.530748,6.375405,5.661106,-3.464025,1.356160,-8.617102,1.220481,-0.383542,2.014186,2.587749,-6.901957,-3.553160,-8.692627,8.303288,-9.573637,-3.422041,7.613079,-2.317415,-1.807515,-3.206850,8.913802,-6.743020,-9.358327,2.574590,-9.195849,5.931569,-7.495563,-3.807168,-0.349977,0.569386,2.028584,4.525429,3.480280,1.448066,-0.793710,4.571104,8.763797,-9.976037,1.716928,3.907497,4.718952,-0.894778,-1.216561,-0.424431,-4.876985,0.598073,-2.006419,9.999734,5.047004,1.796037,-3.788856,8.043455,-1.512724,0.168118,0.084526,0.425568,6.695022,-1.398291,-8.586339,-8.982597,-6.892941,-6.237811,-1.860860,8.873631,7.084208,-5.166118,6.772134,1.761593,8.706682,5.256570,2.505179,6.419100,2.557883,8.495331,1.375946,-6.655929,0.967527,-7.776622,-8.408819,0.155225,-6.580017,1.436296,8.174202,7.476164,2.015642,-4.713649,-5.285349,9.475329,3.239769,4.383137,-3.605341,9.752402,9.235347,-9.214545,7.778077,2.411359,7.510091,0.681447,7.097577,8.218973,-9.008176,5.215501,-3.129747,-5.015250,7.389373,-6.095275,6.488199,-0.938779,9.209609,7.371228,-3.202876,-4.479157,6.483198,3.154510,-7.488937,-4.706033,-0.521613,3.052517,-0.376434,-7.636976,-1.777687,-7.991322,-0.051695,-5.517264,0.902329,-8.950168,-3.510891,5.114423,5.344654,-4.342532], dtype = "float64")#candidate|6444|(140,)|const|float64
call_6443 = relay.TupleGetItem(func_3285_call(relay.reshape(const_6444.astype('float64'), [140,])), 1)
call_6445 = relay.TupleGetItem(func_3288_call(relay.reshape(const_6444.astype('float64'), [140,])), 1)
func_6007_call = mod.get_global_var('func_6007')
func_6008_call = mutated_mod.get_global_var('func_6008')
call_6466 = relay.TupleGetItem(func_6007_call(), 0)
call_6467 = relay.TupleGetItem(func_6008_call(), 0)
output = relay.Tuple([call_6415,call_6422,call_6443,const_6444,call_6466,])
output2 = relay.Tuple([call_6416,call_6423,call_6445,const_6444,call_6467,])
func_6473 = relay.Function([], output)
mod['func_6473'] = func_6473
mod = relay.transform.InferType()(mod)
output = func_6473()
func_6474 = relay.Function([], output)
mutated_mod['func_6474'] = func_6474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_6510 = func_4803_call()
call_6511 = func_4803_call()
output = relay.Tuple([call_6510,])
output2 = relay.Tuple([call_6511,])
func_6531 = relay.Function([], output)
mod['func_6531'] = func_6531
mod = relay.transform.InferType()(mod)
mutated_mod['func_6531'] = func_6531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6531_call = mutated_mod.get_global_var('func_6531')
call_6532 = func_6531_call()
output = call_6532
func_6533 = relay.Function([], output)
mutated_mod['func_6533'] = func_6533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_6587 = func_4803_call()
call_6588 = func_4803_call()
output = relay.Tuple([call_6587,])
output2 = relay.Tuple([call_6588,])
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
func_5044_call = mod.get_global_var('func_5044')
func_5045_call = mutated_mod.get_global_var('func_5045')
call_6637 = relay.TupleGetItem(func_5044_call(), 0)
call_6638 = relay.TupleGetItem(func_5045_call(), 0)
output = relay.Tuple([call_6637,])
output2 = relay.Tuple([call_6638,])
func_6643 = relay.Function([], output)
mod['func_6643'] = func_6643
mod = relay.transform.InferType()(mod)
mutated_mod['func_6643'] = func_6643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6643_call = mutated_mod.get_global_var('func_6643')
call_6644 = func_6643_call()
output = call_6644
func_6645 = relay.Function([], output)
mutated_mod['func_6645'] = func_6645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5743_call = mod.get_global_var('func_5743')
func_5744_call = mutated_mod.get_global_var('func_5744')
call_6660 = func_5743_call()
call_6661 = func_5743_call()
func_5652_call = mod.get_global_var('func_5652')
func_5653_call = mutated_mod.get_global_var('func_5653')
call_6683 = relay.TupleGetItem(func_5652_call(), 3)
call_6684 = relay.TupleGetItem(func_5653_call(), 3)
var_6697 = relay.var("var_6697", dtype = "float64", shape = (288, 4))#candidate|6697|(288, 4)|var|float64
bop_6698 = relay.bitwise_and(call_6683.astype('int16'), relay.reshape(var_6697.astype('int16'), relay.shape_of(call_6683))) # shape=(288, 4)
bop_6701 = relay.bitwise_and(call_6684.astype('int16'), relay.reshape(var_6697.astype('int16'), relay.shape_of(call_6684))) # shape=(288, 4)
output = relay.Tuple([call_6660,bop_6698,])
output2 = relay.Tuple([call_6661,bop_6701,])
func_6706 = relay.Function([var_6697,], output)
mod['func_6706'] = func_6706
mod = relay.transform.InferType()(mod)
mutated_mod['func_6706'] = func_6706
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6707 = relay.var("var_6707", dtype = "float64", shape = (288, 4))#candidate|6707|(288, 4)|var|float64
func_6706_call = mutated_mod.get_global_var('func_6706')
call_6708 = func_6706_call(var_6707)
output = call_6708
func_6709 = relay.Function([var_6707], output)
mutated_mod['func_6709'] = func_6709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4622_call = mod.get_global_var('func_4622')
func_4623_call = mutated_mod.get_global_var('func_4623')
call_6727 = relay.TupleGetItem(func_4622_call(), 0)
call_6728 = relay.TupleGetItem(func_4623_call(), 0)
output = relay.Tuple([call_6727,])
output2 = relay.Tuple([call_6728,])
func_6731 = relay.Function([], output)
mod['func_6731'] = func_6731
mod = relay.transform.InferType()(mod)
mutated_mod['func_6731'] = func_6731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6731_call = mutated_mod.get_global_var('func_6731')
call_6732 = func_6731_call()
output = call_6732
func_6733 = relay.Function([], output)
mutated_mod['func_6733'] = func_6733
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6756 = relay.var("var_6756", dtype = "float32", shape = (11, 8, 9))#candidate|6756|(11, 8, 9)|var|float32
uop_6757 = relay.sinh(var_6756.astype('float32')) # shape=(11, 8, 9)
output = relay.Tuple([uop_6757,])
output2 = relay.Tuple([uop_6757,])
func_6761 = relay.Function([var_6756,], output)
mod['func_6761'] = func_6761
mod = relay.transform.InferType()(mod)
var_6762 = relay.var("var_6762", dtype = "float32", shape = (11, 8, 9))#candidate|6762|(11, 8, 9)|var|float32
output = func_6761(var_6762)
func_6763 = relay.Function([var_6762], output)
mutated_mod['func_6763'] = func_6763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5926_call = mod.get_global_var('func_5926')
func_5927_call = mutated_mod.get_global_var('func_5927')
call_6771 = func_5926_call()
call_6772 = func_5926_call()
output = call_6771
output2 = call_6772
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
func_6213_call = mod.get_global_var('func_6213')
func_6214_call = mutated_mod.get_global_var('func_6214')
call_6782 = relay.TupleGetItem(func_6213_call(), 0)
call_6783 = relay.TupleGetItem(func_6214_call(), 0)
func_566_call = mod.get_global_var('func_566')
func_570_call = mutated_mod.get_global_var('func_570')
const_6785 = relay.const([[-7,-6,2,-6,5,3,-9,3,8,4,-2,8,5,4,6,-2,4,-8,1,5,5,9,4,-8,10,6,1,10,6,4,1,2,4,-2,-3,3,7,-2,4,3,1,9,-3,-8,2,2,-7,-1,-6,6,-9,5,-2,7,8,1,-9,-1,-9,3,2,5,10,10,8,-3,-8,-5,9,6,1,-7,8,-3,9,-8,-1,-2,-10,5,2,-7,10,9,-3,5,2,6,-9,9,-5,3,-2,5,9,2,-1,4,-2,-1,7,10,-7,1,5,8,-9,-6,-7,-2,4,-10,6,6,-6,-4,-4,-4,3,1,-7,10,9,6,-8,2,4,-8,-5,-8,-1,6,1,8,-7,-3,-7,2,-10,4,9,-1,10,-3,4,-6,8,-2,-3,-2,-9,-7,-8,6,9,8,-6,9,6,10,5,-7,-9,-1,-9,-5,8,9,-2,5,-3,-7,10,4,2,-8,-2,-10,-3,-3,4,5,1,9,8,-5,5,-1,-2,2,1,-10,6,5,-1,-4,-8,8,-2,1,8,-3,9,-9,3,2,-5,8,-4,-1,-1,1,-3,-7,3,8,-5,6,9,5,-1,5,-1,7,7,-10,4,-8,-10,5,6,-7,-4,-6,-2,-4,-10,-1,3,-6,-8,9,-8,1,3,-3,9,1,-7,-8,-8,4,-1,-8,-4,5,1,-6,-2,-6,4,5,1,9,-4,9,-9,-9,7,-5,2,-5,-5,-1,-9,-3,8,6,-5,-9,4,-1,8,-3,9,-8,-9,3,5,10,-3,-6,-10,-10,9,-6,-7,6,-8,2,7,10,4,-10,9,2,-3,-3,-3,10,4,5,-2,7,-9,9,3,-10,7,6,9,10,-6,-7,-7,1,4,1,8,-7,-8,-3,-10,-8,4,-2,3,7,6,10,-2,3,10,3,3,-5,10,2,2,4,-5,10]], dtype = "uint16")#candidate|6785|(1, 352)|const|uint16
call_6784 = func_566_call(relay.reshape(const_6785.astype('uint16'), [4, 11, 8]), relay.reshape(const_6785.astype('uint16'), [4, 11, 8]), )
call_6786 = func_566_call(relay.reshape(const_6785.astype('uint16'), [4, 11, 8]), relay.reshape(const_6785.astype('uint16'), [4, 11, 8]), )
bop_6794 = relay.right_shift(const_6785.astype('int8'), relay.reshape(call_6784.astype('int8'), relay.shape_of(const_6785))) # shape=(1, 352)
bop_6797 = relay.right_shift(const_6785.astype('int8'), relay.reshape(call_6786.astype('int8'), relay.shape_of(const_6785))) # shape=(1, 352)
func_5926_call = mod.get_global_var('func_5926')
func_5927_call = mutated_mod.get_global_var('func_5927')
call_6798 = func_5926_call()
call_6799 = func_5926_call()
func_3337_call = mod.get_global_var('func_3337')
func_3341_call = mutated_mod.get_global_var('func_3341')
var_6820 = relay.var("var_6820", dtype = "bool", shape = (490,))#candidate|6820|(490,)|var|bool
var_6821 = relay.var("var_6821", dtype = "float64", shape = (88, 1))#candidate|6821|(88, 1)|var|float64
call_6819 = relay.TupleGetItem(func_3337_call(relay.reshape(var_6820.astype('bool'), [490,]), relay.reshape(var_6821.astype('float64'), [88, 1]), ), 0)
call_6822 = relay.TupleGetItem(func_3341_call(relay.reshape(var_6820.astype('bool'), [490,]), relay.reshape(var_6821.astype('float64'), [88, 1]), ), 0)
uop_6828 = relay.sin(bop_6794.astype('float64')) # shape=(1, 352)
uop_6830 = relay.sin(bop_6797.astype('float64')) # shape=(1, 352)
output = relay.Tuple([call_6782,call_6798,call_6819,var_6820,var_6821,uop_6828,])
output2 = relay.Tuple([call_6783,call_6799,call_6822,var_6820,var_6821,uop_6830,])
func_6833 = relay.Function([var_6820,var_6821,], output)
mod['func_6833'] = func_6833
mod = relay.transform.InferType()(mod)
mutated_mod['func_6833'] = func_6833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6833_call = mutated_mod.get_global_var('func_6833')
var_6835 = relay.var("var_6835", dtype = "bool", shape = (490,))#candidate|6835|(490,)|var|bool
var_6836 = relay.var("var_6836", dtype = "float64", shape = (88, 1))#candidate|6836|(88, 1)|var|float64
call_6834 = func_6833_call(var_6835,var_6836,)
output = call_6834
func_6837 = relay.Function([var_6835,var_6836,], output)
mutated_mod['func_6837'] = func_6837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3385_call = mod.get_global_var('func_3385')
func_3387_call = mutated_mod.get_global_var('func_3387')
call_6850 = relay.TupleGetItem(func_3385_call(), 1)
call_6851 = relay.TupleGetItem(func_3387_call(), 1)
func_6370_call = mod.get_global_var('func_6370')
func_6374_call = mutated_mod.get_global_var('func_6374')
var_6860 = relay.var("var_6860", dtype = "bool", shape = (70, 2))#candidate|6860|(70, 2)|var|bool
var_6861 = relay.var("var_6861", dtype = "bool", shape = (490,))#candidate|6861|(490,)|var|bool
call_6859 = relay.TupleGetItem(func_6370_call(relay.reshape(var_6860.astype('bool'), [140,]), relay.reshape(var_6861.astype('bool'), [490,]), ), 0)
call_6862 = relay.TupleGetItem(func_6374_call(relay.reshape(var_6860.astype('bool'), [140,]), relay.reshape(var_6861.astype('bool'), [490,]), ), 0)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_6876 = relay.TupleGetItem(func_2698_call(), 0)
call_6877 = relay.TupleGetItem(func_2700_call(), 0)
output = relay.Tuple([call_6850,call_6859,var_6860,var_6861,call_6876,])
output2 = relay.Tuple([call_6851,call_6862,var_6860,var_6861,call_6877,])
func_6891 = relay.Function([var_6860,var_6861,], output)
mod['func_6891'] = func_6891
mod = relay.transform.InferType()(mod)
mutated_mod['func_6891'] = func_6891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6891_call = mutated_mod.get_global_var('func_6891')
var_6893 = relay.var("var_6893", dtype = "bool", shape = (70, 2))#candidate|6893|(70, 2)|var|bool
var_6894 = relay.var("var_6894", dtype = "bool", shape = (490,))#candidate|6894|(490,)|var|bool
call_6892 = func_6891_call(var_6893,var_6894,)
output = call_6892
func_6895 = relay.Function([var_6893,var_6894,], output)
mutated_mod['func_6895'] = func_6895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6007_call = mod.get_global_var('func_6007')
func_6008_call = mutated_mod.get_global_var('func_6008')
call_6934 = relay.TupleGetItem(func_6007_call(), 0)
call_6935 = relay.TupleGetItem(func_6008_call(), 0)
output = call_6934
output2 = call_6935
func_6940 = relay.Function([], output)
mod['func_6940'] = func_6940
mod = relay.transform.InferType()(mod)
mutated_mod['func_6940'] = func_6940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6940_call = mutated_mod.get_global_var('func_6940')
call_6941 = func_6940_call()
output = call_6941
func_6942 = relay.Function([], output)
mutated_mod['func_6942'] = func_6942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6473_call = mod.get_global_var('func_6473')
func_6474_call = mutated_mod.get_global_var('func_6474')
call_6997 = relay.TupleGetItem(func_6473_call(), 2)
call_6998 = relay.TupleGetItem(func_6474_call(), 2)
output = relay.Tuple([call_6997,])
output2 = relay.Tuple([call_6998,])
func_7001 = relay.Function([], output)
mod['func_7001'] = func_7001
mod = relay.transform.InferType()(mod)
output = func_7001()
func_7002 = relay.Function([], output)
mutated_mod['func_7002'] = func_7002
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7053 = relay.var("var_7053", dtype = "float64", shape = (4, 12, 3))#candidate|7053|(4, 12, 3)|var|float64
uop_7054 = relay.sqrt(var_7053.astype('float64')) # shape=(4, 12, 3)
output = uop_7054
output2 = uop_7054
func_7062 = relay.Function([var_7053,], output)
mod['func_7062'] = func_7062
mod = relay.transform.InferType()(mod)
mutated_mod['func_7062'] = func_7062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7063 = relay.var("var_7063", dtype = "float64", shape = (4, 12, 3))#candidate|7063|(4, 12, 3)|var|float64
func_7062_call = mutated_mod.get_global_var('func_7062')
call_7064 = func_7062_call(var_7063)
output = call_7064
func_7065 = relay.Function([var_7063], output)
mutated_mod['func_7065'] = func_7065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6071_call = mod.get_global_var('func_6071')
func_6072_call = mutated_mod.get_global_var('func_6072')
call_7088 = func_6071_call()
call_7089 = func_6071_call()
func_4067_call = mod.get_global_var('func_4067')
func_4069_call = mutated_mod.get_global_var('func_4069')
var_7121 = relay.var("var_7121", dtype = "bool", shape = (140,))#candidate|7121|(140,)|var|bool
call_7120 = func_4067_call(relay.reshape(var_7121.astype('bool'), [10, 2, 7]))
call_7122 = func_4067_call(relay.reshape(var_7121.astype('bool'), [10, 2, 7]))
output = relay.Tuple([call_7088,call_7120,var_7121,])
output2 = relay.Tuple([call_7089,call_7122,var_7121,])
func_7128 = relay.Function([var_7121,], output)
mod['func_7128'] = func_7128
mod = relay.transform.InferType()(mod)
mutated_mod['func_7128'] = func_7128
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7129 = relay.var("var_7129", dtype = "bool", shape = (140,))#candidate|7129|(140,)|var|bool
func_7128_call = mutated_mod.get_global_var('func_7128')
call_7130 = func_7128_call(var_7129)
output = call_7130
func_7131 = relay.Function([var_7129], output)
mutated_mod['func_7131'] = func_7131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5550_call = mod.get_global_var('func_5550')
func_5552_call = mutated_mod.get_global_var('func_5552')
call_7133 = relay.TupleGetItem(func_5550_call(), 0)
call_7134 = relay.TupleGetItem(func_5552_call(), 0)
output = call_7133
output2 = call_7134
func_7135 = relay.Function([], output)
mod['func_7135'] = func_7135
mod = relay.transform.InferType()(mod)
mutated_mod['func_7135'] = func_7135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7135_call = mutated_mod.get_global_var('func_7135')
call_7136 = func_7135_call()
output = call_7136
func_7137 = relay.Function([], output)
mutated_mod['func_7137'] = func_7137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3684_call = mod.get_global_var('func_3684')
func_3685_call = mutated_mod.get_global_var('func_3685')
call_7138 = func_3684_call()
call_7139 = func_3684_call()
const_7143 = relay.const([[[True,True,False,False,False,False,False]],[[False,False,True,False,True,True,False]],[[True,False,True,False,True,False,False]],[[True,True,False,True,False,True,True]],[[True,True,True,False,True,True,False]],[[True,True,True,True,True,False,True]],[[True,True,True,False,False,False,False]],[[True,False,True,False,True,True,True]],[[False,False,False,True,False,True,True]],[[True,True,True,False,False,False,True]]], dtype = "bool")#candidate|7143|(10, 1, 7)|const|bool
bop_7144 = relay.equal(call_7138.astype('bool'), relay.reshape(const_7143.astype('bool'), relay.shape_of(call_7138))) # shape=(10, 1, 7)
bop_7147 = relay.equal(call_7139.astype('bool'), relay.reshape(const_7143.astype('bool'), relay.shape_of(call_7139))) # shape=(10, 1, 7)
func_3761_call = mod.get_global_var('func_3761')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_7149 = relay.TupleGetItem(func_3761_call(), 0)
call_7150 = relay.TupleGetItem(func_3763_call(), 0)
func_5048_call = mod.get_global_var('func_5048')
func_5050_call = mutated_mod.get_global_var('func_5050')
call_7151 = func_5048_call()
call_7152 = func_5048_call()
func_6126_call = mod.get_global_var('func_6126')
func_6127_call = mutated_mod.get_global_var('func_6127')
call_7154 = relay.TupleGetItem(func_6126_call(), 0)
call_7155 = relay.TupleGetItem(func_6127_call(), 0)
output = relay.Tuple([bop_7144,call_7149,call_7151,call_7154,])
output2 = relay.Tuple([bop_7147,call_7150,call_7152,call_7155,])
func_7156 = relay.Function([], output)
mod['func_7156'] = func_7156
mod = relay.transform.InferType()(mod)
mutated_mod['func_7156'] = func_7156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7156_call = mutated_mod.get_global_var('func_7156')
call_7157 = func_7156_call()
output = call_7157
func_7158 = relay.Function([], output)
mutated_mod['func_7158'] = func_7158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5980_call = mod.get_global_var('func_5980')
func_5981_call = mutated_mod.get_global_var('func_5981')
call_7264 = relay.TupleGetItem(func_5980_call(), 0)
call_7265 = relay.TupleGetItem(func_5981_call(), 0)
output = relay.Tuple([call_7264,])
output2 = relay.Tuple([call_7265,])
func_7284 = relay.Function([], output)
mod['func_7284'] = func_7284
mod = relay.transform.InferType()(mod)
output = func_7284()
func_7285 = relay.Function([], output)
mutated_mod['func_7285'] = func_7285
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7346 = relay.const([[[False,True,True,True,True,True,False],[True,False,False,False,True,True,True],[True,True,False,False,True,False,True],[True,True,True,False,True,True,True],[True,True,False,True,False,True,False],[True,False,True,True,True,True,True],[False,False,True,True,True,True,True],[True,True,True,False,False,False,False],[True,True,True,False,True,True,False]],[[True,False,False,True,True,True,False],[False,False,True,False,True,False,True],[False,True,False,True,False,True,True],[True,False,True,False,True,True,True],[False,False,True,False,True,True,True],[False,True,True,False,True,False,False],[False,True,True,True,False,True,False],[True,True,False,False,True,True,False],[False,False,True,True,True,False,True]],[[False,False,False,False,True,True,False],[False,True,False,True,False,True,False],[True,False,False,False,True,False,False],[False,False,False,True,False,False,False],[True,False,True,True,False,True,True],[True,False,True,False,True,True,True],[False,False,True,True,True,True,True],[False,False,True,True,False,True,False],[False,True,False,False,False,True,True]],[[False,False,True,False,False,False,False],[True,False,True,True,False,False,False],[True,True,True,False,True,False,True],[True,False,True,False,True,True,False],[True,False,True,False,False,False,False],[False,True,False,True,True,True,True],[True,True,True,True,False,True,True],[False,True,False,True,True,True,True],[True,False,True,False,False,True,False]],[[False,True,False,False,False,False,True],[True,True,False,True,False,False,False],[True,True,True,True,False,True,False],[False,False,False,True,False,True,True],[False,False,False,False,False,False,False],[False,True,True,False,False,False,True],[True,False,True,False,True,False,True],[True,True,True,True,True,True,False],[True,True,False,True,True,False,True]],[[True,False,True,False,True,False,False],[False,False,True,True,False,False,True],[True,False,False,True,True,True,False],[False,True,True,True,False,True,False],[True,True,True,True,True,False,True],[True,False,True,True,True,False,False],[True,False,True,True,False,True,False],[True,False,False,True,True,True,False],[True,False,False,True,True,True,False]],[[True,True,True,False,True,False,True],[False,False,True,False,False,False,True],[False,True,True,True,True,True,False],[True,True,False,False,True,False,True],[True,True,True,False,False,False,False],[True,False,True,False,False,False,False],[False,False,True,False,True,False,True],[False,True,True,True,False,True,False],[False,True,True,True,False,True,True]],[[False,True,True,False,False,False,False],[False,False,False,True,False,True,True],[True,True,True,True,False,False,True],[True,False,True,True,True,False,False],[False,True,True,False,True,False,False],[True,False,False,True,False,False,False],[False,True,False,True,False,True,False],[True,True,True,False,True,False,True],[True,True,True,True,False,False,True]],[[True,False,False,False,False,False,False],[False,True,False,False,False,False,True],[True,True,True,False,True,True,False],[False,True,True,True,False,False,False],[True,False,False,False,False,False,True],[False,False,True,False,True,True,False],[False,False,True,True,True,False,True],[False,True,True,True,True,False,False],[True,False,True,False,False,True,True]],[[False,True,False,False,True,True,False],[True,False,False,True,False,True,False],[False,True,True,False,True,False,True],[False,False,False,True,False,True,False],[False,False,True,False,True,True,False],[False,False,False,True,False,False,False],[True,True,False,True,False,True,True],[True,True,True,True,True,True,True],[True,False,True,True,False,False,True]],[[True,True,True,True,True,True,True],[True,True,True,False,False,False,True],[True,True,True,False,True,False,False],[False,True,True,False,True,False,True],[True,False,True,False,True,False,True],[False,False,False,True,True,False,False],[False,False,True,True,True,False,True],[False,False,True,True,True,False,True],[False,False,False,True,False,True,True]],[[True,False,True,True,False,True,True],[True,True,True,True,True,False,False],[True,True,False,True,True,True,False],[True,False,True,True,False,False,True],[True,True,False,False,True,True,False],[True,True,True,True,False,False,False],[False,False,True,True,True,True,False],[True,False,True,False,False,False,True],[True,False,False,False,False,True,False]],[[True,False,False,True,True,True,False],[False,True,False,False,False,True,True],[True,False,True,False,True,False,False],[True,True,False,False,True,False,False],[True,True,True,True,False,True,False],[True,True,False,True,False,False,True],[False,False,False,False,False,False,False],[True,False,True,True,True,True,True],[True,True,False,False,True,True,True]],[[True,False,True,False,True,True,False],[False,False,True,False,False,False,False],[False,False,True,False,False,False,True],[False,True,False,True,False,False,True],[True,True,True,False,False,False,True],[True,False,True,True,False,False,False],[False,False,False,False,False,True,False],[True,True,True,True,False,False,False],[True,False,True,False,False,False,True]]], dtype = "bool")#candidate|7346|(14, 9, 7)|const|bool
var_7347 = relay.var("var_7347", dtype = "bool", shape = (14, 9, 7))#candidate|7347|(14, 9, 7)|var|bool
bop_7348 = relay.logical_or(const_7346.astype('bool'), relay.reshape(var_7347.astype('bool'), relay.shape_of(const_7346))) # shape=(14, 9, 7)
output = relay.Tuple([bop_7348,])
output2 = relay.Tuple([bop_7348,])
func_7362 = relay.Function([var_7347,], output)
mod['func_7362'] = func_7362
mod = relay.transform.InferType()(mod)
var_7363 = relay.var("var_7363", dtype = "bool", shape = (14, 9, 7))#candidate|7363|(14, 9, 7)|var|bool
output = func_7362(var_7363)
func_7364 = relay.Function([var_7363], output)
mutated_mod['func_7364'] = func_7364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3385_call = mod.get_global_var('func_3385')
func_3387_call = mutated_mod.get_global_var('func_3387')
call_7394 = relay.TupleGetItem(func_3385_call(), 1)
call_7395 = relay.TupleGetItem(func_3387_call(), 1)
func_566_call = mod.get_global_var('func_566')
func_570_call = mutated_mod.get_global_var('func_570')
var_7404 = relay.var("var_7404", dtype = "uint16", shape = (352,))#candidate|7404|(352,)|var|uint16
call_7403 = func_566_call(relay.reshape(var_7404.astype('uint16'), [4, 11, 8]), relay.reshape(var_7404.astype('uint16'), [4, 11, 8]), )
call_7405 = func_566_call(relay.reshape(var_7404.astype('uint16'), [4, 11, 8]), relay.reshape(var_7404.astype('uint16'), [4, 11, 8]), )
func_4228_call = mod.get_global_var('func_4228')
func_4230_call = mutated_mod.get_global_var('func_4230')
var_7436 = relay.var("var_7436", dtype = "bool", shape = (140,))#candidate|7436|(140,)|var|bool
call_7435 = relay.TupleGetItem(func_4228_call(relay.reshape(var_7436.astype('bool'), [10, 2, 7])), 3)
call_7437 = relay.TupleGetItem(func_4230_call(relay.reshape(var_7436.astype('bool'), [10, 2, 7])), 3)
output = relay.Tuple([call_7394,call_7403,var_7404,call_7435,var_7436,])
output2 = relay.Tuple([call_7395,call_7405,var_7404,call_7437,var_7436,])
func_7446 = relay.Function([var_7404,var_7436,], output)
mod['func_7446'] = func_7446
mod = relay.transform.InferType()(mod)
var_7447 = relay.var("var_7447", dtype = "uint16", shape = (352,))#candidate|7447|(352,)|var|uint16
var_7448 = relay.var("var_7448", dtype = "bool", shape = (140,))#candidate|7448|(140,)|var|bool
output = func_7446(var_7447,var_7448,)
func_7449 = relay.Function([var_7447,var_7448,], output)
mutated_mod['func_7449'] = func_7449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4878_call = mod.get_global_var('func_4878')
func_4880_call = mutated_mod.get_global_var('func_4880')
call_7459 = relay.TupleGetItem(func_4878_call(), 1)
call_7460 = relay.TupleGetItem(func_4880_call(), 1)
output = relay.Tuple([call_7459,])
output2 = relay.Tuple([call_7460,])
func_7461 = relay.Function([], output)
mod['func_7461'] = func_7461
mod = relay.transform.InferType()(mod)
output = func_7461()
func_7462 = relay.Function([], output)
mutated_mod['func_7462'] = func_7462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3385_call = mod.get_global_var('func_3385')
func_3387_call = mutated_mod.get_global_var('func_3387')
call_7476 = relay.TupleGetItem(func_3385_call(), 1)
call_7477 = relay.TupleGetItem(func_3387_call(), 1)
func_7362_call = mod.get_global_var('func_7362')
func_7364_call = mutated_mod.get_global_var('func_7364')
var_7480 = relay.var("var_7480", dtype = "bool", shape = (882,))#candidate|7480|(882,)|var|bool
call_7479 = relay.TupleGetItem(func_7362_call(relay.reshape(var_7480.astype('bool'), [14, 9, 7])), 0)
call_7481 = relay.TupleGetItem(func_7364_call(relay.reshape(var_7480.astype('bool'), [14, 9, 7])), 0)
func_3718_call = mod.get_global_var('func_3718')
func_3721_call = mutated_mod.get_global_var('func_3721')
var_7486 = relay.var("var_7486", dtype = "float32", shape = (1, 128))#candidate|7486|(1, 128)|var|float32
call_7485 = relay.TupleGetItem(func_3718_call(relay.reshape(var_7486.astype('float32'), [128,])), 1)
call_7487 = relay.TupleGetItem(func_3721_call(relay.reshape(var_7486.astype('float32'), [128,])), 1)
output = relay.Tuple([call_7476,call_7479,var_7480,call_7485,var_7486,])
output2 = relay.Tuple([call_7477,call_7481,var_7480,call_7487,var_7486,])
func_7515 = relay.Function([var_7480,var_7486,], output)
mod['func_7515'] = func_7515
mod = relay.transform.InferType()(mod)
var_7516 = relay.var("var_7516", dtype = "bool", shape = (882,))#candidate|7516|(882,)|var|bool
var_7517 = relay.var("var_7517", dtype = "float32", shape = (1, 128))#candidate|7517|(1, 128)|var|float32
output = func_7515(var_7516,var_7517,)
func_7518 = relay.Function([var_7516,var_7517,], output)
mutated_mod['func_7518'] = func_7518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6779_call = mod.get_global_var('func_6779')
func_6781_call = mutated_mod.get_global_var('func_6781')
call_7554 = func_6779_call()
call_7555 = func_6779_call()
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
const_7570 = relay.const([-5.375054,-0.160699,4.383782,1.244771,-9.060549,-4.841638,8.939184,-6.780695,1.267817,6.482165,-4.550988,-6.840287,4.124625,8.776676,2.048089,2.659622,-6.426430,0.165720,-2.517949,1.706092,6.948512,-3.457321,-2.845046,-3.916595,5.127556,7.876100,-2.568666,1.762522,-0.384655,-2.522650,6.214367,7.563844,5.499558,-1.128679,8.105526,-3.970733,6.984871,9.245813,6.861565,2.330950,4.891192,4.794650,6.051003,3.093154,4.385625,6.247135,-9.419004,-0.237773,9.585184,7.938791,-0.111719,-8.974552,-2.093086,4.582012,7.962113,-9.200248,5.261028,-7.346109,-6.682985,1.773645,2.465702,7.082239,7.864456,1.843957,-8.119075,-2.061152,1.791876,-8.783202,-6.674491,8.928916,-9.325817,1.997513,3.245239,-7.745919,7.101176,4.336405,-5.252391,-3.793217,-1.598258,7.643044,8.343976,5.833040,-6.741986,-8.448820,-0.493560,-4.100648,-7.037778,-9.954853,2.158303,7.429372,-4.854792,7.646601,3.090409,0.969093,6.041582,-5.675527,-4.801536,4.734749,7.702141,4.447523,-9.108392,1.063294,3.661285,-3.117518,-4.673725,-7.594977,5.744686,-1.226574,7.449368,-8.087415,-5.830962,2.900891,1.263531,4.540340,6.955178,-0.891199,-4.266312,-4.022222,9.756886,-8.600721,-1.076018,6.689348,-0.773102,0.456300,0.830858,-0.414681,-5.961647,-6.696500,6.966683,2.085129,-2.016788,-6.924917,9.916085,5.420032,5.461292,-5.157012,-3.711639,0.996844,2.868176,-7.414805,6.719879,-7.733072,1.742136,0.548702,-8.678666,5.586080,-6.939915,8.441951,-4.990735,-0.079973,-1.141520,7.593259,-5.636394,8.333791,8.232145,-2.186837,3.262056,8.717947,4.217127,9.046744,4.189479,8.005649,-3.702066,8.025856,9.805104,-3.972531,-4.226896,-0.411486,3.854865,5.814360,3.312082,9.234476,-6.797021,5.847206,0.183926,-6.389164,3.277234,-8.782190,-1.169926,-4.321237,3.848254,-6.221537,8.581816,6.308116,-3.352535,2.910677,-4.255913,-3.700630,7.300635,9.103107,-9.124562,5.162238,4.329237,9.570585,0.888343,6.787523,0.726025,3.267429,-3.014529,4.991343,6.062053,-4.869172,1.244021,-7.095588,5.517059,9.132034,1.392520,9.333141,-3.022354,0.674059,7.504745,-5.022266,-2.832155,5.987546,-2.887821,8.826465,8.533471,-9.892826,6.722625,-4.813573,-5.319080,-5.993036,-2.256859,-3.109958,5.630296,6.169932,-6.504226,9.055690,7.682970,0.594477,5.728843,6.228755,-8.679343,3.425816,-4.740148,-8.727340,6.215973,9.092198,7.064694,-9.594174,8.459110,2.432907,9.350851,-9.353503,9.142209,2.680401,-1.995916,5.853700,-4.854461,-7.180288,-9.162885,8.581533,-1.609632,-3.372167,-5.846072,-5.918480,-9.297479,2.378543,-4.237218,-8.687499,9.432407,-0.078550,-3.901507,-6.550694,-7.192050,2.314584,-0.110792,-8.218286,0.996816,-0.001742,9.153319,7.101913,-4.812148,2.611731,-5.059350,-4.643693,3.497462,-6.418591,-2.710198,-7.905703,3.721004,-6.434244,-4.186113,-3.094387,7.748316,7.089538,8.058978,-6.153070,3.163723,-8.475619,4.948900,0.477601,0.690598,-4.690005,3.368372,-4.642984,-8.128324,-2.770110,1.835714,7.548240,9.659435,6.351916,0.706299,-8.754446,-3.807082,3.689153,8.262882,-4.577975,-2.922544,-6.482323,-3.722098,-7.594974,6.151089,1.735720,-4.462140,4.018736,-3.937227,-2.514708,-4.727938,-1.887540,-6.274301,-7.465321,2.814159,-8.988437,6.029009,1.488291,-5.199407,7.011489,-2.567721,-1.785342,4.103173,-8.166641,5.815970,0.497502,9.143809,-6.577735,4.159847,2.815845,1.603826,-7.239919,-2.700874,-3.381093,-1.374058,0.954929,1.585511,6.114121,5.918828,-0.551127,-7.277322,4.792379,1.201912,2.124582,-8.836921,0.555495,5.339109,7.130636,9.306539,-5.171948,7.495901,-4.934266,3.642026,4.295705,6.699439,2.040518,9.937668,7.953620,-5.736938,-7.645953,8.297641,2.940661,3.518874,6.052239,-4.590731,-5.591728,0.835400,-7.525784,-8.012278,7.910194,6.123338,-8.669636,4.945867,-9.385280,-1.039257,0.817802,-4.717018,-5.399479,3.942580,1.479969,5.994839,0.823643,-0.336044,-9.581033,1.884407,8.670646,-0.095978,3.700051,4.132011,-7.557605,-8.857660,-2.878843,-9.056836,0.280609,-1.165364,8.755716,-9.991024,-9.986038,2.165317,-8.098761,-5.748834,6.554010,6.069136,8.513264,-6.190744,-3.538056,5.836783,-1.263830,-5.941462,0.939251,-4.123869,-4.408509,0.607341,2.636395,1.130178,4.599926,5.592877,9.279680,1.684167,-5.310253,-0.988810,8.174786,3.876821,2.597673,0.293067,-1.542718,7.359722,-9.393954,2.497775,2.793298,9.331283,-9.971774,-5.556853,0.314701,-4.325123,5.976554,4.310119,-4.011906,-8.346427,-5.860035,-8.423042,4.718599,5.295786,-8.040651,-1.404704,-7.058015,-7.123858,-4.817369,-6.225350,9.599312,4.487600,8.520980,7.240457,5.997994,5.395810,8.547767,-5.328782,8.512125,-2.524704,-3.624454,-1.123253,1.318177,-6.024087,1.419311,0.276369,8.603150,7.948943,6.287667,6.957986,0.061075,-4.202572,-8.055614,2.896028,3.956962,-4.954218,-0.330759,-7.502664,7.622176,-2.006885,7.535042,7.988081,-8.843457,3.558492,3.103552,4.124698,4.289083,4.470864,-9.003826,1.315917,8.045693,-5.335675,-5.198801,6.008534,1.631262,-4.632002,4.690348,1.000945,5.289338,-3.194278,7.628574,2.693338,2.157507,2.698271,0.230174,7.173593,-4.511497,5.271772,-9.471012,-6.732406,-2.416897,-6.621664,5.809291,4.029531,-8.197683,0.057226,7.498986,-7.722608,-5.647915,5.242039,0.448450,-9.031200,-5.105771,-9.654778,-7.612246,-4.828702,-4.189638,-7.747813,-3.015457,-8.690153,6.245351,7.861050,-5.956756,-6.109867,8.257423,-6.173793,-6.521089,-7.027117,-7.756693,-9.924563,6.938722,5.787643,6.423181,0.001959,-0.131193,8.752533,-0.858055,-4.690485,-4.849103,7.337001,-0.168853,-9.968187,-6.259740,2.481631,-3.412775,4.452159,-1.592963,2.196569,-4.140905,-5.289296,-4.286621,4.511949,-2.409618,6.700993,-9.005485,-5.144615,-8.385727,4.342063,2.785094,-1.537168,-3.562997,6.842100,-4.650598,1.323113,-6.259329,1.296204,5.033457,9.355246,5.021543,-9.995101,0.060529,-8.229706,-5.925881,-1.098778,2.722911,5.933261,-1.339552,-3.065836,7.643154,2.679183,1.698285,-7.080029,4.748085,-8.858230,-1.460419,-5.460901,1.901377,2.419543,8.980884,5.494400,-3.639057,-6.663266,-2.050670,-3.246375,-9.362294,8.412559,-8.212710,-8.496375,3.528333,-7.108319,-4.630840,4.914274,-6.274836,0.564437,-9.983903,-0.707403,0.907060,2.735002,6.775376,9.118635,6.896086,-6.810451,-2.272910,-0.926321,4.197175,0.478555,6.442925,-1.942787,8.361738,5.667414,-8.257964,1.655867,3.817167,5.908315,-1.482441,-7.493613,8.436617,3.447232,-0.889606,3.487862,4.984058,2.121085,4.855709,-2.745755,9.118382,-4.405003,2.984053,4.027006,-8.208192,9.813779,7.453945,1.824227,-6.353474,-8.397865,-8.805869,4.988059,-9.405683,-0.349118,-7.410173,-7.114658,8.362032,6.754978,-2.041178,6.584775,-2.265544,0.435935,-9.067413,-9.552096,-4.365139,6.679560,3.481480,-8.306255,6.593320,7.360329,4.450149,7.723944,4.417337,3.635442,8.247764,-7.353366,2.713661,8.710287,-2.311388,3.246799,-8.754300,7.747867,8.256118,3.354085,4.492445,-5.210828,9.570807,1.032120,-3.576654,-8.714085,1.509220,5.176340,5.958562,-6.747578,6.254700,-8.956084,9.408116,6.745569,9.035659,8.669418,0.654038,5.200422,-7.178998,2.485737,4.652723,-9.115002,1.712944,6.055367,8.391748,-6.765390,6.656521,-4.227873,0.844975,8.038054,6.504105,6.907149,-4.707995,2.863379,6.790491,-9.681353,-1.192974,4.803350,-9.201408,-3.925374,-1.145052,-1.255494,1.399193,-7.229525,-0.467406,2.777680,1.070519,8.736965,6.125811,-9.781608,9.603842,4.816144,9.930789,0.112163,-6.884612,2.216619,7.127356,-3.991051,8.984439,5.171774,4.632964,7.723685,3.982804,-5.081717,1.239653,2.934533,2.634900,-0.679932,6.515472,1.393371,-4.155293,-6.750678,-6.281280,-0.849835,-4.776068,-8.315610,5.528626,-0.289889,-2.616622,5.555540,4.869970,-9.662396,-5.899829,7.632456,9.584604,1.126081,-6.306559,7.015851,-4.302068,-0.958575,3.929854,-5.723284,-8.877634,8.725345,-1.790458,-4.967034,8.763593,-7.726829,5.823155,9.944230,-6.880465,-1.509139,-6.450528,-7.125730,-8.554201,6.957966,1.383333,-1.732747,-6.438450,-6.707237,-8.498376,-1.829169,8.120890,7.757511,3.992198,9.928579,4.393302,-7.233600,3.804539,5.454273,8.926763,8.667121,-4.193301,-5.010957,2.080421,0.985047,1.876236,6.625512,4.481695,9.480489,4.512474,-1.539734,6.575512,2.372726,9.202557,-6.566145,5.004935,9.768212,0.263223,0.219899,-8.896691,-0.857696,-5.366718,7.770737,3.366002,-8.195603,7.584628,2.899631,9.273514,-2.231528,2.980413,3.235397,-0.814180,2.790652,-4.465972,2.933351,0.726084,-7.918056,8.299496,8.259957,9.960245,-2.305919,5.268947,2.127110,-8.604082,2.053135,-0.527668,-3.857324,-9.654334,-0.857533,-1.454200,8.041185,5.074423,-8.079812,2.029353,6.258407,9.041979,-2.521891,-1.552583,-8.340882,2.208660,-2.042344,-2.167475,-1.347544,-2.109355,-5.891037,-4.995153,0.513811,5.020133,1.476210,6.155459,1.502138,-2.517455,9.139352,9.952828,6.224916,-6.191906,-0.303241,-2.220529,9.005211,5.671585,-2.415314,7.974223,-5.909078,3.817674,-1.828714,-5.743703,6.660311,1.010115,1.790423,-0.757263,6.925078,1.325363,-7.391299,-5.064280,-2.930719,8.342733,-3.830202,-8.798982,8.204647,-3.341192,6.801017,-9.649909,8.689674,8.262718,-4.554955,4.984821,-5.194437,-0.224471,-8.788584,-7.913761,-4.363533,9.342314,7.851638,1.376693,6.749500,-9.712371,4.058698,-6.188268,-6.197231,4.045856,8.695271,-2.207315,3.448803,-8.199586,7.568173,0.631612,-8.897575,-1.913568,-0.765164,0.213720,1.337412,-0.548663,-8.504319,1.336979,4.835249,2.282941,9.076849,-3.395580,-2.659558,5.683587,-2.108175,-1.256511,7.426502,-9.061179,-1.512608,-1.856729,8.959369,-4.811425,3.914373,-3.435220,2.477684,1.160711,9.020250,0.714339,0.735846,4.403128,1.793872,-3.757232,8.316141,8.798053,-6.784613,5.402197,-0.847129,1.309138,-2.956281,-2.269083,-8.039199,-4.686850,-0.081230,2.171996,-6.761105,5.180531,-5.917250,4.649319,-2.631220,-4.332760,-8.336038,-2.376758,6.042241,-2.834537,3.119576,9.750259,-8.444097,6.211217,-7.478352,-6.385265,1.609216,-4.287809,-9.380789,2.095413,-0.432812,6.751434,-7.312053,-8.470698,-1.847946,2.352694,9.626677,2.595624,-1.936743,-2.412406,5.955766,-8.535206,-5.849498,3.830810,-0.393556,2.940899,-2.806735,8.667124,-4.582100,-6.620432,-3.090100,-6.719913,5.016520,1.379926,-6.254995,-1.730090,2.737795,9.922207,9.514136,-8.345431,5.333013,2.585613,-0.507693,-9.546170,-4.134097,5.952862,-3.853804,-8.711515,3.128024,-1.908765,-4.115366,-8.659829,7.019758,8.990320,-7.755477,-9.750575,-2.319635,3.761174,-5.955067,6.310864,-1.709722,0.657993,6.024737,-3.224058,6.231572,-5.244711,7.500178,5.397450,-2.497053,-1.478481,-6.758051,4.427079,-1.563481,-8.957604,-1.871918,2.473612,-7.898547,-7.550424,-7.944164,9.718538,3.664319,3.905768,-8.010598,5.437077,-9.064599,6.600163,-0.288557,8.585087,1.018605,7.455931,1.645617,-4.984747,1.347880,6.452154,-9.438375,7.074701,3.671906,-8.101177,-4.620594,-2.665212,4.179861,6.890318,-4.915420,-6.085842,-1.638777,-5.526210,-7.013349,-3.607966,6.253163,-4.986283,-9.772649,8.864099,-9.146411,5.205146,5.331457,0.013281,1.022755,-2.975493,7.853514,3.631888,-4.467796,-9.808856,-3.157780,-6.451920,-9.369167,9.532993,-0.817677,-9.378334,6.127152,7.040568,-5.053126,0.017375,-0.319030,8.113367,2.723991,5.882709,-0.963923,-9.459389,-9.766055,-2.876777,2.320480,1.064411,-5.643479,1.532645,6.386361,-7.260529,7.019574,8.807469,8.783824,-7.207996,8.793191,-8.500140,4.067959,6.819946,7.425780,-5.738693,1.269357,1.143358,-7.495486,1.686202,7.714067,7.617897,-2.048414,-9.236656,5.989604,-4.491055,7.880170,6.321454,3.199078,-9.260627,-1.241924,-5.325787,5.632356,-8.871494,-8.783528,1.486530,3.625015,-4.559507,-2.525390,-8.681887,3.863496,-4.416316,8.595736,6.693974,-7.804881,-7.964708,8.269669,9.735974,-9.394254,-5.466567,9.785401,-5.970684,-9.516123,-8.729228,-0.469656,-2.303187,4.571847,-6.180922,-4.266671,-1.943065,5.154707,-8.372801,9.228018,8.723449,7.257237,-9.812925,-7.602063,3.087292,8.497322,5.421552,-1.568818,-3.055204,-2.254954,8.242457,-9.014572,-1.037598,-8.427054,-4.676967,-8.785983,1.841909,9.698880,-9.021618,-6.709476,-4.748986,-1.288748,0.808114,-3.217671,-9.673583,-6.635612,0.316407,2.394630,1.079218,-1.448452,6.967306,1.570510,-7.648110,-9.674658,-6.943309,1.433197,1.214105,-6.132097,-6.758827,-6.208842,-3.439059,-1.300645,8.580327,6.519357,1.783401,3.173785,-3.192799,1.272832,5.595660,8.379560,4.859287,1.724038,-0.330181,2.430706,-3.673397,-7.457351,6.593734,-9.586742,-5.726076,2.034677,-7.653231,4.453494,4.296322,6.678441,-6.388269,4.965447,1.621220,-7.222251,-1.926526,8.389725,7.056067,8.394337,-4.297344,-6.802008,3.234669,5.591008,-8.611590,-6.144813,0.698437,-2.736505,4.775733,4.992383,-8.883820,-9.000164,-3.517592,0.973785,9.039483,-2.473213,3.647451,2.165057,-8.895796,-3.459794,7.678017,-5.252727,-4.982970,-9.094671,-2.317325,2.774515,-3.959596,-6.807960,3.006637,-6.062301,-4.937777,-6.425747,7.133793,3.148883,-6.462629,-9.125373,-4.769543,7.785212,-0.428071,-9.207190,6.954809,9.122018,-1.668121,-5.337822,-4.908638,-2.383619,8.544929,-6.477745,-9.550888,-6.824751,7.783401,-0.843810,-7.330019,-7.461972,-9.358549,3.546799,-2.390567,9.892985,-6.507515,-3.012144,-0.269981,-4.203609,-1.100017,5.794273,-8.607652,3.012508,-7.445583,7.014551,0.701332,4.221077,9.052803,-6.855533,-5.226179,-6.200806,5.125491,9.616627,7.774323,-0.024829,-2.861161,1.042838,1.894092,-2.656346,-3.879768,-0.943748,9.512302,9.102249,3.901211,3.730466,4.471700,-2.653812,-0.673100,1.952552,0.368666,5.649205,2.409661,-9.776200,-5.930060,-2.394610,1.292803,-3.585865,8.532564,2.535910,8.756170,-8.853094,-1.299852,-9.038840,-0.109170,-0.801732,2.841100,4.049451,-5.526200,1.899937,-4.622639,-4.077190,1.283283,-2.743073,-3.084059,6.998956,-7.519359,8.999535,-4.422445,-0.880041,0.808715,8.671469,-8.591932,1.981334,-6.026497,7.597562,-6.746832,-3.890804,5.007669,-7.791334,-7.923946,0.716647,7.505930,6.892395,-5.605911,-3.178745,0.781541,-1.459918,-8.006158,-1.659232,4.143355,7.606859,7.028824,8.983501,9.548471,3.058921,0.357621,-4.006698,6.649304,-3.329565,0.034397,9.596693,-9.693328,6.984724,7.106052,-9.954738,4.894552,-1.026135,0.905180,0.178212,-0.794076,7.939708,-8.258880,-8.733162,6.375282,5.287174,-4.112435,0.119286,1.424018,6.413133,2.857795,3.474937,-3.048002,7.220647,1.586183,-9.137835,7.804491,8.939987,0.925679,9.812728,-1.850505,-7.910402,9.546997,-7.477550,-8.439032,2.766916,6.236350,-5.034353,0.394807,8.129574,0.041405,-5.250813,1.162618,-0.250284,1.866652,-1.065594,-7.863411,-2.743715,-9.023432,-8.589095,8.481211,-4.722656,-8.512192,-1.097118,0.230256,-8.574032,3.746885,2.796008,-8.541829,5.412891,-2.595861,-0.143397,-4.833955,-1.096053,5.329999,4.584744,7.536709,6.885991,5.280254,4.782281,7.365448,3.378385,-6.560341,-8.739258,-3.758704,-9.513234,9.069879,8.109249,-9.208358,-3.928463,2.803548,-2.892662,-5.002172,-2.305169,5.366336,-8.893984,-9.644840,6.780547,-3.315766,5.862404,2.235546,3.494449,-0.627188,5.946588,3.745438,-3.444560,7.000389,1.144809,-7.582683,5.886708,7.693567,4.152713,3.449984,-1.878427,-9.773584,-2.522825,9.659266,-4.417008,4.525885,-8.725349,1.655729,8.635996,1.443018,-5.063875,-3.978767,2.452819,6.571582,5.122606,0.060084,4.222971,-0.099342,-3.909520,6.242731,5.101237,-5.325953,2.175498,2.121109,-1.256116,7.904977,-6.503840,0.109375,6.641512,-1.009530,0.090852,-4.289228,5.501184,4.880126,7.058009,-0.055551,0.619308,-2.471934,2.899039,5.634358,5.926729,-6.568041,-8.963948,1.773931,1.466589,0.992539,-0.632343,7.624047,-2.260164,4.919468,1.712280,-5.401791,-6.366343,-5.768866,-2.855557,5.152098,-3.773097,-5.472773,4.722998,0.270363,1.049892,-8.719378,-0.857790,-8.211810,-5.815790,-0.794141,5.102656,-5.937721,-6.204477,4.484467,-9.139575,-0.327305,6.585954,1.974273,-0.012917,6.861835,4.410838,5.278308,1.208321,-1.326261,0.902157,7.561538,-8.764064,-0.388586,-2.797984,2.810874,5.629637,-9.378741,-8.515213,2.152629,-5.319654,3.242527,-1.598362,9.494930,-1.558950,1.223568,1.712718,-6.023054,-9.133874,-3.327658,2.527924,3.264234,4.368174,9.589607,-9.094056,-3.734695,1.177532,-5.600049,2.438400,3.350387,-5.185029,6.377434,7.505499,9.392182,1.756029,8.028231,0.131170,7.658684,-0.251484,7.584714,9.444112,0.092479,0.022015,0.899004,9.821776,-8.291470,7.489497,4.189519,6.590888,8.458425,-6.253917,5.921164,6.600940,-4.951021,8.689378,-7.118116,-2.341399,6.555443,-9.774292,-0.049593,3.841321,3.943941,-3.306721,-8.238480,2.595170,-4.375838,-0.488975,8.773858,-2.272545,6.282006,2.069974,1.270973,3.032556,8.756870,1.918318,3.487877,-2.947671,9.648022,-4.547167,5.882157,0.385090,3.887336,9.337060,-0.487197,4.102848,-8.945194,3.346218,-5.362129,-8.250865,-0.533223,0.783029,9.685785,-2.630796,-6.000217,-1.192950,-3.803430,-8.531107,2.137115,3.842203,6.531136,1.893704,1.006755,6.170171,9.249443,-6.251193,5.483535,9.054780,7.879515,-2.762109,-0.478467,8.351423,-5.876464,5.982663,-7.694958,3.877782,9.230213,3.563835,-2.359860,-7.083859,-8.498340,9.112628,-7.060894,-2.590790,5.794155,6.899794,7.918355,-4.880276,-8.453235,9.830125,-3.529892,0.968436,8.657970,6.931280,2.636131,7.725710,-4.896202,-3.934417,-7.309968,-0.541624,8.689384,6.679012,0.338473,-1.225281,1.887487,-6.794333,3.468298,7.910673,-8.114113,-5.002004,-7.548548,2.226785,-5.449566,2.436130,5.057272,-9.373145,-1.127485,0.740125,-0.277148,8.449113,-1.807859,5.515313,6.979706,-8.563495,7.670142,-7.047994,7.464859,-5.395411,7.504189,-0.076781,-1.939277,9.989737,-2.576384,-5.408859,-3.932046,1.425573,2.659655,-4.593899,8.375896,-6.576818,3.648546,9.830249,-9.902275,4.570390,9.632765,-4.323717,-2.353161,-4.037138,2.302188,8.129078,0.712017,-4.624477,-0.559923,5.865121,8.999986,-9.048916,-0.416644,4.599783,-1.309376,-1.243568,-9.062698,9.394767,-6.289287,-7.414351,-2.305219,-7.522456,-7.334985,-4.331949,0.483223,-1.243442,0.962164,-8.518073,-8.742578,-4.627756,-5.756591,4.465422,-2.378926,8.420254,-4.288377,-3.443464,-9.496890,-9.095478,3.428335,7.141511,0.316531,8.183831,-1.380857,-1.686476,-5.665937,9.621372,-2.209345,4.838300,3.365911,0.956081,-1.664061,-7.404775,-2.256687,3.253138,4.868594,4.899880,0.677802,8.300749,-9.706243,-4.581616,4.559327,8.889247,-8.743067,-5.935695,4.838789,-6.521782,9.317614,-3.341963,0.339803,3.363132,-4.474504,2.061540,2.926608,-7.103014,5.326628,-7.616468,-0.486308,-0.276294,7.354727,2.603855,-7.319535,-5.282936,-6.584125,-2.313608,4.707376,9.190851,-2.081793,0.113379,9.140222,2.113977,-2.239681,1.690391,2.426586,-7.536029,-6.285836,6.982067,2.919118,-3.514366,3.939818,3.994400,-5.542467,-3.908490,-5.467453,4.375066,2.867477,-5.414562,-6.354274,9.098289,3.759950,-7.469556,1.039771,-6.648553,-0.752163,-0.875334,4.505675,-3.149011,-7.456808,-6.326927,-1.352533,1.795678,-2.242476,1.489363,6.346466,-9.809722,-0.281840,7.937169,2.680065,-4.896109,-5.276892,7.443058,9.623518,-1.241096,-4.549458,-7.612477,-8.402444,4.712194,4.601344,4.446415,1.246893,8.830523,5.283142,3.377928,-8.821356,-2.083062,-4.175205,4.381295,7.164915,-1.361100,-0.234278,-0.728424,-7.357872,-4.167224,-5.065043,-1.831406,5.577208,-1.835789,-7.435909,5.032320,4.147564,-8.696967,3.636291,5.700766,6.231640,7.155789,-6.015427,-6.566250,9.592246,-7.840262,-4.928115,1.415644,-6.993073,-0.920435,0.494500,-7.617087,0.719025,-9.524553,-0.455559,7.554871,5.903928,0.371596,-7.334922,-2.847198,-9.483780,-2.047704,-9.051268,1.541860,2.751317,8.563432,0.201236,9.861319,-5.399173,-0.964835,-5.389455,-0.643236,-7.172166,5.034673,7.432931,-3.983709,1.198791,3.450474,-3.309262,-1.319250,-4.400405,-3.418711,5.946746,3.627307,7.057435,-1.781771,0.325271,-7.070512,6.563934,3.566716,0.872010,-0.350848,-5.247077,-3.318221,-5.786341,-4.532069,1.699072,7.546764,-7.720619,-2.790591,-6.858783,7.666566,-0.547128,9.791087,-6.481056,-2.188232,-6.271263,-8.756577,-3.571712,8.590490,6.412564,-6.514025,-9.396624,-0.768919,-1.140691,-5.823023,9.100937,-0.638558,6.105517,6.564970,-0.844571,-0.990209,0.801299,2.250096,7.538465,-5.632567,-4.331055,7.684541,-2.503165,-5.121257,2.744241,4.325870,-4.902009,-9.152402,1.349445,8.512628,0.618963,-2.476941,-4.481187,6.725547,-7.901099,5.794099,-4.047840,2.248395,-7.552589,8.611132,2.624320,-9.633201,-7.342326,7.589757,9.031815,-6.225169,-9.923484,3.727269,-9.316078,2.571414,-3.298109,-8.503229,9.860110,-0.951428,8.353453,4.428452,-8.347268,-4.145289,-4.424834,3.768830,1.891450,9.137608,-1.183389,-9.117412,1.528046,-4.647701,-6.287769,-7.077598,-8.769114,1.251677,-2.379130,-3.022619,8.230688,4.280968,7.904116,9.317093,-3.848579,-5.255812,4.213009,-2.927452,-3.690508,-4.448856,0.665664,3.768067,3.503242,9.584879,7.704354,5.921508,-7.457517,8.780635,5.938360,-0.988012,6.609474,-2.565169,-5.624270], dtype = "float32")#candidate|7570|(2112,)|const|float32
call_7569 = relay.TupleGetItem(func_4460_call(relay.reshape(const_7570.astype('float32'), [352, 6])), 1)
call_7571 = relay.TupleGetItem(func_4462_call(relay.reshape(const_7570.astype('float32'), [352, 6])), 1)
func_4296_call = mod.get_global_var('func_4296')
func_4298_call = mutated_mod.get_global_var('func_4298')
call_7580 = func_4296_call()
call_7581 = func_4296_call()
output = relay.Tuple([call_7554,call_7569,const_7570,call_7580,])
output2 = relay.Tuple([call_7555,call_7571,const_7570,call_7581,])
func_7591 = relay.Function([], output)
mod['func_7591'] = func_7591
mod = relay.transform.InferType()(mod)
output = func_7591()
func_7592 = relay.Function([], output)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6213_call = mod.get_global_var('func_6213')
func_6214_call = mutated_mod.get_global_var('func_6214')
call_7599 = relay.TupleGetItem(func_6213_call(), 0)
call_7600 = relay.TupleGetItem(func_6214_call(), 0)
output = relay.Tuple([call_7599,])
output2 = relay.Tuple([call_7600,])
func_7608 = relay.Function([], output)
mod['func_7608'] = func_7608
mod = relay.transform.InferType()(mod)
mutated_mod['func_7608'] = func_7608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7608_call = mutated_mod.get_global_var('func_7608')
call_7609 = func_7608_call()
output = call_7609
func_7610 = relay.Function([], output)
mutated_mod['func_7610'] = func_7610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3640_call = mod.get_global_var('func_3640')
func_3642_call = mutated_mod.get_global_var('func_3642')
call_7621 = func_3640_call()
call_7622 = func_3640_call()
output = call_7621
output2 = call_7622
func_7630 = relay.Function([], output)
mod['func_7630'] = func_7630
mod = relay.transform.InferType()(mod)
output = func_7630()
func_7631 = relay.Function([], output)
mutated_mod['func_7631'] = func_7631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3228_call = mod.get_global_var('func_3228')
func_3230_call = mutated_mod.get_global_var('func_3230')
call_7634 = func_3228_call()
call_7635 = func_3228_call()
func_2848_call = mod.get_global_var('func_2848')
func_2849_call = mutated_mod.get_global_var('func_2849')
call_7652 = relay.TupleGetItem(func_2848_call(), 0)
call_7653 = relay.TupleGetItem(func_2849_call(), 0)
func_6370_call = mod.get_global_var('func_6370')
func_6374_call = mutated_mod.get_global_var('func_6374')
var_7658 = relay.var("var_7658", dtype = "bool", shape = (140,))#candidate|7658|(140,)|var|bool
var_7659 = relay.var("var_7659", dtype = "bool", shape = (49, 10))#candidate|7659|(49, 10)|var|bool
call_7657 = relay.TupleGetItem(func_6370_call(relay.reshape(var_7658.astype('bool'), [140,]), relay.reshape(var_7659.astype('bool'), [490,]), ), 4)
call_7660 = relay.TupleGetItem(func_6374_call(relay.reshape(var_7658.astype('bool'), [140,]), relay.reshape(var_7659.astype('bool'), [490,]), ), 4)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
var_7671 = relay.var("var_7671", dtype = "float64", shape = (88,))#candidate|7671|(88,)|var|float64
call_7670 = relay.TupleGetItem(func_1748_call(relay.reshape(var_7671.astype('float64'), [11, 2, 4])), 1)
call_7672 = relay.TupleGetItem(func_1750_call(relay.reshape(var_7671.astype('float64'), [11, 2, 4])), 1)
func_6193_call = mod.get_global_var('func_6193')
func_6199_call = mutated_mod.get_global_var('func_6199')
var_7682 = relay.var("var_7682", dtype = "int64", shape = (660,))#candidate|7682|(660,)|var|int64
call_7681 = relay.TupleGetItem(func_6193_call(relay.reshape(var_7682.astype('int64'), [5, 11, 12]), relay.reshape(var_7682.astype('int64'), [5, 11, 12]), relay.reshape(var_7671.astype('float64'), [88, 1]), relay.reshape(var_7682.astype('int64'), [5, 11, 12]), ), 2)
call_7683 = relay.TupleGetItem(func_6199_call(relay.reshape(var_7682.astype('int64'), [5, 11, 12]), relay.reshape(var_7682.astype('int64'), [5, 11, 12]), relay.reshape(var_7671.astype('float64'), [88, 1]), relay.reshape(var_7682.astype('int64'), [5, 11, 12]), ), 2)
output = relay.Tuple([call_7634,call_7652,call_7657,var_7658,var_7659,call_7670,var_7671,call_7681,var_7682,])
output2 = relay.Tuple([call_7635,call_7653,call_7660,var_7658,var_7659,call_7672,var_7671,call_7683,var_7682,])
func_7696 = relay.Function([var_7658,var_7659,var_7671,var_7682,], output)
mod['func_7696'] = func_7696
mod = relay.transform.InferType()(mod)
var_7697 = relay.var("var_7697", dtype = "bool", shape = (140,))#candidate|7697|(140,)|var|bool
var_7698 = relay.var("var_7698", dtype = "bool", shape = (49, 10))#candidate|7698|(49, 10)|var|bool
var_7699 = relay.var("var_7699", dtype = "float64", shape = (88,))#candidate|7699|(88,)|var|float64
var_7700 = relay.var("var_7700", dtype = "int64", shape = (660,))#candidate|7700|(660,)|var|int64
output = func_7696(var_7697,var_7698,var_7699,var_7700,)
func_7701 = relay.Function([var_7697,var_7698,var_7699,var_7700,], output)
mutated_mod['func_7701'] = func_7701
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7726 = relay.var("var_7726", dtype = "uint16", shape = ())#candidate|7726|()|var|uint16
var_7727 = relay.var("var_7727", dtype = "uint16", shape = (16, 3, 1))#candidate|7727|(16, 3, 1)|var|uint16
bop_7728 = relay.equal(var_7726.astype('bool'), var_7727.astype('bool')) # shape=(16, 3, 1)
bop_7735 = relay.less(var_7726.astype('bool'), bop_7728.astype('bool')) # shape=(16, 3, 1)
bop_7739 = relay.multiply(bop_7728.astype('int8'), relay.reshape(bop_7735.astype('int8'), relay.shape_of(bop_7728))) # shape=(16, 3, 1)
uop_7748 = relay.sigmoid(bop_7739.astype('float64')) # shape=(16, 3, 1)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_7752 = relay.TupleGetItem(func_2698_call(), 0)
call_7753 = relay.TupleGetItem(func_2700_call(), 0)
output = relay.Tuple([uop_7748,call_7752,])
output2 = relay.Tuple([uop_7748,call_7753,])
func_7772 = relay.Function([var_7726,var_7727,], output)
mod['func_7772'] = func_7772
mod = relay.transform.InferType()(mod)
mutated_mod['func_7772'] = func_7772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7772_call = mutated_mod.get_global_var('func_7772')
var_7774 = relay.var("var_7774", dtype = "uint16", shape = ())#candidate|7774|()|var|uint16
var_7775 = relay.var("var_7775", dtype = "uint16", shape = (16, 3, 1))#candidate|7775|(16, 3, 1)|var|uint16
call_7773 = func_7772_call(var_7774,var_7775,)
output = call_7773
func_7776 = relay.Function([var_7774,var_7775,], output)
mutated_mod['func_7776'] = func_7776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4878_call = mod.get_global_var('func_4878')
func_4880_call = mutated_mod.get_global_var('func_4880')
call_7789 = relay.TupleGetItem(func_4878_call(), 1)
call_7790 = relay.TupleGetItem(func_4880_call(), 1)
func_5679_call = mod.get_global_var('func_5679')
func_5680_call = mutated_mod.get_global_var('func_5680')
call_7804 = func_5679_call()
call_7805 = func_5679_call()
output = relay.Tuple([call_7789,call_7804,])
output2 = relay.Tuple([call_7790,call_7805,])
func_7812 = relay.Function([], output)
mod['func_7812'] = func_7812
mod = relay.transform.InferType()(mod)
output = func_7812()
func_7813 = relay.Function([], output)
mutated_mod['func_7813'] = func_7813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_7841 = relay.TupleGetItem(func_7812_call(), 0)
call_7842 = relay.TupleGetItem(func_7813_call(), 0)
output = call_7841
output2 = call_7842
func_7852 = relay.Function([], output)
mod['func_7852'] = func_7852
mod = relay.transform.InferType()(mod)
output = func_7852()
func_7853 = relay.Function([], output)
mutated_mod['func_7853'] = func_7853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5044_call = mod.get_global_var('func_5044')
func_5045_call = mutated_mod.get_global_var('func_5045')
call_7912 = relay.TupleGetItem(func_5044_call(), 0)
call_7913 = relay.TupleGetItem(func_5045_call(), 0)
func_4067_call = mod.get_global_var('func_4067')
func_4069_call = mutated_mod.get_global_var('func_4069')
var_7937 = relay.var("var_7937", dtype = "bool", shape = (140,))#candidate|7937|(140,)|var|bool
call_7936 = func_4067_call(relay.reshape(var_7937.astype('bool'), [10, 2, 7]))
call_7938 = func_4067_call(relay.reshape(var_7937.astype('bool'), [10, 2, 7]))
func_566_call = mod.get_global_var('func_566')
func_570_call = mutated_mod.get_global_var('func_570')
call_7940 = func_566_call(relay.reshape(call_7912.astype('uint16'), [4, 11, 8]), relay.reshape(call_7912.astype('uint16'), [4, 11, 8]), )
call_7941 = func_566_call(relay.reshape(call_7912.astype('uint16'), [4, 11, 8]), relay.reshape(call_7912.astype('uint16'), [4, 11, 8]), )
bop_7962 = relay.divide(call_7912.astype('float64'), relay.reshape(call_7940.astype('float64'), relay.shape_of(call_7912))) # shape=(4, 11, 8)
bop_7965 = relay.divide(call_7913.astype('float64'), relay.reshape(call_7941.astype('float64'), relay.shape_of(call_7913))) # shape=(4, 11, 8)
output = relay.Tuple([call_7936,var_7937,bop_7962,])
output2 = relay.Tuple([call_7938,var_7937,bop_7965,])
func_7966 = relay.Function([var_7937,], output)
mod['func_7966'] = func_7966
mod = relay.transform.InferType()(mod)
var_7967 = relay.var("var_7967", dtype = "bool", shape = (140,))#candidate|7967|(140,)|var|bool
output = func_7966(var_7967)
func_7968 = relay.Function([var_7967], output)
mutated_mod['func_7968'] = func_7968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6531_call = mod.get_global_var('func_6531')
func_6533_call = mutated_mod.get_global_var('func_6533')
call_7997 = relay.TupleGetItem(func_6531_call(), 0)
call_7998 = relay.TupleGetItem(func_6533_call(), 0)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_7999 = relay.TupleGetItem(func_7812_call(), 0)
call_8000 = relay.TupleGetItem(func_7813_call(), 0)
func_4751_call = mod.get_global_var('func_4751')
func_4753_call = mutated_mod.get_global_var('func_4753')
call_8007 = func_4751_call()
call_8008 = func_4751_call()
func_7128_call = mod.get_global_var('func_7128')
func_7131_call = mutated_mod.get_global_var('func_7131')
var_8010 = relay.var("var_8010", dtype = "bool", shape = (70, 2))#candidate|8010|(70, 2)|var|bool
call_8009 = relay.TupleGetItem(func_7128_call(relay.reshape(var_8010.astype('bool'), [140,])), 2)
call_8011 = relay.TupleGetItem(func_7131_call(relay.reshape(var_8010.astype('bool'), [140,])), 2)
output = relay.Tuple([call_7997,call_7999,call_8007,call_8009,var_8010,])
output2 = relay.Tuple([call_7998,call_8000,call_8008,call_8011,var_8010,])
func_8018 = relay.Function([var_8010,], output)
mod['func_8018'] = func_8018
mod = relay.transform.InferType()(mod)
var_8019 = relay.var("var_8019", dtype = "bool", shape = (70, 2))#candidate|8019|(70, 2)|var|bool
output = func_8018(var_8019)
func_8020 = relay.Function([var_8019], output)
mutated_mod['func_8020'] = func_8020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7461_call = mod.get_global_var('func_7461')
func_7462_call = mutated_mod.get_global_var('func_7462')
call_8044 = relay.TupleGetItem(func_7461_call(), 0)
call_8045 = relay.TupleGetItem(func_7462_call(), 0)
func_2616_call = mod.get_global_var('func_2616')
func_2618_call = mutated_mod.get_global_var('func_2618')
var_8047 = relay.var("var_8047", dtype = "float64", shape = (5, 28))#candidate|8047|(5, 28)|var|float64
call_8046 = relay.TupleGetItem(func_2616_call(relay.reshape(var_8047.astype('float64'), [5, 7, 4])), 2)
call_8048 = relay.TupleGetItem(func_2618_call(relay.reshape(var_8047.astype('float64'), [5, 7, 4])), 2)
func_3337_call = mod.get_global_var('func_3337')
func_3341_call = mutated_mod.get_global_var('func_3341')
const_8050 = relay.const([True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,False,False], dtype = "bool")#candidate|8050|(490,)|const|bool
var_8051 = relay.var("var_8051", dtype = "float64", shape = (88,))#candidate|8051|(88,)|var|float64
call_8049 = relay.TupleGetItem(func_3337_call(relay.reshape(const_8050.astype('bool'), [490,]), relay.reshape(var_8051.astype('float64'), [88, 1]), ), 4)
call_8052 = relay.TupleGetItem(func_3341_call(relay.reshape(const_8050.astype('bool'), [490,]), relay.reshape(var_8051.astype('float64'), [88, 1]), ), 4)
output = relay.Tuple([call_8044,call_8046,var_8047,call_8049,const_8050,var_8051,])
output2 = relay.Tuple([call_8045,call_8048,var_8047,call_8052,const_8050,var_8051,])
func_8053 = relay.Function([var_8047,var_8051,], output)
mod['func_8053'] = func_8053
mod = relay.transform.InferType()(mod)
var_8054 = relay.var("var_8054", dtype = "float64", shape = (5, 28))#candidate|8054|(5, 28)|var|float64
var_8055 = relay.var("var_8055", dtype = "float64", shape = (88,))#candidate|8055|(88,)|var|float64
output = func_8053(var_8054,var_8055,)
func_8056 = relay.Function([var_8054,var_8055,], output)
mutated_mod['func_8056'] = func_8056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5433_call = mod.get_global_var('func_5433')
func_5435_call = mutated_mod.get_global_var('func_5435')
call_8084 = func_5433_call()
call_8085 = func_5433_call()
output = call_8084
output2 = call_8085
func_8092 = relay.Function([], output)
mod['func_8092'] = func_8092
mod = relay.transform.InferType()(mod)
output = func_8092()
func_8093 = relay.Function([], output)
mutated_mod['func_8093'] = func_8093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4497_call = mod.get_global_var('func_4497')
func_4498_call = mutated_mod.get_global_var('func_4498')
call_8120 = relay.TupleGetItem(func_4497_call(), 0)
call_8121 = relay.TupleGetItem(func_4498_call(), 0)
func_7446_call = mod.get_global_var('func_7446')
func_7449_call = mutated_mod.get_global_var('func_7449')
var_8123 = relay.var("var_8123", dtype = "uint16", shape = (352,))#candidate|8123|(352,)|var|uint16
var_8124 = relay.var("var_8124", dtype = "bool", shape = (1, 140))#candidate|8124|(1, 140)|var|bool
call_8122 = relay.TupleGetItem(func_7446_call(relay.reshape(var_8123.astype('uint16'), [352,]), relay.reshape(var_8124.astype('bool'), [140,]), ), 0)
call_8125 = relay.TupleGetItem(func_7449_call(relay.reshape(var_8123.astype('uint16'), [352,]), relay.reshape(var_8124.astype('bool'), [140,]), ), 0)
output = relay.Tuple([call_8120,call_8122,var_8123,var_8124,])
output2 = relay.Tuple([call_8121,call_8125,var_8123,var_8124,])
func_8134 = relay.Function([var_8123,var_8124,], output)
mod['func_8134'] = func_8134
mod = relay.transform.InferType()(mod)
mutated_mod['func_8134'] = func_8134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8134_call = mutated_mod.get_global_var('func_8134')
var_8136 = relay.var("var_8136", dtype = "uint16", shape = (352,))#candidate|8136|(352,)|var|uint16
var_8137 = relay.var("var_8137", dtype = "bool", shape = (1, 140))#candidate|8137|(1, 140)|var|bool
call_8135 = func_8134_call(var_8136,var_8137,)
output = call_8135
func_8138 = relay.Function([var_8136,var_8137,], output)
mutated_mod['func_8138'] = func_8138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6779_call = mod.get_global_var('func_6779')
func_6781_call = mutated_mod.get_global_var('func_6781')
call_8229 = func_6779_call()
call_8230 = func_6779_call()
func_3017_call = mod.get_global_var('func_3017')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_8250 = func_3017_call()
call_8251 = func_3017_call()
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_8253 = relay.TupleGetItem(func_6597_call(), 0)
call_8254 = relay.TupleGetItem(func_6599_call(), 0)
output = relay.Tuple([call_8229,call_8250,call_8253,])
output2 = relay.Tuple([call_8230,call_8251,call_8254,])
func_8264 = relay.Function([], output)
mod['func_8264'] = func_8264
mod = relay.transform.InferType()(mod)
mutated_mod['func_8264'] = func_8264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8264_call = mutated_mod.get_global_var('func_8264')
call_8265 = func_8264_call()
output = call_8265
func_8266 = relay.Function([], output)
mutated_mod['func_8266'] = func_8266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4248_call = mod.get_global_var('func_4248')
func_4250_call = mutated_mod.get_global_var('func_4250')
call_8296 = relay.TupleGetItem(func_4248_call(), 0)
call_8297 = relay.TupleGetItem(func_4250_call(), 0)
var_8301 = relay.var("var_8301", dtype = "float32", shape = (352, 15))#candidate|8301|(352, 15)|var|float32
bop_8302 = relay.not_equal(call_8296.astype('bool'), var_8301.astype('bool')) # shape=(352, 15)
bop_8305 = relay.not_equal(call_8297.astype('bool'), var_8301.astype('bool')) # shape=(352, 15)
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_8314 = relay.TupleGetItem(func_6597_call(), 0)
call_8315 = relay.TupleGetItem(func_6599_call(), 0)
uop_8322 = relay.sigmoid(call_8296.astype('float32')) # shape=(352, 1)
uop_8324 = relay.sigmoid(call_8297.astype('float32')) # shape=(352, 1)
uop_8341 = relay.log10(uop_8322.astype('float64')) # shape=(352, 1)
uop_8343 = relay.log10(uop_8324.astype('float64')) # shape=(352, 1)
output = relay.Tuple([bop_8302,call_8314,uop_8341,])
output2 = relay.Tuple([bop_8305,call_8315,uop_8343,])
func_8345 = relay.Function([var_8301,], output)
mod['func_8345'] = func_8345
mod = relay.transform.InferType()(mod)
mutated_mod['func_8345'] = func_8345
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8346 = relay.var("var_8346", dtype = "float32", shape = (352, 15))#candidate|8346|(352, 15)|var|float32
func_8345_call = mutated_mod.get_global_var('func_8345')
call_8347 = func_8345_call(var_8346)
output = call_8347
func_8348 = relay.Function([var_8346], output)
mutated_mod['func_8348'] = func_8348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8264_call = mod.get_global_var('func_8264')
func_8266_call = mutated_mod.get_global_var('func_8266')
call_8361 = relay.TupleGetItem(func_8264_call(), 1)
call_8362 = relay.TupleGetItem(func_8266_call(), 1)
output = relay.Tuple([call_8361,])
output2 = relay.Tuple([call_8362,])
func_8389 = relay.Function([], output)
mod['func_8389'] = func_8389
mod = relay.transform.InferType()(mod)
mutated_mod['func_8389'] = func_8389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8389_call = mutated_mod.get_global_var('func_8389')
call_8390 = func_8389_call()
output = call_8390
func_8391 = relay.Function([], output)
mutated_mod['func_8391'] = func_8391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_8440 = relay.TupleGetItem(func_2698_call(), 0)
call_8441 = relay.TupleGetItem(func_2700_call(), 0)
output = relay.Tuple([call_8440,])
output2 = relay.Tuple([call_8441,])
func_8450 = relay.Function([], output)
mod['func_8450'] = func_8450
mod = relay.transform.InferType()(mod)
mutated_mod['func_8450'] = func_8450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8450_call = mutated_mod.get_global_var('func_8450')
call_8451 = func_8450_call()
output = call_8451
func_8452 = relay.Function([], output)
mutated_mod['func_8452'] = func_8452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8092_call = mod.get_global_var('func_8092')
func_8093_call = mutated_mod.get_global_var('func_8093')
call_8503 = func_8092_call()
call_8504 = func_8092_call()
var_8506 = relay.var("var_8506", dtype = "float64", shape = (352, 5))#candidate|8506|(352, 5)|var|float64
bop_8507 = relay.left_shift(call_8503.astype('int32'), relay.reshape(var_8506.astype('int32'), relay.shape_of(call_8503))) # shape=(352, 5)
bop_8510 = relay.left_shift(call_8504.astype('int32'), relay.reshape(var_8506.astype('int32'), relay.shape_of(call_8504))) # shape=(352, 5)
bop_8512 = relay.power(var_8506.astype('float64'), relay.reshape(bop_8507.astype('float64'), relay.shape_of(var_8506))) # shape=(352, 5)
bop_8515 = relay.power(var_8506.astype('float64'), relay.reshape(bop_8510.astype('float64'), relay.shape_of(var_8506))) # shape=(352, 5)
func_4751_call = mod.get_global_var('func_4751')
func_4753_call = mutated_mod.get_global_var('func_4753')
call_8516 = func_4751_call()
call_8517 = func_4751_call()
output = relay.Tuple([bop_8512,call_8516,])
output2 = relay.Tuple([bop_8515,call_8517,])
func_8521 = relay.Function([var_8506,], output)
mod['func_8521'] = func_8521
mod = relay.transform.InferType()(mod)
var_8522 = relay.var("var_8522", dtype = "float64", shape = (352, 5))#candidate|8522|(352, 5)|var|float64
output = func_8521(var_8522)
func_8523 = relay.Function([var_8522], output)
mutated_mod['func_8523'] = func_8523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5863_call = mod.get_global_var('func_5863')
func_5865_call = mutated_mod.get_global_var('func_5865')
call_8550 = relay.TupleGetItem(func_5863_call(), 0)
call_8551 = relay.TupleGetItem(func_5865_call(), 0)
output = relay.Tuple([call_8550,])
output2 = relay.Tuple([call_8551,])
func_8570 = relay.Function([], output)
mod['func_8570'] = func_8570
mod = relay.transform.InferType()(mod)
output = func_8570()
func_8571 = relay.Function([], output)
mutated_mod['func_8571'] = func_8571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7284_call = mod.get_global_var('func_7284')
func_7285_call = mutated_mod.get_global_var('func_7285')
call_8611 = relay.TupleGetItem(func_7284_call(), 0)
call_8612 = relay.TupleGetItem(func_7285_call(), 0)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_8625 = relay.TupleGetItem(func_2773_call(), 1)
call_8626 = relay.TupleGetItem(func_2775_call(), 1)
func_3337_call = mod.get_global_var('func_3337')
func_3341_call = mutated_mod.get_global_var('func_3341')
var_8629 = relay.var("var_8629", dtype = "bool", shape = (490,))#candidate|8629|(490,)|var|bool
var_8630 = relay.var("var_8630", dtype = "float64", shape = (88,))#candidate|8630|(88,)|var|float64
call_8628 = relay.TupleGetItem(func_3337_call(relay.reshape(var_8629.astype('bool'), [490,]), relay.reshape(var_8630.astype('float64'), [88, 1]), ), 2)
call_8631 = relay.TupleGetItem(func_3341_call(relay.reshape(var_8629.astype('bool'), [490,]), relay.reshape(var_8630.astype('float64'), [88, 1]), ), 2)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_8634 = relay.TupleGetItem(func_2773_call(), 1)
call_8635 = relay.TupleGetItem(func_2775_call(), 1)
func_7966_call = mod.get_global_var('func_7966')
func_7968_call = mutated_mod.get_global_var('func_7968')
var_8639 = relay.var("var_8639", dtype = "bool", shape = (140,))#candidate|8639|(140,)|var|bool
call_8638 = relay.TupleGetItem(func_7966_call(relay.reshape(var_8639.astype('bool'), [140,])), 2)
call_8640 = relay.TupleGetItem(func_7968_call(relay.reshape(var_8639.astype('bool'), [140,])), 2)
output = relay.Tuple([call_8611,call_8625,call_8628,var_8629,var_8630,call_8634,call_8638,var_8639,])
output2 = relay.Tuple([call_8612,call_8626,call_8631,var_8629,var_8630,call_8635,call_8640,var_8639,])
func_8647 = relay.Function([var_8629,var_8630,var_8639,], output)
mod['func_8647'] = func_8647
mod = relay.transform.InferType()(mod)
var_8648 = relay.var("var_8648", dtype = "bool", shape = (490,))#candidate|8648|(490,)|var|bool
var_8649 = relay.var("var_8649", dtype = "float64", shape = (88,))#candidate|8649|(88,)|var|float64
var_8650 = relay.var("var_8650", dtype = "bool", shape = (140,))#candidate|8650|(140,)|var|bool
output = func_8647(var_8648,var_8649,var_8650,)
func_8651 = relay.Function([var_8648,var_8649,var_8650,], output)
mutated_mod['func_8651'] = func_8651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6473_call = mod.get_global_var('func_6473')
func_6474_call = mutated_mod.get_global_var('func_6474')
call_8673 = relay.TupleGetItem(func_6473_call(), 1)
call_8674 = relay.TupleGetItem(func_6474_call(), 1)
output = call_8673
output2 = call_8674
func_8703 = relay.Function([], output)
mod['func_8703'] = func_8703
mod = relay.transform.InferType()(mod)
output = func_8703()
func_8704 = relay.Function([], output)
mutated_mod['func_8704'] = func_8704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7591_call = mod.get_global_var('func_7591')
func_7592_call = mutated_mod.get_global_var('func_7592')
call_8778 = relay.TupleGetItem(func_7591_call(), 1)
call_8779 = relay.TupleGetItem(func_7592_call(), 1)
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_8788 = func_4803_call()
call_8789 = func_4803_call()
output = relay.Tuple([call_8778,call_8788,])
output2 = relay.Tuple([call_8779,call_8789,])
func_8790 = relay.Function([], output)
mod['func_8790'] = func_8790
mod = relay.transform.InferType()(mod)
output = func_8790()
func_8791 = relay.Function([], output)
mutated_mod['func_8791'] = func_8791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3017_call = mod.get_global_var('func_3017')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_8845 = func_3017_call()
call_8846 = func_3017_call()
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_8863 = relay.TupleGetItem(func_6597_call(), 0)
call_8864 = relay.TupleGetItem(func_6599_call(), 0)
output = relay.Tuple([call_8845,call_8863,])
output2 = relay.Tuple([call_8846,call_8864,])
func_8877 = relay.Function([], output)
mod['func_8877'] = func_8877
mod = relay.transform.InferType()(mod)
output = func_8877()
func_8878 = relay.Function([], output)
mutated_mod['func_8878'] = func_8878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3017_call = mod.get_global_var('func_3017')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_8898 = func_3017_call()
call_8899 = func_3017_call()
output = relay.Tuple([call_8898,])
output2 = relay.Tuple([call_8899,])
func_8904 = relay.Function([], output)
mod['func_8904'] = func_8904
mod = relay.transform.InferType()(mod)
mutated_mod['func_8904'] = func_8904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8904_call = mutated_mod.get_global_var('func_8904')
call_8905 = func_8904_call()
output = call_8905
func_8906 = relay.Function([], output)
mutated_mod['func_8906'] = func_8906
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8945 = relay.const([[[-4.310469,-5.938537,9.315623,-1.610271,-7.821648,-5.864708,7.044151,-2.437136,-5.953153,4.346810,-3.720816,-2.854138]],[[2.137043,9.581277,-1.405046,4.136678,-9.277134,-7.500674,-3.088496,-0.510894,-6.468567,7.774026,3.020084,1.909187]],[[9.370072,-5.201357,3.776792,8.945948,2.496700,-2.035305,9.542296,-3.073302,1.927828,5.322734,7.351072,-9.296349]],[[6.538237,2.247747,-3.498044,-3.830523,-3.056355,9.382397,-1.181285,-8.246172,9.836097,9.774697,8.677840,-0.102896]],[[7.997076,-7.155341,-7.420483,-8.846159,4.601302,-3.489520,-1.504275,6.145773,-6.875884,-3.764080,1.005980,-6.500929]],[[0.837626,3.023084,6.428191,-5.065015,-8.966893,-4.222800,9.471759,-6.276705,-0.906347,-0.642441,6.327213,9.586383]],[[-3.110596,-8.777571,3.616822,8.381075,3.264039,7.088005,-6.205773,2.575839,-3.432579,1.900016,-8.197208,-2.786269]],[[9.842631,9.179152,-4.808070,-2.072698,9.032901,-6.067704,1.075676,4.619732,1.426246,5.738652,-4.089134,-7.038257]],[[-2.631859,8.878627,2.818040,-8.620134,-7.113163,0.508256,-2.005649,-6.147110,7.172913,-8.534186,-7.564883,5.510830]]], dtype = "float32")#candidate|8945|(9, 1, 12)|const|float32
uop_8946 = relay.rsqrt(const_8945.astype('float32')) # shape=(9, 1, 12)
bop_8956 = relay.not_equal(uop_8946.astype('bool'), relay.reshape(const_8945.astype('bool'), relay.shape_of(uop_8946))) # shape=(9, 1, 12)
bop_8972 = relay.right_shift(uop_8946.astype('uint8'), relay.reshape(bop_8956.astype('uint8'), relay.shape_of(uop_8946))) # shape=(9, 1, 12)
output = relay.Tuple([bop_8972,])
output2 = relay.Tuple([bop_8972,])
func_8977 = relay.Function([], output)
mod['func_8977'] = func_8977
mod = relay.transform.InferType()(mod)
mutated_mod['func_8977'] = func_8977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8977_call = mutated_mod.get_global_var('func_8977')
call_8978 = func_8977_call()
output = call_8978
func_8979 = relay.Function([], output)
mutated_mod['func_8979'] = func_8979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6643_call = mod.get_global_var('func_6643')
func_6645_call = mutated_mod.get_global_var('func_6645')
call_9044 = relay.TupleGetItem(func_6643_call(), 0)
call_9045 = relay.TupleGetItem(func_6645_call(), 0)
func_8134_call = mod.get_global_var('func_8134')
func_8138_call = mutated_mod.get_global_var('func_8138')
const_9047 = relay.const([True,False,True,True,True,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True], dtype = "bool")#candidate|9047|(140,)|const|bool
call_9046 = relay.TupleGetItem(func_8134_call(relay.reshape(call_9044.astype('uint16'), [352,]), relay.reshape(const_9047.astype('bool'), [1, 140]), ), 0)
call_9048 = relay.TupleGetItem(func_8138_call(relay.reshape(call_9044.astype('uint16'), [352,]), relay.reshape(const_9047.astype('bool'), [1, 140]), ), 0)
func_5926_call = mod.get_global_var('func_5926')
func_5927_call = mutated_mod.get_global_var('func_5927')
call_9053 = func_5926_call()
call_9054 = func_5926_call()
output = relay.Tuple([call_9044,call_9046,const_9047,call_9053,])
output2 = relay.Tuple([call_9045,call_9048,const_9047,call_9054,])
func_9057 = relay.Function([], output)
mod['func_9057'] = func_9057
mod = relay.transform.InferType()(mod)
output = func_9057()
func_9058 = relay.Function([], output)
mutated_mod['func_9058'] = func_9058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_9109 = relay.TupleGetItem(func_6597_call(), 0)
call_9110 = relay.TupleGetItem(func_6599_call(), 0)
func_7772_call = mod.get_global_var('func_7772')
func_7776_call = mutated_mod.get_global_var('func_7776')
const_9117 = relay.const(-3, dtype = "uint16")#candidate|9117|()|const|uint16
var_9118 = relay.var("var_9118", dtype = "uint16", shape = (48,))#candidate|9118|(48,)|var|uint16
call_9116 = relay.TupleGetItem(func_7772_call(relay.reshape(const_9117.astype('uint16'), []), relay.reshape(var_9118.astype('uint16'), [16, 3, 1]), ), 1)
call_9119 = relay.TupleGetItem(func_7776_call(relay.reshape(const_9117.astype('uint16'), []), relay.reshape(var_9118.astype('uint16'), [16, 3, 1]), ), 1)
output = relay.Tuple([call_9109,call_9116,const_9117,var_9118,])
output2 = relay.Tuple([call_9110,call_9119,const_9117,var_9118,])
func_9123 = relay.Function([var_9118,], output)
mod['func_9123'] = func_9123
mod = relay.transform.InferType()(mod)
var_9124 = relay.var("var_9124", dtype = "uint16", shape = (48,))#candidate|9124|(48,)|var|uint16
output = func_9123(var_9124)
func_9125 = relay.Function([var_9124], output)
mutated_mod['func_9125'] = func_9125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3836_call = mod.get_global_var('func_3836')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_9144 = relay.TupleGetItem(func_3836_call(), 0)
call_9145 = relay.TupleGetItem(func_3838_call(), 0)
output = relay.Tuple([call_9144,])
output2 = relay.Tuple([call_9145,])
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
func_6007_call = mod.get_global_var('func_6007')
func_6008_call = mutated_mod.get_global_var('func_6008')
call_9170 = relay.TupleGetItem(func_6007_call(), 0)
call_9171 = relay.TupleGetItem(func_6008_call(), 0)
func_8450_call = mod.get_global_var('func_8450')
func_8452_call = mutated_mod.get_global_var('func_8452')
call_9191 = relay.TupleGetItem(func_8450_call(), 0)
call_9192 = relay.TupleGetItem(func_8452_call(), 0)
output = relay.Tuple([call_9170,call_9191,])
output2 = relay.Tuple([call_9171,call_9192,])
func_9200 = relay.Function([], output)
mod['func_9200'] = func_9200
mod = relay.transform.InferType()(mod)
output = func_9200()
func_9201 = relay.Function([], output)
mutated_mod['func_9201'] = func_9201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5044_call = mod.get_global_var('func_5044')
func_5045_call = mutated_mod.get_global_var('func_5045')
call_9223 = relay.TupleGetItem(func_5044_call(), 0)
call_9224 = relay.TupleGetItem(func_5045_call(), 0)
output = relay.Tuple([call_9223,])
output2 = relay.Tuple([call_9224,])
func_9238 = relay.Function([], output)
mod['func_9238'] = func_9238
mod = relay.transform.InferType()(mod)
output = func_9238()
func_9239 = relay.Function([], output)
mutated_mod['func_9239'] = func_9239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_9240 = func_3961_call()
call_9241 = func_3961_call()
func_4751_call = mod.get_global_var('func_4751')
func_4753_call = mutated_mod.get_global_var('func_4753')
call_9261 = func_4751_call()
call_9262 = func_4751_call()
output = relay.Tuple([call_9240,call_9261,])
output2 = relay.Tuple([call_9241,call_9262,])
func_9266 = relay.Function([], output)
mod['func_9266'] = func_9266
mod = relay.transform.InferType()(mod)
mutated_mod['func_9266'] = func_9266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9266_call = mutated_mod.get_global_var('func_9266')
call_9267 = func_9266_call()
output = call_9267
func_9268 = relay.Function([], output)
mutated_mod['func_9268'] = func_9268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8877_call = mod.get_global_var('func_8877')
func_8878_call = mutated_mod.get_global_var('func_8878')
call_9288 = relay.TupleGetItem(func_8877_call(), 1)
call_9289 = relay.TupleGetItem(func_8878_call(), 1)
output = relay.Tuple([call_9288,])
output2 = relay.Tuple([call_9289,])
func_9305 = relay.Function([], output)
mod['func_9305'] = func_9305
mod = relay.transform.InferType()(mod)
output = func_9305()
func_9306 = relay.Function([], output)
mutated_mod['func_9306'] = func_9306
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9315 = relay.var("var_9315", dtype = "float64", shape = (8, 10, 8))#candidate|9315|(8, 10, 8)|var|float64
uop_9316 = relay.sin(var_9315.astype('float64')) # shape=(8, 10, 8)
uop_9321 = relay.acos(var_9315.astype('float32')) # shape=(8, 10, 8)
output = relay.Tuple([uop_9316,uop_9321,])
output2 = relay.Tuple([uop_9316,uop_9321,])
func_9328 = relay.Function([var_9315,], output)
mod['func_9328'] = func_9328
mod = relay.transform.InferType()(mod)
mutated_mod['func_9328'] = func_9328
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9329 = relay.var("var_9329", dtype = "float64", shape = (8, 10, 8))#candidate|9329|(8, 10, 8)|var|float64
func_9328_call = mutated_mod.get_global_var('func_9328')
call_9330 = func_9328_call(var_9329)
output = call_9330
func_9331 = relay.Function([var_9329], output)
mutated_mod['func_9331'] = func_9331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6643_call = mod.get_global_var('func_6643')
func_6645_call = mutated_mod.get_global_var('func_6645')
call_9336 = relay.TupleGetItem(func_6643_call(), 0)
call_9337 = relay.TupleGetItem(func_6645_call(), 0)
output = call_9336
output2 = call_9337
func_9348 = relay.Function([], output)
mod['func_9348'] = func_9348
mod = relay.transform.InferType()(mod)
mutated_mod['func_9348'] = func_9348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9348_call = mutated_mod.get_global_var('func_9348')
call_9349 = func_9348_call()
output = call_9349
func_9350 = relay.Function([], output)
mutated_mod['func_9350'] = func_9350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_9436 = func_3961_call()
call_9437 = func_3961_call()
func_9328_call = mod.get_global_var('func_9328')
func_9331_call = mutated_mod.get_global_var('func_9331')
const_9464 = relay.const([[-6.627435,-6.113967],[-6.979568,-1.978248],[8.688312,3.366074],[0.440032,1.712776],[4.786222,5.597531],[-3.793136,-9.800350],[-9.564346,-0.145292],[-1.781215,-1.835854],[-3.118190,9.791960],[-4.853276,-5.431552],[3.010292,-9.398638],[-2.679360,-0.244943],[-1.852468,4.997544],[6.058339,-8.077651],[7.927747,8.991123],[9.450384,-3.304950],[-4.032031,3.025529],[7.147630,5.520805],[4.327652,0.209486],[1.247279,-5.584898],[-6.942491,-3.132568],[9.969483,1.800381],[2.651433,-4.745890],[-4.627762,1.829002],[-4.124159,1.531042],[-5.959699,-1.354118],[8.167471,8.711755],[2.946312,-1.275758],[5.622759,-8.470740],[-4.904170,0.114954],[-3.279568,-9.074225],[-3.692508,8.266603],[-5.077046,-1.951700],[4.211901,6.269019],[-8.545005,2.451788],[-0.292071,8.828023],[0.712787,-9.489849],[0.498592,9.080914],[1.144261,-3.717314],[1.730793,2.522123],[3.659329,-8.389166],[-4.894558,8.862295],[-9.378539,1.414867],[-5.274855,-4.838293],[-4.507103,6.497615],[-7.211171,2.374793],[8.451931,9.850882],[6.306521,-3.387015],[-9.192097,-7.733965],[-4.282757,-8.435427],[-0.139896,5.794530],[-2.741315,-8.710846],[-6.154923,6.360212],[1.751827,3.683074],[-4.159308,4.487155],[9.669752,-2.545196],[1.777765,-0.947775],[-3.914419,-6.801872],[-2.388595,-6.695030],[-7.910163,7.839830],[-6.720448,5.320491],[4.973226,-9.906556],[-6.292253,-4.651371],[-1.503692,3.232748],[3.795136,6.300147],[-8.460507,-7.900267],[-6.405716,-9.858244],[-1.238859,4.781265],[-3.152712,-8.708987],[5.345777,4.188171],[-7.951110,0.026261],[2.178901,-0.498710],[9.410046,-8.108222],[-4.704730,-7.373055],[0.699252,9.829334],[7.540753,8.501916],[6.532563,5.229688],[-5.470528,-7.614940],[-1.746856,4.359682],[8.672924,-4.551921],[-9.012325,-9.436710],[-7.713489,1.215036],[3.304924,3.962769],[8.358770,-6.865457],[-7.239442,-5.580118],[6.120953,2.990554],[-4.685162,8.996478],[5.705450,-6.386574],[-9.157207,-2.674107],[-3.635290,0.394454],[-0.792442,-3.242289],[0.421744,-9.526966],[-9.972224,-6.311505],[-1.672910,-5.102229],[7.202968,-3.657994],[9.881738,-3.551051],[6.488422,-1.148289],[-1.617499,-5.825007],[-5.304845,-0.059540],[3.601207,4.343917],[3.007836,2.523365],[-4.657026,5.927706],[0.199755,-4.918484],[-3.037679,6.829223],[7.378065,5.527009],[0.182469,-8.446206],[-3.445847,0.841361],[7.563352,-3.409035],[-6.189043,-8.580848],[8.585032,-1.606490],[2.500367,1.904551],[5.449385,-6.384037],[8.646715,-2.407143],[8.888757,-5.296146],[-7.102901,9.786109],[6.823867,-7.654356],[-4.596123,-8.780616],[-0.654404,-8.231812],[5.506361,-2.910152],[-0.105883,4.572414],[-4.883187,-0.185852],[-8.189441,-6.139068],[-7.592770,-9.683688],[0.836522,-2.224543],[-4.596088,2.082516],[8.906462,-2.426090],[6.112978,-3.699586],[0.054440,3.040887],[1.643840,8.188473],[3.558471,-4.811012],[-5.638887,3.765319],[-1.594388,1.679381],[-4.339391,5.252768],[-2.047008,-6.219425],[-1.677225,-5.092934],[-0.780273,-8.385129],[1.006416,5.208929],[5.930770,4.291118],[-0.991226,3.770960],[-1.299479,5.132674],[7.030865,-6.875203],[4.629934,5.558012],[4.876946,6.043335],[-4.343699,-1.869474],[-7.603517,-3.124364],[5.395082,3.834646],[-0.841905,-2.444738],[8.776756,1.140483],[0.876383,-3.554202],[-9.201765,-3.768222],[3.357691,4.312453],[8.724441,-9.671295],[9.591637,5.145348],[-2.219721,-1.796834],[5.619405,8.666072],[4.716590,9.840912],[-6.750896,5.496359],[-9.551041,8.388000],[6.517418,7.636073],[-1.017351,-0.145975],[-9.171199,-0.736001],[-0.241778,1.907992],[-7.346266,-5.709837],[6.127480,-8.867914],[-5.672460,-6.013441],[3.293874,-9.082883],[-4.561222,-3.936536],[6.444699,-1.643093],[-0.944552,-1.739198],[7.561723,4.318821],[-9.707309,6.498167],[2.428506,-4.234831],[5.324722,-1.087789],[-5.351446,-5.246992],[-6.913028,1.861077],[8.678019,2.848981],[-5.470851,6.723672],[3.788238,3.875609],[-3.631481,9.208638],[-2.046676,8.170316],[-4.474993,7.692328],[1.494998,7.462776],[-5.057089,4.104605],[-4.942102,0.322437],[1.840744,3.641076],[6.511789,-2.718918],[3.815398,-1.162266],[8.981704,-1.097123],[1.103548,-6.322515],[0.013993,2.077610],[-9.641589,8.191238],[8.878629,-4.901709],[4.691868,-5.924591],[-0.050609,5.952083],[-6.755164,-4.657481],[7.610294,-7.614261],[-6.953623,9.486644],[-4.269751,1.617721],[-1.844345,-5.278543],[3.465216,-7.719392],[-0.430493,-0.840068],[8.945792,-4.603449],[8.795165,-8.094276],[1.289976,6.877308],[2.352061,5.779822],[6.328036,1.280125],[-2.037001,-1.294662],[-9.637196,-9.519722],[0.626558,2.813327],[-0.820678,-0.912543],[-4.523677,3.217354],[2.666674,4.325324],[9.491688,4.932053],[0.216359,-8.549380],[-5.279815,-8.509214],[7.574992,0.681546],[3.861757,-3.296757],[-5.478251,9.614795],[8.606849,7.781213],[4.629983,3.053487],[0.061152,-2.130413],[3.454977,-4.312511],[3.622489,-4.205358],[-3.763934,6.595118],[7.959220,8.187342],[-9.164984,-8.365693],[7.807107,6.329850],[6.208274,-1.995365],[6.812343,3.418538],[6.136788,-2.634307],[-8.639385,-6.331125],[-9.003575,-2.397457],[8.444852,8.797450],[-0.237265,1.338588],[9.937826,8.847457],[2.703088,-2.585060],[-0.477758,-5.234994],[0.033830,-5.978758],[1.214824,-2.051619],[-4.172531,6.156562],[5.047331,1.697380],[5.344034,5.011955],[5.511893,0.179015],[-6.239307,0.856069],[4.369362,2.056215],[-4.185719,6.661060],[-9.539494,8.328633],[-6.571319,-5.198457],[-0.314739,-5.935477],[-4.289989,-2.612967],[-4.908166,-0.448129],[6.218896,1.129713],[8.997183,-9.111206],[-4.980619,-0.354394],[2.992145,9.490280],[-2.755394,7.660770],[1.073693,-0.513303],[-7.968827,-5.257711],[-1.562341,5.444770],[-3.308617,8.474019],[3.277006,-5.457463],[3.364567,-2.168025],[-2.904723,-9.194348],[5.432910,8.070789],[1.586511,-7.598236],[8.336681,-9.756831],[-1.628568,0.086823],[-2.350888,-5.431095],[-8.214086,7.841052],[9.659649,3.834959],[7.286362,1.854432],[0.950995,-1.666942],[-4.065832,-6.511850],[3.353266,-9.957875],[7.942877,-9.728351],[-9.249808,5.844188],[1.597383,-9.928162],[7.858219,9.365382],[9.826068,4.869579],[6.111950,-1.149573],[7.641781,9.635141],[7.615506,-5.168152],[-9.457084,8.183573],[0.542220,0.587413],[5.164837,-9.852566],[7.875723,-9.519619],[-5.399444,-7.613926],[2.456671,7.075357],[5.728477,1.371140],[-5.129924,3.946093],[-4.608608,1.402522],[-5.696158,4.879564],[-1.188992,-0.782944],[6.975147,1.989077],[-3.218778,1.572026],[-9.994410,-3.673149],[-8.031367,-1.535456],[1.155947,9.782537],[-1.399556,-8.935075],[3.195455,5.848145],[9.201376,-1.202530],[-2.894281,-6.035357],[0.212977,-4.112611],[-4.206639,5.547789],[-9.297077,-3.786044],[-3.074063,5.731769],[-7.655091,9.404525],[7.632445,-6.827461],[-2.248344,7.964975],[-6.277477,8.223154],[-3.438234,5.107121],[1.731983,6.325193],[-2.548130,1.229478],[2.257101,-5.465428],[-4.516759,2.290728],[-4.412438,-7.903736],[-4.735637,9.139539],[3.151097,-6.762742],[-6.146008,1.037950],[8.471222,7.948518]], dtype = "float64")#candidate|9464|(320, 2)|const|float64
call_9463 = relay.TupleGetItem(func_9328_call(relay.reshape(const_9464.astype('float64'), [8, 10, 8])), 0)
call_9465 = relay.TupleGetItem(func_9331_call(relay.reshape(const_9464.astype('float64'), [8, 10, 8])), 0)
func_3718_call = mod.get_global_var('func_3718')
func_3721_call = mutated_mod.get_global_var('func_3721')
var_9480 = relay.var("var_9480", dtype = "float32", shape = (32, 4))#candidate|9480|(32, 4)|var|float32
call_9479 = relay.TupleGetItem(func_3718_call(relay.reshape(var_9480.astype('float32'), [128,])), 1)
call_9481 = relay.TupleGetItem(func_3721_call(relay.reshape(var_9480.astype('float32'), [128,])), 1)
uop_9494 = relay.atan(call_9479.astype('float64')) # shape=(8, 6, 16)
uop_9496 = relay.atan(call_9481.astype('float64')) # shape=(8, 6, 16)
output = relay.Tuple([call_9436,call_9463,const_9464,var_9480,uop_9494,])
output2 = relay.Tuple([call_9437,call_9465,const_9464,var_9480,uop_9496,])
func_9497 = relay.Function([var_9480,], output)
mod['func_9497'] = func_9497
mod = relay.transform.InferType()(mod)
var_9498 = relay.var("var_9498", dtype = "float32", shape = (32, 4))#candidate|9498|(32, 4)|var|float32
output = func_9497(var_9498)
func_9499 = relay.Function([var_9498], output)
mutated_mod['func_9499'] = func_9499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3385_call = mod.get_global_var('func_3385')
func_3387_call = mutated_mod.get_global_var('func_3387')
call_9507 = relay.TupleGetItem(func_3385_call(), 0)
call_9508 = relay.TupleGetItem(func_3387_call(), 0)
func_7966_call = mod.get_global_var('func_7966')
func_7968_call = mutated_mod.get_global_var('func_7968')
const_9524 = relay.const([True,True,True,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False], dtype = "bool")#candidate|9524|(140,)|const|bool
call_9523 = relay.TupleGetItem(func_7966_call(relay.reshape(const_9524.astype('bool'), [140,])), 1)
call_9525 = relay.TupleGetItem(func_7968_call(relay.reshape(const_9524.astype('bool'), [140,])), 1)
output = relay.Tuple([call_9507,call_9523,const_9524,])
output2 = relay.Tuple([call_9508,call_9525,const_9524,])
func_9528 = relay.Function([], output)
mod['func_9528'] = func_9528
mod = relay.transform.InferType()(mod)
mutated_mod['func_9528'] = func_9528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9528_call = mutated_mod.get_global_var('func_9528')
call_9529 = func_9528_call()
output = call_9529
func_9530 = relay.Function([], output)
mutated_mod['func_9530'] = func_9530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9266_call = mod.get_global_var('func_9266')
func_9268_call = mutated_mod.get_global_var('func_9268')
call_9593 = relay.TupleGetItem(func_9266_call(), 0)
call_9594 = relay.TupleGetItem(func_9268_call(), 0)
output = call_9593
output2 = call_9594
func_9597 = relay.Function([], output)
mod['func_9597'] = func_9597
mod = relay.transform.InferType()(mod)
output = func_9597()
func_9598 = relay.Function([], output)
mutated_mod['func_9598'] = func_9598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6940_call = mod.get_global_var('func_6940')
func_6942_call = mutated_mod.get_global_var('func_6942')
call_9635 = func_6940_call()
call_9636 = func_6940_call()
var_9650 = relay.var("var_9650", dtype = "bool", shape = (10, 2, 7))#candidate|9650|(10, 2, 7)|var|bool
bop_9651 = relay.bitwise_xor(call_9635.astype('int8'), var_9650.astype('int8')) # shape=(10, 2, 7)
bop_9654 = relay.bitwise_xor(call_9636.astype('int8'), var_9650.astype('int8')) # shape=(10, 2, 7)
output = relay.Tuple([bop_9651,])
output2 = relay.Tuple([bop_9654,])
func_9670 = relay.Function([var_9650,], output)
mod['func_9670'] = func_9670
mod = relay.transform.InferType()(mod)
var_9671 = relay.var("var_9671", dtype = "bool", shape = (10, 2, 7))#candidate|9671|(10, 2, 7)|var|bool
output = func_9670(var_9671)
func_9672 = relay.Function([var_9671], output)
mutated_mod['func_9672'] = func_9672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9305_call = mod.get_global_var('func_9305')
func_9306_call = mutated_mod.get_global_var('func_9306')
call_9746 = relay.TupleGetItem(func_9305_call(), 0)
call_9747 = relay.TupleGetItem(func_9306_call(), 0)
output = relay.Tuple([call_9746,])
output2 = relay.Tuple([call_9747,])
func_9753 = relay.Function([], output)
mod['func_9753'] = func_9753
mod = relay.transform.InferType()(mod)
output = func_9753()
func_9754 = relay.Function([], output)
mutated_mod['func_9754'] = func_9754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3836_call = mod.get_global_var('func_3836')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_9785 = relay.TupleGetItem(func_3836_call(), 0)
call_9786 = relay.TupleGetItem(func_3838_call(), 0)
func_5926_call = mod.get_global_var('func_5926')
func_5927_call = mutated_mod.get_global_var('func_5927')
call_9820 = func_5926_call()
call_9821 = func_5926_call()
func_4991_call = mod.get_global_var('func_4991')
func_4993_call = mutated_mod.get_global_var('func_4993')
var_9825 = relay.var("var_9825", dtype = "bool", shape = (140,))#candidate|9825|(140,)|var|bool
call_9824 = relay.TupleGetItem(func_4991_call(relay.reshape(var_9825.astype('bool'), [5, 28])), 2)
call_9826 = relay.TupleGetItem(func_4993_call(relay.reshape(var_9825.astype('bool'), [5, 28])), 2)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_9827 = relay.TupleGetItem(func_2773_call(), 1)
call_9828 = relay.TupleGetItem(func_2775_call(), 1)
uop_9837 = relay.erf(call_9827.astype('float64')) # shape=(4, 11, 8)
uop_9839 = relay.erf(call_9828.astype('float64')) # shape=(4, 11, 8)
func_8450_call = mod.get_global_var('func_8450')
func_8452_call = mutated_mod.get_global_var('func_8452')
call_9846 = relay.TupleGetItem(func_8450_call(), 0)
call_9847 = relay.TupleGetItem(func_8452_call(), 0)
bop_9850 = relay.greater(call_9824.astype('bool'), relay.reshape(call_9820.astype('bool'), relay.shape_of(call_9824))) # shape=(10, 1, 7)
bop_9853 = relay.greater(call_9826.astype('bool'), relay.reshape(call_9821.astype('bool'), relay.shape_of(call_9826))) # shape=(10, 1, 7)
bop_9857 = relay.bitwise_xor(uop_9837.astype('int8'), relay.reshape(call_9827.astype('int8'), relay.shape_of(uop_9837))) # shape=(4, 11, 8)
bop_9860 = relay.bitwise_xor(uop_9839.astype('int8'), relay.reshape(call_9828.astype('int8'), relay.shape_of(uop_9839))) # shape=(4, 11, 8)
func_9528_call = mod.get_global_var('func_9528')
func_9530_call = mutated_mod.get_global_var('func_9530')
call_9861 = relay.TupleGetItem(func_9528_call(), 1)
call_9862 = relay.TupleGetItem(func_9530_call(), 1)
output = relay.Tuple([call_9785,var_9825,call_9846,bop_9850,bop_9857,call_9861,])
output2 = relay.Tuple([call_9786,var_9825,call_9847,bop_9853,bop_9860,call_9862,])
func_9868 = relay.Function([var_9825,], output)
mod['func_9868'] = func_9868
mod = relay.transform.InferType()(mod)
mutated_mod['func_9868'] = func_9868
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9869 = relay.var("var_9869", dtype = "bool", shape = (140,))#candidate|9869|(140,)|var|bool
func_9868_call = mutated_mod.get_global_var('func_9868')
call_9870 = func_9868_call(var_9869)
output = call_9870
func_9871 = relay.Function([var_9869], output)
mutated_mod['func_9871'] = func_9871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7461_call = mod.get_global_var('func_7461')
func_7462_call = mutated_mod.get_global_var('func_7462')
call_9918 = relay.TupleGetItem(func_7461_call(), 0)
call_9919 = relay.TupleGetItem(func_7462_call(), 0)
func_7446_call = mod.get_global_var('func_7446')
func_7449_call = mutated_mod.get_global_var('func_7449')
const_9926 = relay.const([2,-8,-5,8,1,-1,-4,-10,1,-3,9,1,-9,-3,-10,10,-2,-9,-3,1,8,5,-8,6,-8,6,-4,7,-1,8,-1,-5,7,2,-10,-3,6,-2,-5,-6,1,10,10,7,-10,-7,3,5,-6,9,-3,4,-2,-6,9,10,5,-3,1,-8,-7,1,-7,-10,-7,-6,-3,10,1,10,9,9,-2,-8,-4,-4,-3,1,-5,-10,-9,-3,-9,6,2,-9,10,4,2,-6,10,7,7,3,8,4,-10,-10,1,-10,-5,-3,-8,-6,-1,-9,2,-6,6,1,-1,-1,-4,-1,-8,8,-1,-8,-8,-1,7,-1,8,10,-5,7,-7,-8,-9,8,1,1,-8,2,5,6,5,-3,-5,6,5,9,-10,-5,-7,8,-10,1,-8,-4,8,5,9,6,-10,-7,6,6,-2,-4,-3,-8,-1,-1,-4,4,-6,7,6,1,-6,10,4,-7,-9,7,5,-7,6,7,-4,4,-9,-7,-2,4,9,-1,2,-1,-1,4,-6,2,8,4,10,4,-6,-6,-3,8,6,7,9,10,-8,6,5,10,7,7,-9,-7,-4,-5,5,9,5,1,5,4,4,-1,-7,-2,2,-10,-2,6,-3,-3,6,-2,-9,5,-4,7,-8,-7,-9,9,-10,-2,7,-10,-1,-1,-6,-8,-7,7,3,-1,4,7,-9,-5,-5,-3,7,5,6,-4,2,-7,6,-2,2,1,-1,9,3,3,1,2,-1,5,-6,10,-3,-9,-3,-10,-4,10,9,7,3,2,8,-9,5,-6,5,1,5,6,10,-2,5,2,-3,-6,3,-10,3,7,5,9,9,5,9,-1,-7,5,-7,8,10,-4,-3,1,4,-6,-1,-9,4,-4,5,-3,-8,-6,7,-3,-7,7,1,-8,8,-6,-10,1,8,8,-1,-8,9,-4,-8,-3,-5,-9], dtype = "uint16")#candidate|9926|(352,)|const|uint16
var_9927 = relay.var("var_9927", dtype = "bool", shape = (140,))#candidate|9927|(140,)|var|bool
call_9925 = relay.TupleGetItem(func_7446_call(relay.reshape(const_9926.astype('uint16'), [352,]), relay.reshape(var_9927.astype('bool'), [140,]), ), 1)
call_9928 = relay.TupleGetItem(func_7449_call(relay.reshape(const_9926.astype('uint16'), [352,]), relay.reshape(var_9927.astype('bool'), [140,]), ), 1)
output = relay.Tuple([call_9918,call_9925,const_9926,var_9927,])
output2 = relay.Tuple([call_9919,call_9928,const_9926,var_9927,])
func_9936 = relay.Function([var_9927,], output)
mod['func_9936'] = func_9936
mod = relay.transform.InferType()(mod)
var_9937 = relay.var("var_9937", dtype = "bool", shape = (140,))#candidate|9937|(140,)|var|bool
output = func_9936(var_9937)
func_9938 = relay.Function([var_9937], output)
mutated_mod['func_9938'] = func_9938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6213_call = mod.get_global_var('func_6213')
func_6214_call = mutated_mod.get_global_var('func_6214')
call_9989 = relay.TupleGetItem(func_6213_call(), 0)
call_9990 = relay.TupleGetItem(func_6214_call(), 0)
func_3836_call = mod.get_global_var('func_3836')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_10002 = relay.TupleGetItem(func_3836_call(), 0)
call_10003 = relay.TupleGetItem(func_3838_call(), 0)
func_5863_call = mod.get_global_var('func_5863')
func_5865_call = mutated_mod.get_global_var('func_5865')
call_10005 = relay.TupleGetItem(func_5863_call(), 1)
call_10006 = relay.TupleGetItem(func_5865_call(), 1)
output = relay.Tuple([call_9989,call_10002,call_10005,])
output2 = relay.Tuple([call_9990,call_10003,call_10006,])
func_10012 = relay.Function([], output)
mod['func_10012'] = func_10012
mod = relay.transform.InferType()(mod)
mutated_mod['func_10012'] = func_10012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10012_call = mutated_mod.get_global_var('func_10012')
call_10013 = func_10012_call()
output = call_10013
func_10014 = relay.Function([], output)
mutated_mod['func_10014'] = func_10014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8570_call = mod.get_global_var('func_8570')
func_8571_call = mutated_mod.get_global_var('func_8571')
call_10015 = relay.TupleGetItem(func_8570_call(), 0)
call_10016 = relay.TupleGetItem(func_8571_call(), 0)
var_10030 = relay.var("var_10030", dtype = "float32", shape = (10, 6, 7))#candidate|10030|(10, 6, 7)|var|float32
bop_10031 = relay.equal(call_10015.astype('bool'), var_10030.astype('bool')) # shape=(10, 6, 7)
bop_10034 = relay.equal(call_10016.astype('bool'), var_10030.astype('bool')) # shape=(10, 6, 7)
func_6213_call = mod.get_global_var('func_6213')
func_6214_call = mutated_mod.get_global_var('func_6214')
call_10037 = relay.TupleGetItem(func_6213_call(), 0)
call_10038 = relay.TupleGetItem(func_6214_call(), 0)
uop_10052 = relay.asin(call_10037.astype('float32')) # shape=(10, 1, 7)
uop_10054 = relay.asin(call_10038.astype('float32')) # shape=(10, 1, 7)
func_6473_call = mod.get_global_var('func_6473')
func_6474_call = mutated_mod.get_global_var('func_6474')
call_10055 = relay.TupleGetItem(func_6473_call(), 1)
call_10056 = relay.TupleGetItem(func_6474_call(), 1)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
var_10071 = relay.var("var_10071", dtype = "float32", shape = (2112,))#candidate|10071|(2112,)|var|float32
call_10070 = relay.TupleGetItem(func_4460_call(relay.reshape(var_10071.astype('float32'), [352, 6])), 0)
call_10072 = relay.TupleGetItem(func_4462_call(relay.reshape(var_10071.astype('float32'), [352, 6])), 0)
output = relay.Tuple([bop_10031,uop_10052,call_10055,call_10070,var_10071,])
output2 = relay.Tuple([bop_10034,uop_10054,call_10056,call_10072,var_10071,])
func_10091 = relay.Function([var_10030,var_10071,], output)
mod['func_10091'] = func_10091
mod = relay.transform.InferType()(mod)
var_10092 = relay.var("var_10092", dtype = "float32", shape = (10, 6, 7))#candidate|10092|(10, 6, 7)|var|float32
var_10093 = relay.var("var_10093", dtype = "float32", shape = (2112,))#candidate|10093|(2112,)|var|float32
output = func_10091(var_10092,var_10093,)
func_10094 = relay.Function([var_10092,var_10093,], output)
mutated_mod['func_10094'] = func_10094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_10157 = func_3961_call()
call_10158 = func_3961_call()
func_9753_call = mod.get_global_var('func_9753')
func_9754_call = mutated_mod.get_global_var('func_9754')
call_10167 = relay.TupleGetItem(func_9753_call(), 0)
call_10168 = relay.TupleGetItem(func_9754_call(), 0)
func_9200_call = mod.get_global_var('func_9200')
func_9201_call = mutated_mod.get_global_var('func_9201')
call_10174 = relay.TupleGetItem(func_9200_call(), 0)
call_10175 = relay.TupleGetItem(func_9201_call(), 0)
output = relay.Tuple([call_10157,call_10167,call_10174,])
output2 = relay.Tuple([call_10158,call_10168,call_10175,])
func_10182 = relay.Function([], output)
mod['func_10182'] = func_10182
mod = relay.transform.InferType()(mod)
mutated_mod['func_10182'] = func_10182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10182_call = mutated_mod.get_global_var('func_10182')
call_10183 = func_10182_call()
output = call_10183
func_10184 = relay.Function([], output)
mutated_mod['func_10184'] = func_10184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3684_call = mod.get_global_var('func_3684')
func_3685_call = mutated_mod.get_global_var('func_3685')
call_10185 = func_3684_call()
call_10186 = func_3684_call()
func_6071_call = mod.get_global_var('func_6071')
func_6072_call = mutated_mod.get_global_var('func_6072')
call_10188 = func_6071_call()
call_10189 = func_6071_call()
func_4067_call = mod.get_global_var('func_4067')
func_4069_call = mutated_mod.get_global_var('func_4069')
const_10197 = relay.const([True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True], dtype = "bool")#candidate|10197|(140,)|const|bool
call_10196 = func_4067_call(relay.reshape(const_10197.astype('bool'), [10, 2, 7]))
call_10198 = func_4067_call(relay.reshape(const_10197.astype('bool'), [10, 2, 7]))
output = relay.Tuple([call_10185,call_10188,call_10196,const_10197,])
output2 = relay.Tuple([call_10186,call_10189,call_10198,const_10197,])
func_10212 = relay.Function([], output)
mod['func_10212'] = func_10212
mod = relay.transform.InferType()(mod)
mutated_mod['func_10212'] = func_10212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10212_call = mutated_mod.get_global_var('func_10212')
call_10213 = func_10212_call()
output = call_10213
func_10214 = relay.Function([], output)
mutated_mod['func_10214'] = func_10214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7001_call = mod.get_global_var('func_7001')
func_7002_call = mutated_mod.get_global_var('func_7002')
call_10235 = relay.TupleGetItem(func_7001_call(), 0)
call_10236 = relay.TupleGetItem(func_7002_call(), 0)
output = relay.Tuple([call_10235,])
output2 = relay.Tuple([call_10236,])
func_10237 = relay.Function([], output)
mod['func_10237'] = func_10237
mod = relay.transform.InferType()(mod)
mutated_mod['func_10237'] = func_10237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10237_call = mutated_mod.get_global_var('func_10237')
call_10238 = func_10237_call()
output = call_10238
func_10239 = relay.Function([], output)
mutated_mod['func_10239'] = func_10239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8450_call = mod.get_global_var('func_8450')
func_8452_call = mutated_mod.get_global_var('func_8452')
call_10320 = relay.TupleGetItem(func_8450_call(), 0)
call_10321 = relay.TupleGetItem(func_8452_call(), 0)
func_7362_call = mod.get_global_var('func_7362')
func_7364_call = mutated_mod.get_global_var('func_7364')
var_10350 = relay.var("var_10350", dtype = "bool", shape = (882,))#candidate|10350|(882,)|var|bool
call_10349 = relay.TupleGetItem(func_7362_call(relay.reshape(var_10350.astype('bool'), [14, 9, 7])), 0)
call_10351 = relay.TupleGetItem(func_7364_call(relay.reshape(var_10350.astype('bool'), [14, 9, 7])), 0)
output = relay.Tuple([call_10320,call_10349,var_10350,])
output2 = relay.Tuple([call_10321,call_10351,var_10350,])
func_10359 = relay.Function([var_10350,], output)
mod['func_10359'] = func_10359
mod = relay.transform.InferType()(mod)
var_10360 = relay.var("var_10360", dtype = "bool", shape = (882,))#candidate|10360|(882,)|var|bool
output = func_10359(var_10360)
func_10361 = relay.Function([var_10360], output)
mutated_mod['func_10361'] = func_10361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6731_call = mod.get_global_var('func_6731')
func_6733_call = mutated_mod.get_global_var('func_6733')
call_10401 = relay.TupleGetItem(func_6731_call(), 0)
call_10402 = relay.TupleGetItem(func_6733_call(), 0)
func_7135_call = mod.get_global_var('func_7135')
func_7137_call = mutated_mod.get_global_var('func_7137')
call_10411 = func_7135_call()
call_10412 = func_7135_call()
output = relay.Tuple([call_10401,call_10411,])
output2 = relay.Tuple([call_10402,call_10412,])
func_10423 = relay.Function([], output)
mod['func_10423'] = func_10423
mod = relay.transform.InferType()(mod)
mutated_mod['func_10423'] = func_10423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10423_call = mutated_mod.get_global_var('func_10423')
call_10424 = func_10423_call()
output = call_10424
func_10425 = relay.Function([], output)
mutated_mod['func_10425'] = func_10425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8703_call = mod.get_global_var('func_8703')
func_8704_call = mutated_mod.get_global_var('func_8704')
call_10438 = func_8703_call()
call_10439 = func_8703_call()
output = call_10438
output2 = call_10439
func_10448 = relay.Function([], output)
mod['func_10448'] = func_10448
mod = relay.transform.InferType()(mod)
output = func_10448()
func_10449 = relay.Function([], output)
mutated_mod['func_10449'] = func_10449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8977_call = mod.get_global_var('func_8977')
func_8979_call = mutated_mod.get_global_var('func_8979')
call_10469 = relay.TupleGetItem(func_8977_call(), 0)
call_10470 = relay.TupleGetItem(func_8979_call(), 0)
func_4878_call = mod.get_global_var('func_4878')
func_4880_call = mutated_mod.get_global_var('func_4880')
call_10499 = relay.TupleGetItem(func_4878_call(), 1)
call_10500 = relay.TupleGetItem(func_4880_call(), 1)
output = relay.Tuple([call_10469,call_10499,])
output2 = relay.Tuple([call_10470,call_10500,])
func_10501 = relay.Function([], output)
mod['func_10501'] = func_10501
mod = relay.transform.InferType()(mod)
mutated_mod['func_10501'] = func_10501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10501_call = mutated_mod.get_global_var('func_10501')
call_10502 = func_10501_call()
output = call_10502
func_10503 = relay.Function([], output)
mutated_mod['func_10503'] = func_10503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8092_call = mod.get_global_var('func_8092')
func_8093_call = mutated_mod.get_global_var('func_8093')
call_10537 = func_8092_call()
call_10538 = func_8092_call()
func_5044_call = mod.get_global_var('func_5044')
func_5045_call = mutated_mod.get_global_var('func_5045')
call_10539 = relay.TupleGetItem(func_5044_call(), 0)
call_10540 = relay.TupleGetItem(func_5045_call(), 0)
uop_10554 = relay.asinh(call_10537.astype('float64')) # shape=(352, 5)
uop_10556 = relay.asinh(call_10538.astype('float64')) # shape=(352, 5)
output = relay.Tuple([call_10539,uop_10554,])
output2 = relay.Tuple([call_10540,uop_10556,])
func_10557 = relay.Function([], output)
mod['func_10557'] = func_10557
mod = relay.transform.InferType()(mod)
output = func_10557()
func_10558 = relay.Function([], output)
mutated_mod['func_10558'] = func_10558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10212_call = mod.get_global_var('func_10212')
func_10214_call = mutated_mod.get_global_var('func_10214')
call_10606 = relay.TupleGetItem(func_10212_call(), 3)
call_10607 = relay.TupleGetItem(func_10214_call(), 3)
func_8345_call = mod.get_global_var('func_8345')
func_8348_call = mutated_mod.get_global_var('func_8348')
const_10614 = relay.const([[6.573766,6.376252],[-1.928625,-9.288259],[-5.930356,9.494294],[-0.326734,-9.265090],[-0.411436,-5.017261],[-9.930805,-2.143627],[-4.609640,1.504778],[-8.249168,-2.813180],[8.413224,5.850148],[2.925926,6.461718],[3.846312,0.979767],[9.405154,6.946520],[-1.534220,-9.282120],[-3.327537,-1.525294],[9.419363,9.449190],[-4.484980,7.604670],[8.958731,-7.501188],[-9.956092,5.774057],[-1.670691,1.004110],[-6.309828,-3.395866],[7.662280,4.666978],[6.060804,-5.384110],[3.886130,-0.497301],[3.809100,1.694898],[-0.860597,5.424061],[-8.868850,4.410889],[-7.187327,-9.604148],[0.715668,5.513061],[6.973348,8.600795],[-0.970849,2.554565],[7.731268,6.921754],[0.268273,-4.797791],[-3.220922,-7.344814],[-9.327863,-3.313270],[1.419145,9.230096],[5.063983,2.595464],[-7.969330,7.718402],[-8.669957,-7.346676],[7.897673,-2.964093],[8.451409,-6.457064],[-3.769563,-5.584197],[-2.131294,6.037375],[4.984789,3.688988],[0.676832,2.855154],[3.730608,-2.919188],[-0.682583,2.506016],[2.426841,-4.214897],[-4.529585,-1.905228],[-1.632238,1.045759],[8.605825,-5.683780],[-9.875177,8.467637],[-8.779669,3.716785],[-3.178473,4.403216],[-3.592031,-6.506425],[-7.151178,-8.634856],[1.829823,1.450811],[1.563175,6.727379],[-5.334754,0.422196],[9.996792,-7.122174],[-6.278543,9.553676],[-0.671030,3.149568],[0.843142,-1.506280],[-0.605055,5.428319],[4.178610,2.094939],[3.755730,-9.146414],[-5.497469,-9.680808],[-2.031487,1.175024],[-4.707397,0.545880],[4.097155,-8.719555],[-2.249544,-7.875101],[6.997805,2.415129],[3.754187,-8.346213],[1.480893,-3.489024],[-1.176759,5.560179],[3.238592,7.552828],[1.695543,-3.445759],[4.085624,6.379438],[9.216124,6.632944],[1.453977,-5.223368],[8.984920,-1.462852],[4.400301,9.306273],[6.110006,-3.141270],[5.224559,4.883631],[3.879145,-2.027278],[-3.562118,-2.595856],[2.939535,-8.941791],[-3.082919,2.163635],[2.090310,-6.382063],[-5.002165,8.891698],[-8.932040,4.678305],[9.753834,-2.144557],[-6.441743,-0.494921],[1.465684,0.901844],[-8.224883,8.131459],[-3.762620,-7.875359],[-9.416972,-3.274492],[-7.547498,9.759545],[7.463658,7.915397],[6.531840,3.480918],[-4.392547,-2.998173],[0.702125,-7.914014],[2.976763,-5.867315],[4.210885,-6.714653],[-4.386674,-7.700548],[-0.712330,5.575417],[-3.027882,-3.492993],[1.459362,-3.446251],[8.752433,8.855219],[-4.963270,-6.840633],[8.370701,7.421685],[-0.273604,2.759323],[-5.251495,1.478366],[8.721555,-5.559875],[3.577093,0.535596],[6.528179,-4.144388],[-3.239518,3.697267],[-9.604860,-1.033415],[-9.099571,-8.491429],[0.045248,8.324724],[4.897349,-0.162948],[-0.939447,1.976710],[-7.751886,-2.813102],[-9.630971,-4.878013],[-8.150192,3.432929],[-2.730509,-7.845920],[3.948279,8.126097],[-5.662679,-5.353306],[9.350910,-0.712339],[1.679743,-2.861915],[-4.229581,5.500046],[3.645911,3.586745],[9.962343,-8.361035],[4.210850,7.825136],[3.130523,1.859560],[0.746453,-3.910651],[4.426544,-6.096838],[-1.606056,-8.374496],[7.847470,4.200935],[0.358939,-6.895125],[5.291479,-3.876106],[-4.686019,1.188725],[-1.614435,8.959768],[-8.377835,2.537583],[6.394011,-7.369129],[-6.697946,-9.316376],[6.697923,-4.049778],[2.505463,5.306024],[-7.681802,7.114477],[6.316926,-6.385107],[1.206120,-0.696608],[8.634818,4.478913],[4.513309,-9.314046],[-8.973041,-3.056385],[-5.008638,1.366875],[8.060687,-2.664389],[-1.890988,-7.110163],[-8.008007,-4.259074],[6.340532,9.480168],[-4.265302,3.316893],[4.708058,3.790363],[-6.747874,2.781304],[-5.571535,-9.689329],[0.148546,0.825847],[-0.944251,-9.179970],[7.024464,7.799582],[3.429730,8.156376],[3.474310,8.365893],[3.021508,2.473347],[-2.647305,-9.648930],[6.515763,5.143069],[-7.806806,-4.987547],[-4.556622,7.061011],[6.727550,-7.018022],[-8.300824,-7.815181],[-5.312734,-4.705722],[-9.999668,-2.530825],[-6.240345,-7.123418],[5.561140,-5.428670],[-4.260769,4.926616],[0.200473,-8.826313],[6.760566,9.593144],[1.511417,0.282872],[-4.885370,8.050672],[1.551112,9.719240],[-1.159183,8.604516],[5.623931,7.787199],[7.109515,8.918706],[-9.571306,7.403595],[-2.191150,4.268086],[3.229798,-8.059350],[-1.832100,-7.932352],[8.368802,3.795088],[7.968193,1.274683],[-4.509283,9.170186],[4.669035,2.943679],[-3.197051,6.669454],[1.122811,-7.994268],[-6.502249,-2.599264],[-6.055563,-6.983816],[8.151773,-6.271026],[5.670960,9.554418],[-2.417186,9.402177],[7.290406,2.508806],[9.189853,6.761665],[2.506650,8.226715],[-1.286892,-4.630204],[3.935833,-1.618537],[-5.426232,5.589356],[-0.651806,-2.824388],[4.273053,3.827743],[-5.176513,0.753696],[7.905490,-1.205774],[-5.451472,-0.180100],[-3.369300,-9.911368],[-2.960152,-3.730740],[9.220637,-8.686192],[-8.512075,-6.327995],[-6.025706,2.004014],[4.044223,-5.951140],[7.531374,3.573421],[3.130262,-8.711889],[3.166702,5.109300],[1.595881,-2.251218],[1.662052,-4.083421],[6.949721,-1.017232],[-5.839824,-8.197143],[-0.539107,7.602553],[-3.339510,1.240781],[-1.502343,4.994694],[-4.415014,3.698958],[-7.425131,-8.453459],[-0.248305,0.966903],[-3.765571,5.571423],[4.616712,-3.309998],[7.037737,3.929293],[-2.645023,9.554793],[-3.447090,-1.268304],[8.098022,-3.723804],[-9.510642,7.388939],[-3.638560,-3.626248],[-7.986164,1.580742],[-8.146662,7.342199],[4.006108,7.094616],[-4.468702,9.407422],[4.596341,9.175156],[2.257421,-6.664200],[9.105852,5.312965],[-1.732256,-7.180249],[8.542664,7.260862],[3.109445,1.232050],[9.737109,-4.418473],[6.436108,6.336127],[-2.564823,7.016222],[-3.815952,9.881365],[-3.174459,2.129342],[-8.845265,1.727553],[-2.538776,0.563533],[-6.998933,-1.699407],[2.033778,8.713736],[-2.695975,4.080758],[1.510077,2.793193],[-3.386688,7.076764],[2.815863,-1.897258],[-4.733902,4.528161],[-6.677409,-4.594461],[-9.858129,-6.553932],[-6.710781,-0.423791],[-5.016913,8.119159],[5.762128,-3.212818],[2.120920,-5.780495],[-6.347971,-5.737873],[-4.846901,2.488646],[9.035991,8.415887],[6.006113,9.800202],[4.887563,-8.657484],[-6.774435,-5.939195],[-7.508409,9.436199],[-8.975550,-8.962136],[-2.267753,-4.967508],[7.443988,4.754947],[7.014611,-9.710507],[4.644119,-1.519436],[0.169625,-7.984946],[-7.043148,1.546916],[7.343985,-4.985553],[-3.648303,4.364264],[-7.131447,-2.753339],[1.580799,-1.866216],[-8.739185,7.402608],[-1.390033,0.459473],[0.194716,3.340575],[-6.547808,-2.377312],[-3.560983,1.580654],[-4.378824,5.710487],[-6.293974,-9.137699],[-2.478898,9.115805],[3.546841,-2.671187],[-5.240193,3.552183],[1.313228,-5.468688],[-4.783916,-6.952862],[0.076992,6.209286],[-6.990680,-3.882293],[-9.525276,-5.016196],[5.890805,-9.275326],[7.001768,8.172105],[-1.501414,7.313657],[3.096284,4.498624],[-5.309228,-7.401221],[4.027637,7.042517],[4.179141,8.694407],[-2.976222,-5.497076],[2.131879,-1.487691],[8.814043,-1.110626],[7.819650,3.291806],[2.052158,-4.794006],[-0.314295,-0.778971],[-1.784490,4.602490],[2.110609,-8.756987],[3.450229,-3.606374],[7.068088,6.188553],[-4.058561,-7.209252],[8.088355,-2.293482],[-8.237737,-5.635700],[-1.548872,-8.133007],[5.906728,-2.275446],[-7.081536,-1.594761],[3.100992,-7.834460],[-9.854019,1.955854],[-3.585017,-6.979552],[2.294145,-9.781768],[6.490474,4.688415],[3.740508,-2.322032],[5.571960,-8.400694],[7.702872,3.993025],[9.482146,5.046110],[4.073495,-9.266920],[-7.010107,3.168124],[5.757168,2.694147],[7.812968,-2.103931],[8.786842,5.232594],[9.555814,-2.644912],[-9.192914,6.019623],[-0.527234,0.336149],[2.690928,2.444563],[-6.811478,-4.382914],[-5.515685,-1.557850],[-6.050656,3.747321],[-6.199724,-5.177436],[-6.260284,-6.652229],[9.090469,-1.622421],[0.107481,7.029299],[2.235052,-9.246601],[-1.999626,6.317299],[5.662914,-5.464716],[0.533827,1.405275],[-3.790621,9.390633],[-2.107183,6.576882],[-1.506669,1.387535],[-4.699085,-1.645197],[3.156762,6.814523],[9.392571,5.540121],[7.444722,-1.637297],[9.318771,-3.595761],[-5.692566,-5.978698],[3.245813,-8.963319],[8.946564,1.590308],[-4.539593,5.923141],[8.195773,2.750866],[0.930774,1.478914],[-8.213384,0.215404],[3.170319,9.882757],[-9.251432,-3.865629],[-0.969552,9.675184],[4.999874,1.797776],[-0.761033,6.756554],[5.303408,4.415189],[8.478089,8.764877],[-0.852566,9.446138],[-6.752939,9.303570],[-5.894741,3.158394],[-0.948966,-8.428360],[6.603172,-6.997079],[-4.191569,9.698532],[-5.278373,9.107426],[5.205667,-2.772172],[0.888364,7.740448],[-6.824035,-4.817914],[4.958151,9.338549],[-7.189690,6.803817],[2.212781,-4.477951],[7.335683,-0.556160],[-9.902095,-1.440823],[-5.532477,0.545380],[-1.298536,-7.459271],[-6.366129,-1.959029],[-5.254962,1.500204],[4.799051,-7.484863],[-0.846419,7.390859],[2.607271,-7.525876],[7.490894,3.464571],[2.316213,4.543050],[-2.660704,-1.467739],[4.571724,-5.661382],[8.348586,-5.820046],[-5.230726,2.351004],[8.205881,-0.051467],[-0.369750,-5.570354],[4.090244,-8.784794],[9.596756,6.999348],[2.583988,-5.449710],[-1.841988,-8.782136],[-4.951517,-3.725730],[7.780478,-7.337670],[-5.307518,7.085642],[2.934442,-2.367722],[-8.767526,1.970293],[4.195460,9.622677],[-3.008587,8.992304],[-7.927226,-8.281783],[-4.731646,2.959026],[4.271189,1.235656],[-5.889323,-3.043072],[-8.919646,8.829803],[3.202644,-9.382357],[2.300342,5.985786],[5.219907,-2.656868],[-9.861046,7.281148],[1.179698,5.892732],[-6.938925,0.370771],[0.473952,-3.368392],[-3.095168,-5.663993],[-7.849080,-9.735949],[-5.981205,8.166799],[-5.767844,3.206255],[0.868484,-6.649731],[8.993409,4.435757],[-2.735959,8.297985],[-6.624432,9.120286],[5.541191,3.970087],[0.986199,3.977031],[1.585970,5.694694],[-1.652224,3.197344],[8.400709,-2.305840],[2.123281,-7.720052],[-4.914302,4.213396],[7.016923,-5.286745],[3.260753,-9.761436],[2.217847,-8.492263],[3.941298,6.002716],[5.580148,1.945940],[-4.686014,0.222019],[1.954768,4.304530],[2.675640,-2.173823],[7.053582,5.489051],[-5.449267,4.656689],[6.113686,0.121022],[-7.587046,-6.685956],[1.442346,-0.357109],[-0.210297,5.007126],[-2.133946,2.356603],[5.192118,-6.265098],[-7.250878,8.934971],[-0.397297,5.302763],[9.160634,-5.134372],[0.716897,4.694384],[-5.692490,-2.613214],[3.859241,-6.294238],[-4.919180,-7.085097],[5.176347,-6.885998],[-4.818761,1.758446],[9.893402,8.865559],[8.478381,-0.810953],[-8.522771,9.881850],[2.194028,7.801119],[2.926825,-0.360364],[-8.731782,0.988174],[-7.685046,8.001314],[-3.580791,8.899861],[6.100915,-9.685270],[-9.107880,3.974097],[-4.783352,6.881981],[-0.515514,-4.794299],[-4.346652,6.793288],[5.470464,-2.552449],[0.522158,8.079615],[-0.866848,6.028272],[5.091357,-7.344083],[-2.957481,-8.207847],[-3.398288,-9.460278],[7.969322,-1.346125],[-5.439685,-5.434507],[8.102842,3.330031],[-7.986929,-6.739319],[9.645325,9.953293],[0.642121,-3.212521],[4.451203,-9.075951],[-4.877833,2.499625],[1.827118,0.360321],[1.472229,-6.800495],[-8.767706,1.573941],[-3.716760,-6.210294],[7.134777,-8.430458],[3.807994,-8.434771],[8.691749,1.902468],[-4.437353,7.877686],[-4.454673,3.921811],[-9.325806,-7.599831],[5.425166,-2.537894],[1.904812,0.452640],[-4.441777,3.668485],[-2.544489,-3.290449],[-9.427635,7.278013],[-2.905000,5.188826],[9.503804,8.737612],[-3.395862,-3.955619],[9.238552,3.282075],[9.265946,-4.488199],[-8.650716,-8.652216],[8.812833,-6.708271],[-5.756031,-5.425407],[5.007054,5.342285],[-6.130891,-1.356730],[1.077275,-8.089273],[4.888513,4.694812],[-7.566319,-6.047692],[-9.163166,2.640826],[-0.844864,5.182753],[4.308740,4.410262],[9.277469,1.982230],[6.374476,-2.219370],[5.970126,-3.150066],[-6.707670,8.080909],[8.352003,5.337090],[-1.880462,7.385890],[6.181096,1.382943],[4.749579,1.169690],[-8.837509,-5.318210],[-3.467296,-0.928790],[-0.022802,3.910504],[-4.694357,6.500165],[-4.148438,1.201815],[-5.477004,3.770144],[-0.246018,-1.918819],[-8.020043,-7.281682],[7.150987,-7.058444],[-5.332267,7.369656],[5.203020,2.439428],[6.684393,8.356451],[-6.880516,7.426129],[-9.428079,-0.387561],[5.509598,-1.814674],[-2.021185,-7.001505],[0.956907,6.296499],[2.054618,-1.351438],[3.869352,7.988442],[9.979280,2.881693],[7.781422,-7.902090],[2.997606,-8.771080],[7.710386,-0.363314],[-1.544592,6.253861],[-1.050027,5.130566],[3.377958,-3.338259],[1.233977,-3.343930],[2.920803,-9.124134],[-8.873922,-6.734100],[8.802433,-0.614805],[2.521139,-2.087266],[-2.204656,0.984007],[8.667160,-8.388128],[0.219199,1.187865],[-0.459846,1.617609],[1.261985,7.504107],[-4.770341,-9.022231],[-7.823057,-2.737554],[1.845097,0.185084],[4.133517,-9.315352],[0.479906,1.018429],[-3.022606,-9.720273],[-2.261817,-7.943834],[6.678947,1.449884],[0.505424,-3.703175],[1.927334,6.673959],[5.381967,-3.222606],[6.236482,5.308653],[5.865988,2.499169],[-3.969592,8.700407],[1.024886,-4.494248],[2.422082,-1.559257],[4.548678,-9.545787],[-9.112842,-2.100677],[1.935769,-0.612101],[6.288345,6.757459],[-6.329773,-1.634706],[-7.133781,-7.843362],[0.618760,3.229032],[-3.072228,3.249597],[-7.595913,-4.775621],[6.350533,-3.100661],[4.155216,-5.984125],[9.561241,-3.704977],[-6.041686,-4.642384],[-4.311704,8.761685],[5.240868,-3.025377],[-6.570821,-0.595970],[1.765432,4.677130],[4.663215,3.363270],[-3.034346,0.132671],[-8.743716,-0.918267],[1.679475,2.031457],[0.900060,0.723053],[2.085387,-5.695115],[-8.364192,-5.002232],[-6.929873,-2.446372],[-3.040210,-4.252774],[6.396389,-8.836841],[5.481018,2.703909],[7.638933,-3.630242],[8.855936,8.216088],[5.260269,-9.050967],[-4.697177,-2.017062],[5.640970,-0.197393],[-0.695618,-9.685810],[2.404712,8.682659],[9.618733,4.058162],[-1.666269,2.310021],[1.546205,-6.292802],[1.109499,-8.290061],[-0.368423,-6.395128],[-9.218785,1.059821],[8.980613,-5.551154],[-0.370599,-3.378597],[-6.452507,-3.694636],[5.924026,-1.327521],[-9.637839,-9.731697],[-5.754741,-9.548709],[7.602471,-3.113889],[3.833852,-6.068454],[5.346015,1.957486],[6.188966,-8.847274],[0.486865,-9.039547],[-7.052979,-1.277041],[6.062710,-4.125372],[2.430731,-6.165102],[8.286342,-1.443535],[-2.258616,-3.455205],[-1.485924,1.215774],[0.828910,5.832389],[-5.290824,9.499303],[5.015703,-9.745268],[-7.362398,-1.221615],[9.138456,-7.521467],[8.630988,1.099128],[-6.700618,7.744647],[-9.163698,-3.505583],[-4.941256,-4.787361],[1.762841,-1.139632],[4.231046,8.280010],[8.072094,-3.596547],[8.014977,-2.187918],[6.090255,-6.181317],[0.335693,-3.854175],[2.931141,7.765069],[9.608034,-9.369254],[2.733836,6.940800],[8.441880,5.848982],[-7.972250,1.401356],[-9.161794,-6.635621],[-5.067049,9.908602],[-4.925290,7.133881],[-5.568885,-2.606186],[-3.766965,-8.795149],[4.370738,6.730007],[9.421576,3.148647],[-2.539482,2.124963],[-2.149274,-0.460911],[-6.431864,-5.494194],[-9.697927,-8.095051],[-0.487932,-1.226715],[-1.708752,2.951503],[-5.184940,-8.729459],[3.427506,6.233146],[6.488591,-4.679723],[-1.523050,-6.206956],[4.574355,5.219276],[-8.548336,-7.257112],[-4.597345,2.093985],[-4.362485,-6.924824],[6.917158,-0.188560],[6.201118,-2.594326],[-5.571693,-6.723011],[-6.712204,4.030876],[-0.683996,3.980211],[4.861435,1.408405],[-6.023764,-2.762868],[7.484261,6.520393],[4.549000,6.427057],[5.328914,9.328816],[8.161753,-8.661685],[-6.962554,3.807954],[-7.115217,1.658758],[-9.276431,-9.827781],[-3.493951,2.080417],[3.180325,-9.168436],[-0.168623,3.397104],[-4.086202,3.571850],[8.938048,3.806237],[-9.967974,-3.810349],[4.129089,-9.626932],[-9.736772,-0.953651],[5.940262,4.414812],[-1.583672,1.063518],[3.849532,-7.437993],[-9.807224,3.459198],[1.343981,8.218108],[4.938657,-6.155848],[-2.679780,4.399797],[8.141721,1.775605],[4.702628,-4.684602],[-0.633604,0.886408],[-7.260445,8.428437],[5.872542,-9.169282],[8.816352,-2.426792],[0.176893,4.355274],[3.836990,7.298008],[-6.053357,7.247212],[8.446666,0.932825],[-4.594455,8.375971],[-8.744593,8.342130],[-6.565669,-8.557204],[8.081738,-1.882174],[-9.164805,-5.866561],[-5.956053,-5.554901],[-3.040798,2.821986],[9.755110,-7.018357],[9.737556,0.674818],[-3.378595,1.300282],[-7.533035,5.831844],[8.689751,5.221365],[5.523829,5.864282],[2.238947,5.065757],[-5.232266,7.347733],[7.528760,3.934997],[3.658247,4.278657],[5.818470,-3.239248],[-0.050681,3.863603],[-4.473718,9.824660],[2.377148,7.246207],[2.482635,-0.383486],[7.695747,2.425717],[9.804967,5.484551],[1.011799,3.640850],[-0.840089,3.181219],[3.023234,-4.951282],[8.484944,4.368618],[-5.827802,5.023382],[4.984492,6.596315],[0.430611,-1.840182],[6.021422,7.965205],[-8.560776,8.014073],[2.506352,3.757209],[-8.873471,-6.785623],[-5.080045,-3.758771],[-6.972256,-8.769547],[8.798675,4.086842],[-7.072871,-4.902690],[2.245134,8.498404],[-0.756584,-4.409935],[3.879690,-3.813719],[4.741368,5.551551],[-4.357177,3.226783],[8.796515,1.309512],[3.149061,6.962934],[-5.143593,-7.770662],[9.735384,8.862953],[-6.881755,1.715288],[6.146073,8.179869],[-8.891378,-7.859344],[-8.617534,-6.915250],[4.006282,6.247508],[-2.408989,1.942838],[-9.024969,-2.254242],[9.970297,1.371361],[-4.319052,5.574018],[-1.553217,-8.015802],[0.573231,9.788018],[-4.990846,8.121145],[6.427625,5.229848],[2.248479,-0.309829],[-4.586262,2.417093],[-6.991058,5.309403],[-5.986223,2.368911],[-5.023916,6.049659],[-1.133766,1.379793],[-2.077711,6.453280],[8.310004,7.366914],[8.766340,-9.002236],[0.359858,5.709747],[-6.006987,-6.957053],[0.101916,4.238021],[9.583170,3.049819],[-6.787202,8.024281],[0.365557,-5.963881],[4.114559,9.313224],[-8.280899,-6.700400],[2.357859,9.235549],[-0.425959,-6.747789],[2.566123,7.075149],[5.250362,2.633771],[-9.162248,-4.433045],[8.771905,-8.461863],[3.622016,9.876134],[-2.909056,4.230641],[6.776077,9.783653],[-3.433370,1.924619],[-5.082537,-6.028314],[8.938572,3.225564],[-1.213996,6.709067],[-3.357037,-9.876856],[5.385137,3.492433],[1.663401,2.994807],[-1.624332,2.947786],[8.963785,-6.918385],[3.493234,7.052125],[-1.951945,-2.673748],[-6.732808,-8.521669],[-6.910677,-3.814659],[-7.105460,3.503162],[-0.774018,-4.333942],[3.954380,3.659471],[-1.171932,-9.749367],[1.869330,-1.593681],[-0.770397,-2.768728],[-4.027119,-4.962899],[-9.320657,-6.492231],[-5.360551,-4.620738],[6.712560,5.382642],[-0.964944,6.355655],[8.627720,4.989937],[8.942720,-6.338615],[-5.349637,-8.975292],[-5.570434,3.978678],[-4.641193,6.059434],[7.576569,8.083204],[5.682472,-4.269100],[-7.677956,-9.762317],[9.183783,-1.056591],[-0.887061,4.544508],[8.522745,7.369612],[-4.709472,-2.655200],[8.548236,3.819925],[-4.331929,5.928647],[-0.657556,7.744004],[2.616196,-8.211700],[5.913692,6.674625],[1.216764,4.245249],[-3.659411,-5.869760],[6.930619,9.910716],[4.014630,-6.744128],[-0.175830,8.142814],[4.924530,6.681811],[-6.983671,7.212238],[-9.862554,8.164567],[3.806224,-3.001549],[-3.812604,-1.214394],[-9.218286,-9.227583],[7.906627,0.302647],[-7.664348,-3.823439],[4.270718,-4.221034],[9.296288,-5.046276],[-2.949164,2.330298],[-1.546261,1.565244],[9.062624,-3.551424],[-3.925845,5.362245],[7.117275,7.727967],[3.681758,4.592095],[9.325576,-6.286277],[-7.050850,-8.299617],[4.908286,-8.000009],[6.799464,-9.964424],[-3.779258,-5.650485],[2.424576,-1.456898],[-9.235887,-9.519087],[8.094841,3.180603],[6.523437,4.640216],[-6.064305,-7.447345],[4.880288,7.518985],[-7.120990,3.669953],[-4.907512,8.960768],[1.462598,8.178650],[3.389867,2.945542],[1.804643,6.631254],[6.143487,-3.749562],[-1.956553,1.131371],[-3.484845,1.364589],[-2.186236,5.272472],[-0.246377,-3.020689],[-5.835571,-2.099811],[6.672947,-0.353925],[-0.307782,2.436825],[-0.179503,1.847712],[-4.564825,-9.984207],[2.965105,1.180860],[1.280772,-4.312902],[-3.127628,7.648023],[-1.014171,-4.989880],[-2.992783,7.747721],[5.257266,-6.255572],[-6.132933,-6.314576],[-6.201076,2.786576],[-0.586355,8.715160],[5.748627,-6.425485],[-6.560445,-3.393074],[5.315241,-5.523804],[6.074810,-8.963033],[-0.099098,-2.272015],[-5.867783,1.657350],[-7.621638,-0.704095],[0.128058,-2.403311],[9.323305,-0.681894],[-4.502663,4.216153],[-6.844334,9.706155],[5.271764,-6.312126],[-3.173452,-2.156653],[1.545724,8.950344],[7.964842,7.175780],[2.401434,1.739777],[-9.684437,-4.556675],[0.783710,-9.081795],[0.784238,8.653692],[3.760958,-8.405728],[6.563776,-3.342204],[-1.345644,-7.628898],[2.712680,3.737024],[8.422778,0.972666],[-5.585336,-8.859626],[1.328254,3.777214],[5.725555,8.488812],[-3.390222,-5.891249],[9.117230,9.629710],[0.665843,1.966696],[0.953904,2.480104],[5.709351,-8.603446],[6.068265,6.665558],[0.664789,0.246492],[-2.117757,7.469437],[6.894347,-1.784138],[-1.801672,-4.112151],[2.638135,-7.391495],[-4.906787,2.127498],[-6.538172,-5.586372],[-1.529198,0.495082],[-2.900777,-8.035318],[3.857841,-7.631031],[-9.691814,9.323687],[-9.308211,-0.436482],[6.347959,-5.762925],[-8.212838,-3.782818],[0.943525,-7.441364],[-6.636856,0.184848],[3.257801,9.343238],[7.893397,9.305596],[-5.064390,-2.204160],[-1.822089,-9.866773],[9.182410,-1.386523],[-2.919366,-8.814606],[8.847312,-9.480400],[-6.706827,-7.947972],[0.694937,2.319749],[9.303233,-5.030212],[5.299299,-6.890265],[7.648045,-9.018091],[8.082269,7.901553],[1.318180,4.420166],[-0.426861,-8.372322],[0.836070,-9.499292],[8.387152,4.389025],[-7.039924,-2.819412],[-9.075506,-5.637924],[-5.571535,-3.237507],[7.028902,9.689092],[-2.511972,6.036665],[-4.878758,9.269422],[-6.441872,2.605971],[1.255386,4.612564],[-3.666593,-3.586568],[-4.755746,2.738513],[0.170473,4.394698],[4.343910,9.223808],[8.259119,-0.816915],[-2.674799,-1.710639],[-8.822376,-9.097571],[-0.493292,4.485922],[-7.848938,-4.290929],[-8.243122,3.438683],[5.086082,-6.932158],[7.332404,-3.613652],[-7.692814,7.005153],[7.995420,-2.440872],[5.737067,6.167761],[-8.737670,-9.127882],[-3.867699,9.725796],[-6.076553,-6.569077],[2.597349,-2.167710],[-1.863958,-0.666577],[-2.293974,-8.164219],[2.878357,2.347888],[3.243915,-7.608238],[9.174408,-9.506242],[7.474044,8.522462],[-8.631726,-3.275489],[-3.317389,9.491861],[4.686749,-9.025504],[6.474816,5.957210],[8.979859,2.773122],[-2.176016,-3.586938],[-7.830128,2.015297],[-6.104858,-4.419871],[8.046702,1.465900],[8.765576,-1.874076],[-2.554396,-4.920362],[5.246577,-8.987528],[-7.164898,-8.864272],[1.356055,1.070685],[2.126038,-1.268088],[7.527374,7.697349],[6.764763,-0.442705],[6.926214,0.883252],[3.809570,8.882578],[-4.793349,4.992267],[4.557841,0.035478],[-5.971431,-8.883882],[3.885118,-7.115232],[7.256109,6.190234],[-3.748370,-1.863583],[1.135616,6.181467],[3.667979,2.553663],[-2.037322,9.112727],[-1.646639,-6.521668],[6.232164,2.391670],[5.339459,6.148993],[2.568703,5.508167],[-7.427146,0.553079],[-0.145910,8.926749],[3.710085,0.658660],[1.073227,0.157146],[4.538266,9.154440],[-4.027169,4.539312],[-1.929981,2.721484],[-6.241950,9.014648],[-1.934952,-2.570464],[0.252373,-3.344949],[-8.002996,-0.600535],[-5.193839,-2.655059],[1.612418,-2.063976],[-8.687071,-3.661047],[-9.444599,-9.900367],[-2.441449,-6.665889],[-6.082542,9.248049],[-7.727418,-6.485297],[8.315490,-1.817679],[-3.107268,1.786889],[-8.726409,3.193652],[-6.797120,2.531263],[2.042500,2.641386],[0.218597,-1.236960],[-1.739311,3.805468],[-3.123228,0.723824],[-1.730483,0.395241],[-8.116529,3.478868],[5.097002,3.533491],[-4.100018,-6.878350],[-7.838998,4.171249],[4.084876,1.162159],[-7.320147,-1.743249],[-6.421616,-8.456765],[-9.918561,6.554201],[7.215718,4.862450],[-3.576591,-5.331878],[-9.071113,-7.758176],[-7.128972,-0.236913],[-6.059284,2.850389],[8.627422,6.287395],[0.250800,-0.322147],[1.665632,7.157478],[-9.926180,1.885357],[7.589532,9.850419],[5.145069,5.695170],[-0.088908,0.862867],[1.612604,8.912780],[1.245504,5.822061],[-2.841781,-5.999467],[8.757102,-9.070726],[-3.873126,-6.910226],[8.817840,3.302838],[-8.928974,-8.677409],[2.632756,0.546175],[-3.363325,6.809665],[5.867827,5.578554],[-5.411905,5.982788],[7.345763,-8.981916],[-3.475182,3.139972],[-9.576125,-3.930977],[6.182670,6.850378],[-8.569364,-8.204930],[8.888637,-4.583679],[-0.422607,6.823360],[8.408198,-3.578653],[-2.711290,6.069834],[-4.028949,5.493662],[6.282011,5.905397],[-3.950296,1.033131],[0.225658,-4.575513],[8.719733,2.126318],[-4.402881,7.208257],[7.707371,-2.558131],[-4.110463,-7.211783],[-0.253290,3.495610],[1.389738,0.478059],[-1.765119,3.445426],[-0.497229,-4.118410],[-2.039827,6.659156],[-8.215469,3.816793],[-4.656138,-8.767567],[7.263838,5.471071],[-9.769672,8.353402],[5.435514,3.054402],[-5.807331,3.115991],[-3.156454,-5.705886],[0.819378,6.256070],[-0.965203,-1.578692],[-8.622408,0.710196],[4.230855,-4.208987],[-9.138804,-0.672889],[-0.360877,7.078791],[-1.334814,3.937376],[-7.361232,8.478464],[4.874370,-5.820596],[0.385861,-6.981908],[1.625677,0.822110],[5.943515,-4.503679],[-5.776116,9.697693],[-5.782347,9.804869],[-3.882951,-3.433458],[-2.106115,-6.707551],[-6.891899,-7.142368],[8.037895,-0.833597],[-6.432695,-3.575028],[9.087890,1.396705],[4.059722,-8.313321],[6.616618,-8.551199],[-2.343474,7.181587],[-5.085710,-1.466747],[-8.778535,9.681180],[9.182723,-2.437359],[5.082426,0.096142],[7.001617,-3.756717],[-4.751404,-3.151545],[-1.491335,5.610719],[3.418616,-4.847466],[-7.329136,3.759326],[4.443625,8.347267],[-4.830434,-3.892513],[-7.395762,-6.604750],[0.734402,-8.757802],[3.256258,0.747465],[9.506249,-8.212587],[3.075177,-3.711724],[6.113546,-7.301180],[-8.231384,2.968465],[8.433730,4.138587],[-5.567882,2.425997],[-6.177493,0.832954],[0.837946,-1.234899],[2.040461,7.891836],[4.216753,-7.315946],[4.729049,8.938786],[-9.263886,-2.159965],[-8.568752,9.374710],[3.498831,-6.047644],[-3.970745,7.905160],[7.945800,-3.413985],[-9.270670,5.786948],[-7.004839,-4.197301],[3.942312,7.934538],[8.151822,9.124862],[8.113483,-2.299528],[-0.996614,4.925031],[-1.251901,-0.458032],[-4.211475,-2.930543],[-9.800201,-1.398522],[0.179389,6.314804],[-6.988607,9.629231],[-5.136760,1.426189],[3.832384,0.333018],[4.947108,1.887254],[9.675070,5.531756],[-1.659597,0.219047],[5.927097,5.167748],[-6.283486,2.981300],[-9.187180,-4.123760],[-1.705252,-1.533407],[4.240890,0.909036],[-3.655824,-2.713281],[-0.602413,2.469700],[1.477301,2.120092],[-3.403133,-6.358365],[9.899462,9.553711],[-5.333660,6.420275],[-7.007975,-1.274401],[8.347279,-8.075996],[-7.053609,2.035742],[-4.494528,-6.811288],[5.603251,-9.973517],[-3.589818,1.999823],[7.783567,8.486901],[-0.097709,-5.288945],[8.050153,9.615765],[-7.064317,-5.932040],[-6.687850,8.643300],[0.491923,2.266603],[1.218027,-6.481916],[-3.262613,-5.715492],[4.254571,7.764789],[-8.893732,-1.024145],[-9.889742,-4.166310],[0.534822,-0.578870],[-8.747790,-3.051782],[7.428431,4.196299],[7.525203,-2.280606],[1.526069,8.093976],[2.745994,-3.244863],[-0.977476,8.914137],[-2.175925,2.201682],[-7.846016,-5.130211],[9.561755,-4.897101],[-6.992899,-7.338197],[-9.704316,7.739405],[2.223368,-9.899365],[2.054965,-3.229229],[3.388376,-9.545886],[9.679502,1.937964],[3.580985,-8.627309],[-5.278544,1.561194],[-8.283329,-8.520641],[4.576393,-8.514819],[9.230327,2.352692],[-7.601900,-1.896344],[7.360823,8.224497],[4.393292,-3.841688],[-0.783405,9.659444],[-2.635447,3.008916],[-4.038077,6.395086],[0.509783,-8.940052],[-0.555753,0.071766],[5.365461,-0.792566],[8.012736,5.960614],[-7.586992,9.950377],[9.148019,0.729168],[-3.683323,-6.269985],[-0.871380,-3.414215],[-5.904124,-5.436562],[-1.112472,5.907103],[-7.846084,-1.993923],[1.072972,-4.970861],[4.408454,8.774969],[-8.165457,-4.447386],[0.057130,-6.267384],[-9.326378,-7.596498],[6.595058,2.509667],[-9.889643,-3.062115],[-9.413812,-8.560745],[-8.272651,0.244470],[1.708538,-4.814226],[4.133058,-7.226989],[-5.186108,6.239280],[5.180545,5.932605],[-2.351477,-6.034042],[2.168054,8.240939],[1.475109,3.220699],[-4.659394,9.274659],[9.374306,-8.926971],[8.934274,-5.084366],[9.739743,-3.682160],[6.662665,7.910648],[1.876265,-1.892211],[-2.687701,-6.634490],[-7.875195,-6.061573],[5.623917,-1.815659],[9.829287,7.922715],[7.363843,-6.087127],[4.295361,0.684886],[-2.254837,1.356296],[-4.007468,-9.004365],[2.920203,-8.221921],[8.379926,6.557572],[-6.461239,9.721430],[-4.896207,-3.860019],[-3.741310,-3.296358],[-7.493432,-4.251010],[-9.674142,-0.693016],[-6.838966,-4.144800],[8.249680,1.207140],[8.775919,3.379460],[-5.078472,9.485390],[-3.883172,-9.645987],[1.578710,-3.621524],[-5.068869,-1.457378],[-8.843065,8.276617],[-9.989802,1.964606],[-0.044015,-1.291468],[3.945822,2.009860],[-7.175921,-6.358124],[6.440719,-3.634774],[9.327368,-9.406280],[6.121572,-0.950945],[6.596334,-7.635378],[3.385669,7.412953],[-8.817288,3.616567],[-3.178890,3.620255],[-5.025007,9.633540],[-3.508968,-6.054822],[-7.030666,8.530696],[2.634991,-2.882084],[8.130865,-6.991841],[-2.593985,-1.145643],[6.088558,-9.293135],[0.797618,5.686923],[9.724755,5.309916],[-1.948872,4.543208],[-7.471826,-2.000864],[-5.522940,-5.773101],[-0.295092,5.674827],[-7.945964,1.671023],[4.203391,1.000094],[-4.896697,-3.900049],[2.447019,2.042762],[5.725559,6.979963],[-7.552853,-2.235094],[-2.420560,-5.170972],[8.434081,5.263808],[-3.605327,-1.231386],[-4.260833,-4.475043],[-9.269290,-6.344120],[-0.363069,0.712504],[-6.897691,6.497285],[-6.569712,8.680205],[-6.407957,7.369783],[8.660821,5.828587],[-2.680878,-2.091559],[-4.563222,8.286575],[1.769419,-0.701153],[1.981648,-6.034252],[-3.242513,-3.006412],[0.478516,9.218092],[-8.187730,2.912373],[2.785161,8.838228],[-2.122133,-1.152165],[-4.329562,4.846273],[2.594353,3.855424],[3.163937,-9.596065],[0.466491,3.913959],[7.815947,-4.773892],[6.151244,0.356792],[-7.889947,-5.819057],[-7.735581,1.593462],[-7.588506,2.486147],[6.567379,5.507796],[-5.633430,-5.467526],[-7.879293,-8.313009],[4.246897,8.738899],[-9.322354,2.549646],[0.102456,-6.459755],[5.217489,-0.909968],[-0.841052,5.568702],[-0.287933,3.654321],[3.242632,-9.493493],[7.394489,9.778582],[3.682795,4.014748],[2.853171,8.773938],[0.123378,8.228747],[4.336719,-0.183761],[1.640370,3.715320],[-3.979426,-6.686819],[3.769361,-6.854201],[1.985427,3.953100],[-5.953463,-4.956415],[7.786622,4.828404],[2.274782,0.566670],[-7.568596,6.968759],[-3.199978,-8.318622],[3.249697,-5.675237],[5.726328,6.230575],[-8.907518,-2.189307],[7.342160,-3.386159],[-2.507263,5.174171],[-5.094186,-4.338787],[7.158663,-4.721424],[2.374618,-9.246303],[5.397560,2.733424],[7.013560,1.013571],[6.027138,1.461736],[8.149144,9.615424],[8.104529,8.059229],[-2.969297,-9.827452],[9.694900,4.266111],[4.304469,3.642520],[-1.932686,-9.859782],[2.321990,0.923735],[4.112807,-9.512312],[-0.300575,-5.830451],[-8.662670,-7.619202],[8.589627,-7.450398],[2.179415,7.235764],[-6.508664,-4.616463],[0.249311,-6.990499],[-0.157755,0.553837],[-9.683260,-0.866581],[-8.900553,-1.276550],[0.687288,0.119958],[-7.761856,5.990864],[0.090084,-7.756261],[-4.904873,-3.286177],[3.341322,-1.771677],[-4.765436,4.776234],[3.478723,5.648830],[-8.384188,1.816876],[-4.727362,0.132037],[-7.618000,5.241353],[0.151566,9.707492],[-2.273564,-2.739170],[5.473559,6.063401],[-4.722052,-9.809966],[7.262322,6.905213],[-3.077887,4.671814],[5.829994,3.944692],[1.912751,5.043910],[-9.057313,-8.657763],[-2.015216,5.541754],[-1.735744,9.939109],[3.920185,-3.468017],[-1.091785,7.847441],[-1.302840,4.852024],[9.098206,-4.788066],[1.736660,6.939139],[-9.526729,-1.583952],[-5.692234,-6.623965],[7.318891,-2.703299],[-9.613082,1.339485],[-6.959881,0.590250],[4.781656,3.500581],[0.929653,5.463913],[4.713957,-6.548477],[2.107015,1.026449],[-9.494749,-3.134361],[3.358347,5.729670],[8.684019,-0.729279],[2.720653,2.552219],[7.593869,9.430935],[-8.667306,4.775685],[5.077545,3.483921],[1.464919,3.133140],[2.986615,9.943627],[-6.098895,-3.984683],[5.546890,3.296287],[-7.433819,7.171353],[4.388404,-4.787748],[6.482039,-8.428341],[8.203690,7.109046],[-6.627467,1.008278],[-3.300725,-5.081231],[1.474541,0.121628],[-7.036413,1.822127],[4.205479,-6.786689],[5.072837,-2.119189],[-3.996026,6.490644],[-9.700084,-5.955671],[1.149751,-2.132646],[-1.038322,-2.150937],[8.572537,-7.762595],[6.349491,-9.209801],[-1.630550,9.995260],[6.625235,0.748748],[-2.407953,-1.878959],[9.556870,7.014724],[-7.288853,1.429421],[7.209696,-5.619956],[3.139999,-2.612525],[-2.065628,1.954123],[0.570542,-1.338795],[-4.760192,-8.337365],[-2.351515,1.080072],[-4.522583,2.895927],[4.236793,0.054554],[-5.799869,5.250570],[0.336271,-8.685476],[5.929236,-9.737118],[1.871027,3.459934],[-1.814792,-2.551904],[-1.889541,6.450156],[2.377037,7.551066],[2.701275,1.910545],[-4.516062,2.362548],[-2.556835,2.515085],[2.545059,-6.965338],[-4.700475,-7.889006],[1.202287,-3.530366],[-1.572939,-4.091170],[-4.622153,-2.882284],[4.766697,5.526227],[2.782386,4.494785],[3.711269,8.433768],[-1.729600,7.854934],[7.316162,-4.734316],[-9.475189,1.936867],[-1.942329,-0.525853],[6.129336,-1.100218],[-9.167847,0.469290],[-2.863219,9.647304],[0.945598,-1.836782],[-9.292769,7.570518],[6.720233,2.128869],[-5.515069,-9.111286],[-0.824771,6.933707],[-4.370301,-1.660683],[3.674584,-0.198893],[-0.873492,9.390367],[-6.782736,-3.879696],[3.312706,-8.617997],[1.098710,2.118429],[-0.217535,-7.289036],[-9.571629,3.452307],[1.031936,-9.374230],[4.205146,-4.727634],[-7.450188,5.202947],[6.277524,-4.517267],[3.204499,0.091463],[-7.518086,-0.090391],[-1.631481,1.391180],[-2.778013,2.850061],[9.435730,6.461827],[-1.709059,-6.859737],[3.333020,0.493573],[3.299707,-5.595196],[2.641391,7.438673],[-1.530734,-3.662147],[-8.291668,7.954934],[-5.136108,-0.785363],[-6.375238,-6.078102],[7.083302,-6.229831],[2.084602,2.482454],[8.237173,4.833574],[2.794342,-3.030283],[1.709514,3.345806],[-5.434177,-5.791308],[6.761839,-7.772516],[-2.626800,5.078122],[-9.186688,7.420663],[9.923420,-3.716560],[-2.328070,4.926620],[3.913079,8.567934],[2.375223,-3.685314],[6.013466,-4.398904],[-0.207310,6.921388],[-7.217844,-8.536293],[-5.603061,-9.820739],[4.292221,-8.295281],[-0.599302,3.092076],[5.804839,-0.403961],[5.396822,-2.956328],[-9.291211,-7.856733],[-4.798729,8.706494],[-7.235338,3.845872],[8.559669,-8.440220],[-0.239306,-2.187183],[9.016357,-8.771094],[-9.047597,0.419671],[-6.241702,3.208415],[-4.439122,4.664025],[2.557590,4.473052],[-4.385435,-2.516491],[-2.499538,-1.263782],[6.452607,-7.671014],[5.962516,4.606310],[5.337059,1.209259],[-8.015815,-2.298724],[-5.348030,9.298015],[3.833256,5.440960],[6.042667,5.509424],[9.009837,5.213931],[8.623813,8.720146],[-1.751368,-9.516702],[6.648889,1.731201],[-0.579402,-7.260739],[8.644786,-0.954554],[5.236049,6.804203],[9.805998,-8.042271],[-5.427535,0.477146],[2.490625,-3.281573],[7.596926,-7.408011],[0.343508,7.078298],[2.697705,-3.541610],[6.472309,3.569522],[2.945193,-3.917889],[-6.915418,1.473200],[-9.638580,-9.642853],[7.798639,6.912604],[7.904291,0.801697],[-3.103463,4.358167],[-7.069495,-8.776065],[-9.293885,-7.185210],[-0.407748,6.601161],[-7.161228,-9.114214],[4.724739,-4.712501],[6.352037,-6.155332],[3.658360,4.178021],[-6.608727,-4.326090],[8.986076,-1.993622],[-1.906830,1.258687],[3.986247,7.742167],[9.300417,-2.244812],[-2.093344,6.244439],[6.101946,0.146168],[0.175417,-6.352222],[8.272045,-9.430729],[4.853555,-0.162094],[-6.636924,4.940063],[-5.446963,6.501631],[-5.352505,0.031836],[-0.143399,-7.346112],[-3.781011,6.200473],[4.678134,8.140680],[-5.629665,9.898271],[-4.423475,2.164025],[9.845737,0.188256],[-2.676018,9.176825],[-9.411091,6.301094],[5.493831,-8.606136],[6.703989,7.974817],[2.390718,0.217125],[-9.861704,-3.410392],[5.338989,1.889155],[-0.733956,-6.634126],[5.638673,5.948167],[-8.066364,6.747592],[-1.137456,7.664509],[0.586512,-6.851144],[7.011416,-1.141357],[-5.007389,9.794557],[-5.927094,-4.680946],[6.436039,4.107594],[-2.970103,-4.427730],[-0.947959,-0.025408],[-8.356747,-7.614809],[-1.715955,-3.065375],[7.473582,-9.290650],[0.809096,6.873670],[-5.660994,-1.926330],[-7.551354,1.704748],[-4.486689,-1.570238],[4.645601,-3.060460],[-1.332856,8.316806],[3.857972,2.731211],[-2.201879,8.177553],[2.012736,1.594952],[-5.078800,4.497625],[-9.450337,-1.959199],[-9.606452,4.357991],[5.691427,7.982190],[-4.763895,3.640359],[9.025574,-2.223180],[-0.250184,5.662520],[-0.287440,7.958913],[0.902693,-0.310545],[3.848990,-8.511063],[6.752126,8.758854],[6.297209,-2.934987],[7.482541,-7.388846],[-8.201558,-4.071253],[-8.527528,-0.891922],[5.570425,8.460701],[-3.583700,-2.178958],[-5.003362,-0.757387],[-9.609470,2.172433],[-3.303012,8.846061],[8.814200,-3.618132],[4.941370,-7.554402],[0.057993,-5.268188],[-8.471268,3.657152],[7.638951,8.281808],[-3.968209,0.726731],[1.141460,4.929241],[3.071590,-4.112087],[-6.479225,-5.789708],[8.617025,8.844150],[-1.069743,9.163028],[6.630100,7.523485],[-6.252732,9.058352],[-4.610087,8.876444],[8.426143,-6.363054],[-2.038185,8.614083],[6.821065,-4.560166],[-7.129177,7.430353],[6.057870,1.200698],[4.812661,-8.043129],[8.183027,1.557368],[-9.086514,-3.987290],[7.347354,-1.723313],[1.800801,-5.906981],[-5.048246,6.110134],[-8.738742,1.287572],[-4.153864,-9.077214],[4.262095,7.515181],[-6.842271,3.472049],[-1.126755,-0.067509],[-5.332765,3.356561],[-8.563267,-7.123763],[-0.726516,9.177746],[5.216060,-2.546525],[-6.416788,8.183317],[3.301399,-7.020707],[9.203292,4.177708],[5.269067,3.283948],[-9.443736,7.567639],[-8.254012,3.928300],[-6.385993,7.241187],[2.404591,6.713076],[3.244054,-0.311228],[9.784569,-2.301992],[-7.111886,-2.054440],[-8.579476,8.189354],[-4.580560,0.161978],[-9.283882,7.608668],[-9.525425,-1.881475],[7.878793,4.896482],[0.854809,0.648046],[-5.627161,2.359821],[2.853502,8.236691],[-6.066334,1.814557],[8.049570,0.089678],[2.335990,-0.909064],[-7.699721,-2.221569],[-7.971879,-5.474908],[7.452230,0.517549],[9.772844,-9.432973],[-3.216947,-2.714660],[-8.741210,-4.926522],[3.744607,5.569200],[-5.291291,-9.458551],[6.122652,-4.614683],[-2.676543,2.492713],[5.890379,2.322640],[3.523500,8.307996],[8.474421,-7.972953],[7.000579,-6.046678],[3.178750,-5.393866],[1.787555,-8.636478],[6.087074,6.278095],[2.488565,9.307439],[5.674484,5.193290],[-5.435906,-6.095178],[7.311981,4.321805],[8.588146,5.985726],[7.013427,5.190591],[-7.839014,7.899283],[-1.017742,2.304410],[5.383869,-3.886580],[6.593772,-0.476630],[1.331784,-3.471572],[8.068760,4.365641],[4.011268,3.990801],[-5.440464,8.477714],[-2.830286,-5.312336],[3.617271,-1.132892],[-5.210313,3.498811],[9.903342,3.599200],[3.816547,5.911239],[5.349956,6.686848],[3.430961,-4.140331],[5.882722,-9.400330],[-5.618335,1.451253],[-1.480438,7.389755],[-2.872120,-8.706762],[-3.267157,-3.561440],[4.895951,-9.360623],[6.798328,5.411620],[8.789993,-7.896954],[-5.081794,-5.443222],[-9.605614,-0.551909],[-5.545697,6.197407],[7.976528,-4.401710],[-8.864237,3.821935],[-2.410006,-2.579975],[2.805581,-6.796965],[0.220016,-1.096886],[1.752973,5.768061],[-0.934603,-6.798092],[4.765861,1.542180],[8.864753,-5.673109],[2.154846,-0.688298],[5.512439,0.690651],[-8.552769,9.209899],[-5.389375,5.592718],[0.266658,0.597442],[2.015886,-9.705078],[-0.736836,5.655769],[6.955255,9.311497],[4.827346,-2.418413],[-2.861960,0.548227],[1.257827,6.935056],[-9.937831,8.966704],[5.942190,6.561084],[-8.075106,1.277792],[-3.064349,-7.498769],[-1.675501,-5.280383],[4.891344,-2.005309],[-6.096863,0.088013],[9.143213,6.050845],[8.283749,3.769939],[-6.872419,5.343347],[-2.426882,2.257397],[4.941293,-7.476148],[3.297842,5.777354],[3.780991,-7.432518],[-8.846515,7.613070],[-9.092185,7.160645],[7.838299,-5.128171],[-9.027856,-9.832289],[-3.355673,5.768824],[9.705287,0.249149],[-0.346167,-5.910813],[1.977997,1.519790],[-5.579476,4.876176],[8.919422,-5.695079],[9.816215,-5.588037],[6.606070,-4.313275],[-8.682242,1.351841],[2.499049,-3.950797],[-4.888501,4.243609],[-5.859391,5.564206],[2.451592,8.126600],[7.648777,6.361844],[3.805289,-6.456421],[-7.285711,-0.621545],[-5.861105,-3.406033],[5.531875,0.843430],[1.327542,3.453453],[5.137041,-5.103264],[5.889176,-6.746603],[-7.587875,0.377043],[6.686881,-2.738029],[-7.850044,4.665112],[-0.935512,-2.403463],[-1.617721,4.630867],[-1.595414,5.109260],[0.094756,-5.717819],[-2.768820,-0.233689],[-8.337418,-6.392149],[5.562027,0.675417],[7.867676,5.749565],[-0.175754,1.349832],[2.004030,6.418393],[0.089443,-1.932182],[-7.771807,0.952275],[8.750150,8.274252],[3.099733,6.947580],[-9.021978,-0.542827],[8.585767,-7.866866],[4.213170,7.309782],[-0.085914,-5.940695],[5.829568,6.397997],[4.172832,-2.631956],[-6.724476,-5.457280],[4.744548,-5.537959],[-1.802175,-6.415170],[-7.229640,-3.324005],[-6.473891,5.836305],[-5.824509,3.159693],[-6.896094,7.441520],[9.914339,-7.406771],[-7.357462,-9.371263],[-6.609744,1.915836],[2.618629,3.798979],[-6.107541,-7.683587],[6.778481,-4.159502],[4.584210,4.994809],[-9.863970,-1.967454],[4.958796,9.722984],[3.724460,3.818279],[-0.049567,0.793694],[-1.822376,-9.698263],[-4.637318,-1.714484],[-1.734916,4.431262],[-1.268336,0.668453],[5.264597,-7.142802],[-0.846102,-0.805774],[0.150893,0.308506],[7.272704,-3.790797],[0.506083,-3.586041],[5.459834,6.493407],[9.089837,5.422511],[-1.457201,-3.894817],[-2.757589,-4.594592],[-8.715529,6.968645],[-3.266859,-4.756086],[3.719305,-2.227874],[4.456824,-7.469020],[9.642794,-5.952776],[-2.324647,-2.439129],[-7.112034,-9.276529],[1.343880,7.018044],[-4.361212,-0.263242],[5.778569,-6.076145],[9.774327,-6.705119],[5.965283,1.523329],[-8.386253,-9.822376],[2.693421,1.409563],[6.937039,1.315802],[-1.501892,2.510360],[6.280115,-7.426424],[-3.783978,6.213158],[9.073075,-8.190443],[-6.555839,4.930138],[7.718528,4.170340],[-6.445289,-2.867313],[-9.962082,-6.420226],[-7.720902,1.750098],[8.146955,-7.195562],[-5.840595,1.110489],[2.358528,2.298500],[9.817663,1.272624],[-3.535471,-9.104491],[7.126413,-4.495560],[-1.947538,5.713616],[-7.969837,-3.357915],[-6.239449,6.267970],[-8.670965,-5.343372],[-6.710933,5.925901],[-0.562351,-7.886856],[0.780521,5.831478],[8.352217,-7.847590],[-2.933134,-7.614351],[4.043561,4.753536],[-6.792741,-1.674602],[6.249677,-4.344927],[-1.980748,-3.502457],[-5.855120,7.243485],[1.708104,2.562246],[5.845566,-6.430088],[1.570570,-4.569954],[9.738547,-0.346304],[7.799976,-5.385124],[4.320213,-4.580282],[-5.189935,-8.663931],[-5.497968,-2.395208],[-9.532697,-7.655575],[4.751990,9.269169],[-4.476794,0.600240],[4.975340,6.222893],[9.533114,-2.034016],[-3.435158,-2.028396],[7.914524,-8.904220],[1.122718,2.880836],[-7.117644,2.549148],[-8.293039,-7.452012],[-4.210369,-1.368148],[1.542911,-3.148299],[5.179740,8.330834],[-1.733900,-6.579587],[-1.406554,5.933011],[2.220384,2.628038],[-7.918643,4.066822],[9.034524,6.779755],[-8.011718,-1.641107],[7.542961,-6.803031],[8.222159,1.510057],[9.978256,1.291409],[-0.826752,7.556792],[9.679288,3.524471],[3.155974,-1.658984],[-9.754740,8.528544],[6.615171,-6.014543],[-4.292329,6.368404],[-3.645549,2.935318],[-3.487568,3.705333],[4.307827,-7.799504],[3.587189,0.270875],[-3.333103,6.594283],[6.938017,9.069757],[-7.637063,-6.120240],[-4.757741,-7.408228],[-0.022382,0.492237],[-8.989346,2.229465],[7.902689,-5.191394],[9.109080,-7.979750],[6.350222,-4.855905],[-5.626464,9.608989],[0.856449,0.499755],[2.173676,-0.152778],[-5.657689,-3.543500],[-6.755400,-8.425402],[9.767381,-2.635097],[-9.847499,2.904615],[-3.966204,0.811263],[1.996113,-9.064436],[-0.521347,3.796740],[3.182773,6.575832],[4.571937,9.366789],[6.865024,1.092188],[-5.804007,5.360027],[-9.264848,2.373061],[-6.398028,1.281910],[8.275610,-7.148924],[-3.269841,-5.481770],[8.088167,4.673382],[2.466115,-0.321537],[-8.434119,-0.610683],[3.202787,-1.222014],[-3.527416,-2.848145],[-7.418478,-4.132471],[4.831927,7.937750],[-3.073568,-4.363426],[3.334876,-4.496563],[-9.893225,4.731182],[8.728199,0.618249],[8.069683,-2.180223],[2.942718,-5.361481],[2.201568,-8.015270],[1.281191,-6.189551],[9.151382,2.826112],[-0.834242,2.510082],[-0.618269,7.101514],[-0.955842,-6.551621],[-1.821144,2.344826],[8.670780,9.078904],[6.764196,-2.042090],[4.698851,-6.248863],[0.175731,9.910874],[-5.838388,-2.347196],[8.325419,-2.550308],[-9.273987,0.331043],[5.512822,3.436368],[-6.392618,5.628318],[-8.056807,-2.902685],[-6.685827,-5.027137],[-4.090132,3.583619],[-0.624786,7.252842],[-2.599977,-9.146816],[-1.114747,0.338601],[-7.009397,7.154995],[-4.469555,-5.064802],[-9.913483,-1.017445],[-6.284566,-5.979652],[5.997604,6.822758],[7.331366,1.856673],[-2.355595,-7.887814],[-7.721553,-5.945836],[-5.740728,1.592856],[1.921479,5.460198],[9.641337,-8.568960],[-2.787811,-6.648645],[0.091308,-6.196914],[6.368819,-2.931587],[8.973319,-7.153290],[-3.222348,-0.563222],[-0.018209,7.026745],[-7.219694,2.054432],[0.174902,5.797675],[-8.317375,0.771983],[6.286928,-7.516583],[6.431131,-8.771625],[-3.354551,-9.663886],[0.982344,8.127002],[6.929112,1.055050],[-4.012373,1.647314],[2.520325,8.607404],[-1.432006,8.416915],[-5.290352,-0.104610],[-3.089048,-7.167645],[-6.372555,3.228550],[-8.466956,2.470637],[-0.678896,1.337478],[-5.360956,-3.472430],[1.294095,4.582252],[-8.103292,9.124015],[8.448092,-3.914937],[-1.590416,-6.562462],[-2.215002,-5.477126],[-4.692384,-5.326228],[4.232838,4.753061],[-6.585515,3.647038],[-4.884314,8.765598],[6.549856,6.445846],[5.716839,-4.858661],[6.245165,-9.454049],[-9.722965,-7.995868],[-3.531495,4.242553],[-3.608477,7.999852],[-5.590027,-8.882337],[-6.862850,4.104946],[-1.132891,-9.273636],[8.341952,2.002599],[1.885269,-2.876358],[-4.586779,-9.942696],[7.510580,-0.887350],[6.963923,-8.956111],[-3.628724,-9.147041],[-0.826228,-3.433191],[-8.171598,-7.987392],[6.785558,-8.601156],[5.371154,6.948395],[9.359476,4.904000],[9.377457,-4.327472],[7.785279,4.084692],[8.172690,-5.889862],[5.201795,-1.678683],[6.182454,9.880420],[-4.578867,0.968913],[-7.578345,-4.855208],[7.246337,-7.318722],[9.511620,9.612939],[6.176908,1.599900],[-9.652474,4.530529],[-2.794741,5.399958],[-6.721891,6.743929],[4.871328,9.108151],[9.129172,7.663574],[4.513027,5.912752],[4.241560,6.784233],[7.839183,5.662871],[6.097080,-7.315148],[0.601988,8.695317],[-1.571319,-1.211318],[-0.049041,-8.645004],[9.568284,-0.548960],[2.763391,-3.818344],[-0.696255,-9.103301],[-9.560423,3.755380],[-3.268608,3.742155],[4.843860,1.289685],[6.368334,8.355759],[9.898793,8.555052],[-3.378311,8.474047],[-9.460468,-9.407047],[-1.295527,-6.180333],[-9.233806,-4.783854],[9.862164,-5.233367],[-8.909051,7.981429],[-2.865149,7.452038],[-5.130568,-8.771870],[-3.551578,-5.142262],[1.302213,6.549389],[7.544110,-5.303943],[3.234962,-0.533970],[2.483650,-7.092490],[4.486420,3.415721],[-7.416573,0.620434],[-8.056560,8.998176],[-4.160923,7.704447],[-8.628646,3.617470],[-7.525923,-8.149825],[-3.948136,4.371424],[9.819536,5.489270],[3.756156,-5.077426],[-0.327701,-1.001770],[-5.496280,0.987187],[2.354321,-2.251030],[-4.738386,-8.113321],[-7.189250,-6.702073],[2.548480,-4.048021],[5.533450,2.148065],[-4.724368,0.901540],[-1.867021,5.721602],[2.389446,4.649162],[7.420646,3.707317],[4.332755,3.633964],[-1.932767,-2.731536],[0.982590,-5.078156],[-8.838224,2.495140],[-1.752157,0.258236],[-0.237621,0.617544],[-9.649921,-4.708596],[-6.836035,8.891856],[6.548429,7.342335],[-3.423010,-2.877989],[-0.738419,3.216513],[-5.958031,-3.107833],[3.435638,7.175134],[-8.985817,8.820136],[4.374359,9.522376],[7.651788,3.154020],[5.964241,-9.938979],[-8.566217,5.375316],[-6.540438,-2.002870],[1.392624,3.725539],[-2.595978,-4.638351],[9.534881,3.714270],[0.444113,-2.849919],[5.787548,-3.203154],[9.322767,6.149516],[1.964724,-8.148708],[5.219510,-7.285670],[2.306826,8.100549],[6.578998,1.592157],[6.659065,2.361033],[1.626207,-7.362556],[-1.183795,2.755086],[3.607783,9.257189],[6.157504,-7.484863],[-5.106604,0.952301],[-6.530358,-8.094267],[-2.166598,-6.981555],[-5.538938,-2.001430],[-1.345751,1.415531],[5.210745,-8.123730],[0.189954,1.504181],[7.253340,3.958117],[7.457722,-5.914368],[6.103008,5.395970],[-4.948246,2.173940],[8.088706,-9.599506],[-6.871980,-2.214850],[-2.085106,5.428896],[3.484818,-1.253544],[-1.238750,-2.374778],[-9.521485,-9.959336],[0.711036,1.135825],[9.021370,7.621121],[-6.867186,-9.108943],[3.330616,0.942656],[9.386127,7.786032],[7.049914,-3.128066],[1.584258,1.690532],[0.607233,7.209832],[4.317973,-3.106165],[8.559339,-0.780777],[1.960571,9.141098],[7.721831,-0.135795],[4.257446,0.481406],[3.561770,-3.057882],[0.533191,-5.745976],[2.572267,3.661907],[-0.305235,-5.171426],[7.202912,4.329256],[9.116688,5.420934],[9.586358,-1.876166],[4.944787,-2.448878],[2.794966,6.520373],[-5.230202,6.402648],[9.082968,0.938258],[-5.785773,-6.864010],[-4.805572,-1.597232],[-5.083072,-6.552656],[9.813479,-2.488124],[1.036485,2.847612],[9.633763,7.698239],[-4.828774,-2.402139],[1.481254,4.101329],[5.649340,-9.091650],[7.428960,6.674168],[-1.124004,-9.943045],[-5.627121,5.436483],[7.764897,-7.630693],[3.744715,-2.635694],[-5.736704,-4.948456],[-3.296455,9.926449],[4.465316,5.755136],[-6.506007,-6.834834],[1.768287,-7.569930],[1.753640,9.053808],[-1.659445,7.683398],[2.522547,0.633096],[-1.891575,1.835965],[5.522434,-8.885290],[-2.562500,-1.042175],[9.640887,-4.725344],[9.648400,-8.903803],[-9.909902,7.426375],[-1.450921,-2.944981],[-5.307713,3.844719],[7.322097,-4.976188],[-9.350444,3.569157],[-5.976347,3.271622],[-0.284695,-6.215771],[1.538644,-6.588350],[-9.521974,-2.913274],[2.408275,-2.916986],[9.821219,-2.102847],[0.645267,3.628276],[-9.871864,-9.329460],[-6.900392,-0.185730],[2.885217,-3.020206],[8.542383,-3.948484],[-9.249032,-0.443370],[-0.117915,-4.352924],[6.381666,-8.525179],[7.766594,-6.932338],[2.814448,-4.587812],[-2.064598,-4.889567],[-1.105993,-6.634791],[-2.623402,8.391723],[-9.164733,-0.614814],[5.719707,-1.221168],[2.388638,0.973959],[-0.975676,-5.236621],[-3.067299,-7.956066],[2.432442,7.674167],[9.281673,-3.798755],[-0.565575,6.555294],[7.978142,5.669239],[-2.636940,5.389566],[5.696059,-6.735791],[-5.290060,6.207422],[5.342629,-2.578948],[-8.053394,-4.000017],[9.771231,8.609231],[7.041365,-8.795699],[-3.103769,6.869287],[9.717246,2.400873],[3.076330,0.683429],[-5.106928,-6.642255],[-6.124470,1.180229],[-0.163591,-3.207523],[-1.767278,-1.396132],[-0.515922,-7.327187],[-5.136881,8.517458],[4.502404,-2.749580],[-4.584898,-5.434219],[-4.317133,1.698405],[9.587902,-4.252376],[-0.042155,-0.369912],[-5.775695,-3.515240],[7.294352,-0.311746],[-4.364090,-0.269790],[-1.212641,-1.470974],[-9.844226,5.133385],[-5.182494,9.940353],[2.811138,4.681920],[-2.503119,-5.613734],[-2.533612,-8.916846],[-2.560941,-3.790786],[-4.480175,-9.634199],[2.657213,-5.610963],[8.305402,8.707009],[-8.336232,-7.458872],[-6.855594,5.148804],[2.102920,8.760631],[2.253557,4.746822],[-0.447805,-6.030141],[-4.752429,9.745194],[-5.546972,0.969991],[-0.605081,1.640596],[3.940262,-1.823015],[7.880374,4.849430],[-7.984401,2.438847],[-6.480564,2.264363],[-6.376438,0.654549],[-7.480342,-4.500632],[-2.687078,-5.174383],[-6.628440,1.984702],[9.674842,1.272523],[-3.637864,5.564758],[-0.967451,-4.962861],[-2.353074,2.863063],[0.730584,7.085159],[-2.324932,-3.081558],[-5.157809,4.138792],[-1.331604,-6.169848],[-1.343003,3.149454],[-9.514860,4.780655],[1.745641,1.615164],[3.623871,-9.750291],[-8.759178,-1.431023],[1.419182,8.045785],[-8.114440,0.428705],[-3.001864,-2.107576],[4.037428,2.365197],[2.013344,-1.057759],[-2.078648,-0.237369],[8.460791,-7.293667],[-3.341275,-3.971733],[-6.778942,1.286699],[-8.869947,5.437703],[6.630724,9.115228],[0.993669,-8.881574],[-4.897566,5.659486],[0.505399,-8.519649],[-7.148488,-1.156150],[-4.202223,5.531944],[-8.777790,9.077411],[0.441972,9.964727],[-2.300669,6.796993],[0.874754,-0.830496],[9.126228,-4.622289],[5.703665,1.216855],[-4.411070,2.079205],[-8.231494,7.392613],[7.884041,0.238421],[3.794166,9.573951],[7.165071,-5.915379],[4.270142,-0.084136],[-2.951186,6.150413],[-3.846988,-6.454783],[-2.978041,7.849138],[-2.513924,5.599431],[2.807426,-4.635488],[-2.586911,-0.360710],[-5.675375,-6.264516],[-6.965183,-5.414832],[-1.274809,-1.268995],[-2.884481,5.304219],[-5.511252,1.245098],[4.583239,9.951278],[2.315996,3.315673],[1.105811,-4.505175],[-9.353238,9.173652],[4.925747,-2.162632],[6.312114,-5.465414],[5.282754,-3.234646],[-8.967248,-3.617934],[3.155906,-5.462639],[6.238504,-9.205770],[-4.980457,-4.910221],[7.644095,8.764523],[-7.039159,-4.935933],[-1.757744,0.492434],[-2.511174,-1.484933],[-6.187295,-3.963330],[-2.828429,-5.519307],[8.335400,-8.410044],[4.497724,-3.940263],[3.998426,-2.914209],[9.154605,1.811316],[3.818273,5.049902],[1.987662,8.520047],[-5.237003,7.193230],[-4.808761,-6.057902],[-3.619299,6.248121],[-2.136583,-8.028726],[1.895641,2.735106],[-9.371315,9.258335],[1.369696,4.580828],[-2.450226,-8.673578],[3.213994,3.515196],[-6.496841,0.994567],[-6.223174,-1.992646],[-5.285726,-6.888649],[3.165068,6.470929],[7.116373,-9.958503],[4.189339,1.275440],[-2.287750,6.466892],[5.791742,7.166010],[-2.322705,-0.451045],[-5.465364,8.569053],[8.865322,-0.223503],[5.680287,-0.292961],[-2.809255,-6.578109],[4.294649,1.697569],[3.742378,5.692606],[5.563659,-3.098882],[6.324259,4.462655],[-7.333667,-6.650990],[-8.774447,-1.839167],[-0.407554,-0.043868],[4.824479,8.497354],[-9.922232,-4.764231],[1.379573,-6.752554],[0.302857,-2.336468],[2.855659,-1.347256],[7.012157,-8.546618],[5.998783,0.671727],[1.563945,7.051341],[-5.820916,2.313732],[9.992810,7.220987],[3.340954,-0.088940],[-1.222291,9.749684],[-2.625189,2.240864],[1.308468,6.040066],[8.078413,-8.587821],[1.946131,9.288618],[-6.827560,-6.521772],[9.561605,-7.377920],[-4.238889,5.915670],[-4.901902,-8.286625],[-0.420260,-1.914282],[3.554998,-8.968353],[-8.279738,-7.649163],[-1.486606,-2.525938],[-9.200652,7.111099],[-9.729422,4.768588],[-3.715836,0.752460],[4.790619,6.479751],[-8.679822,3.153800],[6.129130,-0.231057],[8.157230,4.749138],[-8.915680,-3.083015],[7.673509,-6.398393],[-0.345460,-1.747848],[-7.228835,1.935445],[2.913737,5.098354],[-1.552523,-8.407379],[0.253226,5.138564],[1.597303,-2.103361],[-5.359729,-9.510426],[-5.751329,9.721627],[-7.939581,0.509035],[-2.484871,4.292525],[0.783411,9.496270],[5.337441,-4.790907],[-2.499271,0.066186],[-4.625212,3.355440],[6.738295,-3.099065],[6.189286,-6.517955],[2.302913,-5.830666],[-4.282050,-6.925486],[6.741937,4.817073],[3.553462,0.220887],[6.046154,7.458303],[-2.658931,6.789645],[-0.825349,-9.929964],[2.300902,-8.883296],[-0.856381,-9.805830],[-9.106420,4.754018],[-8.071054,-2.909236],[-2.928355,0.030495],[7.609831,4.150986],[-4.110432,8.404254],[1.090550,-1.987048],[-6.039813,5.716960],[1.677168,2.219027],[-3.385079,6.659612],[1.783180,-6.702505],[8.210313,7.502603],[-6.444582,6.743075],[7.397972,-0.089606],[-6.732095,-1.146420],[8.369564,8.303750],[5.645842,-3.985631],[2.934256,9.565113],[8.164061,-8.211142],[2.110372,4.613037],[7.745750,-1.899491],[8.093588,0.108486],[4.245459,-4.021029],[7.877571,-4.768252],[-5.244000,5.638355],[-5.950351,-0.453777],[-5.020888,9.767902],[3.691550,-6.198025],[9.306907,2.474548],[9.099548,-3.172553],[-9.706390,0.115311],[-3.688425,7.693764],[-2.454951,5.684389],[9.378568,-3.065541],[-6.136858,4.935388],[9.190514,-5.242897],[9.796111,8.679385],[-2.992083,5.872925],[8.907211,5.089830],[-4.437738,-7.094127],[4.892751,-2.921517],[-7.321233,-5.764490],[-2.838556,-5.162442],[5.737506,-0.181023],[-9.776738,4.797453],[2.241420,-4.203434],[1.809153,-6.378970],[-2.058256,-5.964432],[-6.858391,-0.739478],[-9.119671,-2.808081],[-2.049894,-2.016422],[3.302675,-8.844277],[-4.457753,7.867291],[2.047118,-5.452986],[2.843365,-2.169869],[-4.204501,3.959632],[8.765684,3.227543],[-3.261661,-2.682236],[-9.631344,9.079417],[4.364463,4.852270],[9.199294,0.420038],[-3.401038,-9.026614],[1.499000,0.359961],[4.052326,-6.454920],[-1.821789,-9.161791],[4.821030,-4.168019],[7.601504,-9.780823],[1.847792,8.395208],[-5.728810,9.018310],[-2.550926,-4.319744],[4.590663,9.518584],[-0.749735,3.663612],[1.219253,5.599495],[8.635940,-4.212574],[7.285406,8.929032],[3.229668,-4.236875],[-6.401583,-9.698484],[6.326840,-2.650231],[0.602998,7.288207],[8.503942,-5.387533],[4.655835,-0.520250],[0.399918,3.780492],[7.765044,-7.558868],[5.722162,-9.547031],[-3.028112,2.155822],[5.501162,-8.033330],[0.896681,-3.033508],[5.439161,-9.384631],[-9.108122,5.487613],[7.184947,1.551774],[2.537575,3.172293],[-7.922858,-2.084761],[2.601735,-7.098490],[2.568730,3.399491],[-5.304523,-2.883552],[-9.705506,-5.070452],[3.054760,6.697108],[3.265692,3.652936],[-7.611806,6.369581],[-8.989326,2.460706],[8.901535,-2.734262],[6.549647,-6.214302],[3.804433,7.509717],[7.501035,-3.950800],[2.886455,6.902076],[-8.882829,4.224960],[-0.312466,9.009826],[5.847784,-9.155314],[-2.133109,1.894648],[-1.221407,-4.540575],[-5.578247,5.466929],[0.842910,-7.074742],[7.521156,4.937220],[-5.310917,-9.149846],[-5.697891,2.014174],[2.043293,-7.557394],[-5.928742,8.966206],[7.218923,-5.221817],[3.881782,5.063426],[-4.096499,7.693572]], dtype = "float32")#candidate|10614|(2640, 2)|const|float32
call_10613 = relay.TupleGetItem(func_8345_call(relay.reshape(const_10614.astype('float32'), [352, 15])), 2)
call_10615 = relay.TupleGetItem(func_8348_call(relay.reshape(const_10614.astype('float32'), [352, 15])), 2)
func_10012_call = mod.get_global_var('func_10012')
func_10014_call = mutated_mod.get_global_var('func_10014')
call_10621 = relay.TupleGetItem(func_10012_call(), 1)
call_10622 = relay.TupleGetItem(func_10014_call(), 1)
bop_10624 = relay.bitwise_or(call_10621.astype('uint32'), call_10613.astype('uint32')) # shape=(10, 352, 7)
bop_10627 = relay.bitwise_or(call_10622.astype('uint32'), call_10615.astype('uint32')) # shape=(10, 352, 7)
const_10628 = relay.const([[[True,True,True,False,False,False,True],[False,False,False,False,True,False,True],[True,False,True,False,True,True,True],[False,True,False,False,True,True,False],[False,False,False,False,True,False,False],[True,False,True,False,False,False,False]],[[True,False,True,True,False,False,True],[True,True,False,True,False,False,True],[True,True,True,False,True,True,False],[False,True,False,False,True,True,False],[False,True,False,True,True,True,False],[True,True,True,False,False,True,True]],[[True,False,False,False,True,True,False],[True,True,False,True,False,False,True],[False,False,True,False,True,True,True],[True,False,False,False,True,True,True],[False,True,False,True,True,True,True],[False,False,False,True,True,False,True]],[[False,True,False,False,True,False,False],[False,True,True,True,False,True,False],[True,True,True,True,False,True,False],[True,False,False,True,True,False,True],[False,False,False,False,True,False,False],[False,False,False,True,False,False,False]],[[False,True,False,True,False,True,True],[False,True,True,True,True,True,True],[False,True,False,True,False,False,True],[True,False,False,False,True,False,True],[True,False,True,True,False,False,False],[False,True,True,True,False,True,False]],[[False,False,True,False,False,True,True],[False,True,True,True,False,True,True],[True,True,False,False,False,False,True],[False,False,True,False,True,True,True],[False,False,False,False,False,True,False],[False,True,False,False,False,True,False]],[[False,False,True,True,True,False,True],[True,False,False,True,False,False,False],[True,True,True,True,True,True,True],[True,True,False,False,False,False,False],[False,True,False,True,True,False,False],[False,False,False,False,False,False,True]],[[False,False,True,True,True,True,True],[False,False,False,False,True,False,False],[True,False,False,False,True,True,True],[False,True,True,True,True,True,True],[True,False,False,True,False,False,False],[False,True,True,False,True,False,False]],[[True,False,False,False,True,True,False],[False,False,True,True,True,True,False],[False,False,True,True,False,True,False],[True,True,False,True,False,False,True],[False,False,False,True,False,False,True],[True,True,False,False,True,True,True]],[[False,False,True,False,True,False,True],[True,True,True,False,True,False,True],[True,False,True,True,False,True,False],[False,True,False,False,True,False,False],[False,True,True,True,False,False,True],[True,False,True,False,True,False,True]]], dtype = "bool")#candidate|10628|(10, 6, 7)|const|bool
bop_10629 = relay.bitwise_xor(call_10621.astype('int16'), const_10628.astype('int16')) # shape=(10, 6, 7)
bop_10632 = relay.bitwise_xor(call_10622.astype('int16'), const_10628.astype('int16')) # shape=(10, 6, 7)
const_10649 = relay.const([[4.332734,7.143705],[1.674150,-9.495585],[-4.823398,7.047491],[-9.231522,0.434967],[4.241756,-9.983492],[2.998640,7.628228],[-3.491606,0.419439],[-5.974574,-8.606633],[9.863377,-4.141841],[8.733637,-2.090424],[5.732951,-3.914162],[1.767653,5.041763],[-9.663390,-6.379275],[7.504402,-9.950501],[2.630392,5.715213],[2.815904,9.227940],[0.653061,9.454103],[3.329042,-7.015278],[-4.361305,-0.742830],[-9.175531,-3.895254],[6.480376,-7.395243],[-4.531779,8.516319],[-7.155269,-9.599257],[-3.198645,1.920218],[4.345789,-9.615339],[-0.596268,6.258739],[-6.485027,-6.411724],[8.785017,1.819715],[2.977608,-8.983296],[-6.864737,-2.621224],[-4.725858,-0.487569],[-0.727368,-2.220943],[5.965619,-1.002548],[-0.107491,-8.310015],[2.302477,3.277921],[3.374619,-0.395742],[9.867801,0.237911],[-0.494175,-2.821008],[-4.146688,6.798822],[-0.692064,-5.572979],[4.085358,0.704502],[-6.130216,-9.019152],[-2.451122,-2.572194],[-4.433434,5.987939],[5.662574,4.234969],[-4.576117,-1.413149],[9.162488,0.796873],[-8.995202,3.721233],[2.780334,6.061001],[-0.037162,7.467248],[7.689642,-6.179404],[-8.851343,1.350661],[-6.305930,0.367743],[2.592496,3.609021],[-3.612513,-4.855139],[-1.819353,-3.480710],[5.252218,4.898987],[5.200749,-7.012260],[9.043767,-7.092032],[-9.010519,7.278968],[-5.230186,0.616783],[6.596628,-8.458680],[-8.665000,-0.866292],[-9.893104,-5.284165],[-5.738996,8.050465],[-9.961407,-2.378392],[6.345508,-9.946993],[5.269777,-9.163484],[-4.803448,2.522129],[8.926965,9.860850],[-9.586239,-1.346184],[-9.320830,-4.173346],[7.134922,-0.231677],[-1.545518,8.862012],[2.700817,2.726331],[5.221462,2.189393],[-3.769129,9.384474],[-5.487744,9.987840],[-8.610165,-5.998494],[-5.167544,9.770671],[-7.887711,1.266786],[1.164445,-0.397602],[-7.401524,1.306311],[-1.240795,-3.757881],[5.127476,-1.552273],[-9.782915,-3.255940],[7.145434,-4.459142],[-8.482330,1.950933],[5.111734,2.599519],[1.583934,-9.968439],[2.344419,-1.681965],[-5.663826,-5.354240],[-2.202099,3.680846],[-0.871477,-8.181396],[-3.239128,6.770999],[-2.476447,-1.844501],[-7.663263,-5.079174],[2.953475,9.127491],[-4.317535,-7.714661],[-9.989033,-9.090044],[2.026574,-9.113776],[-7.921957,-1.117603],[4.552464,1.479923],[-0.253131,1.224342],[9.005498,5.014483],[-8.103455,5.221213],[-7.796081,2.133246],[0.023250,3.747274],[-5.542166,-7.603553],[-7.802937,4.827058],[1.568345,-8.439006],[-3.899956,-0.881723],[4.415928,4.416714],[-6.591954,5.250347],[-2.166458,-0.811750],[-2.641989,7.330361],[4.114762,5.991120],[-0.988647,3.208710],[8.446399,1.015871],[6.311507,3.996831],[0.510384,4.967007],[-1.868570,-2.306775],[2.772672,-8.459631],[0.346071,-5.715061],[9.153437,-7.220818],[6.052626,2.321536],[0.244738,-4.050480],[-7.390222,-5.470299],[-1.591943,-4.471904],[-4.836466,-2.438019],[3.449631,5.818512],[-5.091476,2.899534],[-4.092589,9.107662],[9.680906,-9.690917],[2.788312,2.657837],[2.611094,-7.977826],[8.381039,-0.275369],[3.803472,-9.792998],[3.324954,3.248945],[1.493409,3.313627],[0.486386,0.130879],[-6.044918,7.351403],[7.761237,0.666178],[-8.433099,-9.128362],[-2.826918,9.309408],[1.025577,-2.761633],[-7.134257,-4.931820],[-1.959759,1.811191],[-9.492565,-6.252768],[-0.490767,6.474462],[9.870686,-9.636389],[-5.131658,7.604277],[5.631311,-5.067502],[-6.278946,2.882584],[6.678576,3.066329],[-0.636815,5.321433],[4.040847,4.059426],[2.789472,9.036060],[8.494465,1.849892],[4.706002,6.992309],[2.791001,9.235633],[-1.372940,-2.771016],[5.556157,-7.053694],[-0.924987,-4.862198],[7.878474,-3.616229],[-3.558839,7.330944],[1.229755,8.541605],[-5.217249,-4.363896],[3.100180,7.736371],[-5.193117,6.043916],[0.406691,0.064775],[0.076329,-2.431563],[0.065906,6.542642],[-1.744009,-3.161419],[2.314987,-9.949718],[-7.475836,-5.465130],[4.253101,8.679592],[4.263028,2.473212],[-3.874877,5.829233],[-6.782955,6.465479],[-1.441746,-1.687668],[8.100441,-9.231396],[-6.882266,-1.620433],[2.234780,-3.682331],[4.270218,4.310137],[-5.728177,9.313319],[0.675314,-5.090428],[-9.617794,-8.846275],[7.359611,-5.275867],[9.743534,8.378269],[1.630911,-9.303799],[-5.197456,7.236575],[-9.600956,5.697362],[2.115842,-1.584043],[1.409884,2.767409],[-3.503468,-3.109740],[-2.529977,-2.809386],[6.178172,5.174906],[-5.360147,-0.450602],[8.723518,-1.059368],[-5.166121,-7.772662],[-1.614254,-6.266403],[-8.947199,-7.997490],[2.452715,-4.399038],[7.753328,2.036088],[-5.636049,2.671900],[-2.459496,-8.612942],[-0.009725,-9.115869],[-5.653232,-4.985491],[8.975278,-5.097687],[-9.542245,-9.544147],[5.086828,5.763924],[4.977919,8.713912],[-9.474937,-2.112944],[-8.179887,-0.611265],[9.862541,5.824178],[8.356390,2.651661],[5.776132,-0.055220],[-1.977628,9.996808],[9.353214,-7.659005],[-5.872512,9.961696],[-0.680224,2.953075],[-0.584447,1.246558],[-3.283371,5.697370],[9.211308,-4.848612],[-4.973486,-0.514155],[5.268850,-4.332380],[5.304564,-2.235614],[-7.526406,-2.293534],[9.258315,-5.446142],[9.730314,-9.373244],[-5.813172,7.903915],[-0.553647,-2.766608],[1.996222,0.371618],[1.664083,6.518127],[-7.273915,-0.024995],[4.972339,4.078801],[-1.543486,-3.995373],[-8.403703,-6.852148],[-9.054173,-6.262475],[0.669163,1.171820],[7.728841,-2.057183],[-0.299225,3.992486],[7.243163,-6.557600],[-2.954776,1.581969],[8.450437,-2.113093],[-0.557212,-8.145274],[5.769858,4.935148],[-4.915061,7.517978],[7.655440,-0.525439],[1.004224,-3.449440],[4.428331,-9.969323],[2.502049,-0.167730],[4.469255,-8.761357],[9.844771,0.031344],[2.115718,-6.847169],[9.770147,0.651494],[8.932813,6.689347],[-5.285926,2.368202],[-2.191570,2.027298],[2.794407,-7.923248],[6.336260,5.171003],[6.026166,5.367928],[1.224911,-5.699526],[3.826273,-9.790964],[5.003569,4.051833],[4.145069,8.669554],[-4.423174,1.382180],[1.804040,0.880614],[-8.464221,9.890274],[0.900769,-6.216835],[-6.148982,4.733101],[8.577910,-0.216686],[6.129408,-7.153296],[-0.817192,-4.213120],[-8.879057,1.404281],[2.569159,-4.544526],[9.076631,-2.381816],[-8.164549,1.979516],[3.256278,-6.385705],[-6.455433,-8.701291],[1.882840,6.106671],[-8.268458,-2.003786],[0.041724,-3.069115],[-9.586578,8.267140],[6.453756,-5.391026],[-9.098219,-8.459581],[4.681961,-2.696168],[-7.414590,8.462544],[6.494554,7.747639],[5.687384,9.212969],[7.322688,3.466362],[-5.021118,4.608830],[-9.699935,-9.068427],[-4.194039,0.696502],[5.171919,4.448350],[-3.483331,1.916472],[4.317222,3.415081],[1.102037,-9.925438],[6.471552,-2.107017],[-1.622222,8.424044],[-8.826891,0.787284],[-0.534200,-2.588634],[3.542163,1.596289],[-9.134421,2.202570],[-3.011139,-2.022712],[6.180190,-8.746919],[1.407313,7.355380],[4.165935,-8.397254],[-9.661509,-9.866658],[-4.754828,-4.743997],[-4.987448,0.088100],[0.788567,7.939949],[-8.449751,3.904127],[-1.743411,-4.497933],[-9.213024,4.093421],[-5.015971,5.103558],[4.310453,8.535800],[-9.975133,5.281921],[-0.959468,-0.404142],[-6.123958,4.654571],[8.581449,-2.006916],[-9.597917,3.011593],[-4.786674,-5.711948],[5.699984,8.091267],[6.296051,-7.553311],[0.022211,2.711950],[6.704559,8.290899],[9.789594,-9.087653],[6.923891,-3.369403],[1.187062,-1.028061],[-4.137176,-5.226869],[6.625277,-9.369088],[-0.190180,-5.201118],[6.960211,1.663594],[0.748381,-0.957002],[1.638954,-1.374419],[4.163074,2.360196],[-5.540408,0.333959],[-6.849860,-6.288290],[0.052369,0.830543],[-0.268436,6.480807],[9.266814,-2.693507],[2.973937,7.678341],[9.371556,5.623359],[-0.614121,6.608069],[8.319403,6.262274],[-9.720978,8.531728],[-1.713297,2.769748],[-5.927595,-9.345852],[-4.735334,3.976234],[5.482684,-9.935739],[-0.255374,-1.320700],[-9.645937,3.967371],[-5.072928,-0.541317],[6.123370,-2.741687],[-3.633057,-4.379744],[7.322521,-1.036548],[3.536503,2.261318],[-5.807266,2.399107],[-5.314981,8.100686],[2.094306,-7.557322],[4.142878,-2.406342],[-9.164253,-4.308050],[-6.291953,8.549768],[-4.481308,6.020750],[8.133805,-4.599454],[1.981730,-0.486984],[1.145094,-0.414743],[9.901615,-1.680153],[7.179219,6.307051],[-3.479000,-2.958491],[-0.263531,-4.513587],[3.655033,-1.934838],[-2.425871,-9.796261],[-9.027219,7.049755],[-0.523072,-2.403851],[-5.132916,-5.144474],[2.090923,0.161604],[-5.899795,-7.948231],[-0.604438,9.542254],[8.609029,-5.526928],[-4.973916,4.236273],[-4.408287,2.130690],[-9.688448,-9.764853],[-6.228517,5.601898],[-6.689660,1.467506],[-9.860188,1.053926],[-7.252576,6.607070],[-8.934876,-2.461987],[-4.580360,5.343569],[-2.154974,-0.753349],[-5.805361,-6.881389],[4.692090,-0.785953],[-3.312114,-3.184699],[6.042377,1.766838],[-4.856791,1.172502],[5.189565,-5.347875],[5.438790,-7.216412],[-0.564551,6.613343],[6.654207,9.079003],[2.070581,-6.205593],[-0.409938,-4.585535],[-8.434127,5.244482],[-8.414530,7.202080],[-2.227212,-0.597413],[5.338403,-0.426180],[6.271291,-0.299596],[6.297932,3.571562],[8.753222,-6.291708],[1.990297,2.270054],[2.654478,-6.164289],[-8.012505,8.414813],[4.489304,-3.874140],[-0.336620,-1.807102],[-2.172692,-2.273210],[1.499330,-0.992837],[4.856964,-2.330746],[-7.800376,-7.943658],[-1.753398,7.128382],[-8.181040,-4.834423],[-5.165548,-6.680690],[4.351532,-0.516521],[8.798702,6.826992],[7.304174,3.931210],[-5.135178,5.425692],[1.605325,-7.547290],[-4.945450,-8.315473],[-1.761372,2.827573],[-1.172798,2.933462],[-9.169361,2.929291],[-6.545713,-5.517897],[3.464007,-3.774361],[5.707841,-9.224420],[1.323255,9.857321],[-7.565248,-4.045908],[-4.882466,-7.040511],[6.727549,-4.862438],[3.984420,7.979162],[-5.645361,8.789713],[3.920525,9.985240],[5.647938,-3.168840],[1.738699,0.385526],[9.712903,-5.761605],[1.741348,-5.617909],[8.337904,-1.096694],[8.560859,-2.093708],[-5.888247,0.420470],[-6.840484,-0.763707],[-4.490548,-4.049654],[-8.020092,3.183173],[-8.006371,6.152153],[-4.902148,-5.844458],[-9.474288,4.371450],[4.861207,9.750105],[7.060725,1.714446],[-3.375436,-6.906040],[-5.619001,-6.627445],[-8.608350,2.677742],[0.281868,-5.474764],[-6.094042,0.200230],[3.509839,-5.935803],[1.971400,-7.671040],[-6.690962,-6.838418],[-7.274004,8.120683],[6.216458,4.988437],[-6.871822,-4.451705],[-6.351768,2.991927],[-5.563421,6.706016],[4.137032,-4.235279],[-5.979044,-8.834918],[-1.082840,6.590933],[0.378606,-0.791588],[-9.129512,-4.465626],[-6.212207,-5.860277],[2.168205,0.627164],[0.726165,1.865583],[1.754070,9.556415],[1.249724,-2.526807],[-9.895592,-0.669208],[0.986806,-5.491526],[-6.670635,-8.899752],[-0.744377,6.459557],[-1.813091,2.816132],[-2.350890,7.757265],[-7.895793,5.843966],[-7.040375,9.802405],[7.237926,-8.624978],[-9.916005,-4.976845],[8.158896,0.575705],[8.254499,8.532966],[-0.315645,0.706848],[3.665877,-5.982105],[2.593478,2.645104],[0.070757,-2.524152],[-2.114986,4.095509],[-6.017383,-6.439708],[-6.707099,9.780028],[-2.747539,-2.292542],[9.563672,9.676874],[-4.816796,-6.509655],[7.770512,8.432630],[-7.187261,7.140767],[-4.732411,-5.285598],[-6.013030,-5.035384],[-2.972976,5.561401],[-1.528203,2.171393],[7.862923,-6.849093],[-7.443564,-6.432837],[1.088335,8.117442],[7.571026,-2.488005],[5.293545,-1.059695],[4.788823,1.768691],[-5.439093,6.512389],[-1.780343,-6.526133],[8.204010,6.069687],[6.477705,-0.382916],[2.958036,3.529395],[-3.545779,-4.720029],[-8.485428,-2.212514],[8.442137,7.110566],[-3.933425,-1.257090],[-3.589046,-8.491173],[4.838789,7.711612],[1.249898,8.666851],[7.634276,-4.357582],[8.784018,-7.193513],[3.476324,5.122831],[-3.726200,4.032090],[2.195841,1.137212],[-8.313141,-6.769734],[6.059689,2.975676],[9.264005,3.435403],[7.757142,-0.119502],[-9.926624,-9.122275],[4.267170,-1.871547],[-7.119648,-9.463436],[2.375337,7.303686],[-5.224022,2.878875],[-9.486718,-7.660209],[-1.314496,-5.717274],[9.630485,-1.600454],[4.987788,-6.001255],[-2.607939,-2.368669],[-4.692709,8.184196],[-2.351126,2.072380],[-2.051262,-0.087608],[6.226188,-2.659310],[-0.657080,5.725963],[5.081518,9.974782],[-4.673121,-6.035157],[-9.036315,-8.806831],[5.358912,-3.208043],[-8.317529,-6.268607],[3.696270,3.221409],[-7.985534,-0.167323],[2.213937,-1.280965],[1.874224,3.955220],[6.995461,-1.915699],[8.098569,-4.407714],[-5.747850,-1.831205],[5.538454,9.518391],[-5.809681,9.906775],[-0.162256,0.639051],[-0.459539,1.466411],[-3.690859,0.369326],[-8.621076,8.719226],[-6.542651,-1.085414],[0.806375,-1.753051],[-9.388349,1.518216],[-0.016512,0.647436],[-6.780268,-9.363275],[-7.981118,-3.006510],[1.349492,5.096106],[4.907930,5.777275],[-6.807630,1.993535],[-4.102637,-4.568095],[2.991040,6.493310],[6.955583,7.833883],[-4.013583,-9.454239],[3.892302,7.860660],[-7.723866,-3.240635],[7.875564,-4.699602],[9.420349,7.030505],[7.572927,-7.574777],[3.465699,-3.067308],[-7.570301,-1.482957],[-5.780586,-3.902819],[8.567041,-6.371089],[-4.155624,-7.793027],[-7.680753,8.912348],[-7.864023,8.137548],[5.508157,-5.269446],[-0.395335,8.592462],[-2.041402,5.798975],[-1.837561,-8.946997],[8.075167,5.757378],[1.114080,5.821807],[-4.952334,-1.367800],[-7.478970,-9.861097],[6.801541,-1.729674],[-0.534027,0.370714],[-0.645070,0.430511],[-8.126697,-9.940807],[-8.586256,9.890902],[3.473810,1.571105],[7.557707,-8.356252],[2.429302,0.064724],[-4.364577,-2.997976],[6.093641,7.567855],[-7.694922,-7.172097],[6.693517,-8.046892],[0.296719,6.493764],[6.784514,-7.357213],[-8.438608,-0.446877],[-0.662554,1.309590],[3.337297,2.667962],[7.450422,-4.826449],[3.224752,-2.209932],[-6.466532,-5.698401],[-8.442386,-6.995189],[-3.658067,-4.547940],[-7.695731,-7.616556],[4.257965,8.365535],[-2.289386,6.127056],[6.523217,0.842703],[1.978594,2.938621],[4.345267,8.371559],[-1.526159,6.654457],[-2.454395,3.029878],[-3.802713,2.866248],[5.727691,-0.184522],[4.591144,3.823805],[-3.419333,4.917924],[-6.468994,7.908703],[-8.314576,2.894085],[-2.919211,3.774769],[5.200175,4.938542],[6.007109,1.797789],[7.445300,-3.008336],[6.947187,-3.872547],[-0.783476,3.561709],[-4.932154,-6.373820],[0.761556,7.446474],[-9.053345,4.255180],[-4.701351,4.433703],[4.346824,-6.603349],[5.226423,-2.710552],[8.444797,-5.376917],[-6.345366,-3.371196],[-0.622463,-8.619194],[7.899462,4.160487],[-3.003541,5.015648],[-5.233969,-4.039220],[6.760947,-5.732151],[6.801514,6.535567],[8.758173,3.281572],[-5.563222,4.602767],[-6.574932,-5.966171],[4.111195,-1.882802],[-6.306676,-2.537758],[-2.258713,3.286286],[-8.702796,-5.695485],[-1.847160,-6.919113],[1.657832,2.906060],[6.847277,-7.562779],[-1.665241,7.944860],[7.911541,-2.863175],[6.354274,-4.038221],[2.562972,2.403610],[9.014327,-6.705419],[-4.717701,-3.031564],[-3.088923,8.210595],[-6.374599,5.288484],[-7.570852,-9.371885],[-5.257273,-8.233470],[-3.319748,-3.125835],[-9.280554,8.669738],[8.076235,5.315885],[-6.020784,-5.048125],[2.443426,-8.660942],[9.509903,0.595744],[2.542324,8.899290],[-3.599444,0.649497],[-0.551624,-2.729356],[-1.631826,8.110473],[2.262580,1.150655],[-3.749361,-3.014727],[7.356779,0.862480],[8.528930,-3.179648],[-5.754859,-3.349379],[6.770610,8.509964],[9.302959,-6.454781],[0.217512,-1.997262],[-4.657749,-1.780101],[0.016791,5.052636],[-4.138832,9.686022],[0.583175,-9.042863],[-4.795273,-6.374110],[-0.123780,2.121241],[7.448982,5.337578],[4.699595,-7.946287],[8.861975,-2.913911],[6.190694,7.997897],[-2.219144,8.153094],[4.526176,-9.590338],[7.849696,3.052928],[-7.250346,3.075081],[4.412262,8.111898],[-8.939351,-2.371407],[-1.432993,-1.161352],[-2.550037,4.407339],[3.968777,-2.579629],[-0.629013,-7.971982],[4.417322,-1.069464],[-1.376645,-4.421361],[-5.974892,3.064735],[6.837429,6.560197],[-4.911285,8.356706],[3.477163,-4.312801],[-3.018816,1.291539],[8.509629,-5.978226],[-9.678606,-4.228061],[-5.565334,-6.282925],[-0.636551,-8.891784],[4.504515,-8.661080],[1.552129,6.385334],[-7.842652,9.714404],[-5.472683,-5.512409],[-8.317127,3.240157],[9.188340,-6.572709],[-9.214536,-1.541888],[-6.375567,-7.568077],[-0.024637,2.827362],[-2.052685,9.500318],[-8.428858,6.969545],[9.837107,-5.223051],[-9.792955,-0.268952],[-0.100124,-0.686418],[3.282683,3.250362],[5.121101,-3.953943],[-4.422355,2.586417],[-5.552217,-6.340738],[-6.968210,6.003867],[4.170740,1.999750],[6.407924,1.854171],[-0.317207,-4.596475],[-5.826093,1.358842],[4.416884,-0.990455],[-6.995441,6.963804],[-8.620324,2.367256],[6.284161,-8.963326],[1.802663,1.071766],[-8.097176,-7.794319],[-2.096336,-1.470006],[-6.642941,-4.195434],[9.289610,-9.276292],[-4.740417,-0.613849],[3.473263,6.495903],[4.838231,0.138567],[-0.881630,2.179930],[2.408246,5.684349],[9.456357,-4.165043],[-4.144566,7.277261],[0.383536,2.449484],[6.948567,-5.963270],[9.912518,-4.400116],[-6.332128,9.906643],[-4.314120,5.480947],[-8.730252,2.349580],[-6.368764,-9.623205],[-8.535225,1.823091],[1.602715,9.345382],[-7.370031,8.115144],[-4.627260,-0.485801],[5.660450,1.728852],[9.434970,8.343819],[4.137370,5.674290],[-1.338056,-2.661379],[0.757680,7.453531],[-5.622948,-8.669849],[-1.758100,4.270423],[2.818909,1.997338],[3.308012,-6.779944],[1.673575,9.545736],[-0.062750,7.031141],[-3.492048,9.029370],[6.148759,-7.652989],[3.604347,-0.504339],[-8.400765,-3.892883],[-0.196405,-8.181788],[-0.959279,-4.511464],[-1.527168,2.134243],[-1.571169,4.365597],[-3.342344,-4.001917],[9.975491,-4.109731],[7.996823,3.827943],[-0.425147,1.400586],[1.884548,-9.055997],[-3.542547,-6.007690],[-0.766553,2.591075],[-8.604185,8.904587],[2.845238,-1.195048],[-9.654888,-6.279839],[7.485052,9.219987],[9.071489,-9.699774],[-4.745977,0.456400],[7.765941,5.208579],[8.830708,-4.011383],[-3.056958,-8.520685],[-4.842865,-2.338737],[8.583614,-9.079514],[-0.498316,-5.148548],[1.321461,0.955689],[-8.324838,-4.972762],[-5.929250,4.998692],[3.239854,4.234568],[-1.943042,9.670538],[-7.406653,0.931176],[-7.440717,-5.017052],[-1.304622,1.205452],[-4.522241,7.145553],[7.026813,-4.775277],[-2.007944,6.376389],[-2.589475,1.207791],[-8.965990,5.898505],[-9.655384,9.533434],[-3.458009,-5.425008],[-6.544238,-3.484679],[-9.877036,5.538933],[-2.416309,5.411585],[-2.469174,-8.202978],[0.718543,9.526906],[-0.922934,-6.170648],[6.154047,-6.107294],[0.712089,-5.058772],[-1.090190,-5.875082],[3.441756,-3.331648],[-3.393694,-7.604075],[-9.197067,4.317575],[-2.440039,0.576617],[4.809382,9.380284],[5.235838,-7.761968],[-5.598464,7.933953],[-0.190753,5.307780],[1.810064,4.131987],[7.008845,-8.779590],[-9.542874,5.853681],[-2.877424,3.917682],[-5.216581,0.471726],[-5.828052,3.837394],[-2.580639,8.042105],[-1.524104,-7.133131],[-5.914483,4.963103],[2.218748,8.394268],[9.601728,-4.542942],[-9.098782,6.257044],[6.002236,-6.715619],[9.478195,-8.273802],[-5.832552,-3.460641],[0.493683,5.212142],[-0.518256,9.107662],[-6.888111,8.099154],[-2.090749,-1.237915],[9.259623,2.524686],[-3.992830,0.270468],[2.998271,3.591331],[8.011478,2.807436],[2.868753,1.586488],[0.544003,8.078262],[7.188444,-1.199382],[1.458944,-9.428940],[-5.515245,7.690468],[-1.812582,-5.708188],[-3.132920,7.216322],[4.393048,-6.245566],[8.975308,-1.313216],[2.907016,4.187435],[-3.500494,-9.029124],[-6.645328,4.312706],[-2.697920,0.012708],[5.026269,6.378318],[4.353017,0.953101],[5.821396,8.167354],[2.171234,9.136098],[-1.211491,-4.592035],[-9.889857,-0.981095],[2.336305,-3.522292],[-3.608218,-2.628972],[4.530223,6.212276],[8.914987,-4.530069],[8.879754,7.962726],[0.700001,8.549308],[5.360606,1.230547],[-0.780729,-5.468790],[3.635015,9.036471],[-5.051205,1.006552],[6.475732,6.417906],[9.955598,8.863118],[1.855378,-1.183497],[-2.641626,-5.595678],[9.984287,1.656404],[6.070352,3.725117],[-5.517922,-5.153558],[5.150772,7.026201],[3.750885,7.229795],[-7.974455,3.837681],[0.489218,-3.284648],[1.498965,-5.011128],[-8.189696,-5.805019],[6.243681,-2.579559],[-1.206876,1.798636],[-9.835114,3.644333],[5.362382,0.827254],[8.798580,5.718336],[-1.465925,-9.329199],[3.233496,-2.164147],[0.633968,3.720048],[-0.199089,-2.745137],[5.187978,-9.781563],[-1.223210,9.000999],[-9.417262,8.188467],[2.709867,0.664408],[6.567959,8.143123],[-9.759002,-9.730969],[-4.258558,-7.660726],[-7.095074,6.010560],[-1.936692,2.322210],[9.305280,-0.058987],[0.504423,-5.708215],[8.722968,-7.373936],[5.899413,4.730143],[1.948810,6.736472],[0.304270,6.151059],[0.516811,7.155786],[-4.452040,-8.098624],[3.129478,-0.074724],[9.610864,9.394601],[-0.085199,1.038313],[5.904417,6.513205],[-1.464314,-0.808295],[-4.882704,0.891183],[5.385362,-7.967465],[-9.884801,9.142250],[8.419846,-1.971010],[-3.589249,4.997187],[-5.519964,0.740149],[7.923047,-6.301724],[1.448774,-2.116121],[-1.722433,5.613061],[-1.318322,-7.086210],[0.379931,1.062268],[6.659107,1.953097],[5.117085,-3.840254],[1.991316,-4.541478],[-0.735932,-0.018804],[5.404446,0.242197],[0.930186,2.404860],[-7.585721,-7.149634],[-3.905929,2.684951],[8.878112,1.698402],[5.895219,-5.204656],[7.294781,-5.362428],[-7.019326,-8.129312],[7.169815,9.271527],[-5.088959,-9.838759],[-1.890738,-6.232725],[-3.697354,-6.745229],[-9.266730,2.728408],[0.556046,-8.455797],[-2.095634,-7.341195],[-8.100561,-0.441285],[5.277543,-9.908770],[1.167307,-0.464407],[3.602734,-3.791750],[-3.720543,0.216943],[-8.122878,5.093265],[2.246319,8.546937],[-6.465346,-8.132761],[-6.535923,-5.630208],[-0.447332,0.492259],[4.839006,-9.628923],[0.332669,7.017024],[5.155618,-1.155353],[2.135095,-5.140244],[-8.923301,-9.100499],[2.812118,6.192695],[6.334786,5.419505],[-0.011614,8.748690],[3.290658,-5.092515],[-6.404080,-9.765351],[-2.602124,-9.339120],[-2.801117,-3.039542],[-4.893885,4.094589],[3.588409,0.164533],[-1.294088,5.856342],[5.933567,1.516999],[-5.316865,4.237080],[7.291824,-2.487545],[7.373445,5.368246],[0.913574,-2.281412],[-9.417466,-7.422266],[-5.936370,-6.763912],[-6.233156,8.056457],[1.183977,-7.143299],[-7.250860,-0.640814],[-4.107034,2.905855],[3.843192,4.662484],[6.076054,-7.883760],[-0.210134,5.007667],[-1.118479,0.306084],[3.733197,0.065171],[9.428836,-3.289547],[3.283855,5.405478],[-9.182623,2.016994],[0.073353,-1.491529],[-8.244973,-6.434222],[6.588066,0.202946],[-8.590681,7.727359],[6.391090,-5.438148],[-0.048589,-2.445295],[3.874575,9.489544],[6.618029,-9.292900],[-3.443475,6.256643],[1.848356,0.934458],[4.270674,8.501475],[2.599758,-8.518703],[3.097257,-0.224894],[0.134637,1.432070],[-0.568561,-6.421629],[-5.194554,3.507224],[-2.228265,9.317804],[-5.376996,-0.545371],[-7.909965,0.455601],[-8.869383,-7.009596],[-6.692543,-0.255063],[-3.692128,1.415831],[-2.019997,-3.482981],[-2.978910,9.857981],[-1.570741,-5.770998],[3.361769,-0.041146],[-5.965959,-9.546680],[9.434742,-7.843494],[5.512644,-0.041236],[7.896883,-6.111937],[9.876706,-6.246044],[-7.428157,-8.168444],[-0.779301,-2.274339],[-9.746081,2.329536],[-8.230827,3.728797],[2.397761,-7.314261],[-4.595929,-2.957421],[-2.417506,-2.598953],[4.841350,4.082104],[-6.880485,-6.975929],[-7.858864,5.520049],[8.285752,-9.325981],[-6.779106,-0.377884],[3.295442,-9.606646],[9.229313,9.645193],[2.233266,2.215998],[-5.826711,3.054466],[3.400565,-9.367640],[-7.107540,-6.498134],[-4.983584,2.360721],[-8.046338,-8.109046],[-7.640197,-0.683616],[0.730701,3.181849],[9.274406,9.462189],[2.941146,-1.345076],[-1.025466,1.254873],[-4.983953,8.671427],[-8.786749,1.822125],[-2.218106,-6.503880],[-2.180858,-3.997208],[6.613026,5.846654],[-7.091237,-2.178930],[7.887790,-6.471526],[7.261596,-2.744447],[7.839134,9.082076],[-6.624889,7.135168],[-4.546686,-2.194750],[-2.990368,5.483511],[-6.133216,-6.030815],[4.882815,5.528332],[1.459239,7.083994],[8.645246,7.893478],[4.604271,-3.282603],[6.512685,-6.657914],[9.616527,3.483134],[2.523326,6.703963],[4.460914,-5.571665],[6.951265,6.756215],[-8.944297,9.516878],[-0.370427,-9.166062],[6.111347,5.458423],[-0.771365,8.571674],[-1.746648,2.494675],[9.383455,-7.707373],[-2.038366,5.137195],[-7.113714,9.260826],[3.275674,-9.682766],[6.116155,6.892555],[0.871831,9.390049],[-4.305199,9.460163],[2.997820,-1.301624],[-0.270419,2.170292],[-3.677291,-5.951663],[8.231199,7.441557],[-3.018416,-0.179574],[-1.306898,8.386711],[3.197970,-2.180740],[6.942254,-3.199721],[-1.050861,6.877811],[0.490419,-7.232233],[6.772915,-4.720119],[-5.965002,-0.852956],[0.869422,-0.980538],[-1.023459,1.561054],[-5.161752,-6.974997],[-4.800459,2.866466],[3.799972,4.949434],[7.840067,-7.572306],[-4.371189,-6.371997],[-7.692351,1.937611],[5.706834,-8.033749],[1.710192,4.394354],[8.804965,2.631235],[0.287129,-9.816917],[8.055338,9.363606],[5.195871,-0.475637],[5.513075,-4.006263],[8.051737,5.380103],[9.965626,-4.900417],[-7.919663,1.014506],[4.619152,9.203302],[8.663969,-4.918705],[7.570409,8.706098],[3.795173,-7.885368],[-2.882740,2.381484],[-8.276166,1.226585],[-2.283791,9.450158],[7.845457,-1.936860],[0.294608,4.072912],[5.104625,-2.278532],[-2.008609,-2.122563],[4.495185,-2.605110],[6.606365,2.105913],[-6.616416,-5.275693],[-3.006243,4.895559],[-4.776897,3.961383],[5.215941,-5.685464],[-2.344280,3.867007],[-8.250909,-7.052906],[-2.901232,-5.463340],[-1.078451,-9.968501],[-1.512018,2.049398],[-7.050467,-3.459382],[-2.480537,-9.756755],[2.124289,2.811294],[6.240911,-5.670545],[-7.032722,3.408058],[6.788699,-4.337853],[4.337596,-1.444380],[2.689246,9.287386],[6.751560,-9.563974],[7.899639,4.037092],[5.968852,-9.533967],[-1.239989,6.397714],[6.398275,0.061622],[-5.934939,3.769996],[-2.977544,5.749302],[5.328454,1.389817],[-9.632846,7.828686],[6.934291,-0.730450],[3.582451,0.015494],[3.497559,-4.765673],[-5.791502,1.570200],[5.170046,-0.974439],[4.487325,-7.431124],[-6.132389,2.341732],[0.602908,-8.702317],[1.932505,-9.256831],[8.365243,-1.958152],[-1.774557,-6.041698],[2.696711,1.825184],[-3.559272,-8.413657],[9.554870,-4.874012],[6.686796,-0.270380],[-2.415784,3.211917],[-6.185479,-5.208442],[9.921776,-5.642821],[7.375623,-8.603878],[2.138752,-2.396353],[-2.932585,7.584910],[5.349663,0.448464],[8.855516,4.074878],[5.607755,6.734705],[-8.441346,5.519455],[8.046904,1.058314],[-7.303584,3.190998],[0.973900,0.777195],[-2.283998,8.237324],[4.692242,-2.103110],[1.268021,-7.385035],[-9.003869,-1.413785],[-0.201002,5.040427],[1.174320,-2.040665],[-5.885407,7.896196],[4.748045,2.517941],[7.656762,9.318415],[-0.967272,1.435548],[-7.717642,-6.875816],[-0.115534,2.691955],[-4.441006,-7.042126],[-6.137103,-8.579595],[-4.273885,-0.127086],[-6.313726,1.265963],[7.201124,-4.784720],[3.115595,7.288070],[-6.661793,-7.776335],[-7.267709,7.597906],[-8.151684,-3.929002],[-5.738040,-3.641085],[4.413370,0.570351],[-7.190238,1.723262],[8.486587,4.752635],[-8.869219,-4.866729],[-4.875940,3.189506],[3.051859,-5.945034],[-0.844037,-2.880323],[4.964505,2.230126],[9.484809,-3.390903],[8.739999,6.257984],[-2.759499,3.781477],[6.490396,1.065817],[4.358655,-0.079274],[8.823611,-0.994741],[-0.766468,-1.088706],[9.095320,-3.520503],[-1.708054,8.385535],[-7.497014,2.424100],[5.520717,2.326441],[-7.563528,9.126735],[2.235337,-5.128590],[-7.669040,-9.842814],[1.722479,-1.105289],[-6.428793,-2.365017],[5.245189,1.716047],[-0.951266,-3.751052],[1.543333,8.648089],[-5.251372,2.665117],[-3.914271,-9.194030],[4.789398,0.819816],[-3.070084,0.476767],[-9.059744,1.926543],[6.729205,-0.302116],[2.887407,-4.606916],[-3.836516,8.920534],[-9.419918,9.948774],[-0.432076,6.535587],[-9.706385,9.988482],[-7.483714,-0.901100],[-9.688910,-1.001723],[-4.757740,5.070146],[-3.458125,-6.338170],[8.996079,6.256155],[4.311060,1.437810],[2.199564,7.944085],[9.825160,-1.051838],[1.336733,9.363759],[-3.849851,-5.688864],[-3.516450,4.559339],[4.338150,8.636387],[8.659847,-8.621123],[8.104370,-2.962136],[-9.150842,9.177445],[-0.204144,8.966197],[-3.234944,0.377496],[-3.849845,1.326869],[-9.458596,8.691336],[-4.261082,-2.756785],[-9.201542,-2.664714],[-9.964785,-7.591125],[-7.745427,2.434443],[6.453266,2.666511],[6.798044,-7.743074],[-5.778842,-7.002050],[-9.778181,-1.815639],[-9.791655,-7.649229],[0.783680,2.476560],[-6.662651,-8.506441],[7.624052,8.070531],[-7.397119,-4.261733],[-0.619684,0.641152],[-3.699870,3.057022],[-2.884866,0.889404],[-9.241711,3.735366],[3.673712,-4.151587],[-9.609236,-1.453930],[-9.433599,-7.500167],[-3.332510,-5.964272],[7.561181,7.930122],[4.364776,4.209071],[-2.724696,-7.701562],[-8.679429,-7.114715],[-3.044770,3.902728],[6.080787,-3.456392],[-7.364255,-8.419333],[4.281441,2.654878],[7.908926,-8.649176],[4.730888,-9.264016],[9.367725,-9.640175],[-6.903006,6.066843],[4.475566,1.944085],[-7.264766,-2.384221],[-4.677566,-5.160871],[6.118537,-7.571617],[-4.426870,9.791442],[-4.292303,-5.183769],[6.835201,-5.225989],[6.830298,-3.819179],[-2.719164,-9.217298],[-8.507541,6.601265],[1.832135,-8.323716],[1.013735,0.321762],[-3.983950,8.253249],[-6.898199,-4.935978],[2.570044,6.001903],[-3.755953,3.989210],[9.317465,0.988705],[2.807324,-1.927125],[-1.076164,4.073103],[-5.652028,-6.090227],[-5.632191,0.543959],[8.763090,-4.519372],[-7.607691,2.646598],[1.461465,-1.223042],[-0.683320,-7.397652],[-6.058888,4.452173],[-8.348327,8.940620],[9.387910,0.679446],[1.301668,7.082780],[-5.363105,2.324874],[6.883251,1.534069],[-6.630470,-9.129286],[3.875826,-3.499362],[4.520372,1.379233],[-1.782648,-3.443828],[-2.475518,4.242349],[6.677398,-6.608023],[-2.961434,-2.746089],[-6.611918,9.589775],[9.728845,-4.559280],[-9.122387,8.990476],[-7.525075,3.304262],[9.171712,-3.217309],[7.181394,8.823046],[-4.572447,-4.791704],[-7.117499,7.375509],[-0.616542,3.295280],[-7.400797,4.570624],[-3.721087,-8.307031],[7.032617,9.868082],[-8.732571,-9.961620],[-2.791598,-8.735654],[8.190131,2.108700],[8.376102,-2.379788],[1.709368,-3.931377],[5.824636,5.092156],[-4.967223,-1.718447],[4.205827,-7.159431],[-2.072248,-6.421183],[-3.292547,9.212375],[2.399657,3.267547],[2.763908,7.414854],[0.457437,-3.035409],[1.902712,-8.722984],[-6.186095,4.939632],[3.376025,9.175960],[-1.839150,-4.828837],[-5.213554,-8.944062],[-2.481914,-4.173238],[2.084802,5.310470],[0.885592,-4.489824],[7.807799,-6.633559],[4.061467,1.784933],[1.056541,-2.404315],[-7.368833,5.187485],[5.233621,5.107933],[0.831212,9.572404],[8.536693,-2.627506],[1.000244,0.050467],[4.023973,-4.515903],[5.672331,7.424355],[-2.237766,-2.736903],[-0.553788,9.923309],[7.419079,-9.426202],[-6.446652,5.879158],[-8.391390,4.262255],[-4.303403,-0.382653],[-4.924576,3.095292],[-7.038764,8.544454],[-9.391368,-6.951941],[6.599317,-9.902307],[-7.522179,1.599478],[9.090941,-5.953790],[-5.203341,0.757977],[-1.438403,9.900765],[-4.304665,-6.434173],[0.354926,3.434514],[8.932197,8.170507],[4.594315,5.852344],[-0.418496,-3.376555],[6.615609,4.401257],[-9.469405,6.509755],[-7.827018,-5.491292],[0.421225,3.180363],[-2.958740,-3.174851],[-2.203953,-4.330630],[-2.604068,5.340355],[-9.426152,-6.981203],[-0.666171,-5.923387],[-3.340070,3.816651],[-4.989055,6.010836],[-9.524542,-6.803606],[8.065993,-9.021633],[-3.058418,6.539074],[-8.894227,0.125059],[-3.249612,1.236925],[9.962676,-4.601064],[4.143884,-7.517624],[6.204408,2.413689],[3.298504,-2.769285],[-1.322595,-5.645732],[3.198173,2.336057],[1.786700,-5.550853],[-6.665943,-4.385586],[9.515510,8.977666],[9.650098,-2.081139],[9.672360,-8.485302],[-5.868129,7.410580],[-8.516264,4.563902],[3.334529,7.459551],[-2.919810,6.046474],[0.609392,-6.555027],[-3.678542,0.607286],[-2.668364,-0.367971],[7.909769,-6.015013],[3.239339,3.544611],[5.126189,9.034968],[3.804794,7.451822],[-4.403458,0.037116],[6.767457,2.610785],[3.826378,0.011820],[-2.827185,-9.693290],[-2.045898,2.212630],[-0.536394,8.916929],[-9.994108,9.073110],[-0.335365,6.605456],[0.615397,-7.757100],[-6.363777,-3.834061],[9.870078,6.657336],[9.572753,0.326892],[-8.687321,2.442855],[5.475520,8.635871],[7.653484,-9.287684],[7.012383,-6.311971],[-5.296538,0.795333],[-5.498777,-3.017233],[0.290222,-8.704990],[3.761484,7.868642],[-5.804698,9.339267],[0.427545,3.388410],[5.049307,-4.978991],[3.727555,1.717765],[-0.377630,0.179362],[-5.379205,-6.156087],[7.663181,-8.973666],[-7.207706,4.414672],[-5.017733,9.722649],[7.270208,-8.050718],[-2.952639,5.431553],[6.968798,6.198998],[-6.561115,4.122340],[-4.219235,-4.510354],[-2.948004,0.272209],[-5.076214,7.979506],[9.694723,2.524449],[-1.575752,1.460006],[-0.335057,-3.804085],[6.733605,1.483501],[-5.451092,-0.544031],[-7.224187,9.357798],[6.080271,-5.638318],[2.169996,-5.348644],[-8.259724,6.517160],[5.044416,1.825371],[6.267632,6.684687],[1.864268,-6.600234],[2.950221,-2.411401],[-2.546415,-7.700121],[-0.890603,8.483778],[0.625805,-9.387770],[9.584187,-7.094361],[-4.584942,3.793141],[1.251184,-6.336515],[7.957825,2.896554],[0.741790,3.328254],[7.852320,6.445435],[-3.037500,6.200599],[-7.818960,9.470186],[9.383230,-4.369231],[3.380915,0.852488],[3.926673,3.522366],[1.705689,8.656196],[-4.981896,-8.584666],[0.847938,-1.016285],[-4.122859,4.232089],[3.398653,3.521639],[-3.994560,3.090663],[9.089454,-3.449950],[-9.954997,9.825665],[-7.497337,2.852050],[4.397446,-5.348107],[8.376211,-3.832728],[-3.969886,3.820542],[-1.032928,-2.862036],[-5.276173,-3.191247],[7.120548,-3.600947],[-5.060150,0.187326],[2.266395,-7.509285],[-3.723996,6.822244],[9.577155,1.844981],[8.153183,2.234412],[7.626886,-9.032232],[1.556971,3.324928],[4.785519,8.167926],[-8.590706,9.899796],[3.702756,-4.009858],[-5.358791,8.003787],[-1.157926,-1.541728],[4.373006,9.867566],[2.127874,2.393220],[9.281626,8.916946],[-4.559193,-5.778903],[8.304617,-9.152438],[8.836504,-8.458969],[-6.194258,2.187550],[5.405445,-0.716949],[-6.836870,2.907260],[2.589606,-3.304270],[-1.719355,-2.495602],[-2.562273,0.842483],[-3.207593,-7.389712],[-3.585814,6.274573],[2.206516,9.768837],[-6.202763,3.406602],[-1.014008,8.308661],[1.006824,-1.049027],[6.064084,1.320001],[4.988180,-3.017922],[-6.680116,-7.045482],[7.198473,-2.621262],[-8.297062,5.696842],[1.297423,7.310198],[-8.793663,-8.748764],[9.355581,0.339817],[5.813487,-9.427847],[3.674676,-4.746738],[-2.807190,-2.330499],[-5.092289,-5.983491],[4.086900,-4.042119],[-4.798890,-4.180052],[-5.326384,1.069285],[5.624558,-8.929842],[5.417938,8.372533],[1.254144,-6.299773],[-5.351196,-4.831713],[0.866946,-9.949852],[-8.944521,-1.820532],[-5.445094,5.648697],[8.805111,-8.758732],[1.040047,7.812143],[-7.824080,1.010749],[-2.927972,9.904696],[2.551914,1.705533],[-8.354214,4.443910],[-8.183719,1.544658],[-8.049797,7.808858],[1.804349,-4.881315],[0.318017,0.736449],[-1.887107,3.940689],[2.093940,-3.774151],[-2.952355,0.650045],[2.175082,-4.858528],[-8.513085,-9.927542],[-9.970667,-8.487187],[-1.209567,4.165061],[-8.702435,5.947627],[5.584740,0.414366],[0.645077,1.665449],[-2.754599,-6.721326],[8.789465,8.439884],[-9.623531,-8.385035],[-2.648987,2.967393],[3.712430,-7.698991],[0.262796,3.095795],[-4.279088,7.231467],[-2.931457,-8.445987],[-0.660797,-9.428959],[6.476912,5.717334],[7.593322,-6.186549],[0.494303,-9.933139],[-9.618900,-7.105604],[-3.301074,5.778420],[5.144264,-5.576963],[4.226888,-8.171836],[5.530820,-8.817336],[-8.380193,0.664556],[2.873692,3.333138],[9.231876,-4.186126],[-5.776599,2.759784],[-4.706428,-8.258595],[-2.246075,7.902674],[7.834366,9.802664],[-6.439582,8.379290],[6.333353,-1.994110],[-0.926345,3.884502],[-5.064082,-4.902342],[0.367964,5.473106],[-2.258825,6.218715],[0.942685,-5.330044],[-8.686104,0.564402],[8.599390,3.025651],[6.016701,-5.113653],[-8.133806,8.257310],[3.180303,9.185832],[-2.914508,-1.156106],[-4.845732,2.989600],[-0.403381,-9.269083],[5.205012,1.797076],[-1.125426,8.775490],[-8.098065,-2.719597],[-4.647549,1.282629],[0.775332,-4.047432],[-8.312380,-5.592909],[-0.516266,-4.806461],[0.383629,6.499374],[-9.324092,-6.233169],[1.894323,3.940536],[6.312572,-7.005832],[0.634386,2.201369],[1.502199,-4.205204],[-9.449633,-4.654803],[-6.088905,7.987283],[-9.291966,-8.484215],[9.174111,4.757057],[6.666026,-1.659943],[-3.579717,-4.638081],[0.510629,-5.582121],[2.000758,-3.498981],[5.852999,-7.974679],[8.216789,-2.942369],[-0.603539,-5.475178],[0.198930,-6.905364],[-9.081112,7.530619],[-9.166670,2.487972],[5.009078,-7.158905],[-8.810067,-2.999803],[7.039261,-4.164449],[-2.980190,-1.885717],[5.519969,-9.892149],[6.468367,6.160915],[7.965134,-5.887499],[-3.701315,1.073864],[-0.691686,-5.539464],[-9.256092,-3.070512],[7.434250,-5.148292],[8.726495,-9.920057],[-8.003363,8.551959],[-5.472480,7.144747],[8.444940,2.796643],[5.768395,5.608896],[-9.940980,3.505784],[-7.231319,-9.696933],[-2.482000,6.729828],[-7.929454,-5.115749],[-9.812153,-8.808215],[5.643673,4.287145],[9.032988,-8.091400],[6.794665,-6.506827],[-8.855984,3.262278],[-1.345162,-6.149067],[-0.219181,-9.331935],[-1.633583,6.884793],[4.051918,6.307769],[-4.178043,0.179913],[8.449817,-6.665379],[-4.773685,-0.018048],[-9.829771,4.610574],[2.458868,9.997645],[-2.923998,-2.353890],[8.428997,0.825737],[2.996016,9.706624],[8.793546,-4.540752],[-4.507908,-3.763234],[5.983951,6.098553],[-6.506917,-3.762835],[7.561921,5.778476],[-9.074605,-8.148982],[-1.389889,-0.451199],[-7.630939,6.040100],[-3.130873,-7.239620],[-0.913082,0.822734],[1.786982,-7.281192],[-4.948016,7.632124],[-5.883228,5.860753],[9.098392,-9.243726],[4.894764,1.227234],[-3.199311,-8.227770],[-4.359352,-0.841095],[5.721623,6.236087],[-6.356621,-7.094878],[-7.733027,-0.774725],[-6.713350,8.788684],[5.111307,0.297871],[-1.842924,-1.299841],[6.501623,-5.752789],[7.158896,2.697363],[-9.842667,0.897858],[-9.599284,2.079127],[-0.352329,5.464321],[0.253846,-2.566932],[7.560357,-7.765025],[-7.673534,-8.672656],[8.484594,-5.196538],[7.756509,2.071607],[-7.437532,3.525645],[-2.266921,8.541650],[-3.450062,7.344473],[-2.141650,6.193176],[-2.350920,1.705561],[-8.627155,-5.725544],[-6.597261,9.672300],[-5.290050,-8.147017],[3.740407,8.158992],[-6.686665,-3.728949],[-1.707246,8.524669],[0.268381,-9.078027],[-6.840604,3.201125],[0.637143,-5.771983],[-7.636356,-5.790384],[-7.078978,8.328338],[-3.165946,7.747490],[4.573841,0.360696],[8.290402,-7.147453],[6.174342,-1.992030],[2.560710,6.147470],[-4.385258,-0.497823],[5.625939,7.230877],[7.322306,5.609947],[-2.473694,4.736279],[7.431678,7.217519],[4.222772,0.332658],[-5.446752,-0.099939],[1.496665,-2.199312],[4.565738,-6.639484],[6.282560,-1.519840],[-9.331188,-1.761814],[-1.872828,1.108918],[3.055928,-2.798256],[-6.505628,3.228280],[-2.300138,-2.892370],[3.121185,1.872917],[-2.542552,3.502068],[8.180599,-9.830778],[-9.313323,-4.778658],[-5.923914,-5.270414],[-5.600002,-9.260509],[-9.223589,3.788022],[7.988006,5.705557],[6.488232,6.974140],[-0.940494,0.328334],[-0.505821,-6.922184],[5.051107,9.897892],[-6.025065,0.780487],[2.716409,8.244465],[0.387049,-9.713235],[7.718131,-0.702049],[-1.973767,-7.886815],[-2.865550,-2.720133],[2.638315,7.517552],[-1.783541,4.060235],[-1.192560,9.130399],[-0.562741,-0.452564],[-4.013492,7.554856],[-9.947334,-1.454137],[5.580456,8.108025],[-8.483763,9.415517],[-9.230553,-7.656053],[3.295560,0.482246],[-5.096832,1.498615],[-7.731560,1.335364],[-9.648936,-8.484333],[-2.799712,2.089090],[4.072080,7.626960],[6.568373,0.760198],[-3.523085,-7.160985],[8.723721,7.887964],[-8.765755,6.562998],[-3.073266,9.022755],[6.421712,4.788297],[-6.139992,5.601625],[-0.771966,-4.171030],[7.860421,1.355039],[9.777131,-6.152097],[-1.207178,9.586967],[-2.685974,1.375028],[5.910650,-2.275855],[-0.074700,-5.825133],[-3.663571,-6.765341],[-8.476721,-7.612867],[-7.012888,3.648000],[6.112159,0.985998],[-7.472846,1.000666],[6.370038,1.592661],[7.326408,5.673298],[-8.165496,8.590764],[9.278250,4.203050],[-3.331749,-4.173851],[7.757987,-5.405183],[9.161386,-4.827578],[-1.753743,-4.947476],[-6.981181,-5.258734],[6.288342,5.988575],[0.173982,4.531865],[-9.761705,9.400061],[-3.371789,-0.549681],[3.908564,2.332692],[-4.308498,-0.019424],[8.358888,-9.484381],[5.707306,5.810489],[-9.134821,-7.974890],[9.732353,-0.749887],[-5.578274,-9.106809],[8.495650,-2.476912],[-6.849817,8.048900],[-3.770971,6.258704],[9.887551,3.312994],[3.500010,4.808246],[-2.147012,6.915862],[5.006243,6.397128],[8.338977,9.491609],[-2.505123,-4.842836],[3.433151,1.278879],[0.482114,2.134046],[-0.798460,4.600753],[7.524520,8.664070],[-5.890568,-5.576264],[0.375031,0.893374],[1.580835,2.468799],[4.061384,-2.380866],[-7.441193,-8.859690],[6.950924,-9.988008],[-4.038520,4.707963],[-7.026553,6.903892],[4.129393,5.429843],[-4.684696,-8.675731],[7.329643,2.720247],[6.105062,1.385648],[-7.877755,3.371222],[5.588464,1.864954],[-7.937864,3.658897],[-9.805964,0.155100],[-2.142209,-0.248656],[-4.486423,6.286817],[-4.054567,-8.790990],[-0.692464,3.566124],[7.271850,-9.700032],[-3.904315,-2.048104],[-3.596631,-0.688818],[1.432917,4.485106],[-4.641564,-5.957112],[-2.851344,-8.711833],[-8.980524,-5.708370],[-0.843775,7.669237],[-3.664215,-1.919918],[-8.092588,9.572522],[-9.562270,4.191574],[-3.169688,-3.615184],[-4.890306,8.360146],[-2.728134,6.276226],[-8.340411,8.494153],[-4.211072,-1.518238],[9.701699,4.571304],[9.145428,-2.331633],[-0.086517,4.165151],[-8.846032,5.318800],[-8.979606,8.677980],[-3.312451,-7.805463],[-5.251608,1.425547],[-8.146685,-8.403586],[-5.844928,1.396425],[-5.911235,-6.870752],[3.145343,3.283649],[6.121584,-4.850367],[4.558730,-4.211282],[8.309541,-2.205740],[-5.856732,-5.630207],[1.034910,-7.363459],[-8.730225,-4.147774],[-2.265833,-3.956035],[-0.784167,0.770581],[-2.530015,-9.927950],[-9.473847,-5.714842],[2.371790,9.278815],[-1.259946,-5.130289],[-1.326486,-6.661892],[8.983594,-0.602692],[6.259014,2.082306],[-3.145901,6.841942],[7.790606,7.424900],[-7.707458,0.150577],[-1.446315,2.558497],[-0.891921,7.600895],[2.720847,1.174937],[-5.246107,-6.309509],[-4.670103,7.971363],[-2.316296,-6.914712],[-2.198400,8.948246],[5.869409,-6.296295],[-2.138985,-3.246255],[-5.596483,2.572582],[4.591377,-4.670533],[-5.953702,7.206499],[-0.333703,-1.834487],[0.235539,-4.911583],[-9.027660,-0.225095],[-3.988627,1.074723],[1.241228,1.103613],[5.935232,4.241098],[-6.658550,-0.959882],[-8.595887,8.201227],[4.957930,6.399215],[-9.184983,-9.594548],[-2.321257,-7.984666],[-6.828147,7.322979],[-8.549220,6.556220],[5.827678,-0.268417],[-4.571564,4.534441],[6.098339,4.620614],[-0.578386,3.108733],[8.412648,6.039910],[3.917273,-3.642647],[0.009515,1.715943],[7.471188,-2.952814],[7.494447,-6.579351],[2.150415,-9.345948],[-4.842687,0.383075],[-4.701927,-5.993333],[5.073457,8.840274],[1.963076,-8.252007],[7.336540,-6.898646],[-7.395959,-7.199653],[-3.969144,2.896271],[-1.195941,-5.610573],[8.043458,6.121971],[-6.625954,5.373591],[0.167560,-5.171445],[3.573263,4.391367],[-8.761430,2.181193],[-0.059683,-3.016876],[-7.258472,4.234930],[7.874344,6.258983],[3.022073,9.991192],[-5.199937,3.985084],[5.982903,6.506013],[-4.159245,-9.668511],[-6.565721,2.662536],[0.389583,7.089379],[4.544003,-4.908432],[-7.545966,-3.820158],[-5.775791,-8.855913],[-4.349616,-5.581151],[9.587909,-1.340001],[-1.043811,6.682297],[-6.675319,-0.218328],[-6.978030,4.957093],[-5.445450,0.264971],[-0.583828,-9.829773],[3.316119,2.410089],[0.727281,8.549840],[3.286197,-7.250002],[-0.766799,0.658821],[9.998054,-7.139396],[6.005875,2.839479],[6.965899,5.878959],[-3.400487,-7.064695],[-1.959891,-3.837370],[1.122908,-4.959822],[9.474597,9.313614],[-5.984575,0.504854],[-8.677359,-9.471683],[0.788159,8.186377],[-1.485626,-6.090794],[-7.290418,-9.059924],[1.117392,-7.371864],[-6.365635,0.243634],[-7.570613,-0.715050],[5.388015,-3.651023],[9.137354,-7.220389],[-8.214271,-3.250538],[-7.885092,-9.508448],[5.388100,7.141513],[2.569097,-6.256817],[-2.622825,0.215567],[-8.625668,-3.756299],[7.457305,9.582007],[4.401926,-9.630703],[4.404788,-0.247495],[7.777475,-3.833294],[5.436378,3.001273],[-7.357413,-8.813364],[-7.303124,3.594590],[8.122984,-7.917901],[-7.078876,-5.209115],[2.614829,5.268047],[4.883073,-8.640564],[-0.989176,8.471002],[-4.248659,-1.120364],[-0.421257,-2.332882],[6.249485,3.628537],[5.167262,7.733144],[1.821225,0.135734],[-7.458498,7.371149],[-6.002397,5.654942],[8.403018,-5.101130],[8.770700,-6.888324],[1.978507,-3.301465],[-6.080078,-9.300641],[-3.050016,2.300627],[4.437386,-9.149178],[9.036496,4.063203],[-5.897091,3.407420],[1.952832,2.498788],[-6.648276,7.268614],[-4.697039,-7.092587],[6.053642,-5.609050],[2.801343,-9.561715],[-7.150535,-6.976548],[-8.218114,2.926062],[-8.508135,-0.626203],[-8.483604,9.042879],[8.616355,1.940666],[-3.587886,-9.054557],[-1.639792,0.068675],[-7.605464,-0.432950],[2.015409,8.990723],[-1.985872,-2.744099],[1.460936,-8.043886],[-4.352648,-9.502539],[-6.887258,-0.066614],[-5.070318,6.370533],[0.909110,-5.616793],[-3.923586,1.513128],[3.483917,0.773629],[9.377146,0.625459],[3.704774,9.991918],[9.065375,9.948145],[4.689620,-2.222491],[6.596973,-9.817992],[9.142297,-1.616069],[4.082908,3.502418],[-3.776137,-2.138750],[-9.041881,-5.228934],[9.597809,9.251835],[-1.790104,2.356047],[-3.024426,8.520452],[0.338481,0.395824],[-0.342749,-0.948712],[2.532440,-3.290807],[-4.266108,3.514162],[-0.909363,-3.309658],[7.829616,-7.773822],[4.883498,1.886142],[-9.636017,0.947071],[-1.912958,-1.528780],[-9.172503,-6.450551],[-3.147847,-4.764838],[9.490926,5.540933],[3.834370,-6.051065],[7.695947,-6.328163],[-2.670355,9.320696],[-5.088214,-0.814606],[6.575561,0.677926],[3.041139,1.522935],[8.803221,-0.846284],[3.497227,-0.460591],[-3.910914,-7.815677],[-1.300614,-6.362527],[-5.627055,3.524125],[-9.825182,-4.786197],[-0.938335,9.095706],[5.560784,2.803819],[-7.806665,-3.187927],[7.396060,5.394154],[6.284645,5.063545],[-2.269447,-8.024391],[2.477398,-5.822219],[3.497917,0.022476],[-0.478200,8.937192],[8.232572,-3.161202],[-0.778002,-6.291434],[-0.973234,6.911000],[3.592715,6.002244],[-6.186098,-2.793743],[1.266993,5.988205],[7.515484,-6.968766],[-5.831111,-7.793738],[-2.913622,8.567506],[9.414148,-4.596657],[2.431736,7.359241],[-9.468399,2.928630],[-3.447253,0.571276],[-4.619037,-9.844512],[8.046688,7.756451],[-9.766562,-3.004232],[9.191034,6.928165],[5.578209,-1.377393],[-3.034449,2.675147],[-9.039705,4.766162],[-1.166883,-2.613086],[-7.070825,6.937632],[3.233432,3.674194],[-9.172800,-3.991157],[9.109859,-8.610136],[8.690608,-6.233214],[-3.522696,-1.005635],[-3.370848,6.157278],[-9.411183,7.874960],[-3.371508,9.270097],[5.664092,1.524338],[-7.303897,1.491830],[8.415887,-6.067401],[-1.659010,-6.120525],[-9.759160,0.946003],[9.654544,2.595157],[-1.370654,-3.767589],[1.099383,-2.251191],[-9.164186,-6.117102],[7.076967,-4.755395],[9.321432,5.753767],[3.975366,-1.448144],[0.054144,-1.407293],[-7.048610,-1.854290],[-0.447460,8.210368],[-6.208648,0.839180],[2.197326,2.891983],[0.471179,-3.027727],[-1.745736,4.605917],[5.637222,6.515082],[0.809442,7.977491],[-7.215936,4.663650],[-6.060347,-1.922488],[-9.130303,8.364497],[-3.772129,3.218667],[4.730801,-4.929092],[5.036519,5.485023],[-4.522269,0.982682],[4.473439,9.737773],[2.506838,-8.240128],[-1.410896,-8.182388],[-2.256891,-4.769437],[2.007966,1.932195],[1.447708,-3.745032],[0.945291,-1.804278],[0.933065,2.710708],[-0.624435,-6.576310],[4.358348,-4.982154],[9.391066,2.000743],[-8.778775,-0.948573],[3.206811,-2.982842],[-7.397115,1.753642],[0.499231,3.347755],[-1.364467,0.844925],[8.836483,-6.792491],[-8.662548,-4.016609],[9.284151,-0.266728],[-6.630011,0.696321],[-2.122732,-3.310787],[9.386874,-1.088943],[8.055794,7.095469],[-9.822864,2.844141],[-0.780320,7.314856],[-5.396526,-1.695916],[2.555218,7.502141],[-4.657757,1.265816],[6.200167,9.586295],[8.662137,3.501775],[8.235379,-3.041778],[4.921374,8.313560],[3.501906,-5.724866],[3.241896,-1.437901],[0.770614,-2.714110],[-2.530098,-0.605830],[9.926437,-0.032489],[5.803352,-9.300021],[-7.024218,7.456788],[-1.931510,8.953748],[4.747941,9.821480],[2.805941,5.454044],[3.602181,-5.712612],[4.814167,7.427843],[-6.480681,3.751860],[3.912938,-7.496473],[9.632684,3.891229],[-3.087777,7.757090],[3.672183,-2.521158],[-0.342944,6.256152],[6.989074,-5.620958],[6.788222,-1.098000],[0.914604,0.062438],[0.649125,6.340982],[3.913263,-6.477894],[6.891418,6.399520],[-6.321144,5.208416],[3.917888,-3.681476],[-1.131126,1.547045],[2.262468,6.481432],[-4.730202,7.046212],[-9.936724,-9.401941],[-6.254087,-7.274466],[-1.645869,-3.603716],[4.448099,-5.836254],[-2.196747,-8.043731],[8.033471,-6.218548],[6.988449,2.455174],[4.150038,7.062301],[4.120546,4.699272],[-5.916612,-1.908073],[-1.239075,6.828341],[-0.380718,-4.613417],[-9.210566,-5.349038],[8.007502,-2.149669],[-5.444318,-6.263155],[5.253314,-6.648385],[3.379505,-0.391188],[3.774898,-5.160389],[8.710037,1.232368],[7.936354,-3.483148],[-0.132197,1.090450],[-6.229558,-0.692394],[-1.845564,-6.506882],[-1.388362,-6.316989],[-8.705632,1.011600],[1.070859,6.460808],[9.747745,2.694963],[7.130102,9.277940],[-5.379738,6.836347],[-9.736742,0.010260],[-7.097257,-0.696893],[-8.057901,-4.316534],[0.387042,-5.711550],[9.717809,8.263959],[7.366817,-5.357700],[1.527560,-4.150399],[-7.477985,-2.049058],[-0.425066,2.503559],[8.974408,1.431209],[3.865451,-5.957410],[-9.135336,3.160155],[2.216535,-6.399126],[0.925739,4.611749],[-2.342234,-5.258448],[2.088845,-3.770362],[5.720524,-2.946301],[2.050014,-6.160039],[2.186059,-7.418106],[-5.021775,1.419955],[-5.290546,-2.204875],[-6.770677,-8.726036],[1.305869,-5.289403],[2.199071,-9.196508],[-2.179337,2.769287],[3.972784,-6.463196],[9.044258,-2.565336],[3.470786,1.997760],[9.212121,6.336419],[3.626295,4.229928],[5.196538,8.458607],[-3.888047,8.216170],[-6.478021,-4.933706],[-9.180114,-0.245691],[6.994905,3.271759],[-7.246255,8.334746],[-7.349904,-2.703864],[-3.380825,1.825449],[1.778425,5.840302],[-8.414219,-8.661666],[9.464129,-5.758929],[-9.004247,4.570384],[0.696511,-5.504672],[6.949016,-5.338184],[-2.084326,5.432387],[-7.077906,-8.433895],[7.157473,4.638894],[-1.493451,-0.224370],[-5.672175,-9.621400],[1.019424,7.305263],[-1.705252,9.658431],[3.065674,-4.136971],[-5.836472,-8.829351],[-9.812054,-4.620960],[-1.378922,6.924334],[4.371619,5.510011],[8.558602,-9.211498],[8.544198,5.978632],[6.813631,-1.392593],[-0.516554,2.654223],[-6.024251,5.880778],[-0.761512,9.729270],[4.118539,-1.927930],[-2.283341,4.507565],[6.903705,3.231684],[3.924065,-8.460325],[7.428338,4.508387],[4.157251,-4.006340],[-9.441581,-0.313695],[9.381083,-7.668490],[4.352877,9.807215],[-7.977057,9.386101],[6.004126,-8.480458],[5.843998,3.184027],[3.115240,3.738948],[8.739891,3.226216],[6.039878,9.008032],[4.038547,-8.233031],[-5.203291,-9.121036],[-5.849201,-6.678295],[-1.117569,-5.269366],[3.509504,-2.432517],[-2.896879,-7.395050],[0.587846,1.080000],[6.940097,7.312475],[-7.618339,4.980670],[-0.993763,8.005565],[5.635307,-1.757023],[5.611754,-2.070960],[-6.891323,1.921931],[-7.995338,4.856669],[8.385053,-6.778592],[5.116028,9.237250],[3.558092,-9.384620],[2.174048,-1.447920],[8.541622,-5.056936],[9.662765,1.431798],[-7.971021,-0.280632],[-3.090789,-4.465641],[6.201966,9.135628],[2.591925,-9.262281],[4.470473,-0.885724],[9.932334,-8.359845],[0.677269,2.921948],[7.304458,-8.453095],[1.906024,-2.132088],[-6.642982,-5.201352],[3.568484,-9.454662],[-8.547734,-5.279529],[8.491328,-2.447263],[5.524128,3.598827],[-6.535714,-1.986980],[-8.248755,7.526893],[6.484167,1.278610],[-5.481032,9.635265],[0.928863,-0.493686],[9.019421,-1.350981],[4.737694,8.871469],[2.973575,2.070759],[8.125395,5.973066],[4.524403,3.008632],[-5.155895,-2.638907],[-6.462766,-4.464568],[-1.051604,-6.395690],[8.000498,-1.351990],[1.336760,-8.298679],[3.551949,-6.139868],[2.537227,-4.396153],[-4.613664,3.740681],[-2.844623,-6.671383],[-8.129148,4.733697],[6.304984,-3.052123],[-6.026229,-3.968819],[-2.365624,-0.852919],[-1.912809,-3.779890],[-2.764758,-6.450380],[-2.188083,0.192368],[-9.704622,-0.536319],[-9.071223,0.354571],[4.944522,9.533596],[-9.676985,3.606361],[-5.007299,-2.654826],[0.988108,-9.915731],[5.195589,-8.084371],[-5.132938,9.971707],[1.896091,4.629412],[9.577681,-7.724947],[-9.031213,-1.304104],[5.590998,0.799577],[5.692335,-6.955028],[-4.729350,-6.779195],[-5.740034,-3.965881],[-8.581777,2.667745],[7.021814,7.471129],[9.520673,8.320935],[5.031988,-9.880660],[4.155581,-1.704272],[-6.433101,1.128152],[9.361612,-1.432819],[5.218209,0.737095],[-8.259402,6.880117],[9.489197,-1.848537],[-9.422682,8.957363],[1.473586,-7.247116],[8.609449,3.757240],[-5.524847,2.759364],[-9.025149,3.476370],[-0.667527,1.237716],[5.992183,-5.664813],[-2.110914,6.460484],[-4.485495,-4.638477],[-8.348665,-1.628946],[-7.322863,6.565466],[0.796250,-8.326638],[4.117611,1.792916],[-8.708573,-2.897153],[8.201997,1.494965],[-3.524561,3.395910],[0.631229,-9.791657],[-4.183338,5.326914],[6.121716,7.466551],[6.094328,-2.855344],[0.416959,-1.232793],[2.732224,8.893134],[1.274162,-8.000383],[7.573750,-5.118703],[7.030739,7.390439],[-7.196931,-7.617482],[5.226252,-3.542064],[-1.633170,5.039395],[-9.516570,4.989296],[7.993006,-6.721857],[3.718804,-5.520335],[-6.921997,1.606783],[6.438145,-9.706989],[-2.719055,4.828860],[-4.116414,-3.268950],[6.690819,7.959646],[-0.737071,1.122259],[4.752051,-0.820145],[-1.677294,-3.133811],[-7.844433,-3.757186],[-3.639354,8.629080],[-2.262903,-1.597326],[-0.152141,7.249062],[2.701411,3.385131],[5.618525,0.901240],[-7.119297,-8.614449],[-7.207883,-4.208329],[-0.604462,-2.925801],[4.930576,0.322726],[2.332249,-5.964933],[5.895048,2.698753],[-0.775695,-6.265141],[4.389872,4.148140],[7.228613,-0.001823],[-1.854828,-2.796716],[6.950101,6.197395],[-2.183057,-2.213669],[-0.940873,6.939531],[-2.556439,-5.291474],[0.842614,3.061508],[-8.854451,8.071595],[-4.231894,0.783027],[-7.125138,3.258608],[0.533574,-5.554836],[-8.800605,0.725127],[9.484991,-5.663970],[0.331374,0.046733],[8.977736,5.542438],[5.899889,7.883916],[-8.186452,-0.178302],[7.304601,-1.750789],[-7.968876,-2.624488],[-9.274913,8.611820],[6.808447,1.654380],[0.149530,6.439896],[0.343857,-5.677428],[8.381068,-3.105527],[7.199366,-7.619205],[2.012039,2.326185],[3.884125,-9.371801],[7.288523,-6.643449],[4.626892,6.828727],[-1.009759,9.132489],[2.143003,-9.599734],[7.097644,-9.126827],[0.794967,8.502335],[7.469325,-6.492959],[5.127737,-0.626197],[-3.061071,1.737573],[9.980916,-7.781270],[1.435489,5.980572],[-7.067726,-2.967046],[7.631970,-1.042500],[4.544509,4.396968],[-9.182507,-1.847470],[-8.731278,-3.407431],[1.317337,-6.502766],[-0.423474,-7.464804],[-1.264811,-8.577499],[9.803764,-2.594483],[5.995432,1.366833],[2.974630,8.551583],[-7.167339,6.835777],[3.105972,0.688424],[6.285449,8.179134],[9.729891,5.813440],[4.029237,-9.859233],[-4.994201,6.744526],[6.544756,4.885953],[6.308976,-4.269263],[-5.187592,-5.381500],[7.468569,-3.023907],[5.505004,-7.253453],[6.353722,-6.554463],[5.566887,0.947682],[-5.359905,0.267572],[3.661557,-0.814776],[5.670763,-7.125419],[-0.406981,8.504039],[-1.317445,-0.482130],[8.812314,-8.762950],[-5.779514,-4.667110],[0.827036,-9.898038],[-4.440997,7.147123],[-1.058406,4.460529],[-5.845496,2.555282],[-6.174431,-6.288474],[-1.239758,4.723356],[9.344315,-4.878526],[-2.108386,4.142990],[-0.295565,1.853912],[0.274087,-0.612601],[-9.245847,-4.485439],[3.357796,1.563614],[-6.968250,-0.560447],[-0.205264,4.382088],[-8.893113,-6.860479],[-7.255373,-8.958062],[2.651373,9.403166],[7.001828,-4.363766],[8.245197,-2.619539],[-6.174552,5.930254],[-9.100100,7.441844],[3.672121,-4.192086],[-2.375004,-6.388372],[9.613994,0.678027],[5.858362,1.252554],[-0.303652,-1.754402],[-4.598684,-7.083140],[6.364822,-0.805654],[9.417712,-6.286072],[-0.326207,-1.794850],[9.132655,3.443588],[-4.242376,1.971034],[1.907515,-6.528577],[-4.151121,-0.894042],[3.531631,4.854925],[-8.547875,-4.567211],[5.537987,-9.568924],[-2.831985,-5.343845],[8.555139,-8.733648],[-7.991030,1.247857],[-8.265100,8.195653],[4.766196,-2.697097],[-6.368685,0.409593],[3.662275,3.834689],[-2.608907,-2.493882],[-8.917380,1.158836],[-5.447768,4.449212],[3.254722,-7.181661],[-3.247002,2.998338],[6.035111,5.301707],[2.224262,-1.709427],[-4.526272,-3.927117],[5.917372,3.311706],[7.366994,-4.655164],[-0.997001,0.058166],[-3.943391,-2.969990],[8.512803,-1.035535],[6.432918,3.460381],[-5.669519,3.736643],[2.860266,-9.276124],[-8.806395,-5.525812],[-4.129171,6.776967],[1.051458,-3.982762],[-5.621810,-1.977513],[-4.276503,6.005047],[-1.938057,5.941815],[-2.201455,-1.534101],[-8.964955,4.311987],[-2.838562,-2.892336],[-8.301481,-2.639911],[-6.100354,9.985397],[8.542933,7.333252],[9.877031,7.975381],[6.837080,-8.246715],[1.307849,2.523168],[3.750646,-5.529257],[-5.812824,-1.221476],[-5.612198,-0.438433],[-5.392244,1.212197],[-0.974936,5.810597],[7.215973,4.208043],[4.523547,1.517871],[-6.761537,-9.577119],[6.449134,-9.744549],[-8.103163,-1.598971],[1.126670,5.202584],[-9.230283,9.338114],[4.805691,-0.516758],[7.189803,7.101453],[-2.371680,3.813462],[9.324452,-0.029043],[-7.617376,6.265371],[-1.784337,7.588061],[-1.194738,9.651442],[2.348667,7.755651],[7.657635,-1.166600]], dtype = "float32")#candidate|10649|(2640, 2)|const|float32
bop_10650 = relay.less(const_10614.astype('bool'), relay.reshape(const_10649.astype('bool'), relay.shape_of(const_10614))) # shape=(2640, 2)
output = relay.Tuple([call_10606,bop_10624,bop_10629,bop_10650,])
output2 = relay.Tuple([call_10607,bop_10627,bop_10632,bop_10650,])
func_10674 = relay.Function([], output)
mod['func_10674'] = func_10674
mod = relay.transform.InferType()(mod)
output = func_10674()
func_10675 = relay.Function([], output)
mutated_mod['func_10675'] = func_10675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6779_call = mod.get_global_var('func_6779')
func_6781_call = mutated_mod.get_global_var('func_6781')
call_10693 = func_6779_call()
call_10694 = func_6779_call()
output = call_10693
output2 = call_10694
func_10705 = relay.Function([], output)
mod['func_10705'] = func_10705
mod = relay.transform.InferType()(mod)
output = func_10705()
func_10706 = relay.Function([], output)
mutated_mod['func_10706'] = func_10706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9200_call = mod.get_global_var('func_9200')
func_9201_call = mutated_mod.get_global_var('func_9201')
call_10731 = relay.TupleGetItem(func_9200_call(), 0)
call_10732 = relay.TupleGetItem(func_9201_call(), 0)
func_9670_call = mod.get_global_var('func_9670')
func_9672_call = mutated_mod.get_global_var('func_9672')
const_10745 = relay.const([False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False], dtype = "bool")#candidate|10745|(140,)|const|bool
call_10744 = relay.TupleGetItem(func_9670_call(relay.reshape(const_10745.astype('bool'), [10, 2, 7])), 0)
call_10746 = relay.TupleGetItem(func_9672_call(relay.reshape(const_10745.astype('bool'), [10, 2, 7])), 0)
func_8904_call = mod.get_global_var('func_8904')
func_8906_call = mutated_mod.get_global_var('func_8906')
call_10753 = relay.TupleGetItem(func_8904_call(), 0)
call_10754 = relay.TupleGetItem(func_8906_call(), 0)
output = relay.Tuple([call_10731,call_10744,const_10745,call_10753,])
output2 = relay.Tuple([call_10732,call_10746,const_10745,call_10754,])
func_10755 = relay.Function([], output)
mod['func_10755'] = func_10755
mod = relay.transform.InferType()(mod)
output = func_10755()
func_10756 = relay.Function([], output)
mutated_mod['func_10756'] = func_10756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7284_call = mod.get_global_var('func_7284')
func_7285_call = mutated_mod.get_global_var('func_7285')
call_10798 = relay.TupleGetItem(func_7284_call(), 0)
call_10799 = relay.TupleGetItem(func_7285_call(), 0)
output = call_10798
output2 = call_10799
func_10802 = relay.Function([], output)
mod['func_10802'] = func_10802
mod = relay.transform.InferType()(mod)
output = func_10802()
func_10803 = relay.Function([], output)
mutated_mod['func_10803'] = func_10803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9057_call = mod.get_global_var('func_9057')
func_9058_call = mutated_mod.get_global_var('func_9058')
call_10806 = relay.TupleGetItem(func_9057_call(), 2)
call_10807 = relay.TupleGetItem(func_9058_call(), 2)
output = call_10806
output2 = call_10807
func_10808 = relay.Function([], output)
mod['func_10808'] = func_10808
mod = relay.transform.InferType()(mod)
output = func_10808()
func_10809 = relay.Function([], output)
mutated_mod['func_10809'] = func_10809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_10873 = func_4803_call()
call_10874 = func_4803_call()
output = call_10873
output2 = call_10874
func_10922 = relay.Function([], output)
mod['func_10922'] = func_10922
mod = relay.transform.InferType()(mod)
mutated_mod['func_10922'] = func_10922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10922_call = mutated_mod.get_global_var('func_10922')
call_10923 = func_10922_call()
output = call_10923
func_10924 = relay.Function([], output)
mutated_mod['func_10924'] = func_10924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mod.get_global_var('func_6154')
func_6155_call = mutated_mod.get_global_var('func_6155')
call_11012 = relay.TupleGetItem(func_6154_call(), 0)
call_11013 = relay.TupleGetItem(func_6155_call(), 0)
output = call_11012
output2 = call_11013
func_11014 = relay.Function([], output)
mod['func_11014'] = func_11014
mod = relay.transform.InferType()(mod)
mutated_mod['func_11014'] = func_11014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11014_call = mutated_mod.get_global_var('func_11014')
call_11015 = func_11014_call()
output = call_11015
func_11016 = relay.Function([], output)
mutated_mod['func_11016'] = func_11016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8264_call = mod.get_global_var('func_8264')
func_8266_call = mutated_mod.get_global_var('func_8266')
call_11082 = relay.TupleGetItem(func_8264_call(), 0)
call_11083 = relay.TupleGetItem(func_8266_call(), 0)
output = call_11082
output2 = call_11083
func_11090 = relay.Function([], output)
mod['func_11090'] = func_11090
mod = relay.transform.InferType()(mod)
mutated_mod['func_11090'] = func_11090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11090_call = mutated_mod.get_global_var('func_11090')
call_11091 = func_11090_call()
output = call_11091
func_11092 = relay.Function([], output)
mutated_mod['func_11092'] = func_11092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10808_call = mod.get_global_var('func_10808')
func_10809_call = mutated_mod.get_global_var('func_10809')
call_11123 = func_10808_call()
call_11124 = func_10808_call()
output = call_11123
output2 = call_11124
func_11141 = relay.Function([], output)
mod['func_11141'] = func_11141
mod = relay.transform.InferType()(mod)
output = func_11141()
func_11142 = relay.Function([], output)
mutated_mod['func_11142'] = func_11142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3990_call = mod.get_global_var('func_3990')
func_3991_call = mutated_mod.get_global_var('func_3991')
call_11149 = relay.TupleGetItem(func_3990_call(), 0)
call_11150 = relay.TupleGetItem(func_3991_call(), 0)
output = call_11149
output2 = call_11150
func_11151 = relay.Function([], output)
mod['func_11151'] = func_11151
mod = relay.transform.InferType()(mod)
output = func_11151()
func_11152 = relay.Function([], output)
mutated_mod['func_11152'] = func_11152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10182_call = mod.get_global_var('func_10182')
func_10184_call = mutated_mod.get_global_var('func_10184')
call_11186 = relay.TupleGetItem(func_10182_call(), 2)
call_11187 = relay.TupleGetItem(func_10184_call(), 2)
output = call_11186
output2 = call_11187
func_11197 = relay.Function([], output)
mod['func_11197'] = func_11197
mod = relay.transform.InferType()(mod)
output = func_11197()
func_11198 = relay.Function([], output)
mutated_mod['func_11198'] = func_11198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10012_call = mod.get_global_var('func_10012')
func_10014_call = mutated_mod.get_global_var('func_10014')
call_11214 = relay.TupleGetItem(func_10012_call(), 1)
call_11215 = relay.TupleGetItem(func_10014_call(), 1)
func_9266_call = mod.get_global_var('func_9266')
func_9268_call = mutated_mod.get_global_var('func_9268')
call_11256 = relay.TupleGetItem(func_9266_call(), 0)
call_11257 = relay.TupleGetItem(func_9268_call(), 0)
bop_11261 = relay.logical_and(call_11256.astype('bool'), relay.reshape(call_11214.astype('bool'), relay.shape_of(call_11256))) # shape=(10, 1, 7)
bop_11264 = relay.logical_and(call_11257.astype('bool'), relay.reshape(call_11215.astype('bool'), relay.shape_of(call_11257))) # shape=(10, 1, 7)
output = relay.Tuple([bop_11261,])
output2 = relay.Tuple([bop_11264,])
func_11286 = relay.Function([], output)
mod['func_11286'] = func_11286
mod = relay.transform.InferType()(mod)
output = func_11286()
func_11287 = relay.Function([], output)
mutated_mod['func_11287'] = func_11287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6731_call = mod.get_global_var('func_6731')
func_6733_call = mutated_mod.get_global_var('func_6733')
call_11320 = relay.TupleGetItem(func_6731_call(), 0)
call_11321 = relay.TupleGetItem(func_6733_call(), 0)
func_7062_call = mod.get_global_var('func_7062')
func_7065_call = mutated_mod.get_global_var('func_7065')
const_11330 = relay.const([[-8.265366,8.575385,-9.648789,-2.391480,-4.588598,-3.422160],[-7.370123,5.752848,5.514536,0.305966,9.306202,7.894607],[0.592974,7.742476,7.207354,-0.476518,-9.402885,2.882490],[3.948086,5.589743,3.123535,6.970586,8.493824,-0.426191],[0.489828,7.187345,-9.195730,-2.631193,-4.094088,7.489295],[-8.884070,9.094892,4.407140,-9.093509,-2.348725,-1.283365],[4.340852,7.882916,-4.853015,5.425198,7.480421,-7.158948],[4.404318,-8.291820,-2.978209,9.543361,4.255623,-1.404263],[6.338051,-9.234993,-9.834179,5.663612,-3.925448,-0.741071],[-1.437914,-5.504752,0.620302,7.881132,1.579653,-2.056969],[6.919081,5.449137,-6.786157,5.158216,-4.307043,4.532551],[7.672096,-3.127394,-0.683262,-5.786716,-3.209296,-1.421838],[-9.455584,-4.708609,9.482691,4.831805,-6.875140,-5.602516],[-3.877484,0.882408,5.555280,-0.189841,1.772925,-1.426306],[6.108105,1.476932,-0.393530,8.055403,8.445592,-9.824515],[-3.384941,-5.970902,-9.708157,8.954542,-1.099533,3.878127],[-9.014216,-8.806745,-5.704803,8.832245,-5.431636,5.859590],[-4.555443,7.261092,-7.039118,5.494067,3.895136,-0.529216],[-0.233307,4.555947,-8.296988,-2.734976,-2.055246,-0.271879],[2.222621,-9.968783,-1.919876,-2.551188,0.065342,0.343018],[-7.857827,-5.907795,-7.062438,2.365425,3.558516,3.477389],[-4.398690,-2.606730,0.832847,6.366653,-2.605430,-0.823893],[-7.088717,0.241591,-3.097424,7.064529,3.381441,-6.630668],[-6.503638,-4.826657,-5.131433,4.166639,5.101869,4.584125]], dtype = "float64")#candidate|11330|(24, 6)|const|float64
call_11329 = func_7062_call(relay.reshape(const_11330.astype('float64'), [4, 12, 3]))
call_11331 = func_7062_call(relay.reshape(const_11330.astype('float64'), [4, 12, 3]))
func_5550_call = mod.get_global_var('func_5550')
func_5552_call = mutated_mod.get_global_var('func_5552')
call_11349 = relay.TupleGetItem(func_5550_call(), 0)
call_11350 = relay.TupleGetItem(func_5552_call(), 0)
bop_11352 = relay.subtract(call_11329.astype('int64'), relay.reshape(const_11330.astype('int64'), relay.shape_of(call_11329))) # shape=(4, 12, 3)
bop_11355 = relay.subtract(call_11331.astype('int64'), relay.reshape(const_11330.astype('int64'), relay.shape_of(call_11331))) # shape=(4, 12, 3)
func_10802_call = mod.get_global_var('func_10802')
func_10803_call = mutated_mod.get_global_var('func_10803')
call_11373 = func_10802_call()
call_11374 = func_10802_call()
output = relay.Tuple([call_11320,call_11349,bop_11352,call_11373,])
output2 = relay.Tuple([call_11321,call_11350,bop_11355,call_11374,])
func_11377 = relay.Function([], output)
mod['func_11377'] = func_11377
mod = relay.transform.InferType()(mod)
output = func_11377()
func_11378 = relay.Function([], output)
mutated_mod['func_11378'] = func_11378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11090_call = mod.get_global_var('func_11090')
func_11092_call = mutated_mod.get_global_var('func_11092')
call_11379 = func_11090_call()
call_11380 = func_11090_call()
func_5550_call = mod.get_global_var('func_5550')
func_5552_call = mutated_mod.get_global_var('func_5552')
call_11383 = relay.TupleGetItem(func_5550_call(), 0)
call_11384 = relay.TupleGetItem(func_5552_call(), 0)
func_10448_call = mod.get_global_var('func_10448')
func_10449_call = mutated_mod.get_global_var('func_10449')
call_11385 = func_10448_call()
call_11386 = func_10448_call()
output = relay.Tuple([call_11379,call_11383,call_11385,])
output2 = relay.Tuple([call_11380,call_11384,call_11386,])
func_11398 = relay.Function([], output)
mod['func_11398'] = func_11398
mod = relay.transform.InferType()(mod)
mutated_mod['func_11398'] = func_11398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11398_call = mutated_mod.get_global_var('func_11398')
call_11399 = func_11398_call()
output = call_11399
func_11400 = relay.Function([], output)
mutated_mod['func_11400'] = func_11400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10448_call = mod.get_global_var('func_10448')
func_10449_call = mutated_mod.get_global_var('func_10449')
call_11409 = func_10448_call()
call_11410 = func_10448_call()
func_3917_call = mod.get_global_var('func_3917')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_11414 = relay.TupleGetItem(func_3917_call(relay.reshape(call_11409.astype('bool'), [10, 1, 7])), 0)
call_11415 = relay.TupleGetItem(func_3920_call(relay.reshape(call_11409.astype('bool'), [10, 1, 7])), 0)
func_6193_call = mod.get_global_var('func_6193')
func_6199_call = mutated_mod.get_global_var('func_6199')
const_11420 = relay.const([-4,7,-6,7,6,8,2,-8,-5,-1,5,7,-5,-7,9,-10,-9,-10,-8,7,-9,-5,-9,7,-3,-7,8,-10,6,-3,9,9,10,7,8,-4,-8,-10,-2,-3,3,-3,3,-6,-3,5,2,-2,-5,2,2,10,3,-9,7,1,-3,1,-10,-4,-7,4,4,4,6,3,-2,-10,-3,1,2,-9,6,10,10,8,-6,7,-2,-9,6,6,5,4,-4,9,5,-10,10,9,-5,-7,1,9,6,-10,10,-2,-4,4,-1,4,2,9,4,-4,-4,8,-9,-7,-6,9,4,2,10,-8,8,-9,5,-2,5,-8,9,2,-6,2,7,10,7,-3,-6,9,10,4,-7,6,4,-9,-3,-10,-4,-1,-6,-4,10,1,8,-2,10,-6,4,-9,8,-3,10,10,-8,7,-1,-8,-8,-9,-2,7,-6,-9,4,1,5,-3,-7,-1,3,10,8,-6,-8,-5,5,2,-4,4,-8,-2,-10,2,-9,4,-10,7,-4,-6,-6,-5,-4,4,10,8,4,-3,-6,-2,7,-6,-2,-4,-5,-9,3,4,10,7,-6,8,-4,2,5,4,2,8,2,8,-2,10,10,-5,2,2,9,-5,10,-3,-3,-6,7,-7,-4,8,-4,5,4,6,-4,-3,-8,-5,8,-3,7,6,-3,-6,-1,-7,5,-9,-4,5,3,2,-6,10,-7,7,-4,9,-7,4,-1,1,3,-7,6,4,9,3,-4,-1,9,4,-10,-1,-10,-5,8,-9,7,-7,-7,6,-8,3,-3,-3,-4,-6,-2,1,3,-4,-3,1,8,-7,-8,1,2,-8,-10,-9,-7,-7,3,-4,-6,-7,-1,1,4,-4,-10,2,9,-9,2,1,5,10,-8,6,3,6,-2,5,4,-2,-2,-8,-4,-10,-5,6,9,-1,2,-4,3,-1,7,-10,-3,7,7,-6,10,-7,-7,8,9,-4,7,6,-7,2,2,5,6,-1,-5,6,-3,2,-6,-5,-10,-7,-8,-6,1,9,3,7,7,-4,4,-10,1,-6,-2,3,1,-8,5,6,-3,-7,2,-6,1,1,-8,-2,-3,-7,1,-7,-9,3,-1,10,-7,-10,3,6,-4,9,8,-2,-2,-3,10,-5,-9,5,-9,-3,1,5,-9,-8,-10,4,10,6,-6,3,3,7,8,1,6,-6,-9,-3,-4,1,9,9,-3,1,5,7,4,9,3,-1,-6,-8,-8,1,-1,5,8,-9,-2,-4,4,7,3,-10,-6,7,-8,4,5,9,10,6,-9,-2,-5,7,6,-7,-10,9,-8,7,-1,-1,10,4,3,9,5,4,-6,1,-5,-4,5,-2,-8,-8,-1,7,8,-1,-1,4,2,10,-9,1,-9,-10,6,9,2,-7,8,-4,7,-9,8,6,1,7,7,5,-2,-2,10,4,-1,-5,-7,7,-8,2,-2,-3,4,-5,9,1,-7,-2,6,-9,9,6,-4,-9,1,-8,10,8,-3,-9,4,-6,2,-10,-5,5,-4,1,-6,-10,-2,2,10,-7,2,7,-5,9,-2,6,-7,-3,-4,8,-5,-8,7,-8,-1,-3,-3,1,5,3,-6,-5,2,1,-4,-5,-7,5,-5,2,2,-1,6,-10,9,-8,-4,9,3,-9,10,6,-9,3,6,1,3,-2,3,9,7,8,-10,-7,-6,-10,4,-4,-6,10,2,-1,-3,-3,-5,10,-2,5,-3,7,-3,-6,10,2,6,-8,-3,-5,-2,-5,-5,-2,1,-10,-2,-8], dtype = "int64")#candidate|11420|(660,)|const|int64
const_11421 = relay.const([-2.189856,1.931008,-8.163323,9.466403,-4.906651,9.392262,-3.096053,4.732247,6.065110,8.787093,-7.900972,-3.526097,-3.751109,5.860461,-8.264294,9.089006,1.376959,-5.045074,1.470254,-2.478855,-6.959484,5.455019,0.378888,9.903945,-0.012656,8.198416,-3.823044,5.731697,2.498441,-0.342589,5.791968,5.610307,-4.213894,7.907922,8.373101,-7.800592,2.406369,-8.111866,-4.437440,7.455355,-5.278414,7.861960,3.902760,-7.425179,9.949601,-8.543730,-7.931195,4.066446,2.135305,-6.985279,-2.869525,6.147118,-4.183836,6.992482,2.356095,3.685826,4.258229,9.413678,6.361630,2.657197,-2.274535,-8.441389,8.916956,-5.211536,-2.143260,1.187230,5.805729,-5.588026,-3.091415,-9.162926,-5.981134,-4.748281,5.976860,-0.627573,3.848225,5.775530,-2.993249,-2.408811,-2.025214,-5.917678,-3.187058,4.251597,-3.107311,4.279451,8.117746,2.166895,-1.482487,0.124212], dtype = "float64")#candidate|11421|(88,)|const|float64
call_11419 = relay.TupleGetItem(func_6193_call(relay.reshape(const_11420.astype('int64'), [5, 11, 12]), relay.reshape(const_11420.astype('int64'), [5, 11, 12]), relay.reshape(const_11421.astype('float64'), [88, 1]), relay.reshape(const_11420.astype('int64'), [5, 11, 12]), ), 3)
call_11422 = relay.TupleGetItem(func_6199_call(relay.reshape(const_11420.astype('int64'), [5, 11, 12]), relay.reshape(const_11420.astype('int64'), [5, 11, 12]), relay.reshape(const_11421.astype('float64'), [88, 1]), relay.reshape(const_11420.astype('int64'), [5, 11, 12]), ), 3)
func_10448_call = mod.get_global_var('func_10448')
func_10449_call = mutated_mod.get_global_var('func_10449')
call_11423 = func_10448_call()
call_11424 = func_10448_call()
output = relay.Tuple([call_11409,call_11414,call_11419,const_11420,const_11421,call_11423,])
output2 = relay.Tuple([call_11410,call_11415,call_11422,const_11420,const_11421,call_11424,])
func_11446 = relay.Function([], output)
mod['func_11446'] = func_11446
mod = relay.transform.InferType()(mod)
output = func_11446()
func_11447 = relay.Function([], output)
mutated_mod['func_11447'] = func_11447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10922_call = mod.get_global_var('func_10922')
func_10924_call = mutated_mod.get_global_var('func_10924')
call_11538 = func_10922_call()
call_11539 = func_10922_call()
output = call_11538
output2 = call_11539
func_11576 = relay.Function([], output)
mod['func_11576'] = func_11576
mod = relay.transform.InferType()(mod)
mutated_mod['func_11576'] = func_11576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11576_call = mutated_mod.get_global_var('func_11576')
call_11577 = func_11576_call()
output = call_11577
func_11578 = relay.Function([], output)
mutated_mod['func_11578'] = func_11578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8977_call = mod.get_global_var('func_8977')
func_8979_call = mutated_mod.get_global_var('func_8979')
call_11592 = relay.TupleGetItem(func_8977_call(), 0)
call_11593 = relay.TupleGetItem(func_8979_call(), 0)
output = call_11592
output2 = call_11593
func_11594 = relay.Function([], output)
mod['func_11594'] = func_11594
mod = relay.transform.InferType()(mod)
output = func_11594()
func_11595 = relay.Function([], output)
mutated_mod['func_11595'] = func_11595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3640_call = mod.get_global_var('func_3640')
func_3642_call = mutated_mod.get_global_var('func_3642')
call_11599 = func_3640_call()
call_11600 = func_3640_call()
var_11604 = relay.var("var_11604", dtype = "bool", shape = (10, 5, 7))#candidate|11604|(10, 5, 7)|var|bool
bop_11605 = relay.subtract(call_11599.astype('int64'), var_11604.astype('int64')) # shape=(10, 5, 7)
bop_11608 = relay.subtract(call_11600.astype('int64'), var_11604.astype('int64')) # shape=(10, 5, 7)
output = bop_11605
output2 = bop_11608
func_11613 = relay.Function([var_11604,], output)
mod['func_11613'] = func_11613
mod = relay.transform.InferType()(mod)
mutated_mod['func_11613'] = func_11613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11614 = relay.var("var_11614", dtype = "bool", shape = (10, 5, 7))#candidate|11614|(10, 5, 7)|var|bool
func_11613_call = mutated_mod.get_global_var('func_11613')
call_11615 = func_11613_call(var_11614)
output = call_11615
func_11616 = relay.Function([var_11614], output)
mutated_mod['func_11616'] = func_11616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5980_call = mod.get_global_var('func_5980')
func_5981_call = mutated_mod.get_global_var('func_5981')
call_11635 = relay.TupleGetItem(func_5980_call(), 1)
call_11636 = relay.TupleGetItem(func_5981_call(), 1)
func_3228_call = mod.get_global_var('func_3228')
func_3230_call = mutated_mod.get_global_var('func_3230')
call_11647 = func_3228_call()
call_11648 = func_3228_call()
func_5433_call = mod.get_global_var('func_5433')
func_5435_call = mutated_mod.get_global_var('func_5435')
call_11657 = func_5433_call()
call_11658 = func_5433_call()
output = relay.Tuple([call_11635,call_11647,call_11657,])
output2 = relay.Tuple([call_11636,call_11648,call_11658,])
func_11697 = relay.Function([], output)
mod['func_11697'] = func_11697
mod = relay.transform.InferType()(mod)
output = func_11697()
func_11698 = relay.Function([], output)
mutated_mod['func_11698'] = func_11698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10755_call = mod.get_global_var('func_10755')
func_10756_call = mutated_mod.get_global_var('func_10756')
call_11705 = relay.TupleGetItem(func_10755_call(), 3)
call_11706 = relay.TupleGetItem(func_10756_call(), 3)
output = call_11705
output2 = call_11706
func_11707 = relay.Function([], output)
mod['func_11707'] = func_11707
mod = relay.transform.InferType()(mod)
output = func_11707()
func_11708 = relay.Function([], output)
mutated_mod['func_11708'] = func_11708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10557_call = mod.get_global_var('func_10557')
func_10558_call = mutated_mod.get_global_var('func_10558')
call_11744 = relay.TupleGetItem(func_10557_call(), 1)
call_11745 = relay.TupleGetItem(func_10558_call(), 1)
uop_11752 = relay.sinh(call_11744.astype('float64')) # shape=(352, 5)
uop_11754 = relay.sinh(call_11745.astype('float64')) # shape=(352, 5)
uop_11756 = relay.log2(call_11744.astype('float32')) # shape=(352, 5)
uop_11758 = relay.log2(call_11745.astype('float32')) # shape=(352, 5)
func_11446_call = mod.get_global_var('func_11446')
func_11447_call = mutated_mod.get_global_var('func_11447')
call_11759 = relay.TupleGetItem(func_11446_call(), 4)
call_11760 = relay.TupleGetItem(func_11447_call(), 4)
uop_11770 = relay.asin(uop_11752.astype('float64')) # shape=(352, 5)
uop_11772 = relay.asin(uop_11754.astype('float64')) # shape=(352, 5)
output = relay.Tuple([uop_11756,call_11759,uop_11770,])
output2 = relay.Tuple([uop_11758,call_11760,uop_11772,])
func_11783 = relay.Function([], output)
mod['func_11783'] = func_11783
mod = relay.transform.InferType()(mod)
output = func_11783()
func_11784 = relay.Function([], output)
mutated_mod['func_11784'] = func_11784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8877_call = mod.get_global_var('func_8877')
func_8878_call = mutated_mod.get_global_var('func_8878')
call_11808 = relay.TupleGetItem(func_8877_call(), 1)
call_11809 = relay.TupleGetItem(func_8878_call(), 1)
output = call_11808
output2 = call_11809
func_11813 = relay.Function([], output)
mod['func_11813'] = func_11813
mod = relay.transform.InferType()(mod)
mutated_mod['func_11813'] = func_11813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11813_call = mutated_mod.get_global_var('func_11813')
call_11814 = func_11813_call()
output = call_11814
func_11815 = relay.Function([], output)
mutated_mod['func_11815'] = func_11815
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11841 = relay.var("var_11841", dtype = "int8", shape = (10, 4, 1))#candidate|11841|(10, 4, 1)|var|int8
const_11842 = relay.const([[[3,-7,-8,-4,-6,-9],[8,-10,7,10,-4,-5],[9,4,10,-10,-10,5],[9,-4,2,1,-3,3]],[[-2,-7,-4,-3,-2,1],[-1,-6,-1,10,-4,4],[-10,-6,-7,2,1,-8],[-2,2,-10,-7,-5,3]],[[-5,5,-7,-3,-3,9],[9,-1,-1,-7,-2,6],[-1,2,-7,9,9,-1],[-2,-3,-5,-7,4,-5]],[[7,-7,-1,10,7,6],[-10,-5,-1,-5,-1,8],[-1,-2,-2,-1,1,9],[-4,-1,-4,6,-4,-3]],[[7,7,-4,-6,9,3],[7,4,3,-7,6,-7],[-5,-6,-4,-3,5,-1],[-5,8,-6,-9,5,10]],[[-7,-3,7,5,5,-10],[-8,-9,4,-4,8,-5],[2,-9,7,3,8,-7],[9,6,1,2,10,-4]],[[1,3,7,4,-2,-6],[-2,-3,6,5,3,-9],[1,6,3,8,-6,-7],[-1,-4,-4,1,9,8]],[[5,-3,9,3,-3,3],[-8,4,-2,-9,-2,5],[3,-5,2,-8,-9,5],[4,7,-10,-5,-9,-4]],[[-2,3,8,-1,6,3],[-9,4,3,5,-1,5],[3,10,3,-3,7,-8],[-6,7,-4,9,-3,-1]],[[-6,6,-1,9,-4,-5],[2,-9,-6,7,-5,3],[5,3,8,-6,4,-2],[-4,-6,1,-3,-9,-4]]], dtype = "int8")#candidate|11842|(10, 4, 6)|const|int8
bop_11843 = relay.bitwise_and(var_11841.astype('int8'), const_11842.astype('int8')) # shape=(10, 4, 6)
output = bop_11843
output2 = bop_11843
func_11851 = relay.Function([var_11841,], output)
mod['func_11851'] = func_11851
mod = relay.transform.InferType()(mod)
var_11852 = relay.var("var_11852", dtype = "int8", shape = (10, 4, 1))#candidate|11852|(10, 4, 1)|var|int8
output = func_11851(var_11852)
func_11853 = relay.Function([var_11852], output)
mutated_mod['func_11853'] = func_11853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8977_call = mod.get_global_var('func_8977')
func_8979_call = mutated_mod.get_global_var('func_8979')
call_11855 = relay.TupleGetItem(func_8977_call(), 0)
call_11856 = relay.TupleGetItem(func_8979_call(), 0)
func_11141_call = mod.get_global_var('func_11141')
func_11142_call = mutated_mod.get_global_var('func_11142')
call_11861 = func_11141_call()
call_11862 = func_11141_call()
output = relay.Tuple([call_11855,call_11861,])
output2 = relay.Tuple([call_11856,call_11862,])
func_11877 = relay.Function([], output)
mod['func_11877'] = func_11877
mod = relay.transform.InferType()(mod)
output = func_11877()
func_11878 = relay.Function([], output)
mutated_mod['func_11878'] = func_11878
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11902 = relay.const([[[9.241288,-6.200921,2.359802,-6.948269,3.834624,-8.655933,-1.769514,1.078979,-8.423382,-1.124207,-1.500433,7.145495,-5.387044,-2.211098,7.285686,5.388275],[-5.388168,-9.587316,3.073364,-4.939886,-3.199321,-4.298708,-6.982562,-6.297609,-0.470524,8.810291,2.079440,-3.002078,7.596290,4.029845,-3.368677,2.594900],[-6.064027,5.830418,-8.622300,-6.689259,-1.602325,-6.072325,-2.188084,0.494596,5.506756,-2.601151,3.851323,-4.736763,3.824695,9.989524,-6.741185,9.801785],[2.397498,0.213810,-7.363579,-2.085696,-8.630664,2.123742,-0.117616,1.315029,-4.616543,-0.340627,3.472142,-7.342202,-5.528730,-8.576288,-1.420009,8.796835],[-8.448835,-4.234094,-1.708098,5.237280,4.095223,-0.974531,4.436825,8.107885,0.722567,8.296116,-3.660871,8.707109,-6.837761,9.615345,1.385966,-0.808708],[2.022351,-4.700835,4.663289,9.990641,4.314701,-6.850385,8.780955,-0.518770,-0.609168,4.037750,2.152491,4.916555,9.986233,-7.950906,-6.337671,-4.991540],[6.540737,2.429495,8.596349,2.432810,-5.992925,5.980007,5.467380,-5.712090,-8.318366,-6.282679,5.771241,7.176725,4.016859,1.005692,-9.051904,8.264534],[0.330008,-7.586681,4.004218,1.924638,-8.814603,-2.961469,-1.999270,1.562522,-6.291868,-7.040300,9.566689,-0.906990,2.933954,-9.221576,-2.352345,-3.795931],[0.107292,-0.729260,-4.297318,-9.291448,-4.522370,0.569708,-0.647792,6.271813,-3.939976,-5.721874,5.863831,-4.001091,-0.418261,-2.840916,6.136749,-2.001192],[-8.162643,3.685907,-6.880757,2.209510,-6.379211,6.370034,6.383279,-0.800794,-5.465465,3.006786,4.116064,9.079948,0.399865,-4.649243,-5.370684,8.054209],[8.290575,8.481715,-9.001997,9.500111,5.392763,2.816200,8.982438,3.976260,-1.122693,-3.883683,-4.979714,-2.137246,8.421127,-0.783654,7.276289,-6.873086],[7.226791,4.268584,-7.851853,-9.258712,3.310835,-9.690522,0.676134,3.479278,5.696555,-1.760340,6.222440,8.426543,4.424075,-0.731421,4.239049,-6.405514]],[[-1.516371,-4.274092,-0.217751,1.392544,9.551286,-2.600490,1.328904,-0.564009,7.190521,-5.369351,0.551662,-8.751491,-3.161890,-7.623691,3.755683,-5.125267],[-8.243161,0.024189,1.168132,-9.721302,-1.640231,-5.315434,-5.638864,-3.949047,4.020451,-0.799652,-0.523326,7.545469,2.523959,-1.056640,-7.077966,5.890930],[-6.931233,1.093454,2.500284,-4.370316,5.664186,1.903480,6.860924,8.322335,-1.121434,-8.555334,-1.948366,1.435655,6.209383,7.706065,-5.850871,-6.735064],[3.014252,0.955184,5.914434,-6.471619,-0.033082,1.200527,-6.216384,-7.481492,-3.267353,2.964751,-5.348684,2.249070,5.688830,-6.980340,8.696636,-6.060648],[-8.606063,3.644632,7.422727,-7.014183,2.044305,5.347970,0.565608,-4.081589,-8.158259,-7.507536,3.390128,-7.803511,-2.315727,-6.960291,1.479649,-3.565709],[-0.456474,-4.854455,-3.804921,5.916507,-4.578595,8.936637,-1.616108,7.513999,2.067518,-0.654155,5.675077,7.987997,5.868071,3.707738,-4.858856,-1.730862],[5.499991,-5.024077,-9.543298,2.567273,0.991099,-8.113052,5.543971,-2.231933,5.898603,8.860876,-9.233560,4.393458,-8.366553,-3.192873,-9.084715,-8.683630],[2.065930,2.023183,-7.717992,-1.314624,8.572460,-7.431590,0.047970,-5.701535,6.573985,9.051384,-2.679594,2.759765,-0.265167,-7.827635,-9.772851,-9.432770],[1.372324,4.475609,9.500105,4.921931,-3.727442,4.766235,3.677941,3.129741,6.961059,-2.398385,8.135415,-8.587213,2.181268,-3.869174,6.286352,-9.873776],[7.385510,1.337380,5.702008,8.011956,-7.620868,8.672395,-2.295872,-6.529634,-6.883723,-6.241223,-1.033798,6.280845,6.901819,1.760021,-3.959674,0.727327],[-2.019968,-1.263593,-2.270448,5.283918,-6.594588,-4.359928,7.404991,-3.812839,6.494092,3.511793,-4.326900,7.086263,1.713518,-1.723892,-0.271679,5.301530],[-6.005010,3.784742,9.519089,6.374714,1.054969,5.132499,-3.456274,-4.105283,-2.787652,1.143398,-0.288825,-8.392712,-4.559974,-2.998548,-5.177660,6.892266]],[[9.080153,0.600314,8.586988,7.604889,-1.032297,-8.367329,-4.112211,-7.113560,-8.856334,1.120496,3.939822,-8.931263,7.979984,-4.118826,-9.669355,-9.600631],[-8.740526,8.759661,9.549767,4.203424,1.526923,-9.676124,-0.029193,-6.604384,5.685615,-2.301737,1.768500,-0.752560,2.535166,-2.816016,-8.085314,6.096009],[8.018988,-2.499962,8.739313,-8.360916,6.556723,6.483617,-0.169144,0.599217,9.372962,-7.615542,-7.569292,1.246784,5.684799,-0.604009,3.546800,4.932200],[-7.752594,9.582305,7.896623,-4.406551,-5.623730,-3.340571,6.795179,-0.536397,6.397507,5.963425,0.535937,5.031554,-0.625644,-7.583583,-9.068192,-3.032487],[-2.184760,-6.567406,-0.013728,-3.214033,-3.941440,7.097635,-0.920234,4.035670,-2.002474,-6.988432,0.315630,-3.169846,7.553121,3.246859,-0.938772,-6.634813],[6.119478,-3.401210,4.955498,4.254578,-7.329733,1.706115,-8.895086,-7.730374,6.291939,2.363466,0.690148,-2.750636,-9.453051,-0.231024,-9.332785,0.685822],[3.004185,9.415810,8.122447,8.838052,2.581461,-1.436655,2.865879,-4.187502,8.696951,0.474169,5.715438,5.393060,-7.463772,0.247174,-3.072511,-7.978409],[-3.526851,-7.872817,-3.713856,9.134482,-0.889416,-8.166388,8.973306,-9.293300,-1.944012,3.744160,-0.433206,7.305840,-2.480252,8.084624,-4.819587,-6.777219],[4.943084,-8.474828,-9.907249,9.715014,4.539717,-3.365072,-3.795082,-9.415532,0.941151,-4.752752,-3.395237,-8.693710,-4.625884,-5.269003,2.641696,-4.998865],[7.784891,8.973469,-2.491695,7.598825,-1.070217,-1.459300,-0.458490,5.587177,-1.960434,0.798371,0.469062,1.049252,8.103227,-0.361628,4.240073,7.878528],[3.822312,-2.476159,2.151710,-7.671188,-2.810165,-3.895406,6.765756,-5.443751,-0.378398,-5.498651,5.157813,8.796242,3.924659,3.352331,-7.438365,-5.907380],[9.356879,-7.188990,-8.849753,-5.763388,9.192732,5.909974,-0.029442,7.750560,-2.791309,1.203055,2.170125,-2.225674,-6.084233,5.795934,2.550181,2.392709]]], dtype = "float32")#candidate|11902|(3, 12, 16)|const|float32
uop_11903 = relay.sin(const_11902.astype('float32')) # shape=(3, 12, 16)
output = relay.Tuple([uop_11903,])
output2 = relay.Tuple([uop_11903,])
func_11919 = relay.Function([], output)
mod['func_11919'] = func_11919
mod = relay.transform.InferType()(mod)
mutated_mod['func_11919'] = func_11919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11919_call = mutated_mod.get_global_var('func_11919')
call_11920 = func_11919_call()
output = call_11920
func_11921 = relay.Function([], output)
mutated_mod['func_11921'] = func_11921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mod.get_global_var('func_5343')
func_5345_call = mutated_mod.get_global_var('func_5345')
call_11922 = relay.TupleGetItem(func_5343_call(), 0)
call_11923 = relay.TupleGetItem(func_5345_call(), 0)
output = call_11922
output2 = call_11923
func_11930 = relay.Function([], output)
mod['func_11930'] = func_11930
mod = relay.transform.InferType()(mod)
mutated_mod['func_11930'] = func_11930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11930_call = mutated_mod.get_global_var('func_11930')
call_11931 = func_11930_call()
output = call_11931
func_11932 = relay.Function([], output)
mutated_mod['func_11932'] = func_11932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6071_call = mod.get_global_var('func_6071')
func_6072_call = mutated_mod.get_global_var('func_6072')
call_11943 = func_6071_call()
call_11944 = func_6071_call()
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_11948 = func_4803_call()
call_11949 = func_4803_call()
output = relay.Tuple([call_11943,call_11948,])
output2 = relay.Tuple([call_11944,call_11949,])
func_11952 = relay.Function([], output)
mod['func_11952'] = func_11952
mod = relay.transform.InferType()(mod)
mutated_mod['func_11952'] = func_11952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11952_call = mutated_mod.get_global_var('func_11952')
call_11953 = func_11952_call()
output = call_11953
func_11954 = relay.Function([], output)
mutated_mod['func_11954'] = func_11954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6071_call = mod.get_global_var('func_6071')
func_6072_call = mutated_mod.get_global_var('func_6072')
call_11964 = func_6071_call()
call_11965 = func_6071_call()
func_11697_call = mod.get_global_var('func_11697')
func_11698_call = mutated_mod.get_global_var('func_11698')
call_11972 = relay.TupleGetItem(func_11697_call(), 1)
call_11973 = relay.TupleGetItem(func_11698_call(), 1)
output = relay.Tuple([call_11964,call_11972,])
output2 = relay.Tuple([call_11965,call_11973,])
func_11982 = relay.Function([], output)
mod['func_11982'] = func_11982
mod = relay.transform.InferType()(mod)
output = func_11982()
func_11983 = relay.Function([], output)
mutated_mod['func_11983'] = func_11983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5863_call = mod.get_global_var('func_5863')
func_5865_call = mutated_mod.get_global_var('func_5865')
call_12022 = relay.TupleGetItem(func_5863_call(), 0)
call_12023 = relay.TupleGetItem(func_5865_call(), 0)
func_8450_call = mod.get_global_var('func_8450')
func_8452_call = mutated_mod.get_global_var('func_8452')
call_12028 = relay.TupleGetItem(func_8450_call(), 0)
call_12029 = relay.TupleGetItem(func_8452_call(), 0)
output = relay.Tuple([call_12022,call_12028,])
output2 = relay.Tuple([call_12023,call_12029,])
func_12038 = relay.Function([], output)
mod['func_12038'] = func_12038
mod = relay.transform.InferType()(mod)
output = func_12038()
func_12039 = relay.Function([], output)
mutated_mod['func_12039'] = func_12039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4878_call = mod.get_global_var('func_4878')
func_4880_call = mutated_mod.get_global_var('func_4880')
call_12066 = relay.TupleGetItem(func_4878_call(), 1)
call_12067 = relay.TupleGetItem(func_4880_call(), 1)
uop_12073 = relay.rsqrt(call_12066.astype('float64')) # shape=(352, 5)
uop_12075 = relay.rsqrt(call_12067.astype('float64')) # shape=(352, 5)
output = uop_12073
output2 = uop_12075
func_12087 = relay.Function([], output)
mod['func_12087'] = func_12087
mod = relay.transform.InferType()(mod)
output = func_12087()
func_12088 = relay.Function([], output)
mutated_mod['func_12088'] = func_12088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_12122 = func_4803_call()
call_12123 = func_4803_call()
output = relay.Tuple([call_12122,])
output2 = relay.Tuple([call_12123,])
func_12124 = relay.Function([], output)
mod['func_12124'] = func_12124
mod = relay.transform.InferType()(mod)
mutated_mod['func_12124'] = func_12124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12124_call = mutated_mod.get_global_var('func_12124')
call_12125 = func_12124_call()
output = call_12125
func_12126 = relay.Function([], output)
mutated_mod['func_12126'] = func_12126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8977_call = mod.get_global_var('func_8977')
func_8979_call = mutated_mod.get_global_var('func_8979')
call_12133 = relay.TupleGetItem(func_8977_call(), 0)
call_12134 = relay.TupleGetItem(func_8979_call(), 0)
func_4622_call = mod.get_global_var('func_4622')
func_4623_call = mutated_mod.get_global_var('func_4623')
call_12136 = relay.TupleGetItem(func_4622_call(), 0)
call_12137 = relay.TupleGetItem(func_4623_call(), 0)
func_8790_call = mod.get_global_var('func_8790')
func_8791_call = mutated_mod.get_global_var('func_8791')
call_12168 = relay.TupleGetItem(func_8790_call(), 1)
call_12169 = relay.TupleGetItem(func_8791_call(), 1)
func_4744_call = mod.get_global_var('func_4744')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_12198 = func_4744_call()
call_12199 = func_4744_call()
func_11141_call = mod.get_global_var('func_11141')
func_11142_call = mutated_mod.get_global_var('func_11142')
call_12204 = func_11141_call()
call_12205 = func_11141_call()
uop_12206 = relay.acosh(call_12133.astype('float64')) # shape=(9, 1, 12)
uop_12208 = relay.acosh(call_12134.astype('float64')) # shape=(9, 1, 12)
func_11151_call = mod.get_global_var('func_11151')
func_11152_call = mutated_mod.get_global_var('func_11152')
call_12209 = func_11151_call()
call_12210 = func_11151_call()
bop_12211 = relay.left_shift(uop_12206.astype('uint32'), relay.reshape(call_12133.astype('uint32'), relay.shape_of(uop_12206))) # shape=(9, 1, 12)
bop_12214 = relay.left_shift(uop_12208.astype('uint32'), relay.reshape(call_12134.astype('uint32'), relay.shape_of(uop_12208))) # shape=(9, 1, 12)
uop_12234 = relay.log(call_12136.astype('float64')) # shape=(352, 5)
uop_12236 = relay.log(call_12137.astype('float64')) # shape=(352, 5)
bop_12244 = relay.logical_or(uop_12206.astype('bool'), relay.reshape(bop_12211.astype('bool'), relay.shape_of(uop_12206))) # shape=(9, 1, 12)
bop_12247 = relay.logical_or(uop_12208.astype('bool'), relay.reshape(bop_12214.astype('bool'), relay.shape_of(uop_12208))) # shape=(9, 1, 12)
uop_12259 = relay.sin(uop_12234.astype('float64')) # shape=(352, 5)
uop_12261 = relay.sin(uop_12236.astype('float64')) # shape=(352, 5)
output = relay.Tuple([call_12168,call_12198,call_12204,call_12209,bop_12244,uop_12259,])
output2 = relay.Tuple([call_12169,call_12199,call_12205,call_12210,bop_12247,uop_12261,])
func_12276 = relay.Function([], output)
mod['func_12276'] = func_12276
mod = relay.transform.InferType()(mod)
mutated_mod['func_12276'] = func_12276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12276_call = mutated_mod.get_global_var('func_12276')
call_12277 = func_12276_call()
output = call_12277
func_12278 = relay.Function([], output)
mutated_mod['func_12278'] = func_12278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11952_call = mod.get_global_var('func_11952')
func_11954_call = mutated_mod.get_global_var('func_11954')
call_12353 = relay.TupleGetItem(func_11952_call(), 0)
call_12354 = relay.TupleGetItem(func_11954_call(), 0)
func_5980_call = mod.get_global_var('func_5980')
func_5981_call = mutated_mod.get_global_var('func_5981')
call_12355 = relay.TupleGetItem(func_5980_call(), 0)
call_12356 = relay.TupleGetItem(func_5981_call(), 0)
var_12358 = relay.var("var_12358", dtype = "float64", shape = (352, 5))#candidate|12358|(352, 5)|var|float64
bop_12359 = relay.not_equal(call_12355.astype('bool'), relay.reshape(var_12358.astype('bool'), relay.shape_of(call_12355))) # shape=(352, 5)
bop_12362 = relay.not_equal(call_12356.astype('bool'), relay.reshape(var_12358.astype('bool'), relay.shape_of(call_12356))) # shape=(352, 5)
func_10448_call = mod.get_global_var('func_10448')
func_10449_call = mutated_mod.get_global_var('func_10449')
call_12368 = func_10448_call()
call_12369 = func_10448_call()
func_8904_call = mod.get_global_var('func_8904')
func_8906_call = mutated_mod.get_global_var('func_8906')
call_12375 = relay.TupleGetItem(func_8904_call(), 0)
call_12376 = relay.TupleGetItem(func_8906_call(), 0)
uop_12377 = relay.cos(var_12358.astype('float32')) # shape=(352, 5)
func_7128_call = mod.get_global_var('func_7128')
func_7131_call = mutated_mod.get_global_var('func_7131')
var_12382 = relay.var("var_12382", dtype = "bool", shape = (140,))#candidate|12382|(140,)|var|bool
call_12381 = relay.TupleGetItem(func_7128_call(relay.reshape(var_12382.astype('bool'), [140,])), 1)
call_12383 = relay.TupleGetItem(func_7131_call(relay.reshape(var_12382.astype('bool'), [140,])), 1)
func_12124_call = mod.get_global_var('func_12124')
func_12126_call = mutated_mod.get_global_var('func_12126')
call_12397 = relay.TupleGetItem(func_12124_call(), 0)
call_12398 = relay.TupleGetItem(func_12126_call(), 0)
output = relay.Tuple([call_12353,bop_12359,call_12368,call_12375,uop_12377,call_12381,var_12382,call_12397,])
output2 = relay.Tuple([call_12354,bop_12362,call_12369,call_12376,uop_12377,call_12383,var_12382,call_12398,])
func_12402 = relay.Function([var_12358,var_12382,], output)
mod['func_12402'] = func_12402
mod = relay.transform.InferType()(mod)
var_12403 = relay.var("var_12403", dtype = "float64", shape = (352, 5))#candidate|12403|(352, 5)|var|float64
var_12404 = relay.var("var_12404", dtype = "bool", shape = (140,))#candidate|12404|(140,)|var|bool
output = func_12402(var_12403,var_12404,)
func_12405 = relay.Function([var_12403,var_12404,], output)
mutated_mod['func_12405'] = func_12405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4744_call = mod.get_global_var('func_4744')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_12466 = func_4744_call()
call_12467 = func_4744_call()
func_4248_call = mod.get_global_var('func_4248')
func_4250_call = mutated_mod.get_global_var('func_4250')
call_12480 = relay.TupleGetItem(func_4248_call(), 0)
call_12481 = relay.TupleGetItem(func_4250_call(), 0)
uop_12484 = relay.rsqrt(call_12480.astype('float64')) # shape=(352, 1)
uop_12486 = relay.rsqrt(call_12481.astype('float64')) # shape=(352, 1)
bop_12497 = relay.floor_mod(uop_12484.astype('float64'), call_12466.astype('float64')) # shape=(10, 352, 7)
bop_12500 = relay.floor_mod(uop_12486.astype('float64'), call_12467.astype('float64')) # shape=(10, 352, 7)
var_12501 = relay.var("var_12501", dtype = "float64", shape = (10, 352, 7))#candidate|12501|(10, 352, 7)|var|float64
bop_12502 = relay.logical_xor(bop_12497.astype('uint64'), relay.reshape(var_12501.astype('uint64'), relay.shape_of(bop_12497))) # shape=(10, 352, 7)
bop_12505 = relay.logical_xor(bop_12500.astype('uint64'), relay.reshape(var_12501.astype('uint64'), relay.shape_of(bop_12500))) # shape=(10, 352, 7)
func_11377_call = mod.get_global_var('func_11377')
func_11378_call = mutated_mod.get_global_var('func_11378')
call_12511 = relay.TupleGetItem(func_11377_call(), 2)
call_12512 = relay.TupleGetItem(func_11378_call(), 2)
bop_12517 = relay.power(bop_12497.astype('float32'), relay.reshape(var_12501.astype('float32'), relay.shape_of(bop_12497))) # shape=(10, 352, 7)
bop_12520 = relay.power(bop_12500.astype('float32'), relay.reshape(var_12501.astype('float32'), relay.shape_of(bop_12500))) # shape=(10, 352, 7)
func_6731_call = mod.get_global_var('func_6731')
func_6733_call = mutated_mod.get_global_var('func_6733')
call_12522 = relay.TupleGetItem(func_6731_call(), 0)
call_12523 = relay.TupleGetItem(func_6733_call(), 0)
uop_12527 = relay.log10(bop_12497.astype('float32')) # shape=(10, 352, 7)
uop_12529 = relay.log10(bop_12500.astype('float32')) # shape=(10, 352, 7)
output = relay.Tuple([bop_12502,call_12511,bop_12517,call_12522,uop_12527,])
output2 = relay.Tuple([bop_12505,call_12512,bop_12520,call_12523,uop_12529,])
func_12530 = relay.Function([var_12501,], output)
mod['func_12530'] = func_12530
mod = relay.transform.InferType()(mod)
mutated_mod['func_12530'] = func_12530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12531 = relay.var("var_12531", dtype = "float64", shape = (10, 352, 7))#candidate|12531|(10, 352, 7)|var|float64
func_12530_call = mutated_mod.get_global_var('func_12530')
call_12532 = func_12530_call(var_12531)
output = call_12532
func_12533 = relay.Function([var_12531], output)
mutated_mod['func_12533'] = func_12533
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12600 = relay.var("var_12600", dtype = "float64", shape = (10, 7, 13))#candidate|12600|(10, 7, 13)|var|float64
uop_12601 = relay.exp(var_12600.astype('float64')) # shape=(10, 7, 13)
func_11594_call = mod.get_global_var('func_11594')
func_11595_call = mutated_mod.get_global_var('func_11595')
call_12608 = func_11594_call()
call_12609 = func_11594_call()
func_1000_call = mod.get_global_var('func_1000')
func_1002_call = mutated_mod.get_global_var('func_1002')
const_12613 = relay.const([-3.740818,-6.184289,7.047127,-8.957998,1.735979,7.807973,-7.293051,8.574141,-4.147959,4.007150,4.820497,7.594901,0.049001,9.720055,-0.977129,-8.743885,9.675664,-2.538376,0.944989,-3.816145,8.696302,5.245400,-4.139719,1.925565,-5.267585,-1.388371,-7.702620,-1.062299,-2.806925,-1.106513,-8.332955,1.774250,0.265286,-4.311199,-2.090976,2.180257,-2.173334,-5.271520,2.720203,7.095719,-5.361482,0.337645,-7.250037,8.776559,-0.903371,1.430877,-3.540788,-1.568440,-3.016323,-4.196502,5.172572,-0.687132,-1.709241,-3.800291,-2.231940,-3.422529,4.700508,-6.770904,9.174678,-5.568317,9.171413,-1.983831,4.157722,-8.893229,-4.056459,-8.625603,-3.388655,7.964071,8.440364,6.758976,-5.705580,3.592463,7.447729,3.769808,0.448421,-0.939099,2.765858,-0.285503,-7.069967,-5.752519,8.009883,-9.064210,5.924676,3.573039,-2.852520,-1.662051,-9.938493,-1.252423,8.370884,-0.355772,-3.316358,-9.068114,1.516362,-2.030600,5.647158,-7.950189,6.441356,-5.910431,1.870582,-6.357197,-5.874683,-0.306541,-6.576505,4.625985,-6.012075,-9.130975,-2.646577,-6.684523,1.787585,7.522411,9.732328,6.873909,6.458743,6.625789,9.507300,-4.411253,-1.200663,-9.518863,2.246016,3.560130,9.509567,-2.139623,-3.878215,-0.917236,1.883929,-5.007385,0.276022,-3.039530,6.487261,5.616345,3.285320,8.482381,-2.670677,-7.905784,4.126161,6.375091,2.442015,-2.429689,-8.190080,2.427635,0.999852,-2.908427,3.185548,5.709570,-4.708212,-5.583484,-1.259252,-9.218781,6.046242,-8.672037,-1.986495,-0.109131,-5.918315,5.528148,1.903719,-6.851241,-1.964814,9.516112,4.665045,-1.387402,-0.558898,9.601468,-5.172077,8.062561,-4.290392,-6.100799,-9.140029,-5.462613,-4.180304,5.445270,-8.198776,-1.297078,4.615230,6.899404,-6.774387,-6.654459,-9.060583,4.343928,9.997447,-5.919722,-6.789713,-7.225838,2.491279,7.500106,-4.152418,4.297299,8.782154,3.244637,-8.851456,2.915272,2.399049,8.605169,-7.057458,-0.091904,9.385840,7.484203,-1.223319,-3.596249,9.984541,4.649853,6.473197,-1.220665,-6.606598,6.603926,-1.478523,6.244665,-1.718412,5.876146,9.673345,4.953571,5.345688,-2.106137,-2.554819,9.935112,2.080493,-1.261570,-6.980358,3.405518,-3.760713,2.862390,4.488498,-3.654623,2.907941,-0.967186,-6.065166,3.268508,6.477896,0.959344,7.375172,0.903505,6.586252,2.763185,-4.813106,-9.260672,5.908978,-1.670950,-2.960668,-4.308890,-1.418122,-8.267832,-3.284680,-8.344320,5.207654,-7.191121,9.631257,6.753526,2.159339,-9.194233,9.105486,-4.610080,-6.993439,-7.435190,-3.286718,-5.328074,1.894933,5.902400,-5.779266,5.893981,6.879947,-7.573484,1.188115,4.524092,-9.597806,7.387493,-3.287252,-4.790030,-8.018918,4.601452,-3.694274,8.701608,-2.147385,5.604780,7.315808,-2.723155,-7.599827,8.551472,7.424533,-7.186769,-5.071057,5.463121,-4.747489,7.255708,-8.838748,8.729108,-5.266401,8.030520,2.906581,2.761614,7.084687,6.244346,8.914055,-5.411924,0.159354,-1.316646,-3.467747,-8.720771,-0.835251,5.038126,-9.281025,0.886908,3.596452,6.887827,9.374429,0.640773,-4.677307,6.754763,8.388306,-3.827020,-9.920412,-3.126157,3.039564,5.030937,-0.823358,-3.270992,2.166434,0.990529,-0.491928,5.181595,-1.700409,3.996993,4.791753,-2.158120,-7.579975,3.133389,3.372080,1.383540,-5.251228,-4.655309,3.212165,6.400086,-3.428088,6.361768,2.732939,8.186467,-7.714409,3.891901,0.568268,-4.667376,-5.740723,-3.137816,-5.613525,-3.452402,0.303019,9.536695,-2.642901,5.766934,-4.709255,6.399218,-8.948881,9.194185,1.830154,-8.761048,-8.336098,-4.730376,2.248905,-4.012243,-4.425490,-8.885903,-1.984637,-5.584368,8.517767,5.533769,1.505829,4.508543,2.575902,-1.546374,0.762088,1.729250,1.160305,6.055349,5.157246,-8.773644,-3.788751,9.879194,1.485171,0.466895,4.196019,-5.014631,-3.965192,-2.362024,-6.252814,-3.124037,-3.440559,9.853183,-7.673692,-0.182066,-6.678662,6.750681,0.532671,9.944946,8.207341,2.790805,-9.766475,9.930518,-7.835921,-9.279027,-7.383255,-8.158460,0.942660,-9.850644,-0.482637,3.929757,-9.075137,-4.189501,6.349987,-0.246712,-6.588971,9.577842,7.008762,8.976123,4.094220,-7.371571,3.686252,-5.818261,-4.613655,-3.714056,5.549613,0.626962,-2.755390,6.405727,-5.958086,-4.121903,-1.192100,0.020665,-9.033494,6.943749,-0.405744,9.139291,-6.832911,-6.350944,6.734725,-1.931892,-7.763605,-3.985990,1.960496,-5.362817,2.232996,-4.222543,8.499187,2.528318,3.988004,1.533838,-9.553677,8.551730,-2.622464,4.380614,-1.654025,-7.511463,8.879664,6.864151,-7.642371,-2.964242,0.830846,7.067956,-0.012950,-5.725497,1.436808,-7.865174,4.965187,8.422855,5.282055,5.487598,-7.725967,4.824315,-2.643674,-6.542050,-5.879571,-5.650993,7.072505,-8.956874,-2.445240,2.911462,-4.886417,1.349824,9.812057,5.228457,6.943384,-4.177564,-4.910125,1.448537,5.740582,-9.598873,4.119474,9.024396,-1.110665,-4.031273,-5.357714,5.941965,0.314824,-5.999049,5.128282,-4.095107,-5.447341,-7.304121,-3.168797,5.342937,4.914283,0.397613,-2.348382,2.973431,2.398824,7.537001,-8.842217,-4.013216,0.778749,-5.824693,1.092118,6.727928,-9.542609,-3.638324,-4.853996,-9.567270,7.537776,-7.726220,-6.710060,7.382181,8.179792,8.343266,1.308557,-2.866155,6.132772,6.525605,2.119104,-2.927299,-3.249042,-2.872361,6.557025,-4.735418,-5.347400,-6.989893,-5.662728,-0.282087,9.705399,6.896917,-2.692454,3.043083,8.471947,-6.552971,-7.553055,-1.378156,9.671065,6.991077,7.111198,-5.166560,-9.466980,-2.203722,-0.126217,-9.179820,-2.628359,-1.025082,4.855897,-7.704984,-0.666327,0.549568,-6.727653,0.316979,-9.637603,-7.473569,-2.840304,-1.529013,6.697249,0.858685,6.358193,2.129338,-1.541804,-0.960481,-0.626629,-5.864853,4.198042,6.076390,7.722582,-3.537661,1.072565,6.291234,0.449963,-4.979090,-4.043229,-9.617893,0.723465,1.036968,9.239762,-7.416843,8.426894,-8.330468,-0.766748,-8.480151,-7.133155,-0.527270,8.927829,3.393682,2.802975,5.017420,9.505333,9.932285,-5.640985,-9.184146,6.902048,6.007398,0.268159,1.867969,2.841487,9.635814,-4.288295,9.650412,2.043001,-4.418013,-7.664187,-3.755268,5.840401,-7.405651,0.360894,6.875311,0.073094,0.476576,-1.080764,9.551675,-4.627630,6.437888,-9.374929,-4.344550,1.761263,-5.031249,-8.708710,-7.913347,-7.365614,2.711520,4.381511,-2.533484,9.102112,-8.886302,9.256025,8.151594,-7.565765,-1.342493,8.093338,8.139126,-0.542214,-2.314301,-6.206999,-5.156485,-4.347677,-3.161683,5.025677,-0.198174,-3.504976,-0.306771,-2.449818,2.352504,6.496253,7.857701,-4.107896,9.554591,-6.274482,-6.327864,-2.150128,-7.731320,-6.345131,6.577751,4.197379,1.835479,-0.217094,2.959038,1.698446,5.392505,2.442190,-2.117286,2.146983,-3.362217,7.206485,5.548123,4.496142,-9.906006,-8.386598,8.478371,-6.699709,-6.061609,0.352041,6.689907,-0.159722,1.490226,-1.225564,-9.256614,4.275408,5.395079,4.734556,2.430878,-2.086433,-4.487311,9.576892,7.872308,-9.388572,-7.263887,4.439287,8.847534,-6.226751,3.657845,-6.315918,8.643065,-9.689480,-2.043297,0.231826,2.695823,-7.476909,-3.077698,4.453498,1.690547,0.660978,6.530326,6.311275,2.437702,5.186496,-9.109821,-0.424951,-9.206040,7.522920,-2.029148,-8.117707,-8.836326,2.608375,-8.173496,-2.301615,6.438750,9.409442,7.189859,2.278516,-1.268045,5.842065,-2.617445,-1.227277,9.401749,2.225228,-0.691221,8.059502,-0.312637,-3.054310,7.888572,-0.468539,-7.591948,-2.253617,3.006966,-5.927528,-0.927811,-8.907187,5.803731,1.913437,-9.518814,-0.896851,-4.561655,-6.357112,2.249209,4.770965,6.812623,9.153162,4.587035,9.229598,8.791248,3.582103,-2.615960,-5.055759,-2.657888,-5.820519,-3.535785,-6.410468,-1.852369,-7.797994,1.017449,-4.737793,9.039651,-4.933837,9.737553,8.455130,-7.035441,7.841442,3.321554,-5.424939,4.381807,-1.645912,-7.154964,7.159483,2.405522,-5.548112,1.453532,-1.809851,-9.301184,-3.814845,-6.547386,-6.604202,-6.952364,8.316551,6.997191,2.174332,-9.206751,-6.731171,-1.508386,9.106454,7.741900,-4.772221,5.499252,-8.258125,-1.170059,0.775615,-5.012717,4.608530,4.759733,-1.856747,-6.704644,-7.417436,-8.538896,9.492996,-7.244501,-0.122551,-3.923065,-0.951587,0.917954,2.159751,5.200159,7.677073,-2.489268,-2.380644,4.331219,-0.685661,0.683885,4.646319,-8.273963,-8.399955,5.116918,-6.276069,-5.819127,7.638579,7.546773,0.435647,-1.062905,3.332312,3.419252,-6.308821,-8.570747,-9.069929,9.660387,9.417766,0.274108,-6.314804,3.783550,-1.918696,-8.480475,1.071767,6.205079,-8.729075,7.621017,-9.760438,-6.180977,-7.723783,-7.006235,-8.259978,-4.705246,4.757633,9.313743,-3.920775,-2.216411,-5.673593,9.420453,8.902657,-0.122829,-0.450477,7.306219,-5.303525,7.562691,-9.793052,-6.393665,-0.207135,0.926712,-8.387091,5.898197,6.988499,4.644652,-3.714687,5.931464,0.204556,-8.312834,-7.209116,0.790795,4.489247,2.102131,-3.888883,-5.340292,-0.307210,-1.509733,-5.224152,6.205081,3.772128,-8.794043,3.610961,1.064684,4.714350,-9.288654,5.971181,7.989455,6.096557,2.822314,-0.709645,-1.412838,2.608857,0.365567,-1.557959,7.777030,9.371923,-0.192459,9.913990,-0.264912,2.231113,-2.115097,-2.184519,3.593172,-9.254425,6.634861,-7.077202,2.882220,-8.512642,7.298815,-7.378584,-1.863343,-8.814044,-2.084150,2.697864,1.114839,-6.153453,4.002645,5.480104,-0.989873,1.011660,-8.494292,6.475561,5.045545,-3.900682,-3.936916,4.073514,-1.324202,9.041722,-0.838732,8.181708,1.969521,1.712719,-8.020635,7.524841,5.011787,-4.835219,-1.842459,1.168987,4.503474,6.392042,-3.804361,0.941599,-5.603148,-8.748244,0.951114,-0.013475,5.890453,7.756471,-5.410260,-1.661458,-8.575430,7.074718,-2.298109,-7.354880,-5.563510,8.666440,7.857496,-2.179485,-6.309240,-5.321351,-1.260625,-3.152363,-0.440157,-1.921467,0.910439,-8.032794,9.027277,-5.643015,6.256767,-9.768709,-1.005427,-5.127052,-9.734350,-9.612724,8.108557,-5.335569,6.586164,7.998583,-8.524728,1.808710,-6.015988,2.818837,0.911765,2.556886,2.038931,9.136993,-0.016286,5.588764,-3.377700,8.673695,-6.916215,6.877318,-7.637175,4.147010,-3.343941,-5.120133,3.701313,1.357977,-0.346416,1.936049,-0.331178,1.022233,-8.383665,9.611696,-3.507945,6.591795,-9.710454,7.158264,0.438896,1.965648,5.782732,7.551848,-8.804393,3.073051,6.835529,-6.430993,1.469216,-0.258147,-0.002325,-7.659756,-3.761695,9.466653,9.733267,-7.845451,6.104897,-7.249179,0.212390,2.627421,-0.477101,-7.083964,5.181153,1.206769,3.571070,2.317569,0.411994,-2.251501,6.144979,-8.987075,-1.550461,9.253793,6.601529,-8.875495,1.698784,-5.893627,7.755978,-3.836264,1.276195,5.511004,3.514865,-6.874891,0.879149,8.791327,-5.424812,5.130529,-5.808693,-4.809905,-3.536360,-9.788777,6.485750,-5.866281,-3.592416,5.807174,-6.287552,-4.860164,7.947778,2.039116,0.717811,7.238997,-8.352870,4.967947,-9.731262,-8.335274,-2.257524,-5.850842,5.202551,-1.523651,0.655556,9.850242,8.895745,-4.533191,-7.624988,4.092110,-5.663234,0.242182,1.036582,0.253228,9.859828,-5.423693,-2.813783,5.598987,7.628592,3.782076,8.231658,2.160334,-5.566747,-9.690895,4.732651,6.242006,-7.451884,-8.188372,7.028672,9.114985,-5.672435,-3.032062,0.537759,-3.703721,-7.209599,5.078443,8.486894,-7.364822,-3.276734,-2.992685,-6.086132,1.282919,9.676060,-1.118130,2.089644,8.980209,6.725732,0.136425,1.910257,-8.952886,3.835139,5.591499,-6.045749,7.138005,-9.120676,-1.069475,3.792945,-8.048554,8.795270,6.842926,-6.474030,-3.656105,-8.673770,-6.940764,-1.972651,8.278696,3.917663,-1.563210,-4.217521,-7.170661,0.270187], dtype = "float64")#candidate|12613|(1152,)|const|float64
call_12612 = relay.TupleGetItem(func_1000_call(relay.reshape(const_12613.astype('float64'), [16, 6, 12])), 0)
call_12614 = relay.TupleGetItem(func_1002_call(relay.reshape(const_12613.astype('float64'), [16, 6, 12])), 0)
output = relay.Tuple([uop_12601,call_12608,call_12612,const_12613,])
output2 = relay.Tuple([uop_12601,call_12609,call_12614,const_12613,])
func_12621 = relay.Function([var_12600,], output)
mod['func_12621'] = func_12621
mod = relay.transform.InferType()(mod)
mutated_mod['func_12621'] = func_12621
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12622 = relay.var("var_12622", dtype = "float64", shape = (10, 7, 13))#candidate|12622|(10, 7, 13)|var|float64
func_12621_call = mutated_mod.get_global_var('func_12621')
call_12623 = func_12621_call(var_12622)
output = call_12623
func_12624 = relay.Function([var_12622], output)
mutated_mod['func_12624'] = func_12624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5679_call = mod.get_global_var('func_5679')
func_5680_call = mutated_mod.get_global_var('func_5680')
call_12643 = func_5679_call()
call_12644 = func_5679_call()
func_5550_call = mod.get_global_var('func_5550')
func_5552_call = mutated_mod.get_global_var('func_5552')
call_12689 = relay.TupleGetItem(func_5550_call(), 0)
call_12690 = relay.TupleGetItem(func_5552_call(), 0)
func_10755_call = mod.get_global_var('func_10755')
func_10756_call = mutated_mod.get_global_var('func_10756')
call_12691 = relay.TupleGetItem(func_10755_call(), 2)
call_12692 = relay.TupleGetItem(func_10756_call(), 2)
output = relay.Tuple([call_12643,call_12689,call_12691,])
output2 = relay.Tuple([call_12644,call_12690,call_12692,])
func_12693 = relay.Function([], output)
mod['func_12693'] = func_12693
mod = relay.transform.InferType()(mod)
output = func_12693()
func_12694 = relay.Function([], output)
mutated_mod['func_12694'] = func_12694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3761_call = mod.get_global_var('func_3761')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_12812 = relay.TupleGetItem(func_3761_call(), 0)
call_12813 = relay.TupleGetItem(func_3763_call(), 0)
output = call_12812
output2 = call_12813
func_12815 = relay.Function([], output)
mod['func_12815'] = func_12815
mod = relay.transform.InferType()(mod)
output = func_12815()
func_12816 = relay.Function([], output)
mutated_mod['func_12816'] = func_12816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11141_call = mod.get_global_var('func_11141')
func_11142_call = mutated_mod.get_global_var('func_11142')
call_12823 = func_11141_call()
call_12824 = func_11141_call()
func_9123_call = mod.get_global_var('func_9123')
func_9125_call = mutated_mod.get_global_var('func_9125')
var_12836 = relay.var("var_12836", dtype = "uint16", shape = (48,))#candidate|12836|(48,)|var|uint16
call_12835 = relay.TupleGetItem(func_9123_call(relay.reshape(var_12836.astype('uint16'), [48,])), 2)
call_12837 = relay.TupleGetItem(func_9125_call(relay.reshape(var_12836.astype('uint16'), [48,])), 2)
output = relay.Tuple([call_12823,call_12835,var_12836,])
output2 = relay.Tuple([call_12824,call_12837,var_12836,])
func_12864 = relay.Function([var_12836,], output)
mod['func_12864'] = func_12864
mod = relay.transform.InferType()(mod)
var_12865 = relay.var("var_12865", dtype = "uint16", shape = (48,))#candidate|12865|(48,)|var|uint16
output = func_12864(var_12865)
func_12866 = relay.Function([var_12865], output)
mutated_mod['func_12866'] = func_12866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mod.get_global_var('func_4280')
func_4282_call = mutated_mod.get_global_var('func_4282')
call_12894 = relay.TupleGetItem(func_4280_call(), 0)
call_12895 = relay.TupleGetItem(func_4282_call(), 0)
func_11594_call = mod.get_global_var('func_11594')
func_11595_call = mutated_mod.get_global_var('func_11595')
call_12900 = func_11594_call()
call_12901 = func_11594_call()
output = relay.Tuple([call_12894,call_12900,])
output2 = relay.Tuple([call_12895,call_12901,])
func_12921 = relay.Function([], output)
mod['func_12921'] = func_12921
mod = relay.transform.InferType()(mod)
output = func_12921()
func_12922 = relay.Function([], output)
mutated_mod['func_12922'] = func_12922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11576_call = mod.get_global_var('func_11576')
func_11578_call = mutated_mod.get_global_var('func_11578')
call_12942 = func_11576_call()
call_12943 = func_11576_call()
output = call_12942
output2 = call_12943
func_12951 = relay.Function([], output)
mod['func_12951'] = func_12951
mod = relay.transform.InferType()(mod)
output = func_12951()
func_12952 = relay.Function([], output)
mutated_mod['func_12952'] = func_12952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9305_call = mod.get_global_var('func_9305')
func_9306_call = mutated_mod.get_global_var('func_9306')
call_12953 = relay.TupleGetItem(func_9305_call(), 0)
call_12954 = relay.TupleGetItem(func_9306_call(), 0)
func_9348_call = mod.get_global_var('func_9348')
func_9350_call = mutated_mod.get_global_var('func_9350')
call_12955 = func_9348_call()
call_12956 = func_9348_call()
func_7696_call = mod.get_global_var('func_7696')
func_7701_call = mutated_mod.get_global_var('func_7701')
var_12959 = relay.var("var_12959", dtype = "bool", shape = (140, 1))#candidate|12959|(140, 1)|var|bool
var_12960 = relay.var("var_12960", dtype = "bool", shape = (490,))#candidate|12960|(490,)|var|bool
var_12961 = relay.var("var_12961", dtype = "float64", shape = (88,))#candidate|12961|(88,)|var|float64
var_12962 = relay.var("var_12962", dtype = "int64", shape = (660,))#candidate|12962|(660,)|var|int64
call_12958 = relay.TupleGetItem(func_7696_call(relay.reshape(var_12959.astype('bool'), [140,]), relay.reshape(var_12960.astype('bool'), [49, 10]), relay.reshape(var_12961.astype('float64'), [88,]), relay.reshape(var_12962.astype('int64'), [660,]), ), 4)
call_12963 = relay.TupleGetItem(func_7701_call(relay.reshape(var_12959.astype('bool'), [140,]), relay.reshape(var_12960.astype('bool'), [49, 10]), relay.reshape(var_12961.astype('float64'), [88,]), relay.reshape(var_12962.astype('int64'), [660,]), ), 4)
const_12964 = relay.const([[[9,-8,-9,6,9,-10,-3,-3],[-3,-5,2,-8,6,-2,6,-5],[-1,8,9,1,-5,-6,-7,3],[4,2,-3,-2,4,2,-5,5],[-1,3,8,-8,7,3,3,-4],[4,-2,-4,-8,10,10,-8,-1],[-1,-8,8,-2,-10,-9,-1,-9],[-6,-3,-7,3,-2,3,10,-8],[-8,-10,2,3,6,-4,-2,-1],[-6,-1,5,10,-6,7,9,-1],[-2,5,-2,6,10,-5,5,-3]],[[8,3,7,-1,6,-1,3,-2],[-2,1,-7,3,6,-2,-2,1],[-8,-5,8,7,6,-9,-9,-6],[-9,-6,3,-8,7,-10,-4,1],[7,-4,-4,7,1,2,8,-3],[-4,-5,-10,6,2,8,-8,9],[-7,-8,-6,-4,10,6,-4,5],[2,3,-5,-3,6,7,2,-7],[9,-3,-10,-1,-1,-8,-10,2],[-7,5,-5,-10,-10,3,3,5],[7,8,-3,8,7,-10,3,10]],[[9,1,-4,5,8,-7,9,-2],[10,-4,8,-8,1,4,1,3],[9,-2,-5,-10,6,-3,-1,-1],[-6,3,-8,8,10,3,-8,-9],[-8,-2,1,-7,9,-2,-6,1],[-2,5,5,9,-7,-9,9,-2],[3,4,-7,-9,-1,-9,7,-9],[2,1,7,-7,4,-9,-3,2],[6,8,-6,-2,-1,6,-10,-9],[8,2,-9,2,-4,-6,2,3],[-7,3,-1,2,7,3,2,-10]],[[1,-10,2,4,10,2,-2,-2],[-9,2,-4,-5,-2,-6,8,9],[-7,-10,8,4,-5,-2,3,-4],[2,6,10,-5,-8,9,7,7],[-4,3,-2,9,-3,-2,6,-3],[-4,4,-10,6,-10,-8,-10,2],[-4,5,-2,-3,7,3,3,-4],[5,-1,-9,-5,-10,7,-7,-4],[-6,9,5,-4,1,-10,5,1],[3,7,9,-2,-4,-10,10,6],[-7,3,-8,6,6,4,-1,-1]]], dtype = "uint16")#candidate|12964|(4, 11, 8)|const|uint16
bop_12965 = relay.greater(call_12955.astype('bool'), relay.reshape(const_12964.astype('bool'), relay.shape_of(call_12955))) # shape=(4, 11, 8)
bop_12968 = relay.greater(call_12956.astype('bool'), relay.reshape(const_12964.astype('bool'), relay.shape_of(call_12956))) # shape=(4, 11, 8)
output = relay.Tuple([call_12953,call_12958,var_12959,var_12960,var_12961,var_12962,bop_12965,])
output2 = relay.Tuple([call_12954,call_12963,var_12959,var_12960,var_12961,var_12962,bop_12968,])
F = relay.Function([var_12959,var_12960,var_12961,var_12962,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_12959,var_12960,var_12961,var_12962,], output2)
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
