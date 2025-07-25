import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_31 = relay.const([[[5.328642,-5.244481,-9.301238],[-2.037366,6.316026,2.883512],[-6.105068,-0.512940,-3.311730],[7.341774,7.072457,-8.768069],[-9.241440,9.137329,5.849001]],[[-6.576839,-4.990399,-4.713897],[5.500448,-9.022164,4.151009],[-7.903082,-3.494029,-1.297412],[-7.975473,1.452732,4.721944],[0.138221,9.590185,-6.221370]],[[6.925951,8.806149,3.275722],[5.920003,-7.308271,5.406929],[7.707141,6.005603,-3.744584],[-5.392149,-9.392184,-0.312848],[3.949898,0.478898,-3.932618]],[[-4.340047,5.268361,8.131508],[3.767785,2.689074,4.605025],[-0.654627,-6.223550,-9.822184],[7.641982,2.162471,-9.716220],[1.690729,-6.742522,-2.877969]]], dtype = "float64")#candidate|31|(4, 5, 3)|const|float64
uop_32 = relay.log2(const_31.astype('float64')) # shape=(4, 5, 3)
output = relay.Tuple([uop_32,])
output2 = relay.Tuple([uop_32,])
func_34 = relay.Function([], output)
mod['func_34'] = func_34
mod = relay.transform.InferType()(mod)
output = func_34()
func_35 = relay.Function([], output)
mutated_mod['func_35'] = func_35
mutated_mod = relay.transform.InferType()(mutated_mod)
func_34_call = mod.get_global_var('func_34')
func_35_call = mutated_mod.get_global_var('func_35')
call_117 = relay.TupleGetItem(func_34_call(), 0)
call_118 = relay.TupleGetItem(func_35_call(), 0)
output = relay.Tuple([call_117,])
output2 = relay.Tuple([call_118,])
func_121 = relay.Function([], output)
mod['func_121'] = func_121
mod = relay.transform.InferType()(mod)
output = func_121()
func_122 = relay.Function([], output)
mutated_mod['func_122'] = func_122
mutated_mod = relay.transform.InferType()(mutated_mod)
var_154 = relay.var("var_154", dtype = "float64", shape = ())#candidate|154|()|var|float64
var_155 = relay.var("var_155", dtype = "float64", shape = (14, 3, 11))#candidate|155|(14, 3, 11)|var|float64
bop_156 = relay.greater(var_154.astype('bool'), var_155.astype('bool')) # shape=(14, 3, 11)
func_121_call = mod.get_global_var('func_121')
func_122_call = mutated_mod.get_global_var('func_122')
call_163 = relay.TupleGetItem(func_121_call(), 0)
call_164 = relay.TupleGetItem(func_122_call(), 0)
bop_165 = relay.mod(bop_156.astype('float64'), relay.reshape(var_155.astype('float64'), relay.shape_of(bop_156))) # shape=(14, 3, 11)
output = relay.Tuple([call_163,bop_165,])
output2 = relay.Tuple([call_164,bop_165,])
func_170 = relay.Function([var_154,var_155,], output)
mod['func_170'] = func_170
mod = relay.transform.InferType()(mod)
var_171 = relay.var("var_171", dtype = "float64", shape = ())#candidate|171|()|var|float64
var_172 = relay.var("var_172", dtype = "float64", shape = (14, 3, 11))#candidate|172|(14, 3, 11)|var|float64
output = func_170(var_171,var_172,)
func_173 = relay.Function([var_171,var_172,], output)
mutated_mod['func_173'] = func_173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_122_call = mutated_mod.get_global_var('func_122')
call_238 = relay.TupleGetItem(func_121_call(), 0)
call_239 = relay.TupleGetItem(func_122_call(), 0)
func_121_call = mod.get_global_var('func_121')
func_122_call = mutated_mod.get_global_var('func_122')
call_241 = relay.TupleGetItem(func_121_call(), 0)
call_242 = relay.TupleGetItem(func_122_call(), 0)
func_121_call = mod.get_global_var('func_121')
func_122_call = mutated_mod.get_global_var('func_122')
call_260 = relay.TupleGetItem(func_121_call(), 0)
call_261 = relay.TupleGetItem(func_122_call(), 0)
output = relay.Tuple([call_238,call_241,call_260,])
output2 = relay.Tuple([call_239,call_242,call_261,])
func_266 = relay.Function([], output)
mod['func_266'] = func_266
mod = relay.transform.InferType()(mod)
mutated_mod['func_266'] = func_266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_266_call = mutated_mod.get_global_var('func_266')
call_267 = func_266_call()
output = call_267
func_268 = relay.Function([], output)
mutated_mod['func_268'] = func_268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_34_call = mod.get_global_var('func_34')
func_35_call = mutated_mod.get_global_var('func_35')
call_285 = relay.TupleGetItem(func_34_call(), 0)
call_286 = relay.TupleGetItem(func_35_call(), 0)
output = call_285
output2 = call_286
func_292 = relay.Function([], output)
mod['func_292'] = func_292
mod = relay.transform.InferType()(mod)
mutated_mod['func_292'] = func_292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mutated_mod.get_global_var('func_292')
call_293 = func_292_call()
output = call_293
func_294 = relay.Function([], output)
mutated_mod['func_294'] = func_294
mutated_mod = relay.transform.InferType()(mutated_mod)
const_331 = relay.const([[[6.570825,-8.133572,-0.618897,-0.047291,-8.838008,1.982757,4.494678,-8.681332,-8.735432,6.956224,-2.788553,-0.076072,5.311070,-8.072482],[-5.994376,-7.106571,4.848029,-5.258661,9.505232,-1.103647,-0.457915,-3.656164,-8.008698,-2.215940,-0.328304,-9.451678,0.937020,6.941761],[-4.848055,-2.046048,9.215823,-9.498006,-7.366847,-4.641174,7.880195,5.778576,8.075359,-2.231939,-8.544120,-3.637047,-8.049856,2.722646],[-2.903806,-8.809243,4.067323,2.492871,9.372211,2.964616,-1.648473,4.541521,3.290998,-7.468809,2.267883,-8.070951,3.347799,-6.805261],[5.675605,4.228127,4.501672,-5.471994,-6.227350,2.644754,6.445435,2.956847,7.568174,-9.445751,-3.550685,2.238380,5.111896,9.603151]],[[-4.794226,-3.992081,-9.564129,1.470302,-2.911824,-4.822974,6.250657,-8.222536,-6.391711,6.341652,4.383498,-2.570756,-9.550699,2.193656],[5.545289,-1.737600,-7.198315,1.057951,-6.287691,-2.233717,-9.573789,6.396604,0.556498,4.224265,-3.766285,5.890558,-5.630208,1.459847],[5.881371,-7.320714,3.057301,-2.504922,0.716790,-0.878243,8.595442,-5.822341,8.810789,6.790722,-2.954595,2.209096,7.865870,-0.797142],[-3.803002,-8.732018,-4.072095,8.482477,1.547277,9.720885,7.789064,-8.731297,5.630862,4.996868,7.938289,0.999284,8.504086,-7.804347],[5.926641,-5.885851,-7.465263,6.880446,8.916595,-3.224522,-3.621754,5.996655,-8.654150,-2.405531,1.348215,-9.258877,2.322403,-6.298936]],[[-0.272258,8.002793,3.917236,-8.639161,1.639948,-3.313995,-6.086310,0.168563,-3.200604,-8.256946,0.920011,-1.803294,-4.255413,9.454385],[-8.729660,-9.653076,-4.847659,-8.467117,5.701021,9.971256,-7.564679,1.302852,-5.730481,-0.936924,-4.418185,0.938833,3.552324,-3.767020],[6.317056,4.016316,1.509708,-2.103843,-6.295714,5.334166,1.349105,-8.633959,-5.850755,-6.564179,-3.220816,1.890805,-8.349436,-7.301966],[4.483893,8.988410,-1.658559,-6.713052,0.430042,5.998948,-8.538505,9.934915,2.308482,2.162944,-2.026510,1.451586,-8.881677,2.224243],[7.834069,7.730056,-8.969034,1.163984,0.653177,-9.937602,5.247790,-1.993374,-1.369927,3.812683,4.960293,6.809337,0.790575,0.549419]],[[1.098780,-5.083275,-0.959725,9.244764,-9.021809,-9.571894,0.450116,-1.970456,-0.650366,-1.344112,6.308471,2.468939,-0.048731,-9.323690],[3.449384,-4.524155,-5.332623,8.756266,-2.807509,9.063335,-7.838917,-6.084959,-9.245571,-1.468685,-1.893936,9.702594,-7.735442,-9.110190],[1.122350,-6.900357,-9.518744,3.016646,4.464783,-7.754758,-0.991030,7.170591,8.132221,-9.718195,-3.113222,-9.468515,9.270046,-5.451043],[-6.814598,-3.868158,3.622410,-4.808510,7.470059,-9.564561,6.101371,-6.670512,-0.939209,-0.566706,-3.696425,6.025001,6.486063,5.768473],[5.614197,-8.562351,-8.366676,9.205939,-7.888130,-9.322911,-9.011768,-2.647437,3.154365,7.425134,-2.442452,7.941088,-5.890321,-7.316418]]], dtype = "float64")#candidate|331|(4, 5, 14)|const|float64
uop_332 = relay.log10(const_331.astype('float64')) # shape=(4, 5, 14)
output = uop_332
output2 = uop_332
func_338 = relay.Function([], output)
mod['func_338'] = func_338
mod = relay.transform.InferType()(mod)
mutated_mod['func_338'] = func_338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_338_call = mutated_mod.get_global_var('func_338')
call_339 = func_338_call()
output = call_339
func_340 = relay.Function([], output)
mutated_mod['func_340'] = func_340
mutated_mod = relay.transform.InferType()(mutated_mod)
const_373 = relay.const([[[-7.121807],[7.024123],[1.750665],[8.169534],[0.573505],[5.292489],[-9.476269],[0.135959],[2.580366],[5.836801],[7.450378],[8.636623]],[[-6.899402],[2.360266],[1.572612],[3.826283],[-2.564570],[-9.201977],[-7.021212],[0.101449],[-2.709513],[8.991418],[-2.923702],[-2.200417]],[[-1.737951],[1.458170],[2.341972],[2.459871],[-1.757391],[-5.076735],[7.668096],[-6.506478],[-7.557756],[2.217042],[-2.667252],[-7.561553]],[[2.294527],[3.020108],[-3.491868],[7.437131],[2.794234],[1.959333],[2.528525],[-4.480902],[0.464771],[0.192456],[9.526479],[8.220886]],[[4.697450],[-2.276025],[0.270036],[-0.079548],[-8.902413],[2.043887],[1.535924],[5.871455],[2.256845],[-2.164717],[4.904983],[8.741591]],[[3.609996],[2.679831],[-7.572686],[-8.115653],[5.560018],[7.636717],[-2.971654],[5.831678],[-6.289987],[7.032582],[-7.380635],[-0.330150]],[[0.012636],[-2.816481],[-8.955843],[-2.417310],[9.535527],[-3.702487],[-6.578016],[6.413370],[5.913238],[-1.297645],[-5.997262],[-2.643112]],[[-9.578924],[-8.713824],[2.979627],[2.090750],[8.856513],[2.057439],[1.242232],[3.808547],[-6.023209],[-9.654913],[1.123502],[-1.067314]],[[-2.098196],[-8.272268],[2.041690],[9.535949],[-0.398065],[-0.952222],[8.329133],[5.982335],[1.448211],[-5.811068],[-5.869346],[9.792238]],[[5.028404],[7.115327],[4.877249],[2.012994],[-2.384702],[-3.871781],[-9.253932],[-6.000036],[-9.122591],[-0.788404],[-5.726719],[-1.521389]],[[5.303732],[-3.879668],[3.831085],[-2.017867],[8.634382],[8.161001],[6.870405],[-8.851289],[-8.907363],[8.661747],[3.663733],[5.496660]],[[-3.472691],[2.568432],[5.101950],[3.718354],[-5.562403],[-0.768351],[4.510444],[-3.047325],[-4.877431],[-9.555465],[-7.962417],[-4.322756]],[[0.931746],[1.803187],[6.546451],[-0.297234],[9.076015],[-1.261315],[-6.752690],[6.420455],[0.936441],[-3.494246],[-1.151670],[8.970202]],[[-9.887222],[-1.749433],[-8.806478],[7.935781],[0.409590],[-3.735952],[7.072657],[-4.148589],[-9.962496],[-3.169991],[-5.053229],[5.167242]],[[3.005224],[1.751164],[-9.784085],[3.839702],[-5.191824],[0.515228],[-7.186490],[-5.218438],[-8.521013],[-4.097214],[-0.408022],[-0.051854]],[[5.688669],[2.737213],[-6.156843],[6.748717],[-2.022589],[7.388161],[9.283403],[7.464490],[-4.666789],[-0.040456],[7.821246],[-9.950837]]], dtype = "float32")#candidate|373|(16, 12, 1)|const|float32
uop_374 = relay.log(const_373.astype('float32')) # shape=(16, 12, 1)
output = uop_374
output2 = uop_374
func_384 = relay.Function([], output)
mod['func_384'] = func_384
mod = relay.transform.InferType()(mod)
output = func_384()
func_385 = relay.Function([], output)
mutated_mod['func_385'] = func_385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_266_call = mod.get_global_var('func_266')
func_268_call = mutated_mod.get_global_var('func_268')
call_429 = relay.TupleGetItem(func_266_call(), 0)
call_430 = relay.TupleGetItem(func_268_call(), 0)
output = call_429
output2 = call_430
func_452 = relay.Function([], output)
mod['func_452'] = func_452
mod = relay.transform.InferType()(mod)
mutated_mod['func_452'] = func_452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_452_call = mutated_mod.get_global_var('func_452')
call_453 = func_452_call()
output = call_453
func_454 = relay.Function([], output)
mutated_mod['func_454'] = func_454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_514 = func_292_call()
call_515 = func_292_call()
func_34_call = mod.get_global_var('func_34')
func_35_call = mutated_mod.get_global_var('func_35')
call_518 = relay.TupleGetItem(func_34_call(), 0)
call_519 = relay.TupleGetItem(func_35_call(), 0)
bop_520 = relay.mod(call_518.astype('float32'), relay.reshape(call_514.astype('float32'), relay.shape_of(call_518))) # shape=(4, 5, 3)
bop_523 = relay.mod(call_519.astype('float32'), relay.reshape(call_515.astype('float32'), relay.shape_of(call_519))) # shape=(4, 5, 3)
bop_535 = relay.power(call_518.astype('float32'), relay.reshape(call_514.astype('float32'), relay.shape_of(call_518))) # shape=(4, 5, 3)
bop_538 = relay.power(call_519.astype('float32'), relay.reshape(call_515.astype('float32'), relay.shape_of(call_519))) # shape=(4, 5, 3)
var_541 = relay.var("var_541", dtype = "float32", shape = (4, 5, 3))#candidate|541|(4, 5, 3)|var|float32
bop_542 = relay.bitwise_and(bop_520.astype('int16'), relay.reshape(var_541.astype('int16'), relay.shape_of(bop_520))) # shape=(4, 5, 3)
bop_545 = relay.bitwise_and(bop_523.astype('int16'), relay.reshape(var_541.astype('int16'), relay.shape_of(bop_523))) # shape=(4, 5, 3)
uop_548 = relay.asinh(bop_535.astype('float32')) # shape=(4, 5, 3)
uop_550 = relay.asinh(bop_538.astype('float32')) # shape=(4, 5, 3)
output = relay.Tuple([bop_542,uop_548,])
output2 = relay.Tuple([bop_545,uop_550,])
func_551 = relay.Function([var_541,], output)
mod['func_551'] = func_551
mod = relay.transform.InferType()(mod)
mutated_mod['func_551'] = func_551
mutated_mod = relay.transform.InferType()(mutated_mod)
var_552 = relay.var("var_552", dtype = "float32", shape = (4, 5, 3))#candidate|552|(4, 5, 3)|var|float32
func_551_call = mutated_mod.get_global_var('func_551')
call_553 = func_551_call(var_552)
output = call_553
func_554 = relay.Function([var_552], output)
mutated_mod['func_554'] = func_554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_122_call = mutated_mod.get_global_var('func_122')
call_562 = relay.TupleGetItem(func_121_call(), 0)
call_563 = relay.TupleGetItem(func_122_call(), 0)
output = relay.Tuple([call_562,])
output2 = relay.Tuple([call_563,])
func_564 = relay.Function([], output)
mod['func_564'] = func_564
mod = relay.transform.InferType()(mod)
mutated_mod['func_564'] = func_564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_564_call = mutated_mod.get_global_var('func_564')
call_565 = func_564_call()
output = call_565
func_566 = relay.Function([], output)
mutated_mod['func_566'] = func_566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_385_call = mutated_mod.get_global_var('func_385')
call_572 = func_384_call()
call_573 = func_384_call()
output = call_572
output2 = call_573
func_600 = relay.Function([], output)
mod['func_600'] = func_600
mod = relay.transform.InferType()(mod)
mutated_mod['func_600'] = func_600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_600_call = mutated_mod.get_global_var('func_600')
call_601 = func_600_call()
output = call_601
func_602 = relay.Function([], output)
mutated_mod['func_602'] = func_602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_385_call = mutated_mod.get_global_var('func_385')
call_609 = func_384_call()
call_610 = func_384_call()
output = call_609
output2 = call_610
func_611 = relay.Function([], output)
mod['func_611'] = func_611
mod = relay.transform.InferType()(mod)
mutated_mod['func_611'] = func_611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mutated_mod.get_global_var('func_611')
call_612 = func_611_call()
output = call_612
func_613 = relay.Function([], output)
mutated_mod['func_613'] = func_613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_723 = relay.var("var_723", dtype = "bool", shape = (3, 3, 11))#candidate|723|(3, 3, 11)|var|bool
const_724 = relay.const([[[True,True,False,True,False,False,False,False,True,True,True],[True,False,False,False,False,True,False,False,True,True,False],[True,True,False,True,True,False,True,False,True,False,True]],[[True,True,True,False,True,True,True,True,True,False,True],[True,False,True,False,False,True,True,False,True,True,True],[True,False,True,False,True,True,True,True,False,False,True]],[[False,False,False,True,True,True,False,True,False,True,False],[True,False,False,False,True,False,True,False,False,True,False],[True,True,True,False,False,True,False,False,False,False,True]]], dtype = "bool")#candidate|724|(3, 3, 11)|const|bool
bop_725 = relay.logical_or(var_723.astype('bool'), relay.reshape(const_724.astype('bool'), relay.shape_of(var_723))) # shape=(3, 3, 11)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_740 = func_611_call()
call_741 = func_611_call()
output = relay.Tuple([bop_725,call_740,])
output2 = relay.Tuple([bop_725,call_741,])
func_757 = relay.Function([var_723,], output)
mod['func_757'] = func_757
mod = relay.transform.InferType()(mod)
mutated_mod['func_757'] = func_757
mutated_mod = relay.transform.InferType()(mutated_mod)
var_758 = relay.var("var_758", dtype = "bool", shape = (3, 3, 11))#candidate|758|(3, 3, 11)|var|bool
func_757_call = mutated_mod.get_global_var('func_757')
call_759 = func_757_call(var_758)
output = call_759
func_760 = relay.Function([var_758], output)
mutated_mod['func_760'] = func_760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_266_call = mod.get_global_var('func_266')
func_268_call = mutated_mod.get_global_var('func_268')
call_831 = relay.TupleGetItem(func_266_call(), 2)
call_832 = relay.TupleGetItem(func_268_call(), 2)
uop_835 = relay.sin(call_831.astype('float32')) # shape=(4, 5, 3)
uop_837 = relay.sin(call_832.astype('float32')) # shape=(4, 5, 3)
var_839 = relay.var("var_839", dtype = "float32", shape = (4, 5, 3))#candidate|839|(4, 5, 3)|var|float32
bop_840 = relay.minimum(uop_835.astype('uint64'), relay.reshape(var_839.astype('uint64'), relay.shape_of(uop_835))) # shape=(4, 5, 3)
bop_843 = relay.minimum(uop_837.astype('uint64'), relay.reshape(var_839.astype('uint64'), relay.shape_of(uop_837))) # shape=(4, 5, 3)
func_266_call = mod.get_global_var('func_266')
func_268_call = mutated_mod.get_global_var('func_268')
call_883 = relay.TupleGetItem(func_266_call(), 0)
call_884 = relay.TupleGetItem(func_268_call(), 0)
output = relay.Tuple([bop_840,call_883,])
output2 = relay.Tuple([bop_843,call_884,])
func_891 = relay.Function([var_839,], output)
mod['func_891'] = func_891
mod = relay.transform.InferType()(mod)
mutated_mod['func_891'] = func_891
mutated_mod = relay.transform.InferType()(mutated_mod)
var_892 = relay.var("var_892", dtype = "float32", shape = (4, 5, 3))#candidate|892|(4, 5, 3)|var|float32
func_891_call = mutated_mod.get_global_var('func_891')
call_893 = func_891_call(var_892)
output = call_893
func_894 = relay.Function([var_892], output)
mutated_mod['func_894'] = func_894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_904 = func_611_call()
call_905 = func_611_call()
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_913 = func_292_call()
call_914 = func_292_call()
uop_928 = relay.asinh(call_904.astype('float64')) # shape=(16, 12, 1)
uop_930 = relay.asinh(call_905.astype('float64')) # shape=(16, 12, 1)
output = relay.Tuple([call_913,uop_928,])
output2 = relay.Tuple([call_914,uop_930,])
func_931 = relay.Function([], output)
mod['func_931'] = func_931
mod = relay.transform.InferType()(mod)
output = func_931()
func_932 = relay.Function([], output)
mutated_mod['func_932'] = func_932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_950 = func_611_call()
call_951 = func_611_call()
func_452_call = mod.get_global_var('func_452')
func_454_call = mutated_mod.get_global_var('func_454')
call_999 = func_452_call()
call_1000 = func_452_call()
uop_1021 = relay.atanh(call_950.astype('float32')) # shape=(16, 12, 1)
uop_1023 = relay.atanh(call_951.astype('float32')) # shape=(16, 12, 1)
func_338_call = mod.get_global_var('func_338')
func_340_call = mutated_mod.get_global_var('func_340')
call_1025 = func_338_call()
call_1026 = func_338_call()
output = relay.Tuple([call_999,uop_1021,call_1025,])
output2 = relay.Tuple([call_1000,uop_1023,call_1026,])
func_1047 = relay.Function([], output)
mod['func_1047'] = func_1047
mod = relay.transform.InferType()(mod)
output = func_1047()
func_1048 = relay.Function([], output)
mutated_mod['func_1048'] = func_1048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1095 = relay.var("var_1095", dtype = "float64", shape = (12, 16, 12))#candidate|1095|(12, 16, 12)|var|float64
uop_1096 = relay.asin(var_1095.astype('float64')) # shape=(12, 16, 12)
output = relay.Tuple([uop_1096,])
output2 = relay.Tuple([uop_1096,])
func_1098 = relay.Function([var_1095,], output)
mod['func_1098'] = func_1098
mod = relay.transform.InferType()(mod)
mutated_mod['func_1098'] = func_1098
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1099 = relay.var("var_1099", dtype = "float64", shape = (12, 16, 12))#candidate|1099|(12, 16, 12)|var|float64
func_1098_call = mutated_mod.get_global_var('func_1098')
call_1100 = func_1098_call(var_1099)
output = call_1100
func_1101 = relay.Function([var_1099], output)
mutated_mod['func_1101'] = func_1101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_385_call = mutated_mod.get_global_var('func_385')
call_1109 = func_384_call()
call_1110 = func_384_call()
func_384_call = mod.get_global_var('func_384')
func_385_call = mutated_mod.get_global_var('func_385')
call_1119 = func_384_call()
call_1120 = func_384_call()
output = relay.Tuple([call_1109,call_1119,])
output2 = relay.Tuple([call_1110,call_1120,])
func_1122 = relay.Function([], output)
mod['func_1122'] = func_1122
mod = relay.transform.InferType()(mod)
output = func_1122()
func_1123 = relay.Function([], output)
mutated_mod['func_1123'] = func_1123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_34_call = mod.get_global_var('func_34')
func_35_call = mutated_mod.get_global_var('func_35')
call_1127 = relay.TupleGetItem(func_34_call(), 0)
call_1128 = relay.TupleGetItem(func_35_call(), 0)
func_931_call = mod.get_global_var('func_931')
func_932_call = mutated_mod.get_global_var('func_932')
call_1147 = relay.TupleGetItem(func_931_call(), 0)
call_1148 = relay.TupleGetItem(func_932_call(), 0)
func_384_call = mod.get_global_var('func_384')
func_385_call = mutated_mod.get_global_var('func_385')
call_1154 = func_384_call()
call_1155 = func_384_call()
func_551_call = mod.get_global_var('func_551')
func_554_call = mutated_mod.get_global_var('func_554')
call_1169 = relay.TupleGetItem(func_551_call(relay.reshape(call_1147.astype('float32'), [4, 5, 3])), 1)
call_1170 = relay.TupleGetItem(func_554_call(relay.reshape(call_1147.astype('float32'), [4, 5, 3])), 1)
uop_1202 = relay.exp(call_1154.astype('float32')) # shape=(16, 12, 1)
uop_1204 = relay.exp(call_1155.astype('float32')) # shape=(16, 12, 1)
output = relay.Tuple([call_1127,call_1147,call_1169,uop_1202,])
output2 = relay.Tuple([call_1128,call_1148,call_1170,uop_1204,])
func_1206 = relay.Function([], output)
mod['func_1206'] = func_1206
mod = relay.transform.InferType()(mod)
output = func_1206()
func_1207 = relay.Function([], output)
mutated_mod['func_1207'] = func_1207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1242 = relay.var("var_1242", dtype = "int16", shape = (13, 16, 11))#candidate|1242|(13, 16, 11)|var|int16
var_1243 = relay.var("var_1243", dtype = "int16", shape = (13, 16, 11))#candidate|1243|(13, 16, 11)|var|int16
bop_1244 = relay.right_shift(var_1242.astype('int16'), relay.reshape(var_1243.astype('int16'), relay.shape_of(var_1242))) # shape=(13, 16, 11)
output = bop_1244
output2 = bop_1244
func_1258 = relay.Function([var_1242,var_1243,], output)
mod['func_1258'] = func_1258
mod = relay.transform.InferType()(mod)
var_1259 = relay.var("var_1259", dtype = "int16", shape = (13, 16, 11))#candidate|1259|(13, 16, 11)|var|int16
var_1260 = relay.var("var_1260", dtype = "int16", shape = (13, 16, 11))#candidate|1260|(13, 16, 11)|var|int16
output = func_1258(var_1259,var_1260,)
func_1261 = relay.Function([var_1259,var_1260,], output)
mutated_mod['func_1261'] = func_1261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1047_call = mod.get_global_var('func_1047')
func_1048_call = mutated_mod.get_global_var('func_1048')
call_1282 = relay.TupleGetItem(func_1047_call(), 0)
call_1283 = relay.TupleGetItem(func_1048_call(), 0)
output = call_1282
output2 = call_1283
func_1286 = relay.Function([], output)
mod['func_1286'] = func_1286
mod = relay.transform.InferType()(mod)
output = func_1286()
func_1287 = relay.Function([], output)
mutated_mod['func_1287'] = func_1287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1286_call = mod.get_global_var('func_1286')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_1317 = func_1286_call()
call_1318 = func_1286_call()
output = relay.Tuple([call_1317,])
output2 = relay.Tuple([call_1318,])
func_1338 = relay.Function([], output)
mod['func_1338'] = func_1338
mod = relay.transform.InferType()(mod)
mutated_mod['func_1338'] = func_1338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1338_call = mutated_mod.get_global_var('func_1338')
call_1339 = func_1338_call()
output = call_1339
func_1340 = relay.Function([], output)
mutated_mod['func_1340'] = func_1340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1206_call = mod.get_global_var('func_1206')
func_1207_call = mutated_mod.get_global_var('func_1207')
call_1379 = relay.TupleGetItem(func_1206_call(), 3)
call_1380 = relay.TupleGetItem(func_1207_call(), 3)
func_384_call = mod.get_global_var('func_384')
func_385_call = mutated_mod.get_global_var('func_385')
call_1398 = func_384_call()
call_1399 = func_384_call()
bop_1402 = relay.floor_mod(call_1398.astype('float64'), relay.reshape(call_1379.astype('float64'), relay.shape_of(call_1398))) # shape=(16, 12, 1)
bop_1405 = relay.floor_mod(call_1399.astype('float64'), relay.reshape(call_1380.astype('float64'), relay.shape_of(call_1399))) # shape=(16, 12, 1)
func_891_call = mod.get_global_var('func_891')
func_894_call = mutated_mod.get_global_var('func_894')
const_1407 = relay.const([7.684041,-6.582098,3.401582,-4.250393,0.833776,-8.873807,7.322343,3.924093,-3.419112,-8.375982,4.580832,-2.319673,9.473989,-8.176020,5.688435,5.064095,9.316615,-0.807682,-1.729212,7.456576,-1.329787,4.060923,-0.930316,-5.996460,9.508505,-7.302076,-5.544055,7.911358,-5.974692,-4.602021,7.676758,-2.133136,7.249372,0.546263,-9.810798,-3.433263,-5.779767,-2.874033,-8.224689,-1.750573,3.040184,-9.192570,6.871077,8.601073,-0.573642,0.558652,2.565618,-0.291786,4.917048,6.528564,-1.876578,-9.201021,9.494722,-3.054871,2.644466,8.829951,0.770379,-7.082145,8.441880,-7.017800], dtype = "float32")#candidate|1407|(60,)|const|float32
call_1406 = relay.TupleGetItem(func_891_call(relay.reshape(const_1407.astype('float32'), [4, 5, 3])), 1)
call_1408 = relay.TupleGetItem(func_894_call(relay.reshape(const_1407.astype('float32'), [4, 5, 3])), 1)
uop_1425 = relay.sqrt(call_1406.astype('float32')) # shape=(4, 5, 3)
uop_1427 = relay.sqrt(call_1408.astype('float32')) # shape=(4, 5, 3)
output = relay.Tuple([bop_1402,const_1407,uop_1425,])
output2 = relay.Tuple([bop_1405,const_1407,uop_1427,])
func_1429 = relay.Function([], output)
mod['func_1429'] = func_1429
mod = relay.transform.InferType()(mod)
output = func_1429()
func_1430 = relay.Function([], output)
mutated_mod['func_1430'] = func_1430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1481 = relay.var("var_1481", dtype = "float32", shape = ())#candidate|1481|()|var|float32
const_1482 = relay.const([[[7.378232,-8.758488,-4.067704,-0.356291,0.443889,3.010570],[-7.882795,-7.864685,-2.368524,-1.014298,0.646128,0.782398],[8.439259,2.958304,2.645035,-8.082901,8.109829,9.102312],[-0.797031,0.487820,7.262180,-9.992928,-9.792767,-0.208649],[0.722616,-9.531589,4.385733,1.386823,7.503417,-4.150550],[6.564333,-9.153716,-6.342481,-0.515274,2.905781,-4.427469],[4.633383,-2.212106,0.454772,-2.194550,-3.879150,0.759124],[-6.599483,-4.340940,-8.678681,-6.981920,9.058140,-3.438323],[-3.901671,-3.979568,0.630652,8.886357,-4.967293,-8.418432],[-7.446484,-5.307645,-0.696396,4.055104,-4.177929,-1.697406],[-0.375510,-2.945704,5.263999,6.809818,0.839562,-7.010177],[5.918782,1.656778,4.348169,4.903722,-0.198974,-3.607151]],[[-6.593297,2.307538,2.590557,9.466729,7.853975,4.281764],[-6.079660,-8.996400,9.289458,-1.824379,-7.314748,-7.668672],[-5.989583,-2.140373,3.823361,9.264431,-4.872892,-5.733701],[-7.440849,4.920819,9.831141,9.483272,-4.441480,0.341753],[-7.560987,-4.013705,-2.894315,-7.646014,-4.675018,5.090931],[-7.820362,5.144625,-5.290355,-3.670726,5.877959,-5.804377],[9.132032,7.116786,6.303466,0.567352,-9.010437,3.842484],[-7.044584,0.211523,-6.994370,-3.270942,9.365633,9.561244],[9.841320,7.766699,6.161722,1.916647,4.680338,-9.966127],[5.693256,-1.792285,3.771502,-8.978289,5.712160,9.305485],[5.272247,-4.496826,3.160968,-8.730213,-6.837993,-0.260576],[4.506305,-5.931292,-8.292191,1.272647,-3.654011,2.445267]],[[1.002727,1.589347,-8.972692,-7.642887,-8.545803,-1.601682],[-2.385830,-2.251932,-4.985019,6.091165,-1.580091,-3.116246],[-4.508691,-7.487596,7.188378,3.931256,-8.376834,-9.983273],[4.421947,-2.212923,5.806948,9.761068,6.614234,-3.263273],[-7.571135,7.781519,8.613538,4.675294,9.193725,-1.951428],[-9.458241,-8.262489,-5.483289,9.097130,2.208343,9.632430],[-4.646515,2.073312,-9.603223,-0.761853,7.878590,4.164537],[0.996095,-7.220597,5.824483,-1.023621,-9.930573,-3.355434],[2.322324,-8.874840,0.010154,9.485835,1.402422,6.268482],[3.363239,-2.894951,6.396582,4.985604,7.757461,0.916789],[7.792295,-6.921132,-1.043762,-6.970948,-8.018473,9.375901],[5.589923,6.991842,0.934820,-4.145418,-1.736842,5.315478]],[[9.539702,6.878350,-8.772885,9.979822,-8.371774,-2.932673],[-7.996356,-4.948708,9.441317,-9.356098,-8.645453,2.148229],[-5.831611,-2.075720,4.366066,-9.309807,5.239497,0.583149],[-3.891277,9.085290,-4.597393,-2.475332,-1.194237,0.117245],[-9.185149,-3.743310,4.158540,-1.493937,-5.541933,8.497297],[-0.449643,-4.117302,4.746343,1.335168,-9.133782,-2.163412],[-9.907884,6.124996,3.741094,6.282525,-9.654477,-1.714533],[1.612237,0.890338,-8.781229,8.060661,-1.641666,-0.320818],[2.785275,1.454667,-5.515521,-8.477453,-5.537185,9.569533],[-5.245996,8.693573,2.432857,8.725838,-9.821614,-4.967374],[4.369440,6.321429,7.871850,3.588196,-9.079447,-8.889611],[-7.559219,0.823623,-2.579914,-7.132514,3.281563,6.150366]],[[6.124043,-9.414725,6.753311,-9.978464,-0.867736,-7.370444],[8.831586,8.657460,-9.694841,-5.927584,-3.406068,-8.906645],[8.588134,-1.668668,-4.797179,2.981269,-0.156378,-3.643242],[-8.979943,-1.223554,-1.711273,-2.501987,-6.127273,8.015534],[7.243527,6.032126,-2.272368,-6.004484,-7.929924,-6.341909],[-6.618140,-8.512076,5.344705,-5.741227,-9.278860,6.195656],[7.943002,-6.172040,3.285395,-6.955046,-9.948507,-0.343915],[0.030732,-1.520619,2.437630,9.704643,-9.887726,-3.926031],[-0.078595,4.770739,0.901250,9.038631,-2.426856,-8.993608],[-7.815291,-7.392725,-2.943739,4.112908,1.763601,3.533013],[-4.250770,-7.498082,3.876600,6.644863,3.763171,-7.354170],[9.467166,6.951114,9.344444,6.055938,-2.392968,-0.540192]],[[-6.838746,6.672510,8.320975,1.524609,1.965757,-9.608647],[-0.672885,-3.762241,-9.751134,5.296179,-4.878535,7.443944],[-8.265272,3.834401,-4.306282,-0.231137,1.069403,-3.354195],[-1.976274,1.245113,7.828835,-9.464524,2.523026,5.013865],[2.518727,2.055275,7.133536,-8.697675,0.404268,5.350148],[0.861525,-6.139277,8.020144,-3.700823,-9.333121,8.982273],[5.689855,-5.683570,-9.867130,3.670476,-4.453073,1.836205],[5.894991,7.316742,-2.396579,8.899467,-6.447456,-8.110444],[-5.309904,-7.082036,-2.419189,9.732292,1.993798,-0.312834],[9.079538,-0.189501,-0.485777,-4.508163,8.959227,-8.295869],[-1.634240,2.606734,-9.439599,-9.025906,-0.916686,3.493001],[-5.448738,3.833607,-8.275564,1.473408,3.221546,2.554408]],[[1.986928,6.757377,-2.936759,-4.774659,0.874876,4.670564],[-4.955467,3.001164,-7.446886,1.176953,6.335398,7.166552],[0.921174,0.232414,-9.936491,-0.931765,-8.293593,-1.334994],[-9.835564,3.895981,-6.922853,9.669846,-4.332472,-7.568032],[5.141261,4.134584,-6.632673,5.938498,6.821739,-4.127055],[6.300506,-2.641817,-1.282467,-4.682771,8.510944,9.919968],[5.287499,-9.920109,6.179385,-7.533137,5.709528,8.118266],[-0.822096,5.855551,8.371532,0.352322,-7.943733,6.270600],[-8.153632,8.460642,0.228303,-7.295552,5.867865,2.571836],[1.162899,-3.488336,8.158584,-1.771158,-8.947064,-1.227120],[9.231557,-5.269279,6.584827,-3.515091,-2.621022,4.286559],[-2.237784,-7.296446,3.289314,-9.855161,2.337312,5.158242]],[[-3.054971,1.168495,3.197701,5.613362,6.388322,-5.556303],[0.727786,8.296829,7.695626,4.991231,-6.197903,0.514349],[5.593942,-4.958335,-6.182526,-9.470771,5.349315,3.954405],[3.306165,1.290771,0.184492,6.550691,-0.419783,-5.019867],[6.559330,-4.329315,4.402027,6.072622,0.032835,4.406927],[0.287071,5.447961,2.338295,5.564431,2.783516,-0.032962],[1.220417,0.352203,-5.527011,9.219061,1.163238,6.340563],[9.257346,-1.135351,-6.387025,4.526625,6.290032,-0.350375],[5.393942,2.169832,-9.131794,8.270460,1.975716,9.126498],[-0.827086,9.081515,-1.045922,-3.646855,-1.591791,2.604168],[7.867844,-1.189575,0.882471,1.057688,5.724993,3.319647],[-3.074907,8.144389,8.624267,6.531031,1.524830,1.988424]],[[7.266602,3.628284,-2.398403,-6.048519,7.057138,-9.926794],[5.154904,-8.210869,-4.717708,-4.838313,-5.614269,-5.892073],[2.384039,-7.172775,9.284341,-6.804274,3.895124,-5.482185],[-2.606438,9.904962,6.311527,-1.956388,-9.467272,8.844601],[-2.265062,8.177725,7.921270,-5.669084,-8.417232,4.252859],[2.562565,-7.197156,-7.637264,-9.359617,-9.412581,-8.701181],[-6.386365,-1.001767,7.161411,1.918153,-4.624276,2.408166],[7.454615,-6.307354,-4.054877,8.353120,8.446635,-4.717788],[-5.601717,7.509801,2.903162,-5.113686,-6.930666,-5.909350],[2.561878,-9.493864,-9.702801,6.174039,5.387096,2.266444],[-2.061218,6.177019,9.917107,4.295893,4.967327,-2.818141],[-2.142380,-2.852167,0.025779,6.260692,-5.416369,-7.478774]]], dtype = "float32")#candidate|1482|(9, 12, 6)|const|float32
bop_1483 = relay.mod(var_1481.astype('float32'), const_1482.astype('float32')) # shape=(9, 12, 6)
output = relay.Tuple([bop_1483,])
output2 = relay.Tuple([bop_1483,])
func_1499 = relay.Function([var_1481,], output)
mod['func_1499'] = func_1499
mod = relay.transform.InferType()(mod)
var_1500 = relay.var("var_1500", dtype = "float32", shape = ())#candidate|1500|()|var|float32
output = func_1499(var_1500)
func_1501 = relay.Function([var_1500], output)
mutated_mod['func_1501'] = func_1501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_564_call = mod.get_global_var('func_564')
func_566_call = mutated_mod.get_global_var('func_566')
call_1507 = relay.TupleGetItem(func_564_call(), 0)
call_1508 = relay.TupleGetItem(func_566_call(), 0)
output = relay.Tuple([call_1507,])
output2 = relay.Tuple([call_1508,])
func_1519 = relay.Function([], output)
mod['func_1519'] = func_1519
mod = relay.transform.InferType()(mod)
mutated_mod['func_1519'] = func_1519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1519_call = mutated_mod.get_global_var('func_1519')
call_1520 = func_1519_call()
output = call_1520
func_1521 = relay.Function([], output)
mutated_mod['func_1521'] = func_1521
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1541 = relay.const(-6, dtype = "uint16")#candidate|1541|()|const|uint16
var_1542 = relay.var("var_1542", dtype = "uint16", shape = (8, 13, 1))#candidate|1542|(8, 13, 1)|var|uint16
bop_1543 = relay.minimum(const_1541.astype('uint16'), var_1542.astype('uint16')) # shape=(8, 13, 1)
output = bop_1543
output2 = bop_1543
func_1551 = relay.Function([var_1542,], output)
mod['func_1551'] = func_1551
mod = relay.transform.InferType()(mod)
mutated_mod['func_1551'] = func_1551
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1552 = relay.var("var_1552", dtype = "uint16", shape = (8, 13, 1))#candidate|1552|(8, 13, 1)|var|uint16
func_1551_call = mutated_mod.get_global_var('func_1551')
call_1553 = func_1551_call(var_1552)
output = call_1553
func_1554 = relay.Function([var_1552], output)
mutated_mod['func_1554'] = func_1554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_1579 = func_292_call()
call_1580 = func_292_call()
func_891_call = mod.get_global_var('func_891')
func_894_call = mutated_mod.get_global_var('func_894')
call_1581 = relay.TupleGetItem(func_891_call(relay.reshape(call_1579.astype('float32'), [4, 5, 3])), 0)
call_1582 = relay.TupleGetItem(func_894_call(relay.reshape(call_1579.astype('float32'), [4, 5, 3])), 0)
output = relay.Tuple([call_1579,call_1581,])
output2 = relay.Tuple([call_1580,call_1582,])
func_1588 = relay.Function([], output)
mod['func_1588'] = func_1588
mod = relay.transform.InferType()(mod)
output = func_1588()
func_1589 = relay.Function([], output)
mutated_mod['func_1589'] = func_1589
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1604 = relay.var("var_1604", dtype = "float32", shape = (7, 13, 4))#candidate|1604|(7, 13, 4)|var|float32
uop_1605 = relay.sin(var_1604.astype('float32')) # shape=(7, 13, 4)
output = relay.Tuple([uop_1605,])
output2 = relay.Tuple([uop_1605,])
func_1609 = relay.Function([var_1604,], output)
mod['func_1609'] = func_1609
mod = relay.transform.InferType()(mod)
var_1610 = relay.var("var_1610", dtype = "float32", shape = (7, 13, 4))#candidate|1610|(7, 13, 4)|var|float32
output = func_1609(var_1610)
func_1611 = relay.Function([var_1610], output)
mutated_mod['func_1611'] = func_1611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1429_call = mod.get_global_var('func_1429')
func_1430_call = mutated_mod.get_global_var('func_1430')
call_1660 = relay.TupleGetItem(func_1429_call(), 0)
call_1661 = relay.TupleGetItem(func_1430_call(), 0)
output = call_1660
output2 = call_1661
func_1666 = relay.Function([], output)
mod['func_1666'] = func_1666
mod = relay.transform.InferType()(mod)
output = func_1666()
func_1667 = relay.Function([], output)
mutated_mod['func_1667'] = func_1667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_1683 = func_1666_call()
call_1684 = func_1666_call()
output = relay.Tuple([call_1683,])
output2 = relay.Tuple([call_1684,])
func_1691 = relay.Function([], output)
mod['func_1691'] = func_1691
mod = relay.transform.InferType()(mod)
output = func_1691()
func_1692 = relay.Function([], output)
mutated_mod['func_1692'] = func_1692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1206_call = mod.get_global_var('func_1206')
func_1207_call = mutated_mod.get_global_var('func_1207')
call_1727 = relay.TupleGetItem(func_1206_call(), 3)
call_1728 = relay.TupleGetItem(func_1207_call(), 3)
output = relay.Tuple([call_1727,])
output2 = relay.Tuple([call_1728,])
func_1741 = relay.Function([], output)
mod['func_1741'] = func_1741
mod = relay.transform.InferType()(mod)
output = func_1741()
func_1742 = relay.Function([], output)
mutated_mod['func_1742'] = func_1742
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1755 = relay.const([[[6.041935,3.410585,7.020924,1.520792,-1.870899,-2.508288],[-2.923346,-9.329595,7.347029,1.220959,1.724513,0.496999],[0.292555,0.375973,0.181103,5.474980,-4.905918,-2.049933],[9.243674,4.705103,-6.226368,-6.848171,-2.971946,5.974253],[7.579310,0.879071,-8.513322,2.465398,9.711655,-1.630302],[9.481381,-6.937285,-9.140426,2.559425,-2.852667,0.670788],[7.126233,1.610679,5.545480,1.002597,6.089575,4.160841],[9.642500,2.473727,-0.192921,0.932117,1.607400,2.979046],[3.130829,1.268499,2.486244,-0.196524,-9.312664,6.568942],[6.385543,8.370049,7.425061,-9.240336,9.116418,-6.617845],[6.641248,5.717159,8.623985,7.391839,-1.263355,-1.276288]],[[6.922333,-4.876534,-4.413613,9.597294,-3.722035,-9.989683],[-5.872034,-1.937134,9.693607,3.885740,-9.201727,4.236607],[0.909116,-6.397195,-9.996023,3.819758,-9.842734,5.459525],[9.666645,-1.605152,2.885444,-2.214500,7.417780,9.966668],[6.345552,-9.573683,-5.044848,4.499868,-2.400972,9.971274],[-3.014721,-7.108067,-1.264329,2.082309,2.198385,4.678378],[-9.304482,-8.389021,-4.473365,-5.733314,-9.451502,2.116505],[9.497307,-9.902980,6.685093,-9.951741,-4.910516,-0.153929],[-3.066088,2.431468,1.155524,0.818300,-5.688710,6.485366],[4.905194,-8.046648,-8.245954,-0.271360,-2.717137,8.247950],[-2.636982,4.354170,2.472379,0.418224,1.597021,7.574118]]], dtype = "float32")#candidate|1755|(2, 11, 6)|const|float32
uop_1756 = relay.tan(const_1755.astype('float32')) # shape=(2, 11, 6)
output = uop_1756
output2 = uop_1756
func_1773 = relay.Function([], output)
mod['func_1773'] = func_1773
mod = relay.transform.InferType()(mod)
output = func_1773()
func_1774 = relay.Function([], output)
mutated_mod['func_1774'] = func_1774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_34_call = mod.get_global_var('func_34')
func_35_call = mutated_mod.get_global_var('func_35')
call_1775 = relay.TupleGetItem(func_34_call(), 0)
call_1776 = relay.TupleGetItem(func_35_call(), 0)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_1796 = func_611_call()
call_1797 = func_611_call()
output = relay.Tuple([call_1775,call_1796,])
output2 = relay.Tuple([call_1776,call_1797,])
func_1798 = relay.Function([], output)
mod['func_1798'] = func_1798
mod = relay.transform.InferType()(mod)
mutated_mod['func_1798'] = func_1798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1798_call = mutated_mod.get_global_var('func_1798')
call_1799 = func_1798_call()
output = call_1799
func_1800 = relay.Function([], output)
mutated_mod['func_1800'] = func_1800
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1830 = relay.var("var_1830", dtype = "float32", shape = (8, 12, 15))#candidate|1830|(8, 12, 15)|var|float32
uop_1831 = relay.asin(var_1830.astype('float32')) # shape=(8, 12, 15)
func_1098_call = mod.get_global_var('func_1098')
func_1101_call = mutated_mod.get_global_var('func_1101')
var_1839 = relay.var("var_1839", dtype = "float64", shape = (2304,))#candidate|1839|(2304,)|var|float64
call_1838 = relay.TupleGetItem(func_1098_call(relay.reshape(var_1839.astype('float64'), [12, 16, 12])), 0)
call_1840 = relay.TupleGetItem(func_1101_call(relay.reshape(var_1839.astype('float64'), [12, 16, 12])), 0)
var_1844 = relay.var("var_1844", dtype = "float32", shape = (8, 12, 15))#candidate|1844|(8, 12, 15)|var|float32
bop_1845 = relay.logical_and(uop_1831.astype('bool'), relay.reshape(var_1844.astype('bool'), relay.shape_of(uop_1831))) # shape=(8, 12, 15)
bop_1855 = relay.equal(var_1844.astype('bool'), relay.reshape(bop_1845.astype('bool'), relay.shape_of(var_1844))) # shape=(8, 12, 15)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_1874 = func_292_call()
call_1875 = func_292_call()
bop_1896 = relay.logical_or(uop_1831.astype('bool'), relay.reshape(bop_1855.astype('bool'), relay.shape_of(uop_1831))) # shape=(8, 12, 15)
uop_1911 = relay.acos(bop_1896.astype('float32')) # shape=(8, 12, 15)
output = relay.Tuple([call_1838,var_1839,call_1874,uop_1911,])
output2 = relay.Tuple([call_1840,var_1839,call_1875,uop_1911,])
func_1917 = relay.Function([var_1830,var_1839,var_1844,], output)
mod['func_1917'] = func_1917
mod = relay.transform.InferType()(mod)
var_1918 = relay.var("var_1918", dtype = "float32", shape = (8, 12, 15))#candidate|1918|(8, 12, 15)|var|float32
var_1919 = relay.var("var_1919", dtype = "float64", shape = (2304,))#candidate|1919|(2304,)|var|float64
var_1920 = relay.var("var_1920", dtype = "float32", shape = (8, 12, 15))#candidate|1920|(8, 12, 15)|var|float32
output = func_1917(var_1918,var_1919,var_1920,)
func_1921 = relay.Function([var_1918,var_1919,var_1920,], output)
mutated_mod['func_1921'] = func_1921
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1927 = relay.var("var_1927", dtype = "float32", shape = (7, 5, 11))#candidate|1927|(7, 5, 11)|var|float32
uop_1928 = relay.asin(var_1927.astype('float32')) # shape=(7, 5, 11)
uop_1932 = relay.atanh(uop_1928.astype('float64')) # shape=(7, 5, 11)
func_170_call = mod.get_global_var('func_170')
func_173_call = mutated_mod.get_global_var('func_173')
const_1946 = relay.const(9.077696, dtype = "float64")#candidate|1946|()|const|float64
const_1947 = relay.const([-4.756691,-0.386926,2.823921,6.363454,3.806508,1.188996,-4.158332,-2.133938,3.362103,-9.975920,-6.887239,-5.836983,3.594139,-3.264751,4.392140,-3.476862,3.296550,-5.382385,-8.251753,0.161351,3.197933,7.943819,-2.363135,0.084183,4.136653,-4.536683,-0.270969,7.653077,2.410700,-1.896641,2.279845,-5.830038,5.781119,3.690731,-4.424308,3.216399,6.211978,-1.014866,6.316716,8.948197,8.812280,-3.175583,1.008428,6.018526,4.295575,4.978470,-1.669954,-8.728197,-2.241760,2.094688,-9.949863,-6.173785,6.041203,3.958146,-8.963338,7.025130,-8.783372,3.174493,0.439590,-2.969226,-1.143718,3.725168,0.939338,0.147839,-9.626373,8.130699,6.869793,-4.150242,-9.960992,5.492074,2.026823,-8.789950,1.059932,7.589056,-2.958673,0.865585,0.921259,0.027085,-1.166903,-2.043580,1.155777,2.170286,6.992647,3.165764,1.799280,3.864967,5.430533,8.614572,3.091469,5.353438,-3.918893,4.459181,3.890215,7.310518,7.049812,-6.135773,7.717546,8.247815,-2.728460,-6.032563,-8.660715,-7.603138,4.862638,-3.326717,-3.534084,-9.541309,-8.825990,-8.349585,-8.791455,-1.918072,8.206195,-7.905724,-9.689017,7.050984,-3.417922,4.556673,0.230372,-6.952949,9.282067,-7.258553,-9.653444,-2.968609,-4.014529,-2.119112,-9.400825,-1.498288,-4.560758,-9.192343,-2.663592,7.071076,4.170573,3.684489,-6.857504,7.780554,-9.152566,5.903991,-7.378455,-4.369573,-7.370770,0.004005,9.403846,-0.079864,-0.469055,-9.977720,-1.726581,7.177655,-0.865744,8.390831,-7.194265,-6.190112,-4.162338,4.393457,-7.512590,4.944784,3.022603,1.282926,-4.846555,-3.782964,8.592527,2.637753,-1.081232,6.993884,-8.287268,5.198767,-9.142487,2.049755,6.819382,6.932997,-4.901105,-5.758307,-7.377046,-1.823782,4.119826,7.924784,-2.327202,-0.557093,-6.208245,2.181435,-6.418905,8.341452,0.516244,9.516615,-4.045353,-5.492746,6.893128,-3.189755,-6.857447,-6.895748,8.189710,-7.757515,2.705879,-0.574050,9.550068,-7.500599,-9.306017,-4.983494,-0.130537,-7.471173,-2.454635,-1.989774,5.083597,4.320529,3.591646,2.589778,-7.951266,-8.486139,-1.714074,5.847024,8.886412,-9.023092,3.167715,4.284851,-7.967831,-4.068723,-9.087903,4.447066,5.889783,8.400839,-2.541350,2.218184,4.450109,-0.085347,-7.369667,7.819975,8.900908,1.048404,-7.872683,1.368027,-7.991186,9.943977,-4.768955,-2.096368,-5.359026,-5.782109,-2.332938,4.419969,-8.709165,-1.324259,9.320768,-1.951611,2.039345,8.229097,-0.253361,-8.346004,0.905511,8.935524,-7.091933,0.374252,0.389102,-2.057079,-7.461333,7.976037,0.429570,6.977700,4.185918,-0.392643,-9.326260,-6.836993,-8.113470,5.826409,6.537454,6.883814,9.852071,-6.789802,-1.101523,-2.612409,-7.164068,0.943616,3.230221,-2.381357,-4.103230,4.419690,-0.418199,8.199432,7.550488,-8.499787,4.300050,-4.714461,7.060703,-9.281600,0.192887,-5.145876,-6.435548,-5.724693,-3.681875,3.553882,2.926443,8.709674,-0.711162,-4.784288,-9.079025,-8.940906,-7.122262,-0.330777,7.460509,2.576885,1.450718,-3.323268,-5.253172,-3.288966,2.355156,2.135718,-7.850213,4.679993,-3.909454,-2.774062,-4.535299,-3.761449,-4.778317,-4.698987,7.970560,-3.435375,4.324593,6.368826,9.470091,5.738961,0.333513,2.191883,9.879668,-5.123455,-6.141417,-4.247574,-4.164586,2.331254,1.988375,-4.538098,-5.956140,-7.645162,-8.045624,6.267163,7.375338,-4.217343,1.504138,-7.038340,-7.433569,-8.084961,-8.361277,-2.368964,-7.681584,6.204201,3.789226,-9.655734,-4.298619,-8.717869,-2.302596,7.405391,-3.315666,-6.214779,4.734786,-1.058925,-9.760863,2.896001,-3.170055,7.481158,1.799465,-5.830213,-6.635440,-3.890698,7.564498,9.741343,-0.700357,1.081073,0.063680,9.015953,7.307300,-4.870481,-2.920857,-1.940998,1.692777,8.508669,-1.294572,-1.970627,1.324165,5.335927,6.883103,-3.174706,1.051846,-7.086217,-3.892496,-4.555068,3.654837,2.121966,-3.643771,-5.455450,5.114966,-2.148634,-3.541400,-8.729542,-2.453594,-7.851842,2.745783,2.190831,8.750538,1.190730,4.685772,7.558003,-1.453227,7.884381,-0.824041,9.088166,4.191126,2.875384,-6.124745,2.103320,5.131447,-9.806135,9.277071,-5.919725,8.019537,-3.707768,7.802246,9.517282,-4.561669,-8.047462,9.794962,-5.214554,1.896010,-8.386822,1.022847,-0.119121,2.278358,6.684517,9.131229,3.109256,6.991977,7.241020,0.652038,6.243621,9.168421,-7.668048,8.732659,-7.496747,-5.654263,-7.840445,-9.637870,3.705456,8.845131,-1.132419,-2.036036,4.431054,3.706779,-3.432206,1.656131,-1.892405,2.777711,9.916904,5.988749,9.789897,-5.182686,-2.364521,2.592045,2.796138,-9.861128,1.033737,7.072469,8.028062,6.301381,-0.543358,6.075809,-3.327319,7.837648,0.223163], dtype = "float64")#candidate|1947|(462,)|const|float64
call_1945 = relay.TupleGetItem(func_170_call(relay.reshape(const_1946.astype('float64'), []), relay.reshape(const_1947.astype('float64'), [14, 3, 11]), ), 1)
call_1948 = relay.TupleGetItem(func_173_call(relay.reshape(const_1946.astype('float64'), []), relay.reshape(const_1947.astype('float64'), [14, 3, 11]), ), 1)
func_564_call = mod.get_global_var('func_564')
func_566_call = mutated_mod.get_global_var('func_566')
call_1950 = relay.TupleGetItem(func_564_call(), 0)
call_1951 = relay.TupleGetItem(func_566_call(), 0)
uop_1953 = relay.asinh(uop_1932.astype('float64')) # shape=(7, 5, 11)
uop_1958 = relay.sigmoid(call_1950.astype('float64')) # shape=(4, 5, 3)
uop_1960 = relay.sigmoid(call_1951.astype('float64')) # shape=(4, 5, 3)
const_1962 = relay.const([[[-7.789637,1.486501,-6.093383,-6.413465,-2.015246,-8.294260,3.913207,-6.429233,-9.089879,-9.024955,0.451018],[-0.658553,-4.818490,1.448382,-3.214252,-3.651283,-5.807569,5.100263,2.238483,-3.483822,9.840495,-3.739151],[-2.007111,-7.400670,-2.831276,4.627049,-1.396130,0.571560,0.750743,9.415207,7.982887,-5.504115,9.495379],[-6.743964,-5.791677,-6.826670,2.860580,-8.097685,-5.775152,-9.080810,0.385062,-0.568595,7.166978,-5.837024],[-0.671609,-9.174285,8.012057,-0.083477,-5.751274,4.183523,8.180152,-0.227748,-4.191821,-3.038970,9.635003]],[[4.561487,-9.257814,6.000648,8.220232,0.834517,2.580612,-3.673265,-2.993939,4.051648,5.370884,4.119149],[-0.156400,-7.164511,-9.459487,9.550684,4.756631,-5.219247,0.402636,-1.978557,1.670787,-7.259524,1.577339],[7.480397,5.608233,7.308765,-6.576275,2.774858,-5.652816,7.532493,9.163000,4.582129,-0.333432,-3.238191],[3.454575,-1.205764,-8.430152,8.236138,9.133294,-5.704372,3.678280,-2.297998,-6.770880,-7.757823,4.495578],[-7.998107,8.823428,6.262205,5.203122,3.085832,-9.963268,-8.732448,-4.612728,4.243879,-2.381897,8.853380]],[[3.415519,7.210413,4.687686,-2.708477,-4.344382,0.885372,-5.161654,6.004860,3.023069,-2.353631,-1.991454],[-8.689992,-1.564917,2.253029,6.107670,-5.365447,-1.564873,6.652527,-0.056776,-3.123939,-5.571394,-2.565925],[-8.092689,-7.688817,-9.051915,-3.308831,4.057168,7.915418,-9.993536,1.242574,5.958121,-4.687987,5.730594],[-0.265048,1.047740,-2.131054,-2.462343,8.904315,-4.132490,-5.853268,-0.004717,-8.196664,-3.197272,-3.278854],[-2.128584,-5.422262,6.723988,0.247663,-8.670370,-5.222917,-3.185009,4.285213,4.625861,3.927616,8.763084]],[[-1.217000,-9.317062,4.027481,2.025199,1.990208,9.424583,7.743104,-0.107049,-1.329348,-1.860827,0.502334],[7.991129,-7.547788,0.683707,6.330912,7.891880,-4.165632,-7.805933,-5.338900,5.653050,9.938309,-8.297233],[-0.552968,8.569416,6.658556,9.873780,-8.866186,-5.297748,-9.175166,-1.798832,-5.016321,2.277829,-7.827133],[-8.583845,4.790497,-3.481126,0.100016,-8.056654,-9.179040,-3.427064,5.840841,-5.965232,-8.640592,-6.828398],[-9.252265,-6.052757,0.203300,3.825473,9.161100,-3.782196,-9.000492,8.598365,0.475066,0.616663,1.281146]],[[-8.135076,8.127524,-3.632496,8.141051,-3.179368,-1.064550,-5.242416,8.370344,9.286083,6.090708,6.204023],[-7.707643,4.091920,-3.727280,9.444666,-4.072210,7.919502,-0.105617,-4.533056,-9.686189,0.211136,0.897837],[-7.246686,-3.429100,-7.854229,-1.558065,3.000405,-2.723200,-0.667018,6.678255,7.069637,2.432470,7.283583],[-1.531339,3.508646,6.337159,8.030135,-4.394498,9.113997,4.520882,6.395657,4.463526,1.290444,1.750570],[3.622971,8.243546,7.169342,9.912095,9.371160,-8.719332,-5.076771,9.733536,-4.634893,-3.940789,-4.620531]],[[2.447266,9.859916,-4.359900,0.035180,-0.216075,-9.512856,7.134517,4.514328,3.851937,-6.210890,1.987292],[6.860713,9.430441,8.168896,1.578862,3.086838,3.141008,9.679460,5.358843,3.714084,3.329423,-4.937225],[8.984863,9.145378,-5.924176,-3.716891,4.483827,-9.607687,-6.346127,-1.694912,-6.545377,-9.862251,-9.298724],[7.241242,-2.137665,0.145812,9.821220,-8.717837,4.793877,6.898552,-8.964500,-5.425904,7.979768,-3.936206],[-6.567741,8.216932,-6.607587,-3.515609,4.860676,3.194709,-3.443963,-3.212314,-1.587118,1.305613,-1.052441]],[[4.437365,-4.633020,-3.171011,-8.480490,1.445659,5.083005,2.462495,7.282601,-5.452066,-9.991088,-2.472311],[0.089817,-6.431358,-9.218113,2.367972,-2.940719,8.863627,-7.209299,-1.700893,-1.394556,1.310777,-7.110777],[6.771183,-6.668616,-6.361967,4.411954,-9.502770,4.891439,-4.223082,-3.299553,2.260088,-4.526471,2.155606],[-6.304401,-5.920899,-8.451902,0.528991,-1.340978,-8.499720,-6.174353,5.515344,6.722301,-9.772609,-6.876086],[-6.414407,3.905697,4.404637,-2.014002,-8.180916,-6.847725,9.516595,4.435629,5.054226,-0.383802,-2.838331]]], dtype = "float64")#candidate|1962|(7, 5, 11)|const|float64
bop_1963 = relay.left_shift(uop_1953.astype('int8'), relay.reshape(const_1962.astype('int8'), relay.shape_of(uop_1953))) # shape=(7, 5, 11)
bop_1970 = relay.bitwise_and(bop_1963.astype('int8'), relay.reshape(uop_1932.astype('int8'), relay.shape_of(bop_1963))) # shape=(7, 5, 11)
uop_1984 = relay.sigmoid(uop_1953.astype('float32')) # shape=(7, 5, 11)
bop_1988 = relay.multiply(uop_1932.astype('int64'), const_1946.astype('int64')) # shape=(7, 5, 11)
output = relay.Tuple([call_1945,const_1947,uop_1958,bop_1970,uop_1984,bop_1988,])
output2 = relay.Tuple([call_1948,const_1947,uop_1960,bop_1970,uop_1984,bop_1988,])
func_1993 = relay.Function([var_1927,], output)
mod['func_1993'] = func_1993
mod = relay.transform.InferType()(mod)
var_1994 = relay.var("var_1994", dtype = "float32", shape = (7, 5, 11))#candidate|1994|(7, 5, 11)|var|float32
output = func_1993(var_1994)
func_1995 = relay.Function([var_1994], output)
mutated_mod['func_1995'] = func_1995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1122_call = mod.get_global_var('func_1122')
func_1123_call = mutated_mod.get_global_var('func_1123')
call_2003 = relay.TupleGetItem(func_1122_call(), 0)
call_2004 = relay.TupleGetItem(func_1123_call(), 0)
output = relay.Tuple([call_2003,])
output2 = relay.Tuple([call_2004,])
func_2009 = relay.Function([], output)
mod['func_2009'] = func_2009
mod = relay.transform.InferType()(mod)
output = func_2009()
func_2010 = relay.Function([], output)
mutated_mod['func_2010'] = func_2010
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2018 = relay.var("var_2018", dtype = "int8", shape = (3, 7, 3))#candidate|2018|(3, 7, 3)|var|int8
var_2019 = relay.var("var_2019", dtype = "int8", shape = (3, 7, 3))#candidate|2019|(3, 7, 3)|var|int8
bop_2020 = relay.subtract(var_2018.astype('int8'), relay.reshape(var_2019.astype('int8'), relay.shape_of(var_2018))) # shape=(3, 7, 3)
output = bop_2020
output2 = bop_2020
func_2045 = relay.Function([var_2018,var_2019,], output)
mod['func_2045'] = func_2045
mod = relay.transform.InferType()(mod)
mutated_mod['func_2045'] = func_2045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2045_call = mutated_mod.get_global_var('func_2045')
var_2047 = relay.var("var_2047", dtype = "int8", shape = (3, 7, 3))#candidate|2047|(3, 7, 3)|var|int8
var_2048 = relay.var("var_2048", dtype = "int8", shape = (3, 7, 3))#candidate|2048|(3, 7, 3)|var|int8
call_2046 = func_2045_call(var_2047,var_2048,)
output = call_2046
func_2049 = relay.Function([var_2047,var_2048,], output)
mutated_mod['func_2049'] = func_2049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_600_call = mod.get_global_var('func_600')
func_602_call = mutated_mod.get_global_var('func_602')
call_2063 = func_600_call()
call_2064 = func_600_call()
func_1519_call = mod.get_global_var('func_1519')
func_1521_call = mutated_mod.get_global_var('func_1521')
call_2068 = relay.TupleGetItem(func_1519_call(), 0)
call_2069 = relay.TupleGetItem(func_1521_call(), 0)
output = relay.Tuple([call_2063,call_2068,])
output2 = relay.Tuple([call_2064,call_2069,])
func_2070 = relay.Function([], output)
mod['func_2070'] = func_2070
mod = relay.transform.InferType()(mod)
mutated_mod['func_2070'] = func_2070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2070_call = mutated_mod.get_global_var('func_2070')
call_2071 = func_2070_call()
output = call_2071
func_2072 = relay.Function([], output)
mutated_mod['func_2072'] = func_2072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1286_call = mod.get_global_var('func_1286')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_2090 = func_1286_call()
call_2091 = func_1286_call()
output = relay.Tuple([call_2090,])
output2 = relay.Tuple([call_2091,])
func_2094 = relay.Function([], output)
mod['func_2094'] = func_2094
mod = relay.transform.InferType()(mod)
output = func_2094()
func_2095 = relay.Function([], output)
mutated_mod['func_2095'] = func_2095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1741_call = mod.get_global_var('func_1741')
func_1742_call = mutated_mod.get_global_var('func_1742')
call_2118 = relay.TupleGetItem(func_1741_call(), 0)
call_2119 = relay.TupleGetItem(func_1742_call(), 0)
func_2045_call = mod.get_global_var('func_2045')
func_2049_call = mutated_mod.get_global_var('func_2049')
const_2122 = relay.const([-8,-5,-10,-4,2,-10,-6,6,-9,-2,-9,6,-7,-4,-6,8,-3,-10,4,9,-6,8,-5,-9,-5,1,-10,-5,-7,-1,7,9,-4,4,-3,-3,2,-10,-6,-9,4,7,8,-10,3,10,-3,-2,9,5,1,-10,9,-9,-1,-10,-10,-8,10,-5,-1,5,-5], dtype = "int8")#candidate|2122|(63,)|const|int8
call_2121 = func_2045_call(relay.reshape(const_2122.astype('int8'), [3, 7, 3]), relay.reshape(const_2122.astype('int8'), [3, 7, 3]), )
call_2123 = func_2045_call(relay.reshape(const_2122.astype('int8'), [3, 7, 3]), relay.reshape(const_2122.astype('int8'), [3, 7, 3]), )
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_2125 = func_1666_call()
call_2126 = func_1666_call()
bop_2127 = relay.equal(const_2122.astype('bool'), call_2118.astype('bool')) # shape=(16, 12, 63)
bop_2130 = relay.equal(const_2122.astype('bool'), call_2119.astype('bool')) # shape=(16, 12, 63)
output = relay.Tuple([call_2121,call_2125,bop_2127,])
output2 = relay.Tuple([call_2123,call_2126,bop_2130,])
func_2154 = relay.Function([], output)
mod['func_2154'] = func_2154
mod = relay.transform.InferType()(mod)
mutated_mod['func_2154'] = func_2154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2154_call = mutated_mod.get_global_var('func_2154')
call_2155 = func_2154_call()
output = call_2155
func_2156 = relay.Function([], output)
mutated_mod['func_2156'] = func_2156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2154_call = mod.get_global_var('func_2154')
func_2156_call = mutated_mod.get_global_var('func_2156')
call_2162 = relay.TupleGetItem(func_2154_call(), 0)
call_2163 = relay.TupleGetItem(func_2156_call(), 0)
func_1429_call = mod.get_global_var('func_1429')
func_1430_call = mutated_mod.get_global_var('func_1430')
call_2164 = relay.TupleGetItem(func_1429_call(), 2)
call_2165 = relay.TupleGetItem(func_1430_call(), 2)
uop_2166 = relay.log(call_2162.astype('float32')) # shape=(3, 7, 3)
uop_2168 = relay.log(call_2163.astype('float32')) # shape=(3, 7, 3)
uop_2171 = relay.erf(call_2162.astype('float64')) # shape=(3, 7, 3)
uop_2173 = relay.erf(call_2163.astype('float64')) # shape=(3, 7, 3)
func_551_call = mod.get_global_var('func_551')
func_554_call = mutated_mod.get_global_var('func_554')
call_2196 = relay.TupleGetItem(func_551_call(relay.reshape(call_2164.astype('float32'), [4, 5, 3])), 0)
call_2197 = relay.TupleGetItem(func_554_call(relay.reshape(call_2164.astype('float32'), [4, 5, 3])), 0)
var_2198 = relay.var("var_2198", dtype = "float64", shape = (3, 7, 3))#candidate|2198|(3, 7, 3)|var|float64
bop_2199 = relay.equal(uop_2171.astype('bool'), relay.reshape(var_2198.astype('bool'), relay.shape_of(uop_2171))) # shape=(3, 7, 3)
bop_2202 = relay.equal(uop_2173.astype('bool'), relay.reshape(var_2198.astype('bool'), relay.shape_of(uop_2173))) # shape=(3, 7, 3)
uop_2204 = relay.log10(uop_2166.astype('float64')) # shape=(3, 7, 3)
uop_2206 = relay.log10(uop_2168.astype('float64')) # shape=(3, 7, 3)
output = relay.Tuple([call_2164,call_2196,bop_2199,uop_2204,])
output2 = relay.Tuple([call_2165,call_2197,bop_2202,uop_2206,])
func_2207 = relay.Function([var_2198,], output)
mod['func_2207'] = func_2207
mod = relay.transform.InferType()(mod)
var_2208 = relay.var("var_2208", dtype = "float64", shape = (3, 7, 3))#candidate|2208|(3, 7, 3)|var|float64
output = func_2207(var_2208)
func_2209 = relay.Function([var_2208], output)
mutated_mod['func_2209'] = func_2209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_2259 = func_292_call()
call_2260 = func_292_call()
uop_2273 = relay.exp(call_2259.astype('float64')) # shape=(4, 5, 3)
uop_2275 = relay.exp(call_2260.astype('float64')) # shape=(4, 5, 3)
func_1206_call = mod.get_global_var('func_1206')
func_1207_call = mutated_mod.get_global_var('func_1207')
call_2283 = relay.TupleGetItem(func_1206_call(), 3)
call_2284 = relay.TupleGetItem(func_1207_call(), 3)
output = relay.Tuple([uop_2273,call_2283,])
output2 = relay.Tuple([uop_2275,call_2284,])
func_2288 = relay.Function([], output)
mod['func_2288'] = func_2288
mod = relay.transform.InferType()(mod)
mutated_mod['func_2288'] = func_2288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2288_call = mutated_mod.get_global_var('func_2288')
call_2289 = func_2288_call()
output = call_2289
func_2290 = relay.Function([], output)
mutated_mod['func_2290'] = func_2290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_564_call = mod.get_global_var('func_564')
func_566_call = mutated_mod.get_global_var('func_566')
call_2338 = relay.TupleGetItem(func_564_call(), 0)
call_2339 = relay.TupleGetItem(func_566_call(), 0)
output = relay.Tuple([call_2338,])
output2 = relay.Tuple([call_2339,])
func_2344 = relay.Function([], output)
mod['func_2344'] = func_2344
mod = relay.transform.InferType()(mod)
mutated_mod['func_2344'] = func_2344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2344_call = mutated_mod.get_global_var('func_2344')
call_2345 = func_2344_call()
output = call_2345
func_2346 = relay.Function([], output)
mutated_mod['func_2346'] = func_2346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2344_call = mod.get_global_var('func_2344')
func_2346_call = mutated_mod.get_global_var('func_2346')
call_2360 = relay.TupleGetItem(func_2344_call(), 0)
call_2361 = relay.TupleGetItem(func_2346_call(), 0)
output = call_2360
output2 = call_2361
func_2369 = relay.Function([], output)
mod['func_2369'] = func_2369
mod = relay.transform.InferType()(mod)
mutated_mod['func_2369'] = func_2369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2369_call = mutated_mod.get_global_var('func_2369')
call_2370 = func_2369_call()
output = call_2370
func_2371 = relay.Function([], output)
mutated_mod['func_2371'] = func_2371
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2471 = relay.var("var_2471", dtype = "bool", shape = (5, 13, 12))#candidate|2471|(5, 13, 12)|var|bool
var_2472 = relay.var("var_2472", dtype = "bool", shape = (5, 13, 12))#candidate|2472|(5, 13, 12)|var|bool
bop_2473 = relay.logical_or(var_2471.astype('bool'), relay.reshape(var_2472.astype('bool'), relay.shape_of(var_2471))) # shape=(5, 13, 12)
uop_2482 = relay.atan(var_2472.astype('float32')) # shape=(5, 13, 12)
output = relay.Tuple([bop_2473,uop_2482,])
output2 = relay.Tuple([bop_2473,uop_2482,])
func_2485 = relay.Function([var_2471,var_2472,], output)
mod['func_2485'] = func_2485
mod = relay.transform.InferType()(mod)
mutated_mod['func_2485'] = func_2485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2485_call = mutated_mod.get_global_var('func_2485')
var_2487 = relay.var("var_2487", dtype = "bool", shape = (5, 13, 12))#candidate|2487|(5, 13, 12)|var|bool
var_2488 = relay.var("var_2488", dtype = "bool", shape = (5, 13, 12))#candidate|2488|(5, 13, 12)|var|bool
call_2486 = func_2485_call(var_2487,var_2488,)
output = call_2486
func_2489 = relay.Function([var_2487,var_2488,], output)
mutated_mod['func_2489'] = func_2489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_122_call = mutated_mod.get_global_var('func_122')
call_2505 = relay.TupleGetItem(func_121_call(), 0)
call_2506 = relay.TupleGetItem(func_122_call(), 0)
uop_2507 = relay.cos(call_2505.astype('float32')) # shape=(4, 5, 3)
uop_2509 = relay.cos(call_2506.astype('float32')) # shape=(4, 5, 3)
func_1773_call = mod.get_global_var('func_1773')
func_1774_call = mutated_mod.get_global_var('func_1774')
call_2511 = func_1773_call()
call_2512 = func_1773_call()
func_1338_call = mod.get_global_var('func_1338')
func_1340_call = mutated_mod.get_global_var('func_1340')
call_2513 = relay.TupleGetItem(func_1338_call(), 0)
call_2514 = relay.TupleGetItem(func_1340_call(), 0)
func_2045_call = mod.get_global_var('func_2045')
func_2049_call = mutated_mod.get_global_var('func_2049')
var_2522 = relay.var("var_2522", dtype = "int8", shape = (63,))#candidate|2522|(63,)|var|int8
call_2521 = func_2045_call(relay.reshape(var_2522.astype('int8'), [3, 7, 3]), relay.reshape(var_2522.astype('int8'), [3, 7, 3]), )
call_2523 = func_2045_call(relay.reshape(var_2522.astype('int8'), [3, 7, 3]), relay.reshape(var_2522.astype('int8'), [3, 7, 3]), )
output = relay.Tuple([uop_2507,call_2511,call_2513,call_2521,var_2522,])
output2 = relay.Tuple([uop_2509,call_2512,call_2514,call_2523,var_2522,])
func_2525 = relay.Function([var_2522,], output)
mod['func_2525'] = func_2525
mod = relay.transform.InferType()(mod)
mutated_mod['func_2525'] = func_2525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2526 = relay.var("var_2526", dtype = "int8", shape = (63,))#candidate|2526|(63,)|var|int8
func_2525_call = mutated_mod.get_global_var('func_2525')
call_2527 = func_2525_call(var_2526)
output = call_2527
func_2528 = relay.Function([var_2526], output)
mutated_mod['func_2528'] = func_2528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1798_call = mod.get_global_var('func_1798')
func_1800_call = mutated_mod.get_global_var('func_1800')
call_2551 = relay.TupleGetItem(func_1798_call(), 1)
call_2552 = relay.TupleGetItem(func_1800_call(), 1)
uop_2561 = relay.log10(call_2551.astype('float64')) # shape=(16, 12, 1)
uop_2563 = relay.log10(call_2552.astype('float64')) # shape=(16, 12, 1)
output = uop_2561
output2 = uop_2563
func_2578 = relay.Function([], output)
mod['func_2578'] = func_2578
mod = relay.transform.InferType()(mod)
mutated_mod['func_2578'] = func_2578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2578_call = mutated_mod.get_global_var('func_2578')
call_2579 = func_2578_call()
output = call_2579
func_2580 = relay.Function([], output)
mutated_mod['func_2580'] = func_2580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1429_call = mod.get_global_var('func_1429')
func_1430_call = mutated_mod.get_global_var('func_1430')
call_2586 = relay.TupleGetItem(func_1429_call(), 2)
call_2587 = relay.TupleGetItem(func_1430_call(), 2)
uop_2597 = relay.atanh(call_2586.astype('float32')) # shape=(4, 5, 3)
uop_2599 = relay.atanh(call_2587.astype('float32')) # shape=(4, 5, 3)
uop_2616 = relay.atan(uop_2597.astype('float32')) # shape=(4, 5, 3)
uop_2618 = relay.atan(uop_2599.astype('float32')) # shape=(4, 5, 3)
output = uop_2616
output2 = uop_2618
func_2623 = relay.Function([], output)
mod['func_2623'] = func_2623
mod = relay.transform.InferType()(mod)
output = func_2623()
func_2624 = relay.Function([], output)
mutated_mod['func_2624'] = func_2624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2623_call = mod.get_global_var('func_2623')
func_2624_call = mutated_mod.get_global_var('func_2624')
call_2628 = func_2623_call()
call_2629 = func_2623_call()
uop_2641 = relay.acos(call_2628.astype('float32')) # shape=(4, 5, 3)
uop_2643 = relay.acos(call_2629.astype('float32')) # shape=(4, 5, 3)
output = uop_2641
output2 = uop_2643
func_2648 = relay.Function([], output)
mod['func_2648'] = func_2648
mod = relay.transform.InferType()(mod)
output = func_2648()
func_2649 = relay.Function([], output)
mutated_mod['func_2649'] = func_2649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_122_call = mutated_mod.get_global_var('func_122')
call_2677 = relay.TupleGetItem(func_121_call(), 0)
call_2678 = relay.TupleGetItem(func_122_call(), 0)
output = relay.Tuple([call_2677,])
output2 = relay.Tuple([call_2678,])
func_2684 = relay.Function([], output)
mod['func_2684'] = func_2684
mod = relay.transform.InferType()(mod)
mutated_mod['func_2684'] = func_2684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2684_call = mutated_mod.get_global_var('func_2684')
call_2685 = func_2684_call()
output = call_2685
func_2686 = relay.Function([], output)
mutated_mod['func_2686'] = func_2686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_2703 = func_1666_call()
call_2704 = func_1666_call()
func_1741_call = mod.get_global_var('func_1741')
func_1742_call = mutated_mod.get_global_var('func_1742')
call_2706 = relay.TupleGetItem(func_1741_call(), 0)
call_2707 = relay.TupleGetItem(func_1742_call(), 0)
func_1499_call = mod.get_global_var('func_1499')
func_1501_call = mutated_mod.get_global_var('func_1501')
var_2725 = relay.var("var_2725", dtype = "float32", shape = ())#candidate|2725|()|var|float32
call_2724 = relay.TupleGetItem(func_1499_call(relay.reshape(var_2725.astype('float32'), [])), 0)
call_2726 = relay.TupleGetItem(func_1501_call(relay.reshape(var_2725.astype('float32'), [])), 0)
func_1798_call = mod.get_global_var('func_1798')
func_1800_call = mutated_mod.get_global_var('func_1800')
call_2735 = relay.TupleGetItem(func_1798_call(), 0)
call_2736 = relay.TupleGetItem(func_1800_call(), 0)
func_2207_call = mod.get_global_var('func_2207')
func_2209_call = mutated_mod.get_global_var('func_2209')
var_2738 = relay.var("var_2738", dtype = "float64", shape = (63,))#candidate|2738|(63,)|var|float64
call_2737 = relay.TupleGetItem(func_2207_call(relay.reshape(var_2738.astype('float64'), [3, 7, 3])), 2)
call_2739 = relay.TupleGetItem(func_2209_call(relay.reshape(var_2738.astype('float64'), [3, 7, 3])), 2)
output = relay.Tuple([call_2703,call_2706,call_2724,var_2725,call_2735,call_2737,var_2738,])
output2 = relay.Tuple([call_2704,call_2707,call_2726,var_2725,call_2736,call_2739,var_2738,])
func_2742 = relay.Function([var_2725,var_2738,], output)
mod['func_2742'] = func_2742
mod = relay.transform.InferType()(mod)
var_2743 = relay.var("var_2743", dtype = "float32", shape = ())#candidate|2743|()|var|float32
var_2744 = relay.var("var_2744", dtype = "float64", shape = (63,))#candidate|2744|(63,)|var|float64
output = func_2742(var_2743,var_2744,)
func_2745 = relay.Function([var_2743,var_2744,], output)
mutated_mod['func_2745'] = func_2745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_452_call = mod.get_global_var('func_452')
func_454_call = mutated_mod.get_global_var('func_454')
call_2762 = func_452_call()
call_2763 = func_452_call()
var_2764 = relay.var("var_2764", dtype = "float64", shape = (4, 5, 3))#candidate|2764|(4, 5, 3)|var|float64
bop_2765 = relay.add(call_2762.astype('uint64'), relay.reshape(var_2764.astype('uint64'), relay.shape_of(call_2762))) # shape=(4, 5, 3)
bop_2768 = relay.add(call_2763.astype('uint64'), relay.reshape(var_2764.astype('uint64'), relay.shape_of(call_2763))) # shape=(4, 5, 3)
func_2742_call = mod.get_global_var('func_2742')
func_2745_call = mutated_mod.get_global_var('func_2745')
const_2772 = relay.const(8.216592, dtype = "float32")#candidate|2772|()|const|float32
const_2773 = relay.const([-8.040347,4.509530,-6.437256,5.792592,-6.130869,8.867497,-1.480165,-0.019045,0.757318,-4.245269,9.617196,7.182819,-4.574554,6.516806,4.199176,4.601731,-4.913114,-2.507634,8.241337,-6.566467,-5.382026,-9.521558,-5.766873,4.580617,-5.734882,1.901310,-7.358358,-3.601017,3.407454,-5.137889,-5.766463,6.313281,-5.605247,-5.088006,0.774901,5.120079,-1.267002,7.847972,1.504989,4.067252,-7.578014,0.295880,3.199688,5.951898,3.933995,0.092346,8.886721,-3.486953,-9.726041,6.488739,-3.398800,8.675342,5.274799,7.792857,5.341878,-9.583829,3.210988,-4.061662,3.884937,1.875326,1.558715,9.943790,8.514224], dtype = "float64")#candidate|2773|(63,)|const|float64
call_2771 = relay.TupleGetItem(func_2742_call(relay.reshape(const_2772.astype('float32'), []), relay.reshape(const_2773.astype('float64'), [63,]), ), 3)
call_2774 = relay.TupleGetItem(func_2745_call(relay.reshape(const_2772.astype('float32'), []), relay.reshape(const_2773.astype('float64'), [63,]), ), 3)
uop_2775 = relay.sinh(call_2762.astype('float32')) # shape=(4, 5, 3)
uop_2777 = relay.sinh(call_2763.astype('float32')) # shape=(4, 5, 3)
func_452_call = mod.get_global_var('func_452')
func_454_call = mutated_mod.get_global_var('func_454')
call_2778 = func_452_call()
call_2779 = func_452_call()
output = relay.Tuple([bop_2765,call_2771,const_2772,const_2773,uop_2775,call_2778,])
output2 = relay.Tuple([bop_2768,call_2774,const_2772,const_2773,uop_2777,call_2779,])
func_2785 = relay.Function([var_2764,], output)
mod['func_2785'] = func_2785
mod = relay.transform.InferType()(mod)
mutated_mod['func_2785'] = func_2785
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2786 = relay.var("var_2786", dtype = "float64", shape = (4, 5, 3))#candidate|2786|(4, 5, 3)|var|float64
func_2785_call = mutated_mod.get_global_var('func_2785')
call_2787 = func_2785_call(var_2786)
output = call_2787
func_2788 = relay.Function([var_2786], output)
mutated_mod['func_2788'] = func_2788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2154_call = mod.get_global_var('func_2154')
func_2156_call = mutated_mod.get_global_var('func_2156')
call_2814 = relay.TupleGetItem(func_2154_call(), 2)
call_2815 = relay.TupleGetItem(func_2156_call(), 2)
var_2817 = relay.var("var_2817", dtype = "bool", shape = (16, 12, 63))#candidate|2817|(16, 12, 63)|var|bool
bop_2818 = relay.not_equal(call_2814.astype('bool'), relay.reshape(var_2817.astype('bool'), relay.shape_of(call_2814))) # shape=(16, 12, 63)
bop_2821 = relay.not_equal(call_2815.astype('bool'), relay.reshape(var_2817.astype('bool'), relay.shape_of(call_2815))) # shape=(16, 12, 63)
uop_2823 = relay.cos(bop_2818.astype('float32')) # shape=(16, 12, 63)
uop_2825 = relay.cos(bop_2821.astype('float32')) # shape=(16, 12, 63)
func_2154_call = mod.get_global_var('func_2154')
func_2156_call = mutated_mod.get_global_var('func_2156')
call_2827 = relay.TupleGetItem(func_2154_call(), 1)
call_2828 = relay.TupleGetItem(func_2156_call(), 1)
bop_2834 = relay.add(uop_2823.astype('float64'), relay.reshape(bop_2818.astype('float64'), relay.shape_of(uop_2823))) # shape=(16, 12, 63)
bop_2837 = relay.add(uop_2825.astype('float64'), relay.reshape(bop_2821.astype('float64'), relay.shape_of(uop_2825))) # shape=(16, 12, 63)
func_34_call = mod.get_global_var('func_34')
func_35_call = mutated_mod.get_global_var('func_35')
call_2838 = relay.TupleGetItem(func_34_call(), 0)
call_2839 = relay.TupleGetItem(func_35_call(), 0)
bop_2842 = relay.logical_and(call_2814.astype('bool'), relay.reshape(var_2817.astype('bool'), relay.shape_of(call_2814))) # shape=(16, 12, 63)
bop_2845 = relay.logical_and(call_2815.astype('bool'), relay.reshape(var_2817.astype('bool'), relay.shape_of(call_2815))) # shape=(16, 12, 63)
const_2855 = relay.const([[[True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True],[True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True],[True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False],[False,False,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,True,True],[True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,True,False,False,False,True],[True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False],[False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True],[False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False],[True,True,True,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False],[False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True],[False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False],[False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False]],[[False,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,False,True],[False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True],[True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True],[False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True],[True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False],[False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True],[False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True],[False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True],[True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True],[True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False],[True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,True],[False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False]],[[False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,False,False],[False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False],[False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,True],[False,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False],[True,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,True,True],[False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False],[False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True],[True,True,True,False,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True],[False,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False],[False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True],[False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True],[False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True]],[[True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,True],[False,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False],[True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False],[False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True],[False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True],[True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True],[False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True],[False,True,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True],[True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False],[True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True],[True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,False],[False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,True]],[[True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False],[True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,False,False],[True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True],[False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,True],[False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False],[True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False],[True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False],[True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False],[True,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,False],[False,True,True,False,True,True,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True],[True,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True],[True,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False]],[[True,True,True,False,False,False,False,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True],[False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False],[False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,False,True,True,False,False,False,True,True],[False,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True],[True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,True,True,False,False],[False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True],[True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,False,False],[False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True],[True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False],[False,False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True],[True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False],[False,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True]],[[False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False],[True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True],[True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,False],[True,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True],[False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False],[False,False,False,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True],[False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False],[False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False],[False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True],[True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True],[False,True,False,False,True,False,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False],[False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False]],[[True,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,True,True],[False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False],[False,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,False,False],[False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True],[False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False],[False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True],[False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False],[False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True],[True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False],[False,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,True],[False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,False],[True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True]],[[True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True],[False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,True,False,False],[True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,True,True,False,False],[True,True,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,False],[True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True],[True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True],[False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False],[False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False],[False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,False],[False,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False],[True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False],[False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False]],[[True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True],[True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True],[False,False,False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False],[True,True,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,True],[False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True],[False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False],[True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,False],[False,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,True],[True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False],[True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,False,False,False,False],[False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False],[True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False]],[[False,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False],[True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True],[False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True],[True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False],[False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,True,False,True],[False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,True],[False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,True],[True,True,True,True,False,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False],[False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True],[False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False],[False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False],[False,True,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True]],[[False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,True],[False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,False],[True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,True],[True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,True,True,False],[True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False],[False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,True],[True,True,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,True],[False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True],[True,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True],[False,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False],[False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,True],[False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False]],[[True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,True,True],[False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,True],[False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True],[True,True,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,True,True,True,False],[False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False],[True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True],[True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False],[False,False,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,False,False,True,True,False,False,False,False],[True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True],[True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True],[True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,False,False],[False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True]],[[True,True,True,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False],[False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False],[True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False],[False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True],[False,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False],[False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,False,False,False],[False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,False],[False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,False,False,True],[False,True,False,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,True],[False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False],[False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,True,True],[False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True]],[[True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True],[False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False],[False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False],[True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False],[False,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,True,False],[True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True],[False,True,True,False,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False],[True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False],[True,True,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,True],[False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,False],[True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,False,True],[True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False]],[[False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False],[True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False],[True,True,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True],[True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True],[False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False],[True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True],[False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True],[True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,False,True],[False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,True],[False,True,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False],[True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True],[False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False]]], dtype = "bool")#candidate|2855|(16, 12, 63)|const|bool
bop_2856 = relay.bitwise_and(call_2814.astype('uint32'), relay.reshape(const_2855.astype('uint32'), relay.shape_of(call_2814))) # shape=(16, 12, 63)
bop_2859 = relay.bitwise_and(call_2815.astype('uint32'), relay.reshape(const_2855.astype('uint32'), relay.shape_of(call_2815))) # shape=(16, 12, 63)
uop_2866 = relay.acosh(call_2838.astype('float64')) # shape=(4, 5, 3)
uop_2868 = relay.acosh(call_2839.astype('float64')) # shape=(4, 5, 3)
output = relay.Tuple([call_2827,bop_2834,bop_2842,bop_2856,uop_2866,])
output2 = relay.Tuple([call_2828,bop_2837,bop_2845,bop_2859,uop_2868,])
func_2869 = relay.Function([var_2817,], output)
mod['func_2869'] = func_2869
mod = relay.transform.InferType()(mod)
var_2870 = relay.var("var_2870", dtype = "bool", shape = (16, 12, 63))#candidate|2870|(16, 12, 63)|var|bool
output = func_2869(var_2870)
func_2871 = relay.Function([var_2870], output)
mutated_mod['func_2871'] = func_2871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2623_call = mod.get_global_var('func_2623')
func_2624_call = mutated_mod.get_global_var('func_2624')
call_2876 = func_2623_call()
call_2877 = func_2623_call()
func_121_call = mod.get_global_var('func_121')
func_122_call = mutated_mod.get_global_var('func_122')
call_2929 = relay.TupleGetItem(func_121_call(), 0)
call_2930 = relay.TupleGetItem(func_122_call(), 0)
output = relay.Tuple([call_2876,call_2929,])
output2 = relay.Tuple([call_2877,call_2930,])
func_2934 = relay.Function([], output)
mod['func_2934'] = func_2934
mod = relay.transform.InferType()(mod)
output = func_2934()
func_2935 = relay.Function([], output)
mutated_mod['func_2935'] = func_2935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1773_call = mod.get_global_var('func_1773')
func_1774_call = mutated_mod.get_global_var('func_1774')
call_2947 = func_1773_call()
call_2948 = func_1773_call()
output = relay.Tuple([call_2947,])
output2 = relay.Tuple([call_2948,])
func_2951 = relay.Function([], output)
mod['func_2951'] = func_2951
mod = relay.transform.InferType()(mod)
mutated_mod['func_2951'] = func_2951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2951_call = mutated_mod.get_global_var('func_2951')
call_2952 = func_2951_call()
output = call_2952
func_2953 = relay.Function([], output)
mutated_mod['func_2953'] = func_2953
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2984 = relay.var("var_2984", dtype = "float64", shape = (1, 9, 7))#candidate|2984|(1, 9, 7)|var|float64
uop_2985 = relay.asinh(var_2984.astype('float64')) # shape=(1, 9, 7)
func_2045_call = mod.get_global_var('func_2045')
func_2049_call = mutated_mod.get_global_var('func_2049')
call_2994 = func_2045_call(relay.reshape(uop_2985.astype('int8'), [3, 7, 3]), relay.reshape(uop_2985.astype('int8'), [3, 7, 3]), )
call_2995 = func_2045_call(relay.reshape(uop_2985.astype('int8'), [3, 7, 3]), relay.reshape(uop_2985.astype('int8'), [3, 7, 3]), )
output = relay.Tuple([uop_2985,call_2994,])
output2 = relay.Tuple([uop_2985,call_2995,])
func_3005 = relay.Function([var_2984,], output)
mod['func_3005'] = func_3005
mod = relay.transform.InferType()(mod)
mutated_mod['func_3005'] = func_3005
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3006 = relay.var("var_3006", dtype = "float64", shape = (1, 9, 7))#candidate|3006|(1, 9, 7)|var|float64
func_3005_call = mutated_mod.get_global_var('func_3005')
call_3007 = func_3005_call(var_3006)
output = call_3007
func_3008 = relay.Function([var_3006], output)
mutated_mod['func_3008'] = func_3008
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3037 = relay.var("var_3037", dtype = "float64", shape = (2, 6, 15))#candidate|3037|(2, 6, 15)|var|float64
uop_3038 = relay.log10(var_3037.astype('float64')) # shape=(2, 6, 15)
output = relay.Tuple([uop_3038,])
output2 = relay.Tuple([uop_3038,])
func_3047 = relay.Function([var_3037,], output)
mod['func_3047'] = func_3047
mod = relay.transform.InferType()(mod)
var_3048 = relay.var("var_3048", dtype = "float64", shape = (2, 6, 15))#candidate|3048|(2, 6, 15)|var|float64
output = func_3047(var_3048)
func_3049 = relay.Function([var_3048], output)
mutated_mod['func_3049'] = func_3049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_600_call = mod.get_global_var('func_600')
func_602_call = mutated_mod.get_global_var('func_602')
call_3081 = func_600_call()
call_3082 = func_600_call()
output = relay.Tuple([call_3081,])
output2 = relay.Tuple([call_3082,])
func_3084 = relay.Function([], output)
mod['func_3084'] = func_3084
mod = relay.transform.InferType()(mod)
mutated_mod['func_3084'] = func_3084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3084_call = mutated_mod.get_global_var('func_3084')
call_3085 = func_3084_call()
output = call_3085
func_3086 = relay.Function([], output)
mutated_mod['func_3086'] = func_3086
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3116 = relay.var("var_3116", dtype = "uint16", shape = (1, 5, 10))#candidate|3116|(1, 5, 10)|var|uint16
var_3117 = relay.var("var_3117", dtype = "uint16", shape = (13, 5, 10))#candidate|3117|(13, 5, 10)|var|uint16
bop_3118 = relay.bitwise_xor(var_3116.astype('uint16'), var_3117.astype('uint16')) # shape=(13, 5, 10)
output = bop_3118
output2 = bop_3118
func_3122 = relay.Function([var_3116,var_3117,], output)
mod['func_3122'] = func_3122
mod = relay.transform.InferType()(mod)
mutated_mod['func_3122'] = func_3122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3122_call = mutated_mod.get_global_var('func_3122')
var_3124 = relay.var("var_3124", dtype = "uint16", shape = (1, 5, 10))#candidate|3124|(1, 5, 10)|var|uint16
var_3125 = relay.var("var_3125", dtype = "uint16", shape = (13, 5, 10))#candidate|3125|(13, 5, 10)|var|uint16
call_3123 = func_3122_call(var_3124,var_3125,)
output = call_3123
func_3126 = relay.Function([var_3124,var_3125,], output)
mutated_mod['func_3126'] = func_3126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_338_call = mod.get_global_var('func_338')
func_340_call = mutated_mod.get_global_var('func_340')
call_3155 = func_338_call()
call_3156 = func_338_call()
output = call_3155
output2 = call_3156
func_3160 = relay.Function([], output)
mod['func_3160'] = func_3160
mod = relay.transform.InferType()(mod)
output = func_3160()
func_3161 = relay.Function([], output)
mutated_mod['func_3161'] = func_3161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1286_call = mod.get_global_var('func_1286')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_3162 = func_1286_call()
call_3163 = func_1286_call()
func_1098_call = mod.get_global_var('func_1098')
func_1101_call = mutated_mod.get_global_var('func_1101')
var_3167 = relay.var("var_3167", dtype = "float64", shape = (1152, 2))#candidate|3167|(1152, 2)|var|float64
call_3166 = relay.TupleGetItem(func_1098_call(relay.reshape(var_3167.astype('float64'), [12, 16, 12])), 0)
call_3168 = relay.TupleGetItem(func_1101_call(relay.reshape(var_3167.astype('float64'), [12, 16, 12])), 0)
func_2934_call = mod.get_global_var('func_2934')
func_2935_call = mutated_mod.get_global_var('func_2935')
call_3183 = relay.TupleGetItem(func_2934_call(), 0)
call_3184 = relay.TupleGetItem(func_2935_call(), 0)
output = relay.Tuple([call_3162,call_3166,var_3167,call_3183,])
output2 = relay.Tuple([call_3163,call_3168,var_3167,call_3184,])
func_3192 = relay.Function([var_3167,], output)
mod['func_3192'] = func_3192
mod = relay.transform.InferType()(mod)
mutated_mod['func_3192'] = func_3192
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3193 = relay.var("var_3193", dtype = "float64", shape = (1152, 2))#candidate|3193|(1152, 2)|var|float64
func_3192_call = mutated_mod.get_global_var('func_3192')
call_3194 = func_3192_call(var_3193)
output = call_3194
func_3195 = relay.Function([var_3193], output)
mutated_mod['func_3195'] = func_3195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1047_call = mod.get_global_var('func_1047')
func_1048_call = mutated_mod.get_global_var('func_1048')
call_3278 = relay.TupleGetItem(func_1047_call(), 0)
call_3279 = relay.TupleGetItem(func_1048_call(), 0)
output = call_3278
output2 = call_3279
func_3281 = relay.Function([], output)
mod['func_3281'] = func_3281
mod = relay.transform.InferType()(mod)
output = func_3281()
func_3282 = relay.Function([], output)
mutated_mod['func_3282'] = func_3282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1691_call = mod.get_global_var('func_1691')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_3301 = relay.TupleGetItem(func_1691_call(), 0)
call_3302 = relay.TupleGetItem(func_1692_call(), 0)
output = relay.Tuple([call_3301,])
output2 = relay.Tuple([call_3302,])
func_3305 = relay.Function([], output)
mod['func_3305'] = func_3305
mod = relay.transform.InferType()(mod)
mutated_mod['func_3305'] = func_3305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3305_call = mutated_mod.get_global_var('func_3305')
call_3306 = func_3305_call()
output = call_3306
func_3307 = relay.Function([], output)
mutated_mod['func_3307'] = func_3307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2951_call = mod.get_global_var('func_2951')
func_2953_call = mutated_mod.get_global_var('func_2953')
call_3308 = relay.TupleGetItem(func_2951_call(), 0)
call_3309 = relay.TupleGetItem(func_2953_call(), 0)
func_1258_call = mod.get_global_var('func_1258')
func_1261_call = mutated_mod.get_global_var('func_1261')
var_3312 = relay.var("var_3312", dtype = "int16", shape = (2288,))#candidate|3312|(2288,)|var|int16
call_3311 = func_1258_call(relay.reshape(var_3312.astype('int16'), [13, 16, 11]), relay.reshape(var_3312.astype('int16'), [13, 16, 11]), )
call_3313 = func_1258_call(relay.reshape(var_3312.astype('int16'), [13, 16, 11]), relay.reshape(var_3312.astype('int16'), [13, 16, 11]), )
func_1338_call = mod.get_global_var('func_1338')
func_1340_call = mutated_mod.get_global_var('func_1340')
call_3315 = relay.TupleGetItem(func_1338_call(), 0)
call_3316 = relay.TupleGetItem(func_1340_call(), 0)
uop_3329 = relay.tan(var_3312.astype('float64')) # shape=(2288,)
bop_3345 = relay.greater(uop_3329.astype('bool'), relay.reshape(call_3311.astype('bool'), relay.shape_of(uop_3329))) # shape=(2288,)
bop_3348 = relay.greater(uop_3329.astype('bool'), relay.reshape(call_3313.astype('bool'), relay.shape_of(uop_3329))) # shape=(2288,)
func_384_call = mod.get_global_var('func_384')
func_385_call = mutated_mod.get_global_var('func_385')
call_3351 = func_384_call()
call_3352 = func_384_call()
func_1588_call = mod.get_global_var('func_1588')
func_1589_call = mutated_mod.get_global_var('func_1589')
call_3356 = relay.TupleGetItem(func_1588_call(), 0)
call_3357 = relay.TupleGetItem(func_1589_call(), 0)
func_1773_call = mod.get_global_var('func_1773')
func_1774_call = mutated_mod.get_global_var('func_1774')
call_3358 = func_1773_call()
call_3359 = func_1773_call()
bop_3365 = relay.logical_and(bop_3345.astype('bool'), relay.reshape(uop_3329.astype('bool'), relay.shape_of(bop_3345))) # shape=(2288,)
bop_3368 = relay.logical_and(bop_3348.astype('bool'), relay.reshape(uop_3329.astype('bool'), relay.shape_of(bop_3348))) # shape=(2288,)
output = relay.Tuple([call_3308,call_3315,call_3351,call_3356,call_3358,bop_3365,])
output2 = relay.Tuple([call_3309,call_3316,call_3352,call_3357,call_3359,bop_3368,])
func_3369 = relay.Function([var_3312,], output)
mod['func_3369'] = func_3369
mod = relay.transform.InferType()(mod)
mutated_mod['func_3369'] = func_3369
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3370 = relay.var("var_3370", dtype = "int16", shape = (2288,))#candidate|3370|(2288,)|var|int16
func_3369_call = mutated_mod.get_global_var('func_3369')
call_3371 = func_3369_call(var_3370)
output = call_3371
func_3372 = relay.Function([var_3370], output)
mutated_mod['func_3372'] = func_3372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3281_call = mod.get_global_var('func_3281')
func_3282_call = mutated_mod.get_global_var('func_3282')
call_3398 = func_3281_call()
call_3399 = func_3281_call()
output = call_3398
output2 = call_3399
func_3408 = relay.Function([], output)
mod['func_3408'] = func_3408
mod = relay.transform.InferType()(mod)
mutated_mod['func_3408'] = func_3408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3408_call = mutated_mod.get_global_var('func_3408')
call_3409 = func_3408_call()
output = call_3409
func_3410 = relay.Function([], output)
mutated_mod['func_3410'] = func_3410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_3460 = func_611_call()
call_3461 = func_611_call()
const_3472 = relay.const([[[9.882871,-3.518263,3.612321,-7.848412,4.001881,-8.412566,-3.991438,7.681621,2.158510,8.654060,5.272054,3.365303,2.125427],[1.684625,-0.628559,-6.138300,1.002935,5.178125,7.180767,7.462106,7.387802,0.128992,8.871090,1.072971,2.524597,2.804755],[-1.668684,8.572688,3.304299,-7.096790,5.983668,1.377616,-1.662238,-4.561355,-8.209278,-2.241616,3.395662,8.857424,2.737995],[1.330887,0.141084,7.443824,-6.018292,-2.857081,2.284039,9.313449,2.096965,7.005165,8.666573,7.338556,7.774661,-9.981280],[-0.114211,-4.440797,-5.737539,-8.840012,-4.079784,4.444444,-9.148921,3.475985,4.812953,3.696418,6.630634,-1.334729,-1.457157],[5.986836,0.276084,-3.348537,2.744216,6.690304,2.521637,-4.468009,-6.141489,-6.721992,2.770975,-1.353348,-4.859930,9.840177],[1.373401,-7.938229,-5.704010,6.124425,2.178547,6.566265,-1.031708,0.275387,-4.499018,-2.766040,3.253139,-9.129771,-1.209101],[1.518702,-1.821442,-2.646694,-1.715689,7.596067,-1.873125,4.815521,-2.003060,5.029771,1.624546,-7.445448,-4.293474,-1.076748],[7.300157,-4.884552,-6.941147,-9.868218,-8.421709,-9.325663,-8.224446,2.452495,-6.110729,-0.061844,1.071065,-2.493623,-6.263530],[1.112124,5.287846,1.987666,-7.447931,-3.691114,6.689368,7.269746,8.892884,7.929494,0.121584,9.097149,0.818695,-8.085561],[8.470687,4.742731,-2.882881,-9.352662,6.658776,-3.108014,4.557163,-9.017403,-5.767676,-2.848380,8.267734,2.720937,9.874811],[-8.580793,-1.792481,2.695788,3.636977,-9.701974,3.502167,7.642113,-2.996641,-0.243493,-3.569189,-0.747836,-7.308622,1.710602]],[[-1.566683,-8.486369,8.916653,-7.036508,-1.680182,9.346873,6.581242,7.381758,-2.844251,1.067379,-2.447192,-1.190059,-4.182426],[7.662436,6.728702,-3.488289,4.283211,8.308382,8.627198,0.711708,-9.982613,-1.686364,-6.570186,-4.862492,-7.553416,2.540825],[-8.663113,-5.372390,-9.417345,4.099193,-1.158585,-0.561522,9.005966,-6.407270,7.848473,-7.275512,-4.604780,1.913178,-4.249634],[9.135106,1.109351,0.548842,-4.383982,-1.538200,-0.459259,-5.781415,8.234239,-9.120599,1.162732,-7.442347,-8.895605,-1.436230],[8.171734,4.282629,4.033770,-7.831319,7.524967,-9.985670,7.429855,7.506683,3.096080,-1.656359,-4.890328,4.562568,7.308150],[-3.898600,-1.103306,-5.564957,8.863910,7.274717,-5.747449,4.543149,2.631294,9.493670,8.127432,-2.153738,0.593814,6.403923],[-9.201058,9.352106,-0.130225,4.144866,-2.229282,-1.556813,-0.909408,-3.414885,-4.468011,-8.998229,-5.127466,-3.386294,-3.265652],[-2.654786,-6.069175,3.362316,-4.266746,-5.984239,1.840787,6.215872,-9.101502,3.121019,4.883591,6.613004,0.594380,5.425876],[-4.785429,2.335841,9.335768,-4.347621,-3.389465,-1.197240,-8.774373,9.502075,-6.681100,0.367659,8.964267,2.902170,-6.713866],[-4.249143,8.042015,9.945340,1.433547,-8.156108,-7.531378,-7.200524,7.619989,6.479078,-6.074576,8.602979,1.204167,0.084010],[9.279001,2.214113,4.759504,0.613533,-7.938220,-1.463834,-4.536622,-1.774560,6.345076,7.508188,6.234822,-1.283490,1.525545],[-7.004482,-8.213037,1.815474,9.021923,-2.169829,-0.656902,6.484325,-5.111897,4.971922,-5.364940,-0.838172,-5.857549,-0.993346]],[[-7.541036,2.350997,-5.915713,3.160706,6.016810,-5.151253,3.283139,-8.151489,2.172662,-6.783431,4.112783,-0.747062,7.192838],[-6.607477,-2.968614,7.805184,0.549395,-4.932164,7.197170,4.597636,7.492525,9.761346,-6.339600,-2.959552,9.831867,4.392189],[-6.347706,-6.556335,-0.996214,-5.177978,-7.249554,-3.551280,-0.355072,7.365910,-3.904503,3.704488,6.519067,-4.718933,-9.732133],[3.338033,-5.036701,-7.501689,-0.604073,-8.081682,4.195531,8.189517,9.354909,-3.109659,-9.199826,1.991742,-0.434955,-6.675882],[3.231350,0.196346,-1.047721,6.070577,9.447540,3.152726,-0.003761,2.088638,-9.936766,5.898526,-8.504689,-9.878290,-9.401818],[3.484560,-4.457811,-4.763594,-9.306321,8.079698,-4.798415,6.542291,-7.906256,9.102048,1.418701,4.369662,6.963077,0.235754],[-9.692353,-8.379492,0.682399,5.199027,-5.396186,4.577723,2.935502,8.972071,4.912218,2.499471,4.104605,-7.636743,9.063959],[8.907928,1.130190,-2.963197,-7.145719,-7.845308,-6.818523,0.151170,0.379930,-8.145304,8.575871,-5.290549,-5.753455,-1.344061],[-8.769599,-9.956573,-6.736383,-6.711208,-3.842355,8.533972,5.716907,-0.280955,6.466013,-1.645404,-0.573446,6.990419,-0.380150],[-6.200972,-5.069180,9.332314,-6.730649,-4.284927,4.844407,-3.312354,-0.399671,-6.692199,0.619078,6.219828,-1.535032,6.886275],[-8.938494,-1.496523,-7.075168,-1.470810,0.817890,7.703095,2.074610,4.646340,-5.526556,4.632188,7.105321,-8.414449,-7.455722],[-1.155615,-1.172881,-4.056187,-0.832017,0.348038,3.085732,0.076818,5.240833,-2.111787,5.849372,8.251485,5.581190,-8.385182]],[[-3.040407,6.557766,-5.507120,9.826155,2.666061,-7.129257,-2.337139,-9.726183,7.591395,3.254112,-5.036481,0.375380,8.434459],[3.616578,5.206814,1.164067,2.205019,8.400581,-9.514966,-4.354205,-9.264475,-7.648034,-2.916582,-8.769459,-6.942025,7.604613],[-9.264684,-1.069316,4.868934,-1.901662,8.541924,7.616236,4.791541,9.519903,4.313681,0.326762,-8.340680,2.680542,7.692701],[-1.627781,8.920707,-6.577693,-5.827245,9.478645,7.965461,2.260845,3.212175,1.543777,3.506148,3.147147,-7.101381,-6.068613],[-7.944746,5.204702,5.540305,6.387549,6.183829,-0.830494,5.791152,-3.783273,-1.144896,4.598906,-0.643761,-3.655567,9.523349],[-1.470543,-7.727946,-8.811783,-1.690949,-6.201521,1.390066,-5.013243,-2.092387,0.488820,-5.397088,-7.048140,8.211291,0.119613],[-5.957334,9.711086,0.946660,2.561864,-9.626492,-6.707991,0.315888,-0.264197,-1.796100,-6.059347,-3.639997,-5.850812,9.696526],[2.380464,6.304020,-0.856102,-0.857539,0.091805,3.515824,6.209778,9.208507,3.923769,3.201740,5.375849,-4.470289,-0.242981],[5.414181,-0.326708,1.412769,7.706775,-7.770735,-5.762846,0.595967,-8.247106,-2.507285,-7.347013,2.952017,-7.469356,-8.918686],[-7.400653,9.399527,4.765181,-9.018287,1.561756,8.235912,-5.933940,-6.260622,-6.333913,-8.014462,4.770892,-4.059181,-3.354016],[2.337191,-7.193128,2.376201,-3.201780,0.685762,1.751563,2.119877,0.710830,-5.916768,-9.848766,-0.832302,-4.663817,8.821884],[1.018862,-6.713680,8.161251,6.406407,0.892314,1.698821,3.313750,5.570357,-2.874299,-8.549367,6.793281,7.472532,8.281623]],[[-1.143623,-8.860292,6.375894,7.266454,-6.654230,3.064211,1.003704,-4.294556,4.244376,8.974602,-7.752123,7.114667,-7.413621],[4.010334,7.014220,1.706563,3.309684,5.930627,-5.102353,-6.995381,-2.689167,-2.205398,-8.524093,-2.058185,-2.823991,-9.281487],[4.207414,9.201409,-0.863001,4.955305,-6.936280,2.334086,-6.637025,-8.081363,0.008641,8.217515,9.184293,1.342896,-1.655718],[5.834212,-1.807215,-2.776996,7.628538,9.387580,-7.907023,8.499435,3.217307,-7.296503,-4.384778,-1.808935,1.674438,0.822871],[7.507930,-9.398246,-6.990197,7.921792,8.300663,-4.420009,5.877115,-5.858677,-0.047685,-0.519262,-8.009678,8.357973,-9.140689],[7.478076,-4.849457,-1.248763,2.321890,4.261145,-1.731935,-7.051105,-4.034551,-9.145310,-3.791332,-8.634983,7.457980,8.134971],[3.339635,-6.893817,-8.441090,-4.479413,-5.015784,2.661510,7.406718,5.871690,9.758356,-4.720050,-8.264165,9.879129,3.293794],[9.938638,3.874268,1.084645,4.573600,-3.094920,0.284759,-1.211850,3.043370,8.700658,7.789370,-5.420236,1.262722,-9.103132],[8.845511,-6.296934,8.557799,7.288233,-8.812235,-1.149747,-8.203538,-8.797164,5.600616,6.073408,-0.263066,0.939025,9.222631],[-5.834380,-2.903315,-8.973187,-9.116100,7.481702,-5.262069,-8.430214,2.416031,9.859611,0.747946,4.828279,-2.317857,1.059668],[6.978908,-5.366381,-2.336445,3.154812,-9.443466,2.971871,5.899781,-1.850092,2.386699,-2.218882,1.440268,5.741099,8.178797],[5.000119,6.406800,-2.059536,-9.706731,-0.892174,7.399570,4.727521,9.870240,1.388008,5.215180,3.661834,-3.512613,0.319009]],[[7.486950,8.049482,4.374368,-9.575445,7.400974,-7.768145,-5.417945,8.317651,-7.080523,4.509897,7.024806,-3.134411,-8.245259],[8.280677,-5.122672,5.187150,4.949048,-6.396148,1.449508,-5.594418,-3.458826,-1.509239,8.601609,-8.722050,4.673114,3.975850],[-0.363115,9.160324,5.118569,-8.368125,-1.170042,3.083785,-3.049299,-2.710637,4.054525,-7.333965,4.299672,-2.902428,-3.538505],[4.790965,-7.151855,-7.260312,-9.232695,4.277748,8.239760,9.732643,1.135052,6.756732,3.580808,-3.102010,-3.286075,-2.942807],[9.655934,-4.929154,8.129653,4.071310,9.888792,6.939912,-7.433571,2.372847,-8.421568,9.239327,-5.790489,3.134991,-7.013371],[-4.091449,-6.753689,4.313012,5.772323,-4.541130,7.923402,-7.166784,0.158249,-0.631406,-2.144637,2.074738,2.565333,2.109218],[-8.932711,0.065910,-5.689244,9.243401,-5.105969,-2.085613,0.700097,-1.915883,0.997668,7.235487,-0.554269,-1.592207,9.604782],[4.248974,-4.273664,-3.126201,9.637237,3.868042,8.643881,4.814957,5.077279,5.659199,-6.436908,5.439482,-4.685280,-1.770353],[7.501040,-2.559033,4.977979,7.631356,-2.920784,-8.318702,9.775667,4.782372,-2.316338,-3.764410,-4.069963,-8.202536,3.442758],[-6.938352,-8.421379,2.744899,9.356242,8.620732,3.965933,-6.203091,-6.169399,-6.320501,2.892679,4.746773,-4.883404,7.251297],[4.116049,0.229489,-0.054911,8.095136,-4.968111,-0.923790,-9.405208,-9.562430,-6.503043,0.614335,7.702817,-7.364803,2.294728],[4.322958,2.838469,-3.496277,-2.225221,8.257676,-0.271413,-2.394938,5.675467,-6.152270,-5.086690,-7.595214,-1.380666,8.116674]],[[1.945499,-7.552898,4.119747,-8.166438,-7.021699,-6.767621,-2.668956,5.426684,-5.496250,6.708918,-0.782609,2.055896,6.415575],[2.437023,6.530693,7.732681,-6.792165,0.563440,6.594043,-6.125719,-8.968683,2.212624,2.793353,6.654413,-9.550321,8.786847],[3.413030,3.909094,-5.752944,-4.507363,1.149021,-9.931871,7.304217,-0.736092,6.526794,-4.481731,2.632287,-4.254845,8.410895],[-7.126867,8.619327,-5.009942,-7.931387,3.158166,6.567642,-2.192938,8.173045,-9.654254,-1.009636,-1.073061,-8.472287,1.620898],[-8.228425,-0.612068,-5.582807,6.060359,-6.369410,-8.535639,8.199858,-3.888572,2.497913,5.507017,3.847354,6.333535,-3.711329],[-3.652209,-6.916693,-2.277669,8.915966,-1.881630,1.805346,0.615070,-7.476260,-7.444900,0.827527,-3.638591,8.621499,-2.422103],[2.736029,-2.938318,5.977844,-3.378693,6.629073,-7.256373,6.456831,-3.842265,-9.838776,6.038492,5.406835,-5.039943,-5.852671],[9.750283,-1.625643,-0.985524,4.815977,-5.855413,8.807711,-3.243910,1.968223,-0.040330,-9.282087,-9.602359,-7.975983,7.159161],[6.103380,4.356278,-9.890812,-5.338416,-8.349538,-8.548715,5.018189,-4.966351,-7.564306,2.243354,4.228232,-0.949514,-4.323461],[-5.292349,-5.024197,-0.752422,3.967947,5.524463,-3.895322,-4.657030,3.958205,-3.564319,4.230532,9.336919,-4.615722,-2.970174],[-3.522045,5.310786,6.848995,-8.751739,4.704584,9.237350,-0.092658,-9.499365,-2.134829,3.261490,1.308512,1.077661,-7.704605],[-4.242402,4.733689,-4.926915,-7.675528,3.149720,9.166745,6.626468,-3.029985,3.466837,-3.367566,-0.192220,-9.556861,-1.406958]],[[4.103357,7.965821,-0.740628,-1.211848,-0.011803,-9.995604,-9.189464,-0.040203,2.505576,-5.464413,-7.947061,-8.189388,9.343887],[-5.011766,-9.017549,-2.246515,-5.960358,7.543602,5.701981,-4.274500,-2.976226,-0.810552,-8.767271,-5.275821,5.453897,-0.426232],[-3.843201,-7.978913,0.455982,4.485229,7.298040,5.266123,7.321564,-8.650236,8.636322,-7.976514,3.387869,-3.548903,3.502609],[9.745917,-9.862421,5.710904,-4.637751,-3.823513,-9.822513,8.493259,7.408522,1.248840,3.767268,-0.734677,-1.262494,-4.078392],[4.119506,-0.427864,0.824408,0.451290,7.327268,-6.270445,-4.994541,2.611229,3.955029,-0.228442,1.986936,9.221859,-5.611425],[4.838607,4.962096,-4.728241,1.850827,7.524925,5.394809,-6.455772,3.393983,-1.470961,0.904276,-7.936486,2.856181,-0.444792],[-3.286211,0.714294,7.883800,-8.121068,6.491741,1.730619,6.096713,7.818896,-4.383854,7.172043,1.206203,4.376629,7.984514],[3.252960,9.937608,3.288596,5.556444,-8.893034,-1.065320,7.092096,5.126147,-5.777561,-9.440565,6.783606,4.838742,-5.882927],[8.907381,7.484811,-3.073024,0.893111,-1.636561,7.180125,6.966918,-5.022116,-9.103360,7.378254,9.044743,-6.448115,-7.369139],[-0.030329,-7.599054,-8.070372,-7.448330,-8.900635,-2.371227,-3.527368,6.610703,-7.877432,4.032312,-1.593782,2.546216,-7.366934],[5.399335,-4.964061,-4.101266,2.929922,3.015155,-8.190549,1.556678,-9.528905,-5.318821,7.001257,1.743455,6.063671,-1.581269],[-2.877866,0.181737,-6.512330,-4.445234,-7.218718,8.216276,2.624162,0.322663,0.428667,1.403352,-2.353775,-2.246624,9.539198]],[[-8.541223,9.616592,-4.425492,-6.678642,-3.273294,-4.582365,8.128998,4.155397,-1.959080,1.170509,2.056945,-2.413001,1.285397],[-3.130300,-2.441045,5.264512,-7.967598,-4.398062,-8.528060,5.822262,8.573434,7.102692,-1.281270,-8.772573,-9.771604,4.220282],[-8.302490,-1.903864,-0.693859,2.700662,-7.293024,7.151681,9.189269,6.402513,-0.483751,-1.213770,-7.893291,-0.700683,2.870154],[8.555390,7.939896,3.426076,-8.456313,7.419135,-5.371588,-4.497064,5.038807,-6.170241,4.388181,-9.033787,-2.240029,0.808122],[7.988848,4.375017,-3.488960,-6.286174,0.383010,1.071200,9.088486,7.612637,-9.699987,-4.375762,9.560812,-4.475098,-0.278815],[3.597324,-9.175200,3.565204,-3.610928,-7.515943,3.102090,-1.107504,-5.741998,-2.855426,-2.679999,8.873003,7.746241,-1.818452],[-0.397359,3.472987,-8.787506,2.176887,-0.776066,-1.892925,-3.800202,0.879098,9.321971,-9.720512,-6.662392,0.311569,-9.763547],[8.698411,-2.209358,5.100867,-8.173773,1.879536,7.681661,5.534085,3.931885,-6.341948,-0.287522,5.403548,-2.399773,4.258197],[-8.708072,3.552548,-2.957738,2.982338,0.326191,9.382278,2.041041,-9.802239,-4.280200,-6.887359,5.872983,6.661362,6.016455],[1.652710,-6.941990,-7.935660,8.636641,-8.419788,-9.318337,-4.873664,-1.265646,6.085928,-0.216082,-7.854465,-9.159000,-6.920274],[7.371048,1.228244,-7.405644,-4.829917,-7.684122,6.883332,2.443261,4.932950,1.467737,1.493449,9.457253,-9.111031,-0.869058],[-5.866460,5.438042,-2.456609,-0.935159,5.757912,-0.174782,-7.894013,-0.987297,-6.806989,6.748481,9.800015,4.570059,-8.048421]],[[-2.089310,-2.605630,4.677646,4.603998,6.775142,8.752120,1.596233,-3.907314,8.452501,-2.460667,-9.972840,9.980727,-5.032005],[7.084150,6.971412,0.544488,-6.961872,-0.451246,-8.075116,-4.034947,8.833838,-8.568090,6.790236,-8.460653,2.424901,-1.068799],[6.859905,9.267906,6.312909,4.915402,-4.987676,-5.819800,-4.495522,-5.734497,-8.866126,-2.399044,-3.155018,-2.875241,7.482112],[-2.161032,-3.337820,-6.645950,-4.989552,4.713206,-0.380894,-3.051198,0.603846,6.636877,0.984814,8.805087,8.142915,9.380283],[-0.793311,3.235847,-8.511139,-1.257771,-5.494271,-0.872518,-0.428476,-6.528118,-1.431201,7.426237,7.054602,9.425323,-9.848702],[-6.085695,-4.760260,3.084694,-5.816477,-6.443749,8.334635,3.089844,-7.554399,-1.572047,9.701041,5.161818,-9.981645,-6.155391],[-7.455825,-2.805568,-6.637041,-3.591712,8.246707,6.874812,-9.166673,-3.558466,-5.378587,1.585019,-3.834922,9.149824,6.845494],[5.059061,2.384681,0.668120,-4.946075,-2.559432,3.579407,0.682048,-3.719150,-2.111727,6.954360,-9.373248,-5.089375,-9.179622],[-5.477645,-6.160721,-9.763062,3.652786,2.976650,7.314830,-7.096012,-0.857631,-1.390781,-8.472940,-1.705286,3.075791,-6.042024],[7.155337,-1.563928,8.393405,1.788282,-8.595585,6.168746,4.481377,-0.240024,-4.075021,-8.384346,-1.769993,2.451245,-0.425610],[8.829511,5.484708,7.243798,-1.687553,-7.740527,-8.271771,-3.618291,4.665585,-3.784101,-4.414212,-2.109881,-5.718185,-6.714775],[6.702882,0.849714,8.073189,-2.653380,-1.094728,-9.485955,4.711763,-8.207070,-2.447531,-6.777608,2.921208,0.173016,9.790735]],[[-9.669796,-3.593074,4.311066,-3.572328,2.360064,9.138086,-7.706263,-6.300195,0.447636,4.603402,2.158771,-0.700040,-9.761314],[4.350627,0.360168,5.593242,-4.692342,-3.422989,0.990833,-4.612963,9.671731,-9.736754,-0.527122,-3.158824,-7.785436,3.924945],[7.283667,9.196975,9.723999,4.027975,-9.616682,1.457223,2.256504,-2.145229,-8.870463,9.988815,-1.992083,-3.731800,-3.042587],[-8.345058,-4.490214,5.174725,3.872678,9.350022,6.345361,-3.836195,7.308566,-6.271406,0.065099,-4.666058,5.774583,2.950744],[3.222699,-7.483677,-5.546302,5.995857,4.793188,3.908898,9.549202,7.740560,3.089465,-4.667196,2.250847,2.122052,4.443227],[9.787829,-5.464209,3.941833,-1.649118,6.604793,-2.641684,5.572463,2.367451,3.191860,-8.405988,9.398299,-2.074213,-4.276344],[-8.098548,-3.120298,0.403535,1.836219,1.186683,-3.125633,-6.429713,-8.373401,-7.171712,-2.448536,-9.317606,-9.852149,9.895723],[5.872975,-5.101897,0.405871,5.454422,-0.969151,7.642954,-0.635896,-9.612554,-5.960080,5.784408,-9.425513,6.922836,1.352752],[-3.679623,-9.379680,-8.256598,8.477500,5.977995,6.753102,-1.793835,-3.787023,2.872133,-9.706778,4.380889,6.927906,-4.036437],[-5.709033,-3.847800,5.805724,9.839514,-0.641144,6.284934,-8.076917,2.085079,-8.722543,-5.365977,0.376868,7.759675,6.485440],[1.029201,9.938010,-1.782334,3.329733,-9.898596,4.327307,-9.756059,3.972780,7.036880,-9.840409,2.453137,5.121711,5.773652],[-2.124434,-1.624870,7.509624,-5.781076,5.914601,-7.163296,7.241727,-4.098818,5.548230,1.708240,-1.858474,-3.342955,3.217871]],[[3.695290,3.109888,6.279421,-7.498598,-3.478794,2.477658,-8.396705,5.964470,7.663421,1.929815,-2.491336,-9.997741,9.071172],[-6.753542,-1.597324,-7.668274,-2.376202,-9.410544,4.339173,-2.645889,8.581665,-8.178891,-0.245796,-6.978588,-4.276614,5.303308],[-5.448320,-1.099287,5.485515,-4.700415,-2.034254,8.110045,-3.763193,6.322262,-3.618966,4.412372,9.654467,-4.299328,-3.955766],[-8.365160,-0.725350,8.235474,1.843046,6.268269,-0.865843,-5.499549,-5.926299,-7.105951,-4.914411,-4.116699,6.455090,-6.195366],[1.044161,-3.113749,0.444882,-5.688819,1.547305,8.123629,-6.863247,2.212221,-7.266679,4.939914,5.620179,7.090932,6.033595],[7.202400,-2.787614,-6.688944,-7.902538,7.889778,2.416007,2.356339,2.421411,2.896686,7.600305,-8.975977,7.556547,-3.839060],[4.711677,-0.222182,3.770153,5.741308,2.732041,0.409722,0.256259,0.491398,5.829998,1.705977,0.542931,-7.745271,8.373012],[-9.975337,-6.935985,4.319018,5.300696,3.332950,6.291318,-9.696100,-0.704015,-5.306599,-8.183965,-1.959212,6.827671,-5.696103],[-1.293706,6.955462,6.633550,-7.182507,4.092865,-4.168083,9.864403,1.287752,-9.844863,7.170296,-2.602334,-3.194752,-0.712827],[-2.707920,-3.184360,-5.040349,7.820030,-0.093176,-3.382222,-2.971033,8.961878,-5.455734,-4.774560,9.866190,3.161983,5.223630],[4.985303,-4.343868,-9.467000,4.457109,6.933033,-3.816544,4.590337,7.435743,9.735093,3.032381,-1.815959,-6.304415,-8.727684],[-0.301135,-4.083616,9.764698,7.343642,6.181450,-3.885328,8.032913,8.800803,-4.244003,-9.896634,-5.777485,3.861633,-9.353484]],[[2.911867,2.691253,2.560011,8.665882,8.363275,8.060619,-6.285892,7.042700,0.591476,-2.497483,-8.454081,9.791519,-3.789753],[-0.740492,-7.881304,-1.085525,1.677537,8.845464,8.261087,4.023105,0.009718,9.703053,6.272885,-7.818946,5.882675,6.106790],[8.006453,8.705745,-9.955155,2.873718,-0.332353,-0.428922,2.339696,-1.956346,-2.509934,-1.722888,-3.822884,8.721563,-0.046435],[-8.826764,-2.862153,9.656785,9.780220,-0.207457,-5.343317,-3.195839,6.119126,9.030593,-3.405114,2.072211,5.645511,-7.955500],[8.107164,8.546843,9.317767,-1.966781,-4.350179,0.692633,-4.631297,1.615393,7.994323,1.739072,4.334202,-4.432113,8.621495],[-2.939766,9.781010,-8.493350,4.151588,-7.503557,-5.865107,-2.285978,-3.146715,-1.345351,3.614692,4.799476,2.807255,6.118713],[6.418142,-9.361646,0.167781,7.982877,6.947380,-2.025892,-9.121272,9.599832,8.022421,7.487280,0.193102,-0.647409,7.393300],[5.831499,-0.814449,6.260333,-1.366689,-3.836047,1.340310,-9.348707,-3.772105,0.635097,3.558267,2.535529,-8.018272,-6.567150],[-6.304526,3.758699,9.129074,-2.739178,9.934504,6.789377,8.269820,-1.186031,-6.834849,7.002277,1.255507,3.495807,6.363588],[7.643984,6.406179,1.146590,-2.437044,7.370814,9.061530,4.111649,-1.042078,8.576844,6.463355,-2.445255,-7.829712,-0.201870],[-4.851428,6.427718,-8.709947,1.552990,-4.429687,8.549434,2.806963,-6.483441,-3.631382,-5.441586,5.596397,-0.147985,0.711826],[-2.458573,-5.203083,3.718476,-2.205018,-9.085463,5.457447,-7.310146,-3.085845,-6.243039,-1.392173,-3.479218,-8.736141,6.283435]],[[-0.615732,-6.516736,-4.330842,-3.214620,7.050627,8.489023,-1.536102,-4.190595,-0.273499,5.762377,-7.920382,-7.290629,1.861302],[9.385416,7.074527,5.982197,-0.090827,2.207307,-3.237361,2.724223,1.811481,9.693258,-2.219758,0.078112,-1.762000,4.401750],[-2.239672,3.654787,2.390761,-4.510237,-1.879998,-9.367106,3.277537,3.029500,3.670860,-7.574829,-3.503307,-6.803972,7.298131],[7.677418,8.963560,3.941668,-2.636549,5.798661,5.720405,2.555134,6.323587,9.211581,3.826453,-0.827291,6.559049,-4.399024],[-0.232102,0.262632,-3.250833,0.537470,6.893250,-4.531161,1.905862,8.882744,0.700264,-6.893939,3.253527,6.533076,4.710295],[9.029477,-8.199078,-5.727924,1.989077,9.879867,-5.191132,3.887211,3.718030,2.718597,5.633443,3.645998,0.178039,8.360489],[7.372110,-2.702805,-9.487824,-4.597190,8.423904,6.420502,-1.568982,-4.800221,8.768114,-2.445701,5.386568,5.467677,1.543204],[2.691469,0.477109,0.443720,-4.201431,7.338012,0.802765,0.216032,-0.233647,8.567301,5.910956,0.325042,2.771200,4.934723],[9.270059,2.113715,-5.498502,-8.931682,6.712735,-8.523744,4.013343,-5.726153,7.914392,1.294905,-9.250654,-2.929566,-9.887258],[-1.545705,-0.423072,7.652854,1.409656,-1.675683,5.801581,2.610582,-2.819586,-6.091487,0.080218,-2.051519,5.906841,-2.767580],[1.449583,2.489541,-0.302174,4.398743,-9.440002,-4.267664,-2.270852,3.186070,3.893702,-8.059133,-4.031616,5.873817,-1.806561],[0.674648,5.520627,1.994984,-4.327849,0.738791,1.827992,0.916136,4.523193,6.576465,-5.112838,7.099987,0.598123,4.146478]],[[2.906960,9.173912,6.236774,5.317239,-0.640962,9.647504,8.595787,4.115250,9.331338,-7.449590,-4.280590,-7.072806,-9.403810],[4.110856,-5.980321,-4.179073,8.168853,3.546662,-5.092048,-0.949416,2.324707,8.207976,-3.585063,4.423266,-6.588059,-1.045776],[0.761535,8.243100,-5.199647,5.020023,-9.579161,-2.326434,3.807682,-4.402191,-8.827895,-4.473593,-4.141409,8.720812,-7.153925],[-2.582936,-1.882197,-5.714731,-9.628297,-1.627662,-5.486747,6.237047,3.496956,-5.846464,3.987499,-2.049226,0.161744,8.485044],[-9.150683,-2.924994,-7.683865,7.262219,2.320994,-8.802235,-7.926169,1.686970,0.581716,2.708059,-0.710124,0.647018,-4.268440],[-0.454686,0.972991,8.303285,-0.996610,-6.350943,-7.607192,3.806617,5.766538,9.559748,-2.451326,-3.960572,2.801063,-3.269411],[-8.953150,9.720091,3.583151,-9.419630,-6.956312,6.536739,-9.204630,4.289470,4.271084,-2.597440,-4.964552,-3.048406,-6.848049],[-4.127945,-8.978017,-4.997065,1.172362,7.615526,5.728867,5.066004,9.287423,-5.747267,-6.010872,3.958449,-5.518589,1.618399],[7.924800,-5.513309,-8.923866,-8.582372,5.113514,1.870073,-9.100655,-7.324580,4.280447,3.089627,-5.598473,-6.875372,6.654971],[-2.485861,1.335687,3.464129,-1.357283,6.117501,-0.700438,1.936330,-7.480320,-4.593234,-3.492393,-8.074505,-3.744848,-4.340624],[6.223221,-9.378515,-8.192761,-0.581013,-3.261908,1.783767,3.271784,4.784095,-6.289956,-9.303350,-7.174971,9.631760,5.697184],[-9.782523,-5.437428,-9.437794,7.542088,-7.912393,4.899771,7.880622,-2.753476,-8.562565,9.662167,-9.808460,4.386156,-4.788581]],[[6.273735,-8.690198,1.159950,7.270103,1.037868,0.336290,-9.818255,0.871045,2.552582,5.188560,6.797588,1.416431,9.400682],[-3.967819,-8.124353,-9.450133,-7.405387,-4.131585,7.613397,8.297575,0.164841,8.706751,8.394228,-5.754696,-3.686563,-8.748400],[6.483643,-7.021170,2.585005,0.732478,-7.210633,-9.727970,-0.964073,-3.142516,-1.473315,7.945437,9.802571,7.984959,2.719895],[3.846168,5.537338,3.773290,7.418262,7.720809,-4.248063,8.928480,2.858779,8.880600,-6.137710,4.584108,-8.764056,8.411160],[-3.369955,-7.468793,-1.297982,7.898724,2.405398,-6.943628,-0.481414,-1.850884,3.518260,8.087326,0.880237,-8.189081,4.200198],[-8.475614,-3.665127,8.211032,-4.642497,-7.159289,8.725782,-4.495905,-4.956687,9.216922,-5.370365,5.332451,8.685466,-2.599957],[-1.486922,1.097683,0.390296,0.402336,8.544326,-5.896600,-4.378094,-1.768801,-5.152498,-3.408222,1.725052,8.442543,4.296627],[6.913102,-9.391012,0.812949,7.574422,-9.892041,-7.128453,-4.782432,-4.638388,8.781029,-4.039330,-7.704364,-0.010075,9.325945],[-8.504229,-7.768691,-9.410766,2.952588,9.364855,1.595206,6.553852,6.214832,0.977494,5.504553,-9.887518,-5.948874,-8.630094],[0.922308,8.095676,-4.582801,-9.878876,-8.604197,0.942962,2.665184,-6.979631,3.787499,-4.054297,-3.058220,-9.754070,8.425667],[-2.783070,1.495760,-8.720960,-6.705242,-2.484003,0.153856,5.376279,6.176078,6.476207,6.229702,6.286892,5.060086,-7.935583],[9.216721,2.426653,8.599074,-4.825409,-8.309813,-6.498033,-4.986994,-8.536739,9.181337,8.326499,-3.718121,9.103950,7.381597]]], dtype = "float32")#candidate|3472|(16, 12, 13)|const|float32
bop_3473 = relay.multiply(call_3460.astype('uint32'), const_3472.astype('uint32')) # shape=(16, 12, 13)
bop_3476 = relay.multiply(call_3461.astype('uint32'), const_3472.astype('uint32')) # shape=(16, 12, 13)
output = relay.Tuple([bop_3473,])
output2 = relay.Tuple([bop_3476,])
func_3481 = relay.Function([], output)
mod['func_3481'] = func_3481
mod = relay.transform.InferType()(mod)
output = func_3481()
func_3482 = relay.Function([], output)
mutated_mod['func_3482'] = func_3482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3503 = relay.var("var_3503", dtype = "uint16", shape = ())#candidate|3503|()|var|uint16
const_3504 = relay.const([[[-1,10,-7,-6,-2,6,-3,10,-10],[9,-3,-7,1,2,-10,1,-9,-5],[-3,-9,-5,2,3,6,-6,-5,2],[-6,7,2,-4,9,3,2,-6,-1],[-4,-1,-5,-2,3,-4,1,-9,-9],[-4,-5,10,8,6,-1,-4,-9,5]],[[1,-9,-7,1,-2,-4,1,-7,2],[6,7,5,8,6,4,3,1,2],[-4,5,1,-8,1,1,-3,5,-9],[-10,10,4,9,1,-9,7,-4,-1],[4,-9,5,8,9,7,-4,2,-3],[7,-4,-2,-1,-8,1,-2,-9,10]],[[3,1,3,-9,-5,2,7,-1,-10],[-4,10,-8,9,6,10,-1,5,-6],[-2,-7,6,-6,-3,-4,8,5,-7],[-10,10,-6,3,-5,1,-1,8,1],[-9,9,-4,4,10,-1,-10,-7,9],[3,3,4,-1,9,3,5,7,-4]],[[8,2,-9,9,3,2,-7,6,4],[4,-3,9,2,-7,-10,9,-1,8],[-1,-1,-2,8,9,9,-2,-1,7],[10,-3,-10,8,-3,-8,8,9,-8],[4,2,8,7,8,4,7,7,-10],[3,4,-6,-10,-6,6,1,7,-1]],[[5,-6,5,8,-1,2,-10,9,2],[10,2,2,-9,-9,-4,-3,10,4],[9,-7,-7,-4,-3,-2,-8,8,10],[9,-3,-8,-1,-8,10,4,1,2],[10,4,-8,-10,-1,-8,10,-10,8],[-10,9,-7,9,10,5,-8,7,8]],[[-2,-2,1,-4,9,-6,2,-5,-5],[3,4,-3,-5,-3,7,-10,2,-2],[3,-5,-9,-9,-8,-3,-7,-6,10],[-1,2,-9,-5,-8,2,1,-5,8],[-7,5,1,6,-4,10,-4,9,3],[7,-9,-7,6,-6,2,4,-1,3]],[[-7,-10,3,-7,1,5,5,3,6],[5,-8,2,5,9,5,7,-5,4],[-7,5,6,1,1,-7,6,8,3],[3,-5,3,6,-1,7,9,6,-1],[3,6,-7,-10,3,4,9,7,10],[4,-9,7,4,-9,9,3,-1,-3]],[[-9,1,2,-1,3,-4,7,-10,-7],[-2,10,-1,3,-10,-4,5,5,-9],[-3,7,8,10,-3,4,7,1,9],[-8,-8,9,9,-7,-1,-3,-5,-10],[-6,-10,3,9,10,-9,3,-1,6],[-3,5,-1,-6,-9,-7,-6,3,1]],[[8,8,-1,-6,4,7,9,-5,2],[1,2,-9,-10,1,-10,9,-2,7],[4,10,-3,10,-9,-8,-2,-8,-8],[-3,-3,2,-7,-3,-10,4,4,-5],[-1,2,-9,2,9,4,-7,6,1],[3,-10,7,-5,-5,-7,9,-5,-9]]], dtype = "uint16")#candidate|3504|(9, 6, 9)|const|uint16
bop_3505 = relay.logical_xor(var_3503.astype('uint16'), const_3504.astype('uint16')) # shape=(9, 6, 9)
func_3408_call = mod.get_global_var('func_3408')
func_3410_call = mutated_mod.get_global_var('func_3410')
call_3525 = func_3408_call()
call_3526 = func_3408_call()
func_2785_call = mod.get_global_var('func_2785')
func_2788_call = mutated_mod.get_global_var('func_2788')
call_3531 = relay.TupleGetItem(func_2785_call(relay.reshape(call_3525.astype('float64'), [4, 5, 3])), 1)
call_3532 = relay.TupleGetItem(func_2788_call(relay.reshape(call_3525.astype('float64'), [4, 5, 3])), 1)
func_3369_call = mod.get_global_var('func_3369')
func_3372_call = mutated_mod.get_global_var('func_3372')
var_3541 = relay.var("var_3541", dtype = "int16", shape = (2288,))#candidate|3541|(2288,)|var|int16
call_3540 = relay.TupleGetItem(func_3369_call(relay.reshape(var_3541.astype('int16'), [2288,])), 4)
call_3542 = relay.TupleGetItem(func_3372_call(relay.reshape(var_3541.astype('int16'), [2288,])), 4)
output = relay.Tuple([bop_3505,call_3525,call_3531,call_3540,var_3541,])
output2 = relay.Tuple([bop_3505,call_3526,call_3532,call_3542,var_3541,])
func_3555 = relay.Function([var_3503,var_3541,], output)
mod['func_3555'] = func_3555
mod = relay.transform.InferType()(mod)
mutated_mod['func_3555'] = func_3555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3555_call = mutated_mod.get_global_var('func_3555')
var_3557 = relay.var("var_3557", dtype = "uint16", shape = ())#candidate|3557|()|var|uint16
var_3558 = relay.var("var_3558", dtype = "int16", shape = (2288,))#candidate|3558|(2288,)|var|int16
call_3556 = func_3555_call(var_3557,var_3558,)
output = call_3556
func_3559 = relay.Function([var_3557,var_3558,], output)
mutated_mod['func_3559'] = func_3559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1286_call = mod.get_global_var('func_1286')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_3602 = func_1286_call()
call_3603 = func_1286_call()
output = relay.Tuple([call_3602,])
output2 = relay.Tuple([call_3603,])
func_3620 = relay.Function([], output)
mod['func_3620'] = func_3620
mod = relay.transform.InferType()(mod)
mutated_mod['func_3620'] = func_3620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3620_call = mutated_mod.get_global_var('func_3620')
call_3621 = func_3620_call()
output = call_3621
func_3622 = relay.Function([], output)
mutated_mod['func_3622'] = func_3622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2578_call = mod.get_global_var('func_2578')
func_2580_call = mutated_mod.get_global_var('func_2580')
call_3632 = func_2578_call()
call_3633 = func_2578_call()
func_2344_call = mod.get_global_var('func_2344')
func_2346_call = mutated_mod.get_global_var('func_2346')
call_3646 = relay.TupleGetItem(func_2344_call(), 0)
call_3647 = relay.TupleGetItem(func_2346_call(), 0)
var_3662 = relay.var("var_3662", dtype = "float64", shape = (4, 5, 3))#candidate|3662|(4, 5, 3)|var|float64
bop_3663 = relay.floor_divide(call_3646.astype('float64'), relay.reshape(var_3662.astype('float64'), relay.shape_of(call_3646))) # shape=(4, 5, 3)
bop_3666 = relay.floor_divide(call_3647.astype('float64'), relay.reshape(var_3662.astype('float64'), relay.shape_of(call_3647))) # shape=(4, 5, 3)
bop_3667 = relay.multiply(bop_3663.astype('uint8'), relay.reshape(call_3646.astype('uint8'), relay.shape_of(bop_3663))) # shape=(4, 5, 3)
bop_3670 = relay.multiply(bop_3666.astype('uint8'), relay.reshape(call_3647.astype('uint8'), relay.shape_of(bop_3666))) # shape=(4, 5, 3)
output = relay.Tuple([call_3632,bop_3667,])
output2 = relay.Tuple([call_3633,bop_3670,])
func_3671 = relay.Function([var_3662,], output)
mod['func_3671'] = func_3671
mod = relay.transform.InferType()(mod)
var_3672 = relay.var("var_3672", dtype = "float64", shape = (4, 5, 3))#candidate|3672|(4, 5, 3)|var|float64
output = func_3671(var_3672)
func_3673 = relay.Function([var_3672], output)
mutated_mod['func_3673'] = func_3673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2010_call = mutated_mod.get_global_var('func_2010')
call_3721 = relay.TupleGetItem(func_2009_call(), 0)
call_3722 = relay.TupleGetItem(func_2010_call(), 0)
func_3192_call = mod.get_global_var('func_3192')
func_3195_call = mutated_mod.get_global_var('func_3195')
const_3733 = relay.const([0.883574,-1.276600,-6.505531,8.861153,-4.585398,-9.584035,8.944996,4.520711,-5.887955,-2.423259,-3.916552,5.773045,-7.345456,-6.928544,-2.490520,-3.282897,-6.567972,-3.651474,6.790819,3.304460,4.216693,3.985478,1.770029,8.584450,7.023169,-0.527235,-0.381797,-0.609707,-9.339532,-2.171043,-6.231119,-9.842444,-5.501644,6.536717,-2.050093,5.222966,-2.851206,4.125239,0.156324,-1.130072,-2.371847,-9.022643,-7.959161,4.750957,6.359576,8.267749,1.416071,4.140809,-9.053524,1.273591,3.270234,9.810365,0.117298,0.291879,1.648068,4.857542,-3.816371,8.410963,1.681234,4.628074,-3.695027,-8.199935,8.420359,9.510752,6.292038,-2.587301,-2.844515,-0.451098,-7.258494,-2.752289,2.422315,6.143600,-1.831014,3.324127,-9.581353,-4.032435,2.946560,-3.194991,-7.337854,5.068662,-4.069281,-0.298661,2.829601,6.239348,-9.204228,0.758336,6.338731,-2.447256,0.621359,3.039219,-3.985543,5.644318,2.352225,-6.207322,6.516428,3.270587,-3.944161,-4.931395,-7.144039,0.794525,-7.714184,9.377034,-4.400640,6.221519,7.656100,8.236375,-8.897331,6.506147,-9.050324,-3.288114,4.252097,0.706172,8.276261,6.651063,1.898801,9.822262,-1.346462,-6.564943,-7.716252,-5.893732,-0.420286,6.127155,-6.448999,-2.375802,3.628066,2.947707,-4.085784,-0.770526,-2.345246,-1.446383,-4.857053,9.078483,-7.669109,8.030980,5.092409,-5.839820,9.107106,7.518274,-2.253445,-9.687831,-0.726758,7.676785,8.977897,-3.919718,8.785166,0.236145,-5.192128,-9.497338,-6.183851,5.120893,-5.632890,-8.233236,-3.459432,3.618954,9.668585,-6.757937,9.755256,6.042842,9.611599,2.265328,-7.988367,-3.256426,0.938261,7.415384,1.845767,-9.879468,-6.852064,7.793791,-8.551612,5.867219,4.855754,9.575705,9.413286,7.072646,-8.542653,-8.934273,0.833342,-8.115458,1.051845,9.060043,-6.239964,-9.819356,-6.693783,2.842924,0.266686,-4.496569,-5.370165,1.758894,-9.594515,-7.104072,3.790156,2.879489,-7.627225,-7.420878,4.864704,-6.950158,7.736338,-8.801820,-0.407737,-5.561124,5.960857,-5.891811,-1.357220,5.757821,-4.859439,1.637069,-7.119552,1.839247,-8.299585,8.423222,1.155605,-2.325694,-0.311022,-0.190805,-8.681793,-7.603346,5.458289,-8.464466,5.333101,7.415546,0.524902,9.151764,4.148386,-5.830883,-1.803224,-0.865859,6.751988,-1.140071,9.660941,5.005068,6.099979,9.852462,-0.767335,-5.687998,-5.621530,-3.037003,5.021489,3.307898,-8.349584,-6.156026,5.119948,-3.936034,4.971057,8.146909,7.545215,7.630535,-7.564483,6.986559,-1.292050,-9.645963,6.488405,-4.467435,4.254674,-3.336657,-6.813012,-3.930351,5.075387,-8.259704,-5.468665,0.599949,-8.876125,-2.019427,-9.728060,-9.942019,-0.669043,1.629497,5.780441,-1.157111,3.236987,-7.269316,7.237265,-1.106537,2.037033,-2.598465,-8.940337,6.090731,-3.537925,9.034475,7.400828,1.312144,3.250782,-9.238235,-0.823809,0.576435,6.599457,9.123178,-4.922112,2.210623,4.029681,3.399523,9.028442,-0.183387,4.746068,-0.927465,3.630101,-5.435875,-4.410207,9.991181,3.574258,5.519529,-2.560012,7.209476,-3.258155,-0.922127,-0.998085,7.498726,-9.238262,0.393752,4.941486,4.790449,4.279293,8.886351,-6.622544,9.446341,8.171616,-0.920599,6.096240,4.430937,-3.927189,3.722363,5.671464,-7.211937,8.011568,1.346553,-1.981327,3.728471,-9.212604,6.400659,-2.792392,-6.985944,0.618421,8.070436,0.370113,-2.953966,3.982722,-8.493614,-9.865948,-5.359452,2.669549,2.276965,-3.589479,9.933127,0.731912,3.151358,8.502610,-0.355014,-2.443238,-3.871698,-6.556586,7.020147,-5.601138,-3.584609,7.047144,-1.140697,3.275700,-9.410693,7.205177,-5.270580,-6.115388,-7.286218,-8.280631,4.213391,-7.336211,-5.792526,-5.989808,-6.469919,2.037578,-1.341749,-5.565912,1.938324,-7.184204,9.122508,-9.427872,-7.198028,-8.779442,-9.773310,8.296299,1.182882,6.925479,-6.631010,-4.822460,7.301687,-8.306684,-7.266023,-8.447531,-4.139725,5.220501,-8.852457,0.454571,-0.818010,3.123156,-9.154928,-2.948144,7.491474,4.745896,-7.310289,-3.523935,-4.589092,6.025771,7.885752,-1.481932,-8.235429,-3.543470,0.678563,1.692008,8.240962,3.107912,-0.484897,4.157062,9.316711,1.978785,-6.958372,0.871671,-4.044965,7.887749,9.653397,3.115340,0.878684,-4.602104,-1.957107,4.292085,7.948263,6.592951,-1.886893,0.470340,-3.715350,5.590854,-5.674317,5.948054,9.773373,6.584910,-6.747276,-3.140175,-5.860243,5.123559,7.297126,-5.940150,5.605578,-7.804707,-8.716310,8.703850,-4.637684,-0.910009,-4.557276,-4.523098,-0.515646,-7.941620,-5.229441,8.214351,9.538590,2.026347,4.902495,3.411160,-0.356901,-0.508560,2.628497,3.592995,1.229011,1.061355,4.865407,9.656909,8.850828,-4.096177,5.525719,-8.658309,-3.767983,9.061714,6.736812,-8.182658,-9.437362,-4.789327,2.035819,9.273105,4.782797,-5.239669,-8.825459,4.937654,7.077694,-8.050845,2.202635,3.809996,-3.965492,7.656361,-3.947911,9.281966,-6.809507,-4.650152,9.853867,-2.561516,-9.392568,1.433500,6.037426,-7.599041,7.744590,1.878793,5.381769,-6.879164,4.924363,5.794212,-0.777938,-7.229783,0.944781,-2.753924,-6.508279,7.206744,5.703643,-8.458570,3.861721,2.420600,3.942726,3.793225,0.440214,-8.741622,3.503075,-7.504943,9.854282,2.359524,-9.186322,5.174516,-2.028967,9.618166,-2.566282,-2.578369,8.347063,-9.618403,-8.063334,2.922190,0.287095,-9.453066,-2.993523,-1.583543,0.797580,-3.795212,9.815234,6.684261,-3.310373,2.115583,-1.812158,6.581402,7.168910,-6.612194,8.548069,-1.322352,6.832494,-3.165037,8.468338,8.715926,-3.810544,-3.899179,-2.828044,9.396486,2.094181,2.449338,3.058049,6.425371,-8.201209,-6.372329,4.346570,-0.318582,-9.436272,-2.144076,-9.946082,-7.989360,0.716210,-7.499743,-2.510466,7.905860,0.389673,9.055485,4.966139,8.662730,-5.321637,1.513478,-8.485532,9.962250,-3.275208,1.416990,0.119984,9.413747,-6.561451,-2.152119,-2.412229,-3.536973,-3.375245,-4.456561,-2.266071,6.089620,0.787971,7.256214,4.113640,-5.435199,-5.197352,-5.069810,-2.269485,2.411833,6.097833,0.986686,5.793954,6.732220,-4.329507,1.266516,-0.120098,7.705671,2.661418,5.287388,4.274449,3.590982,4.524414,-7.852631,3.164441,6.565656,0.759416,-0.425357,-7.611841,2.509980,0.358452,-3.980082,1.500328,-8.625379,-6.020718,3.317045,9.798733,0.161063,-9.770514,-6.249914,3.910341,7.590098,6.921566,0.349184,1.835949,-1.634417,6.743187,-3.345333,-1.309990,-3.028057,7.024661,5.349238,-0.822480,8.964091,-0.272116,-1.238571,7.970598,-7.486681,-6.209207,1.869617,-8.791117,-6.714960,-2.164840,3.750408,1.567511,0.096170,3.887261,-2.299773,3.353276,3.395700,8.237748,-5.871153,7.204112,9.161268,-4.478469,7.124359,-0.274405,8.043686,4.783888,-9.628441,-5.742483,4.513065,-1.948094,3.975570,0.023767,8.151761,-8.880329,-2.051874,-3.418404,5.361594,-9.757311,-8.206423,3.712286,6.342242,-9.968575,0.324069,7.427678,-0.462578,-4.643245,9.665988,-9.389548,7.395253,-3.162505,-4.771762,2.231360,-3.801710,8.868643,9.484819,-1.855760,4.993010,-0.779874,5.723165,9.758203,6.858745,4.958317,1.493930,5.139690,-9.082049,-4.107621,-9.489667,1.237149,8.997124,3.454682,4.355851,6.928667,-3.200719,5.197169,2.487328,-9.917979,8.067511,-7.493888,8.740677,3.635361,7.960431,3.603847,7.239061,-0.827081,1.976843,7.377325,4.120800,6.947938,-9.975428,7.975413,2.356674,-2.116774,0.307074,6.470625,-0.863563,6.420603,7.883384,-0.694047,3.221370,9.537484,-5.904152,4.266918,-9.691120,-0.701016,9.542559,-2.548057,1.229822,0.649604,4.515142,7.680610,7.134939,-4.155305,7.986873,-7.556275,9.282177,3.390115,-4.446764,-9.909718,4.808383,-4.851190,-3.406254,9.754037,5.097819,9.376615,-3.927406,7.808729,8.028515,-9.399048,-6.805087,8.275332,-4.035726,9.766524,8.263744,1.293910,-9.173675,8.937021,0.526419,-8.289452,-6.913908,9.420247,2.293974,-0.271651,-9.074452,8.526967,2.692118,5.572375,-7.296020,4.057380,-8.310782,-9.508505,-8.948846,0.076227,8.345822,-2.525648,0.437554,-4.360262,-7.354402,1.381006,9.873478,1.823366,3.075655,-0.789436,-9.195845,0.869418,2.447169,8.283323,-8.982997,1.344836,0.259970,0.909035,1.934353,8.343669,-1.889392,9.636734,8.633086,2.300423,9.051234,-9.792796,6.999224,-6.654727,-7.431156,-1.665024,-2.561522,-1.144418,6.854860,3.399901,5.315167,0.573110,6.848033,3.712197,7.774488,-3.339973,-3.732224,-7.012619,-5.805412,-2.793981,0.030749,1.908223,-1.935811,2.746964,5.590929,4.393229,4.595935,2.095924,8.701020,0.027053,4.982391,9.909754,7.913003,5.343756,-8.074586,-2.777474,-5.295022,4.302367,0.254599,-5.337876,3.243864,0.982119,-4.682631,-5.158184,9.600720,2.960759,8.677484,-2.024398,-8.891999,-4.561625,-1.134598,-4.693462,7.324691,5.010720,-9.527057,4.728728,3.898187,-3.184916,0.648177,0.639591,8.670680,1.810178,8.578573,7.622435,8.221865,-5.835470,-1.503076,-6.838501,6.543780,-4.950040,-8.790450,5.729872,-2.629624,0.226757,-2.192286,-8.329424,2.969533,-7.020735,8.556910,8.989864,-3.362089,-4.103857,-4.822924,-9.718005,5.894035,-2.782892,-7.231582,2.592495,1.373284,2.247445,-3.344102,6.235013,8.335695,-8.062185,4.715714,-6.803590,-3.380389,-0.914590,0.351596,-9.670238,8.521343,-0.534933,-5.770663,-0.567204,9.323050,-8.056143,2.243676,4.344537,4.773780,-1.415653,6.019358,-0.593468,9.630564,8.890452,1.966919,4.480493,-4.292580,3.718486,-5.142772,-1.068524,7.362658,2.059435,8.318320,7.075555,-6.015912,0.041028,-0.576851,7.799700,3.233049,7.320337,-5.788453,5.543046,-6.206244,-3.220711,7.366681,-8.364615,1.083227,7.317210,3.425508,2.161104,-2.704326,1.863717,2.218317,7.856920,3.993632,4.576387,6.916190,-2.331763,9.503325,-8.675843,-2.227760,6.438844,-7.120532,-2.597113,-1.219941,-1.847923,-5.495505,7.919523,-1.039963,-1.377750,7.228692,-0.968927,3.048210,8.228610,0.091249,8.653586,-3.488116,0.075605,9.669964,-0.852456,3.763686,5.478802,7.311730,2.024475,8.467000,1.968272,-3.443780,5.354634,6.639207,-4.752046,4.035959,-7.850474,2.585655,-6.374826,4.465595,-3.866797,0.043627,-3.261540,-0.875333,3.957800,-0.814240,8.410587,-6.517750,-3.941761,0.757321,-3.072664,-9.404605,-2.607274,-5.196208,-0.052589,-2.056365,-4.485716,-2.129592,-5.077098,9.131413,-8.560837,-9.794046,-2.522914,8.732383,-3.101408,8.770801,2.009624,2.104389,8.074379,-9.096523,6.022578,-6.112595,5.589301,3.674325,-3.886458,3.334160,-0.079679,-7.875905,-1.536501,2.382279,-0.101059,3.787647,-7.755887,3.205933,-9.642984,9.288067,-0.105864,0.494059,8.426319,5.321766,2.272222,-5.595391,8.575622,-3.726418,-1.627897,-0.123685,7.661736,-0.628150,9.628715,4.632707,-6.518500,9.725363,2.692359,-4.216729,2.523526,-3.732663,-2.533790,-7.810845,3.388763,2.981832,-1.197516,-7.630330,4.907852,8.394911,-9.966849,-5.748998,-7.035436,-8.815816,-6.337285,-4.201720,-2.617405,2.463732,2.980415,-8.978449,-5.805323,3.816395,-5.643945,-9.001006,-8.012956,-8.460367,2.266328,6.035448,-9.066272,9.651331,-4.976447,7.660672,-7.938283,0.446855,-3.634149,-0.183041,2.692213,-1.537319,4.362800,0.705978,-0.220382,-8.705510,-5.735586,4.049732,1.224204,-3.691465,-5.488832,7.022051,-5.117855,3.619873,-8.671020,6.747124,0.066644,4.547955,7.931013,-4.200608,-6.751785,8.341526,7.758417,-1.867073,8.096072,-8.400200,-9.774445,-7.399696,2.353395,9.879116,9.727138,4.291593,-1.707349,5.178971,-9.689104,-7.735102,-3.490461,7.228444,-3.878939,3.753188,-4.495467,-7.481652,1.084935,8.177829,-4.460627,-6.331802,-0.870793,-4.988005,5.048870,-0.870335,0.938563,-4.854631,-0.413331,0.217359,7.150061,-2.380077,5.412401,-4.491757,0.512739,9.957162,3.056495,2.860404,0.791226,-6.625901,3.746095,-1.070309,5.434612,-8.169623,8.507498,8.251346,-6.064422,-7.891225,-8.805652,-8.080176,6.604751,7.242725,-4.848891,-9.448297,-3.915107,-7.102617,4.997601,-8.986567,6.480195,-9.618268,8.293085,-8.614275,6.799360,7.408564,0.523834,1.089085,4.334304,9.689428,2.576661,3.696204,2.359131,4.604546,5.756442,6.264088,-9.203712,2.705220,8.910322,-6.605210,-7.050337,-6.675962,7.871970,-3.972293,-9.411637,-8.141885,1.061590,0.642826,1.352256,3.346054,7.536735,-2.504920,-3.954419,7.880277,9.923580,-9.735713,5.389353,2.689450,-7.487036,1.163150,-7.772258,-9.481128,4.759836,-0.304332,-9.403846,3.595980,-2.826016,-1.816991,2.709782,4.263378,7.680282,4.389465,-9.946335,0.983637,-6.395384,-1.171389,0.535567,5.417036,-5.104157,3.508641,6.334501,-8.042393,-4.709111,3.860815,-7.867131,-5.878916,-6.379546,-1.432359,0.593663,-7.598144,-1.833143,-9.702005,8.355254,1.120997,7.130360,5.441261,1.193465,-1.419462,-7.109192,-0.094963,-5.936223,-3.514378,-9.623349,-7.199340,-8.601922,8.678786,0.475464,-5.443268,3.079475,-8.880460,6.801694,-9.969468,-0.633365,-1.209205,-0.321588,2.075927,-9.709448,4.334212,6.328226,-1.266835,-1.889200,-2.141565,3.529253,3.723796,-7.886690,8.739456,9.075650,3.500276,-3.090668,-3.624468,-1.068247,-1.981209,9.697852,0.989880,8.216973,-8.814440,1.966881,5.969501,-4.996945,-1.833851,-0.316273,-9.727926,8.814069,9.598026,4.111542,-5.571742,-2.335653,-8.665409,-8.580711,-4.747328,9.645179,-5.196913,9.046434,8.096490,-5.871776,1.697012,7.314541,-8.618338,2.906341,9.053750,4.500063,-8.452960,-4.159935,4.592251,-1.597827,-6.046754,-6.785951,-7.692907,-5.258429,9.763736,4.364029,7.227414,-9.161993,4.972963,-1.949098,9.195727,-9.006071,6.369628,-4.299271,-3.413641,-8.883992,9.623363,4.607804,-6.815926,8.505392,-2.093510,-9.600910,-2.490924,6.700453,-0.446797,-2.681453,9.997243,3.372531,0.855461,0.895039,-8.963123,-5.852285,-0.721639,-0.542521,4.511907,0.636977,-9.547796,5.711151,-9.024160,9.328782,-5.741723,-6.853823,-5.924017,-4.619272,-9.220592,4.389778,4.272679,-7.531990,3.320999,8.308628,-5.792730,-3.491088,-2.333480,6.958788,-1.494344,-7.527834,-8.988137,-5.502563,-8.304003,-9.917859,-3.876194,-1.156335,2.192318,-5.207805,3.626207,7.449030,-7.481758,-7.804553,-0.087766,0.863184,-8.380169,5.258695,2.502679,-8.677769,9.375255,-7.180172,-9.206458,0.856905,0.959297,9.996165,4.608293,-2.888923,-3.557796,0.528758,1.932216,-2.699509,-5.927392,-2.112416,0.518212,0.091774,-8.623755,0.934116,-3.471081,-4.615588,-1.895555,-4.543415,1.244725,0.214177,-7.075265,-7.360306,3.507122,6.084895,-4.085698,6.623713,-1.870770,-9.429218,-4.947578,-2.729728,8.072352,-0.533566,-3.086537,7.323743,-6.696727,0.617099,4.382486,-7.513519,-8.118222,-7.867122,4.449791,4.532032,8.227797,-3.352702,2.796506,-6.570774,-2.040683,-7.783844,-8.258311,-1.248721,-5.078054,2.310565,2.300309,-9.052700,3.911473,-3.954275,6.190594,6.291955,-8.879080,-9.226823,-6.327250,-3.247428,-7.369071,4.994578,-4.251071,7.888527,9.574470,9.981746,-3.040443,0.466470,-3.875897,-6.757711,4.730497,-4.291885,-9.502408,5.650641,-0.214966,8.567982,-5.215087,8.284992,-6.264050,0.649175,6.831921,-8.495034,-6.439894,6.511202,3.689726,-6.663357,7.948274,-3.513102,-2.847471,-7.320711,0.220145,1.006998,-3.649531,0.904193,1.139328,7.324011,6.721069,-2.547483,3.639701,-9.076642,4.810690,9.978469,-5.404822,-0.467649,5.702026,1.157728,-3.640354,-8.796503,9.576836,9.014151,-8.928806,6.555217,-0.001007,2.824658,8.333315,6.744713,8.098203,-0.786867,-1.170280,-2.573784,6.204172,7.491762,-9.132248,2.474432,3.928306,-5.663250,9.264029,3.292931,9.879551,1.385621,-5.746940,1.912609,5.785067,1.135666,1.809167,8.270439,5.500888,-4.272286,-0.603556,9.815551,0.703657,6.015382,3.501712,-3.015285,8.578397,-6.559919,-5.505038,4.634753,4.704299,-6.359173,-3.583037,0.706024,-3.323370,7.592528,6.829337,-0.158084,-0.560831,0.697612,-7.907105,-4.092837,2.339545,5.383473,3.134506,6.745855,-1.979362,5.544357,7.874922,-0.291229,-2.520457,-1.969445,6.134470,-2.389849,-7.880736,9.224553,-2.210035,4.509392,-9.093341,8.306463,6.154408,-7.970273,-0.077112,6.332771,6.918050,1.320595,6.980809,2.288583,-9.405722,4.008757,-8.498867,7.615647,-3.505195,-4.745606,-7.383099,-8.345897,3.365828,9.890967,-5.265704,2.762448,-9.289699,-3.131220,7.400984,-9.007490,0.808885,-1.785943,3.351745,-2.530377,-0.233306,-6.443031,1.021383,9.763683,-9.947955,-1.782069,1.403563,-0.094826,5.372950,9.666088,-9.269635,-3.724627,0.757394,3.563269,7.628133,5.375109,9.602286,-2.182204,-4.549960,7.152905,-2.857610,-5.526116,9.231789,9.329120,4.001200,4.087477,7.547419,7.018438,8.181678,1.171516,0.350643,-5.461895,-4.492801,6.324866,-2.225062,7.857925,-4.972168,-8.224178,-5.926778,-1.571112,1.773855,-6.270399,-1.708891,6.812597,-1.425264,-9.118291,3.712121,-3.648027,8.815800,4.046458,-5.376752,-1.165313,-0.807222,3.674310,-0.707477,-8.998830,8.769870,-5.330193,-9.861535,5.244043,-8.766424,-8.227631,9.297368,-5.016793,-3.460084,-8.673022,-1.350136,-2.925516,-6.827251,-0.214154,2.107914,-2.568988,8.336351,-6.185679,-0.686978,-3.991625,5.740884,8.961776,-3.939151,6.774493,2.358965,2.093788,-8.990228,-7.581078,2.354150,-1.719515,0.822419,-4.578548,4.744206,-5.505832,-1.663132,6.800682,-4.713919,-5.088115,-1.740936,4.903079,-9.124747,4.711085,-9.588301,4.773750,-7.758536,9.771872,-3.400946,-4.122545,-5.348125,4.900500,-0.224556,2.755883,8.385297,2.319569,0.262249,6.669491,0.998064,6.725604,-1.610323,-3.365514,-1.302835,-4.463217,6.374575,-8.271930,-7.399654,-9.579162,-9.558825,4.436372,-5.828281,5.174704,0.636871,7.067870,-8.492774,5.612396,7.205318,4.492400,1.410745,-4.729030,1.133590,-0.812044,-9.340128,-9.967822,-2.225238,7.823230,-4.606414,5.224283,0.073315,-4.712448,4.607654,3.093039,8.254340,-0.697541,-6.648964,3.392011,3.637389,7.542713,5.412475,0.184289,5.673554,-5.673758,5.538274,-9.479548,-0.332017,-1.970744,-7.894672,-5.289920,8.430148,-9.497023,4.131365,6.107354,0.063945,-0.807665,-0.876004,9.403892,-7.299642,7.968267,4.175200,1.903365,-1.219955,6.573401,4.805126,7.180951,-4.352079,-1.966917,0.187132,-0.560893,6.959442,6.273742,-2.024732,0.650012,-9.757409,4.960854,-8.261131,5.983504,-3.378778,1.298024,-1.184357,-1.948656,-3.962210,-0.234960,-2.250011,9.772294,-4.333570,9.113715,6.685600,2.698938,6.169371,8.585119,3.498896,0.187981,1.477794,8.102039,8.929187,-6.617965,3.547909,8.355651,9.552218,1.317856,-5.052734,5.696770,9.115041,2.977668,2.426118,4.586830,-5.206459,-4.431332,6.818526,2.064152,-9.659694,2.723198,2.804094,0.682650,9.326080,-1.965962,-1.008896,0.917572,-5.544238,-2.307436,2.322187,6.574527,-1.186414,5.256982,2.826174,-4.761946,-3.389171,0.517435,3.401289,-7.288551,1.352402,-3.262582,-4.437925,-8.668017,-5.263624,-3.588417,-4.679769,9.285991,-2.558046,-1.063135,-0.489612,8.782299,-0.677492,-1.306455,6.090499,-7.959859,5.731429,-8.262876,-6.896588,-4.505039,-4.569235,-6.845037,-2.698620,6.287984,-5.350125,7.239330,7.884071,5.220116,5.444587,1.180384,8.547215,-9.020175,-0.702660,-8.964851,7.835360,2.721622,-2.078030,-8.119510,-0.087756,5.785427,1.800821,9.306816,3.102070,1.525261,-1.499428,5.221815,-4.775383,-3.116598,2.299938,-9.058412,8.452179,-0.594194,3.345722,7.577826,-8.654749,4.038079,2.985609,-5.065808,8.154385,7.146783,-6.653538,7.768446,-4.364805,9.750237,0.001784,-6.254703,-6.458156,-8.068249,9.871215,9.259089,-3.727340,-6.772621,3.202837,-3.682915,-5.336131,-7.909751,-3.729858,8.700029,1.329190,-7.183278,-6.624670,4.757938,9.260303,3.740586,7.181438,9.625124,2.872673,3.305855,-7.055246,3.281831,-5.262951,-6.127963,-6.545727,0.265544,-0.038626,-0.397740,4.443587,7.931456,3.939517,5.209208,9.636407,-9.133736,-6.007240,4.744669,4.972252,8.810121,-8.302995,-1.762406,-1.406800,-2.880427,-8.164852,3.334291,0.262098,-4.098251,3.091266,8.831349,-4.207828,5.761376,-2.408958,-9.284700,-4.476591,1.870062,6.349182,7.075806,7.572115,-4.956440,-1.890582,2.829354,0.970915,-6.680577,-9.248143,5.541468,3.679775,7.730739,-9.824994,6.555797,-3.441927,2.355306,-4.901670,8.812137,5.142881,8.006830,1.011021,5.448970,3.649826,-2.714676,7.885444,-0.025283,-5.325986,-0.734011,1.092892,1.368978,-8.782465,1.111198,5.306297,2.313089,5.084706,-6.475420,9.033456,8.756874,4.497866,-5.179740,4.314418,1.072678,4.336325,-7.851703,0.733915,-1.258161,7.722159,2.812897,-1.735669,5.345462,4.148311,-1.650917,0.803358,4.064342,3.365796,4.332581,9.433426,3.081318,4.740865,0.537756,2.788217,-2.666122,-2.016189,-6.688986,-1.845356,-0.113162,6.424588,3.288009,-4.181127,-6.940315,-2.802954,-9.918799,-0.384619,-9.412508,-5.330652,3.153160,8.825617,-6.207462,5.387085,-9.421960,-0.027368,7.258445,-0.830076,-5.457038,-0.738153,-8.856973,-1.374211,-4.202488,-8.578180,-4.492805,-7.388888,4.792427,-2.822448,0.576560,-5.466823,9.866087,-3.306693,-5.812696,7.089074,4.887457,6.815895,9.962898,3.396340,7.609531,-9.993365,-3.429738,5.430664,2.982448,2.978673,9.815380,-1.685379,-7.374214,4.312237,5.898598,6.410241,-2.329456,1.277602,-6.173148,8.565538,-6.770268,-1.079404,0.257674,-3.698700,2.796093,6.976929,5.683352,2.980237,7.124442,1.095388,-1.526740,8.936804,4.386765,-3.412539,4.654787,5.911014,6.017986,-0.146251,1.598956,7.546271,-0.097256,4.233630,6.351414,3.372735,-0.554160,6.732840,0.376961,0.694837,6.089243,8.257830,-5.132220,9.675703,-7.694647,-2.585921,-6.403137,-5.788655,-3.150869,3.130825,-5.138533,-0.260910,1.988523,7.126005,5.221896,9.702186,-9.269279,3.936874,-4.584401,5.228927,2.509940,-1.126700,3.203813,-0.577446,3.509258,0.914933,7.760322,-0.386357,-8.023739,4.184345,-9.170233,-0.557787,8.569749,0.630034,-0.398936,-7.627476,-8.516134,-4.453768,4.146676,-6.500417,-4.883841,1.926271,6.316637,-3.963312,0.944899,7.003079,-0.508719,3.255770,-1.780406,2.493419,2.888408,-5.809258,1.795909,4.631584,6.112468,9.062167,-0.583911,0.714062,-3.069353,4.400188,-3.927254,5.688220,-9.646565,-4.085915,-3.477145,-1.322260,-0.085959,6.030469,8.618400,-3.609786,-6.942548,-3.621768,-6.661754,4.739747,1.545036,5.227938,1.475872,-3.256060,6.600475,-8.396376,2.420517,0.201090,9.347016,5.064299,6.855120,-9.403733,6.615363,-1.460284,-3.561946,-6.870605,-7.681572,2.311867,-4.121767,-7.465329,6.124242,3.480114,1.064278,-1.680494,-1.217464,8.944564,0.778150,1.577161,-9.319904,6.410702,7.929534,-7.117619,4.181183,-7.065044,4.894088,1.073743,6.382425,4.117282,8.118529,-7.146484,7.892653,7.847039,0.396357,3.242860,0.386352,-6.964305,-3.613125,-7.192737,1.828846,-4.181378,0.405364,6.859233,-8.372837,6.651299,-4.341407,9.634579,8.876546,-8.805903,-7.786935,-6.721627,-5.974040,-5.416700,4.472931,-4.436799,3.137618,-3.459897,-0.952420,-7.582524,-7.693650,-1.139770,1.332513,2.721637,8.710486,4.160650,5.692017,7.930478,-2.494505,4.182877,-3.134773,-7.845847,-3.233857,2.243763,-5.791169,4.547049,3.493673,9.470233,-0.128438,-8.704164,2.523508,3.582470,9.364991,-3.337584,-9.066861,-7.145725,-2.358050,6.738308,9.775625,8.159701,-9.870544,-9.164353,4.144698,-5.810380,-6.594394,9.063291,-2.753159], dtype = "float64")#candidate|3733|(2304,)|const|float64
call_3732 = relay.TupleGetItem(func_3192_call(relay.reshape(const_3733.astype('float64'), [1152, 2])), 3)
call_3734 = relay.TupleGetItem(func_3195_call(relay.reshape(const_3733.astype('float64'), [1152, 2])), 3)
func_1741_call = mod.get_global_var('func_1741')
func_1742_call = mutated_mod.get_global_var('func_1742')
call_3749 = relay.TupleGetItem(func_1741_call(), 0)
call_3750 = relay.TupleGetItem(func_1742_call(), 0)
output = relay.Tuple([call_3721,call_3732,const_3733,call_3749,])
output2 = relay.Tuple([call_3722,call_3734,const_3733,call_3750,])
func_3758 = relay.Function([], output)
mod['func_3758'] = func_3758
mod = relay.transform.InferType()(mod)
mutated_mod['func_3758'] = func_3758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3758_call = mutated_mod.get_global_var('func_3758')
call_3759 = func_3758_call()
output = call_3759
func_3760 = relay.Function([], output)
mutated_mod['func_3760'] = func_3760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_3773 = func_611_call()
call_3774 = func_611_call()
output = call_3773
output2 = call_3774
func_3781 = relay.Function([], output)
mod['func_3781'] = func_3781
mod = relay.transform.InferType()(mod)
output = func_3781()
func_3782 = relay.Function([], output)
mutated_mod['func_3782'] = func_3782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1429_call = mod.get_global_var('func_1429')
func_1430_call = mutated_mod.get_global_var('func_1430')
call_3839 = relay.TupleGetItem(func_1429_call(), 2)
call_3840 = relay.TupleGetItem(func_1430_call(), 2)
func_1917_call = mod.get_global_var('func_1917')
func_1921_call = mutated_mod.get_global_var('func_1921')
const_3864 = relay.const([4.429759,4.995374,-1.492441,-5.305682,4.415808,9.998579,0.258300,2.143010,9.638824,1.967967,8.378670,-0.612422,-9.804725,-8.408204,0.443385,4.376649,-9.889437,9.788149,2.845485,8.084459,1.000568,-5.165343,8.597163,-7.839657,-7.355613,-8.374825,-2.196167,5.898240,-8.677786,-7.821828,-9.736750,-7.226735,-1.115102,2.170859,-7.553153,-3.274902,-5.404482,-9.740895,-8.511234,-3.605005,3.124139,-3.070556,0.473835,-3.847021,-0.807505,4.524176,-2.640889,8.490936,-3.809786,6.112536,8.629680,-3.444561,-7.542198,-4.767834,3.991249,-5.760590,3.260233,-7.085723,-5.411033,-2.483741,6.017874,3.840988,-1.758379,-4.119375,-7.927925,8.862681,8.981528,3.119779,-3.456774,-8.258902,-0.394322,-9.264055,-8.772155,-8.622330,-4.350225,0.689897,6.596062,8.517066,3.137140,-8.081969,2.082628,-5.921212,2.411011,2.351844,7.118897,0.981977,-0.619744,4.294537,0.154415,8.606064,8.288336,4.729514,-8.438327,-8.390708,4.828673,4.532549,-9.064751,4.009555,7.650656,5.844643,4.227909,-8.104905,2.436040,-2.132724,2.662925,-2.841766,-8.534720,7.010253,-0.950597,-8.025469,-8.386364,8.108631,5.473150,-9.097650,4.837898,4.051872,6.652835,-8.321971,-5.888615,2.693550,-0.188858,-5.685715,0.484197,9.375260,7.941147,6.677385,2.032774,-7.552824,-0.139025,7.271563,-2.612876,-9.704955,-1.089723,-4.755877,6.110518,8.712955,4.379221,-0.888757,3.185443,8.491419,4.525880,8.526100,4.772655,-3.158759,-4.940176,3.610482,-4.036976,-9.143944,-8.290669,6.333227,-8.349131,1.659271,-9.431559,1.713126,-0.088437,-2.320083,8.959813,-9.078201,6.065418,-9.920949,9.226202,8.404596,0.864561,-5.035088,-0.690881,4.286991,-8.760956,1.219674,-7.430241,2.178446,1.842203,3.718701,5.673217,8.523601,-6.854109,-5.271642,1.511193,0.987485,-9.678411,-5.509885,-6.563159,7.864181,-5.049057,6.988447,6.916114,4.767351,9.581255,-2.807456,0.176003,9.943050,4.242849,8.695737,5.048694,-7.482392,-0.612678,2.088517,-1.052694,-7.348356,0.199389,-3.573449,-6.849102,6.560111,-2.123154,-7.727559,8.080584,4.970744,4.134558,1.319247,6.831498,-9.596120,-8.547956,-7.971993,4.296003,6.259984,8.984594,4.719041,-9.774805,0.185502,-0.839053,-0.324528,5.171852,1.907059,-9.029426,-3.534092,-9.552717,4.519913,-0.579984,4.810524,-2.093638,-3.400933,-0.185833,0.091209,-6.648269,7.789436,-0.989498,-2.182755,5.734654,5.028074,-1.464086,-1.167356,-4.376668,9.344896,7.144698,-0.044131,0.610000,9.114292,0.219276,-1.308209,9.470505,-4.840653,9.838207,-3.682151,-0.815840,-8.340345,4.405499,1.808768,3.090028,-5.149190,-6.755759,-3.444790,5.420893,2.643904,1.968345,-7.314452,-2.670885,-3.268432,9.730287,-6.934350,-9.206715,-2.396395,7.157974,-9.801823,-8.854891,-9.722345,2.576034,-8.450859,-4.377633,7.100910,-2.104346,6.047740,3.653214,-0.513200,-2.660610,-0.710775,-4.103668,-9.979655,0.421339,-5.329574,5.357701,-9.958234,5.856555,5.509879,-4.638969,4.872290,-7.946429,2.183557,5.034081,-2.642155,8.104846,-8.579185,0.319787,7.035611,2.121866,-7.488879,-8.972559,-9.486399,3.783108,-2.744530,-2.289242,-4.521679,-9.903229,-0.228408,-0.846001,5.060131,-5.584489,3.225737,-2.835959,-3.725407,-7.866858,-9.375001,1.857274,-4.082144,-2.091878,-4.239384,0.051313,6.169064,3.436919,1.030436,-2.683870,2.477789,-1.796766,-5.126659,4.184477,1.580630,1.733739,7.376445,-6.959148,6.516319,-3.636633,9.106374,0.986174,7.765567,9.296250,-0.384446,0.734944,-5.632556,-0.697485,-6.701420,5.450606,0.644564,8.337969,2.497320,-7.830439,-8.063313,-9.050787,-5.490450,-6.864393,-2.727616,-8.952212,0.945647,-9.142083,-6.085604,-3.465002,4.129453,-1.017841,-5.325140,8.917899,0.510747,-2.323803,-1.336207,6.993871,-7.700457,-7.366094,2.821070,2.777000,-3.597828,-3.227437,-7.331739,4.594851,-2.775579,-6.414268,5.476239,-6.834587,-7.134772,-9.576910,-8.582485,6.618347,4.890931,5.819903,9.261607,6.644428,2.843756,-6.688996,-8.857846,6.687569,8.861658,7.479083,2.846626,1.884701,-1.982685,-4.265541,4.544392,-7.937253,3.722284,-0.272166,-7.780441,-1.179083,2.139345,-0.983206,-1.308250,9.745460,9.577914,-8.609412,-7.809233,-7.047472,4.375654,7.339040,6.200723,2.638701,-0.281293,2.722564,7.226861,-0.252947,-1.620146,-6.644061,-9.782163,-0.105240,-3.068263,-0.165017,-2.974016,7.232580,8.201320,-7.804041,-7.172430,4.430041,3.342010,-4.460680,-0.262098,-5.635946,0.945761,0.963791,-8.241641,3.045950,-3.481706,2.870350,9.235099,-6.412813,-0.904216,7.578223,-7.775609,3.771182,1.890486,-6.574057,-8.189173,-9.240194,5.800570,7.126755,1.896823,-0.310305,-2.919562,-5.832737,-7.127506,-1.119377,4.071469,-5.587744,-8.371586,-0.304203,5.377328,1.101256,9.204249,8.563014,8.985480,-4.225833,6.481867,-9.144954,-4.151440,0.723900,1.031496,1.745882,6.089808,-1.653382,3.095691,5.051469,1.836136,-0.817379,-7.218802,8.728436,-6.567070,-2.299302,-5.030929,6.355609,0.413291,2.202144,-1.550448,-5.644695,-7.814249,5.528594,6.816707,-1.526295,7.577427,3.134817,-6.014242,8.086999,-6.799163,7.452846,-6.829580,6.836987,7.790244,-1.042559,-6.575069,-8.506542,6.834945,-3.703026,-7.568501,4.499311,-3.169064,-4.630879,5.040648,1.252042,3.297669,-7.497715,-0.050206,-5.396283,1.891966,5.851908,5.346589,-8.692491,-3.901465,6.136828,-9.989932,-3.629344,9.476029,2.386061,7.933262,-7.195653,3.144227,-9.051215,-0.818503,-2.586495,-4.329124,2.478511,3.705575,-0.484140,8.923464,-5.920710,5.253975,-4.767996,4.253203,3.813672,-5.528519,-1.612926,3.482777,7.556043,6.160365,8.240283,-8.656268,7.334163,-2.229313,7.677930,5.393807,7.757868,-4.079615,9.525837,-6.228123,-3.737034,-9.111360,-7.338565,-8.512072,4.165796,6.432747,6.512753,-1.600394,3.424430,-6.275515,-6.603194,3.676350,-4.748622,1.073664,2.953705,5.600996,-6.430066,-1.052527,6.926935,9.745904,-0.692074,6.271336,-8.427537,-9.963300,-9.701445,-6.269937,-9.858076,6.166393,8.351608,-6.687639,-1.712306,6.950195,1.858646,9.177877,-4.845911,-4.898324,-6.658139,-6.204653,3.993497,-3.683804,1.885409,-2.559578,-2.837175,0.652430,-0.624297,5.393782,2.093868,4.383320,-2.249952,0.573614,2.208495,-6.280749,0.832443,-3.725013,6.450295,-1.204551,9.694407,2.069537,-7.945738,-2.864074,-0.756437,3.447825,-8.783110,3.953603,-8.439854,6.093909,-0.873218,3.220336,-1.476124,-7.597187,-5.454274,-0.394354,9.506595,-5.045894,-4.232362,-6.370402,-4.733090,-3.379231,-0.828083,9.997734,-7.970643,3.767591,-7.424310,-1.980081,-1.255113,7.115365,-6.945973,7.832564,5.552698,9.639502,-0.577178,-2.002799,-2.780358,1.169355,-5.668213,4.696280,0.007495,9.885002,9.068305,-0.754283,-8.404134,-6.501597,4.175957,-3.201959,8.500424,2.280933,3.907678,-6.424189,-5.571051,7.210863,1.541433,-4.705264,8.275265,-2.162943,7.676501,-8.530828,-4.055287,-0.611083,-1.402296,-1.964233,2.074936,5.586410,-9.499804,-3.879466,3.571736,1.426454,-9.283775,8.518911,-5.264534,-0.344701,-5.251233,6.015564,8.984830,4.290357,5.237310,-5.680860,1.273885,2.022516,7.552546,-7.120970,8.255698,8.250247,4.277733,5.991657,5.841264,-3.459822,8.279780,-8.808756,1.482081,-2.469732,-9.869283,3.410321,5.316811,5.959872,-3.896543,1.123508,2.902735,5.643708,-5.996588,-6.108765,-0.121353,1.542090,1.598109,9.720961,6.450211,2.359945,-8.893190,7.026714,7.247540,-3.221130,1.165182,-2.759335,2.307214,1.117752,-5.727521,9.486763,-6.584988,-4.898251,-7.444797,9.271444,-2.804228,6.738950,0.307201,-9.991989,5.814921,8.456232,-6.972691,-6.502616,0.003277,7.229852,7.038588,4.739856,-8.760881,3.147831,0.093734,-0.316962,4.987750,-1.383203,1.944723,-8.678342,9.005922,5.133267,3.905022,3.361187,7.171690,-3.200629,9.930310,1.064259,-0.422203,2.155541,4.392381,9.358799,4.729556,5.450940,-9.135080,-8.404514,3.808099,5.323514,1.663299,-2.635720,-0.536822,0.882064,-9.580631,2.442006,-9.552966,-3.307619,-1.604877,-7.922882,2.874435,-5.383032,3.946259,5.982669,-6.240006,6.253053,-9.886425,0.554059,6.449375,-0.271257,6.204352,-2.442342,-6.045874,1.413095,-9.556953,5.073475,5.723357,0.318654,-9.834996,-1.012561,7.438921,-1.654731,9.630003,-7.612976,-0.999343,-1.651569,-2.438193,2.070011,3.195153,-4.170155,0.997725,0.635712,9.573690,5.240993,9.285236,3.118627,-3.091919,-7.821348,3.372962,-4.784586,-5.721955,0.825279,4.561836,1.788101,0.762485,-8.706529,8.593235,7.165459,-1.092537,-3.248438,-8.881552,-1.746645,7.464349,-0.608056,-3.526752,2.066791,0.781380,1.570113,9.957725,8.284586,-3.132764,1.767061,5.634912,0.527877,-9.873397,-2.467925,3.918785,6.073621,4.112775,0.589344,-8.292852,-5.435560,5.249978,-8.921059,5.164384,8.750146,2.897178,0.226207,3.275805,-8.073007,0.374815,7.848866,0.215046,9.716405,-4.853734,-2.699485,5.601866,8.384796,9.054490,-9.161110,4.415648,-9.938797,-7.627695,-2.788903,-9.425291,8.173996,7.596500,-9.914347,1.369213,0.580124,-2.339353,-4.925828,1.714813,-1.819844,7.902262,2.772672,-4.411623,7.755687,2.723034,6.856381,-8.113822,5.950685,5.375317,4.150092,-1.427312,-2.163079,-4.942583,-5.809635,-1.562401,-7.605395,1.433844,0.869644,-5.459852,0.417879,-8.918654,9.649025,3.712752,-1.329551,3.799636,-0.459409,-5.624108,-1.197937,0.017916,-8.087043,-2.890088,-1.081517,-1.299068,8.457716,-0.924647,9.921417,6.647212,-3.380911,8.808536,9.431804,-3.105858,-5.809726,8.493197,3.227143,-8.625851,-9.954136,6.752052,-0.646484,-5.905339,-0.838746,-2.446162,6.455148,-9.072355,5.336388,-2.885589,-5.037991,-6.893811,-2.009333,-3.455158,-7.183855,2.116973,9.288629,3.734863,3.386881,6.224111,0.697971,3.799601,-2.270355,-8.916226,3.861872,-8.068340,7.683273,2.788965,-2.726274,3.156918,-4.111330,-3.936742,6.662388,1.494075,2.918074,-2.954297,1.660437,-6.179241,-9.734344,4.411201,3.318729,9.371389,-6.410918,-3.063870,-9.602631,1.650637,9.306563,-6.063034,-9.988387,3.065580,1.270810,-4.573075,6.440702,-9.800641,1.203912,5.423232,0.341242,9.461673,2.359218,5.795898,5.999795,-1.549697,-5.858911,-7.979678,0.107102,-4.624934,8.816473,7.085452,4.191081,-4.861111,4.945143,-7.211107,1.976409,-2.503393,2.345442,-6.503285,-5.960315,2.472938,-1.053259,9.704651,9.226839,-7.740976,-3.597275,4.928696,7.007823,-6.379792,-1.891327,8.636268,-6.594084,-3.660486,2.063738,1.243289,-8.690852,-3.601320,-9.327045,-4.378340,-8.077165,-1.757115,-9.759228,-1.310763,-1.773885,-9.602421,2.968754,-8.141449,6.825286,-9.320164,6.132601,-0.806647,-6.186861,-3.496928,4.660977,9.888597,2.249991,-4.657627,1.418381,6.080776,-7.658325,-5.353108,-3.969858,8.128127,-9.155380,-7.310601,0.625088,1.849469,-4.227717,-7.152505,-0.619245,5.879697,-0.486514,5.501095,-3.791263,7.497323,-6.754887,6.426582,-6.613928,-0.559558,-8.679269,-4.422525,0.503330,7.601981,-2.557248,5.974389,6.731445,-0.404283,7.504452,-1.904162,2.120210,-3.137622,2.492030,-6.134156,-6.268127,-1.431022,7.969309,1.036777,-3.839632,-4.380874,-4.160796,7.073255,-6.543487,4.885458,0.535784,-0.407043,2.417214,-4.513908,-7.008993,-9.138467,3.783983,1.411092,-3.523626,-6.397104,4.043354,7.584095,-2.082816,-5.497565,-4.629352,-4.957368,2.943286,-8.096971,8.079728,2.945870,1.113654,0.336556,1.463256,-8.020696,8.022476,-3.424657,4.626697,-9.896905,4.270847,1.465071,8.772215,7.295479,-5.720991,6.759624,3.042613,6.554400,3.550330,6.632477,9.804768,-8.328835,-4.171224,8.628671,-2.353598,-7.641185,-5.100733,4.937021,9.292506,-7.650920,4.283590,-3.805124,4.246381,6.232943,-4.862723,3.452559,-1.130422,-5.935580,-4.932668,6.064376,5.110889,-2.257219,3.542621,0.431155,6.179739,-6.301939,-3.183564,9.087500,-5.425266,-3.576821,9.214654,-7.846018,4.841409,2.902678,-2.522412,-9.982135,-4.366018,-1.827614,-6.164870,-0.040867,0.265389,-0.399317,5.752698,1.549297,4.577536,-5.856891,1.250642,-6.459085,2.918124,9.802449,-6.711542,-0.338776,-1.619388,-4.150895,-8.377551,-2.440655,9.341771,8.510925,-9.527420,-9.321964,-2.925358,3.701271,2.241414,-9.147954,9.436534,4.518138,2.306937,-7.617757,-1.877523,8.906971,8.487618,-0.444360,-4.665082,-6.618073,7.492407,-8.452187,5.866717,7.741882,-9.865708,-6.825177,1.078606,4.325258,8.891450,2.267484,6.439810,-9.076645,-1.707314,6.207660,5.374467,-6.525165,6.885856,-6.333134,-5.920624,9.525931,-4.313150,-1.766627,3.648194,-1.374369,6.040004,-6.711845,-3.491809,3.629041,-2.966794,-5.706342,-3.893068,-7.932297,3.631186,3.936658,-9.925533,-3.040212,-9.653500,0.785516,0.351904,-9.527617,2.209050,8.796435,8.705281,-4.936933,5.716509,9.673673,5.054631,5.321231,8.174866,-5.255968,-3.282409,-4.704877,8.794497,-9.245106,9.949267,0.116745,-9.188171,7.784603,-6.505403,2.186836,-4.252622,9.465391,-9.742874,-0.212935,7.497281,6.855131,-1.683149,-4.614083,9.962294,-1.910919,3.324990,4.536923,-3.356678,-1.836047,6.400596,-2.375093,-1.015113,0.146428,6.764750,-8.360030,7.858157,-0.858921,8.254505,6.093166,7.166462,-5.090844,-9.628603,-7.271538,-1.110714,6.439538,-9.665217,4.733775,2.473085,3.498728,-4.673598,-0.420978,-0.871338,6.350605,2.288641,-3.209370,-4.273580,-5.037003,5.918967,1.582545,0.723607,6.757371,1.101987,-5.780582,5.220454,0.638858,-2.320667,9.875001,-9.458642,-8.846698,-8.723052,-2.299686,1.221369,5.268789,-7.036721,-0.986500,5.055214,8.326601,-3.125335,2.460195,-6.318111,-3.907648,-3.367246,9.337353,-5.727014,2.047229,-3.731746,-9.538331,-1.500764,-2.390729,-6.334091,-1.165179,-4.728469,-7.250136,6.940288,3.242875,-3.630801,-5.893381,8.339436,2.805293,-6.294487,-9.085242,1.692921,-2.667774,-6.866536,-4.063579,-0.215994,-6.934275,-3.349468,3.007780,6.423117,2.966556,-2.185070,-2.074338,3.552221,-6.317130,-1.470133,0.342856,6.257700,6.367684,-7.691391,-2.862566,-9.688306,-1.588069,-4.549730,7.994254,-6.366062,7.273754,-0.310272,-0.526677,-3.438770,2.879014,-5.605145,-1.599271,4.004370,3.490150,1.376482,-5.557011,6.730096,-5.364617,-9.495609,5.977079,6.356362,-0.297614,-1.131840,5.061731,3.739825,-4.135912,2.444972,1.912508,-9.451082,8.826093,-9.241446,-9.509672,-4.725976,9.444727,-2.604252,5.487453,-9.971278,8.145175,-1.819236,6.579300,-4.047954,4.896294,-3.701650,-3.389200,-4.172087,-9.369680,7.267690,-6.689140,8.725290,-6.323365,-1.002573,4.330436,5.287238,9.597497,-2.111645,1.886551,-2.142922,-9.930282,1.922771,-6.700696,-3.980292], dtype = "float32")#candidate|3864|(1440,)|const|float32
const_3865 = relay.const([3.112369,7.364768,-1.651293,5.757984,-9.905179,-8.907105,6.224071,-5.987510,0.516313,9.605478,8.484585,-3.889005,-9.069901,-1.177565,-2.235051,2.108880,1.274193,-9.216499,-6.467973,0.910403,-5.619856,3.194609,-9.872685,5.896237,-3.652579,-2.886473,7.282467,5.559932,2.916629,6.064172,1.670856,-2.599099,-5.201706,-9.504765,-1.560702,3.649697,-8.881134,-3.209047,1.648081,-1.413703,6.981664,0.906988,-3.618377,-2.912061,1.229168,4.607782,8.531845,4.427297,-2.020478,-7.023599,2.472845,-1.392906,-2.070982,1.827200,-3.783865,-3.597607,-1.211109,-3.148085,-1.930078,-2.422550,7.371696,7.801665,7.065584,-4.617199,-6.338386,7.196735,-2.760134,2.336442,-4.648159,-1.758573,2.933612,-3.666121,1.298757,-1.492357,-8.461106,3.124687,-0.574023,-3.767038,2.598761,-1.097100,4.925105,1.532204,8.043326,7.176290,1.948404,-2.025757,-4.638778,-4.305372,6.128897,9.987742,-5.879141,5.622974,9.168275,-0.569813,-5.750419,2.708778,-7.200059,-3.061897,8.379126,-7.370219,9.924698,8.473473,3.443515,3.720391,-6.819276,-6.606214,9.221412,-9.104993,6.402244,9.272833,1.001653,-9.834844,-7.154389,5.353864,-3.346532,-3.988196,-5.852073,1.671876,-1.084563,-8.701655,0.576256,0.369274,9.747524,-9.808143,-3.731104,-0.682864,-2.859773,-1.463333,4.187555,-3.257641,5.154366,-5.204752,4.750427,4.070581,-6.961711,-5.598495,1.264116,0.489842,3.373188,8.612942,7.200847,1.553219,-6.232152,-3.450452,3.899153,2.451879,-0.960660,-2.979277,2.551117,6.389333,-6.454238,-0.446310,2.945693,-8.932803,3.212715,-7.538510,8.126870,-5.747564,8.223126,-1.157649,4.991350,9.493435,4.615934,5.143985,-8.083219,-3.561088,0.695826,-9.628803,-1.019635,8.820498,-1.821486,0.072541,-8.541193,-9.831091,-4.141980,-9.409805,-0.501587,1.913072,-8.421809,0.907432,6.240747,9.902491,-9.078447,9.809314,-7.604985,-5.641621,3.647541,-2.252180,3.200824,8.376090,8.400959,4.563629,-9.919197,0.585296,-3.027505,6.890623,5.808409,-7.480382,-6.922537,-8.792865,-5.680855,5.131617,-4.443008,5.428557,-4.373150,-7.332948,6.521047,-6.383020,-7.984183,-1.806985,-6.540824,1.188898,-8.807354,8.140849,8.373067,7.903904,-3.919796,7.790513,-3.299411,-3.940709,-1.664552,3.943949,-2.536290,0.692791,8.239150,4.045303,8.200025,9.450756,-9.936813,-3.266259,5.627612,-0.103851,-0.151856,-6.464664,-9.701595,-7.166017,7.479831,-6.975099,5.547705,6.030040,6.678270,-9.879866,5.372896,-1.035225,-3.034210,4.126535,-3.519210,8.900176,-5.369631,-4.979383,-5.490477,7.366075,-1.059567,4.842478,3.618533,-3.481598,-2.499236,4.274205,2.787242,6.743427,-9.241987,5.917182,-7.027904,7.800887,-0.289835,-9.804280,-6.291240,7.948440,6.185916,-3.988728,1.542640,-8.201475,5.091138,3.733428,3.319699,-2.105210,2.276945,8.024627,-4.669870,-1.718541,-7.274011,4.723243,-8.355366,7.781005,-2.094776,-0.759148,-9.969034,8.239052,-5.637101,-7.365907,8.839830,4.138219,-0.786825,0.353459,-6.154460,-8.682459,-3.847548,7.816015,-2.071753,-0.179608,4.021361,-6.652192,0.864319,9.857562,-9.691581,-0.537488,4.506538,-8.896415,-2.116984,-3.015074,-0.354881,5.935805,5.770694,0.550731,0.139956,-0.284058,5.567647,-5.657726,-2.165472,-3.957536,-7.314690,-2.819919,9.865934,9.668966,-5.207236,-7.562855,-1.156556,2.060139,-4.804179,2.793783,0.492347,-1.288231,-4.640478,3.908811,1.522150,6.485662,-5.895902,0.158417,3.813457,3.892220,-9.042383,-4.594241,3.666047,-5.347728,-8.995205,1.133117,8.393940,-5.062517,8.671670,-9.106969,-4.661606,-3.628069,-1.287158,-0.318370,-0.580484,4.515870,5.578158,-9.380702,-5.912301,-7.137666,-4.118553,-3.708498,-7.799382,-3.170180,-5.438197,-7.962070,-1.972033,-9.130745,-8.373756,-1.159732,-8.070173,4.608192,5.540409,3.785180,9.819264,7.245761,4.334271,2.116317,-6.279293,5.741556,1.497226,8.319862,-2.591735,-6.341962,-3.519286,-5.384372,-5.757425,-6.227776,7.296118,1.971832,-2.722863,-6.157527,-8.689052,3.148941,0.722993,-2.418670,-0.921251,3.856747,5.499077,8.253979,-9.123939,-9.053944,4.721123,1.135321,-2.365944,4.837858,8.662227,3.760819,-7.154269,-1.179461,2.904755,-7.180914,1.144631,0.133915,3.393607,-5.279976,-2.528677,-3.583240,-9.388175,-8.441687,6.786733,3.105450,8.282178,-8.525596,8.573303,-9.606175,4.340012,-3.925001,-0.406967,2.052374,-7.330894,8.223960,8.979199,-2.781278,9.510055,-2.742245,1.664239,4.556585,-3.074689,-9.897703,1.487801,6.381149,0.674955,0.168783,8.075489,8.577467,-2.556693,-1.200567,-5.055959,9.728714,8.497128,-9.031919,0.871937,9.558132,-0.874335,7.290901,-7.649194,-5.349365,-3.141879,0.690664,7.217366,4.847978,-2.729974,9.212418,8.081732,-3.767533,-8.866759,9.764474,5.627727,-9.735911,-9.069242,2.930742,-6.544249,-8.644771,1.505904,-7.097973,-8.219619,-1.777647,4.417346,9.369726,8.812240,4.527395,4.605482,1.819261,3.393008,-8.541632,-4.778873,4.154183,6.737647,3.776459,8.006369,3.224337,-4.910007,-0.775346,3.729031,-7.173187,-3.643564,9.738934,-9.143512,-6.241122,-0.577217,6.458383,-8.288352,6.587554,-8.583665,-5.285222,-5.869667,6.019495,5.550394,-1.035262,1.394799,7.234791,-6.841161,3.601554,-4.720045,-9.897602,-2.553252,4.434918,-9.094073,6.821139,8.652854,9.752189,3.700802,-5.101741,-5.864734,-3.353968,3.085880,3.170739,-5.765030,-9.247882,-0.711603,1.927152,-5.886004,3.675198,5.187329,2.187002,-7.304441,-0.440663,5.988040,8.791754,1.367433,-8.006120,4.746229,-7.380689,-0.659966,-9.660867,0.782899,-6.057644,-9.203789,8.362867,-9.921424,7.827969,3.452706,-2.033583,-5.857390,-0.475758,1.323111,4.684540,2.135695,-2.272789,-2.781293,-7.793021,-1.097823,-9.844547,5.682670,-1.883733,-6.889309,-6.390521,9.207152,1.109984,-3.918100,9.433436,-2.696834,9.823837,-5.319285,3.842443,-4.054089,3.216161,-8.701741,-2.466339,8.045415,2.440639,-0.767937,8.988461,5.454344,1.407221,-4.309300,1.903199,5.966323,-1.129618,6.084970,8.716397,-6.497348,-0.774830,-9.091625,-3.959705,-4.465000,9.118196,2.755127,-4.817946,7.261688,7.855935,4.905817,-0.019253,9.478061,-2.669392,5.107011,-5.671117,-3.305032,-0.897712,6.127971,-6.099529,1.645662,-3.778726,-1.816193,4.652534,8.354679,-0.520981,6.148257,9.167593,8.014355,6.647564,4.691058,-7.979264,1.353835,-9.005826,1.862802,-9.702158,8.162879,-8.547290,0.175781,8.051104,-1.779505,0.035611,8.800143,-4.974233,7.188931,8.164667,6.638986,-9.953868,-2.581070,-4.020462,-7.404935,-6.250607,4.334416,3.001390,-7.815367,9.802170,-5.724872,1.722186,-1.854410,5.865641,9.467962,-1.399772,-5.900650,7.465382,-2.669257,5.564310,-7.430182,-2.443469,-9.316505,7.256054,-4.298172,4.654554,8.333205,-3.145638,-9.110633,3.090608,-1.969399,-4.782753,8.848958,-1.716345,6.262919,-4.351559,3.133534,-6.402406,-6.616090,4.597910,-0.540878,-4.359168,1.789391,2.865101,-3.726510,3.364786,4.584789,5.353917,-5.067669,-3.676012,7.690783,9.117363,2.189836,-6.199434,5.730148,-9.052101,-3.412977,-2.618037,-9.158224,3.171261,-1.140282,3.472945,1.448392,-8.033820,-4.965444,9.389916,4.557263,5.597236,-5.121867,4.898480,2.685258,-4.851115,-5.062091,3.802429,-9.435098,6.779843,0.172848,-9.849212,7.254237,-7.631188,8.847332,-6.017557,7.327067,3.111839,4.435269,1.870942,7.897091,6.136773,-9.842175,-7.603501,2.040486,-4.848834,-3.448531,6.189908,1.918018,-2.621458,-9.333048,-1.807734,-4.741723,5.438045,-6.544240,-0.553700,-4.132318,0.987094,-5.893178,-1.136068,0.724067,-2.499716,4.766316,3.346930,-5.178480,-6.805972,-7.435508,-2.700535,-3.786045,7.444610,-8.123464,-1.083937,7.091530,-3.474057,5.338789,2.841234,1.045976,2.993993,-1.580338,5.975754,-6.707685,5.995526,-5.647640,1.691005,7.094864,9.500570,-9.196042,0.029605,2.422641,5.796174,-1.027686,6.217571,-6.143259,-8.056072,-2.729794,5.560192,8.050591,8.113958,-7.216054,3.985922,9.113731,-7.711544,-5.743018,7.209284,7.296818,2.294374,-3.584222,8.275001,9.746753,1.686432,7.815167,-6.310761,6.984851,2.133318,-7.438280,3.184206,7.687313,9.784492,0.156294,-9.134750,7.501149,-3.990708,-7.098776,-2.261758,-0.187671,5.388663,9.288925,-0.663796,-6.221040,-1.668316,-7.267749,-7.927625,5.314430,-9.776244,2.365442,8.385633,-1.976718,-6.331763,8.432024,-5.682088,-5.022698,-6.828698,4.767606,-6.068048,-4.888507,-4.793173,-1.187522,-4.503004,-3.503667,1.798475,0.410338,-7.567452,-5.125090,2.945949,8.000986,9.984193,7.558584,1.086291,6.403885,-9.948502,0.070796,-5.220284,-7.000251,0.161267,7.062468,-1.238712,-1.353467,-3.261614,6.732317,-4.250319,5.847151,-7.231415,5.761489,9.938130,9.844815,-8.701306,-0.362692,-2.350850,-8.065011,0.181002,-0.800432,-8.473140,-6.015821,-2.308266,-3.686958,9.587167,-1.613130,0.595779,8.741907,-0.002939,-7.190002,9.677924,-3.608811,2.179145,-6.701397,-0.968691,-2.564766,1.474393,-1.886683,-0.894357,-2.437532,-4.479466,9.388678,3.215111,1.272645,5.001339,-8.093083,-4.899981,9.300336,2.616486,2.092364,-9.904110,8.000336,-6.909370,1.051424,-2.790690,-2.697544,9.730321,-2.353442,3.213804,-1.807549,-5.244575,0.960492,0.112326,-4.789613,-2.010083,4.007381,-0.836320,-9.140771,-2.902309,9.384078,-3.517378,5.251509,-1.542686,-0.644897,3.777180,-9.841614,7.761581,9.997058,-5.327944,-9.458128,0.426043,-7.200916,-2.590359,-5.659289,-3.627711,5.236640,-1.996778,-7.173825,8.809350,-9.277340,-5.471767,-0.827710,-9.359067,-2.855944,1.963938,-0.251783,-7.097384,-3.848513,9.271411,5.725612,3.594329,-1.934703,-2.885369,-3.545692,0.385111,-0.511200,7.862688,-0.954056,-4.108166,4.204199,9.504175,-2.408947,-3.906173,-0.368814,-3.463751,3.117270,-9.636584,6.382965,8.270285,-4.406735,-3.414992,-2.055968,0.883216,6.668721,8.429735,-2.986443,-3.386038,7.815831,9.342698,0.662889,7.461059,9.455784,-9.448293,-2.353670,-0.547090,6.766980,-9.276629,7.889632,-6.713518,6.087154,7.654035,-3.002780,5.191933,-5.588462,6.399168,-6.027592,-8.975306,-7.861965,-8.903880,-6.940656,-4.068539,7.476484,5.790412,-9.115774,0.512234,-6.759227,4.286173,5.117505,-1.472073,-3.646455,9.770731,-0.152563,-8.686472,-8.424888,-9.694986,-1.433027,-1.209102,0.444059,-9.732445,7.300003,6.755938,-3.302030,-9.956414,4.730242,8.477485,-1.475308,-3.783794,-6.467897,-9.798864,9.695799,-8.621688,7.908182,0.550765,-1.405313,-3.420277,-0.302837,5.061060,5.057184,-7.741757,-6.784774,-4.886196,-6.998430,-5.308704,7.980062,4.777101,2.893633,-2.922728,4.471603,9.153303,1.973778,4.865550,1.950394,-8.880981,2.356929,-6.170117,-6.508978,-3.208020,1.319310,-3.028816,1.891023,-4.341151,3.193248,0.165169,-0.674450,-2.806522,2.893365,6.503162,3.348896,5.643576,-3.468490,-8.413459,-7.882189,7.575025,7.931754,-5.676026,-5.681577,6.437198,-4.248131,-3.106333,4.937764,-1.994891,-6.302949,-0.114652,-0.595533,-4.224450,6.981209,1.694806,-8.036913,3.512577,-8.007570,-5.402034,-3.508237,-6.870238,7.227117,-3.515101,-6.831657,9.277632,-9.539600,-2.287267,4.197602,-8.832044,5.268621,-0.881503,-7.368150,-3.598451,4.834435,7.608901,-5.624947,-9.206016,-8.220079,0.870708,-5.866481,-4.496773,-4.882109,4.598363,2.321141,-8.505152,3.193975,-3.557311,-4.205784,4.446088,-5.249289,-2.380044,-1.142831,-2.285544,1.912506,4.312063,-1.117871,-2.932837,-7.138374,-3.281312,9.435349,8.954058,2.597490,4.573863,-1.253912,9.400065,4.063021,0.008163,4.001626,5.229961,5.081042,-9.879627,-3.688554,-8.157627,-6.933998,-9.651517,5.755909,-4.797299,-1.706223,0.589451,-1.962848,6.952902,-8.224867,-4.009614,-7.318530,-3.964282,-3.214348,4.937664,5.478586,-2.937379,-0.161722,-9.713610,-2.481878,-9.985285,-3.798358,0.082653,-8.227947,-6.475987,1.066968,-1.227941,-5.500950,-4.247588,8.680651,7.682077,9.297413,-7.086434,9.909238,-5.684084,-4.440874,-4.993422,-6.024247,8.851117,-1.769467,3.533377,-6.592154,4.173029,-4.201269,-4.755122,5.764664,-5.990950,7.759312,-9.461292,7.754004,-2.420159,2.191698,-5.035610,-1.643250,-7.426964,-1.262538,-8.968206,-8.894509,5.136184,7.809749,-2.376839,-0.653078,-5.563962,-9.995799,-8.119959,5.747663,8.128494,6.576416,-5.729363,8.533302,-3.309965,-6.308936,3.872937,-2.206554,0.326876,-8.780284,-7.160732,-4.438599,-5.866669,9.983895,0.083705,1.308950,8.545707,-7.918449,-0.666773,-9.718361,3.407162,7.607881,3.662600,-6.740796,-0.154592,8.464517,5.847769,3.364638,-4.053829,-8.193846,9.449557,-6.017815,-5.472798,-7.247858,-5.781137,6.695739,9.244766,-9.943826,-8.378975,4.902014,2.671655,9.185570,-6.283895,-8.846519,8.263006,-0.726994,-1.231425,9.105747,-3.058603,8.886885,-3.531771,-1.078231,-4.138817,4.575196,4.945953,2.939981,9.681080,0.184734,4.836745,-0.075920,-0.490855,1.013088,6.820173,9.804049,-4.212252,-3.363970,8.293499,-2.450064,-1.016814,-9.455539,-1.945331,-7.769196,-5.101124,5.176402,-8.821554,-3.334260,7.010929,7.336749,-8.286972,-6.200127,-1.793885,-6.239041,1.317826,9.871997,-1.597115,-0.233029,0.867164,-4.292847,-3.026822,5.247935,6.631959,-0.814503,4.408061,6.897564,-2.152523,-7.189990,-3.375232,8.276449,1.872767,2.275081,-6.789660,-1.569524,6.642770,-1.702378,-1.873333,-4.770076,4.945408,-6.681435,-1.384940,4.751206,2.133023,9.644460,-0.044141,-8.865273,3.210821,0.493102,1.149399,0.116998,-4.256628,-1.637855,4.022541,-4.894640,1.657612,9.596656,-5.390715,7.220687,-4.381819,8.867295,1.205125,-8.049307,-5.650164,-3.306830,4.159543,-8.294503,0.297259,9.486929,0.745433,-0.793156,-9.606099,-9.267696,-0.613855,2.640656,0.403307,5.891661,-0.310778,3.369662,0.731575,-1.130792,-3.569523,-0.346554,2.328036,-3.718844,0.632631,-2.905049,5.464237,-4.865474,-5.042500,-0.827613,-8.544309,-9.850097,-7.571473,1.400391,7.999174,-9.299970,-0.100974,-4.133595,-8.503199,-2.934222,5.968997,-2.714046,-2.073335,-9.979334,-6.129802,-6.997762,-1.437128,1.262597,-9.130293,-7.543495,-9.322514,3.751211,5.139346,-0.677946,3.247064,6.344866,5.631118,1.353659,-5.713213,-6.464198,-8.976222,8.024851,7.027867,7.821104,-3.438605,-3.300864,6.938737,2.392158,1.302105,-2.416925,7.908373,2.909502,1.176590,-0.634749,-7.179537,-8.503660,8.197113,1.934011,-4.637045,-2.151746,-8.165671,3.898612,2.530979,-1.881104,1.272925,4.654110,-0.134960,6.548261,0.267228,2.130352,1.201219,-3.402974,0.076284,2.852257,2.244348,-0.615664,-6.830771,4.536305,2.356521,-1.436429,-0.220390,0.644823,-4.471825,2.716013,-8.543905,1.076718,-7.215780,-2.344529,9.192816,-0.012469,3.226934,-9.996644,-8.270040,1.051109,9.652537,-8.317576,9.216114,-2.864585,7.478637,8.282035,-0.078314,6.939377,9.266256,1.749964,4.450668,7.472607,-0.952470,3.725804,7.259873,-6.834381,-7.783916,-1.799818,-0.391432,-8.137877,-7.700191,2.986808,-3.979966,-5.918259,-9.995653,4.163722,7.120423,2.438138,-8.082116,-9.742900,8.775578,0.207018,-3.186614,-8.584301,-9.767441,-8.710671,-2.612105,-6.226638,-2.821015,-0.693890,-5.652993,-3.149653,-2.833094,3.657224,-8.042087,-4.624316,0.318058,-6.339414,-2.600360,-6.298114,6.172552,1.092891,3.877895,-8.682421,-3.633329,-9.482322,-2.558681,-2.321377,-3.523768,-4.862716,-4.980013,4.633320,-2.644726,7.627086,-9.250437,0.730277,-1.211250,6.847082,-0.779358,2.097804,2.445967,2.599875,-2.783979,-4.378545,-9.448000,-6.865883,-6.400932,-8.360607,8.307765,2.456153,0.432402,8.897099,2.212835,4.662083,-0.913262,6.874571,1.278301,-6.073539,-7.511672,-7.814365,9.356870,6.292653,-0.831957,-6.489628,6.031696,8.937203,-6.552656,-9.191140,-6.083448,-9.735427,-1.429355,-7.430115,-8.155690,-2.419479,5.148381,1.770245,8.726674,-4.453013,-4.023538,8.155980,-5.829164,7.563307,4.527799,9.687306,0.277048,-2.188327,2.635632,4.017619,7.974724,-0.009386,7.400194,5.188584,5.385703,-1.383529,-4.833343,4.324362,2.486713,-4.362079,7.151235,-6.557082,0.365492,-7.314425,3.363860,-2.580567,7.218565,3.445762,6.497310,7.449296,7.337952,-7.690199,0.341718,-6.740571,-9.515162,2.562360,-4.764768,5.036192,4.770303,-3.589695,5.831419,3.154276,-2.414925,4.063141,-9.506904,-3.007798,1.765239,3.850341,-7.637228,1.331577,-9.082711,-1.939230,-8.242784,-4.949903,-4.704718,-3.290028,-0.187717,-6.736035,-5.350635,-2.693926,2.461116,-7.445986,9.436440,4.171998,-0.863492,8.381404,-8.254414,0.126473,4.963291,-6.089846,3.882648,5.030484,-5.976817,-4.921255,-8.295706,1.761945,0.668411,-9.782282,-1.469971,-9.483446,-3.277773,1.325716,-7.926715,1.537509,1.939351,1.313018,-8.469214,-7.885671,-8.890178,9.687858,8.289489,-5.525630,5.814285,0.040475,8.170848,-9.218808,2.558750,-0.574725,-6.877139,5.180321,1.940995,-6.411965,-7.147318,-4.115399,0.637155,9.228740,9.901490,3.172620,-6.555239,-5.137846,4.503683,4.172619,-9.060570,-1.867533,6.273936,-3.632265,-3.561349,-5.424761,7.806808,1.295791,-5.982258,9.905563,9.555038,-9.138619,-0.334571,3.272746,3.942203,-1.722036,-1.890779,9.450124,8.960168,-8.234381,-6.223297,-4.972769,5.980830,0.004029,-3.135524,9.340731,9.420699,5.522519,-4.240293,1.427766,1.315472,-5.378104,-5.822665,5.019857,1.112901,5.141291,-1.717185,-2.242168,-9.648092,0.972383,-1.231554,-8.378536,8.576174,9.645716,-0.247912,1.107640,0.438279,9.179556,7.819027,4.235883,-3.526778,0.326520,-7.482455,-3.621843,1.552417,0.021227,1.966103,2.031640,7.740947,-2.498870,-4.054999,6.239740,1.841900,0.290382,8.882063,-6.517018,-5.203156,-5.844607,8.507545,5.918824,-3.962990,-1.327043,-8.238575,-9.297063,3.946242,8.302079,3.079343,2.371504,3.745735,6.046359,4.998579,-2.226485,7.102198,-0.814992,4.344308,4.035028,-9.427866,4.236540,-4.132192,-0.384017,4.853634,0.680667,-9.944481,1.348581,1.574421,-2.762589,-3.491833,-6.618305,5.285901,-9.934269,-2.165272,-6.230885,-9.180222,9.943622,-5.491175,-9.018466,0.032921,-5.107117,-2.214701,7.846717,-7.824788,-5.147803,-7.056338,8.198159,5.385034,5.512589,8.324922,-6.667376,2.247741,-0.913165,8.357649,1.399951,-0.955333,-7.794908,-7.258604,6.592411,9.918793,8.459080,-3.650271,0.531194,9.078614,-5.747148,-6.874847,-5.607998,-7.597099,5.625819,2.163232,1.717568,-2.367274,-2.874908,3.116830,-0.824841,1.568879,6.123301,-2.518083,6.325715,0.640956,-6.151854,-5.450512,5.538007,-3.131209,-6.672514,-2.451911,1.672235,4.202208,2.340013,4.439610,5.993284,8.549152,7.267327,0.705952,0.030560,-0.427683,-7.536737,-5.008060,6.705103,4.086405,-0.155140,1.173357,-4.003791,8.880864,-8.791592,6.465170,8.919237,-8.440691,-5.103922,8.701482,-5.380573,-6.710527,-7.845410,-5.414405,6.744758,8.955528,6.882280,6.154364,6.698030,1.265673,-2.718851,6.678983,-1.788333,-4.140310,0.151908,-0.784320,5.168212,8.481317,-8.885698,1.869966,5.900374,4.611470,-3.628431,-7.647012,-7.481781,8.015042,3.773177,-4.781498,-3.956626,-8.985195,7.736314,9.787929,2.669289,-2.205407,-4.068996,6.646331,1.955851,7.767974,-4.791627,4.663395,5.393225,5.434050,-5.167482,-5.225284,-0.890778,-3.833781,-0.811330,-7.100554,-9.356368,1.034754,-9.916565,-2.717954,5.301247,0.532828,-3.310358,-4.817797,9.936533,-9.883816,-7.370404,-2.306840,2.403948,-6.443379,-9.248418,-7.455589,5.154550,-1.423738,-2.616050,2.888062,-0.607299,6.274249,-3.767442,-8.729441,1.482058,6.156527,-2.951507,-2.281885,-3.228166,7.443361,0.123076,-1.163914,5.756793,9.660455,6.179333,2.229448,5.455051,-8.306528,6.896611,-6.991512,4.426043,-1.247334,5.909141,-1.942777,6.036394,1.741497,2.868774,8.827637,-0.101020,-4.777911,-2.429565,9.439564,5.299847,9.940459,-4.637507,5.987027,7.968172,4.964065,4.508820,-8.755859,0.286027,1.711794,4.489028,3.981552,4.350319,-7.070085,-8.493716,-5.484719,1.120792,-7.368024,1.642786,-1.640002,5.904553,1.228167,0.653627,6.561013,6.040963,7.866864,5.617695,-1.019599,-8.263989,-4.037232,-8.130684,-0.547702,-0.591336,-5.940345,8.431715,-1.187453,-8.328399,4.442980,-2.441381,8.828557,7.595204,-2.442833,9.504063,-1.172487,8.145153,-9.793367,7.918819,-5.487394,6.935148,1.201591,1.519507,0.248010,4.441817,9.463833,9.878232,-0.483862,8.162024,-8.184708,3.367875,-0.589610,7.027578,3.875610,-6.197839,1.946791,-5.618553,-4.990837,-0.962825,7.363305,-9.125328,2.054751,7.008346,-2.950001,1.547273,-2.388152,1.240757,1.860363,3.400933,0.143174,-0.008503,-3.219443,0.191509,-5.148569,-1.080242,-5.885071,-8.146794,8.075428,2.968625,-7.567586,-0.297943,4.935931,-6.926702,-6.520816,5.625751,2.901926,-4.500794,-8.541893,-3.515534,-7.738263,6.285492,6.703360,-8.261644,2.945922,-0.356942,-5.263205,-3.828912,4.637118,4.940459,1.562747,5.292712,-3.138205,-5.257707,-6.446222,-4.433814,1.558852,6.314622,7.308809,0.167834,0.525291,6.444110,-7.690055,8.524884,-1.348116,-2.435520,-8.271405,-8.556182,0.523708,1.227583,7.441865,-4.484770,1.853188,7.574470,-5.185265,-2.802070,-6.223382,4.525504,7.456277,-9.875565,1.419042,4.946429,2.548564,9.336413,-1.098122,-8.645835,-0.561986,7.472229,-2.517928,-5.581296,5.804753,-4.536677,-8.168618,5.363607,-0.413114,7.911223,-4.852011,3.880716,-2.942867,-5.819684,-9.533927,-5.196473,-4.586426,-7.557917,-3.064389,3.496276,8.772807,-6.017929,2.037896,-7.610230,8.541584,-9.568578,-1.015822,5.310372,-5.817643,-6.397226,-3.766169,6.018689,-8.107808,9.153533,-1.480693,-8.355407,-9.560683,-1.915520,-2.664289,-9.868416,-3.738508,5.006431,-0.132995,-2.735665,7.566138,4.603955,6.755771,-0.688039,1.941274,5.831048,-9.258973,9.799259,-9.525365,-8.214655,-6.306129,-0.010478,6.112888,-3.821992,3.506786,-0.961585,7.082507,-9.204211,-4.080291,-4.996854,1.875306,-4.946741,5.227380,-0.702083,9.904806,8.225462,9.160636,-9.975848,6.977260,2.754051,9.973169,4.077061,8.066319,-4.569633,-7.172052,0.370398,-8.608046,8.677448,-6.280192,1.873760,2.214245,6.903142,-6.514116,5.321854,-4.009890,-3.232861,1.151533,-6.943677,-1.975904,-1.146400,5.452048,-0.287349,9.520713,-8.185133,0.346280,3.205495,-9.634534,-9.597811,7.782446,-6.844334,-0.923396,8.328650,9.501021,-0.609415,-9.682036,-6.936061,5.242291,0.438701,5.549596,-9.875902,8.440705,1.750982,-0.089974,4.331349,8.956589,-0.104276,-5.053917,5.567023,0.882020,8.265550,6.667239,-5.589760,-1.975123,3.986387,9.525021,9.876642,-9.631612,-9.756840,-6.652823,-5.386374,7.025086,3.166952,-5.526313,4.459201,-8.916090,-3.647557,5.545518,-1.272043,-9.880763,0.872405,9.073677,3.213322,8.874097,1.194166,5.286841,8.851051,-3.175322,-2.991245,-8.430377,-6.379965,4.684333,-8.440198,8.173902,-5.969277,-7.350449,6.505272,-2.103693,9.803650,-9.260369,0.571618,-7.221929,3.365294,0.238873,-7.258004,5.284093,0.200803,4.107577,6.325201,-7.251081,-6.148738,4.543723,8.493078,-2.597160,5.350182,4.477294,-1.096734,-3.433969,-0.512090,-3.559869,3.084509,5.905125,-1.523582,-6.381774,-6.010845,8.682832,2.631223,-2.415697,5.445563,-1.435807,-1.431292,7.150040,6.476442,-3.917077,-3.199630,-1.927090,-7.256186,-4.144242,-7.028990,0.412359,9.853694,-4.858873,5.043835,0.964708,4.969930,-2.639697,0.073250,9.164510,8.196306,-8.578377,-8.346362,1.509017,0.583901,9.243813], dtype = "float64")#candidate|3865|(2304,)|const|float64
call_3863 = relay.TupleGetItem(func_1917_call(relay.reshape(const_3864.astype('float32'), [8, 12, 15]), relay.reshape(const_3865.astype('float64'), [2304,]), relay.reshape(const_3864.astype('float32'), [8, 12, 15]), ), 1)
call_3866 = relay.TupleGetItem(func_1921_call(relay.reshape(const_3864.astype('float32'), [8, 12, 15]), relay.reshape(const_3865.astype('float64'), [2304,]), relay.reshape(const_3864.astype('float32'), [8, 12, 15]), ), 1)
const_3869 = relay.const([-0.604792,6.038470,5.273731,6.757771,2.161759,-8.026755,1.191106,-0.940896,8.521279,0.037472,-9.722889,7.042927,8.262909,-1.222495,-3.336692,-8.979352,7.443058,-7.291277,1.549112,-5.299029,7.892285,-3.339649,-5.807022,3.015466,-2.105903,-9.471096,2.858853,-6.532864,6.168914,5.606904,-1.466471,-3.550597,2.195697,-3.898147,-0.392913,5.754678,-3.361705,6.283412,1.043685,-8.045505,8.322803,-5.692767,-2.766679,5.800995,8.363040,0.858166,-8.757618,-3.242279,6.508674,3.579277,3.302766,7.786877,-0.650031,9.789371,3.736897,7.129441,-2.911860,-5.949625,-4.689232,-3.160620,-6.144552,-9.206567,-9.220155,5.458479,0.973099,7.002144,8.126622,-9.369528,5.048590,1.734062,7.248420,6.711254,-0.866762,-0.093824,-0.497032,2.664536,8.551341,4.683984,-8.292338,6.419908,9.248867,-6.113520,0.028870,-4.183054,-7.666393,9.533835,-1.335532,4.033701,-7.606443,-5.599036,1.929060,-1.357581,2.281799,-3.068701,-0.999291,3.977427,-2.327899,-3.079429,9.811675,2.606821,4.133100,8.112428,8.741058,-9.359509,6.635844,-5.955748,-8.049231,0.120105,8.617862,4.102637,0.349778,5.970586,0.544113,7.657997,3.584054,-7.833487,0.587650,-6.440358,8.877140,8.683101,4.588567,4.940974,-3.586657,5.495773,-9.104975,9.594919,-0.155548,7.015030,-2.949418,-1.874535,1.934908,-5.889294,-2.743853,-0.640439,-6.051605,-1.400267,9.086636,2.042585,-0.144777,0.313816,-6.957905,-1.467229,-1.450089,-8.910068,-0.430973,-3.255181,0.162178,1.858447,7.739929,6.855394,5.049686,-4.847520,7.820712,-8.792377,-7.280126,-4.717516,-3.241566,4.863398,4.784885,4.774447,-8.210032,8.201832,3.099413,-2.679061,-5.677821,-3.243835,8.219276,2.253540,-9.266802,7.727613,5.628079,4.411062,-1.762159,-9.040311,-5.218158,-2.017544,5.993973,1.287293,-4.611360,-0.535890,4.829279,-2.894878,0.623922,-9.550012,9.110451,-8.584342,7.239901,-2.178388,8.515731,3.861884,-0.550113,-3.436230,-9.995943,-9.125524,6.372923,8.927198,4.638754,-9.590142,2.266354,8.952794,-4.813595,-5.374778,5.549198,7.833797,9.193998,4.964603,-8.285802,-1.643285,6.356758,7.024305,3.579279,2.920405,-6.581852,7.042638,-8.035846,-1.747769,-5.300670,7.150465,9.080281,-6.903184,6.665735,6.107375,-5.944073,-2.641470,-3.467396,-5.234707,8.605937,3.942816,3.245861,8.352837,0.768466,-4.597843,-1.794930,0.076184,6.786180,0.271928,7.950123,-7.536334,-5.667394,6.266522,0.698352,-5.852050,-5.536264,-5.318683,-3.613161,5.744082,-5.683982,2.554550,3.094169,-5.937641,5.725497,-8.487329,-8.815874,-8.617678,9.002853,-0.991463,4.150422,9.443686,-5.112413,-3.185236,-1.584788,-8.612461,3.945853,6.277713,-9.566917,9.512225,7.035945,2.132948,9.152180,-8.928271,3.521753,8.271903,9.090602,-5.922463,-7.123264,-4.863260,5.989842,7.959832,3.298132,0.740379,6.613560,8.285301,-0.455604,-2.615563,-5.161359,9.586211,9.326675,-6.679432,3.669739,-8.134802,1.554179,-4.058144,8.335002,-8.649630,4.769626,7.008564,-1.942711,3.715954,5.647661,-4.246412,8.766724,5.498200,-9.541567,0.329348,1.974064,-7.359287,8.936525,0.790239,-0.180020,9.177018,8.614897,-5.256031,6.991658,8.911495,-5.439866,-2.713485,6.219585,-5.760215,2.259925,7.540340,-2.964683,-8.992140,8.490333,-2.000334,9.553738,8.666108,-7.044117,-4.548270,7.462470,-8.766293,-6.423746,6.918189,0.391664,2.087920,-1.730270,9.283133,-9.043594,-3.404203,6.170023,-0.782189,-8.124695,5.907119,4.474609,-3.700213,5.116635,-8.947227,9.780853,6.768195,-7.564644,2.427323,-1.638176,6.715603,-5.957451,-5.031722,-0.255089,-6.071466,-3.434681,-3.228451,-2.314068,-3.804682,9.287106,0.716845,9.541671,1.912666,5.288595,-0.254153,6.287742,0.345616,6.001552,8.458300,-2.325611,-2.531699,-3.072789,-1.580138,4.726066,-1.977943,-1.169101,3.921916,9.962204,8.398635,6.280830,-4.792062,0.905392,9.807946,5.101620,-1.724017,-2.478353,-0.579216,9.176696,3.443969,8.933527,-9.220255,3.161676,4.045592,-1.170875,-8.890143,-6.075696,1.797313,-1.712178,-2.783089,5.302326,1.274753,7.492276,-7.198103,-3.533485,5.345618,-6.607962,8.074051,5.635427,-0.709767,0.700064,-2.195517,7.829823,4.199333,-9.547858,3.307593,3.566988,1.654909,-2.064640,9.131328,-1.761034,-8.203727,-3.819937,-2.319866,9.219279,-7.447065,9.249663,-1.029106,-5.078485,-9.115443,-6.838056,-5.206798,-6.004339,-8.991219,-8.328160,-8.830392,4.865487,5.629965,-4.607710,1.502659,-4.197640,3.828304,-5.490134,-6.164088,2.115506,6.852909,-4.793939,3.051233,-4.275478,6.289649,-7.689672,4.938426,-9.227087,1.268141,-5.625711,-4.201470,-5.971408,6.258868,-4.411583,7.845345,-9.449263,9.946579,1.250876,-4.888483,-2.179877,-3.726183,2.296156,-9.382591,-1.982030,-6.293469,7.119070,9.229285,-8.955728,-2.631737,-1.919891,4.629884,4.300239,6.355465,3.296582,-2.985512,2.159741,-6.575901,-3.488111,-2.946949,6.699294,8.938439,-2.074196,-7.957421,0.690089,4.690518,5.172085,8.813628,6.762338,7.677512,-5.518621,-2.636751,-2.282479,-7.325048,-0.982045,5.861531,3.784762,-7.087850,5.770455,2.105059,4.848389,-2.236652,7.150794,1.963321,-6.340777,5.744683,-7.243270,-3.229883,0.608535,4.731987,2.307319,9.126080,-2.680202,-0.486123,-0.209215,-1.716490,-0.395590,-2.871456,-4.502098,-3.562158,-4.930676,2.344252,-8.036585,6.158993,-6.859214,3.435982,7.395762,4.668978,-1.745170,7.215380,4.173897,-5.249284,-7.064881,7.094655,5.685110,6.088310,8.623657,-0.203120,-5.136793,7.596043,2.469302,1.833228,2.429069,-7.099748,-4.792573,4.334537,2.774109,-6.751534,-9.366401,9.547849,4.049967,-2.773933,9.006387,-8.923192,-1.654423,1.010490,-9.932904,1.008304,5.355350,9.466190,3.583064,8.386040,3.961966,8.073618,0.893870,1.094875,3.317432,3.112890,-8.935949,4.412666,-2.027579,-9.270890,7.965827,-8.476180,8.010437,-7.624917,-2.565438,-3.321084,0.622090,-3.607758,-3.132768,-3.692033,7.181991,-7.170743,5.171915,-5.131389,-9.462547,2.318952,-9.599354,-9.869145,2.906530,9.578845,-7.303565,1.070367,1.717976,-7.144087,4.536023,1.737684,8.867525,0.639146,7.260215,-6.730236,-0.566786,1.809134,8.954712,0.384019,2.435780,2.521589,-5.590871,2.217533,-4.445844,9.385774,-6.320009,-8.778627,-0.953123,0.911994,1.282470,-6.695638,1.410704,9.606235,5.329597,4.869908,1.518651,5.699990,-7.799388,6.083760,-6.114884,-5.109203,7.779458,-2.542218,-2.343425,-2.630434,7.434866,-2.730956,-0.021595,-6.650824,-3.731443,-5.528839,-7.117932,4.210183,1.331832,8.312045,4.282182,-1.945228,-8.142894,-4.219072,-6.935655,-8.555347,0.158091,-4.837580,-2.426063,-5.937824,4.560281,-6.604117,-0.878851,-0.664825,-1.751815,0.507405,6.533567,1.558208,7.597013,8.428903,-3.616760,9.914903,-1.153867,7.815504,-5.011057,6.262305,7.720605,2.919568,2.568859,3.800760,0.986008,8.642287,-1.731704,-4.272684,-3.378583,-8.518608,-5.013787,8.503155,9.798577,1.957628,-6.069411,9.290228,0.333732,0.787111,-9.398118,-2.450575,2.849184,8.611556,-9.021269,8.664994,6.894177,5.346443,-3.158269,-1.810755,-6.951770,8.530517,-9.802524,-6.137631,-7.891667,-1.549439,-7.485962,-2.172785,-5.618869,0.055231,-2.179958,8.133098,-4.946202,7.016196,2.927218,4.788865,5.058001,-2.505537,9.324685,2.324817,-2.939678,0.907960,3.964343,8.931765,8.315550,-4.880175,8.845312,0.586033,5.784655,-2.895391,-8.756292,-5.518174,7.473654,7.348881,9.531592,-2.225324,-6.942733,-1.011966,3.151119,4.253581,-4.303259,-2.398536,5.211672,-9.391141,-9.823994,-2.198952,-3.244201,0.157867,2.624196,-0.471706,9.580609,1.684085,-3.744956,8.973617,3.653321,-1.448935,0.887384,8.192258,-9.626360,8.055916,9.810314,2.254596,-8.491129,3.360364,7.405222,-5.471343,-5.166066,-5.484648,7.756730,-4.464682,-6.182068,-9.250238,-6.036875,3.334225,1.113646,2.293701,-2.483457,-2.879924,3.011146,-9.280916,-3.720213,-4.583957,-0.520065,7.789959,-6.868367,-7.048825,4.316254,-6.697325,7.178312,-4.470919,-7.967951,9.531927,1.683104,7.613508,0.041373,2.390844,-8.753098,-4.866902,8.080522,-6.968933,7.444191,-0.813708,-8.748232,-6.774277,-3.356764,-5.657404,9.121228,0.738823,-4.223041,2.735735,2.932016,0.395199,-2.424781,-5.869910,7.062531,-5.086260,-9.833248,1.454073,8.644620,-8.461370,3.591806,6.994096,-8.929087,8.388310,4.658537,-5.764641,8.693748,5.913093,2.046063,6.233713,-1.866887,2.754783,5.914937,9.983151,5.040602,-4.512141,3.590721,3.232011,4.476493,-0.537056,4.146713,9.510048,-2.268241,0.414911,-5.367899,-0.598104,-9.787929,2.011133,0.762317,-2.901763,-5.224516,4.483470,-9.098775,1.360255,0.275462,9.582513,-4.117361,8.566484,8.240579,-8.778996,-7.120748,-4.281385,4.559786,-2.823619,1.513963,0.559098,1.493918,1.031065,0.317527,5.094651,-8.892459,0.621573,9.395028,8.636663,0.938557,8.944684,-3.243557,-7.156182,8.734646,-0.749050,-0.841029,1.185268,-8.850038,1.196186,1.309171,-3.511488,0.047414,6.596847,2.402350,3.749937,-4.851438,-8.107459,2.889856,-3.929785,7.536279,2.404110,-4.158001,0.063590,4.346367,-1.414468,-6.355545,-8.040843,1.113837,-9.228540,-1.046328,4.853562,-8.065211,1.103185,2.229628,8.780962,4.649255,-7.262447,3.976619,-1.950029,-9.481683,5.669431,-0.648217,7.021827,2.576307,-1.654543,5.236653,4.489953,2.075968,8.834402,-8.679702,5.693137,3.902112,-0.575727,7.213318,2.316168,9.113667,-0.586247,-9.744353,0.571318,-1.000448,6.753444,-3.511346,8.635198,-5.383306,-0.848584,4.538957,-6.846158,1.285380,2.906827,2.181960,-7.383072,-6.859698,-7.130555,-7.178617,-2.976008,2.343754,7.880158,-5.967181,2.693384,8.358539,-1.260641,6.455713,-3.295688,2.368682,-8.274859,-0.816147,1.993726,5.569023,-9.315534,-3.920109,-4.852952,-2.126044,7.448443,5.269485,6.512877,-3.482307,9.079372,-7.442664,-1.770208,-4.063733,9.223610,7.380519,8.648659,-4.974143,7.098171,-5.132644,1.679632,5.223854,-9.383186,8.622463,1.790319,8.608810,-8.119677,-2.703449,0.547157,7.570257,-5.074985,1.711627,6.713531,0.842340,-6.642931,0.450685,-9.789489,-1.826703,5.541774,7.781239,3.467264,8.114474,-2.634602,-5.306941,-6.579891,-2.762961,4.615460,-8.182601,-0.685825,2.013815,-6.848066,-1.420694,2.123011,1.982091,-5.534794,4.364741,3.089901,6.712788,1.482442,5.208986,6.505447,-5.535875,8.834696,-7.924401,-1.118452,1.349376,-2.827071,7.961690,-5.396279,-9.439257,3.307409,2.670454,-0.586535,3.268850,-3.218042,-3.053556,-3.087814,-3.310557,3.902469,4.179035,-2.801069,-0.066777,-5.926235,-5.081240,-9.564806,-9.281064,8.009332,-4.681109,-9.191450,1.460482,-6.164382,8.839892,-9.630726,7.023145,-3.212199,8.837549,4.922976,6.428818,3.397365,-2.359183,-9.758451,-1.541023,-8.908179,2.842421,-7.364703,-1.222550,-9.032753,8.814001,7.407845,1.168010,-9.073205,4.114515,-9.499516,3.666278,-4.430269,-4.487499,-0.909989,-6.638511,2.829236,-1.128600,-0.572921,9.377361,-0.051831,9.374344,0.205188,9.521775,2.119057,2.612052,5.807830,-6.288821,-8.280620,-1.060607,4.367296,-4.307800,-7.822626,-3.752424,4.552648,-1.940013,-9.933493,4.293858,-5.623063,6.153470,6.390471,7.551947,-9.189533,1.313492,-4.858270,5.155553,-9.238126,7.897015,-2.377125,-5.386665,8.069683,8.632436,-3.813984,3.408918,1.248432,8.287971,0.152566,3.261833,-4.210987,-5.683308,-8.304239,-6.009257,3.501789,-7.205162,8.172229,8.127323,4.460284,-4.936763,-0.883992,-4.717186,2.765519,-3.758752,-1.978404,-3.743705,-9.008686,-2.796873,-2.812290,-5.315825,-5.847000,-5.442402,2.699315,-5.045576,-2.925817,-4.775429,-3.544035,5.027786,-8.756530,-7.693932,8.673369,8.266024,3.909929,5.088432,-5.250613,-5.970420,-6.534025,-6.980149,-0.496581,-7.309342,-4.639367,1.315713,3.560967,-7.253463,0.236391,-0.294914,4.697025,-1.662423,1.227387,-3.361002,7.554668,-0.726044,5.839573,8.135514,5.765569,7.500069,1.506849,-7.027532,0.700465,-5.413052,1.326501,2.346001,2.594780,-5.340716,9.220463,-9.315933,9.191354,-9.846494,-5.934983,-3.085751,8.206150,5.040114,9.473815,8.403534,-4.366893,8.056480,7.842845,-7.439376,-0.198198,8.741247,5.716505,8.804739,7.061082,-9.219093,3.382699,5.943827,-6.056730,2.966704,6.024408,-6.863762,6.048154,7.614802,-9.696317,9.499544,-8.087904,5.672854,-1.935813,-8.254698,-9.169864,8.038687,-3.021025,2.359513,5.363731,-1.998652,2.253569,-9.431997,-3.119814,8.470768,3.934300,1.657219,-0.370126,-5.488106,2.724319,-6.349516,8.494124,-5.302497,-0.074897,-1.524700,-3.151228,-6.595879,7.990951,-8.880307,1.075218,-8.617194,-1.482857,-2.003931,-1.473321,-6.421473,-1.218258,-2.515744,-4.313613,3.866480,-7.509386,4.611296,-0.477098,-8.147490,-6.432081,0.950692,1.152338,1.866179,6.794873,-2.562611,-0.541902,-0.790491,3.372688,-4.086028,9.695900,-0.768268,1.301802,-4.760083,-6.342299,3.983415,-8.678849,-9.262408,-7.702055,0.417426,9.588970,-6.933827,-2.327135,-6.365250,0.963347,-7.163768,-1.189191,-2.335017,-1.656144,0.019728,6.064624,8.707928,4.038446,8.890488,5.053681,-0.445601,-1.217414,-2.641873,2.935240,-8.394291,2.638298,1.641848,-8.018052,9.557550,-1.073495,6.846603,8.695124,2.881523,-7.079924,1.529650,-6.562718,-1.176388,-3.843392,2.717971,-5.830832,-8.902050,-8.111499,5.585430,6.203785,3.372137,-9.162732,7.459861,-7.916460,-6.461111,-0.490977,-3.731246,9.471598,8.355357,-4.237705,0.603710,3.059190,-1.955671,9.522343,-6.420274,3.937166,9.135687,-4.587668,9.633100,8.708039,4.709459,8.880432,-0.635209,-6.974347,-3.056833,4.173366,7.405647,8.240079,-7.983978,-3.424781,9.330130,9.083341,6.255319,-6.830434,-5.024737,-0.375043,1.724999,3.722746,8.131640,5.996400,-4.832697,0.369020,5.069531,-4.717374,-3.402314,-1.504476,-4.547553,-3.307210,4.539080,-4.552139,-6.021164,2.872058,2.680516,-1.935985,7.062277,-0.089899,-3.357167,2.283925,4.755640,1.633921,-6.253593,0.814031,6.741445,-2.284766,-4.532237,-7.664110,-4.331408,-3.345966,6.033600,-7.833144,4.208649,-3.053234,-9.805538,8.909570,4.640013,3.751904,9.174276,-3.840950,-0.271561,2.224541,-9.793206,-8.327391,-3.689067,-0.163331,6.369884,-3.419011,6.417837,-7.461546,-5.739139,5.493308,-5.567258,-9.972718,-1.551722,5.647524,5.873353,7.587227,-7.994229,-5.598112,4.430434,-4.028432,5.011994,2.229352,-3.413660,3.785544,7.522592,-8.054579,5.743976,5.638753,-6.788580,2.309019,-1.368620,1.745518,-5.623481,2.137299,-9.632867,-7.622356,-3.089139,-2.771672,7.863864,5.450849,1.037979,-5.153534,-7.125202,-5.345035,-7.898422,5.154161,-7.399967,-7.752319,-3.283580,-3.653482,4.353565,7.125038,-7.384574,-8.903159,9.250355,1.420181,-5.929283,4.386136,5.418940,9.955039,2.390783,-1.428594,4.815798,-9.514719,-2.687918,-8.220296,8.205397,3.818406,8.036128,5.000646,-6.005955,9.013989,9.540476,9.402918,-9.933209,-6.117894,5.679722,-1.721158,1.658687,2.641159,6.644293,-5.299825,7.357768,3.244593,9.498603,8.683082,1.579354,-3.435939,3.457836,2.432310,-6.202842,-1.683120,3.794357,-9.018850,0.755233,-9.826492,1.412990,-0.659211,7.056879,-8.941704,-6.445210,-6.255057,-1.628508,-2.010066,-4.084167,-6.709665,-1.375250,9.536951,5.367463,-6.177727,4.346362,6.399895,2.908038,4.564322,1.114082,-4.822923,7.395986,8.105604,8.005583,6.692984,-5.325446,5.150507,-2.753618,-9.416240,-8.210380,1.608658,7.008774,6.998970,-4.607210,7.817800,-0.896308,3.737351,-3.492101,3.320585,8.012602,-7.961688,-6.393436,-6.571248,-9.758711,-8.910239,0.301410,-8.957471,1.791156,-7.080204,-6.893937,2.298077,2.711905,-3.031774,-8.166810,9.909382,-2.228361,3.199658,1.224034,-0.386601,-6.069361,9.108466,-5.938695,-5.637446,6.382252,4.029761,3.853365,-3.450016,5.534258,-3.682543,-1.084215,9.790186,3.486677,-0.490769,-9.253173,-6.016708,1.071278,0.616455,4.660721,7.317597,-5.499076,-2.766147,-0.077893,-0.109719,3.722878,9.156418,-7.395930,0.306736,9.753793,1.256744,-8.129036,-9.843473,8.689878,8.828245,0.684719,7.130751,3.374890,6.475692,-6.636452,8.100907,8.466133,3.599853,-4.458802,5.759016,-0.581609,6.611744,0.922341,1.466429,2.578786,7.575840,3.466951,-6.457948,6.811030,-7.006051,3.467923,9.975657,-3.473084,4.921775,3.367403,-8.494692,5.148206,-2.130047,8.253606,6.854737,-7.698477,-6.036951,0.565426,-2.331448,-1.642608,-9.203931,7.620953,-4.118052,-0.642709,-1.115536,4.212055,-1.124806,-6.880905,4.729040,-1.615987,3.018250,0.015135,-1.306627,-9.773923,7.347367,-3.032717,1.705024,-8.476832,9.170872,7.167946,-6.220926,8.345004,9.116758,-1.449884,4.172154,2.839503,9.067111,-0.946412,7.495893,0.987003,-1.432704,-3.467645,2.071549,6.862575,2.451149,-8.316094,5.031394,-2.714304,5.425531,5.029178,7.737014,4.293351,-4.303098,6.444459,0.978805,-9.641808,-7.165414,9.906112,0.435373,-7.251780,3.627709,6.229259,-2.573869,5.880532,-4.123154,8.087416,0.112259,-0.629795,-2.800592,3.475616,-1.412852,4.881110,-1.236518,-0.145118,-0.059361,-3.869799,4.835908,-1.280019,-0.194740,-5.326319,0.108466,-6.616809,-0.248668,-7.424180,-5.705432,-6.619647,6.968240,5.355440,-0.168299,-0.228151,6.959950,-0.068502,-0.537567,-8.563242,-9.608681,5.027167,-1.066225,-3.909275,-0.727087,-5.925219,-5.748966,-1.931222,-7.258503,8.927180,7.006471,9.349125,8.434908,-3.030504,6.730263,-5.770455,7.920998,1.448265,3.170308,-4.833197,-5.119266,5.372530,-7.115158,-0.005866,4.074399,8.052870,2.706593,8.347368,4.305083,-3.077302,1.040064,-5.498530,-2.891323,-2.630366,-9.461363,-1.594209,3.166315,9.983235,4.911421,2.370820,-5.440839,2.572477,0.934404,-6.629333,-4.853969,1.174212,9.109110,-1.107712,6.085666,3.968435,-9.994315,-4.901783,8.411163,6.368922,-3.292119,-0.354537,1.680410,-6.437004,-5.374626,3.894421,-7.240864,-9.492806,9.874460,5.825926,-4.147088,-9.296380,-1.124883,-4.109399,-6.038524,-3.766697,-2.907301,0.821340,1.548542,5.398970,-2.123241,-2.043814,5.711608,-9.015601,-3.781876,-7.812204,9.179041,1.443652,9.670242,5.148174,6.601593,-1.259620,-3.033497,1.444739,-5.773586,-2.518370,-7.875331,2.428075,6.960940,-7.469613,3.742037,-7.694851,0.955094,3.721931,-1.631677,-0.974506,-5.878972,2.204779,3.604851,-0.770850,3.733513,-4.302244,-6.577405,-9.327574,-4.750702,1.705690,8.665069,-5.391819,1.067994,6.166252,-2.036497,5.169394,4.839554,-2.437777,4.430517,-5.157920,3.090413,-6.152421,-1.151880,5.114902,1.657291,-6.770403,7.191522,9.095592,-3.024836,-2.074618,2.163776,-7.944301,-5.836512,6.883159,2.411143,3.000429,-2.071797,-2.305178,-9.547449,6.349513,-9.791854,-9.193794,-0.393382,-4.175071,-2.130067,-5.215885,-6.140810,-6.194002,9.025914,2.576605,5.378621,3.454219,-9.130193,-8.926067,9.843691,0.377494,-3.505239,0.230172,4.583574,5.872143,-2.241293,1.747333,-6.439621,-8.726012,4.062256,5.866792,-1.101153,7.793831,-7.125035,0.674612,8.937102,-6.275995,-8.449860,1.048447,5.189650,6.783227,-1.548474,1.694111,3.991466,-4.074146,2.411165,8.755446,-9.776603,-0.534616,0.926272,-3.745706,-3.274134,-1.557554,3.301665,4.488095,-7.800509,-8.708185,7.329615,-4.867018,0.660449,-4.899934,-6.930911,-7.806696,-4.553989,9.802855,-3.201359,-6.926128,-6.709147,1.932203,-9.350633,5.781727,-2.633548,9.935477,1.530316,-7.879186,-8.278990,3.448358,-2.022118,8.053457,-8.533754,-5.861172,8.574207,-2.410285,0.856551,0.636046,-5.703758,4.699127,-7.464662,-3.089692,-9.418547,0.098082,2.698914,2.916182,-4.352372,-8.321758,0.025512,-6.615491,-1.082491,2.567342,-1.774541,2.025307,0.257064,8.135157,-3.330291,4.499939,-9.213885,2.176704,1.599715,-8.426314,-0.908652,-4.710608,8.709993,-4.998938,1.276611,-6.338890,-2.335346,-3.087883,-7.613042,9.669750,-4.688859,1.114601,1.581432,-2.271201,3.557551,2.706825,-8.645258,9.363602,-0.814195,3.066771,1.138979,9.062628,2.455886,3.775364,-8.721157,-9.178065,8.226209,3.334971,1.386130,2.152841,-1.396543,-1.800902,7.814641,5.295753,5.815622,0.053209,-1.332352,-1.261012,3.066683,5.859404,-2.818052,-7.278755,3.774880,0.427427,1.973262,0.516846,6.609938,-1.666579,8.163918,-2.563946,-4.459047,-2.644192,-9.534630,8.998267,-6.114379,1.937960,-3.825201,9.693422,-7.121966,-5.600565,0.770926,4.026719,6.131183,5.829523,4.987285,7.826061,-5.540184,-4.018796,-4.225743,-6.032514,-5.061904,-0.069588,3.603531,-6.410460,-7.361187,4.708919,-5.024058,-1.823211,9.636723,7.553886,4.157736,-2.981023,-3.755944,-1.440783,-6.420550,5.576570,9.401184,-3.807076,1.567506,-0.513662,6.886805,-8.140349,-2.573773,-9.543387,-5.146615,6.709142,-6.054029,2.841880,-6.255699,-4.613118,-0.634729,-2.689958,0.420213,-3.750780,7.177723,-8.489355,7.826118,4.066375,6.084648,6.530659,9.876193,0.422673,-0.781192,-4.739928,-8.774483,-0.787148,-4.684805,-7.291820,4.416582,5.040248,6.866650,6.194062,-1.714941,6.399992,-4.405721,4.242723,6.476547,-5.472914,-5.409882,-6.107967,0.082686,6.424577,5.932096,2.682869,4.517758,-6.785970,-5.876337,1.560816,-2.753607,-6.057637,8.523139,-0.269132,-4.208719,-3.575049,5.913819,8.818792,6.213616,-6.166373,3.588792,6.553047,-4.473159,8.053143,-9.094187,8.931156,2.300419,7.458030,-2.144845,1.037172,-2.488646,2.828908,1.511226,-7.208614,4.184866,0.386756,-4.289719,6.149822,-9.122988,2.222255,6.560329,4.205850,-7.747506,1.039963,-7.124908,0.308851,9.784351,-8.877658,-6.678075,3.352582,-4.136283,-8.334853,-7.017408,2.353161,-7.651171,9.006874,-1.851182,2.839274,4.716696,6.067098,5.423840,2.524309,8.962064,1.194890,-7.149667,4.704128,-3.305001,-7.239483,-8.247017,7.902378,-8.843321,-3.211324,-3.949601,-2.036633,9.314781,5.363695,-8.028507,5.443576,4.793945,5.161625,4.093168,-9.278316,-7.099257,-9.107816,-3.068768,-8.242900,-2.639775,2.400173,-9.319092,3.117122,6.262726,-6.099869,9.882268,8.614752,4.153813,-9.958076,-6.863209,-8.392530,9.089738,3.480130,-1.671302,6.893264,-2.173777,6.872929,-9.078774,-6.567209,-1.982867,5.437636,-9.454286,-0.708179,-4.069871,4.810790,3.959739,7.285111,-2.830978,-9.559871,-2.706963,-1.362982,9.918361,8.960129,-4.986613,9.375131,0.001962,-1.516014,-5.367822,0.245417,0.012805,2.535565,-6.595380,-5.499192,9.626135,4.673520,-5.635051,-7.000053,-1.573294,3.289428,-1.645830,8.284593,8.037711,4.676117,-8.494736,-5.689911,3.726133,-1.401812,6.311695,9.305820,7.913783,-8.057040,-8.223925,6.248092,4.474043,4.019802,-8.776128,8.666248,-0.696857,9.424668,4.225152,-3.872027,8.848692,-2.202699,2.576023,9.589334,-1.988235,-6.188800,-9.749055,4.520982,-3.065783,3.216170,8.359331,3.053021,-1.250649,-2.176468,-6.203977,-2.328812,5.749375,-9.505711,-9.503165,-6.499724,-9.643829,1.170376,-7.656447,-2.988561,6.245467,5.801346,-2.006096,-7.997731,2.872122,-7.439578,-9.738020,6.804478,1.429320,-9.316974,1.776466,-4.686459,-3.278001,6.247243,6.266344,2.289032,1.645782,0.622834,2.730242,-5.367211,4.066886,2.893002,-9.006789,3.161481,-9.882036,1.779465,-9.835043,0.984114,-1.939108,-0.170289,-6.040286,-6.068930,-6.040186,1.239233,-5.708909,2.044392,-5.980731,4.676140,0.768077,-7.541242,-7.098282,-9.342277,-0.369103,7.063850,-9.542503,-1.130524,-9.973791], dtype = "float64")#candidate|3869|(2304,)|const|float64
bop_3870 = relay.floor_mod(call_3863.astype('float64'), relay.reshape(const_3869.astype('float64'), relay.shape_of(call_3863))) # shape=(2304,)
bop_3873 = relay.floor_mod(call_3866.astype('float64'), relay.reshape(const_3869.astype('float64'), relay.shape_of(call_3866))) # shape=(2304,)
output = relay.Tuple([call_3839,const_3864,const_3865,bop_3870,])
output2 = relay.Tuple([call_3840,const_3864,const_3865,bop_3873,])
func_3881 = relay.Function([], output)
mod['func_3881'] = func_3881
mod = relay.transform.InferType()(mod)
mutated_mod['func_3881'] = func_3881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3881_call = mutated_mod.get_global_var('func_3881')
call_3882 = func_3881_call()
output = call_3882
func_3883 = relay.Function([], output)
mutated_mod['func_3883'] = func_3883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1798_call = mod.get_global_var('func_1798')
func_1800_call = mutated_mod.get_global_var('func_1800')
call_3889 = relay.TupleGetItem(func_1798_call(), 1)
call_3890 = relay.TupleGetItem(func_1800_call(), 1)
func_1588_call = mod.get_global_var('func_1588')
func_1589_call = mutated_mod.get_global_var('func_1589')
call_3891 = relay.TupleGetItem(func_1588_call(), 1)
call_3892 = relay.TupleGetItem(func_1589_call(), 1)
output = relay.Tuple([call_3889,call_3891,])
output2 = relay.Tuple([call_3890,call_3892,])
func_3893 = relay.Function([], output)
mod['func_3893'] = func_3893
mod = relay.transform.InferType()(mod)
mutated_mod['func_3893'] = func_3893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3893_call = mutated_mod.get_global_var('func_3893')
call_3894 = func_3893_call()
output = call_3894
func_3895 = relay.Function([], output)
mutated_mod['func_3895'] = func_3895
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3904 = relay.var("var_3904", dtype = "float64", shape = (15, 8, 1))#candidate|3904|(15, 8, 1)|var|float64
uop_3905 = relay.atanh(var_3904.astype('float64')) # shape=(15, 8, 1)
uop_3907 = relay.erf(uop_3905.astype('float32')) # shape=(15, 8, 1)
func_3893_call = mod.get_global_var('func_3893')
func_3895_call = mutated_mod.get_global_var('func_3895')
call_3910 = relay.TupleGetItem(func_3893_call(), 0)
call_3911 = relay.TupleGetItem(func_3895_call(), 0)
bop_3915 = relay.bitwise_or(uop_3907.astype('int8'), relay.reshape(uop_3905.astype('int8'), relay.shape_of(uop_3907))) # shape=(15, 8, 1)
func_1588_call = mod.get_global_var('func_1588')
func_1589_call = mutated_mod.get_global_var('func_1589')
call_3920 = relay.TupleGetItem(func_1588_call(), 1)
call_3921 = relay.TupleGetItem(func_1589_call(), 1)
func_3881_call = mod.get_global_var('func_3881')
func_3883_call = mutated_mod.get_global_var('func_3883')
call_3932 = relay.TupleGetItem(func_3881_call(), 0)
call_3933 = relay.TupleGetItem(func_3883_call(), 0)
uop_3935 = relay.exp(uop_3905.astype('float64')) # shape=(15, 8, 1)
output = relay.Tuple([call_3910,bop_3915,call_3920,call_3932,uop_3935,])
output2 = relay.Tuple([call_3911,bop_3915,call_3921,call_3933,uop_3935,])
func_3938 = relay.Function([var_3904,], output)
mod['func_3938'] = func_3938
mod = relay.transform.InferType()(mod)
mutated_mod['func_3938'] = func_3938
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3939 = relay.var("var_3939", dtype = "float64", shape = (15, 8, 1))#candidate|3939|(15, 8, 1)|var|float64
func_3938_call = mutated_mod.get_global_var('func_3938')
call_3940 = func_3938_call(var_3939)
output = call_3940
func_3941 = relay.Function([var_3939], output)
mutated_mod['func_3941'] = func_3941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2578_call = mod.get_global_var('func_2578')
func_2580_call = mutated_mod.get_global_var('func_2580')
call_3949 = func_2578_call()
call_3950 = func_2578_call()
const_3952 = relay.const([[[5.204817,-8.603591,-9.782363,-4.224024],[-3.757293,-4.397552,-1.228251,-6.394361],[-4.989561,3.759065,-2.808335,3.587343],[-5.631811,-6.805321,-1.826081,1.221810],[-6.487301,6.057807,0.952633,-5.904610],[-1.201506,-0.117624,5.282576,0.196406],[1.099025,0.948677,8.831879,-9.721669],[-4.512778,-5.014990,-5.976704,-4.065518],[8.413418,9.327479,5.779001,2.786497],[-2.719470,-8.939515,-1.244035,0.987494],[-5.756602,4.647731,8.504242,-5.331367],[-7.400441,-1.116392,-4.126200,6.858265]],[[-4.072348,-1.852840,-6.730702,1.297206],[9.879731,-5.638680,3.838421,-5.114124],[7.555959,8.651812,8.292634,-1.465919],[2.093667,-1.804428,6.054484,2.983554],[-4.982883,-9.329776,2.508240,0.444031],[2.849358,-4.119650,8.996556,1.273270],[-1.010254,-7.700042,-0.840953,6.948773],[7.465845,5.647548,6.240802,9.035416],[7.820863,-1.594921,1.140513,7.244111],[-0.210511,-8.117656,-5.914102,-6.415497],[-6.544655,-9.792164,0.857104,-2.672069],[3.576303,8.619204,7.111477,-1.170234]],[[-6.267621,2.145015,-5.101780,9.586244],[4.977714,5.002009,7.770858,-8.380136],[-1.515976,-5.204008,9.437832,-1.089738],[-9.075455,5.452576,-8.844077,-7.347260],[4.361522,4.388918,6.533280,-4.764490],[-8.287857,-0.034698,4.799097,0.455086],[-6.433658,2.392052,2.066443,-8.456496],[5.172394,5.113370,-0.401230,4.511560],[1.644360,4.199521,8.253661,2.035764],[2.801545,1.840454,5.721539,-6.119680],[-4.859684,3.634944,-8.627213,3.918795],[1.260784,3.924869,6.386759,5.301266]],[[9.158370,2.295278,-5.511402,-1.878280],[-1.997425,-6.153270,5.683822,5.510361],[-0.838664,0.052048,1.227205,0.022076],[0.023750,-3.004982,8.278157,5.826773],[-3.748224,5.981191,-7.153599,5.905804],[1.820791,-8.741048,-7.419292,-1.569260],[-7.302005,4.372528,-1.714840,-9.603393],[-8.449695,-7.049279,8.662074,-9.279822],[-0.487775,-3.316715,-1.967337,-6.325782],[-8.989392,-2.059296,-6.099862,6.617794],[-5.615485,-3.159109,0.988687,-2.573880],[2.685152,3.578843,-6.355809,9.924448]],[[5.760936,3.587043,6.667563,0.315944],[-0.917378,-9.055911,-6.112935,4.415230],[4.032230,-7.950454,0.812188,-0.661178],[1.361286,0.070907,5.897895,2.420711],[-1.602307,-1.194068,-6.858096,9.511940],[9.561809,8.700877,-4.582986,-3.540098],[1.663195,-9.539347,0.730332,0.146240],[0.846204,2.792853,7.143651,5.686030],[1.802393,3.077698,-5.898072,2.164482],[9.939302,3.674355,0.369088,7.354481],[-6.903196,0.054162,-0.244595,1.152830],[8.108168,-3.986542,3.013817,6.891297]],[[-0.965448,-5.070183,5.958711,-3.596169],[-5.112818,-1.908698,-5.633438,-8.061205],[-9.108850,-7.269003,6.142823,-6.634080],[-0.251078,3.908427,-5.583007,5.490427],[-7.353027,5.040143,7.372745,-0.402754],[-0.305042,7.118111,-7.579028,1.570192],[-6.870352,9.354509,9.264335,-5.830267],[-3.438974,1.302786,-8.839263,4.640735],[-3.039504,7.725432,0.579782,-2.910115],[-2.940956,-5.589939,1.690313,3.349205],[7.985246,5.066021,-7.280683,5.144365],[-8.724616,-8.768568,5.486574,7.365412]],[[-1.889105,7.250463,-3.812117,6.392599],[1.728496,4.383941,-7.035619,-8.029754],[9.856142,-8.951647,-1.911321,-1.382851],[4.958242,7.923258,9.506681,-9.343054],[0.866461,7.846442,4.505240,2.292562],[-0.167490,-3.429973,1.849327,-7.351963],[-0.246172,0.448778,-7.965896,8.422204],[-3.167481,-4.510517,0.956482,8.796207],[-3.103999,-4.694267,-6.040345,6.581200],[-5.670922,6.645139,-6.244323,-1.780082],[-9.683706,8.411707,-3.596432,-5.096614],[-9.342380,-3.084857,-8.014860,-5.817224]],[[-0.316692,-8.783296,-0.752108,9.916520],[1.860433,5.936060,-2.249381,1.519670],[5.974267,-8.515292,9.375727,-0.257760],[1.500474,-2.557242,-6.227415,1.659993],[1.491214,6.124595,4.141169,2.671484],[4.288652,-9.684740,-9.741680,8.035321],[7.228600,4.890281,-9.162576,-3.433922],[-7.845944,1.306703,9.465854,3.809500],[6.506948,6.706271,2.114302,2.571051],[8.164848,3.395160,8.231835,3.461416],[-5.642368,-9.666485,-9.754375,-0.526927],[5.818365,5.764210,-8.898716,0.587253]],[[-5.190099,-1.781356,6.251666,-2.136577],[-2.026751,8.486413,-5.441564,-9.213796],[0.822104,-9.135466,9.484167,0.929652],[-4.224946,1.280106,6.946365,-7.927548],[3.900959,-1.245949,0.089550,7.407379],[-3.930547,7.853958,6.241673,6.600196],[-7.158734,-9.085791,-7.579757,-0.515325],[0.902771,-6.275221,6.960034,-1.216298],[5.772294,9.686730,2.428919,-7.184405],[8.385998,2.628341,3.218580,-8.128290],[-0.332097,5.785573,-0.604004,2.346328],[-5.554709,-6.731377,9.567154,-3.572810]],[[1.715929,7.131838,8.330440,-3.712423],[6.814065,8.010761,-1.864166,1.378466],[1.832455,-3.051118,-7.284126,9.102406],[6.273641,-0.591487,-1.381713,9.430587],[1.608327,-3.343809,3.859513,1.986746],[-6.748335,9.040705,-4.252939,8.609451],[-8.657109,2.699105,-2.786420,6.935001],[0.576035,-5.203464,-2.677933,6.833939],[-4.345838,-0.859237,8.329190,-2.102573],[2.195524,-9.481829,-2.460395,4.055988],[9.186817,-7.047473,6.063841,4.942964],[3.022693,-0.217436,-5.483533,9.795473]],[[8.439531,-2.346476,-7.524811,3.716299],[-8.776670,1.896170,7.351198,1.102643],[-2.437567,-0.568587,8.323846,-6.099314],[2.445194,6.620968,-6.676638,-3.568749],[-6.762048,-0.521846,-6.289712,-2.553648],[-4.277696,8.319894,-7.038914,-8.221100],[-0.583915,-6.622018,0.503995,0.174465],[1.083062,-3.377078,7.847459,-3.157156],[1.392226,-4.233784,-1.642332,-2.298270],[4.674506,-8.191188,5.697344,-6.613305],[-7.771875,2.844089,9.281281,-4.477921],[3.722403,-8.082845,-1.387851,2.922961]],[[-1.286347,1.107478,-3.121683,3.940197],[2.087359,-9.499087,-1.858000,9.692060],[1.325540,-7.728647,9.250440,-0.382903],[5.844275,7.688144,8.675226,7.889542],[0.184556,-3.804734,0.575414,4.813433],[2.008215,4.335692,-6.603160,-6.036397],[5.298587,-7.644629,-7.886903,-9.446485],[6.240313,6.776724,-2.414823,-7.126122],[7.470586,7.498710,-6.380929,1.285850],[-8.417495,-5.177469,2.741921,4.529464],[3.452041,9.776996,-6.048778,-6.156078],[-3.308661,-9.495647,-6.830765,-0.589998]],[[7.630735,-4.770381,-5.825023,6.647225],[-7.171069,0.011659,8.615453,3.612379],[-2.498042,-1.340020,-5.567927,-3.243650],[-1.981229,9.798644,-8.665479,-3.855774],[4.712258,4.323664,-1.285294,7.346626],[-2.289357,0.923705,0.677295,4.949613],[0.615549,-9.745902,-0.220625,-4.789054],[4.940358,5.891947,6.146344,5.694711],[5.311081,-5.850983,9.896684,-6.775544],[-0.614782,5.003506,-2.331170,3.499044],[-2.721121,8.086535,7.555370,9.339266],[8.243051,-7.549839,-0.081671,-5.403671]],[[-5.619475,-1.189841,-3.805527,-4.494756],[-9.864384,-4.722830,-5.581718,-6.505704],[9.242865,1.952958,-8.291852,4.340742],[2.423538,-8.193974,7.090924,7.922540],[-5.264006,2.757041,9.253164,1.887460],[-4.431626,-0.142778,-7.164460,6.009273],[8.608585,-0.807208,-0.298640,5.667300],[4.738495,8.461861,-7.632062,-6.589008],[-4.551872,5.209355,0.277461,5.813780],[-3.181922,-2.030275,6.241363,-0.783972],[-9.729675,-9.186546,-5.881116,7.514066],[8.659117,-0.916046,7.013350,-0.261636]],[[2.447515,0.305946,3.732857,-5.852976],[1.366866,-4.676520,-3.243191,9.550148],[9.951321,9.564484,8.527809,3.530597],[-5.916361,3.845483,-2.648748,9.062043],[1.815770,4.995844,-0.424705,1.943369],[-4.673369,-6.342699,-0.863706,-4.651640],[0.947963,-3.535700,-2.932772,0.265847],[3.776606,-5.757820,1.652563,6.522915],[8.584089,4.123536,-5.356734,7.771159],[-5.739661,-8.917292,8.087846,-3.439641],[-7.209071,2.955689,-8.195872,3.029189],[7.879032,8.594742,-1.614381,-2.306832]],[[8.689017,7.039741,-9.972928,9.430729],[-9.646782,3.455261,-9.156329,-6.715403],[-3.644124,1.140857,-3.157635,3.833298],[-1.471486,-6.079505,5.266392,-4.516032],[-5.653773,2.677779,-9.656157,8.318853],[-0.464895,-6.681964,-9.803495,7.523011],[1.019532,3.986886,-3.871303,0.317001],[-3.043830,9.682585,-5.150993,-7.984140],[9.312448,3.892406,-8.469264,-6.300784],[-2.594674,7.408410,9.917709,1.436373],[9.181964,-5.143366,9.935084,7.361598],[-4.260529,-8.685888,-4.352246,9.946558]]], dtype = "float64")#candidate|3952|(16, 12, 4)|const|float64
bop_3953 = relay.greater(call_3949.astype('bool'), const_3952.astype('bool')) # shape=(16, 12, 4)
bop_3956 = relay.greater(call_3950.astype('bool'), const_3952.astype('bool')) # shape=(16, 12, 4)
bop_3969 = relay.bitwise_and(const_3952.astype('uint16'), relay.reshape(bop_3953.astype('uint16'), relay.shape_of(const_3952))) # shape=(16, 12, 4)
bop_3972 = relay.bitwise_and(const_3952.astype('uint16'), relay.reshape(bop_3956.astype('uint16'), relay.shape_of(const_3952))) # shape=(16, 12, 4)
bop_3980 = relay.add(bop_3969.astype('int8'), relay.reshape(bop_3953.astype('int8'), relay.shape_of(bop_3969))) # shape=(16, 12, 4)
bop_3983 = relay.add(bop_3972.astype('int8'), relay.reshape(bop_3956.astype('int8'), relay.shape_of(bop_3972))) # shape=(16, 12, 4)
output = relay.Tuple([bop_3980,])
output2 = relay.Tuple([bop_3983,])
func_3987 = relay.Function([], output)
mod['func_3987'] = func_3987
mod = relay.transform.InferType()(mod)
mutated_mod['func_3987'] = func_3987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3987_call = mutated_mod.get_global_var('func_3987')
call_3988 = func_3987_call()
output = call_3988
func_3989 = relay.Function([], output)
mutated_mod['func_3989'] = func_3989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3084_call = mod.get_global_var('func_3084')
func_3086_call = mutated_mod.get_global_var('func_3086')
call_4049 = relay.TupleGetItem(func_3084_call(), 0)
call_4050 = relay.TupleGetItem(func_3086_call(), 0)
output = relay.Tuple([call_4049,])
output2 = relay.Tuple([call_4050,])
func_4059 = relay.Function([], output)
mod['func_4059'] = func_4059
mod = relay.transform.InferType()(mod)
mutated_mod['func_4059'] = func_4059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4059_call = mutated_mod.get_global_var('func_4059')
call_4060 = func_4059_call()
output = call_4060
func_4061 = relay.Function([], output)
mutated_mod['func_4061'] = func_4061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_931_call = mod.get_global_var('func_931')
func_932_call = mutated_mod.get_global_var('func_932')
call_4114 = relay.TupleGetItem(func_931_call(), 1)
call_4115 = relay.TupleGetItem(func_932_call(), 1)
func_1122_call = mod.get_global_var('func_1122')
func_1123_call = mutated_mod.get_global_var('func_1123')
call_4116 = relay.TupleGetItem(func_1122_call(), 0)
call_4117 = relay.TupleGetItem(func_1123_call(), 0)
uop_4119 = relay.sigmoid(call_4116.astype('float32')) # shape=(16, 12, 1)
uop_4121 = relay.sigmoid(call_4117.astype('float32')) # shape=(16, 12, 1)
output = relay.Tuple([call_4114,uop_4119,])
output2 = relay.Tuple([call_4115,uop_4121,])
func_4129 = relay.Function([], output)
mod['func_4129'] = func_4129
mod = relay.transform.InferType()(mod)
output = func_4129()
func_4130 = relay.Function([], output)
mutated_mod['func_4130'] = func_4130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1691_call = mod.get_global_var('func_1691')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_4155 = relay.TupleGetItem(func_1691_call(), 0)
call_4156 = relay.TupleGetItem(func_1692_call(), 0)
func_1122_call = mod.get_global_var('func_1122')
func_1123_call = mutated_mod.get_global_var('func_1123')
call_4177 = relay.TupleGetItem(func_1122_call(), 0)
call_4178 = relay.TupleGetItem(func_1123_call(), 0)
bop_4180 = relay.bitwise_xor(call_4155.astype('uint32'), relay.reshape(call_4177.astype('uint32'), relay.shape_of(call_4155))) # shape=(16, 12, 1)
bop_4183 = relay.bitwise_xor(call_4156.astype('uint32'), relay.reshape(call_4178.astype('uint32'), relay.shape_of(call_4156))) # shape=(16, 12, 1)
output = bop_4180
output2 = bop_4183
func_4185 = relay.Function([], output)
mod['func_4185'] = func_4185
mod = relay.transform.InferType()(mod)
output = func_4185()
func_4186 = relay.Function([], output)
mutated_mod['func_4186'] = func_4186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1588_call = mod.get_global_var('func_1588')
func_1589_call = mutated_mod.get_global_var('func_1589')
call_4270 = relay.TupleGetItem(func_1588_call(), 0)
call_4271 = relay.TupleGetItem(func_1589_call(), 0)
func_2045_call = mod.get_global_var('func_2045')
func_2049_call = mutated_mod.get_global_var('func_2049')
var_4278 = relay.var("var_4278", dtype = "int8", shape = (63,))#candidate|4278|(63,)|var|int8
call_4277 = func_2045_call(relay.reshape(var_4278.astype('int8'), [3, 7, 3]), relay.reshape(var_4278.astype('int8'), [3, 7, 3]), )
call_4279 = func_2045_call(relay.reshape(var_4278.astype('int8'), [3, 7, 3]), relay.reshape(var_4278.astype('int8'), [3, 7, 3]), )
func_3671_call = mod.get_global_var('func_3671')
func_3673_call = mutated_mod.get_global_var('func_3673')
call_4280 = relay.TupleGetItem(func_3671_call(relay.reshape(call_4270.astype('float64'), [4, 5, 3])), 1)
call_4281 = relay.TupleGetItem(func_3673_call(relay.reshape(call_4270.astype('float64'), [4, 5, 3])), 1)
output = relay.Tuple([call_4270,call_4277,var_4278,call_4280,])
output2 = relay.Tuple([call_4271,call_4279,var_4278,call_4281,])
func_4284 = relay.Function([var_4278,], output)
mod['func_4284'] = func_4284
mod = relay.transform.InferType()(mod)
mutated_mod['func_4284'] = func_4284
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4285 = relay.var("var_4285", dtype = "int8", shape = (63,))#candidate|4285|(63,)|var|int8
func_4284_call = mutated_mod.get_global_var('func_4284')
call_4286 = func_4284_call(var_4285)
output = call_4286
func_4287 = relay.Function([var_4285], output)
mutated_mod['func_4287'] = func_4287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1741_call = mod.get_global_var('func_1741')
func_1742_call = mutated_mod.get_global_var('func_1742')
call_4304 = relay.TupleGetItem(func_1741_call(), 0)
call_4305 = relay.TupleGetItem(func_1742_call(), 0)
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_4306 = func_1666_call()
call_4307 = func_1666_call()
func_3987_call = mod.get_global_var('func_3987')
func_3989_call = mutated_mod.get_global_var('func_3989')
call_4308 = relay.TupleGetItem(func_3987_call(), 0)
call_4309 = relay.TupleGetItem(func_3989_call(), 0)
output = relay.Tuple([call_4304,call_4306,call_4308,])
output2 = relay.Tuple([call_4305,call_4307,call_4309,])
func_4313 = relay.Function([], output)
mod['func_4313'] = func_4313
mod = relay.transform.InferType()(mod)
output = func_4313()
func_4314 = relay.Function([], output)
mutated_mod['func_4314'] = func_4314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1588_call = mod.get_global_var('func_1588')
func_1589_call = mutated_mod.get_global_var('func_1589')
call_4361 = relay.TupleGetItem(func_1588_call(), 0)
call_4362 = relay.TupleGetItem(func_1589_call(), 0)
output = call_4361
output2 = call_4362
func_4381 = relay.Function([], output)
mod['func_4381'] = func_4381
mod = relay.transform.InferType()(mod)
output = func_4381()
func_4382 = relay.Function([], output)
mutated_mod['func_4382'] = func_4382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_4404 = func_1666_call()
call_4405 = func_1666_call()
output = relay.Tuple([call_4404,])
output2 = relay.Tuple([call_4405,])
func_4417 = relay.Function([], output)
mod['func_4417'] = func_4417
mod = relay.transform.InferType()(mod)
mutated_mod['func_4417'] = func_4417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4417_call = mutated_mod.get_global_var('func_4417')
call_4418 = func_4417_call()
output = call_4418
func_4419 = relay.Function([], output)
mutated_mod['func_4419'] = func_4419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2951_call = mod.get_global_var('func_2951')
func_2953_call = mutated_mod.get_global_var('func_2953')
call_4439 = relay.TupleGetItem(func_2951_call(), 0)
call_4440 = relay.TupleGetItem(func_2953_call(), 0)
uop_4442 = relay.log10(call_4439.astype('float64')) # shape=(2, 11, 6)
uop_4444 = relay.log10(call_4440.astype('float64')) # shape=(2, 11, 6)
output = uop_4442
output2 = uop_4444
func_4446 = relay.Function([], output)
mod['func_4446'] = func_4446
mod = relay.transform.InferType()(mod)
output = func_4446()
func_4447 = relay.Function([], output)
mutated_mod['func_4447'] = func_4447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3160_call = mod.get_global_var('func_3160')
func_3161_call = mutated_mod.get_global_var('func_3161')
call_4458 = func_3160_call()
call_4459 = func_3160_call()
func_3047_call = mod.get_global_var('func_3047')
func_3049_call = mutated_mod.get_global_var('func_3049')
const_4477 = relay.const([2.495145,7.755787,2.357396,-3.084472,-2.318488,-0.778543,2.082614,8.262697,-5.074023,-6.532711,2.324868,-8.350909,5.274091,-8.407837,-1.671457,2.832266,9.676786,0.280022,8.416483,-5.851679,-8.175962,-5.036534,-5.848476,-7.733233,8.715617,-5.325852,-5.434788,-1.079658,-0.323343,-8.757626,-0.900936,-6.384043,3.277949,-0.704421,0.208833,-9.893724,-4.747705,8.015969,-2.022409,4.385266,-8.914231,0.424591,-1.644936,7.641742,-0.054532,-0.387334,7.267972,-3.528953,-6.021650,7.328325,-6.721551,-2.501532,-2.705713,0.895318,9.215284,-3.078321,-6.883317,-6.442710,1.329654,1.302485,-2.450637,7.798549,-5.030356,-7.253734,-8.178643,-6.322333,1.487242,0.340041,-9.674273,6.258733,-8.768760,-6.876295,6.920453,0.615654,-9.960894,-9.361538,-2.188570,-9.372603,-9.401805,-7.956469,4.431376,7.103886,5.645141,-6.254669,8.388625,1.792546,-3.302407,0.540098,4.405959,-8.548790,2.359074,-8.733530,-2.468716,0.137274,0.523618,-2.957279,-1.396598,4.771697,-4.944612,-6.168162,9.313186,1.135139,3.783909,5.504872,-7.753041,-0.088166,9.784395,2.143896,1.544757,-5.283597,-3.448868,9.427986,-7.989762,-1.910313,4.865256,-9.152539,9.489145,-0.525474,-0.974178,4.321625,6.075100,5.486264,-5.851173,1.307840,0.299381,-4.816465,-0.706745,-0.831934,-7.215480,4.731830,7.226254,4.207836,-1.443593,0.749598,2.216326,8.525402,-8.991031,4.404965,4.039763,9.694230,-2.785950,7.192722,7.525020,4.612924,-0.289145,7.825946,0.608045,-2.465649,-4.167500,-3.476097,-9.457803,8.464829,-0.441075,2.077390,9.308776,-4.432898,-7.754072,-0.083344,-1.302691,-7.710600,-9.075309,-2.443246,-5.957674,7.847329,3.748334,-5.839219,2.126313,-7.281311,8.480873,-1.013934,-1.650786,-9.863617,-8.049109,5.473554,5.130529,4.985844,2.249442,4.618158,2.592398,4.178625], dtype = "float64")#candidate|4477|(180,)|const|float64
call_4476 = relay.TupleGetItem(func_3047_call(relay.reshape(const_4477.astype('float64'), [2, 6, 15])), 0)
call_4478 = relay.TupleGetItem(func_3049_call(relay.reshape(const_4477.astype('float64'), [2, 6, 15])), 0)
bop_4493 = relay.logical_or(call_4476.astype('bool'), relay.reshape(const_4477.astype('bool'), relay.shape_of(call_4476))) # shape=(2, 6, 15)
bop_4496 = relay.logical_or(call_4478.astype('bool'), relay.reshape(const_4477.astype('bool'), relay.shape_of(call_4478))) # shape=(2, 6, 15)
bop_4499 = relay.minimum(bop_4493.astype('uint8'), relay.reshape(call_4476.astype('uint8'), relay.shape_of(bop_4493))) # shape=(2, 6, 15)
bop_4502 = relay.minimum(bop_4496.astype('uint8'), relay.reshape(call_4478.astype('uint8'), relay.shape_of(bop_4496))) # shape=(2, 6, 15)
output = relay.Tuple([call_4458,bop_4499,])
output2 = relay.Tuple([call_4459,bop_4502,])
func_4514 = relay.Function([], output)
mod['func_4514'] = func_4514
mod = relay.transform.InferType()(mod)
mutated_mod['func_4514'] = func_4514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4514_call = mutated_mod.get_global_var('func_4514')
call_4515 = func_4514_call()
output = call_4515
func_4516 = relay.Function([], output)
mutated_mod['func_4516'] = func_4516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3781_call = mod.get_global_var('func_3781')
func_3782_call = mutated_mod.get_global_var('func_3782')
call_4517 = func_3781_call()
call_4518 = func_3781_call()
func_452_call = mod.get_global_var('func_452')
func_454_call = mutated_mod.get_global_var('func_454')
call_4521 = func_452_call()
call_4522 = func_452_call()
func_1519_call = mod.get_global_var('func_1519')
func_1521_call = mutated_mod.get_global_var('func_1521')
call_4523 = relay.TupleGetItem(func_1519_call(), 0)
call_4524 = relay.TupleGetItem(func_1521_call(), 0)
bop_4527 = relay.subtract(call_4523.astype('uint8'), relay.reshape(call_4521.astype('uint8'), relay.shape_of(call_4523))) # shape=(4, 5, 3)
bop_4530 = relay.subtract(call_4524.astype('uint8'), relay.reshape(call_4522.astype('uint8'), relay.shape_of(call_4524))) # shape=(4, 5, 3)
uop_4537 = relay.rsqrt(call_4523.astype('float32')) # shape=(4, 5, 3)
uop_4539 = relay.rsqrt(call_4524.astype('float32')) # shape=(4, 5, 3)
output = relay.Tuple([call_4517,bop_4527,uop_4537,])
output2 = relay.Tuple([call_4518,bop_4530,uop_4539,])
func_4540 = relay.Function([], output)
mod['func_4540'] = func_4540
mod = relay.transform.InferType()(mod)
mutated_mod['func_4540'] = func_4540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4540_call = mutated_mod.get_global_var('func_4540')
call_4541 = func_4540_call()
output = call_4541
func_4542 = relay.Function([], output)
mutated_mod['func_4542'] = func_4542
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4607 = relay.var("var_4607", dtype = "float64", shape = (13, 12, 13))#candidate|4607|(13, 12, 13)|var|float64
var_4608 = relay.var("var_4608", dtype = "float64", shape = (13, 12, 13))#candidate|4608|(13, 12, 13)|var|float64
bop_4609 = relay.maximum(var_4607.astype('float64'), relay.reshape(var_4608.astype('float64'), relay.shape_of(var_4607))) # shape=(13, 12, 13)
bop_4621 = relay.greater(bop_4609.astype('bool'), relay.reshape(var_4607.astype('bool'), relay.shape_of(bop_4609))) # shape=(13, 12, 13)
bop_4630 = relay.logical_or(var_4608.astype('bool'), relay.reshape(var_4607.astype('bool'), relay.shape_of(var_4608))) # shape=(13, 12, 13)
output = relay.Tuple([bop_4621,bop_4630,])
output2 = relay.Tuple([bop_4621,bop_4630,])
func_4648 = relay.Function([var_4607,var_4608,], output)
mod['func_4648'] = func_4648
mod = relay.transform.InferType()(mod)
mutated_mod['func_4648'] = func_4648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4648_call = mutated_mod.get_global_var('func_4648')
var_4650 = relay.var("var_4650", dtype = "float64", shape = (13, 12, 13))#candidate|4650|(13, 12, 13)|var|float64
var_4651 = relay.var("var_4651", dtype = "float64", shape = (13, 12, 13))#candidate|4651|(13, 12, 13)|var|float64
call_4649 = func_4648_call(var_4650,var_4651,)
output = call_4649
func_4652 = relay.Function([var_4650,var_4651,], output)
mutated_mod['func_4652'] = func_4652
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4696 = relay.var("var_4696", dtype = "float64", shape = (9, 16, 7))#candidate|4696|(9, 16, 7)|var|float64
uop_4697 = relay.exp(var_4696.astype('float64')) # shape=(9, 16, 7)
uop_4699 = relay.sqrt(uop_4697.astype('float64')) # shape=(9, 16, 7)
func_2785_call = mod.get_global_var('func_2785')
func_2788_call = mutated_mod.get_global_var('func_2788')
var_4713 = relay.var("var_4713", dtype = "float64", shape = (60,))#candidate|4713|(60,)|var|float64
call_4712 = relay.TupleGetItem(func_2785_call(relay.reshape(var_4713.astype('float64'), [4, 5, 3])), 4)
call_4714 = relay.TupleGetItem(func_2788_call(relay.reshape(var_4713.astype('float64'), [4, 5, 3])), 4)
output = relay.Tuple([uop_4699,call_4712,var_4713,])
output2 = relay.Tuple([uop_4699,call_4714,var_4713,])
func_4719 = relay.Function([var_4696,var_4713,], output)
mod['func_4719'] = func_4719
mod = relay.transform.InferType()(mod)
var_4720 = relay.var("var_4720", dtype = "float64", shape = (9, 16, 7))#candidate|4720|(9, 16, 7)|var|float64
var_4721 = relay.var("var_4721", dtype = "float64", shape = (60,))#candidate|4721|(60,)|var|float64
output = func_4719(var_4720,var_4721,)
func_4722 = relay.Function([var_4720,var_4721,], output)
mutated_mod['func_4722'] = func_4722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1691_call = mod.get_global_var('func_1691')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_4768 = relay.TupleGetItem(func_1691_call(), 0)
call_4769 = relay.TupleGetItem(func_1692_call(), 0)
func_34_call = mod.get_global_var('func_34')
func_35_call = mutated_mod.get_global_var('func_35')
call_4770 = relay.TupleGetItem(func_34_call(), 0)
call_4771 = relay.TupleGetItem(func_35_call(), 0)
output = relay.Tuple([call_4768,call_4770,])
output2 = relay.Tuple([call_4769,call_4771,])
func_4778 = relay.Function([], output)
mod['func_4778'] = func_4778
mod = relay.transform.InferType()(mod)
mutated_mod['func_4778'] = func_4778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4778_call = mutated_mod.get_global_var('func_4778')
call_4779 = func_4778_call()
output = call_4779
func_4780 = relay.Function([], output)
mutated_mod['func_4780'] = func_4780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_600_call = mod.get_global_var('func_600')
func_602_call = mutated_mod.get_global_var('func_602')
call_4781 = func_600_call()
call_4782 = func_600_call()
uop_4783 = relay.log2(call_4781.astype('float64')) # shape=(16, 12, 1)
uop_4785 = relay.log2(call_4782.astype('float64')) # shape=(16, 12, 1)
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_4800 = func_1666_call()
call_4801 = func_1666_call()
var_4813 = relay.var("var_4813", dtype = "float32", shape = (16, 12, 3))#candidate|4813|(16, 12, 3)|var|float32
bop_4814 = relay.less_equal(call_4781.astype('bool'), var_4813.astype('bool')) # shape=(16, 12, 3)
bop_4817 = relay.less_equal(call_4782.astype('bool'), var_4813.astype('bool')) # shape=(16, 12, 3)
func_3122_call = mod.get_global_var('func_3122')
func_3126_call = mutated_mod.get_global_var('func_3126')
var_4819 = relay.var("var_4819", dtype = "uint16", shape = (50,))#candidate|4819|(50,)|var|uint16
var_4820 = relay.var("var_4820", dtype = "uint16", shape = (650, 1))#candidate|4820|(650, 1)|var|uint16
call_4818 = func_3122_call(relay.reshape(var_4819.astype('uint16'), [1, 5, 10]), relay.reshape(var_4820.astype('uint16'), [13, 5, 10]), )
call_4821 = func_3122_call(relay.reshape(var_4819.astype('uint16'), [1, 5, 10]), relay.reshape(var_4820.astype('uint16'), [13, 5, 10]), )
func_2485_call = mod.get_global_var('func_2485')
func_2489_call = mutated_mod.get_global_var('func_2489')
var_4824 = relay.var("var_4824", dtype = "bool", shape = (780,))#candidate|4824|(780,)|var|bool
call_4823 = relay.TupleGetItem(func_2485_call(relay.reshape(var_4824.astype('bool'), [5, 13, 12]), relay.reshape(var_4824.astype('bool'), [5, 13, 12]), ), 0)
call_4825 = relay.TupleGetItem(func_2489_call(relay.reshape(var_4824.astype('bool'), [5, 13, 12]), relay.reshape(var_4824.astype('bool'), [5, 13, 12]), ), 0)
output = relay.Tuple([uop_4783,call_4800,bop_4814,call_4818,var_4819,var_4820,call_4823,var_4824,])
output2 = relay.Tuple([uop_4785,call_4801,bop_4817,call_4821,var_4819,var_4820,call_4825,var_4824,])
func_4826 = relay.Function([var_4813,var_4819,var_4820,var_4824,], output)
mod['func_4826'] = func_4826
mod = relay.transform.InferType()(mod)
var_4827 = relay.var("var_4827", dtype = "float32", shape = (16, 12, 3))#candidate|4827|(16, 12, 3)|var|float32
var_4828 = relay.var("var_4828", dtype = "uint16", shape = (50,))#candidate|4828|(50,)|var|uint16
var_4829 = relay.var("var_4829", dtype = "uint16", shape = (650, 1))#candidate|4829|(650, 1)|var|uint16
var_4830 = relay.var("var_4830", dtype = "bool", shape = (780,))#candidate|4830|(780,)|var|bool
output = func_4826(var_4827,var_4828,var_4829,var_4830,)
func_4831 = relay.Function([var_4827,var_4828,var_4829,var_4830,], output)
mutated_mod['func_4831'] = func_4831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4417_call = mod.get_global_var('func_4417')
func_4419_call = mutated_mod.get_global_var('func_4419')
call_4891 = relay.TupleGetItem(func_4417_call(), 0)
call_4892 = relay.TupleGetItem(func_4419_call(), 0)
func_2648_call = mod.get_global_var('func_2648')
func_2649_call = mutated_mod.get_global_var('func_2649')
call_4893 = func_2648_call()
call_4894 = func_2648_call()
output = relay.Tuple([call_4891,call_4893,])
output2 = relay.Tuple([call_4892,call_4894,])
func_4895 = relay.Function([], output)
mod['func_4895'] = func_4895
mod = relay.transform.InferType()(mod)
mutated_mod['func_4895'] = func_4895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4895_call = mutated_mod.get_global_var('func_4895')
call_4896 = func_4895_call()
output = call_4896
func_4897 = relay.Function([], output)
mutated_mod['func_4897'] = func_4897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3881_call = mod.get_global_var('func_3881')
func_3883_call = mutated_mod.get_global_var('func_3883')
call_4904 = relay.TupleGetItem(func_3881_call(), 3)
call_4905 = relay.TupleGetItem(func_3883_call(), 3)
uop_4912 = relay.sinh(call_4904.astype('float32')) # shape=(2304,)
uop_4914 = relay.sinh(call_4905.astype('float32')) # shape=(2304,)
output = relay.Tuple([uop_4912,])
output2 = relay.Tuple([uop_4914,])
func_4928 = relay.Function([], output)
mod['func_4928'] = func_4928
mod = relay.transform.InferType()(mod)
output = func_4928()
func_4929 = relay.Function([], output)
mutated_mod['func_4929'] = func_4929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2344_call = mod.get_global_var('func_2344')
func_2346_call = mutated_mod.get_global_var('func_2346')
call_4969 = relay.TupleGetItem(func_2344_call(), 0)
call_4970 = relay.TupleGetItem(func_2346_call(), 0)
func_2742_call = mod.get_global_var('func_2742')
func_2745_call = mutated_mod.get_global_var('func_2745')
const_4972 = relay.const(-9.229665, dtype = "float32")#candidate|4972|()|const|float32
const_4973 = relay.const([[-6.775183,-0.799625,-4.439108],[-4.953820,-2.060526,0.561444],[-5.881398,-6.615682,-9.460286],[8.790095,2.060770,-8.725689],[-0.599698,4.669466,9.314708],[-3.581799,-0.926826,-5.826704],[0.734739,1.389283,-1.424208],[9.854009,4.047627,-0.395487],[7.054668,-0.298835,-3.352223],[6.088209,4.044282,9.285921],[3.030331,-1.579237,2.166254],[6.310929,1.065144,-7.690673],[6.274397,-9.788619,-2.565773],[-5.516343,-8.586342,-1.043814],[-6.206913,-7.849121,6.097975],[-6.219752,5.888648,-4.499790],[-1.196437,6.344009,-8.295766],[9.525741,-3.421805,-8.838687],[-9.946959,-9.676630,7.181865],[8.847885,-0.799159,4.744484],[-5.193516,6.990288,8.617677]], dtype = "float64")#candidate|4973|(21, 3)|const|float64
call_4971 = relay.TupleGetItem(func_2742_call(relay.reshape(const_4972.astype('float32'), []), relay.reshape(const_4973.astype('float64'), [63,]), ), 3)
call_4974 = relay.TupleGetItem(func_2745_call(relay.reshape(const_4972.astype('float32'), []), relay.reshape(const_4973.astype('float64'), [63,]), ), 3)
output = relay.Tuple([call_4969,call_4971,const_4972,const_4973,])
output2 = relay.Tuple([call_4970,call_4974,const_4972,const_4973,])
func_4976 = relay.Function([], output)
mod['func_4976'] = func_4976
mod = relay.transform.InferType()(mod)
output = func_4976()
func_4977 = relay.Function([], output)
mutated_mod['func_4977'] = func_4977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1519_call = mod.get_global_var('func_1519')
func_1521_call = mutated_mod.get_global_var('func_1521')
call_5032 = relay.TupleGetItem(func_1519_call(), 0)
call_5033 = relay.TupleGetItem(func_1521_call(), 0)
output = relay.Tuple([call_5032,])
output2 = relay.Tuple([call_5033,])
func_5034 = relay.Function([], output)
mod['func_5034'] = func_5034
mod = relay.transform.InferType()(mod)
mutated_mod['func_5034'] = func_5034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5034_call = mutated_mod.get_global_var('func_5034')
call_5035 = func_5034_call()
output = call_5035
func_5036 = relay.Function([], output)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4446_call = mod.get_global_var('func_4446')
func_4447_call = mutated_mod.get_global_var('func_4447')
call_5070 = func_4446_call()
call_5071 = func_4446_call()
func_2207_call = mod.get_global_var('func_2207')
func_2209_call = mutated_mod.get_global_var('func_2209')
const_5075 = relay.const([[8.088615],[-9.052863],[1.662005],[9.641091],[-2.409592],[0.406657],[0.859619],[6.577879],[-2.684707],[7.537817],[-7.539417],[8.084497],[0.547658],[7.637679],[-1.254581],[0.030166],[-8.613798],[-2.000152],[0.447812],[9.709148],[9.586551],[0.907890],[9.701117],[9.276616],[-3.807965],[-0.647912],[-3.258754],[-7.000531],[-5.466064],[6.970023],[6.298368],[-2.580317],[-4.864399],[-2.840066],[3.532556],[9.878758],[-5.963575],[1.691858],[9.507186],[1.870777],[-9.704225],[-1.023972],[4.908279],[-0.917768],[3.946554],[-4.039810],[-2.743790],[-2.013717],[4.243305],[-0.721559],[-7.977073],[1.915527],[-0.599512],[-6.527560],[-5.565906],[3.710496],[1.864936],[4.312438],[5.864410],[5.049806],[3.161164],[4.041166],[-4.235652]], dtype = "float64")#candidate|5075|(63, 1)|const|float64
call_5074 = relay.TupleGetItem(func_2207_call(relay.reshape(const_5075.astype('float64'), [3, 7, 3])), 0)
call_5076 = relay.TupleGetItem(func_2209_call(relay.reshape(const_5075.astype('float64'), [3, 7, 3])), 0)
uop_5084 = relay.asinh(call_5070.astype('float32')) # shape=(2, 11, 6)
uop_5086 = relay.asinh(call_5071.astype('float32')) # shape=(2, 11, 6)
uop_5090 = relay.rsqrt(const_5075.astype('float32')) # shape=(63, 1)
bop_5092 = relay.minimum(uop_5090.astype('float32'), relay.reshape(const_5075.astype('float32'), relay.shape_of(uop_5090))) # shape=(63, 1)
bop_5095 = relay.logical_xor(bop_5092.astype('int32'), relay.reshape(uop_5090.astype('int32'), relay.shape_of(bop_5092))) # shape=(63, 1)
func_1993_call = mod.get_global_var('func_1993')
func_1995_call = mutated_mod.get_global_var('func_1995')
const_5099 = relay.const([-9.565345,5.822511,4.655229,0.318475,-1.493272,-2.921898,-8.377974,-5.829605,3.292568,9.067553,0.461737,3.995927,7.464497,0.892326,-6.633339,5.920726,8.730665,9.264894,-6.658255,4.813614,-8.949896,-3.225280,3.083298,-9.213437,-7.355985,-3.418137,9.664386,-1.815946,-6.862689,8.462126,-8.505057,3.399069,-9.978536,-2.700199,-5.478662,2.849529,-1.426682,9.112056,-7.935654,-9.170716,9.099875,-5.249802,8.563005,6.685558,-0.543425,-7.614853,8.015798,6.026320,-9.304210,-0.282924,8.668724,6.754162,-6.867950,4.169843,-3.536678,1.183500,-6.036678,-2.543289,-5.506588,0.659278,9.002504,1.763341,-1.795758,-2.716702,7.683636,0.049675,-8.010752,-0.378733,3.993225,4.322376,5.852651,4.721729,-5.618883,2.871425,6.537060,-6.851271,-6.849934,-3.310160,-2.786674,-6.182587,6.443544,-4.782619,-8.459661,-1.623455,-5.689729,-2.803574,-1.839177,-6.297241,5.758291,1.473458,-9.679050,5.651312,-4.073548,5.189502,-3.721715,-4.289928,1.327495,2.537355,3.000057,8.033559,3.110647,4.888488,7.058444,0.655729,-0.977315,-1.888612,-4.350765,8.050383,2.094772,7.073300,-2.398317,4.302952,-1.353028,-4.726146,8.134402,9.499450,5.149261,-6.543458,-9.917759,0.320247,4.370992,-7.116406,-0.478575,-6.676907,-8.111468,5.610077,4.168242,7.070076,-6.598586,3.859219,8.188873,-2.618084,9.760275,-4.209866,-3.036123,-1.429452,3.811922,9.789547,5.115153,4.276414,3.032188,-5.355258,7.308704,-6.796454,7.298058,1.232758,0.629269,4.165028,5.920549,-0.268714,-7.678694,4.673898,6.289689,0.119214,-5.351958,3.119201,7.457003,-6.509084,0.611224,-1.391898,-6.740415,5.860700,-7.814742,-6.525474,-9.032066,6.681287,-8.502922,-6.262355,-6.087850,-0.608135,-1.880037,-4.660976,0.161158,7.909493,-3.834870,-9.389485,0.222466,-6.564719,-4.150745,0.542386,2.153411,3.818399,3.049131,-1.144200,0.497667,-5.455032,-4.169917,-7.252780,8.525812,-1.741589,6.881628,-2.888210,-8.140993,-3.728539,-3.583737,-5.833573,6.579627,0.497312,4.508389,-0.650712,-4.967268,9.343897,9.311315,-7.961532,5.731204,-5.822248,0.303021,7.017317,0.521742,8.783443,-3.024253,-7.157784,7.300822,-7.147134,8.917178,-7.985292,-0.659221,-8.949455,5.981590,-7.232059,7.916453,0.666624,-6.033895,-4.192594,2.812362,8.228924,2.781094,9.460001,6.231806,-6.295433,-4.794586,-4.503024,-0.876748,-9.837379,4.013988,-2.654054,-1.526456,-9.982649,-6.180300,-5.309360,-5.565627,7.179948,5.989042,-0.438891,8.730004,1.974520,2.716022,-8.951597,-2.304224,4.997302,8.779804,-3.938245,-0.468361,-7.045541,-6.669466,-9.172243,-5.166083,-1.941892,-5.731786,-7.751163,6.152504,1.346938,6.074798,-3.187790,-7.849862,-9.849787,8.432421,8.888162,7.526648,0.966391,6.353450,-6.433418,2.342273,6.331988,0.574537,5.265974,-9.260773,-4.960851,-9.864631,0.964522,-1.805226,4.017251,6.173477,1.225612,-5.268929,-8.523927,-1.395809,-3.973039,9.680136,8.421800,7.895071,-9.202452,6.848901,-6.948782,8.035769,0.404868,6.490597,-1.721185,7.653468,4.152354,-0.011470,4.362599,-3.880137,-4.526899,-5.471078,-2.647007,8.439947,1.420474,6.393380,-7.861531,8.947628,2.997342,-2.132308,6.551187,2.632148,-3.860270,-9.009743,3.097608,8.426444,7.807608,4.796545,9.542624,-9.144752,-9.037741,-8.689174,-2.608711,-8.482044,-1.191434,6.305130,-9.079578,-8.381562,-7.964714,9.249673,7.396586,-7.300561,-6.766438,4.051125,-7.415219,-5.332134,3.613896,8.870279,-8.058546,9.719067,4.532821,7.435469,-1.663788,-6.855854,-8.399533,-3.370095,-1.620407,-0.746853,-9.610900,-6.111165,7.724406,9.988724,-0.136685,2.578650,-7.593898,8.680023,3.703039,-1.106404,2.399020,2.445819,-7.461722,5.977402,-1.519596,3.339970,9.247004,6.979389,-4.174667,-6.161086,6.698630,4.754114,-1.919325,1.568473,2.559240,4.089750,-4.825044,5.149639,-8.340721,7.759682,-5.940689,-7.071789,9.394214,7.758155], dtype = "float32")#candidate|5099|(385,)|const|float32
call_5098 = relay.TupleGetItem(func_1993_call(relay.reshape(const_5099.astype('float32'), [7, 5, 11])), 0)
call_5100 = relay.TupleGetItem(func_1995_call(relay.reshape(const_5099.astype('float32'), [7, 5, 11])), 0)
func_1047_call = mod.get_global_var('func_1047')
func_1048_call = mutated_mod.get_global_var('func_1048')
call_5116 = relay.TupleGetItem(func_1047_call(), 1)
call_5117 = relay.TupleGetItem(func_1048_call(), 1)
uop_5132 = relay.cosh(call_5070.astype('float32')) # shape=(2, 11, 6)
uop_5134 = relay.cosh(call_5071.astype('float32')) # shape=(2, 11, 6)
output = relay.Tuple([call_5074,uop_5084,bop_5095,call_5098,const_5099,call_5116,uop_5132,])
output2 = relay.Tuple([call_5076,uop_5086,bop_5095,call_5100,const_5099,call_5117,uop_5134,])
func_5140 = relay.Function([], output)
mod['func_5140'] = func_5140
mod = relay.transform.InferType()(mod)
mutated_mod['func_5140'] = func_5140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5140_call = mutated_mod.get_global_var('func_5140')
call_5141 = func_5140_call()
output = call_5141
func_5142 = relay.Function([], output)
mutated_mod['func_5142'] = func_5142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1122_call = mod.get_global_var('func_1122')
func_1123_call = mutated_mod.get_global_var('func_1123')
call_5149 = relay.TupleGetItem(func_1122_call(), 0)
call_5150 = relay.TupleGetItem(func_1123_call(), 0)
output = call_5149
output2 = call_5150
func_5152 = relay.Function([], output)
mod['func_5152'] = func_5152
mod = relay.transform.InferType()(mod)
output = func_5152()
func_5153 = relay.Function([], output)
mutated_mod['func_5153'] = func_5153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1286_call = mod.get_global_var('func_1286')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_5157 = func_1286_call()
call_5158 = func_1286_call()
uop_5174 = relay.tan(call_5157.astype('float32')) # shape=(4, 5, 3)
uop_5176 = relay.tan(call_5158.astype('float32')) # shape=(4, 5, 3)
uop_5193 = relay.asin(uop_5174.astype('float64')) # shape=(4, 5, 3)
uop_5195 = relay.asin(uop_5176.astype('float64')) # shape=(4, 5, 3)
uop_5196 = relay.cosh(uop_5174.astype('float64')) # shape=(4, 5, 3)
uop_5198 = relay.cosh(uop_5176.astype('float64')) # shape=(4, 5, 3)
func_121_call = mod.get_global_var('func_121')
func_122_call = mutated_mod.get_global_var('func_122')
call_5203 = relay.TupleGetItem(func_121_call(), 0)
call_5204 = relay.TupleGetItem(func_122_call(), 0)
var_5205 = relay.var("var_5205", dtype = "float32", shape = (4, 5, 3))#candidate|5205|(4, 5, 3)|var|float32
bop_5206 = relay.greater(uop_5174.astype('bool'), relay.reshape(var_5205.astype('bool'), relay.shape_of(uop_5174))) # shape=(4, 5, 3)
bop_5209 = relay.greater(uop_5176.astype('bool'), relay.reshape(var_5205.astype('bool'), relay.shape_of(uop_5176))) # shape=(4, 5, 3)
output = relay.Tuple([uop_5193,uop_5196,call_5203,bop_5206,])
output2 = relay.Tuple([uop_5195,uop_5198,call_5204,bop_5209,])
F = relay.Function([var_5205,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5205,], output2)
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
