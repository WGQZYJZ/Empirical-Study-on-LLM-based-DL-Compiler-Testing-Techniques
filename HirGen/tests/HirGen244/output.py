import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_131 = relay.var("var_131", dtype = "float32", shape = (7, 9, 6))#candidate|131|(7, 9, 6)|var|float32
uop_132 = relay.acosh(var_131.astype('float32')) # shape=(7, 9, 6)
output = relay.Tuple([uop_132,])
output2 = relay.Tuple([uop_132,])
func_144 = relay.Function([var_131,], output)
mod['func_144'] = func_144
mod = relay.transform.InferType()(mod)
mutated_mod['func_144'] = func_144
mutated_mod = relay.transform.InferType()(mutated_mod)
var_145 = relay.var("var_145", dtype = "float32", shape = (7, 9, 6))#candidate|145|(7, 9, 6)|var|float32
func_144_call = mutated_mod.get_global_var('func_144')
call_146 = func_144_call(var_145)
output = call_146
func_147 = relay.Function([var_145], output)
mutated_mod['func_147'] = func_147
mutated_mod = relay.transform.InferType()(mutated_mod)
var_175 = relay.var("var_175", dtype = "int64", shape = ())#candidate|175|()|var|int64
var_176 = relay.var("var_176", dtype = "int64", shape = (8, 2, 8))#candidate|176|(8, 2, 8)|var|int64
bop_177 = relay.add(var_175.astype('int64'), var_176.astype('int64')) # shape=(8, 2, 8)
func_144_call = mod.get_global_var('func_144')
func_147_call = mutated_mod.get_global_var('func_147')
var_192 = relay.var("var_192", dtype = "float32", shape = (378,))#candidate|192|(378,)|var|float32
call_191 = relay.TupleGetItem(func_144_call(relay.reshape(var_192.astype('float32'), [7, 9, 6])), 0)
call_193 = relay.TupleGetItem(func_147_call(relay.reshape(var_192.astype('float32'), [7, 9, 6])), 0)
const_215 = relay.const([-4.486850,2.563462,4.401701,2.033345,-1.158465,5.440698,-5.653959,0.844989,-2.387548,4.798679,-5.895149,-4.605049,3.480837,8.337312,-6.283951,-6.841100,0.053392,-5.765885,-1.011360,1.626332,-2.959705,-6.333225,-5.666378,-5.404445,0.435893,-5.025137,6.823822,7.115755,3.262552,-8.538278,2.415202,-8.814927,-2.372511,3.791411,-4.445296,2.091268,7.578475,7.751243,1.562032,-8.454131,-8.256505,-0.573822,5.725481,-1.385765,2.494742,-2.276563,9.069210,5.300280,0.683823,9.761283,0.551117,-8.862237,-9.898084,-3.521829,-3.991581,-8.232681,0.056947,-4.902547,-7.279533,3.560552,7.870926,-3.378190,8.127129,-0.397276,-5.752668,-2.272072,6.174296,-0.804682,6.001278,6.975260,2.175484,-7.030629,5.806024,6.870451,0.567491,4.893445,-9.054401,4.554428,2.016560,-8.597497,9.943150,1.177180,-9.690585,-7.791782,6.600205,3.781816,-4.962491,4.934722,-6.431640,6.626872,-6.600112,7.611578,7.824933,-1.038325,-8.418540,-1.749567,9.313470,-9.996248,-4.708715,3.089495,5.377237,-3.476172,-3.962307,0.882360,7.592868,-0.540706,0.351190,-3.698027,3.056960,0.131848,-2.392766,2.246957,0.628904,0.113106,5.373786,2.778627,4.234753,-3.728962,-4.016736,-7.950598,-5.367071,3.315847,-6.869803,-1.819086,-8.271003,-0.816292,-2.672421,-4.113720,1.623740,3.175296,5.891471,3.822967,-3.820486,-2.947452,7.725480,-4.550859,-3.871600,0.197946,-2.329090,-1.928804,4.682160,1.000521,-8.077626,-6.647362,6.974474,-1.209501,-9.514971,4.827263,9.549873,8.785482,-7.252417,4.148333,6.973210,-7.030844,-6.597375,-5.901637,1.713425,5.632012,-0.645880,1.568720,2.859437,-6.222473,-7.105476,4.875829,8.180870,-7.382112,-6.501627,-5.953754,0.686653,7.157858,1.184694,2.298878,6.830857,9.109263,-4.949253,6.534738,-1.603197,-9.434317,6.511264,2.459771,-4.454313,7.627405,6.691888,2.255528,-6.484732,-8.197764,-1.648095,-9.221164,0.007775,3.980370,-2.121537,7.189549,-8.762003,3.542584,8.357088,3.121164,7.636065,0.416025,-9.008035,9.022720,0.846746,7.229834,8.775602,-4.246857,9.479374,9.288353,-7.573180,-2.968687,-8.816743,4.863799,-1.582763,0.652686,9.327939,-4.742666,8.582117,-8.850725,-3.065699,0.595771,7.197099,-7.250607,3.876940,-6.738711,-4.340964,2.488315,7.912904,5.654040,9.630371,8.822444,0.056273,-5.184152,3.360745,8.058981,-5.789488,4.528323,-8.927235,-7.735456,9.021965,-5.212315,-9.696988,-9.852733,-4.355293,2.303039,2.406119,-4.360555,6.188810,1.950356,4.981671,-8.314083,7.726362,0.541600,3.366213,-2.351025,-3.700789,-3.533325,-5.146900,-4.172844,-7.814022,-2.694278,-0.375854,-2.486150,2.952077,-9.505120,0.864004,3.153336,5.103444,-0.996863,-1.235363,8.962313,1.321678,5.152602,3.633994,-3.478342,-2.381573,8.905696,8.090875,-0.528603,2.287117,7.501043,7.082392,-4.480741,0.882013,8.199174,8.314812,0.805017,-7.197654,-1.196098,-3.702940,-9.656881,1.238966,-7.335376,7.596848,3.321979,3.091671,9.292354,2.280168,5.827960,9.660025,9.985192,-5.656816,7.261659,2.123825,-6.784396,4.963031,-7.492791,-9.838661,5.902643,6.210642,-1.945031,-9.719254,5.771750,0.123119,-0.921995,2.779639,3.961674,-8.611371,4.452408,-4.687889,-5.849006,-2.353027,-6.968873,5.549219,-7.618832,9.541983,0.891863,1.153348,8.495165,-2.784984,0.830557,7.495448,9.032864,3.543744,-6.653354,-9.396228,7.420308,3.770066,3.393668,-8.134697,-6.475565,-8.983725,5.309737,-7.571172,3.988701,-9.153879,8.419498,9.169279,-5.477464,3.716199,8.083682,9.512694,-5.957463,-4.574145,1.674692,4.712820,-3.645887,9.652254,8.395020,8.981063,-9.108872,4.495985,8.047343,-9.885132,-5.972839,-1.098680,7.044128,-4.456106,4.682656,8.692760,5.663327,-4.411693,6.066348,9.506140,7.716988,1.664701,5.690935,9.228744,9.210566,-4.161788,6.647136], dtype = "float32")#candidate|215|(378,)|const|float32
bop_216 = relay.minimum(var_192.astype('float32'), relay.reshape(const_215.astype('float32'), relay.shape_of(var_192))) # shape=(378,)
bop_221 = relay.greater_equal(var_192.astype('bool'), relay.reshape(const_215.astype('bool'), relay.shape_of(var_192))) # shape=(378,)
func_144_call = mod.get_global_var('func_144')
func_147_call = mutated_mod.get_global_var('func_147')
call_240 = relay.TupleGetItem(func_144_call(relay.reshape(const_215.astype('float32'), [7, 9, 6])), 0)
call_241 = relay.TupleGetItem(func_147_call(relay.reshape(const_215.astype('float32'), [7, 9, 6])), 0)
bop_244 = relay.less(call_240.astype('bool'), var_175.astype('bool')) # shape=(7, 9, 6)
bop_247 = relay.less(call_241.astype('bool'), var_175.astype('bool')) # shape=(7, 9, 6)
var_248 = relay.var("var_248", dtype = "float32", shape = (7, 9, 6))#candidate|248|(7, 9, 6)|var|float32
bop_249 = relay.logical_or(call_240.astype('bool'), relay.reshape(var_248.astype('bool'), relay.shape_of(call_240))) # shape=(7, 9, 6)
bop_252 = relay.logical_or(call_241.astype('bool'), relay.reshape(var_248.astype('bool'), relay.shape_of(call_241))) # shape=(7, 9, 6)
func_144_call = mod.get_global_var('func_144')
func_147_call = mutated_mod.get_global_var('func_147')
call_268 = relay.TupleGetItem(func_144_call(relay.reshape(bop_221.astype('float32'), [7, 9, 6])), 0)
call_269 = relay.TupleGetItem(func_147_call(relay.reshape(bop_221.astype('float32'), [7, 9, 6])), 0)
func_144_call = mod.get_global_var('func_144')
func_147_call = mutated_mod.get_global_var('func_147')
call_289 = relay.TupleGetItem(func_144_call(relay.reshape(var_192.astype('float32'), [7, 9, 6])), 0)
call_290 = relay.TupleGetItem(func_147_call(relay.reshape(var_192.astype('float32'), [7, 9, 6])), 0)
output = relay.Tuple([bop_177,call_191,bop_216,bop_221,bop_244,bop_249,call_268,call_289,])
output2 = relay.Tuple([bop_177,call_193,bop_216,bop_221,bop_247,bop_252,call_269,call_290,])
func_293 = relay.Function([var_175,var_176,var_192,var_248,], output)
mod['func_293'] = func_293
mod = relay.transform.InferType()(mod)
var_294 = relay.var("var_294", dtype = "int64", shape = ())#candidate|294|()|var|int64
var_295 = relay.var("var_295", dtype = "int64", shape = (8, 2, 8))#candidate|295|(8, 2, 8)|var|int64
var_296 = relay.var("var_296", dtype = "float32", shape = (378,))#candidate|296|(378,)|var|float32
var_297 = relay.var("var_297", dtype = "float32", shape = (7, 9, 6))#candidate|297|(7, 9, 6)|var|float32
output = func_293(var_294,var_295,var_296,var_297,)
func_298 = relay.Function([var_294,var_295,var_296,var_297,], output)
mutated_mod['func_298'] = func_298
mutated_mod = relay.transform.InferType()(mutated_mod)
const_339 = relay.const([[[-0.811425,-6.455708,9.862107,-6.891224,4.883563],[-1.711473,-4.559540,-5.757792,6.112772,-4.842631],[9.274863,-0.291813,-6.577249,9.897487,2.528828],[1.823237,-4.281922,-2.785011,-7.409249,-1.436248],[-6.956182,-8.371016,6.839151,-2.400425,-5.041976]],[[-2.583825,2.275217,2.281408,-2.344181,9.501849],[-6.863940,0.684420,4.158050,-2.063564,0.348663],[2.881499,3.225481,-6.367881,-4.162382,2.254841],[2.604127,3.290181,2.928364,8.284512,9.678693],[3.590759,3.238917,-6.767119,4.195286,-9.675616]],[[-4.156675,-2.994705,9.870065,-8.286018,1.724635],[-9.932807,3.456655,-7.962701,0.364509,8.780853],[-1.137294,-1.308664,3.871379,-3.944752,4.989138],[2.980133,0.906354,-9.119602,-3.792642,-0.372119],[-9.913182,9.015103,-1.903510,-8.070651,7.386979]],[[-9.218191,1.824174,3.865257,-4.146170,6.766571],[-4.372216,1.638697,-1.665471,-2.470834,-5.958311],[6.539278,-2.720937,6.524377,-1.116985,-6.682765],[6.715351,3.938440,1.167610,2.625667,7.711869],[5.060771,-5.551567,8.272224,-4.085139,2.915163]],[[-5.266942,-6.692452,5.654860,-9.815771,6.071032],[0.325224,1.188134,1.207269,2.625888,-5.537885],[7.957316,-6.158756,-4.316998,1.275692,-5.916188],[-5.627199,5.873235,3.398552,-2.042983,-3.911396],[-5.341925,-4.914448,-1.684275,-7.216920,-8.870065]],[[-0.578996,-5.955061,2.801057,-1.399678,-6.466783],[-0.954318,-5.500722,1.941433,-6.264475,2.990437],[2.935856,7.000797,5.325505,-7.003526,0.170781],[9.870921,-6.273235,7.883204,-8.519765,-2.437623],[-4.605826,4.590655,-9.303825,-1.792958,-9.177644]],[[7.381038,9.096339,9.048268,6.834916,-7.078327],[5.312068,-7.053761,4.785699,8.781123,-2.092374],[-2.409007,-5.448035,6.719775,-2.212286,-6.432985],[5.261572,6.324798,-6.200029,5.908159,-0.548598],[-1.801058,6.878739,8.977463,-0.791491,6.290708]],[[2.106518,6.846119,4.010472,-8.332813,-8.224633],[4.595313,1.205259,-9.078732,5.305739,5.771010],[8.749358,5.734761,-9.737237,-4.385172,-1.989786],[0.890691,3.211572,4.861967,8.850781,2.062582],[-4.353623,5.643893,9.914503,8.203344,-0.891535]],[[-6.937283,1.583909,-8.719015,-6.799725,-1.000082],[-2.150342,-3.683992,0.950332,6.433725,-2.591165],[-1.570174,0.407304,-0.933056,-8.233334,3.062563],[-8.152297,-5.834996,-9.024455,6.868668,5.216108],[8.466659,-0.116137,-9.376848,8.641669,-2.534416]],[[-7.226584,2.311133,3.925285,-2.028918,9.643565],[-8.934544,3.151235,1.122802,9.338368,-7.418547],[0.603069,5.579555,-3.866937,9.511411,7.529308],[8.393019,-2.696634,2.014793,-8.266077,9.615193],[4.263661,2.578245,4.829153,-4.728542,9.728709]]], dtype = "float64")#candidate|339|(10, 5, 5)|const|float64
var_340 = relay.var("var_340", dtype = "float64", shape = (10, 5, 5))#candidate|340|(10, 5, 5)|var|float64
bop_341 = relay.power(const_339.astype('float64'), relay.reshape(var_340.astype('float64'), relay.shape_of(const_339))) # shape=(10, 5, 5)
func_144_call = mod.get_global_var('func_144')
func_147_call = mutated_mod.get_global_var('func_147')
const_349 = relay.const([-9.357100,-1.954775,-9.907663,-0.627077,-2.829134,9.168108,-5.710441,-9.117334,0.266767,-7.386463,-2.041532,1.340544,5.047757,-4.522492,0.516333,-2.862430,-9.828497,9.993476,-4.091160,6.331853,-2.619417,-8.442081,-7.850611,7.323937,2.268044,-7.785990,-1.881746,4.080162,-7.496715,7.184024,-2.038836,8.443432,-4.418057,9.636821,-1.742635,2.432994,8.633642,-8.135698,-0.690839,3.852109,2.691254,4.964756,3.675005,1.027022,4.300793,0.258065,-7.578453,-5.646720,-8.430916,5.413991,-5.303965,0.134563,-3.316164,-3.110285,-8.287089,-2.957718,3.470770,0.378060,1.753671,1.685027,6.278934,-1.372898,5.828960,-8.120057,-2.920499,8.412970,-9.184557,-3.681356,-5.054911,-9.138319,9.786532,-8.528147,-7.586052,1.695177,-6.663401,-5.918868,-3.693006,4.273255,1.152688,6.471184,0.840173,3.860617,4.050028,-8.069998,-1.625246,-8.252802,-1.587163,-7.933733,2.595708,-8.788574,-0.278853,9.453824,5.515984,2.299805,5.019203,-4.463489,5.173151,-9.460556,5.579230,-2.137549,3.119643,6.228041,1.057684,6.194200,-9.776080,-6.405654,-4.866933,4.963402,-2.208475,6.903551,8.934267,-9.632762,1.066892,7.975276,0.218458,-4.013962,4.409339,-3.953224,4.567646,1.313075,4.126771,8.769814,6.545789,8.206588,2.103882,8.650301,-5.329225,5.645256,9.613992,9.590936,-6.957020,5.640470,9.196686,-2.257407,3.296733,-6.848603,7.167593,8.356338,-5.612137,-0.865162,4.361185,-6.884598,0.571898,9.096836,7.009756,8.366653,-9.593556,2.544155,4.628294,-5.013669,6.603997,3.035038,-6.308586,7.220391,-5.221821,-1.416007,-3.269216,0.731580,-2.557689,-0.344530,5.085073,2.758670,-5.072708,-8.043338,-8.919694,7.442039,9.107858,-5.042223,2.465805,0.979964,2.048677,2.338037,-8.849238,3.505010,8.144290,-5.046110,-9.740272,-2.334606,-4.871837,-9.445603,5.352693,-7.258949,-5.995671,3.220366,7.150795,7.838848,-5.753880,-8.675652,-7.814766,-7.336523,3.953986,-0.846985,-7.610064,-1.421391,7.062131,-5.578085,-7.633575,-1.055563,8.767413,-3.521050,-9.575782,-8.928291,-5.988127,0.323535,-7.404542,-0.989930,2.256436,1.937987,2.919452,-7.362868,-9.068934,-3.557910,-7.746449,-3.127972,-4.554264,-7.521542,-4.221942,7.298467,6.530054,4.955274,-1.068515,2.525543,0.250155,-8.255197,-2.068514,4.608600,9.078765,-4.020098,-4.586109,7.522318,1.596182,3.237901,-4.837692,9.532205,-1.910324,-7.611665,-1.217705,-0.313111,-7.863939,8.770187,9.277623,-8.126965,-2.688058,-4.246834,5.608094,1.461087,7.741300,-2.823359,1.710469,0.990973,5.323304,3.851251,5.663494,5.255605,-0.816761,6.584230,9.114777,-3.738422,-6.164058,9.471973,-9.936832,-6.828923,2.724986,-0.370445,-7.443478,-1.602897,7.608294,-6.056108,5.040500,-9.858635,-3.651738,-1.242879,8.478776,1.152548,1.936954,9.748761,5.310605,-9.818720,6.044109,8.815601,-9.678714,6.117658,3.932650,0.144614,4.613624,-4.354132,8.610262,3.069092,4.701151,-8.136720,0.386643,3.014737,6.071120,-2.402817,-0.788924,5.791125,2.745758,-3.656701,-3.764740,-4.606917,8.344522,6.451327,5.791699,-4.250951,7.036207,2.453936,-5.519870,0.744675,-4.908357,-2.998463,7.166498,-1.966155,-2.239064,-4.684393,-3.319015,-0.725428,6.231408,-2.072389,4.072323,-6.120835,1.749172,7.596894,-6.536115,4.339975,-3.075032,3.316876,7.639515,7.079956,-6.200753,-5.907599,-1.861748,-9.546625,-9.529607,-7.825835,1.251480,-6.230562,-7.064291,7.337909,-8.431628,-5.084396,-4.823802,1.847175,6.772565,-5.336100,-2.195672,-8.435429,2.026667,-2.612815,3.037936,9.257549,6.069256,7.135970,-5.839354,-7.116411,0.805849,8.983306,-5.016259,-6.649580,3.391437,4.256590,7.796983,-2.129141,8.547531,0.810342,2.840467,5.476860,-3.039397,8.190252,6.238410,-0.279552,-6.493825,6.682232,-2.194450,-5.199027,-4.155668,2.175881,0.641510,-4.117518], dtype = "float32")#candidate|349|(378,)|const|float32
call_348 = relay.TupleGetItem(func_144_call(relay.reshape(const_349.astype('float32'), [7, 9, 6])), 0)
call_350 = relay.TupleGetItem(func_147_call(relay.reshape(const_349.astype('float32'), [7, 9, 6])), 0)
func_144_call = mod.get_global_var('func_144')
func_147_call = mutated_mod.get_global_var('func_147')
call_357 = relay.TupleGetItem(func_144_call(relay.reshape(call_348.astype('float32'), [7, 9, 6])), 0)
call_358 = relay.TupleGetItem(func_147_call(relay.reshape(call_348.astype('float32'), [7, 9, 6])), 0)
func_293_call = mod.get_global_var('func_293')
func_298_call = mutated_mod.get_global_var('func_298')
var_364 = relay.var("var_364", dtype = "int64", shape = ())#candidate|364|()|var|int64
var_365 = relay.var("var_365", dtype = "int64", shape = (128,))#candidate|365|(128,)|var|int64
call_363 = relay.TupleGetItem(func_293_call(relay.reshape(var_364.astype('int64'), []), relay.reshape(var_365.astype('int64'), [8, 2, 8]), relay.reshape(const_349.astype('float32'), [378,]), relay.reshape(const_349.astype('float32'), [7, 9, 6]), ), 1)
call_366 = relay.TupleGetItem(func_298_call(relay.reshape(var_364.astype('int64'), []), relay.reshape(var_365.astype('int64'), [8, 2, 8]), relay.reshape(const_349.astype('float32'), [378,]), relay.reshape(const_349.astype('float32'), [7, 9, 6]), ), 1)
func_144_call = mod.get_global_var('func_144')
func_147_call = mutated_mod.get_global_var('func_147')
call_378 = relay.TupleGetItem(func_144_call(relay.reshape(call_363.astype('float32'), [7, 9, 6])), 0)
call_379 = relay.TupleGetItem(func_147_call(relay.reshape(call_363.astype('float32'), [7, 9, 6])), 0)
bop_380 = relay.logical_xor(call_378.astype('int16'), relay.reshape(call_363.astype('int16'), relay.shape_of(call_378))) # shape=(7, 9, 6)
bop_383 = relay.logical_xor(call_379.astype('int16'), relay.reshape(call_366.astype('int16'), relay.shape_of(call_379))) # shape=(7, 9, 6)
uop_386 = relay.sin(bop_341.astype('float64')) # shape=(10, 5, 5)
func_293_call = mod.get_global_var('func_293')
func_298_call = mutated_mod.get_global_var('func_298')
call_392 = relay.TupleGetItem(func_293_call(relay.reshape(var_364.astype('int64'), []), relay.reshape(var_365.astype('int64'), [8, 2, 8]), relay.reshape(call_378.astype('float32'), [378,]), relay.reshape(call_357.astype('float32'), [7, 9, 6]), ), 4)
call_393 = relay.TupleGetItem(func_298_call(relay.reshape(var_364.astype('int64'), []), relay.reshape(var_365.astype('int64'), [8, 2, 8]), relay.reshape(call_378.astype('float32'), [378,]), relay.reshape(call_357.astype('float32'), [7, 9, 6]), ), 4)
output = relay.Tuple([call_348,const_349,call_357,var_364,var_365,bop_380,uop_386,call_392,])
output2 = relay.Tuple([call_350,const_349,call_358,var_364,var_365,bop_383,uop_386,call_393,])
func_395 = relay.Function([var_340,var_364,var_365,], output)
mod['func_395'] = func_395
mod = relay.transform.InferType()(mod)
var_396 = relay.var("var_396", dtype = "float64", shape = (10, 5, 5))#candidate|396|(10, 5, 5)|var|float64
var_397 = relay.var("var_397", dtype = "int64", shape = ())#candidate|397|()|var|int64
var_398 = relay.var("var_398", dtype = "int64", shape = (128,))#candidate|398|(128,)|var|int64
output = func_395(var_396,var_397,var_398,)
func_399 = relay.Function([var_396,var_397,var_398,], output)
mutated_mod['func_399'] = func_399
mutated_mod = relay.transform.InferType()(mutated_mod)
const_503 = relay.const([[[-0.588777,2.734983,3.451252,2.726090,-8.598608,1.418559,-7.068067,-7.317105],[-6.511392,2.456506,-9.687177,1.765427,2.710071,-3.081509,-3.754314,-7.881319],[5.173989,2.971005,9.053126,2.138556,0.360661,-0.692665,-9.378120,-3.740290],[2.508159,-8.707899,-0.738836,-8.139025,-8.359267,2.217548,-1.794194,0.283234],[5.267015,-5.420972,9.153670,5.092708,-6.638536,4.099318,-6.161724,7.080854]],[[2.355881,2.407181,9.932035,-7.322839,-0.889537,5.126268,7.991877,-9.594570],[8.516307,5.755603,-9.419893,-7.055332,0.706817,-9.594017,0.236338,8.212374],[0.924611,-3.640070,-2.909142,-0.599111,-8.094057,-2.180485,7.941196,5.001478],[6.222402,7.659098,9.084320,3.626035,7.940539,-8.935340,9.239863,-4.489409],[5.549246,-0.936053,0.929619,-7.831326,-2.761093,4.215595,-4.584987,-0.148490]]], dtype = "float32")#candidate|503|(2, 5, 8)|const|float32
uop_504 = relay.tan(const_503.astype('float32')) # shape=(2, 5, 8)
output = relay.Tuple([uop_504,])
output2 = relay.Tuple([uop_504,])
func_510 = relay.Function([], output)
mod['func_510'] = func_510
mod = relay.transform.InferType()(mod)
mutated_mod['func_510'] = func_510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_510_call = mutated_mod.get_global_var('func_510')
call_511 = func_510_call()
output = call_511
func_512 = relay.Function([], output)
mutated_mod['func_512'] = func_512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_510_call = mod.get_global_var('func_510')
func_512_call = mutated_mod.get_global_var('func_512')
call_538 = relay.TupleGetItem(func_510_call(), 0)
call_539 = relay.TupleGetItem(func_512_call(), 0)
output = relay.Tuple([call_538,])
output2 = relay.Tuple([call_539,])
func_573 = relay.Function([], output)
mod['func_573'] = func_573
mod = relay.transform.InferType()(mod)
output = func_573()
func_574 = relay.Function([], output)
mutated_mod['func_574'] = func_574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_510_call = mod.get_global_var('func_510')
func_512_call = mutated_mod.get_global_var('func_512')
call_582 = relay.TupleGetItem(func_510_call(), 0)
call_583 = relay.TupleGetItem(func_512_call(), 0)
output = call_582
output2 = call_583
func_587 = relay.Function([], output)
mod['func_587'] = func_587
mod = relay.transform.InferType()(mod)
output = func_587()
func_588 = relay.Function([], output)
mutated_mod['func_588'] = func_588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_592 = func_587_call()
call_593 = func_587_call()
output = relay.Tuple([call_592,])
output2 = relay.Tuple([call_593,])
func_606 = relay.Function([], output)
mod['func_606'] = func_606
mod = relay.transform.InferType()(mod)
mutated_mod['func_606'] = func_606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_606_call = mutated_mod.get_global_var('func_606')
call_607 = func_606_call()
output = call_607
func_608 = relay.Function([], output)
mutated_mod['func_608'] = func_608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_727 = func_587_call()
call_728 = func_587_call()
uop_732 = relay.sinh(call_727.astype('float64')) # shape=(2, 5, 8)
uop_734 = relay.sinh(call_728.astype('float64')) # shape=(2, 5, 8)
output = uop_732
output2 = uop_734
func_747 = relay.Function([], output)
mod['func_747'] = func_747
mod = relay.transform.InferType()(mod)
mutated_mod['func_747'] = func_747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_747_call = mutated_mod.get_global_var('func_747')
call_748 = func_747_call()
output = call_748
func_749 = relay.Function([], output)
mutated_mod['func_749'] = func_749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_774 = func_587_call()
call_775 = func_587_call()
output = call_774
output2 = call_775
func_792 = relay.Function([], output)
mod['func_792'] = func_792
mod = relay.transform.InferType()(mod)
mutated_mod['func_792'] = func_792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_792_call = mutated_mod.get_global_var('func_792')
call_793 = func_792_call()
output = call_793
func_794 = relay.Function([], output)
mutated_mod['func_794'] = func_794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_799 = relay.TupleGetItem(func_573_call(), 0)
call_800 = relay.TupleGetItem(func_574_call(), 0)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_809 = relay.TupleGetItem(func_573_call(), 0)
call_810 = relay.TupleGetItem(func_574_call(), 0)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_815 = relay.TupleGetItem(func_573_call(), 0)
call_816 = relay.TupleGetItem(func_574_call(), 0)
output = relay.Tuple([call_799,call_809,call_815,])
output2 = relay.Tuple([call_800,call_810,call_816,])
func_821 = relay.Function([], output)
mod['func_821'] = func_821
mod = relay.transform.InferType()(mod)
mutated_mod['func_821'] = func_821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_821_call = mutated_mod.get_global_var('func_821')
call_822 = func_821_call()
output = call_822
func_823 = relay.Function([], output)
mutated_mod['func_823'] = func_823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_867 = relay.TupleGetItem(func_606_call(), 0)
call_868 = relay.TupleGetItem(func_608_call(), 0)
func_821_call = mod.get_global_var('func_821')
func_823_call = mutated_mod.get_global_var('func_823')
call_869 = relay.TupleGetItem(func_821_call(), 1)
call_870 = relay.TupleGetItem(func_823_call(), 1)
func_747_call = mod.get_global_var('func_747')
func_749_call = mutated_mod.get_global_var('func_749')
call_907 = func_747_call()
call_908 = func_747_call()
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_910 = func_587_call()
call_911 = func_587_call()
var_919 = relay.var("var_919", dtype = "float32", shape = (2, 5, 8))#candidate|919|(2, 5, 8)|var|float32
bop_920 = relay.floor_divide(call_869.astype('float64'), relay.reshape(var_919.astype('float64'), relay.shape_of(call_869))) # shape=(2, 5, 8)
bop_923 = relay.floor_divide(call_870.astype('float64'), relay.reshape(var_919.astype('float64'), relay.shape_of(call_870))) # shape=(2, 5, 8)
uop_926 = relay.log2(call_907.astype('float32')) # shape=(2, 5, 8)
uop_928 = relay.log2(call_908.astype('float32')) # shape=(2, 5, 8)
func_792_call = mod.get_global_var('func_792')
func_794_call = mutated_mod.get_global_var('func_794')
call_935 = func_792_call()
call_936 = func_792_call()
output = relay.Tuple([call_867,call_910,bop_920,uop_926,call_935,])
output2 = relay.Tuple([call_868,call_911,bop_923,uop_928,call_936,])
func_948 = relay.Function([var_919,], output)
mod['func_948'] = func_948
mod = relay.transform.InferType()(mod)
mutated_mod['func_948'] = func_948
mutated_mod = relay.transform.InferType()(mutated_mod)
var_949 = relay.var("var_949", dtype = "float32", shape = (2, 5, 8))#candidate|949|(2, 5, 8)|var|float32
func_948_call = mutated_mod.get_global_var('func_948')
call_950 = func_948_call(var_949)
output = call_950
func_951 = relay.Function([var_949], output)
mutated_mod['func_951'] = func_951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_747_call = mod.get_global_var('func_747')
func_749_call = mutated_mod.get_global_var('func_749')
call_979 = func_747_call()
call_980 = func_747_call()
var_991 = relay.var("var_991", dtype = "float64", shape = (2, 5, 8))#candidate|991|(2, 5, 8)|var|float64
bop_992 = relay.less_equal(call_979.astype('bool'), relay.reshape(var_991.astype('bool'), relay.shape_of(call_979))) # shape=(2, 5, 8)
bop_995 = relay.less_equal(call_980.astype('bool'), relay.reshape(var_991.astype('bool'), relay.shape_of(call_980))) # shape=(2, 5, 8)
output = relay.Tuple([bop_992,])
output2 = relay.Tuple([bop_995,])
func_1002 = relay.Function([var_991,], output)
mod['func_1002'] = func_1002
mod = relay.transform.InferType()(mod)
var_1003 = relay.var("var_1003", dtype = "float64", shape = (2, 5, 8))#candidate|1003|(2, 5, 8)|var|float64
output = func_1002(var_1003)
func_1004 = relay.Function([var_1003], output)
mutated_mod['func_1004'] = func_1004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_1019 = relay.TupleGetItem(func_606_call(), 0)
call_1020 = relay.TupleGetItem(func_608_call(), 0)
func_821_call = mod.get_global_var('func_821')
func_823_call = mutated_mod.get_global_var('func_823')
call_1032 = relay.TupleGetItem(func_821_call(), 1)
call_1033 = relay.TupleGetItem(func_823_call(), 1)
output = relay.Tuple([call_1019,call_1032,])
output2 = relay.Tuple([call_1020,call_1033,])
func_1041 = relay.Function([], output)
mod['func_1041'] = func_1041
mod = relay.transform.InferType()(mod)
output = func_1041()
func_1042 = relay.Function([], output)
mutated_mod['func_1042'] = func_1042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1041_call = mod.get_global_var('func_1041')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_1067 = relay.TupleGetItem(func_1041_call(), 1)
call_1068 = relay.TupleGetItem(func_1042_call(), 1)
output = call_1067
output2 = call_1068
func_1070 = relay.Function([], output)
mod['func_1070'] = func_1070
mod = relay.transform.InferType()(mod)
output = func_1070()
func_1071 = relay.Function([], output)
mutated_mod['func_1071'] = func_1071
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1076 = relay.var("var_1076", dtype = "float64", shape = (8, 6, 8))#candidate|1076|(8, 6, 8)|var|float64
uop_1077 = relay.acosh(var_1076.astype('float64')) # shape=(8, 6, 8)
func_747_call = mod.get_global_var('func_747')
func_749_call = mutated_mod.get_global_var('func_749')
call_1082 = func_747_call()
call_1083 = func_747_call()
uop_1089 = relay.asin(call_1082.astype('float64')) # shape=(2, 5, 8)
uop_1091 = relay.asin(call_1083.astype('float64')) # shape=(2, 5, 8)
output = relay.Tuple([uop_1077,uop_1089,])
output2 = relay.Tuple([uop_1077,uop_1091,])
func_1093 = relay.Function([var_1076,], output)
mod['func_1093'] = func_1093
mod = relay.transform.InferType()(mod)
mutated_mod['func_1093'] = func_1093
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1094 = relay.var("var_1094", dtype = "float64", shape = (8, 6, 8))#candidate|1094|(8, 6, 8)|var|float64
func_1093_call = mutated_mod.get_global_var('func_1093')
call_1095 = func_1093_call(var_1094)
output = call_1095
func_1096 = relay.Function([var_1094], output)
mutated_mod['func_1096'] = func_1096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1070_call = mod.get_global_var('func_1070')
func_1071_call = mutated_mod.get_global_var('func_1071')
call_1106 = func_1070_call()
call_1107 = func_1070_call()
func_1093_call = mod.get_global_var('func_1093')
func_1096_call = mutated_mod.get_global_var('func_1096')
var_1116 = relay.var("var_1116", dtype = "float64", shape = (384,))#candidate|1116|(384,)|var|float64
call_1115 = relay.TupleGetItem(func_1093_call(relay.reshape(var_1116.astype('float64'), [8, 6, 8])), 1)
call_1117 = relay.TupleGetItem(func_1096_call(relay.reshape(var_1116.astype('float64'), [8, 6, 8])), 1)
output = relay.Tuple([call_1106,call_1115,var_1116,])
output2 = relay.Tuple([call_1107,call_1117,var_1116,])
func_1124 = relay.Function([var_1116,], output)
mod['func_1124'] = func_1124
mod = relay.transform.InferType()(mod)
mutated_mod['func_1124'] = func_1124
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1125 = relay.var("var_1125", dtype = "float64", shape = (384,))#candidate|1125|(384,)|var|float64
func_1124_call = mutated_mod.get_global_var('func_1124')
call_1126 = func_1124_call(var_1125)
output = call_1126
func_1127 = relay.Function([var_1125], output)
mutated_mod['func_1127'] = func_1127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1070_call = mod.get_global_var('func_1070')
func_1071_call = mutated_mod.get_global_var('func_1071')
call_1165 = func_1070_call()
call_1166 = func_1070_call()
output = relay.Tuple([call_1165,])
output2 = relay.Tuple([call_1166,])
func_1169 = relay.Function([], output)
mod['func_1169'] = func_1169
mod = relay.transform.InferType()(mod)
output = func_1169()
func_1170 = relay.Function([], output)
mutated_mod['func_1170'] = func_1170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_1219 = func_587_call()
call_1220 = func_587_call()
var_1235 = relay.var("var_1235", dtype = "float32", shape = (2, 5, 8))#candidate|1235|(2, 5, 8)|var|float32
bop_1236 = relay.not_equal(call_1219.astype('bool'), relay.reshape(var_1235.astype('bool'), relay.shape_of(call_1219))) # shape=(2, 5, 8)
bop_1239 = relay.not_equal(call_1220.astype('bool'), relay.reshape(var_1235.astype('bool'), relay.shape_of(call_1220))) # shape=(2, 5, 8)
output = bop_1236
output2 = bop_1239
func_1242 = relay.Function([var_1235,], output)
mod['func_1242'] = func_1242
mod = relay.transform.InferType()(mod)
var_1243 = relay.var("var_1243", dtype = "float32", shape = (2, 5, 8))#candidate|1243|(2, 5, 8)|var|float32
output = func_1242(var_1243)
func_1244 = relay.Function([var_1243], output)
mutated_mod['func_1244'] = func_1244
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1257 = relay.const([[[8.049506,-7.300917,1.652917,0.965593,-8.243255,0.924237,-4.702376,6.057953,1.216566,-7.669456,5.513720,-9.667745,4.169044,7.824298,7.973595,-5.836446],[-9.493373,7.826982,-0.173547,6.828607,-3.574291,-8.269024,-6.185512,7.001001,0.586551,-8.036931,-5.662333,8.619972,-8.674431,8.263973,6.133154,5.275675],[3.106313,-6.098557,6.515133,-0.349255,-2.147579,-9.919502,-5.305781,-7.134810,6.373332,-4.274532,7.277524,1.938347,-2.544955,4.612059,1.785186,6.640888],[-6.345128,-5.364290,-2.609960,2.879209,5.053945,6.213791,-0.802413,-3.375072,-3.374686,2.744422,-8.870731,-7.317908,-1.565031,-2.848829,-9.844691,-3.479240],[2.425662,-9.535810,9.666284,0.214049,-8.140353,-1.851967,-5.656204,-9.357619,8.049439,0.732511,4.026783,9.351078,0.995340,7.044734,7.746748,-0.895904],[-7.324406,-0.170119,9.032995,7.981190,-4.370649,-2.059760,-6.106347,-3.501615,-2.983624,7.206338,9.560163,9.378207,-9.830365,-7.711869,-9.677710,1.160317],[1.784884,-0.618939,3.554689,-3.688957,2.510676,-2.858024,-4.969269,-6.496888,-3.609411,-4.221875,-1.909770,8.117594,-8.108871,-0.648596,-4.453190,1.990910]],[[-0.125694,-2.864815,5.382712,1.369438,9.510819,-4.821480,-4.209303,0.600182,-9.697082,-4.549764,2.135245,-6.166586,2.830768,0.190055,-0.194713,-0.704288],[-6.096978,-5.359657,0.428657,5.118192,6.545553,-5.143224,-9.675594,9.541500,6.354284,4.097832,3.954042,-5.605031,-7.284358,-3.160392,8.373631,5.918628],[-5.146941,3.684004,-2.929796,-8.848947,5.909382,3.605492,-2.431549,-4.747534,6.715105,7.736623,9.719081,8.252484,1.038080,-6.340099,-5.573374,-5.254050],[4.443554,0.378740,-0.134649,-0.132308,-4.733207,4.960947,-6.142894,6.224897,0.236451,-1.074940,-9.607222,0.644826,5.674750,-7.220976,5.931904,-1.448125],[1.966013,-3.266784,-2.635909,0.630699,1.241850,2.464523,-3.805097,5.486607,6.077147,2.695822,9.982666,9.697733,-4.943386,9.408387,3.324034,4.805731],[6.583383,-6.323980,-5.017363,-6.692487,2.688556,9.499414,-3.263135,8.778881,-2.843199,-2.921981,4.983562,-6.307958,0.643173,-1.395051,-7.224582,6.856492],[5.647527,5.087942,8.471942,3.569056,5.915634,6.769329,4.830071,-9.872854,5.636116,-5.331808,-4.286869,-3.056032,-8.472851,-0.907743,-3.165929,-1.053597]],[[-9.527647,5.898640,4.088697,-0.596112,3.321471,7.462971,-1.790892,-0.344680,-8.263340,4.533847,-5.634880,-1.797067,-8.191077,7.465092,0.270612,-7.317011],[1.762535,3.626047,4.240254,9.566340,2.850609,7.884508,-4.625996,6.495978,-5.873645,-2.328062,1.209910,0.100716,7.916551,-3.842346,-0.896502,-3.984998],[2.643505,8.146936,3.142652,0.308493,6.691584,4.985540,6.858052,-8.590925,4.787828,-3.516186,5.767070,-7.997581,-0.941618,2.960731,1.774130,-2.304531],[-1.507068,1.088592,-8.850610,-2.855436,-3.331921,-1.963099,3.754094,7.828689,9.245562,8.001070,-5.045690,8.917980,-2.357561,3.413799,0.131434,-1.779281],[7.697249,1.016531,7.120621,6.819945,0.672650,8.488529,-1.293802,2.984618,-7.524908,3.532732,-3.069138,4.398638,4.921159,3.807891,-6.728560,-0.954009],[0.225330,9.519693,-8.635006,-1.554497,-6.429127,-2.252439,7.032393,-7.809653,-2.231573,-0.513332,8.104456,4.116740,-3.681101,6.610038,3.160367,2.942451],[9.605748,8.018615,2.696071,-6.457492,4.784844,5.612449,-6.803427,-0.428025,0.018370,-3.453666,-3.408587,9.233041,-9.207649,1.106134,1.232876,-4.491374]],[[5.689183,-2.404910,-8.476310,4.922204,5.138904,-1.347476,-1.265068,-6.872033,1.855604,-2.771625,-8.460543,-1.872640,-1.015522,-7.711731,-0.042772,4.519981],[-6.741111,1.511221,-8.187202,-5.659127,4.878036,0.843371,7.579350,8.327977,-7.730088,-9.461439,0.807827,1.267608,-6.049294,0.401698,2.311811,4.639551],[-2.388193,-4.740183,8.222526,-7.208103,2.747406,-2.502943,9.775768,6.214353,-2.565011,9.678539,-2.182049,6.980913,-4.138990,-4.007317,4.085935,-4.877837],[-2.898703,-9.311315,5.093770,-7.519285,4.503398,-3.788054,-8.668855,-4.526578,1.977045,-0.549252,3.098022,6.595327,8.075914,0.622441,7.970839,-7.656471],[-3.591918,2.686366,-1.857533,-9.064336,-7.154978,-1.325101,-5.398217,5.425244,-8.578093,5.194031,-9.292110,-0.012499,-4.597286,-5.653646,6.503609,8.473718],[-3.525434,9.472845,-9.255533,-2.572904,-8.779848,4.687738,3.525949,8.470137,8.310469,2.529420,1.578840,6.300923,7.091634,2.993853,-0.992161,-0.208530],[9.762171,5.036382,1.057082,-9.491886,9.530978,-2.383418,4.302411,-3.850077,9.163541,-4.860102,2.676102,-4.840781,3.895620,6.159121,5.003523,-9.296647]]], dtype = "float64")#candidate|1257|(4, 7, 16)|const|float64
uop_1258 = relay.sigmoid(const_1257.astype('float64')) # shape=(4, 7, 16)
uop_1276 = relay.acosh(const_1257.astype('float64')) # shape=(4, 7, 16)
var_1281 = relay.var("var_1281", dtype = "float64", shape = (4, 7, 16))#candidate|1281|(4, 7, 16)|var|float64
bop_1282 = relay.floor_divide(uop_1258.astype('float64'), relay.reshape(var_1281.astype('float64'), relay.shape_of(uop_1258))) # shape=(4, 7, 16)
bop_1300 = relay.mod(bop_1282.astype('float64'), relay.reshape(uop_1276.astype('float64'), relay.shape_of(bop_1282))) # shape=(4, 7, 16)
bop_1307 = relay.logical_and(uop_1276.astype('bool'), relay.reshape(uop_1258.astype('bool'), relay.shape_of(uop_1276))) # shape=(4, 7, 16)
output = relay.Tuple([bop_1300,bop_1307,])
output2 = relay.Tuple([bop_1300,bop_1307,])
func_1319 = relay.Function([var_1281,], output)
mod['func_1319'] = func_1319
mod = relay.transform.InferType()(mod)
mutated_mod['func_1319'] = func_1319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1320 = relay.var("var_1320", dtype = "float64", shape = (4, 7, 16))#candidate|1320|(4, 7, 16)|var|float64
func_1319_call = mutated_mod.get_global_var('func_1319')
call_1321 = func_1319_call(var_1320)
output = call_1321
func_1322 = relay.Function([var_1320], output)
mutated_mod['func_1322'] = func_1322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_747_call = mod.get_global_var('func_747')
func_749_call = mutated_mod.get_global_var('func_749')
call_1334 = func_747_call()
call_1335 = func_747_call()
func_1093_call = mod.get_global_var('func_1093')
func_1096_call = mutated_mod.get_global_var('func_1096')
const_1341 = relay.const([2.735080,-6.579313,-8.815194,-3.599941,0.926773,5.151712,8.014602,-9.588501,9.673381,-6.305264,4.720864,9.320038,-2.064895,2.897302,9.213684,-7.825613,-3.663155,-0.427553,5.973476,-5.129082,7.292519,-5.310025,-6.380829,5.107115,2.831281,-6.353666,1.258766,2.393877,-6.183723,3.325855,8.231899,-0.114882,6.484124,-8.521921,-7.925395,3.667184,-1.766071,-3.301734,-7.812716,-7.654599,6.953341,3.189603,1.052139,-1.003845,0.710058,1.055855,-3.891667,-0.529058,-6.567099,-4.414845,0.330546,8.345073,9.829173,6.301544,0.243306,7.708889,-9.444909,5.629908,4.815901,-6.598846,6.354801,-0.520282,2.196936,5.729360,8.237085,-8.471388,8.076802,2.568027,-4.195141,1.212967,-6.984203,-4.293061,5.846553,-2.149543,-2.984083,3.596192,5.296692,3.830122,8.492594,-1.371228,-4.888594,7.344796,-3.666178,-5.187946,7.969643,-0.858859,7.933294,6.660906,-9.126738,5.517271,-1.436552,5.495589,-5.177751,-6.048033,5.264158,5.206243,-8.305606,-1.493559,9.010347,1.760665,-4.886137,-7.662071,-5.391247,-9.057090,-3.371463,4.075780,-5.544563,-2.533917,8.342845,-1.530532,0.005190,-7.577018,7.608674,8.378158,-0.969060,3.180610,-6.288869,-1.839654,6.269832,-9.516734,-7.741670,-8.219790,-2.982934,-0.575679,-0.018838,-5.739912,-2.417319,4.784464,2.204161,-4.283051,9.383497,-7.330005,4.315095,-0.837425,4.993161,-5.576229,4.869070,5.680585,3.772153,2.476905,-6.284239,-4.829323,0.920097,-2.634641,-8.872183,-9.795251,9.716051,2.063246,0.199133,6.950422,-3.453282,-3.976237,0.372703,5.156336,1.958550,-6.399869,5.346268,-9.238556,-0.274936,9.555567,2.863421,-1.376100,3.756613,-9.193525,0.357675,6.461570,4.905674,1.662396,7.448232,-2.580115,-3.069561,2.880256,9.696038,-0.977929,-7.663881,-5.853238,1.964955,-4.374753,-5.893420,3.006811,8.168742,-1.635043,-5.799555,6.636747,-9.420853,0.638384,-0.036089,-1.967230,-9.625259,2.898074,5.120631,0.374181,-0.254168,1.306481,-9.778065,-1.436202,1.404532,-6.244085,9.308178,-2.415092,0.076273,-5.724109,-6.080945,8.153338,2.446642,8.227623,-8.783607,6.670874,6.680901,-1.440385,9.839747,7.428366,9.104195,-1.618256,1.762920,-0.841580,-8.398714,-6.133155,-2.300991,-4.730457,-3.689413,-2.431082,-7.213427,5.536834,-8.428177,2.707979,-1.763537,-6.571456,-4.260462,-0.345950,6.144090,7.095075,4.835300,-1.187582,9.915036,3.620380,9.831972,4.603483,6.074898,4.656930,-2.029347,4.749770,2.311492,-2.525872,7.725110,2.247321,7.382630,-3.802201,-7.759263,-5.104052,8.888678,4.708230,5.979514,-1.776450,2.057680,-4.230160,-8.320284,-7.359883,-1.251366,-2.807352,-9.574294,-6.146234,-0.059537,-6.310702,-4.650181,-8.575293,9.892687,-6.648284,-3.851620,7.350437,-2.959515,9.745481,-3.764322,-1.917365,-8.594259,-6.379510,-0.184418,3.428291,4.139459,8.755286,-0.397286,-5.274303,1.087604,1.516701,2.766255,5.027044,-3.041111,9.375129,-6.826227,5.179224,-5.768998,6.448337,2.128869,1.232102,9.581351,-9.911324,-2.877118,7.557449,3.377845,-0.311484,4.350168,-6.132018,-8.784863,-5.493466,5.509685,-5.572359,3.846511,-1.833217,-2.860696,-9.664646,-5.629411,7.022434,7.542278,-3.047987,8.939080,2.698998,-1.594413,8.010585,4.165402,1.856640,8.769172,-1.639060,-8.507330,1.451118,-2.026988,-1.951112,-3.109057,-1.919274,-5.147136,-5.630882,4.094307,-4.315163,2.260734,-1.308627,-4.191217,0.560767,1.725238,-3.392451,-1.334427,-9.688325,5.588592,1.749569,0.201724,5.925032,-7.407735,0.274649,-8.748272,4.497784,5.169245,-5.434422,-5.732679,-7.299412,-2.893803,6.580059,-3.434504,1.561533,-3.233412,-7.113668,-6.311964,1.563684,2.663272,-9.051311,-2.354488,-6.641411,-2.447147,7.677274,-5.601749,-7.488953,8.696423,-1.150667,-6.108966,5.148305,-0.605148,-8.901468,-0.987620,-0.149341,-0.795024,9.725918,-9.331212,7.960771,-7.190834,3.988874,-0.403233,7.859421], dtype = "float64")#candidate|1341|(384,)|const|float64
call_1340 = relay.TupleGetItem(func_1093_call(relay.reshape(const_1341.astype('float64'), [8, 6, 8])), 0)
call_1342 = relay.TupleGetItem(func_1096_call(relay.reshape(const_1341.astype('float64'), [8, 6, 8])), 0)
func_1002_call = mod.get_global_var('func_1002')
func_1004_call = mutated_mod.get_global_var('func_1004')
call_1343 = relay.TupleGetItem(func_1002_call(relay.reshape(call_1334.astype('float64'), [2, 5, 8])), 0)
call_1344 = relay.TupleGetItem(func_1004_call(relay.reshape(call_1334.astype('float64'), [2, 5, 8])), 0)
output = relay.Tuple([call_1334,call_1340,const_1341,call_1343,])
output2 = relay.Tuple([call_1335,call_1342,const_1341,call_1344,])
func_1346 = relay.Function([], output)
mod['func_1346'] = func_1346
mod = relay.transform.InferType()(mod)
output = func_1346()
func_1347 = relay.Function([], output)
mutated_mod['func_1347'] = func_1347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_510_call = mod.get_global_var('func_510')
func_512_call = mutated_mod.get_global_var('func_512')
call_1438 = relay.TupleGetItem(func_510_call(), 0)
call_1439 = relay.TupleGetItem(func_512_call(), 0)
output = call_1438
output2 = call_1439
func_1450 = relay.Function([], output)
mod['func_1450'] = func_1450
mod = relay.transform.InferType()(mod)
mutated_mod['func_1450'] = func_1450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1450_call = mutated_mod.get_global_var('func_1450')
call_1451 = func_1450_call()
output = call_1451
func_1452 = relay.Function([], output)
mutated_mod['func_1452'] = func_1452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1169_call = mod.get_global_var('func_1169')
func_1170_call = mutated_mod.get_global_var('func_1170')
call_1480 = relay.TupleGetItem(func_1169_call(), 0)
call_1481 = relay.TupleGetItem(func_1170_call(), 0)
output = relay.Tuple([call_1480,])
output2 = relay.Tuple([call_1481,])
func_1512 = relay.Function([], output)
mod['func_1512'] = func_1512
mod = relay.transform.InferType()(mod)
mutated_mod['func_1512'] = func_1512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1512_call = mutated_mod.get_global_var('func_1512')
call_1513 = func_1512_call()
output = call_1513
func_1514 = relay.Function([], output)
mutated_mod['func_1514'] = func_1514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_1518 = relay.TupleGetItem(func_573_call(), 0)
call_1519 = relay.TupleGetItem(func_574_call(), 0)
func_948_call = mod.get_global_var('func_948')
func_951_call = mutated_mod.get_global_var('func_951')
call_1520 = relay.TupleGetItem(func_948_call(relay.reshape(call_1518.astype('float32'), [2, 5, 8])), 3)
call_1521 = relay.TupleGetItem(func_951_call(relay.reshape(call_1518.astype('float32'), [2, 5, 8])), 3)
uop_1539 = relay.rsqrt(call_1518.astype('float32')) # shape=(2, 5, 8)
uop_1541 = relay.rsqrt(call_1519.astype('float32')) # shape=(2, 5, 8)
output = relay.Tuple([call_1520,uop_1539,])
output2 = relay.Tuple([call_1521,uop_1541,])
func_1554 = relay.Function([], output)
mod['func_1554'] = func_1554
mod = relay.transform.InferType()(mod)
mutated_mod['func_1554'] = func_1554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1554_call = mutated_mod.get_global_var('func_1554')
call_1555 = func_1554_call()
output = call_1555
func_1556 = relay.Function([], output)
mutated_mod['func_1556'] = func_1556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1512_call = mod.get_global_var('func_1512')
func_1514_call = mutated_mod.get_global_var('func_1514')
call_1604 = relay.TupleGetItem(func_1512_call(), 0)
call_1605 = relay.TupleGetItem(func_1514_call(), 0)
output = call_1604
output2 = call_1605
func_1609 = relay.Function([], output)
mod['func_1609'] = func_1609
mod = relay.transform.InferType()(mod)
output = func_1609()
func_1610 = relay.Function([], output)
mutated_mod['func_1610'] = func_1610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1169_call = mod.get_global_var('func_1169')
func_1170_call = mutated_mod.get_global_var('func_1170')
call_1630 = relay.TupleGetItem(func_1169_call(), 0)
call_1631 = relay.TupleGetItem(func_1170_call(), 0)
output = call_1630
output2 = call_1631
func_1632 = relay.Function([], output)
mod['func_1632'] = func_1632
mod = relay.transform.InferType()(mod)
output = func_1632()
func_1633 = relay.Function([], output)
mutated_mod['func_1633'] = func_1633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_747_call = mod.get_global_var('func_747')
func_749_call = mutated_mod.get_global_var('func_749')
call_1648 = func_747_call()
call_1649 = func_747_call()
output = call_1648
output2 = call_1649
func_1659 = relay.Function([], output)
mod['func_1659'] = func_1659
mod = relay.transform.InferType()(mod)
output = func_1659()
func_1660 = relay.Function([], output)
mutated_mod['func_1660'] = func_1660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_1702 = relay.TupleGetItem(func_573_call(), 0)
call_1703 = relay.TupleGetItem(func_574_call(), 0)
func_1346_call = mod.get_global_var('func_1346')
func_1347_call = mutated_mod.get_global_var('func_1347')
call_1709 = relay.TupleGetItem(func_1346_call(), 1)
call_1710 = relay.TupleGetItem(func_1347_call(), 1)
func_1041_call = mod.get_global_var('func_1041')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_1719 = relay.TupleGetItem(func_1041_call(), 0)
call_1720 = relay.TupleGetItem(func_1042_call(), 0)
output = relay.Tuple([call_1702,call_1709,call_1719,])
output2 = relay.Tuple([call_1703,call_1710,call_1720,])
func_1721 = relay.Function([], output)
mod['func_1721'] = func_1721
mod = relay.transform.InferType()(mod)
output = func_1721()
func_1722 = relay.Function([], output)
mutated_mod['func_1722'] = func_1722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1070_call = mod.get_global_var('func_1070')
func_1071_call = mutated_mod.get_global_var('func_1071')
call_1736 = func_1070_call()
call_1737 = func_1070_call()
output = call_1736
output2 = call_1737
func_1751 = relay.Function([], output)
mod['func_1751'] = func_1751
mod = relay.transform.InferType()(mod)
output = func_1751()
func_1752 = relay.Function([], output)
mutated_mod['func_1752'] = func_1752
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1779 = relay.var("var_1779", dtype = "float32", shape = (5, 10, 11))#candidate|1779|(5, 10, 11)|var|float32
var_1780 = relay.var("var_1780", dtype = "float32", shape = (5, 10, 11))#candidate|1780|(5, 10, 11)|var|float32
bop_1781 = relay.floor_mod(var_1779.astype('float32'), relay.reshape(var_1780.astype('float32'), relay.shape_of(var_1779))) # shape=(5, 10, 11)
bop_1788 = relay.left_shift(var_1780.astype('uint64'), relay.reshape(bop_1781.astype('uint64'), relay.shape_of(var_1780))) # shape=(5, 10, 11)
output = bop_1788
output2 = bop_1788
func_1791 = relay.Function([var_1779,var_1780,], output)
mod['func_1791'] = func_1791
mod = relay.transform.InferType()(mod)
mutated_mod['func_1791'] = func_1791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1791_call = mutated_mod.get_global_var('func_1791')
var_1793 = relay.var("var_1793", dtype = "float32", shape = (5, 10, 11))#candidate|1793|(5, 10, 11)|var|float32
var_1794 = relay.var("var_1794", dtype = "float32", shape = (5, 10, 11))#candidate|1794|(5, 10, 11)|var|float32
call_1792 = func_1791_call(var_1793,var_1794,)
output = call_1792
func_1795 = relay.Function([var_1793,var_1794,], output)
mutated_mod['func_1795'] = func_1795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1659_call = mod.get_global_var('func_1659')
func_1660_call = mutated_mod.get_global_var('func_1660')
call_1806 = func_1659_call()
call_1807 = func_1659_call()
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_1813 = relay.TupleGetItem(func_606_call(), 0)
call_1814 = relay.TupleGetItem(func_608_call(), 0)
func_1751_call = mod.get_global_var('func_1751')
func_1752_call = mutated_mod.get_global_var('func_1752')
call_1828 = func_1751_call()
call_1829 = func_1751_call()
output = relay.Tuple([call_1806,call_1813,call_1828,])
output2 = relay.Tuple([call_1807,call_1814,call_1829,])
func_1830 = relay.Function([], output)
mod['func_1830'] = func_1830
mod = relay.transform.InferType()(mod)
output = func_1830()
func_1831 = relay.Function([], output)
mutated_mod['func_1831'] = func_1831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_792_call = mod.get_global_var('func_792')
func_794_call = mutated_mod.get_global_var('func_794')
call_1867 = func_792_call()
call_1868 = func_792_call()
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_1877 = relay.TupleGetItem(func_606_call(), 0)
call_1878 = relay.TupleGetItem(func_608_call(), 0)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_1884 = relay.TupleGetItem(func_1830_call(), 1)
call_1885 = relay.TupleGetItem(func_1831_call(), 1)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_1889 = relay.TupleGetItem(func_573_call(), 0)
call_1890 = relay.TupleGetItem(func_574_call(), 0)
output = relay.Tuple([call_1867,call_1877,call_1884,call_1889,])
output2 = relay.Tuple([call_1868,call_1878,call_1885,call_1890,])
func_1892 = relay.Function([], output)
mod['func_1892'] = func_1892
mod = relay.transform.InferType()(mod)
output = func_1892()
func_1893 = relay.Function([], output)
mutated_mod['func_1893'] = func_1893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_1902 = func_1632_call()
call_1903 = func_1632_call()
output = relay.Tuple([call_1902,])
output2 = relay.Tuple([call_1903,])
func_1911 = relay.Function([], output)
mod['func_1911'] = func_1911
mod = relay.transform.InferType()(mod)
output = func_1911()
func_1912 = relay.Function([], output)
mutated_mod['func_1912'] = func_1912
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1939 = relay.var("var_1939", dtype = "uint8", shape = (2, 12, 3))#candidate|1939|(2, 12, 3)|var|uint8
var_1940 = relay.var("var_1940", dtype = "uint8", shape = (2, 12, 3))#candidate|1940|(2, 12, 3)|var|uint8
bop_1941 = relay.subtract(var_1939.astype('uint8'), relay.reshape(var_1940.astype('uint8'), relay.shape_of(var_1939))) # shape=(2, 12, 3)
output = bop_1941
output2 = bop_1941
func_1950 = relay.Function([var_1939,var_1940,], output)
mod['func_1950'] = func_1950
mod = relay.transform.InferType()(mod)
mutated_mod['func_1950'] = func_1950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1950_call = mutated_mod.get_global_var('func_1950')
var_1952 = relay.var("var_1952", dtype = "uint8", shape = (2, 12, 3))#candidate|1952|(2, 12, 3)|var|uint8
var_1953 = relay.var("var_1953", dtype = "uint8", shape = (2, 12, 3))#candidate|1953|(2, 12, 3)|var|uint8
call_1951 = func_1950_call(var_1952,var_1953,)
output = call_1951
func_1954 = relay.Function([var_1952,var_1953,], output)
mutated_mod['func_1954'] = func_1954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_2011 = func_1609_call()
call_2012 = func_1609_call()
output = relay.Tuple([call_2011,])
output2 = relay.Tuple([call_2012,])
func_2017 = relay.Function([], output)
mod['func_2017'] = func_2017
mod = relay.transform.InferType()(mod)
output = func_2017()
func_2018 = relay.Function([], output)
mutated_mod['func_2018'] = func_2018
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2041 = relay.const([[[2.856319,5.233178,-4.733190,1.050381,7.936714,-3.352355,-4.885334,6.222262,9.600334,1.320195],[-3.570570,-8.826695,6.026467,-7.966481,8.142862,2.604111,1.900541,-7.072009,-9.840523,-4.831393],[8.309570,3.367735,-8.904101,-6.491570,-9.366379,0.186114,5.796401,-9.548754,2.370808,0.268571],[-8.541187,4.088794,1.437966,1.521452,7.288208,4.319991,-3.311928,-8.002954,3.895458,-7.590144],[1.424330,-4.265605,1.506575,6.643316,6.099845,-9.472225,5.333796,4.546772,3.918276,-8.803083],[9.970023,6.019946,-5.193029,-8.360852,-1.948379,-2.400333,2.784819,9.191997,9.420774,0.316451],[3.389408,-9.107084,1.152819,3.850905,8.587304,-4.770418,5.673677,-9.835116,2.794708,-5.330805],[-1.698497,7.296781,0.240293,-2.617082,3.957832,-5.044503,9.696732,-0.740288,-4.439679,-6.780136],[7.619118,-3.470735,-4.056603,9.753524,-1.873107,-1.034579,-0.561287,-3.070521,-2.708483,-4.288629],[-2.975360,-6.269277,7.703826,-0.273090,-5.300084,2.616475,9.037777,-3.480111,8.387546,-8.475142]],[[9.349397,-2.071071,-8.003768,-7.448779,3.888813,5.612217,5.289730,-6.758045,-1.085070,-4.150192],[9.867224,-9.223665,-5.527220,-3.021054,-8.871194,8.319012,7.848491,9.962759,-8.159908,-4.544135],[-5.555866,0.236928,2.319911,8.481948,-3.299569,-6.436844,2.610375,4.758086,-1.655236,9.153326],[-5.305081,-9.436870,-5.727471,0.752780,6.520417,5.690073,8.598230,9.538593,-0.660444,-8.257757],[1.403066,-2.890822,-4.662720,-8.990211,2.443572,3.936079,-1.841639,-2.987204,-6.318054,7.733007],[9.404187,0.845199,7.176507,-6.296021,1.423237,-9.355212,9.718315,-0.706131,-1.554733,-1.514926],[-7.925405,1.769938,-8.325226,-5.772869,-1.023866,-4.160156,-0.064805,-8.868529,1.873812,3.202694],[-8.318819,9.560474,-6.437123,3.241955,-2.291409,-4.270225,7.721785,5.478009,2.152158,-2.316337],[5.684703,-8.549780,0.466244,2.273558,3.050658,8.023132,-4.414821,1.129971,-2.070379,-1.501975],[9.871261,-1.349374,-3.008805,-8.041764,4.712262,9.237567,8.035398,-2.769341,2.234299,6.449920]],[[-0.269704,-3.114383,7.916438,4.476548,-0.013099,-2.327241,-5.112742,-5.427804,-0.976778,6.525958],[-0.674877,-7.845005,-8.355603,-7.327338,-9.750714,-1.869665,-4.861924,-8.331219,-9.141863,-7.279085],[0.628613,-5.076464,8.304025,-3.271142,9.453207,4.586895,4.862932,-0.496383,-6.246913,7.885294],[-1.291391,1.690444,-3.088028,8.411209,0.367248,5.279792,-8.590467,-5.333766,-6.266346,-4.024332],[-3.257564,3.968940,0.432318,7.820809,-9.392172,1.365302,-8.800024,-1.262128,-2.495542,-3.713493],[1.384514,-3.263324,5.609052,2.381757,1.049575,-4.802317,8.426726,8.999167,6.168442,-2.734696],[5.381218,-0.255922,-2.691170,-0.104547,-1.681429,-7.760027,-1.711055,-3.587424,2.287184,-0.528200],[4.278371,8.105474,-3.078444,1.015570,9.017278,-5.344551,3.049880,2.563983,8.472225,-9.333203],[-0.778501,3.138935,1.242910,-1.061610,7.289129,-9.447726,5.824529,9.610937,-2.378253,7.369052],[-5.659063,6.140230,7.531632,4.985913,-5.612030,-2.885400,-4.379089,-6.582181,5.042473,-4.524869]],[[1.907771,2.269291,-2.643616,-5.435020,-6.370736,9.855255,8.250637,-6.528184,8.730631,9.028961],[-3.968863,-4.058011,9.536567,-2.972219,3.171133,0.569870,2.711948,-5.231690,1.723530,9.996956],[-5.575444,-8.912190,9.835200,-1.874773,-1.474358,-4.500177,-5.896247,6.324596,5.887374,-6.528988],[6.231837,5.407781,6.394904,-8.517155,0.008836,-1.947358,-0.894497,6.553916,1.460372,-1.067715],[-5.350738,-5.640264,6.420664,-3.305394,-8.985413,-7.993258,6.242086,-7.431001,6.893421,2.889982],[-7.905042,-3.653397,0.624349,-7.291010,-8.305842,-5.325745,-2.112180,7.291047,8.719049,-3.680115],[-3.921780,7.444949,8.831907,-5.733332,-4.887213,8.585684,4.953542,-8.203301,3.095692,-4.124901],[2.086004,-5.465617,0.640521,-1.780425,-0.831386,-5.237846,2.263226,-5.744104,-5.443419,1.653576],[-5.799922,7.519649,-6.386938,-0.347510,5.282488,4.182942,-2.455326,-8.864710,6.350643,-9.345750],[6.275459,0.895206,-0.285925,5.801075,-2.503388,7.613528,0.222021,3.783143,-9.250628,-3.540909]]], dtype = "float32")#candidate|2041|(4, 10, 10)|const|float32
uop_2042 = relay.cos(const_2041.astype('float32')) # shape=(4, 10, 10)
output = relay.Tuple([uop_2042,])
output2 = relay.Tuple([uop_2042,])
func_2048 = relay.Function([], output)
mod['func_2048'] = func_2048
mod = relay.transform.InferType()(mod)
mutated_mod['func_2048'] = func_2048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2048_call = mutated_mod.get_global_var('func_2048')
call_2049 = func_2048_call()
output = call_2049
func_2050 = relay.Function([], output)
mutated_mod['func_2050'] = func_2050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1659_call = mod.get_global_var('func_1659')
func_1660_call = mutated_mod.get_global_var('func_1660')
call_2061 = func_1659_call()
call_2062 = func_1659_call()
func_1169_call = mod.get_global_var('func_1169')
func_1170_call = mutated_mod.get_global_var('func_1170')
call_2063 = relay.TupleGetItem(func_1169_call(), 0)
call_2064 = relay.TupleGetItem(func_1170_call(), 0)
var_2072 = relay.var("var_2072", dtype = "float32", shape = (2, 5, 8))#candidate|2072|(2, 5, 8)|var|float32
bop_2073 = relay.divide(call_2063.astype('float32'), relay.reshape(var_2072.astype('float32'), relay.shape_of(call_2063))) # shape=(2, 5, 8)
bop_2076 = relay.divide(call_2064.astype('float32'), relay.reshape(var_2072.astype('float32'), relay.shape_of(call_2064))) # shape=(2, 5, 8)
uop_2086 = relay.sin(var_2072.astype('float64')) # shape=(2, 5, 8)
output = relay.Tuple([call_2061,bop_2073,uop_2086,])
output2 = relay.Tuple([call_2062,bop_2076,uop_2086,])
func_2088 = relay.Function([var_2072,], output)
mod['func_2088'] = func_2088
mod = relay.transform.InferType()(mod)
mutated_mod['func_2088'] = func_2088
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2089 = relay.var("var_2089", dtype = "float32", shape = (2, 5, 8))#candidate|2089|(2, 5, 8)|var|float32
func_2088_call = mutated_mod.get_global_var('func_2088')
call_2090 = func_2088_call(var_2089)
output = call_2090
func_2091 = relay.Function([var_2089], output)
mutated_mod['func_2091'] = func_2091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_792_call = mod.get_global_var('func_792')
func_794_call = mutated_mod.get_global_var('func_794')
call_2093 = func_792_call()
call_2094 = func_792_call()
const_2125 = relay.const([[[-0.350033,9.899073,-0.381498,2.156746,5.593354,6.995895,-3.949856,5.989933],[0.010336,-8.768364,4.382289,7.404268,0.826720,-4.485532,-5.379428,5.105493],[5.811589,0.916706,-0.995007,-4.404825,-0.083592,8.440533,6.360048,-7.630151],[-0.936123,-0.087204,-0.494457,3.707486,-6.068214,-0.001080,-5.229537,0.490128],[-9.742555,4.584130,2.547666,-2.706334,1.036597,-6.036600,-3.602291,2.531485]],[[3.219612,7.506998,-6.106243,4.031515,-0.955579,9.722433,-2.764861,-2.524625],[5.627882,1.104556,5.094773,-2.816499,0.822266,-7.021299,3.877586,-8.537818],[3.818832,-2.392517,7.344898,-2.090809,2.007542,-5.733423,-6.108599,7.711969],[-2.926920,-6.486453,-7.626168,0.674659,0.448249,-9.648948,6.640945,5.451763],[-2.372845,-5.191717,-8.656220,8.096838,8.944010,1.844482,0.682668,2.909492]]], dtype = "float32")#candidate|2125|(2, 5, 8)|const|float32
bop_2126 = relay.greater_equal(call_2093.astype('bool'), relay.reshape(const_2125.astype('bool'), relay.shape_of(call_2093))) # shape=(2, 5, 8)
bop_2129 = relay.greater_equal(call_2094.astype('bool'), relay.reshape(const_2125.astype('bool'), relay.shape_of(call_2094))) # shape=(2, 5, 8)
output = bop_2126
output2 = bop_2129
func_2130 = relay.Function([], output)
mod['func_2130'] = func_2130
mod = relay.transform.InferType()(mod)
mutated_mod['func_2130'] = func_2130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2130_call = mutated_mod.get_global_var('func_2130')
call_2131 = func_2130_call()
output = call_2131
func_2132 = relay.Function([], output)
mutated_mod['func_2132'] = func_2132
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2143 = relay.const([[[5.722697,-5.724436,8.981251,0.947458,-1.148573,8.239712,7.598340,0.549544,-6.833196,5.910069,9.495630,0.160751,2.337323,8.776942],[4.610716,-1.010905,-3.087991,-9.207273,7.250124,-4.743801,0.570962,8.841603,9.954220,1.567328,4.639297,6.114066,-0.862166,2.116443],[-5.028965,4.281251,2.734487,8.396575,0.346037,-3.576392,3.057978,-8.321251,-4.284689,4.136874,-7.213200,-5.113226,4.632910,7.167745],[-2.908460,-4.671177,4.678283,-0.694915,1.018194,7.393013,-4.263083,4.556161,-5.008868,-5.591852,0.307645,-0.417178,-3.818246,7.997388],[2.422395,-2.065377,7.941073,-5.904787,-1.236596,0.453827,-0.846424,-5.829488,-8.700659,-9.749370,-9.467014,-2.903476,9.899123,4.735026],[5.272656,2.696967,7.948419,-5.599423,-5.714273,-7.704596,1.987215,-8.409266,-9.046612,-3.155106,-3.210168,3.680837,8.147492,-1.477875]],[[4.847036,1.030590,-6.873978,7.225558,-1.646198,-3.035527,-0.412051,5.316368,7.595060,-3.471262,9.241697,-9.975053,9.068263,-8.283385],[7.382545,3.895599,-8.726819,8.838073,-3.959011,0.564880,-0.621344,7.122721,-7.513218,4.484488,1.616751,7.402495,-2.003414,-4.860560],[6.280285,1.919374,-4.727920,8.412043,2.220783,6.242806,7.774155,-6.485669,9.954071,4.365559,-3.473397,9.947707,-8.413714,-2.782746],[-6.141897,-8.628040,0.011904,6.048886,3.900886,5.040281,0.161795,-6.493415,3.385253,3.259588,-6.284606,-7.973536,7.791084,-3.389365],[-4.738702,-5.000260,-5.378287,-1.808202,-8.771062,0.145752,5.698839,-4.499947,7.447241,6.080507,2.066199,9.539880,8.567244,2.023650],[1.395881,-6.426260,-2.614378,3.620158,-4.613069,5.838654,2.993995,-6.209364,9.245265,1.047599,0.394842,0.468803,9.923074,-8.777654]],[[-5.381692,0.578196,-1.919885,4.825601,9.639396,9.515329,-2.945649,-1.981404,7.351866,-9.058824,-5.716302,4.532588,1.875042,-3.331060],[-0.366234,1.517029,-5.019549,-3.826942,6.559233,-0.048658,-8.485818,-3.363407,-0.305682,-4.605978,7.826380,-6.385620,1.066243,6.757154],[-6.309470,7.345227,-1.661216,6.027136,-0.023225,0.816235,4.555789,-5.859092,2.045395,-6.323710,7.265170,9.554748,-2.916961,-9.903016],[-2.271943,-7.289928,-3.583852,1.808266,-3.851376,6.933204,-9.422379,-3.872488,-9.782818,-3.575259,0.497765,5.810419,6.971625,0.289137],[-1.567942,6.605025,8.858008,3.838722,-1.768289,7.776330,1.498291,3.291953,4.682159,9.371694,-3.336926,-0.403660,7.563289,-3.641466],[-9.857414,-5.445495,-7.549594,7.009502,7.335844,2.473711,3.965258,-1.629292,7.399231,8.331859,-5.683360,2.665717,-1.831713,-5.060067]],[[6.931697,-7.296682,2.057288,7.960559,0.732207,9.192034,0.002706,-1.409518,9.672980,-3.451901,-3.483906,-9.939055,-6.936958,2.275208],[1.138121,-0.083315,-1.281964,-6.843592,6.127198,4.584433,8.533974,6.140656,0.035412,7.828198,6.061956,-2.096482,7.287503,-9.436871],[-9.824844,-1.408009,4.544205,-4.166975,-8.634588,5.076416,-5.737393,-4.415181,-1.174925,4.144946,4.197231,-9.641182,-7.449473,-1.091770],[3.128633,3.725611,-1.725558,7.984853,4.636161,9.519308,5.892094,8.896348,-9.913479,0.262360,-6.957270,-2.610818,3.458940,-3.145685],[5.015170,-9.445057,5.538076,-6.539860,1.482458,5.842582,-0.100632,-2.653417,-8.695643,2.504970,1.846524,8.780228,7.059551,6.075391],[-1.855047,-3.307670,-3.724601,5.685521,8.070957,1.127595,0.419269,9.929537,-1.012170,4.016325,3.156596,7.883651,9.819340,-8.978980]],[[-2.105136,-6.587159,0.488468,2.391239,0.655854,0.129320,-2.288456,3.322185,-6.499177,8.126743,7.190294,5.537402,-9.305756,8.263606],[9.559347,-5.669844,-3.505276,-3.400615,-0.727739,3.823405,-1.944198,-9.377881,-7.608502,6.086524,-2.224447,3.562234,1.702733,-4.830910],[7.337076,-3.967803,-7.035110,-2.727027,8.093498,-9.519604,-7.961166,0.701844,6.401802,-0.067617,0.220843,-8.420317,-7.492848,2.038893],[-6.736776,1.280839,-0.359504,-6.495403,4.689383,8.921075,0.932340,-1.101551,2.611671,1.959391,7.914703,-2.680081,1.489333,-9.907823],[-8.135044,1.291035,7.375988,-6.415142,-1.577371,-4.969142,-3.645102,-8.059886,-8.796295,3.145063,-5.732246,-8.863281,-3.223709,5.928507],[1.880464,-8.916595,1.052855,-7.296814,-2.638962,-8.343430,2.726360,-9.322997,-0.977216,9.861300,3.844343,9.672926,4.690928,1.708776]],[[-2.824594,5.736893,-4.085372,-4.332195,-6.311643,1.419609,6.722131,4.485318,-6.507842,-3.851860,5.417974,2.181984,8.275757,-7.275782],[-2.898989,-8.392941,-7.944682,-7.785006,7.509956,8.913998,3.121345,0.430446,-3.651192,0.462883,-1.036650,-4.717007,-6.084530,4.149173],[-0.688938,-4.867410,9.080118,3.503610,2.099242,6.783351,-9.061911,-0.550408,5.521181,2.977176,-4.862266,-9.732277,-1.573299,-2.631417],[5.576852,-3.073554,-2.848446,-0.408426,-0.595813,4.499895,-6.428947,-0.488356,5.273718,-5.443812,-1.219249,2.756220,0.819305,-3.172967],[-8.747406,-7.763141,-7.094306,9.057403,2.714036,-0.591912,0.425590,3.313184,-7.328113,0.024289,-5.851897,-5.398452,5.253639,-3.201606],[-0.082247,-4.824490,6.082491,-9.500575,-7.462581,-5.602217,9.825813,0.814202,2.659536,-1.636208,-1.626070,7.004948,-1.600859,-5.250688]],[[9.929574,-8.226740,0.232610,-0.244532,1.051662,-7.059177,-9.472172,8.201495,6.421902,0.555491,-7.095972,8.059743,8.799025,1.312722],[-9.259578,9.378698,-3.950231,9.338700,-5.845382,9.979779,-3.198675,6.938736,-9.196429,3.479883,4.199408,-0.832770,-8.936049,2.450872],[2.082465,7.747668,-1.270725,0.552462,-6.969347,-4.307663,5.869125,-4.211477,2.661102,-5.725036,8.745400,0.169297,-0.175804,-4.502069],[2.294844,-5.180258,-3.131228,7.902122,-5.212187,-7.572233,7.403954,-9.908294,-4.641666,5.516679,-6.464905,3.803680,9.270567,3.416241],[0.071729,-1.026933,5.104293,6.269085,2.468995,-5.727840,9.458960,-8.198339,6.208612,6.784406,-6.092059,6.253103,5.638415,-3.383272],[5.659820,-2.063582,6.225300,-4.920417,-3.015008,-7.148299,-2.203372,4.152023,2.870008,-1.220196,-0.640307,-6.886259,-6.261717,-2.962592]],[[2.679810,-4.609178,-3.354748,0.250705,-1.482921,-3.830682,5.029946,-3.021658,5.096839,8.359524,9.824769,4.884805,-4.941913,-5.780755],[0.580286,-1.137510,9.359601,8.055778,4.473320,2.765438,-7.411826,-4.168390,0.896892,6.807132,6.909861,6.821568,2.734377,-2.976700],[9.036583,-2.730673,9.070431,2.292007,-2.516564,-3.405640,0.025861,3.438088,5.717316,7.798789,-8.639198,7.447973,5.795230,-8.411856],[1.612415,-6.561628,-6.147674,9.838856,3.678009,-4.212567,-8.595628,-1.438208,5.924555,4.914551,9.205531,7.791109,-6.416131,9.200979],[5.859653,-5.768866,2.825962,0.459750,7.997161,0.171119,4.656762,-1.939651,2.926342,7.923910,-7.547970,4.317557,4.786566,3.614777],[-4.242698,-2.951661,5.618285,-2.140234,2.013165,-0.391425,9.791690,-2.793852,8.456753,-2.936159,8.984004,9.246509,-0.385475,9.419231]],[[2.242846,2.379109,-6.842196,-1.880295,-8.344029,-4.103065,-3.985792,9.962840,-9.844404,1.035542,-0.260580,-3.726145,5.995901,-2.214776],[6.534162,-9.988843,-0.975987,-8.273012,7.159841,-1.655549,3.080875,8.268168,1.758668,6.723586,-9.736234,-3.951807,-6.152341,-4.825454],[-7.350270,-8.297969,4.893568,3.551446,-8.642742,-5.749492,-1.011242,-4.931323,5.562331,4.519181,-3.825146,-1.958495,6.033918,0.067732],[-8.429984,-0.334107,-8.164554,-5.286167,2.369737,-1.367991,9.257465,4.144285,8.046967,9.883504,6.022181,-3.149569,-4.796908,6.071370],[3.314655,5.715103,-0.068708,-9.256921,-2.081904,-7.652828,-6.935322,-3.531648,2.541263,4.215319,7.823651,5.613331,-0.878238,-0.612950],[1.438649,-7.166717,-9.538374,-0.337569,9.375919,-4.921030,1.884601,6.253561,8.552462,7.619645,0.836896,5.856323,3.487656,-9.573131]]], dtype = "float64")#candidate|2143|(9, 6, 14)|const|float64
uop_2144 = relay.log(const_2143.astype('float64')) # shape=(9, 6, 14)
func_2048_call = mod.get_global_var('func_2048')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_2147 = relay.TupleGetItem(func_2048_call(), 0)
call_2148 = relay.TupleGetItem(func_2050_call(), 0)
func_948_call = mod.get_global_var('func_948')
func_951_call = mutated_mod.get_global_var('func_951')
const_2162 = relay.const([-2.317730,-5.830075,2.047962,3.090365,-4.786269,0.877310,-7.750452,-6.234878,-6.339451,-3.656512,-8.610044,-9.546128,-6.504402,-0.164260,-3.605730,-9.607961,-9.637506,5.328274,9.463068,1.289014,-2.699432,6.297097,-6.026590,9.823294,-2.612378,-1.428824,-7.218567,8.254610,8.842850,-0.554310,4.730281,-8.088259,-0.880144,-9.861527,9.250900,6.366849,-5.217813,-5.256254,-7.716535,2.702653,7.827998,-2.932409,4.757547,-1.813033,3.025364,-4.266165,4.692423,-0.794506,-9.834952,-6.056360,-5.184238,0.800575,-8.991989,9.708399,-7.613302,-8.232963,-9.903332,9.927154,-7.473144,6.561203,-4.878788,-2.918200,-0.721324,7.042752,1.456915,-2.867107,8.881628,-6.053819,1.768511,5.898956,2.251319,-0.788131,-5.480894,7.120129,9.952227,-4.967690,-3.533516,-8.284137,0.567261,8.927968], dtype = "float32")#candidate|2162|(80,)|const|float32
call_2161 = relay.TupleGetItem(func_948_call(relay.reshape(const_2162.astype('float32'), [2, 5, 8])), 1)
call_2163 = relay.TupleGetItem(func_951_call(relay.reshape(const_2162.astype('float32'), [2, 5, 8])), 1)
output = relay.Tuple([uop_2144,call_2147,call_2161,const_2162,])
output2 = relay.Tuple([uop_2144,call_2148,call_2163,const_2162,])
func_2169 = relay.Function([], output)
mod['func_2169'] = func_2169
mod = relay.transform.InferType()(mod)
output = func_2169()
func_2170 = relay.Function([], output)
mutated_mod['func_2170'] = func_2170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_2271 = func_587_call()
call_2272 = func_587_call()
output = call_2271
output2 = call_2272
func_2280 = relay.Function([], output)
mod['func_2280'] = func_2280
mod = relay.transform.InferType()(mod)
mutated_mod['func_2280'] = func_2280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2280_call = mutated_mod.get_global_var('func_2280')
call_2281 = func_2280_call()
output = call_2281
func_2282 = relay.Function([], output)
mutated_mod['func_2282'] = func_2282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1911_call = mod.get_global_var('func_1911')
func_1912_call = mutated_mod.get_global_var('func_1912')
call_2324 = relay.TupleGetItem(func_1911_call(), 0)
call_2325 = relay.TupleGetItem(func_1912_call(), 0)
output = call_2324
output2 = call_2325
func_2338 = relay.Function([], output)
mod['func_2338'] = func_2338
mod = relay.transform.InferType()(mod)
mutated_mod['func_2338'] = func_2338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2338_call = mutated_mod.get_global_var('func_2338')
call_2339 = func_2338_call()
output = call_2339
func_2340 = relay.Function([], output)
mutated_mod['func_2340'] = func_2340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_2341 = relay.TupleGetItem(func_2017_call(), 0)
call_2342 = relay.TupleGetItem(func_2018_call(), 0)
func_2088_call = mod.get_global_var('func_2088')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_2356 = relay.TupleGetItem(func_2088_call(relay.reshape(call_2341.astype('float32'), [2, 5, 8])), 1)
call_2357 = relay.TupleGetItem(func_2091_call(relay.reshape(call_2341.astype('float32'), [2, 5, 8])), 1)
output = relay.Tuple([call_2341,call_2356,])
output2 = relay.Tuple([call_2342,call_2357,])
func_2365 = relay.Function([], output)
mod['func_2365'] = func_2365
mod = relay.transform.InferType()(mod)
mutated_mod['func_2365'] = func_2365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2365_call = mutated_mod.get_global_var('func_2365')
call_2366 = func_2365_call()
output = call_2366
func_2367 = relay.Function([], output)
mutated_mod['func_2367'] = func_2367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1450_call = mod.get_global_var('func_1450')
func_1452_call = mutated_mod.get_global_var('func_1452')
call_2437 = func_1450_call()
call_2438 = func_1450_call()
func_1002_call = mod.get_global_var('func_1002')
func_1004_call = mutated_mod.get_global_var('func_1004')
call_2444 = relay.TupleGetItem(func_1002_call(relay.reshape(call_2437.astype('float64'), [2, 5, 8])), 0)
call_2445 = relay.TupleGetItem(func_1004_call(relay.reshape(call_2437.astype('float64'), [2, 5, 8])), 0)
func_1659_call = mod.get_global_var('func_1659')
func_1660_call = mutated_mod.get_global_var('func_1660')
call_2448 = func_1659_call()
call_2449 = func_1659_call()
uop_2450 = relay.cosh(call_2437.astype('float32')) # shape=(2, 5, 8)
uop_2452 = relay.cosh(call_2438.astype('float32')) # shape=(2, 5, 8)
uop_2462 = relay.log10(uop_2450.astype('float32')) # shape=(2, 5, 8)
uop_2464 = relay.log10(uop_2452.astype('float32')) # shape=(2, 5, 8)
output = relay.Tuple([call_2444,call_2448,uop_2462,])
output2 = relay.Tuple([call_2445,call_2449,uop_2464,])
func_2467 = relay.Function([], output)
mod['func_2467'] = func_2467
mod = relay.transform.InferType()(mod)
mutated_mod['func_2467'] = func_2467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mutated_mod.get_global_var('func_2467')
call_2468 = func_2467_call()
output = call_2468
func_2469 = relay.Function([], output)
mutated_mod['func_2469'] = func_2469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_2473 = relay.TupleGetItem(func_2467_call(), 1)
call_2474 = relay.TupleGetItem(func_2469_call(), 1)
output = relay.Tuple([call_2473,])
output2 = relay.Tuple([call_2474,])
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
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_2582 = func_587_call()
call_2583 = func_587_call()
func_1124_call = mod.get_global_var('func_1124')
func_1127_call = mutated_mod.get_global_var('func_1127')
var_2595 = relay.var("var_2595", dtype = "float64", shape = (384,))#candidate|2595|(384,)|var|float64
call_2594 = relay.TupleGetItem(func_1124_call(relay.reshape(var_2595.astype('float64'), [384,])), 1)
call_2596 = relay.TupleGetItem(func_1127_call(relay.reshape(var_2595.astype('float64'), [384,])), 1)
output = relay.Tuple([call_2582,call_2594,var_2595,])
output2 = relay.Tuple([call_2583,call_2596,var_2595,])
func_2599 = relay.Function([var_2595,], output)
mod['func_2599'] = func_2599
mod = relay.transform.InferType()(mod)
var_2600 = relay.var("var_2600", dtype = "float64", shape = (384,))#candidate|2600|(384,)|var|float64
output = func_2599(var_2600)
func_2601 = relay.Function([var_2600], output)
mutated_mod['func_2601'] = func_2601
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2620 = relay.var("var_2620", dtype = "float64", shape = (2, 11, 1))#candidate|2620|(2, 11, 1)|var|float64
uop_2621 = relay.acos(var_2620.astype('float64')) # shape=(2, 11, 1)
bop_2628 = relay.right_shift(uop_2621.astype('int64'), relay.reshape(var_2620.astype('int64'), relay.shape_of(uop_2621))) # shape=(2, 11, 1)
output = relay.Tuple([bop_2628,])
output2 = relay.Tuple([bop_2628,])
func_2634 = relay.Function([var_2620,], output)
mod['func_2634'] = func_2634
mod = relay.transform.InferType()(mod)
mutated_mod['func_2634'] = func_2634
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2635 = relay.var("var_2635", dtype = "float64", shape = (2, 11, 1))#candidate|2635|(2, 11, 1)|var|float64
func_2634_call = mutated_mod.get_global_var('func_2634')
call_2636 = func_2634_call(var_2635)
output = call_2636
func_2637 = relay.Function([var_2635], output)
mutated_mod['func_2637'] = func_2637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_2686 = relay.TupleGetItem(func_1830_call(), 1)
call_2687 = relay.TupleGetItem(func_1831_call(), 1)
func_2130_call = mod.get_global_var('func_2130')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_2699 = func_2130_call()
call_2700 = func_2130_call()
func_1512_call = mod.get_global_var('func_1512')
func_1514_call = mutated_mod.get_global_var('func_1514')
call_2715 = relay.TupleGetItem(func_1512_call(), 0)
call_2716 = relay.TupleGetItem(func_1514_call(), 0)
func_1070_call = mod.get_global_var('func_1070')
func_1071_call = mutated_mod.get_global_var('func_1071')
call_2721 = func_1070_call()
call_2722 = func_1070_call()
var_2739 = relay.var("var_2739", dtype = "float32", shape = (2, 5, 8))#candidate|2739|(2, 5, 8)|var|float32
bop_2740 = relay.mod(call_2721.astype('float64'), relay.reshape(var_2739.astype('float64'), relay.shape_of(call_2721))) # shape=(2, 5, 8)
bop_2743 = relay.mod(call_2722.astype('float64'), relay.reshape(var_2739.astype('float64'), relay.shape_of(call_2722))) # shape=(2, 5, 8)
output = relay.Tuple([call_2686,call_2699,call_2715,bop_2740,])
output2 = relay.Tuple([call_2687,call_2700,call_2716,bop_2743,])
func_2751 = relay.Function([var_2739,], output)
mod['func_2751'] = func_2751
mod = relay.transform.InferType()(mod)
mutated_mod['func_2751'] = func_2751
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2752 = relay.var("var_2752", dtype = "float32", shape = (2, 5, 8))#candidate|2752|(2, 5, 8)|var|float32
func_2751_call = mutated_mod.get_global_var('func_2751')
call_2753 = func_2751_call(var_2752)
output = call_2753
func_2754 = relay.Function([var_2752], output)
mutated_mod['func_2754'] = func_2754
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2770 = relay.var("var_2770", dtype = "float32", shape = (4, 14, 14))#candidate|2770|(4, 14, 14)|var|float32
var_2771 = relay.var("var_2771", dtype = "float32", shape = (4, 14, 14))#candidate|2771|(4, 14, 14)|var|float32
bop_2772 = relay.power(var_2770.astype('float32'), relay.reshape(var_2771.astype('float32'), relay.shape_of(var_2770))) # shape=(4, 14, 14)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_2780 = relay.TupleGetItem(func_573_call(), 0)
call_2781 = relay.TupleGetItem(func_574_call(), 0)
bop_2788 = relay.logical_or(bop_2772.astype('bool'), relay.reshape(var_2771.astype('bool'), relay.shape_of(bop_2772))) # shape=(4, 14, 14)
func_395_call = mod.get_global_var('func_395')
func_399_call = mutated_mod.get_global_var('func_399')
const_2810 = relay.const([[-1.003091,-1.488810],[1.078584,-5.690487],[2.728831,5.404303],[4.163764,2.321980],[4.952894,7.123418],[-3.965411,-3.873746],[4.478702,2.214916],[0.204141,-5.599641],[9.822093,5.905393],[-1.668110,-5.784785],[8.387756,2.789847],[-7.865182,-5.136627],[9.197133,6.222985],[8.696654,-8.094805],[0.056842,-6.391461],[5.805108,-5.944905],[2.333283,0.534869],[1.899816,4.888738],[-4.800844,7.012404],[-6.670343,-6.465302],[6.424829,0.134455],[3.432806,3.091383],[9.352934,3.330392],[3.413201,8.917759],[7.592907,-2.931039],[-1.462107,0.528912],[3.277386,9.722879],[9.234580,2.346449],[7.360723,9.073731],[-4.515489,9.994487],[-4.924196,-7.069195],[-5.717812,-6.590573],[0.186099,-5.250014],[-3.186685,-3.633556],[-1.922749,1.890803],[1.856683,-4.809409],[6.797003,7.397052],[6.094490,2.217650],[-7.326684,6.702757],[3.413902,-7.102512],[-2.930676,4.117481],[2.089824,-8.557514],[0.600164,2.896996],[-5.569167,-8.815663],[8.188801,-6.072672],[-3.990859,-1.668962],[8.881329,-4.389872],[8.453629,5.488374],[0.178506,-1.277467],[-6.962807,2.390621],[0.873350,-5.284666],[-5.218242,3.688632],[5.340063,-0.425472],[-9.821737,-7.986137],[-3.061080,-4.888327],[3.849341,-2.416720],[-5.976515,1.232556],[8.741006,2.449625],[8.636680,4.976634],[-3.120843,6.141258],[-0.871107,8.495169],[-7.441939,-7.471190],[-5.716322,-8.904775],[6.816746,7.222637],[-1.605448,-7.225013],[4.565570,-4.576864],[-9.840823,-3.604581],[-3.756228,-7.290803],[-9.891572,8.539476],[1.283125,9.010626],[8.385343,4.929837],[-3.952917,-9.845735],[-6.784962,8.125129],[-9.623924,-6.025304],[5.715208,0.926716],[5.061168,-2.031201],[-6.820526,-9.576390],[3.624543,4.191362],[-6.523889,0.133609],[2.428135,5.008883],[7.304056,5.086078],[-4.858727,-1.417786],[2.006069,4.205375],[6.561018,-1.642306],[-2.797776,1.102505],[-4.985927,-5.755721],[3.784198,-8.365224],[2.509970,-1.857128],[-6.029744,4.316685],[-8.983114,-6.986997],[7.267771,-1.525636],[6.160568,-7.473060],[1.809056,1.600053],[7.195509,-4.245797],[-2.350004,0.850647],[-8.713816,-4.034880],[-1.052352,1.962696],[0.047195,-8.754495],[-4.508398,7.995177],[9.654514,1.062728],[1.365875,-4.302115],[-5.894185,8.183763],[0.213623,-6.714042],[4.835350,-4.923707],[-5.845021,-9.361549],[5.648295,0.443389],[5.597154,3.205051],[-8.468045,4.323988],[-5.570883,-0.345449],[6.250109,8.135925],[6.297716,-3.261464],[-9.103882,-3.091874],[7.657408,-3.839841],[8.856431,-3.241608],[-0.261305,0.429144],[-3.148534,-8.653677],[-9.889977,1.627393],[-3.989259,5.774306],[-5.685721,-6.051562],[-5.746921,-7.459301],[2.355476,1.306473],[-0.728518,0.594942],[1.135875,2.829193],[-6.863893,-8.708799],[1.646119,-9.627537]], dtype = "float64")#candidate|2810|(125, 2)|const|float64
var_2811 = relay.var("var_2811", dtype = "int64", shape = ())#candidate|2811|()|var|int64
const_2812 = relay.const([-7,-9,-2,-9,-5,5,4,7,-7,8,-3,3,1,-3,8,3,4,6,5,10,8,10,-1,6,9,3,-10,1,-4,6,-4,-9,1,2,-3,-5,-2,-3,-5,3,2,5,-2,5,1,-10,-2,-3,6,-8,2,10,-2,8,-9,-1,-5,-4,3,5,-3,-10,3,8,1,-10,1,8,10,-9,7,1,6,-10,-9,2,-9,-6,6,-4,10,-1,-2,4,-6,-1,3,-4,-1,8,9,-9,4,1,-1,-6,-6,2,9,10,-9,8,-4,2,9,3,-2,8,-10,-6,3,2,3,1,-9,7,1,1,8,-1,5,-6,-10,3,-3,-3,-10,-10], dtype = "int64")#candidate|2812|(128,)|const|int64
call_2809 = relay.TupleGetItem(func_395_call(relay.reshape(const_2810.astype('float64'), [10, 5, 5]), relay.reshape(var_2811.astype('int64'), []), relay.reshape(const_2812.astype('int64'), [128,]), ), 5)
call_2813 = relay.TupleGetItem(func_399_call(relay.reshape(const_2810.astype('float64'), [10, 5, 5]), relay.reshape(var_2811.astype('int64'), []), relay.reshape(const_2812.astype('int64'), [128,]), ), 5)
func_1554_call = mod.get_global_var('func_1554')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_2816 = relay.TupleGetItem(func_1554_call(), 1)
call_2817 = relay.TupleGetItem(func_1556_call(), 1)
output = relay.Tuple([call_2780,bop_2788,call_2809,const_2810,var_2811,const_2812,call_2816,])
output2 = relay.Tuple([call_2781,bop_2788,call_2813,const_2810,var_2811,const_2812,call_2817,])
func_2818 = relay.Function([var_2770,var_2771,var_2811,], output)
mod['func_2818'] = func_2818
mod = relay.transform.InferType()(mod)
var_2819 = relay.var("var_2819", dtype = "float32", shape = (4, 14, 14))#candidate|2819|(4, 14, 14)|var|float32
var_2820 = relay.var("var_2820", dtype = "float32", shape = (4, 14, 14))#candidate|2820|(4, 14, 14)|var|float32
var_2821 = relay.var("var_2821", dtype = "int64", shape = ())#candidate|2821|()|var|int64
output = func_2818(var_2819,var_2820,var_2821,)
func_2822 = relay.Function([var_2819,var_2820,var_2821,], output)
mutated_mod['func_2822'] = func_2822
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2827 = relay.const([[[-3,2],[-7,2],[8,-3],[-1,8],[-4,-9],[-10,5],[-4,8],[1,8],[3,4],[8,-6],[-9,-1],[-9,8]],[[-6,2],[-8,1],[-3,-6],[10,-10],[5,5],[-4,-8],[-1,-5],[7,-4],[2,10],[-4,-10],[9,3],[1,6]],[[-9,-9],[-3,-6],[-7,-5],[-6,-7],[6,8],[10,6],[7,1],[-3,6],[-8,-5],[-4,-5],[1,7],[-10,6]],[[4,5],[4,-3],[1,1],[-3,-5],[3,-3],[-10,2],[-10,-1],[-3,-8],[10,9],[7,7],[8,-3],[6,-3]]], dtype = "uint8")#candidate|2827|(4, 12, 2)|const|uint8
var_2828 = relay.var("var_2828", dtype = "uint8", shape = (4, 12, 2))#candidate|2828|(4, 12, 2)|var|uint8
bop_2829 = relay.not_equal(const_2827.astype('bool'), relay.reshape(var_2828.astype('bool'), relay.shape_of(const_2827))) # shape=(4, 12, 2)
output = bop_2829
output2 = bop_2829
func_2832 = relay.Function([var_2828,], output)
mod['func_2832'] = func_2832
mod = relay.transform.InferType()(mod)
var_2833 = relay.var("var_2833", dtype = "uint8", shape = (4, 12, 2))#candidate|2833|(4, 12, 2)|var|uint8
output = func_2832(var_2833)
func_2834 = relay.Function([var_2833], output)
mutated_mod['func_2834'] = func_2834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_747_call = mod.get_global_var('func_747')
func_749_call = mutated_mod.get_global_var('func_749')
call_2851 = func_747_call()
call_2852 = func_747_call()
uop_2858 = relay.cos(call_2851.astype('float64')) # shape=(2, 5, 8)
uop_2860 = relay.cos(call_2852.astype('float64')) # shape=(2, 5, 8)
var_2869 = relay.var("var_2869", dtype = "float64", shape = (2, 5, 8))#candidate|2869|(2, 5, 8)|var|float64
bop_2870 = relay.minimum(call_2851.astype('float64'), relay.reshape(var_2869.astype('float64'), relay.shape_of(call_2851))) # shape=(2, 5, 8)
bop_2873 = relay.minimum(call_2852.astype('float64'), relay.reshape(var_2869.astype('float64'), relay.shape_of(call_2852))) # shape=(2, 5, 8)
bop_2874 = relay.multiply(uop_2858.astype('uint64'), relay.reshape(var_2869.astype('uint64'), relay.shape_of(uop_2858))) # shape=(2, 5, 8)
bop_2877 = relay.multiply(uop_2860.astype('uint64'), relay.reshape(var_2869.astype('uint64'), relay.shape_of(uop_2860))) # shape=(2, 5, 8)
output = relay.Tuple([bop_2870,bop_2874,])
output2 = relay.Tuple([bop_2873,bop_2877,])
func_2885 = relay.Function([var_2869,], output)
mod['func_2885'] = func_2885
mod = relay.transform.InferType()(mod)
mutated_mod['func_2885'] = func_2885
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2886 = relay.var("var_2886", dtype = "float64", shape = (2, 5, 8))#candidate|2886|(2, 5, 8)|var|float64
func_2885_call = mutated_mod.get_global_var('func_2885')
call_2887 = func_2885_call(var_2886)
output = call_2887
func_2888 = relay.Function([var_2886], output)
mutated_mod['func_2888'] = func_2888
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2890 = relay.var("var_2890", dtype = "float32", shape = (16, 12, 16))#candidate|2890|(16, 12, 16)|var|float32
uop_2891 = relay.sigmoid(var_2890.astype('float32')) # shape=(16, 12, 16)
func_792_call = mod.get_global_var('func_792')
func_794_call = mutated_mod.get_global_var('func_794')
call_2893 = func_792_call()
call_2894 = func_792_call()
func_821_call = mod.get_global_var('func_821')
func_823_call = mutated_mod.get_global_var('func_823')
call_2896 = relay.TupleGetItem(func_821_call(), 1)
call_2897 = relay.TupleGetItem(func_823_call(), 1)
func_2599_call = mod.get_global_var('func_2599')
func_2601_call = mutated_mod.get_global_var('func_2601')
var_2899 = relay.var("var_2899", dtype = "float64", shape = (384,))#candidate|2899|(384,)|var|float64
call_2898 = relay.TupleGetItem(func_2599_call(relay.reshape(var_2899.astype('float64'), [384,])), 1)
call_2900 = relay.TupleGetItem(func_2601_call(relay.reshape(var_2899.astype('float64'), [384,])), 1)
func_1791_call = mod.get_global_var('func_1791')
func_1795_call = mutated_mod.get_global_var('func_1795')
var_2920 = relay.var("var_2920", dtype = "float32", shape = (1, 550))#candidate|2920|(1, 550)|var|float32
call_2919 = func_1791_call(relay.reshape(var_2920.astype('float32'), [5, 10, 11]), relay.reshape(var_2920.astype('float32'), [5, 10, 11]), )
call_2921 = func_1791_call(relay.reshape(var_2920.astype('float32'), [5, 10, 11]), relay.reshape(var_2920.astype('float32'), [5, 10, 11]), )
bop_2922 = relay.left_shift(uop_2891.astype('uint8'), relay.reshape(var_2890.astype('uint8'), relay.shape_of(uop_2891))) # shape=(16, 12, 16)
func_1169_call = mod.get_global_var('func_1169')
func_1170_call = mutated_mod.get_global_var('func_1170')
call_2925 = relay.TupleGetItem(func_1169_call(), 0)
call_2926 = relay.TupleGetItem(func_1170_call(), 0)
func_144_call = mod.get_global_var('func_144')
func_147_call = mutated_mod.get_global_var('func_147')
const_2932 = relay.const([4.598822,0.911306,6.513580,-2.922030,4.366922,0.046456,-0.313803,-7.334700,-2.614536,3.234601,1.283258,-6.886095,-9.282502,-4.307592,8.281766,-3.249969,-9.244099,-0.212014,-7.432456,0.962749,7.173681,-6.930664,-8.530315,7.692399,-7.088172,-9.273517,4.292265,-7.744724,-0.602688,-0.549027,-5.039392,-6.394569,-3.823309,-2.293965,6.525980,7.055597,-9.559368,9.915035,-7.439575,4.360789,1.435544,-7.234420,-8.117304,-2.870032,6.662421,8.029437,-9.588206,-7.693498,-5.223820,7.036899,-6.681512,-2.556645,-5.458343,-4.663768,-0.569986,3.005668,1.108989,5.809017,0.634191,-5.230803,-3.482767,-2.696194,-8.485199,8.527717,6.571080,-4.220051,6.615686,-6.175090,-8.371466,-1.940070,-1.450991,9.078287,4.688281,4.527738,-6.432991,8.895729,2.756486,3.962919,-4.141224,-8.000246,3.786012,-6.983720,-7.372714,5.713014,9.727886,7.759231,4.224195,2.942067,1.494117,1.575428,9.876209,-4.455964,-8.276063,-2.938735,6.736153,-2.594993,5.395271,1.059689,8.518520,6.054048,8.203447,-5.153827,7.697886,1.053098,4.662367,-6.861367,-2.909553,1.516447,6.788959,5.487782,1.845361,0.271915,-8.934959,-0.509825,6.241867,-7.871728,-9.250675,-5.484878,1.768388,1.344321,-7.830902,9.328036,-5.224439,-8.497516,-6.367089,-6.384829,2.938761,-8.627232,7.453472,-5.029578,-5.044605,3.967732,8.843419,-1.797025,4.765772,4.308363,-7.070856,-3.722815,-7.781947,-3.750504,6.193862,-1.377904,-7.313019,-7.248886,2.948439,1.784172,-7.671120,-1.361970,-9.511245,-6.812282,-4.891452,3.239684,-9.930647,-3.758427,-1.791803,4.639007,6.146745,1.826758,-6.107508,8.923911,-2.279866,-6.417557,0.117284,-7.172886,0.786626,-2.399204,6.725109,-4.051196,3.381828,-4.922001,8.465462,8.119341,2.131651,5.839167,0.908069,9.405391,8.725832,-8.353719,-6.372351,-1.534029,0.164174,-0.514660,-5.025264,-7.223347,8.200940,-8.019174,-1.073146,7.918611,-9.420625,5.081649,-2.584561,0.007339,-3.889554,-5.391581,-3.423117,6.352306,3.719045,-4.442182,-8.900501,-3.113263,1.057637,5.016319,-4.793795,4.128414,2.713733,-3.639486,8.476964,6.676429,5.293533,7.710295,-6.129780,2.316263,-0.869733,9.506343,-9.652532,-1.425453,-5.110675,7.339801,-1.514569,9.018694,-2.609790,6.083488,4.483703,6.694487,6.938916,9.125523,6.940947,7.234982,-1.147049,6.205603,-1.643463,5.396570,3.439888,-6.210984,5.239053,2.302730,3.809636,-6.701252,6.469293,-3.090479,-9.567764,-2.456304,-0.250344,9.593997,-1.631496,-8.380304,-8.165998,-6.303900,-4.785792,8.865401,-1.545700,8.472803,-0.746206,8.392654,-0.575870,-2.296411,5.536067,-1.511443,-7.249627,-7.016792,-8.802088,-2.709270,-9.392382,-2.799232,0.775650,0.939790,-9.784987,5.670186,-2.522702,-2.095391,-4.493944,6.850719,6.192179,-0.103428,8.843692,6.854557,4.212475,-9.546159,-3.244224,-6.912944,-6.348116,4.793639,3.219240,3.795512,2.239582,-4.982320,-1.247767,0.137270,5.487318,-5.183547,6.249097,3.700868,7.456336,-5.280640,-6.353741,5.180936,-6.523336,-9.231405,9.920326,2.427274,8.562335,2.780942,8.480837,-0.183486,-7.720701,0.691883,-8.074419,-8.753625,-7.455835,7.756365,2.467069,-9.588066,4.652797,6.383112,-6.172604,-3.688197,-7.374341,-0.673233,-2.646161,1.168377,7.960162,-1.528960,6.273908,0.683968,-1.084585,-3.889069,4.686678,3.365980,1.496296,8.973409,-7.053845,-2.254489,3.448515,-0.736302,0.491103,-3.327667,9.043967,-2.138968,6.688274,-0.910559,-5.917607,-1.933354,1.812036,-0.794157,-8.083924,2.136715,6.738665,-9.206089,-6.084335,0.891222,-6.580338,-7.276945,-6.569421,-9.351225,-9.092239,9.317296,0.880991,-7.943925,-4.288008,-7.771372,-6.109216,6.858078,8.822090,3.843566,-8.355506,2.309345,-5.375199,-9.661317,-6.099697,0.567763,-6.324590,3.352854,-2.859735,-5.921396,-6.265006,5.165571,-2.133796,2.817192], dtype = "float32")#candidate|2932|(378,)|const|float32
call_2931 = relay.TupleGetItem(func_144_call(relay.reshape(const_2932.astype('float32'), [7, 9, 6])), 0)
call_2933 = relay.TupleGetItem(func_147_call(relay.reshape(const_2932.astype('float32'), [7, 9, 6])), 0)
output = relay.Tuple([call_2893,call_2896,call_2898,var_2899,call_2919,var_2920,bop_2922,call_2925,call_2931,const_2932,])
output2 = relay.Tuple([call_2894,call_2897,call_2900,var_2899,call_2921,var_2920,bop_2922,call_2926,call_2933,const_2932,])
func_2938 = relay.Function([var_2890,var_2899,var_2920,], output)
mod['func_2938'] = func_2938
mod = relay.transform.InferType()(mod)
mutated_mod['func_2938'] = func_2938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2938_call = mutated_mod.get_global_var('func_2938')
var_2940 = relay.var("var_2940", dtype = "float32", shape = (16, 12, 16))#candidate|2940|(16, 12, 16)|var|float32
var_2941 = relay.var("var_2941", dtype = "float64", shape = (384,))#candidate|2941|(384,)|var|float64
var_2942 = relay.var("var_2942", dtype = "float32", shape = (1, 550))#candidate|2942|(1, 550)|var|float32
call_2939 = func_2938_call(var_2940,var_2941,var_2942,)
output = call_2939
func_2943 = relay.Function([var_2940,var_2941,var_2942,], output)
mutated_mod['func_2943'] = func_2943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1554_call = mod.get_global_var('func_1554')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_2953 = relay.TupleGetItem(func_1554_call(), 1)
call_2954 = relay.TupleGetItem(func_1556_call(), 1)
uop_2968 = relay.sqrt(call_2953.astype('float32')) # shape=(2, 5, 8)
uop_2970 = relay.sqrt(call_2954.astype('float32')) # shape=(2, 5, 8)
func_1070_call = mod.get_global_var('func_1070')
func_1071_call = mutated_mod.get_global_var('func_1071')
call_2974 = func_1070_call()
call_2975 = func_1070_call()
output = relay.Tuple([uop_2968,call_2974,])
output2 = relay.Tuple([uop_2970,call_2975,])
func_2994 = relay.Function([], output)
mod['func_2994'] = func_2994
mod = relay.transform.InferType()(mod)
output = func_2994()
func_2995 = relay.Function([], output)
mutated_mod['func_2995'] = func_2995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_3020 = relay.TupleGetItem(func_606_call(), 0)
call_3021 = relay.TupleGetItem(func_608_call(), 0)
const_3031 = relay.const([[[-2.877559,4.713170,-9.817357,8.144477,6.678053,0.804906,-0.931650,4.899677],[3.144427,-3.410778,5.476480,8.853554,6.058682,-2.994641,9.535410,-5.556310],[1.294958,5.867364,-1.504629,5.769450,7.119447,7.133146,2.279200,1.274912],[-5.927802,-4.162710,9.898934,-8.198546,-6.382051,2.170637,6.761084,2.737788],[2.445081,-8.973046,-1.233752,6.368051,-3.153508,9.684956,2.736986,-2.806328]],[[1.123544,5.722160,7.631559,1.352581,-3.067983,9.958079,-0.590556,0.370838],[-0.525767,6.973793,8.404869,-3.002503,5.322693,5.268379,-4.913773,-5.258775],[-2.368232,-9.542715,-1.234987,9.080550,-0.218679,-7.727419,-5.577171,-6.089658],[5.833399,1.771676,-0.414053,-5.713293,3.253874,-9.050487,-0.179628,9.883418],[-6.238832,-3.386907,5.318214,-0.438478,-8.241158,-5.233223,-4.162920,9.329589]]], dtype = "float32")#candidate|3031|(2, 5, 8)|const|float32
bop_3032 = relay.right_shift(call_3020.astype('int32'), relay.reshape(const_3031.astype('int32'), relay.shape_of(call_3020))) # shape=(2, 5, 8)
bop_3035 = relay.right_shift(call_3021.astype('int32'), relay.reshape(const_3031.astype('int32'), relay.shape_of(call_3021))) # shape=(2, 5, 8)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_3042 = func_587_call()
call_3043 = func_587_call()
output = relay.Tuple([bop_3032,call_3042,])
output2 = relay.Tuple([bop_3035,call_3043,])
func_3045 = relay.Function([], output)
mod['func_3045'] = func_3045
mod = relay.transform.InferType()(mod)
output = func_3045()
func_3046 = relay.Function([], output)
mutated_mod['func_3046'] = func_3046
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3056 = relay.const(-9.735909, dtype = "float64")#candidate|3056|()|const|float64
var_3057 = relay.var("var_3057", dtype = "float64", shape = (9, 10, 15))#candidate|3057|(9, 10, 15)|var|float64
bop_3058 = relay.floor_mod(const_3056.astype('float64'), var_3057.astype('float64')) # shape=(9, 10, 15)
output = bop_3058
output2 = bop_3058
func_3066 = relay.Function([var_3057,], output)
mod['func_3066'] = func_3066
mod = relay.transform.InferType()(mod)
var_3067 = relay.var("var_3067", dtype = "float64", shape = (9, 10, 15))#candidate|3067|(9, 10, 15)|var|float64
output = func_3066(var_3067)
func_3068 = relay.Function([var_3067], output)
mutated_mod['func_3068'] = func_3068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_3085 = func_587_call()
call_3086 = func_587_call()
uop_3087 = relay.atan(call_3085.astype('float64')) # shape=(2, 5, 8)
uop_3089 = relay.atan(call_3086.astype('float64')) # shape=(2, 5, 8)
output = relay.Tuple([uop_3087,])
output2 = relay.Tuple([uop_3089,])
func_3091 = relay.Function([], output)
mod['func_3091'] = func_3091
mod = relay.transform.InferType()(mod)
mutated_mod['func_3091'] = func_3091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3091_call = mutated_mod.get_global_var('func_3091')
call_3092 = func_3091_call()
output = call_3092
func_3093 = relay.Function([], output)
mutated_mod['func_3093'] = func_3093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_3097 = relay.TupleGetItem(func_2467_call(), 1)
call_3098 = relay.TupleGetItem(func_2469_call(), 1)
uop_3103 = relay.exp(call_3097.astype('float64')) # shape=(2, 5, 8)
uop_3105 = relay.exp(call_3098.astype('float64')) # shape=(2, 5, 8)
func_1512_call = mod.get_global_var('func_1512')
func_1514_call = mutated_mod.get_global_var('func_1514')
call_3113 = relay.TupleGetItem(func_1512_call(), 0)
call_3114 = relay.TupleGetItem(func_1514_call(), 0)
func_144_call = mod.get_global_var('func_144')
func_147_call = mutated_mod.get_global_var('func_147')
const_3134 = relay.const([-7.716495,8.157679,2.097069,9.933514,7.610044,1.819262,-1.938926,4.289963,9.384914,-5.781923,0.606673,-5.660109,-7.955195,1.361625,-8.409792,-1.563610,-5.889837,-2.136609,6.061144,7.074451,-4.240192,5.839057,-4.473314,6.273378,2.341593,-6.655490,5.907686,4.454090,-8.312935,7.542369,9.578932,4.939145,9.691708,4.973687,8.144518,-5.796399,-4.144630,0.699656,-6.923319,-5.504957,-0.330029,-3.960924,-3.731476,-4.603021,6.962771,4.421394,5.548221,-3.418631,8.396939,6.874531,-7.121800,-7.170670,9.530583,3.331258,-3.349773,2.833387,-7.455005,-5.787559,8.577926,0.282001,2.707146,4.753940,9.665072,5.193756,-7.651593,-1.289018,-0.997687,7.526117,-5.117806,-9.024129,-7.856822,2.193979,1.227340,6.111250,-7.677861,0.905751,-9.401556,-6.703225,-0.028552,-5.996555,-9.737238,5.636735,5.671952,-1.463177,-0.300351,-9.233535,-8.423126,5.923957,2.683901,-0.262958,-5.806607,8.164504,0.393424,-0.338505,-3.852889,-0.422803,4.045535,6.602099,-8.087124,-7.027267,-2.375062,0.914387,4.241386,4.167293,-7.927195,-2.987890,2.002862,9.776966,-7.268771,4.976852,-2.851021,5.836166,6.332986,-6.853678,1.046007,-5.123324,3.434745,-9.344659,4.664693,5.340569,-6.428395,-5.059441,-0.404891,-6.152774,8.215546,3.770276,9.877200,-4.566349,0.607814,-3.009820,0.143634,1.282637,-3.927354,0.181710,8.466696,1.702801,5.213181,3.779644,6.050318,-7.774003,3.634204,-8.020018,-7.212682,-9.897468,9.968542,-0.788325,5.786468,6.108055,-5.505302,8.748348,-2.757546,9.227682,-3.379618,7.646084,-1.518303,7.067913,1.460332,-0.522137,-9.041212,7.112813,5.021082,-3.510141,7.228728,-5.731975,6.269599,8.194850,9.646788,4.235848,-6.211277,5.789144,-1.696454,-8.429462,8.425119,8.106775,9.642801,9.152032,5.940482,-5.504035,-2.409240,-4.076735,-2.949010,3.468098,-8.873880,-4.431858,2.253540,9.997900,-0.382157,4.653843,-1.063361,9.137020,9.934074,-3.255067,-4.850081,-0.999011,7.775126,-4.413433,-1.952394,0.099946,-2.360127,3.916587,-6.038645,3.998904,8.358093,-1.977644,-3.382904,6.584916,-8.237695,-1.022640,-4.340558,2.113612,3.522087,-1.770028,0.855065,-0.354534,5.930454,8.181775,-5.437246,-6.874226,0.805613,9.925705,-2.566000,-6.841203,-7.199277,3.942783,1.451209,-3.527623,3.241900,-3.293768,9.876215,-8.508036,4.307878,-0.855657,6.166156,4.771849,0.326287,-9.649893,3.890622,-7.736506,8.802840,8.918229,2.041012,7.443672,-0.060478,5.281726,-0.698427,-5.683082,-1.576266,9.979712,2.631397,-8.250075,7.647156,-8.401059,7.609765,-9.582950,-3.303176,9.840306,9.152066,-5.422563,9.924424,9.566585,-4.818115,6.617338,-8.567999,-8.443604,7.429932,-0.609092,7.353539,3.237713,-8.507849,5.631292,5.666779,-2.932005,3.640878,-8.064305,-0.580157,-9.481552,7.216861,0.042282,-5.953814,3.986150,2.690819,-1.223266,-3.550002,1.707592,0.572707,-3.134794,-8.232794,0.437933,0.226065,-9.705973,-8.984361,-6.571078,-6.917070,6.503657,0.721940,-4.395660,9.808029,5.803251,-3.644764,-5.900368,3.337073,3.512319,4.737149,0.661037,-1.347267,-7.353962,-1.869241,0.303491,9.373582,9.149817,6.429479,7.078035,-8.360224,7.044353,8.517289,-7.498670,-2.268002,-9.140488,3.594022,-1.755814,9.332423,-0.771198,-1.341045,-1.631136,-4.322893,-3.555069,8.880748,-8.234780,1.896389,1.286070,9.163657,2.495152,8.060899,3.212655,-6.004321,-3.738894,9.616342,4.641040,-5.882285,1.733037,-0.048707,1.237772,3.082731,0.965023,1.132142,1.933410,3.879090,-9.099540,9.919239,4.338329,6.839063,3.943981,-2.355334,-4.930874,8.508316,2.070123,-9.667010,1.623327,4.740010,-4.906539,2.124333,9.316860,-9.425346,5.579358,-8.814635,4.185462,2.480770,-9.906213,-4.986169,-7.088509,-1.784085,1.156240,-5.955646,-9.419681,9.547124,-6.179557,-0.821149,8.461740], dtype = "float32")#candidate|3134|(378,)|const|float32
call_3133 = relay.TupleGetItem(func_144_call(relay.reshape(const_3134.astype('float32'), [7, 9, 6])), 0)
call_3135 = relay.TupleGetItem(func_147_call(relay.reshape(const_3134.astype('float32'), [7, 9, 6])), 0)
bop_3156 = relay.greater(uop_3103.astype('bool'), relay.reshape(call_3113.astype('bool'), relay.shape_of(uop_3103))) # shape=(2, 5, 8)
bop_3159 = relay.greater(uop_3105.astype('bool'), relay.reshape(call_3114.astype('bool'), relay.shape_of(uop_3105))) # shape=(2, 5, 8)
output = relay.Tuple([call_3133,const_3134,bop_3156,])
output2 = relay.Tuple([call_3135,const_3134,bop_3159,])
func_3161 = relay.Function([], output)
mod['func_3161'] = func_3161
mod = relay.transform.InferType()(mod)
output = func_3161()
func_3162 = relay.Function([], output)
mutated_mod['func_3162'] = func_3162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_3191 = func_587_call()
call_3192 = func_587_call()
func_1093_call = mod.get_global_var('func_1093')
func_1096_call = mutated_mod.get_global_var('func_1096')
var_3206 = relay.var("var_3206", dtype = "float64", shape = (384,))#candidate|3206|(384,)|var|float64
call_3205 = relay.TupleGetItem(func_1093_call(relay.reshape(var_3206.astype('float64'), [8, 6, 8])), 1)
call_3207 = relay.TupleGetItem(func_1096_call(relay.reshape(var_3206.astype('float64'), [8, 6, 8])), 1)
const_3208 = relay.const([-5.142406,-6.366843,5.468528,-3.190580,8.235825,2.001800,7.227425,3.905985,1.621493,9.439401,1.412501,-4.725137,1.323476,6.803917,-1.327477,-1.315298,7.902206,7.217779,5.815984,1.954472,0.776349,-9.814829,-9.741366,-3.664865,-4.078820,3.871235,3.789557,7.081648,-4.279962,-9.123959,-7.995787,-1.195769,6.668938,-9.124135,2.377471,3.637897,-4.011537,3.454433,-4.348260,-5.237192,-2.821569,-0.700490,8.656685,-2.091830,-7.361890,4.557143,0.479369,2.492948,7.325618,2.511946,6.534253,-2.635055,-3.695968,-1.225132,1.178988,6.839238,-7.337437,1.322149,-0.050200,5.294812,3.100360,6.804394,-2.014717,2.050176,-5.144103,-1.353367,-8.492114,-5.539908,5.055813,1.286973,6.816244,-0.987626,-8.815948,-8.922674,8.612972,-8.647763,-4.723881,9.078264,-1.758983,-3.964946,-1.514130,-7.656523,5.009919,2.413464,2.795321,-0.947957,-3.639679,-2.515144,-8.385045,6.040135,-5.218441,-6.732309,1.200866,-3.066687,9.004238,-3.082150,0.714983,-2.374922,4.426098,0.101173,-8.566543,-4.316261,-7.124410,2.343223,6.130156,-8.300105,-2.674361,-9.020182,1.390816,0.237764,4.783463,-1.255077,-9.407782,-3.435599,-1.789577,-9.955377,0.116621,2.325545,6.726083,-5.366453,6.786028,7.632412,-9.329860,4.414316,-0.609980,-4.660423,9.066166,-1.685653,3.402252,8.845526,5.442469,-2.519886,-9.378518,-7.749227,-2.691131,-8.880282,-3.895605,-4.722066,7.198922,-4.182470,-9.849785,-3.476719,4.230829,-1.551887,6.961408,-6.065601,9.324555,7.157453,0.240088,-2.807634,-5.145153,4.122145,-2.362159,6.000470,-3.033910,3.494768,-9.330120,-7.887999,-6.812886,-1.460820,-7.065786,-1.447677,8.760287,-4.376341,-5.367374,4.484191,5.890311,2.871522,-1.456438,-4.849461,-4.158877,3.914350,9.380967,-6.354907,-9.712191,0.473807,7.282593,2.911566,2.975681,2.212854,-0.904418,-3.870781,-1.468998,5.900296,2.248363,6.237577,2.039220,-2.879198,-3.270609,-6.604849,-2.223062,7.591341,-7.316791,-2.552424,-4.662455,4.520872,-8.067968,2.760656,6.632264,6.808895,-5.357439,-7.971976,-3.079503,-3.509369,4.401162,5.081579,-6.414325,8.767462,8.051321,-3.527033,-8.688258,-3.918994,8.306825,6.760985,-4.563666,7.550424,3.362786,-1.326061,8.278270,-4.179270,-1.972754,-9.136373,-1.440753,8.182456,7.378270,-6.388660,1.676725,4.402338,-6.936761,9.817522,4.218717,2.651783,-9.988449,-6.383273,-5.838811,-4.057966,1.480319,3.800374,-6.553001,8.401084,-1.563174,7.287488,7.642444,-9.614402,4.584799,-5.235382,9.699370,6.929627,-1.240809,7.776660,-7.486606,3.172422,-2.194136,-9.095374,3.772411,-2.845813,7.622940,7.546235,-9.867205,-7.189520,0.347796,9.108483,-0.115594,-1.268198,-6.988799,9.840575,1.855857,-2.609596,5.310622,-9.013886,9.163641,-9.885750,5.665358,5.899762,7.430793,8.514724,-2.238089,4.665170,-6.244549,2.060632,4.130517,3.017865,2.662684,-7.355485,-2.719160,3.627193,-7.383004,-6.338899,8.447029,7.733772,1.622017,2.562652,0.656850,-4.585337,-7.575463,9.455081,-3.235898,-6.720537,-0.799462,-0.710238,-6.115089,-0.614097,3.070987,-0.697773,-4.144696,-5.239063,-9.016303,-3.895073,-4.852710,2.988315,-8.203284,0.678989,-7.770275,4.707551,-1.341716,8.605377,8.710926,7.267986,8.977064,-4.838173,-6.417258,5.464677,-3.867180,-8.573738,2.958552,-3.370553,-2.029145,-6.506933,9.999319,-9.936275,-0.967782,-8.812618,0.484434,-8.899784,6.618969,9.315246,9.497959,8.932310,-6.380631,0.445411,5.690246,1.631433,1.977393,-4.602518,2.818665,-3.783478,0.110294,-2.498568,9.702464,1.950154,7.492466,-9.294168,8.260250,-7.986641,8.658723,5.158986,4.726657,3.142371,8.914229,-6.188741,-0.918724,-9.641887,7.809184,-1.785699,4.044516,-1.591304,-2.273365,-5.534937,-4.888392,6.890084,-4.503385,-9.929428,-7.385117,-6.455224,-3.738430,-7.519768,1.007188,-9.880634,7.221789,8.860829,-6.792057,4.807736,-4.400000,-2.232367], dtype = "float64")#candidate|3208|(384,)|const|float64
bop_3209 = relay.multiply(var_3206.astype('int8'), relay.reshape(const_3208.astype('int8'), relay.shape_of(var_3206))) # shape=(384,)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
const_3216 = relay.const([[3.172677,3.249850,4.634624,0.130297],[-7.857300,3.222823,0.922022,-6.405906],[-1.350499,5.123118,0.118512,1.305806],[3.839942,-1.729953,-2.047782,7.156186],[-5.502638,-8.587513,6.631227,-7.891595],[-5.166830,9.906988,1.586705,9.206977],[3.845945,5.958349,5.399000,0.386652],[8.772158,8.484496,-8.594566,-2.048347],[7.271778,7.245011,-7.562244,2.065286],[9.909103,-1.021552,-7.890145,-4.657132],[3.165501,3.366918,9.743696,8.673737],[-7.842919,-9.389127,5.378592,4.539884],[5.366201,0.935764,-0.211104,7.902183],[9.510347,7.380509,8.682293,-2.027066],[9.216533,-0.014238,-4.530476,0.975605],[-4.256390,1.358807,-2.735117,-6.006393],[9.917644,-1.838746,-9.594084,5.953135],[4.281259,-3.933738,5.139972,9.679489],[-0.134985,3.371725,8.954886,2.184975],[-8.435181,6.117461,3.195058,-3.661627],[-2.030874,-0.823627,-3.714901,-1.633993],[-6.414944,1.718729,2.325989,-0.321116],[-2.700898,-7.102456,7.272360,0.399071],[7.072705,-8.714680,-7.707273,7.754731],[9.053639,-8.135624,-5.448492,-4.213599],[0.575571,-1.603643,-0.689610,-9.273362],[-7.324709,8.685803,-0.954317,9.517333],[7.548896,-0.158062,-7.330345,-5.126119],[8.184671,-2.292811,-8.138701,8.736828],[-6.840849,-5.818336,-1.252160,0.385057],[-2.160214,-7.252035,3.882856,-5.810782],[-1.018019,-0.550579,-0.649879,-0.342046],[8.674938,4.922687,2.340675,5.683267],[-6.386190,2.581899,-7.265984,4.838516],[9.505370,9.911011,8.709650,1.647034],[-0.410437,9.861354,1.358705,9.402417],[-4.827520,-3.981618,9.682215,0.981245],[8.072262,-2.779248,9.058346,-9.021537],[-5.309048,8.918146,0.677840,7.066017],[-3.252973,7.518952,-5.461362,2.009183],[8.162598,2.346983,1.773308,8.761734],[5.453584,7.377028,9.561323,7.459638],[3.575176,-0.098881,4.216361,5.260780],[-3.454064,3.591815,9.827126,5.458340],[-7.452953,0.148514,2.336216,4.969061],[-6.719361,0.205521,-0.126178,8.624421],[3.026129,4.600603,8.435732,-9.081876],[4.838768,2.945323,-7.202451,9.843863],[8.161347,6.831998,7.563920,6.608421],[9.816438,-6.135362,1.850387,7.916521],[5.868185,7.322021,0.189794,-9.453878],[-0.328509,1.562049,-8.869248,9.931931],[5.744074,-5.538221,4.559700,1.705887],[-7.532829,3.145351,9.046639,-4.602945],[7.481052,-3.516925,0.484660,7.850409],[-2.656794,0.201396,3.450765,-1.873685],[4.325969,-0.465514,-9.807186,9.710389],[1.164975,-8.275736,1.885369,4.782511],[-8.487475,-5.793209,-2.939025,1.890932],[-7.882140,6.399921,-2.842224,6.775853],[-5.728166,-0.273271,1.447159,3.196904],[-5.132644,6.509586,-4.996130,-3.176233],[-3.622763,-9.549186,-9.327272,2.670811],[-7.052869,7.431832,-1.177763,-4.716554],[-2.558728,9.585770,-2.746120,-4.852051],[-8.456929,3.610207,-8.020512,-8.955599],[-7.691815,8.052412,-2.642186,2.310136],[0.683798,1.689341,6.149937,-6.021624],[4.217651,1.560770,-7.642084,-4.130100],[-4.592892,6.108154,-6.174648,9.101671],[-6.506064,7.547472,-9.642290,-9.631299],[3.957311,4.364386,1.980325,-5.687112],[-8.008439,1.526980,0.500756,8.250763],[9.507971,-4.471828,-5.589742,-5.232761],[-2.790913,-8.549692,-1.060133,-8.022374],[-3.897741,7.077819,9.586198,-5.451211],[5.536049,-7.007283,-7.336410,-7.807829],[-6.754996,1.790892,5.602839,-9.721845],[7.655228,-2.565029,8.741928,-4.013329],[-5.443921,8.260952,1.693676,8.321130],[7.326073,-9.407940,-6.866978,3.393689],[7.707045,8.902784,-8.105152,1.942695],[-3.725218,-0.712081,-9.504846,-7.836738],[-0.582970,9.813847,9.934807,-8.731422],[-1.939709,-0.162505,-1.136964,-1.460005],[-2.078774,-1.997842,5.349986,6.838638],[2.005760,1.407864,-4.701089,-6.427439],[1.445696,-1.997679,4.187453,-0.349087],[0.078919,-0.916764,-9.897990,-0.865132],[-1.215957,-6.900434,-6.101434,-2.817477],[3.662191,8.178843,8.450239,-4.331958],[3.722382,3.198525,1.309193,0.855134],[1.124663,-6.955431,-9.453013,-0.672435],[7.272456,-9.960777,-5.314487,5.386922],[-9.563116,5.922797,0.299880,-3.898924],[5.773920,8.123174,6.622666,2.498572],[-2.698865,6.155906,-2.982290,2.205284],[-3.830715,0.017903,-2.421469,-3.456268],[-3.356064,-2.568291,7.165076,-7.201364],[7.357056,5.320241,-5.810118,3.501832],[5.218880,0.573801,-2.296691,9.986012],[-5.484073,-2.523109,-4.923385,4.843097],[-1.332654,-4.125878,4.238900,-3.356992],[-9.018863,1.509067,7.100524,7.623520],[2.402117,-0.042501,2.386808,-8.291163],[2.575720,3.893937,8.503657,-6.382130],[-6.531001,2.918973,7.639379,-1.966329],[-0.445636,4.904330,-7.866009,-0.814333],[3.687786,-1.236831,-7.294321,3.749499],[6.673193,9.858578,5.264795,-3.795012],[-9.312102,1.033579,-3.492477,0.530969],[-9.075711,-2.052637,9.919489,-0.836000]], dtype = "float64")#candidate|3216|(112, 4)|const|float64
call_3215 = relay.TupleGetItem(func_1319_call(relay.reshape(const_3216.astype('float64'), [4, 7, 16])), 1)
call_3217 = relay.TupleGetItem(func_1322_call(relay.reshape(const_3216.astype('float64'), [4, 7, 16])), 1)
func_2832_call = mod.get_global_var('func_2832')
func_2834_call = mutated_mod.get_global_var('func_2834')
var_3223 = relay.var("var_3223", dtype = "uint8", shape = (96,))#candidate|3223|(96,)|var|uint8
call_3222 = func_2832_call(relay.reshape(var_3223.astype('uint8'), [4, 12, 2]))
call_3224 = func_2832_call(relay.reshape(var_3223.astype('uint8'), [4, 12, 2]))
bop_3227 = relay.less_equal(const_3216.astype('bool'), relay.reshape(call_3215.astype('bool'), relay.shape_of(const_3216))) # shape=(112, 4)
bop_3230 = relay.less_equal(const_3216.astype('bool'), relay.reshape(call_3217.astype('bool'), relay.shape_of(const_3216))) # shape=(112, 4)
const_3233 = relay.const([-1.244421,1.904370,-3.433642,1.799138,-4.812424,-8.712022,-0.775792,1.094539,9.758781,-0.949958,7.308742,-1.377522,-9.175571,3.461509,-8.743922,3.630975,0.691570,-7.589372,2.490995,-5.558455,-4.568390,-9.795992,6.930738,8.996482,-4.256397,-3.720843,-1.297551,6.105843,1.188884,-7.996612,8.083944,-9.820296,-7.767776,0.400939,-1.222618,0.919966,-8.520921,-9.015129,8.693408,-6.160856,7.430026,-2.949230,4.659656,9.776060,-0.067029,-5.066530,7.608409,-6.391620,-8.541690,5.555144,9.515558,3.256735,0.217725,7.050645,-9.374930,-8.500310,-4.837037,3.051938,5.671786,-9.474470,-5.018148,9.086639,-8.884482,3.719269,8.896825,3.303072,-9.529877,-0.430818,-3.571398,-5.233701,0.917900,5.408275,1.295513,2.519696,8.187547,-1.605545,6.716302,3.574450,3.837262,-7.144409,-3.433936,-1.000918,-2.965249,-8.853827,-6.467519,1.979049,8.747888,-0.878953,-6.306759,7.619338,0.927439,3.290512,-7.151670,-4.213349,-2.528420,-6.226033,0.355873,0.211785,-2.534830,-4.060530,-0.702730,-7.189408,-0.430258,5.987779,3.086835,-0.276933,-2.458921,6.087044,0.656704,8.741675,-9.479535,-6.392854,-7.815553,8.378944,7.624577,8.828984,-2.398516,5.995529,-1.028300,6.548196,-6.424696,5.671980,3.822022,5.915744,-1.881755,-9.216601,-2.493276,-7.286730,-0.072331,6.671734,-3.057027,-2.023823,4.170850,9.961795,-2.738251,8.917067,2.567572,7.238258,9.824413,4.951882,8.839507,-6.785491,-6.088511,-8.438811,-0.134619,-8.355687,5.913821,5.378946,-0.185776,-3.508596,6.784613,0.140848,-3.076794,-1.973869,2.200227,-7.577437,4.053309,1.421861,4.122340,3.651497,9.068247,-7.993236,-0.576736,1.934085,5.292666,7.773252,8.987862,5.927679,6.721927,2.505727,6.581602,-3.513790,-5.673577,-5.602367,0.359642,-5.721715,6.457993,3.023529,-0.706675,-1.053308,9.258382,9.630325,4.140638,-5.731131,-0.011908,0.261095,3.974925,-3.921593,3.883615,-3.320105,-9.769024,-5.646445,9.356910,0.462850,-0.589783,9.562595,4.274538,0.650661,7.239740,-8.568550,4.937768,3.080964,9.319679,6.223040,-7.737617,2.778098,-3.303591,-7.949888,-9.810927,2.919417,-7.753087,-1.205838,1.526525,-7.512821,0.938934,-8.948299,-3.825555,-0.994450,-0.218658,2.493901,9.184339,6.083516,-6.227696,9.402754,-0.538377,7.792425,-1.775302,-8.001026,3.314511,-9.554628,3.574072,-9.111178,1.144980,5.300464,-4.469264,-8.620653,-1.136295,6.695049,-0.621842,3.545465,5.963262,3.717013,-3.283083,-5.516844,-9.177754,-8.924550,2.179103,5.632209,4.174518,-8.424424,4.706102,5.031914,6.941871,-6.712896,-4.182159,-2.871993,8.253532,6.435360,7.844554,9.537675,-3.973190,-7.102448,-0.490120,-0.328159,-2.733483,6.752170,-1.417905,7.510456,5.094429,7.322507,3.918273,-3.857301,4.967536,-2.645574,0.107336,-0.205096,-7.981556,4.177284,-3.581736,-6.527910,1.638735,3.857160,2.590067,7.792567,-8.332636,-4.440817,-2.758818,-5.257150,-9.637261,-4.107758,8.202919,5.806224,0.126424,-9.249020,9.205823,9.765820,1.011058,-8.669837,2.321505,6.857708,-9.622229,-2.107767,-8.987782,-0.194440,0.835226,-6.060227,5.857524,-2.624762,6.011812,-7.281294,-4.542120,7.378720,-3.608374,-5.223942,5.214427,-3.647920,9.688391,-6.210811,0.937824,-7.089006,0.178851,3.147297,-1.575252,-6.772801,5.489378,-0.520057,-6.209270,2.097464,1.671023,-3.905215,4.650384,-9.552234,3.033404,3.230469,8.585083,-0.412892,-8.732505,4.992145,9.148483,-0.442787,6.742237,-9.692565,-9.892677,-5.700834,1.906747,-9.355562,1.804375,5.148431,1.088399,-8.411911,-1.402069,-0.202901,-9.044449,-2.373581,4.599556,-2.091389,3.194885,-0.566167,-3.766339,-7.897358,1.056975,8.298691,2.489809,-1.438365,6.173823,-6.835573,2.801295,-6.866954,-7.414360,8.219524,-0.037601,-1.927913,1.941827,3.524126,-3.746916,3.132472,5.436760,-0.749759,-9.316921,9.852907,2.584475,5.004785,-3.573953,6.015131], dtype = "float64")#candidate|3233|(384,)|const|float64
bop_3234 = relay.greater_equal(var_3206.astype('bool'), relay.reshape(const_3233.astype('bool'), relay.shape_of(var_3206))) # shape=(384,)
func_2938_call = mod.get_global_var('func_2938')
func_2943_call = mutated_mod.get_global_var('func_2943')
var_3247 = relay.var("var_3247", dtype = "float32", shape = (3072,))#candidate|3247|(3072,)|var|float32
var_3248 = relay.var("var_3248", dtype = "float32", shape = (55, 10))#candidate|3248|(55, 10)|var|float32
call_3246 = relay.TupleGetItem(func_2938_call(relay.reshape(var_3247.astype('float32'), [16, 12, 16]), relay.reshape(bop_3234.astype('float64'), [384,]), relay.reshape(var_3248.astype('float32'), [1, 550]), ), 7)
call_3249 = relay.TupleGetItem(func_2943_call(relay.reshape(var_3247.astype('float32'), [16, 12, 16]), relay.reshape(bop_3234.astype('float64'), [384,]), relay.reshape(var_3248.astype('float32'), [1, 550]), ), 7)
output = relay.Tuple([call_3191,call_3205,bop_3209,call_3222,var_3223,bop_3227,bop_3234,call_3246,var_3247,var_3248,])
output2 = relay.Tuple([call_3192,call_3207,bop_3209,call_3224,var_3223,bop_3230,bop_3234,call_3249,var_3247,var_3248,])
func_3260 = relay.Function([var_3206,var_3223,var_3247,var_3248,], output)
mod['func_3260'] = func_3260
mod = relay.transform.InferType()(mod)
mutated_mod['func_3260'] = func_3260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3260_call = mutated_mod.get_global_var('func_3260')
var_3262 = relay.var("var_3262", dtype = "float64", shape = (384,))#candidate|3262|(384,)|var|float64
var_3263 = relay.var("var_3263", dtype = "uint8", shape = (96,))#candidate|3263|(96,)|var|uint8
var_3264 = relay.var("var_3264", dtype = "float32", shape = (3072,))#candidate|3264|(3072,)|var|float32
var_3265 = relay.var("var_3265", dtype = "float32", shape = (55, 10))#candidate|3265|(55, 10)|var|float32
call_3261 = func_3260_call(var_3262,var_3263,var_3264,var_3265,)
output = call_3261
func_3266 = relay.Function([var_3262,var_3263,var_3264,var_3265,], output)
mutated_mod['func_3266'] = func_3266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1911_call = mod.get_global_var('func_1911')
func_1912_call = mutated_mod.get_global_var('func_1912')
call_3327 = relay.TupleGetItem(func_1911_call(), 0)
call_3328 = relay.TupleGetItem(func_1912_call(), 0)
func_1554_call = mod.get_global_var('func_1554')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_3360 = relay.TupleGetItem(func_1554_call(), 0)
call_3361 = relay.TupleGetItem(func_1556_call(), 0)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
const_3364 = relay.const([5.653246,-4.289176,8.550326,5.999573,-9.042578,-5.057593,-5.690631,1.114680,-9.064417,2.579893,3.008705,9.094062,8.459393,-0.420703,7.749608,-1.580102,-1.143982,-8.348580,-2.471028,-6.826845,-4.480706,1.459757,2.716591,-2.373551,7.374677,-2.703216,-4.051817,4.584435,6.223370,-1.902880,9.517915,6.339288,5.815276,5.883779,-9.561016,4.869952,-4.076618,9.010660,9.040754,7.067236,7.230079,0.380524,2.591941,1.383842,9.909377,6.159711,-7.572883,-9.479654,-3.357535,-7.100056,5.457370,-5.324467,-5.506401,5.208332,8.928692,-0.970843,3.274913,-1.259336,-6.645659,3.242638,-3.755639,-4.581714,7.360180,-9.340397,7.997983,-2.300012,-0.837632,-9.995951,3.917021,5.258158,2.125734,5.099651,9.182889,5.060554,-2.295504,6.756896,-3.243683,9.572108,-1.332119,7.368045,-2.628362,-6.309751,-1.438678,4.236316,2.896495,3.482966,-9.490387,2.167015,-8.855899,-0.941680,9.085145,5.267116,2.193090,8.258701,6.414249,8.322183,4.738926,-7.376387,0.947893,6.935407,-7.655718,1.040681,3.688696,3.905366,2.742461,-5.766414,7.851106,-6.557688,2.310211,7.615626,1.541429,-0.521229,-9.587788,-9.055982,4.976770,-2.607222,-3.477880,-0.142142,-2.576303,-7.027661,0.304951,-3.661880,-9.179126,-3.643660,1.048315,-5.398979,-3.967419,6.903030,-4.814995,-7.020337,9.200324,2.230062,-8.622475,9.597012,1.627702,0.061966,9.612100,-3.690388,-2.169596,0.806248,-0.180285,-2.388404,-4.488894,1.640885,-1.933480,-6.840029,8.668302,7.318888,-5.781720,-4.156545,-7.545869,-4.625927,-6.314219,-9.426823,1.610061,-3.374866,3.195909,5.501741,-1.872847,-7.455822,-3.636266,-1.606032,1.692934,-8.593350,-2.397044,1.716516,-8.197021,-8.767602,-9.142496,7.388952,-6.002624,2.542022,6.526338,-4.519700,-3.107202,-8.392366,0.499168,-4.439192,-3.851814,-7.945513,6.223063,-7.471830,-8.270779,-4.000734,7.525150,-1.878938,3.240129,6.151731,-9.364458,-2.608526,7.494388,-3.873220,3.868210,0.153648,7.104555,1.918490,2.196190,-4.261769,-9.833586,4.789565,-7.141913,-1.611482,1.921620,-0.411445,5.923051,-6.120994,1.542842,7.498582,3.213813,1.956614,0.125844,-1.950331,-0.298101,-0.724822,1.004883,-0.192444,6.238775,-2.931067,-9.931652,1.040565,6.479175,-5.131068,-7.432570,-9.279853,-1.156981,-3.452833,-2.610062,7.993316,2.203607,1.690502,7.810662,-1.918151,-7.091647,6.519333,-4.618773,-2.275044,3.310656,-1.150101,6.210164,2.796276,-0.056893,6.790454,-6.345282,8.337716,-6.300271,1.441563,-3.263602,-3.157277,-0.164199,-3.103834,-9.551546,-9.576189,6.402566,7.861005,0.020687,2.209790,-4.609355,-7.905091,5.883789,-8.109523,4.604824,4.479617,-1.300231,-1.212200,6.141964,1.222060,-4.577611,6.389230,-6.875844,-9.699103,-4.308275,-4.584858,-8.835561,6.960615,-0.004914,5.476038,1.500229,-5.984503,-8.059200,-3.173973,6.206126,-5.384743,-1.247726,8.647327,-4.394065,-1.579986,6.058988,-1.067862,-4.934741,6.378690,3.823088,-9.934305,8.037288,-0.081369,6.526735,-5.346755,-8.563779,-3.065246,-8.286886,-4.417984,8.628730,1.414119,6.670413,-8.350495,-8.230995,-2.880989,-9.163718,-8.266307,4.435061,-7.548192,-2.774328,7.100722,7.901702,3.373211,-8.192263,-3.940709,-7.853503,-8.725487,6.270667,3.929640,0.541912,-9.149608,-4.881929,2.167712,6.153973,1.808355,-2.821724,6.791666,-9.430801,-3.177589,-4.405653,6.685694,-5.740347,-2.489600,-9.229954,5.521803,1.689693,-5.789344,9.602573,-5.069208,3.716317,-1.136323,-5.173650,7.161366,-9.947050,8.840512,-0.226059,4.531127,2.443539,8.209662,-4.088635,6.526273,-4.271742,2.834309,4.537015,-7.536738,5.586776,7.075276,-0.755526,1.500559,-8.933301,7.928667,5.950912,7.380803,-9.591467,-9.049474,-8.155517,3.402329,5.930654,-5.235266,-5.707174,3.346911,2.140312,2.091958,6.079978,-9.167225,-8.919823,3.751817,-3.736066,-6.555516,0.923499,1.237423,-7.998009,-7.438455,-5.081043,-1.299425,3.395154,-8.402869,-5.989627,6.696416,-3.844308,5.746337,0.655418,-0.811875,-4.353226,9.450495,-6.657287,4.831584,3.880865,-5.752905,-8.053463,-4.950277,5.626676,-3.365967,-8.461723,6.198278,0.134749,4.627854,4.674499,-9.056551,-6.770700,7.641387,3.765966,2.244322,-0.114431,-5.813399,1.918109,3.336784,7.683534,-1.443208,1.505131,8.292588,3.915631,4.009480,-2.815769,-1.487235,2.655629,1.584972,-7.313965,4.159219,7.424441,9.113934,-8.432733,0.127593,-3.955107,-8.235389,5.182125,-3.502659,-8.137037,-7.852513,7.290239,-8.625305,-5.843492,3.964091,-1.142548,-7.370110,-4.529307,-5.046540], dtype = "float64")#candidate|3364|(448,)|const|float64
call_3363 = relay.TupleGetItem(func_1319_call(relay.reshape(const_3364.astype('float64'), [4, 7, 16])), 0)
call_3365 = relay.TupleGetItem(func_1322_call(relay.reshape(const_3364.astype('float64'), [4, 7, 16])), 0)
bop_3367 = relay.floor_mod(call_3327.astype('float64'), relay.reshape(call_3360.astype('float64'), relay.shape_of(call_3327))) # shape=(2, 5, 8)
bop_3370 = relay.floor_mod(call_3328.astype('float64'), relay.reshape(call_3361.astype('float64'), relay.shape_of(call_3328))) # shape=(2, 5, 8)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_3373 = relay.TupleGetItem(func_573_call(), 0)
call_3374 = relay.TupleGetItem(func_574_call(), 0)
func_2832_call = mod.get_global_var('func_2832')
func_2834_call = mutated_mod.get_global_var('func_2834')
var_3379 = relay.var("var_3379", dtype = "uint8", shape = (96,))#candidate|3379|(96,)|var|uint8
call_3378 = func_2832_call(relay.reshape(var_3379.astype('uint8'), [4, 12, 2]))
call_3380 = func_2832_call(relay.reshape(var_3379.astype('uint8'), [4, 12, 2]))
func_2938_call = mod.get_global_var('func_2938')
func_2943_call = mutated_mod.get_global_var('func_2943')
var_3391 = relay.var("var_3391", dtype = "float32", shape = (3072,))#candidate|3391|(3072,)|var|float32
const_3392 = relay.const([[-9.185442,-3.952955,2.451503,1.912661,-8.631402,0.220928,9.187791,-7.724817,-7.339300,7.104875,-8.495090,1.256504,2.139026,-5.954918,-7.188301,1.079982,-9.032786,6.571146,-7.523201,8.628347,-5.525129,4.311975,3.034782,-0.633505,-6.599199,4.891820,4.063759,-0.635066,0.333631,2.638880,-9.536506,-2.214172,-3.307938,-5.391129,-1.519567,6.859459,-4.306657,-2.941721,5.169503,-2.188918,8.306165,-7.313541,-7.444024,0.028226,6.151079,2.957107,-8.339893,-7.254274,6.068255,7.580204,-7.279743,5.795139,2.568237,-6.886989,-4.058391,3.938836,-2.928938,5.889651,-0.063854,-0.865008,9.665567,9.793347,8.995823,-0.472099],[-8.976543,-2.071846,5.726476,5.244027,-5.220205,1.072329,-5.847182,-7.387646,-0.926793,9.105445,-1.764835,-1.656058,2.347071,7.518669,-7.374294,-7.652519,-1.365621,1.958859,-2.082153,-4.029949,7.803818,8.288991,-6.502147,-0.209370,8.946337,8.228860,-6.969237,1.657247,7.507172,-6.173720,6.204226,-4.751193,-2.385410,1.048559,1.501264,7.407841,2.852072,-5.063759,-8.566032,-9.541186,2.962018,7.633408,8.315215,8.803412,-8.108036,-6.495122,-4.624641,4.361177,0.498488,4.418660,-2.976819,2.723775,-5.215883,-9.645454,-6.228077,-2.998989,-2.392936,1.152884,9.492482,9.432038,1.888628,7.336371,-9.259147,-3.224979],[4.830362,-5.182706,-3.206129,6.016508,-4.815648,6.789149,-5.512429,-5.888473,7.115154,-7.583674,-8.714659,-6.992090,-1.151902,-2.920298,-6.445162,-8.705665,-5.031226,-8.224689,-7.433445,4.938105,5.854439,8.376652,7.816942,-3.303612,-7.452923,5.134539,-6.002314,-4.329925,9.924170,-7.187195,3.576657,2.502541,3.356149,-7.264075,6.480314,-0.550554,-5.628889,-5.872993,9.815912,-5.044616,1.689403,1.494774,-2.431821,-8.402862,-4.101379,5.411339,8.540339,6.527371,-1.922673,-9.431396,-8.524543,-9.772957,5.321425,-8.675262,-8.291138,-4.657347,-1.482492,7.696322,6.075120,-6.313913,-7.632975,1.047489,-9.835273,7.058299],[-2.729051,-1.511775,-5.906415,6.079654,2.430325,2.571250,-7.887049,2.189332,4.507721,3.131864,2.675134,-7.414043,-5.526339,4.743811,-6.591865,3.714264,2.063328,9.185827,7.027629,0.789202,-9.663902,-0.610139,-0.276588,2.482014,-3.183877,-1.037402,-8.910586,-9.946971,-2.944967,3.394115,-3.023206,9.050330,-1.754415,2.823932,9.840192,-7.561252,6.911651,-6.282622,3.841271,8.952613,0.568992,4.085468,-4.032385,-5.310719,2.108760,-4.270862,-0.527640,7.655347,-7.723012,-3.606907,8.502715,-6.871074,5.606995,-9.618183,-5.187326,9.460431,9.915478,-8.682666,-6.681494,-2.290095,-9.299726,6.300419,-9.422898,-3.833448],[6.804067,-0.608161,7.484033,-7.991237,-3.206736,8.441423,-9.208191,-3.511001,3.124843,-6.058312,0.075943,-7.422259,8.691913,-7.720613,-4.956930,-1.872886,-9.955408,8.499429,2.556379,-9.553256,-0.830673,7.780216,-1.810726,3.349822,-2.984083,3.206083,-8.164698,9.670970,0.356746,-2.466382,-6.205765,-1.259107,2.398824,2.484293,0.882093,-8.387757,5.368858,-7.570876,7.554602,-0.784516,0.930791,6.724750,0.209273,9.175908,8.153341,-0.699045,2.307819,-2.023724,-5.105373,6.370142,5.444420,-8.312390,7.742383,9.387977,-5.382020,-1.261657,9.433991,7.871438,7.462421,-4.031801,-1.193773,-1.371652,2.813601,7.251770],[-2.503028,0.172061,-8.829471,6.939958,-9.688660,3.782065,-0.439600,2.523374,4.251122,-9.944146,2.614725,1.772321,0.245174,6.131204,-7.593224,3.052099,-4.953819,7.044072,-2.281946,-7.245080,2.099117,8.764223,-1.134725,8.454591,4.649770,-4.143713,-3.891078,5.430470,9.063841,-6.699721,8.570422,1.399606,-3.555993,-5.950964,4.311674,-8.087175,-0.767960,-7.898120,-3.342898,6.316004,5.476068,-4.149486,1.046466,0.784627,5.016492,0.239831,2.416388,-8.172955,7.939086,-7.735057,0.381318,5.296036,-4.509430,-8.444423,8.295255,9.486040,4.245980,1.997266,7.800433,-1.797351,-7.764727,2.625288,-1.497394,-7.783792]], dtype = "float64")#candidate|3392|(6, 64)|const|float64
var_3393 = relay.var("var_3393", dtype = "float32", shape = (550,))#candidate|3393|(550,)|var|float32
call_3390 = relay.TupleGetItem(func_2938_call(relay.reshape(var_3391.astype('float32'), [16, 12, 16]), relay.reshape(const_3392.astype('float64'), [384,]), relay.reshape(var_3393.astype('float32'), [1, 550]), ), 8)
call_3394 = relay.TupleGetItem(func_2943_call(relay.reshape(var_3391.astype('float32'), [16, 12, 16]), relay.reshape(const_3392.astype('float64'), [384,]), relay.reshape(var_3393.astype('float32'), [1, 550]), ), 8)
const_3399 = relay.const([0.604262,8.785113,9.815934,5.742823,9.292076,3.152657,1.148259,2.313971,8.586346,-2.302801,4.907663,-7.396048,9.996877,7.790415,1.921914,-0.766961,5.869796,1.148523,3.240027,9.312137,1.103235,-0.332360,-2.374051,-5.930407,6.360291,-5.796293,-4.453339,-4.983648,6.810151,-8.215804,-1.300692,5.965885,-4.907530,-1.849657,3.161384,-6.588235,-6.667457,8.959677,0.506689,-4.754759,-0.871179,1.465482,0.286473,1.818425,1.322526,-0.076818,-8.233308,4.994307,-6.907282,-5.321876,-2.628172,-2.824545,-9.295506,8.428523,3.756838,-3.836094,9.620534,6.818795,6.143407,6.482279,-6.699408,-4.204032,8.347506,1.769957,5.796484,9.563556,6.604134,-3.407933,5.572940,6.316569,2.308151,-4.146080,9.305823,-0.578987,-1.989739,3.253251,8.742438,7.067602,-6.172647,-5.882089,4.052388,0.382043,7.699066,-8.996562,1.540844,2.192604,8.756534,5.615032,7.214618,-1.072957,6.861103,-8.319772,3.722723,6.838309,0.526461,-0.786143,2.374527,4.708034,4.307956,5.197471,1.348501,-7.781954,4.276751,9.624164,1.905868,-3.061763,0.543469,2.555696,6.135888,-2.304505,-1.545069,4.843312,-7.742253,-1.791111,-6.800627,9.138823,-2.594938,-7.156017,7.358054,3.794803,9.817622,-2.752921,-5.270130,-2.666287,-4.607912,-1.072028,5.846751,2.969757,-4.481025,5.988610,0.727257,-8.301330,-2.342128,8.423913,-2.859191,-6.323391,2.462596,1.623477,-3.648377,9.857224,-3.598326,5.820347,4.715163,-8.567246,-5.896999,-0.119990,-2.578441,-9.662860,1.333514,-4.339534,-9.690406,-2.834656,9.626379,6.503361,9.276503,6.777356,7.840950,2.348151,3.697737,-3.320811,7.541513,2.674571,-6.203930,8.585161,-8.546628,3.200362,-0.558868,-0.356597,7.317453,-3.230082,-4.854663,1.122722,-9.694119,-6.272111,-0.683127,-3.455992,1.311684,1.149167,3.259808,7.669909,-2.368540,-2.691205,-2.531126,2.853756,-3.330843,-1.985770,2.432037,-2.415209,-7.515244,4.628866,-6.751942,2.694839,8.705581,9.041277,3.119940,-8.638864,6.251298,-0.343390,2.393647,-4.544475,7.722906,-0.069282,-7.822575,6.625260,5.013599,4.158084,-5.813828,1.063334,1.734242,-7.368438,-5.734047,-4.342445,8.355288,2.893932,-8.423817,-9.279354,0.277241,-5.211399,-3.324248,-3.794806,-5.353709,8.908419,-8.312377,4.583558,8.293204,-3.916014,-9.898954,8.058876,-6.785639,5.707925,-1.246199,-1.764502,-3.497431,5.908083,-2.412460,1.697515,2.134419,2.913249,6.993115,4.961998,-7.783572,-7.511706,0.767939,-7.753034,2.317295,-3.354480,-2.034877,4.984396,-1.098077,4.544746,-4.083151,0.468346,6.905025,-9.661917,8.571102,0.550804,9.011117,0.624653,2.997249,-5.274611,9.441715,9.113134,-9.563581,-9.130940,0.039881,7.873670,-1.686004,-8.278851,-0.433761,0.718103,-3.677283,3.825043,-5.492109,-5.191108,6.854956,-4.900820,-5.074200,-4.256152,-5.619705,5.452303,-0.318609,-3.908481,0.191735,-1.075218,8.187230,-7.641951,-5.353883,7.585679,-4.211417,-9.039669,7.335290,-5.594982,-0.882091,-4.115792,9.497421,3.587955,-1.968636,2.355257,-4.454042,8.024249,1.549670,2.764447,-6.451148,-4.917036,8.254505,-9.994529,-0.931803,-2.596120,7.013649,1.858132,-5.887921,-0.874846,-5.181018,-1.484623,9.856180,-9.050281,7.576441,-8.122056,4.918561,-5.862341,7.881619,8.109471,8.582819,7.856471,-4.963237,-4.971259,8.619826,6.519112,-5.156328,-9.872266,-8.088737,-1.612085,-5.342426,7.618633,6.459238,-5.716926,-5.261668,-9.313487,4.693043,-7.131859,9.845558,-6.924086,9.274804,-7.573316,-2.943980,2.104269,-2.284279,-1.971012,-9.070404,-2.061801,-4.999071,-7.640277,-1.643591,-2.052802,-6.053047,8.874794,6.556171,-5.412304,5.408348,-1.785504,3.421256,-0.535495,1.480870,2.143756,-5.052102,-8.162677,-6.903500,3.766725,0.247961,4.381120,-2.232942,6.596190,-4.187827,-2.514630,2.253849,7.612409,-2.019409,-5.281728,2.188063,1.693711,6.997582,-2.380910,0.118297,-1.819588,7.455415,-7.727743,-3.385232,-7.283111,-7.423384,-8.965556,2.193973,-4.619292,-8.662260,-3.760933,-3.594910,2.636213,0.031803,-8.404480,-1.954746,8.829115,-2.201452,1.838290,-6.107105,8.561645,3.943412,-7.299367,-1.117120,-3.352382,1.856597,-2.664248,6.574644,5.436798,5.996079,3.119265,-6.694269,8.264842,-6.508289,0.137351,-2.001392,9.490255,-2.953473,1.411558,4.332555,3.908941,-9.200304,-5.912107,-7.889918,-0.331209,5.702632,6.131282,-7.504238,-4.890818,5.525908,5.310958,7.281317,0.667445,-1.108447,-4.416876,3.516709,-8.068950,4.756469,5.938131,-5.990865,4.567627,6.737294,9.517599,3.062640,-5.466626,7.051167,5.267923,3.012946,2.096712,4.992109,4.908281,4.470592,-1.588756,-8.394914,-2.960094,3.164689,9.251821,-2.708430,-8.562661,-3.348392,2.525113,4.860204,-7.002927,5.649558,-2.282739,4.015257,8.296338,-7.909599,5.096904,9.800158,9.267426,8.357215,2.612903,-4.202518,-6.310275,3.916725,-7.025483,-4.007246,3.777803,-3.078972,-4.711796,0.756571,3.870615,2.356438,-3.688070,-7.366535,4.999738,-7.778093,-9.640458,-5.351846,-5.012940,-2.618807,-6.912344,3.206255,-9.938191,-9.382542,-5.743148,9.936614,8.149430,-9.970111,7.497176,3.370630,5.208896,-1.763272,-8.310360,-2.154444,-9.559446,-7.053645,8.748042,-0.343245,4.566970,-3.134403,-5.764582,2.050728,-7.212004,6.469269,8.185740,-7.638768,5.201348,-3.266397,4.226724,-1.760819,1.709697,0.226347,-8.986284,-9.821357,-9.073864,1.516443,-4.410621,-2.548750,4.940723,2.864587,-3.315074,0.998266,-4.427078,-9.823393,-6.990830,9.372682,5.023727,-3.376142,-8.803317,4.012928,2.155430,8.283419,-1.159396,-6.861890,9.029316,-8.650773,2.439593,3.478718,7.583255,6.288397,-0.696515,5.432318,6.123446,-0.036487,-2.571491,-2.622850,-6.518169,-2.905210,8.468469,-8.461079,-2.415688,0.008675,-5.413427,8.917007,-1.985791,0.617891,8.975267,-7.270876,-6.897845,-9.415927,-7.554340,-8.477403,-1.199174,4.612897,6.338857,-8.199570,-4.276024,6.173970,7.478923,-9.388338,-7.753833,-5.741551,-2.732019,-8.607702,4.153150,-7.805112,-3.882464,0.974625,3.206891,-9.100037,-7.474341,-6.534693,-5.255550,-2.418623,-9.196035,4.392037,-4.765862,-0.389516,-0.157096,-8.874467,8.575417,-3.799125,6.684646,-9.379254,-2.760366,-5.597095,9.442329,-7.358645,-4.817137,8.549369,6.062752,0.803609,4.163471,3.752443,4.266978,1.696090,-5.841504,-0.886986,1.057264,-8.697407,6.463554,8.541957,7.049515,5.040563,-2.753567,-7.155079,7.404697,5.216370,9.577295,3.450580,-3.958823,7.851875,-7.580319,3.936036,-3.867240,3.884910,-2.776798,-5.997437,-1.898530,9.215042,0.472328,4.610054,-0.245640,1.213123,6.638017,-3.340169,6.221336,-6.960503,6.895934,-5.564760,9.066025,8.633995,-2.882081,0.873093,4.499389,6.845033,-7.667957,-2.503168,7.837168,-0.166331,-8.707381,6.496311,-4.699098,9.161049,2.360739,6.802310,4.843152,-9.871056,-6.903528,3.656546,-4.558840,-5.755104,9.636644,1.631759,-2.013266,6.587704,-0.089675,8.505688,-1.886581,-1.337180,-9.945747,-7.010844,5.883574,2.919390,-7.096748,1.958334,1.692221,5.154531,-1.715153,0.448019,-2.641081,0.430349,4.173760,8.450133,5.060767,6.279702,3.952831,-2.573618,-8.205988,-7.686408,-1.008589,-8.182810,-7.522940,-4.336748,-8.520988,5.794071,-2.936123,-5.225159,5.605725,7.422698,1.982517,-2.227476,-6.156085,4.396840,-4.806057,0.277063,-0.353557,-3.624920,1.352543,0.607075,0.681735,-2.104118,-4.245404,5.319993,-6.553067,-9.945331,-8.943010,-3.369677,5.785870,9.092254,5.003311,-5.427784,-8.104377,-0.555796,4.596613,-8.825743,2.103109,-3.383258,2.200522,5.299756,-0.286192,1.105802,3.147551,5.442234,-3.111198,-0.116395,5.730884,6.656104,-8.377488,1.537223,7.665523,-1.684137,-2.282547,-2.807365,-1.368129,8.624574,-1.704311,8.239789,-2.182612,-2.946585,-5.411033,5.713560,-7.688665,9.419750,-2.814173,-1.472600,-2.655651,-8.286756,-9.329120,-2.193799,2.172842,5.649967,3.191880,8.755988,-8.444768,-7.099140,-9.599822,-1.040212,-4.050968,8.679436,8.123172,-9.713897,-0.275033,-1.003854,-1.274751,-2.910588,5.084500,4.228883,-5.539531,-3.638369,-4.985560,7.117480,-3.197338,3.600361,-5.392027,-4.300302,2.744056,9.351083,3.252123,-6.832409,2.742095,7.802519,-4.932639,0.815100,2.726222,5.824057,-3.238440,4.612925,4.312440,3.903057,5.861170,7.907239,-8.810797,5.329492,-1.924580,7.704969,-4.064461,-5.097185,1.524873,1.067911,-7.157423,7.193896,-3.184972,8.736892,3.018349,9.399817,-2.459164,0.425256,4.512390,4.627520,-8.350791,8.994168,6.542251,-8.271014,3.772161,-5.362602,-7.096893,-8.867699,-8.559013,-5.792703,-4.973660,-0.167115,-2.312276,-6.947733,-1.288751,-2.650891,-9.323980,7.653433,4.331667,2.529784,-0.544388,-6.281475,1.741492,2.550345,1.498110,2.074377,9.485383,-6.073918,-9.398748,8.353160,-0.122346,9.154350,-5.444569,4.414076,-6.506863,-9.263961,-1.767920,-1.795183,-8.307724,6.431255,8.354499,2.701904,-3.674294,6.100013,-7.559715,-5.969268,-8.648375,-3.129043,-4.378998,-0.119782,-6.203025,7.247665,-8.384399,-9.302480,2.760818,-8.781012,-6.939903,1.893596,4.478907,8.650977,-5.611105,3.968560,-5.033784,0.304573,0.788958,2.391728,-2.340499,-2.626338,-9.950202,2.779417,-2.506089,3.408770,-2.565906,4.774515,2.806597,3.593795,-4.287327,-9.297070,-5.330188,-8.979266,4.400067,9.453956,-2.151898,-9.283739,-8.350539,2.557798,1.081196,-8.399678,1.670167,-2.082028,-6.734996,-6.167706,-8.866557,2.695496,-3.077047,-4.210121,-4.660069,-3.262098,9.973599,6.653216,-2.834249,-1.888019,9.012669,9.030903,-5.533257,0.248523,-5.446548,-3.303952,-3.785028,9.050633,5.940778,5.025126,-4.524041,-4.082978,-2.945799,4.306492,-1.074169,3.109614,-1.291157,6.225132,-8.197130,-1.946787,-9.864738,0.706335,-5.630642,-5.126092,-5.755745,8.828171,2.425896,-5.127703,-6.925042,-6.265273,9.275425,-8.764907,6.598496,-0.111690,1.492019,-0.705351,7.256628,-2.311253,-1.563450,9.371774,-9.805498,2.464931,6.948019,-2.333642,-6.394279,-3.498107,-4.300934,5.241387,-0.492480,0.377514,-0.804612,-2.568521,9.690394,-8.211947,3.149940,-7.030844,-3.632580,8.450883,2.639614,8.967873,-0.193786,6.114739,2.166545,-8.577106,-7.012762,9.845034,9.351881,7.764646,-6.453033,2.374322,5.278956,-5.902999,5.225278,0.563049,7.238184,-2.694776,6.829544,-1.505881,1.218273,-9.699699,-6.116250,-4.370478,4.498735,-8.064958,9.831935,3.005167,8.321615,2.430827,4.462212,3.932430,9.463931,1.747097,3.428947,5.101893,-0.533514,-2.769960,8.001721,6.296001,-0.214168,2.735541,6.787106,4.542445,-9.151979,8.317889,2.160159,-6.406427,2.212262,9.418671,7.452020,3.388665,9.991030,-6.749118,-8.110524,1.384849,3.320099,7.674159,-2.583716,7.090960,9.298123,-1.712702,5.884399,0.140537,-7.421259,1.605472,-6.459041,-1.363511,-5.260551,-8.003448,-5.569824,-7.725533,-3.637299,-1.771313,-0.281752,1.604049,-9.399810,-9.432556,-4.542094,-0.163990,3.073221,-2.596465,-1.162553,2.133110,5.172207,-3.225665,6.873923,9.514942,-9.971157,-0.233831,3.328367,-3.307924,-1.423133,0.186421,-0.368443,3.665314,0.452091,4.262693,-8.000716,5.927796,5.279497,7.971966,-6.475610,-7.575363,-3.055165,6.746626,8.992694,-5.956279,-6.792907,-6.870943,8.295892,-5.600486,-0.643047,4.400707,-4.321644,-9.507847,-8.900045,0.212976,4.100284,7.040310,-7.270366,3.834417,-5.511558,5.065471,-2.242384,0.430618,-1.591721,-7.831918,-5.982450,5.995717,-4.711866,-4.753531,-1.764459,4.156277,5.692403,1.589268,4.155569,5.906026,-6.548179,5.411946,0.830798,4.668034,-3.162906,-7.978905,2.052019,-2.423292,7.384436,-6.172167,-8.889030,4.442437,-3.798385,1.893973,-0.192174,9.823866,-6.050234,1.321913,6.024621,8.527988,-7.166746,-1.976514,2.597080,-3.128411,4.811425,-4.115418,-3.117627,-4.591335,2.617782,7.153777,-8.114501,-5.167053,1.624846,-0.885000,-2.529309,-7.659660,2.327612,-7.421772,4.293926,-2.721236,7.292808,-0.591513,-8.974247,-5.596975,2.102766,8.988266,-6.232349,-6.409021,6.500157,1.090422,-8.092430,1.182754,-8.790413,-2.668062,-8.874484,1.136338,-5.814781,9.157758,-5.844283,-8.152857,8.187698,0.305453,9.147327,5.627841,9.735914,1.581100,8.137036,1.541907,-5.082740,2.365146,-2.642350,8.198866,5.323882,-5.169958,-2.442265,8.720441,-8.078876,-8.811971,-9.051588,3.921757,-3.716464,5.559092,9.283292,5.900551,-8.642522,-9.115170,3.357521,7.302147,-9.117181,-2.310090,-6.518167,0.499760,9.380493,1.568579,2.837802,7.078125,5.269231,7.239523,6.516419,-3.150704,-5.212154,3.899173,-0.925336,-3.287764,-6.871461,-3.298742,-9.934933,7.786034,8.625278,5.603993,9.038775,-7.292758,4.765743,3.764760,-2.277613,-3.368335,-4.650642,8.893839,4.102648,-9.647633,-5.862097,-6.650556,-6.383421,-6.322688,-3.678124,-8.968536,-3.557955,-7.820443,6.975149,8.015996,-3.023745,-8.881882,2.751495,5.339781,2.681246,-9.415181,-5.038907,-8.137916,-0.909103,-6.456211,-3.968610,3.378230,6.050064,-9.873590,5.038494,3.263143,1.617437,6.030386,6.822373,2.944862,-4.670748,-5.942732,3.436025,8.335829,-0.865066,-8.352444,-6.547602,9.198534,-5.318083,-5.734453,6.360852,5.685873,2.611812,2.237733,0.838978,0.573693,-3.594075,4.036408,-8.851279,-5.786845,-6.436293,6.474087,-7.980854,6.580814,-4.044148,-2.448643,8.741782,5.534729,-9.935370,4.893980,5.870149,0.889798,-2.414164,5.943992,6.380830,5.105972,4.927845,9.057470,-0.243861,-7.618308,-4.483065,-0.356326,-7.047647,4.996145,3.845310,-9.312974,6.256321,-3.570703,-1.764735,5.897290,8.840656,-1.549159,9.605196,-8.078829,-9.512123,4.228616,-5.383735,-2.153633,4.444342,4.993961,-5.196306,5.357398,-9.676474,6.702131,-3.318544,-3.752801,-5.167166,-1.643838,-1.652500,3.516120,8.774050,-2.762742,-7.833701,-8.503352,-4.855489,-8.144478,1.626427,-0.870896,-8.015421,2.607018,-1.323594,-3.778385,-3.235360,5.459917,-0.533189,1.206884,1.066253,3.301835,-9.233585,3.203316,5.758461,0.572234,9.624288,-0.235118,9.300336,-5.066588,-1.939499,-5.855805,5.349228,3.470702,-3.213606,8.869225,-2.711035,-9.702748,-8.007248,4.042285,5.983851,8.408841,9.418312,-1.392548,5.354775,-2.910073,-3.126726,-0.982784,-5.206586,7.478730,-9.508429,-4.874499,5.421524,3.787005,-9.836012,4.986987,8.996468,3.125079,2.872101,1.442906,-9.739502,-8.259473,0.567395,1.462275,-9.897416,-3.083181,3.295047,-5.319555,1.338720,2.554249,-9.932203,-4.080788,6.344746,-7.673530,4.993551,1.428544,-2.962441,-0.937256,-8.892769,7.545255,-9.543089,0.804099,3.803415,-6.372296,4.636329,-1.840788,7.221986,8.476965,-2.903017,1.706608,0.410767,-0.077523,-1.100604,7.700188,-0.166428,1.903299,2.826190,-2.937552,-3.880922,2.237659,-8.822571,-8.116649,-9.506492,-5.754989,5.802257,1.078335,-4.513941,-3.907785,-2.900168,4.259632,3.562232,-7.039814,8.962679,2.212563,1.100227,9.032029,-4.102929,8.829718,8.489938,-4.170113,7.061673,-7.388291,9.293915,-0.825979,-2.040134,-2.831473,6.915394,-5.967127,4.033060,-5.886471,5.868206,6.991555,1.313770,-3.536238,-9.832113,-7.953784,-2.464038,-4.281895,3.105051,-1.717097,-3.251242,2.293095,9.121573,9.393436,4.498395,6.999839,2.284344,2.121975,-5.790989,-5.315098,-4.358733,-5.177469,4.245048,-1.879948,-0.436295,-2.778425,2.782139,-3.257262,-5.282156,4.692364,2.968438,-1.758247,9.998239,-0.477555,5.236438,5.820253,9.587075,8.881286,-4.582136,5.411325,-6.794355,3.602069,-4.659152,-6.580172,0.286115,-4.388824,-1.200138,-7.241610,-1.930610,0.685681,1.795908,2.620592,7.305156,0.236027,-7.244110,-5.462568,-4.503684,-6.377033,3.492029,6.461044,3.821284,9.280546,-8.534011,0.789181,-2.934971,0.155335,0.697934,-2.393960,7.853513,-5.801960,3.657823,-4.909076,2.029380,-7.689791,7.241945,2.637224,3.777393,-0.072322,-1.157366,2.035444,7.453143,-2.959873,9.012824,9.211886,-1.247914,1.551107,-4.042570,-8.241544,-8.276655,-5.379601,-5.289531,-3.487621,-8.665953,-3.998101,4.525385,-2.343066,-7.259584,1.453267,2.049636,-7.693757,5.454861,7.926555,7.029648,6.323867,-8.296322,8.189939,0.862674,5.547548,-3.659100,1.855069,6.404075,-4.655954,-1.848587,9.916588,-7.463868,-3.782108,7.284601,4.842314,4.209358,4.939646,-8.683558,-6.174962,-3.095595,-9.597432,1.205463,-2.718273,7.324520,-2.998539,8.674239,9.798543,8.177704,9.992609,-0.060470,2.668246,9.741590,9.083031,1.244789,1.052577,0.035920,6.771356,3.669407,2.813981,-0.915827,9.855073,-6.224898,-0.060900,-4.333449,-7.408096,-0.350145,-9.566583,-9.072225,-6.227106,6.981586,-7.099466,1.267561,-7.448298,6.063099,9.060839,4.771971,6.842962,1.956706,-0.979917,7.981523,-5.183980,-4.691171,6.368770,6.441178,5.003647,-6.744845,5.363445,6.887635,-5.057132,-4.992656,-9.331006,-0.693184,8.160701,9.168571,2.435568,-7.584441,6.141333,-2.280620,-5.687045,-5.422410,8.691962,7.711121,-9.248088,-5.023212,3.678008,-1.095899,-3.002252,-6.400194,-7.648288,0.778959,-1.390222,-8.621424,8.312579,2.710730,-5.949687,3.500462,-2.754943,-2.795662,9.008318,2.147625,2.725041,-1.637831,7.814095,4.573487,3.951727,7.770342,2.412315,3.121047,0.247238,-7.321326,-8.431554,7.817287,-5.493634,2.267973,-3.136786,-0.409686,-7.521130,9.943894,3.832161,3.260163,-7.905736,2.482035,-6.698374,-0.994468,3.830393,0.325119,-1.093798,-7.263208,2.870267,-3.323294,-6.877314,2.463973,7.988999,-3.154993,-6.080178,7.274031,2.559832,-0.549028,9.911032,0.197072,2.985037,-4.262817,1.262983,-1.829570,-0.104695,-2.907618,9.928773,9.806139,-5.150113,-4.700177,-1.644400,2.667684,-9.925193,5.224862,-8.868037,-7.616164,-4.247752,9.662281,8.882133,-7.561527,-7.967585,-1.039073,-4.802441,4.197751,-3.960631,3.798280,1.552145,-1.099427,-7.284063,-3.213978,-6.187467,-0.721431,2.176669,-8.617723,0.925062,5.942074,4.841572,-8.687582,9.183995,-6.377466,3.599962,-4.461567,8.631738,-3.554146,9.142881,-3.857751,5.601998,-9.708435,8.454572,7.641499,8.621070,-0.032271,-2.896775,-1.706634,-6.326221,6.969197,9.701998,8.589133,-3.522590,-9.316022,-4.746953,0.573966,-0.038542,-4.962576,-1.171000,-0.533179,-4.870549,-1.771963,8.605673,0.564706,-0.190121,9.040684,-7.164970,-2.471163,-2.580441,-7.151071,1.791187,-8.358060,9.859593,8.242513,-3.547100,7.653008,7.364428,-5.457667,7.339439,-1.567340,-6.103096,3.812536,-4.735942,-6.592748,-6.918166,3.887590,-2.053494,1.850662,0.780515,-2.046843,0.259796,-7.123724,4.295415,0.749183,-7.699074,-7.709034,-8.804220,-5.828544,3.029872,3.791543,2.835899,-4.216032,7.798727,-6.303011,-3.104612,-1.074642,-3.198649,-5.328451,3.885608,-0.746554,-3.956431,8.076562,-4.821242,9.590128,-8.131718,-1.535075,-8.884114,7.979822,-7.578260,-9.830484,-0.705535,-1.545638,6.581713,0.221066,3.816834,3.247037,-0.470110,-6.031030,-1.448374,3.578699,-6.663602,-9.259001,-0.472007,-5.626492,5.870449,7.370852,-1.590010,8.826594,8.662482,-2.512813,-8.970219,-2.395188,-7.941080,-5.969275,-9.495694,2.817930,1.490759,8.740512,-2.943192,-0.604485,-7.904128,9.339126,-6.987348,7.619128,7.951103,-5.450457,3.312344,3.093406,1.023380,-1.221979,5.001957,-5.282640,3.747389,-4.530932,-4.713044,-1.278549,-5.482505,3.225223,-5.150529,-9.356240,-4.899314,2.065206,1.962176,-9.543339,-0.607637,0.493081,-1.508141,-3.502645,8.793164,4.831773,-9.434132,4.980006,-9.613020,0.705231,4.778983,-1.742520,-2.469962,5.626088,-9.472598,-2.621519,-4.622273,-9.507301,3.608960,-7.911069,1.934522,-8.972603,6.754713,6.276620,-5.669418,-4.069616,-1.513683,-8.585677,2.731377,8.977285,4.848768,-7.666553,2.354266,-7.144139,-1.559534,2.709891,9.834505,1.751113,4.339787,-8.830716,8.087241,7.520997,6.262517,-9.766865,1.635714,2.020767,0.125355,-0.850041,-1.260607,1.002901,-4.241332,4.065380,2.804441,-2.076253,4.140759,-6.804204,-6.202890,-8.625782,4.988368,-9.865073,-4.213167,4.836969,3.312630,-4.283055,0.968581,-1.860960,7.840800,9.798531,-9.252969,5.043794,-8.305883,-8.503146,-3.327629,-4.707999,9.866840,-6.694607,-7.476433,0.084227,-9.716043,-1.977210,-2.138881,7.886864,-0.235992,-0.325686,-7.523762,-1.893108,8.786013,9.663712,6.595175,-5.914999,-6.873110,6.984475,-6.458267,8.485761,-1.776338,-0.088790,-4.661737,-7.933909,-0.129536,-7.732494,4.797609,1.281680,2.504351,-5.151889,4.057942,-0.390477,6.275613,-4.603786,-4.689568,-6.763456,7.448693,7.331342,-3.476508,-0.827441,-1.709867,-6.751111,9.211907,9.455737,-4.316847,-6.831821,-6.796444,-1.972856,-7.120898,6.529129,-9.728363,8.989335,4.251922,6.750481,7.960821,-7.952013,-1.073452,7.196822,1.701770,5.026235,-1.008620,2.283738,-7.219344,-2.483879,-0.019508,1.511131,-1.026594,1.424118,-4.088609,9.663849,-8.072939,2.150330,-5.968046,2.546334,5.337653,-8.009154,-9.877538,-1.653434,8.908106,6.572754,9.589667,-8.256540,1.586540,8.450866,-1.908562,6.813140,-3.596231,-4.998362,8.544217,-8.227151,-5.787983,-1.004287,-5.637013,4.996693,-7.709170,-3.534632,7.416996,6.020923,-8.097657,-4.519672,4.409147,7.838564,9.536154,4.747007,4.496483,9.831315,-3.212377,-8.791915,9.800265,-8.071311,-5.047378,6.004784,8.367255,9.421779,8.025094,-4.393679,5.429179,-8.557346,9.402837,-2.283944,-9.394463,-8.116422,7.836995,3.604204,-2.890380,-3.162925,-7.216032,8.872077,-0.360621,8.374240,-8.260389,5.283200,-1.967589,-9.020501,7.057389,-9.986548,0.278818,-5.635520,-9.967694,7.476311,3.466529,8.463877,2.807994,0.360656,7.308352,9.900287,-0.736902,-4.127036,-1.660860,0.850252,7.284994,6.208301,-2.296422,6.497898,-2.573612,-4.744752,8.208961,5.434497,-6.440915,-4.064995,-6.917022,2.235709,-7.969252,9.229486,8.034303,-6.927692,-7.247031,8.263712,7.208115,6.462683,2.689121,7.329369,-2.416378,0.160240,7.583457,-7.300646,0.895862,8.565970,9.783684,-1.325435,0.357236,1.076139,6.318848,-3.729983,-2.763596,-0.116219,5.111732,-5.475813,-7.083548,-9.391360,6.958706,3.234028,3.542869,9.723340,8.391201,1.944246,-3.355821,8.271275,0.229859,2.694672,6.984519,4.045198,9.070760,-7.785410,5.497146,-4.068112,-9.597098,2.069450,-3.506682,-7.304907,-6.596735,-5.371546,6.439192,-9.181889,9.748009,-1.005919,7.644162,-5.908065,2.416492,5.176742,5.074254,9.724515,6.228730,0.316341,9.978888,-0.799565,4.954655,4.688760,-8.509472,1.352506,7.059333,-6.482729,7.350011,6.000784,-0.427298,8.095273,-2.052922,4.341284,9.650600,4.536673,-4.869200,6.715021,-4.419557,-9.435375,-6.894881,8.600072,0.945846,8.762831,-3.062641,4.387763,5.479856,-8.108218,-6.560105,4.572726,1.858868,-3.656168,-7.770064,4.874323,-5.854502,5.339204,-3.978762,-2.676043,6.673370,-3.789117,8.562893,-1.950989,9.085881,-5.236115,-1.019572,7.580612,3.814201,1.918622,0.346803,-6.447435,1.651348,1.186047,-2.742827,6.875853,2.225928,5.399667,-1.837947,3.300412,9.002686,0.611309,1.426268,4.609636,-4.292323,6.144957,6.690616,-7.252133,0.097792,-3.573871,5.911361,6.420712,-6.895168,8.660794,-0.231869,-5.955556,5.796511,7.395978,-2.399538,3.324847,-6.991053,7.185369,-9.332021,-7.502343,3.592051,-5.647969,-2.135727,8.110443,-3.258738,0.777435,2.427485,-4.383948,3.182930,7.882211,-9.345777,1.066718,5.939213,3.689374,-5.222039,-2.236055,-0.921792,-4.393900,-9.665085,8.543596,3.688513,-3.838107,-4.314348,3.230808,-7.035445,-3.351682,8.007919,7.522132,-9.923132,-2.470404,-5.725675,-5.823302,5.843054,-2.906256,-1.360436,3.815425,-5.139538,-9.263281,-0.850181,5.261167,-8.335219,-8.420401,0.356719,9.086062,-3.434218,-5.577896,-5.590959,8.658019,1.416035,2.535159,-4.671696,0.979502,-2.045062,5.365474,7.818356,-9.894101,-2.879024,3.023406,-6.925173,2.893438,1.806241,-8.790287,-0.542846,5.555116,1.891607,0.516043,3.033048,-9.565683,-4.483401,3.951598,-7.402048,-3.577156,-2.839981,-2.230305,-4.684222,7.768136,2.434066,0.017360,6.562707,-6.426031,6.768413,-9.037918,-9.401317,1.328121,6.374472,6.802780,-7.854955,-8.324804,9.607855,2.514978,0.936939,4.185292,-2.843003,-1.291386,-0.611492,-4.881733,2.883884,-6.927159,-7.876995,-0.917309,-7.823120,5.360753,9.433136,4.736173,6.971030,-5.298269,0.601197,9.266049,-9.100395,-0.568250,-1.599857,4.028843,4.100234,-6.255029,4.699943,5.444679,-0.623991,-9.327514,6.375190,-9.414898,-2.316127,7.936344,4.406097,-2.756019,-6.500310,-7.751792,8.128353,-2.098921,1.391440,-8.332466,-0.880154,3.574614,9.647652,-9.197040,8.346319,3.033147,-2.964426,-3.948597,4.795125,3.468719,1.548885,9.785525,6.942936,3.399652,-5.029254,2.006663,-1.565101,8.718869,-9.014834,-8.045956,-0.217329,-6.953791,-2.593040,-3.459458,2.492003,7.955327,2.115647,0.400438,6.748917,-0.954630,9.615090,-2.982257,-6.915765,4.288347,3.145277,-0.563200,7.198901,-7.969760,3.900815,2.579755,9.714166,0.676632,0.227698,6.914363,-6.970399,-3.391823,-0.849821,6.593349,-0.477712,8.504999,-7.144872,-5.614730,-3.768894,3.099138,8.735668,-9.546756,4.955622,-9.807389,6.335192,4.225457,6.021068,5.187392,-1.607476,-0.472192,9.220459,2.185612,0.848828,7.730477,-6.217036,-1.371241,9.952219,-7.526925,-2.540104,-8.756521,5.900876,6.660093,1.986366,-1.952933,6.110437,7.197571,-9.926941,-2.315048,-0.540718,-7.235637,-0.227409,-8.670879,9.358300,8.414842,7.503660,5.711018,4.082515,1.146705,4.201897,4.670921,-2.047254,4.487227,8.847939,9.673867,8.843714,-5.389535,-5.085627,-8.843755,-8.780439,4.406302,9.625307,-8.135268,-0.751455,2.803609,1.525980,-9.841313,7.862994,-8.796789,-8.279932,-8.907400,1.911513,8.084662,-8.424103,-8.725737,3.061435,-4.406495,-9.272651,-1.928445,9.020846,8.795536,-3.823490,-2.349969,4.165861,-4.598342,-6.487866,-6.421795,4.934549,9.019467,1.000438,-0.014865,-0.214906,3.523906,1.945061,8.361243,9.848613,9.826322,-4.806579,-6.962187,0.820943,2.433562,0.535786,1.231320,-2.132282,-2.942424,-8.226751,-2.810944,-6.812679,-6.579893,3.761597,-2.799902,-6.224413,-6.095180,1.223408,-4.166083,2.733915,4.167019,1.146787,-3.275317,2.895483,5.012784,0.517597,-5.004629,8.986270,-7.088871,-3.777744,-0.718565,-0.670769,-8.930670,1.145331,-3.737133,-4.384965,9.914712,9.056084,4.329008,9.553347,-1.969098,9.114726,-3.467857,2.627642,7.938788,9.160549,-8.304632,8.091347,8.167695,-9.371432,7.123415,0.806183,-0.147907,-6.412770,-0.403820,0.367893,4.814054,2.084271,3.352300,-7.210355,3.612307,-4.804461,9.657262,-5.549963,-3.667623,0.266338,2.464031,2.409690,3.773189,-3.236206,6.683459,-0.161494,-5.906673,-8.029097,5.813288,-9.548050,-6.579806,-1.329166,-7.024412,-1.541544,2.251331,7.413061,3.926200,5.235948,-6.385967,-6.260298,8.125717,-1.216790,-8.147969,1.442401,8.080738,-6.662395,9.022849,-6.291874,1.183828,-2.607625,-7.445325,-3.381780,-5.146740,-3.749200,0.661447,-6.706344,9.195084,-9.908145,1.369381,7.137498,3.656886,-6.029211,8.414517,5.123400,-8.711937,8.633948,9.967351,-4.531327,6.208740,-2.381657,8.059503,1.244745,-9.344315,-6.133143,-6.040577,-3.508655,-4.122335,-6.451154,5.684600,-4.608074,0.697130,-3.182727,5.760240,9.134743,7.550191,4.761669,-5.862079,-9.865148,-5.948047,2.861713,-7.015755,0.179810,-8.377489,-0.636933,5.807701,2.328444,4.457171,1.444259,-1.332542,0.159641,-4.385355,-9.516696,-5.749082,3.997158,-3.320505,3.494697,0.748036,4.393982,-1.745923,2.838088,-2.238111,-4.204180,7.618748,2.875150,-0.434989,7.894303,9.853704,-8.601907,-6.766665,2.035711,-3.503567,-1.526986,1.566568,2.890734,4.984535,6.549999,-9.065825,3.493167,6.150959,6.272246,-3.254327,-3.579646,4.825379,4.012942,5.753470,-9.390485,6.827062,2.888423,-9.336546,-7.020915,6.145972,3.122192,6.150997,2.637293,2.469666,4.695025,-9.551477,-2.533502,-1.631859,0.153810,-4.940543,1.636912,-9.352850,-6.600341,7.260166,7.455527,-3.812713,-6.036775,2.396960,-0.688721,4.771867,-8.147892,4.128907,3.127067,-6.178435,7.925097,-5.083406,-0.391372,1.829306,1.920575,5.448534,-9.579624,8.160336,-3.373168,-5.437825,-4.029030,-9.176805,3.993005,5.801378,6.180442,-0.909507,-0.320453,6.186983,2.818111,9.220024,4.956255,2.522796,-7.449708,1.376337,-5.635420,3.850063,1.763459,3.694253,3.913677,1.427434,7.992833,-1.461566,-7.501164,-0.568374,-6.993981,-6.962091,7.181924,2.102399,-6.167805,-9.986700,9.270469,7.124302,0.835132,0.199907,2.605154,1.300512,-3.757980,-2.167879,1.103499,5.617773,-6.114116,8.470215,3.558868,2.503169,4.245527,-1.439126,2.822437,6.738334,9.938179,-8.547113,9.639032,9.288487,0.331542,-3.001371,-5.240121,-2.045499,6.891145,-1.292404,1.218606,4.763695,4.198626,6.013175,0.071364,1.358101,5.383820,-2.469102,1.804632,4.199599,8.314655,6.433565,4.210503,9.371068,-3.975841,0.796376,7.456102,-5.720294,4.398953,-1.189263,7.840675,9.756962,7.244056,9.072028,2.322661,8.310470,7.747292,-0.078211,-6.761591,1.195490,-8.067309,-8.212813,6.851929,-5.153913,-6.398704,-5.703019,0.125278,6.447791,2.640224,0.048128,4.599270,6.016366,-2.919361,1.270801,9.082599,3.615520,8.244751,-6.871535,-4.826515,9.124133,6.435518,-0.308795,4.284945,8.763969,3.638776,4.646732,4.292957,6.049105,4.471189,-1.266105,5.073127,-2.482580,-0.547835,-2.416134,0.830275,5.720158,8.112322,2.226715,4.392973,1.952054,-4.320001,5.190585,4.519192,2.356421,5.422420,-9.844418,9.525537,-2.236973,0.798699,-7.814709,-6.549967,7.046445,-3.407034,0.947856,3.864858,-5.856759,1.338061,0.916430,-1.650756,5.138264,-7.959396,-9.782659,-1.165625,8.692196,5.324338,4.620329,-6.261181,8.235619,6.459597,-3.449053,9.935430,-3.291894,9.070685,-2.276051,-9.361451,7.414106,3.755711,-8.538814,-9.402868,6.569067,-1.999117,-3.009657,9.768805,3.888454,-0.716550,9.927069,-1.310354,-7.210500,3.052418,5.559939,4.890779,-8.099233,-1.368808,-4.096699,3.127049,8.437996,-6.264045,-6.828843,1.457325,2.961148,8.523139,-2.939289,-3.297003,8.608211,8.992622,-1.630373,-6.315708,7.826959,8.840359,2.797478,7.706484,-2.580113,-9.590117,0.054269,-8.420877,4.369176,2.545281,2.983434,7.558751,3.235065,8.072178,8.193061,-0.985742,8.420778,-0.584013,-1.957566,2.263774,-6.928902,0.979906,9.376992,-3.135347,-7.687050,-8.751755,8.774473,-2.291846,-2.094584,-7.087478,2.301447,-1.834719,7.220423,-4.933567,-2.087366,-7.733310,8.047848,-5.654346,-0.564536,-8.921179,-4.645122,-3.554169,-4.946343,-0.995250,9.691706,-7.931229,-6.114503,9.427319,1.704931,4.998572,4.833879,-5.841631,-2.860118,6.782188,3.144626,7.323069,3.769161,-7.347162,-5.973796,-6.657757,0.758025,4.207870,-7.802422,6.908121,-8.549272,4.525601,9.492278,-0.912011,4.848566,-4.904484,4.917774,-8.288806,7.888154,-3.239469,-2.922581,7.591451,5.293099,1.549041,1.784436,-8.728809,2.819059,4.202786,2.800904,-9.692833,-6.518643,-1.226801,-0.207106,-3.696663,9.189683,-4.188813,6.276231,6.993671,-1.659346,-7.835185,-4.560002,7.045794,0.419548,-3.501320,-2.373599,5.052897,7.406522,8.895852,-4.980572,1.884581,-4.700727], dtype = "float32")#candidate|3399|(3072,)|const|float32
bop_3400 = relay.divide(var_3391.astype('float64'), relay.reshape(const_3399.astype('float64'), relay.shape_of(var_3391))) # shape=(3072,)
output = relay.Tuple([call_3363,const_3364,bop_3367,call_3373,call_3378,var_3379,call_3390,const_3392,var_3393,bop_3400,])
output2 = relay.Tuple([call_3365,const_3364,bop_3370,call_3374,call_3380,var_3379,call_3394,const_3392,var_3393,bop_3400,])
func_3406 = relay.Function([var_3379,var_3391,var_3393,], output)
mod['func_3406'] = func_3406
mod = relay.transform.InferType()(mod)
mutated_mod['func_3406'] = func_3406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3406_call = mutated_mod.get_global_var('func_3406')
var_3408 = relay.var("var_3408", dtype = "uint8", shape = (96,))#candidate|3408|(96,)|var|uint8
var_3409 = relay.var("var_3409", dtype = "float32", shape = (3072,))#candidate|3409|(3072,)|var|float32
var_3410 = relay.var("var_3410", dtype = "float32", shape = (550,))#candidate|3410|(550,)|var|float32
call_3407 = func_3406_call(var_3408,var_3409,var_3410,)
output = call_3407
func_3411 = relay.Function([var_3408,var_3409,var_3410,], output)
mutated_mod['func_3411'] = func_3411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_3418 = relay.TupleGetItem(func_573_call(), 0)
call_3419 = relay.TupleGetItem(func_574_call(), 0)
output = relay.Tuple([call_3418,])
output2 = relay.Tuple([call_3419,])
func_3429 = relay.Function([], output)
mod['func_3429'] = func_3429
mod = relay.transform.InferType()(mod)
mutated_mod['func_3429'] = func_3429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3429_call = mutated_mod.get_global_var('func_3429')
call_3430 = func_3429_call()
output = call_3430
func_3431 = relay.Function([], output)
mutated_mod['func_3431'] = func_3431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_3476 = relay.TupleGetItem(func_1830_call(), 1)
call_3477 = relay.TupleGetItem(func_1831_call(), 1)
output = call_3476
output2 = call_3477
func_3478 = relay.Function([], output)
mod['func_3478'] = func_3478
mod = relay.transform.InferType()(mod)
mutated_mod['func_3478'] = func_3478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3478_call = mutated_mod.get_global_var('func_3478')
call_3479 = func_3478_call()
output = call_3479
func_3480 = relay.Function([], output)
mutated_mod['func_3480'] = func_3480
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3499 = relay.var("var_3499", dtype = "uint32", shape = ())#candidate|3499|()|var|uint32
var_3500 = relay.var("var_3500", dtype = "uint32", shape = (8, 6, 1))#candidate|3500|(8, 6, 1)|var|uint32
bop_3501 = relay.not_equal(var_3499.astype('bool'), var_3500.astype('bool')) # shape=(8, 6, 1)
func_510_call = mod.get_global_var('func_510')
func_512_call = mutated_mod.get_global_var('func_512')
call_3504 = relay.TupleGetItem(func_510_call(), 0)
call_3505 = relay.TupleGetItem(func_512_call(), 0)
output = relay.Tuple([bop_3501,call_3504,])
output2 = relay.Tuple([bop_3501,call_3505,])
func_3509 = relay.Function([var_3499,var_3500,], output)
mod['func_3509'] = func_3509
mod = relay.transform.InferType()(mod)
mutated_mod['func_3509'] = func_3509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3509_call = mutated_mod.get_global_var('func_3509')
var_3511 = relay.var("var_3511", dtype = "uint32", shape = ())#candidate|3511|()|var|uint32
var_3512 = relay.var("var_3512", dtype = "uint32", shape = (8, 6, 1))#candidate|3512|(8, 6, 1)|var|uint32
call_3510 = func_3509_call(var_3511,var_3512,)
output = call_3510
func_3513 = relay.Function([var_3511,var_3512,], output)
mutated_mod['func_3513'] = func_3513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_747_call = mod.get_global_var('func_747')
func_749_call = mutated_mod.get_global_var('func_749')
call_3551 = func_747_call()
call_3552 = func_747_call()
uop_3571 = relay.acos(call_3551.astype('float64')) # shape=(2, 5, 8)
uop_3573 = relay.acos(call_3552.astype('float64')) # shape=(2, 5, 8)
func_1093_call = mod.get_global_var('func_1093')
func_1096_call = mutated_mod.get_global_var('func_1096')
const_3584 = relay.const([-5.897039,1.411442,-7.059113,7.336407,-7.395496,-1.541609,3.091729,6.084209,-6.841541,-7.887522,-8.201799,-9.289947,7.951552,-1.946465,-7.899675,-1.295817,5.774342,-3.013188,1.817904,-8.359859,0.470556,-4.646305,6.971967,-1.523690,-2.682870,-1.192626,-1.424950,-8.202849,4.384845,-2.035902,2.956098,-0.856195,9.365924,-1.541007,4.111446,-0.791903,-9.694940,0.674545,7.367142,1.007176,-0.846914,-2.388630,-1.318265,-6.947996,9.873175,4.560989,-7.773830,0.463235,-5.878739,-9.730564,-6.165426,-5.186285,-3.623301,5.687360,-0.875518,0.525500,-8.243973,6.924913,-7.777567,-7.886137,-2.223839,-8.311065,-9.865966,-3.784104,-6.363083,-6.342798,-2.635347,1.435803,-8.255531,-1.333007,7.129146,5.258145,5.405837,-5.122490,5.804890,3.406696,-1.649197,-3.108099,3.903764,-5.128431,0.188127,-8.049265,9.215596,-5.879200,-5.509860,-0.761378,-7.159145,3.191802,-5.942106,0.928958,3.450265,-8.700896,4.478965,-6.276001,8.128104,-0.106076,5.500705,-2.697740,-9.377292,-0.359208,1.845639,-1.414372,-6.137659,8.406101,8.370413,-1.173846,0.449105,-9.805193,5.599158,2.708960,3.939644,-7.352891,3.746242,-1.878838,4.904927,-5.003924,2.896015,1.615780,6.642666,3.001974,0.395415,1.351427,-6.893105,7.047207,-0.560371,-2.762101,-3.815588,-5.039654,-4.541012,7.584367,8.957184,-1.132067,-0.872929,-8.429179,9.250171,-3.165430,-1.066699,2.075931,-4.715631,-7.616286,-6.944712,-3.579111,0.124948,-3.085161,6.949522,-0.105304,6.312877,-2.273515,-2.542458,0.990743,-4.745161,-6.208785,1.920026,5.013522,8.423127,-0.859623,-1.335998,-8.767840,0.821836,0.279771,4.112598,8.264520,4.948777,-5.413857,9.230717,6.529334,-7.334387,-3.892582,4.751355,4.743085,2.584488,-7.734559,-8.300387,-3.476584,0.455713,3.287641,4.067824,-2.419981,-7.748392,-5.905889,-9.396049,2.960450,3.003803,2.265574,9.716314,8.897419,-5.203016,-9.025304,6.136433,2.508087,2.719861,7.849156,1.962468,0.279133,-5.796949,4.494774,1.638871,2.304922,-9.043250,2.349495,1.103225,1.797868,9.143652,6.806658,-6.636215,2.279613,3.285828,-3.717568,-0.001384,-4.861428,2.247730,-8.396874,-0.590365,4.746202,-9.354267,-3.304721,-4.059187,2.885128,6.310015,-2.593013,7.591005,3.448481,-6.708928,-3.781980,4.678877,5.626745,-2.922869,5.236466,-3.682825,-8.013563,-4.819094,-3.202003,-6.642820,-2.514486,-4.814366,6.595946,-6.090174,-8.604638,-6.370023,-5.253930,0.072242,-8.900481,2.586875,-1.230922,-4.315910,-1.133765,4.717087,2.645947,-9.087224,-5.284424,-8.230198,3.670541,-1.455750,9.480073,-4.286753,0.207618,-3.346025,8.593572,6.198710,1.949183,-4.679851,-8.596639,-8.560627,0.562563,4.166995,-1.012134,8.571259,2.342250,4.900535,-6.913157,-9.037344,-1.758253,0.567636,-2.529261,3.852084,5.336048,6.374696,-9.244826,6.510143,-6.205143,4.576542,3.459244,-4.669730,-7.608771,6.448931,5.738280,-2.779174,-6.371281,-7.159214,8.410806,-7.688971,6.135459,-5.121431,-2.368394,-4.024977,2.560425,0.785975,-8.777741,0.699080,1.319886,-8.680159,-1.007189,-2.196231,-6.499485,8.429987,3.624731,-9.482918,5.020398,-0.206257,8.157872,-3.417504,-4.156431,0.091306,-3.977747,2.532383,6.555830,-0.492198,9.302269,4.930754,7.835754,7.898818,-1.681511,-7.605020,-5.380181,5.593385,5.147824,-9.375900,1.758003,-3.373858,-2.920205,-2.548732,5.836179,7.540314,1.808096,9.575811,5.456560,2.968132,-5.706471,5.875334,-5.246196,-9.107370,1.556945,6.044711,-1.767961,-1.717874,-1.416510,1.885055,2.703686,-8.537123,3.916726,-4.447690,-8.678148,-0.109255,5.899520,1.759049,9.709233,2.083484,5.417600,7.874251,-2.407535,-3.446872,-2.800847,2.330174,0.478993,1.582648,5.966772,5.341094,8.427731,-5.796984,-5.037407,1.483131,-7.370555,-7.627563,1.029880,0.718947,4.173164,-5.416739,4.673400,7.300896,7.672194,3.147311,-9.458251,-6.112011,9.917727], dtype = "float64")#candidate|3584|(384,)|const|float64
call_3583 = relay.TupleGetItem(func_1093_call(relay.reshape(const_3584.astype('float64'), [8, 6, 8])), 1)
call_3585 = relay.TupleGetItem(func_1096_call(relay.reshape(const_3584.astype('float64'), [8, 6, 8])), 1)
func_1093_call = mod.get_global_var('func_1093')
func_1096_call = mutated_mod.get_global_var('func_1096')
call_3587 = relay.TupleGetItem(func_1093_call(relay.reshape(const_3584.astype('float64'), [8, 6, 8])), 1)
call_3588 = relay.TupleGetItem(func_1096_call(relay.reshape(const_3584.astype('float64'), [8, 6, 8])), 1)
func_3045_call = mod.get_global_var('func_3045')
func_3046_call = mutated_mod.get_global_var('func_3046')
call_3591 = relay.TupleGetItem(func_3045_call(), 0)
call_3592 = relay.TupleGetItem(func_3046_call(), 0)
func_2365_call = mod.get_global_var('func_2365')
func_2367_call = mutated_mod.get_global_var('func_2367')
call_3593 = relay.TupleGetItem(func_2365_call(), 0)
call_3594 = relay.TupleGetItem(func_2367_call(), 0)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_3597 = func_587_call()
call_3598 = func_587_call()
output = relay.Tuple([uop_3571,call_3583,const_3584,call_3587,call_3591,call_3593,call_3597,])
output2 = relay.Tuple([uop_3573,call_3585,const_3584,call_3588,call_3592,call_3594,call_3598,])
func_3599 = relay.Function([], output)
mod['func_3599'] = func_3599
mod = relay.transform.InferType()(mod)
output = func_3599()
func_3600 = relay.Function([], output)
mutated_mod['func_3600'] = func_3600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_3619 = func_587_call()
call_3620 = func_587_call()
var_3635 = relay.var("var_3635", dtype = "float32", shape = (2, 5, 8))#candidate|3635|(2, 5, 8)|var|float32
bop_3636 = relay.bitwise_or(call_3619.astype('int8'), relay.reshape(var_3635.astype('int8'), relay.shape_of(call_3619))) # shape=(2, 5, 8)
bop_3639 = relay.bitwise_or(call_3620.astype('int8'), relay.reshape(var_3635.astype('int8'), relay.shape_of(call_3620))) # shape=(2, 5, 8)
func_2338_call = mod.get_global_var('func_2338')
func_2340_call = mutated_mod.get_global_var('func_2340')
call_3677 = func_2338_call()
call_3678 = func_2338_call()
output = relay.Tuple([bop_3636,call_3677,])
output2 = relay.Tuple([bop_3639,call_3678,])
func_3680 = relay.Function([var_3635,], output)
mod['func_3680'] = func_3680
mod = relay.transform.InferType()(mod)
mutated_mod['func_3680'] = func_3680
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3681 = relay.var("var_3681", dtype = "float32", shape = (2, 5, 8))#candidate|3681|(2, 5, 8)|var|float32
func_3680_call = mutated_mod.get_global_var('func_3680')
call_3682 = func_3680_call(var_3681)
output = call_3682
func_3683 = relay.Function([var_3681], output)
mutated_mod['func_3683'] = func_3683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_3704 = relay.TupleGetItem(func_2017_call(), 0)
call_3705 = relay.TupleGetItem(func_2018_call(), 0)
output = relay.Tuple([call_3704,])
output2 = relay.Tuple([call_3705,])
func_3741 = relay.Function([], output)
mod['func_3741'] = func_3741
mod = relay.transform.InferType()(mod)
mutated_mod['func_3741'] = func_3741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3741_call = mutated_mod.get_global_var('func_3741')
call_3742 = func_3741_call()
output = call_3742
func_3743 = relay.Function([], output)
mutated_mod['func_3743'] = func_3743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3749 = relay.var("var_3749", dtype = "float64", shape = (3, 13, 9))#candidate|3749|(3, 13, 9)|var|float64
uop_3750 = relay.atanh(var_3749.astype('float64')) # shape=(3, 13, 9)
func_1911_call = mod.get_global_var('func_1911')
func_1912_call = mutated_mod.get_global_var('func_1912')
call_3760 = relay.TupleGetItem(func_1911_call(), 0)
call_3761 = relay.TupleGetItem(func_1912_call(), 0)
func_1124_call = mod.get_global_var('func_1124')
func_1127_call = mutated_mod.get_global_var('func_1127')
var_3764 = relay.var("var_3764", dtype = "float64", shape = (6, 64))#candidate|3764|(6, 64)|var|float64
call_3763 = relay.TupleGetItem(func_1124_call(relay.reshape(var_3764.astype('float64'), [384,])), 2)
call_3765 = relay.TupleGetItem(func_1127_call(relay.reshape(var_3764.astype('float64'), [384,])), 2)
uop_3769 = relay.cos(uop_3750.astype('float64')) # shape=(3, 13, 9)
output = relay.Tuple([call_3760,call_3763,var_3764,uop_3769,])
output2 = relay.Tuple([call_3761,call_3765,var_3764,uop_3769,])
func_3771 = relay.Function([var_3749,var_3764,], output)
mod['func_3771'] = func_3771
mod = relay.transform.InferType()(mod)
var_3772 = relay.var("var_3772", dtype = "float64", shape = (3, 13, 9))#candidate|3772|(3, 13, 9)|var|float64
var_3773 = relay.var("var_3773", dtype = "float64", shape = (6, 64))#candidate|3773|(6, 64)|var|float64
output = func_3771(var_3772,var_3773,)
func_3774 = relay.Function([var_3772,var_3773,], output)
mutated_mod['func_3774'] = func_3774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2280_call = mod.get_global_var('func_2280')
func_2282_call = mutated_mod.get_global_var('func_2282')
call_3821 = func_2280_call()
call_3822 = func_2280_call()
func_2485_call = mod.get_global_var('func_2485')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_3831 = relay.TupleGetItem(func_2485_call(), 0)
call_3832 = relay.TupleGetItem(func_2487_call(), 0)
output = relay.Tuple([call_3821,call_3831,])
output2 = relay.Tuple([call_3822,call_3832,])
func_3842 = relay.Function([], output)
mod['func_3842'] = func_3842
mod = relay.transform.InferType()(mod)
mutated_mod['func_3842'] = func_3842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3842_call = mutated_mod.get_global_var('func_3842')
call_3843 = func_3842_call()
output = call_3843
func_3844 = relay.Function([], output)
mutated_mod['func_3844'] = func_3844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3091_call = mod.get_global_var('func_3091')
func_3093_call = mutated_mod.get_global_var('func_3093')
call_3867 = relay.TupleGetItem(func_3091_call(), 0)
call_3868 = relay.TupleGetItem(func_3093_call(), 0)
output = relay.Tuple([call_3867,])
output2 = relay.Tuple([call_3868,])
func_3889 = relay.Function([], output)
mod['func_3889'] = func_3889
mod = relay.transform.InferType()(mod)
output = func_3889()
func_3890 = relay.Function([], output)
mutated_mod['func_3890'] = func_3890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1911_call = mod.get_global_var('func_1911')
func_1912_call = mutated_mod.get_global_var('func_1912')
call_3952 = relay.TupleGetItem(func_1911_call(), 0)
call_3953 = relay.TupleGetItem(func_1912_call(), 0)
output = call_3952
output2 = call_3953
func_3960 = relay.Function([], output)
mod['func_3960'] = func_3960
mod = relay.transform.InferType()(mod)
mutated_mod['func_3960'] = func_3960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3960_call = mutated_mod.get_global_var('func_3960')
call_3961 = func_3960_call()
output = call_3961
func_3962 = relay.Function([], output)
mutated_mod['func_3962'] = func_3962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3842_call = mod.get_global_var('func_3842')
func_3844_call = mutated_mod.get_global_var('func_3844')
call_3975 = relay.TupleGetItem(func_3842_call(), 0)
call_3976 = relay.TupleGetItem(func_3844_call(), 0)
output = relay.Tuple([call_3975,])
output2 = relay.Tuple([call_3976,])
func_3990 = relay.Function([], output)
mod['func_3990'] = func_3990
mod = relay.transform.InferType()(mod)
mutated_mod['func_3990'] = func_3990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3990_call = mutated_mod.get_global_var('func_3990')
call_3991 = func_3990_call()
output = call_3991
func_3992 = relay.Function([], output)
mutated_mod['func_3992'] = func_3992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1450_call = mod.get_global_var('func_1450')
func_1452_call = mutated_mod.get_global_var('func_1452')
call_4008 = func_1450_call()
call_4009 = func_1450_call()
output = call_4008
output2 = call_4009
func_4010 = relay.Function([], output)
mod['func_4010'] = func_4010
mod = relay.transform.InferType()(mod)
mutated_mod['func_4010'] = func_4010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4010_call = mutated_mod.get_global_var('func_4010')
call_4011 = func_4010_call()
output = call_4011
func_4012 = relay.Function([], output)
mutated_mod['func_4012'] = func_4012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1554_call = mod.get_global_var('func_1554')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_4170 = relay.TupleGetItem(func_1554_call(), 0)
call_4171 = relay.TupleGetItem(func_1556_call(), 0)
output = call_4170
output2 = call_4171
func_4172 = relay.Function([], output)
mod['func_4172'] = func_4172
mod = relay.transform.InferType()(mod)
mutated_mod['func_4172'] = func_4172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4172_call = mutated_mod.get_global_var('func_4172')
call_4173 = func_4172_call()
output = call_4173
func_4174 = relay.Function([], output)
mutated_mod['func_4174'] = func_4174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_4211 = relay.TupleGetItem(func_573_call(), 0)
call_4212 = relay.TupleGetItem(func_574_call(), 0)
func_2017_call = mod.get_global_var('func_2017')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_4215 = relay.TupleGetItem(func_2017_call(), 0)
call_4216 = relay.TupleGetItem(func_2018_call(), 0)
func_2017_call = mod.get_global_var('func_2017')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_4217 = relay.TupleGetItem(func_2017_call(), 0)
call_4218 = relay.TupleGetItem(func_2018_call(), 0)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_4219 = relay.TupleGetItem(func_1830_call(), 0)
call_4220 = relay.TupleGetItem(func_1831_call(), 0)
func_1791_call = mod.get_global_var('func_1791')
func_1795_call = mutated_mod.get_global_var('func_1795')
var_4227 = relay.var("var_4227", dtype = "float32", shape = (550,))#candidate|4227|(550,)|var|float32
call_4226 = func_1791_call(relay.reshape(var_4227.astype('float32'), [5, 10, 11]), relay.reshape(var_4227.astype('float32'), [5, 10, 11]), )
call_4228 = func_1791_call(relay.reshape(var_4227.astype('float32'), [5, 10, 11]), relay.reshape(var_4227.astype('float32'), [5, 10, 11]), )
func_1911_call = mod.get_global_var('func_1911')
func_1912_call = mutated_mod.get_global_var('func_1912')
call_4230 = relay.TupleGetItem(func_1911_call(), 0)
call_4231 = relay.TupleGetItem(func_1912_call(), 0)
uop_4242 = relay.erf(call_4217.astype('float32')) # shape=(2, 5, 8)
uop_4244 = relay.erf(call_4218.astype('float32')) # shape=(2, 5, 8)
output = relay.Tuple([call_4211,call_4215,call_4219,call_4226,var_4227,call_4230,uop_4242,])
output2 = relay.Tuple([call_4212,call_4216,call_4220,call_4228,var_4227,call_4231,uop_4244,])
func_4245 = relay.Function([var_4227,], output)
mod['func_4245'] = func_4245
mod = relay.transform.InferType()(mod)
mutated_mod['func_4245'] = func_4245
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4246 = relay.var("var_4246", dtype = "float32", shape = (550,))#candidate|4246|(550,)|var|float32
func_4245_call = mutated_mod.get_global_var('func_4245')
call_4247 = func_4245_call(var_4246)
output = call_4247
func_4248 = relay.Function([var_4246], output)
mutated_mod['func_4248'] = func_4248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3599_call = mod.get_global_var('func_3599')
func_3600_call = mutated_mod.get_global_var('func_3600')
call_4255 = relay.TupleGetItem(func_3599_call(), 6)
call_4256 = relay.TupleGetItem(func_3600_call(), 6)
func_3066_call = mod.get_global_var('func_3066')
func_3068_call = mutated_mod.get_global_var('func_3068')
const_4262 = relay.const([-9.255527,2.772418,6.309022,8.015860,-5.324109,6.974219,-5.125734,4.937358,-2.432219,-9.663108,3.380871,-8.029014,0.912461,-2.067999,-5.005557,7.662542,-8.038178,-5.949999,6.572098,-7.001853,5.745444,8.002334,2.449715,-4.277405,-7.622459,3.045792,-5.865969,-2.681961,-5.220938,3.810776,8.849311,9.991587,0.206300,3.416857,5.290842,6.060009,7.855226,0.006419,2.591690,5.621203,-0.456447,4.315636,-8.049030,-8.428921,-5.741695,3.588890,-8.805869,9.435796,5.007166,-2.126193,-1.387514,8.888386,-8.182692,-2.958166,-1.599909,-0.653327,-2.804160,-2.762448,7.178866,7.429650,-6.248943,0.982113,-5.042585,-7.883865,-5.368058,-3.489577,-9.752483,-9.568794,-2.795464,-6.138857,-4.291798,4.819241,-9.606684,-7.645891,1.513739,6.163838,-5.983241,-7.988370,5.983215,-9.265143,-9.310510,7.270111,4.424218,1.597587,-0.497611,-4.242898,-6.101621,-8.832457,4.727556,1.804442,-4.963901,-8.265486,3.770704,6.956637,-0.590368,-3.647912,4.671679,0.861393,-8.478961,-0.450688,7.748029,9.559560,5.141155,-0.164479,-3.912763,3.591554,9.330312,-7.546318,-6.999735,1.927461,3.710206,0.062047,2.022976,5.601657,-7.984046,2.784127,4.913218,3.788215,-6.331213,3.383971,2.235989,2.341527,4.309581,-0.119034,-5.484254,-2.123416,9.813850,-4.214260,-6.079577,-6.316788,3.184611,-0.962734,2.491903,3.008382,-0.180218,-8.383887,8.137303,-5.298395,2.512643,6.409231,-8.411064,-0.649912,8.362452,9.687325,-9.289787,-1.471336,7.592228,-8.836633,5.815509,-6.415658,4.936518,7.013787,-6.688542,1.598962,-4.482398,4.739664,-7.065130,5.827826,-7.520081,3.810406,-5.365275,6.785653,2.497169,-5.166645,4.413476,-3.727961,-4.991032,-1.768402,3.779087,-4.121775,-2.308422,-8.328993,9.569624,-5.747497,-2.799213,0.510252,-0.643306,-2.473489,-5.735800,-7.274639,4.732280,-0.642088,-0.478359,9.568227,-4.548732,-6.658893,1.008311,0.478401,-2.458632,2.840241,-3.511204,1.795848,6.198113,-5.932024,4.886697,2.295176,6.788317,-1.197819,-5.762561,0.076388,0.189633,1.638758,-9.474820,-3.349411,6.343939,-6.194999,-7.558368,-0.888035,0.147912,8.948498,3.026746,-3.401505,2.606838,-7.598848,-7.997024,-1.618362,6.434718,-0.800895,0.840062,-9.928529,-7.222553,-5.253717,0.148539,-6.182806,8.676046,3.535892,2.721622,4.818551,-2.564118,-8.259036,9.392715,-7.446558,1.902795,-9.229633,0.911264,7.563498,7.861006,-8.381844,-4.728908,-2.577519,4.871216,-3.964381,1.199718,7.118905,6.539067,-2.488200,-7.810162,-1.246767,4.269023,-1.677419,2.723122,0.792041,3.250527,1.643400,-7.462666,8.534241,1.053033,-3.752075,5.413888,-7.234738,-5.405952,5.988190,-1.400091,-7.376187,6.106813,-8.417050,-1.850023,9.387701,-3.032563,2.681351,-5.999022,-7.760181,-6.047340,-4.259895,-2.851172,-5.490617,1.842738,0.776451,1.247480,-4.297119,4.089482,-9.073970,-0.514524,9.702584,-3.329154,4.077634,-2.519920,1.812001,8.759214,-3.797830,-9.022166,-8.344620,8.871326,0.558296,8.797192,3.331030,9.588646,-6.349896,8.805236,-7.747719,-1.982351,7.593572,2.313234,8.513233,-0.774849,-9.498794,-3.956034,5.681005,-7.992888,7.292016,-8.694993,-8.935067,-9.196664,3.700624,7.381605,3.412309,6.709078,-0.936066,6.921122,8.091524,3.286763,6.200579,-0.138193,6.773625,7.357717,-9.564116,9.159208,3.859664,3.310991,-4.618025,-1.922559,-8.015401,-6.188872,-9.087480,-7.974677,6.193075,3.100782,-0.765985,2.774117,8.550281,-9.894878,-2.254499,-4.526521,9.815290,-6.522699,-6.061750,4.650032,3.585060,8.622776,-3.236551,3.319258,-2.166026,-6.688383,8.515818,-6.432164,-3.544548,-8.612411,0.853192,4.487422,6.361790,-4.577368,-1.035312,-9.911087,6.109554,-5.088127,-0.857081,1.651276,-0.780418,5.336717,-9.442033,-9.913022,-7.617222,0.941168,-9.020152,-8.422490,6.310542,0.709986,-6.136724,5.104060,-4.360504,6.457993,0.970184,2.602324,-7.621220,4.835614,-6.298460,-9.201947,1.714195,-6.810493,-0.422375,6.974960,7.662196,6.197072,-8.794851,3.141623,-1.538923,5.376254,-0.812540,-6.001060,5.288534,0.688194,5.244235,-1.509294,3.161925,-1.931556,1.598566,5.642733,9.789062,3.960539,0.282616,-5.262925,2.889300,-9.966646,-8.638129,2.894614,-7.050535,3.942103,-2.656520,-4.506019,7.339785,2.617292,-7.325628,3.770704,9.254748,-2.585710,-2.430091,8.691925,-2.983706,0.815405,-5.033134,5.187531,5.106311,-8.551631,-0.957998,4.379176,-2.475319,8.141492,-1.057109,-2.096703,3.860287,-4.078332,7.873235,3.656694,4.587836,-9.260621,5.340013,6.144740,-4.044032,-7.872956,-0.845965,-6.858394,-5.971871,-1.146199,4.123044,8.321481,7.319936,-0.122921,4.509280,-0.218589,-5.077833,-1.503381,-5.466183,-1.673227,7.601560,-6.241378,-9.126759,-3.076848,-7.500244,9.701980,1.028772,-2.192758,4.444535,3.455466,-5.324249,9.652580,-9.778641,4.800488,5.084068,-8.514929,-4.386076,6.315125,3.701176,-8.614976,-1.202127,0.159115,-8.286784,-8.389511,-0.577229,-8.657876,1.555481,8.564376,8.323865,9.688895,-5.528150,9.389544,-7.101079,-3.892951,0.239847,7.793230,-2.593894,7.768535,-7.705901,-8.769636,-3.559787,5.415149,3.956524,6.581216,4.360005,2.966731,-2.423029,9.353309,6.413502,4.429517,-5.203049,-5.535614,6.069680,5.355920,9.518156,0.306063,-9.762374,-5.498539,2.818387,-0.806056,-7.062509,0.066672,-6.318621,1.084759,-0.272497,-7.676937,8.966222,2.572551,6.464356,-7.277260,0.093520,-6.515635,-2.417490,0.680302,-0.767900,6.911137,8.949805,-8.382757,9.145064,-8.695930,-4.184396,-8.335048,3.105715,-0.693976,-2.675745,-8.996181,-5.430536,1.009172,4.745638,5.421971,-9.152353,-7.566682,4.364042,7.638528,-0.563814,-2.729542,6.152108,-7.379551,-9.005090,7.433225,4.741324,-2.402979,-4.846992,-9.736798,-5.034173,3.534618,-6.267839,0.871842,-6.597680,-1.711759,-0.409820,7.385968,4.091073,-3.753246,2.386970,-3.066240,0.779151,-0.868456,-0.240548,7.533799,-9.346223,6.131973,-5.070626,-1.025625,-6.400766,5.141167,1.231767,-5.266121,-0.455649,0.607102,-6.592852,-5.195858,-7.355594,5.145759,-7.809326,-7.538304,2.553408,0.141656,-4.185650,7.211343,4.028216,8.939047,7.043448,8.275234,-1.437303,4.905008,8.575856,6.841542,8.269582,-6.121169,8.749382,-6.914000,7.275023,6.565022,-7.270981,-2.507967,1.461495,-4.613820,6.478714,6.482959,-2.566541,-8.600304,-3.298395,-5.949378,-1.405623,7.352987,1.130450,-2.349157,-4.748575,-4.470193,-5.734752,-2.695646,-6.063746,5.366243,-7.229134,5.959469,1.897442,-2.640793,3.774764,8.828143,-0.666105,-8.139555,9.806105,-7.540562,-1.931133,-0.798506,1.389520,-4.782702,4.126656,2.423075,-0.502355,8.007736,-4.576900,-2.001938,-5.475949,7.711252,-0.270068,-4.271439,-2.051341,2.802307,0.891341,-3.678067,-0.552333,-5.840262,-5.084119,-3.382382,-4.925341,-5.463724,9.729800,1.493851,0.735489,-0.702654,-1.407231,2.590834,1.514869,3.083471,-5.770834,7.268230,-5.041118,-8.768838,0.149841,-6.845640,-7.436463,-5.472741,0.053354,7.493310,-2.358439,-1.248882,-3.858056,-2.167630,8.621454,-2.704997,6.605709,-1.377379,5.072838,-4.510773,6.781950,6.883519,6.146676,-8.254796,4.247770,0.064520,0.926412,-4.966873,4.786113,-1.598191,-4.020305,-8.625813,-8.602894,4.464908,-0.646145,1.651525,-4.766151,3.075906,-2.771137,-1.992045,-7.028642,-4.651207,-5.246378,9.756117,4.948069,-5.809329,1.137431,3.400504,6.872942,3.152364,-6.107256,-6.449519,3.747870,-8.842505,7.070825,0.982738,3.397683,6.638322,-6.783544,8.379811,-0.720040,0.859101,7.217855,-9.834141,-3.284494,-5.655815,-4.654173,6.682806,-0.312511,3.927796,2.609851,2.284419,-7.821882,-5.400208,-5.523563,-9.990673,6.879058,-1.092883,-2.416166,9.697423,-9.783660,9.182835,-2.356872,9.129701,3.719027,-8.826220,2.618155,5.220520,2.898799,5.550909,4.030535,-6.572456,3.184087,6.322630,1.717020,-5.101152,-0.961521,-1.191367,9.644826,-1.606223,0.516011,7.767332,-4.125209,-9.111765,-8.572837,6.565248,-3.980500,-5.013696,-1.539578,9.256696,-9.195208,-1.132455,-1.032657,-9.863550,-6.557209,-4.059029,8.511660,-8.915310,-9.010977,0.372537,-4.195010,-7.931569,5.501450,9.938053,4.048536,0.782450,-4.391088,-0.419773,6.869191,-3.023835,5.919322,7.893203,-6.252539,3.611783,-3.568534,6.181015,4.261698,5.086530,-9.590626,3.544641,-2.550372,-2.274481,-7.152927,6.961032,2.183446,9.110962,-9.717837,8.721002,-5.724685,4.416069,-8.350966,-7.974970,-0.171122,-4.473976,-3.338817,-3.532460,-5.570475,1.891815,-4.544344,-5.501812,8.457045,-0.755317,-6.507681,-4.815821,-2.654110,-9.617483,6.855071,8.939465,-5.502671,-0.929254,3.460576,9.432436,1.858062,-9.827017,8.340142,2.151123,-7.119964,-6.329972,-6.691226,2.109148,-8.381497,2.143119,-6.962767,-8.617074,-1.276236,7.798503,7.816578,2.174467,-8.800271,-7.065590,6.303155,-0.092537,-8.728685,-4.936652,3.887183,1.169326,1.191525,2.217378,9.571996,1.728521,9.305959,1.133984,7.692474,9.514231,-2.956602,-2.511811,-6.680543,1.901224,6.231739,0.775980,-1.011362,3.271639,8.208581,2.400899,-0.830730,-9.886382,-3.921971,-5.615301,-6.172250,3.852634,-0.568424,-6.603078,-7.763188,6.123369,-1.370699,-2.281984,6.310772,-4.837192,5.163361,-9.301574,-4.993703,2.182252,-5.898147,3.179643,3.825363,-4.540390,-4.153547,-0.172649,-1.694980,-3.141476,-7.806266,6.052317,-0.807189,-1.810713,-1.473477,0.432962,5.193689,4.462351,0.136221,0.901362,9.628465,-3.050362,-4.225116,-1.432801,-9.605928,3.265384,7.447365,-0.505938,0.248890,5.005308,9.047692,-6.786522,1.748672,5.946657,-6.520928,-7.301321,-5.393493,0.177341,7.467005,0.333999,0.752984,6.891898,-9.144884,-9.107651,-4.353227,9.634570,8.200381,9.110601,8.684262,6.386705,8.997565,7.243978,-0.992031,-9.177918,-2.945803,2.639391,4.118309,-8.148359,-7.125690,5.929817,8.016747,9.575403,-0.419491,1.047144,9.247895,-5.531883,-9.702740,-2.343737,-9.409332,0.248044,-2.809596,-8.321672,1.947146,9.084875,-8.928949,-2.619075,6.397941,-2.888702,-4.380940,4.258562,-5.901544,-6.847225,4.030465,2.259712,-7.014182,-9.836858,2.829584,-8.279103,-1.210454,-0.074189,-3.570570,-8.330078,-1.616735,8.560489,-3.592482,-8.983291,-6.367657,-9.198215,8.971730,-6.219949,-7.224032,5.332411,8.883658,-9.650836,4.934404,-6.895362,2.793841,-6.004994,3.891408,3.606734,-7.094461,-8.997381,-0.826681,6.805627,-6.910430,8.102352,-0.457189,-7.406307,-8.726622,3.732207,-3.027182,9.009897,-5.445475,7.295043,-9.641552,-2.472981,3.720720,6.997340,1.102526,3.185473,-6.026322,-8.026023,2.694061,0.148033,2.678668,-8.563223,-3.185494,3.473124,1.367767,3.790397,5.725313,-4.110790,-6.309563,3.786759,-2.545359,-2.131445,4.000019,-6.991818,7.491626,5.429907,-4.862592,-2.417151,2.049595,-5.535341,1.196339,-8.031872,5.851998,9.309288,3.059631,5.513769,5.698839,-1.941873,-1.392119,-3.423619,-5.380018,-6.764858,2.616325,-1.881293,-7.108945,9.250617,-4.332197,8.441664,-9.252136,7.927380,3.979947,-1.435076,-5.271485,8.607916,8.867799,4.431431,4.713057,-9.156505,-4.031914,-7.794150,9.273702,-6.798555,6.519769,6.640267,-3.343569,9.377839,3.078070,9.493749,2.720857,-6.528232,-8.639083,-3.444005,9.842588,-1.760827,3.682065,9.520350,-6.022468,-6.077899,5.644010,2.909187,2.470914,8.095261,-5.860852,-5.592418,2.445845,-4.763843,-9.979738,-0.162726,-8.710633,-8.371539,7.432989,-4.272802,3.270150,4.167178,7.431211,0.519327,-0.949138,2.739037,5.790974,-1.647756,9.423263,-2.803749,5.508853,0.996964,4.465682,-7.168198,7.116872,-1.130434,8.948121,9.050216,-7.149126,1.192079,9.527213,-6.037984,5.720437,-3.324067,5.501019,-8.512878,6.222704,-4.498963,0.780178,6.734027,-7.896206,-3.759488,2.644465,-2.601455,-2.023421,-0.375077,-2.258724,-5.557498,8.350714,-1.711694,9.537752,-2.710591,0.283120,2.403839,3.592204,9.650223,-2.305269,6.971141,-9.315970,7.900234,-5.816129,-6.644625,-2.774323,-4.427928,8.524243,2.324666,7.727096,3.131492,-8.946435,-9.255143,0.325874,7.256791,7.662077,-1.438874,-2.290567,-3.103268,9.846206,-4.044687,5.855440,-1.200137,1.342129,6.326373,2.009962,6.206162,2.208813,1.728636,-3.236620,-3.091177,1.334569,9.547715,-6.471020,-4.203679,-6.507754,-2.848298,5.294867,0.342832,-9.255133,-0.170121,3.523903,4.859884,0.495897,-5.774975,-6.531456,3.880056,3.418965,4.872632,-7.784207,0.349058,-3.829898,-5.878928,-9.914881,3.859333,-2.852411,-4.185180,8.294914,-2.290362,-9.970501,-0.050121,2.017968,0.817159,-1.939528,-6.254539,-0.177750,-6.702804,1.091384,7.209365,-7.217191,-2.034332,-9.812832,-8.458767,7.819525,-6.244497,8.670057,-5.217815,-3.667322,8.852786,-8.578641,0.096460,-3.560464,-8.665300,-8.700678,5.583859,-4.799038,7.720023,7.323480,-9.405695,-2.311904,-1.340735,-6.808878,-4.604015,-2.070926,3.369812,9.892146,-2.198252,-4.395689,-7.636973,-7.855788,8.528663,9.372081,3.694711,9.122552,3.623298,-7.851867,0.851439,-6.312373,2.671710,-8.042043,-0.267443,7.108268,1.421033,6.385490,-1.253505,7.162814,-8.940373,-9.933018,3.005363,2.727958,3.088682,5.432646,-8.667538,-0.264968,-4.502865,4.952534,-4.383174,8.208462,-6.468797,0.701139,-2.285611,7.078949,-8.584723,-4.292614,3.621937,-0.752795,2.839992,4.981538,-2.245063,7.849086,-4.530198,7.223785,5.329674,-8.089982,7.850416,-1.056561,9.232990,-3.047070,4.754654,6.407748,-2.206752,3.609017,6.389912,-6.458174,-3.854862,4.977225,-4.100800,-4.604726,0.052068,0.638856,-2.047017,8.550938,7.648815,3.000027,-7.141826,0.418288,6.957683,5.704996,-0.319514,-5.199763,9.920589,2.690756,-0.381821,-4.742059,3.875030,-7.369182,9.731136,4.748427], dtype = "float64")#candidate|4262|(1350,)|const|float64
call_4261 = func_3066_call(relay.reshape(const_4262.astype('float64'), [9, 10, 15]))
call_4263 = func_3066_call(relay.reshape(const_4262.astype('float64'), [9, 10, 15]))
output = relay.Tuple([call_4255,call_4261,const_4262,])
output2 = relay.Tuple([call_4256,call_4263,const_4262,])
func_4281 = relay.Function([], output)
mod['func_4281'] = func_4281
mod = relay.transform.InferType()(mod)
output = func_4281()
func_4282 = relay.Function([], output)
mutated_mod['func_4282'] = func_4282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_4299 = func_1609_call()
call_4300 = func_1609_call()
output = call_4299
output2 = call_4300
func_4304 = relay.Function([], output)
mod['func_4304'] = func_4304
mod = relay.transform.InferType()(mod)
output = func_4304()
func_4305 = relay.Function([], output)
mutated_mod['func_4305'] = func_4305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3045_call = mod.get_global_var('func_3045')
func_3046_call = mutated_mod.get_global_var('func_3046')
call_4382 = relay.TupleGetItem(func_3045_call(), 1)
call_4383 = relay.TupleGetItem(func_3046_call(), 1)
func_1554_call = mod.get_global_var('func_1554')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_4404 = relay.TupleGetItem(func_1554_call(), 0)
call_4405 = relay.TupleGetItem(func_1556_call(), 0)
func_293_call = mod.get_global_var('func_293')
func_298_call = mutated_mod.get_global_var('func_298')
var_4413 = relay.var("var_4413", dtype = "int64", shape = ())#candidate|4413|()|var|int64
const_4414 = relay.const([-3,-1,7,-8,-2,5,-6,2,1,10,9,9,-3,10,-6,-5,-3,10,10,2,-6,7,-4,-10,9,4,-7,9,-5,-9,-9,-2,3,-4,-7,5,1,-7,-3,1,-9,1,9,-6,-7,5,-9,10,-10,5,9,3,3,7,7,7,3,9,-6,-4,10,-10,-10,-3,5,8,-7,5,10,-4,-8,-2,1,-2,-10,1,-10,1,1,10,9,9,-8,-3,-4,7,10,-4,-5,-9,5,-5,8,4,-9,5,-2,-5,7,-1,7,-7,-9,9,9,9,7,-10,-1,6,1,-9,4,-7,3,3,6,-8,-1,9,6,-6,3,10,2,-3,5,-8], dtype = "int64")#candidate|4414|(128,)|const|int64
const_4415 = relay.const([6.835523,1.649658,8.486934,-5.730773,-7.397599,-7.386342,-8.581335,6.692462,0.576951,-2.938245,6.047804,2.126394,1.197783,-8.616388,0.997667,-1.633594,-2.145519,9.432627,-0.405595,1.553938,1.927941,-9.900851,0.063578,1.121444,0.672238,-3.194163,4.100995,-0.295033,4.868183,0.929374,-9.519375,-7.468360,-9.132410,-1.004733,0.900345,8.214732,0.349139,-4.247013,2.219261,3.897898,-2.388901,6.390824,-1.205865,-3.352094,3.135674,-8.031647,7.764940,-4.244896,7.804039,-7.744977,-0.447772,2.958292,0.239370,-8.071605,-5.849136,-1.351684,7.524595,-7.585094,1.499704,-3.308096,2.218677,-3.842597,3.204081,-1.270501,8.462155,7.582618,-1.895066,8.800569,-0.808871,-4.019634,-4.909799,5.741199,0.045321,3.959783,-1.678253,2.414556,-8.590368,-2.739306,-7.640634,-3.886683,-1.871482,1.583331,1.670049,-4.990751,-0.716521,-7.137315,9.692705,2.709308,6.151657,-4.833201,-0.949943,4.238994,1.107568,-2.656993,-6.306835,-4.569138,-5.406309,4.435685,-6.368795,9.376651,0.775956,1.196228,-9.070679,9.858294,3.615434,6.053607,0.049231,6.496328,1.249177,-1.517954,-4.383126,-1.275175,-3.818184,-9.105253,3.991602,4.589836,4.238889,-5.517450,7.080337,-8.013167,3.951676,-7.037912,-4.754029,4.045583,8.587728,-6.200488,-1.917126,-3.313160,-7.104795,-5.656802,8.628481,-9.541581,-3.478112,-7.028187,-8.503150,4.649326,-8.695819,-0.417847,6.758118,-4.839009,8.083491,-5.129489,7.345825,-6.279771,-2.477662,-1.610927,4.053137,-6.367577,2.862697,7.992131,3.628718,6.581732,9.340692,8.384682,5.744963,5.690279,-4.317803,5.215375,1.254255,9.397591,-5.350417,7.665802,1.077536,6.815109,-8.324485,-4.548535,3.609806,8.182070,-9.181876,7.253835,0.460326,-2.633552,0.286575,0.066326,-5.302846,-9.352721,-0.708349,-3.475000,1.405106,-5.922293,-8.852781,-2.127299,-3.800249,-7.652211,-4.386410,5.229592,6.262827,1.712195,9.453364,9.209668,2.302466,-2.145423,7.017868,1.969095,-7.824188,-8.678406,6.925817,2.774160,-2.823029,-8.298512,2.844179,-7.151625,4.937242,5.296953,3.400272,-7.704432,-4.068789,-7.049560,7.842086,2.904625,-6.898866,1.378506,-1.466832,0.461027,-5.218661,4.699896,6.042195,-5.462507,8.862763,9.362541,-7.985128,6.235545,-7.882654,-1.918751,-2.090900,-9.399037,0.690505,-3.738751,-5.968678,7.514473,1.152729,-5.826779,-4.726688,0.680140,6.818576,-9.259828,8.956005,-6.929707,-3.684753,9.557874,-7.351657,1.021641,1.331287,9.512954,8.162200,9.210226,9.489180,-6.304099,-1.896500,3.809129,-0.677557,-2.291755,-1.001358,-5.281065,0.099576,4.823418,9.870077,-0.343529,-8.188505,-5.348511,-6.341266,-1.262665,9.363255,8.052085,-2.195966,1.956497,8.856830,-0.305859,6.170444,-2.539166,9.069222,-6.276763,-2.643418,6.842070,9.080244,-0.584053,3.532917,7.738697,3.644467,0.918121,-7.530766,6.677089,-6.783989,7.373996,-4.500884,-9.277188,2.772505,-9.613912,1.406035,-7.592998,5.000387,-1.592653,6.792062,3.560808,0.562419,-8.520434,-6.657359,7.379307,-9.809581,-1.701342,-9.791268,-6.177201,8.781584,8.043913,-8.795371,5.159557,-6.983304,7.253406,-4.037797,8.718218,5.949933,6.971756,1.807583,-8.204919,8.339580,-8.429882,6.295495,6.544756,5.808882,-8.052181,-4.548334,0.029222,7.252814,-5.427456,5.890628,7.902833,7.483902,-1.424597,7.073600,-9.092997,5.583992,-0.516274,3.004916,-3.457962,-4.255625,4.562112,-2.674001,-0.927029,1.482745,9.612723,-2.437047,0.002038,2.988052,-1.853752,-8.535449,1.844296,9.655955,-3.062531,4.523277,7.676820,5.957702,-0.511329,4.611858,-4.565241,5.539339,4.507170,-1.305916,-1.475985,5.609662,0.012512,4.244841,4.655698,-0.224591,-1.393989,-5.847412,-3.168005,-1.585915,-9.975212,4.570840,-8.777980,-9.831510,-9.637573,-8.016837,9.846339,7.231192,7.064531,0.880724,2.118812], dtype = "float32")#candidate|4415|(378,)|const|float32
call_4412 = relay.TupleGetItem(func_293_call(relay.reshape(var_4413.astype('int64'), []), relay.reshape(const_4414.astype('int64'), [8, 2, 8]), relay.reshape(const_4415.astype('float32'), [378,]), relay.reshape(const_4415.astype('float32'), [7, 9, 6]), ), 2)
call_4416 = relay.TupleGetItem(func_298_call(relay.reshape(var_4413.astype('int64'), []), relay.reshape(const_4414.astype('int64'), [8, 2, 8]), relay.reshape(const_4415.astype('float32'), [378,]), relay.reshape(const_4415.astype('float32'), [7, 9, 6]), ), 2)
func_3406_call = mod.get_global_var('func_3406')
func_3411_call = mutated_mod.get_global_var('func_3411')
const_4418 = relay.const([-6,5,5,3,8,10,6,-4,-2,7,2,-1,9,1,-1,-9,1,8,10,7,9,-5,5,9,4,3,-1,2,6,-5,4,-7,-7,-10,-8,-4,6,1,3,-9,7,4,6,7,7,-10,-7,-5,-4,9,2,9,5,9,10,-4,10,3,3,-8,4,-1,-7,-3,-1,-2,-10,-3,9,-2,10,5,5,5,-8,10,3,2,10,-10,2,8,-3,4,2,10,-5,1,-3,-9,9,4,3,-1,-3,-5], dtype = "uint8")#candidate|4418|(96,)|const|uint8
const_4419 = relay.const([[7.601914,0.121145,3.022620,8.506840,3.606140,8.450390,-6.492691,5.155541,6.107829,3.798889,-4.409986,2.021423,9.463900,8.942681,-7.604356,-6.321186,8.601071,-9.145757,3.309837,-9.420715,-4.261269,-0.917602,-3.945496,7.854996,-7.382807,-1.466005,3.108879,-1.326854,-7.896383,7.969653,4.690625,-7.112936,3.792208,-6.298162,-3.136663,7.576308,-1.073406,4.155308,-5.523106,0.882860,7.464010,2.989402,2.799548,-3.248828,9.287771,-3.506867,3.472621,9.965537,6.307676,-8.311813,-0.021196,-1.604719,9.931670,-1.109398,-8.525831,-5.019855,2.962405,4.700875,2.082126,-0.101570,1.436728,-9.651983,4.432344,5.971410,4.238808,-3.888435,-6.707672,-2.620536,-3.173640,1.668679,-2.659643,-9.834571,1.485191,3.820347,4.154784,4.691706,-9.246581,-9.305384,6.333282,8.767124,1.557004,9.153057,-4.910070,2.121250,-4.874798,-4.435734,-4.903051,-7.446983,-3.275666,3.463000,1.348828,-1.298283,-4.001006,4.784870,-4.367199,-1.702589,-1.143618,5.050664,4.333877,9.132377,2.194517,6.961654,-4.591079,2.481328,7.836070,0.495095,5.367421,-3.342721,-7.241083,-4.173919,-5.266380,-1.472968,-3.531204,-5.000338,-2.768764,2.159327,6.191061,3.632038,-9.912590,-2.126043,5.622929,-8.381309,3.905933,-0.208708,-4.997333,-6.086077,0.656880,6.753875,3.088983,-6.080409,5.016230,0.730501,-6.668132,-6.682667,-4.751580,-4.273114,-1.222074,-8.883581,5.998335,2.034448,4.626626,6.692159,-0.054352,-6.675805,-3.136916,2.050704,-3.724766,-7.242787,-9.901329,1.918428,5.151858,-9.737150,-8.623978,3.794626,-4.135660,1.909620,-1.307624,-5.367809,6.406960,-8.962252,3.783424,2.610869,7.229470,-0.628023,6.880960,-2.469554,0.827141,-5.698154,4.896906,-0.012034,8.500261,-7.831465,-3.576155,-0.165198,0.607553,8.644015,4.199440,9.250872,-1.894900,-5.136735,6.280402,-3.494033,2.296894,6.000476,-4.942231,-9.333503,6.438377,3.979048,-5.022112,-5.513821,3.529097,-2.166492,-5.532125,1.663456,-1.344650,-4.941975,-3.301084,-7.362414,-0.785971,-7.216177,1.063980,-4.260966,6.157822,-1.326675,8.209138,-8.284305,-5.785778,6.554436,-9.983050,7.681187,-6.030974,-2.195544,-2.594993,4.177317,-7.971947,3.107823,-2.173384,5.397651,-5.611975,5.353337,-4.645027,-1.936299,4.517557,3.743037,-6.982863,-2.371087,8.536479,9.436105,8.735171,-3.460683,-7.012364,-7.431091,7.759137,7.477913,3.005475,4.442921,-8.803788,7.095650,-0.779849,6.661360,7.936987,6.120976,-3.531731,5.744517,5.981177,-8.336838,1.994366,2.863011,-8.631583,-8.968210,0.153667,1.088067,9.106676,6.256423,1.677375,-1.304054,-2.393836,7.898497,-1.288055,2.939763,-2.367050,-0.921726,-7.919285,-7.863523,-9.360458,-0.312463,6.075761,7.486040,-2.690997,-9.479347,3.319860,2.773165,-0.284153,-5.872723,7.454408,7.660001,7.505317,7.851408,0.053988,-6.149695,3.402596,8.342645,-5.649688,8.784920,-0.222551,6.566921,8.911911,2.237998,0.282639,-4.309224,2.863457,4.708620,4.438924,-9.521551,-7.387910,-1.538796,-5.237904,-3.307290,-2.400736,4.092901,5.023594,-0.200994,5.820824,0.857937,-3.046061,0.053538,5.406357,-0.432184,-9.590587,6.009825,-5.714266,-2.151349,7.404233,5.160596,-7.817403,-0.778536,7.953245,-8.001834,5.492698,-7.729644,-1.384835,4.110566,-1.845298,-9.368964,4.382289,7.205982,-1.982657,-1.356164,3.777755,6.898228,-6.655213,7.873070,0.561938,5.910379,4.742686,-5.264543,3.155945,6.790251,4.081190,-6.796629,3.553634,-8.175259,1.679473,-3.171520,6.629504,2.951259,7.767921,6.469368,-2.976757,9.362984,-4.994882,7.168811,-7.492041,8.657449,2.239112,-0.059876,-7.039997,-1.999568,9.262842,-4.188477,-3.918245,-6.837586,-8.920328,-9.628414,-9.282013,2.348738,5.538707,1.693385,0.653101,-4.547729,-2.632412,-6.183334,9.289113,3.381632,6.111888,4.491028,3.454092,5.388700,-1.248600,-0.499064,-1.921349,0.306072,5.632081,4.313244,-9.544026,5.243874,-2.674588,1.434729,-7.602580,-4.375554,-7.083763,0.412331,6.080935,4.029714,5.534580,0.260998,9.362639,7.893152,7.176882,-4.629771,-3.932584,-5.419172,5.396471,0.156191,-5.633229,9.005675,1.401558,-6.988411,2.852471,-9.214453,-6.667525,-0.418648,7.629646,-3.712602,-8.290637,-9.685756,-9.541003,3.673453,-1.197064,0.561049,-9.494246,9.202799,8.206946,1.688834,9.781524,3.067065,6.299895,-2.449234,-6.880757,1.338289,8.963370,1.632167,-3.895444,6.741558,7.489033,-8.303583,9.969906,-0.856799,7.780743,6.913143,4.226783,-7.370404,0.512645,9.654808,6.561458,-4.199148,-4.362983,-9.059709,7.162824,6.546342,-5.666657,-4.651629,3.657083,6.089454,-5.093744,-0.437227,0.412957,-4.308903,7.923316,-6.812812,-1.013811,7.886411,1.831909,-6.195646,4.819143,6.041114,4.797590,4.987235,-7.153200,6.873448,3.954156,5.163788,5.984244,8.311242,5.845599,5.749077,4.547506,5.516746,2.424786,8.238065,1.052939,-0.616540,-5.971920,-1.272252,-0.750227,-0.606529,1.778101,1.254352,0.614379,2.009573,-0.509616,9.279595,6.302113,-3.097598,-9.386510,2.778808,9.661037,-0.295049,8.313921,-4.155859,-2.570251,6.829952,-4.419834,-4.103879,-3.924742,0.064043,3.832189,-3.252812,5.180760,0.294116,-4.697266,9.980525,-1.341715,0.330644,-8.155354,-6.649553,-2.063404,-2.666798,-9.270314,2.837028,-7.021731,8.312466,3.927362,-3.096776,5.536578,-7.850770,-8.820805,0.289709,5.328389,-9.387698,-2.854145,-2.348785,2.217654,-0.749165,-1.856618,-7.865506,-8.765371,-8.000260,4.993944,-2.541913,-3.144421,-9.241299,-3.359202,1.285904,-1.080759,-0.275635,-8.800544,-8.242422,0.486599,5.665497,-7.993134,0.062775,-8.499651,-2.853470,-0.734789,-2.065751,8.707574,-5.855744,-0.794190,8.684893,6.346823,0.289439,-8.371252,1.288329,-6.021013,7.580714,-0.147463,1.238295,-1.401460,-7.826153,-6.414253,5.927927,3.021015,-6.117965,-2.194357,4.501358,1.983055,7.443765,-2.077616,4.867308,-2.312058,4.340461,8.825346,7.193978,-5.095228,9.503551,-4.467005,-7.363622,-7.469039,4.069530,-0.375000,-4.979996,7.512501,1.548182,2.682279,0.722662,-2.603093,-5.374309,9.650097,8.882114,-4.638772,0.320451,-6.991137,-2.789176,-2.893418,3.539888,-0.146851,-3.914424,0.204101,0.832099,-2.909992,-4.809617,3.521874,2.767182,-1.581216,-5.254918,5.362062,4.278967,7.912834,-1.239993,6.414742,-5.927596,7.257217,-9.190721,6.898876,1.138248,-2.230280,-5.775844,0.346450,-2.205629,-5.645698,-3.993767,-1.222502,9.909868,1.237235,3.610007,0.267055,0.600149,-0.714435,-0.699592,4.486894,-2.201503,0.763193,-6.332127,-3.695263,0.777860,0.131372,-8.808052,9.213530,-9.075238,4.558041,-5.310326,6.677442,3.245916,1.924416,4.664567,-4.222781,-6.802598,-1.897827,-5.333840,7.698699,-9.206757,2.705326,5.268304,-2.693874,3.525238,5.259004,8.319784,3.837450,4.508329,-3.238270,-8.496409,-2.954778,-3.795342,9.693120,3.706766,-5.976354,6.451919,-1.574011,9.657560,-7.352184,-4.885699,-6.930091,2.523160,-2.947387,-4.958519,5.555992,2.600867,7.216835,1.459773,-2.808243,4.670655,-0.936896,-5.074133,2.245421,8.980372,6.890451,-1.124913,3.329289,0.168836,-9.403210,-3.968223,-5.718699,9.300449,-7.288665,-6.496209,1.073901,8.752173,3.376511,-5.055469,0.026250,-9.836424,0.449141,-3.561133,-3.181564,-2.958328,4.776871,4.353110,8.854780,1.055185,9.775861,-6.296509,-4.457129,-4.811642,-4.831419,-1.933671,-4.830117,-9.780021,1.935189,1.065640,-1.440356,-6.127337,-3.130068,-3.843819,-8.901227,1.309465,9.633775,-2.071126,-7.896130,8.930257,5.272845,-1.239543,2.952093,4.688176,-6.209274,-4.776999,2.135230,-7.519090,-4.998212,8.362624,4.595416,-7.323397,-2.962712,-4.292453,7.393534,2.720764,5.180964,9.083282,-7.855252,-1.147887,7.929824,-1.963579,1.946395,-6.291552,8.942403,2.845832,5.764580,0.091571,-3.859738,-8.878815,-2.550926,0.822562,0.097959,-3.316311,8.654338,-1.959031,3.753301,9.443403,-9.452427,2.914991,8.062449,-8.330196,-9.195717,5.799764,2.870033,8.087389,0.363602,7.158820,7.756766,6.164040,-6.049043,9.983856,-5.786121,0.986413,-7.758122,-0.204003,2.894423,-9.135386,-4.484312,-7.201232,0.090261,9.735532,-1.504749,-4.473331,-4.950460,2.459626,0.435040,9.384915,4.140031,-2.549016,3.795597,-8.006178,0.206545,-7.366097,-9.947768,9.227012,-7.749472,-6.023197,-3.221240,-5.476471,-4.549192,3.487375,-9.603385,2.123188,3.530100,-9.066511,-0.626439,7.525114,2.575108,-4.842038,7.869333,-0.999556,-6.170838,-9.896993,9.429975,-6.269615,-9.992520,3.828446,-4.441848,1.979251,6.091051,-7.771846,-8.365185,1.323025,0.270148,3.626834,-7.353670,7.111007,-2.601040,3.077021,-5.591513,-7.086337,2.088407,-0.462832,-1.271112,-1.944198,5.139833,-9.229494,-5.744957,2.527934,0.878210,-1.341938,-6.117800,-2.606666,-1.783398,-7.344154,0.678960,9.274441,2.560336,-9.368529,3.087100,0.372509,0.473132,-1.427291,2.204666,-9.843814,-1.933151,-9.844922,-6.469301,-5.326798,-9.287719,8.197556,7.062982,1.493952,-4.887319,-2.016067,-9.303578,-6.050215,8.441754,7.354625,3.297302,7.524456,9.161544,-4.840110,4.352743,-4.701656,-0.464988,7.707452,-4.667156,-0.822420,6.067976,1.193785,-9.169573,1.139063,-3.317194,-1.367099,-7.966744,-5.789951,-5.399571,0.311433,7.371296,3.476177,-1.555378,5.978394,9.470923,5.678504,-8.761260,-9.929217,5.862506,2.569798,2.972955,9.211324,9.017459,2.577286,-9.258458,9.366639,-8.846958,1.342504,-9.484798,8.339905,-4.823970,-7.386388,6.609408,7.768308,-6.271355,1.806466,2.162018,-7.879743,-5.630435,-4.445202,-1.623481,-5.590629,-2.335424,5.390226,-2.631523,3.197388,-4.109540,9.952288,-1.826376,-7.518877,8.615944,-9.203831,-6.748734,-1.109613,-8.585333,6.593613,-8.622413,5.893094,-4.710951,5.825862,-0.926868,8.456129,-3.162974,-9.904327,-8.663079,-5.596637,-9.868526,-2.950165,5.115743,6.186141,4.752512,-0.034394,-9.973862,-9.425385,1.422714,0.754520,-0.986009,-2.090858,-6.618773,-2.445053,3.636249,-0.460117,6.477015,-5.462811,3.841495,4.366880,-1.142502,9.462773,2.562513,2.990732,6.344881,-5.198803,-3.682605,6.046309,-5.286316,6.970761,-7.579594,2.933757,-6.187809,-2.237329,-0.166712,-6.442054,8.215399,9.234520,7.874062,2.692564,-4.540901,6.687707,-8.293029,3.563884,-3.832749,-3.449335,-3.842463,-4.841106,9.925041,6.107378,-7.705049,5.158394,6.577243,8.903750,7.830799,5.411074,-7.851768,-9.009982,5.228766,3.727458,-7.110239,-3.681038,-0.528875,7.135999,9.032837,2.217435,-8.992567,-3.948685,6.690673,3.367556,-6.222781,-1.464529,8.228192,-8.963127,-3.512163,-1.291756,8.153676,-1.292684,8.548696,-6.736936,-4.165020,6.513960,-9.268269,-8.282685,5.738688,-3.744629,-6.854773,-6.666819,-4.391596,2.455122,3.615843,2.463795,-3.652204,-0.159994,-4.586248,5.812902,-1.308595,6.609142,-3.014460,-2.551511,1.913416,4.690963,-9.876269,0.533583,-7.151324,0.765218,-4.639348,0.954486,-4.759134,5.728569,-8.178275,2.703291,2.683850,5.380842,-8.280931,2.094402,-9.240874,-4.586339,-0.008161,8.169387,-2.963782,-1.089078,-6.820985,3.716800,9.698208,2.252330,5.039740,-7.516561,6.344418,-9.928794,-3.300138,-8.773997,3.646314,7.072726,-5.802331,-2.694035,9.121288,-0.330786,-4.779960,9.062810,-1.010999,3.024901,2.135187,-2.876989,6.148971,1.431364,-2.526633,1.870441,-7.038008,8.858415,2.320344,1.026983,0.689275,-3.681999,1.272876,1.725913,-2.124980,-6.620081,1.472904,5.913936,1.809780,-7.247610,-4.851537,1.464371,-0.470795,2.913055,5.101477,-6.362420,-1.773500,-2.063009,-9.860056,8.606690,3.362493,0.741074,-7.696455,4.956926,5.589431,4.124747,4.357330,-5.315282,-7.598484,-8.965772,-5.662840,-1.174581,3.784530,-8.106743,-3.038828,3.421856,4.970300,-9.798440,3.326827,-2.649260,2.317925,-9.984302,-4.647775,-4.549608,-8.593192,-4.500494,-3.515190,-6.685403,-6.691772,5.736857,-9.115523,-7.937161,2.241437,-5.893726,-9.912834,9.727843,-7.928716,2.196350,-8.738626,8.382949,-1.784729,4.869146,-6.037607,-0.932517,3.527554,-5.906768,-8.284595,4.199367,8.003209,-9.717179,-0.345605,-1.004918,5.919936,-3.502388,2.715473,4.821252,3.433162,-1.552892,-6.427827,-7.810221,7.446434,8.772792,9.186898,0.637327,-4.724371,5.548610,-4.987436,-6.018028,8.160201,3.575759,-0.692201,-3.398864,-3.705527,-4.638520,2.856324,-8.865620,2.143523,9.174200,-6.139924,5.679715,-5.049337,-4.434838,-3.963599,3.010736,8.090031,2.817861,4.887693,2.086950,-4.055249,-6.728546,9.144110,-2.174795,-2.574215,8.642435,7.555515,-4.158715,1.335933,-8.401551,1.566238,8.281021,-6.350369,-7.400850,-0.090861,6.205448,2.121371,2.535975,-5.080087,6.918472,6.881143,-8.169203,-9.283675,-1.839087,2.677945,1.067538,-5.065125,3.330390,6.159916,-3.540843,2.560068,5.464338,7.347761,3.786349,-4.940629,9.831695,-5.717787,-2.360459,-7.576287,-1.037050,5.213057,-7.520947,5.440665,8.172442,4.022916,-9.678942,0.394320,-6.812576,-5.134505,3.467648,-4.830126,-9.385416,-0.247028,3.802368,-5.171848,-2.004745,-4.648866,4.760344,-7.076388,-3.980239,7.747777,-8.991978,-5.063781,8.617435,1.304221,-5.776325,9.409430,-9.653305,7.518404,-5.179105,2.962785,-8.462204,3.224497,5.829731,-9.542061,-4.225590,1.870394,-3.426832,0.210472,-1.977677,-7.923558,-5.416926,-1.114327,8.797151,9.879023,6.928507,-5.899000,-9.380089,8.404932,0.731090,4.069061,0.870895,5.670307,6.138979,-5.978045,3.691976,-8.838625,-3.266696,-7.316159,-2.799510,-7.061020,-9.260674,2.109474,-0.177039,1.505904,-4.746419,5.207830,5.728573,-2.247017,4.121398,-8.536234,0.508932,2.764164,6.509462,-0.531764,9.887203,6.538687,5.812827,-2.012382,-6.663899,-6.240721,-1.030510,-9.286500,-0.520278,-4.438090,3.635847,-6.083012,3.912944,9.767198,2.028900,6.476956,-2.351865,-7.333246,3.114051,6.495498,-1.317186,9.549175,-4.000154,-0.548502,-9.616888,-7.587579,-1.034381,-8.612858,-2.320102,-3.029022,7.739581,-5.136097,9.192095,-8.549608,3.345978,-8.939295,4.264530,9.071872,7.650508,-3.685991,-5.315559,-5.623910,0.043549,5.241596,-6.832885,8.917917,1.282701,0.484192,-5.627701,0.420734,4.696759,-4.139011,9.573864,-3.270302,1.018134,-0.756074,-3.630527,-3.403042,-8.986300,7.390743,-4.012019,-6.061740,4.881579,-5.215199,2.455641,6.832511,8.501159,7.612537,9.137885,4.131974,-1.919093,6.232820,-9.307675,-5.565336,7.780495,1.965620,-6.995753,1.653093,0.990492,-3.255538,3.473822,-2.259167,2.321268,-1.955061,5.006947,0.158267,0.730192,-4.618852,5.279401,-2.417441,8.829967,-4.995440,-4.008846,9.335634,0.401914,-6.150121,6.970516,8.046740,6.048651,-8.983575,4.233890,-9.545829,-8.354417,6.978342,-5.668510,-0.970017,9.464667,6.539614,-1.495662,-6.974910,-3.321107,-6.112398,9.804346,-3.158147,0.871261,2.790614,1.092548,-2.578902,1.046383,6.673309,0.559437,6.785768,-3.811671,-6.772056,1.170100,-1.460814,-4.864653,0.060062,-5.611342,-9.577675,-4.466528,-6.267769,6.517804,3.732592,-3.207087,-9.011758,-6.171095,1.692528,2.877632,4.542231,-1.264367,-1.192582,6.501049,-0.462847,-2.926744,0.098595,-9.101527,-8.955356,-2.541470,-8.944949,-8.896960,8.007635,-2.083032,1.379381,-6.905478,-2.199306,-0.845079,9.026088,3.483960,9.103085,-5.139445,-8.632369,-3.105729,1.224751,7.915559,-2.483996,-7.315567,-5.911177,-0.003418,-9.272444,1.390469,9.546374,-1.082652,6.101079,-5.785340,7.382333,8.069378,3.478407,-2.455394,2.726553,7.345616,9.565660,4.113179,-6.648269,2.067313,-9.018994,-6.766772,-2.223568,4.393918,-6.307285,-1.882813,-9.951336,2.618171,5.732518,-6.874950],[4.937993,-3.186597,-0.710591,0.045017,6.997733,6.774034,8.115823,9.678697,-4.550473,7.178259,-2.622400,-4.140548,0.901842,6.074170,1.739035,2.193932,5.593148,8.596647,9.540139,-2.735156,3.629426,0.733198,4.526056,-6.457525,7.291782,-7.479934,9.073941,-2.506533,7.498429,-9.473993,-6.321353,2.193279,4.489990,6.630730,7.593509,-1.574110,6.355440,4.811551,-8.431114,0.610850,4.915645,-5.440721,-7.227159,-6.981763,-8.664392,3.707757,-9.758186,-9.984085,7.449583,3.691124,8.012977,-4.500460,1.846592,-1.397077,8.889386,0.933264,8.932965,-9.518404,-5.303444,6.353775,0.569235,1.487153,-5.426694,6.829958,9.176676,-8.926864,-3.283159,-0.969488,1.500085,-8.035301,-8.846189,9.613875,4.860661,3.824271,-6.005987,-3.056200,6.406358,-0.164422,6.816372,-4.551633,-9.680577,8.236850,3.475990,-3.536808,-9.975027,0.707452,-5.478209,1.393680,-6.902613,3.659713,4.537156,-0.220008,-8.329588,-8.936863,4.832606,-5.480058,-8.691782,-8.407621,2.071607,-3.952855,9.611170,-3.230028,-7.966690,0.945864,7.144169,-4.695306,-5.939318,7.858694,8.264075,-1.780224,-0.254609,-0.350903,1.146641,-5.763927,8.314411,-8.621432,0.498852,-5.034915,-2.231911,-8.148096,-0.767251,3.567136,-0.829690,2.048707,-5.981501,-7.086590,1.946906,0.626088,1.708332,3.288721,-1.641214,-3.566696,9.230972,-6.101043,-9.391452,7.173988,7.892727,-9.173604,0.943397,1.694242,9.769934,0.402005,-3.645381,9.583458,-3.274458,-3.633546,8.277560,-0.931371,7.796937,-1.415803,-8.175810,-2.564832,-1.857707,0.594754,5.145981,-0.781098,-5.476706,6.240088,-3.250417,-4.722968,9.321111,-7.889826,1.137160,5.790466,6.280071,6.915261,6.061727,7.445753,-7.410744,-7.055571,1.156159,-7.401489,-1.480962,-1.959657,2.357726,3.850170,6.099172,3.539132,3.319864,1.193950,-2.271177,-6.016527,-0.895851,-4.196092,-7.969446,-2.945449,2.600956,5.484469,-2.137900,-4.664519,-8.812686,6.629173,7.809000,4.515052,5.432222,1.878409,8.786562,-2.034176,4.687900,-4.135293,2.571620,4.704459,0.162582,-8.963573,-6.405548,6.838709,-5.891590,-7.531366,8.387414,-8.262472,-7.468136,7.691383,0.826292,-2.011545,-1.979955,-1.855017,0.895062,-2.953444,-0.670169,0.847079,2.986965,-8.089199,3.879945,-2.440170,-3.310997,8.926004,-0.220439,-3.578756,-6.865884,7.452042,1.211338,-0.325173,4.457578,6.092593,0.227206,0.671646,-8.629383,5.455646,-7.342215,-1.107498,-4.994453,-8.833819,-9.436037,8.659314,3.905618,1.581538,-2.307532,9.406752,-2.090448,-0.988771,6.570718,2.098167,6.482559,3.981890,-8.900030,-6.255715,-9.261967,9.103070,7.665208,2.881455,3.083273,6.809345,2.434617,-3.979155,3.781673,6.281295,-5.390711,-2.214240,5.657383,6.907885,-8.833954,3.362165,-9.643559,5.586420,7.890746,-7.459078,-2.141470,-7.165113,0.302261,1.803529,1.960925,6.204112,9.395047,6.417217,-8.267578,-6.280891,-5.019030,4.022551,8.031140,-5.155469,7.385138,0.452004,-5.391647,0.369978,-1.377024,7.231326,-7.917874,2.747264,-2.456166,-1.012423,-7.318156,9.318748,-7.379401,6.236100,-3.062873,-7.031136,0.631894,7.754638,-6.315064,7.346629,4.902217,-8.717020,0.478254,-4.825081,0.923965,-2.531630,0.690646,-1.255907,-1.173806,9.879419,-5.087084,0.791020,-7.799820,2.369038,0.730806,0.002512,9.951803,-7.293425,-5.031874,5.951546,-9.426399,6.349639,8.350925,8.517071,9.003526,-7.345524,4.327952,4.313299,-4.813487,-8.108708,2.110006,4.336387,6.808847,-3.166256,-9.433881,8.748366,8.181989,-3.655315,2.633587,7.720805,6.753484,-5.961488,7.135094,-6.170173,-7.814667,5.513664,-7.558293,7.679239,6.049951,7.912447,3.105803,-8.585354,4.613422,6.962444,-3.783346,-5.885545,3.564593,-7.471658,-8.953317,-7.419979,3.528745,6.724109,-6.577017,-9.952790,-5.376174,4.705797,-5.428130,-7.615106,9.917901,-9.763192,-5.789338,8.553737,2.853366,-5.237781,-1.942489,8.014349,3.437622,5.074688,8.895479,8.256998,-0.289947,8.432973,-2.775259,-4.511580,0.760474,3.335990,8.511105,2.934878,3.096348,6.018624,7.126794,3.085784,5.493426,-7.583020,-8.064371,-2.919860,7.503976,-5.203100,0.327868,4.208048,7.949334,3.156866,7.088041,-7.285635,-5.449471,-8.163457,-7.493799,-0.536902,-9.035977,-0.493864,-1.653493,1.556783,-4.065855,3.936750,2.616858,-2.411339,-9.355149,8.298308,5.662838,-0.940359,7.623636,6.176178,-1.256543,5.118510,-6.113056,-1.355115,-0.324532,-4.297834,8.920535,4.191511,-0.849470,6.423324,6.935613,-6.668921,-9.012198,-4.224153,5.551328,9.428741,-6.836155,8.727024,-2.465341,2.797137,5.331696,2.050974,-1.262135,9.105573,4.729439,2.902176,-1.104530,3.044760,-0.035743,-5.074144,6.137332,2.340246,1.757051,-2.979646,-1.661687,-7.087843,-1.164583,-0.395832,-1.738665,3.203316,6.900474,-8.762227,4.489121,-6.179123,-9.946424,5.152729,7.576128,2.925758,7.893403,-0.500331,6.048870,-7.295231,3.498042,-8.108177,-6.029580,3.871086,-3.169716,8.729857,4.605497,9.298182,6.202352,1.131741,-7.550431,7.024301,-2.298023,7.942413,-0.458973,4.307426,3.320857,-3.305713,-1.426265,2.240554,3.968404,-9.824198,-5.091980,-7.697549,-7.259936,-8.780412,-5.956305,2.130489,-1.016340,8.566930,-2.777063,-6.113083,-1.704467,2.499356,-1.675580,-6.001464,-0.300386,-7.142995,-5.513268,-5.134950,-2.462382,6.885169,-3.018812,3.008250,-6.803441,4.227036,-3.559039,-7.960308,-1.506716,5.745762,-0.795022,9.897731,-1.232901,9.104927,-5.193228,1.739418,9.004654,-1.119605,7.222627,-6.230891,-9.762009,-4.857009,3.443208,8.115846,3.722226,-8.667701,-2.893220,-1.431532,1.428696,-0.514220,4.664060,-1.502837,-6.926303,-1.284187,-9.182352,1.003495,-4.877601,6.428222,-7.310012,-2.934592,4.721499,8.883881,-7.223167,-2.626490,-1.660112,6.360165,3.340235,-7.358916,-0.892800,8.530964,8.136132,5.903589,7.154909,4.198144,-3.222074,8.858251,-8.946590,7.798091,-8.976953,-9.303689,-0.446995,-2.112414,8.623935,-5.232277,0.300664,-2.635587,-2.151169,-1.084756,5.856372,-4.198422,6.675363,9.190581,-5.409414,-9.870809,8.157376,6.720593,0.421233,9.100033,-8.453693,-5.073710,4.454733,-1.860052,7.358293,0.123221,-2.618278,-5.301211,0.190665,9.272967,-4.197341,-8.091469,-2.011614,-1.590314,6.116674,-8.976973,0.456943,1.643904,-3.345127,-6.053778,3.479406,-9.593931,2.947422,8.893013,-3.405017,0.391446,5.015481,-1.989913,0.032582,2.024909,-0.542402,4.357622,-9.491793,6.694516,-3.973783,-2.077108,0.142176,-6.503813,0.656959,-0.310155,-6.591085,0.476489,1.105022,-5.113949,-0.597270,-6.244666,4.681997,-3.196716,-7.431972,-2.585329,9.113594,-2.054504,7.698546,-7.605400,9.725501,1.541751,-8.634231,8.763415,-2.823712,-4.937605,6.403588,-4.830407,-8.865157,-2.593773,-3.077686,-6.646587,-7.308323,-1.571441,7.266044,-8.551932,2.798288,-1.942867,-9.584230,-8.701639,6.984924,8.798283,9.601540,-4.971305,-6.671492,-6.485981,6.655039,3.616286,-1.736733,-3.300776,-1.758813,-3.417399,-5.724153,0.945102,-6.885783,6.272112,-6.384911,-1.317437,-7.657219,-4.553903,4.275143,8.619932,5.019031,-1.934040,2.316475,3.252266,-6.742625,5.821706,-4.405250,0.331342,-7.137469,8.544140,-1.577614,-4.678369,-5.005129,7.802341,-8.723450,-2.374513,8.879256,2.245042,1.883170,-5.923753,-3.449735,-1.382250,-4.986599,8.272492,0.730451,-4.653160,-0.820815,-5.427148,0.222948,-3.147649,2.814529,9.344307,-9.251672,7.197548,0.878240,1.620983,8.695211,-3.303184,6.166855,4.815074,-0.830879,-5.554168,-1.762395,0.937241,2.428968,4.926266,7.897712,5.521738,0.256516,6.769438,7.772734,-2.719556,6.398688,-0.426392,-0.663632,1.849693,4.095031,2.131439,-2.677130,1.627114,2.187553,-6.967614,5.164819,-8.820332,-1.932305,9.880576,-1.043402,8.962464,5.153311,-9.784235,3.510215,-6.954897,-2.244060,-4.388570,2.961095,-4.680209,2.655541,0.756912,-8.929255,3.193972,8.354733,-0.166003,9.626777,0.377282,-7.162009,-5.086247,6.921323,-7.295969,9.695103,6.278282,2.447946,0.074848,-2.543564,3.621100,-3.814563,-0.995704,-6.560403,8.468263,-6.876055,-1.916036,-6.474152,-1.244797,9.364887,9.271958,3.415674,2.025929,-5.664367,3.531679,1.257309,-5.906429,-8.309104,-1.248224,3.566137,-7.056449,-5.249274,-8.075257,7.971855,5.858010,-2.186116,3.487477,5.125984,-5.595781,0.349344,-2.799393,-7.619493,-5.710850,8.656459,1.082200,-4.511169,-4.880389,-4.553678,-6.016437,3.196658,8.625991,-2.856820,-4.805429,5.858893,-6.688177,-1.365676,-5.170985,9.395301,9.907249,5.426757,3.436159,-5.293889,-2.288388,5.202235,8.590163,-7.216428,-7.560505,3.138639,-2.162879,1.439118,-4.232205,-7.314021,-1.918060,1.624026,-8.353692,5.351563,5.215950,-3.114590,-5.323692,-3.558076,-8.246696,-3.078670,5.711308,5.131469,2.951350,-2.751516,5.323593,-3.139471,-2.273016,8.434802,-6.706858,6.281999,3.280103,9.130565,1.926036,7.631289,1.215476,-6.174946,2.934460,-6.267300,-7.560509,-4.600633,7.297891,3.125587,0.384061,0.171060,2.714793,0.150664,-9.860054,6.822882,-4.615788,5.791387,-1.745513,-5.714538,-2.676175,-5.321614,-2.610550,-4.631596,6.475409,9.902621,-6.140768,-3.408388,2.739646,-7.863814,2.179128,2.332964,-1.394295,5.439380,-1.967805,9.656852,-6.751049,6.068538,-5.315333,8.059532,-0.708978,-2.691446,2.082546,-1.236713,-3.580744,-9.999618,-4.416121,2.502834,-9.214740,-0.482198,2.653735,7.398728,6.674343,-6.250786,-4.636720,-2.339618,-0.526148,-0.160640,2.977336,4.451423,9.807680,4.894731,1.744199,6.790698,1.224115,4.059451,3.323196,8.197735,7.219532,-3.828699,6.096641,-4.659462,-5.564080,4.684029,-3.830995,9.167032,-7.102192,7.116905,-3.395634,5.655919,-1.387206,-8.860709,-0.185049,8.619772,3.332531,9.288316,-6.629640,-6.836166,-0.908091,-3.024197,-3.987409,2.485439,3.729038,1.928861,6.457259,5.240176,4.844827,8.568957,9.544947,7.807824,-9.699624,3.595283,3.661271,6.746228,0.455051,-9.683044,-4.305680,-6.765577,-9.795767,5.373978,0.183350,-8.688468,-7.964401,-3.197013,-0.200964,-1.677630,-6.003396,4.312779,8.094594,-1.527911,-8.043341,6.589025,-7.213911,-2.667515,2.889517,-7.530699,4.815291,4.439309,-1.763301,3.552446,6.463828,7.924791,-6.722742,1.753726,-7.323773,-7.012201,-9.285756,5.544021,-5.016503,-2.237844,7.037472,-0.349616,0.726732,-0.661776,8.489875,-0.510001,3.347129,-0.748532,-0.191504,0.238828,0.785876,8.481551,7.084624,-5.700109,2.567612,9.753199,0.431308,0.528320,7.159473,-1.521866,9.998042,-6.424831,2.328687,-6.710425,-0.501744,-7.689467,-1.214684,-0.909464,-7.966203,1.868576,7.006667,-8.090269,-3.948180,5.594602,9.975637,-0.357767,-1.927585,8.810585,9.391658,8.611357,6.278424,-9.853079,4.056945,-7.308437,9.159808,1.452546,-1.263074,-7.968408,7.598608,4.595361,2.551748,-8.281128,-7.657400,0.149150,4.814369,5.305841,-9.730351,-9.084523,-9.976931,0.139507,-5.797654,-7.476884,-8.999591,4.325560,-6.296617,-0.781110,-1.738825,4.803737,-4.089193,1.887162,6.530849,2.756743,-5.230511,-0.894841,-9.439102,-4.417181,-1.104607,3.590304,1.131568,3.553831,0.049933,-6.946634,-5.339149,-7.724642,-1.981643,-8.835305,1.812883,-3.720485,-6.879872,-4.580470,-8.964051,8.817962,-2.409785,-6.114986,-8.745896,4.639878,4.500979,0.751959,-7.409040,5.354156,7.884718,-9.603271,5.242771,-6.283260,8.995596,-2.247782,-5.122125,7.078380,-2.740236,-2.956544,4.919811,1.962907,4.592552,-2.664369,-8.041607,6.568732,0.029272,-4.672759,-1.106212,-1.992119,-5.759517,7.982201,5.537237,5.281177,-5.290232,-2.224777,2.952101,3.806107,-1.027890,-2.067274,8.979567,3.004654,-9.545524,8.637676,-6.737707,-1.148048,-3.538019,9.272229,-6.135232,5.128952,6.798205,-9.841182,3.718943,0.635387,1.214870,8.742838,9.794107,-0.570994,-9.542334,-8.673138,9.034229,9.020075,5.870472,0.920457,0.424796,-1.094133,-6.175746,-3.266994,-9.352383,-9.721236,0.902614,-1.917409,-5.792233,-4.062133,-6.332009,9.939204,-8.004138,3.752633,-6.202713,4.652718,-4.214745,-0.116412,0.722383,-5.982271,-1.856241,9.804566,-3.575939,0.492666,-7.374481,-9.421284,-3.264741,4.687189,-9.015150,-8.272569,4.937670,1.135641,-3.831038,0.573320,-5.443690,0.362488,-6.170763,-9.985471,5.234208,8.903344,-9.667241,-6.582046,7.253426,7.714695,2.150338,-5.731407,3.078311,-9.141781,2.851660,6.933032,3.219213,6.682665,-7.525070,6.532204,5.053421,7.357469,-8.735961,-5.712473,9.501829,2.987151,-6.521922,-1.193020,8.856456,9.032262,-0.663564,-3.304436,3.658554,8.916582,-2.026867,3.748117,5.180423,6.643400,6.555269,1.216632,0.862605,7.787194,4.830440,0.442953,-5.025055,6.064673,-8.584168,-3.182836,4.892961,9.731860,-2.200350,0.966259,1.462841,9.840380,1.683378,-4.738122,-1.683234,-3.431960,0.555458,-9.954843,-5.777015,-3.818786,-1.062406,-6.807999,-9.962330,4.841547,2.739497,-9.059541,5.686843,4.277618,-1.968029,8.587050,3.319735,-2.216530,6.664790,-1.232715,8.680859,-6.860845,1.968798,8.269225,-4.556514,1.515892,-8.814342,2.233443,7.309945,-7.343580,-3.360183,-6.760415,7.672197,-6.395243,-5.690335,-6.768548,2.946396,4.551718,2.872247,-3.776012,7.934795,8.028449,4.262388,7.407917,7.940079,-7.704146,5.842698,5.472216,-9.877892,1.440884,-4.464409,-6.161746,2.669511,0.374439,-2.682625,-7.687138,5.584711,3.119442,-0.536431,2.396346,-5.647618,7.019608,2.107825,-6.042315,-0.147886,-3.443185,1.726820,-4.966914,-7.212915,-7.760798,6.661937,-6.783637,-5.232382,3.124720,-8.486550,8.298541,0.674555,-6.347119,8.696486,-2.389627,-4.577587,6.174662,6.118827,-8.957223,1.366442,-8.065588,-5.740779,6.111880,5.722941,6.781601,1.500924,-9.473088,-6.565244,0.501623,-7.973002,8.326512,-9.741969,-3.281153,7.456443,3.775625,3.933698,9.042299,-2.995323,8.936097,-7.853515,7.763500,5.477897,-9.636234,-6.185463,5.286855,3.090280,-8.665605,8.801244,1.473839,9.580178,9.078339,-6.798111,-4.225972,1.345821,-4.353957,4.871080,-5.617122,-4.929857,-4.147974,-5.199704,2.138691,-8.106962,-9.157378,-2.276526,-2.510319,-7.756507,8.425439,9.973424,-5.716320,4.593088,-8.080312,-9.023560,2.948319,0.775250,-0.391418,4.441119,5.666235,5.938892,-4.042645,1.697266,7.594826,-4.962052,-1.182932,1.754404,0.753970,-9.271901,3.554194,-7.388614,1.244017,-2.830880,9.565120,2.232463,8.434475,-9.680235,-7.071010,8.372957,-7.064275,-1.641364,3.625182,3.935398,-9.625912,-2.086189,-1.107687,-5.250563,-1.712472,6.152761,1.520524,-2.949427,5.149012,-1.479849,-7.001557,-5.831254,4.408524,1.380127,-0.659642,9.121352,-3.335952,-3.417146,-0.647567,-8.044247,0.636515,1.070195,-8.245403,1.469839,-1.019170,-3.526875,7.373257,6.177213,8.065571,0.904798,4.627111,5.274085,-3.502281,7.709003,-0.970868,3.231322,1.768541,-0.122120,-0.710331,-6.199195,5.719735,9.397417,6.745971,-2.709223,-4.558243,-0.053511,-5.580527,9.091589,7.890490,-1.988650,0.651346,3.704161,-8.931250,-1.266751,5.490190,3.254262,2.691766,-9.408086,-4.864360,-8.585861,-3.073349,-7.172521,-6.271777,-7.037605,-6.133875,6.449615,-2.190901,9.609591,3.590095,-7.171723,-8.102627,6.708695,-4.184756,-9.540888,-8.832795,3.264964,9.882794,-6.255917,-4.650986,0.103169,8.801457,-0.107850,8.893391,-0.872249,6.574126,9.731941,-9.963589,-7.890414,-0.078007,5.201237,4.500040,-4.219774,3.813676,-5.584423,4.897762,-2.213731,-3.839937,-7.465046,-0.375237,-4.960911,0.632075,0.511296,1.409665,6.399877,-3.835827,-4.179622,9.053344,-9.852022,2.076270,-4.271337,-7.789658,3.636727]], dtype = "float32")#candidate|4419|(2, 1536)|const|float32
const_4420 = relay.const([-1.630166,-9.301593,7.120952,-7.431603,3.195403,-8.255069,-7.178234,5.854481,7.119565,-0.997086,-5.892650,8.340266,-4.812516,4.187310,1.952542,8.839256,1.385977,5.545921,-9.159812,8.916007,1.901875,3.150434,-3.351857,-6.905957,3.837909,2.322808,5.065141,-1.275909,5.714720,-2.779948,-3.244496,7.104158,4.838304,-6.705367,-8.640280,2.025806,8.565500,0.372175,1.866313,-3.928790,4.504263,-0.796291,-2.587053,-7.822162,-0.024374,-6.752262,-2.241458,-9.464232,6.266149,8.385283,-1.749917,8.538308,-2.056021,-2.321824,-8.988394,-8.676208,-0.353330,8.993939,0.904452,-7.511523,-8.822183,-4.801996,-2.459259,-3.439802,3.313241,4.194371,-9.965526,-5.586167,-9.604141,-2.313350,0.413281,-6.702148,6.132835,-8.695355,2.020580,-2.495139,-7.814726,-8.940731,-7.631349,-9.275465,6.542129,5.161612,-6.469403,-6.214043,-1.284457,-3.117536,9.554930,9.078200,-4.698165,7.053290,6.365868,6.430767,1.106157,-1.777612,-1.724211,3.977280,3.769178,3.531062,-8.926068,-8.416362,-0.578865,-7.811399,9.417107,-1.982594,-7.143060,5.443766,9.475671,9.990372,-8.788005,-7.045354,-0.272865,-4.245492,6.158816,1.409987,9.947908,-4.068471,-3.497472,6.122160,2.704020,0.799083,-9.882992,9.480886,3.523742,-6.245758,-9.544702,-3.939284,-7.795602,-8.886868,-8.796403,-9.256280,4.901621,2.693948,7.709060,1.049927,-4.494732,-8.815108,7.894475,0.878905,-7.353564,5.725133,-7.996648,0.837877,-8.992820,-0.962866,-0.817961,9.633621,-8.561128,2.147267,5.859256,-0.804282,-0.878987,-5.457747,-6.633464,-2.797947,2.797361,3.512117,-2.263820,7.660785,4.913397,8.414441,-5.157985,8.122228,-8.763161,-5.325565,-0.410012,2.169191,-2.299435,-5.131996,5.520383,6.346552,-5.535853,8.116219,-3.907246,-1.221080,-9.050898,2.715961,-4.281146,0.558132,7.841652,-1.739562,-2.495658,-8.431747,-0.418874,7.514388,-7.374726,-5.931242,-6.672972,1.220913,-5.082591,-0.634797,0.551520,7.273208,-7.609536,-5.486778,1.203721,1.413532,7.652214,-3.916657,2.523483,7.477474,-5.067653,-0.001605,8.177084,8.429462,6.318410,9.470506,0.423433,-2.972716,0.871611,-8.044534,-4.715230,2.775764,1.056446,3.222547,1.592466,-1.803728,-3.795258,-4.262976,-9.708986,-9.754463,9.112905,0.840916,-4.003085,5.165008,-1.386309,-0.814637,3.349979,-6.094190,2.016048,0.602294,6.822501,8.608027,3.427968,9.027070,5.099168,5.797946,3.263606,-5.431951,3.568388,-1.347281,2.499431,-0.565658,-4.248238,5.750847,-1.703078,-2.509255,9.531657,7.181059,-6.288924,-0.914969,-2.382681,-7.656369,-6.422694,-9.604668,-5.556764,-9.323808,0.692774,7.369092,8.499354,-0.511330,3.820931,5.350630,-6.523395,6.929294,-6.513343,-9.057815,-7.065948,-4.977505,3.211650,-4.234379,7.308917,2.265198,8.071304,-1.694483,-6.762890,-4.244375,-8.646918,-3.125762,-1.566917,1.700735,3.716963,-1.990538,-5.123910,1.886375,4.157952,-0.724299,-0.754682,3.250225,-0.824198,-4.583728,-8.176703,-9.410790,2.529472,4.857623,2.915549,-0.010821,2.149739,-1.404711,1.952563,9.171972,9.431783,-0.213830,-1.289359,6.497761,8.093502,2.115653,-6.271090,-3.738697,-9.386918,0.994372,-7.576879,-9.022232,-8.641547,-6.877424,-3.256464,-4.719954,5.439690,6.291795,5.948469,-8.480040,8.132189,-5.834901,4.018912,7.278709,7.891960,6.455896,-9.345284,4.720833,-7.528305,-0.117145,1.855054,-4.470067,8.626340,-1.907038,-3.797596,-2.618983,-9.114924,3.000635,4.661410,5.538552,-8.282867,8.449969,6.236525,6.998827,-2.772506,-3.361467,6.753584,-0.871205,5.466664,6.405983,6.031180,7.620400,-7.360279,0.634230,1.625679,-7.386768,-9.453265,-5.554179,-1.531197,2.280613,3.147297,7.752155,7.936484,-4.707884,-2.589754,-6.402336,4.265436,-8.607907,2.723281,4.099204,-3.843728,-8.215097,4.666889,-4.972820,-7.935228,-2.135362,-7.564697,-5.014527,3.961871,-7.999082,-2.734885,4.680593,-4.336584,-9.165933,-3.191586,-7.248604,5.232124,5.686113,3.320417,5.044903,0.062274,9.388090,6.477223,6.016225,-8.619924,-3.343787,1.330749,-6.366035,1.671596,6.854466,9.055683,6.401713,-5.934711,1.892846,-8.283515,0.632483,6.399030,9.165279,0.152036,0.854503,-6.117052,-9.267655,-5.511939,8.307474,9.353014,8.586307,-0.419921,-8.119951,2.160666,-8.423430,-5.108675,0.363627,3.705965,-8.438623,-1.652552,-7.620953,2.001882,-1.244293,-8.093225,-4.712933,-9.458000,-9.161764,-9.416774,1.145028,-3.654005,7.337609,7.194095,-1.232869,-8.435392,3.765206,3.140258,9.660074,0.490467,-0.251570,-9.247112,8.820111,-1.954593,5.745775,-1.231974,-7.093660,7.845231,2.909998,-0.317404,9.632068,-0.802122,4.540650,-3.132247,7.989455,-0.408670,6.171447,-6.658092,3.874792,-0.128501,0.171680,7.021319,-4.036797,3.398834,-9.909086,1.108854,-5.951659,-3.205473,3.121616,5.909114,-0.980120,-8.618636,-4.812458,3.587388,0.613652,-6.993480,-3.745340,-8.183330,-1.009966,0.829354,-5.025717,-7.924672,-5.472429,-8.844377,-3.179335,-2.285333,-6.895905,-3.620811,1.982994,-7.061452,-4.412183,7.379821,0.067388,7.748456,-3.388537,-4.049431,4.382132,3.893818,6.409092,-6.221967,4.552658,2.331844,9.264499,-2.218857,1.288211,-0.830899,-3.127626,-9.246415,3.130688,1.357245,-6.843946,-6.173590,2.312921,-2.756333,-2.941427,-4.438315,3.821899,8.827986,7.267176,-7.827652,-8.235489,-2.903540,-5.258872,-0.500947,-0.735173,3.674077,2.026297,6.394404,-2.982106,-6.912687,-0.515037,-9.502442,-0.009921,-3.112533,-7.220855,-1.546509,7.706241,6.852068,5.170189,-3.294272,3.533329,3.026385,0.387038,7.161439,-4.728402,-2.157520,-1.876446], dtype = "float32")#candidate|4420|(550,)|const|float32
call_4417 = relay.TupleGetItem(func_3406_call(relay.reshape(const_4418.astype('uint8'), [96,]), relay.reshape(const_4419.astype('float32'), [3072,]), relay.reshape(const_4420.astype('float32'), [550,]), ), 8)
call_4421 = relay.TupleGetItem(func_3411_call(relay.reshape(const_4418.astype('uint8'), [96,]), relay.reshape(const_4419.astype('float32'), [3072,]), relay.reshape(const_4420.astype('float32'), [550,]), ), 8)
const_4422 = relay.const([[[-10,4,-1,-8,9,3,-3,7,-6,-2,-7,3,-4,-1],[-7,-3,-5,4,9,4,-5,1,-1,6,3,8,-8,-4],[-6,-9,9,1,-9,1,-8,-8,-2,-8,1,2,2,6],[1,-4,6,-1,7,8,-6,6,3,-6,6,10,8,1],[-2,-1,4,1,9,4,5,-4,8,6,7,-10,5,-10],[2,2,6,-8,-7,2,-4,-5,-8,-1,-10,-10,10,-8],[10,6,9,7,-1,8,5,-7,-8,-9,9,5,-10,6]],[[6,2,2,-9,10,-8,2,-9,8,7,6,4,-7,-7],[-5,6,-7,-7,-10,1,2,-9,5,-1,-5,3,-6,1],[8,-2,-10,-4,9,-9,-6,7,10,-2,7,10,-6,5],[1,-7,3,4,8,-4,9,-5,2,5,-7,6,2,6],[-10,10,-7,2,6,7,6,-2,3,-2,-9,-8,3,2],[2,3,-1,7,2,9,-7,-4,8,-10,3,-7,-8,-9],[-10,6,9,8,-4,9,4,4,4,6,3,-4,-5,-1]],[[7,4,10,-1,-1,10,-2,9,-7,-9,2,5,-1,-4],[-10,-9,-4,6,5,3,-6,9,-2,-6,-3,9,10,3],[-3,-8,-1,-9,2,-8,-3,-10,6,9,-2,-6,-9,2],[-1,1,-9,6,-7,-4,-2,-5,5,-4,-9,-8,7,5],[3,7,2,7,-8,3,1,6,10,-10,1,6,6,-10],[-10,-1,4,-8,-6,8,-9,1,8,5,1,5,-9,1],[-6,10,-9,10,9,-10,4,-2,8,-5,3,4,-3,-7]],[[1,8,10,-5,9,10,3,6,7,2,-1,2,5,9],[7,10,3,-5,-8,-2,8,-8,4,-10,-1,-8,7,8],[8,-2,1,-4,2,7,-4,8,1,-2,-9,7,3,2],[-7,-4,8,-1,7,-5,-9,-10,1,4,3,8,6,-2],[3,1,-4,5,10,-3,5,10,10,8,8,-5,6,1],[-3,3,6,-5,10,4,-8,-10,7,-9,-10,8,9,-8],[-9,8,-1,7,6,2,2,9,5,2,-9,-8,-10,-8]],[[-2,-1,-5,-4,-2,6,2,6,-3,1,4,1,6,4],[-6,2,-7,8,6,10,2,3,-5,-6,-4,8,4,-1],[7,-6,-6,-10,5,-8,-9,-6,6,2,10,2,7,-2],[-7,1,6,8,8,-8,-5,6,5,-4,-3,4,6,-9],[-4,-6,-2,9,-6,2,5,1,-6,-4,8,4,6,-9],[2,7,-9,-10,-2,10,6,-4,-2,10,9,-1,-4,10],[-2,2,7,1,2,6,10,2,8,6,-8,-9,4,7]]], dtype = "int64")#candidate|4422|(5, 7, 14)|const|int64
bop_4423 = relay.logical_xor(var_4413.astype('uint8'), const_4422.astype('uint8')) # shape=(5, 7, 14)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_4428 = func_1632_call()
call_4429 = func_1632_call()
output = relay.Tuple([call_4382,call_4404,call_4412,const_4414,const_4415,call_4417,const_4418,const_4419,const_4420,bop_4423,call_4428,])
output2 = relay.Tuple([call_4383,call_4405,call_4416,const_4414,const_4415,call_4421,const_4418,const_4419,const_4420,bop_4423,call_4429,])
func_4430 = relay.Function([var_4413,], output)
mod['func_4430'] = func_4430
mod = relay.transform.InferType()(mod)
mutated_mod['func_4430'] = func_4430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4431 = relay.var("var_4431", dtype = "int64", shape = ())#candidate|4431|()|var|int64
func_4430_call = mutated_mod.get_global_var('func_4430')
call_4432 = func_4430_call(var_4431)
output = call_4432
func_4433 = relay.Function([var_4431], output)
mutated_mod['func_4433'] = func_4433
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4435 = relay.var("var_4435", dtype = "float32", shape = (6, 11, 7))#candidate|4435|(6, 11, 7)|var|float32
var_4436 = relay.var("var_4436", dtype = "float32", shape = (6, 11, 7))#candidate|4436|(6, 11, 7)|var|float32
bop_4437 = relay.minimum(var_4435.astype('float32'), relay.reshape(var_4436.astype('float32'), relay.shape_of(var_4435))) # shape=(6, 11, 7)
output = relay.Tuple([bop_4437,])
output2 = relay.Tuple([bop_4437,])
func_4454 = relay.Function([var_4435,var_4436,], output)
mod['func_4454'] = func_4454
mod = relay.transform.InferType()(mod)
mutated_mod['func_4454'] = func_4454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4454_call = mutated_mod.get_global_var('func_4454')
var_4456 = relay.var("var_4456", dtype = "float32", shape = (6, 11, 7))#candidate|4456|(6, 11, 7)|var|float32
var_4457 = relay.var("var_4457", dtype = "float32", shape = (6, 11, 7))#candidate|4457|(6, 11, 7)|var|float32
call_4455 = func_4454_call(var_4456,var_4457,)
output = call_4455
func_4458 = relay.Function([var_4456,var_4457,], output)
mutated_mod['func_4458'] = func_4458
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4528 = relay.var("var_4528", dtype = "int64", shape = (8, 11, 12))#candidate|4528|(8, 11, 12)|var|int64
var_4529 = relay.var("var_4529", dtype = "int64", shape = (8, 11, 12))#candidate|4529|(8, 11, 12)|var|int64
bop_4530 = relay.subtract(var_4528.astype('int64'), relay.reshape(var_4529.astype('int64'), relay.shape_of(var_4528))) # shape=(8, 11, 12)
uop_4534 = relay.sinh(var_4529.astype('float32')) # shape=(8, 11, 12)
var_4548 = relay.var("var_4548", dtype = "float32", shape = (8, 11, 12))#candidate|4548|(8, 11, 12)|var|float32
bop_4549 = relay.add(uop_4534.astype('uint8'), relay.reshape(var_4548.astype('uint8'), relay.shape_of(uop_4534))) # shape=(8, 11, 12)
output = relay.Tuple([bop_4530,bop_4549,])
output2 = relay.Tuple([bop_4530,bop_4549,])
func_4553 = relay.Function([var_4528,var_4529,var_4548,], output)
mod['func_4553'] = func_4553
mod = relay.transform.InferType()(mod)
mutated_mod['func_4553'] = func_4553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4553_call = mutated_mod.get_global_var('func_4553')
var_4555 = relay.var("var_4555", dtype = "int64", shape = (8, 11, 12))#candidate|4555|(8, 11, 12)|var|int64
var_4556 = relay.var("var_4556", dtype = "int64", shape = (8, 11, 12))#candidate|4556|(8, 11, 12)|var|int64
var_4557 = relay.var("var_4557", dtype = "float32", shape = (8, 11, 12))#candidate|4557|(8, 11, 12)|var|float32
call_4554 = func_4553_call(var_4555,var_4556,var_4557,)
output = call_4554
func_4558 = relay.Function([var_4555,var_4556,var_4557,], output)
mutated_mod['func_4558'] = func_4558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1721_call = mod.get_global_var('func_1721')
func_1722_call = mutated_mod.get_global_var('func_1722')
call_4583 = relay.TupleGetItem(func_1721_call(), 0)
call_4584 = relay.TupleGetItem(func_1722_call(), 0)
output = relay.Tuple([call_4583,])
output2 = relay.Tuple([call_4584,])
func_4610 = relay.Function([], output)
mod['func_4610'] = func_4610
mod = relay.transform.InferType()(mod)
output = func_4610()
func_4611 = relay.Function([], output)
mutated_mod['func_4611'] = func_4611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1554_call = mod.get_global_var('func_1554')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_4676 = relay.TupleGetItem(func_1554_call(), 0)
call_4677 = relay.TupleGetItem(func_1556_call(), 0)
var_4685 = relay.var("var_4685", dtype = "float32", shape = (2, 5, 8))#candidate|4685|(2, 5, 8)|var|float32
bop_4686 = relay.bitwise_and(call_4676.astype('int64'), relay.reshape(var_4685.astype('int64'), relay.shape_of(call_4676))) # shape=(2, 5, 8)
bop_4689 = relay.bitwise_and(call_4677.astype('int64'), relay.reshape(var_4685.astype('int64'), relay.shape_of(call_4677))) # shape=(2, 5, 8)
func_1751_call = mod.get_global_var('func_1751')
func_1752_call = mutated_mod.get_global_var('func_1752')
call_4704 = func_1751_call()
call_4705 = func_1751_call()
func_1124_call = mod.get_global_var('func_1124')
func_1127_call = mutated_mod.get_global_var('func_1127')
var_4727 = relay.var("var_4727", dtype = "float64", shape = (384,))#candidate|4727|(384,)|var|float64
call_4726 = relay.TupleGetItem(func_1124_call(relay.reshape(var_4727.astype('float64'), [384,])), 1)
call_4728 = relay.TupleGetItem(func_1127_call(relay.reshape(var_4727.astype('float64'), [384,])), 1)
output = relay.Tuple([bop_4686,call_4704,call_4726,var_4727,])
output2 = relay.Tuple([bop_4689,call_4705,call_4728,var_4727,])
func_4729 = relay.Function([var_4685,var_4727,], output)
mod['func_4729'] = func_4729
mod = relay.transform.InferType()(mod)
mutated_mod['func_4729'] = func_4729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4729_call = mutated_mod.get_global_var('func_4729')
var_4731 = relay.var("var_4731", dtype = "float32", shape = (2, 5, 8))#candidate|4731|(2, 5, 8)|var|float32
var_4732 = relay.var("var_4732", dtype = "float64", shape = (384,))#candidate|4732|(384,)|var|float64
call_4730 = func_4729_call(var_4731,var_4732,)
output = call_4730
func_4733 = relay.Function([var_4731,var_4732,], output)
mutated_mod['func_4733'] = func_4733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3741_call = mod.get_global_var('func_3741')
func_3743_call = mutated_mod.get_global_var('func_3743')
call_4766 = relay.TupleGetItem(func_3741_call(), 0)
call_4767 = relay.TupleGetItem(func_3743_call(), 0)
output = relay.Tuple([call_4766,])
output2 = relay.Tuple([call_4767,])
func_4792 = relay.Function([], output)
mod['func_4792'] = func_4792
mod = relay.transform.InferType()(mod)
output = func_4792()
func_4793 = relay.Function([], output)
mutated_mod['func_4793'] = func_4793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1554_call = mod.get_global_var('func_1554')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_4807 = relay.TupleGetItem(func_1554_call(), 0)
call_4808 = relay.TupleGetItem(func_1556_call(), 0)
func_2634_call = mod.get_global_var('func_2634')
func_2637_call = mutated_mod.get_global_var('func_2637')
const_4812 = relay.const([[9.448024,0.707321,-9.650803,-1.869772,2.756280,-9.437892,3.765644,-5.019765,9.620133,9.608466,-6.669499,7.926806,9.063735,8.368796,6.576003,8.378045,5.339283,-5.687258,-2.949666,-9.148401,-5.276370,9.688071]], dtype = "float64")#candidate|4812|(1, 22)|const|float64
call_4811 = relay.TupleGetItem(func_2634_call(relay.reshape(const_4812.astype('float64'), [2, 11, 1])), 0)
call_4813 = relay.TupleGetItem(func_2637_call(relay.reshape(const_4812.astype('float64'), [2, 11, 1])), 0)
output = relay.Tuple([call_4807,call_4811,const_4812,])
output2 = relay.Tuple([call_4808,call_4813,const_4812,])
func_4829 = relay.Function([], output)
mod['func_4829'] = func_4829
mod = relay.transform.InferType()(mod)
output = func_4829()
func_4830 = relay.Function([], output)
mutated_mod['func_4830'] = func_4830
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4884 = relay.const([[[9,3,-6,-1,-8,8,-7,-5],[2,4,10,-3,-10,7,-8,-7],[10,4,-3,-4,-7,4,-3,-10],[-5,-8,-4,-1,1,-2,-8,5],[-8,-7,3,-1,4,-6,-4,-1],[-3,-3,1,-1,-3,-3,-1,2],[7,-2,1,-1,-7,-3,5,2],[-2,-5,9,7,-7,5,-7,7],[6,-4,-3,3,4,-2,7,-7],[9,4,-7,1,9,2,-3,-2],[10,-4,-1,-4,-3,5,10,-1]],[[-3,-6,5,-4,3,2,9,-3],[-8,-2,5,5,2,-8,-2,-1],[1,7,7,10,-1,8,-6,9],[-1,4,-6,-2,9,-1,8,-9],[-3,6,-10,-2,1,-1,2,-1],[-10,8,2,-6,-1,-3,3,9],[8,6,4,-1,9,-9,1,-5],[-5,-10,-3,9,7,5,5,6],[1,-3,9,9,-7,10,-10,-10],[-7,1,9,8,-3,-4,8,2],[-1,4,3,1,-2,8,7,7]],[[10,-6,8,-3,-6,7,-8,-3],[8,-2,-9,-10,3,4,-8,3],[-7,-5,2,5,-8,2,-3,-6],[2,-3,8,-3,1,-2,-6,-7],[6,9,-9,-8,7,2,6,-3],[5,-1,-9,-5,-2,1,1,-5],[7,5,-8,-4,4,5,3,8],[3,-2,-4,5,3,-5,2,-3],[4,7,-2,7,9,6,9,2],[1,-6,-1,10,7,-2,7,-9],[7,5,9,5,-5,9,-3,7]],[[7,9,-4,-3,8,9,-3,10],[-6,-9,-8,-2,5,6,4,-4],[-9,-8,5,4,-9,9,-3,1],[-4,4,-5,5,-8,10,6,-3],[-8,-8,2,-6,-6,2,4,9],[-4,-9,1,-10,7,-3,5,-6],[6,-6,5,-1,7,-10,-7,-8],[-4,-3,-1,4,-5,10,2,3],[-1,8,2,-9,-3,9,-2,2],[-4,-10,7,4,2,2,-2,-2],[5,-3,9,6,-2,1,-2,9]],[[9,-2,5,8,9,-3,-4,-8],[-7,6,2,8,-6,6,-4,-3],[-4,7,10,9,5,4,7,8],[2,9,-5,8,6,1,-8,-2],[1,2,-7,5,-2,-9,3,-2],[1,-1,-8,10,-2,3,5,-2],[7,10,-6,-5,-5,7,2,-5],[1,-9,-2,5,10,-3,5,3],[-9,7,-9,-4,-7,-4,-10,-3],[-2,2,-3,-7,-6,8,-6,-5],[-6,-10,5,9,5,-2,-2,-8]],[[1,-8,8,7,-8,5,-6,10],[-3,6,4,-1,-1,-4,9,-7],[3,-5,3,-4,7,-8,10,-4],[8,-10,-9,1,-3,5,6,-4],[-7,9,9,4,3,-8,10,5],[-5,-2,5,4,-8,-3,1,5],[-4,-10,8,-2,6,3,3,-5],[2,-3,-1,-8,-8,-7,-6,-6],[7,-7,10,3,9,-1,3,-3],[3,5,-2,7,3,8,-4,-2],[-10,3,10,7,3,4,-6,-4]],[[-2,5,1,-6,3,6,8,-8],[8,-10,1,-10,7,-2,-8,4],[-5,-5,-10,-3,-3,-2,-6,1],[4,-2,1,1,5,-3,-10,-4],[7,-3,8,-9,4,4,-4,4],[8,-4,10,-9,9,-10,10,-5],[-5,3,6,-6,3,-8,7,-6],[-10,4,-6,-4,6,7,2,-2],[-2,-10,-6,7,-8,-6,-9,-10],[3,-6,6,5,6,9,-3,2],[-3,-4,-1,-10,-7,6,9,4]],[[9,-4,-10,8,-10,-5,-7,10],[1,10,-6,3,-7,1,4,-9],[-5,-7,-1,-4,-1,7,6,-7],[-3,3,5,5,4,9,3,-10],[-10,-7,1,5,-10,7,8,-5],[2,10,-3,-1,-5,6,8,-8],[2,-3,-7,-4,-9,-3,6,9],[5,5,-6,-6,7,-9,-7,-5],[-2,-1,-7,6,-5,-2,-8,-8],[10,-2,10,-9,1,3,-7,-6],[-7,8,9,9,-4,4,1,6]],[[5,-10,-7,1,-9,5,-3,4],[7,3,7,-1,-4,-4,6,8],[7,6,9,1,2,-3,-8,-6],[-9,2,-2,1,-9,2,-5,5],[-2,-8,-8,8,-5,-4,8,-8],[8,4,-5,7,10,-9,10,8],[7,-3,-3,5,-4,2,1,-10],[2,-9,1,-10,5,-7,-5,9],[1,7,4,5,-10,-3,-5,-10],[-9,5,-6,4,-6,8,-7,3],[8,-3,9,2,3,2,8,-6]],[[-2,-10,5,2,4,3,7,-9],[-6,-7,10,-6,-7,-2,2,-4],[10,5,-8,7,4,-1,-7,-6],[-3,-10,4,-6,6,-6,10,5],[5,-5,4,3,5,-1,-4,-7],[-1,10,5,-8,7,-1,5,-7],[3,-3,6,-7,10,3,-6,-3],[-7,6,-2,-3,10,6,-8,-8],[-6,10,-5,-3,6,10,-8,10],[-5,-7,1,-6,6,6,6,6],[5,4,-2,6,6,-9,9,10]],[[-4,-1,-1,-5,8,10,5,5],[-2,1,-7,2,-1,8,10,3],[6,-8,10,3,-5,1,-9,-2],[-7,-6,8,-8,9,-10,-3,-5],[-9,-8,-8,-7,6,-3,-8,7],[-7,-10,1,7,-3,10,-2,-8],[10,9,9,-1,8,1,10,-1],[-10,-4,-10,-10,-6,10,-5,-8],[-4,-3,3,-9,7,-6,7,3],[-10,-8,-8,3,9,1,-2,1],[5,1,7,10,-10,-2,-4,4]],[[-4,2,1,5,3,-5,6,-2],[-9,1,-3,-1,-5,-9,10,3],[-8,-3,4,-8,-3,-9,7,9],[6,-4,-1,1,-10,7,6,1],[6,-2,1,5,-2,-2,-10,7],[-5,3,7,-3,6,6,-1,5],[-10,-10,-4,-6,3,-7,3,7],[4,3,5,8,-8,-3,-1,10],[3,4,-7,6,-8,-1,5,-8],[-9,2,-7,-5,-7,7,5,3],[7,5,-8,4,-4,-9,-2,-9]],[[8,-6,4,-1,10,-2,5,-2],[1,-6,10,6,-4,2,4,8],[-5,-6,-6,3,-4,10,8,-2],[1,9,8,5,4,10,1,7],[-2,4,-9,3,-1,3,-5,10],[4,7,-7,-6,10,-9,3,6],[9,3,-6,-1,7,6,-8,-6],[-6,-4,5,-5,3,-5,-10,-2],[-10,6,9,-5,-9,8,7,-10],[9,9,-4,-9,10,3,-5,-8],[-10,-3,10,-5,10,6,9,2]]], dtype = "uint32")#candidate|4884|(13, 11, 8)|const|uint32
var_4885 = relay.var("var_4885", dtype = "uint32", shape = (13, 11, 8))#candidate|4885|(13, 11, 8)|var|uint32
bop_4886 = relay.add(const_4884.astype('uint32'), relay.reshape(var_4885.astype('uint32'), relay.shape_of(const_4884))) # shape=(13, 11, 8)
output = bop_4886
output2 = bop_4886
func_4898 = relay.Function([var_4885,], output)
mod['func_4898'] = func_4898
mod = relay.transform.InferType()(mod)
mutated_mod['func_4898'] = func_4898
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4899 = relay.var("var_4899", dtype = "uint32", shape = (13, 11, 8))#candidate|4899|(13, 11, 8)|var|uint32
func_4898_call = mutated_mod.get_global_var('func_4898')
call_4900 = func_4898_call(var_4899)
output = call_4900
func_4901 = relay.Function([var_4899], output)
mutated_mod['func_4901'] = func_4901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_4934 = relay.TupleGetItem(func_606_call(), 0)
call_4935 = relay.TupleGetItem(func_608_call(), 0)
func_2365_call = mod.get_global_var('func_2365')
func_2367_call = mutated_mod.get_global_var('func_2367')
call_4941 = relay.TupleGetItem(func_2365_call(), 1)
call_4942 = relay.TupleGetItem(func_2367_call(), 1)
func_2634_call = mod.get_global_var('func_2634')
func_2637_call = mutated_mod.get_global_var('func_2637')
const_4944 = relay.const([6.153080,-6.233996,5.694359,-6.186513,8.322759,8.847695,1.101518,-9.473908,8.182337,-9.514170,-3.997850,1.324646,-3.594926,-9.250394,0.377453,0.232382,0.238144,7.628093,3.634589,-9.845902,1.444169,5.614648], dtype = "float64")#candidate|4944|(22,)|const|float64
call_4943 = relay.TupleGetItem(func_2634_call(relay.reshape(const_4944.astype('float64'), [2, 11, 1])), 0)
call_4945 = relay.TupleGetItem(func_2637_call(relay.reshape(const_4944.astype('float64'), [2, 11, 1])), 0)
output = relay.Tuple([call_4934,call_4941,call_4943,const_4944,])
output2 = relay.Tuple([call_4935,call_4942,call_4945,const_4944,])
func_4948 = relay.Function([], output)
mod['func_4948'] = func_4948
mod = relay.transform.InferType()(mod)
mutated_mod['func_4948'] = func_4948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4948_call = mutated_mod.get_global_var('func_4948')
call_4949 = func_4948_call()
output = call_4949
func_4950 = relay.Function([], output)
mutated_mod['func_4950'] = func_4950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1450_call = mod.get_global_var('func_1450')
func_1452_call = mutated_mod.get_global_var('func_1452')
call_4973 = func_1450_call()
call_4974 = func_1450_call()
output = relay.Tuple([call_4973,])
output2 = relay.Tuple([call_4974,])
func_4993 = relay.Function([], output)
mod['func_4993'] = func_4993
mod = relay.transform.InferType()(mod)
output = func_4993()
func_4994 = relay.Function([], output)
mutated_mod['func_4994'] = func_4994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_792_call = mod.get_global_var('func_792')
func_794_call = mutated_mod.get_global_var('func_794')
call_5097 = func_792_call()
call_5098 = func_792_call()
uop_5104 = relay.sigmoid(call_5097.astype('float32')) # shape=(2, 5, 8)
uop_5106 = relay.sigmoid(call_5098.astype('float32')) # shape=(2, 5, 8)
func_3960_call = mod.get_global_var('func_3960')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_5115 = func_3960_call()
call_5116 = func_3960_call()
output = relay.Tuple([uop_5104,call_5115,])
output2 = relay.Tuple([uop_5106,call_5116,])
func_5117 = relay.Function([], output)
mod['func_5117'] = func_5117
mod = relay.transform.InferType()(mod)
mutated_mod['func_5117'] = func_5117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5117_call = mutated_mod.get_global_var('func_5117')
call_5118 = func_5117_call()
output = call_5118
func_5119 = relay.Function([], output)
mutated_mod['func_5119'] = func_5119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_5132 = relay.TupleGetItem(func_2017_call(), 0)
call_5133 = relay.TupleGetItem(func_2018_call(), 0)
output = relay.Tuple([call_5132,])
output2 = relay.Tuple([call_5133,])
func_5151 = relay.Function([], output)
mod['func_5151'] = func_5151
mod = relay.transform.InferType()(mod)
mutated_mod['func_5151'] = func_5151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5151_call = mutated_mod.get_global_var('func_5151')
call_5152 = func_5151_call()
output = call_5152
func_5153 = relay.Function([], output)
mutated_mod['func_5153'] = func_5153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_5173 = func_1609_call()
call_5174 = func_1609_call()
output = call_5173
output2 = call_5174
func_5187 = relay.Function([], output)
mod['func_5187'] = func_5187
mod = relay.transform.InferType()(mod)
mutated_mod['func_5187'] = func_5187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5187_call = mutated_mod.get_global_var('func_5187')
call_5188 = func_5187_call()
output = call_5188
func_5189 = relay.Function([], output)
mutated_mod['func_5189'] = func_5189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4829_call = mod.get_global_var('func_4829')
func_4830_call = mutated_mod.get_global_var('func_4830')
call_5208 = relay.TupleGetItem(func_4829_call(), 2)
call_5209 = relay.TupleGetItem(func_4830_call(), 2)
output = relay.Tuple([call_5208,])
output2 = relay.Tuple([call_5209,])
func_5217 = relay.Function([], output)
mod['func_5217'] = func_5217
mod = relay.transform.InferType()(mod)
output = func_5217()
func_5218 = relay.Function([], output)
mutated_mod['func_5218'] = func_5218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1450_call = mod.get_global_var('func_1450')
func_1452_call = mutated_mod.get_global_var('func_1452')
call_5224 = func_1450_call()
call_5225 = func_1450_call()
output = relay.Tuple([call_5224,])
output2 = relay.Tuple([call_5225,])
func_5244 = relay.Function([], output)
mod['func_5244'] = func_5244
mod = relay.transform.InferType()(mod)
output = func_5244()
func_5245 = relay.Function([], output)
mutated_mod['func_5245'] = func_5245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1554_call = mod.get_global_var('func_1554')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_5248 = relay.TupleGetItem(func_1554_call(), 0)
call_5249 = relay.TupleGetItem(func_1556_call(), 0)
output = relay.Tuple([call_5248,])
output2 = relay.Tuple([call_5249,])
func_5256 = relay.Function([], output)
mod['func_5256'] = func_5256
mod = relay.transform.InferType()(mod)
output = func_5256()
func_5257 = relay.Function([], output)
mutated_mod['func_5257'] = func_5257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1070_call = mod.get_global_var('func_1070')
func_1071_call = mutated_mod.get_global_var('func_1071')
call_5262 = func_1070_call()
call_5263 = func_1070_call()
func_3509_call = mod.get_global_var('func_3509')
func_3513_call = mutated_mod.get_global_var('func_3513')
var_5274 = relay.var("var_5274", dtype = "uint32", shape = ())#candidate|5274|()|var|uint32
const_5275 = relay.const([-2,6,4,-8,5,-9,-3,7,8,5,-7,2,4,-2,-10,2,2,3,5,-4,-9,-5,4,6,-4,-4,5,-4,9,-5,-4,2,5,3,-9,4,8,10,3,-5,-1,5,-7,9,4,-5,-1,4], dtype = "uint32")#candidate|5275|(48,)|const|uint32
call_5273 = relay.TupleGetItem(func_3509_call(relay.reshape(var_5274.astype('uint32'), []), relay.reshape(const_5275.astype('uint32'), [8, 6, 1]), ), 0)
call_5276 = relay.TupleGetItem(func_3513_call(relay.reshape(var_5274.astype('uint32'), []), relay.reshape(const_5275.astype('uint32'), [8, 6, 1]), ), 0)
output = relay.Tuple([call_5262,call_5273,var_5274,const_5275,])
output2 = relay.Tuple([call_5263,call_5276,var_5274,const_5275,])
func_5284 = relay.Function([var_5274,], output)
mod['func_5284'] = func_5284
mod = relay.transform.InferType()(mod)
var_5285 = relay.var("var_5285", dtype = "uint32", shape = ())#candidate|5285|()|var|uint32
output = func_5284(var_5285)
func_5286 = relay.Function([var_5285], output)
mutated_mod['func_5286'] = func_5286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5217_call = mod.get_global_var('func_5217')
func_5218_call = mutated_mod.get_global_var('func_5218')
call_5291 = relay.TupleGetItem(func_5217_call(), 0)
call_5292 = relay.TupleGetItem(func_5218_call(), 0)
output = relay.Tuple([call_5291,])
output2 = relay.Tuple([call_5292,])
func_5300 = relay.Function([], output)
mod['func_5300'] = func_5300
mod = relay.transform.InferType()(mod)
mutated_mod['func_5300'] = func_5300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5300_call = mutated_mod.get_global_var('func_5300')
call_5301 = func_5300_call()
output = call_5301
func_5302 = relay.Function([], output)
mutated_mod['func_5302'] = func_5302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4993_call = mod.get_global_var('func_4993')
func_4994_call = mutated_mod.get_global_var('func_4994')
call_5323 = relay.TupleGetItem(func_4993_call(), 0)
call_5324 = relay.TupleGetItem(func_4994_call(), 0)
func_3599_call = mod.get_global_var('func_3599')
func_3600_call = mutated_mod.get_global_var('func_3600')
call_5372 = relay.TupleGetItem(func_3599_call(), 3)
call_5373 = relay.TupleGetItem(func_3600_call(), 3)
output = relay.Tuple([call_5323,call_5372,])
output2 = relay.Tuple([call_5324,call_5373,])
func_5374 = relay.Function([], output)
mod['func_5374'] = func_5374
mod = relay.transform.InferType()(mod)
output = func_5374()
func_5375 = relay.Function([], output)
mutated_mod['func_5375'] = func_5375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1721_call = mod.get_global_var('func_1721')
func_1722_call = mutated_mod.get_global_var('func_1722')
call_5376 = relay.TupleGetItem(func_1721_call(), 0)
call_5377 = relay.TupleGetItem(func_1722_call(), 0)
output = relay.Tuple([call_5376,])
output2 = relay.Tuple([call_5377,])
func_5402 = relay.Function([], output)
mod['func_5402'] = func_5402
mod = relay.transform.InferType()(mod)
output = func_5402()
func_5403 = relay.Function([], output)
mutated_mod['func_5403'] = func_5403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mod.get_global_var('func_1892')
func_1893_call = mutated_mod.get_global_var('func_1893')
call_5416 = relay.TupleGetItem(func_1892_call(), 3)
call_5417 = relay.TupleGetItem(func_1893_call(), 3)
func_1659_call = mod.get_global_var('func_1659')
func_1660_call = mutated_mod.get_global_var('func_1660')
call_5427 = func_1659_call()
call_5428 = func_1659_call()
output = relay.Tuple([call_5416,call_5427,])
output2 = relay.Tuple([call_5417,call_5428,])
func_5432 = relay.Function([], output)
mod['func_5432'] = func_5432
mod = relay.transform.InferType()(mod)
mutated_mod['func_5432'] = func_5432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5432_call = mutated_mod.get_global_var('func_5432')
call_5433 = func_5432_call()
output = call_5433
func_5434 = relay.Function([], output)
mutated_mod['func_5434'] = func_5434
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5441 = relay.var("var_5441", dtype = "uint32", shape = ())#candidate|5441|()|var|uint32
var_5442 = relay.var("var_5442", dtype = "uint32", shape = (14, 7, 2))#candidate|5442|(14, 7, 2)|var|uint32
bop_5443 = relay.multiply(var_5441.astype('uint32'), var_5442.astype('uint32')) # shape=(14, 7, 2)
func_1554_call = mod.get_global_var('func_1554')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_5455 = relay.TupleGetItem(func_1554_call(), 0)
call_5456 = relay.TupleGetItem(func_1556_call(), 0)
output = relay.Tuple([bop_5443,call_5455,])
output2 = relay.Tuple([bop_5443,call_5456,])
func_5463 = relay.Function([var_5441,var_5442,], output)
mod['func_5463'] = func_5463
mod = relay.transform.InferType()(mod)
var_5464 = relay.var("var_5464", dtype = "uint32", shape = ())#candidate|5464|()|var|uint32
var_5465 = relay.var("var_5465", dtype = "uint32", shape = (14, 7, 2))#candidate|5465|(14, 7, 2)|var|uint32
output = func_5463(var_5464,var_5465,)
func_5466 = relay.Function([var_5464,var_5465,], output)
mutated_mod['func_5466'] = func_5466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_5486 = relay.TupleGetItem(func_573_call(), 0)
call_5487 = relay.TupleGetItem(func_574_call(), 0)
func_1892_call = mod.get_global_var('func_1892')
func_1893_call = mutated_mod.get_global_var('func_1893')
call_5494 = relay.TupleGetItem(func_1892_call(), 0)
call_5495 = relay.TupleGetItem(func_1893_call(), 0)
output = relay.Tuple([call_5486,call_5494,])
output2 = relay.Tuple([call_5487,call_5495,])
func_5525 = relay.Function([], output)
mod['func_5525'] = func_5525
mod = relay.transform.InferType()(mod)
mutated_mod['func_5525'] = func_5525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5525_call = mutated_mod.get_global_var('func_5525')
call_5526 = func_5525_call()
output = call_5526
func_5527 = relay.Function([], output)
mutated_mod['func_5527'] = func_5527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5402_call = mod.get_global_var('func_5402')
func_5403_call = mutated_mod.get_global_var('func_5403')
call_5531 = relay.TupleGetItem(func_5402_call(), 0)
call_5532 = relay.TupleGetItem(func_5403_call(), 0)
func_3741_call = mod.get_global_var('func_3741')
func_3743_call = mutated_mod.get_global_var('func_3743')
call_5545 = relay.TupleGetItem(func_3741_call(), 0)
call_5546 = relay.TupleGetItem(func_3743_call(), 0)
func_1911_call = mod.get_global_var('func_1911')
func_1912_call = mutated_mod.get_global_var('func_1912')
call_5560 = relay.TupleGetItem(func_1911_call(), 0)
call_5561 = relay.TupleGetItem(func_1912_call(), 0)
func_4829_call = mod.get_global_var('func_4829')
func_4830_call = mutated_mod.get_global_var('func_4830')
call_5563 = relay.TupleGetItem(func_4829_call(), 0)
call_5564 = relay.TupleGetItem(func_4830_call(), 0)
output = relay.Tuple([call_5531,call_5545,call_5560,call_5563,])
output2 = relay.Tuple([call_5532,call_5546,call_5561,call_5564,])
func_5565 = relay.Function([], output)
mod['func_5565'] = func_5565
mod = relay.transform.InferType()(mod)
mutated_mod['func_5565'] = func_5565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5565_call = mutated_mod.get_global_var('func_5565')
call_5566 = func_5565_call()
output = call_5566
func_5567 = relay.Function([], output)
mutated_mod['func_5567'] = func_5567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_5574 = relay.TupleGetItem(func_4610_call(), 0)
call_5575 = relay.TupleGetItem(func_4611_call(), 0)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_5585 = relay.TupleGetItem(func_3161_call(), 0)
call_5586 = relay.TupleGetItem(func_3162_call(), 0)
func_510_call = mod.get_global_var('func_510')
func_512_call = mutated_mod.get_global_var('func_512')
call_5637 = relay.TupleGetItem(func_510_call(), 0)
call_5638 = relay.TupleGetItem(func_512_call(), 0)
const_5654 = relay.const([[[1.942053,-5.722890,-0.189734,-1.616298,-9.451713,-1.615576],[-3.339787,-0.106806,-0.488848,4.622121,-8.839578,9.242215],[-2.577318,-6.025395,1.222507,8.671889,7.092828,1.249074],[-3.814701,6.707380,-7.380755,-5.917199,-6.220394,2.235467],[1.860033,-5.854098,4.342874,-6.283288,8.415109,0.656708],[-3.150591,4.320541,6.581049,5.911726,6.377427,-8.761128],[-0.260362,-4.930678,2.583578,4.275649,-3.571160,6.611036],[7.812094,7.033881,-5.083774,1.929190,4.988937,-0.842350],[4.741453,3.909996,-0.928041,-0.418064,-1.353851,7.386469]],[[-5.249115,3.259380,-3.411542,3.559278,-7.761895,6.698696],[1.287948,9.457741,8.702769,2.613919,8.100100,6.648693],[-3.160586,8.381679,-1.035200,6.733162,4.036206,-7.939402],[5.795849,-8.719494,-8.034528,-0.128802,-7.378334,3.159651],[1.611933,7.123954,5.493970,4.425043,-7.360367,-8.741260],[1.866890,-3.727129,-3.999155,9.507009,-2.656574,9.887524],[2.651593,-0.754294,7.379491,9.606486,3.045234,-5.242761],[-4.316446,-3.806464,-1.597348,5.142932,-9.602542,-4.363469],[-1.105771,-7.692496,8.680839,-0.202233,1.874854,8.102830]],[[-8.366607,-8.289779,1.883761,-6.347547,-2.750334,-8.050041],[7.482792,-4.175378,0.511145,0.541540,-4.369610,-2.654449],[1.364585,-8.502932,-9.001019,-6.936095,1.157623,-3.474934],[4.608881,-8.996966,1.240926,-9.890609,-8.959410,9.066848],[0.195632,-5.895454,-5.220162,-2.036230,4.717335,1.682097],[-0.048073,-5.476575,-7.167291,-7.326647,9.431187,6.101724],[8.651958,5.871380,-9.512207,-3.905114,8.674934,-2.534639],[7.180276,-6.864904,7.781782,-0.187937,0.964630,9.714669],[5.324977,3.199558,-7.371814,-5.358521,-2.676234,-3.786994]],[[-0.433568,-6.489311,8.137568,7.737834,2.391061,0.656195],[4.090206,-9.523165,-4.324324,-2.509763,1.967777,-5.221970],[-4.171007,-0.877396,-1.944910,-3.777494,8.110401,1.570160],[4.840174,3.715103,-6.396977,1.756351,5.537820,-6.023222],[-5.260902,7.773655,-3.424811,4.200626,-0.937285,9.288827],[-6.818901,9.739885,-7.053669,-7.020779,-6.858739,4.112282],[-9.124681,-1.461403,-3.157745,3.884697,-1.740712,9.707076],[-3.423841,5.946692,-7.333096,-0.345045,-2.113237,-3.572842],[-6.161231,-8.571981,-1.699845,3.310336,8.622684,-1.803361]],[[-3.472060,-0.167727,4.370109,6.813574,-1.158361,-3.295263],[1.346029,-0.170131,0.722020,-0.616781,8.608645,-4.207889],[-1.978076,3.114462,3.253587,-1.809029,9.144640,-7.343767],[-2.341013,6.206226,8.784910,8.781992,-9.589651,-1.633984],[-1.085382,7.087290,-9.210211,4.289514,4.622003,-3.135626],[7.716016,-8.128749,9.557069,7.103445,-0.478122,-8.004943],[-9.957244,-6.872654,7.041923,-3.398403,7.723368,-0.738743],[5.186832,6.961204,-9.161649,-9.314830,-3.217684,-8.974384],[2.372923,7.061441,-0.909955,3.461664,4.178656,9.216155]],[[6.564691,-9.472562,0.166498,-2.830075,-3.022027,3.675054],[1.478617,-7.746586,-0.069492,6.311467,-2.752236,0.625095],[-6.607285,-0.008857,-5.279936,9.434858,6.416657,0.309668],[-4.565336,-2.309285,4.501659,6.346658,2.213373,-6.500828],[-4.406634,2.590494,-1.731025,-5.007792,-9.109521,-5.132620],[-7.848487,-3.319468,9.612309,1.789074,3.164708,-8.573485],[9.961660,9.807255,-3.584008,5.702788,1.079512,9.147463],[0.264549,-0.500215,-8.640025,7.801522,-5.409682,9.413256],[8.644218,7.613248,-3.490710,2.497518,3.403691,-5.043953]],[[-9.729430,7.140693,-1.350797,4.420479,-7.959202,6.529054],[-0.476080,7.045947,-9.288409,-2.555911,8.712727,-8.733988],[0.287766,-3.834504,-8.040976,-1.057672,-1.944471,-7.951087],[0.493203,-6.603907,-2.613567,-0.424365,-5.311627,4.277912],[-5.254003,-4.725484,-0.669912,3.660509,-5.175270,-1.938641],[-2.769630,0.044258,-6.762871,-9.916350,7.973142,5.468838],[-3.484482,-8.246370,-8.482666,-5.601147,0.994704,-6.372902],[4.335199,-5.262357,1.741931,9.867020,6.710518,-8.622469],[-9.568180,0.597239,-3.619673,0.011239,5.552321,1.403527]]], dtype = "float32")#candidate|5654|(7, 9, 6)|const|float32
bop_5655 = relay.greater(call_5585.astype('bool'), relay.reshape(const_5654.astype('bool'), relay.shape_of(call_5585))) # shape=(7, 9, 6)
bop_5658 = relay.greater(call_5586.astype('bool'), relay.reshape(const_5654.astype('bool'), relay.shape_of(call_5586))) # shape=(7, 9, 6)
func_3889_call = mod.get_global_var('func_3889')
func_3890_call = mutated_mod.get_global_var('func_3890')
call_5667 = relay.TupleGetItem(func_3889_call(), 0)
call_5668 = relay.TupleGetItem(func_3890_call(), 0)
func_5300_call = mod.get_global_var('func_5300')
func_5302_call = mutated_mod.get_global_var('func_5302')
call_5669 = relay.TupleGetItem(func_5300_call(), 0)
call_5670 = relay.TupleGetItem(func_5302_call(), 0)
func_2994_call = mod.get_global_var('func_2994')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_5673 = relay.TupleGetItem(func_2994_call(), 1)
call_5674 = relay.TupleGetItem(func_2995_call(), 1)
output = relay.Tuple([call_5574,call_5637,bop_5655,call_5667,call_5669,call_5673,])
output2 = relay.Tuple([call_5575,call_5638,bop_5658,call_5668,call_5670,call_5674,])
func_5687 = relay.Function([], output)
mod['func_5687'] = func_5687
mod = relay.transform.InferType()(mod)
mutated_mod['func_5687'] = func_5687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5687_call = mutated_mod.get_global_var('func_5687')
call_5688 = func_5687_call()
output = call_5688
func_5689 = relay.Function([], output)
mutated_mod['func_5689'] = func_5689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5117_call = mod.get_global_var('func_5117')
func_5119_call = mutated_mod.get_global_var('func_5119')
call_5694 = relay.TupleGetItem(func_5117_call(), 1)
call_5695 = relay.TupleGetItem(func_5119_call(), 1)
func_2885_call = mod.get_global_var('func_2885')
func_2888_call = mutated_mod.get_global_var('func_2888')
call_5700 = relay.TupleGetItem(func_2885_call(relay.reshape(call_5694.astype('float64'), [2, 5, 8])), 1)
call_5701 = relay.TupleGetItem(func_2888_call(relay.reshape(call_5694.astype('float64'), [2, 5, 8])), 1)
func_4729_call = mod.get_global_var('func_4729')
func_4733_call = mutated_mod.get_global_var('func_4733')
const_5720 = relay.const([[-5.119497,4.273777,-4.044553,2.154876,-7.132931,8.898157,6.773183,-7.319461],[-7.624804,7.604805,9.110420,-5.739005,-4.362224,2.698782,-6.023705,-1.694516],[1.099511,1.071515,5.694809,9.711768,-9.579388,-8.398572,6.052247,4.539574],[4.370523,4.229278,9.246174,7.100143,6.442189,-2.063877,5.163238,-3.774442],[3.178969,-0.787751,-3.178596,-1.438273,-7.110530,6.363725,1.604323,-2.468766],[5.766733,0.766049,1.236127,-4.503988,7.894019,-0.290580,6.434407,-4.141213],[2.819886,3.732775,-8.327300,-4.796302,-3.971186,-5.954800,-2.053508,-9.079913],[-3.180117,-4.905874,8.386797,3.657617,-3.891425,8.135107,-6.194889,-2.947233],[2.386501,-3.019812,5.439451,-1.242991,-8.607964,-9.044505,9.879994,-3.948525],[-1.506757,-8.745291,9.680472,6.670081,7.279942,4.604799,-7.061658,9.382380],[1.072503,4.746052,-0.585122,3.281370,-7.156335,4.295729,-7.283054,-3.809754],[2.458046,-7.979568,-8.479159,-8.924503,1.079651,2.576329,6.799698,6.514817],[-5.101525,4.910113,-2.585685,5.799307,-5.220685,3.715974,-5.453043,-7.020993],[-3.635401,-3.468642,-2.051809,-7.114573,-9.628395,0.823266,5.464859,0.614680],[9.224626,-1.104653,3.228045,-9.869221,6.590357,-8.853409,8.294845,1.536033],[-9.448627,-3.882724,-2.388246,-5.067460,3.869341,-1.894302,-6.419490,-0.311670],[-9.894786,3.259480,4.548258,-5.159461,9.995327,-5.489202,2.294556,-5.156900],[-9.623984,-9.940211,-6.620942,3.205624,-6.002795,-8.957466,7.319421,-1.242904],[9.575556,3.714673,0.125236,1.723125,4.831224,-5.570011,8.033586,-5.503999],[3.010038,-2.482828,2.103794,7.889008,4.978647,-6.937218,8.528847,8.135532],[-4.218098,3.893919,-4.241091,1.450442,-2.834399,-9.504354,-6.953551,3.848791],[8.657237,4.591167,-1.495848,-3.000288,-5.385643,-4.349375,2.455410,1.000004],[1.309745,6.082218,1.269251,8.859837,-8.853143,-2.570623,-8.637486,7.228932],[1.386800,-7.846134,6.739895,-5.950642,9.801641,8.010576,-7.860600,-9.634436],[6.593844,6.809325,-8.030518,6.491193,-6.302172,-9.139207,3.387040,-4.938313],[-5.829525,-9.920175,0.959552,-4.196961,-8.755319,4.162595,-9.062655,-5.423859],[1.012034,-0.263279,-9.951946,3.295042,4.642343,9.996834,0.256467,-6.282234],[-7.112848,1.108593,2.196071,-2.319396,-5.704293,-1.160118,2.476717,-0.461713],[-8.207028,6.717899,-2.870474,9.519817,-1.622409,3.001575,-8.036572,7.417916],[-1.375282,-4.550098,-4.740894,2.437228,-8.597476,9.119105,-3.116440,-4.265424],[4.134733,3.394817,-4.120065,6.017579,1.992634,-8.632915,-1.228042,-1.641463],[9.597721,-7.507984,8.757444,-8.132117,6.762056,-5.441059,8.352281,-6.694100],[-7.243930,6.570202,-6.591370,3.493245,0.465404,7.064016,9.068946,-2.821938],[-8.018322,1.273452,9.405646,1.900254,1.727855,-3.590148,4.432022,6.357157],[4.046590,-0.831765,-1.219066,4.066132,-0.733506,5.505096,3.501913,-3.265594],[4.330152,3.639270,5.442312,9.292386,-1.141510,7.937739,7.624003,3.587374],[1.510496,-6.310963,1.431288,4.598597,1.719895,-5.940452,8.977725,-3.700727],[-6.380538,7.848048,6.761697,-3.133883,-3.205972,3.050214,0.838015,-3.090368],[-8.484195,-7.125419,6.497670,0.438761,-7.594235,7.714750,-1.911515,-2.348780],[9.761849,-0.961365,5.810720,2.940484,4.348240,3.458783,4.782304,8.449997],[-3.295702,-1.665565,-3.281413,-5.674516,7.301853,-7.130844,-7.350583,-8.922137],[-2.181755,-1.927520,3.945942,8.436460,-5.890903,2.264802,6.666936,1.705869],[-9.225755,4.672141,-0.693636,-1.077780,4.355826,8.033917,7.468586,7.533238],[3.096602,3.178070,2.213063,6.098939,8.326252,-4.915449,1.679995,9.235891],[1.169655,-8.515146,-0.365970,1.397652,3.391564,5.060212,-4.614315,-8.419005],[-7.888368,-0.411635,6.398692,1.789491,1.640371,8.966068,-7.790946,-9.249586],[1.794082,5.202954,4.591327,2.605174,4.114174,-5.639375,6.413234,9.554453],[-7.324770,-6.418195,1.092450,4.875888,4.750498,-7.112247,3.217800,1.450140]], dtype = "float64")#candidate|5720|(48, 8)|const|float64
call_5719 = relay.TupleGetItem(func_4729_call(relay.reshape(call_5694.astype('float32'), [2, 5, 8]), relay.reshape(const_5720.astype('float64'), [384,]), ), 2)
call_5721 = relay.TupleGetItem(func_4733_call(relay.reshape(call_5694.astype('float32'), [2, 5, 8]), relay.reshape(const_5720.astype('float64'), [384,]), ), 2)
var_5744 = relay.var("var_5744", dtype = "float64", shape = (48, 8))#candidate|5744|(48, 8)|var|float64
bop_5745 = relay.floor_divide(const_5720.astype('float64'), relay.reshape(var_5744.astype('float64'), relay.shape_of(const_5720))) # shape=(48, 8)
output = relay.Tuple([call_5694,call_5700,call_5719,bop_5745,])
output2 = relay.Tuple([call_5695,call_5701,call_5721,bop_5745,])
func_5750 = relay.Function([var_5744,], output)
mod['func_5750'] = func_5750
mod = relay.transform.InferType()(mod)
var_5751 = relay.var("var_5751", dtype = "float64", shape = (48, 8))#candidate|5751|(48, 8)|var|float64
output = func_5750(var_5751)
func_5752 = relay.Function([var_5751], output)
mutated_mod['func_5752'] = func_5752
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5758 = relay.var("var_5758", dtype = "uint32", shape = (14, 16, 9))#candidate|5758|(14, 16, 9)|var|uint32
var_5759 = relay.var("var_5759", dtype = "uint32", shape = (14, 16, 9))#candidate|5759|(14, 16, 9)|var|uint32
bop_5760 = relay.equal(var_5758.astype('bool'), relay.reshape(var_5759.astype('bool'), relay.shape_of(var_5758))) # shape=(14, 16, 9)
func_4553_call = mod.get_global_var('func_4553')
func_4558_call = mutated_mod.get_global_var('func_4558')
const_5764 = relay.const([4,3,5,8,-4,-5,-2,9,7,-10,8,6,-4,6,-9,-5,4,9,-5,7,-1,-4,-9,9,-10,1,-10,4,6,-10,-2,-2,-4,4,-9,-1,-3,5,7,-8,-4,-6,5,-8,7,8,6,-6,10,-2,-2,1,-7,9,-10,-10,3,-9,-4,-1,-7,-2,8,3,-9,9,7,9,6,-5,-3,3,1,-8,10,-5,8,-8,-5,-8,-6,-8,-9,-5,4,-1,7,5,-5,2,-2,-2,6,9,-1,-8,6,-7,2,7,-6,-5,4,2,2,-7,-4,-7,9,2,4,6,-7,-4,7,-8,-2,9,-2,-7,6,1,3,10,3,-1,-5,7,-9,4,-4,2,-3,4,-1,-10,-7,9,-8,-3,5,9,2,-2,9,-9,-8,1,-2,-7,-7,4,-1,-5,5,1,5,-10,8,-8,-7,1,9,-9,6,8,4,-7,-6,-3,2,1,-5,-4,2,-3,-10,6,-8,-2,10,8,-3,-10,-9,2,-8,9,-3,-8,5,-5,8,6,-8,-10,8,4,-3,10,7,3,4,-1,-5,3,-2,4,-2,6,9,-8,-4,-8,-7,8,2,-3,3,3,-3,-7,5,-7,-2,-6,-10,9,9,2,-8,3,-2,-6,8,-3,8,-10,-1,-1,-1,-5,-5,7,-4,3,-9,-1,3,-8,-1,-4,2,3,10,-10,4,3,10,5,-1,5,5,3,-7,8,3,-6,-7,-10,-6,-9,-6,2,-4,-9,7,5,3,-9,10,-6,-9,-9,3,3,-10,2,7,-1,2,4,-7,3,-6,8,-8,-8,-9,5,-6,3,-3,1,2,-10,5,6,-2,2,9,-3,-4,-8,-8,7,1,10,-9,-5,3,5,-9,10,10,-1,-1,8,7,-10,-6,9,-9,3,-9,8,4,-2,4,4,3,3,-2,-1,4,4,-8,-9,-3,6,-3,-8,8,9,3,6,-1,-1,-9,-1,-4,6,1,9,-10,-10,7,-1,9,7,-5,9,3,8,4,6,6,10,-7,-3,-3,-3,10,-7,4,-2,-8,-5,-5,-2,4,-7,-10,-10,-7,6,-8,2,3,-9,-3,5,4,-2,-3,-9,2,7,-4,-9,-2,1,-5,9,10,6,1,-7,-1,5,3,1,2,9,7,-7,6,10,-8,-1,7,6,-7,6,-1,-2,-6,4,-10,-4,-1,-7,-6,8,6,-6,5,2,2,1,-8,2,5,2,6,-4,4,4,10,7,1,8,3,9,-7,-3,-3,-9,-10,6,4,5,-3,1,10,9,9,-9,-7,-10,-9,1,7,-8,2,2,-4,-5,5,10,4,-9,7,7,-8,-2,1,7,-5,6,-9,-5,-5,-1,8,8,-3,5,8,-7,9,1,5,10,3,7,-4,6,-5,-2,2,-5,8,6,3,2,5,4,1,7,-7,7,-1,1,-2,10,-2,9,-6,7,8,-1,-3,2,8,8,-6,-7,8,4,10,3,9,-1,7,-4,5,10,2,-2,1,-8,-6,5,-2,5,-3,1,10,-6,-9,-4,8,4,5,-2,7,5,-4,7,-1,7,1,-5,1,-8,4,7,-5,3,9,6,7,7,-4,-7,-7,9,2,8,5,-6,-5,10,5,10,1,8,-9,-1,-1,8,-3,-3,10,10,7,-4,-10,4,10,-9,-2,-10,4,-6,10,-1,10,9,7,-7,7,7,-8,3,5,-10,1,-9,-3,-9,8,7,-8,-10,-6,-9,10,10,-7,5,-7,8,-5,2,-10,1,3,-6,4,5,-4,-5,-10,-10,8,-6,8,-2,3,-3,6,-2,1,1,-5,7,1,-2,7,-6,9,1,-10,-2,-6,5,-8,1,5,9,8,-9,-8,-2,5,3,1,-3,6,3,10,-5,7,2,-8,1,-6,7,-3,10,-8,-4,-4,2,-2,-3,-5,5,-4,5,5,-10,-8,5,-7,-1,-8,3,-4,4,-2,-10,-5,10,-9,3,-10,-7,1,10,-8,4,8,10,4,7,2,4,2,1,10,-7,7,9,-5,10,1,-9,-3,10,4,-5,5,-8,-7,8,10,-8,-7,-9,-9,8,-4,9,-8,7,6,-8,5,-6,2,-10,9,-3,6,-1,-2,-4,-5,-4,-4,5,-6,1,-9,-6,10,5,-3,-6,-10,-5,-5,9,-6,5,7,-9,2,-4,8,-4,-5,8,9,10,-2,-4,-6,10,-7,1,4,-6,-4,9,-2,10,2,-7,5,-2,4,7,8,-1,2,-10,-6,5,1,-1,7,-2,1,-1,7,-5,-9,3,8,4,-8,8,-3,3,9,6,-5,-6,-8,-5,10,7,10,7,-4,10,5,7,5,1,5,-1,-6,9,3,8,-3,5,7,-1,-2,2,-1,7,-2,-9,6,9,6,-5,-3,-4,-1,8,-10,-6,2,-2,-10,8,-9,-9,6,6,-10,-2,-5,-9,-5,4,-8,10,10,-2,2,2,-4,6,-3,-3,-5,-5,-1,-9,-3,-4,3,2,9,-4,3,-2,-7,8,-3,2,-4,-2,-1,-3,-4,-9,2,-10,5,-4,8,-5,6,-4,4,1,-2,3,4,2,-3,-4,-2,8,6,6,-7,10,6,-4,-1,8,-8,1,-9,9,-3,10,7,3,-7,-7,1,10,3,-10,9,-8,-1,10,-1,3,-3,-9,1,4,-2,4,10,3,-8,-8,10,-7,-4,-10,-5,10,8,-8,1,6,-3,-7,6,6,2,4,-7,-1,-5,7,8,10,7,2,8,-1,10,-3,9,-10,-1,-1,5,-3,-6,2,10,-7,-10,4,9,-8,-5,-7,10,3,4,-2,-7,1,5,-7,-7,-1], dtype = "int64")#candidate|5764|(1056,)|const|int64
call_5763 = relay.TupleGetItem(func_4553_call(relay.reshape(const_5764.astype('int64'), [8, 11, 12]), relay.reshape(const_5764.astype('int64'), [8, 11, 12]), relay.reshape(const_5764.astype('float32'), [8, 11, 12]), ), 1)
call_5765 = relay.TupleGetItem(func_4558_call(relay.reshape(const_5764.astype('int64'), [8, 11, 12]), relay.reshape(const_5764.astype('int64'), [8, 11, 12]), relay.reshape(const_5764.astype('float32'), [8, 11, 12]), ), 1)
func_1512_call = mod.get_global_var('func_1512')
func_1514_call = mutated_mod.get_global_var('func_1514')
call_5777 = relay.TupleGetItem(func_1512_call(), 0)
call_5778 = relay.TupleGetItem(func_1514_call(), 0)
bop_5780 = relay.mod(bop_5760.astype('float64'), relay.reshape(var_5758.astype('float64'), relay.shape_of(bop_5760))) # shape=(14, 16, 9)
bop_5791 = relay.subtract(bop_5760.astype('float64'), relay.reshape(bop_5780.astype('float64'), relay.shape_of(bop_5760))) # shape=(14, 16, 9)
func_2994_call = mod.get_global_var('func_2994')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_5808 = relay.TupleGetItem(func_2994_call(), 0)
call_5809 = relay.TupleGetItem(func_2995_call(), 0)
output = relay.Tuple([call_5763,const_5764,call_5777,bop_5791,call_5808,])
output2 = relay.Tuple([call_5765,const_5764,call_5778,bop_5791,call_5809,])
func_5810 = relay.Function([var_5758,var_5759,], output)
mod['func_5810'] = func_5810
mod = relay.transform.InferType()(mod)
var_5811 = relay.var("var_5811", dtype = "uint32", shape = (14, 16, 9))#candidate|5811|(14, 16, 9)|var|uint32
var_5812 = relay.var("var_5812", dtype = "uint32", shape = (14, 16, 9))#candidate|5812|(14, 16, 9)|var|uint32
output = func_5810(var_5811,var_5812,)
func_5813 = relay.Function([var_5811,var_5812,], output)
mutated_mod['func_5813'] = func_5813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5374_call = mod.get_global_var('func_5374')
func_5375_call = mutated_mod.get_global_var('func_5375')
call_5831 = relay.TupleGetItem(func_5374_call(), 1)
call_5832 = relay.TupleGetItem(func_5375_call(), 1)
func_3509_call = mod.get_global_var('func_3509')
func_3513_call = mutated_mod.get_global_var('func_3513')
var_5843 = relay.var("var_5843", dtype = "uint32", shape = ())#candidate|5843|()|var|uint32
const_5844 = relay.const([-6,2,7,3,6,3,-1,-8,4,-2,-2,8,8,-4,-8,2,5,5,-10,5,-2,-7,-9,-5,10,1,-10,6,7,-1,-9,9,7,-8,-4,-6,1,1,-8,-10,4,10,2,-4,-4,-6,-9,10], dtype = "uint32")#candidate|5844|(48,)|const|uint32
call_5842 = relay.TupleGetItem(func_3509_call(relay.reshape(var_5843.astype('uint32'), []), relay.reshape(const_5844.astype('uint32'), [8, 6, 1]), ), 0)
call_5845 = relay.TupleGetItem(func_3513_call(relay.reshape(var_5843.astype('uint32'), []), relay.reshape(const_5844.astype('uint32'), [8, 6, 1]), ), 0)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_5846 = relay.TupleGetItem(func_606_call(), 0)
call_5847 = relay.TupleGetItem(func_608_call(), 0)
output = relay.Tuple([call_5831,call_5842,var_5843,const_5844,call_5846,])
output2 = relay.Tuple([call_5832,call_5845,var_5843,const_5844,call_5847,])
func_5850 = relay.Function([var_5843,], output)
mod['func_5850'] = func_5850
mod = relay.transform.InferType()(mod)
var_5851 = relay.var("var_5851", dtype = "uint32", shape = ())#candidate|5851|()|var|uint32
output = func_5850(var_5851)
func_5852 = relay.Function([var_5851], output)
mutated_mod['func_5852'] = func_5852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_5860 = relay.TupleGetItem(func_606_call(), 0)
call_5861 = relay.TupleGetItem(func_608_call(), 0)
output = call_5860
output2 = call_5861
func_5865 = relay.Function([], output)
mod['func_5865'] = func_5865
mod = relay.transform.InferType()(mod)
output = func_5865()
func_5866 = relay.Function([], output)
mutated_mod['func_5866'] = func_5866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4792_call = mod.get_global_var('func_4792')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_5903 = relay.TupleGetItem(func_4792_call(), 0)
call_5904 = relay.TupleGetItem(func_4793_call(), 0)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_5905 = relay.TupleGetItem(func_1830_call(), 0)
call_5906 = relay.TupleGetItem(func_1831_call(), 0)
output = relay.Tuple([call_5903,call_5905,])
output2 = relay.Tuple([call_5904,call_5906,])
func_5914 = relay.Function([], output)
mod['func_5914'] = func_5914
mod = relay.transform.InferType()(mod)
mutated_mod['func_5914'] = func_5914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5914_call = mutated_mod.get_global_var('func_5914')
call_5915 = func_5914_call()
output = call_5915
func_5916 = relay.Function([], output)
mutated_mod['func_5916'] = func_5916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3045_call = mod.get_global_var('func_3045')
func_3046_call = mutated_mod.get_global_var('func_3046')
call_5919 = relay.TupleGetItem(func_3045_call(), 0)
call_5920 = relay.TupleGetItem(func_3046_call(), 0)
output = relay.Tuple([call_5919,])
output2 = relay.Tuple([call_5920,])
func_5927 = relay.Function([], output)
mod['func_5927'] = func_5927
mod = relay.transform.InferType()(mod)
mutated_mod['func_5927'] = func_5927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5927_call = mutated_mod.get_global_var('func_5927')
call_5928 = func_5927_call()
output = call_5928
func_5929 = relay.Function([], output)
mutated_mod['func_5929'] = func_5929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1346_call = mod.get_global_var('func_1346')
func_1347_call = mutated_mod.get_global_var('func_1347')
call_5930 = relay.TupleGetItem(func_1346_call(), 2)
call_5931 = relay.TupleGetItem(func_1347_call(), 2)
func_5187_call = mod.get_global_var('func_5187')
func_5189_call = mutated_mod.get_global_var('func_5189')
call_5935 = func_5187_call()
call_5936 = func_5187_call()
output = relay.Tuple([call_5930,call_5935,])
output2 = relay.Tuple([call_5931,call_5936,])
func_5937 = relay.Function([], output)
mod['func_5937'] = func_5937
mod = relay.transform.InferType()(mod)
output = func_5937()
func_5938 = relay.Function([], output)
mutated_mod['func_5938'] = func_5938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4281_call = mod.get_global_var('func_4281')
func_4282_call = mutated_mod.get_global_var('func_4282')
call_5988 = relay.TupleGetItem(func_4281_call(), 2)
call_5989 = relay.TupleGetItem(func_4282_call(), 2)
output = relay.Tuple([call_5988,])
output2 = relay.Tuple([call_5989,])
func_5994 = relay.Function([], output)
mod['func_5994'] = func_5994
mod = relay.transform.InferType()(mod)
output = func_5994()
func_5995 = relay.Function([], output)
mutated_mod['func_5995'] = func_5995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2338_call = mod.get_global_var('func_2338')
func_2340_call = mutated_mod.get_global_var('func_2340')
call_6011 = func_2338_call()
call_6012 = func_2338_call()
func_5525_call = mod.get_global_var('func_5525')
func_5527_call = mutated_mod.get_global_var('func_5527')
call_6015 = relay.TupleGetItem(func_5525_call(), 0)
call_6016 = relay.TupleGetItem(func_5527_call(), 0)
func_293_call = mod.get_global_var('func_293')
func_298_call = mutated_mod.get_global_var('func_298')
var_6027 = relay.var("var_6027", dtype = "int64", shape = ())#candidate|6027|()|var|int64
var_6028 = relay.var("var_6028", dtype = "int64", shape = (128,))#candidate|6028|(128,)|var|int64
const_6029 = relay.const([-9.143153,7.556960,2.846505,3.468480,9.833676,-2.241834,-3.589968,-6.717881,-3.439933,-8.618423,4.062224,-8.501599,-1.325348,-3.120850,8.951292,-3.957563,-0.782151,3.285548,3.396660,7.122142,-2.949280,-3.617766,0.014953,-2.187640,-4.632280,2.705661,-9.779639,5.773003,-1.038185,-4.029629,6.824539,1.786189,-4.051194,4.476395,-4.830954,2.519679,-3.294102,7.582235,-3.408647,7.908471,-9.011079,-2.238987,-4.144726,-1.278725,9.204093,-9.576655,0.490769,0.762308,-1.352210,0.835125,7.401780,9.732459,2.769320,2.322494,4.279296,-7.452440,8.989511,-7.371313,-9.145668,-8.429452,3.162627,0.914017,1.934182,-2.505671,1.113542,-2.039294,-4.497813,7.614215,-2.535602,8.468874,2.957293,-8.778075,-0.872972,0.909809,9.887187,0.201485,-8.880453,6.825724,6.791556,-5.712314,-4.420264,3.039614,-3.322115,-1.072785,0.017859,-1.305468,4.397173,5.918725,6.024382,-5.621272,4.486657,7.611704,-1.651558,4.082658,9.970228,1.203394,-7.254628,-8.311030,9.117657,3.702388,9.839309,6.574198,-1.089892,-8.621289,8.031861,-4.501048,-7.344239,4.681360,1.469527,-7.452209,-0.009257,-3.523589,-6.188664,8.103235,6.989182,-7.960188,1.807360,2.613538,2.000881,6.643586,-1.619039,0.127875,-7.514551,-8.265836,7.715164,-1.774955,-4.103790,-3.750108,0.492236,-9.729990,-8.492908,0.299759,-3.536186,-1.896636,6.337253,0.109270,1.215035,-1.892389,7.546303,2.978182,-0.173381,-9.058957,-9.899483,9.554545,-4.572367,-0.574338,9.424151,-8.888728,-5.979789,0.728493,1.353689,-3.530344,8.762328,-3.934840,5.397764,7.239033,6.200470,-0.209240,-5.622448,9.537302,8.390468,3.594436,-2.325748,-6.763747,-6.578734,-6.949794,-0.562876,6.529247,4.677766,-6.709170,1.159653,-1.555993,2.624778,5.619824,4.361334,4.441562,-2.665105,2.843471,-4.634773,-2.412407,4.643345,-7.006314,3.880576,2.882040,5.431223,1.118341,0.062899,4.063432,-8.684029,-4.406395,-8.067332,-7.467251,-6.301458,9.977589,5.534299,-2.923482,-7.150800,1.690526,-5.223353,-7.944088,-7.382581,-2.016999,-5.016190,5.496121,-6.882586,-1.441965,5.388992,-0.313779,-8.177183,-4.639965,4.138283,-4.643291,-1.338322,4.928424,-5.216780,-3.406389,4.481437,-1.166543,9.718596,-9.754256,0.367186,-6.219419,2.265304,-2.561341,-6.436810,4.400270,1.855642,6.538579,4.494172,-3.879219,-9.296450,0.633909,-3.897263,2.737704,3.913113,7.637782,-4.844466,8.772311,-9.207494,4.321587,-8.230592,-5.692761,-5.558696,0.122127,-4.332895,0.100072,2.624391,-9.100053,-3.016978,6.537508,1.341634,-9.487292,-8.056805,0.378914,-0.469350,3.016651,-4.353621,-2.149691,3.610522,-3.218759,-4.995066,-6.921431,-6.313679,8.033206,1.342403,-4.181042,0.135784,-1.804700,-5.674081,6.980477,8.185959,-0.796779,-1.600407,-7.185921,-7.810516,-8.221331,6.241209,-3.535183,5.727073,-8.190864,-9.585166,-4.182190,-7.627928,4.924037,-6.982396,7.480949,9.079787,7.599428,-4.005743,6.043535,6.510435,9.519589,2.062260,-7.227311,2.090735,6.017965,-0.508723,-0.878830,-9.310891,8.979275,-6.144700,-1.244354,-2.721358,2.660467,-2.517068,-2.129519,-0.276839,-5.979754,3.618772,7.938560,1.556745,5.370174,-2.840267,-8.011148,9.560177,9.336910,-1.177796,-0.230044,-8.345234,-5.007373,-0.490311,-4.886195,-6.527879,-2.927101,1.514577,7.251804,-3.973564,-8.442761,-3.013928,-2.126960,5.322944,5.159066,9.821669,-5.070133,6.737097,-2.696591,1.156445,2.222537,9.449964,-2.730952,6.882731,-9.545273,-1.289334,-4.471687,5.775444,-7.775486,-7.043921,3.029777,1.926020,7.894500,-9.677631,2.255584,-4.773349,9.272145,-0.503088,4.954946,8.227147,-5.467212,-1.249310,-8.146658,4.660420,-7.865362,-8.386393,4.567525,-6.311619,4.500419,2.244717,-3.257310,0.646162,9.775839,1.033481,7.637512,-0.818889,-3.301609,-0.001949,7.184612,-4.030527,8.634835], dtype = "float32")#candidate|6029|(378,)|const|float32
call_6026 = relay.TupleGetItem(func_293_call(relay.reshape(var_6027.astype('int64'), []), relay.reshape(var_6028.astype('int64'), [8, 2, 8]), relay.reshape(const_6029.astype('float32'), [378,]), relay.reshape(const_6029.astype('float32'), [7, 9, 6]), ), 4)
call_6030 = relay.TupleGetItem(func_298_call(relay.reshape(var_6027.astype('int64'), []), relay.reshape(var_6028.astype('int64'), [8, 2, 8]), relay.reshape(const_6029.astype('float32'), [378,]), relay.reshape(const_6029.astype('float32'), [7, 9, 6]), ), 4)
output = relay.Tuple([call_6011,call_6015,call_6026,var_6027,var_6028,const_6029,])
output2 = relay.Tuple([call_6012,call_6016,call_6030,var_6027,var_6028,const_6029,])
func_6036 = relay.Function([var_6027,var_6028,], output)
mod['func_6036'] = func_6036
mod = relay.transform.InferType()(mod)
var_6037 = relay.var("var_6037", dtype = "int64", shape = ())#candidate|6037|()|var|int64
var_6038 = relay.var("var_6038", dtype = "int64", shape = (128,))#candidate|6038|(128,)|var|int64
output = func_6036(var_6037,var_6038,)
func_6039 = relay.Function([var_6037,var_6038,], output)
mutated_mod['func_6039'] = func_6039
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6044 = relay.const([[[6,3,5,-7,-4,1,2,-6,-9,5,4,3,6,6,-2],[3,-5,3,-8,-8,-3,-2,-6,-2,-1,-1,2,-10,7,-4],[7,8,4,5,-2,-4,-1,-3,-5,4,-1,10,10,-4,5],[10,5,-5,1,-3,-2,-1,-3,10,7,-3,-2,4,4,8],[3,-3,-6,-7,10,-2,-7,5,-5,-8,-2,3,-8,3,2],[-3,-9,-5,-7,-6,4,-1,-10,3,-1,8,-3,-7,-7,-5],[2,-5,-4,-10,5,-10,-1,-2,-7,-6,5,4,-6,-1,9]],[[-1,-3,4,7,2,9,2,3,10,-6,-10,2,-9,5,9],[-7,7,-7,9,6,-7,-5,4,1,-10,2,-10,-4,-5,10],[-2,-4,-8,1,-6,-1,1,-10,-4,1,-9,-3,-9,7,-5],[8,3,6,5,-9,4,4,5,-10,-6,-10,2,-4,-10,5],[-8,-1,-6,-4,-6,-4,4,6,1,-6,-5,-9,-2,9,4],[5,8,-6,-5,-7,-7,3,-6,-1,-3,3,-5,-6,-7,-9],[1,-4,-2,-3,-3,9,-1,1,9,6,9,9,-2,-1,10]],[[-10,3,-9,-6,-1,-7,1,3,7,2,-6,-3,-6,-2,5],[-6,4,-9,-4,9,6,-8,-4,-8,4,6,-2,-9,-5,-5],[4,5,3,-4,3,-4,9,-7,-4,-6,7,-2,-3,7,-1],[-10,8,-4,-1,9,4,-2,-7,8,4,-2,5,9,-5,8],[1,-1,-3,-1,5,-8,-1,-10,9,-10,1,3,-5,8,1],[6,-5,-2,-3,-3,-10,5,-1,-2,4,-3,-3,5,-9,10],[8,-1,-2,-1,3,-3,-5,6,5,6,7,8,-4,-2,5]],[[-2,-9,-6,-3,7,-3,10,-1,3,4,7,7,-3,-8,5],[-10,-6,7,1,-1,9,-1,1,5,7,-3,1,2,2,-3],[-3,1,2,-3,9,1,7,7,3,-2,-1,7,-7,-8,-10],[8,-3,-5,9,8,-2,-8,-1,7,-6,4,-7,1,-1,5],[-1,-7,3,9,-1,-10,8,-4,-2,2,-3,7,-9,-4,-9],[-2,-3,5,4,-8,3,-10,7,-9,-8,-8,9,-10,4,-9],[-6,-3,1,-5,-4,-9,-2,-9,4,9,-10,4,-10,6,-10]],[[-7,5,7,10,2,-4,2,-2,6,-8,10,10,5,-8,-6],[-7,7,2,9,-6,5,-2,8,7,-9,-9,-3,3,-10,3],[1,10,-2,-2,4,4,9,-8,9,3,10,-7,2,3,10],[10,3,-9,-2,-8,8,10,9,6,-1,7,10,6,-5,6],[2,7,5,4,7,-6,5,2,-3,-1,-7,8,4,1,-3],[-5,4,2,-9,9,-8,1,-2,-7,-3,-9,-9,-10,-1,4],[-10,8,-2,5,7,-7,10,10,5,5,8,-10,1,1,3]],[[-5,-4,-8,3,10,-7,7,-7,1,4,9,2,-10,1,6],[-9,-6,-5,-3,-8,-10,-8,-6,4,6,-3,-10,6,1,-5],[3,9,-1,6,5,-5,-10,-2,9,-4,-1,-9,4,-5,5],[2,-6,-9,-7,10,-8,-5,-9,5,-2,-2,7,-6,-9,8],[2,1,-2,6,-3,9,1,-10,-2,6,-5,7,-10,-7,-5],[-2,-6,7,-1,-7,-9,-8,2,-9,-4,-10,-5,-4,-9,3],[-5,-1,6,-9,10,3,-4,-10,-8,5,-5,-2,-10,-5,-5]],[[-3,3,-3,3,-8,-10,4,2,2,-4,4,10,10,-10,8],[-5,-8,-8,-7,-3,-6,6,6,-6,9,-5,-9,-7,-4,-8],[-4,7,1,-1,6,5,-6,4,10,2,9,-2,-2,-1,-8],[1,2,-2,-1,1,-8,9,-7,7,2,9,-7,-2,-2,5],[2,1,-6,-6,9,-4,6,-2,6,-2,-1,10,2,6,6],[3,1,-1,9,4,5,-5,-1,3,8,-8,8,8,-1,-3],[8,-3,2,-4,1,8,-5,-8,10,6,9,-9,-1,7,1]],[[-8,-6,8,7,8,1,6,9,-2,5,8,-1,1,4,-3],[7,-6,4,-2,9,9,-8,-5,6,7,-7,-7,4,2,5],[-4,9,-7,5,4,-1,-1,-7,-7,6,-6,9,-3,1,-10],[5,3,6,-8,1,-5,4,-1,-4,4,2,-5,3,-5,-5],[5,1,-3,7,-7,3,1,8,8,10,-4,-4,-5,-6,5],[5,9,-7,-2,4,-3,1,-4,-5,3,-6,10,-5,-9,3],[-2,6,-4,-4,7,6,-6,-3,-8,-5,-4,9,3,6,6]],[[-7,-10,8,6,-10,1,-3,5,-7,2,5,3,9,9,-9],[9,-1,-9,-2,-2,-5,10,-2,-4,7,1,4,-5,1,2],[-7,5,9,9,-6,4,4,1,-9,4,-3,-8,-10,-3,7],[10,4,1,7,5,-1,-7,4,-2,5,9,-1,-6,-1,2],[2,-3,-5,-2,-6,-10,-5,-3,-6,-2,-1,8,1,4,5],[-10,-8,-5,-7,9,-3,10,5,9,-6,-2,-3,8,-6,-5],[-8,10,-8,-1,2,-8,-7,7,10,3,6,-5,-6,2,-7]],[[5,-2,3,9,-4,-6,-8,-1,-4,10,8,-3,-6,8,-4],[-4,2,3,-3,3,-3,-10,-1,7,-1,-5,4,4,10,5],[8,-3,5,-10,-6,8,10,-4,6,-8,-8,-7,-2,2,2],[-4,-9,3,-2,-4,5,-10,9,-8,5,3,-1,-8,1,5],[-7,6,-5,-2,3,5,-8,-7,-1,4,-2,-9,-5,-6,-7],[2,9,2,6,-10,9,-10,-2,-6,1,9,4,6,7,8],[10,-9,-5,-2,-4,3,-8,10,8,-5,3,2,-5,9,-10]],[[-7,-6,-9,7,5,4,3,-10,5,1,7,-7,-3,7,6],[10,8,-2,-10,-10,8,-4,-9,-6,-10,-6,10,6,-8,9],[2,9,-9,1,-8,6,-7,9,-3,-2,-1,-2,4,6,4],[-7,-7,8,-7,-5,10,-3,10,-6,-6,-9,-9,-7,10,-6],[-1,1,-1,-3,-8,3,10,6,7,-4,-10,-7,-4,3,-10],[-8,-4,-10,-8,3,-9,-3,-2,10,2,-2,7,-3,-6,4],[-9,-8,1,-8,-10,6,-7,10,-9,1,-2,-4,-6,9,5]],[[-9,-8,-7,-6,-2,6,-6,7,2,-4,-7,-10,7,-10,-8],[-4,9,-6,2,1,-8,2,-8,10,6,5,-4,4,10,2],[9,7,-7,-4,4,-5,-10,8,7,-10,-4,4,-1,-1,-4],[-7,6,-1,-6,4,-10,-4,-5,10,10,4,-6,-4,-9,-6],[-6,8,-8,7,-5,5,9,8,4,7,-8,10,1,9,-8],[5,-9,-6,-1,10,-3,3,-6,9,9,-6,6,10,-9,-9],[5,1,-6,-10,9,5,5,-7,9,3,-1,-6,2,-4,7]]], dtype = "int64")#candidate|6044|(12, 7, 15)|const|int64
const_6045 = relay.const([[[3,-1,-5,-7,-8,-8,2,8,-7,7,-2,-10,-7,-5,4],[9,8,-4,-9,-5,7,-8,1,5,7,-1,-5,9,-9,3],[2,9,-1,4,3,-5,-3,1,8,-1,8,-6,-4,-6,-7],[6,-10,3,7,-1,5,3,10,-3,2,5,-7,-4,6,-3],[9,-6,4,2,5,4,-1,1,2,2,-7,3,-10,2,-7],[8,-6,-6,-2,-4,4,-10,-6,8,2,-2,-1,-2,2,-4],[10,-4,6,7,-10,8,8,1,-6,1,-1,6,6,2,1]],[[6,9,10,-1,5,5,-7,1,6,-5,5,8,9,-1,-3],[-6,-6,8,-10,10,-2,1,9,-5,9,-3,-7,8,-6,-6],[1,-7,-5,-2,4,2,-8,-5,-3,3,-2,6,7,7,3],[2,5,1,-4,5,-5,-4,-10,-2,-1,6,-1,-7,8,-4],[7,-5,5,2,-8,-9,-6,8,4,-8,4,10,-8,-6,1],[7,5,-2,-9,2,-3,-2,4,2,9,4,-6,9,-9,10],[4,-10,9,-1,-4,8,6,6,-10,-9,-2,2,-5,-2,5]],[[-6,1,-10,-6,9,-6,9,6,3,6,5,-4,6,8,-8],[1,-4,10,3,6,7,-10,5,4,2,-9,7,-5,-5,-10],[8,6,6,-5,-3,-2,5,9,-9,-8,-2,-9,-2,-2,5],[-1,7,-6,-5,-3,-4,-1,8,6,4,8,3,-6,10,-4],[-4,-10,6,4,-9,-2,-2,9,-4,9,1,3,-5,-8,7],[-3,-9,-9,-1,8,2,10,-4,5,-5,3,2,-7,3,3],[9,10,-9,5,-4,9,-5,-9,7,7,8,8,-4,-6,-10]],[[8,5,9,8,3,9,9,10,-2,-4,10,9,-2,3,-1],[-9,4,8,5,9,10,-9,-3,7,-7,-6,-4,3,7,6],[-10,-10,6,-10,-6,10,-7,4,-9,7,3,10,-6,1,-10],[-5,1,-7,-3,-9,-5,4,-9,4,-1,-3,4,-10,-8,-6],[-10,-1,6,8,-4,-10,-6,-3,-7,3,7,10,1,2,3],[-10,-10,-3,-10,8,8,2,-4,-6,-1,-9,-5,2,1,7],[-5,-8,-1,-9,-4,4,-7,-3,-3,-2,-10,-7,-9,2,4]],[[-5,-10,1,-4,2,-9,9,5,7,-2,4,-1,8,-1,-10],[-4,3,-8,5,9,9,6,-6,-1,-10,-3,7,-7,-3,-7],[-5,-8,5,7,7,7,-5,-3,5,5,8,-10,-1,-2,-7],[-7,-10,-3,10,-6,3,10,-8,9,10,-7,-2,-3,-7,-9],[-4,9,1,10,9,6,-9,1,3,1,6,2,-6,-2,2],[9,8,-1,-7,10,-8,9,-7,7,2,5,-5,-5,6,5],[-9,-5,2,7,8,9,-8,-3,9,-6,7,7,10,2,9]],[[3,4,6,3,-9,-3,-7,5,7,-10,-4,-4,-7,-5,10],[8,6,3,-10,-7,7,7,2,-4,7,2,8,-4,-2,-8],[5,-8,-10,2,7,-10,1,10,1,-4,7,4,2,4,9],[6,8,4,7,1,-7,-2,-10,4,6,4,2,1,-5,7],[5,-7,-1,2,-7,4,5,2,8,-9,-2,8,-8,-7,1],[7,1,-10,3,2,6,3,2,7,9,-6,6,4,-2,8],[-9,1,9,2,-5,3,10,3,9,-6,3,-1,6,4,8]],[[-1,-9,5,-4,-1,3,10,-7,-7,-2,-9,5,-7,-3,6],[5,8,-8,1,2,-10,-3,10,3,10,-10,-2,9,5,10],[-5,1,-8,-6,10,10,-3,-10,7,-10,-1,-8,-7,-4,-8],[6,-1,7,-5,-10,-1,6,-5,6,-2,-1,-9,9,5,-10],[8,-8,-4,-10,-6,-5,1,10,2,10,-4,-8,-9,1,-10],[8,-9,-7,-1,-2,-9,5,-10,8,3,-7,-10,-2,-2,4],[3,10,-10,3,-5,-8,3,4,10,-7,-1,-2,9,-1,-6]],[[-3,-9,-9,9,10,-8,-8,-4,8,6,9,-10,-10,6,2],[-8,-8,-5,6,2,7,6,3,-10,4,-6,5,5,-7,-9],[-10,3,2,9,-3,5,1,7,-1,-4,-5,7,8,-7,2],[5,1,-4,-7,10,-5,10,-6,1,4,-2,8,8,3,5],[9,1,-8,-2,9,-5,-9,-10,1,-2,-9,-3,4,-6,-7],[4,1,-4,10,3,10,-4,4,3,7,2,8,6,-7,10],[-1,9,-2,10,1,-3,-3,9,3,5,-7,-10,2,-10,-8]],[[4,7,-3,8,-10,9,9,2,-1,2,-9,-5,-6,4,-8],[6,-4,-7,3,10,-2,9,-3,1,-8,-2,-2,5,-5,-5],[3,-7,6,2,7,5,1,5,4,9,-9,-8,-9,-10,-4],[-9,8,-2,2,-6,-5,10,-2,1,-1,10,1,-2,1,-7],[6,-9,-4,1,-4,6,-5,-7,-3,4,9,3,-2,-2,-6],[-7,5,-7,7,-6,4,-4,8,5,-10,-3,-5,-10,-1,9],[1,10,-1,6,4,1,-4,6,-6,1,-1,6,-3,2,-9]],[[3,-6,6,1,-5,6,4,1,-9,-2,3,-9,1,7,7],[-6,-4,5,-10,-3,-1,3,6,5,10,-10,-3,6,-10,-7],[7,-9,-6,2,-1,4,-4,9,-10,-9,-4,-7,-5,-8,4],[-2,-9,-1,-5,4,9,-8,-5,-7,3,-7,-5,3,5,-5],[-9,9,9,-4,4,10,5,8,-7,5,1,9,6,7,3],[10,10,1,-9,4,2,7,-2,-7,10,-10,-4,8,-1,1],[9,-8,-1,8,2,3,6,1,-5,-10,8,7,-9,4,-1]],[[3,-6,-9,-8,9,1,-5,-2,-6,5,-3,5,7,-8,-5],[-5,9,9,-10,-6,-10,9,-5,-2,-9,8,1,5,-1,-8],[1,5,5,-1,5,-2,-6,10,5,4,-10,7,8,-9,4],[-5,3,7,4,-2,5,3,8,-3,-5,6,-9,-9,6,8],[-7,5,3,-7,7,-5,5,4,-1,-6,-5,-4,-5,3,-2],[1,6,-7,-7,-3,6,-9,-5,-4,-3,5,-3,2,1,-9],[-10,2,8,2,-6,10,-2,2,-5,6,-7,3,9,7,-5]],[[-4,-9,-9,-8,2,6,5,-2,-9,-3,4,5,1,-5,7],[5,2,-10,2,-2,3,6,-9,-4,5,3,-1,-7,4,9],[9,-5,-1,-4,4,-5,7,4,2,-2,7,-6,-6,1,4],[-1,7,6,2,10,9,10,9,-1,2,-7,1,-1,6,-6],[3,5,-5,7,4,-1,7,8,7,-6,-5,10,-8,-4,3],[7,7,-8,-5,-8,-4,-2,2,6,1,8,7,-3,-1,9],[7,1,-8,-6,4,9,-5,-9,-1,6,-9,8,-4,-8,8]]], dtype = "int64")#candidate|6045|(12, 7, 15)|const|int64
bop_6046 = relay.equal(const_6044.astype('bool'), relay.reshape(const_6045.astype('bool'), relay.shape_of(const_6044))) # shape=(12, 7, 15)
func_5284_call = mod.get_global_var('func_5284')
func_5286_call = mutated_mod.get_global_var('func_5286')
var_6068 = relay.var("var_6068", dtype = "uint32", shape = ())#candidate|6068|()|var|uint32
call_6067 = relay.TupleGetItem(func_5284_call(relay.reshape(var_6068.astype('uint32'), [])), 1)
call_6069 = relay.TupleGetItem(func_5286_call(relay.reshape(var_6068.astype('uint32'), [])), 1)
output = relay.Tuple([bop_6046,call_6067,var_6068,])
output2 = relay.Tuple([bop_6046,call_6069,var_6068,])
func_6074 = relay.Function([var_6068,], output)
mod['func_6074'] = func_6074
mod = relay.transform.InferType()(mod)
mutated_mod['func_6074'] = func_6074
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6075 = relay.var("var_6075", dtype = "uint32", shape = ())#candidate|6075|()|var|uint32
func_6074_call = mutated_mod.get_global_var('func_6074')
call_6076 = func_6074_call(var_6075)
output = call_6076
func_6077 = relay.Function([var_6075], output)
mutated_mod['func_6077'] = func_6077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_6104 = func_1632_call()
call_6105 = func_1632_call()
output = call_6104
output2 = call_6105
func_6106 = relay.Function([], output)
mod['func_6106'] = func_6106
mod = relay.transform.InferType()(mod)
output = func_6106()
func_6107 = relay.Function([], output)
mutated_mod['func_6107'] = func_6107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1512_call = mod.get_global_var('func_1512')
func_1514_call = mutated_mod.get_global_var('func_1514')
call_6121 = relay.TupleGetItem(func_1512_call(), 0)
call_6122 = relay.TupleGetItem(func_1514_call(), 0)
output = call_6121
output2 = call_6122
func_6129 = relay.Function([], output)
mod['func_6129'] = func_6129
mod = relay.transform.InferType()(mod)
mutated_mod['func_6129'] = func_6129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6129_call = mutated_mod.get_global_var('func_6129')
call_6130 = func_6129_call()
output = call_6130
func_6131 = relay.Function([], output)
mutated_mod['func_6131'] = func_6131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_6234 = relay.TupleGetItem(func_606_call(), 0)
call_6235 = relay.TupleGetItem(func_608_call(), 0)
func_6106_call = mod.get_global_var('func_6106')
func_6107_call = mutated_mod.get_global_var('func_6107')
call_6240 = func_6106_call()
call_6241 = func_6106_call()
output = relay.Tuple([call_6234,call_6240,])
output2 = relay.Tuple([call_6235,call_6241,])
func_6243 = relay.Function([], output)
mod['func_6243'] = func_6243
mod = relay.transform.InferType()(mod)
mutated_mod['func_6243'] = func_6243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6243_call = mutated_mod.get_global_var('func_6243')
call_6244 = func_6243_call()
output = call_6244
func_6245 = relay.Function([], output)
mutated_mod['func_6245'] = func_6245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_6297 = relay.TupleGetItem(func_1830_call(), 1)
call_6298 = relay.TupleGetItem(func_1831_call(), 1)
output = relay.Tuple([call_6297,])
output2 = relay.Tuple([call_6298,])
func_6300 = relay.Function([], output)
mod['func_6300'] = func_6300
mod = relay.transform.InferType()(mod)
output = func_6300()
func_6301 = relay.Function([], output)
mutated_mod['func_6301'] = func_6301
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6309 = relay.var("var_6309", dtype = "bool", shape = ())#candidate|6309|()|var|bool
const_6310 = relay.const([[[False,True,True,True,True,True,False,True,True,True,True,False,True,True],[False,False,False,False,False,True,True,True,True,True,True,True,True,True],[False,False,True,True,False,False,False,True,True,True,True,False,False,False],[True,False,True,True,False,True,True,True,True,True,False,False,False,True],[True,True,False,False,False,True,True,False,True,True,True,True,False,False],[True,True,False,False,True,False,False,True,True,True,False,False,False,False],[True,True,True,False,False,True,False,False,False,True,False,False,True,False],[True,True,False,False,False,True,True,True,True,True,True,False,False,True],[True,True,False,False,False,True,False,False,True,True,True,True,False,True],[True,True,True,False,True,False,True,True,True,False,True,False,True,False]],[[False,True,True,True,False,True,True,False,True,False,True,False,True,False],[True,True,True,True,True,True,True,False,True,False,True,False,False,False],[False,True,False,False,True,False,False,True,True,True,False,False,True,True],[False,False,True,False,False,False,True,True,True,False,True,False,True,False],[False,True,True,False,True,True,True,False,True,True,True,True,False,True],[True,False,False,False,False,True,False,False,False,True,True,True,True,False],[False,False,True,False,False,False,True,True,True,False,True,True,True,False],[False,True,False,True,True,False,True,False,False,True,False,False,False,False],[True,False,False,True,False,True,False,False,True,True,True,True,True,False],[False,False,True,False,True,True,True,True,True,True,True,True,False,True]],[[True,True,True,True,True,False,False,True,True,False,False,True,True,True],[False,False,False,False,False,True,False,False,False,True,True,True,False,False],[True,True,True,False,False,True,True,True,True,False,False,False,False,False],[True,False,False,True,False,False,True,True,True,True,True,True,True,False],[False,True,False,True,False,True,False,False,False,True,True,True,True,False],[False,False,False,True,False,False,True,False,False,False,True,True,False,False],[False,True,False,True,False,False,False,True,False,False,True,False,False,True],[False,True,True,False,True,True,True,True,False,False,False,False,True,True],[False,True,False,False,False,False,True,False,True,False,True,True,False,True],[True,False,False,True,False,True,True,True,False,True,True,False,True,True]]], dtype = "bool")#candidate|6310|(3, 10, 14)|const|bool
bop_6311 = relay.logical_and(var_6309.astype('bool'), const_6310.astype('bool')) # shape=(3, 10, 14)
bop_6320 = relay.right_shift(const_6310.astype('int64'), var_6309.astype('int64')) # shape=(3, 10, 14)
bop_6337 = relay.floor_mod(var_6309.astype('float64'), bop_6320.astype('float64')) # shape=(3, 10, 14)
bop_6352 = relay.equal(bop_6337.astype('bool'), relay.reshape(const_6310.astype('bool'), relay.shape_of(bop_6337))) # shape=(3, 10, 14)
uop_6358 = relay.asin(const_6310.astype('float32')) # shape=(3, 10, 14)
func_395_call = mod.get_global_var('func_395')
func_399_call = mutated_mod.get_global_var('func_399')
const_6375 = relay.const([2.537056,-8.300281,-4.092549,4.295685,-3.712826,0.061120,5.099452,-2.981823,7.630009,-3.367841,-1.891364,4.719244,-5.274892,-3.158412,-3.705768,6.627307,3.378746,8.356540,4.307426,3.616769,-9.872415,5.028557,2.979639,4.270632,-9.494979,-8.304901,9.326994,-9.603714,2.245807,3.736409,2.676271,5.125402,-4.412398,-7.671235,-2.771965,9.647720,-3.482285,-8.801468,-9.935312,-5.725295,2.209445,-6.112797,4.066072,-9.215383,9.458808,-7.047307,-9.554756,-2.489064,5.626585,2.984812,-4.015739,-3.585957,1.580036,-1.811027,-0.479302,-2.573943,3.455251,7.771032,-4.396071,9.237477,3.942958,-6.006370,-5.208028,3.163283,6.041734,3.513303,5.189243,-6.633633,-7.189856,1.999194,-3.656907,-2.375004,-4.996309,-6.275008,-0.421854,-0.012147,0.906492,1.389168,8.624488,5.240247,2.445283,-8.677465,-6.205784,3.214293,2.744512,-3.856953,8.941541,1.124354,-3.134938,-2.696355,-1.514853,-2.232294,4.858776,9.464655,-1.394756,9.410540,4.258173,5.498815,-9.127352,-5.400422,0.341692,4.138616,6.924777,-1.688957,-7.724707,-2.595492,4.003762,5.042586,6.826162,-2.173109,0.347124,8.673374,9.041284,6.266038,-1.452530,-0.642682,-7.018010,-6.764476,-6.448019,3.487793,4.307663,9.440313,-3.153407,4.790915,9.618636,-8.997101,5.567453,6.446749,-9.109865,-3.905304,-9.617977,-3.695501,1.401992,1.295023,3.641910,-6.035511,-1.810643,0.152571,-9.923137,-6.850847,-8.389738,8.339383,4.031188,5.555228,4.024133,-7.015931,-1.539721,-0.974558,6.573105,5.410505,-4.679665,8.606265,-5.969826,7.119200,6.564972,-6.372941,-2.417580,8.895835,9.993057,6.477995,-4.809201,-3.870208,-8.519865,-9.614229,-7.518917,-0.096988,-3.166904,-4.907187,6.416455,2.879820,6.644375,-8.020570,3.014328,3.067842,-0.321812,0.918875,-9.399666,3.813876,-5.123985,-6.673044,-8.707383,2.261067,-1.024440,3.967585,-4.267249,-8.945553,-8.861173,3.515972,-7.478925,-3.239968,-5.112257,-3.582815,-3.815753,9.364789,8.029298,5.909259,8.666963,-8.492891,-4.658709,1.934438,8.325873,0.562845,-0.575054,6.105919,2.775620,-0.710678,-7.887210,0.044486,-2.228809,6.183569,-1.257418,7.403449,-5.079641,-1.279032,8.505871,1.527913,8.065831,2.581511,8.663170,5.958010,-3.333801,-1.070632,-4.948336,0.795939,8.807805,-4.069475,-0.048217,4.894388,-1.921432,8.662562,3.923844,-7.161929,5.539537,-0.622031,-3.432278,-3.291239,4.833189,9.250140,-2.905271,4.772282,-3.666258,6.092966,9.557621,4.234502,-6.913874,-8.496096,7.998020,0.472950,-9.156183,3.955508], dtype = "float64")#candidate|6375|(250,)|const|float64
const_6376 = relay.const([-2,3,3,2,7,-10,1,1,10,-2,-9,-2,-6,1,-2,9,5,5,7,9,-7,8,-10,2,4,1,-5,-8,7,-8,-6,-2,-2,-8,-4,4,-8,3,-1,10,-9,9,-3,6,-8,10,3,2,8,-4,-1,-8,-1,8,4,-7,8,-6,5,-10,8,5,-3,5,-1,6,7,10,2,10,-6,10,1,3,-10,8,-7,7,2,-3,-3,4,2,-10,1,-4,-4,-9,10,2,-8,-6,-5,-5,7,1,-7,-1,-10,7,8,-8,-6,9,2,-6,2,-5,6,-6,-8,-4,4,5,-6,-7,2,9,4,-3,-9,-9,2,-10,6,5,4,8], dtype = "int64")#candidate|6376|(128,)|const|int64
call_6374 = relay.TupleGetItem(func_395_call(relay.reshape(const_6375.astype('float64'), [10, 5, 5]), relay.reshape(var_6309.astype('int64'), []), relay.reshape(const_6376.astype('int64'), [128,]), ), 3)
call_6377 = relay.TupleGetItem(func_399_call(relay.reshape(const_6375.astype('float64'), [10, 5, 5]), relay.reshape(var_6309.astype('int64'), []), relay.reshape(const_6376.astype('int64'), [128,]), ), 3)
var_6386 = relay.var("var_6386", dtype = "float32", shape = (3, 10, 14))#candidate|6386|(3, 10, 14)|var|float32
bop_6387 = relay.less(uop_6358.astype('bool'), relay.reshape(var_6386.astype('bool'), relay.shape_of(uop_6358))) # shape=(3, 10, 14)
output = relay.Tuple([bop_6311,bop_6352,call_6374,const_6375,const_6376,bop_6387,])
output2 = relay.Tuple([bop_6311,bop_6352,call_6377,const_6375,const_6376,bop_6387,])
func_6396 = relay.Function([var_6309,var_6386,], output)
mod['func_6396'] = func_6396
mod = relay.transform.InferType()(mod)
var_6397 = relay.var("var_6397", dtype = "bool", shape = ())#candidate|6397|()|var|bool
var_6398 = relay.var("var_6398", dtype = "float32", shape = (3, 10, 14))#candidate|6398|(3, 10, 14)|var|float32
output = func_6396(var_6397,var_6398,)
func_6399 = relay.Function([var_6397,var_6398,], output)
mutated_mod['func_6399'] = func_6399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1070_call = mod.get_global_var('func_1070')
func_1071_call = mutated_mod.get_global_var('func_1071')
call_6410 = func_1070_call()
call_6411 = func_1070_call()
output = relay.Tuple([call_6410,])
output2 = relay.Tuple([call_6411,])
func_6438 = relay.Function([], output)
mod['func_6438'] = func_6438
mod = relay.transform.InferType()(mod)
mutated_mod['func_6438'] = func_6438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6438_call = mutated_mod.get_global_var('func_6438')
call_6439 = func_6438_call()
output = call_6439
func_6440 = relay.Function([], output)
mutated_mod['func_6440'] = func_6440
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6461 = relay.const([[[10,-1,-3,5,5,1,4,-8,10,3,-6,3,1,-1,-2,6],[-3,4,-9,1,3,-8,1,-6,-7,-3,2,-3,9,9,-10,-3],[6,-1,8,-9,-6,-8,2,-10,-4,6,-6,-1,10,6,9,-3],[7,-7,5,-6,6,10,9,-9,-10,9,3,-2,-1,2,-6,-2],[10,7,-9,6,8,-3,5,-10,-8,-2,-8,-3,1,-9,-10,-9],[4,6,1,-9,8,-8,8,8,4,9,4,-2,-5,1,4,6],[8,-1,3,-9,-6,4,4,1,3,9,2,-4,2,4,7,-4],[-9,-5,-9,-3,-3,10,-2,5,-1,-3,-6,1,4,6,5,-6],[8,-9,8,-1,-1,-6,4,-8,-6,9,10,3,-7,-3,10,-7],[3,-5,-9,1,9,-5,-9,-9,6,10,-8,-9,-10,7,4,-10],[9,-9,4,-10,-9,8,-8,4,5,-9,7,-9,-2,8,-10,4],[-4,10,7,2,7,-4,9,10,-4,-8,-8,-9,-3,6,-5,-5]],[[-7,6,-8,-10,10,-1,-3,-4,9,9,1,8,5,9,8,9],[-10,-9,-3,3,-2,6,-3,-6,4,-2,5,9,7,10,-2,3],[3,-10,1,-4,8,-2,-10,-7,-6,-9,10,1,-8,5,1,3],[9,2,7,-5,-6,7,-5,-10,5,4,-1,-5,7,8,7,3],[5,8,-9,-8,-1,-1,-1,-9,-4,2,-7,4,-6,-3,-6,-10],[10,-4,2,6,-8,10,-9,4,4,-1,-2,5,9,-2,4,9],[-10,5,-4,-5,-7,10,6,1,9,-10,-9,8,5,-5,1,-3],[7,-3,10,-3,-5,-4,8,-2,9,7,-9,6,-2,2,-4,-4],[-4,4,-7,2,-10,4,4,-5,7,9,-5,-1,5,-10,-10,-2],[3,10,-2,3,-9,-10,-2,3,4,-7,-8,-8,2,4,4,6],[-3,-9,-7,7,-9,6,-1,-3,3,-6,10,4,3,2,7,9],[2,-4,-2,4,1,5,3,9,-1,8,10,-1,-1,4,-1,-7]],[[1,-4,4,6,-2,-7,2,2,4,3,2,-9,-7,1,6,-2],[9,1,6,1,10,-2,8,6,-1,-6,-2,-6,-9,-8,-4,1],[-8,9,2,1,-9,-6,8,9,-8,-4,1,9,6,-5,8,4],[-10,10,-4,-6,8,2,-2,7,5,2,1,5,1,-8,6,6],[6,10,9,-6,7,-4,10,-3,-3,2,6,-1,-7,-5,2,1],[-9,9,8,-6,-5,6,-10,-10,-3,6,10,-6,6,-2,-5,6],[5,-2,3,9,-6,3,3,-8,-6,6,2,4,5,4,-10,-4],[10,-7,-3,10,3,-5,9,-3,-10,2,2,7,2,7,-6,7],[6,6,2,9,1,2,-9,-4,5,-8,2,6,9,-5,6,-8],[8,2,-1,-5,-6,2,-3,4,-2,5,-10,-7,-4,-5,-6,3],[-8,-6,-9,-5,10,-10,-4,1,1,-2,-6,-1,3,1,10,5],[-2,-8,6,5,3,-8,-4,-4,4,-5,5,3,1,-7,-9,-8]],[[7,-3,1,10,-5,-10,-9,1,10,-6,-1,3,2,-2,6,3],[8,-6,-3,-3,-7,7,-7,9,-6,4,-1,-9,7,-5,3,-6],[-1,-10,-1,3,7,-3,-10,-4,7,-4,-5,5,-8,4,-6,2],[7,4,-4,7,8,-8,4,5,-9,2,-5,5,7,3,-2,-1],[-7,-6,-3,-4,4,-9,3,-10,6,4,10,5,9,-1,4,-9],[-8,-4,9,-1,-8,-1,-6,-3,4,-4,-7,2,-6,6,-4,1],[-1,4,-10,4,7,1,6,-8,1,5,-10,3,-9,-7,3,6],[10,-5,4,2,-7,-5,-9,5,4,8,-8,-1,10,-1,-4,9],[6,-8,-5,10,-5,7,9,-4,6,6,-2,3,4,5,1,-4],[7,-7,-4,6,-3,3,-7,-4,8,-8,-6,-2,-5,8,10,2],[6,2,6,7,-3,1,7,4,5,6,3,4,5,-3,-6,4],[4,-9,-6,-2,-9,8,8,1,-3,5,-7,3,10,8,-3,-7]],[[-10,9,-7,4,4,3,-3,-5,3,2,8,-1,1,6,2,1],[10,-8,1,-2,-4,-6,1,-3,1,4,1,2,5,-4,-1,-10],[4,-7,-10,9,6,-2,7,1,3,1,-3,5,-9,6,3,1],[4,4,9,-9,-9,1,-8,-5,-10,-6,9,10,2,10,-1,-5],[-10,-10,-2,-1,-10,10,7,-1,-4,-9,-10,-1,-6,-10,-3,-4],[5,10,-3,-2,-7,2,-8,8,-4,4,-7,-8,7,2,4,3],[-1,9,-7,-6,-3,-6,-3,-4,-1,-3,-5,-3,-9,-2,-10,4],[-9,-5,6,-9,-2,-2,1,-4,-4,3,7,2,9,-1,-9,2],[10,4,-7,-4,2,-3,-10,5,3,-3,-4,-6,-9,5,4,7],[3,9,-8,10,-9,-1,2,-4,6,5,10,-6,-10,8,8,-1],[7,-2,5,5,7,-2,3,-3,-3,2,2,4,-1,-8,-8,-10],[1,1,4,-9,-3,-7,8,9,8,7,-9,2,3,-9,-10,-7]],[[-10,6,-6,2,-7,6,-1,-9,6,1,-6,7,6,2,4,-7],[-10,8,-10,-5,-3,4,-8,5,6,-1,-10,4,6,-1,9,-7],[-5,-5,9,-1,3,-6,-6,-6,6,7,-6,3,-8,4,-6,-6],[-8,-5,-5,9,4,8,6,-4,-1,-10,3,1,-10,1,-8,5],[10,-4,8,2,9,-2,5,-9,9,7,5,-3,5,-10,-3,-2],[7,-7,-1,7,-10,-7,4,-3,-5,5,8,-6,-4,-9,-5,9],[7,9,6,8,-6,10,10,3,6,7,7,-9,4,-9,9,3],[3,-5,-9,-4,-7,6,-2,5,8,1,9,-8,8,-4,-5,-2],[-2,-9,10,-7,-10,6,-2,9,3,7,8,7,-3,2,9,-8],[10,1,3,-7,-10,6,-4,-2,-2,10,-4,-5,-7,7,-10,-6],[-4,-10,-6,-1,-2,6,1,4,7,-3,-3,8,-5,8,1,8],[3,-2,7,-3,2,4,7,5,3,5,-8,8,7,1,-9,1]],[[6,-1,1,-1,-5,-6,-4,8,-1,-5,-5,2,-8,8,-3,1],[6,-2,8,-10,8,-9,7,10,-2,6,-8,9,-5,-5,-8,8],[8,3,-1,1,8,-2,7,2,-8,7,9,2,-3,-2,3,6],[-8,-7,1,10,8,-2,-3,4,-5,7,-7,9,8,-2,1,-2],[7,10,7,-7,2,-10,6,-6,5,6,-6,1,-8,5,-10,-10],[6,7,10,8,3,-6,-2,-3,-8,10,-6,8,-3,-3,9,2],[-3,-9,-10,2,-5,-6,1,-5,-8,2,7,8,-4,4,4,9],[2,-10,-6,-8,3,9,3,4,2,-7,-8,8,-8,5,8,-1],[5,3,-4,-4,6,10,9,3,1,-10,-7,-3,1,-8,6,-7],[9,-2,-4,-7,-10,-2,-2,-10,-8,-2,-7,9,4,6,7,9],[-5,8,-7,-2,3,-4,2,7,-4,-5,3,10,-1,7,2,-3],[-9,8,5,1,-7,-2,10,-9,6,9,7,-1,8,6,6,-6]],[[-8,10,-6,1,7,2,-3,-6,-2,2,-4,8,1,-1,3,1],[-2,7,4,-1,3,10,2,-5,-3,-4,8,-1,5,-5,7,-10],[-6,9,6,1,-3,3,1,2,5,-10,-7,3,3,8,3,-1],[6,-1,9,-10,-4,-10,3,8,-7,4,-1,5,4,-4,-3,9],[4,-10,1,7,-4,-2,-8,-6,3,8,6,8,7,10,6,9],[-9,-2,10,-10,6,-3,4,-9,1,1,-1,9,10,9,-9,5],[-7,10,8,-4,-2,1,8,3,9,7,2,9,-7,7,7,6],[2,-3,-8,7,6,7,9,-3,3,-10,6,-8,-8,-9,-8,-8],[2,3,8,1,-7,8,-8,8,-1,-6,-8,9,1,8,4,-2],[-7,8,2,-9,-6,8,-8,-5,5,-5,8,-6,4,8,1,-6],[-2,4,-4,6,-2,5,-1,10,-4,8,10,10,-1,4,6,-8],[6,4,-5,-1,-7,8,1,-3,-4,6,6,-10,2,-8,-3,9]],[[-8,-1,-3,1,-3,7,6,6,4,6,7,8,-9,10,-3,-3],[-1,-6,-9,6,6,3,-5,4,10,-9,3,8,4,-5,-8,7],[-3,6,10,1,5,-9,-2,2,-2,-10,-10,8,8,-10,2,-6],[10,4,-3,-5,-8,3,-9,1,-5,8,-9,9,10,4,7,-4],[1,7,4,2,-6,1,9,-7,-2,2,-1,-9,-10,-2,4,-2],[-5,-6,-10,-10,-5,-4,-10,-1,-5,-4,-3,7,9,-10,7,-5],[-2,-1,3,-1,-2,-5,5,7,-10,-8,7,8,-5,6,-2,-4],[3,-7,7,-7,2,-3,9,-8,-2,-5,4,-4,4,2,-2,10],[-2,-4,-4,9,-2,-4,-4,-3,1,-5,1,-5,-9,3,-1,-7],[-10,3,-1,-2,9,-7,8,-9,-5,-5,4,-3,5,6,-9,-1],[5,6,10,-2,-4,10,-6,3,5,-2,-8,-4,1,2,-5,2],[1,-8,6,8,7,-1,8,6,6,4,3,8,10,-7,-5,4]]], dtype = "int64")#candidate|6461|(9, 12, 16)|const|int64
var_6462 = relay.var("var_6462", dtype = "int64", shape = (9, 12, 16))#candidate|6462|(9, 12, 16)|var|int64
bop_6463 = relay.less_equal(const_6461.astype('bool'), relay.reshape(var_6462.astype('bool'), relay.shape_of(const_6461))) # shape=(9, 12, 16)
func_4010_call = mod.get_global_var('func_4010')
func_4012_call = mutated_mod.get_global_var('func_4012')
call_6484 = func_4010_call()
call_6485 = func_4010_call()
output = relay.Tuple([bop_6463,call_6484,])
output2 = relay.Tuple([bop_6463,call_6485,])
func_6498 = relay.Function([var_6462,], output)
mod['func_6498'] = func_6498
mod = relay.transform.InferType()(mod)
var_6499 = relay.var("var_6499", dtype = "int64", shape = (9, 12, 16))#candidate|6499|(9, 12, 16)|var|int64
output = func_6498(var_6499)
func_6500 = relay.Function([var_6499], output)
mutated_mod['func_6500'] = func_6500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5687_call = mod.get_global_var('func_5687')
func_5689_call = mutated_mod.get_global_var('func_5689')
call_6523 = relay.TupleGetItem(func_5687_call(), 2)
call_6524 = relay.TupleGetItem(func_5689_call(), 2)
const_6544 = relay.const([[[True,True,True,False,False,False],[False,True,True,False,False,True],[True,True,False,False,False,True],[True,True,True,False,True,True],[True,False,False,False,False,True],[False,True,True,False,True,True],[False,False,False,True,False,True],[False,True,False,False,True,False],[True,False,True,False,True,True]],[[True,False,True,False,False,True],[True,True,False,False,True,False],[True,True,False,False,False,False],[True,False,True,True,False,False],[True,True,False,True,False,True],[False,True,False,True,True,False],[True,True,True,True,True,False],[True,True,True,True,True,True],[True,False,True,False,True,True]],[[False,False,True,True,True,True],[False,True,False,False,True,False],[True,False,True,False,True,False],[True,True,True,False,False,False],[False,False,False,True,False,True],[True,True,False,False,False,True],[True,False,True,True,True,False],[True,False,False,False,False,True],[True,True,False,False,False,True]],[[True,False,True,True,True,True],[True,False,False,True,False,False],[False,True,True,True,True,False],[True,False,False,True,True,False],[True,False,False,True,False,False],[False,True,False,True,True,True],[True,False,False,True,True,False],[False,True,False,True,True,True],[True,False,True,True,False,False]],[[True,True,False,True,False,True],[True,True,False,True,False,True],[True,True,True,True,True,False],[True,True,False,True,False,True],[False,True,True,False,False,True],[False,True,False,True,True,True],[False,False,False,False,False,False],[False,True,False,True,False,True],[False,True,False,False,True,False]],[[True,True,True,False,True,True],[False,False,False,False,True,True],[True,True,False,True,True,False],[False,True,True,False,True,True],[True,True,False,True,True,True],[True,False,True,False,False,False],[True,False,False,True,True,True],[True,False,False,True,False,False],[True,False,True,False,False,False]],[[True,True,True,True,False,False],[True,True,False,False,True,True],[False,False,True,True,True,False],[False,False,True,True,True,True],[True,False,True,False,False,True],[True,True,False,False,True,False],[True,False,True,True,False,False],[False,False,False,False,True,True],[False,False,False,True,True,True]]], dtype = "bool")#candidate|6544|(7, 9, 6)|const|bool
bop_6545 = relay.equal(call_6523.astype('bool'), relay.reshape(const_6544.astype('bool'), relay.shape_of(call_6523))) # shape=(7, 9, 6)
bop_6548 = relay.equal(call_6524.astype('bool'), relay.reshape(const_6544.astype('bool'), relay.shape_of(call_6524))) # shape=(7, 9, 6)
func_4792_call = mod.get_global_var('func_4792')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_6550 = relay.TupleGetItem(func_4792_call(), 0)
call_6551 = relay.TupleGetItem(func_4793_call(), 0)
bop_6578 = relay.floor_mod(call_6523.astype('float64'), relay.reshape(const_6544.astype('float64'), relay.shape_of(call_6523))) # shape=(7, 9, 6)
bop_6581 = relay.floor_mod(call_6524.astype('float64'), relay.reshape(const_6544.astype('float64'), relay.shape_of(call_6524))) # shape=(7, 9, 6)
output = relay.Tuple([bop_6545,call_6550,bop_6578,])
output2 = relay.Tuple([bop_6548,call_6551,bop_6581,])
func_6605 = relay.Function([], output)
mod['func_6605'] = func_6605
mod = relay.transform.InferType()(mod)
output = func_6605()
func_6606 = relay.Function([], output)
mutated_mod['func_6606'] = func_6606
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6634 = relay.var("var_6634", dtype = "int64", shape = (16, 4, 3))#candidate|6634|(16, 4, 3)|var|int64
var_6635 = relay.var("var_6635", dtype = "int64", shape = (16, 4, 3))#candidate|6635|(16, 4, 3)|var|int64
bop_6636 = relay.bitwise_xor(var_6634.astype('int64'), relay.reshape(var_6635.astype('int64'), relay.shape_of(var_6634))) # shape=(16, 4, 3)
func_2751_call = mod.get_global_var('func_2751')
func_2754_call = mutated_mod.get_global_var('func_2754')
const_6649 = relay.const([-5.601257,9.287114,5.376427,-9.961661,-9.727481,-9.036209,-0.308703,-8.478655,2.974375,4.860911,-8.730022,7.023266,-1.407976,4.730880,-4.992625,-6.702328,-1.708419,-1.449488,-6.250376,-4.312233,-3.519757,2.912565,4.402593,-3.129080,9.199820,-4.739922,5.994421,-2.127536,-3.608513,0.287091,4.771325,8.179482,9.380504,1.666631,7.507405,-0.104080,-7.811276,-1.539905,-6.348212,6.324865,-9.582196,5.708249,1.690314,-1.451115,-4.194355,-9.803055,9.030462,7.192300,-5.693536,-3.795362,-1.231294,4.888920,-0.474156,-5.210107,5.894622,-3.779440,-1.684771,0.938271,-3.800939,0.314915,7.921590,-4.937214,-4.372748,-4.638737,-7.554647,-0.493330,9.809303,9.032701,5.400522,-7.224413,7.198910,-1.965794,3.159719,2.368819,9.913011,-0.353098,4.829660,4.883251,-3.832121,-0.696042], dtype = "float32")#candidate|6649|(80,)|const|float32
call_6648 = relay.TupleGetItem(func_2751_call(relay.reshape(const_6649.astype('float32'), [2, 5, 8])), 2)
call_6650 = relay.TupleGetItem(func_2754_call(relay.reshape(const_6649.astype('float32'), [2, 5, 8])), 2)
func_5525_call = mod.get_global_var('func_5525')
func_5527_call = mutated_mod.get_global_var('func_5527')
call_6661 = relay.TupleGetItem(func_5525_call(), 0)
call_6662 = relay.TupleGetItem(func_5527_call(), 0)
func_4993_call = mod.get_global_var('func_4993')
func_4994_call = mutated_mod.get_global_var('func_4994')
call_6668 = relay.TupleGetItem(func_4993_call(), 0)
call_6669 = relay.TupleGetItem(func_4994_call(), 0)
output = relay.Tuple([bop_6636,call_6648,const_6649,call_6661,call_6668,])
output2 = relay.Tuple([bop_6636,call_6650,const_6649,call_6662,call_6669,])
func_6675 = relay.Function([var_6634,var_6635,], output)
mod['func_6675'] = func_6675
mod = relay.transform.InferType()(mod)
var_6676 = relay.var("var_6676", dtype = "int64", shape = (16, 4, 3))#candidate|6676|(16, 4, 3)|var|int64
var_6677 = relay.var("var_6677", dtype = "int64", shape = (16, 4, 3))#candidate|6677|(16, 4, 3)|var|int64
output = func_6675(var_6676,var_6677,)
func_6678 = relay.Function([var_6676,var_6677,], output)
mutated_mod['func_6678'] = func_6678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_821_call = mod.get_global_var('func_821')
func_823_call = mutated_mod.get_global_var('func_823')
call_6683 = relay.TupleGetItem(func_821_call(), 1)
call_6684 = relay.TupleGetItem(func_823_call(), 1)
output = relay.Tuple([call_6683,])
output2 = relay.Tuple([call_6684,])
func_6685 = relay.Function([], output)
mod['func_6685'] = func_6685
mod = relay.transform.InferType()(mod)
mutated_mod['func_6685'] = func_6685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6685_call = mutated_mod.get_global_var('func_6685')
call_6686 = func_6685_call()
output = call_6686
func_6687 = relay.Function([], output)
mutated_mod['func_6687'] = func_6687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_6748 = relay.TupleGetItem(func_1830_call(), 2)
call_6749 = relay.TupleGetItem(func_1831_call(), 2)
func_4829_call = mod.get_global_var('func_4829')
func_4830_call = mutated_mod.get_global_var('func_4830')
call_6752 = relay.TupleGetItem(func_4829_call(), 2)
call_6753 = relay.TupleGetItem(func_4830_call(), 2)
output = relay.Tuple([call_6748,call_6752,])
output2 = relay.Tuple([call_6749,call_6753,])
func_6763 = relay.Function([], output)
mod['func_6763'] = func_6763
mod = relay.transform.InferType()(mod)
output = func_6763()
func_6764 = relay.Function([], output)
mutated_mod['func_6764'] = func_6764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5994_call = mod.get_global_var('func_5994')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_6775 = relay.TupleGetItem(func_5994_call(), 0)
call_6776 = relay.TupleGetItem(func_5995_call(), 0)
output = relay.Tuple([call_6775,])
output2 = relay.Tuple([call_6776,])
func_6779 = relay.Function([], output)
mod['func_6779'] = func_6779
mod = relay.transform.InferType()(mod)
output = func_6779()
func_6780 = relay.Function([], output)
mutated_mod['func_6780'] = func_6780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5432_call = mod.get_global_var('func_5432')
func_5434_call = mutated_mod.get_global_var('func_5434')
call_6795 = relay.TupleGetItem(func_5432_call(), 1)
call_6796 = relay.TupleGetItem(func_5434_call(), 1)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_6804 = func_587_call()
call_6805 = func_587_call()
output = relay.Tuple([call_6795,call_6804,])
output2 = relay.Tuple([call_6796,call_6805,])
func_6806 = relay.Function([], output)
mod['func_6806'] = func_6806
mod = relay.transform.InferType()(mod)
mutated_mod['func_6806'] = func_6806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6806_call = mutated_mod.get_global_var('func_6806')
call_6807 = func_6806_call()
output = call_6807
func_6808 = relay.Function([], output)
mutated_mod['func_6808'] = func_6808
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6818 = relay.const([[[True,False,True,True,False,False,False,True,False,True],[True,True,False,True,False,True,False,False,True,True],[True,False,True,True,True,False,True,False,True,False],[False,False,False,True,False,False,False,False,True,False],[True,False,True,True,False,False,False,False,False,False],[True,True,False,False,False,True,True,True,True,False],[True,True,False,True,True,False,True,True,True,False],[True,False,True,True,False,True,True,False,True,True],[False,False,False,False,False,False,False,True,False,True],[True,True,True,False,True,False,False,False,True,True],[True,False,False,False,True,False,True,False,False,False]]], dtype = "bool")#candidate|6818|(1, 11, 10)|const|bool
var_6819 = relay.var("var_6819", dtype = "bool", shape = (2, 11, 10))#candidate|6819|(2, 11, 10)|var|bool
bop_6820 = relay.logical_or(const_6818.astype('bool'), var_6819.astype('bool')) # shape=(2, 11, 10)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_6824 = relay.TupleGetItem(func_573_call(), 0)
call_6825 = relay.TupleGetItem(func_574_call(), 0)
func_3091_call = mod.get_global_var('func_3091')
func_3093_call = mutated_mod.get_global_var('func_3093')
call_6837 = relay.TupleGetItem(func_3091_call(), 0)
call_6838 = relay.TupleGetItem(func_3093_call(), 0)
uop_6841 = relay.erf(var_6819.astype('float32')) # shape=(2, 11, 10)
func_2130_call = mod.get_global_var('func_2130')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_6844 = func_2130_call()
call_6845 = func_2130_call()
func_1659_call = mod.get_global_var('func_1659')
func_1660_call = mutated_mod.get_global_var('func_1660')
call_6850 = func_1659_call()
call_6851 = func_1659_call()
output = relay.Tuple([bop_6820,call_6824,call_6837,uop_6841,call_6844,call_6850,])
output2 = relay.Tuple([bop_6820,call_6825,call_6838,uop_6841,call_6845,call_6851,])
func_6865 = relay.Function([var_6819,], output)
mod['func_6865'] = func_6865
mod = relay.transform.InferType()(mod)
var_6866 = relay.var("var_6866", dtype = "bool", shape = (2, 11, 10))#candidate|6866|(2, 11, 10)|var|bool
output = func_6865(var_6866)
func_6867 = relay.Function([var_6866], output)
mutated_mod['func_6867'] = func_6867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4792_call = mod.get_global_var('func_4792')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_6904 = relay.TupleGetItem(func_4792_call(), 0)
call_6905 = relay.TupleGetItem(func_4793_call(), 0)
func_5187_call = mod.get_global_var('func_5187')
func_5189_call = mutated_mod.get_global_var('func_5189')
call_6931 = func_5187_call()
call_6932 = func_5187_call()
output = relay.Tuple([call_6904,call_6931,])
output2 = relay.Tuple([call_6905,call_6932,])
func_6934 = relay.Function([], output)
mod['func_6934'] = func_6934
mod = relay.transform.InferType()(mod)
output = func_6934()
func_6935 = relay.Function([], output)
mutated_mod['func_6935'] = func_6935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4948_call = mod.get_global_var('func_4948')
func_4950_call = mutated_mod.get_global_var('func_4950')
call_6936 = relay.TupleGetItem(func_4948_call(), 2)
call_6937 = relay.TupleGetItem(func_4950_call(), 2)
func_2467_call = mod.get_global_var('func_2467')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_6938 = relay.TupleGetItem(func_2467_call(), 2)
call_6939 = relay.TupleGetItem(func_2469_call(), 2)
output = relay.Tuple([call_6936,call_6938,])
output2 = relay.Tuple([call_6937,call_6939,])
func_6950 = relay.Function([], output)
mod['func_6950'] = func_6950
mod = relay.transform.InferType()(mod)
output = func_6950()
func_6951 = relay.Function([], output)
mutated_mod['func_6951'] = func_6951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6106_call = mod.get_global_var('func_6106')
func_6107_call = mutated_mod.get_global_var('func_6107')
call_7038 = func_6106_call()
call_7039 = func_6106_call()
output = relay.Tuple([call_7038,])
output2 = relay.Tuple([call_7039,])
func_7053 = relay.Function([], output)
mod['func_7053'] = func_7053
mod = relay.transform.InferType()(mod)
mutated_mod['func_7053'] = func_7053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7053_call = mutated_mod.get_global_var('func_7053')
call_7054 = func_7053_call()
output = call_7054
func_7055 = relay.Function([], output)
mutated_mod['func_7055'] = func_7055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_587_call = mod.get_global_var('func_587')
func_588_call = mutated_mod.get_global_var('func_588')
call_7102 = func_587_call()
call_7103 = func_587_call()
output = relay.Tuple([call_7102,])
output2 = relay.Tuple([call_7103,])
func_7113 = relay.Function([], output)
mod['func_7113'] = func_7113
mod = relay.transform.InferType()(mod)
mutated_mod['func_7113'] = func_7113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7113_call = mutated_mod.get_global_var('func_7113')
call_7114 = func_7113_call()
output = call_7114
func_7115 = relay.Function([], output)
mutated_mod['func_7115'] = func_7115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6605_call = mod.get_global_var('func_6605')
func_6606_call = mutated_mod.get_global_var('func_6606')
call_7134 = relay.TupleGetItem(func_6605_call(), 2)
call_7135 = relay.TupleGetItem(func_6606_call(), 2)
output = relay.Tuple([call_7134,])
output2 = relay.Tuple([call_7135,])
func_7138 = relay.Function([], output)
mod['func_7138'] = func_7138
mod = relay.transform.InferType()(mod)
output = func_7138()
func_7139 = relay.Function([], output)
mutated_mod['func_7139'] = func_7139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7160 = relay.var("var_7160", dtype = "int8", shape = ())#candidate|7160|()|var|int8
var_7161 = relay.var("var_7161", dtype = "int8", shape = (12, 9, 13))#candidate|7161|(12, 9, 13)|var|int8
bop_7162 = relay.bitwise_xor(var_7160.astype('int8'), var_7161.astype('int8')) # shape=(12, 9, 13)
output = bop_7162
output2 = bop_7162
func_7166 = relay.Function([var_7160,var_7161,], output)
mod['func_7166'] = func_7166
mod = relay.transform.InferType()(mod)
var_7167 = relay.var("var_7167", dtype = "int8", shape = ())#candidate|7167|()|var|int8
var_7168 = relay.var("var_7168", dtype = "int8", shape = (12, 9, 13))#candidate|7168|(12, 9, 13)|var|int8
output = func_7166(var_7167,var_7168,)
func_7169 = relay.Function([var_7167,var_7168,], output)
mutated_mod['func_7169'] = func_7169
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7211 = relay.var("var_7211", dtype = "bool", shape = (8, 5, 13))#candidate|7211|(8, 5, 13)|var|bool
var_7212 = relay.var("var_7212", dtype = "bool", shape = (8, 5, 13))#candidate|7212|(8, 5, 13)|var|bool
bop_7213 = relay.logical_or(var_7211.astype('bool'), relay.reshape(var_7212.astype('bool'), relay.shape_of(var_7211))) # shape=(8, 5, 13)
uop_7219 = relay.acos(var_7212.astype('float32')) # shape=(8, 5, 13)
output = relay.Tuple([bop_7213,uop_7219,])
output2 = relay.Tuple([bop_7213,uop_7219,])
func_7224 = relay.Function([var_7211,var_7212,], output)
mod['func_7224'] = func_7224
mod = relay.transform.InferType()(mod)
var_7225 = relay.var("var_7225", dtype = "bool", shape = (8, 5, 13))#candidate|7225|(8, 5, 13)|var|bool
var_7226 = relay.var("var_7226", dtype = "bool", shape = (8, 5, 13))#candidate|7226|(8, 5, 13)|var|bool
output = func_7224(var_7225,var_7226,)
func_7227 = relay.Function([var_7225,var_7226,], output)
mutated_mod['func_7227'] = func_7227
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7233 = relay.var("var_7233", dtype = "float32", shape = (7, 9, 6))#candidate|7233|(7, 9, 6)|var|float32
uop_7234 = relay.sqrt(var_7233.astype('float32')) # shape=(7, 9, 6)
const_7238 = relay.const([[[1.260870,0.588423,1.092965,4.696242,5.355810,1.912299],[-5.312566,-6.680521,-0.394247,3.087320,-4.272362,-5.814552],[-7.042905,3.879105,9.604947,-4.937572,4.656700,5.423125],[3.969527,8.783544,8.967586,-6.728893,-3.233620,-8.106850],[6.161419,-2.449170,2.196650,-9.303930,8.822513,-1.026696],[-7.642984,-7.274835,2.121151,2.809798,-7.040052,5.632041],[0.308023,-7.668267,3.834010,-6.426871,-9.532157,-5.288671],[9.112036,-6.789613,3.538224,3.493048,9.334599,5.371538],[-9.399133,5.514243,-0.808158,-7.917649,8.362562,8.701022]],[[-0.055329,1.318855,-2.249518,-0.113657,7.035479,6.592428],[6.913210,-8.286074,-9.633147,7.195969,-1.080801,0.846445],[-4.031808,-5.310144,-7.599327,-3.257705,4.312345,-2.381385],[1.252704,-5.560729,6.887828,0.092936,-6.668312,2.474110],[-2.938219,6.384535,-3.374428,2.460821,1.908492,-7.298152],[4.943283,-6.691246,-5.812031,-6.118609,2.396668,-5.463905],[-0.478814,9.575938,-6.738653,1.862741,-3.751886,0.866215],[-6.514240,5.909927,7.478204,0.472993,-4.850314,3.704295],[-3.062001,-1.762520,-7.443899,-0.416727,5.160232,-7.390094]],[[1.016503,-5.625674,-2.731359,-5.821745,-7.656765,-9.854415],[1.421153,-4.097930,2.974205,-6.897901,7.195880,4.716350],[-7.075671,0.417931,-5.530389,0.002857,6.172649,0.439387],[9.900095,-6.231115,6.048699,3.286912,2.617192,-8.890403],[-1.967361,-3.558010,4.131921,5.812104,-2.113875,8.145751],[-5.180534,-5.277971,-0.195219,-5.653876,4.638440,8.439773],[6.844256,3.293997,-1.904112,-2.375196,-1.441831,3.848140],[-3.120276,3.875390,2.561975,8.006593,2.304309,0.783020],[1.028193,-4.215583,8.479290,2.823848,-0.870897,9.725970]],[[-1.517081,5.891467,-1.898110,9.152095,-6.741355,1.545744],[0.887243,4.966347,-2.062229,4.062028,-3.570431,-1.821931],[0.259938,1.953670,-4.182646,0.059262,-5.499052,-1.757064],[5.046679,3.004275,-2.364843,4.333923,-1.855170,0.170279],[1.733711,-3.511756,-2.123993,5.389144,0.020037,2.544136],[2.904807,-4.884796,-1.587238,8.832953,-2.830970,3.076623],[2.979815,2.601970,5.401473,8.895479,9.135819,4.708118],[-1.622080,0.411088,1.372592,-3.298135,0.324402,-3.710841],[3.963439,2.608052,-4.606612,-8.986207,0.773251,9.670809]],[[-9.132283,-6.127147,6.571463,2.622204,-5.598661,9.027797],[-9.040258,9.608432,-6.768317,4.344250,2.641267,-8.543451],[9.780727,2.749165,-9.570383,1.862921,1.607257,-0.490721],[3.387465,1.488559,-6.635909,7.763551,-2.824941,6.862818],[-5.607074,-8.792444,5.710605,-1.071115,3.034081,-2.579798],[-5.343342,8.608723,8.870514,-9.241364,2.396474,-5.666861],[-6.630756,-7.782409,-6.064042,-8.470437,-1.235358,-0.987102],[1.999512,-3.134730,3.895028,-5.880542,2.851126,6.737971],[6.192585,2.438522,6.891078,-7.650708,-7.100056,-0.421680]],[[-5.974786,0.565208,6.640777,5.065620,-2.816756,-4.576069],[-7.221528,-3.948796,-3.075318,-1.048476,7.738307,-2.639510],[6.637728,2.066602,-3.089544,5.023013,-5.822775,8.596481],[-9.670045,-8.697897,1.526982,-1.602997,0.958212,8.503600],[7.441673,2.151189,4.356550,3.466192,-2.306759,-0.882459],[0.436313,-2.229773,5.605788,4.556661,-8.508684,-1.240109],[-9.121871,0.369715,9.394110,2.076637,-4.458250,-1.254399],[2.223954,-9.015557,-1.023813,-7.739265,-0.217722,5.863197],[-0.677475,-6.617992,-9.914291,-0.165122,4.676969,-8.937659]],[[-1.936851,7.373750,-6.447042,4.872305,-3.478424,0.108707],[-2.043030,-2.152169,-0.638925,-3.441169,-1.961195,8.201766],[-9.301438,-0.894269,2.803072,-8.124186,-8.468422,-8.317006],[1.801541,-8.579362,-3.594725,-0.927962,1.362838,3.232019],[-7.562973,1.672417,-3.784073,5.405958,-9.731207,2.321521],[-7.672516,-2.482620,3.638924,0.352852,-5.791073,-3.849928],[-9.694749,8.933283,7.346266,9.032668,4.952504,9.981100],[-9.981008,-0.695261,-6.150419,-0.642726,7.424169,4.167382],[-1.157589,-9.958475,2.102975,7.420165,7.686303,4.068116]]], dtype = "float32")#candidate|7238|(7, 9, 6)|const|float32
bop_7239 = relay.left_shift(uop_7234.astype('int32'), relay.reshape(const_7238.astype('int32'), relay.shape_of(uop_7234))) # shape=(7, 9, 6)
func_6243_call = mod.get_global_var('func_6243')
func_6245_call = mutated_mod.get_global_var('func_6245')
call_7246 = relay.TupleGetItem(func_6243_call(), 1)
call_7247 = relay.TupleGetItem(func_6245_call(), 1)
output = relay.Tuple([bop_7239,call_7246,])
output2 = relay.Tuple([bop_7239,call_7247,])
func_7254 = relay.Function([var_7233,], output)
mod['func_7254'] = func_7254
mod = relay.transform.InferType()(mod)
mutated_mod['func_7254'] = func_7254
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7255 = relay.var("var_7255", dtype = "float32", shape = (7, 9, 6))#candidate|7255|(7, 9, 6)|var|float32
func_7254_call = mutated_mod.get_global_var('func_7254')
call_7256 = func_7254_call(var_7255)
output = call_7256
func_7257 = relay.Function([var_7255], output)
mutated_mod['func_7257'] = func_7257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3990_call = mod.get_global_var('func_3990')
func_3992_call = mutated_mod.get_global_var('func_3992')
call_7337 = relay.TupleGetItem(func_3990_call(), 0)
call_7338 = relay.TupleGetItem(func_3992_call(), 0)
const_7340 = relay.const([[[-6.957572,4.516451,1.328658,4.631604,-7.786339,9.415312,8.108445,-9.640200],[5.434041,-7.614917,-5.118898,1.691995,4.736618,-3.970268,-3.077155,5.126140],[0.272677,-5.394931,2.196231,2.352187,5.799310,-0.456685,9.649673,4.599680],[4.191699,1.955116,5.733276,-4.839223,-8.520744,-7.512695,-1.267937,3.806483],[-0.294476,-6.883256,5.478544,7.604077,2.282717,7.704330,-6.584928,8.985023]],[[-5.900081,-4.822581,6.003401,2.931520,8.206586,-3.321828,9.427586,5.378186],[8.104809,-4.837484,2.559999,6.624006,5.841377,8.400855,9.188008,1.153072],[0.103415,6.854745,-3.113671,-5.947925,-0.861588,-9.940483,-9.422468,-7.228905],[3.113422,-5.351898,-3.849491,0.889357,-6.072331,-0.077722,5.734497,5.860867],[7.882300,-4.430854,7.868126,2.664535,1.404941,-1.871680,5.704948,-0.520817]]], dtype = "float32")#candidate|7340|(2, 5, 8)|const|float32
bop_7341 = relay.add(call_7337.astype('int8'), relay.reshape(const_7340.astype('int8'), relay.shape_of(call_7337))) # shape=(2, 5, 8)
bop_7344 = relay.add(call_7338.astype('int8'), relay.reshape(const_7340.astype('int8'), relay.shape_of(call_7338))) # shape=(2, 5, 8)
func_2017_call = mod.get_global_var('func_2017')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_7358 = relay.TupleGetItem(func_2017_call(), 0)
call_7359 = relay.TupleGetItem(func_2018_call(), 0)
output = relay.Tuple([bop_7341,call_7358,])
output2 = relay.Tuple([bop_7344,call_7359,])
func_7377 = relay.Function([], output)
mod['func_7377'] = func_7377
mod = relay.transform.InferType()(mod)
mutated_mod['func_7377'] = func_7377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7377_call = mutated_mod.get_global_var('func_7377')
call_7378 = func_7377_call()
output = call_7378
func_7379 = relay.Function([], output)
mutated_mod['func_7379'] = func_7379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1911_call = mod.get_global_var('func_1911')
func_1912_call = mutated_mod.get_global_var('func_1912')
call_7382 = relay.TupleGetItem(func_1911_call(), 0)
call_7383 = relay.TupleGetItem(func_1912_call(), 0)
func_5850_call = mod.get_global_var('func_5850')
func_5852_call = mutated_mod.get_global_var('func_5852')
const_7413 = relay.const(4, dtype = "uint32")#candidate|7413|()|const|uint32
call_7412 = relay.TupleGetItem(func_5850_call(relay.reshape(const_7413.astype('uint32'), [])), 2)
call_7414 = relay.TupleGetItem(func_5852_call(relay.reshape(const_7413.astype('uint32'), [])), 2)
output = relay.Tuple([call_7382,call_7412,const_7413,])
output2 = relay.Tuple([call_7383,call_7414,const_7413,])
func_7415 = relay.Function([], output)
mod['func_7415'] = func_7415
mod = relay.transform.InferType()(mod)
mutated_mod['func_7415'] = func_7415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7415_call = mutated_mod.get_global_var('func_7415')
call_7416 = func_7415_call()
output = call_7416
func_7417 = relay.Function([], output)
mutated_mod['func_7417'] = func_7417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_747_call = mod.get_global_var('func_747')
func_749_call = mutated_mod.get_global_var('func_749')
call_7455 = func_747_call()
call_7456 = func_747_call()
func_5927_call = mod.get_global_var('func_5927')
func_5929_call = mutated_mod.get_global_var('func_5929')
call_7465 = relay.TupleGetItem(func_5927_call(), 0)
call_7466 = relay.TupleGetItem(func_5929_call(), 0)
func_6763_call = mod.get_global_var('func_6763')
func_6764_call = mutated_mod.get_global_var('func_6764')
call_7472 = relay.TupleGetItem(func_6763_call(), 1)
call_7473 = relay.TupleGetItem(func_6764_call(), 1)
func_1632_call = mod.get_global_var('func_1632')
func_1633_call = mutated_mod.get_global_var('func_1633')
call_7490 = func_1632_call()
call_7491 = func_1632_call()
var_7498 = relay.var("var_7498", dtype = "float64", shape = (12, 22))#candidate|7498|(12, 22)|var|float64
bop_7499 = relay.bitwise_and(call_7472.astype('int32'), var_7498.astype('int32')) # shape=(12, 22)
bop_7502 = relay.bitwise_and(call_7473.astype('int32'), var_7498.astype('int32')) # shape=(12, 22)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_7504 = relay.TupleGetItem(func_573_call(), 0)
call_7505 = relay.TupleGetItem(func_574_call(), 0)
func_1751_call = mod.get_global_var('func_1751')
func_1752_call = mutated_mod.get_global_var('func_1752')
call_7523 = func_1751_call()
call_7524 = func_1751_call()
output = relay.Tuple([call_7455,call_7465,call_7490,bop_7499,call_7504,call_7523,])
output2 = relay.Tuple([call_7456,call_7466,call_7491,bop_7502,call_7505,call_7524,])
func_7527 = relay.Function([var_7498,], output)
mod['func_7527'] = func_7527
mod = relay.transform.InferType()(mod)
mutated_mod['func_7527'] = func_7527
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7528 = relay.var("var_7528", dtype = "float64", shape = (12, 22))#candidate|7528|(12, 22)|var|float64
func_7527_call = mutated_mod.get_global_var('func_7527')
call_7529 = func_7527_call(var_7528)
output = call_7529
func_7530 = relay.Function([var_7528], output)
mutated_mod['func_7530'] = func_7530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2130_call = mod.get_global_var('func_2130')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_7558 = func_2130_call()
call_7559 = func_2130_call()
output = relay.Tuple([call_7558,])
output2 = relay.Tuple([call_7559,])
func_7561 = relay.Function([], output)
mod['func_7561'] = func_7561
mod = relay.transform.InferType()(mod)
mutated_mod['func_7561'] = func_7561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7561_call = mutated_mod.get_global_var('func_7561')
call_7562 = func_7561_call()
output = call_7562
func_7563 = relay.Function([], output)
mutated_mod['func_7563'] = func_7563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3091_call = mod.get_global_var('func_3091')
func_3093_call = mutated_mod.get_global_var('func_3093')
call_7564 = relay.TupleGetItem(func_3091_call(), 0)
call_7565 = relay.TupleGetItem(func_3093_call(), 0)
func_3406_call = mod.get_global_var('func_3406')
func_3411_call = mutated_mod.get_global_var('func_3411')
var_7577 = relay.var("var_7577", dtype = "uint8", shape = (96,))#candidate|7577|(96,)|var|uint8
var_7578 = relay.var("var_7578", dtype = "float32", shape = (3072,))#candidate|7578|(3072,)|var|float32
const_7579 = relay.const([[1.988881,3.083407],[-0.352122,4.541042],[-4.096914,1.580493],[3.308957,-4.819802],[7.191944,8.250591],[-4.842554,-1.149422],[3.839154,8.991920],[-5.541978,7.223694],[-6.065624,-4.659225],[1.569740,6.484665],[-0.829107,-9.909425],[4.012083,4.971614],[-7.603994,-1.804285],[4.637074,8.744379],[2.840167,-5.509436],[4.833742,6.704984],[7.032197,-8.261534],[5.463932,-0.580856],[2.949455,0.714173],[-7.343736,9.976155],[-8.993654,5.387695],[1.618974,-5.611871],[9.292509,-4.384942],[-9.933056,5.863986],[8.897446,-8.614387],[3.229789,4.304389],[-9.691043,1.387255],[9.700094,9.517306],[-6.837695,7.243175],[0.734183,-1.147652],[3.139555,-4.838466],[-6.317679,3.442248],[4.256777,9.868389],[-3.089743,9.274785],[3.519032,3.717018],[-0.167873,-6.738750],[-1.071641,-2.884081],[3.343290,-7.449858],[1.795861,3.123081],[-3.147572,-7.632788],[-3.596140,-4.204487],[-6.499666,8.349852],[-2.096307,-3.675102],[9.561964,-7.174977],[9.204963,-0.232184],[6.999137,7.055009],[8.196154,1.149706],[3.376352,6.142687],[3.493379,-7.345504],[-2.323183,4.838727],[4.410685,6.907662],[0.775058,-1.010839],[-0.963831,5.965985],[2.917987,-1.071980],[3.794921,0.980822],[5.060077,9.647386],[-7.439214,-6.941256],[7.299989,-2.270094],[-0.507355,-1.269223],[9.355330,-7.370682],[2.389946,1.263507],[-3.544165,0.261951],[4.709320,-7.400840],[0.781606,1.059358],[9.219180,-2.387908],[-2.983149,9.783263],[-4.498065,-9.806163],[-1.813837,5.576762],[-1.881702,2.797949],[2.666259,6.230725],[7.294071,1.075814],[0.077312,-8.041052],[1.882949,2.977396],[8.761847,-5.387441],[-6.519789,7.016637],[5.960724,-2.893048],[-0.205026,-8.694161],[-2.769374,-7.386077],[4.667495,2.681393],[8.282566,7.171171],[-6.162396,-4.790126],[-3.102600,-4.681808],[7.543025,5.570777],[-4.109334,-4.316295],[2.510835,-8.841600],[-1.802146,5.892920],[4.993497,-4.207125],[5.331819,1.596439],[2.129404,9.408105],[-6.495845,-2.086107],[-3.833179,-2.347321],[-0.702303,2.831913],[5.587071,5.894134],[-6.380877,6.192370],[5.137785,-6.671159],[9.840818,3.034618],[3.933156,-7.775771],[-9.107692,6.063058],[4.363285,6.850438],[5.312513,7.219253],[3.404294,-3.175842],[-8.733174,2.323160],[-6.992029,-4.012013],[6.248933,-9.450605],[-9.893185,-6.649081],[7.291494,4.858905],[1.733462,-4.862814],[1.877948,8.354105],[3.801519,3.341030],[6.112637,1.164657],[-0.853535,6.533405],[2.270410,6.008389],[9.333801,-4.901054],[5.626432,0.108647],[5.454616,2.685035],[8.795615,3.850534],[3.450971,-1.694536],[7.774127,-5.074253],[3.057987,5.708314],[4.384584,4.118415],[-7.006516,1.242433],[8.447315,-6.594716],[7.006955,-7.021691],[-2.688399,4.238693],[-3.973675,-7.818500],[9.512710,4.982822],[-6.771038,-5.409805],[2.051473,-7.402896],[4.740115,-5.200089],[-6.879343,2.161367],[-9.808338,6.480072],[5.639785,-6.672869],[-7.064909,3.758100],[2.411261,9.273892],[3.914552,9.068802],[2.547223,-4.636035],[-6.110412,6.180429],[6.049037,-2.241706],[-1.046494,-0.956695],[-5.630161,6.098092],[2.092838,-1.508030],[-7.567145,8.681934],[2.770757,-5.911753],[-0.677622,-3.846860],[4.867344,-0.993537],[-2.378899,5.076479],[-1.161947,9.816703],[-3.190192,3.747147],[9.537364,9.102912],[6.586299,-0.787628],[2.971188,5.226126],[0.927447,-0.212830],[-9.940659,-8.413240],[4.764806,3.199130],[5.514911,-6.446649],[-1.195716,-3.403473],[-6.698960,7.399463],[-8.587250,-0.830396],[-2.968937,3.432817],[3.095345,6.255884],[-8.910031,8.439992],[7.239082,2.354493],[4.000641,-0.666615],[-9.055615,3.948120],[-1.054051,-6.835433],[-1.078202,9.244756],[5.191018,3.907488],[-0.479718,-9.077322],[-0.556353,9.740965],[-4.575851,-2.116456],[-0.281994,0.195543],[9.832188,0.498387],[4.225556,-4.113839],[2.422728,7.839587],[0.132104,4.275831],[0.263264,-4.038872],[4.389224,3.906989],[3.073678,2.492259],[-0.797590,-8.445658],[-6.849767,-3.022884],[2.235212,2.719986],[-7.424266,4.180597],[7.975394,6.679647],[-8.012364,-0.188000],[1.516434,-4.044671],[-6.187146,4.826765],[-1.365942,-9.516502],[3.353442,3.367336],[-9.152406,6.060409],[8.487168,-3.193355],[-9.570566,3.295549],[9.340148,-0.952390],[5.129535,0.438244],[5.088309,-5.736857],[-6.559894,-7.720724],[6.390412,2.454043],[-2.983811,-6.162003],[7.327194,0.334815],[7.844758,9.036383],[-3.263474,0.565299],[-3.863479,8.450608],[3.804738,8.683576],[2.814903,-7.126822],[4.436381,-4.161000],[-2.883629,9.218016],[8.228331,7.789461],[2.711913,1.092246],[3.323532,3.770388],[-4.775983,6.363921],[2.543687,3.577815],[-6.223027,8.968711],[9.539380,4.880053],[6.625760,-9.884132],[3.600901,9.025642],[-3.241527,7.108556],[5.307342,1.536017],[9.893120,-4.390706],[4.670521,0.757640],[8.774633,-1.175074],[-3.174984,-6.708866],[-2.448773,-0.209528],[5.975394,6.894757],[7.842463,3.332456],[2.732921,-6.291317],[2.070506,3.828663],[-3.103208,-4.975801],[-6.893380,0.048659],[-6.131271,-5.791529],[-1.136376,0.178510],[-1.488973,8.343980],[1.278604,-1.377646],[4.723155,3.388394],[7.452261,4.320120],[-3.611023,5.891254],[-9.474765,3.656214],[3.837869,-6.821269],[0.288903,5.724706],[-1.643191,5.222007],[2.008709,-0.373078],[-6.149382,8.904309],[8.020440,4.179779],[-5.126706,-6.158247],[3.122780,5.329511],[2.344906,-0.697397],[0.478166,-0.719527],[-9.016033,3.645352],[0.529072,-2.203925],[-8.849729,-5.868675],[0.312145,3.673340],[-2.036262,-0.490610],[6.279114,-0.996771],[0.254202,3.291432],[-3.025573,-7.987965],[2.904921,-7.832526],[-2.676723,-1.392479],[-5.743651,-5.578706],[4.524390,0.545087],[8.476426,9.923710],[-1.952295,1.666732],[0.001559,-3.567090],[-0.326091,-3.802751],[9.800992,-7.318572],[-3.829945,-0.289963],[7.586682,-1.092627],[-8.817708,7.608318],[7.617072,-4.302525],[-8.920416,-0.950316],[6.367146,-5.842862],[0.805321,8.456056],[7.709845,-8.351988],[6.826258,9.165522],[6.966499,2.677531],[0.181247,5.832886],[8.437732,-5.445180],[3.234566,0.044638]], dtype = "float32")#candidate|7579|(275, 2)|const|float32
call_7576 = relay.TupleGetItem(func_3406_call(relay.reshape(var_7577.astype('uint8'), [96,]), relay.reshape(var_7578.astype('float32'), [3072,]), relay.reshape(const_7579.astype('float32'), [550,]), ), 9)
call_7580 = relay.TupleGetItem(func_3411_call(relay.reshape(var_7577.astype('uint8'), [96,]), relay.reshape(var_7578.astype('float32'), [3072,]), relay.reshape(const_7579.astype('float32'), [550,]), ), 9)
output = relay.Tuple([call_7564,call_7576,var_7577,var_7578,const_7579,])
output2 = relay.Tuple([call_7565,call_7580,var_7577,var_7578,const_7579,])
func_7587 = relay.Function([var_7577,var_7578,], output)
mod['func_7587'] = func_7587
mod = relay.transform.InferType()(mod)
mutated_mod['func_7587'] = func_7587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7587_call = mutated_mod.get_global_var('func_7587')
var_7589 = relay.var("var_7589", dtype = "uint8", shape = (96,))#candidate|7589|(96,)|var|uint8
var_7590 = relay.var("var_7590", dtype = "float32", shape = (3072,))#candidate|7590|(3072,)|var|float32
call_7588 = func_7587_call(var_7589,var_7590,)
output = call_7588
func_7591 = relay.Function([var_7589,var_7590,], output)
mutated_mod['func_7591'] = func_7591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6106_call = mod.get_global_var('func_6106')
func_6107_call = mutated_mod.get_global_var('func_6107')
call_7602 = func_6106_call()
call_7603 = func_6106_call()
output = call_7602
output2 = call_7603
func_7604 = relay.Function([], output)
mod['func_7604'] = func_7604
mod = relay.transform.InferType()(mod)
mutated_mod['func_7604'] = func_7604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7604_call = mutated_mod.get_global_var('func_7604')
call_7605 = func_7604_call()
output = call_7605
func_7606 = relay.Function([], output)
mutated_mod['func_7606'] = func_7606
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7637 = relay.var("var_7637", dtype = "int32", shape = (8, 4, 15))#candidate|7637|(8, 4, 15)|var|int32
const_7638 = relay.const([[[-7,-3,5,-8,-8,-2,9,9,-5,3,6,-3,-6,-7,-2],[-8,8,-3,-9,-3,-6,-9,7,2,6,1,9,6,-4,10],[2,2,7,4,-8,2,3,6,-9,1,-6,-9,6,-8,2],[4,-6,-3,-6,9,-5,-8,2,10,4,9,6,3,-5,2]],[[-1,-1,-5,-9,1,-4,1,-7,-8,6,-8,4,-3,6,9],[7,-4,-6,1,9,5,10,-7,-1,-4,7,-4,-8,7,6],[9,8,2,-4,1,-4,-9,4,-1,-9,6,9,-8,-8,10],[-4,7,-4,-8,-1,2,-7,10,-4,-8,10,-2,5,-5,-8]],[[-5,5,4,3,8,9,9,-2,7,2,3,-1,-10,-7,-7],[3,5,8,-9,-9,4,8,6,-2,6,-10,7,-3,10,-3],[3,3,-4,-9,-1,-10,8,8,-8,9,-6,2,-2,10,5],[1,1,-7,-4,-10,5,-9,9,-9,8,10,8,-5,7,2]],[[-1,9,6,7,-2,-4,6,-10,-3,-2,6,4,4,-4,-7],[4,-1,7,8,-9,10,7,-9,9,-5,-2,2,5,-5,10],[5,-9,-6,-6,-2,-7,8,-8,-3,8,9,9,6,-1,2],[5,5,6,2,-10,-8,-9,-2,-5,6,-1,5,-8,5,-4]],[[-1,8,2,-9,-9,1,7,4,-6,2,-2,7,-6,-8,2],[-2,10,-9,6,-1,1,10,3,-7,3,-1,6,-2,-10,-5],[-4,-5,7,-1,6,-7,5,4,3,6,-3,-1,-2,-1,-5],[7,3,6,-8,4,10,-10,3,4,5,2,-7,-7,5,-3]],[[6,2,2,3,6,3,-3,4,4,1,-7,7,5,-5,6],[1,-10,3,-10,3,6,-5,-6,4,-6,-1,-6,-9,6,1],[5,-4,-4,8,-5,-1,6,9,-2,6,-6,3,7,4,7],[3,-7,7,-6,-5,-8,4,-10,-10,6,2,-2,5,-6,-3]],[[6,3,5,-5,6,3,-6,-10,10,1,-5,-7,10,6,-4],[-9,5,6,-5,-2,-2,-7,-2,7,8,-5,4,1,7,-2],[-8,-1,-4,-4,9,1,1,-10,-6,2,-6,10,10,-4,3],[-7,-6,6,5,-10,-6,-6,1,-7,-4,5,-5,-9,-8,-3]],[[8,4,6,5,-9,-6,10,-9,7,-9,4,-10,-1,-7,4],[2,8,8,-5,9,-2,7,8,-10,-4,5,-5,1,6,6],[8,1,-3,1,-4,2,-7,5,-8,10,5,2,-10,7,2],[3,-1,-5,-3,-6,9,2,-8,-1,1,-8,5,-8,4,-1]]], dtype = "int32")#candidate|7638|(8, 4, 15)|const|int32
bop_7639 = relay.less_equal(var_7637.astype('bool'), relay.reshape(const_7638.astype('bool'), relay.shape_of(var_7637))) # shape=(8, 4, 15)
bop_7645 = relay.greater_equal(var_7637.astype('bool'), relay.reshape(const_7638.astype('bool'), relay.shape_of(var_7637))) # shape=(8, 4, 15)
output = relay.Tuple([bop_7639,bop_7645,])
output2 = relay.Tuple([bop_7639,bop_7645,])
func_7650 = relay.Function([var_7637,], output)
mod['func_7650'] = func_7650
mod = relay.transform.InferType()(mod)
mutated_mod['func_7650'] = func_7650
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7651 = relay.var("var_7651", dtype = "int32", shape = (8, 4, 15))#candidate|7651|(8, 4, 15)|var|int32
func_7650_call = mutated_mod.get_global_var('func_7650')
call_7652 = func_7650_call(var_7651)
output = call_7652
func_7653 = relay.Function([var_7651], output)
mutated_mod['func_7653'] = func_7653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6934_call = mod.get_global_var('func_6934')
func_6935_call = mutated_mod.get_global_var('func_6935')
call_7662 = relay.TupleGetItem(func_6934_call(), 0)
call_7663 = relay.TupleGetItem(func_6935_call(), 0)
output = call_7662
output2 = call_7663
func_7666 = relay.Function([], output)
mod['func_7666'] = func_7666
mod = relay.transform.InferType()(mod)
mutated_mod['func_7666'] = func_7666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7666_call = mutated_mod.get_global_var('func_7666')
call_7667 = func_7666_call()
output = call_7667
func_7668 = relay.Function([], output)
mutated_mod['func_7668'] = func_7668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1169_call = mod.get_global_var('func_1169')
func_1170_call = mutated_mod.get_global_var('func_1170')
call_7784 = relay.TupleGetItem(func_1169_call(), 0)
call_7785 = relay.TupleGetItem(func_1170_call(), 0)
func_3960_call = mod.get_global_var('func_3960')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_7792 = func_3960_call()
call_7793 = func_3960_call()
func_4729_call = mod.get_global_var('func_4729')
func_4733_call = mutated_mod.get_global_var('func_4733')
const_7812 = relay.const([1.782048,2.482856,-2.621420,5.838250,-6.307544,-7.286018,5.293784,8.499891,8.411392,7.427281,-1.310510,5.511849,9.300433,8.719104,8.232181,6.086259,-9.080231,-0.946668,0.235396,-0.300496,-7.534264,7.034260,-1.433981,1.934743,1.052679,8.595094,-3.645115,6.170952,8.716009,5.037901,4.487948,5.496341,3.251975,-9.521604,-4.979265,-3.018048,-4.299231,-7.449290,0.053826,-6.064696,-7.206015,-2.842313,1.105743,-1.657300,-2.801126,7.191534,-7.923691,-0.178298,-0.800063,-3.234607,4.192498,1.722942,-4.282353,-4.750332,-2.592382,-7.796594,5.025110,6.519636,-9.725819,5.012722,9.024503,-1.374960,8.767973,-1.262758,-2.754198,-8.901006,7.101821,2.760667,4.585564,9.923730,-6.462872,-1.752913,8.902641,-2.833812,-3.892945,-6.638135,-0.204755,0.044015,0.054212,-9.992121,3.254788,-5.794942,-8.279499,-4.125680,6.794409,7.417321,-4.314972,5.708627,-2.625128,2.505863,5.218176,-5.240466,1.568781,-6.122550,1.819764,-4.408613,4.108704,-6.375456,-5.993976,-2.709298,-1.449131,9.586087,8.574827,-9.391443,7.715549,-4.960683,-7.565747,-4.964367,2.705186,-8.986946,2.227636,2.301536,7.770073,5.294297,-8.643944,-2.975764,2.751134,1.506473,-4.063765,-0.878712,-3.450209,7.791304,-4.156927,-2.551287,-1.107106,-3.635973,6.234437,-9.400633,6.401245,-7.610552,9.480926,0.091304,-8.230181,-8.713426,-7.782165,-4.868450,6.915431,3.108206,-7.780854,8.829424,0.144669,-5.313737,3.855055,7.531211,-8.911327,4.969217,-8.427660,8.091901,3.207510,-5.214614,-5.983417,-7.043902,-7.832487,8.064445,6.672792,2.422306,1.139820,1.467888,-8.287007,4.374268,-3.078149,6.383868,6.060862,-8.644999,-1.341851,6.981243,4.615845,-5.786556,2.885468,-8.391593,6.653624,8.676963,-9.875916,7.907666,-9.685373,0.004263,0.505590,7.689811,3.070393,-9.837104,-4.985135,9.864937,8.217982,2.030154,3.097255,-0.910187,0.575238,1.759903,-2.819392,2.330257,-3.794585,-6.279848,9.860421,-8.942987,1.964910,-5.818336,-2.006346,0.092846,7.079490,7.583877,5.228682,0.063608,1.117396,-8.745201,-7.045598,-2.042586,-0.163574,-7.961807,3.800627,2.012874,1.369917,-8.926081,5.471644,-0.935033,1.335037,8.136235,2.998342,9.937124,-5.792326,-7.541520,2.397531,8.110776,6.424314,0.590978,-1.042147,3.771273,-9.470283,-6.478582,-9.449700,7.338776,-9.662956,-5.855115,1.891389,-8.513734,6.571448,-8.931990,-9.823789,-2.755662,-4.966322,-6.151256,-1.599648,-3.105534,9.431978,-6.798203,7.535018,7.124742,2.873444,0.979490,-5.801405,-4.218710,0.151165,-5.734771,-8.635369,2.832026,9.933586,6.160366,-3.454024,-1.492773,-7.663777,9.775782,-8.726084,1.776198,-6.581203,6.256072,4.433666,-3.799595,-9.317130,-8.478109,8.411884,8.536655,7.779951,8.599776,4.646788,5.812850,-8.095846,9.833092,-2.481114,-8.303489,-1.349143,9.998379,0.409954,-2.679658,-5.368082,-8.824784,-3.893354,-6.723843,3.652197,5.625963,-7.070865,-4.662005,5.635787,4.473471,9.588338,-3.173448,6.455559,2.384409,8.370772,5.194582,-0.865637,-8.320697,6.175910,-5.977730,-9.124906,7.198629,-7.141745,0.075044,-9.435047,7.179675,4.359613,1.838438,7.437818,6.422444,-8.248325,3.165167,2.559201,0.440643,-3.089384,0.232927,-2.587547,5.458573,-3.852419,-8.003878,-8.641500,-1.827508,-2.283091,-5.577967,-7.069523,-3.959902,-3.446157,1.597533,8.696505,9.180535,-7.292139,-1.866067,3.022689,-5.905015,6.602290,-1.498277,-1.856186,9.608117,-4.277240,7.319643,9.447941,8.943636,1.204796,6.394627,-4.780198,-5.476554,4.293812,7.890457,5.755580,7.713176,-7.395210,-5.119360,-0.773317,4.724361,6.765365,-3.440560,4.787749,0.316620,-0.169118,1.327877,2.906357,-4.450537,5.633363,6.397922,0.740113,6.876270,2.169701,-9.417877,4.394981,-7.848345,-4.073912,0.958584,6.439412,-6.373000,-9.631583,-6.394172,-0.845130,-9.277276,-6.325717,-5.144603,-1.119751,4.710445], dtype = "float64")#candidate|7812|(384,)|const|float64
call_7811 = relay.TupleGetItem(func_4729_call(relay.reshape(call_7792.astype('float32'), [2, 5, 8]), relay.reshape(const_7812.astype('float64'), [384,]), ), 0)
call_7813 = relay.TupleGetItem(func_4733_call(relay.reshape(call_7792.astype('float32'), [2, 5, 8]), relay.reshape(const_7812.astype('float64'), [384,]), ), 0)
output = relay.Tuple([call_7784,call_7792,call_7811,const_7812,])
output2 = relay.Tuple([call_7785,call_7793,call_7813,const_7812,])
func_7816 = relay.Function([], output)
mod['func_7816'] = func_7816
mod = relay.transform.InferType()(mod)
mutated_mod['func_7816'] = func_7816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7816_call = mutated_mod.get_global_var('func_7816')
call_7817 = func_7816_call()
output = call_7817
func_7818 = relay.Function([], output)
mutated_mod['func_7818'] = func_7818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5256_call = mod.get_global_var('func_5256')
func_5257_call = mutated_mod.get_global_var('func_5257')
call_7847 = relay.TupleGetItem(func_5256_call(), 0)
call_7848 = relay.TupleGetItem(func_5257_call(), 0)
output = call_7847
output2 = call_7848
func_7853 = relay.Function([], output)
mod['func_7853'] = func_7853
mod = relay.transform.InferType()(mod)
mutated_mod['func_7853'] = func_7853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7853_call = mutated_mod.get_global_var('func_7853')
call_7854 = func_7853_call()
output = call_7854
func_7855 = relay.Function([], output)
mutated_mod['func_7855'] = func_7855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_7919 = func_1609_call()
call_7920 = func_1609_call()
output = relay.Tuple([call_7919,])
output2 = relay.Tuple([call_7920,])
func_7937 = relay.Function([], output)
mod['func_7937'] = func_7937
mod = relay.transform.InferType()(mod)
mutated_mod['func_7937'] = func_7937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7937_call = mutated_mod.get_global_var('func_7937')
call_7938 = func_7937_call()
output = call_7938
func_7939 = relay.Function([], output)
mutated_mod['func_7939'] = func_7939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mod.get_global_var('func_1892')
func_1893_call = mutated_mod.get_global_var('func_1893')
call_8031 = relay.TupleGetItem(func_1892_call(), 1)
call_8032 = relay.TupleGetItem(func_1893_call(), 1)
func_5374_call = mod.get_global_var('func_5374')
func_5375_call = mutated_mod.get_global_var('func_5375')
call_8070 = relay.TupleGetItem(func_5374_call(), 0)
call_8071 = relay.TupleGetItem(func_5375_call(), 0)
func_5432_call = mod.get_global_var('func_5432')
func_5434_call = mutated_mod.get_global_var('func_5434')
call_8078 = relay.TupleGetItem(func_5432_call(), 0)
call_8079 = relay.TupleGetItem(func_5434_call(), 0)
output = relay.Tuple([call_8031,call_8070,call_8078,])
output2 = relay.Tuple([call_8032,call_8071,call_8079,])
func_8091 = relay.Function([], output)
mod['func_8091'] = func_8091
mod = relay.transform.InferType()(mod)
mutated_mod['func_8091'] = func_8091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8091_call = mutated_mod.get_global_var('func_8091')
call_8092 = func_8091_call()
output = call_8092
func_8093 = relay.Function([], output)
mutated_mod['func_8093'] = func_8093
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8159 = relay.var("var_8159", dtype = "uint8", shape = ())#candidate|8159|()|var|uint8
var_8160 = relay.var("var_8160", dtype = "uint8", shape = (11, 8, 4))#candidate|8160|(11, 8, 4)|var|uint8
bop_8161 = relay.left_shift(var_8159.astype('uint8'), var_8160.astype('uint8')) # shape=(11, 8, 4)
bop_8185 = relay.add(var_8159.astype('uint32'), bop_8161.astype('uint32')) # shape=(11, 8, 4)
output = bop_8185
output2 = bop_8185
func_8190 = relay.Function([var_8159,var_8160,], output)
mod['func_8190'] = func_8190
mod = relay.transform.InferType()(mod)
mutated_mod['func_8190'] = func_8190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8190_call = mutated_mod.get_global_var('func_8190')
var_8192 = relay.var("var_8192", dtype = "uint8", shape = ())#candidate|8192|()|var|uint8
var_8193 = relay.var("var_8193", dtype = "uint8", shape = (11, 8, 4))#candidate|8193|(11, 8, 4)|var|uint8
call_8191 = func_8190_call(var_8192,var_8193,)
output = call_8191
func_8194 = relay.Function([var_8192,var_8193,], output)
mutated_mod['func_8194'] = func_8194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3960_call = mod.get_global_var('func_3960')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_8200 = func_3960_call()
call_8201 = func_3960_call()
output = call_8200
output2 = call_8201
func_8219 = relay.Function([], output)
mod['func_8219'] = func_8219
mod = relay.transform.InferType()(mod)
output = func_8219()
func_8220 = relay.Function([], output)
mutated_mod['func_8220'] = func_8220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7816_call = mod.get_global_var('func_7816')
func_7818_call = mutated_mod.get_global_var('func_7818')
call_8276 = relay.TupleGetItem(func_7816_call(), 2)
call_8277 = relay.TupleGetItem(func_7818_call(), 2)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_8280 = relay.TupleGetItem(func_1830_call(), 0)
call_8281 = relay.TupleGetItem(func_1831_call(), 0)
func_1721_call = mod.get_global_var('func_1721')
func_1722_call = mutated_mod.get_global_var('func_1722')
call_8297 = relay.TupleGetItem(func_1721_call(), 1)
call_8298 = relay.TupleGetItem(func_1722_call(), 1)
output = relay.Tuple([call_8276,call_8280,call_8297,])
output2 = relay.Tuple([call_8277,call_8281,call_8298,])
func_8300 = relay.Function([], output)
mod['func_8300'] = func_8300
mod = relay.transform.InferType()(mod)
mutated_mod['func_8300'] = func_8300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8300_call = mutated_mod.get_global_var('func_8300')
call_8301 = func_8300_call()
output = call_8301
func_8302 = relay.Function([], output)
mutated_mod['func_8302'] = func_8302
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8344 = relay.const([[[1,8,-3,5,9,-6,-3,6],[7,-1,5,3,3,8,8,-4],[3,7,3,5,9,3,-10,10],[-10,-10,-6,-10,2,7,-1,1],[4,-1,-1,-7,2,2,10,1],[-4,4,3,3,3,9,2,9],[9,-3,8,1,-1,-2,-7,-2],[6,-5,1,6,9,-7,7,-8],[-7,9,2,-5,-2,-5,-2,2]],[[-4,-8,-4,-8,-2,-3,-2,7],[2,3,5,1,7,-8,5,-6],[6,2,8,10,-7,-9,4,6],[-2,-1,9,6,-10,-4,6,-3],[-1,2,-7,1,5,-10,-6,6],[7,6,-1,-1,-9,-5,-4,7],[3,7,2,-3,8,8,2,-3],[-3,-5,3,5,-3,-9,9,2],[-3,-4,-9,-2,2,10,-5,-5]],[[3,-3,7,10,-10,-7,-3,3],[-10,-1,-7,3,-2,-5,7,5],[1,-6,-10,8,-5,1,6,6],[-2,-4,-9,-10,1,9,-7,-9],[6,7,-4,-4,-2,9,-10,5],[-3,2,-7,4,-8,-7,9,3],[1,-1,-9,-6,-1,-8,-1,2],[-1,7,-7,-7,5,-9,-9,-2],[-4,-5,-8,-3,-7,10,5,3]],[[6,-5,2,7,-5,-4,1,-5],[8,10,-5,7,-6,-2,-8,-9],[7,-7,-8,-8,1,7,9,8],[6,-3,1,-2,6,-9,1,9],[6,8,-10,-6,10,4,-7,-7],[10,-3,2,9,-9,2,-10,9],[9,-7,8,2,9,7,8,-1],[6,1,-7,-5,1,-8,2,-7],[7,-10,9,10,7,6,-3,-4]],[[-8,6,5,4,1,-7,9,4],[7,-10,-7,6,10,-7,-6,-4],[4,-2,1,5,9,-5,-5,6],[-4,-2,-9,-4,10,-3,-2,3],[-7,7,2,-2,-5,3,7,-5],[8,-1,-4,5,6,-2,-7,6],[-9,-1,-6,-6,-1,2,8,8],[-5,-2,-6,4,-7,2,-1,-7],[3,3,-1,4,-8,10,4,-2]]], dtype = "int16")#candidate|8344|(5, 9, 8)|const|int16
const_8345 = relay.const([[[5,6,-10,1,2,8,9,5],[1,9,-1,-8,-3,3,-7,-5],[-10,6,-10,8,10,-3,5,8],[8,-9,-2,-7,2,-8,4,3],[-4,3,-5,-9,8,-7,2,1],[3,-8,-7,-1,-6,1,-4,-3],[3,-4,1,-7,-5,-4,-10,-8],[4,-9,10,1,-8,-7,7,1],[-8,-10,10,7,-2,4,-3,4]],[[-8,-10,10,6,4,-10,-3,-2],[-6,9,-10,3,5,-1,-10,8],[7,-6,-9,-4,-8,-5,5,-2],[-10,9,7,-1,9,-3,-8,-7],[-10,3,-7,-4,1,-6,7,-9],[10,8,-10,-2,-2,8,-7,-6],[-9,-6,-7,-1,-2,-7,4,-7],[-4,4,3,-2,10,-6,6,3],[2,-2,-10,7,10,10,-10,10]],[[9,7,-7,-6,9,-3,-5,-8],[6,5,-5,-7,-8,8,-5,1],[2,5,-7,8,4,-10,-8,5],[10,-1,4,-7,6,-10,6,2],[-1,9,1,-5,9,-1,4,2],[-5,9,10,2,3,-4,5,-7],[6,-6,3,9,5,-2,7,2],[-6,3,-7,1,-9,9,2,2],[-3,-2,-10,-2,-2,-3,-8,-3]],[[6,-10,1,2,-4,-3,8,4],[-4,10,7,8,-6,-8,-5,-9],[-7,3,10,-7,6,-1,-7,-8],[1,-6,1,8,4,4,-9,2],[3,3,3,-8,-1,-5,-3,-1],[10,3,-3,1,-8,-1,-9,2],[-10,-5,-4,4,-1,-4,-10,1],[6,3,8,9,10,-3,-2,-1],[10,7,-7,7,-8,4,-10,9]],[[-2,5,8,-6,-1,7,5,-8],[-2,-9,4,8,-1,-1,9,6],[4,-3,-5,-3,1,-2,6,1],[4,6,8,-9,8,9,-2,1],[8,10,-5,4,3,-2,5,-8],[5,-7,9,3,6,7,9,-5],[3,4,2,-4,1,5,-1,-5],[6,3,-7,-5,10,-4,1,8],[7,-4,8,-4,-7,-7,2,7]]], dtype = "int16")#candidate|8345|(5, 9, 8)|const|int16
bop_8346 = relay.left_shift(const_8344.astype('int16'), relay.reshape(const_8345.astype('int16'), relay.shape_of(const_8344))) # shape=(5, 9, 8)
output = bop_8346
output2 = bop_8346
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
