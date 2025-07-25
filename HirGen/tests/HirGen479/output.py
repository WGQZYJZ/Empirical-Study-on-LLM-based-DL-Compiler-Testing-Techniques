import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_133 = relay.var("var_133", dtype = "float64", shape = (11, 15, 3))#candidate|133|(11, 15, 3)|var|float64
uop_134 = relay.cos(var_133.astype('float64')) # shape=(11, 15, 3)
output = relay.Tuple([uop_134,])
output2 = relay.Tuple([uop_134,])
func_143 = relay.Function([var_133,], output)
mod['func_143'] = func_143
mod = relay.transform.InferType()(mod)
var_144 = relay.var("var_144", dtype = "float64", shape = (11, 15, 3))#candidate|144|(11, 15, 3)|var|float64
output = func_143(var_144)
func_145 = relay.Function([var_144], output)
mutated_mod['func_145'] = func_145
mutated_mod = relay.transform.InferType()(mutated_mod)
var_201 = relay.var("var_201", dtype = "float32", shape = (4, 11, 3))#candidate|201|(4, 11, 3)|var|float32
uop_202 = relay.sinh(var_201.astype('float32')) # shape=(4, 11, 3)
func_143_call = mod.get_global_var('func_143')
func_145_call = mutated_mod.get_global_var('func_145')
const_205 = relay.const([-7.857492,9.884592,-3.642022,4.453479,7.250467,6.422079,8.172184,6.337698,-6.227743,-5.766418,-3.861151,2.414649,8.877184,-9.877960,5.505009,-5.771932,-3.195155,-5.696250,9.591529,9.359585,6.843290,-1.176547,9.088376,-5.260492,3.517738,8.591376,-6.252787,9.956483,1.302019,-3.128508,-3.172482,-9.008261,-0.200850,-8.240243,-0.946167,4.657270,-7.625400,-9.629402,4.336550,0.679575,7.157392,-2.218175,1.753540,-3.917890,-1.847679,6.766174,3.987340,0.464033,0.861722,2.080353,3.757403,3.424948,3.989940,-7.475806,-9.224785,3.209934,-2.720414,3.978651,-5.696255,-4.961405,8.327458,3.980317,2.418170,-4.765772,-6.838254,4.520983,-7.238206,-1.491081,-3.271969,-4.242530,-4.167266,3.937086,-4.061970,1.674628,-4.124968,3.147500,5.809344,-4.676531,8.475214,6.992278,-3.995889,0.701173,-0.905799,-0.145178,-8.973824,8.813179,9.612799,-3.758919,-0.775020,-4.281217,5.786760,-8.935319,-6.402897,-2.222265,1.812516,-1.603736,-0.869344,8.799599,7.891065,3.268308,-1.692935,-5.805362,3.775019,9.868075,-3.763083,-4.590816,7.512502,4.426410,3.551027,8.709095,8.915352,6.818264,-9.049230,-0.480928,-8.871361,8.848355,9.997618,-1.047263,-8.995145,-8.503694,1.157652,4.041782,5.145581,5.278863,-9.295525,8.546868,-0.384261,0.465937,0.749614,-6.679796,1.145351,0.879312,3.777732,-6.367306,9.952772,2.128850,2.745926,-8.361145,2.732375,-8.407982,-8.843195,5.413054,-7.888264,3.988389,8.987074,5.953887,-2.932376,5.756936,4.683202,1.721873,-7.113961,7.681347,7.909605,-5.473683,5.505611,-4.805952,-8.857321,-2.772927,-5.818638,0.403890,1.602474,8.475033,0.742069,-2.558573,-8.410761,3.830901,-5.021885,-0.107305,-5.993682,-8.122011,3.229476,-2.549044,-2.966237,-4.102721,-8.703853,-4.594006,5.225455,2.713506,-9.684481,8.480585,-9.087397,8.739938,5.573002,-6.105143,-2.646724,-2.629007,-1.690365,-1.795194,9.434646,0.182790,-6.523273,-6.551154,1.562699,-2.904359,9.251966,-5.417583,-4.092797,-8.545898,-4.577990,-4.923085,9.994261,-5.258393,2.936616,-4.200675,-0.704980,-5.193538,-2.627224,-9.956827,9.232854,8.605432,-1.529003,-5.433397,-7.489520,-5.242055,8.066688,0.872995,1.521726,-9.503876,-3.423289,-9.847584,3.162954,5.484653,1.086145,4.299093,-8.900010,4.777666,3.361475,-2.196035,-3.530478,-2.875910,1.050869,-9.181242,2.383888,6.282182,0.619335,-2.199842,-5.129602,-8.721952,8.489455,-7.900133,1.081446,-5.727974,8.834736,-8.165461,-0.096910,-3.481111,-3.126137,-5.727236,6.893035,-0.341542,9.637991,9.110693,-7.558176,0.354277,-4.032042,-5.800190,2.125871,-3.399374,1.287611,-4.232479,4.382715,1.846921,6.178244,8.132104,3.838642,-3.364941,2.920360,-6.942128,2.865072,2.302585,-3.598334,9.796241,0.155962,-0.882763,-0.520017,-0.689673,5.149408,-7.486566,8.100068,-1.413968,2.454562,-0.961345,-4.192201,-2.739961,-5.169523,8.210467,8.971590,0.379713,-4.732905,5.791881,-7.862979,-2.496008,0.561751,1.200722,9.765629,3.408580,-8.450263,2.844095,9.866342,-4.652817,7.723617,-3.183524,5.388964,6.553195,9.684528,-0.867567,-4.606008,-1.785826,2.396227,5.282157,6.674601,7.022976,-3.479893,-6.549595,3.571545,6.317947,8.477871,1.312976,3.023846,-7.151356,-8.236696,3.554189,-0.684002,-7.215197,4.262377,-6.867577,3.658185,-4.263102,-4.720339,7.728361,4.548631,-6.060307,-1.501082,5.944807,7.533204,-7.167369,9.213795,-1.980869,7.786030,0.193464,-5.256675,8.369410,-3.634817,7.748299,5.215490,-2.032478,-5.372066,7.114001,-7.608231,-6.677731,-4.016826,4.095933,-4.505175,5.597170,4.339285,-2.202002,-1.900764,5.751987,8.989404,7.518203,6.808574,-3.043209,8.426676,-6.470869,-8.128370,8.309092,9.091524,-7.495233,-3.952155,-5.980579,7.955246,-5.888135,-1.540421,-0.569676,-7.657355,-3.855153,2.529068,6.972403,-4.459916,-7.140083,9.555490,-0.310338,2.896928,-7.898450,-7.764381,3.433953,-1.794048,-9.239961,8.841050,-7.258982,-0.321990,6.915704,4.705068,-6.323309,-2.487949,9.949227,-5.567454,-0.392679,-8.041779,-5.065490,1.773143,-6.393611,5.228634,1.097795,4.522887,-6.612975,-2.076897,8.392648,1.890278,-5.340860,0.293865,3.295964,4.150037,5.177544,-6.189219,-3.509174,1.806154,4.194395,0.164722,0.785759,5.383237,2.574614,8.847905,9.373334,-2.910655,-7.897205,3.153846,-9.490249,5.978226,0.715244,7.078356,-3.403995,-3.662137,1.559142,-1.412674,5.855093,-8.307773,1.418203,4.682146,-4.408223,-7.711871,5.492543,-7.973328,-8.662337,8.992584,-1.601615,-9.651854,2.919726,-4.551970,-7.235255,4.243431,-4.861243,-5.131540,2.106448,9.002738,-4.016158,-8.169199,4.721317,8.861592,2.415151,2.300965,0.123812,-6.070035,3.772155,6.330602,7.806877,6.600926,-7.928513,3.307548,8.499761,-4.659129,8.618012,-0.370618,7.388560,-9.055915,-1.109849,-8.874727,6.201199,3.460840,-5.830948,0.917561,9.950129,3.278852,-1.475348,-4.174458,5.306443,9.445290,8.411449,-5.480583,1.884647,1.304119,-5.302462,7.127745,-9.432514,-1.947854], dtype = "float64")#candidate|205|(495,)|const|float64
call_204 = relay.TupleGetItem(func_143_call(relay.reshape(const_205.astype('float64'), [11, 15, 3])), 0)
call_206 = relay.TupleGetItem(func_145_call(relay.reshape(const_205.astype('float64'), [11, 15, 3])), 0)
uop_207 = relay.asinh(uop_202.astype('float32')) # shape=(4, 11, 3)
const_210 = relay.const([[[-4.564220,3.889621,-4.516532],[6.965577,-8.207636,9.541872],[4.453882,9.578305,8.599585],[-6.317967,-0.349544,-0.407046],[5.664630,-6.978979,-3.689010],[5.905727,8.136383,-2.830741],[0.391709,7.939462,3.644380],[1.535461,-6.341752,3.967014],[-3.236055,2.873630,-9.447719],[-9.518263,5.444693,-8.807240],[-8.884758,-9.099299,-4.995401]],[[-0.161454,-9.573269,9.100860],[-5.448379,7.883375,2.251824],[-9.510813,-9.656166,8.893751],[0.110502,-9.856769,-4.071445],[5.264218,-9.562701,-1.547308],[-8.862817,-7.794131,2.755435],[8.421404,-3.881609,-8.398458],[4.536608,-3.132041,-5.946273],[-8.342717,2.637018,2.410106],[8.372868,8.076754,-7.161907],[-8.145546,-8.455816,-9.160877]],[[2.144207,1.413277,-3.354228],[7.926385,-5.286741,6.253004],[1.426830,6.062643,-3.362089],[-0.669587,7.051524,-2.776986],[-9.985030,-0.551072,7.571490],[-4.989319,-1.997393,8.249242],[1.732832,-6.067736,-3.221146],[7.250514,0.087771,-0.264983],[8.984173,4.697059,-6.043106],[-9.599428,6.322820,2.623838],[4.064620,8.578821,8.181577]],[[-6.247517,8.780792,4.586455],[-2.457835,-7.972810,0.768386],[-8.831814,8.912771,7.281351],[8.705076,-0.757505,-2.885889],[4.042075,2.990949,-4.326796],[6.035094,-0.494004,7.863512],[-5.792033,-5.950988,-4.652767],[-2.092500,-7.316594,-7.874061],[1.354980,5.225734,-7.222487],[-2.734140,-1.436312,-1.526165],[-0.689893,5.994122,3.411068]]], dtype = "float32")#candidate|210|(4, 11, 3)|const|float32
bop_211 = relay.maximum(uop_202.astype('int32'), relay.reshape(const_210.astype('int32'), relay.shape_of(uop_202))) # shape=(4, 11, 3)
func_143_call = mod.get_global_var('func_143')
func_145_call = mutated_mod.get_global_var('func_145')
call_230 = relay.TupleGetItem(func_143_call(relay.reshape(call_204.astype('float64'), [11, 15, 3])), 0)
call_231 = relay.TupleGetItem(func_145_call(relay.reshape(call_204.astype('float64'), [11, 15, 3])), 0)
bop_248 = relay.bitwise_or(bop_211.astype('int32'), relay.reshape(const_210.astype('int32'), relay.shape_of(bop_211))) # shape=(4, 11, 3)
uop_258 = relay.acosh(uop_202.astype('float64')) # shape=(4, 11, 3)
func_143_call = mod.get_global_var('func_143')
func_145_call = mutated_mod.get_global_var('func_145')
call_268 = relay.TupleGetItem(func_143_call(relay.reshape(call_230.astype('float64'), [11, 15, 3])), 0)
call_269 = relay.TupleGetItem(func_145_call(relay.reshape(call_230.astype('float64'), [11, 15, 3])), 0)
bop_278 = relay.floor_mod(uop_258.astype('float32'), relay.reshape(var_201.astype('float32'), relay.shape_of(uop_258))) # shape=(4, 11, 3)
output = relay.Tuple([call_204,const_205,uop_207,call_230,bop_248,call_268,bop_278,])
output2 = relay.Tuple([call_206,const_205,uop_207,call_231,bop_248,call_269,bop_278,])
func_283 = relay.Function([var_201,], output)
mod['func_283'] = func_283
mod = relay.transform.InferType()(mod)
var_284 = relay.var("var_284", dtype = "float32", shape = (4, 11, 3))#candidate|284|(4, 11, 3)|var|float32
output = func_283(var_284)
func_285 = relay.Function([var_284], output)
mutated_mod['func_285'] = func_285
mutated_mod = relay.transform.InferType()(mutated_mod)
var_662 = relay.var("var_662", dtype = "int32", shape = (11, 8, 12))#candidate|662|(11, 8, 12)|var|int32
var_663 = relay.var("var_663", dtype = "int32", shape = (11, 8, 12))#candidate|663|(11, 8, 12)|var|int32
bop_664 = relay.multiply(var_662.astype('int32'), relay.reshape(var_663.astype('int32'), relay.shape_of(var_662))) # shape=(11, 8, 12)
func_283_call = mod.get_global_var('func_283')
func_285_call = mutated_mod.get_global_var('func_285')
const_670 = relay.const([-3.445652,3.438578,-4.622180,4.284813,-4.209352,-1.796963,-9.537826,-6.449874,3.612483,3.477806,4.199799,-7.037758,-6.846226,0.251013,-3.863468,-6.973220,-3.405316,7.494691,6.330342,-8.355454,1.370972,1.998915,2.017034,2.690723,7.592753,-3.346751,4.702342,2.979822,-2.045580,-7.779559,5.890267,-8.804068,-9.432991,-0.493707,-6.156838,5.059360,-0.835557,6.250029,-3.329279,-3.229496,4.514553,-2.655609,6.350052,6.504556,6.657635,-9.710712,-2.302250,-6.151247,-2.521597,-5.429935,9.680407,-6.543057,3.745746,4.257520,-8.482513,6.252881,7.400491,1.204687,5.510237,-3.590604,-5.481717,9.739411,2.664199,9.285819,3.296865,-2.446280,8.045083,-9.350577,-6.091179,8.828144,1.827866,3.492856,-7.610811,7.390418,9.932254,-7.936211,-7.189986,-5.349478,9.671832,1.040592,5.145376,9.449844,-1.957802,2.858309,-7.085452,3.352506,-1.130858,-3.378783,4.093669,-4.469535,7.497901,-0.380032,1.603791,-3.730668,-9.465296,6.624440,3.852299,8.424492,-6.510987,2.280975,4.178173,-8.297246,3.785378,-7.682929,-1.962077,3.485583,-7.348253,1.771604,-6.328728,-1.421173,5.172373,-5.951761,2.952391,-0.723833,8.528006,-5.426098,-4.265507,-9.174178,6.301052,0.609411,2.889633,4.832421,-9.360486,7.472477,-5.076477,-5.764900,6.232157,5.955510,-7.279104,-4.652204,7.667481,-4.788484], dtype = "float32")#candidate|670|(132,)|const|float32
call_669 = relay.TupleGetItem(func_283_call(relay.reshape(const_670.astype('float32'), [4, 11, 3])), 0)
call_671 = relay.TupleGetItem(func_285_call(relay.reshape(const_670.astype('float32'), [4, 11, 3])), 0)
output = relay.Tuple([bop_664,call_669,const_670,])
output2 = relay.Tuple([bop_664,call_671,const_670,])
func_672 = relay.Function([var_662,var_663,], output)
mod['func_672'] = func_672
mod = relay.transform.InferType()(mod)
mutated_mod['func_672'] = func_672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_672_call = mutated_mod.get_global_var('func_672')
var_674 = relay.var("var_674", dtype = "int32", shape = (11, 8, 12))#candidate|674|(11, 8, 12)|var|int32
var_675 = relay.var("var_675", dtype = "int32", shape = (11, 8, 12))#candidate|675|(11, 8, 12)|var|int32
call_673 = func_672_call(var_674,var_675,)
output = call_673
func_676 = relay.Function([var_674,var_675,], output)
mutated_mod['func_676'] = func_676
mutated_mod = relay.transform.InferType()(mutated_mod)
const_838 = relay.const(10, dtype = "uint8")#candidate|838|()|const|uint8
var_839 = relay.var("var_839", dtype = "uint8", shape = (1, 1, 8))#candidate|839|(1, 1, 8)|var|uint8
bop_840 = relay.multiply(const_838.astype('uint8'), var_839.astype('uint8')) # shape=(1, 1, 8)
uop_844 = relay.log(bop_840.astype('float64')) # shape=(1, 1, 8)
output = relay.Tuple([uop_844,])
output2 = relay.Tuple([uop_844,])
func_847 = relay.Function([var_839,], output)
mod['func_847'] = func_847
mod = relay.transform.InferType()(mod)
var_848 = relay.var("var_848", dtype = "uint8", shape = (1, 1, 8))#candidate|848|(1, 1, 8)|var|uint8
output = func_847(var_848)
func_849 = relay.Function([var_848], output)
mutated_mod['func_849'] = func_849
mutated_mod = relay.transform.InferType()(mutated_mod)
var_880 = relay.var("var_880", dtype = "float32", shape = (7, 12, 4))#candidate|880|(7, 12, 4)|var|float32
uop_881 = relay.erf(var_880.astype('float32')) # shape=(7, 12, 4)
output = relay.Tuple([uop_881,])
output2 = relay.Tuple([uop_881,])
func_884 = relay.Function([var_880,], output)
mod['func_884'] = func_884
mod = relay.transform.InferType()(mod)
var_885 = relay.var("var_885", dtype = "float32", shape = (7, 12, 4))#candidate|885|(7, 12, 4)|var|float32
output = func_884(var_885)
func_886 = relay.Function([var_885], output)
mutated_mod['func_886'] = func_886
mutated_mod = relay.transform.InferType()(mutated_mod)
var_965 = relay.var("var_965", dtype = "float64", shape = (3, 4, 12))#candidate|965|(3, 4, 12)|var|float64
uop_966 = relay.sin(var_965.astype('float64')) # shape=(3, 4, 12)
output = relay.Tuple([uop_966,])
output2 = relay.Tuple([uop_966,])
func_978 = relay.Function([var_965,], output)
mod['func_978'] = func_978
mod = relay.transform.InferType()(mod)
mutated_mod['func_978'] = func_978
mutated_mod = relay.transform.InferType()(mutated_mod)
var_979 = relay.var("var_979", dtype = "float64", shape = (3, 4, 12))#candidate|979|(3, 4, 12)|var|float64
func_978_call = mutated_mod.get_global_var('func_978')
call_980 = func_978_call(var_979)
output = call_980
func_981 = relay.Function([var_979], output)
mutated_mod['func_981'] = func_981
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1131 = relay.var("var_1131", dtype = "float32", shape = (6, 16, 3))#candidate|1131|(6, 16, 3)|var|float32
uop_1132 = relay.exp(var_1131.astype('float32')) # shape=(6, 16, 3)
output = relay.Tuple([uop_1132,])
output2 = relay.Tuple([uop_1132,])
func_1143 = relay.Function([var_1131,], output)
mod['func_1143'] = func_1143
mod = relay.transform.InferType()(mod)
mutated_mod['func_1143'] = func_1143
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1144 = relay.var("var_1144", dtype = "float32", shape = (6, 16, 3))#candidate|1144|(6, 16, 3)|var|float32
func_1143_call = mutated_mod.get_global_var('func_1143')
call_1145 = func_1143_call(var_1144)
output = call_1145
func_1146 = relay.Function([var_1144], output)
mutated_mod['func_1146'] = func_1146
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1572 = relay.const([[[-9,-6,8,-3,10,4,7,10],[9,-9,6,-3,1,-5,-5,8],[7,-10,-5,6,6,-9,-9,5],[3,-7,3,-7,1,9,-9,9],[1,3,-4,-1,8,-5,7,3],[3,-10,1,3,1,7,6,-6],[-5,3,7,-10,-4,-1,5,2]]], dtype = "int8")#candidate|1572|(1, 7, 8)|const|int8
var_1573 = relay.var("var_1573", dtype = "int8", shape = (1, 7, 8))#candidate|1573|(1, 7, 8)|var|int8
bop_1574 = relay.minimum(const_1572.astype('int8'), relay.reshape(var_1573.astype('int8'), relay.shape_of(const_1572))) # shape=(1, 7, 8)
uop_1585 = relay.atan(bop_1574.astype('float64')) # shape=(1, 7, 8)
bop_1587 = relay.greater_equal(bop_1574.astype('bool'), relay.reshape(var_1573.astype('bool'), relay.shape_of(bop_1574))) # shape=(1, 7, 8)
bop_1596 = relay.bitwise_xor(uop_1585.astype('uint64'), relay.reshape(bop_1574.astype('uint64'), relay.shape_of(uop_1585))) # shape=(1, 7, 8)
bop_1599 = relay.mod(uop_1585.astype('float64'), relay.reshape(bop_1587.astype('float64'), relay.shape_of(uop_1585))) # shape=(1, 7, 8)
output = relay.Tuple([bop_1596,bop_1599,])
output2 = relay.Tuple([bop_1596,bop_1599,])
func_1602 = relay.Function([var_1573,], output)
mod['func_1602'] = func_1602
mod = relay.transform.InferType()(mod)
mutated_mod['func_1602'] = func_1602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1603 = relay.var("var_1603", dtype = "int8", shape = (1, 7, 8))#candidate|1603|(1, 7, 8)|var|int8
func_1602_call = mutated_mod.get_global_var('func_1602')
call_1604 = func_1602_call(var_1603)
output = call_1604
func_1605 = relay.Function([var_1603], output)
mutated_mod['func_1605'] = func_1605
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1707 = relay.const([[[-6.777129,-4.897662,8.302904,-4.050678,6.966325],[-5.381209,0.970195,-3.482107,1.333837,1.606180],[2.247845,0.212101,-2.877274,-8.129708,2.534359],[-6.782213,4.400886,-3.046854,-1.446031,-9.851670],[4.725257,0.396662,2.384956,9.946951,-8.915369],[1.345706,5.363366,3.669749,-1.104438,9.352644],[3.996463,-3.637274,-2.212430,-7.084665,0.806344],[-9.406578,5.458890,6.031547,9.977334,-5.995501],[-8.313135,0.485085,-7.618518,3.676197,6.702638],[3.805587,-8.350525,0.008802,-7.923399,9.046310],[-0.544711,-1.415477,-4.574888,8.678936,-9.845480],[9.762170,0.102733,-3.054042,1.549213,-4.428433],[1.744563,-1.516367,4.590238,-2.424462,6.216111],[5.971911,-0.709575,9.252688,-2.036253,-6.064244]],[[-4.329244,8.505321,9.210715,-2.591385,7.800701],[4.127842,-3.249846,-3.573563,4.758833,8.109299],[8.940309,9.775379,-9.760220,-6.772854,5.890176],[2.480733,-4.369186,5.769784,3.976944,7.129272],[-1.021622,2.143777,-3.854709,4.761613,-4.147449],[-2.699677,2.568558,8.420551,-0.571096,-5.060449],[7.668138,-1.567336,-0.522824,9.407784,3.808123],[-1.323532,4.040336,-8.994805,-2.143094,9.280359],[-3.564807,-1.107586,9.826704,2.253474,8.966168],[4.529213,5.005016,-8.693594,6.724807,2.633190],[-3.022854,3.904563,3.907402,1.777391,8.210083],[3.921449,-8.615890,4.373646,7.826853,-1.811878],[8.235486,6.809664,5.379340,-8.448979,5.457097],[8.358439,-4.043182,3.642091,-5.838922,5.813243]],[[-6.387308,1.212602,-8.720938,-3.289461,6.928744],[-5.080129,6.992091,0.311513,3.601733,7.276562],[-6.992682,0.650645,4.346666,-2.578951,1.377190],[8.543275,-3.718369,8.081907,-5.424750,0.025157],[-0.371543,-0.141250,6.360262,-6.305501,5.592974],[-9.184678,-5.602869,-4.160432,-5.151126,2.985430],[-4.530677,5.663325,4.846651,2.766087,5.665276],[6.051945,-0.144613,2.738291,1.075308,6.855235],[5.762127,-3.181845,8.856602,-1.583303,-2.607944],[9.817475,-6.230323,2.078235,7.127544,5.737182],[8.973561,-5.163797,-9.348918,-7.405613,8.794204],[0.184008,6.105634,-3.640385,-4.145523,-8.669239],[-0.362066,-9.740213,3.643955,-1.564441,-5.804817],[3.223499,-7.040924,-1.759257,5.317914,5.521958]],[[-9.557018,3.892660,-6.359848,-0.355722,-0.567401],[3.208392,-0.248602,-1.047490,-8.882986,2.638276],[-0.228499,-2.240835,-1.785275,-4.222537,2.941691],[6.480170,-4.418048,0.973037,-2.696525,7.401622],[3.554036,-4.956072,-2.466281,5.440440,2.591525],[-6.406900,9.261975,5.926721,9.498599,4.177775],[6.446231,-8.812865,6.931543,-8.757985,7.617346],[6.870086,7.049411,-1.121536,-4.325849,-1.253518],[-5.835251,1.195257,6.165659,-8.252275,-1.040001],[-2.717161,-5.921059,2.946846,-4.059030,2.751761],[-2.758262,-1.630722,-9.597007,0.666483,-4.535279],[7.088117,-2.354164,-5.914921,2.957750,-6.652786],[-9.239254,2.750368,0.190053,6.880863,-6.969403],[0.836903,6.780145,-8.405394,1.563907,-4.189440]],[[0.815878,-0.515430,-6.349404,-7.986568,5.193310],[-4.511283,8.771206,-1.842885,-2.533894,-0.969773],[2.263635,5.269731,-1.553818,-4.202739,-6.496925],[2.582570,-8.298041,1.639373,5.276032,-1.023041],[1.628327,-0.949929,-8.875957,5.215847,-7.888788],[-8.497294,-2.032534,-1.301849,5.930422,-6.630534],[4.998662,-4.982179,2.330420,9.285829,8.299128],[-4.754535,-5.920532,6.549449,5.426384,5.487408],[-4.036860,1.311659,-2.777632,0.590731,7.197845],[6.956427,-1.486835,-9.411414,8.620896,-8.595665],[-7.308980,4.501524,3.970609,2.737424,-5.223960],[7.737380,-9.237499,2.639604,-0.705304,8.099978],[-4.207259,2.748735,-7.806889,-0.541291,0.455486],[-3.520496,3.638647,-7.687635,-9.494657,-0.506050]],[[-9.285121,3.736499,-5.089140,8.809735,-8.956792],[-9.897301,7.032447,6.546619,-8.159346,-1.678990],[-3.306026,0.426274,-2.846741,-3.639658,3.681337],[2.154543,-3.923702,9.247186,0.382372,-0.322295],[9.517921,-1.310277,-4.507565,-5.425133,-4.513916],[-0.427732,1.621827,-3.368399,0.932477,-9.558623],[0.675781,-7.011082,-1.387457,8.204439,0.463850],[1.487399,-2.100058,1.223351,1.634865,4.096325],[-3.801319,-6.289672,1.925075,-3.252694,-4.794005],[-7.754225,-2.870501,9.232207,-7.168679,7.290884],[-1.723060,-6.733514,-6.799971,5.335041,8.463448],[9.852651,-3.711124,1.432933,2.079097,-4.554572],[-6.420171,9.459689,-4.252443,0.816373,2.901138],[-1.122337,-2.676829,9.280710,-2.919479,-3.277196]],[[4.281734,-9.718489,-3.403301,-8.892046,2.866331],[6.112188,8.214257,-8.984764,6.766127,-6.826860],[-0.591281,7.412735,1.172950,-6.058167,1.084988],[2.370658,-0.240991,1.818464,6.318844,-2.673151],[-2.475785,-4.835905,4.924724,1.487150,-2.094651],[6.738274,-4.933375,1.026209,0.127635,-2.582549],[8.329415,-1.241743,8.169528,-7.621691,9.301462],[6.879758,-7.545263,8.796166,-3.569663,-3.080543],[-5.849614,-6.337318,-2.985518,-1.491206,5.931989],[8.376416,-8.634746,-6.439939,5.879428,-4.569876],[-8.576188,-1.435483,9.778985,-9.143610,7.111716],[-7.506679,-8.658053,-4.268577,1.439596,2.744204],[3.177706,1.245365,-7.151286,2.668109,-3.181466],[-8.386900,2.720907,0.556175,-2.287410,1.987294]],[[-5.586382,5.561230,-9.998706,-2.237955,-3.425832],[-0.393421,-4.999840,1.324379,8.011242,-6.651880],[-8.434472,-4.302348,3.242503,-0.234413,8.336202],[9.391242,0.540065,9.823873,2.722396,1.214758],[9.915591,3.483322,6.887100,-5.195755,-7.589549],[-2.564575,2.701475,-6.399808,-1.086244,-1.017954],[-1.293848,-6.454403,-6.576034,5.847096,9.184062],[2.659556,-8.188841,-6.971161,5.808529,2.295735],[3.893518,-3.937190,-2.364672,7.491600,7.096947],[8.555396,-3.748294,5.094986,0.811383,-9.927826],[-1.475779,9.094756,-6.601002,-9.353175,-9.585904],[1.803689,-3.697231,-8.059934,6.016495,0.026599],[4.082322,-4.735681,-8.231346,-9.966026,2.158106],[-2.416161,-2.325640,-8.773044,1.761024,-1.378757]],[[-0.754194,4.029308,4.063135,-6.247156,-5.942545],[2.597014,-3.378222,8.539437,2.253357,-7.075329],[-1.256659,-4.954974,-5.786321,1.074650,-6.013362],[6.316847,-6.452824,2.395092,-3.279961,-4.453368],[5.072191,-1.503540,2.492023,2.753439,5.750309],[8.560640,-8.279676,-4.660240,9.963073,7.605466],[2.610546,-1.550102,7.807975,4.961769,1.934413],[-3.035882,1.626324,-2.268723,-2.295045,2.528453],[6.149280,5.583861,8.103754,-6.910979,-4.459435],[-9.586422,-3.701756,6.066970,-0.485341,2.202990],[-8.352066,-6.715705,-5.512516,-8.769914,-3.391678],[-4.982110,1.417544,-4.959971,9.668237,4.729728],[-2.881018,7.308124,-5.267471,-7.022171,3.433285],[9.893589,-5.539809,9.521021,-9.430089,7.975739]],[[-7.805726,7.364286,-8.839237,-9.704599,-2.108786],[1.808457,7.838330,-5.028438,0.111472,-3.925047],[-6.090075,-9.669489,6.186811,-9.414426,0.394089],[6.586789,9.352874,3.273122,-5.583040,-5.494963],[4.471138,1.563508,-1.259391,3.746316,-5.479682],[6.043305,6.500652,9.482999,8.897738,-6.585644],[-8.412311,-2.325397,-3.735842,8.977998,9.578008],[-5.852647,3.521716,0.488348,4.194046,7.989329],[-1.596508,-9.364975,-7.986783,0.403369,3.758140],[-8.671534,2.361995,-8.791335,2.880064,-9.733765],[4.810563,0.792847,-9.664189,-1.471238,7.890664],[8.144420,-2.443362,9.629626,-8.026674,4.683165],[9.339787,3.315807,-6.227774,-6.415119,8.421390],[7.459276,7.012959,2.502418,9.064853,5.219862]],[[8.870035,4.373885,5.571150,-5.908862,2.031305],[9.593521,1.243258,6.013421,-8.179577,3.030321],[-2.894488,-9.472146,-4.121338,8.110209,-2.816742],[-5.770534,2.421016,3.042475,2.384084,-0.022322],[3.395683,3.954638,-2.204581,5.534615,-7.766178],[-6.073898,8.726140,3.908312,-2.398739,7.544245],[4.511266,-4.253337,8.343049,6.721422,1.270632],[8.700734,-5.132331,-1.755339,3.166287,6.974478],[-4.876811,-2.712263,7.130147,7.006119,-7.366669],[-5.960840,2.445013,1.363196,-7.293617,1.590826],[-2.500490,7.137363,9.969267,-8.511889,5.259754],[-4.292075,7.021244,9.255881,-7.372130,8.870050],[4.034683,8.294605,-7.897281,-6.670124,3.067689],[3.885732,-6.156767,-1.914813,-8.833920,7.907478]]], dtype = "float32")#candidate|1707|(11, 14, 5)|const|float32
uop_1708 = relay.exp(const_1707.astype('float32')) # shape=(11, 14, 5)
output = uop_1708
output2 = uop_1708
func_1716 = relay.Function([], output)
mod['func_1716'] = func_1716
mod = relay.transform.InferType()(mod)
output = func_1716()
func_1717 = relay.Function([], output)
mutated_mod['func_1717'] = func_1717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_1718 = func_1716_call()
call_1719 = func_1716_call()
func_884_call = mod.get_global_var('func_884')
func_886_call = mutated_mod.get_global_var('func_886')
var_1729 = relay.var("var_1729", dtype = "float32", shape = (336,))#candidate|1729|(336,)|var|float32
call_1728 = relay.TupleGetItem(func_884_call(relay.reshape(var_1729.astype('float32'), [7, 12, 4])), 0)
call_1730 = relay.TupleGetItem(func_886_call(relay.reshape(var_1729.astype('float32'), [7, 12, 4])), 0)
bop_1746 = relay.subtract(call_1728.astype('uint8'), relay.reshape(var_1729.astype('uint8'), relay.shape_of(call_1728))) # shape=(7, 12, 4)
bop_1749 = relay.subtract(call_1730.astype('uint8'), relay.reshape(var_1729.astype('uint8'), relay.shape_of(call_1730))) # shape=(7, 12, 4)
var_1750 = relay.var("var_1750", dtype = "float32", shape = (11, 14, 5))#candidate|1750|(11, 14, 5)|var|float32
bop_1751 = relay.right_shift(call_1718.astype('uint8'), relay.reshape(var_1750.astype('uint8'), relay.shape_of(call_1718))) # shape=(11, 14, 5)
bop_1754 = relay.right_shift(call_1719.astype('uint8'), relay.reshape(var_1750.astype('uint8'), relay.shape_of(call_1719))) # shape=(11, 14, 5)
output = relay.Tuple([bop_1746,bop_1751,])
output2 = relay.Tuple([bop_1749,bop_1754,])
func_1756 = relay.Function([var_1729,var_1750,], output)
mod['func_1756'] = func_1756
mod = relay.transform.InferType()(mod)
mutated_mod['func_1756'] = func_1756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1756_call = mutated_mod.get_global_var('func_1756')
var_1758 = relay.var("var_1758", dtype = "float32", shape = (336,))#candidate|1758|(336,)|var|float32
var_1759 = relay.var("var_1759", dtype = "float32", shape = (11, 14, 5))#candidate|1759|(11, 14, 5)|var|float32
call_1757 = func_1756_call(var_1758,var_1759,)
output = call_1757
func_1760 = relay.Function([var_1758,var_1759,], output)
mutated_mod['func_1760'] = func_1760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_1813 = func_1716_call()
call_1814 = func_1716_call()
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_1815 = func_1716_call()
call_1816 = func_1716_call()
output = relay.Tuple([call_1813,call_1815,])
output2 = relay.Tuple([call_1814,call_1816,])
func_1817 = relay.Function([], output)
mod['func_1817'] = func_1817
mod = relay.transform.InferType()(mod)
output = func_1817()
func_1818 = relay.Function([], output)
mutated_mod['func_1818'] = func_1818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_1836 = relay.TupleGetItem(func_1817_call(), 1)
call_1837 = relay.TupleGetItem(func_1818_call(), 1)
output = relay.Tuple([call_1836,])
output2 = relay.Tuple([call_1837,])
func_1888 = relay.Function([], output)
mod['func_1888'] = func_1888
mod = relay.transform.InferType()(mod)
mutated_mod['func_1888'] = func_1888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1888_call = mutated_mod.get_global_var('func_1888')
call_1889 = func_1888_call()
output = call_1889
func_1890 = relay.Function([], output)
mutated_mod['func_1890'] = func_1890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1888_call = mod.get_global_var('func_1888')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_1897 = relay.TupleGetItem(func_1888_call(), 0)
call_1898 = relay.TupleGetItem(func_1890_call(), 0)
var_1904 = relay.var("var_1904", dtype = "float32", shape = (11, 14, 5))#candidate|1904|(11, 14, 5)|var|float32
bop_1905 = relay.bitwise_and(call_1897.astype('int16'), relay.reshape(var_1904.astype('int16'), relay.shape_of(call_1897))) # shape=(11, 14, 5)
bop_1908 = relay.bitwise_and(call_1898.astype('int16'), relay.reshape(var_1904.astype('int16'), relay.shape_of(call_1898))) # shape=(11, 14, 5)
func_1888_call = mod.get_global_var('func_1888')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_1931 = relay.TupleGetItem(func_1888_call(), 0)
call_1932 = relay.TupleGetItem(func_1890_call(), 0)
func_1756_call = mod.get_global_var('func_1756')
func_1760_call = mutated_mod.get_global_var('func_1760')
var_1936 = relay.var("var_1936", dtype = "float32", shape = (336,))#candidate|1936|(336,)|var|float32
call_1935 = relay.TupleGetItem(func_1756_call(relay.reshape(var_1936.astype('float32'), [336,]), relay.reshape(call_1931.astype('float32'), [11, 14, 5]), ), 0)
call_1937 = relay.TupleGetItem(func_1760_call(relay.reshape(var_1936.astype('float32'), [336,]), relay.reshape(call_1931.astype('float32'), [11, 14, 5]), ), 0)
func_672_call = mod.get_global_var('func_672')
func_676_call = mutated_mod.get_global_var('func_676')
const_1970 = relay.const([-6,-9,-10,-5,6,1,10,-9,-1,9,4,-3,-2,2,-5,7,-7,6,9,-4,7,-1,9,9,-8,1,-6,10,1,3,-1,5,9,7,5,2,-9,8,-2,6,-7,-5,3,3,5,8,-8,-6,-6,-2,-6,-2,9,3,-1,1,-7,-3,2,-4,1,5,-5,-4,-3,2,3,4,-8,-3,-5,-4,-3,-3,-2,1,9,1,-4,4,3,7,-2,10,-8,-8,9,7,1,-4,7,4,-1,1,-2,-5,3,-1,-6,6,3,-9,5,4,-6,-7,-6,-8,-8,4,-3,4,-4,-10,7,-4,-9,-5,-9,-10,-9,-5,-2,2,1,1,-9,-10,4,-3,8,-3,8,-3,7,1,4,1,-10,-7,10,-7,-5,-2,-8,7,-2,-5,8,-9,-3,1,6,-3,-4,9,8,-5,-2,-9,-3,8,-9,-6,-5,2,-3,7,-4,8,-1,-3,1,-4,-6,5,1,5,-8,-7,-5,-1,3,-8,8,-8,-2,-2,1,-6,-8,8,-4,-7,3,-3,4,-7,-2,5,-2,3,-6,-5,-8,5,1,3,-8,8,-6,-2,-7,-1,-5,-2,-1,-8,-7,-3,-5,-1,2,4,6,-3,-4,-7,3,1,4,2,-8,10,3,-10,-2,7,-5,-5,-4,7,3,-1,10,2,-7,9,5,1,-5,-8,-4,-10,-9,-1,-5,-3,2,3,-7,-8,-9,2,-8,-4,5,-9,-1,9,-6,-3,9,-7,1,5,-5,4,1,10,2,2,5,6,2,6,-6,-9,4,-7,8,-2,-6,10,6,-7,-1,-6,2,-4,7,-2,-8,9,-9,-8,-10,-3,-1,-4,-1,3,-1,10,-3,8,6,-5,3,8,-2,-10,-9,9,-5,6,5,10,10,-9,-6,-5,7,9,-5,1,-5,2,-5,5,5,6,3,-7,-5,6,-3,6,-10,-1,3,-4,4,-6,8,-7,-3,4,8,-6,8,-6,2,3,6,5,-6,10,5,-9,7,8,10,3,3,-2,-3,2,-10,-7,10,8,3,6,-3,-10,4,10,10,-1,-7,4,1,5,-4,8,4,-10,3,4,-2,6,-4,9,2,-9,-4,8,2,7,-8,7,-10,-9,-2,10,-9,9,5,-9,9,7,-2,9,2,7,-10,2,-1,2,5,-7,-8,-10,-4,1,9,-7,5,-3,1,-7,-6,8,9,9,3,10,2,-4,1,2,-5,8,-4,-9,5,-5,-4,-6,-4,-8,-1,-8,-10,-3,-10,-10,-5,-7,1,3,3,-7,-2,1,-8,-3,-9,5,-3,-10,-3,-10,-9,7,-4,-8,-10,-3,7,-8,-2,5,-2,-3,-9,10,3,2,8,6,4,10,-10,-6,-6,2,-5,-1,9,2,9,10,3,-6,3,-4,7,-1,-6,3,-3,-1,-4,-5,-8,-1,-10,-1,-4,5,-10,-6,-2,3,6,-1,-3,-7,-5,-1,1,2,-6,-6,7,-10,2,-5,5,-6,5,9,-8,-6,1,7,-3,3,9,10,5,-4,-7,3,6,4,7,-9,2,-9,7,4,7,9,-1,4,10,2,9,-1,7,8,1,-8,-5,5,-4,-1,-8,-7,-1,2,-10,-9,2,-6,5,2,3,10,-6,9,-6,1,3,1,-10,3,9,-1,-2,-1,-2,5,-2,3,-2,10,-5,9,10,3,-5,9,10,7,8,-1,1,-8,-2,3,-3,1,-5,-7,-10,-4,-7,-9,5,-1,3,5,-1,-7,4,-7,4,-7,8,-5,-4,-3,5,2,-7,-5,4,-4,-5,-7,4,5,6,8,-6,2,5,-5,-1,-2,-9,-1,-7,9,8,10,-4,10,7,-3,5,6,-5,2,-9,4,-9,2,-10,9,-9,-1,-4,-2,-1,5,-2,-7,4,-1,-2,-1,-8,9,6,-7,7,-9,-9,1,7,7,8,8,-3,-7,4,10,-2,1,8,-4,-5,7,7,-5,5,6,8,-7,3,-8,3,8,-8,5,8,-1,6,9,6,-8,6,6,7,4,9,-6,1,-10,-6,5,6,-9,5,-6,1,-6,9,2,-7,-6,2,1,-10,2,-5,10,-4,6,6,-4,5,6,2,-9,-6,-7,9,-2,6,4,1,-5,-10,8,-2,-3,-2,10,-8,-5,6,-3,-8,3,-8,-7,1,-8,4,7,8,-4,10,6,-5,-2,-1,-5,7,2,4,-4,5,6,-8,7,6,8,-7,3,5,2,-10,6,-4,-3,-10,-5,-1,-4,5,-6,-5,6,1,6,5,-6,7,-2,-10,1,-6,-7,-7,-7,-6,-3,9,5,-7,10,2,-6,-7,10,-5,-9,7,-7,9,-9,7,6,-9,8,3,-9,3,4,8,-7,-6,4,-2,-10,-7,6,10,3,-4,-7,-10,-3,-6,5,2,-6,8,-4,5,5,-2,7,4,3,-3,-6,1,-6,-8,-10,2,-1,-8,-5,8,6,-1,-5,-2,-5,-1,8,10,-6,6,1,1,-2,-8,3,-9,9,1,6,-2,-10,10,2,5,-2,-5,-1,-6,7,-2,-1,9,-10,2,6,7,-7,-6,-10,-7,2,-5,8,7,-5,-8,-9,-4,9,-5,2,-3,-8,5,9,-10,4,5,-7,9,-1,-8,-4,-9,10,8,-5,-10,7,3,-9,-1,8,-7,10,7,-3,-4,-9,9,-7,3,5,7,1,10,-2,-7,6,-5,9,10,9,10,6,-9,-4,7,8,-1,-5,-2,-3,7,-2,8,6,-5,3,-3,5,-2,-6,8,2,-6,-2,3,-7,7,-5,-3,4,-8,-5,3,-4,-9,-3,-6,-6,-1,-3,4,-7,1,7,-4,6,-5,2,-3,3], dtype = "int32")#candidate|1970|(1056,)|const|int32
call_1969 = relay.TupleGetItem(func_672_call(relay.reshape(const_1970.astype('int32'), [11, 8, 12]), relay.reshape(const_1970.astype('int32'), [11, 8, 12]), ), 0)
call_1971 = relay.TupleGetItem(func_676_call(relay.reshape(const_1970.astype('int32'), [11, 8, 12]), relay.reshape(const_1970.astype('int32'), [11, 8, 12]), ), 0)
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_1975 = relay.TupleGetItem(func_1817_call(), 1)
call_1976 = relay.TupleGetItem(func_1818_call(), 1)
output = relay.Tuple([bop_1905,call_1931,call_1935,var_1936,call_1969,const_1970,call_1975,])
output2 = relay.Tuple([bop_1908,call_1932,call_1937,var_1936,call_1971,const_1970,call_1976,])
func_1981 = relay.Function([var_1904,var_1936,], output)
mod['func_1981'] = func_1981
mod = relay.transform.InferType()(mod)
mutated_mod['func_1981'] = func_1981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1981_call = mutated_mod.get_global_var('func_1981')
var_1983 = relay.var("var_1983", dtype = "float32", shape = (11, 14, 5))#candidate|1983|(11, 14, 5)|var|float32
var_1984 = relay.var("var_1984", dtype = "float32", shape = (336,))#candidate|1984|(336,)|var|float32
call_1982 = func_1981_call(var_1983,var_1984,)
output = call_1982
func_1985 = relay.Function([var_1983,var_1984,], output)
mutated_mod['func_1985'] = func_1985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_2004 = relay.TupleGetItem(func_1817_call(), 0)
call_2005 = relay.TupleGetItem(func_1818_call(), 0)
output = relay.Tuple([call_2004,])
output2 = relay.Tuple([call_2005,])
func_2043 = relay.Function([], output)
mod['func_2043'] = func_2043
mod = relay.transform.InferType()(mod)
output = func_2043()
func_2044 = relay.Function([], output)
mutated_mod['func_2044'] = func_2044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2064 = relay.TupleGetItem(func_2043_call(), 0)
call_2065 = relay.TupleGetItem(func_2044_call(), 0)
var_2073 = relay.var("var_2073", dtype = "float32", shape = (11, 14, 5))#candidate|2073|(11, 14, 5)|var|float32
bop_2074 = relay.floor_mod(call_2064.astype('float32'), relay.reshape(var_2073.astype('float32'), relay.shape_of(call_2064))) # shape=(11, 14, 5)
bop_2077 = relay.floor_mod(call_2065.astype('float32'), relay.reshape(var_2073.astype('float32'), relay.shape_of(call_2065))) # shape=(11, 14, 5)
output = bop_2074
output2 = bop_2077
func_2090 = relay.Function([var_2073,], output)
mod['func_2090'] = func_2090
mod = relay.transform.InferType()(mod)
var_2091 = relay.var("var_2091", dtype = "float32", shape = (11, 14, 5))#candidate|2091|(11, 14, 5)|var|float32
output = func_2090(var_2091)
func_2092 = relay.Function([var_2091], output)
mutated_mod['func_2092'] = func_2092
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2106 = relay.var("var_2106", dtype = "float64", shape = (1, 10, 2))#candidate|2106|(1, 10, 2)|var|float64
uop_2107 = relay.tan(var_2106.astype('float64')) # shape=(1, 10, 2)
output = uop_2107
output2 = uop_2107
func_2109 = relay.Function([var_2106,], output)
mod['func_2109'] = func_2109
mod = relay.transform.InferType()(mod)
mutated_mod['func_2109'] = func_2109
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2110 = relay.var("var_2110", dtype = "float64", shape = (1, 10, 2))#candidate|2110|(1, 10, 2)|var|float64
func_2109_call = mutated_mod.get_global_var('func_2109')
call_2111 = func_2109_call(var_2110)
output = call_2111
func_2112 = relay.Function([var_2110], output)
mutated_mod['func_2112'] = func_2112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_2130 = func_1716_call()
call_2131 = func_1716_call()
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_2133 = relay.TupleGetItem(func_1817_call(), 0)
call_2134 = relay.TupleGetItem(func_1818_call(), 0)
output = relay.Tuple([call_2130,call_2133,])
output2 = relay.Tuple([call_2131,call_2134,])
func_2147 = relay.Function([], output)
mod['func_2147'] = func_2147
mod = relay.transform.InferType()(mod)
mutated_mod['func_2147'] = func_2147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mutated_mod.get_global_var('func_2147')
call_2148 = func_2147_call()
output = call_2148
func_2149 = relay.Function([], output)
mutated_mod['func_2149'] = func_2149
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2169 = relay.var("var_2169", dtype = "float64", shape = (1, 16, 12))#candidate|2169|(1, 16, 12)|var|float64
uop_2170 = relay.erf(var_2169.astype('float64')) # shape=(1, 16, 12)
bop_2173 = relay.right_shift(uop_2170.astype('int16'), relay.reshape(var_2169.astype('int16'), relay.shape_of(uop_2170))) # shape=(1, 16, 12)
bop_2190 = relay.add(bop_2173.astype('int64'), relay.reshape(uop_2170.astype('int64'), relay.shape_of(bop_2173))) # shape=(1, 16, 12)
uop_2201 = relay.acos(var_2169.astype('float32')) # shape=(1, 16, 12)
output = relay.Tuple([bop_2190,uop_2201,])
output2 = relay.Tuple([bop_2190,uop_2201,])
func_2204 = relay.Function([var_2169,], output)
mod['func_2204'] = func_2204
mod = relay.transform.InferType()(mod)
var_2205 = relay.var("var_2205", dtype = "float64", shape = (1, 16, 12))#candidate|2205|(1, 16, 12)|var|float64
output = func_2204(var_2205)
func_2206 = relay.Function([var_2205], output)
mutated_mod['func_2206'] = func_2206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mod.get_global_var('func_2147')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_2273 = relay.TupleGetItem(func_2147_call(), 0)
call_2274 = relay.TupleGetItem(func_2149_call(), 0)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_2278 = func_1716_call()
call_2279 = func_1716_call()
func_1602_call = mod.get_global_var('func_1602')
func_1605_call = mutated_mod.get_global_var('func_1605')
var_2281 = relay.var("var_2281", dtype = "int8", shape = (56,))#candidate|2281|(56,)|var|int8
call_2280 = relay.TupleGetItem(func_1602_call(relay.reshape(var_2281.astype('int8'), [1, 7, 8])), 0)
call_2282 = relay.TupleGetItem(func_1605_call(relay.reshape(var_2281.astype('int8'), [1, 7, 8])), 0)
output = relay.Tuple([call_2273,call_2278,call_2280,var_2281,])
output2 = relay.Tuple([call_2274,call_2279,call_2282,var_2281,])
func_2288 = relay.Function([var_2281,], output)
mod['func_2288'] = func_2288
mod = relay.transform.InferType()(mod)
var_2289 = relay.var("var_2289", dtype = "int8", shape = (56,))#candidate|2289|(56,)|var|int8
output = func_2288(var_2289)
func_2290 = relay.Function([var_2289], output)
mutated_mod['func_2290'] = func_2290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mod.get_global_var('func_2147')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_2302 = relay.TupleGetItem(func_2147_call(), 0)
call_2303 = relay.TupleGetItem(func_2149_call(), 0)
func_1143_call = mod.get_global_var('func_1143')
func_1146_call = mutated_mod.get_global_var('func_1146')
var_2318 = relay.var("var_2318", dtype = "float32", shape = (288,))#candidate|2318|(288,)|var|float32
call_2317 = relay.TupleGetItem(func_1143_call(relay.reshape(var_2318.astype('float32'), [6, 16, 3])), 0)
call_2319 = relay.TupleGetItem(func_1146_call(relay.reshape(var_2318.astype('float32'), [6, 16, 3])), 0)
output = relay.Tuple([call_2302,call_2317,var_2318,])
output2 = relay.Tuple([call_2303,call_2319,var_2318,])
func_2328 = relay.Function([var_2318,], output)
mod['func_2328'] = func_2328
mod = relay.transform.InferType()(mod)
var_2329 = relay.var("var_2329", dtype = "float32", shape = (288,))#candidate|2329|(288,)|var|float32
output = func_2328(var_2329)
func_2330 = relay.Function([var_2329], output)
mutated_mod['func_2330'] = func_2330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mod.get_global_var('func_2147')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_2361 = relay.TupleGetItem(func_2147_call(), 1)
call_2362 = relay.TupleGetItem(func_2149_call(), 1)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2363 = relay.TupleGetItem(func_2043_call(), 0)
call_2364 = relay.TupleGetItem(func_2044_call(), 0)
output = relay.Tuple([call_2361,call_2363,])
output2 = relay.Tuple([call_2362,call_2364,])
func_2382 = relay.Function([], output)
mod['func_2382'] = func_2382
mod = relay.transform.InferType()(mod)
mutated_mod['func_2382'] = func_2382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2382_call = mutated_mod.get_global_var('func_2382')
call_2383 = func_2382_call()
output = call_2383
func_2384 = relay.Function([], output)
mutated_mod['func_2384'] = func_2384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mod.get_global_var('func_2147')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_2393 = relay.TupleGetItem(func_2147_call(), 0)
call_2394 = relay.TupleGetItem(func_2149_call(), 0)
var_2404 = relay.var("var_2404", dtype = "float32", shape = (11, 14, 5))#candidate|2404|(11, 14, 5)|var|float32
bop_2405 = relay.subtract(call_2393.astype('int64'), relay.reshape(var_2404.astype('int64'), relay.shape_of(call_2393))) # shape=(11, 14, 5)
bop_2408 = relay.subtract(call_2394.astype('int64'), relay.reshape(var_2404.astype('int64'), relay.shape_of(call_2394))) # shape=(11, 14, 5)
output = bop_2405
output2 = bop_2408
func_2410 = relay.Function([var_2404,], output)
mod['func_2410'] = func_2410
mod = relay.transform.InferType()(mod)
mutated_mod['func_2410'] = func_2410
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2411 = relay.var("var_2411", dtype = "float32", shape = (11, 14, 5))#candidate|2411|(11, 14, 5)|var|float32
func_2410_call = mutated_mod.get_global_var('func_2410')
call_2412 = func_2410_call(var_2411)
output = call_2412
func_2413 = relay.Function([var_2411], output)
mutated_mod['func_2413'] = func_2413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2382_call = mod.get_global_var('func_2382')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_2508 = relay.TupleGetItem(func_2382_call(), 1)
call_2509 = relay.TupleGetItem(func_2384_call(), 1)
output = call_2508
output2 = call_2509
func_2546 = relay.Function([], output)
mod['func_2546'] = func_2546
mod = relay.transform.InferType()(mod)
output = func_2546()
func_2547 = relay.Function([], output)
mutated_mod['func_2547'] = func_2547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_2566 = relay.TupleGetItem(func_1817_call(), 0)
call_2567 = relay.TupleGetItem(func_1818_call(), 0)
output = relay.Tuple([call_2566,])
output2 = relay.Tuple([call_2567,])
func_2598 = relay.Function([], output)
mod['func_2598'] = func_2598
mod = relay.transform.InferType()(mod)
mutated_mod['func_2598'] = func_2598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2598_call = mutated_mod.get_global_var('func_2598')
call_2599 = func_2598_call()
output = call_2599
func_2600 = relay.Function([], output)
mutated_mod['func_2600'] = func_2600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_2675 = relay.TupleGetItem(func_1817_call(), 1)
call_2676 = relay.TupleGetItem(func_1818_call(), 1)
func_1981_call = mod.get_global_var('func_1981')
func_1985_call = mutated_mod.get_global_var('func_1985')
const_2709 = relay.const([2.671558,8.362588,1.761582,-3.991065,4.418246,9.329844,3.532558,5.264773,0.800349,-5.162674,-8.913849,5.771803,4.608441,-5.612308,-6.368481,-6.599315,-3.226413,1.579707,9.608865,-4.659149,6.911627,-9.423208,9.311459,0.077193,9.459386,-2.220458,6.247401,-9.815827,5.751188,-3.225341,-6.132560,2.320699,-3.779476,-2.340346,5.699366,8.823499,-3.518481,3.956862,6.337038,-7.179922,9.709003,-0.991078,-4.234682,6.483871,8.215150,-0.832090,-6.584604,-3.507201,-6.687331,-2.929775,7.681621,3.472937,-2.480972,-3.284238,6.343523,-4.090906,4.321778,-4.874726,7.594361,6.871268,9.693658,3.985467,-7.030868,-9.746409,-8.489151,-4.450035,-8.871228,-9.938517,-7.680927,-9.123674,2.936339,-9.031286,9.664733,2.335827,5.575814,-7.593680,-7.939664,-5.372541,4.578274,9.772036,-6.266186,-5.693962,4.393048,9.604386,8.518067,-6.868438,-3.479800,7.159177,5.721911,4.490654,4.346866,3.054836,1.745195,-3.390077,-4.208790,-2.460108,3.883654,-2.058398,0.512327,2.210677,4.942955,-3.485264,-0.157076,-5.907597,-6.224041,-7.477254,2.227066,6.638499,-3.916923,4.998237,6.157925,0.146307,-6.790669,-5.872241,6.635565,-6.516718,4.886145,-5.589331,-8.468460,9.534550,-2.148758,9.145935,0.937817,-4.979997,-4.341366,-5.306848,-9.608295,0.541454,8.669356,-7.896301,9.601345,-0.621556,3.729832,-8.911770,4.158895,-4.319689,-3.342330,6.949987,-4.395705,1.436208,7.550786,3.975780,5.191336,0.404728,-3.479236,2.957439,-8.760200,-4.884351,-6.210009,-1.085743,-7.495109,-4.910837,-2.965818,-1.861271,1.407605,8.175879,2.689727,-2.346758,7.492703,-7.675925,-2.217101,9.415776,1.736568,-5.043651,4.464984,6.576730,-9.675143,-5.033862,7.025132,3.618806,-7.090717,3.491965,5.799027,-2.849432,6.573509,-9.228432,-4.479461,0.261448,2.700460,4.774146,-7.610356,-4.537669,-4.208720,2.895327,5.239957,9.354374,0.570361,-9.694409,-3.501048,-6.232549,5.906756,4.838789,-7.815948,1.441421,3.950892,-5.576553,6.105954,-2.463646,5.032883,8.881782,-4.003493,-9.145256,2.825303,2.766069,2.805205,-6.414827,-4.267974,-0.795896,-8.835019,2.036277,8.933269,2.060244,-9.241473,-1.708592,6.126581,9.552243,-9.929501,6.447940,-6.960906,-0.003503,-2.236147,-3.650999,-4.844783,-0.137147,-7.381404,-9.156329,3.401759,-8.128724,9.730024,-8.047119,-4.075019,5.731873,0.462873,-4.748216,9.579010,-9.135855,1.047709,-2.927850,9.083753,-8.495130,-7.246395,6.132757,-2.240131,-0.224881,7.397146,-1.517398,-8.386126,-2.837257,9.785705,2.082447,8.686949,-4.550434,-1.360532,3.447803,9.625674,5.863472,-5.872037,-5.012179,-3.911299,1.326537,3.797378,2.257282,6.931471,9.739016,-3.833426,1.732567,-1.216783,9.264299,-4.999392,9.800362,-2.024771,-4.206972,3.551280,-2.934776,8.191130,7.139425,7.955698,-3.849504,1.560934,4.304142,-6.714983,2.740155,1.243445,8.009402,7.966852,1.122830,2.726352,4.530748,-4.660026,-1.479446,4.345318,-0.946378,-0.431500,5.179481,4.907481,5.552775,1.167734,-0.181437,8.549907,-7.410587,-6.386622,3.927654,5.266386,2.593239,-7.504141,3.888972,9.744578,-7.698598,-3.456764,0.902467,2.417024,6.621663,-0.940354,4.188003,7.247168,-4.999688,8.174750,9.122163,-5.782974,6.035279,-5.902201,-6.368162,-6.295083,5.609706,-0.357527,-7.471252,-1.984974,-8.887051,-0.584364,-5.495801,-2.436258,6.706864,-5.262512,-9.760478,0.646339,6.861191], dtype = "float32")#candidate|2709|(336,)|const|float32
call_2708 = relay.TupleGetItem(func_1981_call(relay.reshape(call_2675.astype('float32'), [11, 14, 5]), relay.reshape(const_2709.astype('float32'), [336,]), ), 2)
call_2710 = relay.TupleGetItem(func_1985_call(relay.reshape(call_2675.astype('float32'), [11, 14, 5]), relay.reshape(const_2709.astype('float32'), [336,]), ), 2)
func_1602_call = mod.get_global_var('func_1602')
func_1605_call = mutated_mod.get_global_var('func_1605')
var_2737 = relay.var("var_2737", dtype = "int8", shape = (56,))#candidate|2737|(56,)|var|int8
call_2736 = relay.TupleGetItem(func_1602_call(relay.reshape(var_2737.astype('int8'), [1, 7, 8])), 0)
call_2738 = relay.TupleGetItem(func_1605_call(relay.reshape(var_2737.astype('int8'), [1, 7, 8])), 0)
bop_2739 = relay.multiply(call_2708.astype('uint32'), relay.reshape(const_2709.astype('uint32'), relay.shape_of(call_2708))) # shape=(7, 12, 4)
bop_2742 = relay.multiply(call_2710.astype('uint32'), relay.reshape(const_2709.astype('uint32'), relay.shape_of(call_2710))) # shape=(7, 12, 4)
output = relay.Tuple([call_2675,call_2736,var_2737,bop_2739,])
output2 = relay.Tuple([call_2676,call_2738,var_2737,bop_2742,])
func_2745 = relay.Function([var_2737,], output)
mod['func_2745'] = func_2745
mod = relay.transform.InferType()(mod)
var_2746 = relay.var("var_2746", dtype = "int8", shape = (56,))#candidate|2746|(56,)|var|int8
output = func_2745(var_2746)
func_2747 = relay.Function([var_2746], output)
mutated_mod['func_2747'] = func_2747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2598_call = mod.get_global_var('func_2598')
func_2600_call = mutated_mod.get_global_var('func_2600')
call_2763 = relay.TupleGetItem(func_2598_call(), 0)
call_2764 = relay.TupleGetItem(func_2600_call(), 0)
func_1602_call = mod.get_global_var('func_1602')
func_1605_call = mutated_mod.get_global_var('func_1605')
var_2772 = relay.var("var_2772", dtype = "int8", shape = (56,))#candidate|2772|(56,)|var|int8
call_2771 = relay.TupleGetItem(func_1602_call(relay.reshape(var_2772.astype('int8'), [1, 7, 8])), 0)
call_2773 = relay.TupleGetItem(func_1605_call(relay.reshape(var_2772.astype('int8'), [1, 7, 8])), 0)
uop_2778 = relay.acosh(call_2771.astype('float64')) # shape=(1, 7, 8)
uop_2780 = relay.acosh(call_2773.astype('float64')) # shape=(1, 7, 8)
func_2288_call = mod.get_global_var('func_2288')
func_2290_call = mutated_mod.get_global_var('func_2290')
call_2785 = relay.TupleGetItem(func_2288_call(relay.reshape(var_2772.astype('int8'), [56,])), 1)
call_2786 = relay.TupleGetItem(func_2290_call(relay.reshape(var_2772.astype('int8'), [56,])), 1)
func_2410_call = mod.get_global_var('func_2410')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_2796 = func_2410_call(relay.reshape(call_2763.astype('float32'), [11, 14, 5]))
call_2797 = func_2410_call(relay.reshape(call_2763.astype('float32'), [11, 14, 5]))
func_1756_call = mod.get_global_var('func_1756')
func_1760_call = mutated_mod.get_global_var('func_1760')
var_2802 = relay.var("var_2802", dtype = "float32", shape = (168, 2))#candidate|2802|(168, 2)|var|float32
call_2801 = relay.TupleGetItem(func_1756_call(relay.reshape(var_2802.astype('float32'), [336,]), relay.reshape(call_2796.astype('float32'), [11, 14, 5]), ), 0)
call_2803 = relay.TupleGetItem(func_1760_call(relay.reshape(var_2802.astype('float32'), [336,]), relay.reshape(call_2796.astype('float32'), [11, 14, 5]), ), 0)
var_2820 = relay.var("var_2820", dtype = "float64", shape = (11, 7, 8))#candidate|2820|(11, 7, 8)|var|float64
bop_2821 = relay.floor_mod(uop_2778.astype('float32'), var_2820.astype('float32')) # shape=(11, 7, 8)
bop_2824 = relay.floor_mod(uop_2780.astype('float32'), var_2820.astype('float32')) # shape=(11, 7, 8)
uop_2825 = relay.tan(call_2771.astype('float32')) # shape=(1, 7, 8)
uop_2827 = relay.tan(call_2773.astype('float32')) # shape=(1, 7, 8)
uop_2832 = relay.sin(var_2820.astype('float64')) # shape=(11, 7, 8)
func_2382_call = mod.get_global_var('func_2382')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_2838 = relay.TupleGetItem(func_2382_call(), 1)
call_2839 = relay.TupleGetItem(func_2384_call(), 1)
output = relay.Tuple([call_2763,var_2772,call_2785,call_2796,call_2801,var_2802,bop_2821,uop_2825,uop_2832,call_2838,])
output2 = relay.Tuple([call_2764,var_2772,call_2786,call_2797,call_2803,var_2802,bop_2824,uop_2827,uop_2832,call_2839,])
func_2851 = relay.Function([var_2772,var_2802,var_2820,], output)
mod['func_2851'] = func_2851
mod = relay.transform.InferType()(mod)
var_2852 = relay.var("var_2852", dtype = "int8", shape = (56,))#candidate|2852|(56,)|var|int8
var_2853 = relay.var("var_2853", dtype = "float32", shape = (168, 2))#candidate|2853|(168, 2)|var|float32
var_2854 = relay.var("var_2854", dtype = "float64", shape = (11, 7, 8))#candidate|2854|(11, 7, 8)|var|float64
output = func_2851(var_2852,var_2853,var_2854,)
func_2855 = relay.Function([var_2852,var_2853,var_2854,], output)
mutated_mod['func_2855'] = func_2855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mod.get_global_var('func_2147')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_2873 = relay.TupleGetItem(func_2147_call(), 0)
call_2874 = relay.TupleGetItem(func_2149_call(), 0)
func_1143_call = mod.get_global_var('func_1143')
func_1146_call = mutated_mod.get_global_var('func_1146')
const_2880 = relay.const([8.448589,7.072741,-9.959112,-1.863055,0.898541,4.299980,-7.832549,-0.926412,-0.264599,4.565216,-4.150277,-6.758082,-4.702387,1.353583,9.106449,-9.303001,-2.652419,7.073820,-4.412758,-2.748415,1.894753,-4.286358,3.373002,-4.646263,-6.279954,-0.815745,-4.122909,-3.758706,-6.193907,4.353993,7.012201,-4.566057,2.621183,-7.379237,1.913048,-0.896471,-4.686637,-5.712211,2.617237,2.463750,1.987870,9.641649,0.805033,-2.428347,3.761414,0.634010,9.539113,-5.395973,2.638130,-9.706928,6.696549,7.550078,7.875297,8.197386,-5.343191,-2.725603,4.128738,0.613591,4.467947,-5.395243,4.354592,2.746209,8.920376,-5.058087,8.778449,5.013360,9.408103,-3.983053,7.230476,7.885686,8.811805,8.640795,2.537476,2.719048,-5.680948,2.953983,0.348911,-7.610744,7.684213,1.143809,4.784835,3.274554,8.182524,6.130172,-4.451706,-1.326995,-2.073864,-8.230911,-8.988678,-0.333056,9.561922,8.637326,8.922845,5.272630,-8.254511,7.419527,2.321490,-3.895121,-1.960383,8.055363,-6.782348,-1.342302,8.762538,4.160148,-4.673176,-3.070473,1.728975,-0.990579,9.163084,5.596438,-2.294603,2.909467,-9.817767,-2.655779,3.026812,9.223509,1.037032,-8.000266,-5.094817,4.392142,-1.154827,-0.892071,5.137945,-8.089982,-6.092010,-3.409181,-1.356604,-4.030824,6.845356,8.711522,9.023181,-5.395546,4.634648,0.470354,-6.321150,-6.449595,8.421628,8.337532,-2.299217,6.130001,2.056276,1.664025,-9.903388,-2.580592,3.307678,-4.792705,-8.991303,4.874337,-5.948170,7.416259,3.660428,7.200067,-0.867418,1.370007,-7.788778,5.815410,-7.921028,2.426953,9.846504,-0.531331,2.939330,2.835998,-1.978914,0.701437,6.085630,4.817514,4.404637,2.775572,1.088804,-7.125333,-2.164501,-9.136212,-7.109472,1.452088,0.847395,-4.602578,-1.014650,5.160955,3.933194,2.928100,5.888957,0.555174,7.990734,7.009806,-0.925911,-5.214323,0.488288,8.509945,-6.751679,1.903210,4.241263,3.030144,1.010800,-9.448689,3.299858,-6.471985,-6.186174,3.864320,-5.992542,9.840824,-7.675838,2.953238,-9.024955,-4.099041,0.751735,-9.122689,0.020341,4.256034,-4.354561,3.696864,3.084415,3.287640,-6.144167,-6.781631,7.507210,2.269964,7.295150,6.402406,8.802983,6.934472,-7.961353,3.016443,1.980977,-6.427196,-9.618256,4.929395,9.224156,-4.854786,-9.929304,6.576134,-3.149932,2.683972,9.049225,4.513077,-1.905743,-5.402395,-5.750196,0.625065,-1.914918,-3.464184,2.705093,-7.543314,-3.924820,-9.939067,4.926034,-7.987042,-9.309826,-7.659658,-2.185073,5.975134,-4.849436,3.965986,9.883457,-8.172144,8.886325,0.998014,-5.330063,3.934151,-8.063583,9.392706,2.421759,9.425741,-5.049632,-5.546029,3.878345,2.109968,0.607889,-7.641660,8.408782,-6.947612,0.324101,-9.727075,2.691442,-1.533951,3.502769,-9.663629,3.552338,9.504365,1.297552,4.335656,8.055725,-4.861184,3.923877,9.879761,2.128581,1.544165,3.927754,-5.448580], dtype = "float32")#candidate|2880|(288,)|const|float32
call_2879 = relay.TupleGetItem(func_1143_call(relay.reshape(const_2880.astype('float32'), [6, 16, 3])), 0)
call_2881 = relay.TupleGetItem(func_1146_call(relay.reshape(const_2880.astype('float32'), [6, 16, 3])), 0)
func_1981_call = mod.get_global_var('func_1981')
func_1985_call = mutated_mod.get_global_var('func_1985')
var_2892 = relay.var("var_2892", dtype = "float32", shape = (336,))#candidate|2892|(336,)|var|float32
call_2891 = relay.TupleGetItem(func_1981_call(relay.reshape(call_2873.astype('float32'), [11, 14, 5]), relay.reshape(var_2892.astype('float32'), [336,]), ), 0)
call_2893 = relay.TupleGetItem(func_1985_call(relay.reshape(call_2873.astype('float32'), [11, 14, 5]), relay.reshape(var_2892.astype('float32'), [336,]), ), 0)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
var_2896 = relay.var("var_2896", dtype = "int8", shape = (14, 4))#candidate|2896|(14, 4)|var|int8
call_2895 = relay.TupleGetItem(func_2745_call(relay.reshape(var_2896.astype('int8'), [56,])), 3)
call_2897 = relay.TupleGetItem(func_2747_call(relay.reshape(var_2896.astype('int8'), [56,])), 3)
uop_2914 = relay.tan(call_2873.astype('float64')) # shape=(11, 14, 5)
uop_2916 = relay.tan(call_2874.astype('float64')) # shape=(11, 14, 5)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
const_2942 = relay.const([-0.394333,-7.842178,-7.385082,-1.196674,0.293017,-6.902895,-9.038783,-4.812906,-5.400814,8.676812,-6.199892,5.178337,-9.127012,-5.326371,-2.234377,-1.334061,-0.061132,2.108154,8.211649,-1.397739,-9.036805,4.513176,-8.867717,-2.214000,-5.723747,7.819456,6.360669,3.045567,-7.861326,7.123215,7.138098,1.638637,-8.595749,-6.718767,-1.500703,-7.335955,3.636865,-5.658910,0.293279,4.945356,-9.972310,4.121877,9.511505,4.139785,-9.191230,-3.503204,-1.376075,0.533040,-6.136343,-5.155936,-4.251396,6.218989,0.356752,-0.366727,2.458672,-4.104490,-1.207102,6.883281,-1.347716,2.761747,0.146073,-5.062164,6.778636,-7.158940,-6.922792,5.989480,4.572623,-1.783199,-8.705021,9.390432,-2.965576,2.091244,9.685277,-0.687016,9.519732,-5.144176,4.395180,4.413726,5.210062,4.296616,-3.808331,-7.979913,4.435909,-3.371667,4.978155,1.026364,6.950173,-4.614372,5.898623,-1.502269,-0.086429,4.369011,-5.750400,5.921470,-5.807352,9.348094,8.345864,-4.134026,-1.103721,-6.726788,1.048808,-6.162242,-2.589543,8.130146,8.121421,-7.414658,1.510798,-2.714157,-1.129947,9.469487,-8.248949,-5.560619,-1.577250,-3.120999,6.887681,0.192632,2.214221,-5.873432,-9.248149,4.954149,9.214321,-9.540599,-2.183219,-3.292796,-0.211123,0.137836,-9.620213,-4.135105,2.396769,-5.588909,0.428587,8.635990,2.083757,-7.510128,0.048466,7.612695,0.038707,5.444508,-0.103802,1.392067,0.301614,4.098000,-6.703042,4.278619,4.081424,-9.496976,8.654309,2.211802,2.390783,-0.404573,7.877093,-2.538784,7.210062,-5.770927,6.030683,-8.131695,6.017203,4.013713,8.206560,9.148138,-1.779954,8.624989,3.579270,-1.820869,-0.065798,2.501277,-8.958501,7.884696,-7.578508,-1.447327,0.620242,-6.324975,-8.907707,-1.335771,-6.347888,-5.380351,8.313533,-7.322052,-3.474305,-6.000501,-7.393409,7.497647,6.260211,-4.434809,-7.988002,0.138880,-2.578843,-0.450380,7.910084,-9.064777,-5.619704,-6.569256], dtype = "float64")#candidate|2942|(192,)|const|float64
call_2941 = relay.TupleGetItem(func_2204_call(relay.reshape(const_2942.astype('float64'), [1, 16, 12])), 1)
call_2943 = relay.TupleGetItem(func_2206_call(relay.reshape(const_2942.astype('float64'), [1, 16, 12])), 1)
output = relay.Tuple([call_2879,const_2880,call_2891,var_2892,call_2895,var_2896,uop_2914,call_2941,const_2942,])
output2 = relay.Tuple([call_2881,const_2880,call_2893,var_2892,call_2897,var_2896,uop_2916,call_2943,const_2942,])
func_2950 = relay.Function([var_2892,var_2896,], output)
mod['func_2950'] = func_2950
mod = relay.transform.InferType()(mod)
var_2951 = relay.var("var_2951", dtype = "float32", shape = (336,))#candidate|2951|(336,)|var|float32
var_2952 = relay.var("var_2952", dtype = "int8", shape = (14, 4))#candidate|2952|(14, 4)|var|int8
output = func_2950(var_2951,var_2952,)
func_2953 = relay.Function([var_2951,var_2952,], output)
mutated_mod['func_2953'] = func_2953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2996 = relay.TupleGetItem(func_2043_call(), 0)
call_2997 = relay.TupleGetItem(func_2044_call(), 0)
func_2288_call = mod.get_global_var('func_2288')
func_2290_call = mutated_mod.get_global_var('func_2290')
const_3004 = relay.const([5,8,4,7,1,9,3,10,6,3,4,-7,7,-1,-1,2,10,-6,-10,-6,-10,-6,4,8,-6,8,-2,-7,4,-7,-4,-3,-1,-9,-1,-1,10,5,5,-8,8,-1,2,1,-3,2,-7,2,-1,8,5,-6,1,1,-7,-9], dtype = "int8")#candidate|3004|(56,)|const|int8
call_3003 = relay.TupleGetItem(func_2288_call(relay.reshape(const_3004.astype('int8'), [56,])), 0)
call_3005 = relay.TupleGetItem(func_2290_call(relay.reshape(const_3004.astype('int8'), [56,])), 0)
func_1602_call = mod.get_global_var('func_1602')
func_1605_call = mutated_mod.get_global_var('func_1605')
call_3017 = relay.TupleGetItem(func_1602_call(relay.reshape(const_3004.astype('int8'), [1, 7, 8])), 1)
call_3018 = relay.TupleGetItem(func_1605_call(relay.reshape(const_3004.astype('int8'), [1, 7, 8])), 1)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
call_3029 = relay.TupleGetItem(func_2745_call(relay.reshape(const_3004.astype('int8'), [56,])), 3)
call_3030 = relay.TupleGetItem(func_2747_call(relay.reshape(const_3004.astype('int8'), [56,])), 3)
output = relay.Tuple([call_2996,call_3003,const_3004,call_3017,call_3029,])
output2 = relay.Tuple([call_2997,call_3005,const_3004,call_3018,call_3030,])
func_3034 = relay.Function([], output)
mod['func_3034'] = func_3034
mod = relay.transform.InferType()(mod)
output = func_3034()
func_3035 = relay.Function([], output)
mutated_mod['func_3035'] = func_3035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2382_call = mod.get_global_var('func_2382')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_3105 = relay.TupleGetItem(func_2382_call(), 0)
call_3106 = relay.TupleGetItem(func_2384_call(), 0)
func_2109_call = mod.get_global_var('func_2109')
func_2112_call = mutated_mod.get_global_var('func_2112')
const_3121 = relay.const([9.391037,-1.480880,6.238760,-7.963480,7.773050,-9.117495,7.070305,3.257469,-7.689280,8.757447,-2.273452,6.177378,7.760914,3.357247,2.616962,-6.567165,8.197545,1.573404,-0.781179,-3.514270], dtype = "float64")#candidate|3121|(20,)|const|float64
call_3120 = func_2109_call(relay.reshape(const_3121.astype('float64'), [1, 10, 2]))
call_3122 = func_2109_call(relay.reshape(const_3121.astype('float64'), [1, 10, 2]))
output = relay.Tuple([call_3105,call_3120,const_3121,])
output2 = relay.Tuple([call_3106,call_3122,const_3121,])
func_3123 = relay.Function([], output)
mod['func_3123'] = func_3123
mod = relay.transform.InferType()(mod)
output = func_3123()
func_3124 = relay.Function([], output)
mutated_mod['func_3124'] = func_3124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2382_call = mod.get_global_var('func_2382')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_3154 = relay.TupleGetItem(func_2382_call(), 1)
call_3155 = relay.TupleGetItem(func_2384_call(), 1)
output = call_3154
output2 = call_3155
func_3160 = relay.Function([], output)
mod['func_3160'] = func_3160
mod = relay.transform.InferType()(mod)
output = func_3160()
func_3161 = relay.Function([], output)
mutated_mod['func_3161'] = func_3161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3034_call = mod.get_global_var('func_3034')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_3226 = relay.TupleGetItem(func_3034_call(), 2)
call_3227 = relay.TupleGetItem(func_3035_call(), 2)
func_978_call = mod.get_global_var('func_978')
func_981_call = mutated_mod.get_global_var('func_981')
const_3231 = relay.const([[-0.329247,-2.641285,0.407632,7.211393,8.894614,-1.658870,1.540370,-3.635667,7.361654,-5.907155,1.171675,2.156155,6.821073,-9.735883,-7.133585,4.318593,3.156077,-4.477957,-5.394567,-9.313663,-0.979834,-0.888406,6.249882,7.963849,-9.813789,-8.869380,-0.160799,-0.150644,-6.621722,5.916311,-2.573335,8.178991,-6.050970,9.334366,-4.874994,7.462883,-7.138989,-5.127078,-0.680443,-5.362617,3.989028,-6.715659,-7.202416,-1.480577,9.259101,8.025808,-8.911966,7.604201,-9.801268,4.416671,5.860573,-4.571581,5.067561,8.279259,-9.198655,-4.456968,-1.706195,5.342540,-6.290510,-8.547738,-6.187386,7.194695,-3.703658,3.619253,0.694220,2.683455,6.468328,-0.332606,-9.120231,-1.492249,-5.995526,6.593154],[-0.656711,4.328175,-1.521222,-6.345932,-4.996457,1.849124,8.152517,9.359652,0.205950,1.387097,-7.325855,3.487442,2.726633,9.589496,7.812754,-5.365232,-7.644533,-3.151554,5.828192,8.824002,-2.813119,3.075225,5.118615,3.010563,8.345452,-9.806579,-1.613238,8.273721,0.853232,9.625904,8.657482,-4.621773,-8.121070,-8.715118,-3.300145,7.937585,-8.765518,-2.078804,9.430734,-6.872650,-0.640333,6.414937,6.381462,-9.383059,6.022232,1.035387,6.481174,-7.847255,-5.501660,-2.449768,-2.595211,5.174586,-3.739757,5.680538,1.921377,-2.181977,-4.093353,1.995319,-9.062658,-8.304927,7.166142,-4.329237,-4.666793,-5.271145,0.991098,5.444575,-0.274621,-3.346918,-7.082963,5.051130,-3.720770,1.610330]], dtype = "float64")#candidate|3231|(2, 72)|const|float64
call_3230 = relay.TupleGetItem(func_978_call(relay.reshape(const_3231.astype('float64'), [3, 4, 12])), 0)
call_3232 = relay.TupleGetItem(func_981_call(relay.reshape(const_3231.astype('float64'), [3, 4, 12])), 0)
func_2109_call = mod.get_global_var('func_2109')
func_2112_call = mutated_mod.get_global_var('func_2112')
var_3234 = relay.var("var_3234", dtype = "float64", shape = (20,))#candidate|3234|(20,)|var|float64
call_3233 = func_2109_call(relay.reshape(var_3234.astype('float64'), [1, 10, 2]))
call_3235 = func_2109_call(relay.reshape(var_3234.astype('float64'), [1, 10, 2]))
bop_3239 = relay.add(call_3233.astype('uint16'), relay.reshape(var_3234.astype('uint16'), relay.shape_of(call_3233))) # shape=(1, 10, 2)
bop_3242 = relay.add(call_3235.astype('uint16'), relay.reshape(var_3234.astype('uint16'), relay.shape_of(call_3235))) # shape=(1, 10, 2)
func_2851_call = mod.get_global_var('func_2851')
func_2855_call = mutated_mod.get_global_var('func_2855')
const_3266 = relay.const([-0.281067,-9.456478,-3.994871,3.745000,-6.629694,5.025037,-5.600461,-0.690460,-7.077985,9.902593,0.670385,8.402163,3.017647,8.943709,2.948140,-0.815186,2.900012,-5.180496,-7.555387,-8.632769,6.776368,7.840632,8.029417,-3.843642,-7.769626,1.836623,-8.307783,-2.692252,4.744425,-2.792657,-6.124743,-3.995786,6.412785,6.524631,-5.471886,7.942985,4.372952,9.481231,-7.965207,-5.813888,6.650503,-7.764499,-8.190089,1.968456,-4.629736,1.245033,-3.971176,6.454849,-0.406173,8.689770,-6.208321,5.257193,-1.363386,8.165508,-6.154029,5.465330,6.569382,3.170770,-8.037861,7.319356,0.207858,4.522329,-5.143001,7.554939,3.541221,5.376999,1.174509,2.429861,3.096861,3.090811,5.999158,1.436075,-0.821819,-5.110591,8.187555,-2.072805,-6.542821,0.341634,-7.528430,-8.340911,4.099888,3.873377,-6.680735,-1.194803,0.563202,1.989434,-0.210241,4.639902,-2.705913,0.302661,4.429487,-7.947580,4.655596,-2.648369,-5.190103,7.648263,-4.006210,3.399324,-8.621774,-3.568749,9.509314,-2.414901,-8.759843,-4.770839,6.032589,4.143253,2.820264,4.030699,0.303880,-1.342837,-4.618850,5.468007,6.844998,1.608550,7.248962,9.325426,1.904451,-3.851319,-6.805723,-2.704527,6.976584,-7.908463,4.780699,5.890268,-9.633116,6.097444,-4.507853,6.168596,5.215896,2.024985,9.178860,6.481906,-5.629864,-6.400816,-1.420423,-7.481186,-2.574758,0.699699,-4.226806,-3.686311,-0.785733,6.213031,7.042953,-1.128805,7.903415,4.392215,6.913288,-3.852763,-7.676495,-7.691559,5.463952,-4.875516,8.198447,-5.715365,0.296535,-0.159190,-1.010746,-1.121904,0.461370,-3.600019,-2.906932,6.373356,-7.572612,0.370417,-5.941282,6.423828,-6.655225,-5.451886,6.418237,-8.492833,9.533231,2.958773,-0.370483,2.093902,-5.682384,2.802184,7.221007,-0.638763,-2.992045,4.660832,9.569382,-1.660704,-0.245275,-5.772664,3.335202,-0.536945,1.024736,-3.818435,6.507840,7.201963,7.736139,-7.058061,3.688234,-2.959948,-8.322538,2.306426,7.531345,-6.615497,-0.851521,9.240605,3.631077,-7.972875,3.942456,-5.330706,8.137507,8.867948,-9.803883,8.291143,-8.210893,6.858905,2.787044,8.104429,2.615297,4.838168,-2.889715,9.594762,-0.930556,-0.001182,4.222347,8.697767,9.759889,0.087280,-2.906837,5.316220,2.787098,-0.011078,7.531996,1.735429,5.389657,-9.341122,3.396410,6.569551,-4.725840,-9.967484,-0.826923,-0.613005,-3.179494,-7.183812,-8.345707,6.827237,-4.965869,8.724237,2.359762,-7.857138,6.811152,-3.555861,9.207671,-9.486349,-2.790819,1.355933,-2.613401,-4.639054,6.051994,-9.985056,-6.631765,1.447412,6.329271,7.008224,4.480969,3.519428,-3.091029,-1.776241,5.429993,8.116866,2.004003,-3.792384,-0.215031,-1.185760,0.702285,-5.343436,-2.814232,5.809079,-0.827421,5.770170,-5.483538,-4.095986,-7.087826,-6.965743,0.889255,7.882678,-9.341169,9.912952,-7.184704,1.461932,-8.192756,-2.988156,7.720092,-0.090416,-2.929296,-6.930776,-9.961341,1.816953,3.544593,-2.124267,-9.443558,2.529858,5.445415,8.673920,-9.204772,-7.577856,-1.824935,4.719432,-0.433319,0.870050,3.770251,1.338961,-9.526972,2.285682,1.267648,2.279173,4.633258,-2.085662,5.816717,5.437130,-3.657090,-7.318230,-6.691588,1.023910,6.161420,6.141486,-1.901726,-5.083794,5.690145,-9.133089,3.263886,-5.054336,-5.038643,4.732797,3.061885,8.202388,-0.218693,-4.210509,9.351725,7.153445,7.296097,-2.411727], dtype = "float32")#candidate|3266|(336,)|const|float32
var_3267 = relay.var("var_3267", dtype = "float64", shape = (7, 88))#candidate|3267|(7, 88)|var|float64
call_3265 = relay.TupleGetItem(func_2851_call(relay.reshape(call_3226.astype('int8'), [56,]), relay.reshape(const_3266.astype('float32'), [168, 2]), relay.reshape(var_3267.astype('float64'), [11, 7, 8]), ), 8)
call_3268 = relay.TupleGetItem(func_2855_call(relay.reshape(call_3226.astype('int8'), [56,]), relay.reshape(const_3266.astype('float32'), [168, 2]), relay.reshape(var_3267.astype('float64'), [11, 7, 8]), ), 8)
func_2546_call = mod.get_global_var('func_2546')
func_2547_call = mutated_mod.get_global_var('func_2547')
call_3270 = func_2546_call()
call_3271 = func_2546_call()
uop_3281 = relay.sigmoid(var_3267.astype('float64')) # shape=(7, 88)
uop_3286 = relay.sinh(uop_3281.astype('float32')) # shape=(7, 88)
func_672_call = mod.get_global_var('func_672')
func_676_call = mutated_mod.get_global_var('func_676')
var_3299 = relay.var("var_3299", dtype = "int32", shape = (1056,))#candidate|3299|(1056,)|var|int32
call_3298 = relay.TupleGetItem(func_672_call(relay.reshape(var_3299.astype('int32'), [11, 8, 12]), relay.reshape(var_3299.astype('int32'), [11, 8, 12]), ), 1)
call_3300 = relay.TupleGetItem(func_676_call(relay.reshape(var_3299.astype('int32'), [11, 8, 12]), relay.reshape(var_3299.astype('int32'), [11, 8, 12]), ), 1)
output = relay.Tuple([call_3226,call_3230,const_3231,bop_3239,call_3265,const_3266,call_3270,uop_3286,call_3298,var_3299,])
output2 = relay.Tuple([call_3227,call_3232,const_3231,bop_3242,call_3268,const_3266,call_3271,uop_3286,call_3300,var_3299,])
func_3301 = relay.Function([var_3234,var_3267,var_3299,], output)
mod['func_3301'] = func_3301
mod = relay.transform.InferType()(mod)
var_3302 = relay.var("var_3302", dtype = "float64", shape = (20,))#candidate|3302|(20,)|var|float64
var_3303 = relay.var("var_3303", dtype = "float64", shape = (7, 88))#candidate|3303|(7, 88)|var|float64
var_3304 = relay.var("var_3304", dtype = "int32", shape = (1056,))#candidate|3304|(1056,)|var|int32
output = func_3301(var_3302,var_3303,var_3304,)
func_3305 = relay.Function([var_3302,var_3303,var_3304,], output)
mutated_mod['func_3305'] = func_3305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_3494 = relay.TupleGetItem(func_2043_call(), 0)
call_3495 = relay.TupleGetItem(func_2044_call(), 0)
func_2410_call = mod.get_global_var('func_2410')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_3518 = func_2410_call(relay.reshape(call_3494.astype('float32'), [11, 14, 5]))
call_3519 = func_2410_call(relay.reshape(call_3494.astype('float32'), [11, 14, 5]))
output = relay.Tuple([call_3494,call_3518,])
output2 = relay.Tuple([call_3495,call_3519,])
func_3523 = relay.Function([], output)
mod['func_3523'] = func_3523
mod = relay.transform.InferType()(mod)
mutated_mod['func_3523'] = func_3523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3523_call = mutated_mod.get_global_var('func_3523')
call_3524 = func_3523_call()
output = call_3524
func_3525 = relay.Function([], output)
mutated_mod['func_3525'] = func_3525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3570 = relay.var("var_3570", dtype = "uint32", shape = (2, 10, 11))#candidate|3570|(2, 10, 11)|var|uint32
var_3571 = relay.var("var_3571", dtype = "uint32", shape = (2, 10, 11))#candidate|3571|(2, 10, 11)|var|uint32
bop_3572 = relay.logical_xor(var_3570.astype('uint32'), relay.reshape(var_3571.astype('uint32'), relay.shape_of(var_3570))) # shape=(2, 10, 11)
func_1602_call = mod.get_global_var('func_1602')
func_1605_call = mutated_mod.get_global_var('func_1605')
var_3576 = relay.var("var_3576", dtype = "int8", shape = (56,))#candidate|3576|(56,)|var|int8
call_3575 = relay.TupleGetItem(func_1602_call(relay.reshape(var_3576.astype('int8'), [1, 7, 8])), 0)
call_3577 = relay.TupleGetItem(func_1605_call(relay.reshape(var_3576.astype('int8'), [1, 7, 8])), 0)
var_3580 = relay.var("var_3580", dtype = "uint32", shape = (2, 10, 11))#candidate|3580|(2, 10, 11)|var|uint32
bop_3581 = relay.floor_divide(var_3570.astype('float64'), relay.reshape(var_3580.astype('float64'), relay.shape_of(var_3570))) # shape=(2, 10, 11)
bop_3601 = relay.logical_or(bop_3572.astype('bool'), relay.reshape(var_3570.astype('bool'), relay.shape_of(bop_3572))) # shape=(2, 10, 11)
output = relay.Tuple([call_3575,var_3576,bop_3581,bop_3601,])
output2 = relay.Tuple([call_3577,var_3576,bop_3581,bop_3601,])
func_3606 = relay.Function([var_3570,var_3571,var_3576,var_3580,], output)
mod['func_3606'] = func_3606
mod = relay.transform.InferType()(mod)
var_3607 = relay.var("var_3607", dtype = "uint32", shape = (2, 10, 11))#candidate|3607|(2, 10, 11)|var|uint32
var_3608 = relay.var("var_3608", dtype = "uint32", shape = (2, 10, 11))#candidate|3608|(2, 10, 11)|var|uint32
var_3609 = relay.var("var_3609", dtype = "int8", shape = (56,))#candidate|3609|(56,)|var|int8
var_3610 = relay.var("var_3610", dtype = "uint32", shape = (2, 10, 11))#candidate|3610|(2, 10, 11)|var|uint32
output = func_3606(var_3607,var_3608,var_3609,var_3610,)
func_3611 = relay.Function([var_3607,var_3608,var_3609,var_3610,], output)
mutated_mod['func_3611'] = func_3611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_3679 = relay.TupleGetItem(func_3123_call(), 2)
call_3680 = relay.TupleGetItem(func_3124_call(), 2)
output = call_3679
output2 = call_3680
func_3720 = relay.Function([], output)
mod['func_3720'] = func_3720
mod = relay.transform.InferType()(mod)
output = func_3720()
func_3721 = relay.Function([], output)
mutated_mod['func_3721'] = func_3721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mod.get_global_var('func_2147')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_3758 = relay.TupleGetItem(func_2147_call(), 1)
call_3759 = relay.TupleGetItem(func_2149_call(), 1)
func_2851_call = mod.get_global_var('func_2851')
func_2855_call = mutated_mod.get_global_var('func_2855')
const_3764 = relay.const([1,2,-9,-3,5,5,-10,6,4,6,-2,4,10,-1,8,-9,-8,-3,7,-3,8,6,2,3,-3,-5,1,-5,5,-9,-1,-4,-1,-4,-4,3,-5,-9,2,-3,2,-3,7,6,-5,-5,-5,-3,-5,-7,4,-3,10,7,6,8], dtype = "int8")#candidate|3764|(56,)|const|int8
var_3765 = relay.var("var_3765", dtype = "float32", shape = (2, 168))#candidate|3765|(2, 168)|var|float32
var_3766 = relay.var("var_3766", dtype = "float64", shape = (616,))#candidate|3766|(616,)|var|float64
call_3763 = relay.TupleGetItem(func_2851_call(relay.reshape(const_3764.astype('int8'), [56,]), relay.reshape(var_3765.astype('float32'), [168, 2]), relay.reshape(var_3766.astype('float64'), [11, 7, 8]), ), 1)
call_3767 = relay.TupleGetItem(func_2855_call(relay.reshape(const_3764.astype('int8'), [56,]), relay.reshape(var_3765.astype('float32'), [168, 2]), relay.reshape(var_3766.astype('float64'), [11, 7, 8]), ), 1)
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_3768 = relay.TupleGetItem(func_1817_call(), 0)
call_3769 = relay.TupleGetItem(func_1818_call(), 0)
output = relay.Tuple([call_3758,call_3763,const_3764,var_3765,var_3766,call_3768,])
output2 = relay.Tuple([call_3759,call_3767,const_3764,var_3765,var_3766,call_3769,])
func_3804 = relay.Function([var_3765,var_3766,], output)
mod['func_3804'] = func_3804
mod = relay.transform.InferType()(mod)
var_3805 = relay.var("var_3805", dtype = "float32", shape = (2, 168))#candidate|3805|(2, 168)|var|float32
var_3806 = relay.var("var_3806", dtype = "float64", shape = (616,))#candidate|3806|(616,)|var|float64
output = func_3804(var_3805,var_3806,)
func_3807 = relay.Function([var_3805,var_3806,], output)
mutated_mod['func_3807'] = func_3807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3523_call = mod.get_global_var('func_3523')
func_3525_call = mutated_mod.get_global_var('func_3525')
call_3876 = relay.TupleGetItem(func_3523_call(), 1)
call_3877 = relay.TupleGetItem(func_3525_call(), 1)
func_1888_call = mod.get_global_var('func_1888')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_3909 = relay.TupleGetItem(func_1888_call(), 0)
call_3910 = relay.TupleGetItem(func_1890_call(), 0)
output = relay.Tuple([call_3876,call_3909,])
output2 = relay.Tuple([call_3877,call_3910,])
func_3919 = relay.Function([], output)
mod['func_3919'] = func_3919
mod = relay.transform.InferType()(mod)
output = func_3919()
func_3920 = relay.Function([], output)
mutated_mod['func_3920'] = func_3920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_3929 = relay.TupleGetItem(func_2043_call(), 0)
call_3930 = relay.TupleGetItem(func_2044_call(), 0)
output = relay.Tuple([call_3929,])
output2 = relay.Tuple([call_3930,])
func_3932 = relay.Function([], output)
mod['func_3932'] = func_3932
mod = relay.transform.InferType()(mod)
output = func_3932()
func_3933 = relay.Function([], output)
mutated_mod['func_3933'] = func_3933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mod.get_global_var('func_2147')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_3951 = relay.TupleGetItem(func_2147_call(), 1)
call_3952 = relay.TupleGetItem(func_2149_call(), 1)
output = relay.Tuple([call_3951,])
output2 = relay.Tuple([call_3952,])
func_3966 = relay.Function([], output)
mod['func_3966'] = func_3966
mod = relay.transform.InferType()(mod)
output = func_3966()
func_3967 = relay.Function([], output)
mutated_mod['func_3967'] = func_3967
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4048 = relay.var("var_4048", dtype = "float32", shape = (5, 7, 8))#candidate|4048|(5, 7, 8)|var|float32
uop_4049 = relay.log(var_4048.astype('float32')) # shape=(5, 7, 8)
func_1602_call = mod.get_global_var('func_1602')
func_1605_call = mutated_mod.get_global_var('func_1605')
const_4061 = relay.const([[-3,-7,7,2,3,9,-1,-4,9,-5,5,6,8,-2,1,5,7,4,10,-10,-6,-4,5,2,-9,-4,6,-8],[7,7,-2,-3,2,4,5,-9,-3,10,1,4,10,-4,10,-1,4,5,10,-6,5,-6,-4,-3,-8,-4,4,-10]], dtype = "int8")#candidate|4061|(2, 28)|const|int8
call_4060 = relay.TupleGetItem(func_1602_call(relay.reshape(const_4061.astype('int8'), [1, 7, 8])), 0)
call_4062 = relay.TupleGetItem(func_1605_call(relay.reshape(const_4061.astype('int8'), [1, 7, 8])), 0)
output = relay.Tuple([uop_4049,call_4060,const_4061,])
output2 = relay.Tuple([uop_4049,call_4062,const_4061,])
func_4063 = relay.Function([var_4048,], output)
mod['func_4063'] = func_4063
mod = relay.transform.InferType()(mod)
var_4064 = relay.var("var_4064", dtype = "float32", shape = (5, 7, 8))#candidate|4064|(5, 7, 8)|var|float32
output = func_4063(var_4064)
func_4065 = relay.Function([var_4064], output)
mutated_mod['func_4065'] = func_4065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3034_call = mod.get_global_var('func_3034')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_4154 = relay.TupleGetItem(func_3034_call(), 2)
call_4155 = relay.TupleGetItem(func_3035_call(), 2)
output = relay.Tuple([call_4154,])
output2 = relay.Tuple([call_4155,])
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
func_3720_call = mod.get_global_var('func_3720')
func_3721_call = mutated_mod.get_global_var('func_3721')
call_4289 = func_3720_call()
call_4290 = func_3720_call()
func_283_call = mod.get_global_var('func_283')
func_285_call = mutated_mod.get_global_var('func_285')
var_4296 = relay.var("var_4296", dtype = "float32", shape = (132,))#candidate|4296|(132,)|var|float32
call_4295 = relay.TupleGetItem(func_283_call(relay.reshape(var_4296.astype('float32'), [4, 11, 3])), 3)
call_4297 = relay.TupleGetItem(func_285_call(relay.reshape(var_4296.astype('float32'), [4, 11, 3])), 3)
func_1981_call = mod.get_global_var('func_1981')
func_1985_call = mutated_mod.get_global_var('func_1985')
var_4303 = relay.var("var_4303", dtype = "float32", shape = (7, 110))#candidate|4303|(7, 110)|var|float32
var_4304 = relay.var("var_4304", dtype = "float32", shape = (336,))#candidate|4304|(336,)|var|float32
call_4302 = relay.TupleGetItem(func_1981_call(relay.reshape(var_4303.astype('float32'), [11, 14, 5]), relay.reshape(var_4304.astype('float32'), [336,]), ), 0)
call_4305 = relay.TupleGetItem(func_1985_call(relay.reshape(var_4303.astype('float32'), [11, 14, 5]), relay.reshape(var_4304.astype('float32'), [336,]), ), 0)
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_4319 = relay.TupleGetItem(func_1817_call(), 1)
call_4320 = relay.TupleGetItem(func_1818_call(), 1)
output = relay.Tuple([call_4289,call_4295,var_4296,call_4302,var_4303,var_4304,call_4319,])
output2 = relay.Tuple([call_4290,call_4297,var_4296,call_4305,var_4303,var_4304,call_4320,])
func_4321 = relay.Function([var_4296,var_4303,var_4304,], output)
mod['func_4321'] = func_4321
mod = relay.transform.InferType()(mod)
mutated_mod['func_4321'] = func_4321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4321_call = mutated_mod.get_global_var('func_4321')
var_4323 = relay.var("var_4323", dtype = "float32", shape = (132,))#candidate|4323|(132,)|var|float32
var_4324 = relay.var("var_4324", dtype = "float32", shape = (7, 110))#candidate|4324|(7, 110)|var|float32
var_4325 = relay.var("var_4325", dtype = "float32", shape = (336,))#candidate|4325|(336,)|var|float32
call_4322 = func_4321_call(var_4323,var_4324,var_4325,)
output = call_4322
func_4326 = relay.Function([var_4323,var_4324,var_4325,], output)
mutated_mod['func_4326'] = func_4326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3966_call = mod.get_global_var('func_3966')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_4331 = relay.TupleGetItem(func_3966_call(), 0)
call_4332 = relay.TupleGetItem(func_3967_call(), 0)
func_3919_call = mod.get_global_var('func_3919')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_4333 = relay.TupleGetItem(func_3919_call(), 0)
call_4334 = relay.TupleGetItem(func_3920_call(), 0)
output = relay.Tuple([call_4331,call_4333,])
output2 = relay.Tuple([call_4332,call_4334,])
func_4341 = relay.Function([], output)
mod['func_4341'] = func_4341
mod = relay.transform.InferType()(mod)
output = func_4341()
func_4342 = relay.Function([], output)
mutated_mod['func_4342'] = func_4342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2546_call = mod.get_global_var('func_2546')
func_2547_call = mutated_mod.get_global_var('func_2547')
call_4365 = func_2546_call()
call_4366 = func_2546_call()
output = call_4365
output2 = call_4366
func_4391 = relay.Function([], output)
mod['func_4391'] = func_4391
mod = relay.transform.InferType()(mod)
output = func_4391()
func_4392 = relay.Function([], output)
mutated_mod['func_4392'] = func_4392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_4404 = relay.TupleGetItem(func_1817_call(), 1)
call_4405 = relay.TupleGetItem(func_1818_call(), 1)
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_4407 = relay.TupleGetItem(func_3123_call(), 1)
call_4408 = relay.TupleGetItem(func_3124_call(), 1)
var_4414 = relay.var("var_4414", dtype = "float64", shape = (1, 10, 2))#candidate|4414|(1, 10, 2)|var|float64
bop_4415 = relay.equal(call_4407.astype('bool'), relay.reshape(var_4414.astype('bool'), relay.shape_of(call_4407))) # shape=(1, 10, 2)
bop_4418 = relay.equal(call_4408.astype('bool'), relay.reshape(var_4414.astype('bool'), relay.shape_of(call_4408))) # shape=(1, 10, 2)
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_4421 = relay.TupleGetItem(func_3123_call(), 0)
call_4422 = relay.TupleGetItem(func_3124_call(), 0)
output = relay.Tuple([call_4404,bop_4415,call_4421,])
output2 = relay.Tuple([call_4405,bop_4418,call_4422,])
func_4425 = relay.Function([var_4414,], output)
mod['func_4425'] = func_4425
mod = relay.transform.InferType()(mod)
var_4426 = relay.var("var_4426", dtype = "float64", shape = (1, 10, 2))#candidate|4426|(1, 10, 2)|var|float64
output = func_4425(var_4426)
func_4427 = relay.Function([var_4426], output)
mutated_mod['func_4427'] = func_4427
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4435 = relay.const([[[-6.398903,6.962490,-8.793043,5.051631,-3.703063,6.099083,8.486237,-7.468766,-8.651402,-8.662200,2.752389,-0.815299,-0.347270],[3.085635,-4.375543,-9.220913,-4.842853,0.530976,2.513875,5.769793,-6.317449,0.770592,-1.401907,2.866408,-0.466217,6.906809],[8.747741,6.223067,4.871637,7.569370,2.943299,-0.073836,3.143527,-6.377342,-1.993790,4.272413,2.858250,-4.175224,-8.696637],[-8.418392,-7.619043,-3.044398,6.245379,6.191238,4.184736,-9.286663,-6.495674,-2.589816,1.999255,-1.753130,-5.805715,-2.020873],[6.057191,1.593909,-0.458412,-9.806891,0.441706,-7.212437,6.474238,9.751628,0.098718,6.580929,7.879185,6.289080,0.946443],[-1.065944,0.958146,6.280198,-5.439535,7.862203,-0.399406,6.909840,-5.415591,-6.483101,7.373526,-4.093821,-0.204136,6.726436],[-0.392394,-0.496960,-2.741202,2.505360,9.570306,-4.121173,-5.184450,-6.515754,-2.089245,-1.432217,-0.979075,-6.094305,3.363539]],[[-5.823636,-4.405230,7.370190,-1.115275,-8.788042,-9.265609,3.008406,-0.949647,6.259230,6.659227,1.844507,5.098362,-9.324710],[7.724723,-6.673200,-0.081690,-8.331591,-5.677810,6.895404,8.559368,9.980047,8.953179,8.098001,9.124281,-8.060804,-8.534181],[-9.079038,-7.653454,6.361625,2.624159,-3.029646,-8.415838,-2.712575,-4.558619,-1.666715,-0.875042,7.601231,-5.982512,5.497989],[-2.983657,-5.974971,-8.401960,-3.099474,0.516449,-4.889768,5.897574,-3.031243,1.538430,-1.884498,-8.317303,8.397048,3.720693],[5.888775,9.827897,1.644690,-8.275506,-0.975078,-8.221876,6.205144,6.816031,-6.598682,-1.488596,-7.702083,5.505248,5.530115],[0.350520,-1.266818,-5.549828,-1.463554,0.940881,4.338233,2.516696,-0.448238,-3.823784,-2.607908,8.928517,7.977414,2.751508],[7.711677,-3.943418,3.765939,2.298433,-0.813850,0.913977,2.871081,-9.312033,-4.436099,-2.975427,7.299184,1.040631,-7.265187]]], dtype = "float32")#candidate|4435|(2, 7, 13)|const|float32
var_4436 = relay.var("var_4436", dtype = "float32", shape = (2, 7, 13))#candidate|4436|(2, 7, 13)|var|float32
bop_4437 = relay.power(const_4435.astype('float32'), relay.reshape(var_4436.astype('float32'), relay.shape_of(const_4435))) # shape=(2, 7, 13)
output = bop_4437
output2 = bop_4437
func_4445 = relay.Function([var_4436,], output)
mod['func_4445'] = func_4445
mod = relay.transform.InferType()(mod)
var_4446 = relay.var("var_4446", dtype = "float32", shape = (2, 7, 13))#candidate|4446|(2, 7, 13)|var|float32
output = func_4445(var_4446)
func_4447 = relay.Function([var_4446], output)
mutated_mod['func_4447'] = func_4447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3160_call = mod.get_global_var('func_3160')
func_3161_call = mutated_mod.get_global_var('func_3161')
call_4553 = func_3160_call()
call_4554 = func_3160_call()
output = call_4553
output2 = call_4554
func_4576 = relay.Function([], output)
mod['func_4576'] = func_4576
mod = relay.transform.InferType()(mod)
mutated_mod['func_4576'] = func_4576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4576_call = mutated_mod.get_global_var('func_4576')
call_4577 = func_4576_call()
output = call_4577
func_4578 = relay.Function([], output)
mutated_mod['func_4578'] = func_4578
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4609 = relay.const([[[-3.442289,8.722726,1.915067,9.296857,-9.491622,0.754163,-1.776317,7.288595,-4.888017],[-3.256519,-4.324319,6.335028,-7.724810,5.351652,3.173249,-5.939456,1.883001,6.873465],[-7.608135,-6.050837,-9.532287,3.330156,-8.974997,9.408463,-1.023895,-4.620879,-1.198866],[6.090145,4.182023,5.568134,6.449089,-3.607114,0.527212,8.121567,-6.602292,4.910514],[-7.529813,-5.375596,3.080290,2.357927,0.808549,-6.884525,8.645752,7.782797,-1.257960],[4.114272,-0.582922,2.568359,7.798311,-8.493842,-0.415638,9.284782,-8.502218,-4.965823],[8.720046,0.239818,3.675282,-2.408808,6.305209,9.457672,-4.198145,7.279769,-6.594152],[2.717356,0.500658,-7.533924,4.010987,-8.004577,0.046743,1.345115,4.837460,9.702844],[1.653731,5.558843,8.726464,-6.486099,-9.381379,7.675285,-3.862434,-9.359135,-3.647561],[-5.991088,-5.573232,3.680235,8.793029,-4.532897,5.119224,8.817255,-8.127375,8.474586],[-3.762388,8.548113,8.371166,1.791562,6.238419,3.006475,-5.547983,9.410587,4.169398],[-2.681834,-4.795264,4.710611,1.297348,-0.150344,8.560604,8.219882,7.774968,-7.689349],[2.310639,0.636380,-4.365503,-0.818488,-9.550197,0.004933,-9.578350,-6.388844,6.831243],[-6.545808,-5.384013,-5.288059,-2.189101,8.119061,-8.200112,-0.685230,-8.532922,6.719221],[8.142927,1.641036,0.684076,1.742216,2.504994,-8.582249,1.088017,8.203679,3.881338]],[[0.758628,6.251416,-1.823480,0.914572,-9.077834,-2.996379,-6.697568,8.824879,0.310740],[-2.976370,2.658125,-3.776660,-7.599492,-7.426093,9.262272,5.363485,-4.615004,-0.722925],[4.182074,3.506243,1.777742,5.248706,3.710421,4.892839,5.279613,2.319566,8.261679],[7.261557,3.269989,1.743265,7.541813,-4.798393,-1.183436,-7.696609,-0.314294,5.685384],[6.727720,7.382132,5.076256,2.373410,-3.427060,3.744592,-1.124184,-4.366191,7.072690],[4.594675,-6.499675,-7.831898,-2.184091,-0.285605,-0.064948,-6.835600,-6.172754,2.128976],[-8.546698,5.540850,4.624908,9.030296,4.955523,-5.681145,4.559174,6.265964,1.167056],[-7.532018,9.081257,-0.116106,-7.980464,7.079298,-1.042093,1.072985,-7.632847,8.252587],[9.416384,1.219921,-0.337262,2.189787,6.345333,-6.797773,-1.303974,-8.345287,5.693047],[-0.218709,6.063200,8.563744,-8.042173,9.308828,9.444496,-5.784104,8.741354,4.919171],[0.099758,2.060408,1.415414,9.311832,1.176773,2.668969,-6.615827,-6.589877,-6.745465],[1.207429,-1.577489,8.334660,-5.274319,1.759928,6.203895,9.286561,3.804681,-5.434837],[-6.805210,5.825554,7.667995,6.037380,-9.877695,-2.626158,0.866406,3.064338,-3.392269],[4.210390,-5.110323,-5.536712,6.446151,0.830490,-1.473895,2.731204,3.445131,-9.385695],[-5.783072,9.342982,-8.738828,9.736059,0.102004,2.320763,7.090968,-0.818107,2.035635]],[[0.161356,3.520140,-4.497491,-0.720604,-1.173044,-9.791505,9.387347,-4.479337,8.918385],[-7.142183,-3.712459,9.369160,8.030398,-5.206468,-5.146159,-8.233389,-7.215192,-3.160851],[0.847762,4.549744,0.877729,4.481205,-3.786006,6.801022,-1.899019,-5.245520,6.049193],[-9.288386,-5.348194,6.036424,7.119110,-5.181215,8.126952,-7.970543,-0.047615,-5.772111],[4.107026,-0.296802,-7.052644,7.352030,4.740096,5.571308,9.842221,3.047946,1.833682],[-1.077848,-5.762693,-4.024028,-4.478609,-4.022358,-0.928098,-3.764596,-2.833742,0.041931],[-2.807077,7.414413,-0.561208,-4.495915,1.822807,1.254212,-5.729255,4.368076,4.937321],[-1.102588,-5.854245,-0.453517,-9.965407,-7.261317,9.600595,3.290532,-3.375045,8.165960],[0.157333,-8.598950,1.464154,2.536559,9.788020,-4.635978,8.575531,-8.761153,1.727817],[-5.094030,7.568946,0.942041,8.001532,-7.247671,5.730195,-3.619874,-6.133850,4.776278],[8.296210,5.894153,6.701742,9.715343,3.974005,-9.242847,-6.569730,-4.023930,8.401554],[-1.981778,-9.385391,-1.602557,-1.071381,-5.325791,0.429443,-5.597058,1.586274,-8.568896],[2.130118,2.440853,1.894845,2.604193,-4.877640,-1.434993,1.542722,-7.775059,0.913238],[-6.009647,-8.471297,-1.430003,-3.008306,-4.965927,6.905583,6.239583,-3.169667,0.028402],[-3.555148,8.019052,-7.568917,4.672301,-9.364463,9.620576,-2.833828,4.390172,-4.605411]],[[1.269178,-3.966891,-2.699544,-1.554100,-7.060192,-3.966768,-5.879850,-3.453806,-5.325546],[4.546435,0.729373,9.517724,-9.347355,-7.520757,-8.793018,8.204942,3.388191,3.507626],[3.715511,3.501143,-6.925194,7.555131,1.220716,-2.723566,-7.612964,3.871986,1.106124],[-4.539331,-7.952580,6.930214,-9.718799,-4.613440,-5.373350,2.389080,9.089432,2.799993],[6.547434,0.606862,6.724098,-2.008476,7.994053,0.335242,-5.924819,-2.249080,-5.407995],[-4.120717,5.790465,-5.635134,-1.478606,9.815421,0.557340,-3.106124,-4.477179,9.991217],[9.052305,0.038599,6.600833,-9.107464,2.776501,-0.590885,-3.635814,-2.034080,-7.025115],[-2.560611,-1.847873,-8.579972,-2.831354,-5.485936,-3.246800,-3.030259,1.073143,2.988098],[-4.244676,3.929178,-0.310138,3.209290,-3.129662,-6.788192,3.005885,2.818753,1.211343],[5.628589,-9.410198,-5.072520,9.400797,3.046453,-8.192637,7.199170,-9.710029,-2.704451],[-0.631521,3.100062,9.263013,6.445659,-7.044222,6.190899,3.716320,-0.565702,-7.099817],[-1.385347,2.896167,7.787310,-9.698771,7.392493,5.056449,-0.625481,6.599717,-7.594793],[5.126368,9.192630,-0.851049,6.244323,5.996965,-1.949479,-0.416326,8.860716,-0.354083],[-9.698480,4.607396,6.512032,4.759305,3.884166,9.915518,-5.194985,7.649724,4.442648],[-5.938959,6.067963,-8.516826,1.584793,6.517135,-7.398292,0.794385,-7.889379,-4.670667]],[[0.346130,7.864204,2.304073,-4.844251,-3.969655,0.678834,-8.955763,-8.987573,-8.559340],[0.399068,-1.462520,-2.641651,-2.000411,4.413682,2.432678,-2.234519,4.967161,9.301422],[-1.652504,-7.681065,8.089191,-7.378247,5.867256,-9.938139,3.650765,-6.975078,-3.436563],[3.914561,-6.210137,5.842494,-7.523994,9.147108,-1.234638,-5.699758,-4.687658,2.400326],[8.085063,8.494468,-0.398664,-8.011580,0.786693,0.024262,5.386015,-5.989277,6.770904],[5.808275,5.151392,-8.630289,7.411954,3.430888,6.485131,-7.664259,-7.540310,-7.066663],[6.390142,3.202473,8.963740,-5.658329,7.173715,-1.166444,-0.910180,-2.429857,-4.451621],[2.987599,-7.665049,-6.305941,2.566069,-7.734808,-9.034116,6.125458,0.212915,5.982370],[1.841743,4.643602,-6.487709,-8.297167,-4.966863,7.174332,8.154308,-1.268940,4.681245],[3.733039,3.914510,-5.990392,-8.381853,2.444860,-8.219911,-6.986371,-6.343885,-8.181834],[-3.993303,-5.585406,-8.219357,7.468547,-4.593207,0.395206,-5.967245,0.297039,-4.705540],[-2.977997,1.866399,-0.494530,-4.150716,3.618443,-8.165508,3.012572,-4.875690,0.832579],[7.208140,-1.417470,0.616319,3.046200,6.821948,5.002858,3.456899,-5.405556,-3.484195],[-8.291085,-1.241787,6.989234,-1.142229,3.606791,-2.148324,4.894808,0.332234,-0.155814],[8.827214,7.737006,-0.626427,-0.432377,-6.796977,-1.587211,0.349255,6.629713,-9.682202]],[[-0.612224,3.643038,-2.598771,9.232797,-2.160854,2.523363,0.470220,-8.696154,7.090402],[6.839186,-1.314943,9.895258,-3.191600,-1.935407,-2.497497,8.915287,0.583437,-9.086487],[-7.653642,8.772328,-2.617095,8.991259,0.358861,-9.653434,-8.959048,-8.564846,3.951715],[4.409255,-6.693433,8.683900,4.469950,4.478162,-2.368725,-7.265302,6.737009,9.496362],[-4.248887,5.597213,-6.716413,2.922916,-6.695446,-9.998137,4.588966,8.390300,2.269980],[-1.039504,5.899124,8.277474,9.860798,4.329043,4.830407,-1.222742,5.929954,2.886730],[-6.894520,6.013861,-7.913262,-4.732161,5.633256,1.192347,7.944380,6.721376,5.248119],[-2.467391,-0.057827,-9.641234,-7.128478,-7.279454,-9.760485,5.641060,-8.387359,9.871900],[-8.102284,-8.503957,-4.411220,-0.853393,8.052057,-8.121011,-3.337019,1.648205,-6.584737],[-4.491274,-4.733740,5.771775,-6.227700,9.992711,7.926360,6.071757,1.784738,7.209262],[6.125484,1.665137,-5.556175,-9.261936,-0.185364,1.080887,8.489159,6.446687,-3.858830],[-8.325935,0.820019,6.476947,1.590225,8.277438,-7.938446,-5.170060,-0.116720,-2.238118],[4.381027,-7.192917,-3.918744,8.601956,0.043165,-2.152376,2.049621,1.322483,-0.407681],[1.011984,5.282540,-4.241625,9.223555,-6.535848,-4.983161,-2.521483,1.826832,5.609784],[3.400081,8.258829,6.842102,-5.363959,-9.477885,-0.940348,8.715460,-2.684724,-7.195550]]], dtype = "float64")#candidate|4609|(6, 15, 9)|const|float64
uop_4610 = relay.log2(const_4609.astype('float64')) # shape=(6, 15, 9)
output = uop_4610
output2 = uop_4610
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
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_4678 = func_1716_call()
call_4679 = func_1716_call()
output = call_4678
output2 = call_4679
func_4682 = relay.Function([], output)
mod['func_4682'] = func_4682
mod = relay.transform.InferType()(mod)
mutated_mod['func_4682'] = func_4682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4682_call = mutated_mod.get_global_var('func_4682')
call_4683 = func_4682_call()
output = call_4683
func_4684 = relay.Function([], output)
mutated_mod['func_4684'] = func_4684
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4699 = relay.var("var_4699", dtype = "uint64", shape = (13, 13, 11))#candidate|4699|(13, 13, 11)|var|uint64
const_4700 = relay.const([[[-3,-5,-8,5,1,-5,-1,-7,-4,-5,4],[-7,-6,-4,-8,7,2,6,2,-3,3,-5],[8,5,8,-10,-3,-9,-6,8,-2,5,4],[5,5,10,-7,4,-4,-7,8,-7,8,2],[10,6,-4,5,4,-5,-9,-9,-9,-4,-4],[7,10,-3,-9,10,4,9,-7,-9,6,10],[-10,-4,1,-1,-8,-7,10,5,-4,9,3],[7,4,-10,1,-6,8,7,5,-6,-6,-1],[2,8,-3,3,6,-5,-7,1,-5,-6,-4],[-6,-3,-3,-5,7,-10,-3,-1,8,-8,8],[-8,-3,5,-7,4,-1,6,-6,-8,-8,6],[-3,10,6,2,3,-4,-2,8,1,3,-9],[-4,9,5,-10,9,-10,5,-6,2,7,-10]],[[7,10,-9,8,9,-10,5,6,-8,9,5],[-4,10,-4,1,10,9,-6,1,6,-9,10],[4,9,4,-10,1,2,1,2,10,-2,10],[-9,5,2,-6,5,-10,-3,-4,5,-8,-9],[-3,-5,-3,-3,-6,-5,-2,4,-1,7,5],[8,-3,-5,10,-4,-6,-7,5,-1,6,3],[-5,3,7,-7,-10,-2,-8,5,-2,2,-7],[7,2,-4,-6,-6,5,-6,3,-7,-8,7],[-7,-7,-3,-6,-1,2,-3,-4,5,-7,-1],[-5,6,-7,-2,-4,7,9,-10,10,-8,-5],[-1,9,8,6,-10,-6,-4,3,-7,6,-10],[-6,10,4,-8,-8,-9,-5,-2,8,4,8],[-9,8,2,2,1,-2,3,8,6,-2,-4]],[[2,2,9,6,-5,-10,2,7,4,1,-8],[4,10,5,-3,-1,-6,-4,8,-4,-4,-8],[-8,10,4,10,8,9,1,1,4,8,-4],[6,-4,-7,-5,-5,-3,-5,-6,10,-8,-5],[-4,5,-6,-9,-9,4,-3,2,-7,3,9],[6,4,3,-4,2,-3,-7,2,-3,9,2],[10,2,-10,9,2,9,1,5,-10,-7,-4],[6,-10,-6,-6,-1,-4,-4,-5,-4,-8,10],[-4,-9,3,-9,-10,-4,-2,7,1,-2,2],[-9,-9,-5,-7,10,-1,-6,-3,-3,10,3],[-8,-9,10,-3,-9,1,-5,-7,-1,-4,6],[-9,4,1,-9,-5,-7,-3,-6,-9,-9,5],[7,6,10,10,-1,4,1,9,-2,-7,1]],[[-5,-6,-3,7,9,-1,1,7,5,2,-3],[-7,-5,9,5,1,8,-6,-2,-1,8,8],[-3,-3,-2,8,-10,-8,-3,4,-8,9,10],[-8,-10,-5,-1,6,-5,2,3,-3,-4,-5],[-9,-4,4,4,1,-8,9,7,-6,1,3],[-9,3,9,-4,-6,-5,-1,-6,-5,-4,-7],[-8,-2,7,-6,-9,7,8,1,2,6,-10],[10,-9,-2,-10,8,1,-10,3,9,2,4],[-1,3,-2,3,-3,7,-8,9,-10,-7,4],[1,3,9,-5,-7,-10,4,-7,-6,-1,-6],[-4,8,9,4,3,3,7,-3,-7,-1,-9],[10,1,8,-9,-1,-9,-6,4,-2,-7,-3],[8,-7,6,-3,2,-3,-7,6,-7,-8,6]],[[3,-6,-7,1,-7,7,4,-1,-10,-10,9],[6,-5,10,7,7,-8,-8,-6,-6,-8,5],[8,-10,-3,3,-10,-5,4,-8,3,-3,-8],[5,-2,5,4,3,-9,2,5,-2,-8,10],[4,3,3,6,8,5,2,9,3,-10,5],[4,9,5,-3,-9,2,4,-9,9,2,9],[-6,-2,10,-1,5,-7,1,4,-6,3,-7],[5,7,-7,-8,7,-3,-6,2,-10,-5,1],[-8,2,-10,-3,-1,-6,2,1,8,-7,6],[5,-1,5,9,-1,-1,-2,9,-9,-4,3],[6,8,-2,6,8,-8,-6,4,8,-6,-10],[1,4,10,-5,-3,-6,7,-6,8,6,-3],[-8,2,2,-5,4,2,6,-5,-6,1,1]],[[-2,3,-1,7,-3,-10,-2,-3,-7,-3,-5],[2,9,10,1,-10,-8,-6,-3,-4,-9,1],[9,8,-9,6,9,5,5,8,7,-1,-2],[-4,10,-9,-4,-10,-2,-10,9,-8,3,6],[9,4,-3,-8,9,-10,-2,8,1,3,-6],[6,-9,6,8,-2,8,-10,10,-8,4,10],[8,3,7,3,-9,1,-5,-1,-8,1,-8],[9,-1,-9,-6,10,-8,-5,9,8,-1,9],[5,1,3,-9,3,1,4,8,10,8,-10],[-2,-3,10,-1,-9,9,8,-2,-2,-5,-10],[2,3,-5,-9,3,6,6,-7,-3,3,-8],[3,-10,-6,8,5,3,4,-6,3,-6,3],[-4,-1,9,-8,-9,-7,-6,5,9,5,-8]],[[8,-2,3,-9,-4,-9,2,2,-4,-1,-9],[4,-2,-4,4,6,5,-4,-9,-7,8,9],[5,-9,10,10,8,5,-6,9,-10,2,4],[-6,-1,-8,-8,-6,-8,-1,-5,-10,-6,3],[6,4,8,1,-3,6,9,-10,3,-7,-3],[9,-9,2,-6,7,-8,7,-8,9,7,-3],[1,1,-3,5,9,5,5,-5,-4,-2,-5],[8,7,-3,5,1,1,-2,-2,-10,4,-1],[3,-1,-10,9,2,-7,7,5,7,-9,-8],[3,-1,5,8,-6,3,6,-10,9,2,-3],[7,10,6,4,-2,5,10,9,-7,-9,-10],[-4,-9,4,-8,-10,-7,-10,-2,6,-1,-7],[3,9,1,-10,2,-3,6,4,-6,-10,-7]],[[-7,-5,2,8,-7,5,10,-3,-7,4,-9],[9,6,-10,-10,7,7,-4,7,8,2,-9],[9,3,-8,6,-7,3,-10,-10,-1,2,8],[-4,-8,9,8,-4,-10,1,-6,-9,9,6],[4,-2,4,10,-9,-9,1,-9,-7,-3,10],[7,8,8,-8,9,-2,-7,-6,-10,-5,2],[-8,2,3,-2,-7,8,-7,-7,3,-6,-8],[3,2,-8,4,-3,-10,8,8,6,-9,3],[1,10,5,-10,3,-8,9,-3,6,7,-9],[-9,5,4,-10,-1,-6,-6,8,-5,-9,7],[-7,-3,4,-10,3,2,7,-1,1,-1,-2],[10,-10,5,8,-9,10,-9,-10,-9,-10,-10],[-7,7,4,6,2,-9,9,-4,-4,3,5]],[[-2,10,-9,-2,-9,-1,-6,-2,-10,-8,-9],[-3,-3,7,2,-7,8,-6,10,-5,7,-7],[10,5,6,-9,10,9,8,1,-8,4,8],[3,8,-8,4,9,-7,-4,-10,9,6,7],[-5,-5,9,-1,1,-6,1,-7,-1,9,-3],[-2,-7,-4,8,8,-2,-6,-6,9,-10,8],[10,8,-2,-9,1,9,-2,-2,6,4,5],[-10,-9,-8,-3,10,-2,5,5,-8,-5,6],[-3,10,10,-9,5,8,6,3,-4,3,1],[-9,-1,-7,-5,-6,1,8,-1,8,6,-10],[-4,4,-5,-2,-4,-7,10,-5,-6,3,-8],[-1,-10,5,-7,-10,7,8,2,10,-3,-3],[10,-7,-1,-4,-1,-8,-3,9,-9,10,-5]],[[-9,10,-5,8,-3,-7,7,-1,7,-5,5],[7,8,6,-3,8,-10,-3,9,-6,-2,-5],[3,9,9,4,-3,-9,6,-1,-6,10,7],[-2,5,-1,3,5,3,3,-1,6,-9,-5],[2,-5,-6,6,-8,-10,-6,-1,8,-4,-3],[2,5,6,-5,-8,-10,7,8,9,-4,1],[1,-1,-10,-9,4,-7,-1,1,-5,-5,2],[10,9,-7,10,5,10,2,10,4,-5,1],[3,4,-2,2,-2,5,-4,4,-10,5,4],[-1,9,8,-6,9,-2,-7,1,10,4,7],[-8,9,-2,10,-10,-10,-8,-2,-9,6,-4],[-8,2,2,-3,-1,-2,1,-5,-9,3,5],[-10,-8,9,-2,6,-10,8,-4,1,-4,-8]],[[-6,-7,9,6,3,-2,-7,-6,-4,9,-1],[-5,9,-2,8,9,4,-1,-8,-8,5,4],[3,-8,-10,-10,-3,-8,1,-5,-2,7,2],[1,-6,-1,-1,10,-2,-8,7,-5,-4,-5],[3,-6,-6,-10,-10,8,-10,-7,-3,4,9],[-10,-1,-9,10,-10,3,9,-10,8,2,7],[5,2,3,3,-7,8,-2,2,8,6,-9],[-1,-5,-10,6,-8,9,9,5,4,7,-9],[9,-10,3,-10,-2,-3,1,4,9,8,-2],[-2,7,9,9,2,9,-9,-7,-9,2,-5],[-5,10,-1,-4,5,1,3,7,-10,-2,-10],[-3,9,-3,-4,-4,7,3,-4,2,4,-3],[-7,-10,1,6,-2,6,1,-2,10,-3,4]],[[7,-4,1,-4,6,-7,10,8,-7,7,4],[7,-4,-6,3,3,-1,-9,-7,-5,6,-1],[9,-2,-2,2,-8,3,-7,9,10,10,-10],[-2,-3,2,-10,-8,2,7,-1,-1,-9,1],[5,8,3,-7,-8,-10,9,-2,4,-7,-2],[-2,5,-3,10,-2,5,10,-5,-1,-9,6],[4,4,8,6,-8,-2,-2,9,9,6,-9],[-2,-7,-9,-5,-2,-3,-6,-10,10,1,-2],[6,-4,3,1,-8,8,7,2,10,-10,10],[3,-10,-9,6,-3,-5,9,7,-9,4,-2],[3,-2,6,8,-2,8,-6,3,10,-4,1],[2,3,4,-9,8,-8,6,6,4,9,-10],[-8,-8,-6,-5,6,-6,-9,8,-7,-9,-9]],[[-1,-3,5,-6,8,7,-4,8,2,7,7],[-10,-3,1,4,-10,-7,1,-6,6,-10,-8],[7,-6,-2,-9,-10,-3,-8,8,6,-8,-1],[-2,3,-1,-10,1,-6,6,-1,-8,6,3],[-8,7,-9,5,-1,8,-5,-8,7,2,-8],[3,5,-8,5,-6,-4,-4,-5,4,-8,-1],[9,-7,1,-2,-8,-6,-6,-4,8,3,3],[7,-8,4,-3,-6,4,-1,-3,-4,7,3],[-6,4,7,8,-5,-5,-3,-7,-6,1,8],[-7,-4,-3,-10,-4,-1,10,6,-7,-10,3],[3,-2,-5,-9,4,8,-6,8,-5,-2,-9],[-6,10,-7,6,-8,10,-10,-4,9,-4,5],[-8,-7,5,1,2,10,-1,-6,7,-7,-3]]], dtype = "uint64")#candidate|4700|(13, 13, 11)|const|uint64
bop_4701 = relay.less(var_4699.astype('bool'), relay.reshape(const_4700.astype('bool'), relay.shape_of(var_4699))) # shape=(13, 13, 11)
uop_4707 = relay.acos(const_4700.astype('float32')) # shape=(13, 13, 11)
func_1981_call = mod.get_global_var('func_1981')
func_1985_call = mutated_mod.get_global_var('func_1985')
const_4742 = relay.const([2.554716,6.055385,-3.482836,-5.788332,-8.084328,6.342486,-5.700016,4.083507,5.872671,1.892853,1.420646,-7.601395,1.750577,-4.820315,-8.541891,-6.653875,7.876759,-8.538387,0.600348,2.940412,-1.353411,6.589927,4.331266,1.240879,7.482511,6.511443,5.573063,-6.974359,-7.206088,6.045151,7.018216,-2.914599,-3.425433,2.500944,6.809350,2.835229,9.356551,9.086517,8.545245,9.339767,4.094905,6.100069,-7.204208,5.120148,-9.216867,-9.927266,-3.024459,1.417234,9.353160,-8.097240,5.825397,-5.364948,-1.312254,3.760094,-8.371841,6.274622,7.703235,0.045910,-1.634139,-9.640020,6.595673,-1.764784,-5.642400,-4.733184,-7.589520,-0.056308,4.877796,-1.517506,-2.695897,1.438461,7.417815,-8.811016,-4.420159,-4.160777,-7.999133,6.840026,6.870525,8.131774,3.170311,7.991407,-4.726602,0.471652,9.101434,-0.346264,6.739135,-2.597772,-0.863654,0.187727,-2.350663,7.209520,2.335144,0.246472,-0.771368,-9.326729,-9.195768,-6.266631,3.371333,-6.977590,2.022484,8.907537,5.935979,6.933559,-5.854382,-5.994194,0.872021,-9.964682,-4.722832,2.625994,-7.099662,8.002130,-5.957807,-8.012065,8.332407,-7.095686,6.441285,-2.107481,4.476612,-5.114276,-5.437246,8.138852,-1.684361,-5.329419,2.583030,2.229453,0.355934,-9.063964,-1.673476,-7.029852,-3.390690,2.675046,-2.127179,-4.780494,7.343397,0.467238,8.635897,9.168377,-1.119150,-8.056903,-4.096780,-3.699268,-7.472493,2.302834,0.134590,4.542469,-9.382979,2.118535,-3.734381,-3.080453,-1.054289,3.359200,-8.497470,5.487552,8.323611,-4.222514,7.747695,1.032923,-6.024623,4.370745,-7.518774,3.197306,7.930805,6.655158,-6.085304,8.141874,-1.340381,-0.043367,-3.784503,3.361616,6.969369,1.279800,-6.563954,0.477205,6.996887,-7.843544,3.365117,-2.165853,-8.148316,-2.365299,1.596030,1.122339,-6.227264,1.508296,5.880156,-1.013130,-5.236064,-0.350720,5.749142,8.087792,-9.110532,-6.275991,5.855634,-7.261479,7.372864,-4.424099,-3.739593,-0.107502,1.493111,1.332645,-5.329095,-5.132647,5.104655,-0.354454,-9.212676,0.161311,0.877693,-9.337968,-7.528019,0.895917,9.106622,1.896523,8.351034,-4.481114,8.530951,-6.560037,-8.604633,-5.193970,0.085136,-0.608475,8.106960,-2.819181,7.913537,1.021987,4.904112,5.727306,3.075893,-7.425587,-6.045789,9.375618,7.015382,-1.482486,-2.736126,7.994538,5.836647,1.285867,-7.944687,6.520008,-4.853009,3.556403,6.258564,-2.920737,7.283269,-0.270527,-8.065928,2.620871,3.588759,1.828178,0.388718,2.961132,-6.007314,3.196274,-8.637559,-5.706776,8.895748,-3.059785,4.419207,6.424193,2.473200,-5.336887,-2.720718,0.755576,9.571814,7.014002,-3.489171,0.648939,-6.679596,2.643843,-8.859207,5.824731,4.941351,-3.743258,4.501951,-1.427684,8.011699,-6.299349,-5.878805,6.552964,-5.675261,-2.574675,9.454088,2.321244,-0.489906,-7.600349,-0.297873,1.780467,9.849796,-9.284583,6.204782,-4.039963,-8.802936,-6.726059,-5.426417,-8.720304,3.512408,0.747027,0.709381,-6.257606,4.214289,-8.880447,-4.825697,-4.249327,9.997032,-6.630417,4.680374,-2.269440,0.984367,-0.851829,-0.863476,-5.129430,-1.027328,7.159949,-9.134500,1.981337,-4.429782,-6.937556,8.525884,0.837941,0.537292,-3.217483,-1.041286,-0.931447,5.238497,3.172867,-2.194347,7.945915,-8.624060,-1.616942,-7.455771,-2.393180,3.354309,-0.029979,8.967013,9.438947,4.922542,9.046558,-8.027789,-0.336691,8.167398,-2.514597,2.373624,-1.891853,-9.699815,4.939932,-0.657409,3.569377,-6.727434,9.275248,2.575913,-3.688260,-9.486430,-8.976719,-8.476439,-2.362609,4.421926,1.045300,9.520826,-6.496740,-0.068381,-2.636838,2.776902,-5.301139,3.617244,-7.829114,-5.148667,-9.092412,-3.871938,-4.437471,9.726241,-5.667974,4.709749,1.727033,8.307274,-6.140769,5.049789,2.295829,-4.764487,-1.270736,2.498627,1.844444,-0.453692,-6.158569,-0.302245,4.163837,9.043076,-5.672042,6.200493,5.514471,3.115196,-1.452441,7.829919,-0.810452,1.403323,6.862535,8.621098,-1.019521,-8.534152,-0.883637,7.720621,-7.511980,-7.158356,1.913003,3.249749,-1.421449,-9.884646,5.172468,-1.194699,-8.628962,0.071881,-3.410455,-0.288047,-6.621159,0.391370,4.417085,-1.135502,-1.183996,7.802029,-5.907891,-8.708607,2.074318,5.446757,-4.220288,-8.741962,3.154746,1.687675,-5.412286,-6.328617,-2.268119,-7.394382,0.235401,-9.087146,6.705245,6.241484,-3.533387,-8.273052,2.082679,-7.845297,-8.156333,-0.600290,-0.810020,9.173471,8.048616,0.786744,-2.425052,9.205602,-7.232442,6.086353,9.814686,8.237960,-8.513041,-2.025745,8.874504,-3.268956,3.252975,3.820736,-1.240266,3.801709,5.408294,3.234267,-6.853639,9.559924,-4.860545,-7.594526,4.041231,6.257534,2.285927,8.700577,7.169593,-0.358532,-7.095928,-1.449114,1.691860,-3.453540,4.674220,-7.640405,6.400012,-1.217454,-1.708130,9.351613,9.915990,7.331877,-8.336154,4.772753,-8.607623,1.088764,-2.059022,4.213736,2.511919,-4.810339,-8.623252,-4.896142,-3.611197,4.175029,9.856230,-2.767823,-4.638944,8.695613,0.806360,-2.564344,6.698608,-0.800149,5.244749,3.992955,-9.051006,9.549746,-1.290260,-9.173553,1.139879,6.557522,-9.566874,8.811274,9.666600,-8.653173,4.046762,7.187403,-5.602904,-7.666387,5.543721,-3.103867,5.142716,-0.897423,2.174530,-1.029841,7.330677,3.751027,-9.958620,-1.335584,0.743716,-9.833193,7.365946,7.783981,9.677471,0.294673,3.116690,-3.627163,-6.306553,-4.439500,9.914616,-7.828161,-2.408496,6.846267,-9.251568,5.471222,-1.075722,-3.148792,4.021902,0.151865,-5.912213,9.480395,-5.427002,-1.110905,5.306210,-9.937453,-7.026956,7.339678,-4.447718,1.657354,-6.816359,-8.759094,-1.461908,-2.644786,3.620570,-1.502180,-6.202255,2.582010,-1.482317,7.769594,1.716861,-8.404362,-5.132311,-6.340905,-5.366394,7.166956,-5.214954,6.114894,2.284530,-3.761655,6.872787,-0.503544,2.419404,-8.492877,4.078610,2.492207,1.343074,-1.104735,4.664414,-0.009931,-2.950022,-0.362251,-3.654790,6.507247,0.939133,-1.300984,6.916902,-6.567966,-4.244163,-7.603691,9.243909,-4.024993,0.729187,-9.260632,-8.943079,6.836141,3.725121,3.801284,4.262022,3.837077,2.066092,-6.445306,-2.733471,0.328137,9.657994,-0.027192,2.029681,-0.967667,-2.621742,5.012267,7.435565,4.217086,-8.361831,-3.796716,-7.262240,-6.839329,7.419469,-6.142792,5.009561,6.383256,1.410708,9.709760,-6.794404,8.333078,9.652720,2.541818,1.369811,7.002784,-0.036455,-6.347703,7.667435,-9.103889,6.739701,-4.259158,-5.241129,9.284949,7.698668,-4.414298,-1.394891,-1.609856,-0.014855,3.629092,1.596582,3.482101,-5.357580,-7.893242,-4.474454,6.209010,7.106629,-7.927032,2.293358,8.578971,7.393812,-6.090015,2.289142,7.956255,9.261479,-8.597525,4.559010,-2.712571,1.617504,5.555621,2.184311,6.124955,-6.647340,-9.053449,4.550648,-3.748668,6.419374,2.074492,-6.802164,-0.077075,3.313750,-1.181305,-1.977909,-0.643481,3.136454,6.746335,-3.097644,7.147479,-2.927108,-7.021585,6.246778,-6.984807,-7.245340,7.490231,-9.768258,-5.175374,-6.948439,-3.544078,0.270883,-3.496528,-9.838875,2.954347,-6.715445,3.246281,-8.135637,5.951047,2.595828,-9.415237,9.179448,-7.507069,2.905990,4.209197,6.734026,-9.991405,-0.945959,7.476909,-4.846084,-0.953093,8.646026,0.233466,9.584961,1.525001,9.647513,-5.849449,2.338122,-1.727333,4.457828,4.284309,-7.478167,5.446687,-9.618484,0.699868,5.205333,-2.816960,-2.530774,-2.939322,-7.209225,-5.141197,6.094896,-8.210322,7.401640,6.924154,-2.678007,2.291102,-7.729591,8.747462,3.049206,2.620561,-1.282808,1.078036,-6.912366,8.683048,6.384615,-8.192140,-7.438721,7.397640,9.454031,9.513556,3.087635,-1.348041,5.280166,1.462139,2.146204,-1.001551,-2.730814,-3.978423,5.172139,6.079737,7.352162,-5.531477,-0.706567,1.829944,-8.047927], dtype = "float32")#candidate|4742|(770,)|const|float32
const_4743 = relay.const([-6.517310,0.801693,3.258956,-4.004193,7.980153,0.924980,5.832461,4.366441,6.438154,-5.316947,-4.444985,8.643444,4.413107,-6.048428,-0.944679,-9.650233,1.077330,-0.261953,-4.726810,-9.465756,7.749850,7.014265,-0.775198,4.423085,4.528085,1.716924,-0.133554,5.703550,3.272655,-2.310985,9.892948,-0.344891,-5.491665,6.776452,5.831341,-1.034914,5.152307,-5.413692,-8.854321,8.493771,4.033196,-0.483191,-2.893949,2.716862,3.400723,3.357482,7.242444,6.918336,-7.779798,-1.740842,-6.727104,-8.317071,1.660060,-7.886363,-0.476540,6.348787,-1.175367,4.433224,-0.038771,-4.222356,-9.076974,-3.795432,9.620731,5.930583,8.230144,-1.834619,9.954692,3.742566,4.845371,-6.325784,-3.897167,4.803415,0.920425,8.991066,-0.712934,-1.138889,0.206600,-2.016907,-5.506278,-7.320850,7.354570,-4.007091,3.188709,0.382557,1.472471,-2.178085,-8.235919,-9.504920,-1.962033,8.249173,-9.411139,1.052114,-8.239636,-5.308704,8.353130,-7.326695,4.789716,7.850471,7.335752,6.110380,7.974716,-5.225279,-6.457405,5.341019,-8.670478,4.947252,-4.669240,-7.221681,-7.666308,-8.095743,6.944728,-1.505446,2.585058,2.716280,1.211969,1.474405,-5.997349,-9.285881,-5.110495,0.729913,-5.025611,9.719274,1.428826,4.365147,8.725326,5.591911,0.637579,8.126350,-8.803274,1.555171,-7.610941,-3.253799,-4.060077,7.950942,-4.671402,0.224677,3.759383,-9.687479,-7.583538,-6.751171,7.579931,-2.704198,0.540624,3.977173,-2.130848,6.109019,7.392539,8.318879,-3.544192,-4.416242,1.695066,9.844575,1.340857,9.445798,-1.826718,1.534193,5.964651,-1.650221,8.936487,-2.837105,-0.872202,-7.416082,1.623074,1.641729,-3.853985,8.397684,5.568118,-7.300417,-7.782178,-2.009861,4.958107,-3.626216,9.016217,-9.136096,-2.426329,-0.315966,-4.080691,-4.201901,-2.883709,-0.223247,9.563902,-4.048563,-9.235368,2.403211,-5.086935,8.957074,2.424103,-2.011802,-4.791976,-4.574624,-4.772907,1.881117,6.766013,-2.719830,0.666732,8.072935,-8.255032,2.089711,-8.533673,7.912541,-6.923552,5.157098,-5.478374,-1.030501,-6.849799,0.848868,2.962759,1.182555,-5.406099,-5.618046,-9.501409,3.342122,4.540897,-7.691024,9.565132,-2.983337,-0.602530,-8.991011,-0.070253,-6.544724,9.923167,7.552556,-4.725015,9.190529,-3.463335,9.987239,7.772867,-3.272928,5.261420,7.632425,-6.422302,1.467992,4.017391,-8.696452,-4.220978,-3.408827,-5.000737,9.840501,-6.144281,-6.113255,-0.571648,-9.875433,-7.972564,5.943857,6.441168,-3.982110,-2.915907,-2.566387,9.494605,2.879221,3.888990,2.185438,3.223407,6.812075,-0.045758,5.752743,4.139694,-3.627355,-3.746626,8.983939,-7.775809,8.496641,3.825535,-3.755822,-5.422685,4.627751,5.165750,-9.551605,0.455963,5.318248,9.309728,-0.597424,-9.777889,-7.128483,-5.659529,-2.139568,7.820520,-2.652094,1.140647,-1.337737,-5.592224,-8.363608,-7.356614,8.387285,-4.866115,2.844868,4.224065,-3.789339,8.595609,-0.056426,-3.655030,-0.850186,-0.570263,9.487206,-5.605073,-7.105732,2.138252,-4.473289,3.154930,7.855124,-9.477080,2.659350,-6.042214,2.255616,-5.267136,-9.922115,-9.587927,-5.002825,7.180565,9.286495,0.625021,-4.047319,-7.003096,1.363987,-7.408032,3.097256,0.469844,-7.367645,-0.739498,4.410472,3.468931,7.205024,8.082062,5.416424,4.201795,-0.077747,-6.588652,5.289959,5.775165,-2.707238,5.243016,3.610456,-1.978687,4.642178,0.504730,4.694041], dtype = "float32")#candidate|4743|(336,)|const|float32
call_4741 = relay.TupleGetItem(func_1981_call(relay.reshape(const_4742.astype('float32'), [11, 14, 5]), relay.reshape(const_4743.astype('float32'), [336,]), ), 4)
call_4744 = relay.TupleGetItem(func_1985_call(relay.reshape(const_4742.astype('float32'), [11, 14, 5]), relay.reshape(const_4743.astype('float32'), [336,]), ), 4)
output = relay.Tuple([bop_4701,uop_4707,call_4741,const_4742,const_4743,])
output2 = relay.Tuple([bop_4701,uop_4707,call_4744,const_4742,const_4743,])
func_4745 = relay.Function([var_4699,], output)
mod['func_4745'] = func_4745
mod = relay.transform.InferType()(mod)
mutated_mod['func_4745'] = func_4745
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4746 = relay.var("var_4746", dtype = "uint64", shape = (13, 13, 11))#candidate|4746|(13, 13, 11)|var|uint64
func_4745_call = mutated_mod.get_global_var('func_4745')
call_4747 = func_4745_call(var_4746)
output = call_4747
func_4748 = relay.Function([var_4746], output)
mutated_mod['func_4748'] = func_4748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3966_call = mod.get_global_var('func_3966')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_4842 = relay.TupleGetItem(func_3966_call(), 0)
call_4843 = relay.TupleGetItem(func_3967_call(), 0)
func_2851_call = mod.get_global_var('func_2851')
func_2855_call = mutated_mod.get_global_var('func_2855')
const_4851 = relay.const([-9,-4,-9,-9,-9,-2,-8,2,-2,-2,3,-9,-8,5,9,2,4,-9,2,5,-10,-4,7,-10,10,5,8,4,-4,5,-2,1,2,-10,-7,6,2,-8,7,-8,-9,-2,7,-2,-4,6,3,1,-5,-2,4,2,9,4,9,4], dtype = "int8")#candidate|4851|(56,)|const|int8
const_4852 = relay.const([9.206723,8.062136,-8.569299,-8.159687,-5.349258,-1.842723,-5.448977,-2.319982,-3.493938,-6.542943,-0.651792,6.128695,-3.480666,-8.396461,-8.212948,0.617553,8.582491,7.590008,2.704906,-9.405747,3.313644,7.465747,-1.640652,6.383629,3.433769,-5.212489,2.123034,2.661372,8.879159,5.529187,-1.842215,2.015672,9.332324,0.943941,-6.832148,5.538877,-0.437966,3.576259,-2.662649,-3.794491,2.004792,5.811365,-4.357855,-8.937343,-3.736108,7.674002,0.752441,3.552242,-5.487736,3.775118,-4.347700,-3.781293,-9.581498,-8.557289,-6.482224,-3.079059,1.807680,1.655994,-7.283220,8.812658,8.914800,0.313994,9.250266,-7.543935,-2.153412,6.848913,-0.004179,2.494470,5.791439,5.132482,-0.445508,3.511379,4.961106,8.947484,0.891566,-4.663323,-4.079127,3.319328,-9.356030,0.266483,3.574009,-3.510095,-9.436962,-4.545001,0.732776,-3.264173,-7.095263,5.131660,-5.701824,5.177032,-7.895219,-5.633656,-9.611966,-1.285338,2.341422,0.121759,-2.601086,-7.946723,8.582647,3.873511,-7.289305,9.841654,0.184649,-7.893696,3.868387,3.314137,-3.111627,-2.767732,1.569786,3.124325,-0.435723,-4.482724,-2.997013,-7.397987,6.152565,-7.378070,1.348324,-2.746758,4.502893,-3.106219,1.967294,-7.266263,8.592974,-1.557989,5.544028,-1.587863,-6.528591,9.898799,0.489430,-0.385875,6.476438,7.956522,-2.008206,4.121411,-9.617505,9.188605,-2.989069,6.790197,-6.185338,-0.212457,-0.643498,-4.515374,8.713402,3.977451,8.835787,-8.284839,9.518649,8.056498,2.200278,4.782211,-0.100959,9.182326,-0.273102,-3.169455,-7.951743,-2.496045,8.494698,3.247630,-0.975506,-4.121508,2.055984,-7.481281,-2.549538,-1.152991,2.902532,0.429150,-5.161095,-6.072189,-6.263824,-9.427539,0.852027,5.943910,8.638974,-6.437868,4.943869,1.150093,0.711337,8.609220,1.199588,7.394205,2.223467,-0.870801,-4.569045,-5.986637,5.445649,0.840598,-9.076435,-0.745866,-0.914876,4.328134,7.247568,-0.929794,2.242524,-0.854245,1.713700,6.707578,-3.932955,7.912112,-4.109863,8.214870,-8.028696,-5.205647,6.486457,-7.334736,1.383209,-6.226602,-7.337710,2.531028,-2.788768,-8.125201,-6.215842,4.056775,7.958562,4.594077,-7.763915,8.063010,6.859654,0.118270,-5.793207,-1.092665,-8.286517,-9.262068,8.138383,-0.314027,5.234636,-8.669747,-9.062813,1.793960,-3.529376,8.299782,7.208767,5.555291,-3.426115,-7.624577,-4.700698,7.315239,7.311821,9.099262,1.926237,-4.420068,-9.542023,-7.978959,-4.179595,-4.893685,-6.716063,-0.765609,-1.462457,5.107717,-4.248333,-2.208068,-5.218871,5.764704,1.210019,2.590885,-5.852074,-8.929709,-8.567536,2.218555,-6.525115,3.659664,6.453130,-7.972214,6.024834,4.162917,8.415722,-3.176153,8.235757,3.107997,-0.972882,4.722335,7.269631,4.682518,4.962939,-7.601975,-2.601626,-4.950741,7.118579,5.370445,-3.330461,0.507960,-1.378460,-0.383985,5.575053,6.859475,-7.528837,2.546726,-2.538034,7.706229,7.059898,5.128970,1.335699,-2.881407,-9.969280,7.547036,-5.628107,6.905215,-9.724002,-6.674715,6.194089,4.405229,-8.021162,9.155869,7.276251,-0.676212,9.719185,-2.941674,-8.486022,0.870348,-8.708157,0.098031,4.628919,-7.490493,-2.505828,-3.136222,-7.463872,1.134319,-0.626693,3.350395,8.421617,-8.787273,1.955313,2.591826,9.909812,-3.213729,0.516059,-9.776395,-5.479760,-2.418957,5.159928,0.581229,-1.825194,5.790997,9.494798,-3.224403,-3.920795,0.334489], dtype = "float32")#candidate|4852|(336,)|const|float32
const_4853 = relay.const([-9.003686,1.593372,-6.100378,-3.637951,-2.928194,6.577908,4.914470,4.155986,-8.302712,-9.471824,8.617484,-5.489512,-4.561052,6.570002,9.357345,-7.694536,-4.783086,0.403309,-8.228805,-6.219635,1.153359,-8.080222,-7.973323,-5.721119,-6.135104,-5.078178,-3.196683,-1.561847,3.708685,-7.129134,-6.002023,-0.957711,-0.341837,5.038245,0.454774,2.380791,-7.589642,-6.212294,2.555220,3.928852,4.263314,0.186220,-3.149053,-6.022710,8.345106,-5.014322,-3.288057,7.066009,9.955816,8.433935,-9.240756,4.559345,-4.525915,7.747476,-5.160517,-1.721418,-9.838055,0.537243,3.135028,-5.925945,6.164856,-5.036625,8.129903,-2.237811,6.586601,-4.653148,7.669082,-2.057491,4.690891,0.061752,-6.207540,6.706826,-2.211130,7.691143,2.375864,-4.235617,0.256642,-0.417007,-9.008917,7.710008,-4.518937,2.112005,7.180627,4.729695,8.622447,-8.765521,-3.403741,2.891188,3.929827,-4.704764,-2.977726,5.157970,-4.485312,5.796740,-3.891114,-4.698904,-2.362925,-0.319064,2.661696,-8.805472,9.479913,-9.124881,-9.963444,-2.367599,-5.980165,-6.993586,8.124361,-5.571592,2.583038,9.924707,-2.098331,-3.050744,5.172506,-9.799348,2.478557,-1.965678,-4.242667,-3.554056,-6.796099,-4.039515,-7.835406,4.875748,-0.405028,0.347578,0.262786,4.578352,-3.036581,-7.583529,6.962447,-7.271351,7.828640,9.615635,2.072664,6.119577,-8.927763,-0.938092,-6.708632,-7.904409,-6.703706,4.903289,-0.229432,0.458697,-2.338817,0.123028,1.301694,-9.678970,-5.345695,-5.096125,-7.413703,2.204336,7.371064,9.536814,9.617365,-2.972405,1.848400,-8.227547,-3.871129,-8.870688,7.932902,-4.159520,0.846107,-4.555061,-3.260559,1.551622,-9.587578,3.718524,-8.326103,1.078402,7.970725,2.293606,8.675752,-4.226529,-3.365625,3.149103,-9.265923,-9.940350,-0.846716,7.081725,8.451157,9.411294,4.178265,8.464003,3.434861,-5.821387,-3.690242,6.562949,5.077651,0.400859,-8.446022,8.847515,1.645463,-0.585106,-7.257095,-4.055189,-4.661581,9.159742,9.638450,-8.063867,-0.104592,7.548402,-8.900773,-8.903944,-5.137392,0.126287,-3.913465,-5.351890,-0.706069,-9.356073,-5.367780,-0.128487,-0.460285,8.889365,-5.986252,9.208214,-6.793614,6.716040,1.779172,-4.817996,-4.810245,0.855625,-1.823172,-5.663764,-0.694614,-7.989896,4.906351,-0.394649,-7.769126,6.247810,4.111580,5.636486,0.072819,-7.233657,6.198592,1.532935,5.820921,-5.890695,-5.800842,-0.165291,3.990683,8.554088,-8.320883,5.760669,8.764791,9.911543,8.090596,-1.974153,-9.864881,8.224090,3.429653,3.324969,0.265320,7.237637,-4.307203,3.210884,-5.668380,-6.044988,-5.650982,5.400451,6.459064,-8.206169,-7.383426,7.081279,7.608272,-0.748603,0.082237,5.181477,6.380062,-0.824581,3.254291,-6.171956,4.053141,-5.764793,-2.545102,6.327323,-3.995174,-5.392940,9.280023,3.785831,-4.576421,0.239922,2.013823,6.626938,9.993200,-2.266078,0.219967,-6.733621,-7.372125,-7.538797,4.214314,-2.955164,9.921288,-6.608754,-3.916269,5.430389,2.284554,5.384604,-2.405374,5.851462,-2.701627,-3.575751,-2.455075,-7.574881,1.915053,8.699633,6.609340,-3.677545,-5.427664,5.046013,9.780939,-4.038303,7.677452,2.030582,-2.367039,-9.778280,5.127890,-9.259900,4.129097,-1.100493,0.755405,7.938899,5.772226,2.840273,-1.461523,-2.789197,2.542447,-0.460170,-3.580439,-3.789887,4.468257,-4.657183,1.296400,-4.503070,1.869973,0.563216,4.390845,8.048094,9.495667,-1.248269,1.130997,4.679850,1.503042,-6.804658,9.105323,-4.212126,2.404678,6.318729,7.793672,4.175214,-3.750493,5.223235,-3.420835,-4.700388,3.261043,6.395598,-3.895217,-6.998248,5.549943,3.429041,4.440996,8.819718,-0.419729,-6.192657,-4.983610,0.686686,-0.420144,-8.228711,5.000046,-1.433715,-1.193182,-5.055353,-1.398832,-8.505080,5.211832,8.112605,-9.821813,6.560941,9.170541,-1.857876,1.267153,6.022396,1.221085,-6.484652,-0.199333,0.679468,6.371084,2.724502,-7.529683,3.823992,-7.684988,6.770938,7.697824,5.488631,-3.921042,-0.583637,0.237597,1.676106,-7.818421,-5.865302,9.451625,2.869406,5.682456,-9.159865,-3.531066,1.787869,-1.276650,0.798586,6.294029,3.190434,7.538387,1.486609,8.893754,4.343816,7.230019,-4.310217,6.691361,8.503595,6.369960,4.895894,2.046545,-7.132976,6.817009,7.297754,-4.175235,-1.105233,-8.804407,2.549291,-8.806256,9.253192,-3.760600,-5.898648,2.973221,-2.717293,-3.844453,5.187906,-5.075483,0.642820,7.491330,-9.790568,2.144058,6.365865,-5.042169,4.561712,8.649639,-2.162670,8.420624,-1.434557,-1.981595,5.122515,-6.175687,-0.437768,-4.323433,-5.063710,-6.819492,3.866107,3.963877,-2.122184,9.150105,-8.486948,-2.941477,-9.342367,-9.967402,3.109085,7.610888,0.130349,7.717712,-8.968737,4.830328,7.394617,4.905688,-4.626338,-5.168530,1.018122,-6.040243,-2.868424,-7.049048,-6.726328,5.885715,-6.080104,-4.652158,-5.380419,5.220100,0.873394,3.344685,0.958991,-3.276092,4.653686,-0.948374,-8.051866,2.563337,4.279555,-1.723784,-9.045570,6.701540,-1.759559,-9.330696,0.843233,-6.654565,-9.224740,-0.430264,-9.172313,6.198146,0.082700,-1.725934,4.406653,-9.217956,-1.927230,-7.485151,9.714949,0.190422,-3.145714,-9.720013,3.186662,-5.435152,9.906277,5.603371,4.067388,5.403629,-5.584972,3.007796,9.947024,4.080301,-4.573908,-8.420508,9.058809,2.242623,1.305817,-0.681723,-9.040798,9.419689,9.832225,-8.910899,4.058376,8.754238,5.189025,6.081922,-7.237017,-9.551963,5.143348,-2.322648,-2.645204,-7.685928,-1.635537,9.938345,2.915353,-5.816265,4.782772,-8.794873,-3.563167,8.663627,-5.430313,5.466988,0.273935,2.547742,-8.259442,0.736927,4.630465,2.017852,-8.996188,5.087997,2.102094,-9.365163,-1.574865,1.842767,-6.742674,-6.727600,-6.294524,-3.135095,-6.541858,-2.119533,9.379594,5.875396,5.305923,-1.034198,7.596234,0.380313,9.013307,-8.463323,-2.177425,4.109767,-8.113711,4.298605,6.774102,-8.615832,5.301073,-5.772704,-3.847282,-4.961958,-3.074777,-4.519810,-5.857396,-7.027101,9.224076,7.122787,1.924699,3.757413,-3.472181,-7.751923,-7.849011,0.797579,7.772828,-5.197538,-2.051894,2.506180,-8.466053,-7.148591,3.472956,-1.332714,0.704102,4.074757,-0.960633,-7.591041,3.352951,-3.552321,1.460476,-8.462722,-2.415699], dtype = "float64")#candidate|4853|(616,)|const|float64
call_4850 = relay.TupleGetItem(func_2851_call(relay.reshape(const_4851.astype('int8'), [56,]), relay.reshape(const_4852.astype('float32'), [168, 2]), relay.reshape(const_4853.astype('float64'), [11, 7, 8]), ), 7)
call_4854 = relay.TupleGetItem(func_2855_call(relay.reshape(const_4851.astype('int8'), [56,]), relay.reshape(const_4852.astype('float32'), [168, 2]), relay.reshape(const_4853.astype('float64'), [11, 7, 8]), ), 7)
func_1888_call = mod.get_global_var('func_1888')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_4861 = relay.TupleGetItem(func_1888_call(), 0)
call_4862 = relay.TupleGetItem(func_1890_call(), 0)
output = relay.Tuple([call_4842,call_4850,const_4851,const_4852,const_4853,call_4861,])
output2 = relay.Tuple([call_4843,call_4854,const_4851,const_4852,const_4853,call_4862,])
func_4863 = relay.Function([], output)
mod['func_4863'] = func_4863
mod = relay.transform.InferType()(mod)
mutated_mod['func_4863'] = func_4863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4863_call = mutated_mod.get_global_var('func_4863')
call_4864 = func_4863_call()
output = call_4864
func_4865 = relay.Function([], output)
mutated_mod['func_4865'] = func_4865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_4917 = func_1716_call()
call_4918 = func_1716_call()
func_2109_call = mod.get_global_var('func_2109')
func_2112_call = mutated_mod.get_global_var('func_2112')
var_4934 = relay.var("var_4934", dtype = "float64", shape = (20,))#candidate|4934|(20,)|var|float64
call_4933 = func_2109_call(relay.reshape(var_4934.astype('float64'), [1, 10, 2]))
call_4935 = func_2109_call(relay.reshape(var_4934.astype('float64'), [1, 10, 2]))
output = relay.Tuple([call_4917,call_4933,var_4934,])
output2 = relay.Tuple([call_4918,call_4935,var_4934,])
func_4939 = relay.Function([var_4934,], output)
mod['func_4939'] = func_4939
mod = relay.transform.InferType()(mod)
var_4940 = relay.var("var_4940", dtype = "float64", shape = (20,))#candidate|4940|(20,)|var|float64
output = func_4939(var_4940)
func_4941 = relay.Function([var_4940], output)
mutated_mod['func_4941'] = func_4941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4682_call = mod.get_global_var('func_4682')
func_4684_call = mutated_mod.get_global_var('func_4684')
call_5009 = func_4682_call()
call_5010 = func_4682_call()
output = relay.Tuple([call_5009,])
output2 = relay.Tuple([call_5010,])
func_5014 = relay.Function([], output)
mod['func_5014'] = func_5014
mod = relay.transform.InferType()(mod)
output = func_5014()
func_5015 = relay.Function([], output)
mutated_mod['func_5015'] = func_5015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4619_call = mod.get_global_var('func_4619')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_5049 = func_4619_call()
call_5050 = func_4619_call()
var_5064 = relay.var("var_5064", dtype = "float64", shape = (6, 15, 9))#candidate|5064|(6, 15, 9)|var|float64
bop_5065 = relay.bitwise_and(call_5049.astype('int8'), relay.reshape(var_5064.astype('int8'), relay.shape_of(call_5049))) # shape=(6, 15, 9)
bop_5068 = relay.bitwise_and(call_5050.astype('int8'), relay.reshape(var_5064.astype('int8'), relay.shape_of(call_5050))) # shape=(6, 15, 9)
func_2410_call = mod.get_global_var('func_2410')
func_2413_call = mutated_mod.get_global_var('func_2413')
const_5070 = relay.const([-1.087457,4.670620,-3.714241,-8.646449,7.562066,-0.223083,-4.286615,2.304419,8.984717,-6.265385,4.596340,-4.706577,-2.574207,3.155440,-7.115327,3.161160,7.622193,6.142180,0.223030,3.765296,-0.138661,-6.793591,-9.922224,6.296759,4.217270,-6.379375,-1.004653,-8.312405,9.557671,-2.186436,2.087523,0.903642,5.362048,-1.594343,-4.739155,1.720416,3.320150,2.820343,-5.628736,0.358599,-2.838837,-2.701264,0.093572,6.050301,-2.592711,-3.734204,4.836055,-4.379890,-5.447518,7.183818,-7.516623,9.798577,-2.862728,6.539776,0.328052,-4.147392,-9.902095,-7.459907,-6.033655,-9.746609,3.248877,-3.179063,-7.849561,2.160548,4.334747,1.012078,-0.664054,-2.313979,5.461144,7.004307,-4.993959,-6.269418,-6.345831,-4.423326,-3.368942,6.757040,2.164468,-0.820458,-4.142263,-7.803914,9.564124,2.660577,-6.778989,-0.816288,4.323216,-3.505624,-0.743253,-3.725816,2.091008,7.457527,9.182087,-9.034511,-8.426343,5.730647,-2.212234,-4.543221,0.773128,6.444842,0.121423,-1.628276,8.027326,3.282780,2.190651,-4.871890,-3.772453,5.760304,-9.342465,9.096324,-0.115011,2.786657,-4.373282,-9.308277,1.993886,-3.877071,-7.680303,6.073964,0.175856,6.974165,-4.863995,-2.187722,6.834683,3.447561,1.962508,-7.238202,2.703640,-3.109190,7.630122,5.809298,5.097804,-8.990421,-1.377740,4.727861,-9.144478,2.964209,8.973666,2.384706,2.517253,-7.410917,2.793887,-7.889818,6.180248,4.541498,-6.828600,3.674422,-6.255990,2.723752,-8.927423,-1.753777,5.535956,0.977560,9.259679,9.529844,7.935577,2.143925,-6.921386,7.043727,6.386273,-0.248331,-6.271687,3.728640,1.818336,8.276604,9.314291,-3.209214,8.970024,5.993047,0.507639,7.660936,3.685648,6.939051,2.409027,5.814678,2.359191,-5.332331,7.427984,-8.487740,-0.442522,-1.398859,-7.277811,-7.908966,8.941480,-0.133975,-2.525846,8.498027,3.858863,5.467400,-5.115107,7.878291,-8.495092,6.531297,1.612850,1.476282,2.279956,1.439395,-1.665928,-2.401656,-2.981493,-0.372706,-4.207898,-6.902132,4.890888,-2.284592,-8.126461,3.853222,5.898842,-9.550151,8.927616,-1.851582,-3.653312,-8.152699,0.015652,-6.396212,8.611328,-2.137668,-9.359196,1.727548,-4.771758,3.138215,1.468925,-2.708391,0.665167,0.341129,-9.824242,-9.801568,-9.453530,6.754707,2.512583,5.008035,1.307051,-6.952454,-2.417774,9.723990,-7.528807,8.799515,1.621074,-7.229857,-2.576618,4.170163,-4.483126,6.595501,-7.688162,-3.427046,-3.432721,0.410934,-1.674991,-8.155781,0.914566,6.869385,-3.796125,-7.768453,-7.477002,5.040365,-1.642796,8.418147,-1.461223,4.070947,-8.628769,-6.879761,6.537799,-1.173512,0.890799,-4.187188,-4.878695,-6.167741,-4.834028,-3.893295,-4.899189,-5.534002,2.147154,3.040385,-6.953646,-8.412365,-9.340952,-7.390565,-1.094105,6.949640,2.770696,0.220215,-4.808159,-2.888601,-4.739706,0.736703,-4.114864,5.537969,-8.989807,5.853704,-8.791594,8.420506,-6.700963,-8.696236,-8.030744,4.405954,-9.035714,5.296525,-3.083190,3.485637,-4.406316,6.682622,-0.472548,-3.462811,4.493525,-6.047142,-2.392272,1.630268,5.356494,6.067563,0.833796,7.315741,5.478308,-5.963556,-8.256222,-4.729626,3.592905,-3.950344,6.249817,-7.380001,-0.334512,-6.374641,-0.206462,-0.523954,3.607773,7.434353,-7.903677,-0.744295,3.591024,2.594041,9.088159,-4.743553,-7.196696,-8.570218,-1.147901,-2.685002,5.497978,1.518892,-4.615304,1.310667,2.722350,3.618761,1.810326,-9.789428,-1.932772,7.984355,7.120896,-9.108459,-2.441575,1.928186,0.203150,2.657131,-7.755017,-9.491273,-9.132699,5.787321,-9.460423,5.695035,-1.235869,-7.914223,-5.115451,-7.070191,-6.476060,2.077835,-2.538863,7.786642,-8.527223,-1.163098,7.777631,-6.488506,8.549022,3.104846,-9.020680,7.948262,-1.599407,8.016482,5.006999,1.102889,0.262113,-8.743322,4.286442,7.379478,6.596695,9.520297,1.279882,-2.652808,0.394185,-2.347220,3.275697,-5.916356,-6.983383,-9.164654,-9.113214,0.984515,-7.250578,7.696318,0.167297,9.863871,-6.610068,9.308605,-0.600787,-2.121475,5.622172,9.159728,5.280458,5.990534,-2.541429,3.362038,1.614226,-0.004150,3.236201,6.453684,-3.765689,2.682112,1.819363,-8.925920,-4.668328,0.591449,-2.234818,-6.494876,5.383839,1.730223,5.530703,-9.996718,3.534246,-8.113272,-2.821754,3.266119,0.360343,4.520285,3.811046,-5.634611,0.980935,8.006307,4.771684,6.089286,8.931428,-7.306602,4.372692,8.174589,3.000621,0.645974,-0.334038,-4.505915,5.740656,-1.882539,-4.155432,3.218877,9.801064,5.917441,-3.035779,3.943811,9.897571,4.702777,-0.102796,9.984232,-4.908503,7.288915,2.334035,-7.638404,7.914479,1.676145,-6.437115,4.012605,0.731141,-9.327573,2.479190,-9.218578,3.318073,-6.716260,-7.277473,1.352713,-7.016550,0.352651,-0.897847,0.765123,7.036216,6.388401,8.106393,2.344184,4.787829,-7.810410,7.666896,9.272824,-0.247121,-3.999494,2.147234,-6.170952,-1.809776,3.595889,0.818033,-4.922516,9.244248,-0.182294,4.573039,-8.260141,6.013197,7.826135,7.408829,5.559535,-7.217695,-4.170933,5.789211,-9.386368,0.725857,5.921740,-3.004908,6.919529,5.309761,-5.902156,9.888682,-5.794375,6.583850,7.060125,-3.011896,8.880202,-0.637467,4.461662,-5.754473,2.685372,8.763926,-3.859926,-0.105886,-5.725634,-6.301549,-6.506204,5.437726,-2.093532,3.751445,6.217816,0.804614,-5.793893,-4.045636,8.277572,9.422235,-5.653003,7.583562,-1.557387,-6.400892,-5.642792,7.989756,-1.583696,0.446423,-0.097550,-8.708063,-4.211722,-4.520718,5.746982,-0.055809,3.462678,6.226828,2.744508,-8.785666,4.018991,-2.771298,9.141207,-0.961020,-1.400479,3.698724,-7.247559,-9.698869,1.089571,-3.506283,0.385003,3.846077,-3.751569,8.378934,-0.189120,-4.653651,-3.332403,3.121172,-1.039785,-4.374630,8.138980,7.972795,9.900153,-4.151667,-7.363907,-5.953549,-0.244686,-6.496115,-4.670628,-3.852475,-2.743308,-0.886526,3.928196,-2.737150,-1.182152,-9.905791,-1.298789,6.203368,3.599832,-4.355175,-8.469376,3.937802,0.188893,-7.596602,5.631865,-3.899058,6.289295,8.969747,-1.193313,-4.882664,-4.530896,-3.003935,2.426994,-8.996798,3.127372,-3.085938,6.842507,-9.264526,-1.442682,2.327040,7.257500,2.213392,-5.407157,5.454716,-7.949056,4.014519,-0.878215,-8.405319,-9.691740,-6.837785,3.760207,9.248215,0.202159,7.963248,-4.175182,9.703630,-7.138652,-9.546313,2.863128,7.609426,-3.059212,-8.637397,-9.047848,-1.500817,-5.511839,3.447783,5.115104,-5.484406,-3.021130,-3.878753,-6.164916,6.987613,-5.990604,-0.779587,9.637938,-7.472110,-3.253991,5.506375,3.760257,4.404341,-9.216177,6.129359,-0.581319,-4.362202,-0.289979,7.228710,2.643774,8.042304,3.283019,9.265207,-4.185210,-5.642055,9.475597,6.723146,5.467282,-5.343630,9.342256,5.825143,6.265723,0.118055,3.873710,9.764370,9.994309,-0.660532,-5.147674,8.029879,1.583869,0.682499,7.987878,6.664120,-1.584055,7.396229,-4.186494,8.494085,-1.167232,1.534188,3.606925,-4.533369,5.863108,4.885666,8.428549,-7.014537,-2.069579,5.565112,9.078124,-2.128246,-3.396515,7.134062,7.102337,-6.478294,3.859609,1.878057,-5.124029,2.160646,-7.317559,3.039516,-0.372209,2.571069,-4.556354,-6.193057,8.494341,4.592882,-5.498257,-3.393853,7.222977,-3.053832,-7.751523,3.142939,3.849832,2.452736,-4.492476,7.840247,-3.084134,2.535466,2.427968,-5.703776,9.551775,-9.102268,5.804529,0.351697,-6.921196,5.811055,4.346477,6.225729,-0.808085,-8.653866,-3.159897,6.560031,-6.595568,5.581738,-3.998955,8.972486,4.314778,-4.947609,-6.870489,4.853873,0.854618,-9.668896,3.156634,1.015783,-1.894819,-1.841840,-0.661342,9.282655,4.872760,-5.615918,4.430589,8.804118,-5.429569,0.764055,6.808772,0.540488,1.381172,1.320773,5.253018,-9.029665,-4.852330,-0.266145,-2.171878,-0.058366,-7.973137], dtype = "float32")#candidate|5070|(770,)|const|float32
call_5069 = func_2410_call(relay.reshape(const_5070.astype('float32'), [11, 14, 5]))
call_5071 = func_2410_call(relay.reshape(const_5070.astype('float32'), [11, 14, 5]))
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_5084 = relay.TupleGetItem(func_3123_call(), 2)
call_5085 = relay.TupleGetItem(func_3124_call(), 2)
func_1888_call = mod.get_global_var('func_1888')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_5086 = relay.TupleGetItem(func_1888_call(), 0)
call_5087 = relay.TupleGetItem(func_1890_call(), 0)
uop_5090 = relay.sigmoid(var_5064.astype('float32')) # shape=(6, 15, 9)
output = relay.Tuple([bop_5065,call_5069,const_5070,call_5084,call_5086,uop_5090,])
output2 = relay.Tuple([bop_5068,call_5071,const_5070,call_5085,call_5087,uop_5090,])
func_5092 = relay.Function([var_5064,], output)
mod['func_5092'] = func_5092
mod = relay.transform.InferType()(mod)
var_5093 = relay.var("var_5093", dtype = "float64", shape = (6, 15, 9))#candidate|5093|(6, 15, 9)|var|float64
output = func_5092(var_5093)
func_5094 = relay.Function([var_5093], output)
mutated_mod['func_5094'] = func_5094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3034_call = mod.get_global_var('func_3034')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_5210 = relay.TupleGetItem(func_3034_call(), 3)
call_5211 = relay.TupleGetItem(func_3035_call(), 3)
func_1756_call = mod.get_global_var('func_1756')
func_1760_call = mutated_mod.get_global_var('func_1760')
var_5213 = relay.var("var_5213", dtype = "float32", shape = (336,))#candidate|5213|(336,)|var|float32
var_5214 = relay.var("var_5214", dtype = "float32", shape = (770,))#candidate|5214|(770,)|var|float32
call_5212 = relay.TupleGetItem(func_1756_call(relay.reshape(var_5213.astype('float32'), [336,]), relay.reshape(var_5214.astype('float32'), [11, 14, 5]), ), 0)
call_5215 = relay.TupleGetItem(func_1760_call(relay.reshape(var_5213.astype('float32'), [336,]), relay.reshape(var_5214.astype('float32'), [11, 14, 5]), ), 0)
uop_5221 = relay.asin(call_5212.astype('float32')) # shape=(7, 12, 4)
uop_5223 = relay.asin(call_5215.astype('float32')) # shape=(7, 12, 4)
func_3606_call = mod.get_global_var('func_3606')
func_3611_call = mutated_mod.get_global_var('func_3611')
var_5230 = relay.var("var_5230", dtype = "uint32", shape = (220,))#candidate|5230|(220,)|var|uint32
call_5229 = relay.TupleGetItem(func_3606_call(relay.reshape(var_5230.astype('uint32'), [2, 10, 11]), relay.reshape(var_5230.astype('uint32'), [2, 10, 11]), relay.reshape(call_5210.astype('int8'), [56,]), relay.reshape(var_5230.astype('uint32'), [2, 10, 11]), ), 3)
call_5231 = relay.TupleGetItem(func_3611_call(relay.reshape(var_5230.astype('uint32'), [2, 10, 11]), relay.reshape(var_5230.astype('uint32'), [2, 10, 11]), relay.reshape(call_5210.astype('int8'), [56,]), relay.reshape(var_5230.astype('uint32'), [2, 10, 11]), ), 3)
output = relay.Tuple([call_5210,var_5213,var_5214,uop_5221,call_5229,var_5230,])
output2 = relay.Tuple([call_5211,var_5213,var_5214,uop_5223,call_5231,var_5230,])
func_5240 = relay.Function([var_5213,var_5214,var_5230,], output)
mod['func_5240'] = func_5240
mod = relay.transform.InferType()(mod)
mutated_mod['func_5240'] = func_5240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5240_call = mutated_mod.get_global_var('func_5240')
var_5242 = relay.var("var_5242", dtype = "float32", shape = (336,))#candidate|5242|(336,)|var|float32
var_5243 = relay.var("var_5243", dtype = "float32", shape = (770,))#candidate|5243|(770,)|var|float32
var_5244 = relay.var("var_5244", dtype = "uint32", shape = (220,))#candidate|5244|(220,)|var|uint32
call_5241 = func_5240_call(var_5242,var_5243,var_5244,)
output = call_5241
func_5245 = relay.Function([var_5242,var_5243,var_5244,], output)
mutated_mod['func_5245'] = func_5245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2382_call = mod.get_global_var('func_2382')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_5269 = relay.TupleGetItem(func_2382_call(), 0)
call_5270 = relay.TupleGetItem(func_2384_call(), 0)
func_2288_call = mod.get_global_var('func_2288')
func_2290_call = mutated_mod.get_global_var('func_2290')
var_5291 = relay.var("var_5291", dtype = "int8", shape = (56,))#candidate|5291|(56,)|var|int8
call_5290 = relay.TupleGetItem(func_2288_call(relay.reshape(var_5291.astype('int8'), [56,])), 1)
call_5292 = relay.TupleGetItem(func_2290_call(relay.reshape(var_5291.astype('int8'), [56,])), 1)
output = relay.Tuple([call_5269,call_5290,var_5291,])
output2 = relay.Tuple([call_5270,call_5292,var_5291,])
func_5312 = relay.Function([var_5291,], output)
mod['func_5312'] = func_5312
mod = relay.transform.InferType()(mod)
mutated_mod['func_5312'] = func_5312
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5313 = relay.var("var_5313", dtype = "int8", shape = (56,))#candidate|5313|(56,)|var|int8
func_5312_call = mutated_mod.get_global_var('func_5312')
call_5314 = func_5312_call(var_5313)
output = call_5314
func_5315 = relay.Function([var_5313], output)
mutated_mod['func_5315'] = func_5315
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5349 = relay.var("var_5349", dtype = "float32", shape = (3, 13, 11))#candidate|5349|(3, 13, 11)|var|float32
var_5350 = relay.var("var_5350", dtype = "float32", shape = (3, 13, 11))#candidate|5350|(3, 13, 11)|var|float32
bop_5351 = relay.minimum(var_5349.astype('float32'), relay.reshape(var_5350.astype('float32'), relay.shape_of(var_5349))) # shape=(3, 13, 11)
output = bop_5351
output2 = bop_5351
func_5362 = relay.Function([var_5349,var_5350,], output)
mod['func_5362'] = func_5362
mod = relay.transform.InferType()(mod)
var_5363 = relay.var("var_5363", dtype = "float32", shape = (3, 13, 11))#candidate|5363|(3, 13, 11)|var|float32
var_5364 = relay.var("var_5364", dtype = "float32", shape = (3, 13, 11))#candidate|5364|(3, 13, 11)|var|float32
output = func_5362(var_5363,var_5364,)
func_5365 = relay.Function([var_5363,var_5364,], output)
mutated_mod['func_5365'] = func_5365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2546_call = mod.get_global_var('func_2546')
func_2547_call = mutated_mod.get_global_var('func_2547')
call_5372 = func_2546_call()
call_5373 = func_2546_call()
output = relay.Tuple([call_5372,])
output2 = relay.Tuple([call_5373,])
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
func_3034_call = mod.get_global_var('func_3034')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_5470 = relay.TupleGetItem(func_3034_call(), 3)
call_5471 = relay.TupleGetItem(func_3035_call(), 3)
func_3804_call = mod.get_global_var('func_3804')
func_3807_call = mutated_mod.get_global_var('func_3807')
const_5487 = relay.const([[-9.836670],[1.067457],[7.723916],[3.402129],[8.086575],[-1.552121],[-9.593935],[-7.033179],[4.899524],[3.403911],[6.870560],[5.781528],[3.320291],[5.410669],[-4.862626],[-3.603024],[4.553211],[-9.742315],[2.951114],[-6.960991],[-6.224818],[-7.422334],[-7.396866],[8.829728],[-6.422094],[1.009689],[-9.420332],[4.412171],[0.004042],[6.369808],[1.031722],[-2.244049],[6.670273],[1.105806],[-9.586067],[0.262133],[-3.263782],[4.116957],[-7.932367],[-5.405819],[9.435263],[5.727843],[6.302713],[-6.788849],[4.652949],[-7.828754],[7.998097],[1.724702],[0.154915],[-1.863775],[-5.603628],[6.756631],[5.380664],[-2.295399],[1.915639],[-8.861243],[-9.144470],[-9.356889],[-2.526488],[8.386845],[-8.353997],[-7.188612],[-6.148220],[5.652050],[-3.224448],[-4.181820],[3.310261],[-2.358764],[-1.286443],[0.965086],[8.054105],[8.657392],[7.312528],[7.380935],[-6.500083],[9.730220],[0.017233],[-1.234109],[3.247290],[1.827145],[9.679519],[0.478342],[7.001698],[7.637224],[-3.726468],[-3.672721],[-6.804119],[7.180376],[0.076632],[-1.802400],[0.755380],[5.612623],[0.297951],[5.818645],[5.510288],[7.352939],[-6.180605],[9.284951],[-4.262274],[5.309243],[7.296194],[-4.434656],[0.023126],[2.029711],[2.905809],[-4.980486],[5.645714],[4.310157],[-2.933707],[-2.189625],[9.637433],[-9.663246],[-8.291926],[-5.251774],[0.128135],[8.158127],[5.789210],[-5.708343],[0.252225],[1.391041],[5.806859],[-2.202428],[8.310699],[-3.150728],[-3.866638],[4.600176],[-2.637157],[3.882474],[-1.751228],[0.026227],[6.843189],[-6.296117],[-2.182235],[-8.498570],[2.917057],[-3.037919],[5.876955],[3.290908],[-5.920681],[-3.633954],[-6.311356],[4.656560],[-2.233126],[2.032095],[-7.676333],[-3.793502],[6.155913],[-4.026928],[9.203165],[-7.156422],[-2.741738],[-7.862008],[6.429996],[0.327570],[1.679735],[-1.402144],[2.806288],[-6.490222],[-9.682858],[-8.292711],[-2.994541],[-8.643442],[-1.272535],[8.321321],[4.340045],[-1.557011],[8.152412],[-8.926670],[-2.539920],[-3.168658],[5.328462],[-8.550109],[-8.754855],[-1.789891],[-3.750848],[8.959844],[4.036221],[4.144257],[-5.672322],[-3.679894],[-5.543582],[-8.941896],[3.977207],[-8.787510],[-0.738073],[4.461498],[4.767503],[-0.393235],[-3.230578],[-8.947469],[-9.374549],[3.057481],[9.270727],[3.636079],[4.504139],[-7.455455],[-6.748175],[6.089590],[4.572133],[5.699271],[1.006796],[1.426010],[-5.077273],[-5.298832],[3.701398],[-0.444000],[1.938668],[9.593569],[-6.096417],[-3.418317],[-6.225641],[3.860799],[2.085242],[-7.109036],[-0.833525],[-7.166971],[-6.505435],[-6.304859],[-5.566567],[9.847723],[3.684591],[5.436761],[1.535601],[2.844871],[8.189896],[-2.175380],[-2.294347],[-9.005509],[-5.949955],[-8.008469],[-7.841871],[-0.764208],[8.783516],[-3.568746],[-4.878255],[2.629860],[2.803630],[-4.583933],[3.784102],[-6.776013],[6.228082],[5.638107],[-3.564689],[-9.335772],[-9.772816],[9.368741],[1.866522],[-0.477389],[-2.105052],[-9.536506],[-3.143626],[-4.777860],[-6.013890],[4.359378],[-1.235522],[-1.363219],[-9.567978],[-5.915372],[0.269123],[9.949081],[7.313113],[5.012121],[9.441589],[2.748789],[-5.816186],[-7.922849],[8.223500],[-8.713013],[1.387274],[-1.916657],[2.813578],[5.553823],[-7.400317],[-8.623107],[-6.347873],[2.754487],[-8.309445],[3.319886],[-2.605303],[2.314713],[-7.656198],[-9.717723],[-3.371181],[-3.239120],[-4.882520],[1.771026],[1.668343],[9.664428],[-1.314508],[-6.024025],[4.999168],[9.926262],[-8.541179],[2.208980],[1.236982],[5.365152],[-0.275962],[-7.325050],[-0.033677],[-7.108228],[7.750556],[-9.347971],[9.532582],[-2.479534],[0.264739],[-1.916694],[-5.067761],[-7.841234],[-7.028418],[-8.605116],[-5.859823],[-5.500679],[4.485208],[9.310093],[4.873063],[-7.528346],[3.409363],[9.168764],[-3.333641],[1.583453],[-0.282761],[-9.653264],[7.435181],[4.029012],[4.562591],[5.559278],[0.845786],[-3.655415],[-1.089404],[-1.461268],[-9.747828],[-9.138817],[2.235749],[-1.991041],[1.809748],[8.230939]], dtype = "float32")#candidate|5487|(336, 1)|const|float32
const_5488 = relay.const([-3.639076,4.281140,-5.008542,3.752126,-5.455341,-9.442377,8.711790,-9.027017,9.450670,-8.451975,-9.794743,-4.052731,-6.055269,-3.766586,5.641760,-1.098969,-6.023243,1.147252,-5.694300,5.983889,5.854074,-9.116976,-1.948300,-7.440697,8.390895,8.744813,6.984509,-1.966273,1.914931,2.417163,-1.115873,9.907097,8.588620,5.780634,6.912600,-9.922201,-7.626144,-2.458000,4.682030,-4.194384,7.005618,0.158528,0.324934,-9.944622,-8.823856,3.384571,0.559522,0.382817,-9.023040,-9.026836,9.475167,-9.716257,5.953444,9.272605,7.661779,-0.465173,2.172313,6.505217,9.348099,8.629672,6.010256,-2.523985,7.250864,-2.593983,-0.288632,-6.899787,3.425871,8.994346,9.069304,-1.506940,-1.934488,0.571073,-8.540594,-4.279661,-8.400269,8.558519,-5.556871,-0.264100,1.298226,9.365080,6.715608,-5.478451,-2.301560,-5.889167,-9.670505,-6.028846,8.105173,-7.803548,-0.546151,2.675347,-5.226447,8.304677,-4.061112,3.622026,-7.627707,2.231163,-0.485603,-4.986239,5.523385,-6.254010,7.715972,-4.214762,-7.663845,-8.758850,7.791121,4.503537,-9.260675,-8.380101,-1.665320,7.717023,4.332233,-2.198588,-1.274896,-8.378666,6.687938,8.148391,-3.146288,1.464694,-3.385713,1.560887,6.415675,2.454928,9.653666,-2.748621,6.855770,-0.708562,-3.486136,-6.692280,-3.282559,-6.808486,1.845219,-8.566915,9.345456,-4.803879,-3.520818,3.234236,-7.271076,7.109856,8.726859,3.598936,8.454779,5.260133,0.500714,-9.622039,-9.844205,1.424003,-1.766771,6.032075,-5.261470,0.541937,-2.229003,-5.694278,-8.475030,-9.985756,-3.465052,-9.214691,-0.927184,1.582511,-3.013493,9.015755,0.883195,-9.499781,-4.860691,7.575010,-2.831393,9.976457,-5.523085,1.849629,-2.062807,-4.130355,-5.706865,-7.426136,-0.522779,-3.047941,-1.196860,2.183873,-0.156316,5.162175,-3.651228,0.460865,-4.645663,2.511883,6.396896,9.910345,-6.414527,-7.307261,-0.236316,9.395847,-3.520950,5.586489,3.383359,-5.659466,6.796153,7.720524,5.988904,-3.199229,3.875816,-4.257978,-0.105120,-4.811604,0.840126,3.265611,-7.880278,-0.744868,-0.139223,0.202245,-6.794403,-9.275304,2.271062,2.984516,-4.802603,-6.416968,4.101056,-0.040811,-1.965494,0.213931,0.047798,-2.791085,6.284132,5.676931,-5.700784,-2.288504,-7.014519,-6.290821,-5.485031,-3.699108,1.982655,-9.128263,1.818241,4.758522,-5.790222,9.223954,2.348025,6.850676,-5.480236,9.385499,8.706673,-4.716513,-4.208897,7.425783,-0.068521,3.338452,3.421205,5.734033,0.883262,-5.696437,8.635687,3.470550,0.148731,5.984155,3.359148,5.643462,-1.920553,7.043483,-3.622395,5.979452,-8.267277,8.493643,9.294996,5.619362,5.976653,-6.218754,0.522284,6.796475,-0.128748,6.884067,9.655435,-4.540562,-9.596135,-2.413394,-9.871954,8.736863,6.014743,-7.974808,1.718391,0.441579,-5.073820,0.390363,8.634760,-8.991690,-4.417615,-3.491687,-2.722893,8.477254,-8.332224,-9.395422,-4.582090,8.114206,-2.201771,-1.815917,0.496887,-2.778722,1.295100,-1.312291,-7.167398,-8.398651,-9.004820,2.638048,3.953286,5.715433,-9.733462,-6.113169,6.479332,-5.984375,-4.908895,-4.409100,-6.641945,1.490557,-4.117018,0.689736,-7.437142,8.411666,-6.598060,-1.681440,-5.916532,3.202943,7.492879,9.328661,7.063152,-6.096763,-6.368097,-0.846984,8.493089,-5.996837,6.111291,-0.804338,1.564282,-4.656888,-0.979589,7.116789,-7.165959,-4.029948,-7.148545,-4.191904,9.165198,9.024015,8.754236,6.440802,8.160597,9.295658,2.203222,7.809881,1.715617,-2.252724,-1.904330,-3.715358,-4.372492,-2.952460,-1.198585,-4.653151,8.550141,8.956081,0.945943,9.447475,-2.652861,5.893053,-1.199403,-0.708814,-9.003503,-2.957755,-2.267208,4.681347,4.086898,-9.258641,5.737541,3.398843,-3.967014,4.956419,0.963757,3.577194,0.046997,0.242412,0.981186,-8.541008,-6.399816,-1.540658,2.165792,4.960697,3.325400,1.069356,1.056072,2.071407,3.101221,0.514549,0.703830,9.295293,-1.109551,-6.131052,-2.743453,3.066292,9.345329,-6.125248,-7.680668,1.789295,7.155550,-6.408794,-4.221215,-2.052408,-0.322917,-1.386045,-2.464287,0.102184,7.576848,-6.033390,-8.061437,-8.029857,4.690106,-6.955955,1.589555,3.455917,-9.280779,1.746486,5.285049,0.764993,0.624718,2.885379,8.672547,-4.400081,2.096496,-1.129168,7.205338,5.911893,9.897036,-0.079315,-9.515036,7.404204,8.556091,7.014458,8.313255,-3.692577,-0.979554,-1.123245,-7.911681,-3.926363,-5.066357,5.922637,-1.755497,-8.846984,6.098289,-6.400978,5.574175,-1.280836,-1.009415,8.212668,-2.093062,-8.797574,-5.487169,-1.293304,-0.142050,-4.612290,-9.552092,-2.593879,-7.559331,-1.580871,7.232066,1.287176,2.119662,8.398373,6.917074,4.352323,-1.935509,5.079636,-1.182012,-0.317262,-7.432446,0.404757,-0.051669,5.444971,8.102223,-5.689383,-3.644203,2.527106,-7.185603,8.760923,9.425663,7.064861,2.909871,-0.287353,8.763492,-4.403733,5.527644,-2.238750,2.108812,8.824887,5.454772,1.385623,9.574220,3.156067,9.385158,-6.509376,6.299313,-0.678378,-3.054660,4.803744,2.830328,6.624602,6.388818,8.187580,-4.542675,0.128508,-6.969426,0.465343,3.056686,7.920065,-2.033957,-7.488915,-9.386295,-9.835845,1.488415,-6.242619,3.090064,-2.759732,0.563553,9.682347,-0.210729,1.247889,3.587829,-2.106842,-2.845920,4.863248,8.745905,-1.431839,-6.877786,-6.499112,-9.225882,8.078944,8.330160,3.500111,5.839870,-1.351125,4.867600,-0.213752,-4.467767,-0.512462,4.570460,6.116019,1.471790,-4.336720,-6.837386,3.324677,9.555814,-2.587773,-3.036032,0.466609,-1.168194,5.132162,9.308426,-9.340136,7.649642,-6.128858,-1.998964,8.424874,-3.512583,-0.013168,3.384715,3.281469,-6.794115,0.829412,4.317489,-2.238906,-6.375173,-0.307457,6.566301,6.159726,1.737285,0.423392,-4.494814,4.170580,-4.736042,3.649880,2.052299,-1.111193,8.409191,9.187629,-9.089747,-6.715239,5.320615,4.609943,-5.391881,3.691004,-2.792300,7.821103,-7.312593,9.912258,-0.225167,-7.087917,-5.332115,0.206975,-0.715209,-5.786302,-5.374288,5.883809,1.410624,5.163319,1.884852,2.215465,7.890995,-9.096711,6.371916,2.569063,6.078474,-4.355054,-4.493787,1.038626,-1.078095,-6.816178,-6.530739,-6.246170,-3.158988,2.861355,6.637758,4.430489,-8.477087,-2.151583,-0.636234,6.938038], dtype = "float64")#candidate|5488|(616,)|const|float64
call_5486 = relay.TupleGetItem(func_3804_call(relay.reshape(const_5487.astype('float32'), [2, 168]), relay.reshape(const_5488.astype('float64'), [616,]), ), 3)
call_5489 = relay.TupleGetItem(func_3807_call(relay.reshape(const_5487.astype('float32'), [2, 168]), relay.reshape(const_5488.astype('float64'), [616,]), ), 3)
output = relay.Tuple([call_5470,call_5486,const_5487,const_5488,])
output2 = relay.Tuple([call_5471,call_5489,const_5487,const_5488,])
func_5492 = relay.Function([], output)
mod['func_5492'] = func_5492
mod = relay.transform.InferType()(mod)
output = func_5492()
func_5493 = relay.Function([], output)
mutated_mod['func_5493'] = func_5493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5014_call = mod.get_global_var('func_5014')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_5494 = relay.TupleGetItem(func_5014_call(), 0)
call_5495 = relay.TupleGetItem(func_5015_call(), 0)
func_4391_call = mod.get_global_var('func_4391')
func_4392_call = mutated_mod.get_global_var('func_4392')
call_5506 = func_4391_call()
call_5507 = func_4391_call()
func_672_call = mod.get_global_var('func_672')
func_676_call = mutated_mod.get_global_var('func_676')
const_5512 = relay.const([[-6,5,-5,10,-2,-1,1,5,-2,-7,8,-8,7,-4,7,1,10,-3,-8,8,3,-10,7,-8,6,2,7,6,-7,-10,-6,-8,-6,1,3,5,1,10,-3,-8,6,-2,9,-9,-10,-1,-2,5,7,4,-7,7,4,-5,8,3,-5,-8,-5,-3,8,1,2,-9,-2,-10,-2,7,4,3,7,-7,1,7,2,2,3,-1,-9,-5,-3,-2,-1,1,2,7,-9,2,-10,7,8,-4,-3,7,5,-7,-4,-5,9,-10,1,-10,4,2,10,7,-1,10,-8,-7,6,5,-4,-7,-6,6,8,8,8,7,-1,6,7,-5,-1,-10,-8,-9,5,5,-4,-9,-7,-4,6,2,6,-9,-2,-8,9,-1,2,9,-7,9,7,6,6,8,-3,-1,-8,4,7,4,1,-10,7,-2,-6,-8,10,9,-3,-2,-7,7,-5,7,2,-5,9,8,7,-2,3,-7,3,-3,-3,5,7,-7,-3,-2,6,-2,3,2,-1,4,-4,9,7,8,-4,-9,-6,-1,9,-8,3,1,-9,7,-7,2,-1,1,-2,5,-1,-6,1,8,3,6,-3,1,9,-9,-8,-8,-3,-7,7,10,-6,-6,4,-6,9,4,-8,5,-2,2,7,-10,-10,-5,9,-6,10,4,8,-4,2,1,2,7,-2,5,-10,10,-2,-8,10,5,-8,5,-9,-6,-6,2,3,-3,8,-4,3,-10,-1,-3,2,3,9,9,9,-2,2,-5,1,2,6,-10,4,-1,6,-7,5,2,10,-3,-7,-5,9,6,8,1,-5,-10,-9,-3,-6,-7,10,7,1,8,7,8,5,-5,-9,-4,5,3,-6,3,7,-3,9,7,-1,9,8,1,-9,-6,-3,5,6,-4,-4,-6,-4,8,-10,5,-9,7,-2,-1,-7,3,9,7,-8,8,5,5,-5,-5,5,6,6,1,4,-1,1,10,-4,5,-8,-5,9,4,-2,-8,-1,-3,10,5,8,-4,1,-8,2,10,6,-5,-5,10,-8,-6,-5,-3,3,-10,5,-7,-9,-5,8,-3,1,1,4,5,2,-10,10,-3,-5,-1,8,-7,5,-9,7,7,-7,4,-2,5,2,-4,-1,5,-1,-6,-6,-5,7,4,-6,-2,3,-4,6,-10,5,9,2,-3,2,-1,4,-9,-10,7,-8,-8,-4,6,2,-8,-2,6,-3,-7,10,-3,-6,7,7,-3,-2,6,5,-8,7,-5,-7,5,10,4,1,-4,10,-6,-7,2,10,-7,-7,2,-5,5,8,9,-3,5,8,3,-5,5,-6,1,-4,-2,7,6,-3,-1,2,-6,-5,-7,4,-3,8,9,6,3,2,10,1,1,-7,-4,4,-4,-5,-4,-2,6,-6,4,-6,-9,-2,10,-4,-9,5,2],[7,10,6,9,-10,7,-1,-5,8,7,-2,-5,-8,-9,-2,-2,-4,1,6,-7,-4,-2,5,-3,-3,5,7,-4,-6,6,2,7,8,-6,-7,-1,-7,-7,2,5,10,3,-10,10,9,-4,-4,5,-8,-6,-3,-5,2,3,1,1,10,9,-10,5,-5,-8,-1,-10,-5,-1,7,-3,9,-3,5,-4,-8,4,3,5,10,8,-8,8,7,6,-7,-3,4,-9,-9,-4,7,3,9,8,3,1,-4,-9,-8,7,3,-2,-5,5,-3,1,9,9,-3,-7,3,-10,-5,-10,-3,10,8,-2,-4,-8,-8,-8,2,4,4,-4,7,4,2,-7,-2,8,1,-4,6,4,1,-10,-9,10,4,-10,9,-3,9,-3,-8,-2,2,-4,8,-2,-9,-3,7,-2,1,-3,6,-1,-7,8,7,4,6,8,7,-4,-4,-7,-4,3,-2,6,-6,3,-1,-1,-10,6,5,1,-3,8,-4,10,5,3,-2,5,6,-3,10,-3,-9,6,4,5,4,7,-10,8,-10,3,10,2,-8,2,1,8,-4,-3,4,8,-3,6,9,9,4,5,-3,-1,4,-1,-9,-4,-5,-3,-6,7,-3,-5,6,6,-9,8,-8,3,4,-8,4,8,-10,8,-2,-7,9,-1,-7,7,-8,6,-3,9,-4,10,8,7,9,-3,-10,7,-2,4,-5,-5,-5,-8,-1,-8,3,-3,6,-8,5,5,2,7,-10,5,-4,-8,-3,-9,-3,-9,5,-7,4,-5,7,-6,-3,2,4,9,-10,-8,3,-7,-4,-5,10,1,7,3,-7,-2,-2,6,-4,5,-3,-6,10,-3,10,3,-9,-2,-10,10,-3,-8,7,-2,-10,-4,10,7,1,-2,7,-9,-2,3,-7,9,-5,7,-2,10,6,5,4,-5,4,-6,-5,-9,9,8,5,7,6,-2,5,-2,-8,8,-9,-6,10,-3,-6,-3,6,-2,1,-1,-5,5,4,10,2,-3,1,-3,-9,10,-1,-4,-4,-8,-6,-2,-3,-1,-4,-9,1,9,-1,-4,1,10,7,-8,8,6,6,-5,4,-4,-8,-7,6,10,-10,-8,8,-2,-9,6,6,-3,1,-9,-5,5,9,2,-10,1,-9,-1,-6,-4,3,4,1,2,-7,-8,6,-6,7,-10,-2,-7,1,-10,10,4,3,5,-7,-7,-9,-7,-8,2,10,-4,-5,5,-10,-5,-10,-6,-8,10,-7,2,-2,1,-9,-9,6,-3,-4,-7,5,5,-2,8,-9,7,-5,-3,5,1,8,-5,1,5,6,8,-5,-7,-3,7,5,-9,5,9,8,6,-10,-10,10,-8,9,-8,-8,-1,1,-2,-4,-9,5,-8,10,8,-6,-2,-4,-5,-8,-7,-9,7,6,8,-2,-8,-7,-9,2,-8]], dtype = "int32")#candidate|5512|(2, 528)|const|int32
call_5511 = relay.TupleGetItem(func_672_call(relay.reshape(const_5512.astype('int32'), [11, 8, 12]), relay.reshape(const_5512.astype('int32'), [11, 8, 12]), ), 2)
call_5513 = relay.TupleGetItem(func_676_call(relay.reshape(const_5512.astype('int32'), [11, 8, 12]), relay.reshape(const_5512.astype('int32'), [11, 8, 12]), ), 2)
func_3919_call = mod.get_global_var('func_3919')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_5534 = relay.TupleGetItem(func_3919_call(), 0)
call_5535 = relay.TupleGetItem(func_3920_call(), 0)
func_4391_call = mod.get_global_var('func_4391')
func_4392_call = mutated_mod.get_global_var('func_4392')
call_5540 = func_4391_call()
call_5541 = func_4391_call()
func_1756_call = mod.get_global_var('func_1756')
func_1760_call = mutated_mod.get_global_var('func_1760')
var_5545 = relay.var("var_5545", dtype = "float32", shape = (336,))#candidate|5545|(336,)|var|float32
call_5544 = relay.TupleGetItem(func_1756_call(relay.reshape(var_5545.astype('float32'), [336,]), relay.reshape(call_5494.astype('float32'), [11, 14, 5]), ), 0)
call_5546 = relay.TupleGetItem(func_1760_call(relay.reshape(var_5545.astype('float32'), [336,]), relay.reshape(call_5494.astype('float32'), [11, 14, 5]), ), 0)
uop_5549 = relay.sinh(const_5512.astype('float32')) # shape=(2, 528)
var_5552 = relay.var("var_5552", dtype = "int32", shape = (2, 528))#candidate|5552|(2, 528)|var|int32
bop_5553 = relay.not_equal(const_5512.astype('bool'), relay.reshape(var_5552.astype('bool'), relay.shape_of(const_5512))) # shape=(2, 528)
uop_5561 = relay.acos(uop_5549.astype('float64')) # shape=(2, 528)
var_5570 = relay.var("var_5570", dtype = "float64", shape = (2, 528))#candidate|5570|(2, 528)|var|float64
bop_5571 = relay.logical_and(uop_5561.astype('bool'), relay.reshape(var_5570.astype('bool'), relay.shape_of(uop_5561))) # shape=(2, 528)
output = relay.Tuple([call_5494,call_5506,call_5511,call_5534,call_5540,call_5544,var_5545,bop_5553,bop_5571,])
output2 = relay.Tuple([call_5495,call_5507,call_5513,call_5535,call_5541,call_5546,var_5545,bop_5553,bop_5571,])
func_5576 = relay.Function([var_5545,var_5552,var_5570,], output)
mod['func_5576'] = func_5576
mod = relay.transform.InferType()(mod)
mutated_mod['func_5576'] = func_5576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5576_call = mutated_mod.get_global_var('func_5576')
var_5578 = relay.var("var_5578", dtype = "float32", shape = (336,))#candidate|5578|(336,)|var|float32
var_5579 = relay.var("var_5579", dtype = "int32", shape = (2, 528))#candidate|5579|(2, 528)|var|int32
var_5580 = relay.var("var_5580", dtype = "float64", shape = (2, 528))#candidate|5580|(2, 528)|var|float64
call_5577 = func_5576_call(var_5578,var_5579,var_5580,)
output = call_5577
func_5581 = relay.Function([var_5578,var_5579,var_5580,], output)
mutated_mod['func_5581'] = func_5581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5014_call = mod.get_global_var('func_5014')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_5585 = relay.TupleGetItem(func_5014_call(), 0)
call_5586 = relay.TupleGetItem(func_5015_call(), 0)
output = relay.Tuple([call_5585,])
output2 = relay.Tuple([call_5586,])
func_5597 = relay.Function([], output)
mod['func_5597'] = func_5597
mod = relay.transform.InferType()(mod)
output = func_5597()
func_5598 = relay.Function([], output)
mutated_mod['func_5598'] = func_5598
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5694 = relay.const([[[-1,-2,6,8,-9,-9,5,-9],[-7,8,-10,-7,9,9,7,9],[-2,2,9,1,3,2,-5,-2],[1,-8,8,-9,-1,9,8,7],[1,9,9,9,1,-9,2,1],[-3,6,6,-2,-2,6,1,1],[1,3,1,4,-1,10,-6,9],[-2,1,-10,7,-4,-1,6,-6],[-1,9,-8,6,5,5,7,-1],[10,-6,-4,10,6,4,3,-1],[8,-8,10,-10,-10,-8,-10,7],[-10,-10,-8,4,-4,-7,10,-1],[7,-9,-3,-4,3,-1,9,-4],[-3,-5,5,-6,-8,5,-1,8],[-8,-7,-5,4,-2,-10,-5,2]],[[-9,10,6,4,-2,-4,5,-3],[9,4,8,2,4,-1,-8,-8],[9,2,7,9,-5,2,-5,3],[-4,7,-6,2,-3,-1,-7,10],[1,9,-10,-9,1,6,-6,-1],[-7,-2,9,5,8,-3,-6,-1],[6,7,10,10,-7,9,-5,-4],[9,5,2,10,-5,7,7,-10],[-9,9,-1,1,7,-3,-10,-7],[3,-7,-4,-4,-1,2,-8,10],[-7,7,2,-10,-7,3,8,-6],[-2,7,-1,4,-2,9,9,9],[2,6,3,-3,8,8,4,8],[-7,3,-6,2,-5,9,-2,-10],[4,6,-3,-6,3,-7,-7,6]],[[-8,4,7,-3,6,-4,2,-3],[-1,4,8,-5,5,1,-4,8],[5,7,7,-4,-6,1,4,4],[3,-9,9,5,5,6,4,-3],[-5,2,-2,4,9,-6,9,10],[2,-6,-5,-5,-8,2,-6,-2],[-7,2,5,9,-1,-8,-7,-4],[-2,-1,1,9,-8,3,8,-6],[4,-4,4,-2,10,-5,10,7],[-10,-1,4,-2,1,-8,-3,-3],[4,5,-5,-5,8,-4,-1,-2],[-9,2,3,8,1,4,-2,-10],[-8,-4,-1,6,9,10,10,1],[-5,5,-10,3,-10,-5,5,7],[-2,6,10,-5,-3,10,-6,-5]],[[7,10,-2,9,1,-4,-1,2],[4,7,2,-6,6,8,-9,5],[-2,1,8,-6,4,-7,-1,-8],[-9,-10,8,5,1,10,-8,-4],[-9,-4,5,-6,-2,-3,4,-9],[-8,-5,4,-4,5,5,-6,2],[5,2,8,10,5,-4,-7,-3],[1,-3,7,-3,9,4,8,3],[-5,-5,5,4,9,8,-10,-2],[6,-9,-5,5,-10,-1,8,2],[-9,8,-2,-1,-10,-8,-7,-3],[-8,-9,-3,-6,7,1,-1,9],[-2,3,1,7,-2,-2,-7,-5],[-5,7,9,3,1,1,9,-2],[-9,6,-9,-3,-10,-2,-10,-4]],[[-1,5,4,-6,-1,9,-7,10],[-7,7,-9,-1,-5,-8,9,-2],[-4,-10,4,-7,3,7,-8,7],[3,-3,4,3,-6,4,4,-8],[2,1,4,-5,4,6,-6,9],[-6,-2,-8,-10,8,4,10,2],[-9,-2,-3,-1,-6,10,1,1],[-6,10,10,2,3,-1,7,-7],[-8,-1,-3,-9,3,-2,3,-4],[8,4,-1,7,-10,9,4,4],[-4,-7,9,-7,-7,7,-2,-8],[-2,-2,7,-8,-10,6,4,9],[5,8,-10,-8,-6,7,-5,-10],[-7,1,2,3,-8,-5,9,4],[-8,9,7,-6,-4,1,-10,-8]],[[3,-1,1,-4,-2,-3,3,-4],[10,-2,3,-2,-3,-8,-3,-9],[6,-1,1,7,-4,-4,-8,9],[-4,-8,9,5,2,4,-8,2],[-3,10,-8,-7,7,-1,-2,4],[-1,2,-2,-3,-8,10,10,-9],[-6,-6,6,-7,7,-8,8,2],[6,-1,-10,-1,-1,-6,4,3],[4,2,-3,1,-9,-8,2,-10],[7,-5,6,-7,8,8,-9,-1],[8,-5,6,-2,6,4,1,6],[-5,-7,10,8,7,9,-4,-1],[6,5,3,-7,-9,-6,-4,10],[-7,2,9,5,-5,4,-7,-4],[-10,-4,-6,1,-3,6,1,-9]],[[-3,6,-3,7,-5,7,-5,-6],[-2,9,3,-5,-7,6,-7,8],[7,1,3,10,-1,4,10,1],[2,1,-10,-2,7,6,-4,-3],[8,-5,-4,-3,-1,-10,-6,-2],[3,-4,10,-1,-5,-9,3,3],[8,2,-10,6,1,2,-7,4],[10,2,-5,4,-9,-10,-7,-4],[9,-8,3,10,-9,1,-9,-7],[-2,-6,1,-6,3,5,-9,6],[6,-8,-9,3,1,4,-9,-6],[2,-10,1,5,4,-7,-10,-2],[8,-5,6,-5,-2,-6,1,-3],[-5,-6,-9,-2,3,-5,-4,-1],[-4,-9,6,9,4,8,9,-8]],[[2,-3,-5,3,6,-10,4,-5],[8,3,10,2,9,-9,3,5],[9,8,4,-1,1,1,5,-8],[-1,-8,4,5,2,-4,-1,-2],[-8,6,4,-2,-3,2,10,10],[2,-2,-8,10,3,6,-4,8],[-9,-1,4,-9,8,-4,3,10],[3,-2,3,2,-5,-1,7,10],[-6,8,-6,-8,10,1,-7,9],[-6,-3,-10,-4,3,3,-7,-5],[-5,4,2,4,-5,3,9,-5],[2,2,3,6,-3,8,-3,-4],[6,10,1,7,-10,-1,-4,-3],[-4,-8,-3,5,-7,-6,3,-1],[-10,-6,4,9,8,4,-4,-10]],[[-4,-5,5,2,10,4,-10,4],[-3,-2,-6,4,1,-7,7,-5],[-8,-7,-2,-4,-9,-8,3,-10],[4,5,3,5,-7,10,2,4],[-8,2,2,-4,6,9,-4,6],[-10,-8,-10,6,-7,-1,4,8],[10,1,8,2,-7,-3,-1,1],[-2,4,-3,-9,-9,-9,8,4],[-9,-10,2,1,7,2,-5,-9],[1,-8,4,-5,2,5,-3,-7],[-5,9,3,7,-6,-7,-10,-9],[-10,5,6,8,-4,-7,-1,9],[-5,3,8,7,-9,-6,-1,-1],[-2,6,4,8,-6,-5,1,-4],[2,-4,9,4,-6,-10,5,-7]],[[-8,7,-6,4,-9,-2,2,-7],[-5,-5,-4,6,-1,-4,-10,3],[5,-3,-6,4,3,6,-4,-10],[-5,5,5,-9,8,3,6,5],[8,2,-3,9,-2,3,-1,-5],[1,-6,-1,-1,8,-6,-1,-4],[9,5,2,-9,-3,2,-9,-10],[7,5,1,-9,-3,3,-6,-5],[5,-8,-5,3,1,-2,4,-9],[8,-1,3,7,-6,7,1,6],[3,-5,1,8,5,2,-2,2],[-8,-8,-2,-4,9,-10,-7,-6],[-2,-9,-1,9,-7,-7,4,10],[2,-3,-4,5,-2,4,5,10],[-3,4,-7,3,-4,4,10,1]],[[1,8,-3,-1,-10,-4,6,-2],[-4,4,9,-5,8,10,3,-3],[5,2,-6,3,-9,-1,-3,-2],[1,-6,3,-3,1,2,3,8],[5,-4,-6,-9,5,8,4,3],[-7,-8,-2,-3,2,-7,-9,3],[-9,-6,-5,8,6,-8,-5,8],[3,2,4,-8,-1,3,2,-5],[-4,-3,-8,1,-6,-6,3,5],[-9,9,4,-4,-2,8,-3,-4],[6,10,-10,-9,1,9,1,-9],[-3,-8,8,6,8,-4,7,-10],[5,10,-10,-2,-6,6,-7,10],[3,-8,9,-1,-8,-10,4,9],[-9,-7,-7,3,-3,1,-3,-9]],[[8,-1,1,-5,-8,-3,6,-4],[-8,5,1,9,8,4,-10,2],[-10,8,-5,-2,10,7,-7,1],[3,3,6,10,1,-7,-6,-10],[2,-10,2,1,-7,-6,-1,-10],[-2,8,4,-4,-3,7,-2,8],[4,2,-1,-8,3,-3,-8,7],[-7,-8,7,5,4,9,-8,9],[-8,9,-6,-10,-8,3,9,8],[7,6,-9,-3,-4,9,1,7],[9,-1,-3,-3,-5,9,-6,-9],[-4,-6,9,-7,4,-6,-2,-6],[-8,-7,7,2,-6,-7,1,-5],[2,-9,3,-3,-2,3,1,8],[-8,10,2,-9,-6,-1,10,-1]],[[9,3,-8,10,7,-7,-5,-8],[7,-8,10,9,2,3,6,-6],[6,7,-8,-5,2,-3,-6,-8],[9,-3,-1,-6,-2,7,-3,-1],[6,2,-6,-9,10,3,-5,2],[-7,6,7,3,1,7,6,-2],[7,4,-2,2,-9,1,-8,-1],[-7,-2,-8,-6,-6,-4,5,3],[-9,-7,-4,-6,-6,8,-9,-6],[5,-5,-5,-2,7,5,2,-4],[-7,-6,10,5,-1,9,-1,8],[-4,-8,5,-2,-8,2,7,4],[7,-6,-4,-2,-5,4,-5,-3],[-7,-10,3,-7,-10,-2,7,10],[6,10,8,-4,4,-10,-10,9]]], dtype = "uint16")#candidate|5694|(13, 15, 8)|const|uint16
var_5695 = relay.var("var_5695", dtype = "uint16", shape = (13, 15, 8))#candidate|5695|(13, 15, 8)|var|uint16
bop_5696 = relay.multiply(const_5694.astype('uint16'), relay.reshape(var_5695.astype('uint16'), relay.shape_of(const_5694))) # shape=(13, 15, 8)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
const_5706 = relay.const([2.317104,-5.527235,4.680263,-7.073606,-8.276619,-4.427205,8.041265,-0.675010,5.594889,-6.698527,4.852996,-1.525202,5.872778,5.930267,-4.709477,-3.988665,-2.320426,-7.491528,-1.375234,-7.481253,4.002473,9.290710,-7.891407,4.576144,-6.488632,8.265917,-8.946449,6.243243,-6.961211,-2.136297,-8.083273,1.656398,9.753709,-7.012702,-8.992763,-6.604116,1.707956,-6.317769,8.329801,6.183342,9.325517,-1.033687,-4.093000,-8.586019,-1.029131,-0.302833,0.336500,7.311914,8.456684,-6.851726,-1.348699,2.028475,-1.482970,1.435485,-9.729360,-8.009973,8.187133,1.736440,-3.703756,4.622465,-5.479913,8.821506,7.339123,-2.312687,-6.439376,-0.357666,-6.085879,-8.825768,3.944172,-8.352696,1.727270,3.644598,9.042508,-9.253666,-9.138094,-2.868658,1.712943,-6.648942,-9.182202,-8.857108,9.270343,5.817020,-1.677111,1.894875,-2.753060,1.634893,-4.549011,-0.915651,7.219263,4.503112,-2.739678,-9.090929,-5.547924,-1.810422,-7.926464,0.516985,1.894810,9.221751,4.909813,3.803966,-0.761252,4.413677,-6.953813,0.905161,-1.165313,3.639670,-9.982314,9.369266,4.765032,-2.077786,-9.040220,7.616201,-4.350074,4.722897,1.172545,4.780279,-0.413847,-0.025114,3.783947,-9.451884,9.160114,-8.967050,-3.518508,-6.363463,-8.621033,1.470517,-2.142401,-3.130675,4.955606,-3.573000,7.022762,-0.187679,-4.406407,-7.331929,-2.220826,-3.776307,-6.042959,-9.341103,-1.791250,-0.469680,9.040950,9.675855,8.687304,-5.796251,8.057969,8.049340,0.158077,-6.871033,6.683054,3.151967,-6.931231,6.174873,-0.252660,1.459557,-6.893434,7.855585,2.335327,4.281867,2.549651,7.743291,7.378465,7.116595,-8.429760,-0.853909,-6.307398,-3.422692,6.238528,4.091768,2.749858,-7.830956,7.584320,1.714613,-3.830727,6.012895,-5.239416,4.986491,7.337818,-4.868165,-3.977345,9.886458,-3.363589,3.291372,7.469785,-0.935170,7.899898,-4.561370,-8.939200,7.017200,5.820400,-3.118773,5.502074,1.400966], dtype = "float64")#candidate|5706|(192,)|const|float64
call_5705 = relay.TupleGetItem(func_2204_call(relay.reshape(const_5706.astype('float64'), [1, 16, 12])), 1)
call_5707 = relay.TupleGetItem(func_2206_call(relay.reshape(const_5706.astype('float64'), [1, 16, 12])), 1)
func_3966_call = mod.get_global_var('func_3966')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_5713 = relay.TupleGetItem(func_3966_call(), 0)
call_5714 = relay.TupleGetItem(func_3967_call(), 0)
uop_5724 = relay.erf(var_5695.astype('float64')) # shape=(13, 15, 8)
func_2851_call = mod.get_global_var('func_2851')
func_2855_call = mutated_mod.get_global_var('func_2855')
const_5731 = relay.const([-2,1,-10,5,9,4,10,-2,8,-10,2,-9,3,2,-7,-7,10,6,2,5,-3,-3,-2,-9,-7,-3,4,8,2,-7,9,-8,5,8,-7,-9,1,5,-7,6,-3,2,2,5,10,-3,-9,7,-4,1,7,2,-4,-3,-9,-6], dtype = "int8")#candidate|5731|(56,)|const|int8
const_5732 = relay.const([-0.077583,1.248752,-6.152240,-4.146588,0.267505,6.649353,-9.112835,8.362978,-1.915535,-6.434817,-8.478622,-5.031492,-9.947209,-7.476039,6.397358,6.859069,-4.165141,6.967935,3.817939,4.163999,3.225542,-1.982562,-0.279000,-5.972994,3.413636,0.259203,0.379918,-3.105911,-5.588213,-3.954855,7.948117,0.981179,-9.890500,-6.154797,-4.862959,-5.110893,-9.954552,2.166959,0.115779,1.745660,-4.865365,-2.356872,-8.034999,5.714700,4.617726,-1.415894,4.383999,-9.913038,-7.691350,-8.418465,-8.586233,-5.094557,8.395336,-7.770027,0.027120,-9.254705,-7.829408,-7.439741,1.936894,9.977803,2.773646,0.648518,3.382174,-9.858488,-7.215482,-6.899321,6.142817,8.373413,-6.116733,1.799492,9.132384,6.485810,3.922549,-6.356947,4.169459,3.455627,5.204901,-9.196803,5.603937,-9.424231,3.201247,-8.542278,-2.433262,6.210720,0.361024,-0.229066,-7.169206,-3.577060,1.965841,3.391193,-2.280834,0.358613,0.470893,-2.261933,-8.848841,9.090139,7.631867,7.504117,6.759869,-2.092476,0.810284,-0.974695,-0.793244,4.074399,2.421304,7.519413,-9.357014,-6.674953,-2.326483,-6.811121,5.066555,-2.403935,7.513286,-5.050383,-1.413411,-1.913866,-3.329527,-9.539271,8.362570,-7.621912,-1.320147,3.923707,5.623861,-9.346080,-3.201266,-7.088498,-0.443357,0.880284,-8.411448,0.158890,-2.978705,2.360933,-2.056770,-7.140227,9.501343,-4.416511,-1.067384,-5.101962,4.557111,2.837793,8.094646,-0.366904,-0.461623,-5.124058,0.529827,8.702680,6.743042,-4.513335,-0.917359,4.789477,-0.576092,0.055037,5.782713,-8.451936,0.226288,7.034649,9.493721,-1.103503,9.406885,7.192607,-8.712948,-0.369498,3.257702,9.487595,6.757828,1.339333,0.905576,-3.615030,9.022134,1.212853,-8.171120,7.699458,-2.594173,9.091190,-2.027763,7.099621,-6.860631,-8.767084,-2.913159,1.522171,9.905621,7.226815,-7.333667,5.433846,-1.719708,-3.629140,5.620315,3.196729,7.489896,5.334335,4.053285,6.442078,2.893592,8.165175,6.040432,5.049978,9.578597,4.305482,9.160693,2.648799,-1.445684,-5.307715,-1.314551,7.355459,0.574081,9.604100,0.767026,-3.240727,1.819300,5.363491,-3.686435,8.560237,9.316384,6.160377,5.866639,8.362095,-9.001141,-6.091783,4.653930,0.603509,-7.135578,6.894120,6.306114,-3.771629,3.538733,1.324349,4.175353,2.839605,-9.858958,9.378102,-5.703120,3.553447,-0.664099,5.281868,8.845193,-7.631893,3.669894,-7.673309,4.081588,6.564582,-1.338275,3.933898,2.235564,-6.515077,6.393028,-2.158913,-1.211087,9.256198,8.912996,-8.736830,8.405727,-4.289315,-5.006549,7.909603,-8.224181,-1.622283,8.962575,-6.357858,9.337030,-3.123182,-1.950767,-9.889460,-0.514937,5.396661,-2.927949,6.664057,6.279438,-3.156370,-7.079589,2.793854,4.455268,5.310988,2.482857,0.748113,-8.189461,-3.563879,-6.316240,-3.543672,-0.169330,-7.201851,6.017483,-6.877069,-8.292622,4.379453,-6.768353,8.811157,-0.116080,-5.277777,-4.197368,-1.435515,-6.910794,3.186186,0.732950,7.154884,3.453490,-1.775605,1.520969,9.465152,-7.738267,-9.654766,-5.806038,-1.461746,-0.945403,-0.676073,-6.879614,-1.649318,1.464355,-4.180705,2.737000,-3.004771,1.237448,6.485042,3.345410,-5.170926,0.579365,-9.989325,-0.824414,4.108947,-4.625616,3.671341,-5.378105,8.645493,1.520155,4.681577,3.432806,-4.216244,-8.166120,-6.128699,-7.352188,6.538617,7.076271,9.035335,-0.225076,0.466231,8.595520,-1.153029], dtype = "float32")#candidate|5732|(336,)|const|float32
var_5733 = relay.var("var_5733", dtype = "float64", shape = (616,))#candidate|5733|(616,)|var|float64
call_5730 = relay.TupleGetItem(func_2851_call(relay.reshape(const_5731.astype('int8'), [56,]), relay.reshape(const_5732.astype('float32'), [168, 2]), relay.reshape(var_5733.astype('float64'), [11, 7, 8]), ), 8)
call_5734 = relay.TupleGetItem(func_2855_call(relay.reshape(const_5731.astype('int8'), [56,]), relay.reshape(const_5732.astype('float32'), [168, 2]), relay.reshape(var_5733.astype('float64'), [11, 7, 8]), ), 8)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_5735 = relay.TupleGetItem(func_2043_call(), 0)
call_5736 = relay.TupleGetItem(func_2044_call(), 0)
output = relay.Tuple([bop_5696,call_5705,const_5706,call_5713,uop_5724,call_5730,const_5731,const_5732,var_5733,call_5735,])
output2 = relay.Tuple([bop_5696,call_5707,const_5706,call_5714,uop_5724,call_5734,const_5731,const_5732,var_5733,call_5736,])
func_5741 = relay.Function([var_5695,var_5733,], output)
mod['func_5741'] = func_5741
mod = relay.transform.InferType()(mod)
mutated_mod['func_5741'] = func_5741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5741_call = mutated_mod.get_global_var('func_5741')
var_5743 = relay.var("var_5743", dtype = "uint16", shape = (13, 15, 8))#candidate|5743|(13, 15, 8)|var|uint16
var_5744 = relay.var("var_5744", dtype = "float64", shape = (616,))#candidate|5744|(616,)|var|float64
call_5742 = func_5741_call(var_5743,var_5744,)
output = call_5742
func_5745 = relay.Function([var_5743,var_5744,], output)
mutated_mod['func_5745'] = func_5745
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5773 = relay.var("var_5773", dtype = "float32", shape = (16, 14, 15))#candidate|5773|(16, 14, 15)|var|float32
uop_5774 = relay.sin(var_5773.astype('float32')) # shape=(16, 14, 15)
func_1888_call = mod.get_global_var('func_1888')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_5778 = relay.TupleGetItem(func_1888_call(), 0)
call_5779 = relay.TupleGetItem(func_1890_call(), 0)
func_4939_call = mod.get_global_var('func_4939')
func_4941_call = mutated_mod.get_global_var('func_4941')
const_5784 = relay.const([4.475010,0.919934,-6.427959,-3.922651,-6.532854,-9.175664,-5.058079,-5.604807,-3.001753,6.208707,0.357377,-6.516661,1.634711,-3.062162,8.881397,3.603240,-3.606814,-6.138543,-0.257041,-9.128758], dtype = "float64")#candidate|5784|(20,)|const|float64
call_5783 = relay.TupleGetItem(func_4939_call(relay.reshape(const_5784.astype('float64'), [20,])), 0)
call_5785 = relay.TupleGetItem(func_4941_call(relay.reshape(const_5784.astype('float64'), [20,])), 0)
func_4321_call = mod.get_global_var('func_4321')
func_4326_call = mutated_mod.get_global_var('func_4326')
var_5787 = relay.var("var_5787", dtype = "float32", shape = (66, 2))#candidate|5787|(66, 2)|var|float32
var_5788 = relay.var("var_5788", dtype = "float32", shape = (336,))#candidate|5788|(336,)|var|float32
call_5786 = relay.TupleGetItem(func_4321_call(relay.reshape(var_5787.astype('float32'), [132,]), relay.reshape(call_5783.astype('float32'), [7, 110]), relay.reshape(var_5788.astype('float32'), [336,]), ), 1)
call_5789 = relay.TupleGetItem(func_4326_call(relay.reshape(var_5787.astype('float32'), [132,]), relay.reshape(call_5783.astype('float32'), [7, 110]), relay.reshape(var_5788.astype('float32'), [336,]), ), 1)
output = relay.Tuple([uop_5774,call_5778,call_5783,const_5784,call_5786,var_5787,var_5788,])
output2 = relay.Tuple([uop_5774,call_5779,call_5785,const_5784,call_5789,var_5787,var_5788,])
func_5808 = relay.Function([var_5773,var_5787,var_5788,], output)
mod['func_5808'] = func_5808
mod = relay.transform.InferType()(mod)
var_5809 = relay.var("var_5809", dtype = "float32", shape = (16, 14, 15))#candidate|5809|(16, 14, 15)|var|float32
var_5810 = relay.var("var_5810", dtype = "float32", shape = (66, 2))#candidate|5810|(66, 2)|var|float32
var_5811 = relay.var("var_5811", dtype = "float32", shape = (336,))#candidate|5811|(336,)|var|float32
output = func_5808(var_5809,var_5810,var_5811,)
func_5812 = relay.Function([var_5809,var_5810,var_5811,], output)
mutated_mod['func_5812'] = func_5812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4863_call = mod.get_global_var('func_4863')
func_4865_call = mutated_mod.get_global_var('func_4865')
call_5883 = relay.TupleGetItem(func_4863_call(), 4)
call_5884 = relay.TupleGetItem(func_4865_call(), 4)
output = call_5883
output2 = call_5884
func_5897 = relay.Function([], output)
mod['func_5897'] = func_5897
mod = relay.transform.InferType()(mod)
mutated_mod['func_5897'] = func_5897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5897_call = mutated_mod.get_global_var('func_5897')
call_5898 = func_5897_call()
output = call_5898
func_5899 = relay.Function([], output)
mutated_mod['func_5899'] = func_5899
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5928 = relay.var("var_5928", dtype = "float32", shape = (14, 15, 6))#candidate|5928|(14, 15, 6)|var|float32
uop_5929 = relay.cos(var_5928.astype('float32')) # shape=(14, 15, 6)
func_672_call = mod.get_global_var('func_672')
func_676_call = mutated_mod.get_global_var('func_676')
var_5938 = relay.var("var_5938", dtype = "int32", shape = (1056,))#candidate|5938|(1056,)|var|int32
call_5937 = relay.TupleGetItem(func_672_call(relay.reshape(var_5938.astype('int32'), [11, 8, 12]), relay.reshape(var_5938.astype('int32'), [11, 8, 12]), ), 1)
call_5939 = relay.TupleGetItem(func_676_call(relay.reshape(var_5938.astype('int32'), [11, 8, 12]), relay.reshape(var_5938.astype('int32'), [11, 8, 12]), ), 1)
output = relay.Tuple([uop_5929,call_5937,var_5938,])
output2 = relay.Tuple([uop_5929,call_5939,var_5938,])
func_5945 = relay.Function([var_5928,var_5938,], output)
mod['func_5945'] = func_5945
mod = relay.transform.InferType()(mod)
var_5946 = relay.var("var_5946", dtype = "float32", shape = (14, 15, 6))#candidate|5946|(14, 15, 6)|var|float32
var_5947 = relay.var("var_5947", dtype = "int32", shape = (1056,))#candidate|5947|(1056,)|var|int32
output = func_5945(var_5946,var_5947,)
func_5948 = relay.Function([var_5946,var_5947,], output)
mutated_mod['func_5948'] = func_5948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2598_call = mod.get_global_var('func_2598')
func_2600_call = mutated_mod.get_global_var('func_2600')
call_5966 = relay.TupleGetItem(func_2598_call(), 0)
call_5967 = relay.TupleGetItem(func_2600_call(), 0)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
var_5976 = relay.var("var_5976", dtype = "int8", shape = (56,))#candidate|5976|(56,)|var|int8
call_5975 = relay.TupleGetItem(func_2745_call(relay.reshape(var_5976.astype('int8'), [56,])), 2)
call_5977 = relay.TupleGetItem(func_2747_call(relay.reshape(var_5976.astype('int8'), [56,])), 2)
output = relay.Tuple([call_5966,call_5975,var_5976,])
output2 = relay.Tuple([call_5967,call_5977,var_5976,])
func_5991 = relay.Function([var_5976,], output)
mod['func_5991'] = func_5991
mod = relay.transform.InferType()(mod)
mutated_mod['func_5991'] = func_5991
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5992 = relay.var("var_5992", dtype = "int8", shape = (56,))#candidate|5992|(56,)|var|int8
func_5991_call = mutated_mod.get_global_var('func_5991')
call_5993 = func_5991_call(var_5992)
output = call_5993
func_5994 = relay.Function([var_5992], output)
mutated_mod['func_5994'] = func_5994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2382_call = mod.get_global_var('func_2382')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_6091 = relay.TupleGetItem(func_2382_call(), 0)
call_6092 = relay.TupleGetItem(func_2384_call(), 0)
func_3966_call = mod.get_global_var('func_3966')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_6095 = relay.TupleGetItem(func_3966_call(), 0)
call_6096 = relay.TupleGetItem(func_3967_call(), 0)
output = relay.Tuple([call_6091,call_6095,])
output2 = relay.Tuple([call_6092,call_6096,])
func_6097 = relay.Function([], output)
mod['func_6097'] = func_6097
mod = relay.transform.InferType()(mod)
mutated_mod['func_6097'] = func_6097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6097_call = mutated_mod.get_global_var('func_6097')
call_6098 = func_6097_call()
output = call_6098
func_6099 = relay.Function([], output)
mutated_mod['func_6099'] = func_6099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5400_call = mod.get_global_var('func_5400')
func_5402_call = mutated_mod.get_global_var('func_5402')
call_6139 = relay.TupleGetItem(func_5400_call(), 0)
call_6140 = relay.TupleGetItem(func_5402_call(), 0)
func_143_call = mod.get_global_var('func_143')
func_145_call = mutated_mod.get_global_var('func_145')
var_6180 = relay.var("var_6180", dtype = "float64", shape = (165, 3))#candidate|6180|(165, 3)|var|float64
call_6179 = relay.TupleGetItem(func_143_call(relay.reshape(var_6180.astype('float64'), [11, 15, 3])), 0)
call_6181 = relay.TupleGetItem(func_145_call(relay.reshape(var_6180.astype('float64'), [11, 15, 3])), 0)
output = relay.Tuple([call_6139,call_6179,var_6180,])
output2 = relay.Tuple([call_6140,call_6181,var_6180,])
func_6182 = relay.Function([var_6180,], output)
mod['func_6182'] = func_6182
mod = relay.transform.InferType()(mod)
var_6183 = relay.var("var_6183", dtype = "float64", shape = (165, 3))#candidate|6183|(165, 3)|var|float64
output = func_6182(var_6183)
func_6184 = relay.Function([var_6183], output)
mutated_mod['func_6184'] = func_6184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_6292 = relay.TupleGetItem(func_4162_call(), 0)
call_6293 = relay.TupleGetItem(func_4164_call(), 0)
output = call_6292
output2 = call_6293
func_6306 = relay.Function([], output)
mod['func_6306'] = func_6306
mod = relay.transform.InferType()(mod)
output = func_6306()
func_6307 = relay.Function([], output)
mutated_mod['func_6307'] = func_6307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5492_call = mod.get_global_var('func_5492')
func_5493_call = mutated_mod.get_global_var('func_5493')
call_6338 = relay.TupleGetItem(func_5492_call(), 2)
call_6339 = relay.TupleGetItem(func_5493_call(), 2)
output = call_6338
output2 = call_6339
func_6342 = relay.Function([], output)
mod['func_6342'] = func_6342
mod = relay.transform.InferType()(mod)
mutated_mod['func_6342'] = func_6342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6342_call = mutated_mod.get_global_var('func_6342')
call_6343 = func_6342_call()
output = call_6343
func_6344 = relay.Function([], output)
mutated_mod['func_6344'] = func_6344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4863_call = mod.get_global_var('func_4863')
func_4865_call = mutated_mod.get_global_var('func_4865')
call_6363 = relay.TupleGetItem(func_4863_call(), 4)
call_6364 = relay.TupleGetItem(func_4865_call(), 4)
output = relay.Tuple([call_6363,])
output2 = relay.Tuple([call_6364,])
func_6370 = relay.Function([], output)
mod['func_6370'] = func_6370
mod = relay.transform.InferType()(mod)
mutated_mod['func_6370'] = func_6370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6370_call = mutated_mod.get_global_var('func_6370')
call_6371 = func_6370_call()
output = call_6371
func_6372 = relay.Function([], output)
mutated_mod['func_6372'] = func_6372
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6379 = relay.var("var_6379", dtype = "int16", shape = (2, 9, 14))#candidate|6379|(2, 9, 14)|var|int16
const_6380 = relay.const([[[1,2,-4,1,-1,9,1,-10,-10,-1,10,-4,3,5],[-10,-4,10,10,-8,2,-10,-7,-1,-3,-5,-4,10,-3],[5,-5,-9,-5,-4,-5,-7,-4,-7,10,-5,9,-9,-6],[10,-10,-7,1,5,-5,2,-1,-4,-8,5,9,10,9],[10,6,7,6,-2,-8,-4,6,-10,6,2,-4,-9,7],[10,7,-3,9,-1,-4,1,-2,4,10,-6,9,-8,5],[6,7,9,-6,-8,-2,10,-4,7,-6,5,-6,-10,-9],[8,6,-5,1,-8,6,-4,5,-4,6,6,-2,-6,1],[3,-6,3,4,6,4,2,10,-8,-1,7,-6,7,-3]],[[8,1,-6,-10,-9,-9,-10,1,-2,-2,-7,5,-8,6],[-10,-2,-4,10,10,-1,6,5,2,10,6,-8,-4,-6],[5,2,2,-4,5,-6,-3,7,8,5,-10,6,8,-1],[-7,7,-1,-7,-2,-9,2,3,4,-5,2,2,7,-7],[2,-7,7,10,4,-8,8,-3,-5,-8,-6,9,2,-9],[-9,-6,-6,-9,9,-10,-7,-7,-6,-5,-7,-9,-5,1],[10,-10,8,-10,-9,7,8,-10,6,2,-10,-4,-2,-1],[1,-6,-2,10,2,-6,8,-8,-1,-3,-10,2,2,8],[-10,10,-9,-4,5,-2,-5,10,2,-10,-8,1,-8,7]]], dtype = "int16")#candidate|6380|(2, 9, 14)|const|int16
bop_6381 = relay.bitwise_and(var_6379.astype('int16'), relay.reshape(const_6380.astype('int16'), relay.shape_of(var_6379))) # shape=(2, 9, 14)
output = relay.Tuple([bop_6381,])
output2 = relay.Tuple([bop_6381,])
func_6386 = relay.Function([var_6379,], output)
mod['func_6386'] = func_6386
mod = relay.transform.InferType()(mod)
mutated_mod['func_6386'] = func_6386
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6387 = relay.var("var_6387", dtype = "int16", shape = (2, 9, 14))#candidate|6387|(2, 9, 14)|var|int16
func_6386_call = mutated_mod.get_global_var('func_6386')
call_6388 = func_6386_call(var_6387)
output = call_6388
func_6389 = relay.Function([var_6387], output)
mutated_mod['func_6389'] = func_6389
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6411 = relay.var("var_6411", dtype = "float32", shape = (15, 11, 15))#candidate|6411|(15, 11, 15)|var|float32
uop_6412 = relay.acosh(var_6411.astype('float32')) # shape=(15, 11, 15)
func_5808_call = mod.get_global_var('func_5808')
func_5812_call = mutated_mod.get_global_var('func_5812')
var_6432 = relay.var("var_6432", dtype = "float32", shape = (3360,))#candidate|6432|(3360,)|var|float32
const_6433 = relay.const([[0.400705],[6.431435],[-1.349232],[4.573301],[6.143746],[1.036680],[5.885087],[6.211032],[3.083463],[-8.302142],[8.703588],[6.306689],[-1.297513],[-7.353186],[-6.603029],[-1.976102],[-0.443313],[-1.743994],[-4.451819],[-1.986222],[6.242033],[8.093077],[-3.971685],[-2.171055],[-7.700034],[-4.981179],[2.522000],[0.437609],[-1.945569],[-2.202670],[0.882071],[-9.219881],[-3.656079],[-1.684960],[-3.080830],[-3.351882],[6.128670],[-5.583160],[-8.302252],[8.007232],[5.985414],[7.266842],[8.103551],[-3.285055],[-2.164180],[9.861212],[5.667754],[2.907375],[-6.203279],[3.809514],[-4.680834],[-7.327249],[6.124991],[6.650995],[9.300243],[-4.971147],[-5.657453],[-0.530405],[9.112661],[7.775931],[9.372459],[6.696087],[-9.659558],[1.441469],[-4.417401],[4.616237],[-6.845894],[-1.317258],[3.712061],[-0.716936],[5.637614],[7.607941],[-7.200602],[2.723105],[8.225405],[0.505217],[2.035651],[4.091254],[2.683146],[-7.288140],[4.821673],[-8.900376],[0.291445],[-0.815967],[1.222980],[-5.451055],[8.524327],[-3.203037],[3.270823],[3.417731],[0.439320],[4.351457],[1.776564],[-4.369038],[3.840262],[1.789917],[0.802005],[8.652016],[-9.271875],[8.496791],[-0.303011],[-7.004619],[7.677449],[8.728695],[4.773940],[3.747796],[6.654485],[4.788102],[-0.858969],[3.645616],[2.008838],[-6.046336],[-9.733263],[0.756070],[9.097227],[-5.253774],[-7.697010],[-5.216139],[-5.122309],[-9.056291],[-5.290907],[-4.124333],[2.198956],[3.181918],[7.531874],[1.286935],[3.225919],[7.367565],[3.946768],[-6.041020],[7.270577],[-7.692028]], dtype = "float32")#candidate|6433|(132, 1)|const|float32
var_6434 = relay.var("var_6434", dtype = "float32", shape = (336,))#candidate|6434|(336,)|var|float32
call_6431 = relay.TupleGetItem(func_5808_call(relay.reshape(var_6432.astype('float32'), [16, 14, 15]), relay.reshape(const_6433.astype('float32'), [66, 2]), relay.reshape(var_6434.astype('float32'), [336,]), ), 6)
call_6435 = relay.TupleGetItem(func_5812_call(relay.reshape(var_6432.astype('float32'), [16, 14, 15]), relay.reshape(const_6433.astype('float32'), [66, 2]), relay.reshape(var_6434.astype('float32'), [336,]), ), 6)
output = relay.Tuple([uop_6412,call_6431,var_6432,const_6433,var_6434,])
output2 = relay.Tuple([uop_6412,call_6435,var_6432,const_6433,var_6434,])
func_6438 = relay.Function([var_6411,var_6432,var_6434,], output)
mod['func_6438'] = func_6438
mod = relay.transform.InferType()(mod)
mutated_mod['func_6438'] = func_6438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6438_call = mutated_mod.get_global_var('func_6438')
var_6440 = relay.var("var_6440", dtype = "float32", shape = (15, 11, 15))#candidate|6440|(15, 11, 15)|var|float32
var_6441 = relay.var("var_6441", dtype = "float32", shape = (3360,))#candidate|6441|(3360,)|var|float32
var_6442 = relay.var("var_6442", dtype = "float32", shape = (336,))#candidate|6442|(336,)|var|float32
call_6439 = func_6438_call(var_6440,var_6441,var_6442,)
output = call_6439
func_6443 = relay.Function([var_6440,var_6441,var_6442,], output)
mutated_mod['func_6443'] = func_6443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_6454 = relay.TupleGetItem(func_4162_call(), 0)
call_6455 = relay.TupleGetItem(func_4164_call(), 0)
output = call_6454
output2 = call_6455
func_6466 = relay.Function([], output)
mod['func_6466'] = func_6466
mod = relay.transform.InferType()(mod)
mutated_mod['func_6466'] = func_6466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6466_call = mutated_mod.get_global_var('func_6466')
call_6467 = func_6466_call()
output = call_6467
func_6468 = relay.Function([], output)
mutated_mod['func_6468'] = func_6468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5400_call = mod.get_global_var('func_5400')
func_5402_call = mutated_mod.get_global_var('func_5402')
call_6625 = relay.TupleGetItem(func_5400_call(), 0)
call_6626 = relay.TupleGetItem(func_5402_call(), 0)
func_1888_call = mod.get_global_var('func_1888')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_6636 = relay.TupleGetItem(func_1888_call(), 0)
call_6637 = relay.TupleGetItem(func_1890_call(), 0)
func_2546_call = mod.get_global_var('func_2546')
func_2547_call = mutated_mod.get_global_var('func_2547')
call_6664 = func_2546_call()
call_6665 = func_2546_call()
output = relay.Tuple([call_6625,call_6636,call_6664,])
output2 = relay.Tuple([call_6626,call_6637,call_6665,])
func_6679 = relay.Function([], output)
mod['func_6679'] = func_6679
mod = relay.transform.InferType()(mod)
output = func_6679()
func_6680 = relay.Function([], output)
mutated_mod['func_6680'] = func_6680
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6700 = relay.var("var_6700", dtype = "uint8", shape = (1, 5, 4))#candidate|6700|(1, 5, 4)|var|uint8
var_6701 = relay.var("var_6701", dtype = "uint8", shape = (12, 5, 4))#candidate|6701|(12, 5, 4)|var|uint8
bop_6702 = relay.logical_xor(var_6700.astype('uint8'), var_6701.astype('uint8')) # shape=(12, 5, 4)
func_283_call = mod.get_global_var('func_283')
func_285_call = mutated_mod.get_global_var('func_285')
var_6709 = relay.var("var_6709", dtype = "float32", shape = (132,))#candidate|6709|(132,)|var|float32
call_6708 = relay.TupleGetItem(func_283_call(relay.reshape(var_6709.astype('float32'), [4, 11, 3])), 3)
call_6710 = relay.TupleGetItem(func_285_call(relay.reshape(var_6709.astype('float32'), [4, 11, 3])), 3)
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_6712 = relay.TupleGetItem(func_4162_call(), 0)
call_6713 = relay.TupleGetItem(func_4164_call(), 0)
output = relay.Tuple([bop_6702,call_6708,var_6709,call_6712,])
output2 = relay.Tuple([bop_6702,call_6710,var_6709,call_6713,])
func_6716 = relay.Function([var_6700,var_6701,var_6709,], output)
mod['func_6716'] = func_6716
mod = relay.transform.InferType()(mod)
mutated_mod['func_6716'] = func_6716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6716_call = mutated_mod.get_global_var('func_6716')
var_6718 = relay.var("var_6718", dtype = "uint8", shape = (1, 5, 4))#candidate|6718|(1, 5, 4)|var|uint8
var_6719 = relay.var("var_6719", dtype = "uint8", shape = (12, 5, 4))#candidate|6719|(12, 5, 4)|var|uint8
var_6720 = relay.var("var_6720", dtype = "float32", shape = (132,))#candidate|6720|(132,)|var|float32
call_6717 = func_6716_call(var_6718,var_6719,var_6720,)
output = call_6717
func_6721 = relay.Function([var_6718,var_6719,var_6720,], output)
mutated_mod['func_6721'] = func_6721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2546_call = mod.get_global_var('func_2546')
func_2547_call = mutated_mod.get_global_var('func_2547')
call_6728 = func_2546_call()
call_6729 = func_2546_call()
output = relay.Tuple([call_6728,])
output2 = relay.Tuple([call_6729,])
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
func_6370_call = mod.get_global_var('func_6370')
func_6372_call = mutated_mod.get_global_var('func_6372')
call_6830 = relay.TupleGetItem(func_6370_call(), 0)
call_6831 = relay.TupleGetItem(func_6372_call(), 0)
uop_6845 = relay.sin(call_6830.astype('float64')) # shape=(616,)
uop_6847 = relay.sin(call_6831.astype('float64')) # shape=(616,)
bop_6856 = relay.maximum(uop_6845.astype('uint32'), relay.reshape(call_6830.astype('uint32'), relay.shape_of(uop_6845))) # shape=(616,)
bop_6859 = relay.maximum(uop_6847.astype('uint32'), relay.reshape(call_6831.astype('uint32'), relay.shape_of(uop_6847))) # shape=(616,)
var_6876 = relay.var("var_6876", dtype = "float64", shape = (616,))#candidate|6876|(616,)|var|float64
bop_6877 = relay.greater_equal(uop_6845.astype('bool'), relay.reshape(var_6876.astype('bool'), relay.shape_of(uop_6845))) # shape=(616,)
bop_6880 = relay.greater_equal(uop_6847.astype('bool'), relay.reshape(var_6876.astype('bool'), relay.shape_of(uop_6847))) # shape=(616,)
func_3966_call = mod.get_global_var('func_3966')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_6890 = relay.TupleGetItem(func_3966_call(), 0)
call_6891 = relay.TupleGetItem(func_3967_call(), 0)
output = relay.Tuple([bop_6856,bop_6877,call_6890,])
output2 = relay.Tuple([bop_6859,bop_6880,call_6891,])
func_6907 = relay.Function([var_6876,], output)
mod['func_6907'] = func_6907
mod = relay.transform.InferType()(mod)
var_6908 = relay.var("var_6908", dtype = "float64", shape = (616,))#candidate|6908|(616,)|var|float64
output = func_6907(var_6908)
func_6909 = relay.Function([var_6908], output)
mutated_mod['func_6909'] = func_6909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mod.get_global_var('func_2147')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_6925 = relay.TupleGetItem(func_2147_call(), 1)
call_6926 = relay.TupleGetItem(func_2149_call(), 1)
func_4863_call = mod.get_global_var('func_4863')
func_4865_call = mutated_mod.get_global_var('func_4865')
call_6930 = relay.TupleGetItem(func_4863_call(), 0)
call_6931 = relay.TupleGetItem(func_4865_call(), 0)
output = relay.Tuple([call_6925,call_6930,])
output2 = relay.Tuple([call_6926,call_6931,])
func_6937 = relay.Function([], output)
mod['func_6937'] = func_6937
mod = relay.transform.InferType()(mod)
output = func_6937()
func_6938 = relay.Function([], output)
mutated_mod['func_6938'] = func_6938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6937_call = mod.get_global_var('func_6937')
func_6938_call = mutated_mod.get_global_var('func_6938')
call_6955 = relay.TupleGetItem(func_6937_call(), 1)
call_6956 = relay.TupleGetItem(func_6938_call(), 1)
func_6716_call = mod.get_global_var('func_6716')
func_6721_call = mutated_mod.get_global_var('func_6721')
const_6969 = relay.const([4,2,-8,-3,2,-5,8,-2,1,8,2,6,-5,6,-7,-5,2,3,10,-6], dtype = "uint8")#candidate|6969|(20,)|const|uint8
var_6970 = relay.var("var_6970", dtype = "uint8", shape = (240,))#candidate|6970|(240,)|var|uint8
const_6971 = relay.const([6.704443,-0.535517,-3.413304,-1.178512,4.844919,8.332290,-0.937388,-1.580160,4.688026,5.124554,-9.913794,4.047785,-3.615285,9.091616,-5.662154,-4.322498,-7.429407,-1.709603,-2.654242,-2.221984,-4.085290,-0.807179,-5.747653,-0.019852,-6.825665,-0.823490,7.704809,4.514880,-7.015575,9.847748,-6.714517,-9.154507,5.223235,7.792772,4.079009,4.942916,-6.740096,3.393918,-0.135946,-5.298147,6.261436,6.731363,5.630982,5.891920,-9.408108,-2.766496,-3.760250,4.976906,9.173532,4.911104,-1.179152,4.938919,-4.420856,-2.159687,-1.613118,-7.540263,4.422554,-6.164070,-8.619545,-3.380888,-0.667260,5.842328,3.663403,-6.472982,-0.767527,-1.610036,-3.603038,5.525012,-9.080021,1.691755,-9.024168,-5.022649,-6.447551,-4.775563,-2.870001,8.247912,3.168307,-8.777723,5.002259,-4.737135,-8.236745,9.965862,-4.872290,-0.900384,-4.806887,9.238803,2.985576,-4.744517,-8.848960,-4.972281,5.708447,9.094677,8.031250,0.767949,1.214277,-6.991580,-7.536931,-6.881713,-1.180481,4.621037,2.073218,4.378110,5.877223,-4.193281,2.566838,-5.425164,-4.752530,9.005674,4.142218,-7.707653,-5.470221,6.049186,-1.004475,3.884367,-2.793541,3.500625,0.459952,-7.399735,-9.864320,-8.388792,2.438971,-8.900788,4.075346,9.492151,1.887282,1.302069,-5.905589,-6.865621,-2.439478,6.844735,0.035152,-6.588360], dtype = "float32")#candidate|6971|(132,)|const|float32
call_6968 = relay.TupleGetItem(func_6716_call(relay.reshape(const_6969.astype('uint8'), [1, 5, 4]), relay.reshape(var_6970.astype('uint8'), [12, 5, 4]), relay.reshape(const_6971.astype('float32'), [132,]), ), 3)
call_6972 = relay.TupleGetItem(func_6721_call(relay.reshape(const_6969.astype('uint8'), [1, 5, 4]), relay.reshape(var_6970.astype('uint8'), [12, 5, 4]), relay.reshape(const_6971.astype('float32'), [132,]), ), 3)
output = relay.Tuple([call_6955,call_6968,const_6969,var_6970,const_6971,])
output2 = relay.Tuple([call_6956,call_6972,const_6969,var_6970,const_6971,])
func_6973 = relay.Function([var_6970,], output)
mod['func_6973'] = func_6973
mod = relay.transform.InferType()(mod)
mutated_mod['func_6973'] = func_6973
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6974 = relay.var("var_6974", dtype = "uint8", shape = (240,))#candidate|6974|(240,)|var|uint8
func_6973_call = mutated_mod.get_global_var('func_6973')
call_6975 = func_6973_call(var_6974)
output = call_6975
func_6976 = relay.Function([var_6974], output)
mutated_mod['func_6976'] = func_6976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5400_call = mod.get_global_var('func_5400')
func_5402_call = mutated_mod.get_global_var('func_5402')
call_6994 = relay.TupleGetItem(func_5400_call(), 0)
call_6995 = relay.TupleGetItem(func_5402_call(), 0)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
var_7022 = relay.var("var_7022", dtype = "int8", shape = (56,))#candidate|7022|(56,)|var|int8
call_7021 = relay.TupleGetItem(func_2745_call(relay.reshape(var_7022.astype('int8'), [56,])), 3)
call_7023 = relay.TupleGetItem(func_2747_call(relay.reshape(var_7022.astype('int8'), [56,])), 3)
func_143_call = mod.get_global_var('func_143')
func_145_call = mutated_mod.get_global_var('func_145')
const_7056 = relay.const([5.123357,9.319180,0.250588,4.745705,-2.472059,8.671105,-4.996161,-1.790792,0.574599,-3.363371,1.367005,-5.555491,-3.130187,8.966776,1.720689,7.748860,8.711404,8.328111,3.879432,9.059855,-0.534934,-2.766254,-6.988196,7.412071,-1.385966,7.084803,1.665276,6.821891,-0.345592,0.538748,0.303727,-7.115165,0.575334,0.323144,-5.972728,2.206771,3.390133,6.992431,-4.819422,7.791307,-2.084687,-1.946510,-0.694999,5.843750,-9.477111,-0.027856,3.479667,6.539975,5.022729,-8.380378,1.286625,-3.990814,5.209503,4.331537,-0.706560,-2.715222,6.103761,6.726597,-4.355859,-2.050930,0.477792,-3.467249,0.188923,-1.657246,-7.346892,-5.656462,-6.155009,3.316661,-6.691009,4.699647,7.558135,8.636962,-6.126222,5.955055,-2.963698,0.280040,-7.316813,-2.496592,6.397200,-2.858515,2.424019,-1.936106,6.131032,-9.346368,-9.263280,2.143962,4.806271,-6.937314,7.619556,9.361850,-9.897989,1.078539,-4.665237,-0.157035,-2.918864,-3.969269,-5.264138,5.330816,-0.419924,5.873941,5.303324,-9.803612,-0.523635,-7.053056,-7.879645,8.915565,6.186494,-9.385215,-4.934722,1.212406,2.285040,4.229758,-1.875184,-1.709758,-2.984447,4.498510,-1.673292,-5.301690,9.772549,-5.381590,-4.752642,-2.992778,-6.039292,-3.843251,6.914795,-6.442504,9.241488,-3.174128,-5.548211,-5.962940,1.554101,7.426045,5.697972,-3.455036,-2.387977,8.004037,-1.377816,-5.545241,-0.891700,4.124140,7.274815,-9.880959,4.349438,-0.813192,5.616691,-5.427259,4.097510,-2.452362,-5.289951,7.201805,8.139715,8.686979,-3.714986,6.170937,-6.310033,-8.293066,-3.288585,-2.650272,-3.719018,4.983987,2.172948,-4.517753,4.013916,-2.188564,7.504085,0.884560,-8.782995,-4.100516,-4.956757,1.469493,-0.824060,-9.343763,-8.352380,7.882788,-8.667135,7.750869,-9.645215,-0.953577,-1.656084,6.427481,-9.560134,7.564495,-6.770402,7.555552,0.662371,3.125651,-7.591667,-6.120944,5.305469,9.939885,-3.358769,7.589981,-4.090992,2.880170,-3.513426,-3.957796,0.145176,0.233514,1.345561,-1.006488,1.796325,2.900344,-9.323923,5.342982,9.483545,5.524718,8.678931,-7.484607,-6.745982,-3.272395,2.133744,0.181663,-8.013532,-5.386363,5.045342,-6.979608,-8.935555,-3.424434,5.071560,-6.042863,3.443227,7.003511,9.494939,-1.439818,0.776421,-5.420585,-6.706445,3.389690,6.917453,-1.101573,-1.969462,8.660427,-9.831758,6.508019,0.301751,-4.134135,4.229144,7.472114,-3.874127,-1.007966,1.343597,-0.266278,-1.976694,-0.033759,0.698391,-4.216008,-1.771850,-9.096393,-4.910479,-8.418560,-6.653450,-7.323072,-1.968556,-2.610391,8.146582,-1.111131,1.553781,-9.137177,-2.631323,1.483620,-4.409231,-2.299037,-7.769167,7.322287,-5.759135,-5.569055,3.663618,3.063919,4.448290,-2.625581,-2.557159,6.882834,1.649501,-6.428264,-7.280693,3.678466,3.736042,8.258664,-0.067361,-1.934279,6.431441,8.194284,4.073981,-3.801075,-4.028298,-6.159329,-2.972277,2.330225,4.429149,9.568733,3.479614,-2.459156,-3.126665,-6.618195,8.201631,-4.890966,-3.958843,9.497017,-8.300932,-6.227334,-5.409702,2.539495,-9.885515,-4.476774,-0.585505,9.357138,-4.777000,2.954497,-6.769825,8.663450,-5.495747,-5.702869,-9.583303,6.554051,7.954624,6.182545,-3.106856,-9.869657,9.826391,-3.519518,7.920598,-7.866635,-4.994088,-7.590637,9.205891,-2.701425,8.430228,-8.670737,-4.353176,-9.979212,1.733296,3.534211,9.115618,-2.472899,-7.064829,-5.054007,8.193144,0.032845,-9.496412,-1.703462,9.825372,-3.611778,1.245957,-3.935161,-5.708056,8.618692,9.791397,2.706871,3.715845,6.710158,-7.326062,9.263481,-9.768794,8.623046,-1.365262,5.376618,-6.241389,6.525747,-2.387669,6.455730,-4.111831,8.706798,1.269336,-8.319141,-2.007705,-2.666216,-7.596774,-4.719596,-6.043641,3.111800,4.525628,4.576614,-9.396598,5.570328,-7.110496,3.465494,-6.900316,-2.717113,8.737047,-8.821077,4.939100,5.018942,-9.623185,-1.535949,9.209357,7.420202,-4.066414,7.005203,3.733913,-9.687102,7.496465,7.315454,-5.887221,-6.012105,-9.289993,2.202298,7.596564,1.254830,5.716043,7.010831,-0.612409,8.094991,8.098657,9.907633,-4.935906,-8.376498,-1.727785,4.530570,-3.931993,-7.568028,-6.112788,-3.875051,-7.646110,0.588060,3.250474,4.117717,0.552390,9.021594,1.116305,-2.429309,-0.466870,3.190736,-9.066256,4.818258,-3.029684,1.445994,0.188468,4.144058,-7.169360,1.605583,9.088174,7.643481,-4.326127,5.969104,9.390739,8.046518,-4.644522,-0.343615,3.540320,8.941831,-9.186413,-3.713805,-8.963970,4.255399,-8.838390,7.575732,4.792124,-9.416874,8.756662,1.913553,2.666294,-6.224961,-2.381645,-6.317292,-8.082186,9.289318,9.702434,-6.216405,6.025126,-3.937939,5.227947,6.497258,-1.731508,-3.591471,5.161076,-1.248559,-5.781853,2.593366,-1.254635,-5.462658,4.611222,5.266394,7.676644,1.166141,7.890029,-5.995846,1.685730,-2.227374,4.488918,8.960843,-0.768294,-0.123847,-3.151697,7.314017,5.765628,3.888247,-4.131099,7.525422,-4.267906,-5.008877,-3.771029,-0.464387,1.251903,5.962634,3.241542], dtype = "float64")#candidate|7056|(495,)|const|float64
call_7055 = relay.TupleGetItem(func_143_call(relay.reshape(const_7056.astype('float64'), [11, 15, 3])), 0)
call_7057 = relay.TupleGetItem(func_145_call(relay.reshape(const_7056.astype('float64'), [11, 15, 3])), 0)
func_2410_call = mod.get_global_var('func_2410')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_7062 = func_2410_call(relay.reshape(call_6994.astype('float32'), [11, 14, 5]))
call_7063 = func_2410_call(relay.reshape(call_6994.astype('float32'), [11, 14, 5]))
output = relay.Tuple([call_6994,call_7021,var_7022,call_7055,const_7056,call_7062,])
output2 = relay.Tuple([call_6995,call_7023,var_7022,call_7057,const_7056,call_7063,])
func_7077 = relay.Function([var_7022,], output)
mod['func_7077'] = func_7077
mod = relay.transform.InferType()(mod)
mutated_mod['func_7077'] = func_7077
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7078 = relay.var("var_7078", dtype = "int8", shape = (56,))#candidate|7078|(56,)|var|int8
func_7077_call = mutated_mod.get_global_var('func_7077')
call_7079 = func_7077_call(var_7078)
output = call_7079
func_7080 = relay.Function([var_7078], output)
mutated_mod['func_7080'] = func_7080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3966_call = mod.get_global_var('func_3966')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_7098 = relay.TupleGetItem(func_3966_call(), 0)
call_7099 = relay.TupleGetItem(func_3967_call(), 0)
output = call_7098
output2 = call_7099
func_7147 = relay.Function([], output)
mod['func_7147'] = func_7147
mod = relay.transform.InferType()(mod)
mutated_mod['func_7147'] = func_7147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7147_call = mutated_mod.get_global_var('func_7147')
call_7148 = func_7147_call()
output = call_7148
func_7149 = relay.Function([], output)
mutated_mod['func_7149'] = func_7149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6937_call = mod.get_global_var('func_6937')
func_6938_call = mutated_mod.get_global_var('func_6938')
call_7168 = relay.TupleGetItem(func_6937_call(), 0)
call_7169 = relay.TupleGetItem(func_6938_call(), 0)
output = call_7168
output2 = call_7169
func_7172 = relay.Function([], output)
mod['func_7172'] = func_7172
mod = relay.transform.InferType()(mod)
mutated_mod['func_7172'] = func_7172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mutated_mod.get_global_var('func_7172')
call_7173 = func_7172_call()
output = call_7173
func_7174 = relay.Function([], output)
mutated_mod['func_7174'] = func_7174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5897_call = mod.get_global_var('func_5897')
func_5899_call = mutated_mod.get_global_var('func_5899')
call_7272 = func_5897_call()
call_7273 = func_5897_call()
func_5014_call = mod.get_global_var('func_5014')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_7274 = relay.TupleGetItem(func_5014_call(), 0)
call_7275 = relay.TupleGetItem(func_5015_call(), 0)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_7289 = relay.TupleGetItem(func_2043_call(), 0)
call_7290 = relay.TupleGetItem(func_2044_call(), 0)
func_2090_call = mod.get_global_var('func_2090')
func_2092_call = mutated_mod.get_global_var('func_2092')
call_7304 = func_2090_call(relay.reshape(call_7289.astype('float32'), [11, 14, 5]))
call_7305 = func_2090_call(relay.reshape(call_7289.astype('float32'), [11, 14, 5]))
output = relay.Tuple([call_7272,call_7274,call_7289,call_7304,])
output2 = relay.Tuple([call_7273,call_7275,call_7290,call_7305,])
func_7311 = relay.Function([], output)
mod['func_7311'] = func_7311
mod = relay.transform.InferType()(mod)
output = func_7311()
func_7312 = relay.Function([], output)
mutated_mod['func_7312'] = func_7312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mod.get_global_var('func_2147')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_7313 = relay.TupleGetItem(func_2147_call(), 0)
call_7314 = relay.TupleGetItem(func_2149_call(), 0)
func_6342_call = mod.get_global_var('func_6342')
func_6344_call = mutated_mod.get_global_var('func_6344')
call_7324 = func_6342_call()
call_7325 = func_6342_call()
output = relay.Tuple([call_7313,call_7324,])
output2 = relay.Tuple([call_7314,call_7325,])
func_7326 = relay.Function([], output)
mod['func_7326'] = func_7326
mod = relay.transform.InferType()(mod)
output = func_7326()
func_7327 = relay.Function([], output)
mutated_mod['func_7327'] = func_7327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_7336 = relay.TupleGetItem(func_3123_call(), 2)
call_7337 = relay.TupleGetItem(func_3124_call(), 2)
output = call_7336
output2 = call_7337
func_7349 = relay.Function([], output)
mod['func_7349'] = func_7349
mod = relay.transform.InferType()(mod)
output = func_7349()
func_7350 = relay.Function([], output)
mutated_mod['func_7350'] = func_7350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6937_call = mod.get_global_var('func_6937')
func_6938_call = mutated_mod.get_global_var('func_6938')
call_7485 = relay.TupleGetItem(func_6937_call(), 1)
call_7486 = relay.TupleGetItem(func_6938_call(), 1)
func_4576_call = mod.get_global_var('func_4576')
func_4578_call = mutated_mod.get_global_var('func_4578')
call_7512 = func_4576_call()
call_7513 = func_4576_call()
output = relay.Tuple([call_7485,call_7512,])
output2 = relay.Tuple([call_7486,call_7513,])
func_7539 = relay.Function([], output)
mod['func_7539'] = func_7539
mod = relay.transform.InferType()(mod)
output = func_7539()
func_7540 = relay.Function([], output)
mutated_mod['func_7540'] = func_7540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4682_call = mod.get_global_var('func_4682')
func_4684_call = mutated_mod.get_global_var('func_4684')
call_7560 = func_4682_call()
call_7561 = func_4682_call()
func_5741_call = mod.get_global_var('func_5741')
func_5745_call = mutated_mod.get_global_var('func_5745')
var_7579 = relay.var("var_7579", dtype = "uint16", shape = (1560,))#candidate|7579|(1560,)|var|uint16
const_7580 = relay.const([0.215017,-9.195483,3.769543,-0.152824,-6.936224,-9.260837,-9.308477,-4.085613,1.903587,6.247877,-1.912940,-9.213463,-0.688753,9.154070,6.551348,4.987283,1.000310,1.150730,-5.650976,-1.893926,-6.269578,-4.905895,8.528207,-0.683979,7.623743,9.904844,-1.104762,-6.470485,2.961552,7.070861,-1.336331,-9.464055,-3.099684,-5.473125,4.689281,-9.339496,0.939806,-0.758534,1.695954,5.384284,8.342088,-6.048568,-5.030218,-6.485447,-7.983576,9.842325,6.015208,4.647037,5.898069,-6.872268,-9.441175,-1.444792,-5.905652,-3.249863,8.685609,-2.537172,-4.034018,6.946396,3.866714,-3.250588,6.719953,-3.909383,2.909692,-1.751279,6.015077,9.666928,9.384768,4.901758,5.124233,-3.744603,3.400721,4.323970,2.144080,8.777048,-3.721264,3.787109,2.032164,-9.745420,5.381993,4.040152,-3.133125,-7.767774,-7.573338,0.563053,8.562285,1.124363,-8.512397,-5.171636,6.045281,-4.540600,6.326023,2.765845,1.402303,-9.945639,-4.800080,7.370282,-6.827328,8.182679,3.291131,-7.706646,-8.080174,3.311313,-2.037450,-8.441228,5.275711,-5.145117,-2.589438,0.632091,9.288835,-5.592643,6.347250,-4.011113,1.633995,2.178050,-2.405329,3.398965,1.006017,0.489926,-1.541309,3.775353,-5.487505,6.661199,8.191029,-7.747661,-0.433383,-3.939659,-6.129664,8.362947,-0.302980,-8.856821,3.646457,4.730862,3.757763,-4.317095,1.582756,9.668378,8.175256,-1.537930,-7.175938,-0.713310,-7.509541,-9.847503,8.752924,-1.172685,-1.142422,7.323549,4.905194,-2.735252,4.263614,-7.111953,-2.904673,4.203684,-4.820368,-6.347263,-5.972664,3.628611,-4.906322,-0.467129,-7.406247,2.542196,9.213540,-1.647827,-4.124396,3.510740,6.237534,-3.734014,-9.597763,-1.876414,8.679185,9.788164,6.031446,-6.893909,-6.633407,5.182409,-9.442509,-1.394707,4.895211,-4.227276,7.768605,-2.967006,3.514594,1.699334,-4.531151,2.923191,-3.530097,1.499691,3.969046,6.390227,-9.167514,-4.908560,-7.502618,0.346160,3.113986,8.572463,3.518483,-8.984615,-9.540182,-0.428550,6.918994,-5.076652,-7.297733,0.355192,-3.384016,-6.849626,0.833470,8.182641,6.893879,-6.064657,-5.557671,3.300861,5.832774,-9.905714,1.629438,-3.109156,-4.064341,0.689484,-7.351912,0.248382,9.951600,-8.806851,-5.412710,-5.280938,-2.914304,2.117696,-2.841559,-6.972758,-7.991456,1.052513,-9.048388,-5.988996,8.664682,8.294223,-0.506105,-9.562846,-5.863245,-3.651987,-4.420749,-8.830935,0.315495,5.283040,2.310963,8.846939,-0.201623,4.922742,-9.419415,-5.175922,3.303000,-8.034212,-4.233117,-3.954711,8.636772,6.585516,7.163360,-5.235311,2.749942,5.625262,7.753714,-0.147983,6.778234,-4.923516,1.837252,3.455038,4.546519,-3.847563,-6.615334,-0.917448,-5.421101,4.750594,-5.176154,-7.574616,6.253100,-5.379629,7.720592,0.724427,-6.607189,-4.925578,-6.517134,7.047585,8.505241,7.323905,-1.910748,0.044265,8.405485,-6.428432,-6.267440,-0.760322,-7.085927,2.286182,7.685358,5.964891,-9.376882,-3.488625,0.852862,-7.557168,1.885995,1.690705,-2.827660,-5.033962,0.299029,6.483896,-4.345980,-4.927514,-3.396628,-0.441000,-8.586115,6.871724,3.599809,4.645683,3.993188,-4.309966,0.178630,-4.196234,-9.127100,0.716727,-2.879822,-1.437518,-8.032427,7.538972,-7.377010,1.742936,6.319864,2.071268,-2.433877,-6.295078,5.329131,-5.057248,-5.022939,-5.087378,-9.181994,-5.384967,-6.168938,1.294230,6.322846,9.474149,-5.922503,-2.815519,2.556748,-5.460971,-4.824657,-9.296119,2.954615,-4.602869,8.394762,4.797016,0.755341,-5.912388,-4.277982,-2.070448,3.840962,1.918260,-3.536185,9.676408,5.892010,5.145156,-2.632172,9.649277,9.513959,4.613717,-3.927045,-1.630750,7.057524,2.236429,-9.441061,7.068036,7.788243,8.803767,0.168026,-8.555837,-5.085624,-8.678069,6.878283,5.625035,-5.649185,2.970724,2.400028,-3.340827,1.551682,-6.930962,9.282152,8.837688,-3.706203,8.153108,3.456889,-1.107858,8.696306,2.940964,1.894936,8.948980,9.378853,-9.510552,-7.497753,1.357864,4.831551,8.396241,-5.823534,1.263084,8.104655,-2.831212,-5.446181,9.080285,3.518544,-2.447954,5.282308,-5.389409,2.667967,7.726289,2.312912,8.778580,-6.833359,-9.702185,1.704079,7.393799,-8.387525,4.022447,-5.145927,-4.051049,3.767799,-6.002541,6.997868,-5.996245,-6.908383,-0.412894,-8.496018,-4.051901,9.530837,3.603239,-2.072268,8.519728,-5.221711,-9.396740,5.276281,9.869831,2.760275,0.180906,-5.239872,8.893369,0.598478,4.979438,0.103875,-4.104228,-3.879911,6.156575,-5.779259,7.323069,-2.603765,-2.512103,-3.793177,-8.603404,1.259473,-8.327733,3.801684,-5.174114,-7.291743,3.261668,1.537179,-4.437805,2.392437,3.759816,-5.069243,5.884951,-2.579691,7.807008,0.987445,-4.938094,0.374856,-3.750800,2.258790,-5.385350,-2.926969,6.808852,3.616173,6.721437,-2.936167,6.804685,2.167154,4.572746,-7.151891,8.734267,-0.883951,-4.006155,-4.798869,7.362110,-7.043596,4.708045,5.811730,-6.990657,-8.606223,7.028960,-7.671983,-8.071987,7.564052,4.387951,-2.973384,3.393319,7.913796,-4.123087,3.612482,3.242192,6.546801,-1.957310,8.933215,-0.336676,8.425376,-6.714912,-9.873379,1.397813,-7.822291,0.594988,3.383683,-3.428081,-9.578513,4.639882,-1.650408,0.042560,7.725936,-2.310288,2.451052,1.296625,-1.379625,-6.392317,-8.271574,8.108552,6.045147,8.520919,0.021427,9.819915,-8.166423,3.673134,4.078915,3.635842,9.925669,9.139633,-0.093571,9.371480,5.237850,1.822830,9.096776,-0.943078,4.462931,-2.150518,6.286876,-5.416207,-9.915488,-9.997573,8.735543,-4.444157,9.281541,6.663880,-0.489752,3.128751,-7.761850,4.949485,6.419241,-9.120101,5.419556,9.580185,-5.132510,9.508489,-5.097807,-5.784517,2.752880,-5.602655,7.381600,-0.632702,-6.347084,0.029170,-2.574856,-2.304866,-0.114733,-4.342698,3.122976,5.756781,8.459952,-0.976161,-9.827584,7.903133,-4.286293,9.276054,9.284853,7.725433,8.283393,8.632090,-2.219486,4.945715,-7.976506,-7.463651,2.828686,-0.037430,-9.332424,-0.013687,8.771582,-5.260210,3.052148,5.919547,3.685097,-5.755071,8.994227,-2.639225,-4.639874,3.242185,8.987808,-6.076546,6.666230,-1.809990,-0.509430,-4.690619,-9.898421,3.676706,-7.138390,4.002242,1.603739,-3.992060,0.444651,-2.649722,-5.958172,-0.187955], dtype = "float64")#candidate|7580|(616,)|const|float64
call_7578 = relay.TupleGetItem(func_5741_call(relay.reshape(var_7579.astype('uint16'), [13, 15, 8]), relay.reshape(const_7580.astype('float64'), [616,]), ), 6)
call_7581 = relay.TupleGetItem(func_5745_call(relay.reshape(var_7579.astype('uint16'), [13, 15, 8]), relay.reshape(const_7580.astype('float64'), [616,]), ), 6)
output = relay.Tuple([call_7560,call_7578,var_7579,const_7580,])
output2 = relay.Tuple([call_7561,call_7581,var_7579,const_7580,])
func_7591 = relay.Function([var_7579,], output)
mod['func_7591'] = func_7591
mod = relay.transform.InferType()(mod)
var_7592 = relay.var("var_7592", dtype = "uint16", shape = (1560,))#candidate|7592|(1560,)|var|uint16
output = func_7591(var_7592)
func_7593 = relay.Function([var_7592], output)
mutated_mod['func_7593'] = func_7593
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7602 = relay.var("var_7602", dtype = "uint32", shape = (16, 10, 12))#candidate|7602|(16, 10, 12)|var|uint32
const_7603 = relay.const([[[-9,1,3,7,-6,-1,10,-10,7,-2,-9,-6],[4,1,10,-2,-5,2,4,-3,6,3,-7,-6],[4,1,-6,6,2,6,5,10,-2,-7,2,7],[6,-4,3,-7,10,2,-8,8,6,-1,3,-1],[4,3,2,3,-2,-10,9,-3,7,8,6,7],[-1,2,-8,1,3,-7,6,2,9,2,-1,-8],[2,6,-2,-9,9,-9,4,-8,-5,-1,-5,8],[7,3,-7,-6,8,7,7,5,7,5,-5,10],[6,-1,-8,-6,-1,3,-9,-6,-3,9,9,5],[7,9,3,-1,5,-1,-1,6,-5,9,-7,2]],[[-8,-1,-2,-4,6,-10,5,9,1,10,6,-5],[4,6,-9,-3,-7,3,-1,-8,-10,-8,-10,-4],[-9,-5,10,-8,4,-8,-10,9,5,9,-6,-7],[-7,-3,3,8,-10,9,-4,6,10,-10,-7,10],[-10,-10,-7,-5,3,9,-3,-10,-1,7,-5,-3],[7,5,-2,-7,-5,-9,5,5,1,-8,3,9],[6,-1,-9,3,-8,1,5,-2,-7,3,6,2],[3,2,-7,-2,-9,1,5,-7,6,5,-5,4],[-8,4,4,-1,-5,3,-8,-2,-7,-8,-10,-7],[2,-8,9,-9,-10,2,8,-10,-8,4,9,-4]],[[10,9,6,4,8,-5,5,-7,-6,8,-2,-8],[3,-10,-7,-9,6,-4,-5,-10,-2,3,8,4],[-9,-9,-5,5,8,-2,-10,1,10,10,-6,2],[7,9,5,9,-8,-7,7,10,-5,-2,5,3],[-9,-5,-5,-4,2,8,-7,-1,7,-7,-10,-4],[1,-2,-9,2,-7,-4,-3,5,-2,-5,1,-5],[6,5,-8,2,4,6,8,1,6,-10,-6,8],[-9,10,-1,-8,-4,4,3,3,-2,9,8,5],[-7,-5,-1,2,6,-10,6,5,-5,4,-6,3],[8,8,-4,-10,-2,-6,9,-5,-10,3,6,-8]],[[8,-7,10,4,2,4,7,-4,2,-3,8,6],[-4,-5,-7,-9,4,-1,4,4,7,1,-5,-4],[7,-8,5,4,-2,-10,-4,6,-5,-4,-10,6],[-6,3,3,8,7,4,9,1,-9,-2,2,-2],[-5,-5,-5,-4,7,2,-7,10,6,7,-4,-9],[-1,-7,-9,7,3,10,-4,-9,-4,-3,-3,6],[-6,5,1,-2,-4,-3,-8,-8,-4,-1,3,-1],[4,7,-6,-7,3,-4,-5,-7,7,-2,10,-8],[-8,-3,2,7,10,1,8,10,-9,6,-3,1],[-2,-7,-4,-9,5,-5,-7,-2,8,-3,-1,-8]],[[9,4,-8,6,-9,4,-9,8,-4,2,5,8],[-7,-2,6,-1,-5,-1,-2,-4,-9,6,3,3],[-7,9,-8,7,-8,6,-8,-10,-1,-7,7,4],[4,-5,4,-4,-4,-4,8,2,2,-1,-4,-5],[-4,-10,8,7,3,-8,-2,9,3,-10,9,-8],[-9,-1,-2,2,1,-6,-3,2,5,-5,2,4],[-9,8,-8,1,7,-2,10,-4,-5,3,-3,6],[-5,-6,-4,10,-7,-5,5,2,-8,3,-10,1],[9,-5,-9,2,-9,8,-1,1,7,2,-10,7],[1,-7,9,8,2,-10,-2,2,3,9,8,-1]],[[-5,-10,7,4,7,1,-9,-4,2,-1,-10,-8],[-3,-8,-6,-10,4,-6,7,-3,9,-2,2,-9],[-4,1,-5,9,-5,-1,-8,1,-2,6,-7,6],[10,-4,8,9,6,-5,8,-9,3,-3,2,4],[1,3,-7,-5,9,-1,5,-8,-9,-1,9,1],[9,-2,10,-5,3,10,-9,9,4,-4,10,-1],[-6,-10,-10,8,7,-2,-5,-9,-5,10,-3,1],[-9,-10,8,1,-2,3,-2,-3,1,5,10,-6],[-10,-10,-7,4,-5,-8,4,1,10,7,-2,-10],[-4,1,-6,1,-7,-1,-2,-2,-9,-2,-10,6]],[[6,2,6,3,5,-5,2,9,7,-6,4,7],[-8,6,-3,-8,8,7,9,3,3,-7,4,-6],[5,-1,10,4,-9,8,3,-9,5,4,-5,10],[-4,6,-2,-8,-4,7,9,6,10,-7,9,5],[-3,9,-5,-7,7,-7,-6,7,-6,-8,8,2],[-7,2,-7,9,5,8,-9,6,-8,7,10,8],[2,10,9,7,-2,-1,5,9,-9,9,3,4],[-10,9,-6,-5,-2,-8,6,-8,-4,7,8,1],[-4,5,-8,9,1,8,-5,-6,6,10,9,2],[7,-7,7,4,8,9,10,6,5,1,-4,7]],[[-2,6,6,-9,7,-10,1,6,-5,7,-2,-1],[6,-7,10,2,2,5,6,-3,-7,-9,-8,2],[-9,-1,4,8,-3,-10,-10,6,10,3,5,-1],[8,-5,-7,10,-7,-9,-2,-1,-3,-9,-5,8],[-6,3,5,-8,-4,-9,-1,6,-9,-9,1,7],[2,8,9,-3,5,8,10,4,8,-4,2,7],[7,2,7,-2,3,8,-6,-1,-7,-4,5,-2],[1,4,-7,3,-8,-2,6,7,7,-3,6,-5],[-3,3,-7,2,10,9,6,3,-1,-10,2,6],[3,-10,3,4,-6,-5,2,9,3,9,-4,-5]],[[9,1,3,9,-9,4,6,-10,-5,-5,2,8],[6,9,2,-6,-9,10,-4,-5,10,5,-7,8],[1,8,-7,-1,4,2,3,-6,-5,-2,5,-2],[-7,3,-3,8,4,7,2,4,-7,-1,6,-1],[-4,-10,2,-6,-10,-5,-9,6,8,-5,-1,-6],[7,1,5,-4,6,-9,-7,-9,3,-9,6,-6],[-1,5,-9,-2,-8,-2,4,-3,-10,-9,7,-4],[-4,3,-10,-6,-9,3,-2,6,8,5,4,2],[-8,10,1,-8,-9,-6,-9,2,-3,-7,9,-7],[3,-9,-9,10,-4,-5,-6,-1,-3,6,9,-9]],[[2,-7,1,-8,-7,-9,9,-6,-2,1,3,5],[-9,7,8,10,3,-2,5,-7,8,9,-7,-2],[5,9,5,3,4,4,9,1,-3,-4,-3,-1],[1,10,-4,-9,8,-6,-1,-9,-2,-4,-6,10],[-9,10,-9,5,-10,10,-1,-2,6,-2,-8,1],[-5,-10,1,2,6,2,-4,5,-5,-9,-3,-5],[-8,5,9,5,-2,-5,-5,-3,-3,-6,3,1],[6,4,1,-8,8,7,3,3,7,6,-7,4],[-5,6,-4,8,9,9,3,8,-5,1,7,3],[2,-9,-10,8,5,-3,-3,9,5,1,-7,9]],[[6,-2,-4,10,-4,-6,3,-10,-9,5,6,-5],[4,-10,7,-5,-1,-9,-1,2,7,10,5,-6],[2,8,7,-8,-9,4,-8,-10,-5,6,7,1],[-8,-4,8,-7,5,-6,-9,5,-5,-6,5,3],[-7,6,-9,-8,8,9,-3,-4,-2,-1,7,10],[3,6,-4,-10,8,-2,2,1,1,-6,8,3],[2,-2,-9,2,10,10,5,-4,-5,-9,8,9],[-1,6,-4,-9,2,-5,6,3,-3,10,2,-2],[-2,-5,2,2,6,-3,6,5,3,-10,-7,-5],[-5,-10,-10,-3,-3,3,-10,-9,2,7,3,-9]],[[-3,-7,10,-3,-8,-2,-5,-1,1,4,-8,10],[-6,-9,2,-7,-4,7,10,-1,-3,7,7,-8],[1,-2,6,8,-10,1,2,6,4,-2,-5,3],[7,8,9,2,10,6,5,-8,-10,4,-8,-7],[-8,-9,3,3,-3,4,8,9,-8,-6,8,8],[4,9,4,4,-7,3,4,-2,8,6,-9,-6],[1,-2,7,-8,-1,10,-5,5,9,3,-5,-10],[-10,1,-3,-8,10,-3,9,-7,-10,-4,-3,-8],[9,6,6,-9,2,8,8,8,-6,-6,-4,-3],[-1,-1,6,-7,-1,-8,-6,-5,-6,4,9,-3]],[[-4,-9,-1,-7,1,-7,5,3,6,5,8,-10],[5,10,7,8,-2,4,-1,-8,-6,9,-8,9],[6,5,6,-10,-1,-4,6,2,10,3,-6,2],[-5,-5,-5,-8,2,5,-1,10,7,-2,7,3],[1,-9,-9,1,1,-9,-2,-7,10,-4,-7,5],[-8,7,3,3,5,1,2,-10,-7,9,-5,6],[8,-8,-2,-9,10,-6,-7,4,-10,6,6,4],[4,-5,-2,6,-10,-5,7,-5,-1,9,1,-9],[-10,-4,2,2,-3,-7,-7,-5,9,-1,5,5],[-8,-3,10,3,-1,-8,5,1,6,-3,2,2]],[[-7,10,-9,-7,9,-10,-5,1,-10,-9,9,-4],[-7,-8,6,-10,2,-4,-5,2,4,5,4,5],[2,-2,-1,6,5,7,-3,-4,-5,8,1,3],[1,-3,1,1,-2,-6,9,-3,5,6,6,-5],[-8,10,2,-5,3,-9,7,-2,5,4,-10,-10],[6,5,6,5,-2,3,10,8,-7,-10,9,3],[-9,-7,3,-6,-1,-3,10,1,2,-9,-4,-8],[3,3,-9,3,-3,-5,-8,-7,1,-6,-7,6],[-2,2,1,7,7,6,-8,1,9,-10,-8,-6],[7,3,-10,1,-1,10,-4,-6,6,-6,10,6]],[[5,8,2,-4,7,-3,6,9,-9,-1,-5,-6],[8,-5,-9,-10,8,-10,4,-9,3,6,-8,-9],[5,1,-7,-10,7,3,-8,-4,3,-7,10,-5],[-10,4,-9,4,-3,5,2,-4,3,-8,-2,-7],[6,3,-2,1,-1,-9,-10,-6,9,-2,7,1],[5,10,2,6,1,-4,-8,-4,-1,-1,7,-3],[-1,7,-5,9,-8,9,8,7,-7,-2,-5,-5],[-1,-9,-6,-5,9,4,-10,4,-1,9,-2,-9],[-7,-1,-9,-1,5,-9,2,7,-5,5,-1,5],[-6,1,1,5,3,10,-4,-4,-1,-9,6,6]],[[4,-9,4,9,10,-8,-10,-9,-10,-4,-10,-3],[-1,5,6,-9,5,-7,3,9,-8,4,-7,-10],[2,1,-2,4,-7,-1,2,-5,-7,8,-2,3],[1,5,-2,6,1,-7,-4,-4,-2,3,-4,-3],[-5,-3,7,5,5,7,-9,1,-2,10,-9,-4],[1,7,10,-8,-2,-1,7,6,-10,-1,-7,6],[3,3,2,5,9,-9,-3,-3,8,-5,-4,8],[5,2,4,-1,-7,8,-6,-3,6,-3,8,5],[3,-10,-10,-2,10,7,5,-10,6,2,-3,-6],[-6,10,-8,10,7,-8,-10,2,-6,3,-10,-2]]], dtype = "uint32")#candidate|7603|(16, 10, 12)|const|uint32
bop_7604 = relay.minimum(var_7602.astype('uint32'), relay.reshape(const_7603.astype('uint32'), relay.shape_of(var_7602))) # shape=(16, 10, 12)
func_4745_call = mod.get_global_var('func_4745')
func_4748_call = mutated_mod.get_global_var('func_4748')
const_7615 = relay.const([-3,-1,3,6,-5,9,-1,-10,-9,-6,-7,9,9,-9,3,8,-8,-4,8,-10,-4,8,-8,-8,3,5,-6,-1,10,-5,-5,9,-5,-6,-3,-8,5,-6,2,9,-7,-9,-1,-7,2,4,-6,-3,-5,4,3,-9,-7,1,-9,9,7,1,8,-8,2,10,-6,1,-9,-1,6,-3,5,6,-6,-3,5,-8,-4,5,-10,-5,7,-8,-10,1,9,3,-9,1,6,-6,-10,3,-3,-1,3,-9,-4,7,8,-4,-3,2,-7,-5,6,3,-8,-9,5,5,-8,8,-3,-7,-4,-7,-9,-1,9,7,-9,-1,-7,9,-10,9,9,9,-2,-1,9,-5,7,3,2,-3,-2,-8,-5,-8,1,3,5,-10,-2,3,-10,-10,-4,5,4,-9,-2,-5,3,-4,-1,4,10,-2,6,-2,8,3,6,8,-8,6,3,9,-5,4,-9,-3,-2,-9,-4,7,4,4,8,10,10,-7,9,2,-8,-1,3,-4,-3,-5,6,9,-2,2,4,7,1,-8,8,4,4,-3,-1,4,-1,-1,3,-9,-10,4,-4,-7,-4,5,4,-8,-7,7,-9,2,-2,-9,10,9,-10,3,5,-10,6,1,-5,10,1,9,-10,9,1,-8,-5,-2,-1,8,-6,7,4,-6,6,-10,-3,6,-10,-7,1,6,6,1,-3,-5,7,-5,-7,-1,-6,1,-10,5,2,-2,9,10,-6,-3,10,-9,10,-10,-4,-2,-2,10,-4,5,-6,10,5,-3,1,-9,5,-9,-2,4,2,4,10,9,8,-1,-10,-4,-1,7,4,-4,-6,4,2,3,3,-9,3,9,9,-10,1,6,-2,5,-1,-4,9,-4,-7,6,-8,5,2,-7,-3,4,2,5,2,-9,-6,9,-3,8,-2,10,-1,3,8,-8,6,7,9,1,2,4,5,5,8,7,-10,-2,-3,-8,-5,-4,-8,1,2,1,-4,-2,-10,-6,-2,10,4,-7,-7,10,1,6,-4,7,1,-10,2,-5,-10,-3,-5,-6,-5,6,6,-5,-9,-6,-10,-10,10,-7,3,7,2,-6,10,-10,5,-6,-1,9,4,6,10,-4,-8,-3,2,4,9,-4,4,-6,9,3,7,-1,-9,4,3,-10,-10,1,4,-9,-7,-3,-7,3,3,6,-8,-10,6,-8,3,-1,10,6,-9,-6,7,9,-8,-10,10,10,4,7,-3,10,-3,-8,3,7,-10,8,10,-1,-4,1,8,-2,-1,-6,-3,10,-9,9,6,-6,8,-4,-3,-9,8,1,-1,-2,-1,7,-5,2,-9,8,8,10,9,-6,-10,1,5,6,2,-8,-6,-9,-6,-9,-3,-8,2,-6,-3,3,-7,3,-6,-8,9,-3,5,-10,-2,-3,7,-3,1,-9,-2,-8,-9,-1,-2,-3,-6,-7,-8,-1,-5,3,-6,-8,6,3,-10,-8,-4,3,-7,6,-3,-6,10,-1,-2,5,-1,-6,10,6,2,10,3,3,-2,-7,2,7,-1,-4,-1,2,2,2,9,4,1,9,-7,-8,-1,-5,-8,-4,-9,3,-9,-3,-5,3,-2,-7,-2,1,-9,10,1,5,-6,-10,9,-6,-8,-9,3,-7,10,-1,8,-2,8,9,7,-3,-4,7,-6,-2,-3,7,5,-2,6,7,-5,3,1,7,7,-1,2,-4,3,3,7,2,2,4,1,-3,2,-2,-9,1,8,7,-9,8,-7,8,9,-3,-7,-10,-2,-5,-9,7,7,-6,-9,-4,-5,2,5,5,3,-6,9,-9,9,5,-2,-7,-8,3,-7,-8,1,-4,10,-10,-9,5,4,-9,9,-10,4,-1,10,2,1,8,9,-8,-3,-4,-9,-10,-5,4,3,-7,1,1,-2,-7,-2,4,-8,2,5,2,5,6,3,5,6,-4,2,8,-10,-6,1,4,6,-1,-2,-4,-6,-8,-10,4,-7,-3,-4,2,6,-6,7,6,-8,4,-9,10,9,-4,-10,-3,9,-5,-6,6,-4,9,-4,7,-2,-3,-9,8,-10,-7,3,9,-5,-6,3,3,6,-1,8,4,8,3,-10,-7,3,1,5,9,-6,1,9,-7,9,-7,5,-7,7,-4,10,7,7,-1,-8,2,-7,3,8,-3,9,4,-9,1,-2,3,6,5,-8,6,7,1,-1,-2,-8,8,2,3,4,7,7,-7,-2,8,9,7,2,-1,-6,-1,-7,2,-2,1,7,1,-10,10,-1,3,4,7,1,8,3,2,10,-9,6,-8,10,8,-8,-3,9,-10,-5,9,-6,-3,-6,-7,6,-9,-8,7,6,9,6,-6,7,9,4,-7,-5,-9,5,9,4,6,-5,-1,2,7,-3,4,9,-1,9,5,-10,7,10,9,-4,-9,1,9,1,1,9,3,7,2,4,2,-2,1,2,10,-8,4,9,1,9,6,-7,5,3,-2,5,-10,10,10,1,8,7,9,7,-9,-3,-4,6,-4,9,5,-9,-2,4,1,-2,-5,2,8,-3,6,4,6,-1,8,-8,3,-5,4,-7,-7,7,7,-7,1,-1,-7,6,4,6,7,-2,9,7,7,2,2,-7,1,5,-3,8,3,3,-3,-9,3,3,9,9,6,3,1,9,1,3,-2,5,-8,5,7,4,-5,4,-8,3,4,-2,-3,8,-6,-9,-3,4,-3,5,-2,2,7,-3,-8,-7,-10,9,9,-9,-8,3,-5,5,7,9,-10,-7,6,-1,6,-9,6,-10,-5,10,-9,7,2,-9,-3,-8,-9,1,5,-4,-10,7,-10,3,-6,-1,7,-7,1,8,6,10,-3,5,-2,10,1,-8,-4,8,-5,7,8,-3,-3,6,6,-7,4,-8,-10,-8,8,3,10,-4,-10,-9,6,-9,2,8,-9,9,-8,2,7,-8,10,7,-3,-5,3,-3,-5,-7,8,-4,-2,-4,2,-8,-10,4,-10,-9,3,9,-9,6,-7,-10,-10,-3,9,-3,-5,-8,9,-4,4,-3,-9,-2,7,4,-10,-10,-1,3,2,9,-8,4,-10,6,4,-10,4,-3,1,-6,2,-3,10,-10,-3,2,7,-9,-6,10,8,5,1,4,5,-5,7,1,4,-10,2,10,-7,6,-6,3,6,6,6,-1,2,-10,-4,4,2,-6,-5,-4,3,-4,-8,-3,-5,-4,-10,1,-1,-1,-2,2,1,8,2,6,4,6,-9,6,7,2,-5,9,4,10,7,1,9,3,3,-1,-1,9,-6,-1,-5,10,8,5,-9,9,8,-3,-1,-2,-6,-3,10,7,7,8,-3,-1,8,-2,-10,5,10,6,-4,6,-1,-9,3,4,-3,1,3,-4,5,-9,6,-4,4,8,10,10,-6,-2,-4,-6,-1,3,-6,-4,-5,-7,-9,-9,-5,-2,4,-6,-10,7,5,9,10,-7,-2,-1,-7,10,-1,10,-6,1,-2,-10,3,6,-3,-3,8,-1,-2,7,-3,5,6,2,-6,3,9,-2,-1,10,3,6,3,2,-2,-7,6,8,5,-3,2,3,-9,2,3,-5,5,-8,9,-6,-10,5,-4,7,3,-2,-8,-4,2,-9,10,-1,-5,5,-10,-6,-5,6,4,-9,-5,-1,10,2,-3,-4,4,10,-6,-5,8,-7,-2,2,-8,4,4,8,9,3,-10,-5,-6,-6,-9,-9,4,-10,10,-4,-3,-4,2,-10,-2,2,-3,8,1,-10,-7,-9,-6,7,1,6,8,2,6,2,8,-1,1,8,5,4,8,1,4,-2,9,-10,2,6,7,-5,2,-4,7,-8,-2,2,-8,6,3,7,-9,-9,-3,8,-3,-3,-1,1,-8,8,-1,-2,7,1,9,10,-6,-1,-3,9,4,-4,-6,2,-2,-6,5,2,-9,2,2,7,2,-9,9,-3,-9,-9,-2,10,3,6,7,10,2,5,-5,-6,-2,-3,2,-5,5,-7,-5,8,5,6,4,10,-9,2,7,10,-2,10,1,6,-7,10,9,2,5,-6,3,5,-10,7,-4,7,-1,1,-2,5,-9,3,-6,2,2,-10,-5,-8,-1,-2,-1,-2,-6,4,9,9,-8,-6,9,6,5,8,-1,6,-1,-9,-7,-7,-4,-5,2,-1,-6,5,-4,-7,-8,-10,1,-3,4,7,2,8,-4,-9,7,-7,6,10,-4,10,2,-1,7,7,3,-5,-9,1,4,-2,-1,-3,2,8,10,7,1,7,9,9,10,-9,5,-2,1,1,4,8,9,1,-7,3,4,3,-6,9,6,-4,-7,1,2,-9,-8,-10,4,-8,10,6,3,-1,-4,6,-6,3,7,-1,-8,3,7,4,-7,-2,-4,-4,10,8,4,3,4,-5,-10,10,-9,5,-10,-7,9,-5,8,2,3,-1,3,10,10,8,4,-9,5,-8,10,2,-5,-4,6,-2,-5,-7,4,8,3,-3,6,-9,-3,3,-4,-7,-2,3,-9,7,5,4,3,3,-8,4,-8,4,-2,9,4,3,8,-3,1,1,-8,-7,-5,-7,-9,-6,4,2,-8,9,8,-7,-2,-3,2,8,9,1,8,-8,8,5,5,-9,-8,-5,4,5,4,-8,-2,-8,-4,8,6,-8,-1,8,10,-8,-6,7,5,-4,9,-5,8,3,-10,-3,-6,-1,-6,2,-4,6,-1,10,6,3,7,6,1,9,-10,-8,-5,-1,7,9,-4,-3,-10,1,8,9,3,-5,5,-6,8,1,-2,-6,-8,8,10,6,-4,-5,-2,10,-2,-8,8,-1,-7,-4,7,-5,7,-8,7,-6,-3,-5,-5,-10,1,3,-3,8,1,8,1,4,9,4,5,6,3,3,-8,5,3,9,-6,-4,8,-4,5,7,-1,-9,3,6,-7,-3,2,-2,-8,10,7,-1,-8,-6,-5,9,5,2,-3,1,-7,-7,-4,3,2,-6,-9,-6,1,10,-4,-10,6,5], dtype = "uint64")#candidate|7615|(1859,)|const|uint64
call_7614 = relay.TupleGetItem(func_4745_call(relay.reshape(const_7615.astype('uint64'), [13, 13, 11])), 0)
call_7616 = relay.TupleGetItem(func_4748_call(relay.reshape(const_7615.astype('uint64'), [13, 13, 11])), 0)
output = relay.Tuple([bop_7604,call_7614,const_7615,])
output2 = relay.Tuple([bop_7604,call_7616,const_7615,])
func_7631 = relay.Function([var_7602,], output)
mod['func_7631'] = func_7631
mod = relay.transform.InferType()(mod)
mutated_mod['func_7631'] = func_7631
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7632 = relay.var("var_7632", dtype = "uint32", shape = (16, 10, 12))#candidate|7632|(16, 10, 12)|var|uint32
func_7631_call = mutated_mod.get_global_var('func_7631')
call_7633 = func_7631_call(var_7632)
output = call_7633
func_7634 = relay.Function([var_7632], output)
mutated_mod['func_7634'] = func_7634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6731_call = mod.get_global_var('func_6731')
func_6733_call = mutated_mod.get_global_var('func_6733')
call_7673 = relay.TupleGetItem(func_6731_call(), 0)
call_7674 = relay.TupleGetItem(func_6733_call(), 0)
func_7311_call = mod.get_global_var('func_7311')
func_7312_call = mutated_mod.get_global_var('func_7312')
call_7689 = relay.TupleGetItem(func_7311_call(), 3)
call_7690 = relay.TupleGetItem(func_7312_call(), 3)
func_672_call = mod.get_global_var('func_672')
func_676_call = mutated_mod.get_global_var('func_676')
var_7694 = relay.var("var_7694", dtype = "int32", shape = (1056,))#candidate|7694|(1056,)|var|int32
call_7693 = relay.TupleGetItem(func_672_call(relay.reshape(var_7694.astype('int32'), [11, 8, 12]), relay.reshape(var_7694.astype('int32'), [11, 8, 12]), ), 1)
call_7695 = relay.TupleGetItem(func_676_call(relay.reshape(var_7694.astype('int32'), [11, 8, 12]), relay.reshape(var_7694.astype('int32'), [11, 8, 12]), ), 1)
func_6731_call = mod.get_global_var('func_6731')
func_6733_call = mutated_mod.get_global_var('func_6733')
call_7719 = relay.TupleGetItem(func_6731_call(), 0)
call_7720 = relay.TupleGetItem(func_6733_call(), 0)
uop_7732 = relay.log(call_7693.astype('float64')) # shape=(11, 15, 3)
uop_7734 = relay.log(call_7695.astype('float64')) # shape=(11, 15, 3)
func_5576_call = mod.get_global_var('func_5576')
func_5581_call = mutated_mod.get_global_var('func_5581')
const_7736 = relay.const([-7.673504,3.125355,5.065366,0.103245,3.377785,3.043905,-7.663037,-1.517691,-9.140819,8.007092,1.744669,-6.505144,3.136386,7.453828,1.061854,-3.930151,-5.967195,-2.624246,3.540353,-5.323249,8.921023,3.777053,-3.997540,-4.610892,-8.489239,-3.330232,9.251644,-6.732815,7.603884,8.648484,3.755194,-9.437297,-2.613263,4.310872,-6.015759,-1.517708,-5.900938,-4.972234,3.738098,0.507314,-2.509213,4.454649,-2.629256,-8.137317,5.800194,1.440404,6.968731,-7.477890,-0.161523,7.256168,6.691304,-8.420559,6.142791,-9.857023,7.740021,2.958347,-4.967435,-0.084860,-5.683761,-3.288377,-5.960538,-4.275652,2.709494,9.760226,6.987590,-0.217839,-3.091783,-3.393394,9.778767,9.487149,-4.769800,7.230560,5.292963,-1.945033,-9.794477,-4.618010,-2.609852,3.895791,2.542481,7.617291,0.067876,-7.131013,-5.817250,-4.885632,2.071552,-6.652011,-8.897918,-3.036607,1.909384,4.718373,9.645310,7.414195,3.300389,4.366167,6.480480,2.596640,7.459480,7.664825,-7.056880,5.075846,6.633209,9.443573,3.876698,4.088435,-8.966442,1.364283,-4.659398,0.231876,0.481704,9.948976,2.796471,0.328203,-1.330525,-9.223323,-4.595535,-9.546087,-3.343826,4.340541,-8.976898,-2.457895,-5.841731,-2.467936,-3.302106,-2.962036,7.122502,1.839480,-0.480759,5.335339,0.337350,7.507594,1.701504,4.725122,4.047522,-8.361916,5.463467,8.862759,-7.415945,5.489567,7.844155,-7.597667,8.287719,-2.273442,-9.280950,-7.556738,1.388720,-0.563762,0.453201,-5.635388,-1.053981,-7.564496,-7.617285,3.684022,-0.052605,2.729398,-0.191652,-9.952430,8.697013,0.409397,-8.340246,5.684419,1.422516,-8.204816,6.713324,-3.894233,3.895815,-5.747003,-2.691079,-9.687893,-6.404173,-2.437374,6.901908,-9.543353,6.211245,7.213656,6.848924,-5.983625,-7.530308,0.987537,5.142270,5.826567,0.750188,-9.284477,-4.094275,-0.293483,7.129615,7.681687,9.323782,0.574955,-8.124778,-5.569186,-2.957975,-4.535703,6.588023,-3.151116,9.660840,-7.855326,7.986293,-1.205138,4.389144,-4.910961,-6.230357,-3.291375,2.668298,-8.752902,-6.144921,7.123317,0.433735,0.142618,-7.797653,-8.254722,6.719155,-8.415861,9.796567,-4.247590,6.432166,6.648145,0.875431,9.357292,-0.938796,-5.316485,-0.876335,6.931565,9.836027,-2.381976,-8.002955,-0.815460,7.286045,2.435432,9.984491,-9.744996,-8.479638,-1.709954,8.374142,7.342429,-3.414836,-6.974080,9.195922,-0.022375,-7.676688,-0.425930,6.660339,-2.854706,2.699138,-8.106696,-1.381621,3.775538,-1.266877,-5.724029,1.458210,0.317846,4.431559,-7.906571,2.484754,7.213993,-4.981358,6.214793,-2.709493,-0.760007,0.230601,5.327444,5.673154,-5.442915,-9.450846,7.897023,-0.281757,6.294800,-1.248756,7.303928,5.821303,0.932192,-4.888140,0.059382,8.282065,9.644757,-2.173674,-8.837973,5.589211,-3.687827,2.598024,-6.003811,-5.178318,4.869906,8.131071,3.506408,8.112053,-5.994178,7.246327,4.963880,-6.475803,7.619971,6.098238,-8.263367,-5.768970,-0.593998,4.896541,-2.608398,1.153562,-0.475588,-1.227629,7.119803,9.931825,3.321267,9.485052,3.443686,7.639413,0.957671,-7.819871,-6.651785,-1.894261,-4.067156,2.660494,4.884837,-1.745291,0.613158,8.233052,-1.648993,4.420203,0.304074,-2.316021,-5.576299,0.778282,-7.693738,9.237012,3.218453,-7.621261,5.658694,-4.444904,-9.666745,4.768024,4.048775,-4.921184,7.981119,1.847879,-1.809505,4.403749,-3.276440], dtype = "float32")#candidate|7736|(336,)|const|float32
call_7735 = relay.TupleGetItem(func_5576_call(relay.reshape(const_7736.astype('float32'), [336,]), relay.reshape(var_7694.astype('int32'), [2, 528]), relay.reshape(var_7694.astype('float64'), [2, 528]), ), 2)
call_7737 = relay.TupleGetItem(func_5581_call(relay.reshape(const_7736.astype('float32'), [336,]), relay.reshape(var_7694.astype('int32'), [2, 528]), relay.reshape(var_7694.astype('float64'), [2, 528]), ), 2)
uop_7739 = relay.asin(uop_7732.astype('float32')) # shape=(11, 15, 3)
uop_7741 = relay.asin(uop_7734.astype('float32')) # shape=(11, 15, 3)
output = relay.Tuple([call_7673,call_7689,var_7694,call_7719,call_7735,const_7736,uop_7739,])
output2 = relay.Tuple([call_7674,call_7690,var_7694,call_7720,call_7737,const_7736,uop_7741,])
func_7743 = relay.Function([var_7694,], output)
mod['func_7743'] = func_7743
mod = relay.transform.InferType()(mod)
var_7744 = relay.var("var_7744", dtype = "int32", shape = (1056,))#candidate|7744|(1056,)|var|int32
output = func_7743(var_7744)
func_7745 = relay.Function([var_7744], output)
mutated_mod['func_7745'] = func_7745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_7751 = func_1716_call()
call_7752 = func_1716_call()
output = relay.Tuple([call_7751,])
output2 = relay.Tuple([call_7752,])
func_7753 = relay.Function([], output)
mod['func_7753'] = func_7753
mod = relay.transform.InferType()(mod)
output = func_7753()
func_7754 = relay.Function([], output)
mutated_mod['func_7754'] = func_7754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3720_call = mod.get_global_var('func_3720')
func_3721_call = mutated_mod.get_global_var('func_3721')
call_7770 = func_3720_call()
call_7771 = func_3720_call()
var_7775 = relay.var("var_7775", dtype = "float64", shape = (20,))#candidate|7775|(20,)|var|float64
bop_7776 = relay.power(call_7770.astype('float64'), relay.reshape(var_7775.astype('float64'), relay.shape_of(call_7770))) # shape=(20,)
bop_7779 = relay.power(call_7771.astype('float64'), relay.reshape(var_7775.astype('float64'), relay.shape_of(call_7771))) # shape=(20,)
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_7786 = relay.TupleGetItem(func_3123_call(), 0)
call_7787 = relay.TupleGetItem(func_3124_call(), 0)
var_7789 = relay.var("var_7789", dtype = "float64", shape = (20,))#candidate|7789|(20,)|var|float64
bop_7790 = relay.multiply(var_7775.astype('uint64'), relay.reshape(var_7789.astype('uint64'), relay.shape_of(var_7775))) # shape=(20,)
output = relay.Tuple([bop_7776,call_7786,bop_7790,])
output2 = relay.Tuple([bop_7779,call_7787,bop_7790,])
func_7794 = relay.Function([var_7775,var_7789,], output)
mod['func_7794'] = func_7794
mod = relay.transform.InferType()(mod)
var_7795 = relay.var("var_7795", dtype = "float64", shape = (20,))#candidate|7795|(20,)|var|float64
var_7796 = relay.var("var_7796", dtype = "float64", shape = (20,))#candidate|7796|(20,)|var|float64
output = func_7794(var_7795,var_7796,)
func_7797 = relay.Function([var_7795,var_7796,], output)
mutated_mod['func_7797'] = func_7797
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7831 = relay.const([[[-4,-8,-2,-2,-10,-6,-2,-2,-4],[-7,7,5,10,1,6,5,-8,-10],[-3,1,7,-8,8,-10,-8,-7,8],[-5,6,8,-3,1,-7,2,-7,7],[2,-3,-7,5,9,-2,-6,5,-2],[3,7,9,-8,6,-5,9,10,10],[-6,-5,-8,2,-4,5,2,-3,5]],[[5,-2,7,7,7,-2,5,3,-3],[-6,5,5,-8,-2,-8,-5,-8,-5],[6,-5,-9,1,2,-5,3,3,-3],[-9,-7,-4,-8,9,5,3,6,-6],[4,3,1,5,1,-3,-4,9,-5],[-6,1,-9,9,-10,1,-4,-5,-2],[-6,10,5,-6,-6,-10,-8,-4,-2]],[[-7,-8,-10,5,7,-10,6,-6,-7],[-10,9,8,8,8,6,8,4,10],[-6,-5,-7,-2,5,9,-10,-5,-6],[-2,10,8,-1,9,2,-7,-6,-1],[-1,8,-2,8,-8,3,-7,-10,-5],[4,7,-1,-7,-9,-3,8,3,10],[2,7,10,-4,5,7,-4,-5,-8]],[[-10,-5,10,9,-3,-3,-8,-10,7],[-7,8,-6,-1,8,9,-4,-1,-8],[-8,8,-9,-2,-5,6,-4,-2,-6],[-9,-9,4,-5,9,-7,4,5,-5],[-2,-3,-1,1,-1,-10,-3,3,8],[-10,-6,-8,7,8,-5,-8,2,-5],[10,10,1,8,9,-4,1,-1,-6]],[[-1,2,-6,-2,3,6,7,-6,-7],[7,8,9,6,-7,-8,-5,-7,6],[-3,8,2,-3,-9,-6,-5,4,-2],[7,-4,4,-9,-8,-5,8,3,-3],[9,4,7,4,6,5,-2,3,-7],[7,5,10,2,-7,3,9,-7,10],[6,4,-4,9,9,4,-10,-2,6]],[[6,-10,-2,4,7,-8,-3,-2,6],[6,-4,9,3,-8,-6,-6,4,-5],[1,10,1,6,2,-3,-2,6,-5],[5,-6,-10,-9,5,4,-2,1,4],[9,8,-6,2,9,5,6,-2,2],[5,10,-7,-1,-9,8,-6,1,-2],[4,-6,-3,9,-10,-2,-4,-6,-6]],[[-9,9,-1,9,-7,1,9,3,-10],[-8,-8,1,3,-8,10,-3,10,6],[10,-9,8,-8,7,4,-10,10,1],[9,-9,-6,-10,9,-10,3,2,8],[-6,-9,-10,4,-5,9,6,-3,-4],[5,7,-5,-10,-8,-4,2,-3,-3],[-6,-2,-1,-9,10,3,1,9,3]],[[3,-6,-4,7,10,-9,-4,2,-5],[8,2,-6,-3,5,4,-8,9,-10],[-6,-1,9,-1,-6,-1,-8,7,-9],[4,-9,-6,5,2,9,9,6,-2],[-1,-10,-6,7,1,1,-6,-4,6],[-10,3,4,-1,-7,-2,-4,10,9],[-6,-9,10,-1,-6,1,-2,-2,-2]],[[-8,9,10,2,6,1,-7,2,5],[7,8,10,5,10,-8,-4,-5,-10],[8,-10,-6,-10,9,-1,1,2,-1],[-9,-6,-4,3,-3,-4,-5,6,7],[-8,7,6,-2,5,-6,-8,-3,-6],[-9,6,7,-6,2,-10,4,-5,-5],[-8,-8,3,-9,3,-5,8,7,-7]]], dtype = "int16")#candidate|7831|(9, 7, 9)|const|int16
var_7832 = relay.var("var_7832", dtype = "int16", shape = (9, 7, 9))#candidate|7832|(9, 7, 9)|var|int16
bop_7833 = relay.less(const_7831.astype('bool'), relay.reshape(var_7832.astype('bool'), relay.shape_of(const_7831))) # shape=(9, 7, 9)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
const_7841 = relay.const([[8.290780,2.164836,3.755657,2.311346,8.547866,-5.202818,0.366933,-5.189348,-1.724747,-9.194715,9.392811,-5.458519,-5.011198,3.480525,-3.970723,4.820339,9.115152,3.541710,5.747420,-3.138596,5.861330,-1.490386,1.588947,-2.265961,-5.009053,9.063141,2.514792,3.547764,9.603600,-7.862786,-0.557459,5.486416,-1.827964,6.692851,7.552091,-7.238442,-9.095358,5.021947,7.173314,2.539947,-2.875301,8.545329,-1.336490,3.183401,-6.976929,-2.654807,1.085774,-1.015744,-5.667642,-1.729750,9.532471,-7.844009,2.608451,-1.721483,-4.013239,-6.473142,-3.131767,-7.966147,-2.366683,-1.112719,3.643490,-8.059649,-8.001495,-4.361619,-5.692788,1.382299,0.102685,8.626030,2.858499,5.756710,5.552936,9.861355,3.402839,-7.082708,9.377460,-1.124296,0.412764,-3.535697,0.640051,2.962022,3.056726,-8.881533,-6.067722,2.531042,4.237237,9.315897,6.839023,-8.449664,-1.892378,-5.985459,0.254732,-2.896696,6.423476,-1.657186,2.961704,-2.380438,-7.366445,5.904347,-9.647922,4.493304,8.732394,-0.901422,0.545248,-6.567000,-9.555232,8.683998,5.557230,-4.218008,-6.285799,-0.788197,-9.403058,-5.240408,6.349984,-3.995549,9.299858,5.866102,-9.260836,2.513836,-9.453176,-5.240368,-8.852926,-2.370074,7.603528,2.207197,5.085499,-6.928701,-1.228975,3.298278,-6.770983,-7.091767,9.889138,9.462726,7.340505,9.637701,-6.406248,-5.450021,3.056802,-0.175951,-4.390236,0.029571,5.982446,2.947027,-0.514934,0.338479,-2.942445,-7.628608,4.483120,-9.396077,-4.418302,-4.100588,0.053804,-4.640933,8.528417,4.401288,-2.110904,-9.683983,-4.739243,6.989589,-1.685591,-9.755358,-3.805585,-4.578550,-9.975638,8.351214,-6.957042,9.765237,-6.151730,-7.110301,-3.911910,1.837298,-1.743250,4.669337,-2.282621,-7.660388,7.780651,1.062952,8.904562,-8.751835,-1.699335,6.955197,8.509865,-7.332224,-4.999069,-2.667106,6.739075,4.189161,9.628716,-1.982655,8.529689,-0.642133,3.294357,7.600725,8.840099,-7.464086,9.042483,-0.774189,-7.320494,-2.679843,8.365639,-6.044619,1.277119,8.231203,-6.270074,-9.011432,-2.856823,-7.932237,-1.430081,-6.309528,8.712251,-1.529476,-9.762074,-2.585490,5.880082,1.257047,4.318478,6.470229,8.393444,8.929446,4.272805,-5.092073,-1.407163,4.320450,-2.499607,-7.366320,3.316414,-1.970958,6.496328,-7.545727,9.292351,2.977080,8.847889,9.027056,8.845744,-8.172265,-9.723534,-6.284714,-4.073831,-7.376250,-8.606305,-2.219962,4.958194,7.881877,0.911285,9.911556,-8.621613,8.966745,-6.704679,-2.919511,1.286261,-7.136589,9.849204,-2.622720,-4.806347,-0.437329,6.110245,-0.495865,1.268961,9.653750,-1.971754,-9.749687,-1.293951,-1.795051,-9.925797,-3.782257,-1.505766,-1.097921,-5.065769,6.275733,3.280154,5.949966,-5.764773,8.484105,0.961181,5.120228,5.538312,-5.823270,9.156173,-4.056839,-8.110934,-3.839341,9.354460,-4.087928,4.649063,6.785302,-4.987703,-9.461003,-2.257102,-6.199903,-3.972027,0.233851,8.184219,4.797188,1.146775,8.992879,9.527272,-0.038987,-5.105876,-6.901491,-7.046195,-6.744942,-7.506759,0.237510,-3.240860,-3.031326,6.533189,-2.002760,-0.180792,-9.376371,-5.397533,5.987479,2.226166,-8.699515,-9.790622,1.758514,-1.235755,2.296667,-7.408433,-9.195199,6.432280,-1.615149,-6.864748,7.734657,-0.177165,-2.648380,8.342811,-2.856243,1.179639,-2.284817,0.679377,-2.673581,8.884263,-9.352654,1.927123,-8.085127,-9.161953,6.626609,-3.542349,4.643786,-6.918323,6.257788,7.795271,-3.139955,-5.421115,-5.047824,5.568082,-2.658607,3.512758,-2.486892,6.338751,8.088055,7.213184,-1.559932,1.004829,6.546353,-0.473200,-1.837033,-7.680263,-3.170526,8.658824,5.950579,-0.950489,-4.168355,-4.558456,-0.269940,6.970721,7.377383,-5.538583,-4.356367,2.031106,-2.235180,-3.799368,8.240009,4.999085,-1.264135,9.858402,5.821535,0.813345,1.356271,6.935598,6.456111,2.924352,3.189936,-0.717320,5.973755,5.486009,8.408975,-1.749405,1.154025,5.279367,9.012837,7.953405,-7.225995,-1.590433,-8.300178,9.502431,-6.318054,5.854530,-9.920100,-6.835843,8.865053,7.926658,9.505712,-2.734946,-8.316951,-6.783054,-2.090994,-4.344428,-7.835719,-1.410965,-3.496028,-2.045881,-2.909143,6.338547,-8.950826,-2.419879,9.628033,-6.400073,-7.094426,7.210010,-2.863945,-7.780776,1.255196,9.883394,0.511685,2.262948,6.173290,-6.969436,4.710350,8.958289,6.328109,3.909164,7.052539,-2.110644,-2.510434,-8.110252,0.364656,7.525350,-8.697376,9.827559,-5.853785,3.826316,-0.436434,5.318911,3.700290,0.297773,9.565556,-3.272782,5.125781,-1.525456,-5.205766,-6.051736,3.168404,1.013622,6.151387,4.659836,7.768884,4.730672,-7.085213,3.846157,6.406244,3.211986,3.992485,-9.741996,-9.747682,4.456955,2.186668,-8.916737,7.042725,-1.168931,-8.366491,4.482023,7.042870,-3.261851,7.421846,3.042615,-3.483390,1.866619,-4.639974,-3.586836,-5.467453,-8.345137,-9.742394,-7.711804,-6.924813,-1.258367,-5.041262,-4.368922,-6.956419,-5.195836,-2.248963,8.663311,-3.750726,-8.131464,-2.378135,9.561092,-4.403089,-8.766672,-0.600449,0.175097,-6.917259,-5.826700,4.936279,-3.710698,4.113153,9.194047,-8.520245,-5.294678,-9.234043,-1.288588,-5.147590,2.849166,7.107448,3.269684,5.967301,-6.718822,-5.902909,-7.521248,0.991888,2.661403,1.698321,-1.240778,2.755769,-6.280393,7.361593,-7.791533,-8.993723,1.495621,-5.935468,-4.364496,5.309051,5.439690,9.589470,0.467090,-1.284652,5.794602,9.657429,6.720736,-8.867922,-6.800312,-0.395672,9.053300,9.685808,-6.466810,5.191866,2.464588,3.065828,-2.695882,-3.297883,3.424663,2.296479,3.939256,-7.649473,9.450044,-3.831340,8.684652,9.677885,-8.538287,4.948973,-1.689714,3.604502,3.654042,-6.983332,0.881795,4.928616,5.994327,9.854544,6.658916,3.822316,-8.893490,6.273513,2.722998,2.056249,9.352124,-4.829647,3.275910,0.141478,4.133080,1.347024,-1.887668,5.174951,8.613076,-4.594269,1.693747,4.947500,-9.729409,0.931049,6.527533,0.622863,6.498864,-7.549693,6.950802,9.625879,1.166918,5.683524,8.670593,6.974202,2.268228,7.472600,-6.800518,-3.678540,2.427121,-3.977447,-0.301195,1.863988,1.483485,0.672045,8.186349,2.099208,0.612402,8.061934,-6.893583,3.256074,-4.669248,-9.753318,6.572799,3.851411,-5.720873,-0.033253,1.399973,-2.551330,5.182947,3.936757,-9.306204,-1.053039,9.108385,-9.081833,-6.437790,3.802207,-0.813983,9.463744,9.841401,7.797135,-5.200462,-5.219539,9.697906,1.343934,-9.354665,-2.274820,4.372078,-5.605967,-3.094613,-8.513465,-3.905257,1.149703,2.260681,3.136316,-5.983610,-4.457255,-9.611203,-9.795681,9.534041,-9.709126,5.428463,-3.729998,8.758816,9.675142,7.088894,6.474638,-2.496388,9.884207,7.519852,-2.200725,8.470898,2.004131,7.126803,1.394038,9.110387,4.089055,-2.853837,6.806134,-2.277274,3.076414,2.839985,-7.032925,-6.351253,7.432946,-0.741452,0.899662,9.677015,3.541900,-0.992759,6.422417,-6.618600,-8.914338,9.863190,9.173706,6.045479,0.792778,6.831667,-9.399238,2.988266,0.519913,3.550243,2.100364,9.312339,7.995727,-3.218093,0.515702,9.423258,1.725834,-0.280030,5.040406,-7.571846,-1.254223,-5.471593,0.502823,-7.378390,6.421717,6.307997,-1.448763,7.011912,-6.434241,6.176685,-2.249925,-6.978392,7.948897,-9.822748,-5.287777,7.175484,-3.344430,0.273999,-7.239476,0.187409,3.279214,-6.108884,1.349227,0.310704,3.388307,-8.757667,-1.966057,-6.348700,1.945370,-1.488725,9.458304,-4.495729,4.756685,7.794762,2.963749,3.178286,2.111929,9.416619,1.013917,-9.941929,4.941864,-5.727001,4.506960,5.433315,-6.566176,-5.309503,9.695622,5.926094,-8.620679,-8.018138,5.144587,-7.128080,-8.876168,-7.361824,8.548847,-1.987633,1.123708,-6.483499,2.582607,7.214171,5.847669,6.903656,-7.818532,2.840775,3.471057,-7.943320,1.431938,6.108506,-9.974907,0.327965,0.782682,-1.096876,-7.150417,0.416542,-6.392314,8.249860,0.184084,0.671776,-6.556065,-6.345335,-5.676036,-3.375250,-9.246821,6.401511,4.676250,-1.395580,8.874922,5.791968,0.685127,0.877187,6.013724,4.011537,-8.939657,-8.174784,9.831400,-0.520174,-9.884111,8.744016,2.814604,6.111320,9.505945,8.113031,3.744800,-0.307304,5.675948,-7.611770,6.664794]], dtype = "float64")#candidate|7841|(1, 810)|const|float64
call_7840 = relay.TupleGetItem(func_5092_call(relay.reshape(const_7841.astype('float64'), [6, 15, 9])), 1)
call_7842 = relay.TupleGetItem(func_5094_call(relay.reshape(const_7841.astype('float64'), [6, 15, 9])), 1)
output = relay.Tuple([bop_7833,call_7840,const_7841,])
output2 = relay.Tuple([bop_7833,call_7842,const_7841,])
func_7853 = relay.Function([var_7832,], output)
mod['func_7853'] = func_7853
mod = relay.transform.InferType()(mod)
mutated_mod['func_7853'] = func_7853
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7854 = relay.var("var_7854", dtype = "int16", shape = (9, 7, 9))#candidate|7854|(9, 7, 9)|var|int16
func_7853_call = mutated_mod.get_global_var('func_7853')
call_7855 = func_7853_call(var_7854)
output = call_7855
func_7856 = relay.Function([var_7854], output)
mutated_mod['func_7856'] = func_7856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4863_call = mod.get_global_var('func_4863')
func_4865_call = mutated_mod.get_global_var('func_4865')
call_7929 = relay.TupleGetItem(func_4863_call(), 5)
call_7930 = relay.TupleGetItem(func_4865_call(), 5)
output = relay.Tuple([call_7929,])
output2 = relay.Tuple([call_7930,])
func_7942 = relay.Function([], output)
mod['func_7942'] = func_7942
mod = relay.transform.InferType()(mod)
output = func_7942()
func_7943 = relay.Function([], output)
mutated_mod['func_7943'] = func_7943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6937_call = mod.get_global_var('func_6937')
func_6938_call = mutated_mod.get_global_var('func_6938')
call_7944 = relay.TupleGetItem(func_6937_call(), 1)
call_7945 = relay.TupleGetItem(func_6938_call(), 1)
output = call_7944
output2 = call_7945
func_7950 = relay.Function([], output)
mod['func_7950'] = func_7950
mod = relay.transform.InferType()(mod)
output = func_7950()
func_7951 = relay.Function([], output)
mutated_mod['func_7951'] = func_7951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2546_call = mod.get_global_var('func_2546')
func_2547_call = mutated_mod.get_global_var('func_2547')
call_7971 = func_2546_call()
call_7972 = func_2546_call()
func_6097_call = mod.get_global_var('func_6097')
func_6099_call = mutated_mod.get_global_var('func_6099')
call_8010 = relay.TupleGetItem(func_6097_call(), 1)
call_8011 = relay.TupleGetItem(func_6099_call(), 1)
output = relay.Tuple([call_7971,call_8010,])
output2 = relay.Tuple([call_7972,call_8011,])
func_8018 = relay.Function([], output)
mod['func_8018'] = func_8018
mod = relay.transform.InferType()(mod)
mutated_mod['func_8018'] = func_8018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8018_call = mutated_mod.get_global_var('func_8018')
call_8019 = func_8018_call()
output = call_8019
func_8020 = relay.Function([], output)
mutated_mod['func_8020'] = func_8020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3919_call = mod.get_global_var('func_3919')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_8034 = relay.TupleGetItem(func_3919_call(), 0)
call_8035 = relay.TupleGetItem(func_3920_call(), 0)
func_6907_call = mod.get_global_var('func_6907')
func_6909_call = mutated_mod.get_global_var('func_6909')
var_8037 = relay.var("var_8037", dtype = "float64", shape = (616,))#candidate|8037|(616,)|var|float64
call_8036 = relay.TupleGetItem(func_6907_call(relay.reshape(var_8037.astype('float64'), [616,])), 1)
call_8038 = relay.TupleGetItem(func_6909_call(relay.reshape(var_8037.astype('float64'), [616,])), 1)
func_7753_call = mod.get_global_var('func_7753')
func_7754_call = mutated_mod.get_global_var('func_7754')
call_8039 = relay.TupleGetItem(func_7753_call(), 0)
call_8040 = relay.TupleGetItem(func_7754_call(), 0)
output = relay.Tuple([call_8034,call_8036,var_8037,call_8039,])
output2 = relay.Tuple([call_8035,call_8038,var_8037,call_8040,])
func_8047 = relay.Function([var_8037,], output)
mod['func_8047'] = func_8047
mod = relay.transform.InferType()(mod)
var_8048 = relay.var("var_8048", dtype = "float64", shape = (616,))#candidate|8048|(616,)|var|float64
output = func_8047(var_8048)
func_8049 = relay.Function([var_8048], output)
mutated_mod['func_8049'] = func_8049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6679_call = mod.get_global_var('func_6679')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_8073 = relay.TupleGetItem(func_6679_call(), 1)
call_8074 = relay.TupleGetItem(func_6680_call(), 1)
output = call_8073
output2 = call_8074
func_8076 = relay.Function([], output)
mod['func_8076'] = func_8076
mod = relay.transform.InferType()(mod)
output = func_8076()
func_8077 = relay.Function([], output)
mutated_mod['func_8077'] = func_8077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_8078 = relay.TupleGetItem(func_1817_call(), 0)
call_8079 = relay.TupleGetItem(func_1818_call(), 0)
output = relay.Tuple([call_8078,])
output2 = relay.Tuple([call_8079,])
func_8093 = relay.Function([], output)
mod['func_8093'] = func_8093
mod = relay.transform.InferType()(mod)
output = func_8093()
func_8094 = relay.Function([], output)
mutated_mod['func_8094'] = func_8094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4619_call = mod.get_global_var('func_4619')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_8100 = func_4619_call()
call_8101 = func_4619_call()
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_8102 = relay.TupleGetItem(func_3123_call(), 2)
call_8103 = relay.TupleGetItem(func_3124_call(), 2)
const_8116 = relay.const([[[-8.164737,-6.669111,9.633407,-3.884297,-4.246515,2.012858,2.659811,-5.646519,-7.487387],[1.383810,2.829595,8.781605,6.838892,-4.268359,-5.246208,-4.099711,0.461990,4.245480],[8.116897,-5.632029,-5.845723,2.610872,-0.878516,-4.349423,-0.060200,1.532349,4.131454],[-5.828118,8.623329,7.252945,-5.752495,-4.709532,-7.966904,-7.937533,9.523184,3.237750],[-4.942935,1.747224,6.490207,-5.556443,7.159145,7.734977,-7.287135,-4.702252,-5.912183],[4.337227,6.694618,-0.720432,1.683939,0.722520,3.945417,-1.437541,-5.523524,-9.270203],[4.414627,0.431358,-6.928482,-1.147674,-6.722985,-6.086307,-1.113306,1.024527,8.357008],[-8.254501,-9.507755,1.414590,-3.993419,-5.383520,-1.058103,-4.005799,2.840863,-9.370267],[-4.917860,-1.266097,2.470449,8.615809,-7.341427,-5.739284,-2.416166,-2.184886,-3.301762],[6.370017,8.661886,7.583953,-0.520878,5.683615,6.457286,-9.180845,-4.467521,-3.327435],[0.900463,-7.353729,-9.392573,-5.179612,6.132350,-0.124956,-7.084681,-9.507520,4.891568],[6.115382,-9.064125,8.145348,2.428817,3.976409,-3.008105,0.594789,-2.877224,8.334471],[-8.707367,2.315655,-6.748951,-2.267504,0.868159,-6.383903,-6.404436,0.400753,-8.272447],[0.751663,-1.477920,-2.048713,-7.059521,-1.671890,9.943083,-0.409176,9.131334,6.654313],[1.971212,3.403950,-1.788750,2.499175,7.419287,9.150802,0.925068,3.764213,-0.017492]],[[-8.240171,-7.981796,3.668668,-4.345216,2.822361,9.640712,8.351765,-5.228125,-7.629596],[-3.124529,-8.088894,-4.159506,2.731776,-5.260228,1.189606,-5.041896,3.310058,-8.918586],[-3.349047,-2.193470,5.053774,-2.279274,-0.220542,1.179020,-9.958850,-7.068886,2.209712],[-9.142198,-6.899147,-0.749296,3.394176,0.359558,5.196831,2.608282,-2.681676,2.854828],[-6.293333,-8.769815,5.344206,7.257240,8.636018,-3.904921,-8.737514,-8.983106,1.882475],[-5.347459,2.441865,8.490516,6.231322,3.735165,2.885543,5.502656,-6.713273,-4.443672],[9.675709,8.831092,-2.705535,-3.424189,6.872049,7.660971,2.593711,6.873327,-8.937699],[9.551020,-0.432434,6.162639,6.736851,4.965657,2.248339,2.636428,9.185344,3.737611],[-5.608923,-5.795899,-0.186680,-3.168884,5.680915,4.523204,0.884259,8.156775,3.672147],[9.468683,-0.819721,-2.055174,-0.675929,-5.060394,2.591874,7.243758,2.716870,0.290411],[-8.753241,0.963466,5.865620,6.001196,3.028740,-8.226678,4.035273,-8.074536,-2.345401],[0.305086,-1.742483,-4.468073,-9.443187,-6.211056,1.943612,8.865110,6.361587,5.767404],[6.430055,8.501319,-4.975041,3.383462,4.877160,4.329706,2.772372,7.317458,-8.687164],[0.942823,5.514656,6.151563,7.915249,-5.093585,7.414955,8.809478,-8.102790,-2.034555],[4.692036,7.619075,1.658165,-5.803294,0.004910,-6.500875,-0.373644,-9.767726,1.572321]],[[-8.562319,5.698977,-2.173634,6.069118,2.954504,-7.313686,-4.519610,-1.583187,6.683134],[-1.917846,-4.865130,0.536051,1.291482,-6.994111,0.181705,1.694295,-7.553568,4.374435],[-5.801280,-6.061777,-7.270156,3.204958,-9.963800,-6.579419,1.904154,-0.271210,7.441093],[-7.381259,7.876058,-7.882999,3.514358,-4.047387,-4.302732,-2.773443,-1.142248,4.465966],[6.394285,7.573411,-4.797621,4.170572,-1.746793,8.233456,4.852958,8.178111,-4.118001],[-9.540025,9.345434,1.288393,-5.821619,-3.621237,-8.923656,0.765579,-6.119099,-6.722549],[5.889371,-1.911185,5.431100,9.790561,-6.363706,1.133369,-7.089180,-1.650318,-9.090184],[-5.406551,9.470955,-9.198403,-8.588156,8.181961,-5.679483,2.842311,-6.921515,-3.097562],[5.862283,-5.238989,-5.114796,-4.245643,8.514243,-4.045178,-8.026806,-9.708780,-3.414559],[4.462513,1.497454,2.512746,-6.848020,0.774642,1.719030,-6.596420,0.488922,-5.152878],[-2.006416,-9.144958,4.721270,-3.141782,9.764776,3.322836,0.619428,-6.645176,5.648188],[-5.057220,-3.077735,-3.825632,3.304171,-6.940178,-8.354749,-8.772870,5.591179,-5.554949],[-7.437733,-4.949373,-5.542930,1.612721,4.613543,-0.913185,8.114917,-3.142912,-3.218212],[5.838694,-1.234706,-1.884304,-3.444902,7.249983,7.012732,-6.172738,-0.958112,-1.200487],[-0.899151,-9.614827,8.630001,2.867216,-1.304820,6.303591,-6.767341,-2.371497,-0.154182]],[[2.283595,-7.540755,9.486767,3.616215,0.989349,-7.281837,-8.001852,2.196062,-0.813028],[2.759104,4.939744,-1.768085,-5.145628,-7.909228,0.592398,5.836991,2.903101,1.191074],[2.915566,0.818508,3.013492,-9.033887,-3.921199,-0.042194,1.017696,-2.743690,9.929727],[9.055518,-6.898828,6.320698,-6.537468,-5.717333,-7.658363,-7.362802,-2.648285,-9.700716],[-6.573864,6.646787,-6.710312,6.256908,3.435333,-4.048096,-0.125052,-7.798468,3.865834],[-7.612075,-8.024877,-2.077800,6.084569,3.158634,-9.520511,8.438427,-3.468833,0.197891],[-8.860929,-5.366097,6.968512,8.968146,-2.569592,-8.263884,3.638709,-6.024513,5.989943],[-8.896479,6.628377,6.988689,4.710964,-5.585354,5.573435,-4.961802,3.172797,-7.119773],[2.732353,-7.349822,1.669275,-0.717788,-1.403520,4.386649,3.630139,-7.338691,1.947676],[-3.289749,-5.423659,-7.032110,-3.416378,8.441993,-0.101289,-4.237814,4.759927,1.358653],[0.808472,5.774072,-0.919532,-4.905864,-0.651243,3.321382,-4.187389,-2.053112,-0.529725],[-1.627264,7.637236,-5.620545,4.177263,-2.633065,-7.839658,-2.892436,5.752134,1.799423],[-6.352527,1.180655,-8.571504,-2.814074,-9.155038,8.867760,3.107720,2.565242,7.997473],[-6.557749,6.381414,-3.678395,1.328860,8.434037,-3.445108,-7.858671,-9.664360,-9.935837],[-2.175528,7.630551,2.986638,-5.534788,0.669225,-6.733836,7.916341,2.063030,9.753567]],[[-2.015015,-0.070674,6.004594,-2.284532,0.328777,4.361521,2.555361,-2.423113,-1.010686],[9.639399,1.421602,-6.108815,-7.056921,-5.026427,-6.291403,8.534052,-0.745178,5.959181],[-5.953768,-2.727938,-1.320084,4.574135,4.566108,6.001132,-9.205757,-6.533125,2.758600],[0.360606,9.544763,4.863156,0.694735,-1.263340,1.583048,5.869000,-3.245567,6.900036],[8.065079,-7.383693,9.941045,-1.310339,5.110383,3.593157,6.287023,-2.275446,-2.492357],[3.194264,-2.111431,-5.634104,6.315379,5.822519,7.119414,-2.088078,-8.184577,3.626088],[-2.228702,0.702404,1.020977,-0.729819,2.468317,7.450459,7.627368,3.541261,-7.431283],[1.047402,0.728611,7.582876,9.733920,2.073225,9.357861,4.586401,-0.689393,3.758954],[3.127160,-5.464426,-8.703777,9.741991,-0.576836,4.103915,-6.961926,-3.852411,5.010487],[-7.344575,-4.716373,-2.015560,-3.375027,7.896017,-6.143187,-9.707972,6.640872,-3.456358],[-3.811010,0.217745,-5.926965,-3.792678,3.037432,-4.585476,-8.044841,7.433480,-1.150648],[-0.263036,-6.461530,5.076346,-4.475237,-2.498387,0.159401,9.499815,-7.350433,-1.423316],[4.633164,5.407252,-1.218350,-9.258514,-1.250593,2.489250,4.095650,-8.993216,4.603953],[3.414001,4.477011,5.848214,-0.026683,8.431756,2.729503,-8.323963,-6.298840,9.663884],[1.075268,3.248665,-7.191303,6.878781,2.663887,4.127802,6.782214,-3.508177,-8.434370]],[[7.323909,9.663667,-1.395194,1.231034,9.719343,-9.687676,-1.101783,-2.862612,-2.001462],[-8.461513,3.955435,0.587880,-0.442892,1.444638,0.114731,3.706709,-0.791659,1.953709],[2.306390,9.188120,-2.657486,-1.636312,-5.122671,4.170399,8.053670,-7.976157,6.379010],[1.859785,-3.340975,-9.241670,-7.711152,9.893164,-7.372222,7.236299,4.375881,3.922591],[8.867941,-4.957662,-4.708031,-2.216824,3.100716,-8.669812,-5.756315,-2.742872,-8.131990],[-0.651205,-3.987304,-9.823522,4.040240,0.319511,-0.027615,-3.549127,-1.169725,3.680327],[-3.104062,-9.846139,-0.253993,-8.633388,-9.459781,-0.476895,-3.323897,2.497161,-8.756271],[0.353922,-3.621100,-3.184756,9.578440,-3.832838,9.623873,9.163422,8.221850,1.782250],[-6.324712,-4.385315,-1.035167,-4.079447,1.568699,-8.277958,5.624840,3.664978,-0.370576],[-3.656654,4.409639,8.344702,5.029421,-9.121466,-5.924228,-8.214675,-7.276024,4.990647],[2.181006,3.718889,7.690943,-7.756889,0.559205,-0.073945,0.628985,-2.158241,6.080398],[8.150916,-4.658201,3.210494,2.170277,4.722100,-4.458561,2.077668,-1.200299,1.171501],[-0.549707,-5.740815,1.588645,3.582613,-2.721333,7.201437,5.086110,-9.692591,1.079209],[-7.759486,9.521005,-9.463000,-3.346449,-0.872835,-3.409396,-8.835142,8.839790,-3.349122],[-1.165442,-7.274093,2.407283,-4.399564,-1.670097,-0.744136,3.674458,4.322845,7.738415]]], dtype = "float64")#candidate|8116|(6, 15, 9)|const|float64
bop_8117 = relay.not_equal(call_8100.astype('bool'), relay.reshape(const_8116.astype('bool'), relay.shape_of(call_8100))) # shape=(6, 15, 9)
bop_8120 = relay.not_equal(call_8101.astype('bool'), relay.reshape(const_8116.astype('bool'), relay.shape_of(call_8101))) # shape=(6, 15, 9)
func_4619_call = mod.get_global_var('func_4619')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_8129 = func_4619_call()
call_8130 = func_4619_call()
func_4682_call = mod.get_global_var('func_4682')
func_4684_call = mutated_mod.get_global_var('func_4684')
call_8150 = func_4682_call()
call_8151 = func_4682_call()
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
var_8155 = relay.var("var_8155", dtype = "float64", shape = (192,))#candidate|8155|(192,)|var|float64
call_8154 = relay.TupleGetItem(func_2204_call(relay.reshape(var_8155.astype('float64'), [1, 16, 12])), 1)
call_8156 = relay.TupleGetItem(func_2206_call(relay.reshape(var_8155.astype('float64'), [1, 16, 12])), 1)
func_6716_call = mod.get_global_var('func_6716')
func_6721_call = mutated_mod.get_global_var('func_6721')
var_8160 = relay.var("var_8160", dtype = "uint8", shape = (240,))#candidate|8160|(240,)|var|uint8
const_8161 = relay.const([9.982035,-3.520344,9.907086,-1.158957,3.797254,4.826872,8.336669,-4.503887,6.510483,-7.300641,2.367538,2.646267,-2.773306,4.362075,-1.572821,2.050777,3.113888,3.030101,6.060058,5.665129,-3.579000,-4.821785,-0.752323,3.935780,1.061026,-4.916174,-5.344541,-9.847404,5.881428,-9.294289,6.777406,-0.864939,8.292280,5.925014,1.609624,8.490928,-8.965319,0.624262,-8.784221,-3.251861,1.672900,1.595813,-9.604711,-5.396851,0.927252,-1.504628,0.941632,3.555614,-0.700688,4.992066,-2.373882,5.147859,1.130846,0.071752,7.986617,0.168746,-3.609132,-6.442548,-5.098911,-8.921208,6.341311,-6.301671,2.701215,8.893896,2.129013,7.220026,-0.697927,-0.831644,-8.938654,5.763439,0.243559,-6.742214,3.008028,-8.346407,0.587690,-7.442000,7.378301,5.083553,-4.654479,-0.877831,-0.076163,0.922918,9.160809,-3.451933,7.722662,7.734719,-0.867895,-6.344169,1.086885,9.927389,-2.016791,3.335578,8.803463,-2.627652,-8.366104,9.662949,3.711600,5.553805,-2.408366,-6.875922,0.729460,-9.878692,5.218494,-5.054833,7.285092,7.083372,6.429104,-0.010126,-6.497960,-5.381951,7.334165,9.942856,2.595077,7.055711,-1.557396,7.616692,-7.539442,7.456041,4.218659,-0.383418,4.545529,-3.927649,-4.246205,0.962414,8.598017,1.564218,5.298822,3.877850,7.045016,-7.521251,-3.995157,-9.317672], dtype = "float32")#candidate|8161|(132,)|const|float32
call_8159 = relay.TupleGetItem(func_6716_call(relay.reshape(call_8102.astype('uint8'), [1, 5, 4]), relay.reshape(var_8160.astype('uint8'), [12, 5, 4]), relay.reshape(const_8161.astype('float32'), [132,]), ), 2)
call_8162 = relay.TupleGetItem(func_6721_call(relay.reshape(call_8102.astype('uint8'), [1, 5, 4]), relay.reshape(var_8160.astype('uint8'), [12, 5, 4]), relay.reshape(const_8161.astype('float32'), [132,]), ), 2)
uop_8167 = relay.acosh(call_8154.astype('float32')) # shape=(1, 16, 12)
uop_8169 = relay.acosh(call_8156.astype('float32')) # shape=(1, 16, 12)
output = relay.Tuple([call_8102,bop_8117,call_8129,call_8150,var_8155,call_8159,var_8160,const_8161,uop_8167,])
output2 = relay.Tuple([call_8103,bop_8120,call_8130,call_8151,var_8155,call_8162,var_8160,const_8161,uop_8169,])
func_8192 = relay.Function([var_8155,var_8160,], output)
mod['func_8192'] = func_8192
mod = relay.transform.InferType()(mod)
var_8193 = relay.var("var_8193", dtype = "float64", shape = (192,))#candidate|8193|(192,)|var|float64
var_8194 = relay.var("var_8194", dtype = "uint8", shape = (240,))#candidate|8194|(240,)|var|uint8
output = func_8192(var_8193,var_8194,)
func_8195 = relay.Function([var_8193,var_8194,], output)
mutated_mod['func_8195'] = func_8195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8076_call = mod.get_global_var('func_8076')
func_8077_call = mutated_mod.get_global_var('func_8077')
call_8253 = func_8076_call()
call_8254 = func_8076_call()
output = relay.Tuple([call_8253,])
output2 = relay.Tuple([call_8254,])
func_8277 = relay.Function([], output)
mod['func_8277'] = func_8277
mod = relay.transform.InferType()(mod)
output = func_8277()
func_8278 = relay.Function([], output)
mutated_mod['func_8278'] = func_8278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7950_call = mod.get_global_var('func_7950')
func_7951_call = mutated_mod.get_global_var('func_7951')
call_8292 = func_7950_call()
call_8293 = func_7950_call()
output = call_8292
output2 = call_8293
func_8338 = relay.Function([], output)
mod['func_8338'] = func_8338
mod = relay.transform.InferType()(mod)
output = func_8338()
func_8339 = relay.Function([], output)
mutated_mod['func_8339'] = func_8339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4682_call = mod.get_global_var('func_4682')
func_4684_call = mutated_mod.get_global_var('func_4684')
call_8351 = func_4682_call()
call_8352 = func_4682_call()
func_2288_call = mod.get_global_var('func_2288')
func_2290_call = mutated_mod.get_global_var('func_2290')
var_8362 = relay.var("var_8362", dtype = "int8", shape = (56,))#candidate|8362|(56,)|var|int8
call_8361 = relay.TupleGetItem(func_2288_call(relay.reshape(var_8362.astype('int8'), [56,])), 1)
call_8363 = relay.TupleGetItem(func_2290_call(relay.reshape(var_8362.astype('int8'), [56,])), 1)
output = relay.Tuple([call_8351,call_8361,var_8362,])
output2 = relay.Tuple([call_8352,call_8363,var_8362,])
func_8365 = relay.Function([var_8362,], output)
mod['func_8365'] = func_8365
mod = relay.transform.InferType()(mod)
var_8366 = relay.var("var_8366", dtype = "int8", shape = (56,))#candidate|8366|(56,)|var|int8
output = func_8365(var_8366)
func_8367 = relay.Function([var_8366], output)
mutated_mod['func_8367'] = func_8367
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8391 = relay.var("var_8391", dtype = "int8", shape = (2, 10, 10))#candidate|8391|(2, 10, 10)|var|int8
var_8392 = relay.var("var_8392", dtype = "int8", shape = (2, 10, 10))#candidate|8392|(2, 10, 10)|var|int8
bop_8393 = relay.add(var_8391.astype('int8'), relay.reshape(var_8392.astype('int8'), relay.shape_of(var_8391))) # shape=(2, 10, 10)
output = bop_8393
output2 = bop_8393
func_8401 = relay.Function([var_8391,var_8392,], output)
mod['func_8401'] = func_8401
mod = relay.transform.InferType()(mod)
var_8402 = relay.var("var_8402", dtype = "int8", shape = (2, 10, 10))#candidate|8402|(2, 10, 10)|var|int8
var_8403 = relay.var("var_8403", dtype = "int8", shape = (2, 10, 10))#candidate|8403|(2, 10, 10)|var|int8
output = func_8401(var_8402,var_8403,)
func_8404 = relay.Function([var_8402,var_8403,], output)
mutated_mod['func_8404'] = func_8404
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8413 = relay.const([[[7.457990,2.772169,3.317109,3.471084,-7.406589,-6.840226,-8.166896,-0.156698,-5.148300],[-9.059783,3.400795,-4.104717,9.133280,4.590001,-3.707900,-6.408895,-7.962240,-4.368095],[-1.818264,-4.246788,-1.010635,-5.233199,-5.801060,-6.403278,3.333061,-7.071940,9.574298],[9.945085,-4.310058,1.309557,4.437448,-8.300228,6.285907,-1.616273,-9.418751,-3.102452],[1.954516,0.634496,8.726684,-1.572507,-8.235523,3.087151,-8.873550,-3.755321,-2.167275],[4.701448,9.982571,5.644467,-5.239114,1.948568,-6.961116,-0.565301,-2.930769,-6.630724],[3.001795,-7.019271,1.633011,2.771057,-7.676029,-9.422983,4.503828,8.242919,8.155147],[5.955419,-6.796857,-1.166679,-5.625014,-9.974372,-2.092669,-6.562664,4.438689,3.830127],[5.146444,-3.481738,-3.449028,-8.372946,-8.865392,5.618676,-5.214617,-2.572996,8.349045],[6.640981,8.520100,-2.469474,-3.470962,9.787401,-1.320106,-7.497957,5.721658,5.201310],[1.096131,9.319878,4.960528,7.573580,1.869843,-7.417465,-2.220775,-5.866135,4.502572]],[[6.342590,9.386077,-8.565684,6.144136,6.725356,3.099626,1.470468,-9.615505,7.919666],[8.648551,3.745534,-6.787448,7.366756,-7.253617,-6.778556,-1.660368,8.414711,-6.720400],[1.462518,6.931688,-5.256859,-0.788651,1.341909,-9.336323,-1.004096,-7.363351,-0.832325],[-9.129636,2.006024,5.694936,-9.509585,-1.653051,6.480889,1.992830,-7.635087,-5.448429],[-3.100499,-7.167404,1.361048,-3.530359,-2.732570,-5.843557,2.758631,-3.614971,7.922592],[-9.863346,-0.421387,0.269639,2.170257,-9.937648,9.010680,-2.791949,7.526540,-9.958463],[5.273213,3.966363,0.522482,-0.475386,-5.218177,7.454736,-4.097140,3.237519,-7.777173],[-5.104182,-7.156296,-4.651026,0.073730,9.967445,9.260910,-0.794102,-3.025248,4.832698],[5.630498,-2.934141,-9.265642,6.678223,3.263844,6.995274,2.876105,2.438069,2.976532],[-4.364116,-5.237956,2.900566,3.565998,-3.345405,7.700418,4.527222,9.896113,-5.383453],[3.910635,-5.271677,4.685229,8.054113,6.091049,-2.445833,-6.544505,-4.495874,-0.024033]],[[-4.389994,3.325029,1.453600,-6.761945,0.764299,-3.289992,-2.283155,7.018806,-4.885116],[-4.249442,2.497676,-7.706073,-6.792483,-3.796099,0.121471,0.062684,-5.553728,-2.688962],[0.154969,-5.298374,-2.283990,3.245586,3.000648,2.318356,9.128700,2.679167,1.128368],[-4.601101,-6.710066,-4.829495,9.669521,6.746261,-2.775030,6.022067,6.630740,-4.422081],[-8.458337,-4.853300,-3.067181,9.647409,2.520289,9.477743,-3.059207,5.919365,-6.621188],[-4.555153,2.714452,-3.856481,4.208330,3.137265,3.586158,-3.884595,7.944770,0.736470],[-9.521655,5.114375,9.339488,-0.308775,-6.777672,-4.949705,-2.818234,-1.144620,2.168112],[3.470196,-1.892966,6.323725,9.461618,8.772857,-6.360326,-1.110522,1.762014,-1.489622],[-9.419232,-3.687510,-5.945825,-9.289345,8.034917,-3.271959,8.012447,6.784875,7.696179],[9.556932,-6.188127,6.305115,-7.592354,0.759029,-0.119054,-4.356779,6.201311,2.238310],[-9.304785,-1.310892,4.230850,-9.572160,-8.834414,-9.473434,-9.357535,-6.129114,3.347556]]], dtype = "float32")#candidate|8413|(3, 11, 9)|const|float32
uop_8414 = relay.cosh(const_8413.astype('float32')) # shape=(3, 11, 9)
bop_8421 = relay.logical_and(const_8413.astype('bool'), relay.reshape(uop_8414.astype('bool'), relay.shape_of(const_8413))) # shape=(3, 11, 9)
output = relay.Tuple([bop_8421,])
output2 = relay.Tuple([bop_8421,])
func_8444 = relay.Function([], output)
mod['func_8444'] = func_8444
mod = relay.transform.InferType()(mod)
output = func_8444()
func_8445 = relay.Function([], output)
mutated_mod['func_8445'] = func_8445
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8464 = relay.var("var_8464", dtype = "float32", shape = (3, 7, 11))#candidate|8464|(3, 7, 11)|var|float32
uop_8465 = relay.cosh(var_8464.astype('float32')) # shape=(3, 7, 11)
func_7539_call = mod.get_global_var('func_7539')
func_7540_call = mutated_mod.get_global_var('func_7540')
call_8476 = relay.TupleGetItem(func_7539_call(), 0)
call_8477 = relay.TupleGetItem(func_7540_call(), 0)
output = relay.Tuple([uop_8465,call_8476,])
output2 = relay.Tuple([uop_8465,call_8477,])
func_8492 = relay.Function([var_8464,], output)
mod['func_8492'] = func_8492
mod = relay.transform.InferType()(mod)
mutated_mod['func_8492'] = func_8492
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8493 = relay.var("var_8493", dtype = "float32", shape = (3, 7, 11))#candidate|8493|(3, 7, 11)|var|float32
func_8492_call = mutated_mod.get_global_var('func_8492')
call_8494 = func_8492_call(var_8493)
output = call_8494
func_8495 = relay.Function([var_8493], output)
mutated_mod['func_8495'] = func_8495
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8512 = relay.var("var_8512", dtype = "bool", shape = (4, 12, 6))#candidate|8512|(4, 12, 6)|var|bool
var_8513 = relay.var("var_8513", dtype = "bool", shape = (4, 12, 6))#candidate|8513|(4, 12, 6)|var|bool
bop_8514 = relay.logical_or(var_8512.astype('bool'), relay.reshape(var_8513.astype('bool'), relay.shape_of(var_8512))) # shape=(4, 12, 6)
output = bop_8514
output2 = bop_8514
func_8532 = relay.Function([var_8512,var_8513,], output)
mod['func_8532'] = func_8532
mod = relay.transform.InferType()(mod)
var_8533 = relay.var("var_8533", dtype = "bool", shape = (4, 12, 6))#candidate|8533|(4, 12, 6)|var|bool
var_8534 = relay.var("var_8534", dtype = "bool", shape = (4, 12, 6))#candidate|8534|(4, 12, 6)|var|bool
output = func_8532(var_8533,var_8534,)
func_8535 = relay.Function([var_8533,var_8534,], output)
mutated_mod['func_8535'] = func_8535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5014_call = mod.get_global_var('func_5014')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_8619 = relay.TupleGetItem(func_5014_call(), 0)
call_8620 = relay.TupleGetItem(func_5015_call(), 0)
output = relay.Tuple([call_8619,])
output2 = relay.Tuple([call_8620,])
func_8624 = relay.Function([], output)
mod['func_8624'] = func_8624
mod = relay.transform.InferType()(mod)
mutated_mod['func_8624'] = func_8624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8624_call = mutated_mod.get_global_var('func_8624')
call_8625 = func_8624_call()
output = call_8625
func_8626 = relay.Function([], output)
mutated_mod['func_8626'] = func_8626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7147_call = mod.get_global_var('func_7147')
func_7149_call = mutated_mod.get_global_var('func_7149')
call_8672 = func_7147_call()
call_8673 = func_7147_call()
output = call_8672
output2 = call_8673
func_8682 = relay.Function([], output)
mod['func_8682'] = func_8682
mod = relay.transform.InferType()(mod)
mutated_mod['func_8682'] = func_8682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8682_call = mutated_mod.get_global_var('func_8682')
call_8683 = func_8682_call()
output = call_8683
func_8684 = relay.Function([], output)
mutated_mod['func_8684'] = func_8684
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8697 = relay.var("var_8697", dtype = "int16", shape = (15, 1, 6))#candidate|8697|(15, 1, 6)|var|int16
var_8698 = relay.var("var_8698", dtype = "int16", shape = (15, 2, 6))#candidate|8698|(15, 2, 6)|var|int16
bop_8699 = relay.less(var_8697.astype('bool'), var_8698.astype('bool')) # shape=(15, 2, 6)
output = relay.Tuple([bop_8699,])
output2 = relay.Tuple([bop_8699,])
func_8704 = relay.Function([var_8697,var_8698,], output)
mod['func_8704'] = func_8704
mod = relay.transform.InferType()(mod)
var_8705 = relay.var("var_8705", dtype = "int16", shape = (15, 1, 6))#candidate|8705|(15, 1, 6)|var|int16
var_8706 = relay.var("var_8706", dtype = "int16", shape = (15, 2, 6))#candidate|8706|(15, 2, 6)|var|int16
output = func_8704(var_8705,var_8706,)
func_8707 = relay.Function([var_8705,var_8706,], output)
mutated_mod['func_8707'] = func_8707
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8737 = relay.var("var_8737", dtype = "float32", shape = (16, 4, 15))#candidate|8737|(16, 4, 15)|var|float32
var_8738 = relay.var("var_8738", dtype = "float32", shape = (16, 4, 15))#candidate|8738|(16, 4, 15)|var|float32
bop_8739 = relay.power(var_8737.astype('float32'), relay.reshape(var_8738.astype('float32'), relay.shape_of(var_8737))) # shape=(16, 4, 15)
func_283_call = mod.get_global_var('func_283')
func_285_call = mutated_mod.get_global_var('func_285')
var_8747 = relay.var("var_8747", dtype = "float32", shape = (132,))#candidate|8747|(132,)|var|float32
call_8746 = relay.TupleGetItem(func_283_call(relay.reshape(var_8747.astype('float32'), [4, 11, 3])), 6)
call_8748 = relay.TupleGetItem(func_285_call(relay.reshape(var_8747.astype('float32'), [4, 11, 3])), 6)
uop_8769 = relay.log10(call_8746.astype('float32')) # shape=(4, 11, 3)
uop_8771 = relay.log10(call_8748.astype('float32')) # shape=(4, 11, 3)
output = relay.Tuple([bop_8739,var_8747,uop_8769,])
output2 = relay.Tuple([bop_8739,var_8747,uop_8771,])
func_8776 = relay.Function([var_8737,var_8738,var_8747,], output)
mod['func_8776'] = func_8776
mod = relay.transform.InferType()(mod)
var_8777 = relay.var("var_8777", dtype = "float32", shape = (16, 4, 15))#candidate|8777|(16, 4, 15)|var|float32
var_8778 = relay.var("var_8778", dtype = "float32", shape = (16, 4, 15))#candidate|8778|(16, 4, 15)|var|float32
var_8779 = relay.var("var_8779", dtype = "float32", shape = (132,))#candidate|8779|(132,)|var|float32
output = func_8776(var_8777,var_8778,var_8779,)
func_8780 = relay.Function([var_8777,var_8778,var_8779,], output)
mutated_mod['func_8780'] = func_8780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8792 = relay.var("var_8792", dtype = "uint8", shape = ())#candidate|8792|()|var|uint8
var_8793 = relay.var("var_8793", dtype = "uint8", shape = (10, 15, 8))#candidate|8793|(10, 15, 8)|var|uint8
bop_8794 = relay.multiply(var_8792.astype('uint8'), var_8793.astype('uint8')) # shape=(10, 15, 8)
uop_8811 = relay.asin(bop_8794.astype('float32')) # shape=(10, 15, 8)
output = relay.Tuple([uop_8811,])
output2 = relay.Tuple([uop_8811,])
func_8816 = relay.Function([var_8792,var_8793,], output)
mod['func_8816'] = func_8816
mod = relay.transform.InferType()(mod)
var_8817 = relay.var("var_8817", dtype = "uint8", shape = ())#candidate|8817|()|var|uint8
var_8818 = relay.var("var_8818", dtype = "uint8", shape = (10, 15, 8))#candidate|8818|(10, 15, 8)|var|uint8
output = func_8816(var_8817,var_8818,)
func_8819 = relay.Function([var_8817,var_8818,], output)
mutated_mod['func_8819'] = func_8819
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8827 = relay.var("var_8827", dtype = "float64", shape = (2, 13, 16))#candidate|8827|(2, 13, 16)|var|float64
uop_8828 = relay.tan(var_8827.astype('float64')) # shape=(2, 13, 16)
func_4425_call = mod.get_global_var('func_4425')
func_4427_call = mutated_mod.get_global_var('func_4427')
var_8831 = relay.var("var_8831", dtype = "float64", shape = (20,))#candidate|8831|(20,)|var|float64
call_8830 = relay.TupleGetItem(func_4425_call(relay.reshape(var_8831.astype('float64'), [1, 10, 2])), 1)
call_8832 = relay.TupleGetItem(func_4427_call(relay.reshape(var_8831.astype('float64'), [1, 10, 2])), 1)
func_5897_call = mod.get_global_var('func_5897')
func_5899_call = mutated_mod.get_global_var('func_5899')
call_8833 = func_5897_call()
call_8834 = func_5897_call()
func_2328_call = mod.get_global_var('func_2328')
func_2330_call = mutated_mod.get_global_var('func_2330')
const_8843 = relay.const([[-1.004208,7.769934,-4.883315,1.545419,6.224534,0.496462,0.249179,7.745686,-0.956414,-8.997416,1.930552,5.926492,-4.502449,-7.785296,-3.601595,3.453003,-1.210785,-7.534398,-6.017112,-8.334221,0.540167,-0.601852,-6.067685,-4.496447,0.677030,3.547598,9.262910,-4.815054,5.863428,-0.907338,-5.095272,1.282559,-1.111757,6.980449,3.762005,-1.612929,0.665116,2.034144,-6.729609,-7.227099,6.991776,6.612673,6.592214,-1.440855,-1.015318,-7.194769,-3.627353,1.084894,3.595665,7.831645,-5.387269,8.912797,4.947193,-7.391208,5.725162,1.223255,-7.836998,6.517785,-2.355574,-7.223080,-1.364981,-1.410831,-9.839753,-8.287184,-3.036126,-0.575078,5.083411,5.336270,7.352591,7.867823,-4.996154,0.120086,7.172897,-9.375669,-1.734344,-7.528965,0.793457,4.570819,6.473532,2.215616,9.920268,-2.040182,-7.554853,6.709915,9.326277,-8.489994,-0.495646,-2.682948,-3.959649,0.120556,-9.572474,2.143731,-0.638306,7.616073,-2.869868,-9.043072,7.060326,9.473629,-9.296310,1.457034,6.005343,1.821698,7.462242,1.763235,4.611471,-9.730113,-1.987574,4.066977,-0.091696,-8.200661,-1.409579,-4.511241,-2.957447,3.701544,4.339508,-8.232096,-5.506853,-7.649822,-9.347962,6.132828,-6.208157,9.169536,9.863996,-2.560935,7.004732,4.393442,9.599640,4.540345,4.354003,-1.905135,1.919563,4.791515,-1.656069,0.090997,5.313550,-3.266702,-8.982446,-1.240712,1.674200,4.182584,-8.845762,-4.764335,6.910536,8.560356,-3.194225,7.877236,-8.436937,6.086485,-3.855622,0.295564,8.948800,0.569332,8.794876,6.118223,-6.082405,-7.890597,6.065431,-5.703351,-3.076692,8.635897,5.982765,0.630275,2.243869,7.225504,0.003565,1.478575,-6.464737,0.084441,1.750607,-5.296050,1.231031,-3.478768,0.535067,0.980798,-5.236945,-3.674968,4.542761,3.461110,-8.259170,-5.985073,-8.018168,-3.552249,1.639481,-2.447577,9.082711,-7.938831,2.139542,0.869516,-0.388393,5.470489,-1.295331,-2.874166,7.685605,-5.436074,-9.434159,7.594073,1.864360,-1.629977,7.948423,7.817506,3.775398,-5.318543,-1.018886,-0.766594,-8.619792,8.946370,7.827530,6.545589,7.398569,9.209427,-0.159885,-7.430539,-0.425363,-9.812839,-7.215503,-4.593595,-3.156806,-8.164109,4.257179,4.516942,-5.149772,-3.560829,-6.690896,-8.594279,4.961024,-2.868943,6.618522,5.813750,2.703514,6.068054,0.084083,6.455127,-2.372168,-4.670665,-4.965230,-0.523677,-8.615831,4.975144,-5.334554,6.118773,7.782378,0.533587,-4.216239,-5.084649,3.268587,0.310021,-9.030817,-0.795702,2.924788,-0.200747,-1.599949,-7.513906,9.690676,4.696312,-7.257601,2.227460,-8.464280,-7.135149,-0.844492,-8.841632,-7.927263,-3.574355,5.578113,-7.141614,-2.911024,-3.666337,6.949691,3.893265,-5.042877,-3.800255,8.925101,-0.788018,-6.357850,8.732188,-7.419766,-7.371512,9.652171,2.805295,5.148933,6.958771,-2.175844,-9.987026,5.165314,-7.144996,9.065574,-8.602478,-0.918602,-9.610691]], dtype = "float32")#candidate|8843|(1, 288)|const|float32
call_8842 = relay.TupleGetItem(func_2328_call(relay.reshape(const_8843.astype('float32'), [288,])), 0)
call_8844 = relay.TupleGetItem(func_2330_call(relay.reshape(const_8843.astype('float32'), [288,])), 0)
uop_8850 = relay.atan(uop_8828.astype('float32')) # shape=(2, 13, 16)
bop_8861 = relay.bitwise_xor(uop_8850.astype('int8'), relay.reshape(var_8827.astype('int8'), relay.shape_of(uop_8850))) # shape=(2, 13, 16)
output = relay.Tuple([call_8830,var_8831,call_8833,call_8842,const_8843,bop_8861,])
output2 = relay.Tuple([call_8832,var_8831,call_8834,call_8844,const_8843,bop_8861,])
func_8864 = relay.Function([var_8827,var_8831,], output)
mod['func_8864'] = func_8864
mod = relay.transform.InferType()(mod)
var_8865 = relay.var("var_8865", dtype = "float64", shape = (2, 13, 16))#candidate|8865|(2, 13, 16)|var|float64
var_8866 = relay.var("var_8866", dtype = "float64", shape = (20,))#candidate|8866|(20,)|var|float64
output = func_8864(var_8865,var_8866,)
func_8867 = relay.Function([var_8865,var_8866,], output)
mutated_mod['func_8867'] = func_8867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6466_call = mod.get_global_var('func_6466')
func_6468_call = mutated_mod.get_global_var('func_6468')
call_8896 = func_6466_call()
call_8897 = func_6466_call()
output = call_8896
output2 = call_8897
func_8899 = relay.Function([], output)
mod['func_8899'] = func_8899
mod = relay.transform.InferType()(mod)
output = func_8899()
func_8900 = relay.Function([], output)
mutated_mod['func_8900'] = func_8900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7349_call = mod.get_global_var('func_7349')
func_7350_call = mutated_mod.get_global_var('func_7350')
call_8901 = func_7349_call()
call_8902 = func_7349_call()
func_8816_call = mod.get_global_var('func_8816')
func_8819_call = mutated_mod.get_global_var('func_8819')
const_8908 = relay.const(-6, dtype = "uint8")#candidate|8908|()|const|uint8
var_8909 = relay.var("var_8909", dtype = "uint8", shape = (1200,))#candidate|8909|(1200,)|var|uint8
call_8907 = relay.TupleGetItem(func_8816_call(relay.reshape(const_8908.astype('uint8'), []), relay.reshape(var_8909.astype('uint8'), [10, 15, 8]), ), 0)
call_8910 = relay.TupleGetItem(func_8819_call(relay.reshape(const_8908.astype('uint8'), []), relay.reshape(var_8909.astype('uint8'), [10, 15, 8]), ), 0)
output = relay.Tuple([call_8901,call_8907,const_8908,var_8909,])
output2 = relay.Tuple([call_8902,call_8910,const_8908,var_8909,])
func_8913 = relay.Function([var_8909,], output)
mod['func_8913'] = func_8913
mod = relay.transform.InferType()(mod)
var_8914 = relay.var("var_8914", dtype = "uint8", shape = (1200,))#candidate|8914|(1200,)|var|uint8
output = func_8913(var_8914)
func_8915 = relay.Function([var_8914], output)
mutated_mod['func_8915'] = func_8915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7942_call = mod.get_global_var('func_7942')
func_7943_call = mutated_mod.get_global_var('func_7943')
call_8928 = relay.TupleGetItem(func_7942_call(), 0)
call_8929 = relay.TupleGetItem(func_7943_call(), 0)
output = relay.Tuple([call_8928,])
output2 = relay.Tuple([call_8929,])
func_8934 = relay.Function([], output)
mod['func_8934'] = func_8934
mod = relay.transform.InferType()(mod)
output = func_8934()
func_8935 = relay.Function([], output)
mutated_mod['func_8935'] = func_8935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_9037 = relay.TupleGetItem(func_4162_call(), 0)
call_9038 = relay.TupleGetItem(func_4164_call(), 0)
output = call_9037
output2 = call_9038
func_9044 = relay.Function([], output)
mod['func_9044'] = func_9044
mod = relay.transform.InferType()(mod)
mutated_mod['func_9044'] = func_9044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9044_call = mutated_mod.get_global_var('func_9044')
call_9045 = func_9044_call()
output = call_9045
func_9046 = relay.Function([], output)
mutated_mod['func_9046'] = func_9046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7942_call = mod.get_global_var('func_7942')
func_7943_call = mutated_mod.get_global_var('func_7943')
call_9052 = relay.TupleGetItem(func_7942_call(), 0)
call_9053 = relay.TupleGetItem(func_7943_call(), 0)
func_847_call = mod.get_global_var('func_847')
func_849_call = mutated_mod.get_global_var('func_849')
const_9078 = relay.const([[-3,10,-7,3,-10,4,-1,2]], dtype = "uint8")#candidate|9078|(1, 8)|const|uint8
call_9077 = relay.TupleGetItem(func_847_call(relay.reshape(const_9078.astype('uint8'), [1, 1, 8])), 0)
call_9079 = relay.TupleGetItem(func_849_call(relay.reshape(const_9078.astype('uint8'), [1, 1, 8])), 0)
output = relay.Tuple([call_9052,call_9077,const_9078,])
output2 = relay.Tuple([call_9053,call_9079,const_9078,])
func_9080 = relay.Function([], output)
mod['func_9080'] = func_9080
mod = relay.transform.InferType()(mod)
output = func_9080()
func_9081 = relay.Function([], output)
mutated_mod['func_9081'] = func_9081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8076_call = mod.get_global_var('func_8076')
func_8077_call = mutated_mod.get_global_var('func_8077')
call_9091 = func_8076_call()
call_9092 = func_8076_call()
output = relay.Tuple([call_9091,])
output2 = relay.Tuple([call_9092,])
func_9096 = relay.Function([], output)
mod['func_9096'] = func_9096
mod = relay.transform.InferType()(mod)
mutated_mod['func_9096'] = func_9096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9096_call = mutated_mod.get_global_var('func_9096')
call_9097 = func_9096_call()
output = call_9097
func_9098 = relay.Function([], output)
mutated_mod['func_9098'] = func_9098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7950_call = mod.get_global_var('func_7950')
func_7951_call = mutated_mod.get_global_var('func_7951')
call_9114 = func_7950_call()
call_9115 = func_7950_call()
func_6438_call = mod.get_global_var('func_6438')
func_6443_call = mutated_mod.get_global_var('func_6443')
const_9136 = relay.const([-3.646603,-3.277545,6.912543,-6.215520,2.556365,-1.597865,0.876018,-1.508352,9.376479,-5.447288,9.508791,9.127173,-2.740812,3.750353,3.131536,-3.415806,3.681306,2.567762,0.559840,-4.460036,0.332992,4.554987,-9.202213,-0.702212,6.077733,1.539187,-8.083266,-2.241681,9.805955,-8.040626,-3.807800,-0.562473,6.846322,6.146118,8.640687,-3.490848,-0.507184,6.184546,5.691673,-6.604653,-5.195576,1.193479,7.698098,4.015370,8.935836,0.649191,-0.410311,3.778129,4.445481,0.920877,-1.238182,3.856876,7.951479,-1.399724,-2.572974,9.856543,-9.956014,0.803390,9.990535,-9.038491,6.725560,-9.010422,1.335426,0.764047,-3.432708,4.655444,-3.845051,9.768012,-7.656486,-5.033008,6.824009,9.618518,-1.447679,2.064750,-2.989407,9.644808,0.943423,6.897229,0.089311,0.413303,0.457533,9.519066,8.054161,2.291882,-4.055367,-8.726936,-9.668398,2.333828,5.174431,-1.545304,-3.980326,7.181775,2.156325,-3.935800,3.697376,0.899504,-3.602745,5.664559,4.384202,6.741219,-5.206210,8.384549,-0.821735,-5.938414,7.270874,2.853680,-3.633971,7.286969,3.260279,-2.217597,4.409697,-7.476443,-5.977737,8.656222,-6.028496,8.504592,7.600117,3.616749,4.175029,4.738542,-1.049539,-0.599792,7.699934,9.764004,5.281212,0.256261,3.948186,4.903299,3.733178,8.022771,7.616618,6.751647,-4.421972,-8.063100,-1.687308,-3.499103,-3.785306,1.721093,2.278303,1.417016,-3.874935,5.506784,-1.931861,-3.393441,-1.798200,8.479623,-5.780158,-3.912002,-2.205825,6.735245,-8.930119,0.599552,-6.652317,-7.548591,0.538977,7.235742,-4.158255,4.651334,4.943208,3.514856,-2.362317,9.991232,1.017697,8.575248,2.411111,-6.695491,-3.779821,-3.205978,-1.611891,-5.533183,-2.078820,6.783283,0.530595,8.815205,-9.571996,-8.455090,-4.117964,-7.364212,5.939026,0.897235,-5.585415,-5.786339,3.474538,4.575830,2.605347,-4.187096,5.516177,-4.564579,-2.049870,3.168599,-2.216283,0.005550,-8.852092,-8.113112,6.947575,-6.849274,8.500875,5.702405,2.315297,-1.789151,-9.393910,8.148045,1.036023,-3.761477,4.504549,-3.290719,6.922136,-5.746641,9.882798,4.110686,-7.615641,-7.867573,-5.067599,4.362604,1.763415,-7.607635,-0.140221,0.421952,-0.314368,9.405572,-1.499582,1.372303,-9.980872,2.801239,9.163070,-7.108010,-7.153116,5.761947,-0.506074,-5.802601,4.229552,-8.398884,-4.456287,1.566804,3.944692,3.171639,-3.154018,-3.940936,-5.288927,9.627696,-0.208074,-1.633595,-0.353028,-0.947131,-7.707071,-4.676208,6.087835,9.520349,8.906284,-6.907087,8.798108,-6.975712,0.982297,-4.354830,-6.808302,1.738031,-6.239809,7.442845,9.654087,8.307826,-5.432651,8.000010,-7.761257,-4.010761,4.052119,7.232208,-9.491698,2.227933,-8.710759,2.271343,4.704393,7.040191,-2.858497,-4.005978,-1.248275,5.888167,-4.498690,7.985301,4.563000,-1.925667,-0.736284,-3.103916,7.030859,-5.681802,5.426457,-0.831286,-6.442287,-2.919329,-5.588339,8.258514,3.507115,8.125408,4.562912,-9.758249,-6.342789,-1.812526,-5.730375,9.096303,-3.395066,3.799597,-1.810453,-2.065329,-8.241749,5.354975,7.085582,1.704371,-1.736712,-1.822273,7.437376,-7.228679,7.077465,8.686603,1.077753,7.258783,-5.890336,-4.632786,-6.783314,-2.941292,6.733831,5.217003,-7.543094,7.284505,-1.908452,-8.311049,6.013227,6.918205,2.406182,-9.734369,-8.311428,-7.625990,3.915806,0.920289,5.790976,-3.576443,8.634566,-5.806157,-3.912643,-7.632514,2.091066,0.773827,-0.385611,-1.249332,2.793544,-9.246755,-5.041318,-7.305538,6.560219,-8.063693,9.979929,-9.669576,-9.234454,-5.024024,-6.912397,4.077330,-4.554047,-1.214756,-8.974186,-2.694864,-7.664021,1.718019,-7.441187,-8.170510,8.480872,-2.875619,3.016211,6.234758,7.578994,-5.503563,9.946549,-6.919942,-3.085386,-4.410773,3.573608,-3.762413,5.490569,-1.586998,-0.834230,-0.096406,2.807931,-6.467882,4.534270,2.961803,-7.473066,-2.074730,6.497146,0.410036,-1.405121,-0.897402,-0.164763,2.890153,-0.542337,6.558523,-0.905778,-5.610661,7.337442,-3.641240,5.731570,9.383728,5.710138,0.099705,-4.289893,2.322001,-3.209913,-5.523505,-6.215107,-9.643633,-6.537527,0.226692,5.661684,-8.624478,1.192554,8.445439,-4.668927,-9.725879,0.578458,3.209195,-8.851548,-9.263856,-7.459413,0.838724,-4.684559,-4.627205,-3.931604,2.484766,3.169759,-5.682659,-9.469683,1.807887,-8.960198,-7.373069,7.539342,-4.209881,-8.046440,-3.072943,4.935479,-1.857812,-1.033635,-0.029583,-5.179992,-4.656002,-1.791472,-9.393097,7.712212,1.018831,2.478424,6.733092,3.619933,-8.066333,-1.151971,4.713511,4.575348,6.785213,-1.089166,-5.214663,6.491015,-8.964955,6.309053,-7.764184,7.086677,-8.138853,5.748625,3.226493,3.580433,2.819376,6.747868,-9.457665,-6.862318,-4.856381,5.709343,2.455523,6.818865,-2.489982,5.831850,3.700100,9.314521,2.674138,8.782107,0.403364,0.225298,-3.078489,7.164723,6.101954,-6.844203,-1.535224,-9.270843,-2.533984,-2.922527,-5.775102,7.479638,-8.986919,7.720231,-2.992390,-1.647203,-1.972886,-1.344636,-7.128042,3.319751,5.668544,8.907763,8.438830,1.338301,-0.275349,2.414507,4.187772,-5.455896,8.398889,-0.872946,6.737136,9.275248,-5.118371,-7.676762,-4.617758,-3.376432,-4.818769,5.026110,9.981159,3.078701,-3.259901,-6.710384,-6.638602,5.497218,-3.581830,4.120776,1.611151,5.104775,-1.649042,-6.057081,0.644005,-3.162424,4.675368,-7.403887,-0.321526,-8.745203,-4.551382,0.120186,8.808037,-5.965326,-4.670150,8.799290,-1.531666,8.298116,9.082157,7.561710,-9.813266,-5.489643,-3.186939,-5.747984,-0.650692,9.035144,6.351790,9.482543,-1.372037,-6.158315,7.573520,-0.122157,1.673500,-6.349039,6.152390,3.948928,1.735275,6.747461,-5.619920,7.669022,-3.282017,3.060773,3.120735,4.962946,-5.766054,-5.544060,9.186442,-5.561252,-9.128564,3.933861,-5.069072,8.244166,-5.854302,7.367756,-5.457395,-0.942219,-8.286609,-5.324240,-1.455866,6.549893,7.532539,0.336953,-6.318664,5.084374,-8.250032,-5.705685,-4.110968,6.546729,3.947689,6.393394,8.213188,-7.791425,-5.994038,7.159871,-6.997758,5.084428,-7.705257,1.162634,-4.867068,8.632222,2.289812,-8.928944,6.886341,2.805804,-1.654570,-1.104093,-4.657702,5.037729,2.226265,0.635070,4.562667,9.225840,3.076410,-0.750397,-1.717414,6.016443,-2.616679,9.256890,4.076946,-9.299040,8.499475,3.150691,2.800644,-1.647247,7.993244,5.387767,9.489185,-9.436043,9.580287,-7.133424,-5.847755,6.960357,9.079901,-6.122664,3.307354,2.983501,4.631669,-6.043295,6.077602,7.070708,3.583465,-1.866813,3.719974,3.611975,3.405063,-8.826895,1.455305,-9.555350,-0.761995,3.610398,9.282266,2.365755,3.274333,-9.430229,-0.917118,4.975723,-3.223969,-1.029404,-8.739093,-5.413221,-2.314848,7.177233,-4.773122,-4.174692,-3.701151,9.397024,-7.638701,-8.012663,-6.938090,6.313582,-3.554767,-7.323808,-0.217190,0.932705,4.740317,-4.399218,-1.595087,8.181917,-4.466007,-0.510470,-3.022371,-2.208416,-5.208662,-5.914414,4.578923,4.572746,3.026206,-4.720397,6.821115,-2.591395,3.805706,-1.654271,0.756308,2.449984,5.206282,-9.755748,2.132560,2.726534,-8.755764,-7.173103,8.091953,8.786060,-1.065546,-4.835956,1.752073,-2.752829,3.318860,1.444037,-1.212750,-7.469634,-5.798799,3.133184,-4.654669,8.166708,6.599755,-2.557777,9.359574,7.034274,-4.155443,1.546322,-6.249292,-4.201440,-4.770781,-7.315543,-8.645684,7.090724,-7.424629,-5.100763,8.992670,8.745564,-3.279218,9.338060,5.393602,0.913371,-2.188746,-6.273511,-2.675766,-2.124740,-7.585783,8.057125,-5.080682,0.296784,-6.976835,8.445805,4.852743,-0.590063,-8.480571,2.321230,-1.836383,9.190147,-6.169731,2.198329,6.860713,1.911174,6.121836,-1.395518,0.295480,-1.866222,-1.965131,9.450319,-8.806771,2.043853,0.257758,-7.630179,9.598245,-7.640927,7.612786,-1.531751,-4.940906,-5.133754,-3.052571,8.051685,-9.788555,1.186813,3.213599,-0.290955,-4.617733,-6.935606,3.364257,9.885311,7.628995,-4.425118,-5.702310,8.758528,-2.308421,-6.301002,-0.511720,9.548225,4.766423,3.132160,0.452585,-8.203364,8.602551,-7.824472,5.075411,8.181565,9.353028,-3.473514,-1.433928,-5.453462,5.900760,-9.281877,-0.830499,3.531379,-0.301485,-8.749375,-6.157149,-9.696530,-7.342940,-6.080628,-4.583813,-0.611520,3.792424,4.129275,-5.020965,3.017620,-0.332468,0.268047,4.366953,-8.514606,-2.555822,6.424236,6.018429,-0.204604,-7.731045,-6.178585,5.209819,9.553293,5.549124,-0.498396,-6.817306,9.260580,0.931690,-4.046257,6.914188,9.734163,2.025047,9.941348,-3.214832,-8.827296,-8.454117,5.613276,4.214461,1.742883,-5.478138,-4.529646,1.212429,9.787101,6.530271,8.224603,2.104488,-0.870398,2.403507,2.143393,4.385053,3.069644,-4.821181,8.103646,8.549689,-1.920280,1.352792,-9.518212,1.577382,0.425838,6.339300,6.733478,9.125539,-2.752431,1.524147,-9.901662,5.146237,3.004872,9.719969,-8.185942,4.428057,-3.401337,5.246178,1.440495,-7.743686,0.613527,9.007446,-8.966707,-9.583139,3.013923,6.422779,0.905418,9.718149,-7.052229,9.323521,2.758201,-2.467062,4.177148,7.106119,-9.982278,-4.154692,3.067903,-1.980519,-1.175884,-2.782598,8.806938,-7.601770,1.401151,2.142065,-7.066039,-5.704135,0.221186,7.541372,-4.693496,8.591378,-3.394490,1.626493,7.472399,-7.147467,-2.022414,6.412644,-9.929543,-4.643375,-4.640429,1.189425,6.710597,-6.083503,-5.290192,7.325287,-9.167523,0.641601,-3.965533,6.350615,6.052588,-3.209494,-2.057161,8.604807,4.968355,-1.608461,9.428084,-8.283953,2.924768,9.289388,-2.268752,9.840499,4.804939,1.301529,7.547100,9.375231,-7.210458,-6.649243,8.876491,8.699848,-0.440795,-7.112508,-4.967837,-9.336351,-8.787762,4.647031,-8.925498,8.615693,-1.690858,-5.784591,9.475557,-6.174356,0.411855,9.338637,-0.724941,5.545772,-3.027433,-7.535165,-1.974547,2.657334,-4.163918,6.962897,8.471146,-7.014551,1.054247,2.971266,-4.151458,7.064583,-0.038912,-5.210555,4.891430,8.870271,-7.468968,-6.877435,-4.769645,7.153899,3.904809,-1.565153,5.622698,-5.418436,9.784131,-8.260049,2.184445,6.438890,-4.904355,-5.956157,2.836862,6.265071,3.570709,-6.015929,0.720570,-5.786226,-8.562609,4.123334,7.418536,-8.937624,4.311325,-7.059962,-2.747208,1.757075,4.438955,6.337096,7.012146,-5.955407,-7.390270,4.824128,-5.702985,-4.266839,-3.097494,0.016905,0.588004,-3.422226,-1.726900,9.377147,-4.053144,9.149409,-8.858813,-4.425272,5.301985,-3.084135,7.801750,-2.700777,7.625919,-4.243098,-8.218691,8.103014,6.793019,7.200416,-8.122778,3.897601,2.343257,2.994696,8.182652,5.563277,-3.615968,-3.272083,0.784407,-7.881204,-2.927438,-0.250588,-6.453352,-1.534598,8.766771,7.280096,0.704491,-6.030632,1.983350,-5.101908,7.201956,5.967036,-8.347069,6.417184,-0.771312,-4.176191,-9.142756,-4.361667,2.019419,0.844707,-6.458748,-4.203630,6.644564,-4.266646,-0.485986,3.305678,-0.020228,-7.338003,-8.251066,5.801737,3.446376,9.823240,-5.577126,-4.306366,6.615645,1.996964,-9.562459,8.288368,-2.495721,-2.656470,-1.892515,5.322689,-8.583258,7.187019,6.766755,-0.377664,6.294719,5.757197,7.907740,1.241455,1.776763,-5.941614,-5.588800,5.408458,4.012947,-4.946654,8.078846,-7.537218,6.268476,-5.724527,-6.683022,3.958174,3.203603,-4.360540,-4.483574,6.762559,-4.101743,5.954900,4.826404,7.003163,-3.068028,-6.962869,5.136599,6.364972,8.450180,-6.062880,-3.726803,0.185460,-4.100688,-2.059559,9.638138,-7.694636,3.138962,-3.206673,-9.853319,6.652469,6.699208,-8.157114,8.453673,8.538086,1.505255,-7.215044,1.887393,5.224980,1.834902,-4.138433,6.990154,-2.034132,-1.478210,7.370998,1.458238,3.116483,4.340832,7.228703,-1.472264,2.620536,-1.083458,5.425801,2.353507,2.966484,4.142991,2.977951,-5.995256,3.511722,-5.074980,5.856201,-6.741263,5.246600,-0.209539,-5.027882,7.013207,3.482130,4.224550,-0.404899,0.434047,-1.497076,5.204487,-9.103504,7.741531,1.859264,-1.850475,7.024197,8.689345,-8.339130,-5.653278,-6.084184,-5.140941,6.446156,2.535971,-1.504100,-3.333011,5.154750,-9.208625,7.349725,4.979420,-6.602366,-6.402600,-3.603139,-7.931691,9.612747,8.757743,-9.460223,2.542275,-1.848820,0.112941,-1.855624,2.567042,-0.625608,7.496364,3.877972,-9.980151,-6.883630,-1.623479,-3.978298,-5.816262,6.868937,-6.057097,7.279636,4.182132,-4.014807,0.205698,-1.941712,-0.125161,-9.142064,8.512361,-7.248673,5.735706,-8.389072,-2.173887,-4.698524,-1.936005,-4.622899,-2.522085,0.923378,9.551199,-3.862382,-6.281739,8.866800,2.874010,-9.544470,-9.647171,-8.389348,5.139020,2.317636,-3.481508,-6.963354,5.260855,3.420053,5.428688,1.869157,-8.032468,9.681220,2.666407,7.880748,-5.555653,2.786467,-0.789576,8.768394,-9.093695,6.835344,-9.605102,2.954576,8.749841,0.182235,4.416632,6.540704,9.595029,-1.502975,-9.654482,4.592194,1.781078,0.725600,4.024120,-9.710095,3.026634,-3.962754,6.208394,2.153000,-9.986173,7.585971,3.319804,0.094341,4.133561,1.499710,3.649153,4.904533,9.365459,-4.194040,0.663141,-0.971878,3.392108,-1.332643,4.812780,0.955111,0.346852,3.378878,3.875351,1.716519,7.506127,-9.852229,8.636111,0.396637,-0.482026,1.562838,-8.092065,-6.775700,-7.539938,0.866811,-7.179688,5.535100,0.735395,7.433371,3.057606,-8.809224,5.593170,3.236152,-0.805307,-6.297553,5.676813,-0.714130,0.542363,3.369188,5.357136,0.792227,1.885324,9.268049,-3.483328,4.971101,9.668775,-3.313538,8.913142,-9.177570,-0.941765,-9.554911,-2.212088,-3.059533,-8.514094,-3.997082,-0.133814,0.747536,-0.776720,-6.227954,5.820115,0.064455,8.147973,-3.058064,4.348056,-9.657757,3.289900,5.711559,4.004117,9.368955,8.605261,-0.801827,-8.649814,9.379740,-5.073380,1.014474,-8.012518,4.635435,-9.672154,-5.853449,-2.343973,4.414216,9.488090,6.501807,-8.113712,-4.198204,-9.885949,2.179941,3.765981,-9.033896,9.431475,6.958293,-9.676087,9.503968,-0.655829,-3.905426,3.029039,-6.721921,1.715542,6.192300,8.851543,3.244882,-9.831660,-2.052005,-7.735140,-1.680132,-8.800576,8.958674,-5.480316,0.440328,-7.480126,7.282056,7.602263,-2.287577,8.145128,6.591198,-4.071586,1.464589,1.708469,-2.763384,-7.289271,5.892927,-3.606675,3.364561,-4.445150,-0.029266,-4.939108,-9.228938,2.400103,-6.306209,-8.378900,0.909239,1.214292,-6.862315,-5.704952,-4.238967,2.517554,8.798649,-8.045974,-7.823859,9.784481,1.459606,-5.455596,-7.260549,-8.748103,-2.148457,-5.616804,2.132553,-1.834976,-9.516468,-5.880777,9.993446,0.913762,-4.802251,3.033599,-5.979521,1.046694,7.191106,1.824817,5.889531,-2.769696,-4.078459,-3.428399,-2.798832,9.811844,3.797596,0.385256,5.036880,-6.012216,-4.947745,-9.442637,-6.401640,-1.787028,3.777766,9.128945,-1.895578,5.855049,-1.727759,-9.830386,-0.419385,-0.710298,-5.780011,2.517090,-5.091154,8.424805,6.726988,7.615023,0.828813,7.226165,8.968086,1.970453,8.855993,-9.834794,-8.048231,-7.915424,2.976150,9.736790,5.316218,2.899359,-1.058824,-5.431541,3.476061,4.831757,-7.485132,7.468124,-9.074386,3.419415,6.625443,1.429471,-1.638391,6.375710,-2.955398,0.056030,4.010831,8.622571,1.438530,2.547445,6.907367,3.088541,-1.522930,2.247096,-0.551027,-0.671161,9.415809,2.156747,8.313127,1.547492,9.701090,8.155189,1.113580,-1.966814,6.078717,4.519503,1.298116,-0.226444,-6.181828,-0.070723,-4.249390,-5.392783,-4.822537,3.625205,-2.959641,-5.501421,-1.026207,-5.399004,-9.219383,-0.744236,3.550568,7.581864,1.978123,-0.996763,9.440044,-0.271757,5.988146,3.423625,-1.269772,0.115274,9.824359,5.472077,-1.440598,-3.971367,-6.313479,-7.340358,-2.787770,-1.456748,9.020829,2.429103,7.382294,-0.007078,0.819902,6.976998,-8.183675,-2.215427,-1.785670,1.035254,-5.204001,6.607783,0.542538,-7.964082,2.021657,7.093168,6.210642,-5.186653,-0.646313,0.582411,-9.528057,1.749221,7.446791,3.981527,9.299253,-3.608549,-5.772349,5.283436,0.591211,6.193669,-0.034825,7.664172,-7.007651,5.284662,-7.583031,-9.514822,9.101828,-7.646560,4.773233,-6.318952,-6.064332,-4.840564,-2.927712,-0.108380,3.132962,0.865460,-4.462923,3.603694,-4.806203,0.961287,1.972358,6.917047,-6.653217,-2.422685,4.062672,-4.698386,5.933393,-4.386539,-4.303648,-7.410936,9.441131,-8.201601,-0.423855,-1.223219,-5.424740,-6.489043,6.006946,-1.870521,9.272220,6.078705,0.560272,-4.902755,7.178312,-7.233868,-4.361498,6.775667,-6.204797,3.872453,-9.794528,7.267672,-6.839512,-1.362368,-9.748622,0.466717,7.860337,-2.557766,-3.916998,-4.374903,-6.866461,-6.064790,9.345599,-7.062906,5.976810,-1.193692,0.970187,-2.000874,3.540310,4.203053,4.628353,9.112472,4.218475,7.510904,7.372466,2.350726,-9.304326,-1.605364,-2.772033,-8.180226,-5.078915,5.713089,-9.621648,2.466288,-0.290571,4.439992,8.245494,7.259689,6.284843,0.226018,-7.550234,-3.147143,-6.224765,-3.300285,7.493728,-9.038185,7.893124,1.827239,1.446275,-0.709638,6.430446,3.588042,-2.920360,6.702447,6.118712,-9.027770,-0.572454,-1.625219,1.163048,8.173444,1.265719,3.798249,8.546060,1.313623,0.166952,-4.305302,3.523382,-4.690019,-0.480801,7.117229,-7.393251,2.871425,-2.713258,2.629367,-6.974406,-6.777488,-0.200250,8.682281,-7.409566,-3.980140,-4.689557,-7.053566,-9.191332,4.455577,0.387569,-6.072920,9.899267,-6.774667,4.948279,8.841764,-2.132048,-3.674711,4.025400,-6.960432,-7.915068,-9.526632,5.829185,-5.728732,9.728666,6.822079,2.739503,-0.367766,0.180696,-3.701318,-7.978200,7.301976,-7.707322,4.924488,2.101512,6.333871,-6.806149,-4.746553,4.031556,1.431792,-0.740335,3.852042,-2.563773,-0.504304,-7.299951,-4.273739,7.727796,7.963299,7.785168,3.555881,-7.874832,-1.835368,-2.007804,-4.570651,-4.210895,-0.414653,-6.997680,-7.918441,8.118061,0.924439,0.565272,-3.874316,8.058067,-7.836720,-7.859298,2.364201,3.749601,2.170056,-6.162927,9.253102,8.800443,2.634144,0.414197,-7.428552,4.374383,-8.772454,-5.067080,4.434979,-1.049034,-6.529232,0.653886,4.735836,-5.717205,5.996355,-9.260332,9.719090,-0.846170,-9.815413,-6.976114,0.390627,-6.955955,-4.734099,-4.334037,-2.847352,-1.602777,-1.544983,-7.205779,-2.381876,-2.841540,4.248795,-4.264673,1.917889,6.292675,-3.032709,-8.010910,4.279409,4.238804,1.220056,0.132959,-6.009152,2.540688,-8.015171,-3.338710,-1.948739,-2.996878,8.209722,-0.729816,9.764603,-6.680703,4.996480,6.216328,9.884901,-9.852955,2.337942,-8.971619,0.459333,-0.807640,7.219381,-5.923054,5.964155,2.476096,7.370606,8.390443,-7.214631,-0.701457,6.299553,-1.250624,-5.234880,5.413007,3.099354,7.714138,9.632324,-9.507500,-2.237690,-1.126918,4.945249,5.852232,9.848620,5.004327,-0.296843,5.364512,-9.663922,9.936194,7.900605,-3.376169,-0.960900,5.780434,8.562546,3.373530,3.836139,6.373511,6.283777,8.305492,-1.840725,-4.065227,6.202503,-2.031328,-3.100688,-0.161387,-3.415413,-1.867287,9.352307,5.763137,3.185558,-9.211689,-4.076229,7.150710,-7.121493,1.717806,4.230297,-5.337825,4.708115,-4.163019,-9.527421,8.899418,8.695410,5.868282,-4.850680,0.568859,3.262387,-6.640515,-4.247961,-7.331870,-7.354814,8.238965,1.133756,-3.584235,-1.720331,-8.707362,-4.875881,0.502982,8.331720,-1.921437,5.495231,2.168598,4.680396,5.319508,3.644248,3.031075,6.431721,-9.964954,-3.181847,2.578658,0.224903,9.279424,-0.777862,-0.696181,4.284855,8.979556,-7.132820,-2.888106,-0.769578,5.901236,5.443444,0.246639,2.812838,0.656404,7.363485,-1.599410,4.651208,-5.175307,9.369005,0.614009,2.081960,0.503495,-0.806783,9.964777,9.728285,-9.801572,1.758200,2.089749,7.731554,-7.575009,-1.860557,-5.911039,-5.546421,5.159808,7.281622,3.809121,6.724937,-2.640585,-4.457674,-6.726070,9.446611,-4.072527,-3.664412,0.693551,-2.494323,-6.867107,7.375083,-5.341049,1.680689,0.505913,8.145969,7.485098,9.842570,-2.212823,-8.881785,-8.374236,8.430410,-0.666560,-0.606294,-2.785757,-2.957446,8.931973,9.909120,5.733071,0.834333,1.465878,5.946174,3.922687,-1.925025,-2.037586,-5.687330,-7.400564,1.136799,-8.424151,2.587868,6.308531,9.738829,7.447429,-0.097478,-3.068557,6.124130,-5.074666,-6.349823,4.846093,6.211871,7.853798,-4.565317,-7.078258,8.277525,-4.680695,5.840857,-4.337747,-1.127433,1.995233,-9.864410,5.879176,9.611996,6.601696,9.876236,-6.567684,-5.966804,7.383863,-9.808802,0.633765,-5.669607,-0.462678,1.387110,-4.305104,-2.007962,-4.167091,1.147600,-8.816272,-9.185753,4.405867,-7.481937,-6.832634,5.816969,-0.275101,5.307086,2.069885,5.727172,0.700821,-9.805978,-4.807465,6.721702,-8.791711,-1.331577,2.491575,-5.520720,2.879610,9.094490,2.161126,2.622017,-4.253370,3.928505,-1.397819,3.573755,2.771949,7.160651,-5.536549,6.086652,-0.929051,1.591005,-5.309608,-1.353164,-8.723005,5.524006,-2.181221,1.183743,-5.020755,0.653785,6.657916,-4.768705,-2.893149,2.079164,4.154248,9.052731,-5.196094,6.501048,-8.532552,-5.009153,5.901676,9.274554,-7.360277,-1.504240,6.133198,3.951755,-3.716588,-1.089808,-9.403907,5.165012,-5.865079,4.136410,4.152951,3.686615,-4.756399,1.416982,8.822504,0.552160,6.811157,-3.575565,3.971386,-0.652654,-5.110713,2.860602,-0.871647,-4.896772,6.710108,0.475749,-5.737729,2.908138,5.112833,1.424496,0.894713,-2.092128,-5.487933,3.479167,8.215654,-5.903908,-1.486431,-6.929712,-2.285015,8.847684,-0.321319,9.145495,6.691168,5.783806,8.351822,-2.678106,3.551374,7.856670,2.695265,-4.113337,-2.863625,-7.652020,-6.821023,1.502143,5.257494,-6.564793,-3.115777,0.030000,-4.966146,-9.633833,8.529856,-6.980639,4.793595,-9.037844,0.330407,7.793818,6.960672,-6.635058,-8.378952,8.368833,6.889343,3.705892,3.489819,1.940686,4.676454,4.081638,-3.993783,-4.291055,3.214466,5.888629,9.792752,5.854378,-6.239393,-9.217130,8.817329,9.585549,2.399019,-2.042371,2.344058,1.750094,1.880147,9.456667,-6.661831,-3.701175,-8.588973,-2.533410,-4.832851,0.121953,-7.790546,-0.641443,5.546740,-4.555786,-6.521241,8.559247,-9.204857,2.367384,5.050431,-7.245396,-7.156576,0.506822,-5.503542,-4.401945,7.071161,6.742298,3.377660,-6.676743,7.862285,5.693812,2.447413,4.002588,1.917571,-3.664524,4.475524,6.411720,1.543872,0.916543,-3.064810,-7.034412,1.697905,4.815139,8.869574,7.302548,-3.269692,1.050888,6.657096,-2.188499,5.078663,6.812289,1.873266,-9.821714,7.435384,-4.421246,2.179164,-3.391435,-5.454013,8.241626,5.720690,5.319763,4.616469,7.233660,3.000854,-6.999835,-6.658175,-7.819586,-4.510172,-1.468784,-2.873442,6.461551,-5.621789,-8.738024,-4.339752,-1.872872,-7.531515,7.931562,-4.719705,-6.274157,-3.723259,-3.757027,-3.510528,-2.950861,7.932626,-7.965367,0.008881,2.431666,6.437801,8.402538,1.006754,9.586952,5.114012,-6.362777,-8.383601,1.476137,8.871871,1.458184,-3.968704,-1.711482,6.287789,2.135982,-1.179181,-2.924841,-8.489081,3.599610,7.180502,7.235794,-3.894516,7.915529,-9.510624,4.178148,-2.588767,5.639969,9.624224,4.308247,7.649736,8.469121,9.051865,0.577420,1.653854,-8.758178,-5.022694,0.692666,5.556612,7.081859,-4.047406,6.183422,7.866079,0.611885,-4.725627,4.313013,-0.777015,8.654440,-7.616725,0.524683,-8.595055,2.737487,-0.642030,1.163809,5.658536,8.997230,3.540726,-5.685873,-7.886347,7.170828,-4.823965,-8.936374,-8.981969,3.655168,-4.948323,-3.675803,-5.383285,7.073225,9.446179,-4.819940,3.344666,-1.842987,-5.549847,-0.355272,-5.322746,4.713868,-3.860587,6.528093,1.069261,-5.163725,-6.621698,-3.533158,-4.044382,9.517178,-4.684334,-6.161292,0.608251,8.799901,3.529618,-8.934398,7.459967,5.481282,4.469848,-8.485422,3.667149,9.142981,-9.250740,-1.901692,6.129854,-5.684619,3.419094,-4.306650,3.233671,-2.942960,6.924022,-4.373669,-8.962422,-2.438437,0.345262,-7.355005,8.244102,-3.374657,-8.662350,-6.651686,-9.250099,8.138694,8.930089,-0.250760,0.468447,-1.303039,-5.070251,-2.074209,-6.680753,-6.153971,0.301778,-2.709683,-5.748409,-4.541391,9.766956,2.604416,4.793864,9.275711,-7.445345,3.326409,-3.615620,-8.269948,4.355959,1.227324,9.891927,4.795512,-6.746601,-3.296035,-3.450010,9.005011,5.269821,8.890464,-3.875407,-5.109739,-6.144532,-0.061203,9.880439,7.442865,3.292162,-2.401220,7.838039,-2.497652,7.177672,-9.893734,5.705169,2.489361,-5.579837,-7.619809,2.400688,7.733155,-3.865519,-9.484479,-4.787331,-1.261003,-9.274275,3.434422,-3.902478,8.532113,-1.599009,1.134884,-8.043962,-8.605664,8.958359,5.845890,4.184161,6.242020,-4.504716,7.158732,7.871295,3.108420,-5.704085,0.478378,-9.151881,-6.743228,7.059996,-0.813536,-3.908920,-1.003821,5.298122,-8.779660,9.019229,8.532494,0.634914,-4.431608,-1.628975,-5.167660,-9.207515,-0.130061,4.783197,8.819197,-9.681524,-1.987395,4.067484,4.314370,-0.142474,4.581811,6.232851,2.299169,-2.218644,5.420465,7.517629,4.883855,-5.145301,-4.021150,4.931059,-4.019664,-1.307763,-3.100215,7.588827,-2.196830,-7.299117,7.264196,-6.801031,-7.559512,0.137376,-4.974674], dtype = "float32")#candidate|9136|(2475,)|const|float32
var_9137 = relay.var("var_9137", dtype = "float32", shape = (840, 4))#candidate|9137|(840, 4)|var|float32
var_9138 = relay.var("var_9138", dtype = "float32", shape = (336,))#candidate|9138|(336,)|var|float32
call_9135 = relay.TupleGetItem(func_6438_call(relay.reshape(const_9136.astype('float32'), [15, 11, 15]), relay.reshape(var_9137.astype('float32'), [3360,]), relay.reshape(var_9138.astype('float32'), [336,]), ), 4)
call_9139 = relay.TupleGetItem(func_6443_call(relay.reshape(const_9136.astype('float32'), [15, 11, 15]), relay.reshape(var_9137.astype('float32'), [3360,]), relay.reshape(var_9138.astype('float32'), [336,]), ), 4)
output = relay.Tuple([call_9114,call_9135,const_9136,var_9137,var_9138,])
output2 = relay.Tuple([call_9115,call_9139,const_9136,var_9137,var_9138,])
func_9140 = relay.Function([var_9137,var_9138,], output)
mod['func_9140'] = func_9140
mod = relay.transform.InferType()(mod)
mutated_mod['func_9140'] = func_9140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9140_call = mutated_mod.get_global_var('func_9140')
var_9142 = relay.var("var_9142", dtype = "float32", shape = (840, 4))#candidate|9142|(840, 4)|var|float32
var_9143 = relay.var("var_9143", dtype = "float32", shape = (336,))#candidate|9143|(336,)|var|float32
call_9141 = func_9140_call(var_9142,var_9143,)
output = call_9141
func_9144 = relay.Function([var_9142,var_9143,], output)
mutated_mod['func_9144'] = func_9144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6937_call = mod.get_global_var('func_6937')
func_6938_call = mutated_mod.get_global_var('func_6938')
call_9176 = relay.TupleGetItem(func_6937_call(), 0)
call_9177 = relay.TupleGetItem(func_6938_call(), 0)
uop_9218 = relay.atanh(call_9176.astype('float32')) # shape=(11, 14, 5)
uop_9220 = relay.atanh(call_9177.astype('float32')) # shape=(11, 14, 5)
uop_9225 = relay.asinh(uop_9218.astype('float64')) # shape=(11, 14, 5)
uop_9227 = relay.asinh(uop_9220.astype('float64')) # shape=(11, 14, 5)
output = relay.Tuple([uop_9225,])
output2 = relay.Tuple([uop_9227,])
func_9236 = relay.Function([], output)
mod['func_9236'] = func_9236
mod = relay.transform.InferType()(mod)
output = func_9236()
func_9237 = relay.Function([], output)
mutated_mod['func_9237'] = func_9237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8018_call = mod.get_global_var('func_8018')
func_8020_call = mutated_mod.get_global_var('func_8020')
call_9321 = relay.TupleGetItem(func_8018_call(), 0)
call_9322 = relay.TupleGetItem(func_8020_call(), 0)
output = relay.Tuple([call_9321,])
output2 = relay.Tuple([call_9322,])
func_9332 = relay.Function([], output)
mod['func_9332'] = func_9332
mod = relay.transform.InferType()(mod)
mutated_mod['func_9332'] = func_9332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9332_call = mutated_mod.get_global_var('func_9332')
call_9333 = func_9332_call()
output = call_9333
func_9334 = relay.Function([], output)
mutated_mod['func_9334'] = func_9334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8093_call = mod.get_global_var('func_8093')
func_8094_call = mutated_mod.get_global_var('func_8094')
call_9345 = relay.TupleGetItem(func_8093_call(), 0)
call_9346 = relay.TupleGetItem(func_8094_call(), 0)
output = call_9345
output2 = call_9346
func_9353 = relay.Function([], output)
mod['func_9353'] = func_9353
mod = relay.transform.InferType()(mod)
mutated_mod['func_9353'] = func_9353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9353_call = mutated_mod.get_global_var('func_9353')
call_9354 = func_9353_call()
output = call_9354
func_9355 = relay.Function([], output)
mutated_mod['func_9355'] = func_9355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7950_call = mod.get_global_var('func_7950')
func_7951_call = mutated_mod.get_global_var('func_7951')
call_9356 = func_7950_call()
call_9357 = func_7950_call()
output = relay.Tuple([call_9356,])
output2 = relay.Tuple([call_9357,])
func_9375 = relay.Function([], output)
mod['func_9375'] = func_9375
mod = relay.transform.InferType()(mod)
output = func_9375()
func_9376 = relay.Function([], output)
mutated_mod['func_9376'] = func_9376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9096_call = mod.get_global_var('func_9096')
func_9098_call = mutated_mod.get_global_var('func_9098')
call_9377 = relay.TupleGetItem(func_9096_call(), 0)
call_9378 = relay.TupleGetItem(func_9098_call(), 0)
output = relay.Tuple([call_9377,])
output2 = relay.Tuple([call_9378,])
func_9391 = relay.Function([], output)
mod['func_9391'] = func_9391
mod = relay.transform.InferType()(mod)
mutated_mod['func_9391'] = func_9391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9391_call = mutated_mod.get_global_var('func_9391')
call_9392 = func_9391_call()
output = call_9392
func_9393 = relay.Function([], output)
mutated_mod['func_9393'] = func_9393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6370_call = mod.get_global_var('func_6370')
func_6372_call = mutated_mod.get_global_var('func_6372')
call_9461 = relay.TupleGetItem(func_6370_call(), 0)
call_9462 = relay.TupleGetItem(func_6372_call(), 0)
func_1756_call = mod.get_global_var('func_1756')
func_1760_call = mutated_mod.get_global_var('func_1760')
var_9466 = relay.var("var_9466", dtype = "float32", shape = (336,))#candidate|9466|(336,)|var|float32
const_9467 = relay.const([1.747699,-4.235250,-1.706608,9.640785,6.940030,5.354119,3.475797,2.018553,-2.319042,3.361799,5.017900,9.395840,-6.117595,2.667144,8.725098,9.403946,-8.887628,8.478164,-0.725672,-9.355449,4.316393,4.923451,0.477445,-4.167726,6.278255,-6.539222,-5.091320,1.715576,7.744464,-2.799335,4.070177,4.566231,9.980367,-2.805184,0.842622,8.799685,-8.144685,8.123917,9.425355,0.367939,-0.631170,-3.870411,4.834143,0.028247,-6.812339,3.452918,1.611986,2.711518,-5.808826,-8.442965,-2.612191,-0.203069,-8.314135,1.365431,-4.700282,5.743680,-8.562585,6.017792,9.915598,-5.097798,-1.712214,7.859463,-8.192477,6.382216,-5.082446,-9.760862,4.169437,-2.234873,1.935188,-2.508222,-2.695792,-4.165896,5.843403,0.513692,-3.257331,-4.078966,0.346898,0.065404,9.972388,-1.780491,-1.240819,-5.337324,-9.151477,-0.002836,-9.783742,8.813986,-7.800347,-4.700399,8.413426,-2.956488,4.627460,-4.031419,-0.956455,0.429152,-7.358942,3.519692,-9.607803,6.758000,-0.379550,-8.054521,-7.755403,-6.464956,0.747649,-8.196577,-0.370581,2.416627,2.433112,-1.013915,2.987058,5.762309,-7.569630,-2.559163,4.281059,4.619938,8.379582,-7.656276,6.445458,-9.746456,8.601524,1.818114,9.331990,-0.843011,-9.629147,-2.118056,-2.068160,-9.852697,1.994548,5.772705,-9.498393,-9.031930,2.364641,5.256955,8.563398,6.621541,-3.888897,-0.508954,9.202471,-9.104528,-0.089383,6.708173,6.641048,1.214786,4.659549,8.405619,0.120870,9.666890,-5.828152,3.327637,0.966729,6.290391,3.650353,5.435619,-9.078046,-0.175535,6.521861,3.274455,5.724428,1.038443,5.232019,-2.011479,-4.429890,6.686806,-2.803531,7.249115,-6.671118,9.980189,-8.795082,-0.615081,8.718224,3.745952,3.356422,7.745168,7.229533,6.892898,6.452074,7.809672,1.818731,-7.653793,6.529867,3.336995,-5.281011,7.063991,-7.456882,1.023437,5.574817,-7.152395,8.134834,9.750666,-6.720477,-4.686498,2.636338,5.548732,-6.589386,-3.198131,8.010237,6.119323,5.875516,8.102865,2.442997,4.645838,7.513466,1.752317,0.303441,-8.086282,1.245177,0.082814,-9.887451,3.178086,-3.675629,4.927304,-8.711707,-6.516733,1.046277,1.481959,-4.316760,2.391363,-8.807892,8.288206,-2.031218,5.763277,-8.315384,-1.469803,9.666932,3.915432,4.484070,-6.151925,-6.723288,8.267573,-3.470445,-7.591048,4.713488,-2.348542,-6.393571,0.733289,6.841072,-3.792593,9.220034,7.840238,-9.910998,6.539681,3.203270,3.007311,-2.704826,2.286795,5.753118,9.993581,-4.947465,-1.852288,9.122621,7.396899,-8.164125,-6.444199,-6.922170,1.863331,4.588127,-9.597318,-8.794131,-0.393216,0.517252,3.570070,3.463746,7.632340,-1.696822,-4.826817,-3.449044,8.087797,8.193085,-3.933135,4.310564,-5.446788,-8.888924,8.951552,6.236621,4.745053,7.523869,4.814353,-7.576278,-9.109013,0.590807,-0.202706,-3.447237,-5.216645,-5.735700,2.646507,-2.936073,-9.664314,5.725170,3.209347,5.171331,9.425146,8.800575,2.491702,6.613724,3.083237,-8.067463,-6.116223,1.106139,-0.051368,-7.944606,1.705853,3.871905,7.490761,5.570576,0.641971,-9.641689,3.927655,-4.705456,6.556975,3.061702,-2.768443,-8.024287,-8.436984,3.244484,7.107638,9.394177,0.558647,-6.812865,5.777947,7.467170,-5.900727,4.225592,-4.917352,-7.279940,3.128187,-9.191910,6.119918,4.648488,-4.853645,-7.396049,-4.335977,-3.159969,2.628901,-2.748084,-0.539720,2.947691,3.724802,-0.247707,-7.556891,6.311583,-6.684843,4.890645,4.220031,-8.012128,-1.958548,4.691363,-1.060032,-1.887513,5.680210,-7.844176,-5.929043,-9.976211,-7.190240,6.418616,-8.625498,-8.987488,-9.641812,-0.793879,-6.237090,6.432865,-0.630408,1.838076,-4.013765,-1.098973,0.686404,7.593676,-7.714302,5.503387,3.020475,-2.705870,-7.960782,-9.166584,-2.009634,-6.819712,1.121178,5.600110,-1.664487,-1.923832,-0.494339,-4.800465,6.163676,-3.281777,-6.754141,-6.096000,-2.111400,1.185388,-2.397739,-1.914118,-0.500698,7.501355,-5.914402,2.080767,-2.651242,-9.664459,-3.724713,-1.862401,-2.727610,-9.450259,-0.489146,-7.230592,1.333609,2.895803,-5.506580,-0.461787,-1.896580,-0.851959,4.835568,-6.290935,-6.283877,-3.847697,3.249104,-2.169355,8.574718,-5.006112,-6.368664,0.081392,-1.178724,6.655838,-2.022982,-0.537469,8.632257,3.745811,-0.428731,-9.078766,-6.555618,-7.634258,7.188563,-4.036769,2.647947,8.708361,2.215753,3.202133,9.273586,-7.471086,-5.162434,7.609461,-4.919904,-3.819326,-8.752753,7.273862,-3.600297,-1.412479,-8.807116,-5.036143,-1.205889,2.207625,-6.951512,2.077899,8.952070,2.297803,-7.612290,-0.416110,-0.302047,-3.920009,3.068801,2.572049,8.160496,-9.856257,-1.885834,6.129087,-7.182297,6.806409,2.688943,-7.111066,-2.633513,-7.255531,-3.791260,6.511063,-3.288150,4.674786,5.074435,6.789396,7.767930,3.349397,-5.396948,-1.602766,1.650399,-3.517387,-9.369874,-9.247003,-8.249849,-0.598270,7.117156,9.411605,1.051627,0.909784,-3.779392,3.348072,-0.262522,3.615069,7.337660,4.935660,1.861159,7.508743,8.440085,8.484410,-6.000823,-6.336810,8.537705,7.634864,0.485219,-7.312601,5.576304,2.867810,-7.284978,3.301799,-5.590811,-7.112595,-0.867026,6.046691,5.781934,4.182223,-6.158263,0.938655,-2.166262,-7.395250,-7.721331,2.366330,-6.147790,5.898065,7.832478,-4.531218,-2.309856,-0.459919,-5.372645,-5.768188,-0.976239,-0.198121,0.300050,-4.128084,-7.476686,0.495332,6.089215,4.453618,7.804348,-6.742113,7.449001,-4.049162,-7.245840,-9.201407,0.235949,-0.015462,-0.489234,-0.535861,0.582072,6.621290,-2.354565,-8.110543,0.842964,1.474684,-6.497291,-3.595155,2.845379,4.650533,9.549395,-4.827659,-3.654643,-6.160150,2.639139,5.517401,1.065888,0.805502,4.243138,-6.974578,2.840364,-8.950228,3.765060,6.346099,3.991167,-8.509116,-2.881336,7.448403,-7.449699,5.607608,4.748688,-0.882656,-8.706222,-5.429020,1.034089,-2.868812,-4.726637,-0.183211,7.133880,-1.123673,9.182624,9.406414,-7.561327,-5.251679,-2.516960,-7.653552,-1.636224,7.678245,-2.040420,2.462668,-4.785286,-5.830962,-9.103195,-8.948530,-1.698405,-4.605417,-0.813490,6.377772,5.775929,5.696200,-6.204117,8.151165,-1.343987,7.641381,-9.160939,-0.278794,-2.997883,7.615088,0.500586,9.920388,7.460786,2.285045,1.271684,-6.361458,3.708323,2.548606,1.102405,-7.974190,2.569177,0.687492,-8.706571,-2.893967,-5.777966,2.723612,0.818281,-2.674048,6.788588,-6.411504,-7.177017,0.062890,-7.119352,7.392525,2.975903,4.679377,0.422764,-7.691210,-5.860007,8.979680,-2.908511,2.835777,1.160116,-1.053219,0.475808,8.573284,0.425207,1.005053,5.568653,-0.049648,3.520354,2.958854,-5.452757,-8.763266,-0.619090,2.151112,7.218338,5.926372,-6.610822,3.786580,-5.208477,-1.533733,4.829683,-2.023290,-1.254086,4.516043,-6.406808,6.332691,-3.516372,-0.048666,4.366050,6.421321,-8.911947,0.822891,9.974664,-0.566163,1.585587,9.384047,6.507866,-5.911390,-6.757823,6.687961,-9.681534,6.272962,-2.419035,-5.171930,-2.066512,-9.954208,-9.906257,1.249672,-9.285228,5.142799,-6.347203,-5.084658,-4.406545,-6.307443,-5.305542,-8.013471,-5.683355,9.622493,9.979037,-6.130579,-2.200958,-9.602165,-4.818735,-6.059186,9.576947,-4.016502,-3.264575,6.955710,0.906596,-9.123452,3.851184,8.302793,-0.049130,2.191631,-8.345318,4.611824,-8.106803,0.783549,-3.482151,-5.890494,0.368666,9.910725,4.268598,0.409654,-0.366375,3.765315,-2.395602,9.971297,2.081182,-2.492939,-9.731549,-2.214867,2.349579,6.457102,6.770690,9.025249,2.722685,6.400692,-0.061540,2.484019,-6.874663,-2.949074,3.479691,6.405909,-4.741277,-7.152962,-7.321051,-4.306482,-7.439043,7.387179,3.931101,8.747838,2.144770,9.590155,4.616799,4.908582,5.121976,-7.592800,7.789137,-0.012734,4.460760,3.236033,2.288769,6.823682,7.790650,-2.368114,7.886895], dtype = "float32")#candidate|9467|(770,)|const|float32
call_9465 = relay.TupleGetItem(func_1756_call(relay.reshape(var_9466.astype('float32'), [336,]), relay.reshape(const_9467.astype('float32'), [11, 14, 5]), ), 1)
call_9468 = relay.TupleGetItem(func_1760_call(relay.reshape(var_9466.astype('float32'), [336,]), relay.reshape(const_9467.astype('float32'), [11, 14, 5]), ), 1)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_9469 = relay.TupleGetItem(func_2043_call(), 0)
call_9470 = relay.TupleGetItem(func_2044_call(), 0)
output = relay.Tuple([call_9461,call_9465,var_9466,const_9467,call_9469,])
output2 = relay.Tuple([call_9462,call_9468,var_9466,const_9467,call_9470,])
func_9492 = relay.Function([var_9466,], output)
mod['func_9492'] = func_9492
mod = relay.transform.InferType()(mod)
mutated_mod['func_9492'] = func_9492
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9493 = relay.var("var_9493", dtype = "float32", shape = (336,))#candidate|9493|(336,)|var|float32
func_9492_call = mutated_mod.get_global_var('func_9492')
call_9494 = func_9492_call(var_9493)
output = call_9494
func_9495 = relay.Function([var_9493], output)
mutated_mod['func_9495'] = func_9495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3932_call = mod.get_global_var('func_3932')
func_3933_call = mutated_mod.get_global_var('func_3933')
call_9536 = relay.TupleGetItem(func_3932_call(), 0)
call_9537 = relay.TupleGetItem(func_3933_call(), 0)
output = call_9536
output2 = call_9537
func_9564 = relay.Function([], output)
mod['func_9564'] = func_9564
mod = relay.transform.InferType()(mod)
mutated_mod['func_9564'] = func_9564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9564_call = mutated_mod.get_global_var('func_9564')
call_9565 = func_9564_call()
output = call_9565
func_9566 = relay.Function([], output)
mutated_mod['func_9566'] = func_9566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_9607 = func_1716_call()
call_9608 = func_1716_call()
func_7077_call = mod.get_global_var('func_7077')
func_7080_call = mutated_mod.get_global_var('func_7080')
const_9615 = relay.const([[-5,-10,4,6,-7,-1,-3,6,-4,-5,-6,10,-8,9,-2,-6,3,5,-4,-5,-5,-5,-5,4,-4,6,7,-4],[-2,8,-1,10,-10,1,-5,-2,3,9,-8,7,5,4,3,6,10,-9,10,-6,6,2,-2,-2,-4,4,7,6]], dtype = "int8")#candidate|9615|(2, 28)|const|int8
call_9614 = relay.TupleGetItem(func_7077_call(relay.reshape(const_9615.astype('int8'), [56,])), 3)
call_9616 = relay.TupleGetItem(func_7080_call(relay.reshape(const_9615.astype('int8'), [56,])), 3)
func_1602_call = mod.get_global_var('func_1602')
func_1605_call = mutated_mod.get_global_var('func_1605')
call_9630 = relay.TupleGetItem(func_1602_call(relay.reshape(const_9615.astype('int8'), [1, 7, 8])), 1)
call_9631 = relay.TupleGetItem(func_1605_call(relay.reshape(const_9615.astype('int8'), [1, 7, 8])), 1)
uop_9646 = relay.log2(call_9614.astype('float32')) # shape=(11, 15, 3)
uop_9648 = relay.log2(call_9616.astype('float32')) # shape=(11, 15, 3)
uop_9659 = relay.tan(uop_9646.astype('float64')) # shape=(11, 15, 3)
uop_9661 = relay.tan(uop_9648.astype('float64')) # shape=(11, 15, 3)
bop_9666 = relay.divide(uop_9646.astype('float32'), relay.reshape(uop_9659.astype('float32'), relay.shape_of(uop_9646))) # shape=(11, 15, 3)
bop_9669 = relay.divide(uop_9648.astype('float32'), relay.reshape(uop_9661.astype('float32'), relay.shape_of(uop_9648))) # shape=(11, 15, 3)
func_4863_call = mod.get_global_var('func_4863')
func_4865_call = mutated_mod.get_global_var('func_4865')
call_9672 = relay.TupleGetItem(func_4863_call(), 5)
call_9673 = relay.TupleGetItem(func_4865_call(), 5)
func_8277_call = mod.get_global_var('func_8277')
func_8278_call = mutated_mod.get_global_var('func_8278')
call_9676 = relay.TupleGetItem(func_8277_call(), 0)
call_9677 = relay.TupleGetItem(func_8278_call(), 0)
output = relay.Tuple([call_9607,const_9615,call_9630,bop_9666,call_9672,call_9676,])
output2 = relay.Tuple([call_9608,const_9615,call_9631,bop_9669,call_9673,call_9677,])
func_9678 = relay.Function([], output)
mod['func_9678'] = func_9678
mod = relay.transform.InferType()(mod)
mutated_mod['func_9678'] = func_9678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9678_call = mutated_mod.get_global_var('func_9678')
call_9679 = func_9678_call()
output = call_9679
func_9680 = relay.Function([], output)
mutated_mod['func_9680'] = func_9680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4391_call = mod.get_global_var('func_4391')
func_4392_call = mutated_mod.get_global_var('func_4392')
call_9707 = func_4391_call()
call_9708 = func_4391_call()
func_6386_call = mod.get_global_var('func_6386')
func_6389_call = mutated_mod.get_global_var('func_6389')
var_9727 = relay.var("var_9727", dtype = "int16", shape = (252,))#candidate|9727|(252,)|var|int16
call_9726 = relay.TupleGetItem(func_6386_call(relay.reshape(var_9727.astype('int16'), [2, 9, 14])), 0)
call_9728 = relay.TupleGetItem(func_6389_call(relay.reshape(var_9727.astype('int16'), [2, 9, 14])), 0)
output = relay.Tuple([call_9707,call_9726,var_9727,])
output2 = relay.Tuple([call_9708,call_9728,var_9727,])
func_9734 = relay.Function([var_9727,], output)
mod['func_9734'] = func_9734
mod = relay.transform.InferType()(mod)
mutated_mod['func_9734'] = func_9734
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9735 = relay.var("var_9735", dtype = "int16", shape = (252,))#candidate|9735|(252,)|var|int16
func_9734_call = mutated_mod.get_global_var('func_9734')
call_9736 = func_9734_call(var_9735)
output = call_9736
func_9737 = relay.Function([var_9735], output)
mutated_mod['func_9737'] = func_9737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3932_call = mod.get_global_var('func_3932')
func_3933_call = mutated_mod.get_global_var('func_3933')
call_9745 = relay.TupleGetItem(func_3932_call(), 0)
call_9746 = relay.TupleGetItem(func_3933_call(), 0)
output = relay.Tuple([call_9745,])
output2 = relay.Tuple([call_9746,])
func_9770 = relay.Function([], output)
mod['func_9770'] = func_9770
mod = relay.transform.InferType()(mod)
mutated_mod['func_9770'] = func_9770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9770_call = mutated_mod.get_global_var('func_9770')
call_9771 = func_9770_call()
output = call_9771
func_9772 = relay.Function([], output)
mutated_mod['func_9772'] = func_9772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5400_call = mod.get_global_var('func_5400')
func_5402_call = mutated_mod.get_global_var('func_5402')
call_9785 = relay.TupleGetItem(func_5400_call(), 0)
call_9786 = relay.TupleGetItem(func_5402_call(), 0)
output = call_9785
output2 = call_9786
func_9789 = relay.Function([], output)
mod['func_9789'] = func_9789
mod = relay.transform.InferType()(mod)
output = func_9789()
func_9790 = relay.Function([], output)
mutated_mod['func_9790'] = func_9790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3160_call = mod.get_global_var('func_3160')
func_3161_call = mutated_mod.get_global_var('func_3161')
call_9820 = func_3160_call()
call_9821 = func_3160_call()
func_8913_call = mod.get_global_var('func_8913')
func_8915_call = mutated_mod.get_global_var('func_8915')
const_9829 = relay.const([6,-8,-5,-10,7,-3,5,9,2,6,-3,-3,-7,-8,3,-4,1,-5,-10,9,4,-4,7,5,-7,-1,8,-1,-5,8,6,6,-1,-8,-5,10,-8,-10,-2,-6,-6,1,1,10,5,-3,-7,10,9,3,-4,5,9,-9,-2,10,-2,-1,5,8,-9,-10,-1,8,-10,-5,-4,-8,-10,2,10,8,-2,-4,2,8,-4,-2,3,-4,-1,-7,3,-5,-2,3,-10,-3,-1,1,10,7,-2,-8,8,-7,-5,3,-10,1,7,6,-6,-10,-6,10,-4,2,7,8,4,-2,10,6,-6,-5,-8,10,10,1,-5,-3,-10,-5,-5,-2,-10,7,-2,1,-8,10,-7,-10,-2,-2,3,-8,-8,-2,5,1,10,5,-1,-7,5,4,10,7,-8,1,-2,-6,1,7,-4,1,-6,-6,-7,5,2,3,5,4,-9,-7,-3,5,-3,-9,-1,-2,1,6,-1,-9,2,5,-2,-3,5,1,-2,-3,9,1,6,-6,1,6,-1,-5,9,-2,-2,-1,2,-6,-10,-9,-2,-6,-6,-7,2,-9,8,-8,5,-7,5,-3,-4,1,-9,-3,-1,-1,-3,3,10,2,5,7,10,-4,-4,1,-5,3,3,5,7,2,-4,7,7,4,-9,-2,4,5,-5,7,-1,4,-8,-9,-6,-5,7,4,1,-8,8,-9,-7,2,1,2,2,5,6,5,6,-2,-3,-1,-4,-3,10,-7,-6,-1,-10,8,-8,4,-8,7,10,-1,6,5,10,4,-10,6,-10,5,-9,-2,8,4,4,2,-1,-6,4,6,-1,-1,-1,-9,6,-1,-4,4,10,10,7,9,-6,4,-8,1,3,10,-2,7,2,-3,-2,10,2,7,3,-9,4,-8,-6,-2,2,-6,-3,-2,-10,1,9,3,3,-5,9,5,7,-4,2,-5,1,9,-2,-9,6,-2,5,-8,-9,-5,5,10,3,7,1,10,-3,6,-1,-8,8,10,7,-10,-1,3,-4,9,8,-5,-10,-10,5,8,2,-1,-6,-4,10,-1,8,8,6,3,5,-2,-10,-10,10,-1,4,5,-2,4,2,3,-9,5,-10,1,4,-2,6,1,2,10,-1,-7,-3,-7,8,4,10,-5,6,6,9,-6,2,3,-7,-1,10,-3,10,-8,9,8,-1,-2,10,7,-7,-6,-10,2,-4,8,-2,-8,1,3,-6,-1,-5,-6,-2,6,-7,8,-1,-5,-7,2,-3,2,-4,6,-9,9,-10,10,-7,1,9,1,4,-7,-8,10,9,7,-10,-5,10,2,-10,-1,-1,3,4,9,2,8,-7,3,-2,-1,-3,-1,2,-2,8,-3,8,8,-2,1,-5,3,-9,7,-9,4,-5,-7,-8,3,-4,6,2,5,3,7,-7,9,9,7,-4,-1,8,10,-7,-6,9,3,6,-7,-4,-6,-9,6,10,-5,6,5,-4,-2,10,-1,9,-2,4,3,-8,-6,3,4,-5,10,-6,7,-2,10,6,10,-9,-2,4,8,6,8,8,-5,-10,6,9,-6,4,-10,-9,-10,3,-1,7,8,7,-5,7,-10,2,-2,1,2,6,-10,4,-5,-1,-7,-6,-4,-10,-8,8,3,5,-2,5,-6,8,8,-7,3,9,-8,5,-10,10,2,-7,7,2,8,3,-10,1,5,3,6,5,9,-4,5,-8,-2,-1,6,-8,3,-10,4,-5,9,-6,1,7,-1,10,6,4,2,-9,-1,5,-2,-8,-6,5,2,10,-3,5,9,2,5,7,1,6,-7,-5,7,3,-8,-1,-10,-6,-10,-6,6,8,4,-9,-1,7,7,7,5,9,8,4,3,-10,-10,-3,6,10,-7,7,3,6,-5,-5,-2,-6,6,-10,-1,-3,-9,-9,-10,-9,7,4,9,3,-4,-8,5,-9,-7,4,-9,1,5,-7,1,3,1,10,-9,5,1,10,-9,-9,-7,-6,-9,-6,-9,1,-8,-9,-4,-8,2,-8,9,9,6,6,-10,-10,9,5,-1,-7,-3,-6,5,-1,1,2,-7,10,10,7,-10,10,2,-7,-2,-2,1,1,3,-3,-1,-4,7,-2,-4,6,5,-1,-9,-10,3,5,1,1,8,-8,-10,-7,-10,1,-9,8,-5,1,-9,7,4,-7,-10,8,-2,-6,1,-7,-6,7,-9,9,3,-8,-10,4,6,8,-8,3,3,2,5,-6,-2,-6,7,-3,-5,3,-5,-9,6,7,4,-6,9,2,7,-7,-3,10,-10,10,-3,1,8,8,-7,-2,5,7,-5,-10,-7,1,-1,9,3,5,2,5,5,-8,8,-5,-5,9,-9,4,5,5,-8,7,6,9,-9,-8,8,9,5,3,6,1,8,-1,-1,-10,3,-10,1,-6,6,7,9,1,9,3,-5,-1,8,-7,2,-7,7,3,9,-8,-3,-8,-10,8,5,7,6,5,1,6,-1,10,10,-6,3,3,-7,-2,-10,-8,-2,4,-2,5,-3,9,-3,2,2,-4,1,5,-6,5,-5,-2,-8,6,-5,5,1,-2,3,-8,1,2,-9,10,-3,-3,9,-7,10,-9,4,3,-8,-10,8,-9,-1,-2,9,-6,-10,1,2,8,-1,9,3,-3,-8,3,2,-8,5,3,-2,6,-6,3,7,2,-8,-5,6,3,10,1,-8,-7,8,6,-9,-4,-9,4,8,-4,-8,9,-7,-7,8,1,8,-10,-9,6,9,4,-7,-6,4,-3,-10,-6,3,-4,-3,9,-4,-6,7,5,-6,-6,7,7,-3,-6,3,10,7,-8,-10,10,8,-10,-9,-1,-2,-7,-2,-2,7,9,-2,-7,-4,7,-4,9,2,8,-4,8,9,-7,-2,-5,-1,-10,-5,1,-3,-5,-7,10,-6,3,-9,-8,-6,7,-7,8,1,10,6,7,-2,-8,-7,-8,-9,4,4,4,8,2,8,-3,10,4,7,-5,2,-7,4,-5,-10,10,-1,-6,10,4,7,-4,3,3,7,-8,-3,-1,4,-1,5,10,10,4,-3,-7,-6,-9,8,8,2,-8,4,-2,-5,3,-6,3,9,5,8,6,10,-4,9,-6,9,-6,3,-1,10,-6,7,2,1,-9,7,2,3,8,7,3,-7,-8,4,9,-3,2,-8,-5,-2,-5,-2,-8,2,-8,-1,-8,-7,-9,8,-9,-6,-1,7,-1,-4,10,5], dtype = "uint8")#candidate|9829|(1200,)|const|uint8
call_9828 = relay.TupleGetItem(func_8913_call(relay.reshape(const_9829.astype('uint8'), [1200,])), 2)
call_9830 = relay.TupleGetItem(func_8915_call(relay.reshape(const_9829.astype('uint8'), [1200,])), 2)
func_7147_call = mod.get_global_var('func_7147')
func_7149_call = mutated_mod.get_global_var('func_7149')
call_9835 = func_7147_call()
call_9836 = func_7147_call()
output = relay.Tuple([call_9820,call_9828,const_9829,call_9835,])
output2 = relay.Tuple([call_9821,call_9830,const_9829,call_9836,])
func_9876 = relay.Function([], output)
mod['func_9876'] = func_9876
mod = relay.transform.InferType()(mod)
mutated_mod['func_9876'] = func_9876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9876_call = mutated_mod.get_global_var('func_9876')
call_9877 = func_9876_call()
output = call_9877
func_9878 = relay.Function([], output)
mutated_mod['func_9878'] = func_9878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9770_call = mod.get_global_var('func_9770')
func_9772_call = mutated_mod.get_global_var('func_9772')
call_9888 = relay.TupleGetItem(func_9770_call(), 0)
call_9889 = relay.TupleGetItem(func_9772_call(), 0)
output = relay.Tuple([call_9888,])
output2 = relay.Tuple([call_9889,])
func_9891 = relay.Function([], output)
mod['func_9891'] = func_9891
mod = relay.transform.InferType()(mod)
mutated_mod['func_9891'] = func_9891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9891_call = mutated_mod.get_global_var('func_9891')
call_9892 = func_9891_call()
output = call_9892
func_9893 = relay.Function([], output)
mutated_mod['func_9893'] = func_9893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4682_call = mod.get_global_var('func_4682')
func_4684_call = mutated_mod.get_global_var('func_4684')
call_9906 = func_4682_call()
call_9907 = func_4682_call()
func_4939_call = mod.get_global_var('func_4939')
func_4941_call = mutated_mod.get_global_var('func_4941')
var_9923 = relay.var("var_9923", dtype = "float64", shape = (20, 1))#candidate|9923|(20, 1)|var|float64
call_9922 = relay.TupleGetItem(func_4939_call(relay.reshape(var_9923.astype('float64'), [20,])), 1)
call_9924 = relay.TupleGetItem(func_4941_call(relay.reshape(var_9923.astype('float64'), [20,])), 1)
func_1981_call = mod.get_global_var('func_1981')
func_1985_call = mutated_mod.get_global_var('func_1985')
const_9933 = relay.const([0.614179,-0.474534,-7.574168,-9.143431,-5.962111,0.412790,-9.499258,-7.006143,6.308397,3.329870,8.977436,-5.701887,-5.559408,6.206077,-5.247235,-7.874880,4.849829,0.600805,-4.915359,5.037066,-4.029460,0.813000,2.389176,-1.219088,2.511033,-2.851899,-5.650694,-9.540058,4.395091,-5.560291,1.615565,-9.339242,2.683943,-1.742287,7.123566,8.077378,-9.925688,-2.423382,-8.724631,-9.963840,5.579047,-4.678871,1.962605,-7.740872,-3.186123,5.300892,6.710593,-8.725639,8.443857,-3.758856,8.729286,2.517761,6.030594,9.805447,-2.768195,3.962840,-3.307763,-2.939826,2.973812,4.431704,8.618702,1.759460,-2.712974,-5.114024,-5.717858,-6.832815,-9.550418,9.381095,-9.889324,8.802841,-7.967320,-0.574266,-7.643652,9.104807,4.041163,-1.529590,6.802579,2.569564,6.105827,1.103019,9.918225,3.115812,3.954178,4.387087,-7.003649,2.448819,5.507755,8.589712,-2.145355,7.348168,9.429771,-6.461543,2.911981,-1.351281,4.080038,-3.288270,-6.779725,-7.695985,-8.954845,6.812263,-0.349461,-6.516137,-6.661561,-3.032125,-0.638044,-8.041663,7.935325,-7.836931,-6.188753,6.503080,-8.472549,-1.140343,-6.752322,9.054166,-5.550651,7.997248,8.569162,2.639765,7.007412,-7.934661,0.387548,-8.837293,4.432947,-8.170799,3.069615,-0.863736,8.065267,-0.185418,4.185068,0.584804,-3.790185,0.714126,-1.543658,0.078728,-6.283716,0.953663,-1.931450,-0.421881,-9.331536,-7.246356,-4.102018,9.338710,4.575578,0.185040,8.737135,3.441232,9.291365,3.188060,5.938339,-0.870410,-8.143902,6.826144,0.073012,9.276250,-5.739339,7.927870,-4.972995,4.177795,9.389806,-9.941532,8.398768,-7.557224,-1.811392,-7.186073,8.098797,9.153823,-6.189314,-4.968547,-8.550731,6.357579,1.431227,-4.081379,2.882159,-7.545855,-3.666977,-0.961958,-0.351527,6.662410,-1.431833,-0.764953,-7.252957,-8.939703,-9.506004,-1.883693,-2.152265,-3.304523,-0.716309,6.117944,-1.122388,-9.029031,-5.184672,-3.472084,-1.733689,-6.903164,5.636983,-8.745796,-3.972031,-8.173010,5.278673,-7.175955,-7.743960,-3.148834,5.405259,-7.093905,8.567709,-3.252383,4.108207,-6.516638,-4.530506,7.295276,2.616027,5.686967,-6.340519,-8.050961,-1.185550,6.200008,7.738774,-4.638327,6.337814,-8.678818,2.475260,-9.422767,3.530461,-6.132333,1.490113,4.477855,8.032335,7.386225,-7.129099,-5.477783,-7.809762,2.647492,6.683188,-2.674753,9.408133,2.015681,5.719634,6.664369,-1.221427,1.591015,6.168064,-7.103125,4.400653,-1.388224,9.030489,2.192230,-9.761421,-9.040943,-2.916869,-7.472891,6.378264,-8.299487,-4.374905,-0.711335,-1.564014,-3.999921,-0.751125,-8.823605,-7.631910,-2.382876,7.898008,5.813440,-4.897396,6.044511,-0.596435,-4.050980,1.081924,5.975766,1.147019,-5.728288,6.823257,1.442042,0.142659,9.116762,8.053339,-4.915413,6.790175,-8.808465,9.528299,-2.401506,-4.083109,2.649700,-9.367586,8.215076,-9.163862,5.376563,-8.065351,-0.164952,-0.256857,-7.540803,4.422900,7.744989,-0.670115,-1.445801,7.003265,-2.899324,-4.096376,-6.479275,-6.578261,-9.455378,9.456291,-6.792434,-6.326631,-5.541255,-9.602745,-1.319179,0.014563,5.286935,-0.982431,1.274041,-6.164672,5.964768,2.516897,3.278575,6.794411,8.305260,7.207138,-9.515975,-8.148076,1.610547,7.623427,-5.289242,1.481614,0.858042,9.568388,0.469550,-5.048339,-7.012996,-0.053097,3.987904,3.758287,0.874681,-7.047802,0.139042,-2.590274,1.093677], dtype = "float32")#candidate|9933|(336,)|const|float32
call_9932 = relay.TupleGetItem(func_1981_call(relay.reshape(call_9906.astype('float32'), [11, 14, 5]), relay.reshape(const_9933.astype('float32'), [336,]), ), 4)
call_9934 = relay.TupleGetItem(func_1985_call(relay.reshape(call_9906.astype('float32'), [11, 14, 5]), relay.reshape(const_9933.astype('float32'), [336,]), ), 4)
func_5400_call = mod.get_global_var('func_5400')
func_5402_call = mutated_mod.get_global_var('func_5402')
call_9936 = relay.TupleGetItem(func_5400_call(), 0)
call_9937 = relay.TupleGetItem(func_5402_call(), 0)
bop_9948 = relay.divide(const_9933.astype('float32'), var_9923.astype('float32')) # shape=(20, 336)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
var_9955 = relay.var("var_9955", dtype = "float64", shape = (810,))#candidate|9955|(810,)|var|float64
call_9954 = relay.TupleGetItem(func_5092_call(relay.reshape(var_9955.astype('float64'), [6, 15, 9])), 0)
call_9956 = relay.TupleGetItem(func_5094_call(relay.reshape(var_9955.astype('float64'), [6, 15, 9])), 0)
output = relay.Tuple([call_9906,call_9922,call_9932,call_9936,bop_9948,call_9954,var_9955,])
output2 = relay.Tuple([call_9907,call_9924,call_9934,call_9937,bop_9948,call_9956,var_9955,])
func_9962 = relay.Function([var_9923,var_9955,], output)
mod['func_9962'] = func_9962
mod = relay.transform.InferType()(mod)
var_9963 = relay.var("var_9963", dtype = "float64", shape = (20, 1))#candidate|9963|(20, 1)|var|float64
var_9964 = relay.var("var_9964", dtype = "float64", shape = (810,))#candidate|9964|(810,)|var|float64
output = func_9962(var_9963,var_9964,)
func_9965 = relay.Function([var_9963,var_9964,], output)
mutated_mod['func_9965'] = func_9965
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10034 = relay.const([[[9.083988],[-4.317522],[3.652446],[-8.814306],[8.187117],[-4.204505],[1.197599],[3.838315],[2.019696],[7.542625],[-6.431855],[1.996376],[-7.884251],[-5.542029],[-6.217676],[6.124880]],[[6.736991],[-9.263569],[-7.150198],[1.044259],[-5.649771],[9.337452],[-9.752463],[-4.344068],[2.962424],[-4.271905],[4.052145],[-6.340107],[5.077508],[3.350696],[-9.728587],[-3.154013]],[[5.814284],[-7.994938],[8.285627],[8.277518],[3.172654],[6.191634],[6.237454],[-2.281717],[4.943192],[-7.091635],[-1.367748],[7.436886],[4.278262],[3.882290],[8.490863],[-5.634805]],[[-3.767106],[-1.063766],[-2.490602],[4.434372],[-1.303649],[5.789948],[-1.705963],[7.865793],[-4.214439],[-6.985825],[-7.395926],[-4.919965],[-9.566305],[3.716800],[6.886465],[-6.886346]],[[1.729466],[2.162498],[-3.975346],[2.040285],[-4.110883],[-6.290079],[-5.734478],[-1.721079],[-3.825011],[6.752272],[-9.090064],[-3.982658],[8.657536],[3.608318],[1.828687],[-1.808666]],[[-0.822058],[-9.439438],[-7.015297],[-9.252415],[-7.950628],[3.328802],[-4.092948],[9.813213],[-7.440982],[5.400179],[3.930876],[-3.838699],[6.879302],[0.478360],[4.615603],[1.648509]],[[-6.114024],[8.701969],[-0.575874],[9.852967],[-1.285821],[4.173665],[-1.145518],[9.352676],[-7.148103],[-0.215438],[3.590920],[-0.747018],[-4.025617],[9.593206],[-0.532964],[0.949455]],[[2.623618],[3.427013],[-9.238567],[-0.077400],[-8.557289],[3.649144],[6.039504],[2.931825],[4.992881],[3.506124],[-6.936106],[-4.301982],[5.127913],[8.462764],[-1.337345],[-6.966301]],[[1.689703],[9.081669],[-4.749215],[-7.546603],[-4.352209],[-5.568934],[9.631437],[8.113685],[5.583122],[4.101390],[-0.101170],[-7.909330],[3.445892],[6.704730],[-7.326943],[2.163592]]], dtype = "float64")#candidate|10034|(9, 16, 1)|const|float64
uop_10035 = relay.asinh(const_10034.astype('float64')) # shape=(9, 16, 1)
bop_10040 = relay.equal(const_10034.astype('bool'), relay.reshape(uop_10035.astype('bool'), relay.shape_of(const_10034))) # shape=(9, 16, 1)
bop_10053 = relay.minimum(uop_10035.astype('float64'), relay.reshape(bop_10040.astype('float64'), relay.shape_of(uop_10035))) # shape=(9, 16, 1)
output = relay.Tuple([bop_10053,])
output2 = relay.Tuple([bop_10053,])
func_10071 = relay.Function([], output)
mod['func_10071'] = func_10071
mod = relay.transform.InferType()(mod)
mutated_mod['func_10071'] = func_10071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10071_call = mutated_mod.get_global_var('func_10071')
call_10072 = func_10071_call()
output = call_10072
func_10073 = relay.Function([], output)
mutated_mod['func_10073'] = func_10073
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10095 = relay.var("var_10095", dtype = "float32", shape = (8, 16, 3))#candidate|10095|(8, 16, 3)|var|float32
const_10096 = relay.const([[[-4.083245,0.671388,1.829994],[-9.158955,6.111277,6.990780],[1.828211,0.591013,-4.539137],[-3.553979,5.833702,-6.872155],[-2.701362,6.074703,-0.878020],[-2.748521,6.333660,-9.265668],[3.244123,-2.095437,-1.008220],[-5.031981,1.634833,-8.687085],[0.412978,7.874357,8.622302],[-6.684437,1.936898,2.428267],[-4.772770,9.543561,2.643880],[8.482225,-2.624956,0.501446],[6.480516,-9.388698,0.679480],[-6.864099,8.517238,-2.912831],[9.532017,-0.665224,-8.138999],[-8.830457,-3.292124,-9.216636]],[[-4.443449,-2.744686,4.735912],[8.814694,4.937072,-4.526339],[-3.660264,6.122189,-0.706903],[3.527493,1.685465,-4.549824],[9.787578,-4.673608,-3.762511],[7.011902,-3.634196,4.986029],[8.145372,-9.112945,-7.774066],[2.208643,8.241143,-0.468829],[-9.250457,9.584095,-2.900199],[7.865542,2.167755,9.360399],[6.446249,-3.736280,-9.852320],[6.533475,-8.897479,-8.972722],[-4.522268,-7.620575,-3.309168],[7.272597,-6.231881,-8.959141],[0.163552,-5.574745,-9.651161],[-1.512642,-9.646078,5.169829]],[[2.719234,-9.447990,1.077225],[-6.551021,-2.915250,7.562715],[-1.163031,-6.417593,-8.093324],[8.851719,-4.026717,-2.666187],[6.536380,-9.372636,2.339464],[-6.032205,3.544166,-4.083203],[4.405688,-3.752784,8.464106],[-2.847547,1.534578,-5.305277],[-1.235142,2.668609,8.042101],[2.726141,-3.956748,-7.265717],[2.480197,-7.919181,8.261170],[7.366169,-3.200066,8.889781],[-7.660960,0.171473,-4.012450],[7.110768,2.969132,0.429885],[-1.606598,4.473599,8.073880],[-5.082567,-4.396653,2.973392]],[[2.390512,-3.014753,-6.722010],[-8.849323,6.980635,-7.926974],[2.040280,-1.740745,-1.322935],[-0.310286,-8.420713,-4.358456],[9.384291,9.527272,9.867363],[-7.566360,1.713504,-9.020512],[-3.505659,-8.929767,-3.502853],[7.234744,-2.693735,-4.687972],[0.505082,6.173831,-4.583163],[7.924292,-7.843297,3.488614],[9.066372,7.666863,-1.179054],[6.908104,-9.234541,2.010056],[-2.306478,-1.274560,-7.153136],[-2.092305,6.619147,-9.629814],[7.803781,-4.397097,-3.325869],[2.401942,5.989259,-1.571880]],[[8.722414,-4.661089,-8.026642],[-9.894617,-9.240040,6.748821],[-5.650841,-3.224208,-2.064774],[4.770871,8.859152,2.274733],[-3.060989,8.014392,0.131496],[1.592371,3.621654,-0.661840],[9.607601,2.666441,-7.799635],[1.807711,-3.608941,-4.288048],[-8.115621,-4.497148,2.950496],[8.800272,-9.892289,8.665872],[-8.261285,-9.936932,-0.751294],[1.721850,-3.484175,3.130246],[-0.754908,6.324495,1.019464],[9.128888,2.045212,7.270266],[6.473001,-4.320727,4.928726],[-1.619649,7.263198,-7.326617]],[[5.503447,7.783054,-4.396316],[-6.460754,2.651301,8.679757],[-8.868089,-0.781742,-1.721246],[-0.036681,-5.041698,7.068807],[7.989374,-7.933259,3.298262],[-2.691993,-2.997224,-4.427098],[2.779242,7.494793,-7.677799],[8.715555,9.011046,-4.812772],[7.269405,-8.221535,-5.083809],[4.864894,9.032635,-7.171307],[-1.020716,2.315466,-6.852382],[4.117185,6.141577,6.098446],[5.403902,-0.621076,-4.497029],[-4.876378,4.229036,-6.682088],[5.880824,1.159784,5.681705],[2.325651,6.270880,-3.438295]],[[-5.114711,1.055623,9.434788],[3.929719,5.421089,3.513636],[-1.797278,5.531037,-6.782159],[1.393797,5.325745,-5.140617],[-2.689587,6.117936,9.690061],[-8.377145,8.485802,4.591331],[-4.494489,-4.931555,-7.027998],[3.693153,0.980497,-0.292901],[-6.695583,8.152962,3.676509],[-8.241689,0.939429,1.219729],[-2.001907,-6.726349,6.977393],[-5.058860,-6.171753,1.896295],[-9.346598,-9.647407,1.749008],[-7.828754,-6.653997,6.875411],[7.191810,-5.154126,4.676077],[3.564874,4.819986,-8.501673]],[[0.025614,-3.777114,7.206455],[-2.158756,-6.079444,6.545109],[-2.650029,-6.397524,-5.943684],[-2.012117,7.368302,-0.665197],[-7.215293,-9.197518,-0.222465],[-4.142093,8.038223,5.871270],[-2.405423,5.712151,-0.826009],[-3.377735,-7.621024,-4.825693],[-2.134097,-4.967294,1.259707],[6.871504,8.611515,0.381801],[-5.804165,0.647204,-2.540103],[-5.655460,8.009080,8.246226],[-6.306184,-4.372522,-3.250389],[6.263089,5.005269,9.540168],[2.423754,-2.424400,-2.814093],[-2.342006,7.309652,3.032813]]], dtype = "float32")#candidate|10096|(8, 16, 3)|const|float32
bop_10097 = relay.divide(var_10095.astype('float32'), relay.reshape(const_10096.astype('float32'), relay.shape_of(var_10095))) # shape=(8, 16, 3)
func_8682_call = mod.get_global_var('func_8682')
func_8684_call = mutated_mod.get_global_var('func_8684')
call_10103 = func_8682_call()
call_10104 = func_8682_call()
func_5240_call = mod.get_global_var('func_5240')
func_5245_call = mutated_mod.get_global_var('func_5245')
const_10110 = relay.const([-2.365767,4.095566,-2.120933,-1.126232,-6.543911,8.888838,-6.316304,0.826588,-0.060209,7.230838,9.996695,2.916837,-8.797903,2.345860,-2.289552,-8.675043,-7.648986,5.171087,-9.577441,2.377853,8.643349,-3.046396,1.923486,-7.646757,0.868610,6.846995,9.259033,-2.533267,1.520459,7.277661,3.945292,-1.086859,-9.272349,-3.109525,4.999283,3.092246,-0.691022,-1.740843,-8.429223,-3.659225,-1.451883,-1.628547,-7.217701,-6.428796,3.706930,-2.950596,9.520579,-1.557569,-6.949192,-0.729448,9.177130,-0.145175,-7.987229,4.032888,9.075657,-8.851273,-4.057203,-1.424630,-4.307807,-5.005008,-1.611914,-2.564405,1.188341,8.501695,-8.424626,3.940855,-8.984628,2.396726,2.984087,4.788228,-4.286110,-2.650548,-4.523819,-1.419691,4.980762,-1.866445,2.997403,4.846289,-1.633384,-2.551151,5.478065,-2.591072,7.118373,-7.440898,-5.255851,-7.524209,1.342842,2.142179,8.438369,-1.643866,-0.196962,-7.591563,-0.561091,-0.379366,3.071293,8.055715,5.495985,-7.295635,0.043388,3.257442,-4.268668,9.540331,-5.629557,7.183120,-3.190747,3.054671,6.035758,-8.654746,3.387453,-4.363356,8.268180,8.213435,4.202171,5.360695,-3.008611,-6.543752,-4.325333,5.453888,9.364214,-5.728441,-6.644562,-9.725874,-2.210772,8.119193,-5.318033,-4.498315,9.106460,-2.963777,3.233861,-3.474291,-6.733462,-6.734552,-7.490393,3.281111,-4.286089,4.172210,8.530336,-7.629974,-0.270227,-6.405838,7.469852,-2.025925,-9.087483,1.938888,-5.478087,-1.850825,6.161543,-2.797067,-9.637306,4.959852,7.385358,2.782954,-5.375043,-9.368646,-8.346388,9.396903,6.591568,-5.787793,-2.565958,8.566040,4.441458,7.830738,-9.911261,-3.087716,-0.317011,-1.982063,-2.048723,-7.397093,4.652317,6.208102,9.235809,-4.767333,-5.319200,9.363560,-0.883732,-7.804075,-1.009174,-1.902131,2.065602,5.620531,-1.763196,6.103080,0.876087,-7.370299,9.734319,-1.436149,-4.554628,5.769859,-1.450919,-2.340602,-0.861025,-2.706583,-5.631555,7.789007,-2.869201,1.653613,-6.194616,0.178558,6.502164,3.691462,-6.269605,3.372934,-7.725500,6.021681,4.185334,8.587196,-7.061213,-0.485378,9.763938,-8.245206,-0.139996,-2.489873,5.697359,9.711343,4.448525,3.169122,-8.740551,3.093027,0.727857,1.944358,-9.728324,-1.045421,3.431861,2.950791,9.456200,-8.936810,-7.733455,-1.186187,-8.419301,-7.726176,-0.521135,1.351124,-5.543984,6.498623,-0.922483,7.320522,-9.267130,1.216741,-8.649812,-7.894752,3.557260,-4.618468,0.713862,0.784988,-5.903605,-7.185223,0.858898,8.917921,-1.466967,2.112142,-6.275438,5.266492,1.785897,-6.400414,3.347001,5.210154,0.764428,-3.793971,-3.067894,-6.329282,3.159130,-9.376108,0.953344,3.317303,-8.821720,-9.823334,5.368501,1.910929,-2.580933,-6.010279,-9.550380,-5.268512,2.000391,7.352444,-4.924471,-8.474593,-4.494569,-7.185053,9.856978,9.000370,4.968905,-4.974876,8.989488,6.632957,3.302668,2.032787,1.506022,1.020335,3.930365,-4.907793,-4.740323,1.079522,7.071024,-8.784040,1.168728,5.580899,4.314408,1.510699,4.684447,1.048882,0.398263,7.308807,-1.545670,0.429836,9.433708,-3.004926,7.329610,-3.595520,4.048297,5.943087,-7.975734,8.916679,-4.310741,-4.239701,9.054106,-7.078369,-2.881385,1.745633,-1.054561,-4.718655,6.089989,1.218241,3.753094,4.737985,7.032777,7.351627,6.200643,5.874142,-7.582692,-8.825630,0.460659,-3.743170,-5.049617,9.294533,-0.062299,-2.707493], dtype = "float32")#candidate|10110|(336,)|const|float32
var_10111 = relay.var("var_10111", dtype = "uint32", shape = (220,))#candidate|10111|(220,)|var|uint32
call_10109 = relay.TupleGetItem(func_5240_call(relay.reshape(const_10110.astype('float32'), [336,]), relay.reshape(call_10103.astype('float32'), [770,]), relay.reshape(var_10111.astype('uint32'), [220,]), ), 1)
call_10112 = relay.TupleGetItem(func_5245_call(relay.reshape(const_10110.astype('float32'), [336,]), relay.reshape(call_10103.astype('float32'), [770,]), relay.reshape(var_10111.astype('uint32'), [220,]), ), 1)
bop_10113 = relay.multiply(const_10096.astype('float32'), relay.reshape(var_10095.astype('float32'), relay.shape_of(const_10096))) # shape=(8, 16, 3)
output = relay.Tuple([bop_10097,call_10103,call_10109,const_10110,var_10111,bop_10113,])
output2 = relay.Tuple([bop_10097,call_10104,call_10112,const_10110,var_10111,bop_10113,])
func_10121 = relay.Function([var_10095,var_10111,], output)
mod['func_10121'] = func_10121
mod = relay.transform.InferType()(mod)
mutated_mod['func_10121'] = func_10121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10121_call = mutated_mod.get_global_var('func_10121')
var_10123 = relay.var("var_10123", dtype = "float32", shape = (8, 16, 3))#candidate|10123|(8, 16, 3)|var|float32
var_10124 = relay.var("var_10124", dtype = "uint32", shape = (220,))#candidate|10124|(220,)|var|uint32
call_10122 = func_10121_call(var_10123,var_10124,)
output = call_10122
func_10125 = relay.Function([var_10123,var_10124,], output)
mutated_mod['func_10125'] = func_10125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_10157 = relay.TupleGetItem(func_2043_call(), 0)
call_10158 = relay.TupleGetItem(func_2044_call(), 0)
output = relay.Tuple([call_10157,])
output2 = relay.Tuple([call_10158,])
func_10185 = relay.Function([], output)
mod['func_10185'] = func_10185
mod = relay.transform.InferType()(mod)
mutated_mod['func_10185'] = func_10185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10185_call = mutated_mod.get_global_var('func_10185')
call_10186 = func_10185_call()
output = call_10186
func_10187 = relay.Function([], output)
mutated_mod['func_10187'] = func_10187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4576_call = mod.get_global_var('func_4576')
func_4578_call = mutated_mod.get_global_var('func_4578')
call_10296 = func_4576_call()
call_10297 = func_4576_call()
func_4619_call = mod.get_global_var('func_4619')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_10319 = func_4619_call()
call_10320 = func_4619_call()
func_9770_call = mod.get_global_var('func_9770')
func_9772_call = mutated_mod.get_global_var('func_9772')
call_10323 = relay.TupleGetItem(func_9770_call(), 0)
call_10324 = relay.TupleGetItem(func_9772_call(), 0)
func_5945_call = mod.get_global_var('func_5945')
func_5948_call = mutated_mod.get_global_var('func_5948')
var_10329 = relay.var("var_10329", dtype = "float32", shape = (1260,))#candidate|10329|(1260,)|var|float32
const_10330 = relay.const([-10,-10,1,-8,-3,9,-9,-4,-3,-9,-2,-5,-3,-10,-9,-8,9,5,-4,-1,9,4,-2,-4,9,-8,-6,-3,2,-8,2,9,4,5,6,6,-6,7,1,5,-3,-2,-7,-7,-10,-1,1,-8,-5,6,9,-1,4,-4,-7,6,1,-8,3,-1,-10,-9,-4,7,-10,-3,7,-5,-1,-6,8,-8,-10,-1,-2,9,-5,-3,7,-10,-5,7,8,2,1,-8,2,9,-2,6,-3,6,-5,-8,-2,-9,-5,8,-8,-5,-8,9,-8,-1,-9,4,6,-9,-2,-3,-7,-9,9,-8,-6,6,-3,-4,-3,3,4,3,9,10,1,6,-6,-2,2,9,-10,-4,10,-6,-4,5,6,9,2,-9,-3,-2,-9,3,4,-3,-7,-9,-6,-9,4,10,2,7,9,6,10,10,-2,-3,4,-1,3,-9,-5,-9,10,8,1,5,-1,1,-1,-3,5,-9,1,10,-2,-1,7,7,-1,9,-2,1,7,7,4,-1,5,8,2,8,-8,10,-2,3,1,7,-8,7,2,-5,3,5,-6,1,-2,-1,-1,4,-9,7,8,-5,2,-4,-7,1,5,-9,-1,-10,-1,-3,-3,4,-5,5,-4,-4,4,9,6,-3,-7,3,-3,3,3,6,7,1,-10,-9,-7,-1,10,-2,1,9,-6,-8,-5,-2,-8,-8,8,-7,6,-5,7,-3,7,3,-1,-5,-5,7,-3,2,-7,6,-10,6,-9,10,-6,-4,10,-2,-2,-9,2,-10,-5,8,-1,-5,-7,6,1,-3,10,-1,-7,-3,-2,9,-8,-8,-9,5,1,10,3,6,-3,3,8,-6,-9,-5,9,2,1,2,-8,-10,7,7,-10,-3,1,8,10,-4,1,9,-3,9,2,-6,6,-7,9,-2,6,2,1,-7,-4,-1,10,6,10,-7,-7,-1,10,8,4,8,5,-9,2,9,-7,-2,8,-8,5,1,10,-9,-1,-10,6,9,8,10,-4,-7,-7,5,8,6,-1,-7,8,-1,-4,-4,-1,-4,10,10,-2,4,5,-9,-3,8,1,-4,3,5,-8,-8,3,7,-5,-7,3,10,-1,3,-3,9,-6,2,2,-5,-8,9,-4,-3,3,-9,3,6,-8,9,8,7,5,-3,7,-7,-10,4,-3,6,9,4,-5,-8,-9,-6,7,3,3,8,6,2,-2,-2,5,2,-3,8,9,1,-2,-9,10,-2,-9,-2,-8,3,-1,6,4,2,8,-3,3,-7,1,-4,9,4,8,5,10,-5,-2,9,-1,-3,-10,-6,-2,-7,-10,-6,7,-6,-7,1,6,2,-7,6,-1,-6,7,3,-4,2,3,10,-9,-7,7,4,3,5,-7,9,10,-1,5,8,-8,3,10,1,2,-4,5,-4,5,10,2,2,-3,1,-8,-9,-9,8,-8,9,-9,10,-2,-4,-6,9,-4,-10,-3,-6,9,-7,-8,8,-6,-5,-1,-10,-9,-7,1,-1,-4,-3,-1,10,-6,8,4,9,6,-6,9,7,-2,-3,10,-9,4,-5,-3,-6,-2,3,4,-5,-6,-5,-6,-2,-7,-1,-8,5,-4,-8,-3,-6,-9,-10,-10,3,-5,10,-1,10,-7,6,1,7,2,-2,2,-2,4,-5,-7,2,-7,5,-5,5,-6,-7,-4,4,-2,3,-4,-6,-6,-5,-9,9,7,1,9,-6,-1,-5,9,-1,6,6,10,10,-3,1,10,-8,-3,3,-9,8,1,-4,-3,-5,10,10,-5,6,-5,-2,6,-6,-10,-3,-7,6,-4,-10,5,9,9,5,-2,-2,9,-6,3,-6,-8,-10,9,4,-6,4,2,-9,3,-6,7,3,-1,5,-10,7,-1,4,-4,-5,5,-4,-3,9,-8,-2,-3,3,4,10,-8,-2,5,-8,6,-1,-5,7,7,3,-3,2,-1,-1,-2,9,-9,10,-8,-3,4,-5,-9,8,-10,-3,7,10,10,-3,2,4,-4,5,3,-8,2,-7,-6,6,5,1,-7,-9,2,-1,5,-8,-2,-3,-3,-3,4,5,-4,-10,-2,-2,-3,6,-5,4,4,9,6,-10,-4,-3,4,2,1,-10,4,2,5,5,-6,-9,10,6,-1,7,3,6,10,-7,2,3,-1,3,4,-5,-8,3,-2,6,-7,-1,-2,8,-6,2,4,4,-2,-1,-7,-1,3,-3,-2,10,-3,-2,7,9,-6,-1,-6,-8,-2,-9,7,5,3,-7,-8,-6,8,-6,-9,10,5,6,6,4,-2,8,2,-1,1,9,5,-2,3,-1,2,8,5,-3,-7,-1,-9,-8,2,3,7,7,-7,-6,7,-5,-9,8,-6,-4,-9,3,4,6,-3,3,1,2,7,10,-5,4,-9,-7,5,-9,-6,10,-6,-10,-7,8,3,8,10,-5,-5,1,1,-1,1,1,-2,9,-9,-8,-2,-8,8,6,-6,-3,7,-8,-3,-7,9,-2,-8,1,-10,8,5,8,2,1,2,-2,9,-7,7,5,-1,8,-7,-9,-8,-10,10,6,1,-1,-1,-2,-3,5,5,5,-8,-5,2,4,2,-2,-4,-6,6,-6,2,-9,8,-4,-5,-9,2,8,2,3,-5,-6,-3,-2,2,6,-7,-9,-1,10,-2,7,-4,7,4,-10,6,8,10,8,1,8,-1,4,7,-7,2,-2,-6,2,10,-1,-10,8,2,-2,2,-10,6,-4,-8,4,5,-8,-5,-3,4,3,-6,2,7,-10,5,-1,-5,-5,-7,5,-3,3,3,4,3,-1,-8,-6,6,-1,9,3,-8,9,5,7,8,7,5,1,7,-6,3,-10,-9,4], dtype = "int32")#candidate|10330|(1056,)|const|int32
call_10328 = relay.TupleGetItem(func_5945_call(relay.reshape(var_10329.astype('float32'), [14, 15, 6]), relay.reshape(const_10330.astype('int32'), [1056,]), ), 1)
call_10331 = relay.TupleGetItem(func_5948_call(relay.reshape(var_10329.astype('float32'), [14, 15, 6]), relay.reshape(const_10330.astype('int32'), [1056,]), ), 1)
func_8047_call = mod.get_global_var('func_8047')
func_8049_call = mutated_mod.get_global_var('func_8049')
const_10340 = relay.const([6.038276,-2.469619,-0.997565,6.029661,-3.662517,1.473304,2.503337,-7.034791,5.967417,-9.323963,-4.671798,4.716098,-3.175081,-9.824510,5.576122,7.983408,-0.693746,5.491321,-3.142343,5.621504,-9.118584,3.966636,2.475070,-5.777805,4.516515,4.010979,2.072884,-9.694160,-4.653785,8.115655,0.358817,-6.809234,-9.941420,-9.947742,-5.432671,9.814277,0.340810,-5.367302,7.818594,4.873445,5.790718,-5.674906,-4.359878,9.965572,0.889208,-8.438310,8.261347,-2.391428,-2.222008,9.989977,-1.437173,7.465307,7.458585,-7.689306,-1.150390,7.152047,3.500777,-1.142369,-8.523458,-9.190040,8.290887,-9.674607,0.210915,-1.655942,-9.139954,2.760501,1.293641,-4.707332,-0.310558,2.158783,-4.941059,8.844155,-3.782796,9.486196,0.826447,-1.134565,6.265832,1.592824,9.361569,-6.732027,4.900915,-9.225460,1.955069,7.941911,3.557444,-6.915487,2.712450,0.966390,-8.289344,7.739367,-4.031028,-7.438565,-1.914345,6.024349,8.575472,8.886950,0.055081,7.976970,-8.380101,-5.899634,2.468698,-9.382036,-1.930081,-0.698546,-3.700290,-0.069385,9.243859,-4.459674,4.985839,3.231130,-3.680574,9.407968,-9.508540,-9.251264,-2.338421,5.600835,5.201292,-3.360880,4.087064,-7.904569,-8.145222,4.699873,4.237274,-1.220503,9.662847,-1.452950,-3.434008,5.035260,-7.961841,-9.096260,-4.532593,4.437466,9.972851,-5.588286,-0.057205,-8.093438,5.691190,2.811472,-7.261003,8.318881,9.058224,8.433345,-6.176266,4.004667,-3.488097,0.832108,4.227631,-2.287213,-9.808035,9.365184,-0.258439,-4.252714,7.223453,-9.183605,4.722578,7.900032,0.138200,-8.790965,3.499505,7.716718,1.430344,1.871113,6.174247,9.698870,-2.025205,-4.915313,3.055729,-0.427278,-0.702532,-2.219385,3.938637,3.123367,-2.270936,-7.188715,4.528765,0.812301,-3.643872,5.570628,-2.694112,2.882375,2.479204,8.944889,-4.815375,-7.964375,0.846571,-5.620915,-3.585970,2.903978,-2.908975,8.692533,8.724886,-3.511395,4.214949,1.948448,3.977599,-5.119960,9.881654,7.808678,5.975969,-3.763986,-7.451158,2.659572,-0.922710,5.086280,-4.669431,-9.532659,2.271723,6.899340,-7.072471,-2.449378,-4.990486,3.003726,2.229884,6.920940,-2.431681,4.458872,3.332307,3.166497,5.607688,-2.171246,8.327418,-2.749169,7.624260,6.382806,-2.327087,5.708587,-6.282176,-0.282959,7.795336,2.741942,-9.030008,-3.301077,2.827613,0.124634,-9.303379,3.852813,1.310158,-9.741351,7.031901,-8.309309,-8.881920,-9.300155,-0.108527,-9.022746,9.305375,5.001613,-9.503257,7.645110,-7.265008,-4.833393,-7.870394,-5.421180,4.735759,-8.246060,0.352806,0.932946,7.690019,-3.817356,-8.438942,0.123609,-7.439977,6.135100,5.399204,7.199463,-7.701644,-7.093665,4.610506,-3.183283,-2.107862,5.191111,4.917310,8.814063,8.005206,7.110227,-2.915171,4.693182,2.939750,5.947517,0.236773,-1.145619,-9.709364,-1.262842,-3.590145,9.505875,6.341857,-9.748003,2.371634,4.394284,6.139515,-7.212812,-9.598021,5.872499,5.919402,-1.112277,1.698264,-5.552126,3.085172,0.668530,2.295725,-2.515974,2.532726,0.740188,-3.466042,0.875703,4.224511,7.183292,6.231614,-2.640044,7.981034,2.904624,0.166038,2.978647,-4.511916,-5.543778,4.505391,0.224680,7.741926,1.884990,7.719372,-7.734716,-9.302428,-3.789023,-0.750246,-5.618402,5.407840,-8.630905,3.490053,-1.375258,-5.046267,5.812985,0.707492,-8.414473,-8.288142,7.681956,7.114256,-8.669484,2.748627,0.910362,3.876748,-3.243641,-5.596443,-7.559484,-1.972090,0.303679,3.748912,-9.104900,8.709006,-7.371810,-8.263348,-3.689728,2.927363,3.448814,8.607844,-0.571216,5.084327,-2.542578,6.774621,5.316601,5.898982,-9.686991,-1.022434,0.128998,9.360064,0.920080,7.224155,8.442417,-0.135333,-2.134714,-4.023524,4.712366,8.355728,5.009178,-1.168334,-6.441908,9.108430,-9.814625,2.746161,-1.215318,6.418457,-9.847153,0.834615,1.591043,-1.580006,6.863908,-9.737213,-6.755351,-5.256989,-7.788274,9.298458,-9.836668,1.823764,-7.408913,3.924591,-3.935992,-6.368481,8.899843,-4.495234,9.294771,-4.559595,8.160431,8.423293,-3.717311,5.443296,-2.422359,9.937035,-8.758206,-3.607119,6.721471,1.301914,-3.382880,-5.878684,6.154215,5.613948,-4.686901,6.701548,-7.378025,8.985618,4.039431,-9.853074,4.255818,-3.638029,-6.388854,-2.809587,-3.572361,0.597444,6.963428,3.830061,3.624895,-9.860894,-7.220428,4.433345,-5.073175,-5.157557,-8.462186,-1.550451,-7.769382,4.962397,2.088064,6.745763,9.640982,-1.139816,-2.560536,5.910805,-4.938235,2.658208,8.597451,-6.926485,-0.484946,1.459706,8.136012,-0.519472,7.746969,-3.603080,-2.634633,-2.900792,3.354369,-9.887227,-3.730523,5.484662,5.636601,-6.900591,8.128001,8.680623,3.892114,-1.338084,-6.051857,-5.187316,-4.630655,-3.101886,-4.857975,-8.620618,3.108847,-4.764399,-1.342968,1.857637,-1.809020,5.861071,-8.197738,9.493453,9.610206,-7.538966,1.747488,2.014275,8.863594,-7.979294,9.719814,3.232709,4.976339,-7.227083,7.830305,-9.745098,8.736048,-4.447872,-7.718138,3.143480,8.651772,4.491274,2.245372,5.766802,-7.803793,-3.052031,-5.019738,-7.678278,5.371918,-1.352055,-9.696909,6.804824,-7.866333,5.690841,1.180366,-1.728496,-2.782715,9.634828,6.855078,9.745579,-1.859857,6.395928,5.757570,2.153324,-1.934409,-7.159590,-9.880771,5.417276,0.978704,7.734702,0.468443,6.770468,7.514855,7.270431,5.266556,-1.359497,1.418343,3.760844,7.427226,7.622390,-3.293869,8.985613,7.689281,8.702814,5.261013,-6.590755,-7.134096,8.966423,-4.262271,-2.898093,6.968500,-0.699959,-3.187935,4.178114,-2.171876,-2.265009,-0.107395,8.951654,-7.299679,-0.946607,0.368054,-3.937286,3.363377,4.430385,6.697217,3.858945,-8.147000,3.310135,7.242105,-6.701716,4.713596,-2.737006,-3.060813,-1.489044,-5.397779,0.107450,0.736147,-3.874489,8.973823,-9.543178,8.959816,2.008276,1.244765,7.769358,3.186162,-2.640141,-2.811049,9.966061,-2.586186,1.323407,-2.294099,-4.782090,-6.364558,-4.210101,-8.571948,-3.517985,3.597646,5.675034,-2.402904,9.416406,5.173030,1.418970,9.160434,-9.538860,-1.233502,-1.518776,-3.804669,-3.703957,4.175266,-7.317829,5.812113,-7.165617,-0.799003,-4.610778,-6.623015,7.380408,2.226205,2.904475,8.256775,4.531306,9.002113], dtype = "float64")#candidate|10340|(616,)|const|float64
call_10339 = relay.TupleGetItem(func_8047_call(relay.reshape(const_10340.astype('float64'), [616,])), 2)
call_10341 = relay.TupleGetItem(func_8049_call(relay.reshape(const_10340.astype('float64'), [616,])), 2)
func_8365_call = mod.get_global_var('func_8365')
func_8367_call = mutated_mod.get_global_var('func_8367')
const_10347 = relay.const([4,6,2,-6,-3,2,-6,-9,-5,-9,1,3,6,8,-4,2,6,-10,5,7,5,-4,-6,-7,7,3,4,9,-7,-9,-8,9,-10,-2,2,-3,-1,-10,-9,9,3,-5,-9,-6,-1,-7,8,3,-4,-5,6,-3,-6,-5,10,-2], dtype = "int8")#candidate|10347|(56,)|const|int8
call_10346 = relay.TupleGetItem(func_8365_call(relay.reshape(const_10347.astype('int8'), [56,])), 1)
call_10348 = relay.TupleGetItem(func_8367_call(relay.reshape(const_10347.astype('int8'), [56,])), 1)
const_10350 = relay.const([3.322235,-8.259266,-2.157459,5.261208,2.943169,7.240564,5.971870,6.198221,-7.205109,-3.948325,6.746273,6.567483,-3.053710,-6.121114,-5.393096,-1.138579,7.079832,7.713902,9.721547,-0.607751,-8.349533,7.552345,3.637538,-1.653737,-0.936247,-6.326036,5.115342,-8.549689,7.208354,-8.330301,5.272945,7.524284,0.464374,-3.274928,-7.333689,8.113554,-4.484200,-7.840634,9.260247,-8.083760,2.323236,8.478562,-9.019937,-4.227909,-5.211257,3.833963,-9.544771,-0.044544,-6.663442,-6.427217,6.952331,7.636882,-6.614847,-2.421227,5.235116,-6.352678,4.605693,2.420914,9.677924,5.973556,-7.105997,2.094305,4.659216,4.834138,-0.998886,-7.749501,3.611969,-4.183883,1.170283,-0.333932,3.632808,-8.537485,-5.715856,-7.025063,2.197922,-8.459462,-4.518638,-7.567290,8.814981,7.050084,2.872721,-1.973016,-1.113482,1.154663,6.956204,-8.718011,-8.278576,6.240943,-2.439256,-2.489137,7.726042,-5.912796,6.361554,1.381094,-2.397229,-3.960865,3.689308,-9.220198,5.353449,1.905158,1.027166,0.941992,-7.730402,6.580709,-6.117382,6.680089,-8.205066,-1.621857,-2.807875,-8.810498,-5.584076,8.693646,0.461167,4.595872,1.704734,9.356074,-5.279949,-4.808416,4.407969,-9.634686,3.251861,9.523075,8.059517,2.643314,-6.204071,-9.934828,2.668280,-2.400359,2.891191,2.455016,-1.385416,-1.428285,-9.170089,-7.610973,-8.652157,0.006974,-9.487845,5.803926,-9.813581,3.730425,-5.110919,-2.815671,7.070630,7.089920,-5.061455,7.501053,9.498817,-9.021366,-7.488584,-4.118264,0.236223,3.007467,-7.326114,4.912826,9.642670,0.640083,-2.905524,8.013086,-6.161484,-9.148469,-5.292163,-2.788014,6.072027,3.776888,4.577964,-4.303073,9.877894,-1.364249,-8.790390,3.563390,-9.317555,-2.655762,-8.788093,2.470784,-6.064408,1.192889,2.172935,-0.231737,-0.241762,1.431493,0.241927,-3.484549,1.246457,1.785398,-2.665574,3.937228,6.101427,6.584387,-0.689499,3.220503,3.645266,7.132433,-3.062872,8.095884,7.963414,-9.566677,8.962914,4.640282,1.396701,-9.912869,3.380803,-2.780366,8.685218,-5.765672,-1.195853,-6.737102,8.598175,9.314091,-6.165157,-3.084438,4.179606,-0.656135,-9.849583,6.448542,-8.274440,5.062877,9.174533,0.259872,-9.188617,-1.655572,6.982264,-9.684907,-9.912886,-1.624302,-8.001218,-4.261994,4.933298,-7.368894,9.147981,5.053097,-3.440036,3.897427,-0.792095,-8.954939,3.122035,-9.267911,-2.547256,3.053382,-7.017367,0.247007,-5.227440,-3.015897,-4.021614,3.347063,-6.700243,-5.543749,-0.179313,-8.014890,-4.002544,7.579275,-0.904232,-2.886465,-6.162533,0.232288,8.507398,9.842396,4.671433,2.376238,3.957650,1.608464,3.585971,-2.610588,2.309397,-7.279500,2.016339,8.409875,4.317084,-6.551599,0.408496,-0.047224,-1.288990,0.113777,3.424891,-7.830180,8.952416,-1.103743,5.385932,-1.610813,-0.496434,-8.072126,-5.362621,8.177632,7.552676,8.078484,5.534565,0.321976,-7.712393,8.486654,7.201864,-1.856268,5.971259,6.231744,4.738584,-6.605525,-3.711995,1.711870,-9.696651,7.645734,8.254493,8.286470,-7.131626,-0.511777,2.511371,9.207200,8.385188,0.773115,-6.546859,1.011165,7.268563,0.075129,-6.130621,-3.893920,0.200791,-8.361981,5.252047,-8.986770,-7.897647,-7.473395,-7.683017,-2.569103,5.845919,7.349586,-0.809430,2.977018,-7.112747,-4.007396,9.034697,9.250051,-4.138533,7.021106,6.840858,8.044571,2.819731,6.603254,3.590055,7.060665,-8.611322,4.613917,-7.160618,-8.382118,6.718225,5.529299,3.296337,-0.925928,5.628829,3.430625,3.608075,-4.765717,-4.201632,-6.007799,-4.803293,-9.785904,-4.066583,9.432402,-1.043128,3.081167,-0.981835,8.400782,-9.908686,6.196375,7.306212,-2.700858,-6.387370,2.505137,5.778628,-6.622721,-4.898710,-4.919265,-4.965224,2.521435,6.651010,1.727428,8.341580,0.818446,-5.435203,9.915447,-5.696141,-9.726726,5.728990,7.476153,4.269002,-6.923372,5.362509,9.212429,-7.835552,-6.781599,9.308420,-1.238195,-7.242340,-4.042729,-4.865783,4.979160,-7.201888,8.734878,1.936685,-4.437054,7.414289,-4.736584,4.983793,-8.122908,-0.579122,7.897058,-6.436168,6.178841,4.773542,3.505449,5.146663,-4.703062,-5.511907,6.387804,1.090613,2.823751,-9.550725,3.847508,7.205234,-4.710263,-3.947457,2.270427,2.008913,-6.676813,9.971745,-4.671019,-2.483670,-4.094705,1.981861,-3.857334,2.274947,3.104648,-6.138917,2.952592,-9.713011,3.544720,3.740395,-1.152742,5.318307,8.719690,-5.559144,-3.366253,1.976853,-6.735001,-3.362997,4.456049,-9.487813,-4.848662,8.360263,-5.318552,1.091703,-9.560814,-1.887028,8.887427,6.008189,-0.650606,-7.864204,-7.979635,9.486974,-7.809868,-5.201821,7.554507,-3.967624,9.383689,8.632144,-6.899289,7.293995,2.736282,1.836585,-1.134430,-1.840653,-2.993533,2.316073,-0.981611,0.304187,-0.750333,-0.191635,-7.913811,1.363459,-4.824953,4.911380,5.693022,0.652813,9.900520,4.591699,-5.573640,-4.751567,2.326319,9.047281,8.871233,-6.000786,-3.514630,2.371179,-4.442998,-7.293631,-1.175321,6.984024,2.999023,-8.054004,4.788986,-2.445849,4.942563,-7.893288,-0.630653,-9.472588,8.515432,5.154961,9.137351,-3.875396,-1.073790,-9.752848,7.214852,-2.180952,8.947290,7.476304,1.057073,-4.337040,-6.630786,9.098046,-8.106428,-1.922530,-9.498829,-0.154728,0.259439,1.229952,0.138552,-2.561509,0.606989,1.621233,1.304101,6.003080,-6.905022,-6.220055,5.896932,5.229858,8.213394,2.032026,-0.093205,-2.251145,-4.473997,0.356307,0.732345,-4.204213,-5.850933,9.499615,-5.517800,-2.398928,-7.059223,-5.875321,-1.226885,-8.207525,4.743687,-8.903062,2.040634,9.328205,-8.913654,7.544956,-4.999363,5.514588,-9.023653,1.212854,5.435587,9.332543,-7.173479,8.305089,-3.252003,-6.816486,9.294521,0.438949,5.219294,3.562424,7.403079,-4.100792,-1.140964,-4.198560,-8.978048,-4.036629,-5.850627,-6.003970,1.299215,0.028296,9.379004,8.638200,-6.107457,4.469486,-8.268779,-5.267525,9.624095,4.517202,-4.084792,-2.213485,4.026697,-1.950171,2.100961,-1.135179,9.689674,-5.623244,-1.781371,3.272690,-7.264969,-6.230505,4.978395,-5.773678,8.022052,6.802356,8.758461,2.571118,-7.586094,-6.018125,-8.885127,-2.665186,1.790630,-8.685987,-1.457595,-2.027286,-6.411225,8.160362,6.504542,-7.412516,-2.617731,-6.313093,-3.550179,-9.217198,-4.133052,-7.168247,-5.402887,-8.000297,4.570739,9.612415,-0.265967,-5.096296,-8.661025,3.987555,9.380620,4.346324,9.424116,5.968641,9.174986,-6.549384,2.400118,-6.481260,6.460087,8.287792,9.388532,-9.931899,-8.431148,-1.348203,1.671879,7.843330,5.074474,-9.555501,-7.470488,-5.886811,5.624491,2.796278,0.985216,-7.192215,-6.254530,0.760162,-0.193068,-2.539763,-4.542419,-6.191994,-4.985364,-8.802677,-2.766931,-2.323448,9.849739,-3.018988,1.715931,4.563070,2.674846,1.325180,1.078804,9.685174,-3.579324,-8.784660,-7.742637,-1.379298,-7.699080,-7.551376,2.920721,-1.924087,-6.024999,-8.237910,-3.950930,-7.785384,8.648053,-3.201200,6.803784,5.969505,9.681336,-2.332205,-3.494433,-0.177827,-7.324693,9.507474,1.107716,-3.983845,-5.979990,4.880575,-9.929450,-8.590220,0.529026,-9.821624,-2.488151,-4.880354,2.165394,9.476512,-0.395914,9.361991,-3.591822,-4.865149,-3.303029,0.767871,2.724935,1.599983,4.673292,-5.482558,-4.875595,3.833526,-9.076042,-9.773963,-7.024367,2.975170,0.754584,9.517174,0.066560,2.878109,-0.870921,-1.499843,8.907686,1.557008,2.545015,3.910840,-1.246024,-5.556615,5.485217,3.091680,-2.025241,-4.781038,4.763686,3.261616,1.848000,-7.069348,-3.092213,-5.194463,-2.162834,-5.163161,6.986386,-3.453811,-6.225442,-2.223853,2.407025,2.909085,-8.196658,-7.410725,-2.850422,-8.348950,-3.618416,5.904528,6.254574,8.065833,-6.941703,0.016717,6.982569,1.296159,-6.727705,7.189693,6.618649,8.944670,-3.299118,5.764897,4.834795,8.912662,-3.993925,-4.208318,-7.933364,-2.458398,0.867503,-5.329365,7.105502,-5.653633,5.514999,8.232525,8.463153,-0.515704,-8.767898,-8.394623,9.252708,-7.194781,-6.401862,3.211652,-0.256543,6.108301,2.458043,-1.778565,-3.731276,-4.790130,2.310720,-5.745871,-1.313382,-9.485622,1.893503,-0.624480,-8.214190,-2.247260,-5.800793,8.945259,1.033517,-1.415923,-0.517520,0.762392,-8.972967,-1.106918,-2.267318,-0.095766,3.044856,8.401581,1.460083,0.998889,-9.723923,-6.965042,0.745359,8.468445,6.546215,1.054396,0.348266,-3.219286,-5.699539,3.469484,3.908058,3.509332,-0.554298,8.343712,6.671086,-7.772805,2.240299,-0.295833,-5.215590,9.913282,1.278249,-3.935572,-7.429937,-8.327134,0.826349,6.452333,2.469479,-3.976415,4.853345,7.670704,-7.874811,6.966620,4.000669,4.699899,5.334335,8.768091,6.132820,2.242991,-5.625101,6.663803,3.582849,-4.147921,1.671522,2.490820,3.346372,5.195302,-7.799162,0.029164,-3.198646,6.576700,8.200908,4.584405,-5.311134,-9.754370,-0.938406,1.787362,-6.764688,9.198970,-9.624276,4.103968,0.261557,6.728379,5.533039,8.259600,2.110403,4.925155,6.987160,-8.002214,-0.282884,-6.244400,-4.312182,-6.152120,-4.716360,-0.270894,-0.314232,-2.452779,6.839722,2.049675,-2.582344,-5.633764,-1.287952,-8.964222,-8.649500,9.010142,-2.154109,-6.500398,8.388325,4.846090,-7.130955,-9.468633,1.369758,-0.821915,6.920947,9.380364,7.571740,3.465094,-0.489048,3.850040,-9.375241,4.235460,6.384319,6.024182,-6.671259,-5.579653,9.659995,-0.397100,7.883097,5.754252,-9.116137,-7.030306,-1.982791,3.580029,7.600713,-8.907458,-5.890574,-9.106096,4.317410,-5.927720,9.137397,-1.188254,-2.683289,0.546918,8.050358,-8.079658,-8.889075,8.531175,-9.979047,8.226285,-5.458572,-5.501991,8.351798,-0.431911,-4.405860,-2.722161,5.931283,-4.304322,0.466813,4.615352,-1.548869,8.085181,-2.810855,-6.812325,1.285951,-2.273028,7.043853,-1.846056,-0.154372,0.235758,-9.510421,-0.636700,-1.804594,7.978068,-7.968530,-0.406172,-8.691342,4.231686,8.328887,2.310142,4.146669,-9.618625,-4.488974,8.893833,9.532525,-6.540354,9.038156,5.121626,1.672406,8.790450,2.586465,9.906328,8.371475,-1.590003,-9.207033,-9.714394,5.990526,-7.488805,4.205476,-1.288082,-8.610002,-8.074243,4.471411,8.929958,-2.749322,7.999543,-0.778130,1.863676,0.668105,-0.251567,-3.266531,-8.959147,4.827802,0.635925,-0.315078,9.277755,-6.052276,-6.869585,7.090461,6.999378,8.067805,0.236702,3.249360,8.296950,-2.410143,-7.215446,-5.728284,1.050862,8.972505,9.107643,-7.619245,-0.136163,-9.420139,5.067433,-2.740216,-5.716681,1.948318,0.950083,-3.980184,8.491062,9.770610,8.290454,-6.870551,8.505883,-1.681395,-5.185350,-5.227270,2.794403,0.909137,-4.695928,8.278681,2.745638,4.809965,2.710274,-3.847233,-0.827346,-8.775613,5.351895,-8.009053,-1.574448,0.926601,-5.492896,4.268761,8.051566,-3.024146,-2.841365,-3.644523,-3.342740,6.583638,5.395721,-2.762040,0.938314,-3.590439,-4.554601,3.904535,9.647986,5.109720,-5.514766,2.493762,8.967961,-3.648062,-6.663764,-8.276837,-5.915851,-5.722169,5.897526,6.471976,-3.084486,4.766043,6.786939,5.972616,-4.169014,-5.766348,-5.547875,-5.174909,5.763279,6.764224,3.302525,-9.136390,4.722316,0.938524,7.314542,5.992634,-6.536311,-0.515998,-0.643092,-5.949780,-6.431228,6.554559,8.286772,2.384321,-5.777091,-0.784168,-8.686480,6.217331,6.052149,-6.773598,-1.294169,-4.958887,-9.886555,-0.833337,6.697588,4.493944,9.680146,-8.603308,-3.173673,8.293204,-2.544137,-6.973725,-1.897500,4.285808,1.732360,-3.778522,0.503219,-3.140292,-7.929101,-4.981079,-5.035369,3.750435,0.080038,-4.826323,2.910826,-9.681764,7.469240,-4.417684,1.592093,2.039151,9.608473,-2.964476,2.895745,6.918724,8.848040,2.327991,5.210497,4.676294,-0.850148,7.522715,3.870210,4.606640,-2.727615,-3.213296,5.782763,-0.625292,7.817192,-5.937828,-1.645570,-2.463749,3.910358,1.381590,9.476317,5.154472,-2.276724,4.873570,4.438361,-0.284898,3.306470,0.319916,-0.313908,4.811708,-9.684415,-0.354106,7.815184,-6.040134,-1.046777,-3.353947,-7.574541,0.584546,-2.724020,-1.846440,-4.648540,8.874615,5.377044,-7.952545,5.379613,8.618884,2.821753,-3.686817,2.413682,-4.852215,-8.028702,0.392398,-9.120435,7.823389,6.960826,-1.850505,-0.858830,3.130912,-2.930292,4.904794,-8.685810,9.101360,4.945169,-5.167276,-4.971651,-6.397280,3.891144,0.007088,3.627951,-5.317521,-9.920562,-2.966645,0.706590,-1.545955,5.652613,0.613543,9.825675,-1.007341,-7.166235,1.034245,0.773374,8.617036,8.980438,-9.899819,1.038902,4.087411,-5.328024,-2.080586,-9.274456,8.969151,-0.411948,7.341624,-9.030492,-4.952378,-9.468953,4.160947,-3.578976,7.792697,-2.305928,-3.811177,-2.562498,7.156630,3.091414,-7.894039,1.810465,6.218895,-8.993487,2.726771,-9.040086,7.878381,2.407948,-2.680238,5.174757,5.965304,-1.067297,5.845948], dtype = "float32")#candidate|10350|(1260,)|const|float32
bop_10351 = relay.equal(var_10329.astype('bool'), relay.reshape(const_10350.astype('bool'), relay.shape_of(var_10329))) # shape=(1260,)
func_978_call = mod.get_global_var('func_978')
func_981_call = mutated_mod.get_global_var('func_981')
const_10367 = relay.const([-3.092881,-4.776300,-9.654720,6.412050,0.470624,-8.201963,3.635576,5.640555,-9.894163,-8.693947,-7.924986,3.512280,-2.768587,0.451271,-5.287745,-5.782884,-7.045799,0.204100,6.664143,3.503505,5.308124,8.332577,-1.949178,4.313579,-0.646518,-8.140877,1.618806,7.962951,-1.034386,0.711094,3.587719,7.624636,1.306451,-9.502593,6.351087,1.727741,8.200307,8.991531,6.142969,-4.176262,3.601301,-1.294397,8.346967,-8.246478,-3.969820,-8.512247,0.019924,6.777572,-6.258565,2.844926,-1.269272,8.763006,3.090102,6.959139,2.162215,-2.023310,2.929889,5.136232,4.194112,-4.717445,9.989638,0.909085,-0.225151,4.519187,-0.848341,-1.741947,2.350464,-1.417857,9.771972,1.724034,4.678688,7.906652,-8.101765,2.819637,-4.405311,8.723878,-8.826390,0.913996,-4.112924,-2.458301,2.375680,3.868630,-5.962571,-4.289610,5.228312,-5.449469,2.191449,4.502096,-0.368192,2.847965,-9.428610,-1.550587,6.943137,1.809928,1.678637,-9.283399,3.489408,6.526423,0.100236,6.852800,-5.377661,-0.947201,4.642741,7.876792,-1.764534,-0.208031,-8.718452,-5.425344,-3.220936,3.586500,0.888081,6.008647,3.758558,-0.982632,-1.207585,6.745003,6.428936,-6.965046,-2.991449,-2.629081,1.605510,5.480579,6.928767,7.595133,-4.994871,6.134469,3.944644,-8.124715,-8.130968,5.649815,-1.986267,3.767155,-3.605829,-8.131171,3.763722,-7.465793,8.230309,-0.431573,2.405105,7.580527,-5.754552,6.230091,0.675560,-2.804226], dtype = "float64")#candidate|10367|(144,)|const|float64
call_10366 = relay.TupleGetItem(func_978_call(relay.reshape(const_10367.astype('float64'), [3, 4, 12])), 0)
call_10368 = relay.TupleGetItem(func_981_call(relay.reshape(const_10367.astype('float64'), [3, 4, 12])), 0)
func_4445_call = mod.get_global_var('func_4445')
func_4447_call = mutated_mod.get_global_var('func_4447')
const_10371 = relay.const([3.275702,-4.699275,9.336748,-6.190689,-0.201534,-2.647690,3.831633,-9.648822,1.879590,7.303018,-1.187708,-6.880468,9.316114,3.529614,2.684817,2.746225,5.200372,2.079232,-8.460474,2.882398,0.984563,-6.781499,-7.011651,-8.274347,-7.329206,5.143197,-6.135261,6.497789,6.221802,7.473602,-9.777771,2.640644,-6.622698,7.222373,-8.040367,6.902441,-7.551556,-9.591882,-4.584694,1.722368,-3.874090,1.765231,-6.350094,2.226286,7.349937,-1.812270,8.782566,8.754877,-5.552861,-5.291625,0.984496,-0.505270,0.894008,-0.395573,6.405953,-1.110080,-8.841721,9.957646,-0.134756,-4.806975,9.622193,-3.650370,7.348918,-4.539141,-3.045701,-1.465656,-3.703828,0.169322,-5.196622,1.308109,9.123813,1.508926,-0.794110,7.219973,6.596076,-3.048202,-5.226786,9.275928,8.744748,-4.772685,5.085198,2.353540,5.464031,4.170659,1.328248,-4.373801,3.210633,-2.605126,-3.895869,-6.728319,-8.696647,-3.292233,0.626016,-3.671930,3.951292,-4.678690,7.676284,-7.757504,8.403298,-7.548561,-9.971704,7.743549,8.521674,9.304025,9.294809,6.291034,0.309609,8.988998,-6.833405,0.496731,-0.521695,-1.620578,6.997965,-1.361480,-8.946043,2.707849,5.522385,-9.542576,2.983475,-2.219141,-7.630478,-7.965958,4.722833,-5.924102,0.024260,8.506080,-6.565138,6.729297,-5.874015,-0.634055,6.597926,-4.681408,-5.978424,9.412263,-0.799265,8.993294,5.101551,-0.291976,6.522412,-5.725332,-1.719038,-0.842162,0.379157,2.666439,7.727980,4.232391,9.231429,-2.350709,-9.184455,9.795091,5.270303,3.522693,-3.778681,-8.672957,5.575946,-5.358666,-8.740830,-7.877663,8.810472,-8.996024,1.178262,4.466291,8.450879,-7.372384,0.024661,-8.184056,-3.481350,6.309623,-5.014653,-9.993705,3.620065,4.991514,0.126599,9.797266,9.975571,-2.363104,1.215646,-7.168113,1.302430,8.731281,-2.581676,2.745140], dtype = "float32")#candidate|10371|(182,)|const|float32
call_10370 = func_4445_call(relay.reshape(const_10371.astype('float32'), [2, 7, 13]))
call_10372 = func_4445_call(relay.reshape(const_10371.astype('float32'), [2, 7, 13]))
output = relay.Tuple([call_10296,call_10319,call_10323,call_10328,const_10330,call_10339,const_10340,call_10346,const_10347,bop_10351,call_10366,const_10367,call_10370,const_10371,])
output2 = relay.Tuple([call_10297,call_10320,call_10324,call_10331,const_10330,call_10341,const_10340,call_10348,const_10347,bop_10351,call_10368,const_10367,call_10372,const_10371,])
func_10386 = relay.Function([var_10329,], output)
mod['func_10386'] = func_10386
mod = relay.transform.InferType()(mod)
mutated_mod['func_10386'] = func_10386
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10387 = relay.var("var_10387", dtype = "float32", shape = (1260,))#candidate|10387|(1260,)|var|float32
func_10386_call = mutated_mod.get_global_var('func_10386')
call_10388 = func_10386_call(var_10387)
output = call_10388
func_10389 = relay.Function([var_10387], output)
mutated_mod['func_10389'] = func_10389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7349_call = mod.get_global_var('func_7349')
func_7350_call = mutated_mod.get_global_var('func_7350')
call_10408 = func_7349_call()
call_10409 = func_7349_call()
func_5312_call = mod.get_global_var('func_5312')
func_5315_call = mutated_mod.get_global_var('func_5315')
const_10425 = relay.const([-8,7,6,4,6,7,10,5,10,9,-5,2,7,6,-3,-5,8,8,5,3,5,-7,-2,8,-10,1,-3,-7,-10,-6,-3,-3,-3,4,-4,-1,-9,-4,1,-2,-1,6,-3,-2,7,-8,-1,1,4,3,-4,-7,-3,3,-2,-4], dtype = "int8")#candidate|10425|(56,)|const|int8
call_10424 = relay.TupleGetItem(func_5312_call(relay.reshape(const_10425.astype('int8'), [56,])), 2)
call_10426 = relay.TupleGetItem(func_5315_call(relay.reshape(const_10425.astype('int8'), [56,])), 2)
output = relay.Tuple([call_10408,call_10424,const_10425,])
output2 = relay.Tuple([call_10409,call_10426,const_10425,])
func_10430 = relay.Function([], output)
mod['func_10430'] = func_10430
mod = relay.transform.InferType()(mod)
output = func_10430()
func_10431 = relay.Function([], output)
mutated_mod['func_10431'] = func_10431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9891_call = mod.get_global_var('func_9891')
func_9893_call = mutated_mod.get_global_var('func_9893')
call_10432 = relay.TupleGetItem(func_9891_call(), 0)
call_10433 = relay.TupleGetItem(func_9893_call(), 0)
func_9044_call = mod.get_global_var('func_9044')
func_9046_call = mutated_mod.get_global_var('func_9046')
call_10436 = func_9044_call()
call_10437 = func_9044_call()
func_9876_call = mod.get_global_var('func_9876')
func_9878_call = mutated_mod.get_global_var('func_9878')
call_10440 = relay.TupleGetItem(func_9876_call(), 2)
call_10441 = relay.TupleGetItem(func_9878_call(), 2)
func_8444_call = mod.get_global_var('func_8444')
func_8445_call = mutated_mod.get_global_var('func_8445')
call_10450 = relay.TupleGetItem(func_8444_call(), 0)
call_10451 = relay.TupleGetItem(func_8445_call(), 0)
func_10386_call = mod.get_global_var('func_10386')
func_10389_call = mutated_mod.get_global_var('func_10389')
const_10465 = relay.const([-2.190811,6.551837,0.461411,-9.530095,-0.293296,4.203695,-0.631665,2.084908,0.788832,3.230286,1.964328,0.252168,1.001626,6.782298,7.467638,0.932197,-9.233016,8.927831,1.266401,0.830839,-7.461516,-5.820679,4.895607,0.346480,6.617719,-0.402595,6.644656,-6.782492,9.171709,4.114917,-5.651759,-9.441721,3.102994,-7.971591,-0.193593,-4.399225,-7.095110,6.995813,5.148232,-1.825006,-6.642491,8.539287,2.819026,-1.352618,3.974213,6.939271,9.423788,-5.992723,-4.293407,3.321244,2.391307,2.243293,-0.761860,3.177957,0.082143,4.690588,-3.029245,0.402394,-3.345823,-5.581462,9.428053,3.507306,-7.607482,3.255448,-0.116200,7.016008,3.162753,2.248971,8.205295,6.114448,9.332112,-8.080930,7.201690,4.036576,-6.608014,-6.648764,2.194598,-2.396357,9.683373,-6.551760,-6.056528,4.522188,9.484377,7.714281,-3.612738,9.721207,7.575812,5.986750,-4.636020,-1.112571,8.949339,-9.120428,-3.779967,-4.130809,5.105241,1.103180,-2.910587,0.041838,-0.441344,-2.349235,6.291402,-7.816804,-0.837054,0.497065,-3.554916,2.820625,-0.710762,-8.999242,-2.954019,6.951061,-3.028844,1.721711,6.261438,-3.076860,2.915337,-2.586083,-7.074724,-9.422492,9.265310,1.965627,8.919726,5.508907,6.064429,3.062766,-1.688485,8.611352,5.758780,2.653678,0.413640,-5.977979,-8.476559,0.072085,9.083079,8.088122,2.744439,-7.004084,5.407307,0.261883,-3.061455,-0.189960,4.493593,7.657981,-1.492506,1.066520,-0.979165,6.068588,1.523690,6.136306,-0.607994,2.521970,-1.853266,-9.096690,1.768785,-9.478738,-2.169041,-0.927394,-3.933906,8.572833,-1.723232,-7.629987,-5.151668,9.680409,-5.284906,0.736312,-2.359268,-6.853700,-1.884384,-9.470102,-2.802726,7.029828,-6.934266,-3.929106,0.440129,2.135754,5.554813,-6.513226,1.589884,2.572492,4.440741,-2.588408,5.808538,-4.574152,-2.156908,4.551222,5.886589,5.927204,-4.555160,-3.596253,7.066330,4.705340,6.711335,5.181569,5.858746,-9.531973,5.753351,-9.632485,9.214628,-0.457458,-4.760627,2.457537,7.092705,0.760209,-3.152085,9.188916,9.260795,-7.992253,9.842444,-6.829912,-1.616638,4.375323,0.341442,-0.962467,-7.556315,-2.905005,-6.454278,-9.564089,7.166961,7.299764,6.103054,9.014752,1.225796,2.780686,8.156373,-9.986572,-3.548761,8.620209,6.510567,-9.308919,0.213536,-5.872492,-3.729391,0.554120,-6.028697,-5.439087,4.301534,6.433339,7.825348,2.325295,-4.484074,3.201593,3.146496,-5.586008,-4.864126,-7.937378,-6.996685,-6.597258,9.181260,-6.357955,-6.053104,8.166028,-9.018281,7.756399,7.628793,5.493980,-4.725551,-5.390273,5.315279,-9.497295,-1.021671,4.297590,-7.316869,9.715891,4.092603,4.563608,-9.324125,-4.565008,9.859501,8.020162,-5.724181,-2.522093,4.200200,7.089050,-9.612470,-8.818842,-7.158062,5.132197,7.849825,4.267312,-1.731257,0.509401,4.224868,4.708845,7.037594,-4.677415,9.224808,-3.489010,4.451286,-4.117041,2.823156,-4.029526,-2.437829,-8.120887,9.215597,9.948109,1.566318,-2.652943,-8.577966,6.830276,-2.452697,3.840737,8.128212,-1.312404,7.984580,-8.088475,-5.440757,7.528210,-8.816053,-1.299143,6.235012,3.980836,-7.001106,4.837650,7.901447,-9.632743,-5.928024,-9.428958,0.122567,1.921319,2.406276,-3.545587,-1.106222,-1.501793,6.623055,-9.173645,-7.458780,9.751143,-3.862989,6.820409,-4.418492,6.047004,-5.666463,-7.995481,2.994760,-0.471993,8.962929,-6.468278,-7.149766,-3.607771,2.913725,-6.448082,-5.017690,1.242129,0.100532,-5.818150,-7.874065,-6.402180,3.798848,6.788719,-8.359975,9.454351,-0.424631,-2.313838,3.381478,-9.536273,1.811840,-0.096827,2.580469,-6.643377,6.851192,-2.243554,5.906870,-6.435675,1.157509,5.375467,1.608510,5.016251,-2.251173,7.050092,-2.415008,-4.720936,-0.353656,2.421407,-4.466781,-1.532770,-6.368117,-8.351026,-1.991160,2.566071,-5.611110,6.926680,1.636183,0.963072,-0.336459,3.703127,-0.373251,1.267420,4.261109,-9.734398,-0.207557,4.512909,1.240709,-1.553315,-2.729916,5.835978,-4.371026,-2.587183,9.056966,0.477679,-2.556394,-3.122969,0.464488,-7.767721,-7.216420,-4.522073,9.873150,-5.740943,8.096647,-6.315887,-5.580763,-9.029849,3.938798,-8.944606,-9.321291,-3.855701,5.874590,-1.807708,-1.178364,3.145445,4.647117,-7.345551,4.298556,-7.537392,4.098105,-1.510545,-5.916927,7.068939,0.202602,5.771932,6.011122,2.901998,-7.885592,2.294608,-1.419588,-3.001087,7.560345,-7.128125,4.536888,9.551302,-8.397769,-1.299085,0.676060,-6.169366,7.615664,-7.690523,8.984657,9.959724,1.508413,3.599539,8.723540,-3.585188,-5.579278,3.571291,4.688569,-4.707150,-2.762185,-6.197377,-7.149967,7.633042,-7.664528,3.659987,3.153904,-7.494779,0.861339,-6.152422,0.098669,2.919153,6.318404,1.129199,-5.821607,-4.717739,-6.785903,-6.620138,1.810563,-7.695465,8.684793,-9.990567,1.695911,-1.046940,-0.736408,6.405811,0.092642,5.662933,-2.071036,8.510438,-9.123471,8.895940,-7.097839,-7.196668,4.503682,-5.481042,-7.451826,4.015366,2.208404,-0.799630,-5.425541,6.715381,0.176303,2.948519,0.666235,-6.822027,-0.526429,-1.552792,7.768134,1.787984,6.110874,0.624483,-7.867362,2.274233,-3.962976,1.843689,-2.460835,-3.169130,2.583377,3.409803,-6.065533,-9.850350,5.541376,-7.815597,3.558687,-7.788624,5.258623,-5.246073,-1.032732,6.597093,-5.813488,-9.686861,4.114775,-7.826056,-3.069803,7.914597,7.449539,2.704194,-8.001767,9.511282,4.915762,-2.670161,9.411119,-3.115633,1.724863,0.988187,-8.341826,-0.232287,-9.019357,-5.989846,-3.550254,-2.262702,-8.227821,-1.782483,7.335244,-2.621703,8.511947,4.188817,-9.625318,7.660943,1.375345,3.507074,-9.005748,4.517238,-8.829650,6.265189,4.706516,-5.286812,2.273564,-4.038089,-1.090450,-6.368566,1.326548,-3.568224,0.007425,0.570961,-0.568624,0.315057,-1.981098,-0.174072,-0.897629,6.527523,1.104942,7.010706,6.401454,2.893833,9.175705,9.275670,9.199027,-7.034539,1.904730,2.739332,-9.457104,-3.504488,5.551978,2.322497,-7.883933,9.633991,-6.403779,7.624384,-6.149522,5.461517,-1.303909,-1.516305,-2.351820,-8.734873,1.093752,-5.531553,-7.774173,-8.906792,8.283024,-0.655460,1.923578,7.896147,-4.007565,1.106898,9.443394,-6.446033,1.340524,5.320597,9.510194,-2.474245,4.949140,-7.135379,8.965130,3.773463,-1.252020,4.041715,9.038097,5.389779,9.389407,-9.868840,4.669838,-8.548644,2.133345,7.228184,2.352387,7.221673,-3.087006,3.314364,1.520979,-6.152748,-6.401375,9.652701,-7.197516,9.356842,5.519288,-9.924675,4.133259,1.631340,-8.376227,9.618725,-9.601824,-0.671874,8.916504,4.889178,-3.213879,-3.362345,9.429544,-8.814410,9.902945,2.148075,9.274710,7.987805,-2.384059,5.626064,6.602331,-0.981735,-8.175288,-9.707460,-7.597132,-7.321351,7.853537,3.862226,-6.667490,-7.129893,-6.992572,-2.817161,4.771413,-5.144769,-2.310455,-0.231120,-1.414646,-4.833253,8.899613,-2.478777,-1.246544,-2.831259,-0.172728,-7.429084,9.657393,-9.685187,-7.455970,1.156223,-2.472658,6.486407,-0.023740,4.763028,-2.791971,5.167109,-6.411838,-5.882076,-8.913613,8.033819,-3.178844,3.633592,-8.871052,4.837856,-0.816292,8.584881,-5.242696,2.310215,-1.114269,-3.767141,-4.048067,5.770717,8.843954,7.356705,-6.011804,-9.340229,-8.617954,2.084614,1.493768,1.092791,8.276949,4.310459,2.827088,-6.672968,3.301172,7.196369,-3.853101,-9.499832,-1.763111,3.559780,-7.928340,7.370378,8.496000,-5.185270,-9.212389,-9.137805,-0.042104,9.763537,5.723498,9.073380,-1.322331,-3.762294,1.368506,9.368867,3.959205,4.867209,-6.284851,-4.568412,7.284231,1.890309,3.212451,6.182024,2.423876,1.622401,7.903414,7.144215,2.294843,-2.343195,-0.717440,-6.802817,3.572013,-7.406033,4.043923,4.425031,6.995327,-4.525998,1.833682,-6.433073,-6.200608,4.277530,-9.405383,-8.037936,-1.161897,7.015009,-7.834677,-5.239607,5.280635,9.611174,-2.894995,2.847447,1.568395,-0.220560,4.022192,7.271341,-6.999125,1.305504,2.159182,2.400629,6.541694,9.018319,-6.490864,3.433359,-4.414370,-9.382795,9.546977,-6.742132,3.331524,9.779241,1.425986,6.274948,1.093474,-5.288453,-5.787750,4.732418,-4.081993,0.237674,-2.370891,-5.296632,0.859785,6.221370,-6.550535,-7.250934,-4.031324,6.145685,-9.509386,-1.216225,5.754428,5.355285,-5.511147,9.741009,8.566747,5.247174,2.639980,-5.407829,7.983728,-3.958047,3.016980,1.100965,-5.098975,1.202461,9.161696,5.347587,-2.615356,-7.080409,4.947095,-8.822573,-4.183364,-9.551849,5.760445,8.021910,5.402897,7.029297,-2.981783,-2.613146,2.809207,7.082278,7.028058,3.813929,0.202554,-9.336194,-7.194886,4.840983,1.787375,-6.091570,-4.325649,7.154519,5.187145,-5.308546,5.251693,1.929641,-4.968828,-9.889142,1.136042,-9.381652,2.687779,2.345098,7.767710,4.025964,-6.788266,7.817200,3.135206,-6.039973,7.857036,-0.150102,-0.728912,9.713966,-1.363614,-5.933789,-2.376025,0.323382,-7.806038,5.375290,3.672722,-7.913426,-6.804115,2.711344,-2.289537,1.346897,-5.340593,-3.373855,3.299207,-9.762616,3.260263,0.833859,6.110881,-6.335410,3.737462,5.906404,-8.545453,-3.553699,9.383973,-9.252954,-0.218112,-8.421046,6.655838,3.459617,-0.566804,-9.303404,-5.099091,8.710352,-9.642063,3.508733,2.949656,9.783222,-0.202534,9.837782,3.788740,9.048276,6.773545,-7.215550,2.650935,3.707207,3.640114,0.572683,4.239645,0.042757,-0.562750,9.085858,1.388206,1.467940,-0.508949,-3.803153,-4.716756,7.703565,9.748465,-9.618679,7.478485,-4.686006,-7.025942,9.541171,8.673944,8.931818,2.948536,9.418493,7.063620,6.729096,6.018552,2.733206,7.817396,9.479002,3.169031,3.318631,9.693211,8.749184,-5.908677,2.586739,-1.425104,8.536466,8.731397,-7.837732,-6.307252,6.523571,4.185585,4.591384,6.719105,9.980910,8.565426,-0.523993,9.264776,-8.279989,-3.589245,1.810167,-4.576830,-9.958330,7.948526,4.555391,-6.293291,-2.581986,9.930800,7.354923,-7.645206,9.649790,5.880467,7.418535,-4.434252,-7.760063,4.184308,4.860336,3.551377,-2.757242,-6.360114,-1.936065,-2.260983,6.561301,-1.829949,-5.434443,2.607525,-2.269744,8.216926,7.461848,7.286430,-2.731683,3.407428,5.536935,-0.736561,-0.938567,0.440221,1.248567,5.332995,0.180701,3.802638,-0.658155,-9.164833,-6.373639,-0.051065,6.449835,8.478800,3.947729,1.342353,9.235922,-6.836459,-9.087630,-1.501620,5.708120,-0.168048,-5.453919,-1.808041,6.931024,7.241910,3.219007,5.210328,-6.736298,-3.786343,-6.967683,-0.393879,0.745932,0.927439,-0.928973,-5.699101,3.393878,-5.404841,-7.528113,-6.843567,4.493557,0.256141,-1.788838,3.871864,-9.313872,-5.318173,3.306896,-8.528944,5.566518,7.627831,-5.626103,8.875176,-4.853851,3.856221,-9.922080,-2.856788,1.413956,-8.899977,8.480268,-1.916147,-3.835828,-9.263055,2.506819,-3.378695,-4.674350,-6.178031,1.942849,-9.672785,-7.865987,4.107916,5.299725,-6.916170,6.659360,-8.268930,5.856619,-2.520799,1.694511,6.249804,-3.932178,3.781107,4.823738,3.427077,4.950113,8.390622,1.843786,9.773311,-5.442346,2.150058,-3.550706,-0.380209,7.757238,7.930992,7.823844,8.162602,0.226210,-2.260025,2.445779,6.069583,9.037467,-6.746385,6.766705,-6.418209,7.272223,-4.781208,2.902263,5.099398,2.416721,-2.782407,-6.616076,-2.914689,-8.741310,-2.727004,-4.503345,1.820388,-1.326682,-2.340492,4.544204,-6.608391,2.518531,-6.748838,7.409663,8.729547,1.063631,-0.684378,2.779834,6.087716,5.039113,5.507710,4.989395,-0.718057,-6.147684,-5.537022,4.115836,7.750502,1.785124,2.440649,4.139682,4.494666,-8.985034,-7.157106,2.868174,-2.946181,-9.359529,-2.765922,-9.664407,1.770884,-3.977218,-8.705098,-3.064931,-4.968787,5.725746,5.408598,-7.630271,3.312583,-2.270558,-5.351052,8.830433,-1.230523,1.171072,-0.190061,5.283106,-5.703053,4.248961,7.780925,-0.629178,1.126285,-9.262154,6.803299,3.463511,5.040444,-8.221083,4.960916,-8.508332,3.336667,0.331100,6.077204,-1.232694,-4.135587,-2.767026,7.902907,8.757532,8.693547,4.307507,-7.778512,8.482621,-2.124608,2.851985,-0.430136,-6.237061,1.319672,6.498995,-4.413933,1.134598,6.310053,7.132125,-7.557770,8.666402,-6.249245,-9.987349,8.009809,-9.844204,-5.250692,-5.381329,-9.771127,-0.937511,-6.715075,-5.827864,9.605283,7.944200,-1.996776,-2.214426,4.311018,-4.824546,-0.234633,-3.340196,-2.417683,-1.035214,-3.627989,6.873347,0.485695,3.377725,8.011918,-8.133677,2.346470,3.222568,-6.171893,-9.017981,8.031078,8.787487,-2.485505,-0.162200,9.938155,6.112556,4.160519,-7.279938,-1.490780,-5.723256,1.489577,7.695679,-0.456245,-0.319686,-5.025947,-4.921291,8.034357,2.581989,4.556697,1.207151,-3.206600,-4.734350,2.125713,-2.801244,-0.714701,-1.669298,-8.033261,-8.375790,-6.053798,0.960645,-5.085582,6.086494], dtype = "float32")#candidate|10465|(1260,)|const|float32
call_10464 = relay.TupleGetItem(func_10386_call(relay.reshape(const_10465.astype('float32'), [1260,])), 9)
call_10466 = relay.TupleGetItem(func_10389_call(relay.reshape(const_10465.astype('float32'), [1260,])), 9)
output = relay.Tuple([call_10432,call_10436,call_10440,call_10450,call_10464,const_10465,])
output2 = relay.Tuple([call_10433,call_10437,call_10441,call_10451,call_10466,const_10465,])
func_10478 = relay.Function([], output)
mod['func_10478'] = func_10478
mod = relay.transform.InferType()(mod)
mutated_mod['func_10478'] = func_10478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10478_call = mutated_mod.get_global_var('func_10478')
call_10479 = func_10478_call()
output = call_10479
func_10480 = relay.Function([], output)
mutated_mod['func_10480'] = func_10480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_10501 = relay.TupleGetItem(func_3123_call(), 2)
call_10502 = relay.TupleGetItem(func_3124_call(), 2)
func_4063_call = mod.get_global_var('func_4063')
func_4065_call = mutated_mod.get_global_var('func_4065')
var_10508 = relay.var("var_10508", dtype = "float32", shape = (280,))#candidate|10508|(280,)|var|float32
call_10507 = relay.TupleGetItem(func_4063_call(relay.reshape(var_10508.astype('float32'), [5, 7, 8])), 0)
call_10509 = relay.TupleGetItem(func_4065_call(relay.reshape(var_10508.astype('float32'), [5, 7, 8])), 0)
output = relay.Tuple([call_10501,call_10507,var_10508,])
output2 = relay.Tuple([call_10502,call_10509,var_10508,])
func_10513 = relay.Function([var_10508,], output)
mod['func_10513'] = func_10513
mod = relay.transform.InferType()(mod)
var_10514 = relay.var("var_10514", dtype = "float32", shape = (280,))#candidate|10514|(280,)|var|float32
output = func_10513(var_10514)
func_10515 = relay.Function([var_10514], output)
mutated_mod['func_10515'] = func_10515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_10542 = relay.TupleGetItem(func_2043_call(), 0)
call_10543 = relay.TupleGetItem(func_2044_call(), 0)
func_6370_call = mod.get_global_var('func_6370')
func_6372_call = mutated_mod.get_global_var('func_6372')
call_10551 = relay.TupleGetItem(func_6370_call(), 0)
call_10552 = relay.TupleGetItem(func_6372_call(), 0)
output = relay.Tuple([call_10542,call_10551,])
output2 = relay.Tuple([call_10543,call_10552,])
func_10577 = relay.Function([], output)
mod['func_10577'] = func_10577
mod = relay.transform.InferType()(mod)
output = func_10577()
func_10578 = relay.Function([], output)
mutated_mod['func_10578'] = func_10578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6679_call = mod.get_global_var('func_6679')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_10640 = relay.TupleGetItem(func_6679_call(), 2)
call_10641 = relay.TupleGetItem(func_6680_call(), 2)
output = relay.Tuple([call_10640,])
output2 = relay.Tuple([call_10641,])
func_10680 = relay.Function([], output)
mod['func_10680'] = func_10680
mod = relay.transform.InferType()(mod)
output = func_10680()
func_10681 = relay.Function([], output)
mutated_mod['func_10681'] = func_10681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8093_call = mod.get_global_var('func_8093')
func_8094_call = mutated_mod.get_global_var('func_8094')
call_10699 = relay.TupleGetItem(func_8093_call(), 0)
call_10700 = relay.TupleGetItem(func_8094_call(), 0)
output = relay.Tuple([call_10699,])
output2 = relay.Tuple([call_10700,])
func_10704 = relay.Function([], output)
mod['func_10704'] = func_10704
mod = relay.transform.InferType()(mod)
mutated_mod['func_10704'] = func_10704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10704_call = mutated_mod.get_global_var('func_10704')
call_10705 = func_10704_call()
output = call_10705
func_10706 = relay.Function([], output)
mutated_mod['func_10706'] = func_10706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4341_call = mod.get_global_var('func_4341')
func_4342_call = mutated_mod.get_global_var('func_4342')
call_10720 = relay.TupleGetItem(func_4341_call(), 0)
call_10721 = relay.TupleGetItem(func_4342_call(), 0)
output = call_10720
output2 = call_10721
func_10733 = relay.Function([], output)
mod['func_10733'] = func_10733
mod = relay.transform.InferType()(mod)
mutated_mod['func_10733'] = func_10733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10733_call = mutated_mod.get_global_var('func_10733')
call_10734 = func_10733_call()
output = call_10734
func_10735 = relay.Function([], output)
mutated_mod['func_10735'] = func_10735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9678_call = mod.get_global_var('func_9678')
func_9680_call = mutated_mod.get_global_var('func_9680')
call_10739 = relay.TupleGetItem(func_9678_call(), 4)
call_10740 = relay.TupleGetItem(func_9680_call(), 4)
output = relay.Tuple([call_10739,])
output2 = relay.Tuple([call_10740,])
func_10754 = relay.Function([], output)
mod['func_10754'] = func_10754
mod = relay.transform.InferType()(mod)
output = func_10754()
func_10755 = relay.Function([], output)
mutated_mod['func_10755'] = func_10755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7172_call = mod.get_global_var('func_7172')
func_7174_call = mutated_mod.get_global_var('func_7174')
call_10809 = func_7172_call()
call_10810 = func_7172_call()
func_9353_call = mod.get_global_var('func_9353')
func_9355_call = mutated_mod.get_global_var('func_9355')
call_10815 = func_9353_call()
call_10816 = func_9353_call()
output = relay.Tuple([call_10809,call_10815,])
output2 = relay.Tuple([call_10810,call_10816,])
func_10820 = relay.Function([], output)
mod['func_10820'] = func_10820
mod = relay.transform.InferType()(mod)
output = func_10820()
func_10821 = relay.Function([], output)
mutated_mod['func_10821'] = func_10821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10185_call = mod.get_global_var('func_10185')
func_10187_call = mutated_mod.get_global_var('func_10187')
call_10842 = relay.TupleGetItem(func_10185_call(), 0)
call_10843 = relay.TupleGetItem(func_10187_call(), 0)
output = call_10842
output2 = call_10843
func_10845 = relay.Function([], output)
mod['func_10845'] = func_10845
mod = relay.transform.InferType()(mod)
output = func_10845()
func_10846 = relay.Function([], output)
mutated_mod['func_10846'] = func_10846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_10850 = relay.TupleGetItem(func_3123_call(), 0)
call_10851 = relay.TupleGetItem(func_3124_call(), 0)
output = call_10850
output2 = call_10851
func_10852 = relay.Function([], output)
mod['func_10852'] = func_10852
mod = relay.transform.InferType()(mod)
output = func_10852()
func_10853 = relay.Function([], output)
mutated_mod['func_10853'] = func_10853
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10894 = relay.var("var_10894", dtype = "float32", shape = (7, 14, 9))#candidate|10894|(7, 14, 9)|var|float32
uop_10895 = relay.sqrt(var_10894.astype('float32')) # shape=(7, 14, 9)
func_6438_call = mod.get_global_var('func_6438')
func_6443_call = mutated_mod.get_global_var('func_6443')
var_10908 = relay.var("var_10908", dtype = "float32", shape = (2475,))#candidate|10908|(2475,)|var|float32
var_10909 = relay.var("var_10909", dtype = "float32", shape = (3360,))#candidate|10909|(3360,)|var|float32
var_10910 = relay.var("var_10910", dtype = "float32", shape = (336,))#candidate|10910|(336,)|var|float32
call_10907 = relay.TupleGetItem(func_6438_call(relay.reshape(var_10908.astype('float32'), [15, 11, 15]), relay.reshape(var_10909.astype('float32'), [3360,]), relay.reshape(var_10910.astype('float32'), [336,]), ), 0)
call_10911 = relay.TupleGetItem(func_6443_call(relay.reshape(var_10908.astype('float32'), [15, 11, 15]), relay.reshape(var_10909.astype('float32'), [3360,]), relay.reshape(var_10910.astype('float32'), [336,]), ), 0)
func_2410_call = mod.get_global_var('func_2410')
func_2413_call = mutated_mod.get_global_var('func_2413')
const_10913 = relay.const([0.014599,2.165649,0.327900,9.592496,-0.190208,-6.677832,-0.275494,4.738995,1.169945,3.670333,-6.541984,5.413836,1.116605,-9.877438,1.959929,-5.503959,-8.755860,-5.396772,4.781946,-9.857387,-2.733016,-0.972252,-1.211173,4.944235,-9.156957,-7.703496,9.162084,2.661819,8.416039,1.286351,5.581974,2.497706,7.855280,8.542358,-0.393785,3.085652,-0.802397,3.996162,5.717228,-3.149024,-1.322508,-0.847730,-3.075706,-6.935835,2.085913,3.621192,1.908375,0.609561,-2.033253,1.163873,-2.880319,-7.998515,8.165702,6.399265,-3.076833,-7.357340,-4.425429,0.646739,-1.407569,-1.280352,2.343123,9.004182,2.747587,-7.867686,1.679649,-6.948865,-2.672959,3.597616,-1.577873,-6.065497,-0.866421,3.992021,-4.854861,-3.882438,-5.383153,-4.335542,-9.279892,1.726739,-5.186248,1.903712,6.771309,8.176500,-0.516762,4.900586,-2.773128,-8.550354,2.264266,1.354933,-7.469669,-1.387483,1.093953,-9.397006,-7.626344,8.979502,6.568841,9.043701,-0.605400,-1.545104,3.891518,9.213980,-3.694918,-8.420337,-6.209496,6.173382,6.949376,6.525781,-6.738071,-7.494323,5.193232,-1.166978,7.164527,-7.909756,-5.827316,-6.068503,-8.843745,2.083839,2.350299,-7.232168,-9.633952,-2.750259,-3.129869,-5.880528,-1.839900,9.707318,-1.344590,-7.023242,0.054049,0.588027,-3.358883,3.973919,0.201161,9.434853,7.239049,-0.621456,5.189457,6.279167,1.608429,-3.103189,0.818427,9.661953,3.560796,1.934132,-1.325861,9.474572,-7.396885,-7.149897,1.629918,2.584146,7.732347,-9.180096,-7.058445,-1.556008,1.557704,8.147585,0.864777,-3.059659,4.806640,1.971638,-5.647584,-1.107733,-6.331120,8.494843,-8.914132,-9.421794,-5.682609,-0.674747,-4.529228,-2.534052,5.308967,-4.765772,5.329249,-7.148094,-3.802182,-8.025636,-8.546122,-7.665180,9.309417,-3.181087,-1.893423,-6.771879,-9.391446,1.269966,6.756263,-5.084301,-4.577390,9.608913,-3.982424,-3.619960,-8.079637,4.241707,7.735179,1.992530,4.895439,-7.888520,-7.753374,5.513027,8.380978,1.421533,-5.180693,5.631671,9.531088,-1.324901,-8.848668,-2.086037,-3.410852,9.925056,9.723522,-1.037175,7.835583,-5.712852,3.146687,-7.012395,7.085410,-3.188570,6.391946,-1.824713,-0.909230,-3.211032,3.292788,5.543726,5.406696,7.124841,4.918182,4.491478,-3.111130,-4.371000,7.976658,-3.097266,6.801831,6.782057,-4.870015,8.013640,-7.367189,-1.815783,-7.425998,8.363666,-7.074821,9.386759,0.155487,-3.625916,-3.092771,6.450578,3.967218,-1.520350,-5.940759,-6.524476,9.149813,-6.982071,9.283283,1.141412,-2.183209,4.829985,3.464168,8.761924,-3.842141,-6.222750,-0.185289,-9.679692,5.412754,-5.881631,-0.277783,4.280078,-1.926013,-5.808398,-6.889466,-6.490796,-8.385445,0.381510,-0.110520,-6.904692,3.579181,6.754915,4.537891,6.307404,8.062333,-2.187674,-9.756417,0.606556,2.948050,0.883352,-2.451936,2.202305,9.987222,-8.818411,7.034608,-6.160407,-5.816144,-2.191717,-0.834116,-6.054862,-5.642160,5.717021,-7.798026,9.820009,-2.478460,9.372960,-2.960690,-1.041608,-3.367320,5.378711,7.775932,-0.577066,-1.274078,7.513632,-5.183363,-0.824022,7.357988,-5.575962,-1.045178,2.767847,-4.665855,1.882608,8.583881,-3.070428,6.582202,5.160109,-8.136715,-5.257296,5.428315,6.131947,1.889940,-2.686034,7.296885,0.178828,-9.537325,5.942625,0.204858,-3.691848,-8.667219,-5.095919,-6.738672,-3.277914,5.172001,1.903450,9.433237,4.335486,-2.786208,0.537739,-2.356235,-9.805056,0.382067,8.192291,-6.649035,-0.960714,-7.833287,-4.836486,-7.794473,3.704935,9.630876,-2.839769,8.594144,-4.312044,6.856499,-2.130316,-5.353844,6.084745,-0.868128,-2.182205,-0.942684,5.828572,-2.839882,0.598924,-2.746231,-5.674507,-8.418071,-5.533747,-8.127709,6.759347,-9.695338,2.980021,-4.850004,6.784318,9.785775,-5.932631,-6.385673,9.961554,6.710193,1.200331,6.167731,-3.302722,8.981923,-6.180880,7.786834,5.474826,6.064947,-2.602985,5.728445,-7.563854,2.590783,-8.211397,-2.603778,-4.599402,7.145174,9.200784,-7.119846,-2.705782,5.538829,0.676055,-7.237259,-0.288706,-5.137145,-9.311494,-7.530249,-0.608061,5.530692,2.314937,-7.080253,9.475746,-8.340667,0.948622,-5.925707,-4.837360,-7.764194,-1.603603,-7.867159,-8.488718,7.028056,1.275615,1.016122,-2.313285,-8.147056,-6.232434,7.840386,-3.191977,-2.665923,-0.674276,3.067208,-7.174132,7.143400,4.632154,-9.155870,-1.813390,-3.901658,6.389532,5.894514,-6.250121,-7.649467,9.085715,-6.872689,2.662418,6.242128,-1.415722,-0.353020,-2.490180,6.987617,0.129164,1.727275,-8.880300,8.722967,7.352187,0.134072,9.224896,-2.446834,3.795499,-4.611658,3.020654,8.730331,4.738836,2.971321,2.943603,7.283212,-9.014357,-1.226519,-7.491664,-4.568878,-8.588103,7.205784,6.278160,-3.232010,-6.030835,4.471907,-0.942630,7.847617,-6.465190,5.848849,-4.877392,3.656938,7.634675,9.818587,6.500139,3.346788,2.185414,1.374494,-6.736887,2.923290,9.598171,7.760508,9.397631,9.174046,8.533144,0.982567,4.742241,-0.055347,-5.770284,-0.029076,0.691053,-0.463823,-0.400620,-7.701441,2.670246,4.770891,-1.520419,8.284241,-7.240007,-3.331767,8.519720,3.193298,-0.141492,-8.549604,9.799443,-2.950637,-3.688292,3.502523,0.987373,-4.636877,2.430577,1.202792,-4.822977,-8.125218,8.247598,-2.268718,-0.636818,4.201465,4.818111,-5.899249,-3.693018,7.451522,7.424889,9.834533,-8.919027,3.675183,5.340530,-1.243052,4.177345,-4.742674,0.541831,-7.539495,-5.678297,-3.480294,9.134827,-9.119887,5.229311,-6.944702,-7.621454,3.020394,7.956562,4.366463,1.370328,-8.686410,-7.776668,0.722345,4.527117,2.303235,5.908642,5.060936,-7.347333,-8.118653,-9.028523,-0.477764,-9.760830,1.887127,5.993873,1.196672,-8.623229,2.232961,-2.561273,-5.250510,-8.678785,-8.511523,6.447407,-6.229046,7.604775,-1.654538,-0.989483,3.125033,-8.649985,-0.466382,1.110273,7.675632,-0.140881,-6.235667,3.531805,-6.281268,-5.038420,-1.064478,9.673419,-1.606115,5.652072,-9.098085,3.763126,5.662637,-6.018852,6.347685,0.759683,-4.273236,-6.562628,-4.524114,1.740627,2.614166,0.051073,-5.584984,7.332991,-9.635386,3.532995,-4.338822,-7.620886,-1.774443,9.701461,-6.858323,-2.334881,-3.802907,0.294251,4.565685,-1.706517,-0.084503,-6.611255,-4.520978,1.916764,-8.326560,2.633585,-6.964827,-1.116838,-1.779477,-2.141760,-7.579066,4.263841,1.221993,-4.138515,-2.464334,-2.408104,-0.439255,3.220846,-2.646825,5.785550,4.939744,1.475491,-7.032869,-6.242261,2.926435,4.516130,-9.499978,6.537859,5.132596,-3.175398,-4.054686,9.729263,5.374399,9.485303,8.144130,-8.378775,1.371928,-0.272438,-8.264985,-1.593420,-0.223798,4.985656,2.689750,-5.934593,-6.517737,-3.659808,2.419102,-2.557560,-5.417135,-9.920710,-5.246600,-3.410509,-9.763630,-1.577936,2.358827,9.686025,-0.768218,-6.891806,9.851181,2.698551,8.380769,-1.473149,9.470883,5.530263,-9.217787,2.871504,6.758061,-8.815806,0.205337,-7.886342,1.749349,-9.011393,-0.337207,3.808311,3.299724,-5.039190,-4.674825,-1.362348,3.485062,5.730523,7.716998,-6.669597,-8.701071,0.498750,3.194786,6.200338,5.204701,5.619875,-3.242846,4.212478,1.000067,4.108230,-6.372346,3.449869,3.310407,9.268282,3.944737,9.773807,-5.459051,0.952857,-5.016144,-7.696451,-5.815031,-9.308469,7.348420,8.489075,0.153145,-1.911597,-4.391769,3.213322,3.816276,-5.853739,-5.373644,-1.226189,-3.417451,1.456812,-1.339256,-4.726171,5.860706,-4.803837,-6.232399,9.874382,-8.890469,4.470616,5.708995,-8.437573,4.963804,9.119942,5.904790,-7.230132,-5.077196,-5.096870,-5.056791,1.404033,6.184465,-3.123317,3.202353,9.479467,6.370249,-7.960031,0.303857,1.196735,-7.287491,7.277321,0.345847,9.524319,7.057302,-8.909128,5.298964,0.509318,2.056728,-6.515209,0.070656,-5.746085,0.130273,5.267249], dtype = "float32")#candidate|10913|(770,)|const|float32
call_10912 = func_2410_call(relay.reshape(const_10913.astype('float32'), [11, 14, 5]))
call_10914 = func_2410_call(relay.reshape(const_10913.astype('float32'), [11, 14, 5]))
output = relay.Tuple([uop_10895,call_10907,var_10908,var_10909,var_10910,call_10912,const_10913,])
output2 = relay.Tuple([uop_10895,call_10911,var_10908,var_10909,var_10910,call_10914,const_10913,])
func_10927 = relay.Function([var_10894,var_10908,var_10909,var_10910,], output)
mod['func_10927'] = func_10927
mod = relay.transform.InferType()(mod)
mutated_mod['func_10927'] = func_10927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10927_call = mutated_mod.get_global_var('func_10927')
var_10929 = relay.var("var_10929", dtype = "float32", shape = (7, 14, 9))#candidate|10929|(7, 14, 9)|var|float32
var_10930 = relay.var("var_10930", dtype = "float32", shape = (2475,))#candidate|10930|(2475,)|var|float32
var_10931 = relay.var("var_10931", dtype = "float32", shape = (3360,))#candidate|10931|(3360,)|var|float32
var_10932 = relay.var("var_10932", dtype = "float32", shape = (336,))#candidate|10932|(336,)|var|float32
call_10928 = func_10927_call(var_10929,var_10930,var_10931,var_10932,)
output = call_10928
func_10933 = relay.Function([var_10929,var_10930,var_10931,var_10932,], output)
mutated_mod['func_10933'] = func_10933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_10944 = func_1716_call()
call_10945 = func_1716_call()
func_5240_call = mod.get_global_var('func_5240')
func_5245_call = mutated_mod.get_global_var('func_5245')
const_10952 = relay.const([[-9.281547,2.493798,-0.132042,7.015469,-4.153721,-8.927541,-3.172181,-6.977961,-4.277648,-0.172564,6.205918,-3.536593,2.845719,-9.214062],[8.061024,8.941334,5.669547,0.177565,-6.183884,-4.024010,0.875480,-0.790097,5.191289,-2.544570,5.194156,4.242726,7.154967,8.891029],[4.582190,2.213873,3.651410,0.083353,7.352666,-8.918395,1.242932,-5.420695,-8.938130,-4.029414,-5.159180,6.887138,-3.728111,-3.376993],[-3.526565,-2.302600,-4.006111,1.368175,-9.145324,-5.816216,3.152515,-8.503647,2.649875,9.924700,4.842877,-1.528722,-0.181548,1.285877],[-3.756256,2.397880,2.731293,5.166186,6.823898,1.280563,8.571184,5.271755,2.425207,0.307966,-2.155369,-7.086908,5.706890,3.405552],[-2.930694,-1.475283,3.695850,-5.707218,3.422740,-2.945454,-0.666956,-9.017863,9.603721,-4.201324,8.998486,-1.102779,8.498426,-3.233845],[6.230140,-1.256112,-9.628714,-4.841410,-0.960993,1.277002,-3.641568,-9.352366,3.605279,-1.334367,-9.052302,6.763367,2.877419,-9.506596],[-3.536025,4.600719,-4.147571,-8.492026,-5.957674,-4.744240,2.877692,-6.233785,4.632447,-9.380906,8.214059,-0.865795,8.316649,-2.481621],[2.059097,7.398897,6.389918,5.760474,0.497372,-9.423866,-3.737562,-8.943625,-3.676083,-0.133817,-4.807139,0.061049,3.092301,1.191375],[4.447960,1.488445,-5.427407,3.146898,8.149804,-4.034989,-3.238229,-4.439527,2.109677,-0.992932,1.103162,-1.729019,6.725014,-1.981317],[3.439104,4.842353,8.652323,2.379887,-2.220081,6.893469,6.442721,-8.630077,-8.342003,-7.680035,9.346216,-3.011064,1.842800,-3.751502],[-1.884413,-7.654580,3.157501,-8.468567,-9.666331,-8.564633,-2.768298,5.914750,2.371738,5.764751,-2.327374,-3.576402,-6.478249,1.282254],[4.315462,-4.466163,-1.435809,3.975063,2.849357,-1.966327,2.172687,-9.505395,-4.863401,2.076006,1.489203,3.236595,-3.841036,3.992512],[-7.504489,9.039560,5.216317,0.945832,-1.328618,5.499464,1.108541,7.224766,-2.945153,-4.862525,0.550281,5.800548,8.925653,7.481094],[-6.863161,-6.685488,7.787879,-9.132980,-6.899878,-1.493395,-9.250180,-9.468856,0.230368,-7.925846,9.915260,-1.608243,-4.011017,2.961878],[-8.425809,0.477238,6.884890,-0.151172,9.336734,2.790872,-9.028746,-7.314488,0.455509,-3.693743,4.702748,0.313040,-6.437244,1.118490],[1.523621,-2.928496,5.041786,-6.798675,8.135039,3.225062,7.545256,-2.485272,-3.801120,-7.247653,1.447227,-5.202550,3.154261,2.436427],[2.741022,-7.184344,1.547567,8.612456,-2.942526,-5.627374,-2.485513,9.516146,-5.763827,5.568295,-8.856006,1.593572,3.001065,-0.699681],[9.432035,-3.596659,6.226843,0.741205,9.552131,5.222216,-3.205752,8.687144,-9.380813,-2.320623,9.982481,5.382774,3.080663,0.303697],[8.949717,8.168601,-9.703148,5.882684,-0.871267,-7.564963,6.741522,4.099267,1.695023,-8.616548,8.369569,9.056187,5.348721,5.182184],[1.453450,2.223707,-1.136676,1.137988,-3.281575,-1.517396,6.936198,-0.095761,7.001796,-1.620268,-1.867873,-1.133474,4.342532,-5.227067],[-4.846653,8.526365,4.157888,-6.931340,3.448729,-1.034398,4.657043,-5.852934,1.476868,4.493506,-9.787915,-2.536712,6.213782,2.843770],[-5.245989,4.136905,9.994982,-0.799197,0.661071,-0.087331,-8.929221,-6.705934,-0.517862,-2.106133,0.572140,-9.770058,6.927927,-7.108684],[6.683611,0.213043,-8.050157,-1.607816,1.634023,-2.557911,-4.415349,0.466039,7.718153,-4.756578,-8.238440,8.394750,-1.730431,9.361380]], dtype = "float32")#candidate|10952|(24, 14)|const|float32
var_10953 = relay.var("var_10953", dtype = "uint32", shape = (220,))#candidate|10953|(220,)|var|uint32
call_10951 = relay.TupleGetItem(func_5240_call(relay.reshape(const_10952.astype('float32'), [336,]), relay.reshape(call_10944.astype('float32'), [770,]), relay.reshape(var_10953.astype('uint32'), [220,]), ), 2)
call_10954 = relay.TupleGetItem(func_5245_call(relay.reshape(const_10952.astype('float32'), [336,]), relay.reshape(call_10944.astype('float32'), [770,]), relay.reshape(var_10953.astype('uint32'), [220,]), ), 2)
var_10975 = relay.var("var_10975", dtype = "float32", shape = (24, 14))#candidate|10975|(24, 14)|var|float32
bop_10976 = relay.subtract(const_10952.astype('int16'), relay.reshape(var_10975.astype('int16'), relay.shape_of(const_10952))) # shape=(24, 14)
output = relay.Tuple([call_10944,call_10951,var_10953,bop_10976,])
output2 = relay.Tuple([call_10945,call_10954,var_10953,bop_10976,])
F = relay.Function([var_10953,var_10975,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10953,var_10975,], output2)
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
