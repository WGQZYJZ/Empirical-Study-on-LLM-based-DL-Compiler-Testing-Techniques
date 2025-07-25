import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_69 = relay.var("var_69", dtype = "float32", shape = (9, 1, 15))#candidate|69|(9, 1, 15)|var|float32
uop_70 = relay.cos(var_69.astype('float32')) # shape=(9, 1, 15)
output = uop_70
output2 = uop_70
func_99 = relay.Function([var_69,], output)
mod['func_99'] = func_99
mod = relay.transform.InferType()(mod)
var_100 = relay.var("var_100", dtype = "float32", shape = (9, 1, 15))#candidate|100|(9, 1, 15)|var|float32
output = func_99(var_100)
func_101 = relay.Function([var_100], output)
mutated_mod['func_101'] = func_101
mutated_mod = relay.transform.InferType()(mutated_mod)
const_198 = relay.const([[[-4.721369,3.807826],[2.813860,-5.988397],[8.019701,7.808321],[4.208618,4.451142],[7.978498,5.286176],[-0.265864,3.804374],[7.524171,1.144230],[1.447031,-2.075721],[8.723926,-2.406941]],[[-6.268881,9.516861],[4.415837,-0.915941],[6.538688,-7.135006],[3.624510,6.243999],[2.762167,8.138872],[-0.102264,1.897329],[3.455687,7.141171],[7.787534,5.771483],[-4.046393,1.810681]],[[-3.464056,-8.271085],[5.832240,-3.091301],[-7.841002,0.545780],[4.271061,-6.431640],[9.332894,3.710241],[3.210777,7.052279],[-8.255429,1.650708],[7.196353,1.816192],[-9.980871,0.805595]],[[-0.261711,-0.942957],[-5.158735,-8.032170],[-5.056785,3.439861],[-2.623449,9.844166],[6.072955,-1.701493],[9.917323,-6.203098],[-4.803824,-7.169774],[4.717204,4.981392],[-4.930536,-9.453472]],[[0.794263,-6.865908],[5.644617,5.402728],[-4.605040,-0.266762],[1.333158,0.697696],[-8.912696,5.626176],[5.963184,7.957583],[-7.051641,-2.307222],[7.829733,9.182162],[-4.842379,-7.660470]],[[9.444364,3.499054],[-3.531149,0.327868],[8.930690,9.397373],[-2.527652,-7.460397],[-6.685617,-7.608494],[-2.259534,5.693485],[4.512061,-7.731830],[-3.028703,6.355850],[-2.372635,1.887616]],[[-5.912598,-5.216070],[-0.393613,2.097382],[1.771556,-3.315308],[-6.608614,-1.699331],[-7.350055,-2.535564],[-2.556916,9.928301],[8.804749,-8.057920],[6.682980,3.398161],[-6.862523,8.285489]],[[7.728834,5.302204],[5.522904,-1.661182],[-3.589524,-8.976877],[7.227611,-5.390556],[-7.814255,-8.372978],[-1.532386,9.048856],[0.227297,-8.204459],[4.862469,-0.188483],[-4.182909,8.140860]],[[9.395959,4.074130],[-2.696811,-9.011321],[-8.074380,2.061607],[-4.415243,9.685247],[-0.844014,0.628869],[7.183525,9.872451],[3.749592,5.674544],[7.203225,1.306204],[-2.924200,-6.494703]],[[7.875883,-5.620255],[6.971463,-0.155408],[-3.795613,-9.811145],[-3.013513,-3.043429],[4.714214,-9.893455],[9.654716,8.536431],[-0.952366,7.947022],[4.457207,3.976159],[6.312952,5.496018]],[[3.612981,-1.769694],[0.378966,-7.582599],[-4.904659,3.911441],[-7.249947,2.658200],[7.480288,-0.427169],[9.320286,-0.533571],[4.506399,5.033597],[-3.551846,2.737295],[-9.952876,2.511610]],[[0.240161,-0.334001],[-4.203898,9.874869],[8.196389,-7.099605],[2.947152,4.501139],[-3.624126,-0.190458],[8.482102,-3.721662],[-8.553448,-3.986794],[-9.805198,-6.964991],[9.245542,3.196625]],[[-9.544966,4.548936],[0.614848,-2.651627],[-2.370574,-9.991006],[5.326875,3.921215],[-0.605471,-4.016321],[5.842621,-5.551847],[-7.809713,4.238777],[5.824695,8.184979],[-7.402955,7.312969]],[[-5.381006,-7.508736],[5.299291,-7.402689],[9.647031,-8.052229],[4.158393,-5.630844],[1.630901,-0.451279],[2.931703,9.812178],[9.250594,-7.982370],[0.578940,6.327560],[7.067341,6.360995]],[[-6.321815,-7.461355],[6.224990,-7.131300],[2.055701,4.797509],[3.433061,6.665650],[-8.548633,9.549759],[0.302043,8.160796],[5.057198,0.722403],[-1.534986,-7.116102],[-9.187330,8.378774]]], dtype = "float64")#candidate|198|(15, 9, 2)|const|float64
uop_199 = relay.asinh(const_198.astype('float64')) # shape=(15, 9, 2)
output = relay.Tuple([uop_199,])
output2 = relay.Tuple([uop_199,])
func_225 = relay.Function([], output)
mod['func_225'] = func_225
mod = relay.transform.InferType()(mod)
output = func_225()
func_226 = relay.Function([], output)
mutated_mod['func_226'] = func_226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_239 = relay.TupleGetItem(func_225_call(), 0)
call_240 = relay.TupleGetItem(func_226_call(), 0)
const_248 = relay.const([[[3.137395,-4.573182],[3.183883,-4.191509],[-8.258650,-4.337855],[-7.948413,-7.248309],[-5.345873,5.905825],[7.927211,-4.027976],[-7.490388,-8.558134],[5.733357,-7.866600],[6.596264,0.703561]],[[4.127838,2.297899],[-3.016097,4.446883],[-6.326340,9.972792],[9.758472,-3.320885],[-7.258674,-3.979422],[1.251341,-0.723182],[8.834725,6.410051],[8.829775,3.916769],[5.048174,1.837656]],[[7.045528,-5.265152],[-7.823981,-2.596057],[1.798538,-5.214474],[9.908777,-3.753548],[3.833478,3.615850],[4.737920,9.651268],[5.759360,-6.032680],[8.224594,-1.231353],[-6.667778,1.325838]],[[-1.790310,-4.423810],[-0.825601,8.697338],[9.741706,1.934537],[-7.636887,7.872358],[0.592259,7.773766],[-9.919239,2.437811],[6.957959,-4.033571],[4.619389,-7.821011],[8.554679,8.268832]],[[-4.039190,3.207544],[-5.402189,-0.750024],[-0.489851,-7.339485],[3.717693,-4.980052],[7.226413,9.284306],[-7.212551,-2.659291],[0.229372,0.502199],[2.776572,2.692722],[-6.444352,-7.908461]],[[9.764912,8.983358],[-8.823937,3.350716],[0.352465,7.617889],[-2.642950,1.667469],[-7.095584,-6.780625],[1.356063,-9.070164],[-0.684053,-8.044807],[4.530232,6.064731],[2.377713,-0.674593]],[[-2.304854,7.617699],[9.960157,5.947630],[-1.511478,-2.464050],[-6.068404,-3.451789],[5.499423,0.999578],[-1.491723,-3.422175],[-7.625550,-2.726706],[-3.382390,2.216718],[8.562456,3.791867]],[[-6.570233,-3.008587],[6.452591,8.887002],[3.500883,8.531503],[8.226722,-1.539967],[-4.671009,3.065432],[-8.119231,4.846421],[-4.316682,1.110302],[5.865614,-0.184288],[9.332720,-6.294211]],[[-6.720868,1.284368],[-6.863287,-1.805167],[9.534443,4.046269],[4.313402,-1.046979],[5.570137,-2.298448],[-0.134196,5.543153],[-3.953946,0.396189],[-5.139050,4.766167],[-2.914157,-9.090027]],[[9.932739,-7.121053],[4.293351,8.157761],[-1.372439,-0.572135],[6.084067,1.834438],[-1.016467,4.929382],[-9.573297,6.961465],[8.044517,2.540899],[4.884447,-3.690704],[-0.992415,9.297173]],[[-2.548291,-2.165702],[-1.748873,-7.234797],[-8.221941,6.029006],[-2.275161,1.952319],[-2.834819,9.821321],[5.936501,7.087433],[-9.660380,-5.127138],[-3.031406,-1.683532],[-3.433513,3.027166]],[[0.135088,-5.796995],[5.853395,8.622008],[-2.522279,-9.675759],[3.894467,-9.167828],[1.056187,7.834621],[3.055101,-3.306580],[9.378687,9.463498],[-6.328287,-5.416986],[-8.377365,9.216040]],[[-9.018953,-0.175465],[7.327896,1.046702],[-4.283189,-7.209217],[6.221531,-1.158168],[3.118228,-2.186121],[6.147911,-0.336233],[-0.876477,-9.102535],[7.913179,-7.210513],[-5.523113,-6.543259]],[[-6.656204,-0.738198],[-9.680872,-1.932606],[-4.272830,-0.062122],[8.334644,-8.783650],[-4.813511,-5.299284],[1.169799,-5.654242],[-9.276756,-7.220548],[9.337829,1.808046],[1.989287,-3.600483]],[[-6.400925,1.918605],[8.546091,-7.184469],[1.775623,-9.621804],[9.957983,-3.050033],[3.830080,6.907724],[-7.873561,-5.022392],[-7.839716,5.493587],[0.177560,3.350559],[-8.097527,-5.527789]]], dtype = "float64")#candidate|248|(15, 9, 2)|const|float64
bop_249 = relay.left_shift(call_239.astype('uint8'), relay.reshape(const_248.astype('uint8'), relay.shape_of(call_239))) # shape=(15, 9, 2)
bop_252 = relay.left_shift(call_240.astype('uint8'), relay.reshape(const_248.astype('uint8'), relay.shape_of(call_240))) # shape=(15, 9, 2)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_254 = relay.TupleGetItem(func_225_call(), 0)
call_255 = relay.TupleGetItem(func_226_call(), 0)
func_99_call = mod.get_global_var('func_99')
func_101_call = mutated_mod.get_global_var('func_101')
const_259 = relay.const([6.693163,9.210897,1.444271,-9.471834,-1.922404,0.549661,-1.894764,-0.490098,2.548928,8.857439,-1.627750,3.191022,9.020523,-5.900891,-2.648998,-9.652431,1.060837,-6.851135,5.068633,7.101480,-5.860061,-6.754682,9.711016,-2.756893,-1.040139,0.944558,0.056331,7.594105,4.967235,-6.416514,3.227793,-5.563149,-8.308281,3.244916,0.187690,-9.103238,-8.409819,-2.538425,4.994595,-3.306168,-3.948358,3.095403,-5.546844,6.004682,-8.919162,8.949769,-7.655840,-0.936583,-8.161004,-7.487870,6.586506,-8.292381,0.745283,7.153220,3.986441,0.369355,9.636899,0.883604,3.543643,-6.209671,-5.441270,5.748721,9.091275,-9.646408,2.735748,0.520241,7.129218,-3.001844,9.496342,1.933080,0.851820,-0.007515,9.031763,6.426718,-7.580613,-9.150684,8.375997,6.361255,-3.421452,3.132784,7.232087,-6.930396,-3.765858,2.108071,-5.500280,-5.467952,2.641268,3.299222,-7.185414,8.095246,-5.099244,-1.800907,7.194372,-6.184030,6.235953,-9.260199,-7.595210,2.651749,7.343351,-5.537070,9.578280,-3.985171,-7.449974,-3.997490,-2.011877,7.117844,3.088296,-1.680627,-7.456539,-7.450860,-3.235289,-2.257125,9.516540,7.641562,-7.395870,0.831665,-5.782094,3.402386,4.740292,-4.659586,9.671756,-7.928780,2.018136,-3.077509,5.399618,6.486748,3.383197,-5.183840,5.330446,5.744750,-9.138600,1.558713,-9.453209,9.212594,-1.073212], dtype = "float32")#candidate|259|(135,)|const|float32
call_258 = func_99_call(relay.reshape(const_259.astype('float32'), [9, 1, 15]))
call_260 = func_99_call(relay.reshape(const_259.astype('float32'), [9, 1, 15]))
uop_264 = relay.cos(const_248.astype('float64')) # shape=(15, 9, 2)
output = relay.Tuple([bop_249,call_254,call_258,const_259,uop_264,])
output2 = relay.Tuple([bop_252,call_255,call_260,const_259,uop_264,])
func_269 = relay.Function([], output)
mod['func_269'] = func_269
mod = relay.transform.InferType()(mod)
mutated_mod['func_269'] = func_269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_269_call = mutated_mod.get_global_var('func_269')
call_270 = func_269_call()
output = call_270
func_271 = relay.Function([], output)
mutated_mod['func_271'] = func_271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_269_call = mod.get_global_var('func_269')
func_271_call = mutated_mod.get_global_var('func_271')
call_304 = relay.TupleGetItem(func_269_call(), 3)
call_305 = relay.TupleGetItem(func_271_call(), 3)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_315 = relay.TupleGetItem(func_225_call(), 0)
call_316 = relay.TupleGetItem(func_226_call(), 0)
func_99_call = mod.get_global_var('func_99')
func_101_call = mutated_mod.get_global_var('func_101')
call_328 = func_99_call(relay.reshape(call_304.astype('float32'), [9, 1, 15]))
call_329 = func_99_call(relay.reshape(call_304.astype('float32'), [9, 1, 15]))
uop_342 = relay.cosh(call_328.astype('float32')) # shape=(9, 1, 15)
uop_344 = relay.cosh(call_329.astype('float32')) # shape=(9, 1, 15)
output = relay.Tuple([call_304,call_315,uop_342,])
output2 = relay.Tuple([call_305,call_316,uop_344,])
func_349 = relay.Function([], output)
mod['func_349'] = func_349
mod = relay.transform.InferType()(mod)
output = func_349()
func_350 = relay.Function([], output)
mutated_mod['func_350'] = func_350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_354 = relay.TupleGetItem(func_225_call(), 0)
call_355 = relay.TupleGetItem(func_226_call(), 0)
var_369 = relay.var("var_369", dtype = "float64", shape = (15, 9, 2))#candidate|369|(15, 9, 2)|var|float64
bop_370 = relay.minimum(call_354.astype('int16'), relay.reshape(var_369.astype('int16'), relay.shape_of(call_354))) # shape=(15, 9, 2)
bop_373 = relay.minimum(call_355.astype('int16'), relay.reshape(var_369.astype('int16'), relay.shape_of(call_355))) # shape=(15, 9, 2)
output = relay.Tuple([bop_370,])
output2 = relay.Tuple([bop_373,])
func_378 = relay.Function([var_369,], output)
mod['func_378'] = func_378
mod = relay.transform.InferType()(mod)
mutated_mod['func_378'] = func_378
mutated_mod = relay.transform.InferType()(mutated_mod)
var_379 = relay.var("var_379", dtype = "float64", shape = (15, 9, 2))#candidate|379|(15, 9, 2)|var|float64
func_378_call = mutated_mod.get_global_var('func_378')
call_380 = func_378_call(var_379)
output = call_380
func_381 = relay.Function([var_379], output)
mutated_mod['func_381'] = func_381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_395 = relay.TupleGetItem(func_225_call(), 0)
call_396 = relay.TupleGetItem(func_226_call(), 0)
uop_403 = relay.sqrt(call_395.astype('float64')) # shape=(15, 9, 2)
uop_405 = relay.sqrt(call_396.astype('float64')) # shape=(15, 9, 2)
uop_415 = relay.sinh(call_395.astype('float64')) # shape=(15, 9, 2)
uop_417 = relay.sinh(call_396.astype('float64')) # shape=(15, 9, 2)
bop_421 = relay.logical_or(uop_415.astype('bool'), relay.reshape(call_395.astype('bool'), relay.shape_of(uop_415))) # shape=(15, 9, 2)
bop_424 = relay.logical_or(uop_417.astype('bool'), relay.reshape(call_396.astype('bool'), relay.shape_of(uop_417))) # shape=(15, 9, 2)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_425 = relay.TupleGetItem(func_225_call(), 0)
call_426 = relay.TupleGetItem(func_226_call(), 0)
func_99_call = mod.get_global_var('func_99')
func_101_call = mutated_mod.get_global_var('func_101')
var_431 = relay.var("var_431", dtype = "float32", shape = (3, 45))#candidate|431|(3, 45)|var|float32
call_430 = func_99_call(relay.reshape(var_431.astype('float32'), [9, 1, 15]))
call_432 = func_99_call(relay.reshape(var_431.astype('float32'), [9, 1, 15]))
output = relay.Tuple([uop_403,bop_421,call_425,call_430,var_431,])
output2 = relay.Tuple([uop_405,bop_424,call_426,call_432,var_431,])
func_435 = relay.Function([var_431,], output)
mod['func_435'] = func_435
mod = relay.transform.InferType()(mod)
mutated_mod['func_435'] = func_435
mutated_mod = relay.transform.InferType()(mutated_mod)
var_436 = relay.var("var_436", dtype = "float32", shape = (3, 45))#candidate|436|(3, 45)|var|float32
func_435_call = mutated_mod.get_global_var('func_435')
call_437 = func_435_call(var_436)
output = call_437
func_438 = relay.Function([var_436], output)
mutated_mod['func_438'] = func_438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_447 = relay.var("var_447", dtype = "uint32", shape = ())#candidate|447|()|var|uint32
const_448 = relay.const([[[-4,-10,-6,8,-7,5,1,1]],[[-8,7,9,5,5,7,-4,5]]], dtype = "uint32")#candidate|448|(2, 1, 8)|const|uint32
bop_449 = relay.maximum(var_447.astype('uint32'), const_448.astype('uint32')) # shape=(2, 1, 8)
bop_456 = relay.left_shift(var_447.astype('uint16'), const_448.astype('uint16')) # shape=(2, 1, 8)
var_463 = relay.var("var_463", dtype = "uint32", shape = (2, 16, 8))#candidate|463|(2, 16, 8)|var|uint32
bop_464 = relay.logical_or(const_448.astype('bool'), var_463.astype('bool')) # shape=(2, 16, 8)
uop_468 = relay.rsqrt(bop_449.astype('float32')) # shape=(2, 1, 8)
func_269_call = mod.get_global_var('func_269')
func_271_call = mutated_mod.get_global_var('func_271')
call_475 = relay.TupleGetItem(func_269_call(), 1)
call_476 = relay.TupleGetItem(func_271_call(), 1)
output = relay.Tuple([bop_456,bop_464,uop_468,call_475,])
output2 = relay.Tuple([bop_456,bop_464,uop_468,call_476,])
func_483 = relay.Function([var_447,var_463,], output)
mod['func_483'] = func_483
mod = relay.transform.InferType()(mod)
mutated_mod['func_483'] = func_483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_483_call = mutated_mod.get_global_var('func_483')
var_485 = relay.var("var_485", dtype = "uint32", shape = ())#candidate|485|()|var|uint32
var_486 = relay.var("var_486", dtype = "uint32", shape = (2, 16, 8))#candidate|486|(2, 16, 8)|var|uint32
call_484 = func_483_call(var_485,var_486,)
output = call_484
func_487 = relay.Function([var_485,var_486,], output)
mutated_mod['func_487'] = func_487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_583 = relay.TupleGetItem(func_225_call(), 0)
call_584 = relay.TupleGetItem(func_226_call(), 0)
func_378_call = mod.get_global_var('func_378')
func_381_call = mutated_mod.get_global_var('func_381')
call_616 = relay.TupleGetItem(func_378_call(relay.reshape(call_583.astype('float64'), [15, 9, 2])), 0)
call_617 = relay.TupleGetItem(func_381_call(relay.reshape(call_583.astype('float64'), [15, 9, 2])), 0)
output = relay.Tuple([call_583,call_616,])
output2 = relay.Tuple([call_584,call_617,])
func_625 = relay.Function([], output)
mod['func_625'] = func_625
mod = relay.transform.InferType()(mod)
output = func_625()
func_626 = relay.Function([], output)
mutated_mod['func_626'] = func_626
mutated_mod = relay.transform.InferType()(mutated_mod)
const_657 = relay.const([[[-0.624903,-9.321129,-3.962215,6.514239],[4.825410,3.492320,1.740475,-5.139692],[8.355579,0.622559,-2.820253,2.634512],[4.463179,5.249962,2.269558,-3.960919]],[[3.094825,9.273980,-4.335122,-8.262920],[-3.713112,1.040037,7.550532,1.268862],[7.308907,-3.791196,-5.789299,-4.573894],[9.359692,-3.061697,-9.937856,-9.303364]],[[0.380827,0.073188,-8.209840,-9.773870],[6.931666,-8.872233,6.907574,-0.866279],[3.630301,1.266656,-7.955961,1.596421],[9.310074,-9.326676,-7.810692,-2.853987]],[[-1.475477,5.355868,2.350877,-2.993275],[4.355571,7.075117,-8.939339,0.922924],[-8.293789,-7.618727,-8.059091,5.683602],[8.271395,3.163968,-8.586607,8.758413]],[[-4.253730,-2.219228,-4.348663,-4.310583],[7.918134,0.932937,9.897434,3.712544],[9.966900,-9.243263,9.200167,6.892332],[8.589630,-1.688316,-8.646993,2.179015]],[[-3.393555,-9.901364,-2.222931,7.202998],[-3.348722,4.546094,4.867596,-2.522640],[-3.437719,9.537707,-6.663259,-0.832440],[7.458457,4.158288,7.734207,-9.383490]],[[-1.032824,-0.145350,-4.544018,5.601174],[-9.021558,-7.327504,1.363973,-6.010258],[-8.427042,-7.912656,7.296661,-7.465834],[1.060370,-9.036898,-1.524192,9.128519]],[[-2.590202,1.836708,3.465922,0.117303],[-1.433099,9.663605,-0.988516,9.367747],[3.532374,9.552185,9.706403,-2.248898],[-7.372949,1.722690,3.559334,1.174199]],[[-7.571754,-6.161216,6.250488,-3.064362],[-2.407924,-7.049645,4.867006,0.425087],[9.511923,6.123834,-2.072609,4.677952],[4.156447,-1.034444,5.891491,-4.041077]],[[-0.673297,2.131773,-8.456721,9.990688],[-6.706316,-5.451662,-3.289077,-9.661250],[-8.161954,-5.602235,1.057828,6.413384],[-6.043879,-8.046664,-5.074053,0.712696]],[[3.751704,-3.144845,-5.544066,-0.912454],[4.155265,0.083673,-4.825472,2.260962],[5.757948,-2.703596,-6.109995,4.216771],[8.043130,-8.406362,-8.187594,-9.455215]],[[9.625568,-9.260783,7.538784,-6.805653],[8.091860,-6.007993,5.086755,-0.972929],[4.409321,-7.352449,4.568440,-4.822505],[6.187306,-8.010085,-0.583687,7.235311]],[[2.306183,-2.223766,8.392122,-9.251243],[-5.972326,-9.749573,-5.404763,-8.071657],[7.995710,1.538485,9.778770,8.842643],[7.341755,-7.157356,8.075385,0.872644]],[[1.392390,4.703018,-5.806952,3.108882],[-2.983404,-0.033118,4.529370,-4.249364],[9.245252,8.442661,6.486216,6.550326],[-8.215371,-5.228990,-5.481920,-3.418856]],[[2.066868,-2.283866,2.094317,-2.171954],[1.636680,9.104355,-0.673196,-7.987534],[4.527005,-1.330028,-2.482426,6.168592],[0.392382,-7.446968,4.653534,-4.161615]],[[-9.387608,-3.646642,-0.439609,2.380274],[-3.321375,-7.299869,-7.960329,-3.709848],[-5.222565,-8.483706,2.818494,5.298032],[-6.139754,-8.513063,9.021564,-3.900114]]], dtype = "float32")#candidate|657|(16, 4, 4)|const|float32
uop_658 = relay.log10(const_657.astype('float32')) # shape=(16, 4, 4)
output = uop_658
output2 = uop_658
func_663 = relay.Function([], output)
mod['func_663'] = func_663
mod = relay.transform.InferType()(mod)
mutated_mod['func_663'] = func_663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_663_call = mutated_mod.get_global_var('func_663')
call_664 = func_663_call()
output = call_664
func_665 = relay.Function([], output)
mutated_mod['func_665'] = func_665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_349_call = mod.get_global_var('func_349')
func_350_call = mutated_mod.get_global_var('func_350')
call_668 = relay.TupleGetItem(func_349_call(), 2)
call_669 = relay.TupleGetItem(func_350_call(), 2)
output = call_668
output2 = call_669
func_676 = relay.Function([], output)
mod['func_676'] = func_676
mod = relay.transform.InferType()(mod)
output = func_676()
func_677 = relay.Function([], output)
mutated_mod['func_677'] = func_677
mutated_mod = relay.transform.InferType()(mutated_mod)
var_678 = relay.var("var_678", dtype = "float64", shape = (3, 14, 1))#candidate|678|(3, 14, 1)|var|float64
uop_679 = relay.atanh(var_678.astype('float64')) # shape=(3, 14, 1)
output = uop_679
output2 = uop_679
func_681 = relay.Function([var_678,], output)
mod['func_681'] = func_681
mod = relay.transform.InferType()(mod)
var_682 = relay.var("var_682", dtype = "float64", shape = (3, 14, 1))#candidate|682|(3, 14, 1)|var|float64
output = func_681(var_682)
func_683 = relay.Function([var_682], output)
mutated_mod['func_683'] = func_683
mutated_mod = relay.transform.InferType()(mutated_mod)
var_772 = relay.var("var_772", dtype = "float32", shape = (14, 2, 14))#candidate|772|(14, 2, 14)|var|float32
uop_773 = relay.asinh(var_772.astype('float32')) # shape=(14, 2, 14)
uop_775 = relay.sinh(var_772.astype('float64')) # shape=(14, 2, 14)
output = relay.Tuple([uop_773,uop_775,])
output2 = relay.Tuple([uop_773,uop_775,])
func_787 = relay.Function([var_772,], output)
mod['func_787'] = func_787
mod = relay.transform.InferType()(mod)
mutated_mod['func_787'] = func_787
mutated_mod = relay.transform.InferType()(mutated_mod)
var_788 = relay.var("var_788", dtype = "float32", shape = (14, 2, 14))#candidate|788|(14, 2, 14)|var|float32
func_787_call = mutated_mod.get_global_var('func_787')
call_789 = func_787_call(var_788)
output = call_789
func_790 = relay.Function([var_788], output)
mutated_mod['func_790'] = func_790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_349_call = mod.get_global_var('func_349')
func_350_call = mutated_mod.get_global_var('func_350')
call_794 = relay.TupleGetItem(func_349_call(), 2)
call_795 = relay.TupleGetItem(func_350_call(), 2)
output = call_794
output2 = call_795
func_813 = relay.Function([], output)
mod['func_813'] = func_813
mod = relay.transform.InferType()(mod)
output = func_813()
func_814 = relay.Function([], output)
mutated_mod['func_814'] = func_814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_663_call = mod.get_global_var('func_663')
func_665_call = mutated_mod.get_global_var('func_665')
call_846 = func_663_call()
call_847 = func_663_call()
output = relay.Tuple([call_846,])
output2 = relay.Tuple([call_847,])
func_848 = relay.Function([], output)
mod['func_848'] = func_848
mod = relay.transform.InferType()(mod)
output = func_848()
func_849 = relay.Function([], output)
mutated_mod['func_849'] = func_849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_877 = relay.TupleGetItem(func_225_call(), 0)
call_878 = relay.TupleGetItem(func_226_call(), 0)
output = relay.Tuple([call_877,])
output2 = relay.Tuple([call_878,])
func_888 = relay.Function([], output)
mod['func_888'] = func_888
mod = relay.transform.InferType()(mod)
output = func_888()
func_889 = relay.Function([], output)
mutated_mod['func_889'] = func_889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_938 = relay.TupleGetItem(func_888_call(), 0)
call_939 = relay.TupleGetItem(func_889_call(), 0)
func_813_call = mod.get_global_var('func_813')
func_814_call = mutated_mod.get_global_var('func_814')
call_944 = func_813_call()
call_945 = func_813_call()
output = relay.Tuple([call_938,call_944,])
output2 = relay.Tuple([call_939,call_945,])
func_970 = relay.Function([], output)
mod['func_970'] = func_970
mod = relay.transform.InferType()(mod)
mutated_mod['func_970'] = func_970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mutated_mod.get_global_var('func_970')
call_971 = func_970_call()
output = call_971
func_972 = relay.Function([], output)
mutated_mod['func_972'] = func_972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_1069 = relay.TupleGetItem(func_888_call(), 0)
call_1070 = relay.TupleGetItem(func_889_call(), 0)
func_625_call = mod.get_global_var('func_625')
func_626_call = mutated_mod.get_global_var('func_626')
call_1082 = relay.TupleGetItem(func_625_call(), 0)
call_1083 = relay.TupleGetItem(func_626_call(), 0)
output = relay.Tuple([call_1069,call_1082,])
output2 = relay.Tuple([call_1070,call_1083,])
func_1086 = relay.Function([], output)
mod['func_1086'] = func_1086
mod = relay.transform.InferType()(mod)
mutated_mod['func_1086'] = func_1086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1086_call = mutated_mod.get_global_var('func_1086')
call_1087 = func_1086_call()
output = call_1087
func_1088 = relay.Function([], output)
mutated_mod['func_1088'] = func_1088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_625_call = mod.get_global_var('func_625')
func_626_call = mutated_mod.get_global_var('func_626')
call_1131 = relay.TupleGetItem(func_625_call(), 1)
call_1132 = relay.TupleGetItem(func_626_call(), 1)
func_663_call = mod.get_global_var('func_663')
func_665_call = mutated_mod.get_global_var('func_665')
call_1133 = func_663_call()
call_1134 = func_663_call()
output = relay.Tuple([call_1131,call_1133,])
output2 = relay.Tuple([call_1132,call_1134,])
func_1137 = relay.Function([], output)
mod['func_1137'] = func_1137
mod = relay.transform.InferType()(mod)
output = func_1137()
func_1138 = relay.Function([], output)
mutated_mod['func_1138'] = func_1138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_1172 = relay.TupleGetItem(func_970_call(), 1)
call_1173 = relay.TupleGetItem(func_972_call(), 1)
var_1175 = relay.var("var_1175", dtype = "float32", shape = (9, 4, 15))#candidate|1175|(9, 4, 15)|var|float32
bop_1176 = relay.left_shift(call_1172.astype('int64'), var_1175.astype('int64')) # shape=(9, 4, 15)
bop_1179 = relay.left_shift(call_1173.astype('int64'), var_1175.astype('int64')) # shape=(9, 4, 15)
func_349_call = mod.get_global_var('func_349')
func_350_call = mutated_mod.get_global_var('func_350')
call_1190 = relay.TupleGetItem(func_349_call(), 2)
call_1191 = relay.TupleGetItem(func_350_call(), 2)
output = relay.Tuple([bop_1176,call_1190,])
output2 = relay.Tuple([bop_1179,call_1191,])
func_1196 = relay.Function([var_1175,], output)
mod['func_1196'] = func_1196
mod = relay.transform.InferType()(mod)
var_1197 = relay.var("var_1197", dtype = "float32", shape = (9, 4, 15))#candidate|1197|(9, 4, 15)|var|float32
output = func_1196(var_1197)
func_1198 = relay.Function([var_1197], output)
mutated_mod['func_1198'] = func_1198
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1267 = relay.const(-7, dtype = "uint8")#candidate|1267|()|const|uint8
var_1268 = relay.var("var_1268", dtype = "uint8", shape = (3, 5, 16))#candidate|1268|(3, 5, 16)|var|uint8
bop_1269 = relay.greater(const_1267.astype('bool'), var_1268.astype('bool')) # shape=(3, 5, 16)
output = bop_1269
output2 = bop_1269
func_1272 = relay.Function([var_1268,], output)
mod['func_1272'] = func_1272
mod = relay.transform.InferType()(mod)
mutated_mod['func_1272'] = func_1272
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1273 = relay.var("var_1273", dtype = "uint8", shape = (3, 5, 16))#candidate|1273|(3, 5, 16)|var|uint8
func_1272_call = mutated_mod.get_global_var('func_1272')
call_1274 = func_1272_call(var_1273)
output = call_1274
func_1275 = relay.Function([var_1273], output)
mutated_mod['func_1275'] = func_1275
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1308 = relay.var("var_1308", dtype = "float32", shape = (12, 3, 9))#candidate|1308|(12, 3, 9)|var|float32
var_1309 = relay.var("var_1309", dtype = "float32", shape = (12, 3, 9))#candidate|1309|(12, 3, 9)|var|float32
bop_1310 = relay.floor_divide(var_1308.astype('float32'), relay.reshape(var_1309.astype('float32'), relay.shape_of(var_1308))) # shape=(12, 3, 9)
output = relay.Tuple([bop_1310,])
output2 = relay.Tuple([bop_1310,])
func_1319 = relay.Function([var_1308,var_1309,], output)
mod['func_1319'] = func_1319
mod = relay.transform.InferType()(mod)
mutated_mod['func_1319'] = func_1319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mutated_mod.get_global_var('func_1319')
var_1321 = relay.var("var_1321", dtype = "float32", shape = (12, 3, 9))#candidate|1321|(12, 3, 9)|var|float32
var_1322 = relay.var("var_1322", dtype = "float32", shape = (12, 3, 9))#candidate|1322|(12, 3, 9)|var|float32
call_1320 = func_1319_call(var_1321,var_1322,)
output = call_1320
func_1323 = relay.Function([var_1321,var_1322,], output)
mutated_mod['func_1323'] = func_1323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1137_call = mod.get_global_var('func_1137')
func_1138_call = mutated_mod.get_global_var('func_1138')
call_1378 = relay.TupleGetItem(func_1137_call(), 1)
call_1379 = relay.TupleGetItem(func_1138_call(), 1)
func_1319_call = mod.get_global_var('func_1319')
func_1323_call = mutated_mod.get_global_var('func_1323')
const_1384 = relay.const([[-2.597833,-8.254126,0.198893,6.728202,3.438659,5.134798,8.372450,7.052428,-8.683514,7.588563,7.599081,-8.636253,-8.066743,3.044991,-7.214469,-3.802051,-1.688004,-2.104905,1.026109,3.302479,7.766658,-1.421417,-4.572050,-0.542857,-0.696120,4.657500,5.305239,8.493688,8.441816,5.423934,-9.851064,-0.528366,-9.108308,-1.835108,-1.078859,9.673330,3.639410,-8.679373,8.187355,-5.181867,-8.500010,2.921712,2.931047,9.504707,8.145476,-4.206025,9.712834,-1.120736,-8.577134,5.888314,-5.176423,-2.946300,8.024103,-1.991821,5.445554,-9.086840,-7.041550,0.781027,-6.207706,-6.353701,6.090379,4.150595,9.528827,9.345759,7.799899,-0.292936,5.748511,1.113464,8.861459,9.743875,-0.567257,2.344954,9.043063,-9.565088,2.284742,-2.814873,-6.270524,0.296725,9.459766,0.919257,-8.184833,3.981539,-6.087232,-7.394671,-5.129532,-5.246374,7.581640,0.092494,-6.041342,-4.390472,-9.350591,4.504726,-2.272767,-2.544882,4.960625,-7.610452,4.302483,3.539687,-7.128912,5.151553,1.774875,8.153110,8.912342,9.442142,4.539943,-9.239481,-2.789373,-3.400625,-6.597841,3.631741,-6.990532,5.633137,3.781780,2.996822,-1.568024,-6.855121,-2.399518,-5.982895,-4.820887,9.559294,8.429431,2.954046,1.782303,2.732438,-4.616010,6.748698,-2.758083,-8.020607,1.773176,-5.884502,-1.424824,8.338271,-2.283553,7.178373,-7.275489,-5.215635,-5.931321,1.930069,4.897913,6.888175,1.640448,-7.596267,-8.181769,8.869927,-2.946350,1.066109,-5.301869,8.580361,2.473449,8.695977,-2.187125,2.682400,3.767128,-5.629086,2.307008,-9.533724,8.616891,4.574425,2.314662,1.950967,-9.450065,3.771914,-2.595584,6.636085,0.956279,8.518499,4.606273,-7.549555,1.663280,0.197485,-4.945616,-6.438181,8.518398,1.094222,-7.055527,-7.145817,-5.434933,-3.343782,5.726977,-1.174764,-4.734701,-7.482436,-2.664649,5.487733,1.714303,3.142358,-1.600186,7.259428,5.478397,8.216343,-3.914731,-1.478692,0.928040,9.153774,-3.574121,2.324881,2.147671,-4.411125,-4.087823,4.785187,0.955516,9.350213,-0.042257,5.097822,-3.152653,-9.799112,-6.125387,4.801494,8.253556,-3.892460,-7.484344,-8.125339,9.413762,5.432637,-8.353140,-2.916301,6.274912,-1.318500,-2.830551,3.207932,-1.591999,7.384210,-1.228450,-7.968007,2.254818,-1.262560,-9.866073,8.556184,3.353549,1.569509,-6.353295,1.766437,4.987052,0.699493,0.313402,-7.633668,-3.285036,3.565248,-5.654803,-6.529110,-5.775567,4.665080,-8.549160,9.602734,-5.318399,6.770689,-6.678891,-8.070560,-0.494952,0.555694,6.734915,1.277610,-8.289070,-5.495697,-8.462162,-3.769530,7.251594,0.872509,2.141993,-8.013184,8.139844,-1.225605,-2.214711,-4.752943,-9.358382,2.912359,5.737751,-9.501705,5.044139,9.951494,4.840547,-5.831716,6.691270,-2.816938,-7.405635,-4.378118,9.142103,9.734081,-9.479384,-4.219181,-6.777894,-3.263628,4.904247,2.757441,0.464402,-0.514229,-1.787402,-3.340503,4.874820,-3.884663,0.960854,0.348709,8.324819,-7.256529,-0.732378,8.999513,-8.250533,6.541375,-0.626977,-1.406582,1.326766,-2.972145,-4.598990,2.449816,-2.376868,0.473990,1.386080,-6.551057,-1.977155,-2.593835,4.733166,0.639071,8.071259,2.929219,0.959932,1.253646,9.015536,-0.076182,-0.381876,5.442478,-0.192147,-2.335921,5.722130,-4.477109]], dtype = "float32")#candidate|1384|(1, 324)|const|float32
call_1383 = relay.TupleGetItem(func_1319_call(relay.reshape(const_1384.astype('float32'), [12, 3, 9]), relay.reshape(const_1384.astype('float32'), [12, 3, 9]), ), 0)
call_1385 = relay.TupleGetItem(func_1323_call(relay.reshape(const_1384.astype('float32'), [12, 3, 9]), relay.reshape(const_1384.astype('float32'), [12, 3, 9]), ), 0)
output = relay.Tuple([call_1378,call_1383,const_1384,])
output2 = relay.Tuple([call_1379,call_1385,const_1384,])
func_1392 = relay.Function([], output)
mod['func_1392'] = func_1392
mod = relay.transform.InferType()(mod)
output = func_1392()
func_1393 = relay.Function([], output)
mutated_mod['func_1393'] = func_1393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_1396 = relay.TupleGetItem(func_848_call(), 0)
call_1397 = relay.TupleGetItem(func_849_call(), 0)
output = call_1396
output2 = call_1397
func_1439 = relay.Function([], output)
mod['func_1439'] = func_1439
mod = relay.transform.InferType()(mod)
output = func_1439()
func_1440 = relay.Function([], output)
mutated_mod['func_1440'] = func_1440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_269_call = mod.get_global_var('func_269')
func_271_call = mutated_mod.get_global_var('func_271')
call_1441 = relay.TupleGetItem(func_269_call(), 2)
call_1442 = relay.TupleGetItem(func_271_call(), 2)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_1469 = relay.TupleGetItem(func_848_call(), 0)
call_1470 = relay.TupleGetItem(func_849_call(), 0)
var_1472 = relay.var("var_1472", dtype = "float32", shape = (9, 3, 15))#candidate|1472|(9, 3, 15)|var|float32
bop_1473 = relay.bitwise_xor(call_1441.astype('int16'), var_1472.astype('int16')) # shape=(9, 3, 15)
bop_1476 = relay.bitwise_xor(call_1442.astype('int16'), var_1472.astype('int16')) # shape=(9, 3, 15)
uop_1478 = relay.asinh(var_1472.astype('float64')) # shape=(9, 3, 15)
output = relay.Tuple([call_1469,bop_1473,uop_1478,])
output2 = relay.Tuple([call_1470,bop_1476,uop_1478,])
func_1480 = relay.Function([var_1472,], output)
mod['func_1480'] = func_1480
mod = relay.transform.InferType()(mod)
mutated_mod['func_1480'] = func_1480
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1481 = relay.var("var_1481", dtype = "float32", shape = (9, 3, 15))#candidate|1481|(9, 3, 15)|var|float32
func_1480_call = mutated_mod.get_global_var('func_1480')
call_1482 = func_1480_call(var_1481)
output = call_1482
func_1483 = relay.Function([var_1481], output)
mutated_mod['func_1483'] = func_1483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_1493 = relay.TupleGetItem(func_970_call(), 0)
call_1494 = relay.TupleGetItem(func_972_call(), 0)
uop_1500 = relay.acos(call_1493.astype('float64')) # shape=(15, 9, 2)
uop_1502 = relay.acos(call_1494.astype('float64')) # shape=(15, 9, 2)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
const_1509 = relay.const([-4.142542,-3.966041,9.043810,0.060462,6.342132,5.039897,6.771497,-6.986446,9.254294,8.621715,1.403198,7.570772,-7.296854,-4.094554,-4.124490,3.471274,2.314173,5.262974,-6.528094,-9.248380,2.198541,9.493451,-3.070124,-9.484850,8.934474,-6.038577,9.554226,-5.329587,9.306163,8.033227,2.367908,-8.152772,-0.427003,-6.497935,-1.856589,-2.630287,-5.868164,-1.709733,5.282855,-0.070027,-2.301722,-2.925029], dtype = "float64")#candidate|1509|(42,)|const|float64
call_1508 = func_681_call(relay.reshape(const_1509.astype('float64'), [3, 14, 1]))
call_1510 = func_681_call(relay.reshape(const_1509.astype('float64'), [3, 14, 1]))
output = relay.Tuple([uop_1500,call_1508,const_1509,])
output2 = relay.Tuple([uop_1502,call_1510,const_1509,])
func_1538 = relay.Function([], output)
mod['func_1538'] = func_1538
mod = relay.transform.InferType()(mod)
mutated_mod['func_1538'] = func_1538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1538_call = mutated_mod.get_global_var('func_1538')
call_1539 = func_1538_call()
output = call_1539
func_1540 = relay.Function([], output)
mutated_mod['func_1540'] = func_1540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1086_call = mod.get_global_var('func_1086')
func_1088_call = mutated_mod.get_global_var('func_1088')
call_1605 = relay.TupleGetItem(func_1086_call(), 1)
call_1606 = relay.TupleGetItem(func_1088_call(), 1)
output = call_1605
output2 = call_1606
func_1615 = relay.Function([], output)
mod['func_1615'] = func_1615
mod = relay.transform.InferType()(mod)
mutated_mod['func_1615'] = func_1615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1615_call = mutated_mod.get_global_var('func_1615')
call_1616 = func_1615_call()
output = call_1616
func_1617 = relay.Function([], output)
mutated_mod['func_1617'] = func_1617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_814_call = mutated_mod.get_global_var('func_814')
call_1654 = func_813_call()
call_1655 = func_813_call()
output = call_1654
output2 = call_1655
func_1656 = relay.Function([], output)
mod['func_1656'] = func_1656
mod = relay.transform.InferType()(mod)
mutated_mod['func_1656'] = func_1656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1656_call = mutated_mod.get_global_var('func_1656')
call_1657 = func_1656_call()
output = call_1657
func_1658 = relay.Function([], output)
mutated_mod['func_1658'] = func_1658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_269_call = mod.get_global_var('func_269')
func_271_call = mutated_mod.get_global_var('func_271')
call_1659 = relay.TupleGetItem(func_269_call(), 3)
call_1660 = relay.TupleGetItem(func_271_call(), 3)
output = relay.Tuple([call_1659,])
output2 = relay.Tuple([call_1660,])
func_1661 = relay.Function([], output)
mod['func_1661'] = func_1661
mod = relay.transform.InferType()(mod)
mutated_mod['func_1661'] = func_1661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1661_call = mutated_mod.get_global_var('func_1661')
call_1662 = func_1661_call()
output = call_1662
func_1663 = relay.Function([], output)
mutated_mod['func_1663'] = func_1663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_1685 = func_1439_call()
call_1686 = func_1439_call()
var_1687 = relay.var("var_1687", dtype = "float32", shape = (16, 4, 4))#candidate|1687|(16, 4, 4)|var|float32
bop_1688 = relay.logical_or(call_1685.astype('bool'), relay.reshape(var_1687.astype('bool'), relay.shape_of(call_1685))) # shape=(16, 4, 4)
bop_1691 = relay.logical_or(call_1686.astype('bool'), relay.reshape(var_1687.astype('bool'), relay.shape_of(call_1686))) # shape=(16, 4, 4)
func_1319_call = mod.get_global_var('func_1319')
func_1323_call = mutated_mod.get_global_var('func_1323')
var_1693 = relay.var("var_1693", dtype = "float32", shape = (54, 6))#candidate|1693|(54, 6)|var|float32
call_1692 = relay.TupleGetItem(func_1319_call(relay.reshape(var_1693.astype('float32'), [12, 3, 9]), relay.reshape(var_1693.astype('float32'), [12, 3, 9]), ), 0)
call_1694 = relay.TupleGetItem(func_1323_call(relay.reshape(var_1693.astype('float32'), [12, 3, 9]), relay.reshape(var_1693.astype('float32'), [12, 3, 9]), ), 0)
output = relay.Tuple([bop_1688,call_1692,var_1693,])
output2 = relay.Tuple([bop_1691,call_1694,var_1693,])
func_1701 = relay.Function([var_1687,var_1693,], output)
mod['func_1701'] = func_1701
mod = relay.transform.InferType()(mod)
var_1702 = relay.var("var_1702", dtype = "float32", shape = (16, 4, 4))#candidate|1702|(16, 4, 4)|var|float32
var_1703 = relay.var("var_1703", dtype = "float32", shape = (54, 6))#candidate|1703|(54, 6)|var|float32
output = func_1701(var_1702,var_1703,)
func_1704 = relay.Function([var_1702,var_1703,], output)
mutated_mod['func_1704'] = func_1704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_1834 = relay.TupleGetItem(func_848_call(), 0)
call_1835 = relay.TupleGetItem(func_849_call(), 0)
output = call_1834
output2 = call_1835
func_1854 = relay.Function([], output)
mod['func_1854'] = func_1854
mod = relay.transform.InferType()(mod)
mutated_mod['func_1854'] = func_1854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1854_call = mutated_mod.get_global_var('func_1854')
call_1855 = func_1854_call()
output = call_1855
func_1856 = relay.Function([], output)
mutated_mod['func_1856'] = func_1856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_1865 = relay.TupleGetItem(func_848_call(), 0)
call_1866 = relay.TupleGetItem(func_849_call(), 0)
func_625_call = mod.get_global_var('func_625')
func_626_call = mutated_mod.get_global_var('func_626')
call_1867 = relay.TupleGetItem(func_625_call(), 0)
call_1868 = relay.TupleGetItem(func_626_call(), 0)
output = relay.Tuple([call_1865,call_1867,])
output2 = relay.Tuple([call_1866,call_1868,])
func_1877 = relay.Function([], output)
mod['func_1877'] = func_1877
mod = relay.transform.InferType()(mod)
output = func_1877()
func_1878 = relay.Function([], output)
mutated_mod['func_1878'] = func_1878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_1884 = relay.TupleGetItem(func_848_call(), 0)
call_1885 = relay.TupleGetItem(func_849_call(), 0)
uop_1897 = relay.exp(call_1884.astype('float64')) # shape=(16, 4, 4)
uop_1899 = relay.exp(call_1885.astype('float64')) # shape=(16, 4, 4)
func_99_call = mod.get_global_var('func_99')
func_101_call = mutated_mod.get_global_var('func_101')
const_1903 = relay.const([1.416272,2.389559,7.693657,-2.398297,-0.998250,1.518734,-6.199884,5.548673,9.499693,6.902324,6.378059,-2.699975,9.578202,-7.505695,4.975213,-2.533815,0.183685,0.856793,-2.493744,-8.087987,7.999025,-1.873357,7.909500,-6.096119,-3.978126,1.293210,7.432918,9.520179,-3.794962,3.029355,-1.074861,-5.610107,-6.269009,-8.645544,-8.247383,5.793397,-1.430194,1.586494,4.699197,4.510779,2.306876,8.542810,-9.767433,3.510437,0.467750,-6.097329,-5.524283,1.533693,6.192028,6.399528,-8.245834,9.655602,-7.592743,-9.886708,-4.289856,8.289113,9.111217,8.993798,-2.959790,-0.478140,4.829458,0.343668,9.195933,-2.710837,-8.378915,-4.198274,-6.786348,-3.121524,-9.698796,-4.509629,-1.235274,-3.349217,5.438624,0.248206,-8.511812,7.479193,5.122568,-7.690695,0.686463,0.181671,-2.906037,-3.596774,3.719718,-2.519862,-8.312174,0.765764,-6.071078,-8.412759,8.929594,5.584358,1.384774,0.410498,9.144481,7.333636,8.613810,6.316252,9.436347,-5.152693,-8.980265,-7.992618,-6.842288,9.687512,-4.715503,-7.058436,8.917818,9.061343,-5.778021,4.344698,-7.684307,-7.018988,4.273222,-3.486164,1.992977,-8.285676,1.711738,-3.532133,-1.130157,-6.550426,9.549048,-3.588848,3.921497,3.204314,-6.931274,5.772722,-8.032325,-0.036956,6.222973,-8.041104,-3.396433,-9.131939,6.210268,0.698050,-0.172100,-5.769385,-4.973262], dtype = "float32")#candidate|1903|(135,)|const|float32
call_1902 = func_99_call(relay.reshape(const_1903.astype('float32'), [9, 1, 15]))
call_1904 = func_99_call(relay.reshape(const_1903.astype('float32'), [9, 1, 15]))
output = relay.Tuple([uop_1897,call_1902,const_1903,])
output2 = relay.Tuple([uop_1899,call_1904,const_1903,])
func_1914 = relay.Function([], output)
mod['func_1914'] = func_1914
mod = relay.transform.InferType()(mod)
output = func_1914()
func_1915 = relay.Function([], output)
mutated_mod['func_1915'] = func_1915
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1960 = relay.const([[[-5.434197,6.204359],[-8.743816,-5.510543],[4.726321,2.828387],[-8.600316,-1.513969]],[[-7.537098,-5.503160],[-8.467647,-2.146083],[-1.929142,6.873072],[-8.816706,9.295770]],[[1.924841,-7.363785],[4.075684,0.526536],[1.529869,-4.544508],[-6.874784,-3.080510]],[[0.669038,-9.004790],[7.268626,1.682500],[8.012647,0.920060],[4.599320,-5.104501]],[[7.164847,-9.357625],[5.977313,-5.638599],[-2.723522,-3.264843],[6.373643,2.842859]]], dtype = "float32")#candidate|1960|(5, 4, 2)|const|float32
uop_1961 = relay.acos(const_1960.astype('float32')) # shape=(5, 4, 2)
output = uop_1961
output2 = uop_1961
func_1970 = relay.Function([], output)
mod['func_1970'] = func_1970
mod = relay.transform.InferType()(mod)
output = func_1970()
func_1971 = relay.Function([], output)
mutated_mod['func_1971'] = func_1971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1538_call = mod.get_global_var('func_1538')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_1994 = relay.TupleGetItem(func_1538_call(), 2)
call_1995 = relay.TupleGetItem(func_1540_call(), 2)
var_2002 = relay.var("var_2002", dtype = "float64", shape = (42,))#candidate|2002|(42,)|var|float64
bop_2003 = relay.left_shift(call_1994.astype('int32'), relay.reshape(var_2002.astype('int32'), relay.shape_of(call_1994))) # shape=(42,)
bop_2006 = relay.left_shift(call_1995.astype('int32'), relay.reshape(var_2002.astype('int32'), relay.shape_of(call_1995))) # shape=(42,)
output = relay.Tuple([bop_2003,])
output2 = relay.Tuple([bop_2006,])
func_2013 = relay.Function([var_2002,], output)
mod['func_2013'] = func_2013
mod = relay.transform.InferType()(mod)
mutated_mod['func_2013'] = func_2013
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2014 = relay.var("var_2014", dtype = "float64", shape = (42,))#candidate|2014|(42,)|var|float64
func_2013_call = mutated_mod.get_global_var('func_2013')
call_2015 = func_2013_call(var_2014)
output = call_2015
func_2016 = relay.Function([var_2014], output)
mutated_mod['func_2016'] = func_2016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2021 = relay.TupleGetItem(func_1914_call(), 2)
call_2022 = relay.TupleGetItem(func_1915_call(), 2)
output = call_2021
output2 = call_2022
func_2031 = relay.Function([], output)
mod['func_2031'] = func_2031
mod = relay.transform.InferType()(mod)
mutated_mod['func_2031'] = func_2031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mutated_mod.get_global_var('func_2031')
call_2032 = func_2031_call()
output = call_2032
func_2033 = relay.Function([], output)
mutated_mod['func_2033'] = func_2033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_625_call = mod.get_global_var('func_625')
func_626_call = mutated_mod.get_global_var('func_626')
call_2040 = relay.TupleGetItem(func_625_call(), 0)
call_2041 = relay.TupleGetItem(func_626_call(), 0)
const_2048 = relay.const([[[4.181641,9.133185],[2.463019,6.589433],[6.283467,0.891056],[-9.765319,1.156862],[9.712214,6.690865],[7.370104,7.952140],[-3.599677,-8.620488],[6.222372,-6.923253],[-4.587396,-2.715056]],[[6.439036,-8.815792],[7.645793,-9.213040],[3.949931,-1.843041],[9.703671,4.269218],[-2.737910,-3.973647],[-4.184220,-0.360319],[-2.312102,0.033215],[6.071468,-7.470877],[3.114734,0.293951]],[[1.361497,-4.610266],[8.204420,2.937490],[-2.323445,7.123070],[-5.374915,-5.155681],[-2.896507,-1.166162],[5.580867,8.495073],[6.368251,8.723164],[-9.065149,-0.431645],[-1.874097,2.818225]],[[8.049543,-0.480362],[1.009148,7.783176],[-5.525477,-0.528005],[-8.076363,9.499175],[-9.597805,-0.104941],[5.656364,5.933364],[-7.909809,6.016660],[-1.264930,-2.175127],[0.788626,-1.794212]],[[1.744751,-6.970401],[5.485455,-7.080609],[-6.924969,2.105095],[2.296754,-7.137294],[9.424049,-9.360449],[0.540272,0.302166],[-3.220984,-0.683925],[-8.582271,-8.538776],[-6.951095,5.757337]],[[-5.108368,6.822921],[-8.590202,3.807929],[2.547544,-8.215153],[2.315495,-7.976591],[-9.057465,0.962906],[-8.685211,-6.665012],[-8.602277,-9.710932],[-4.800932,-6.952904],[3.463292,8.865180]],[[-3.111151,9.964140],[-6.589736,-4.408786],[9.588159,0.567109],[-6.002043,-6.498264],[-4.694579,-0.941997],[-8.514317,1.608572],[-1.544417,2.279853],[3.776959,4.258328],[2.583862,4.463267]],[[-1.249776,-2.583028],[9.350956,1.413600],[-5.277476,-8.394202],[6.236599,2.155603],[1.194729,-1.815303],[-9.238722,8.978673],[-3.618102,0.248945],[-0.127645,2.974878],[-4.737628,-5.701433]],[[1.299855,-5.539649],[3.826891,-9.073181],[4.043795,-5.689889],[-3.024965,-0.891634],[-9.763324,6.704814],[5.711477,7.659209],[7.496369,-7.562269],[-4.055167,7.070061],[9.859091,0.426386]],[[-9.753258,7.588664],[2.941523,-9.999956],[-0.626289,-5.311946],[6.267586,4.312127],[-2.800754,-8.763657],[5.009865,3.307879],[7.946680,-0.315628],[-3.819053,7.717759],[8.314831,-9.196988]],[[6.774890,8.735143],[-6.558625,-4.615277],[5.859855,-8.131385],[-9.300602,9.794263],[7.215202,9.940713],[-4.208907,6.223978],[2.495780,9.134143],[0.337692,3.556715],[3.537137,-6.421218]],[[-5.741874,6.772189],[-6.704178,0.152326],[-3.003126,4.476716],[-8.379140,-4.071712],[-3.956585,8.502364],[-4.224293,-1.239942],[7.242703,-8.294990],[-5.238422,-5.868904],[-3.250499,-3.518615]],[[2.322027,1.680122],[1.724502,0.213274],[-3.466100,-9.378917],[-3.517838,-6.323957],[-1.064245,-9.970002],[1.631669,-1.267193],[-3.611612,-7.266944],[-1.563041,9.355041],[0.942012,5.424632]],[[8.963702,-5.779891],[-8.208188,-0.278436],[-8.969048,-7.551810],[-4.670531,-7.838763],[7.402024,0.836181],[9.948480,-3.940910],[7.241439,6.362187],[2.914811,3.312398],[-6.109423,-2.176213]],[[-1.052352,7.109957],[7.146136,1.420777],[-8.030732,5.845532],[2.752168,7.159718],[2.142951,-9.014818],[-4.825115,4.423492],[3.578276,-3.076795],[-7.777839,-9.295106],[-6.596656,1.226372]]], dtype = "float64")#candidate|2048|(15, 9, 2)|const|float64
bop_2049 = relay.logical_xor(call_2040.astype('int32'), relay.reshape(const_2048.astype('int32'), relay.shape_of(call_2040))) # shape=(15, 9, 2)
bop_2052 = relay.logical_xor(call_2041.astype('int32'), relay.reshape(const_2048.astype('int32'), relay.shape_of(call_2041))) # shape=(15, 9, 2)
func_1480_call = mod.get_global_var('func_1480')
func_1483_call = mutated_mod.get_global_var('func_1483')
var_2075 = relay.var("var_2075", dtype = "float32", shape = (405,))#candidate|2075|(405,)|var|float32
call_2074 = relay.TupleGetItem(func_1480_call(relay.reshape(var_2075.astype('float32'), [9, 3, 15])), 1)
call_2076 = relay.TupleGetItem(func_1483_call(relay.reshape(var_2075.astype('float32'), [9, 3, 15])), 1)
func_1538_call = mod.get_global_var('func_1538')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_2079 = relay.TupleGetItem(func_1538_call(), 1)
call_2080 = relay.TupleGetItem(func_1540_call(), 1)
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2082 = relay.TupleGetItem(func_1914_call(), 1)
call_2083 = relay.TupleGetItem(func_1915_call(), 1)
bop_2088 = relay.mod(var_2075.astype('float32'), relay.reshape(call_2074.astype('float32'), relay.shape_of(var_2075))) # shape=(405,)
bop_2091 = relay.mod(var_2075.astype('float32'), relay.reshape(call_2076.astype('float32'), relay.shape_of(var_2075))) # shape=(405,)
output = relay.Tuple([bop_2049,call_2079,call_2082,bop_2088,])
output2 = relay.Tuple([bop_2052,call_2080,call_2083,bop_2091,])
func_2094 = relay.Function([var_2075,], output)
mod['func_2094'] = func_2094
mod = relay.transform.InferType()(mod)
mutated_mod['func_2094'] = func_2094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2095 = relay.var("var_2095", dtype = "float32", shape = (405,))#candidate|2095|(405,)|var|float32
func_2094_call = mutated_mod.get_global_var('func_2094')
call_2096 = func_2094_call(var_2095)
output = call_2096
func_2097 = relay.Function([var_2095], output)
mutated_mod['func_2097'] = func_2097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1661_call = mod.get_global_var('func_1661')
func_1663_call = mutated_mod.get_global_var('func_1663')
call_2113 = relay.TupleGetItem(func_1661_call(), 0)
call_2114 = relay.TupleGetItem(func_1663_call(), 0)
func_483_call = mod.get_global_var('func_483')
func_487_call = mutated_mod.get_global_var('func_487')
var_2130 = relay.var("var_2130", dtype = "uint32", shape = ())#candidate|2130|()|var|uint32
var_2131 = relay.var("var_2131", dtype = "uint32", shape = (256,))#candidate|2131|(256,)|var|uint32
call_2129 = relay.TupleGetItem(func_483_call(relay.reshape(var_2130.astype('uint32'), []), relay.reshape(var_2131.astype('uint32'), [2, 16, 8]), ), 1)
call_2132 = relay.TupleGetItem(func_487_call(relay.reshape(var_2130.astype('uint32'), []), relay.reshape(var_2131.astype('uint32'), [2, 16, 8]), ), 1)
func_378_call = mod.get_global_var('func_378')
func_381_call = mutated_mod.get_global_var('func_381')
const_2138 = relay.const([-5.029930,7.254974,0.830042,-7.115137,8.454857,-6.702255,1.081352,6.663931,6.639264,1.922444,2.827880,6.342048,-1.167075,2.015674,6.211204,-8.917005,-7.267195,-3.512139,-8.463440,3.040297,-0.049391,0.756241,-4.484991,-9.367970,-6.398316,-8.270239,-5.390322,-7.369143,4.216558,-0.820144,9.003552,-8.351645,4.786380,7.868750,3.944394,6.868780,8.404484,3.805519,4.663825,7.041796,4.500208,2.722928,9.168593,-2.286816,-7.830145,7.578977,0.294953,4.101599,6.534453,-7.908593,-0.873746,-4.709987,-9.277097,3.965162,1.941117,7.641410,-1.715092,7.152159,-4.796622,-4.577396,-5.028246,0.130189,1.934955,-2.429437,4.078893,1.641603,-3.526938,9.828821,8.590024,4.203680,-4.135720,4.213916,2.300826,-0.938479,-1.710301,-4.961962,6.085857,-6.528613,3.415329,4.928787,-6.673032,-4.833670,-3.616242,0.182860,-4.195174,7.260093,-0.956759,-1.793549,1.257482,8.304308,4.611183,-6.444370,4.211166,-5.542423,-6.067631,-1.705650,-7.593897,7.797417,-7.889850,4.654290,0.433243,4.519479,4.659786,-6.970487,1.407069,9.987075,8.698393,4.666900,-2.474682,9.365392,0.442234,3.140338,-4.588858,-0.078105,-5.253008,-7.166077,-4.681724,9.076548,0.982224,-4.658913,3.965542,4.733240,-9.927340,-2.114232,-8.749084,3.686429,4.818423,-1.108290,5.549600,-5.624723,-7.307900,-4.331218,2.152487,-6.502360,4.220199,9.627069,-3.813039,3.122064,0.903473,-9.083893,-3.080668,9.680738,-0.776226,4.638420,-2.885837,3.977539,-6.868661,-4.367740,4.412735,-5.694723,9.829879,-4.119135,9.313582,-8.859482,1.194692,-1.190828,-2.020332,2.617577,2.118152,1.835269,-8.849985,-8.344102,-1.990371,-4.601852,-3.462814,-3.182591,-6.425015,2.811724,-2.521731,-7.171500,-6.551161,9.093009,-6.870426,-2.136672,-6.717735,-8.563880,-1.990273,4.158781,8.776399,1.508016,5.564799,4.391462,-6.236506,5.571801,1.028731,-5.608841,-8.190688,-9.414379,-1.465919,2.232054,-2.751795,4.549758,-4.418845,3.869029,7.315181,4.185670,-9.264280,-4.808922,-1.742831,-6.585029,-7.385691,2.524181,-5.069279,4.638313,-4.290845,2.020643,-9.242532,-6.083012,-1.183393,-0.754765,-5.084209,-1.672252,5.781168,3.363918,-0.485583,8.013013,-2.199287,1.884745,-8.748073,9.693769,4.549776,-5.259581,7.855310,7.288817,-8.028018,3.138031,6.273091,-1.140005,6.086897,-3.586127,2.323646,-5.860391,5.016733,-7.615420,-5.626568,-2.815561,3.428036,-1.488021,3.675850,-4.571526,7.881087,-6.963173,4.298955,5.355031,-8.377533,-5.332357,4.399451,1.551768,-6.707151,0.590196,9.877164,5.414527,-3.857697,-2.382653,9.627566,2.637131,-7.772634,5.146121,-0.208602,-0.301731,2.377152,-7.121724,0.249897,0.748476,-4.766087,2.530924,-4.060275,-5.058987,-1.911099,1.108075], dtype = "float64")#candidate|2138|(270,)|const|float64
call_2137 = relay.TupleGetItem(func_378_call(relay.reshape(const_2138.astype('float64'), [15, 9, 2])), 0)
call_2139 = relay.TupleGetItem(func_381_call(relay.reshape(const_2138.astype('float64'), [15, 9, 2])), 0)
output = relay.Tuple([call_2113,call_2129,var_2130,var_2131,call_2137,const_2138,])
output2 = relay.Tuple([call_2114,call_2132,var_2130,var_2131,call_2139,const_2138,])
func_2153 = relay.Function([var_2130,var_2131,], output)
mod['func_2153'] = func_2153
mod = relay.transform.InferType()(mod)
var_2154 = relay.var("var_2154", dtype = "uint32", shape = ())#candidate|2154|()|var|uint32
var_2155 = relay.var("var_2155", dtype = "uint32", shape = (256,))#candidate|2155|(256,)|var|uint32
output = func_2153(var_2154,var_2155,)
func_2156 = relay.Function([var_2154,var_2155,], output)
mutated_mod['func_2156'] = func_2156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_2243 = relay.TupleGetItem(func_848_call(), 0)
call_2244 = relay.TupleGetItem(func_849_call(), 0)
output = call_2243
output2 = call_2244
func_2255 = relay.Function([], output)
mod['func_2255'] = func_2255
mod = relay.transform.InferType()(mod)
mutated_mod['func_2255'] = func_2255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2255_call = mutated_mod.get_global_var('func_2255')
call_2256 = func_2255_call()
output = call_2256
func_2257 = relay.Function([], output)
mutated_mod['func_2257'] = func_2257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_625_call = mod.get_global_var('func_625')
func_626_call = mutated_mod.get_global_var('func_626')
call_2258 = relay.TupleGetItem(func_625_call(), 1)
call_2259 = relay.TupleGetItem(func_626_call(), 1)
output = relay.Tuple([call_2258,])
output2 = relay.Tuple([call_2259,])
func_2264 = relay.Function([], output)
mod['func_2264'] = func_2264
mod = relay.transform.InferType()(mod)
output = func_2264()
func_2265 = relay.Function([], output)
mutated_mod['func_2265'] = func_2265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2255_call = mod.get_global_var('func_2255')
func_2257_call = mutated_mod.get_global_var('func_2257')
call_2273 = func_2255_call()
call_2274 = func_2255_call()
output = relay.Tuple([call_2273,])
output2 = relay.Tuple([call_2274,])
func_2285 = relay.Function([], output)
mod['func_2285'] = func_2285
mod = relay.transform.InferType()(mod)
output = func_2285()
func_2286 = relay.Function([], output)
mutated_mod['func_2286'] = func_2286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1656_call = mod.get_global_var('func_1656')
func_1658_call = mutated_mod.get_global_var('func_1658')
call_2323 = func_1656_call()
call_2324 = func_1656_call()
output = call_2323
output2 = call_2324
func_2330 = relay.Function([], output)
mod['func_2330'] = func_2330
mod = relay.transform.InferType()(mod)
output = func_2330()
func_2331 = relay.Function([], output)
mutated_mod['func_2331'] = func_2331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_625_call = mod.get_global_var('func_625')
func_626_call = mutated_mod.get_global_var('func_626')
call_2356 = relay.TupleGetItem(func_625_call(), 1)
call_2357 = relay.TupleGetItem(func_626_call(), 1)
output = relay.Tuple([call_2356,])
output2 = relay.Tuple([call_2357,])
func_2360 = relay.Function([], output)
mod['func_2360'] = func_2360
mod = relay.transform.InferType()(mod)
output = func_2360()
func_2361 = relay.Function([], output)
mutated_mod['func_2361'] = func_2361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1392_call = mod.get_global_var('func_1392')
func_1393_call = mutated_mod.get_global_var('func_1393')
call_2396 = relay.TupleGetItem(func_1392_call(), 1)
call_2397 = relay.TupleGetItem(func_1393_call(), 1)
func_1392_call = mod.get_global_var('func_1392')
func_1393_call = mutated_mod.get_global_var('func_1393')
call_2412 = relay.TupleGetItem(func_1392_call(), 0)
call_2413 = relay.TupleGetItem(func_1393_call(), 0)
func_1137_call = mod.get_global_var('func_1137')
func_1138_call = mutated_mod.get_global_var('func_1138')
call_2415 = relay.TupleGetItem(func_1137_call(), 1)
call_2416 = relay.TupleGetItem(func_1138_call(), 1)
var_2417 = relay.var("var_2417", dtype = "float32", shape = (16, 4, 4))#candidate|2417|(16, 4, 4)|var|float32
bop_2418 = relay.greater(call_2415.astype('bool'), relay.reshape(var_2417.astype('bool'), relay.shape_of(call_2415))) # shape=(16, 4, 4)
bop_2421 = relay.greater(call_2416.astype('bool'), relay.reshape(var_2417.astype('bool'), relay.shape_of(call_2416))) # shape=(16, 4, 4)
func_813_call = mod.get_global_var('func_813')
func_814_call = mutated_mod.get_global_var('func_814')
call_2422 = func_813_call()
call_2423 = func_813_call()
func_2255_call = mod.get_global_var('func_2255')
func_2257_call = mutated_mod.get_global_var('func_2257')
call_2427 = func_2255_call()
call_2428 = func_2255_call()
output = relay.Tuple([call_2396,call_2412,bop_2418,call_2422,call_2427,])
output2 = relay.Tuple([call_2397,call_2413,bop_2421,call_2423,call_2428,])
func_2430 = relay.Function([var_2417,], output)
mod['func_2430'] = func_2430
mod = relay.transform.InferType()(mod)
var_2431 = relay.var("var_2431", dtype = "float32", shape = (16, 4, 4))#candidate|2431|(16, 4, 4)|var|float32
output = func_2430(var_2431)
func_2432 = relay.Function([var_2431], output)
mutated_mod['func_2432'] = func_2432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2255_call = mod.get_global_var('func_2255')
func_2257_call = mutated_mod.get_global_var('func_2257')
call_2502 = func_2255_call()
call_2503 = func_2255_call()
func_663_call = mod.get_global_var('func_663')
func_665_call = mutated_mod.get_global_var('func_665')
call_2508 = func_663_call()
call_2509 = func_663_call()
uop_2510 = relay.sqrt(call_2502.astype('float64')) # shape=(16, 4, 4)
uop_2512 = relay.sqrt(call_2503.astype('float64')) # shape=(16, 4, 4)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_2516 = relay.TupleGetItem(func_225_call(), 0)
call_2517 = relay.TupleGetItem(func_226_call(), 0)
func_2285_call = mod.get_global_var('func_2285')
func_2286_call = mutated_mod.get_global_var('func_2286')
call_2525 = relay.TupleGetItem(func_2285_call(), 0)
call_2526 = relay.TupleGetItem(func_2286_call(), 0)
output = relay.Tuple([call_2508,uop_2510,call_2516,call_2525,])
output2 = relay.Tuple([call_2509,uop_2512,call_2517,call_2526,])
func_2536 = relay.Function([], output)
mod['func_2536'] = func_2536
mod = relay.transform.InferType()(mod)
output = func_2536()
func_2537 = relay.Function([], output)
mutated_mod['func_2537'] = func_2537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_2541 = relay.TupleGetItem(func_888_call(), 0)
call_2542 = relay.TupleGetItem(func_889_call(), 0)
output = relay.Tuple([call_2541,])
output2 = relay.Tuple([call_2542,])
func_2543 = relay.Function([], output)
mod['func_2543'] = func_2543
mod = relay.transform.InferType()(mod)
mutated_mod['func_2543'] = func_2543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mutated_mod.get_global_var('func_2543')
call_2544 = func_2543_call()
output = call_2544
func_2545 = relay.Function([], output)
mutated_mod['func_2545'] = func_2545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2255_call = mod.get_global_var('func_2255')
func_2257_call = mutated_mod.get_global_var('func_2257')
call_2581 = func_2255_call()
call_2582 = func_2255_call()
func_2430_call = mod.get_global_var('func_2430')
func_2432_call = mutated_mod.get_global_var('func_2432')
call_2588 = relay.TupleGetItem(func_2430_call(relay.reshape(call_2581.astype('float32'), [16, 4, 4])), 0)
call_2589 = relay.TupleGetItem(func_2432_call(relay.reshape(call_2581.astype('float32'), [16, 4, 4])), 0)
func_1196_call = mod.get_global_var('func_1196')
func_1198_call = mutated_mod.get_global_var('func_1198')
var_2591 = relay.var("var_2591", dtype = "float32", shape = (540,))#candidate|2591|(540,)|var|float32
call_2590 = relay.TupleGetItem(func_1196_call(relay.reshape(var_2591.astype('float32'), [9, 4, 15])), 0)
call_2592 = relay.TupleGetItem(func_1198_call(relay.reshape(var_2591.astype('float32'), [9, 4, 15])), 0)
output = relay.Tuple([call_2581,call_2588,call_2590,var_2591,])
output2 = relay.Tuple([call_2582,call_2589,call_2592,var_2591,])
func_2595 = relay.Function([var_2591,], output)
mod['func_2595'] = func_2595
mod = relay.transform.InferType()(mod)
var_2596 = relay.var("var_2596", dtype = "float32", shape = (540,))#candidate|2596|(540,)|var|float32
output = func_2595(var_2596)
func_2597 = relay.Function([var_2596], output)
mutated_mod['func_2597'] = func_2597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_2605 = relay.TupleGetItem(func_970_call(), 0)
call_2606 = relay.TupleGetItem(func_972_call(), 0)
func_2013_call = mod.get_global_var('func_2013')
func_2016_call = mutated_mod.get_global_var('func_2016')
var_2620 = relay.var("var_2620", dtype = "float64", shape = (42,))#candidate|2620|(42,)|var|float64
call_2619 = relay.TupleGetItem(func_2013_call(relay.reshape(var_2620.astype('float64'), [42,])), 0)
call_2621 = relay.TupleGetItem(func_2016_call(relay.reshape(var_2620.astype('float64'), [42,])), 0)
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2632 = relay.TupleGetItem(func_1914_call(), 2)
call_2633 = relay.TupleGetItem(func_1915_call(), 2)
func_2330_call = mod.get_global_var('func_2330')
func_2331_call = mutated_mod.get_global_var('func_2331')
call_2640 = func_2330_call()
call_2641 = func_2330_call()
const_2671 = relay.const([-7,2,10,6,-1,3,3,10,5,6,6,-2,3,8,9,1,1,-5,3,8,-4,-5,-1,4,-7,-8,6,-7,-6,-2,3,1,9,4,5,-7,-6,-9,7,3,-6,4], dtype = "int32")#candidate|2671|(42,)|const|int32
bop_2672 = relay.minimum(call_2619.astype('uint8'), relay.reshape(const_2671.astype('uint8'), relay.shape_of(call_2619))) # shape=(42,)
bop_2675 = relay.minimum(call_2621.astype('uint8'), relay.reshape(const_2671.astype('uint8'), relay.shape_of(call_2621))) # shape=(42,)
output = relay.Tuple([call_2605,var_2620,call_2632,call_2640,bop_2672,])
output2 = relay.Tuple([call_2606,var_2620,call_2633,call_2641,bop_2675,])
func_2680 = relay.Function([var_2620,], output)
mod['func_2680'] = func_2680
mod = relay.transform.InferType()(mod)
var_2681 = relay.var("var_2681", dtype = "float64", shape = (42,))#candidate|2681|(42,)|var|float64
output = func_2680(var_2681)
func_2682 = relay.Function([var_2681], output)
mutated_mod['func_2682'] = func_2682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2545_call = mutated_mod.get_global_var('func_2545')
call_2686 = relay.TupleGetItem(func_2543_call(), 0)
call_2687 = relay.TupleGetItem(func_2545_call(), 0)
output = relay.Tuple([call_2686,])
output2 = relay.Tuple([call_2687,])
func_2736 = relay.Function([], output)
mod['func_2736'] = func_2736
mod = relay.transform.InferType()(mod)
output = func_2736()
func_2737 = relay.Function([], output)
mutated_mod['func_2737'] = func_2737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1970_call = mod.get_global_var('func_1970')
func_1971_call = mutated_mod.get_global_var('func_1971')
call_2742 = func_1970_call()
call_2743 = func_1970_call()
func_1701_call = mod.get_global_var('func_1701')
func_1704_call = mutated_mod.get_global_var('func_1704')
var_2766 = relay.var("var_2766", dtype = "float32", shape = (16, 16))#candidate|2766|(16, 16)|var|float32
const_2767 = relay.const([9.397901,-3.548716,3.394547,0.716057,-5.353818,3.148039,-1.038909,-9.694832,0.151277,6.288786,-3.825938,-4.709493,-4.864873,-3.481391,-8.373228,9.291003,-7.760232,3.717578,0.255461,9.152945,0.553337,-0.079975,-8.646328,-1.695379,-2.204008,-2.752120,-1.799296,4.232258,8.339209,-4.041083,-3.409833,2.027185,7.286639,8.998829,5.424157,-7.533543,0.258381,-0.974098,2.865954,-7.899547,-3.929964,-0.344227,9.494816,6.978072,-3.238184,-2.055417,3.197438,7.234633,8.291571,3.512490,2.686736,4.110595,-7.540767,-9.705254,9.115602,1.400319,8.642322,-4.250441,4.226632,0.948903,5.140367,7.712875,1.340501,4.818590,0.499508,8.296554,-3.816161,0.177120,-3.887293,-4.906138,-1.023469,-5.770899,-2.642397,-1.835127,-6.969374,9.931335,-5.829598,0.379526,2.731574,-6.729330,5.010641,4.508702,-2.985427,9.510455,9.043005,-4.318037,1.906401,9.673042,9.180614,-2.875873,-8.652662,4.814494,-9.131651,-6.846926,3.660565,-3.152925,5.014082,-9.314119,-8.188265,-8.341069,-5.026514,-3.346923,4.322304,6.245430,3.587475,2.584248,0.276352,-4.524909,0.594187,5.988780,6.773705,3.963785,4.222067,5.054973,7.236461,0.746586,-1.980284,-6.836350,-8.951221,1.149621,0.030374,7.836069,1.759864,-6.885082,-2.354863,-1.686152,0.578913,-2.688570,3.084363,-7.043267,-0.261155,-7.348315,4.960387,-1.859035,-6.918848,-7.005740,-2.210766,-3.438984,3.786131,-9.191299,-2.558867,-5.812582,5.059531,5.188188,-8.395645,8.377738,0.416157,3.679280,-5.814536,-8.219600,1.256842,-1.576680,-0.697863,-4.770074,1.377541,-3.129571,0.256602,4.112769,9.656616,0.692393,2.864764,-4.397618,0.281154,4.453559,-6.323006,-6.536767,-6.297055,3.590505,-7.898493,2.067093,5.032899,5.721910,-9.686649,7.463080,0.904854,4.083057,3.213737,-0.201264,8.517909,3.604389,2.954042,-0.182559,-9.127096,7.323929,1.417938,5.255783,-0.331186,6.270746,7.746690,-4.540136,5.401288,6.247754,-1.257810,5.681041,-7.758178,5.142745,1.777738,3.749335,8.771209,-1.088987,3.339609,9.968541,-1.675784,-3.235593,0.392840,6.485934,-7.517634,-8.521637,-8.204457,9.580660,-1.392752,-9.084321,-9.911352,7.229845,-6.191426,-9.466152,5.220074,9.841622,-6.842302,-4.760044,8.386642,-7.914299,-6.445317,-9.879060,5.298473,1.092865,-6.096623,3.969439,-4.477684,-1.371507,-0.076789,-1.152551,5.756863,5.187959,-8.396782,5.227652,4.140232,1.369892,-2.189038,-9.800039,0.111476,6.612834,-0.502757,-5.279067,-5.629367,7.667485,1.752204,-6.677420,-8.203158,-8.719509,6.937942,-2.550349,-2.623116,5.876663,7.807804,-2.713817,3.608610,-4.497820,-9.743021,-7.092194,2.714008,5.600607,-7.837747,3.113481,5.568699,7.544087,-5.826770,-3.037778,0.014408,0.320820,2.286592,-9.155031,-4.578182,-2.762099,7.104121,5.251212,7.137758,-9.160269,-2.290568,-5.422033,3.163652,2.310839,4.254441,-1.544463,5.701665,9.328360,5.582401,5.263868,-5.354337,-6.488947,3.611355,-4.594464,-4.974094,-6.126581,7.482515,5.570088,-9.887683,-4.307154,-5.646695,-4.428073,-1.690653,-8.023249,3.581949,6.124015,-3.454142,-4.760549,4.505857,-0.066432,9.115679,4.180940,3.771839,2.175924,3.357429,2.967722,9.577517,2.600250,9.510587,9.808455,1.933613,-3.927986,3.764162,5.180391,2.423409,-7.790509], dtype = "float32")#candidate|2767|(324,)|const|float32
call_2765 = relay.TupleGetItem(func_1701_call(relay.reshape(var_2766.astype('float32'), [16, 4, 4]), relay.reshape(const_2767.astype('float32'), [54, 6]), ), 0)
call_2768 = relay.TupleGetItem(func_1704_call(relay.reshape(var_2766.astype('float32'), [16, 4, 4]), relay.reshape(const_2767.astype('float32'), [54, 6]), ), 0)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_2771 = func_2031_call()
call_2772 = func_2031_call()
output = relay.Tuple([call_2742,call_2765,var_2766,const_2767,call_2771,])
output2 = relay.Tuple([call_2743,call_2768,var_2766,const_2767,call_2772,])
func_2776 = relay.Function([var_2766,], output)
mod['func_2776'] = func_2776
mod = relay.transform.InferType()(mod)
mutated_mod['func_2776'] = func_2776
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2777 = relay.var("var_2777", dtype = "float32", shape = (16, 16))#candidate|2777|(16, 16)|var|float32
func_2776_call = mutated_mod.get_global_var('func_2776')
call_2778 = func_2776_call(var_2777)
output = call_2778
func_2779 = relay.Function([var_2777], output)
mutated_mod['func_2779'] = func_2779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_2813 = func_1439_call()
call_2814 = func_1439_call()
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2820 = relay.TupleGetItem(func_1914_call(), 2)
call_2821 = relay.TupleGetItem(func_1915_call(), 2)
output = relay.Tuple([call_2813,call_2820,])
output2 = relay.Tuple([call_2814,call_2821,])
func_2845 = relay.Function([], output)
mod['func_2845'] = func_2845
mod = relay.transform.InferType()(mod)
mutated_mod['func_2845'] = func_2845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2845_call = mutated_mod.get_global_var('func_2845')
call_2846 = func_2845_call()
output = call_2846
func_2847 = relay.Function([], output)
mutated_mod['func_2847'] = func_2847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_676_call = mod.get_global_var('func_676')
func_677_call = mutated_mod.get_global_var('func_677')
call_2881 = func_676_call()
call_2882 = func_676_call()
const_2888 = relay.const([[[5.089045,-8.297670,4.320766,-5.563283,-8.250008,-8.749141,-5.932898,-5.061929,-6.251830,-9.626699,-8.521013,0.749021,4.902136,-9.227457,-6.155575],[2.900026,3.569714,-4.317842,6.464232,-6.815738,-9.213879,4.667150,2.830627,-2.025753,0.706963,-3.338909,-1.032682,-8.040570,2.036916,1.604255]],[[-1.027935,5.078825,-5.758628,-7.809892,-8.521530,6.644930,6.028201,5.770352,-1.841600,-3.312534,-0.908905,5.208309,-2.147133,-8.943217,-1.859488],[8.771761,-1.209448,-9.750638,-6.851017,0.977185,0.469968,-6.208763,8.016139,3.472349,8.023469,6.202842,3.574103,-8.014588,-0.347831,4.121030]],[[-0.594470,5.391525,6.452909,5.383305,-9.915104,-9.138605,6.958767,-6.229594,0.708429,5.503037,4.139417,-6.823796,9.395777,-0.471224,-3.831830],[5.216540,-0.996399,9.185540,-6.951067,-4.463399,9.447295,4.795222,4.359690,8.171549,8.704828,0.112120,-7.000076,2.925754,-4.305091,7.918611]],[[3.780727,6.887661,-2.066631,8.157182,4.970256,7.940016,0.239337,9.085444,3.583080,9.987373,8.005633,7.817833,-5.520924,-8.110873,9.124908],[3.210058,-2.701235,-1.436636,-0.922480,4.429184,0.338142,-7.141323,1.628928,5.744692,3.055787,-6.453465,1.122758,-8.022653,-3.020454,-1.784362]],[[-1.707410,6.035403,-7.231460,2.313998,3.319885,-0.775939,-8.498628,7.572991,3.368446,-8.113264,0.536596,4.821341,-4.072426,5.463701,-2.287746],[-6.142435,0.811214,3.405140,-5.033255,-1.538324,-9.123847,-4.410521,-4.891736,-6.387752,8.167589,-7.383106,0.476678,9.835798,0.593266,2.040181]],[[1.313126,-5.499725,1.829672,-4.807501,8.788190,2.112598,-6.626339,-2.991184,-9.272518,-6.968116,8.874184,-3.795373,-6.628725,-5.817309,-2.124349],[-3.503457,-4.065627,1.819622,-2.842927,5.019386,-7.728350,0.098921,-7.978748,4.846057,0.151677,-5.352782,-4.401850,1.499998,1.516136,-4.749132]],[[0.250380,0.799478,-5.768641,7.230398,-1.607583,-6.190292,-3.297836,9.453559,0.053024,5.434644,-3.354535,0.674912,-4.516491,-8.652014,-9.354084],[-4.386803,2.309975,3.434960,-9.307727,-1.374506,2.347844,5.236716,7.479960,9.560969,-4.917150,1.051411,-3.227427,5.895157,6.301605,-4.058609]],[[5.413145,-8.260656,-3.568478,-2.292704,-0.342817,-5.233284,3.128050,4.374331,-9.332883,0.612487,6.521497,-0.338738,8.450048,4.250306,9.120300],[-6.833857,-0.126928,4.210627,0.403591,8.037319,-4.102123,9.344376,1.355486,-1.958914,8.849581,-2.874292,-2.519438,9.721160,5.074689,2.013652]],[[-1.334520,0.249481,-0.169115,-0.988845,-7.446871,6.928465,1.461658,-7.567733,-1.010170,-3.293333,-7.395094,-9.657629,6.947585,-5.438601,-3.700109],[6.123323,5.078996,5.872650,4.478710,1.800725,4.646361,3.943063,-8.374478,-0.118264,-8.601192,-3.342038,0.054170,-5.639191,-3.286057,0.551002]]], dtype = "float32")#candidate|2888|(9, 2, 15)|const|float32
bop_2889 = relay.greater_equal(call_2881.astype('bool'), const_2888.astype('bool')) # shape=(9, 2, 15)
bop_2892 = relay.greater_equal(call_2882.astype('bool'), const_2888.astype('bool')) # shape=(9, 2, 15)
func_2776_call = mod.get_global_var('func_2776')
func_2779_call = mutated_mod.get_global_var('func_2779')
const_2894 = relay.const([[3.299186,6.529453,-2.103075,-5.806712,-3.830772,-5.328737,9.654619,0.803836],[8.730652,5.369973,-3.666054,-5.964534,-8.990972,-1.599218,-7.418418,-7.693588],[1.869218,4.382785,3.268224,6.008649,-2.331155,-5.349719,-2.784942,-1.765536],[0.996161,7.023608,4.144704,9.202616,9.970555,-8.253437,-9.477917,7.083861],[4.288200,8.064478,1.895644,-5.502837,-4.820856,4.148687,9.335876,0.096687],[0.208454,-9.410660,-5.130813,-3.519877,5.828402,6.444754,9.467497,-4.785985],[-8.550666,-0.300800,-6.634751,4.049906,6.665240,7.801494,-1.697936,-8.632905],[-1.139472,-2.717064,-8.320839,-7.560702,-9.751406,3.810181,4.570974,-3.481874],[-1.984143,9.138176,3.352318,3.889072,2.821800,7.974444,9.000276,5.525186],[-9.305394,-5.832656,5.594812,3.625453,6.690379,7.867862,-7.623415,-9.366287],[-6.324529,0.191392,-9.339479,6.555745,9.976447,3.487788,-3.555703,-0.497438],[2.998906,1.569772,-0.124840,-1.512512,-3.517202,-1.690473,2.009141,9.924704],[-3.107615,9.567331,8.171112,-3.000150,-5.943306,-8.976404,-1.021407,0.932272],[8.928402,-7.903890,6.699890,3.053276,9.060486,-7.903065,-7.014257,-9.457002],[-1.510409,1.091613,-6.821894,5.676864,-8.195064,2.643251,-2.897497,-9.237833],[-9.403565,1.442175,7.915767,8.061962,-9.226743,1.489269,6.922381,4.990416],[4.048231,0.332397,-1.725389,-2.316568,-4.250911,-9.237286,4.209661,9.736397],[5.937549,2.231879,3.392038,7.114918,3.097603,3.144332,4.113753,-9.072433],[2.544844,-7.132539,-3.529596,-7.724360,4.931694,-6.083386,2.341158,-9.337600],[-9.396752,2.453599,-4.435156,-9.426977,2.011420,-1.330581,-4.601512,-7.928528],[-7.655204,-8.019501,6.336429,-5.143265,2.264194,5.342274,-1.756380,4.095132],[-2.602361,-0.301509,-9.817512,-3.257053,-0.976792,-3.176879,4.028830,3.291810],[3.819947,9.711263,-4.409676,2.736174,-3.815205,7.637858,-3.246750,4.131653],[0.705557,8.443687,-0.783683,-6.944503,-1.972421,-9.369583,7.634293,-2.837939],[6.117002,4.829113,2.220665,3.748062,-0.768109,-2.277808,6.305723,7.203521],[6.932286,-1.976688,-7.403136,6.582896,8.119803,-7.473992,5.954798,-8.353483],[-1.318957,-8.088222,-8.037320,2.113047,-2.666148,-9.808095,-5.673609,7.788721],[-5.340564,1.720062,-6.995921,-5.626079,-5.134933,-1.439561,5.092694,-0.276679],[-3.372896,4.398351,-3.083447,7.051337,-5.480211,6.715160,9.270839,-4.989258],[-8.738415,-1.344049,-5.003596,0.816751,-8.378296,-1.472039,-3.604540,8.233945],[-3.007825,0.900428,-5.430499,7.683864,-1.651239,9.270156,8.108168,-9.261428],[6.836403,-7.288933,7.632561,8.521108,3.004904,9.704298,-9.357847,8.922291]], dtype = "float32")#candidate|2894|(32, 8)|const|float32
call_2893 = relay.TupleGetItem(func_2776_call(relay.reshape(const_2894.astype('float32'), [16, 16])), 2)
call_2895 = relay.TupleGetItem(func_2779_call(relay.reshape(const_2894.astype('float32'), [16, 16])), 2)
output = relay.Tuple([bop_2889,call_2893,const_2894,])
output2 = relay.Tuple([bop_2892,call_2895,const_2894,])
func_2896 = relay.Function([], output)
mod['func_2896'] = func_2896
mod = relay.transform.InferType()(mod)
output = func_2896()
func_2897 = relay.Function([], output)
mutated_mod['func_2897'] = func_2897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2545_call = mutated_mod.get_global_var('func_2545')
call_2921 = relay.TupleGetItem(func_2543_call(), 0)
call_2922 = relay.TupleGetItem(func_2545_call(), 0)
uop_2924 = relay.log(call_2921.astype('float64')) # shape=(15, 9, 2)
uop_2926 = relay.log(call_2922.astype('float64')) # shape=(15, 9, 2)
func_1877_call = mod.get_global_var('func_1877')
func_1878_call = mutated_mod.get_global_var('func_1878')
call_2927 = relay.TupleGetItem(func_1877_call(), 1)
call_2928 = relay.TupleGetItem(func_1878_call(), 1)
output = relay.Tuple([uop_2924,call_2927,])
output2 = relay.Tuple([uop_2926,call_2928,])
func_2938 = relay.Function([], output)
mod['func_2938'] = func_2938
mod = relay.transform.InferType()(mod)
mutated_mod['func_2938'] = func_2938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2938_call = mutated_mod.get_global_var('func_2938')
call_2939 = func_2938_call()
output = call_2939
func_2940 = relay.Function([], output)
mutated_mod['func_2940'] = func_2940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2255_call = mod.get_global_var('func_2255')
func_2257_call = mutated_mod.get_global_var('func_2257')
call_2946 = func_2255_call()
call_2947 = func_2255_call()
output = call_2946
output2 = call_2947
func_2972 = relay.Function([], output)
mod['func_2972'] = func_2972
mod = relay.transform.InferType()(mod)
output = func_2972()
func_2973 = relay.Function([], output)
mutated_mod['func_2973'] = func_2973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2545_call = mutated_mod.get_global_var('func_2545')
call_3010 = relay.TupleGetItem(func_2543_call(), 0)
call_3011 = relay.TupleGetItem(func_2545_call(), 0)
func_787_call = mod.get_global_var('func_787')
func_790_call = mutated_mod.get_global_var('func_790')
const_3041 = relay.const([-7.314001,1.922360,-1.992838,9.735356,-3.129113,-3.913947,5.108544,4.561173,-4.840404,-1.895773,0.513001,-9.957349,-4.592152,6.694912,-7.860968,2.381260,9.531556,-1.741335,-8.433011,-7.205357,-7.074136,-9.036035,-5.826484,-0.386400,-7.554290,-9.989780,-5.161876,-1.780676,-8.147702,-5.126431,0.843946,0.162867,4.932260,-1.076830,-6.798305,-0.763253,1.735877,-9.002183,-1.520724,2.513969,7.379454,-8.404775,-4.099591,6.274201,-8.353330,5.982497,1.718852,9.083707,-8.401464,-7.712294,-1.497102,3.028653,3.012295,-5.651435,3.637995,-7.496875,6.173465,-4.688047,5.420197,-9.306489,5.284232,2.902109,1.454746,8.501495,-0.517625,-5.853453,-9.014348,5.662562,3.891385,2.193015,9.887980,7.561881,-1.070040,-7.493246,2.783677,-3.636807,-1.482528,0.090836,-2.900564,-0.519246,6.191101,7.202406,-2.907197,0.451522,-2.905926,-0.784868,0.709470,1.095465,3.675102,0.377065,-4.162163,-6.620694,-3.973155,-8.390567,-8.280743,6.241084,9.358082,-3.842109,5.229388,4.000975,-7.755375,0.422161,-8.405937,-1.647471,-6.952143,-9.219145,3.866467,-8.719967,5.599996,-0.992391,3.661956,8.918538,-3.840985,-6.595895,3.618661,-2.628421,-9.785790,2.335840,-3.011267,-2.713947,-0.473538,1.044899,3.822167,6.725093,7.770512,8.726583,0.610812,4.835190,-8.341596,-8.553299,-8.818668,3.114134,-9.105926,5.680268,-2.798765,-0.182292,-3.724956,-8.496343,8.071830,-6.310101,1.999998,8.537110,-5.504313,6.169436,-2.779827,1.364579,-8.363587,8.263364,3.391754,3.716253,3.585273,-5.595390,0.381005,4.013493,-7.981212,5.737376,2.385531,6.416462,-3.365840,-1.793275,-8.391801,2.250883,1.927521,1.145212,9.262578,-5.642445,-0.295099,-9.152890,-0.902093,-8.046479,-1.404078,-4.546277,-0.565459,3.159443,-5.021230,-7.399044,2.247099,8.445858,-0.483403,-1.581919,2.147109,-4.061232,5.840347,-2.958874,6.827287,5.415557,-6.573603,8.033871,6.274314,6.701780,6.672088,-7.133076,3.643045,9.436461,-7.087779,5.374608,-6.350812,-2.961842,1.805645,0.904378,4.137470,-7.678223,6.589701,3.785155,-4.801680,-1.354657,-1.005376,2.178574,4.655131,7.781100,-0.273904,6.466728,2.248241,-5.664225,-2.481473,7.990010,-4.804534,-2.665162,7.104519,-8.933747,-5.794212,3.783556,9.159599,5.595799,1.542837,2.257443,3.711160,8.941695,-0.796587,9.687870,0.066173,-5.994030,-9.414855,0.356927,-8.972431,-6.074822,7.518759,5.047129,-7.541158,9.782665,-0.724952,1.742343,7.250578,-4.195471,-8.956201,6.835054,-0.306293,-6.774351,-4.047008,-4.112218,7.291862,4.003697,9.025960,-8.727541,5.154626,7.866124,-4.693767,-3.428616,2.261328,5.586265,-0.759966,-9.441625,-5.174696,-6.868102,-1.969879,-9.079183,8.850280,-5.193833,-1.571834,-6.815645,-9.733825,5.593276,-6.467595,7.545885,-5.741419,8.389204,5.645144,2.440195,-6.571204,-9.069744,6.581559,5.344311,-8.951140,0.633366,-9.125469,4.626211,5.068592,7.553991,-3.053961,-0.945900,6.721477,7.955752,2.432969,-6.917639,-9.334509,-1.283336,6.982350,-9.399874,-8.577195,2.172380,1.691316,2.610276,9.102055,-8.023845,7.862588,9.044991,5.456650,4.075157,8.020186,-3.736889,-5.925765,2.875509,-8.698203,-5.507296,0.671455,7.203474,-2.182984,-1.258200,9.874534,9.176548,8.043756,6.096607,6.653467,0.521574,5.753740,2.433947,-9.929334,4.335880,-4.320991,0.487237,5.465883,4.216928,-0.053297,-6.648704,-9.287477,-0.085172,-6.349820,-0.518395,4.520586,-4.101116,-2.170251,-5.885061,2.870855,6.576686,3.508137,0.253467,-8.833351,-8.914120,-9.139153,-0.211270,-0.527518,-5.662229,1.334181,3.808964,-4.630209,1.270358,9.046368,-6.076186,2.278182,-0.434265,-6.834691,-7.991195,-1.507793,5.590909,9.387956,-9.913779,4.397889,-8.250702,4.242807,9.768664,5.426059,-0.135954,-6.733371,7.477720,0.990859,4.102667,-9.030108,-5.430088,-7.223627,4.124576,5.571839,-1.686053,4.083261,9.278153,-2.724822,-3.634270,2.774197,-2.769850,0.216187,-3.198104,4.547539,0.901643], dtype = "float32")#candidate|3041|(392,)|const|float32
call_3040 = relay.TupleGetItem(func_787_call(relay.reshape(const_3041.astype('float32'), [14, 2, 14])), 1)
call_3042 = relay.TupleGetItem(func_790_call(relay.reshape(const_3041.astype('float32'), [14, 2, 14])), 1)
func_1701_call = mod.get_global_var('func_1701')
func_1704_call = mutated_mod.get_global_var('func_1704')
var_3046 = relay.var("var_3046", dtype = "float32", shape = (32, 8))#candidate|3046|(32, 8)|var|float32
const_3047 = relay.const([6.322926,-0.708749,-1.775023,-3.473021,5.737183,0.798423,6.397176,-1.551520,6.724109,7.725801,9.397089,-1.740042,5.498953,-2.879994,3.894114,-8.439745,-1.453092,-7.559277,7.862575,-1.749378,7.738770,-8.325019,6.821222,3.215687,-6.214566,-7.559738,-1.655272,0.130800,8.519820,-7.493312,-9.335524,0.761537,-9.788371,3.638494,2.547289,-7.035755,1.608765,2.475750,8.618202,-7.368819,-5.463192,5.543895,8.632314,-0.602489,-5.280483,4.248198,0.784392,-0.173035,-2.569971,-6.492167,1.954363,-2.958729,4.752322,0.239333,-3.215397,-6.294672,1.899732,-3.670131,-8.045198,2.152212,5.001763,9.433435,-3.509485,-4.079259,6.618065,-1.310748,-2.339223,-6.988249,-6.055644,-8.633315,1.167721,6.868524,7.683621,1.729387,-4.406971,-1.189284,-9.446958,1.991946,7.951629,4.410414,-3.179422,0.542494,3.452349,-9.918798,-6.068003,-9.929630,1.611203,-2.274803,9.434890,-2.949885,-7.228571,-9.881183,0.495983,5.083543,3.311645,9.613336,-1.592153,-5.271659,-3.501934,-0.515156,-3.699927,-1.991519,-9.158494,-8.298348,2.253158,-9.422009,0.597578,-9.866926,-1.345477,-4.498944,-5.132879,2.461083,-0.297965,-5.441477,-4.323723,9.994523,-3.596532,-3.512965,-3.270430,-1.087157,4.429452,-6.225349,1.768508,5.034158,-1.885801,-7.103403,-5.169170,-8.793265,5.186870,8.344994,5.870542,-2.304533,8.614096,-5.075039,6.005681,9.823119,5.059161,-6.776328,-3.184673,-3.326988,4.243497,8.401492,-7.664733,-0.846175,8.238062,6.515854,7.053874,-9.501227,-8.871639,-7.895272,6.135480,7.337903,0.288921,-2.691838,8.715229,9.426858,2.836639,-7.481334,-6.874458,4.314702,6.684093,-7.721411,3.801986,2.144619,3.773314,8.761475,8.517625,-7.385678,-8.252744,-0.224803,7.507531,-1.775618,-8.383153,8.246117,-8.259868,-5.658312,9.394843,-3.632811,2.662668,3.617149,5.004331,-4.935510,1.255411,-1.145373,2.810208,5.411391,-6.619303,8.961523,9.862029,6.386592,7.943305,4.051975,-6.043732,0.133972,2.453789,-3.518146,-0.579853,4.477276,5.202555,4.291221,-8.687984,-4.900228,5.666759,6.534720,-4.810239,-8.549783,9.144476,-4.171378,9.915875,4.961759,-7.653596,7.955903,-4.869662,-3.114539,-5.021848,-9.584740,0.089853,1.327744,-2.342785,1.356951,1.550746,3.738389,0.590764,-7.382997,3.733154,9.006674,-5.186791,-1.596575,0.671972,-8.609122,1.655092,-7.621707,8.327411,9.855309,-5.082691,-3.774045,-8.515029,-3.477947,-5.736988,-6.723212,8.808723,9.861072,-2.713696,-2.307723,1.107023,-3.631906,-7.523419,8.219012,-1.581085,2.612444,0.609659,1.174366,3.949786,4.094805,-4.144496,-5.949941,7.989274,6.179191,1.402000,5.166548,1.156146,1.082069,-6.054560,3.994137,8.161898,4.058956,0.208974,-6.979081,5.336881,-7.057562,4.281936,2.291527,-4.630322,2.911265,-9.817985,-1.587665,-1.080303,8.683907,-6.166971,1.453219,-0.494734,-0.925000,9.140599,-4.551690,-2.164551,5.449758,2.498696,-2.428495,9.243685,-9.390619,-9.225475,2.523036,-7.828058,4.696970,-3.118598,7.963702,-3.375678,-6.678493,-0.183924,-3.060256,5.553559,2.638454,-9.049335,-0.950376,2.021613,2.849607,-3.643696,-0.609496,-6.060808,7.830602,-4.172805,2.122310,7.615575,8.736823,-5.756270,-2.155633,8.997078,1.170588,-4.394828,0.592038,-6.343020,4.752183,-9.709767,1.141218], dtype = "float32")#candidate|3047|(324,)|const|float32
call_3045 = relay.TupleGetItem(func_1701_call(relay.reshape(var_3046.astype('float32'), [16, 4, 4]), relay.reshape(const_3047.astype('float32'), [54, 6]), ), 1)
call_3048 = relay.TupleGetItem(func_1704_call(relay.reshape(var_3046.astype('float32'), [16, 4, 4]), relay.reshape(const_3047.astype('float32'), [54, 6]), ), 1)
output = relay.Tuple([call_3010,call_3040,const_3041,call_3045,var_3046,const_3047,])
output2 = relay.Tuple([call_3011,call_3042,const_3041,call_3048,var_3046,const_3047,])
func_3053 = relay.Function([var_3046,], output)
mod['func_3053'] = func_3053
mod = relay.transform.InferType()(mod)
var_3054 = relay.var("var_3054", dtype = "float32", shape = (32, 8))#candidate|3054|(32, 8)|var|float32
output = func_3053(var_3054)
func_3055 = relay.Function([var_3054], output)
mutated_mod['func_3055'] = func_3055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1392_call = mod.get_global_var('func_1392')
func_1393_call = mutated_mod.get_global_var('func_1393')
call_3128 = relay.TupleGetItem(func_1392_call(), 2)
call_3129 = relay.TupleGetItem(func_1393_call(), 2)
output = relay.Tuple([call_3128,])
output2 = relay.Tuple([call_3129,])
func_3136 = relay.Function([], output)
mod['func_3136'] = func_3136
mod = relay.transform.InferType()(mod)
mutated_mod['func_3136'] = func_3136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3136_call = mutated_mod.get_global_var('func_3136')
call_3137 = func_3136_call()
output = call_3137
func_3138 = relay.Function([], output)
mutated_mod['func_3138'] = func_3138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_3139 = relay.TupleGetItem(func_888_call(), 0)
call_3140 = relay.TupleGetItem(func_889_call(), 0)
func_1319_call = mod.get_global_var('func_1319')
func_1323_call = mutated_mod.get_global_var('func_1323')
var_3150 = relay.var("var_3150", dtype = "float32", shape = (324,))#candidate|3150|(324,)|var|float32
call_3149 = relay.TupleGetItem(func_1319_call(relay.reshape(var_3150.astype('float32'), [12, 3, 9]), relay.reshape(var_3150.astype('float32'), [12, 3, 9]), ), 0)
call_3151 = relay.TupleGetItem(func_1323_call(relay.reshape(var_3150.astype('float32'), [12, 3, 9]), relay.reshape(var_3150.astype('float32'), [12, 3, 9]), ), 0)
uop_3154 = relay.log(call_3149.astype('float64')) # shape=(12, 3, 9)
uop_3156 = relay.log(call_3151.astype('float64')) # shape=(12, 3, 9)
func_2153_call = mod.get_global_var('func_2153')
func_2156_call = mutated_mod.get_global_var('func_2156')
var_3161 = relay.var("var_3161", dtype = "uint32", shape = ())#candidate|3161|()|var|uint32
const_3162 = relay.const([-10,7,5,6,3,3,-7,-4,-8,-5,-2,9,9,1,8,4,-6,-1,7,1,3,6,2,8,-4,-3,6,-10,-7,-5,-4,5,9,8,-3,4,2,-8,3,-4,-3,-1,-10,-1,1,-4,-4,4,-4,7,-1,7,-2,-10,3,10,-3,-2,-2,-2,1,-8,4,8,4,7,-6,-9,-7,5,-2,-7,-8,8,4,-2,5,-1,2,6,3,-1,6,-1,-10,-5,1,-9,-1,-8,-8,-1,2,1,9,2,-9,-5,5,-9,10,1,-6,-8,-9,3,9,-8,3,-7,-7,6,-1,10,-5,-5,3,-6,-6,5,3,1,-1,2,-10,-8,-7,-10,5,8,-9,7,-9,-10,-9,10,-4,-5,10,10,-6,5,-3,6,9,8,-7,9,-7,-2,-5,-8,1,-3,-1,-3,1,4,6,-2,4,-10,-4,-10,9,9,4,2,-1,8,-10,-2,-8,-7,-6,9,8,4,10,4,6,3,3,5,2,9,-4,-5,7,9,10,3,7,1,-1,-5,10,-5,3,8,-3,9,6,-2,-7,-6,8,4,-9,3,10,7,5,-5,-3,-6,-8,8,1,8,-2,5,-6,-5,6,6,-7,-7,6,3,-5,-10,5,8,7,-4,-10,8,1,-10,-3,-2,9,5,1,7,-8,-8,4,-9,-2,9,-3,8,4,1], dtype = "uint32")#candidate|3162|(256,)|const|uint32
call_3160 = relay.TupleGetItem(func_2153_call(relay.reshape(var_3161.astype('uint32'), []), relay.reshape(const_3162.astype('uint32'), [256,]), ), 2)
call_3163 = relay.TupleGetItem(func_2156_call(relay.reshape(var_3161.astype('uint32'), []), relay.reshape(const_3162.astype('uint32'), [256,]), ), 2)
output = relay.Tuple([call_3139,var_3150,uop_3154,call_3160,var_3161,const_3162,])
output2 = relay.Tuple([call_3140,var_3150,uop_3156,call_3163,var_3161,const_3162,])
func_3166 = relay.Function([var_3150,var_3161,], output)
mod['func_3166'] = func_3166
mod = relay.transform.InferType()(mod)
mutated_mod['func_3166'] = func_3166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3166_call = mutated_mod.get_global_var('func_3166')
var_3168 = relay.var("var_3168", dtype = "float32", shape = (324,))#candidate|3168|(324,)|var|float32
var_3169 = relay.var("var_3169", dtype = "uint32", shape = ())#candidate|3169|()|var|uint32
call_3167 = func_3166_call(var_3168,var_3169,)
output = call_3167
func_3170 = relay.Function([var_3168,var_3169,], output)
mutated_mod['func_3170'] = func_3170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3275 = relay.TupleGetItem(func_2536_call(), 3)
call_3276 = relay.TupleGetItem(func_2537_call(), 3)
output = relay.Tuple([call_3275,])
output2 = relay.Tuple([call_3276,])
func_3316 = relay.Function([], output)
mod['func_3316'] = func_3316
mod = relay.transform.InferType()(mod)
mutated_mod['func_3316'] = func_3316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3316_call = mutated_mod.get_global_var('func_3316')
call_3317 = func_3316_call()
output = call_3317
func_3318 = relay.Function([], output)
mutated_mod['func_3318'] = func_3318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_3322 = func_2031_call()
call_3323 = func_2031_call()
func_3053_call = mod.get_global_var('func_3053')
func_3055_call = mutated_mod.get_global_var('func_3055')
var_3325 = relay.var("var_3325", dtype = "float32", shape = (64, 4))#candidate|3325|(64, 4)|var|float32
call_3324 = relay.TupleGetItem(func_3053_call(relay.reshape(var_3325.astype('float32'), [32, 8])), 5)
call_3326 = relay.TupleGetItem(func_3055_call(relay.reshape(var_3325.astype('float32'), [32, 8])), 5)
func_2595_call = mod.get_global_var('func_2595')
func_2597_call = mutated_mod.get_global_var('func_2597')
var_3336 = relay.var("var_3336", dtype = "float32", shape = (540,))#candidate|3336|(540,)|var|float32
call_3335 = relay.TupleGetItem(func_2595_call(relay.reshape(var_3336.astype('float32'), [540,])), 0)
call_3337 = relay.TupleGetItem(func_2597_call(relay.reshape(var_3336.astype('float32'), [540,])), 0)
output = relay.Tuple([call_3322,call_3324,var_3325,call_3335,var_3336,])
output2 = relay.Tuple([call_3323,call_3326,var_3325,call_3337,var_3336,])
func_3344 = relay.Function([var_3325,var_3336,], output)
mod['func_3344'] = func_3344
mod = relay.transform.InferType()(mod)
mutated_mod['func_3344'] = func_3344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3344_call = mutated_mod.get_global_var('func_3344')
var_3346 = relay.var("var_3346", dtype = "float32", shape = (64, 4))#candidate|3346|(64, 4)|var|float32
var_3347 = relay.var("var_3347", dtype = "float32", shape = (540,))#candidate|3347|(540,)|var|float32
call_3345 = func_3344_call(var_3346,var_3347,)
output = call_3345
func_3348 = relay.Function([var_3346,var_3347,], output)
mutated_mod['func_3348'] = func_3348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_3350 = relay.TupleGetItem(func_848_call(), 0)
call_3351 = relay.TupleGetItem(func_849_call(), 0)
output = call_3350
output2 = call_3351
func_3365 = relay.Function([], output)
mod['func_3365'] = func_3365
mod = relay.transform.InferType()(mod)
mutated_mod['func_3365'] = func_3365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3365_call = mutated_mod.get_global_var('func_3365')
call_3366 = func_3365_call()
output = call_3366
func_3367 = relay.Function([], output)
mutated_mod['func_3367'] = func_3367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_3383 = relay.TupleGetItem(func_3136_call(), 0)
call_3384 = relay.TupleGetItem(func_3138_call(), 0)
func_2264_call = mod.get_global_var('func_2264')
func_2265_call = mutated_mod.get_global_var('func_2265')
call_3385 = relay.TupleGetItem(func_2264_call(), 0)
call_3386 = relay.TupleGetItem(func_2265_call(), 0)
var_3398 = relay.var("var_3398", dtype = "float32", shape = (2, 324))#candidate|3398|(2, 324)|var|float32
bop_3399 = relay.multiply(call_3383.astype('int16'), var_3398.astype('int16')) # shape=(2, 324)
bop_3402 = relay.multiply(call_3384.astype('int16'), var_3398.astype('int16')) # shape=(2, 324)
output = relay.Tuple([call_3385,bop_3399,])
output2 = relay.Tuple([call_3386,bop_3402,])
func_3403 = relay.Function([var_3398,], output)
mod['func_3403'] = func_3403
mod = relay.transform.InferType()(mod)
var_3404 = relay.var("var_3404", dtype = "float32", shape = (2, 324))#candidate|3404|(2, 324)|var|float32
output = func_3403(var_3404)
func_3405 = relay.Function([var_3404], output)
mutated_mod['func_3405'] = func_3405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3412 = relay.var("var_3412", dtype = "int64", shape = (11, 4, 15))#candidate|3412|(11, 4, 15)|var|int64
var_3413 = relay.var("var_3413", dtype = "int64", shape = (11, 4, 15))#candidate|3413|(11, 4, 15)|var|int64
bop_3414 = relay.greater_equal(var_3412.astype('bool'), relay.reshape(var_3413.astype('bool'), relay.shape_of(var_3412))) # shape=(11, 4, 15)
func_787_call = mod.get_global_var('func_787')
func_790_call = mutated_mod.get_global_var('func_790')
const_3421 = relay.const([[8.639270,0.209022],[2.940197,6.913327],[-9.264191,4.742908],[-4.818067,-5.797029],[-7.408954,-2.918300],[5.912003,-9.295622],[0.086556,5.642320],[-2.224196,-2.406824],[-8.148033,-9.152243],[5.397403,-6.241216],[-2.658212,7.635190],[9.900285,2.595222],[-3.175695,-3.228678],[-9.966871,5.061989],[-3.783836,-5.253292],[9.751701,-3.619854],[-3.586326,8.050114],[-5.858256,0.157599],[4.280788,-4.358623],[5.485819,-6.348507],[9.164209,0.623671],[9.352208,-1.806918],[5.487974,-8.219700],[3.111443,2.894682],[-9.799718,-3.461952],[-3.414882,4.259547],[-8.899416,-6.536785],[1.238344,0.989151],[8.721648,-2.293074],[2.713873,-6.556912],[9.374212,6.806399],[2.309809,-0.193953],[3.306161,6.469232],[8.007733,8.704730],[-6.244322,4.059229],[-9.793839,-8.423196],[9.909028,-9.084828],[2.265206,-8.548339],[-5.253583,-3.024326],[-3.589837,6.863367],[7.619799,2.422602],[4.859696,-1.825520],[-3.029925,0.540643],[9.382380,-9.144578],[-9.209590,2.017391],[1.032599,2.996776],[-3.284771,6.138567],[-4.017481,-4.635563],[7.367487,-4.483066],[3.219440,-3.249643],[-0.239686,-8.702322],[-9.345770,5.201366],[-5.005500,-1.144600],[-2.517332,5.457634],[2.620088,4.528243],[4.644291,8.024649],[3.031778,5.157411],[1.092183,-3.048725],[2.984625,7.862897],[0.255275,-3.928081],[4.997898,0.563104],[-3.492666,-9.971296],[3.261263,-2.657797],[-9.564972,-7.108923],[6.136508,-2.938895],[2.808478,3.522641],[4.641545,-6.022259],[4.786460,-0.511868],[-6.214171,-5.587161],[-4.940682,-1.253475],[-2.609201,-5.920992],[1.589370,-9.308568],[-4.360085,7.807825],[3.454368,-2.575429],[3.237802,7.343027],[-2.968617,0.680958],[7.526605,4.257017],[7.808644,1.279991],[-8.923256,-3.753851],[-7.777326,5.043214],[8.593236,1.408264],[5.813853,2.311241],[-1.660711,5.670722],[3.099159,9.199540],[-2.853102,-5.251791],[0.674556,8.407930],[-8.380450,4.803951],[-4.123089,8.870706],[4.688728,-6.736964],[6.785621,6.469113],[-9.687822,-2.249290],[3.914145,-2.350262],[-4.692893,0.050411],[-1.436123,-2.025561],[-1.002314,-0.054079],[-6.796816,-7.164059],[-4.650358,-9.904379],[0.289200,7.612344],[-7.335427,8.472452],[-1.820762,6.050555],[-1.351153,-6.492324],[7.518094,3.799866],[-0.883222,-2.603977],[-1.954710,-7.839472],[8.681005,-8.150841],[-1.388021,-4.717707],[6.269986,-9.194842],[4.897456,-5.770397],[0.500608,-4.612496],[4.355437,-0.329907],[7.799649,-0.935125],[-7.395279,-7.309808],[8.676185,-9.015322],[1.988155,-4.817353],[-4.702442,-5.251318],[-0.845623,6.553759],[6.610749,-8.194142],[-7.209639,-3.703837],[8.601674,6.429627],[7.094801,4.127458],[-0.037141,-7.467548],[-6.925649,-3.274095],[4.099333,-8.415294],[2.220140,0.289663],[-2.505159,-7.052592],[4.289188,-2.312528],[5.589399,-3.296779],[-3.282808,-9.945475],[5.062758,-7.640296],[5.686135,-8.139568],[6.704422,5.114785],[-2.420323,6.643808],[-8.479577,8.233333],[-5.247867,4.667358],[3.125399,-4.120282],[7.532240,-6.653722],[7.586736,0.591238],[8.882347,8.060786],[-2.302806,-9.528586],[-7.232997,1.222559],[8.534670,-7.600801],[2.658065,8.359610],[8.236466,-5.545713],[-7.190225,9.814490],[5.617458,5.534277],[-6.131285,7.216620],[9.789215,6.238821],[9.766334,-4.086786],[-4.054058,-4.905684],[-1.842651,-7.172239],[4.266076,3.861550],[-6.949999,5.399604],[4.896774,-8.190977],[5.470559,-8.995214],[4.791650,-4.957407],[5.564121,2.731026],[9.218503,5.215613],[-8.158263,5.487224],[-5.734603,8.923619],[4.030732,-4.670076],[7.270102,-6.730266],[-9.045609,1.250148],[7.581189,-4.660743],[6.900803,-3.937845],[3.445684,-4.324862],[6.363119,0.428347],[-8.501540,-5.819499],[9.603264,-8.321623],[-2.300435,3.675637],[-7.012903,-7.629299],[3.194553,-8.980454],[6.232957,0.887619],[-2.333311,-4.098555],[-7.066690,3.576669],[-4.026530,-1.895302],[-7.986112,8.427380],[-3.457227,6.618195],[5.284036,-5.680807],[-0.808664,2.659637],[3.178092,-7.993271],[4.861033,2.382952],[-0.661361,-0.268368],[3.628619,-9.166965],[-1.106875,-3.050880],[-9.646125,5.372370],[2.750807,-1.719311],[-8.130206,7.051555],[0.137863,3.936051],[-1.692770,-0.805801],[1.810073,-6.748442],[6.191082,-0.354441],[-8.925395,-8.549513],[-0.592604,-9.391183],[9.771956,7.597251],[1.370001,2.612614],[-6.095894,2.611805]], dtype = "float32")#candidate|3421|(196, 2)|const|float32
call_3420 = relay.TupleGetItem(func_787_call(relay.reshape(const_3421.astype('float32'), [14, 2, 14])), 1)
call_3422 = relay.TupleGetItem(func_790_call(relay.reshape(const_3421.astype('float32'), [14, 2, 14])), 1)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3427 = relay.TupleGetItem(func_2536_call(), 1)
call_3428 = relay.TupleGetItem(func_2537_call(), 1)
var_3453 = relay.var("var_3453", dtype = "float32", shape = (196, 2))#candidate|3453|(196, 2)|var|float32
bop_3454 = relay.power(const_3421.astype('float64'), relay.reshape(var_3453.astype('float64'), relay.shape_of(const_3421))) # shape=(196, 2)
func_3344_call = mod.get_global_var('func_3344')
func_3348_call = mutated_mod.get_global_var('func_3348')
var_3464 = relay.var("var_3464", dtype = "float32", shape = (1, 540))#candidate|3464|(1, 540)|var|float32
call_3463 = relay.TupleGetItem(func_3344_call(relay.reshape(call_3427.astype('float32'), [64, 4]), relay.reshape(var_3464.astype('float32'), [540,]), ), 1)
call_3465 = relay.TupleGetItem(func_3348_call(relay.reshape(call_3427.astype('float32'), [64, 4]), relay.reshape(var_3464.astype('float32'), [540,]), ), 1)
output = relay.Tuple([bop_3414,call_3420,call_3427,bop_3454,call_3463,var_3464,])
output2 = relay.Tuple([bop_3414,call_3422,call_3428,bop_3454,call_3465,var_3464,])
func_3466 = relay.Function([var_3412,var_3413,var_3453,var_3464,], output)
mod['func_3466'] = func_3466
mod = relay.transform.InferType()(mod)
mutated_mod['func_3466'] = func_3466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3466_call = mutated_mod.get_global_var('func_3466')
var_3468 = relay.var("var_3468", dtype = "int64", shape = (11, 4, 15))#candidate|3468|(11, 4, 15)|var|int64
var_3469 = relay.var("var_3469", dtype = "int64", shape = (11, 4, 15))#candidate|3469|(11, 4, 15)|var|int64
var_3470 = relay.var("var_3470", dtype = "float32", shape = (196, 2))#candidate|3470|(196, 2)|var|float32
var_3471 = relay.var("var_3471", dtype = "float32", shape = (1, 540))#candidate|3471|(1, 540)|var|float32
call_3467 = func_3466_call(var_3468,var_3469,var_3470,var_3471,)
output = call_3467
func_3472 = relay.Function([var_3468,var_3469,var_3470,var_3471,], output)
mutated_mod['func_3472'] = func_3472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_814_call = mutated_mod.get_global_var('func_814')
call_3506 = func_813_call()
call_3507 = func_813_call()
var_3510 = relay.var("var_3510", dtype = "float32", shape = (9, 1, 15))#candidate|3510|(9, 1, 15)|var|float32
bop_3511 = relay.floor_mod(call_3506.astype('float64'), relay.reshape(var_3510.astype('float64'), relay.shape_of(call_3506))) # shape=(9, 1, 15)
bop_3514 = relay.floor_mod(call_3507.astype('float64'), relay.reshape(var_3510.astype('float64'), relay.shape_of(call_3507))) # shape=(9, 1, 15)
func_813_call = mod.get_global_var('func_813')
func_814_call = mutated_mod.get_global_var('func_814')
call_3520 = func_813_call()
call_3521 = func_813_call()
func_2094_call = mod.get_global_var('func_2094')
func_2097_call = mutated_mod.get_global_var('func_2097')
var_3532 = relay.var("var_3532", dtype = "float32", shape = (405,))#candidate|3532|(405,)|var|float32
call_3531 = relay.TupleGetItem(func_2094_call(relay.reshape(var_3532.astype('float32'), [405,])), 2)
call_3533 = relay.TupleGetItem(func_2097_call(relay.reshape(var_3532.astype('float32'), [405,])), 2)
func_3466_call = mod.get_global_var('func_3466')
func_3472_call = mutated_mod.get_global_var('func_3472')
var_3550 = relay.var("var_3550", dtype = "int64", shape = (660,))#candidate|3550|(660,)|var|int64
var_3551 = relay.var("var_3551", dtype = "float32", shape = (392,))#candidate|3551|(392,)|var|float32
const_3552 = relay.const([[2.066986,9.194217,2.762363,-8.661248,-5.307621,-5.596393,-4.625455,-6.924693,0.294781,-3.318924,-2.720230,9.905620,-3.561241,-4.878617,-1.330550,-2.374384,2.858157,7.617227,3.027217,-9.602788,-8.669305,1.450390,-0.290291,9.617542,-3.480098,0.455770,-9.948216,9.242787,-1.070802,-1.940073,-1.517000,-4.501959,-3.640468,-1.583764,8.752858,-6.718021,-8.365648,-4.269515,3.346173,-2.905108,8.899908,-7.452230,-9.204747,9.955845,9.058527,-9.461425,-8.192506,-6.416291,-4.034944,-2.529925,1.429378,6.325212,8.868495,9.100702,-4.253646,-4.831859,5.693307,2.303710,-9.704916,-4.976925],[-2.937009,3.712446,8.195851,-7.698445,-5.883662,9.290038,2.783201,5.361255,4.798455,6.006384,0.660968,1.962547,-0.439754,-6.482377,5.402640,7.408897,8.636535,0.029382,-1.065550,-2.457770,-2.974764,-5.994399,6.945795,-9.230606,-5.343083,-4.581602,4.529286,6.408346,-0.483308,-2.022893,-0.093436,-2.702003,-6.473872,6.498706,6.026377,-8.139081,4.172178,9.685118,-7.553598,7.385750,8.237607,-8.869279,-4.682501,-0.279604,-7.054597,-9.446545,-8.838685,-0.546878,-3.427613,7.907127,-7.911488,-4.206772,1.589564,-6.741838,9.757268,-2.311302,6.884568,-9.634323,-3.277250,-3.365738],[3.502934,-7.402280,0.443286,6.967178,-1.727219,1.271202,-9.669268,-9.989274,9.926272,6.758880,3.640683,8.073840,1.298256,-1.906034,0.061507,-7.860541,8.383372,-3.096991,7.675031,9.350281,2.952821,-9.354427,-4.783893,4.055336,4.886698,-1.432060,-9.880931,3.394528,0.304843,-5.742748,1.357311,-7.095748,1.456068,0.797971,-0.915582,-6.079822,-8.875985,6.736882,4.533657,-7.928584,6.771901,6.339684,8.389686,1.871756,-8.542345,6.083564,-3.135767,9.502696,-3.109568,5.100253,4.437059,-1.825292,-6.127703,-8.323619,-5.742972,3.852891,5.417617,-8.182318,8.646889,-2.773054],[7.535571,0.580349,3.998477,7.298570,-1.362562,-1.654217,-5.236692,6.548349,-6.375589,-8.798763,-3.815825,-7.290801,2.848235,-6.977284,0.140942,-1.182332,-8.454447,-5.124396,-7.215489,-5.313141,-7.607269,-4.558691,6.537985,-4.951491,2.045554,9.783042,-6.200043,-6.331415,-4.178013,-4.540129,9.932222,-1.748695,9.026887,7.216550,-5.708376,-0.554644,-9.051431,8.865678,-4.371643,0.044457,-5.035361,5.845867,-5.331370,-5.619929,3.434670,-9.871373,-0.815637,-6.955869,-6.054864,9.085584,0.695511,2.740372,6.525396,-4.771600,-7.023746,6.604872,-7.192987,7.740621,-1.936178,4.113820],[2.501674,-6.785581,-7.772349,7.618596,-4.101000,0.187581,-1.671359,0.239485,4.279255,8.197491,9.250364,-0.818507,7.711976,7.902399,-9.303143,3.166269,-5.730893,6.297803,5.851139,4.151246,1.525234,1.638339,-7.033232,5.143595,-0.377073,4.628995,-8.703532,3.097900,-3.750533,8.660551,0.896298,-1.682643,4.528863,-2.950288,-1.264334,-7.652204,-7.847854,0.381931,5.049617,-9.157253,9.846788,2.905957,-9.038353,8.511835,9.873385,5.205196,-9.898851,5.621826,3.128921,-4.970945,5.407565,3.938101,-2.153263,-0.197481,-1.160618,-1.536190,4.996435,8.266679,-6.083301,-6.674179],[1.942545,8.245315,7.480665,9.320288,-4.561864,-7.775711,7.163998,-9.631144,-6.890984,1.054477,0.836182,-0.435612,9.945632,-0.698794,-5.796242,-3.705332,-5.643772,8.460008,-1.850630,-3.065808,-3.374992,-0.757205,2.159258,-8.220297,-0.712877,-2.292560,2.103442,-2.868438,-9.522841,-8.134024,7.504971,-2.417062,-9.799767,6.140725,6.197658,-1.424098,-2.403080,3.916742,8.285695,2.259607,7.382730,7.186760,-8.490112,3.732767,9.070514,4.089835,-9.733432,-2.390143,-6.063137,2.705189,-2.635505,7.453876,4.855927,-8.951895,-9.465299,-7.447134,3.051415,-5.499061,1.130685,-5.782245],[-7.900435,5.528054,2.898143,9.796052,0.151434,2.331671,-5.770557,-7.277395,3.048259,-4.522922,-9.854396,6.743941,2.008734,6.302839,-1.041674,7.748200,9.427439,1.642053,-9.008172,-4.611464,-2.500234,2.043197,2.437860,-6.446067,-8.404268,-6.297020,8.115857,-1.095175,-4.150232,3.741742,4.257540,3.541195,0.110389,-4.850772,7.554787,4.619397,-0.445842,2.602712,-5.545719,1.116769,-2.027379,2.214229,1.977316,-8.591649,5.354676,-8.378321,-9.617181,7.836565,9.608319,-5.334515,1.526078,-5.769969,-2.595790,5.339994,6.065352,-1.236951,-9.993529,4.817038,0.945457,4.731372],[5.484237,-5.933507,5.279098,8.533951,5.006628,-6.096095,3.423461,-2.941289,-7.987768,-0.441095,-2.907867,4.116541,-4.725750,2.279124,2.197408,-0.711137,-7.533860,-9.421364,-0.365164,-0.109000,0.756688,-0.199245,7.993743,1.225869,-1.726204,4.523418,-5.853981,-9.695855,9.385338,-4.378523,-9.355037,8.907764,6.260349,2.826461,4.564803,9.228288,-8.994751,8.067974,9.652158,4.981530,-1.351647,-7.116928,1.238825,2.032066,-5.420260,3.198851,-6.281898,-2.283835,8.834136,-2.745433,0.269374,6.635466,9.159085,-7.517315,4.370825,4.592783,-1.954078,-3.034076,-5.251118,8.565922],[-4.636396,9.129890,4.839234,-8.257903,8.960982,-2.746364,7.236135,-9.222192,-6.793329,3.369887,-7.223861,-9.346150,-5.767399,2.727263,-8.874893,-4.567342,5.550628,-1.609505,9.235861,2.593990,1.239168,3.773092,-1.490090,4.280095,-8.089066,-9.049587,3.959853,-8.386491,-9.877673,-1.902242,-4.311926,9.590608,0.889023,-4.234216,-5.920642,1.680855,8.510601,-1.692185,6.625674,2.455139,-8.378064,-9.839211,-9.667603,-6.035731,-4.468622,4.440855,6.159494,0.162263,-2.804623,6.371301,0.108135,-0.311534,1.710351,-2.250967,0.546833,7.832223,-3.697149,0.926846,-2.302459,9.575019]], dtype = "float32")#candidate|3552|(9, 60)|const|float32
call_3549 = relay.TupleGetItem(func_3466_call(relay.reshape(var_3550.astype('int64'), [11, 4, 15]), relay.reshape(var_3550.astype('int64'), [11, 4, 15]), relay.reshape(var_3551.astype('float32'), [196, 2]), relay.reshape(const_3552.astype('float32'), [1, 540]), ), 0)
call_3553 = relay.TupleGetItem(func_3472_call(relay.reshape(var_3550.astype('int64'), [11, 4, 15]), relay.reshape(var_3550.astype('int64'), [11, 4, 15]), relay.reshape(var_3551.astype('float32'), [196, 2]), relay.reshape(const_3552.astype('float32'), [1, 540]), ), 0)
func_1137_call = mod.get_global_var('func_1137')
func_1138_call = mutated_mod.get_global_var('func_1138')
call_3560 = relay.TupleGetItem(func_1137_call(), 0)
call_3561 = relay.TupleGetItem(func_1138_call(), 0)
func_2360_call = mod.get_global_var('func_2360')
func_2361_call = mutated_mod.get_global_var('func_2361')
call_3568 = relay.TupleGetItem(func_2360_call(), 0)
call_3569 = relay.TupleGetItem(func_2361_call(), 0)
output = relay.Tuple([bop_3511,call_3520,call_3531,var_3532,call_3549,var_3550,var_3551,const_3552,call_3560,call_3568,])
output2 = relay.Tuple([bop_3514,call_3521,call_3533,var_3532,call_3553,var_3550,var_3551,const_3552,call_3561,call_3569,])
func_3570 = relay.Function([var_3510,var_3532,var_3550,var_3551,], output)
mod['func_3570'] = func_3570
mod = relay.transform.InferType()(mod)
mutated_mod['func_3570'] = func_3570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3570_call = mutated_mod.get_global_var('func_3570')
var_3572 = relay.var("var_3572", dtype = "float32", shape = (9, 1, 15))#candidate|3572|(9, 1, 15)|var|float32
var_3573 = relay.var("var_3573", dtype = "float32", shape = (405,))#candidate|3573|(405,)|var|float32
var_3574 = relay.var("var_3574", dtype = "int64", shape = (660,))#candidate|3574|(660,)|var|int64
var_3575 = relay.var("var_3575", dtype = "float32", shape = (392,))#candidate|3575|(392,)|var|float32
call_3571 = func_3570_call(var_3572,var_3573,var_3574,var_3575,)
output = call_3571
func_3576 = relay.Function([var_3572,var_3573,var_3574,var_3575,], output)
mutated_mod['func_3576'] = func_3576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_3735 = relay.TupleGetItem(func_225_call(), 0)
call_3736 = relay.TupleGetItem(func_226_call(), 0)
func_2845_call = mod.get_global_var('func_2845')
func_2847_call = mutated_mod.get_global_var('func_2847')
call_3757 = relay.TupleGetItem(func_2845_call(), 1)
call_3758 = relay.TupleGetItem(func_2847_call(), 1)
func_2360_call = mod.get_global_var('func_2360')
func_2361_call = mutated_mod.get_global_var('func_2361')
call_3759 = relay.TupleGetItem(func_2360_call(), 0)
call_3760 = relay.TupleGetItem(func_2361_call(), 0)
output = relay.Tuple([call_3735,call_3757,call_3759,])
output2 = relay.Tuple([call_3736,call_3758,call_3760,])
func_3762 = relay.Function([], output)
mod['func_3762'] = func_3762
mod = relay.transform.InferType()(mod)
mutated_mod['func_3762'] = func_3762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3762_call = mutated_mod.get_global_var('func_3762')
call_3763 = func_3762_call()
output = call_3763
func_3764 = relay.Function([], output)
mutated_mod['func_3764'] = func_3764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_3772 = relay.TupleGetItem(func_3316_call(), 0)
call_3773 = relay.TupleGetItem(func_3318_call(), 0)
output = call_3772
output2 = call_3773
func_3795 = relay.Function([], output)
mod['func_3795'] = func_3795
mod = relay.transform.InferType()(mod)
output = func_3795()
func_3796 = relay.Function([], output)
mutated_mod['func_3796'] = func_3796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3797 = relay.TupleGetItem(func_2536_call(), 3)
call_3798 = relay.TupleGetItem(func_2537_call(), 3)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_3801 = relay.TupleGetItem(func_3316_call(), 0)
call_3802 = relay.TupleGetItem(func_3318_call(), 0)
func_1086_call = mod.get_global_var('func_1086')
func_1088_call = mutated_mod.get_global_var('func_1088')
call_3804 = relay.TupleGetItem(func_1086_call(), 0)
call_3805 = relay.TupleGetItem(func_1088_call(), 0)
func_2736_call = mod.get_global_var('func_2736')
func_2737_call = mutated_mod.get_global_var('func_2737')
call_3810 = relay.TupleGetItem(func_2736_call(), 0)
call_3811 = relay.TupleGetItem(func_2737_call(), 0)
output = relay.Tuple([call_3797,call_3801,call_3804,call_3810,])
output2 = relay.Tuple([call_3798,call_3802,call_3805,call_3811,])
func_3815 = relay.Function([], output)
mod['func_3815'] = func_3815
mod = relay.transform.InferType()(mod)
mutated_mod['func_3815'] = func_3815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3815_call = mutated_mod.get_global_var('func_3815')
call_3816 = func_3815_call()
output = call_3816
func_3817 = relay.Function([], output)
mutated_mod['func_3817'] = func_3817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2330_call = mod.get_global_var('func_2330')
func_2331_call = mutated_mod.get_global_var('func_2331')
call_3889 = func_2330_call()
call_3890 = func_2330_call()
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_3903 = func_1439_call()
call_3904 = func_1439_call()
uop_3909 = relay.log10(call_3889.astype('float32')) # shape=(9, 1, 15)
uop_3911 = relay.log10(call_3890.astype('float32')) # shape=(9, 1, 15)
output = relay.Tuple([call_3903,uop_3909,])
output2 = relay.Tuple([call_3904,uop_3911,])
func_3916 = relay.Function([], output)
mod['func_3916'] = func_3916
mod = relay.transform.InferType()(mod)
output = func_3916()
func_3917 = relay.Function([], output)
mutated_mod['func_3917'] = func_3917
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3935 = relay.var("var_3935", dtype = "float64", shape = (10, 3, 14))#candidate|3935|(10, 3, 14)|var|float64
uop_3936 = relay.asinh(var_3935.astype('float64')) # shape=(10, 3, 14)
output = uop_3936
output2 = uop_3936
func_3938 = relay.Function([var_3935,], output)
mod['func_3938'] = func_3938
mod = relay.transform.InferType()(mod)
var_3939 = relay.var("var_3939", dtype = "float64", shape = (10, 3, 14))#candidate|3939|(10, 3, 14)|var|float64
output = func_3938(var_3939)
func_3940 = relay.Function([var_3939], output)
mutated_mod['func_3940'] = func_3940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_3993 = relay.TupleGetItem(func_3136_call(), 0)
call_3994 = relay.TupleGetItem(func_3138_call(), 0)
uop_4001 = relay.sin(call_3993.astype('float64')) # shape=(1, 324)
uop_4003 = relay.sin(call_3994.astype('float64')) # shape=(1, 324)
output = relay.Tuple([uop_4001,])
output2 = relay.Tuple([uop_4003,])
func_4008 = relay.Function([], output)
mod['func_4008'] = func_4008
mod = relay.transform.InferType()(mod)
output = func_4008()
func_4009 = relay.Function([], output)
mutated_mod['func_4009'] = func_4009
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4022 = relay.var("var_4022", dtype = "float64", shape = (5, 2, 2))#candidate|4022|(5, 2, 2)|var|float64
uop_4023 = relay.rsqrt(var_4022.astype('float64')) # shape=(5, 2, 2)
func_99_call = mod.get_global_var('func_99')
func_101_call = mutated_mod.get_global_var('func_101')
const_4043 = relay.const([4.270775,9.589533,-8.539490,3.951275,7.223963,-4.320443,-4.817357,3.247921,-9.729628,-3.480204,5.813775,0.836746,9.577449,-5.972511,4.205687,-3.700374,4.821406,-1.633653,-1.126867,-7.402269,-0.488130,2.506608,-0.887686,3.873483,1.015669,-0.520883,4.177984,-0.532475,-7.861067,5.862205,-2.026286,2.764583,-5.868561,0.733988,1.441213,-4.796450,-0.189518,4.989410,-4.024342,-5.810144,-0.477400,-3.456648,-1.932652,-3.365715,6.542879,-6.892896,-7.778835,-3.357346,9.709827,4.547507,2.873496,2.887799,1.137584,4.372889,8.198270,0.427644,-6.895047,6.134137,-8.497931,8.410838,6.368395,0.310948,6.420772,-2.753000,-3.882509,-9.378851,-5.281007,0.087005,-7.354374,8.217525,-0.160546,2.771224,7.281114,-9.244973,-6.620723,4.099599,6.918288,9.538736,-0.452924,-9.447222,-4.347031,2.709925,-3.348091,-1.380050,8.296449,-6.935112,0.461138,-0.236571,-9.492211,-4.476184,-4.340783,-8.407683,5.075282,0.035646,-1.432195,-8.491489,-8.313713,5.654436,-8.058683,7.318531,2.761199,-6.158814,7.714913,0.635287,6.840698,-8.157061,-7.371137,3.137255,3.322868,7.192139,-8.013747,-2.214516,1.512444,8.068550,0.158735,4.236431,-8.400440,0.816236,-3.644779,7.736177,0.888633,-1.570120,8.823174,1.768596,-2.558681,-9.790520,-5.983414,4.735525,-3.920796,8.431742,6.831380,-2.908300,-1.926136,5.743547,7.427209], dtype = "float32")#candidate|4043|(135,)|const|float32
call_4042 = func_99_call(relay.reshape(const_4043.astype('float32'), [9, 1, 15]))
call_4044 = func_99_call(relay.reshape(const_4043.astype('float32'), [9, 1, 15]))
func_3916_call = mod.get_global_var('func_3916')
func_3917_call = mutated_mod.get_global_var('func_3917')
call_4052 = relay.TupleGetItem(func_3916_call(), 0)
call_4053 = relay.TupleGetItem(func_3917_call(), 0)
output = relay.Tuple([uop_4023,call_4042,const_4043,call_4052,])
output2 = relay.Tuple([uop_4023,call_4044,const_4043,call_4053,])
func_4061 = relay.Function([var_4022,], output)
mod['func_4061'] = func_4061
mod = relay.transform.InferType()(mod)
mutated_mod['func_4061'] = func_4061
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4062 = relay.var("var_4062", dtype = "float64", shape = (5, 2, 2))#candidate|4062|(5, 2, 2)|var|float64
func_4061_call = mutated_mod.get_global_var('func_4061')
call_4063 = func_4061_call(var_4062)
output = call_4063
func_4064 = relay.Function([var_4062], output)
mutated_mod['func_4064'] = func_4064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_4109 = relay.TupleGetItem(func_848_call(), 0)
call_4110 = relay.TupleGetItem(func_849_call(), 0)
func_676_call = mod.get_global_var('func_676')
func_677_call = mutated_mod.get_global_var('func_677')
call_4118 = func_676_call()
call_4119 = func_676_call()
func_1538_call = mod.get_global_var('func_1538')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_4131 = relay.TupleGetItem(func_1538_call(), 0)
call_4132 = relay.TupleGetItem(func_1540_call(), 0)
func_1538_call = mod.get_global_var('func_1538')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_4133 = relay.TupleGetItem(func_1538_call(), 1)
call_4134 = relay.TupleGetItem(func_1540_call(), 1)
var_4142 = relay.var("var_4142", dtype = "float32", shape = (9, 15, 15))#candidate|4142|(9, 15, 15)|var|float32
bop_4143 = relay.subtract(call_4118.astype('float32'), var_4142.astype('float32')) # shape=(9, 15, 15)
bop_4146 = relay.subtract(call_4119.astype('float32'), var_4142.astype('float32')) # shape=(9, 15, 15)
uop_4148 = relay.sinh(call_4133.astype('float32')) # shape=(3, 14, 1)
uop_4150 = relay.sinh(call_4134.astype('float32')) # shape=(3, 14, 1)
output = relay.Tuple([call_4109,call_4131,bop_4143,uop_4148,])
output2 = relay.Tuple([call_4110,call_4132,bop_4146,uop_4150,])
func_4174 = relay.Function([var_4142,], output)
mod['func_4174'] = func_4174
mod = relay.transform.InferType()(mod)
var_4175 = relay.var("var_4175", dtype = "float32", shape = (9, 15, 15))#candidate|4175|(9, 15, 15)|var|float32
output = func_4174(var_4175)
func_4176 = relay.Function([var_4175], output)
mutated_mod['func_4176'] = func_4176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_4191 = relay.TupleGetItem(func_3316_call(), 0)
call_4192 = relay.TupleGetItem(func_3318_call(), 0)
output = call_4191
output2 = call_4192
func_4213 = relay.Function([], output)
mod['func_4213'] = func_4213
mod = relay.transform.InferType()(mod)
mutated_mod['func_4213'] = func_4213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4213_call = mutated_mod.get_global_var('func_4213')
call_4214 = func_4213_call()
output = call_4214
func_4215 = relay.Function([], output)
mutated_mod['func_4215'] = func_4215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1970_call = mod.get_global_var('func_1970')
func_1971_call = mutated_mod.get_global_var('func_1971')
call_4225 = func_1970_call()
call_4226 = func_1970_call()
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_4252 = relay.TupleGetItem(func_225_call(), 0)
call_4253 = relay.TupleGetItem(func_226_call(), 0)
output = relay.Tuple([call_4225,call_4252,])
output2 = relay.Tuple([call_4226,call_4253,])
func_4254 = relay.Function([], output)
mod['func_4254'] = func_4254
mod = relay.transform.InferType()(mod)
mutated_mod['func_4254'] = func_4254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4254_call = mutated_mod.get_global_var('func_4254')
call_4255 = func_4254_call()
output = call_4255
func_4256 = relay.Function([], output)
mutated_mod['func_4256'] = func_4256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1615_call = mod.get_global_var('func_1615')
func_1617_call = mutated_mod.get_global_var('func_1617')
call_4293 = func_1615_call()
call_4294 = func_1615_call()
uop_4298 = relay.log10(call_4293.astype('float32')) # shape=(15, 9, 2)
uop_4300 = relay.log10(call_4294.astype('float32')) # shape=(15, 9, 2)
output = relay.Tuple([uop_4298,])
output2 = relay.Tuple([uop_4300,])
func_4304 = relay.Function([], output)
mod['func_4304'] = func_4304
mod = relay.transform.InferType()(mod)
mutated_mod['func_4304'] = func_4304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4304_call = mutated_mod.get_global_var('func_4304')
call_4305 = func_4304_call()
output = call_4305
func_4306 = relay.Function([], output)
mutated_mod['func_4306'] = func_4306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_4322 = relay.TupleGetItem(func_3136_call(), 0)
call_4323 = relay.TupleGetItem(func_3138_call(), 0)
var_4324 = relay.var("var_4324", dtype = "float32", shape = (1, 324))#candidate|4324|(1, 324)|var|float32
bop_4325 = relay.divide(call_4322.astype('float64'), relay.reshape(var_4324.astype('float64'), relay.shape_of(call_4322))) # shape=(1, 324)
bop_4328 = relay.divide(call_4323.astype('float64'), relay.reshape(var_4324.astype('float64'), relay.shape_of(call_4323))) # shape=(1, 324)
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
const_4330 = relay.const([9.543059,1.201576,7.140427,6.343698,9.907631,-8.088872,-6.725082,-3.541602,0.044747,-3.347836,-2.623568,5.281901,4.468281,-3.977672,-0.341322,1.289323,-6.350023,-7.447068,-0.542702,-8.683644], dtype = "float64")#candidate|4330|(20,)|const|float64
call_4329 = relay.TupleGetItem(func_4061_call(relay.reshape(const_4330.astype('float64'), [5, 2, 2])), 2)
call_4331 = relay.TupleGetItem(func_4064_call(relay.reshape(const_4330.astype('float64'), [5, 2, 2])), 2)
func_2680_call = mod.get_global_var('func_2680')
func_2682_call = mutated_mod.get_global_var('func_2682')
var_4340 = relay.var("var_4340", dtype = "float64", shape = (42,))#candidate|4340|(42,)|var|float64
call_4339 = relay.TupleGetItem(func_2680_call(relay.reshape(var_4340.astype('float64'), [42,])), 3)
call_4341 = relay.TupleGetItem(func_2682_call(relay.reshape(var_4340.astype('float64'), [42,])), 3)
uop_4345 = relay.sin(var_4340.astype('float64')) # shape=(42,)
uop_4350 = relay.asinh(call_4322.astype('float32')) # shape=(1, 324)
uop_4352 = relay.asinh(call_4323.astype('float32')) # shape=(1, 324)
func_1392_call = mod.get_global_var('func_1392')
func_1393_call = mutated_mod.get_global_var('func_1393')
call_4381 = relay.TupleGetItem(func_1392_call(), 0)
call_4382 = relay.TupleGetItem(func_1393_call(), 0)
output = relay.Tuple([bop_4325,call_4329,const_4330,call_4339,uop_4345,uop_4350,call_4381,])
output2 = relay.Tuple([bop_4328,call_4331,const_4330,call_4341,uop_4345,uop_4352,call_4382,])
func_4383 = relay.Function([var_4324,var_4340,], output)
mod['func_4383'] = func_4383
mod = relay.transform.InferType()(mod)
var_4384 = relay.var("var_4384", dtype = "float32", shape = (1, 324))#candidate|4384|(1, 324)|var|float32
var_4385 = relay.var("var_4385", dtype = "float64", shape = (42,))#candidate|4385|(42,)|var|float64
output = func_4383(var_4384,var_4385,)
func_4386 = relay.Function([var_4384,var_4385,], output)
mutated_mod['func_4386'] = func_4386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2545_call = mutated_mod.get_global_var('func_2545')
call_4407 = relay.TupleGetItem(func_2543_call(), 0)
call_4408 = relay.TupleGetItem(func_2545_call(), 0)
output = call_4407
output2 = call_4408
func_4412 = relay.Function([], output)
mod['func_4412'] = func_4412
mod = relay.transform.InferType()(mod)
mutated_mod['func_4412'] = func_4412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4412_call = mutated_mod.get_global_var('func_4412')
call_4413 = func_4412_call()
output = call_4413
func_4414 = relay.Function([], output)
mutated_mod['func_4414'] = func_4414
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4475 = relay.var("var_4475", dtype = "float32", shape = (14, 12, 11))#candidate|4475|(14, 12, 11)|var|float32
var_4476 = relay.var("var_4476", dtype = "float32", shape = (14, 12, 11))#candidate|4476|(14, 12, 11)|var|float32
bop_4477 = relay.power(var_4475.astype('float32'), relay.reshape(var_4476.astype('float32'), relay.shape_of(var_4475))) # shape=(14, 12, 11)
func_4412_call = mod.get_global_var('func_4412')
func_4414_call = mutated_mod.get_global_var('func_4414')
call_4491 = func_4412_call()
call_4492 = func_4412_call()
output = relay.Tuple([bop_4477,call_4491,])
output2 = relay.Tuple([bop_4477,call_4492,])
func_4500 = relay.Function([var_4475,var_4476,], output)
mod['func_4500'] = func_4500
mod = relay.transform.InferType()(mod)
var_4501 = relay.var("var_4501", dtype = "float32", shape = (14, 12, 11))#candidate|4501|(14, 12, 11)|var|float32
var_4502 = relay.var("var_4502", dtype = "float32", shape = (14, 12, 11))#candidate|4502|(14, 12, 11)|var|float32
output = func_4500(var_4501,var_4502,)
func_4503 = relay.Function([var_4501,var_4502,], output)
mutated_mod['func_4503'] = func_4503
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4540 = relay.var("var_4540", dtype = "float64", shape = ())#candidate|4540|()|var|float64
const_4541 = relay.const([[[7.990735,-9.531436,-3.051749,9.350738,3.891691,-0.817740,-4.673905],[6.410243,-0.495692,-1.921408,-4.347511,6.128108,6.576319,-8.843597],[2.148930,-3.281708,-7.173350,-8.085301,2.294943,-0.742497,8.729853],[9.647115,1.948934,3.899272,9.100291,4.892104,-4.583421,0.453272],[8.855655,3.338141,5.236432,9.551466,-2.499564,8.604778,-9.055264],[-3.729709,-1.989963,8.932037,9.259789,4.296978,-2.911162,-9.731023],[6.489523,-8.270048,1.934188,8.470839,3.045188,2.365942,-4.059818],[-7.002379,-3.545316,-9.432794,-7.970311,-7.662628,-8.485415,3.987788],[-3.058553,-0.740120,7.426690,5.093058,-5.166894,-1.959415,8.913471],[6.311802,-4.450618,-5.770156,0.494076,1.141747,-7.075241,8.739198],[-4.915826,2.946238,-8.621490,-2.938917,-9.640745,-0.576221,4.524964],[0.122847,-5.682945,-7.917662,-7.200356,1.043872,-4.678427,9.763903],[5.381172,0.174666,9.925497,-8.848790,-8.064423,-2.199980,-8.968637]],[[7.185503,3.647929,7.915163,-0.392476,-5.387014,-8.422526,-2.530255],[-3.095281,-8.489493,-6.679102,4.530829,-8.989505,4.506512,4.714510],[-1.578301,-4.901561,7.396202,-6.593056,-8.067412,-4.429936,0.270147],[-9.168735,1.148073,4.254335,-3.115862,-0.556230,-8.178679,-1.659520],[0.127464,3.567324,6.976128,-1.196462,7.948209,5.797965,0.500200],[-5.321580,2.401804,-8.538916,7.412304,-9.512683,5.540675,-4.749166],[6.556482,5.312057,-4.172976,-2.716913,-0.980797,-7.348734,6.582611],[6.616698,9.453673,8.847808,4.668238,-5.478523,-0.156431,-4.840498],[1.548566,5.287883,8.104253,2.525561,3.225991,-5.519823,-6.379933],[3.564890,-9.912870,-8.979889,-7.862346,-9.472393,6.947055,-8.725465],[8.094491,8.519539,7.839712,-1.492789,5.380227,-9.872147,9.043941],[2.301048,6.750803,-6.366952,3.905539,-0.336446,-5.841642,2.156374],[2.195121,9.856745,1.709557,5.905165,3.247228,8.614993,4.872434]],[[8.306644,-2.889565,5.921735,4.011247,-0.954832,-6.128035,-9.120198],[5.914498,4.909947,-0.279613,-8.607284,0.852639,-2.805512,8.846247],[-8.984767,-4.330668,8.853005,-2.166827,-5.325075,-2.166086,-6.900556],[9.369040,-8.732063,1.311954,5.267216,-9.020908,9.377285,5.645749],[8.330281,3.222980,-9.154762,8.358360,2.557471,-6.500167,-6.971261],[-7.289541,9.584621,8.236748,-0.565629,7.854531,-6.596500,7.590192],[-4.124221,-6.291573,6.745938,8.511855,5.940137,-6.965738,-1.637828],[-8.090273,7.949219,0.017370,6.007965,-8.592721,3.671903,5.131584],[-2.826555,7.704285,-7.197290,-6.761314,-7.805211,7.130632,-3.912623],[-4.380549,-0.879516,0.809102,3.294338,-2.193937,-7.415009,-6.248565],[2.288400,3.177086,9.466168,-1.080529,-5.381922,0.913625,-6.884573],[-7.153796,-0.632969,8.724504,-4.345779,2.440345,3.356708,-3.821542],[-3.642626,-8.431006,-1.659118,7.429049,-7.242187,7.833143,-1.519261]],[[1.335757,9.064868,-1.314400,-8.376184,-9.970477,-7.800402,-6.912754],[-5.851967,2.515716,-5.166434,-3.549637,-4.626694,-6.437693,9.516796],[2.440791,-8.784162,-5.933692,2.768200,-6.948499,-0.572103,-8.601300],[-1.966920,-0.046569,6.400563,0.969973,2.172368,-3.078726,-1.586846],[4.008882,2.702223,9.227367,4.735851,5.564385,-2.398002,5.445876],[2.362074,-8.592598,-9.602987,-3.907412,-7.351517,8.197629,0.263438],[1.687276,-8.941368,1.208542,-7.335221,-3.883662,-1.868654,-2.757579],[3.389755,4.473990,0.536021,-2.757317,-4.738174,4.966882,-6.491911],[4.343913,-6.455961,4.879570,3.060350,-8.518775,-5.583116,3.085528],[2.574168,5.413651,9.643304,2.357355,-6.788567,6.638395,-8.296978],[-2.767146,9.984142,-1.999812,-9.291579,6.689722,-9.821758,2.951180],[-4.907100,0.742775,-3.175333,-4.495019,8.801440,-8.918645,6.712743],[-3.994027,-4.338467,-4.882800,-8.255742,-4.816412,3.525873,-3.745274]],[[1.972446,-2.648173,8.471802,0.123321,-2.967994,1.917423,4.558015],[-1.803228,3.184177,-0.155290,5.553963,-7.713721,0.508186,-5.194022],[-8.836305,-1.066617,2.007451,2.669919,-8.863618,-0.515362,-5.472654],[-3.822093,-2.803630,-0.006181,-4.588356,0.533153,2.570472,6.414444],[-0.858541,2.287238,1.314313,0.410157,-9.760354,8.921110,3.289219],[-1.320313,0.939402,-2.032792,4.471650,-4.421060,1.214687,0.363196],[0.397236,-3.550596,-5.154886,-3.210600,0.986243,-5.417343,-4.009690],[0.398405,-8.742935,8.224322,-1.948855,4.871885,-8.285539,6.469218],[9.924247,-2.748860,-5.492695,1.238962,3.848138,-6.860673,9.069203],[-6.475320,-6.744239,7.962468,2.528389,-9.963196,-7.740671,4.450368],[0.004017,5.780118,7.558503,7.232852,-2.903979,0.274314,-8.871885],[-9.382442,-5.058943,4.433083,-9.743924,3.157269,5.231690,-3.637582],[6.166397,-5.228958,-8.001262,-4.306075,-4.851045,1.486228,-8.600853]],[[-5.356214,-6.464008,-9.521527,2.533311,4.878178,-8.684000,-5.427975],[5.550590,-6.920774,-6.965457,8.377230,-0.662680,7.228211,-8.641820],[5.929471,7.852750,7.361949,-2.676269,-9.156676,-2.545477,-6.456576],[4.535596,-1.809869,4.942440,2.854532,-2.386143,-8.360397,-9.555339],[2.260088,3.624236,6.984127,-5.998225,-9.749071,-2.046072,-4.925588],[1.899373,-9.361493,8.177836,9.270082,6.421701,2.808762,5.152581],[-4.976452,7.084712,-3.935704,-9.518817,3.048228,6.689055,6.892476],[-3.623590,-5.707655,-5.729704,-2.746519,1.920302,-3.549115,3.891108],[-3.759881,-7.463652,-6.250082,-3.046059,-4.315003,3.935777,8.727940],[6.233830,-3.665654,8.918307,2.040245,9.628979,9.780616,8.811747],[2.726986,8.685766,-0.629883,-7.072731,9.840086,2.261416,8.134012],[6.323886,6.672404,-7.487631,8.101716,-1.481655,7.470143,-1.454280],[9.904804,1.126562,-6.630257,-8.068601,-9.372294,-1.034218,-9.032872]],[[8.701047,-5.788591,-6.579052,7.246871,2.718745,-8.334965,-6.657422],[-1.228148,9.956500,-8.087550,-4.373122,6.398477,3.887126,-4.390012],[-8.894906,-6.330566,-8.231680,-3.866826,-9.877408,2.330980,-7.446838],[-8.759116,-3.672615,-9.733762,-7.528264,-6.834161,0.561375,6.115414],[7.661582,-7.865180,-8.729890,6.042381,7.373951,-6.604111,3.497859],[-6.789701,5.725497,-5.149616,7.215350,4.493859,-8.416232,-9.536620],[-3.630854,-3.529117,1.332563,4.276153,0.504458,7.320096,-9.480085],[1.604425,1.411090,-0.817784,-9.113906,-4.311175,8.372894,2.973181],[9.229090,1.325042,8.341567,2.596233,1.322587,3.450140,0.572085],[6.026093,-4.882214,-4.161455,-9.839207,-7.826644,6.419480,-8.627960],[3.739736,-1.815114,-3.390511,-1.105591,-1.696287,-0.428519,-4.351087],[-5.677542,-7.571368,7.759000,-6.626272,1.179501,-7.730165,6.336179],[-2.878959,-3.856174,0.569240,6.156737,6.082819,-2.671234,6.404798]],[[0.905593,-9.114748,-1.055173,1.541688,6.038519,1.323378,7.418544],[-8.013278,5.295760,-1.267526,-0.052208,3.964847,1.458793,0.317107],[-3.218545,6.402749,-3.210350,9.928378,-9.612768,9.722537,3.885663],[-3.190345,-3.432594,4.789014,-0.220000,-6.046280,-5.979207,-1.110743],[-7.321678,3.127823,-8.084788,-4.492084,-3.709030,3.805908,-9.319689],[-0.487561,0.239281,-2.796939,0.582426,-7.754943,-6.868389,8.402527],[-5.834130,-5.872818,3.180801,7.612381,-7.288887,8.810717,4.218650],[-1.112626,5.142113,0.994842,0.473497,-2.291195,-1.007812,-0.944812],[6.902077,3.833158,8.653055,-4.090526,9.512506,9.935054,5.944899],[-5.578618,1.868847,9.859821,1.548425,-4.237946,-6.317976,8.272120],[4.334598,8.043568,4.839222,-6.167567,2.429749,-7.238220,-5.073620],[-1.924027,-0.771674,-6.467517,2.924772,-2.005648,6.188127,-3.039875],[9.889548,-9.648301,8.361643,-5.349420,-7.803386,-4.681086,3.679363]],[[-3.387212,-0.035309,-6.528564,9.060569,-5.845447,-7.594040,3.445919],[0.125005,0.335297,1.496949,5.712006,-5.143938,-3.508759,-5.904841],[-1.792582,4.062695,3.321357,3.442471,-6.651986,0.516494,-5.585632],[2.815477,3.048635,7.147314,1.646297,-4.379031,8.834197,-7.146615],[6.641269,-2.501742,0.758987,-0.427613,3.665596,-4.980279,-4.577855],[6.422416,0.819820,-7.817027,7.609242,1.116425,-4.117087,-7.834527],[-0.792682,8.597814,0.785269,9.825286,5.867308,-2.056255,-9.678467],[-5.386171,-1.542479,3.674826,-4.512296,-5.368981,1.604860,2.981770],[7.619927,3.230967,-2.887147,8.087414,5.059699,-4.958541,-2.563870],[8.667800,5.551000,4.818170,0.530245,4.519731,-2.860121,-3.193273],[-4.912169,3.386539,4.923862,3.428513,-6.251945,2.520353,-9.839880],[-3.183870,-2.954401,6.141432,-8.932224,7.492438,0.901960,5.258772],[-3.002447,9.640487,1.702699,-4.269515,9.569408,8.161451,-5.666947]],[[7.887361,-0.107237,4.985051,-9.384052,9.603074,1.318183,-4.666130],[1.199867,-7.421863,7.981402,-6.885248,1.766874,6.452181,4.288195],[-1.521240,-2.738248,-0.598636,9.430101,4.561431,-6.352607,-6.112746],[-9.243277,-1.815015,6.809709,3.032080,-7.874198,0.075149,4.932175],[-4.099534,7.254691,-4.962798,2.437201,9.754399,0.758077,-1.024929],[2.794702,2.770490,7.342034,8.670510,3.952296,-8.010992,3.350583],[8.727971,-7.268750,3.661334,-6.352086,1.154861,-4.549562,-6.215690],[-2.726455,0.186853,-9.439062,0.938109,-0.214452,-5.117145,1.976791],[4.130367,-8.522948,6.137111,-0.276569,9.066548,6.576594,-5.357018],[2.281674,6.956037,6.962187,5.914745,8.774230,-7.306199,8.201661],[8.657935,8.453251,3.815100,4.726928,-8.110123,5.639486,-6.579984],[5.628213,-1.082155,-4.595013,-1.152121,-0.080527,1.065888,-3.465777],[8.873214,-9.117392,-4.594755,4.842746,1.345932,5.995892,3.226907]],[[5.990943,6.950649,-2.567509,2.416787,2.551812,2.602923,4.222735],[0.486863,-1.336747,-5.850759,-3.578746,-6.744906,-4.779120,-5.065380],[4.077046,9.168801,-5.441943,0.090786,-5.567590,9.696055,-0.349745],[-9.254149,1.367601,4.357599,-3.536183,-2.085081,3.939300,7.175367],[-6.947422,7.813244,1.791156,1.973839,1.859135,-4.432035,4.764465],[6.591008,-3.663739,-1.498513,9.273276,9.951035,1.693649,-1.557220],[-9.153056,-1.287524,-0.547841,3.307224,-1.268629,9.963061,6.814155],[-3.512741,5.016973,9.913850,8.768741,6.184493,2.178340,-2.587941],[-6.791970,8.357894,-3.772086,2.890760,0.696886,-4.233742,6.818904],[4.140837,-8.310401,-2.713951,9.701576,9.578184,3.009880,-3.992858],[-8.118558,0.706233,1.458275,6.642566,-9.337800,-6.960854,7.693475],[-9.017528,-6.616958,-1.980883,7.057290,-4.376763,-0.945245,1.394724],[-7.882116,-4.281296,-1.335932,6.262472,0.960742,-3.126989,-5.144157]],[[7.297658,7.801746,-6.769319,-6.597916,-9.122887,8.988001,-5.401498],[2.744957,5.674667,1.613650,-5.135627,7.840592,-0.373643,-7.181311],[2.163634,5.550115,1.383095,-2.948090,9.468586,-3.526655,-7.988814],[-4.212386,0.519949,-6.880657,-2.849163,-6.040429,7.951366,-2.582764],[-7.478206,-1.511656,6.854774,3.588707,2.964482,5.500531,-9.508426],[-2.330296,2.049569,6.895377,-1.388242,-6.844953,-6.715763,3.570551],[-2.311131,3.111698,9.020753,-5.922596,2.478545,5.029666,2.887547],[0.321567,-3.541004,-9.059944,7.284188,-5.399560,1.664334,-2.420165],[7.526106,-2.188126,5.395201,1.828933,5.370564,-8.585592,1.663800],[4.472354,-5.776395,-8.886838,8.878706,-9.289066,-6.905929,-7.697754],[7.423373,6.246212,2.357935,4.975750,3.689388,1.948553,-6.037404],[-6.418988,0.248915,8.382252,-3.978096,-4.159015,-8.607430,-8.936230],[9.144739,4.355658,2.012096,7.034627,-3.920078,-2.286726,6.723481]],[[-7.964470,8.011226,7.653639,8.128186,-2.240089,-5.981936,9.216880],[8.171971,-4.236343,-9.556721,-5.414871,-8.774349,-4.284273,-6.612392],[7.861626,-0.924703,0.274824,-2.078401,-6.988505,7.336707,0.024696],[6.590125,2.625740,5.687287,8.148316,9.679315,1.229340,-2.999925],[-9.169638,-9.961435,-5.059902,2.376103,-3.443146,9.496380,1.547173],[7.555880,-3.309852,8.888521,-9.988594,2.665055,8.439924,2.914996],[1.030339,-5.165552,-9.444575,8.087667,-2.294462,-5.429213,-8.726276],[6.331009,2.320589,-0.619330,-6.128292,3.927428,-3.486176,-5.574081],[1.377853,5.612805,7.997031,-9.727570,-3.831207,4.610453,-3.140256],[-7.865905,1.813942,4.753618,-3.969815,-3.817575,2.689747,3.181296],[1.953568,8.904566,9.669926,9.468324,3.808862,-4.647511,1.909893],[-8.778873,-6.878693,-8.262231,-6.699327,-0.422811,0.355781,4.591686],[-2.287672,8.094837,3.279848,-1.479668,2.555970,7.206101,7.663419]]], dtype = "float64")#candidate|4541|(13, 13, 7)|const|float64
bop_4542 = relay.floor_divide(var_4540.astype('float64'), const_4541.astype('float64')) # shape=(13, 13, 7)
func_2330_call = mod.get_global_var('func_2330')
func_2331_call = mutated_mod.get_global_var('func_2331')
call_4548 = func_2330_call()
call_4549 = func_2330_call()
output = relay.Tuple([bop_4542,call_4548,])
output2 = relay.Tuple([bop_4542,call_4549,])
func_4560 = relay.Function([var_4540,], output)
mod['func_4560'] = func_4560
mod = relay.transform.InferType()(mod)
var_4561 = relay.var("var_4561", dtype = "float64", shape = ())#candidate|4561|()|var|float64
output = func_4560(var_4561)
func_4562 = relay.Function([var_4561], output)
mutated_mod['func_4562'] = func_4562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1877_call = mod.get_global_var('func_1877')
func_1878_call = mutated_mod.get_global_var('func_1878')
call_4574 = relay.TupleGetItem(func_1877_call(), 1)
call_4575 = relay.TupleGetItem(func_1878_call(), 1)
func_2285_call = mod.get_global_var('func_2285')
func_2286_call = mutated_mod.get_global_var('func_2286')
call_4576 = relay.TupleGetItem(func_2285_call(), 0)
call_4577 = relay.TupleGetItem(func_2286_call(), 0)
func_2153_call = mod.get_global_var('func_2153')
func_2156_call = mutated_mod.get_global_var('func_2156')
var_4579 = relay.var("var_4579", dtype = "uint32", shape = ())#candidate|4579|()|var|uint32
call_4578 = relay.TupleGetItem(func_2153_call(relay.reshape(var_4579.astype('uint32'), []), relay.reshape(call_4576.astype('uint32'), [256,]), ), 3)
call_4580 = relay.TupleGetItem(func_2156_call(relay.reshape(var_4579.astype('uint32'), []), relay.reshape(call_4576.astype('uint32'), [256,]), ), 3)
output = relay.Tuple([call_4574,call_4576,call_4578,var_4579,])
output2 = relay.Tuple([call_4575,call_4577,call_4580,var_4579,])
func_4600 = relay.Function([var_4579,], output)
mod['func_4600'] = func_4600
mod = relay.transform.InferType()(mod)
var_4601 = relay.var("var_4601", dtype = "uint32", shape = ())#candidate|4601|()|var|uint32
output = func_4600(var_4601)
func_4602 = relay.Function([var_4601], output)
mutated_mod['func_4602'] = func_4602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_4669 = relay.TupleGetItem(func_225_call(), 0)
call_4670 = relay.TupleGetItem(func_226_call(), 0)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_4671 = relay.TupleGetItem(func_3136_call(), 0)
call_4672 = relay.TupleGetItem(func_3138_call(), 0)
output = relay.Tuple([call_4669,call_4671,])
output2 = relay.Tuple([call_4670,call_4672,])
func_4692 = relay.Function([], output)
mod['func_4692'] = func_4692
mod = relay.transform.InferType()(mod)
mutated_mod['func_4692'] = func_4692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4692_call = mutated_mod.get_global_var('func_4692')
call_4693 = func_4692_call()
output = call_4693
func_4694 = relay.Function([], output)
mutated_mod['func_4694'] = func_4694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_4771 = relay.TupleGetItem(func_970_call(), 1)
call_4772 = relay.TupleGetItem(func_972_call(), 1)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
var_4781 = relay.var("var_4781", dtype = "float64", shape = (42,))#candidate|4781|(42,)|var|float64
call_4780 = func_681_call(relay.reshape(var_4781.astype('float64'), [3, 14, 1]))
call_4782 = func_681_call(relay.reshape(var_4781.astype('float64'), [3, 14, 1]))
bop_4807 = relay.logical_or(call_4780.astype('bool'), relay.reshape(var_4781.astype('bool'), relay.shape_of(call_4780))) # shape=(3, 14, 1)
bop_4810 = relay.logical_or(call_4782.astype('bool'), relay.reshape(var_4781.astype('bool'), relay.shape_of(call_4782))) # shape=(3, 14, 1)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_4822 = relay.TupleGetItem(func_3136_call(), 0)
call_4823 = relay.TupleGetItem(func_3138_call(), 0)
output = relay.Tuple([call_4771,bop_4807,call_4822,])
output2 = relay.Tuple([call_4772,bop_4810,call_4823,])
func_4824 = relay.Function([var_4781,], output)
mod['func_4824'] = func_4824
mod = relay.transform.InferType()(mod)
var_4825 = relay.var("var_4825", dtype = "float64", shape = (42,))#candidate|4825|(42,)|var|float64
output = func_4824(var_4825)
func_4826 = relay.Function([var_4825], output)
mutated_mod['func_4826'] = func_4826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3762_call = mod.get_global_var('func_3762')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_4851 = relay.TupleGetItem(func_3762_call(), 0)
call_4852 = relay.TupleGetItem(func_3764_call(), 0)
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
const_4870 = relay.const([[-7.750347,-5.731340,-1.928960,-5.495770,4.084053,-2.962220,4.447228,5.741837,7.359950,4.910438,4.302176,1.990070,6.401988,-4.339119,6.898874,6.407178,-2.484665,-6.985107,5.706727,3.237328,3.532184,3.681503,-0.030082,-7.877860,0.820507,-5.151122,9.125372,1.788149,-9.624121,-2.668091,-4.481072,2.485334,2.850592,8.854637,-0.165777,0.317680,-2.043749,-4.233943,-2.076564,0.244146,9.209324,-5.444133,7.591430,4.361875,-9.263959,-8.103611,-3.960073,2.654555,0.812763,-1.004032,-6.294751,0.937696,-6.684985,9.418273,-6.234830,-8.138470,-2.273620,-0.256974,-8.814786,-1.623570,8.827652,-8.311647,-3.189212,-7.721253,-0.699830,-3.431002,-0.614999,-2.411978,5.471467,6.014338,-1.039344,1.081840,3.325750,-2.564607,-8.627291,-0.488473,8.709582,4.554939,-0.887804,8.402785,-1.281509,7.837058,-4.455958,5.093481,-4.463856,2.440197,-3.885493,7.864286,3.781976,3.468299,-9.744992,9.436350,-2.546069,-2.605711,-3.214240,-4.736688,6.345454,-9.367408,3.151714,0.558418,-9.747381,-3.140036,-2.219721,-1.592719,2.708148,8.940545,1.244186,-6.623910,6.024325,8.412137,-2.776856,-7.406570,0.163331,3.926494,-4.365455,-9.422053,-3.908764,0.641600,0.072023,-2.645043,7.678790,-4.813616,-2.451367,1.667465,0.763860,-7.850727,-2.806713,1.878606,3.484832,-2.019092,-4.016193,-6.741823,5.321774,7.502849,-4.550117]], dtype = "float32")#candidate|4870|(1, 135)|const|float32
call_4869 = relay.TupleGetItem(func_435_call(relay.reshape(const_4870.astype('float32'), [3, 45])), 4)
call_4871 = relay.TupleGetItem(func_438_call(relay.reshape(const_4870.astype('float32'), [3, 45])), 4)
func_1137_call = mod.get_global_var('func_1137')
func_1138_call = mutated_mod.get_global_var('func_1138')
call_4887 = relay.TupleGetItem(func_1137_call(), 1)
call_4888 = relay.TupleGetItem(func_1138_call(), 1)
output = relay.Tuple([call_4851,call_4869,const_4870,call_4887,])
output2 = relay.Tuple([call_4852,call_4871,const_4870,call_4888,])
func_4891 = relay.Function([], output)
mod['func_4891'] = func_4891
mod = relay.transform.InferType()(mod)
output = func_4891()
func_4892 = relay.Function([], output)
mutated_mod['func_4892'] = func_4892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1656_call = mod.get_global_var('func_1656')
func_1658_call = mutated_mod.get_global_var('func_1658')
call_4908 = func_1656_call()
call_4909 = func_1656_call()
func_663_call = mod.get_global_var('func_663')
func_665_call = mutated_mod.get_global_var('func_665')
call_4933 = func_663_call()
call_4934 = func_663_call()
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_4939 = relay.TupleGetItem(func_1914_call(), 0)
call_4940 = relay.TupleGetItem(func_1915_call(), 0)
var_4960 = relay.var("var_4960", dtype = "float32", shape = (9, 5, 15))#candidate|4960|(9, 5, 15)|var|float32
bop_4961 = relay.not_equal(call_4908.astype('bool'), var_4960.astype('bool')) # shape=(9, 5, 15)
bop_4964 = relay.not_equal(call_4909.astype('bool'), var_4960.astype('bool')) # shape=(9, 5, 15)
output = relay.Tuple([call_4933,call_4939,bop_4961,])
output2 = relay.Tuple([call_4934,call_4940,bop_4964,])
func_4967 = relay.Function([var_4960,], output)
mod['func_4967'] = func_4967
mod = relay.transform.InferType()(mod)
mutated_mod['func_4967'] = func_4967
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4968 = relay.var("var_4968", dtype = "float32", shape = (9, 5, 15))#candidate|4968|(9, 5, 15)|var|float32
func_4967_call = mutated_mod.get_global_var('func_4967')
call_4969 = func_4967_call(var_4968)
output = call_4969
func_4970 = relay.Function([var_4968], output)
mutated_mod['func_4970'] = func_4970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_269_call = mod.get_global_var('func_269')
func_271_call = mutated_mod.get_global_var('func_271')
call_5029 = relay.TupleGetItem(func_269_call(), 2)
call_5030 = relay.TupleGetItem(func_271_call(), 2)
func_1480_call = mod.get_global_var('func_1480')
func_1483_call = mutated_mod.get_global_var('func_1483')
const_5036 = relay.const([[0.979309],[2.405889],[-9.321965],[-1.511223],[-8.159725],[8.855888],[7.138463],[1.531053],[6.812708],[1.395719],[8.991750],[-4.426359],[-9.242977],[-1.207472],[2.803832],[8.727275],[5.787739],[-0.354583],[-6.851590],[5.875045],[-1.587507],[-6.938128],[-2.731146],[0.287609],[-2.401114],[4.373122],[-9.323576],[-6.217353],[1.637933],[-9.145171],[0.403040],[9.413047],[-4.897182],[8.829895],[5.304768],[0.267444],[5.103509],[1.079660],[-8.545433],[8.266904],[1.383741],[-3.812037],[-7.416093],[-3.157913],[-4.911644],[7.471817],[9.734694],[-1.791656],[-4.173856],[-3.857601],[6.160795],[9.594782],[-2.353469],[-0.490564],[2.959086],[3.211029],[-2.216485],[6.632239],[-8.719232],[-3.701748],[-6.304531],[-4.656989],[-1.774692],[2.944732],[-6.312115],[-1.693101],[1.251569],[-7.697287],[8.014785],[-8.309817],[-8.816685],[1.132002],[-4.597069],[-3.122703],[6.976913],[6.620045],[-5.792168],[1.087511],[-5.724785],[4.709667],[-2.122446],[-2.978668],[8.333323],[0.941845],[2.317580],[-8.018135],[9.047778],[-1.168285],[-3.227192],[-3.682254],[9.501493],[9.257074],[-7.164598],[4.670450],[0.500685],[0.911671],[-9.476072],[4.358584],[2.044839],[-4.767937],[7.402860],[-5.835892],[4.489047],[-4.984433],[6.047510],[2.290827],[-5.508134],[-7.638638],[1.271441],[5.128215],[-3.662273],[-2.487706],[7.328519],[3.638594],[0.991862],[8.915386],[-6.370095],[3.578706],[9.074620],[0.814610],[2.645813],[1.777271],[1.266959],[-1.061952],[5.138112],[1.779262],[-4.172175],[1.185856],[3.084079],[-9.408975],[-5.229525],[7.504096],[-3.364786],[-3.744304],[-9.693018],[-1.682886],[-2.655424],[0.478151],[-9.080000],[-2.795818],[-2.818454],[4.340638],[-2.919903],[-7.617511],[2.145941],[-1.015851],[-1.878318],[-2.210777],[-8.510790],[-0.919510],[-4.713273],[-7.196425],[5.458300],[-4.119482],[5.029669],[5.627152],[-6.122498],[6.776548],[2.404210],[7.992198],[-5.830131],[2.767167],[0.505059],[9.971891],[-5.750992],[3.826064],[6.526459],[-2.866457],[5.297544],[-0.657307],[3.769445],[-7.558205],[-4.908690],[-4.370359],[4.899839],[7.294841],[3.416302],[0.931399],[-5.058732],[5.663327],[-8.374673],[-6.215662],[-2.221654],[-4.092116],[8.042000],[2.159706],[4.852431],[7.310840],[2.498990],[8.202728],[4.810242],[-7.048098],[1.835914],[9.185220],[8.380511],[4.044394],[7.646089],[7.521908],[-9.118669],[-4.295048],[-9.900354],[-1.706202],[6.136716],[5.688497],[-2.461719],[-7.025827],[4.794646],[-2.312379],[-2.226255],[2.106553],[-3.164217],[7.471054],[-5.134995],[-2.210362],[4.731993],[-8.237521],[-8.039870],[3.423316],[-6.502223],[-4.952741],[8.908564],[-4.137642],[1.799883],[-6.820336],[5.205629],[7.410820],[-2.574065],[9.384192],[4.213493],[7.885640],[-5.821063],[-5.884322],[-8.837350],[1.223607],[3.875177],[2.518874],[-1.615455],[1.172572],[2.519981],[9.040588],[4.720236],[-8.729567],[0.689881],[-1.152194],[4.195658],[8.787493],[-6.766197],[-5.262144],[9.573730],[9.264193],[4.085519],[-3.577276],[4.602821],[-0.076653],[2.245159],[5.646771],[-4.627293],[-6.412909],[8.340317],[7.814049],[-1.152759],[1.575370],[-3.726444],[7.529935],[9.535423],[-4.077854],[-7.712307],[-6.161584],[8.090172],[-9.193317],[-7.917331],[3.515908],[7.315513],[-5.785801],[8.176064],[-8.028859],[8.555702],[-3.329981],[6.792740],[9.553987],[-4.244050],[-7.787896],[-1.190249],[-6.117670],[8.383321],[-5.513995],[-1.431315],[-3.523548],[0.551947],[3.203822],[-1.465477],[-6.843877],[2.958593],[-8.241388],[6.877752],[1.966718],[8.928796],[-7.690317],[-3.167972],[1.317900],[6.375818],[7.375580],[-7.656672],[9.512494],[-7.139185],[-0.621240],[-8.112282],[-8.599868],[7.149179],[8.343074],[6.403995],[-9.237086],[-8.198010],[-3.066050],[-0.671279],[-8.768905],[-8.014251],[6.656441],[8.987704],[-3.167829],[4.536089],[3.192952],[-8.803577],[9.084254],[-8.910238],[-5.262346],[3.417824],[-6.452431],[4.815990],[-3.911458],[5.010321],[2.941224],[-3.650518],[-0.766724],[8.788160],[-8.469534],[7.797184],[6.466087],[2.786275],[1.770848],[2.089003],[2.964326],[-8.044305],[-7.684984],[9.712054],[9.182287],[7.825071],[-6.866297],[-4.627175],[0.894887],[6.301819],[-7.763336],[8.608806],[-3.288120],[5.748540],[-5.071278],[4.072865],[4.970147],[-7.205110],[2.434074],[0.811581],[-5.054504],[3.421975],[-5.670563],[2.491514],[-5.114248],[1.930989],[8.726124],[-1.524646],[-4.109432],[1.835518],[-6.011604],[-1.765157],[-7.339287],[4.828695],[-9.259951],[5.916003],[3.229849],[0.930609],[-4.783939],[1.171091],[-6.432754],[8.946680],[-3.606089],[7.707919],[7.077789],[2.806751],[-3.141201],[-8.520658],[-8.755066],[-6.862185],[-7.987607],[3.056686],[9.982395],[6.028068],[5.645453],[-0.350555],[-8.364036],[5.928512],[7.846052],[1.049378],[0.780894],[-5.816803],[-7.982597],[9.471690]], dtype = "float32")#candidate|5036|(405, 1)|const|float32
call_5035 = relay.TupleGetItem(func_1480_call(relay.reshape(const_5036.astype('float32'), [9, 3, 15])), 0)
call_5037 = relay.TupleGetItem(func_1483_call(relay.reshape(const_5036.astype('float32'), [9, 3, 15])), 0)
bop_5044 = relay.logical_and(const_5036.astype('bool'), call_5029.astype('bool')) # shape=(9, 405, 15)
bop_5047 = relay.logical_and(const_5036.astype('bool'), call_5030.astype('bool')) # shape=(9, 405, 15)
uop_5048 = relay.tan(bop_5044.astype('float32')) # shape=(9, 405, 15)
uop_5050 = relay.tan(bop_5047.astype('float32')) # shape=(9, 405, 15)
output = relay.Tuple([call_5035,uop_5048,])
output2 = relay.Tuple([call_5037,uop_5050,])
func_5052 = relay.Function([], output)
mod['func_5052'] = func_5052
mod = relay.transform.InferType()(mod)
mutated_mod['func_5052'] = func_5052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5052_call = mutated_mod.get_global_var('func_5052')
call_5053 = func_5052_call()
output = call_5053
func_5054 = relay.Function([], output)
mutated_mod['func_5054'] = func_5054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4412_call = mod.get_global_var('func_4412')
func_4414_call = mutated_mod.get_global_var('func_4414')
call_5144 = func_4412_call()
call_5145 = func_4412_call()
var_5146 = relay.var("var_5146", dtype = "float64", shape = (15, 9, 2))#candidate|5146|(15, 9, 2)|var|float64
bop_5147 = relay.bitwise_or(call_5144.astype('uint16'), relay.reshape(var_5146.astype('uint16'), relay.shape_of(call_5144))) # shape=(15, 9, 2)
bop_5150 = relay.bitwise_or(call_5145.astype('uint16'), relay.reshape(var_5146.astype('uint16'), relay.shape_of(call_5145))) # shape=(15, 9, 2)
output = bop_5147
output2 = bop_5150
func_5163 = relay.Function([var_5146,], output)
mod['func_5163'] = func_5163
mod = relay.transform.InferType()(mod)
mutated_mod['func_5163'] = func_5163
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5164 = relay.var("var_5164", dtype = "float64", shape = (15, 9, 2))#candidate|5164|(15, 9, 2)|var|float64
func_5163_call = mutated_mod.get_global_var('func_5163')
call_5165 = func_5163_call(var_5164)
output = call_5165
func_5166 = relay.Function([var_5164], output)
mutated_mod['func_5166'] = func_5166
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5175 = relay.var("var_5175", dtype = "int32", shape = (7, 16, 15))#candidate|5175|(7, 16, 15)|var|int32
const_5176 = relay.const([[[-10,-3,-7,2,-7,-6,3,-1,-8,10,7,-8,-10,6,4],[5,5,5,-10,-6,1,5,9,4,4,-7,1,-9,-2,5],[3,7,6,7,-10,-7,6,4,8,5,1,5,7,-5,9],[4,7,-9,5,3,1,-6,-9,-6,-8,1,5,3,9,1],[-7,-1,6,1,8,-7,-3,-9,5,1,6,-5,9,-3,6],[-6,8,-9,-9,-8,-4,9,-9,-2,-4,8,-5,3,2,2],[-1,-1,8,-5,-2,-8,-1,-4,3,-5,-6,-9,7,-7,-7],[7,9,-8,9,6,8,6,10,10,-5,-2,-7,4,-2,-10],[-9,-6,-4,7,-8,5,-8,-7,-2,-4,9,7,-7,-7,1],[-8,4,-1,10,2,-3,-8,-9,-1,-2,-5,1,7,5,8],[3,10,-2,8,1,2,6,-8,4,5,4,-7,3,4,-9],[-6,8,2,9,4,9,-5,-7,-1,2,-7,7,1,7,10],[6,10,3,8,1,1,9,6,-9,-8,-2,-5,-8,-1,-2],[3,-8,-3,-5,3,2,-6,2,-8,-9,-9,-1,4,-3,-4],[-7,-2,-10,-7,6,10,6,1,-10,-8,-5,-1,-3,6,9],[10,9,-2,9,-1,-1,-2,-9,-6,2,-9,1,5,-7,10]],[[3,4,4,-8,-7,-7,-3,7,4,10,-5,4,1,10,2],[-3,-1,-6,5,9,6,10,5,-9,1,6,10,-2,9,8],[3,6,-10,-1,8,-7,-8,-4,-6,-3,-6,-3,-6,7,8],[-7,-7,-6,-7,4,-9,-2,9,9,10,-6,-8,3,5,-1],[5,3,3,9,-8,-9,-5,3,8,-1,3,-7,8,7,9],[-6,8,-6,-1,-4,9,8,-4,-8,-1,3,10,-5,9,10],[9,-2,-9,9,7,-1,-7,-10,7,3,1,-4,-7,7,-2],[-4,5,10,-8,4,-2,-2,3,10,-2,-10,1,3,-4,4],[9,6,5,10,5,-7,-10,-6,10,2,8,-6,7,-9,-2],[-6,-2,-9,-6,-10,-4,8,7,6,7,-9,4,-8,-7,-2],[9,-9,10,-9,6,7,-6,3,-8,-3,9,-2,9,3,-8],[-2,5,-9,1,1,-5,9,-5,7,3,10,3,-4,3,-6],[-4,-7,2,-2,-2,-2,3,-10,-4,-4,10,9,-6,-4,2],[-10,-2,3,-1,-9,-2,-1,2,5,-2,-5,3,-4,8,-7],[-1,5,4,-7,7,-7,7,-5,-1,7,9,6,7,-10,9],[5,6,1,-10,-2,-4,-5,1,2,-10,5,-2,-1,10,-5]],[[-1,-1,8,7,-10,-4,-10,-5,-1,-2,5,-2,10,-7,-7],[1,3,-6,-4,1,-2,10,6,-4,4,9,7,8,5,10],[-10,-3,-3,-3,2,4,-9,-9,-2,3,10,7,3,5,-3],[-1,5,5,3,-8,-10,-8,-9,-5,9,-8,1,-8,-3,2],[9,-10,-9,6,-2,6,7,2,-10,-8,6,2,3,2,5],[5,-9,-10,-9,10,-1,5,10,-5,-4,-3,-8,6,5,9],[-3,-3,9,-1,-8,-2,-7,6,-2,-10,-3,-7,-8,-2,2],[-10,-6,-7,6,3,-1,2,2,7,-8,-10,-2,2,9,-10],[7,-6,-4,-8,-3,6,-8,3,-6,-3,1,-5,-2,10,1],[4,3,1,-3,10,3,-1,4,-10,6,5,9,-10,-7,2],[-2,5,6,-3,-6,6,-8,-2,-1,-3,8,-6,-7,7,7],[-1,-8,2,-4,-3,-7,2,6,-6,-4,7,6,-8,10,-7],[7,-5,4,-8,-4,9,-10,5,-2,-4,-1,-8,-6,9,6],[-4,2,7,-9,-2,-8,4,-1,5,-1,10,1,8,8,5],[1,-4,-1,1,-8,4,-6,-3,9,-10,8,-2,-8,8,8],[-8,5,4,-5,-7,-9,-8,-9,-10,8,9,-10,4,-3,-5]],[[-6,-2,7,6,-2,-6,3,-4,6,1,5,-1,-2,4,9],[-4,2,-5,-3,-2,5,-4,5,-1,3,6,-3,-3,-2,-8],[-4,-6,-10,5,4,-8,9,-7,9,5,1,8,-8,1,-5],[1,-3,6,-1,-9,-2,4,-9,6,-1,10,4,-8,-8,-2],[-7,-4,3,-6,-5,-9,-3,6,6,-2,5,-8,7,-9,4],[1,8,4,7,8,-6,-9,-2,5,-9,4,6,-10,10,9],[5,-7,-5,-6,10,6,-1,-7,2,-10,8,4,7,-8,-5],[3,8,3,-9,-8,5,7,9,-6,5,-1,-9,6,10,3],[2,5,5,3,-9,5,7,9,-5,8,-10,-4,5,-4,-5],[-10,4,6,5,5,10,-9,1,4,2,9,-2,-2,-6,-2],[5,9,9,-9,5,-2,4,-4,9,5,10,5,9,-9,-4],[-8,-4,8,-2,-2,9,-4,5,-9,5,-6,-8,-9,8,3],[-10,3,-8,1,-6,-9,-7,9,10,-4,2,4,-3,-8,-2],[7,2,7,-8,1,1,10,-2,10,7,-9,-6,-10,5,-3],[8,8,-7,1,-5,-3,4,-4,4,-10,-8,1,-1,6,-6],[-4,7,6,9,3,-2,10,-2,4,-6,7,3,-1,-7,-2]],[[-4,-9,10,-8,5,-3,-8,4,-7,5,3,1,-8,-10,-7],[-9,-1,-3,4,-2,-3,-7,-9,-2,-9,10,-9,-8,1,-3],[2,-1,-10,6,6,-6,-4,-9,-4,-7,-7,7,-10,-2,-6],[-1,-9,-3,-7,-5,-8,9,4,3,8,-2,-9,-1,-5,9],[-10,-2,-3,7,6,10,-5,-6,-8,6,8,-2,-7,5,-6],[5,-5,4,-2,9,-5,1,-9,-8,5,4,1,10,9,-10],[-2,-2,2,6,-8,-3,5,4,3,2,3,-1,1,2,9],[-6,7,-7,-5,4,-7,8,-2,-7,-2,1,4,-2,5,7],[-8,-2,-1,5,-1,9,7,-1,10,4,-6,9,-6,5,7],[-5,4,-1,6,1,6,-5,-9,-3,-2,-3,1,8,-5,9],[6,-8,-1,5,6,3,8,-6,-4,-6,-6,-7,-10,-4,-10],[8,7,6,6,3,9,-3,-6,2,10,8,-4,2,-8,9],[-9,3,3,-4,-3,1,5,-9,-5,-10,-10,10,1,-7,10],[8,5,5,-5,6,-8,-9,3,3,-10,2,3,-3,-7,5],[8,-7,9,10,-3,-1,5,5,10,5,-2,10,-2,10,-5],[5,2,-8,-3,4,-7,8,-5,-10,-2,-6,4,2,1,5]],[[8,-1,1,-1,8,-2,-10,-6,5,3,3,-2,5,2,5],[-2,-7,-5,-10,5,-2,2,-9,-1,6,-2,3,-5,9,4],[7,8,9,-2,-8,7,-6,-5,9,1,-10,-4,8,-1,9],[10,-1,7,2,1,8,1,8,1,4,1,-7,-6,4,-4],[3,6,2,6,-7,-3,4,1,2,7,5,9,-3,-7,-4],[-10,4,-1,-3,2,3,-5,3,-6,9,10,-1,6,-6,3],[-5,-7,8,9,6,-1,1,3,-3,9,-2,6,2,9,8],[-7,4,-3,-3,-4,-6,-7,1,10,-1,-6,2,8,5,-3],[1,5,4,-10,2,8,-10,-6,-5,5,-9,-10,-4,-6,-8],[-1,7,-8,7,1,-1,9,2,-4,-6,-4,1,-6,2,3],[9,3,-1,-10,-9,8,-10,3,4,10,6,5,-7,2,2],[-3,9,-10,7,9,-1,-5,-3,2,6,7,5,1,2,-3],[-1,7,2,-2,-7,2,5,-8,8,8,-1,7,-7,-10,-2],[-3,-9,4,-6,-8,-5,-1,-10,1,-9,1,3,8,6,9],[2,2,-10,1,-3,1,1,-10,-8,-8,-1,-9,-7,-6,-6],[1,-7,-7,1,5,9,2,5,-3,-5,2,-2,-2,-9,-1]],[[3,2,7,7,1,2,9,2,-5,8,5,-8,2,-5,-8],[7,10,-9,1,5,-9,4,10,-1,8,-9,-1,10,-6,-8],[3,6,-7,2,-3,1,-3,-10,-8,2,-10,1,-7,-9,-7],[-7,-2,-4,8,-6,5,2,2,-3,-3,-10,-5,6,-3,-4],[2,1,-6,3,-2,-6,-8,-5,10,-3,-4,-8,4,-2,1],[-7,7,8,-4,-9,2,3,6,2,-9,-9,-8,3,-2,-10],[1,5,3,3,-4,6,-10,8,9,1,5,-3,8,-8,1],[1,-3,-1,-10,6,9,-2,10,-4,-1,9,7,-10,9,3],[-6,-3,-3,-7,-9,10,4,-8,3,-5,8,-10,-5,-10,-10],[4,1,5,2,-8,-7,-8,10,7,-9,-8,6,2,8,-6],[8,4,-9,-3,3,9,-8,10,4,-1,-10,10,7,-9,-5],[-3,7,2,8,-5,7,-10,-3,-2,10,10,4,-5,-1,6],[-1,10,-6,-2,-8,-5,2,-9,-6,4,6,-5,3,1,-6],[1,-6,5,-3,-6,5,5,7,-2,7,-10,-1,5,-6,-7],[5,-10,-7,3,-2,-1,10,-4,-2,-1,-4,3,-5,7,-9],[4,2,-5,8,9,8,-7,-7,-7,-7,7,-9,-7,3,6]]], dtype = "int32")#candidate|5176|(7, 16, 15)|const|int32
bop_5177 = relay.greater_equal(var_5175.astype('bool'), relay.reshape(const_5176.astype('bool'), relay.shape_of(var_5175))) # shape=(7, 16, 15)
output = bop_5177
output2 = bop_5177
func_5181 = relay.Function([var_5175,], output)
mod['func_5181'] = func_5181
mod = relay.transform.InferType()(mod)
mutated_mod['func_5181'] = func_5181
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5182 = relay.var("var_5182", dtype = "int32", shape = (7, 16, 15))#candidate|5182|(7, 16, 15)|var|int32
func_5181_call = mutated_mod.get_global_var('func_5181')
call_5183 = func_5181_call(var_5182)
output = call_5183
func_5184 = relay.Function([var_5182], output)
mutated_mod['func_5184'] = func_5184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5250 = relay.var("var_5250", dtype = "float32", shape = (13, 3, 16))#candidate|5250|(13, 3, 16)|var|float32
var_5251 = relay.var("var_5251", dtype = "float32", shape = (13, 3, 16))#candidate|5251|(13, 3, 16)|var|float32
bop_5252 = relay.greater_equal(var_5250.astype('bool'), relay.reshape(var_5251.astype('bool'), relay.shape_of(var_5250))) # shape=(13, 3, 16)
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
const_5257 = relay.const([-6.371210,-0.469112,1.475408,-3.582472,-8.712242,9.205054,4.280346,-2.991364,-5.024690,-2.060917,9.230296,-3.890905,-9.592385,-0.478835,-1.775236,-1.350489,1.428686,-3.437151,6.705620,-8.756928,-5.386102,5.758482,4.235375,6.762878,-3.966528,2.525294,-2.173258,-5.677367,-1.235367,-3.445341,5.153342,0.764166,-9.615408,-6.689709,-2.491348,8.367292,-2.526654,-8.976390,-8.046449,8.339981,1.943712,1.428335,-0.239513,-3.252164,-6.117881,8.355590,-4.611709,7.488027,-9.677405,-7.751303,-9.816410,4.977100,5.944557,4.117408,1.271875,-5.954278,8.441059,-4.915597,1.824841,-0.128441,5.900401,-6.212884,-1.009289,-4.088259,4.678457,7.416830,-5.171245,-3.064505,-9.014700,-7.609760,-7.555328,4.204978,-4.701735,6.714522,-7.361964,9.444280,1.000020,6.120226,3.397291,-2.201720,3.873486,9.404127,-6.827771,3.964826,3.153416,-1.840443,-7.250619,6.850162,2.386518,7.167152,1.242142,7.384348,-2.531046,-6.352899,3.281986,-4.333901,3.086239,-0.719022,1.616332,-5.925612,0.734854,-1.953996,-4.275512,-2.824824,-2.822610,-2.225077,5.092966,-9.229673,-3.896069,5.221908,0.969888,-8.671054,4.164158,-2.977775,-5.948688,8.269344,6.597572,-0.729005,-5.283019,4.736960,-0.825871,-2.403328,6.402636,1.987920,7.329773,8.851612,-7.581440,0.416709,3.122211,-7.905536,0.946014,2.469737,1.702148,-3.057186,9.256175], dtype = "float32")#candidate|5257|(135,)|const|float32
call_5256 = relay.TupleGetItem(func_435_call(relay.reshape(const_5257.astype('float32'), [3, 45])), 0)
call_5258 = relay.TupleGetItem(func_438_call(relay.reshape(const_5257.astype('float32'), [3, 45])), 0)
func_1086_call = mod.get_global_var('func_1086')
func_1088_call = mutated_mod.get_global_var('func_1088')
call_5260 = relay.TupleGetItem(func_1086_call(), 0)
call_5261 = relay.TupleGetItem(func_1088_call(), 0)
output = relay.Tuple([bop_5252,call_5256,const_5257,call_5260,])
output2 = relay.Tuple([bop_5252,call_5258,const_5257,call_5261,])
func_5266 = relay.Function([var_5250,var_5251,], output)
mod['func_5266'] = func_5266
mod = relay.transform.InferType()(mod)
mutated_mod['func_5266'] = func_5266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5266_call = mutated_mod.get_global_var('func_5266')
var_5268 = relay.var("var_5268", dtype = "float32", shape = (13, 3, 16))#candidate|5268|(13, 3, 16)|var|float32
var_5269 = relay.var("var_5269", dtype = "float32", shape = (13, 3, 16))#candidate|5269|(13, 3, 16)|var|float32
call_5267 = func_5266_call(var_5268,var_5269,)
output = call_5267
func_5270 = relay.Function([var_5268,var_5269,], output)
mutated_mod['func_5270'] = func_5270
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5283 = relay.const(-6, dtype = "uint32")#candidate|5283|()|const|uint32
var_5284 = relay.var("var_5284", dtype = "uint32", shape = (2, 16, 14))#candidate|5284|(2, 16, 14)|var|uint32
bop_5285 = relay.bitwise_or(const_5283.astype('uint32'), var_5284.astype('uint32')) # shape=(2, 16, 14)
output = relay.Tuple([bop_5285,])
output2 = relay.Tuple([bop_5285,])
func_5294 = relay.Function([var_5284,], output)
mod['func_5294'] = func_5294
mod = relay.transform.InferType()(mod)
var_5295 = relay.var("var_5295", dtype = "uint32", shape = (2, 16, 14))#candidate|5295|(2, 16, 14)|var|uint32
output = func_5294(var_5295)
func_5296 = relay.Function([var_5295], output)
mutated_mod['func_5296'] = func_5296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1086_call = mod.get_global_var('func_1086')
func_1088_call = mutated_mod.get_global_var('func_1088')
call_5385 = relay.TupleGetItem(func_1086_call(), 0)
call_5386 = relay.TupleGetItem(func_1088_call(), 0)
output = relay.Tuple([call_5385,])
output2 = relay.Tuple([call_5386,])
func_5400 = relay.Function([], output)
mod['func_5400'] = func_5400
mod = relay.transform.InferType()(mod)
mutated_mod['func_5400'] = func_5400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5400_call = mutated_mod.get_global_var('func_5400')
call_5401 = func_5400_call()
output = call_5401
func_5402 = relay.Function([], output)
mutated_mod['func_5402'] = func_5402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5052_call = mod.get_global_var('func_5052')
func_5054_call = mutated_mod.get_global_var('func_5054')
call_5405 = relay.TupleGetItem(func_5052_call(), 1)
call_5406 = relay.TupleGetItem(func_5054_call(), 1)
output = call_5405
output2 = call_5406
func_5409 = relay.Function([], output)
mod['func_5409'] = func_5409
mod = relay.transform.InferType()(mod)
output = func_5409()
func_5410 = relay.Function([], output)
mutated_mod['func_5410'] = func_5410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5409_call = mod.get_global_var('func_5409')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_5411 = func_5409_call()
call_5412 = func_5409_call()
output = relay.Tuple([call_5411,])
output2 = relay.Tuple([call_5412,])
func_5414 = relay.Function([], output)
mod['func_5414'] = func_5414
mod = relay.transform.InferType()(mod)
output = func_5414()
func_5415 = relay.Function([], output)
mutated_mod['func_5415'] = func_5415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_625_call = mod.get_global_var('func_625')
func_626_call = mutated_mod.get_global_var('func_626')
call_5416 = relay.TupleGetItem(func_625_call(), 1)
call_5417 = relay.TupleGetItem(func_626_call(), 1)
output = call_5416
output2 = call_5417
func_5418 = relay.Function([], output)
mod['func_5418'] = func_5418
mod = relay.transform.InferType()(mod)
mutated_mod['func_5418'] = func_5418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5418_call = mutated_mod.get_global_var('func_5418')
call_5419 = func_5418_call()
output = call_5419
func_5420 = relay.Function([], output)
mutated_mod['func_5420'] = func_5420
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5453 = relay.var("var_5453", dtype = "int64", shape = ())#candidate|5453|()|var|int64
var_5454 = relay.var("var_5454", dtype = "int64", shape = (5, 11, 9))#candidate|5454|(5, 11, 9)|var|int64
bop_5455 = relay.maximum(var_5453.astype('int64'), var_5454.astype('int64')) # shape=(5, 11, 9)
func_2360_call = mod.get_global_var('func_2360')
func_2361_call = mutated_mod.get_global_var('func_2361')
call_5474 = relay.TupleGetItem(func_2360_call(), 0)
call_5475 = relay.TupleGetItem(func_2361_call(), 0)
output = relay.Tuple([bop_5455,call_5474,])
output2 = relay.Tuple([bop_5455,call_5475,])
func_5483 = relay.Function([var_5453,var_5454,], output)
mod['func_5483'] = func_5483
mod = relay.transform.InferType()(mod)
var_5484 = relay.var("var_5484", dtype = "int64", shape = ())#candidate|5484|()|var|int64
var_5485 = relay.var("var_5485", dtype = "int64", shape = (5, 11, 9))#candidate|5485|(5, 11, 9)|var|int64
output = func_5483(var_5484,var_5485,)
func_5486 = relay.Function([var_5484,var_5485,], output)
mutated_mod['func_5486'] = func_5486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3795_call = mod.get_global_var('func_3795')
func_3796_call = mutated_mod.get_global_var('func_3796')
call_5505 = func_3795_call()
call_5506 = func_3795_call()
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_5530 = relay.TupleGetItem(func_225_call(), 0)
call_5531 = relay.TupleGetItem(func_226_call(), 0)
output = relay.Tuple([call_5505,call_5530,])
output2 = relay.Tuple([call_5506,call_5531,])
func_5548 = relay.Function([], output)
mod['func_5548'] = func_5548
mod = relay.transform.InferType()(mod)
output = func_5548()
func_5549 = relay.Function([], output)
mutated_mod['func_5549'] = func_5549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1970_call = mod.get_global_var('func_1970')
func_1971_call = mutated_mod.get_global_var('func_1971')
call_5550 = func_1970_call()
call_5551 = func_1970_call()
const_5560 = relay.const([[[4.862774,-8.747867],[3.163576,5.025196],[6.723258,-8.698817],[-6.320870,6.169898]],[[7.830296,-6.753342],[7.815057,8.444290],[2.289636,1.870544],[-7.126938,-7.010227]],[[-6.654107,-8.325934],[5.835475,-4.288956],[-2.570804,5.534214],[-8.882060,-4.694634]],[[6.047148,0.884489],[-7.061642,-1.237965],[-8.723816,1.669612],[9.760714,-3.372099]],[[-8.257405,5.230382],[5.429241,2.894459],[-6.215350,-3.022333],[9.223741,-0.216291]]], dtype = "float32")#candidate|5560|(5, 4, 2)|const|float32
bop_5561 = relay.add(call_5550.astype('int32'), relay.reshape(const_5560.astype('int32'), relay.shape_of(call_5550))) # shape=(5, 4, 2)
bop_5564 = relay.add(call_5551.astype('int32'), relay.reshape(const_5560.astype('int32'), relay.shape_of(call_5551))) # shape=(5, 4, 2)
func_5181_call = mod.get_global_var('func_5181')
func_5184_call = mutated_mod.get_global_var('func_5184')
var_5570 = relay.var("var_5570", dtype = "int32", shape = (1680,))#candidate|5570|(1680,)|var|int32
call_5569 = func_5181_call(relay.reshape(var_5570.astype('int32'), [7, 16, 15]))
call_5571 = func_5181_call(relay.reshape(var_5570.astype('int32'), [7, 16, 15]))
output = relay.Tuple([bop_5561,call_5569,var_5570,])
output2 = relay.Tuple([bop_5564,call_5571,var_5570,])
func_5587 = relay.Function([var_5570,], output)
mod['func_5587'] = func_5587
mod = relay.transform.InferType()(mod)
var_5588 = relay.var("var_5588", dtype = "int32", shape = (1680,))#candidate|5588|(1680,)|var|int32
output = func_5587(var_5588)
func_5589 = relay.Function([var_5588], output)
mutated_mod['func_5589'] = func_5589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4304_call = mod.get_global_var('func_4304')
func_4306_call = mutated_mod.get_global_var('func_4306')
call_5591 = relay.TupleGetItem(func_4304_call(), 0)
call_5592 = relay.TupleGetItem(func_4306_call(), 0)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_5610 = relay.TupleGetItem(func_2536_call(), 2)
call_5611 = relay.TupleGetItem(func_2537_call(), 2)
output = relay.Tuple([call_5591,call_5610,])
output2 = relay.Tuple([call_5592,call_5611,])
func_5615 = relay.Function([], output)
mod['func_5615'] = func_5615
mod = relay.transform.InferType()(mod)
output = func_5615()
func_5616 = relay.Function([], output)
mutated_mod['func_5616'] = func_5616
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5625 = relay.var("var_5625", dtype = "float64", shape = (4, 10, 10))#candidate|5625|(4, 10, 10)|var|float64
var_5626 = relay.var("var_5626", dtype = "float64", shape = (4, 10, 10))#candidate|5626|(4, 10, 10)|var|float64
bop_5627 = relay.divide(var_5625.astype('float64'), relay.reshape(var_5626.astype('float64'), relay.shape_of(var_5625))) # shape=(4, 10, 10)
bop_5635 = relay.equal(var_5626.astype('bool'), relay.reshape(bop_5627.astype('bool'), relay.shape_of(var_5626))) # shape=(4, 10, 10)
bop_5638 = relay.greater(var_5625.astype('bool'), relay.reshape(bop_5627.astype('bool'), relay.shape_of(var_5625))) # shape=(4, 10, 10)
output = relay.Tuple([bop_5635,bop_5638,])
output2 = relay.Tuple([bop_5635,bop_5638,])
func_5641 = relay.Function([var_5625,var_5626,], output)
mod['func_5641'] = func_5641
mod = relay.transform.InferType()(mod)
mutated_mod['func_5641'] = func_5641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5641_call = mutated_mod.get_global_var('func_5641')
var_5643 = relay.var("var_5643", dtype = "float64", shape = (4, 10, 10))#candidate|5643|(4, 10, 10)|var|float64
var_5644 = relay.var("var_5644", dtype = "float64", shape = (4, 10, 10))#candidate|5644|(4, 10, 10)|var|float64
call_5642 = func_5641_call(var_5643,var_5644,)
output = call_5642
func_5645 = relay.Function([var_5643,var_5644,], output)
mutated_mod['func_5645'] = func_5645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5647 = relay.var("var_5647", dtype = "float32", shape = (13, 2, 13))#candidate|5647|(13, 2, 13)|var|float32
uop_5648 = relay.log(var_5647.astype('float32')) # shape=(13, 2, 13)
bop_5656 = relay.greater(var_5647.astype('bool'), relay.reshape(uop_5648.astype('bool'), relay.shape_of(var_5647))) # shape=(13, 2, 13)
output = relay.Tuple([bop_5656,])
output2 = relay.Tuple([bop_5656,])
func_5685 = relay.Function([var_5647,], output)
mod['func_5685'] = func_5685
mod = relay.transform.InferType()(mod)
mutated_mod['func_5685'] = func_5685
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5686 = relay.var("var_5686", dtype = "float32", shape = (13, 2, 13))#candidate|5686|(13, 2, 13)|var|float32
func_5685_call = mutated_mod.get_global_var('func_5685')
call_5687 = func_5685_call(var_5686)
output = call_5687
func_5688 = relay.Function([var_5686], output)
mutated_mod['func_5688'] = func_5688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1877_call = mod.get_global_var('func_1877')
func_1878_call = mutated_mod.get_global_var('func_1878')
call_5767 = relay.TupleGetItem(func_1877_call(), 0)
call_5768 = relay.TupleGetItem(func_1878_call(), 0)
var_5769 = relay.var("var_5769", dtype = "float32", shape = (16, 4, 4))#candidate|5769|(16, 4, 4)|var|float32
bop_5770 = relay.minimum(call_5767.astype('uint64'), relay.reshape(var_5769.astype('uint64'), relay.shape_of(call_5767))) # shape=(16, 4, 4)
bop_5773 = relay.minimum(call_5768.astype('uint64'), relay.reshape(var_5769.astype('uint64'), relay.shape_of(call_5768))) # shape=(16, 4, 4)
func_663_call = mod.get_global_var('func_663')
func_665_call = mutated_mod.get_global_var('func_665')
call_5787 = func_663_call()
call_5788 = func_663_call()
output = relay.Tuple([bop_5770,call_5787,])
output2 = relay.Tuple([bop_5773,call_5788,])
func_5795 = relay.Function([var_5769,], output)
mod['func_5795'] = func_5795
mod = relay.transform.InferType()(mod)
mutated_mod['func_5795'] = func_5795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5796 = relay.var("var_5796", dtype = "float32", shape = (16, 4, 4))#candidate|5796|(16, 4, 4)|var|float32
func_5795_call = mutated_mod.get_global_var('func_5795')
call_5797 = func_5795_call(var_5796)
output = call_5797
func_5798 = relay.Function([var_5796], output)
mutated_mod['func_5798'] = func_5798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_814_call = mutated_mod.get_global_var('func_814')
call_5869 = func_813_call()
call_5870 = func_813_call()
func_1656_call = mod.get_global_var('func_1656')
func_1658_call = mutated_mod.get_global_var('func_1658')
call_5877 = func_1656_call()
call_5878 = func_1656_call()
func_5587_call = mod.get_global_var('func_5587')
func_5589_call = mutated_mod.get_global_var('func_5589')
var_5882 = relay.var("var_5882", dtype = "int32", shape = (1680,))#candidate|5882|(1680,)|var|int32
call_5881 = relay.TupleGetItem(func_5587_call(relay.reshape(var_5882.astype('int32'), [1680,])), 2)
call_5883 = relay.TupleGetItem(func_5589_call(relay.reshape(var_5882.astype('int32'), [1680,])), 2)
output = relay.Tuple([call_5869,call_5877,call_5881,var_5882,])
output2 = relay.Tuple([call_5870,call_5878,call_5883,var_5882,])
func_5893 = relay.Function([var_5882,], output)
mod['func_5893'] = func_5893
mod = relay.transform.InferType()(mod)
mutated_mod['func_5893'] = func_5893
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5894 = relay.var("var_5894", dtype = "int32", shape = (1680,))#candidate|5894|(1680,)|var|int32
func_5893_call = mutated_mod.get_global_var('func_5893')
call_5895 = func_5893_call(var_5894)
output = call_5895
func_5896 = relay.Function([var_5894], output)
mutated_mod['func_5896'] = func_5896
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5909 = relay.var("var_5909", dtype = "uint64", shape = (10, 6, 4))#candidate|5909|(10, 6, 4)|var|uint64
const_5910 = relay.const([[[4,1,3,-3],[4,2,2,-10],[3,-2,6,8],[-7,-1,7,-10],[-6,-10,-2,5],[-6,-7,-8,-7]],[[-9,-5,5,7],[4,-2,5,-3],[-2,-3,5,-10],[4,-7,4,-7],[-5,10,-4,1],[-4,-8,-4,4]],[[-3,10,-5,-6],[10,3,-9,9],[-1,-3,5,-4],[8,9,-4,-8],[10,-4,10,3],[-5,-6,-7,10]],[[1,4,9,6],[-1,-9,-10,1],[-5,-4,-4,5],[-3,6,5,9],[-1,-3,-2,-8],[-5,-9,6,-4]],[[4,-5,5,10],[10,-10,-3,-2],[-4,5,-3,-1],[3,-5,8,7],[-9,2,4,-2],[5,-1,10,5]],[[8,10,-4,-10],[-10,4,-6,2],[7,1,-4,-8],[-6,-9,2,-2],[5,-2,4,-6],[10,-2,2,2]],[[-8,1,-8,2],[9,10,-7,-4],[4,-1,-9,-1],[-8,-5,-9,-10],[-2,10,1,3],[5,-1,-6,7]],[[2,-8,-5,-10],[-4,-3,-6,1],[-5,7,4,6],[-3,-6,-4,9],[-8,-7,-6,4],[-5,-6,-10,-8]],[[-9,-3,-7,6],[7,-9,2,-9],[4,3,-4,-3],[-6,10,7,2],[-7,1,-3,-5],[1,-1,3,5]],[[-7,-9,-9,-2],[3,-10,-3,6],[-5,-3,-6,-9],[2,9,-2,-3],[5,2,6,7],[-7,10,9,-10]]], dtype = "uint64")#candidate|5910|(10, 6, 4)|const|uint64
bop_5911 = relay.greater_equal(var_5909.astype('bool'), relay.reshape(const_5910.astype('bool'), relay.shape_of(var_5909))) # shape=(10, 6, 4)
func_2543_call = mod.get_global_var('func_2543')
func_2545_call = mutated_mod.get_global_var('func_2545')
call_5923 = relay.TupleGetItem(func_2543_call(), 0)
call_5924 = relay.TupleGetItem(func_2545_call(), 0)
func_5641_call = mod.get_global_var('func_5641')
func_5645_call = mutated_mod.get_global_var('func_5645')
const_5926 = relay.const([5.451139,8.330836,1.439376,5.515346,0.169572,5.963232,-0.863677,-2.105818,6.741028,-3.920514,1.589647,9.194788,6.012630,6.235152,-2.440519,-6.678982,3.977151,6.077870,8.005808,-5.218334,7.621607,1.458550,3.806958,-6.388588,-9.317802,2.420650,-2.132289,-2.344594,3.621540,-2.452140,-5.960626,8.705639,-4.565838,-1.152364,0.260824,-5.066424,-0.770608,0.132779,6.249940,-3.734579,-9.522229,6.648638,-3.760262,2.465938,1.373517,3.735792,-4.946530,-8.669129,-8.565781,9.903746,3.847542,-2.201932,8.956663,0.603811,5.537788,-3.149532,3.969993,-9.909707,1.990754,-4.132713,4.342821,-0.760879,-1.513245,-3.194058,0.008551,6.013830,1.198534,-2.447247,3.790279,5.689786,0.767018,-0.270740,-4.186383,9.048724,-8.318065,-5.165856,3.254044,-2.956777,2.928656,-5.947614,-4.017014,3.226789,4.658197,-4.687626,7.681252,-9.760359,7.605992,-8.394428,3.402710,2.378306,9.659581,-9.810622,-1.753150,-2.421784,7.847758,-2.240016,-1.367836,-0.239661,2.517602,-5.070095,-8.618524,5.684454,-7.973072,3.121693,0.815980,9.585060,8.009179,-7.152665,-4.819157,8.463008,0.148514,0.488854,-6.727073,-1.741798,-5.441083,-8.886687,4.032571,-4.887401,9.753466,7.806204,-1.298759,9.761596,-8.438607,1.418291,3.598349,3.980055,-1.105446,-9.861355,-0.129202,-4.451355,-5.286800,9.893833,8.356970,3.419475,-6.928511,6.443934,5.775393,-6.076925,-2.804637,9.632839,-3.878115,1.400878,2.023762,7.790054,-9.418811,7.587366,0.523830,-6.400370,-4.249813,0.338336,-3.968457,-1.232549,-3.504611,-3.322505,-2.727991,-5.089993,-1.011858,-3.089116,9.311286,7.166453,7.915284,-6.594023,8.736954,2.702071,-2.382276,-3.431352,-5.766984,6.821178,3.731647,8.191557,8.848100,6.093703,4.221999,6.599943,6.336725,-9.915678,5.182185,1.298208,6.828051,0.106591,-4.594310,3.272256,-4.235300,3.541220,-9.323374,7.155761,-5.955820,7.618440,-1.579340,-1.770567,8.101280,1.762274,-1.011582,4.506121,8.622869,5.388290,4.535278,-2.555336,2.550788,1.723235,8.842311,7.112785,3.960467,5.735646,-0.619954,-8.464612,3.232948,-5.652578,-8.240127,3.037614,-3.835519,6.376375,6.935740,7.958824,3.966031,-7.753289,-9.778723,-2.441382,-8.709225,9.472468,-1.178339,-4.396017,1.341706,7.519054,1.764485,-1.650722,5.309865,2.475731,5.110394,-5.366347,7.263584,7.052628,-2.946663,-2.028012,-0.385921,3.911455,8.086646,-1.686117,8.624329,-2.636984,-6.376570,-0.622927,4.478944,1.893566,8.669902,3.804256,-0.019558,-7.436419,9.029314,-9.907105,-6.082475,-5.730281,7.492156,9.788025,-0.245186,8.392039,-3.184519,-1.120015,4.748803,-3.720942,8.542385,-3.834826,7.613330,4.202201,7.088775,-1.988009,9.258136,6.835807,5.869659,7.015670,-0.996760,-8.927000,1.103405,-2.470207,-1.764792,3.142527,9.461558,-4.976953,-9.832480,4.392709,3.683893,4.144959,-4.180885,5.604420,2.602964,0.267731,-2.870673,-4.748879,-4.651448,-0.713629,-1.193775,5.911429,9.783958,-6.597385,2.742543,2.254025,7.762582,6.023988,0.278480,3.599189,-5.469201,0.025635,-2.490298,-8.555044,-5.001483,-6.176293,-3.599278,-2.917109,3.382419,9.173137,-9.092794,8.657218,3.045017,5.159475,6.769391,-5.725736,1.714456,-9.745074,7.067760,8.950242,-4.539118,-3.982666,1.105983,-7.204774,0.414797,1.384950,6.415743,9.659993,0.934562,8.760043,0.112982,-9.466289,8.720172,1.662391,3.648400,6.932641,-5.336048,-6.231771,-0.526969,-6.286564,-9.144654,-4.208245,-6.240457,9.452868,-4.748460,-4.241211,-5.488400,1.110972,-2.688439,-6.486962,0.303316,0.407018,-7.659171,3.573348,-5.175940,-3.923531,6.234089,-5.279051,1.403549,7.828963,0.909730,4.746775,3.218034,0.981152,4.871362,5.281903,9.061968,-3.201096,8.485763,6.098999,6.799986,-7.458595,-0.367892,-4.791946,-4.213986,5.617779,-8.741239,5.996187,7.053161,2.167576,8.937551,8.862565,0.339618,-4.781541,4.703351,-8.478362,4.118381,0.623028,-7.312974,5.837901,-5.220763,-3.229250,-7.840297,-9.941938,-7.913156,-5.941798,-8.521928,0.970685,-8.334126,-4.223442], dtype = "float64")#candidate|5926|(400,)|const|float64
call_5925 = relay.TupleGetItem(func_5641_call(relay.reshape(const_5926.astype('float64'), [4, 10, 10]), relay.reshape(const_5926.astype('float64'), [4, 10, 10]), ), 0)
call_5927 = relay.TupleGetItem(func_5645_call(relay.reshape(const_5926.astype('float64'), [4, 10, 10]), relay.reshape(const_5926.astype('float64'), [4, 10, 10]), ), 0)
output = relay.Tuple([bop_5911,call_5923,call_5925,const_5926,])
output2 = relay.Tuple([bop_5911,call_5924,call_5927,const_5926,])
func_5928 = relay.Function([var_5909,], output)
mod['func_5928'] = func_5928
mod = relay.transform.InferType()(mod)
var_5929 = relay.var("var_5929", dtype = "uint64", shape = (10, 6, 4))#candidate|5929|(10, 6, 4)|var|uint64
output = func_5928(var_5929)
func_5930 = relay.Function([var_5929], output)
mutated_mod['func_5930'] = func_5930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_5934 = func_5418_call()
call_5935 = func_5418_call()
output = relay.Tuple([call_5934,])
output2 = relay.Tuple([call_5935,])
func_5938 = relay.Function([], output)
mod['func_5938'] = func_5938
mod = relay.transform.InferType()(mod)
output = func_5938()
func_5939 = relay.Function([], output)
mutated_mod['func_5939'] = func_5939
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6025 = relay.const([[[-4,-9,-3,-2,6,-5]],[[-8,9,-4,-7,6,9]],[[-9,-4,8,9,2,1]],[[-3,-2,-8,1,1,-2]],[[-6,9,2,-5,-1,-8]],[[-5,-1,6,-2,4,-6]],[[-10,-2,7,-7,-2,7]],[[6,-7,-1,8,-3,-2]],[[-10,6,8,-10,-10,-1]],[[-4,-2,-9,-2,-10,-2]]], dtype = "int32")#candidate|6025|(10, 1, 6)|const|int32
var_6026 = relay.var("var_6026", dtype = "int32", shape = (10, 1, 6))#candidate|6026|(10, 1, 6)|var|int32
bop_6027 = relay.less(const_6025.astype('bool'), relay.reshape(var_6026.astype('bool'), relay.shape_of(const_6025))) # shape=(10, 1, 6)
bop_6038 = relay.bitwise_xor(const_6025.astype('uint16'), relay.reshape(bop_6027.astype('uint16'), relay.shape_of(const_6025))) # shape=(10, 1, 6)
func_2896_call = mod.get_global_var('func_2896')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_6041 = relay.TupleGetItem(func_2896_call(), 0)
call_6042 = relay.TupleGetItem(func_2897_call(), 0)
uop_6047 = relay.sigmoid(bop_6038.astype('float32')) # shape=(10, 1, 6)
bop_6050 = relay.minimum(uop_6047.astype('float64'), relay.reshape(bop_6038.astype('float64'), relay.shape_of(uop_6047))) # shape=(10, 1, 6)
uop_6055 = relay.sqrt(uop_6047.astype('float64')) # shape=(10, 1, 6)
output = relay.Tuple([call_6041,bop_6050,uop_6055,])
output2 = relay.Tuple([call_6042,bop_6050,uop_6055,])
func_6066 = relay.Function([var_6026,], output)
mod['func_6066'] = func_6066
mod = relay.transform.InferType()(mod)
var_6067 = relay.var("var_6067", dtype = "int32", shape = (10, 1, 6))#candidate|6067|(10, 1, 6)|var|int32
output = func_6066(var_6067)
func_6068 = relay.Function([var_6067], output)
mutated_mod['func_6068'] = func_6068
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6096 = relay.var("var_6096", dtype = "float32", shape = (3, 10, 2))#candidate|6096|(3, 10, 2)|var|float32
const_6097 = relay.const([[[5.683168,-1.505647],[7.985789,2.295270],[4.568345,8.433210],[-1.351227,-6.841500],[-6.634515,-1.007327],[-8.099645,8.899649],[2.881974,-0.842948],[-2.114273,0.943010],[-9.494396,-5.160997],[-0.667382,-2.314572]],[[2.387956,7.970734],[7.955548,-6.471094],[-8.556150,4.723257],[-4.047207,5.270102],[-3.429906,9.217680],[-9.324559,8.050874],[5.882536,-1.579766],[7.811003,2.626710],[0.587346,-2.032972],[-7.697215,-9.672863]],[[-2.861225,8.314814],[-5.340549,-4.875793],[7.498686,-4.533456],[5.102015,-2.992280],[8.288063,-6.824890],[-2.425330,3.630503],[-7.586450,-4.890929],[-5.502971,8.069169],[-8.079517,4.379619],[-1.128537,-5.694606]]], dtype = "float32")#candidate|6097|(3, 10, 2)|const|float32
bop_6098 = relay.mod(var_6096.astype('float32'), relay.reshape(const_6097.astype('float32'), relay.shape_of(var_6096))) # shape=(3, 10, 2)
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
var_6112 = relay.var("var_6112", dtype = "float32", shape = (1, 135))#candidate|6112|(1, 135)|var|float32
call_6111 = relay.TupleGetItem(func_435_call(relay.reshape(var_6112.astype('float32'), [3, 45])), 2)
call_6113 = relay.TupleGetItem(func_438_call(relay.reshape(var_6112.astype('float32'), [3, 45])), 2)
output = relay.Tuple([bop_6098,call_6111,var_6112,])
output2 = relay.Tuple([bop_6098,call_6113,var_6112,])
func_6120 = relay.Function([var_6096,var_6112,], output)
mod['func_6120'] = func_6120
mod = relay.transform.InferType()(mod)
mutated_mod['func_6120'] = func_6120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6120_call = mutated_mod.get_global_var('func_6120')
var_6122 = relay.var("var_6122", dtype = "float32", shape = (3, 10, 2))#candidate|6122|(3, 10, 2)|var|float32
var_6123 = relay.var("var_6123", dtype = "float32", shape = (1, 135))#candidate|6123|(1, 135)|var|float32
call_6121 = func_6120_call(var_6122,var_6123,)
output = call_6121
func_6124 = relay.Function([var_6122,var_6123,], output)
mutated_mod['func_6124'] = func_6124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_269_call = mod.get_global_var('func_269')
func_271_call = mutated_mod.get_global_var('func_271')
call_6155 = relay.TupleGetItem(func_269_call(), 2)
call_6156 = relay.TupleGetItem(func_271_call(), 2)
output = call_6155
output2 = call_6156
func_6161 = relay.Function([], output)
mod['func_6161'] = func_6161
mod = relay.transform.InferType()(mod)
output = func_6161()
func_6162 = relay.Function([], output)
mutated_mod['func_6162'] = func_6162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5548_call = mod.get_global_var('func_5548')
func_5549_call = mutated_mod.get_global_var('func_5549')
call_6167 = relay.TupleGetItem(func_5548_call(), 1)
call_6168 = relay.TupleGetItem(func_5549_call(), 1)
func_3466_call = mod.get_global_var('func_3466')
func_3472_call = mutated_mod.get_global_var('func_3472')
const_6172 = relay.const([[3,-4],[-8,10],[10,-1],[5,2],[5,-1],[-4,-7],[-8,1],[-2,-2],[2,3],[-10,9],[10,-8],[2,-4],[-10,6],[-9,-4],[-9,-9],[-5,-8],[-6,-7],[6,6],[-8,3],[-4,6],[4,-9],[6,-10],[-8,8],[9,-2],[-8,1],[7,-10],[-10,6],[1,-2],[-8,6],[4,-9],[-4,-10],[2,7],[-3,4],[6,6],[6,-1],[-5,-2],[4,5],[5,-2],[10,1],[6,-1],[-6,10],[8,7],[-7,1],[-1,-5],[10,-5],[-3,-3],[1,-6],[-1,7],[-2,7],[-2,-6],[-3,2],[-9,-9],[6,-5],[10,-3],[-1,7],[6,7],[-8,9],[-1,10],[-1,5],[7,10],[-7,4],[2,-6],[6,5],[5,1],[-10,-5],[7,-2],[8,-8],[-3,-10],[-5,8],[2,2],[-7,-2],[-3,-8],[-5,-2],[8,1],[-5,-1],[-9,-9],[-5,-4],[10,5],[-3,2],[1,-8],[4,-9],[8,-8],[-8,9],[2,-4],[4,-4],[-3,2],[7,3],[3,-4],[-3,-9],[10,-2],[-10,10],[9,-9],[-3,7],[-1,2],[-10,-5],[6,2],[-10,-10],[10,-3],[-3,2],[-8,-6],[3,6],[2,-3],[-5,-9],[-8,2],[-2,2],[-4,-10],[-9,-10],[-3,-9],[2,10],[5,8],[4,3],[-8,1],[7,10],[10,8],[-4,8],[3,-4],[5,8],[-9,-10],[-6,4],[9,-4],[1,-8],[7,2],[-2,-9],[-10,-1],[10,4],[10,2],[-6,1],[-4,-2],[10,7],[5,9],[2,4],[4,8],[9,-3],[6,4],[-4,9],[-2,4],[-10,1],[10,5],[-1,-3],[-6,-9],[3,-3],[-7,-10],[4,10],[10,-9],[-5,-8],[-10,5],[3,6],[-1,6],[7,10],[8,9],[-9,7],[-3,2],[7,-10],[-4,-10],[-7,6],[-3,9],[-4,6],[-10,4],[-3,1],[-7,1],[4,3],[-10,-2],[-9,-4],[-3,-2],[5,8],[4,7],[5,1],[-4,8],[-8,3],[-5,-7],[-7,9],[-6,-8],[-1,-8],[-10,-2],[4,7],[-10,3],[7,5],[5,6],[-3,-4],[6,-1],[8,-1],[4,-3],[9,-4],[6,-4],[-7,3],[-3,4],[4,8],[-9,8],[-8,-8],[-2,-1],[-1,-9],[-6,10],[-6,-5],[-3,-6],[8,8],[4,-5],[-7,-5],[3,10],[-10,-3],[-4,10],[-5,8],[6,7],[-9,-1],[1,5],[10,6],[5,9],[9,-4],[4,-2],[10,7],[3,2],[-8,-6],[3,-8],[-1,-8],[4,-6],[1,5],[-5,-4],[-4,-3],[-4,-10],[-1,3],[8,-7],[-8,9],[-4,5],[2,-1],[-5,-4],[-8,8],[3,6],[6,8],[-1,-7],[1,2],[-9,-3],[7,10],[10,2],[10,-2],[10,6],[7,4],[-8,8],[-4,-9],[9,6],[7,-7],[9,-7],[-1,-1],[-6,9],[-1,-1],[1,-10],[-2,-2],[10,-7],[5,6],[-3,-2],[-3,-5],[9,10],[6,-9],[-3,-6],[10,5],[5,9],[-6,-3],[-1,3],[-7,10],[-4,-6],[-4,-7],[-7,-9],[8,-7],[6,2],[-4,-10],[9,6],[6,4],[6,8],[6,-6],[-8,-10],[-1,-9],[4,8],[8,10],[5,-5],[-1,9],[-8,9],[2,-7],[-2,-7],[5,-9],[-9,6],[7,5],[3,3],[9,-3],[-8,-1],[10,1],[6,-5],[3,-9],[-9,2],[-10,-7],[8,-8],[1,4],[-6,2],[-4,7],[10,-10],[-4,-7],[-3,-2],[-7,7],[-1,2],[6,3],[-10,9],[-7,-5],[-8,2],[-3,8],[10,-10],[-9,4],[-2,3],[-2,-2],[-1,-10],[7,5],[-8,9],[6,9],[9,2],[-8,9],[-3,-10],[7,9],[2,6],[5,-5],[6,6],[5,-7],[7,-2],[4,-7],[-2,-1],[-2,8],[-2,-3],[8,9],[6,-8],[-1,3],[2,4],[-7,-4],[1,-1],[-10,5],[5,-8]], dtype = "int64")#candidate|6172|(330, 2)|const|int64
var_6173 = relay.var("var_6173", dtype = "float32", shape = (392,))#candidate|6173|(392,)|var|float32
const_6174 = relay.const([-5.032043,-0.776807,-2.200671,2.812977,5.993489,-4.277319,4.737387,5.161321,-0.582962,9.063442,7.056783,9.998455,7.393296,-7.378950,-2.493765,2.134647,-1.157780,6.234491,-2.327933,7.441292,0.571178,-8.419374,-3.456808,-2.686139,7.116969,2.262476,1.985061,-1.864359,5.883073,4.705312,-2.448410,-8.864946,-2.716574,6.755603,7.815072,-9.062575,3.560368,8.431581,-0.491988,-1.238685,4.039200,-9.175600,-0.824503,7.921790,9.296168,3.529921,0.569376,-1.689316,-0.629901,-1.476802,5.144093,-5.532645,7.391086,-3.195351,1.368280,0.009477,-8.177045,6.941460,3.921580,9.122618,9.006557,-3.458968,-5.816300,9.369992,-9.484355,-9.018846,-5.922132,-5.799783,-4.503511,-0.949341,4.802662,4.632861,3.309041,5.414495,4.677099,-1.698071,0.900504,-9.433773,2.361437,-5.218183,4.948694,3.763303,-1.887186,-8.754284,-6.680880,-2.018615,-3.344391,-4.716207,3.079142,-0.578738,-1.462027,5.758355,1.380485,7.325452,3.669985,5.519323,1.295568,3.852734,-0.162250,-9.657708,-2.792232,3.833890,-7.786473,-9.102492,1.479538,6.267965,1.450166,6.517539,-5.752833,-7.223073,1.633139,-4.136253,-8.528083,-8.148972,7.465350,-4.278598,2.026081,0.300603,5.296545,8.724713,-0.664993,-6.696724,-9.927217,5.112734,-6.129929,-0.212422,7.056199,-3.876794,-1.365583,-6.072162,-4.995118,2.246483,-6.751994,3.368044,2.340610,-0.357195,1.568375,5.963696,6.669487,-5.739417,-2.534117,5.160986,-1.611941,-2.946459,-9.913820,-5.610543,6.307880,-0.339132,-6.701920,6.205385,2.812553,-7.832690,-1.752238,-4.624481,-7.070462,0.857086,8.141696,-5.707790,6.958646,4.085856,2.330791,-7.704807,6.001455,0.385051,-8.268596,3.086352,-4.637280,2.590364,-8.022784,-0.860000,-6.595163,9.764735,-1.636729,8.366261,-6.838675,4.511506,2.193534,-2.736202,1.219241,-0.938533,-3.911264,0.002958,7.794056,3.047441,-2.976470,-8.926683,-5.303091,-9.385775,1.420233,-2.451941,-8.291693,-4.701183,6.100107,2.181277,-0.527539,-2.760453,7.096212,8.120698,-2.357786,-6.200163,2.553224,-8.954832,1.314919,-0.962646,-9.265774,-4.999167,0.235197,-8.769313,-7.978578,0.201875,-1.807322,5.280649,5.698280,-3.107891,-5.590391,-5.450626,-2.933668,7.796510,0.887091,-2.524694,-8.301856,8.710013,3.974624,-1.163605,5.164382,-2.376706,0.857410,4.865040,1.569614,8.081141,6.855072,9.367623,-4.846054,0.174961,-0.828348,2.962569,-7.479323,-4.739120,8.483934,7.198190,-0.833356,-1.080011,-0.090652,-1.453651,4.634215,7.575404,8.666404,-5.533933,3.575008,-0.674570,-5.252917,-7.736891,-2.443679,-8.936051,9.975077,-6.362622,-2.090092,5.903326,-2.948461,-0.694411,6.745269,-0.045828,-1.965636,-8.501017,-4.109348,2.912562,4.464285,-7.835973,1.060898,1.117870,-8.341871,-9.666220,-5.926522,5.439884,-2.624317,-6.835363,8.597963,-2.056048,-5.230373,4.941355,8.085204,4.866676,-1.668558,-3.099297,-0.192935,-1.123754,3.596335,6.494133,6.259000,5.251337,-9.445567,9.760080,-5.212375,3.630824,0.306726,-8.147589,-5.775479,4.221569,5.128466,-8.705336,9.653854,-7.326070,2.665314,-2.590865,8.143946,-0.283349,2.402824,0.440747,-8.804758,-0.202124,-6.565479,-6.724701,-7.553422,5.024491,-5.979794,-3.360410,2.310979,-4.534611,-7.772656,2.796990,-9.745110,-9.584812,0.466674,-5.998332,-6.783966,0.194942,6.533006,4.773664,8.598941,5.072815,-7.229295,1.383450,-4.744632,7.270163,-4.503339,-3.003976,-9.066404,4.239157,0.540539,8.733482,-4.444431,-1.080003,8.273665,-8.136412,-9.221938,-3.329349,0.284603,-3.464343,6.927243,-2.447538,-5.532176,0.558968,7.558046,3.657319,-2.426182,5.213101,6.240115,-6.778312,0.136595,-8.374970,-4.066970,3.389423,-9.241157,7.317636,9.669856,-4.956607,9.637093,-4.743521,-0.363564,9.125869,8.856096,7.588857,-3.085233,9.952114,-2.569387,1.892555,-3.223199,-2.264109,0.646304,-8.971558,-4.342806,-0.049772,-2.523325,-0.236597,-3.123878,1.495127,-4.269695,0.621915,-4.720516,9.671068,-4.632459,1.435602,5.203252,4.424912,-4.643768,4.375531,-4.519767,-9.723052,-6.531837,1.341715,-8.994469,-0.924148,-3.457390,6.239963,-1.453461,9.829791,2.777583,1.031245,5.500036,3.397723,4.837761,-6.982028,1.572226,-8.827101,5.064298,-3.019116,9.498204,4.817655,-8.122203,-2.955085,4.933196,5.728490,7.406792,4.700798,-1.140954,-0.916710,4.890119,5.491149,4.879628,-3.589203,-6.181340,-1.776742,-3.803056,5.630424,-6.969415,7.476216,2.673303,-4.806004,-0.114236,8.145528,1.264662,-6.273939,-3.012489,3.080719,0.329018,3.550317,-9.867366,8.789422,6.450369,-0.297935,2.820084,2.619403,-5.860477,7.224750,7.845750,1.121729,-1.322510,7.877606,-3.977164,-0.278808,-8.782754,0.839437,9.016657,2.782956,2.001485,-0.021452,-2.161673,1.904506,4.536311,0.371613,-5.534595,1.035470,-0.566272,0.418888,6.346437,-9.608251,5.805248,4.639000,3.575168,5.345327,-7.917607,0.795357,2.499645,2.242621,5.220707,1.540595,-8.385100,-4.969270,1.311290,0.938083,9.314865,8.602715,6.206481,1.041033,6.865591,7.985692,-2.736311,-4.915967,9.561031,-6.070672,-7.495170,-7.609518,5.286944,2.352492,9.020145,7.323929,1.724748,8.162298,6.852704,6.154455,-6.378950,-6.933013,6.833006,-9.708477,9.882872,5.546652,7.425695,-5.356251,-5.922801,1.059071,-9.291033,-5.045350,2.409343,-7.795975,-8.527765,-8.529531,-9.420262,5.335738,3.115446,-8.137984,-3.489766,9.873956,-1.256785,-4.175777,1.974826,-6.570383,8.645801,5.223882,-1.077069,4.690120], dtype = "float32")#candidate|6174|(540,)|const|float32
call_6171 = relay.TupleGetItem(func_3466_call(relay.reshape(const_6172.astype('int64'), [11, 4, 15]), relay.reshape(const_6172.astype('int64'), [11, 4, 15]), relay.reshape(var_6173.astype('float32'), [196, 2]), relay.reshape(const_6174.astype('float32'), [1, 540]), ), 3)
call_6175 = relay.TupleGetItem(func_3472_call(relay.reshape(const_6172.astype('int64'), [11, 4, 15]), relay.reshape(const_6172.astype('int64'), [11, 4, 15]), relay.reshape(var_6173.astype('float32'), [196, 2]), relay.reshape(const_6174.astype('float32'), [1, 540]), ), 3)
output = relay.Tuple([call_6167,call_6171,const_6172,var_6173,const_6174,])
output2 = relay.Tuple([call_6168,call_6175,const_6172,var_6173,const_6174,])
func_6176 = relay.Function([var_6173,], output)
mod['func_6176'] = func_6176
mod = relay.transform.InferType()(mod)
mutated_mod['func_6176'] = func_6176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6177 = relay.var("var_6177", dtype = "float32", shape = (392,))#candidate|6177|(392,)|var|float32
func_6176_call = mutated_mod.get_global_var('func_6176')
call_6178 = func_6176_call(var_6177)
output = call_6178
func_6179 = relay.Function([var_6177], output)
mutated_mod['func_6179'] = func_6179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6231 = relay.var("var_6231", dtype = "float32", shape = (1, 14, 10))#candidate|6231|(1, 14, 10)|var|float32
uop_6232 = relay.tan(var_6231.astype('float32')) # shape=(1, 14, 10)
func_2153_call = mod.get_global_var('func_2153')
func_2156_call = mutated_mod.get_global_var('func_2156')
const_6236 = relay.const(-3, dtype = "uint32")#candidate|6236|()|const|uint32
var_6237 = relay.var("var_6237", dtype = "uint32", shape = (256,))#candidate|6237|(256,)|var|uint32
call_6235 = relay.TupleGetItem(func_2153_call(relay.reshape(const_6236.astype('uint32'), []), relay.reshape(var_6237.astype('uint32'), [256,]), ), 2)
call_6238 = relay.TupleGetItem(func_2156_call(relay.reshape(const_6236.astype('uint32'), []), relay.reshape(var_6237.astype('uint32'), [256,]), ), 2)
output = relay.Tuple([uop_6232,call_6235,const_6236,var_6237,])
output2 = relay.Tuple([uop_6232,call_6238,const_6236,var_6237,])
func_6240 = relay.Function([var_6231,var_6237,], output)
mod['func_6240'] = func_6240
mod = relay.transform.InferType()(mod)
mutated_mod['func_6240'] = func_6240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6240_call = mutated_mod.get_global_var('func_6240')
var_6242 = relay.var("var_6242", dtype = "float32", shape = (1, 14, 10))#candidate|6242|(1, 14, 10)|var|float32
var_6243 = relay.var("var_6243", dtype = "uint32", shape = (256,))#candidate|6243|(256,)|var|uint32
call_6241 = func_6240_call(var_6242,var_6243,)
output = call_6241
func_6244 = relay.Function([var_6242,var_6243,], output)
mutated_mod['func_6244'] = func_6244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1538_call = mod.get_global_var('func_1538')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_6252 = relay.TupleGetItem(func_1538_call(), 2)
call_6253 = relay.TupleGetItem(func_1540_call(), 2)
uop_6258 = relay.tan(call_6252.astype('float64')) # shape=(42,)
uop_6260 = relay.tan(call_6253.astype('float64')) # shape=(42,)
output = relay.Tuple([uop_6258,])
output2 = relay.Tuple([uop_6260,])
func_6266 = relay.Function([], output)
mod['func_6266'] = func_6266
mod = relay.transform.InferType()(mod)
mutated_mod['func_6266'] = func_6266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6266_call = mutated_mod.get_global_var('func_6266')
call_6267 = func_6266_call()
output = call_6267
func_6268 = relay.Function([], output)
mutated_mod['func_6268'] = func_6268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5414_call = mod.get_global_var('func_5414')
func_5415_call = mutated_mod.get_global_var('func_5415')
call_6269 = relay.TupleGetItem(func_5414_call(), 0)
call_6270 = relay.TupleGetItem(func_5415_call(), 0)
func_6120_call = mod.get_global_var('func_6120')
func_6124_call = mutated_mod.get_global_var('func_6124')
const_6273 = relay.const([-7.568113,-4.510594,-6.982432,-9.373030,7.224816,7.093177,9.772046,-6.528702,-4.383580,-0.572109,-7.495887,1.549059,7.952509,-9.001675,0.014969,-9.184758,0.178493,7.802467,3.829075,5.168385,9.634960,-1.515058,-3.925977,9.486448,-6.430776,9.638337,2.275343,0.765518,-7.833733,3.801197,2.100823,7.582829,-3.788232,-5.986809,-9.737115,-4.161797,-3.091897,6.554737,-1.589176,8.913980,-8.318173,0.624331,-2.597231,6.124437,4.745607,-0.911617,-4.185931,6.491699,-5.935572,2.342773,-5.673657,-6.894241,-8.514641,9.567164,8.788752,6.369437,6.965138,6.720201,8.056532,-9.307037], dtype = "float32")#candidate|6273|(60,)|const|float32
const_6274 = relay.const([-6.395315,5.219331,-5.818403,6.503425,-2.102443,5.115516,8.306130,5.048906,-2.236267,9.966653,-2.448497,4.504469,7.397267,-7.391347,-2.152957,-1.542736,-5.849319,1.797952,-6.553484,1.946424,0.252546,-0.757760,1.316959,4.415994,-7.257795,1.792182,6.184682,7.804988,-8.627151,5.099072,7.725462,2.335226,7.619197,2.268216,-5.024411,3.224864,5.616836,-8.483271,1.280983,-7.138387,-9.485164,-7.122783,-9.879595,-9.761538,9.508848,0.737934,-6.188645,1.856022,-3.217875,0.141547,3.365650,-9.662992,-8.899273,-1.771461,-7.611476,-7.172211,-4.790389,-0.281431,-0.994062,-8.557721,-8.481431,-5.197164,-7.709768,2.715153,-7.898347,5.328724,0.215022,8.721691,0.511555,1.166703,-8.973380,-8.791547,4.108087,-1.121226,-8.274948,5.723066,-6.333345,4.578704,6.314348,9.434990,2.488783,-7.878042,-7.318564,6.464577,5.999923,2.941158,-5.078177,-2.485806,-7.262007,9.574428,4.678864,-1.270572,-6.663994,4.333752,-1.076883,-8.513262,5.056876,-5.407948,-2.577646,4.301523,-1.130712,1.088208,8.066980,-4.920763,-5.023174,-4.344417,2.909927,-6.109576,-6.612535,8.125566,-5.631078,-1.383190,-3.167994,-1.119062,-9.654463,-6.108699,-2.504115,1.753333,-3.294384,-0.010184,1.911453,-4.170835,4.009228,1.393523,-3.861513,-3.820148,-8.511943,0.281571,2.308354,7.691956,2.627978,-5.597894,4.379214,9.440379,-4.876901], dtype = "float32")#candidate|6274|(135,)|const|float32
call_6272 = relay.TupleGetItem(func_6120_call(relay.reshape(const_6273.astype('float32'), [3, 10, 2]), relay.reshape(const_6274.astype('float32'), [1, 135]), ), 2)
call_6275 = relay.TupleGetItem(func_6124_call(relay.reshape(const_6273.astype('float32'), [3, 10, 2]), relay.reshape(const_6274.astype('float32'), [1, 135]), ), 2)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_6283 = func_2031_call()
call_6284 = func_2031_call()
uop_6293 = relay.acosh(call_6269.astype('float64')) # shape=(9, 405, 15)
uop_6295 = relay.acosh(call_6270.astype('float64')) # shape=(9, 405, 15)
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
var_6303 = relay.var("var_6303", dtype = "float64", shape = (5, 4))#candidate|6303|(5, 4)|var|float64
call_6302 = relay.TupleGetItem(func_4061_call(relay.reshape(var_6303.astype('float64'), [5, 2, 2])), 2)
call_6304 = relay.TupleGetItem(func_4064_call(relay.reshape(var_6303.astype('float64'), [5, 2, 2])), 2)
uop_6309 = relay.log10(uop_6293.astype('float64')) # shape=(9, 405, 15)
uop_6311 = relay.log10(uop_6295.astype('float64')) # shape=(9, 405, 15)
bop_6316 = relay.add(uop_6293.astype('float32'), relay.reshape(uop_6309.astype('float32'), relay.shape_of(uop_6293))) # shape=(9, 405, 15)
bop_6319 = relay.add(uop_6295.astype('float32'), relay.reshape(uop_6311.astype('float32'), relay.shape_of(uop_6295))) # shape=(9, 405, 15)
output = relay.Tuple([call_6272,const_6273,const_6274,call_6283,call_6302,var_6303,bop_6316,])
output2 = relay.Tuple([call_6275,const_6273,const_6274,call_6284,call_6304,var_6303,bop_6319,])
func_6324 = relay.Function([var_6303,], output)
mod['func_6324'] = func_6324
mod = relay.transform.InferType()(mod)
mutated_mod['func_6324'] = func_6324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6325 = relay.var("var_6325", dtype = "float64", shape = (5, 4))#candidate|6325|(5, 4)|var|float64
func_6324_call = mutated_mod.get_global_var('func_6324')
call_6326 = func_6324_call(var_6325)
output = call_6326
func_6327 = relay.Function([var_6325], output)
mutated_mod['func_6327'] = func_6327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2896_call = mod.get_global_var('func_2896')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_6332 = relay.TupleGetItem(func_2896_call(), 1)
call_6333 = relay.TupleGetItem(func_2897_call(), 1)
func_1970_call = mod.get_global_var('func_1970')
func_1971_call = mutated_mod.get_global_var('func_1971')
call_6342 = func_1970_call()
call_6343 = func_1970_call()
uop_6366 = relay.cosh(call_6342.astype('float32')) # shape=(5, 4, 2)
uop_6368 = relay.cosh(call_6343.astype('float32')) # shape=(5, 4, 2)
func_5266_call = mod.get_global_var('func_5266')
func_5270_call = mutated_mod.get_global_var('func_5270')
var_6371 = relay.var("var_6371", dtype = "float32", shape = (312, 2))#candidate|6371|(312, 2)|var|float32
call_6370 = relay.TupleGetItem(func_5266_call(relay.reshape(var_6371.astype('float32'), [13, 3, 16]), relay.reshape(var_6371.astype('float32'), [13, 3, 16]), ), 3)
call_6372 = relay.TupleGetItem(func_5270_call(relay.reshape(var_6371.astype('float32'), [13, 3, 16]), relay.reshape(var_6371.astype('float32'), [13, 3, 16]), ), 3)
uop_6382 = relay.tan(uop_6366.astype('float32')) # shape=(5, 4, 2)
uop_6384 = relay.tan(uop_6368.astype('float32')) # shape=(5, 4, 2)
func_6176_call = mod.get_global_var('func_6176')
func_6179_call = mutated_mod.get_global_var('func_6179')
const_6388 = relay.const([7.036250,-2.916106,8.310792,-9.179008,-1.034917,5.738778,1.930821,-1.062043,-7.626979,-1.437713,-4.935876,-0.061406,9.224404,-8.687373,9.755311,3.556620,-0.726865,6.338144,-3.814141,7.921898,-0.570298,7.689222,-0.291677,0.997022,3.192037,-5.206053,4.156191,2.621373,-2.455548,4.729120,-7.973474,7.551545,2.971855,-4.940245,-2.199662,-0.371179,9.866693,2.231890,-2.345256,-7.228408,-1.732368,6.714798,1.445206,-0.415769,-9.103560,9.898710,-8.453755,2.580462,7.561063,5.314771,5.048902,-9.197884,-8.037786,-5.979206,-0.608118,-0.932868,3.070774,-3.469127,4.534547,2.838314,7.693269,-0.772036,5.068321,2.647391,0.715230,-7.575688,-4.084329,8.812179,-0.996707,9.969443,-4.731692,-1.051173,-9.986768,-1.956318,3.339370,5.289784,-1.066971,3.563036,-0.510502,-9.906625,8.353046,-1.951475,3.679383,-5.978148,-8.357507,-3.450688,-0.807455,-6.789891,-3.670657,-4.302028,-5.697708,-7.563832,5.299815,-4.143330,-2.741500,1.205636,-7.767973,6.615500,-7.350556,5.541491,-1.114506,4.362595,-6.214381,0.573481,1.548860,8.810486,5.560385,-6.847542,7.802358,-5.639531,-2.689952,4.944910,-1.069141,-9.932002,9.812386,5.433678,-4.423775,-2.395593,-0.579211,3.909847,2.618916,-2.557732,-7.391196,1.855020,0.598723,5.320526,7.732566,-0.266299,0.846268,-0.045404,0.824600,-9.832379,4.643028,-9.643042,-1.863027,8.906249,-8.525854,0.748975,-3.670875,-9.436937,-0.203301,7.689735,4.341503,4.834402,1.012765,2.626941,7.567574,-5.477469,-9.322789,7.660301,-0.806483,-0.205505,-7.260191,2.562939,-0.414134,-3.014232,5.718308,-9.966893,-6.410996,1.495850,-2.813408,-2.957796,6.458952,-9.081474,5.311609,-0.765521,-9.223281,9.604537,-5.524129,8.706947,-3.421695,-7.951883,-3.078705,-4.187592,-5.866298,-9.857566,-3.957245,0.809129,1.311626,8.518633,0.583660,-7.402093,-1.479777,-5.263650,-0.591150,2.223502,4.111685,-7.656453,1.411078,-8.038053,-0.331877,-4.658182,4.253752,-5.317863,1.731647,-8.620596,-0.047377,-7.422221,-8.792116,0.578253,-3.790171,5.833121,-0.093960,9.969591,9.829885,-2.987760,-8.220014,-0.907683,-4.525506,-7.716819,2.070689,-1.245054,1.064835,-2.403359,8.957745,-6.216887,4.636216,9.335204,3.949345,6.633559,0.107179,9.586983,-1.507749,6.206286,-2.573660,-8.076159,-0.947334,2.934258,8.415635,4.960682,-2.022285,-1.677670,-9.331649,8.034121,4.951799,-9.590425,-3.706663,-6.299389,5.356897,1.433782,-1.022979,1.886356,-5.861578,-3.769791,4.936358,-5.548104,-7.845194,5.011954,8.870476,-1.857644,2.119818,9.613314,-5.322336,-7.796818,0.807864,-8.979094,7.557557,8.580095,-7.619886,4.346084,4.903519,4.692502,-4.316182,-5.138774,-7.376658,-4.744385,0.919885,7.886631,-7.590404,-9.962750,-7.300155,6.752510,-7.433582,5.336160,-4.679398,-1.074435,6.104288,0.542388,-1.594742,3.479926,6.167780,-4.558115,7.648627,-0.208059,7.324424,4.628566,2.485069,6.899825,5.115918,9.252697,3.752627,-9.011546,2.114236,2.514162,6.471275,-1.105439,-2.673818,-8.522501,5.523874,4.677991,3.372205,-5.530757,7.493755,-8.344055,-8.351617,3.638047,-5.548529,-0.892185,9.714740,0.712097,-2.795751,0.734879,2.954831,-0.135452,9.441552,9.499471,7.063958,1.803486,-4.242620,8.218815,0.724243,-0.617453,-3.734638,-5.851784,-7.815287,2.382537,9.501354,-7.744602,-3.079142,9.603311,-8.399090,-2.444780,-5.153157,2.248860,5.273634,-1.677895,1.696288,-2.011497,3.316808,3.641490,3.190599,3.423871,-4.564380,3.959320,-8.890804,-2.708185,6.965365,-0.248424,-4.398418,-6.273938,1.307928,1.607307,-6.388578,-8.167377,-7.640020,2.696922,-0.953405,-3.246920,-1.959348,2.621850,0.658767,-5.754536,-5.284697,-4.133264,-1.834712,2.719464,0.869324,-6.425194,-0.466197,-4.678036,-8.312461,-6.959923,-2.105774,6.370215,-0.131751,5.069261,-6.320975,9.091829,4.357959,-0.608007,-8.515283,9.327081,-9.135804,2.285306,-5.967920,2.367759,-8.309238,-2.577804,-8.707446,8.413068,-1.859512,-8.635745], dtype = "float32")#candidate|6388|(392,)|const|float32
call_6387 = relay.TupleGetItem(func_6176_call(relay.reshape(const_6388.astype('float32'), [392,])), 2)
call_6389 = relay.TupleGetItem(func_6179_call(relay.reshape(const_6388.astype('float32'), [392,])), 2)
output = relay.Tuple([call_6332,call_6370,var_6371,uop_6382,call_6387,const_6388,])
output2 = relay.Tuple([call_6333,call_6372,var_6371,uop_6384,call_6389,const_6388,])
func_6392 = relay.Function([var_6371,], output)
mod['func_6392'] = func_6392
mod = relay.transform.InferType()(mod)
var_6393 = relay.var("var_6393", dtype = "float32", shape = (312, 2))#candidate|6393|(312, 2)|var|float32
output = func_6392(var_6393)
func_6394 = relay.Function([var_6393], output)
mutated_mod['func_6394'] = func_6394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4213_call = mod.get_global_var('func_4213')
func_4215_call = mutated_mod.get_global_var('func_4215')
call_6410 = func_4213_call()
call_6411 = func_4213_call()
output = call_6410
output2 = call_6411
func_6419 = relay.Function([], output)
mod['func_6419'] = func_6419
mod = relay.transform.InferType()(mod)
mutated_mod['func_6419'] = func_6419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6419_call = mutated_mod.get_global_var('func_6419')
call_6420 = func_6419_call()
output = call_6420
func_6421 = relay.Function([], output)
mutated_mod['func_6421'] = func_6421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_6475 = relay.TupleGetItem(func_2536_call(), 1)
call_6476 = relay.TupleGetItem(func_2537_call(), 1)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_6515 = relay.TupleGetItem(func_3316_call(), 0)
call_6516 = relay.TupleGetItem(func_3318_call(), 0)
output = relay.Tuple([call_6475,call_6515,])
output2 = relay.Tuple([call_6476,call_6516,])
func_6547 = relay.Function([], output)
mod['func_6547'] = func_6547
mod = relay.transform.InferType()(mod)
output = func_6547()
func_6548 = relay.Function([], output)
mutated_mod['func_6548'] = func_6548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5548_call = mod.get_global_var('func_5548')
func_5549_call = mutated_mod.get_global_var('func_5549')
call_6591 = relay.TupleGetItem(func_5548_call(), 1)
call_6592 = relay.TupleGetItem(func_5549_call(), 1)
output = call_6591
output2 = call_6592
func_6619 = relay.Function([], output)
mod['func_6619'] = func_6619
mod = relay.transform.InferType()(mod)
mutated_mod['func_6619'] = func_6619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6619_call = mutated_mod.get_global_var('func_6619')
call_6620 = func_6619_call()
output = call_6620
func_6621 = relay.Function([], output)
mutated_mod['func_6621'] = func_6621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2285_call = mod.get_global_var('func_2285')
func_2286_call = mutated_mod.get_global_var('func_2286')
call_6655 = relay.TupleGetItem(func_2285_call(), 0)
call_6656 = relay.TupleGetItem(func_2286_call(), 0)
func_5483_call = mod.get_global_var('func_5483')
func_5486_call = mutated_mod.get_global_var('func_5486')
var_6658 = relay.var("var_6658", dtype = "int64", shape = ())#candidate|6658|()|var|int64
var_6659 = relay.var("var_6659", dtype = "int64", shape = (495,))#candidate|6659|(495,)|var|int64
call_6657 = relay.TupleGetItem(func_5483_call(relay.reshape(var_6658.astype('int64'), []), relay.reshape(var_6659.astype('int64'), [5, 11, 9]), ), 0)
call_6660 = relay.TupleGetItem(func_5486_call(relay.reshape(var_6658.astype('int64'), []), relay.reshape(var_6659.astype('int64'), [5, 11, 9]), ), 0)
output = relay.Tuple([call_6655,call_6657,var_6658,var_6659,])
output2 = relay.Tuple([call_6656,call_6660,var_6658,var_6659,])
func_6665 = relay.Function([var_6658,var_6659,], output)
mod['func_6665'] = func_6665
mod = relay.transform.InferType()(mod)
var_6666 = relay.var("var_6666", dtype = "int64", shape = ())#candidate|6666|()|var|int64
var_6667 = relay.var("var_6667", dtype = "int64", shape = (495,))#candidate|6667|(495,)|var|int64
output = func_6665(var_6666,var_6667,)
func_6668 = relay.Function([var_6666,var_6667,], output)
mutated_mod['func_6668'] = func_6668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4412_call = mod.get_global_var('func_4412')
func_4414_call = mutated_mod.get_global_var('func_4414')
call_6690 = func_4412_call()
call_6691 = func_4412_call()
output = call_6690
output2 = call_6691
func_6701 = relay.Function([], output)
mod['func_6701'] = func_6701
mod = relay.transform.InferType()(mod)
mutated_mod['func_6701'] = func_6701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6701_call = mutated_mod.get_global_var('func_6701')
call_6702 = func_6701_call()
output = call_6702
func_6703 = relay.Function([], output)
mutated_mod['func_6703'] = func_6703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_6818 = relay.TupleGetItem(func_888_call(), 0)
call_6819 = relay.TupleGetItem(func_889_call(), 0)
func_5641_call = mod.get_global_var('func_5641')
func_5645_call = mutated_mod.get_global_var('func_5645')
const_6821 = relay.const([-0.097335,-6.618876,4.402693,-5.811063,3.293638,-3.861499,1.398949,1.804355,-9.505175,6.059978,5.555224,4.751784,5.158285,7.331937,-9.062862,-8.890901,-6.044672,-9.405682,-8.288960,2.368595,-8.195101,-7.684488,8.892678,8.962057,-8.735144,0.621567,3.211745,9.196936,-4.134762,5.786250,4.105063,1.694661,-2.161258,-1.184933,-6.711464,-0.363583,2.966550,-3.462181,-1.984416,9.858193,8.654834,4.852329,4.213852,8.926371,7.750854,-7.218306,-4.829277,-0.774992,8.929936,5.634584,-0.355550,-5.272367,6.724354,-8.186744,1.948459,-2.317007,-1.551947,8.365264,6.757348,6.207636,3.951195,7.188256,0.466870,-9.228437,-4.132711,0.059891,-1.127806,0.907242,-0.143151,2.004717,4.359472,-1.226253,3.905994,3.246085,-8.462839,0.387477,0.651719,-1.835356,4.816435,9.565238,-8.100129,-5.330467,3.790573,-3.949631,-9.168503,2.889067,-7.769355,7.921910,0.846253,-7.625679,-7.176318,9.745134,-1.727957,-9.346400,-3.510961,-2.238621,-7.640274,3.009429,-9.455418,-7.335167,-7.223761,-9.114153,0.371923,-0.154358,-1.337921,0.374132,8.466779,-0.998685,-9.914154,5.738268,5.225455,8.316612,-3.543974,8.288552,7.761907,0.532359,6.235835,-1.702962,-7.627918,8.376400,0.732592,1.517561,6.366385,-7.047145,-8.827184,-2.715988,2.632491,-3.827116,1.070718,-8.974213,1.230983,-6.374290,1.521107,1.174369,2.595120,5.684917,6.550073,6.708654,-5.863437,-1.191040,6.454863,-1.162681,0.701578,3.715191,-5.525067,2.861785,4.325844,-2.275118,-9.461776,-1.213090,-6.269612,-4.878997,-1.107748,-5.500156,9.814067,-6.726363,-0.904143,-1.787188,8.788901,-6.270807,6.808372,4.882340,2.719979,-3.340416,4.844283,1.194153,-1.154428,-2.422525,-7.253850,0.670819,3.890149,-5.933728,9.028907,7.027376,-9.805010,-8.500625,5.095547,2.905045,-1.166093,-1.271838,-4.701831,4.300972,0.388021,-5.843544,2.352384,-5.923594,7.324582,-7.987284,9.983496,8.398589,0.184391,2.239728,8.889699,0.309376,-1.533874,2.924617,0.183442,7.424581,-4.718895,-1.626739,-0.724206,4.798013,-5.321872,-8.042306,2.382913,8.279342,3.704781,-6.289544,4.200285,-0.027216,7.790298,1.767462,8.474527,-5.873205,-0.802290,3.825065,8.041346,-6.320804,-0.188326,6.179588,-7.339370,-4.897407,7.824636,-2.650954,-7.121118,8.321089,-3.251674,-0.963918,8.296218,-7.732178,-7.305487,-5.051250,-0.567179,1.160661,3.520575,-1.958880,0.407395,-1.096247,1.284190,-8.405790,3.768490,-7.126872,-2.837174,9.258191,6.434716,7.979510,1.953563,6.529544,-4.614619,-7.221714,1.415498,9.918960,8.933112,1.407678,-9.801983,-3.985197,4.191788,9.812508,-6.095663,-5.761704,-0.339332,4.219765,7.632248,7.829158,6.536177,-0.235702,3.517654,7.061165,2.154140,8.472076,-0.923225,8.628338,-2.292556,7.360091,-6.012747,-0.126628,6.321665,-0.326048,-3.300288,-5.838381,-5.860355,-8.697748,-3.678897,-7.671775,0.236415,0.381019,-5.063543,9.495085,-6.690710,5.408544,-2.517483,9.940927,6.951249,3.987579,-9.246342,9.243295,-9.729243,-1.744153,7.955334,-7.934496,-7.230215,9.251846,-6.206771,-1.505223,6.360610,0.023182,6.000280,-9.923243,5.141825,2.343625,1.993978,-8.663035,-8.637957,0.947836,2.434668,-6.637449,8.244356,-9.793828,1.220399,-8.515226,-7.311920,-9.376517,0.499819,-2.222967,-1.320443,-2.603797,-6.239928,5.744201,7.007197,8.251546,-4.965402,-9.420342,1.502432,-2.763783,6.225057,1.863382,-2.748579,-1.972867,-0.325989,-6.197824,-6.413156,5.393102,1.276654,7.662975,3.582192,-7.007274,9.561393,4.709825,7.148375,1.936598,5.353945,9.751042,-0.549750,6.870314,-4.813654,-4.604596,-9.801823,-5.830755,-4.861308,-2.469058,-1.042517,-7.710445,7.717912,-2.977894,9.368180,-2.925554,-6.714326,-7.516429,5.814088,-3.179410,-0.608744,-2.768148,-4.448493,-2.281655,-8.645754,-7.849529,9.092268,-9.229325,-7.752762,-2.311179,-9.240329,-9.402298,-7.905561,-1.451966,-8.875380,9.483648,9.595627,9.484834,-3.806379,-7.118919,-3.901116,8.434207,2.161477,8.442292,-8.509834,5.762730,-2.016068,-0.283648,7.374512,-6.610058], dtype = "float64")#candidate|6821|(400,)|const|float64
call_6820 = relay.TupleGetItem(func_5641_call(relay.reshape(const_6821.astype('float64'), [4, 10, 10]), relay.reshape(const_6821.astype('float64'), [4, 10, 10]), ), 1)
call_6822 = relay.TupleGetItem(func_5645_call(relay.reshape(const_6821.astype('float64'), [4, 10, 10]), relay.reshape(const_6821.astype('float64'), [4, 10, 10]), ), 1)
func_5641_call = mod.get_global_var('func_5641')
func_5645_call = mutated_mod.get_global_var('func_5645')
call_6832 = relay.TupleGetItem(func_5641_call(relay.reshape(const_6821.astype('float64'), [4, 10, 10]), relay.reshape(call_6820.astype('float64'), [4, 10, 10]), ), 0)
call_6833 = relay.TupleGetItem(func_5645_call(relay.reshape(const_6821.astype('float64'), [4, 10, 10]), relay.reshape(call_6820.astype('float64'), [4, 10, 10]), ), 0)
output = relay.Tuple([call_6818,call_6820,const_6821,call_6832,])
output2 = relay.Tuple([call_6819,call_6822,const_6821,call_6833,])
func_6836 = relay.Function([], output)
mod['func_6836'] = func_6836
mod = relay.transform.InferType()(mod)
output = func_6836()
func_6837 = relay.Function([], output)
mutated_mod['func_6837'] = func_6837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5548_call = mod.get_global_var('func_5548')
func_5549_call = mutated_mod.get_global_var('func_5549')
call_6841 = relay.TupleGetItem(func_5548_call(), 0)
call_6842 = relay.TupleGetItem(func_5549_call(), 0)
output = call_6841
output2 = call_6842
func_6859 = relay.Function([], output)
mod['func_6859'] = func_6859
mod = relay.transform.InferType()(mod)
output = func_6859()
func_6860 = relay.Function([], output)
mutated_mod['func_6860'] = func_6860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1086_call = mod.get_global_var('func_1086')
func_1088_call = mutated_mod.get_global_var('func_1088')
call_6877 = relay.TupleGetItem(func_1086_call(), 0)
call_6878 = relay.TupleGetItem(func_1088_call(), 0)
output = relay.Tuple([call_6877,])
output2 = relay.Tuple([call_6878,])
func_6885 = relay.Function([], output)
mod['func_6885'] = func_6885
mod = relay.transform.InferType()(mod)
output = func_6885()
func_6886 = relay.Function([], output)
mutated_mod['func_6886'] = func_6886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5938_call = mod.get_global_var('func_5938')
func_5939_call = mutated_mod.get_global_var('func_5939')
call_6941 = relay.TupleGetItem(func_5938_call(), 0)
call_6942 = relay.TupleGetItem(func_5939_call(), 0)
func_99_call = mod.get_global_var('func_99')
func_101_call = mutated_mod.get_global_var('func_101')
const_6952 = relay.const([[0.817386,-0.687310,-7.123764,-7.376269,9.206974,-2.366742,8.901811,-6.106281,-3.851276,0.216259,-1.366205,-2.564987,-9.810063,-1.298190,1.562775,6.892641,-2.812836,8.514908,6.862613,8.206338,-3.743262,8.040248,-2.965605,6.672251,-3.165546,-0.871904,8.664085,8.773448,-3.759920,-7.098227,-1.533122,2.320054,7.196996,2.845829,-2.228734,-8.360087,5.355071,-1.160017,9.595149,-5.883185,-3.770553,-6.465743,3.170737,-2.447447,-7.404205],[7.547621,-2.652568,3.774059,-2.202682,-8.189312,3.598171,7.907564,-8.401620,-3.500721,4.803326,2.942930,7.442610,5.986910,7.784514,1.042788,-2.241995,-4.630238,1.472558,4.621483,9.920198,-0.657295,-3.039211,6.937531,4.663843,-0.853649,-8.923727,-7.056221,4.803603,-7.048421,3.482760,-1.431915,-1.593472,-4.425290,-1.542480,8.776684,7.940580,-1.953194,7.338384,5.898310,5.610994,-7.205738,3.138057,-9.058411,-5.151283,-9.708563],[-4.452275,-9.713753,0.297065,-2.678687,-5.602025,5.958726,4.251996,1.762631,6.462382,9.860969,-3.368815,-9.110176,-5.173188,-3.450391,9.459790,0.684825,-1.249802,6.116411,-6.503288,6.155706,4.711984,3.800384,9.997654,-1.224570,0.816670,0.328687,2.032528,4.446524,-8.357801,-0.514620,-1.715033,4.004141,6.511508,3.954480,-4.358975,-0.561114,4.064831,-0.306367,-3.624695,-0.139259,-9.536004,8.844894,3.591889,-8.059485,1.928259]], dtype = "float32")#candidate|6952|(3, 45)|const|float32
call_6951 = func_99_call(relay.reshape(const_6952.astype('float32'), [9, 1, 15]))
call_6953 = func_99_call(relay.reshape(const_6952.astype('float32'), [9, 1, 15]))
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
const_6959 = relay.const([-4.327459,4.173276,-0.988256,-3.684998,-1.478304,2.772772,1.008074,4.478155,6.383219,-5.118179,5.238310,-1.314789,4.408079,-0.935364,2.957395,-6.176143,1.834327,7.203611,-0.301072,4.202945], dtype = "float64")#candidate|6959|(20,)|const|float64
call_6958 = relay.TupleGetItem(func_4061_call(relay.reshape(const_6959.astype('float64'), [5, 2, 2])), 2)
call_6960 = relay.TupleGetItem(func_4064_call(relay.reshape(const_6959.astype('float64'), [5, 2, 2])), 2)
output = relay.Tuple([call_6941,call_6951,const_6952,call_6958,const_6959,])
output2 = relay.Tuple([call_6942,call_6953,const_6952,call_6960,const_6959,])
func_6977 = relay.Function([], output)
mod['func_6977'] = func_6977
mod = relay.transform.InferType()(mod)
mutated_mod['func_6977'] = func_6977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6977_call = mutated_mod.get_global_var('func_6977')
call_6978 = func_6977_call()
output = call_6978
func_6979 = relay.Function([], output)
mutated_mod['func_6979'] = func_6979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6859_call = mod.get_global_var('func_6859')
func_6860_call = mutated_mod.get_global_var('func_6860')
call_6998 = func_6859_call()
call_6999 = func_6859_call()
func_663_call = mod.get_global_var('func_663')
func_665_call = mutated_mod.get_global_var('func_665')
call_7005 = func_663_call()
call_7006 = func_663_call()
output = relay.Tuple([call_6998,call_7005,])
output2 = relay.Tuple([call_6999,call_7006,])
func_7010 = relay.Function([], output)
mod['func_7010'] = func_7010
mod = relay.transform.InferType()(mod)
output = func_7010()
func_7011 = relay.Function([], output)
mutated_mod['func_7011'] = func_7011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6161_call = mod.get_global_var('func_6161')
func_6162_call = mutated_mod.get_global_var('func_6162')
call_7046 = func_6161_call()
call_7047 = func_6161_call()
func_2153_call = mod.get_global_var('func_2153')
func_2156_call = mutated_mod.get_global_var('func_2156')
var_7053 = relay.var("var_7053", dtype = "uint32", shape = ())#candidate|7053|()|var|uint32
var_7054 = relay.var("var_7054", dtype = "uint32", shape = (256,))#candidate|7054|(256,)|var|uint32
call_7052 = relay.TupleGetItem(func_2153_call(relay.reshape(var_7053.astype('uint32'), []), relay.reshape(var_7054.astype('uint32'), [256,]), ), 2)
call_7055 = relay.TupleGetItem(func_2156_call(relay.reshape(var_7053.astype('uint32'), []), relay.reshape(var_7054.astype('uint32'), [256,]), ), 2)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
const_7064 = relay.const([-5.545209,0.238115,-8.357208,2.639741,-8.828634,6.022562,4.189337,9.584784,9.264906,1.280837,4.778881,-9.234701,-4.941979,7.207920,-6.379918,-2.272486,-4.299730,-3.219436,8.343395,0.901120,-9.449295,5.448997,-2.818008,5.863471,0.215963,0.335163,-3.913721,-3.096558,0.107405,6.721521,-2.772612,-2.546976,4.652349,5.003929,-6.939223,-6.779836,7.326138,6.787126,9.715263,-1.001821,7.452998,7.987626], dtype = "float64")#candidate|7064|(42,)|const|float64
call_7063 = func_681_call(relay.reshape(const_7064.astype('float64'), [3, 14, 1]))
call_7065 = func_681_call(relay.reshape(const_7064.astype('float64'), [3, 14, 1]))
func_6066_call = mod.get_global_var('func_6066')
func_6068_call = mutated_mod.get_global_var('func_6068')
const_7069 = relay.const([[-3,-7,2,-1],[7,9,9,-7],[2,9,-9,6],[-1,-9,-10,-1],[5,3,6,-4],[-9,2,-1,-9],[4,2,-2,1],[-9,-8,-1,-3],[4,8,9,3],[-4,-7,6,5],[3,3,-8,-1],[-7,7,7,-6],[3,3,5,9],[2,4,4,-8],[-9,-2,-5,5]], dtype = "int32")#candidate|7069|(15, 4)|const|int32
call_7068 = relay.TupleGetItem(func_6066_call(relay.reshape(const_7069.astype('int32'), [10, 1, 6])), 1)
call_7070 = relay.TupleGetItem(func_6068_call(relay.reshape(const_7069.astype('int32'), [10, 1, 6])), 1)
func_6161_call = mod.get_global_var('func_6161')
func_6162_call = mutated_mod.get_global_var('func_6162')
call_7077 = func_6161_call()
call_7078 = func_6161_call()
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_7099 = func_681_call(relay.reshape(call_7063.astype('float64'), [3, 14, 1]))
call_7100 = func_681_call(relay.reshape(call_7063.astype('float64'), [3, 14, 1]))
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_7101 = relay.TupleGetItem(func_1914_call(), 2)
call_7102 = relay.TupleGetItem(func_1915_call(), 2)
output = relay.Tuple([call_7046,call_7052,var_7053,var_7054,call_7063,const_7064,call_7068,const_7069,call_7077,call_7099,call_7101,])
output2 = relay.Tuple([call_7047,call_7055,var_7053,var_7054,call_7065,const_7064,call_7070,const_7069,call_7078,call_7100,call_7102,])
func_7103 = relay.Function([var_7053,var_7054,], output)
mod['func_7103'] = func_7103
mod = relay.transform.InferType()(mod)
var_7104 = relay.var("var_7104", dtype = "uint32", shape = ())#candidate|7104|()|var|uint32
var_7105 = relay.var("var_7105", dtype = "uint32", shape = (256,))#candidate|7105|(256,)|var|uint32
output = func_7103(var_7104,var_7105,)
func_7106 = relay.Function([var_7104,var_7105,], output)
mutated_mod['func_7106'] = func_7106
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7170 = relay.var("var_7170", dtype = "float32", shape = (1, 15, 3))#candidate|7170|(1, 15, 3)|var|float32
uop_7171 = relay.exp(var_7170.astype('float32')) # shape=(1, 15, 3)
bop_7179 = relay.greater_equal(uop_7171.astype('bool'), relay.reshape(var_7170.astype('bool'), relay.shape_of(uop_7171))) # shape=(1, 15, 3)
output = bop_7179
output2 = bop_7179
func_7182 = relay.Function([var_7170,], output)
mod['func_7182'] = func_7182
mod = relay.transform.InferType()(mod)
var_7183 = relay.var("var_7183", dtype = "float32", shape = (1, 15, 3))#candidate|7183|(1, 15, 3)|var|float32
output = func_7182(var_7183)
func_7184 = relay.Function([var_7183], output)
mutated_mod['func_7184'] = func_7184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_349_call = mod.get_global_var('func_349')
func_350_call = mutated_mod.get_global_var('func_350')
call_7248 = relay.TupleGetItem(func_349_call(), 2)
call_7249 = relay.TupleGetItem(func_350_call(), 2)
output = relay.Tuple([call_7248,])
output2 = relay.Tuple([call_7249,])
func_7263 = relay.Function([], output)
mod['func_7263'] = func_7263
mod = relay.transform.InferType()(mod)
output = func_7263()
func_7264 = relay.Function([], output)
mutated_mod['func_7264'] = func_7264
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7335 = relay.const([[[-3.415456,-0.597213,-4.627176,0.969108,0.691279,2.958052,-2.149640,7.375628,-6.312866,0.250901,0.916168,-0.079789,-6.675027,-4.686988,7.610262],[9.875664,2.529843,-8.844773,9.158930,-8.045423,-3.707947,-9.475379,1.677255,0.188119,-9.582821,3.311199,-8.420713,-5.843163,-6.468852,1.304699],[-8.103818,-7.343292,-2.889254,4.077930,-7.627189,-0.519220,3.470536,6.602107,6.111412,-2.457015,9.336961,4.614866,7.605580,-5.073482,-8.816752],[-7.840119,-5.557548,-6.078145,3.775893,1.283576,4.524044,-1.003096,-7.755817,8.235933,-7.666965,-4.334221,-2.546075,0.883554,1.318134,1.539813],[6.565085,-4.544018,-7.203241,-9.560382,-1.903138,-8.062245,-2.801995,2.304262,-7.940889,-7.237368,-1.739374,8.803124,-6.734031,5.047046,-2.458967],[5.283764,-0.040466,-0.260227,9.330858,-0.398644,-7.359283,6.636132,0.212330,3.094087,-2.255744,-1.153131,-1.275706,3.171659,-7.117273,-1.398018],[2.540313,2.252670,3.621205,7.526781,-4.568050,1.691496,-9.911619,3.744342,5.916339,7.425066,-9.514883,-4.497505,7.510774,5.398747,-8.589375],[6.202084,-4.604625,7.071007,-4.291196,-5.830179,-9.302640,0.887752,-5.592386,-2.855599,8.790619,7.637095,5.135694,5.741640,3.053902,0.343157],[-3.356762,-8.873380,5.403240,0.751718,-4.935986,-3.373024,6.404680,2.508586,4.086916,1.499366,8.362159,-0.151844,-9.210624,-5.340007,7.954722],[-9.743962,-9.163808,-6.440785,-0.334643,0.647312,2.014476,-3.108472,9.585083,-4.466882,9.132733,3.335869,1.971873,-0.444016,9.350653,4.735950],[-7.516430,5.628876,-4.060505,-1.053699,6.657049,7.187210,0.455706,6.982878,1.067157,0.632483,7.781774,-3.697093,8.437140,-9.443549,6.763803],[5.812801,3.999997,-5.152542,-0.268685,5.756501,-6.128409,-8.088350,-8.877961,-7.880742,1.894055,-3.225514,-2.601573,6.451551,3.713891,3.707818],[-1.789937,-9.822841,3.310395,9.402036,1.322386,7.305365,-6.688175,-0.561134,5.643085,-0.987301,-9.900953,0.892904,3.788840,-6.960112,-3.721545],[0.403587,-2.297690,4.716391,-8.912534,8.758603,7.467422,6.331032,-6.007401,-7.922438,-3.358233,7.556688,5.480057,-9.832812,4.244939,-8.080907],[-4.358981,-6.345148,3.203757,-7.741286,8.988160,-7.779741,-2.922156,-6.725171,6.462255,-9.448913,0.759677,-1.253297,-2.989713,-7.276813,-8.416924],[5.447995,-2.521056,3.012863,3.201003,-3.910412,-7.544089,0.585317,-1.592516,1.500994,-1.387286,-2.095864,5.581238,9.930306,7.479724,-1.766834]],[[-9.045409,-5.760812,1.225025,-0.541316,0.668843,9.725097,9.366997,-5.398502,-8.326589,7.986543,7.247527,6.315958,6.516328,-1.693968,-1.089568],[-3.682566,-2.794903,7.723795,-4.170393,4.349764,-4.475947,3.342401,4.848517,-4.796014,-3.457169,7.852096,4.195711,-1.875133,7.848756,5.370155],[7.123947,-7.122550,-4.882850,-5.035746,1.687620,-4.425644,-5.627609,-8.083033,9.830726,-1.422268,-6.655763,9.161799,-7.866710,-0.225192,-8.329641],[5.929887,1.426446,9.616131,9.466542,1.611560,6.310975,3.420431,8.503462,-7.653485,-4.596807,-0.649486,-5.958673,-0.535337,-8.455035,-8.420183],[-2.223293,-7.987294,7.170523,0.035995,8.629645,2.948038,-5.222322,7.757326,-6.830110,-6.405690,-9.418340,-7.393299,-5.264204,2.095445,2.110624],[3.338543,3.020615,-1.405679,7.358145,9.273326,-2.785133,-3.874780,5.859256,-4.223864,9.628679,-5.520173,-3.835451,-8.299224,0.815874,9.729365],[0.612936,-1.687666,-6.519931,1.298796,-0.615905,4.111134,3.418382,7.069197,1.383468,0.112691,-2.544428,-2.879513,-8.281757,7.117394,-1.306854],[-1.725440,1.108919,-2.352782,0.909081,-8.367142,-0.103663,-1.171236,2.778479,8.311723,-5.072128,0.063046,-2.938344,8.722962,-3.587370,2.099540],[0.518098,-7.258800,-5.015817,-4.817512,-0.571100,-2.495254,-8.761888,-6.026251,-4.596356,-8.668127,-5.175666,-7.853113,7.289921,5.660559,-1.048660],[-9.673554,4.715685,3.368853,4.204322,5.014889,-3.865018,3.426570,0.750408,-6.483728,5.202399,-4.452090,-1.613079,-7.133152,-2.832527,5.972131],[-7.708282,-4.861232,-8.377494,-8.382198,9.235323,8.348096,7.332454,4.314051,-9.367331,-7.882715,-6.529098,-3.813155,8.527497,8.920775,-9.362450],[7.149062,-9.597597,-1.679980,7.577339,0.387823,5.688639,-4.357594,2.311989,7.033890,0.722162,3.458909,-0.586724,-2.602293,-2.602697,2.109027],[-2.684480,-8.465440,-1.680820,1.644016,6.690512,-6.090132,4.817989,7.285607,-6.041447,-1.918578,-2.766232,-2.993218,3.293959,0.681704,-2.029558],[6.911125,8.487341,3.404182,-7.654873,5.759207,0.490422,-7.497508,-8.743604,8.316984,-0.917072,-8.656345,3.837330,5.724253,4.014902,0.089079],[8.858136,-2.865298,-1.319181,-3.593435,-1.027458,-1.248360,-8.997000,-5.243109,-1.344122,8.053681,1.835837,6.550702,-7.122554,-5.772233,5.029579],[0.911619,-0.446726,9.766177,-1.082377,4.363520,8.374636,-4.016109,5.994849,-2.187339,9.165556,-1.722723,3.848608,3.028337,7.346727,8.268774]],[[4.541951,2.945394,-8.070354,-8.597907,9.796623,8.574464,6.066318,-1.856354,-1.792034,-4.214531,-4.699761,3.008753,0.636172,-0.921113,-0.930318],[7.103030,-2.276136,5.525832,-6.557562,2.905234,5.770640,-7.878637,5.879575,0.488784,-9.142948,9.263497,0.486278,-6.791925,8.568882,6.202530],[6.022059,-2.741023,9.498972,-9.171224,9.205007,4.748981,9.222377,-4.182472,-0.498712,-3.137146,6.666273,-1.428257,-7.119014,6.730597,3.756396],[7.320185,-1.431826,-2.661138,4.813851,0.299822,8.568094,-2.634458,-1.475970,8.205828,-3.901745,1.193949,6.788340,-0.758068,7.635724,6.307437],[-8.668707,6.693054,-4.159072,4.421049,-9.833211,2.348663,9.244602,-0.036583,-8.850057,0.476462,-4.271968,-5.645636,-5.115158,5.881964,6.072440],[-3.292328,-6.536669,-2.146015,2.245015,-6.638211,-6.548383,6.985290,0.295403,4.980357,0.570161,8.402034,-3.731756,0.033126,-1.407279,-8.994388],[-7.901430,-3.168093,-8.254734,6.110130,-8.069472,3.690467,1.393681,-8.586453,4.191412,-9.323627,-9.611836,-1.274746,-4.263964,2.557449,-4.282264],[-2.625446,-3.522115,8.360501,2.005376,3.310411,5.756103,-3.412464,5.570759,6.650022,-8.944715,-2.654286,4.079638,2.237260,-2.604247,3.656942],[-8.188748,3.254497,-4.237688,8.779669,-8.558055,4.487418,-6.628429,-7.670290,-4.517438,-1.022301,-1.454138,-3.525431,8.720934,5.695856,-8.351843],[-8.782366,-6.110259,-1.120326,4.035177,-6.995436,-8.830308,5.000957,3.103959,-7.939019,1.498372,-3.114843,3.461226,-5.921715,9.763363,1.246290],[-1.272186,-0.079866,2.059088,4.852222,3.853651,-8.772376,8.726658,-3.412288,-0.286434,-9.762262,7.973347,9.024859,3.434859,6.526204,7.107201],[2.786805,-4.340964,-6.507633,-3.795872,-1.779427,3.717398,1.939788,-6.606860,8.026336,-1.440084,4.357374,-8.645823,8.617603,-9.768439,-1.535720],[5.255294,8.320876,-5.003036,2.007203,6.541188,-5.187760,1.569566,3.305591,0.659664,-2.955345,-5.474226,5.664558,-6.523137,1.373714,8.877610],[-2.074964,9.871808,-9.634368,1.635491,-7.407636,-5.295795,3.497817,-7.567724,0.722434,6.740430,3.034629,2.429772,-7.871308,3.106260,-2.528930],[-4.195585,5.197707,-7.114087,0.909791,-1.670329,-8.496437,-7.412410,-5.271337,-7.845915,-2.802960,8.379413,-4.082653,-3.665514,-3.304827,-3.574473],[-5.295542,2.549432,-8.949819,1.468516,2.702691,6.184614,-5.266341,6.319961,-6.102275,8.853835,6.805244,-8.061759,3.200182,-0.901509,1.384493]],[[9.522505,0.852622,3.340558,-9.103477,1.512985,-4.996601,-1.403834,-6.601027,6.369075,9.992004,8.827728,3.534305,-3.455682,-1.788589,-2.727831],[9.596846,5.473010,-3.608545,-9.268960,-5.929733,-5.361798,-8.266140,4.894586,-3.542141,8.727974,7.100230,-8.535985,3.123282,-7.467714,-3.149200],[9.809067,-4.632149,-1.221594,5.129046,2.080383,6.958876,9.733126,-1.573789,-5.062717,9.800359,7.361679,7.999519,-3.141024,-6.643565,-6.282461],[3.861961,9.302568,9.324033,8.938756,-0.925657,-5.157305,-7.484683,-2.937368,-8.540749,-2.691908,-6.684063,0.695547,7.739923,-1.423910,-4.842486],[-1.657810,-8.109334,5.749402,-5.396278,8.201776,9.618388,-0.879231,1.722201,1.974982,5.311394,9.650639,4.432156,8.863698,-4.825926,-3.792709],[3.262593,5.905698,-5.992406,4.545704,4.176627,-7.176184,-1.379216,-4.650723,3.988243,7.096774,4.861816,-5.398146,3.538558,-4.013102,-6.676509],[-8.867644,1.146567,3.254010,-4.733036,-9.083841,1.269285,9.256180,8.073755,5.839890,9.798608,-0.571039,-2.638508,8.481964,-8.462763,0.951029],[-1.384955,-2.249760,1.616190,-8.210940,-8.044240,1.217351,6.077410,6.256049,7.015938,9.187669,-6.540941,5.463045,-5.208518,-4.722401,-4.717769],[5.410711,-8.482223,7.920972,-9.367646,8.356904,-9.093870,-6.095843,0.602370,2.253795,8.296405,5.597473,-8.263868,-9.110795,5.392344,1.488968],[-7.305780,4.760437,3.928444,4.335247,-6.430411,-3.638193,1.211925,-6.592712,5.674270,3.285086,-1.947520,-6.400755,-5.698452,8.059752,0.233079],[2.988167,-4.180142,-7.871781,2.571136,1.042881,7.161602,5.235346,-5.429017,0.354516,2.965422,-9.636661,-3.408517,-4.668784,3.200889,-8.329217],[-1.572983,7.566492,-2.433481,-1.521024,0.045514,1.647735,-3.945697,0.525560,-6.778786,-2.959156,-2.970890,0.506276,1.335425,4.493388,-7.520798],[5.341432,3.458949,3.830907,6.121713,-2.896274,4.725703,1.390977,-2.760509,-5.641306,0.051842,-9.468459,-2.231266,-4.817055,8.762685,-7.773757],[-9.651643,-5.062680,-2.548252,5.597761,-6.927273,-2.664185,-3.662379,7.060953,4.103181,9.681562,-0.587561,-1.552885,-0.246519,-8.603920,-2.804291],[1.894995,-9.573868,-6.786231,4.514311,-7.487617,3.374109,1.220766,-8.235692,-0.148384,-7.506369,7.934072,2.871685,3.218348,-9.555810,8.992238],[6.851444,1.328363,0.589084,-2.600566,-0.290944,-2.824595,-0.136296,3.181431,-9.726079,-9.012049,5.288004,1.554335,2.982210,-3.233085,-9.284128]],[[-4.944185,-0.882107,8.535410,0.483035,-9.309187,7.176932,-9.505113,-7.403497,-5.122365,0.592805,-0.414347,-0.885890,-3.264028,-9.299279,-6.212525],[-2.671667,-9.664861,-7.047300,-0.449059,-4.971517,2.740236,4.823792,9.924603,6.768852,-9.849128,-4.131041,-8.844929,-6.929113,-3.365070,2.353652],[4.473239,2.713088,9.764700,-0.932327,9.661948,-0.769732,-2.262131,-6.473951,-3.741918,5.168383,0.187012,7.276804,0.167268,-4.444878,-9.900525],[-0.285248,1.493832,-8.298750,9.711425,0.146001,9.282905,-0.612125,7.168860,1.052191,-6.956179,4.198473,-1.038596,6.730612,-7.972560,4.051729],[-7.863509,5.002448,1.296501,-3.859763,-2.747137,5.414410,7.706597,4.478235,9.751548,-0.052884,3.392425,3.354144,-2.058940,5.838410,-4.969538],[-9.635022,-6.073244,-3.855744,0.365478,6.546834,-8.131530,4.024714,-6.431146,0.926039,3.812328,4.024268,4.195685,-7.593750,-8.715004,-4.034266],[-8.031257,5.958883,-4.294477,-3.813952,-9.438068,2.265144,-3.258845,-1.613789,2.456261,-6.085328,-5.623191,-6.471347,-2.296466,0.720789,-2.791631],[9.612967,-0.691886,-7.130314,1.288965,-3.036251,-6.684311,-5.613376,-9.161766,1.185197,-4.896258,-4.000762,7.278540,-5.103373,6.942211,-1.575169],[-8.170727,-9.753846,-9.315443,8.129239,4.371003,5.559817,-7.349009,8.425385,2.005414,-2.232928,-6.165776,-4.069711,9.871938,-5.716918,-5.910910],[3.897163,-5.220885,-3.592615,-2.940494,-2.448816,5.230166,7.959858,-1.560190,3.705972,9.080425,6.792281,-2.573402,6.481822,0.490857,7.510409],[6.083084,-9.089689,-9.811879,-0.840762,-8.197507,0.719427,2.240580,5.602060,5.998822,8.021527,7.563053,-6.188496,-1.381376,8.345994,9.162046],[4.891210,4.943046,7.166803,-5.677764,-3.012311,-3.562333,9.576194,-3.645160,9.046635,6.824263,-9.342946,-4.059088,-7.029328,8.515959,-3.035405],[-7.116858,7.183733,2.792775,-1.456853,-8.391176,-1.402486,-7.148177,-9.756055,3.731069,-9.349453,-4.679076,9.928591,5.493609,9.300097,1.188516],[-2.117699,-7.567541,-9.754436,-7.099043,8.809027,5.702902,8.371994,1.778411,0.561472,-4.851919,3.490456,-9.584537,5.651447,3.606581,-1.587940],[-4.523337,-6.190460,-5.882097,-6.382116,7.710597,-1.880696,6.719957,-4.807048,8.559020,7.332919,5.347388,6.724468,7.972032,-4.668359,8.634089],[-9.619484,8.608792,-7.799029,2.409682,-7.397546,4.278602,0.634006,-8.284573,3.401891,8.178999,9.829916,-2.448974,3.662371,0.654605,-5.829147]],[[-8.816479,-1.409070,8.499361,-3.284323,7.592717,-2.702902,3.266481,-7.529378,6.546076,4.027219,-0.009679,-8.708187,4.126236,3.245497,7.420118],[-8.117651,-9.852753,4.665043,5.046040,-9.703466,-6.023912,6.243704,-2.230179,5.618476,-4.412565,7.684198,-4.392017,2.539117,7.723109,-0.366654],[-6.711398,-8.626736,-9.711298,-0.243464,4.320594,-9.225431,7.220143,8.080100,6.640846,-7.268050,-2.948888,8.571427,4.976343,-8.120442,7.402005],[3.864999,2.051198,-1.721544,0.840760,-0.208683,5.187049,-5.150213,-5.253563,-8.974777,-2.563297,1.845302,-4.688584,9.006867,9.637809,-5.385166],[6.055850,-2.598988,-9.990216,-2.626574,-7.373370,-7.598749,2.382151,-0.812198,9.406818,-8.587001,0.005682,-8.885369,-9.447780,8.958717,9.878575],[-6.858379,9.321776,-2.461658,9.441990,0.116877,4.448309,9.869685,-1.937784,-4.215675,-3.182503,-0.727587,3.469845,-9.929702,-7.543067,1.679028],[5.246548,-6.258383,7.140630,-6.791568,1.781053,-0.742637,-0.241649,-4.114554,7.812650,-7.651633,0.842855,-3.869588,6.900330,-8.154283,-1.340096],[4.822163,9.374919,0.529949,-6.336528,8.922256,6.540151,-2.375300,8.562458,1.640246,-0.516464,-9.109495,-4.602130,-3.916686,4.643101,5.743483],[-7.281160,-1.006395,5.255360,-0.815296,7.003127,0.654299,8.732502,-5.095829,-2.043983,-0.604009,3.374178,-0.058001,1.728950,2.101322,5.046633],[-3.813386,-3.883432,8.708498,-3.811242,7.495840,7.409696,5.845088,9.442968,2.429806,8.043693,-8.741937,6.265741,-9.081632,1.551014,7.115028],[-5.190233,-5.645138,-9.813571,-3.693766,-4.417858,4.075358,6.267132,-2.601869,-2.879583,-8.004491,7.678806,3.075866,-4.466072,5.351932,1.061546],[-1.397551,8.470255,-6.334117,4.971632,-4.039096,7.458759,7.516985,-2.170995,3.435871,-4.168979,-3.917315,-5.083496,-3.069130,4.015248,-5.844995],[-1.244021,3.729124,7.362839,-3.301435,-0.557395,-6.044430,-7.428963,-6.051635,-8.959501,8.789167,-1.941773,-8.930415,7.031816,6.899396,7.844019],[-0.612061,-0.838610,1.846072,1.154055,-9.572915,-6.954777,9.253740,3.617827,-6.722428,9.345884,-8.031552,5.078185,-6.388673,5.313806,-2.364695],[7.355831,-9.066338,-9.238114,-1.591008,2.675561,1.776272,9.946156,-7.242958,2.881758,-9.020651,2.120778,-1.009182,-4.402516,0.811619,-3.295056],[-4.634519,-1.378158,2.380598,-9.989428,6.055314,5.472194,3.687503,9.255441,8.904794,-7.170692,-2.180115,-5.119614,7.662131,6.942639,-9.166141]],[[-7.463033,-7.653584,8.775308,0.285977,5.780135,-2.014782,6.257739,7.216653,5.065131,0.812559,1.172298,4.353144,-9.059300,-5.378731,-7.534394],[8.074956,9.410905,5.398230,-5.037035,-3.601171,8.738117,-6.102858,-6.651720,-4.523632,-1.129472,-6.808305,5.536102,0.745098,-7.288060,1.885181],[-2.649054,6.045734,-7.266691,-5.721163,6.273903,-6.022097,6.756485,6.016387,5.176092,-5.677959,-9.135252,8.064185,-7.160292,1.695516,-2.207522],[3.861684,-1.952227,-2.566599,-6.021584,5.471046,0.673687,-8.543206,-8.469685,-9.447420,9.810653,4.458587,6.040787,3.954547,7.287040,-5.338169],[-3.929874,-0.663488,-7.358630,5.827171,8.713192,-3.825015,1.291464,-7.463910,4.942882,2.377387,5.462018,-3.510992,3.529073,-5.461811,-6.266349],[-3.189449,0.254927,8.444151,2.235586,-0.153871,4.598179,5.861716,9.292442,-3.045719,-6.318620,-5.698305,-3.271985,0.578712,-3.160251,-3.146541],[-4.573018,8.395215,6.219855,-6.385818,-7.177678,-6.183070,0.964117,-5.966158,8.434340,3.789789,-4.078374,0.269388,-1.306909,-1.089076,-3.739837],[-9.068795,5.591837,-5.541557,-6.672874,0.714606,6.774041,2.475454,8.004797,-5.502465,-6.958690,-0.011478,2.376853,-2.537886,-3.474628,-2.103881],[4.647541,-8.211081,8.197210,-1.295570,2.316924,-2.055702,0.630725,7.372422,3.832008,1.725037,-0.798717,-5.902439,5.023194,4.751073,0.400297],[-4.214744,-3.008092,9.057481,-2.219360,-5.318882,5.680989,-4.313244,-4.373191,7.887196,0.167929,1.694742,-6.045050,9.370289,-3.965582,-7.662309],[3.933976,2.232645,7.284702,7.424159,-1.797633,4.707454,-8.276120,-5.650811,7.544929,-3.077989,-2.159117,-8.964859,0.381308,-9.797717,8.730669],[3.702047,7.758288,-8.118020,1.880067,-6.560382,9.301276,4.377049,-1.995425,-3.710626,4.701268,-2.517271,1.760508,-8.886041,2.387494,-3.640094],[3.157059,5.697096,-6.984567,3.287184,9.048669,5.400129,0.820975,-5.643627,-7.671309,-0.857977,3.062345,1.474824,5.554520,6.312541,-6.881551],[5.680791,0.337934,0.386229,7.157738,7.295527,-8.328446,5.741943,9.213421,1.709333,5.732042,1.841493,1.248401,8.026216,-9.138325,1.192160],[-8.198812,5.596921,3.977719,-3.179492,6.686627,0.230143,-5.958665,-8.517820,-4.586304,-0.392936,6.608878,-2.790176,-7.539556,4.288367,-0.469379],[-6.820880,-4.421473,-1.565009,-1.634562,-3.046885,-8.293894,4.451265,-4.060081,-6.165857,-4.289907,-6.855015,-1.315838,-4.368781,-5.518971,9.174835]],[[-0.242892,-3.651707,0.959957,-5.676722,4.440951,-1.568121,-0.908690,-9.447098,4.753438,7.336770,5.766941,1.778226,-6.203435,9.802390,5.232523],[7.762860,-8.356441,-5.512272,-3.675380,9.234358,7.680125,9.194670,7.804451,1.991431,-1.655234,-5.844530,-0.005937,5.306534,5.639639,-0.708463],[0.292408,-4.046107,1.721067,-8.115988,4.773598,2.221032,2.808072,-4.682830,-2.350791,9.781099,-9.318377,9.935522,4.942929,9.247246,0.009190],[8.351084,7.349890,-2.099268,7.981962,-7.960451,-8.484639,6.425991,-3.952851,-7.901968,4.924479,8.291438,-7.003995,9.629526,4.942009,-6.414852],[-4.118416,-8.197296,-0.664779,-7.741171,3.771443,-6.028709,-6.310446,2.816437,-1.528937,8.342146,6.066684,5.469303,2.150802,9.232797,-0.634750],[4.027748,4.666662,-6.296394,-6.785917,3.376142,-9.464805,0.083330,-7.408731,0.851104,6.586364,-5.202298,-4.430083,-7.266558,-8.083656,-9.697225],[3.560395,4.637062,4.159991,-9.588790,-8.414788,4.197141,-0.427659,3.044924,6.100651,8.893622,-6.564797,6.456287,4.996431,-7.767758,8.353912],[-3.313666,9.530903,-3.287726,-4.163027,-4.012762,-3.877571,9.775262,8.003399,6.627509,6.132314,2.420612,4.859887,-8.006227,-4.277681,-1.219440],[-4.499319,-0.322289,7.488209,-5.340676,-5.003319,-4.535012,5.776612,1.031041,0.182280,9.084652,7.569769,-8.825347,-9.612784,8.489909,6.506501],[-1.421104,3.627934,5.261344,0.183214,-8.602409,3.417706,5.363732,-5.632312,5.094612,7.754841,-9.977731,0.043200,3.923909,-9.815844,-4.312726],[2.306491,2.051410,7.883504,4.303443,-2.125684,-4.774239,-7.713216,-6.293257,-0.549608,-5.383280,3.304390,-4.983564,5.073087,-3.227214,7.658522],[-4.716861,5.947631,7.994887,-5.338058,-8.999862,-8.174670,-7.943793,-4.416081,0.525000,-9.346680,-1.050409,-8.339886,-4.348980,0.382832,4.942001],[1.621100,8.122025,0.075734,-3.092812,9.620973,3.453528,0.896203,-6.952016,-6.465551,0.179546,-6.357310,-1.654486,-6.076100,-3.551860,5.810629],[-0.688585,1.855156,-3.119103,-2.193346,9.992666,0.956983,4.273548,-3.045945,-6.392402,3.739291,-9.193424,3.825860,6.992100,8.518540,6.243788],[3.109612,-3.835667,6.639633,-0.156126,5.418878,2.838171,-1.059069,4.078094,3.676809,1.201351,7.620930,-5.469338,5.867761,9.880195,1.838350],[1.268644,-7.539305,-5.391919,-3.101860,-0.583241,-3.743790,-0.577799,-0.497894,0.381192,8.669271,9.232246,-4.666828,-0.673451,1.853594,3.516337]],[[-7.734401,1.600432,-3.735990,1.935954,-0.020859,-7.925544,7.200448,6.930191,-9.663966,7.273559,-8.224848,7.382425,-4.325449,-6.901545,9.035689],[9.509994,-6.626217,-6.411686,-3.869969,-6.947367,6.386043,2.878047,3.783663,5.724724,9.588106,-3.728351,4.535977,5.562983,1.827044,0.931126],[3.570333,-3.312286,7.522537,-9.341301,-2.169130,7.026643,4.863259,7.593056,1.082614,-8.243607,8.721806,-5.398903,-3.980328,3.724430,1.764834],[-2.288216,3.326727,7.609814,-1.809465,-2.180957,-3.150299,-1.566337,-3.232346,-0.411173,-4.168510,-7.689369,1.078719,-3.035642,-0.663058,6.757989],[-6.679590,-0.607023,1.540186,2.438356,1.841730,-6.461347,9.752359,2.649488,-8.782906,4.578779,1.770820,2.376974,5.559406,-4.795340,6.995916],[4.119499,-8.941802,3.093301,8.419333,6.007057,-8.014746,-5.632002,-6.296360,0.280544,-7.616098,-8.931948,-1.828884,-8.058138,3.119209,-3.656661],[0.612538,6.383971,9.231396,4.822380,7.559951,-0.677584,-9.644419,1.885717,-5.238269,-5.216256,0.948675,-3.663807,-7.676097,6.731015,-0.150282],[-4.878484,-3.553006,2.447904,-4.158354,-8.566566,4.798306,8.674612,-9.855377,-3.372867,3.814122,3.327471,5.966490,-3.616416,-7.277816,-2.051567],[7.418315,-6.892452,-5.559301,-7.312959,-4.994672,-1.574673,2.919502,-1.921754,-5.393132,-0.167147,1.171857,-0.303923,-2.010458,-4.474485,9.149686],[3.898922,8.027247,-2.225722,7.207766,-4.685154,0.279126,6.289217,-5.356036,-7.112029,-9.246142,-9.679791,-4.162077,4.181445,7.455055,-9.005990],[-4.510889,-3.229123,8.565156,2.791018,5.336243,6.479991,-8.156146,3.774072,-4.920896,2.701469,-2.506158,-6.509971,-1.474479,9.898799,7.067175],[-9.607167,4.691571,3.454649,5.567031,2.043004,-8.937848,-0.404755,0.105397,0.845652,3.213670,7.884319,-5.652317,9.279466,1.441911,-5.299869],[-1.966009,-9.441136,5.260970,-1.020805,-3.979186,2.108723,-4.746912,6.393848,7.939766,9.969017,6.868868,0.080157,-8.681251,-3.141232,0.982574],[-0.270962,-3.693714,-3.514613,-2.496138,-4.705335,-6.643820,8.655038,8.866661,9.533374,6.094303,-6.851864,1.765577,-6.466593,-7.053168,9.760087],[-2.426720,3.531847,-0.916982,-0.935382,-5.339659,1.461162,9.931464,-9.331491,6.736012,4.943761,-9.630401,5.832228,7.528222,-4.466933,-4.399550],[-9.137123,9.484497,8.614595,0.948740,8.573528,6.354726,-3.364171,4.695279,2.284995,-3.534069,-7.123199,-2.976662,-4.412974,6.359744,2.178813]],[[-4.909537,-9.153065,5.548305,5.855768,-5.427572,9.794277,1.154908,-7.117990,-2.699842,3.794645,-3.125715,5.188718,8.687902,3.540708,-8.012146],[2.369299,-3.267288,1.895840,8.988026,-7.041798,5.185808,5.925286,9.564523,4.463332,-5.999214,1.498990,-1.120410,9.350616,-2.429010,2.018889],[-2.841508,-5.054363,-2.412438,-6.930061,-7.602577,0.925495,-5.077676,2.851392,-0.482755,0.277171,3.604195,-1.278602,-1.573554,-8.987729,-8.769689],[8.306760,-1.087467,3.101718,2.413963,-5.403776,-6.287524,7.778759,4.226049,-3.985435,-2.801937,-5.253592,-8.043749,8.782418,-3.290312,-8.259890],[0.627263,6.304253,6.382520,4.701427,2.474565,-8.079850,2.414765,-8.577338,-4.472649,7.691110,0.467999,7.559688,-3.031969,-5.840240,-0.153637],[7.154492,-8.723905,4.682869,4.682882,8.904722,-7.257534,-4.077265,1.972244,-5.191360,8.737154,-1.747363,5.976243,0.869925,5.409988,7.737341],[-7.993101,7.534354,4.696854,-1.535888,2.433672,6.159225,6.230602,-7.712449,3.918669,3.933525,-6.891970,0.732894,4.830576,6.032603,-3.443177],[-2.874470,7.158585,5.232013,-3.299664,4.189064,5.302702,0.403743,-0.928807,-8.338105,6.615560,-9.539816,7.342887,9.793832,-8.921428,8.345774],[5.858103,6.070614,-4.701066,-0.488144,-5.070788,-1.202833,-5.856219,0.973598,4.249975,-3.427927,9.311814,-3.735838,-7.674659,7.634827,-4.925079],[1.014904,-0.318627,-4.174166,-2.617268,5.836997,-2.120760,-3.858783,1.924474,1.462181,1.828131,5.153290,9.195826,-8.567228,-0.998120,-0.662009],[-8.928828,-6.520836,8.696701,1.348598,8.839781,-4.179669,6.457487,5.210620,-8.944497,5.633958,-9.376426,-4.608523,2.425266,-1.734306,-9.014073],[-6.964686,-0.015408,1.829991,-2.938928,4.700452,6.639043,5.477210,7.907086,-2.344587,-8.872330,1.254457,-1.889805,-8.630148,-1.492637,4.968180],[0.327824,-5.243063,0.114703,5.194535,-7.103852,3.418622,9.368047,-9.220231,6.267849,-1.769064,2.212993,9.931861,-8.263175,9.678535,-8.756661],[6.279705,-7.593367,3.981909,-3.596507,5.169104,-7.666381,-1.863541,-8.615426,-1.310486,0.822267,0.755118,-1.016245,2.037277,-1.887453,-2.618649],[6.448422,-4.398154,8.152036,4.339135,0.268052,-5.142973,-5.976190,6.046407,-5.714503,-4.145526,-5.640247,-0.658835,-1.246951,5.342813,-7.257607],[2.658562,-0.810911,8.790238,-0.516423,9.997284,-8.217292,3.729825,-2.306832,4.105234,-4.684817,7.864251,7.577272,3.023733,9.551015,-9.880351]],[[-4.960918,1.985888,2.335008,-8.533415,-6.452079,6.195226,-8.413345,9.292675,9.152711,1.060511,-6.093460,3.013964,-2.045469,-8.203840,4.515576],[7.978952,-0.427737,-8.062860,8.443863,6.471583,-8.946003,-4.058283,9.383607,-0.521194,-1.421093,-7.859992,-1.499307,-7.562666,4.846992,-7.336448],[2.591939,-1.698033,-5.328001,-2.659490,-3.479769,6.586951,-8.455595,1.253448,3.950233,1.588532,1.311667,0.564592,8.017124,-5.475508,-0.131877],[4.083282,-2.734222,1.191722,1.926767,-7.359787,-5.575058,-5.010979,-3.832123,-7.544841,6.232866,2.638726,-0.958559,-9.037693,0.412082,-2.014632],[4.263540,4.234929,8.209248,1.752856,-0.386489,-8.083505,0.198960,-3.921876,-1.644859,-1.240286,-8.800346,-4.189555,-7.012034,-4.497878,7.492137],[8.732421,-0.736137,-0.022426,4.232632,-3.864572,-0.631380,-2.550480,-9.193222,1.631760,-1.806842,-8.028946,1.191060,1.462286,-7.001138,1.091068],[-7.591947,-0.994624,-9.454300,-9.612615,-4.057155,7.022768,-4.566956,1.400498,-4.925671,7.957463,-7.937140,6.990628,2.175190,7.190121,-2.388794],[2.311254,4.231647,-1.059192,5.904417,8.961818,8.033268,-9.362208,3.177473,-1.278842,-7.313665,-4.991068,-2.244183,-0.576741,-6.661733,8.937387],[3.445213,4.914809,-2.371676,-2.158882,-4.170026,-6.516842,-1.053466,2.850995,-0.847806,-2.670727,-3.868798,6.358682,-4.587221,-1.043506,3.604325],[-0.301511,-9.406299,1.119462,0.381885,-6.459566,1.401449,0.998988,6.573426,1.157406,1.693359,-2.592092,-1.466700,-5.498890,-1.356207,5.895112],[-9.681674,-4.385408,4.477092,5.747156,9.727611,6.430579,-3.109637,-5.449565,2.675777,8.226164,6.378174,-7.481873,5.250175,1.296807,1.918205],[4.682800,-9.801829,9.598444,1.749300,-2.647741,-6.297831,-4.517471,-0.468741,3.971622,-5.591010,-6.833205,-4.298829,-3.013895,5.548177,7.693019],[-6.171059,-2.513756,-4.188007,4.440262,6.526726,-7.222909,7.979368,-8.464534,-9.910572,6.445794,6.057120,-0.882590,7.004065,0.853303,-4.239325],[1.261472,-8.119288,5.352561,5.834504,-0.481259,-9.815350,9.566694,7.536494,-3.622911,9.240327,6.823981,8.318818,-6.195379,-5.907745,-6.238728],[5.208246,5.900864,6.627868,-5.815866,8.835701,7.334489,-5.365564,4.627830,6.469774,1.663306,-9.903805,2.268550,-8.239210,-5.961103,9.734071],[-2.930011,-9.516624,-0.876181,-6.432021,0.979313,-1.051003,-8.840911,3.175256,-3.115961,1.159203,3.890235,-2.110743,8.533151,-6.630219,3.676095]],[[-6.656924,-5.422353,-5.078551,9.727035,-7.621780,-0.469956,2.969329,9.426925,9.704475,7.026662,4.230138,-6.800615,8.851675,-4.175795,2.359232],[-8.091440,9.544852,-2.487719,9.537258,3.181862,-6.699642,-0.531648,-5.230662,-6.703585,-5.022479,-8.843099,-4.255238,0.944195,-0.068683,-5.893993],[-4.190865,-2.247620,4.431984,2.476802,-4.989232,-6.230082,-6.535954,-4.511842,-5.797809,-6.168770,8.392447,-0.461886,4.019107,7.634912,-3.307574],[2.086630,-5.882280,-4.096444,4.670988,3.138321,-9.943806,-1.525984,-0.527697,2.389748,-6.619746,2.547893,-0.291109,8.154680,-7.170143,-0.975022],[-1.351943,4.247044,6.977973,4.999253,5.609209,-3.471441,-3.532964,-9.757382,7.935796,-0.422230,-3.248075,0.823298,2.698580,-2.750746,-8.748183],[-9.664510,7.735116,7.664993,-8.043579,7.309891,9.573748,8.495682,-3.487658,3.011163,-5.371224,8.266002,4.539399,2.468900,-4.302630,-0.843217],[-7.020130,2.836850,-8.561873,-4.173847,9.903517,-1.130484,8.969041,9.528028,-5.541753,-1.631092,-0.248200,7.277159,-1.579522,-9.779270,-1.174473],[1.951473,-3.490411,-5.014876,-7.264968,6.016084,-3.655310,-1.405849,4.907066,-8.986434,-4.801874,-5.416788,-4.001083,8.660759,5.495865,5.117216],[-5.289235,-2.296777,-9.647725,-4.635689,-7.222024,-2.440565,1.394450,-4.272256,-2.523046,-9.888666,3.076020,0.487415,-6.914586,6.548819,4.329933],[-1.737432,3.936095,-3.193002,1.106229,-4.718461,-2.248209,3.576752,-1.238672,-9.125731,-0.129395,4.466244,-5.599289,0.529311,2.434595,-5.699011],[-4.833757,5.257436,2.072964,9.227499,-5.252032,-3.616947,-0.498321,-6.036219,-0.637941,-1.406632,-8.126178,-8.490859,-5.855280,4.146331,-8.955882],[-3.125176,-9.151774,0.963132,9.431814,2.004510,-6.904772,-1.622300,3.761182,5.196573,-9.941332,-7.562156,-9.764838,4.998085,-0.522004,-5.423268],[-9.765522,4.020263,-5.758001,-8.674444,2.363388,1.159915,-1.171553,6.372771,9.783446,7.896508,-3.844666,-8.613005,-7.247240,4.291330,-2.404614],[-2.597514,9.844985,-2.919614,-2.730946,6.910641,-0.807558,5.307496,5.420807,-4.253361,-1.354704,-9.715024,8.211043,2.177994,-1.013445,-2.999626],[-4.490470,7.686821,6.137272,-3.336185,-4.468203,5.954793,-1.921681,4.620223,8.390373,-7.317154,3.019821,-8.424059,8.170700,1.177046,8.466255],[8.492237,-6.458927,5.271656,-5.568985,5.058415,7.706046,7.095548,8.076725,6.909963,-3.869013,-1.271046,-3.394032,-6.769582,-5.408358,9.435386]]], dtype = "float64")#candidate|7335|(12, 16, 15)|const|float64
uop_7336 = relay.log10(const_7335.astype('float64')) # shape=(12, 16, 15)
output = relay.Tuple([uop_7336,])
output2 = relay.Tuple([uop_7336,])
func_7350 = relay.Function([], output)
mod['func_7350'] = func_7350
mod = relay.transform.InferType()(mod)
output = func_7350()
func_7351 = relay.Function([], output)
mutated_mod['func_7351'] = func_7351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5414_call = mod.get_global_var('func_5414')
func_5415_call = mutated_mod.get_global_var('func_5415')
call_7389 = relay.TupleGetItem(func_5414_call(), 0)
call_7390 = relay.TupleGetItem(func_5415_call(), 0)
var_7394 = relay.var("var_7394", dtype = "float32", shape = (9, 405, 15))#candidate|7394|(9, 405, 15)|var|float32
bop_7395 = relay.logical_or(call_7389.astype('bool'), relay.reshape(var_7394.astype('bool'), relay.shape_of(call_7389))) # shape=(9, 405, 15)
bop_7398 = relay.logical_or(call_7390.astype('bool'), relay.reshape(var_7394.astype('bool'), relay.shape_of(call_7390))) # shape=(9, 405, 15)
output = bop_7395
output2 = bop_7398
func_7406 = relay.Function([var_7394,], output)
mod['func_7406'] = func_7406
mod = relay.transform.InferType()(mod)
mutated_mod['func_7406'] = func_7406
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7407 = relay.var("var_7407", dtype = "float32", shape = (9, 405, 15))#candidate|7407|(9, 405, 15)|var|float32
func_7406_call = mutated_mod.get_global_var('func_7406')
call_7408 = func_7406_call(var_7407)
output = call_7408
func_7409 = relay.Function([var_7407], output)
mutated_mod['func_7409'] = func_7409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1086_call = mod.get_global_var('func_1086')
func_1088_call = mutated_mod.get_global_var('func_1088')
call_7417 = relay.TupleGetItem(func_1086_call(), 0)
call_7418 = relay.TupleGetItem(func_1088_call(), 0)
func_5294_call = mod.get_global_var('func_5294')
func_5296_call = mutated_mod.get_global_var('func_5296')
var_7420 = relay.var("var_7420", dtype = "uint32", shape = (448,))#candidate|7420|(448,)|var|uint32
call_7419 = relay.TupleGetItem(func_5294_call(relay.reshape(var_7420.astype('uint32'), [2, 16, 14])), 0)
call_7421 = relay.TupleGetItem(func_5296_call(relay.reshape(var_7420.astype('uint32'), [2, 16, 14])), 0)
func_4174_call = mod.get_global_var('func_4174')
func_4176_call = mutated_mod.get_global_var('func_4176')
var_7425 = relay.var("var_7425", dtype = "float32", shape = (2025,))#candidate|7425|(2025,)|var|float32
call_7424 = relay.TupleGetItem(func_4174_call(relay.reshape(var_7425.astype('float32'), [9, 15, 15])), 2)
call_7426 = relay.TupleGetItem(func_4176_call(relay.reshape(var_7425.astype('float32'), [9, 15, 15])), 2)
uop_7428 = relay.acosh(call_7424.astype('float64')) # shape=(9, 15, 15)
uop_7430 = relay.acosh(call_7426.astype('float64')) # shape=(9, 15, 15)
func_2845_call = mod.get_global_var('func_2845')
func_2847_call = mutated_mod.get_global_var('func_2847')
call_7433 = relay.TupleGetItem(func_2845_call(), 0)
call_7434 = relay.TupleGetItem(func_2847_call(), 0)
output = relay.Tuple([call_7417,call_7419,var_7420,var_7425,uop_7428,call_7433,])
output2 = relay.Tuple([call_7418,call_7421,var_7420,var_7425,uop_7430,call_7434,])
func_7458 = relay.Function([var_7420,var_7425,], output)
mod['func_7458'] = func_7458
mod = relay.transform.InferType()(mod)
var_7459 = relay.var("var_7459", dtype = "uint32", shape = (448,))#candidate|7459|(448,)|var|uint32
var_7460 = relay.var("var_7460", dtype = "float32", shape = (2025,))#candidate|7460|(2025,)|var|float32
output = func_7458(var_7459,var_7460,)
func_7461 = relay.Function([var_7459,var_7460,], output)
mutated_mod['func_7461'] = func_7461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4008_call = mod.get_global_var('func_4008')
func_4009_call = mutated_mod.get_global_var('func_4009')
call_7470 = relay.TupleGetItem(func_4008_call(), 0)
call_7471 = relay.TupleGetItem(func_4009_call(), 0)
uop_7472 = relay.cos(call_7470.astype('float32')) # shape=(1, 324)
uop_7474 = relay.cos(call_7471.astype('float32')) # shape=(1, 324)
output = relay.Tuple([uop_7472,])
output2 = relay.Tuple([uop_7474,])
func_7479 = relay.Function([], output)
mod['func_7479'] = func_7479
mod = relay.transform.InferType()(mod)
mutated_mod['func_7479'] = func_7479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7479_call = mutated_mod.get_global_var('func_7479')
call_7480 = func_7479_call()
output = call_7480
func_7481 = relay.Function([], output)
mutated_mod['func_7481'] = func_7481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7484 = relay.var("var_7484", dtype = "float32", shape = (15, 7, 13))#candidate|7484|(15, 7, 13)|var|float32
uop_7485 = relay.acos(var_7484.astype('float32')) # shape=(15, 7, 13)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_7488 = relay.TupleGetItem(func_848_call(), 0)
call_7489 = relay.TupleGetItem(func_849_call(), 0)
output = relay.Tuple([uop_7485,call_7488,])
output2 = relay.Tuple([uop_7485,call_7489,])
func_7491 = relay.Function([var_7484,], output)
mod['func_7491'] = func_7491
mod = relay.transform.InferType()(mod)
var_7492 = relay.var("var_7492", dtype = "float32", shape = (15, 7, 13))#candidate|7492|(15, 7, 13)|var|float32
output = func_7491(var_7492)
func_7493 = relay.Function([var_7492], output)
mutated_mod['func_7493'] = func_7493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5052_call = mod.get_global_var('func_5052')
func_5054_call = mutated_mod.get_global_var('func_5054')
call_7530 = relay.TupleGetItem(func_5052_call(), 0)
call_7531 = relay.TupleGetItem(func_5054_call(), 0)
output = call_7530
output2 = call_7531
func_7532 = relay.Function([], output)
mod['func_7532'] = func_7532
mod = relay.transform.InferType()(mod)
mutated_mod['func_7532'] = func_7532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7532_call = mutated_mod.get_global_var('func_7532')
call_7533 = func_7532_call()
output = call_7533
func_7534 = relay.Function([], output)
mutated_mod['func_7534'] = func_7534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1392_call = mod.get_global_var('func_1392')
func_1393_call = mutated_mod.get_global_var('func_1393')
call_7566 = relay.TupleGetItem(func_1392_call(), 0)
call_7567 = relay.TupleGetItem(func_1393_call(), 0)
output = call_7566
output2 = call_7567
func_7585 = relay.Function([], output)
mod['func_7585'] = func_7585
mod = relay.transform.InferType()(mod)
output = func_7585()
func_7586 = relay.Function([], output)
mutated_mod['func_7586'] = func_7586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4304_call = mod.get_global_var('func_4304')
func_4306_call = mutated_mod.get_global_var('func_4306')
call_7605 = relay.TupleGetItem(func_4304_call(), 0)
call_7606 = relay.TupleGetItem(func_4306_call(), 0)
output = relay.Tuple([call_7605,])
output2 = relay.Tuple([call_7606,])
func_7612 = relay.Function([], output)
mod['func_7612'] = func_7612
mod = relay.transform.InferType()(mod)
mutated_mod['func_7612'] = func_7612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7612_call = mutated_mod.get_global_var('func_7612')
call_7613 = func_7612_call()
output = call_7613
func_7614 = relay.Function([], output)
mutated_mod['func_7614'] = func_7614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_7706 = relay.TupleGetItem(func_225_call(), 0)
call_7707 = relay.TupleGetItem(func_226_call(), 0)
output = relay.Tuple([call_7706,])
output2 = relay.Tuple([call_7707,])
func_7708 = relay.Function([], output)
mod['func_7708'] = func_7708
mod = relay.transform.InferType()(mod)
mutated_mod['func_7708'] = func_7708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7708_call = mutated_mod.get_global_var('func_7708')
call_7709 = func_7708_call()
output = call_7709
func_7710 = relay.Function([], output)
mutated_mod['func_7710'] = func_7710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_7717 = func_2031_call()
call_7718 = func_2031_call()
var_7726 = relay.var("var_7726", dtype = "float32", shape = (135,))#candidate|7726|(135,)|var|float32
bop_7727 = relay.divide(call_7717.astype('float64'), relay.reshape(var_7726.astype('float64'), relay.shape_of(call_7717))) # shape=(135,)
bop_7730 = relay.divide(call_7718.astype('float64'), relay.reshape(var_7726.astype('float64'), relay.shape_of(call_7718))) # shape=(135,)
output = relay.Tuple([bop_7727,])
output2 = relay.Tuple([bop_7730,])
func_7737 = relay.Function([var_7726,], output)
mod['func_7737'] = func_7737
mod = relay.transform.InferType()(mod)
var_7738 = relay.var("var_7738", dtype = "float32", shape = (135,))#candidate|7738|(135,)|var|float32
output = func_7737(var_7738)
func_7739 = relay.Function([var_7738], output)
mutated_mod['func_7739'] = func_7739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2845_call = mod.get_global_var('func_2845')
func_2847_call = mutated_mod.get_global_var('func_2847')
call_7744 = relay.TupleGetItem(func_2845_call(), 0)
call_7745 = relay.TupleGetItem(func_2847_call(), 0)
func_6240_call = mod.get_global_var('func_6240')
func_6244_call = mutated_mod.get_global_var('func_6244')
const_7747 = relay.const([2.280881,3.132204,3.525131,-6.029574,2.570892,-4.347209,-7.517166,-4.886240,-7.339196,-2.135186,-7.795776,-3.461068,9.224498,0.200310,-2.724955,6.953875,6.151407,-9.410740,0.943426,-5.023261,0.626338,9.174442,-9.596671,-4.305855,-2.424438,0.237344,2.032397,8.653972,3.335456,6.783851,7.669211,9.937588,-4.749024,1.043079,-6.194703,-5.988453,-1.522430,1.676972,4.227259,-8.965917,-8.387489,-0.648685,8.425523,-7.234655,-9.398370,4.519995,8.527247,-9.353403,-4.157860,1.945342,6.845973,-8.586142,0.173757,-6.835814,-2.328875,-5.447665,-6.003753,-6.539779,-9.280367,4.827055,-3.175700,6.694068,6.046853,9.324790,5.187322,6.676190,-3.173434,1.330940,1.106457,-4.612648,-0.808876,0.748630,1.238471,-4.315424,-2.747691,-2.597169,-5.823335,-9.487467,2.118157,2.751611,-8.316365,7.711693,9.616259,2.827796,7.007773,-2.314860,-9.584378,-4.239573,6.784607,-9.870801,-9.530733,-7.926817,-2.355760,8.942590,9.222808,-4.688876,3.289595,-4.016853,-5.133099,1.480407,-9.534901,2.148429,7.810770,-2.529491,4.297146,0.076585,-9.540997,-1.996945,-1.331297,-5.355509,7.715570,-6.395024,2.284697,1.943097,-5.393533,5.206993,-1.873885,4.736176,-6.152418,-5.734815,-2.203200,-2.239709,7.893818,6.216143,-0.696323,7.703112,2.270880,-0.462940,4.830587,-2.412263,-3.374183,-3.354966,5.585073,3.555975,2.902755,9.692084,4.311776,-4.832675,-5.976379,-0.937628], dtype = "float32")#candidate|7747|(140,)|const|float32
call_7746 = relay.TupleGetItem(func_6240_call(relay.reshape(const_7747.astype('float32'), [1, 14, 10]), relay.reshape(call_7744.astype('uint32'), [256,]), ), 2)
call_7748 = relay.TupleGetItem(func_6244_call(relay.reshape(const_7747.astype('float32'), [1, 14, 10]), relay.reshape(call_7744.astype('uint32'), [256,]), ), 2)
func_5052_call = mod.get_global_var('func_5052')
func_5054_call = mutated_mod.get_global_var('func_5054')
call_7758 = relay.TupleGetItem(func_5052_call(), 0)
call_7759 = relay.TupleGetItem(func_5054_call(), 0)
output = relay.Tuple([call_7744,call_7746,const_7747,call_7758,])
output2 = relay.Tuple([call_7745,call_7748,const_7747,call_7759,])
func_7769 = relay.Function([], output)
mod['func_7769'] = func_7769
mod = relay.transform.InferType()(mod)
mutated_mod['func_7769'] = func_7769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7769_call = mutated_mod.get_global_var('func_7769')
call_7770 = func_7769_call()
output = call_7770
func_7771 = relay.Function([], output)
mutated_mod['func_7771'] = func_7771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6419_call = mod.get_global_var('func_6419')
func_6421_call = mutated_mod.get_global_var('func_6421')
call_7859 = func_6419_call()
call_7860 = func_6419_call()
output = call_7859
output2 = call_7860
func_7870 = relay.Function([], output)
mod['func_7870'] = func_7870
mod = relay.transform.InferType()(mod)
mutated_mod['func_7870'] = func_7870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7870_call = mutated_mod.get_global_var('func_7870')
call_7871 = func_7870_call()
output = call_7871
func_7872 = relay.Function([], output)
mutated_mod['func_7872'] = func_7872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_7914 = relay.TupleGetItem(func_3136_call(), 0)
call_7915 = relay.TupleGetItem(func_3138_call(), 0)
func_6547_call = mod.get_global_var('func_6547')
func_6548_call = mutated_mod.get_global_var('func_6548')
call_7929 = relay.TupleGetItem(func_6547_call(), 1)
call_7930 = relay.TupleGetItem(func_6548_call(), 1)
output = relay.Tuple([call_7914,call_7929,])
output2 = relay.Tuple([call_7915,call_7930,])
func_7954 = relay.Function([], output)
mod['func_7954'] = func_7954
mod = relay.transform.InferType()(mod)
output = func_7954()
func_7955 = relay.Function([], output)
mutated_mod['func_7955'] = func_7955
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7956 = relay.var("var_7956", dtype = "float64", shape = (1, 6, 2))#candidate|7956|(1, 6, 2)|var|float64
uop_7957 = relay.exp(var_7956.astype('float64')) # shape=(1, 6, 2)
output = uop_7957
output2 = uop_7957
func_7962 = relay.Function([var_7956,], output)
mod['func_7962'] = func_7962
mod = relay.transform.InferType()(mod)
var_7963 = relay.var("var_7963", dtype = "float64", shape = (1, 6, 2))#candidate|7963|(1, 6, 2)|var|float64
output = func_7962(var_7963)
func_7964 = relay.Function([var_7963], output)
mutated_mod['func_7964'] = func_7964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6885_call = mod.get_global_var('func_6885')
func_6886_call = mutated_mod.get_global_var('func_6886')
call_7982 = relay.TupleGetItem(func_6885_call(), 0)
call_7983 = relay.TupleGetItem(func_6886_call(), 0)
output = call_7982
output2 = call_7983
func_7988 = relay.Function([], output)
mod['func_7988'] = func_7988
mod = relay.transform.InferType()(mod)
mutated_mod['func_7988'] = func_7988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7988_call = mutated_mod.get_global_var('func_7988')
call_7989 = func_7988_call()
output = call_7989
func_7990 = relay.Function([], output)
mutated_mod['func_7990'] = func_7990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_8031 = relay.TupleGetItem(func_2536_call(), 0)
call_8032 = relay.TupleGetItem(func_2537_call(), 0)
output = call_8031
output2 = call_8032
func_8035 = relay.Function([], output)
mod['func_8035'] = func_8035
mod = relay.transform.InferType()(mod)
mutated_mod['func_8035'] = func_8035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8035_call = mutated_mod.get_global_var('func_8035')
call_8036 = func_8035_call()
output = call_8036
func_8037 = relay.Function([], output)
mutated_mod['func_8037'] = func_8037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_8082 = relay.TupleGetItem(func_2536_call(), 3)
call_8083 = relay.TupleGetItem(func_2537_call(), 3)
output = call_8082
output2 = call_8083
func_8104 = relay.Function([], output)
mod['func_8104'] = func_8104
mod = relay.transform.InferType()(mod)
mutated_mod['func_8104'] = func_8104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8104_call = mutated_mod.get_global_var('func_8104')
call_8105 = func_8104_call()
output = call_8105
func_8106 = relay.Function([], output)
mutated_mod['func_8106'] = func_8106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3762_call = mod.get_global_var('func_3762')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_8121 = relay.TupleGetItem(func_3762_call(), 1)
call_8122 = relay.TupleGetItem(func_3764_call(), 1)
func_7479_call = mod.get_global_var('func_7479')
func_7481_call = mutated_mod.get_global_var('func_7481')
call_8125 = relay.TupleGetItem(func_7479_call(), 0)
call_8126 = relay.TupleGetItem(func_7481_call(), 0)
output = relay.Tuple([call_8121,call_8125,])
output2 = relay.Tuple([call_8122,call_8126,])
func_8129 = relay.Function([], output)
mod['func_8129'] = func_8129
mod = relay.transform.InferType()(mod)
output = func_8129()
func_8130 = relay.Function([], output)
mutated_mod['func_8130'] = func_8130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2972_call = mod.get_global_var('func_2972')
func_2973_call = mutated_mod.get_global_var('func_2973')
call_8165 = func_2972_call()
call_8166 = func_2972_call()
uop_8167 = relay.cos(call_8165.astype('float32')) # shape=(16, 4, 4)
uop_8169 = relay.cos(call_8166.astype('float32')) # shape=(16, 4, 4)
func_4824_call = mod.get_global_var('func_4824')
func_4826_call = mutated_mod.get_global_var('func_4826')
const_8184 = relay.const([-8.097119,-6.073700,8.662753,-7.449263,0.303138,-0.885301,9.152057,-3.492297,-5.778981,6.183040,-4.348087,-0.016621,7.113557,-4.887440,8.295587,-2.185366,2.948915,3.432330,1.364082,7.048375,9.209413,3.483570,9.726351,2.743974,-4.220827,3.961080,1.505837,2.402536,9.387056,2.653266,1.354410,-1.773169,-6.136064,6.158424,5.977941,0.469242,-8.476341,3.854732,-8.767209,6.090217,-9.345391,7.623202], dtype = "float64")#candidate|8184|(42,)|const|float64
call_8183 = relay.TupleGetItem(func_4824_call(relay.reshape(const_8184.astype('float64'), [42,])), 2)
call_8185 = relay.TupleGetItem(func_4826_call(relay.reshape(const_8184.astype('float64'), [42,])), 2)
output = relay.Tuple([uop_8167,call_8183,const_8184,])
output2 = relay.Tuple([uop_8169,call_8185,const_8184,])
func_8202 = relay.Function([], output)
mod['func_8202'] = func_8202
mod = relay.transform.InferType()(mod)
mutated_mod['func_8202'] = func_8202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8202_call = mutated_mod.get_global_var('func_8202')
call_8203 = func_8202_call()
output = call_8203
func_8204 = relay.Function([], output)
mutated_mod['func_8204'] = func_8204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8129_call = mod.get_global_var('func_8129')
func_8130_call = mutated_mod.get_global_var('func_8130')
call_8211 = relay.TupleGetItem(func_8129_call(), 0)
call_8212 = relay.TupleGetItem(func_8130_call(), 0)
uop_8219 = relay.log(call_8211.astype('float64')) # shape=(135,)
uop_8221 = relay.log(call_8212.astype('float64')) # shape=(135,)
output = uop_8219
output2 = uop_8221
func_8232 = relay.Function([], output)
mod['func_8232'] = func_8232
mod = relay.transform.InferType()(mod)
mutated_mod['func_8232'] = func_8232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8232_call = mutated_mod.get_global_var('func_8232')
call_8233 = func_8232_call()
output = call_8233
func_8234 = relay.Function([], output)
mutated_mod['func_8234'] = func_8234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1137_call = mod.get_global_var('func_1137')
func_1138_call = mutated_mod.get_global_var('func_1138')
call_8375 = relay.TupleGetItem(func_1137_call(), 1)
call_8376 = relay.TupleGetItem(func_1138_call(), 1)
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_8377 = relay.TupleGetItem(func_848_call(), 0)
call_8378 = relay.TupleGetItem(func_849_call(), 0)
func_4383_call = mod.get_global_var('func_4383')
func_4386_call = mutated_mod.get_global_var('func_4386')
var_8381 = relay.var("var_8381", dtype = "float32", shape = (3, 108))#candidate|8381|(3, 108)|var|float32
const_8382 = relay.const([2.078180,-7.610525,-0.674365,5.350325,-4.945741,3.572003,3.882524,7.384729,-1.888429,-6.538231,5.681632,-8.950077,-3.487561,-0.741174,9.404614,7.991974,5.609152,1.111009,-4.474588,-8.504026,6.491869,5.990980,-8.867189,-7.932521,-1.135835,3.490549,-5.148662,4.789445,-7.121980,-4.619474,-0.693566,9.423995,4.965836,5.187584,2.655029,-6.974500,4.841428,-2.206731,9.877372,-5.552836,2.248047,1.864000], dtype = "float64")#candidate|8382|(42,)|const|float64
call_8380 = relay.TupleGetItem(func_4383_call(relay.reshape(var_8381.astype('float32'), [1, 324]), relay.reshape(const_8382.astype('float64'), [42,]), ), 4)
call_8383 = relay.TupleGetItem(func_4386_call(relay.reshape(var_8381.astype('float32'), [1, 324]), relay.reshape(const_8382.astype('float64'), [42,]), ), 4)
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
var_8386 = relay.var("var_8386", dtype = "float32", shape = (135,))#candidate|8386|(135,)|var|float32
call_8385 = relay.TupleGetItem(func_435_call(relay.reshape(var_8386.astype('float32'), [3, 45])), 4)
call_8387 = relay.TupleGetItem(func_438_call(relay.reshape(var_8386.astype('float32'), [3, 45])), 4)
func_8232_call = mod.get_global_var('func_8232')
func_8234_call = mutated_mod.get_global_var('func_8234')
call_8392 = func_8232_call()
call_8393 = func_8232_call()
uop_8396 = relay.exp(call_8385.astype('float32')) # shape=(3, 45)
uop_8398 = relay.exp(call_8387.astype('float32')) # shape=(3, 45)
uop_8400 = relay.sqrt(uop_8396.astype('float64')) # shape=(3, 45)
uop_8402 = relay.sqrt(uop_8398.astype('float64')) # shape=(3, 45)
bop_8404 = relay.right_shift(uop_8400.astype('uint8'), relay.reshape(call_8385.astype('uint8'), relay.shape_of(uop_8400))) # shape=(3, 45)
bop_8407 = relay.right_shift(uop_8402.astype('uint8'), relay.reshape(call_8387.astype('uint8'), relay.shape_of(uop_8402))) # shape=(3, 45)
output = relay.Tuple([call_8375,call_8377,call_8380,var_8381,const_8382,var_8386,call_8392,bop_8404,])
output2 = relay.Tuple([call_8376,call_8378,call_8383,var_8381,const_8382,var_8386,call_8393,bop_8407,])
func_8408 = relay.Function([var_8381,var_8386,], output)
mod['func_8408'] = func_8408
mod = relay.transform.InferType()(mod)
var_8409 = relay.var("var_8409", dtype = "float32", shape = (3, 108))#candidate|8409|(3, 108)|var|float32
var_8410 = relay.var("var_8410", dtype = "float32", shape = (135,))#candidate|8410|(135,)|var|float32
output = func_8408(var_8409,var_8410,)
func_8411 = relay.Function([var_8409,var_8410,], output)
mutated_mod['func_8411'] = func_8411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_8439 = func_1439_call()
call_8440 = func_1439_call()
output = relay.Tuple([call_8439,])
output2 = relay.Tuple([call_8440,])
func_8441 = relay.Function([], output)
mod['func_8441'] = func_8441
mod = relay.transform.InferType()(mod)
mutated_mod['func_8441'] = func_8441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8441_call = mutated_mod.get_global_var('func_8441')
call_8442 = func_8441_call()
output = call_8442
func_8443 = relay.Function([], output)
mutated_mod['func_8443'] = func_8443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2545_call = mutated_mod.get_global_var('func_2545')
call_8603 = relay.TupleGetItem(func_2543_call(), 0)
call_8604 = relay.TupleGetItem(func_2545_call(), 0)
func_8104_call = mod.get_global_var('func_8104')
func_8106_call = mutated_mod.get_global_var('func_8106')
call_8606 = func_8104_call()
call_8607 = func_8104_call()
func_6701_call = mod.get_global_var('func_6701')
func_6703_call = mutated_mod.get_global_var('func_6703')
call_8627 = func_6701_call()
call_8628 = func_6701_call()
func_848_call = mod.get_global_var('func_848')
func_849_call = mutated_mod.get_global_var('func_849')
call_8651 = relay.TupleGetItem(func_848_call(), 0)
call_8652 = relay.TupleGetItem(func_849_call(), 0)
output = relay.Tuple([call_8603,call_8606,call_8627,call_8651,])
output2 = relay.Tuple([call_8604,call_8607,call_8628,call_8652,])
func_8668 = relay.Function([], output)
mod['func_8668'] = func_8668
mod = relay.transform.InferType()(mod)
mutated_mod['func_8668'] = func_8668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8668_call = mutated_mod.get_global_var('func_8668')
call_8669 = func_8668_call()
output = call_8669
func_8670 = relay.Function([], output)
mutated_mod['func_8670'] = func_8670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7479_call = mod.get_global_var('func_7479')
func_7481_call = mutated_mod.get_global_var('func_7481')
call_8702 = relay.TupleGetItem(func_7479_call(), 0)
call_8703 = relay.TupleGetItem(func_7481_call(), 0)
func_1392_call = mod.get_global_var('func_1392')
func_1393_call = mutated_mod.get_global_var('func_1393')
call_8705 = relay.TupleGetItem(func_1392_call(), 1)
call_8706 = relay.TupleGetItem(func_1393_call(), 1)
uop_8719 = relay.log(call_8702.astype('float32')) # shape=(1, 324)
uop_8721 = relay.log(call_8703.astype('float32')) # shape=(1, 324)
func_2285_call = mod.get_global_var('func_2285')
func_2286_call = mutated_mod.get_global_var('func_2286')
call_8724 = relay.TupleGetItem(func_2285_call(), 0)
call_8725 = relay.TupleGetItem(func_2286_call(), 0)
func_99_call = mod.get_global_var('func_99')
func_101_call = mutated_mod.get_global_var('func_101')
var_8736 = relay.var("var_8736", dtype = "float32", shape = (135,))#candidate|8736|(135,)|var|float32
call_8735 = func_99_call(relay.reshape(var_8736.astype('float32'), [9, 1, 15]))
call_8737 = func_99_call(relay.reshape(var_8736.astype('float32'), [9, 1, 15]))
output = relay.Tuple([call_8705,uop_8719,call_8724,call_8735,var_8736,])
output2 = relay.Tuple([call_8706,uop_8721,call_8725,call_8737,var_8736,])
func_8743 = relay.Function([var_8736,], output)
mod['func_8743'] = func_8743
mod = relay.transform.InferType()(mod)
mutated_mod['func_8743'] = func_8743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8744 = relay.var("var_8744", dtype = "float32", shape = (135,))#candidate|8744|(135,)|var|float32
func_8743_call = mutated_mod.get_global_var('func_8743')
call_8745 = func_8743_call(var_8744)
output = call_8745
func_8746 = relay.Function([var_8744], output)
mutated_mod['func_8746'] = func_8746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2896_call = mod.get_global_var('func_2896')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_8868 = relay.TupleGetItem(func_2896_call(), 1)
call_8869 = relay.TupleGetItem(func_2897_call(), 1)
output = relay.Tuple([call_8868,])
output2 = relay.Tuple([call_8869,])
func_8879 = relay.Function([], output)
mod['func_8879'] = func_8879
mod = relay.transform.InferType()(mod)
mutated_mod['func_8879'] = func_8879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8879_call = mutated_mod.get_global_var('func_8879')
call_8880 = func_8879_call()
output = call_8880
func_8881 = relay.Function([], output)
mutated_mod['func_8881'] = func_8881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_269_call = mod.get_global_var('func_269')
func_271_call = mutated_mod.get_global_var('func_271')
call_8893 = relay.TupleGetItem(func_269_call(), 2)
call_8894 = relay.TupleGetItem(func_271_call(), 2)
output = call_8893
output2 = call_8894
func_8897 = relay.Function([], output)
mod['func_8897'] = func_8897
mod = relay.transform.InferType()(mod)
output = func_8897()
func_8898 = relay.Function([], output)
mutated_mod['func_8898'] = func_8898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1970_call = mod.get_global_var('func_1970')
func_1971_call = mutated_mod.get_global_var('func_1971')
call_8939 = func_1970_call()
call_8940 = func_1970_call()
var_8942 = relay.var("var_8942", dtype = "float32", shape = (5, 4, 2))#candidate|8942|(5, 4, 2)|var|float32
bop_8943 = relay.equal(call_8939.astype('bool'), relay.reshape(var_8942.astype('bool'), relay.shape_of(call_8939))) # shape=(5, 4, 2)
bop_8946 = relay.equal(call_8940.astype('bool'), relay.reshape(var_8942.astype('bool'), relay.shape_of(call_8940))) # shape=(5, 4, 2)
output = relay.Tuple([bop_8943,])
output2 = relay.Tuple([bop_8946,])
func_8950 = relay.Function([var_8942,], output)
mod['func_8950'] = func_8950
mod = relay.transform.InferType()(mod)
mutated_mod['func_8950'] = func_8950
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8951 = relay.var("var_8951", dtype = "float32", shape = (5, 4, 2))#candidate|8951|(5, 4, 2)|var|float32
func_8950_call = mutated_mod.get_global_var('func_8950')
call_8952 = func_8950_call(var_8951)
output = call_8952
func_8953 = relay.Function([var_8951], output)
mutated_mod['func_8953'] = func_8953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4213_call = mod.get_global_var('func_4213')
func_4215_call = mutated_mod.get_global_var('func_4215')
call_8979 = func_4213_call()
call_8980 = func_4213_call()
func_8743_call = mod.get_global_var('func_8743')
func_8746_call = mutated_mod.get_global_var('func_8746')
const_9033 = relay.const([5.164264,5.978182,-1.562707,-6.384447,0.477820,0.314013,0.077721,9.696651,8.005168,-2.055429,1.298343,9.162057,9.431536,7.994229,-7.300189,3.410671,-6.088125,-8.630896,0.213148,-2.353291,8.730171,-6.265537,-5.790648,-6.903794,5.497416,-5.923990,8.418007,3.230607,3.288847,0.574954,0.058120,3.726473,-6.462885,-0.586946,-5.201419,-5.069974,-3.193345,-1.520601,5.728237,-8.884797,-5.815324,7.930391,-3.714221,-4.073152,6.265928,-7.826435,-1.869194,8.737468,8.556305,-7.471054,-0.057708,8.792949,-9.978296,3.197924,-5.764566,-8.347876,-2.605265,-9.218948,2.430962,-2.518316,0.370670,1.004048,4.989481,-6.880478,9.820518,-4.628939,7.609692,-8.734342,-9.386492,1.327423,-5.276227,3.068972,0.708695,8.608303,-3.925751,-3.662769,-4.401782,9.819054,-6.072006,-1.607541,4.249164,6.512065,3.221374,-4.241223,2.855970,-0.583140,8.400690,8.271788,-7.910843,1.182850,-5.239331,-7.834275,-5.821308,-2.395655,2.972375,-4.577118,-5.892589,2.622090,2.827894,3.515517,-4.646711,-0.254240,9.583769,-8.582462,2.250755,-3.371981,1.690258,-4.577141,-0.061516,-8.292486,-4.234171,-4.475746,-1.971725,-1.387040,3.697201,9.972372,8.186254,-6.880423,9.205313,-0.487498,-8.656335,-2.533861,8.859465,1.469409,-2.377386,8.915004,-6.484012,8.219380,-3.364749,3.417380,4.112379,3.723740,-3.599011,8.317789,-2.709689], dtype = "float32")#candidate|9033|(135,)|const|float32
call_9032 = relay.TupleGetItem(func_8743_call(relay.reshape(const_9033.astype('float32'), [135,])), 1)
call_9034 = relay.TupleGetItem(func_8746_call(relay.reshape(const_9033.astype('float32'), [135,])), 1)
func_5294_call = mod.get_global_var('func_5294')
func_5296_call = mutated_mod.get_global_var('func_5296')
var_9045 = relay.var("var_9045", dtype = "uint32", shape = (448,))#candidate|9045|(448,)|var|uint32
call_9044 = relay.TupleGetItem(func_5294_call(relay.reshape(var_9045.astype('uint32'), [2, 16, 14])), 0)
call_9046 = relay.TupleGetItem(func_5296_call(relay.reshape(var_9045.astype('uint32'), [2, 16, 14])), 0)
uop_9054 = relay.cos(call_9044.astype('float64')) # shape=(2, 16, 14)
uop_9056 = relay.cos(call_9046.astype('float64')) # shape=(2, 16, 14)
func_6120_call = mod.get_global_var('func_6120')
func_6124_call = mutated_mod.get_global_var('func_6124')
const_9070 = relay.const([-5.033854,-1.556645,2.961033,-3.763230,-8.739669,2.774081,4.013331,-1.888110,-5.322603,4.586669,-2.061306,9.273005,-5.427721,-2.652187,-6.297295,5.762768,-8.101744,1.618129,-8.094377,-9.603769,-9.787151,2.439533,-8.984893,-5.507696,-2.848198,-4.534928,0.509488,-7.927961,7.722237,-5.562134,-1.450689,-9.357302,0.963020,-7.340929,7.026101,-2.936306,-0.567704,9.676216,6.607929,5.868769,-4.700480,-9.606058,7.495644,8.176081,-2.240368,6.670269,0.499574,5.157430,0.591773,0.932475,-4.319076,-4.655806,2.413373,-8.046940,3.819149,-4.469933,3.012106,-0.369614,1.151675,3.925003], dtype = "float32")#candidate|9070|(60,)|const|float32
call_9069 = relay.TupleGetItem(func_6120_call(relay.reshape(const_9070.astype('float32'), [3, 10, 2]), relay.reshape(const_9033.astype('float32'), [1, 135]), ), 0)
call_9071 = relay.TupleGetItem(func_6124_call(relay.reshape(const_9070.astype('float32'), [3, 10, 2]), relay.reshape(const_9033.astype('float32'), [1, 135]), ), 0)
func_1392_call = mod.get_global_var('func_1392')
func_1393_call = mutated_mod.get_global_var('func_1393')
call_9085 = relay.TupleGetItem(func_1392_call(), 0)
call_9086 = relay.TupleGetItem(func_1393_call(), 0)
func_6665_call = mod.get_global_var('func_6665')
func_6668_call = mutated_mod.get_global_var('func_6668')
var_9090 = relay.var("var_9090", dtype = "int64", shape = ())#candidate|9090|()|var|int64
var_9091 = relay.var("var_9091", dtype = "int64", shape = (495,))#candidate|9091|(495,)|var|int64
call_9089 = relay.TupleGetItem(func_6665_call(relay.reshape(var_9090.astype('int64'), []), relay.reshape(var_9091.astype('int64'), [495,]), ), 2)
call_9092 = relay.TupleGetItem(func_6668_call(relay.reshape(var_9090.astype('int64'), []), relay.reshape(var_9091.astype('int64'), [495,]), ), 2)
func_1854_call = mod.get_global_var('func_1854')
func_1856_call = mutated_mod.get_global_var('func_1856')
call_9098 = func_1854_call()
call_9099 = func_1854_call()
uop_9102 = relay.atanh(uop_9054.astype('float64')) # shape=(2, 16, 14)
uop_9104 = relay.atanh(uop_9056.astype('float64')) # shape=(2, 16, 14)
output = relay.Tuple([call_8979,call_9032,const_9033,var_9045,call_9069,const_9070,call_9085,call_9089,var_9090,var_9091,call_9098,uop_9102,])
output2 = relay.Tuple([call_8980,call_9034,const_9033,var_9045,call_9071,const_9070,call_9086,call_9092,var_9090,var_9091,call_9099,uop_9104,])
func_9112 = relay.Function([var_9045,var_9090,var_9091,], output)
mod['func_9112'] = func_9112
mod = relay.transform.InferType()(mod)
mutated_mod['func_9112'] = func_9112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9112_call = mutated_mod.get_global_var('func_9112')
var_9114 = relay.var("var_9114", dtype = "uint32", shape = (448,))#candidate|9114|(448,)|var|uint32
var_9115 = relay.var("var_9115", dtype = "int64", shape = ())#candidate|9115|()|var|int64
var_9116 = relay.var("var_9116", dtype = "int64", shape = (495,))#candidate|9116|(495,)|var|int64
call_9113 = func_9112_call(var_9114,var_9115,var_9116,)
output = call_9113
func_9117 = relay.Function([var_9114,var_9115,var_9116,], output)
mutated_mod['func_9117'] = func_9117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2972_call = mod.get_global_var('func_2972')
func_2973_call = mutated_mod.get_global_var('func_2973')
call_9133 = func_2972_call()
call_9134 = func_2972_call()
output = call_9133
output2 = call_9134
func_9137 = relay.Function([], output)
mod['func_9137'] = func_9137
mod = relay.transform.InferType()(mod)
mutated_mod['func_9137'] = func_9137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9137_call = mutated_mod.get_global_var('func_9137')
call_9138 = func_9137_call()
output = call_9138
func_9139 = relay.Function([], output)
mutated_mod['func_9139'] = func_9139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7870_call = mod.get_global_var('func_7870')
func_7872_call = mutated_mod.get_global_var('func_7872')
call_9142 = func_7870_call()
call_9143 = func_7870_call()
func_7737_call = mod.get_global_var('func_7737')
func_7739_call = mutated_mod.get_global_var('func_7739')
var_9158 = relay.var("var_9158", dtype = "float32", shape = (45, 3))#candidate|9158|(45, 3)|var|float32
call_9157 = relay.TupleGetItem(func_7737_call(relay.reshape(var_9158.astype('float32'), [135,])), 0)
call_9159 = relay.TupleGetItem(func_7739_call(relay.reshape(var_9158.astype('float32'), [135,])), 0)
const_9196 = relay.const([[7.015279,-9.998964,-5.636842],[-7.077010,3.991978,3.700151],[9.796664,-4.561305,8.828564],[-3.497311,4.350382,7.921699],[5.422531,-8.020799,8.022455],[7.925927,-5.495094,6.540919],[6.270913,7.036880,-2.767611],[-8.903397,2.517755,-4.983815],[-2.314561,0.996039,-3.641817],[-5.515053,-7.391314,-9.677199],[-5.082777,-9.736695,-8.230057],[-4.133437,5.621693,-9.801823],[-9.846450,4.173152,2.013704],[-4.555238,1.831197,6.849063],[-3.811671,5.592238,-9.052156],[4.489481,-6.594217,-0.924633],[7.342161,-8.575880,-4.750298],[-5.196833,8.916633,-5.674989],[1.879152,-5.382800,-1.052793],[-3.988858,-3.943109,1.763976],[-8.225493,2.378149,-8.850018],[0.095983,-8.912880,3.124692],[-3.046437,-7.140382,8.708089],[-4.160803,0.385043,9.298792],[4.065224,4.558356,-5.046115],[-7.867300,4.860327,7.826491],[7.983490,3.264918,-3.976439],[-1.662475,-5.942868,5.111566],[9.459921,-4.954117,-6.289142],[2.908901,1.689723,3.929168],[1.963803,-9.767035,-1.059017],[6.789395,-2.255999,3.203460],[0.216402,3.326004,-7.009726],[7.023400,8.528554,7.018794],[-6.290413,7.900518,6.426906],[2.826215,-4.833765,8.310913],[6.103183,9.826640,7.606774],[-2.971100,-7.476953,-1.322763],[-5.755000,8.417268,7.508985],[-1.948913,9.961141,9.453986],[-7.825563,4.542661,1.799635],[3.764650,6.418575,-2.744849],[-3.320387,7.214712,5.951126],[9.310070,-8.645702,3.076910],[1.395378,1.219068,1.918012]], dtype = "float32")#candidate|9196|(45, 3)|const|float32
bop_9197 = relay.mod(var_9158.astype('float64'), relay.reshape(const_9196.astype('float64'), relay.shape_of(var_9158))) # shape=(45, 3)
output = relay.Tuple([call_9142,call_9157,bop_9197,])
output2 = relay.Tuple([call_9143,call_9159,bop_9197,])
F = relay.Function([var_9158,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9158,], output2)
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
