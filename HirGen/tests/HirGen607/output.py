import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_317 = relay.var("var_317", dtype = "uint32", shape = (8, 1, 3))#candidate|317|(8, 1, 3)|var|uint32
var_318 = relay.var("var_318", dtype = "uint32", shape = (8, 16, 3))#candidate|318|(8, 16, 3)|var|uint32
bop_319 = relay.minimum(var_317.astype('uint32'), var_318.astype('uint32')) # shape=(8, 16, 3)
output = bop_319
output2 = bop_319
func_327 = relay.Function([var_317,var_318,], output)
mod['func_327'] = func_327
mod = relay.transform.InferType()(mod)
mutated_mod['func_327'] = func_327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_327_call = mutated_mod.get_global_var('func_327')
var_329 = relay.var("var_329", dtype = "uint32", shape = (8, 1, 3))#candidate|329|(8, 1, 3)|var|uint32
var_330 = relay.var("var_330", dtype = "uint32", shape = (8, 16, 3))#candidate|330|(8, 16, 3)|var|uint32
call_328 = func_327_call(var_329,var_330,)
output = call_328
func_331 = relay.Function([var_329,var_330,], output)
mutated_mod['func_331'] = func_331
mutated_mod = relay.transform.InferType()(mutated_mod)
var_778 = relay.var("var_778", dtype = "float32", shape = (1, 4, 16))#candidate|778|(1, 4, 16)|var|float32
var_779 = relay.var("var_779", dtype = "float32", shape = (5, 4, 16))#candidate|779|(5, 4, 16)|var|float32
bop_780 = relay.less_equal(var_778.astype('bool'), var_779.astype('bool')) # shape=(5, 4, 16)
output = relay.Tuple([bop_780,])
output2 = relay.Tuple([bop_780,])
func_791 = relay.Function([var_778,var_779,], output)
mod['func_791'] = func_791
mod = relay.transform.InferType()(mod)
var_792 = relay.var("var_792", dtype = "float32", shape = (1, 4, 16))#candidate|792|(1, 4, 16)|var|float32
var_793 = relay.var("var_793", dtype = "float32", shape = (5, 4, 16))#candidate|793|(5, 4, 16)|var|float32
output = func_791(var_792,var_793,)
func_794 = relay.Function([var_792,var_793,], output)
mutated_mod['func_794'] = func_794
mutated_mod = relay.transform.InferType()(mutated_mod)
const_880 = relay.const(True, dtype = "bool")#candidate|880|()|const|bool
var_881 = relay.var("var_881", dtype = "bool", shape = (10, 2, 13))#candidate|881|(10, 2, 13)|var|bool
bop_882 = relay.logical_and(const_880.astype('bool'), var_881.astype('bool')) # shape=(10, 2, 13)
output = relay.Tuple([bop_882,])
output2 = relay.Tuple([bop_882,])
func_894 = relay.Function([var_881,], output)
mod['func_894'] = func_894
mod = relay.transform.InferType()(mod)
var_895 = relay.var("var_895", dtype = "bool", shape = (10, 2, 13))#candidate|895|(10, 2, 13)|var|bool
output = func_894(var_895)
func_896 = relay.Function([var_895], output)
mutated_mod['func_896'] = func_896
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1028 = relay.var("var_1028", dtype = "float32", shape = (9, 16, 4))#candidate|1028|(9, 16, 4)|var|float32
uop_1029 = relay.asin(var_1028.astype('float32')) # shape=(9, 16, 4)
func_327_call = mod.get_global_var('func_327')
func_331_call = mutated_mod.get_global_var('func_331')
var_1037 = relay.var("var_1037", dtype = "uint32", shape = (24,))#candidate|1037|(24,)|var|uint32
var_1038 = relay.var("var_1038", dtype = "uint32", shape = (384,))#candidate|1038|(384,)|var|uint32
call_1036 = func_327_call(relay.reshape(var_1037.astype('uint32'), [8, 1, 3]), relay.reshape(var_1038.astype('uint32'), [8, 16, 3]), )
call_1039 = func_327_call(relay.reshape(var_1037.astype('uint32'), [8, 1, 3]), relay.reshape(var_1038.astype('uint32'), [8, 16, 3]), )
func_327_call = mod.get_global_var('func_327')
func_331_call = mutated_mod.get_global_var('func_331')
call_1043 = func_327_call(relay.reshape(var_1037.astype('uint32'), [8, 1, 3]), relay.reshape(var_1038.astype('uint32'), [8, 16, 3]), )
call_1044 = func_327_call(relay.reshape(var_1037.astype('uint32'), [8, 1, 3]), relay.reshape(var_1038.astype('uint32'), [8, 16, 3]), )
func_791_call = mod.get_global_var('func_791')
func_794_call = mutated_mod.get_global_var('func_794')
var_1046 = relay.var("var_1046", dtype = "float32", shape = (64,))#candidate|1046|(64,)|var|float32
var_1047 = relay.var("var_1047", dtype = "float32", shape = (320,))#candidate|1047|(320,)|var|float32
call_1045 = relay.TupleGetItem(func_791_call(relay.reshape(var_1046.astype('float32'), [1, 4, 16]), relay.reshape(var_1047.astype('float32'), [5, 4, 16]), ), 0)
call_1048 = relay.TupleGetItem(func_794_call(relay.reshape(var_1046.astype('float32'), [1, 4, 16]), relay.reshape(var_1047.astype('float32'), [5, 4, 16]), ), 0)
func_327_call = mod.get_global_var('func_327')
func_331_call = mutated_mod.get_global_var('func_331')
call_1058 = func_327_call(relay.reshape(var_1037.astype('uint32'), [8, 1, 3]), relay.reshape(call_1036.astype('uint32'), [8, 16, 3]), )
call_1059 = func_327_call(relay.reshape(var_1037.astype('uint32'), [8, 1, 3]), relay.reshape(call_1036.astype('uint32'), [8, 16, 3]), )
var_1063 = relay.var("var_1063", dtype = "uint32", shape = (8, 16, 3))#candidate|1063|(8, 16, 3)|var|uint32
bop_1064 = relay.less(call_1036.astype('bool'), relay.reshape(var_1063.astype('bool'), relay.shape_of(call_1036))) # shape=(8, 16, 3)
bop_1067 = relay.less(call_1039.astype('bool'), relay.reshape(var_1063.astype('bool'), relay.shape_of(call_1039))) # shape=(8, 16, 3)
output = relay.Tuple([uop_1029,var_1037,var_1038,call_1043,call_1045,var_1046,var_1047,call_1058,bop_1064,])
output2 = relay.Tuple([uop_1029,var_1037,var_1038,call_1044,call_1048,var_1046,var_1047,call_1059,bop_1067,])
func_1076 = relay.Function([var_1028,var_1037,var_1038,var_1046,var_1047,var_1063,], output)
mod['func_1076'] = func_1076
mod = relay.transform.InferType()(mod)
var_1077 = relay.var("var_1077", dtype = "float32", shape = (9, 16, 4))#candidate|1077|(9, 16, 4)|var|float32
var_1078 = relay.var("var_1078", dtype = "uint32", shape = (24,))#candidate|1078|(24,)|var|uint32
var_1079 = relay.var("var_1079", dtype = "uint32", shape = (384,))#candidate|1079|(384,)|var|uint32
var_1080 = relay.var("var_1080", dtype = "float32", shape = (64,))#candidate|1080|(64,)|var|float32
var_1081 = relay.var("var_1081", dtype = "float32", shape = (320,))#candidate|1081|(320,)|var|float32
var_1082 = relay.var("var_1082", dtype = "uint32", shape = (8, 16, 3))#candidate|1082|(8, 16, 3)|var|uint32
output = func_1076(var_1077,var_1078,var_1079,var_1080,var_1081,var_1082,)
func_1083 = relay.Function([var_1077,var_1078,var_1079,var_1080,var_1081,var_1082,], output)
mutated_mod['func_1083'] = func_1083
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1495 = relay.const([[[-9.871779,-3.241221,-7.986400,2.048062,7.115406,5.837991],[0.150356,1.595897,4.854793,4.637851,8.374828,-4.953231],[3.859332,-0.050090,-0.313127,8.083175,-4.779763,-8.516948],[0.585381,3.596633,-1.137169,1.600179,-8.259247,5.136634],[-6.178982,5.191751,-9.976474,-1.104593,-5.156730,-6.931174],[-6.662656,-9.893869,0.366179,1.776854,-2.594788,4.845672],[5.009830,-8.829104,-2.634533,0.667173,2.262842,-0.180278],[4.922532,6.262650,5.229735,-7.179978,-6.479433,-0.705210],[0.198889,-8.667787,-3.759813,-0.924687,-6.155636,6.057271],[1.747825,2.798245,5.122520,-0.219253,-4.186930,0.764276],[9.007384,3.144351,-7.552044,4.957893,-9.967079,7.255236],[-9.104125,-3.365797,3.214689,2.077867,6.375931,7.631018],[-4.581211,1.187012,7.373331,-7.211440,-4.108843,-8.007351],[8.150208,7.708268,0.334140,-0.110993,-4.080063,1.770415],[-1.823644,-1.216674,0.578744,-1.352865,-1.218519,1.670738],[-3.243010,-5.021672,5.572164,2.861944,9.595692,-0.218753]],[[-4.319282,-6.951774,-4.727653,-2.961580,-1.878263,-5.311557],[-6.208079,9.598094,-1.824448,-7.718313,-6.865356,4.101244],[-3.254728,-5.109029,4.600540,-8.732905,8.527645,0.678837],[-2.018872,-8.036659,-6.217136,5.926441,6.035378,9.481003],[2.104709,2.732871,3.596388,0.929827,8.588617,3.058013],[0.117087,-5.498264,-7.440938,-3.431039,5.333579,7.415888],[9.796882,-3.222874,5.260339,-5.757062,-7.113140,-6.516594],[-8.758159,2.856738,2.486930,4.480914,-0.037454,1.441009],[8.131485,-5.505943,-0.747024,-6.195772,-3.912902,-8.512045],[5.001369,-2.501190,-9.266768,8.941615,-9.815483,6.622106],[9.961663,-8.526853,-9.274437,-8.721440,6.664465,7.104586],[-3.717245,9.696141,-8.187968,-9.083027,-6.747259,6.460576],[0.484154,-2.487142,5.391357,5.170952,-6.196139,7.240730],[8.335410,-7.096762,-7.565990,-2.613004,6.381939,1.093189],[3.811829,9.148337,-0.387461,9.771093,5.784950,4.364137],[4.473832,6.015599,7.965934,-7.615815,-9.742060,2.711935]],[[-3.397277,3.544852,-6.688024,-1.827110,-8.406551,7.093286],[-6.326722,-6.574497,-9.340954,2.437069,-8.748510,1.108490],[2.441021,-7.357483,-7.695975,-8.722592,1.450113,8.321005],[-4.948575,-3.828170,4.657939,8.739353,-1.292180,-9.264322],[0.023785,-3.841073,-4.519891,9.046348,5.230625,-6.418432],[-2.329724,3.638940,-3.680575,3.883579,-7.710263,-3.268036],[0.982911,9.131180,3.594713,8.241564,0.619111,3.671451],[5.321481,6.353435,-1.541565,5.579061,-1.958202,5.003381],[1.182588,8.860418,-0.949525,7.464589,6.239818,9.358364],[-9.648143,-6.407285,-2.387375,-3.941177,-8.110812,-1.333106],[2.912584,5.846210,-2.985889,-4.880897,3.358771,7.114794],[6.348376,-8.742771,-5.769018,-1.536492,-7.746716,-1.198387],[-5.661537,-3.606368,6.793429,7.317613,-2.158138,-9.704404],[6.404951,-5.148000,3.193421,-3.441277,4.838126,7.073751],[-3.039760,-4.100300,-5.863504,0.807629,7.941654,-9.512109],[3.750970,1.007319,-0.399862,-2.308643,6.521861,0.067138]]], dtype = "float32")#candidate|1495|(3, 16, 6)|const|float32
const_1496 = relay.const([[[0.673653,-1.252092,-3.798499,-7.971226,4.367942,4.370740],[5.739730,-3.592252,6.153005,-6.436949,-5.575975,1.310238],[-4.231602,8.300995,7.874992,-3.096976,7.668967,2.509491],[6.428897,8.119568,9.904344,-1.467788,0.973072,-7.062762],[-3.740725,-4.592254,6.033452,9.863716,-5.114648,8.890689],[6.769167,-3.451659,-1.340361,-5.765442,-2.691742,-0.971365],[9.768219,-9.739456,-9.593626,1.530197,1.678822,4.256129],[6.277003,8.255709,2.390780,5.527680,-2.910480,-8.136695],[-2.241441,-2.450926,-4.259436,-1.497524,2.061162,-4.753867],[8.764992,-6.447517,3.767573,2.842893,2.646474,-9.910431],[-3.398712,3.542093,-8.135728,2.820320,7.897819,6.400962],[9.027386,7.245965,-6.776277,-8.700546,8.928328,0.850741],[-5.591211,-4.774388,6.577457,-7.290463,-0.553221,-0.942542],[2.213434,8.735875,5.327102,-4.137469,-1.623963,-3.842611],[-3.401522,-9.845728,9.172234,-1.476026,7.305738,9.598006],[-1.135929,-1.141653,-4.876354,9.210482,-7.947425,-4.971594]],[[7.768127,-5.130356,-3.795136,-3.425087,7.025316,-5.411629],[-6.807876,-9.068420,7.572397,-0.251732,-1.241928,8.752167],[2.302943,-2.920602,2.591670,-3.118885,-1.174332,8.082725],[2.556930,7.190120,-1.532456,7.818219,-7.812164,-7.181892],[-7.392050,8.887979,2.012705,3.287671,6.154719,6.511983],[-4.285623,3.694010,-8.622962,8.695110,4.211479,2.065680],[-8.376384,-4.005716,-3.508327,8.119948,-3.243046,7.881663],[0.243429,-5.140349,9.239659,0.375189,6.692500,-9.854957],[8.678146,5.962889,-1.551205,0.717393,-3.004979,1.896674],[-7.944022,2.124362,-7.453987,6.035215,1.727516,-7.885018],[4.607440,-1.088217,8.536436,-6.329590,-9.081507,1.876239],[-2.898956,3.512099,-8.211666,-8.142882,4.190360,5.937194],[-6.802931,8.679598,5.506971,-0.913037,-7.174537,9.727465],[7.239085,-0.122428,-2.798157,-1.728187,-9.460803,1.119193],[9.478055,-8.569809,8.446729,-5.985924,-2.419773,0.630101],[3.802901,-4.857290,-7.488604,1.450919,5.163117,9.679560]],[[3.297262,7.991170,1.657479,5.181934,-6.422900,-7.290991],[3.843776,0.936317,-7.226430,0.205637,4.990721,1.277236],[-3.562638,3.793435,4.566174,5.014639,6.366810,-8.527765],[5.622374,6.771239,8.378268,9.537492,-2.145002,-0.454790],[8.549472,-4.440272,8.595309,-3.450313,3.290133,-2.597192],[-4.986998,6.583897,-2.357633,-0.602160,8.979508,3.991792],[4.674680,-0.386950,5.721449,3.120118,-2.732905,3.075929],[5.914780,6.150720,-2.888525,8.568103,2.019104,-5.966524],[4.964097,5.842876,-0.068671,2.751774,7.173393,6.834150],[8.995929,0.793311,-4.166524,3.553644,-4.784811,-1.748571],[-7.006323,9.586400,0.746598,6.419943,4.753287,3.793815],[3.386185,2.743553,-3.517827,-2.061752,9.377206,-5.556538],[-8.019516,-9.672124,-1.954342,5.591020,-5.184776,2.499523],[-4.079377,-6.997587,8.628158,2.542727,2.038771,-1.331374],[6.114429,2.331443,-7.472448,4.433803,7.675482,-7.004236],[-5.622221,8.461449,-4.215926,-1.823731,2.637243,-2.066893]]], dtype = "float32")#candidate|1496|(3, 16, 6)|const|float32
bop_1497 = relay.floor_mod(const_1495.astype('float32'), relay.reshape(const_1496.astype('float32'), relay.shape_of(const_1495))) # shape=(3, 16, 6)
uop_1507 = relay.asin(const_1495.astype('float64')) # shape=(3, 16, 6)
bop_1513 = relay.logical_and(uop_1507.astype('bool'), relay.reshape(const_1495.astype('bool'), relay.shape_of(uop_1507))) # shape=(3, 16, 6)
output = relay.Tuple([bop_1497,bop_1513,])
output2 = relay.Tuple([bop_1497,bop_1513,])
func_1522 = relay.Function([], output)
mod['func_1522'] = func_1522
mod = relay.transform.InferType()(mod)
mutated_mod['func_1522'] = func_1522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mutated_mod.get_global_var('func_1522')
call_1523 = func_1522_call()
output = call_1523
func_1524 = relay.Function([], output)
mutated_mod['func_1524'] = func_1524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_1528 = relay.TupleGetItem(func_1522_call(), 1)
call_1529 = relay.TupleGetItem(func_1524_call(), 1)
output = call_1528
output2 = call_1529
func_1537 = relay.Function([], output)
mod['func_1537'] = func_1537
mod = relay.transform.InferType()(mod)
mutated_mod['func_1537'] = func_1537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mutated_mod.get_global_var('func_1537')
call_1538 = func_1537_call()
output = call_1538
func_1539 = relay.Function([], output)
mutated_mod['func_1539'] = func_1539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_1548 = func_1537_call()
call_1549 = func_1537_call()
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_1552 = relay.TupleGetItem(func_1522_call(), 0)
call_1553 = relay.TupleGetItem(func_1524_call(), 0)
func_327_call = mod.get_global_var('func_327')
func_331_call = mutated_mod.get_global_var('func_331')
const_1563 = relay.const([8,4,5,5,6,-1,-6,-10,-5,3,-7,4,-6,-1,-8,-10,-10,-8,10,-9,7,1,-8,-10], dtype = "uint32")#candidate|1563|(24,)|const|uint32
var_1564 = relay.var("var_1564", dtype = "uint32", shape = (384, 1))#candidate|1564|(384, 1)|var|uint32
call_1562 = func_327_call(relay.reshape(const_1563.astype('uint32'), [8, 1, 3]), relay.reshape(var_1564.astype('uint32'), [8, 16, 3]), )
call_1565 = func_327_call(relay.reshape(const_1563.astype('uint32'), [8, 1, 3]), relay.reshape(var_1564.astype('uint32'), [8, 16, 3]), )
bop_1571 = relay.minimum(var_1564.astype('uint8'), const_1563.astype('uint8')) # shape=(384, 24)
output = relay.Tuple([call_1548,call_1552,call_1562,bop_1571,])
output2 = relay.Tuple([call_1549,call_1553,call_1565,bop_1571,])
func_1574 = relay.Function([var_1564,], output)
mod['func_1574'] = func_1574
mod = relay.transform.InferType()(mod)
var_1575 = relay.var("var_1575", dtype = "uint32", shape = (384, 1))#candidate|1575|(384, 1)|var|uint32
output = func_1574(var_1575)
func_1576 = relay.Function([var_1575], output)
mutated_mod['func_1576'] = func_1576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_1674 = relay.TupleGetItem(func_1522_call(), 0)
call_1675 = relay.TupleGetItem(func_1524_call(), 0)
uop_1676 = relay.acos(call_1674.astype('float32')) # shape=(3, 16, 6)
uop_1678 = relay.acos(call_1675.astype('float32')) # shape=(3, 16, 6)
func_1574_call = mod.get_global_var('func_1574')
func_1576_call = mutated_mod.get_global_var('func_1576')
var_1697 = relay.var("var_1697", dtype = "uint32", shape = (384,))#candidate|1697|(384,)|var|uint32
call_1696 = relay.TupleGetItem(func_1574_call(relay.reshape(var_1697.astype('uint32'), [384, 1])), 3)
call_1698 = relay.TupleGetItem(func_1576_call(relay.reshape(var_1697.astype('uint32'), [384, 1])), 3)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_1706 = func_1537_call()
call_1707 = func_1537_call()
uop_1709 = relay.tan(call_1706.astype('float32')) # shape=(3, 16, 6)
uop_1711 = relay.tan(call_1707.astype('float32')) # shape=(3, 16, 6)
func_327_call = mod.get_global_var('func_327')
func_331_call = mutated_mod.get_global_var('func_331')
const_1713 = relay.const([-5,9,-8,-5,9,-6,-9,3,2,-7,9,-4,10,-4,-8,-8,-10,6,-9,2,-4,-7,7,-4], dtype = "uint32")#candidate|1713|(24,)|const|uint32
call_1712 = func_327_call(relay.reshape(const_1713.astype('uint32'), [8, 1, 3]), relay.reshape(var_1697.astype('uint32'), [8, 16, 3]), )
call_1714 = func_327_call(relay.reshape(const_1713.astype('uint32'), [8, 1, 3]), relay.reshape(var_1697.astype('uint32'), [8, 16, 3]), )
func_1076_call = mod.get_global_var('func_1076')
func_1083_call = mutated_mod.get_global_var('func_1083')
const_1716 = relay.const([-4.409919,-7.939488,4.608635,7.844693,-7.290493,-1.662738,5.404699,5.766690,1.713150,-0.420767,-1.943116,0.909119,-9.676619,-0.269696,-1.221063,9.240813,-1.927653,-8.947375,-9.586386,-0.921664,4.658663,-2.675859,-1.359523,2.809238,-3.573993,2.387818,-3.519177,8.635223,2.906743,-9.889478,7.107680,7.700518,-8.507392,9.389079,0.987957,8.840611,-5.134138,2.637880,0.125790,-4.952981,-2.839011,-4.801329,-2.952518,0.638752,5.808162,-8.469159,-5.732874,-5.469820,8.664927,7.849971,-8.684171,0.176578,2.402771,3.341622,0.734753,-8.519540,5.619963,7.240239,-3.001663,-7.958774,-7.530157,-3.369799,-6.486454,9.914382,-2.860282,-2.595136,3.627181,3.549013,2.638288,1.506675,-8.645589,-2.328620,-9.941576,-8.528340,4.000946,-3.877933,8.201728,-4.827704,-2.146684,0.028502,-5.206994,5.715847,0.081841,-5.789150,1.195645,-9.496028,8.776215,-6.482746,-4.463777,-5.893245,5.233403,1.495998,6.083190,-9.839613,-1.628160,-8.485422,2.657492,-5.486871,-1.332894,2.110586,9.726641,-5.329361,9.010284,-1.988678,9.564842,6.754127,-9.125440,9.665773,-0.297512,4.810055,2.288502,1.806194,8.850282,9.972496,6.465293,6.323412,-3.158590,2.891612,-2.262467,3.192324,1.320162,-3.609174,-8.808977,2.184109,4.157650,5.654999,8.287017,-0.221932,-5.594095,-8.186561,-0.046508,-8.557305,4.593034,-7.103765,-3.485017,9.458887,-0.430919,3.978983,4.758451,8.173813,2.229260,2.535241,-9.805156,2.882462,-8.223858,-8.544802,4.002508,6.167544,-9.877099,6.883173,-8.463779,-5.478910,-5.351685,3.495593,2.835694,9.318994,8.639238,1.328044,-2.175718,-6.612536,-9.607706,8.614739,-3.836614,1.538376,9.680276,7.230432,2.609704,-8.764660,5.088025,-1.030822,9.502869,4.455788,-5.816099,-9.467513,3.002936,0.203158,4.993086,7.977059,-8.549354,-0.424186,9.272741,4.472718,-7.486180,2.360044,6.958739,-0.533655,4.334932,9.170649,-8.026982,-4.303447,-2.572200,3.644728,-0.402199,3.691529,4.634764,-5.114755,5.621176,-3.354981,-1.377497,7.525234,4.036246,-7.821246,0.071932,-9.544945,8.468494,6.321682,6.550120,9.764231,-9.705616,-2.700703,-7.458566,-7.288435,-1.624401,7.321705,-6.599616,-7.430192,-0.743510,-3.364117,-1.041077,8.712753,4.199471,0.945302,-5.106130,0.187860,-0.065286,-7.477713,-5.245602,-9.609913,8.812908,5.775360,5.897420,5.506847,-3.454792,6.921902,0.695261,-7.292331,-6.058207,6.774736,-7.544997,0.345840,-5.095428,-7.510834,-4.559085,1.325277,-9.100700,-5.966235,-2.862328,-6.408412,7.106703,1.138685,-4.213020,-8.049117,4.656852,8.972819,-9.886952,-7.662250,6.836919,6.766773,-2.851645,8.402695,-2.265220,-1.014292,-2.392157,4.601635,-2.892207,-6.397788,9.537700,5.207318,-1.070568,-8.573913,7.583284,0.791062,2.078636,1.981323,7.312553,5.907839,-0.647276,-6.181115,-2.785852,-3.144742,-3.043113,9.622875,9.016972,-1.928943,-6.662958,-1.728749,-2.968964,-0.410045,4.362747,9.213221,-2.856207,-1.961180,-5.972277,5.319028,-4.051993,2.313043,-4.202123,-5.057452,-4.840691,3.195420,-7.982128,-2.712834,8.567747,-3.467834,-1.414377,4.935302,-9.620457,9.123117,-0.910208,0.557087,3.874196,6.775180,-3.460069,2.738717,5.866347,8.149457,2.867958,-9.102668,-3.480085,5.526681,-0.969717,8.737084,-2.371595,3.434658,-7.035802,2.132749,0.700295,0.888622,4.740799,-4.919462,-0.788567,-9.953999,-5.769418,-9.822411,8.100202,5.176055,1.399855,0.975733,-2.221337,-9.586869,1.215234,-9.190663,9.752179,-1.547439,-4.241633,3.816671,-0.647933,-5.114223,-5.455172,3.280354,-8.619484,1.175892,-0.993437,1.808293,4.408176,4.238133,-7.147342,6.281919,9.082223,-8.153104,2.252299,-6.023838,1.948005,-6.722915,-2.295524,2.626749,-3.590915,-6.908360,1.398411,0.636269,5.584717,-0.030293,-1.956777,4.280855,4.140436,-0.256635,3.746702,7.499259,3.276443,-4.167976,7.318317,6.902073,-9.404439,-4.810185,6.448999,-7.197473,-8.881468,-3.619205,9.968956,7.080786,5.313020,9.307176,-5.229130,1.195208,-9.104606,2.609481,-9.541995,3.232890,-0.657776,-3.089727,-2.680029,4.681560,7.184610,0.390817,6.246944,-7.053641,-0.939315,-0.915827,-4.478266,8.863517,8.006918,-2.829631,1.757365,7.599280,-8.186441,3.850716,-5.302927,5.733638,8.861056,-3.063752,6.042378,1.371401,-4.037166,5.413993,-3.212649,0.260548,2.057040,8.198633,-9.526890,8.650690,-0.012966,1.086786,7.420341,7.756454,5.173777,5.240308,-8.611149,5.250321,-0.446461,9.040558,8.896724,0.819356,-1.119099,8.039659,8.052488,5.374983,2.255719,-7.155447,-7.250173,6.299103,-9.049838,-7.239653,-9.537068,0.519309,-8.086292,1.344451,-7.088105,2.817729,2.810811,6.096276,7.881390,-4.966912,7.089428,4.283463,-4.037645,7.233517,8.678067,0.228574,1.145273,3.823589,0.938568,3.485591,5.504900,7.697938,6.646809,9.887889,8.313380,-2.051393,-5.320007,-9.771407,-0.333202,9.716377,-3.577227,7.579860,-2.062999,3.927167,7.326072,8.068319,4.540255,3.707599,8.419349,7.101866,3.839867,0.798022,7.460625,-6.863036,6.635369,-2.430211,9.565584,-2.553296,-9.573851,1.067218,-6.491334,-8.544807,3.025165,5.735553,-9.253328,-1.008218,-5.525829,8.706608,5.424272,2.686699,-8.180327,-7.359431,-0.284265,6.211443,3.605097,-0.508520,5.683196,1.902612,1.149591,0.599820,-6.409932,8.165113,6.489165,-5.845456,-7.893368,1.532538,1.827365,-2.234983,-4.248373,-3.745461,2.783496,-1.415463,9.744548,9.556335,-6.109720,-6.845182,-0.817981,0.540827,3.346404,2.246854,0.767101,-8.520662,-9.728587,-7.834802,-8.943584,-3.470259,-5.905910,-2.544932,4.155248,-0.082450,-6.210393,-1.546129,-2.937245,-6.559234,5.903937,3.430968,-7.108697,-5.249520,6.200561,-8.184849,8.799429,8.892951,4.183267,-1.010452,7.186129,-0.076537,0.179902,3.650239,-3.577024,4.405331,7.677480,-1.406570,-3.108833,-6.574731], dtype = "float32")#candidate|1716|(576,)|const|float32
var_1717 = relay.var("var_1717", dtype = "float32", shape = (64,))#candidate|1717|(64,)|var|float32
var_1718 = relay.var("var_1718", dtype = "float32", shape = (80, 4))#candidate|1718|(80, 4)|var|float32
call_1715 = relay.TupleGetItem(func_1076_call(relay.reshape(const_1716.astype('float32'), [9, 16, 4]), relay.reshape(const_1713.astype('uint32'), [24,]), relay.reshape(var_1697.astype('uint32'), [384,]), relay.reshape(var_1717.astype('float32'), [64,]), relay.reshape(var_1718.astype('float32'), [320,]), relay.reshape(var_1697.astype('uint32'), [8, 16, 3]), ), 7)
call_1719 = relay.TupleGetItem(func_1083_call(relay.reshape(const_1716.astype('float32'), [9, 16, 4]), relay.reshape(const_1713.astype('uint32'), [24,]), relay.reshape(var_1697.astype('uint32'), [384,]), relay.reshape(var_1717.astype('float32'), [64,]), relay.reshape(var_1718.astype('float32'), [320,]), relay.reshape(var_1697.astype('uint32'), [8, 16, 3]), ), 7)
output = relay.Tuple([uop_1676,call_1696,var_1697,uop_1709,call_1712,const_1713,call_1715,const_1716,var_1717,var_1718,])
output2 = relay.Tuple([uop_1678,call_1698,var_1697,uop_1711,call_1714,const_1713,call_1719,const_1716,var_1717,var_1718,])
func_1724 = relay.Function([var_1697,var_1717,var_1718,], output)
mod['func_1724'] = func_1724
mod = relay.transform.InferType()(mod)
var_1725 = relay.var("var_1725", dtype = "uint32", shape = (384,))#candidate|1725|(384,)|var|uint32
var_1726 = relay.var("var_1726", dtype = "float32", shape = (64,))#candidate|1726|(64,)|var|float32
var_1727 = relay.var("var_1727", dtype = "float32", shape = (80, 4))#candidate|1727|(80, 4)|var|float32
output = func_1724(var_1725,var_1726,var_1727,)
func_1728 = relay.Function([var_1725,var_1726,var_1727,], output)
mutated_mod['func_1728'] = func_1728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_1750 = func_1537_call()
call_1751 = func_1537_call()
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_1769 = func_1537_call()
call_1770 = func_1537_call()
func_327_call = mod.get_global_var('func_327')
func_331_call = mutated_mod.get_global_var('func_331')
const_1789 = relay.const([7,8,-9,1,6,-4,1,-7,-10,3,-4,-1,6,-8,-2,-8,7,7,2,-9,-3,-7,8,3], dtype = "uint32")#candidate|1789|(24,)|const|uint32
var_1790 = relay.var("var_1790", dtype = "uint32", shape = (384,))#candidate|1790|(384,)|var|uint32
call_1788 = func_327_call(relay.reshape(const_1789.astype('uint32'), [8, 1, 3]), relay.reshape(var_1790.astype('uint32'), [8, 16, 3]), )
call_1791 = func_327_call(relay.reshape(const_1789.astype('uint32'), [8, 1, 3]), relay.reshape(var_1790.astype('uint32'), [8, 16, 3]), )
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_1806 = func_1537_call()
call_1807 = func_1537_call()
func_1076_call = mod.get_global_var('func_1076')
func_1083_call = mutated_mod.get_global_var('func_1083')
var_1814 = relay.var("var_1814", dtype = "float32", shape = (576,))#candidate|1814|(576,)|var|float32
var_1815 = relay.var("var_1815", dtype = "float32", shape = (64,))#candidate|1815|(64,)|var|float32
var_1816 = relay.var("var_1816", dtype = "float32", shape = (160, 2))#candidate|1816|(160, 2)|var|float32
call_1813 = relay.TupleGetItem(func_1076_call(relay.reshape(var_1814.astype('float32'), [9, 16, 4]), relay.reshape(const_1789.astype('uint32'), [24,]), relay.reshape(call_1788.astype('uint32'), [384,]), relay.reshape(var_1815.astype('float32'), [64,]), relay.reshape(var_1816.astype('float32'), [320,]), relay.reshape(var_1790.astype('uint32'), [8, 16, 3]), ), 1)
call_1817 = relay.TupleGetItem(func_1083_call(relay.reshape(var_1814.astype('float32'), [9, 16, 4]), relay.reshape(const_1789.astype('uint32'), [24,]), relay.reshape(call_1788.astype('uint32'), [384,]), relay.reshape(var_1815.astype('float32'), [64,]), relay.reshape(var_1816.astype('float32'), [320,]), relay.reshape(var_1790.astype('uint32'), [8, 16, 3]), ), 1)
func_1076_call = mod.get_global_var('func_1076')
func_1083_call = mutated_mod.get_global_var('func_1083')
call_1822 = relay.TupleGetItem(func_1076_call(relay.reshape(var_1814.astype('float32'), [9, 16, 4]), relay.reshape(const_1789.astype('uint32'), [24,]), relay.reshape(call_1788.astype('uint32'), [384,]), relay.reshape(var_1815.astype('float32'), [64,]), relay.reshape(var_1816.astype('float32'), [320,]), relay.reshape(call_1788.astype('uint32'), [8, 16, 3]), ), 0)
call_1823 = relay.TupleGetItem(func_1083_call(relay.reshape(var_1814.astype('float32'), [9, 16, 4]), relay.reshape(const_1789.astype('uint32'), [24,]), relay.reshape(call_1788.astype('uint32'), [384,]), relay.reshape(var_1815.astype('float32'), [64,]), relay.reshape(var_1816.astype('float32'), [320,]), relay.reshape(call_1788.astype('uint32'), [8, 16, 3]), ), 0)
func_1574_call = mod.get_global_var('func_1574')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_1826 = relay.TupleGetItem(func_1574_call(relay.reshape(call_1788.astype('uint32'), [384, 1])), 2)
call_1827 = relay.TupleGetItem(func_1576_call(relay.reshape(call_1788.astype('uint32'), [384, 1])), 2)
output = relay.Tuple([call_1750,call_1769,call_1788,const_1789,var_1790,call_1806,call_1813,var_1814,var_1815,var_1816,call_1822,call_1826,])
output2 = relay.Tuple([call_1751,call_1770,call_1791,const_1789,var_1790,call_1807,call_1817,var_1814,var_1815,var_1816,call_1823,call_1827,])
func_1832 = relay.Function([var_1790,var_1814,var_1815,var_1816,], output)
mod['func_1832'] = func_1832
mod = relay.transform.InferType()(mod)
var_1833 = relay.var("var_1833", dtype = "uint32", shape = (384,))#candidate|1833|(384,)|var|uint32
var_1834 = relay.var("var_1834", dtype = "float32", shape = (576,))#candidate|1834|(576,)|var|float32
var_1835 = relay.var("var_1835", dtype = "float32", shape = (64,))#candidate|1835|(64,)|var|float32
var_1836 = relay.var("var_1836", dtype = "float32", shape = (160, 2))#candidate|1836|(160, 2)|var|float32
output = func_1832(var_1833,var_1834,var_1835,var_1836,)
func_1837 = relay.Function([var_1833,var_1834,var_1835,var_1836,], output)
mutated_mod['func_1837'] = func_1837
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1848 = relay.var("var_1848", dtype = "int16", shape = (11, 4, 3))#candidate|1848|(11, 4, 3)|var|int16
const_1849 = relay.const([[[5,-1,-8],[10,-3,2],[-6,2,5],[-10,-8,7]],[[-2,9,-4],[5,2,-6],[5,6,8],[3,-8,5]],[[-10,6,-9],[-2,-6,4],[3,9,-5],[6,3,-10]],[[-3,9,10],[7,-1,10],[4,3,-10],[9,-8,1]],[[-3,5,-10],[-1,10,6],[-3,1,-4],[8,-2,-9]],[[9,8,-6],[3,5,-7],[5,-9,7],[-6,-8,8]],[[8,3,6],[2,2,7],[8,-9,-9],[9,-2,10]],[[8,2,5],[-2,-4,4],[-9,-9,8],[-10,5,-1]],[[-6,8,-3],[-7,-4,-6],[9,-3,3],[4,4,4]],[[9,-10,5],[-9,-2,-9],[5,5,-7],[10,9,8]],[[1,-7,-9],[-8,-6,5],[10,10,-8],[8,-5,5]]], dtype = "int16")#candidate|1849|(11, 4, 3)|const|int16
bop_1850 = relay.less(var_1848.astype('bool'), relay.reshape(const_1849.astype('bool'), relay.shape_of(var_1848))) # shape=(11, 4, 3)
bop_1864 = relay.power(const_1849.astype('float64'), relay.reshape(bop_1850.astype('float64'), relay.shape_of(const_1849))) # shape=(11, 4, 3)
output = relay.Tuple([bop_1864,])
output2 = relay.Tuple([bop_1864,])
func_1867 = relay.Function([var_1848,], output)
mod['func_1867'] = func_1867
mod = relay.transform.InferType()(mod)
var_1868 = relay.var("var_1868", dtype = "int16", shape = (11, 4, 3))#candidate|1868|(11, 4, 3)|var|int16
output = func_1867(var_1868)
func_1869 = relay.Function([var_1868], output)
mutated_mod['func_1869'] = func_1869
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1892 = relay.var("var_1892", dtype = "float64", shape = (10, 2, 8))#candidate|1892|(10, 2, 8)|var|float64
uop_1893 = relay.asin(var_1892.astype('float64')) # shape=(10, 2, 8)
output = relay.Tuple([uop_1893,])
output2 = relay.Tuple([uop_1893,])
func_1901 = relay.Function([var_1892,], output)
mod['func_1901'] = func_1901
mod = relay.transform.InferType()(mod)
var_1902 = relay.var("var_1902", dtype = "float64", shape = (10, 2, 8))#candidate|1902|(10, 2, 8)|var|float64
output = func_1901(var_1902)
func_1903 = relay.Function([var_1902], output)
mutated_mod['func_1903'] = func_1903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_1977 = func_1537_call()
call_1978 = func_1537_call()
func_1076_call = mod.get_global_var('func_1076')
func_1083_call = mutated_mod.get_global_var('func_1083')
var_1983 = relay.var("var_1983", dtype = "float32", shape = (576,))#candidate|1983|(576,)|var|float32
var_1984 = relay.var("var_1984", dtype = "uint32", shape = (24,))#candidate|1984|(24,)|var|uint32
var_1985 = relay.var("var_1985", dtype = "uint32", shape = (384,))#candidate|1985|(384,)|var|uint32
const_1986 = relay.const([6.942579,1.794785,-1.307228,-4.002762,-9.743525,-4.363073,-9.791503,-9.656079,7.641184,8.880298,-7.742588,-7.240510,3.332645,6.319024,-6.416586,7.930656,-0.190326,-5.763142,-1.514737,8.110182,-0.476986,-3.450321,-7.610439,0.923638,3.101466,-2.787262,-6.528703,-5.484474,8.547487,-2.174722,-2.487074,-7.248801,-9.236834,1.072666,2.761082,6.148523,-3.466069,0.374345,-9.132433,-7.169741,7.060970,5.858797,5.832627,-8.541330,3.084284,-9.816079,-4.037868,-7.734013,4.070131,5.312615,0.790869,-6.851590,-6.577725,-9.056271,3.238835,-6.084848,4.448291,-1.545713,4.737808,-6.067114,1.606435,3.729472,6.408320,-5.612457], dtype = "float32")#candidate|1986|(64,)|const|float32
const_1987 = relay.const([-1.211950,1.142968,4.224706,1.641076,-4.758880,-0.887500,0.844181,1.178115,9.352658,6.943035,-9.374918,-9.829594,7.302408,3.713682,-9.789612,5.682115,-3.580992,3.066220,-3.896273,-0.318906,-3.166091,6.469427,6.593212,-8.957524,-4.158882,2.411096,-5.027730,-5.573194,-9.832643,6.113457,-7.091423,1.570770,2.639232,1.491364,4.310979,-2.492596,-4.455223,5.469170,-7.382919,-2.662773,-7.303405,-6.799147,9.203550,-4.529048,-3.892939,-4.823442,-4.115130,4.395111,-8.477941,9.816941,8.524299,0.937893,4.176642,2.288068,-2.018913,-9.307156,-4.325320,-5.967198,6.387556,5.394059,-9.327549,7.653621,-0.115291,-1.953187,9.106209,-1.090964,9.323518,-7.493541,3.094298,1.450345,0.844225,-9.242358,-5.246141,1.518306,9.071348,5.921124,-3.285208,-4.697453,9.810671,5.388647,-8.954171,5.485010,9.100338,4.527300,-9.603830,-8.153293,-9.589185,8.395181,5.255193,0.853051,7.502568,-6.193089,6.936901,-6.017557,6.757943,6.366205,-8.490675,-0.856679,-8.069887,-8.608523,-2.051081,-7.272084,3.609691,3.448511,-4.781611,1.442253,5.891145,0.958200,-0.677863,8.158531,3.189042,6.966461,-0.289178,3.224517,2.020949,9.556954,-6.483592,7.859788,8.035801,7.567105,4.400956,5.498653,-4.805797,4.633245,6.806510,8.485830,6.265621,-3.450628,-0.332084,-1.835224,3.053720,8.350663,1.733221,3.784821,6.954878,-5.846513,3.491247,8.951036,-5.277920,-3.275203,4.554188,-4.575370,-8.828085,-0.302596,-7.380993,1.854845,-7.691394,6.393906,0.475864,-4.383976,9.279835,7.754037,2.974571,4.544793,9.273922,3.482709,4.178220,2.845492,-2.078187,-3.757850,-8.588814,-3.013869,-0.946002,-1.971083,-4.286625,-0.720443,6.423667,-8.029886,-5.504222,-0.936460,8.232183,-3.103278,0.374555,-3.181595,-5.650531,-9.587869,-9.918048,4.207320,-4.760634,-1.033626,9.020904,7.629738,-1.263431,5.081531,3.677211,-8.472059,0.551181,7.553252,-2.247819,-7.321999,-8.567070,5.904521,3.955854,5.209968,-6.519869,-3.069968,-9.025808,-9.257145,3.496779,0.810719,3.099240,0.294302,-3.596491,0.335995,-0.738127,7.550311,-8.106286,-3.053692,-1.245576,-2.332293,7.447779,-9.174040,-3.125207,4.983705,-4.178396,-6.687509,-9.560909,-2.494410,-0.158531,-8.200488,2.516031,1.695854,-3.087025,6.775892,5.946026,-5.286849,-6.227544,-8.071064,5.290336,-1.532868,-5.610347,-0.141198,-1.894141,6.711291,-1.490922,3.520744,-7.527915,-7.817671,-2.725570,8.350113,3.103435,3.153959,-5.775160,-7.974010,6.058935,7.317045,9.513558,-8.677720,-5.346518,-6.899011,7.935147,-1.614663,-0.036311,8.877165,-8.841552,-7.444987,-9.306415,2.821160,4.278249,-6.763775,-5.293560,-0.634127,4.304419,7.869683,-8.813301,6.006980,9.956862,1.977376,-9.068774,4.826950,4.900032,-4.935339,2.087924,-0.510476,5.511543,5.994165,-8.042700,6.493285,-4.986585,9.818395,-4.475832,7.683001,-5.947642,5.392347,0.456326,2.550674,-2.760453,-9.832624,9.638269,-9.645517,9.023650,-8.373476,5.158091,-0.104394,-7.467483,-1.977275,-0.328191,0.921215,7.925346,4.175851,8.652261,0.959615,-9.435152,8.415291,7.238071,-7.876123,8.296443,-2.314870,-3.460486,-5.852735,2.427738,0.109902,-9.217821,-6.721853,3.950275,-3.089652,8.856652,-8.995745,0.140933,7.306730], dtype = "float32")#candidate|1987|(320,)|const|float32
call_1982 = relay.TupleGetItem(func_1076_call(relay.reshape(var_1983.astype('float32'), [9, 16, 4]), relay.reshape(var_1984.astype('uint32'), [24,]), relay.reshape(var_1985.astype('uint32'), [384,]), relay.reshape(const_1986.astype('float32'), [64,]), relay.reshape(const_1987.astype('float32'), [320,]), relay.reshape(var_1985.astype('uint32'), [8, 16, 3]), ), 4)
call_1988 = relay.TupleGetItem(func_1083_call(relay.reshape(var_1983.astype('float32'), [9, 16, 4]), relay.reshape(var_1984.astype('uint32'), [24,]), relay.reshape(var_1985.astype('uint32'), [384,]), relay.reshape(const_1986.astype('float32'), [64,]), relay.reshape(const_1987.astype('float32'), [320,]), relay.reshape(var_1985.astype('uint32'), [8, 16, 3]), ), 4)
var_2017 = relay.var("var_2017", dtype = "bool", shape = (5, 4, 16))#candidate|2017|(5, 4, 16)|var|bool
bop_2018 = relay.add(call_1982.astype('int8'), relay.reshape(var_2017.astype('int8'), relay.shape_of(call_1982))) # shape=(5, 4, 16)
bop_2021 = relay.add(call_1988.astype('int8'), relay.reshape(var_2017.astype('int8'), relay.shape_of(call_1988))) # shape=(5, 4, 16)
uop_2037 = relay.asin(bop_2018.astype('float64')) # shape=(5, 4, 16)
uop_2039 = relay.asin(bop_2021.astype('float64')) # shape=(5, 4, 16)
output = relay.Tuple([call_1977,var_1983,var_1984,var_1985,const_1986,const_1987,uop_2037,])
output2 = relay.Tuple([call_1978,var_1983,var_1984,var_1985,const_1986,const_1987,uop_2039,])
func_2041 = relay.Function([var_1983,var_1984,var_1985,var_2017,], output)
mod['func_2041'] = func_2041
mod = relay.transform.InferType()(mod)
mutated_mod['func_2041'] = func_2041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2041_call = mutated_mod.get_global_var('func_2041')
var_2043 = relay.var("var_2043", dtype = "float32", shape = (576,))#candidate|2043|(576,)|var|float32
var_2044 = relay.var("var_2044", dtype = "uint32", shape = (24,))#candidate|2044|(24,)|var|uint32
var_2045 = relay.var("var_2045", dtype = "uint32", shape = (384,))#candidate|2045|(384,)|var|uint32
var_2046 = relay.var("var_2046", dtype = "bool", shape = (5, 4, 16))#candidate|2046|(5, 4, 16)|var|bool
call_2042 = func_2041_call(var_2043,var_2044,var_2045,var_2046,)
output = call_2042
func_2047 = relay.Function([var_2043,var_2044,var_2045,var_2046,], output)
mutated_mod['func_2047'] = func_2047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_2080 = relay.TupleGetItem(func_1522_call(), 0)
call_2081 = relay.TupleGetItem(func_1524_call(), 0)
var_2089 = relay.var("var_2089", dtype = "float32", shape = (3, 16, 6))#candidate|2089|(3, 16, 6)|var|float32
bop_2090 = relay.bitwise_and(call_2080.astype('int32'), relay.reshape(var_2089.astype('int32'), relay.shape_of(call_2080))) # shape=(3, 16, 6)
bop_2093 = relay.bitwise_and(call_2081.astype('int32'), relay.reshape(var_2089.astype('int32'), relay.shape_of(call_2081))) # shape=(3, 16, 6)
func_1867_call = mod.get_global_var('func_1867')
func_1869_call = mutated_mod.get_global_var('func_1869')
var_2096 = relay.var("var_2096", dtype = "int16", shape = (132,))#candidate|2096|(132,)|var|int16
call_2095 = relay.TupleGetItem(func_1867_call(relay.reshape(var_2096.astype('int16'), [11, 4, 3])), 0)
call_2097 = relay.TupleGetItem(func_1869_call(relay.reshape(var_2096.astype('int16'), [11, 4, 3])), 0)
output = relay.Tuple([bop_2090,call_2095,var_2096,])
output2 = relay.Tuple([bop_2093,call_2097,var_2096,])
func_2099 = relay.Function([var_2089,var_2096,], output)
mod['func_2099'] = func_2099
mod = relay.transform.InferType()(mod)
var_2100 = relay.var("var_2100", dtype = "float32", shape = (3, 16, 6))#candidate|2100|(3, 16, 6)|var|float32
var_2101 = relay.var("var_2101", dtype = "int16", shape = (132,))#candidate|2101|(132,)|var|int16
output = func_2099(var_2100,var_2101,)
func_2102 = relay.Function([var_2100,var_2101,], output)
mutated_mod['func_2102'] = func_2102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_2215 = func_1537_call()
call_2216 = func_1537_call()
uop_2221 = relay.sin(call_2215.astype('float64')) # shape=(3, 16, 6)
uop_2223 = relay.sin(call_2216.astype('float64')) # shape=(3, 16, 6)
var_2226 = relay.var("var_2226", dtype = "float64", shape = (3, 16, 6))#candidate|2226|(3, 16, 6)|var|float64
bop_2227 = relay.bitwise_xor(uop_2221.astype('uint32'), relay.reshape(var_2226.astype('uint32'), relay.shape_of(uop_2221))) # shape=(3, 16, 6)
bop_2230 = relay.bitwise_xor(uop_2223.astype('uint32'), relay.reshape(var_2226.astype('uint32'), relay.shape_of(uop_2223))) # shape=(3, 16, 6)
bop_2238 = relay.minimum(uop_2221.astype('int64'), relay.reshape(var_2226.astype('int64'), relay.shape_of(uop_2221))) # shape=(3, 16, 6)
bop_2241 = relay.minimum(uop_2223.astype('int64'), relay.reshape(var_2226.astype('int64'), relay.shape_of(uop_2223))) # shape=(3, 16, 6)
output = relay.Tuple([bop_2227,bop_2238,])
output2 = relay.Tuple([bop_2230,bop_2241,])
func_2261 = relay.Function([var_2226,], output)
mod['func_2261'] = func_2261
mod = relay.transform.InferType()(mod)
mutated_mod['func_2261'] = func_2261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2262 = relay.var("var_2262", dtype = "float64", shape = (3, 16, 6))#candidate|2262|(3, 16, 6)|var|float64
func_2261_call = mutated_mod.get_global_var('func_2261')
call_2263 = func_2261_call(var_2262)
output = call_2263
func_2264 = relay.Function([var_2262], output)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_2326 = relay.TupleGetItem(func_1522_call(), 0)
call_2327 = relay.TupleGetItem(func_1524_call(), 0)
func_2261_call = mod.get_global_var('func_2261')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_2329 = relay.TupleGetItem(func_2261_call(relay.reshape(call_2326.astype('float64'), [3, 16, 6])), 1)
call_2330 = relay.TupleGetItem(func_2264_call(relay.reshape(call_2326.astype('float64'), [3, 16, 6])), 1)
func_1832_call = mod.get_global_var('func_1832')
func_1837_call = mutated_mod.get_global_var('func_1837')
var_2337 = relay.var("var_2337", dtype = "uint32", shape = (24, 16))#candidate|2337|(24, 16)|var|uint32
const_2338 = relay.const([-0.535189,-1.998360,3.935391,-4.624117,-0.093868,0.550104,9.747502,-4.221557,0.021581,6.440104,7.180490,1.613486,-6.395623,7.095284,-4.528544,-1.561831,-0.599687,1.552132,6.700977,7.996185,-0.547145,2.380765,-4.462068,-7.605167,1.680111,-3.013315,-5.372307,-6.709795,-2.896045,-6.966223,-2.942269,2.268549,-0.010871,-9.846868,-7.468699,0.165276,6.190250,-3.284099,-8.942471,9.211146,-8.890158,6.317655,7.590165,-0.520123,0.010910,3.391636,5.017941,-0.754483,7.638619,6.228303,-8.160931,-8.204600,-3.181055,6.998761,-4.244403,-7.712545,-5.490794,5.132173,-1.778948,-9.102108,-8.468440,2.027890,-1.501860,5.885558,4.413777,-5.058664,-5.521513,4.521306,0.409093,5.904556,9.349063,6.822231,8.723309,5.517962,-7.693539,4.780449,3.984685,-8.365259,-8.181720,0.493729,9.552679,0.807586,9.627563,-4.461966,9.944906,-9.854586,8.769320,0.141813,-9.546676,-4.794725,-2.719165,7.451510,4.725611,5.213088,-2.199525,6.738644,-8.632267,8.892269,4.286598,4.985864,2.903944,8.594756,2.991571,-4.715373,2.132180,-6.930181,-1.933273,-7.356924,7.808256,-2.662475,-9.182958,1.152173,-0.996727,-5.301316,-4.377373,2.657464,4.850355,4.256480,2.884234,-0.287561,-0.286371,-0.879771,1.983562,-5.800546,-6.460643,-5.101829,-7.509834,-4.918099,-0.292620,-0.036059,-4.725167,-4.408301,-5.376038,-7.322290,8.874789,5.584090,4.515866,8.227784,-5.365951,1.474467,-5.504328,8.520546,-4.512711,2.315367,8.866238,9.361012,4.022488,5.395952,0.687944,1.973222,2.453318,2.370939,-1.424934,3.392456,-6.376825,-9.996249,-0.066303,-1.638065,7.279133,7.449742,7.876702,-7.435097,-8.829372,0.798829,6.732937,0.222590,5.988566,8.290705,3.859424,-5.318566,2.781454,-0.544584,-6.977117,-5.081412,-2.991728,-2.780988,2.015467,6.932180,2.858930,7.467946,7.637231,0.223251,8.515975,4.842054,7.201651,3.752141,-3.112326,-9.477669,-9.344004,-8.866914,-1.952943,-6.559222,1.098733,4.261283,-5.658551,4.841976,8.926407,-4.219692,7.613896,0.811422,6.078401,0.680349,-7.160769,5.703829,2.355867,-2.307293,-2.645314,3.280652,-7.272189,-6.791341,4.491649,-1.490805,-2.473185,-1.908932,-9.727485,-5.275520,-2.701558,5.761459,0.079379,5.752535,-0.500673,-2.880312,-7.784216,-4.352025,7.967553,-4.536767,-0.413306,5.996823,9.716351,-3.433519,-6.630283,-7.761023,8.773657,5.964077,-9.191631,1.346241,-3.837420,8.637161,0.228913,5.134840,9.535902,3.843902,8.029799,-1.346508,-4.406233,-4.017940,-7.907539,7.921614,7.949479,-8.622385,1.984414,-6.889265,-1.970702,5.906714,-6.929385,-1.381197,-9.255409,1.913924,-4.544529,-6.437997,5.946959,1.338535,0.706854,7.484271,-2.913952,-6.368777,6.610929,7.242643,5.518495,9.547748,-3.929756,6.230509,1.505378,-3.850365,-6.735064,6.149767,2.777165,0.777174,0.014065,3.461320,0.918647,-0.377983,4.161111,-1.649050,-1.818623,-0.439873,5.908044,8.928140,-9.008193,-1.315937,-7.297981,-5.597756,3.278889,4.903928,-2.342913,-3.489598,-2.311802,-6.365578,-6.918715,-2.784720,-5.996035,2.793787,-6.348755,7.735016,-8.288888,-9.611638,5.564834,2.922454,-9.635077,9.673728,2.752683,-6.426366,-4.356529,8.449548,1.356947,1.049523,-5.297015,2.738716,9.674378,-0.328886,8.319602,5.276969,8.137730,4.593312,4.754803,4.309742,-8.693592,-0.373460,-9.660974,3.986945,-5.932676,-9.394124,-2.957840,8.736116,-6.508939,6.172939,-0.610121,-9.962513,6.506701,-6.695818,-7.451017,-4.485334,7.655731,-3.511941,-8.710443,-9.125012,-1.682119,-8.424181,-6.629580,4.548690,5.376641,-6.959712,4.244938,4.469079,-4.137224,9.537479,0.789072,6.365193,-4.279395,2.264963,-9.640717,8.714068,-9.483043,2.488758,-7.335510,4.875228,2.822620,9.755291,-8.508552,-0.977450,-9.552831,1.706503,8.973281,2.488299,-9.665687,-1.730013,-2.236157,-2.985232,2.981661,0.110891,-1.315623,0.049818,2.946566,-9.257740,-0.719518,-3.044218,-5.839077,-2.277920,4.898993,2.253934,-3.513580,-3.208298,-6.968614,9.209011,-5.416858,4.619760,6.712175,-8.651472,8.484759,-9.880813,0.423494,0.413674,3.572739,3.911539,4.900058,-8.275566,1.325643,-1.492624,2.323002,4.712924,-8.784678,-7.378431,-3.433901,-6.535120,1.901428,6.050939,-2.284130,-9.444238,-2.739062,-8.443527,3.190229,-0.973753,2.939013,-1.383852,-2.863781,-6.886086,-1.804169,2.567207,7.164287,-2.785383,-8.103200,-4.446627,-5.755006,-0.418768,-2.511297,-7.821575,-4.371127,-1.475830,3.890436,-1.209111,6.520950,9.279798,-7.857983,-6.029019,-7.706797,-4.358409,-8.831660,6.768802,-2.861074,4.435102,-3.859803,-1.495860,-3.818718,-7.837441,3.103357,-2.569266,2.386837,-8.280128,-2.948541,-8.891795,3.389297,5.951750,1.996846,9.928850,5.770292,-3.308075,-5.439918,-8.431029,-2.682020,9.194391,5.548530,-2.224288,4.883998,-1.120779,8.237526,-2.735862,-4.861440,-9.337195,4.074571,6.076934,-9.035364,-9.772957,-2.921994,-2.226135,-9.241364,-1.995491,5.550013,-9.849557,0.209564,-2.419965,7.474031,1.161676,-3.337810,4.525848,3.171188,-5.729996,6.124461,9.247097,9.378596,-4.252312,3.659586,-0.259951,2.776915,0.541459,2.708081,3.615696,-9.664778,-0.729918,-8.839817,-3.377144,-5.256004,6.992450,-9.462271,5.959682,-2.072137,8.214098,-1.000481,-4.949884,-0.914428,-9.923356,5.411863,2.366785,3.890528,6.416099,5.299216,6.917061,-5.677099,0.991540,0.022048,9.447506,-1.357486,0.676858,-8.889284,-1.299945,7.866864,-0.922397,-8.144790,1.722893,-4.885898,1.648439,-7.174518,7.859437,-2.119414,1.633451,-4.391616,8.635532,9.921138,3.298774,3.709107,8.669355,9.210805,0.529758,3.825685,0.405080,5.603872,5.139270,5.970882,1.538522,-6.331685,-1.216358,8.024324,0.930852,-6.985405,-2.223212,7.271187,5.981204,6.356146,-2.657076,4.742317,-4.850224,6.251901,-1.823124,6.365945,-3.386061,1.685457,-1.001653], dtype = "float32")#candidate|2338|(576,)|const|float32
var_2339 = relay.var("var_2339", dtype = "float32", shape = (64,))#candidate|2339|(64,)|var|float32
var_2340 = relay.var("var_2340", dtype = "float32", shape = (4, 80))#candidate|2340|(4, 80)|var|float32
call_2336 = relay.TupleGetItem(func_1832_call(relay.reshape(var_2337.astype('uint32'), [384,]), relay.reshape(const_2338.astype('float32'), [576,]), relay.reshape(var_2339.astype('float32'), [64,]), relay.reshape(var_2340.astype('float32'), [160, 2]), ), 10)
call_2341 = relay.TupleGetItem(func_1837_call(relay.reshape(var_2337.astype('uint32'), [384,]), relay.reshape(const_2338.astype('float32'), [576,]), relay.reshape(var_2339.astype('float32'), [64,]), relay.reshape(var_2340.astype('float32'), [160, 2]), ), 10)
func_1901_call = mod.get_global_var('func_1901')
func_1903_call = mutated_mod.get_global_var('func_1903')
var_2346 = relay.var("var_2346", dtype = "float64", shape = (160,))#candidate|2346|(160,)|var|float64
call_2345 = relay.TupleGetItem(func_1901_call(relay.reshape(var_2346.astype('float64'), [10, 2, 8])), 0)
call_2347 = relay.TupleGetItem(func_1903_call(relay.reshape(var_2346.astype('float64'), [10, 2, 8])), 0)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_2349 = func_1537_call()
call_2350 = func_1537_call()
output = relay.Tuple([call_2326,call_2329,call_2336,var_2337,const_2338,var_2339,var_2340,call_2345,var_2346,call_2349,])
output2 = relay.Tuple([call_2327,call_2330,call_2341,var_2337,const_2338,var_2339,var_2340,call_2347,var_2346,call_2350,])
func_2377 = relay.Function([var_2337,var_2339,var_2340,var_2346,], output)
mod['func_2377'] = func_2377
mod = relay.transform.InferType()(mod)
mutated_mod['func_2377'] = func_2377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2377_call = mutated_mod.get_global_var('func_2377')
var_2379 = relay.var("var_2379", dtype = "uint32", shape = (24, 16))#candidate|2379|(24, 16)|var|uint32
var_2380 = relay.var("var_2380", dtype = "float32", shape = (64,))#candidate|2380|(64,)|var|float32
var_2381 = relay.var("var_2381", dtype = "float32", shape = (4, 80))#candidate|2381|(4, 80)|var|float32
var_2382 = relay.var("var_2382", dtype = "float64", shape = (160,))#candidate|2382|(160,)|var|float64
call_2378 = func_2377_call(var_2379,var_2380,var_2381,var_2382,)
output = call_2378
func_2383 = relay.Function([var_2379,var_2380,var_2381,var_2382,], output)
mutated_mod['func_2383'] = func_2383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_2426 = relay.TupleGetItem(func_1522_call(), 1)
call_2427 = relay.TupleGetItem(func_1524_call(), 1)
output = call_2426
output2 = call_2427
func_2428 = relay.Function([], output)
mod['func_2428'] = func_2428
mod = relay.transform.InferType()(mod)
output = func_2428()
func_2429 = relay.Function([], output)
mutated_mod['func_2429'] = func_2429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2443 = relay.var("var_2443", dtype = "float32", shape = (11, 16, 12))#candidate|2443|(11, 16, 12)|var|float32
const_2444 = relay.const([[[-2.448491,0.407841,9.241255,-5.634116,9.042104,5.942672,4.973517,-5.380510,9.480083,4.958785,-6.291532,5.794883],[3.839259,8.876076,8.388638,9.424742,1.893116,-0.735199,-2.933940,-3.001754,3.251024,-7.264098,7.134903,6.165973],[1.122255,4.572457,0.139879,-9.089523,-4.662845,1.116830,-9.847293,7.355557,8.643375,-0.747605,3.227136,3.180662],[-2.922919,0.340694,-7.054226,-2.439619,6.145058,1.324503,-4.004128,2.667988,5.068863,-7.489715,-7.877039,2.757364],[-3.546046,5.849189,3.642380,-3.463038,-0.815241,7.053121,-3.968315,-8.652802,7.203211,-6.307261,0.513865,4.688950],[-6.694404,-7.582318,3.021183,2.691829,-7.446880,5.178975,2.617502,4.264906,-6.613583,8.508233,2.771043,-1.702040],[9.188248,-5.967985,2.622456,-3.395120,-6.569613,-8.362770,-4.955698,9.269292,-3.639362,-1.999254,-3.376901,6.882860],[8.748482,6.518894,-4.010254,2.968421,-5.555654,-8.638992,8.115580,-4.907269,9.783787,-0.821813,-6.557797,-6.968546],[-1.876892,-6.050757,1.749032,8.005353,-0.985445,6.587291,2.562542,2.138791,-7.044701,0.863864,-3.556799,1.442169],[-8.139357,1.798874,7.158657,9.707007,1.435029,-4.708667,7.634516,4.505334,-5.805881,-9.164451,1.318797,-5.635954],[2.752002,-7.743264,8.319512,2.222230,7.185158,-8.621077,1.674416,-0.410686,9.761848,1.146385,1.447150,2.552020],[5.369721,8.475123,9.589589,-5.066981,6.395614,-5.288681,4.100190,-6.869707,-4.667719,0.582914,-3.188921,-6.806867],[3.656622,-1.096785,-0.362803,-0.039176,7.526156,6.301022,4.695747,1.407467,-5.077820,0.878310,7.779194,-3.837311],[-4.554830,4.035740,8.881482,8.334511,5.368605,3.547163,1.643262,5.305548,0.151773,8.646918,7.667426,1.672951],[-9.754632,5.869925,-5.923899,8.486141,0.382583,7.013028,9.716738,4.216078,-8.708316,-8.139065,0.224162,-2.194400],[-8.797316,8.610970,-1.888193,5.075196,-1.759259,3.986397,-5.403059,3.744179,3.032781,9.285321,3.777262,-3.912075]],[[0.698286,7.338315,-9.687590,-7.210684,0.779536,-5.475683,-7.252780,-1.500491,-6.726021,-0.206352,9.475093,1.832465],[-3.780162,3.537400,7.271050,-3.301606,-7.341243,2.737827,1.688420,-8.235866,-0.520323,3.870302,-6.999940,2.669048],[6.814167,-1.323081,6.256512,0.044034,-2.134308,-5.060980,-2.353598,-5.074574,-0.238395,-1.426493,5.352020,5.735443],[8.919941,6.541000,-9.334780,0.414928,-0.036050,-0.844514,5.464348,4.364370,-0.620152,7.484122,-9.571360,-9.606236],[-0.091925,0.745076,8.978552,3.737864,8.216423,-2.935250,4.467351,3.492648,2.630107,6.585769,1.706448,-1.887994],[-4.433913,0.623006,-7.335928,-0.877476,-4.404207,-9.896995,-3.581761,-0.773496,-1.269526,8.080012,-1.965530,7.865942],[6.858615,-0.541641,-2.369712,-4.612037,9.562446,8.756588,3.776081,-8.689642,5.547478,1.461560,-4.133329,9.053042],[6.285834,-6.192607,4.852731,7.862418,-9.309627,-9.036947,1.253423,-2.955668,-5.471329,-1.428118,8.924557,9.508491],[3.465915,-1.486288,-3.939771,7.890807,-2.319136,-9.989936,6.736415,-1.825230,7.741378,-9.151932,-4.239591,3.990046],[6.576299,-2.161824,-0.781969,2.638215,2.085795,9.085510,-8.006996,8.589380,-8.707765,-5.986502,7.755931,-3.418941],[8.239770,3.058498,5.288660,-8.109666,-5.597041,6.833110,-2.513548,1.384106,-2.891440,-6.216596,7.750254,2.177834],[0.390435,3.642311,3.564729,5.493000,4.081859,-9.345842,-9.051464,2.187283,9.474435,2.023191,9.752037,2.119420],[-1.502125,-2.021213,9.953038,9.541780,-9.232927,-6.139102,-4.028403,-8.543637,-1.869784,-1.202395,-8.031033,-5.108938],[-1.643912,2.065137,-1.053480,7.945455,-8.241798,-5.735067,-6.711719,-0.690794,-1.004349,-4.566766,6.661708,-0.883459],[3.863269,-2.179125,-7.956728,5.919973,-8.327618,8.129233,-7.656127,2.037483,-0.259875,-2.670083,-3.901811,7.471295],[3.658452,0.641499,4.372942,8.412618,5.647088,-5.867896,-1.804852,-4.077131,-3.413507,8.942371,3.292611,-9.938055]],[[-6.152509,-3.087870,4.034885,8.866371,4.403229,2.037501,2.885230,5.887916,-8.654506,-0.694773,5.716818,-2.195874],[-8.682598,-1.150508,-1.359453,-1.436706,-7.620899,8.811147,-3.306338,-5.884417,-7.137575,-2.313765,-2.727597,-0.333075],[1.851467,6.356405,1.159568,7.361201,6.611548,0.312009,-5.028986,-0.973926,-7.989346,-5.678824,4.955724,-6.420481],[1.146787,4.938320,-3.006002,-9.483735,-6.731946,1.578842,5.781517,-6.889328,-8.603950,3.248483,7.977389,1.986773],[1.145170,-0.340170,0.613762,-5.955555,-2.526267,-5.148091,7.093314,-8.200431,9.303040,-7.429117,-4.206173,0.844476],[-6.566074,6.851059,9.026305,-3.144424,2.342323,7.430921,8.668296,3.963395,7.482879,8.944638,-4.889875,-0.067158],[5.819999,6.216484,7.866244,-5.766576,2.809875,1.379950,7.499517,4.025967,7.055388,0.550992,8.642608,-4.691993],[-1.669463,6.170338,8.249554,-5.196378,-4.463641,3.463945,7.551076,-6.130881,1.294837,9.802338,2.790654,3.151163],[4.638801,6.484974,0.081304,1.579393,0.737140,2.843559,-9.711109,2.535866,4.241386,0.326748,5.889578,2.685355],[7.542012,1.757216,2.485925,8.459540,6.159173,9.773729,-2.230648,-3.858827,-7.786224,9.904236,-6.515797,3.643397],[8.537929,-6.084138,-1.990541,2.393188,-0.274734,-4.959396,-5.611873,-9.446580,0.129282,-3.343194,-8.051188,0.405944],[-8.301370,2.795521,-6.245253,-2.545860,3.281352,-0.676329,-3.053958,-5.238583,-7.410581,9.637108,-4.242134,-4.645460],[5.577781,-0.630139,8.074375,-0.628537,-3.105735,-3.462969,3.267288,-3.867322,7.913908,-9.894986,-7.407955,-5.674626],[-5.664563,5.624190,1.105352,-5.347601,5.145904,-1.186572,-1.096696,-5.220755,6.899003,1.699666,-3.637900,6.408741],[-9.706531,3.950281,-6.671249,3.982783,9.102648,-1.624562,-4.721733,-7.236871,2.351585,0.849393,3.574630,-5.454303],[-5.992263,7.651325,9.393807,5.461147,6.526454,-7.307676,-3.137414,-3.308074,7.479715,2.058698,6.851816,1.048384]],[[-5.270799,-5.372332,-6.874434,-9.689777,4.163680,7.649138,6.592524,-7.450915,-6.867223,-8.796197,4.297255,-7.177164],[9.595555,-6.308361,2.526380,5.883132,-2.833685,-6.353107,-1.989219,-1.667683,-0.067998,-8.333395,-7.147173,-3.663061],[-2.449642,6.119429,1.117667,-3.636213,8.858468,5.755884,-6.693126,4.594679,6.829844,3.111644,-2.438476,3.772839],[-6.094137,-9.540310,-8.452362,5.303062,-2.267339,-8.759207,-7.235284,-0.196313,-8.436171,5.492392,1.155393,6.135397],[-8.118679,-5.888121,-2.908643,3.518766,-1.552429,1.929250,8.369367,2.483304,-5.497995,6.884038,-5.798321,-7.492823],[-2.047805,2.735467,-0.091215,-5.877621,8.850583,-7.414922,-2.285261,-8.530735,6.407737,4.602581,-3.654197,-8.809694],[7.715371,-4.720271,-4.279390,-8.701034,-7.747151,-9.439672,-5.489784,3.368848,2.845853,-4.280799,7.081078,-7.240068],[-1.409465,4.464381,-5.133099,1.131783,-7.481253,4.863004,9.883668,6.478302,7.562151,-7.338230,-6.823808,-6.499529],[7.973552,9.320204,3.273455,-8.140625,0.446622,5.385565,6.786532,1.683508,-4.015349,-4.836715,-2.831374,7.669100],[6.963508,-0.305795,5.478811,-2.405101,5.735519,8.448444,6.119642,-7.141566,-0.474284,2.624078,4.844370,2.918262],[0.098427,8.260924,9.603393,-9.391460,-9.350946,-5.095106,3.087753,3.035675,-4.667194,6.230603,-7.540585,-5.993352],[3.151917,-0.753232,4.394711,-8.481315,-7.951774,-4.769008,-5.170711,-5.077825,3.151114,-1.536647,3.206741,7.384001],[9.741649,-9.216774,8.947625,-8.919725,-5.132681,9.829452,-9.654950,-5.773823,6.204630,-5.052865,5.056084,-6.504060],[9.988809,4.217632,-4.239803,-5.382545,-6.330069,5.603290,7.865254,-0.779144,5.482552,2.511994,-3.975919,-2.718791],[1.143989,1.354023,0.421839,9.281809,8.737063,-6.541184,-4.862873,8.045661,2.603928,-4.734799,-0.607219,-1.563382],[-9.832954,7.073028,2.855779,-5.268018,-0.222510,-1.070593,4.185552,-2.103396,-9.361638,4.652981,6.961136,9.487335]],[[2.177122,3.895838,2.289803,4.484875,-1.377178,-5.600083,-7.172313,-7.457376,-9.855911,2.665030,-6.795706,-4.334031],[-7.883924,8.412548,-5.350672,-5.484950,-6.342363,2.820962,2.693492,3.576473,3.325683,4.395053,-7.372641,-4.863870],[-7.562984,5.547009,6.793752,-1.488979,5.692538,1.290263,-8.061788,8.917416,-9.566288,-2.886181,-8.926152,5.914237],[0.266669,4.800361,-5.061376,0.670864,0.202032,6.042611,-1.984955,-8.423143,-7.120597,-9.744938,3.095337,7.259442],[-4.378555,3.981705,-4.954811,4.017989,-2.512005,2.811465,-0.212093,8.398167,0.159857,4.867614,-7.811385,7.404996],[3.236779,-6.036182,-0.021696,-8.162721,3.462417,9.758251,-3.495571,-1.728901,3.229521,0.663588,-1.805933,-3.961571],[-6.484281,7.371647,5.271490,4.348969,-1.360848,-8.867293,4.965096,-4.318153,-1.759146,-6.558412,-7.701719,9.046171],[7.011781,4.467424,-8.255794,5.412489,9.372970,4.167709,-1.946931,-5.567093,-4.588728,6.842718,0.586054,2.030047],[0.470844,6.183421,-5.905922,3.084632,8.399720,3.410850,-3.108080,-6.371282,0.141275,3.962705,-7.222949,8.255487],[-6.761284,0.429884,-8.914239,8.447519,-0.170299,2.658862,-0.450588,-4.872000,5.724888,7.086990,9.783208,-8.558894],[7.014373,-9.733897,8.759906,0.109896,-1.902037,5.550881,4.381792,-0.447018,0.086857,-2.586942,-1.389550,-5.843241],[-6.486257,-6.974027,1.307522,-6.602285,-0.448999,7.421844,-4.748781,7.967929,0.707562,9.997120,0.663462,-9.578514],[6.940142,-4.621505,-9.075553,-6.265683,-2.515188,-7.278858,7.481247,4.159981,2.075760,7.103510,0.784469,-5.717429],[3.795366,6.869231,2.806039,-8.787418,-8.926435,-5.579097,9.342390,8.097899,3.696536,5.281633,-6.200127,-5.204694],[1.066356,-4.874776,-8.540470,7.133137,-3.204837,9.772316,7.583860,0.524712,-5.642045,-0.363715,-4.409990,-5.258253],[6.625897,-9.470148,-0.907655,6.798442,-8.641289,-4.534483,-5.938672,-2.717155,-0.964630,-2.225554,1.424558,9.636162]],[[5.710303,4.275664,6.678820,-6.314470,-9.636891,-9.419488,8.625509,-0.132779,5.001665,4.727486,9.452281,5.367662],[1.687029,9.526899,1.013404,-5.610250,-5.024012,-2.844802,0.779376,-8.852606,4.270857,-7.026494,-9.832700,-4.167363],[5.383570,1.521331,9.930400,-6.261690,-9.504331,-1.914908,-6.385983,-6.763950,-8.257220,-9.467088,7.922427,8.023038],[-7.476358,-7.617975,0.575261,-5.887876,-6.487773,4.369863,-9.555681,-9.512462,4.928040,-9.712807,7.131126,-6.278626],[0.323670,-9.628612,0.324835,4.639660,2.256635,-4.291653,-3.794402,-8.182446,-2.627412,3.673840,8.714580,4.602195],[-4.762391,9.469600,-9.408706,5.656977,-4.720836,6.975181,-8.556645,8.841543,-9.362674,-1.159073,2.787279,9.671274],[-1.483781,-0.643261,-1.458281,-3.284655,-0.389724,-2.330871,7.291092,-6.491317,6.152273,4.128385,6.766334,-8.923871],[-2.284264,-9.679055,3.729576,2.566661,-3.001301,5.567499,5.480887,5.800916,0.949376,-5.379308,-9.888778,3.384437],[-4.410473,7.258765,5.669472,3.047443,-8.407785,4.269599,2.811019,8.531513,2.647731,-0.729217,-0.490328,-4.723884],[-9.879631,-1.645600,1.632924,-7.046596,-6.979828,6.631322,4.993095,3.652429,7.927546,8.073328,8.677986,-1.853937],[-0.410920,3.063123,4.420270,-1.720639,-8.725378,-8.015440,-9.989672,-0.925314,-5.696134,1.082958,-4.074660,8.417471],[5.040276,6.704633,6.475128,0.473123,-6.944253,-8.786550,-3.686198,1.131134,6.500229,6.353260,3.378524,-6.475861],[6.647681,0.458129,-7.747727,5.100304,-7.146516,-5.444363,3.348842,4.865184,-0.453545,3.557721,-4.634511,6.539048],[-6.584090,-9.268306,-8.677214,4.875978,-3.278410,-0.893850,5.731846,-2.224927,-8.338916,0.851472,9.262696,6.238481],[-7.926358,-9.296023,-7.880617,-3.708317,-1.697848,-8.948217,6.747931,9.798677,-9.772459,-2.226780,7.920744,3.281987],[8.923413,8.932277,1.788902,-2.803648,5.673682,9.639385,-6.709673,-1.978881,-5.494522,-7.697499,-5.766613,5.554759]],[[7.636205,-9.948379,-8.302119,-4.711275,-9.316093,-9.030427,-3.692261,8.937506,-4.747430,8.489990,-1.528392,1.275044],[-4.777715,-7.360207,5.989754,-3.740535,6.657038,-2.646156,-6.524086,5.985587,-4.434493,6.681806,-8.954887,8.832172],[6.756682,-7.737105,-6.607513,-3.034214,1.921819,-1.839395,-3.028351,8.783531,6.527733,1.018747,-8.687410,5.060024],[7.732416,2.940707,5.326468,-7.458532,-6.251978,8.058586,-2.014700,4.041544,-1.463882,2.797715,-7.937124,4.401678],[-8.516294,-7.147982,1.738009,9.800062,-7.131373,9.014636,6.628454,-7.081544,-2.320968,2.587402,0.625280,-1.802958],[-3.928012,-0.704581,-8.020563,-7.766427,-3.458718,8.128730,-9.063350,-1.615797,8.526341,8.342779,2.036112,-7.327481],[3.027934,1.038436,6.193763,-4.424313,7.615761,-9.433729,-7.108637,-3.046022,2.368137,3.362576,-6.851493,-9.999329],[3.026415,9.012624,3.321358,-3.984891,0.757416,1.912708,2.918677,-2.401201,-0.577073,-1.407025,7.518451,-7.160763],[-6.812550,6.425066,2.385908,-2.018805,6.825201,-8.841780,-8.735631,5.392534,-4.676464,-6.286067,-8.867949,-4.158092],[2.868844,-6.860883,0.057737,-7.533595,-1.921598,-6.276973,8.622162,-9.143652,-8.466464,-7.248850,8.684501,-6.481294],[-6.699392,0.708302,0.468614,-1.500634,-8.406869,-5.119999,9.121522,9.511842,-4.714695,5.316173,-5.437398,-5.601230],[-6.140320,4.748269,-5.574796,1.736530,-3.408775,4.666578,-4.573717,7.261535,-5.504054,-0.908551,-0.830223,2.207835],[-7.573928,-9.629698,-2.090015,7.974889,3.997188,-4.208918,1.763705,8.623073,-3.784694,7.330732,-2.962993,2.479594],[-9.312290,-5.491550,4.542514,1.244057,-4.104484,2.959779,-6.212883,-6.360081,1.490440,6.619617,-3.073643,1.013539],[-6.234124,-1.389958,2.306041,0.358304,0.231566,-3.044616,-1.671346,-4.987913,8.396853,1.473589,9.466181,-9.794675],[6.811210,4.292907,-6.386742,-4.386477,5.801984,9.762526,1.676999,1.215490,-9.745332,2.080949,3.624490,2.066567]],[[4.580233,0.323768,-8.350935,-4.658659,9.473345,-4.932684,-7.543450,-5.118732,7.810345,-2.610051,9.912449,8.198624],[7.223408,-2.596466,0.452683,1.410138,-8.158216,5.196239,-2.429596,-0.835213,2.823241,9.083904,-0.660373,1.740390],[9.911061,-7.509124,8.160046,-7.745337,-0.058897,-9.942575,6.700679,9.437260,-6.570046,-5.193051,-6.961880,-7.859015],[5.650005,2.573928,-2.310223,2.591259,-6.572829,-9.728514,-2.021862,-6.843493,8.938804,-5.376014,-9.436994,-0.743224],[-8.575049,-2.874335,-6.763171,-6.856247,-0.894726,8.994393,-9.339450,8.863016,-1.837702,8.098968,-3.325407,4.222604],[-2.258816,-0.446405,2.150711,2.726955,-1.015867,-8.562128,-4.076650,-8.893179,-2.503634,7.308609,8.677311,1.390019],[-6.881321,-9.564192,-8.300749,-0.853105,5.700647,-3.811487,-4.942997,-1.954322,8.108785,9.888372,5.058023,-1.003667],[9.956389,-8.058362,-1.406001,-6.833571,-4.649789,-1.170626,-3.317941,4.983272,8.533639,1.380458,3.968456,-5.595183],[-0.988558,1.700382,-4.352806,-3.223344,5.100829,-4.809562,-4.434303,5.464694,2.205161,-2.948987,-8.966845,6.390948],[8.648185,6.057447,-3.389583,0.013342,1.903381,-5.117187,-7.410881,0.093624,0.708129,-8.950763,-6.120114,0.714621],[6.748994,-8.047066,9.895769,3.594547,-3.393173,-6.766904,6.774173,8.276706,-5.340082,-0.045583,-7.188930,-4.655208],[8.580309,-3.100583,-6.153264,3.883575,9.301847,-5.145537,5.811459,7.182578,-9.106470,-1.596693,4.349095,4.029853],[4.145653,-0.016643,3.679233,0.392366,4.430735,4.197339,6.599149,7.582382,-0.704272,-2.647787,-5.564193,0.963110],[1.022108,-9.157601,3.619346,-9.907706,7.195671,6.845336,8.180134,3.501475,-7.955830,9.465534,5.579228,-8.669018],[-6.664206,0.781508,-3.860182,4.763452,-7.640075,-2.454326,7.357719,-2.622363,0.556964,-6.083133,-4.748054,-4.449510],[-7.800143,4.639458,-4.056478,0.147153,-0.130857,0.205547,8.106680,-1.351859,-6.568847,2.962178,0.904353,-9.242203]],[[6.611613,0.319607,-8.253567,-2.642479,9.946009,-2.305650,6.945824,-8.758123,-2.727613,-4.595325,5.393774,1.611307],[0.774219,9.821436,-5.575672,-1.271398,-4.696245,-2.572789,0.307291,2.286114,-4.961271,-8.247237,7.576995,9.309707],[4.011171,3.236319,-1.119223,-7.846777,-2.215672,-2.684395,-7.527741,-1.354134,-4.802581,1.765885,-5.170506,9.867612],[9.053435,-8.461309,-9.854197,-9.463103,-1.912014,-1.421275,4.836312,-0.264248,7.616882,-1.772456,6.654684,-8.535973],[1.050628,3.094025,8.761348,-7.618611,5.707413,2.773352,-7.854565,5.204027,-8.379941,6.703847,-4.104094,4.986223],[-7.590443,3.775501,-7.323900,-0.432353,-4.827691,2.624507,-2.515135,-0.570588,3.348230,4.790100,8.359960,-0.735551],[3.226551,6.824885,8.235774,0.033700,9.370063,-9.536311,-7.484447,0.155978,-7.341445,-9.793581,3.073408,-4.609276],[2.245724,-8.245772,-5.733641,-0.237739,9.784630,-8.134015,-7.955317,-3.223990,-2.318563,1.440951,7.775267,4.349746],[-2.620119,-8.879906,-1.799173,-3.231758,8.647907,1.570502,3.371339,4.555659,4.939048,3.763603,6.896993,8.852510],[-5.931948,-1.823248,-2.238763,-9.562060,-6.399670,-7.182482,8.195709,-6.548058,8.325539,6.469931,4.408984,3.732807],[-8.334063,-5.686485,4.452369,4.620831,-5.132156,2.130853,-5.682635,9.028778,1.085133,3.629877,-2.225800,7.606927],[6.847584,-3.754375,0.036097,-7.402794,3.462670,6.413068,-7.523966,-7.818520,-0.353994,9.806907,2.023253,0.368543],[-3.525855,-3.501286,-9.336341,6.148030,-0.766894,-8.337917,9.674004,2.486960,7.082114,6.674333,2.430914,4.173049],[-0.860581,-8.923178,9.833261,-7.718113,0.378085,4.754307,-4.184403,5.565655,-7.256502,-3.406632,-5.113626,-3.457200],[-8.853490,-4.617724,-8.587049,8.842217,-9.786742,-9.569616,-8.542665,-1.160315,2.377318,6.017546,-5.077499,-3.677992],[5.420400,-0.630304,-3.388278,9.538680,2.011931,5.434450,4.451920,-1.479131,-8.855569,-8.149401,4.972554,-3.024813]],[[-7.235175,-7.287887,1.241744,5.373804,9.292479,-8.762314,3.873482,-8.780187,2.861764,-6.136124,-7.083470,6.652226],[6.831094,8.424459,-5.353794,-0.009087,-0.562676,1.785256,2.310525,-0.672211,-6.260911,3.471889,-8.095177,-9.381080],[9.669057,0.293792,6.810204,-8.168610,-6.205761,6.257191,-5.383040,1.136751,-1.846609,-3.803269,8.820488,-0.257787],[6.104292,0.795795,6.843369,-8.749553,-9.146109,4.573690,-4.475821,3.740931,9.641807,2.836616,-5.464459,-5.762980],[0.150857,-0.335071,0.110922,-7.957156,-9.441125,6.093777,-3.801897,-4.357080,9.385502,-1.901233,-8.282554,-2.070924],[2.018462,4.092086,-4.807120,-0.680657,-2.187315,-3.304078,-6.913174,-1.771649,2.448743,-3.364364,7.490057,-6.823165],[-4.934447,-9.701511,-1.702369,8.990043,-2.877387,7.972396,-3.338326,-3.704084,8.813706,6.141199,-8.608883,-7.001116],[6.042399,4.125439,-6.367354,6.033965,-5.670670,3.791572,-6.439198,-6.047106,4.252881,6.283830,-0.674679,-2.265705],[-1.498967,4.630756,8.156917,-6.540109,-0.134583,-5.049420,-8.415631,-0.675831,1.860944,4.734248,-9.841615,4.421174],[-7.695826,7.931290,-1.046458,-0.557650,7.930215,7.349280,3.925572,6.456905,4.417614,-1.084113,3.831940,1.076507],[-3.705920,-0.257344,-1.750276,-2.019970,-9.806124,6.190348,9.118914,-5.111881,6.025497,-5.404577,3.597019,2.639040],[4.492553,-8.156720,-4.769808,3.833956,1.263253,3.482187,9.588040,-3.930638,9.399298,5.042761,8.786451,-7.715134],[6.577157,6.387323,-3.274417,-8.923174,7.520538,6.835932,-6.941829,-1.312099,-5.378256,6.496222,-0.694482,-4.635562],[-5.478527,-5.130596,0.803126,-9.587520,5.910312,2.307799,-3.136268,2.399421,7.687743,8.994909,-7.359666,2.439779],[4.855460,-2.076132,-9.892186,-8.993731,-7.710655,-1.091675,4.817426,1.262672,-8.767227,-1.362447,-6.267848,-2.487216],[-0.763807,8.178733,-4.071842,-7.326735,9.404492,0.429111,7.800612,-6.620761,-7.213141,0.914570,-3.003786,0.400858]],[[8.116232,9.989143,2.959252,0.836089,-0.313266,-4.179159,6.517873,-0.956034,-0.226446,-4.965314,7.054256,9.264184],[2.022613,6.402290,6.178484,6.588142,6.363368,-3.279766,-2.487575,-0.206883,-9.362244,4.941512,6.499608,7.082837],[6.754339,6.352135,-7.292816,4.593466,2.475592,7.214929,5.645131,-2.812332,-4.583398,2.691257,-9.955272,8.303475],[5.036798,8.643518,-4.697333,-3.799385,-4.872482,8.280037,-4.967732,9.016712,5.700699,2.811499,4.135250,8.329171],[-0.408834,-4.998556,8.851079,-6.033062,4.475304,6.420681,-6.670861,3.626201,-8.145295,1.378236,3.039600,-7.384794],[-1.293780,6.795134,2.619230,7.509666,-4.629954,1.625376,7.485864,-4.373619,1.055162,-9.941813,9.164304,-7.315407],[-2.464153,-2.646903,-3.033431,3.536075,-2.262378,-7.777268,0.211861,-7.827421,-8.527222,2.998858,3.044224,-3.700450],[-5.270038,-9.188474,-0.751416,5.939228,-7.815872,6.181884,-6.729647,6.814226,4.264838,2.506126,7.556780,-9.374761],[1.730969,8.902128,4.085097,0.897105,9.788113,8.879740,-3.158504,-1.096471,2.877999,-0.773543,-1.240083,-1.566030],[5.614068,5.233101,0.186130,-9.534788,0.359764,4.575251,3.918258,-2.484050,-3.368647,1.147253,-0.222250,-0.086731],[0.481558,-8.026244,-3.970652,9.767536,-5.975210,9.770197,5.296817,-1.445861,9.993846,3.210530,-7.369933,3.630775],[-6.866965,2.868351,7.970310,-5.837638,-9.390284,-8.997888,8.994935,5.467471,-9.367346,-3.749924,-3.765975,5.174233],[-8.069938,1.473768,-5.343743,-9.567149,2.307680,-7.689572,1.806165,8.574859,0.297905,-6.384769,9.567163,-1.003086],[-4.315219,5.343233,8.027577,9.075094,-7.555983,-2.705249,9.002759,2.745601,-8.095006,1.852107,-9.781118,-6.094571],[4.090189,-8.288970,-1.135063,-6.976086,8.021153,5.863995,-2.691450,7.589886,2.650614,-7.639590,-1.580891,3.120919],[0.276756,-0.516345,1.787024,0.752720,6.731868,-6.732529,-2.530484,9.539109,-0.987630,-4.039230,3.266976,9.762604]]], dtype = "float32")#candidate|2444|(11, 16, 12)|const|float32
bop_2445 = relay.divide(var_2443.astype('float32'), relay.reshape(const_2444.astype('float32'), relay.shape_of(var_2443))) # shape=(11, 16, 12)
uop_2448 = relay.acosh(var_2443.astype('float64')) # shape=(11, 16, 12)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_2450 = func_1537_call()
call_2451 = func_1537_call()
bop_2453 = relay.mod(bop_2445.astype('float64'), relay.reshape(uop_2448.astype('float64'), relay.shape_of(bop_2445))) # shape=(11, 16, 12)
func_1076_call = mod.get_global_var('func_1076')
func_1083_call = mutated_mod.get_global_var('func_1083')
var_2457 = relay.var("var_2457", dtype = "float32", shape = (576,))#candidate|2457|(576,)|var|float32
const_2458 = relay.const([1,2,-3,-3,-3,-1,-9,-5,8,4,2,6,10,10,3,1,-3,9,-1,8,7,-2,8,7], dtype = "uint32")#candidate|2458|(24,)|const|uint32
const_2459 = relay.const([[-4,-3,1,2,-6,-5,-2,-1,-8,-8,-10,6,-9,-5,-6,-3,7,3,-7,-3,3,-8,-4,6,3,-7,-6,-1,7,-1,3,5,-9,-10,-3,-3,-1,-5,-9,9,6,5,10,-7,1,1,-2,-4,5,1,-4,-6,5,-2,-2,-8,-8,2,-8,4,-7,-3,-1,3,-8,-4,9,9,-3,10,-1,-4,9,6,5,9,5,4,-7,-10,1,9,-7,-2,1,-6,10,3,5,9,9,3,-9,10,6,-3,5,5,-2,2,10,-8,-7,-10,-10,2,6,-5,-6,1,4,-7,7,1,-10,3,-1,8,1,10,-4,3,2,5,3,-8,-9,6,-8,5,3,5,8,2,1,1,6,7,3,6,7,3,-10,2,-7,5,3,-4,5,-2,-7,2,-8,1,-1,7,10,4,8,-9,2,-5,-4,-8,6,-5,-3,-8,8,-10,6,-8,7,8,9,10,-9,-6,7,-4,-2,-6,8,5,5,6,5,8,10,-7,1,-10,-6,5,-10,6,10,8,8,-5,-1,4,6,7,-8,-5,-4,9,-3,5,5,-5,5,-2,-9,6,9,5,2,3,8,8,3,4,-4,-9,-10,4,2,-8,5,10,-6,1,-8,-7,-2,-10,4,3,5,-5,-8,2,-4,-10,6,5,4,-9,2,-9,-3,-1,5,3,8,6,-8,8,9,-3,8,9,7,4,-6,-4,-4,-7,3,-10,9,-8,6,-9,6,2,-3,3,10,9,-10,6,10,-4,1,-3,-2,7,9,-7,-9,6,-1,-2,-8,-5,-4,4,-4,6,-4,8,-9,6,-3,2,1,6,1,-2,-8,9,8,5,-4,9,-9,-4,2,-10,-2,-8,4,-6,3,4,-5,-5,-8,6,3,-10,10,5,-5,-8,-7,1,-10,6,4,-5,5,-1,2,7,-3,-8,-2,-7,-7,-5,1,10,2,5,8,-5,1,9,5,9,-4,3,1,4,-6,6,6,9,2,6,-5,2,-8,9,7,-3,6,-9,-7,9]], dtype = "uint32")#candidate|2459|(1, 384)|const|uint32
var_2460 = relay.var("var_2460", dtype = "float32", shape = (64,))#candidate|2460|(64,)|var|float32
const_2461 = relay.const([7.305590,2.542532,-2.219690,-4.109937,4.910849,9.728521,-1.133470,1.664470,-9.683649,9.133131,5.060422,1.443110,-7.262019,-8.623467,6.972544,-5.829110,-4.124609,-3.513111,-8.312205,-1.089349,-4.347236,-1.558004,0.856670,0.288133,9.409811,0.364832,9.512131,-6.045112,9.731372,6.901824,7.312820,9.773823,7.619555,-9.281776,-1.373797,8.625204,-4.418859,0.799572,1.618860,5.654424,0.071167,5.044131,2.022091,-9.161930,-5.410994,-1.326212,-2.835048,-6.499819,7.151264,6.951392,1.292237,-0.681335,-4.331338,4.209808,-2.603215,-0.813051,-6.006792,-3.720957,-1.300910,-0.906686,-7.822715,-4.798886,-8.696913,-5.270371,7.740415,6.798615,-4.585013,-3.215226,2.570611,-9.393657,-1.610290,0.539289,8.110819,-3.840607,-6.441744,-8.168901,0.795592,5.565984,5.164748,9.896948,5.211436,1.542547,2.579818,-5.763930,-3.807324,-4.142324,-4.179184,2.763390,-9.117493,9.064277,-4.462611,9.530492,-0.951921,5.015417,6.010210,-9.764113,8.226113,-5.540980,9.285943,3.946169,-0.372255,-3.090975,0.191336,-0.740366,2.661719,-8.725632,0.619490,-6.014308,9.980330,-0.131171,-3.425372,9.820661,-6.711809,-6.443352,4.895359,6.093353,-3.536590,-4.716270,2.744042,7.311526,-0.070100,-7.173695,4.349739,2.386079,-7.349443,4.773037,-9.571795,-7.134988,0.209361,-4.054224,-3.174646,-3.577121,8.671830,-4.865793,5.342486,6.260256,-9.237689,7.514875,-2.710137,-5.736504,-6.411344,-1.710517,-4.101598,-2.839262,4.681657,-0.049645,-7.137915,-5.621686,5.853650,5.037021,-9.037614,-1.830873,-8.361128,5.069312,-9.396948,-8.895755,1.924424,9.342716,0.513921,2.357558,-7.694885,3.006745,-3.370215,-6.740377,-0.369796,-6.692150,6.845320,9.945558,8.975126,-6.687346,-0.165455,-7.658088,8.606081,-4.014521,4.338121,-3.933403,9.431660,4.184758,2.401725,-3.925493,2.422236,9.028902,6.036955,-6.431519,4.484646,2.980068,2.115626,9.951872,2.680512,-1.387937,-3.877421,4.046598,-0.411958,1.224741,-4.269485,4.012056,1.855760,-9.436546,-7.312760,2.184251,-7.554831,1.110119,-6.523570,-6.587651,-7.586728,7.199298,2.923135,4.836794,0.355193,-5.217045,-5.502508,7.251844,-0.528662,-5.465688,-4.603032,-8.791839,-9.828607,8.380925,-4.831344,0.458638,-0.648588,8.885622,0.820094,0.412364,-3.674173,-4.252642,4.261616,-3.990175,-5.794865,-3.062028,-7.206701,3.829977,4.876500,9.335188,-7.344471,-7.212476,2.631487,9.182065,-7.571959,7.256444,-4.893358,8.012854,5.134413,9.787751,0.865156,5.422862,-4.630823,-8.677657,1.700144,7.996484,-4.453947,-3.575784,-9.618575,-5.670250,-5.142731,5.807716,-8.115841,-9.751350,-4.913291,8.724268,-8.186657,5.214843,9.764104,-4.041105,5.593547,-1.477477,3.642540,-9.717862,-7.966437,7.797072,-9.222721,7.982254,4.243836,8.770625,2.797599,2.197979,5.039010,-4.607319,5.886329,7.736955,9.808670,-4.538176,-9.611227,-0.770765,-9.436031,8.025582,-0.763733,2.504625,-4.119006,3.771726,2.254295,0.475125,8.571070,6.084386,-5.244895,2.415856,-5.445326,9.652111,-6.556489,-1.537599,5.329166,-4.836538,-5.465253,7.702298,-5.706698,8.594132,-5.530320,-9.032795,-0.777838,-5.616014,-2.500552,-1.316309,6.921850,9.212404,7.216692,-9.742448,3.872897,-2.661311,-6.757887,-6.901223], dtype = "float32")#candidate|2461|(320,)|const|float32
call_2456 = relay.TupleGetItem(func_1076_call(relay.reshape(var_2457.astype('float32'), [9, 16, 4]), relay.reshape(const_2458.astype('uint32'), [24,]), relay.reshape(const_2459.astype('uint32'), [384,]), relay.reshape(var_2460.astype('float32'), [64,]), relay.reshape(const_2461.astype('float32'), [320,]), relay.reshape(const_2459.astype('uint32'), [8, 16, 3]), ), 3)
call_2462 = relay.TupleGetItem(func_1083_call(relay.reshape(var_2457.astype('float32'), [9, 16, 4]), relay.reshape(const_2458.astype('uint32'), [24,]), relay.reshape(const_2459.astype('uint32'), [384,]), relay.reshape(var_2460.astype('float32'), [64,]), relay.reshape(const_2461.astype('float32'), [320,]), relay.reshape(const_2459.astype('uint32'), [8, 16, 3]), ), 3)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_2480 = relay.TupleGetItem(func_1522_call(), 1)
call_2481 = relay.TupleGetItem(func_1524_call(), 1)
uop_2496 = relay.rsqrt(uop_2448.astype('float32')) # shape=(11, 16, 12)
output = relay.Tuple([call_2450,bop_2453,call_2456,var_2457,const_2458,const_2459,var_2460,const_2461,call_2480,uop_2496,])
output2 = relay.Tuple([call_2451,bop_2453,call_2462,var_2457,const_2458,const_2459,var_2460,const_2461,call_2481,uop_2496,])
func_2501 = relay.Function([var_2443,var_2457,var_2460,], output)
mod['func_2501'] = func_2501
mod = relay.transform.InferType()(mod)
var_2502 = relay.var("var_2502", dtype = "float32", shape = (11, 16, 12))#candidate|2502|(11, 16, 12)|var|float32
var_2503 = relay.var("var_2503", dtype = "float32", shape = (576,))#candidate|2503|(576,)|var|float32
var_2504 = relay.var("var_2504", dtype = "float32", shape = (64,))#candidate|2504|(64,)|var|float32
output = func_2501(var_2502,var_2503,var_2504,)
func_2505 = relay.Function([var_2502,var_2503,var_2504,], output)
mutated_mod['func_2505'] = func_2505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_2521 = func_1537_call()
call_2522 = func_1537_call()
output = call_2521
output2 = call_2522
func_2524 = relay.Function([], output)
mod['func_2524'] = func_2524
mod = relay.transform.InferType()(mod)
output = func_2524()
func_2525 = relay.Function([], output)
mutated_mod['func_2525'] = func_2525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_2531 = func_1537_call()
call_2532 = func_1537_call()
output = relay.Tuple([call_2531,])
output2 = relay.Tuple([call_2532,])
func_2536 = relay.Function([], output)
mod['func_2536'] = func_2536
mod = relay.transform.InferType()(mod)
mutated_mod['func_2536'] = func_2536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mutated_mod.get_global_var('func_2536')
call_2537 = func_2536_call()
output = call_2537
func_2538 = relay.Function([], output)
mutated_mod['func_2538'] = func_2538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_2548 = relay.TupleGetItem(func_2536_call(), 0)
call_2549 = relay.TupleGetItem(func_2538_call(), 0)
output = call_2548
output2 = call_2549
func_2598 = relay.Function([], output)
mod['func_2598'] = func_2598
mod = relay.transform.InferType()(mod)
output = func_2598()
func_2599 = relay.Function([], output)
mutated_mod['func_2599'] = func_2599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2598_call = mod.get_global_var('func_2598')
func_2599_call = mutated_mod.get_global_var('func_2599')
call_2630 = func_2598_call()
call_2631 = func_2598_call()
uop_2636 = relay.asinh(call_2630.astype('float64')) # shape=(3, 16, 6)
uop_2638 = relay.asinh(call_2631.astype('float64')) # shape=(3, 16, 6)
func_1832_call = mod.get_global_var('func_1832')
func_1837_call = mutated_mod.get_global_var('func_1837')
var_2666 = relay.var("var_2666", dtype = "uint32", shape = (384,))#candidate|2666|(384,)|var|uint32
var_2667 = relay.var("var_2667", dtype = "float32", shape = (576,))#candidate|2667|(576,)|var|float32
const_2668 = relay.const([8.542280,9.896272,7.339389,6.315299,-5.871581,-3.336366,-9.671768,-5.907204,7.352493,7.426813,-3.295678,8.559183,4.728778,0.867237,-8.961126,-5.722223,7.633778,-6.422371,7.339000,-5.116614,2.541652,-7.136412,0.693596,8.294787,-3.867178,-3.855454,1.644849,8.461672,-5.666388,1.555586,-7.671932,-7.883193,-9.051829,-3.154152,-5.696531,9.665725,1.613078,9.455511,-2.109155,-9.961500,9.319693,8.709544,-6.420952,6.896051,3.446651,8.611123,-7.148387,6.702210,-6.119334,2.987012,-4.883373,-0.777589,-2.955850,-9.603700,3.733792,1.835151,4.596008,3.608862,-0.182985,-5.129554,-7.941017,3.225877,-4.425027,8.394593], dtype = "float32")#candidate|2668|(64,)|const|float32
var_2669 = relay.var("var_2669", dtype = "float32", shape = (320,))#candidate|2669|(320,)|var|float32
call_2665 = relay.TupleGetItem(func_1832_call(relay.reshape(var_2666.astype('uint32'), [384,]), relay.reshape(var_2667.astype('float32'), [576,]), relay.reshape(const_2668.astype('float32'), [64,]), relay.reshape(var_2669.astype('float32'), [160, 2]), ), 8)
call_2670 = relay.TupleGetItem(func_1837_call(relay.reshape(var_2666.astype('uint32'), [384,]), relay.reshape(var_2667.astype('float32'), [576,]), relay.reshape(const_2668.astype('float32'), [64,]), relay.reshape(var_2669.astype('float32'), [160, 2]), ), 8)
output = relay.Tuple([uop_2636,call_2665,var_2666,var_2667,const_2668,var_2669,])
output2 = relay.Tuple([uop_2638,call_2670,var_2666,var_2667,const_2668,var_2669,])
func_2671 = relay.Function([var_2666,var_2667,var_2669,], output)
mod['func_2671'] = func_2671
mod = relay.transform.InferType()(mod)
var_2672 = relay.var("var_2672", dtype = "uint32", shape = (384,))#candidate|2672|(384,)|var|uint32
var_2673 = relay.var("var_2673", dtype = "float32", shape = (576,))#candidate|2673|(576,)|var|float32
var_2674 = relay.var("var_2674", dtype = "float32", shape = (320,))#candidate|2674|(320,)|var|float32
output = func_2671(var_2672,var_2673,var_2674,)
func_2675 = relay.Function([var_2672,var_2673,var_2674,], output)
mutated_mod['func_2675'] = func_2675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_2681 = relay.TupleGetItem(func_2536_call(), 0)
call_2682 = relay.TupleGetItem(func_2538_call(), 0)
func_894_call = mod.get_global_var('func_894')
func_896_call = mutated_mod.get_global_var('func_896')
const_2685 = relay.const([True,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,True,False,True], dtype = "bool")#candidate|2685|(260,)|const|bool
call_2684 = relay.TupleGetItem(func_894_call(relay.reshape(const_2685.astype('bool'), [10, 2, 13])), 0)
call_2686 = relay.TupleGetItem(func_896_call(relay.reshape(const_2685.astype('bool'), [10, 2, 13])), 0)
output = relay.Tuple([call_2681,call_2684,const_2685,])
output2 = relay.Tuple([call_2682,call_2686,const_2685,])
func_2689 = relay.Function([], output)
mod['func_2689'] = func_2689
mod = relay.transform.InferType()(mod)
mutated_mod['func_2689'] = func_2689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2689_call = mutated_mod.get_global_var('func_2689')
call_2690 = func_2689_call()
output = call_2690
func_2691 = relay.Function([], output)
mutated_mod['func_2691'] = func_2691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2524_call = mod.get_global_var('func_2524')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_2731 = func_2524_call()
call_2732 = func_2524_call()
func_1076_call = mod.get_global_var('func_1076')
func_1083_call = mutated_mod.get_global_var('func_1083')
var_2746 = relay.var("var_2746", dtype = "float32", shape = (6, 96))#candidate|2746|(6, 96)|var|float32
const_2747 = relay.const([3,-5,-8,-3,-4,-6,-10,2,-7,8,10,3,6,8,-3,8,-5,-5,1,-7,-7,-9,-10,-1], dtype = "uint32")#candidate|2747|(24,)|const|uint32
const_2748 = relay.const([-5,6,10,-7,10,5,10,-5,4,2,-3,4,8,-5,1,9,-3,-5,6,1,-4,6,-8,-8,6,-6,1,-1,4,-9,5,10,-2,1,6,4,10,-3,-10,1,-1,3,6,10,-1,4,6,4,-10,-5,-8,-8,8,7,2,-2,-6,2,2,-2,10,10,2,1,-10,-10,-5,9,2,1,-5,-7,-9,-4,1,-3,4,7,9,1,6,10,-2,7,4,-5,1,3,-1,1,3,-6,-9,-4,-3,-10,8,2,-10,1,-9,4,-8,-1,3,4,-8,-4,3,9,-5,-7,-10,1,10,-3,-8,-10,-3,-9,3,-2,-4,-9,-6,-3,9,4,-10,9,-8,-8,1,-7,9,1,-9,-2,-1,8,-1,-2,2,10,-2,-2,3,-7,8,-7,9,-8,4,1,-2,7,-1,-2,3,-5,-2,5,6,8,-7,-2,4,5,9,5,5,5,-9,1,10,8,2,5,-9,-4,9,-5,6,-3,5,8,-10,-10,-9,-2,6,1,7,-7,-1,3,9,-3,7,1,5,-6,10,5,-6,10,-1,1,7,4,-1,7,4,-6,-7,-7,-6,-9,-8,8,5,7,9,6,7,3,9,-9,-10,-6,-2,1,-3,-6,9,6,-4,-2,2,-8,-9,1,10,9,-5,-7,5,8,-8,-10,10,1,-8,8,2,-2,-8,-7,3,8,-10,-6,3,-4,8,-10,-1,-6,-5,-10,4,-5,5,3,-7,-5,-8,-3,-4,-3,-2,-5,-3,1,-5,4,3,4,-9,-3,7,-5,-8,5,-5,8,-3,-10,2,-4,-2,-10,8,-2,-8,5,-2,2,9,6,8,-1,7,-9,3,-7,4,8,1,8,5,-7,-6,-1,-6,8,2,-5,3,7,-7,-10,4,-2,-8,-4,-8,3,8,8,2,-8,-9,1,-8,9,5,-8,-7,-1,3,-9,-6,4,8,-8,1,-7,8,4,8,-1,1,1,-10,-3,8,5,-6,-8,2,-7,1,-3,1,6,9,2,9,-9,6,3,6,9], dtype = "uint32")#candidate|2748|(384,)|const|uint32
var_2749 = relay.var("var_2749", dtype = "float32", shape = (64,))#candidate|2749|(64,)|var|float32
var_2750 = relay.var("var_2750", dtype = "float32", shape = (320,))#candidate|2750|(320,)|var|float32
call_2745 = relay.TupleGetItem(func_1076_call(relay.reshape(var_2746.astype('float32'), [9, 16, 4]), relay.reshape(const_2747.astype('uint32'), [24,]), relay.reshape(const_2748.astype('uint32'), [384,]), relay.reshape(var_2749.astype('float32'), [64,]), relay.reshape(var_2750.astype('float32'), [320,]), relay.reshape(const_2748.astype('uint32'), [8, 16, 3]), ), 3)
call_2751 = relay.TupleGetItem(func_1083_call(relay.reshape(var_2746.astype('float32'), [9, 16, 4]), relay.reshape(const_2747.astype('uint32'), [24,]), relay.reshape(const_2748.astype('uint32'), [384,]), relay.reshape(var_2749.astype('float32'), [64,]), relay.reshape(var_2750.astype('float32'), [320,]), relay.reshape(const_2748.astype('uint32'), [8, 16, 3]), ), 3)
output = relay.Tuple([call_2731,call_2745,var_2746,const_2747,const_2748,var_2749,var_2750,])
output2 = relay.Tuple([call_2732,call_2751,var_2746,const_2747,const_2748,var_2749,var_2750,])
func_2753 = relay.Function([var_2746,var_2749,var_2750,], output)
mod['func_2753'] = func_2753
mod = relay.transform.InferType()(mod)
mutated_mod['func_2753'] = func_2753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2753_call = mutated_mod.get_global_var('func_2753')
var_2755 = relay.var("var_2755", dtype = "float32", shape = (6, 96))#candidate|2755|(6, 96)|var|float32
var_2756 = relay.var("var_2756", dtype = "float32", shape = (64,))#candidate|2756|(64,)|var|float32
var_2757 = relay.var("var_2757", dtype = "float32", shape = (320,))#candidate|2757|(320,)|var|float32
call_2754 = func_2753_call(var_2755,var_2756,var_2757,)
output = call_2754
func_2758 = relay.Function([var_2755,var_2756,var_2757,], output)
mutated_mod['func_2758'] = func_2758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2524_call = mod.get_global_var('func_2524')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_2787 = func_2524_call()
call_2788 = func_2524_call()
output = relay.Tuple([call_2787,])
output2 = relay.Tuple([call_2788,])
func_2822 = relay.Function([], output)
mod['func_2822'] = func_2822
mod = relay.transform.InferType()(mod)
mutated_mod['func_2822'] = func_2822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2822_call = mutated_mod.get_global_var('func_2822')
call_2823 = func_2822_call()
output = call_2823
func_2824 = relay.Function([], output)
mutated_mod['func_2824'] = func_2824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2822_call = mod.get_global_var('func_2822')
func_2824_call = mutated_mod.get_global_var('func_2824')
call_2902 = relay.TupleGetItem(func_2822_call(), 0)
call_2903 = relay.TupleGetItem(func_2824_call(), 0)
var_2907 = relay.var("var_2907", dtype = "bool", shape = (3, 16, 6))#candidate|2907|(3, 16, 6)|var|bool
bop_2908 = relay.floor_divide(call_2902.astype('float64'), relay.reshape(var_2907.astype('float64'), relay.shape_of(call_2902))) # shape=(3, 16, 6)
bop_2911 = relay.floor_divide(call_2903.astype('float64'), relay.reshape(var_2907.astype('float64'), relay.shape_of(call_2903))) # shape=(3, 16, 6)
output = relay.Tuple([bop_2908,])
output2 = relay.Tuple([bop_2911,])
func_2912 = relay.Function([var_2907,], output)
mod['func_2912'] = func_2912
mod = relay.transform.InferType()(mod)
var_2913 = relay.var("var_2913", dtype = "bool", shape = (3, 16, 6))#candidate|2913|(3, 16, 6)|var|bool
output = func_2912(var_2913)
func_2914 = relay.Function([var_2913], output)
mutated_mod['func_2914'] = func_2914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2524_call = mod.get_global_var('func_2524')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_2960 = func_2524_call()
call_2961 = func_2524_call()
var_2966 = relay.var("var_2966", dtype = "bool", shape = (3, 16, 6))#candidate|2966|(3, 16, 6)|var|bool
bop_2967 = relay.equal(call_2960.astype('bool'), relay.reshape(var_2966.astype('bool'), relay.shape_of(call_2960))) # shape=(3, 16, 6)
bop_2970 = relay.equal(call_2961.astype('bool'), relay.reshape(var_2966.astype('bool'), relay.shape_of(call_2961))) # shape=(3, 16, 6)
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_2975 = relay.TupleGetItem(func_2536_call(), 0)
call_2976 = relay.TupleGetItem(func_2538_call(), 0)
output = relay.Tuple([bop_2967,call_2975,])
output2 = relay.Tuple([bop_2970,call_2976,])
func_2979 = relay.Function([var_2966,], output)
mod['func_2979'] = func_2979
mod = relay.transform.InferType()(mod)
var_2980 = relay.var("var_2980", dtype = "bool", shape = (3, 16, 6))#candidate|2980|(3, 16, 6)|var|bool
output = func_2979(var_2980)
func_2981 = relay.Function([var_2980], output)
mutated_mod['func_2981'] = func_2981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2598_call = mod.get_global_var('func_2598')
func_2599_call = mutated_mod.get_global_var('func_2599')
call_3123 = func_2598_call()
call_3124 = func_2598_call()
output = call_3123
output2 = call_3124
func_3144 = relay.Function([], output)
mod['func_3144'] = func_3144
mod = relay.transform.InferType()(mod)
mutated_mod['func_3144'] = func_3144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3144_call = mutated_mod.get_global_var('func_3144')
call_3145 = func_3144_call()
output = call_3145
func_3146 = relay.Function([], output)
mutated_mod['func_3146'] = func_3146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3144_call = mod.get_global_var('func_3144')
func_3146_call = mutated_mod.get_global_var('func_3146')
call_3152 = func_3144_call()
call_3153 = func_3144_call()
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_3155 = relay.TupleGetItem(func_1522_call(), 1)
call_3156 = relay.TupleGetItem(func_1524_call(), 1)
uop_3165 = relay.exp(call_3152.astype('float32')) # shape=(3, 16, 6)
uop_3167 = relay.exp(call_3153.astype('float32')) # shape=(3, 16, 6)
func_2912_call = mod.get_global_var('func_2912')
func_2914_call = mutated_mod.get_global_var('func_2914')
call_3173 = relay.TupleGetItem(func_2912_call(relay.reshape(call_3152.astype('bool'), [3, 16, 6])), 0)
call_3174 = relay.TupleGetItem(func_2914_call(relay.reshape(call_3152.astype('bool'), [3, 16, 6])), 0)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_3178 = func_2428_call()
call_3179 = func_2428_call()
output = relay.Tuple([call_3155,uop_3165,call_3173,call_3178,])
output2 = relay.Tuple([call_3156,uop_3167,call_3174,call_3179,])
func_3198 = relay.Function([], output)
mod['func_3198'] = func_3198
mod = relay.transform.InferType()(mod)
output = func_3198()
func_3199 = relay.Function([], output)
mutated_mod['func_3199'] = func_3199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2689_call = mod.get_global_var('func_2689')
func_2691_call = mutated_mod.get_global_var('func_2691')
call_3200 = relay.TupleGetItem(func_2689_call(), 1)
call_3201 = relay.TupleGetItem(func_2691_call(), 1)
output = relay.Tuple([call_3200,])
output2 = relay.Tuple([call_3201,])
func_3234 = relay.Function([], output)
mod['func_3234'] = func_3234
mod = relay.transform.InferType()(mod)
output = func_3234()
func_3235 = relay.Function([], output)
mutated_mod['func_3235'] = func_3235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3144_call = mod.get_global_var('func_3144')
func_3146_call = mutated_mod.get_global_var('func_3146')
call_3285 = func_3144_call()
call_3286 = func_3144_call()
func_3144_call = mod.get_global_var('func_3144')
func_3146_call = mutated_mod.get_global_var('func_3146')
call_3291 = func_3144_call()
call_3292 = func_3144_call()
func_1724_call = mod.get_global_var('func_1724')
func_1728_call = mutated_mod.get_global_var('func_1728')
var_3295 = relay.var("var_3295", dtype = "uint32", shape = (384,))#candidate|3295|(384,)|var|uint32
const_3296 = relay.const([[3.815811,7.762110,-8.688426,3.073005,6.922034,5.636111,-9.580379,1.905632,1.564493,7.388942,-0.783264,1.634474,-7.891195,1.341920,6.171324,4.102646,-8.289907,-5.104089,-9.511528,-9.282260,2.087787,4.455832,6.137482,8.036270,-0.658476,5.570512,-4.358705,1.900170,-9.158182,-3.344928,0.712131,-7.896673,-2.490037,-2.349657,-0.686814,-0.047020,-5.133205,8.568619,7.485997,-0.745805,-5.533204,-4.523803,1.794069,2.158259,-3.212586,2.463698,8.108461,-3.815828,-9.526140,-2.583352,2.181850,-0.830958,-8.443163,-4.236268,-3.352101,-9.485594,-8.835655,0.851949,-0.489377,8.967381,-4.677824,-3.200157,9.084077,0.626385]], dtype = "float32")#candidate|3296|(1, 64)|const|float32
const_3297 = relay.const([1.258216,2.268824,6.378856,8.494138,-1.220951,-1.178723,-0.253643,-3.510342,-3.065846,-0.418735,-9.493844,7.782392,6.485812,1.019969,-3.975921,3.454041,-5.603527,-3.492554,-4.621569,2.054158,5.728524,-9.770042,-8.513313,-3.217044,-8.649313,0.553579,6.472582,-7.759455,-7.588247,1.297840,-5.366658,-7.285902,0.885400,-0.745077,-4.316480,2.012715,9.099554,6.830765,-6.735798,-8.058626,-9.056144,-0.862239,-0.590784,-4.249668,-5.686950,-8.698405,8.250566,-1.287543,2.620126,-5.709416,-1.805974,3.033437,7.767098,0.874317,-7.372293,7.462836,-9.469328,-2.151651,-5.039010,6.466758,-4.808726,8.900795,-9.042247,6.283957,-4.083231,7.360492,9.657802,-7.548762,0.810711,-0.170867,-0.349251,8.868385,3.973630,1.807465,-1.260207,2.284486,-2.316379,-0.972675,-2.489344,-7.495976,-9.101443,7.090243,-0.688105,-3.292090,-4.646794,7.076358,-7.831197,4.213456,-6.191779,-6.982619,9.080579,-5.133779,-3.521025,-1.043803,-6.993709,-6.946873,-7.528106,-6.068848,6.916714,-0.928086,3.736281,-2.180326,-3.124414,-4.494954,7.715948,-4.332611,-3.398888,-2.812048,1.635919,5.410316,-1.984075,-0.559657,8.612452,8.548588,-3.941936,-3.828777,-3.298570,0.753831,-9.380419,5.934459,-0.828628,-4.331771,-2.431185,-3.063193,9.106411,8.714899,6.283060,-2.755683,-0.158011,1.657921,-2.688186,6.412054,0.173443,2.789312,-8.717478,4.430379,-8.527109,3.262362,-6.659207,4.283016,9.913019,6.264245,-8.337676,2.100504,-2.591326,5.997611,2.317192,8.900560,-4.911022,-6.644105,9.304800,0.745916,-0.623995,0.442450,-8.666953,-3.713629,2.616549,-5.975668,-5.079923,9.881269,8.630257,5.892556,5.745035,0.927273,3.430389,-2.931583,9.226866,9.721294,-0.460021,-3.127411,2.060226,-5.164233,4.843457,-6.002975,-3.555520,-3.752760,0.918650,-5.759926,-7.253249,-1.493960,-0.352485,-3.740967,-2.845611,8.377426,-1.176758,-6.790597,-6.059847,7.452890,2.941879,1.770364,4.495288,8.547129,2.590145,8.810449,7.696957,-6.968917,-6.097378,0.685676,-3.422254,5.219109,4.210313,-3.532480,-4.858934,2.882578,8.287497,6.199131,-7.109203,8.835359,1.135034,5.304052,-3.728220,-9.502261,-9.708218,-1.882010,-0.859529,-9.109865,0.707251,3.441110,-7.741551,9.397194,-3.551271,-8.040463,-7.466084,-5.490739,-5.707481,-2.442704,1.621814,9.526073,0.070604,-5.633645,4.056327,6.375431,1.975396,-2.082992,1.814970,-4.446738,-6.461353,-0.713290,-5.849035,-1.141405,-1.303246,-9.914749,1.001722,9.305015,8.377419,-3.159067,-2.731547,0.246861,4.930680,8.332329,4.255997,-5.204724,-0.846163,-2.199188,0.603402,8.221067,-8.074733,-7.712949,1.843636,-0.507327,7.633689,1.429189,-6.635200,-2.197200,-8.127977,-7.024387,6.548061,-9.388268,7.312062,-5.445743,6.000540,-4.792460,3.946715,-0.213911,-3.698176,8.452495,0.594221,-2.753381,7.122526,9.140432,-3.858854,-6.571112,-7.556137,-3.841653,4.087187,6.126422,-7.213581,-6.606487,-2.554523,4.168552,3.907044,-3.013045,9.422671,-2.196423,6.779188,9.704073,7.923920,1.212669,-2.603631,2.999277,8.960445,-1.194617,-8.299651,0.475629,0.390176,-1.847304,-0.666093,-2.816007,1.918396,-3.969195,-2.015813,-7.302677,9.783345,-2.572286,6.510317,-6.613495,-5.551843,9.348421,6.637096,0.557200], dtype = "float32")#candidate|3297|(320,)|const|float32
call_3294 = relay.TupleGetItem(func_1724_call(relay.reshape(var_3295.astype('uint32'), [384,]), relay.reshape(const_3296.astype('float32'), [64,]), relay.reshape(const_3297.astype('float32'), [80, 4]), ), 6)
call_3298 = relay.TupleGetItem(func_1728_call(relay.reshape(var_3295.astype('uint32'), [384,]), relay.reshape(const_3296.astype('float32'), [64,]), relay.reshape(const_3297.astype('float32'), [80, 4]), ), 6)
func_1901_call = mod.get_global_var('func_1901')
func_1903_call = mutated_mod.get_global_var('func_1903')
const_3304 = relay.const([7.193501,-1.564543,4.891073,-5.178168,7.710438,6.288304,-8.689699,4.726636,5.979555,6.668468,-4.243395,1.066890,-1.923134,-2.397081,-2.974115,6.231735,3.323352,6.905485,-9.147801,4.742413,-6.103237,6.425990,-9.812342,-4.139454,7.545099,-3.519253,-2.739953,0.349293,-8.015621,-7.951952,5.448684,-3.208985,3.064521,4.965999,1.896346,9.808109,3.728404,-7.867135,2.666517,2.547162,4.374507,6.569816,3.809142,-0.341649,-9.380928,-4.827093,-0.857113,-9.091666,8.945038,8.827423,5.674503,-6.831516,-9.008242,-0.332749,8.841511,-5.411004,-2.032122,8.595848,9.916118,7.848988,-6.414216,7.547948,-6.765383,9.600166,6.714054,-4.041244,2.193238,9.736146,8.693637,-6.992828,5.922097,5.643640,-3.609564,3.513695,-0.842338,8.999120,3.774925,2.127568,6.856085,9.978911,-8.456318,1.066248,-5.396060,8.359320,-4.463594,2.118355,-2.564501,0.138509,6.423516,-2.691073,6.971515,-4.493631,-3.084621,-8.417330,-4.418806,-0.455620,4.484000,3.309000,-1.090755,-7.392135,-3.826248,-3.924611,-5.884329,1.336706,6.899273,-6.672280,4.731294,5.178132,-6.053539,1.459559,5.460258,8.391757,8.780760,-9.198848,0.417008,5.296483,-2.762593,3.837911,0.089578,-3.597784,-1.377481,-8.110713,-5.965079,-2.474761,1.386115,8.462523,5.574334,-9.616091,9.109402,9.350182,6.621416,-7.341302,-4.216204,-4.697305,-5.951049,-9.099054,4.035083,1.446474,-4.188951,2.363540,5.945110,-8.538243,6.196921,-6.460527,-0.838771,-7.629380,-2.513171,0.915720,-3.991794,-0.038004,9.253889,1.418645,1.296234,-0.118816,-6.547537,-0.181330,-4.179964,9.168532,6.520308,4.226936], dtype = "float64")#candidate|3304|(160,)|const|float64
call_3303 = relay.TupleGetItem(func_1901_call(relay.reshape(const_3304.astype('float64'), [10, 2, 8])), 0)
call_3305 = relay.TupleGetItem(func_1903_call(relay.reshape(const_3304.astype('float64'), [10, 2, 8])), 0)
func_3198_call = mod.get_global_var('func_3198')
func_3199_call = mutated_mod.get_global_var('func_3199')
call_3306 = relay.TupleGetItem(func_3198_call(), 1)
call_3307 = relay.TupleGetItem(func_3199_call(), 1)
output = relay.Tuple([call_3285,call_3291,call_3294,var_3295,const_3296,const_3297,call_3303,const_3304,call_3306,])
output2 = relay.Tuple([call_3286,call_3292,call_3298,var_3295,const_3296,const_3297,call_3305,const_3304,call_3307,])
func_3315 = relay.Function([var_3295,], output)
mod['func_3315'] = func_3315
mod = relay.transform.InferType()(mod)
mutated_mod['func_3315'] = func_3315
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3316 = relay.var("var_3316", dtype = "uint32", shape = (384,))#candidate|3316|(384,)|var|uint32
func_3315_call = mutated_mod.get_global_var('func_3315')
call_3317 = func_3315_call(var_3316)
output = call_3317
func_3318 = relay.Function([var_3316], output)
mutated_mod['func_3318'] = func_3318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_3359 = relay.TupleGetItem(func_1522_call(), 0)
call_3360 = relay.TupleGetItem(func_1524_call(), 0)
output = call_3359
output2 = call_3360
func_3370 = relay.Function([], output)
mod['func_3370'] = func_3370
mod = relay.transform.InferType()(mod)
mutated_mod['func_3370'] = func_3370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3370_call = mutated_mod.get_global_var('func_3370')
call_3371 = func_3370_call()
output = call_3371
func_3372 = relay.Function([], output)
mutated_mod['func_3372'] = func_3372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_3413 = relay.TupleGetItem(func_1522_call(), 0)
call_3414 = relay.TupleGetItem(func_1524_call(), 0)
uop_3420 = relay.cosh(call_3413.astype('float64')) # shape=(3, 16, 6)
uop_3422 = relay.cosh(call_3414.astype('float64')) # shape=(3, 16, 6)
func_1867_call = mod.get_global_var('func_1867')
func_1869_call = mutated_mod.get_global_var('func_1869')
const_3438 = relay.const([7,-5,-10,-6,7,-9,8,-3,-2,10,-9,1,2,8,-6,-1,3,-8,4,-6,-5,5,-8,4,5,-2,-1,-8,-8,2,-5,9,-10,3,-10,-6,3,10,-10,-1,-6,-1,7,2,8,-9,9,-3,4,5,-4,-1,-10,8,5,5,2,10,7,-3,6,-10,-10,5,10,10,-1,-10,-1,-1,8,8,3,-7,8,5,-4,2,-9,-1,-7,4,-9,-10,-5,-7,-6,4,10,10,-3,-3,-10,-4,4,-10,6,10,10,-6,-1,-9,5,-6,5,5,1,-7,-5,-1,-8,-9,-7,-10,8,-4,-8,-6,6,-1,8,-1,4,-9,10,-7,3,3,-6,8,8,3], dtype = "int16")#candidate|3438|(132,)|const|int16
call_3437 = relay.TupleGetItem(func_1867_call(relay.reshape(const_3438.astype('int16'), [11, 4, 3])), 0)
call_3439 = relay.TupleGetItem(func_1869_call(relay.reshape(const_3438.astype('int16'), [11, 4, 3])), 0)
uop_3455 = relay.atan(const_3438.astype('float32')) # shape=(132,)
output = relay.Tuple([uop_3420,call_3437,uop_3455,])
output2 = relay.Tuple([uop_3422,call_3439,uop_3455,])
func_3461 = relay.Function([], output)
mod['func_3461'] = func_3461
mod = relay.transform.InferType()(mod)
mutated_mod['func_3461'] = func_3461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3461_call = mutated_mod.get_global_var('func_3461')
call_3462 = func_3461_call()
output = call_3462
func_3463 = relay.Function([], output)
mutated_mod['func_3463'] = func_3463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_3479 = func_1537_call()
call_3480 = func_1537_call()
func_327_call = mod.get_global_var('func_327')
func_331_call = mutated_mod.get_global_var('func_331')
const_3482 = relay.const([[9,-7,-3,6,-9,3,-9,5,1,4,-10,4,9,-3,-5,-1,-2,-1,9,10,-8,-10,-8,-2]], dtype = "uint32")#candidate|3482|(1, 24)|const|uint32
const_3483 = relay.const([-4,-10,6,-4,4,-2,2,-5,-1,-2,2,4,8,9,8,-8,10,1,-7,-5,-4,8,-2,-1,-9,2,5,-5,7,-3,-3,-9,8,1,5,-8,4,7,1,7,-2,-1,-6,-10,-10,1,-5,-10,-10,-10,-8,6,-6,-8,-10,7,5,-9,-4,-5,3,10,6,-10,-3,-3,-9,-5,-3,-2,-7,7,6,-2,-8,-5,-4,-8,4,-9,10,-10,-5,6,5,3,8,3,-9,-2,-3,-7,-3,9,6,-4,2,-7,-10,-6,-2,6,-10,-4,5,7,5,7,10,-5,6,3,5,6,5,-10,-3,-7,-7,-4,-6,-2,-5,-9,5,-3,3,-10,8,-4,9,1,2,5,-10,-4,1,9,5,3,10,-2,2,3,-9,4,-3,-10,-3,-6,5,9,-8,-4,-4,2,2,1,7,3,-3,5,-2,-10,-3,7,-8,6,5,-8,6,7,7,2,-1,3,-2,9,5,-10,-8,6,3,4,1,-1,6,-3,-5,9,9,-2,-10,6,10,4,3,6,4,-6,-5,-4,-4,-4,-1,6,2,-5,-7,-8,7,7,-3,-5,-6,-6,7,-10,6,-1,4,10,-3,8,6,-1,9,-2,-2,3,-8,-8,8,8,-1,-2,-6,5,-7,-1,1,5,-9,-2,4,10,-4,-8,6,8,-5,-6,-3,10,4,-5,3,-2,-7,-5,2,2,2,10,-6,-7,9,1,2,5,5,8,-10,-10,7,-7,-1,-6,-8,10,5,4,9,-7,1,7,-2,1,5,8,-9,10,-3,-2,3,5,-9,1,6,-9,1,-2,10,6,7,9,10,-5,-8,-6,-8,8,-9,3,8,-4,-1,4,10,-9,8,2,-1,-3,-5,-9,-7,8,7,-3,7,-6,4,10,-1,-10,8,7,10,-8,8,-5,4,2,7,6,5,-10,3,-10,8,-5,1,-8,1,-5,3,5,5,7,-3,4,7,6,6,4,5,2,1,-6,-6,-3,-10,4,-6,-7,-6,-6,9,-2,-7,8,-6,-7], dtype = "uint32")#candidate|3483|(384,)|const|uint32
call_3481 = func_327_call(relay.reshape(const_3482.astype('uint32'), [8, 1, 3]), relay.reshape(const_3483.astype('uint32'), [8, 16, 3]), )
call_3484 = func_327_call(relay.reshape(const_3482.astype('uint32'), [8, 1, 3]), relay.reshape(const_3483.astype('uint32'), [8, 16, 3]), )
func_2261_call = mod.get_global_var('func_2261')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_3486 = relay.TupleGetItem(func_2261_call(relay.reshape(call_3479.astype('float64'), [3, 16, 6])), 0)
call_3487 = relay.TupleGetItem(func_2264_call(relay.reshape(call_3479.astype('float64'), [3, 16, 6])), 0)
func_2261_call = mod.get_global_var('func_2261')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_3488 = relay.TupleGetItem(func_2261_call(relay.reshape(call_3479.astype('float64'), [3, 16, 6])), 1)
call_3489 = relay.TupleGetItem(func_2264_call(relay.reshape(call_3479.astype('float64'), [3, 16, 6])), 1)
func_1901_call = mod.get_global_var('func_1901')
func_1903_call = mutated_mod.get_global_var('func_1903')
const_3496 = relay.const([[8.688413,-3.430317,1.140432,-6.142318,4.050015,3.083471,5.056369,-7.210406,0.576084,-9.494818,9.703428,1.842264,9.262853,-8.467115,-9.525531,-0.596952,-6.569837,9.375561,-1.713203,-2.381392,-1.860610,-0.875416,-0.700329,3.730007,-8.746764,9.719756,3.196013,1.165168,-5.446649,7.427829,-5.321980,-1.911775,-5.065540,-7.295184,-5.112334,4.420455,-7.438007,-9.346467,-5.837998,7.537103,-6.195074,-4.366895,5.667599,-0.969078,7.201867,5.597660,-1.898023,-8.190037,3.360108,8.131490,-0.880102,-1.774068,1.895977,5.914072,-4.952657,-2.926823,9.319958,-5.885345,-6.093304,-2.248957,-5.636515,2.804152,-1.368095,-6.975922,-8.590286,5.500550,-9.823369,-4.685555,-0.214478,5.998573,-8.231818,4.028831,-4.826570,-1.110931,0.078462,1.877365,-3.002050,-8.900714,-9.613862,-5.037835,-8.266461,5.672070,6.451283,-4.753805,2.262361,-8.170327,4.406131,-3.298822,-8.370648,-2.035810,0.147056,7.076516,-0.102787,-4.944067,-9.558971,-7.713316,-3.246894,3.626714,1.923767,-2.743372,1.551025,-4.829547,-0.336521,2.410426,5.335679,-1.436956,3.837904,8.196114,2.073873,-7.590826,-1.441912,9.201605,2.226492,2.002101,-2.944080,8.771050,-4.495519,4.696987,-3.749114,7.951362,-9.758878,3.395042,-9.686599,-0.287305,-5.238298,4.646887,0.500429,-2.979042,-5.378917,6.591809,2.362112,-3.585542,-7.138721,-3.998272,-5.936329,-3.307879,-7.547007,-9.030090,-9.041955,-5.571034,-1.382118,-1.184652,-1.344258,-8.743153,-8.070098,-3.389870,-5.358299,8.411097,-8.489852,-4.314575,-1.590241,5.477935,-6.076598,6.699755,-8.334602,3.478001,9.743959,-2.501634,-5.174038,-9.512521]], dtype = "float64")#candidate|3496|(1, 160)|const|float64
call_3495 = relay.TupleGetItem(func_1901_call(relay.reshape(const_3496.astype('float64'), [10, 2, 8])), 0)
call_3497 = relay.TupleGetItem(func_1903_call(relay.reshape(const_3496.astype('float64'), [10, 2, 8])), 0)
output = relay.Tuple([call_3479,call_3481,const_3482,const_3483,call_3486,call_3488,call_3495,const_3496,])
output2 = relay.Tuple([call_3480,call_3484,const_3482,const_3483,call_3487,call_3489,call_3497,const_3496,])
func_3507 = relay.Function([], output)
mod['func_3507'] = func_3507
mod = relay.transform.InferType()(mod)
mutated_mod['func_3507'] = func_3507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mutated_mod.get_global_var('func_3507')
call_3508 = func_3507_call()
output = call_3508
func_3509 = relay.Function([], output)
mutated_mod['func_3509'] = func_3509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3198_call = mod.get_global_var('func_3198')
func_3199_call = mutated_mod.get_global_var('func_3199')
call_3533 = relay.TupleGetItem(func_3198_call(), 1)
call_3534 = relay.TupleGetItem(func_3199_call(), 1)
func_2524_call = mod.get_global_var('func_2524')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_3537 = func_2524_call()
call_3538 = func_2524_call()
output = relay.Tuple([call_3533,call_3537,])
output2 = relay.Tuple([call_3534,call_3538,])
func_3542 = relay.Function([], output)
mod['func_3542'] = func_3542
mod = relay.transform.InferType()(mod)
output = func_3542()
func_3543 = relay.Function([], output)
mutated_mod['func_3543'] = func_3543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_3697 = relay.TupleGetItem(func_1522_call(), 0)
call_3698 = relay.TupleGetItem(func_1524_call(), 0)
output = relay.Tuple([call_3697,])
output2 = relay.Tuple([call_3698,])
func_3725 = relay.Function([], output)
mod['func_3725'] = func_3725
mod = relay.transform.InferType()(mod)
output = func_3725()
func_3726 = relay.Function([], output)
mutated_mod['func_3726'] = func_3726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2524_call = mod.get_global_var('func_2524')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_3757 = func_2524_call()
call_3758 = func_2524_call()
func_2524_call = mod.get_global_var('func_2524')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_3775 = func_2524_call()
call_3776 = func_2524_call()
var_3779 = relay.var("var_3779", dtype = "bool", shape = (3, 16, 6))#candidate|3779|(3, 16, 6)|var|bool
bop_3780 = relay.right_shift(call_3757.astype('uint8'), relay.reshape(var_3779.astype('uint8'), relay.shape_of(call_3757))) # shape=(3, 16, 6)
bop_3783 = relay.right_shift(call_3758.astype('uint8'), relay.reshape(var_3779.astype('uint8'), relay.shape_of(call_3758))) # shape=(3, 16, 6)
func_3198_call = mod.get_global_var('func_3198')
func_3199_call = mutated_mod.get_global_var('func_3199')
call_3791 = relay.TupleGetItem(func_3198_call(), 1)
call_3792 = relay.TupleGetItem(func_3199_call(), 1)
uop_3796 = relay.log10(call_3775.astype('float32')) # shape=(3, 16, 6)
uop_3798 = relay.log10(call_3776.astype('float32')) # shape=(3, 16, 6)
output = relay.Tuple([bop_3780,call_3791,uop_3796,])
output2 = relay.Tuple([bop_3783,call_3792,uop_3798,])
func_3802 = relay.Function([var_3779,], output)
mod['func_3802'] = func_3802
mod = relay.transform.InferType()(mod)
mutated_mod['func_3802'] = func_3802
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3803 = relay.var("var_3803", dtype = "bool", shape = (3, 16, 6))#candidate|3803|(3, 16, 6)|var|bool
func_3802_call = mutated_mod.get_global_var('func_3802')
call_3804 = func_3802_call(var_3803)
output = call_3804
func_3805 = relay.Function([var_3803], output)
mutated_mod['func_3805'] = func_3805
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3826 = relay.var("var_3826", dtype = "float32", shape = (11, 9, 15))#candidate|3826|(11, 9, 15)|var|float32
uop_3827 = relay.exp(var_3826.astype('float32')) # shape=(11, 9, 15)
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_3834 = relay.TupleGetItem(func_2536_call(), 0)
call_3835 = relay.TupleGetItem(func_2538_call(), 0)
output = relay.Tuple([uop_3827,call_3834,])
output2 = relay.Tuple([uop_3827,call_3835,])
func_3839 = relay.Function([var_3826,], output)
mod['func_3839'] = func_3839
mod = relay.transform.InferType()(mod)
mutated_mod['func_3839'] = func_3839
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3840 = relay.var("var_3840", dtype = "float32", shape = (11, 9, 15))#candidate|3840|(11, 9, 15)|var|float32
func_3839_call = mutated_mod.get_global_var('func_3839')
call_3841 = func_3839_call(var_3840)
output = call_3841
func_3842 = relay.Function([var_3840], output)
mutated_mod['func_3842'] = func_3842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_3850 = func_1537_call()
call_3851 = func_1537_call()
var_3870 = relay.var("var_3870", dtype = "bool", shape = (3, 16, 6))#candidate|3870|(3, 16, 6)|var|bool
bop_3871 = relay.multiply(call_3850.astype('float32'), relay.reshape(var_3870.astype('float32'), relay.shape_of(call_3850))) # shape=(3, 16, 6)
bop_3874 = relay.multiply(call_3851.astype('float32'), relay.reshape(var_3870.astype('float32'), relay.shape_of(call_3851))) # shape=(3, 16, 6)
func_3839_call = mod.get_global_var('func_3839')
func_3842_call = mutated_mod.get_global_var('func_3842')
var_3887 = relay.var("var_3887", dtype = "float32", shape = (1485,))#candidate|3887|(1485,)|var|float32
call_3886 = relay.TupleGetItem(func_3839_call(relay.reshape(var_3887.astype('float32'), [11, 9, 15])), 1)
call_3888 = relay.TupleGetItem(func_3842_call(relay.reshape(var_3887.astype('float32'), [11, 9, 15])), 1)
output = relay.Tuple([bop_3871,call_3886,var_3887,])
output2 = relay.Tuple([bop_3874,call_3888,var_3887,])
func_3892 = relay.Function([var_3870,var_3887,], output)
mod['func_3892'] = func_3892
mod = relay.transform.InferType()(mod)
var_3893 = relay.var("var_3893", dtype = "bool", shape = (3, 16, 6))#candidate|3893|(3, 16, 6)|var|bool
var_3894 = relay.var("var_3894", dtype = "float32", shape = (1485,))#candidate|3894|(1485,)|var|float32
output = func_3892(var_3893,var_3894,)
func_3895 = relay.Function([var_3893,var_3894,], output)
mutated_mod['func_3895'] = func_3895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_3903 = func_2428_call()
call_3904 = func_2428_call()
output = call_3903
output2 = call_3904
func_3905 = relay.Function([], output)
mod['func_3905'] = func_3905
mod = relay.transform.InferType()(mod)
output = func_3905()
func_3906 = relay.Function([], output)
mutated_mod['func_3906'] = func_3906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2822_call = mod.get_global_var('func_2822')
func_2824_call = mutated_mod.get_global_var('func_2824')
call_3907 = relay.TupleGetItem(func_2822_call(), 0)
call_3908 = relay.TupleGetItem(func_2824_call(), 0)
output = call_3907
output2 = call_3908
func_3919 = relay.Function([], output)
mod['func_3919'] = func_3919
mod = relay.transform.InferType()(mod)
mutated_mod['func_3919'] = func_3919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3919_call = mutated_mod.get_global_var('func_3919')
call_3920 = func_3919_call()
output = call_3920
func_3921 = relay.Function([], output)
mutated_mod['func_3921'] = func_3921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3370_call = mod.get_global_var('func_3370')
func_3372_call = mutated_mod.get_global_var('func_3372')
call_3922 = func_3370_call()
call_3923 = func_3370_call()
var_3944 = relay.var("var_3944", dtype = "float32", shape = (3, 16, 6))#candidate|3944|(3, 16, 6)|var|float32
bop_3945 = relay.add(call_3922.astype('uint16'), relay.reshape(var_3944.astype('uint16'), relay.shape_of(call_3922))) # shape=(3, 16, 6)
bop_3948 = relay.add(call_3923.astype('uint16'), relay.reshape(var_3944.astype('uint16'), relay.shape_of(call_3923))) # shape=(3, 16, 6)
func_1076_call = mod.get_global_var('func_1076')
func_1083_call = mutated_mod.get_global_var('func_1083')
const_3950 = relay.const([8.068877,1.278555,9.135521,5.876252,2.498587,4.490978,-3.565288,-6.688367,-4.210041,-7.076532,9.533207,1.876085,-4.087838,0.245284,-9.513471,-3.793164,9.368598,7.591765,0.210171,6.188365,-3.481137,9.319562,-1.644678,4.775085,-6.414725,5.964727,5.555949,-3.551581,4.166878,-3.185110,-4.967474,-0.520260,-7.262318,-5.628017,-0.593864,-8.614145,7.487442,9.334170,4.875104,-2.196039,-6.932171,-2.114836,-6.863119,-7.266192,-8.407420,2.931572,3.389137,-9.872823,-7.413667,9.706489,-2.619263,5.972619,2.649830,6.706443,-2.932218,1.763809,2.279471,-6.009764,-4.262743,-9.522554,8.190798,1.306486,1.000929,7.586989,9.287204,-6.269646,-3.525581,0.229342,-3.898110,8.130191,-9.891789,6.410242,-4.676157,9.259754,-5.625437,5.866841,2.115929,-7.835460,-8.461217,-9.970941,-1.549139,-5.705532,2.512728,9.550622,-0.385221,-2.961803,7.273896,6.926323,1.252561,-2.325754,-1.362906,-2.335824,-5.890008,-2.202671,-8.124892,-4.563952,3.554421,8.188981,-8.514745,-3.328844,7.179578,1.291153,-7.157412,-5.585859,1.309931,-6.140187,-7.166830,-4.903024,6.411143,-5.906020,3.335260,0.986567,1.665343,6.303622,4.251286,-0.491589,-6.681685,6.088900,-3.882969,6.446492,-8.171958,4.607331,-8.673168,6.909808,-4.940759,3.144063,7.087779,-4.857107,2.904616,-3.661133,8.536963,-6.458658,7.210008,9.070045,5.854011,3.745690,-6.529726,8.644069,-5.339579,-9.039583,-9.597089,9.553589,-5.531786,-3.482542,4.184554,-3.308519,0.242498,0.095711,-2.339652,5.812069,7.337657,0.260884,4.007401,-2.145635,-1.655424,0.222994,-0.531535,-7.809601,-4.733702,-2.279251,1.878590,5.753563,5.629856,7.550468,5.543425,-0.324802,-2.680267,-4.003697,-1.697158,4.150491,0.415132,3.154343,1.836192,7.380483,-8.829290,-3.696603,-8.619782,-0.147383,-4.866736,-0.898139,-7.888736,-6.273254,-4.691760,4.377704,4.580802,9.009808,3.029001,-0.644112,-5.615588,-4.136677,8.422355,2.485795,-2.907985,-8.777418,5.020223,-8.021899,5.142726,-0.685780,2.987973,-5.971158,4.434310,-8.336741,-2.676077,0.215865,-6.914826,0.974563,-6.231004,3.947957,-0.773136,5.070376,-9.114075,-9.034584,-0.369636,-1.798240,-9.565221,-6.126208,-9.921385,-0.536702,4.772707,-2.994355,4.062861,-9.742380,-5.050865,2.702269,1.085529,-3.641010,-7.238481,2.649369,-6.516685,8.517735,-0.731692,-3.157994,-4.110905,4.180010,-0.205897,8.734342,4.463174,-1.413838,4.502937,-7.023261,-2.286965,8.194249,6.480592,-7.953385,-9.995672,-1.088360,4.597871,9.273391,8.643492,-6.108071,-5.677822,-1.766398,1.513447,8.962530,-9.112628,2.020424,5.486426,1.349538,9.052829,-8.622015,7.661481,-1.143765,4.125449,-8.434937,-8.403525,-1.972066,-2.195459,-7.297914,2.333967,6.258158,9.095984,8.888765,3.177574,-8.953245,-6.009964,-8.862976,3.272602,-6.832987,-5.843780,-6.983522,2.939360,-6.258537,4.239012,1.672902,-5.777787,-9.707593,0.592417,-8.832789,-3.813566,4.677195,0.105884,6.296827,-3.439093,5.785595,-4.593662,0.184338,6.554738,-5.814673,-5.809470,6.673794,-3.395207,2.334652,0.443064,-9.533385,-9.608221,-8.711031,6.395846,-2.983749,-7.470204,-1.992714,5.555039,-5.909210,9.680754,9.801103,9.345564,3.652798,-9.260308,4.948969,-9.374767,-2.562144,-5.089505,6.879100,-0.080151,1.139630,0.880110,9.729134,-2.749598,2.866975,-2.839962,3.853947,-5.829978,6.069601,5.594793,-1.025876,-5.608529,-9.641212,-7.298029,-5.826764,-5.194238,4.404605,-4.289678,-2.101916,-5.440985,-5.160414,3.796022,-9.138010,-0.600968,-0.700578,7.359324,-5.110350,3.711221,-7.708953,-6.672443,-3.608826,-9.522898,-0.446558,6.913388,0.655506,6.922780,-0.733766,-2.892021,-1.658116,3.907103,-1.416567,6.849977,-2.101452,-6.704179,-0.720853,-9.111006,5.048431,-8.669663,6.136516,-6.805517,-1.351131,-9.725274,-4.092182,8.145215,-5.825510,-6.781514,2.640078,7.304506,-8.663659,-2.363936,-8.966996,-3.327674,-4.203461,3.934546,-9.943233,-7.441331,5.113491,7.492643,7.669410,-3.524573,5.127401,1.657808,3.028975,9.221773,-3.344413,-9.632127,-5.532992,-7.782621,-7.603100,-1.617658,8.115681,6.307478,2.827114,4.958303,9.563020,-9.884602,-6.406988,-6.774462,-4.949930,5.051734,4.548997,8.588919,-1.416253,-3.000711,-6.931939,0.774144,-0.773780,-1.135175,-0.312205,-3.796854,-9.054040,-6.251756,-8.368869,-5.661083,-8.796383,5.452470,0.486017,7.057745,-2.420968,-1.110654,-6.609584,6.740258,-5.751349,8.066528,2.369553,0.614004,-0.706787,-2.702013,-3.767932,-9.634051,-4.437534,-4.223571,-6.874136,-9.449217,-5.100063,7.940287,-3.827093,0.907181,3.938500,7.905475,-6.616485,-9.028672,7.849582,-2.954488,3.966172,-9.660346,-2.874431,4.582699,3.567704,-1.276896,8.820744,-7.906924,-6.364460,-9.053148,-7.427182,-3.725703,-1.374441,-8.179997,7.181756,7.794731,3.634125,-4.225194,3.541127,-7.682274,7.960239,-9.932417,3.637619,4.828307,-4.086636,7.335585,6.932485,4.046670,-3.024195,6.279463,-9.863440,-3.707249,9.238618,-6.575896,-5.342148,2.856267,7.619754,-4.690922,-9.330721,-8.398428,-5.332840,-2.626966,3.437894,9.038540,9.431018,9.764649,-9.578526,9.063858,-3.187309,-1.030748,-4.500640,0.299035,1.616667,-5.365566,9.230020,-2.852558,-4.622894,0.132573,-3.111849,1.063662,-4.834058,-5.809211,-0.924946,-2.516182,9.473577,-0.529515,-2.291002,7.320370,0.424088,3.259652,-3.832227,-7.151715,-8.463296,-8.560772,0.589765,-6.847291,-9.288016,-8.503869,-7.440847,4.613241,2.827762,-3.387238,9.113587,5.475703,8.527805,1.052471,-6.304349,9.892525,-9.822891,5.286222,4.556681,7.409315,-7.212100,4.440905,-5.827415,-5.317291,-4.885490,6.705411,-6.846796,-9.409910,0.736253,4.108830,-5.867750,4.526546,-0.376524,-5.421324,-3.035425,9.582863,3.763680,-8.014135,-5.271592,3.596133,9.102583,-1.924654,5.132260,9.538183,7.301277,-2.236245,5.883961], dtype = "float32")#candidate|3950|(576,)|const|float32
var_3951 = relay.var("var_3951", dtype = "uint32", shape = (24,))#candidate|3951|(24,)|var|uint32
var_3952 = relay.var("var_3952", dtype = "uint32", shape = (384,))#candidate|3952|(384,)|var|uint32
var_3953 = relay.var("var_3953", dtype = "float32", shape = (16, 4))#candidate|3953|(16, 4)|var|float32
const_3954 = relay.const([4.268131,6.818279,-7.578569,3.146934,2.772889,3.594838,0.452758,1.951118,-1.653817,3.830888,3.870181,-6.838658,-8.663761,-7.053028,-1.804009,-0.772509,-5.216899,-2.069839,-4.743140,-5.046872,7.704217,9.169456,8.707546,2.923455,-3.992103,-5.474663,-1.982714,9.440888,-5.371209,-6.166528,9.163973,-5.392559,-2.163509,-7.022463,-3.861375,4.572822,9.234897,8.181959,7.362139,-1.703568,8.170197,6.481815,-3.719881,-6.683955,9.085682,4.396802,1.026736,-6.669288,7.828882,-1.960133,0.617749,0.405369,-2.920698,6.836816,3.943652,5.644065,-7.969583,-0.442986,7.018636,4.685106,-9.825093,5.184423,-2.250714,5.662925,2.531107,9.313056,3.935396,4.067920,0.763600,2.742094,-1.435355,1.055830,-7.826601,5.895037,-1.829114,-5.080466,-9.264378,-3.449713,5.466927,-9.360625,-5.741562,4.044886,-4.451125,4.697554,9.921719,2.792077,-3.788539,-3.287773,-7.338109,-7.428223,-0.249441,5.412776,4.550995,4.979157,-3.859660,0.151861,8.200167,-2.743304,7.739529,-8.214723,8.495239,-4.626029,-3.322039,-8.911194,2.674597,-6.228842,9.274636,-1.028252,7.335000,4.295234,4.206206,-8.583386,5.932496,-0.433700,5.080387,4.486645,-4.622736,-0.962942,-3.366856,-2.182018,2.105555,5.809755,-3.809875,2.549175,8.136190,4.612156,0.920938,9.131963,5.305122,3.851721,-5.470063,0.958703,1.472734,-1.675486,-2.558984,9.809995,4.811930,-6.857070,-2.623709,7.056584,-2.518253,-1.737437,4.464880,-9.884523,6.918212,1.441773,-5.420005,6.621425,-1.323938,0.449270,-6.158028,-3.077546,9.380977,3.491053,4.838052,0.012069,-5.376074,7.853669,1.056062,-2.579743,-2.471821,8.066228,-6.647022,-6.836227,-1.164335,2.431944,-2.531303,-8.917840,-1.498913,0.750962,-9.938956,5.213499,-7.123683,-6.777585,-3.420229,-8.407713,-8.389306,7.497793,-7.823762,5.981097,4.931260,0.614540,4.467117,3.958396,-5.341993,2.261462,0.207925,2.739335,0.741973,2.482973,-9.559181,-9.707579,3.223039,1.287731,9.205345,-6.716512,0.200511,-8.338980,1.786278,-5.753789,-4.325395,3.984012,-4.918218,2.502762,-0.352889,8.109136,4.924035,-0.367604,5.724175,-5.608486,-3.544778,1.547924,1.285532,-2.162823,0.857180,-4.667884,-4.506293,6.836910,-7.086626,0.183312,5.195235,8.215036,-5.617354,-1.628573,8.598804,4.986553,5.909588,6.195004,-4.296634,-2.680415,-1.471310,-1.410733,-5.762292,2.596923,-1.892793,4.936705,7.151228,-0.518000,-7.458825,7.659993,-0.679695,-5.738853,9.265468,-8.821390,3.379148,1.093488,3.082268,2.401003,0.866296,-6.593000,9.210120,0.576754,-2.854021,-7.518125,-2.204682,-7.717153,-1.549924,8.623012,-0.564795,-3.549962,-7.809976,3.285069,5.786299,7.445032,1.133065,-1.374640,6.059366,1.880586,-7.560054,4.559097,5.745246,9.722626,-7.900472,4.974644,-7.689433,-4.605441,0.678537,-6.048139,-6.102014,3.593974,0.080943,-8.938699,6.490265,-8.560941,-0.025430,2.158639,8.098682,0.455512,8.547052,-1.205574,-4.467748,-5.263811,-7.643258,-4.656487,-2.190289,-4.280135,-4.418569,-3.734496,-8.733038,7.347108,-0.260465,-8.883562,7.075333,7.589485,-1.777921,-7.153973,6.985437,-0.200719,3.550351,-5.550670,-7.382037,6.424185,-1.270884,-1.856283,-1.290855,7.850777,-5.319093,-6.947907,0.560296,-1.809565], dtype = "float32")#candidate|3954|(320,)|const|float32
call_3949 = relay.TupleGetItem(func_1076_call(relay.reshape(const_3950.astype('float32'), [9, 16, 4]), relay.reshape(var_3951.astype('uint32'), [24,]), relay.reshape(var_3952.astype('uint32'), [384,]), relay.reshape(var_3953.astype('float32'), [64,]), relay.reshape(const_3954.astype('float32'), [320,]), relay.reshape(var_3952.astype('uint32'), [8, 16, 3]), ), 2)
call_3955 = relay.TupleGetItem(func_1083_call(relay.reshape(const_3950.astype('float32'), [9, 16, 4]), relay.reshape(var_3951.astype('uint32'), [24,]), relay.reshape(var_3952.astype('uint32'), [384,]), relay.reshape(var_3953.astype('float32'), [64,]), relay.reshape(const_3954.astype('float32'), [320,]), relay.reshape(var_3952.astype('uint32'), [8, 16, 3]), ), 2)
func_1574_call = mod.get_global_var('func_1574')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_3959 = relay.TupleGetItem(func_1574_call(relay.reshape(var_3952.astype('uint32'), [384, 1])), 3)
call_3960 = relay.TupleGetItem(func_1576_call(relay.reshape(var_3952.astype('uint32'), [384, 1])), 3)
output = relay.Tuple([bop_3945,call_3949,const_3950,var_3951,var_3952,var_3953,const_3954,call_3959,])
output2 = relay.Tuple([bop_3948,call_3955,const_3950,var_3951,var_3952,var_3953,const_3954,call_3960,])
func_3963 = relay.Function([var_3944,var_3951,var_3952,var_3953,], output)
mod['func_3963'] = func_3963
mod = relay.transform.InferType()(mod)
var_3964 = relay.var("var_3964", dtype = "float32", shape = (3, 16, 6))#candidate|3964|(3, 16, 6)|var|float32
var_3965 = relay.var("var_3965", dtype = "uint32", shape = (24,))#candidate|3965|(24,)|var|uint32
var_3966 = relay.var("var_3966", dtype = "uint32", shape = (384,))#candidate|3966|(384,)|var|uint32
var_3967 = relay.var("var_3967", dtype = "float32", shape = (16, 4))#candidate|3967|(16, 4)|var|float32
output = func_3963(var_3964,var_3965,var_3966,var_3967,)
func_3968 = relay.Function([var_3964,var_3965,var_3966,var_3967,], output)
mutated_mod['func_3968'] = func_3968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3725_call = mod.get_global_var('func_3725')
func_3726_call = mutated_mod.get_global_var('func_3726')
call_3974 = relay.TupleGetItem(func_3725_call(), 0)
call_3975 = relay.TupleGetItem(func_3726_call(), 0)
func_2041_call = mod.get_global_var('func_2041')
func_2047_call = mutated_mod.get_global_var('func_2047')
var_3996 = relay.var("var_3996", dtype = "float32", shape = (576,))#candidate|3996|(576,)|var|float32
var_3997 = relay.var("var_3997", dtype = "uint32", shape = (24, 1))#candidate|3997|(24, 1)|var|uint32
const_3998 = relay.const([4,2,-8,-6,-10,8,3,6,-6,-1,-2,10,-2,6,1,-1,3,-2,10,7,-2,6,8,-7,9,-9,-9,-8,-2,-2,-4,-9,-8,-7,10,-8,1,-8,-6,-3,-5,5,-1,-6,7,-7,2,-7,10,-9,-2,-3,-1,-1,-7,1,7,9,-10,3,4,-10,10,7,5,-8,-2,-7,-3,-1,3,6,9,9,10,-9,-2,1,8,9,3,-8,10,2,-2,-6,7,6,-7,7,7,-2,-7,-2,-2,-6,-10,-1,-8,6,6,-6,5,-10,6,-10,5,3,-6,5,-6,2,-5,-10,8,4,9,-6,3,7,-5,-6,10,10,-4,3,-6,-8,7,-4,4,-8,10,-9,4,-6,-4,7,2,7,2,6,4,9,-3,-8,-2,2,-4,9,-9,-5,7,-5,9,5,-4,9,6,-3,2,-6,2,8,-10,-4,-2,-10,-2,10,-8,3,5,-2,-4,1,-8,10,-6,-6,7,-5,-8,2,1,1,4,-3,-10,3,4,7,3,-2,10,-5,-7,-8,7,-6,1,-10,-3,-5,2,4,3,7,-3,-7,8,-1,-4,1,8,-2,7,3,6,3,-9,-3,-10,-8,-1,7,-7,-4,7,4,5,4,7,1,9,-1,-1,-9,-7,6,-4,-7,1,-3,9,6,3,-7,9,-4,-2,-7,1,5,-4,4,-6,-10,2,-7,-1,6,-5,2,1,-4,-3,7,6,-2,3,-10,-6,-7,-2,-3,1,6,-4,-2,6,-7,7,-3,-6,-3,8,9,4,6,4,8,1,-3,-2,-10,-1,7,1,-2,2,7,1,-8,3,10,3,5,3,7,-3,6,-3,3,-3,-2,-2,-7,-6,7,-8,9,8,5,1,1,-10,9,1,9,9,-3,2,-4,-6,10,-2,5,-2,-3,4,-7,2,8,-8,-9,10,-7,-3,-3,-6,1,9,-9,-8,-5,6,-9,-10,2,-5,4,-5,10,-6,7,3,9,5,4,-10,-6,-5,-5,-1,4,1,3,-10,6,-3,5,10,-9], dtype = "uint32")#candidate|3998|(384,)|const|uint32
var_3999 = relay.var("var_3999", dtype = "bool", shape = (320,))#candidate|3999|(320,)|var|bool
call_3995 = relay.TupleGetItem(func_2041_call(relay.reshape(var_3996.astype('float32'), [576,]), relay.reshape(var_3997.astype('uint32'), [24,]), relay.reshape(const_3998.astype('uint32'), [384,]), relay.reshape(var_3999.astype('bool'), [5, 4, 16]), ), 6)
call_4000 = relay.TupleGetItem(func_2047_call(relay.reshape(var_3996.astype('float32'), [576,]), relay.reshape(var_3997.astype('uint32'), [24,]), relay.reshape(const_3998.astype('uint32'), [384,]), relay.reshape(var_3999.astype('bool'), [5, 4, 16]), ), 6)
output = relay.Tuple([call_3974,call_3995,var_3996,var_3997,const_3998,var_3999,])
output2 = relay.Tuple([call_3975,call_4000,var_3996,var_3997,const_3998,var_3999,])
func_4015 = relay.Function([var_3996,var_3997,var_3999,], output)
mod['func_4015'] = func_4015
mod = relay.transform.InferType()(mod)
var_4016 = relay.var("var_4016", dtype = "float32", shape = (576,))#candidate|4016|(576,)|var|float32
var_4017 = relay.var("var_4017", dtype = "uint32", shape = (24, 1))#candidate|4017|(24, 1)|var|uint32
var_4018 = relay.var("var_4018", dtype = "bool", shape = (320,))#candidate|4018|(320,)|var|bool
output = func_4015(var_4016,var_4017,var_4018,)
func_4019 = relay.Function([var_4016,var_4017,var_4018,], output)
mutated_mod['func_4019'] = func_4019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mod.get_global_var('func_3542')
func_3543_call = mutated_mod.get_global_var('func_3543')
call_4069 = relay.TupleGetItem(func_3542_call(), 0)
call_4070 = relay.TupleGetItem(func_3543_call(), 0)
output = call_4069
output2 = call_4070
func_4076 = relay.Function([], output)
mod['func_4076'] = func_4076
mod = relay.transform.InferType()(mod)
mutated_mod['func_4076'] = func_4076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4076_call = mutated_mod.get_global_var('func_4076')
call_4077 = func_4076_call()
output = call_4077
func_4078 = relay.Function([], output)
mutated_mod['func_4078'] = func_4078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_4111 = relay.TupleGetItem(func_2536_call(), 0)
call_4112 = relay.TupleGetItem(func_2538_call(), 0)
output = relay.Tuple([call_4111,])
output2 = relay.Tuple([call_4112,])
func_4122 = relay.Function([], output)
mod['func_4122'] = func_4122
mod = relay.transform.InferType()(mod)
mutated_mod['func_4122'] = func_4122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4122_call = mutated_mod.get_global_var('func_4122')
call_4123 = func_4122_call()
output = call_4123
func_4124 = relay.Function([], output)
mutated_mod['func_4124'] = func_4124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mod.get_global_var('func_3905')
func_3906_call = mutated_mod.get_global_var('func_3906')
call_4125 = func_3905_call()
call_4126 = func_3905_call()
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_4133 = relay.TupleGetItem(func_3507_call(), 5)
call_4134 = relay.TupleGetItem(func_3509_call(), 5)
func_2671_call = mod.get_global_var('func_2671')
func_2675_call = mutated_mod.get_global_var('func_2675')
var_4141 = relay.var("var_4141", dtype = "uint32", shape = (384,))#candidate|4141|(384,)|var|uint32
const_4142 = relay.const([-5.379013,-9.431087,2.144382,-9.023277,-8.453023,0.346882,8.456833,7.348590,-2.311688,-8.615928,0.691002,9.546645,0.573784,3.557313,7.185109,-7.908432,-7.694905,3.042256,8.018917,-4.938598,-1.176458,-9.401519,-4.278703,1.740358,-4.287732,-4.162953,7.577272,-9.830026,-9.357750,-7.336493,-0.245516,6.257862,6.842469,-1.122853,6.827617,-2.284366,6.056779,3.099956,-6.966512,-7.338647,-0.042677,-9.940311,-8.649860,4.431373,7.590017,-9.529337,-3.134955,-7.384536,-4.945487,8.833198,0.466936,-3.670200,-8.130310,-5.778239,-2.625323,-5.396797,6.742166,-3.675278,6.633287,6.413753,6.491438,-6.518722,5.633959,-6.050283,3.955020,2.833758,4.256848,1.735175,-0.549533,9.229418,-6.379130,4.441060,-5.527664,3.387155,7.290277,-1.925431,-8.446119,1.348678,5.337793,-5.292939,4.199320,6.373785,0.496689,-3.131649,-7.890085,-9.994282,0.790215,8.099102,6.564935,9.247209,2.710119,-6.332338,-5.088257,5.975539,6.191146,0.057580,-6.604144,6.054221,4.920715,2.035328,6.387073,3.204066,1.860423,8.021641,8.969647,-3.213243,-7.094618,6.077581,-3.442314,0.621278,-0.515938,-3.429612,2.394236,-9.589480,9.767617,2.305751,2.935010,-6.537890,4.115972,3.511902,-1.402723,7.015951,-1.304945,-3.467738,8.301242,-7.527610,-5.080109,-0.207285,2.846125,-8.362024,-6.735281,1.309427,-3.078283,0.026075,9.253587,0.045580,-6.953763,2.521904,8.877085,7.361737,6.556390,-0.675414,-9.811776,6.932945,6.336579,-6.275243,9.953548,2.021382,8.126661,5.011801,9.855981,7.750161,5.420367,6.367093,-0.855507,-7.565911,-1.125474,5.676213,0.517602,-1.545852,-7.872514,0.598232,3.325347,-4.810564,9.654241,6.597615,-7.286748,-9.809883,0.443413,-1.986782,-0.952577,1.838224,2.732084,3.345361,-9.154826,5.673768,-1.313713,-6.013561,1.705167,0.925755,0.775575,6.245076,9.478595,8.839454,8.702547,-9.229166,-2.341122,5.651091,-9.679026,2.499222,-0.738710,4.631869,4.765023,-7.275569,-0.323625,1.967428,9.424504,6.453877,-8.573674,2.756284,-3.910337,3.483836,-6.862719,-3.576403,0.409320,5.982219,-9.039730,-1.569708,-6.579035,-9.063868,-3.639497,-7.450655,8.344694,-5.505642,0.667757,7.619356,4.141920,-1.594451,1.690828,-8.430610,-6.076254,6.162062,9.122728,-8.645650,-6.163451,-3.727661,-2.568941,-2.082161,4.330474,9.178482,4.476113,-2.987023,2.004670,-0.270951,-5.989934,4.985937,-3.811447,0.040487,5.939579,5.418683,3.838218,-3.807248,1.979544,6.608861,-2.008657,2.709984,9.008031,-1.428087,-2.176315,-6.477959,-0.861917,-7.104763,-4.927193,-3.045259,7.519701,8.701538,9.772209,4.399149,8.583116,2.245337,7.508372,2.566969,1.127010,-3.242342,-4.151295,-1.362812,-4.285218,5.222149,-9.457169,-4.104236,6.388400,-5.720311,-6.745009,0.139017,-1.795654,4.703598,7.018378,9.820383,-6.897017,1.076876,-5.602522,3.914820,-3.807081,6.573778,-3.255842,-5.391758,5.367402,3.562288,-6.307968,4.083281,2.298251,5.357288,4.450134,3.403130,-5.474008,-5.380636,-7.594647,4.540636,-1.533085,-7.586428,0.542505,5.965708,6.909235,-0.030481,8.730236,6.784851,-0.365482,-0.327305,1.743844,8.354091,-2.797443,-3.313948,-6.200920,2.339925,-9.993452,9.175649,-3.960200,-5.898472,1.518603,-8.320984,4.802533,-8.604344,-0.907408,3.665579,-5.026782,9.465101,7.041887,-0.913320,8.134161,-7.506566,5.622477,1.055590,-7.913606,7.182168,-4.084237,8.427458,2.119210,9.218019,-3.026563,0.723971,-4.556409,7.895037,-9.759989,4.048710,5.901144,2.721748,4.257296,-0.525114,2.488263,-0.586459,5.085055,6.272271,7.820539,-0.171638,9.272782,-1.306442,-1.181302,6.806567,2.278026,5.990762,2.921962,5.603884,8.330863,-2.356369,-7.956360,6.259011,-2.690096,-6.741129,8.531188,4.349306,2.744708,-2.285348,2.391136,-0.743412,-1.238081,2.266189,2.071419,9.528968,4.945169,7.602811,-5.069863,4.333154,9.105540,-7.981427,9.617999,1.054323,9.754514,-1.940170,-1.765243,-8.770982,-6.333784,-4.986564,-0.467680,3.183236,5.259720,6.433071,0.057247,9.044490,3.179386,2.242591,2.607625,3.941237,5.297211,-2.742861,-0.878224,-5.390534,-0.774055,-3.695880,-3.811149,-9.374530,-2.731011,9.638483,5.427353,-1.290343,-9.269574,8.762907,7.877529,6.222995,-3.090953,-8.538054,-9.181555,-2.030435,8.936202,8.940474,-3.109842,8.296115,-2.957166,-9.321848,6.473845,-5.143829,-0.877352,-4.353157,-7.987315,-5.718888,5.690965,2.873527,-8.989286,-2.698336,0.047853,8.239159,-2.937540,-2.813451,-0.833648,-0.996149,-7.773904,9.269727,-4.370937,-2.394867,6.105750,4.105150,5.118731,-1.366814,-3.486622,4.867168,0.056118,3.387533,0.960968,-1.459146,-8.724812,-2.799074,6.548292,-2.978849,6.816775,-0.774673,1.058079,4.979860,-3.428868,-4.173657,-4.934710,-7.126684,9.437366,7.449838,-4.125928,-9.889163,-7.000944,2.205029,-6.777812,5.765939,-3.128449,2.709004,-7.300509,-2.140448,-8.898503,7.518117,-7.544126,-5.169294,-2.431927,-1.038230,4.766579,8.659775,5.447261,3.779621,-7.800659,4.408878,-4.525712,4.748028,5.844047,-1.867402,-1.925642,1.877087,7.657015,-0.563111,5.079070,-4.208651,2.460251,8.722045,-4.191665,4.201262,9.834678,5.430583,0.166910,-4.064213,-5.678957,-1.730334,2.892718,7.238299,-5.909629,-4.145389,6.800007,-1.612305,-3.498447,0.088747,9.680183,-8.029320,-0.441939,-1.910444,-1.994817,-1.113778,4.943847,8.523139,-3.345779,-1.615098,9.467003,9.607721,3.585633,0.682466,1.147319,1.014610,1.414098,4.112112,5.114936,0.531244,4.103347,3.311620,5.939222,5.315803,3.416801,-2.235455,-0.214701,4.068451,7.398627,7.138427,-6.033755,7.589880,-6.650887,1.948610,0.361906,7.107634,-5.941017,2.282291,-2.557842,-3.583335,-9.340008,-6.355749,-5.446560,1.866915,-4.411851,-0.324836,0.685337,6.812592,-8.025527,6.831960,6.043012,-6.822501,1.902692,0.492690], dtype = "float32")#candidate|4142|(576,)|const|float32
var_4143 = relay.var("var_4143", dtype = "float32", shape = (320,))#candidate|4143|(320,)|var|float32
call_4140 = relay.TupleGetItem(func_2671_call(relay.reshape(var_4141.astype('uint32'), [384,]), relay.reshape(const_4142.astype('float32'), [576,]), relay.reshape(var_4143.astype('float32'), [320,]), ), 2)
call_4144 = relay.TupleGetItem(func_2675_call(relay.reshape(var_4141.astype('uint32'), [384,]), relay.reshape(const_4142.astype('float32'), [576,]), relay.reshape(var_4143.astype('float32'), [320,]), ), 2)
func_2377_call = mod.get_global_var('func_2377')
func_2383_call = mutated_mod.get_global_var('func_2383')
const_4154 = relay.const([5.420244,-4.973110,2.763098,2.095504,-1.079062,8.637712,-4.409848,6.940910,0.934922,7.545969,2.498729,5.096359,1.158917,2.545829,4.601285,-5.780818,-8.779629,7.813477,-3.337844,-9.930851,4.600345,-0.597293,-4.013819,-9.181991,6.221271,-7.954421,-6.328329,6.440470,-3.322697,-7.409275,8.246597,-8.740852,-0.920140,5.590175,4.593271,2.286372,4.309660,-7.185080,3.382002,-5.722464,-9.854540,-0.161577,-6.288727,-6.014514,-1.375059,4.826964,-6.081295,5.425348,4.721406,0.196611,2.648334,3.661103,-3.056115,-7.589804,-3.679658,1.002384,7.210276,8.184415,6.679730,-5.517177,2.193804,7.595674,-5.384078,-0.034680], dtype = "float32")#candidate|4154|(64,)|const|float32
var_4155 = relay.var("var_4155", dtype = "float64", shape = (8, 20))#candidate|4155|(8, 20)|var|float64
call_4153 = relay.TupleGetItem(func_2377_call(relay.reshape(var_4141.astype('uint32'), [24, 16]), relay.reshape(const_4154.astype('float32'), [64,]), relay.reshape(var_4143.astype('float32'), [4, 80]), relay.reshape(var_4155.astype('float64'), [160,]), ), 5)
call_4156 = relay.TupleGetItem(func_2383_call(relay.reshape(var_4141.astype('uint32'), [24, 16]), relay.reshape(const_4154.astype('float32'), [64,]), relay.reshape(var_4143.astype('float32'), [4, 80]), relay.reshape(var_4155.astype('float64'), [160,]), ), 5)
func_1901_call = mod.get_global_var('func_1901')
func_1903_call = mutated_mod.get_global_var('func_1903')
call_4168 = relay.TupleGetItem(func_1901_call(relay.reshape(var_4155.astype('float64'), [10, 2, 8])), 0)
call_4169 = relay.TupleGetItem(func_1903_call(relay.reshape(var_4155.astype('float64'), [10, 2, 8])), 0)
output = relay.Tuple([call_4125,call_4133,call_4140,var_4141,const_4142,var_4143,call_4153,const_4154,var_4155,call_4168,])
output2 = relay.Tuple([call_4126,call_4134,call_4144,var_4141,const_4142,var_4143,call_4156,const_4154,var_4155,call_4169,])
func_4171 = relay.Function([var_4141,var_4143,var_4155,], output)
mod['func_4171'] = func_4171
mod = relay.transform.InferType()(mod)
var_4172 = relay.var("var_4172", dtype = "uint32", shape = (384,))#candidate|4172|(384,)|var|uint32
var_4173 = relay.var("var_4173", dtype = "float32", shape = (320,))#candidate|4173|(320,)|var|float32
var_4174 = relay.var("var_4174", dtype = "float64", shape = (8, 20))#candidate|4174|(8, 20)|var|float64
output = func_4171(var_4172,var_4173,var_4174,)
func_4175 = relay.Function([var_4172,var_4173,var_4174,], output)
mutated_mod['func_4175'] = func_4175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2822_call = mod.get_global_var('func_2822')
func_2824_call = mutated_mod.get_global_var('func_2824')
call_4187 = relay.TupleGetItem(func_2822_call(), 0)
call_4188 = relay.TupleGetItem(func_2824_call(), 0)
output = relay.Tuple([call_4187,])
output2 = relay.Tuple([call_4188,])
func_4196 = relay.Function([], output)
mod['func_4196'] = func_4196
mod = relay.transform.InferType()(mod)
output = func_4196()
func_4197 = relay.Function([], output)
mutated_mod['func_4197'] = func_4197
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4202 = relay.const([[[-0.454689,-9.442313,-6.140682,9.432945,6.020792,-7.879454,-2.203515,-1.423473,9.743001],[9.653116,-3.335492,-1.036529,-1.109171,6.115910,5.974164,-0.417863,-6.121667,-2.522061],[-0.960862,9.603460,-9.546236,-9.662557,5.825502,-4.677647,1.676772,9.657874,4.359551],[7.125664,-5.952258,7.216897,8.733458,0.512984,-4.127846,-0.999858,-9.270527,5.643353],[-3.263565,3.747358,-8.320270,-2.221166,5.032528,4.949570,4.016330,-6.808453,3.030971],[8.514385,-4.332253,-8.200147,-4.029163,6.600519,-0.961009,5.349734,0.170256,1.577671],[7.428763,2.280357,2.492368,7.085362,2.351166,-1.899553,-4.995514,8.808267,9.815748],[4.667916,3.773580,-7.420041,9.463949,-6.133232,-7.728204,-1.792783,9.365531,7.594761]],[[-4.273335,8.622016,-5.791684,9.674081,2.492821,3.969956,-2.164210,8.485237,-2.950994],[-3.769214,8.684989,-3.791263,-6.190093,8.407785,-2.706226,-6.631462,-8.929795,6.367250],[5.506838,1.319376,0.086900,1.972873,6.470723,9.269297,-5.239714,-0.117189,-5.044780],[-9.899239,7.488077,-4.308717,-6.011136,3.901871,-4.745774,9.187116,2.263885,0.359447],[-8.475225,-0.891994,9.123571,4.031723,6.364388,0.497508,-5.300056,-3.852462,-8.235829],[4.581807,9.277265,7.466422,8.115050,-6.847025,3.284173,-2.866676,-6.898055,5.508945],[-1.276700,-5.370719,-2.152972,-9.190997,2.111848,9.606387,0.882224,-8.383595,0.824403],[5.547235,-5.083117,6.319428,3.671663,2.067059,-5.994955,4.541118,9.290051,1.651921]],[[0.881384,-0.938893,-3.505559,-2.582768,8.789442,7.494860,-4.394655,3.134469,-2.109763],[-1.149940,-9.232404,9.952739,0.303706,-9.345477,-8.289951,-0.447344,3.231461,-7.570961],[-5.884626,5.346953,0.595441,-1.427999,5.000007,6.103752,-3.607859,9.710846,4.678553],[-8.101028,7.489628,-7.880915,-6.672482,-8.515976,2.752479,7.609430,8.393099,2.131338],[1.130939,0.373549,-6.346889,-8.182075,-5.600675,5.119472,7.815895,-8.669218,-4.523165],[-6.119642,-8.318891,-3.156496,-0.631482,3.770356,1.284057,-1.405989,6.442459,9.067587],[-2.781633,-0.189751,-3.306645,5.343949,0.307051,-3.169043,-3.268323,-8.478599,8.590592],[-7.773209,3.910384,-3.543115,8.352237,4.922930,-3.697314,-0.718686,0.472693,6.029267]],[[-4.623642,4.552009,4.529887,-9.373687,-4.915998,-8.871955,7.752078,8.708023,-2.199280],[3.134981,4.008594,-9.170698,-6.630604,-8.710222,-8.942154,8.238567,-0.930981,-7.454220],[-2.067484,1.313674,-4.485774,1.971307,6.576409,-8.525891,-8.431457,6.440905,-1.793669],[0.006562,-4.134457,-6.956578,0.548350,2.327909,-0.172952,4.150641,-7.072909,-7.492889],[-4.002638,4.210742,-1.880570,-0.403300,4.045780,-2.236695,4.863178,-1.453040,-3.045453],[-6.433736,-1.835190,9.124211,-6.782683,-9.927793,-3.581354,2.895390,-9.476143,-5.855118],[-0.107535,4.729464,-1.286389,0.552310,7.048065,0.421206,6.455138,8.064924,1.402866],[-0.162347,-2.461634,8.113791,2.437834,4.476752,0.346579,0.375324,-9.570354,3.386803]],[[-3.893355,8.457445,8.310357,1.685811,-4.698136,-6.870194,-3.147852,6.826704,6.462362],[5.562270,1.310101,-6.888846,-7.030995,-0.104406,-6.810690,2.358738,2.518921,-7.282722],[9.230081,5.707625,6.335768,6.036346,-0.409626,-8.168225,1.621574,3.745864,-5.573763],[8.518084,7.374475,-4.342324,-0.664212,-0.158004,-3.608065,-8.952272,0.988373,6.861276],[6.737867,-5.851144,-9.784276,-5.143450,-7.254848,-3.013383,2.775268,4.836946,-0.495526],[8.999161,5.061218,-0.619427,-9.970382,1.648018,-6.148908,-9.927295,7.450100,2.854815],[5.382008,-9.706339,4.076875,1.132807,-3.408975,4.524680,-2.128208,8.719541,0.479180],[0.953949,-3.273804,6.907709,4.952515,6.924711,-4.845374,-2.634502,-1.886612,1.073158]],[[-1.514998,-8.372747,2.877021,5.547761,-1.790737,1.372464,-2.858849,-0.080862,9.593615],[7.512271,5.661163,1.044875,9.869132,-3.124754,-5.728915,-6.324404,-7.553153,-9.551905],[-5.216048,1.087147,-4.189710,-9.885383,4.724269,-5.055725,-6.410309,4.390194,-8.353426],[5.786958,2.104635,9.897216,7.248065,-1.807590,-8.409364,9.742121,-1.613025,-9.526165],[5.081372,7.592796,7.480285,6.930403,5.127750,9.538982,-0.730232,1.677493,-4.628703],[1.342538,-8.391274,3.166963,-8.900383,-4.802070,5.652181,-5.872510,3.538979,3.918701],[5.342745,8.799642,-0.790976,-5.249838,6.248093,-5.356651,-9.402271,-7.153453,9.641671],[0.219387,-2.473568,-0.270941,-5.675713,9.281703,-1.120206,-9.077120,9.366781,-6.689225]],[[8.710179,-9.483441,-4.051868,-0.784517,0.478642,-8.323874,1.012890,-8.664156,3.716920],[3.048381,8.943858,7.071585,-6.730781,0.792973,6.733785,8.235854,-6.897945,-7.576113],[-6.686022,1.032159,8.063522,-4.544571,-2.577731,-7.331077,3.302076,0.541846,-3.873717],[-1.634660,4.461427,3.512316,2.547811,9.716520,-1.946101,-8.283092,-1.856422,-4.448440],[8.730912,-8.652240,-6.860073,8.514033,7.056915,-9.141998,-8.964803,-3.332648,8.225026],[-4.955956,-5.059448,-7.044440,9.407837,2.154238,3.441728,0.283942,-9.356083,-0.989325],[8.582502,-1.529863,-8.598024,-7.345062,7.218516,-0.598480,-9.219320,7.233941,-1.758483],[-3.157365,-7.114456,-2.342401,8.916019,9.476336,0.383598,-9.959934,2.941375,8.686364]],[[-1.436751,-9.270402,-4.414980,-5.229780,-6.515455,8.859018,7.553409,-0.881904,8.766438],[9.548122,8.995191,-7.460617,-1.395495,0.113624,7.201489,-1.474362,-3.099085,8.577749],[7.875099,-9.939057,6.958719,2.536592,8.661303,6.980705,-1.874250,9.178449,2.930936],[-6.770999,3.750576,8.321217,8.490599,-8.250766,2.064436,-2.491658,5.226689,-1.473432],[9.907324,5.243198,6.774298,8.962704,-0.435067,5.303187,8.920391,5.211269,5.807619],[8.880729,-8.337914,7.571756,-3.060568,6.173637,-7.585240,-1.943765,6.275699,-0.698424],[-5.730883,-4.870198,-5.354430,-4.870135,7.732678,-3.023212,2.273617,9.341044,5.715560],[3.622869,7.539277,9.521264,-0.866607,8.972112,-8.028027,-7.467321,7.306896,7.830607]],[[8.980333,4.276185,1.716698,0.051430,-3.919504,7.090098,4.804453,8.210901,6.239682],[-7.031379,-7.293696,0.644085,4.733734,-9.477978,-5.798896,8.797598,8.192677,-7.549412],[-1.982833,4.217299,3.106167,9.246076,2.962877,0.802668,1.683858,-5.611652,4.698648],[-4.232869,-8.143154,3.458687,-4.584299,-7.099640,-6.881669,9.359088,-9.055689,7.966914],[0.977931,3.157180,5.736499,1.052292,-0.472281,-5.654482,4.172811,6.811347,9.820519],[-6.591779,3.927074,-1.848828,0.892138,-8.205440,-0.836913,4.247685,-8.331601,1.683743],[8.972335,4.700574,-8.246392,8.790352,-1.112566,3.093168,-4.315343,-2.146929,-7.552776],[5.027022,-8.764674,-6.723869,0.480030,-2.356824,-5.802342,6.534149,-8.896695,9.146591]],[[-0.728761,-2.351162,2.067799,7.671796,9.869920,4.855118,-3.227642,4.263515,5.907530],[7.352432,-5.848301,-5.805916,3.997006,-3.870684,-9.278883,4.936428,3.307786,-5.353096],[2.538882,-5.657350,4.882806,6.404321,-4.679246,-4.623509,-2.927366,-5.303142,5.721131],[4.305520,-4.730061,-5.951731,5.498416,5.874749,4.554395,-8.135607,4.540096,4.234430],[-4.188902,-2.469744,7.177451,-6.999510,0.193016,-2.568286,-3.484258,1.921930,-8.483138],[8.912124,1.353301,-4.099589,-9.626202,-5.921753,5.818982,-9.528169,-9.736622,-2.120169],[9.437487,1.866034,7.951908,2.737221,9.751644,-5.795157,-8.104590,4.489148,-7.955908],[-3.008360,-2.676440,3.513747,-3.091125,-1.388213,-7.886282,8.043871,2.818131,-6.999148]],[[-3.338651,-6.089026,4.702233,8.960177,1.907271,6.898287,-5.593229,-7.994034,-5.042787],[-0.272562,-0.857617,0.917405,8.800956,-3.543747,7.644815,0.087993,5.080192,8.645678],[-2.536831,-3.001196,-3.870033,-2.542731,-7.816249,8.277597,-8.968301,0.521455,-9.877509],[1.135401,4.290153,5.443188,7.916088,4.833266,-8.027113,9.106298,6.434362,-4.936438],[6.801234,1.763495,-0.654035,1.589100,-2.304198,6.990977,4.797251,6.556936,-6.963021],[-5.767448,8.871726,-0.938887,-3.985902,0.484868,-3.608278,1.099430,-8.810595,5.327293],[-0.698905,3.312935,5.390153,9.190884,8.931220,-0.890098,3.275664,4.204978,-6.473216],[3.113571,4.081195,-8.278985,-1.986924,-3.674906,-3.115967,2.044042,-5.565648,-0.652566]],[[2.825446,-5.957460,-5.186864,7.598746,8.610482,-4.761046,-9.214653,0.581874,-6.765018],[9.584116,9.674104,7.607050,8.911972,-6.930358,9.254203,-7.480834,1.162895,-6.041235],[5.146637,9.286390,-2.712329,-2.830851,5.197366,6.763517,8.755702,2.337416,-4.407447],[9.476892,0.832003,7.708149,-0.713778,-0.042309,-9.138976,3.050849,-9.156892,1.768583],[-0.303459,1.598139,0.235907,-1.216496,-8.478150,7.359805,-5.534563,-3.183802,9.857822],[7.043617,7.614935,6.387218,-3.101940,9.497113,8.539576,3.134525,-6.458526,-1.317473],[4.055966,8.545184,-8.294013,-9.160592,2.133285,-3.030637,-3.178354,-1.427413,6.347352],[-8.586386,-0.440884,-0.500590,-1.903926,5.410908,6.284798,-3.317171,-9.505868,-3.628595]]], dtype = "float32")#candidate|4202|(12, 8, 9)|const|float32
uop_4203 = relay.log(const_4202.astype('float32')) # shape=(12, 8, 9)
output = relay.Tuple([uop_4203,])
output2 = relay.Tuple([uop_4203,])
func_4207 = relay.Function([], output)
mod['func_4207'] = func_4207
mod = relay.transform.InferType()(mod)
mutated_mod['func_4207'] = func_4207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4207_call = mutated_mod.get_global_var('func_4207')
call_4208 = func_4207_call()
output = call_4208
func_4209 = relay.Function([], output)
mutated_mod['func_4209'] = func_4209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3725_call = mod.get_global_var('func_3725')
func_3726_call = mutated_mod.get_global_var('func_3726')
call_4210 = relay.TupleGetItem(func_3725_call(), 0)
call_4211 = relay.TupleGetItem(func_3726_call(), 0)
output = call_4210
output2 = call_4211
func_4217 = relay.Function([], output)
mod['func_4217'] = func_4217
mod = relay.transform.InferType()(mod)
mutated_mod['func_4217'] = func_4217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4217_call = mutated_mod.get_global_var('func_4217')
call_4218 = func_4217_call()
output = call_4218
func_4219 = relay.Function([], output)
mutated_mod['func_4219'] = func_4219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_4235 = relay.TupleGetItem(func_1522_call(), 0)
call_4236 = relay.TupleGetItem(func_1524_call(), 0)
output = call_4235
output2 = call_4236
func_4240 = relay.Function([], output)
mod['func_4240'] = func_4240
mod = relay.transform.InferType()(mod)
output = func_4240()
func_4241 = relay.Function([], output)
mutated_mod['func_4241'] = func_4241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_4316 = func_2428_call()
call_4317 = func_2428_call()
func_2041_call = mod.get_global_var('func_2041')
func_2047_call = mutated_mod.get_global_var('func_2047')
var_4319 = relay.var("var_4319", dtype = "float32", shape = (576,))#candidate|4319|(576,)|var|float32
var_4320 = relay.var("var_4320", dtype = "uint32", shape = (24,))#candidate|4320|(24,)|var|uint32
var_4321 = relay.var("var_4321", dtype = "uint32", shape = (384, 1))#candidate|4321|(384, 1)|var|uint32
var_4322 = relay.var("var_4322", dtype = "bool", shape = (8, 40))#candidate|4322|(8, 40)|var|bool
call_4318 = relay.TupleGetItem(func_2041_call(relay.reshape(var_4319.astype('float32'), [576,]), relay.reshape(var_4320.astype('uint32'), [24,]), relay.reshape(var_4321.astype('uint32'), [384,]), relay.reshape(var_4322.astype('bool'), [5, 4, 16]), ), 1)
call_4323 = relay.TupleGetItem(func_2047_call(relay.reshape(var_4319.astype('float32'), [576,]), relay.reshape(var_4320.astype('uint32'), [24,]), relay.reshape(var_4321.astype('uint32'), [384,]), relay.reshape(var_4322.astype('bool'), [5, 4, 16]), ), 1)
output = relay.Tuple([call_4316,call_4318,var_4319,var_4320,var_4321,var_4322,])
output2 = relay.Tuple([call_4317,call_4323,var_4319,var_4320,var_4321,var_4322,])
func_4330 = relay.Function([var_4319,var_4320,var_4321,var_4322,], output)
mod['func_4330'] = func_4330
mod = relay.transform.InferType()(mod)
mutated_mod['func_4330'] = func_4330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4330_call = mutated_mod.get_global_var('func_4330')
var_4332 = relay.var("var_4332", dtype = "float32", shape = (576,))#candidate|4332|(576,)|var|float32
var_4333 = relay.var("var_4333", dtype = "uint32", shape = (24,))#candidate|4333|(24,)|var|uint32
var_4334 = relay.var("var_4334", dtype = "uint32", shape = (384, 1))#candidate|4334|(384, 1)|var|uint32
var_4335 = relay.var("var_4335", dtype = "bool", shape = (8, 40))#candidate|4335|(8, 40)|var|bool
call_4331 = func_4330_call(var_4332,var_4333,var_4334,var_4335,)
output = call_4331
func_4336 = relay.Function([var_4332,var_4333,var_4334,var_4335,], output)
mutated_mod['func_4336'] = func_4336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3461_call = mod.get_global_var('func_3461')
func_3463_call = mutated_mod.get_global_var('func_3463')
call_4377 = relay.TupleGetItem(func_3461_call(), 0)
call_4378 = relay.TupleGetItem(func_3463_call(), 0)
func_2671_call = mod.get_global_var('func_2671')
func_2675_call = mutated_mod.get_global_var('func_2675')
const_4401 = relay.const([-8,-3,-9,-10,-8,4,3,-1,2,-9,9,10,4,-10,9,-4,-4,3,-9,6,3,-9,1,5,-3,8,-8,-3,2,-7,5,-5,8,10,-3,5,8,4,3,-3,-6,10,1,-6,9,5,7,-2,-10,-4,-3,-10,-2,10,-4,4,6,-3,9,2,-5,3,7,-8,-2,-1,-9,3,3,-9,-6,4,6,1,-9,5,-1,5,-8,6,-5,-4,-8,-8,-10,-8,9,-2,-1,2,7,-3,8,8,-1,5,-3,-2,7,2,6,-8,1,-10,3,2,1,-10,-1,6,-7,10,1,-1,-2,8,2,-1,-3,5,6,8,1,6,-10,-8,5,-7,9,-7,-10,9,8,-4,2,9,-7,5,8,-1,-6,-5,8,9,9,-8,-8,4,-8,1,10,-10,-8,6,-8,2,8,7,9,-3,2,1,10,-8,-4,10,8,10,5,-1,4,7,3,6,-9,-2,2,-3,-7,-3,-9,-4,3,6,-1,-10,-2,-5,-10,7,-3,10,-2,-8,-3,9,-3,10,8,-3,3,-4,-10,-10,-1,10,7,9,-1,8,9,-8,2,-2,6,-9,-9,-5,-1,9,-3,-6,-9,10,6,-5,-7,1,1,-10,-9,5,2,-8,7,5,-6,-2,9,-6,2,-10,-2,-8,2,-9,9,-10,-6,-1,6,2,-8,1,-6,10,6,-7,-1,-1,-5,6,6,2,-4,4,-1,-6,-9,-6,-1,5,10,-8,-8,-6,1,4,9,9,1,7,-10,-2,-9,-5,9,-2,1,2,8,2,-3,9,4,-7,-3,-8,-9,-1,-3,3,-8,2,2,9,-1,1,7,6,-8,-8,-9,-2,-1,7,3,7,-2,1,3,5,-2,10,4,3,-10,3,-9,8,-1,-3,4,6,-9,1,8,7,-4,-1,4,-2,-5,4,9,-6,-6,5,-1,5,7,-3,3,6,9,-6,1,7,-3,2,2,4,-6,-7,9,8,-7,-2,-3,8,6,-6,1,5,-6,-6,4,6,9,9,-5,-4,10,-5], dtype = "uint32")#candidate|4401|(384,)|const|uint32
var_4402 = relay.var("var_4402", dtype = "float32", shape = (2, 288))#candidate|4402|(2, 288)|var|float32
const_4403 = relay.const([[4.765507,-7.441145,3.581926,8.097290,8.930836,5.649511,-6.259431,-7.005917],[-3.817394,4.556421,-4.161629,7.605675,9.582573,-8.570373,8.809397,4.150127],[3.413889,-0.816944,6.253036,-4.298619,8.899912,-4.903918,-2.877188,7.848070],[8.547680,-8.156868,-0.777544,-9.307409,-8.069430,5.222865,-7.526787,-7.671642],[-9.239072,6.111038,-9.953119,-7.686955,0.306146,2.920238,6.955606,-3.943124],[8.884680,7.119334,-4.732611,-9.979157,-6.359684,5.025967,-9.894354,-7.258929],[-2.620137,-1.157114,2.321736,-4.629546,8.127339,3.444681,-8.494493,1.522035],[-0.619002,5.423629,-6.144716,2.436141,7.832049,-4.881619,1.227132,-2.053360],[-2.328015,-5.395041,-2.041340,-3.579881,1.206012,-6.732089,8.732746,4.451042],[-4.329424,-3.747047,-1.412296,-7.285211,-8.277264,-9.199949,9.069480,4.874916],[8.319506,-2.169119,-8.191107,-0.081819,-0.646308,9.627219,-4.754365,0.466342],[0.428420,-2.550982,4.047887,5.452771,8.169963,5.872382,0.480166,-5.646054],[0.364267,-8.163207,4.394810,8.793863,1.266611,9.614195,0.276939,6.785896],[-3.059082,8.401236,-5.619435,-0.997165,-6.281365,-8.022556,-7.383707,-0.333897],[7.428515,-6.050347,7.314989,-9.762968,-9.888582,5.547816,-6.990854,8.678201],[-6.666536,6.546686,7.743069,-0.230577,7.107599,9.603150,8.303839,8.793515],[-5.210531,9.966442,6.238889,3.006015,4.360181,-0.624064,8.721897,-2.654102],[-0.784215,-2.797086,0.243191,1.239153,6.101459,4.266678,-1.680737,-1.558670],[-6.727644,2.881481,4.760328,8.294623,5.189293,4.586332,2.872643,-5.264708],[5.463489,-9.354071,9.159961,3.945488,-5.872738,9.269500,-7.998943,-0.468170],[6.158954,-7.809549,-2.959471,4.773675,0.159669,-2.663956,-8.418448,-5.602350],[0.261990,2.236916,-6.434817,5.555816,8.586004,-6.718201,-2.836607,-9.081824],[-4.832178,1.516885,-5.363180,-8.580863,6.224929,7.828903,9.900397,3.605357],[-2.551195,5.245140,5.381028,1.733313,3.197238,-6.321388,-2.538120,6.674333],[-7.269590,8.249989,0.251434,-4.513274,-3.261150,-9.456493,-1.626180,-3.951898],[-9.278808,4.030289,4.667511,-8.640531,-8.307808,-3.802426,1.312174,8.287694],[-0.581813,4.022880,-3.494610,-6.127131,1.126086,-5.757286,-0.199836,-6.425992],[-8.453570,7.309461,-4.833730,-8.914673,-6.382651,-1.573880,-8.110972,3.919003],[-2.085297,-3.583297,1.849905,-0.805773,-7.941893,-3.415573,5.722351,8.284221],[-9.045766,9.161061,7.269317,-4.570026,7.355299,9.638516,-2.651127,-2.817203],[7.640870,-3.515938,-0.642735,4.941728,5.337359,3.758934,-8.468933,6.100409],[7.010471,-8.387587,-1.066088,0.826664,4.315559,-4.178408,5.762127,-7.264282],[2.813595,5.902159,5.028470,-8.556028,-0.994861,-3.945463,2.958536,-7.909700],[-5.894632,5.582492,5.558440,-1.863708,4.757472,-8.066971,-9.399855,-7.320021],[9.491110,1.965378,-0.660503,-1.491224,7.526960,-6.229102,-6.793497,-7.483517],[5.451391,7.882198,-1.906235,4.633034,-0.192823,-0.993437,-4.576059,4.246348],[7.400600,7.967724,-7.028427,-1.660375,-2.444238,-4.316229,9.663184,7.622946],[-9.321010,9.648680,0.436305,3.945858,1.522218,-9.528255,-9.043288,5.056740],[-7.038121,6.253689,-6.577316,-1.113826,-3.704792,3.856640,6.160286,-0.752273],[-5.967912,-6.149274,-9.377392,0.903062,-1.931561,-1.015660,9.421727,-0.081960]], dtype = "float32")#candidate|4403|(40, 8)|const|float32
call_4400 = relay.TupleGetItem(func_2671_call(relay.reshape(const_4401.astype('uint32'), [384,]), relay.reshape(var_4402.astype('float32'), [576,]), relay.reshape(const_4403.astype('float32'), [320,]), ), 0)
call_4404 = relay.TupleGetItem(func_2675_call(relay.reshape(const_4401.astype('uint32'), [384,]), relay.reshape(var_4402.astype('float32'), [576,]), relay.reshape(const_4403.astype('float32'), [320,]), ), 0)
output = relay.Tuple([call_4377,call_4400,const_4401,var_4402,const_4403,])
output2 = relay.Tuple([call_4378,call_4404,const_4401,var_4402,const_4403,])
func_4405 = relay.Function([var_4402,], output)
mod['func_4405'] = func_4405
mod = relay.transform.InferType()(mod)
mutated_mod['func_4405'] = func_4405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4406 = relay.var("var_4406", dtype = "float32", shape = (2, 288))#candidate|4406|(2, 288)|var|float32
func_4405_call = mutated_mod.get_global_var('func_4405')
call_4407 = func_4405_call(var_4406)
output = call_4407
func_4408 = relay.Function([var_4406], output)
mutated_mod['func_4408'] = func_4408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_4412 = relay.TupleGetItem(func_3507_call(), 5)
call_4413 = relay.TupleGetItem(func_3509_call(), 5)
output = relay.Tuple([call_4412,])
output2 = relay.Tuple([call_4413,])
func_4421 = relay.Function([], output)
mod['func_4421'] = func_4421
mod = relay.transform.InferType()(mod)
mutated_mod['func_4421'] = func_4421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4421_call = mutated_mod.get_global_var('func_4421')
call_4422 = func_4421_call()
output = call_4422
func_4423 = relay.Function([], output)
mutated_mod['func_4423'] = func_4423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2822_call = mod.get_global_var('func_2822')
func_2824_call = mutated_mod.get_global_var('func_2824')
call_4435 = relay.TupleGetItem(func_2822_call(), 0)
call_4436 = relay.TupleGetItem(func_2824_call(), 0)
func_2099_call = mod.get_global_var('func_2099')
func_2102_call = mutated_mod.get_global_var('func_2102')
var_4438 = relay.var("var_4438", dtype = "int16", shape = (132, 1))#candidate|4438|(132, 1)|var|int16
call_4437 = relay.TupleGetItem(func_2099_call(relay.reshape(call_4435.astype('float32'), [3, 16, 6]), relay.reshape(var_4438.astype('int16'), [132,]), ), 0)
call_4439 = relay.TupleGetItem(func_2102_call(relay.reshape(call_4435.astype('float32'), [3, 16, 6]), relay.reshape(var_4438.astype('int16'), [132,]), ), 0)
output = relay.Tuple([call_4435,call_4437,var_4438,])
output2 = relay.Tuple([call_4436,call_4439,var_4438,])
func_4440 = relay.Function([var_4438,], output)
mod['func_4440'] = func_4440
mod = relay.transform.InferType()(mod)
var_4441 = relay.var("var_4441", dtype = "int16", shape = (132, 1))#candidate|4441|(132, 1)|var|int16
output = func_4440(var_4441)
func_4442 = relay.Function([var_4441], output)
mutated_mod['func_4442'] = func_4442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3370_call = mod.get_global_var('func_3370')
func_3372_call = mutated_mod.get_global_var('func_3372')
call_4473 = func_3370_call()
call_4474 = func_3370_call()
output = relay.Tuple([call_4473,])
output2 = relay.Tuple([call_4474,])
func_4479 = relay.Function([], output)
mod['func_4479'] = func_4479
mod = relay.transform.InferType()(mod)
output = func_4479()
func_4480 = relay.Function([], output)
mutated_mod['func_4480'] = func_4480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4076_call = mod.get_global_var('func_4076')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_4484 = func_4076_call()
call_4485 = func_4076_call()
func_4207_call = mod.get_global_var('func_4207')
func_4209_call = mutated_mod.get_global_var('func_4209')
call_4488 = relay.TupleGetItem(func_4207_call(), 0)
call_4489 = relay.TupleGetItem(func_4209_call(), 0)
output = relay.Tuple([call_4484,call_4488,])
output2 = relay.Tuple([call_4485,call_4489,])
func_4490 = relay.Function([], output)
mod['func_4490'] = func_4490
mod = relay.transform.InferType()(mod)
mutated_mod['func_4490'] = func_4490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4490_call = mutated_mod.get_global_var('func_4490')
call_4491 = func_4490_call()
output = call_4491
func_4492 = relay.Function([], output)
mutated_mod['func_4492'] = func_4492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3370_call = mod.get_global_var('func_3370')
func_3372_call = mutated_mod.get_global_var('func_3372')
call_4526 = func_3370_call()
call_4527 = func_3370_call()
output = call_4526
output2 = call_4527
func_4536 = relay.Function([], output)
mod['func_4536'] = func_4536
mod = relay.transform.InferType()(mod)
output = func_4536()
func_4537 = relay.Function([], output)
mutated_mod['func_4537'] = func_4537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2598_call = mod.get_global_var('func_2598')
func_2599_call = mutated_mod.get_global_var('func_2599')
call_4541 = func_2598_call()
call_4542 = func_2598_call()
output = call_4541
output2 = call_4542
func_4543 = relay.Function([], output)
mod['func_4543'] = func_4543
mod = relay.transform.InferType()(mod)
output = func_4543()
func_4544 = relay.Function([], output)
mutated_mod['func_4544'] = func_4544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3461_call = mod.get_global_var('func_3461')
func_3463_call = mutated_mod.get_global_var('func_3463')
call_4560 = relay.TupleGetItem(func_3461_call(), 1)
call_4561 = relay.TupleGetItem(func_3463_call(), 1)
var_4571 = relay.var("var_4571", dtype = "float64", shape = (11, 4, 3))#candidate|4571|(11, 4, 3)|var|float64
bop_4572 = relay.logical_or(call_4560.astype('bool'), relay.reshape(var_4571.astype('bool'), relay.shape_of(call_4560))) # shape=(11, 4, 3)
bop_4575 = relay.logical_or(call_4561.astype('bool'), relay.reshape(var_4571.astype('bool'), relay.shape_of(call_4561))) # shape=(11, 4, 3)
output = bop_4572
output2 = bop_4575
func_4578 = relay.Function([var_4571,], output)
mod['func_4578'] = func_4578
mod = relay.transform.InferType()(mod)
var_4579 = relay.var("var_4579", dtype = "float64", shape = (11, 4, 3))#candidate|4579|(11, 4, 3)|var|float64
output = func_4578(var_4579)
func_4580 = relay.Function([var_4579], output)
mutated_mod['func_4580'] = func_4580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3919_call = mod.get_global_var('func_3919')
func_3921_call = mutated_mod.get_global_var('func_3921')
call_4590 = func_3919_call()
call_4591 = func_3919_call()
output = relay.Tuple([call_4590,])
output2 = relay.Tuple([call_4591,])
func_4596 = relay.Function([], output)
mod['func_4596'] = func_4596
mod = relay.transform.InferType()(mod)
output = func_4596()
func_4597 = relay.Function([], output)
mutated_mod['func_4597'] = func_4597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4490_call = mod.get_global_var('func_4490')
func_4492_call = mutated_mod.get_global_var('func_4492')
call_4632 = relay.TupleGetItem(func_4490_call(), 1)
call_4633 = relay.TupleGetItem(func_4492_call(), 1)
uop_4649 = relay.tan(call_4632.astype('float64')) # shape=(12, 8, 9)
uop_4651 = relay.tan(call_4633.astype('float64')) # shape=(12, 8, 9)
func_2041_call = mod.get_global_var('func_2041')
func_2047_call = mutated_mod.get_global_var('func_2047')
var_4654 = relay.var("var_4654", dtype = "float32", shape = (12, 48))#candidate|4654|(12, 48)|var|float32
var_4655 = relay.var("var_4655", dtype = "uint32", shape = (24,))#candidate|4655|(24,)|var|uint32
var_4656 = relay.var("var_4656", dtype = "uint32", shape = (1, 384))#candidate|4656|(1, 384)|var|uint32
const_4657 = relay.const([False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True], dtype = "bool")#candidate|4657|(320,)|const|bool
call_4653 = relay.TupleGetItem(func_2041_call(relay.reshape(var_4654.astype('float32'), [576,]), relay.reshape(var_4655.astype('uint32'), [24,]), relay.reshape(var_4656.astype('uint32'), [384,]), relay.reshape(const_4657.astype('bool'), [5, 4, 16]), ), 5)
call_4658 = relay.TupleGetItem(func_2047_call(relay.reshape(var_4654.astype('float32'), [576,]), relay.reshape(var_4655.astype('uint32'), [24,]), relay.reshape(var_4656.astype('uint32'), [384,]), relay.reshape(const_4657.astype('bool'), [5, 4, 16]), ), 5)
func_4122_call = mod.get_global_var('func_4122')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_4668 = relay.TupleGetItem(func_4122_call(), 0)
call_4669 = relay.TupleGetItem(func_4124_call(), 0)
output = relay.Tuple([uop_4649,call_4653,var_4654,var_4655,var_4656,const_4657,call_4668,])
output2 = relay.Tuple([uop_4651,call_4658,var_4654,var_4655,var_4656,const_4657,call_4669,])
func_4676 = relay.Function([var_4654,var_4655,var_4656,], output)
mod['func_4676'] = func_4676
mod = relay.transform.InferType()(mod)
mutated_mod['func_4676'] = func_4676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4676_call = mutated_mod.get_global_var('func_4676')
var_4678 = relay.var("var_4678", dtype = "float32", shape = (12, 48))#candidate|4678|(12, 48)|var|float32
var_4679 = relay.var("var_4679", dtype = "uint32", shape = (24,))#candidate|4679|(24,)|var|uint32
var_4680 = relay.var("var_4680", dtype = "uint32", shape = (1, 384))#candidate|4680|(1, 384)|var|uint32
call_4677 = func_4676_call(var_4678,var_4679,var_4680,)
output = call_4677
func_4681 = relay.Function([var_4678,var_4679,var_4680,], output)
mutated_mod['func_4681'] = func_4681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_4702 = relay.TupleGetItem(func_2536_call(), 0)
call_4703 = relay.TupleGetItem(func_2538_call(), 0)
func_3144_call = mod.get_global_var('func_3144')
func_3146_call = mutated_mod.get_global_var('func_3146')
call_4718 = func_3144_call()
call_4719 = func_3144_call()
func_3963_call = mod.get_global_var('func_3963')
func_3968_call = mutated_mod.get_global_var('func_3968')
const_4754 = relay.const([-9,-5,5,-4,4,-3,-3,-1,-7,-8,10,-5,-2,2,-1,-7,7,3,5,-10,-1,-9,-2,-3], dtype = "uint32")#candidate|4754|(24,)|const|uint32
const_4755 = relay.const([[-10,1,-3,5,-2,1,-9,6,-10,-1,-6,10,5,-5,-3,10,-9,-7,1,8,3,7,-4,1,7,4,-5,5,-8,3,-7,-7,4,-9,-6,-8,8,10,-8,8,1,1,8,-5,8,8,-1,-2,-6,9,9,10,3,-9,-9,8,-9,-7,7,-3,-10,-10,3,9,4,3,7,1,3,3,-7,5,2,-4,4,3,6,8,-7,1,4,3,9,-1,5,6,5,-9,1,-7,9,-2,3,-6,-6,-2,-3,4,-10,-2,-9,7,8,-2,-7,8,8,3,-10,4,6,-10,10,10,-9,4,-1,-5,-5,1,-7,-10,-9,-8,3,-8,-5,-7,2,-4,-2,-2,-9,3,3,8,3,5,-4,-4,5,6,-10,-7,-2,3,9,-6,-2,2,3,5,1,-9,-5,10,2,-1,10,-5,9,6,-3,6,-9,1,2,7,8,-8,6,-6,-5,1,5,8,3,-3,4,4,-2,7,-2,7,10,-4,5,-7,7,6,5,7],[9,6,3,-9,4,-9,10,-6,-3,-7,10,-1,-3,8,-4,-5,7,6,-1,3,3,-2,9,-3,8,-3,5,3,2,5,-6,-8,-2,-3,1,8,9,7,8,4,-4,-4,2,9,1,-9,4,10,-2,-7,-10,-7,7,-8,-5,-2,-9,8,-4,-7,-10,-3,-6,8,-7,-10,-4,-5,10,5,-8,-4,3,-10,10,-3,-4,5,-9,-9,-2,5,-8,4,-6,5,5,-10,-3,7,-8,6,-5,3,5,-4,2,10,10,8,-6,7,-4,2,-7,-1,-7,8,-7,10,2,-7,-1,-2,5,-6,-5,-2,10,-6,-1,4,3,2,3,-2,-5,-7,9,9,1,5,-6,5,-1,7,-8,-1,-2,-1,-6,8,-3,10,-6,6,-2,-7,7,8,-3,-9,-3,3,5,10,8,-5,-5,-3,-5,10,9,8,9,4,-9,4,5,-9,1,4,-9,10,-7,5,-3,9,-2,8,3,5,4,7,-7,10,8,-9,6,-9,4,4]], dtype = "uint32")#candidate|4755|(2, 192)|const|uint32
var_4756 = relay.var("var_4756", dtype = "float32", shape = (64,))#candidate|4756|(64,)|var|float32
call_4753 = relay.TupleGetItem(func_3963_call(relay.reshape(call_4718.astype('float32'), [3, 16, 6]), relay.reshape(const_4754.astype('uint32'), [24,]), relay.reshape(const_4755.astype('uint32'), [384,]), relay.reshape(var_4756.astype('float32'), [16, 4]), ), 4)
call_4757 = relay.TupleGetItem(func_3968_call(relay.reshape(call_4718.astype('float32'), [3, 16, 6]), relay.reshape(const_4754.astype('uint32'), [24,]), relay.reshape(const_4755.astype('uint32'), [384,]), relay.reshape(var_4756.astype('float32'), [16, 4]), ), 4)
output = relay.Tuple([call_4702,call_4718,call_4753,const_4754,const_4755,var_4756,])
output2 = relay.Tuple([call_4703,call_4719,call_4757,const_4754,const_4755,var_4756,])
func_4774 = relay.Function([var_4756,], output)
mod['func_4774'] = func_4774
mod = relay.transform.InferType()(mod)
mutated_mod['func_4774'] = func_4774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4775 = relay.var("var_4775", dtype = "float32", shape = (64,))#candidate|4775|(64,)|var|float32
func_4774_call = mutated_mod.get_global_var('func_4774')
call_4776 = func_4774_call(var_4775)
output = call_4776
func_4777 = relay.Function([var_4775], output)
mutated_mod['func_4777'] = func_4777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3461_call = mod.get_global_var('func_3461')
func_3463_call = mutated_mod.get_global_var('func_3463')
call_4796 = relay.TupleGetItem(func_3461_call(), 1)
call_4797 = relay.TupleGetItem(func_3463_call(), 1)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_4798 = relay.TupleGetItem(func_3507_call(), 7)
call_4799 = relay.TupleGetItem(func_3509_call(), 7)
output = relay.Tuple([call_4796,call_4798,])
output2 = relay.Tuple([call_4797,call_4799,])
func_4800 = relay.Function([], output)
mod['func_4800'] = func_4800
mod = relay.transform.InferType()(mod)
output = func_4800()
func_4801 = relay.Function([], output)
mutated_mod['func_4801'] = func_4801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_4813 = relay.TupleGetItem(func_2536_call(), 0)
call_4814 = relay.TupleGetItem(func_2538_call(), 0)
output = relay.Tuple([call_4813,])
output2 = relay.Tuple([call_4814,])
func_4815 = relay.Function([], output)
mod['func_4815'] = func_4815
mod = relay.transform.InferType()(mod)
mutated_mod['func_4815'] = func_4815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4815_call = mutated_mod.get_global_var('func_4815')
call_4816 = func_4815_call()
output = call_4816
func_4817 = relay.Function([], output)
mutated_mod['func_4817'] = func_4817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_4838 = relay.TupleGetItem(func_1522_call(), 0)
call_4839 = relay.TupleGetItem(func_1524_call(), 0)
func_2099_call = mod.get_global_var('func_2099')
func_2102_call = mutated_mod.get_global_var('func_2102')
const_4845 = relay.const([1,-4,4,6,-5,9,-8,-2,-6,-10,6,-4,6,1,10,-7,-3,10,7,3,-8,10,1,-4,-9,-5,8,3,7,3,2,-8,3,2,5,1,-10,-1,3,10,-2,8,-6,3,-5,-1,-6,-1,7,8,1,-7,-10,-5,-4,4,10,3,5,9,2,-6,-9,9,4,-7,-9,-7,-1,-2,7,-2,-2,-5,2,-4,4,-5,10,-8,-3,9,-7,1,-1,6,2,7,4,-8,7,-3,5,3,-3,-10,-4,-10,-7,1,-5,6,-5,-1,6,-7,3,-4,-7,-4,8,9,-2,6,-10,-7,-6,-4,9,-1,-7,8,8,10,10,6,-7,3,3,-9,8,10], dtype = "int16")#candidate|4845|(132,)|const|int16
call_4844 = relay.TupleGetItem(func_2099_call(relay.reshape(call_4838.astype('float32'), [3, 16, 6]), relay.reshape(const_4845.astype('int16'), [132,]), ), 0)
call_4846 = relay.TupleGetItem(func_2102_call(relay.reshape(call_4838.astype('float32'), [3, 16, 6]), relay.reshape(const_4845.astype('int16'), [132,]), ), 0)
output = relay.Tuple([call_4838,call_4844,const_4845,])
output2 = relay.Tuple([call_4839,call_4846,const_4845,])
func_4855 = relay.Function([], output)
mod['func_4855'] = func_4855
mod = relay.transform.InferType()(mod)
output = func_4855()
func_4856 = relay.Function([], output)
mutated_mod['func_4856'] = func_4856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4217_call = mod.get_global_var('func_4217')
func_4219_call = mutated_mod.get_global_var('func_4219')
call_4889 = func_4217_call()
call_4890 = func_4217_call()
func_4536_call = mod.get_global_var('func_4536')
func_4537_call = mutated_mod.get_global_var('func_4537')
call_4898 = func_4536_call()
call_4899 = func_4536_call()
func_4207_call = mod.get_global_var('func_4207')
func_4209_call = mutated_mod.get_global_var('func_4209')
call_4916 = relay.TupleGetItem(func_4207_call(), 0)
call_4917 = relay.TupleGetItem(func_4209_call(), 0)
output = relay.Tuple([call_4889,call_4898,call_4916,])
output2 = relay.Tuple([call_4890,call_4899,call_4917,])
func_4920 = relay.Function([], output)
mod['func_4920'] = func_4920
mod = relay.transform.InferType()(mod)
output = func_4920()
func_4921 = relay.Function([], output)
mutated_mod['func_4921'] = func_4921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4240_call = mod.get_global_var('func_4240')
func_4241_call = mutated_mod.get_global_var('func_4241')
call_4966 = func_4240_call()
call_4967 = func_4240_call()
func_791_call = mod.get_global_var('func_791')
func_794_call = mutated_mod.get_global_var('func_794')
const_4969 = relay.const([-9.137450,-9.578739,-2.158934,9.694496,-3.163768,-3.463076,-6.360661,-7.831131,3.221341,5.639697,3.715652,8.663825,7.617364,9.208211,5.682851,4.312683,6.875988,6.124438,-7.571713,6.262395,9.731575,0.295798,-9.312790,-2.500492,-5.113247,6.967293,2.888407,4.081992,2.610570,5.793699,2.479033,-3.785700,-2.610174,-1.275930,-0.752550,3.124577,1.863111,-5.542488,9.703119,0.678085,-7.077318,4.423415,4.456116,-5.954776,4.701746,-8.765095,-7.093866,5.677993,-5.239830,8.459789,-7.003882,-2.776443,-8.343270,5.404245,7.470165,3.033737,8.142499,5.367127,-7.019568,3.668635,4.189787,-9.573974,-6.315843,-5.981813], dtype = "float32")#candidate|4969|(64,)|const|float32
const_4970 = relay.const([4.762371,1.644601,-9.546195,6.141979,9.608420,6.732290,2.901524,9.117455,-7.616760,6.929085,-1.374947,4.308446,0.882754,9.727537,-5.548928,-2.358734,-1.770181,5.437675,-6.466446,-7.658115,4.635468,-6.804313,-8.763380,-3.373289,-7.631830,-8.720289,3.498739,3.101003,-3.131195,0.659562,-4.710740,-4.934964,3.091818,6.028282,-7.982889,3.771626,-0.789010,-0.911576,-8.754774,9.378286,-4.740275,9.202546,-1.362864,-6.448647,-7.951077,3.641135,-9.926780,7.813712,6.872709,7.773191,5.199600,1.271220,2.359333,-0.257335,0.417984,-7.439730,-4.698871,3.873178,5.269059,4.760546,-4.563331,-8.454802,-5.766507,-2.532351,-4.169923,9.806806,4.774750,0.267618,-6.191230,-9.825565,-8.697279,3.729004,-3.265573,9.322792,-7.142978,4.117144,3.977909,9.903390,-6.556149,7.414161,-6.014254,-1.218227,1.515979,-6.179132,8.059880,3.965815,0.143191,-0.150550,-3.604072,2.510557,-9.329567,8.536049,-6.489079,6.016851,-8.534514,-9.960943,8.166342,-5.373326,-6.334623,-2.621846,1.553981,8.400378,-3.154409,9.836783,5.488587,-1.073888,1.550511,1.254134,-0.649500,-7.887573,3.551589,8.337370,9.276411,-9.097713,-8.720403,-5.488296,-6.972783,1.652960,3.445484,1.227060,9.257374,0.363673,5.607369,0.945673,1.728878,7.751862,-6.496994,-7.665977,-4.595931,2.303753,0.417402,2.229245,-0.475167,2.169796,5.232619,-6.137214,-2.483276,0.455080,1.536512,2.643368,6.963548,2.790600,-8.277494,6.833158,-9.986257,5.550685,-6.654531,-7.231282,3.401464,5.078905,-1.691980,-7.087388,6.120323,5.486440,-8.280669,0.704958,3.334328,8.076300,-0.456992,-0.012402,1.463742,6.750165,-0.603157,-7.039346,1.841907,-0.265715,-6.101365,-6.336894,2.665235,-6.989007,-5.232921,6.145032,-0.535204,3.289487,0.275235,-8.090296,-0.168058,4.550106,3.851653,-2.357661,4.220789,-5.902089,2.931321,3.372426,-5.362760,-3.263922,8.266378,-2.676915,-8.087947,1.899290,-4.857529,6.399291,3.996014,6.073701,-7.237704,0.482889,4.440323,1.467702,-4.100890,8.357643,-2.860607,0.493037,5.619992,-9.230336,-2.588987,2.408890,7.039346,1.316856,5.914964,9.611243,-9.460237,3.244726,-1.286107,3.204491,3.479524,-9.066527,-0.571630,-2.467695,7.267840,-1.997774,-8.966423,-6.850005,-4.815981,-5.304112,7.383818,2.511871,-9.979164,7.342891,-2.692797,3.944431,6.222524,3.904745,2.916706,9.365041,-4.576513,-7.375888,4.057708,-9.791445,-4.560658,-9.209040,-9.775698,-5.158921,-8.171800,-4.365152,-5.571575,1.615002,5.726326,4.934444,-1.841888,5.215789,-7.033182,4.013570,8.123908,3.394618,-0.327571,3.339443,-3.165096,7.093706,3.070368,9.027672,8.877618,0.789884,0.427836,2.442979,5.480417,8.148674,4.298762,4.720232,-2.423239,-3.964385,-7.043929,-8.087959,0.116211,-3.060288,0.326375,-6.427045,-5.891752,1.396979,0.887946,2.416661,9.811175,-3.664188,7.316674,7.009187,8.134934,-6.046708,1.482491,-1.995369,-3.074353,3.399101,-4.426358,-0.707071,4.986539,-3.190080,-7.297872,8.364548,-4.156823,-6.972342,-3.670351,-6.390049,-7.777631,1.375970,4.431937,-1.006672,-6.077701,6.861564,-5.724151,9.652507,6.501504,-4.303407,8.633458,3.454676,8.110512,1.615724,-8.326192,4.352893,-2.221328,-6.976061,-2.902242,3.318729], dtype = "float32")#candidate|4970|(320,)|const|float32
call_4968 = relay.TupleGetItem(func_791_call(relay.reshape(const_4969.astype('float32'), [1, 4, 16]), relay.reshape(const_4970.astype('float32'), [5, 4, 16]), ), 0)
call_4971 = relay.TupleGetItem(func_794_call(relay.reshape(const_4969.astype('float32'), [1, 4, 16]), relay.reshape(const_4970.astype('float32'), [5, 4, 16]), ), 0)
func_4122_call = mod.get_global_var('func_4122')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_4978 = relay.TupleGetItem(func_4122_call(), 0)
call_4979 = relay.TupleGetItem(func_4124_call(), 0)
bop_5007 = relay.mod(call_4966.astype('float64'), relay.reshape(call_4978.astype('float64'), relay.shape_of(call_4966))) # shape=(3, 16, 6)
bop_5010 = relay.mod(call_4967.astype('float64'), relay.reshape(call_4979.astype('float64'), relay.shape_of(call_4967))) # shape=(3, 16, 6)
func_2822_call = mod.get_global_var('func_2822')
func_2824_call = mutated_mod.get_global_var('func_2824')
call_5014 = relay.TupleGetItem(func_2822_call(), 0)
call_5015 = relay.TupleGetItem(func_2824_call(), 0)
output = relay.Tuple([call_4968,const_4969,const_4970,bop_5007,call_5014,])
output2 = relay.Tuple([call_4971,const_4969,const_4970,bop_5010,call_5015,])
func_5016 = relay.Function([], output)
mod['func_5016'] = func_5016
mod = relay.transform.InferType()(mod)
output = func_5016()
func_5017 = relay.Function([], output)
mutated_mod['func_5017'] = func_5017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mod.get_global_var('func_4536')
func_4537_call = mutated_mod.get_global_var('func_4537')
call_5033 = func_4536_call()
call_5034 = func_4536_call()
func_2099_call = mod.get_global_var('func_2099')
func_2102_call = mutated_mod.get_global_var('func_2102')
const_5050 = relay.const([7,-2,-4,4,-7,7,3,6,-3,-2,2,-9,2,-4,-7,1,-2,-8,4,-4,-1,1,-8,-5,-7,-7,6,3,-4,-2,-4,7,-6,4,9,2,-8,-1,1,-9,-3,-7,-4,7,-7,-3,2,9,-6,-7,-1,-2,-2,-5,-1,3,-1,-4,-3,7,2,3,9,-1,4,-10,8,4,-9,5,3,5,-10,-1,4,5,7,1,9,-2,1,-10,8,-1,2,8,-5,1,5,-10,-1,6,-10,-5,10,-4,3,-2,-7,-9,-2,-6,9,-4,-1,-3,9,2,6,-10,9,9,-7,3,5,-3,-9,4,6,4,4,10,9,-5,-1,3,-9,2,-5,-10,-8,-7], dtype = "int16")#candidate|5050|(132,)|const|int16
call_5049 = relay.TupleGetItem(func_2099_call(relay.reshape(call_5033.astype('float32'), [3, 16, 6]), relay.reshape(const_5050.astype('int16'), [132,]), ), 1)
call_5051 = relay.TupleGetItem(func_2102_call(relay.reshape(call_5033.astype('float32'), [3, 16, 6]), relay.reshape(const_5050.astype('int16'), [132,]), ), 1)
bop_5052 = relay.right_shift(call_5049.astype('uint8'), relay.reshape(const_5050.astype('uint8'), relay.shape_of(call_5049))) # shape=(11, 4, 3)
bop_5055 = relay.right_shift(call_5051.astype('uint8'), relay.reshape(const_5050.astype('uint8'), relay.shape_of(call_5051))) # shape=(11, 4, 3)
bop_5060 = relay.not_equal(call_5049.astype('bool'), relay.reshape(const_5050.astype('bool'), relay.shape_of(call_5049))) # shape=(11, 4, 3)
bop_5063 = relay.not_equal(call_5051.astype('bool'), relay.reshape(const_5050.astype('bool'), relay.shape_of(call_5051))) # shape=(11, 4, 3)
output = relay.Tuple([call_5033,bop_5052,bop_5060,])
output2 = relay.Tuple([call_5034,bop_5055,bop_5063,])
func_5074 = relay.Function([], output)
mod['func_5074'] = func_5074
mod = relay.transform.InferType()(mod)
output = func_5074()
func_5075 = relay.Function([], output)
mutated_mod['func_5075'] = func_5075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5016_call = mod.get_global_var('func_5016')
func_5017_call = mutated_mod.get_global_var('func_5017')
call_5090 = relay.TupleGetItem(func_5016_call(), 2)
call_5091 = relay.TupleGetItem(func_5017_call(), 2)
output = relay.Tuple([call_5090,])
output2 = relay.Tuple([call_5091,])
func_5098 = relay.Function([], output)
mod['func_5098'] = func_5098
mod = relay.transform.InferType()(mod)
output = func_5098()
func_5099 = relay.Function([], output)
mutated_mod['func_5099'] = func_5099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4207_call = mod.get_global_var('func_4207')
func_4209_call = mutated_mod.get_global_var('func_4209')
call_5174 = relay.TupleGetItem(func_4207_call(), 0)
call_5175 = relay.TupleGetItem(func_4209_call(), 0)
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_5180 = relay.TupleGetItem(func_2536_call(), 0)
call_5181 = relay.TupleGetItem(func_2538_call(), 0)
func_2501_call = mod.get_global_var('func_2501')
func_2505_call = mutated_mod.get_global_var('func_2505')
const_5183 = relay.const([-6.059699,-4.076409,-3.715642,2.321862,-5.508012,1.909226,6.218956,1.587542,-1.376092,2.645819,-2.588949,6.452293,5.033255,0.625446,6.412752,-6.981450,-1.134209,2.201025,-9.462129,-1.211933,8.768685,0.622627,-0.058728,6.860500,2.304765,-2.066008,-5.652401,7.360910,5.941363,-2.207666,-8.688332,1.985626,-1.186478,0.697318,6.769673,9.987600,8.409125,9.975679,-3.473264,2.531137,7.074701,7.958257,5.635479,3.040528,3.684969,0.089906,0.840470,-5.120908,1.621640,-1.336455,3.950695,-5.026241,-3.579968,-1.069319,-2.383892,-0.372710,1.473329,8.939742,-9.260512,-7.066295,-1.061264,6.318065,-2.352054,3.830406,-3.345146,-5.424486,-0.582021,-7.929757,-4.434662,8.729471,-8.101599,6.705594,4.325010,1.688025,4.124947,7.861791,6.605875,1.274824,-3.387784,-8.884539,-2.458619,-7.770220,6.649760,8.286333,0.460483,-9.498153,-7.701214,-6.735716,-8.784663,9.152781,8.966849,2.721542,-0.931997,-3.645035,-0.307562,6.654196,0.422251,6.313745,-0.517897,-3.541721,2.842974,-5.735829,-1.263419,5.586488,-0.286443,5.260923,7.271322,-8.576766,5.726026,-4.529312,0.304247,8.381935,8.262593,1.278825,7.937650,1.165386,-5.105150,5.431387,-9.765748,8.075290,5.266098,-3.335865,-5.617452,-5.353749,1.381391,7.941189,-0.801625,9.542116,3.648000,-4.419685,8.301126,1.325598,5.911342,-0.334960,8.635841,-1.737131,-2.376704,8.788177,8.420879,6.094845,-0.242158,-7.890253,9.415973,-6.296654,-4.944582,1.069269,-3.658525,-2.492833,4.274618,-1.009622,-7.470012,-1.271135,1.369326,4.804243,2.373849,-6.280091,1.960009,5.049822,-0.999154,4.408915,-1.884216,-9.507189,1.612215,-6.027929,-4.950177,7.295882,1.087698,8.097476,4.312652,9.445965,3.814877,-7.036244,-5.928134,1.623880,6.422215,-0.651175,-9.555905,8.314745,5.518306,-0.691750,-8.395665,-5.669071,9.781116,-8.022593,0.173103,-3.249053,4.980437,2.100208,-9.267303,3.810954,-1.067563,0.904618,-1.959566,-1.799443,-3.968182,9.308160,6.650652,-4.012216,-9.845801,9.038913,-2.748400,-4.953533,5.313449,-7.630413,1.268395,4.161044,0.256355,-4.337853,1.929935,2.783057,3.143688,-8.944539,-7.433813,-5.251102,-0.978786,-1.761739,2.160207,-9.451834,2.922527,-1.273674,-1.059506,-0.709932,-6.733587,-4.386793,5.849498,5.298605,-5.209251,9.060104,-9.661357,4.102458,-5.047006,5.083273,6.536361,-6.374350,-8.450674,8.482844,-6.858839,-6.725685,-6.957928,7.412757,-4.278544,-3.150159,-6.522613,-6.513244,6.749694,3.948210,9.649616,9.920358,4.029895,1.759187,-5.901741,-9.632136,-8.179801,0.938176,2.011860,2.663744,3.258522,7.186070,8.978857,-3.246010,6.007234,-0.293829,8.350648,2.422199,5.065813,-9.171902,8.215025,1.319644,-3.077422,-1.869056,8.130094,6.493679,-9.238897,-7.606973,-0.608685,-1.054276,2.354341,7.609436,5.017221,5.068063,7.802071,-2.785102,-1.002894,4.448473,7.377640,3.884912,7.770277,8.722405,3.338128,9.228427,1.333423,2.318375,8.125260,4.808708,-4.763290,4.153041,-7.857756,-2.013144,0.378669,2.464792,-3.513623,1.336669,-5.744814,8.010028,3.427893,7.886594,-0.281532,1.585128,5.024282,-5.076919,3.468969,-1.946758,-7.806040,-1.636231,-8.568431,-5.879599,-6.190090,-6.334536,-8.775728,-0.264659,-6.331576,-0.483450,5.592133,-6.532898,-2.036846,-0.932712,5.908252,-6.437321,1.119359,5.098303,-8.644663,-0.892277,-8.653686,6.191368,-7.925918,-4.086730,-9.764699,-9.478003,-9.470228,-5.228873,6.521611,-8.005822,3.657648,-2.996110,9.428139,-8.005803,8.847829,6.292998,5.717078,7.005418,-3.841912,2.493543,-1.302391,-1.988908,-0.357845,-8.202166,5.673417,-2.566342,9.355719,-4.900178,3.379529,-0.767412,0.086523,-6.965893,0.008824,8.202160,9.161791,-8.142091,-1.364501,-9.338004,4.773392,-4.218211,8.882420,-1.587672,-7.099848,7.887350,0.421302,-8.187054,2.168003,-6.631450,-8.295994,5.365921,-5.417903,-1.237070,-6.983097,5.285469,8.519657,9.444861,2.838959,6.574386,-9.458379,8.953490,-0.826222,-3.830509,-7.216835,-6.654280,-4.834735,-2.895935,1.420349,6.427750,1.667363,-0.528245,9.838312,2.697136,5.350827,-8.001539,1.892736,6.684679,1.601767,-8.112442,-5.971883,0.030824,-4.408727,4.074331,-1.528916,3.384236,-3.080810,-2.980565,2.344072,-8.345927,-8.517050,-0.970790,-7.662729,9.958699,-1.641419,4.111280,0.582663,2.477874,-1.904781,8.120877,-6.120749,-9.488437,-8.269756,-7.230806,-2.783411,-9.626624,9.901897,-9.768288,0.704373,0.053852,7.693973,-3.022267,9.931058,-5.126594,9.082728,-6.300365,0.254786,-8.733264,6.080673,8.317579,8.690675,-1.354054,3.754690,-3.217833,7.533974,-4.056823,-3.498162,0.164368,-8.553169,4.175342,3.376387,1.727823,-8.274200,5.380653,-8.572944,3.392130,-0.369578,-0.700222,-2.212866,-7.767495,5.737795,0.336339,-9.026410,8.900340,-9.268977,-9.732028,3.749220,-2.913276,0.214557,4.685933,1.831001,4.669496,0.278985,1.709815,-2.652178,3.688406,-4.603246,2.212147,0.001701,5.200291,0.052894,4.418278,-0.749400,-5.691772,3.890399,2.306403,-6.216747,4.229314,8.145979,5.363095,-3.381324,2.559218,1.009617,9.464391,9.532683,2.393651,-2.129014,6.143248,-6.396548,-8.042391,-2.155978,-3.456650,-1.311873,-5.542138,-3.234431,1.144548,-8.046243,4.206586,3.936073,-8.822123,-9.666485,6.790118,-7.012548,3.524842,-6.713565,9.534478,9.957076,4.732512,0.710487,7.011341,-9.235944,-8.943233,8.250927,-2.311088,5.500733,-2.738227,-3.018680,-0.471849,-7.475237,-1.971256,-6.366192,4.582937,9.527752,6.759717,-2.382836,9.378099,-9.557775,9.748671,5.347221,-4.218955,-2.120752,-6.041318,2.486638,-7.966594,-9.483500,-5.406117,-8.601640,5.293823,2.610405,-8.967614,2.738265,-0.694993,0.337984,-0.024810,3.364703,7.856073,0.165793,1.785249,6.350238,-6.842461,-8.245505,-3.522231,2.460560,-7.418316,-8.391897,-0.892042,-7.414744,5.181114,0.741250,4.733954,5.197419,-0.493605,-3.708114,5.010411,9.963750,-4.344004,-3.458124,-5.017333,-5.050591,-1.758308,9.350043,-3.910230,6.755121,-7.475241,9.534052,-7.882190,-5.663659,8.322974,-6.390386,-3.075498,1.832222,1.511324,5.540707,4.940913,-0.628948,6.971124,-3.298178,-2.174004,5.224565,-1.322805,-8.976333,1.175274,-3.687269,3.938517,0.369055,-9.334717,-4.652164,0.406972,-4.424695,3.280994,-4.833791,-8.027894,7.685394,0.558740,5.829823,1.236377,-1.908211,0.190376,-1.529721,6.211932,-2.579197,-3.848770,2.583178,3.039703,-4.293805,-8.559329,4.588373,9.075991,8.838514,6.392034,6.194641,-2.786484,-4.413605,-5.588887,1.620665,-4.608348,4.749713,-1.965554,-2.945543,-5.658099,1.348086,-8.935925,-3.454654,3.507635,-6.707830,-7.302273,3.859712,0.022799,-9.530659,-4.870932,3.956650,-5.935444,0.103636,5.533903,-4.370958,-4.728847,-4.060435,-4.853623,7.921850,1.864638,-5.025913,4.458785,-0.354405,1.983215,-9.163466,-5.963347,1.393713,-4.710170,-4.571800,-0.296845,-7.060306,-4.306624,5.986007,8.791847,-6.524789,-7.509259,-9.561034,-0.700387,-6.650466,-5.914777,-4.201450,-7.955835,7.739167,-2.461641,-1.606896,-5.562468,-0.678517,-8.412141,3.654406,-7.532241,-8.822820,-0.867261,-3.389292,8.550009,3.660412,9.320631,5.133266,3.289395,-2.119222,-6.231188,-4.125359,3.073390,9.618064,1.729651,2.145510,-7.022531,-3.163556,3.959317,9.527814,-5.516865,-1.872671,-9.117317,9.989739,-5.016562,-5.572578,7.573084,0.149786,2.829276,-4.977493,1.079253,-8.728754,4.582163,-3.241166,3.525141,4.802394,-1.577043,2.132197,7.385268,-6.558028,-5.860399,-2.900479,-4.669927,6.803310,-7.411093,-0.047420,1.821002,4.285330,7.265395,9.791437,-3.123312,-4.443410,-7.329943,7.745248,1.790001,4.388132,-6.767458,8.200937,1.099919,-5.746950,-8.749462,6.097129,7.748320,-8.873618,1.245269,0.161185,-1.746311,-8.025479,7.249183,2.687169,-0.581931,4.654859,-1.598621,3.996628,1.909003,-1.112372,-7.492992,9.445208,-2.376153,-4.810185,-7.894685,1.569095,-0.358430,8.706962,-6.740995,-2.682598,-5.728181,1.358229,-6.168691,-6.731085,2.078504,8.422626,9.512108,4.810083,-9.215660,5.972098,-5.114480,2.597985,-6.275970,-8.148526,9.144700,4.788214,-7.722007,3.051792,6.436883,-8.181376,-2.869310,-3.415733,4.545574,9.331769,-3.975640,-2.469317,-1.746535,0.076248,-6.016016,4.639164,-2.119563,1.587765,5.360001,4.936526,9.910805,9.985010,6.197055,0.370722,-7.072339,-2.469636,7.321558,1.751690,-6.933388,-4.767191,-9.224948,3.028474,2.191067,-4.615937,7.582082,9.514244,3.548649,-5.809873,3.435184,8.933409,-6.096917,-1.728338,-4.664753,0.110450,-2.428841,-2.044078,9.360641,1.466726,-5.769913,-2.973123,0.095746,-3.502609,-7.564223,1.096859,-9.124064,9.177076,-6.344064,-7.687879,3.568877,4.335095,-3.565149,5.276390,1.319711,-1.115730,-7.859856,3.868249,-0.655611,-7.694361,-6.771826,-0.028816,6.498994,-0.092834,8.071803,-8.447611,-0.288408,-7.057062,1.194735,7.749265,-7.703932,5.593381,-6.546603,-7.664355,-8.706661,3.613541,-2.698374,-2.297267,-4.480284,0.799619,5.826308,-0.506071,-5.438803,-1.977721,-9.205603,-5.658196,2.873514,0.508483,8.043200,4.588555,8.819902,-9.205563,-6.373062,3.258734,0.942963,1.928350,-4.221450,5.532441,-1.456981,3.100893,1.033935,-6.727213,4.813752,-4.580048,8.791049,-1.672451,-4.437389,1.772063,6.682311,2.785795,2.439762,-8.280867,9.975167,-6.315024,0.532279,-8.880918,-9.564870,-9.964784,0.060856,-3.524096,-5.013295,5.192748,8.193160,6.027308,8.537874,-8.535762,8.356344,-1.568423,-5.556604,0.733646,-3.084668,-3.843408,-1.581326,-8.578084,7.706613,-2.319732,-6.915260,-4.606586,-6.090231,-6.148659,0.132922,8.843576,9.841439,0.530546,-3.248653,-3.296176,-5.970011,7.663750,1.854633,-9.905580,-6.491152,-3.984070,-1.988935,8.449894,-6.962365,-5.286326,-7.736633,5.842745,-0.134888,8.271897,6.620681,0.298891,-9.393618,-9.216511,7.397341,-8.925176,7.892356,-1.819532,0.735310,3.128150,1.891225,4.536919,0.988608,-8.210045,3.061998,-6.158664,6.652075,8.443291,1.633928,8.905781,-2.755131,-9.269964,-1.508692,-4.594226,-8.739859,3.658294,8.468997,5.377064,6.180938,-1.292125,9.665431,9.216067,6.430619,-4.643031,-1.415272,4.953414,0.445356,2.895544,-9.333408,-9.098696,4.724380,-5.144283,-3.379515,1.279584,8.390939,4.699631,-5.027671,4.601785,5.094746,-6.839210,7.552534,-7.342794,-0.352318,-0.671608,1.855815,1.075571,0.329165,-5.669644,-8.803438,2.007931,6.241146,-0.613289,-3.681148,8.699184,-1.731313,2.882094,2.553214,-8.125395,5.281877,-8.412952,3.742707,7.697124,-2.548566,4.555157,7.542823,-4.437292,1.194262,2.376506,0.762729,6.004488,-0.378039,6.709336,-5.222472,9.299985,0.006177,6.280281,-3.552622,7.828015,-0.424082,5.669659,4.825666,-3.404866,-3.315251,-5.175575,9.249869,1.898612,3.596866,4.699609,6.678657,0.798410,7.848494,9.692945,-3.802835,-2.108054,3.401494,-8.461816,2.773781,2.774256,-8.898320,2.193209,1.236843,-7.963892,-2.441374,4.523890,-9.459885,-4.123817,0.943918,6.847258,-6.786119,-8.773233,4.585254,-8.997354,4.063941,6.794847,-7.118384,5.086733,5.597926,-7.147176,-0.907330,0.721891,-0.951368,-4.771244,-7.261390,1.755336,2.492192,-0.847988,4.457748,6.588928,7.730533,-8.069000,-9.481809,7.222902,4.482375,4.771460,9.484365,4.787539,-9.248250,5.226599,1.410867,4.417528,-2.102654,-1.327786,-8.039270,2.622347,-4.732189,5.434249,6.771158,-6.149484,-6.212146,-5.671247,5.933391,-3.660432,6.215108,-1.634742,-5.933008,9.409058,6.171003,-8.702581,-2.356116,1.932343,-1.082411,6.308619,-7.809016,-4.562774,3.338167,-7.869928,-2.612511,-2.414854,5.535162,7.813558,-8.069243,-8.455347,-6.001275,2.664738,-8.846770,9.468417,-4.960658,1.576303,-0.474826,7.306317,-4.118269,-2.530344,-6.471617,0.336746,0.714024,-5.027582,9.279700,-0.508978,6.249004,-4.598441,-5.782117,-3.352405,-3.296229,7.901894,-5.105232,-1.901463,1.479800,9.514639,0.300956,0.267438,4.094185,-2.743903,-2.998621,-6.371115,1.501930,-7.603798,-3.480241,-4.571944,-7.978992,-5.069265,-2.289554,5.515236,2.929473,-5.994554,6.624361,-6.365314,9.612441,-2.287651,2.278173,3.353123,6.778819,-5.897153,2.560607,3.349823,8.298117,-9.652215,-3.524642,7.834996,-0.918635,1.877201,3.990838,6.744808,-0.331853,-3.242341,-7.886254,-8.784997,0.513866,-6.807057,4.430142,-0.748668,6.330932,8.955144,7.627421,4.713493,-9.760995,9.180751,-9.544852,-4.555280,-4.519971,-0.642705,-4.329890,2.524781,-3.951417,-1.822190,7.238378,-5.344894,1.711062,-2.803244,-3.797654,6.020561,-2.234216,-6.894601,8.699456,-2.437324,9.040643,-3.643108,7.350728,-5.847371,3.571208,-3.159662,5.073333,0.011274,-3.939306,9.502173,-1.330584,6.460564,-6.904427,6.301719,-9.884391,6.833090,9.267328,4.281303,2.965433,-7.067691,6.548144,8.561710,6.037499,3.264328,2.511438,-2.855360,8.703325,-8.190538,5.191454,3.976634,0.232843,3.154765,5.336911,-8.678656,-6.436066,9.193551,9.347619,6.053132,-6.663240,-9.354860,5.807374,1.374193,-0.020054,-6.183924,8.672451,2.265518,6.735423,3.174836,4.477212,6.139707,-1.380729,7.870113,-3.195025,-6.934193,-6.590299,-0.282352,6.051481,-8.751757,4.484361,8.433812,5.563836,-7.137466,-1.480625,8.730273,3.755606,0.873210,4.634769,5.379228,8.798191,-4.188039,-0.201100,-8.536035,-1.045631,0.533834,9.153851,7.897254,4.889722,4.258899,1.318279,4.016001,-2.297333,3.414924,-1.348304,3.504359,-0.433974,9.844811,-4.144243,8.662592,-9.202646,-8.774597,1.376330,-3.234237,2.100896,-3.101600,-7.117339,2.489272,9.425005,4.194159,1.275239,5.675150,-2.270675,-5.796859,-1.196702,-5.093623,-5.242516,3.256604,-3.808329,-4.913946,7.749401,-3.196582,7.710562,-3.963310,-9.181323,-9.297686,-0.964176,-0.816107,-3.997244,5.194242,-3.606641,1.458658,8.948294,-2.450840,8.571715,5.041483,-5.060980,-3.716519,-6.806889,-0.259702,-5.662669,-5.450589,-7.694849,-4.689336,-4.347874,-0.943834,7.315327,4.601751,-5.896913,-3.074208,0.973755,-4.995230,4.941861,9.351187,-8.876167,5.115203,-1.685963,4.392473,-3.654435,5.740403,-7.016463,7.223612,7.440566,-8.293199,-8.143165,1.725207,-8.295861,2.080225,7.301900,4.775094,-2.035438,-8.405877,9.525312,-2.993311,7.978669,-1.386051,3.701321,2.020545,-3.446386,-3.052280,-4.535402,-9.966623,9.166697,0.467594,-0.286429,-6.358155,6.116562,8.486406,2.531461,-0.548140,1.869969,-2.431693,-8.606857,-9.376150,0.106807,2.818682,-6.163061,-2.510836,-8.222376,-7.637116,8.825778,1.248521,-6.743002,4.175027,-1.239993,-4.594738,-0.248793,-5.096004,4.372996,3.334946,0.819832,-4.121906,1.550548,-3.726314,-9.069544,-2.813773,2.019543,-7.989312,5.622240,5.254695,8.096906,5.226555,-0.510313,-8.110627,-0.906133,-3.646907,4.283598,-9.748008,-0.751038,-8.365724,7.163664,-5.162837,-9.376314,-2.797534,-5.256732,-9.039707,-3.109597,9.305178,6.924610,-8.335414,5.361484,-0.745316,9.534511,1.420191,2.440071,8.627425,0.486743,9.956801,-4.876834,5.762478,-7.150759,3.788233,3.081915,0.681339,-3.808794,8.870852,5.993627,-7.903845,-6.064660,-1.752444,9.885695,-8.948672,1.827227,1.678274,-7.168946,-0.779307,-6.195739,3.750571,-6.959396,-0.420887,-7.708750,-8.536703,7.599591,-0.981455,1.197436,5.369825,-3.613737,6.351002,-5.592394,-0.808197,6.890180,4.482554,-2.210494,3.451967,0.780251,3.618715,7.138976,3.745610,3.247387,-1.277747,-5.894621,4.764532,-9.212792,-0.283603,9.138308,2.335142,4.919333,-4.548573,1.544470,-5.011861,-6.316390,-8.079731,-5.040527,-7.671582,2.693686,-0.647651,4.573454,1.540234,-9.295679,-7.805580,-5.583814,-9.271646,-6.195857,1.345911,-3.306486,-6.964396,2.951958,8.183369,1.700667,1.622316,-2.208390,-3.489674,-2.782511,5.474936,-3.613464,-6.533223,6.996743,-0.367540,-4.784135,7.552383,-4.182892,7.595010,-6.954619,9.418281,-0.258944,8.708194,-9.237704,-9.917625,4.025184,7.772352,5.095979,-7.381849,-1.402708,-2.101960,-9.857945,7.186905,-5.482591,-3.916826,4.317696,-6.132316,9.422625,9.336477,4.839191,-6.295613,7.889371,-1.243426,7.806287,-0.945366,-7.431548,-3.667413,-2.889505,8.988853,-9.716209,-3.082080,7.791439,-9.332344,-6.961785,-2.221679,1.655137,-4.072694,-5.860561,-6.526690,3.159411,5.881746,9.953578,-9.265714,6.785233,-7.368279,5.839273,-8.047558,0.454615,6.896651,-2.585478,-0.524721,-1.381860,-9.345739,8.733705,3.589333,3.180702,-3.707076,-4.170289,6.489366,-9.286621,-2.369696,-3.921294,-1.772535,1.355732,0.398989,0.397493,1.784815,-9.115450,-2.019337,-4.044805,-0.563980,-3.549588,5.231806,4.500660,0.835487,-4.320912,3.128070,-2.116557,6.108910,-9.207180,1.363151,-0.335655,9.591757,-4.909831,-1.613198,0.684979,4.535742,-0.792604,2.370282,4.136554,1.069191,-5.806099,-5.409926,1.866505,-0.805628,-4.985709,6.306107,-4.967015,5.147682,5.446773,-3.364080,-8.285952,-0.827934,-8.627248,-3.912512,-0.498503,5.256291,-8.291923,8.535693,8.011257,4.835947,6.333487,-8.035854,-7.280212,7.762526,-7.363874,-3.998691,9.154821,2.659161,-3.227573,5.147380,0.857993,8.360137,-0.697681,2.912607,-3.086361,7.047761,-7.890451,-4.339342,8.745430,-6.201025,4.761646,-4.285598,2.068817,-4.220728,3.227928,4.742770,-9.562447,-5.323146,3.164803,2.815432,4.661621,-8.293218,-4.222524,-4.316466,-6.277008,2.386729,3.294278,-5.800884,5.168208,0.628262,-6.279679,-2.117668,3.137020,4.916360,-2.842893,5.633308,3.094174,6.590241,-8.254920,8.083066,-9.748100,-9.666422,-6.355673,3.007785,4.856364,-9.390290,9.641234,-2.098139,3.501648,8.521943,-5.212338,4.946761,-7.023549,-1.463001,-6.457439,0.972306,-9.837665,6.126841,-4.938459,4.120633,3.008046,7.281856,-3.205781,7.032385,0.648684,3.434256,3.950816,0.999711,-8.177596,-5.660104,2.339222,3.596170,6.940232,-0.852276,5.065856,7.886836,6.894134,3.016552,8.247373,-3.248249,-3.087637,-3.672992,-0.450407,2.764686,8.469099,-9.782811,-4.815416,0.800141,-8.527993,0.210487,6.078035,-5.560402,-5.356906,-6.954159,-4.336745,-6.997705,-7.169921,2.082222,4.243791,6.839997,-3.797620,9.288043,-9.593814,0.692333,8.404110,-0.077733,1.407495,4.814764,4.057896,0.737602,-4.519384,-4.100017,6.643564,-2.413746,-6.027851,5.781553,0.428947,9.525274,5.011778,-5.206484,-9.977059,1.506598,5.167434,7.441417,-7.936608,-8.684925,-1.679558,-7.452164,-3.621434,-6.905493,-6.945558,-6.855835,7.092329,9.721975,-2.561087,6.033567,3.126489,-3.806139,9.204401,4.894294,0.358503,4.900992,-3.602132,3.832502,-4.808354,1.497550,0.260864,-2.494123,-7.467534,-0.749264,0.015953,4.693502,-6.521084,4.827699,0.023786,-6.424837,-4.954143,-5.103098,5.260338,-3.551965,-5.569827,-5.272633,0.693446,-0.505617,5.683266,-3.579193,-3.784504,4.354356,2.887052,-2.605549,8.312965,4.324843,-7.596739,-8.435980,0.943374,1.465556,-1.905944,-3.839694,-5.175920,4.230963,8.360401,-5.815597,6.792390,-3.061086,-5.117150,7.166153,8.944599,-8.491163,9.628330,1.769632,3.913719,-0.850522,9.394773,0.464938,4.920878,8.329165,-3.655503,-7.567566,7.351271,-6.301242,8.952189,6.145136,4.086883,8.449392,-9.015093,0.332785,1.216174,5.002227,-5.771192,4.117257,-9.259880,-9.917384,-9.365891,-3.437046,-8.832875,-3.873053,4.381552,-7.985221,2.792866,5.322767,3.094148,1.784019,-6.601819,2.946568,1.147527,-9.420255,0.040029,-0.970194,6.874207,5.838780,3.417675,5.161982,7.055512,5.118485,8.727895,-5.158023,-2.744674,-2.974080,-0.431482,0.734072,-6.950348,4.822843,2.160527,2.538409,8.549454,-6.494227,-4.065583,7.365047,7.551450,-9.941703,4.526787,4.535638,-8.907363,-9.063402,5.284254,-3.813162,3.597866,5.445358,8.529443,3.408248,2.385252,-1.941884,8.267622,9.083149,-2.297584,-5.366035,-1.620458,7.816556,4.680627,-7.979355,-6.875559,-8.584524,-6.406521,-5.290249,-9.433780,-5.545265,5.625027,-3.561532,-9.440165,6.739822,6.202241,-4.652228,-8.796769,4.347567,1.007765,-8.612620,-4.932821,9.075468,7.664634,6.391309,7.803621,5.258638,-0.526537,-2.803076,-8.064432,2.918365,2.975868,4.462884,-7.693820,1.039498,-2.578540,7.576205,-8.904452,-2.338230,-8.618672,5.716096,7.302569,-6.902337,-2.009844,5.568337,-3.467816,7.398139,-2.442909,7.457999,2.689088,7.383923,3.928306,-9.210830,1.944628,6.430128,-6.910528,-9.638150,2.595814,0.965373,8.180674,-2.009547,-4.464920,3.226372,7.274528,1.637041,1.107159,-5.502031,3.045932,-4.254117,0.413525,-0.704495,-2.430869,-3.854857,7.815462,-8.617419,-4.075125,-9.487440,-8.134701,4.450803,1.256350,-8.425923,2.390789,7.334593,4.360502,-3.242728,4.061753,1.853517,5.986943,0.982960,7.766181,0.903564,2.300206,-1.485221,1.190971,4.417118,-7.975895,6.005939,-8.279098,-9.630027,-3.707960,4.071465,5.694391,6.842306,-5.023974,6.464892,-8.345671,0.199467,2.040416,6.874813,4.005982,6.825103,-8.286241,-7.557399,5.420972,6.537569,7.050597,9.727491,8.505104,5.842733,7.407343,0.315575,4.382913,5.862886,1.152577,8.288315,3.784109,-9.525824,0.728755,1.608454,-5.289127,-8.618555,3.388860,-6.550766,-8.580636,-4.671859,1.557109,-1.343528,-6.829857,8.965910,-0.735424,-5.810219,3.243796,-8.912744,5.149574,6.118330,-3.497128,8.352307,2.788289,-5.047894,9.298832,0.399020,-0.506769,6.153917,-6.493751,-8.452668,8.136231,-4.019669,-1.955235,3.946772,-7.866429,7.880065,-8.286392,-4.765171,-5.082536], dtype = "float32")#candidate|5183|(2112,)|const|float32
var_5184 = relay.var("var_5184", dtype = "float32", shape = (576,))#candidate|5184|(576,)|var|float32
var_5185 = relay.var("var_5185", dtype = "float32", shape = (64,))#candidate|5185|(64,)|var|float32
call_5182 = relay.TupleGetItem(func_2501_call(relay.reshape(const_5183.astype('float32'), [11, 16, 12]), relay.reshape(var_5184.astype('float32'), [576,]), relay.reshape(var_5185.astype('float32'), [64,]), ), 3)
call_5186 = relay.TupleGetItem(func_2505_call(relay.reshape(const_5183.astype('float32'), [11, 16, 12]), relay.reshape(var_5184.astype('float32'), [576,]), relay.reshape(var_5185.astype('float32'), [64,]), ), 3)
func_3802_call = mod.get_global_var('func_3802')
func_3805_call = mutated_mod.get_global_var('func_3805')
call_5192 = relay.TupleGetItem(func_3802_call(relay.reshape(call_5180.astype('bool'), [3, 16, 6])), 2)
call_5193 = relay.TupleGetItem(func_3805_call(relay.reshape(call_5180.astype('bool'), [3, 16, 6])), 2)
output = relay.Tuple([call_5174,call_5180,call_5182,const_5183,var_5184,var_5185,call_5192,])
output2 = relay.Tuple([call_5175,call_5181,call_5186,const_5183,var_5184,var_5185,call_5193,])
func_5197 = relay.Function([var_5184,var_5185,], output)
mod['func_5197'] = func_5197
mod = relay.transform.InferType()(mod)
var_5198 = relay.var("var_5198", dtype = "float32", shape = (576,))#candidate|5198|(576,)|var|float32
var_5199 = relay.var("var_5199", dtype = "float32", shape = (64,))#candidate|5199|(64,)|var|float32
output = func_5197(var_5198,var_5199,)
func_5200 = relay.Function([var_5198,var_5199,], output)
mutated_mod['func_5200'] = func_5200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_5225 = relay.TupleGetItem(func_3234_call(), 0)
call_5226 = relay.TupleGetItem(func_3235_call(), 0)
func_2501_call = mod.get_global_var('func_2501')
func_2505_call = mutated_mod.get_global_var('func_2505')
var_5245 = relay.var("var_5245", dtype = "float32", shape = (2112,))#candidate|5245|(2112,)|var|float32
const_5246 = relay.const([9.468658,-1.603264,-9.115551,7.967358,2.845835,1.665890,-9.947663,-0.590101,2.047398,-8.565939,-9.569018,-6.532907,-4.456167,-6.761017,2.735063,-2.172403,-4.195815,-1.732975,2.030921,0.012901,-2.182649,-6.690805,3.465852,-5.135080,-9.737369,0.555842,-2.805802,-9.794349,3.378683,-8.576812,0.058464,-0.239827,5.040450,-8.028358,-1.645156,7.371360,-6.061418,2.139696,-5.215712,5.850090,7.892613,-2.301230,-8.698040,-6.986387,6.439710,-9.997931,6.450659,-9.085829,-2.025453,2.837976,7.751237,5.764779,-9.868791,8.119668,-7.353419,5.806311,9.075454,6.993535,-6.374325,-7.377496,-1.815595,-5.812877,8.737152,-5.397298,-0.230174,-2.537454,-6.468531,3.973250,4.002045,-7.255207,8.527309,6.843301,2.358308,3.677104,-6.436567,0.309143,-2.919281,-3.094995,5.565427,5.303239,-8.926387,3.790861,8.694567,8.939051,0.907384,3.393147,3.369159,-6.403192,6.779799,5.608589,9.215532,9.497315,-0.904492,3.193889,-4.937490,2.896316,-9.646930,-3.474580,-4.394194,-5.154415,1.782744,-2.640902,-2.047569,7.453249,-3.313901,0.726126,8.366023,-4.849024,-8.697108,4.061167,-7.270971,3.699184,3.434067,4.073527,8.791563,-2.846217,9.184687,-7.996249,8.595139,0.473395,-6.984420,0.358807,2.681830,3.974731,8.663916,2.690907,-5.450767,-1.899205,-9.270092,7.259856,-9.595830,-3.099169,-4.262278,3.251994,-1.136394,-3.108790,-7.974819,-7.208643,1.560064,6.739275,5.230873,-2.797110,-8.004849,2.605943,-3.612224,-9.924083,-6.581085,-1.891280,5.383076,-6.741617,0.258933,-8.150516,-4.283843,8.376662,2.699762,-4.729597,1.369842,-0.622770,-2.586615,-2.811507,-0.932347,9.388182,6.335747,0.034630,3.890368,-8.422821,-0.577051,-2.709679,-6.551096,-0.779311,7.043810,-8.634028,-3.257369,-4.185428,-0.239072,1.234755,5.091135,-4.268183,0.649396,-2.932380,5.440443,5.681557,2.380395,9.114835,6.874352,6.667449,-7.117340,-4.363767,-4.102124,8.444684,7.992626,2.666402,8.914931,-3.921374,-6.194455,-7.796173,0.192991,7.489938,0.306810,-1.560352,3.938102,8.793291,8.764069,-4.223756,-4.114502,7.605379,-9.008619,7.333489,-4.017751,-5.186318,-4.846583,-7.762877,-1.244507,-4.882180,-4.549325,1.171212,1.751206,-2.388172,-4.584422,-1.823705,-5.524672,-5.793915,6.121580,0.879070,4.734496,-1.906881,-0.652418,-3.128982,-8.328506,-5.124226,5.999333,-9.076753,7.413816,-6.987447,0.805969,-6.803101,-2.047712,0.812253,-2.302118,0.689373,-5.403638,7.050320,-6.164152,-6.680404,6.393161,-9.254086,-6.689068,0.754503,8.373263,2.565370,-4.064857,-9.803144,-9.624999,-1.005437,-2.075337,5.969426,5.020505,9.043187,-3.132048,0.110588,3.515137,-6.536315,-6.679844,3.358761,9.136624,1.710631,-4.061879,-1.710693,5.348953,-2.424211,-8.822998,-5.853613,-7.620902,-2.465813,1.828834,-4.645678,3.229624,-5.590752,-9.553991,6.245117,-1.879568,-7.848804,-4.075974,-5.622143,9.511875,-6.293383,-3.901735,-7.695918,-9.751606,1.303472,-7.082084,-5.906573,-1.284815,6.581550,-7.392601,6.828199,8.537161,-0.883199,-3.291039,3.242656,1.063680,-8.355973,4.895900,-2.071833,3.726041,5.586635,-6.216990,0.649573,2.721179,6.957260,2.205785,-5.039558,-3.326226,-4.075077,2.578983,9.793505,4.145706,-7.522676,-8.923856,6.662301,-8.754352,4.235906,-9.603959,-5.764350,9.326875,-5.305834,-9.560953,-0.597960,8.791065,6.554089,-5.852118,8.706781,-8.657808,-8.287391,-2.871034,-8.766066,9.539437,9.630492,-3.702164,9.167428,-1.573179,-5.761652,-4.235350,5.104975,-1.574607,0.416331,6.783829,-2.390143,-9.724026,-8.147015,-0.808649,-5.222959,-4.632655,-7.698899,0.795539,8.991620,0.256314,-8.253478,-4.008410,3.633069,-4.844381,8.139538,4.715275,-5.735458,2.566906,-2.702307,4.178848,2.667180,6.692821,4.372984,4.014809,-1.638399,-8.141046,-7.954814,-9.946894,8.965319,-0.671079,3.865864,2.225312,-4.769205,-2.320312,-6.220045,7.123904,-1.013540,9.007733,0.341970,-0.121502,1.792782,-3.871961,8.723712,2.286767,3.199143,9.990365,9.106709,-8.558497,7.102230,0.979081,2.306510,5.482910,5.820312,9.485073,8.412001,-6.656164,-2.822856,7.600054,7.111444,7.841904,-7.162367,1.556842,2.518441,4.706420,3.559795,-1.253668,8.628141,-3.538658,6.744183,6.285293,0.860309,6.505235,-3.153596,9.646626,-5.702712,5.306327,7.882134,-4.681370,-4.382287,-7.930520,-8.700361,-7.307592,-0.806296,-8.665885,-3.766347,8.248334,8.973922,-8.230850,7.740031,-7.362220,-2.982244,-6.871126,-6.864449,-7.254761,1.797217,-1.940248,1.428274,5.111897,9.631380,6.753414,-5.370564,5.485185,-1.328683,8.549156,1.328202,7.190109,6.870276,-4.555161,-6.028487,6.709998,5.627002,-1.770443,-8.592187,-0.388382,1.941743,-5.322147,-4.241189,-1.329809,1.001564,-0.509998,3.407642,-5.871862,-0.790879,-0.934329,5.695955,-3.879303,-4.765827,3.481821,-6.995364,-9.206123,-1.302783,1.590967,7.952819,1.222444,-5.321727,9.237255,8.134902,-2.670237,-0.231445,-3.516530,-0.359541,-4.062973,2.995783,-0.196411,-0.773718,-1.726815,4.770954,3.770984,7.572974,1.399763,2.503993,5.179038,-7.865706,-7.553990,-1.749689,-4.487101,5.972444,7.502555,-7.340797,-9.332062,6.099969,0.437339,8.789736,1.510472,1.036849,-1.590784,9.574431,3.876228,0.514714,5.865559,6.683004,1.959486,-8.219146,4.891252,-3.021923,9.594748,-7.509479,-5.613099,-6.658376,-5.489134,-1.626852,-1.175498,-1.703372,1.573258,0.616812,-2.036913,-6.923895,3.646361,-8.479796,4.999476,-7.151693,-4.593593,-6.375384,-3.334757,-1.969546,-3.064804,3.005834,2.997126,8.022603,-5.559226,7.108653,2.601485,-1.029382,-2.320599,8.934815,3.884151,3.027586,3.514641,-9.216632,-8.688331,-2.115687,5.530883,5.836415,-5.441494,8.013779,4.368765,4.620185,-7.986750,2.039405,-8.148027,-4.246423,-8.353129,-6.576195,1.279006,-1.515001,6.906685,3.886736,-3.462518,2.688545], dtype = "float32")#candidate|5246|(576,)|const|float32
const_5247 = relay.const([2.701144,6.701205,-6.971073,6.008011,0.774299,-0.169358,9.383262,1.048009,4.320209,-7.368633,0.948327,8.591311,-1.421779,-4.237040,6.446794,-7.462278,-0.863539,-7.950049,-5.799918,5.525523,-1.603453,6.822493,-7.175965,-1.928745,-5.766521,6.977568,-3.627065,-0.973562,8.826050,-3.818068,-2.679731,-2.144780,-8.581029,-3.124800,-6.481161,6.623437,3.895023,-3.184958,1.359500,-0.189788,6.325396,1.464563,-4.755789,-4.700092,-7.056464,1.946509,6.568812,1.550653,-8.833353,-6.676273,-7.306513,8.804999,-7.793926,0.432912,9.038263,-7.582611,1.023794,-3.553719,4.926552,-9.963624,-6.061802,-4.543496,6.750038,6.530285], dtype = "float32")#candidate|5247|(64,)|const|float32
call_5244 = relay.TupleGetItem(func_2501_call(relay.reshape(var_5245.astype('float32'), [11, 16, 12]), relay.reshape(const_5246.astype('float32'), [576,]), relay.reshape(const_5247.astype('float32'), [64,]), ), 9)
call_5248 = relay.TupleGetItem(func_2505_call(relay.reshape(var_5245.astype('float32'), [11, 16, 12]), relay.reshape(const_5246.astype('float32'), [576,]), relay.reshape(const_5247.astype('float32'), [64,]), ), 9)
uop_5249 = relay.asin(call_5225.astype('float32')) # shape=(10, 2, 13)
uop_5251 = relay.asin(call_5226.astype('float32')) # shape=(10, 2, 13)
const_5285 = relay.const([[[9.553612,-0.902804,-7.386653,-2.385067,8.610427,-3.823296,-2.989302,-0.436148,-0.026513,8.341925,3.138345,9.286144,-4.710408],[-5.580678,-1.239483,9.642572,-3.774142,6.015158,9.792215,1.086490,-9.303479,1.023978,6.892979,4.652975,-7.624752,7.540307]],[[4.854715,-0.881704,6.331158,-3.106603,0.169933,8.223508,8.736034,-6.353767,-6.633684,7.157650,-7.698098,0.988134,9.639367],[3.329288,7.633443,5.201103,9.013543,5.420747,-7.794025,-2.354256,1.583828,-8.278427,-1.823838,5.610393,-1.440940,-3.874863]],[[9.897181,-5.024783,-1.414234,-3.686227,-0.314367,-3.134702,8.331337,-3.520673,8.757407,2.459334,-3.964555,9.462463,3.982085],[9.790779,-4.403930,-4.901473,1.840488,-7.698034,-3.204567,-0.838343,-9.553828,-7.870803,-9.258632,-1.116122,4.880205,-1.762419]],[[9.346769,6.059801,-6.830790,-9.117606,-9.148255,-5.044294,-6.938074,3.702784,6.526286,2.794977,4.207119,1.583574,7.056600],[8.954544,-8.011168,-1.316475,-3.715571,-8.101770,2.309962,2.753972,0.003760,9.799391,-0.672720,-3.713898,-6.972105,9.193319]],[[3.254424,1.164754,-6.814920,1.325007,-8.516596,-4.508760,8.261580,3.108433,-7.079603,-8.805348,-2.915395,3.463601,2.818560],[-0.296941,4.476380,7.960412,9.553009,1.115996,7.740503,-9.846236,8.906930,-5.223886,3.931494,8.818924,-0.493650,2.556928]],[[6.498886,5.656204,-2.637602,0.744249,-1.927354,-6.528867,1.732874,3.808245,-4.917609,7.612480,6.266388,8.991560,7.042578],[-6.690097,-6.350269,9.026734,-6.036737,-4.338537,-3.502252,-1.400088,-1.843583,-9.919745,1.661069,6.426255,9.947191,8.842209]],[[-3.738101,5.995386,2.154289,-0.635200,6.280656,7.454925,-2.442796,-9.338618,0.532132,7.102893,9.238700,-5.592319,-6.999148],[2.773884,-5.306278,-9.560378,2.702256,-1.987907,3.980236,-1.967111,-4.353135,-4.194994,-7.602830,-8.488634,4.180742,4.261524]],[[7.453494,4.817149,1.262538,-4.160008,6.519266,5.188615,-8.346615,9.525184,-4.743152,0.884005,-8.358658,2.537925,-9.815926],[-1.264964,-6.128055,3.255173,5.269102,5.501853,2.876059,-6.187249,-5.602650,0.219727,-1.638365,-8.657619,-1.208381,6.482977]],[[7.662195,8.746915,-7.303312,7.200546,-5.106393,5.718386,-3.704162,-3.904338,-6.507319,-0.650689,-6.182551,7.730969,6.207983],[1.967179,0.376938,-4.322510,-4.848168,0.307895,6.743723,3.295217,8.748411,-7.730623,8.470769,5.796519,7.037733,-4.540615]],[[6.066720,-2.282941,4.661443,-5.473373,2.520958,8.488074,2.762691,-7.873668,2.574247,-0.608474,-6.330384,-5.943599,7.440648],[8.817791,-8.448025,3.807454,-4.506522,-5.203959,7.329562,-3.451155,3.477512,-5.692916,-9.317520,2.233143,-1.380872,-1.543818]]], dtype = "float32")#candidate|5285|(10, 2, 13)|const|float32
bop_5286 = relay.less(uop_5249.astype('bool'), relay.reshape(const_5285.astype('bool'), relay.shape_of(uop_5249))) # shape=(10, 2, 13)
bop_5289 = relay.less(uop_5251.astype('bool'), relay.reshape(const_5285.astype('bool'), relay.shape_of(uop_5251))) # shape=(10, 2, 13)
output = relay.Tuple([call_5244,var_5245,const_5246,const_5247,bop_5286,])
output2 = relay.Tuple([call_5248,var_5245,const_5246,const_5247,bop_5289,])
func_5306 = relay.Function([var_5245,], output)
mod['func_5306'] = func_5306
mod = relay.transform.InferType()(mod)
mutated_mod['func_5306'] = func_5306
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5307 = relay.var("var_5307", dtype = "float32", shape = (2112,))#candidate|5307|(2112,)|var|float32
func_5306_call = mutated_mod.get_global_var('func_5306')
call_5308 = func_5306_call(var_5307)
output = call_5308
func_5309 = relay.Function([var_5307], output)
mutated_mod['func_5309'] = func_5309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4217_call = mod.get_global_var('func_4217')
func_4219_call = mutated_mod.get_global_var('func_4219')
call_5326 = func_4217_call()
call_5327 = func_4217_call()
func_5016_call = mod.get_global_var('func_5016')
func_5017_call = mutated_mod.get_global_var('func_5017')
call_5328 = relay.TupleGetItem(func_5016_call(), 1)
call_5329 = relay.TupleGetItem(func_5017_call(), 1)
output = relay.Tuple([call_5326,call_5328,])
output2 = relay.Tuple([call_5327,call_5329,])
func_5353 = relay.Function([], output)
mod['func_5353'] = func_5353
mod = relay.transform.InferType()(mod)
output = func_5353()
func_5354 = relay.Function([], output)
mutated_mod['func_5354'] = func_5354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_5359 = func_1537_call()
call_5360 = func_1537_call()
func_5197_call = mod.get_global_var('func_5197')
func_5200_call = mutated_mod.get_global_var('func_5200')
var_5362 = relay.var("var_5362", dtype = "float32", shape = (576,))#candidate|5362|(576,)|var|float32
var_5363 = relay.var("var_5363", dtype = "float32", shape = (64,))#candidate|5363|(64,)|var|float32
call_5361 = relay.TupleGetItem(func_5197_call(relay.reshape(var_5362.astype('float32'), [576,]), relay.reshape(var_5363.astype('float32'), [64,]), ), 0)
call_5364 = relay.TupleGetItem(func_5200_call(relay.reshape(var_5362.astype('float32'), [576,]), relay.reshape(var_5363.astype('float32'), [64,]), ), 0)
func_3802_call = mod.get_global_var('func_3802')
func_3805_call = mutated_mod.get_global_var('func_3805')
call_5368 = relay.TupleGetItem(func_3802_call(relay.reshape(call_5359.astype('bool'), [3, 16, 6])), 0)
call_5369 = relay.TupleGetItem(func_3805_call(relay.reshape(call_5359.astype('bool'), [3, 16, 6])), 0)
func_4440_call = mod.get_global_var('func_4440')
func_4442_call = mutated_mod.get_global_var('func_4442')
var_5378 = relay.var("var_5378", dtype = "int16", shape = (132,))#candidate|5378|(132,)|var|int16
call_5377 = relay.TupleGetItem(func_4440_call(relay.reshape(var_5378.astype('int16'), [132, 1])), 1)
call_5379 = relay.TupleGetItem(func_4442_call(relay.reshape(var_5378.astype('int16'), [132, 1])), 1)
uop_5380 = relay.log10(call_5361.astype('float64')) # shape=(12, 8, 9)
uop_5382 = relay.log10(call_5364.astype('float64')) # shape=(12, 8, 9)
var_5393 = relay.var("var_5393", dtype = "float64", shape = (12, 8, 9))#candidate|5393|(12, 8, 9)|var|float64
bop_5394 = relay.bitwise_xor(uop_5380.astype('uint16'), relay.reshape(var_5393.astype('uint16'), relay.shape_of(uop_5380))) # shape=(12, 8, 9)
bop_5397 = relay.bitwise_xor(uop_5382.astype('uint16'), relay.reshape(var_5393.astype('uint16'), relay.shape_of(uop_5382))) # shape=(12, 8, 9)
uop_5403 = relay.sin(bop_5394.astype('float64')) # shape=(12, 8, 9)
uop_5405 = relay.sin(bop_5397.astype('float64')) # shape=(12, 8, 9)
output = relay.Tuple([call_5359,var_5362,var_5363,call_5368,call_5377,var_5378,uop_5403,])
output2 = relay.Tuple([call_5360,var_5362,var_5363,call_5369,call_5379,var_5378,uop_5405,])
func_5409 = relay.Function([var_5362,var_5363,var_5378,var_5393,], output)
mod['func_5409'] = func_5409
mod = relay.transform.InferType()(mod)
mutated_mod['func_5409'] = func_5409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5409_call = mutated_mod.get_global_var('func_5409')
var_5411 = relay.var("var_5411", dtype = "float32", shape = (576,))#candidate|5411|(576,)|var|float32
var_5412 = relay.var("var_5412", dtype = "float32", shape = (64,))#candidate|5412|(64,)|var|float32
var_5413 = relay.var("var_5413", dtype = "int16", shape = (132,))#candidate|5413|(132,)|var|int16
var_5414 = relay.var("var_5414", dtype = "float64", shape = (12, 8, 9))#candidate|5414|(12, 8, 9)|var|float64
call_5410 = func_5409_call(var_5411,var_5412,var_5413,var_5414,)
output = call_5410
func_5415 = relay.Function([var_5411,var_5412,var_5413,var_5414,], output)
mutated_mod['func_5415'] = func_5415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_5447 = relay.TupleGetItem(func_3234_call(), 0)
call_5448 = relay.TupleGetItem(func_3235_call(), 0)
output = call_5447
output2 = call_5448
func_5452 = relay.Function([], output)
mod['func_5452'] = func_5452
mod = relay.transform.InferType()(mod)
mutated_mod['func_5452'] = func_5452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5452_call = mutated_mod.get_global_var('func_5452')
call_5453 = func_5452_call()
output = call_5453
func_5454 = relay.Function([], output)
mutated_mod['func_5454'] = func_5454
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5463 = relay.var("var_5463", dtype = "uint32", shape = (11, 3, 11))#candidate|5463|(11, 3, 11)|var|uint32
var_5464 = relay.var("var_5464", dtype = "uint32", shape = (11, 3, 11))#candidate|5464|(11, 3, 11)|var|uint32
bop_5465 = relay.right_shift(var_5463.astype('uint32'), relay.reshape(var_5464.astype('uint32'), relay.shape_of(var_5463))) # shape=(11, 3, 11)
func_4196_call = mod.get_global_var('func_4196')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_5468 = relay.TupleGetItem(func_4196_call(), 0)
call_5469 = relay.TupleGetItem(func_4197_call(), 0)
func_2501_call = mod.get_global_var('func_2501')
func_2505_call = mutated_mod.get_global_var('func_2505')
var_5483 = relay.var("var_5483", dtype = "float32", shape = (2112,))#candidate|5483|(2112,)|var|float32
const_5484 = relay.const([-2.219435,1.549602,8.144152,4.338090,4.827506,8.543598,-8.823093,1.249187,2.511781,8.338461,-2.372081,1.094154,-8.978534,0.259341,-1.835431,3.251966,3.584354,2.569819,-7.049932,4.799378,1.637280,6.854624,9.982748,-7.824829,-1.672983,9.789292,0.988584,6.580536,5.478143,7.844140,-5.909139,2.960942,4.728435,-1.256982,5.837581,8.263528,-5.837411,-3.202771,7.520732,-2.192190,-2.791567,9.438194,-0.564508,-9.588206,2.674087,-0.905436,-8.908189,0.432229,-8.255137,-6.533902,-1.177110,-1.244799,-9.273958,-8.891149,-8.504696,9.080691,5.816848,-3.405653,-6.897756,3.383758,4.760364,1.760088,8.626744,9.033449,-2.488334,1.536255,-0.745125,7.352825,9.114027,-3.741154,-8.176777,-3.254066,-6.532894,3.033953,9.595437,6.595859,-4.074966,8.570034,5.285778,0.945585,-1.674352,-4.493792,5.512686,3.215978,-4.270789,-5.654318,2.267732,-9.511359,0.631013,-4.521133,-4.079041,2.769661,-9.300636,1.419382,-8.642950,0.915297,2.334086,1.132540,8.950950,8.777202,-1.252559,-5.060659,7.505993,-5.342618,4.730183,8.446960,-5.684194,-6.472222,3.407101,-6.902454,0.623665,-8.461873,-9.006725,0.947209,-9.843766,6.137715,-6.911579,8.265462,-2.345050,-4.935740,-9.822883,8.648424,5.021571,-4.303171,2.899755,-0.264374,-4.980466,-3.650701,-7.551556,9.469542,-4.714587,6.955416,-0.423262,-5.170820,-3.186226,-6.152823,4.365845,3.805996,-6.764651,4.164729,2.437197,-3.052263,0.157035,-4.875941,-7.270030,-4.840909,-9.516300,2.130984,-7.275774,5.496706,-5.509230,-0.443178,6.766429,-4.926308,2.844012,-5.568931,4.147054,-8.035391,2.203387,-7.281752,-1.951796,-2.229071,4.171159,-5.235448,-9.749175,-1.680000,8.883700,-5.564285,3.073249,-6.666361,-8.334373,3.551325,5.425335,-3.768427,-0.799565,-0.913847,-7.031459,4.478270,-5.623987,1.597149,0.644919,-8.766019,-9.484144,7.800073,3.672229,-7.178441,-0.230751,-7.698418,-9.728135,-5.523834,8.065224,8.318730,-0.910325,1.626114,-3.984732,7.948327,1.946029,4.090508,-2.913737,3.303308,-1.302683,9.125760,1.038512,6.172139,1.889371,-0.869359,-2.072833,-6.404526,-5.626728,-7.316187,-1.562437,-9.180858,4.976650,-0.513009,-0.670380,6.945075,1.197855,-8.160804,-4.936467,-7.557100,7.000118,0.656853,6.325619,-5.934268,4.098082,-8.733741,-8.716247,4.352258,-4.182238,1.346991,0.644107,-6.467503,-0.499439,4.399428,-1.664312,-1.465623,-4.501320,9.857312,0.944359,7.318073,-7.494066,-1.300723,-7.626750,-7.197272,7.926658,-8.477928,2.622644,-5.387453,0.352773,-4.765565,1.537443,4.523661,-4.640272,6.699892,4.187629,2.077690,4.658026,-0.880775,3.713532,-8.234068,2.800710,-4.804396,0.801202,-7.658640,-0.080504,-4.366620,5.596247,-6.880563,2.739605,5.181008,-5.605193,-7.933884,-9.740671,-0.261720,-0.881069,1.354839,8.615988,-1.030239,-9.775884,6.562846,5.139639,-4.180786,7.417768,5.123055,6.347626,7.308499,2.663822,0.502844,6.545917,7.533619,-9.475930,6.899170,-5.725581,6.158785,-9.410014,-3.557115,-8.574268,-3.507062,1.528437,-8.220129,-5.950942,-2.718693,-4.484649,9.402180,4.369186,4.156873,6.316843,0.918473,-7.920741,-6.421619,4.024343,-6.681210,-7.867748,-2.087639,-5.705488,-5.146205,-0.736550,-5.530168,-3.498429,-3.507658,7.392559,9.481764,-9.724076,-9.199085,1.378097,2.688161,1.829381,2.300699,-7.843984,3.950587,-8.385156,4.577272,9.562523,3.083007,-0.978968,7.027176,2.078092,-0.597124,-3.316789,-2.864448,-5.827104,-6.673772,-0.554807,8.622088,8.029570,0.028190,-3.000741,1.747823,8.045989,8.984085,-7.307629,4.283652,4.162228,-0.855264,-2.233151,-2.603635,-0.951073,4.283413,-8.184107,-3.195683,8.189754,4.740044,-3.315612,1.462413,-3.643470,8.961784,-2.693323,-1.326647,1.440470,3.342423,-5.105599,-2.195409,-1.872243,5.466313,-5.648312,9.752123,0.606904,3.953118,5.892437,5.228810,7.897392,-4.961063,4.124264,6.981265,8.464391,8.202678,-9.259544,2.421004,2.661909,4.752114,-2.456157,1.863574,-1.316262,5.339816,-4.363831,9.056749,-4.415051,6.055525,-2.509057,-7.899481,0.578963,9.707130,2.498697,-2.044445,9.605790,-7.584636,-7.050397,-3.002120,-7.321462,-1.169694,-3.068070,-5.821192,-7.219527,9.824329,-7.889699,-2.334583,2.715531,-8.638576,-7.442272,1.550181,-3.117357,8.107297,4.757696,1.546851,-3.646634,-6.030703,2.078147,1.901546,-1.080876,5.813355,-0.522392,-4.282202,1.637085,-0.783293,-1.684857,-6.183825,0.543746,6.882643,2.345887,-0.039197,2.656728,-4.947942,9.256504,-2.746465,-2.896753,-2.591552,3.710540,-6.967216,2.274902,5.402686,-5.472465,7.673942,4.323210,4.302133,4.823711,-4.990843,-6.979020,-7.037801,-1.817788,-3.403101,-6.549261,8.329942,1.122564,-9.304000,-8.436646,-8.604734,2.566395,-2.325023,6.527180,5.721370,2.802856,5.169575,2.272157,4.351912,-5.357634,-8.590442,3.213563,-8.853128,-7.579851,5.706572,-3.421074,2.334022,8.709734,2.819711,3.823464,-3.239619,-7.848712,7.768810,1.665745,-4.144459,-3.592459,-8.814065,-5.713566,-7.737315,9.626224,-5.539232,-6.669005,-4.997676,7.531790,-6.142486,-4.832778,-0.252363,-8.935115,-7.261945,-6.126580,5.328521,-9.314438,-7.390216,-9.971017,1.346739,2.684841,-6.585240,1.304876,8.554112,-4.530985,-4.604606,-6.813901,7.181068,-2.372550,-5.791488,-0.248240,3.749339,8.118350,-8.177485,-6.762808,-4.188395,2.979905,8.348245,5.646537,3.780665,-9.338175,-1.231310,-8.907759,4.385163,-7.948751,-1.602615,9.037197,2.303268,3.573390,3.107680,0.391434,1.929006,-1.246159,8.543869,-0.258687,8.462846,-5.857865,2.158298,4.683541,2.946271,7.401517,5.542019,4.710612,3.779738,-7.148512,1.107532,-2.649756,-7.482418,8.923749,-9.534180,-4.938663,0.530399,-8.865506,-9.508319,6.912870,9.091046,8.820729,-2.630532,8.673205,3.808203,-9.661555,2.755229,-8.496769,6.367406,0.176830,8.767573], dtype = "float32")#candidate|5484|(576,)|const|float32
const_5485 = relay.const([5.048800,7.699551,5.283372,5.250051,8.538948,-6.362931,-2.190562,-1.208607,-6.260372,7.252464,8.541258,-6.099099,2.698488,7.890228,-0.984360,-7.067743,-7.094109,3.042457,-0.433153,-0.770401,-6.787206,-3.933222,-4.670981,2.842882,-1.872412,3.474964,4.601278,-9.294962,8.689902,7.502965,-9.057586,-4.180873,7.149774,6.512661,-2.651017,-5.909583,-3.620195,0.058834,2.768164,2.302968,-0.993681,-6.605105,-2.726930,-2.317669,-2.982470,-9.443407,7.322774,4.444626,-1.181672,-3.996760,-6.916616,5.428174,8.979870,6.734438,4.127667,-0.985187,-6.370914,3.432557,0.314393,-6.803708,3.277447,3.996039,7.909180,3.483064], dtype = "float32")#candidate|5485|(64,)|const|float32
call_5482 = relay.TupleGetItem(func_2501_call(relay.reshape(var_5483.astype('float32'), [11, 16, 12]), relay.reshape(const_5484.astype('float32'), [576,]), relay.reshape(const_5485.astype('float32'), [64,]), ), 7)
call_5486 = relay.TupleGetItem(func_2505_call(relay.reshape(var_5483.astype('float32'), [11, 16, 12]), relay.reshape(const_5484.astype('float32'), [576,]), relay.reshape(const_5485.astype('float32'), [64,]), ), 7)
output = relay.Tuple([bop_5465,call_5468,call_5482,var_5483,const_5484,const_5485,])
output2 = relay.Tuple([bop_5465,call_5469,call_5486,var_5483,const_5484,const_5485,])
func_5505 = relay.Function([var_5463,var_5464,var_5483,], output)
mod['func_5505'] = func_5505
mod = relay.transform.InferType()(mod)
var_5506 = relay.var("var_5506", dtype = "uint32", shape = (11, 3, 11))#candidate|5506|(11, 3, 11)|var|uint32
var_5507 = relay.var("var_5507", dtype = "uint32", shape = (11, 3, 11))#candidate|5507|(11, 3, 11)|var|uint32
var_5508 = relay.var("var_5508", dtype = "float32", shape = (2112,))#candidate|5508|(2112,)|var|float32
output = func_5505(var_5506,var_5507,var_5508,)
func_5509 = relay.Function([var_5506,var_5507,var_5508,], output)
mutated_mod['func_5509'] = func_5509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4596_call = mod.get_global_var('func_4596')
func_4597_call = mutated_mod.get_global_var('func_4597')
call_5518 = relay.TupleGetItem(func_4596_call(), 0)
call_5519 = relay.TupleGetItem(func_4597_call(), 0)
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_5529 = relay.TupleGetItem(func_2536_call(), 0)
call_5530 = relay.TupleGetItem(func_2538_call(), 0)
output = relay.Tuple([call_5518,call_5529,])
output2 = relay.Tuple([call_5519,call_5530,])
func_5544 = relay.Function([], output)
mod['func_5544'] = func_5544
mod = relay.transform.InferType()(mod)
output = func_5544()
func_5545 = relay.Function([], output)
mutated_mod['func_5545'] = func_5545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4855_call = mod.get_global_var('func_4855')
func_4856_call = mutated_mod.get_global_var('func_4856')
call_5549 = relay.TupleGetItem(func_4855_call(), 1)
call_5550 = relay.TupleGetItem(func_4856_call(), 1)
func_1832_call = mod.get_global_var('func_1832')
func_1837_call = mutated_mod.get_global_var('func_1837')
const_5556 = relay.const([[10,3,1,-3,2,-10,4,-6],[7,1,-8,-8,-8,1,10,1],[9,-5,-5,-1,-10,2,10,-3],[2,10,2,-9,2,10,-9,-4],[-4,-9,9,-5,-2,5,7,-8],[3,10,-10,4,1,4,6,8],[-10,8,-8,10,-2,-5,-4,9],[-3,-1,-10,-4,10,10,-9,5],[-5,9,-5,-7,-6,5,5,5],[5,-2,-2,5,-6,7,3,-5],[6,6,-4,8,5,-2,-9,8],[-5,-8,-7,-9,8,-8,-10,1],[-8,-7,10,-4,3,5,3,8],[2,-4,-9,-1,3,-7,-4,-10],[7,-9,-5,4,-1,9,-2,3],[-3,4,2,-8,-7,-9,-5,-5],[6,-3,-9,8,6,3,6,-2],[2,2,3,10,-5,1,10,6],[2,-9,-6,10,-8,-10,8,5],[9,-6,5,10,-9,-4,1,-6],[-9,5,-4,7,-9,-8,8,8],[1,8,10,-10,3,7,-3,-8],[-10,6,-9,7,10,4,9,5],[-6,9,-3,4,-10,9,-5,-6],[9,8,4,5,-1,2,-2,3],[10,-5,-9,-10,-1,-4,5,1],[1,1,5,9,-6,9,8,6],[-1,4,10,-3,-2,-7,-7,2],[-8,-5,-8,2,-7,-9,-10,-4],[6,3,1,-6,4,-1,-2,1],[5,-6,10,6,6,2,-2,8],[-4,3,8,-10,5,-3,4,8],[8,4,-1,-5,6,4,4,8],[-5,-5,2,-5,-9,-3,-10,6],[-6,-6,-9,-5,-6,6,5,10],[-5,-2,2,-2,-6,8,6,4],[2,-1,8,-7,7,6,7,1],[-1,-9,-10,6,5,-2,5,5],[5,-10,1,9,1,9,1,10],[-5,-7,-7,3,-8,-5,10,-2],[-3,7,-10,-4,-4,-8,5,1],[4,-6,-2,5,5,-2,-7,9],[-5,-5,-5,-5,-2,-5,9,-8],[3,-4,-5,4,-8,-5,1,6],[-2,-10,-10,7,-5,10,6,9],[-1,4,-3,-6,-5,7,-6,-1],[-5,-7,-5,6,5,-6,-1,-2],[-7,8,7,10,-6,-7,9,1]], dtype = "uint32")#candidate|5556|(48, 8)|const|uint32
var_5557 = relay.var("var_5557", dtype = "float32", shape = (576,))#candidate|5557|(576,)|var|float32
const_5558 = relay.const([-3.317147,-3.472820,-7.247159,-0.948007,5.507965,6.831354,-6.116367,1.807803,-8.809671,2.965528,-0.549238,-7.168662,-4.828366,-5.367189,-8.175248,-7.863807,-0.991387,2.924158,-7.351296,-0.824856,-6.784972,-8.492124,8.276423,-5.975923,-6.372162,4.793998,5.392965,7.280607,0.738310,1.811646,-6.402312,2.907502,-0.995143,-5.053438,-8.248737,-0.708459,-7.456451,0.828130,6.221340,-9.533985,-2.429570,-6.674312,1.090446,4.411826,4.399554,9.852844,1.546413,6.673687,2.247108,-8.005888,-3.173743,3.182504,-1.538902,-2.993471,-0.608911,9.595712,-1.951072,-7.910091,-0.552586,-9.400356,-5.262543,3.415286,-8.241498,-4.312346], dtype = "float32")#candidate|5558|(64,)|const|float32
var_5559 = relay.var("var_5559", dtype = "float32", shape = (320,))#candidate|5559|(320,)|var|float32
call_5555 = relay.TupleGetItem(func_1832_call(relay.reshape(const_5556.astype('uint32'), [384,]), relay.reshape(var_5557.astype('float32'), [576,]), relay.reshape(const_5558.astype('float32'), [64,]), relay.reshape(var_5559.astype('float32'), [160, 2]), ), 0)
call_5560 = relay.TupleGetItem(func_1837_call(relay.reshape(const_5556.astype('uint32'), [384,]), relay.reshape(var_5557.astype('float32'), [576,]), relay.reshape(const_5558.astype('float32'), [64,]), relay.reshape(var_5559.astype('float32'), [160, 2]), ), 0)
func_4855_call = mod.get_global_var('func_4855')
func_4856_call = mutated_mod.get_global_var('func_4856')
call_5569 = relay.TupleGetItem(func_4855_call(), 2)
call_5570 = relay.TupleGetItem(func_4856_call(), 2)
func_4076_call = mod.get_global_var('func_4076')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_5604 = func_4076_call()
call_5605 = func_4076_call()
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_5610 = relay.TupleGetItem(func_2536_call(), 0)
call_5611 = relay.TupleGetItem(func_2538_call(), 0)
output = relay.Tuple([call_5549,call_5555,const_5556,var_5557,const_5558,var_5559,call_5569,call_5604,call_5610,])
output2 = relay.Tuple([call_5550,call_5560,const_5556,var_5557,const_5558,var_5559,call_5570,call_5605,call_5611,])
func_5614 = relay.Function([var_5557,var_5559,], output)
mod['func_5614'] = func_5614
mod = relay.transform.InferType()(mod)
mutated_mod['func_5614'] = func_5614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5614_call = mutated_mod.get_global_var('func_5614')
var_5616 = relay.var("var_5616", dtype = "float32", shape = (576,))#candidate|5616|(576,)|var|float32
var_5617 = relay.var("var_5617", dtype = "float32", shape = (320,))#candidate|5617|(320,)|var|float32
call_5615 = func_5614_call(var_5616,var_5617,)
output = call_5615
func_5618 = relay.Function([var_5616,var_5617,], output)
mutated_mod['func_5618'] = func_5618
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5695 = relay.var("var_5695", dtype = "float32", shape = (5, 10, 8))#candidate|5695|(5, 10, 8)|var|float32
uop_5696 = relay.asin(var_5695.astype('float32')) # shape=(5, 10, 8)
output = relay.Tuple([uop_5696,])
output2 = relay.Tuple([uop_5696,])
func_5701 = relay.Function([var_5695,], output)
mod['func_5701'] = func_5701
mod = relay.transform.InferType()(mod)
mutated_mod['func_5701'] = func_5701
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5702 = relay.var("var_5702", dtype = "float32", shape = (5, 10, 8))#candidate|5702|(5, 10, 8)|var|float32
func_5701_call = mutated_mod.get_global_var('func_5701')
call_5703 = func_5701_call(var_5702)
output = call_5703
func_5704 = relay.Function([var_5702], output)
mutated_mod['func_5704'] = func_5704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_5856 = relay.TupleGetItem(func_1522_call(), 1)
call_5857 = relay.TupleGetItem(func_1524_call(), 1)
func_2753_call = mod.get_global_var('func_2753')
func_2758_call = mutated_mod.get_global_var('func_2758')
var_5880 = relay.var("var_5880", dtype = "float32", shape = (576,))#candidate|5880|(576,)|var|float32
const_5881 = relay.const([7.952881,8.604092,7.047136,-7.978192,-1.277589,-1.010911,4.533739,-3.020170,7.357570,4.381103,5.291470,-0.767184,-0.144696,-0.777029,-3.550612,9.008955,7.584257,-1.774964,-8.608703,5.667424,8.418887,-0.593985,-0.603006,5.097951,6.101011,3.913221,5.980536,-5.502159,-9.603106,2.927737,-8.235648,9.582909,-2.800364,-2.395950,-1.962791,6.705342,-6.701499,-3.363755,9.895219,-6.502722,-8.677880,5.288549,3.122846,-6.742871,-9.027438,-1.063884,-7.701483,3.904516,8.760699,-4.039316,7.626051,0.925258,4.749198,-5.549597,6.155639,1.044694,-5.693752,-4.886460,-9.391375,4.870119,-4.498947,-7.022490,0.508171,8.000979], dtype = "float32")#candidate|5881|(64,)|const|float32
const_5882 = relay.const([[-0.973520],[-7.036590],[-2.625793],[0.134915],[9.606253],[-0.460702],[5.378855],[-4.356652],[0.265713],[-2.564233],[-1.068459],[5.242213],[7.620595],[6.882590],[3.385007],[6.569101],[0.409358],[-0.531061],[-8.224962],[2.774259],[3.047043],[3.853261],[-6.264943],[-2.111007],[-6.853741],[5.545169],[-1.173569],[7.216221],[-8.982011],[-8.729062],[-2.432609],[2.296114],[0.167718],[5.739686],[-4.550436],[1.567765],[-5.789590],[-6.789175],[3.607540],[-0.906660],[-4.583174],[-2.669961],[4.429994],[-4.967446],[-9.829353],[2.266075],[-8.319259],[-1.163749],[2.735462],[2.937796],[-1.635696],[4.946973],[9.481871],[6.632105],[-1.487690],[9.752344],[-1.051235],[-8.451947],[0.252853],[7.448835],[0.274319],[-8.795191],[2.499638],[8.916732],[-4.327098],[-7.650907],[2.559688],[5.313323],[-2.852948],[9.486389],[-4.427066],[0.714506],[-5.390945],[-5.502755],[-3.942635],[9.363615],[3.339639],[5.511684],[-3.793638],[9.123426],[-9.956626],[0.098629],[5.924784],[-9.333619],[-8.635823],[5.078851],[-2.086347],[2.997958],[-1.125995],[-7.027383],[8.801680],[-7.088405],[5.072586],[6.553752],[-4.049024],[-8.485690],[4.153029],[-0.293406],[-7.370581],[-5.744857],[4.587634],[-1.660001],[-9.504200],[-0.371735],[4.088336],[1.779039],[9.832571],[7.898433],[3.936258],[-6.991181],[0.420275],[-6.263720],[2.247531],[-8.582868],[-2.234769],[-5.419718],[-8.940611],[5.014330],[-1.468193],[6.455544],[9.496606],[-3.918107],[-6.085138],[0.482381],[-5.377310],[1.507542],[5.764378],[-5.948909],[-1.740024],[-5.371549],[7.498252],[-0.310956],[2.146532],[-3.877582],[-5.513435],[-7.332073],[-0.801802],[-9.779769],[-1.822596],[7.566079],[3.377685],[5.159990],[-0.659447],[2.445080],[-9.752391],[1.355194],[-1.510453],[1.256321],[-1.178039],[9.572397],[8.375906],[-2.471797],[-3.165794],[-1.842720],[-2.089533],[-5.122496],[-6.592163],[-0.610851],[0.939678],[4.225376],[-5.716570],[-9.241114],[7.529767],[-6.363956],[6.317534],[-8.353747],[0.820788],[3.323757],[8.091896],[6.394260],[3.668231],[8.544881],[8.042642],[-6.807334],[-8.202955],[-9.561122],[2.369042],[3.832186],[-8.514078],[-7.571599],[-4.573488],[-0.581624],[8.493442],[9.180362],[3.065598],[-3.384758],[-5.226581],[-6.485698],[-1.137061],[6.253956],[-6.113061],[6.609361],[-0.246962],[-2.438795],[-6.919697],[-4.469637],[3.274003],[7.276853],[-7.910901],[4.185828],[2.697813],[-7.438501],[-0.337327],[8.379170],[-5.600380],[5.977440],[-7.147053],[-5.842481],[4.077748],[1.505366],[9.136718],[-8.719206],[-2.883034],[8.238054],[0.380743],[-0.964549],[-6.754781],[-6.105281],[1.700236],[8.449410],[-5.899838],[-2.179140],[8.311031],[4.516857],[-1.175054],[8.951628],[4.392837],[-4.544824],[1.486158],[-5.680899],[1.475404],[2.783626],[-1.204175],[-4.044929],[4.980078],[9.871193],[-1.395642],[-7.486819],[-0.920665],[-6.210226],[-2.711009],[-6.268492],[-8.310125],[8.613904],[-9.209908],[-6.765256],[-1.964561],[4.566656],[8.089477],[-9.911483],[-2.005165],[4.524637],[9.566892],[-8.943132],[5.660981],[-1.525169],[-2.392190],[1.322530],[-8.247635],[-9.875651],[5.115571],[-7.115311],[-0.477512],[-9.148599],[5.286594],[-4.488305],[-9.354878],[-9.585592],[7.014339],[5.111110],[7.180353],[-2.405545],[-2.140061],[-6.629122],[-3.707724],[1.725889],[1.144513],[5.474438],[7.002845],[-8.585928],[-5.642451],[-7.208478],[-2.596185],[3.087588],[-0.560749],[-4.557998],[-4.910313],[5.154646],[3.530549],[2.653797],[5.020454],[8.733763],[-8.807881],[-5.685379],[-5.583420],[-5.026093],[-2.598193],[5.979157],[8.098602],[-2.353145],[4.135492],[-8.730561],[-8.374613],[-1.425460],[0.397275],[1.980808],[-6.565644],[-1.063065],[-3.500179],[-7.038596],[8.177920],[9.764938],[-0.834632],[-4.170656],[4.150286],[8.109297],[5.951110],[4.122603],[3.730064],[4.333088]], dtype = "float32")#candidate|5882|(320, 1)|const|float32
call_5879 = relay.TupleGetItem(func_2753_call(relay.reshape(var_5880.astype('float32'), [6, 96]), relay.reshape(const_5881.astype('float32'), [64,]), relay.reshape(const_5882.astype('float32'), [320,]), ), 1)
call_5883 = relay.TupleGetItem(func_2758_call(relay.reshape(var_5880.astype('float32'), [6, 96]), relay.reshape(const_5881.astype('float32'), [64,]), relay.reshape(const_5882.astype('float32'), [320,]), ), 1)
output = relay.Tuple([call_5856,call_5879,var_5880,const_5881,const_5882,])
output2 = relay.Tuple([call_5857,call_5883,var_5880,const_5881,const_5882,])
func_5884 = relay.Function([var_5880,], output)
mod['func_5884'] = func_5884
mod = relay.transform.InferType()(mod)
mutated_mod['func_5884'] = func_5884
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5885 = relay.var("var_5885", dtype = "float32", shape = (576,))#candidate|5885|(576,)|var|float32
func_5884_call = mutated_mod.get_global_var('func_5884')
call_5886 = func_5884_call(var_5885)
output = call_5886
func_5887 = relay.Function([var_5885], output)
mutated_mod['func_5887'] = func_5887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_5898 = func_2428_call()
call_5899 = func_2428_call()
output = relay.Tuple([call_5898,])
output2 = relay.Tuple([call_5899,])
func_5920 = relay.Function([], output)
mod['func_5920'] = func_5920
mod = relay.transform.InferType()(mod)
mutated_mod['func_5920'] = func_5920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5920_call = mutated_mod.get_global_var('func_5920')
call_5921 = func_5920_call()
output = call_5921
func_5922 = relay.Function([], output)
mutated_mod['func_5922'] = func_5922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3725_call = mod.get_global_var('func_3725')
func_3726_call = mutated_mod.get_global_var('func_3726')
call_5952 = relay.TupleGetItem(func_3725_call(), 0)
call_5953 = relay.TupleGetItem(func_3726_call(), 0)
output = relay.Tuple([call_5952,])
output2 = relay.Tuple([call_5953,])
func_5967 = relay.Function([], output)
mod['func_5967'] = func_5967
mod = relay.transform.InferType()(mod)
mutated_mod['func_5967'] = func_5967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5967_call = mutated_mod.get_global_var('func_5967')
call_5968 = func_5967_call()
output = call_5968
func_5969 = relay.Function([], output)
mutated_mod['func_5969'] = func_5969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mod.get_global_var('func_3542')
func_3543_call = mutated_mod.get_global_var('func_3543')
call_5972 = relay.TupleGetItem(func_3542_call(), 1)
call_5973 = relay.TupleGetItem(func_3543_call(), 1)
output = call_5972
output2 = call_5973
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
func_4122_call = mod.get_global_var('func_4122')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_6046 = relay.TupleGetItem(func_4122_call(), 0)
call_6047 = relay.TupleGetItem(func_4124_call(), 0)
func_5614_call = mod.get_global_var('func_5614')
func_5618_call = mutated_mod.get_global_var('func_5618')
const_6097 = relay.const([-9.882005,-3.392261,-9.275493,2.820465,-2.223393,-8.610569,-1.272806,9.728946,-6.305626,4.579807,-8.224205,-9.351154,-3.133886,-5.239169,2.623890,-3.056379,4.666762,-0.318521,1.816594,2.761720,8.762135,-0.192633,8.698394,-9.829463,2.402262,-8.291246,1.875784,0.784754,7.147126,7.681214,-0.567980,0.957816,-0.330783,2.638586,9.880370,8.771794,3.204215,7.589186,-8.344259,-4.855207,3.029846,1.276651,-5.566335,-0.660442,-6.409374,-6.638406,-7.076518,-9.270430,2.809447,-1.365644,-1.064011,8.429324,1.930150,-6.906466,-6.380043,-6.640543,4.102480,-6.717063,-9.336833,-8.957659,-4.871838,2.747336,-4.186767,9.425764,-3.481261,-5.973630,-2.043090,-1.706960,-7.278647,6.734420,0.020964,9.726721,0.313325,-0.767724,-8.837730,-7.861953,1.600792,0.006023,1.198049,-3.791609,2.134329,-4.587921,-9.409665,0.696511,-4.307749,-4.746920,-9.950399,-4.703946,6.968706,-1.489625,1.440872,4.857557,-4.811226,-7.302452,9.182425,1.519054,-6.656482,-9.907245,-9.737212,5.944731,-1.901227,7.121149,8.698675,-4.421499,-6.809041,1.515640,8.634636,4.690789,0.340936,4.190005,-8.973276,9.930514,1.431212,7.400811,-5.820009,-4.174422,-9.559437,5.475046,7.496938,2.752418,-2.250863,-1.369679,5.832030,-9.168284,7.074966,5.180360,-3.932642,-0.703147,2.975186,-9.419702,8.848900,-8.336831,-6.893187,3.843841,-8.472340,4.570194,6.570647,-1.410699,2.523450,-1.164243,2.804940,-0.869194,-7.537505,1.247346,8.642479,3.982296,-5.069167,-5.461019,-6.039612,-9.993439,-6.082679,6.744510,0.123879,-3.968604,-8.979232,-6.005758,4.609414,-6.061699,2.682401,5.994863,4.129183,9.320015,-6.600126,-6.106854,-3.110993,0.850908,-1.997231,-3.937671,1.371527,6.230725,5.795299,1.037850,-8.450652,9.533393,4.798538,-7.654798,5.808843,-4.756314,-9.059167,-4.598291,8.392119,3.103782,0.129077,-8.123061,7.039746,-8.624090,6.419486,8.649677,7.680362,0.563277,0.578608,3.903362,-9.674669,-6.414424,-1.586690,7.662428,1.303369,-5.070638,-3.460206,4.180440,-7.931760,4.054809,2.401250,7.815834,6.627215,6.404305,7.928491,2.125792,-0.216844,-0.819883,6.959178,-2.376930,-9.627003,5.103959,6.149453,-0.951598,-1.116964,9.323580,-5.863346,6.886751,-2.801315,-7.031140,3.453723,2.928523,-2.002526,3.866689,0.277912,-3.166958,-0.205661,-9.206534,-1.110020,8.434639,-2.519767,-9.157500,4.680582,-1.268940,-0.295716,5.865705,8.232476,4.730993,-6.819494,6.194077,-1.240751,-4.066890,3.009693,0.442045,4.869893,-8.834117,8.475478,0.314454,-2.024195,-1.007856,-5.456446,2.993982,-7.841225,5.031358,9.572409,-5.651168,-6.307543,-4.837637,-4.993466,7.945748,-7.902146,8.089534,-7.189159,-7.797772,4.191718,1.457119,9.367120,1.350929,8.163466,-9.732370,2.608145,7.235315,3.943078,9.200743,3.603757,-9.771552,-6.175493,9.248691,-1.472476,-2.989231,0.167709,4.373776,-7.744397,-0.207631,-7.406444,-5.870121,-0.208364,8.260722,4.645519,6.794142,-8.675940,-2.555730,1.723729,1.060229,2.805333,4.604144,-9.315925,1.447059,7.616826,-3.531220,8.653085,1.955678,-5.669451,1.566463,9.145823,-0.720972,-9.213165,2.898630,2.437962,1.334550,-4.650528,0.656177,-9.432901,0.638891,-0.958990,8.267746,-7.585110,2.222130,1.431750,-6.522014,7.156308,-3.778116,5.452398,-1.363824,5.774035,2.596791,-9.836097,-8.103465,-2.613669,0.849593,9.833753,-0.957672,8.395252,8.700704,-9.503412,-8.953879,-8.060359,-1.247420,-2.612291,-3.298342,-3.425422,4.558310,-8.895616,0.589835,2.122509,-3.605634,9.362817,-9.589938,-2.034505,-3.407927,8.698357,2.839915,7.286470,1.169695,-0.420868,4.945431,0.895981,1.794584,-7.915191,-0.953956,4.022700,2.197922,3.875976,-3.850490,8.151560,4.998981,1.437408,-1.398116,-2.446261,-8.319670,-8.348598,6.087789,-4.404775,5.906794,-8.559109,-3.096768,-7.354035,-2.503740,9.019197,-3.162946,5.355027,5.830298,-2.211626,-3.683353,3.565460,9.633294,-3.073091,9.454273,7.986690,-6.323845,5.707970,-5.237862,-0.842869,8.312499,6.730461,-9.628760,8.418451,0.846185,2.612129,-5.665795,-2.684845,-0.733686,8.768051,9.923536,5.989644,-7.184307,-4.436395,-4.731086,9.719364,-0.120191,5.082814,-8.160696,-4.349212,-2.461409,1.768226,-2.227899,-3.557537,-4.709686,-3.087920,5.687302,0.208316,-3.610806,-6.205506,-3.676538,1.546001,-4.652374,5.022903,5.866144,-9.056629,-7.448354,6.888708,0.925848,3.226338,0.393424,8.129594,2.182355,-1.265289,-9.283701,6.385135,-6.844991,5.556980,6.162588,3.755682,-7.096517,9.249046,0.294975,7.823868,-2.238422,1.532395,-8.882777,-7.758327,5.604774,-7.559564,2.941349,2.764939,-2.539547,-1.366451,0.134097,-7.586727,4.061002,-6.687484,-6.675822,2.304082,4.131632,-9.219482,5.468896,6.383626,8.777860,-7.633974,8.097913,0.431443,-6.941590,-2.141446,8.481920,7.633143,-6.608787,-3.575278,7.971756,8.675179,-6.793122,1.652993,7.524246,-5.899530,-7.444877,7.362482,-6.127172,9.334464,3.888926,4.160485,-0.244295,7.388421,-8.612608,-1.515746,-6.339891,-2.621238,5.212113,-1.072448,5.656967,-6.994788,-4.013139,0.115545,-6.718067,8.393620,-0.004468,-1.813915,-9.416757,9.833503,7.811953,-7.689583,-3.885549,-7.754179,-5.284343,-9.397540,-0.975036,6.356773,-4.135378,0.319294,0.561751,-3.018502,6.924377,3.573762,8.247833,8.144529,-4.779779,-8.292892,-1.531853,-2.694481,4.174853,-5.167861,4.511548,-6.364762,3.826471,-1.312239,0.176440,-9.465173,-6.052910,-0.088952,8.194867,-1.176150,3.298292,-3.439470,-5.865580,3.153594,0.041289,6.029527,6.309205,-9.585613,6.479312,-8.378881,-2.422550,-9.745588,-5.130354,-4.963508,-9.641425,2.231119,2.440158,3.588481,-0.707252,4.988328,5.007802,0.404377,9.245823,6.622283,-2.689929,0.600558,-9.703705,9.116139,-5.780775,-1.237517,4.490762,-0.703845,2.726001,-5.266426,-3.886518], dtype = "float32")#candidate|6097|(576,)|const|float32
const_6098 = relay.const([6.703966,7.394302,-3.769568,-4.751146,-1.705416,1.067863,0.369257,7.170876,-9.649245,2.061331,5.218561,0.431716,-8.226512,9.739476,3.125081,-3.806632,8.639138,9.980833,-5.240720,4.366090,-5.194191,-9.331396,-8.038796,-8.898591,-2.986977,-6.439029,-5.000340,4.954819,6.304585,5.938845,-6.233166,1.586543,9.914159,-8.512136,-3.770416,-0.006569,-2.727044,-7.682280,-1.494343,-4.365486,-9.685721,-0.497991,-7.037127,-8.479857,-4.219682,-3.868721,6.909133,4.133599,-7.851529,-8.155900,4.826979,5.981046,-4.057266,2.017382,-9.053849,4.962039,-1.774068,-7.233931,-0.478553,-6.143309,-9.030261,3.406583,7.544692,-9.026261,-1.811598,-0.871489,1.018571,-0.951323,-4.640014,-4.497295,0.925240,4.220227,9.024536,-6.050024,-3.967578,-6.599468,7.259364,2.316240,-3.746053,-7.253350,-4.544710,3.266774,-8.676809,6.229845,8.859148,-0.002995,-7.426020,-1.397147,5.556212,1.662180,7.913722,-4.561146,6.530163,6.068746,9.600137,7.722021,5.604090,9.085466,-7.269888,-8.717104,-4.711232,-2.755368,-4.228035,-5.818395,9.219526,-4.903136,9.552596,4.022460,-5.324153,9.729832,-2.518789,0.411253,1.922544,7.292270,-3.138138,1.041576,-7.892577,6.465533,-1.854110,-7.247274,6.343621,-6.545962,3.747700,6.321083,7.004566,3.356840,1.086258,5.259968,5.771535,-4.910143,-5.334377,-3.972105,6.620086,6.044715,8.688623,7.962560,-4.619616,-8.655099,5.765389,0.322382,-1.131844,-8.930602,-7.306711,-8.120037,3.526633,4.894213,-0.314822,-7.573917,3.168962,7.255559,-7.600791,2.877383,-0.615110,-9.672382,8.801466,-2.570186,0.842469,-8.392282,-5.616988,3.840107,9.348076,0.715566,5.012864,-9.777069,-2.903762,6.312985,-7.885306,6.920913,-5.605133,9.154192,-2.373247,2.096528,-4.229285,7.871312,-4.817310,-5.529497,0.413606,5.899438,-7.000865,6.951935,1.389262,9.095399,9.804948,9.069193,-8.942086,4.019591,-9.271688,-8.406036,-2.627018,-9.827541,9.813886,2.623486,-6.235417,3.723109,-1.030849,2.305210,3.388524,7.900129,-0.864189,6.630621,2.307985,5.145008,4.627036,4.004453,0.590225,1.905084,-8.497455,8.862109,5.615405,0.440878,2.963198,-1.274224,6.293697,1.059746,-9.636622,8.583910,8.257272,7.696575,-4.454395,3.438672,-0.234574,-1.246788,6.749031,-4.937836,-8.803690,-5.405150,-5.258367,9.302686,-6.964400,1.164562,8.944469,8.531997,5.761579,2.520347,2.475137,9.105793,7.622439,-6.501795,6.102770,-4.997380,7.131939,2.395981,1.111407,6.369238,4.697280,-5.439939,2.287520,-3.780204,-3.562054,0.294987,-9.948782,-4.265055,-0.347877,-5.845658,5.487622,-8.786376,9.206266,-3.590016,-0.328575,-2.755200,9.283025,-0.069730,-3.735159,7.220159,-4.882625,-1.541828,-8.922707,0.012565,-3.611458,-9.736338,-9.424486,-9.050831,7.430058,-6.898411,-9.209727,8.330093,5.301897,5.755832,-1.055872,-9.693995,1.039538,0.210746,2.121157,-1.189816,-9.983234,6.528636,4.384435,-3.083076,1.488154,-0.076996,-4.840844,3.877486,8.534023,7.053294,4.034162,9.720818,2.422156,-9.959393,7.737022,-4.987927,-8.484783,-5.051541,2.488324,-4.175573,9.529787,-1.757539,-2.001079,5.475804,-9.519303,-1.410373,-2.653909,-9.165576,-3.414500,5.271102,-8.383234,-7.937391,0.481610,-2.668679,9.021022,1.378391], dtype = "float32")#candidate|6098|(320,)|const|float32
call_6096 = relay.TupleGetItem(func_5614_call(relay.reshape(const_6097.astype('float32'), [576,]), relay.reshape(const_6098.astype('float32'), [320,]), ), 0)
call_6099 = relay.TupleGetItem(func_5618_call(relay.reshape(const_6097.astype('float32'), [576,]), relay.reshape(const_6098.astype('float32'), [320,]), ), 0)
output = relay.Tuple([call_6046,call_6096,const_6097,const_6098,])
output2 = relay.Tuple([call_6047,call_6099,const_6097,const_6098,])
func_6105 = relay.Function([], output)
mod['func_6105'] = func_6105
mod = relay.transform.InferType()(mod)
mutated_mod['func_6105'] = func_6105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6105_call = mutated_mod.get_global_var('func_6105')
call_6106 = func_6105_call()
output = call_6106
func_6107 = relay.Function([], output)
mutated_mod['func_6107'] = func_6107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4855_call = mod.get_global_var('func_4855')
func_4856_call = mutated_mod.get_global_var('func_4856')
call_6108 = relay.TupleGetItem(func_4855_call(), 2)
call_6109 = relay.TupleGetItem(func_4856_call(), 2)
func_3839_call = mod.get_global_var('func_3839')
func_3842_call = mutated_mod.get_global_var('func_3842')
var_6129 = relay.var("var_6129", dtype = "float32", shape = (1485,))#candidate|6129|(1485,)|var|float32
call_6128 = relay.TupleGetItem(func_3839_call(relay.reshape(var_6129.astype('float32'), [11, 9, 15])), 0)
call_6130 = relay.TupleGetItem(func_3842_call(relay.reshape(var_6129.astype('float32'), [11, 9, 15])), 0)
output = relay.Tuple([call_6108,call_6128,var_6129,])
output2 = relay.Tuple([call_6109,call_6130,var_6129,])
func_6133 = relay.Function([var_6129,], output)
mod['func_6133'] = func_6133
mod = relay.transform.InferType()(mod)
mutated_mod['func_6133'] = func_6133
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6134 = relay.var("var_6134", dtype = "float32", shape = (1485,))#candidate|6134|(1485,)|var|float32
func_6133_call = mutated_mod.get_global_var('func_6133')
call_6135 = func_6133_call(var_6134)
output = call_6135
func_6136 = relay.Function([var_6134], output)
mutated_mod['func_6136'] = func_6136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4920_call = mod.get_global_var('func_4920')
func_4921_call = mutated_mod.get_global_var('func_4921')
call_6183 = relay.TupleGetItem(func_4920_call(), 1)
call_6184 = relay.TupleGetItem(func_4921_call(), 1)
output = call_6183
output2 = call_6184
func_6185 = relay.Function([], output)
mod['func_6185'] = func_6185
mod = relay.transform.InferType()(mod)
output = func_6185()
func_6186 = relay.Function([], output)
mutated_mod['func_6186'] = func_6186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_6187 = func_2428_call()
call_6188 = func_2428_call()
func_4207_call = mod.get_global_var('func_4207')
func_4209_call = mutated_mod.get_global_var('func_4209')
call_6189 = relay.TupleGetItem(func_4207_call(), 0)
call_6190 = relay.TupleGetItem(func_4209_call(), 0)
func_4920_call = mod.get_global_var('func_4920')
func_4921_call = mutated_mod.get_global_var('func_4921')
call_6211 = relay.TupleGetItem(func_4920_call(), 2)
call_6212 = relay.TupleGetItem(func_4921_call(), 2)
output = relay.Tuple([call_6187,call_6189,call_6211,])
output2 = relay.Tuple([call_6188,call_6190,call_6212,])
func_6221 = relay.Function([], output)
mod['func_6221'] = func_6221
mod = relay.transform.InferType()(mod)
mutated_mod['func_6221'] = func_6221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6221_call = mutated_mod.get_global_var('func_6221')
call_6222 = func_6221_call()
output = call_6222
func_6223 = relay.Function([], output)
mutated_mod['func_6223'] = func_6223
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6304 = relay.const([[[-7.516485,4.841601,6.108490,-5.945627,-1.266370],[1.572589,-6.008355,1.450826,8.604308,7.881013],[-0.410849,6.996194,-6.103651,0.723903,8.834567],[4.025704,9.583734,-0.645443,-0.646224,6.119027],[-7.526215,2.065680,0.294221,3.217443,4.382148],[-2.763099,-6.621513,6.297181,-6.074641,-7.908969],[4.765819,-6.998787,-9.986804,5.700067,4.916744],[-5.411061,9.369350,-9.242538,-0.004799,-9.463021],[-8.179840,-4.897214,-7.456676,8.152908,-8.847925],[-5.665712,-3.703900,-2.649609,-4.484842,1.514993],[-9.797770,7.986005,-1.907019,5.209102,7.942104]],[[-2.643956,-3.088483,-0.630049,-3.974750,-6.773393],[5.448924,-7.630738,3.680655,3.377959,2.454469],[7.007248,-8.585170,2.372065,-8.709868,6.451226],[-1.123991,3.670653,-2.773912,-4.120411,-5.872248],[4.356382,6.114543,7.163464,-8.009344,-5.388161],[7.451803,-4.674761,-3.253170,-1.734069,-4.556557],[-6.016256,-4.198528,0.646897,3.213954,4.646130],[-5.350183,-9.933353,1.179471,-8.691672,-3.865221],[2.030597,-0.399571,3.657541,9.130259,4.708608],[6.976828,1.336576,-7.647453,8.674773,-3.777790],[2.349768,3.089012,-8.278023,5.176527,4.473820]],[[-4.274137,5.033154,-8.948878,1.439142,0.777775],[2.172733,3.726316,-6.938862,8.010471,1.053728],[-6.988607,1.148451,-6.120685,-1.489343,-9.831618],[2.128307,-4.253646,-3.909375,0.194277,4.888122],[-9.032251,-6.502823,2.371469,2.819996,-6.860700],[-6.625176,3.971712,-2.449918,9.258272,7.557979],[-3.872020,-9.808123,-7.694702,5.967628,6.615480],[-3.027638,9.098921,6.545019,0.635441,-4.643416],[8.926989,-8.267940,-0.182406,3.258849,-0.055104],[4.711541,3.308437,5.357246,-9.031161,-4.577636],[9.956295,-9.230210,6.937779,7.610073,-9.818499]],[[-6.176901,-9.124651,8.953043,3.997208,4.187729],[8.460341,9.823949,-2.046985,-3.522082,6.119539],[-9.741576,9.911989,-4.967641,-2.254323,2.684372],[6.614426,3.668733,7.107327,-8.195033,1.658052],[-8.029060,-6.059846,2.166805,-7.898294,-8.892064],[-4.977305,8.669910,8.566891,-8.102455,7.035399],[-7.721041,6.752276,3.705031,-6.945677,-5.587050],[8.680152,2.756065,-6.309559,-5.280700,-4.371220],[-7.302632,-9.527789,9.541314,8.206618,3.156041],[2.341208,5.080267,2.971630,6.145877,-5.552395],[5.188356,-7.840112,-1.822750,-8.627579,-7.043675]],[[4.191427,2.279324,-7.798012,5.708335,6.254818],[-6.407831,-4.254075,6.283847,-3.972494,-5.102960],[-5.862186,-4.638016,-2.828909,1.780240,-5.680822],[0.210520,6.200437,5.130065,5.813990,0.641138],[3.955032,-1.563796,-9.432417,-2.955390,-6.966613],[4.145930,-5.116014,-3.762119,-6.533834,5.590935],[8.611367,-3.521971,-2.857952,-6.778456,-0.096043],[-6.275313,1.078809,-4.034254,-3.920756,1.849667],[9.378647,-4.536930,-8.604321,-6.531153,-1.693851],[5.016232,-3.561841,-7.896266,1.322669,3.508613],[2.336604,-0.277577,-9.069085,-6.265750,4.963437]],[[5.738399,-5.282058,-7.008439,-7.857129,-2.413412],[5.072941,-6.718623,2.336319,-3.159824,0.665673],[3.451000,1.171337,-4.184358,-6.745894,-7.766564],[-5.666686,-6.476796,1.090291,8.879610,8.580765],[7.747693,-4.538958,-5.556915,-3.268571,-8.774520],[-3.159980,-3.477275,4.339172,2.204933,6.234519],[4.779881,-6.803967,2.007822,9.110668,9.442021],[-3.550212,7.583457,6.216121,-4.239713,-4.144481],[0.005219,-6.196100,-3.617459,-0.877173,4.329702],[4.571744,4.426716,-4.371081,-3.631335,-5.153811],[-2.809437,-3.148704,6.603541,-8.372879,8.565453]]], dtype = "float32")#candidate|6304|(6, 11, 5)|const|float32
uop_6305 = relay.rsqrt(const_6304.astype('float32')) # shape=(6, 11, 5)
bop_6315 = relay.right_shift(uop_6305.astype('uint64'), relay.reshape(const_6304.astype('uint64'), relay.shape_of(uop_6305))) # shape=(6, 11, 5)
bop_6320 = relay.greater_equal(bop_6315.astype('bool'), relay.reshape(uop_6305.astype('bool'), relay.shape_of(bop_6315))) # shape=(6, 11, 5)
bop_6326 = relay.left_shift(bop_6320.astype('int16'), relay.reshape(uop_6305.astype('int16'), relay.shape_of(bop_6320))) # shape=(6, 11, 5)
output = relay.Tuple([bop_6326,])
output2 = relay.Tuple([bop_6326,])
func_6329 = relay.Function([], output)
mod['func_6329'] = func_6329
mod = relay.transform.InferType()(mod)
output = func_6329()
func_6330 = relay.Function([], output)
mutated_mod['func_6330'] = func_6330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4122_call = mod.get_global_var('func_4122')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_6336 = relay.TupleGetItem(func_4122_call(), 0)
call_6337 = relay.TupleGetItem(func_4124_call(), 0)
uop_6346 = relay.sinh(call_6336.astype('float32')) # shape=(3, 16, 6)
uop_6348 = relay.sinh(call_6337.astype('float32')) # shape=(3, 16, 6)
output = uop_6346
output2 = uop_6348
func_6353 = relay.Function([], output)
mod['func_6353'] = func_6353
mod = relay.transform.InferType()(mod)
output = func_6353()
func_6354 = relay.Function([], output)
mutated_mod['func_6354'] = func_6354
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6367 = relay.var("var_6367", dtype = "float64", shape = (13, 4, 3))#candidate|6367|(13, 4, 3)|var|float64
uop_6368 = relay.cosh(var_6367.astype('float64')) # shape=(13, 4, 3)
output = relay.Tuple([uop_6368,])
output2 = relay.Tuple([uop_6368,])
func_6381 = relay.Function([var_6367,], output)
mod['func_6381'] = func_6381
mod = relay.transform.InferType()(mod)
var_6382 = relay.var("var_6382", dtype = "float64", shape = (13, 4, 3))#candidate|6382|(13, 4, 3)|var|float64
output = func_6381(var_6382)
func_6383 = relay.Function([var_6382], output)
mutated_mod['func_6383'] = func_6383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6221_call = mod.get_global_var('func_6221')
func_6223_call = mutated_mod.get_global_var('func_6223')
call_6389 = relay.TupleGetItem(func_6221_call(), 2)
call_6390 = relay.TupleGetItem(func_6223_call(), 2)
uop_6405 = relay.asinh(call_6389.astype('float32')) # shape=(12, 8, 9)
uop_6407 = relay.asinh(call_6390.astype('float32')) # shape=(12, 8, 9)
var_6423 = relay.var("var_6423", dtype = "float32", shape = (12, 8, 9))#candidate|6423|(12, 8, 9)|var|float32
bop_6424 = relay.logical_and(uop_6405.astype('bool'), relay.reshape(var_6423.astype('bool'), relay.shape_of(uop_6405))) # shape=(12, 8, 9)
bop_6427 = relay.logical_and(uop_6407.astype('bool'), relay.reshape(var_6423.astype('bool'), relay.shape_of(uop_6407))) # shape=(12, 8, 9)
output = relay.Tuple([bop_6424,])
output2 = relay.Tuple([bop_6427,])
func_6434 = relay.Function([var_6423,], output)
mod['func_6434'] = func_6434
mod = relay.transform.InferType()(mod)
var_6435 = relay.var("var_6435", dtype = "float32", shape = (12, 8, 9))#candidate|6435|(12, 8, 9)|var|float32
output = func_6434(var_6435)
func_6436 = relay.Function([var_6435], output)
mutated_mod['func_6436'] = func_6436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3198_call = mod.get_global_var('func_3198')
func_3199_call = mutated_mod.get_global_var('func_3199')
call_6444 = relay.TupleGetItem(func_3198_call(), 2)
call_6445 = relay.TupleGetItem(func_3199_call(), 2)
uop_6446 = relay.log(call_6444.astype('float32')) # shape=(3, 16, 6)
uop_6448 = relay.log(call_6445.astype('float32')) # shape=(3, 16, 6)
func_4196_call = mod.get_global_var('func_4196')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_6449 = relay.TupleGetItem(func_4196_call(), 0)
call_6450 = relay.TupleGetItem(func_4197_call(), 0)
output = relay.Tuple([uop_6446,call_6449,])
output2 = relay.Tuple([uop_6448,call_6450,])
func_6455 = relay.Function([], output)
mod['func_6455'] = func_6455
mod = relay.transform.InferType()(mod)
mutated_mod['func_6455'] = func_6455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6455_call = mutated_mod.get_global_var('func_6455')
call_6456 = func_6455_call()
output = call_6456
func_6457 = relay.Function([], output)
mutated_mod['func_6457'] = func_6457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5098_call = mod.get_global_var('func_5098')
func_5099_call = mutated_mod.get_global_var('func_5099')
call_6470 = relay.TupleGetItem(func_5098_call(), 0)
call_6471 = relay.TupleGetItem(func_5099_call(), 0)
output = relay.Tuple([call_6470,])
output2 = relay.Tuple([call_6471,])
func_6474 = relay.Function([], output)
mod['func_6474'] = func_6474
mod = relay.transform.InferType()(mod)
output = func_6474()
func_6475 = relay.Function([], output)
mutated_mod['func_6475'] = func_6475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6514 = relay.var("var_6514", dtype = "int32", shape = (11, 9, 14))#candidate|6514|(11, 9, 14)|var|int32
var_6515 = relay.var("var_6515", dtype = "int32", shape = (11, 9, 14))#candidate|6515|(11, 9, 14)|var|int32
bop_6516 = relay.multiply(var_6514.astype('int32'), relay.reshape(var_6515.astype('int32'), relay.shape_of(var_6514))) # shape=(11, 9, 14)
output = relay.Tuple([bop_6516,])
output2 = relay.Tuple([bop_6516,])
func_6552 = relay.Function([var_6514,var_6515,], output)
mod['func_6552'] = func_6552
mod = relay.transform.InferType()(mod)
mutated_mod['func_6552'] = func_6552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6552_call = mutated_mod.get_global_var('func_6552')
var_6554 = relay.var("var_6554", dtype = "int32", shape = (11, 9, 14))#candidate|6554|(11, 9, 14)|var|int32
var_6555 = relay.var("var_6555", dtype = "int32", shape = (11, 9, 14))#candidate|6555|(11, 9, 14)|var|int32
call_6553 = func_6552_call(var_6554,var_6555,)
output = call_6553
func_6556 = relay.Function([var_6554,var_6555,], output)
mutated_mod['func_6556'] = func_6556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6221_call = mod.get_global_var('func_6221')
func_6223_call = mutated_mod.get_global_var('func_6223')
call_6603 = relay.TupleGetItem(func_6221_call(), 0)
call_6604 = relay.TupleGetItem(func_6223_call(), 0)
var_6609 = relay.var("var_6609", dtype = "bool", shape = (3, 16, 6))#candidate|6609|(3, 16, 6)|var|bool
bop_6610 = relay.divide(call_6603.astype('float32'), relay.reshape(var_6609.astype('float32'), relay.shape_of(call_6603))) # shape=(3, 16, 6)
bop_6613 = relay.divide(call_6604.astype('float32'), relay.reshape(var_6609.astype('float32'), relay.shape_of(call_6604))) # shape=(3, 16, 6)
func_5353_call = mod.get_global_var('func_5353')
func_5354_call = mutated_mod.get_global_var('func_5354')
call_6615 = relay.TupleGetItem(func_5353_call(), 1)
call_6616 = relay.TupleGetItem(func_5354_call(), 1)
output = relay.Tuple([bop_6610,call_6615,])
output2 = relay.Tuple([bop_6613,call_6616,])
func_6651 = relay.Function([var_6609,], output)
mod['func_6651'] = func_6651
mod = relay.transform.InferType()(mod)
mutated_mod['func_6651'] = func_6651
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6652 = relay.var("var_6652", dtype = "bool", shape = (3, 16, 6))#candidate|6652|(3, 16, 6)|var|bool
func_6651_call = mutated_mod.get_global_var('func_6651')
call_6653 = func_6651_call(var_6652)
output = call_6653
func_6654 = relay.Function([var_6652], output)
mutated_mod['func_6654'] = func_6654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6474_call = mod.get_global_var('func_6474')
func_6475_call = mutated_mod.get_global_var('func_6475')
call_6667 = relay.TupleGetItem(func_6474_call(), 0)
call_6668 = relay.TupleGetItem(func_6475_call(), 0)
func_2041_call = mod.get_global_var('func_2041')
func_2047_call = mutated_mod.get_global_var('func_2047')
const_6683 = relay.const([-7.417132,-6.891509,2.350900,-0.262305,3.455973,0.354013,-0.904924,6.990229,5.843767,-5.031815,3.730376,9.819080,-2.495250,-9.417401,5.948649,5.240936,6.804765,-8.371951,-3.254596,-8.578522,-3.029003,-2.867182,4.372617,-4.334663,-1.315305,-1.523246,-1.143678,0.132447,9.121692,-2.588298,4.664725,-7.968403,-6.367093,4.589841,6.669893,-1.114284,4.631246,-5.202726,-2.701718,2.696055,5.730330,-0.607089,-3.266896,-7.983087,3.467528,-0.232245,-7.541556,0.079378,1.331226,-3.059544,2.330390,-9.932187,1.406451,9.113522,9.197738,-9.906099,-0.143450,-0.783283,-0.480227,-6.848286,-0.112019,-7.259625,2.299225,2.028627,-5.110541,7.626704,-3.771322,6.938933,-7.873130,4.248126,1.507661,2.601008,-2.198012,-7.555811,-0.451823,5.072138,3.008531,-0.267126,5.223179,4.651566,3.270699,1.623062,-3.981316,9.527923,7.942558,7.792211,-3.821928,-0.486037,-3.229059,-3.623769,1.309792,4.314782,3.768141,7.596781,7.147874,1.171645,2.925737,-6.428376,1.764459,3.619982,-9.601973,3.726845,4.716053,-2.944009,4.924920,-5.293209,-2.773057,2.561028,8.963510,-2.284475,-8.330216,3.191642,7.257850,5.217377,8.678295,7.477442,6.845676,7.205119,0.380078,3.256381,-1.313033,5.686423,2.381199,-4.551160,-5.234334,-5.589091,-4.661780,-5.706807,2.027175,-8.607263,-6.194481,2.390627,8.600569,-5.504386,-5.446040,3.961443,-1.613625,1.961898,2.699963,-8.532034,-8.747918,-1.839437,5.268589,-9.702882,3.230867,2.213554,5.531322,0.457680,2.582300,2.252975,6.806130,-4.460695,6.120099,-4.888444,-4.464139,-7.607004,9.626375,5.932554,-2.244931,2.834535,3.606077,2.315511,8.497493,1.872962,7.756342,-2.776761,9.542196,-2.955748,-3.041228,8.320414,9.549397,-1.842525,9.781721,1.648303,0.689691,3.000489,-7.653665,7.402489,2.093532,-0.612663,1.668479,-0.646562,-4.779743,-2.763701,5.653335,3.256119,4.343454,2.760130,9.140327,-5.544643,6.390674,4.138091,7.163185,-7.053868,0.498747,5.722789,3.846126,2.469190,-5.730948,3.306608,-1.880998,-0.766860,-9.660103,-8.816173,8.131888,-4.372740,-0.655282,-5.383261,5.593888,-5.996471,5.988140,1.515399,1.613146,-9.637886,-0.378375,8.593304,-2.317112,5.114714,0.725777,2.545697,-7.275670,-4.551203,1.133258,-1.759525,1.703954,-1.776660,-9.329633,0.987635,-4.394261,2.992938,4.444671,3.387640,3.741861,-9.447356,-1.688733,3.495583,-1.895508,9.783505,-5.374276,-6.702833,4.323579,-3.566652,-6.854984,2.459927,-5.042157,-0.964259,-9.020903,1.113989,-9.203472,-1.900938,8.338106,6.749113,7.526952,-8.752718,5.221253,0.838847,6.979056,-1.660740,-1.701170,-6.793474,9.166407,-9.471797,5.351715,0.370046,-4.966928,-2.740231,5.974204,5.940722,7.859249,-0.232463,-3.707683,6.722049,6.706582,2.889542,1.863476,-1.619301,-5.069002,-4.504317,4.490167,5.637503,-1.075514,5.301502,-1.257712,-4.818934,-3.872203,-5.976658,3.108231,-1.127909,2.047104,-6.250547,-9.039053,7.935650,3.531811,-1.064879,9.235982,-6.264037,6.548115,1.198715,-0.220994,2.446436,-6.606318,8.836524,4.914980,0.998820,-4.449326,-4.252064,-6.933357,1.270639,1.483393,-9.601013,-2.324875,-4.343229,5.536600,7.625366,-5.911100,-0.104224,-5.382813,-9.839762,-3.597935,-8.362426,5.555178,5.486870,1.794345,9.352581,-4.298435,5.094298,2.034419,-0.755448,-3.697561,-4.163172,0.560958,2.842782,1.530653,2.988018,3.211936,-5.440154,-9.517408,1.626412,-7.927019,8.365006,-8.478893,8.338631,-3.094298,-5.740687,4.654936,9.615052,-8.891770,-1.647983,-3.289168,0.964109,-7.062370,-0.393186,4.147909,-9.621907,4.454306,-8.613322,-8.906619,2.599642,4.453129,8.548619,-3.708386,1.356678,-9.693356,-2.604292,-7.345971,-5.967906,5.906426,6.425612,-7.293786,6.581141,3.650234,-0.599466,5.829543,6.751800,5.094806,-9.264947,8.135882,-7.643659,5.230163,9.853263,-6.335384,-4.113737,-2.848576,-9.372315,7.461577,-9.433357,4.631359,6.417570,-5.612030,-7.795397,8.276874,-2.031414,-6.195037,-2.656339,8.219237,7.565366,-9.121323,-8.967281,-0.857301,3.150496,-2.905616,-3.033186,-0.749188,-3.823694,-1.880251,0.388152,4.655798,7.485830,-1.210784,-7.340850,2.411903,-8.493614,8.576918,-1.261813,1.140599,-6.652410,-6.525046,-8.123537,-1.862254,5.618644,1.302225,-2.570604,-6.854875,-4.097472,-6.190156,4.456111,0.762732,9.253438,-8.808159,-1.090308,6.465962,9.481935,3.183912,6.987667,-6.668635,2.807379,7.962618,8.967988,4.473455,-7.425205,-4.325272,9.537023,9.473872,-9.102364,-0.409850,-6.888662,5.049577,3.963821,3.459968,-2.303978,-0.026337,1.789133,-7.856298,8.145384,-4.704412,0.045671,9.709384,-8.879575,1.968879,-6.378544,0.844380,7.884412,-4.209980,-2.645365,8.315729,-3.206424,-0.211659,8.769335,-9.721282,-7.409418,8.132220,6.116107,-8.801220,0.410888,-3.147601,2.377394,-2.781771,0.441862,-1.114488,-6.649908,-9.115371,5.470989,-4.499148,7.276136,7.820934,-2.847669,4.918907,-8.019745,6.882063,5.709771,3.061373,-2.101010,-3.568104,5.519634,1.225447,-4.903129,-5.266648,-7.243141,5.824299,3.819342,1.150394,0.048164,8.215598,-6.661692,9.131371,-9.449024,-2.518653,2.205681,-0.458086,6.426736,-8.675365,-1.668274,9.663839,-2.823701,-2.449971,-2.884116,4.194555,4.615492,8.388694,2.702642,7.654355,5.461276,-2.642015,-0.180301,1.976666,-0.423252,-5.190540,-6.986849,5.553838,-1.236814,-2.302959,3.510428,-4.327529,-9.268487,-5.381499,-6.873651,-4.394543,-9.143344,-0.868981,0.429861,-6.755287,-0.235408,-2.287222,3.865098,1.223532,-1.805095,-7.606699,8.845649,-3.403944,-5.643268,1.749599,-4.073518,-0.361404,6.954091,-6.865737,4.245444,-3.848737,4.917556,-8.531006,1.744169,-9.084332,-5.889318,4.758963,5.333002,8.941422,9.340966,-2.796959,-9.574385,-2.640595,-4.642256,4.592904,0.598169,0.630147,-8.646310,7.233128,6.768242], dtype = "float32")#candidate|6683|(576,)|const|float32
const_6684 = relay.const([-3,7,8,5,1,-5,-5,9,-10,7,-3,2,-3,9,4,-9,9,-9,5,8,-5,1,5,-6], dtype = "uint32")#candidate|6684|(24,)|const|uint32
var_6685 = relay.var("var_6685", dtype = "uint32", shape = (384,))#candidate|6685|(384,)|var|uint32
call_6682 = relay.TupleGetItem(func_2041_call(relay.reshape(const_6683.astype('float32'), [576,]), relay.reshape(const_6684.astype('uint32'), [24,]), relay.reshape(var_6685.astype('uint32'), [384,]), relay.reshape(call_6667.astype('bool'), [5, 4, 16]), ), 2)
call_6686 = relay.TupleGetItem(func_2047_call(relay.reshape(const_6683.astype('float32'), [576,]), relay.reshape(const_6684.astype('uint32'), [24,]), relay.reshape(var_6685.astype('uint32'), [384,]), relay.reshape(call_6667.astype('bool'), [5, 4, 16]), ), 2)
output = relay.Tuple([call_6667,call_6682,const_6683,const_6684,var_6685,])
output2 = relay.Tuple([call_6668,call_6686,const_6683,const_6684,var_6685,])
func_6688 = relay.Function([var_6685,], output)
mod['func_6688'] = func_6688
mod = relay.transform.InferType()(mod)
var_6689 = relay.var("var_6689", dtype = "uint32", shape = (384,))#candidate|6689|(384,)|var|uint32
output = func_6688(var_6689)
func_6690 = relay.Function([var_6689], output)
mutated_mod['func_6690'] = func_6690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3370_call = mod.get_global_var('func_3370')
func_3372_call = mutated_mod.get_global_var('func_3372')
call_6748 = func_3370_call()
call_6749 = func_3370_call()
output = relay.Tuple([call_6748,])
output2 = relay.Tuple([call_6749,])
func_6757 = relay.Function([], output)
mod['func_6757'] = func_6757
mod = relay.transform.InferType()(mod)
mutated_mod['func_6757'] = func_6757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6757_call = mutated_mod.get_global_var('func_6757')
call_6758 = func_6757_call()
output = call_6758
func_6759 = relay.Function([], output)
mutated_mod['func_6759'] = func_6759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5452_call = mod.get_global_var('func_5452')
func_5454_call = mutated_mod.get_global_var('func_5454')
call_6763 = func_5452_call()
call_6764 = func_5452_call()
output = relay.Tuple([call_6763,])
output2 = relay.Tuple([call_6764,])
func_6774 = relay.Function([], output)
mod['func_6774'] = func_6774
mod = relay.transform.InferType()(mod)
output = func_6774()
func_6775 = relay.Function([], output)
mutated_mod['func_6775'] = func_6775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4800_call = mod.get_global_var('func_4800')
func_4801_call = mutated_mod.get_global_var('func_4801')
call_6793 = relay.TupleGetItem(func_4800_call(), 0)
call_6794 = relay.TupleGetItem(func_4801_call(), 0)
output = relay.Tuple([call_6793,])
output2 = relay.Tuple([call_6794,])
func_6809 = relay.Function([], output)
mod['func_6809'] = func_6809
mod = relay.transform.InferType()(mod)
mutated_mod['func_6809'] = func_6809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6809_call = mutated_mod.get_global_var('func_6809')
call_6810 = func_6809_call()
output = call_6810
func_6811 = relay.Function([], output)
mutated_mod['func_6811'] = func_6811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5975_call = mod.get_global_var('func_5975')
func_5977_call = mutated_mod.get_global_var('func_5977')
call_6865 = func_5975_call()
call_6866 = func_5975_call()
output = relay.Tuple([call_6865,])
output2 = relay.Tuple([call_6866,])
func_6875 = relay.Function([], output)
mod['func_6875'] = func_6875
mod = relay.transform.InferType()(mod)
mutated_mod['func_6875'] = func_6875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6875_call = mutated_mod.get_global_var('func_6875')
call_6876 = func_6875_call()
output = call_6876
func_6877 = relay.Function([], output)
mutated_mod['func_6877'] = func_6877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3919_call = mod.get_global_var('func_3919')
func_3921_call = mutated_mod.get_global_var('func_3921')
call_6957 = func_3919_call()
call_6958 = func_3919_call()
output = call_6957
output2 = call_6958
func_6963 = relay.Function([], output)
mod['func_6963'] = func_6963
mod = relay.transform.InferType()(mod)
output = func_6963()
func_6964 = relay.Function([], output)
mutated_mod['func_6964'] = func_6964
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6998 = relay.var("var_6998", dtype = "float32", shape = (3, 13, 14))#candidate|6998|(3, 13, 14)|var|float32
var_6999 = relay.var("var_6999", dtype = "float32", shape = (3, 13, 14))#candidate|6999|(3, 13, 14)|var|float32
bop_7000 = relay.floor_divide(var_6998.astype('float32'), relay.reshape(var_6999.astype('float32'), relay.shape_of(var_6998))) # shape=(3, 13, 14)
uop_7008 = relay.acosh(var_6998.astype('float64')) # shape=(3, 13, 14)
output = relay.Tuple([bop_7000,uop_7008,])
output2 = relay.Tuple([bop_7000,uop_7008,])
func_7024 = relay.Function([var_6998,var_6999,], output)
mod['func_7024'] = func_7024
mod = relay.transform.InferType()(mod)
mutated_mod['func_7024'] = func_7024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7024_call = mutated_mod.get_global_var('func_7024')
var_7026 = relay.var("var_7026", dtype = "float32", shape = (3, 13, 14))#candidate|7026|(3, 13, 14)|var|float32
var_7027 = relay.var("var_7027", dtype = "float32", shape = (3, 13, 14))#candidate|7027|(3, 13, 14)|var|float32
call_7025 = func_7024_call(var_7026,var_7027,)
output = call_7025
func_7028 = relay.Function([var_7026,var_7027,], output)
mutated_mod['func_7028'] = func_7028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5074_call = mod.get_global_var('func_5074')
func_5075_call = mutated_mod.get_global_var('func_5075')
call_7102 = relay.TupleGetItem(func_5074_call(), 1)
call_7103 = relay.TupleGetItem(func_5075_call(), 1)
output = call_7102
output2 = call_7103
func_7118 = relay.Function([], output)
mod['func_7118'] = func_7118
mod = relay.transform.InferType()(mod)
output = func_7118()
func_7119 = relay.Function([], output)
mutated_mod['func_7119'] = func_7119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5920_call = mod.get_global_var('func_5920')
func_5922_call = mutated_mod.get_global_var('func_5922')
call_7160 = relay.TupleGetItem(func_5920_call(), 0)
call_7161 = relay.TupleGetItem(func_5922_call(), 0)
func_5074_call = mod.get_global_var('func_5074')
func_5075_call = mutated_mod.get_global_var('func_5075')
call_7172 = relay.TupleGetItem(func_5074_call(), 1)
call_7173 = relay.TupleGetItem(func_5075_call(), 1)
func_2979_call = mod.get_global_var('func_2979')
func_2981_call = mutated_mod.get_global_var('func_2981')
call_7174 = relay.TupleGetItem(func_2979_call(relay.reshape(call_7160.astype('bool'), [3, 16, 6])), 0)
call_7175 = relay.TupleGetItem(func_2981_call(relay.reshape(call_7160.astype('bool'), [3, 16, 6])), 0)
func_1724_call = mod.get_global_var('func_1724')
func_1728_call = mutated_mod.get_global_var('func_1728')
const_7215 = relay.const([[2,4,7,-7,-3,-8,-9,-10,9,-9,10,-6,5,8,7,-3,7,7,3,3,-4,-8,9,-5,-5,-5,-8,-10,4,-10,1,9,5,4,-9,4,7,8,2,-2,-8,4,7,-1,-3,3,-6,-3,-10,9,-1,5,-6,2,8,7,-3,4,-4,-3,7,2,-10,-4,-10,-10,-5,9,-1,9,8,-7,-4,1,7,-6,1,8,3,-10,3,5,6,-7,-6,-6,2,-5,4,8,-3,-6,2,-4,3,7,-5,-4,-8,-7,1,1,9,-2,4,-6,4,-1,-5,-1,-10,-8,3,-5,-5,7,10,-9,-4,1,3,-6,9,-5,-4,-7,-7,9,-7,2,1,-9,-7,-9,1,2,-7,-3,8,3,4,-6,6,-4,-4,-6,6,-5,6,-6,3,-3,6,7,3,6,1,-2,-9,-2,1,-9,5,-1,-9,-2,-3,-5,2,-1,-3,6,-10,10,5,2,10,-4,-7,-10,10,-9,6,1,5,4,-10,-1,-7,10,5,-9],[-5,-3,-7,-9,2,1,-3,5,6,-5,10,-9,-8,-10,-2,9,-9,10,-3,5,6,-5,-8,-6,-10,5,8,6,2,1,2,-1,-4,8,-9,-5,7,-5,-10,1,1,-9,-9,-7,10,7,9,4,-9,1,5,3,5,1,9,5,-10,-1,9,2,-7,3,4,-1,10,-1,9,-1,1,2,-3,-2,-3,-2,2,-4,-10,6,4,7,1,-3,3,7,-3,6,7,-9,-2,5,-4,4,7,9,9,-9,5,3,5,2,10,-6,-7,-9,5,-2,4,4,-9,-5,1,1,4,-4,3,-9,-5,9,-9,8,2,-4,9,8,-2,-4,-4,9,-8,-9,8,-3,-2,-2,1,-6,3,9,-7,-7,9,2,-8,-5,3,-9,-3,-3,-5,7,-8,-10,10,-10,-8,10,8,-3,10,-3,6,-3,4,-6,-2,8,-4,10,8,5,-6,-5,4,1,10,8,-7,4,8,4,-1,-1,-1,-8,-10,6,5,-10,-1,-6,8,4]], dtype = "uint32")#candidate|7215|(2, 192)|const|uint32
var_7216 = relay.var("var_7216", dtype = "float32", shape = (64,))#candidate|7216|(64,)|var|float32
const_7217 = relay.const([-5.538298,-6.634405,0.261868,-9.485743,9.345426,2.666125,8.808366,2.295721,-0.782532,0.377431,-7.072482,8.228387,-5.577881,-1.990720,-4.329190,7.826823,-7.448040,6.027254,-1.152860,-3.789875,6.238002,-7.296397,-8.559501,-5.848032,-3.106902,1.754824,-3.459603,-2.735828,-3.897053,-6.465012,-3.652611,-1.365020,-8.986938,6.827335,9.430159,-6.068435,9.950332,-5.246800,7.527677,5.154212,-2.433242,-5.417070,5.312999,9.771212,9.102820,-0.732579,0.539025,-9.327270,5.938200,0.962958,-6.135569,1.959083,-8.718900,5.242551,-9.939750,8.235061,2.809555,-1.472403,-9.126418,5.012827,5.263145,-3.503529,-4.104605,-7.706054,-2.696327,-9.522592,-5.893515,-7.745414,9.443541,-4.017151,-1.675318,-3.432525,6.222599,6.421686,2.298458,-7.511812,-7.468740,9.710959,4.640165,-9.503403,1.620521,-9.947539,-6.415699,-0.246123,-0.442745,-9.775079,1.253541,3.282139,0.043960,-1.123070,4.353326,2.868827,0.427433,-4.718635,4.259622,-3.916274,6.184604,-7.202338,-9.352592,-4.136991,8.732573,1.993290,0.308294,4.396055,1.520169,6.304982,-5.310529,0.258996,-2.796875,9.358501,-4.250017,-5.075824,-8.885760,-0.254042,-8.429116,-2.097402,9.114740,-0.406194,-8.410617,1.700668,8.781144,-1.947369,5.624216,-8.652806,4.577465,1.593435,9.634594,1.327517,-6.406412,-7.394284,-0.856207,-1.549270,9.028344,5.443545,8.539162,1.212952,2.378020,-8.097991,7.646728,-5.828275,-0.680994,1.622800,-2.023719,-9.130759,-8.770246,1.326148,4.217256,-6.920552,-9.302868,-5.452051,-9.365551,-4.137891,7.229154,-1.816974,2.639578,1.653517,2.358071,-6.571947,1.672553,-1.634818,3.805225,7.444339,-0.374754,5.350915,3.294585,-1.431603,-9.383707,8.698084,0.918406,-1.484516,7.263310,4.167823,-4.877139,-9.779966,-8.773834,0.519868,-9.865297,-6.713312,-1.054424,0.264417,9.402657,2.379291,-7.393027,2.487059,2.682638,2.129857,9.999072,6.543665,-9.578225,6.246808,-4.031446,-5.362024,2.410796,6.622934,1.436961,7.177635,-0.408103,-6.859009,-4.209385,9.061281,3.195938,-0.370380,2.820195,1.173794,3.736920,-7.223759,4.424114,-8.680080,0.384209,0.422187,-1.566755,1.731997,4.028382,3.509015,0.737270,5.057063,1.276977,4.629785,9.076735,-9.728281,4.774675,1.204037,-8.420334,-7.020480,9.110235,-4.144123,-0.412427,8.553260,5.790984,3.235796,6.593553,7.973556,-5.716945,2.608040,6.873029,-2.817718,-4.598874,-5.981301,6.966048,-2.156679,-3.275153,-2.869581,-8.607588,-0.434463,5.053540,-5.259667,4.810197,4.362205,-4.848735,6.563583,5.342534,-9.949602,5.082235,-4.256264,1.880728,-0.937774,9.019868,8.783128,-9.452202,2.537199,8.822157,-4.176722,2.168510,6.391494,-3.359952,-4.323985,-7.904237,4.624637,1.670025,1.325125,-2.369634,-8.147473,-9.176835,7.282903,4.061774,-8.529646,-3.900709,7.057944,5.089155,0.991266,-8.882565,7.352401,-1.061383,-5.342059,-0.296317,2.235023,6.841528,-5.241794,7.279305,-5.209057,-2.773813,3.790508,0.999710,-4.664754,6.670563,-3.809998,4.837170,0.086988,-2.146338,2.189032,1.013819,5.919607,-8.660441,-3.026694,1.811653,0.904944,-4.870419,-7.483023,0.902417,-4.095194,-3.517138,-0.747987,-6.421519,-2.521060,-1.008842,5.548778,-3.920181,-0.907978,-4.801324,-3.244331], dtype = "float32")#candidate|7217|(320,)|const|float32
call_7214 = relay.TupleGetItem(func_1724_call(relay.reshape(const_7215.astype('uint32'), [384,]), relay.reshape(var_7216.astype('float32'), [64,]), relay.reshape(const_7217.astype('float32'), [80, 4]), ), 0)
call_7218 = relay.TupleGetItem(func_1728_call(relay.reshape(const_7215.astype('uint32'), [384,]), relay.reshape(var_7216.astype('float32'), [64,]), relay.reshape(const_7217.astype('float32'), [80, 4]), ), 0)
output = relay.Tuple([call_7160,call_7172,call_7174,call_7214,const_7215,var_7216,const_7217,])
output2 = relay.Tuple([call_7161,call_7173,call_7175,call_7218,const_7215,var_7216,const_7217,])
func_7223 = relay.Function([var_7216,], output)
mod['func_7223'] = func_7223
mod = relay.transform.InferType()(mod)
var_7224 = relay.var("var_7224", dtype = "float32", shape = (64,))#candidate|7224|(64,)|var|float32
output = func_7223(var_7224)
func_7225 = relay.Function([var_7224], output)
mutated_mod['func_7225'] = func_7225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4076_call = mod.get_global_var('func_4076')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_7227 = func_4076_call()
call_7228 = func_4076_call()
func_7024_call = mod.get_global_var('func_7024')
func_7028_call = mutated_mod.get_global_var('func_7028')
const_7260 = relay.const([[-2.516528,2.720242,8.203091,-4.711134,-4.462963,-7.784639,1.273027,1.451857,3.093500,-0.595376,-5.270569,5.054749,0.873485,-9.411606,-3.428720,-4.776246,-4.114297,-4.851394,-8.755768,-2.657454,-2.855934,4.174531,9.528604,2.033203,1.831015,-9.297883,-3.869819,7.862434,-1.687790,-0.145728,8.656368,-3.511111,-6.605489,-0.333617,3.087955,6.469815,4.222460,5.285485,2.852019,1.134389,-8.045452,1.495823,0.032891,1.867868,-4.843777,7.204407,-0.707722,7.493541,-2.657840,9.519885,-2.790154,-5.867464,8.055522,4.117396,-3.772402,6.615551,-2.035423,1.213360,-2.361622,6.681205,-0.872580,-9.216738,-4.776251,6.659703,9.030771,1.463154,9.886329,-8.450856,3.090828,-6.192993,-4.412423,6.173669,-8.302749,3.604222,0.410555,1.639642,6.195268,-2.816870,-6.025949,-0.276613,-3.296807,3.135693,6.016035,5.689275,3.400444,-2.302679,6.475344,-1.076930,0.882320,-7.020063,7.769962,-0.718467,-9.839580,-9.786072,3.878016,-6.595001,-8.298254,6.839140,6.178948,7.373834,-9.311372,0.901569,8.246725,3.768636,9.321902,0.319160,-7.192097,3.347899,-6.365261,9.712518,-5.715851,8.019327,3.967291,6.388047,4.151018,-5.502820,-8.922985,-5.522442,3.240625,-9.767065,5.464944,6.225790,-4.182947,-7.098382,3.608370,-9.221990,-8.168756,-5.055314,-1.847152,-5.709530,-0.652979,-0.811487,-1.336091,-4.141290,-9.848864,-4.227125,-0.963689,2.627187,-4.668508,2.311732,1.174138,-0.513823,-4.251883,-6.130716,-0.784133,-5.975696,7.652132,3.964200,6.580566,8.321861,1.578966,-9.753040,-1.353946,-6.322702,8.392214,-6.014277,4.635495,-0.243266,9.614665,-3.601346,-8.919347,0.634783,3.860822,5.541267,-8.615412,8.651315,7.773932,-9.320841,4.315416,-6.062252,-4.234597,-6.011516,4.225250,3.024243,5.989880,-0.413943,3.642426,3.522975,3.165719,4.400746,0.085695,7.351571,-8.721880,-8.876595,-4.892869,2.827214,4.188454,-5.105570,-2.180639,-1.002603,0.467281,3.717242,-7.024718,-3.910283,-7.775390,3.989359,-0.247931,-5.058478,-5.217861,-7.066271,6.568572,-4.851179,2.995590,-7.808542,-3.827152,3.889143,1.220031,-4.791122,0.658263,2.944712,9.014285,-7.303208,6.495890,-8.015118,2.589822,-0.879981,-2.677314,-9.804759,9.147112,-6.940083,6.332828,-2.668962,-8.672777,-6.863472,2.040993,8.318235,-8.576524,-8.861341,-0.863832,-0.186349,1.752924,4.871556,8.054622,-5.352618,-1.325935,-9.227983,-9.296913,-9.884551,-7.812707,1.129380,1.727650,-4.015865,-0.742393,3.520112,6.616421,-7.487668,0.190941,5.374335,1.135439,6.338731,-8.174441,9.540980,-3.671307,4.182146,-0.467993,-6.484343,-3.615319,-3.387611,4.565527,4.576429,5.319848,-1.360116,1.034626,0.460696,3.265842,-6.924489,-2.320766,-7.819347,-3.215515,5.931631,-3.207938,-1.286547,-5.249558,9.290378,-4.930602,4.209232,5.081617,-5.281242,5.146687,1.037085,2.189849,-5.025423,-5.727075,-3.370584,-4.181457,1.164203,-0.601110,0.308376,-3.073329,-3.765401,-4.224459,-6.277578,3.251514,-3.376374,-6.433927,7.496538,-8.700136,-8.869237,0.688175,0.173012,-1.816791,-1.027551,-5.363730,-1.438620,2.545732,3.049503,-7.972226,6.950830,8.442985,-9.091019,3.183909,9.011372,1.458381,-8.800805,-9.367635,-0.509899,4.636588,3.386199,8.398343,-0.855922,9.918687,-7.472861,-1.914224,9.728143,8.124228,9.203532,-9.976380,-1.556518,-0.564512,-6.678130,-9.171951,-2.723628,5.365964,9.963209,2.188389,3.559203,-7.804717,-9.743573,8.710957,-7.881492,0.767490,-3.284396,-9.442019,1.942408,4.413910,3.385486,-9.228343,3.739765,-3.966848,-2.610733,7.854835,-7.395017,3.367911,-1.083246,-1.802295,-7.276141,-8.936065,7.255165,3.901683,-9.250624,-2.119577,6.525226,5.752113,0.868921,5.949452,6.913467,2.169687,-2.166167,-4.251718,-3.238558,6.302294,-9.902420,3.938398,-6.534711,-5.865293,2.018756,8.608158,1.222765,-7.305898,-2.379007,2.415131,-2.616647,3.264222,4.243991,1.949309,-8.191675,-4.120609,-7.072592,3.794665,9.212893,8.891375,-1.247831,7.631502,1.655604,-6.971559,9.202429,9.528636,1.973978,9.085299,-1.421004,-2.845705,5.331861,5.484212,-2.193162,2.453765,-8.129306,-7.406636,9.370344,5.434209,1.771794,-8.489384,2.879342,-7.171854,-3.531013,1.304158,-0.456675,7.018428,3.691080,-3.230901,5.742599,4.379104,-7.707256,5.268532,7.407183,5.319207,-3.012100,8.070110,0.658745,-7.319942,6.805479,1.188983,9.917201,-8.341312,6.099090,-8.336939,-6.019764,7.062993,-4.170609,-0.865681,8.674967,-4.938373,7.168631,1.384491,-5.521394,-9.460488,9.962624,6.625611,-6.018831,5.672034,-8.825176,5.898757,2.671738,-9.078081,1.943062,1.320087,-8.538233,-8.949033,-6.173759,-4.981202,-8.097728,-1.844905,-8.107495,-1.455659,8.754191,5.140252,-4.147194,-9.672419,1.857965,3.176666,8.949140,2.832978,-0.022122,5.857788,5.588781,1.769501,-4.395873,1.856923,-3.294103,-3.073964,-2.852387,5.587968,-4.842839,-3.996439,-9.419978,-2.093054,7.350462,0.897477,6.843214,-3.644216,7.294421,-0.174544,7.296453,-2.156071,-1.428085,-5.461527,-7.654929,7.328786,4.598049,-6.483952,9.198677,-5.050469,-9.164698,-5.430449,-3.150038,-4.382011,3.252489,-5.144180,1.849568,-3.105887,6.169264,-6.374115,-6.593913,-7.708315,4.843464,-9.506739,5.335751,4.415380,-8.308719,7.736457,-6.987281,-0.673140,4.050094,4.457531,-3.665362,-1.569982,-1.018217,4.088606,-2.410694,-8.994050,6.522454,-2.844096,5.394289,-9.320351,8.940544,9.162493,-7.799091,9.280352,-3.523808,-9.845491,-8.650350,-6.260067,0.187812,-5.764358,0.722294,3.766305,8.474652]], dtype = "float32")#candidate|7260|(1, 546)|const|float32
call_7259 = relay.TupleGetItem(func_7024_call(relay.reshape(const_7260.astype('float32'), [3, 13, 14]), relay.reshape(const_7260.astype('float32'), [3, 13, 14]), ), 0)
call_7261 = relay.TupleGetItem(func_7028_call(relay.reshape(const_7260.astype('float32'), [3, 13, 14]), relay.reshape(const_7260.astype('float32'), [3, 13, 14]), ), 0)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_7268 = relay.TupleGetItem(func_3507_call(), 2)
call_7269 = relay.TupleGetItem(func_3509_call(), 2)
bop_7271 = relay.logical_xor(const_7260.astype('int16'), relay.reshape(call_7259.astype('int16'), relay.shape_of(const_7260))) # shape=(1, 546)
bop_7274 = relay.logical_xor(const_7260.astype('int16'), relay.reshape(call_7261.astype('int16'), relay.shape_of(const_7260))) # shape=(1, 546)
output = relay.Tuple([call_7227,call_7268,bop_7271,])
output2 = relay.Tuple([call_7228,call_7269,bop_7274,])
func_7279 = relay.Function([], output)
mod['func_7279'] = func_7279
mod = relay.transform.InferType()(mod)
mutated_mod['func_7279'] = func_7279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7279_call = mutated_mod.get_global_var('func_7279')
call_7280 = func_7279_call()
output = call_7280
func_7281 = relay.Function([], output)
mutated_mod['func_7281'] = func_7281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4122_call = mod.get_global_var('func_4122')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_7310 = relay.TupleGetItem(func_4122_call(), 0)
call_7311 = relay.TupleGetItem(func_4124_call(), 0)
output = relay.Tuple([call_7310,])
output2 = relay.Tuple([call_7311,])
func_7327 = relay.Function([], output)
mod['func_7327'] = func_7327
mod = relay.transform.InferType()(mod)
output = func_7327()
func_7328 = relay.Function([], output)
mutated_mod['func_7328'] = func_7328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3461_call = mod.get_global_var('func_3461')
func_3463_call = mutated_mod.get_global_var('func_3463')
call_7421 = relay.TupleGetItem(func_3461_call(), 1)
call_7422 = relay.TupleGetItem(func_3463_call(), 1)
uop_7427 = relay.log(call_7421.astype('float64')) # shape=(11, 4, 3)
uop_7429 = relay.log(call_7422.astype('float64')) # shape=(11, 4, 3)
func_3802_call = mod.get_global_var('func_3802')
func_3805_call = mutated_mod.get_global_var('func_3805')
var_7435 = relay.var("var_7435", dtype = "bool", shape = (4, 72))#candidate|7435|(4, 72)|var|bool
call_7434 = relay.TupleGetItem(func_3802_call(relay.reshape(var_7435.astype('bool'), [3, 16, 6])), 2)
call_7436 = relay.TupleGetItem(func_3805_call(relay.reshape(var_7435.astype('bool'), [3, 16, 6])), 2)
output = relay.Tuple([uop_7427,call_7434,var_7435,])
output2 = relay.Tuple([uop_7429,call_7436,var_7435,])
func_7441 = relay.Function([var_7435,], output)
mod['func_7441'] = func_7441
mod = relay.transform.InferType()(mod)
var_7442 = relay.var("var_7442", dtype = "bool", shape = (4, 72))#candidate|7442|(4, 72)|var|bool
output = func_7441(var_7442)
func_7443 = relay.Function([var_7442], output)
mutated_mod['func_7443'] = func_7443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4421_call = mod.get_global_var('func_4421')
func_4423_call = mutated_mod.get_global_var('func_4423')
call_7449 = relay.TupleGetItem(func_4421_call(), 0)
call_7450 = relay.TupleGetItem(func_4423_call(), 0)
output = call_7449
output2 = call_7450
func_7463 = relay.Function([], output)
mod['func_7463'] = func_7463
mod = relay.transform.InferType()(mod)
output = func_7463()
func_7464 = relay.Function([], output)
mutated_mod['func_7464'] = func_7464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6474_call = mod.get_global_var('func_6474')
func_6475_call = mutated_mod.get_global_var('func_6475')
call_7465 = relay.TupleGetItem(func_6474_call(), 0)
call_7466 = relay.TupleGetItem(func_6475_call(), 0)
output = relay.Tuple([call_7465,])
output2 = relay.Tuple([call_7466,])
func_7486 = relay.Function([], output)
mod['func_7486'] = func_7486
mod = relay.transform.InferType()(mod)
output = func_7486()
func_7487 = relay.Function([], output)
mutated_mod['func_7487'] = func_7487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2689_call = mod.get_global_var('func_2689')
func_2691_call = mutated_mod.get_global_var('func_2691')
call_7564 = relay.TupleGetItem(func_2689_call(), 1)
call_7565 = relay.TupleGetItem(func_2691_call(), 1)
output = relay.Tuple([call_7564,])
output2 = relay.Tuple([call_7565,])
func_7584 = relay.Function([], output)
mod['func_7584'] = func_7584
mod = relay.transform.InferType()(mod)
output = func_7584()
func_7585 = relay.Function([], output)
mutated_mod['func_7585'] = func_7585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4076_call = mod.get_global_var('func_4076')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_7586 = func_4076_call()
call_7587 = func_4076_call()
output = call_7586
output2 = call_7587
func_7610 = relay.Function([], output)
mod['func_7610'] = func_7610
mod = relay.transform.InferType()(mod)
mutated_mod['func_7610'] = func_7610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7610_call = mutated_mod.get_global_var('func_7610')
call_7611 = func_7610_call()
output = call_7611
func_7612 = relay.Function([], output)
mutated_mod['func_7612'] = func_7612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5098_call = mod.get_global_var('func_5098')
func_5099_call = mutated_mod.get_global_var('func_5099')
call_7649 = relay.TupleGetItem(func_5098_call(), 0)
call_7650 = relay.TupleGetItem(func_5099_call(), 0)
output = relay.Tuple([call_7649,])
output2 = relay.Tuple([call_7650,])
func_7651 = relay.Function([], output)
mod['func_7651'] = func_7651
mod = relay.transform.InferType()(mod)
mutated_mod['func_7651'] = func_7651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7651_call = mutated_mod.get_global_var('func_7651')
call_7652 = func_7651_call()
output = call_7652
func_7653 = relay.Function([], output)
mutated_mod['func_7653'] = func_7653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7610_call = mod.get_global_var('func_7610')
func_7612_call = mutated_mod.get_global_var('func_7612')
call_7709 = func_7610_call()
call_7710 = func_7610_call()
output = relay.Tuple([call_7709,])
output2 = relay.Tuple([call_7710,])
func_7720 = relay.Function([], output)
mod['func_7720'] = func_7720
mod = relay.transform.InferType()(mod)
output = func_7720()
func_7721 = relay.Function([], output)
mutated_mod['func_7721'] = func_7721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2822_call = mod.get_global_var('func_2822')
func_2824_call = mutated_mod.get_global_var('func_2824')
call_7760 = relay.TupleGetItem(func_2822_call(), 0)
call_7761 = relay.TupleGetItem(func_2824_call(), 0)
output = relay.Tuple([call_7760,])
output2 = relay.Tuple([call_7761,])
func_7774 = relay.Function([], output)
mod['func_7774'] = func_7774
mod = relay.transform.InferType()(mod)
mutated_mod['func_7774'] = func_7774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7774_call = mutated_mod.get_global_var('func_7774')
call_7775 = func_7774_call()
output = call_7775
func_7776 = relay.Function([], output)
mutated_mod['func_7776'] = func_7776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6329_call = mod.get_global_var('func_6329')
func_6330_call = mutated_mod.get_global_var('func_6330')
call_7815 = relay.TupleGetItem(func_6329_call(), 0)
call_7816 = relay.TupleGetItem(func_6330_call(), 0)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_7850 = relay.TupleGetItem(func_3234_call(), 0)
call_7851 = relay.TupleGetItem(func_3235_call(), 0)
func_5920_call = mod.get_global_var('func_5920')
func_5922_call = mutated_mod.get_global_var('func_5922')
call_7890 = relay.TupleGetItem(func_5920_call(), 0)
call_7891 = relay.TupleGetItem(func_5922_call(), 0)
output = relay.Tuple([call_7815,call_7850,call_7890,])
output2 = relay.Tuple([call_7816,call_7851,call_7891,])
func_7898 = relay.Function([], output)
mod['func_7898'] = func_7898
mod = relay.transform.InferType()(mod)
output = func_7898()
func_7899 = relay.Function([], output)
mutated_mod['func_7899'] = func_7899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mod.get_global_var('func_4536')
func_4537_call = mutated_mod.get_global_var('func_4537')
call_7933 = func_4536_call()
call_7934 = func_4536_call()
output = call_7933
output2 = call_7934
func_7961 = relay.Function([], output)
mod['func_7961'] = func_7961
mod = relay.transform.InferType()(mod)
output = func_7961()
func_7962 = relay.Function([], output)
mutated_mod['func_7962'] = func_7962
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7974 = relay.const(9.088447, dtype = "float64")#candidate|7974|()|const|float64
var_7975 = relay.var("var_7975", dtype = "float64", shape = (5, 7, 9))#candidate|7975|(5, 7, 9)|var|float64
bop_7976 = relay.floor_mod(const_7974.astype('float64'), var_7975.astype('float64')) # shape=(5, 7, 9)
func_6133_call = mod.get_global_var('func_6133')
func_6136_call = mutated_mod.get_global_var('func_6136')
const_7980 = relay.const([[-3.987273,4.366272,4.918740],[-3.313203,-9.968734,7.003082],[2.572432,3.844470,6.679596],[-2.128454,0.794534,7.259549],[-8.108236,-4.462092,-6.345005],[-6.117307,-7.980782,-3.125264],[-4.432410,0.384846,0.166400],[-2.504691,8.813332,9.534606],[-4.646568,-3.293286,-5.858230],[-4.330307,-5.653271,5.660244],[-6.115812,6.110337,4.446173],[9.802494,-1.878547,-1.367900],[9.515023,1.727564,-8.693320],[5.776745,-2.793960,5.265709],[6.136372,3.459648,-1.476493],[-1.232381,-1.934726,5.190231],[-3.153324,5.885214,0.253541],[-3.784630,-9.769748,-4.400998],[-5.490475,1.396517,5.033939],[2.337501,8.025654,9.749902],[6.276962,-9.094645,8.432608],[-9.874242,-0.335457,9.471837],[5.824349,-3.456535,2.606536],[3.397743,-7.837491,-9.183158],[9.842768,-5.877032,-3.974894],[-1.095616,-5.479749,9.706275],[-7.210442,3.385740,8.000491],[-0.264229,-8.178128,-1.363327],[0.865688,8.660600,8.107753],[-4.028313,-4.416513,6.478164],[-3.737524,-2.095255,-3.373269],[-3.430761,1.666670,-6.400614],[-5.501897,-8.492613,6.923402],[-3.364366,-5.966796,4.220481],[6.421069,-0.096705,-8.582287],[-6.469795,0.993483,3.293548],[-2.435012,-2.497672,2.664353],[-7.718892,3.836767,-7.872157],[-0.100270,-7.401017,6.951969],[-8.827505,5.344688,-7.507668],[-3.396966,-1.582117,0.027822],[7.429462,5.634427,-0.680949],[-3.130235,2.472175,6.811842],[1.474970,-1.456660,-8.009651],[0.983752,3.007946,8.771534],[-2.113830,-7.209672,9.721847],[4.646881,-5.592452,-5.947575],[0.457056,1.403117,-9.241982],[5.982602,-3.087202,8.577852],[5.764839,5.532271,2.801341],[-7.419099,-4.625985,-4.205922],[-5.368289,6.143543,4.684330],[0.846870,-6.719597,8.751206],[3.176405,-7.777622,-5.227472],[-4.517707,-1.342090,-2.925464],[-3.547956,-8.719670,-0.298743],[-8.000391,-8.737493,9.474471],[8.356345,-7.108581,6.642562],[3.899014,-0.287561,8.752430],[0.749137,-4.722309,6.242794],[-7.655808,9.235049,9.802666],[2.721308,1.297838,4.527017],[1.045103,5.995636,-2.894319],[0.767002,-4.792923,-7.951358],[5.530015,3.754128,4.385073],[-4.149038,4.739744,-5.920581],[3.022390,-0.595047,8.185067],[2.511483,4.234157,2.264287],[-9.610502,3.895498,-7.986148],[-1.099493,6.655800,-1.574588],[-8.292163,-3.100256,-7.634538],[-0.537639,0.961597,-0.401526],[-8.858881,2.516067,9.773836],[-0.286707,-0.982507,-3.318885],[1.316970,-2.174225,-4.252816],[0.028864,5.989295,-9.626788],[7.745684,-3.222796,-0.235178],[8.401779,-0.873124,-3.013678],[9.990214,4.671449,-3.776201],[7.494289,-0.307705,-0.413515],[-9.271543,-4.875016,-8.956955],[2.296581,2.111208,-1.474257],[0.011974,8.665714,-9.399626],[7.073905,-6.112963,8.796820],[-6.351729,-9.485963,-2.316953],[6.684292,-2.027251,3.367303],[1.535257,-2.364177,-3.799415],[-7.166200,5.615364,2.177941],[0.572675,7.147439,-3.976983],[-2.879465,2.892676,8.143793],[2.696057,-7.773255,-9.003457],[-3.578200,0.705187,4.041025],[1.548970,2.912903,3.886940],[4.622884,1.527822,-3.509611],[6.196058,-7.066464,1.288437],[4.302271,-2.481893,-6.443386],[1.896493,-5.145393,-4.831320],[-7.716476,6.722052,-4.364687],[-8.724027,1.859765,-9.372897],[1.772850,-8.525029,6.559118],[-0.925124,3.137530,-6.597600],[1.797174,-3.090297,-7.938383],[4.057921,8.456969,-8.713203],[0.647294,0.154171,-7.961252],[-9.379189,7.008009,3.729714],[-9.987913,7.020727,7.837604],[-9.969993,9.892521,-9.388954],[1.388547,-2.535529,9.327280],[-0.161001,-8.352110,2.224135],[0.413455,-8.672700,4.024259],[5.134494,0.621937,7.993750],[5.909816,-3.929238,-8.840446],[-6.880217,-3.668473,-9.760863],[-4.645402,8.304621,-7.335521],[9.451576,-0.386538,5.972655],[-4.141947,-5.356747,3.241104],[-7.126802,8.185694,-9.356238],[8.423884,7.170995,6.335303],[1.769305,-0.420778,-7.859550],[-3.066984,-7.068619,-4.626845],[-6.843450,1.465517,-5.745798],[-9.261431,6.065626,1.796701],[4.163803,-0.645388,6.994349],[8.068193,9.888307,3.771224],[-7.662838,-0.225859,-3.988629],[-6.784474,2.276455,2.588552],[6.432040,-8.883078,2.463421],[-2.983617,-6.803336,5.533505],[-2.835006,9.349103,-4.053752],[-0.571214,-3.171539,-5.626983],[9.769606,7.578597,-7.300194],[-4.805985,-3.495613,-3.752658],[6.477863,-3.933354,7.691132],[3.531626,-7.929649,-2.648213],[1.561480,-2.398729,8.882088],[-2.465003,9.605629,8.853138],[2.390080,9.423416,-2.986512],[6.150663,-9.334421,2.155349],[-1.676940,-0.986947,9.281999],[4.679560,5.114659,-5.449462],[-0.391666,5.101414,-6.455672],[1.326772,-4.707739,8.800936],[-7.132862,-5.845856,6.912691],[8.133024,-0.988118,-3.321088],[-8.039825,-3.650504,7.860067],[-0.504016,-2.674041,-7.425076],[-8.663770,-8.141537,-4.481755],[4.413152,-7.010429,-0.938239],[4.760128,6.950902,8.225292],[-4.256061,-7.736157,7.901582],[3.183291,7.683753,7.410413],[7.591942,-0.641164,-8.720919],[5.144202,9.651756,-0.652099],[1.016838,9.759192,6.280974],[9.917577,-8.406298,2.849639],[0.204231,1.668440,-6.572514],[-7.080766,-7.827053,1.240858],[-9.840983,-7.651983,-6.191379],[2.552724,5.111559,0.121994],[9.554498,-6.323289,-1.777771],[3.700954,-9.149013,-0.422027],[8.250177,-7.561685,3.217146],[-4.622633,2.454844,-2.836386],[2.014359,8.052124,-0.161604],[-9.117431,6.715444,-9.225812],[-8.405459,-9.695806,-3.477827],[3.046500,6.505231,-1.571727],[8.759482,-5.631104,7.250852],[-8.693823,-8.712173,1.833672],[-0.756345,-5.175291,-3.187218],[5.082174,-1.154684,-4.436003],[8.796762,-8.744494,5.421018],[3.732974,-3.723200,6.397786],[-6.258113,-6.156346,-8.232857],[-1.866625,7.617240,-3.431308],[6.274143,-3.633836,0.042638],[-5.964919,-9.067339,-7.356084],[4.077995,-6.668670,7.078916],[-6.657479,-1.346654,1.356638],[-3.934739,6.768311,-0.203751],[-2.749532,-0.952144,-7.244450],[1.383697,-7.655861,1.788396],[5.137402,-8.563785,-0.398921],[-5.552572,-8.543976,-3.187714],[5.499501,3.580681,-6.554648],[-3.359360,2.013573,-6.670321],[7.956436,-5.182348,1.051112],[-3.919679,2.775211,5.395528],[-2.018534,-7.525666,-9.545932],[-7.881972,9.246015,-6.839288],[-9.156042,-4.265463,9.216598],[3.811962,-6.475888,-2.256178],[3.934058,5.000594,-3.803726],[7.937619,-0.760169,2.302917],[-5.027478,-8.483451,3.600744],[5.255991,9.033376,1.093826],[-2.167863,2.795980,-7.088586],[7.228130,-1.364301,-5.334882],[3.636398,-0.133232,7.973897],[-2.154597,5.887620,-2.599358],[3.526010,-8.098635,5.027677],[-5.227227,-9.724139,3.323068],[4.264102,1.649754,4.099147],[-9.175244,9.330736,-3.306847],[-4.763175,-2.698271,8.058932],[-8.724911,-1.755189,0.316554],[-7.949793,-2.829798,-4.938347],[-9.290505,-5.627902,5.761382],[0.021328,-0.736712,-3.917413],[-5.726696,4.944252,2.333726],[9.503692,2.196293,-3.888835],[6.255232,-5.874530,-5.329552],[3.453916,1.494232,-8.212951],[2.078004,-9.831249,-8.915288],[-8.781227,-3.892903,2.155019],[-2.214436,7.609120,-4.390089],[0.395792,8.644675,8.310551],[-5.918787,-6.959905,-8.327072],[-9.499347,-8.966610,1.236427],[-6.567448,5.585528,0.485318],[-7.819631,7.426429,-0.139972],[8.740998,-0.739407,5.396195],[-5.473212,-6.442677,6.575774],[9.287096,4.361211,6.964429],[-0.723985,-7.667230,-9.688632],[-0.737539,-0.742144,-7.992309],[-7.247653,-9.239919,-3.707210],[-5.491894,7.424020,4.353240],[-4.627284,-8.602518,7.022664],[-5.314067,8.566809,5.646947],[5.227844,-3.760567,-5.126379],[-1.698238,6.418470,9.455345],[-0.346529,-4.884372,-1.410791],[6.763772,4.295268,-3.422608],[0.801874,-8.420732,-9.071119],[-5.772705,-9.652968,9.759760],[4.724983,6.856531,-9.903424],[6.891742,-5.881166,-7.868160],[2.744860,2.949350,6.115376],[1.800712,0.843935,-4.757452],[-4.430857,6.651870,2.068498],[5.355839,-1.739833,4.127478],[0.152983,6.616089,4.057104],[-5.168800,8.698918,9.506529],[-9.833692,8.621378,-0.928122],[8.266203,-9.186556,7.663759],[2.410862,4.233057,0.815416],[-5.321616,5.400420,4.756119],[6.419758,4.684013,3.177525],[6.825968,-6.675592,2.434827],[-5.159184,8.080248,8.189678],[1.386354,1.122957,-9.268161],[8.669407,5.835752,4.709891],[2.580821,-8.310617,7.883581],[6.391612,7.468026,-2.985955],[9.472700,4.343191,5.703666],[4.149361,5.988916,1.578806],[-7.734502,-5.578077,5.542688],[-0.705245,-1.692334,-2.428122],[-4.579514,3.618778,2.037917],[7.586084,-3.481015,4.681975],[5.881191,-7.381190,8.280986],[5.015049,1.402656,4.985281],[7.197608,8.890221,-4.014321],[8.980800,-0.442667,0.542749],[-8.778519,-8.679004,7.107694],[5.567200,-9.033391,-5.781344],[5.137185,0.290596,7.991027],[-8.855396,-7.732406,2.289993],[8.740522,-7.716633,3.325595],[9.790749,-3.715370,-5.537129],[7.882454,-4.494607,-1.513840],[8.857339,-2.156730,-2.850943],[7.856454,-4.513586,-5.568224],[-3.330215,2.378591,2.305622],[-7.926259,-6.560532,-4.617552],[2.384450,-4.257121,-0.252892],[-8.228354,5.480018,-6.472080],[-6.656940,-7.268259,-3.067337],[-0.608683,-3.472372,6.606551],[-6.601053,-8.731156,-3.566704],[-3.688750,-6.233849,9.431955],[0.751109,-2.053346,6.036349],[-7.282999,-6.390060,-6.888843],[7.865805,7.358639,-7.556491],[-9.248707,6.444016,-1.793467],[6.155914,2.324116,9.818830],[-9.297228,-4.335573,4.517397],[-0.449039,5.623834,-0.922949],[7.714934,8.571248,0.720062],[8.947194,-1.667755,-9.649915],[-8.491905,0.467370,2.074102],[-6.315073,0.652103,-9.928325],[-4.509042,-8.202557,8.406110],[-3.677628,1.568856,-9.328442],[3.556642,-8.352471,-9.768593],[-8.774263,-8.754319,-0.297683],[2.683886,-6.465650,0.200062],[4.950950,8.602488,2.219320],[9.172301,7.486997,9.560753],[2.294908,4.513354,0.010849],[4.634403,-3.110388,2.007383],[2.529906,0.816770,-8.275095],[8.587207,6.664284,7.519410],[2.480169,-1.434628,3.838348],[-8.554454,-9.204692,-7.250078],[6.873614,-5.306717,-4.965533],[-8.003033,-2.468444,2.431980],[-4.849914,-3.875850,4.348168],[1.218886,-7.413543,0.500716],[5.638843,7.285299,1.106452],[9.931263,9.744543,-7.366166],[-8.646082,0.269482,-9.025226],[9.509820,1.576196,-1.113940],[0.586870,-6.326214,6.213765],[-5.249151,4.779948,4.406955],[7.980488,-7.403292,-4.078318],[-1.554864,1.396166,5.266315],[-9.141134,4.460092,-2.775866],[-0.138178,7.506607,-1.315786],[-2.045182,6.380726,-4.272646],[-8.459140,-6.874911,-5.087532],[9.700462,4.143394,-5.849540],[5.737069,4.096817,7.881254],[-4.197938,6.784628,-6.194850],[3.099466,-1.191225,-8.385549],[6.228884,5.489344,8.314954],[-5.011620,-9.195850,-9.719875],[-4.158575,-6.734278,-7.727242],[5.405909,7.766492,-3.392115],[-3.870355,3.865972,-8.764508],[3.889058,-4.366040,8.568275],[-3.995444,6.152147,6.868598],[-5.382432,4.695925,5.560156],[-6.860026,-9.241991,-3.126725],[5.100938,-5.689829,3.252727],[-3.124998,-2.578412,9.511221],[7.303838,9.003111,9.272172],[-9.723182,-4.972181,-3.385201],[1.120308,8.574302,-5.257044],[-2.037085,-0.136197,-4.645522],[1.095009,7.353332,-5.508899],[-4.647076,-0.673702,-2.857428],[-2.461096,4.567268,-2.906028],[0.238404,-7.038263,6.637687],[-8.739739,-4.548269,0.128327],[-9.630759,-8.527900,-8.159328],[6.892492,-6.763566,0.277856],[4.903803,4.018834,-3.904410],[-5.566713,8.752903,-9.695477],[3.245178,-7.827281,-0.035049],[4.016179,-0.157869,-8.510247],[-8.105922,3.494639,4.462848],[3.049208,8.263990,-2.221644],[-8.445952,0.861074,8.732585],[-2.505445,-5.563036,2.801414],[-8.275877,3.083049,-0.791297],[-0.055271,1.841271,7.523515],[-9.276204,2.543065,4.311949],[5.917612,-1.228500,3.338174],[4.023883,2.141720,-2.004569],[-3.183704,1.967728,0.835476],[5.982462,-5.281265,-7.022772],[8.545790,-2.334285,-6.966359],[-7.598328,7.268079,-3.214343],[5.514650,-9.903208,1.774555],[2.074146,-8.234826,5.641524],[-0.351811,6.226510,-8.326540],[-9.955526,-0.307538,-1.927301],[-7.816156,-9.964095,-9.475876],[-5.419360,-9.040388,-4.392497],[8.211090,4.659967,-8.410599],[6.684097,2.778495,7.487865],[-0.058422,-7.121652,-2.518224],[4.442909,3.926851,-2.547226],[-2.081692,8.041555,7.403557],[-0.293272,5.504218,-1.691355],[7.205382,-8.291073,-0.717797],[-2.189834,9.976252,1.445542],[2.416919,-7.492252,4.323695],[-1.476368,5.377306,-3.480248],[0.495298,7.983523,2.668176],[-9.559166,-8.053280,9.379776],[-7.573297,5.000245,-6.563239],[9.924027,-2.767077,0.038615],[-7.263689,5.492824,9.299390],[4.244613,8.037212,-2.440277],[-8.998416,3.827107,4.440670],[-4.428743,-2.790894,-4.466660],[-1.457374,-3.581039,7.454978],[-3.763721,-6.226178,-2.968017],[-2.400029,-6.156073,-0.585256],[-8.509273,-8.414539,3.219659],[-8.067862,4.628631,-7.951535],[-8.174557,-7.535631,6.081705],[-1.385047,1.103813,8.699914],[-6.642996,2.406759,6.941405],[1.543203,9.107583,4.246777],[-4.059591,-6.311653,-4.013516],[9.469996,5.767711,-7.220110],[1.259994,7.679299,9.728998],[-9.023914,-4.384862,-3.564803],[-4.258299,6.372871,9.717316],[-3.059990,-7.256768,-4.831685],[7.707319,5.285770,7.216035],[5.911204,-1.468478,2.078431],[-7.479498,-1.738777,-4.626126],[-1.999300,-2.862271,-5.255747],[1.527142,4.824712,5.187806],[-6.962711,3.411195,8.994284],[0.127907,-4.608186,9.591801],[6.416267,2.526288,-2.087730],[1.986370,-6.564565,-3.536226],[8.911004,-7.560224,-4.517265],[-7.356505,-3.105218,-3.886806],[-5.616398,2.173483,-1.592498],[7.732037,-7.760380,3.797431],[-1.614191,0.123039,-1.650583],[3.285115,1.117331,4.730540],[0.367011,7.862649,8.781973],[2.124193,4.987540,-5.289216],[-0.414301,-8.157301,3.406445],[9.792371,-4.355736,-6.694559],[9.364502,-1.415666,3.528133],[-0.986214,-2.585671,8.506328],[2.089872,8.849033,7.124684],[-5.835516,5.101297,-0.374793],[-4.281124,-4.505669,-3.588073],[-6.318461,-0.023804,5.257171],[-0.546931,-3.491704,5.660323],[-6.903482,1.596320,7.024520],[-4.481451,-3.460505,-7.279771],[-9.374428,-4.301296,3.172535],[3.530600,-4.408271,0.696339],[-0.835796,8.947011,-7.426386],[-4.006425,-8.664468,-0.573745],[-9.739330,8.913118,8.485815],[6.452423,7.393218,-0.382719],[-5.785770,-7.523910,-5.228141],[-2.591761,4.830567,0.652561],[-7.356663,-3.196592,7.540562],[0.164604,2.195133,-9.643820],[-2.549844,-2.645092,-9.370988],[3.523617,5.557241,3.814959],[3.201814,-0.183915,-6.476172],[-3.688900,9.321422,2.153736],[8.573879,-6.993952,6.817608],[7.663634,-2.626400,3.057493],[8.450530,3.142085,-5.101838],[-3.297171,6.807987,-0.849154],[-5.183870,-5.411551,-7.685144],[3.668504,-5.371013,-2.806248],[-0.826059,-0.088233,-2.954222],[2.160334,-3.035141,-9.729831],[-3.487459,-1.048957,7.593643],[2.471301,6.225564,8.689582],[6.475956,9.730813,-2.749355],[2.759188,-4.442336,2.709256],[-6.974493,-8.225082,9.358886],[1.649323,7.082866,3.931306],[7.934425,-4.019256,9.429852],[-0.216806,-5.782369,-6.899526],[2.077366,-4.566994,6.317822],[-1.986194,-4.866011,-2.892536],[5.643218,5.406114,6.647734],[2.126525,8.573255,2.853467],[5.168360,8.669820,-1.776056],[-5.321463,-3.166250,5.781600],[-2.576282,5.923629,-0.222948],[4.209952,1.488873,-4.379367],[0.081637,1.083087,2.303554],[9.563767,-6.566504,4.807233],[8.126314,7.817553,-7.050152],[8.132734,-3.675894,8.855354],[2.166924,2.773070,-6.077835],[7.235457,9.487431,-2.609212],[-9.428195,-2.435128,5.876993],[4.840166,1.267517,-6.981061],[4.266643,6.473545,-4.952654],[-8.835899,1.568775,-4.170124],[4.610165,5.999401,4.507698],[9.970987,-4.678407,-5.337212],[1.674823,-8.980892,-3.841446],[-8.779399,-9.375557,-5.025164],[7.904171,-4.960164,-0.606468],[-0.020004,5.923389,-3.634057],[6.030976,-7.573690,1.857806],[8.195716,-6.880433,-4.532094],[-8.245849,-9.534798,-8.353855],[1.039941,1.267956,-3.292284],[9.352719,7.696888,-0.221134],[1.742411,8.943948,3.367108],[-1.982579,-7.005152,-9.238788],[-5.631544,3.606231,-7.511103],[5.516703,4.814588,0.763671]], dtype = "float32")#candidate|7980|(495, 3)|const|float32
call_7979 = relay.TupleGetItem(func_6133_call(relay.reshape(const_7980.astype('float32'), [1485,])), 1)
call_7981 = relay.TupleGetItem(func_6136_call(relay.reshape(const_7980.astype('float32'), [1485,])), 1)
output = relay.Tuple([bop_7976,call_7979,const_7980,])
output2 = relay.Tuple([bop_7976,call_7981,const_7980,])
func_7983 = relay.Function([var_7975,], output)
mod['func_7983'] = func_7983
mod = relay.transform.InferType()(mod)
mutated_mod['func_7983'] = func_7983
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7984 = relay.var("var_7984", dtype = "float64", shape = (5, 7, 9))#candidate|7984|(5, 7, 9)|var|float64
func_7983_call = mutated_mod.get_global_var('func_7983')
call_7985 = func_7983_call(var_7984)
output = call_7985
func_7986 = relay.Function([var_7984], output)
mutated_mod['func_7986'] = func_7986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6875_call = mod.get_global_var('func_6875')
func_6877_call = mutated_mod.get_global_var('func_6877')
call_8000 = relay.TupleGetItem(func_6875_call(), 0)
call_8001 = relay.TupleGetItem(func_6877_call(), 0)
func_6963_call = mod.get_global_var('func_6963')
func_6964_call = mutated_mod.get_global_var('func_6964')
call_8002 = func_6963_call()
call_8003 = func_6963_call()
output = relay.Tuple([call_8000,call_8002,])
output2 = relay.Tuple([call_8001,call_8003,])
func_8025 = relay.Function([], output)
mod['func_8025'] = func_8025
mod = relay.transform.InferType()(mod)
mutated_mod['func_8025'] = func_8025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8025_call = mutated_mod.get_global_var('func_8025')
call_8026 = func_8025_call()
output = call_8026
func_8027 = relay.Function([], output)
mutated_mod['func_8027'] = func_8027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4596_call = mod.get_global_var('func_4596')
func_4597_call = mutated_mod.get_global_var('func_4597')
call_8051 = relay.TupleGetItem(func_4596_call(), 0)
call_8052 = relay.TupleGetItem(func_4597_call(), 0)
output = relay.Tuple([call_8051,])
output2 = relay.Tuple([call_8052,])
func_8053 = relay.Function([], output)
mod['func_8053'] = func_8053
mod = relay.transform.InferType()(mod)
mutated_mod['func_8053'] = func_8053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8053_call = mutated_mod.get_global_var('func_8053')
call_8054 = func_8053_call()
output = call_8054
func_8055 = relay.Function([], output)
mutated_mod['func_8055'] = func_8055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4479_call = mod.get_global_var('func_4479')
func_4480_call = mutated_mod.get_global_var('func_4480')
call_8065 = relay.TupleGetItem(func_4479_call(), 0)
call_8066 = relay.TupleGetItem(func_4480_call(), 0)
func_5975_call = mod.get_global_var('func_5975')
func_5977_call = mutated_mod.get_global_var('func_5977')
call_8138 = func_5975_call()
call_8139 = func_5975_call()
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_8142 = relay.TupleGetItem(func_1522_call(), 1)
call_8143 = relay.TupleGetItem(func_1524_call(), 1)
func_6329_call = mod.get_global_var('func_6329')
func_6330_call = mutated_mod.get_global_var('func_6330')
call_8171 = relay.TupleGetItem(func_6329_call(), 0)
call_8172 = relay.TupleGetItem(func_6330_call(), 0)
output = relay.Tuple([call_8065,call_8138,call_8142,call_8171,])
output2 = relay.Tuple([call_8066,call_8139,call_8143,call_8172,])
func_8185 = relay.Function([], output)
mod['func_8185'] = func_8185
mod = relay.transform.InferType()(mod)
mutated_mod['func_8185'] = func_8185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8185_call = mutated_mod.get_global_var('func_8185')
call_8186 = func_8185_call()
output = call_8186
func_8187 = relay.Function([], output)
mutated_mod['func_8187'] = func_8187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8053_call = mod.get_global_var('func_8053')
func_8055_call = mutated_mod.get_global_var('func_8055')
call_8230 = relay.TupleGetItem(func_8053_call(), 0)
call_8231 = relay.TupleGetItem(func_8055_call(), 0)
func_4015_call = mod.get_global_var('func_4015')
func_4019_call = mutated_mod.get_global_var('func_4019')
const_8245 = relay.const([-2.424814,-5.266226,-9.276091,-8.248208,-5.962483,1.451285,-7.296859,8.172634,9.877635,-2.463135,4.484935,2.491099,4.073305,-8.230718,-8.807375,0.790029,-7.051069,8.663230,-3.610986,-9.002222,9.745348,6.419208,1.429467,-4.468089,-6.749381,-7.770178,5.359808,4.764406,-1.930010,3.264853,-3.690421,3.362858,-0.869726,7.438365,5.703897,3.532207,3.511766,-7.397169,7.961417,5.956740,-8.139197,9.787691,-1.775086,-8.958094,7.220399,7.124708,-1.237464,-3.604725,6.676573,6.114453,-7.805475,2.199993,9.926878,-6.643950,-0.299844,-1.194520,5.135501,-0.911938,-5.072757,-2.647101,-2.407942,6.446583,5.699025,2.888868,7.607083,4.640570,1.553763,-0.810417,-2.546871,-7.812019,-2.807516,1.044153,-0.489346,4.865528,1.302889,-9.780381,4.140650,-7.071181,-6.026757,5.456685,0.844980,9.522063,9.194521,1.897393,-8.507403,0.204675,0.923951,7.935420,-6.045595,-0.935258,-7.697880,-8.034559,9.237424,-3.209807,-7.968895,9.095226,-6.979771,7.234925,-4.901887,-8.748206,-5.418478,-7.601734,-8.649071,7.039026,-8.742296,-2.215399,0.125916,8.447601,-7.669060,-1.612090,4.630915,-7.839993,-4.262011,-1.536583,-9.592688,7.912323,-8.194740,-7.773476,6.210083,2.336921,-8.081140,8.332739,-6.400124,-0.390146,-4.693536,-6.142686,-0.269150,-7.371707,-6.352745,-9.095208,8.875046,4.211742,2.750412,-3.160576,0.048012,-5.396377,-0.616958,9.861860,-4.416694,8.198938,-9.614203,8.386668,-7.958019,0.920482,-7.976134,7.149975,-5.006934,3.454946,2.542495,-6.413818,5.202333,-9.171949,-4.834627,0.309641,5.634733,-4.433715,-8.159486,-4.741881,8.134715,5.719448,6.089393,6.579506,8.441379,8.942161,-1.452634,6.419297,9.448753,7.279062,-9.195803,-8.073319,9.077884,5.616266,-7.852623,-8.426562,-7.220929,0.925337,8.221280,4.388404,3.948158,8.833260,-8.403287,-3.170787,-0.828685,-5.771171,-9.042439,-6.592960,4.152250,5.398641,1.733723,4.962470,1.084131,-7.582776,4.761255,1.367724,-8.801037,-5.528426,9.755182,-4.675220,1.748861,-9.527532,-5.899985,9.690600,8.457412,2.500846,1.112615,-9.205380,-0.847485,5.867764,-6.331322,-6.588636,2.847531,3.615227,1.753004,-2.454265,-1.239166,-1.297360,0.425375,-4.687786,-2.510432,7.941594,-2.160573,-7.679483,-8.116337,-4.411930,-9.637952,-3.770527,-3.934173,4.943235,0.572845,-7.000901,-9.127050,-8.184934,-6.394045,-3.356251,0.533981,-7.649983,0.882892,-8.576003,-0.836666,-2.392647,6.225459,-7.752315,9.684624,-5.800105,4.700931,-4.369925,7.358484,6.249800,-1.497696,5.732912,-1.286429,4.480607,-4.464887,9.017446,4.277720,-1.184009,-2.590574,-7.173195,-6.426350,4.031854,9.333242,2.346641,-1.182038,-2.314473,8.932177,-6.763242,-1.718873,4.484650,0.082371,5.743677,2.784504,-6.645946,2.158396,3.778599,6.319766,9.375706,-7.588592,6.847195,-5.501850,9.884565,8.338162,0.435733,-2.624994,6.247989,8.602044,-7.508034,-5.336886,4.108713,4.223137,9.750605,4.414959,4.717705,6.550743,-3.049755,-2.423661,4.704736,-7.201735,1.665971,-6.671566,-2.966029,-9.690028,-0.467185,5.475012,-4.845425,-3.400116,3.318441,-9.427624,8.055201,-8.457537,3.888985,-6.770655,-7.568782,9.627537,4.231912,-2.564238,-2.061936,-7.526893,2.919540,-2.333390,-6.261027,3.600899,-9.390250,-5.383511,-4.570275,4.997291,3.341847,-3.228055,-5.341526,-3.106131,8.698989,-7.466806,8.066295,-3.301121,-3.404580,-5.560479,6.784096,6.348684,0.971648,-1.304074,-4.211603,-3.817151,2.366863,7.982676,-8.575955,7.031320,0.593607,6.131964,-3.840469,4.785171,-9.610882,3.090797,-1.386670,5.385338,-4.371737,7.297165,-9.756263,-5.522335,-4.110282,4.665245,3.420313,5.288325,-6.666221,0.247803,-2.951023,-0.385772,-2.282651,2.620106,-3.081513,8.341403,-6.703200,1.174824,-8.670750,-8.201876,6.223250,6.650643,-4.764947,6.465332,-7.037424,7.897762,-7.579500,6.994736,1.264304,6.004391,-4.777288,-0.850707,0.541325,3.960767,0.290566,-7.479866,5.131460,-9.225230,-6.206834,2.373915,-6.108964,-8.641296,-5.955998,-2.457288,-7.731901,9.336249,-3.236609,1.046188,3.159727,0.011948,-7.118523,7.237963,6.273801,6.153899,-7.199187,-5.827439,4.653472,5.182363,4.748756,8.557741,9.964638,-1.500829,-9.424147,6.268833,-7.634350,-0.231781,-6.729984,-9.357680,9.009293,-7.992215,-5.094541,1.466011,3.555932,6.599399,-2.866798,-7.884935,4.803565,9.377855,-4.963881,0.149783,9.591640,7.398798,-2.435774,3.295302,6.177618,6.444377,7.073069,9.386471,5.933403,2.656977,2.945523,3.160632,-8.085202,-8.910201,8.871344,6.749911,8.998825,-4.973169,-6.787694,-2.533425,0.138472,-9.209247,-2.465509,2.505799,-6.500186,9.739525,-7.503886,7.731058,3.624165,0.186430,7.406791,0.661695,5.055208,-2.038668,7.292623,8.133823,-3.709437,8.819447,6.405669,-2.218449,2.317076,2.081548,-7.310042,-5.837939,-6.134221,-9.965810,-5.624120,0.550592,-6.221088,-2.247839,-9.933729,-6.540028,6.891700,4.067919,6.563858,-9.494286,7.885012,-5.215335,-7.619683,3.700967,7.348430,1.287221,9.079530,8.370221,-7.998254,9.826212,-8.338066,-6.582573,-5.687090,-1.022374,8.019354,-9.279700,9.353750,6.678025,-7.151337,-2.223344,-4.335614,9.461702,-0.335721,2.965712,-3.049975,1.175380,1.881239,-0.883562,8.188721,3.099568,-0.272095,7.747753,-1.604444,0.158391,4.952604,-2.842675,4.558208,5.048454,6.695007,9.502572,-0.598295,-9.253860,-0.087606,1.590268,1.252431,-5.245666,-3.111388,2.562165,-5.845286,1.513196,7.169965,-7.446915,-2.383638,-1.821862,-9.534801,8.403887,8.037682,-7.067082,1.636929,7.589125,-8.308871,-4.396959,-4.309033,-3.516023,-0.505546,-6.478000,4.087726,2.308797,8.099733,9.954216,6.260968,-3.001158,-7.113532,-7.005502,-0.338448,6.875591,0.800301,7.232926,3.396109,7.539267,-3.055320,8.106527,-8.416545,1.635875,3.854606,9.176257,3.279237], dtype = "float32")#candidate|8245|(576,)|const|float32
const_8246 = relay.const([7,-10,2,-10,-10,-6,4,10,-4,-3,6,3,8,1,6,-1,-9,8,9,-4,4,9,-9,-9], dtype = "uint32")#candidate|8246|(24,)|const|uint32
const_8247 = relay.const([False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False], dtype = "bool")#candidate|8247|(320,)|const|bool
call_8244 = relay.TupleGetItem(func_4015_call(relay.reshape(const_8245.astype('float32'), [576,]), relay.reshape(const_8246.astype('uint32'), [24, 1]), relay.reshape(const_8247.astype('bool'), [320,]), ), 0)
call_8248 = relay.TupleGetItem(func_4019_call(relay.reshape(const_8245.astype('float32'), [576,]), relay.reshape(const_8246.astype('uint32'), [24, 1]), relay.reshape(const_8247.astype('bool'), [320,]), ), 0)
output = relay.Tuple([call_8230,call_8244,const_8245,const_8246,const_8247,])
output2 = relay.Tuple([call_8231,call_8248,const_8245,const_8246,const_8247,])
func_8252 = relay.Function([], output)
mod['func_8252'] = func_8252
mod = relay.transform.InferType()(mod)
mutated_mod['func_8252'] = func_8252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8252_call = mutated_mod.get_global_var('func_8252')
call_8253 = func_8252_call()
output = call_8253
func_8254 = relay.Function([], output)
mutated_mod['func_8254'] = func_8254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4240_call = mod.get_global_var('func_4240')
func_4241_call = mutated_mod.get_global_var('func_4241')
call_8279 = func_4240_call()
call_8280 = func_4240_call()
output = relay.Tuple([call_8279,])
output2 = relay.Tuple([call_8280,])
func_8281 = relay.Function([], output)
mod['func_8281'] = func_8281
mod = relay.transform.InferType()(mod)
output = func_8281()
func_8282 = relay.Function([], output)
mutated_mod['func_8282'] = func_8282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5975_call = mod.get_global_var('func_5975')
func_5977_call = mutated_mod.get_global_var('func_5977')
call_8360 = func_5975_call()
call_8361 = func_5975_call()
output = call_8360
output2 = call_8361
func_8393 = relay.Function([], output)
mod['func_8393'] = func_8393
mod = relay.transform.InferType()(mod)
mutated_mod['func_8393'] = func_8393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8393_call = mutated_mod.get_global_var('func_8393')
call_8394 = func_8393_call()
output = call_8394
func_8395 = relay.Function([], output)
mutated_mod['func_8395'] = func_8395
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8425 = relay.const([[[6.040419,-7.613454,7.009143,6.207020,4.730060,4.129453],[-4.616631,8.912068,-4.790008,1.859365,0.117268,0.509799],[4.458842,9.846456,-8.463593,-3.458600,-9.637118,-9.774206],[1.044763,7.401726,-6.801933,-3.861311,5.286688,-3.539062],[-3.033855,-5.569078,-3.642312,2.190173,-5.737892,8.108538],[4.295951,-5.269206,-6.731321,3.408204,-5.769358,-2.495991],[9.380157,5.068047,3.267328,-8.984225,-8.058452,1.324193]],[[-8.595455,-9.797874,8.510608,-8.208954,7.924057,8.297589],[4.651112,-7.543152,1.941409,-9.976433,1.994054,-0.757109],[-0.039831,-6.089518,6.524762,1.958428,-7.979793,-9.280549],[1.548154,-0.473517,-3.813931,-6.489735,-6.390487,9.362488],[1.811475,-9.717074,-7.738063,1.978746,-7.721629,6.162847],[9.779222,4.534440,-4.118229,-3.462334,-2.499455,8.818474],[-8.212112,-5.909778,-4.466300,-2.945176,-9.016192,-1.651951]],[[0.794863,0.654022,-9.067062,9.802658,5.857512,9.567254],[9.237466,3.914349,4.343085,-2.298355,-7.663633,-5.115192],[-1.607348,-3.573807,-1.093418,6.194032,2.269005,1.607993],[7.763290,2.722446,4.475101,2.410632,-6.607206,8.468535],[3.165073,1.763490,-1.535448,-7.927494,6.313952,9.296778],[8.799735,5.759118,8.119053,-8.707651,-1.044834,9.417673],[1.523933,-8.877106,0.494360,2.894295,7.269640,-0.725568]],[[-6.371509,-0.008680,-2.266238,6.916853,4.391114,-5.717570],[3.180100,3.156747,-8.366172,-8.225462,7.078930,-1.720246],[-5.924858,8.996376,-3.844998,2.066807,-9.432646,-0.580960],[-0.354193,0.838454,9.944828,-1.476203,-7.985262,-5.051581],[1.301006,-3.582574,7.235205,0.341396,-9.881130,1.979735],[6.111252,-5.665954,-9.005023,-3.510610,-5.142550,-2.859230],[7.670748,7.741651,5.297880,-0.046912,-1.989286,9.526600]],[[8.308758,5.244808,-6.996381,0.522471,7.192999,5.403738],[-1.305342,-8.247320,0.201514,-8.924204,-7.105663,7.309103],[2.771287,-0.572015,-8.830794,2.792581,-6.880532,-2.049138],[9.763698,-7.273036,6.756878,3.836874,9.740156,-4.725967],[-6.823570,5.639043,-7.973177,-0.211114,4.221121,3.649726],[5.335213,7.763781,6.042080,-5.268721,4.325850,-7.724574],[-6.476861,1.386154,4.817136,1.173409,-1.875319,-1.707790]],[[7.683385,7.433237,5.826353,-5.732713,7.766249,6.209868],[3.750082,-6.586528,-8.942907,6.574611,-0.362060,6.447650],[7.196030,8.273128,2.953299,-8.040868,0.201823,6.248780],[1.790401,1.008949,-6.705037,2.581778,-7.844484,-3.083951],[-0.272879,2.714068,-5.160212,5.491689,1.418296,-1.909285],[-6.713402,5.846967,-0.041231,7.661669,6.943644,-8.288617],[7.915682,7.321278,6.482057,-2.491937,-1.814795,-3.455361]],[[-1.053811,-6.988789,1.920330,1.332062,1.284685,4.601193],[8.314138,6.462395,0.697579,-0.816667,-3.669815,-6.091499],[-4.674694,9.538767,-3.135253,8.037426,2.439493,8.941071],[-2.512317,0.361858,1.010053,5.147014,7.962328,6.148243],[8.876240,0.887331,-0.843262,5.053465,-9.848561,9.793655],[3.257468,-1.383025,-1.347730,6.985229,-8.948910,-5.473824],[3.788282,-2.954738,8.082525,7.899568,-3.149400,-7.424786]],[[-7.056070,1.450536,-0.988202,7.567124,3.589838,1.886537],[4.840493,0.799606,8.861052,-9.203130,3.244233,3.973625],[-4.179094,5.638000,0.858758,3.631632,-3.897727,-2.049049],[3.746442,-0.287691,0.364736,-8.005170,-8.912384,-3.618288],[-4.770085,-3.268068,-7.829971,-0.208146,-2.509040,6.076068],[7.528158,0.608932,1.235799,-4.313775,7.349018,3.132829],[-0.873020,-8.563744,8.553354,-0.942440,5.778117,-2.297330]],[[-8.561145,-6.752287,-9.965865,-9.570420,1.106028,9.230974],[-3.547468,3.200844,-6.338750,-7.549453,0.775996,8.615488],[-7.498918,-4.633865,-5.867112,3.425302,4.059274,4.286332],[8.298290,6.988217,5.968230,8.954352,-3.651508,-1.981157],[0.502114,-4.388962,5.199182,-8.662206,8.290104,9.629863],[3.494183,3.641159,-6.198817,-9.533657,-1.878966,-9.607265],[3.167252,1.613586,2.554730,-4.535263,1.316843,2.087668]],[[0.647644,-3.545675,-0.567259,-5.482360,-9.125637,-1.814785],[0.654972,-7.457306,-3.807312,7.929133,-5.302695,8.323831],[-1.795076,-0.494502,-0.596358,-4.245819,3.996153,5.854820],[-7.841966,9.462593,2.839771,-4.234947,3.314528,-3.851615],[3.788428,9.561665,5.754533,1.391331,-9.496778,1.534081],[9.587227,-9.828773,-3.181782,-3.754432,-8.896428,3.862723],[2.596943,-1.850985,-3.989712,-6.912822,-6.849153,5.929738]],[[3.901965,-4.006209,-7.625030,-4.959812,7.394820,5.426534],[-7.593894,8.229439,5.426896,-6.687883,-8.705742,9.821478],[-1.186330,-2.039258,2.361357,-5.876440,7.952836,0.082306],[-0.601475,1.359704,-8.267552,4.767196,1.745338,1.181726],[7.073050,7.681720,-8.443934,-4.624813,9.546256,-6.244809],[-3.091774,2.708363,4.266351,4.359450,-9.025151,1.645747],[8.261615,-6.648829,2.461911,-6.536571,7.388309,-5.977543]],[[-9.410448,-7.132135,-3.188888,8.596766,6.505226,-9.285285],[7.594211,-8.074739,-6.867073,-5.300706,-8.181966,-3.830065],[5.646460,-0.207804,1.001923,-4.703537,2.707207,8.799099],[0.582499,-4.555502,7.457846,0.734263,5.735472,-0.112978],[-6.473504,9.267350,8.257845,-3.332882,-4.854455,-2.170007],[-8.901943,-3.095831,9.261820,9.849506,-3.633278,-0.687802],[-8.344530,-4.410502,5.126968,9.377313,5.359802,5.738716]],[[7.752594,8.286052,-3.003512,4.778084,6.562966,9.623341],[5.911296,2.553552,-7.022508,4.573776,-0.204147,-5.240537],[-1.740741,7.879936,3.323668,3.059578,-8.364272,-5.819707],[-1.038805,7.901705,9.733891,-6.965779,1.234807,-4.129114],[4.341027,-6.631157,4.430589,-8.910176,5.236063,-3.851104],[-2.886054,2.452168,-8.649152,3.633868,3.703579,-3.664450],[0.364278,0.747505,3.170362,1.263065,6.347004,-2.356930]],[[-6.836345,-0.535050,-5.236388,-6.302410,-5.483703,2.735015],[-0.932507,2.856211,-6.432565,-8.243697,7.381686,-7.739119],[-2.157751,2.378505,-4.263464,-7.561386,-8.199642,-0.927354],[6.575985,8.557321,-8.976187,0.958536,-1.710630,-0.847137],[-8.667780,-6.238334,-0.399575,-0.610463,-7.915264,-3.208925],[3.174008,-9.872453,8.395973,-7.516481,3.707781,7.792288],[3.034271,-3.721802,9.907634,-9.341104,-9.161789,8.182370]]], dtype = "float64")#candidate|8425|(14, 7, 6)|const|float64
uop_8426 = relay.tan(const_8425.astype('float64')) # shape=(14, 7, 6)
func_3144_call = mod.get_global_var('func_3144')
func_3146_call = mutated_mod.get_global_var('func_3146')
call_8428 = func_3144_call()
call_8429 = func_3144_call()
output = relay.Tuple([uop_8426,call_8428,])
output2 = relay.Tuple([uop_8426,call_8429,])
func_8433 = relay.Function([], output)
mod['func_8433'] = func_8433
mod = relay.transform.InferType()(mod)
output = func_8433()
func_8434 = relay.Function([], output)
mutated_mod['func_8434'] = func_8434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7463_call = mod.get_global_var('func_7463')
func_7464_call = mutated_mod.get_global_var('func_7464')
call_8479 = func_7463_call()
call_8480 = func_7463_call()
output = call_8479
output2 = call_8480
func_8518 = relay.Function([], output)
mod['func_8518'] = func_8518
mod = relay.transform.InferType()(mod)
mutated_mod['func_8518'] = func_8518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8518_call = mutated_mod.get_global_var('func_8518')
call_8519 = func_8518_call()
output = call_8519
func_8520 = relay.Function([], output)
mutated_mod['func_8520'] = func_8520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mod.get_global_var('func_4536')
func_4537_call = mutated_mod.get_global_var('func_4537')
call_8538 = func_4536_call()
call_8539 = func_4536_call()
func_6651_call = mod.get_global_var('func_6651')
func_6654_call = mutated_mod.get_global_var('func_6654')
call_8573 = relay.TupleGetItem(func_6651_call(relay.reshape(call_8538.astype('bool'), [3, 16, 6])), 1)
call_8574 = relay.TupleGetItem(func_6654_call(relay.reshape(call_8538.astype('bool'), [3, 16, 6])), 1)
func_5353_call = mod.get_global_var('func_5353')
func_5354_call = mutated_mod.get_global_var('func_5354')
call_8576 = relay.TupleGetItem(func_5353_call(), 0)
call_8577 = relay.TupleGetItem(func_5354_call(), 0)
func_4405_call = mod.get_global_var('func_4405')
func_4408_call = mutated_mod.get_global_var('func_4408')
var_8583 = relay.var("var_8583", dtype = "float32", shape = (576,))#candidate|8583|(576,)|var|float32
call_8582 = relay.TupleGetItem(func_4405_call(relay.reshape(var_8583.astype('float32'), [2, 288])), 4)
call_8584 = relay.TupleGetItem(func_4408_call(relay.reshape(var_8583.astype('float32'), [2, 288])), 4)
func_4774_call = mod.get_global_var('func_4774')
func_4777_call = mutated_mod.get_global_var('func_4777')
call_8601 = relay.TupleGetItem(func_4774_call(relay.reshape(call_8573.astype('float32'), [64,])), 5)
call_8602 = relay.TupleGetItem(func_4777_call(relay.reshape(call_8573.astype('float32'), [64,])), 5)
output = relay.Tuple([call_8538,call_8573,call_8576,call_8582,var_8583,call_8601,])
output2 = relay.Tuple([call_8539,call_8574,call_8577,call_8584,var_8583,call_8602,])
func_8608 = relay.Function([var_8583,], output)
mod['func_8608'] = func_8608
mod = relay.transform.InferType()(mod)
mutated_mod['func_8608'] = func_8608
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8609 = relay.var("var_8609", dtype = "float32", shape = (576,))#candidate|8609|(576,)|var|float32
func_8608_call = mutated_mod.get_global_var('func_8608')
call_8610 = func_8608_call(var_8609)
output = call_8610
func_8611 = relay.Function([var_8609], output)
mutated_mod['func_8611'] = func_8611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_8613 = relay.TupleGetItem(func_3234_call(), 0)
call_8614 = relay.TupleGetItem(func_3235_call(), 0)
func_2598_call = mod.get_global_var('func_2598')
func_2599_call = mutated_mod.get_global_var('func_2599')
call_8625 = func_2598_call()
call_8626 = func_2598_call()
output = relay.Tuple([call_8613,call_8625,])
output2 = relay.Tuple([call_8614,call_8626,])
func_8633 = relay.Function([], output)
mod['func_8633'] = func_8633
mod = relay.transform.InferType()(mod)
output = func_8633()
func_8634 = relay.Function([], output)
mutated_mod['func_8634'] = func_8634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5353_call = mod.get_global_var('func_5353')
func_5354_call = mutated_mod.get_global_var('func_5354')
call_8647 = relay.TupleGetItem(func_5353_call(), 1)
call_8648 = relay.TupleGetItem(func_5354_call(), 1)
output = call_8647
output2 = call_8648
func_8666 = relay.Function([], output)
mod['func_8666'] = func_8666
mod = relay.transform.InferType()(mod)
output = func_8666()
func_8667 = relay.Function([], output)
mutated_mod['func_8667'] = func_8667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4543_call = mod.get_global_var('func_4543')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_8673 = func_4543_call()
call_8674 = func_4543_call()
output = relay.Tuple([call_8673,])
output2 = relay.Tuple([call_8674,])
func_8712 = relay.Function([], output)
mod['func_8712'] = func_8712
mod = relay.transform.InferType()(mod)
mutated_mod['func_8712'] = func_8712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8712_call = mutated_mod.get_global_var('func_8712')
call_8713 = func_8712_call()
output = call_8713
func_8714 = relay.Function([], output)
mutated_mod['func_8714'] = func_8714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4217_call = mod.get_global_var('func_4217')
func_4219_call = mutated_mod.get_global_var('func_4219')
call_8808 = func_4217_call()
call_8809 = func_4217_call()
func_4536_call = mod.get_global_var('func_4536')
func_4537_call = mutated_mod.get_global_var('func_4537')
call_8814 = func_4536_call()
call_8815 = func_4536_call()
output = relay.Tuple([call_8808,call_8814,])
output2 = relay.Tuple([call_8809,call_8815,])
func_8817 = relay.Function([], output)
mod['func_8817'] = func_8817
mod = relay.transform.InferType()(mod)
output = func_8817()
func_8818 = relay.Function([], output)
mutated_mod['func_8818'] = func_8818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_8863 = func_2428_call()
call_8864 = func_2428_call()
output = relay.Tuple([call_8863,])
output2 = relay.Tuple([call_8864,])
func_8882 = relay.Function([], output)
mod['func_8882'] = func_8882
mod = relay.transform.InferType()(mod)
mutated_mod['func_8882'] = func_8882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8882_call = mutated_mod.get_global_var('func_8882')
call_8883 = func_8882_call()
output = call_8883
func_8884 = relay.Function([], output)
mutated_mod['func_8884'] = func_8884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7720_call = mod.get_global_var('func_7720')
func_7721_call = mutated_mod.get_global_var('func_7721')
call_8914 = relay.TupleGetItem(func_7720_call(), 0)
call_8915 = relay.TupleGetItem(func_7721_call(), 0)
func_6552_call = mod.get_global_var('func_6552')
func_6556_call = mutated_mod.get_global_var('func_6556')
const_8955 = relay.const([-6,6,-8,9,3,5,1,1,-7,-7,-5,-2,3,2,-2,5,8,2,-2,4,-2,-7,10,-7,4,-2,4,4,10,3,4,10,3,8,2,1,4,10,-7,-10,8,-10,6,2,-7,-5,-6,3,-6,5,6,3,3,1,-10,-8,3,-3,-1,4,-1,-1,4,6,-8,10,-8,-1,8,-10,-6,-7,8,9,-4,-1,2,1,7,-7,-10,-8,-10,9,4,-6,-10,9,-2,1,-1,-10,4,10,9,-8,-4,9,-7,4,10,10,-1,-9,-7,-9,-3,-1,2,-2,-1,-2,-9,1,-9,-7,-4,-8,6,-10,-10,-1,-9,1,8,-4,6,-3,7,10,10,-5,-4,9,-2,3,9,-6,8,2,3,-4,10,-3,-3,2,-10,-8,-2,4,-8,-6,1,-7,-1,7,-3,-4,-10,1,-2,9,-10,6,-5,-5,-7,2,-5,9,6,-2,8,-1,3,-6,-4,4,-3,7,-1,3,-5,6,-1,-6,2,3,3,10,7,8,-10,-7,-5,3,7,3,-8,-4,5,-6,-7,9,-7,6,5,-5,-8,-8,-9,8,6,7,-4,4,10,-8,-1,9,-6,-1,-8,-5,-1,9,3,-5,3,-2,-3,-6,-6,-4,-1,-2,9,-5,-10,-5,-3,-10,-6,-5,6,-5,6,4,8,-7,-2,-6,-2,9,-3,-4,1,-3,6,-5,9,-1,-3,-5,6,2,2,-10,10,8,-6,-10,-6,-5,4,5,1,-6,-5,-9,-2,-9,-8,-9,-10,4,9,4,-8,8,-8,5,8,-8,-4,-4,-8,1,3,6,8,9,3,-5,-10,-5,7,-2,3,8,6,4,-6,-2,8,10,10,-5,3,-6,-6,-3,-4,8,4,-5,-9,-4,7,-3,6,2,5,8,9,10,6,-8,8,-8,-1,3,-5,4,5,-8,3,4,9,-5,-6,4,10,-4,8,-3,6,-9,-4,-4,10,-9,-2,-10,-7,-1,-2,6,-9,-10,-2,-3,8,-1,7,-1,-9,-2,5,4,-9,-4,-10,-10,-1,-3,3,1,-10,-4,-8,-5,-5,-10,9,10,-6,8,5,4,-10,6,5,-5,-2,1,3,-8,3,9,-1,1,-5,5,6,-5,6,-10,-1,-5,3,4,4,-4,-10,-8,-4,-10,7,-9,5,-9,-7,10,-5,10,3,-4,8,3,-3,-10,-1,7,6,-10,2,-9,-2,7,-6,-5,-5,-9,9,10,4,-2,-8,4,7,-2,5,9,2,7,7,10,-3,2,10,5,-9,10,5,3,8,-2,9,-2,-9,3,-1,5,-2,7,8,10,8,-7,4,7,-7,6,-10,1,9,3,-6,3,5,4,3,-3,3,-6,-1,-10,-1,8,-7,1,2,-6,-2,10,1,3,7,-5,-5,1,3,6,-10,-5,3,2,10,8,9,1,2,-5,9,3,-2,-10,6,1,2,10,4,3,-2,-7,-8,2,-4,1,7,-7,-8,6,-3,-7,-2,2,-1,-9,-7,5,-9,-5,5,6,10,3,-8,-10,-3,-10,8,-1,9,3,8,-1,-6,-10,2,3,7,10,2,-10,10,9,10,-6,-10,4,8,7,-2,5,10,8,1,-5,-1,-9,5,-9,-10,5,-6,9,4,10,-2,-2,10,-2,-9,7,3,2,-7,-2,-10,8,6,1,-5,6,5,-10,9,7,8,-9,-1,-9,-4,5,10,9,1,5,-3,3,-10,-3,2,6,-4,-3,6,3,-6,3,2,-1,-3,10,9,2,-4,-8,-4,10,-9,-3,6,-4,-6,6,10,2,-6,-9,-4,4,-7,8,-7,9,1,3,-10,2,6,4,7,-1,-8,8,3,-4,4,-2,-10,1,5,-3,-10,2,2,4,-4,10,5,-6,10,1,-1,9,3,5,3,-2,-10,1,-10,1,9,-6,1,-7,3,9,8,-7,7,7,-1,-4,-3,5,9,-7,-9,-7,6,-3,9,-3,9,7,4,-7,3,6,-6,9,-6,6,-1,6,-4,-8,-1,1,1,-8,-2,-9,-6,-2,7,10,2,-1,-8,2,-5,6,-1,6,4,6,8,-2,-2,9,-10,5,6,4,-10,-7,-7,1,-1,-10,8,3,-3,2,-1,-7,1,-2,-7,-2,-3,3,5,7,-10,3,3,6,2,3,1,4,-1,1,-1,4,4,-5,1,7,1,1,-5,-1,-5,10,-4,5,9,5,9,-7,9,3,3,1,-9,7,-9,3,-5,-7,-7,6,10,-7,3,3,-5,-1,-8,4,7,5,2,-8,-3,5,9,8,-5,8,9,9,10,4,-2,-7,-2,3,-10,-10,-7,-3,-10,-6,5,2,-7,-8,1,-7,2,2,-6,-5,-9,9,2,2,2,7,-2,-1,-2,-6,-3,-5,-6,-7,5,9,9,-8,2,2,-8,1,-10,6,3,4,-4,-1,8,-5,1,5,-3,-2,-4,9,5,-9,2,6,9,9,1,-6,-7,-1,4,-8,-2,-2,-7,6,10,-7,-3,6,-5,5,-7,4,-1,-2,-5,-4,3,1,4,3,7,6,5,3,-9,7,-1,-9,7,9,-6,-9,6,10,-9,6,3,7,-6,-9,9,10,-6,-2,4,5,2,-10,3,-2,3,10,2,7,6,-10,9,-2,-10,-9,6,4,-7,-10,-6,-3,-10,6,-8,9,-8,-8,-10,-3,-7,-7,-6,2,-7,4,-5,-2,-9,9,1,3,7,-8,2,-9,4,3,-7,3,-9,7,3,-1,8,-10,-7,10,-4,5,2,6,-10,-7,-6,-2,9,-1,9,-5,-3,7,7,8,-10,7,6,7,4,6,-6,7,8,-8,-1,5,7,5,-3,-3,-7,2,-4,1,7,-8,-6,10,4,-2,-10,-10,-2,9,10,-8,-2,10,1,4,9,-3,-8,8,1,-6,10,6,-10,7,8,-7,-6,-8,6,-7,5,-9,-2,-4,8,2,7,10,-4,7,10,2,-1,-3,2,4,-9,-2,-10,2,8,8,3,-3,4,-10,-4,-10,-3,-1,-4,-4,-8,2,5,-7,-9,6,-4,-10,9,-5,-2,-7,10,4,3,-7,-6,-8,-6,-2,4,8,9,6,-7,10,-8,6,4,-3,10,7,-10,5,-2,10,6,-3,5,-2,2,4,8,-9,-2,1,-2,-5,1,-10,-8,-8,10,7,3,-10,3,7,3,-6,-8,-6,5,-5,-3,1,9,6,-3,7,-4,2,-8,-1,-3,-8,5,-1,9,-9,5,6,9,5,4,-1,8,8,-2,-1,-7,6,-4,4,-7,8,1,9,-5,-6,-8,-9,-10,-4,-7,7,-5,8,2,-5,-5,4,-8,-9,-9,3,-2,4,1,-2,3,4,2,9,6,-4,6,6,-3,8,10,9,-6,-1,1,7,3,-3,-5,-1,-6,-1,-5,8,-4,9,-10,5,1,4,1,9,-5,1,7,-3,8,-7,1,-2,2,8,-10,-7,-8,7,4,-5,10,-9,7,10,-5,10,-4,2,4,7,2,-8,-7,-4,-1,-10,-5,8,2,-9,6,-5,-10,6,7,-9,-9,1,-10,-9,-4,-1,-9,-2,8,-9,9,-3,-9,2,-4,6,9,-3,4,1,-2,-6,-1,3,-10,-4,-6,-7,-7,2,-1,7,8,9,4,10,2,9,6,5,-6,-4,-7,7,9,7,10,2,-6,9,-10,-5,5,-8,-6,9,-3,2,2,-5], dtype = "int32")#candidate|8955|(1386,)|const|int32
call_8954 = relay.TupleGetItem(func_6552_call(relay.reshape(const_8955.astype('int32'), [11, 9, 14]), relay.reshape(const_8955.astype('int32'), [11, 9, 14]), ), 0)
call_8956 = relay.TupleGetItem(func_6556_call(relay.reshape(const_8955.astype('int32'), [11, 9, 14]), relay.reshape(const_8955.astype('int32'), [11, 9, 14]), ), 0)
func_4479_call = mod.get_global_var('func_4479')
func_4480_call = mutated_mod.get_global_var('func_4480')
call_8957 = relay.TupleGetItem(func_4479_call(), 0)
call_8958 = relay.TupleGetItem(func_4480_call(), 0)
output = relay.Tuple([call_8914,call_8954,const_8955,call_8957,])
output2 = relay.Tuple([call_8915,call_8956,const_8955,call_8958,])
func_8964 = relay.Function([], output)
mod['func_8964'] = func_8964
mod = relay.transform.InferType()(mod)
mutated_mod['func_8964'] = func_8964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8964_call = mutated_mod.get_global_var('func_8964')
call_8965 = func_8964_call()
output = call_8965
func_8966 = relay.Function([], output)
mutated_mod['func_8966'] = func_8966
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8979 = relay.var("var_8979", dtype = "float32", shape = (5, 11, 10))#candidate|8979|(5, 11, 10)|var|float32
uop_8980 = relay.asinh(var_8979.astype('float32')) # shape=(5, 11, 10)
func_4800_call = mod.get_global_var('func_4800')
func_4801_call = mutated_mod.get_global_var('func_4801')
call_8982 = relay.TupleGetItem(func_4800_call(), 1)
call_8983 = relay.TupleGetItem(func_4801_call(), 1)
func_5544_call = mod.get_global_var('func_5544')
func_5545_call = mutated_mod.get_global_var('func_5545')
call_8986 = relay.TupleGetItem(func_5544_call(), 0)
call_8987 = relay.TupleGetItem(func_5545_call(), 0)
output = relay.Tuple([uop_8980,call_8982,call_8986,])
output2 = relay.Tuple([uop_8980,call_8983,call_8987,])
func_9008 = relay.Function([var_8979,], output)
mod['func_9008'] = func_9008
mod = relay.transform.InferType()(mod)
var_9009 = relay.var("var_9009", dtype = "float32", shape = (5, 11, 10))#candidate|9009|(5, 11, 10)|var|float32
output = func_9008(var_9009)
func_9010 = relay.Function([var_9009], output)
mutated_mod['func_9010'] = func_9010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4490_call = mod.get_global_var('func_4490')
func_4492_call = mutated_mod.get_global_var('func_4492')
call_9025 = relay.TupleGetItem(func_4490_call(), 0)
call_9026 = relay.TupleGetItem(func_4492_call(), 0)
output = call_9025
output2 = call_9026
func_9035 = relay.Function([], output)
mod['func_9035'] = func_9035
mod = relay.transform.InferType()(mod)
output = func_9035()
func_9036 = relay.Function([], output)
mutated_mod['func_9036'] = func_9036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2524_call = mod.get_global_var('func_2524')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_9057 = func_2524_call()
call_9058 = func_2524_call()
func_2822_call = mod.get_global_var('func_2822')
func_2824_call = mutated_mod.get_global_var('func_2824')
call_9077 = relay.TupleGetItem(func_2822_call(), 0)
call_9078 = relay.TupleGetItem(func_2824_call(), 0)
output = relay.Tuple([call_9057,call_9077,])
output2 = relay.Tuple([call_9058,call_9078,])
func_9082 = relay.Function([], output)
mod['func_9082'] = func_9082
mod = relay.transform.InferType()(mod)
output = func_9082()
func_9083 = relay.Function([], output)
mutated_mod['func_9083'] = func_9083
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9133 = relay.const([[[-1.885524],[-5.565142],[-5.224076],[5.812921],[-1.686241],[3.951664],[-6.348012],[5.020367],[-4.902244],[-2.468041],[3.142290],[-4.917489],[8.758575],[-4.202892],[-6.947943],[-4.354827]],[[-3.781495],[5.337179],[1.316813],[-6.258018],[-5.599734],[-0.276128],[0.249186],[-7.659445],[-6.578755],[-7.053179],[1.527051],[0.462175],[1.832339],[8.951927],[-4.493978],[9.370095]],[[-1.088804],[3.361438],[9.992426],[1.402340],[6.054140],[9.622923],[-7.034278],[1.468151],[-4.261544],[-2.533991],[-9.574203],[-9.587614],[7.642222],[-0.208017],[3.010842],[2.977113]],[[-9.519902],[6.052550],[-3.339649],[7.869480],[-9.580371],[-6.916152],[-0.854842],[-6.849780],[-2.617710],[1.287083],[-8.244112],[-2.872667],[4.807777],[8.939620],[-4.015364],[4.386644]]], dtype = "float32")#candidate|9133|(4, 16, 1)|const|float32
uop_9134 = relay.sin(const_9133.astype('float32')) # shape=(4, 16, 1)
bop_9136 = relay.not_equal(uop_9134.astype('bool'), relay.reshape(const_9133.astype('bool'), relay.shape_of(uop_9134))) # shape=(4, 16, 1)
uop_9139 = relay.erf(bop_9136.astype('float64')) # shape=(4, 16, 1)
bop_9148 = relay.minimum(uop_9134.astype('int8'), relay.reshape(const_9133.astype('int8'), relay.shape_of(uop_9134))) # shape=(4, 16, 1)
func_4421_call = mod.get_global_var('func_4421')
func_4423_call = mutated_mod.get_global_var('func_4423')
call_9151 = relay.TupleGetItem(func_4421_call(), 0)
call_9152 = relay.TupleGetItem(func_4423_call(), 0)
uop_9153 = relay.log10(uop_9139.astype('float32')) # shape=(4, 16, 1)
func_7983_call = mod.get_global_var('func_7983')
func_7986_call = mutated_mod.get_global_var('func_7986')
const_9156 = relay.const([[-1.859212,-5.715445,-9.279504,-2.158328,2.398262,6.075524,8.170244,-1.800621,-2.550467,8.621208,-5.463980,-7.617273,-9.083834,-0.251301,1.538510,0.368485,-3.237211,-4.442999,-0.851785,1.847582,-3.308207,2.646654,-6.390093,-1.170463,-7.448760,-8.414873,0.957402,5.934235,-9.562231,-2.781807,2.315379,-4.721554,7.984010,-2.193367,5.380619,6.502717,-9.541913,-9.228026,3.224322,3.172597,-1.072238,-0.683817,-7.058541,4.970356,-6.797241,7.102206,0.237942,0.275923,-1.352202,-4.902367,1.992475,1.184336,-6.002337,-7.409349,4.713297,5.646767,5.761610,5.543542,9.859953,0.986937,-7.051066,6.557019,-3.762651,4.882964,-3.402888,-8.055477,1.358243,0.123368,3.175021,8.857309,4.316058,-3.392630,1.982272,4.710080,2.343794,-6.196948,1.330307,7.171496,-7.144448,-1.611414,8.948510,4.798816,2.768349,-0.756036,-2.415718,9.984997,2.945415,9.388234,6.841343,4.882007,6.857669,-3.129423,-3.682135,-6.344033,-3.712620,2.578013,8.649314,0.704370,-1.909117,-0.309579,8.697890,-4.436735,4.870340,1.519407,-9.025137,9.854240,-1.388752,-5.529552,-4.610990,-5.733220,-0.518501,-3.709830,-9.815226,-9.249850,1.126418,7.998838,-7.465796,2.720216,1.492782,-2.616198,-2.579574,0.139539,0.291526,1.825471,-3.363963,1.109922,3.202263,8.071665,6.059957,-6.238829,-0.690217,4.841116,-9.137381,-2.171808,-9.298398,0.035120,8.675622,8.947180,1.681620,-7.933633,-5.005296,-5.164465,1.728643,7.002888,6.093120,9.278827,-4.265716,-9.177466,-0.723655,-0.591414,0.576879,8.445835,8.199456,5.339314,3.474806,-5.280013,9.565642,3.054525,-8.011838,8.291645,5.459310,5.589940,-6.505416,-1.251767,8.943099,6.893439,-4.991470,2.579112,3.271986,-2.760951,-0.566366,5.425640,3.666026,-3.561857,1.970530,4.495545,-6.622872,-3.853573,-3.198509,8.134606,-2.519583,-8.935213,6.332868,-5.196913,1.582850,6.783879,8.362236,8.101881,-2.897318,6.481272,-4.812082,-0.941967,1.073371,5.249305,7.499200,3.518030,2.531446,-3.361756,6.322729,3.090467,-1.692107,-9.803897,9.652824,-1.024742,0.583438,-0.095494,5.015303,6.381501,7.521798,-4.010759,3.239511,-5.997629,-3.769981,-8.070688,7.339560,-5.266043,-4.907377,-8.301266,-9.729842,9.368029,-0.465479,4.888365,-1.487435,-6.116655,2.650673,-8.447991,1.105011,9.665407,-8.012987,7.479034,-6.305238,9.378704,1.053954,-6.990059,-5.208572,2.995495,1.652478,-7.690996,5.302962,-2.138179,-1.111882,-9.337556,0.324299,5.391398,4.005529,-6.770802,-8.903736,-5.078002,6.539937,4.249243,3.060659,-0.598174,-4.715393,-9.423690,0.559421,-8.978074,-5.091272,8.141117,3.239418,1.731937,-9.411868,-4.898296,8.105541,-4.380173,7.049605,-2.843889,-6.260909,-8.503574,-7.215364,4.015491,4.823174,7.639743,-9.849930,0.638909,7.453499,-6.514007,-9.455670,-8.982050,0.924124,-6.124298,-2.277893,9.403565,5.268714,9.726583,6.502830,-4.025982,8.853524,-0.923571,-5.720893,3.487943,-1.403253,5.938809,-7.660716,-7.306525,-1.502691,-9.010362,5.713148,-5.963695,2.744610,-7.092327,-3.785089,7.179810,-6.734965,5.021436,-0.093959,-4.567142,-3.829057,8.304192,3.092091,-1.935598,2.814128,8.280327,7.470011,3.260834,9.759629]], dtype = "float64")#candidate|9156|(1, 315)|const|float64
call_9155 = relay.TupleGetItem(func_7983_call(relay.reshape(const_9156.astype('float64'), [5, 7, 9])), 2)
call_9157 = relay.TupleGetItem(func_7986_call(relay.reshape(const_9156.astype('float64'), [5, 7, 9])), 2)
func_5353_call = mod.get_global_var('func_5353')
func_5354_call = mutated_mod.get_global_var('func_5354')
call_9161 = relay.TupleGetItem(func_5353_call(), 1)
call_9162 = relay.TupleGetItem(func_5354_call(), 1)
func_2598_call = mod.get_global_var('func_2598')
func_2599_call = mutated_mod.get_global_var('func_2599')
call_9169 = func_2598_call()
call_9170 = func_2598_call()
bop_9171 = relay.subtract(uop_9153.astype('int8'), const_9156.astype('int8')) # shape=(4, 16, 315)
bop_9179 = relay.less_equal(bop_9136.astype('bool'), relay.reshape(uop_9153.astype('bool'), relay.shape_of(bop_9136))) # shape=(4, 16, 1)
func_4405_call = mod.get_global_var('func_4405')
func_4408_call = mutated_mod.get_global_var('func_4408')
var_9185 = relay.var("var_9185", dtype = "float32", shape = (36, 16))#candidate|9185|(36, 16)|var|float32
call_9184 = relay.TupleGetItem(func_4405_call(relay.reshape(var_9185.astype('float32'), [2, 288])), 0)
call_9186 = relay.TupleGetItem(func_4408_call(relay.reshape(var_9185.astype('float32'), [2, 288])), 0)
output = relay.Tuple([bop_9148,call_9151,call_9155,call_9161,call_9169,bop_9171,bop_9179,call_9184,var_9185,])
output2 = relay.Tuple([bop_9148,call_9152,call_9157,call_9162,call_9170,bop_9171,bop_9179,call_9186,var_9185,])
func_9190 = relay.Function([var_9185,], output)
mod['func_9190'] = func_9190
mod = relay.transform.InferType()(mod)
var_9191 = relay.var("var_9191", dtype = "float32", shape = (36, 16))#candidate|9191|(36, 16)|var|float32
output = func_9190(var_9191)
func_9192 = relay.Function([var_9191], output)
mutated_mod['func_9192'] = func_9192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8712_call = mod.get_global_var('func_8712')
func_8714_call = mutated_mod.get_global_var('func_8714')
call_9291 = relay.TupleGetItem(func_8712_call(), 0)
call_9292 = relay.TupleGetItem(func_8714_call(), 0)
output = call_9291
output2 = call_9292
func_9306 = relay.Function([], output)
mod['func_9306'] = func_9306
mod = relay.transform.InferType()(mod)
output = func_9306()
func_9307 = relay.Function([], output)
mutated_mod['func_9307'] = func_9307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9306_call = mod.get_global_var('func_9306')
func_9307_call = mutated_mod.get_global_var('func_9307')
call_9313 = func_9306_call()
call_9314 = func_9306_call()
output = relay.Tuple([call_9313,])
output2 = relay.Tuple([call_9314,])
func_9315 = relay.Function([], output)
mod['func_9315'] = func_9315
mod = relay.transform.InferType()(mod)
mutated_mod['func_9315'] = func_9315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9315_call = mutated_mod.get_global_var('func_9315')
call_9316 = func_9315_call()
output = call_9316
func_9317 = relay.Function([], output)
mutated_mod['func_9317'] = func_9317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3725_call = mod.get_global_var('func_3725')
func_3726_call = mutated_mod.get_global_var('func_3726')
call_9379 = relay.TupleGetItem(func_3725_call(), 0)
call_9380 = relay.TupleGetItem(func_3726_call(), 0)
output = call_9379
output2 = call_9380
func_9382 = relay.Function([], output)
mod['func_9382'] = func_9382
mod = relay.transform.InferType()(mod)
output = func_9382()
func_9383 = relay.Function([], output)
mutated_mod['func_9383'] = func_9383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9082_call = mod.get_global_var('func_9082')
func_9083_call = mutated_mod.get_global_var('func_9083')
call_9453 = relay.TupleGetItem(func_9082_call(), 0)
call_9454 = relay.TupleGetItem(func_9083_call(), 0)
func_8053_call = mod.get_global_var('func_8053')
func_8055_call = mutated_mod.get_global_var('func_8055')
call_9470 = relay.TupleGetItem(func_8053_call(), 0)
call_9471 = relay.TupleGetItem(func_8055_call(), 0)
func_6381_call = mod.get_global_var('func_6381')
func_6383_call = mutated_mod.get_global_var('func_6383')
var_9474 = relay.var("var_9474", dtype = "float64", shape = (156,))#candidate|9474|(156,)|var|float64
call_9473 = relay.TupleGetItem(func_6381_call(relay.reshape(var_9474.astype('float64'), [13, 4, 3])), 0)
call_9475 = relay.TupleGetItem(func_6383_call(relay.reshape(var_9474.astype('float64'), [13, 4, 3])), 0)
func_4479_call = mod.get_global_var('func_4479')
func_4480_call = mutated_mod.get_global_var('func_4480')
call_9485 = relay.TupleGetItem(func_4479_call(), 0)
call_9486 = relay.TupleGetItem(func_4480_call(), 0)
output = relay.Tuple([call_9453,call_9470,call_9473,var_9474,call_9485,])
output2 = relay.Tuple([call_9454,call_9471,call_9475,var_9474,call_9486,])
func_9487 = relay.Function([var_9474,], output)
mod['func_9487'] = func_9487
mod = relay.transform.InferType()(mod)
var_9488 = relay.var("var_9488", dtype = "float64", shape = (156,))#candidate|9488|(156,)|var|float64
output = func_9487(var_9488)
func_9489 = relay.Function([var_9488], output)
mutated_mod['func_9489'] = func_9489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mod.get_global_var('func_3542')
func_3543_call = mutated_mod.get_global_var('func_3543')
call_9499 = relay.TupleGetItem(func_3542_call(), 0)
call_9500 = relay.TupleGetItem(func_3543_call(), 0)
func_7279_call = mod.get_global_var('func_7279')
func_7281_call = mutated_mod.get_global_var('func_7281')
call_9509 = relay.TupleGetItem(func_7279_call(), 2)
call_9510 = relay.TupleGetItem(func_7281_call(), 2)
output = relay.Tuple([call_9499,call_9509,])
output2 = relay.Tuple([call_9500,call_9510,])
func_9517 = relay.Function([], output)
mod['func_9517'] = func_9517
mod = relay.transform.InferType()(mod)
mutated_mod['func_9517'] = func_9517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9517_call = mutated_mod.get_global_var('func_9517')
call_9518 = func_9517_call()
output = call_9518
func_9519 = relay.Function([], output)
mutated_mod['func_9519'] = func_9519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4122_call = mod.get_global_var('func_4122')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_9584 = relay.TupleGetItem(func_4122_call(), 0)
call_9585 = relay.TupleGetItem(func_4124_call(), 0)
func_7610_call = mod.get_global_var('func_7610')
func_7612_call = mutated_mod.get_global_var('func_7612')
call_9591 = func_7610_call()
call_9592 = func_7610_call()
func_2377_call = mod.get_global_var('func_2377')
func_2383_call = mutated_mod.get_global_var('func_2383')
const_9617 = relay.const([-7,-8,10,8,-4,6,10,9,8,5,10,7,-8,3,4,-6,1,-1,-6,2,1,-8,-1,-5,10,8,7,-4,-4,8,-9,8,-8,2,9,6,3,9,10,1,-5,2,2,-9,-10,-4,-1,10,1,-5,-5,8,-6,10,-2,-8,1,1,5,-2,6,8,8,9,8,-10,7,-1,-7,-9,-3,8,-6,-9,-8,9,-5,-1,3,-2,4,-5,10,-1,6,-7,-4,5,5,-4,3,9,8,-2,-8,3,-8,2,-2,-6,1,-9,2,9,-6,-2,-4,-8,9,-3,-6,-10,5,-4,-2,-7,-6,2,-10,7,1,6,8,-10,-6,7,-1,8,-8,-3,5,-7,-8,-8,7,-8,-5,-6,10,4,-10,10,8,5,2,-8,2,7,2,10,-1,2,3,-8,5,-1,-3,-4,8,-6,-1,-7,-10,5,-8,-5,-5,4,4,-3,6,-4,4,9,-1,-2,1,-7,4,5,9,2,7,-4,-1,-2,10,5,3,-5,1,7,1,-3,6,-8,9,8,7,9,-8,7,6,-3,-8,-5,8,-10,-8,3,-2,6,2,-9,6,8,-10,2,-7,-7,5,-3,-6,3,6,5,-6,1,-6,6,-10,-8,9,6,-6,10,-7,-4,6,4,-3,9,-1,-9,3,-1,-2,-3,10,9,-4,-5,2,1,-7,9,5,3,-2,-5,10,10,-6,4,-4,-1,-4,1,-6,-5,9,-4,5,2,-10,2,6,3,-5,-7,-10,9,-5,-1,3,5,-1,6,-6,3,7,5,7,5,-5,-1,1,10,-10,-6,-8,-5,-9,2,9,-3,-1,10,-8,-10,-9,9,-2,-5,-1,-5,3,-7,9,10,-7,6,3,5,-3,6,7,2,-6,2,-10,-6,5,5,-5,5,10,-7,9,6,-9,4,8,7,-2,1,6,-3,3,6,-5,-9,4,9,1,5,-6,6,-2,-7,-2,6,-10,-10,9,2,-8,-8,-8,-6,-10,9,-10,1,-7,-8,-9,-8,3,3,-3,5,-5,-4], dtype = "uint32")#candidate|9617|(384,)|const|uint32
var_9618 = relay.var("var_9618", dtype = "float32", shape = (64,))#candidate|9618|(64,)|var|float32
const_9619 = relay.const([-2.982777,0.466509,-6.714289,0.825617,-7.861751,-6.083227,-1.229567,7.655934,6.605883,2.474276,-6.689620,8.924205,-7.391854,-7.383990,-5.032341,3.529512,-9.290294,-6.804005,2.209052,7.705872,1.373267,-8.319815,7.154152,4.398262,1.795594,-9.686262,-6.754879,-4.807745,-4.393583,3.562113,5.431575,1.377783,6.719351,-9.363622,-4.394825,0.325549,6.772701,7.065810,0.401657,-3.012514,5.385059,-6.205470,-0.057475,2.356513,5.571942,-8.601724,5.947465,8.579628,3.037713,6.200645,8.398215,-3.522965,-9.148121,4.149194,-5.287457,0.217299,-4.638180,-3.254024,-6.021734,9.381451,-9.421500,-3.891230,7.871317,-0.404173,8.821485,-6.750823,-5.744910,-4.236843,-4.527096,-4.176972,0.683185,1.428780,-5.139188,-9.934414,4.402252,-3.292445,1.610030,2.706923,-2.385839,-0.873857,8.153356,-5.917111,9.826434,2.544251,-7.158949,-0.483209,2.952124,5.248843,9.316732,-3.719682,5.134683,-4.713812,-3.798291,-6.450759,-6.215958,-7.290688,1.501494,2.278280,5.686649,7.181128,8.537389,7.174024,2.041249,-1.420795,3.711882,3.990760,3.067602,7.574757,9.214972,9.426251,-4.893083,4.836416,-2.872995,-8.657613,2.076153,-9.894759,-2.003114,9.463527,-5.715389,-5.870730,9.299805,8.911673,-1.883860,-0.461752,-7.073451,0.824359,3.065753,-5.590237,9.664536,-4.642388,-8.677600,5.970666,-0.969325,-6.011708,-3.747000,-5.820734,-2.216248,5.803741,2.436882,-8.384362,8.265384,-9.058471,2.459064,-2.907800,-6.818487,3.470492,3.509979,4.700176,-7.073299,6.434445,-2.065823,-3.919891,0.600033,2.547186,6.784034,-8.721543,5.651751,9.673781,3.627498,-3.982426,-5.865074,2.145319,-7.056431,-2.936338,-0.656140,-0.289295,2.598532,-5.280801,-6.051096,6.260224,4.362746,-3.500207,7.220183,3.221089,8.010923,-2.754939,-8.631826,-6.325049,-6.164545,4.099774,-1.388061,2.513728,-9.007748,-4.321386,-6.120467,-2.821908,8.339500,-4.858900,-7.460635,1.832954,0.429987,-0.083098,9.969297,0.986215,6.090807,1.024507,-7.840878,0.964386,-3.023972,9.905760,-6.967559,-7.516537,-6.501757,-7.306628,7.705340,-6.728575,4.225187,-5.899024,1.399568,-4.621083,-2.015282,-8.822553,-0.414287,1.952768,2.800169,9.676932,-6.158342,3.432757,3.013519,5.306031,-7.329014,6.178847,-5.727243,-4.452708,0.316724,-4.033979,-8.833316,-6.360261,2.017853,4.333179,-9.892852,-8.250585,9.512800,3.058546,9.792750,9.688729,9.339490,4.981763,-4.503657,9.103931,-8.278724,4.545272,9.041514,4.232893,3.344919,6.722946,-8.071405,-9.996915,-0.457892,-8.731519,-9.570396,4.509624,-2.426189,-8.189978,-3.561809,7.537239,9.549470,-9.400671,-6.832377,0.888794,-5.013541,-6.234239,-0.102707,-4.652135,-8.366449,-9.807290,-9.879824,-4.841223,-8.013179,4.375247,9.350936,2.749126,0.686554,5.564741,-1.688445,4.272891,2.339410,6.799901,-6.449540,-8.892122,-3.370922,-5.397944,-2.510427,8.288289,6.776938,-7.923744,8.933419,5.557320,4.444718,9.515042,-3.214555,-9.864657,-7.367592,3.026143,-3.229251,0.471032,1.403791,6.083151,7.163855,-8.733790,-3.364597,7.422954,5.526403,-5.180425,9.548931,-8.088673,3.766751,0.457860,-2.810300,-1.146232,6.335010,8.621273,1.718298,-4.652044,1.699600,2.988812,3.642942,-5.028042,-6.555715,3.091981], dtype = "float32")#candidate|9619|(320,)|const|float32
var_9620 = relay.var("var_9620", dtype = "float64", shape = (160,))#candidate|9620|(160,)|var|float64
call_9616 = relay.TupleGetItem(func_2377_call(relay.reshape(const_9617.astype('uint32'), [24, 16]), relay.reshape(var_9618.astype('float32'), [64,]), relay.reshape(const_9619.astype('float32'), [4, 80]), relay.reshape(var_9620.astype('float64'), [160,]), ), 3)
call_9621 = relay.TupleGetItem(func_2383_call(relay.reshape(const_9617.astype('uint32'), [24, 16]), relay.reshape(var_9618.astype('float32'), [64,]), relay.reshape(const_9619.astype('float32'), [4, 80]), relay.reshape(var_9620.astype('float64'), [160,]), ), 3)
func_5967_call = mod.get_global_var('func_5967')
func_5969_call = mutated_mod.get_global_var('func_5969')
call_9644 = relay.TupleGetItem(func_5967_call(), 0)
call_9645 = relay.TupleGetItem(func_5969_call(), 0)
bop_9649 = relay.left_shift(call_9616.astype('uint8'), relay.reshape(const_9617.astype('uint8'), relay.shape_of(call_9616))) # shape=(24, 16)
bop_9652 = relay.left_shift(call_9621.astype('uint8'), relay.reshape(const_9617.astype('uint8'), relay.shape_of(call_9621))) # shape=(24, 16)
output = relay.Tuple([call_9584,call_9591,var_9618,const_9619,var_9620,call_9644,bop_9649,])
output2 = relay.Tuple([call_9585,call_9592,var_9618,const_9619,var_9620,call_9645,bop_9652,])
func_9665 = relay.Function([var_9618,var_9620,], output)
mod['func_9665'] = func_9665
mod = relay.transform.InferType()(mod)
var_9666 = relay.var("var_9666", dtype = "float32", shape = (64,))#candidate|9666|(64,)|var|float32
var_9667 = relay.var("var_9667", dtype = "float64", shape = (160,))#candidate|9667|(160,)|var|float64
output = func_9665(var_9666,var_9667,)
func_9668 = relay.Function([var_9666,var_9667,], output)
mutated_mod['func_9668'] = func_9668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5920_call = mod.get_global_var('func_5920')
func_5922_call = mutated_mod.get_global_var('func_5922')
call_9673 = relay.TupleGetItem(func_5920_call(), 0)
call_9674 = relay.TupleGetItem(func_5922_call(), 0)
output = call_9673
output2 = call_9674
func_9684 = relay.Function([], output)
mod['func_9684'] = func_9684
mod = relay.transform.InferType()(mod)
mutated_mod['func_9684'] = func_9684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9684_call = mutated_mod.get_global_var('func_9684')
call_9685 = func_9684_call()
output = call_9685
func_9686 = relay.Function([], output)
mutated_mod['func_9686'] = func_9686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6474_call = mod.get_global_var('func_6474')
func_6475_call = mutated_mod.get_global_var('func_6475')
call_9754 = relay.TupleGetItem(func_6474_call(), 0)
call_9755 = relay.TupleGetItem(func_6475_call(), 0)
func_8666_call = mod.get_global_var('func_8666')
func_8667_call = mutated_mod.get_global_var('func_8667')
call_9758 = func_8666_call()
call_9759 = func_8666_call()
output = relay.Tuple([call_9754,call_9758,])
output2 = relay.Tuple([call_9755,call_9759,])
func_9760 = relay.Function([], output)
mod['func_9760'] = func_9760
mod = relay.transform.InferType()(mod)
mutated_mod['func_9760'] = func_9760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9760_call = mutated_mod.get_global_var('func_9760')
call_9761 = func_9760_call()
output = call_9761
func_9762 = relay.Function([], output)
mutated_mod['func_9762'] = func_9762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8053_call = mod.get_global_var('func_8053')
func_8055_call = mutated_mod.get_global_var('func_8055')
call_9782 = relay.TupleGetItem(func_8053_call(), 0)
call_9783 = relay.TupleGetItem(func_8055_call(), 0)
output = relay.Tuple([call_9782,])
output2 = relay.Tuple([call_9783,])
func_9788 = relay.Function([], output)
mod['func_9788'] = func_9788
mod = relay.transform.InferType()(mod)
output = func_9788()
func_9789 = relay.Function([], output)
mutated_mod['func_9789'] = func_9789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6329_call = mod.get_global_var('func_6329')
func_6330_call = mutated_mod.get_global_var('func_6330')
call_9813 = relay.TupleGetItem(func_6329_call(), 0)
call_9814 = relay.TupleGetItem(func_6330_call(), 0)
func_8053_call = mod.get_global_var('func_8053')
func_8055_call = mutated_mod.get_global_var('func_8055')
call_9816 = relay.TupleGetItem(func_8053_call(), 0)
call_9817 = relay.TupleGetItem(func_8055_call(), 0)
func_7961_call = mod.get_global_var('func_7961')
func_7962_call = mutated_mod.get_global_var('func_7962')
call_9818 = func_7961_call()
call_9819 = func_7961_call()
func_6688_call = mod.get_global_var('func_6688')
func_6690_call = mutated_mod.get_global_var('func_6690')
const_9840 = relay.const([[-10,1,5,1,5,-9,-8,5,6,2,5,2,-6,2,6,4,-2,9,-3,9,8,2,-10,-9,-3,4,10,-6,4,-10,5,-8,9,8,2,3,-7,7,-2,-4,9,4,6,6,7,10,-1,1,-8,3,6,9,1,-1,-4,9,-2,3,-1,8,6,-10,-6,5],[9,3,4,-7,8,7,4,7,6,-6,10,7,-9,1,7,9,-5,-9,2,3,7,-6,-5,7,-3,-10,-4,-9,1,8,9,6,-10,5,3,6,8,-1,2,-4,-10,8,-1,-6,-8,-2,4,10,-3,5,-1,-7,2,-3,5,-9,-4,-6,-5,-7,1,-7,9,8],[-2,-9,-6,3,-4,2,6,2,-10,2,5,10,1,2,7,-2,-4,2,-9,8,3,-3,-3,8,-7,1,-2,-7,-10,-2,8,-4,9,4,2,1,4,-6,-9,2,-5,-8,-6,9,-4,1,-9,8,-2,5,-6,3,10,-9,-4,-5,-4,5,7,-3,8,-5,-10,6],[5,8,-8,3,10,7,1,-4,-4,-4,-4,-4,-5,-1,1,-9,-9,-10,-9,4,-5,5,2,10,8,-7,-4,-7,9,4,-5,10,9,10,-3,9,-5,3,-2,5,8,4,-2,-1,-7,3,-7,6,3,5,-10,5,7,-5,2,10,-4,3,5,9,8,-4,4,-10],[5,4,-8,-3,8,5,-9,-9,-1,-9,6,-8,9,-9,3,-2,5,-4,-7,-9,6,-3,10,6,-6,-8,2,-5,10,-5,-3,3,-3,2,-5,-4,-6,-4,1,-10,6,9,7,-10,-10,-2,-2,-3,-2,-6,8,6,9,2,1,-6,1,-4,9,-7,-8,4,-2,4],[1,-8,10,-3,-3,8,9,2,9,-10,9,9,-4,7,9,-9,3,-1,3,-1,-1,2,-5,9,10,6,5,-9,8,7,9,-10,-3,-7,-7,3,-9,5,9,10,3,1,9,9,7,-9,-1,-1,9,1,6,1,10,9,-2,-9,3,5,9,3,1,2,-10,8]], dtype = "uint32")#candidate|9840|(6, 64)|const|uint32
call_9839 = relay.TupleGetItem(func_6688_call(relay.reshape(const_9840.astype('uint32'), [384,])), 1)
call_9841 = relay.TupleGetItem(func_6690_call(relay.reshape(const_9840.astype('uint32'), [384,])), 1)
func_5884_call = mod.get_global_var('func_5884')
func_5887_call = mutated_mod.get_global_var('func_5887')
var_9855 = relay.var("var_9855", dtype = "float32", shape = (576,))#candidate|9855|(576,)|var|float32
call_9854 = relay.TupleGetItem(func_5884_call(relay.reshape(var_9855.astype('float32'), [576,])), 1)
call_9856 = relay.TupleGetItem(func_5887_call(relay.reshape(var_9855.astype('float32'), [576,])), 1)
output = relay.Tuple([call_9813,call_9816,call_9818,call_9839,const_9840,call_9854,var_9855,])
output2 = relay.Tuple([call_9814,call_9817,call_9819,call_9841,const_9840,call_9856,var_9855,])
func_9869 = relay.Function([var_9855,], output)
mod['func_9869'] = func_9869
mod = relay.transform.InferType()(mod)
mutated_mod['func_9869'] = func_9869
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9870 = relay.var("var_9870", dtype = "float32", shape = (576,))#candidate|9870|(576,)|var|float32
func_9869_call = mutated_mod.get_global_var('func_9869')
call_9871 = func_9869_call(var_9870)
output = call_9871
func_9872 = relay.Function([var_9870], output)
mutated_mod['func_9872'] = func_9872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6774_call = mod.get_global_var('func_6774')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_9893 = relay.TupleGetItem(func_6774_call(), 0)
call_9894 = relay.TupleGetItem(func_6775_call(), 0)
output = relay.Tuple([call_9893,])
output2 = relay.Tuple([call_9894,])
func_9918 = relay.Function([], output)
mod['func_9918'] = func_9918
mod = relay.transform.InferType()(mod)
mutated_mod['func_9918'] = func_9918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9918_call = mutated_mod.get_global_var('func_9918')
call_9919 = func_9918_call()
output = call_9919
func_9920 = relay.Function([], output)
mutated_mod['func_9920'] = func_9920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9306_call = mod.get_global_var('func_9306')
func_9307_call = mutated_mod.get_global_var('func_9307')
call_9937 = func_9306_call()
call_9938 = func_9306_call()
func_4076_call = mod.get_global_var('func_4076')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_9948 = func_4076_call()
call_9949 = func_4076_call()
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_9962 = func_1537_call()
call_9963 = func_1537_call()
func_2536_call = mod.get_global_var('func_2536')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_9971 = relay.TupleGetItem(func_2536_call(), 0)
call_9972 = relay.TupleGetItem(func_2538_call(), 0)
output = relay.Tuple([call_9937,call_9948,call_9962,call_9971,])
output2 = relay.Tuple([call_9938,call_9949,call_9963,call_9972,])
func_9974 = relay.Function([], output)
mod['func_9974'] = func_9974
mod = relay.transform.InferType()(mod)
mutated_mod['func_9974'] = func_9974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9974_call = mutated_mod.get_global_var('func_9974')
call_9975 = func_9974_call()
output = call_9975
func_9976 = relay.Function([], output)
mutated_mod['func_9976'] = func_9976
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9995 = relay.var("var_9995", dtype = "float64", shape = (10, 3, 1))#candidate|9995|(10, 3, 1)|var|float64
uop_9996 = relay.cos(var_9995.astype('float64')) # shape=(10, 3, 1)
func_8633_call = mod.get_global_var('func_8633')
func_8634_call = mutated_mod.get_global_var('func_8634')
call_9998 = relay.TupleGetItem(func_8633_call(), 0)
call_9999 = relay.TupleGetItem(func_8634_call(), 0)
output = relay.Tuple([uop_9996,call_9998,])
output2 = relay.Tuple([uop_9996,call_9999,])
func_10016 = relay.Function([var_9995,], output)
mod['func_10016'] = func_10016
mod = relay.transform.InferType()(mod)
var_10017 = relay.var("var_10017", dtype = "float64", shape = (10, 3, 1))#candidate|10017|(10, 3, 1)|var|float64
output = func_10016(var_10017)
func_10018 = relay.Function([var_10017], output)
mutated_mod['func_10018'] = func_10018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_10035 = relay.TupleGetItem(func_3234_call(), 0)
call_10036 = relay.TupleGetItem(func_3235_call(), 0)
uop_10040 = relay.erf(call_10035.astype('float32')) # shape=(10, 2, 13)
uop_10042 = relay.erf(call_10036.astype('float32')) # shape=(10, 2, 13)
func_7720_call = mod.get_global_var('func_7720')
func_7721_call = mutated_mod.get_global_var('func_7721')
call_10050 = relay.TupleGetItem(func_7720_call(), 0)
call_10051 = relay.TupleGetItem(func_7721_call(), 0)
func_6552_call = mod.get_global_var('func_6552')
func_6556_call = mutated_mod.get_global_var('func_6556')
var_10054 = relay.var("var_10054", dtype = "int32", shape = (1386,))#candidate|10054|(1386,)|var|int32
call_10053 = relay.TupleGetItem(func_6552_call(relay.reshape(var_10054.astype('int32'), [11, 9, 14]), relay.reshape(var_10054.astype('int32'), [11, 9, 14]), ), 0)
call_10055 = relay.TupleGetItem(func_6556_call(relay.reshape(var_10054.astype('int32'), [11, 9, 14]), relay.reshape(var_10054.astype('int32'), [11, 9, 14]), ), 0)
func_7610_call = mod.get_global_var('func_7610')
func_7612_call = mutated_mod.get_global_var('func_7612')
call_10076 = func_7610_call()
call_10077 = func_7610_call()
func_4440_call = mod.get_global_var('func_4440')
func_4442_call = mutated_mod.get_global_var('func_4442')
const_10085 = relay.const([1,-10,3,-6,-3,5,10,5,-4,-4,-10,2,1,-4,6,-3,-9,-7,10,-5,2,7,9,-6,4,7,2,-5,1,-1,5,6,-6,10,-8,1,6,4,9,6,7,-1,-5,4,-6,-4,9,-8,-3,-3,3,1,-3,3,-2,-9,-4,-9,-5,-8,-8,-5,-2,-9,1,-6,-7,4,-3,-4,-7,7,1,2,-9,-10,-3,-1,8,-10,6,-3,-6,-3,-3,-7,9,-4,9,8,-6,-6,-3,-4,1,-2,-3,-7,2,-9,6,5,-9,6,5,-8,4,2,1,10,1,6,-7,-4,-5,-5,-10,-6,1,6,8,9,-6,-9,8,-8,1,4,8,-10,2,4], dtype = "int16")#candidate|10085|(132,)|const|int16
call_10084 = relay.TupleGetItem(func_4440_call(relay.reshape(const_10085.astype('int16'), [132, 1])), 1)
call_10086 = relay.TupleGetItem(func_4442_call(relay.reshape(const_10085.astype('int16'), [132, 1])), 1)
output = relay.Tuple([uop_10040,call_10050,call_10053,var_10054,call_10076,call_10084,const_10085,])
output2 = relay.Tuple([uop_10042,call_10051,call_10055,var_10054,call_10077,call_10086,const_10085,])
func_10096 = relay.Function([var_10054,], output)
mod['func_10096'] = func_10096
mod = relay.transform.InferType()(mod)
mutated_mod['func_10096'] = func_10096
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10097 = relay.var("var_10097", dtype = "int32", shape = (1386,))#candidate|10097|(1386,)|var|int32
func_10096_call = mutated_mod.get_global_var('func_10096')
call_10098 = func_10096_call(var_10097)
output = call_10098
func_10099 = relay.Function([var_10097], output)
mutated_mod['func_10099'] = func_10099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8281_call = mod.get_global_var('func_8281')
func_8282_call = mutated_mod.get_global_var('func_8282')
call_10138 = relay.TupleGetItem(func_8281_call(), 0)
call_10139 = relay.TupleGetItem(func_8282_call(), 0)
func_5920_call = mod.get_global_var('func_5920')
func_5922_call = mutated_mod.get_global_var('func_5922')
call_10142 = relay.TupleGetItem(func_5920_call(), 0)
call_10143 = relay.TupleGetItem(func_5922_call(), 0)
output = relay.Tuple([call_10138,call_10142,])
output2 = relay.Tuple([call_10139,call_10143,])
func_10169 = relay.Function([], output)
mod['func_10169'] = func_10169
mod = relay.transform.InferType()(mod)
mutated_mod['func_10169'] = func_10169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10169_call = mutated_mod.get_global_var('func_10169')
call_10170 = func_10169_call()
output = call_10170
func_10171 = relay.Function([], output)
mutated_mod['func_10171'] = func_10171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3725_call = mod.get_global_var('func_3725')
func_3726_call = mutated_mod.get_global_var('func_3726')
call_10208 = relay.TupleGetItem(func_3725_call(), 0)
call_10209 = relay.TupleGetItem(func_3726_call(), 0)
func_3542_call = mod.get_global_var('func_3542')
func_3543_call = mutated_mod.get_global_var('func_3543')
call_10223 = relay.TupleGetItem(func_3542_call(), 1)
call_10224 = relay.TupleGetItem(func_3543_call(), 1)
func_7223_call = mod.get_global_var('func_7223')
func_7225_call = mutated_mod.get_global_var('func_7225')
const_10239 = relay.const([3.046588,-8.132941,7.279029,-6.232611,5.571764,0.695704,-3.038273,0.368183,6.921001,-8.019141,8.719581,-9.800530,-0.379530,-2.525312,8.895750,3.311261,-1.964802,-6.996221,4.893463,-6.489778,-2.128838,4.871554,-5.298410,-6.602937,3.227158,9.006746,-8.943074,5.536154,5.304393,7.795123,6.214293,1.845416,-6.900948,-9.275860,-9.691921,-7.070284,-9.601438,-5.784375,-0.857944,-9.962293,4.861114,-1.400910,-8.240113,-8.174486,-9.180044,-2.178325,-9.102633,4.159350,0.363571,-4.512822,-3.439177,-8.020376,6.416152,9.528365,-0.688342,6.126445,0.727745,7.938715,-7.494602,-3.862097,2.445651,-2.639747,-4.432043,-0.796258], dtype = "float32")#candidate|10239|(64,)|const|float32
call_10238 = relay.TupleGetItem(func_7223_call(relay.reshape(const_10239.astype('float32'), [64,])), 3)
call_10240 = relay.TupleGetItem(func_7225_call(relay.reshape(const_10239.astype('float32'), [64,])), 3)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_10244 = relay.TupleGetItem(func_3234_call(), 0)
call_10245 = relay.TupleGetItem(func_3235_call(), 0)
const_10247 = relay.const([-7.055838,8.772293,-8.000153,-5.336506,9.126035,8.789783,-9.570782,-0.081693,-7.375380,-4.991124,-9.169329,8.764983,6.107598,-5.497216,-9.973456,5.731687,7.744131,-1.831031,-7.073493,5.400741,-4.255084,8.237785,7.538977,1.412571,-3.000316,0.649354,-8.388698,-5.071352,-4.142004,-3.076669,4.542055,0.925690,-5.200788,-4.604843,-4.164677,-2.255361,-8.850245,-6.702079,5.576630,3.439319,5.309126,-8.568877,-2.911813,1.127945,6.781699,4.079701,5.027860,5.868758,8.146960,-7.875519,-6.855685,-8.222607,-8.838128,-2.852751,8.766897,-0.888332,4.976919,-6.287623,5.007647,-9.217191,2.095046,4.224470,-5.228635,3.346478], dtype = "float32")#candidate|10247|(64,)|const|float32
bop_10248 = relay.greater(const_10239.astype('bool'), relay.reshape(const_10247.astype('bool'), relay.shape_of(const_10239))) # shape=(64,)
output = relay.Tuple([call_10208,call_10223,call_10238,call_10244,bop_10248,])
output2 = relay.Tuple([call_10209,call_10224,call_10240,call_10245,bop_10248,])
func_10262 = relay.Function([], output)
mod['func_10262'] = func_10262
mod = relay.transform.InferType()(mod)
mutated_mod['func_10262'] = func_10262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10262_call = mutated_mod.get_global_var('func_10262')
call_10263 = func_10262_call()
output = call_10263
func_10264 = relay.Function([], output)
mutated_mod['func_10264'] = func_10264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5074_call = mod.get_global_var('func_5074')
func_5075_call = mutated_mod.get_global_var('func_5075')
call_10275 = relay.TupleGetItem(func_5074_call(), 2)
call_10276 = relay.TupleGetItem(func_5075_call(), 2)
output = call_10275
output2 = call_10276
func_10279 = relay.Function([], output)
mod['func_10279'] = func_10279
mod = relay.transform.InferType()(mod)
output = func_10279()
func_10280 = relay.Function([], output)
mutated_mod['func_10280'] = func_10280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3919_call = mod.get_global_var('func_3919')
func_3921_call = mutated_mod.get_global_var('func_3921')
call_10296 = func_3919_call()
call_10297 = func_3919_call()
func_2671_call = mod.get_global_var('func_2671')
func_2675_call = mutated_mod.get_global_var('func_2675')
var_10301 = relay.var("var_10301", dtype = "uint32", shape = (384,))#candidate|10301|(384,)|var|uint32
const_10302 = relay.const([[9.636065,-0.110804],[-2.050595,-5.942805],[-0.711139,9.643501],[9.256773,-2.056659],[8.075482,-4.070338],[4.012868,0.839756],[-6.063468,-4.605065],[6.364195,-2.066484],[1.002704,4.050227],[1.574647,3.017172],[4.763737,-4.232375],[0.389974,3.877046],[9.238427,5.067381],[-8.760396,2.914305],[-0.283396,4.491783],[-1.201731,-0.960031],[-0.281790,1.000234],[6.256955,1.250498],[5.078941,-2.001136],[2.073592,-5.798214],[9.552916,8.186751],[-5.305104,-4.765864],[-3.205130,-5.958595],[-3.275012,5.980063],[-1.513027,-0.973898],[3.798887,1.887021],[8.586524,0.298801],[7.227985,5.680256],[-5.196340,6.145451],[-9.039664,6.405581],[3.462180,1.412504],[-8.791249,3.469988],[-0.608720,1.679157],[9.704081,-1.499169],[-8.166019,4.112948],[6.694766,-2.481069],[-8.505619,-9.027173],[3.994700,8.157004],[7.074475,-1.144558],[0.140305,3.837269],[1.800378,-5.540688],[0.975669,3.053264],[-2.068821,9.906496],[-8.457181,3.873842],[1.436644,0.902452],[3.277786,-5.404434],[4.279658,5.018842],[-8.582948,-7.813418],[4.263790,-6.061316],[-7.039344,-6.311142],[9.078596,-8.521164],[6.889972,-6.498986],[-0.017089,2.179181],[-3.128476,-1.302497],[6.603615,4.936786],[-6.116042,2.294168],[-9.533147,-1.971958],[-7.192051,8.438204],[2.505147,8.788259],[-3.580650,2.533181],[9.350904,-0.683379],[-0.631106,3.419556],[-1.059631,4.319301],[8.003159,-0.609411],[6.749468,-0.326237],[3.529311,7.071736],[3.314921,8.885907],[-3.100068,-7.430258],[-1.430915,9.538313],[-5.656517,-6.492942],[4.931351,5.126426],[-6.483996,-5.494912],[3.859340,1.335695],[9.241560,5.938113],[5.720780,-1.938082],[1.253540,6.033895],[6.377252,9.969864],[-6.392542,9.097828],[3.604665,-2.268705],[-3.244645,5.143648],[9.573042,5.388196],[6.834008,4.576048],[8.648479,-7.747431],[3.959610,-3.417226],[1.714187,-2.085038],[4.882888,8.736222],[-8.852805,4.074919],[6.433994,-8.398517],[7.132291,6.507848],[-6.591349,-4.537231],[-1.684502,4.469137],[-2.595923,-4.802156],[2.181148,7.214507],[-2.388330,7.733456],[-9.747751,-1.302184],[-5.012893,-4.963497],[-9.581586,-4.001663],[8.955435,-6.212835],[-8.899623,7.734444],[-8.436669,-9.799673],[-8.309792,-7.238015],[-9.172510,7.683783],[-1.083620,-4.337978],[6.618099,4.117643],[-9.498147,-9.665361],[-2.545192,3.838973],[-2.285423,3.976780],[8.046711,-2.309893],[-6.976977,-2.643535],[3.783481,8.193957],[3.261188,-4.797810],[5.256860,-6.241319],[1.091556,7.242301],[-7.434478,-7.708365],[5.400507,0.176286],[6.092811,-9.205262],[-6.108863,1.220388],[-4.364338,-4.120346],[-5.761185,-0.502232],[-5.230874,-8.266036],[-1.734788,4.895780],[-4.141178,2.062138],[0.535532,-9.991317],[1.864712,-2.353170],[-9.859173,6.606325],[2.129685,-9.839992],[-7.084208,7.050627],[-6.246517,-3.694921],[4.985081,5.590540],[-2.301240,0.954754],[8.903118,-1.323195],[-2.006366,-4.522502],[-5.518436,5.469301],[1.690694,-6.076036],[3.286805,-8.222575],[9.337473,-3.830971],[-5.425854,-8.202122],[-1.461087,9.932874],[-2.397690,-5.134689],[-0.405093,6.860371],[-5.473460,-1.627781],[-6.132086,7.469190],[-4.919615,5.461533],[0.872582,-0.234743],[7.429719,-2.016451],[-8.880251,1.910893],[5.813631,1.766439],[8.718677,2.691925],[-7.509607,0.768553],[-0.083759,-8.703478],[1.047427,-2.831463],[6.771852,-5.825560],[2.120022,-6.666515],[-7.144483,-1.118462],[-3.690921,-4.824068],[-1.336346,7.511178],[6.477053,-8.703154],[-1.323010,8.784661],[-0.593920,-8.777828],[-6.441896,3.849802],[8.511763,-9.079257],[8.097781,9.869315],[-6.194319,2.413475],[3.608377,6.876993],[-8.343167,-0.067010],[-6.133196,-9.159418],[8.880461,-5.022228],[7.433082,-2.981742],[-9.580984,9.046022],[0.721899,0.134652],[-9.459123,9.773183],[9.751285,-7.179681],[-6.643375,-6.953096],[-2.500861,9.051968],[2.598275,-5.130835],[4.379414,0.732468],[3.446278,-9.868490],[-7.724008,-9.041153],[-0.112194,-5.203645],[3.812046,1.369389],[-5.135608,-8.775444],[-0.524794,-1.853996],[-7.156774,6.091482],[0.749310,1.679392],[1.079312,-0.921905],[8.908353,-9.663096],[-2.911811,5.238684],[9.261219,0.620934],[7.402484,5.758764],[0.043972,0.281340],[-6.114425,-9.103397],[-9.839076,-8.886301],[6.838680,3.772308],[6.253099,-8.962526],[-6.460650,5.015060],[5.004395,2.553946],[4.587556,-7.372990],[3.856327,-5.849192],[-6.317089,7.187019],[-8.336896,-6.270315],[-8.926422,-7.416566],[6.792118,9.777935],[-5.032668,-9.218239],[4.490968,-7.411621],[-7.633526,-2.038001],[6.670459,2.376598],[9.423916,-1.058959],[-4.839514,0.535263],[-8.913680,-4.470943],[-3.140737,7.228065],[6.332847,-7.110338],[-5.370705,5.385479],[-6.413744,-4.893644],[-8.274140,7.073978],[-7.885980,2.462889],[4.813102,-2.012369],[-3.545781,1.375326],[-8.454850,6.428146],[-9.462028,9.951126],[8.278535,3.952998],[-3.005854,3.030845],[6.781984,-7.164143],[-2.777875,-2.830391],[-5.944109,0.408285],[-2.043521,0.148035],[9.715172,-9.705745],[8.202009,-1.657788],[-9.852385,-4.015542],[8.537851,1.058731],[-2.581682,1.981993],[3.103579,-3.337463],[-1.061177,-5.992206],[4.794252,6.080258],[-7.058357,-9.224237],[6.798637,-0.716908],[9.585646,-5.417910],[-0.349573,0.456738],[6.282400,9.199613],[4.639178,-5.155988],[8.567648,-7.241589],[4.312717,-5.045463],[3.249049,4.360937],[6.817358,-8.502065],[-6.375833,-8.729102],[-9.936300,2.399108],[-5.743204,-1.786138],[3.061491,4.355714],[1.959189,2.358768],[6.957587,-8.962455],[-9.337859,-1.734519],[-7.217075,-7.316902],[9.940914,5.561008],[6.383319,-4.167116],[-4.142817,5.703218],[4.898039,-8.570673],[-5.589625,8.698551],[5.969706,-3.649427],[3.395018,-9.246884],[2.868079,-9.194004],[5.651568,-3.561600],[8.552613,-0.053734],[2.862347,6.556510],[-7.423181,9.931574],[9.023339,-7.098365],[-4.983129,-4.776543],[5.529953,3.155355],[-8.193768,-0.037831],[-3.451128,-7.048790],[9.480409,6.503356],[-7.505860,4.691047],[-2.630510,1.277850],[-5.220195,4.666519],[-9.233001,-6.974645],[-8.536163,-2.858738],[-7.587962,-4.148375],[6.898331,-8.396938],[8.833808,7.134284],[-7.445303,-9.283551],[9.675919,-2.810636],[6.817101,-5.053194],[7.770770,-3.527966],[4.266100,-4.440511],[0.333236,-2.963710],[5.985879,6.731249],[-2.347426,-1.432702],[1.632598,7.916911],[-1.382284,-1.699380],[8.486889,1.455196]], dtype = "float32")#candidate|10302|(288, 2)|const|float32
var_10303 = relay.var("var_10303", dtype = "float32", shape = (2, 160))#candidate|10303|(2, 160)|var|float32
call_10300 = relay.TupleGetItem(func_2671_call(relay.reshape(var_10301.astype('uint32'), [384,]), relay.reshape(const_10302.astype('float32'), [576,]), relay.reshape(var_10303.astype('float32'), [320,]), ), 4)
call_10304 = relay.TupleGetItem(func_2675_call(relay.reshape(var_10301.astype('uint32'), [384,]), relay.reshape(const_10302.astype('float32'), [576,]), relay.reshape(var_10303.astype('float32'), [320,]), ), 4)
uop_10305 = relay.cosh(var_10303.astype('float64')) # shape=(2, 160)
bop_10310 = relay.floor_mod(uop_10305.astype('float32'), relay.reshape(var_10303.astype('float32'), relay.shape_of(uop_10305))) # shape=(2, 160)
func_7898_call = mod.get_global_var('func_7898')
func_7899_call = mutated_mod.get_global_var('func_7899')
call_10315 = relay.TupleGetItem(func_7898_call(), 0)
call_10316 = relay.TupleGetItem(func_7899_call(), 0)
func_6774_call = mod.get_global_var('func_6774')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_10319 = relay.TupleGetItem(func_6774_call(), 0)
call_10320 = relay.TupleGetItem(func_6775_call(), 0)
func_8281_call = mod.get_global_var('func_8281')
func_8282_call = mutated_mod.get_global_var('func_8282')
call_10324 = relay.TupleGetItem(func_8281_call(), 0)
call_10325 = relay.TupleGetItem(func_8282_call(), 0)
func_7720_call = mod.get_global_var('func_7720')
func_7721_call = mutated_mod.get_global_var('func_7721')
call_10326 = relay.TupleGetItem(func_7720_call(), 0)
call_10327 = relay.TupleGetItem(func_7721_call(), 0)
output = relay.Tuple([call_10296,call_10300,var_10301,const_10302,bop_10310,call_10315,call_10319,call_10324,call_10326,])
output2 = relay.Tuple([call_10297,call_10304,var_10301,const_10302,bop_10310,call_10316,call_10320,call_10325,call_10327,])
func_10338 = relay.Function([var_10301,var_10303,], output)
mod['func_10338'] = func_10338
mod = relay.transform.InferType()(mod)
mutated_mod['func_10338'] = func_10338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10338_call = mutated_mod.get_global_var('func_10338')
var_10340 = relay.var("var_10340", dtype = "uint32", shape = (384,))#candidate|10340|(384,)|var|uint32
var_10341 = relay.var("var_10341", dtype = "float32", shape = (2, 160))#candidate|10341|(2, 160)|var|float32
call_10339 = func_10338_call(var_10340,var_10341,)
output = call_10339
func_10342 = relay.Function([var_10340,var_10341,], output)
mutated_mod['func_10342'] = func_10342
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10431 = relay.var("var_10431", dtype = "float64", shape = (4, 7, 14))#candidate|10431|(4, 7, 14)|var|float64
uop_10432 = relay.sinh(var_10431.astype('float64')) # shape=(4, 7, 14)
bop_10437 = relay.greater_equal(uop_10432.astype('bool'), relay.reshape(var_10431.astype('bool'), relay.shape_of(uop_10432))) # shape=(4, 7, 14)
bop_10440 = relay.mod(bop_10437.astype('float32'), relay.reshape(uop_10432.astype('float32'), relay.shape_of(bop_10437))) # shape=(4, 7, 14)
output = relay.Tuple([bop_10440,])
output2 = relay.Tuple([bop_10440,])
func_10457 = relay.Function([var_10431,], output)
mod['func_10457'] = func_10457
mod = relay.transform.InferType()(mod)
mutated_mod['func_10457'] = func_10457
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10458 = relay.var("var_10458", dtype = "float64", shape = (4, 7, 14))#candidate|10458|(4, 7, 14)|var|float64
func_10457_call = mutated_mod.get_global_var('func_10457')
call_10459 = func_10457_call(var_10458)
output = call_10459
func_10460 = relay.Function([var_10458], output)
mutated_mod['func_10460'] = func_10460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1522_call = mod.get_global_var('func_1522')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_10512 = relay.TupleGetItem(func_1522_call(), 1)
call_10513 = relay.TupleGetItem(func_1524_call(), 1)
output = relay.Tuple([call_10512,])
output2 = relay.Tuple([call_10513,])
func_10526 = relay.Function([], output)
mod['func_10526'] = func_10526
mod = relay.transform.InferType()(mod)
output = func_10526()
func_10527 = relay.Function([], output)
mutated_mod['func_10527'] = func_10527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_10627 = relay.TupleGetItem(func_3507_call(), 1)
call_10628 = relay.TupleGetItem(func_3509_call(), 1)
var_10651 = relay.var("var_10651", dtype = "uint32", shape = (8, 16, 3))#candidate|10651|(8, 16, 3)|var|uint32
bop_10652 = relay.greater_equal(call_10627.astype('bool'), relay.reshape(var_10651.astype('bool'), relay.shape_of(call_10627))) # shape=(8, 16, 3)
bop_10655 = relay.greater_equal(call_10628.astype('bool'), relay.reshape(var_10651.astype('bool'), relay.shape_of(call_10628))) # shape=(8, 16, 3)
uop_10690 = relay.cos(call_10627.astype('float32')) # shape=(8, 16, 3)
uop_10692 = relay.cos(call_10628.astype('float32')) # shape=(8, 16, 3)
bop_10695 = relay.equal(bop_10652.astype('bool'), relay.reshape(var_10651.astype('bool'), relay.shape_of(bop_10652))) # shape=(8, 16, 3)
bop_10698 = relay.equal(bop_10655.astype('bool'), relay.reshape(var_10651.astype('bool'), relay.shape_of(bop_10655))) # shape=(8, 16, 3)
bop_10701 = relay.floor_mod(uop_10690.astype('float32'), relay.reshape(bop_10652.astype('float32'), relay.shape_of(uop_10690))) # shape=(8, 16, 3)
bop_10704 = relay.floor_mod(uop_10692.astype('float32'), relay.reshape(bop_10655.astype('float32'), relay.shape_of(uop_10692))) # shape=(8, 16, 3)
func_4855_call = mod.get_global_var('func_4855')
func_4856_call = mutated_mod.get_global_var('func_4856')
call_10706 = relay.TupleGetItem(func_4855_call(), 2)
call_10707 = relay.TupleGetItem(func_4856_call(), 2)
output = relay.Tuple([bop_10695,bop_10701,call_10706,])
output2 = relay.Tuple([bop_10698,bop_10704,call_10707,])
func_10708 = relay.Function([var_10651,], output)
mod['func_10708'] = func_10708
mod = relay.transform.InferType()(mod)
var_10709 = relay.var("var_10709", dtype = "uint32", shape = (8, 16, 3))#candidate|10709|(8, 16, 3)|var|uint32
output = func_10708(var_10709)
func_10710 = relay.Function([var_10709], output)
mutated_mod['func_10710'] = func_10710
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10743 = relay.var("var_10743", dtype = "int16", shape = (9, 15, 1))#candidate|10743|(9, 15, 1)|var|int16
var_10744 = relay.var("var_10744", dtype = "int16", shape = (9, 15, 7))#candidate|10744|(9, 15, 7)|var|int16
bop_10745 = relay.logical_xor(var_10743.astype('int16'), var_10744.astype('int16')) # shape=(9, 15, 7)
output = bop_10745
output2 = bop_10745
func_10749 = relay.Function([var_10743,var_10744,], output)
mod['func_10749'] = func_10749
mod = relay.transform.InferType()(mod)
mutated_mod['func_10749'] = func_10749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10749_call = mutated_mod.get_global_var('func_10749')
var_10751 = relay.var("var_10751", dtype = "int16", shape = (9, 15, 1))#candidate|10751|(9, 15, 1)|var|int16
var_10752 = relay.var("var_10752", dtype = "int16", shape = (9, 15, 7))#candidate|10752|(9, 15, 7)|var|int16
call_10750 = func_10749_call(var_10751,var_10752,)
output = call_10750
func_10753 = relay.Function([var_10751,var_10752,], output)
mutated_mod['func_10753'] = func_10753
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10843 = relay.const([[[-4,-1,-5,3,5,-8,-2,5,-4,3,6,-6,3,6,2,1],[-8,-6,9,1,-9,2,7,-9,2,4,7,3,-7,-3,-4,7],[-7,5,2,1,8,-5,3,-9,-10,-1,2,5,2,8,-4,-7],[8,8,9,-3,3,1,4,8,-2,-8,-4,6,3,-1,-1,-8],[2,10,5,8,1,-3,1,8,-2,-10,9,4,1,1,-6,2],[-4,7,6,-7,-7,4,4,1,-8,4,-6,1,4,1,10,-7],[-6,4,-2,-10,3,-6,8,5,-10,-5,-7,-4,-8,-2,8,3],[-4,5,1,-6,1,-3,9,5,7,6,4,-5,-6,-3,6,8],[4,-5,-9,1,-3,9,2,-3,-1,3,10,-10,-4,-3,-8,8],[4,-8,6,-5,6,5,5,9,7,-1,-9,-7,1,-1,1,-2],[-5,-2,-2,4,-8,-7,4,-6,7,2,-8,9,9,10,-9,8],[5,-9,-4,4,-9,-4,-9,8,10,2,-8,-9,10,8,-2,-5],[4,-1,-4,-10,-7,10,7,-2,7,-6,6,2,3,-5,-6,-1],[2,-9,-8,-3,-5,3,-10,-10,-10,2,2,-1,-5,1,7,-2]],[[-3,-9,-9,-9,3,10,-6,10,7,-3,-7,-5,3,4,5,10],[6,-2,-10,-1,1,-6,-2,-5,10,1,4,-2,9,6,-1,-5],[-6,3,-5,10,-8,5,3,-10,-9,10,6,-2,-7,10,-7,-6],[1,8,6,4,-4,-3,-10,-2,5,-4,-4,-5,-7,3,-1,6],[10,9,-1,1,1,-4,8,-2,8,3,4,-4,-2,-6,6,6],[5,-4,-10,4,1,-4,4,2,-4,3,-1,-3,-4,10,9,9],[-3,2,10,-7,-4,7,-1,-9,4,-6,-8,9,-6,-3,-7,2],[-5,-5,2,5,-5,5,3,-2,3,1,-5,-5,-1,9,-1,8],[-5,1,5,5,-8,7,-4,8,4,-1,4,-1,4,-3,-1,1],[5,5,-7,9,3,-9,-4,-6,-8,9,-3,-7,2,-2,-2,-9],[4,-7,6,-6,-6,6,2,8,9,10,-10,8,8,5,10,8],[-9,3,-5,-4,6,8,-2,-5,-6,10,3,-7,6,10,-5,-10],[-5,10,5,-10,-4,8,7,-4,2,8,-1,-6,-5,5,-7,4],[1,2,6,7,-2,-3,-10,-1,-10,-8,2,-2,-2,-6,-3,1]],[[-4,9,6,-9,3,-7,-8,5,-5,-3,-7,-7,1,8,-4,7],[5,-8,-6,-1,-9,-3,-7,9,3,3,6,-1,-1,-10,-9,5],[-4,6,9,10,6,-7,2,-6,-7,-7,7,7,-6,-5,5,-10],[4,-1,-3,-1,4,1,5,1,6,-2,-5,-1,7,7,-7,-2],[-4,3,6,8,3,6,-9,-7,-4,-6,-1,1,2,-1,4,9],[10,5,6,-6,5,7,8,6,7,2,-8,6,-10,8,-2,-3],[-9,-8,4,-5,3,-10,8,-4,8,10,8,8,5,-3,-5,1],[7,-8,-1,-7,-5,-9,4,7,-1,10,5,9,-3,8,1,1],[-9,8,-4,-6,3,-1,1,9,-4,-1,-6,-8,-5,9,4,-5],[-9,-2,-7,1,6,-6,-9,-6,7,-2,10,-4,-6,4,-2,-2],[-9,3,5,-7,-5,7,-2,-9,-4,2,10,-2,8,6,-2,-1],[7,8,-6,-4,-10,7,5,8,6,5,7,-4,-1,5,3,6],[-9,-1,-9,-8,-5,8,-10,1,-8,3,6,-10,-2,-2,-2,2],[-3,6,7,1,-8,3,-7,3,-3,-1,-8,5,6,4,6,-9]],[[8,-10,-9,6,-10,-3,-5,2,-5,-8,4,2,3,-9,-1,-9],[-2,-3,-10,8,1,-6,-8,-6,-1,-7,-10,-6,4,-3,2,5],[10,6,-8,-1,6,5,8,-10,-8,4,7,-2,-3,-7,8,10],[-9,-2,-3,-7,-10,4,4,7,-10,-3,-10,7,1,-10,-3,8],[1,10,-3,-2,9,-3,9,-6,-2,3,3,9,1,4,-4,-9],[-4,-8,5,-4,-5,9,8,10,-4,5,-2,-5,4,8,-4,2],[5,9,-9,6,9,-7,-1,-10,-9,-4,9,-3,-1,-2,9,4],[-5,5,5,7,5,2,10,-10,-7,9,6,-1,-6,-3,-9,10],[2,-8,-9,3,-9,-1,-9,8,-7,-3,1,-1,9,2,3,-1],[-9,1,4,-1,9,1,-5,5,6,-7,4,-3,-4,-2,-9,1],[2,6,-4,-8,-1,10,-10,7,4,4,-4,10,6,-4,-5,-2],[4,4,9,2,2,5,8,-9,-8,10,-2,9,-4,-2,7,-7],[-4,-1,-10,-2,-9,-4,8,1,6,7,4,7,-10,-7,3,-10],[-3,-7,-5,9,5,-3,7,-3,5,-5,8,9,9,5,-1,8]],[[-5,1,5,4,-3,4,-10,5,7,-6,-1,2,-2,3,-1,7],[7,6,6,-3,8,9,6,-5,5,9,6,-8,-10,2,-6,-7],[-7,-7,6,3,9,2,-7,10,10,-10,3,-7,-2,4,7,1],[6,-10,7,-6,3,-2,7,-4,3,3,1,9,-10,1,6,-3],[9,-7,-7,3,-3,2,-8,6,10,5,3,7,9,-1,8,-9],[9,3,9,6,2,-3,-4,-2,-2,6,-1,7,8,4,3,-5],[9,6,6,1,10,8,5,-6,7,10,-4,-9,-4,10,-6,8],[5,-5,-6,8,-10,-7,6,-10,5,2,-5,-2,4,6,9,7],[-8,6,7,-7,2,-2,9,-3,9,4,6,5,-9,4,-5,-3],[-3,6,-5,-9,-10,7,-10,-2,6,7,1,6,4,-8,-10,1],[-10,-3,3,1,-2,1,-9,-5,10,-10,3,-8,7,6,-7,-1],[6,-1,8,2,-10,-2,-7,-7,8,-7,3,-7,-3,8,-10,6],[-4,6,-9,-10,5,-10,-10,9,-4,8,-4,-10,8,7,-8,5],[-2,-4,3,-3,-7,-1,2,4,6,5,-8,7,6,5,10,6]]], dtype = "int16")#candidate|10843|(5, 14, 16)|const|int16
var_10844 = relay.var("var_10844", dtype = "int16", shape = (5, 14, 16))#candidate|10844|(5, 14, 16)|var|int16
bop_10845 = relay.less(const_10843.astype('bool'), relay.reshape(var_10844.astype('bool'), relay.shape_of(const_10843))) # shape=(5, 14, 16)
func_5701_call = mod.get_global_var('func_5701')
func_5704_call = mutated_mod.get_global_var('func_5704')
const_10849 = relay.const([[-4.025786,-2.049792,-0.765260,0.297544,5.371761,5.635265,-6.529881,-6.390616,7.539123,-1.204996,7.118478,-1.459917,-0.872768,3.128691,9.952632,0.342380,5.446125,1.012113,-6.349772,-8.326847,-9.781878,2.118248,6.910819,-8.674535,6.515256,-7.296737,-0.333636,6.161594,-5.834603,-0.447441,6.230613,-8.163311,7.351691,-3.054215,-9.119206,5.153983,-3.308896,2.046313,4.395274,-4.339497,2.164804,3.358843,4.152627,-6.574612,0.730099,3.091552,-7.892423,0.422579,-2.190195,0.428638,-4.468991,4.089167,0.775628,-3.635284,-3.525534,9.896158,-6.578809,4.683037,0.757421,9.532913,-1.613251,6.576316,-4.955719,0.432947,-3.286018,-8.477672,5.702116,7.663024,-3.033016,9.795510,-8.108599,-1.109788,2.028080,4.375904,4.590036,6.563382,8.383400,1.358206,3.745003,-8.894118,6.885477,1.392306,-3.236537,-2.474424,-8.880680,0.305785,-0.024556,8.934127,-1.327834,1.913860,-6.396604,5.494565,8.661163,4.454089,8.285432,3.851916,-1.758845,-8.399781,3.335421,-0.814623,-1.629933,9.727602,5.985779,3.757731,7.184439,-4.955292,9.438498,4.905352,-4.076427,-0.815205,1.441040,-3.840159,-9.376050,-3.777588,3.433778,2.900017,9.115304,9.796893,-6.721605,-2.146001,2.845773,2.672889,-3.853665,4.816732,6.151962,4.870026,4.264724,7.492891,-6.519825,-8.119458,-7.571733,7.187535,-8.410779,-9.624288,1.097674,-9.344767,1.307523,-3.635716,-8.680089,-4.916832,1.614617,-5.685931,-7.179988,-8.204880,-3.015138,-3.272671,-4.870440,-1.616936,-5.552209,6.889523,2.275882,-6.524868,0.998024,-0.890895,0.678597,-9.969950,-5.705322,1.721705,-0.818435,9.405058,-7.153647,8.508613,-2.610173,4.679551,-4.985617,-1.224135,-8.277073,1.391028,5.271401,-8.856113,-0.770472,8.074135,0.060253,5.714151,-5.581737,-1.116096,9.744348,-2.531209,2.425942,-3.340815,-4.461230,5.290034,-2.643776,5.314514,2.224472,-9.282436,-2.814346,-6.382217,-0.254904,7.028683,4.763350,-8.869218,5.271862,-4.790328,-1.498649,-7.394444,9.294579,-0.096406,-9.083775,-6.777033,3.367384,-6.284744,-7.365428,1.389774,-8.225910,-3.001100,8.257028,-8.913211,5.074114,0.904052,-2.213232,-5.121844,-1.671387,6.856594,-8.233932,-1.254381,-8.520379,0.296796,8.383563,5.914739,7.871863,7.832458,-5.536188,5.510976,-2.475402,-1.870632,0.362195,9.118436,7.260832,-7.037052,-0.916446,5.326478,6.606317,0.723622,2.868178,4.774299,-8.805627,0.844010,-0.546255,-1.106088,-4.324630,7.105698,-2.343156,4.511388,6.793652,1.173863,-7.071522,-6.277259,-4.780183,-7.278342,6.330435,-8.491452,6.997569,-3.680538,3.511397,-3.573586,6.682416,6.173349,-1.019425,1.396766,-4.524510,7.671438,8.988564,3.993387,-8.838983,-9.742949,4.638817,5.772245,-9.032497,-8.451901,4.937613,2.763061,0.481630,-1.796864,0.196649,0.165757,-5.675050,-4.017776,6.296130,2.406761,-3.903854,3.894665,3.044496,-8.703151,-4.999118,9.751546,6.959873,8.034061,9.509826,4.136335,1.427407,-2.572574,2.249968,-4.593799,-8.096247,-1.924814,7.429293,-6.689246,7.143084,-9.398102,-3.095186,9.495065,2.584764,-6.873415,-7.793321,8.711666,-3.832378,2.207123,6.120374,-6.347779,-5.711348,-6.915940,-0.124146,-0.255269,2.640080,-9.289109,-4.954959,2.901500,-0.859690,-9.239308,3.188678,-5.577949,7.342654,-0.543513,7.693573,1.669835,3.763489,2.214059,-0.177302,0.331009,8.014543,9.736269,7.739780,4.138549,-3.516226,-9.870345,5.196490,-8.366808,1.476310,7.650287,6.806348,-6.841551,-2.273840,2.131202,8.270839,-1.274286,-1.232367,-2.986925,1.873776,3.606151,7.480979,4.578136,-0.989317,5.632720,-7.374941,5.233462,0.992052,5.388743,9.389157,2.679367,7.854505,5.484032,2.076978,-9.071313,6.883429,8.088898,8.752941,-4.604406,-3.202176,4.088322,-2.727604,-0.061860,-4.605894,-8.773727,-7.568881,-1.885592,0.060396,6.512314,4.681444,0.308767,9.662029,1.288838,-7.607207,0.844972,-8.166315,2.690208,0.901294,-2.154205,7.606964,9.850849,-1.754113,-7.537368,-6.866731,9.975787,2.819085,-9.575428,0.097501,2.930381,9.643108,-4.436990]], dtype = "float32")#candidate|10849|(1, 400)|const|float32
call_10848 = relay.TupleGetItem(func_5701_call(relay.reshape(const_10849.astype('float32'), [5, 10, 8])), 0)
call_10850 = relay.TupleGetItem(func_5704_call(relay.reshape(const_10849.astype('float32'), [5, 10, 8])), 0)
func_2501_call = mod.get_global_var('func_2501')
func_2505_call = mutated_mod.get_global_var('func_2505')
const_10852 = relay.const([[5.930057,-1.355077,5.832562,6.453758,5.270968,-2.292797,-2.192855,-6.817244,-7.837620,0.036097,-0.121072,-2.717823,-5.501701,5.302971,-1.283846,-1.153193,-8.311952,7.923459,-5.059774,-5.778686,4.243403,-0.117809,-7.807593,2.638355,5.709848,4.370784,3.829683,8.165779,-3.414376,-2.005343,9.920251,-3.116030,-5.225807,-6.694821,-4.983299,-2.750461,7.316381,3.088119,7.918107,-0.221189,8.260852,-2.851387,7.539943,2.550390,-9.445929,-7.914237,-3.675038,0.426393,6.188117,7.884015,-3.049927,6.978928,-5.467037,-2.289749,7.113495,-4.581306,-3.472414,-8.491452,-2.846771,2.858676,6.331390,2.050939,-7.907060,-4.928092,-9.860688,-0.419843,6.682816,-7.669138,-9.972473,0.751338,5.495805,0.981840,4.072351,4.670573,2.188485,-2.014677,-2.520717,-7.263412,4.686467,-0.787581,-6.988843,-4.715095,-1.212545,7.948053,4.356897,9.638832,-3.041429,6.140468,-6.989935,9.343600,6.314434,-9.254309,4.408693,9.670109,-8.282801,-2.134249,-0.432388,-1.498114,4.065733,2.399513,2.442005,4.772785,5.122109,9.064758,8.728769,0.256126,-7.623122,8.496832,-2.465887,-3.053354,-3.188696,2.485297,-6.726431,-1.312914,3.187760,-5.863829,-0.752315,-9.909709,-1.499551,9.447800,5.416996,1.792895,-3.911650,1.719695,0.513529,8.697266,5.013041,-2.094531,7.813103,9.586462,-2.759403,3.002996,-1.090433,7.241189,4.472921,-7.048588,5.136191,-2.002689,-1.364483,6.007688,-6.875097,-6.662678,5.660396,6.408193,0.605894,-4.931971,-3.700922,-3.525398,8.410883,-5.154544,-4.990693,1.502696,-8.683124,8.530956,-2.113523,-8.724864,-0.875208,-3.531026,6.041953,-2.828742,-5.522263,-7.455294,-8.311921,4.137895,-1.294410,-0.106951,0.120768,7.077584,5.035913,-8.698622,3.720702,-1.384334,1.953038,3.920447,-0.798800,3.208000,-3.562528,-0.139694,-7.770267,5.086201,6.214497,3.946185,5.282421,-6.600785,-0.545992,-2.742229,0.452933,6.388177,9.620893,1.375462,-1.818870,7.454849,-3.703289,4.379262,2.264674,-0.117924,-5.023823,2.234857,-1.964539,-9.883454,6.906343,-9.299959,-5.696870,3.458081,-3.853397,2.203085,-1.310171,-0.104474,-8.501159,0.909341,-6.559862,-0.436477,-3.033509,-4.928161,0.032147,7.390930,-3.700518,7.494046,4.341977,-9.357107,6.312993,-5.954137,-7.582461,1.723620,-9.423215,1.484939,-5.581610,5.218028,4.397238,3.511943,-7.809798,6.183947,-2.682956,7.949801,-3.189943,3.341769,-2.057972,5.849594,-6.378093,2.253186,2.717948,8.484653,7.272309,-8.046642,9.458916,8.978478,-7.220154,-9.015050,-0.234591,-6.675578,2.782641,-6.147632,2.483459,3.324841,-1.157475,-7.672048,0.858421,6.207084,-4.998769,5.621257,3.269222,-2.947698,-1.468136,-5.404236,-5.718408,7.376680,8.537065,1.724001,6.731052,-1.336152,-5.970098,4.827402,2.676608,-4.458268,3.580980,8.610780,-2.095634,-6.603043,-7.792624,7.885307,-0.623571,-8.706871,3.639610,-6.462222,-1.001699,-7.833157,-3.488308,-6.156784,9.315840,2.676258,8.904787,8.459299,-5.823744,-3.906485,5.760907,-7.356430,-7.577622,8.845624,-0.191802,-0.829801,-4.220796,4.046448,-3.653535,-9.465685,-3.926095,-8.087482,-2.618957,-5.172531,-0.544870,3.685048,-9.079747,4.809054,2.717156,-5.473161,-0.388668,-8.918614,-8.294355,6.541044,-5.244630,-3.150193,-9.489224,-5.741360,-6.464086,3.106891,9.495614,-8.900802,-2.932772,-9.534849,-2.227072,-0.979907,2.854075,-2.922154,-2.859254,-3.242185,6.463399,-6.378008,-0.770275,2.915563,2.279416,0.997942,2.640757,-9.242457,5.620413,9.094303,-2.971581,-4.155682,2.184772,8.650060,2.414768,-4.015396,-6.470686,-4.040530,2.050848,9.992649,-3.884399,7.933056,0.583924,-5.804350,-4.501433,-5.174746,2.559287,-7.332743,1.826326,-8.278034,4.399310,-9.911260,0.601930,-8.500577,-5.151247,1.881141,-2.043473,-1.098841,4.696316,-0.078253,9.001300,-4.403822,-5.884486,1.362457,-9.084777,-4.274517,-3.434936,0.992568,7.097001,-1.838271,2.449338,-6.325851,-0.703370,2.397809,5.432143,0.297826,5.369266,1.346844,-9.444763,7.406560,7.126421,-3.494487,-8.058349,9.431496,-0.018186,8.591803,-4.152618,0.776419,0.466945,-3.488272,3.788876,3.595360,1.925759,-0.227661,7.039548,-5.458661,6.462448,-5.100104,-9.822888,3.736861,2.230631,-4.023356,-0.802361,-9.601918,7.687142,3.119686,-0.531204,7.172550,6.922193,5.303184,6.186718,8.816963,-2.218409,6.428277,-7.825959,3.307317,7.860741,7.349930,-7.829653,3.320687,-9.030592,-8.441599,4.274671,-8.724584,3.858612,1.009771,2.910090,1.859536,-7.286635,-0.561770,4.394477,-6.095380,4.521156,-4.024117,6.675303,1.840552,-2.390637,-7.208157,8.996217,8.232076,-5.389088,-9.406163,6.827012,-0.818926,-8.326567,-1.823513,-3.989393,-7.725484,-0.162139,5.579853,6.404484,0.934614,-2.755898,9.449205,-2.602025,-2.750316,-7.455497,-2.200877,-3.625625,5.149729,1.956447,-6.336303,4.836148,-8.835179,-4.188396,3.984198,-8.265538,1.808197,2.104360,0.131159,3.968771,-5.000958,-5.606054,-5.186065,6.487784,0.196665,0.806521,7.354353,-7.898495,8.259873,2.909731,-8.864304,6.202506,0.631138,9.851365,8.543957,-1.067606,-1.796088,-7.182995,-3.182511,-6.319560,7.016893,0.078262,-3.525569,-1.326617,-6.138851,6.370038,1.157358,2.787233,2.106185,8.554202,7.405151,-8.940599,-9.304976,-4.534346,2.535202,-1.851413,6.347009,4.904437,-1.276333,6.536520,2.822618,1.093639,7.097386,8.687258,2.821785,4.146317,1.070144,-4.471917,0.456935,-7.070309,-0.461308,6.258672,-4.608836,2.600882,-0.034186,-0.581061,6.198707,-4.097793,-6.190165,8.740010,0.104853,-4.055181,9.948283,-9.857634,-1.428075,9.508585,-2.756025,-8.212213,2.129579,9.466043,-3.211718,5.946917,5.315157,-7.242722,-3.043931,-2.368078,2.057764,-2.469505,5.558528,6.952466,0.422499,-4.936286,5.235677,-4.022436,5.069829,-6.985033,4.376971,1.729287,5.071779,-2.095931,-2.400796,0.856627,-8.637632,-9.481216,5.918319,8.608593,-7.988360,-0.755790,-8.005595,-8.299021,-2.547365,3.036755,-2.938711,-0.255553,-0.686968,6.096878,1.972987,-4.341005,-2.764195,-8.054667,-1.452485,-7.231544,3.134544,-5.241714,-2.986212,8.775912,3.359572,-7.168201,-5.866408,-7.770559,-5.285743,8.429499,-8.320980,6.101764,-6.526527,-2.999563,9.454844,4.536070,7.876902,-5.484415,-8.019618,-0.331082,-7.701317,5.695395,-6.145024,6.349035,-5.486927,-8.348368,9.322924,0.910178,7.157277,-0.381537,7.253302,-5.789850,-2.090329,-2.098430,-1.276490,-3.070466,2.879734,0.788664,9.530650,-3.435243,6.118456,2.546183,-7.144727,-7.764607,-7.175143,-6.471253,-6.141198,0.197725,4.273519,5.570231,-6.530403,-8.624815,-6.658619,1.987366,1.919660,6.480087,5.030630,7.033081,5.550448,2.674300,-8.374156,9.290338,-0.498077,3.182201,-9.173279,-7.112211,8.066595,5.657361,-1.289645,2.235510,-3.995201,9.903116,0.774353,-5.634397,-4.255764,2.733724,3.780823,-5.475974,2.198463,-8.810460,-4.471856,-7.849187,3.779198,3.361323,9.657195,7.639558,9.813973,4.714279,2.990871,-7.641077,3.181085,5.884045,-5.364634,8.499254,1.739485,-3.348124,-0.871572,7.093894,-7.993359,1.880723,-2.658905,2.836910,7.912062,-0.601725,-1.444013,3.758296,-6.511626,3.320950,-4.418238,-5.917245,-6.486564,7.714236,-0.412730,-6.416219,-0.425995,-2.971211,3.340006,-2.900901,-5.175988,3.324071,6.298598,-8.705223,2.990782,1.976087,-6.920731,-5.621624,-7.822218,1.868327,-3.686576,5.104131,-9.863868,0.912341,5.443025,-6.432330,1.657791,9.593818,-2.481994,-9.526806,6.478886,9.094148,-7.234651,-4.214150,-4.698908,1.685055,2.906075,8.258630,-7.288408,5.218784,-7.855693,8.073539,-7.236568,7.606768,-7.617663,-7.914397,3.923613,-9.982517,3.364979,-1.908582,-5.475494,4.331730,-5.316211,7.649102,7.920856,-6.101997,7.488815,1.324970,-0.599679,-7.922750,1.577507,-5.899893,3.416406,-4.168361,8.804920,-3.627158,-3.755469,-0.917444,-6.480174,4.430803,-9.565165,9.595038,0.501746,4.694340,8.777245,-5.479639,9.853769,3.561831,2.054463,3.971641,-3.675787,6.531610,4.379015,9.843315,4.596459,-2.259819,4.756853,9.143626,-2.631675,-0.544901,7.103685,-0.751753,-9.820040,5.265645,8.398238,-2.736281,-5.740547,-4.291016,3.221190,5.112723,-9.396348,2.213144,8.471759,-2.478166,0.582670,-1.342386,-2.999793,6.902934,-2.226690,-6.537891,-4.592258,-8.070232,-8.649451,-5.889170,-5.760516,4.369633,5.035690,-9.836918,3.245025,3.735500,-3.591945,9.064797,-5.731243,9.939420,5.666224,7.273690,-7.095227,-8.148201,-3.646483,8.824347,-5.031739,-2.205751,9.545156,5.390680,7.250114,0.980387,-0.767118,-8.399897,-3.932114,2.915744,-2.562817,7.422949,-7.706442,1.089677,-3.735075,-8.535418,5.185375,7.453623,5.721561,-0.684854,6.210128,-0.546679,-5.416708,-7.483943,-8.923583,1.951393,-6.663347,-0.643894,-2.656022,-9.282638,-4.744544,-8.702110,4.686451,-7.448983,-6.979115,8.118483,-5.056561,8.234737,7.139541,4.508533,9.802324,-5.930870,9.109583,6.276419,-3.077382,3.493387,-9.879418,0.646322,7.422266,-0.851784,-5.407770,5.562383,-2.797011,0.388168,-7.627174,4.969359,4.815095,-1.324754,-4.559028,7.347994,0.078471,8.315755,-2.103725,0.025945,-4.028498,0.344197,0.054313,-4.387263,0.787353,7.036733,-0.668251,2.177141,-1.338092,9.402489,0.627512,-3.036956,2.189656,-0.188714,-1.632495,1.816749,-6.387439,3.754299,7.751753,6.442528,9.383941,-3.144338,2.748678,-4.061241,9.422784,4.455730,-2.776364,0.004209,0.088160,6.874953,4.746526,6.343002,7.904586,-0.130298,-3.592671,0.610461,-1.060916,5.723719,8.424637,-6.852255,0.630906,-6.666706,1.138334,8.255038,1.509890,-9.065969,0.769175,-4.206849,-9.580003,1.213533,-9.546836,-9.977838,5.498278,9.292809,7.745409,7.694174,1.252937,-8.470540,-8.083813,8.122301,-8.868014,-7.219982,3.694391,-6.163702,9.086817,-6.598164,-0.096501,5.400541,3.895765,4.137345,-0.073147,5.347217,-3.273646,-1.267413,-3.409925,-2.062933,4.557994,-0.730261,-8.709185,-0.897147,7.361896,2.547308,4.140067,2.353838,8.204928,-2.253731,1.698240,4.832025,7.184350,-3.693640,-5.045987,0.428440,-8.906039,-2.725305,-4.266299,-8.779792,-5.478946,-8.745184,-2.207375,-5.445556,-5.231939,9.736119,-8.993730,7.805322,-4.679466,4.259355,-8.417087,-2.096997,3.189276,6.989579,6.594832,7.116418,-2.790850,-0.067839,8.080539,-4.515499,9.909381,5.478776,6.622307,5.840020,4.581588,-5.808110,9.905369,-2.627270,5.409644,6.324766,0.681040,-6.684605,-2.791358,6.152449,8.040657,2.382863,5.938383,5.470106,6.342271,7.806647,0.339783,-2.544688,-5.613654,2.572149,2.399504,3.826011,0.873603,-7.160502,-8.074740,8.441871,7.092361,-4.428952,-0.658988,7.804868,-6.831938,-9.865462,-0.125987,1.812905,6.614015,6.640023,8.543840,2.810425,-8.087679,-3.102138,8.733051,0.268062,-7.069545,-1.918575,6.563751,-3.888810,-2.848140,2.424144,1.249231,4.526250,-5.734921,9.801745,6.050936,-7.997715,-4.239016,-7.296668,1.634863,6.043998,1.589865,-1.901508,3.234317,9.853210,1.962792,3.302326,7.949234,2.892892,2.084575,9.508335,3.222797,-8.353307,-9.009301,-0.703380,-1.485888,3.197067,5.307363,-0.158919,-6.696424,-5.527348,6.342211,-4.166043,-6.967396,-5.184014,9.761236,3.700040,8.866897,-4.858689,-7.676203,7.559177,-5.659768,3.062705,-6.421960,5.375205,9.989240,-7.396089,5.084136,3.749341,-3.732379,4.956799,3.290411,5.125974,-5.094009,-7.026968,-9.114347,-4.884192,-0.015710,-0.850848,0.168078,0.089120,8.723551,2.851060,-0.753248,-0.751001,-5.307783,-9.531720,-1.657072,6.887467,-0.376833,-2.806129,6.123567,9.795253,-6.222234,8.377286,0.172568,-9.852166,-4.182676,0.793045,-9.592007,-9.662759,6.099579,-5.993192,-5.906823,3.737322,1.248600,5.700396,-2.402840,-9.512973,-8.489635,-6.705632,-2.222737,-0.341077,9.173181,9.022713,2.222794,-8.956940,6.578226,3.574766,-2.648489,-1.489966,-5.856540,8.286271,-7.103624,6.966880,6.797074,0.618869,-0.481936,-6.042208,5.111526,1.639684,0.068100,-8.301385,-4.284883,-7.933377,-8.449309,-6.587157,-2.143862,7.942220,5.253169,0.257328,-0.094580,-1.664241,-7.661531,-8.037743,-3.805114,8.943054,-5.833418,-5.055395,0.112335,5.264515,9.272615,-9.111263,1.048179,9.648114,-8.389161,3.751050,8.929777,8.533025,9.636416,7.124343,0.488098,8.290898,-6.494109,-9.394858,2.210658,9.122831,0.562955,-9.780726,7.192915,0.603794,8.575478,8.110006,-0.491185,-9.278280,-2.099158,2.614790,-1.936466,5.418314,5.232134,-6.594840,-4.896788,6.110554,5.762400,-5.480748,0.854983,-3.192581,0.812123,7.516351,-6.768594,2.141072,-3.999074,-0.584795,3.896824,0.153139,2.288306,4.557250,-3.744903,8.546776,3.940437,-2.067721,7.798987,1.901243,-2.617751,-7.612606,-5.568073,-3.042263,4.720808,-2.072311,-0.759123,7.867129,8.666697,2.627866,9.392772,-3.995747,2.158579,-7.958118,7.578525,6.924845,-1.692052,4.822330,0.432534,2.472685,-5.905703,6.878279,-4.421022,4.414910,-7.111113,9.524817,0.896077,-2.201199,-0.373578,-9.364203,-3.843772,-2.125388,3.228748,7.067703,7.454202,3.971224,-3.581904,-8.388944,5.425230,1.085849,9.678803,-1.749481,-2.281667,8.021835,3.814090,-6.288078,8.566144,-7.596385,-0.146786,0.385927,3.876807,-1.028118,8.256219,-8.034374,-7.750208,-3.767665,-8.547619,-2.739950,6.093913,5.931206,5.575107,-0.536702,-3.039493,-4.493719,3.739219,-5.898298,-3.147419,-8.661772,-8.635600,7.157154,-6.188185,-3.433677,-0.629004,8.630194,-8.363592,-0.442223,8.301961,-1.481834,5.295477,-2.916907,-8.158648,1.378880,6.888187,-1.979504,-2.615122,-9.468370,-8.113813,1.863266,-8.905232,-3.652128,-8.386573,-2.587320,-0.853046,4.114981,9.122173,-4.904800,3.053809,1.302397,1.052727,-4.910482,8.171794,5.014101,7.549185,-2.326742,2.908068,-7.165855,5.583663,5.497416,1.659937,4.059305,3.056776,-8.401982,-7.762236,0.390802,7.925627,5.411180,4.523405,-8.021526,-8.682206,-2.603158,-7.595246,9.958491,2.693535,9.102747,3.557500,-9.032832,-6.127429,8.236716,-1.533152,-9.027102,-9.851101,-8.412617,-1.574336,-2.973312,4.393455,9.990314,1.456789,1.807926,0.882212,9.248509,7.981640,0.243376,-6.295434,-0.898622,-8.282893,6.233089,3.813133,-8.838423,-0.902596,-2.397562,0.442877,9.742063,-4.815579,3.530342,9.343155,-2.093380,-7.495462,-0.677583,6.225441,6.467364,-9.000828,-5.911403,-6.260769,4.213182,-4.254124,-7.655471,3.483924,-8.682343,-7.743661,-5.449671,8.544138,9.288671,-2.509091,-4.746528,-8.217828,2.475898,-1.526750,-0.744291,-4.427522,-6.715729,4.350785,-1.875060,-2.285740,-9.915404,4.338703,6.853618,-2.355889,-3.089612,-6.235704,-0.982233,2.087733,7.708789,9.203024,-1.103925,-6.921935,-7.211219,-2.693318,-4.592842,-5.197648,7.445686,1.807253,-1.466416,5.617590,7.451712,4.292777,2.858795,5.059566,0.847123,-8.466665,1.832372,-3.096516,0.481176,-5.988025,3.949722,-6.142907,-1.975933,1.176844,6.461071,-0.586099,2.171370,-2.177482,-5.242429,9.535027,8.719112,2.206321,-3.122314,-6.425093,-7.974262,-3.223688,6.455272,4.973197,-7.368659,-9.331019,9.043719,-6.576655,4.218126,0.634432,0.732842,0.572863,6.672687,8.967514,-8.449445,5.971744,-2.457909,-6.160832,-3.961823,-1.729184,5.224585,0.743655,3.852368,3.344129,-5.862680,-0.964911,5.939695,-0.688770,-5.499539,6.889338,-8.373458,-3.602215,-0.778736,-7.334492,-5.465087,5.839234,-7.434704,-9.824474,5.677829,-6.572019,6.558309,5.566085,-3.047599,1.007577,8.219314,7.045698,5.045450,-4.234424,-7.298207,-3.568596,9.358850,-8.704189,-5.095951,4.310651,-4.759989,-9.272758,-5.870462,0.978536,7.194841,-4.623773,7.415099,-6.232185,0.866379,-3.849743,-5.246534,-4.350245,-8.813990,0.967612,6.166552,-4.177889,-7.434614,6.758091,-9.638227,9.068905,0.031523,-1.696969,7.163812,4.242429,-0.680303,-3.133447,7.306814,-5.058408,-0.527476,-6.512051,1.435133,7.354474,8.948819,-9.824753,5.402853,-9.300043,7.693172,1.093048,1.838361,0.912602,-4.341233,-6.384699,-6.183371,-9.246489,-9.780339,0.785385,8.254628,5.897029,2.594806,9.341306,1.506954,-9.438349,-8.276475,0.859277,-3.707164,7.925741,8.130354,-3.015535,4.440365,-8.797367,-6.215373,8.852564,-4.470707,-5.667183,-8.983461,6.760573,8.565755,6.705098,2.057747,-5.107478,5.021041,5.642886,8.047259,1.538766,-0.323364,5.500898,2.972519,-9.057769,2.309053,9.280656,-5.467889,-8.823060,-9.745664,-3.415238,-0.753413,-9.614053,-7.602100,-6.426030,6.254183,-1.710054,8.365634,-6.746280,-5.504991,9.045664,-8.697043,-9.772592,9.080187,-2.225136,-8.215833,2.651460,3.390973,-6.406601,9.201696,-6.282749,-9.882361,-9.769209,-2.614154,-2.110399,-7.365716,-8.137796,1.256438,3.569465,5.391323,-8.202379,-0.632987,4.292619,5.300274,-9.297592,-6.732338,-8.576607,5.412274,0.837900,9.659892,4.204894,6.127973,-5.073590,-2.028772,0.356528,-5.136245,8.576014,4.028602,-5.099954,-0.167570,-7.805876,2.750618,-9.899602,7.524799,-9.987118,7.212522,-5.793664,-6.471833,6.758018,7.112816,-2.673124,2.793272,-8.456552,-0.404419,0.823847,8.674164,-7.180035,-0.649203,-1.496866,-0.546834,3.766524,-0.197064,-5.553223,-9.100568,2.649905,-4.302817,8.115962,8.306191,-2.171761,7.536352,-3.920398,2.591650,9.967207,0.574612,-0.252542,7.485335,-4.918987,9.816010,-4.994555,-6.013155,2.156558,5.571217,-9.920537,0.279478,2.312791,2.410811,5.426640,-5.630493,-9.886013,-8.794922,2.894981,-3.782089,8.146815,-0.298794,-8.487265,0.294450,9.091549,-5.158811,6.218607,-0.155070,-2.691603,7.384668,5.217922,9.485488,9.202697,-0.476891,9.070895,-9.706327,-4.069532,-0.452181,-0.617239,0.690974,-0.587437,0.327906,2.265142,-8.831749,4.556225,8.270509,2.014156,1.909115,9.570468,9.084155,-0.198474,7.675815,-9.694815,0.752316,-4.490432,-3.287927,7.343374,-9.566678,-3.591033,-7.651526,-9.374187,-5.514753,-0.205956,0.192655,5.728388,-7.532328,-5.727925,-7.443887,0.834680,6.186472,-5.824459,9.132609,-6.294949,-8.290849,-8.778935,-4.924120,1.509580,3.196646,-4.518453,8.496904,5.068613,-8.407057,3.124527,5.780211,-5.856571,-3.606907,-4.308257,-6.120368,-1.993507,8.560674,-7.071888,1.062127,-7.492421,5.515986,8.391450,-1.082556,0.415751,3.363937,-7.598589,3.561612,3.014955,5.341199,5.047972,-7.514496,3.003480,1.614128,-5.200733,9.082751,7.905439,0.703046,4.201054,8.189485,-0.726793,0.165890,9.650189,-7.693436,9.172503,7.792507,3.019284,-7.671931,6.860184,-2.757239,-1.762069,8.386550,0.145345,6.234940,-8.973003,6.478941,7.617912,4.217550,2.596683,0.442123,-3.072180,-4.495417,7.833279,-6.242887,-9.083755,-2.445939,-0.843599,-9.069794,-1.552211,-0.296677,-5.385027,-8.781691,-3.961521,8.564718,8.254284,-0.033562,6.783575,3.485536,6.183982,0.989155,1.237466,7.443369,9.495636,6.095788,6.673585,5.590987,7.902886,1.523743,2.477982,7.798146,6.159566,-8.846177,-6.821120,4.891679,7.461610,0.123263,-3.723014,-8.073923,-0.694327,-7.058398,0.117097,-0.046751,4.158398,1.193389,-2.629353,7.132793,-4.122864,-7.945447,4.557538,0.835644,-1.720467,4.724729,6.741651,6.718545,6.390497,9.634478,2.122389,0.960802,8.823300,8.976001,-4.080429,7.769180,9.648437,6.319263,-0.759131,0.492352,-2.187970,4.357473,0.260977,9.514699,-8.874670,9.137075,-9.126267,-0.801032,3.288390,0.324261,-5.687597,1.722669,-4.152327,2.200745,4.067674,-5.561408,1.214380,6.845584,-2.813551,-4.367891,0.178499,-8.805338,-1.368791,0.786808,-8.585359,2.202369,2.479022,-0.228971,-6.559596,-3.450042,4.651200,7.698312,6.590105,8.927832,8.328127,-5.034311,7.510071,9.642015,-2.997729,-3.378649,7.467179,0.600656,-6.063866,5.304516,1.636591,-2.515670,-4.095752,-5.577996,-3.132060,4.602454,5.031700,-0.404262,-6.002514,-2.292291,-1.319050,2.253312,6.271410,-1.633529,0.964622,-3.731786,-3.023375,3.354050,-6.529494,-1.786148,2.294107,-4.336595,3.036232,2.652073,-5.732498,-0.145974,-4.320512,8.195840,5.694897,9.628045,0.956459,5.807606,-6.372373,-9.507052,-7.941113,0.163766,-9.078145,-7.451820,-6.633763,5.186876,-5.447679,1.505453,5.068927,-3.432644,8.102334,3.308049,3.687567,-4.807562,0.266571,-3.832105,1.494048,0.385278,6.017935,9.751996,-3.133641,7.362105,6.003388,6.796017,1.676894,0.256903,-4.594971,8.971635,8.400294,6.551817,-3.326578,3.612799,-8.729148,1.601990,-7.674052,5.805718,4.559793,6.952214,-8.514994,2.286899,-3.907886,-4.512481,-5.004755,-6.757565,1.727285,-1.010267,3.428925,8.148082,1.401970,-0.959273,0.230500,-9.935676,-1.614097,3.655060,-3.457858,-5.288558,9.188730,3.850541,-0.245615,-4.476629,-9.180865,6.761931,-5.244451,4.836657,3.311135,0.268078,6.572685,3.576581,-8.905885,-6.044041,5.086550,8.995620,0.764020,-0.776146,1.188281,1.527191,-8.421730,9.885279,5.227965,-8.871299,-2.372749,-8.765850,0.118097,8.343789,-5.884351,-6.658607,-3.398036,5.657159,8.317549,5.375692,-1.853634,-5.670450,8.406084,7.352724,-9.288922,6.404277,8.488940,-6.916148,9.149723,-8.132470,-2.977062,-1.361288,3.036119,-4.057222,3.058266,0.531587,5.482173,-4.006591,1.695755,3.443935,5.150332,4.788706,-1.803740,9.583175,7.089947,-1.046360,6.486297,9.758724,-7.211096,7.427826,9.955167,0.381521,-4.035861,-7.264989,2.872570,3.213151,-7.714162,6.312752,-5.115810,8.415728,2.571155,5.809535,-4.802595,8.827964,7.338241,-8.341422,7.138733,1.280291,-6.910008,0.007456,3.278650]], dtype = "float32")#candidate|10852|(1, 2112)|const|float32
var_10853 = relay.var("var_10853", dtype = "float32", shape = (576,))#candidate|10853|(576,)|var|float32
const_10854 = relay.const([-9.506581,-8.993412,9.956115,-6.768429,9.094593,4.751716,-5.189220,9.150716,-2.106662,0.968454,5.067150,-4.768073,1.843992,9.587103,7.670793,5.863692,1.621923,-5.624730,-6.485222,2.262283,-5.942447,8.039598,7.964783,-4.840167,-2.718823,-8.153202,-2.224467,-6.222246,-7.386820,-3.112935,-8.012114,0.549211,3.922096,-7.305187,-8.291868,1.636490,-7.593970,-3.482048,1.905970,5.480541,-1.221709,4.364998,-9.245098,-8.906943,-2.881330,-9.433852,-7.708996,-8.025801,3.774505,3.991878,1.917701,-1.617293,-8.043362,2.029674,9.985459,0.493177,-5.266119,9.708950,-4.706356,-2.696931,-3.080740,3.854621,-1.146969,1.388225], dtype = "float32")#candidate|10854|(64,)|const|float32
call_10851 = relay.TupleGetItem(func_2501_call(relay.reshape(const_10852.astype('float32'), [11, 16, 12]), relay.reshape(var_10853.astype('float32'), [576,]), relay.reshape(const_10854.astype('float32'), [64,]), ), 4)
call_10855 = relay.TupleGetItem(func_2505_call(relay.reshape(const_10852.astype('float32'), [11, 16, 12]), relay.reshape(var_10853.astype('float32'), [576,]), relay.reshape(const_10854.astype('float32'), [64,]), ), 4)
output = relay.Tuple([bop_10845,call_10848,const_10849,call_10851,const_10852,var_10853,const_10854,])
output2 = relay.Tuple([bop_10845,call_10850,const_10849,call_10855,const_10852,var_10853,const_10854,])
func_10858 = relay.Function([var_10844,var_10853,], output)
mod['func_10858'] = func_10858
mod = relay.transform.InferType()(mod)
var_10859 = relay.var("var_10859", dtype = "int16", shape = (5, 14, 16))#candidate|10859|(5, 14, 16)|var|int16
var_10860 = relay.var("var_10860", dtype = "float32", shape = (576,))#candidate|10860|(576,)|var|float32
output = func_10858(var_10859,var_10860,)
func_10861 = relay.Function([var_10859,var_10860,], output)
mutated_mod['func_10861'] = func_10861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4207_call = mod.get_global_var('func_4207')
func_4209_call = mutated_mod.get_global_var('func_4209')
call_10879 = relay.TupleGetItem(func_4207_call(), 0)
call_10880 = relay.TupleGetItem(func_4209_call(), 0)
const_10891 = relay.const([[[6.143045,-4.189937,8.292314,1.041909,8.551133,-3.409779,-0.999093,-9.651115,-6.693727],[4.086106,-9.292682,1.825381,-4.067439,-1.550551,-1.646388,-2.921786,-1.868390,-7.924006],[-6.178153,-9.953920,-0.664315,0.040865,-1.370657,4.245378,3.646684,-9.878403,9.988979],[-0.879565,-2.690651,-7.776303,-6.048523,-0.617483,6.595084,3.359034,-9.641719,-3.394867],[-9.048757,5.455071,5.771705,2.579778,-3.159365,-8.328039,1.454180,4.199134,-0.088450],[3.706545,-9.638320,2.841239,-2.011633,-8.477696,-0.514216,1.464387,-3.510106,7.018827],[-0.221582,-5.523265,-6.598005,-0.179861,3.959276,3.553758,9.729209,-9.684673,6.737332],[-5.855390,-6.948568,-4.347096,7.420181,2.682485,9.970756,4.864386,6.197356,-9.090400]],[[7.507282,-8.987155,-5.074063,-0.213610,-4.909955,8.230653,-6.937983,0.918772,-9.147363],[9.095477,9.933717,1.218283,9.986149,-8.651426,-2.519256,-0.875584,-1.480312,-1.711128],[-2.439369,-2.073414,-8.448778,-3.447151,9.390058,9.538169,-8.836273,5.996016,-3.082316],[-0.853078,-5.773670,-0.411069,2.727916,-6.437631,0.719276,-9.474852,3.006285,-4.636966],[-2.603035,-7.513174,-5.103460,-4.674916,-2.575862,5.097580,-5.769598,-9.674737,-9.051921],[-0.037916,2.823685,6.038694,5.149866,-1.492540,9.881959,-0.466994,-9.842275,1.635189],[8.829673,4.097336,-0.520442,-5.712989,-5.327037,7.802376,3.401783,-6.841049,-0.812899],[-5.902633,9.643541,-6.631868,3.711952,-7.176764,1.488910,7.454618,7.488229,-6.345067]],[[1.135250,2.320388,7.815216,-4.357624,-3.822569,7.212359,3.122379,-1.533956,-5.639403],[6.747806,-9.027114,9.181147,0.189286,-5.504370,4.674115,-9.127380,3.169318,-8.452685],[-7.831817,6.727929,1.581670,8.979415,-4.450454,9.397714,-1.498528,1.060508,3.572553],[-1.851840,2.220882,7.190056,7.917953,9.139672,9.350330,8.122203,-6.890405,-6.333133],[3.743603,-5.476979,-2.293819,6.022881,-1.888032,3.017639,0.832238,7.165681,-5.944942],[-2.915455,-8.105951,-9.103297,8.124370,-3.646336,-8.156931,-7.620061,-9.895246,-8.723089],[-8.253350,-1.849991,-4.733523,-7.081394,4.291476,-6.036627,0.928858,-7.311194,-9.112402],[5.779141,-9.498507,6.250615,1.635658,5.081540,5.500946,-5.270308,1.329115,-2.989207]],[[-1.791937,6.886370,-4.642161,2.655934,-4.757954,-1.296502,-0.116126,5.998504,0.209916],[2.954070,-9.726727,-7.173545,-5.530820,5.772667,9.288590,0.222589,4.519899,-6.387313],[-0.005193,1.239599,9.920754,1.583718,1.889726,-6.602913,-7.177626,0.535915,-2.248069],[-9.192487,-1.007844,-0.635772,1.948200,9.189100,6.916913,1.918985,1.055912,-8.954846],[-0.431478,-9.731947,-7.963982,-2.798575,5.539862,8.419576,8.351336,-8.730513,-0.490321],[-1.699005,4.517983,-0.022377,5.380753,-6.943281,-9.937355,8.287848,2.742150,-7.886639],[-1.535503,-9.074049,3.546484,-2.488649,8.388597,-4.256523,8.524583,1.272178,2.569301],[3.655656,5.656969,7.308019,6.407562,-9.233156,7.846216,-0.918407,9.733191,2.389754]],[[8.588003,-8.583435,-4.373542,-7.526784,8.514046,-8.481884,6.488527,4.477609,-9.666080],[-5.996302,4.706618,-0.222366,8.660008,-0.466173,4.985329,9.983277,8.833561,8.500049],[7.898168,-0.238720,2.900300,4.799930,-4.578949,-4.224552,1.101464,-0.796966,9.570164],[0.678334,-3.389046,-5.834275,5.932614,-9.564830,3.236640,2.675288,4.141055,9.069533],[-9.476846,7.700288,2.079529,3.203723,-2.569897,5.681575,-2.900359,-3.930778,-7.751061],[-2.974633,7.590871,8.412002,-7.718787,4.302886,-9.727422,7.381386,5.673040,1.431370],[-1.092839,5.536957,1.288458,-3.832798,-5.070414,-1.898876,0.139780,-3.017968,7.747633],[0.994361,-7.863411,9.976920,7.735939,-3.009998,9.661213,0.372983,-8.447617,-7.504339]],[[8.574815,-8.337131,9.083066,0.345989,7.221528,7.053496,7.271860,4.928884,5.025037],[-7.109996,7.439186,7.950405,-5.314107,-1.817278,-5.655565,-8.290865,3.389954,4.903952],[7.924084,-4.116806,-3.539013,7.697535,-9.924418,-9.720497,3.389062,9.756352,4.556494],[9.123059,5.963987,-2.157054,-6.154448,-1.854867,3.434889,7.395125,-6.103817,-2.592114],[9.270593,-3.354669,-7.314153,-8.906898,2.160764,-2.471517,-6.851913,-0.345576,4.653459],[9.039423,-3.787934,9.223597,8.648957,-1.521277,-1.198069,3.048519,4.363027,-3.442613],[-8.779989,1.866048,-4.946863,-4.074767,-8.950978,-4.369968,3.923042,8.978471,2.043249],[-2.104941,9.569465,-0.779439,5.254135,-7.359748,7.841281,-9.347970,8.696099,4.813804]],[[7.849895,-8.444444,2.060392,1.662392,6.055947,-9.219466,4.779545,4.183580,8.065240],[0.050652,7.018644,7.527400,-0.668282,-8.576599,-1.975727,3.744268,8.242969,6.378304],[-9.165284,-3.139795,5.728299,3.771194,6.276803,-9.865188,-5.359756,2.294123,9.328967],[9.220059,-7.526387,4.643471,2.459528,-7.907293,-4.424875,1.818497,-9.529953,-4.799428],[-8.962952,-1.004764,0.074368,6.620771,-5.243090,0.841112,3.367703,6.492568,7.439636],[-0.474080,8.475845,0.740154,-3.506975,0.008097,-1.839903,0.663751,7.614196,-6.302136],[-6.488919,-4.420779,-8.101215,-1.708903,-8.017706,0.225537,-4.472740,1.871402,-3.028188],[8.712612,3.677281,1.371947,0.790152,5.923104,5.504538,4.602736,1.221139,-7.234928]],[[4.920089,5.381821,6.030352,1.143414,4.269592,4.301836,-8.231545,-6.599890,7.073005],[2.567033,-9.399340,6.688701,0.656492,8.674845,0.723679,-1.904640,-4.509287,-4.993470],[7.203658,5.414879,-0.254478,-0.282017,-4.882601,7.874744,9.360848,-3.104620,1.075242],[1.595724,-6.622024,6.679888,-8.251742,-5.971119,6.684373,-8.482251,7.014536,7.889934],[0.593142,-3.494430,4.555308,9.497009,-0.114340,-7.794034,-9.997463,-9.456646,7.751465],[-4.754406,-4.857127,-5.764463,6.445724,-8.914363,5.431627,9.134822,7.857500,-8.474259],[1.851971,1.999268,7.897022,7.264477,2.580831,-7.838928,0.869400,6.209706,2.224764],[5.311969,-2.831545,4.708789,-9.845605,-1.176544,-9.371139,-1.823932,1.960061,-5.337216]],[[0.499307,-8.636576,0.812213,0.724228,7.874620,-6.607356,6.125631,4.692685,4.599639],[3.727079,5.310579,-0.575631,-6.055703,0.863192,-8.310317,-2.372493,6.805438,5.385316],[0.029677,6.915316,9.208471,0.898672,-7.343067,-7.732393,-4.688047,5.639104,-5.918288],[2.586852,-1.311973,-9.609558,-7.462435,-4.675399,2.245700,3.929384,6.043844,9.715230],[-9.503374,6.752930,5.575944,7.092144,1.379873,-0.837217,-6.930557,-1.791124,-2.343486],[4.255070,0.568593,3.715335,9.244615,2.296680,0.662806,4.495670,7.659293,-9.550016],[6.448580,-2.110915,-4.623157,-4.841766,6.053791,7.779157,9.844650,-8.179285,6.542421],[7.890053,-7.940348,9.305773,2.746105,-3.057777,6.678824,0.222906,-5.471122,3.126544]],[[-1.193614,6.344176,-5.739197,-8.307204,6.220042,-7.841720,-1.522227,-8.443745,-6.397212],[-5.262028,-3.165448,-1.762292,-6.690351,-4.138917,-0.317650,0.948754,8.819886,-1.582202],[-0.676404,4.435601,5.963351,-5.423700,1.229364,5.201399,-0.450636,8.217213,-8.347201],[-7.125083,-3.152359,8.008811,-9.872820,6.626722,3.549914,8.727881,-2.638021,3.543352],[-2.908320,4.143825,-0.615902,6.359534,9.967884,-0.297904,-8.499807,-9.661777,8.742913],[2.257152,-3.408054,-2.129406,-3.947361,8.688856,-4.927908,6.194711,-4.747450,4.363924],[3.934403,1.303721,3.059205,-2.746678,-9.381131,-9.027423,-4.931725,1.090226,1.595644],[-3.357590,1.970903,-3.790940,-5.768670,-5.127279,4.334163,-8.276895,-9.129432,6.917212]],[[5.550862,-8.015830,-1.725436,2.905515,-3.372245,9.386008,-3.481619,-4.161115,-6.311036],[-3.030836,-5.496258,2.153064,-0.738784,-9.556238,-6.091344,-0.251447,7.755723,8.242473],[-6.104295,-6.662273,-8.187887,-3.767984,0.270963,-6.463487,6.579461,-0.043296,-4.388803],[3.713376,4.182383,8.716737,4.122007,2.885940,-5.357733,-3.119122,-3.583163,-5.282172],[6.969708,1.052167,7.722757,-4.403011,-1.907869,-9.156114,-3.746336,5.469183,7.456211],[2.095431,2.770776,5.142866,-0.877665,-6.391666,-1.158129,1.011572,4.987161,-6.054896],[-5.672452,2.604545,7.263439,8.619469,-5.307235,-9.227392,-3.366242,-8.933488,-6.307587],[2.746320,-4.819983,0.910164,-8.434834,-1.802918,-1.735661,-8.700342,4.528019,8.212415]],[[2.310437,-9.354651,-2.214927,8.476991,5.968761,-3.599441,8.946023,-1.230366,4.044500],[-0.397166,-7.154399,3.965183,5.119853,0.671485,4.462936,-1.046746,-3.455365,-1.109307],[0.208292,1.663299,-9.745297,-9.360117,5.811787,0.476456,8.972924,8.207762,-3.778504],[-5.093660,-1.378318,-7.723590,-7.457276,8.940234,8.968967,1.713878,5.823632,5.395016],[-2.873241,-0.083247,-7.759348,-7.993296,1.190138,6.730137,-2.029619,-7.131724,-1.910726],[0.645305,7.974064,0.790192,-8.134103,2.713018,1.586250,8.871583,-5.101050,5.332538],[1.362643,-4.779461,2.676519,-2.254197,7.881719,9.583242,5.280187,7.194139,1.800570],[-6.807547,4.280555,9.476830,-0.237685,9.096045,-9.340329,-7.925181,-0.334754,8.988016]]], dtype = "float32")#candidate|10891|(12, 8, 9)|const|float32
bop_10892 = relay.less(call_10879.astype('bool'), relay.reshape(const_10891.astype('bool'), relay.shape_of(call_10879))) # shape=(12, 8, 9)
bop_10895 = relay.less(call_10880.astype('bool'), relay.reshape(const_10891.astype('bool'), relay.shape_of(call_10880))) # shape=(12, 8, 9)
func_4015_call = mod.get_global_var('func_4015')
func_4019_call = mutated_mod.get_global_var('func_4019')
const_10901 = relay.const([9.116910,-7.099854,1.029554,4.347765,-1.283773,-5.973635,-7.600698,4.032780,-5.137207,1.774329,-8.368781,0.243259,-9.041914,8.209798,-8.104037,-6.658412,-2.298834,3.449254,6.164682,6.033830,-4.106057,-6.272685,-0.524454,-1.929247,6.720819,2.735198,-2.688069,7.413098,5.728837,6.139317,-3.221602,0.823523,-2.481986,-7.343033,0.187079,8.359493,-9.768050,-3.201758,7.631450,3.145057,7.993332,7.014139,-5.951386,-2.859330,8.142099,8.341515,3.334451,-2.299164,-3.438638,2.265203,-6.079788,5.803529,-9.239569,-4.688780,-8.432267,1.348813,-5.000755,2.323621,4.194293,-4.941096,3.045545,-0.177165,8.834806,-6.600455,-7.284832,0.579614,-8.360967,5.002696,9.557727,5.266893,4.024259,0.710680,6.639896,-5.571412,-8.043567,4.346132,8.482486,-6.532292,0.681637,-4.058278,9.506527,-1.418245,-0.359926,-5.566085,2.599475,0.107480,-0.745139,3.287821,2.455157,-2.029209,-4.573425,-7.577070,-7.089191,-0.920925,2.036510,4.244065,5.246487,9.650633,1.860583,3.950583,0.997463,0.832882,7.426595,0.923796,8.467856,-9.303941,4.455148,6.058490,7.930056,2.859139,-4.568835,0.701881,9.260569,3.399932,3.197390,9.318205,2.179050,-4.586750,3.870746,9.058381,-8.161349,7.419183,-1.204592,7.195683,-5.561777,8.659456,5.581948,-5.598230,3.757095,8.679881,-4.698837,0.922638,9.637720,-7.117814,0.086824,0.103132,2.283040,9.419035,7.561527,-9.637363,-5.981003,-1.147540,-3.996097,-7.556507,-1.576858,-4.130094,-4.191168,-6.064653,-1.028003,0.259397,4.616661,7.730906,2.697558,-6.182993,2.941156,-9.126724,-8.580753,6.072083,-6.875160,-5.562918,3.504136,6.824017,-6.967528,2.647716,4.321529,-1.436035,-3.158221,9.779718,0.267044,-9.256799,-2.042481,-9.931492,-7.762609,-5.956195,6.454047,2.904831,1.471352,-9.874164,1.132083,-1.724408,-6.224344,9.765799,-1.513725,-6.532305,-6.557845,-7.900156,-9.976036,-4.513043,-9.169439,9.097339,9.698329,-2.207914,0.209688,9.031649,2.678817,7.540121,-8.913805,-7.425869,-5.000905,-6.888435,6.390877,7.644587,3.691171,-2.090195,-0.241688,7.450356,5.804993,5.356225,4.002146,3.765980,-8.223079,-5.585239,6.586956,-7.856620,-0.289228,-8.405791,5.184088,7.831990,5.375610,2.791681,8.129521,-6.499713,-4.020126,7.905879,-1.736978,-2.533737,-3.294845,3.393872,4.632634,3.434269,8.775826,-5.892244,3.271188,4.205326,6.403120,7.841060,-7.895833,3.212355,6.735294,-2.019958,9.294531,-3.039819,7.308165,3.734739,9.370680,-5.856675,3.944549,-7.932219,-6.090541,0.202861,-9.898687,-1.166795,-2.207814,7.177170,9.999201,0.404289,9.051499,-6.893750,-9.517169,3.516359,-7.207052,-0.342900,-8.138045,-9.062433,-1.570067,8.833118,-9.221274,8.852632,0.058751,-5.296618,-6.187338,-3.860132,-7.447484,1.668593,-7.599257,-3.046320,-7.996994,-2.436137,8.530945,-8.523279,3.185455,-5.310095,1.865719,-4.118359,4.393525,7.975152,9.223589,5.814104,-0.299239,-6.098973,7.549722,1.531579,7.051048,7.961463,5.355244,-4.725916,2.280032,-0.293434,3.909634,3.747475,-2.120140,-8.001309,-8.204309,4.477585,-8.381674,-7.015685,-5.693889,-3.109706,6.046670,7.343948,2.285735,2.124896,-7.497851,9.847680,5.118149,-2.629359,-4.199313,4.849328,-4.428623,2.007931,-5.155207,2.264855,-3.615229,-3.356445,3.891422,-2.516929,0.860053,4.176029,8.477864,5.113992,4.086492,-4.650413,9.669104,4.725627,-1.932493,-3.191620,-9.688285,-0.781335,2.808654,-8.359430,-2.269181,1.609111,9.713059,6.782686,-0.392239,3.350994,2.291708,0.635553,1.188612,-2.993666,4.781848,-8.570005,-9.091963,-6.918395,4.755759,-7.126158,2.649155,6.080112,-8.503896,-3.521552,-7.937808,4.241343,0.811745,-0.332300,6.299294,9.491879,7.305767,-3.529512,-5.328708,-7.997372,6.765321,3.997916,-3.973033,4.031257,7.012668,9.226715,8.685397,7.249810,6.221875,6.482405,4.640053,-8.996297,-4.450708,-3.741213,9.271950,-7.074422,-7.226734,-0.264318,6.872771,3.183227,0.708728,-1.566575,0.531240,0.596842,7.435698,3.197825,0.656743,5.370812,-0.780111,-8.352395,-1.310653,3.412465,-8.863335,-3.073413,5.465068,1.533826,-0.576493,-7.868602,5.664466,1.221787,-0.452747,7.142239,-3.069724,-9.300878,3.268276,-5.862031,3.192091,-7.194015,7.171338,7.247541,-1.204308,1.035373,-9.316971,9.951186,-4.863404,-8.626336,9.517267,-5.941870,6.327098,2.709531,-2.154565,-8.619133,8.454219,8.396203,0.132163,4.992269,3.491962,4.466786,-4.862014,-0.243477,2.772671,-2.613836,-7.039484,-3.225983,7.155816,-0.900299,2.601059,3.752585,3.714389,-0.050932,-0.508350,8.871865,-4.013246,9.245114,9.407568,3.681370,3.789781,9.569228,8.569126,1.258982,0.978256,-4.690192,-6.111131,2.624379,-4.436632,7.463663,-4.402533,4.811988,0.507994,9.111754,-9.084859,2.417316,-5.532679,4.581387,-8.004055,-2.272695,3.694895,-4.598740,5.197468,5.670769,2.092650,-5.179329,3.247134,2.952179,-9.422894,8.460830,2.062035,-1.071026,-5.791393,8.627506,-9.044079,-2.764437,-4.444139,-7.432945,0.118408,-4.869437,-7.322871,-1.021645,-1.312054,-4.738182,-6.979145,4.415069,-4.836552,-4.022001,2.971250,0.122727,5.980767,8.189884,-2.541168,6.814566,-5.197000,1.775182,-7.338497,-1.032728,9.532029,-2.592195,1.644076,3.220021,3.140664,-8.584364,-6.734184,9.462372,6.985034,0.398302,-8.084942,8.349623,-3.117324,0.580674,-2.235603,2.483633,-2.754673,-2.253375,4.961017,8.940758,8.418352,-4.924307,0.613804,3.529655,-1.132711,-9.354424,-4.463130,5.812605,-8.020165,4.031733,4.762473,-1.537085,-3.069161,0.575441,0.664389,2.475901,-6.238574,-6.390928,5.264399,-9.165928,-1.857451,-8.809851,0.021963,-7.102633,-3.871808,-3.437313,-5.269485,7.023423,9.097930,9.175904,2.627076,6.020612,-9.772745,2.619763,-4.339042,5.679520,-9.547711,2.928687,-1.476298,-5.911404,6.193182,-3.009837], dtype = "float32")#candidate|10901|(576,)|const|float32
const_10902 = relay.const([8,5,6,-6,-2,9,-6,-9,8,5,-7,-10,4,-3,-6,2,-8,-1,-8,5,4,5,2,-6], dtype = "uint32")#candidate|10902|(24,)|const|uint32
const_10903 = relay.const([True,False,False,False,False,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False], dtype = "bool")#candidate|10903|(320,)|const|bool
call_10900 = relay.TupleGetItem(func_4015_call(relay.reshape(const_10901.astype('float32'), [576,]), relay.reshape(const_10902.astype('uint32'), [24, 1]), relay.reshape(const_10903.astype('bool'), [320,]), ), 1)
call_10904 = relay.TupleGetItem(func_4019_call(relay.reshape(const_10901.astype('float32'), [576,]), relay.reshape(const_10902.astype('uint32'), [24, 1]), relay.reshape(const_10903.astype('bool'), [320,]), ), 1)
output = relay.Tuple([bop_10892,call_10900,const_10901,const_10902,const_10903,])
output2 = relay.Tuple([bop_10895,call_10904,const_10901,const_10902,const_10903,])
func_10908 = relay.Function([], output)
mod['func_10908'] = func_10908
mod = relay.transform.InferType()(mod)
output = func_10908()
func_10909 = relay.Function([], output)
mutated_mod['func_10909'] = func_10909
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10942 = relay.var("var_10942", dtype = "float32", shape = (8, 11, 9))#candidate|10942|(8, 11, 9)|var|float32
uop_10943 = relay.log2(var_10942.astype('float32')) # shape=(8, 11, 9)
const_10946 = relay.const([[[5.477685,7.947140,2.220421,-6.888162,8.930194,9.978725,-3.340166,-0.143511,5.096344],[0.191280,-8.622534,-3.012679,-4.527350,7.688041,0.948476,-4.339461,1.451440,-8.981502],[0.169122,-5.253631,1.908872,8.629745,8.175748,-9.667069,-1.677011,-7.892494,0.800236],[2.298659,-7.964178,8.787024,0.591654,-3.558474,6.356869,2.743097,0.791549,4.592917],[-6.182931,8.765742,4.881027,-5.615180,6.092622,-7.125782,8.246172,-2.037851,-8.195154],[1.198340,1.909231,-1.233820,-6.572825,0.258141,2.147285,5.646015,-1.304863,-1.654154],[-2.674013,1.309260,7.097681,-5.009689,5.238841,-7.968344,-2.156120,4.537390,-7.670243],[-5.137639,-1.364279,-6.114989,9.520402,8.080872,-6.205128,4.421633,-2.085340,-1.866229],[-5.960538,8.770645,6.500043,7.872577,9.278091,8.597247,-9.749789,5.414687,-5.589679],[5.060849,9.726761,0.885498,-0.853823,-8.245974,2.292141,-0.902717,5.977891,6.938821],[8.781037,2.743872,5.453236,-3.273031,-5.794792,-9.696180,-6.939859,-7.965267,-4.330906]],[[6.712090,-5.775669,-7.749500,0.325713,9.557226,-3.664526,3.975054,7.537367,-3.014182],[-5.536829,1.475349,-8.862294,9.657855,2.143640,-0.982889,9.678205,-1.992449,6.087252],[9.805581,7.277308,-7.723123,7.943851,0.444922,-1.150342,4.618320,9.608635,1.378992],[3.420316,-1.913978,9.890779,-8.610443,-7.320965,-0.262402,2.448606,-4.146678,5.850557],[-1.290075,2.336953,0.422699,-7.593223,-9.370911,2.914925,7.507192,-9.638877,4.026001],[5.196931,-2.818194,-6.855915,2.470113,-0.843280,-3.828667,-5.421393,-8.512798,2.549928],[4.665460,-8.742252,3.908697,-3.145517,-0.398071,-1.905869,-7.296803,-6.075737,2.874006],[9.679964,-7.666656,9.763841,8.537760,-2.671108,2.757213,-6.903640,9.935672,-4.427740],[-7.859749,2.908032,9.623620,6.892658,2.234370,-0.735134,-9.316091,-6.904714,8.842910],[-0.685646,1.032579,-5.493886,-4.854554,-9.210389,8.376701,-1.163518,1.378108,1.779056],[1.428970,-9.816492,-9.850795,0.506616,-7.114049,0.701258,0.963701,1.334571,-5.564181]],[[4.248446,-3.450097,-7.035510,-2.030074,0.473515,2.914690,-9.221188,9.810806,3.269331],[8.228195,2.240458,-4.805583,2.830719,-1.411936,1.564206,-3.397507,3.343418,-6.685958],[6.707669,-6.926954,-1.886066,0.893607,-6.998524,3.691630,-8.410035,-1.315288,-7.151216],[-0.741030,0.899193,-4.562727,-6.797894,9.328901,1.085880,1.993741,4.407886,-2.687108],[2.381618,-6.372166,-3.641654,-4.198240,7.929679,-7.416776,1.144896,9.397620,5.521977],[3.618458,6.378715,0.384010,-5.473774,2.076291,-2.701460,7.913690,0.379657,3.109957],[8.217681,-1.799028,1.132138,2.442616,0.512975,3.638597,-1.103347,-4.246022,5.675281],[4.181740,1.731480,0.675444,-4.514639,2.060069,7.359028,4.268281,-4.129307,9.184139],[6.220519,6.714959,6.238041,0.661239,1.269633,4.791405,-2.236707,7.541423,4.395230],[2.813423,7.672905,8.714023,-1.673218,-6.101015,-0.888454,-0.159608,-9.912658,8.086736],[-1.845837,0.653905,-1.969427,-3.283572,2.570582,-1.326825,5.280309,-2.427644,2.446668]],[[3.221602,3.465845,-2.078650,6.384573,2.474808,-2.672338,7.966572,9.726423,2.129615],[-8.134107,-8.542906,7.407356,-9.001576,4.362426,5.334911,0.931454,-8.256992,-7.399460],[-8.252898,5.403802,4.944239,-5.656662,-7.535247,-1.397855,-8.490771,4.858780,-9.600196],[7.123239,0.963180,-4.940107,7.006394,3.557215,-6.627169,1.243432,7.347961,-0.260671],[-0.467228,-8.615309,-7.864005,-7.433844,7.496114,-7.909331,-7.917858,-1.103784,-4.277009],[9.200454,-1.273803,0.315294,-5.996828,-8.685680,5.306289,3.862095,0.774696,-9.221264],[-2.906040,-6.772954,-8.737494,0.306611,6.370092,9.673429,-7.984541,2.395910,4.996153],[5.836612,1.206686,-4.277945,-5.966119,6.935488,9.695520,-2.594591,-1.834720,8.478933],[4.482820,-7.439601,-7.107940,-9.727776,-8.174656,-1.888921,-1.817196,3.256801,3.237259],[-2.460361,7.061736,2.404816,9.627192,-7.189016,4.534238,-5.031894,4.040430,7.781893],[-6.789009,-9.822806,7.814050,3.855249,7.603882,-6.698140,-5.074095,-8.816539,-0.212989]],[[-2.473157,4.042190,0.390315,-1.633704,0.204648,-4.765649,7.610927,-0.377079,6.548014],[-9.902328,3.456669,-4.478199,-2.304154,-1.967010,-2.433229,4.663390,-2.710577,-5.824675],[7.080714,-7.938505,-3.818491,8.902469,4.691249,3.701898,1.948315,9.022744,2.745652],[-2.754850,-4.662736,4.451643,3.094676,2.645492,9.238931,-6.540753,-3.945820,-4.484234],[8.325031,2.428725,4.697982,-4.181738,-9.906283,-4.347199,5.029346,-9.201406,6.002199],[-6.837557,-3.082670,3.676002,1.045739,-7.583924,-9.570125,-8.703762,-8.878885,-5.315961],[9.393736,-0.925365,3.842520,7.427165,-6.258959,-0.726099,4.568658,-3.160804,5.639415],[-3.533521,4.611832,-1.918659,4.210287,-3.682276,-5.085025,0.345542,0.130816,-4.468177],[-5.845720,6.723158,9.500450,5.142776,-2.890497,-1.851719,0.016873,5.523513,4.476596],[-1.829193,-3.623861,-7.745218,5.581299,-5.155105,6.586124,8.747687,7.222293,-5.996529],[0.254939,5.234201,-0.856900,6.207218,-6.717660,-7.954929,-7.773791,-8.891239,6.902750]],[[-0.570897,6.211843,8.996308,7.763298,-6.886937,0.231529,0.276702,-8.532343,4.136635],[-9.622195,-8.293086,4.606695,-9.718671,6.403740,-4.231247,5.355683,-8.395201,-0.711449],[7.431800,-2.957793,-5.215745,9.454442,-5.633256,-9.253103,-6.041535,-7.557026,-7.497399],[7.847577,-1.258176,4.137572,-0.808261,6.444124,1.192578,-3.136472,3.348288,4.221611],[1.277226,5.614796,-6.738134,7.013832,-3.706446,-4.600116,3.841054,7.014227,-6.966141],[-4.894447,5.795480,9.837431,7.705100,9.721900,3.649668,-6.547601,4.147389,-4.215930],[-4.319614,-4.882552,-9.669889,2.080183,6.681030,2.907368,1.479500,-8.685401,9.113791],[-4.195547,4.120818,6.592008,-6.226846,6.638668,1.817907,6.800450,4.742231,-8.762195],[-9.587883,5.675250,-8.870233,-6.455237,8.512198,-3.669804,-2.080394,5.917351,-8.590430],[-2.363070,9.474095,3.913804,-1.613993,-2.537924,-3.923501,8.148829,-3.597950,-9.770208],[9.368011,-0.126539,7.908225,1.502719,1.446390,-7.259071,7.386881,-1.279671,-0.186210]],[[9.146389,9.288278,1.677114,-2.381592,-9.754024,6.455727,7.961145,3.133970,9.670309],[-8.260453,6.633950,-4.310398,5.280799,-9.101100,-1.681109,3.620070,0.739780,4.447292],[8.945404,9.855450,-9.357180,-3.135015,0.577644,0.780615,4.338462,6.921452,-8.632455],[-6.754999,2.258238,3.983322,4.422395,0.251611,9.352328,6.633435,-5.773274,5.821156],[-4.254218,-3.304706,6.536804,-4.305925,3.416669,4.756173,9.115649,-3.685368,4.603095],[-7.708025,-1.849294,1.449290,-9.588161,-4.111552,-3.183632,4.693195,-4.793758,-7.736730],[-1.816483,-8.513474,4.797813,3.086005,8.866755,9.217198,8.942515,7.183079,-5.416961],[-0.394360,-7.356428,3.208784,-1.467174,5.217775,4.049987,-5.561353,-2.490140,0.534972],[4.146500,0.985344,-4.175403,1.252789,-1.498979,-9.375673,1.919693,-9.437727,0.749288],[-6.038723,-9.204964,-5.778877,-8.434959,5.869391,9.349968,-4.959797,3.058946,0.443073],[-4.554835,-8.280333,-0.509962,3.571445,0.264179,9.597930,-2.427679,-3.122209,5.924071]],[[-2.371576,5.217485,-6.168256,-9.581532,8.748415,-1.137577,-4.927929,6.307024,-5.537995],[5.090989,-6.051176,3.518415,1.194962,3.720973,-9.422108,0.863058,-9.967237,9.579718],[0.300248,9.774790,9.034129,-1.361804,0.139883,-9.114546,7.891477,7.163615,-6.014030],[3.799174,-9.048219,3.594598,1.801245,9.071995,-0.547331,-0.418552,1.538857,-3.806145],[-4.854990,-9.048913,7.076381,6.070507,-7.846124,-0.208642,1.826163,-1.164014,-1.782105],[-0.548750,-8.679283,-5.084981,-0.044846,1.362984,-7.682263,8.746710,-8.616651,-7.326513],[-9.114464,-0.837972,3.632562,-2.443780,-6.705322,-6.374946,-1.899041,-4.568388,7.245372],[5.402484,9.752872,8.297157,7.928593,-9.133154,-0.098435,9.617282,-1.593106,4.782840],[-9.509689,-5.104872,-1.735762,0.295769,-1.724656,-0.586854,-7.817348,1.010412,-6.482696],[-7.138706,7.675752,1.106322,4.226212,8.248130,-2.134666,9.878987,-9.793312,1.437795],[8.714574,5.388756,-1.948921,6.871624,-2.067278,-8.979102,0.546277,-6.956692,-2.673374]]], dtype = "float32")#candidate|10946|(8, 11, 9)|const|float32
bop_10947 = relay.logical_xor(uop_10943.astype('uint32'), relay.reshape(const_10946.astype('uint32'), relay.shape_of(uop_10943))) # shape=(8, 11, 9)
output = relay.Tuple([bop_10947,])
output2 = relay.Tuple([bop_10947,])
func_10963 = relay.Function([var_10942,], output)
mod['func_10963'] = func_10963
mod = relay.transform.InferType()(mod)
mutated_mod['func_10963'] = func_10963
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10964 = relay.var("var_10964", dtype = "float32", shape = (8, 11, 9))#candidate|10964|(8, 11, 9)|var|float32
func_10963_call = mutated_mod.get_global_var('func_10963')
call_10965 = func_10963_call(var_10964)
output = call_10965
func_10966 = relay.Function([var_10964], output)
mutated_mod['func_10966'] = func_10966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8633_call = mod.get_global_var('func_8633')
func_8634_call = mutated_mod.get_global_var('func_8634')
call_10988 = relay.TupleGetItem(func_8633_call(), 0)
call_10989 = relay.TupleGetItem(func_8634_call(), 0)
func_4330_call = mod.get_global_var('func_4330')
func_4336_call = mutated_mod.get_global_var('func_4336')
const_10999 = relay.const([-5.984287,6.881118,-7.337069,6.589691,-4.985978,1.990219,-3.194301,9.564796,-5.332939,-2.792354,-5.242787,-4.226168,7.329425,8.559729,1.074725,1.198151,-8.917231,-8.984012,-7.310711,6.436075,8.668166,-4.977822,7.705427,-6.483429,7.520503,2.502740,-0.300904,-8.260377,0.903217,-6.958600,8.673335,-6.720459,-9.972393,-7.012256,-0.857787,-0.791600,-3.835072,2.347172,-8.875054,5.149750,-2.766552,0.514571,-0.823444,3.405378,4.691918,-7.216960,5.678542,-7.425137,7.191608,-5.163498,-3.686042,-5.831648,1.690926,-7.684645,6.680082,2.232830,0.875292,-9.600618,-2.823707,0.870524,-9.074097,-4.109227,4.743096,2.786552,7.887463,-4.997300,-1.341149,-8.394954,7.772223,3.979858,1.858923,-1.677612,3.305069,-8.054636,-8.554873,3.252831,-8.801215,-3.204725,-0.346965,-6.701601,0.739832,2.575274,1.073736,-7.568028,5.670451,9.893081,-3.825350,4.098492,6.982983,-3.906854,5.336128,-0.322421,5.721975,6.898537,-1.322378,-6.601490,2.739164,-0.119019,4.496596,4.911384,-8.084884,8.589267,-2.897227,5.232109,9.021220,-7.294170,8.009338,-5.105482,0.374644,3.784531,1.017682,-8.975587,6.554304,-1.426604,5.733340,9.415564,-4.655464,-2.188737,1.519927,-0.375140,4.741635,-0.401658,3.818878,-9.009665,-4.373263,5.154902,5.487035,-5.333670,-7.834578,4.522595,-9.764698,6.777805,-5.270916,-7.557125,4.604744,-6.484857,9.427402,-3.132229,9.589550,5.084901,-7.071012,0.517388,-6.481511,-1.726922,-5.896222,-7.167490,1.830126,-1.635017,-0.734443,3.131715,5.444172,-8.555891,-9.281329,-9.974890,6.926803,-9.304707,-0.903990,3.038917,5.336213,6.880900,-2.852897,1.048770,2.551425,5.693093,-0.647208,-0.335798,-3.297290,-4.950445,1.456660,-5.559476,-3.326151,-6.145214,-7.698975,-4.732319,9.046778,-2.249258,3.461090,8.742987,7.900389,-5.914018,-8.122599,6.168747,-4.016923,5.352682,-8.137768,-5.990454,-2.119785,1.539440,9.312235,7.948452,4.758309,-4.066856,8.685932,-6.834079,-8.706883,-6.688649,9.992342,4.916652,1.086672,6.507273,-6.846015,-2.420464,-8.050868,1.565887,3.172087,-4.128402,-1.725320,-7.064316,7.429377,-9.700613,4.269910,-1.438250,6.574491,-1.224843,-4.173366,-1.020115,-1.602871,-8.305711,1.994978,-2.124486,-1.267354,3.356947,1.842325,-6.728612,-6.138626,-3.535536,6.202493,-8.134176,-3.461675,8.673981,-1.917485,7.313943,-9.874836,0.890927,4.377797,5.150741,6.935308,7.411454,-9.786768,8.782750,-5.488898,-7.143943,-1.724375,-3.745126,-0.638070,6.975771,-6.267141,4.784220,-6.322946,-1.909146,-5.910455,4.880655,-1.681529,-8.482849,-9.173376,-5.300543,7.522783,-8.322253,6.649787,-7.363466,-7.429618,5.155189,-5.554835,-7.626591,8.558693,-4.000506,-7.732486,7.370051,-5.979845,9.956180,9.071879,-4.036073,-4.051784,-2.413364,8.280955,0.300454,3.670080,-7.405557,6.596410,-4.213086,8.676162,-6.733753,6.447852,4.680874,1.704042,-4.175557,-7.547617,7.993776,-7.346200,-8.524689,-1.622979,9.685254,-9.070897,9.995130,-5.450064,5.431781,7.107226,9.783411,8.359218,-2.301731,2.132843,-7.416927,6.066276,9.683946,5.006458,-9.148072,0.636039,8.863948,9.355508,-3.370541,6.629587,-2.867132,9.673121,7.318524,-7.353747,-5.485036,-7.268508,6.077142,-6.309546,6.934994,-1.171821,-3.240768,-0.448316,-2.417371,-0.768451,6.436446,-6.987570,-6.105917,-0.477960,-8.870919,-3.777270,-9.430114,2.826264,-1.100159,-7.121979,-3.858357,5.048698,9.878470,-9.875978,-6.910045,-3.407249,-0.837214,0.259994,-2.964076,-6.503139,-0.462290,3.437543,-5.873417,-4.525507,9.246391,-2.830498,0.051078,-0.653803,0.694034,-2.175839,0.495799,-8.538697,6.246728,6.423777,1.329389,4.567971,-2.351212,-3.487744,2.742492,3.003211,-1.830452,-6.321839,-2.581232,-1.176728,-4.170446,2.857767,5.977803,8.250600,9.784723,-2.223129,6.088034,-0.093140,7.728420,-4.141120,3.530164,1.500940,1.885355,9.795655,-3.263836,-8.650976,5.807938,-0.584146,9.497916,5.378616,-2.259548,7.073458,9.404207,4.405903,-8.657633,-2.637002,-5.105002,4.895425,4.254948,0.041230,-9.975061,-5.494792,8.407623,-1.211593,0.746814,6.578444,-3.767355,8.532824,-2.539063,-7.311009,-0.419754,-6.040575,-4.115407,-7.043921,-3.679205,6.815980,1.900153,-5.224680,-2.517396,6.379843,0.015778,-6.533695,0.632336,5.710881,-3.227884,5.872704,-9.031655,0.672478,8.674725,2.943518,1.352474,7.471103,-7.807785,3.826831,-0.717249,-1.292716,6.396091,9.711409,-3.271465,-9.891480,-1.747405,7.251249,3.903155,3.130442,7.513562,6.922989,8.580686,0.480156,-4.391880,9.594544,-2.034318,-2.841741,-0.251035,-9.919573,0.162863,7.210122,-1.484231,-3.392136,-8.017789,6.818206,-5.330860,-6.957798,4.239690,-9.456748,1.601507,-1.348585,9.117251,2.209556,1.308212,9.281218,5.372330,-3.959899,9.560419,2.523126,5.841771,5.003789,6.580585,1.770157,-7.475617,2.473474,9.545790,0.517222,-0.174992,-3.483531,-6.152745,-9.778827,3.138140,-7.044603,-9.380192,-2.488178,-4.896848,2.401596,1.712338,-6.270194,-0.113577,2.805205,4.269912,3.129634,-6.911159,4.890639,3.996808,-8.419929,3.692203,5.652240,-9.874123,5.939998,-5.191608,9.163335,7.271349,6.420393,1.839822,-2.201389,4.760399,-8.584557,3.294566,-3.392491,-6.400482,8.947908,5.136367,8.158533,-8.852838,-5.942714,3.064134,1.533383,3.966575,8.198474,3.854303,-1.604347,4.391820,-7.725743,-9.650196,4.043567,0.405159,-1.812587,8.941717,4.994294,-1.497959,-0.821026,3.086946,7.873429,-3.026175,6.406792,-9.602266,-2.778283,-6.274765,-4.696925,-9.763459,1.155857,6.166761,-0.864174,7.875041,-9.383126,-7.989914,-8.541896,-8.657617,-0.940324,-7.901749,1.790966,4.350280,-7.029754,-7.568161,6.617802,-0.414817,6.607256,-6.477980,-7.210109,5.474747,-8.195528,-8.613450,5.823965,-6.604568,8.065207,2.707479,5.405582,1.902475,-1.752447,-5.781367], dtype = "float32")#candidate|10999|(576,)|const|float32
var_11000 = relay.var("var_11000", dtype = "uint32", shape = (24,))#candidate|11000|(24,)|var|uint32
var_11001 = relay.var("var_11001", dtype = "uint32", shape = (384,))#candidate|11001|(384,)|var|uint32
const_11002 = relay.const([[True,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True],[True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True]], dtype = "bool")#candidate|11002|(2, 160)|const|bool
call_10998 = relay.TupleGetItem(func_4330_call(relay.reshape(const_10999.astype('float32'), [576,]), relay.reshape(var_11000.astype('uint32'), [24,]), relay.reshape(var_11001.astype('uint32'), [384, 1]), relay.reshape(const_11002.astype('bool'), [8, 40]), ), 2)
call_11003 = relay.TupleGetItem(func_4336_call(relay.reshape(const_10999.astype('float32'), [576,]), relay.reshape(var_11000.astype('uint32'), [24,]), relay.reshape(var_11001.astype('uint32'), [384, 1]), relay.reshape(const_11002.astype('bool'), [8, 40]), ), 2)
func_4774_call = mod.get_global_var('func_4774')
func_4777_call = mutated_mod.get_global_var('func_4777')
const_11005 = relay.const([[3.519659,3.026106,5.839752,7.657236,-5.808363,4.550203,1.795109,4.840438,7.772959,2.104064,9.492627,9.850413,-9.447279,1.264751,1.723085,8.976576],[-0.168904,9.268762,9.441153,-8.079092,4.635494,-3.559570,6.869052,8.913392,2.073449,2.990951,5.787647,-7.045612,6.841195,-3.806409,-0.837431,7.496416],[-5.390781,-9.612583,-8.584363,8.953782,-2.564699,-0.886895,-5.231390,-5.657145,-9.728947,-3.500377,-5.551235,-2.366302,-0.222668,1.967065,-3.737727,6.979129],[6.622043,-1.794388,7.163298,8.888660,8.537272,8.090852,7.378011,6.800772,-0.597919,2.292165,6.142871,-6.785180,-2.219657,-4.709452,8.918564,-6.946572]], dtype = "float32")#candidate|11005|(4, 16)|const|float32
call_11004 = relay.TupleGetItem(func_4774_call(relay.reshape(const_11005.astype('float32'), [64,])), 3)
call_11006 = relay.TupleGetItem(func_4777_call(relay.reshape(const_11005.astype('float32'), [64,])), 3)
func_5544_call = mod.get_global_var('func_5544')
func_5545_call = mutated_mod.get_global_var('func_5545')
call_11007 = relay.TupleGetItem(func_5544_call(), 1)
call_11008 = relay.TupleGetItem(func_5545_call(), 1)
func_9190_call = mod.get_global_var('func_9190')
func_9192_call = mutated_mod.get_global_var('func_9192')
call_11014 = relay.TupleGetItem(func_9190_call(relay.reshape(call_10998.astype('float32'), [36, 16])), 3)
call_11015 = relay.TupleGetItem(func_9192_call(relay.reshape(call_10998.astype('float32'), [36, 16])), 3)
func_9035_call = mod.get_global_var('func_9035')
func_9036_call = mutated_mod.get_global_var('func_9036')
call_11029 = func_9035_call()
call_11030 = func_9035_call()
output = relay.Tuple([call_10988,call_10998,const_10999,var_11000,var_11001,const_11002,call_11004,const_11005,call_11007,call_11014,call_11029,])
output2 = relay.Tuple([call_10989,call_11003,const_10999,var_11000,var_11001,const_11002,call_11006,const_11005,call_11008,call_11015,call_11030,])
func_11037 = relay.Function([var_11000,var_11001,], output)
mod['func_11037'] = func_11037
mod = relay.transform.InferType()(mod)
mutated_mod['func_11037'] = func_11037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11037_call = mutated_mod.get_global_var('func_11037')
var_11039 = relay.var("var_11039", dtype = "uint32", shape = (24,))#candidate|11039|(24,)|var|uint32
var_11040 = relay.var("var_11040", dtype = "uint32", shape = (384,))#candidate|11040|(384,)|var|uint32
call_11038 = func_11037_call(var_11039,var_11040,)
output = call_11038
func_11041 = relay.Function([var_11039,var_11040,], output)
mutated_mod['func_11041'] = func_11041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3919_call = mod.get_global_var('func_3919')
func_3921_call = mutated_mod.get_global_var('func_3921')
call_11061 = func_3919_call()
call_11062 = func_3919_call()
func_2261_call = mod.get_global_var('func_2261')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_11076 = relay.TupleGetItem(func_2261_call(relay.reshape(call_11061.astype('float64'), [3, 16, 6])), 1)
call_11077 = relay.TupleGetItem(func_2264_call(relay.reshape(call_11061.astype('float64'), [3, 16, 6])), 1)
output = relay.Tuple([call_11061,call_11076,])
output2 = relay.Tuple([call_11062,call_11077,])
func_11082 = relay.Function([], output)
mod['func_11082'] = func_11082
mod = relay.transform.InferType()(mod)
mutated_mod['func_11082'] = func_11082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11082_call = mutated_mod.get_global_var('func_11082')
call_11083 = func_11082_call()
output = call_11083
func_11084 = relay.Function([], output)
mutated_mod['func_11084'] = func_11084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6774_call = mod.get_global_var('func_6774')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_11085 = relay.TupleGetItem(func_6774_call(), 0)
call_11086 = relay.TupleGetItem(func_6775_call(), 0)
output = call_11085
output2 = call_11086
func_11094 = relay.Function([], output)
mod['func_11094'] = func_11094
mod = relay.transform.InferType()(mod)
mutated_mod['func_11094'] = func_11094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11094_call = mutated_mod.get_global_var('func_11094')
call_11095 = func_11094_call()
output = call_11095
func_11096 = relay.Function([], output)
mutated_mod['func_11096'] = func_11096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4421_call = mod.get_global_var('func_4421')
func_4423_call = mutated_mod.get_global_var('func_4423')
call_11097 = relay.TupleGetItem(func_4421_call(), 0)
call_11098 = relay.TupleGetItem(func_4423_call(), 0)
output = relay.Tuple([call_11097,])
output2 = relay.Tuple([call_11098,])
func_11100 = relay.Function([], output)
mod['func_11100'] = func_11100
mod = relay.transform.InferType()(mod)
mutated_mod['func_11100'] = func_11100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11100_call = mutated_mod.get_global_var('func_11100')
call_11101 = func_11100_call()
output = call_11101
func_11102 = relay.Function([], output)
mutated_mod['func_11102'] = func_11102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4490_call = mod.get_global_var('func_4490')
func_4492_call = mutated_mod.get_global_var('func_4492')
call_11173 = relay.TupleGetItem(func_4490_call(), 1)
call_11174 = relay.TupleGetItem(func_4492_call(), 1)
func_5884_call = mod.get_global_var('func_5884')
func_5887_call = mutated_mod.get_global_var('func_5887')
var_11190 = relay.var("var_11190", dtype = "float32", shape = (576,))#candidate|11190|(576,)|var|float32
call_11189 = relay.TupleGetItem(func_5884_call(relay.reshape(var_11190.astype('float32'), [576,])), 3)
call_11191 = relay.TupleGetItem(func_5887_call(relay.reshape(var_11190.astype('float32'), [576,])), 3)
var_11198 = relay.var("var_11198", dtype = "float32", shape = (12, 8, 9))#candidate|11198|(12, 8, 9)|var|float32
bop_11199 = relay.bitwise_or(call_11173.astype('int8'), relay.reshape(var_11198.astype('int8'), relay.shape_of(call_11173))) # shape=(12, 8, 9)
bop_11202 = relay.bitwise_or(call_11174.astype('int8'), relay.reshape(var_11198.astype('int8'), relay.shape_of(call_11174))) # shape=(12, 8, 9)
func_4543_call = mod.get_global_var('func_4543')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_11228 = func_4543_call()
call_11229 = func_4543_call()
func_10338_call = mod.get_global_var('func_10338')
func_10342_call = mutated_mod.get_global_var('func_10342')
const_11235 = relay.const([-1,-2,-3,3,-1,-8,-5,-10,6,-1,-5,4,6,-5,9,9,-10,-4,-3,2,5,6,-6,10,10,-6,-10,4,2,-1,7,2,10,-4,-5,8,-8,-2,3,-8,-3,7,5,-3,3,9,-3,-1,6,-9,4,1,-4,-8,-4,9,1,3,1,4,-10,-6,-5,-8,-4,2,-4,10,7,-6,-2,-10,-3,10,1,-8,8,-3,-4,-2,6,4,8,-10,2,7,1,9,-10,-7,-1,-1,-10,-2,3,-3,-9,-1,-3,-3,6,-8,-9,10,6,-2,2,-7,-8,-7,2,-2,-6,-9,5,-3,4,-8,8,2,-5,10,8,10,-6,-6,8,9,-2,-3,10,8,9,7,-5,-3,5,-8,3,-6,-6,7,-10,-7,7,-9,-8,-3,6,4,10,10,1,8,-5,-2,9,-2,-6,-3,-1,-1,1,3,3,7,-5,9,-6,-9,-1,1,-10,1,3,10,6,10,3,-5,1,2,-2,1,9,-8,-10,-2,-3,6,-5,-8,8,-10,-3,1,-8,9,5,-7,-1,5,-5,2,10,-4,4,5,3,-5,10,-10,9,8,1,-8,-4,2,2,9,-1,6,-6,1,8,-4,4,-7,-3,-8,-2,-7,-1,-6,-4,-4,8,4,3,-3,-1,-9,3,7,3,-4,-2,-3,-1,-8,6,2,2,-9,-9,-5,-3,5,-10,-4,10,10,-9,6,4,5,-4,3,2,2,-8,4,-3,7,-3,-6,1,4,-9,-1,4,2,-4,-7,-8,-8,6,-8,-10,2,-10,-6,-6,-2,-3,-7,-1,-7,3,9,-1,-10,8,-7,2,2,10,2,8,-3,7,8,-1,2,6,-7,-10,-7,-2,-7,-8,8,-6,-5,4,-5,-8,-10,-7,2,6,4,6,-2,-8,7,-9,3,5,10,-6,4,-10,-4,9,-2,-7,10,-8,6,-3,-1,5,-8,1,-2,2,4,10,-1,-6,-5,9,-10,8,-2,-6,5,-6,4,10,-8,-1,6,-2,2,10,-3,-1,-6,9,-1,-1,-8], dtype = "uint32")#candidate|11235|(384,)|const|uint32
const_11236 = relay.const([-0.965158,2.020202,7.749854,-7.858574,-5.311500,-0.615929,7.724999,4.647006,-3.080538,-7.001686,5.869415,3.884417,3.647899,-7.871901,1.536827,9.923397,9.451575,2.289573,-6.858208,-6.772910,-8.415764,-1.509959,5.903975,1.620971,-3.015080,7.651057,-0.426355,2.869359,-4.865910,-1.251117,-7.322887,-0.885683,-9.753692,-0.245605,9.130043,2.809621,1.061509,4.460303,-4.176282,-7.018853,-5.697314,-4.105301,0.141171,-2.373088,4.247144,8.757249,-9.086296,2.815582,-4.884060,-1.611447,7.636657,0.442568,8.634110,9.980753,2.956954,-8.061047,0.193608,-2.091180,0.119694,-3.277705,-0.681648,-7.259193,3.897001,6.263067,3.201011,6.628150,-4.115527,-8.948576,3.651570,4.461442,8.075428,4.678728,-0.257516,7.455204,-2.949347,-9.147169,-1.927106,-5.589545,-0.932892,3.642870,8.440383,-9.400897,8.635386,1.005143,-0.554077,-0.711233,6.590021,-6.335067,9.654180,7.263670,-1.998091,-0.150241,-2.954788,-0.732754,7.299755,-0.858320,7.887438,-1.522341,5.667271,9.211774,-8.081417,-7.820636,3.924096,9.676832,-6.686781,9.492167,-7.573114,3.507589,-2.288776,5.100862,6.648298,-5.950618,3.035427,-7.136218,-3.578294,-0.736177,2.323199,-5.868830,-3.640645,8.520568,-4.255284,7.489181,4.058136,4.769788,-3.501975,9.765870,0.187260,-7.255952,-8.911251,2.149943,3.084898,5.273589,-0.406707,0.091612,1.020599,-9.286268,3.047037,-5.677688,-1.254706,-6.435775,-3.214922,7.766645,0.326066,-8.033748,-8.701617,8.538179,-8.896299,-8.387103,-1.016570,0.284460,-3.527833,-2.469708,1.937332,-8.230792,-2.068239,-7.663603,-6.716677,-7.506698,-0.834240,3.032714,9.573682,-5.315897,3.784315,-0.388078,-3.156155,3.514804,9.292343,1.630561,-8.481947,7.297782,-3.353374,-2.731737,0.019035,8.062273,8.909567,-0.854001,3.176075,-8.026383,2.440557,-5.373569,-7.629101,-3.592189,6.795767,-5.061670,-8.046866,7.139075,-6.915629,9.252893,-6.748919,4.054430,-2.552996,-1.125117,-9.227300,-6.267356,-4.990758,0.942616,8.744857,-1.286303,3.324550,-4.743700,-9.449967,4.100014,9.700148,-9.988846,7.799271,-3.928693,4.285151,4.541139,9.138644,8.109641,-0.298735,7.982218,7.132389,2.834853,-8.002970,-1.961986,4.702979,3.771943,-5.437268,-0.144173,9.827915,2.384527,-3.540168,-7.775862,1.338480,2.137745,7.374091,6.478559,-2.118375,7.648893,-6.348758,-0.468757,5.439559,7.439056,4.976258,5.576103,-7.564646,-3.886161,5.134995,-1.384799,-7.298436,5.816399,-0.457509,-4.161816,4.728878,-6.766257,8.214965,2.991496,-9.978483,4.326784,-7.812090,5.605114,2.704253,1.111556,-8.842514,5.607224,1.333426,-2.975096,9.968377,7.446881,3.360963,6.077166,-6.533464,3.606435,0.903878,-7.738021,-8.967887,-9.667501,1.112153,-5.509117,7.503264,9.098964,-8.305102,9.918177,-1.225214,-7.988651,-7.398811,2.764277,-4.382159,1.414420,3.729913,-8.837919,7.361921,7.832075,-3.653697,5.583441,-1.048820,7.394572,-1.766917,-2.985266,4.626413,-6.106200,-7.835710,-6.359765,3.883113,-2.686035,0.663402,-0.718772,9.803959,-5.491571,0.128333,-6.900607,-8.954788,1.186090,-5.215570,1.701365,-1.425897,6.343491,7.538904,-1.508921,3.797746,5.116739,3.306873,-8.786686,-0.247932,-4.793391,-2.854683,5.660351,-8.077833,5.512323], dtype = "float32")#candidate|11236|(320,)|const|float32
call_11234 = relay.TupleGetItem(func_10338_call(relay.reshape(const_11235.astype('uint32'), [384,]), relay.reshape(const_11236.astype('float32'), [2, 160]), ), 8)
call_11237 = relay.TupleGetItem(func_10342_call(relay.reshape(const_11235.astype('uint32'), [384,]), relay.reshape(const_11236.astype('float32'), [2, 160]), ), 8)
func_2099_call = mod.get_global_var('func_2099')
func_2102_call = mutated_mod.get_global_var('func_2102')
const_11260 = relay.const([4,3,-9,-7,-7,3,-4,3,9,-9,-5,-3,4,10,10,6,-1,10,-1,2,7,-8,-2,-5,9,5,8,-10,-1,-6,2,-5,-10,-4,-9,-1,-2,9,1,5,10,3,10,-10,4,2,-7,-8,9,2,-8,6,3,4,-1,-6,-8,9,-4,9,-7,1,-7,3,-1,-5,9,1,-9,7,-3,-1,4,9,8,-4,-10,-9,6,-2,-8,-7,10,-10,-2,-9,10,6,-9,-1,-4,4,-2,10,8,6,-10,-4,3,-9,8,2,9,3,-2,7,-9,-9,-3,-8,10,6,9,10,3,-6,7,-1,5,-6,-8,4,-3,6,-3,-6,8,-3,-3,6,-2,9], dtype = "int16")#candidate|11260|(132,)|const|int16
call_11259 = relay.TupleGetItem(func_2099_call(relay.reshape(call_11234.astype('float32'), [3, 16, 6]), relay.reshape(const_11260.astype('int16'), [132,]), ), 2)
call_11261 = relay.TupleGetItem(func_2102_call(relay.reshape(call_11234.astype('float32'), [3, 16, 6]), relay.reshape(const_11260.astype('int16'), [132,]), ), 2)
func_3461_call = mod.get_global_var('func_3461')
func_3463_call = mutated_mod.get_global_var('func_3463')
call_11264 = relay.TupleGetItem(func_3461_call(), 2)
call_11265 = relay.TupleGetItem(func_3463_call(), 2)
output = relay.Tuple([call_11189,var_11190,bop_11199,call_11228,call_11234,const_11235,const_11236,call_11259,const_11260,call_11264,])
output2 = relay.Tuple([call_11191,var_11190,bop_11202,call_11229,call_11237,const_11235,const_11236,call_11261,const_11260,call_11265,])
func_11274 = relay.Function([var_11190,var_11198,], output)
mod['func_11274'] = func_11274
mod = relay.transform.InferType()(mod)
mutated_mod['func_11274'] = func_11274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11274_call = mutated_mod.get_global_var('func_11274')
var_11276 = relay.var("var_11276", dtype = "float32", shape = (576,))#candidate|11276|(576,)|var|float32
var_11277 = relay.var("var_11277", dtype = "float32", shape = (12, 8, 9))#candidate|11277|(12, 8, 9)|var|float32
call_11275 = func_11274_call(var_11276,var_11277,)
output = call_11275
func_11278 = relay.Function([var_11276,var_11277,], output)
mutated_mod['func_11278'] = func_11278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2689_call = mod.get_global_var('func_2689')
func_2691_call = mutated_mod.get_global_var('func_2691')
call_11313 = relay.TupleGetItem(func_2689_call(), 2)
call_11314 = relay.TupleGetItem(func_2691_call(), 2)
func_1867_call = mod.get_global_var('func_1867')
func_1869_call = mutated_mod.get_global_var('func_1869')
const_11325 = relay.const([9,-9,5,-3,8,-4,7,9,9,10,-8,4,10,7,2,-5,3,1,3,3,-9,-4,-1,6,9,-7,6,7,5,-5,-9,10,-4,10,-7,1,-1,2,7,9,-5,5,10,-9,-7,4,5,-7,-8,-8,-9,-1,-3,-2,3,6,-10,1,-6,-8,5,10,7,10,-4,8,-7,-6,2,-9,-1,-4,8,4,-6,-1,-4,10,8,-7,-6,8,6,2,-3,-6,7,-9,5,-3,6,1,-2,-3,9,-5,-9,-8,8,-4,4,9,-9,-8,-2,5,-4,-9,-5,9,4,-9,-6,7,-9,-6,2,4,-4,6,-5,5,5,-8,-8,-6,-10,5,-2,-3,-7,3], dtype = "int16")#candidate|11325|(132,)|const|int16
call_11324 = relay.TupleGetItem(func_1867_call(relay.reshape(const_11325.astype('int16'), [11, 4, 3])), 0)
call_11326 = relay.TupleGetItem(func_1869_call(relay.reshape(const_11325.astype('int16'), [11, 4, 3])), 0)
output = relay.Tuple([call_11313,call_11324,const_11325,])
output2 = relay.Tuple([call_11314,call_11326,const_11325,])
func_11327 = relay.Function([], output)
mod['func_11327'] = func_11327
mod = relay.transform.InferType()(mod)
mutated_mod['func_11327'] = func_11327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11327_call = mutated_mod.get_global_var('func_11327')
call_11328 = func_11327_call()
output = call_11328
func_11329 = relay.Function([], output)
mutated_mod['func_11329'] = func_11329
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11345 = relay.const([[[6.275016,6.446711,-2.158001,-7.071381,5.098691,2.107579,8.520105,-3.991800,-5.129319,-8.236421,2.903708,7.141885,-3.383303],[-7.285067,4.418163,4.176122,6.854612,-9.844552,1.710869,-4.183295,-3.913276,-8.136055,7.393138,-0.902664,1.204255,7.114472],[-6.819131,-6.936026,8.568737,-7.755938,-6.715962,-9.899529,1.569877,-4.445232,4.540723,0.659875,-2.077757,6.623496,-6.136185]],[[4.280098,-9.239562,-4.513127,3.032201,2.403329,1.652466,0.256259,-5.126747,2.919644,-1.443036,-8.461897,-4.098531,-4.287780],[-0.405794,-7.877325,2.559092,-0.532463,2.006531,-4.670593,3.008961,9.720727,-2.939299,0.069026,-6.175720,-8.254644,-7.245959],[-3.688164,-0.598534,6.558143,9.487074,7.829523,1.965871,-8.460532,-9.594261,3.015412,1.880049,-5.563857,5.657005,-2.792095]],[[7.901688,5.934498,6.234110,-1.470581,-3.784181,-5.235854,-3.396459,-0.987062,-9.391949,-9.877426,-8.658252,-0.569839,-2.748427],[3.851021,-6.517101,-5.808356,-9.616302,3.844745,2.243028,7.436891,2.901848,6.724577,2.904652,6.909051,5.504868,-9.196763],[6.988940,8.574282,6.051403,-4.056582,-0.055494,4.786259,-3.917379,-0.642880,6.847814,9.251732,-1.312046,-6.607170,-2.553185]],[[2.419159,4.241266,7.045362,-4.185745,-1.515684,5.539036,-5.744738,0.110152,-1.285869,-7.683536,-7.513053,-4.629869,4.096221],[-1.261801,-8.157533,7.090403,-0.923849,0.005091,-7.849328,-4.524730,-4.702190,6.080145,1.087690,-5.831464,-0.288820,4.575636],[-1.471179,-1.172746,-4.904374,3.939893,8.541712,-9.137237,4.466132,-1.183613,2.522668,1.607719,-7.245342,-1.648264,9.837497]],[[-0.304560,-0.684497,-8.226797,3.276312,-3.674103,-3.271678,1.975900,-4.051913,6.059445,3.848900,3.099668,5.114651,-3.625196],[1.211555,9.542536,-7.089102,-1.129758,2.423044,5.329519,3.692681,-3.409230,-0.141743,-0.923240,3.180074,-0.522095,7.617733],[-5.944592,-1.970388,-8.594203,8.489699,6.412220,8.051456,-3.255229,-4.865824,-7.478022,0.603037,2.885733,-6.395522,6.425528]],[[-7.505391,-8.660470,9.233332,-2.091728,-7.299638,-4.467956,-0.419183,3.012516,9.229903,5.454690,9.782775,-1.213669,-0.882576],[-4.858827,2.937655,3.852027,-7.416873,9.596627,-7.299207,8.192447,-1.788474,-3.387832,2.313116,3.955395,-9.649379,4.140833],[-8.431481,-7.269872,8.955845,6.449270,-3.268899,-9.124154,-3.521821,3.061796,1.751692,0.767932,-6.185620,6.589074,9.879987]],[[-7.118573,0.030725,-2.672580,9.008593,-6.798266,8.189153,8.931084,-9.917739,-0.227479,6.229284,7.227682,2.868741,0.433103],[9.835061,0.117823,9.383366,-7.821083,5.809489,-2.035401,0.029833,-6.347832,-4.343226,8.881434,6.337791,5.669993,2.586207],[-5.469427,-5.304870,-1.725577,-9.958520,-8.444755,5.895132,-7.454028,6.262785,-9.126023,0.480052,-1.600270,-7.255158,1.447411]],[[8.527319,0.897103,9.087109,0.854230,8.795575,7.481803,-3.941166,3.796630,-9.134786,-0.535539,-7.221731,6.644094,2.180026],[9.808949,1.319616,-8.340399,4.986380,1.119996,6.249730,-2.906544,-1.143234,-3.724147,-3.759346,-8.987759,3.204197,-7.169564],[0.080268,5.693268,9.900153,7.795331,5.920763,-6.663815,0.210454,-2.034883,-7.451087,8.729696,-0.439546,5.175807,6.994416]],[[-1.414649,6.270127,-2.246597,-4.996538,3.671965,-5.046166,-8.914329,-9.672642,-1.312148,-5.721459,-1.734987,-3.632997,5.919212],[7.055103,0.021174,-1.848659,8.684836,-4.374080,9.353565,-7.569772,6.329532,0.630661,-0.668146,-1.785332,4.243524,0.897094],[9.790318,9.542607,4.841542,-0.949016,0.189062,-5.882669,-2.557725,-0.984762,8.103868,-0.048769,1.041974,-1.437877,-7.915054]]], dtype = "float64")#candidate|11345|(9, 3, 13)|const|float64
uop_11346 = relay.sqrt(const_11345.astype('float64')) # shape=(9, 3, 13)
output = uop_11346
output2 = uop_11346
func_11351 = relay.Function([], output)
mod['func_11351'] = func_11351
mod = relay.transform.InferType()(mod)
output = func_11351()
func_11352 = relay.Function([], output)
mutated_mod['func_11352'] = func_11352
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11411 = relay.const([[[10,-1,9,7,8,-2,-1,-9,-2,-9,6],[10,9,-2,1,-9,5,1,1,-5,5,6],[-2,2,-1,-10,-1,4,-8,2,-2,-10,10],[3,1,-10,7,-4,-4,-5,-7,9,7,7],[2,7,-8,-2,-8,2,3,6,10,1,4]],[[9,2,9,-3,-5,4,10,-8,-4,5,8],[10,10,-3,5,6,1,4,-7,6,4,5],[4,6,2,4,1,-3,5,1,-3,4,5],[6,8,8,-2,8,8,5,-5,-9,4,-7],[-6,-7,-5,7,-2,4,2,4,4,-3,-5]],[[-2,7,7,3,-10,-4,2,-9,-9,-1,-3],[-6,-9,8,-5,-10,3,2,1,-8,6,8],[-9,-6,-10,-5,2,-9,-4,-4,-9,-7,2],[-4,5,-3,-2,-1,-8,3,-6,8,-8,8],[3,10,-6,4,-8,-2,10,4,-4,7,1]],[[-9,-6,4,3,5,-4,8,6,10,2,-7],[-7,8,-5,5,-3,-5,-9,-3,3,-10,7],[-6,2,6,-10,-10,-3,10,1,6,-8,-3],[1,1,7,10,-9,-6,-6,7,-5,-3,-5],[-6,6,2,-6,1,4,3,3,-5,4,5]],[[4,-4,-1,7,9,6,-7,9,5,3,2],[-1,1,-9,-7,-3,-6,-10,-5,5,-2,1],[-9,-5,2,6,-5,-9,4,1,2,-2,4],[-7,9,-5,3,10,-6,-8,4,2,-2,-6],[-1,-6,3,-1,-10,-8,-10,-1,10,-7,-8]],[[-7,-9,-2,2,-5,-6,-7,-1,-8,9,-1],[8,4,-3,6,-5,4,2,5,3,-10,-3],[8,7,4,-3,-7,-6,10,-1,1,-9,-10],[-10,-6,4,-1,-3,8,6,-8,-6,-9,7],[2,-6,-3,-9,-8,7,1,2,-10,-3,-6]],[[2,-8,-10,-1,-8,4,7,3,-10,4,-4],[3,-6,-10,-3,8,2,-4,-4,-9,9,10],[-1,-3,-1,2,-1,-3,8,-4,2,4,7],[-8,2,-5,3,8,-6,4,-7,7,1,-5],[-5,-2,2,-3,-4,9,-10,-9,-8,6,-10]],[[-3,9,5,10,-3,-10,2,-10,2,-7,2],[-5,-4,-9,-1,3,6,-6,5,4,10,2],[-7,-8,6,9,-7,-10,1,1,10,6,7],[-8,7,-10,-7,1,-5,-2,6,-1,-8,-4],[-2,-1,-9,8,-10,-8,-10,5,1,3,5]]], dtype = "uint16")#candidate|11411|(8, 5, 11)|const|uint16
var_11412 = relay.var("var_11412", dtype = "uint16", shape = (8, 5, 11))#candidate|11412|(8, 5, 11)|var|uint16
bop_11413 = relay.subtract(const_11411.astype('uint16'), relay.reshape(var_11412.astype('uint16'), relay.shape_of(const_11411))) # shape=(8, 5, 11)
output = bop_11413
output2 = bop_11413
func_11439 = relay.Function([var_11412,], output)
mod['func_11439'] = func_11439
mod = relay.transform.InferType()(mod)
mutated_mod['func_11439'] = func_11439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11440 = relay.var("var_11440", dtype = "uint16", shape = (8, 5, 11))#candidate|11440|(8, 5, 11)|var|uint16
func_11439_call = mutated_mod.get_global_var('func_11439')
call_11441 = func_11439_call(var_11440)
output = call_11441
func_11442 = relay.Function([var_11440], output)
mutated_mod['func_11442'] = func_11442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4920_call = mod.get_global_var('func_4920')
func_4921_call = mutated_mod.get_global_var('func_4921')
call_11469 = relay.TupleGetItem(func_4920_call(), 1)
call_11470 = relay.TupleGetItem(func_4921_call(), 1)
func_11274_call = mod.get_global_var('func_11274')
func_11278_call = mutated_mod.get_global_var('func_11278')
var_11479 = relay.var("var_11479", dtype = "float32", shape = (576,))#candidate|11479|(576,)|var|float32
const_11480 = relay.const([-3.197432,-7.114617,-1.445042,-2.365913,0.823816,-5.732910,-7.910693,-9.442212,3.318244,-4.231522,-2.908121,2.404922,-0.515766,3.203066,-4.256322,-4.273203,-0.433348,8.567888,-9.791556,5.971979,-1.401395,-8.466481,-7.630058,3.548723,-4.424167,-2.184573,2.972403,-2.078851,-1.805040,0.913289,-8.394686,8.021504,-5.432255,4.708240,-5.551595,8.859984,-4.906191,7.797745,-6.778084,6.857379,7.926494,-3.216964,8.064225,-8.340223,-7.420469,-6.924236,0.702495,9.806918,6.197850,-8.285022,7.789053,-4.614792,9.017222,8.822836,-2.639336,3.670795,-6.299115,-8.659227,-4.366636,6.868522,-3.272619,5.939771,4.443363,-1.018393,5.016975,-9.969676,-7.525835,-1.827593,-6.671715,2.173140,-3.470704,-7.319089,-6.591139,-8.412081,7.519248,9.597996,-6.955854,3.179263,-2.135721,-9.020823,-8.288389,-5.323998,3.621734,3.155836,-9.334204,-3.812714,8.110282,1.411814,8.494892,-2.841329,6.253379,-5.266206,-8.604455,9.585551,3.490374,-9.533579,-8.314938,-7.941807,7.420703,-9.483775,5.078481,4.550019,6.590801,-0.475783,-4.837283,-4.065330,4.699251,2.724576,-3.882934,-8.704205,-1.255255,-6.972418,3.597624,-0.960603,-2.176064,6.453374,3.650551,-9.771696,0.540906,2.799511,0.827363,-4.271635,0.262722,-5.488611,-1.239202,9.723904,7.651574,-8.323192,0.435441,3.954510,4.497485,1.906062,8.773841,7.638553,-3.486115,1.941032,-1.267878,-5.729320,4.337644,-0.538583,8.497273,3.456530,4.569154,-6.965956,-3.016037,-8.311544,-8.179124,4.871618,8.913574,-0.932521,2.051981,3.999630,5.788485,1.001581,-1.436510,3.838220,-1.307983,-9.154455,-8.560010,-3.491834,-6.990342,-1.792153,-7.008110,8.555329,-1.532590,7.425407,1.477092,-4.289121,6.699258,2.777359,7.817765,9.244196,0.153820,4.194618,-0.465169,4.932993,-2.184846,2.888043,6.528297,-7.814342,7.991700,2.738611,-9.432012,8.837397,-7.569253,0.390440,2.320283,4.129679,-9.433740,-8.655849,-0.762296,3.648107,5.910121,0.244286,7.944782,3.607865,0.288700,3.357798,-2.082473,0.347187,-1.008600,-3.735364,-5.787677,-1.632461,-3.249469,6.988174,-4.107472,5.405971,-8.087874,-9.434869,-5.566617,-8.813199,6.592682,1.674446,-3.296860,-3.833332,5.695917,2.862172,-9.291744,-2.879504,-9.807361,1.646750,-8.547293,6.815802,7.616362,8.654579,5.988448,1.705303,9.614528,-0.830175,-2.134446,-0.235239,6.093304,8.206025,-7.939739,-7.726521,3.861317,3.983957,-3.511414,-2.300337,2.633830,8.331280,8.689137,8.645704,5.474141,2.926127,-0.634823,9.240978,0.300677,6.535600,-7.452178,-6.684146,5.981826,6.652502,-5.233262,0.397035,6.669891,-7.002949,2.375382,-0.627393,0.912112,-8.638042,0.853713,4.710460,-1.481271,-4.577939,-1.425524,2.611642,0.256865,5.595994,-0.746544,0.449276,1.792426,5.542313,8.848967,0.352254,9.426835,-7.943422,3.512928,0.542078,-0.799052,-9.848419,-6.748881,-0.982891,9.772137,-5.234336,-2.721385,4.759772,7.140978,-4.861790,-8.987044,-8.426376,-9.706954,2.833993,-2.390919,8.609005,-5.352163,-1.873765,3.151344,-8.192385,-0.762261,9.137103,-0.101236,6.643341,6.129898,-5.479287,7.215535,0.059671,6.203767,-0.071447,7.716765,-8.343012,3.942231,-7.983437,0.644544,6.614905,4.964438,-6.605274,-6.226361,-4.564843,-8.878870,9.549057,4.865112,5.464083,8.573684,-9.218255,1.920320,8.676473,1.893072,-2.224630,-8.225378,6.181285,-2.494453,-7.074319,4.785854,-4.484369,4.414345,2.179034,-7.792017,-4.218209,-3.145574,-7.255705,2.977225,0.413817,9.069005,-6.906542,4.603484,-0.907022,6.519118,-6.766283,8.497798,-3.876889,6.624157,6.174351,-0.190532,8.713841,-7.850405,5.698061,3.178434,7.013655,-7.640813,2.769690,8.258089,2.255276,-1.301680,7.043639,-6.066643,-4.581398,4.204434,2.897072,5.596932,7.138839,-2.690115,-1.600484,4.101047,-1.258587,8.565919,5.992687,6.374958,1.400266,7.597941,3.194411,8.710528,8.511207,3.378344,-0.154227,7.145416,8.487505,-6.633702,-2.555576,1.575131,2.845581,-9.603151,5.252895,6.060760,6.922696,3.454433,-9.529818,-6.002223,5.643477,-1.357468,7.294130,7.050624,3.099502,-1.972113,1.325729,6.508380,-4.023229,-3.457086,8.896071,-0.696164,-2.019478,-6.226274,-1.820034,-1.494095,-3.535426,-2.305992,-2.102160,-3.184045,9.322990,8.643295,-0.906878,-9.497945,-1.101572,-5.758110,-7.716248,-3.972295,-7.563188,-1.467323,-9.721188,2.045877,0.106831,-6.390644,6.460028,-3.481538,7.703783,-3.722776,-9.569989,-7.959667,8.229824,-7.773485,6.235334,-0.593828,1.116340,1.000893,5.383151,1.925544,-5.324800,-6.159925,-0.855665,-1.521799,0.055423,-9.687799,0.906279,-7.664209,3.454800,6.547158,-1.204666,5.014815,-6.566886,3.021201,6.531415,-2.716451,-6.754728,0.334782,3.173152,-0.230205,-5.897309,-8.625496,2.713916,-5.253506,-2.584335,4.325731,1.176728,-9.367310,4.938994,4.058145,-3.986565,-4.494406,3.863706,-0.546716,-9.977078,1.913072,1.070508,-9.540127,-2.592675,3.532603,-8.646162,5.412254,7.764848,3.693693,8.889750,1.232559,6.486651,-7.956366,-7.436194,7.839947,1.663834,8.986514,4.288380,9.356725,9.190656,-1.866531,-2.807709,9.427847,7.795215,-8.213657,-6.062173,1.387786,-5.502437,-9.163021,-7.282010,8.544818,-7.423764,-3.194076,-5.457686,9.629797,-9.273906,-6.728672,-0.586102,9.325077,-0.386938,-4.861150,0.644511,-7.162329,-5.660971,-0.552540,9.421709,-7.352834,6.092744,6.059318,3.815829,9.668205,-8.242420,-7.652660,6.298376,-5.236947,6.603333,-0.652404,-7.692907,-1.731976,2.432942,2.405605,-0.628673,-0.162584,-1.295929,-2.906678,7.718741,-5.475661,7.915563,-3.275929,-4.036005,-5.882878,2.993414,-0.265636,-3.944895,-4.207147,-3.050863,-5.818093,-7.003700,-5.142994,-1.656770,-8.038329,-6.758122,1.638159,0.091099,-1.111203,-3.926910,6.740870,-2.619541,-2.318214,6.685431,-6.651089,-4.324732,-6.252069,-7.334347,-0.385785,1.111858,-3.893834,3.863624,1.929458,8.498685,-7.345299,9.635966,6.785335,3.502176,-8.407285,5.503536,-3.552875,1.090847,-7.905381,1.758268,-3.536583,1.937068,-6.616831,-9.600719,6.433258,-3.896025,3.181316,4.455083,7.343962,-1.001160,5.101242,-9.219606,-1.843266,1.637611,0.933004,3.151906,0.726260,-6.144150,8.010434,-0.111516,-9.560466,-8.798042,-1.870149,9.849924,-9.950902,6.884856,7.536405,-5.553288,0.174296,-8.938983,-0.073411,-5.163063,-0.885631,-8.350881,6.671310,-2.425556,1.907572,5.237502,-2.374494,4.049658,9.711912,0.950345,-5.521930,-9.755007,4.812856,6.016349,-3.362685,8.580231,-3.273807,-3.443551,-2.181875,-9.209966,4.734212,0.639332,-0.530784,-2.014928,5.535613,-6.710945,3.138459,0.117149,3.098319,7.557442,-6.082871,-4.827497,-2.806715,-6.194639,6.715669,-5.975264,1.983126,-6.283435,-9.463192,8.034230,-8.057094,1.255866,-8.964393,-6.304833,8.448936,9.486447,4.654936,9.887717,-7.432314,-7.831007,-0.057567,-0.153356,9.074641,1.462589,0.483093,7.661013,-1.986291,-5.087821,-7.249140,-3.771834,-6.152572,1.982806,7.182810,4.091805,0.550036,8.556050,-4.325443,3.773062,-3.445213,6.216558,0.537704,-2.710664,8.074424,-8.814500,3.705425,-1.689510,-9.549441,9.694379,-9.821165,9.157275,5.962978,9.389313,-7.625095,8.982043,9.863799,-1.464772,1.526520,-6.792791,4.749928,-8.866282,5.111477,-4.674924,6.668688,7.313918,-5.601728,9.846963,8.884932,9.787455,0.980232,-8.331426,5.295213,4.927579,2.351924,-4.379095,-5.688618,-4.326802,4.934970,2.087352,-3.988370,-6.403356,6.778453,-8.306691,-4.033082,-6.484417,-2.453040,-6.782677,5.035235,5.057873,5.249291,-5.180814,-9.040414,2.249749,4.408534,-6.883710,2.660157,7.754014,-7.070116,8.570601,3.376767,-4.851176,-5.500853,-5.649755,-4.972113,9.280970,3.666886,3.729054,-6.521878,3.936791,1.457359,0.082026,-2.046473,7.185206,1.651467,9.909058,-6.449770,-0.104284,-9.942038,2.488020,-6.421724,-6.230985,-1.136669,-4.492274,-5.904979,-5.886176,9.104487,-4.720504,-0.682695,1.932112,-1.405468,7.944678,-8.974653,4.750495,-9.256742,-3.386492,2.694092,-4.919686,-6.555793,-2.876905,-5.902485,2.127023,5.684739,4.101523,5.908509,7.492713,4.637399,9.589412,-7.186973,-8.431655,9.089544,-1.044613,6.156558,-0.544119,6.245556,-9.214511,1.713962,6.969526,0.874441,6.551132,6.018726,-9.035794,9.756318,9.777406,-4.180408,-6.426844,-3.988782,9.567444,7.199393,9.194183,-7.161262,-0.916785,6.287198,-8.299255,-5.034116,-3.750533,-9.335988,-4.345311,-8.202334,-0.662255,5.055793,-8.203418,2.347511,4.907258,2.138637,5.400829,-2.019556,3.116987,7.945634,-7.333231,8.453994,-3.598757,5.701249,6.826249,-4.035445,-9.111416,-0.306231,3.638972,-2.532596,-7.715403,8.421690,-7.087543,1.711970,-8.747605,8.285474,-5.754894,1.240391,3.995528,6.702743,-3.658618,-4.517428,7.578649], dtype = "float32")#candidate|11480|(864,)|const|float32
call_11478 = relay.TupleGetItem(func_11274_call(relay.reshape(var_11479.astype('float32'), [576,]), relay.reshape(const_11480.astype('float32'), [12, 8, 9]), ), 2)
call_11481 = relay.TupleGetItem(func_11278_call(relay.reshape(var_11479.astype('float32'), [576,]), relay.reshape(const_11480.astype('float32'), [12, 8, 9]), ), 2)
output = relay.Tuple([call_11469,call_11478,var_11479,const_11480,])
output2 = relay.Tuple([call_11470,call_11481,var_11479,const_11480,])
func_11482 = relay.Function([var_11479,], output)
mod['func_11482'] = func_11482
mod = relay.transform.InferType()(mod)
var_11483 = relay.var("var_11483", dtype = "float32", shape = (576,))#candidate|11483|(576,)|var|float32
output = func_11482(var_11483)
func_11484 = relay.Function([var_11483], output)
mutated_mod['func_11484'] = func_11484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9315_call = mod.get_global_var('func_9315')
func_9317_call = mutated_mod.get_global_var('func_9317')
call_11639 = relay.TupleGetItem(func_9315_call(), 0)
call_11640 = relay.TupleGetItem(func_9317_call(), 0)
output = call_11639
output2 = call_11640
func_11658 = relay.Function([], output)
mod['func_11658'] = func_11658
mod = relay.transform.InferType()(mod)
mutated_mod['func_11658'] = func_11658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11658_call = mutated_mod.get_global_var('func_11658')
call_11659 = func_11658_call()
output = call_11659
func_11660 = relay.Function([], output)
mutated_mod['func_11660'] = func_11660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8053_call = mod.get_global_var('func_8053')
func_8055_call = mutated_mod.get_global_var('func_8055')
call_11675 = relay.TupleGetItem(func_8053_call(), 0)
call_11676 = relay.TupleGetItem(func_8055_call(), 0)
func_9315_call = mod.get_global_var('func_9315')
func_9317_call = mutated_mod.get_global_var('func_9317')
call_11681 = relay.TupleGetItem(func_9315_call(), 0)
call_11682 = relay.TupleGetItem(func_9317_call(), 0)
uop_11707 = relay.log2(call_11681.astype('float64')) # shape=(3, 16, 6)
uop_11709 = relay.log2(call_11682.astype('float64')) # shape=(3, 16, 6)
output = relay.Tuple([call_11675,uop_11707,])
output2 = relay.Tuple([call_11676,uop_11709,])
func_11721 = relay.Function([], output)
mod['func_11721'] = func_11721
mod = relay.transform.InferType()(mod)
output = func_11721()
func_11722 = relay.Function([], output)
mutated_mod['func_11722'] = func_11722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6329_call = mod.get_global_var('func_6329')
func_6330_call = mutated_mod.get_global_var('func_6330')
call_11756 = relay.TupleGetItem(func_6329_call(), 0)
call_11757 = relay.TupleGetItem(func_6330_call(), 0)
func_6474_call = mod.get_global_var('func_6474')
func_6475_call = mutated_mod.get_global_var('func_6475')
call_11771 = relay.TupleGetItem(func_6474_call(), 0)
call_11772 = relay.TupleGetItem(func_6475_call(), 0)
func_10457_call = mod.get_global_var('func_10457')
func_10460_call = mutated_mod.get_global_var('func_10460')
var_11775 = relay.var("var_11775", dtype = "float64", shape = (196, 2))#candidate|11775|(196, 2)|var|float64
call_11774 = relay.TupleGetItem(func_10457_call(relay.reshape(var_11775.astype('float64'), [4, 7, 14])), 0)
call_11776 = relay.TupleGetItem(func_10460_call(relay.reshape(var_11775.astype('float64'), [4, 7, 14])), 0)
output = relay.Tuple([call_11756,call_11771,call_11774,var_11775,])
output2 = relay.Tuple([call_11757,call_11772,call_11776,var_11775,])
func_11788 = relay.Function([var_11775,], output)
mod['func_11788'] = func_11788
mod = relay.transform.InferType()(mod)
var_11789 = relay.var("var_11789", dtype = "float64", shape = (196, 2))#candidate|11789|(196, 2)|var|float64
output = func_11788(var_11789)
func_11790 = relay.Function([var_11789], output)
mutated_mod['func_11790'] = func_11790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10279_call = mod.get_global_var('func_10279')
func_10280_call = mutated_mod.get_global_var('func_10280')
call_11908 = func_10279_call()
call_11909 = func_10279_call()
output = relay.Tuple([call_11908,])
output2 = relay.Tuple([call_11909,])
func_11917 = relay.Function([], output)
mod['func_11917'] = func_11917
mod = relay.transform.InferType()(mod)
mutated_mod['func_11917'] = func_11917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11917_call = mutated_mod.get_global_var('func_11917')
call_11918 = func_11917_call()
output = call_11918
func_11919 = relay.Function([], output)
mutated_mod['func_11919'] = func_11919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5353_call = mod.get_global_var('func_5353')
func_5354_call = mutated_mod.get_global_var('func_5354')
call_11923 = relay.TupleGetItem(func_5353_call(), 1)
call_11924 = relay.TupleGetItem(func_5354_call(), 1)
func_8608_call = mod.get_global_var('func_8608')
func_8611_call = mutated_mod.get_global_var('func_8611')
var_11934 = relay.var("var_11934", dtype = "float32", shape = (576,))#candidate|11934|(576,)|var|float32
call_11933 = relay.TupleGetItem(func_8608_call(relay.reshape(var_11934.astype('float32'), [576,])), 2)
call_11935 = relay.TupleGetItem(func_8611_call(relay.reshape(var_11934.astype('float32'), [576,])), 2)
output = relay.Tuple([call_11923,call_11933,var_11934,])
output2 = relay.Tuple([call_11924,call_11935,var_11934,])
func_11936 = relay.Function([var_11934,], output)
mod['func_11936'] = func_11936
mod = relay.transform.InferType()(mod)
var_11937 = relay.var("var_11937", dtype = "float32", shape = (576,))#candidate|11937|(576,)|var|float32
output = func_11936(var_11937)
func_11938 = relay.Function([var_11937], output)
mutated_mod['func_11938'] = func_11938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4122_call = mod.get_global_var('func_4122')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_11982 = relay.TupleGetItem(func_4122_call(), 0)
call_11983 = relay.TupleGetItem(func_4124_call(), 0)
output = relay.Tuple([call_11982,])
output2 = relay.Tuple([call_11983,])
func_11984 = relay.Function([], output)
mod['func_11984'] = func_11984
mod = relay.transform.InferType()(mod)
mutated_mod['func_11984'] = func_11984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11984_call = mutated_mod.get_global_var('func_11984')
call_11985 = func_11984_call()
output = call_11985
func_11986 = relay.Function([], output)
mutated_mod['func_11986'] = func_11986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2598_call = mod.get_global_var('func_2598')
func_2599_call = mutated_mod.get_global_var('func_2599')
call_12009 = func_2598_call()
call_12010 = func_2598_call()
output = call_12009
output2 = call_12010
func_12018 = relay.Function([], output)
mod['func_12018'] = func_12018
mod = relay.transform.InferType()(mod)
output = func_12018()
func_12019 = relay.Function([], output)
mutated_mod['func_12019'] = func_12019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8281_call = mod.get_global_var('func_8281')
func_8282_call = mutated_mod.get_global_var('func_8282')
call_12028 = relay.TupleGetItem(func_8281_call(), 0)
call_12029 = relay.TupleGetItem(func_8282_call(), 0)
func_8281_call = mod.get_global_var('func_8281')
func_8282_call = mutated_mod.get_global_var('func_8282')
call_12038 = relay.TupleGetItem(func_8281_call(), 0)
call_12039 = relay.TupleGetItem(func_8282_call(), 0)
func_4330_call = mod.get_global_var('func_4330')
func_4336_call = mutated_mod.get_global_var('func_4336')
const_12047 = relay.const([-4.338316,-3.279988,1.723081,8.996496,-8.162869,-8.104066,-3.102525,-5.521558,-0.854056,-4.793417,4.189528,1.190891,6.849548,-6.090246,-3.152158,-9.971855,-2.500862,9.695811,-8.319125,-1.791848,-5.357329,-6.981660,-0.030919,8.548068,-2.739800,7.859079,-3.585220,-8.320855,1.068334,-4.598515,0.772675,-4.023849,9.429602,1.013615,-7.828966,-6.003797,-2.507442,-0.276416,8.839656,5.589023,8.202427,-3.062269,3.873386,-1.072288,5.480771,8.361376,9.605115,-7.027845,5.404863,-4.189722,-4.278253,3.964646,-0.572042,0.341411,3.099280,6.152551,1.286128,-2.477543,-3.715115,6.846468,-4.461635,-3.044609,5.455195,-2.549154,5.062522,-2.212178,-5.939285,-6.334639,5.836984,-5.839266,8.221842,-2.551879,7.582354,1.688580,1.880565,-0.851425,6.530253,5.614704,1.843497,-5.695205,-3.255963,-0.074436,-8.894947,6.822303,-1.340372,-4.826504,7.701182,0.503151,-1.682310,0.400980,1.988003,6.542473,-4.894970,1.865915,-8.324860,-8.855401,5.102956,8.963089,-3.127218,8.862158,4.686570,-6.673499,-8.629442,7.482838,-8.827288,-9.267105,-4.065540,1.840218,-9.120792,0.203751,-1.041314,-7.501213,-9.174381,9.696175,-9.996707,-7.607616,-5.300056,1.302648,-0.378399,9.289319,3.581782,-5.010700,6.530908,-3.077370,0.799094,8.042764,-6.547720,8.756581,9.977209,8.121835,6.440382,9.702787,-7.544844,9.458658,-6.098508,6.258154,-4.266081,7.951414,6.029565,-6.364100,9.361913,-3.887133,6.937418,3.577818,-1.246943,-6.850584,-4.442944,-1.847875,-9.796784,9.987328,-4.224578,-0.834703,-0.223724,2.674430,-3.610786,-1.549026,5.247502,3.388121,-6.613218,1.203249,7.998869,4.822780,-6.658457,-6.312427,3.099093,2.486510,-3.507456,-5.682782,9.454657,6.659391,5.421794,-2.708345,-3.392725,5.892220,-5.731888,-6.132003,2.751176,6.085641,6.335131,-3.714867,6.556928,-8.420078,-2.375900,-7.057827,-9.281169,0.180674,-8.510604,-4.325292,1.922270,3.803267,5.648217,9.191205,5.062608,-1.900265,-2.451383,1.795601,-2.005208,7.537456,3.649149,-9.354899,7.099858,4.808260,3.139049,0.312298,-7.575302,-6.165747,-9.310250,-9.899159,-8.174481,-8.720490,6.748446,-2.484795,0.001864,-5.692127,-4.219932,5.338001,-7.282097,4.536500,-9.111142,-5.837334,9.030797,-7.037622,-3.359426,-9.336072,0.085227,4.438562,-9.412859,-1.748949,-2.949271,-1.498491,-9.415876,-7.700953,9.699865,-7.734498,-6.606097,-5.506739,-3.044245,5.819446,5.749624,5.897916,-9.607049,9.271254,5.672558,4.986018,0.970051,-8.169903,1.570423,-4.137492,-4.957012,-9.984624,-8.709186,-0.335805,-9.452155,2.851491,9.002223,-7.744766,-2.347689,6.362460,-2.855437,8.112163,-5.437209,9.075191,-0.865654,-0.469534,-4.520011,-1.207245,5.796070,1.346267,-9.026662,8.364483,-2.869067,-9.821550,-7.426449,-0.609897,-4.876099,-4.112870,9.510585,-4.917157,2.456957,-3.584561,4.933136,-3.746229,8.765672,-4.840923,7.388308,-8.040463,-4.371160,-9.257865,-3.830382,3.583124,-8.780165,8.557723,4.287260,9.857689,3.445545,-3.336474,-7.682293,5.088046,2.150682,-9.028082,-0.872428,-6.835937,8.747912,9.351667,8.162141,-6.869030,-7.313000,8.855217,9.761594,-1.376523,-1.063444,5.418059,-7.207700,-2.177856,5.914437,-8.143713,1.346488,-8.912513,0.900386,-8.332614,-7.340920,-4.027272,9.701797,-8.780797,-3.654691,7.743628,1.262686,-4.214322,7.834240,1.293913,0.398448,-4.324532,-4.404104,6.566173,-2.342682,-2.046292,-8.164189,7.487620,-2.465058,-8.776734,9.925507,8.673329,-6.379660,-4.143346,0.066943,-9.551979,4.359377,9.470780,9.386237,7.554334,0.211152,-2.215501,-3.130767,9.538245,1.038750,1.142797,7.209690,-1.617247,-4.982511,3.207612,-0.877706,-5.785431,0.063079,-3.172108,-8.244810,-7.327831,3.930375,2.644213,2.709588,1.800299,-5.661895,9.848521,5.377983,-9.678373,-3.142525,7.365418,8.739849,-5.213032,-9.268416,-5.379877,-0.248497,-7.768688,3.519229,1.631943,-2.371210,-7.221276,9.050460,-0.268616,1.513523,2.963927,-6.494834,-0.267136,-3.623895,-0.572053,8.163134,-8.087052,-5.983413,-4.182635,-4.533630,-0.837260,-5.779229,-2.749616,-5.476325,-4.807562,8.827007,9.314219,6.472800,7.077728,-7.131208,-2.621751,-9.225123,1.034812,9.751399,6.417170,3.338795,-3.735438,-2.407010,9.608265,7.658937,-1.825344,9.265229,-5.685868,9.210304,0.977337,-1.134986,-0.100286,-1.050700,7.440424,1.698864,3.097463,-1.158427,-1.769713,-2.376607,7.378039,6.230139,-3.201011,6.913482,4.704843,4.890515,-2.727472,-1.383833,-5.894382,-6.724117,-0.142934,-6.427684,-6.940990,8.893268,7.579300,-2.979951,2.134710,-3.690330,3.138426,2.093703,0.971580,8.048361,-6.315048,-1.152917,-8.690365,-1.236032,-1.987969,-8.614998,9.326898,7.197976,-2.384575,3.670074,3.488945,7.654104,1.861517,-7.470807,6.527341,-4.241372,8.262561,1.591427,1.902301,6.909905,-1.552186,-2.606271,5.027543,8.981503,1.434134,-8.515760,-4.320870,5.439544,-6.393403,-5.902461,3.520823,3.101840,8.905012,-2.645658,-1.729027,-4.032592,-9.830528,-8.463353,-3.613811,2.532207,-4.624305,3.722193,0.551656,-2.518096,-9.236580,-4.482563,9.362460,-3.506517,-9.429358,8.810754,-8.518963,4.012039,-4.697570,0.460362,0.446665,-1.261003,-0.144316,4.090342,9.973228,8.636793,-5.812307,7.500227,0.752607,3.379995,3.146966,-1.994379,-5.498650,-9.545126,9.131139,-6.691089,-8.243881,-4.403131,-6.065005,-2.617833,3.331635,8.525175,1.557524,5.971262,-3.951893,-6.104687,5.292443,-2.099516,0.475189,-3.101378,-8.492056,2.135180,8.299230,9.896162,8.296571,0.590560,9.412814,7.198763,-8.954877,5.658737,9.141382,-3.473771,-4.529211,-8.693907,4.941193,-8.585263,1.256018,-1.514139,9.890033,-2.181331,0.726014,3.416212,-3.476227,-3.077432,6.155759,-6.146616,9.563170,2.688676,4.689718,0.310297,-7.748162,-8.758117,-6.280404,-7.689938,-9.394309,-3.329843,3.297582], dtype = "float32")#candidate|12047|(576,)|const|float32
var_12048 = relay.var("var_12048", dtype = "uint32", shape = (6, 4))#candidate|12048|(6, 4)|var|uint32
var_12049 = relay.var("var_12049", dtype = "uint32", shape = (384,))#candidate|12049|(384,)|var|uint32
const_12050 = relay.const([True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False], dtype = "bool")#candidate|12050|(320,)|const|bool
call_12046 = relay.TupleGetItem(func_4330_call(relay.reshape(const_12047.astype('float32'), [576,]), relay.reshape(var_12048.astype('uint32'), [24,]), relay.reshape(var_12049.astype('uint32'), [384, 1]), relay.reshape(const_12050.astype('bool'), [8, 40]), ), 1)
call_12051 = relay.TupleGetItem(func_4336_call(relay.reshape(const_12047.astype('float32'), [576,]), relay.reshape(var_12048.astype('uint32'), [24,]), relay.reshape(var_12049.astype('uint32'), [384, 1]), relay.reshape(const_12050.astype('bool'), [8, 40]), ), 1)
func_8712_call = mod.get_global_var('func_8712')
func_8714_call = mutated_mod.get_global_var('func_8714')
call_12067 = relay.TupleGetItem(func_8712_call(), 0)
call_12068 = relay.TupleGetItem(func_8714_call(), 0)
func_4855_call = mod.get_global_var('func_4855')
func_4856_call = mutated_mod.get_global_var('func_4856')
call_12094 = relay.TupleGetItem(func_4855_call(), 0)
call_12095 = relay.TupleGetItem(func_4856_call(), 0)
output = relay.Tuple([call_12028,call_12038,call_12046,const_12047,var_12048,var_12049,const_12050,call_12067,call_12094,])
output2 = relay.Tuple([call_12029,call_12039,call_12051,const_12047,var_12048,var_12049,const_12050,call_12068,call_12095,])
func_12099 = relay.Function([var_12048,var_12049,], output)
mod['func_12099'] = func_12099
mod = relay.transform.InferType()(mod)
var_12100 = relay.var("var_12100", dtype = "uint32", shape = (6, 4))#candidate|12100|(6, 4)|var|uint32
var_12101 = relay.var("var_12101", dtype = "uint32", shape = (384,))#candidate|12101|(384,)|var|uint32
output = func_12099(var_12100,var_12101,)
func_12102 = relay.Function([var_12100,var_12101,], output)
mutated_mod['func_12102'] = func_12102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3461_call = mod.get_global_var('func_3461')
func_3463_call = mutated_mod.get_global_var('func_3463')
call_12127 = relay.TupleGetItem(func_3461_call(), 0)
call_12128 = relay.TupleGetItem(func_3463_call(), 0)
func_6221_call = mod.get_global_var('func_6221')
func_6223_call = mutated_mod.get_global_var('func_6223')
call_12139 = relay.TupleGetItem(func_6221_call(), 2)
call_12140 = relay.TupleGetItem(func_6223_call(), 2)
output = relay.Tuple([call_12127,call_12139,])
output2 = relay.Tuple([call_12128,call_12140,])
func_12145 = relay.Function([], output)
mod['func_12145'] = func_12145
mod = relay.transform.InferType()(mod)
output = func_12145()
func_12146 = relay.Function([], output)
mutated_mod['func_12146'] = func_12146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11327_call = mod.get_global_var('func_11327')
func_11329_call = mutated_mod.get_global_var('func_11329')
call_12177 = relay.TupleGetItem(func_11327_call(), 0)
call_12178 = relay.TupleGetItem(func_11329_call(), 0)
output = call_12177
output2 = call_12178
func_12180 = relay.Function([], output)
mod['func_12180'] = func_12180
mod = relay.transform.InferType()(mod)
output = func_12180()
func_12181 = relay.Function([], output)
mutated_mod['func_12181'] = func_12181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8666_call = mod.get_global_var('func_8666')
func_8667_call = mutated_mod.get_global_var('func_8667')
call_12185 = func_8666_call()
call_12186 = func_8666_call()
func_4421_call = mod.get_global_var('func_4421')
func_4423_call = mutated_mod.get_global_var('func_4423')
call_12198 = relay.TupleGetItem(func_4421_call(), 0)
call_12199 = relay.TupleGetItem(func_4423_call(), 0)
output = relay.Tuple([call_12185,call_12198,])
output2 = relay.Tuple([call_12186,call_12199,])
func_12227 = relay.Function([], output)
mod['func_12227'] = func_12227
mod = relay.transform.InferType()(mod)
output = func_12227()
func_12228 = relay.Function([], output)
mutated_mod['func_12228'] = func_12228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7463_call = mod.get_global_var('func_7463')
func_7464_call = mutated_mod.get_global_var('func_7464')
call_12237 = func_7463_call()
call_12238 = func_7463_call()
func_11788_call = mod.get_global_var('func_11788')
func_11790_call = mutated_mod.get_global_var('func_11790')
var_12268 = relay.var("var_12268", dtype = "float64", shape = (392,))#candidate|12268|(392,)|var|float64
call_12267 = relay.TupleGetItem(func_11788_call(relay.reshape(var_12268.astype('float64'), [196, 2])), 0)
call_12269 = relay.TupleGetItem(func_11790_call(relay.reshape(var_12268.astype('float64'), [196, 2])), 0)
output = relay.Tuple([call_12237,call_12267,var_12268,])
output2 = relay.Tuple([call_12238,call_12269,var_12268,])
func_12270 = relay.Function([var_12268,], output)
mod['func_12270'] = func_12270
mod = relay.transform.InferType()(mod)
mutated_mod['func_12270'] = func_12270
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12271 = relay.var("var_12271", dtype = "float64", shape = (392,))#candidate|12271|(392,)|var|float64
func_12270_call = mutated_mod.get_global_var('func_12270')
call_12272 = func_12270_call(var_12271)
output = call_12272
func_12273 = relay.Function([var_12271], output)
mutated_mod['func_12273'] = func_12273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_12303 = relay.TupleGetItem(func_3507_call(), 0)
call_12304 = relay.TupleGetItem(func_3509_call(), 0)
output = call_12303
output2 = call_12304
func_12309 = relay.Function([], output)
mod['func_12309'] = func_12309
mod = relay.transform.InferType()(mod)
mutated_mod['func_12309'] = func_12309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12309_call = mutated_mod.get_global_var('func_12309')
call_12310 = func_12309_call()
output = call_12310
func_12311 = relay.Function([], output)
mutated_mod['func_12311'] = func_12311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_12345 = relay.TupleGetItem(func_3234_call(), 0)
call_12346 = relay.TupleGetItem(func_3235_call(), 0)
func_10858_call = mod.get_global_var('func_10858')
func_10861_call = mutated_mod.get_global_var('func_10861')
const_12351 = relay.const([3,8,-10,-5,-10,-9,1,-4,4,8,-2,10,-9,2,7,10,9,-2,-8,-1,-3,3,-8,4,-1,-4,5,-6,-5,6,4,-1,-1,10,-1,10,-3,10,10,-5,-4,5,3,4,10,7,3,6,3,7,-9,8,2,5,-1,4,-9,7,-10,9,10,-5,6,-8,7,2,4,10,-9,-7,-5,-8,-10,6,7,-2,-1,-1,-8,5,6,-3,-9,-6,8,-9,-4,5,3,6,7,8,-6,-5,1,2,-7,-10,8,5,1,6,10,-1,-5,4,4,-9,2,-5,-4,-10,1,-9,6,-4,-5,-2,4,-9,-10,-2,-6,3,7,-1,-6,-3,-3,-8,4,7,4,6,3,-10,2,-5,5,8,-7,-2,-2,-2,5,5,1,9,-1,5,4,-7,7,5,-2,-1,-4,6,6,-10,-7,10,-6,5,-8,1,6,-8,-2,3,8,6,7,-7,-7,5,5,-4,-6,10,9,-8,1,-10,-3,-6,-8,-2,-2,9,-9,7,-2,4,-10,-4,6,-8,9,8,10,2,6,-5,6,-2,-10,8,-10,10,7,-10,7,9,-3,-10,3,-1,8,1,-1,9,-2,3,-9,1,-8,-8,7,3,-4,-5,4,6,-3,8,-10,3,-5,-1,1,8,-2,-6,-4,3,3,3,-3,1,-5,-9,-7,-6,-1,7,-10,-3,3,-5,10,3,5,3,6,-5,-5,6,9,6,-9,-3,-8,-3,-4,8,-6,9,8,1,-8,-6,3,6,-4,-3,5,-3,-10,6,5,-10,-6,4,1,-9,-2,-1,-7,-8,-9,-5,4,-9,-6,-8,8,4,7,7,3,-4,-9,1,-1,-8,-9,7,10,-8,1,-7,-4,-1,9,8,4,-9,6,-10,1,7,8,5,-10,-4,9,-7,4,-3,-8,5,2,4,7,6,9,-10,-7,-4,-6,-7,-2,9,4,9,4,3,-1,5,-8,-6,4,5,10,2,10,2,-6,7,4,2,-1,5,2,10,1,-9,3,-10,-5,-1,-2,8,4,7,-5,-6,-4,8,1,7,3,10,-2,-7,1,-6,10,10,-1,-4,4,3,-10,-5,7,4,-2,6,-5,2,10,10,2,-6,4,1,9,-9,5,10,8,1,-8,-3,-9,-10,3,-1,-9,9,-6,-3,-4,-3,-8,10,7,-5,8,10,5,8,-2,-4,-5,-4,5,5,-2,8,-9,8,-10,5,-3,7,6,7,-2,9,-3,-8,10,8,10,-4,4,9,6,-4,-8,6,-6,-4,-3,-6,3,7,-7,-9,-2,-8,-4,-4,10,9,9,-3,-8,3,-9,-10,-5,8,-3,-9,-10,3,5,-4,5,4,-9,-1,6,-10,3,9,-8,-9,4,8,-8,-7,10,9,-3,3,4,8,-8,-6,8,-10,-2,9,-9,-9,-10,2,-8,-9,-6,4,4,1,-2,-4,2,-9,5,2,5,-10,10,8,3,-10,8,8,-7,6,5,10,-6,-2,6,-4,5,-7,6,-4,3,-7,-9,-4,3,8,4,5,-6,10,1,3,9,-3,-7,5,3,2,-8,-10,8,1,5,-1,-3,3,8,9,5,-4,9,2,-3,5,1,-4,-3,-1,3,1,7,-9,9,-2,-2,-9,-6,-4,-5,10,-4,5,3,10,-1,1,5,3,-10,10,-3,-4,10,-8,8,-9,4,2,1,3,-2,-10,-4,3,-9,-5,-2,1,-8,-6,-9,-1,-10,-10,6,3,-6,7,5,4,-4,8,10,9,10,-6,-2,-10,1,-1,3,-5,6,-9,-3,-7,-3,-5,4,-5,-9,1,-10,-4,-3,8,-9,-7,6,-6,-10,-5,5,8,-6,-6,-3,-6,10,-4,5,8,-4,8,2,10,-6,7,-7,-3,-9,7,5,-7,-5,7,2,3,10,-7,-5,4,-1,5,7,10,6,-8,-3,4,-5,-8,-6,-2,-6,1,-3,5,8,-4,7,-9,-3,1,-3,4,8,2,6,-2,-10,-4,-10,10,8,-10,-10,-5,9,1,-5,-7,-10,8,-2,8,7,-6,-2,4,-2,4,-7,-7,9,6,6,8,4,-1,10,8,-3,4,-3,-7,3,9,2,-6,-5,-6,8,6,-2,8,-6,9,5,7,10,-4,-5,4,-8,-10,-3,-5,-10,2,-8,4,-9,5,4,3,-6,-10,-8,8,-5,3,5,-8,7,-7,-4,-10,3,8,-7,-3,6,4,8,-3,2,-8,2,-2,-7,7,-7,6,-10,7,-3,-8,4,4,6,2,3,-5,-7,7,5,7,9,-1,-8,-6,-1,-10,8,8,1,-4,-1,1,-7,5,-10,-3,8,8,4,-4,10,-1,-10,-2,8,-7,-6,-8,7,-4,-8,8,1,-9,-9,2,-9,-8,4,1,-8,3,-9,7,-4,4,8,-5,7,-5,-9,6,2,8,-5,-7,1,7,1,-7,6,9,3,-4,8,-7,-6,6,6,-3,-2,4,-2,-3,-8,10,-2,-8,2,5,1,8,4,5,-5,3,-3,-3,9,-8,8,10,6,7,2,-10,6,10,2,-2,-6,-6,-1,3,-7,-4,10,5,2,4,3,-4,-1,-9,-2,10,5,8,-7,3,-4,8,-10,8,4,5,7,6,-6,1,-7,7,-10,-7,7,-10,-8,-3,-3,2,4,-5,-7,-8,-8,-2,-1,7,5,8,-6,5,9,4,-10,9,2,-4,7,-5,-3,1,7,5,4,5,2,-3,7,-2,4,10,5,8,-8,-8,9,4,9,-7,3,-2,4,-7,-5,-10,2,6,4,1,4,-2,1,8,-5,3,-10,2,-4,-7,-10,7,-6,1,-6,3,-4,-2,3,4,-6,-6,6,10,-1,-9,5,2,1,-5,-8,7,-7,6,1,-8,9,-3,3,2,-2,4,-9,1,2,8,-6,9,-6,-3,-4,-3,-6,5,2,5,10,-3,8,2,-2,9,7,-3,-4,1,-7,1,3,-5,5,8,9,-8,-7,-6,-1,9], dtype = "int16")#candidate|12351|(1120,)|const|int16
var_12352 = relay.var("var_12352", dtype = "float32", shape = (576,))#candidate|12352|(576,)|var|float32
call_12350 = relay.TupleGetItem(func_10858_call(relay.reshape(const_12351.astype('int16'), [5, 14, 16]), relay.reshape(var_12352.astype('float32'), [576,]), ), 6)
call_12353 = relay.TupleGetItem(func_10861_call(relay.reshape(const_12351.astype('int16'), [5, 14, 16]), relay.reshape(var_12352.astype('float32'), [576,]), ), 6)
output = relay.Tuple([call_12345,call_12350,const_12351,var_12352,])
output2 = relay.Tuple([call_12346,call_12353,const_12351,var_12352,])
func_12360 = relay.Function([var_12352,], output)
mod['func_12360'] = func_12360
mod = relay.transform.InferType()(mod)
var_12361 = relay.var("var_12361", dtype = "float32", shape = (576,))#candidate|12361|(576,)|var|float32
output = func_12360(var_12361)
func_12362 = relay.Function([var_12361], output)
mutated_mod['func_12362'] = func_12362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2689_call = mod.get_global_var('func_2689')
func_2691_call = mutated_mod.get_global_var('func_2691')
call_12384 = relay.TupleGetItem(func_2689_call(), 1)
call_12385 = relay.TupleGetItem(func_2691_call(), 1)
output = relay.Tuple([call_12384,])
output2 = relay.Tuple([call_12385,])
func_12388 = relay.Function([], output)
mod['func_12388'] = func_12388
mod = relay.transform.InferType()(mod)
output = func_12388()
func_12389 = relay.Function([], output)
mutated_mod['func_12389'] = func_12389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5452_call = mod.get_global_var('func_5452')
func_5454_call = mutated_mod.get_global_var('func_5454')
call_12466 = func_5452_call()
call_12467 = func_5452_call()
uop_12472 = relay.log(call_12466.astype('float32')) # shape=(10, 2, 13)
uop_12474 = relay.log(call_12467.astype('float32')) # shape=(10, 2, 13)
uop_12478 = relay.log2(uop_12472.astype('float64')) # shape=(10, 2, 13)
uop_12480 = relay.log2(uop_12474.astype('float64')) # shape=(10, 2, 13)
output = relay.Tuple([uop_12478,])
output2 = relay.Tuple([uop_12480,])
func_12516 = relay.Function([], output)
mod['func_12516'] = func_12516
mod = relay.transform.InferType()(mod)
mutated_mod['func_12516'] = func_12516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12516_call = mutated_mod.get_global_var('func_12516')
call_12517 = func_12516_call()
output = call_12517
func_12518 = relay.Function([], output)
mutated_mod['func_12518'] = func_12518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11351_call = mod.get_global_var('func_11351')
func_11352_call = mutated_mod.get_global_var('func_11352')
call_12523 = func_11351_call()
call_12524 = func_11351_call()
func_11082_call = mod.get_global_var('func_11082')
func_11084_call = mutated_mod.get_global_var('func_11084')
call_12535 = relay.TupleGetItem(func_11082_call(), 0)
call_12536 = relay.TupleGetItem(func_11084_call(), 0)
output = relay.Tuple([call_12523,call_12535,])
output2 = relay.Tuple([call_12524,call_12536,])
func_12558 = relay.Function([], output)
mod['func_12558'] = func_12558
mod = relay.transform.InferType()(mod)
mutated_mod['func_12558'] = func_12558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12558_call = mutated_mod.get_global_var('func_12558')
call_12559 = func_12558_call()
output = call_12559
func_12560 = relay.Function([], output)
mutated_mod['func_12560'] = func_12560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6963_call = mod.get_global_var('func_6963')
func_6964_call = mutated_mod.get_global_var('func_6964')
call_12569 = func_6963_call()
call_12570 = func_6963_call()
func_10279_call = mod.get_global_var('func_10279')
func_10280_call = mutated_mod.get_global_var('func_10280')
call_12572 = func_10279_call()
call_12573 = func_10279_call()
output = relay.Tuple([call_12569,call_12572,])
output2 = relay.Tuple([call_12570,call_12573,])
func_12595 = relay.Function([], output)
mod['func_12595'] = func_12595
mod = relay.transform.InferType()(mod)
mutated_mod['func_12595'] = func_12595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12595_call = mutated_mod.get_global_var('func_12595')
call_12596 = func_12595_call()
output = call_12596
func_12597 = relay.Function([], output)
mutated_mod['func_12597'] = func_12597
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12605 = relay.var("var_12605", dtype = "float32", shape = (11, 12, 14))#candidate|12605|(11, 12, 14)|var|float32
var_12606 = relay.var("var_12606", dtype = "float32", shape = (11, 12, 14))#candidate|12606|(11, 12, 14)|var|float32
bop_12607 = relay.maximum(var_12605.astype('float32'), relay.reshape(var_12606.astype('float32'), relay.shape_of(var_12605))) # shape=(11, 12, 14)
func_10908_call = mod.get_global_var('func_10908')
func_10909_call = mutated_mod.get_global_var('func_10909')
call_12612 = relay.TupleGetItem(func_10908_call(), 0)
call_12613 = relay.TupleGetItem(func_10909_call(), 0)
output = relay.Tuple([bop_12607,call_12612,])
output2 = relay.Tuple([bop_12607,call_12613,])
func_12615 = relay.Function([var_12605,var_12606,], output)
mod['func_12615'] = func_12615
mod = relay.transform.InferType()(mod)
var_12616 = relay.var("var_12616", dtype = "float32", shape = (11, 12, 14))#candidate|12616|(11, 12, 14)|var|float32
var_12617 = relay.var("var_12617", dtype = "float32", shape = (11, 12, 14))#candidate|12617|(11, 12, 14)|var|float32
output = func_12615(var_12616,var_12617,)
func_12618 = relay.Function([var_12616,var_12617,], output)
mutated_mod['func_12618'] = func_12618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8025_call = mod.get_global_var('func_8025')
func_8027_call = mutated_mod.get_global_var('func_8027')
call_12650 = relay.TupleGetItem(func_8025_call(), 0)
call_12651 = relay.TupleGetItem(func_8027_call(), 0)
func_5452_call = mod.get_global_var('func_5452')
func_5454_call = mutated_mod.get_global_var('func_5454')
call_12660 = func_5452_call()
call_12661 = func_5452_call()
func_9190_call = mod.get_global_var('func_9190')
func_9192_call = mutated_mod.get_global_var('func_9192')
var_12668 = relay.var("var_12668", dtype = "float32", shape = (72, 8))#candidate|12668|(72, 8)|var|float32
call_12667 = relay.TupleGetItem(func_9190_call(relay.reshape(var_12668.astype('float32'), [36, 16])), 8)
call_12669 = relay.TupleGetItem(func_9192_call(relay.reshape(var_12668.astype('float32'), [36, 16])), 8)
output = relay.Tuple([call_12650,call_12660,call_12667,var_12668,])
output2 = relay.Tuple([call_12651,call_12661,call_12669,var_12668,])
func_12679 = relay.Function([var_12668,], output)
mod['func_12679'] = func_12679
mod = relay.transform.InferType()(mod)
var_12680 = relay.var("var_12680", dtype = "float32", shape = (72, 8))#candidate|12680|(72, 8)|var|float32
output = func_12679(var_12680)
func_12681 = relay.Function([var_12680], output)
mutated_mod['func_12681'] = func_12681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8252_call = mod.get_global_var('func_8252')
func_8254_call = mutated_mod.get_global_var('func_8254')
call_12711 = relay.TupleGetItem(func_8252_call(), 2)
call_12712 = relay.TupleGetItem(func_8254_call(), 2)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_12724 = func_2428_call()
call_12725 = func_2428_call()
output = relay.Tuple([call_12711,call_12724,])
output2 = relay.Tuple([call_12712,call_12725,])
func_12768 = relay.Function([], output)
mod['func_12768'] = func_12768
mod = relay.transform.InferType()(mod)
mutated_mod['func_12768'] = func_12768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12768_call = mutated_mod.get_global_var('func_12768')
call_12769 = func_12768_call()
output = call_12769
func_12770 = relay.Function([], output)
mutated_mod['func_12770'] = func_12770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4217_call = mod.get_global_var('func_4217')
func_4219_call = mutated_mod.get_global_var('func_4219')
call_12771 = func_4217_call()
call_12772 = func_4217_call()
output = call_12771
output2 = call_12772
func_12786 = relay.Function([], output)
mod['func_12786'] = func_12786
mod = relay.transform.InferType()(mod)
mutated_mod['func_12786'] = func_12786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12786_call = mutated_mod.get_global_var('func_12786')
call_12787 = func_12786_call()
output = call_12787
func_12788 = relay.Function([], output)
mutated_mod['func_12788'] = func_12788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3370_call = mod.get_global_var('func_3370')
func_3372_call = mutated_mod.get_global_var('func_3372')
call_12794 = func_3370_call()
call_12795 = func_3370_call()
output = relay.Tuple([call_12794,])
output2 = relay.Tuple([call_12795,])
func_12804 = relay.Function([], output)
mod['func_12804'] = func_12804
mod = relay.transform.InferType()(mod)
output = func_12804()
func_12805 = relay.Function([], output)
mutated_mod['func_12805'] = func_12805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12018_call = mod.get_global_var('func_12018')
func_12019_call = mutated_mod.get_global_var('func_12019')
call_12858 = func_12018_call()
call_12859 = func_12018_call()
output = relay.Tuple([call_12858,])
output2 = relay.Tuple([call_12859,])
func_12885 = relay.Function([], output)
mod['func_12885'] = func_12885
mod = relay.transform.InferType()(mod)
output = func_12885()
func_12886 = relay.Function([], output)
mutated_mod['func_12886'] = func_12886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12227_call = mod.get_global_var('func_12227')
func_12228_call = mutated_mod.get_global_var('func_12228')
call_12936 = relay.TupleGetItem(func_12227_call(), 1)
call_12937 = relay.TupleGetItem(func_12228_call(), 1)
func_7463_call = mod.get_global_var('func_7463')
func_7464_call = mutated_mod.get_global_var('func_7464')
call_12938 = func_7463_call()
call_12939 = func_7463_call()
output = relay.Tuple([call_12936,call_12938,])
output2 = relay.Tuple([call_12937,call_12939,])
func_12940 = relay.Function([], output)
mod['func_12940'] = func_12940
mod = relay.transform.InferType()(mod)
mutated_mod['func_12940'] = func_12940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12940_call = mutated_mod.get_global_var('func_12940')
call_12941 = func_12940_call()
output = call_12941
func_12942 = relay.Function([], output)
mutated_mod['func_12942'] = func_12942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11094_call = mod.get_global_var('func_11094')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_13004 = func_11094_call()
call_13005 = func_11094_call()
func_11439_call = mod.get_global_var('func_11439')
func_11442_call = mutated_mod.get_global_var('func_11442')
var_13031 = relay.var("var_13031", dtype = "uint16", shape = (1, 440))#candidate|13031|(1, 440)|var|uint16
call_13030 = func_11439_call(relay.reshape(var_13031.astype('uint16'), [8, 5, 11]))
call_13032 = func_11439_call(relay.reshape(var_13031.astype('uint16'), [8, 5, 11]))
func_2377_call = mod.get_global_var('func_2377')
func_2383_call = mutated_mod.get_global_var('func_2383')
const_13037 = relay.const([-10,-7,6,1,1,4,10,8,4,-2,-4,1,3,4,-2,-10,-9,-5,6,-5,-3,-3,-3,-2,-8,4,-9,1,-10,-5,-5,-5,4,9,7,-5,5,1,10,6,8,-9,9,-8,7,3,10,4,7,-2,-9,5,6,5,1,-5,1,5,5,1,9,-2,10,-1,-3,-1,1,-8,2,-4,-5,2,-4,-8,-2,-1,-10,2,-2,9,7,10,6,6,1,2,10,4,3,-4,-8,8,1,10,-2,-9,-6,6,6,1,3,-5,-7,8,10,7,-9,8,4,1,4,4,10,-6,-1,6,-2,6,2,1,5,2,2,4,-7,-1,-7,-2,4,-5,-5,-10,4,6,9,-9,-5,10,2,-3,-1,7,9,4,7,8,-10,7,-4,1,-10,2,3,3,8,-2,10,4,1,3,-7,10,-9,3,-1,1,-5,9,4,1,7,10,3,9,4,-3,-2,10,9,-9,6,-4,-2,6,6,-10,1,2,-4,1,2,-10,-7,8,-2,8,6,8,6,3,-5,5,-3,-1,10,6,6,-8,6,10,-4,7,-10,-9,-3,8,-7,4,-2,8,9,-3,4,9,-9,10,-7,3,-6,-4,5,6,5,-2,7,10,-8,4,-6,1,-1,-7,10,6,4,-6,1,1,-2,-6,6,8,9,-3,-4,-10,-7,-3,-9,-6,8,2,-4,7,7,-8,9,5,7,-3,-6,7,-2,-4,-1,3,-10,9,9,1,-9,-7,4,-6,-3,1,-4,3,-1,8,-7,1,8,-3,-8,-1,3,7,1,6,4,3,8,-5,-5,10,6,1,-3,-10,-1,10,-10,-1,8,-7,7,-2,8,-5,-2,4,8,1,2,-2,2,-4,7,-5,5,1,2,8,-1,-4,9,1,5,-9,-3,9,5,10,-1,8,7,-7,-3,10,1,8,-3,-9,1,5,-1,3,-8,-7,-8,-4,-6,-5,-7,2,-8,-7,-1,9,-6,-8,-9,-2,-4,5,-4,6,-9,9,-5,-5,3,-5], dtype = "uint32")#candidate|13037|(384,)|const|uint32
var_13038 = relay.var("var_13038", dtype = "float32", shape = (16, 4))#candidate|13038|(16, 4)|var|float32
var_13039 = relay.var("var_13039", dtype = "float32", shape = (320,))#candidate|13039|(320,)|var|float32
const_13040 = relay.const([1.414904,4.582451,7.542296,-2.862772,-4.440980,-7.771099,-0.408608,-2.285581,5.359134,7.910404,1.985565,-3.018579,5.841645,-3.525115,-5.512865,6.946335,-6.250784,1.921202,0.629625,4.593686,-5.498782,4.808461,3.866705,6.931336,8.435975,-6.605337,-2.046543,-5.645735,-9.856065,4.950661,-2.095358,-6.217226,4.909386,-8.687456,6.010621,-0.657178,-5.256442,-2.011889,1.061102,-1.606200,-3.643339,0.649114,6.020422,-5.007203,-6.568565,-7.248100,-7.731290,1.663498,4.082247,-7.596924,8.909170,-8.586705,6.102994,8.043026,-1.174872,9.238826,1.913306,4.233283,-9.420243,-3.446217,9.359126,3.090661,-7.085608,6.464011,6.675318,-9.147113,-8.420291,-4.834605,-0.472539,-4.726736,6.736671,0.605960,-7.730418,-3.699212,2.522237,3.809827,9.473842,-6.801696,7.370581,7.833444,-8.543683,4.922941,-1.526205,-5.238591,-3.488876,4.953246,-7.836143,-6.818302,-5.643543,7.655844,4.869731,-3.824309,4.076111,-4.775192,4.940830,4.865424,-9.959792,-2.694760,-4.882848,9.863812,-6.788834,9.620190,2.245536,6.570976,-2.306935,0.167201,-3.340426,-0.840468,9.580583,-3.422460,2.550604,-3.464206,6.949224,-4.426323,0.886573,-8.112828,1.188723,-3.866308,4.101784,-7.264559,-2.788477,2.033166,9.058290,-9.717934,7.555028,4.213511,5.969621,-8.430697,8.394081,-0.986615,-2.932240,-2.994435,-3.211447,-2.388107,-6.192610,0.524906,0.598632,3.300367,8.389339,3.684752,7.108141,8.736943,-4.475266,8.487769,-1.861254,-4.063904,-4.229366,-3.822727,9.953231,-0.636551,2.964521,-2.213487,-5.150490,-0.559313,5.707297,-8.634455,-2.880816,5.336148,1.467961,-0.461752], dtype = "float64")#candidate|13040|(160,)|const|float64
call_13036 = relay.TupleGetItem(func_2377_call(relay.reshape(const_13037.astype('uint32'), [24, 16]), relay.reshape(var_13038.astype('float32'), [64,]), relay.reshape(var_13039.astype('float32'), [4, 80]), relay.reshape(const_13040.astype('float64'), [160,]), ), 7)
call_13041 = relay.TupleGetItem(func_2383_call(relay.reshape(const_13037.astype('uint32'), [24, 16]), relay.reshape(var_13038.astype('float32'), [64,]), relay.reshape(var_13039.astype('float32'), [4, 80]), relay.reshape(const_13040.astype('float64'), [160,]), ), 7)
output = relay.Tuple([call_13004,call_13030,var_13031,call_13036,const_13037,var_13038,var_13039,const_13040,])
output2 = relay.Tuple([call_13005,call_13032,var_13031,call_13041,const_13037,var_13038,var_13039,const_13040,])
func_13042 = relay.Function([var_13031,var_13038,var_13039,], output)
mod['func_13042'] = func_13042
mod = relay.transform.InferType()(mod)
var_13043 = relay.var("var_13043", dtype = "uint16", shape = (1, 440))#candidate|13043|(1, 440)|var|uint16
var_13044 = relay.var("var_13044", dtype = "float32", shape = (16, 4))#candidate|13044|(16, 4)|var|float32
var_13045 = relay.var("var_13045", dtype = "float32", shape = (320,))#candidate|13045|(320,)|var|float32
output = func_13042(var_13043,var_13044,var_13045,)
func_13046 = relay.Function([var_13043,var_13044,var_13045,], output)
mutated_mod['func_13046'] = func_13046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12018_call = mod.get_global_var('func_12018')
func_12019_call = mutated_mod.get_global_var('func_12019')
call_13129 = func_12018_call()
call_13130 = func_12018_call()
output = relay.Tuple([call_13129,])
output2 = relay.Tuple([call_13130,])
func_13149 = relay.Function([], output)
mod['func_13149'] = func_13149
mod = relay.transform.InferType()(mod)
mutated_mod['func_13149'] = func_13149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13149_call = mutated_mod.get_global_var('func_13149')
call_13150 = func_13149_call()
output = call_13150
func_13151 = relay.Function([], output)
mutated_mod['func_13151'] = func_13151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9788_call = mod.get_global_var('func_9788')
func_9789_call = mutated_mod.get_global_var('func_9789')
call_13213 = relay.TupleGetItem(func_9788_call(), 0)
call_13214 = relay.TupleGetItem(func_9789_call(), 0)
func_4076_call = mod.get_global_var('func_4076')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_13225 = func_4076_call()
call_13226 = func_4076_call()
output = relay.Tuple([call_13213,call_13225,])
output2 = relay.Tuple([call_13214,call_13226,])
func_13232 = relay.Function([], output)
mod['func_13232'] = func_13232
mod = relay.transform.InferType()(mod)
output = func_13232()
func_13233 = relay.Function([], output)
mutated_mod['func_13233'] = func_13233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4421_call = mod.get_global_var('func_4421')
func_4423_call = mutated_mod.get_global_var('func_4423')
call_13315 = relay.TupleGetItem(func_4421_call(), 0)
call_13316 = relay.TupleGetItem(func_4423_call(), 0)
output = relay.Tuple([call_13315,])
output2 = relay.Tuple([call_13316,])
func_13353 = relay.Function([], output)
mod['func_13353'] = func_13353
mod = relay.transform.InferType()(mod)
output = func_13353()
func_13354 = relay.Function([], output)
mutated_mod['func_13354'] = func_13354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12786_call = mod.get_global_var('func_12786')
func_12788_call = mutated_mod.get_global_var('func_12788')
call_13388 = func_12786_call()
call_13389 = func_12786_call()
func_7486_call = mod.get_global_var('func_7486')
func_7487_call = mutated_mod.get_global_var('func_7487')
call_13394 = relay.TupleGetItem(func_7486_call(), 0)
call_13395 = relay.TupleGetItem(func_7487_call(), 0)
func_5016_call = mod.get_global_var('func_5016')
func_5017_call = mutated_mod.get_global_var('func_5017')
call_13415 = relay.TupleGetItem(func_5016_call(), 1)
call_13416 = relay.TupleGetItem(func_5017_call(), 1)
output = relay.Tuple([call_13388,call_13394,call_13415,])
output2 = relay.Tuple([call_13389,call_13395,call_13416,])
func_13419 = relay.Function([], output)
mod['func_13419'] = func_13419
mod = relay.transform.InferType()(mod)
mutated_mod['func_13419'] = func_13419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13419_call = mutated_mod.get_global_var('func_13419')
call_13420 = func_13419_call()
output = call_13420
func_13421 = relay.Function([], output)
mutated_mod['func_13421'] = func_13421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8053_call = mod.get_global_var('func_8053')
func_8055_call = mutated_mod.get_global_var('func_8055')
call_13422 = relay.TupleGetItem(func_8053_call(), 0)
call_13423 = relay.TupleGetItem(func_8055_call(), 0)
func_8185_call = mod.get_global_var('func_8185')
func_8187_call = mutated_mod.get_global_var('func_8187')
call_13424 = relay.TupleGetItem(func_8185_call(), 0)
call_13425 = relay.TupleGetItem(func_8187_call(), 0)
output = relay.Tuple([call_13422,call_13424,])
output2 = relay.Tuple([call_13423,call_13425,])
func_13427 = relay.Function([], output)
mod['func_13427'] = func_13427
mod = relay.transform.InferType()(mod)
mutated_mod['func_13427'] = func_13427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13427_call = mutated_mod.get_global_var('func_13427')
call_13428 = func_13427_call()
output = call_13428
func_13429 = relay.Function([], output)
mutated_mod['func_13429'] = func_13429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4490_call = mod.get_global_var('func_4490')
func_4492_call = mutated_mod.get_global_var('func_4492')
call_13449 = relay.TupleGetItem(func_4490_call(), 1)
call_13450 = relay.TupleGetItem(func_4492_call(), 1)
func_13427_call = mod.get_global_var('func_13427')
func_13429_call = mutated_mod.get_global_var('func_13429')
call_13461 = relay.TupleGetItem(func_13427_call(), 1)
call_13462 = relay.TupleGetItem(func_13429_call(), 1)
output = relay.Tuple([call_13449,call_13461,])
output2 = relay.Tuple([call_13450,call_13462,])
func_13478 = relay.Function([], output)
mod['func_13478'] = func_13478
mod = relay.transform.InferType()(mod)
mutated_mod['func_13478'] = func_13478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13478_call = mutated_mod.get_global_var('func_13478')
call_13479 = func_13478_call()
output = call_13479
func_13480 = relay.Function([], output)
mutated_mod['func_13480'] = func_13480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8817_call = mod.get_global_var('func_8817')
func_8818_call = mutated_mod.get_global_var('func_8818')
call_13489 = relay.TupleGetItem(func_8817_call(), 0)
call_13490 = relay.TupleGetItem(func_8818_call(), 0)
output = relay.Tuple([call_13489,])
output2 = relay.Tuple([call_13490,])
func_13493 = relay.Function([], output)
mod['func_13493'] = func_13493
mod = relay.transform.InferType()(mod)
mutated_mod['func_13493'] = func_13493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13493_call = mutated_mod.get_global_var('func_13493')
call_13494 = func_13493_call()
output = call_13494
func_13495 = relay.Function([], output)
mutated_mod['func_13495'] = func_13495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7279_call = mod.get_global_var('func_7279')
func_7281_call = mutated_mod.get_global_var('func_7281')
call_13505 = relay.TupleGetItem(func_7279_call(), 1)
call_13506 = relay.TupleGetItem(func_7281_call(), 1)
output = relay.Tuple([call_13505,])
output2 = relay.Tuple([call_13506,])
func_13507 = relay.Function([], output)
mod['func_13507'] = func_13507
mod = relay.transform.InferType()(mod)
mutated_mod['func_13507'] = func_13507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13507_call = mutated_mod.get_global_var('func_13507')
call_13508 = func_13507_call()
output = call_13508
func_13509 = relay.Function([], output)
mutated_mod['func_13509'] = func_13509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6774_call = mod.get_global_var('func_6774')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_13582 = relay.TupleGetItem(func_6774_call(), 0)
call_13583 = relay.TupleGetItem(func_6775_call(), 0)
func_12270_call = mod.get_global_var('func_12270')
func_12273_call = mutated_mod.get_global_var('func_12273')
const_13585 = relay.const([5.484233,-3.509248,9.824913,-8.190282,-7.738862,-6.529676,6.782119,-0.689350,7.525867,-7.396065,-1.524185,-0.320016,4.792983,3.298308,-5.253335,-3.368396,8.734698,7.153765,3.018416,4.473192,0.259177,-6.259322,-2.994790,5.423636,9.781386,-6.219307,-5.141130,-5.837824,3.637789,-5.431776,4.039091,4.831771,-5.805690,3.301044,-8.098283,6.780828,-7.848400,2.353882,-0.460101,0.424029,-6.558117,6.467468,-7.686794,-8.767410,5.412555,9.193999,8.836259,-5.537276,3.723151,-4.710383,-7.642722,1.888295,1.627338,5.836577,4.118178,1.159541,4.893275,-0.886158,-2.765984,7.854330,-8.143670,7.419573,-7.351539,6.247744,4.773066,2.319587,0.356476,6.713293,8.892494,-7.925716,6.496052,-6.965472,1.944635,-2.820104,-9.870444,8.557940,-4.148286,-6.442269,-1.117423,-3.071629,5.618038,8.527084,-9.163729,6.800897,-7.486848,-9.268079,0.508138,-5.459359,-0.621686,6.455633,-3.344864,2.122624,3.963604,0.869984,7.581455,8.925388,-8.384575,1.872118,9.184549,-1.827843,-7.475083,9.716445,-8.411363,-9.559610,-0.160242,7.203247,2.905521,3.647172,-8.110341,-9.663410,-4.863024,2.379429,9.126543,7.765054,9.825606,-5.803911,3.160585,-2.343722,3.899830,-2.715177,-3.763419,-9.306557,-1.839734,-9.152252,2.125152,-6.890349,-2.752304,-0.704547,-0.985176,2.528007,9.375526,1.349281,8.769109,-5.525122,7.411596,2.377732,-1.889661,2.124203,1.477456,-4.561736,-2.858052,3.313803,-5.394132,-3.274355,3.875300,-1.212787,6.743663,5.232134,0.268790,1.300797,-6.796967,-4.044588,4.951156,3.094314,4.884716,4.798122,-5.623817,4.890041,-9.606635,7.369639,1.681898,-7.446630,-8.952753,7.709581,-0.365174,-1.044828,3.479071,5.622017,-9.582212,-9.057671,-3.951878,7.369229,-0.844701,9.553075,8.744238,-2.799240,5.072179,1.398351,7.156889,3.096307,-4.434572,-9.508143,3.584774,-6.836970,9.617821,3.507842,-5.903637,-8.784007,6.934181,5.049286,6.103341,9.918488,-8.226797,-7.878202,-6.522980,6.715654,6.470246,-7.489231,-0.294367,-1.226225,1.995137,0.727849,-3.102786,-5.115334,-0.604230,-8.968371,-0.792736,-7.212740,4.574234,-2.231474,-7.096854,-0.085846,7.505941,-0.016540,3.042983,0.608333,4.060696,-1.532155,7.158495,6.319733,-4.809367,3.572564,-2.480054,7.211458,-3.694087,4.376604,-2.131417,-5.958541,-8.803958,6.357473,4.642234,3.192452,8.578393,-4.751565,-5.838922,-9.056328,-9.622778,9.671360,8.368627,-5.738612,-1.666821,7.622611,1.853687,3.510911,-7.834367,0.887061,9.091680,-0.192364,-1.636601,8.700609,2.598383,8.290043,3.073018,-4.486791,0.108266,-5.928338,-6.109826,-2.175441,4.833037,9.920845,-1.018472,6.226301,5.462709,4.839233,1.411664,9.766986,-2.425153,-5.085810,2.582035,7.062550,1.486806,0.506192,5.918801,5.165501,1.775367,-5.538105,4.331421,9.313576,-5.053466,-3.410413,-7.961609,-3.596794,-2.717118,-7.441276,6.723123,-5.117231,-8.372320,-6.828106,-8.740611,-4.772338,-0.326264,4.067191,5.249769,2.971135,3.868588,1.797239,8.317623,3.987688,-5.270668,5.781021,2.202815,-7.013883,6.256166,8.629574,-1.311618,3.789958,-2.474890,-0.763794,-3.621402,9.182264,7.054710,4.915415,-1.221863,-1.750822,-7.776039,-6.203135,3.848513,2.005698,7.365598,-9.244856,6.403998,9.028182,1.162277,9.727442,8.831186,6.411044,5.563622,1.747655,2.092569,-0.579878,0.125445,3.787638,9.394878,-7.072277,3.268978,-9.016856,-9.081429,9.242876,5.222658,0.286996,7.952101,7.807617,8.781986,3.417860,-5.564590,4.237775,-8.497063,-9.787026,4.876869,5.451534,-1.185413,7.802337,8.933511,-0.387316,0.338010,7.031327,-4.200764,7.463397,5.710567,6.703033,-8.748064,7.949666,0.843019,-7.355641,-6.060590,-9.044545,3.299579,-3.503366,-2.553693,9.068089,-8.894553,-9.093900,6.666817,5.648198,-8.304270,-6.724020,3.969351,-0.308239,-6.512884,5.080493,-5.258202,3.350215,-8.276641,-4.941323,-1.664943,-8.858795,-8.500493,6.942865,7.929802,-2.521303,6.169472,-9.941932], dtype = "float64")#candidate|13585|(392,)|const|float64
call_13584 = relay.TupleGetItem(func_12270_call(relay.reshape(const_13585.astype('float64'), [392,])), 0)
call_13586 = relay.TupleGetItem(func_12273_call(relay.reshape(const_13585.astype('float64'), [392,])), 0)
func_11658_call = mod.get_global_var('func_11658')
func_11660_call = mutated_mod.get_global_var('func_11660')
call_13613 = func_11658_call()
call_13614 = func_11658_call()
output = relay.Tuple([call_13582,call_13584,const_13585,call_13613,])
output2 = relay.Tuple([call_13583,call_13586,const_13585,call_13614,])
func_13624 = relay.Function([], output)
mod['func_13624'] = func_13624
mod = relay.transform.InferType()(mod)
output = func_13624()
func_13625 = relay.Function([], output)
mutated_mod['func_13625'] = func_13625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_13658 = func_1537_call()
call_13659 = func_1537_call()
func_9517_call = mod.get_global_var('func_9517')
func_9519_call = mutated_mod.get_global_var('func_9519')
call_13672 = relay.TupleGetItem(func_9517_call(), 1)
call_13673 = relay.TupleGetItem(func_9519_call(), 1)
uop_13683 = relay.acos(call_13672.astype('float32')) # shape=(1, 546)
uop_13685 = relay.acos(call_13673.astype('float32')) # shape=(1, 546)
output = relay.Tuple([call_13658,uop_13683,])
output2 = relay.Tuple([call_13659,uop_13685,])
func_13686 = relay.Function([], output)
mod['func_13686'] = func_13686
mod = relay.transform.InferType()(mod)
output = func_13686()
func_13687 = relay.Function([], output)
mutated_mod['func_13687'] = func_13687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8964_call = mod.get_global_var('func_8964')
func_8966_call = mutated_mod.get_global_var('func_8966')
call_13725 = relay.TupleGetItem(func_8964_call(), 3)
call_13726 = relay.TupleGetItem(func_8966_call(), 3)
output = relay.Tuple([call_13725,])
output2 = relay.Tuple([call_13726,])
func_13733 = relay.Function([], output)
mod['func_13733'] = func_13733
mod = relay.transform.InferType()(mod)
mutated_mod['func_13733'] = func_13733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13733_call = mutated_mod.get_global_var('func_13733')
call_13734 = func_13733_call()
output = call_13734
func_13735 = relay.Function([], output)
mutated_mod['func_13735'] = func_13735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6105_call = mod.get_global_var('func_6105')
func_6107_call = mutated_mod.get_global_var('func_6107')
call_13752 = relay.TupleGetItem(func_6105_call(), 0)
call_13753 = relay.TupleGetItem(func_6107_call(), 0)
func_10096_call = mod.get_global_var('func_10096')
func_10099_call = mutated_mod.get_global_var('func_10099')
const_13764 = relay.const([-3,5,-3,-2,6,-5,-10,5,-2,2,-2,-4,2,4,-1,9,3,3,-7,-2,-9,-10,-8,10,3,-7,-9,-8,2,-6,8,-10,-1,6,8,-3,-4,5,-5,3,-10,-4,3,10,1,-10,-5,-9,-1,-4,-4,-5,7,10,8,-1,4,-7,-5,-2,-5,5,-1,6,-9,1,5,-2,8,6,7,-4,1,10,8,-2,4,-5,-2,-9,1,-4,7,-1,-10,-3,-6,-8,8,-5,-9,1,4,8,-9,9,-8,8,-1,-2,-10,7,-10,3,4,6,4,-9,-5,6,-6,6,10,-9,7,-3,4,10,-9,-4,2,-10,-7,-5,-6,6,10,5,-8,-2,-4,9,-8,-4,6,2,7,-2,-1,-7,-10,8,-7,-9,-7,-7,7,-1,-8,4,4,-10,7,7,1,-4,9,2,-5,10,-3,1,6,8,8,8,5,-2,1,10,-5,4,6,-3,-8,-1,1,-4,-5,-1,-2,2,6,-2,7,-9,-6,-8,1,-3,6,2,5,6,-8,-2,7,-8,10,-2,-3,9,5,4,-1,-7,-3,6,-4,-8,1,-3,-6,1,-2,-4,5,-8,3,10,-1,2,-5,1,-1,4,-3,-10,9,-6,6,9,3,6,1,3,1,7,-4,-9,-9,8,-1,10,2,4,6,-1,-1,7,3,6,-7,-1,-1,-7,7,-2,-6,10,-10,7,-8,-5,7,2,3,-3,-9,1,-7,2,-6,4,-9,-9,1,-5,6,9,-1,1,-9,2,9,9,4,1,6,-3,2,-3,9,3,7,7,4,-2,2,-4,9,-8,5,-4,-5,-7,8,1,10,-1,9,-5,-7,8,2,10,-5,6,-6,-2,-7,9,1,-5,5,7,5,6,10,-1,6,-6,8,3,-4,6,-4,-9,6,-7,9,2,8,5,-4,2,8,10,-10,1,-10,5,3,-10,-5,9,-2,9,-10,8,3,-3,8,8,-8,9,-7,1,-8,10,-9,9,-1,-1,-5,5,9,-10,3,2,-6,-9,-7,4,5,-9,2,-4,-8,-5,4,-2,10,-9,-9,-6,3,-9,-8,-4,-6,7,-4,-2,8,7,1,-4,-1,-4,3,7,-7,-4,7,10,-2,-3,10,9,5,9,-7,-7,-7,3,2,5,4,6,9,7,5,-10,-5,4,-8,6,-7,6,-3,-5,8,-6,-1,-6,-10,-6,2,1,-8,7,-7,1,-5,9,5,5,-4,-6,3,7,-4,8,8,1,-2,2,-3,-5,-2,-6,-8,2,2,-7,9,-8,-5,-7,6,1,-10,9,-5,-2,1,-4,1,-9,4,-1,7,6,-8,7,4,-5,-10,-8,1,2,9,8,-1,-6,2,8,9,-3,8,2,-9,-4,1,4,3,-3,1,6,-8,-7,-2,-2,-8,7,-7,5,5,-5,-5,-10,4,-5,-5,-6,-5,-5,-7,-9,2,-10,6,4,-7,8,7,-2,-1,5,8,-9,4,2,-1,-6,-7,-3,-4,-4,6,-4,-2,-4,-3,-9,10,-6,1,4,8,-4,-8,10,6,2,-8,6,3,2,-9,-9,-8,1,-10,1,7,-3,-6,7,-6,3,5,5,9,8,-10,-7,1,-10,-7,8,-8,-10,-5,6,6,-7,-7,1,-2,6,-5,10,2,-6,1,-4,-7,5,1,-7,-1,8,-9,-5,-7,2,-5,5,-2,-8,-4,-4,-7,7,2,-5,-8,-2,1,9,10,9,6,3,-4,3,-3,1,5,8,-1,10,-5,10,10,3,3,-3,5,-6,-7,8,-5,-8,8,8,8,-1,-10,8,-2,-10,-10,-1,1,3,-8,7,-10,2,2,7,9,4,1,-9,-2,8,-6,-8,-8,-6,-2,8,10,9,-1,4,8,-9,-2,4,1,-8,10,-7,-7,-3,-6,10,-2,-7,-7,4,9,-4,6,-4,7,6,-8,-6,-6,3,-1,-9,1,-7,-9,4,6,10,4,-1,-8,8,9,-2,-2,-8,-9,5,5,10,5,-3,-2,5,8,8,-2,-5,-10,-8,3,7,-5,4,6,-5,10,2,-2,5,-2,10,-9,6,2,-6,-4,-9,-7,8,-8,4,2,7,2,5,-7,9,10,7,-1,-6,-8,-3,-7,8,-5,-3,-8,-2,4,-4,4,7,9,5,1,-7,6,5,3,9,8,7,-2,-6,-10,-7,4,-10,10,-4,-9,-9,1,6,-7,-1,7,-1,-1,-5,-9,-7,8,7,5,10,-2,-8,-3,6,1,7,9,9,6,1,8,-10,7,6,-1,-5,7,8,10,-2,-5,-1,6,4,-5,7,3,2,7,2,-6,2,2,3,-6,-7,3,-7,9,1,6,-9,-7,1,-9,-1,1,8,5,-9,6,4,-3,10,-10,-6,-1,7,6,-2,-10,1,8,7,3,-4,10,-2,-9,-7,-3,7,-9,-10,4,-3,-6,-6,-6,-8,8,1,2,-3,4,-3,-6,-9,-7,-2,-2,5,-9,-4,3,5,-6,9,8,10,-3,-8,-3,6,7,-3,2,9,-9,6,5,-3,-6,10,6,5,-2,10,2,-9,3,8,-10,-7,-1,2,4,8,2,5,9,9,5,-1,3,-5,-2,2,-1,-2,1,8,-1,-5,-6,1,2,-7,9,-1,-7,-1,-1,-2,1,5,-8,-7,-1,4,-5,-5,4,4,-9,6,-3,-7,-9,7,3,-3,-6,1,-5,7,9,6,3,5,-5,9,9,2,-7,9,10,-2,-2,-4,-8,-4,-2,-10,-10,-6,-7,3,-5,5,2,3,-4,8,9,-3,-4,4,9,10,1,4,-5,6,-2,3,5,-7,10,-4,-9,6,6,-9,7,4,-7,6,7,-1,10,-4,9,-3,1,8,6,3,-7,7,-4,-2,1,-3,7,-7,8,-4,-7,4,6,-7,-9,6,-5,-1,-6,-9,8,-5,-6,4,6,-8,6,-8,-7,7,-5,5,-8,10,7,2,3,-2,10,4,-5,8,8,4,-2,3,-7,-9,5,10,-3,9,8,7,-1,-5,-5,10,10,1,6,-1,-4,-8,4,-1,10,2,-5,-7,2,-5,-6,10,-10,10,-5,-8,5,-8,-6,5,2,6,-6,4,-7,-5,-5,-9,-6,-10,9,-1,-6,3,-9,9,-6,9,-10,-10,-3,7,7,-10,4,5,-7,-8,-7,-6,9,-10,-2,7,-1,10,9,1,-5,1,10,-3,-4,10,3,-2,5,9,10,-1,2,-6,-9,9,7,-3,7,1,-8,5,-1,4,-6,3,-9,-8,8,-2,-8,-2,10,-1,1,8,-5,9,-9,-1,-9,2,3,-1,-3,-7,-3,-7,2,1,10,-3,2,2,-8,-8,-1,5,2,2,-8,-8,8,5,3,-7,5,9,-1,-9,-6,-6,-9,9,-4,7,-4,2,-8,3,-2,6,10,5,4,2,2,7,8,3,8,3,-2,-5,-3,4,9,-5,3,2,-3,-9,2,-8,-1,4,8,-3,-4,3,-7,3,6,6,-7,9,3,-6,-4,-9,5,6,9,-4,-8,-10,-5,-10,2,-2,-4,-10,-1,-6,-1,1,8,-9,-7,-2,3,9,-7,-9,-6,-8,6,-1,-6,-3,4,5,3,9,-1,6,-2,-10,-5,8,3,-4,-5,7,4,10,-6,-7,1,1,-4,-5,-2,-5,-5,-10,2,9,-9,-1,-6,8,-8,-3,1,-10,-10,3,-10,-1,-3,5,-5,5], dtype = "int32")#candidate|13764|(1386,)|const|int32
call_13763 = relay.TupleGetItem(func_10096_call(relay.reshape(const_13764.astype('int32'), [1386,])), 2)
call_13765 = relay.TupleGetItem(func_10099_call(relay.reshape(const_13764.astype('int32'), [1386,])), 2)
output = relay.Tuple([call_13752,call_13763,const_13764,])
output2 = relay.Tuple([call_13753,call_13765,const_13764,])
func_13767 = relay.Function([], output)
mod['func_13767'] = func_13767
mod = relay.transform.InferType()(mod)
mutated_mod['func_13767'] = func_13767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13767_call = mutated_mod.get_global_var('func_13767')
call_13768 = func_13767_call()
output = call_13768
func_13769 = relay.Function([], output)
mutated_mod['func_13769'] = func_13769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_13809 = relay.TupleGetItem(func_3507_call(), 3)
call_13810 = relay.TupleGetItem(func_3509_call(), 3)
func_10858_call = mod.get_global_var('func_10858')
func_10861_call = mutated_mod.get_global_var('func_10861')
var_13848 = relay.var("var_13848", dtype = "int16", shape = (1120,))#candidate|13848|(1120,)|var|int16
const_13849 = relay.const([-0.778908,3.366949,4.635472,-3.912494,0.245611,-6.932812,-3.997613,-9.262824,-4.301534,-8.392503,9.607606,6.951637,0.146111,9.506200,8.065140,-6.721673,-0.328018,8.939980,4.298573,7.756967,-8.270090,-7.560179,0.406567,0.775690,-6.453515,2.685602,-7.734585,8.375961,-3.284613,-7.683934,-2.319380,-9.135718,-9.424404,-0.224547,4.569146,-9.710477,-9.735264,-5.497059,1.006715,3.296052,5.436930,4.824891,8.501618,7.758450,3.708095,2.865512,-0.783184,-4.086759,7.217551,-0.009033,-9.303730,-7.939088,-0.552508,-2.512425,-5.005369,0.639968,5.908159,3.959545,-7.926165,-3.556791,-8.018662,6.563530,6.569060,1.427729,-3.837532,6.900406,-2.685788,9.467637,-8.665174,-0.341798,1.173601,8.118210,-9.961210,-7.111256,5.995826,7.901117,-5.287821,9.655311,-0.277144,1.798336,-0.423687,-1.726286,-1.583927,5.231526,3.777947,-2.518863,-8.597392,3.405254,-3.994668,5.521193,9.963822,-4.068968,6.775399,4.936155,-3.205038,-6.865739,-9.779503,-2.054980,4.677241,5.114068,1.769294,3.579083,7.515329,1.885520,-2.128474,-0.755022,8.687405,-3.522183,-4.076765,-5.179104,-8.858721,9.744283,6.868547,4.570965,-5.570219,-5.694967,-9.017586,8.018677,-6.107174,-9.719195,5.325629,-2.438885,9.281120,9.267638,4.517974,-2.667758,-1.923372,-7.253566,7.660123,-1.259874,-3.866569,-0.760178,9.676052,3.170780,-1.610393,-2.676709,-5.220324,-0.735711,2.468670,7.606158,4.975126,-9.877459,3.985967,-9.216243,1.838101,-2.210769,1.695544,-9.357267,-1.414676,-8.819933,9.027332,-5.623882,-5.964641,2.827166,-9.926774,-9.305368,6.689974,-3.860644,7.850766,2.502337,1.150433,-8.102658,-7.820958,6.069452,-5.861096,8.664628,4.277410,5.305369,-1.869046,3.861478,6.938075,7.985885,3.068200,-4.060621,-6.167201,6.579052,6.462510,-3.781005,-3.501465,3.796861,6.978742,9.801851,-9.283758,-5.066584,6.123750,-7.760859,5.418125,6.944629,5.345457,7.346099,-1.769811,5.733897,5.593039,2.706900,-2.125316,-1.666528,-8.964586,-3.136893,7.521892,0.035655,-2.816254,8.697047,9.590945,-3.531417,-2.151411,-9.306131,-8.914434,6.152727,4.531961,-8.946826,1.486918,-5.835517,-7.011901,-0.365767,3.115533,-5.610484,8.802676,-0.780520,6.395499,2.601777,-6.771054,-4.141470,-2.782552,-2.605606,-0.045733,8.575371,-3.321367,8.323179,-9.792428,-5.828696,-3.451975,8.110676,-9.964803,-6.137858,4.507644,-1.719485,-8.787835,-1.127693,-8.790116,-6.178331,6.825113,-3.746160,4.891716,-8.984645,6.050654,-1.861105,-6.882725,-1.635346,2.223167,-6.403116,-0.995317,-8.792261,0.393446,6.001671,-0.886628,-8.483458,1.192921,3.326367,9.527831,-8.880907,-1.956916,-9.880868,0.100949,6.144154,4.270641,5.971630,-1.613711,-9.871967,-7.623685,0.634394,-7.424888,6.432281,-2.535275,-1.863743,-3.482980,3.279930,3.191005,4.630609,-5.598034,6.455085,-6.394950,0.448037,9.867587,-9.447188,-5.595099,-1.614531,-5.483363,-7.987943,-1.964417,-3.379019,-8.689125,2.497220,6.436387,-6.068527,9.599012,4.971081,-8.063285,6.399514,5.260361,8.707917,1.370173,-4.948844,7.920491,5.674058,7.553890,9.109674,9.202089,-5.338880,6.435075,-9.231023,-0.806025,6.252242,-1.553945,-3.919052,-2.881279,8.089504,0.804318,8.258717,5.830866,-2.078397,-5.706008,-9.412836,-3.310104,-8.747534,6.630937,2.870245,2.337497,-1.327258,0.510711,8.572092,-1.719318,5.034768,-9.680344,7.327823,0.213042,-0.969649,3.439571,3.467385,5.866188,1.705759,-1.351920,5.596232,3.990660,-3.446544,-4.768589,8.718461,-3.679774,2.552970,9.048684,-0.582152,-2.501818,7.392003,2.559652,-8.610342,-3.503719,1.784898,-2.870942,-6.366421,-8.264367,-1.509488,-1.141480,-9.358869,-6.918011,8.113204,-7.149405,8.931132,4.384390,-6.263923,6.259774,2.219886,-1.421499,6.493153,2.441607,7.729638,-2.671438,9.524553,9.412325,2.458549,8.946607,4.977984,0.643166,-3.791219,1.395391,2.649582,5.504217,5.495807,-4.368495,-7.328842,-6.699791,6.420400,0.672075,-5.890503,-8.019717,4.814643,-8.264163,5.907786,7.199966,-8.083061,-5.910059,0.750151,9.349497,-7.345102,8.616348,4.444013,-1.581987,-4.064190,9.270223,-9.539981,5.574693,9.228842,-0.719621,3.836617,5.246318,8.719489,1.795641,7.285918,0.754010,-0.693504,2.693702,-3.356289,4.764288,3.003110,0.542162,-8.481120,9.966428,5.089460,7.698462,5.946126,-7.377672,-1.984025,-3.737531,-7.500697,9.780360,-2.659660,3.314700,-2.390563,-7.666409,0.544799,1.006062,-8.262392,-3.735244,4.078966,-5.452353,-5.512112,2.836455,-1.924858,-3.978235,5.857861,-7.608601,-1.294582,-2.528980,-4.004597,6.951991,2.912726,5.813551,4.866018,7.881562,6.379970,-7.649331,-9.920866,1.856967,6.266659,-1.390121,0.782243,-8.464803,-8.176806,8.591031,6.373416,-9.135454,2.320012,-0.124109,1.910447,3.138409,1.295520,-7.659231,4.990432,3.953350,-2.284661,8.891824,-7.073442,8.379131,2.253646,8.366937,8.736424,5.600046,9.492969,-4.249529,1.609398,-5.233285,1.109986,-1.303630,-6.181064,0.102306,1.459893,-1.266406,-6.560332,-6.054911,-4.083063,1.892779,-4.989666,7.950266,-5.641038,-9.403176,6.649338,1.752741,-0.742554,-3.143639,7.293344,3.713726,-4.255324,-1.374001,1.366279,-0.910894,-7.964592,-7.870535,-2.330501,-6.867800,2.187582,-1.324394,6.153349,7.240257,-2.926131,-5.708227,2.222661,-2.226822,-8.445318,-4.510872,-8.574336,6.422737,-7.296392,3.720150,8.867099,-2.794746,-3.913612,-7.882365,-8.250896,4.104555,6.435237,-1.304766,9.812554,-2.053756,0.801090,-9.078490,-2.717826,-3.204787,3.888045,8.963585,9.553880,3.086916,7.871415,-6.081362,8.965839,-0.499702,9.456365,1.711289,4.140000,-6.077752,-4.383891,-2.554772,6.871767,-9.991324,-7.493133,6.410439,6.658133,-0.124827,-6.686930,-2.146145,-2.717020,-9.535165,7.579089,0.561657,-1.867351,7.184601,-8.776026,2.360615,-9.693775], dtype = "float32")#candidate|13849|(576,)|const|float32
call_13847 = relay.TupleGetItem(func_10858_call(relay.reshape(var_13848.astype('int16'), [5, 14, 16]), relay.reshape(const_13849.astype('float32'), [576,]), ), 4)
call_13850 = relay.TupleGetItem(func_10861_call(relay.reshape(var_13848.astype('int16'), [5, 14, 16]), relay.reshape(const_13849.astype('float32'), [576,]), ), 4)
output = relay.Tuple([call_13809,call_13847,var_13848,const_13849,])
output2 = relay.Tuple([call_13810,call_13850,var_13848,const_13849,])
func_13860 = relay.Function([var_13848,], output)
mod['func_13860'] = func_13860
mod = relay.transform.InferType()(mod)
var_13861 = relay.var("var_13861", dtype = "int16", shape = (1120,))#candidate|13861|(1120,)|var|int16
output = func_13860(var_13861)
func_13862 = relay.Function([var_13861], output)
mutated_mod['func_13862'] = func_13862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8712_call = mod.get_global_var('func_8712')
func_8714_call = mutated_mod.get_global_var('func_8714')
call_13967 = relay.TupleGetItem(func_8712_call(), 0)
call_13968 = relay.TupleGetItem(func_8714_call(), 0)
output = relay.Tuple([call_13967,])
output2 = relay.Tuple([call_13968,])
func_13970 = relay.Function([], output)
mod['func_13970'] = func_13970
mod = relay.transform.InferType()(mod)
mutated_mod['func_13970'] = func_13970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13970_call = mutated_mod.get_global_var('func_13970')
call_13971 = func_13970_call()
output = call_13971
func_13972 = relay.Function([], output)
mutated_mod['func_13972'] = func_13972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8393_call = mod.get_global_var('func_8393')
func_8395_call = mutated_mod.get_global_var('func_8395')
call_13995 = func_8393_call()
call_13996 = func_8393_call()
func_11351_call = mod.get_global_var('func_11351')
func_11352_call = mutated_mod.get_global_var('func_11352')
call_14005 = func_11351_call()
call_14006 = func_11351_call()
func_8025_call = mod.get_global_var('func_8025')
func_8027_call = mutated_mod.get_global_var('func_8027')
call_14007 = relay.TupleGetItem(func_8025_call(), 0)
call_14008 = relay.TupleGetItem(func_8027_call(), 0)
var_14010 = relay.var("var_14010", dtype = "float64", shape = (9, 3, 13))#candidate|14010|(9, 3, 13)|var|float64
bop_14011 = relay.floor_mod(call_14005.astype('float64'), relay.reshape(var_14010.astype('float64'), relay.shape_of(call_14005))) # shape=(9, 3, 13)
bop_14014 = relay.floor_mod(call_14006.astype('float64'), relay.reshape(var_14010.astype('float64'), relay.shape_of(call_14006))) # shape=(9, 3, 13)
output = relay.Tuple([call_13995,call_14007,bop_14011,])
output2 = relay.Tuple([call_13996,call_14008,bop_14014,])
F = relay.Function([var_14010,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_14010,], output2)
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
