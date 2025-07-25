import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_48 = relay.var("var_48", dtype = "int16", shape = (6, 1, 6))#candidate|48|(6, 1, 6)|var|int16
var_49 = relay.var("var_49", dtype = "int16", shape = (6, 7, 6))#candidate|49|(6, 7, 6)|var|int16
bop_50 = relay.bitwise_xor(var_48.astype('int16'), var_49.astype('int16')) # shape=(6, 7, 6)
output = relay.Tuple([bop_50,])
output2 = relay.Tuple([bop_50,])
func_53 = relay.Function([var_48,var_49,], output)
mod['func_53'] = func_53
mod = relay.transform.InferType()(mod)
mutated_mod['func_53'] = func_53
mutated_mod = relay.transform.InferType()(mutated_mod)
func_53_call = mutated_mod.get_global_var('func_53')
var_55 = relay.var("var_55", dtype = "int16", shape = (6, 1, 6))#candidate|55|(6, 1, 6)|var|int16
var_56 = relay.var("var_56", dtype = "int16", shape = (6, 7, 6))#candidate|56|(6, 7, 6)|var|int16
call_54 = func_53_call(var_55,var_56,)
output = call_54
func_57 = relay.Function([var_55,var_56,], output)
mutated_mod['func_57'] = func_57
mutated_mod = relay.transform.InferType()(mutated_mod)
const_238 = relay.const([[[4.246690,5.232188,5.436998],[-2.455314,-2.610397,8.137668],[-0.295600,9.954939,6.653712],[-9.433918,-0.508905,-7.844107],[7.928110,-0.007693,8.443392],[8.211575,-7.924362,-5.469805],[-9.773408,-1.602883,5.692835],[-6.249535,-6.265981,5.065480],[5.060793,-9.932393,-3.572072],[-0.821166,3.941508,6.072195]],[[-8.812112,4.460604,3.864887],[1.353497,4.288580,-8.124020],[2.128410,-4.235130,0.048706],[-1.089268,7.715759,-0.085158],[8.051566,8.875692,-1.641721],[0.028179,6.777379,3.403806],[-3.138984,-7.215523,-1.940370],[-3.742987,-1.118823,1.874167],[-9.575924,-9.417181,-9.684067],[-3.348794,8.237238,8.064663]],[[-7.187229,1.918463,0.642646],[-5.941588,2.866245,6.330475],[-9.669311,6.024576,5.390447],[-6.479197,-2.576147,4.633701],[2.464140,-3.665541,-9.953091],[-9.934502,-1.113112,-3.777598],[2.401824,0.018364,-0.392245],[-8.793907,-8.036269,0.861147],[0.571610,-9.575943,-3.551221],[-6.252976,7.697811,2.235264]],[[-6.449895,-9.922399,9.291325],[0.497713,6.102097,8.594235],[0.823953,-8.805687,4.119554],[8.242818,3.091151,7.837531],[-3.123912,-7.997871,-8.881610],[7.058361,6.202995,-0.894264],[-5.879951,5.572032,-0.810893],[0.064437,6.954812,-1.077351],[5.484958,4.698934,3.538027],[3.685486,-0.843993,5.221931]],[[4.966719,-0.032320,-1.859213],[4.060350,-1.038115,-8.001125],[7.259103,-4.820838,-2.112672],[8.636370,5.591968,-0.936318],[3.723821,-9.896344,2.557045],[3.532574,-2.689547,-2.365458],[-4.466020,4.406512,-8.560309],[9.251540,-6.360646,-0.584300],[-5.600555,-1.272120,-5.976908],[-1.641036,-1.297003,-3.261166]],[[-4.699680,-5.995816,9.406549],[4.592668,-5.286569,-6.465087],[3.576130,-7.169271,5.279036],[-0.821193,4.745670,9.831462],[6.215773,1.182653,-2.480235],[-1.807168,8.932065,5.680163],[2.664373,-0.687541,-8.497272],[-2.152845,8.119139,4.147700],[-7.029500,-2.817670,-9.904847],[0.114650,-6.724800,-5.163579]],[[-0.100429,9.405424,3.718842],[-5.072159,-9.848533,5.065440],[8.196504,-7.384075,-9.139076],[-0.854340,9.861363,-8.137803],[-4.323276,4.951524,8.072849],[-2.592736,-8.191616,8.566144],[-1.214376,-6.984367,0.815112],[9.241622,-7.468432,4.564896],[7.091932,1.658961,-9.455852],[7.942904,0.884705,0.396279]],[[-2.864523,8.129135,-3.714848],[-8.855040,-3.507017,3.524259],[-8.167507,1.775975,-3.867521],[-0.289212,-1.591302,-0.707342],[5.166139,0.269286,-3.714411],[6.540649,-6.070402,-1.160841],[-5.429407,-8.483601,3.558302],[-7.590205,-5.627486,-0.899703],[-9.737475,9.633771,-5.940328],[4.598227,7.667818,5.890215]],[[-6.206146,-3.125180,5.945936],[3.164604,6.986508,-0.259524],[0.956173,9.990129,-3.741094],[-8.928858,-9.825219,4.078869],[2.499224,-1.843902,-8.076716],[-1.746826,4.998455,2.522697],[5.226509,-2.395529,-7.257907],[-1.194999,1.468783,-7.093487],[1.114446,-1.061911,-3.960676],[8.227347,-3.296727,-5.676410]],[[7.949679,6.410625,5.239044],[6.581404,8.934404,7.973278],[-8.114495,9.872662,0.988156],[-7.911287,-5.274855,-2.788503],[-8.570467,-6.723259,-7.931805],[8.031033,-8.583915,-0.992926],[-2.657417,-7.489987,4.884760],[9.545442,9.518295,7.491457],[-9.127693,-8.961489,-2.277231],[3.041996,-6.275801,8.515372]],[[-9.041168,-7.068216,-4.424295],[-0.501344,-6.647854,-7.243101],[6.056040,3.847162,5.709450],[4.359588,-1.066134,-4.402672],[5.245334,-6.206636,-2.472260],[-3.385451,-3.916870,0.708277],[3.172877,1.536793,-4.202278],[1.875564,-8.624969,0.933351],[7.911220,4.150890,-8.568106],[-3.295530,-7.370004,9.008063]],[[-7.658102,2.764001,-5.348873],[7.234822,9.317765,1.859481],[6.799153,0.595157,1.599002],[9.506291,8.742140,6.638378],[-8.135164,8.931929,-3.447878],[0.457155,-0.403287,7.875838],[9.102362,-3.253626,-0.574982],[7.290291,-8.398461,8.957013],[1.610756,-7.976024,2.472463],[-6.376217,3.969893,-2.525519]],[[-4.611335,0.940411,9.957943],[8.685577,9.715137,6.741822],[6.010309,2.532524,3.354226],[1.633417,8.061674,7.895400],[0.131003,2.498018,-9.974248],[-1.641063,7.750572,4.744256],[0.615163,-8.091055,8.296650],[-5.967152,-3.513542,-3.241669],[-5.112360,-7.729981,-5.632201],[-7.799944,3.798953,-0.186858]]], dtype = "float64")#candidate|238|(13, 10, 3)|const|float64
uop_239 = relay.rsqrt(const_238.astype('float64')) # shape=(13, 10, 3)
bop_243 = relay.mod(const_238.astype('float64'), relay.reshape(uop_239.astype('float64'), relay.shape_of(const_238))) # shape=(13, 10, 3)
const_251 = relay.const([[[-4.486726,0.615784,-4.098305],[-2.700634,-0.933903,-9.607953],[0.312880,-3.612266,-6.024211],[6.004642,1.329452,-9.294995],[-9.186101,3.764939,-3.126453],[1.300271,-8.237377,6.885815],[1.214881,-8.637640,-7.330004],[-3.946260,5.705884,-7.640261],[-8.854174,7.444164,-1.066115],[6.366014,-9.800536,2.819911]],[[-1.659078,-9.667371,7.173146],[6.955969,3.144030,-2.669707],[-0.509843,6.985692,0.416335],[1.500284,9.681974,9.022901],[7.451119,-7.559307,0.846145],[-0.194794,-0.475341,-3.997009],[-7.511565,-2.262280,8.172728],[7.034851,3.484575,-5.988207],[-3.427539,8.620217,-8.399255],[-1.968686,7.558330,-2.488143]],[[-3.217625,-2.858130,7.790383],[-4.714633,-1.536344,9.646754],[3.120873,-5.585092,5.281558],[7.621747,-7.012126,1.696492],[9.893102,-0.385731,6.811884],[8.390420,0.405230,-1.075323],[-8.096730,-9.578565,-3.317197],[-7.643289,-3.640459,-3.400620],[1.767749,-2.380358,-0.474019],[4.344878,1.291260,7.476056]],[[-7.434789,-8.142137,-4.839123],[-5.322294,2.223486,-1.666303],[-2.203203,9.629073,9.760241],[-0.266397,2.141789,-5.417375],[-8.170798,7.017333,-1.910591],[-4.747509,2.909535,-6.922837],[-1.577828,-1.195716,-5.454827],[9.606974,6.667874,7.176479],[-0.291241,-9.116040,-4.540379],[-6.482623,-6.179163,-8.397057]],[[-2.273522,8.690810,5.671659],[5.254435,-1.655673,1.878532],[-7.440303,4.951599,7.720232],[-3.622704,-5.988552,4.313289],[-8.217359,2.746220,0.937436],[0.062197,9.201705,6.668901],[-1.848457,-6.846418,-5.959913],[2.107700,-0.582143,1.579780],[-8.617709,1.963247,-6.252509],[2.816642,-1.456370,0.494371]],[[4.895639,2.049376,1.833837],[9.043623,-9.326194,-6.784466],[-0.009933,9.784017,-3.793005],[-9.005050,7.102315,0.694719],[6.898929,-9.673155,9.283214],[4.120308,-0.711620,5.560109],[-5.752109,2.024921,-0.842985],[5.735962,-0.024765,6.129578],[9.437291,7.597099,-8.413776],[-1.004349,5.936215,2.058036]],[[-3.263550,1.829824,-9.437985],[-9.706723,-9.275796,2.790784],[4.774965,7.251360,8.298781],[-0.431366,-3.735691,1.020560],[-8.252398,-1.126884,-0.078257],[4.110746,0.619753,5.183473],[4.734761,-6.343067,-9.884350],[3.025059,-7.413881,6.325623],[0.439649,0.307769,4.047817],[-5.616338,-8.657680,5.564024]],[[3.184177,-2.929798,-7.560846],[-0.081986,1.145006,6.314160],[-1.413233,-6.467093,8.823530],[-2.837298,4.712185,-4.611171],[3.405597,3.033296,-6.915127],[-6.457211,5.817934,-5.768822],[0.920021,7.799272,4.753216],[-7.039908,3.851828,-9.544906],[-9.967637,-7.811401,-9.937733],[-7.982220,1.266232,-3.477624]],[[-1.697926,5.219312,0.549814],[0.034244,-6.237952,2.530681],[8.834694,5.414348,-9.893089],[3.482120,3.823032,0.062662],[4.298925,0.728459,7.541538],[-6.626850,-9.751642,7.269982],[2.837609,-8.032750,5.876690],[3.490399,1.727740,-6.554145],[-9.437845,-1.195327,4.598140],[-1.909433,0.727239,3.427174]],[[9.021055,1.239828,-8.402495],[3.651472,1.321839,3.394139],[6.192922,-7.317817,-5.749151],[7.443230,-2.483796,-7.227508],[8.517484,-1.513206,-2.516524],[0.310162,0.911143,4.644634],[8.318127,6.830479,8.794582],[3.975262,1.800930,2.866231],[-9.435553,9.396027,0.902579],[-5.863267,-0.645756,3.261165]],[[1.171460,-0.808544,1.514311],[-5.509271,-8.199822,-1.147786],[-8.334913,-5.144665,2.607536],[3.829488,-7.157483,-9.228436],[-6.970888,-2.909214,-1.755656],[9.749007,-0.813836,-6.187429],[-9.149054,-4.950658,3.873365],[-8.863228,4.391927,7.979075],[-2.380404,-9.507867,6.769502],[-3.555238,-5.977979,-5.580277]],[[6.091880,-4.825450,7.921533],[9.881548,8.745045,-6.016956],[-7.248586,-7.306506,-5.701486],[-3.361733,0.390773,9.349043],[-5.701516,-9.061325,1.091715],[8.901916,3.382532,-2.475411],[-3.838163,-2.595931,-8.601096],[-9.208744,3.070796,-3.140642],[5.660993,-9.504555,1.466141],[6.026386,-2.461766,-6.178410]],[[5.351590,-6.384378,4.086989],[8.847972,-9.698843,2.019818],[0.400549,-7.222614,8.329797],[-6.376998,9.918504,1.335529],[-3.335686,-8.576448,-0.091427],[-8.474620,-1.262448,-1.395837],[-3.975580,-8.765791,6.856873],[8.932227,0.397408,4.006681],[-5.447383,8.743224,3.764546],[-2.193874,-8.270631,-0.090948]]], dtype = "float64")#candidate|251|(13, 10, 3)|const|float64
bop_252 = relay.greater_equal(bop_243.astype('bool'), relay.reshape(const_251.astype('bool'), relay.shape_of(bop_243))) # shape=(13, 10, 3)
bop_278 = relay.greater(uop_239.astype('bool'), relay.reshape(bop_243.astype('bool'), relay.shape_of(uop_239))) # shape=(13, 10, 3)
output = relay.Tuple([bop_252,bop_278,])
output2 = relay.Tuple([bop_252,bop_278,])
func_281 = relay.Function([], output)
mod['func_281'] = func_281
mod = relay.transform.InferType()(mod)
output = func_281()
func_282 = relay.Function([], output)
mutated_mod['func_282'] = func_282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_283 = relay.TupleGetItem(func_281_call(), 1)
call_284 = relay.TupleGetItem(func_282_call(), 1)
output = call_283
output2 = call_284
func_291 = relay.Function([], output)
mod['func_291'] = func_291
mod = relay.transform.InferType()(mod)
mutated_mod['func_291'] = func_291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_291_call = mutated_mod.get_global_var('func_291')
call_292 = func_291_call()
output = call_292
func_293 = relay.Function([], output)
mutated_mod['func_293'] = func_293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_331 = relay.TupleGetItem(func_281_call(), 0)
call_332 = relay.TupleGetItem(func_282_call(), 0)
output = call_331
output2 = call_332
func_348 = relay.Function([], output)
mod['func_348'] = func_348
mod = relay.transform.InferType()(mod)
mutated_mod['func_348'] = func_348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mutated_mod.get_global_var('func_348')
call_349 = func_348_call()
output = call_349
func_350 = relay.Function([], output)
mutated_mod['func_350'] = func_350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_435 = relay.TupleGetItem(func_281_call(), 0)
call_436 = relay.TupleGetItem(func_282_call(), 0)
output = call_435
output2 = call_436
func_443 = relay.Function([], output)
mod['func_443'] = func_443
mod = relay.transform.InferType()(mod)
output = func_443()
func_444 = relay.Function([], output)
mutated_mod['func_444'] = func_444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_443_call = mod.get_global_var('func_443')
func_444_call = mutated_mod.get_global_var('func_444')
call_485 = func_443_call()
call_486 = func_443_call()
output = call_485
output2 = call_486
func_490 = relay.Function([], output)
mod['func_490'] = func_490
mod = relay.transform.InferType()(mod)
mutated_mod['func_490'] = func_490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_490_call = mutated_mod.get_global_var('func_490')
call_491 = func_490_call()
output = call_491
func_492 = relay.Function([], output)
mutated_mod['func_492'] = func_492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_291_call = mod.get_global_var('func_291')
func_293_call = mutated_mod.get_global_var('func_293')
call_506 = func_291_call()
call_507 = func_291_call()
func_443_call = mod.get_global_var('func_443')
func_444_call = mutated_mod.get_global_var('func_444')
call_522 = func_443_call()
call_523 = func_443_call()
output = relay.Tuple([call_506,call_522,])
output2 = relay.Tuple([call_507,call_523,])
func_527 = relay.Function([], output)
mod['func_527'] = func_527
mod = relay.transform.InferType()(mod)
mutated_mod['func_527'] = func_527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_527_call = mutated_mod.get_global_var('func_527')
call_528 = func_527_call()
output = call_528
func_529 = relay.Function([], output)
mutated_mod['func_529'] = func_529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_532 = relay.TupleGetItem(func_281_call(), 0)
call_533 = relay.TupleGetItem(func_282_call(), 0)
output = call_532
output2 = call_533
func_566 = relay.Function([], output)
mod['func_566'] = func_566
mod = relay.transform.InferType()(mod)
output = func_566()
func_567 = relay.Function([], output)
mutated_mod['func_567'] = func_567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_588 = func_490_call()
call_589 = func_490_call()
output = call_588
output2 = call_589
func_596 = relay.Function([], output)
mod['func_596'] = func_596
mod = relay.transform.InferType()(mod)
output = func_596()
func_597 = relay.Function([], output)
mutated_mod['func_597'] = func_597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_350_call = mutated_mod.get_global_var('func_350')
call_617 = func_348_call()
call_618 = func_348_call()
uop_620 = relay.erf(call_617.astype('float64')) # shape=(13, 10, 3)
uop_622 = relay.erf(call_618.astype('float64')) # shape=(13, 10, 3)
uop_629 = relay.log10(uop_620.astype('float64')) # shape=(13, 10, 3)
uop_631 = relay.log10(uop_622.astype('float64')) # shape=(13, 10, 3)
func_53_call = mod.get_global_var('func_53')
func_57_call = mutated_mod.get_global_var('func_57')
const_640 = relay.const([4,8,-8,9,3,-2,3,-6,-6,-10,-6,-3,6,6,-8,4,4,7,-6,-8,2,3,-10,2,1,2,-4,4,10,5,6,-1,1,6,6,-10], dtype = "int16")#candidate|640|(36,)|const|int16
var_641 = relay.var("var_641", dtype = "int16", shape = (252,))#candidate|641|(252,)|var|int16
call_639 = relay.TupleGetItem(func_53_call(relay.reshape(const_640.astype('int16'), [6, 1, 6]), relay.reshape(var_641.astype('int16'), [6, 7, 6]), ), 0)
call_642 = relay.TupleGetItem(func_57_call(relay.reshape(const_640.astype('int16'), [6, 1, 6]), relay.reshape(var_641.astype('int16'), [6, 7, 6]), ), 0)
var_648 = relay.var("var_648", dtype = "float64", shape = (13, 10, 3))#candidate|648|(13, 10, 3)|var|float64
bop_649 = relay.bitwise_and(uop_620.astype('uint8'), relay.reshape(var_648.astype('uint8'), relay.shape_of(uop_620))) # shape=(13, 10, 3)
bop_652 = relay.bitwise_and(uop_622.astype('uint8'), relay.reshape(var_648.astype('uint8'), relay.shape_of(uop_622))) # shape=(13, 10, 3)
uop_656 = relay.cos(uop_629.astype('float32')) # shape=(13, 10, 3)
uop_658 = relay.cos(uop_631.astype('float32')) # shape=(13, 10, 3)
uop_674 = relay.cosh(uop_656.astype('float32')) # shape=(13, 10, 3)
uop_676 = relay.cosh(uop_658.astype('float32')) # shape=(13, 10, 3)
uop_683 = relay.log(uop_656.astype('float32')) # shape=(13, 10, 3)
uop_685 = relay.log(uop_658.astype('float32')) # shape=(13, 10, 3)
bop_692 = relay.logical_xor(uop_674.astype('int8'), relay.reshape(bop_649.astype('int8'), relay.shape_of(uop_674))) # shape=(13, 10, 3)
bop_695 = relay.logical_xor(uop_676.astype('int8'), relay.reshape(bop_652.astype('int8'), relay.shape_of(uop_676))) # shape=(13, 10, 3)
func_348_call = mod.get_global_var('func_348')
func_350_call = mutated_mod.get_global_var('func_350')
call_696 = func_348_call()
call_697 = func_348_call()
output = relay.Tuple([call_639,const_640,var_641,uop_683,bop_692,call_696,])
output2 = relay.Tuple([call_642,const_640,var_641,uop_685,bop_695,call_697,])
func_705 = relay.Function([var_641,var_648,], output)
mod['func_705'] = func_705
mod = relay.transform.InferType()(mod)
var_706 = relay.var("var_706", dtype = "int16", shape = (252,))#candidate|706|(252,)|var|int16
var_707 = relay.var("var_707", dtype = "float64", shape = (13, 10, 3))#candidate|707|(13, 10, 3)|var|float64
output = func_705(var_706,var_707,)
func_708 = relay.Function([var_706,var_707,], output)
mutated_mod['func_708'] = func_708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_753 = relay.TupleGetItem(func_281_call(), 1)
call_754 = relay.TupleGetItem(func_282_call(), 1)
output = call_753
output2 = call_754
func_756 = relay.Function([], output)
mod['func_756'] = func_756
mod = relay.transform.InferType()(mod)
mutated_mod['func_756'] = func_756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_756_call = mutated_mod.get_global_var('func_756')
call_757 = func_756_call()
output = call_757
func_758 = relay.Function([], output)
mutated_mod['func_758'] = func_758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_768 = relay.TupleGetItem(func_281_call(), 1)
call_769 = relay.TupleGetItem(func_282_call(), 1)
output = call_768
output2 = call_769
func_776 = relay.Function([], output)
mod['func_776'] = func_776
mod = relay.transform.InferType()(mod)
mutated_mod['func_776'] = func_776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mutated_mod.get_global_var('func_776')
call_777 = func_776_call()
output = call_777
func_778 = relay.Function([], output)
mutated_mod['func_778'] = func_778
mutated_mod = relay.transform.InferType()(mutated_mod)
var_782 = relay.var("var_782", dtype = "float64", shape = (3, 16, 4))#candidate|782|(3, 16, 4)|var|float64
var_783 = relay.var("var_783", dtype = "float64", shape = (3, 16, 4))#candidate|783|(3, 16, 4)|var|float64
bop_784 = relay.floor_divide(var_782.astype('float64'), relay.reshape(var_783.astype('float64'), relay.shape_of(var_782))) # shape=(3, 16, 4)
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_791 = func_490_call()
call_792 = func_490_call()
output = relay.Tuple([bop_784,call_791,])
output2 = relay.Tuple([bop_784,call_792,])
func_796 = relay.Function([var_782,var_783,], output)
mod['func_796'] = func_796
mod = relay.transform.InferType()(mod)
mutated_mod['func_796'] = func_796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_796_call = mutated_mod.get_global_var('func_796')
var_798 = relay.var("var_798", dtype = "float64", shape = (3, 16, 4))#candidate|798|(3, 16, 4)|var|float64
var_799 = relay.var("var_799", dtype = "float64", shape = (3, 16, 4))#candidate|799|(3, 16, 4)|var|float64
call_797 = func_796_call(var_798,var_799,)
output = call_797
func_800 = relay.Function([var_798,var_799,], output)
mutated_mod['func_800'] = func_800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_527_call = mod.get_global_var('func_527')
func_529_call = mutated_mod.get_global_var('func_529')
call_813 = relay.TupleGetItem(func_527_call(), 0)
call_814 = relay.TupleGetItem(func_529_call(), 0)
output = relay.Tuple([call_813,])
output2 = relay.Tuple([call_814,])
func_850 = relay.Function([], output)
mod['func_850'] = func_850
mod = relay.transform.InferType()(mod)
output = func_850()
func_851 = relay.Function([], output)
mutated_mod['func_851'] = func_851
mutated_mod = relay.transform.InferType()(mutated_mod)
var_991 = relay.var("var_991", dtype = "uint8", shape = (13, 9, 14))#candidate|991|(13, 9, 14)|var|uint8
var_992 = relay.var("var_992", dtype = "uint8", shape = (13, 9, 14))#candidate|992|(13, 9, 14)|var|uint8
bop_993 = relay.less_equal(var_991.astype('bool'), relay.reshape(var_992.astype('bool'), relay.shape_of(var_991))) # shape=(13, 9, 14)
output = relay.Tuple([bop_993,])
output2 = relay.Tuple([bop_993,])
func_1000 = relay.Function([var_991,var_992,], output)
mod['func_1000'] = func_1000
mod = relay.transform.InferType()(mod)
mutated_mod['func_1000'] = func_1000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1000_call = mutated_mod.get_global_var('func_1000')
var_1002 = relay.var("var_1002", dtype = "uint8", shape = (13, 9, 14))#candidate|1002|(13, 9, 14)|var|uint8
var_1003 = relay.var("var_1003", dtype = "uint8", shape = (13, 9, 14))#candidate|1003|(13, 9, 14)|var|uint8
call_1001 = func_1000_call(var_1002,var_1003,)
output = call_1001
func_1004 = relay.Function([var_1002,var_1003,], output)
mutated_mod['func_1004'] = func_1004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_1012 = relay.TupleGetItem(func_281_call(), 0)
call_1013 = relay.TupleGetItem(func_282_call(), 0)
func_527_call = mod.get_global_var('func_527')
func_529_call = mutated_mod.get_global_var('func_529')
call_1047 = relay.TupleGetItem(func_527_call(), 1)
call_1048 = relay.TupleGetItem(func_529_call(), 1)
func_443_call = mod.get_global_var('func_443')
func_444_call = mutated_mod.get_global_var('func_444')
call_1049 = func_443_call()
call_1050 = func_443_call()
output = relay.Tuple([call_1012,call_1047,call_1049,])
output2 = relay.Tuple([call_1013,call_1048,call_1050,])
func_1055 = relay.Function([], output)
mod['func_1055'] = func_1055
mod = relay.transform.InferType()(mod)
output = func_1055()
func_1056 = relay.Function([], output)
mutated_mod['func_1056'] = func_1056
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1065 = relay.var("var_1065", dtype = "uint16", shape = ())#candidate|1065|()|var|uint16
var_1066 = relay.var("var_1066", dtype = "uint16", shape = (11, 1, 14))#candidate|1066|(11, 1, 14)|var|uint16
bop_1067 = relay.bitwise_xor(var_1065.astype('uint16'), var_1066.astype('uint16')) # shape=(11, 1, 14)
output = relay.Tuple([bop_1067,])
output2 = relay.Tuple([bop_1067,])
func_1076 = relay.Function([var_1065,var_1066,], output)
mod['func_1076'] = func_1076
mod = relay.transform.InferType()(mod)
mutated_mod['func_1076'] = func_1076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1076_call = mutated_mod.get_global_var('func_1076')
var_1078 = relay.var("var_1078", dtype = "uint16", shape = ())#candidate|1078|()|var|uint16
var_1079 = relay.var("var_1079", dtype = "uint16", shape = (11, 1, 14))#candidate|1079|(11, 1, 14)|var|uint16
call_1077 = func_1076_call(var_1078,var_1079,)
output = call_1077
func_1080 = relay.Function([var_1078,var_1079,], output)
mutated_mod['func_1080'] = func_1080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_291_call = mod.get_global_var('func_291')
func_293_call = mutated_mod.get_global_var('func_293')
call_1088 = func_291_call()
call_1089 = func_291_call()
func_850_call = mod.get_global_var('func_850')
func_851_call = mutated_mod.get_global_var('func_851')
call_1125 = relay.TupleGetItem(func_850_call(), 0)
call_1126 = relay.TupleGetItem(func_851_call(), 0)
output = relay.Tuple([call_1088,call_1125,])
output2 = relay.Tuple([call_1089,call_1126,])
func_1128 = relay.Function([], output)
mod['func_1128'] = func_1128
mod = relay.transform.InferType()(mod)
output = func_1128()
func_1129 = relay.Function([], output)
mutated_mod['func_1129'] = func_1129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_566_call = mod.get_global_var('func_566')
func_567_call = mutated_mod.get_global_var('func_567')
call_1139 = func_566_call()
call_1140 = func_566_call()
output = relay.Tuple([call_1139,])
output2 = relay.Tuple([call_1140,])
func_1142 = relay.Function([], output)
mod['func_1142'] = func_1142
mod = relay.transform.InferType()(mod)
output = func_1142()
func_1143 = relay.Function([], output)
mutated_mod['func_1143'] = func_1143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_850_call = mod.get_global_var('func_850')
func_851_call = mutated_mod.get_global_var('func_851')
call_1161 = relay.TupleGetItem(func_850_call(), 0)
call_1162 = relay.TupleGetItem(func_851_call(), 0)
func_1076_call = mod.get_global_var('func_1076')
func_1080_call = mutated_mod.get_global_var('func_1080')
var_1184 = relay.var("var_1184", dtype = "uint16", shape = ())#candidate|1184|()|var|uint16
var_1185 = relay.var("var_1185", dtype = "uint16", shape = (154,))#candidate|1185|(154,)|var|uint16
call_1183 = relay.TupleGetItem(func_1076_call(relay.reshape(var_1184.astype('uint16'), []), relay.reshape(var_1185.astype('uint16'), [11, 1, 14]), ), 0)
call_1186 = relay.TupleGetItem(func_1080_call(relay.reshape(var_1184.astype('uint16'), []), relay.reshape(var_1185.astype('uint16'), [11, 1, 14]), ), 0)
bop_1194 = relay.add(var_1184.astype('int64'), call_1161.astype('int64')) # shape=(13, 10, 3)
bop_1197 = relay.add(var_1184.astype('int64'), call_1162.astype('int64')) # shape=(13, 10, 3)
output = relay.Tuple([call_1183,var_1185,bop_1194,])
output2 = relay.Tuple([call_1186,var_1185,bop_1197,])
func_1198 = relay.Function([var_1184,var_1185,], output)
mod['func_1198'] = func_1198
mod = relay.transform.InferType()(mod)
mutated_mod['func_1198'] = func_1198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1198_call = mutated_mod.get_global_var('func_1198')
var_1200 = relay.var("var_1200", dtype = "uint16", shape = ())#candidate|1200|()|var|uint16
var_1201 = relay.var("var_1201", dtype = "uint16", shape = (154,))#candidate|1201|(154,)|var|uint16
call_1199 = func_1198_call(var_1200,var_1201,)
output = call_1199
func_1202 = relay.Function([var_1200,var_1201,], output)
mutated_mod['func_1202'] = func_1202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1142_call = mod.get_global_var('func_1142')
func_1143_call = mutated_mod.get_global_var('func_1143')
call_1217 = relay.TupleGetItem(func_1142_call(), 0)
call_1218 = relay.TupleGetItem(func_1143_call(), 0)
func_756_call = mod.get_global_var('func_756')
func_758_call = mutated_mod.get_global_var('func_758')
call_1227 = func_756_call()
call_1228 = func_756_call()
output = relay.Tuple([call_1217,call_1227,])
output2 = relay.Tuple([call_1218,call_1228,])
func_1232 = relay.Function([], output)
mod['func_1232'] = func_1232
mod = relay.transform.InferType()(mod)
output = func_1232()
func_1233 = relay.Function([], output)
mutated_mod['func_1233'] = func_1233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_596_call = mod.get_global_var('func_596')
func_597_call = mutated_mod.get_global_var('func_597')
call_1245 = func_596_call()
call_1246 = func_596_call()
var_1257 = relay.var("var_1257", dtype = "bool", shape = (13, 10, 3))#candidate|1257|(13, 10, 3)|var|bool
bop_1258 = relay.divide(call_1245.astype('float32'), relay.reshape(var_1257.astype('float32'), relay.shape_of(call_1245))) # shape=(13, 10, 3)
bop_1261 = relay.divide(call_1246.astype('float32'), relay.reshape(var_1257.astype('float32'), relay.shape_of(call_1246))) # shape=(13, 10, 3)
output = bop_1258
output2 = bop_1261
func_1264 = relay.Function([var_1257,], output)
mod['func_1264'] = func_1264
mod = relay.transform.InferType()(mod)
var_1265 = relay.var("var_1265", dtype = "bool", shape = (13, 10, 3))#candidate|1265|(13, 10, 3)|var|bool
output = func_1264(var_1265)
func_1266 = relay.Function([var_1265], output)
mutated_mod['func_1266'] = func_1266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_1301 = relay.TupleGetItem(func_281_call(), 0)
call_1302 = relay.TupleGetItem(func_282_call(), 0)
output = call_1301
output2 = call_1302
func_1305 = relay.Function([], output)
mod['func_1305'] = func_1305
mod = relay.transform.InferType()(mod)
mutated_mod['func_1305'] = func_1305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1305_call = mutated_mod.get_global_var('func_1305')
call_1306 = func_1305_call()
output = call_1306
func_1307 = relay.Function([], output)
mutated_mod['func_1307'] = func_1307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_1320 = relay.TupleGetItem(func_1128_call(), 0)
call_1321 = relay.TupleGetItem(func_1129_call(), 0)
uop_1336 = relay.acos(call_1320.astype('float32')) # shape=(13, 10, 3)
uop_1338 = relay.acos(call_1321.astype('float32')) # shape=(13, 10, 3)
output = relay.Tuple([uop_1336,])
output2 = relay.Tuple([uop_1338,])
func_1350 = relay.Function([], output)
mod['func_1350'] = func_1350
mod = relay.transform.InferType()(mod)
mutated_mod['func_1350'] = func_1350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1350_call = mutated_mod.get_global_var('func_1350')
call_1351 = func_1350_call()
output = call_1351
func_1352 = relay.Function([], output)
mutated_mod['func_1352'] = func_1352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1305_call = mod.get_global_var('func_1305')
func_1307_call = mutated_mod.get_global_var('func_1307')
call_1358 = func_1305_call()
call_1359 = func_1305_call()
output = relay.Tuple([call_1358,])
output2 = relay.Tuple([call_1359,])
func_1365 = relay.Function([], output)
mod['func_1365'] = func_1365
mod = relay.transform.InferType()(mod)
output = func_1365()
func_1366 = relay.Function([], output)
mutated_mod['func_1366'] = func_1366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_1367 = func_776_call()
call_1368 = func_776_call()
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_1384 = relay.TupleGetItem(func_1055_call(), 1)
call_1385 = relay.TupleGetItem(func_1056_call(), 1)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_1392 = relay.TupleGetItem(func_281_call(), 0)
call_1393 = relay.TupleGetItem(func_282_call(), 0)
output = relay.Tuple([call_1367,call_1384,call_1392,])
output2 = relay.Tuple([call_1368,call_1385,call_1393,])
func_1394 = relay.Function([], output)
mod['func_1394'] = func_1394
mod = relay.transform.InferType()(mod)
mutated_mod['func_1394'] = func_1394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1394_call = mutated_mod.get_global_var('func_1394')
call_1395 = func_1394_call()
output = call_1395
func_1396 = relay.Function([], output)
mutated_mod['func_1396'] = func_1396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_850_call = mod.get_global_var('func_850')
func_851_call = mutated_mod.get_global_var('func_851')
call_1464 = relay.TupleGetItem(func_850_call(), 0)
call_1465 = relay.TupleGetItem(func_851_call(), 0)
output = call_1464
output2 = call_1465
func_1468 = relay.Function([], output)
mod['func_1468'] = func_1468
mod = relay.transform.InferType()(mod)
mutated_mod['func_1468'] = func_1468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1468_call = mutated_mod.get_global_var('func_1468')
call_1469 = func_1468_call()
output = call_1469
func_1470 = relay.Function([], output)
mutated_mod['func_1470'] = func_1470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_443_call = mod.get_global_var('func_443')
func_444_call = mutated_mod.get_global_var('func_444')
call_1544 = func_443_call()
call_1545 = func_443_call()
func_1264_call = mod.get_global_var('func_1264')
func_1266_call = mutated_mod.get_global_var('func_1266')
call_1547 = func_1264_call(relay.reshape(call_1544.astype('bool'), [13, 10, 3]))
call_1548 = func_1264_call(relay.reshape(call_1544.astype('bool'), [13, 10, 3]))
func_1394_call = mod.get_global_var('func_1394')
func_1396_call = mutated_mod.get_global_var('func_1396')
call_1553 = relay.TupleGetItem(func_1394_call(), 0)
call_1554 = relay.TupleGetItem(func_1396_call(), 0)
func_705_call = mod.get_global_var('func_705')
func_708_call = mutated_mod.get_global_var('func_708')
const_1559 = relay.const([-9,6,-7,1,-10,-5,-6,-3,-8,-3,1,-6,-2,-4,-1,-10,-10,-8,-5,8,-6,4,-5,-3,5,7,-5,8,-10,-4,7,-1,-2,5,6,3,-6,3,5,4,2,-8,6,4,6,9,4,4,9,-3,3,-8,-2,-2,-5,-7,-8,5,8,-4,-7,-2,2,-7,5,7,-6,9,-4,-7,7,-7,8,1,-3,-4,7,-3,2,-10,-10,3,10,5,2,4,-7,-4,-4,3,-1,10,-3,-7,-1,-9,3,-8,-5,8,7,7,-4,-9,8,-8,8,-7,10,-5,-10,-3,-8,6,4,-1,8,2,-10,2,2,-9,9,1,-9,-10,1,-1,-4,2,-3,-8,-2,-4,-3,2,-8,6,-4,-7,-3,1,-2,-1,-1,6,-6,4,-7,2,-5,-5,-5,2,-8,-4,10,5,8,-10,-8,3,-1,4,7,5,-10,5,-3,-5,-8,4,-4,9,4,1,4,-8,2,2,-7,1,9,-3,5,-5,-8,-10,-7,-4,-8,5,-10,-8,6,-2,-9,2,-1,2,4,-8,6,5,-6,-6,-8,6,-5,-10,4,-6,7,1,-3,-3,-10,-9,8,2,7,-8,-1,2,-1,-9,-6,-10,-2,-10,-3,2,-1,-2,9,3,-3,8,7,10,-2,-7,-5,-1,7,2,4,7,-8,-4,-2,2], dtype = "int16")#candidate|1559|(252,)|const|int16
call_1558 = relay.TupleGetItem(func_705_call(relay.reshape(const_1559.astype('int16'), [252,]), relay.reshape(call_1553.astype('float64'), [13, 10, 3]), ), 1)
call_1560 = relay.TupleGetItem(func_708_call(relay.reshape(const_1559.astype('int16'), [252,]), relay.reshape(call_1553.astype('float64'), [13, 10, 3]), ), 1)
func_53_call = mod.get_global_var('func_53')
func_57_call = mutated_mod.get_global_var('func_57')
call_1572 = relay.TupleGetItem(func_53_call(relay.reshape(call_1558.astype('int16'), [6, 1, 6]), relay.reshape(const_1559.astype('int16'), [6, 7, 6]), ), 0)
call_1573 = relay.TupleGetItem(func_57_call(relay.reshape(call_1558.astype('int16'), [6, 1, 6]), relay.reshape(const_1559.astype('int16'), [6, 7, 6]), ), 0)
output = relay.Tuple([call_1544,call_1547,call_1553,call_1558,const_1559,call_1572,])
output2 = relay.Tuple([call_1545,call_1548,call_1554,call_1560,const_1559,call_1573,])
func_1574 = relay.Function([], output)
mod['func_1574'] = func_1574
mod = relay.transform.InferType()(mod)
mutated_mod['func_1574'] = func_1574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mutated_mod.get_global_var('func_1574')
call_1575 = func_1574_call()
output = call_1575
func_1576 = relay.Function([], output)
mutated_mod['func_1576'] = func_1576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_1593 = relay.TupleGetItem(func_1128_call(), 1)
call_1594 = relay.TupleGetItem(func_1129_call(), 1)
func_705_call = mod.get_global_var('func_705')
func_708_call = mutated_mod.get_global_var('func_708')
const_1596 = relay.const([-2,8,8,5,-8,8,10,7,10,-3,-9,-1,-4,2,-2,4,10,4,-7,-3,9,-2,-3,-10,-10,7,7,-10,4,10,9,-10,7,6,2,-8,3,7,-3,-1,9,10,-8,8,6,-8,4,-1,1,-5,-9,3,7,7,8,-10,-6,4,3,-7,-1,-4,-10,-6,-4,-3,7,4,7,-1,9,-1,-2,-8,8,5,-8,-6,4,3,-6,1,-4,5,-6,4,10,10,-2,-8,-4,4,4,4,4,7,4,3,-5,-7,7,-6,-1,-10,7,-7,-2,2,-1,-5,-4,6,2,-3,-10,-10,6,-5,-4,-1,-4,9,9,4,-10,6,-3,1,4,4,6,2,-10,10,3,-5,8,-4,9,-7,-9,4,-9,-9,9,-8,7,-9,-10,-3,10,9,3,-5,3,3,8,6,-2,-10,-8,10,-2,-6,-9,5,-8,7,10,-6,-5,5,-8,-1,-5,1,-1,3,-1,-8,-8,8,-9,-9,-7,4,-6,3,1,4,7,1,8,3,-3,-8,4,-8,10,-4,2,7,8,-2,6,-2,1,10,9,9,-4,2,-2,1,-6,7,2,8,5,-6,5,-5,3,-8,-1,-4,-1,-3,7,-4,-8,2,6,9,-9,-6,4,1,-7,2,3,2,-2,-8,8,3,5,-5,3,-4,-8,-7], dtype = "int16")#candidate|1596|(252,)|const|int16
call_1595 = relay.TupleGetItem(func_705_call(relay.reshape(const_1596.astype('int16'), [252,]), relay.reshape(call_1593.astype('float64'), [13, 10, 3]), ), 4)
call_1597 = relay.TupleGetItem(func_708_call(relay.reshape(const_1596.astype('int16'), [252,]), relay.reshape(call_1593.astype('float64'), [13, 10, 3]), ), 4)
var_1610 = relay.var("var_1610", dtype = "int8", shape = (13, 10, 3))#candidate|1610|(13, 10, 3)|var|int8
bop_1611 = relay.bitwise_or(call_1595.astype('uint8'), relay.reshape(var_1610.astype('uint8'), relay.shape_of(call_1595))) # shape=(13, 10, 3)
bop_1614 = relay.bitwise_or(call_1597.astype('uint8'), relay.reshape(var_1610.astype('uint8'), relay.shape_of(call_1597))) # shape=(13, 10, 3)
bop_1626 = relay.multiply(call_1595.astype('uint32'), relay.reshape(call_1593.astype('uint32'), relay.shape_of(call_1595))) # shape=(13, 10, 3)
bop_1629 = relay.multiply(call_1597.astype('uint32'), relay.reshape(call_1594.astype('uint32'), relay.shape_of(call_1597))) # shape=(13, 10, 3)
output = relay.Tuple([const_1596,bop_1611,bop_1626,])
output2 = relay.Tuple([const_1596,bop_1614,bop_1629,])
func_1638 = relay.Function([var_1610,], output)
mod['func_1638'] = func_1638
mod = relay.transform.InferType()(mod)
var_1639 = relay.var("var_1639", dtype = "int8", shape = (13, 10, 3))#candidate|1639|(13, 10, 3)|var|int8
output = func_1638(var_1639)
func_1640 = relay.Function([var_1639], output)
mutated_mod['func_1640'] = func_1640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_350_call = mutated_mod.get_global_var('func_350')
call_1708 = func_348_call()
call_1709 = func_348_call()
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_1716 = relay.TupleGetItem(func_1638_call(relay.reshape(call_1708.astype('int8'), [13, 10, 3])), 0)
call_1717 = relay.TupleGetItem(func_1640_call(relay.reshape(call_1708.astype('int8'), [13, 10, 3])), 0)
func_53_call = mod.get_global_var('func_53')
func_57_call = mutated_mod.get_global_var('func_57')
const_1720 = relay.const([-6,10,3,-4,-7,-5,4,10,-9,-4,1,3,2,3,5,3,1,1,-3,-10,-1,-7,2,2,10,-6,-5,-4,-1,2,1,9,3,5,-4,-8], dtype = "int16")#candidate|1720|(36,)|const|int16
call_1719 = relay.TupleGetItem(func_53_call(relay.reshape(const_1720.astype('int16'), [6, 1, 6]), relay.reshape(call_1716.astype('int16'), [6, 7, 6]), ), 0)
call_1721 = relay.TupleGetItem(func_57_call(relay.reshape(const_1720.astype('int16'), [6, 1, 6]), relay.reshape(call_1716.astype('int16'), [6, 7, 6]), ), 0)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_1724 = relay.TupleGetItem(func_1128_call(), 1)
call_1725 = relay.TupleGetItem(func_1129_call(), 1)
output = relay.Tuple([call_1708,call_1716,call_1719,const_1720,call_1724,])
output2 = relay.Tuple([call_1709,call_1717,call_1721,const_1720,call_1725,])
func_1736 = relay.Function([], output)
mod['func_1736'] = func_1736
mod = relay.transform.InferType()(mod)
mutated_mod['func_1736'] = func_1736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1736_call = mutated_mod.get_global_var('func_1736')
call_1737 = func_1736_call()
output = call_1737
func_1738 = relay.Function([], output)
mutated_mod['func_1738'] = func_1738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1350_call = mod.get_global_var('func_1350')
func_1352_call = mutated_mod.get_global_var('func_1352')
call_1739 = relay.TupleGetItem(func_1350_call(), 0)
call_1740 = relay.TupleGetItem(func_1352_call(), 0)
output = call_1739
output2 = call_1740
func_1752 = relay.Function([], output)
mod['func_1752'] = func_1752
mod = relay.transform.InferType()(mod)
mutated_mod['func_1752'] = func_1752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1752_call = mutated_mod.get_global_var('func_1752')
call_1753 = func_1752_call()
output = call_1753
func_1754 = relay.Function([], output)
mutated_mod['func_1754'] = func_1754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1142_call = mod.get_global_var('func_1142')
func_1143_call = mutated_mod.get_global_var('func_1143')
call_1757 = relay.TupleGetItem(func_1142_call(), 0)
call_1758 = relay.TupleGetItem(func_1143_call(), 0)
output = call_1757
output2 = call_1758
func_1759 = relay.Function([], output)
mod['func_1759'] = func_1759
mod = relay.transform.InferType()(mod)
mutated_mod['func_1759'] = func_1759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mutated_mod.get_global_var('func_1759')
call_1760 = func_1759_call()
output = call_1760
func_1761 = relay.Function([], output)
mutated_mod['func_1761'] = func_1761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_1762 = relay.TupleGetItem(func_1574_call(), 3)
call_1763 = relay.TupleGetItem(func_1576_call(), 3)
output = call_1762
output2 = call_1763
func_1764 = relay.Function([], output)
mod['func_1764'] = func_1764
mod = relay.transform.InferType()(mod)
mutated_mod['func_1764'] = func_1764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1764_call = mutated_mod.get_global_var('func_1764')
call_1765 = func_1764_call()
output = call_1765
func_1766 = relay.Function([], output)
mutated_mod['func_1766'] = func_1766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_1776 = func_776_call()
call_1777 = func_776_call()
output = call_1776
output2 = call_1777
func_1804 = relay.Function([], output)
mod['func_1804'] = func_1804
mod = relay.transform.InferType()(mod)
mutated_mod['func_1804'] = func_1804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1804_call = mutated_mod.get_global_var('func_1804')
call_1805 = func_1804_call()
output = call_1805
func_1806 = relay.Function([], output)
mutated_mod['func_1806'] = func_1806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_1815 = relay.TupleGetItem(func_1055_call(), 1)
call_1816 = relay.TupleGetItem(func_1056_call(), 1)
output = call_1815
output2 = call_1816
func_1823 = relay.Function([], output)
mod['func_1823'] = func_1823
mod = relay.transform.InferType()(mod)
mutated_mod['func_1823'] = func_1823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mutated_mod.get_global_var('func_1823')
call_1824 = func_1823_call()
output = call_1824
func_1825 = relay.Function([], output)
mutated_mod['func_1825'] = func_1825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_850_call = mod.get_global_var('func_850')
func_851_call = mutated_mod.get_global_var('func_851')
call_1839 = relay.TupleGetItem(func_850_call(), 0)
call_1840 = relay.TupleGetItem(func_851_call(), 0)
output = call_1839
output2 = call_1840
func_1850 = relay.Function([], output)
mod['func_1850'] = func_1850
mod = relay.transform.InferType()(mod)
output = func_1850()
func_1851 = relay.Function([], output)
mutated_mod['func_1851'] = func_1851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1736_call = mod.get_global_var('func_1736')
func_1738_call = mutated_mod.get_global_var('func_1738')
call_1877 = relay.TupleGetItem(func_1736_call(), 1)
call_1878 = relay.TupleGetItem(func_1738_call(), 1)
func_1759_call = mod.get_global_var('func_1759')
func_1761_call = mutated_mod.get_global_var('func_1761')
call_1891 = func_1759_call()
call_1892 = func_1759_call()
output = relay.Tuple([call_1877,call_1891,])
output2 = relay.Tuple([call_1878,call_1892,])
func_1894 = relay.Function([], output)
mod['func_1894'] = func_1894
mod = relay.transform.InferType()(mod)
mutated_mod['func_1894'] = func_1894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1894_call = mutated_mod.get_global_var('func_1894')
call_1895 = func_1894_call()
output = call_1895
func_1896 = relay.Function([], output)
mutated_mod['func_1896'] = func_1896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_1913 = func_1823_call()
call_1914 = func_1823_call()
func_1394_call = mod.get_global_var('func_1394')
func_1396_call = mutated_mod.get_global_var('func_1396')
call_1923 = relay.TupleGetItem(func_1394_call(), 0)
call_1924 = relay.TupleGetItem(func_1396_call(), 0)
func_1764_call = mod.get_global_var('func_1764')
func_1766_call = mutated_mod.get_global_var('func_1766')
call_1926 = func_1764_call()
call_1927 = func_1764_call()
func_1764_call = mod.get_global_var('func_1764')
func_1766_call = mutated_mod.get_global_var('func_1766')
call_1942 = func_1764_call()
call_1943 = func_1764_call()
output = relay.Tuple([call_1913,call_1923,call_1926,call_1942,])
output2 = relay.Tuple([call_1914,call_1924,call_1927,call_1943,])
func_1949 = relay.Function([], output)
mod['func_1949'] = func_1949
mod = relay.transform.InferType()(mod)
output = func_1949()
func_1950 = relay.Function([], output)
mutated_mod['func_1950'] = func_1950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1394_call = mod.get_global_var('func_1394')
func_1396_call = mutated_mod.get_global_var('func_1396')
call_1951 = relay.TupleGetItem(func_1394_call(), 1)
call_1952 = relay.TupleGetItem(func_1396_call(), 1)
output = call_1951
output2 = call_1952
func_1960 = relay.Function([], output)
mod['func_1960'] = func_1960
mod = relay.transform.InferType()(mod)
output = func_1960()
func_1961 = relay.Function([], output)
mutated_mod['func_1961'] = func_1961
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1970 = relay.var("var_1970", dtype = "float64", shape = ())#candidate|1970|()|var|float64
var_1971 = relay.var("var_1971", dtype = "float64", shape = (5, 8, 10))#candidate|1971|(5, 8, 10)|var|float64
bop_1972 = relay.mod(var_1970.astype('float64'), var_1971.astype('float64')) # shape=(5, 8, 10)
func_596_call = mod.get_global_var('func_596')
func_597_call = mutated_mod.get_global_var('func_597')
call_1981 = func_596_call()
call_1982 = func_596_call()
output = relay.Tuple([bop_1972,call_1981,])
output2 = relay.Tuple([bop_1972,call_1982,])
func_1983 = relay.Function([var_1970,var_1971,], output)
mod['func_1983'] = func_1983
mod = relay.transform.InferType()(mod)
var_1984 = relay.var("var_1984", dtype = "float64", shape = ())#candidate|1984|()|var|float64
var_1985 = relay.var("var_1985", dtype = "float64", shape = (5, 8, 10))#candidate|1985|(5, 8, 10)|var|float64
output = func_1983(var_1984,var_1985,)
func_1986 = relay.Function([var_1984,var_1985,], output)
mutated_mod['func_1986'] = func_1986
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2002 = relay.const([[[-0.682702,3.776994,-9.931512,-4.338931,-2.762792,-5.823661,-8.243412,-4.187425,6.590024],[-6.738181,5.939754,7.854939,1.680296,-4.739731,5.338346,5.803343,-6.402551,6.691104]],[[-1.835810,-9.149649,5.923278,6.800529,0.816501,-1.469523,-2.384064,-9.108137,5.136306],[9.795967,3.646907,4.281654,-2.774252,-0.995194,6.622149,8.872632,-0.775106,8.045294]],[[-2.884703,0.006308,-9.017417,-2.209391,3.506817,-4.241073,-3.138544,2.767518,6.301088],[8.825820,5.004198,4.385034,0.767427,-3.436998,-4.374959,3.820675,-0.868884,-1.722636]],[[-2.219438,1.214451,0.172417,1.203098,-1.068493,3.355965,2.657506,8.536377,3.014544],[-6.007531,6.209642,-7.121084,-9.698438,-9.366826,-9.991512,0.399182,-5.440008,-2.469922]],[[-5.605555,2.990898,-9.410590,1.153057,7.770261,-9.324123,3.068040,-1.074253,6.141700],[-4.928963,-5.166972,-9.210866,-8.401264,-7.498316,2.587059,-8.318928,-5.333318,-3.464053]],[[1.966406,-4.935598,-6.500882,7.660851,0.638234,-6.750446,-0.264727,-0.125642,4.812576],[8.253684,-3.065536,-1.200688,3.241777,-7.699989,0.790282,-1.605831,-5.928272,0.370492]],[[-8.531604,-4.154152,-2.418585,-0.472930,3.614037,-8.970308,-5.687713,-1.639183,1.246659],[-5.572569,-9.795768,-4.128601,4.126074,-1.852769,5.209189,-1.436820,-0.707054,-2.076435]],[[5.091791,0.305227,3.347629,5.128234,6.810851,5.530426,9.362303,0.050165,-9.084918],[2.809233,6.780544,4.106606,5.215268,-0.868759,-6.421606,5.397449,0.178977,-5.569062]],[[-3.729809,-4.185454,-2.786784,-8.362626,3.049893,7.753625,9.338076,8.154903,-3.138545],[9.092773,-5.529537,8.165990,-8.235357,-3.787403,0.943814,6.354536,9.837898,1.879118]],[[6.074328,5.546927,-5.886569,-8.660142,7.901884,-5.790045,-2.474101,1.028901,3.579140],[9.638687,3.804636,3.275445,-7.894346,-2.715919,0.868827,5.627004,2.695748,2.774250]],[[0.932333,3.668645,-7.022350,-1.939102,-3.321024,1.452509,-9.654805,3.179607,6.641918],[-3.283332,6.170782,2.277948,4.680453,4.587482,5.215368,-4.463904,-4.083970,5.440930]],[[8.694050,3.644648,8.899500,6.990194,1.646072,-6.816729,1.411021,1.189461,5.520314],[8.857032,4.179238,-3.172341,-5.088056,-6.455509,-9.401551,1.633769,2.802707,7.704970]]], dtype = "float32")#candidate|2002|(12, 2, 9)|const|float32
const_2003 = relay.const([[[6.645378,-4.186913,6.620362,-4.458884,-7.052488,5.050281,-4.805938,8.607240,4.883016],[0.776530,-3.972350,4.953763,5.091313,5.131053,-3.097423,6.600497,9.361882,3.076064]],[[-6.467273,8.684103,8.283324,-7.958644,-9.610582,-1.688899,6.869770,2.017365,-7.005739],[6.667309,6.897120,-6.344295,-2.793014,4.142251,3.700119,-4.417837,1.316855,1.313045]],[[4.940504,-5.719117,3.871436,9.098826,9.642018,-3.140813,-8.387625,6.154059,-4.163213],[1.391828,-5.431340,5.379521,6.553167,6.329832,9.980864,9.731586,-5.362608,-0.161337]],[[1.265599,2.693671,-2.541941,-8.936718,6.425704,3.674226,6.740653,-2.518193,9.501769],[-1.510125,-9.376843,7.334388,-9.749048,-0.654736,5.402673,-0.336123,-9.896430,7.901116]],[[1.741807,2.763140,4.447596,0.589905,3.227659,-6.226714,5.575638,8.326257,-7.723924],[7.380930,-3.789346,-9.941135,6.502920,-3.575705,-7.937175,-2.078500,7.977414,-9.061279]],[[-6.426911,6.336010,-4.156522,1.619201,-4.441675,9.659002,8.199217,5.557523,-9.950914],[9.951609,-2.053078,0.024250,3.787824,8.334026,-6.852398,-8.779093,9.556956,-7.216357]],[[2.079174,9.371269,5.182063,8.999341,5.751828,-2.561485,-1.433231,6.143212,6.446937],[8.223685,8.819530,2.106213,-9.773037,-1.592573,5.231554,4.857487,-5.576812,2.659055]],[[6.732546,4.841808,4.763440,-9.185686,9.146354,3.208809,2.581421,-7.011645,6.327064],[-3.704730,0.688518,6.444697,3.778038,3.959497,7.170688,1.525626,4.231762,3.311451]],[[-0.618178,-5.553960,-7.715067,-2.617274,-9.630680,-3.366864,-8.516758,-0.913590,4.468528],[3.345032,-2.125587,6.061152,9.541548,4.093762,3.608217,3.720576,-2.311306,2.650914]],[[7.281389,-0.055348,-3.153485,3.347393,0.157956,-0.580606,9.021660,-6.590143,5.390541],[5.097599,-6.361009,1.544076,-0.393703,-9.448166,8.224924,8.789117,1.342437,-1.423680]],[[-6.239015,2.104971,8.752007,-3.826306,8.342028,7.704751,-3.686501,3.294934,7.955163],[-4.822734,9.195289,-5.651646,5.308669,-6.969382,-1.270001,-7.339895,-7.198134,-7.836332]],[[-2.454557,6.281642,5.677136,-9.376027,1.102850,4.477197,-3.360586,-8.729997,-7.408416],[-2.430466,-2.517383,-2.778634,-7.214374,3.543599,-4.382414,-6.643851,1.908869,-6.794770]]], dtype = "float32")#candidate|2003|(12, 2, 9)|const|float32
bop_2004 = relay.power(const_2002.astype('float32'), relay.reshape(const_2003.astype('float32'), relay.shape_of(const_2002))) # shape=(12, 2, 9)
uop_2008 = relay.erf(const_2002.astype('float32')) # shape=(12, 2, 9)
output = relay.Tuple([bop_2004,uop_2008,])
output2 = relay.Tuple([bop_2004,uop_2008,])
func_2012 = relay.Function([], output)
mod['func_2012'] = func_2012
mod = relay.transform.InferType()(mod)
mutated_mod['func_2012'] = func_2012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2012_call = mutated_mod.get_global_var('func_2012')
call_2013 = func_2012_call()
output = call_2013
func_2014 = relay.Function([], output)
mutated_mod['func_2014'] = func_2014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mod.get_global_var('func_1759')
func_1761_call = mutated_mod.get_global_var('func_1761')
call_2051 = func_1759_call()
call_2052 = func_1759_call()
output = relay.Tuple([call_2051,])
output2 = relay.Tuple([call_2052,])
func_2061 = relay.Function([], output)
mod['func_2061'] = func_2061
mod = relay.transform.InferType()(mod)
output = func_2061()
func_2062 = relay.Function([], output)
mutated_mod['func_2062'] = func_2062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_756_call = mod.get_global_var('func_756')
func_758_call = mutated_mod.get_global_var('func_758')
call_2063 = func_756_call()
call_2064 = func_756_call()
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_2081 = func_490_call()
call_2082 = func_490_call()
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_2119 = relay.TupleGetItem(func_1055_call(), 2)
call_2120 = relay.TupleGetItem(func_1056_call(), 2)
output = relay.Tuple([call_2063,call_2081,call_2119,])
output2 = relay.Tuple([call_2064,call_2082,call_2120,])
func_2122 = relay.Function([], output)
mod['func_2122'] = func_2122
mod = relay.transform.InferType()(mod)
mutated_mod['func_2122'] = func_2122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2122_call = mutated_mod.get_global_var('func_2122')
call_2123 = func_2122_call()
output = call_2123
func_2124 = relay.Function([], output)
mutated_mod['func_2124'] = func_2124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2061_call = mod.get_global_var('func_2061')
func_2062_call = mutated_mod.get_global_var('func_2062')
call_2160 = relay.TupleGetItem(func_2061_call(), 0)
call_2161 = relay.TupleGetItem(func_2062_call(), 0)
func_1198_call = mod.get_global_var('func_1198')
func_1202_call = mutated_mod.get_global_var('func_1202')
var_2184 = relay.var("var_2184", dtype = "uint16", shape = ())#candidate|2184|()|var|uint16
var_2185 = relay.var("var_2185", dtype = "uint16", shape = (154,))#candidate|2185|(154,)|var|uint16
call_2183 = relay.TupleGetItem(func_1198_call(relay.reshape(var_2184.astype('uint16'), []), relay.reshape(var_2185.astype('uint16'), [154,]), ), 1)
call_2186 = relay.TupleGetItem(func_1202_call(relay.reshape(var_2184.astype('uint16'), []), relay.reshape(var_2185.astype('uint16'), [154,]), ), 1)
output = relay.Tuple([call_2160,call_2183,var_2184,var_2185,])
output2 = relay.Tuple([call_2161,call_2186,var_2184,var_2185,])
func_2193 = relay.Function([var_2184,var_2185,], output)
mod['func_2193'] = func_2193
mod = relay.transform.InferType()(mod)
var_2194 = relay.var("var_2194", dtype = "uint16", shape = ())#candidate|2194|()|var|uint16
var_2195 = relay.var("var_2195", dtype = "uint16", shape = (154,))#candidate|2195|(154,)|var|uint16
output = func_2193(var_2194,var_2195,)
func_2196 = relay.Function([var_2194,var_2195,], output)
mutated_mod['func_2196'] = func_2196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_566_call = mod.get_global_var('func_566')
func_567_call = mutated_mod.get_global_var('func_567')
call_2206 = func_566_call()
call_2207 = func_566_call()
output = call_2206
output2 = call_2207
func_2213 = relay.Function([], output)
mod['func_2213'] = func_2213
mod = relay.transform.InferType()(mod)
mutated_mod['func_2213'] = func_2213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2213_call = mutated_mod.get_global_var('func_2213')
call_2214 = func_2213_call()
output = call_2214
func_2215 = relay.Function([], output)
mutated_mod['func_2215'] = func_2215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_850_call = mod.get_global_var('func_850')
func_851_call = mutated_mod.get_global_var('func_851')
call_2222 = relay.TupleGetItem(func_850_call(), 0)
call_2223 = relay.TupleGetItem(func_851_call(), 0)
output = call_2222
output2 = call_2223
func_2237 = relay.Function([], output)
mod['func_2237'] = func_2237
mod = relay.transform.InferType()(mod)
mutated_mod['func_2237'] = func_2237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2237_call = mutated_mod.get_global_var('func_2237')
call_2238 = func_2237_call()
output = call_2238
func_2239 = relay.Function([], output)
mutated_mod['func_2239'] = func_2239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_2262 = relay.TupleGetItem(func_1128_call(), 0)
call_2263 = relay.TupleGetItem(func_1129_call(), 0)
uop_2273 = relay.sinh(call_2262.astype('float32')) # shape=(13, 10, 3)
uop_2275 = relay.sinh(call_2263.astype('float32')) # shape=(13, 10, 3)
output = uop_2273
output2 = uop_2275
func_2278 = relay.Function([], output)
mod['func_2278'] = func_2278
mod = relay.transform.InferType()(mod)
output = func_2278()
func_2279 = relay.Function([], output)
mutated_mod['func_2279'] = func_2279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2012_call = mod.get_global_var('func_2012')
func_2014_call = mutated_mod.get_global_var('func_2014')
call_2303 = relay.TupleGetItem(func_2012_call(), 0)
call_2304 = relay.TupleGetItem(func_2014_call(), 0)
output = relay.Tuple([call_2303,])
output2 = relay.Tuple([call_2304,])
func_2307 = relay.Function([], output)
mod['func_2307'] = func_2307
mod = relay.transform.InferType()(mod)
mutated_mod['func_2307'] = func_2307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2308 = func_2307_call()
output = call_2308
func_2309 = relay.Function([], output)
mutated_mod['func_2309'] = func_2309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1764_call = mod.get_global_var('func_1764')
func_1766_call = mutated_mod.get_global_var('func_1766')
call_2367 = func_1764_call()
call_2368 = func_1764_call()
output = relay.Tuple([call_2367,])
output2 = relay.Tuple([call_2368,])
func_2377 = relay.Function([], output)
mod['func_2377'] = func_2377
mod = relay.transform.InferType()(mod)
output = func_2377()
func_2378 = relay.Function([], output)
mutated_mod['func_2378'] = func_2378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_2386 = func_490_call()
call_2387 = func_490_call()
output = call_2386
output2 = call_2387
func_2404 = relay.Function([], output)
mod['func_2404'] = func_2404
mod = relay.transform.InferType()(mod)
output = func_2404()
func_2405 = relay.Function([], output)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_756_call = mod.get_global_var('func_756')
func_758_call = mutated_mod.get_global_var('func_758')
call_2471 = func_756_call()
call_2472 = func_756_call()
const_2476 = relay.const([[[True,False,False],[True,False,True],[False,True,True],[True,False,False],[False,True,False],[False,True,False],[False,True,False],[True,False,True],[True,False,True],[True,True,False]],[[False,False,False],[False,True,False],[True,False,True],[False,True,False],[False,True,True],[True,False,False],[True,False,False],[False,True,False],[True,False,False],[False,False,True]],[[False,False,True],[True,False,True],[True,True,True],[True,True,False],[True,False,True],[False,True,True],[True,False,True],[True,False,False],[True,True,True],[False,True,True]],[[True,False,True],[True,True,True],[False,False,False],[True,True,True],[True,False,True],[False,True,False],[False,False,True],[True,True,True],[False,False,True],[True,False,False]],[[False,False,False],[True,True,True],[False,True,False],[False,False,True],[True,True,False],[True,True,True],[True,True,True],[False,True,False],[False,True,False],[True,False,True]],[[True,False,True],[False,True,False],[True,True,True],[True,True,True],[True,False,False],[True,True,True],[False,True,True],[True,True,False],[True,True,True],[True,False,True]],[[False,False,True],[True,False,False],[True,True,True],[False,True,False],[True,False,False],[True,True,False],[True,True,True],[False,False,False],[False,True,False],[True,False,False]],[[False,True,False],[True,False,False],[True,False,False],[False,False,True],[False,False,True],[False,True,False],[False,False,True],[True,False,True],[False,False,False],[False,True,False]],[[False,True,True],[True,False,False],[True,True,False],[True,True,False],[False,True,False],[True,False,False],[True,False,False],[False,False,True],[True,False,True],[True,False,True]],[[False,False,False],[True,True,True],[True,True,False],[True,False,False],[False,True,True],[False,False,True],[False,False,False],[True,False,False],[False,False,False],[True,True,False]],[[False,True,False],[True,True,False],[False,False,True],[False,False,True],[False,False,False],[False,False,True],[True,True,True],[True,False,True],[True,False,True],[True,True,True]],[[True,False,False],[False,True,True],[False,True,False],[True,True,False],[False,False,False],[True,False,False],[False,True,True],[True,True,True],[False,False,True],[False,False,True]],[[True,True,True],[True,True,False],[True,True,True],[True,False,False],[True,True,False],[True,False,False],[True,False,False],[True,True,True],[False,True,True],[False,True,True]]], dtype = "bool")#candidate|2476|(13, 10, 3)|const|bool
bop_2477 = relay.floor_mod(call_2471.astype('float64'), relay.reshape(const_2476.astype('float64'), relay.shape_of(call_2471))) # shape=(13, 10, 3)
bop_2480 = relay.floor_mod(call_2472.astype('float64'), relay.reshape(const_2476.astype('float64'), relay.shape_of(call_2472))) # shape=(13, 10, 3)
output = bop_2477
output2 = bop_2480
func_2501 = relay.Function([], output)
mod['func_2501'] = func_2501
mod = relay.transform.InferType()(mod)
output = func_2501()
func_2502 = relay.Function([], output)
mutated_mod['func_2502'] = func_2502
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2539 = relay.var("var_2539", dtype = "int64", shape = ())#candidate|2539|()|var|int64
var_2540 = relay.var("var_2540", dtype = "int64", shape = (13, 16, 11))#candidate|2540|(13, 16, 11)|var|int64
bop_2541 = relay.bitwise_xor(var_2539.astype('int64'), var_2540.astype('int64')) # shape=(13, 16, 11)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_2556 = func_776_call()
call_2557 = func_776_call()
output = relay.Tuple([bop_2541,call_2556,])
output2 = relay.Tuple([bop_2541,call_2557,])
func_2567 = relay.Function([var_2539,var_2540,], output)
mod['func_2567'] = func_2567
mod = relay.transform.InferType()(mod)
var_2568 = relay.var("var_2568", dtype = "int64", shape = ())#candidate|2568|()|var|int64
var_2569 = relay.var("var_2569", dtype = "int64", shape = (13, 16, 11))#candidate|2569|(13, 16, 11)|var|int64
output = func_2567(var_2568,var_2569,)
func_2570 = relay.Function([var_2568,var_2569,], output)
mutated_mod['func_2570'] = func_2570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1142_call = mod.get_global_var('func_1142')
func_1143_call = mutated_mod.get_global_var('func_1143')
call_2574 = relay.TupleGetItem(func_1142_call(), 0)
call_2575 = relay.TupleGetItem(func_1143_call(), 0)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_2580 = relay.TupleGetItem(func_1055_call(), 0)
call_2581 = relay.TupleGetItem(func_1056_call(), 0)
output = relay.Tuple([call_2574,call_2580,])
output2 = relay.Tuple([call_2575,call_2581,])
func_2584 = relay.Function([], output)
mod['func_2584'] = func_2584
mod = relay.transform.InferType()(mod)
output = func_2584()
func_2585 = relay.Function([], output)
mutated_mod['func_2585'] = func_2585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2307_call = mod.get_global_var('func_2307')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_2759 = relay.TupleGetItem(func_2307_call(), 0)
call_2760 = relay.TupleGetItem(func_2309_call(), 0)
const_2766 = relay.const([[[-1.470960,-4.115596,-6.045820,4.857389,9.155022,9.624777,3.171503,6.112140,2.337268],[3.014547,-8.731524,-1.223257,3.221833,-9.373552,-6.675334,-0.780327,-8.155361,5.486946]],[[-2.650134,-7.309940,7.137790,4.904833,-1.314817,-2.203694,-0.630705,7.597951,-0.399898],[-8.434979,3.705293,-9.767225,-4.850878,-2.656365,0.051220,9.376960,-1.836563,8.431517]],[[-9.190823,-2.395852,7.413360,-6.848897,4.496237,-7.657370,3.718278,2.081989,-6.478100],[6.124105,8.660893,1.949901,8.813418,-6.531245,-8.918331,-8.209627,-8.177509,1.200356]],[[0.384544,-8.875262,-0.986254,-9.558938,9.675232,-2.341754,7.997967,-2.131457,-6.055096],[9.737536,4.464500,7.314772,-7.329643,-6.318530,8.961153,-4.533958,5.140433,2.983786]],[[-1.956481,9.234469,2.636347,3.469350,5.515225,4.090352,7.963806,-7.605232,1.676361],[-4.481052,9.098175,-3.788709,3.558866,9.989006,3.221089,-6.836200,-2.491554,4.332203]],[[6.090069,0.606121,4.057662,-4.564838,7.129217,6.872791,5.269427,-3.765287,-2.385844],[9.906935,-4.498509,-0.650553,7.392693,3.006871,-1.615537,8.478822,1.084803,0.203852]],[[-2.496793,0.388278,-6.732508,-4.585779,-6.048465,-1.293985,8.248899,-1.252547,-9.605800],[-0.012376,5.157526,8.218446,-0.695527,-5.967150,1.960240,-6.634989,3.772508,-3.806669]],[[-6.944633,5.723957,6.295924,5.460837,6.135244,-4.824864,-8.763880,0.511225,-3.729095],[-5.042876,-2.668304,-5.956148,-0.168354,2.806305,-9.306564,9.848328,-8.907764,-3.300934]],[[-8.149088,-2.332962,7.304303,7.489446,9.048459,-6.371456,1.371736,7.695723,8.875853],[-0.685702,-9.241101,0.606369,8.933819,-3.541550,-4.080064,0.113182,-8.779733,-2.467946]],[[6.357308,-2.313367,1.552677,-0.216795,5.163089,-8.820423,-1.657505,-4.088288,-4.937006],[1.787592,-3.269590,3.272126,-0.574010,1.170638,-1.338114,0.030302,6.788426,3.395956]],[[-9.087872,4.746797,2.575418,-2.954970,-1.397904,-9.069865,-5.160021,-9.884816,8.045290],[4.781372,2.120678,8.673471,3.475427,3.622113,-7.641586,5.142775,-9.158779,-9.023048]],[[-1.315586,0.160002,2.505843,9.974308,-8.508327,-9.767940,4.988600,3.454492,-4.759728],[-2.353979,4.108060,-3.010983,-6.222018,-8.135295,-5.188587,-5.854673,2.028359,-9.687802]]], dtype = "float32")#candidate|2766|(12, 2, 9)|const|float32
bop_2767 = relay.left_shift(call_2759.astype('int8'), relay.reshape(const_2766.astype('int8'), relay.shape_of(call_2759))) # shape=(12, 2, 9)
bop_2770 = relay.left_shift(call_2760.astype('int8'), relay.reshape(const_2766.astype('int8'), relay.shape_of(call_2760))) # shape=(12, 2, 9)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_2772 = relay.TupleGetItem(func_1894_call(), 0)
call_2773 = relay.TupleGetItem(func_1896_call(), 0)
output = relay.Tuple([bop_2767,call_2772,])
output2 = relay.Tuple([bop_2770,call_2773,])
func_2781 = relay.Function([], output)
mod['func_2781'] = func_2781
mod = relay.transform.InferType()(mod)
output = func_2781()
func_2782 = relay.Function([], output)
mutated_mod['func_2782'] = func_2782
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2798 = relay.var("var_2798", dtype = "bool", shape = (6, 8, 16))#candidate|2798|(6, 8, 16)|var|bool
var_2799 = relay.var("var_2799", dtype = "bool", shape = (6, 8, 16))#candidate|2799|(6, 8, 16)|var|bool
bop_2800 = relay.logical_or(var_2798.astype('bool'), relay.reshape(var_2799.astype('bool'), relay.shape_of(var_2798))) # shape=(6, 8, 16)
uop_2810 = relay.rsqrt(var_2798.astype('float32')) # shape=(6, 8, 16)
output = relay.Tuple([bop_2800,uop_2810,])
output2 = relay.Tuple([bop_2800,uop_2810,])
func_2812 = relay.Function([var_2798,var_2799,], output)
mod['func_2812'] = func_2812
mod = relay.transform.InferType()(mod)
var_2813 = relay.var("var_2813", dtype = "bool", shape = (6, 8, 16))#candidate|2813|(6, 8, 16)|var|bool
var_2814 = relay.var("var_2814", dtype = "bool", shape = (6, 8, 16))#candidate|2814|(6, 8, 16)|var|bool
output = func_2812(var_2813,var_2814,)
func_2815 = relay.Function([var_2813,var_2814,], output)
mutated_mod['func_2815'] = func_2815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_596_call = mod.get_global_var('func_596')
func_597_call = mutated_mod.get_global_var('func_597')
call_2845 = func_596_call()
call_2846 = func_596_call()
output = call_2845
output2 = call_2846
func_2848 = relay.Function([], output)
mod['func_2848'] = func_2848
mod = relay.transform.InferType()(mod)
output = func_2848()
func_2849 = relay.Function([], output)
mutated_mod['func_2849'] = func_2849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mod.get_global_var('func_1759')
func_1761_call = mutated_mod.get_global_var('func_1761')
call_2852 = func_1759_call()
call_2853 = func_1759_call()
output = relay.Tuple([call_2852,])
output2 = relay.Tuple([call_2853,])
func_2856 = relay.Function([], output)
mod['func_2856'] = func_2856
mod = relay.transform.InferType()(mod)
mutated_mod['func_2856'] = func_2856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2856_call = mutated_mod.get_global_var('func_2856')
call_2857 = func_2856_call()
output = call_2857
func_2858 = relay.Function([], output)
mutated_mod['func_2858'] = func_2858
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2905 = relay.var("var_2905", dtype = "float64", shape = (11, 13, 16))#candidate|2905|(11, 13, 16)|var|float64
uop_2906 = relay.sin(var_2905.astype('float64')) # shape=(11, 13, 16)
func_2848_call = mod.get_global_var('func_2848')
func_2849_call = mutated_mod.get_global_var('func_2849')
call_2910 = func_2848_call()
call_2911 = func_2848_call()
output = relay.Tuple([uop_2906,call_2910,])
output2 = relay.Tuple([uop_2906,call_2911,])
func_2923 = relay.Function([var_2905,], output)
mod['func_2923'] = func_2923
mod = relay.transform.InferType()(mod)
mutated_mod['func_2923'] = func_2923
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2924 = relay.var("var_2924", dtype = "float64", shape = (11, 13, 16))#candidate|2924|(11, 13, 16)|var|float64
func_2923_call = mutated_mod.get_global_var('func_2923')
call_2925 = func_2923_call(var_2924)
output = call_2925
func_2926 = relay.Function([var_2924], output)
mutated_mod['func_2926'] = func_2926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_756_call = mod.get_global_var('func_756')
func_758_call = mutated_mod.get_global_var('func_758')
call_2939 = func_756_call()
call_2940 = func_756_call()
func_2061_call = mod.get_global_var('func_2061')
func_2062_call = mutated_mod.get_global_var('func_2062')
call_2958 = relay.TupleGetItem(func_2061_call(), 0)
call_2959 = relay.TupleGetItem(func_2062_call(), 0)
uop_2965 = relay.atanh(call_2958.astype('float64')) # shape=(13, 10, 3)
uop_2967 = relay.atanh(call_2959.astype('float64')) # shape=(13, 10, 3)
func_1736_call = mod.get_global_var('func_1736')
func_1738_call = mutated_mod.get_global_var('func_1738')
call_2991 = relay.TupleGetItem(func_1736_call(), 1)
call_2992 = relay.TupleGetItem(func_1738_call(), 1)
bop_2997 = relay.maximum(uop_2965.astype('int32'), relay.reshape(call_2939.astype('int32'), relay.shape_of(uop_2965))) # shape=(13, 10, 3)
bop_3000 = relay.maximum(uop_2967.astype('int32'), relay.reshape(call_2940.astype('int32'), relay.shape_of(uop_2967))) # shape=(13, 10, 3)
output = relay.Tuple([call_2991,bop_2997,])
output2 = relay.Tuple([call_2992,bop_3000,])
func_3005 = relay.Function([], output)
mod['func_3005'] = func_3005
mod = relay.transform.InferType()(mod)
mutated_mod['func_3005'] = func_3005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3005_call = mutated_mod.get_global_var('func_3005')
call_3006 = func_3005_call()
output = call_3006
func_3007 = relay.Function([], output)
mutated_mod['func_3007'] = func_3007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1394_call = mod.get_global_var('func_1394')
func_1396_call = mutated_mod.get_global_var('func_1396')
call_3027 = relay.TupleGetItem(func_1394_call(), 1)
call_3028 = relay.TupleGetItem(func_1396_call(), 1)
output = call_3027
output2 = call_3028
func_3066 = relay.Function([], output)
mod['func_3066'] = func_3066
mod = relay.transform.InferType()(mod)
mutated_mod['func_3066'] = func_3066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3066_call = mutated_mod.get_global_var('func_3066')
call_3067 = func_3066_call()
output = call_3067
func_3068 = relay.Function([], output)
mutated_mod['func_3068'] = func_3068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1350_call = mod.get_global_var('func_1350')
func_1352_call = mutated_mod.get_global_var('func_1352')
call_3075 = relay.TupleGetItem(func_1350_call(), 0)
call_3076 = relay.TupleGetItem(func_1352_call(), 0)
output = call_3075
output2 = call_3076
func_3082 = relay.Function([], output)
mod['func_3082'] = func_3082
mod = relay.transform.InferType()(mod)
output = func_3082()
func_3083 = relay.Function([], output)
mutated_mod['func_3083'] = func_3083
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3087 = relay.const([[-2.429794,-7.244555,-3.308320,9.527226,-9.282643,4.913089,1.898407,9.995070,4.224634,-3.114997,-7.226468,4.978418],[-4.330851,-3.756512,4.617278,-0.945564,9.148677,7.108990,-9.632930,3.188644,-8.279919,6.134328,-8.821437,-2.089836],[-5.437821,7.565217,-6.189475,8.981137,0.089507,-0.916448,5.701764,-9.283852,3.449127,4.687342,6.945522,-9.179413],[0.293482,7.024264,-2.615528,3.236339,-9.187911,2.262491,7.399447,6.412656,-5.536711,1.634252,-5.318204,-5.921321],[5.846241,-8.589146,-7.719944,-1.149517,-7.681452,-4.136501,-4.146978,4.964539,-1.976890,4.888003,8.000416,7.138626]], dtype = "float64")#candidate|3087|(5, 12)|const|float64
uop_3088 = relay.rsqrt(const_3087.astype('float64')) # shape=(5, 12)
func_1264_call = mod.get_global_var('func_1264')
func_1266_call = mutated_mod.get_global_var('func_1266')
const_3107 = relay.const([True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,False], dtype = "bool")#candidate|3107|(390,)|const|bool
call_3106 = func_1264_call(relay.reshape(const_3107.astype('bool'), [13, 10, 3]))
call_3108 = func_1264_call(relay.reshape(const_3107.astype('bool'), [13, 10, 3]))
bop_3119 = relay.power(const_3107.astype('float64'), relay.reshape(call_3106.astype('float64'), relay.shape_of(const_3107))) # shape=(390,)
bop_3122 = relay.power(const_3107.astype('float64'), relay.reshape(call_3108.astype('float64'), relay.shape_of(const_3107))) # shape=(390,)
output = relay.Tuple([uop_3088,bop_3119,])
output2 = relay.Tuple([uop_3088,bop_3122,])
func_3125 = relay.Function([], output)
mod['func_3125'] = func_3125
mod = relay.transform.InferType()(mod)
output = func_3125()
func_3126 = relay.Function([], output)
mutated_mod['func_3126'] = func_3126
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3154 = relay.var("var_3154", dtype = "float32", shape = (2, 12, 11))#candidate|3154|(2, 12, 11)|var|float32
uop_3155 = relay.log2(var_3154.astype('float32')) # shape=(2, 12, 11)
output = relay.Tuple([uop_3155,])
output2 = relay.Tuple([uop_3155,])
func_3157 = relay.Function([var_3154,], output)
mod['func_3157'] = func_3157
mod = relay.transform.InferType()(mod)
mutated_mod['func_3157'] = func_3157
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3158 = relay.var("var_3158", dtype = "float32", shape = (2, 12, 11))#candidate|3158|(2, 12, 11)|var|float32
func_3157_call = mutated_mod.get_global_var('func_3157')
call_3159 = func_3157_call(var_3158)
output = call_3159
func_3160 = relay.Function([var_3158], output)
mutated_mod['func_3160'] = func_3160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2377_call = mod.get_global_var('func_2377')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_3199 = relay.TupleGetItem(func_2377_call(), 0)
call_3200 = relay.TupleGetItem(func_2378_call(), 0)
output = call_3199
output2 = call_3200
func_3204 = relay.Function([], output)
mod['func_3204'] = func_3204
mod = relay.transform.InferType()(mod)
output = func_3204()
func_3205 = relay.Function([], output)
mutated_mod['func_3205'] = func_3205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_3229 = func_1468_call()
call_3230 = func_1468_call()
uop_3237 = relay.tan(call_3229.astype('float32')) # shape=(13, 10, 3)
uop_3239 = relay.tan(call_3230.astype('float32')) # shape=(13, 10, 3)
output = uop_3237
output2 = uop_3239
func_3246 = relay.Function([], output)
mod['func_3246'] = func_3246
mod = relay.transform.InferType()(mod)
output = func_3246()
func_3247 = relay.Function([], output)
mutated_mod['func_3247'] = func_3247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2237_call = mod.get_global_var('func_2237')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_3286 = func_2237_call()
call_3287 = func_2237_call()
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_3301 = func_1850_call()
call_3302 = func_1850_call()
output = relay.Tuple([call_3286,call_3301,])
output2 = relay.Tuple([call_3287,call_3302,])
func_3317 = relay.Function([], output)
mod['func_3317'] = func_3317
mod = relay.transform.InferType()(mod)
output = func_3317()
func_3318 = relay.Function([], output)
mutated_mod['func_3318'] = func_3318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2213_call = mod.get_global_var('func_2213')
func_2215_call = mutated_mod.get_global_var('func_2215')
call_3396 = func_2213_call()
call_3397 = func_2213_call()
func_2812_call = mod.get_global_var('func_2812')
func_2815_call = mutated_mod.get_global_var('func_2815')
var_3400 = relay.var("var_3400", dtype = "bool", shape = (768,))#candidate|3400|(768,)|var|bool
call_3399 = relay.TupleGetItem(func_2812_call(relay.reshape(var_3400.astype('bool'), [6, 8, 16]), relay.reshape(var_3400.astype('bool'), [6, 8, 16]), ), 1)
call_3401 = relay.TupleGetItem(func_2815_call(relay.reshape(var_3400.astype('bool'), [6, 8, 16]), relay.reshape(var_3400.astype('bool'), [6, 8, 16]), ), 1)
func_1365_call = mod.get_global_var('func_1365')
func_1366_call = mutated_mod.get_global_var('func_1366')
call_3417 = relay.TupleGetItem(func_1365_call(), 0)
call_3418 = relay.TupleGetItem(func_1366_call(), 0)
output = relay.Tuple([call_3396,call_3399,var_3400,call_3417,])
output2 = relay.Tuple([call_3397,call_3401,var_3400,call_3418,])
func_3419 = relay.Function([var_3400,], output)
mod['func_3419'] = func_3419
mod = relay.transform.InferType()(mod)
var_3420 = relay.var("var_3420", dtype = "bool", shape = (768,))#candidate|3420|(768,)|var|bool
output = func_3419(var_3420)
func_3421 = relay.Function([var_3420], output)
mutated_mod['func_3421'] = func_3421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_3431 = relay.TupleGetItem(func_1055_call(), 2)
call_3432 = relay.TupleGetItem(func_1056_call(), 2)
output = relay.Tuple([call_3431,])
output2 = relay.Tuple([call_3432,])
func_3433 = relay.Function([], output)
mod['func_3433'] = func_3433
mod = relay.transform.InferType()(mod)
mutated_mod['func_3433'] = func_3433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3433_call = mutated_mod.get_global_var('func_3433')
call_3434 = func_3433_call()
output = call_3434
func_3435 = relay.Function([], output)
mutated_mod['func_3435'] = func_3435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2856_call = mod.get_global_var('func_2856')
func_2858_call = mutated_mod.get_global_var('func_2858')
call_3438 = relay.TupleGetItem(func_2856_call(), 0)
call_3439 = relay.TupleGetItem(func_2858_call(), 0)
output = relay.Tuple([call_3438,])
output2 = relay.Tuple([call_3439,])
func_3457 = relay.Function([], output)
mod['func_3457'] = func_3457
mod = relay.transform.InferType()(mod)
mutated_mod['func_3457'] = func_3457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3457_call = mutated_mod.get_global_var('func_3457')
call_3458 = func_3457_call()
output = call_3458
func_3459 = relay.Function([], output)
mutated_mod['func_3459'] = func_3459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1233_call = mutated_mod.get_global_var('func_1233')
call_3465 = relay.TupleGetItem(func_1232_call(), 0)
call_3466 = relay.TupleGetItem(func_1233_call(), 0)
func_3204_call = mod.get_global_var('func_3204')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_3474 = func_3204_call()
call_3475 = func_3204_call()
output = relay.Tuple([call_3465,call_3474,])
output2 = relay.Tuple([call_3466,call_3475,])
func_3481 = relay.Function([], output)
mod['func_3481'] = func_3481
mod = relay.transform.InferType()(mod)
mutated_mod['func_3481'] = func_3481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3481_call = mutated_mod.get_global_var('func_3481')
call_3482 = func_3481_call()
output = call_3482
func_3483 = relay.Function([], output)
mutated_mod['func_3483'] = func_3483
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3519 = relay.var("var_3519", dtype = "int32", shape = (1, 2, 11))#candidate|3519|(1, 2, 11)|var|int32
var_3520 = relay.var("var_3520", dtype = "int32", shape = (4, 2, 11))#candidate|3520|(4, 2, 11)|var|int32
bop_3521 = relay.less_equal(var_3519.astype('bool'), var_3520.astype('bool')) # shape=(4, 2, 11)
output = bop_3521
output2 = bop_3521
func_3525 = relay.Function([var_3519,var_3520,], output)
mod['func_3525'] = func_3525
mod = relay.transform.InferType()(mod)
var_3526 = relay.var("var_3526", dtype = "int32", shape = (1, 2, 11))#candidate|3526|(1, 2, 11)|var|int32
var_3527 = relay.var("var_3527", dtype = "int32", shape = (4, 2, 11))#candidate|3527|(4, 2, 11)|var|int32
output = func_3525(var_3526,var_3527,)
func_3528 = relay.Function([var_3526,var_3527,], output)
mutated_mod['func_3528'] = func_3528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mod.get_global_var('func_2848')
func_2849_call = mutated_mod.get_global_var('func_2849')
call_3545 = func_2848_call()
call_3546 = func_2848_call()
uop_3547 = relay.asin(call_3545.astype('float64')) # shape=(13, 10, 3)
uop_3549 = relay.asin(call_3546.astype('float64')) # shape=(13, 10, 3)
func_1983_call = mod.get_global_var('func_1983')
func_1986_call = mutated_mod.get_global_var('func_1986')
const_3553 = relay.const(2.955902, dtype = "float64")#candidate|3553|()|const|float64
const_3554 = relay.const([6.499267,3.181379,-7.846296,0.433993,-6.054753,-2.170259,-0.903175,4.147004,-8.998783,9.784390,-7.035498,-4.017685,-4.761486,2.949925,-9.227659,-4.499462,-2.671252,-7.445285,4.463134,3.926485,-2.702745,-9.989008,6.987209,1.589063,-7.744317,-1.737346,-0.511209,-4.084424,0.654931,-2.637856,6.873746,5.729825,-2.732879,-1.302169,2.162378,-6.185414,4.511597,2.903406,-3.914145,-9.516145,3.447351,4.870546,-7.137505,0.225276,5.558332,9.381939,-4.500652,-3.433151,-5.091559,3.570385,-9.555015,3.243237,-2.208378,-0.722931,2.240752,4.754964,-1.089907,-0.020360,0.149808,-4.956045,-1.570463,2.285000,-1.710266,1.832868,-6.867955,3.678388,-8.785348,-8.681590,7.945633,-5.193166,5.210682,1.807750,-2.611908,-8.102946,7.534979,5.992653,3.650622,8.905916,-8.496598,-5.100448,8.158249,-7.530105,1.177291,-3.984716,6.385461,0.587976,-7.617451,-6.612701,1.037689,-4.042749,3.331873,-9.018278,-3.086605,8.609128,-1.056929,4.700972,7.673264,-2.957958,-0.415380,3.191329,4.925685,9.183999,3.882941,-8.169705,-4.281323,-8.997475,-2.182227,-1.936040,-4.801988,-3.869350,-6.612621,-9.843400,7.163954,-4.395216,7.019476,7.242124,-3.441467,-9.902298,0.044655,-2.731071,-5.009495,9.484372,6.441832,4.721985,8.988978,0.590673,-8.590267,0.560837,-8.891595,1.108126,5.787216,-3.943044,9.937610,-6.729262,9.438524,1.173425,5.718405,5.495290,-5.154337,-0.153362,-1.147639,1.065041,3.988690,-5.339900,-6.814813,7.317999,-8.009202,-6.855788,-7.329006,-5.487926,6.284469,2.091233,3.530655,-6.352561,-7.699696,3.427883,-1.797988,2.314658,-3.739357,0.197865,0.633711,-1.823600,-9.863567,-7.371438,0.046472,-1.645849,-0.977918,1.454969,-6.806289,1.841407,-0.400151,1.807677,-0.636853,-5.251585,-9.666551,2.532634,-9.338478,-8.273429,-5.157972,-4.752523,1.738329,6.920860,-8.999982,1.252022,-6.777090,4.187267,-1.719500,1.164571,1.873218,9.947452,5.918988,-2.377234,-8.186965,-8.935402,3.525404,8.670519,6.349237,-0.401055,6.003233,5.263928,-8.272272,2.173115,1.032298,8.910872,-6.877532,3.457461,-1.227515,-7.252200,-9.260234,3.939555,5.911583,-0.711556,2.588184,-6.112815,8.669424,-3.251794,6.140547,-7.063968,-6.287478,0.392885,-1.006910,-2.945168,-5.514627,5.981856,2.717485,-4.214527,0.647582,-8.250618,0.278206,-7.776376,-3.064810,8.932461,-7.277247,-6.676731,6.136481,0.075179,-2.232660,-4.559003,-0.643674,3.459000,1.753206,-6.680563,6.320334,0.903004,-6.359401,6.791027,1.673064,-1.996927,-1.546623,-8.433982,-9.697931,0.216386,-9.841633,-4.986052,2.655624,-6.073915,0.220502,-9.146255,2.048096,-7.200126,2.218248,-9.508496,-8.627997,-7.624881,-6.531014,-6.231857,-7.466463,3.291557,-4.551186,-8.027451,-4.264942,-2.988474,5.248916,-7.931845,-8.439286,-6.698442,-3.485279,-5.456523,5.954088,1.096709,-2.563903,1.370434,0.359130,4.674474,-8.533172,1.951603,-0.855651,-4.547861,-8.975074,7.654233,0.960698,-8.825115,-2.685139,-8.039101,6.811923,7.087141,-0.863055,2.046272,-8.796790,3.202399,-9.680782,7.960509,-0.881024,-3.716810,-0.105810,1.334590,-0.751365,7.503425,0.254837,-6.247307,9.930043,-8.518339,-7.238229,8.788036,-1.885263,2.850197,1.792490,2.231926,3.142260,3.347013,5.640207,9.324486,-8.134483,2.493801,8.668364,3.624663,9.829114,-3.492968,9.815368,-2.440180,-3.603908,-4.999672,-4.985124,1.081145,7.259623,2.462359,0.224683,-0.960350,5.320682,5.800212,-4.095370,2.503216,-6.173700,1.806983,5.204248,7.672082,-4.139896,-7.016517,-7.450862,-7.719079,-1.162253,-8.910589,-8.141800,0.300992,-4.348914,-8.121140,4.964565,4.211412,9.745363,4.415502,-5.753351,-4.004735,-1.749388,-3.102355,-6.087609,3.910798,-3.244715,7.625106,-0.904481,7.779470,8.900906,8.623130,5.285217,6.230396,-6.042243,-1.181895,7.712633,4.153213,7.654145,-0.728583,-8.691338,-7.367734,-4.760241,0.686213,-5.654836,2.990713,9.385927,5.130439,1.845887,4.795130,6.320802,4.175048,3.605813,2.266698,-3.273701,-8.781908,4.464621,0.343102,-6.230113,-4.749697], dtype = "float64")#candidate|3554|(400,)|const|float64
call_3552 = relay.TupleGetItem(func_1983_call(relay.reshape(const_3553.astype('float64'), []), relay.reshape(const_3554.astype('float64'), [5, 8, 10]), ), 1)
call_3555 = relay.TupleGetItem(func_1986_call(relay.reshape(const_3553.astype('float64'), []), relay.reshape(const_3554.astype('float64'), [5, 8, 10]), ), 1)
bop_3604 = relay.not_equal(uop_3547.astype('bool'), const_3553.astype('bool')) # shape=(13, 10, 3)
bop_3607 = relay.not_equal(uop_3549.astype('bool'), const_3553.astype('bool')) # shape=(13, 10, 3)
func_348_call = mod.get_global_var('func_348')
func_350_call = mutated_mod.get_global_var('func_350')
call_3613 = func_348_call()
call_3614 = func_348_call()
output = relay.Tuple([call_3552,const_3554,bop_3604,call_3613,])
output2 = relay.Tuple([call_3555,const_3554,bop_3607,call_3614,])
func_3623 = relay.Function([], output)
mod['func_3623'] = func_3623
mod = relay.transform.InferType()(mod)
output = func_3623()
func_3624 = relay.Function([], output)
mutated_mod['func_3624'] = func_3624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1736_call = mod.get_global_var('func_1736')
func_1738_call = mutated_mod.get_global_var('func_1738')
call_3627 = relay.TupleGetItem(func_1736_call(), 2)
call_3628 = relay.TupleGetItem(func_1738_call(), 2)
func_2307_call = mod.get_global_var('func_2307')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_3630 = relay.TupleGetItem(func_2307_call(), 0)
call_3631 = relay.TupleGetItem(func_2309_call(), 0)
output = relay.Tuple([call_3627,call_3630,])
output2 = relay.Tuple([call_3628,call_3631,])
func_3654 = relay.Function([], output)
mod['func_3654'] = func_3654
mod = relay.transform.InferType()(mod)
output = func_3654()
func_3655 = relay.Function([], output)
mutated_mod['func_3655'] = func_3655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1305_call = mod.get_global_var('func_1305')
func_1307_call = mutated_mod.get_global_var('func_1307')
call_3656 = func_1305_call()
call_3657 = func_1305_call()
output = call_3656
output2 = call_3657
func_3670 = relay.Function([], output)
mod['func_3670'] = func_3670
mod = relay.transform.InferType()(mod)
mutated_mod['func_3670'] = func_3670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3670_call = mutated_mod.get_global_var('func_3670')
call_3671 = func_3670_call()
output = call_3671
func_3672 = relay.Function([], output)
mutated_mod['func_3672'] = func_3672
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3675 = relay.var("var_3675", dtype = "float64", shape = ())#candidate|3675|()|var|float64
var_3676 = relay.var("var_3676", dtype = "float64", shape = (15, 8, 2))#candidate|3676|(15, 8, 2)|var|float64
bop_3677 = relay.floor_divide(var_3675.astype('float64'), var_3676.astype('float64')) # shape=(15, 8, 2)
bop_3681 = relay.logical_xor(var_3676.astype('uint64'), var_3675.astype('uint64')) # shape=(15, 8, 2)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_3700 = func_776_call()
call_3701 = func_776_call()
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_3709 = func_1850_call()
call_3710 = func_1850_call()
func_3005_call = mod.get_global_var('func_3005')
func_3007_call = mutated_mod.get_global_var('func_3007')
call_3714 = relay.TupleGetItem(func_3005_call(), 1)
call_3715 = relay.TupleGetItem(func_3007_call(), 1)
func_566_call = mod.get_global_var('func_566')
func_567_call = mutated_mod.get_global_var('func_567')
call_3716 = func_566_call()
call_3717 = func_566_call()
output = relay.Tuple([bop_3677,bop_3681,call_3700,call_3709,call_3714,call_3716,])
output2 = relay.Tuple([bop_3677,bop_3681,call_3701,call_3710,call_3715,call_3717,])
func_3733 = relay.Function([var_3675,var_3676,], output)
mod['func_3733'] = func_3733
mod = relay.transform.InferType()(mod)
mutated_mod['func_3733'] = func_3733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3733_call = mutated_mod.get_global_var('func_3733')
var_3735 = relay.var("var_3735", dtype = "float64", shape = ())#candidate|3735|()|var|float64
var_3736 = relay.var("var_3736", dtype = "float64", shape = (15, 8, 2))#candidate|3736|(15, 8, 2)|var|float64
call_3734 = func_3733_call(var_3735,var_3736,)
output = call_3734
func_3737 = relay.Function([var_3735,var_3736,], output)
mutated_mod['func_3737'] = func_3737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_3771 = relay.TupleGetItem(func_1055_call(), 0)
call_3772 = relay.TupleGetItem(func_1056_call(), 0)
func_1764_call = mod.get_global_var('func_1764')
func_1766_call = mutated_mod.get_global_var('func_1766')
call_3779 = func_1764_call()
call_3780 = func_1764_call()
output = relay.Tuple([call_3771,call_3779,])
output2 = relay.Tuple([call_3772,call_3780,])
func_3783 = relay.Function([], output)
mod['func_3783'] = func_3783
mod = relay.transform.InferType()(mod)
output = func_3783()
func_3784 = relay.Function([], output)
mutated_mod['func_3784'] = func_3784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2061_call = mod.get_global_var('func_2061')
func_2062_call = mutated_mod.get_global_var('func_2062')
call_3818 = relay.TupleGetItem(func_2061_call(), 0)
call_3819 = relay.TupleGetItem(func_2062_call(), 0)
output = call_3818
output2 = call_3819
func_3826 = relay.Function([], output)
mod['func_3826'] = func_3826
mod = relay.transform.InferType()(mod)
output = func_3826()
func_3827 = relay.Function([], output)
mutated_mod['func_3827'] = func_3827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3005_call = mod.get_global_var('func_3005')
func_3007_call = mutated_mod.get_global_var('func_3007')
call_3831 = relay.TupleGetItem(func_3005_call(), 0)
call_3832 = relay.TupleGetItem(func_3007_call(), 0)
var_3833 = relay.var("var_3833", dtype = "int16", shape = (252,))#candidate|3833|(252,)|var|int16
bop_3834 = relay.bitwise_and(call_3831.astype('int16'), relay.reshape(var_3833.astype('int16'), relay.shape_of(call_3831))) # shape=(252,)
bop_3837 = relay.bitwise_and(call_3832.astype('int16'), relay.reshape(var_3833.astype('int16'), relay.shape_of(call_3832))) # shape=(252,)
output = bop_3834
output2 = bop_3837
func_3854 = relay.Function([var_3833,], output)
mod['func_3854'] = func_3854
mod = relay.transform.InferType()(mod)
var_3855 = relay.var("var_3855", dtype = "int16", shape = (252,))#candidate|3855|(252,)|var|int16
output = func_3854(var_3855)
func_3856 = relay.Function([var_3855], output)
mutated_mod['func_3856'] = func_3856
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3858 = relay.const(2, dtype = "uint32")#candidate|3858|()|const|uint32
var_3859 = relay.var("var_3859", dtype = "uint32", shape = (4, 2, 5))#candidate|3859|(4, 2, 5)|var|uint32
bop_3860 = relay.right_shift(const_3858.astype('uint32'), var_3859.astype('uint32')) # shape=(4, 2, 5)
func_291_call = mod.get_global_var('func_291')
func_293_call = mutated_mod.get_global_var('func_293')
call_3863 = func_291_call()
call_3864 = func_291_call()
output = relay.Tuple([bop_3860,call_3863,])
output2 = relay.Tuple([bop_3860,call_3864,])
func_3866 = relay.Function([var_3859,], output)
mod['func_3866'] = func_3866
mod = relay.transform.InferType()(mod)
var_3867 = relay.var("var_3867", dtype = "uint32", shape = (4, 2, 5))#candidate|3867|(4, 2, 5)|var|uint32
output = func_3866(var_3867)
func_3868 = relay.Function([var_3867], output)
mutated_mod['func_3868'] = func_3868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1142_call = mod.get_global_var('func_1142')
func_1143_call = mutated_mod.get_global_var('func_1143')
call_4011 = relay.TupleGetItem(func_1142_call(), 0)
call_4012 = relay.TupleGetItem(func_1143_call(), 0)
func_3733_call = mod.get_global_var('func_3733')
func_3737_call = mutated_mod.get_global_var('func_3737')
var_4047 = relay.var("var_4047", dtype = "float64", shape = ())#candidate|4047|()|var|float64
var_4048 = relay.var("var_4048", dtype = "float64", shape = (240,))#candidate|4048|(240,)|var|float64
call_4046 = relay.TupleGetItem(func_3733_call(relay.reshape(var_4047.astype('float64'), []), relay.reshape(var_4048.astype('float64'), [15, 8, 2]), ), 4)
call_4049 = relay.TupleGetItem(func_3737_call(relay.reshape(var_4047.astype('float64'), []), relay.reshape(var_4048.astype('float64'), [15, 8, 2]), ), 4)
output = relay.Tuple([call_4011,call_4046,var_4047,var_4048,])
output2 = relay.Tuple([call_4012,call_4049,var_4047,var_4048,])
func_4054 = relay.Function([var_4047,var_4048,], output)
mod['func_4054'] = func_4054
mod = relay.transform.InferType()(mod)
var_4055 = relay.var("var_4055", dtype = "float64", shape = ())#candidate|4055|()|var|float64
var_4056 = relay.var("var_4056", dtype = "float64", shape = (240,))#candidate|4056|(240,)|var|float64
output = func_4054(var_4055,var_4056,)
func_4057 = relay.Function([var_4055,var_4056,], output)
mutated_mod['func_4057'] = func_4057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_756_call = mod.get_global_var('func_756')
func_758_call = mutated_mod.get_global_var('func_758')
call_4067 = func_756_call()
call_4068 = func_756_call()
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_4086 = func_490_call()
call_4087 = func_490_call()
output = relay.Tuple([call_4067,call_4086,])
output2 = relay.Tuple([call_4068,call_4087,])
func_4103 = relay.Function([], output)
mod['func_4103'] = func_4103
mod = relay.transform.InferType()(mod)
output = func_4103()
func_4104 = relay.Function([], output)
mutated_mod['func_4104'] = func_4104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2856_call = mod.get_global_var('func_2856')
func_2858_call = mutated_mod.get_global_var('func_2858')
call_4117 = relay.TupleGetItem(func_2856_call(), 0)
call_4118 = relay.TupleGetItem(func_2858_call(), 0)
output = call_4117
output2 = call_4118
func_4123 = relay.Function([], output)
mod['func_4123'] = func_4123
mod = relay.transform.InferType()(mod)
output = func_4123()
func_4124 = relay.Function([], output)
mutated_mod['func_4124'] = func_4124
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4201 = relay.const([[[5.441082,0.811640,-8.607817,4.930803,2.708030,-0.068714,8.390736,9.828052,-3.642684,-2.077512,3.316859,-0.869795,7.779974,-1.547769,7.197116],[2.292766,-1.016862,-6.817258,-4.276455,-5.872619,-8.902618,-1.144885,3.523919,7.482186,4.754717,8.580296,-8.018695,-0.364702,-4.452188,-4.936056]],[[-6.145519,-9.631079,0.693093,4.591972,8.020104,3.768418,-1.903605,4.951333,9.024529,1.513041,0.872919,-5.375806,-7.030254,4.438856,3.942369],[4.980767,9.480578,-5.845394,-0.164970,4.381359,6.877962,6.153262,-1.724572,7.164726,2.180274,-9.668445,1.168787,0.684435,1.711094,0.313959]],[[-1.089411,-1.563008,-2.224531,-3.018033,-2.372622,-8.508992,-3.369284,-0.072240,6.851900,2.672949,-9.188634,2.221831,-0.148296,-6.789956,5.900631],[-0.479372,-4.555279,6.863426,5.400782,9.299425,5.228268,3.032354,1.972751,-1.788786,-5.607523,9.416257,0.153805,-0.186154,1.496320,2.395222]],[[-7.008700,5.379700,-5.621959,-5.330926,-9.822114,-4.528406,5.760818,-7.368189,8.187922,3.296263,-5.345926,-0.161422,6.753355,8.895159,8.547213],[6.748709,-1.541325,-1.409775,-3.840925,-3.553154,-9.542168,-4.304964,-4.842283,-3.998703,-0.363957,0.089052,6.971863,-5.216350,7.640796,6.826454]],[[4.815526,-8.998943,0.980647,-1.708363,1.709583,4.680968,3.937228,-8.197075,-6.872156,7.669457,-2.869454,4.434661,8.570423,3.760042,8.162793],[3.472427,7.849007,-2.457568,4.574998,-5.484750,9.835845,-8.528096,-2.417429,-4.340000,-6.655678,7.675749,1.256281,-7.875115,-2.336228,7.627002]],[[-6.590836,-8.980923,-3.136423,4.529425,-0.714425,3.868933,7.429531,-1.185182,-1.269737,-7.364829,8.805616,9.765467,-4.822479,1.574939,3.855038],[-7.897497,2.972876,-6.319319,9.212189,1.686646,8.205897,2.433286,3.858376,-0.982639,-8.825890,-8.335831,-2.918913,-5.913828,3.775006,-4.834759]],[[-8.082719,-3.253826,8.792020,-2.365400,-6.864514,-9.876468,-9.263442,-7.103916,-3.895965,7.575358,4.819423,-9.928539,2.332509,-3.095380,-5.482480],[-5.345134,7.614078,-9.391797,8.872435,1.874475,9.608124,5.764991,8.723834,5.630221,4.825240,5.800853,-8.386558,-7.806787,-6.020919,-1.710804]],[[8.426128,-5.807430,3.686724,-1.344093,9.432151,6.970192,7.599388,-9.663877,-7.361536,-3.956258,-1.839923,4.591404,5.927602,-0.976871,-7.220498],[-5.352973,0.433564,1.632219,-6.146085,5.952219,7.690018,-4.488968,-8.777596,-2.750693,-1.766012,-1.006138,-6.048680,9.581610,8.758798,4.757849]],[[-6.189979,-1.573832,-4.866641,-8.765786,1.419085,-8.243977,-0.074020,9.280273,0.453165,-8.479086,6.918143,-3.786693,-2.057528,8.606474,-5.908438],[6.007057,6.981117,-7.694336,6.328576,-0.834270,8.203481,-9.370084,4.143225,-4.007424,2.441305,-4.159546,3.598928,-2.168938,-8.025149,0.403069]],[[-8.240101,1.808671,-4.102565,-5.135653,-7.618418,-8.124355,0.564037,-3.625685,5.204272,-5.515896,1.415846,5.880662,9.138887,-7.075009,4.058201],[-9.861540,-9.189926,9.927976,-2.828228,5.840400,-6.458606,-5.693592,-5.312348,-6.506965,3.744980,-7.376436,1.061969,5.109365,5.745734,-8.901375]],[[9.278278,-6.235517,-4.263586,8.163022,4.084595,-1.784763,-1.011190,-2.124249,8.384846,-8.994499,4.914203,9.854666,-9.345574,4.323653,-3.522967],[4.909972,0.290528,0.707474,2.963256,-2.114091,6.744846,6.108655,1.941843,-2.136132,-6.428891,5.128554,6.951671,1.271779,9.373624,7.049695]],[[-2.475624,7.972216,0.684802,-5.543945,2.176926,3.185724,3.587179,1.590192,-7.952501,8.931753,-3.046980,-3.177817,2.796751,-2.602018,9.606742],[-6.820025,-5.523129,0.962322,-9.973348,-3.140044,-0.168101,5.861093,-5.176110,-7.676422,-6.044436,-2.299775,-6.185624,2.568544,-2.317820,-3.141164]],[[7.154148,6.649861,-3.503835,2.701577,-4.323723,8.758326,-9.436056,-4.174130,8.283493,6.248974,-1.438870,-5.276367,5.343191,-6.534308,2.864352],[6.229266,1.890000,-3.825459,7.909004,0.359659,-4.424676,-6.573003,8.262772,7.498176,7.564710,-6.512883,-9.285172,-1.918933,-3.703566,6.577793]],[[1.133840,6.483237,-9.661754,-9.062875,5.403644,2.504753,-0.085309,-8.599648,9.044943,-5.130855,8.089305,-8.879476,-4.222035,8.075689,-3.074582],[-5.420978,1.620913,-3.358655,-4.560644,8.064774,-2.897769,7.948277,-8.317881,-8.405011,9.337134,-8.071328,-2.066859,6.877961,1.268337,0.643896]],[[6.367112,4.013873,9.507172,-1.808343,-8.333884,-1.882087,6.906319,-2.776579,1.253798,0.414470,9.901027,2.826442,-0.219892,-2.361225,4.431078],[0.579725,-0.909783,6.498854,5.938589,8.082126,1.109420,-8.126759,0.913054,-7.070423,-2.387063,9.586076,9.073557,9.745185,1.681279,7.509822]],[[5.771250,-0.640315,2.543567,-3.278862,3.307492,6.030096,3.333786,5.160850,-7.148434,1.333960,9.584409,-3.191118,-1.110831,3.602235,-6.059466],[-8.249490,9.862114,9.447325,7.486489,1.274252,7.181924,1.173973,7.748973,7.344498,9.892316,-7.677774,5.264760,8.135199,-9.455441,-9.708665]]], dtype = "float64")#candidate|4201|(16, 2, 15)|const|float64
var_4202 = relay.var("var_4202", dtype = "float64", shape = (16, 2, 15))#candidate|4202|(16, 2, 15)|var|float64
bop_4203 = relay.maximum(const_4201.astype('float64'), relay.reshape(var_4202.astype('float64'), relay.shape_of(const_4201))) # shape=(16, 2, 15)
uop_4211 = relay.asin(const_4201.astype('float64')) # shape=(16, 2, 15)
output = relay.Tuple([bop_4203,uop_4211,])
output2 = relay.Tuple([bop_4203,uop_4211,])
func_4215 = relay.Function([var_4202,], output)
mod['func_4215'] = func_4215
mod = relay.transform.InferType()(mod)
mutated_mod['func_4215'] = func_4215
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4216 = relay.var("var_4216", dtype = "float64", shape = (16, 2, 15))#candidate|4216|(16, 2, 15)|var|float64
func_4215_call = mutated_mod.get_global_var('func_4215')
call_4217 = func_4215_call(var_4216)
output = call_4217
func_4218 = relay.Function([var_4216], output)
mutated_mod['func_4218'] = func_4218
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4272 = relay.var("var_4272", dtype = "int64", shape = ())#candidate|4272|()|var|int64
var_4273 = relay.var("var_4273", dtype = "int64", shape = (5, 5, 4))#candidate|4273|(5, 5, 4)|var|int64
bop_4274 = relay.right_shift(var_4272.astype('int64'), var_4273.astype('int64')) # shape=(5, 5, 4)
output = bop_4274
output2 = bop_4274
func_4285 = relay.Function([var_4272,var_4273,], output)
mod['func_4285'] = func_4285
mod = relay.transform.InferType()(mod)
mutated_mod['func_4285'] = func_4285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4285_call = mutated_mod.get_global_var('func_4285')
var_4287 = relay.var("var_4287", dtype = "int64", shape = ())#candidate|4287|()|var|int64
var_4288 = relay.var("var_4288", dtype = "int64", shape = (5, 5, 4))#candidate|4288|(5, 5, 4)|var|int64
call_4286 = func_4285_call(var_4287,var_4288,)
output = call_4286
func_4289 = relay.Function([var_4287,var_4288,], output)
mutated_mod['func_4289'] = func_4289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2377_call = mod.get_global_var('func_2377')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_4296 = relay.TupleGetItem(func_2377_call(), 0)
call_4297 = relay.TupleGetItem(func_2378_call(), 0)
output = call_4296
output2 = call_4297
func_4315 = relay.Function([], output)
mod['func_4315'] = func_4315
mod = relay.transform.InferType()(mod)
output = func_4315()
func_4316 = relay.Function([], output)
mutated_mod['func_4316'] = func_4316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_291_call = mod.get_global_var('func_291')
func_293_call = mutated_mod.get_global_var('func_293')
call_4417 = func_291_call()
call_4418 = func_291_call()
output = relay.Tuple([call_4417,])
output2 = relay.Tuple([call_4418,])
func_4435 = relay.Function([], output)
mod['func_4435'] = func_4435
mod = relay.transform.InferType()(mod)
output = func_4435()
func_4436 = relay.Function([], output)
mutated_mod['func_4436'] = func_4436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2279_call = mutated_mod.get_global_var('func_2279')
call_4443 = func_2278_call()
call_4444 = func_2278_call()
output = relay.Tuple([call_4443,])
output2 = relay.Tuple([call_4444,])
func_4473 = relay.Function([], output)
mod['func_4473'] = func_4473
mod = relay.transform.InferType()(mod)
output = func_4473()
func_4474 = relay.Function([], output)
mutated_mod['func_4474'] = func_4474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3317_call = mod.get_global_var('func_3317')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_4529 = relay.TupleGetItem(func_3317_call(), 1)
call_4530 = relay.TupleGetItem(func_3318_call(), 1)
output = relay.Tuple([call_4529,])
output2 = relay.Tuple([call_4530,])
func_4531 = relay.Function([], output)
mod['func_4531'] = func_4531
mod = relay.transform.InferType()(mod)
mutated_mod['func_4531'] = func_4531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4531_call = mutated_mod.get_global_var('func_4531')
call_4532 = func_4531_call()
output = call_4532
func_4533 = relay.Function([], output)
mutated_mod['func_4533'] = func_4533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2856_call = mod.get_global_var('func_2856')
func_2858_call = mutated_mod.get_global_var('func_2858')
call_4551 = relay.TupleGetItem(func_2856_call(), 0)
call_4552 = relay.TupleGetItem(func_2858_call(), 0)
func_3733_call = mod.get_global_var('func_3733')
func_3737_call = mutated_mod.get_global_var('func_3737')
var_4555 = relay.var("var_4555", dtype = "float64", shape = ())#candidate|4555|()|var|float64
var_4556 = relay.var("var_4556", dtype = "float64", shape = (240,))#candidate|4556|(240,)|var|float64
call_4554 = relay.TupleGetItem(func_3733_call(relay.reshape(var_4555.astype('float64'), []), relay.reshape(var_4556.astype('float64'), [15, 8, 2]), ), 2)
call_4557 = relay.TupleGetItem(func_3737_call(relay.reshape(var_4555.astype('float64'), []), relay.reshape(var_4556.astype('float64'), [15, 8, 2]), ), 2)
output = relay.Tuple([call_4551,call_4554,var_4555,var_4556,])
output2 = relay.Tuple([call_4552,call_4557,var_4555,var_4556,])
func_4558 = relay.Function([var_4555,var_4556,], output)
mod['func_4558'] = func_4558
mod = relay.transform.InferType()(mod)
var_4559 = relay.var("var_4559", dtype = "float64", shape = ())#candidate|4559|()|var|float64
var_4560 = relay.var("var_4560", dtype = "float64", shape = (240,))#candidate|4560|(240,)|var|float64
output = func_4558(var_4559,var_4560,)
func_4561 = relay.Function([var_4559,var_4560,], output)
mutated_mod['func_4561'] = func_4561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2061_call = mod.get_global_var('func_2061')
func_2062_call = mutated_mod.get_global_var('func_2062')
call_4606 = relay.TupleGetItem(func_2061_call(), 0)
call_4607 = relay.TupleGetItem(func_2062_call(), 0)
output = call_4606
output2 = call_4607
func_4638 = relay.Function([], output)
mod['func_4638'] = func_4638
mod = relay.transform.InferType()(mod)
output = func_4638()
func_4639 = relay.Function([], output)
mutated_mod['func_4639'] = func_4639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2122_call = mod.get_global_var('func_2122')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_4643 = relay.TupleGetItem(func_2122_call(), 1)
call_4644 = relay.TupleGetItem(func_2124_call(), 1)
output = call_4643
output2 = call_4644
func_4647 = relay.Function([], output)
mod['func_4647'] = func_4647
mod = relay.transform.InferType()(mod)
mutated_mod['func_4647'] = func_4647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4647_call = mutated_mod.get_global_var('func_4647')
call_4648 = func_4647_call()
output = call_4648
func_4649 = relay.Function([], output)
mutated_mod['func_4649'] = func_4649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_527_call = mod.get_global_var('func_527')
func_529_call = mutated_mod.get_global_var('func_529')
call_4683 = relay.TupleGetItem(func_527_call(), 1)
call_4684 = relay.TupleGetItem(func_529_call(), 1)
func_4315_call = mod.get_global_var('func_4315')
func_4316_call = mutated_mod.get_global_var('func_4316')
call_4706 = func_4315_call()
call_4707 = func_4315_call()
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_4721 = relay.TupleGetItem(func_1638_call(relay.reshape(call_4683.astype('int8'), [13, 10, 3])), 0)
call_4722 = relay.TupleGetItem(func_1640_call(relay.reshape(call_4683.astype('int8'), [13, 10, 3])), 0)
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_4725 = relay.TupleGetItem(func_1638_call(relay.reshape(call_4683.astype('int8'), [13, 10, 3])), 0)
call_4726 = relay.TupleGetItem(func_1640_call(relay.reshape(call_4683.astype('int8'), [13, 10, 3])), 0)
func_1983_call = mod.get_global_var('func_1983')
func_1986_call = mutated_mod.get_global_var('func_1986')
const_4737 = relay.const(-7.079126, dtype = "float64")#candidate|4737|()|const|float64
var_4738 = relay.var("var_4738", dtype = "float64", shape = (400,))#candidate|4738|(400,)|var|float64
call_4736 = relay.TupleGetItem(func_1983_call(relay.reshape(const_4737.astype('float64'), []), relay.reshape(var_4738.astype('float64'), [5, 8, 10]), ), 0)
call_4739 = relay.TupleGetItem(func_1986_call(relay.reshape(const_4737.astype('float64'), []), relay.reshape(var_4738.astype('float64'), [5, 8, 10]), ), 0)
output = relay.Tuple([call_4683,call_4706,call_4721,call_4725,call_4736,const_4737,var_4738,])
output2 = relay.Tuple([call_4684,call_4707,call_4722,call_4726,call_4739,const_4737,var_4738,])
func_4758 = relay.Function([var_4738,], output)
mod['func_4758'] = func_4758
mod = relay.transform.InferType()(mod)
var_4759 = relay.var("var_4759", dtype = "float64", shape = (400,))#candidate|4759|(400,)|var|float64
output = func_4758(var_4759)
func_4760 = relay.Function([var_4759], output)
mutated_mod['func_4760'] = func_4760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_566_call = mod.get_global_var('func_566')
func_567_call = mutated_mod.get_global_var('func_567')
call_4822 = func_566_call()
call_4823 = func_566_call()
var_4836 = relay.var("var_4836", dtype = "bool", shape = (13, 10, 3))#candidate|4836|(13, 10, 3)|var|bool
bop_4837 = relay.bitwise_xor(call_4822.astype('uint8'), relay.reshape(var_4836.astype('uint8'), relay.shape_of(call_4822))) # shape=(13, 10, 3)
bop_4840 = relay.bitwise_xor(call_4823.astype('uint8'), relay.reshape(var_4836.astype('uint8'), relay.shape_of(call_4823))) # shape=(13, 10, 3)
output = bop_4837
output2 = bop_4840
func_4849 = relay.Function([var_4836,], output)
mod['func_4849'] = func_4849
mod = relay.transform.InferType()(mod)
mutated_mod['func_4849'] = func_4849
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4850 = relay.var("var_4850", dtype = "bool", shape = (13, 10, 3))#candidate|4850|(13, 10, 3)|var|bool
func_4849_call = mutated_mod.get_global_var('func_4849')
call_4851 = func_4849_call(var_4850)
output = call_4851
func_4852 = relay.Function([var_4850], output)
mutated_mod['func_4852'] = func_4852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_4870 = func_490_call()
call_4871 = func_490_call()
output = relay.Tuple([call_4870,])
output2 = relay.Tuple([call_4871,])
func_4889 = relay.Function([], output)
mod['func_4889'] = func_4889
mod = relay.transform.InferType()(mod)
output = func_4889()
func_4890 = relay.Function([], output)
mutated_mod['func_4890'] = func_4890
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4919 = relay.var("var_4919", dtype = "float64", shape = (3, 6, 8))#candidate|4919|(3, 6, 8)|var|float64
uop_4920 = relay.log(var_4919.astype('float64')) # shape=(3, 6, 8)
output = uop_4920
output2 = uop_4920
func_4930 = relay.Function([var_4919,], output)
mod['func_4930'] = func_4930
mod = relay.transform.InferType()(mod)
var_4931 = relay.var("var_4931", dtype = "float64", shape = (3, 6, 8))#candidate|4931|(3, 6, 8)|var|float64
output = func_4930(var_4931)
func_4932 = relay.Function([var_4931], output)
mutated_mod['func_4932'] = func_4932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3125_call = mod.get_global_var('func_3125')
func_3126_call = mutated_mod.get_global_var('func_3126')
call_4962 = relay.TupleGetItem(func_3125_call(), 0)
call_4963 = relay.TupleGetItem(func_3126_call(), 0)
output = relay.Tuple([call_4962,])
output2 = relay.Tuple([call_4963,])
func_4972 = relay.Function([], output)
mod['func_4972'] = func_4972
mod = relay.transform.InferType()(mod)
mutated_mod['func_4972'] = func_4972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4972_call = mutated_mod.get_global_var('func_4972')
call_4973 = func_4972_call()
output = call_4973
func_4974 = relay.Function([], output)
mutated_mod['func_4974'] = func_4974
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4977 = relay.var("var_4977", dtype = "float64", shape = (11, 10, 13))#candidate|4977|(11, 10, 13)|var|float64
var_4978 = relay.var("var_4978", dtype = "float64", shape = (11, 10, 13))#candidate|4978|(11, 10, 13)|var|float64
bop_4979 = relay.greater(var_4977.astype('bool'), relay.reshape(var_4978.astype('bool'), relay.shape_of(var_4977))) # shape=(11, 10, 13)
output = bop_4979
output2 = bop_4979
func_4982 = relay.Function([var_4977,var_4978,], output)
mod['func_4982'] = func_4982
mod = relay.transform.InferType()(mod)
mutated_mod['func_4982'] = func_4982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4982_call = mutated_mod.get_global_var('func_4982')
var_4984 = relay.var("var_4984", dtype = "float64", shape = (11, 10, 13))#candidate|4984|(11, 10, 13)|var|float64
var_4985 = relay.var("var_4985", dtype = "float64", shape = (11, 10, 13))#candidate|4985|(11, 10, 13)|var|float64
call_4983 = func_4982_call(var_4984,var_4985,)
output = call_4983
func_4986 = relay.Function([var_4984,var_4985,], output)
mutated_mod['func_4986'] = func_4986
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5017 = relay.var("var_5017", dtype = "uint8", shape = (13, 2, 5))#candidate|5017|(13, 2, 5)|var|uint8
const_5018 = relay.const([[[1,2,-9,2,-3],[9,1,-1,4,-10]],[[2,-3,4,-4,9],[2,3,3,-2,-2]],[[-3,2,-4,2,-4],[8,8,-6,-9,5]],[[-10,-9,2,7,-8],[-8,9,-5,-4,2]],[[-3,3,-4,-4,-7],[-2,-9,-2,-4,6]],[[7,2,-3,-2,6],[-2,-4,10,3,-2]],[[4,-9,-4,3,-1],[1,2,-5,-10,9]],[[-1,-3,-7,-7,-9],[-1,3,-6,-1,7]],[[10,2,-1,7,6],[-7,9,3,5,4]],[[-9,6,5,8,-5],[-9,-3,8,-10,5]],[[-3,2,-2,-7,7],[10,-8,-7,-10,-2]],[[10,-1,4,6,4],[-7,-2,8,6,-1]],[[-9,-10,-9,2,1],[-6,5,1,5,-3]]], dtype = "uint8")#candidate|5018|(13, 2, 5)|const|uint8
bop_5019 = relay.maximum(var_5017.astype('uint8'), relay.reshape(const_5018.astype('uint8'), relay.shape_of(var_5017))) # shape=(13, 2, 5)
func_2856_call = mod.get_global_var('func_2856')
func_2858_call = mutated_mod.get_global_var('func_2858')
call_5024 = relay.TupleGetItem(func_2856_call(), 0)
call_5025 = relay.TupleGetItem(func_2858_call(), 0)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_5043 = relay.TupleGetItem(func_1894_call(), 0)
call_5044 = relay.TupleGetItem(func_1896_call(), 0)
func_4647_call = mod.get_global_var('func_4647')
func_4649_call = mutated_mod.get_global_var('func_4649')
call_5046 = func_4647_call()
call_5047 = func_4647_call()
output = relay.Tuple([bop_5019,call_5024,call_5043,call_5046,])
output2 = relay.Tuple([bop_5019,call_5025,call_5044,call_5047,])
func_5052 = relay.Function([var_5017,], output)
mod['func_5052'] = func_5052
mod = relay.transform.InferType()(mod)
mutated_mod['func_5052'] = func_5052
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5053 = relay.var("var_5053", dtype = "uint8", shape = (13, 2, 5))#candidate|5053|(13, 2, 5)|var|uint8
func_5052_call = mutated_mod.get_global_var('func_5052')
call_5054 = func_5052_call(var_5053)
output = call_5054
func_5055 = relay.Function([var_5053], output)
mutated_mod['func_5055'] = func_5055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1394_call = mod.get_global_var('func_1394')
func_1396_call = mutated_mod.get_global_var('func_1396')
call_5128 = relay.TupleGetItem(func_1394_call(), 1)
call_5129 = relay.TupleGetItem(func_1396_call(), 1)
output = relay.Tuple([call_5128,])
output2 = relay.Tuple([call_5129,])
func_5131 = relay.Function([], output)
mod['func_5131'] = func_5131
mod = relay.transform.InferType()(mod)
mutated_mod['func_5131'] = func_5131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5131_call = mutated_mod.get_global_var('func_5131')
call_5132 = func_5131_call()
output = call_5132
func_5133 = relay.Function([], output)
mutated_mod['func_5133'] = func_5133
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5140 = relay.const([[[7,2,7,6],[3,-9,9,5]],[[-7,9,2,8],[-5,-2,-1,4]],[[6,-8,5,8],[-9,2,-10,-1]],[[-2,10,4,-7],[3,7,-10,2]]], dtype = "uint32")#candidate|5140|(4, 2, 4)|const|uint32
var_5141 = relay.var("var_5141", dtype = "uint32", shape = (4, 2, 4))#candidate|5141|(4, 2, 4)|var|uint32
bop_5142 = relay.less(const_5140.astype('bool'), relay.reshape(var_5141.astype('bool'), relay.shape_of(const_5140))) # shape=(4, 2, 4)
output = relay.Tuple([bop_5142,])
output2 = relay.Tuple([bop_5142,])
func_5145 = relay.Function([var_5141,], output)
mod['func_5145'] = func_5145
mod = relay.transform.InferType()(mod)
mutated_mod['func_5145'] = func_5145
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5146 = relay.var("var_5146", dtype = "uint32", shape = (4, 2, 4))#candidate|5146|(4, 2, 4)|var|uint32
func_5145_call = mutated_mod.get_global_var('func_5145')
call_5147 = func_5145_call(var_5146)
output = call_5147
func_5148 = relay.Function([var_5146], output)
mutated_mod['func_5148'] = func_5148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_5207 = relay.TupleGetItem(func_2584_call(), 0)
call_5208 = relay.TupleGetItem(func_2585_call(), 0)
func_3783_call = mod.get_global_var('func_3783')
func_3784_call = mutated_mod.get_global_var('func_3784')
call_5222 = relay.TupleGetItem(func_3783_call(), 1)
call_5223 = relay.TupleGetItem(func_3784_call(), 1)
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_5230 = func_490_call()
call_5231 = func_490_call()
output = relay.Tuple([call_5207,call_5222,call_5230,])
output2 = relay.Tuple([call_5208,call_5223,call_5231,])
func_5239 = relay.Function([], output)
mod['func_5239'] = func_5239
mod = relay.transform.InferType()(mod)
output = func_5239()
func_5240 = relay.Function([], output)
mutated_mod['func_5240'] = func_5240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_527_call = mod.get_global_var('func_527')
func_529_call = mutated_mod.get_global_var('func_529')
call_5258 = relay.TupleGetItem(func_527_call(), 1)
call_5259 = relay.TupleGetItem(func_529_call(), 1)
func_4123_call = mod.get_global_var('func_4123')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_5261 = func_4123_call()
call_5262 = func_4123_call()
bop_5272 = relay.equal(call_5258.astype('bool'), relay.reshape(call_5261.astype('bool'), relay.shape_of(call_5258))) # shape=(13, 10, 3)
bop_5275 = relay.equal(call_5259.astype('bool'), relay.reshape(call_5262.astype('bool'), relay.shape_of(call_5259))) # shape=(13, 10, 3)
output = relay.Tuple([bop_5272,])
output2 = relay.Tuple([bop_5275,])
func_5284 = relay.Function([], output)
mod['func_5284'] = func_5284
mod = relay.transform.InferType()(mod)
mutated_mod['func_5284'] = func_5284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5284_call = mutated_mod.get_global_var('func_5284')
call_5285 = func_5284_call()
output = call_5285
func_5286 = relay.Function([], output)
mutated_mod['func_5286'] = func_5286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_5297 = relay.TupleGetItem(func_2584_call(), 0)
call_5298 = relay.TupleGetItem(func_2585_call(), 0)
func_4558_call = mod.get_global_var('func_4558')
func_4561_call = mutated_mod.get_global_var('func_4561')
var_5311 = relay.var("var_5311", dtype = "float64", shape = ())#candidate|5311|()|var|float64
const_5312 = relay.const([[6.911006],[3.545919],[-8.668507],[-8.109635],[-7.398641],[-5.275611],[1.358625],[-7.874850],[-4.391631],[9.146486],[-0.516349],[-0.799690],[-3.637139],[-4.033177],[4.828562],[8.646607],[2.988497],[-3.436974],[-6.421366],[7.349081],[8.748459],[-2.680802],[-3.764260],[-5.663638],[3.860402],[-1.424499],[8.987563],[-5.231572],[-7.957169],[-2.078345],[3.253619],[0.784664],[-8.820199],[-3.792040],[-8.490225],[-3.724149],[-6.662055],[-8.251386],[2.373676],[6.666826],[-5.601872],[-7.778755],[-0.584019],[-8.110992],[9.552207],[-7.568170],[-9.257689],[2.541302],[9.859346],[3.756806],[3.623807],[-3.999180],[9.283946],[-7.209889],[1.783873],[5.615763],[4.734469],[2.349878],[-8.525698],[5.330188],[-7.661931],[9.940684],[3.641323],[-8.692003],[-6.757179],[-1.852975],[0.425629],[1.203610],[7.524052],[3.040539],[2.996841],[-6.864975],[-0.557478],[4.313331],[4.288050],[-5.762098],[-1.745087],[1.466724],[4.645461],[3.021035],[2.915319],[0.527496],[-1.050337],[2.102874],[5.302803],[-9.862603],[3.300549],[6.395580],[5.275494],[8.283335],[0.152167],[-1.873606],[4.127329],[0.863461],[2.011589],[-8.379414],[-2.536693],[9.117203],[6.505659],[-3.927244],[9.752786],[1.072001],[-6.620691],[-3.055338],[3.150787],[-7.198448],[-7.892583],[3.317460],[-6.042972],[-9.382029],[1.747815],[5.687309],[-3.607992],[-0.452886],[4.697812],[-0.033796],[0.274330],[-1.005191],[0.034530],[4.166483],[-7.331858],[2.311569],[7.653641],[-7.014395],[-4.190837],[9.409992],[6.838489],[2.920547],[-9.952952],[5.903465],[5.181171],[-7.166925],[-8.733901],[-3.324989],[-9.318459],[-7.907236],[3.021646],[3.517224],[-8.862235],[9.683188],[-9.436235],[-8.608246],[3.230054],[4.015519],[8.038027],[2.315172],[8.757068],[-1.539048],[-6.411260],[7.512381],[-7.390154],[2.341481],[8.213660],[-0.430657],[-5.334196],[-8.326772],[2.081032],[8.731506],[6.030441],[-8.993706],[4.646955],[5.270877],[6.976246],[-4.207397],[-6.273323],[-3.751699],[-0.786625],[-4.160656],[-5.794648],[0.828091],[-2.132463],[6.770588],[2.543883],[-8.230517],[-9.138022],[1.950422],[0.453364],[-5.044951],[-2.881345],[-8.644866],[-0.283246],[-7.580753],[8.165753],[-6.831930],[8.620450],[-8.948446],[-8.134839],[7.287752],[-0.178727],[-7.712602],[-5.247516],[7.575659],[-5.474528],[8.268028],[-0.726042],[0.514697],[-5.593769],[0.240174],[-2.215063],[-5.089888],[-4.106891],[-7.821767],[-0.642036],[-7.976675],[9.289712],[2.138926],[-6.869163],[0.364634],[-3.392435],[-9.048017],[4.930823],[9.129582],[6.578711],[9.003364],[3.051001],[1.880809],[-8.573542],[-3.511893],[-5.499429],[-1.385036],[6.307635],[6.504882],[-0.849313],[-4.410274],[4.140213],[4.370396],[-7.908180],[5.196875],[-5.114732],[6.447847],[-0.521162],[6.930923],[-8.747498],[7.900445],[-4.861128],[7.268817],[-6.281682],[7.970278],[5.466393],[1.110211]], dtype = "float64")#candidate|5312|(240, 1)|const|float64
call_5310 = relay.TupleGetItem(func_4558_call(relay.reshape(var_5311.astype('float64'), []), relay.reshape(const_5312.astype('float64'), [240,]), ), 0)
call_5313 = relay.TupleGetItem(func_4561_call(relay.reshape(var_5311.astype('float64'), []), relay.reshape(const_5312.astype('float64'), [240,]), ), 0)
output = relay.Tuple([call_5297,call_5310,var_5311,const_5312,])
output2 = relay.Tuple([call_5298,call_5313,var_5311,const_5312,])
func_5319 = relay.Function([var_5311,], output)
mod['func_5319'] = func_5319
mod = relay.transform.InferType()(mod)
mutated_mod['func_5319'] = func_5319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5320 = relay.var("var_5320", dtype = "float64", shape = ())#candidate|5320|()|var|float64
func_5319_call = mutated_mod.get_global_var('func_5319')
call_5321 = func_5319_call(var_5320)
output = call_5321
func_5322 = relay.Function([var_5320], output)
mutated_mod['func_5322'] = func_5322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mod.get_global_var('func_1759')
func_1761_call = mutated_mod.get_global_var('func_1761')
call_5326 = func_1759_call()
call_5327 = func_1759_call()
func_4054_call = mod.get_global_var('func_4054')
func_4057_call = mutated_mod.get_global_var('func_4057')
var_5336 = relay.var("var_5336", dtype = "float64", shape = ())#candidate|5336|()|var|float64
const_5337 = relay.const([0.288447,1.400431,8.541397,-6.458202,-5.992960,9.426832,-9.832998,1.232338,-9.095634,-3.577987,-8.302014,-7.551399,0.033686,-5.498706,7.987507,-4.463320,-8.022776,6.299432,-3.895120,1.989033,2.826585,-5.464839,8.406469,-5.515110,9.985163,-0.795562,3.812054,-3.730958,4.815979,-2.933025,-4.707737,3.556987,-3.662205,-2.038866,-8.986010,-5.191217,-6.008554,5.385483,-4.113284,3.256192,8.754155,-2.878436,5.475095,1.418044,6.893086,4.055789,-6.886402,7.606583,1.883844,2.532330,1.322080,7.907273,8.708127,3.102589,-9.998010,7.205717,-9.811884,2.562648,-5.398729,-5.974704,-9.885402,-6.738448,-5.111127,7.981952,1.097076,-4.512306,-8.657828,7.817734,-5.111639,-0.435401,3.639663,-3.009724,2.154733,3.534249,-9.859861,2.290347,5.883563,7.213170,1.914751,-4.904851,-2.947109,4.304365,-7.963795,-5.034730,-3.365481,-8.500506,-3.656247,9.215913,-6.316756,6.444638,0.013907,3.658625,-1.748082,-6.135026,7.208721,3.563516,4.747699,8.499447,6.071607,1.705345,-6.167921,6.084229,-1.991681,-7.826004,-2.542096,-1.547542,-5.539578,-7.776460,-6.301581,3.441330,6.716619,5.664458,0.872235,5.140339,-2.595943,-1.432166,-1.631008,2.592420,0.466042,2.743633,-6.836886,8.687497,4.545456,5.203841,-4.454524,6.303037,2.162681,6.692257,9.880782,1.783528,1.357260,-6.409130,-8.234416,-6.173105,5.271798,9.091047,0.843424,4.428876,-9.290837,4.263318,4.138289,0.608692,8.954037,9.848515,3.655209,7.610341,5.551142,-7.638120,1.259682,5.844110,-9.118821,-2.519689,1.404925,-7.342629,4.150082,-6.323414,-3.318969,9.892937,-2.156414,2.747160,-5.596103,-1.357300,-6.905307,6.971113,-8.914296,1.795151,8.826722,-5.008034,5.449720,-9.991092,-7.114107,5.618429,-1.195173,2.732835,0.092136,-3.862493,5.484173,6.989870,9.483389,3.424297,5.812127,-9.954124,2.199832,5.046253,8.121501,6.705500,4.811986,1.344192,7.612733,-2.316372,3.629166,-9.897150,-8.907292,-6.735177,-3.712972,9.356144,-8.087892,-2.006886,-2.148547,-0.368447,-9.126050,-9.806276,-4.530868,5.247643,-5.268890,8.496249,8.621346,-4.643002,2.460305,6.182829,-0.401769,-3.904083,3.035745,-0.228451,-8.171154,2.596600,-2.694626,-4.322392,0.305785,9.362394,-6.480024,2.289930,-2.185566,4.608264,8.198904,-8.381838,1.587432,-6.670162,4.762061,-1.920066,-4.295328,-6.805923,9.606910,8.051742,2.126716,-8.395177,2.904724,9.733518,4.307078,-1.752501], dtype = "float64")#candidate|5337|(240,)|const|float64
call_5335 = relay.TupleGetItem(func_4054_call(relay.reshape(var_5336.astype('float64'), []), relay.reshape(const_5337.astype('float64'), [240,]), ), 1)
call_5338 = relay.TupleGetItem(func_4057_call(relay.reshape(var_5336.astype('float64'), []), relay.reshape(const_5337.astype('float64'), [240,]), ), 1)
output = relay.Tuple([call_5326,call_5335,var_5336,const_5337,])
output2 = relay.Tuple([call_5327,call_5338,var_5336,const_5337,])
func_5339 = relay.Function([var_5336,], output)
mod['func_5339'] = func_5339
mod = relay.transform.InferType()(mod)
mutated_mod['func_5339'] = func_5339
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5340 = relay.var("var_5340", dtype = "float64", shape = ())#candidate|5340|()|var|float64
func_5339_call = mutated_mod.get_global_var('func_5339')
call_5341 = func_5339_call(var_5340)
output = call_5341
func_5342 = relay.Function([var_5340], output)
mutated_mod['func_5342'] = func_5342
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5384 = relay.const([[[-3.567874,0.882653,7.642070,2.490036,5.737848,8.953398,7.974194,-4.622176,-3.351307,9.748114,-7.915938,1.879848,-6.338268],[4.431152,8.496731,-9.570978,0.271437,-4.979203,4.691450,-4.988696,-0.752798,2.619345,-9.993269,-3.416831,-5.109969,9.523013],[4.589708,-3.306099,8.825226,6.870271,-0.249454,-1.544707,-8.913899,1.228256,-0.852197,-1.108891,2.506300,-5.752790,7.352250],[-5.325648,-3.535845,-9.022613,2.936656,5.102501,-4.762724,9.752876,-7.321168,-4.333689,-2.827795,-6.030666,9.701665,-4.672551],[9.294725,-4.348368,0.484963,-6.980582,-1.615217,8.364045,-1.775623,-4.295480,-2.595172,2.244737,5.031484,1.353347,6.152390],[2.058741,-1.862303,6.962326,-9.821601,-0.545457,6.830563,-1.352279,1.160069,5.877289,-6.840003,-6.477555,9.349765,-9.615440],[0.540606,2.640437,3.079248,5.016620,-0.974544,9.722113,-6.102794,-4.751704,5.733234,-2.135256,-1.951833,-5.678902,3.908472],[1.767530,-6.919765,-8.207401,7.747610,4.588016,-3.653448,-0.697274,0.197833,4.790438,4.676023,5.235718,-7.233918,8.253097],[8.736621,-8.679485,-6.145309,-5.288664,8.444050,-5.065985,-1.492458,5.629106,-6.053762,9.485501,-8.394545,-1.000140,-5.629008],[-6.984446,5.653447,2.418758,2.333217,8.635017,-6.535310,-2.147453,-8.077589,-8.352013,-8.516220,9.862122,-3.556130,4.074657],[-5.542032,-8.644177,2.962943,0.601008,3.598717,-1.389791,-8.106153,-4.242296,2.212361,-3.729314,-9.870470,-7.090067,4.047987]],[[0.714710,-1.205618,-8.356385,-0.953171,9.899475,5.814173,-1.259539,2.437734,0.901017,1.496957,-9.361786,-9.898113,-1.879585],[-7.184559,-2.262954,0.283150,9.358006,-0.173492,-4.768047,-7.849017,-4.293785,-2.394915,-6.692224,0.002297,-1.368922,-5.633398],[2.986481,7.975734,9.023093,-7.823759,7.052898,6.311489,8.059404,-3.302162,2.170530,7.865925,-7.941691,-4.012857,-6.879541],[-1.163628,-4.581433,3.358478,-3.127891,-5.442315,-3.510230,1.444458,-3.101177,-2.654605,-8.563813,0.268829,-1.926275,6.280078],[-0.716596,1.595175,-0.881754,7.268081,-8.351943,-3.845874,-0.786257,-5.939076,-5.714124,-6.861568,4.383699,-6.156287,-1.804254],[6.625841,9.123331,0.545478,-0.312203,-2.787406,1.192814,-8.592894,-3.593863,-3.465785,2.133337,-2.924071,-7.509229,-0.135741],[7.393676,5.143454,-3.940833,-4.704756,6.694398,4.431566,1.477011,-6.932772,-7.974041,-4.704534,-8.002450,4.241445,-5.202945],[2.391531,-6.964615,-9.904174,-3.154680,0.480213,-3.817029,-2.077587,-4.860427,7.767644,7.766251,-3.251480,-6.452888,7.610436],[3.356301,-7.529695,-3.798596,-2.797722,7.206857,-0.835850,-3.081544,-8.958798,-1.465016,-1.984306,5.831995,-9.171158,-2.086956],[-0.980040,8.627406,4.550588,-3.103765,-1.380862,2.102052,4.442608,2.233146,-3.490474,-7.226229,-8.217103,-1.806234,3.944272],[7.905772,-8.808017,-3.648028,-6.702391,-5.540353,-5.219443,-0.809055,7.205389,0.910193,-6.512844,0.706629,-2.966616,-1.076638]],[[-1.732521,0.534415,-8.804336,8.648207,-6.635668,4.997420,9.959203,-3.428394,-8.864590,3.049345,-5.586249,-2.691758,3.106239],[-6.275041,8.648169,6.757476,2.752266,1.104407,8.467230,-0.426676,-0.716542,-2.861293,-3.324250,3.804107,5.076211,-1.439289],[9.343814,9.552479,-3.024919,-6.884169,-2.798267,5.683169,8.179493,5.936080,6.181601,-7.689110,5.059941,-5.019511,-1.090293],[-1.817658,-8.907054,5.193068,3.209317,-7.778407,-5.342207,-1.063550,-6.585329,-1.336112,-4.557395,-1.931816,-9.960199,-7.861091],[-7.578989,8.321818,-1.287234,-8.132208,-3.507326,3.016317,-9.951916,-9.311000,-3.845446,7.833707,-6.313740,-7.792521,9.427214],[1.113768,-3.648366,8.152643,-8.382832,3.418822,-1.478670,8.111518,1.695554,5.993920,-9.581593,7.956379,-2.385028,-4.554080],[-1.526903,4.499385,0.597397,0.381671,-2.878588,-8.190295,2.809427,-0.049536,-4.793423,0.330629,-7.458840,5.457740,-7.331828],[4.440157,-6.392893,8.853939,8.203371,-2.525018,5.650063,-0.491403,7.492353,-2.286348,-0.664502,-7.925991,-8.898344,-2.787269],[-5.776868,-2.182043,-0.492822,2.831259,9.699929,-1.354853,-8.569356,1.113920,-6.975858,1.743618,4.564508,0.586733,-4.901107],[-9.631345,2.819174,5.497470,-1.923838,-3.765888,-1.886850,9.548878,-5.667741,-3.894085,7.718963,3.280767,8.369139,5.795079],[-0.116465,-1.897727,-5.116570,-1.290022,6.835293,-9.375646,9.800366,9.709710,-8.669378,7.046196,-8.426313,1.655925,3.117399]]], dtype = "float64")#candidate|5384|(3, 11, 13)|const|float64
uop_5385 = relay.acos(const_5384.astype('float64')) # shape=(3, 11, 13)
const_5387 = relay.const([[[-1.980398,-5.135286,-1.384017,9.485529,-8.283789,-7.103491,-1.202576,-9.685892,-5.579407,-8.692380,-2.883138,4.986439,8.884573],[-5.282454,-6.258570,2.850534,2.511595,-8.446578,9.823139,-4.498481,-6.596364,-7.954173,7.415870,9.120797,6.474844,-9.591762],[0.793293,0.379639,-7.194138,3.807160,-6.962552,8.713584,-7.760815,2.971033,5.687157,4.864314,-5.498469,-4.533344,4.744825],[3.700412,2.686849,-5.454819,-2.295719,3.662795,2.701015,2.661239,-4.926172,4.463063,5.718486,-2.608654,0.891024,-0.842491],[-5.925969,3.433266,-6.822396,-2.046894,-1.030433,2.949073,-6.439312,3.362579,5.284618,6.879620,-5.516982,-5.558284,-5.506569],[-5.071942,-4.568153,4.567207,-9.560101,-0.466729,-1.119654,-5.606192,-9.463654,5.350114,6.107799,-6.089358,3.178416,-8.520300],[5.937704,2.289606,6.934217,0.626660,4.265844,-8.962850,4.959211,-5.402319,1.759415,-2.282806,-2.484750,8.646543,-9.357930],[-1.653804,9.096629,5.069531,2.622368,-9.377087,8.556644,4.032332,8.435239,-2.678376,-4.952713,-5.988918,8.005156,2.880079],[-0.622532,8.763377,6.768432,-6.322302,-6.141963,8.797451,7.991037,3.664578,1.565990,6.944186,-6.490024,2.903750,-1.847406],[1.377373,-6.442926,-4.165515,3.670009,3.249750,4.082776,9.355044,-5.466617,-6.340388,2.251949,-1.893973,-9.468198,9.750944],[4.330964,8.184938,-4.143144,3.655241,-8.455878,9.790448,-5.892776,-9.045763,-7.593920,2.018696,-4.936820,-5.687323,7.305404]],[[-0.918883,-6.069013,2.319694,-7.200636,-4.026212,5.077409,5.928315,2.076561,2.455945,3.846579,8.576158,3.238557,-8.219560],[-3.314931,2.631937,2.419952,0.052837,7.119692,0.840182,-8.143559,-6.399489,-5.633600,1.333206,-7.235489,4.118617,-7.115444],[-6.147319,5.893061,6.796234,3.534738,-4.416488,-1.946110,7.209493,-3.060729,1.456101,-5.769370,-0.959851,6.532037,-9.875617],[-0.699049,2.670469,-9.083969,-8.487641,7.351840,-1.615527,1.894540,4.833662,-7.034921,8.010364,-8.597445,3.857526,4.915939],[6.562752,3.295749,-4.570602,2.815373,-1.337480,0.582673,8.397985,-2.249795,-3.952403,-2.783994,5.106201,-8.740991,0.741649],[5.450793,9.342136,-8.251920,6.772898,-6.952327,8.150576,-3.088469,9.300806,8.242343,-3.809176,-2.908966,8.096802,-0.927368],[-4.240682,0.269471,1.590807,-5.326849,0.223142,2.685782,8.136186,8.870465,8.713828,-3.337437,1.498545,-6.010710,-6.760742],[-7.571661,1.780822,-5.329050,5.249337,-9.926158,3.524320,6.934746,0.082636,7.538694,-6.717523,-5.950798,-6.571822,4.501829],[-2.950728,9.020145,-7.473942,-9.549594,9.919689,4.263067,-7.163038,4.218985,8.169400,6.276279,-5.863184,7.276138,6.373532],[-4.246126,-2.231111,8.496485,0.423723,5.578392,7.426108,-5.032437,2.252795,2.813676,2.933383,5.638410,-9.050497,1.622170],[6.644959,8.593205,-4.876521,4.865902,0.565955,7.684872,1.712451,7.096766,-7.214316,1.680045,9.396523,-1.053161,-8.084869]],[[9.853842,-2.501413,7.233325,3.476803,-3.604428,-4.782631,7.696464,-7.495572,5.193455,2.020455,-2.516186,-6.078083,3.459432],[0.563456,-1.260274,3.081155,-8.554330,-9.753565,-0.324637,-7.956801,-8.183835,-6.209031,1.932684,-1.713668,-2.109064,3.010087],[-3.529034,8.992405,8.602375,5.753453,-8.626432,-3.842680,-3.130089,-7.440860,-8.150397,9.605742,7.782949,-4.525782,-1.191975],[3.460034,0.164498,-7.113196,-5.190170,7.529784,-2.616279,2.386551,-6.083668,2.191792,1.465178,2.416976,-7.029023,-1.745079],[-4.463784,-7.902011,8.452188,8.511369,-3.837468,-4.231002,0.024101,3.990947,-3.119601,-2.667454,-3.742327,4.753656,3.535343],[5.245295,7.327895,-4.454551,3.113288,5.219385,-8.631953,1.489898,-6.483450,-7.486938,1.948657,1.937125,-7.715100,-0.240976],[0.355410,-7.830853,-4.542442,-8.815372,0.209770,9.689463,-6.576466,-8.658723,-2.099789,0.301969,2.750452,-9.726518,6.529283],[1.869561,-6.694214,-0.158505,3.137040,-9.061203,7.623674,-6.687205,6.916651,9.416030,-6.581378,0.929277,5.177916,3.752590],[-5.335331,0.199333,4.157761,1.564202,3.472863,8.604991,4.113809,-6.848214,-9.613977,3.477091,9.570803,7.975173,-8.071054],[-5.959161,-3.712479,3.979996,2.612947,-0.964233,3.609352,-9.834437,-3.982992,0.946255,-5.666940,-7.363312,-0.620771,-6.235447],[-4.082732,6.357754,-3.355028,-9.806614,9.284176,9.863665,-6.902968,2.395137,-7.254017,-7.759922,9.144019,-9.071845,-7.235389]]], dtype = "float64")#candidate|5387|(3, 11, 13)|const|float64
bop_5388 = relay.add(uop_5385.astype('int8'), relay.reshape(const_5387.astype('int8'), relay.shape_of(uop_5385))) # shape=(3, 11, 13)
output = relay.Tuple([bop_5388,])
output2 = relay.Tuple([bop_5388,])
func_5395 = relay.Function([], output)
mod['func_5395'] = func_5395
mod = relay.transform.InferType()(mod)
mutated_mod['func_5395'] = func_5395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5395_call = mutated_mod.get_global_var('func_5395')
call_5396 = func_5395_call()
output = call_5396
func_5397 = relay.Function([], output)
mutated_mod['func_5397'] = func_5397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3246_call = mod.get_global_var('func_3246')
func_3247_call = mutated_mod.get_global_var('func_3247')
call_5401 = func_3246_call()
call_5402 = func_3246_call()
output = call_5401
output2 = call_5402
func_5403 = relay.Function([], output)
mod['func_5403'] = func_5403
mod = relay.transform.InferType()(mod)
mutated_mod['func_5403'] = func_5403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5403_call = mutated_mod.get_global_var('func_5403')
call_5404 = func_5403_call()
output = call_5404
func_5405 = relay.Function([], output)
mutated_mod['func_5405'] = func_5405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_350_call = mutated_mod.get_global_var('func_350')
call_5414 = func_348_call()
call_5415 = func_348_call()
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_5420 = relay.TupleGetItem(func_1128_call(), 0)
call_5421 = relay.TupleGetItem(func_1129_call(), 0)
output = relay.Tuple([call_5414,call_5420,])
output2 = relay.Tuple([call_5415,call_5421,])
func_5430 = relay.Function([], output)
mod['func_5430'] = func_5430
mod = relay.transform.InferType()(mod)
output = func_5430()
func_5431 = relay.Function([], output)
mutated_mod['func_5431'] = func_5431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5284_call = mod.get_global_var('func_5284')
func_5286_call = mutated_mod.get_global_var('func_5286')
call_5461 = relay.TupleGetItem(func_5284_call(), 0)
call_5462 = relay.TupleGetItem(func_5286_call(), 0)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_5469 = func_3670_call()
call_5470 = func_3670_call()
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_5502 = relay.TupleGetItem(func_2781_call(), 0)
call_5503 = relay.TupleGetItem(func_2782_call(), 0)
func_1949_call = mod.get_global_var('func_1949')
func_1950_call = mutated_mod.get_global_var('func_1950')
call_5504 = relay.TupleGetItem(func_1949_call(), 1)
call_5505 = relay.TupleGetItem(func_1950_call(), 1)
output = relay.Tuple([call_5461,call_5469,call_5502,call_5504,])
output2 = relay.Tuple([call_5462,call_5470,call_5503,call_5505,])
func_5507 = relay.Function([], output)
mod['func_5507'] = func_5507
mod = relay.transform.InferType()(mod)
mutated_mod['func_5507'] = func_5507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5507_call = mutated_mod.get_global_var('func_5507')
call_5508 = func_5507_call()
output = call_5508
func_5509 = relay.Function([], output)
mutated_mod['func_5509'] = func_5509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_5527 = relay.TupleGetItem(func_1574_call(), 4)
call_5528 = relay.TupleGetItem(func_1576_call(), 4)
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
const_5532 = relay.const([1,4,5,8,-9,-2,-4,3,4,-7,10,-2,8,-10,-9,7,-6,-5,-2,10,-9,-2,-3,-5,9,-2,1,-1,-4,-6,-1,6,-3,-8,-4,-6,-1,6,-3,4,2,-3,2,4,7,10,2,-5,6,9,4,-5,-4,-10,3,-1,10,7,-1,9,-10,6,-6,6,6,6,-1,-6,3,1,10,2,-9,-5,2,8,4,6,7,-3,-7,5,-9,2,7,-9,-7,-10,-2,7,-6,5,-1,9,3,2,-1,10,8,-10,-5,-3,-10,9,7,-5,10,-4,-3,10,-4,-7,-1,-5,-7,5,5,-6,-2,-8,-2,-3,-5,5,1,5,10,-10,-9,4,-1,-9,9,-1,10,-2,-2,-5,4,-4,-7,-10,-3,10,7,-7,4,-3,9,6,3,4,-6,2,-8,3,-9,4,3,-1,9,9,2,-6,7,-4,3,8,6,-7,8,2,3,9,-10,-10,-8,2,-2,5,-2,10,7,-5,7,7,-4,-5,5,-6,-6,-5,5,4,-8,7,-8,-7,6,-7,-6,2,-3,8,3,-4,2,3,7,-7,6,4,2,10,5,-2,-2,-2,1,5,-8,3,10,-7,3,1,9,-5,1,8,-3,-9,-5,1,3,-10,-5,-10,8,4,-1,-1,4,-1,3,1,10,-2,10,-10,9,3,2,-1,-1,2,-1,4,10,8,-7,-1,8,-3,-9,3,-5,-6,-10,-7,-3,4,-1,9,6,-7,8,-9,3,7,4,-4,8,6,-8,-10,-2,-4,5,-6,-1,-1,1,5,1,-10,4,2,3,-10,2,1,-4,-9,-6,-7,8,-6,-7,4,3,-3,-7,8,4,10,-8,10,-4,9,3,-7,-6,-1,3,3,9,-4,-10,8,-2,9,-9,-10,-9,-5,8,5,-6,-9,2,-9,-7,-1,7,2,-8,-7,-10,-2,-9,1,-10,3,3,-8,-5,9,-10,-8,10,4,1,-4,2,1,-4,1,1,1,8,-2,-6,5,-1,-1,-5,6,-10,-8,-8,-6,-3,6,2,9,-9,-5,2,-9], dtype = "int8")#candidate|5532|(390,)|const|int8
call_5531 = relay.TupleGetItem(func_1638_call(relay.reshape(const_5532.astype('int8'), [13, 10, 3])), 2)
call_5533 = relay.TupleGetItem(func_1640_call(relay.reshape(const_5532.astype('int8'), [13, 10, 3])), 2)
output = relay.Tuple([call_5527,call_5531,const_5532,])
output2 = relay.Tuple([call_5528,call_5533,const_5532,])
func_5539 = relay.Function([], output)
mod['func_5539'] = func_5539
mod = relay.transform.InferType()(mod)
output = func_5539()
func_5540 = relay.Function([], output)
mutated_mod['func_5540'] = func_5540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4103_call = mod.get_global_var('func_4103')
func_4104_call = mutated_mod.get_global_var('func_4104')
call_5549 = relay.TupleGetItem(func_4103_call(), 1)
call_5550 = relay.TupleGetItem(func_4104_call(), 1)
const_5558 = relay.const([[[True,False,False],[False,True,False],[True,True,False],[False,False,False],[True,True,False],[False,True,True],[False,True,True],[False,True,True],[True,True,False],[False,True,True]],[[False,True,True],[False,True,True],[False,False,False],[False,True,False],[True,False,True],[True,False,True],[False,True,False],[False,True,True],[True,True,False],[False,True,False]],[[True,True,True],[False,False,False],[True,False,True],[False,True,False],[False,False,False],[False,True,False],[True,True,True],[True,True,True],[True,True,False],[True,True,True]],[[True,False,False],[False,False,False],[True,False,True],[False,False,False],[False,False,False],[False,False,True],[False,True,False],[False,True,False],[True,False,True],[True,True,False]],[[False,True,False],[False,True,False],[True,False,False],[False,False,False],[False,False,True],[False,False,True],[True,True,True],[True,True,False],[True,False,False],[False,True,True]],[[False,True,False],[False,True,False],[True,False,False],[True,False,True],[False,False,True],[True,False,False],[False,True,True],[True,True,False],[True,False,False],[True,True,True]],[[True,True,False],[True,False,True],[True,True,False],[False,False,False],[True,False,True],[False,True,True],[False,False,True],[True,True,False],[True,True,False],[True,False,True]],[[False,True,True],[False,True,True],[False,False,False],[False,False,False],[False,True,True],[True,False,False],[True,False,False],[False,False,False],[False,True,True],[False,True,True]],[[False,True,True],[True,False,False],[False,False,False],[False,False,True],[False,False,False],[True,False,False],[False,True,True],[False,True,True],[False,True,False],[True,True,True]],[[True,True,True],[False,False,True],[False,False,True],[False,False,True],[True,True,True],[False,False,True],[False,False,False],[True,True,True],[False,True,False],[True,True,False]],[[False,False,True],[True,False,False],[False,False,False],[True,False,True],[False,False,False],[False,False,False],[True,False,True],[False,False,False],[True,False,True],[False,True,False]],[[False,False,False],[True,True,False],[True,False,False],[False,True,True],[True,False,True],[True,False,True],[True,True,True],[False,True,True],[False,True,False],[False,True,True]],[[False,True,True],[True,False,True],[True,False,True],[False,False,False],[True,True,False],[False,False,False],[True,True,False],[False,False,True],[False,False,False],[False,False,True]]], dtype = "bool")#candidate|5558|(13, 10, 3)|const|bool
bop_5559 = relay.power(call_5549.astype('float32'), relay.reshape(const_5558.astype('float32'), relay.shape_of(call_5549))) # shape=(13, 10, 3)
bop_5562 = relay.power(call_5550.astype('float32'), relay.reshape(const_5558.astype('float32'), relay.shape_of(call_5550))) # shape=(13, 10, 3)
output = relay.Tuple([bop_5559,])
output2 = relay.Tuple([bop_5562,])
func_5586 = relay.Function([], output)
mod['func_5586'] = func_5586
mod = relay.transform.InferType()(mod)
output = func_5586()
func_5587 = relay.Function([], output)
mutated_mod['func_5587'] = func_5587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_5632 = func_1850_call()
call_5633 = func_1850_call()
output = call_5632
output2 = call_5633
func_5646 = relay.Function([], output)
mod['func_5646'] = func_5646
mod = relay.transform.InferType()(mod)
mutated_mod['func_5646'] = func_5646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5646_call = mutated_mod.get_global_var('func_5646')
call_5647 = func_5646_call()
output = call_5647
func_5648 = relay.Function([], output)
mutated_mod['func_5648'] = func_5648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_5655 = relay.TupleGetItem(func_281_call(), 0)
call_5656 = relay.TupleGetItem(func_282_call(), 0)
output = call_5655
output2 = call_5656
func_5660 = relay.Function([], output)
mod['func_5660'] = func_5660
mod = relay.transform.InferType()(mod)
mutated_mod['func_5660'] = func_5660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5660_call = mutated_mod.get_global_var('func_5660')
call_5661 = func_5660_call()
output = call_5661
func_5662 = relay.Function([], output)
mutated_mod['func_5662'] = func_5662
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5668 = relay.var("var_5668", dtype = "float32", shape = (15, 3, 13))#candidate|5668|(15, 3, 13)|var|float32
uop_5669 = relay.cosh(var_5668.astype('float32')) # shape=(15, 3, 13)
bop_5682 = relay.bitwise_xor(uop_5669.astype('uint16'), relay.reshape(var_5668.astype('uint16'), relay.shape_of(uop_5669))) # shape=(15, 3, 13)
const_5685 = relay.const([[[1.765731,7.939130,0.781636,3.315796,-9.995206,-2.178944,-7.369968,-9.170040,9.112078,-2.096781,7.884407,-7.012037,-6.502138],[-8.299651,7.047483,7.068710,5.814534,9.818712,1.022758,-3.542925,8.951617,6.452133,-4.035277,-6.200721,-6.919492,-9.074587],[3.809271,-9.931798,-9.087231,-4.863553,4.394950,1.329290,6.433971,7.262087,2.428210,-4.319540,-0.636956,-2.879490,8.196560]],[[-5.838858,7.577591,7.758074,4.716298,4.264156,8.653299,1.617440,3.358150,6.238401,3.207926,1.652810,-1.925752,1.830247],[-9.178573,3.945388,5.232955,9.667577,3.389076,8.101420,4.229756,-5.912417,4.227558,2.172149,-1.198471,1.177392,7.756536],[0.228417,-3.124654,-4.257217,-4.695010,-1.938571,9.258528,0.372075,-5.349478,-7.502902,1.492798,-4.671728,-7.168349,9.579985]],[[-0.969928,2.704844,0.572787,6.262417,6.775221,-5.303615,-2.019395,6.418568,9.791816,-6.416678,-8.091620,7.317775,8.992339],[-8.066594,1.861773,6.296987,-9.833174,2.071164,4.231306,8.503487,-4.448877,-6.963729,-1.442137,-1.689967,-4.697080,1.657243],[3.396335,-9.604668,3.451750,5.363910,-8.176699,-1.875566,5.014444,5.916319,8.056801,5.769495,-9.175292,-5.786485,-7.617284]],[[-3.464093,5.072991,8.948098,-5.422645,1.267244,-8.487607,-8.014550,8.507039,3.302000,-0.518028,5.204906,4.336991,6.151053],[0.884529,-5.533634,1.847064,-9.181454,-1.610154,0.811770,-3.413188,-3.101579,6.215712,1.936966,-7.555065,6.012723,5.448381],[-0.752596,-6.170900,3.467185,1.623345,7.248729,-0.464028,8.047219,4.300556,-6.078228,7.653126,-4.416097,8.362472,-1.767815]],[[-9.741653,8.427482,-9.847286,-3.050024,3.020801,-6.121381,8.541325,8.536703,-2.857651,-3.730661,-9.159737,5.841938,-6.639453],[-6.211807,7.005262,8.519921,4.959332,-7.020351,-7.594156,-2.994356,-6.766174,-0.196561,-0.487165,8.468520,-8.799651,-7.940994],[-8.733136,-4.146291,6.499670,2.968178,5.697590,-1.926887,5.681666,2.458477,5.959005,7.146622,-3.105323,1.063381,-9.313373]],[[3.007561,-2.978401,6.472461,1.037269,5.325910,-5.165335,-3.257716,7.671938,-7.203167,6.677421,-3.650402,2.235193,-5.171312],[8.965497,-1.881356,-8.343355,-9.999451,8.823443,-0.110033,-9.576091,8.184029,-5.517862,-9.437727,-5.712280,-8.455789,-4.322712],[-1.246607,-5.476875,-1.071293,-7.738516,2.124551,-5.702071,-8.228384,4.678201,3.667941,-9.744195,0.077043,-5.020951,0.302711]],[[-6.801107,-9.214221,-4.512519,7.305463,4.997879,0.069701,-2.582764,-9.807175,-0.876443,5.237690,3.393816,6.549586,2.842185],[-9.132247,0.781094,2.808796,4.872112,-9.457034,-4.525840,6.179172,6.804932,-4.890845,8.905124,6.732673,2.586968,-2.728535],[3.687158,-0.765579,-3.750339,-8.024331,-3.779165,6.011452,0.604768,-9.449091,7.701136,7.863909,-8.414393,2.729401,-8.607956]],[[9.238343,1.417378,2.864214,-6.338130,0.648458,-0.455997,-9.367123,0.423893,7.093251,4.226601,0.025286,6.428148,-2.395158],[-3.395456,9.065870,-1.689876,-7.558929,-2.861123,-5.706188,1.487491,1.981060,2.125229,5.475976,-5.798483,6.674175,-7.901335],[-7.498692,3.595224,0.551864,-7.236262,-4.583477,7.528119,-2.568602,-2.237157,-8.720896,5.156450,-1.887290,1.422214,2.197240]],[[-7.594992,-9.507116,6.373003,-8.464726,6.204238,-4.797733,-0.402433,-6.491656,1.154032,-4.331084,8.430579,-6.172054,-1.749769],[8.842822,-7.540889,4.148353,1.165608,4.526526,9.351200,8.221519,0.293996,-4.602061,-0.401214,5.557985,-9.107859,-8.712851],[1.299584,-1.587873,5.813953,7.452159,-4.080569,-5.307666,-9.409884,0.630165,0.781295,-3.013829,-9.738919,-8.629714,1.840232]],[[3.518607,0.989256,6.690139,-6.113395,1.342925,7.429467,3.667445,7.495010,0.134838,1.041400,2.256697,4.295493,3.892993],[7.188228,1.275259,8.387761,-3.232353,-7.775340,6.964678,9.148442,-1.801884,-7.747870,-5.781123,4.209349,8.552967,-0.802118],[5.398466,1.254054,-7.359364,-3.921603,5.964792,-1.533443,6.802987,-1.135591,6.746657,8.664959,-6.021213,0.920516,1.590645]],[[7.157309,1.937890,-7.224232,6.398003,5.026927,-9.868065,4.442049,4.428219,8.207206,-3.271787,-0.080965,4.841926,8.800628],[7.903708,-8.544052,8.755563,4.364763,-8.732574,7.444864,3.174668,3.125861,4.421837,-3.253805,-1.188091,0.253722,1.065412],[-4.300862,8.484974,-2.877148,-9.686953,8.921600,-8.032810,-9.985149,-9.846408,1.672196,-7.779872,8.799375,9.818595,-9.625441]],[[6.242786,1.589617,8.466973,2.927374,5.984656,6.999229,4.493087,-5.877735,-6.276161,-0.784543,-5.182242,-1.060935,-5.612943],[-6.546135,6.485746,9.819054,-4.180817,8.421636,-4.895781,-5.570207,4.007369,7.524223,3.641669,-3.199674,-8.749167,-9.048971],[-9.687463,7.009389,4.832227,5.127943,-4.197242,4.729968,7.465865,1.407567,-2.636181,1.475495,6.187270,-4.054728,-2.793744]],[[-5.245436,0.924888,-0.014370,-3.407738,-8.879272,1.289982,-9.829451,-9.551632,2.954555,3.750811,9.016594,-2.236429,6.025436],[6.648249,-0.773900,-2.885888,-0.070254,-4.992083,-4.179689,-7.342982,-9.212117,-3.070095,1.722811,-4.448300,-2.045419,4.270988],[8.123376,-5.589417,-8.713691,-7.219927,-3.801174,0.872116,-9.003522,0.211234,-9.784019,6.558625,6.055275,-6.390640,-6.108112]],[[5.737276,-5.782289,-1.898926,6.887941,-0.743472,-6.707940,-1.102492,2.691476,8.242407,2.326089,-6.691370,-5.748721,-7.184234],[3.140227,1.646198,-3.477878,-5.591069,3.573467,-9.640668,-8.370646,-6.596372,-9.320992,7.571875,1.174502,7.668697,7.148243],[-0.276163,-0.853752,8.422658,2.994289,5.342967,-5.696478,-3.895319,8.268556,-2.439329,2.691879,-0.819539,2.913734,-9.538143]],[[1.075612,-2.652707,2.724474,-4.225741,2.191870,-6.591484,-1.247308,-5.947820,0.654726,6.054480,-5.128945,-5.040600,-9.267356],[7.547986,-7.178409,-7.640843,3.299078,-9.695598,-6.204578,-2.480400,7.688328,-9.658320,0.011699,-4.486162,-1.841661,5.048643],[3.987730,-5.563250,-5.115793,9.374143,8.841740,-1.186255,-3.952027,-8.666585,-9.832279,0.331463,8.424509,4.078126,-6.682591]]], dtype = "float32")#candidate|5685|(15, 3, 13)|const|float32
bop_5686 = relay.power(uop_5669.astype('float32'), relay.reshape(const_5685.astype('float32'), relay.shape_of(uop_5669))) # shape=(15, 3, 13)
uop_5692 = relay.atan(var_5668.astype('float64')) # shape=(15, 3, 13)
func_4972_call = mod.get_global_var('func_4972')
func_4974_call = mutated_mod.get_global_var('func_4974')
call_5708 = relay.TupleGetItem(func_4972_call(), 0)
call_5709 = relay.TupleGetItem(func_4974_call(), 0)
output = relay.Tuple([bop_5682,bop_5686,uop_5692,call_5708,])
output2 = relay.Tuple([bop_5682,bop_5686,uop_5692,call_5709,])
func_5710 = relay.Function([var_5668,], output)
mod['func_5710'] = func_5710
mod = relay.transform.InferType()(mod)
var_5711 = relay.var("var_5711", dtype = "float32", shape = (15, 3, 13))#candidate|5711|(15, 3, 13)|var|float32
output = func_5710(var_5711)
func_5712 = relay.Function([var_5711], output)
mutated_mod['func_5712'] = func_5712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4473_call = mod.get_global_var('func_4473')
func_4474_call = mutated_mod.get_global_var('func_4474')
call_5743 = relay.TupleGetItem(func_4473_call(), 0)
call_5744 = relay.TupleGetItem(func_4474_call(), 0)
output = relay.Tuple([call_5743,])
output2 = relay.Tuple([call_5744,])
func_5757 = relay.Function([], output)
mod['func_5757'] = func_5757
mod = relay.transform.InferType()(mod)
mutated_mod['func_5757'] = func_5757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5757_call = mutated_mod.get_global_var('func_5757')
call_5758 = func_5757_call()
output = call_5758
func_5759 = relay.Function([], output)
mutated_mod['func_5759'] = func_5759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3623_call = mod.get_global_var('func_3623')
func_3624_call = mutated_mod.get_global_var('func_3624')
call_5858 = relay.TupleGetItem(func_3623_call(), 2)
call_5859 = relay.TupleGetItem(func_3624_call(), 2)
func_3125_call = mod.get_global_var('func_3125')
func_3126_call = mutated_mod.get_global_var('func_3126')
call_5872 = relay.TupleGetItem(func_3125_call(), 0)
call_5873 = relay.TupleGetItem(func_3126_call(), 0)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_5883 = func_1823_call()
call_5884 = func_1823_call()
output = relay.Tuple([call_5858,call_5872,call_5883,])
output2 = relay.Tuple([call_5859,call_5873,call_5884,])
func_5886 = relay.Function([], output)
mod['func_5886'] = func_5886
mod = relay.transform.InferType()(mod)
mutated_mod['func_5886'] = func_5886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5886_call = mutated_mod.get_global_var('func_5886')
call_5887 = func_5886_call()
output = call_5887
func_5888 = relay.Function([], output)
mutated_mod['func_5888'] = func_5888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_5902 = func_3670_call()
call_5903 = func_3670_call()
func_705_call = mod.get_global_var('func_705')
func_708_call = mutated_mod.get_global_var('func_708')
var_5921 = relay.var("var_5921", dtype = "int16", shape = (252, 1))#candidate|5921|(252, 1)|var|int16
call_5920 = relay.TupleGetItem(func_705_call(relay.reshape(var_5921.astype('int16'), [252,]), relay.reshape(call_5902.astype('float64'), [13, 10, 3]), ), 4)
call_5922 = relay.TupleGetItem(func_708_call(relay.reshape(var_5921.astype('int16'), [252,]), relay.reshape(call_5902.astype('float64'), [13, 10, 3]), ), 4)
func_796_call = mod.get_global_var('func_796')
func_800_call = mutated_mod.get_global_var('func_800')
const_5931 = relay.const([[-7.396045,-4.239621,0.030803,-5.416122,8.342376,-1.007264,-7.548661,-6.328898,1.602032,5.425390,-2.706453,-0.426848,9.297732,-8.459700,2.601950,-0.268545,-9.341018,-2.825820,8.079489,-6.660537,-3.398419,5.499271,-3.340593,5.444540,7.479413,-2.825891,3.339647,-0.565536,-5.297275,-0.938294,-5.435599,3.715684,8.332484,-4.379886,-6.123630,2.858959,8.163202,8.415421,-6.769409,-1.373931,-0.938096,0.802233,9.916756,-9.860476,2.937313,-0.296009,4.508129,-9.216553,3.161339,2.642934,4.968575,3.132869,6.841980,0.696894,6.594924,2.710018,-4.072959,7.826237,-5.815895,5.760757,-6.968778,8.593152,2.423142,8.190317,4.724868,-6.981368,6.058461,7.702673,-5.275957,4.813216,-1.623209,0.255525,3.112377,7.988505,5.042937,6.801113,-7.803013,9.435741,-4.761416,-8.123760,-4.012869,0.808417,-8.268948,-1.078636,3.882502,-9.046899,4.338734,-9.383041,-8.283791,-0.273213,-3.545804,-0.373890,3.452372,-6.401398,-8.764904,3.587324,7.091206,-9.816658,7.191662,-7.512511,-7.219032,8.744527,4.800397,2.824968,3.729038,8.355540,7.951856,-5.595467,9.224373,8.895963,2.230022,-4.577731,0.010357,8.653403,-9.545091,7.643981,-3.855692,-2.914554,-5.058762,-7.226347,8.057669,6.485079,0.375549,9.603395,-8.710061,-1.816102,4.977314,-1.635018,7.840254,-5.993047,9.105929,7.006257,-7.270064,9.617919,5.426876,-8.966410,9.190436,4.340400,5.605484,-5.130504,0.792305,6.550710,3.379234,2.419835,7.837012,-3.098871,6.380036,8.287527,6.110461,-4.337562,-0.483881,-3.805862,-3.652697,-8.186093,-5.584930,6.173669,0.864785,6.012014,-1.812945,0.014822,-3.309670,2.588020,0.525047,7.795073,7.019571,6.961594,-6.227747,-8.985803,-8.883120,-8.060493,9.106927,-8.205550,-0.276895,4.923163,6.647614,8.159517,3.807160,6.180091,0.209235,8.841124,5.951944,-5.445335,-3.719488,-4.565960,0.129090,-7.806594,8.308948,9.922368,-3.975802,-8.600616,6.743034,2.527599]], dtype = "float64")#candidate|5931|(1, 192)|const|float64
call_5930 = relay.TupleGetItem(func_796_call(relay.reshape(const_5931.astype('float64'), [3, 16, 4]), relay.reshape(const_5931.astype('float64'), [3, 16, 4]), ), 1)
call_5932 = relay.TupleGetItem(func_800_call(relay.reshape(const_5931.astype('float64'), [3, 16, 4]), relay.reshape(const_5931.astype('float64'), [3, 16, 4]), ), 1)
output = relay.Tuple([call_5902,call_5920,var_5921,call_5930,const_5931,])
output2 = relay.Tuple([call_5903,call_5922,var_5921,call_5932,const_5931,])
func_5934 = relay.Function([var_5921,], output)
mod['func_5934'] = func_5934
mod = relay.transform.InferType()(mod)
mutated_mod['func_5934'] = func_5934
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5935 = relay.var("var_5935", dtype = "int16", shape = (252, 1))#candidate|5935|(252, 1)|var|int16
func_5934_call = mutated_mod.get_global_var('func_5934')
call_5936 = func_5934_call(var_5935)
output = call_5936
func_5937 = relay.Function([var_5935], output)
mutated_mod['func_5937'] = func_5937
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6005 = relay.var("var_6005", dtype = "float64", shape = (15, 9, 15))#candidate|6005|(15, 9, 15)|var|float64
var_6006 = relay.var("var_6006", dtype = "float64", shape = (15, 9, 15))#candidate|6006|(15, 9, 15)|var|float64
bop_6007 = relay.floor_divide(var_6005.astype('float64'), relay.reshape(var_6006.astype('float64'), relay.shape_of(var_6005))) # shape=(15, 9, 15)
uop_6018 = relay.cos(var_6005.astype('float64')) # shape=(15, 9, 15)
bop_6028 = relay.subtract(uop_6018.astype('uint8'), relay.reshape(bop_6007.astype('uint8'), relay.shape_of(uop_6018))) # shape=(15, 9, 15)
uop_6034 = relay.acos(bop_6028.astype('float32')) # shape=(15, 9, 15)
func_1076_call = mod.get_global_var('func_1076')
func_1080_call = mutated_mod.get_global_var('func_1080')
var_6041 = relay.var("var_6041", dtype = "uint16", shape = ())#candidate|6041|()|var|uint16
const_6042 = relay.const([[4],[4],[-9],[3],[-10],[7],[-6],[-1],[-8],[-7],[1],[2],[2],[-3],[-7],[3],[-9],[9],[7],[-10],[-6],[6],[-10],[9],[1],[7],[-1],[-7],[8],[1],[5],[1],[2],[-3],[-9],[-4],[10],[7],[9],[7],[9],[2],[-5],[-2],[1],[10],[-9],[9],[10],[-10],[5],[-6],[-6],[-6],[-6],[-6],[1],[4],[9],[10],[-3],[-3],[5],[6],[7],[4],[2],[8],[2],[4],[9],[4],[10],[-7],[-8],[-6],[-1],[-3],[-4],[-2],[5],[-3],[-8],[6],[7],[10],[1],[-7],[6],[7],[-4],[4],[3],[-2],[6],[-8],[-9],[-9],[-1],[7],[-4],[3],[2],[6],[5],[1],[6],[7],[-3],[-6],[2],[-2],[-4],[10],[-4],[3],[-5],[-5],[8],[7],[5],[-5],[5],[2],[-2],[9],[-4],[-6],[9],[-4],[-6],[-5],[5],[10],[-1],[9],[6],[9],[-7],[-1],[3],[4],[10],[6],[8],[4],[-8],[5],[-9],[7],[5],[-8],[-3],[4]], dtype = "uint16")#candidate|6042|(154, 1)|const|uint16
call_6040 = relay.TupleGetItem(func_1076_call(relay.reshape(var_6041.astype('uint16'), []), relay.reshape(const_6042.astype('uint16'), [11, 1, 14]), ), 0)
call_6043 = relay.TupleGetItem(func_1080_call(relay.reshape(var_6041.astype('uint16'), []), relay.reshape(const_6042.astype('uint16'), [11, 1, 14]), ), 0)
func_527_call = mod.get_global_var('func_527')
func_529_call = mutated_mod.get_global_var('func_529')
call_6044 = relay.TupleGetItem(func_527_call(), 1)
call_6045 = relay.TupleGetItem(func_529_call(), 1)
uop_6046 = relay.exp(uop_6034.astype('float64')) # shape=(15, 9, 15)
output = relay.Tuple([call_6040,var_6041,const_6042,call_6044,uop_6046,])
output2 = relay.Tuple([call_6043,var_6041,const_6042,call_6045,uop_6046,])
func_6049 = relay.Function([var_6005,var_6006,var_6041,], output)
mod['func_6049'] = func_6049
mod = relay.transform.InferType()(mod)
mutated_mod['func_6049'] = func_6049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6049_call = mutated_mod.get_global_var('func_6049')
var_6051 = relay.var("var_6051", dtype = "float64", shape = (15, 9, 15))#candidate|6051|(15, 9, 15)|var|float64
var_6052 = relay.var("var_6052", dtype = "float64", shape = (15, 9, 15))#candidate|6052|(15, 9, 15)|var|float64
var_6053 = relay.var("var_6053", dtype = "uint16", shape = ())#candidate|6053|()|var|uint16
call_6050 = func_6049_call(var_6051,var_6052,var_6053,)
output = call_6050
func_6054 = relay.Function([var_6051,var_6052,var_6053,], output)
mutated_mod['func_6054'] = func_6054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1233_call = mutated_mod.get_global_var('func_1233')
call_6068 = relay.TupleGetItem(func_1232_call(), 0)
call_6069 = relay.TupleGetItem(func_1233_call(), 0)
func_4285_call = mod.get_global_var('func_4285')
func_4289_call = mutated_mod.get_global_var('func_4289')
var_6084 = relay.var("var_6084", dtype = "int64", shape = ())#candidate|6084|()|var|int64
var_6085 = relay.var("var_6085", dtype = "int64", shape = (100,))#candidate|6085|(100,)|var|int64
call_6083 = func_4285_call(relay.reshape(var_6084.astype('int64'), []), relay.reshape(var_6085.astype('int64'), [5, 5, 4]), )
call_6086 = func_4285_call(relay.reshape(var_6084.astype('int64'), []), relay.reshape(var_6085.astype('int64'), [5, 5, 4]), )
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_6111 = relay.TupleGetItem(func_1055_call(), 0)
call_6112 = relay.TupleGetItem(func_1056_call(), 0)
output = relay.Tuple([call_6068,call_6083,var_6084,var_6085,call_6111,])
output2 = relay.Tuple([call_6069,call_6086,var_6084,var_6085,call_6112,])
func_6113 = relay.Function([var_6084,var_6085,], output)
mod['func_6113'] = func_6113
mod = relay.transform.InferType()(mod)
mutated_mod['func_6113'] = func_6113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6113_call = mutated_mod.get_global_var('func_6113')
var_6115 = relay.var("var_6115", dtype = "int64", shape = ())#candidate|6115|()|var|int64
var_6116 = relay.var("var_6116", dtype = "int64", shape = (100,))#candidate|6116|(100,)|var|int64
call_6114 = func_6113_call(var_6115,var_6116,)
output = call_6114
func_6117 = relay.Function([var_6115,var_6116,], output)
mutated_mod['func_6117'] = func_6117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_6148 = relay.TupleGetItem(func_2781_call(), 1)
call_6149 = relay.TupleGetItem(func_2782_call(), 1)
output = relay.Tuple([call_6148,])
output2 = relay.Tuple([call_6149,])
func_6150 = relay.Function([], output)
mod['func_6150'] = func_6150
mod = relay.transform.InferType()(mod)
output = func_6150()
func_6151 = relay.Function([], output)
mutated_mod['func_6151'] = func_6151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1233_call = mutated_mod.get_global_var('func_1233')
call_6175 = relay.TupleGetItem(func_1232_call(), 1)
call_6176 = relay.TupleGetItem(func_1233_call(), 1)
func_4982_call = mod.get_global_var('func_4982')
func_4986_call = mutated_mod.get_global_var('func_4986')
const_6184 = relay.const([[-4.636795,0.268802,-5.355830,7.266437,-3.580222,-8.191098,-0.461797,-2.644847,0.867519,5.005755,-4.723465,-7.993653,9.353410,5.744104,-2.405469,9.355605,5.883518,1.303577,5.086862,4.942358,5.292591,-2.396338,6.229560,9.069523,1.221844,-5.478431,6.695952,-3.641253,-2.212343,-9.741836,-2.209219,9.210104,5.473565,2.602761,-0.741403,-2.035326,-2.020224,7.193517,-7.579130,-3.062947,-6.055015,3.340932,3.874780,-8.695382,5.786941,5.402980,2.486858,-0.712623,6.928830,7.332534,-2.536054,-0.611597,-3.047608,-2.964361,-6.471590,6.533552,7.680553,6.832156,-5.690627,8.050656,-3.554238,3.211412,2.162612,-3.167277,8.184551,-0.732646,-9.183003,-9.743568,4.494501,6.168213,8.541110,-9.408129,4.307678,-9.832415,3.528760,5.039318,-2.939723,5.022253,-6.798837,-0.191845,-3.879482,8.831956,2.705041,8.542075,8.809870,0.620290,6.258316,6.262413,1.346493,-0.020092,9.208647,-9.551891,-8.070227,-0.679014,-5.630766,-1.940647,7.002574,7.721113,6.942469,6.891238,9.607442,-9.885222,-1.340628,7.617601,5.595231,1.420293,2.313109,-3.161275,6.094571,3.202753,7.171677,-4.103476,4.551626,-7.522460,6.599391,7.736222,-1.083542,3.112826,-9.033920,-7.913278,3.654953,-9.740881,9.743674,-2.963330,2.555322,-2.991942,-3.969167,-3.262702,-3.726103,-5.700684,-7.601279,-9.690399,9.108604,-9.181872,-9.488332,6.659228,-7.364536,0.527216,-4.429442,-7.058937,7.348131,2.425801,-0.233065,5.167695,-8.930330,-0.698250,-9.269919,2.316698,-6.249320,7.916633,-8.561506,-2.233832,-6.624403,-8.286404,-8.067478,0.985370,-0.677863,3.991894,-9.973808,5.643584,-0.564094,0.881066,0.388862,7.786959,-5.044335,-5.527637,8.048604,1.329313,-8.408331,3.819183,6.514876,-2.166919,8.171446,-8.847598,6.619083,-0.455149,8.794845,-8.783245,-5.030271,-4.802698,-2.943574,9.473628,-0.369965,8.391371,-5.429795,4.479059,0.796507,5.162869,1.073068,-3.449744,-3.987569,-4.559348,4.755052,-8.185929,-5.455716,-1.618313,9.872803,7.781658,0.129489,9.664056,6.336887,1.908484,-0.635063,0.658310,-7.470014,-7.931568,-0.917444,-1.222449,7.476592,0.791602,0.769280,-9.886103,6.641113,-0.849987,5.034750,-5.104314,-1.318097,9.250362,8.216180,-9.468757,5.717620,-1.439704,-4.917592,3.442119,4.408716,6.736395,-2.743940,8.009389,4.828262,-4.642279,6.279441,3.294260,-2.943015,6.401097,9.576566,7.544401,-1.394251,-0.359769,-2.807103,2.854305,-9.321852,5.827896,-8.467669,-8.035725,-5.530478,-6.075042,-8.496197,-9.739457,9.880615,-0.213580,5.304544,6.786774,1.680667,-0.850950,7.419145,7.967652,8.477633,-5.876148,7.625568,6.602591,-3.294595,-3.712636,-5.432287,3.942861,-8.073485,-5.258236,-0.568342,6.802692,-6.965506,7.231042,2.619559,2.188928,9.171177,8.010805,6.568006,7.285242,-1.000759,-5.576525,-6.269975,-4.691480,2.740391,-7.701270,-4.179011,8.263535,-2.279249,-4.149678,4.513083,-0.588384,-8.381405,4.649637,-7.749469,0.985017,-9.356246,3.085657,8.943885,6.302836,0.087339,-7.952030,-2.696612,-8.814768,1.711327,-7.366391,-4.167001,2.612140,-0.790007,-5.823604,3.371363,-8.065535,3.608791,-8.244130,2.351818,9.619504,-9.601044,8.158310,6.578520,3.840580,-3.376795,2.965385,-0.802187,8.196690,-2.972376,4.695613,6.830035,6.931217,-2.884702,-4.928663,-5.656692,-8.732385,2.187906,1.048386,7.243698,1.595838,-6.563398,-6.006115,-7.823053,-3.921527,-8.338460,-9.453109,3.224638,-4.077316,-7.797037,5.233154,9.954739,6.692344,7.894715,4.035776,0.595732,3.809940,-3.759058,-5.044472,7.365949,4.647996,-5.061182,-5.342617,9.165080,9.965245,4.758565,-4.852802,-0.648997,9.951374,-9.070407,-3.929282,-3.409098,-1.887937,-2.839428,9.098049,3.789562,5.743925,-7.434526,1.235139,-6.709374,9.616744,6.187800,-1.935650,5.934549,-6.816256,9.964838,4.400327,-9.284849,-5.553589,-0.462569,-4.689034,-0.178766,-7.180645,2.862164,-0.144053,-0.816193,1.588890,-1.713053,-4.676479,-0.827620,9.042631,6.904454,0.064589,-8.116266,-0.414933,1.671834,-5.088215,-0.463792,-5.044499,-9.661755,-4.630479,9.067196,9.887019,4.069475,1.223851,-6.520589,4.866823,-7.134827,2.387891,-0.930879,1.688250,-9.253845,4.814812,-5.079453,6.573200,4.027154,-1.252655,9.641788,-1.926196,7.694068,-3.980590,-8.768414,0.967320,-6.039216,-1.023241,5.487626,-4.707301,7.450059,-4.023125,-4.038014,2.942505,4.745618,-5.807364,2.878912,-0.605001,-4.089715,-4.125229,-0.327798,8.143834,-4.706004,-2.341140,-4.845089,3.470789,-2.001625,1.609486,6.021146,-6.252878,-0.881797,-4.684808,4.963766,-5.073593,2.069609,6.747911,6.269088,7.735909,-7.711958,7.128872,-8.151333,-9.331514,-6.814842,4.333410,-1.964469,0.740003,-8.913560,-3.304331,-5.992814,-7.687165,1.737555,4.176543,-6.009850,-5.583696,-5.271460,4.436042,5.880468,-2.550600,-8.731354,5.297048,6.172535,8.665836,-0.923044,-7.469694,7.523543,6.999556,-1.944083,4.978095,6.751928,8.614857,6.804464,-5.504429,-6.340321,-2.578371,4.131271,-4.281841,-5.461264,-8.580865,1.461997,6.461197,9.347494,-9.552424,-0.834734,1.405679,7.359258,5.416614,3.491079,2.933688,-8.645913,-3.721377,-8.347976,1.740832,4.025968,1.425056,-8.643973,0.159427,6.639056,8.565609,8.218979,7.449640,2.405229,0.855200,4.314300,-1.606549,-6.040047,5.851335,6.762441,-0.151368,-4.307926,-0.177473,-2.370508,8.695455,6.625748,0.111515,1.488734,3.413583,-8.606196,5.599974,-4.516264,9.108781,4.521498,7.466777,2.764044,4.142342,5.133541,-6.152683,2.504582,-0.143452,-3.921288,0.546906,-8.625064,-9.925021,5.101275,-6.500528,-1.507005,-9.186283,-8.675440,-3.844435,0.060499,-8.855132,7.249866,9.779021,-2.233241,1.040859,6.469908,-9.459106,-3.009466,-8.124799,-9.048320,5.042528,9.726041,-2.977117,3.773346,1.690279,-3.017072,2.053194,5.450681,-7.045505,-9.031279,-9.567053,-3.370586,-2.541535,-9.815013,-9.494858,1.532830,7.198421,-9.471772,2.559552,-3.935952,-9.125585,-5.311711,3.787311,-0.719317,9.426773,4.582130,8.465690,-0.987225,-6.948970,-7.435126,7.660758,-2.121398,-6.592093,2.029115,-2.117765,3.744988,-2.636519,5.338998,9.390887,-8.472212,-2.682286,-2.120572,2.643445,0.305630,4.393170,6.748094,-4.663644,3.354460,-6.041886,-2.267791,3.783334,9.969461,5.389881,2.452642,3.397703,9.176378,5.604614,0.825103,-5.187558,7.317873,-9.209856,-8.855721,-6.421687,-1.962702,-1.372185,-3.137200,-6.042891,-9.234883,-1.834778,-8.414302,2.571892,5.266515,1.543235,7.965527,-0.945923,-2.436976,8.759230,9.323203,-0.838996,-5.072206,-6.703396,-6.912301,5.823668,-4.650645,-6.642437,6.472977,-0.149982,0.544204,2.723484,2.775182,4.608276,-2.253410,-2.887021,-4.099206,1.623378,-8.642785,6.104252,-1.823967,6.048825,-1.152062,2.754267,2.528699,1.265885,-6.282617,8.211812,-0.114964,6.872874,-2.671421,-0.787474,-8.623071,9.719156,2.581144,-7.266261,3.912201,-3.386442,4.255733,2.244091,5.333253,2.576554,9.043008,8.834906,1.990368,9.027833,-9.512935,3.416302,3.734956,4.582355,9.579622,4.104810,2.904038,0.062757,8.074318,5.973580,2.385815,-3.895846,-7.699732,-6.182440,-9.504809,9.104422,6.088513,-8.358631,7.764260,0.834096,5.570980,-8.593421,-1.928492,8.853409,-2.181213,-6.628605,-4.841017,1.267887,-4.494656,-3.850048,5.937917,8.650914,-4.500262,2.971847,-6.003696,2.973633,6.048666,-7.917778,2.919622,-6.406196,6.722854,8.774783,7.657980,-0.174074,-2.161840,3.538658,-9.551571,-6.941877,-8.376959,-3.293585,-3.504345,-3.629843,3.766045,4.549973,-7.033286,4.580720,-8.011770,8.271646,4.923394,5.038838,4.159765,0.792000,1.492391,-6.797937,2.625682,-2.893603,-7.846094,-1.206723,-7.737653,-3.876826,4.634495,-4.927976,-2.225861,9.711429,0.229084,9.940595,8.524387,-6.942255,-4.986841,-9.783278,7.657869,7.325497,9.107146,-7.396008,0.730856,5.117633,-8.111290,-3.609849,4.519040,-6.965618,-4.257407,5.338628,-8.066840,9.899994,3.628399,-3.160509,-0.486240,-5.702012,9.494096,6.262202,-8.836524,3.747282,-0.712689,9.555386,-9.137395,-7.360947,-0.216793,-5.873301,7.766859,3.891857,-5.932374,-1.920961,-6.546083,-9.516065,4.366990,-0.976963,-6.960023,-6.091017,-1.693478,5.143769,5.961753,8.094670,3.605423,-7.301773,4.928500,5.615476,3.523061,1.441822,6.803252,-4.442070,5.384932,-0.139469,-4.193292,6.022422,-2.614372,8.595829,-6.304169,3.390336,8.429186,2.867362,-3.112978,-2.557619,-3.338461,7.127572,8.621095,-0.703666,-5.854296,2.817509,2.824697,5.649241,1.249698,5.012684,-6.701184,5.893537,-1.782597,-9.914462,-6.777458,-4.702205,-7.669415,-2.447182,6.191246,6.732010,0.067990,8.465815,7.310535,-1.718375,1.870140,-4.329357,8.129661,0.217310,-4.677800,-2.073474,-7.301658,7.067000,-1.368003,3.783216,-5.232433,6.277720,1.024650,-4.556574,-5.908340,2.659329,-9.830656,2.297863,5.944108,1.083512,-5.556576,-1.968517,1.892182,-6.744070,0.136509,1.071667,-4.992156,4.261837,5.442606,-1.324849,2.885197,-1.600994,9.549205,4.162027,-0.416056,4.035839,-5.745168,-3.395855,0.651989,4.027965,-8.489196,1.697165,3.908782,-9.159782,-4.382769,-2.222566,-2.112795,-8.824536,-2.456661,-4.067163,-7.577322,-9.157198,-4.009317,-6.225984,1.729918,-2.737743,1.028003,-6.928231,6.794729,0.519837,4.606018,2.724970,-8.697769,1.977681,2.168384,-2.426867,2.415885,-0.047162,4.725817,-8.732103,-5.787821,-6.995315,-7.642168,-6.800673,5.862048,7.236299,-5.316078,-6.643390,-8.438794,5.724511,8.771604,-9.874073,-8.031693,-5.030363,9.092422,-5.154353,-0.371089,7.188057,2.801277,-2.540116,-9.397955,4.406242,-4.898169,9.178272,-5.834530,-7.658847,-9.510713,-8.012231,8.842904,-1.434740,1.287874,-1.573323,7.069630,-1.602363,8.303835,2.106387,7.308413,-9.242249,-5.554429,-9.706536,1.492236,1.567933,8.823707,-2.185470,-5.764700,-2.782652,-8.603279,1.913813,-0.795381,-0.867429,-9.498184,4.704198,8.071304,9.109269,-3.807828,-4.781921,-5.131258,3.489716,2.824693,-7.070814,7.877944,-0.741739,1.647100,5.960816,9.270908,-8.682459,-0.621114,7.190325,7.204632,5.767494,8.130034,3.486940,9.428623,5.650128,8.721091,1.096581,-7.708056,-0.225909,9.195981,-8.767010,7.987247,6.459012,-5.442868,6.988274,5.371958,4.839417,-7.045391,1.982766,-5.401838,1.879625,-0.358327,-0.043608,-6.723869,1.436169,-4.407182,-9.502767,-9.571291,6.937090,7.122786,-1.430307,-5.065042,6.395958,2.761784,-3.584662,7.521751,4.512670,-1.457584,8.359856,-5.938537,2.525597,-3.647470,-5.818079,6.241575,2.228079,5.361146,5.488605,-7.979847,-7.199628,5.967070,3.451528,-5.350410,5.464183,-1.427882,9.787373,1.247950,5.433751,6.233837,-0.110610,-1.221177,8.853491,5.667379,1.219170,3.753786,8.176300,-7.493458,7.213203,1.028483,-5.354841,8.772604,-3.376813,-7.579922,-9.866837,-8.256569,-2.766843,4.061950,-1.085885,-8.900928,-8.704938,5.799654,3.577138,-6.058951,3.730032,1.338898,1.689487,7.567000,9.200165,7.342733,2.493792,-7.359542,-0.063152,6.177777,-8.853133,-1.428854,2.316924,8.810406,-2.617156,-3.663811,9.987023,2.618431,-1.112866,1.359888,-3.420401,-2.530013,-1.614548,5.238553,-7.423818,4.018755,-6.792431,5.063539,7.639243,-0.969213,-0.897708,2.611917,-3.065444,-9.417021,-2.003713,-6.184783,-2.341374,-7.203669,5.447219,-8.823984,0.377094,5.284185,5.999710,5.617750,9.818881,-0.636670,-1.536327,2.811682,-0.372604,-2.814026,1.443533,4.018530,8.264131,-5.668557,7.852459,-0.548539,-1.123766,1.258636,-6.712653,2.032507,-0.402271,0.418362,9.093643,-1.234888,-3.671899,-3.203850,1.335905,3.020737,-1.210812,-7.153880,-3.044256,-7.056188,-8.637630,9.659620,-9.024270,-0.468590,-3.141940,-9.852507,-0.501326,-4.205002,6.083540,8.670448,-5.701317,7.954437,-2.892015,1.101887,-6.290063,-5.014966,0.128349,6.125260,-0.062383,-5.594921,0.277262,-8.199079,5.201209,-3.446682,-5.729574,-1.157283,-7.281949,7.309426,4.120192,-1.942052,-5.907473,-7.773218,-1.829260,7.755100,0.500127,1.675264,-6.653867,-1.121667,-5.823828,-6.962464,-6.421900,-1.264973,-9.504503,-4.422823,-0.953994,0.978613,3.462885,-4.740110,1.486008,-2.637345,6.453956,3.859456,7.106903,-7.176653,-5.291804,-7.631796,5.724278,-4.778762,-3.183637,4.983139,7.074102,0.352851,-2.131744,-1.245206,-0.841939,-9.062229,-0.908562,9.653935,1.888483,-0.089102,0.025212,9.757232,0.027462,-8.650633,-4.717781,-8.728791,2.263274,-4.505604,9.404713,1.491131,0.079790,6.014494,-6.846159,3.950677,-2.294698,4.234364,2.192855,-7.140193,-4.852410,-8.914325,-7.839753,-5.623128,3.638976,9.917962,5.258426,-7.970608,-0.053794,9.461577,-2.420821,5.383955,-2.259729,-8.214148,9.089766,-2.223457,-3.963660,-0.908417,3.808846,-9.558915,8.307976,1.542555,-3.716720,6.968158,5.473802,7.761175,5.682631,1.625747,-9.553569,6.150705,-7.423788,7.409963,7.289752,-0.543481,2.555118,2.758746,-2.748373,7.572677,-5.894405,-8.377896,0.774413,7.428406,-4.605141,-1.843379,4.963017,-5.967635,4.371600,-1.122850,2.396730,4.895618,7.417045,8.867555,9.543509,-6.314183,9.919333,-7.363364,5.031908,0.873881,-6.784054,-5.602966,-7.977808,1.762677,-1.391501,-2.906360,-8.574015,-2.679619,-8.284555,-1.676151,4.826869,6.154017,7.558047,3.590362,5.497556,-8.572392,8.153247,8.760167,2.684759,3.640218,-0.361931,9.120314,-1.102752,-2.615917,0.158921,-6.472428,-7.417600,8.884677,2.729132,-7.353384,2.816308,-6.180032,3.035266,-0.368629,3.398976,-8.203658,1.368316,-3.607705,-2.452929,-4.630151,5.321558,-4.913276,-0.892741,3.867512,-2.789387,0.168858,-7.869766,-8.947433,0.662263,-8.876063,3.150528,9.008705,-2.237789,-1.897865,-1.040090,-6.684044,8.234621,3.051706,-4.519056,-6.956969,-0.436015,5.273993,0.959563,-5.944438,-5.897256,4.030323,-6.461550,0.850077,3.068482,4.214425,-6.024895,8.248630,-7.092425,-6.102674,-2.298867,8.814689,-9.127612,7.475322,9.303224,-1.781004,3.377057,6.870901,-4.334451,-3.701514,-5.720541,-0.005633,-4.150638,-4.247508,-9.751120,8.582038,7.499030,-6.598763,5.348914,-7.551825,8.504226,6.343001,-7.956995,-1.249170,4.561456,-1.310728,-5.964408,-0.567881,1.372242,4.494174,2.163684,-4.854231,-3.138549,-1.317657,-5.083155,-7.248567,-5.184963,-1.080861,-3.741781,1.685536,-0.268509,4.536899,-1.461341,3.186079,-0.512453,-6.669695,8.477869,6.938467,9.231875,-4.683676,-2.294315,8.107780,-4.445200,4.831817,3.995457,-6.025297,2.358057,-0.998171,7.478975,3.321147,2.064293]], dtype = "float64")#candidate|6184|(1, 1430)|const|float64
call_6183 = func_4982_call(relay.reshape(const_6184.astype('float64'), [11, 10, 13]), relay.reshape(const_6184.astype('float64'), [11, 10, 13]), )
call_6185 = func_4982_call(relay.reshape(const_6184.astype('float64'), [11, 10, 13]), relay.reshape(const_6184.astype('float64'), [11, 10, 13]), )
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_6187 = relay.TupleGetItem(func_2781_call(), 1)
call_6188 = relay.TupleGetItem(func_2782_call(), 1)
var_6200 = relay.var("var_6200", dtype = "float64", shape = (8, 1430))#candidate|6200|(8, 1430)|var|float64
bop_6201 = relay.greater(const_6184.astype('bool'), var_6200.astype('bool')) # shape=(8, 1430)
output = relay.Tuple([call_6175,call_6183,call_6187,bop_6201,])
output2 = relay.Tuple([call_6176,call_6185,call_6188,bop_6201,])
func_6210 = relay.Function([var_6200,], output)
mod['func_6210'] = func_6210
mod = relay.transform.InferType()(mod)
mutated_mod['func_6210'] = func_6210
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6211 = relay.var("var_6211", dtype = "float64", shape = (8, 1430))#candidate|6211|(8, 1430)|var|float64
func_6210_call = mutated_mod.get_global_var('func_6210')
call_6212 = func_6210_call(var_6211)
output = call_6212
func_6213 = relay.Function([var_6211], output)
mutated_mod['func_6213'] = func_6213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1949_call = mod.get_global_var('func_1949')
func_1950_call = mutated_mod.get_global_var('func_1950')
call_6230 = relay.TupleGetItem(func_1949_call(), 1)
call_6231 = relay.TupleGetItem(func_1950_call(), 1)
func_2848_call = mod.get_global_var('func_2848')
func_2849_call = mutated_mod.get_global_var('func_2849')
call_6248 = func_2848_call()
call_6249 = func_2848_call()
func_5339_call = mod.get_global_var('func_5339')
func_5342_call = mutated_mod.get_global_var('func_5342')
const_6279 = relay.const(-3.281263, dtype = "float64")#candidate|6279|()|const|float64
call_6278 = relay.TupleGetItem(func_5339_call(relay.reshape(const_6279.astype('float64'), [])), 0)
call_6280 = relay.TupleGetItem(func_5342_call(relay.reshape(const_6279.astype('float64'), [])), 0)
func_3654_call = mod.get_global_var('func_3654')
func_3655_call = mutated_mod.get_global_var('func_3655')
call_6290 = relay.TupleGetItem(func_3654_call(), 0)
call_6291 = relay.TupleGetItem(func_3655_call(), 0)
output = relay.Tuple([call_6230,call_6248,call_6278,const_6279,call_6290,])
output2 = relay.Tuple([call_6231,call_6249,call_6280,const_6279,call_6291,])
func_6296 = relay.Function([], output)
mod['func_6296'] = func_6296
mod = relay.transform.InferType()(mod)
output = func_6296()
func_6297 = relay.Function([], output)
mutated_mod['func_6297'] = func_6297
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6325 = relay.var("var_6325", dtype = "uint16", shape = (1, 4, 14))#candidate|6325|(1, 4, 14)|var|uint16
var_6326 = relay.var("var_6326", dtype = "uint16", shape = (1, 4, 14))#candidate|6326|(1, 4, 14)|var|uint16
bop_6327 = relay.minimum(var_6325.astype('uint16'), relay.reshape(var_6326.astype('uint16'), relay.shape_of(var_6325))) # shape=(1, 4, 14)
func_6296_call = mod.get_global_var('func_6296')
func_6297_call = mutated_mod.get_global_var('func_6297')
call_6330 = relay.TupleGetItem(func_6296_call(), 2)
call_6331 = relay.TupleGetItem(func_6297_call(), 2)
func_6296_call = mod.get_global_var('func_6296')
func_6297_call = mutated_mod.get_global_var('func_6297')
call_6336 = relay.TupleGetItem(func_6296_call(), 1)
call_6337 = relay.TupleGetItem(func_6297_call(), 1)
uop_6339 = relay.log2(var_6326.astype('float64')) # shape=(1, 4, 14)
output = relay.Tuple([bop_6327,call_6330,call_6336,uop_6339,])
output2 = relay.Tuple([bop_6327,call_6331,call_6337,uop_6339,])
func_6342 = relay.Function([var_6325,var_6326,], output)
mod['func_6342'] = func_6342
mod = relay.transform.InferType()(mod)
mutated_mod['func_6342'] = func_6342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6342_call = mutated_mod.get_global_var('func_6342')
var_6344 = relay.var("var_6344", dtype = "uint16", shape = (1, 4, 14))#candidate|6344|(1, 4, 14)|var|uint16
var_6345 = relay.var("var_6345", dtype = "uint16", shape = (1, 4, 14))#candidate|6345|(1, 4, 14)|var|uint16
call_6343 = func_6342_call(var_6344,var_6345,)
output = call_6343
func_6346 = relay.Function([var_6344,var_6345,], output)
mutated_mod['func_6346'] = func_6346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3783_call = mod.get_global_var('func_3783')
func_3784_call = mutated_mod.get_global_var('func_3784')
call_6351 = relay.TupleGetItem(func_3783_call(), 0)
call_6352 = relay.TupleGetItem(func_3784_call(), 0)
func_3082_call = mod.get_global_var('func_3082')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_6374 = func_3082_call()
call_6375 = func_3082_call()
output = relay.Tuple([call_6351,call_6374,])
output2 = relay.Tuple([call_6352,call_6375,])
func_6376 = relay.Function([], output)
mod['func_6376'] = func_6376
mod = relay.transform.InferType()(mod)
mutated_mod['func_6376'] = func_6376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6376_call = mutated_mod.get_global_var('func_6376')
call_6377 = func_6376_call()
output = call_6377
func_6378 = relay.Function([], output)
mutated_mod['func_6378'] = func_6378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_527_call = mod.get_global_var('func_527')
func_529_call = mutated_mod.get_global_var('func_529')
call_6462 = relay.TupleGetItem(func_527_call(), 1)
call_6463 = relay.TupleGetItem(func_529_call(), 1)
output = relay.Tuple([call_6462,])
output2 = relay.Tuple([call_6463,])
func_6464 = relay.Function([], output)
mod['func_6464'] = func_6464
mod = relay.transform.InferType()(mod)
mutated_mod['func_6464'] = func_6464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6464_call = mutated_mod.get_global_var('func_6464')
call_6465 = func_6464_call()
output = call_6465
func_6466 = relay.Function([], output)
mutated_mod['func_6466'] = func_6466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4123_call = mod.get_global_var('func_4123')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_6502 = func_4123_call()
call_6503 = func_4123_call()
func_1983_call = mod.get_global_var('func_1983')
func_1986_call = mutated_mod.get_global_var('func_1986')
var_6506 = relay.var("var_6506", dtype = "float64", shape = ())#candidate|6506|()|var|float64
const_6507 = relay.const([8.782155,-5.886564,-1.687065,-5.079262,1.050206,2.545198,4.795386,0.863037,1.748327,9.795002,-4.124308,0.739669,-1.808645,-3.278869,3.744152,6.674682,-5.792531,-0.592913,-1.519833,-1.127771,-0.871746,7.165636,0.291010,1.485127,-3.361211,-2.264031,-8.058249,5.100186,1.376289,-7.937716,5.989705,6.711510,5.730395,-2.995865,-0.153072,4.260469,-1.956042,-0.107750,8.407783,-4.672621,-3.827157,-1.081051,5.017780,0.579113,-8.596859,5.057153,8.546775,3.776380,-4.493992,2.107837,2.597327,-7.339505,6.543268,7.665457,-2.665044,-6.428230,-0.166014,9.082214,-3.244789,-6.537420,-2.977698,-2.263734,-6.143898,6.733143,7.861340,6.789443,8.884625,-7.906242,-9.515680,-0.555196,-0.488645,6.157500,8.533037,-0.371264,7.094825,-9.978331,-8.324781,-3.482192,2.576249,3.103285,-5.285023,1.199085,-6.834122,-7.677264,5.279674,4.676266,1.579598,1.579164,0.045702,7.217214,-0.036400,6.535872,-0.470711,-0.801037,1.561626,0.515364,-3.618826,0.506881,-3.354544,-8.495209,-4.495700,2.713009,-6.200348,1.748556,-8.367610,0.934284,-7.173327,9.585287,-6.333223,-0.006404,-0.795273,3.599763,-2.029173,4.523835,-1.599993,0.707882,-2.471298,-3.008096,9.605903,-2.190706,-4.207489,-9.675620,-3.247593,-5.357214,3.123893,-2.558089,-1.411777,4.172026,5.158073,4.606539,-2.487145,-6.594659,-3.919685,5.676912,-7.270677,9.433350,3.257431,-8.413414,-6.900311,-0.142796,9.134003,5.116763,-3.307736,9.319467,3.896503,6.800760,8.263664,-7.732355,2.222467,5.753923,-2.577947,-7.961995,-9.836215,2.345283,0.464907,4.275350,9.197858,-7.413136,7.638658,9.684699,6.261299,-6.208813,-9.156659,-5.402057,-5.117222,-4.030340,-2.360731,9.202944,9.365144,0.968501,-4.856617,1.385358,2.815281,-1.782548,8.999279,-7.973361,-6.874458,5.249594,2.459884,-2.715062,1.061574,-9.550148,-0.284371,7.703376,2.718962,-0.267843,1.593845,9.062968,-3.049263,0.443964,9.253501,-2.530705,-0.299671,-4.817843,6.355080,0.689740,5.904843,-6.778807,0.495673,4.101684,3.795137,8.547744,-3.764957,0.548120,-0.461664,-1.077879,-4.571592,2.683600,5.191270,5.518174,4.679082,5.074348,-2.245386,-6.205414,4.467614,-7.574316,4.037618,7.974212,-1.012686,-7.667678,5.376679,-5.549450,6.904556,-0.380233,-0.329528,1.078594,0.450490,-6.655759,9.283816,7.525821,7.066218,7.631717,0.125675,-8.430935,8.283914,-9.026004,1.196350,3.101637,0.414201,0.531455,0.657808,9.765566,-8.876542,-2.188656,-8.863257,-1.617495,-3.254076,-2.543859,4.927639,7.390894,-6.634492,0.474533,7.363430,-5.638850,7.679267,-9.420947,1.505990,3.042047,2.375056,6.495608,2.434172,5.113667,3.656830,-9.642268,-4.056167,2.352083,4.133027,6.481572,4.855313,9.620636,9.404990,4.739275,3.598529,-0.976727,4.731275,-3.940954,-0.245105,-1.927984,-4.420590,-2.816120,-6.894907,2.111402,-3.412488,-4.677203,-2.616029,-4.216404,4.584166,-1.364695,-2.239836,-1.549945,-9.368993,1.184860,-6.152587,-6.245153,-3.601753,-5.720749,4.173541,-2.113584,-4.461772,2.158771,6.422780,-6.307811,-4.961662,5.047456,-3.520787,-4.075444,1.867567,2.761633,9.250565,-0.903878,-3.749886,-6.674748,-3.598902,6.318795,-8.930682,7.763061,3.678312,-4.321384,3.089879,-9.520784,3.164468,-5.675044,-4.443675,2.153830,-5.499991,1.353788,-2.146270,-7.567837,3.062545,6.687667,-6.699840,6.168478,-9.541336,8.056239,9.448224,1.645158,-3.591568,7.019362,0.409553,-8.886198,-8.359479,-7.381829,-9.329899,3.845696,1.744656,9.799700,-1.117218,7.292261,-4.528900,-0.181712,-7.634716,7.107449,2.524521,-9.285881,7.566530,-0.002861,-7.072751,-0.583880,8.009772,-8.410023,-7.913491,7.537871,-9.969070,1.108753,6.861025,8.151787,-2.453607,1.652021,5.720776,-3.791876,-8.884429,7.965948,-3.679528,1.248228,3.273390,-9.116163,5.089946,-2.487198,-1.233903,9.762199,8.676473,7.133074,8.777014,-4.004291,-5.798706,1.303261,1.794364,-5.091088,-9.724683,-6.994233,2.015581,7.188786,-8.554484,1.444236,3.548248,-0.468976,8.540534,-0.180854,-0.278100,2.053332], dtype = "float64")#candidate|6507|(400,)|const|float64
call_6505 = relay.TupleGetItem(func_1983_call(relay.reshape(var_6506.astype('float64'), []), relay.reshape(const_6507.astype('float64'), [5, 8, 10]), ), 0)
call_6508 = relay.TupleGetItem(func_1986_call(relay.reshape(var_6506.astype('float64'), []), relay.reshape(const_6507.astype('float64'), [5, 8, 10]), ), 0)
output = relay.Tuple([call_6502,call_6505,var_6506,const_6507,])
output2 = relay.Tuple([call_6503,call_6508,var_6506,const_6507,])
func_6514 = relay.Function([var_6506,], output)
mod['func_6514'] = func_6514
mod = relay.transform.InferType()(mod)
var_6515 = relay.var("var_6515", dtype = "float64", shape = ())#candidate|6515|()|var|float64
output = func_6514(var_6515)
func_6516 = relay.Function([var_6515], output)
mutated_mod['func_6516'] = func_6516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_6532 = relay.TupleGetItem(func_1128_call(), 1)
call_6533 = relay.TupleGetItem(func_1129_call(), 1)
func_3826_call = mod.get_global_var('func_3826')
func_3827_call = mutated_mod.get_global_var('func_3827')
call_6540 = func_3826_call()
call_6541 = func_3826_call()
output = relay.Tuple([call_6532,call_6540,])
output2 = relay.Tuple([call_6533,call_6541,])
func_6542 = relay.Function([], output)
mod['func_6542'] = func_6542
mod = relay.transform.InferType()(mod)
output = func_6542()
func_6543 = relay.Function([], output)
mutated_mod['func_6543'] = func_6543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_6574 = func_1468_call()
call_6575 = func_1468_call()
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_6582 = relay.TupleGetItem(func_3457_call(), 0)
call_6583 = relay.TupleGetItem(func_3459_call(), 0)
func_2237_call = mod.get_global_var('func_2237')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_6585 = func_2237_call()
call_6586 = func_2237_call()
output = relay.Tuple([call_6574,call_6582,call_6585,])
output2 = relay.Tuple([call_6575,call_6583,call_6586,])
func_6596 = relay.Function([], output)
mod['func_6596'] = func_6596
mod = relay.transform.InferType()(mod)
mutated_mod['func_6596'] = func_6596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6596_call = mutated_mod.get_global_var('func_6596')
call_6597 = func_6596_call()
output = call_6597
func_6598 = relay.Function([], output)
mutated_mod['func_6598'] = func_6598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3204_call = mod.get_global_var('func_3204')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_6644 = func_3204_call()
call_6645 = func_3204_call()
func_5586_call = mod.get_global_var('func_5586')
func_5587_call = mutated_mod.get_global_var('func_5587')
call_6647 = relay.TupleGetItem(func_5586_call(), 0)
call_6648 = relay.TupleGetItem(func_5587_call(), 0)
func_2848_call = mod.get_global_var('func_2848')
func_2849_call = mutated_mod.get_global_var('func_2849')
call_6649 = func_2848_call()
call_6650 = func_2848_call()
func_5507_call = mod.get_global_var('func_5507')
func_5509_call = mutated_mod.get_global_var('func_5509')
call_6665 = relay.TupleGetItem(func_5507_call(), 0)
call_6666 = relay.TupleGetItem(func_5509_call(), 0)
output = relay.Tuple([call_6644,call_6647,call_6649,call_6665,])
output2 = relay.Tuple([call_6645,call_6648,call_6650,call_6666,])
func_6668 = relay.Function([], output)
mod['func_6668'] = func_6668
mod = relay.transform.InferType()(mod)
mutated_mod['func_6668'] = func_6668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6668_call = mutated_mod.get_global_var('func_6668')
call_6669 = func_6668_call()
output = call_6669
func_6670 = relay.Function([], output)
mutated_mod['func_6670'] = func_6670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1764_call = mod.get_global_var('func_1764')
func_1766_call = mutated_mod.get_global_var('func_1766')
call_6687 = func_1764_call()
call_6688 = func_1764_call()
output = relay.Tuple([call_6687,])
output2 = relay.Tuple([call_6688,])
func_6705 = relay.Function([], output)
mod['func_6705'] = func_6705
mod = relay.transform.InferType()(mod)
output = func_6705()
func_6706 = relay.Function([], output)
mutated_mod['func_6706'] = func_6706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_6709 = relay.TupleGetItem(func_1128_call(), 0)
call_6710 = relay.TupleGetItem(func_1129_call(), 0)
output = call_6709
output2 = call_6710
func_6742 = relay.Function([], output)
mod['func_6742'] = func_6742
mod = relay.transform.InferType()(mod)
output = func_6742()
func_6743 = relay.Function([], output)
mutated_mod['func_6743'] = func_6743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6596_call = mod.get_global_var('func_6596')
func_6598_call = mutated_mod.get_global_var('func_6598')
call_6788 = relay.TupleGetItem(func_6596_call(), 2)
call_6789 = relay.TupleGetItem(func_6598_call(), 2)
output = relay.Tuple([call_6788,])
output2 = relay.Tuple([call_6789,])
func_6810 = relay.Function([], output)
mod['func_6810'] = func_6810
mod = relay.transform.InferType()(mod)
mutated_mod['func_6810'] = func_6810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6810_call = mutated_mod.get_global_var('func_6810')
call_6811 = func_6810_call()
output = call_6811
func_6812 = relay.Function([], output)
mutated_mod['func_6812'] = func_6812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3433_call = mod.get_global_var('func_3433')
func_3435_call = mutated_mod.get_global_var('func_3435')
call_6876 = relay.TupleGetItem(func_3433_call(), 0)
call_6877 = relay.TupleGetItem(func_3435_call(), 0)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_6897 = relay.TupleGetItem(func_2781_call(), 0)
call_6898 = relay.TupleGetItem(func_2782_call(), 0)
output = relay.Tuple([call_6876,call_6897,])
output2 = relay.Tuple([call_6877,call_6898,])
func_6921 = relay.Function([], output)
mod['func_6921'] = func_6921
mod = relay.transform.InferType()(mod)
mutated_mod['func_6921'] = func_6921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6921_call = mutated_mod.get_global_var('func_6921')
call_6922 = func_6921_call()
output = call_6922
func_6923 = relay.Function([], output)
mutated_mod['func_6923'] = func_6923
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6924 = relay.var("var_6924", dtype = "bool", shape = ())#candidate|6924|()|var|bool
var_6925 = relay.var("var_6925", dtype = "bool", shape = (4, 8, 9))#candidate|6925|(4, 8, 9)|var|bool
bop_6926 = relay.logical_and(var_6924.astype('bool'), var_6925.astype('bool')) # shape=(4, 8, 9)
output = bop_6926
output2 = bop_6926
func_6929 = relay.Function([var_6924,var_6925,], output)
mod['func_6929'] = func_6929
mod = relay.transform.InferType()(mod)
mutated_mod['func_6929'] = func_6929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6929_call = mutated_mod.get_global_var('func_6929')
var_6931 = relay.var("var_6931", dtype = "bool", shape = ())#candidate|6931|()|var|bool
var_6932 = relay.var("var_6932", dtype = "bool", shape = (4, 8, 9))#candidate|6932|(4, 8, 9)|var|bool
call_6930 = func_6929_call(var_6931,var_6932,)
output = call_6930
func_6933 = relay.Function([var_6931,var_6932,], output)
mutated_mod['func_6933'] = func_6933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_7042 = relay.TupleGetItem(func_3457_call(), 0)
call_7043 = relay.TupleGetItem(func_3459_call(), 0)
output = relay.Tuple([call_7042,])
output2 = relay.Tuple([call_7043,])
func_7080 = relay.Function([], output)
mod['func_7080'] = func_7080
mod = relay.transform.InferType()(mod)
output = func_7080()
func_7081 = relay.Function([], output)
mutated_mod['func_7081'] = func_7081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5586_call = mod.get_global_var('func_5586')
func_5587_call = mutated_mod.get_global_var('func_5587')
call_7105 = relay.TupleGetItem(func_5586_call(), 0)
call_7106 = relay.TupleGetItem(func_5587_call(), 0)
func_705_call = mod.get_global_var('func_705')
func_708_call = mutated_mod.get_global_var('func_708')
var_7117 = relay.var("var_7117", dtype = "int16", shape = (1, 252))#candidate|7117|(1, 252)|var|int16
call_7116 = relay.TupleGetItem(func_705_call(relay.reshape(var_7117.astype('int16'), [252,]), relay.reshape(call_7105.astype('float64'), [13, 10, 3]), ), 3)
call_7118 = relay.TupleGetItem(func_708_call(relay.reshape(var_7117.astype('int16'), [252,]), relay.reshape(call_7105.astype('float64'), [13, 10, 3]), ), 3)
output = relay.Tuple([call_7105,call_7116,var_7117,])
output2 = relay.Tuple([call_7106,call_7118,var_7117,])
func_7127 = relay.Function([var_7117,], output)
mod['func_7127'] = func_7127
mod = relay.transform.InferType()(mod)
mutated_mod['func_7127'] = func_7127
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7128 = relay.var("var_7128", dtype = "int16", shape = (1, 252))#candidate|7128|(1, 252)|var|int16
func_7127_call = mutated_mod.get_global_var('func_7127')
call_7129 = func_7127_call(var_7128)
output = call_7129
func_7130 = relay.Function([var_7128], output)
mutated_mod['func_7130'] = func_7130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1804_call = mod.get_global_var('func_1804')
func_1806_call = mutated_mod.get_global_var('func_1806')
call_7132 = func_1804_call()
call_7133 = func_1804_call()
output = relay.Tuple([call_7132,])
output2 = relay.Tuple([call_7133,])
func_7134 = relay.Function([], output)
mod['func_7134'] = func_7134
mod = relay.transform.InferType()(mod)
mutated_mod['func_7134'] = func_7134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7134_call = mutated_mod.get_global_var('func_7134')
call_7135 = func_7134_call()
output = call_7135
func_7136 = relay.Function([], output)
mutated_mod['func_7136'] = func_7136
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7185 = relay.var("var_7185", dtype = "int64", shape = (12, 15, 3))#candidate|7185|(12, 15, 3)|var|int64
const_7186 = relay.const([[[-1,-9,4],[2,2,-2],[-5,6,-5],[10,-1,7],[7,8,7],[7,6,8],[10,7,-9],[3,-5,8],[5,5,-2],[-3,-6,-2],[8,10,7],[-1,5,1],[7,7,-2],[-2,-2,-2],[-7,-3,7]],[[-5,-7,8],[-10,-1,8],[-8,5,-7],[-10,-3,-5],[-7,7,7],[-7,8,5],[6,-6,10],[-8,-9,6],[1,6,-10],[-6,-5,-9],[8,3,8],[3,-3,2],[2,-4,4],[-10,7,6],[7,6,-6]],[[6,-9,-1],[9,4,4],[7,-7,-9],[-2,5,-5],[9,-6,5],[10,-7,10],[-7,-3,-1],[8,-2,-1],[-7,10,-4],[-4,6,-8],[1,2,-6],[-7,1,5],[-6,2,-7],[9,-7,5],[-3,-4,10]],[[-9,7,-10],[-6,-7,6],[1,-4,-1],[7,6,-10],[-5,1,-3],[-9,-5,-6],[1,-3,-8],[-10,-2,3],[7,3,4],[-4,8,8],[8,4,6],[-10,1,-5],[2,-10,-10],[-6,-5,-10],[-4,-9,2]],[[2,5,-5],[5,7,-7],[-4,8,3],[-9,4,-10],[6,-1,-6],[4,-6,3],[9,-7,1],[7,-4,3],[2,8,7],[-4,-2,10],[9,6,-3],[7,5,8],[-9,-5,-1],[-2,-10,3],[-8,2,2]],[[-10,8,-6],[-2,-4,-6],[-5,9,-10],[6,-5,4],[-6,5,-6],[4,9,9],[4,8,-10],[-10,1,-5],[-2,-5,-1],[-5,5,7],[-8,-5,-10],[2,-10,1],[5,5,3],[-9,4,1],[6,2,-7]],[[-1,9,-4],[4,4,6],[-4,-9,9],[10,6,-3],[-1,5,10],[-4,9,-9],[-2,-6,-7],[-4,-5,9],[-4,3,6],[6,-5,-1],[-5,8,-8],[-4,1,9],[-6,8,-3],[-7,-9,6],[6,-1,5]],[[8,6,-1],[-2,-5,8],[-1,-6,-6],[-8,-5,-3],[2,-2,-4],[4,-6,-7],[-7,3,2],[-7,-6,3],[-9,6,10],[4,3,-5],[-3,-9,1],[6,-7,-1],[2,5,10],[-1,3,-4],[9,4,-4]],[[-10,-10,-5],[-7,9,10],[6,-10,2],[-10,-9,-2],[-5,9,-4],[-10,9,3],[1,5,-5],[-1,-8,3],[9,3,-6],[10,-6,1],[-5,2,3],[8,-5,-3],[7,-3,-5],[5,10,3],[-2,7,6]],[[-8,1,5],[-5,-7,5],[3,3,8],[-2,3,2],[-6,-3,-2],[3,9,10],[-7,8,-7],[1,6,-6],[4,-9,10],[7,6,10],[-8,-8,6],[-3,-6,6],[-6,5,-3],[-6,1,-7],[7,-10,1]],[[-10,5,-8],[-7,6,3],[-9,1,1],[-5,2,-2],[-8,3,9],[9,7,-7],[-5,-7,10],[-2,-9,2],[-6,6,-4],[1,7,-9],[-9,6,-2],[-10,-9,-7],[7,9,4],[-7,-8,-10],[-1,-4,4]],[[5,-4,9],[5,-3,6],[-5,-1,10],[-6,8,10],[-6,-1,-1],[6,10,6],[7,9,-8],[-2,-10,7],[-10,7,-7],[-6,-9,-5],[-1,6,-2],[1,6,9],[-8,6,4],[8,-6,-2],[3,6,-4]]], dtype = "int64")#candidate|7186|(12, 15, 3)|const|int64
bop_7187 = relay.less_equal(var_7185.astype('bool'), relay.reshape(const_7186.astype('bool'), relay.shape_of(var_7185))) # shape=(12, 15, 3)
output = bop_7187
output2 = bop_7187
func_7194 = relay.Function([var_7185,], output)
mod['func_7194'] = func_7194
mod = relay.transform.InferType()(mod)
var_7195 = relay.var("var_7195", dtype = "int64", shape = (12, 15, 3))#candidate|7195|(12, 15, 3)|var|int64
output = func_7194(var_7195)
func_7196 = relay.Function([var_7195], output)
mutated_mod['func_7196'] = func_7196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7134_call = mod.get_global_var('func_7134')
func_7136_call = mutated_mod.get_global_var('func_7136')
call_7236 = relay.TupleGetItem(func_7134_call(), 0)
call_7237 = relay.TupleGetItem(func_7136_call(), 0)
func_4930_call = mod.get_global_var('func_4930')
func_4932_call = mutated_mod.get_global_var('func_4932')
var_7250 = relay.var("var_7250", dtype = "float64", shape = (144,))#candidate|7250|(144,)|var|float64
call_7249 = func_4930_call(relay.reshape(var_7250.astype('float64'), [3, 6, 8]))
call_7251 = func_4930_call(relay.reshape(var_7250.astype('float64'), [3, 6, 8]))
output = relay.Tuple([call_7236,call_7249,var_7250,])
output2 = relay.Tuple([call_7237,call_7251,var_7250,])
func_7280 = relay.Function([var_7250,], output)
mod['func_7280'] = func_7280
mod = relay.transform.InferType()(mod)
var_7281 = relay.var("var_7281", dtype = "float64", shape = (144,))#candidate|7281|(144,)|var|float64
output = func_7280(var_7281)
func_7282 = relay.Function([var_7281], output)
mutated_mod['func_7282'] = func_7282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1142_call = mod.get_global_var('func_1142')
func_1143_call = mutated_mod.get_global_var('func_1143')
call_7304 = relay.TupleGetItem(func_1142_call(), 0)
call_7305 = relay.TupleGetItem(func_1143_call(), 0)
func_3204_call = mod.get_global_var('func_3204')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_7312 = func_3204_call()
call_7313 = func_3204_call()
output = relay.Tuple([call_7304,call_7312,])
output2 = relay.Tuple([call_7305,call_7313,])
func_7333 = relay.Function([], output)
mod['func_7333'] = func_7333
mod = relay.transform.InferType()(mod)
mutated_mod['func_7333'] = func_7333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7333_call = mutated_mod.get_global_var('func_7333')
call_7334 = func_7333_call()
output = call_7334
func_7335 = relay.Function([], output)
mutated_mod['func_7335'] = func_7335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_282_call = mutated_mod.get_global_var('func_282')
call_7354 = relay.TupleGetItem(func_281_call(), 0)
call_7355 = relay.TupleGetItem(func_282_call(), 0)
func_2193_call = mod.get_global_var('func_2193')
func_2196_call = mutated_mod.get_global_var('func_2196')
var_7357 = relay.var("var_7357", dtype = "uint16", shape = ())#candidate|7357|()|var|uint16
var_7358 = relay.var("var_7358", dtype = "uint16", shape = (154,))#candidate|7358|(154,)|var|uint16
call_7356 = relay.TupleGetItem(func_2193_call(relay.reshape(var_7357.astype('uint16'), []), relay.reshape(var_7358.astype('uint16'), [154,]), ), 0)
call_7359 = relay.TupleGetItem(func_2196_call(relay.reshape(var_7357.astype('uint16'), []), relay.reshape(var_7358.astype('uint16'), [154,]), ), 0)
output = relay.Tuple([call_7354,call_7356,var_7357,var_7358,])
output2 = relay.Tuple([call_7355,call_7359,var_7357,var_7358,])
func_7363 = relay.Function([var_7357,var_7358,], output)
mod['func_7363'] = func_7363
mod = relay.transform.InferType()(mod)
var_7364 = relay.var("var_7364", dtype = "uint16", shape = ())#candidate|7364|()|var|uint16
var_7365 = relay.var("var_7365", dtype = "uint16", shape = (154,))#candidate|7365|(154,)|var|uint16
output = func_7363(var_7364,var_7365,)
func_7366 = relay.Function([var_7364,var_7365,], output)
mutated_mod['func_7366'] = func_7366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4123_call = mod.get_global_var('func_4123')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_7420 = func_4123_call()
call_7421 = func_4123_call()
output = relay.Tuple([call_7420,])
output2 = relay.Tuple([call_7421,])
func_7422 = relay.Function([], output)
mod['func_7422'] = func_7422
mod = relay.transform.InferType()(mod)
mutated_mod['func_7422'] = func_7422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7422_call = mutated_mod.get_global_var('func_7422')
call_7423 = func_7422_call()
output = call_7423
func_7424 = relay.Function([], output)
mutated_mod['func_7424'] = func_7424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1233_call = mutated_mod.get_global_var('func_1233')
call_7458 = relay.TupleGetItem(func_1232_call(), 0)
call_7459 = relay.TupleGetItem(func_1233_call(), 0)
output = call_7458
output2 = call_7459
func_7467 = relay.Function([], output)
mod['func_7467'] = func_7467
mod = relay.transform.InferType()(mod)
output = func_7467()
func_7468 = relay.Function([], output)
mutated_mod['func_7468'] = func_7468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4123_call = mod.get_global_var('func_4123')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_7513 = func_4123_call()
call_7514 = func_4123_call()
output = call_7513
output2 = call_7514
func_7538 = relay.Function([], output)
mod['func_7538'] = func_7538
mod = relay.transform.InferType()(mod)
output = func_7538()
func_7539 = relay.Function([], output)
mutated_mod['func_7539'] = func_7539
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7580 = relay.const([[[True,False,False,True,True,False],[True,False,False,True,False,False],[True,False,True,True,False,False],[True,False,False,False,True,True],[True,True,False,True,False,False],[True,True,False,False,False,True],[False,True,False,False,True,False],[False,False,True,True,True,True],[False,True,True,False,True,False],[True,False,True,False,True,True]],[[False,True,True,False,True,True],[True,True,True,True,False,False],[False,False,False,True,False,True],[False,False,False,True,False,True],[True,False,True,False,False,True],[True,False,False,False,False,True],[False,True,False,True,True,False],[True,True,True,True,False,True],[False,False,True,True,True,True],[False,False,True,False,False,True]],[[True,True,True,True,False,True],[False,False,True,False,True,False],[True,False,True,False,True,True],[True,True,True,False,False,False],[True,True,False,True,True,False],[False,False,True,False,True,True],[True,True,True,False,True,False],[False,False,False,True,False,True],[False,True,True,True,True,True],[True,True,False,True,False,True]],[[True,False,True,True,False,False],[False,False,True,False,False,True],[False,True,True,True,False,False],[False,True,True,True,False,True],[True,False,False,True,True,False],[True,True,False,False,False,True],[True,False,True,False,False,True],[True,True,False,True,False,True],[True,False,False,False,False,False],[True,True,False,True,False,False]],[[True,True,True,False,False,True],[True,True,True,False,True,False],[True,True,True,False,False,True],[True,True,True,True,True,True],[True,True,False,False,False,True],[False,False,False,True,False,False],[False,True,True,True,True,True],[True,False,False,False,False,False],[True,True,True,True,False,False],[False,False,True,True,False,False]],[[False,False,False,False,True,False],[True,True,True,False,False,False],[True,False,False,True,False,True],[True,False,False,False,True,True],[True,True,True,False,False,True],[False,False,True,False,True,False],[False,False,True,True,False,True],[True,False,True,False,True,False],[True,True,False,True,True,True],[False,False,False,True,True,True]],[[False,True,True,True,False,False],[True,False,False,False,False,True],[False,True,True,True,True,False],[True,False,True,True,False,True],[False,False,True,True,False,False],[False,False,False,True,False,False],[False,True,False,False,False,False],[True,False,False,False,True,True],[True,True,False,False,False,False],[True,True,False,True,False,False]],[[True,False,True,True,True,True],[True,True,False,False,False,False],[False,True,False,False,False,False],[False,True,True,False,True,True],[False,True,False,False,False,False],[True,True,False,False,True,False],[True,False,True,True,False,True],[False,True,True,False,True,True],[False,True,False,True,True,True],[True,True,False,True,False,False]],[[False,True,False,False,True,True],[False,False,True,False,True,False],[True,True,True,False,False,False],[True,False,False,True,False,True],[True,True,True,True,False,True],[False,False,False,False,True,True],[True,True,True,False,True,False],[False,True,False,True,True,False],[False,True,False,False,False,False],[True,True,True,False,True,False]],[[True,True,False,True,True,True],[False,False,True,True,False,False],[False,True,True,False,False,True],[False,False,False,False,False,False],[True,False,False,False,False,True],[False,False,False,True,True,True],[False,False,True,True,True,True],[False,True,False,True,True,True],[False,True,True,False,False,False],[True,True,False,True,True,False]],[[False,False,False,False,True,False],[True,True,False,False,True,True],[True,True,True,False,False,False],[True,True,False,False,True,False],[False,False,True,False,True,False],[True,True,False,True,True,True],[True,False,True,True,False,False],[True,False,True,False,False,True],[False,True,False,False,True,False],[False,False,False,True,False,False]]], dtype = "bool")#candidate|7580|(11, 10, 6)|const|bool
var_7581 = relay.var("var_7581", dtype = "bool", shape = (11, 10, 6))#candidate|7581|(11, 10, 6)|var|bool
bop_7582 = relay.logical_and(const_7580.astype('bool'), relay.reshape(var_7581.astype('bool'), relay.shape_of(const_7580))) # shape=(11, 10, 6)
const_7593 = relay.const([[[True,False,False,False,False,False],[True,True,False,True,False,False],[False,False,False,False,True,True],[False,False,True,False,True,False],[True,True,False,False,True,True],[True,False,True,True,False,False],[True,False,True,True,True,True],[True,True,False,False,True,True],[True,True,True,False,False,True],[False,True,False,False,True,False]],[[True,False,False,True,False,True],[True,True,True,False,True,False],[False,False,False,False,False,True],[True,True,True,True,True,True],[False,True,False,False,False,True],[False,True,False,True,False,False],[False,True,True,True,False,False],[True,False,True,True,False,True],[True,True,True,False,False,False],[True,False,False,True,True,False]],[[False,True,True,False,False,False],[False,False,True,False,True,True],[False,True,True,True,False,True],[True,True,True,False,True,True],[False,False,False,False,True,True],[False,False,False,False,False,True],[False,True,True,True,True,True],[True,True,False,False,True,False],[False,False,False,True,False,True],[False,False,False,False,True,True]],[[True,True,True,False,True,False],[True,True,True,False,True,False],[True,False,True,True,False,False],[False,False,False,False,True,False],[True,False,True,True,False,False],[True,False,True,False,False,True],[False,True,False,True,True,True],[True,True,True,True,False,False],[True,False,False,False,False,False],[False,False,False,True,True,False]],[[True,False,False,True,True,False],[False,True,True,False,True,True],[False,False,False,True,True,False],[True,True,True,False,True,True],[False,True,True,False,True,True],[False,False,True,True,True,False],[True,True,False,True,False,True],[False,False,True,False,True,True],[False,True,False,True,True,True],[True,True,False,False,True,True]],[[True,True,False,True,False,True],[True,False,True,True,True,True],[False,True,True,False,True,False],[True,True,True,True,True,False],[False,False,True,False,False,False],[False,False,False,False,True,False],[True,False,False,False,False,True],[True,False,False,False,False,True],[True,True,True,False,False,False],[True,False,False,False,True,False]],[[True,True,False,True,True,True],[True,False,False,False,True,False],[True,False,False,False,True,True],[True,False,False,False,False,True],[False,True,True,False,False,False],[True,True,True,True,False,False],[True,True,True,True,True,False],[True,True,False,True,True,True],[False,False,True,True,True,False],[False,True,True,True,False,True]],[[False,True,False,True,False,False],[False,True,False,True,False,True],[True,True,False,True,True,True],[True,True,False,False,False,True],[False,False,False,False,False,False],[True,False,True,False,True,False],[False,True,True,False,False,False],[False,True,True,False,True,False],[False,False,False,False,False,False],[True,True,True,True,True,True]],[[False,False,True,True,False,False],[True,True,False,True,True,False],[True,True,False,False,False,True],[True,False,True,True,False,True],[True,True,False,False,False,True],[True,False,False,False,False,False],[True,True,True,True,False,True],[True,True,False,True,False,False],[False,True,False,True,False,False],[True,True,True,True,False,False]],[[True,True,False,True,False,False],[True,True,False,True,False,False],[False,True,False,False,True,False],[True,True,True,True,True,True],[False,False,False,True,True,False],[True,False,False,False,True,False],[False,True,True,False,False,True],[True,False,False,True,False,True],[True,True,True,False,True,False],[True,True,False,True,False,True]],[[False,False,False,False,False,True],[False,False,False,True,True,False],[False,False,False,False,True,True],[False,False,False,True,False,True],[True,True,False,True,False,True],[False,False,True,False,False,True],[False,False,True,False,True,False],[True,True,False,True,False,True],[False,False,True,True,True,True],[False,False,False,True,True,True]]], dtype = "bool")#candidate|7593|(11, 10, 6)|const|bool
bop_7594 = relay.bitwise_or(bop_7582.astype('int8'), relay.reshape(const_7593.astype('int8'), relay.shape_of(bop_7582))) # shape=(11, 10, 6)
uop_7598 = relay.log(var_7581.astype('float64')) # shape=(11, 10, 6)
uop_7602 = relay.erf(uop_7598.astype('float32')) # shape=(11, 10, 6)
output = relay.Tuple([bop_7594,uop_7602,])
output2 = relay.Tuple([bop_7594,uop_7602,])
func_7606 = relay.Function([var_7581,], output)
mod['func_7606'] = func_7606
mod = relay.transform.InferType()(mod)
mutated_mod['func_7606'] = func_7606
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7607 = relay.var("var_7607", dtype = "bool", shape = (11, 10, 6))#candidate|7607|(11, 10, 6)|var|bool
func_7606_call = mutated_mod.get_global_var('func_7606')
call_7608 = func_7606_call(var_7607)
output = call_7608
func_7609 = relay.Function([var_7607], output)
mutated_mod['func_7609'] = func_7609
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7618 = relay.var("var_7618", dtype = "float64", shape = (12, 4, 5))#candidate|7618|(12, 4, 5)|var|float64
uop_7619 = relay.asin(var_7618.astype('float64')) # shape=(12, 4, 5)
output = uop_7619
output2 = uop_7619
func_7625 = relay.Function([var_7618,], output)
mod['func_7625'] = func_7625
mod = relay.transform.InferType()(mod)
mutated_mod['func_7625'] = func_7625
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7626 = relay.var("var_7626", dtype = "float64", shape = (12, 4, 5))#candidate|7626|(12, 4, 5)|var|float64
func_7625_call = mutated_mod.get_global_var('func_7625')
call_7627 = func_7625_call(var_7626)
output = call_7627
func_7628 = relay.Function([var_7626], output)
mutated_mod['func_7628'] = func_7628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4103_call = mod.get_global_var('func_4103')
func_4104_call = mutated_mod.get_global_var('func_4104')
call_7690 = relay.TupleGetItem(func_4103_call(), 1)
call_7691 = relay.TupleGetItem(func_4104_call(), 1)
output = call_7690
output2 = call_7691
func_7742 = relay.Function([], output)
mod['func_7742'] = func_7742
mod = relay.transform.InferType()(mod)
mutated_mod['func_7742'] = func_7742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7742_call = mutated_mod.get_global_var('func_7742')
call_7743 = func_7742_call()
output = call_7743
func_7744 = relay.Function([], output)
mutated_mod['func_7744'] = func_7744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1960_call = mod.get_global_var('func_1960')
func_1961_call = mutated_mod.get_global_var('func_1961')
call_7794 = func_1960_call()
call_7795 = func_1960_call()
output = call_7794
output2 = call_7795
func_7801 = relay.Function([], output)
mod['func_7801'] = func_7801
mod = relay.transform.InferType()(mod)
mutated_mod['func_7801'] = func_7801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7801_call = mutated_mod.get_global_var('func_7801')
call_7802 = func_7801_call()
output = call_7802
func_7803 = relay.Function([], output)
mutated_mod['func_7803'] = func_7803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3433_call = mod.get_global_var('func_3433')
func_3435_call = mutated_mod.get_global_var('func_3435')
call_7856 = relay.TupleGetItem(func_3433_call(), 0)
call_7857 = relay.TupleGetItem(func_3435_call(), 0)
output = relay.Tuple([call_7856,])
output2 = relay.Tuple([call_7857,])
func_7860 = relay.Function([], output)
mod['func_7860'] = func_7860
mod = relay.transform.InferType()(mod)
output = func_7860()
func_7861 = relay.Function([], output)
mutated_mod['func_7861'] = func_7861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4315_call = mod.get_global_var('func_4315')
func_4316_call = mutated_mod.get_global_var('func_4316')
call_7864 = func_4315_call()
call_7865 = func_4315_call()
output = relay.Tuple([call_7864,])
output2 = relay.Tuple([call_7865,])
func_7869 = relay.Function([], output)
mod['func_7869'] = func_7869
mod = relay.transform.InferType()(mod)
mutated_mod['func_7869'] = func_7869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7869_call = mutated_mod.get_global_var('func_7869')
call_7870 = func_7869_call()
output = call_7870
func_7871 = relay.Function([], output)
mutated_mod['func_7871'] = func_7871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1752_call = mod.get_global_var('func_1752')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_7931 = func_1752_call()
call_7932 = func_1752_call()
output = call_7931
output2 = call_7932
func_7953 = relay.Function([], output)
mod['func_7953'] = func_7953
mod = relay.transform.InferType()(mod)
output = func_7953()
func_7954 = relay.Function([], output)
mutated_mod['func_7954'] = func_7954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6376_call = mod.get_global_var('func_6376')
func_6378_call = mutated_mod.get_global_var('func_6378')
call_7955 = relay.TupleGetItem(func_6376_call(), 0)
call_7956 = relay.TupleGetItem(func_6378_call(), 0)
output = relay.Tuple([call_7955,])
output2 = relay.Tuple([call_7956,])
func_7967 = relay.Function([], output)
mod['func_7967'] = func_7967
mod = relay.transform.InferType()(mod)
mutated_mod['func_7967'] = func_7967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7967_call = mutated_mod.get_global_var('func_7967')
call_7968 = func_7967_call()
output = call_7968
func_7969 = relay.Function([], output)
mutated_mod['func_7969'] = func_7969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6596_call = mod.get_global_var('func_6596')
func_6598_call = mutated_mod.get_global_var('func_6598')
call_8002 = relay.TupleGetItem(func_6596_call(), 2)
call_8003 = relay.TupleGetItem(func_6598_call(), 2)
output = call_8002
output2 = call_8003
func_8009 = relay.Function([], output)
mod['func_8009'] = func_8009
mod = relay.transform.InferType()(mod)
mutated_mod['func_8009'] = func_8009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8009_call = mutated_mod.get_global_var('func_8009')
call_8010 = func_8009_call()
output = call_8010
func_8011 = relay.Function([], output)
mutated_mod['func_8011'] = func_8011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8075 = relay.var("var_8075", dtype = "bool", shape = (5, 11, 11))#candidate|8075|(5, 11, 11)|var|bool
var_8076 = relay.var("var_8076", dtype = "bool", shape = (5, 11, 11))#candidate|8076|(5, 11, 11)|var|bool
bop_8077 = relay.logical_and(var_8075.astype('bool'), relay.reshape(var_8076.astype('bool'), relay.shape_of(var_8075))) # shape=(5, 11, 11)
uop_8087 = relay.sin(bop_8077.astype('float32')) # shape=(5, 11, 11)
output = relay.Tuple([uop_8087,])
output2 = relay.Tuple([uop_8087,])
func_8089 = relay.Function([var_8075,var_8076,], output)
mod['func_8089'] = func_8089
mod = relay.transform.InferType()(mod)
var_8090 = relay.var("var_8090", dtype = "bool", shape = (5, 11, 11))#candidate|8090|(5, 11, 11)|var|bool
var_8091 = relay.var("var_8091", dtype = "bool", shape = (5, 11, 11))#candidate|8091|(5, 11, 11)|var|bool
output = func_8089(var_8090,var_8091,)
func_8092 = relay.Function([var_8090,var_8091,], output)
mutated_mod['func_8092'] = func_8092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6376_call = mod.get_global_var('func_6376')
func_6378_call = mutated_mod.get_global_var('func_6378')
call_8094 = relay.TupleGetItem(func_6376_call(), 1)
call_8095 = relay.TupleGetItem(func_6378_call(), 1)
func_7194_call = mod.get_global_var('func_7194')
func_7196_call = mutated_mod.get_global_var('func_7196')
const_8109 = relay.const([7,1,-9,7,-6,-8,-10,-4,2,9,-9,2,3,-5,6,7,-2,-9,5,2,3,-8,10,3,7,-5,7,2,3,-6,3,-4,2,-7,-3,8,-8,-10,10,10,7,6,5,8,5,-10,-9,-7,-10,-8,3,1,-6,-10,6,6,5,1,-9,-9,3,7,6,3,-8,8,-10,-5,-2,5,-4,3,-4,-1,-3,1,2,10,-2,3,-7,-3,2,5,2,-1,-4,8,-1,3,1,-2,10,10,-4,-1,-4,9,-4,-1,4,-5,-8,-6,-1,-3,-1,-5,4,4,-8,10,-1,9,1,2,-2,6,9,9,3,2,4,6,3,-7,-6,5,3,-5,-6,4,3,9,5,1,9,-1,-1,2,-10,-4,-5,-6,-5,-7,-7,10,-2,-3,9,5,7,5,-7,-3,6,-3,-8,-1,9,5,-8,5,8,-9,2,-6,-1,9,10,3,9,8,5,10,7,10,-4,9,3,-8,-1,-5,9,-8,-4,-4,-7,10,-2,-7,-10,8,2,-6,5,-1,2,9,-10,8,-10,-8,-5,-10,-1,-7,4,4,3,2,-6,4,-10,9,10,5,2,-6,4,-5,2,7,-7,1,-3,-8,7,6,5,-7,-3,-4,8,1,5,-6,-7,-1,5,6,7,6,-10,-1,-10,-9,-1,-9,2,-10,7,3,8,-10,-8,-3,-4,8,3,-6,-6,-7,9,-7,-5,9,-2,6,6,4,-4,-8,-6,-10,-6,2,-5,-10,-3,7,-3,-2,1,-6,5,3,-7,-8,9,-1,-8,6,2,-10,-4,-4,5,3,-5,-3,1,10,8,2,-7,2,-8,9,-8,-4,5,-1,-4,-6,-5,9,-6,-5,-8,4,10,3,6,-7,-10,-7,8,7,6,3,4,-9,-3,-5,-9,-6,-4,-6,-2,5,3,9,3,5,9,1,10,-4,-2,3,7,-2,-10,-1,3,-4,-1,-8,-9,2,-1,-9,-2,-3,1,8,7,9,10,10,10,-8,7,3,-10,-3,-9,3,5,-10,4,-6,-9,10,7,-3,-6,-7,-10,10,-7,-3,7,-2,4,1,-1,2,-2,-1,4,7,6,6,6,6,-9,4,4,10,-9,7,8,1,-2,10,-8,-6,2,-10,10,-4,4,-6,-1,4,5,-1,1,-4,4,-6,2,-7,-6,3,-5,-6,2,-5,6,4,-3,4,-6,-4,2,-5,6,9,10,-9,-8,2,-4,-6,8,-4,4,4,6,-2,-2,3,10,-1,5,-5,-4,4,6,10,1,-7,-2,6,-3,-6,-7,2,-4,-8,-2,3,-2,5,8,-3,1,-3,3,1,-10,-10,10,4,6,3,7,-7,7,-6,-9,-4,-9,3,8,7,-1,-7,-2,4,-5,9,5,10,7,-6,2,-7,7,-2,-4,-5,9,-5,-2,-10,-8,-8,4,6,1,10,-2,-6,-6,5], dtype = "int64")#candidate|8109|(540,)|const|int64
call_8108 = func_7194_call(relay.reshape(const_8109.astype('int64'), [12, 15, 3]))
call_8110 = func_7194_call(relay.reshape(const_8109.astype('int64'), [12, 15, 3]))
output = relay.Tuple([call_8094,call_8108,const_8109,])
output2 = relay.Tuple([call_8095,call_8110,const_8109,])
func_8111 = relay.Function([], output)
mod['func_8111'] = func_8111
mod = relay.transform.InferType()(mod)
mutated_mod['func_8111'] = func_8111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8111_call = mutated_mod.get_global_var('func_8111')
call_8112 = func_8111_call()
output = call_8112
func_8113 = relay.Function([], output)
mutated_mod['func_8113'] = func_8113
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8118 = relay.var("var_8118", dtype = "uint32", shape = (16, 8, 12))#candidate|8118|(16, 8, 12)|var|uint32
var_8119 = relay.var("var_8119", dtype = "uint32", shape = (16, 8, 12))#candidate|8119|(16, 8, 12)|var|uint32
bop_8120 = relay.bitwise_and(var_8118.astype('uint32'), relay.reshape(var_8119.astype('uint32'), relay.shape_of(var_8118))) # shape=(16, 8, 12)
func_2237_call = mod.get_global_var('func_2237')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_8134 = func_2237_call()
call_8135 = func_2237_call()
output = relay.Tuple([bop_8120,call_8134,])
output2 = relay.Tuple([bop_8120,call_8135,])
func_8195 = relay.Function([var_8118,var_8119,], output)
mod['func_8195'] = func_8195
mod = relay.transform.InferType()(mod)
mutated_mod['func_8195'] = func_8195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8195_call = mutated_mod.get_global_var('func_8195')
var_8197 = relay.var("var_8197", dtype = "uint32", shape = (16, 8, 12))#candidate|8197|(16, 8, 12)|var|uint32
var_8198 = relay.var("var_8198", dtype = "uint32", shape = (16, 8, 12))#candidate|8198|(16, 8, 12)|var|uint32
call_8196 = func_8195_call(var_8197,var_8198,)
output = call_8196
func_8199 = relay.Function([var_8197,var_8198,], output)
mutated_mod['func_8199'] = func_8199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_8216 = relay.TupleGetItem(func_3457_call(), 0)
call_8217 = relay.TupleGetItem(func_3459_call(), 0)
func_2404_call = mod.get_global_var('func_2404')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_8236 = func_2404_call()
call_8237 = func_2404_call()
output = relay.Tuple([call_8216,call_8236,])
output2 = relay.Tuple([call_8217,call_8237,])
func_8240 = relay.Function([], output)
mod['func_8240'] = func_8240
mod = relay.transform.InferType()(mod)
output = func_8240()
func_8241 = relay.Function([], output)
mutated_mod['func_8241'] = func_8241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6668_call = mod.get_global_var('func_6668')
func_6670_call = mutated_mod.get_global_var('func_6670')
call_8254 = relay.TupleGetItem(func_6668_call(), 3)
call_8255 = relay.TupleGetItem(func_6670_call(), 3)
func_2856_call = mod.get_global_var('func_2856')
func_2858_call = mutated_mod.get_global_var('func_2858')
call_8257 = relay.TupleGetItem(func_2856_call(), 0)
call_8258 = relay.TupleGetItem(func_2858_call(), 0)
func_7363_call = mod.get_global_var('func_7363')
func_7366_call = mutated_mod.get_global_var('func_7366')
const_8290 = relay.const(-3, dtype = "uint16")#candidate|8290|()|const|uint16
var_8291 = relay.var("var_8291", dtype = "uint16", shape = (154, 1))#candidate|8291|(154, 1)|var|uint16
call_8289 = relay.TupleGetItem(func_7363_call(relay.reshape(const_8290.astype('uint16'), []), relay.reshape(var_8291.astype('uint16'), [154,]), ), 3)
call_8292 = relay.TupleGetItem(func_7366_call(relay.reshape(const_8290.astype('uint16'), []), relay.reshape(var_8291.astype('uint16'), [154,]), ), 3)
output = relay.Tuple([call_8254,call_8257,call_8289,const_8290,var_8291,])
output2 = relay.Tuple([call_8255,call_8258,call_8292,const_8290,var_8291,])
func_8302 = relay.Function([var_8291,], output)
mod['func_8302'] = func_8302
mod = relay.transform.InferType()(mod)
var_8303 = relay.var("var_8303", dtype = "uint16", shape = (154, 1))#candidate|8303|(154, 1)|var|uint16
output = func_8302(var_8303)
func_8304 = relay.Function([var_8303], output)
mutated_mod['func_8304'] = func_8304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7134_call = mod.get_global_var('func_7134')
func_7136_call = mutated_mod.get_global_var('func_7136')
call_8315 = relay.TupleGetItem(func_7134_call(), 0)
call_8316 = relay.TupleGetItem(func_7136_call(), 0)
output = call_8315
output2 = call_8316
func_8330 = relay.Function([], output)
mod['func_8330'] = func_8330
mod = relay.transform.InferType()(mod)
output = func_8330()
func_8331 = relay.Function([], output)
mutated_mod['func_8331'] = func_8331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5757_call = mod.get_global_var('func_5757')
func_5759_call = mutated_mod.get_global_var('func_5759')
call_8362 = relay.TupleGetItem(func_5757_call(), 0)
call_8363 = relay.TupleGetItem(func_5759_call(), 0)
func_7606_call = mod.get_global_var('func_7606')
func_7609_call = mutated_mod.get_global_var('func_7609')
var_8366 = relay.var("var_8366", dtype = "bool", shape = (660, 1))#candidate|8366|(660, 1)|var|bool
call_8365 = relay.TupleGetItem(func_7606_call(relay.reshape(var_8366.astype('bool'), [11, 10, 6])), 1)
call_8367 = relay.TupleGetItem(func_7609_call(relay.reshape(var_8366.astype('bool'), [11, 10, 6])), 1)
output = relay.Tuple([call_8362,call_8365,var_8366,])
output2 = relay.Tuple([call_8363,call_8367,var_8366,])
func_8397 = relay.Function([var_8366,], output)
mod['func_8397'] = func_8397
mod = relay.transform.InferType()(mod)
mutated_mod['func_8397'] = func_8397
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8398 = relay.var("var_8398", dtype = "bool", shape = (660, 1))#candidate|8398|(660, 1)|var|bool
func_8397_call = mutated_mod.get_global_var('func_8397')
call_8399 = func_8397_call(var_8398)
output = call_8399
func_8400 = relay.Function([var_8398], output)
mutated_mod['func_8400'] = func_8400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1752_call = mod.get_global_var('func_1752')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_8486 = func_1752_call()
call_8487 = func_1752_call()
output = relay.Tuple([call_8486,])
output2 = relay.Tuple([call_8487,])
func_8499 = relay.Function([], output)
mod['func_8499'] = func_8499
mod = relay.transform.InferType()(mod)
mutated_mod['func_8499'] = func_8499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8499_call = mutated_mod.get_global_var('func_8499')
call_8500 = func_8499_call()
output = call_8500
func_8501 = relay.Function([], output)
mutated_mod['func_8501'] = func_8501
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8504 = relay.var("var_8504", dtype = "uint8", shape = (10, 3, 15))#candidate|8504|(10, 3, 15)|var|uint8
const_8505 = relay.const([[[-10,-10,1,6,2,10,10,2,2,8,-4,-8,7,-7,9],[6,6,-4,7,1,-4,9,-10,2,6,-7,-7,9,9,8],[1,7,-9,-6,-3,-6,-9,-10,3,8,-4,-4,-2,-6,-10]],[[-8,8,8,-10,-6,3,-1,4,-9,7,-10,4,3,6,6],[-4,7,-4,9,-9,-9,6,5,5,-9,-3,3,-3,-5,6],[3,8,1,-4,7,7,8,-10,-5,8,7,-3,1,9,-2]],[[-7,-6,-6,-8,9,-6,3,-10,-6,8,-9,7,7,7,-4],[-10,8,8,3,6,3,-8,7,-9,-5,9,2,-5,2,5],[-4,8,3,8,4,-7,6,-3,-5,8,-9,-5,10,2,-3]],[[9,3,1,-5,-1,-1,-6,-6,-3,-3,-3,5,5,-10,-1],[-5,-2,10,-6,2,-4,6,1,-10,6,-5,-8,-9,-8,-2],[-3,9,-7,9,-4,9,-4,-1,-10,1,-6,7,7,-7,-4]],[[-5,-5,-2,-5,-4,-4,8,-1,-4,2,6,-2,-2,-10,5],[5,1,-6,2,8,2,-10,-9,-1,-1,8,1,-2,-10,-1],[6,-7,-5,2,4,-3,1,9,4,4,-3,5,-4,-8,-9]],[[9,6,-4,1,-10,7,3,7,-9,10,-8,-10,8,10,-8],[4,6,-5,2,-8,1,6,-5,-4,5,10,8,4,3,1],[-5,-1,6,3,2,-10,7,6,8,4,5,-7,-3,-8,-9]],[[8,-5,-6,2,1,-9,6,-5,-7,2,8,-7,-8,-10,-5],[-5,-2,1,-3,5,7,-3,9,-3,2,-10,-3,-9,-5,7],[-5,-4,-3,5,8,-10,-6,-7,-10,3,-6,-6,8,-1,-2]],[[7,-1,8,-6,1,-3,-8,-3,-5,-5,-7,-9,-1,-6,-2],[-1,8,9,-7,9,10,1,2,-3,5,5,-1,4,-5,-6],[-9,-7,-8,-2,-3,7,6,1,9,7,10,-7,8,4,-10]],[[-2,7,7,-6,-2,-2,2,4,6,-5,-9,-4,-7,8,8],[2,-8,-7,-4,-5,-4,5,7,-7,-5,5,-7,-10,5,-8],[7,-1,10,-1,-5,-3,3,2,7,4,-2,-8,10,-5,-8]],[[-8,-4,-4,-10,-9,1,-1,9,-6,-3,-10,7,-5,-6,4],[5,10,10,4,-9,5,6,-4,-9,3,9,8,1,-7,-4],[-2,-2,8,6,-1,8,5,-2,-1,9,7,-7,-6,-8,5]]], dtype = "uint8")#candidate|8505|(10, 3, 15)|const|uint8
bop_8506 = relay.not_equal(var_8504.astype('bool'), relay.reshape(const_8505.astype('bool'), relay.shape_of(var_8504))) # shape=(10, 3, 15)
func_2377_call = mod.get_global_var('func_2377')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_8512 = relay.TupleGetItem(func_2377_call(), 0)
call_8513 = relay.TupleGetItem(func_2378_call(), 0)
bop_8516 = relay.right_shift(bop_8506.astype('uint8'), relay.reshape(var_8504.astype('uint8'), relay.shape_of(bop_8506))) # shape=(10, 3, 15)
output = relay.Tuple([call_8512,bop_8516,])
output2 = relay.Tuple([call_8513,bop_8516,])
func_8526 = relay.Function([var_8504,], output)
mod['func_8526'] = func_8526
mod = relay.transform.InferType()(mod)
var_8527 = relay.var("var_8527", dtype = "uint8", shape = (10, 3, 15))#candidate|8527|(10, 3, 15)|var|uint8
output = func_8526(var_8527)
func_8528 = relay.Function([var_8527], output)
mutated_mod['func_8528'] = func_8528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_8572 = relay.TupleGetItem(func_1574_call(), 4)
call_8573 = relay.TupleGetItem(func_1576_call(), 4)
func_3246_call = mod.get_global_var('func_3246')
func_3247_call = mutated_mod.get_global_var('func_3247')
call_8584 = func_3246_call()
call_8585 = func_3246_call()
func_6542_call = mod.get_global_var('func_6542')
func_6543_call = mutated_mod.get_global_var('func_6543')
call_8614 = relay.TupleGetItem(func_6542_call(), 0)
call_8615 = relay.TupleGetItem(func_6543_call(), 0)
output = relay.Tuple([call_8572,call_8584,call_8614,])
output2 = relay.Tuple([call_8573,call_8585,call_8615,])
func_8622 = relay.Function([], output)
mod['func_8622'] = func_8622
mod = relay.transform.InferType()(mod)
mutated_mod['func_8622'] = func_8622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8622_call = mutated_mod.get_global_var('func_8622')
call_8623 = func_8622_call()
output = call_8623
func_8624 = relay.Function([], output)
mutated_mod['func_8624'] = func_8624
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8672 = relay.var("var_8672", dtype = "float64", shape = (1, 4, 5))#candidate|8672|(1, 4, 5)|var|float64
var_8673 = relay.var("var_8673", dtype = "float64", shape = (3, 4, 5))#candidate|8673|(3, 4, 5)|var|float64
bop_8674 = relay.power(var_8672.astype('float64'), var_8673.astype('float64')) # shape=(3, 4, 5)
output = bop_8674
output2 = bop_8674
func_8680 = relay.Function([var_8672,var_8673,], output)
mod['func_8680'] = func_8680
mod = relay.transform.InferType()(mod)
var_8681 = relay.var("var_8681", dtype = "float64", shape = (1, 4, 5))#candidate|8681|(1, 4, 5)|var|float64
var_8682 = relay.var("var_8682", dtype = "float64", shape = (3, 4, 5))#candidate|8682|(3, 4, 5)|var|float64
output = func_8680(var_8681,var_8682,)
func_8683 = relay.Function([var_8681,var_8682,], output)
mutated_mod['func_8683'] = func_8683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4638_call = mod.get_global_var('func_4638')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_8693 = func_4638_call()
call_8694 = func_4638_call()
func_1232_call = mod.get_global_var('func_1232')
func_1233_call = mutated_mod.get_global_var('func_1233')
call_8700 = relay.TupleGetItem(func_1232_call(), 1)
call_8701 = relay.TupleGetItem(func_1233_call(), 1)
output = relay.Tuple([call_8693,call_8700,])
output2 = relay.Tuple([call_8694,call_8701,])
func_8709 = relay.Function([], output)
mod['func_8709'] = func_8709
mod = relay.transform.InferType()(mod)
mutated_mod['func_8709'] = func_8709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8709_call = mutated_mod.get_global_var('func_8709')
call_8710 = func_8709_call()
output = call_8710
func_8711 = relay.Function([], output)
mutated_mod['func_8711'] = func_8711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_566_call = mod.get_global_var('func_566')
func_567_call = mutated_mod.get_global_var('func_567')
call_8753 = func_566_call()
call_8754 = func_566_call()
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_8769 = func_490_call()
call_8770 = func_490_call()
func_7801_call = mod.get_global_var('func_7801')
func_7803_call = mutated_mod.get_global_var('func_7803')
call_8771 = func_7801_call()
call_8772 = func_7801_call()
func_1305_call = mod.get_global_var('func_1305')
func_1307_call = mutated_mod.get_global_var('func_1307')
call_8793 = func_1305_call()
call_8794 = func_1305_call()
output = relay.Tuple([call_8753,call_8769,call_8771,call_8793,])
output2 = relay.Tuple([call_8754,call_8770,call_8772,call_8794,])
func_8800 = relay.Function([], output)
mod['func_8800'] = func_8800
mod = relay.transform.InferType()(mod)
output = func_8800()
func_8801 = relay.Function([], output)
mutated_mod['func_8801'] = func_8801
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8885 = relay.const([[[6.867921,5.301269,0.047478,-7.463970,-3.049337,-1.734652,8.094720,-8.958309,6.009147,1.696651,3.139825,-9.091038,0.092783,8.225716],[-8.395472,5.099747,2.169179,4.181267,-2.774899,-5.428475,-2.778236,5.190723,7.804091,-0.560845,1.610810,6.233388,5.495752,-5.259408],[-9.404894,9.452120,-0.833900,9.065802,5.986925,5.184375,-0.108982,-7.084700,-4.731613,-9.042034,-0.410263,-6.750968,2.705689,-7.635449],[4.798924,4.941345,-8.447870,9.807150,8.624520,-8.313544,8.754563,4.146564,4.276733,0.104780,1.712517,4.552937,-5.721027,-6.255030],[-7.142492,-8.463997,2.035223,6.173608,-8.032754,-5.895171,8.646243,-1.644065,-4.865001,7.111672,-0.577631,9.800424,-1.297717,7.312047],[2.285751,-3.217678,-2.015823,5.465959,5.486907,2.915401,5.380295,6.544270,-6.195569,-8.996554,4.398034,4.804759,-3.658264,-0.642853],[3.153011,8.123424,5.442354,-2.638288,-1.326843,2.720275,7.144140,-0.326667,-3.256162,4.693468,6.755608,-3.266987,0.055823,-4.412993],[-7.535975,4.822074,-5.728347,-1.495662,-6.334075,0.207249,3.891002,-8.788083,5.578226,5.405363,7.354141,7.673375,-3.473864,4.480934],[5.568404,6.177353,-0.950488,5.391557,6.422617,-0.051601,5.156119,4.316148,-2.177738,3.474631,-8.058031,-0.546203,2.535201,-2.956477],[0.897671,-2.016578,-8.235128,-6.937394,-6.370779,9.319299,-8.349509,0.850599,-9.104412,-5.328179,0.146483,-4.893917,-1.969942,9.747382]],[[-3.674747,-2.942538,8.715457,-2.374631,-3.370166,3.467849,9.497301,4.776397,-3.973366,3.906938,1.768698,-0.221845,2.332211,-4.949919],[7.714795,3.952339,3.953206,6.213060,-4.798971,-1.590029,-7.344011,3.386816,3.409329,4.375875,-4.477456,-4.327077,-4.542584,-0.723700],[6.569523,-0.202496,-8.724186,9.373359,1.579941,-7.013992,-2.471824,-1.550171,-6.261404,-6.313091,-0.607705,-3.839316,-2.858992,-7.891276],[4.622158,-4.856077,0.360595,4.288934,6.426284,-9.483862,4.066423,-9.658349,9.517409,-2.128090,1.807809,9.439914,9.462417,-3.722511],[-4.226693,-6.602493,8.374244,2.993555,2.324711,-2.898782,9.520703,8.201954,3.449942,-5.692809,4.903893,4.115891,-3.515455,-4.165431],[-8.870793,4.867736,-1.257592,-4.532661,8.263846,-9.063136,-2.042592,0.900029,5.465812,-2.151587,-6.746644,-7.072897,7.371575,-0.371975],[-5.220244,6.795416,8.549908,-9.567622,0.104156,2.576200,-0.787659,7.673574,-9.591696,-9.508451,-5.750649,4.902387,1.590973,-6.205210],[2.651832,-4.401541,7.521364,-5.330864,4.678217,-2.383135,0.505952,3.737343,-7.805170,-0.368976,2.875550,-3.374974,8.884260,-9.198638],[9.509060,9.980685,-9.551792,5.342451,-0.734986,-0.684178,-6.422934,-2.455572,0.665881,7.061446,-1.127154,-9.330830,-4.751190,7.780462],[-8.710619,-6.887233,-3.320601,-5.261697,-1.936203,6.879995,4.335904,-0.368084,-1.859775,6.562596,-0.926162,6.695457,-5.692950,-7.487128]],[[0.465375,-1.442833,4.715362,7.008321,9.008317,-5.934880,3.890022,-0.581354,-6.819281,-7.479576,4.570201,-7.890684,-6.976920,-5.447410],[7.949414,3.734131,7.360337,4.232994,3.877592,-0.262041,-4.449802,-0.957625,-1.468687,2.273596,3.526944,-4.498691,4.434863,-2.542209],[-4.716667,1.128811,6.066605,-7.117567,-7.626004,8.927846,1.765654,-2.507009,5.171862,4.652363,0.545296,-5.114243,4.010456,5.445199],[6.497192,-9.907166,0.333621,0.078440,6.631956,2.983858,8.428391,9.564090,-1.028882,3.395349,-7.243740,-5.547077,4.194446,-6.176620],[3.852699,8.301226,3.235545,-7.694035,3.839324,0.482000,-2.438462,9.307781,0.407280,-0.211137,-9.020984,2.727330,-9.377555,0.318072],[-6.526263,-0.491609,8.700139,-8.959295,-4.726351,3.890260,9.316004,-2.139662,0.333830,5.242498,-1.480275,8.720143,2.673338,7.899254],[-8.481331,4.174164,-1.475637,-1.832740,-7.424719,-5.486097,5.640658,-6.231971,-4.536356,-9.273249,-7.930489,-0.345359,0.658933,-2.063818],[4.391037,2.063395,-6.546622,-9.196206,-7.847350,-6.008395,-2.727288,0.609047,4.056080,-0.173055,-9.477743,3.073777,-9.204829,5.318967],[2.223198,6.041538,0.968175,-3.091783,3.454877,-2.284231,3.261199,-9.805036,8.972265,-3.483100,-3.607708,-2.961500,8.716286,1.673434],[-0.898737,-0.650925,-1.855238,-2.482713,-1.827094,5.545616,8.820577,6.629627,9.354726,-2.340790,-0.057153,0.730418,1.280810,8.639046]]], dtype = "float64")#candidate|8885|(3, 10, 14)|const|float64
var_8886 = relay.var("var_8886", dtype = "float64", shape = (3, 10, 14))#candidate|8886|(3, 10, 14)|var|float64
bop_8887 = relay.mod(const_8885.astype('float64'), relay.reshape(var_8886.astype('float64'), relay.shape_of(const_8885))) # shape=(3, 10, 14)
output = relay.Tuple([bop_8887,])
output2 = relay.Tuple([bop_8887,])
func_8898 = relay.Function([var_8886,], output)
mod['func_8898'] = func_8898
mod = relay.transform.InferType()(mod)
var_8899 = relay.var("var_8899", dtype = "float64", shape = (3, 10, 14))#candidate|8899|(3, 10, 14)|var|float64
output = func_8898(var_8899)
func_8900 = relay.Function([var_8899], output)
mutated_mod['func_8900'] = func_8900
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8902 = relay.var("var_8902", dtype = "uint16", shape = (13, 1, 9))#candidate|8902|(13, 1, 9)|var|uint16
var_8903 = relay.var("var_8903", dtype = "uint16", shape = (13, 6, 9))#candidate|8903|(13, 6, 9)|var|uint16
bop_8904 = relay.equal(var_8902.astype('bool'), var_8903.astype('bool')) # shape=(13, 6, 9)
func_5430_call = mod.get_global_var('func_5430')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_8917 = relay.TupleGetItem(func_5430_call(), 0)
call_8918 = relay.TupleGetItem(func_5431_call(), 0)
output = relay.Tuple([bop_8904,call_8917,])
output2 = relay.Tuple([bop_8904,call_8918,])
func_8920 = relay.Function([var_8902,var_8903,], output)
mod['func_8920'] = func_8920
mod = relay.transform.InferType()(mod)
mutated_mod['func_8920'] = func_8920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8920_call = mutated_mod.get_global_var('func_8920')
var_8922 = relay.var("var_8922", dtype = "uint16", shape = (13, 1, 9))#candidate|8922|(13, 1, 9)|var|uint16
var_8923 = relay.var("var_8923", dtype = "uint16", shape = (13, 6, 9))#candidate|8923|(13, 6, 9)|var|uint16
call_8921 = func_8920_call(var_8922,var_8923,)
output = call_8921
func_8924 = relay.Function([var_8922,var_8923,], output)
mutated_mod['func_8924'] = func_8924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_8939 = relay.TupleGetItem(func_1574_call(), 3)
call_8940 = relay.TupleGetItem(func_1576_call(), 3)
func_705_call = mod.get_global_var('func_705')
func_708_call = mutated_mod.get_global_var('func_708')
var_8943 = relay.var("var_8943", dtype = "int16", shape = (252,))#candidate|8943|(252,)|var|int16
const_8944 = relay.const([1.061156,0.168361,-9.374426,-1.419747,-6.958502,-4.646672,5.539905,-6.948322,8.541633,-1.942343,0.385868,-2.530458,-7.738628,9.799940,8.140801,-2.509014,7.945494,8.216636,3.635784,7.691577,6.119006,-1.598374,-9.493123,-8.256973,-1.414637,3.995986,5.955990,1.024214,-9.473953,-5.126874,-4.450044,-4.438437,-0.079168,9.501456,8.080760,6.663430,0.462173,-4.692259,-7.205736,7.134867,7.307984,-3.626605,-3.553854,-4.963952,-2.397635,-8.004216,7.864534,4.241426,-9.680327,6.143090,9.864470,-3.157365,9.286540,-6.272048,1.270614,-3.247191,-9.468008,-0.072448,7.444185,5.172622,7.476687,-8.431143,4.018947,-5.705813,-5.281611,2.369533,-0.703850,-3.609468,-2.219320,1.264940,6.450271,-0.647702,-5.004334,-7.831774,5.710286,-7.999097,-0.819518,-1.034525,-0.605877,1.506646,-0.673864,-1.059826,2.494403,-5.308126,3.971316,8.201294,-2.506108,1.325711,-5.359478,-6.794777,4.919303,-5.583266,1.505640,6.332465,2.081921,-6.277769,-2.414893,-3.771313,-1.007833,2.986852,-5.632323,-3.244496,3.944818,-1.601990,3.766084,0.871265,3.843672,-6.882810,-2.218795,-2.745753,3.732655,-0.239115,4.359633,2.084666,6.509124,2.488217,5.135786,-0.569191,0.842564,4.584701,9.108779,-2.323164,-6.594522,5.116416,-5.556032,5.628788,7.905703,8.302296,-8.638673,-9.596401,-1.333696,-4.321652,6.090112,-7.259773,3.701048,2.554908,-6.062551,7.357955,8.570924,-4.264620,-1.086720,2.690533,7.447275,-5.593491,8.502220,0.403517,-7.936544,0.909132,8.874134,3.654247,4.993800,4.158036,-2.065455,0.326881,-6.389824,3.628385,4.098806,-8.210875,-1.590143,-2.390672,5.372462,9.380852,4.397768,0.708216,-3.205074,5.570085,7.751251,2.046909,7.090159,4.714612,-2.097618,-3.230928,9.694180,-3.223279,6.377846,3.569802,6.103819,6.858775,-8.088019,1.115297,1.200500,-0.037430,4.436530,-3.423624,-7.175306,-4.918186,-7.758783,-6.889133,9.000286,5.420028,-2.677473,3.728124,2.747694,-9.686952,0.651222,-4.368558,6.162330,-3.146174,1.324402,9.640052,-9.784928,-9.237975,9.455989,3.457897,-3.246544,8.374018,1.495734,-7.295026,4.476354,-0.565510,-5.538732,6.346939,-0.825470,-3.744116,-0.701601,9.308441,-4.856467,-5.821311,3.865687,-4.549235,-3.461693,-7.801207,1.419209,4.067251,9.653941,5.088179,-3.507668,1.830748,-3.800609,-3.578487,-3.785887,-3.348684,-6.274317,-5.377395,-6.795000,7.944236,-0.181969,-0.284777,-2.350792,4.687428,-8.994090,6.799882,9.590510,1.632512,-1.586324,6.633305,8.214851,3.985227,-7.532477,2.891235,0.188806,9.361422,-2.053361,4.856216,4.533914,3.886755,7.386273,2.570256,7.261053,8.757254,-6.357124,-3.972449,-3.199938,6.842897,4.781599,9.355654,4.387690,9.990669,-1.875372,-7.364603,7.123018,1.042771,-9.972379,3.689769,7.301305,-3.897855,4.055019,-5.147272,-1.555020,-0.622951,-1.140176,-1.579005,8.601195,-4.590683,-1.825518,1.735930,-7.578321,2.730806,3.036762,-5.158547,5.901266,4.684013,-1.286204,-0.614397,3.547843,-0.286121,-1.677847,-8.281644,-2.134311,6.821252,8.767421,-3.321772,-1.916010,2.949709,8.698356,-1.648606,-4.420820,9.183516,3.916247,4.789623,4.204723,0.594143,5.237700,1.961752,-9.229672,-9.703242,0.174795,2.894288,-7.201285,-3.488036,-3.777536,-2.541008,-0.672169,2.350714,4.119193,-3.744798,9.993646,-2.711448,8.333447,-5.671614,7.705598,-5.177491,-4.440577,-8.115976,-2.120251,-7.351642,5.073671,1.901846,-3.207316,-8.396598,4.177151,-5.428847,-8.917391,7.880081,-3.979760,3.020122,6.325717,6.810142,9.811394,-3.225638,-4.569706,-8.500020,-6.479344,8.928990,8.731545,-3.888708,-4.667317,6.704243,-1.656055,7.565410,-5.637882,-0.247204,-6.294444,4.662520,9.025158,3.392178,-4.398443,2.492896,5.150804,-7.838670,-8.624281,7.459009,5.627683,3.061224,-6.327739,7.615479,6.488639,-5.483913,7.237396,7.553170,8.135808,-9.756037,9.479204,-2.171541,-1.803931,4.610648,-5.404811,0.401767,7.333390,9.590437], dtype = "float64")#candidate|8944|(390,)|const|float64
call_8942 = relay.TupleGetItem(func_705_call(relay.reshape(var_8943.astype('int16'), [252,]), relay.reshape(const_8944.astype('float64'), [13, 10, 3]), ), 3)
call_8945 = relay.TupleGetItem(func_708_call(relay.reshape(var_8943.astype('int16'), [252,]), relay.reshape(const_8944.astype('float64'), [13, 10, 3]), ), 3)
func_3866_call = mod.get_global_var('func_3866')
func_3868_call = mutated_mod.get_global_var('func_3868')
var_8950 = relay.var("var_8950", dtype = "uint32", shape = (1, 40))#candidate|8950|(1, 40)|var|uint32
call_8949 = relay.TupleGetItem(func_3866_call(relay.reshape(var_8950.astype('uint32'), [4, 2, 5])), 1)
call_8951 = relay.TupleGetItem(func_3868_call(relay.reshape(var_8950.astype('uint32'), [4, 2, 5])), 1)
output = relay.Tuple([call_8939,call_8942,var_8943,const_8944,call_8949,var_8950,])
output2 = relay.Tuple([call_8940,call_8945,var_8943,const_8944,call_8951,var_8950,])
func_8952 = relay.Function([var_8943,var_8950,], output)
mod['func_8952'] = func_8952
mod = relay.transform.InferType()(mod)
mutated_mod['func_8952'] = func_8952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8952_call = mutated_mod.get_global_var('func_8952')
var_8954 = relay.var("var_8954", dtype = "int16", shape = (252,))#candidate|8954|(252,)|var|int16
var_8955 = relay.var("var_8955", dtype = "uint32", shape = (1, 40))#candidate|8955|(1, 40)|var|uint32
call_8953 = func_8952_call(var_8954,var_8955,)
output = call_8953
func_8956 = relay.Function([var_8954,var_8955,], output)
mutated_mod['func_8956'] = func_8956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_8985 = relay.TupleGetItem(func_2584_call(), 0)
call_8986 = relay.TupleGetItem(func_2585_call(), 0)
output = relay.Tuple([call_8985,])
output2 = relay.Tuple([call_8986,])
func_8994 = relay.Function([], output)
mod['func_8994'] = func_8994
mod = relay.transform.InferType()(mod)
mutated_mod['func_8994'] = func_8994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8994_call = mutated_mod.get_global_var('func_8994')
call_8995 = func_8994_call()
output = call_8995
func_8996 = relay.Function([], output)
mutated_mod['func_8996'] = func_8996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_9066 = func_3670_call()
call_9067 = func_3670_call()
func_7801_call = mod.get_global_var('func_7801')
func_7803_call = mutated_mod.get_global_var('func_7803')
call_9077 = func_7801_call()
call_9078 = func_7801_call()
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_9081 = relay.TupleGetItem(func_1055_call(), 2)
call_9082 = relay.TupleGetItem(func_1056_call(), 2)
func_4889_call = mod.get_global_var('func_4889')
func_4890_call = mutated_mod.get_global_var('func_4890')
call_9096 = relay.TupleGetItem(func_4889_call(), 0)
call_9097 = relay.TupleGetItem(func_4890_call(), 0)
func_756_call = mod.get_global_var('func_756')
func_758_call = mutated_mod.get_global_var('func_758')
call_9103 = func_756_call()
call_9104 = func_756_call()
func_1752_call = mod.get_global_var('func_1752')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_9109 = func_1752_call()
call_9110 = func_1752_call()
func_1759_call = mod.get_global_var('func_1759')
func_1761_call = mutated_mod.get_global_var('func_1761')
call_9112 = func_1759_call()
call_9113 = func_1759_call()
output = relay.Tuple([call_9066,call_9077,call_9081,call_9096,call_9103,call_9109,call_9112,])
output2 = relay.Tuple([call_9067,call_9078,call_9082,call_9097,call_9104,call_9110,call_9113,])
func_9123 = relay.Function([], output)
mod['func_9123'] = func_9123
mod = relay.transform.InferType()(mod)
mutated_mod['func_9123'] = func_9123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9123_call = mutated_mod.get_global_var('func_9123')
call_9124 = func_9123_call()
output = call_9124
func_9125 = relay.Function([], output)
mutated_mod['func_9125'] = func_9125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6376_call = mod.get_global_var('func_6376')
func_6378_call = mutated_mod.get_global_var('func_6378')
call_9138 = relay.TupleGetItem(func_6376_call(), 0)
call_9139 = relay.TupleGetItem(func_6378_call(), 0)
func_9123_call = mod.get_global_var('func_9123')
func_9125_call = mutated_mod.get_global_var('func_9125')
call_9142 = relay.TupleGetItem(func_9123_call(), 3)
call_9143 = relay.TupleGetItem(func_9125_call(), 3)
func_3419_call = mod.get_global_var('func_3419')
func_3421_call = mutated_mod.get_global_var('func_3421')
var_9158 = relay.var("var_9158", dtype = "bool", shape = (768,))#candidate|9158|(768,)|var|bool
call_9157 = relay.TupleGetItem(func_3419_call(relay.reshape(var_9158.astype('bool'), [768,])), 1)
call_9159 = relay.TupleGetItem(func_3421_call(relay.reshape(var_9158.astype('bool'), [768,])), 1)
output = relay.Tuple([call_9138,call_9142,call_9157,var_9158,])
output2 = relay.Tuple([call_9139,call_9143,call_9159,var_9158,])
func_9160 = relay.Function([var_9158,], output)
mod['func_9160'] = func_9160
mod = relay.transform.InferType()(mod)
mutated_mod['func_9160'] = func_9160
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9161 = relay.var("var_9161", dtype = "bool", shape = (768,))#candidate|9161|(768,)|var|bool
func_9160_call = mutated_mod.get_global_var('func_9160')
call_9162 = func_9160_call(var_9161)
output = call_9162
func_9163 = relay.Function([var_9161], output)
mutated_mod['func_9163'] = func_9163
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9245 = relay.const([[[7,-7,-7,10,-9,-7,-10,-9,-4],[-9,-9,-2,4,-5,8,-6,4,-6],[6,-4,-1,-1,8,6,-10,4,5],[-8,-1,-3,-8,3,-2,-5,-7,1],[-10,10,2,-3,-2,-10,2,-7,4],[1,9,-4,-3,9,-9,-9,-3,-10],[-7,-9,-9,-8,-8,3,7,4,8],[-8,8,-2,-8,-8,1,7,-3,9],[-5,3,1,7,-8,3,8,6,7],[-5,-10,-5,4,-1,8,7,6,-9],[5,-5,9,-8,9,5,3,-2,-6],[4,-1,-7,6,4,-5,8,-1,3],[-1,8,-9,6,4,5,-5,2,-5],[-6,-4,-2,5,8,-3,7,4,-1]],[[-8,-4,-5,6,1,7,-6,8,5],[-8,-10,-6,7,-4,-9,-5,4,-3],[10,10,-7,9,1,-5,7,-7,-8],[-9,-8,-8,-10,6,-4,-4,10,8],[-4,-5,4,1,1,-8,3,-6,10],[8,10,-5,-6,-1,-4,6,-5,3],[10,1,-4,-2,6,-7,-5,6,2],[-10,-10,-5,-9,2,-1,-5,1,-2],[-7,-1,4,9,5,-5,-5,-5,3],[9,10,-7,-6,-4,10,-1,2,-10],[-10,-8,-2,-1,-5,4,-6,-1,6],[-1,-10,-9,-1,-7,-10,1,-6,6],[9,9,-4,3,7,8,2,4,-4],[-4,3,10,-10,7,8,-8,-1,-5]],[[9,6,-4,7,-6,9,6,-5,-7],[-4,5,-5,-5,2,-9,2,6,1],[-6,7,-1,-4,-2,-8,5,5,5],[3,-2,-7,-3,-8,9,-1,8,-9],[-6,8,3,6,9,-7,3,4,6],[-8,-10,-10,-6,6,-8,-6,9,2],[-9,-7,2,-3,-4,2,-8,-1,-7],[-1,-1,-10,3,7,10,-1,10,7],[4,8,-7,-9,1,5,-10,-4,3],[-4,-9,-8,10,8,-1,-1,5,2],[10,-8,9,2,2,-2,9,3,7],[-7,-3,7,9,9,-7,-7,2,9],[-1,-3,-4,-9,-3,1,6,-6,-2],[-4,-1,5,4,7,7,1,5,-2]],[[1,6,-4,3,-6,10,10,-8,-7],[-10,-5,8,1,2,5,8,3,-1],[10,6,3,-3,10,-5,-2,-7,-10],[-1,-6,10,4,7,-2,6,-2,-8],[-10,9,10,-6,-9,-1,2,1,-4],[-9,-8,6,7,-4,6,-6,-2,-6],[-9,7,7,-8,-10,5,1,-2,4],[-1,-2,2,6,4,-2,-10,-3,10],[7,-7,6,-10,-7,6,-2,2,1],[-2,1,2,-6,-8,-1,7,4,-4],[-5,9,-1,-3,3,7,-1,-10,-6],[-8,7,9,4,-6,1,1,6,-10],[-5,10,-10,2,9,-6,4,-5,-1],[9,-4,4,-6,-1,-4,-1,-8,7]],[[-1,1,-8,-3,10,3,4,-7,-8],[-4,-5,-9,8,10,-3,5,-5,-2],[-1,7,-4,-3,4,-7,-10,-9,7],[-3,-7,2,9,4,2,-9,2,6],[-8,-4,-8,7,3,-2,1,7,8],[8,7,-3,7,-3,10,4,-6,-2],[-1,-2,-4,-5,10,5,-1,9,-4],[-8,6,9,-9,-6,1,-1,7,-7],[10,8,-3,-9,-5,-4,-1,-1,4],[-3,-4,9,-6,-8,-6,6,6,-3],[8,-5,10,-3,4,8,-3,-10,-9],[-2,9,-10,6,8,-1,-3,5,-3],[9,-6,7,10,4,-4,-9,7,-8],[-1,-4,-6,-2,-7,9,1,-3,3]],[[-2,9,5,10,2,9,6,-4,-1],[-9,-1,9,6,2,-1,-9,-9,1],[-6,7,-8,-9,8,-7,6,-1,2],[-9,-2,-8,-5,7,7,-10,-7,-10],[5,1,3,-4,4,5,7,-6,2],[-3,-1,5,-6,-3,-3,-10,-2,-4],[9,-3,-5,-10,-2,-3,-10,-3,7],[-1,2,10,8,-4,10,-5,-7,-9],[9,-7,6,5,-8,-7,8,-2,3],[-6,1,-1,-9,8,-7,10,-8,6],[9,-10,-2,6,6,-10,9,9,-7],[8,7,4,5,-9,-1,7,-8,8],[5,-10,1,9,8,-9,6,-1,-5],[8,-10,-5,4,2,-10,-2,4,5]],[[1,-5,-1,6,-4,-2,-3,-3,9],[-4,1,-3,-6,-7,6,-8,-7,8],[9,-7,2,-6,-2,-7,-6,-4,-7],[-9,1,-7,-1,5,-8,-7,-6,2],[6,2,8,10,2,-2,-10,-6,-10],[-7,-6,8,-5,2,9,-9,5,-4],[-5,-6,8,-8,2,7,-4,10,7],[7,3,3,-5,-5,-8,-3,3,9],[-9,10,-10,-3,3,8,3,2,-5],[8,-7,-10,1,-7,-5,8,3,7],[-4,10,8,-5,-1,9,-2,-6,9],[6,-3,8,9,-4,-1,6,5,-1],[1,-8,-5,-8,3,7,-4,-5,6],[-5,-9,-5,-1,-6,-6,1,-4,-10]],[[5,7,-4,3,-7,-4,-2,-8,-7],[-1,-6,7,5,9,-7,8,7,-10],[-10,-10,1,-10,5,6,-10,2,-6],[-8,-7,10,-6,-5,-4,5,-8,-2],[10,-4,1,7,-8,9,-8,-5,-2],[8,-3,-10,-8,2,-1,-8,8,6],[-3,3,1,-7,7,-5,-7,8,6],[9,-4,-3,-7,5,-3,7,5,-9],[-3,9,-8,-10,7,-7,5,-10,-6],[3,-4,-1,1,-4,9,7,8,4],[8,3,2,-2,-5,-8,-7,-6,-1],[-9,8,-1,5,-9,-1,2,-6,9],[-4,-7,-3,-4,5,-1,-1,-9,4],[-6,-7,3,-9,-9,10,3,7,7]],[[-6,-2,2,-7,6,10,7,8,-2],[-2,-7,-3,9,3,9,-7,10,8],[-5,-5,-3,10,10,6,10,-10,-10],[-6,-3,4,8,9,-3,1,1,8],[10,4,5,-1,-9,-5,-8,-6,9],[-4,-3,6,9,-5,-3,4,10,-3],[-7,1,-9,-5,-7,-9,2,7,8],[3,-3,8,1,9,-10,-6,9,5],[6,-7,2,3,-1,1,-4,-9,-5],[2,8,7,4,-9,5,-2,-5,-5],[-5,10,9,-7,8,-1,-2,-10,4],[10,-3,4,-2,-8,-5,3,1,6],[-5,-4,-9,-7,-8,3,2,-2,2],[-2,2,1,-1,7,-6,-6,8,-5]],[[5,-9,-6,-6,6,5,6,10,7],[7,-6,4,1,-4,-7,7,-10,8],[-9,-8,4,2,-3,10,-6,10,3],[-5,-1,3,-7,-2,9,6,-4,-4],[8,-10,10,2,9,7,3,6,10],[-2,2,-7,5,10,8,8,1,8],[10,-7,-10,-10,-8,-7,-8,9,-4],[-2,10,8,9,3,-6,3,-10,4],[7,-3,10,5,-10,9,-1,-4,-6],[-6,-10,5,9,-1,-8,-9,9,-2],[-3,-9,3,10,1,-4,8,-2,-8],[-8,4,-8,-6,-1,-8,-6,-2,-7],[-2,-9,-10,-2,3,-1,-8,10,8],[-6,4,9,-2,4,-9,1,7,-6]],[[2,-9,9,-8,9,-1,-5,-1,-8],[-2,5,-4,-8,-6,4,-3,-8,-1],[-4,-6,-6,-2,-7,3,-3,-4,2],[3,-5,-6,8,5,-4,7,-5,3],[-1,6,5,-3,-4,-9,9,8,-8],[10,6,6,-2,-9,5,10,-4,5],[-8,2,-9,10,-10,1,5,-7,-7],[-10,-5,7,1,-7,-6,6,5,7],[8,4,-6,-9,-6,-1,-9,-3,-9],[6,2,7,-10,-3,3,-10,5,-1],[9,-3,6,8,-4,2,3,-3,3],[-4,-3,7,5,6,-3,5,7,-7],[-2,10,7,-9,-10,-7,2,-6,-8],[-10,-2,5,3,7,7,-5,-8,5]],[[5,-8,-8,-7,-6,-5,8,7,4],[-5,-3,-9,6,-1,8,-10,2,9],[-4,-8,1,-5,3,-1,6,-7,10],[-9,-1,3,-6,2,2,6,10,-6],[-1,2,-3,-2,10,-5,-5,-1,5],[-4,6,7,-7,-3,10,10,8,-5],[6,9,-5,10,-9,4,2,4,-6],[-7,-5,2,8,7,5,-9,9,8],[-2,-6,7,6,-10,1,-1,-10,7],[-4,-5,2,-4,10,-9,-1,-7,4],[7,-5,-10,4,5,2,8,-8,8],[3,-5,7,-3,6,5,4,-2,8],[5,5,-6,1,-4,6,-3,4,-4],[-1,-1,-5,-7,-8,-7,-2,8,2]],[[8,-7,6,-2,2,6,-1,3,4],[-8,-8,-1,-1,-9,4,-5,9,-3],[-5,4,5,5,5,-7,5,-9,10],[-8,-4,-3,8,-1,10,-2,10,-4],[3,10,5,-6,-5,-3,-6,-7,8],[1,8,3,-5,-4,-10,-2,8,-1],[-1,5,-4,10,-9,-2,-1,-3,6],[-8,2,10,10,2,-5,-1,2,2],[-4,7,3,10,-4,-2,10,3,-4],[3,4,2,-10,6,8,-9,-2,6],[8,1,9,-4,5,-3,2,-3,-3],[6,7,-7,-1,7,-5,-1,9,4],[-5,-8,-8,1,9,6,8,-9,-5],[-8,-5,10,-8,-10,10,6,2,10]],[[-7,2,5,-9,-2,-6,5,3,-10],[9,-1,6,2,-1,-6,-8,1,10],[-8,7,-7,8,10,3,4,10,10],[-1,8,9,-2,-8,7,-9,6,6],[10,5,-7,9,-10,-7,5,-5,9],[-6,10,-3,9,-3,-9,-8,3,8],[4,1,6,-4,-7,1,-4,-6,2],[-1,-3,-8,3,1,1,-8,-7,-9],[-7,4,-4,10,4,2,7,-9,-10],[-3,10,1,-3,6,-5,5,-10,8],[5,-1,3,-7,9,-1,10,1,5],[-3,10,10,-4,1,-3,-7,-4,7],[4,-8,-9,-3,10,-9,6,5,9],[5,-2,9,-3,4,-7,-5,-7,5]],[[1,-5,1,-5,-3,-5,10,8,-4],[7,-3,7,6,-2,-4,-10,-4,5],[6,2,-4,4,9,-4,-8,2,-4],[3,10,4,2,-10,-9,-2,7,-6],[3,3,-3,6,-9,-5,7,4,1],[3,4,-10,10,-7,7,8,-5,-1],[9,2,-6,-5,-4,2,9,-1,-1],[-5,4,-8,7,-1,8,-3,-9,-8],[-1,-10,2,-4,-5,5,7,-9,-1],[-2,-2,1,6,10,8,-2,1,-5],[2,-5,4,5,9,2,10,8,-8],[-3,-2,2,10,-10,4,5,7,-4],[-1,4,-4,10,2,-5,7,-7,-4],[-1,-10,5,-8,-1,2,6,6,-3]]], dtype = "int32")#candidate|9245|(15, 14, 9)|const|int32
var_9246 = relay.var("var_9246", dtype = "int32", shape = (15, 14, 9))#candidate|9246|(15, 14, 9)|var|int32
bop_9247 = relay.not_equal(const_9245.astype('bool'), relay.reshape(var_9246.astype('bool'), relay.shape_of(const_9245))) # shape=(15, 14, 9)
const_9250 = relay.const([[[7,-1,-3,-6,-9,-4,5,6,-9],[6,-10,5,4,2,-9,9,3,2],[-6,-6,7,1,6,-1,-10,6,-4],[9,8,-3,6,-4,-9,-8,5,3],[-4,3,-2,6,3,-4,-2,-4,-8],[-9,8,-5,10,-5,-7,-8,-1,-10],[7,-8,7,5,7,-4,-6,-1,-8],[3,-10,-2,7,6,3,2,4,-8],[2,-2,5,-5,-9,-7,-3,-5,-1],[7,-9,5,-3,-9,8,5,3,10],[3,8,4,-9,8,-9,10,-4,-3],[10,7,-10,-9,5,-4,9,-4,9],[4,4,-3,8,3,2,-2,-1,-4],[-4,-7,6,-5,9,3,9,10,-9]],[[8,-6,-1,8,-3,-2,9,-1,-4],[8,-1,1,8,1,-5,1,-8,-6],[-5,2,-1,-4,-8,-7,-9,4,-3],[-6,-6,9,7,-5,-6,4,3,-9],[10,-9,8,3,-2,-9,-1,-7,2],[-8,-7,4,4,-5,5,5,9,6],[-9,-7,5,5,-3,-4,-10,5,-7],[-9,8,8,-9,-3,-5,6,-7,7],[2,-9,-4,-1,-7,-2,-5,3,-6],[-9,4,-1,-10,-6,-3,10,-5,-10],[3,-3,-8,-3,7,-8,-9,-6,-10],[5,-6,-8,2,-4,-6,5,-8,8],[-5,-2,-10,-3,-9,3,8,9,9],[-4,-3,9,5,-9,-4,2,9,-4]],[[-4,8,-8,1,1,1,-7,-10,-3],[2,-2,-10,9,8,6,8,8,3],[9,3,6,-7,-7,3,-7,-8,5],[7,-2,3,4,-9,-7,10,10,5],[7,9,10,-6,9,8,-3,-10,-10],[6,2,10,-10,7,-4,-6,-4,-7],[-6,-3,-8,-9,-8,8,1,3,1],[-5,4,3,-4,-10,-1,-3,9,-4],[-1,-8,1,6,-1,-7,2,5,6],[3,4,-6,-10,4,9,6,10,-6],[9,-4,2,-5,5,-10,8,9,-9],[-9,-8,-8,-2,4,6,6,3,-8],[-3,-1,4,1,5,6,-7,-2,-1],[-1,-3,-6,6,-6,1,-5,-8,-5]],[[8,-4,8,-8,6,-1,10,-1,-6],[4,8,10,-4,4,-1,-4,-6,5],[-8,-10,-3,-3,-10,8,9,7,-9],[-7,-2,-5,-3,-6,-7,3,-4,-2],[-4,1,-9,-2,-8,8,-4,10,-7],[10,4,-8,-7,-8,6,7,7,5],[-7,-6,4,4,-10,-7,-1,-8,-5],[8,9,-2,-6,-6,8,-8,-6,2],[8,-9,2,7,5,10,4,-1,-4],[10,3,-2,5,8,4,-3,-7,3],[10,-1,-7,-4,-9,-4,7,2,7],[-1,-3,6,-8,-2,-5,4,-6,10],[-6,-4,9,-7,-1,-6,-4,-3,-5],[-6,1,-10,4,-2,9,-6,8,1]],[[10,-6,8,9,1,8,-4,3,-2],[-2,8,-7,-5,3,4,3,-3,-5],[4,-4,-10,3,7,-9,-10,7,4],[3,8,-5,2,-6,-10,8,7,-7],[6,-10,7,-4,-10,-2,-7,-6,-3],[-7,10,9,-6,-3,3,-9,1,4],[9,-2,-10,-5,-9,10,-1,-6,2],[-2,6,-1,-5,-6,2,-2,-9,-3],[-1,4,9,-4,10,-5,7,1,1],[10,6,2,-7,10,1,5,-2,-1],[-2,3,-5,6,-6,-5,3,-2,-5],[-5,-1,8,-8,5,3,-3,1,7],[-6,9,-2,-8,-10,-3,9,7,5],[-1,2,5,1,8,-5,9,-2,3]],[[3,-10,-4,-9,-1,2,-6,8,-10],[-1,10,5,6,7,2,-1,-1,-9],[-4,-9,-7,-8,5,-8,1,-6,-9],[-8,-4,-3,7,3,-7,-7,1,5],[-7,10,10,-7,-7,4,1,-3,1],[1,-3,7,7,10,-10,-9,-9,10],[-6,2,9,1,10,-7,1,-8,-4],[-4,-9,-2,-1,-5,-9,8,2,-1],[6,1,8,-8,5,5,4,-10,-6],[-1,3,-7,-3,-8,-7,-5,2,2],[3,-1,7,-8,7,-4,-2,2,-5],[6,4,-2,-2,5,-3,4,-6,-4],[2,5,-2,2,8,-9,-3,-8,8],[9,8,-2,10,9,-2,10,-7,-1]],[[8,4,9,6,6,-8,-5,-4,2],[6,-5,-9,-9,9,6,6,-5,-7],[-2,6,-8,-4,-3,9,-8,7,-9],[-8,-5,-4,-9,4,-9,-8,-7,-10],[-1,9,-5,-1,-3,-4,-5,1,-1],[1,-7,4,8,-6,-8,-10,-3,5],[9,-8,-4,-7,7,9,4,6,6],[7,3,9,-4,-10,-1,-2,3,-5],[4,-6,-9,-9,-4,6,6,-4,-9],[-10,-5,7,-9,6,-10,-9,-2,-7],[7,-6,4,2,5,9,-8,-6,-1],[-9,-3,10,-6,10,-3,9,-5,-2],[-6,9,10,-5,6,1,4,8,5],[-1,-7,10,-9,2,3,3,8,-3]],[[9,-7,9,2,10,-1,8,-9,-4],[-6,8,-7,10,2,-1,6,-3,4],[-5,-5,8,1,1,-2,-6,8,-4],[7,-6,-4,4,-6,5,10,8,-4],[-3,-2,-4,9,-1,-6,-3,-1,-1],[-5,-4,-3,3,-10,1,7,2,10],[4,-8,8,9,8,-10,4,-6,-8],[-1,4,-2,-7,9,-10,5,-8,-8],[8,8,7,5,-5,2,-1,6,4],[2,-9,-3,2,3,-3,-6,10,9],[6,-1,-8,-6,-5,6,-2,-5,1],[-2,-7,1,-7,5,5,-7,9,-1],[2,-5,2,8,-10,-7,-2,2,-7],[1,3,3,9,6,7,-4,5,-8]],[[3,-10,-1,-5,-7,2,1,-8,-1],[-2,-3,10,-6,-1,-6,-7,-4,-3],[6,-8,5,9,-5,-10,-9,7,-1],[-2,-3,-7,9,-9,4,10,10,-5],[9,-2,-2,-1,7,1,-8,4,-5],[10,6,8,3,-2,-5,-7,2,9],[4,-2,-1,-6,7,10,-10,7,2],[-7,-5,-8,-5,-5,6,10,-7,8],[7,-8,-5,-6,1,-4,1,7,-10],[6,-2,4,-8,-8,7,4,-2,-6],[-1,4,8,-4,-9,4,-6,5,-3],[5,-1,4,-1,-2,3,9,-2,5],[-1,10,-9,-9,5,2,3,7,10],[-4,2,-3,-5,10,-5,9,3,8]],[[-4,-7,-9,6,6,-7,-7,-7,-6],[5,-3,1,9,6,9,-3,8,-1],[9,-10,1,9,-10,-6,-7,8,-7],[9,-8,5,8,-10,8,-7,7,1],[-7,-5,-9,3,-3,7,1,3,1],[-9,-7,-7,-8,-3,-2,-4,-5,5],[-9,1,1,-1,1,2,-3,-1,9],[9,-2,6,-7,2,9,-7,8,-2],[3,1,-7,-8,-5,-5,8,-4,8],[-4,-8,8,-8,8,2,-4,1,-3],[-10,3,1,-10,3,9,3,8,-2],[1,-3,3,-6,4,-2,-10,-7,8],[2,-5,3,8,-7,-7,5,8,-4],[-7,2,10,8,6,4,3,3,4]],[[-4,-2,-3,2,7,-7,-5,-3,-6],[10,-4,1,-2,7,4,3,-6,-9],[-4,-6,-2,-1,-9,-3,9,1,10],[3,-6,-9,-4,8,-9,-8,1,5],[-8,2,3,2,-9,-5,-3,-2,1],[-1,6,-4,8,2,-7,-5,-5,10],[-2,-2,-5,9,7,1,5,-4,1],[7,-9,1,8,-9,-2,-3,-5,-5],[-3,-10,-6,-10,-3,1,2,7,9],[-7,5,9,9,2,-6,4,-9,-10],[7,5,4,-6,-4,-8,-3,7,3],[5,-8,5,2,-3,-6,-8,-3,-3],[-7,-5,-5,3,10,-6,-5,-4,-6],[9,8,2,5,7,3,6,2,-2]],[[-6,5,-4,-8,9,-6,-3,-6,-6],[-5,6,-10,-3,-8,10,9,4,2],[4,9,-4,-10,-9,-9,5,-6,5],[10,2,2,8,6,5,2,-9,-3],[-7,1,-1,10,6,7,-2,9,4],[6,5,6,1,9,10,-5,9,2],[6,-6,-8,4,-7,-1,-6,-5,-8],[-1,10,9,6,-6,9,4,9,-8],[10,-4,8,-10,-4,-5,5,-3,8],[4,5,-8,7,2,2,3,-3,-1],[-4,-5,-5,3,8,6,8,-1,-9],[1,-1,-1,4,-6,-3,-10,-9,7],[7,7,-8,3,-10,-10,3,4,4],[-6,-9,7,-1,-1,4,-6,10,8]],[[4,-3,-6,-3,6,-3,-3,9,1],[-4,-5,-3,-4,9,2,-1,7,-1],[9,-1,1,5,3,4,2,-8,-4],[3,10,2,-9,8,-9,10,3,10],[7,6,9,-8,9,-9,7,-2,4],[-10,-9,1,-7,5,-4,4,10,1],[-1,2,5,6,3,-10,2,-2,-10],[10,-3,1,-9,9,6,-1,-1,8],[6,9,-2,10,10,-6,6,2,-2],[-9,8,2,-9,1,-10,5,5,-7],[2,-2,1,5,-5,-9,7,-7,7],[9,2,4,-10,-8,-3,-1,-4,7],[10,-7,8,1,-5,10,-8,5,-8],[-2,10,-3,-8,-5,-9,10,-4,-6]],[[2,-8,6,6,-7,-3,-2,3,-8],[-2,-5,9,-1,3,5,-10,7,-3],[-5,6,-1,-7,6,4,10,-10,-5],[7,7,3,-9,8,-10,8,9,-7],[3,-3,6,2,-5,1,1,-6,-9],[-8,-4,6,-5,-7,-8,-7,8,1],[7,-2,-8,-2,2,-5,1,-1,10],[-6,2,1,10,3,8,-2,9,-9],[6,6,-3,8,4,6,-7,-1,8],[10,-2,5,-9,6,10,5,-1,3],[1,6,1,1,6,6,6,1,-9],[7,-5,5,2,-3,-2,7,-10,-1],[6,-8,6,6,9,9,6,-3,-10],[-8,10,-3,10,6,-2,-2,10,3]],[[-3,7,8,10,-1,7,-5,2,-6],[8,7,-7,-2,1,8,-8,-1,-5],[-1,5,1,-1,-8,-2,2,-2,3],[-9,-8,-6,4,-9,9,6,-10,9],[-4,8,5,-8,-9,7,-10,4,9],[-6,4,-8,1,10,-6,5,-3,-3],[4,-7,-2,4,1,1,9,-10,3],[5,-1,-7,8,-6,6,9,-1,-2],[1,6,-5,-3,-4,-9,-3,3,1],[-1,-2,10,-8,-8,5,3,-8,-9],[4,9,-5,7,3,1,7,-3,-1],[-7,-1,-10,-4,4,10,7,5,5],[4,-7,-1,-9,2,-7,6,-2,8],[-3,4,6,-3,1,-9,-8,-6,10]]], dtype = "int32")#candidate|9250|(15, 14, 9)|const|int32
bop_9251 = relay.logical_and(const_9245.astype('bool'), relay.reshape(const_9250.astype('bool'), relay.shape_of(const_9245))) # shape=(15, 14, 9)
output = relay.Tuple([bop_9247,bop_9251,])
output2 = relay.Tuple([bop_9247,bop_9251,])
func_9266 = relay.Function([var_9246,], output)
mod['func_9266'] = func_9266
mod = relay.transform.InferType()(mod)
var_9267 = relay.var("var_9267", dtype = "int32", shape = (15, 14, 9))#candidate|9267|(15, 14, 9)|var|int32
output = func_9266(var_9267)
func_9268 = relay.Function([var_9267], output)
mutated_mod['func_9268'] = func_9268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_9285 = relay.TupleGetItem(func_1055_call(), 0)
call_9286 = relay.TupleGetItem(func_1056_call(), 0)
func_5886_call = mod.get_global_var('func_5886')
func_5888_call = mutated_mod.get_global_var('func_5888')
call_9288 = relay.TupleGetItem(func_5886_call(), 0)
call_9289 = relay.TupleGetItem(func_5888_call(), 0)
output = relay.Tuple([call_9285,call_9288,])
output2 = relay.Tuple([call_9286,call_9289,])
func_9292 = relay.Function([], output)
mod['func_9292'] = func_9292
mod = relay.transform.InferType()(mod)
mutated_mod['func_9292'] = func_9292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9292_call = mutated_mod.get_global_var('func_9292')
call_9293 = func_9292_call()
output = call_9293
func_9294 = relay.Function([], output)
mutated_mod['func_9294'] = func_9294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9323 = relay.var("var_9323", dtype = "float64", shape = (4, 15, 14))#candidate|9323|(4, 15, 14)|var|float64
var_9324 = relay.var("var_9324", dtype = "float64", shape = (4, 15, 14))#candidate|9324|(4, 15, 14)|var|float64
bop_9325 = relay.mod(var_9323.astype('float64'), relay.reshape(var_9324.astype('float64'), relay.shape_of(var_9323))) # shape=(4, 15, 14)
uop_9330 = relay.erf(var_9324.astype('float32')) # shape=(4, 15, 14)
output = relay.Tuple([bop_9325,uop_9330,])
output2 = relay.Tuple([bop_9325,uop_9330,])
func_9338 = relay.Function([var_9323,var_9324,], output)
mod['func_9338'] = func_9338
mod = relay.transform.InferType()(mod)
mutated_mod['func_9338'] = func_9338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9338_call = mutated_mod.get_global_var('func_9338')
var_9340 = relay.var("var_9340", dtype = "float64", shape = (4, 15, 14))#candidate|9340|(4, 15, 14)|var|float64
var_9341 = relay.var("var_9341", dtype = "float64", shape = (4, 15, 14))#candidate|9341|(4, 15, 14)|var|float64
call_9339 = func_9338_call(var_9340,var_9341,)
output = call_9339
func_9342 = relay.Function([var_9340,var_9341,], output)
mutated_mod['func_9342'] = func_9342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7467_call = mod.get_global_var('func_7467')
func_7468_call = mutated_mod.get_global_var('func_7468')
call_9367 = func_7467_call()
call_9368 = func_7467_call()
output = call_9367
output2 = call_9368
func_9369 = relay.Function([], output)
mod['func_9369'] = func_9369
mod = relay.transform.InferType()(mod)
mutated_mod['func_9369'] = func_9369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9369_call = mutated_mod.get_global_var('func_9369')
call_9370 = func_9369_call()
output = call_9370
func_9371 = relay.Function([], output)
mutated_mod['func_9371'] = func_9371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1949_call = mod.get_global_var('func_1949')
func_1950_call = mutated_mod.get_global_var('func_1950')
call_9391 = relay.TupleGetItem(func_1949_call(), 0)
call_9392 = relay.TupleGetItem(func_1950_call(), 0)
func_8994_call = mod.get_global_var('func_8994')
func_8996_call = mutated_mod.get_global_var('func_8996')
call_9433 = relay.TupleGetItem(func_8994_call(), 0)
call_9434 = relay.TupleGetItem(func_8996_call(), 0)
output = relay.Tuple([call_9391,call_9433,])
output2 = relay.Tuple([call_9392,call_9434,])
func_9436 = relay.Function([], output)
mod['func_9436'] = func_9436
mod = relay.transform.InferType()(mod)
mutated_mod['func_9436'] = func_9436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9436_call = mutated_mod.get_global_var('func_9436')
call_9437 = func_9436_call()
output = call_9437
func_9438 = relay.Function([], output)
mutated_mod['func_9438'] = func_9438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_9448 = func_3670_call()
call_9449 = func_3670_call()
output = relay.Tuple([call_9448,])
output2 = relay.Tuple([call_9449,])
func_9459 = relay.Function([], output)
mod['func_9459'] = func_9459
mod = relay.transform.InferType()(mod)
output = func_9459()
func_9460 = relay.Function([], output)
mutated_mod['func_9460'] = func_9460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2061_call = mod.get_global_var('func_2061')
func_2062_call = mutated_mod.get_global_var('func_2062')
call_9466 = relay.TupleGetItem(func_2061_call(), 0)
call_9467 = relay.TupleGetItem(func_2062_call(), 0)
output = call_9466
output2 = call_9467
func_9482 = relay.Function([], output)
mod['func_9482'] = func_9482
mod = relay.transform.InferType()(mod)
mutated_mod['func_9482'] = func_9482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9482_call = mutated_mod.get_global_var('func_9482')
call_9483 = func_9482_call()
output = call_9483
func_9484 = relay.Function([], output)
mutated_mod['func_9484'] = func_9484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7538_call = mod.get_global_var('func_7538')
func_7539_call = mutated_mod.get_global_var('func_7539')
call_9503 = func_7538_call()
call_9504 = func_7538_call()
output = call_9503
output2 = call_9504
func_9510 = relay.Function([], output)
mod['func_9510'] = func_9510
mod = relay.transform.InferType()(mod)
mutated_mod['func_9510'] = func_9510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9510_call = mutated_mod.get_global_var('func_9510')
call_9511 = func_9510_call()
output = call_9511
func_9512 = relay.Function([], output)
mutated_mod['func_9512'] = func_9512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4123_call = mod.get_global_var('func_4123')
func_4124_call = mutated_mod.get_global_var('func_4124')
call_9588 = func_4123_call()
call_9589 = func_4123_call()
func_8089_call = mod.get_global_var('func_8089')
func_8092_call = mutated_mod.get_global_var('func_8092')
const_9591 = relay.const([False,False,False,False,False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,True], dtype = "bool")#candidate|9591|(605,)|const|bool
call_9590 = relay.TupleGetItem(func_8089_call(relay.reshape(const_9591.astype('bool'), [5, 11, 11]), relay.reshape(const_9591.astype('bool'), [5, 11, 11]), ), 0)
call_9592 = relay.TupleGetItem(func_8092_call(relay.reshape(const_9591.astype('bool'), [5, 11, 11]), relay.reshape(const_9591.astype('bool'), [5, 11, 11]), ), 0)
bop_9597 = relay.greater_equal(call_9590.astype('bool'), relay.reshape(const_9591.astype('bool'), relay.shape_of(call_9590))) # shape=(5, 11, 11)
bop_9600 = relay.greater_equal(call_9592.astype('bool'), relay.reshape(const_9591.astype('bool'), relay.shape_of(call_9592))) # shape=(5, 11, 11)
func_6296_call = mod.get_global_var('func_6296')
func_6297_call = mutated_mod.get_global_var('func_6297')
call_9602 = relay.TupleGetItem(func_6296_call(), 2)
call_9603 = relay.TupleGetItem(func_6297_call(), 2)
output = relay.Tuple([call_9588,bop_9597,call_9602,])
output2 = relay.Tuple([call_9589,bop_9600,call_9603,])
func_9633 = relay.Function([], output)
mod['func_9633'] = func_9633
mod = relay.transform.InferType()(mod)
output = func_9633()
func_9634 = relay.Function([], output)
mutated_mod['func_9634'] = func_9634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5660_call = mod.get_global_var('func_5660')
func_5662_call = mutated_mod.get_global_var('func_5662')
call_9635 = func_5660_call()
call_9636 = func_5660_call()
func_4849_call = mod.get_global_var('func_4849')
func_4852_call = mutated_mod.get_global_var('func_4852')
call_9649 = func_4849_call(relay.reshape(call_9635.astype('bool'), [13, 10, 3]))
call_9650 = func_4849_call(relay.reshape(call_9635.astype('bool'), [13, 10, 3]))
func_9160_call = mod.get_global_var('func_9160')
func_9163_call = mutated_mod.get_global_var('func_9163')
var_9653 = relay.var("var_9653", dtype = "bool", shape = (768,))#candidate|9653|(768,)|var|bool
call_9652 = relay.TupleGetItem(func_9160_call(relay.reshape(var_9653.astype('bool'), [768,])), 0)
call_9654 = relay.TupleGetItem(func_9163_call(relay.reshape(var_9653.astype('bool'), [768,])), 0)
output = relay.Tuple([call_9635,call_9649,call_9652,var_9653,])
output2 = relay.Tuple([call_9636,call_9650,call_9654,var_9653,])
func_9655 = relay.Function([var_9653,], output)
mod['func_9655'] = func_9655
mod = relay.transform.InferType()(mod)
mutated_mod['func_9655'] = func_9655
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9656 = relay.var("var_9656", dtype = "bool", shape = (768,))#candidate|9656|(768,)|var|bool
func_9655_call = mutated_mod.get_global_var('func_9655')
call_9657 = func_9655_call(var_9656)
output = call_9657
func_9658 = relay.Function([var_9656], output)
mutated_mod['func_9658'] = func_9658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_9660 = relay.TupleGetItem(func_1055_call(), 0)
call_9661 = relay.TupleGetItem(func_1056_call(), 0)
func_6296_call = mod.get_global_var('func_6296')
func_6297_call = mutated_mod.get_global_var('func_6297')
call_9668 = relay.TupleGetItem(func_6296_call(), 2)
call_9669 = relay.TupleGetItem(func_6297_call(), 2)
func_1574_call = mod.get_global_var('func_1574')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_9674 = relay.TupleGetItem(func_1574_call(), 0)
call_9675 = relay.TupleGetItem(func_1576_call(), 0)
func_756_call = mod.get_global_var('func_756')
func_758_call = mutated_mod.get_global_var('func_758')
call_9682 = func_756_call()
call_9683 = func_756_call()
output = relay.Tuple([call_9660,call_9668,call_9674,call_9682,])
output2 = relay.Tuple([call_9661,call_9669,call_9675,call_9683,])
func_9691 = relay.Function([], output)
mod['func_9691'] = func_9691
mod = relay.transform.InferType()(mod)
output = func_9691()
func_9692 = relay.Function([], output)
mutated_mod['func_9692'] = func_9692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7467_call = mod.get_global_var('func_7467')
func_7468_call = mutated_mod.get_global_var('func_7468')
call_9749 = func_7467_call()
call_9750 = func_7467_call()
output = call_9749
output2 = call_9750
func_9757 = relay.Function([], output)
mod['func_9757'] = func_9757
mod = relay.transform.InferType()(mod)
mutated_mod['func_9757'] = func_9757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9757_call = mutated_mod.get_global_var('func_9757')
call_9758 = func_9757_call()
output = call_9758
func_9759 = relay.Function([], output)
mutated_mod['func_9759'] = func_9759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3204_call = mod.get_global_var('func_3204')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_9780 = func_3204_call()
call_9781 = func_3204_call()
output = call_9780
output2 = call_9781
func_9795 = relay.Function([], output)
mod['func_9795'] = func_9795
mod = relay.transform.InferType()(mod)
output = func_9795()
func_9796 = relay.Function([], output)
mutated_mod['func_9796'] = func_9796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4103_call = mod.get_global_var('func_4103')
func_4104_call = mutated_mod.get_global_var('func_4104')
call_9802 = relay.TupleGetItem(func_4103_call(), 0)
call_9803 = relay.TupleGetItem(func_4104_call(), 0)
func_1076_call = mod.get_global_var('func_1076')
func_1080_call = mutated_mod.get_global_var('func_1080')
const_9808 = relay.const(8, dtype = "uint16")#candidate|9808|()|const|uint16
var_9809 = relay.var("var_9809", dtype = "uint16", shape = (154,))#candidate|9809|(154,)|var|uint16
call_9807 = relay.TupleGetItem(func_1076_call(relay.reshape(const_9808.astype('uint16'), []), relay.reshape(var_9809.astype('uint16'), [11, 1, 14]), ), 0)
call_9810 = relay.TupleGetItem(func_1080_call(relay.reshape(const_9808.astype('uint16'), []), relay.reshape(var_9809.astype('uint16'), [11, 1, 14]), ), 0)
func_9160_call = mod.get_global_var('func_9160')
func_9163_call = mutated_mod.get_global_var('func_9163')
const_9818 = relay.const([True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False], dtype = "bool")#candidate|9818|(768,)|const|bool
call_9817 = relay.TupleGetItem(func_9160_call(relay.reshape(const_9818.astype('bool'), [768,])), 2)
call_9819 = relay.TupleGetItem(func_9163_call(relay.reshape(const_9818.astype('bool'), [768,])), 2)
func_5319_call = mod.get_global_var('func_5319')
func_5322_call = mutated_mod.get_global_var('func_5322')
call_9822 = relay.TupleGetItem(func_5319_call(relay.reshape(const_9808.astype('float64'), [])), 1)
call_9823 = relay.TupleGetItem(func_5322_call(relay.reshape(const_9808.astype('float64'), [])), 1)
bop_9835 = relay.less_equal(const_9818.astype('bool'), relay.reshape(call_9817.astype('bool'), relay.shape_of(const_9818))) # shape=(768,)
bop_9838 = relay.less_equal(const_9818.astype('bool'), relay.reshape(call_9819.astype('bool'), relay.shape_of(const_9818))) # shape=(768,)
func_4054_call = mod.get_global_var('func_4054')
func_4057_call = mutated_mod.get_global_var('func_4057')
const_9840 = relay.const([-7.071043,7.940512,-2.175927,-2.735581,2.809561,-8.096951,7.448719,-1.788350,-1.675240,-2.946126,4.694088,-0.914026,-5.865919,-1.462026,5.013067,-0.012593,-0.009513,3.778000,-4.587776,4.055403,0.468405,7.057090,0.970615,-6.993017,8.859364,-6.310350,-8.209054,9.419628,-3.195343,-1.293480,7.532457,8.883463,4.585873,-9.907898,7.555831,6.158543,8.452001,1.601359,4.212500,-6.238875,5.139154,6.275595,1.855397,-8.982138,-5.894120,3.049233,-7.023689,9.404146,9.645152,4.768861,-8.371423,-1.239315,-7.409571,-2.340052,4.400002,-9.622696,9.027762,-7.857286,-5.212634,-3.863098,-0.522209,-5.060798,2.580795,-1.352148,4.625378,0.598853,-4.688239,-2.099681,5.213889,-3.236670,2.111742,7.473134,0.574244,-0.359348,9.881711,-2.022014,-5.662003,-7.914134,8.253656,5.167869,-6.399025,-6.644597,-2.533733,2.275340,1.241236,-1.940880,-8.143308,7.604355,-0.717294,9.850468,5.878451,9.374708,-3.880240,2.889048,-8.513028,9.714444,6.337732,0.450028,-4.187012,6.902228,4.095933,-8.026002,-5.245960,3.173016,8.928926,-4.631153,-5.476658,3.109418,5.637959,-9.453832,8.412696,-0.496137,5.385893,-0.103603,0.486512,1.248037,3.440397,-4.929586,-5.315127,-2.962898,8.673853,-1.929141,-9.122816,-7.415382,-3.253355,6.627545,-1.302759,-2.234746,-4.419939,5.964659,-6.346061,-1.011853,5.516668,6.903359,-3.162850,5.434476,-0.436004,6.953008,2.640167,-1.894447,4.015585,2.771380,-7.101711,5.615735,-5.243115,-8.873832,-9.726304,6.434790,4.117799,5.115462,-0.972537,1.019596,-7.157613,-8.650589,3.715570,2.655634,-1.646724,-4.082179,-8.277935,1.822414,9.833524,4.868403,-2.551591,5.159605,-5.863358,2.190329,9.250653,8.358858,-3.409084,-3.281260,9.451318,-7.416100,-2.201610,-2.174967,-7.401492,-5.102325,4.768511,3.265986,-2.870982,2.408525,1.120205,9.128746,-4.007437,-8.234766,-7.730104,-7.221893,-3.054631,-2.532316,0.368510,5.404190,-7.347100,3.995013,-7.666789,-2.868318,3.224838,7.423155,-6.596713,-4.182504,2.776367,8.496570,5.758144,4.046275,-6.506175,-7.372240,-2.540251,-2.679478,5.854437,-0.784331,-6.810218,-3.755021,3.843988,5.835781,3.658446,-1.187727,-4.062035,-4.645742,5.201991,-5.037447,5.558533,4.158434,-4.075699,1.381481,-3.427472,3.049704,-5.657994,-9.531556,3.913379,5.098204,5.689916,-1.294897,-5.524848,8.596261,-6.808066,5.133144,3.513058,-7.868519,-7.787817,3.170560,7.263777,-0.359659], dtype = "float64")#candidate|9840|(240,)|const|float64
call_9839 = relay.TupleGetItem(func_4054_call(relay.reshape(const_9808.astype('float64'), []), relay.reshape(const_9840.astype('float64'), [240,]), ), 2)
call_9841 = relay.TupleGetItem(func_4057_call(relay.reshape(const_9808.astype('float64'), []), relay.reshape(const_9840.astype('float64'), [240,]), ), 2)
output = relay.Tuple([call_9802,call_9807,const_9808,var_9809,call_9822,bop_9835,call_9839,const_9840,])
output2 = relay.Tuple([call_9803,call_9810,const_9808,var_9809,call_9823,bop_9838,call_9841,const_9840,])
func_9849 = relay.Function([var_9809,], output)
mod['func_9849'] = func_9849
mod = relay.transform.InferType()(mod)
mutated_mod['func_9849'] = func_9849
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9850 = relay.var("var_9850", dtype = "uint16", shape = (154,))#candidate|9850|(154,)|var|uint16
func_9849_call = mutated_mod.get_global_var('func_9849')
call_9851 = func_9849_call(var_9850)
output = call_9851
func_9852 = relay.Function([var_9850], output)
mutated_mod['func_9852'] = func_9852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5660_call = mod.get_global_var('func_5660')
func_5662_call = mutated_mod.get_global_var('func_5662')
call_9970 = func_5660_call()
call_9971 = func_5660_call()
output = relay.Tuple([call_9970,])
output2 = relay.Tuple([call_9971,])
func_9975 = relay.Function([], output)
mod['func_9975'] = func_9975
mod = relay.transform.InferType()(mod)
mutated_mod['func_9975'] = func_9975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9975_call = mutated_mod.get_global_var('func_9975')
call_9976 = func_9975_call()
output = call_9976
func_9977 = relay.Function([], output)
mutated_mod['func_9977'] = func_9977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3082_call = mod.get_global_var('func_3082')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_9985 = func_3082_call()
call_9986 = func_3082_call()
output = call_9985
output2 = call_9986
func_9987 = relay.Function([], output)
mod['func_9987'] = func_9987
mod = relay.transform.InferType()(mod)
output = func_9987()
func_9988 = relay.Function([], output)
mutated_mod['func_9988'] = func_9988
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9998 = relay.const([[[-4,-6,-6,-5],[8,5,-7,1],[3,-4,-8,-1],[-1,7,-6,-5],[5,-5,-10,4]],[[-10,-7,3,2],[8,6,6,-4],[-10,2,1,10],[1,-1,-8,1],[3,5,-10,3]],[[-1,-5,-8,8],[9,8,9,9],[3,-3,2,-9],[3,-2,-10,-2],[-4,2,5,4]],[[1,-7,-9,-10],[-4,-3,6,3],[7,2,-10,8],[1,-8,1,-2],[5,3,-4,4]],[[6,6,1,-1],[5,-6,8,-1],[-6,-5,2,-9],[7,-8,-3,-2],[-4,-10,8,-3]],[[-3,-7,3,-9],[-8,5,-4,-6],[-6,-5,-9,-7],[5,-7,-7,7],[-9,4,-4,-10]],[[9,-2,-10,7],[3,5,9,4],[-1,7,3,-1],[-8,-4,-8,-5],[-10,10,-3,7]],[[9,9,-6,-1],[6,-5,4,1],[1,-6,-8,3],[-8,-9,2,-9],[10,8,-3,-2]],[[-1,-7,-5,8],[-4,2,-5,-3],[10,6,-9,-2],[2,-4,-2,-3],[-7,7,1,-7]],[[-10,-8,-6,8],[4,-7,-8,2],[2,7,4,5],[2,-3,-7,-7],[-9,-2,9,-10]],[[-3,-4,9,-2],[-3,5,9,-1],[3,-4,-4,7],[-10,-8,-8,-10],[5,-3,3,5]],[[6,-5,9,-8],[10,3,6,7],[9,-5,-4,-2],[-2,-5,-2,-10],[10,5,-3,-2]],[[-8,-7,4,-10],[-1,-2,1,-6],[-8,-9,1,1],[7,9,-3,-3],[5,-3,5,-2]]], dtype = "int32")#candidate|9998|(13, 5, 4)|const|int32
var_9999 = relay.var("var_9999", dtype = "int32", shape = (13, 5, 4))#candidate|9999|(13, 5, 4)|var|int32
bop_10000 = relay.bitwise_xor(const_9998.astype('int32'), relay.reshape(var_9999.astype('int32'), relay.shape_of(const_9998))) # shape=(13, 5, 4)
func_4473_call = mod.get_global_var('func_4473')
func_4474_call = mutated_mod.get_global_var('func_4474')
call_10005 = relay.TupleGetItem(func_4473_call(), 0)
call_10006 = relay.TupleGetItem(func_4474_call(), 0)
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_10007 = func_490_call()
call_10008 = func_490_call()
func_5239_call = mod.get_global_var('func_5239')
func_5240_call = mutated_mod.get_global_var('func_5240')
call_10010 = relay.TupleGetItem(func_5239_call(), 0)
call_10011 = relay.TupleGetItem(func_5240_call(), 0)
func_4647_call = mod.get_global_var('func_4647')
func_4649_call = mutated_mod.get_global_var('func_4649')
call_10033 = func_4647_call()
call_10034 = func_4647_call()
var_10047 = relay.var("var_10047", dtype = "int32", shape = (13, 5, 4))#candidate|10047|(13, 5, 4)|var|int32
bop_10048 = relay.maximum(var_9999.astype('int32'), relay.reshape(var_10047.astype('int32'), relay.shape_of(var_9999))) # shape=(13, 5, 4)
output = relay.Tuple([bop_10000,call_10005,call_10007,call_10010,call_10033,bop_10048,])
output2 = relay.Tuple([bop_10000,call_10006,call_10008,call_10011,call_10034,bop_10048,])
func_10062 = relay.Function([var_9999,var_10047,], output)
mod['func_10062'] = func_10062
mod = relay.transform.InferType()(mod)
mutated_mod['func_10062'] = func_10062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10062_call = mutated_mod.get_global_var('func_10062')
var_10064 = relay.var("var_10064", dtype = "int32", shape = (13, 5, 4))#candidate|10064|(13, 5, 4)|var|int32
var_10065 = relay.var("var_10065", dtype = "int32", shape = (13, 5, 4))#candidate|10065|(13, 5, 4)|var|int32
call_10063 = func_10062_call(var_10064,var_10065,)
output = call_10063
func_10066 = relay.Function([var_10064,var_10065,], output)
mutated_mod['func_10066'] = func_10066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mod.get_global_var('func_1759')
func_1761_call = mutated_mod.get_global_var('func_1761')
call_10074 = func_1759_call()
call_10075 = func_1759_call()
output = relay.Tuple([call_10074,])
output2 = relay.Tuple([call_10075,])
func_10092 = relay.Function([], output)
mod['func_10092'] = func_10092
mod = relay.transform.InferType()(mod)
mutated_mod['func_10092'] = func_10092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10092_call = mutated_mod.get_global_var('func_10092')
call_10093 = func_10092_call()
output = call_10093
func_10094 = relay.Function([], output)
mutated_mod['func_10094'] = func_10094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10125 = relay.var("var_10125", dtype = "bool", shape = (8, 1, 15))#candidate|10125|(8, 1, 15)|var|bool
var_10126 = relay.var("var_10126", dtype = "bool", shape = (8, 9, 15))#candidate|10126|(8, 9, 15)|var|bool
bop_10127 = relay.logical_or(var_10125.astype('bool'), var_10126.astype('bool')) # shape=(8, 9, 15)
func_1232_call = mod.get_global_var('func_1232')
func_1233_call = mutated_mod.get_global_var('func_1233')
call_10130 = relay.TupleGetItem(func_1232_call(), 0)
call_10131 = relay.TupleGetItem(func_1233_call(), 0)
func_9459_call = mod.get_global_var('func_9459')
func_9460_call = mutated_mod.get_global_var('func_9460')
call_10148 = relay.TupleGetItem(func_9459_call(), 0)
call_10149 = relay.TupleGetItem(func_9460_call(), 0)
func_3733_call = mod.get_global_var('func_3733')
func_3737_call = mutated_mod.get_global_var('func_3737')
var_10151 = relay.var("var_10151", dtype = "float64", shape = ())#candidate|10151|()|var|float64
var_10152 = relay.var("var_10152", dtype = "float64", shape = (240,))#candidate|10152|(240,)|var|float64
call_10150 = relay.TupleGetItem(func_3733_call(relay.reshape(var_10151.astype('float64'), []), relay.reshape(var_10152.astype('float64'), [15, 8, 2]), ), 1)
call_10153 = relay.TupleGetItem(func_3737_call(relay.reshape(var_10151.astype('float64'), []), relay.reshape(var_10152.astype('float64'), [15, 8, 2]), ), 1)
func_6514_call = mod.get_global_var('func_6514')
func_6516_call = mutated_mod.get_global_var('func_6516')
call_10161 = relay.TupleGetItem(func_6514_call(relay.reshape(var_10151.astype('float64'), [])), 1)
call_10162 = relay.TupleGetItem(func_6516_call(relay.reshape(var_10151.astype('float64'), [])), 1)
output = relay.Tuple([bop_10127,call_10130,call_10148,call_10150,var_10151,var_10152,call_10161,])
output2 = relay.Tuple([bop_10127,call_10131,call_10149,call_10153,var_10151,var_10152,call_10162,])
func_10184 = relay.Function([var_10125,var_10126,var_10151,var_10152,], output)
mod['func_10184'] = func_10184
mod = relay.transform.InferType()(mod)
var_10185 = relay.var("var_10185", dtype = "bool", shape = (8, 1, 15))#candidate|10185|(8, 1, 15)|var|bool
var_10186 = relay.var("var_10186", dtype = "bool", shape = (8, 9, 15))#candidate|10186|(8, 9, 15)|var|bool
var_10187 = relay.var("var_10187", dtype = "float64", shape = ())#candidate|10187|()|var|float64
var_10188 = relay.var("var_10188", dtype = "float64", shape = (240,))#candidate|10188|(240,)|var|float64
output = func_10184(var_10185,var_10186,var_10187,var_10188,)
func_10189 = relay.Function([var_10185,var_10186,var_10187,var_10188,], output)
mutated_mod['func_10189'] = func_10189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8499_call = mod.get_global_var('func_8499')
func_8501_call = mutated_mod.get_global_var('func_8501')
call_10257 = relay.TupleGetItem(func_8499_call(), 0)
call_10258 = relay.TupleGetItem(func_8501_call(), 0)
output = relay.Tuple([call_10257,])
output2 = relay.Tuple([call_10258,])
func_10267 = relay.Function([], output)
mod['func_10267'] = func_10267
mod = relay.transform.InferType()(mod)
mutated_mod['func_10267'] = func_10267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10267_call = mutated_mod.get_global_var('func_10267')
call_10268 = func_10267_call()
output = call_10268
func_10269 = relay.Function([], output)
mutated_mod['func_10269'] = func_10269
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10273 = relay.var("var_10273", dtype = "int8", shape = (2, 2, 12))#candidate|10273|(2, 2, 12)|var|int8
var_10274 = relay.var("var_10274", dtype = "int8", shape = (2, 2, 12))#candidate|10274|(2, 2, 12)|var|int8
bop_10275 = relay.greater(var_10273.astype('bool'), relay.reshape(var_10274.astype('bool'), relay.shape_of(var_10273))) # shape=(2, 2, 12)
output = relay.Tuple([bop_10275,])
output2 = relay.Tuple([bop_10275,])
func_10283 = relay.Function([var_10273,var_10274,], output)
mod['func_10283'] = func_10283
mod = relay.transform.InferType()(mod)
var_10284 = relay.var("var_10284", dtype = "int8", shape = (2, 2, 12))#candidate|10284|(2, 2, 12)|var|int8
var_10285 = relay.var("var_10285", dtype = "int8", shape = (2, 2, 12))#candidate|10285|(2, 2, 12)|var|int8
output = func_10283(var_10284,var_10285,)
func_10286 = relay.Function([var_10284,var_10285,], output)
mutated_mod['func_10286'] = func_10286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8709_call = mod.get_global_var('func_8709')
func_8711_call = mutated_mod.get_global_var('func_8711')
call_10312 = relay.TupleGetItem(func_8709_call(), 0)
call_10313 = relay.TupleGetItem(func_8711_call(), 0)
output = call_10312
output2 = call_10313
func_10321 = relay.Function([], output)
mod['func_10321'] = func_10321
mod = relay.transform.InferType()(mod)
mutated_mod['func_10321'] = func_10321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10321_call = mutated_mod.get_global_var('func_10321')
call_10322 = func_10321_call()
output = call_10322
func_10323 = relay.Function([], output)
mutated_mod['func_10323'] = func_10323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2404_call = mod.get_global_var('func_2404')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_10328 = func_2404_call()
call_10329 = func_2404_call()
output = call_10328
output2 = call_10329
func_10344 = relay.Function([], output)
mod['func_10344'] = func_10344
mod = relay.transform.InferType()(mod)
output = func_10344()
func_10345 = relay.Function([], output)
mutated_mod['func_10345'] = func_10345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8709_call = mod.get_global_var('func_8709')
func_8711_call = mutated_mod.get_global_var('func_8711')
call_10349 = relay.TupleGetItem(func_8709_call(), 0)
call_10350 = relay.TupleGetItem(func_8711_call(), 0)
output = call_10349
output2 = call_10350
func_10352 = relay.Function([], output)
mod['func_10352'] = func_10352
mod = relay.transform.InferType()(mod)
output = func_10352()
func_10353 = relay.Function([], output)
mutated_mod['func_10353'] = func_10353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5131_call = mod.get_global_var('func_5131')
func_5133_call = mutated_mod.get_global_var('func_5133')
call_10438 = relay.TupleGetItem(func_5131_call(), 0)
call_10439 = relay.TupleGetItem(func_5133_call(), 0)
output = call_10438
output2 = call_10439
func_10440 = relay.Function([], output)
mod['func_10440'] = func_10440
mod = relay.transform.InferType()(mod)
output = func_10440()
func_10441 = relay.Function([], output)
mutated_mod['func_10441'] = func_10441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5539_call = mod.get_global_var('func_5539')
func_5540_call = mutated_mod.get_global_var('func_5540')
call_10445 = relay.TupleGetItem(func_5539_call(), 1)
call_10446 = relay.TupleGetItem(func_5540_call(), 1)
func_6921_call = mod.get_global_var('func_6921')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_10450 = relay.TupleGetItem(func_6921_call(), 1)
call_10451 = relay.TupleGetItem(func_6923_call(), 1)
func_9292_call = mod.get_global_var('func_9292')
func_9294_call = mutated_mod.get_global_var('func_9294')
call_10465 = relay.TupleGetItem(func_9292_call(), 0)
call_10466 = relay.TupleGetItem(func_9294_call(), 0)
func_5646_call = mod.get_global_var('func_5646')
func_5648_call = mutated_mod.get_global_var('func_5648')
call_10469 = func_5646_call()
call_10470 = func_5646_call()
var_10478 = relay.var("var_10478", dtype = "int8", shape = (12, 2, 9))#candidate|10478|(12, 2, 9)|var|int8
bop_10479 = relay.right_shift(call_10450.astype('int16'), relay.reshape(var_10478.astype('int16'), relay.shape_of(call_10450))) # shape=(12, 2, 9)
bop_10482 = relay.right_shift(call_10451.astype('int16'), relay.reshape(var_10478.astype('int16'), relay.shape_of(call_10451))) # shape=(12, 2, 9)
func_3419_call = mod.get_global_var('func_3419')
func_3421_call = mutated_mod.get_global_var('func_3421')
const_10486 = relay.const([False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False], dtype = "bool")#candidate|10486|(768,)|const|bool
call_10485 = relay.TupleGetItem(func_3419_call(relay.reshape(const_10486.astype('bool'), [768,])), 2)
call_10487 = relay.TupleGetItem(func_3421_call(relay.reshape(const_10486.astype('bool'), [768,])), 2)
func_6376_call = mod.get_global_var('func_6376')
func_6378_call = mutated_mod.get_global_var('func_6378')
call_10489 = relay.TupleGetItem(func_6376_call(), 0)
call_10490 = relay.TupleGetItem(func_6378_call(), 0)
func_3433_call = mod.get_global_var('func_3433')
func_3435_call = mutated_mod.get_global_var('func_3435')
call_10494 = relay.TupleGetItem(func_3433_call(), 0)
call_10495 = relay.TupleGetItem(func_3435_call(), 0)
func_2377_call = mod.get_global_var('func_2377')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_10503 = relay.TupleGetItem(func_2377_call(), 0)
call_10504 = relay.TupleGetItem(func_2378_call(), 0)
func_566_call = mod.get_global_var('func_566')
func_567_call = mutated_mod.get_global_var('func_567')
call_10517 = func_566_call()
call_10518 = func_566_call()
func_5403_call = mod.get_global_var('func_5403')
func_5405_call = mutated_mod.get_global_var('func_5405')
call_10528 = func_5403_call()
call_10529 = func_5403_call()
func_4435_call = mod.get_global_var('func_4435')
func_4436_call = mutated_mod.get_global_var('func_4436')
call_10534 = relay.TupleGetItem(func_4435_call(), 0)
call_10535 = relay.TupleGetItem(func_4436_call(), 0)
output = relay.Tuple([call_10445,call_10465,call_10469,bop_10479,call_10485,const_10486,call_10489,call_10494,call_10503,call_10517,call_10528,call_10534,])
output2 = relay.Tuple([call_10446,call_10466,call_10470,bop_10482,call_10487,const_10486,call_10490,call_10495,call_10504,call_10518,call_10529,call_10535,])
func_10539 = relay.Function([var_10478,], output)
mod['func_10539'] = func_10539
mod = relay.transform.InferType()(mod)
mutated_mod['func_10539'] = func_10539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10540 = relay.var("var_10540", dtype = "int8", shape = (12, 2, 9))#candidate|10540|(12, 2, 9)|var|int8
func_10539_call = mutated_mod.get_global_var('func_10539')
call_10541 = func_10539_call(var_10540)
output = call_10541
func_10542 = relay.Function([var_10540], output)
mutated_mod['func_10542'] = func_10542
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10567 = relay.var("var_10567", dtype = "float64", shape = (2, 8, 13))#candidate|10567|(2, 8, 13)|var|float64
var_10568 = relay.var("var_10568", dtype = "float64", shape = (2, 8, 13))#candidate|10568|(2, 8, 13)|var|float64
bop_10569 = relay.floor_mod(var_10567.astype('float64'), relay.reshape(var_10568.astype('float64'), relay.shape_of(var_10567))) # shape=(2, 8, 13)
func_7967_call = mod.get_global_var('func_7967')
func_7969_call = mutated_mod.get_global_var('func_7969')
call_10575 = relay.TupleGetItem(func_7967_call(), 0)
call_10576 = relay.TupleGetItem(func_7969_call(), 0)
func_2061_call = mod.get_global_var('func_2061')
func_2062_call = mutated_mod.get_global_var('func_2062')
call_10577 = relay.TupleGetItem(func_2061_call(), 0)
call_10578 = relay.TupleGetItem(func_2062_call(), 0)
output = relay.Tuple([bop_10569,call_10575,call_10577,])
output2 = relay.Tuple([bop_10569,call_10576,call_10578,])
func_10580 = relay.Function([var_10567,var_10568,], output)
mod['func_10580'] = func_10580
mod = relay.transform.InferType()(mod)
var_10581 = relay.var("var_10581", dtype = "float64", shape = (2, 8, 13))#candidate|10581|(2, 8, 13)|var|float64
var_10582 = relay.var("var_10582", dtype = "float64", shape = (2, 8, 13))#candidate|10582|(2, 8, 13)|var|float64
output = func_10580(var_10581,var_10582,)
func_10583 = relay.Function([var_10581,var_10582,], output)
mutated_mod['func_10583'] = func_10583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10092_call = mod.get_global_var('func_10092')
func_10094_call = mutated_mod.get_global_var('func_10094')
call_10614 = relay.TupleGetItem(func_10092_call(), 0)
call_10615 = relay.TupleGetItem(func_10094_call(), 0)
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_10616 = relay.TupleGetItem(func_3457_call(), 0)
call_10617 = relay.TupleGetItem(func_3459_call(), 0)
func_2377_call = mod.get_global_var('func_2377')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_10630 = relay.TupleGetItem(func_2377_call(), 0)
call_10631 = relay.TupleGetItem(func_2378_call(), 0)
output = relay.Tuple([call_10614,call_10616,call_10630,])
output2 = relay.Tuple([call_10615,call_10617,call_10631,])
func_10643 = relay.Function([], output)
mod['func_10643'] = func_10643
mod = relay.transform.InferType()(mod)
output = func_10643()
func_10644 = relay.Function([], output)
mutated_mod['func_10644'] = func_10644
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10686 = relay.var("var_10686", dtype = "float32", shape = (10, 15, 2))#candidate|10686|(10, 15, 2)|var|float32
uop_10687 = relay.atanh(var_10686.astype('float32')) # shape=(10, 15, 2)
output = relay.Tuple([uop_10687,])
output2 = relay.Tuple([uop_10687,])
func_10689 = relay.Function([var_10686,], output)
mod['func_10689'] = func_10689
mod = relay.transform.InferType()(mod)
mutated_mod['func_10689'] = func_10689
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10690 = relay.var("var_10690", dtype = "float32", shape = (10, 15, 2))#candidate|10690|(10, 15, 2)|var|float32
func_10689_call = mutated_mod.get_global_var('func_10689')
call_10691 = func_10689_call(var_10690)
output = call_10691
func_10692 = relay.Function([var_10690], output)
mutated_mod['func_10692'] = func_10692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_490_call = mod.get_global_var('func_490')
func_492_call = mutated_mod.get_global_var('func_492')
call_10753 = func_490_call()
call_10754 = func_490_call()
output = call_10753
output2 = call_10754
func_10755 = relay.Function([], output)
mod['func_10755'] = func_10755
mod = relay.transform.InferType()(mod)
mutated_mod['func_10755'] = func_10755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10755_call = mutated_mod.get_global_var('func_10755')
call_10756 = func_10755_call()
output = call_10756
func_10757 = relay.Function([], output)
mutated_mod['func_10757'] = func_10757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_10825 = relay.TupleGetItem(func_3457_call(), 0)
call_10826 = relay.TupleGetItem(func_3459_call(), 0)
func_2377_call = mod.get_global_var('func_2377')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_10831 = relay.TupleGetItem(func_2377_call(), 0)
call_10832 = relay.TupleGetItem(func_2378_call(), 0)
output = relay.Tuple([call_10825,call_10831,])
output2 = relay.Tuple([call_10826,call_10832,])
func_10841 = relay.Function([], output)
mod['func_10841'] = func_10841
mod = relay.transform.InferType()(mod)
output = func_10841()
func_10842 = relay.Function([], output)
mutated_mod['func_10842'] = func_10842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7860_call = mod.get_global_var('func_7860')
func_7861_call = mutated_mod.get_global_var('func_7861')
call_10858 = relay.TupleGetItem(func_7860_call(), 0)
call_10859 = relay.TupleGetItem(func_7861_call(), 0)
func_10344_call = mod.get_global_var('func_10344')
func_10345_call = mutated_mod.get_global_var('func_10345')
call_10866 = func_10344_call()
call_10867 = func_10344_call()
output = relay.Tuple([call_10858,call_10866,])
output2 = relay.Tuple([call_10859,call_10867,])
func_10868 = relay.Function([], output)
mod['func_10868'] = func_10868
mod = relay.transform.InferType()(mod)
output = func_10868()
func_10869 = relay.Function([], output)
mutated_mod['func_10869'] = func_10869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9459_call = mod.get_global_var('func_9459')
func_9460_call = mutated_mod.get_global_var('func_9460')
call_10885 = relay.TupleGetItem(func_9459_call(), 0)
call_10886 = relay.TupleGetItem(func_9460_call(), 0)
output = relay.Tuple([call_10885,])
output2 = relay.Tuple([call_10886,])
func_10891 = relay.Function([], output)
mod['func_10891'] = func_10891
mod = relay.transform.InferType()(mod)
output = func_10891()
func_10892 = relay.Function([], output)
mutated_mod['func_10892'] = func_10892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_10941 = relay.TupleGetItem(func_1574_call(), 3)
call_10942 = relay.TupleGetItem(func_1576_call(), 3)
func_8680_call = mod.get_global_var('func_8680')
func_8683_call = mutated_mod.get_global_var('func_8683')
const_10946 = relay.const([-0.350164,-7.259518,0.519664,-3.085251,8.684970,-3.721327,1.781835,4.066537,4.606027,-8.186019,6.559812,5.837935,-8.440229,6.253620,0.554178,3.155599,-5.598839,-8.736798,-8.942583,-9.382145], dtype = "float64")#candidate|10946|(20,)|const|float64
var_10947 = relay.var("var_10947", dtype = "float64", shape = (60,))#candidate|10947|(60,)|var|float64
call_10945 = func_8680_call(relay.reshape(const_10946.astype('float64'), [1, 4, 5]), relay.reshape(var_10947.astype('float64'), [3, 4, 5]), )
call_10948 = func_8680_call(relay.reshape(const_10946.astype('float64'), [1, 4, 5]), relay.reshape(var_10947.astype('float64'), [3, 4, 5]), )
var_10953 = relay.var("var_10953", dtype = "float64", shape = (3, 4, 5))#candidate|10953|(3, 4, 5)|var|float64
bop_10954 = relay.minimum(call_10945.astype('float32'), relay.reshape(var_10953.astype('float32'), relay.shape_of(call_10945))) # shape=(3, 4, 5)
bop_10957 = relay.minimum(call_10948.astype('float32'), relay.reshape(var_10953.astype('float32'), relay.shape_of(call_10948))) # shape=(3, 4, 5)
output = relay.Tuple([call_10941,const_10946,var_10947,bop_10954,])
output2 = relay.Tuple([call_10942,const_10946,var_10947,bop_10957,])
func_10982 = relay.Function([var_10947,var_10953,], output)
mod['func_10982'] = func_10982
mod = relay.transform.InferType()(mod)
mutated_mod['func_10982'] = func_10982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10982_call = mutated_mod.get_global_var('func_10982')
var_10984 = relay.var("var_10984", dtype = "float64", shape = (60,))#candidate|10984|(60,)|var|float64
var_10985 = relay.var("var_10985", dtype = "float64", shape = (3, 4, 5))#candidate|10985|(3, 4, 5)|var|float64
call_10983 = func_10982_call(var_10984,var_10985,)
output = call_10983
func_10986 = relay.Function([var_10984,var_10985,], output)
mutated_mod['func_10986'] = func_10986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5886_call = mod.get_global_var('func_5886')
func_5888_call = mutated_mod.get_global_var('func_5888')
call_11026 = relay.TupleGetItem(func_5886_call(), 1)
call_11027 = relay.TupleGetItem(func_5888_call(), 1)
func_10539_call = mod.get_global_var('func_10539')
func_10542_call = mutated_mod.get_global_var('func_10542')
var_11056 = relay.var("var_11056", dtype = "int8", shape = (216,))#candidate|11056|(216,)|var|int8
call_11055 = relay.TupleGetItem(func_10539_call(relay.reshape(var_11056.astype('int8'), [12, 2, 9])), 3)
call_11057 = relay.TupleGetItem(func_10542_call(relay.reshape(var_11056.astype('int8'), [12, 2, 9])), 3)
bop_11059 = relay.subtract(call_11055.astype('int8'), relay.reshape(var_11056.astype('int8'), relay.shape_of(call_11055))) # shape=(12, 2, 9)
bop_11062 = relay.subtract(call_11057.astype('int8'), relay.reshape(var_11056.astype('int8'), relay.shape_of(call_11057))) # shape=(12, 2, 9)
func_3082_call = mod.get_global_var('func_3082')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_11081 = func_3082_call()
call_11082 = func_3082_call()
output = relay.Tuple([call_11026,bop_11059,call_11081,])
output2 = relay.Tuple([call_11027,bop_11062,call_11082,])
func_11102 = relay.Function([var_11056,], output)
mod['func_11102'] = func_11102
mod = relay.transform.InferType()(mod)
mutated_mod['func_11102'] = func_11102
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11103 = relay.var("var_11103", dtype = "int8", shape = (216,))#candidate|11103|(216,)|var|int8
func_11102_call = mutated_mod.get_global_var('func_11102')
call_11104 = func_11102_call(var_11103)
output = call_11104
func_11105 = relay.Function([var_11103], output)
mutated_mod['func_11105'] = func_11105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9369_call = mod.get_global_var('func_9369')
func_9371_call = mutated_mod.get_global_var('func_9371')
call_11107 = func_9369_call()
call_11108 = func_9369_call()
func_4889_call = mod.get_global_var('func_4889')
func_4890_call = mutated_mod.get_global_var('func_4890')
call_11122 = relay.TupleGetItem(func_4889_call(), 0)
call_11123 = relay.TupleGetItem(func_4890_call(), 0)
func_10539_call = mod.get_global_var('func_10539')
func_10542_call = mutated_mod.get_global_var('func_10542')
var_11153 = relay.var("var_11153", dtype = "int8", shape = (216,))#candidate|11153|(216,)|var|int8
call_11152 = relay.TupleGetItem(func_10539_call(relay.reshape(var_11153.astype('int8'), [12, 2, 9])), 4)
call_11154 = relay.TupleGetItem(func_10542_call(relay.reshape(var_11153.astype('int8'), [12, 2, 9])), 4)
output = relay.Tuple([call_11107,call_11122,call_11152,var_11153,])
output2 = relay.Tuple([call_11108,call_11123,call_11154,var_11153,])
func_11156 = relay.Function([var_11153,], output)
mod['func_11156'] = func_11156
mod = relay.transform.InferType()(mod)
mutated_mod['func_11156'] = func_11156
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11157 = relay.var("var_11157", dtype = "int8", shape = (216,))#candidate|11157|(216,)|var|int8
func_11156_call = mutated_mod.get_global_var('func_11156')
call_11158 = func_11156_call(var_11157)
output = call_11158
func_11159 = relay.Function([var_11157], output)
mutated_mod['func_11159'] = func_11159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2377_call = mod.get_global_var('func_2377')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_11212 = relay.TupleGetItem(func_2377_call(), 0)
call_11213 = relay.TupleGetItem(func_2378_call(), 0)
func_4638_call = mod.get_global_var('func_4638')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_11231 = func_4638_call()
call_11232 = func_4638_call()
output = relay.Tuple([call_11212,call_11231,])
output2 = relay.Tuple([call_11213,call_11232,])
func_11243 = relay.Function([], output)
mod['func_11243'] = func_11243
mod = relay.transform.InferType()(mod)
mutated_mod['func_11243'] = func_11243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11243_call = mutated_mod.get_global_var('func_11243')
call_11244 = func_11243_call()
output = call_11244
func_11245 = relay.Function([], output)
mutated_mod['func_11245'] = func_11245
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11309 = relay.var("var_11309", dtype = "float64", shape = (4, 12, 8))#candidate|11309|(4, 12, 8)|var|float64
uop_11310 = relay.sigmoid(var_11309.astype('float64')) # shape=(4, 12, 8)
var_11317 = relay.var("var_11317", dtype = "float64", shape = (4, 12, 8))#candidate|11317|(4, 12, 8)|var|float64
bop_11318 = relay.floor_mod(var_11309.astype('float32'), relay.reshape(var_11317.astype('float32'), relay.shape_of(var_11309))) # shape=(4, 12, 8)
output = relay.Tuple([uop_11310,bop_11318,])
output2 = relay.Tuple([uop_11310,bop_11318,])
func_11332 = relay.Function([var_11309,var_11317,], output)
mod['func_11332'] = func_11332
mod = relay.transform.InferType()(mod)
var_11333 = relay.var("var_11333", dtype = "float64", shape = (4, 12, 8))#candidate|11333|(4, 12, 8)|var|float64
var_11334 = relay.var("var_11334", dtype = "float64", shape = (4, 12, 8))#candidate|11334|(4, 12, 8)|var|float64
output = func_11332(var_11333,var_11334,)
func_11335 = relay.Function([var_11333,var_11334,], output)
mutated_mod['func_11335'] = func_11335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7538_call = mod.get_global_var('func_7538')
func_7539_call = mutated_mod.get_global_var('func_7539')
call_11398 = func_7538_call()
call_11399 = func_7538_call()
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_11408 = func_1823_call()
call_11409 = func_1823_call()
func_4889_call = mod.get_global_var('func_4889')
func_4890_call = mutated_mod.get_global_var('func_4890')
call_11416 = relay.TupleGetItem(func_4889_call(), 0)
call_11417 = relay.TupleGetItem(func_4890_call(), 0)
output = relay.Tuple([call_11398,call_11408,call_11416,])
output2 = relay.Tuple([call_11399,call_11409,call_11417,])
func_11418 = relay.Function([], output)
mod['func_11418'] = func_11418
mod = relay.transform.InferType()(mod)
output = func_11418()
func_11419 = relay.Function([], output)
mutated_mod['func_11419'] = func_11419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3204_call = mod.get_global_var('func_3204')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_11440 = func_3204_call()
call_11441 = func_3204_call()
output = call_11440
output2 = call_11441
func_11448 = relay.Function([], output)
mod['func_11448'] = func_11448
mod = relay.transform.InferType()(mod)
mutated_mod['func_11448'] = func_11448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11448_call = mutated_mod.get_global_var('func_11448')
call_11449 = func_11448_call()
output = call_11449
func_11450 = relay.Function([], output)
mutated_mod['func_11450'] = func_11450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1142_call = mod.get_global_var('func_1142')
func_1143_call = mutated_mod.get_global_var('func_1143')
call_11484 = relay.TupleGetItem(func_1142_call(), 0)
call_11485 = relay.TupleGetItem(func_1143_call(), 0)
output = relay.Tuple([call_11484,])
output2 = relay.Tuple([call_11485,])
func_11512 = relay.Function([], output)
mod['func_11512'] = func_11512
mod = relay.transform.InferType()(mod)
output = func_11512()
func_11513 = relay.Function([], output)
mutated_mod['func_11513'] = func_11513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1736_call = mod.get_global_var('func_1736')
func_1738_call = mutated_mod.get_global_var('func_1738')
call_11532 = relay.TupleGetItem(func_1736_call(), 1)
call_11533 = relay.TupleGetItem(func_1738_call(), 1)
func_1759_call = mod.get_global_var('func_1759')
func_1761_call = mutated_mod.get_global_var('func_1761')
call_11538 = func_1759_call()
call_11539 = func_1759_call()
func_10539_call = mod.get_global_var('func_10539')
func_10542_call = mutated_mod.get_global_var('func_10542')
const_11553 = relay.const([-6,-2,3,7,-8,-5,-10,7,3,-2,9,-9,-5,10,-6,3,7,10,-5,-7,7,-10,-5,8,-10,10,10,-8,-6,4,3,-6,5,2,5,5,-1,1,-3,-5,9,-2,-7,-3,9,4,5,4,-6,-9,6,-2,-8,-3,10,-4,5,10,-6,-2,-8,-7,-6,4,7,-2,-9,10,-5,-10,2,6,2,7,8,-3,6,1,2,4,3,2,10,3,4,-2,9,-4,-5,9,10,10,-3,-10,10,-2,-1,7,6,-7,-5,-7,-9,5,1,5,-5,9,-8,3,-4,3,9,9,1,-6,-6,-1,5,9,10,-7,-3,-5,7,10,-2,9,2,7,-5,-10,-9,8,-6,9,-2,-3,3,5,5,-1,8,-10,-9,6,1,7,-4,1,-1,-6,-7,10,-8,-1,-2,-1,6,3,-8,9,4,9,-8,-9,-3,6,5,-1,4,-7,-8,-9,2,8,-10,1,-3,-3,1,2,7,3,5,-5,7,5,10,10,7,-4,-6,-2,-3,10,7,7,1,5,3,-6,2,10,7,-6,9,-1,4,6,8,-1,-7,8,8,5], dtype = "int8")#candidate|11553|(216,)|const|int8
call_11552 = relay.TupleGetItem(func_10539_call(relay.reshape(const_11553.astype('int8'), [12, 2, 9])), 0)
call_11554 = relay.TupleGetItem(func_10542_call(relay.reshape(const_11553.astype('int8'), [12, 2, 9])), 0)
func_8920_call = mod.get_global_var('func_8920')
func_8924_call = mutated_mod.get_global_var('func_8924')
var_11557 = relay.var("var_11557", dtype = "uint16", shape = (117,))#candidate|11557|(117,)|var|uint16
const_11558 = relay.const([[2,10,-1,-1,3,1,-7,7,2,5,-1,3,10,2,5,1,-5,-3,-9,-9,4,6,-10,-5,4,-2,9,-8,7,-3,3,-8,-6,7,5,10,7,-3,8,1,8,-7,-1,7,7,10,5,8,-7,9,-10,-1,2,6,-2,1,2,-8,-5,3,-5,9,9,1,4,-7,-8,5,-2,9,-8,3,-10,-5,6,-4,10,-2,5,-6,3,5,-2,1,-1,-8,-3,-1,4,8,5,-2,7,4,7,-1,3,-2,-6,9,-5,8,-7,-1,-4,-10,10,4,6,-9,9,-3,-6,7,8,-9,2,1,6,-10,-2,9,-2,9,-4,9,6,6,-7,-4,-3,-9,2,-6,-3,-1,5,-7,5,-5,4,-2,7,4,5,2,3,-4,-3,-3,5,3,6,-8,-8,1,8,4,-3,3,6,-7,7,4,-2,-6,3,-8,1,-9,1,-1,-3,-8,1,6,5,6,7,-1,7,5,-9,8,-8,-9,6,2,4,8,9,5,-9,5,-9,4,-6,-7,-1,4,-1,-10,4,-6,10,-4,-10,-3,7,5,-6,3,8,-8,-4,-10,-7,2,2,8,2,3,10,-10,-5,5,4,3,10,2,-6,-9,-3,-2],[8,7,3,-3,5,2,-8,1,-6,7,8,2,-2,-6,-3,-9,10,3,5,6,9,10,-4,-1,-9,-10,8,2,-6,-2,-5,-10,-7,8,-8,2,2,-7,6,1,-4,4,-5,-1,-3,8,4,-4,-2,2,9,-9,9,7,2,3,-9,10,-3,4,4,5,1,-10,4,-7,8,-3,-2,2,-10,-3,-2,-4,-4,1,2,7,-7,-8,-10,3,-1,-5,-7,-6,-2,8,2,8,-10,-7,5,6,2,3,1,10,-2,-6,1,-8,2,6,-7,1,3,10,3,-10,-3,9,-8,-7,-3,1,-4,-7,-4,10,1,-9,-3,-2,6,-3,2,-5,10,-1,5,-7,1,-7,10,6,-3,6,7,-2,10,4,-7,4,-2,-2,-7,10,-4,-2,-6,-6,7,-3,-9,-7,-2,1,-1,9,-10,-2,2,6,9,-2,8,2,-1,-10,-3,9,10,-5,7,-4,-6,5,-6,-6,8,-10,8,-2,8,-1,-6,6,-2,-7,-6,-7,7,2,10,-8,6,5,-9,-2,6,10,4,10,-1,-7,7,-1,4,8,3,-4,-4,-4,-3,-4,2,3,-1,3,9,9,4,10,7,-5,4,1,8,2,4,10,-9,-1],[7,2,-6,2,3,9,10,10,1,3,-7,-1,-9,6,-6,-8,-2,9,-3,7,2,6,8,-7,7,10,-5,4,4,3,6,-4,-4,-6,3,3,-1,-1,-4,10,8,-5,1,-6,9,4,1,-6,1,9,7,-3,-10,-7,-3,-8,-7,2,4,2,7,9,-3,10,8,10,-3,6,-7,10,10,-1,-2,-6,2,10,-5,5,5,-4,7,10,8,5,-9,-5,4,-7,-10,-3,-2,-2,-3,6,4,-10,-5,3,6,-9,5,-5,2,7,6,4,4,-4,-3,-2,-10,8,-5,-1,8,-8,-5,-6,-5,-9,-3,-9,-7,4,5,4,10,-3,4,-10,3,7,-10,-3,6,-4,-4,-7,-7,-10,-7,-8,-8,-4,2,-5,1,-2,-7,-6,6,-3,4,-3,1,1,-8,6,7,-8,-5,5,9,7,-2,-10,-4,1,10,-6,5,-8,-6,1,-6,6,6,-7,9,-10,8,1,2,7,4,-5,-1,-6,-9,2,-7,-5,10,-7,-8,9,-8,6,-2,2,-8,-9,-9,-8,1,4,-10,3,4,8,9,-8,10,7,-8,-8,-5,5,-1,4,5,-1,10,-5,-2,-6,2,7,7,4,4,-2,-10,-5]], dtype = "uint16")#candidate|11558|(3, 234)|const|uint16
call_11556 = relay.TupleGetItem(func_8920_call(relay.reshape(var_11557.astype('uint16'), [13, 1, 9]), relay.reshape(const_11558.astype('uint16'), [13, 6, 9]), ), 0)
call_11559 = relay.TupleGetItem(func_8924_call(relay.reshape(var_11557.astype('uint16'), [13, 1, 9]), relay.reshape(const_11558.astype('uint16'), [13, 6, 9]), ), 0)
uop_11564 = relay.tan(call_11556.astype('float64')) # shape=(13, 6, 9)
uop_11566 = relay.tan(call_11559.astype('float64')) # shape=(13, 6, 9)
output = relay.Tuple([call_11532,call_11538,call_11552,const_11553,var_11557,const_11558,uop_11564,])
output2 = relay.Tuple([call_11533,call_11539,call_11554,const_11553,var_11557,const_11558,uop_11566,])
F = relay.Function([var_11557,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_11557,], output2)
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
