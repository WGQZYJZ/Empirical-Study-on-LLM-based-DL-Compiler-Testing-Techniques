import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_388 = relay.var("var_388", dtype = "float32", shape = (6, 6, 2))#candidate|388|(6, 6, 2)|var|float32
uop_389 = relay.cosh(var_388.astype('float32')) # shape=(6, 6, 2)
output = relay.Tuple([uop_389,])
output2 = relay.Tuple([uop_389,])
func_399 = relay.Function([var_388,], output)
mod['func_399'] = func_399
mod = relay.transform.InferType()(mod)
var_400 = relay.var("var_400", dtype = "float32", shape = (6, 6, 2))#candidate|400|(6, 6, 2)|var|float32
output = func_399(var_400)
func_401 = relay.Function([var_400], output)
mutated_mod['func_401'] = func_401
mutated_mod = relay.transform.InferType()(mutated_mod)
const_575 = relay.const([[[-8.317311],[6.796213],[2.888760],[-9.140687],[-6.490687],[-9.762048],[-9.439997],[9.323656],[7.745292],[6.430727],[-2.410349],[-4.798393],[0.491773],[8.434615],[4.748246]],[[0.157730],[5.409349],[2.329369],[-0.774474],[-4.060186],[-9.949219],[4.069509],[-6.444248],[-2.665681],[7.892240],[3.260368],[7.937200],[4.725487],[0.351473],[-2.577400]],[[9.637675],[5.617034],[-4.696838],[1.142145],[-4.778981],[-5.733069],[0.240229],[7.352225],[-6.501645],[8.559756],[4.397027],[0.789184],[-7.150494],[6.921265],[-8.338448]],[[6.583939],[-7.525175],[-7.543827],[1.931130],[8.281873],[-9.398931],[-8.094733],[6.634864],[4.709281],[3.098788],[9.886244],[2.844298],[-9.816881],[2.067137],[7.152644]],[[9.485109],[-4.052076],[0.105477],[-9.670702],[-3.183882],[6.679686],[8.318184],[-7.826527],[9.083118],[8.716554],[3.230424],[-5.882000],[3.607167],[-6.325139],[-0.278645]],[[-4.953946],[-1.858314],[8.650449],[-8.022352],[-1.966741],[-9.854816],[4.510594],[-3.992876],[-9.789091],[5.876439],[-8.733101],[5.543884],[6.689674],[4.220296],[6.833561]],[[1.855936],[4.850122],[-9.108527],[-3.164569],[9.206020],[-2.515508],[-7.172900],[7.398577],[3.648596],[-9.831468],[4.689044],[9.625925],[0.513018],[-6.319761],[0.924086]]], dtype = "float32")#candidate|575|(7, 15, 1)|const|float32
const_576 = relay.const([[[-2.455389],[0.945097],[-1.290326],[-6.086188],[-6.613217],[-3.694100],[0.656439],[-1.324064],[-1.358990],[-7.956353],[-2.564207],[-1.947508],[8.975512],[-9.575593],[8.125194]],[[0.774262],[-1.013048],[-9.482377],[0.967594],[4.277686],[5.401316],[-5.385098],[5.274372],[-2.411082],[-2.448702],[-0.515691],[5.782462],[0.861740],[-4.423585],[0.512695]],[[-0.565632],[9.956843],[3.821950],[6.490578],[-2.025662],[5.966206],[3.395084],[-5.587190],[-5.568936],[-1.033932],[-2.731524],[1.785950],[-0.311661],[-8.432365],[-6.140407]],[[-1.217652],[-7.192633],[9.990126],[8.311166],[9.033779],[6.873952],[2.305545],[-2.167034],[-1.776859],[-4.010515],[5.230147],[8.858009],[-5.811478],[-6.220468],[-2.025421]],[[-1.100656],[3.607654],[-2.149625],[8.892252],[9.453948],[-7.411531],[5.646967],[5.305253],[7.169717],[-3.591287],[9.630326],[-9.316260],[-7.021296],[-5.955068],[5.727148]],[[8.760792],[6.867108],[5.721897],[-8.982528],[3.441192],[6.662284],[-9.306771],[9.424140],[-4.529871],[5.348233],[-9.897767],[-3.014245],[9.781828],[-8.897640],[0.113820]],[[-9.144904],[1.752758],[1.534569],[-7.617147],[2.339705],[-0.765966],[3.043053],[6.863186],[-1.532204],[4.385895],[-5.835701],[-6.915366],[8.203998],[7.522257],[8.960129]]], dtype = "float32")#candidate|576|(7, 15, 1)|const|float32
bop_577 = relay.mod(const_575.astype('float32'), relay.reshape(const_576.astype('float32'), relay.shape_of(const_575))) # shape=(7, 15, 1)
output = bop_577
output2 = bop_577
func_580 = relay.Function([], output)
mod['func_580'] = func_580
mod = relay.transform.InferType()(mod)
mutated_mod['func_580'] = func_580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mutated_mod.get_global_var('func_580')
call_581 = func_580_call()
output = call_581
func_582 = relay.Function([], output)
mutated_mod['func_582'] = func_582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_648 = func_580_call()
call_649 = func_580_call()
var_655 = relay.var("var_655", dtype = "float32", shape = (7, 15, 6))#candidate|655|(7, 15, 6)|var|float32
bop_656 = relay.right_shift(call_648.astype('int32'), var_655.astype('int32')) # shape=(7, 15, 6)
bop_659 = relay.right_shift(call_649.astype('int32'), var_655.astype('int32')) # shape=(7, 15, 6)
output = relay.Tuple([bop_656,])
output2 = relay.Tuple([bop_659,])
func_668 = relay.Function([var_655,], output)
mod['func_668'] = func_668
mod = relay.transform.InferType()(mod)
var_669 = relay.var("var_669", dtype = "float32", shape = (7, 15, 6))#candidate|669|(7, 15, 6)|var|float32
output = func_668(var_669)
func_670 = relay.Function([var_669], output)
mutated_mod['func_670'] = func_670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_674 = func_580_call()
call_675 = func_580_call()
output = call_674
output2 = call_675
func_678 = relay.Function([], output)
mod['func_678'] = func_678
mod = relay.transform.InferType()(mod)
output = func_678()
func_679 = relay.Function([], output)
mutated_mod['func_679'] = func_679
mutated_mod = relay.transform.InferType()(mutated_mod)
var_740 = relay.var("var_740", dtype = "float64", shape = (4, 9, 14))#candidate|740|(4, 9, 14)|var|float64
var_741 = relay.var("var_741", dtype = "float64", shape = (4, 9, 14))#candidate|741|(4, 9, 14)|var|float64
bop_742 = relay.power(var_740.astype('float64'), relay.reshape(var_741.astype('float64'), relay.shape_of(var_740))) # shape=(4, 9, 14)
output = relay.Tuple([bop_742,])
output2 = relay.Tuple([bop_742,])
func_748 = relay.Function([var_740,var_741,], output)
mod['func_748'] = func_748
mod = relay.transform.InferType()(mod)
mutated_mod['func_748'] = func_748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_748_call = mutated_mod.get_global_var('func_748')
var_750 = relay.var("var_750", dtype = "float64", shape = (4, 9, 14))#candidate|750|(4, 9, 14)|var|float64
var_751 = relay.var("var_751", dtype = "float64", shape = (4, 9, 14))#candidate|751|(4, 9, 14)|var|float64
call_749 = func_748_call(var_750,var_751,)
output = call_749
func_752 = relay.Function([var_750,var_751,], output)
mutated_mod['func_752'] = func_752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_810 = func_580_call()
call_811 = func_580_call()
func_678_call = mod.get_global_var('func_678')
func_679_call = mutated_mod.get_global_var('func_679')
call_813 = func_678_call()
call_814 = func_678_call()
output = relay.Tuple([call_810,call_813,])
output2 = relay.Tuple([call_811,call_814,])
func_815 = relay.Function([], output)
mod['func_815'] = func_815
mod = relay.transform.InferType()(mod)
output = func_815()
func_816 = relay.Function([], output)
mutated_mod['func_816'] = func_816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_678_call = mod.get_global_var('func_678')
func_679_call = mutated_mod.get_global_var('func_679')
call_948 = func_678_call()
call_949 = func_678_call()
uop_955 = relay.sigmoid(call_948.astype('float32')) # shape=(7, 15, 1)
uop_957 = relay.sigmoid(call_949.astype('float32')) # shape=(7, 15, 1)
output = relay.Tuple([uop_955,])
output2 = relay.Tuple([uop_957,])
func_962 = relay.Function([], output)
mod['func_962'] = func_962
mod = relay.transform.InferType()(mod)
mutated_mod['func_962'] = func_962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_962_call = mutated_mod.get_global_var('func_962')
call_963 = func_962_call()
output = call_963
func_964 = relay.Function([], output)
mutated_mod['func_964'] = func_964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_678_call = mod.get_global_var('func_678')
func_679_call = mutated_mod.get_global_var('func_679')
call_968 = func_678_call()
call_969 = func_678_call()
uop_986 = relay.exp(call_968.astype('float32')) # shape=(7, 15, 1)
uop_988 = relay.exp(call_969.astype('float32')) # shape=(7, 15, 1)
uop_998 = relay.rsqrt(uop_986.astype('float64')) # shape=(7, 15, 1)
uop_1000 = relay.rsqrt(uop_988.astype('float64')) # shape=(7, 15, 1)
output = uop_998
output2 = uop_1000
func_1015 = relay.Function([], output)
mod['func_1015'] = func_1015
mod = relay.transform.InferType()(mod)
output = func_1015()
func_1016 = relay.Function([], output)
mutated_mod['func_1016'] = func_1016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_678_call = mod.get_global_var('func_678')
func_679_call = mutated_mod.get_global_var('func_679')
call_1054 = func_678_call()
call_1055 = func_678_call()
func_962_call = mod.get_global_var('func_962')
func_964_call = mutated_mod.get_global_var('func_964')
call_1057 = relay.TupleGetItem(func_962_call(), 0)
call_1058 = relay.TupleGetItem(func_964_call(), 0)
func_399_call = mod.get_global_var('func_399')
func_401_call = mutated_mod.get_global_var('func_401')
var_1063 = relay.var("var_1063", dtype = "float32", shape = (72,))#candidate|1063|(72,)|var|float32
call_1062 = relay.TupleGetItem(func_399_call(relay.reshape(var_1063.astype('float32'), [6, 6, 2])), 0)
call_1064 = relay.TupleGetItem(func_401_call(relay.reshape(var_1063.astype('float32'), [6, 6, 2])), 0)
output = relay.Tuple([call_1054,call_1057,call_1062,var_1063,])
output2 = relay.Tuple([call_1055,call_1058,call_1064,var_1063,])
func_1068 = relay.Function([var_1063,], output)
mod['func_1068'] = func_1068
mod = relay.transform.InferType()(mod)
mutated_mod['func_1068'] = func_1068
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1069 = relay.var("var_1069", dtype = "float32", shape = (72,))#candidate|1069|(72,)|var|float32
func_1068_call = mutated_mod.get_global_var('func_1068')
call_1070 = func_1068_call(var_1069)
output = call_1070
func_1071 = relay.Function([var_1069], output)
mutated_mod['func_1071'] = func_1071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_816_call = mutated_mod.get_global_var('func_816')
call_1073 = relay.TupleGetItem(func_815_call(), 1)
call_1074 = relay.TupleGetItem(func_816_call(), 1)
uop_1077 = relay.log2(call_1073.astype('float64')) # shape=(7, 15, 1)
uop_1079 = relay.log2(call_1074.astype('float64')) # shape=(7, 15, 1)
func_678_call = mod.get_global_var('func_678')
func_679_call = mutated_mod.get_global_var('func_679')
call_1082 = func_678_call()
call_1083 = func_678_call()
func_815_call = mod.get_global_var('func_815')
func_816_call = mutated_mod.get_global_var('func_816')
call_1088 = relay.TupleGetItem(func_815_call(), 0)
call_1089 = relay.TupleGetItem(func_816_call(), 0)
bop_1097 = relay.logical_and(uop_1077.astype('bool'), relay.reshape(call_1088.astype('bool'), relay.shape_of(uop_1077))) # shape=(7, 15, 1)
bop_1100 = relay.logical_and(uop_1079.astype('bool'), relay.reshape(call_1089.astype('bool'), relay.shape_of(uop_1079))) # shape=(7, 15, 1)
func_962_call = mod.get_global_var('func_962')
func_964_call = mutated_mod.get_global_var('func_964')
call_1106 = relay.TupleGetItem(func_962_call(), 0)
call_1107 = relay.TupleGetItem(func_964_call(), 0)
output = relay.Tuple([call_1082,bop_1097,call_1106,])
output2 = relay.Tuple([call_1083,bop_1100,call_1107,])
func_1110 = relay.Function([], output)
mod['func_1110'] = func_1110
mod = relay.transform.InferType()(mod)
mutated_mod['func_1110'] = func_1110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1110_call = mutated_mod.get_global_var('func_1110')
call_1111 = func_1110_call()
output = call_1111
func_1112 = relay.Function([], output)
mutated_mod['func_1112'] = func_1112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_962_call = mod.get_global_var('func_962')
func_964_call = mutated_mod.get_global_var('func_964')
call_1128 = relay.TupleGetItem(func_962_call(), 0)
call_1129 = relay.TupleGetItem(func_964_call(), 0)
func_668_call = mod.get_global_var('func_668')
func_670_call = mutated_mod.get_global_var('func_670')
var_1140 = relay.var("var_1140", dtype = "float32", shape = (70, 9))#candidate|1140|(70, 9)|var|float32
call_1139 = relay.TupleGetItem(func_668_call(relay.reshape(var_1140.astype('float32'), [7, 15, 6])), 0)
call_1141 = relay.TupleGetItem(func_670_call(relay.reshape(var_1140.astype('float32'), [7, 15, 6])), 0)
output = relay.Tuple([call_1128,call_1139,var_1140,])
output2 = relay.Tuple([call_1129,call_1141,var_1140,])
func_1146 = relay.Function([var_1140,], output)
mod['func_1146'] = func_1146
mod = relay.transform.InferType()(mod)
var_1147 = relay.var("var_1147", dtype = "float32", shape = (70, 9))#candidate|1147|(70, 9)|var|float32
output = func_1146(var_1147)
func_1148 = relay.Function([var_1147], output)
mutated_mod['func_1148'] = func_1148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_1177 = func_1015_call()
call_1178 = func_1015_call()
var_1198 = relay.var("var_1198", dtype = "float64", shape = (7, 15, 11))#candidate|1198|(7, 15, 11)|var|float64
bop_1199 = relay.add(call_1177.astype('uint32'), var_1198.astype('uint32')) # shape=(7, 15, 11)
bop_1202 = relay.add(call_1178.astype('uint32'), var_1198.astype('uint32')) # shape=(7, 15, 11)
func_668_call = mod.get_global_var('func_668')
func_670_call = mutated_mod.get_global_var('func_670')
const_1204 = relay.const([3.681111,-7.936395,-7.209828,0.186395,4.833975,-2.927758,9.159455,1.440975,-8.946127,5.262614,-7.007983,9.721142,-1.766096,8.011532,1.577545,-5.590048,-7.959104,-0.677264,-1.766647,7.638591,2.496314,4.746804,5.085341,3.268360,-0.584286,-3.721894,4.797611,-9.968029,-2.901860,-6.703137,4.783343,-0.789722,7.016612,-9.430447,-2.277566,-2.550071,3.748481,-1.998463,-4.683782,-7.719302,-9.844395,7.576136,-9.959095,8.868471,5.448191,7.302893,-9.375581,-5.410120,-0.845912,7.983924,-0.478178,-6.012792,0.952440,-2.400907,-2.988739,-6.597199,6.719803,4.444157,-3.030753,-1.238375,-4.684912,-7.399300,7.751707,-5.221109,1.071394,-4.314270,5.455955,6.910780,0.018165,-4.754939,7.883127,4.916388,-9.360575,-0.397962,8.370898,-7.072475,-6.258289,2.500646,-1.667816,-8.231031,2.498277,2.552446,6.931830,-9.282843,0.469836,2.278161,1.970142,5.485588,1.720487,-7.323016,3.372639,-1.910700,2.324171,7.693753,5.859878,8.506960,3.972108,-0.500605,-2.393685,3.217415,1.644241,-6.360897,4.122284,1.584833,9.912317,-8.086359,-6.795533,3.980684,-2.920246,4.191960,-0.480466,-7.512727,-9.871747,-7.226402,3.256745,-5.746300,-7.776723,-8.455812,-4.701733,-3.501480,5.425521,-9.683433,1.950382,-7.155628,2.653207,-8.432762,-1.224230,3.483464,7.559841,1.418366,5.624906,6.346666,-5.720665,-1.504675,9.363563,1.241731,7.965870,6.300809,9.616618,-1.875958,8.724607,-9.817959,7.103043,-8.220827,6.507433,-3.609141,5.540977,0.958392,2.090502,2.180168,-5.167417,0.044378,-1.000900,5.869164,-2.928391,-6.780643,-6.113846,-4.064938,-6.420513,-4.119849,-2.199820,7.325704,-0.005331,-6.657063,-9.852256,3.941418,-4.470769,-1.902819,8.306187,-1.619300,1.470387,1.822616,2.969558,4.883759,0.710334,3.617368,-5.490979,1.482622,9.625315,-6.962205,1.919224,5.714431,3.373468,1.918501,8.440759,-9.832341,-2.292218,-3.797663,0.350743,-2.856490,9.132407,8.091375,-8.786734,-3.134047,-7.967350,8.650639,-3.038019,1.480215,-5.690846,-2.975935,-1.158336,-7.686800,6.323437,-2.869278,-9.383104,2.698831,-3.012252,-4.941002,5.515024,6.230458,3.043836,-6.891677,3.443801,3.176157,-0.171398,0.454051,9.641604,4.153252,-9.476719,0.436226,-7.851246,-9.442876,3.534234,9.469912,8.132782,-0.784677,0.864062,4.322503,-5.810080,-3.112173,-2.727743,1.623528,3.957408,-8.124874,-2.931794,0.283756,-0.979021,-8.641715,-3.906185,7.888769,-4.992817,-2.789553,-9.585398,-5.733046,4.029015,7.142373,-1.338298,8.652868,3.668239,9.598982,6.187763,5.742282,-8.420487,-5.111317,6.262651,-8.040514,5.553803,-9.293369,-3.387677,7.043534,4.543205,-5.917213,3.789112,-2.767130,2.744777,5.614096,-3.296144,6.282173,-4.260757,4.592059,1.838533,6.194318,-7.604530,-9.376762,-4.648374,-1.422293,-7.981258,1.356692,-0.759690,-9.891541,6.526096,6.057291,-2.748362,-3.615980,-8.694871,8.412218,5.596308,-8.832161,-3.023975,7.236369,-0.732816,-3.085572,-1.939201,8.143715,2.858308,-3.475849,7.992329,-8.711311,-9.033379,-0.102807,-6.456726,-6.766998,-6.730534,-2.760173,0.130761,8.389770,0.445823,-9.595252,5.640196,7.998022,-5.467972,7.519509,0.733282,1.185121,-2.158499,-9.810601,1.492480,-5.105727,8.541692,-7.627160,-6.732468,2.482669,-2.462372,9.711507,9.169098,-3.644557,2.984805,2.612004,-7.335967,-7.439162,-6.740674,6.347637,-3.931870,6.560616,-2.112779,-1.062549,8.727563,0.501522,-0.599824,7.407490,2.873701,5.679613,6.984473,2.856963,1.640639,-7.320206,-0.493407,-6.489337,7.596718,-7.117722,0.226442,3.025603,-1.809608,-1.344479,0.205597,-3.186928,-7.815757,7.837807,-6.243747,2.262455,8.945201,9.763359,7.200986,-7.881683,8.193458,9.280001,9.746952,4.800693,6.796005,-4.832415,4.625418,9.454254,-2.655795,8.903152,9.592594,2.448526,-3.063093,-5.251670,-7.368422,6.416193,1.254537,-2.430106,2.393024,2.768612,-4.459899,9.918586,-3.446614,6.609581,-0.808615,-0.079573,9.305473,-9.690182,-5.418514,8.612678,3.101804,0.845432,5.661514,0.323317,7.227715,6.361324,2.404779,-3.508125,1.951276,-5.177550,-6.484711,5.759239,-5.643257,-9.303354,-5.445826,1.058712,-3.287572,0.499938,6.029167,-4.219950,3.074159,-7.762326,-6.413547,-5.895273,-9.968822,5.589801,7.963333,-3.570710,-1.731634,2.334546,-0.968076,-2.022103,1.661163,0.631644,9.228919,7.287471,2.566800,0.576118,-4.245487,-7.020050,-9.911872,-8.574563,-7.959397,-6.335318,5.302439,-6.901779,-4.209139,-1.005119,-2.343429,-9.387378,1.039102,-1.796343,8.975616,-2.267975,5.369403,-3.444659,8.171204,-9.868293,2.652616,-0.246369,-6.393220,8.141396,-2.864181,-6.652675,0.292309,-8.755229,-5.760151,6.876397,-5.998313,-8.539024,-6.782411,9.045466,7.431129,-5.923391,-7.625925,4.318295,8.424343,-4.328977,-9.816409,-3.402516,2.126756,-4.259086,4.179228,-8.685631,2.705718,8.541338,3.823952,0.898444,-5.724888,-9.344502,1.126660,5.642946,-4.535211,-4.886603,-0.567121,-0.287629,3.070413,-7.584991,-5.012252,-8.404138,0.692258,-0.584980,-0.020487,9.728526,8.899859,-1.041792,3.876632,9.942786,3.484749,-0.709720,-5.318587,8.476881,2.643173,-1.620509,-4.982496,4.766307,-1.735955,9.566943,-6.142667,-7.079800,-1.758027,-2.299930,-3.661174,9.701124,0.323598,-6.845211,-4.396717,4.937866,4.200784,4.088533,-5.492378,1.382047,-9.782813,8.310778,9.201554,-7.023332,-2.796575,9.531429,-2.923685,-8.495706,-8.815222,8.990570,9.830177,-9.516345,-9.137607,-6.477126,-4.000716,-7.490218,-9.951398,0.904303,8.605068,8.227108,-6.826820,-7.388614,5.615193,-2.791374,1.627977,-2.478780,-8.162678,6.544268,3.841957,6.407578,8.254911,-1.904683,-3.771219,3.083793,-1.256616,3.214226,5.207316,0.533502,9.082940,-9.161587,-6.646874,4.505009,3.071717,8.033488,-5.777443,3.232831,-8.350320,-5.372577,3.287809,-0.892339,-7.767706,7.355453,-1.519465,0.142528,-7.098326,-3.831948,-0.588310,-4.189100,3.198810,-5.533078,-8.175770,9.865285,-0.164884,2.019222,-8.813100,9.741476,-8.034970,-7.781485,6.152318,-4.339178,-8.997928,-8.503438,-8.766717,-9.167221,3.582677,6.799091,-8.395450,-8.761989,-1.812794,9.980237,-6.234394,-5.168953,4.701208,5.075080,-9.910850,-8.075039,-2.445335,6.600089,2.560172,-3.344053,1.153390,7.363674,9.683991,-1.662423,9.168742,-8.742927,-8.288465,-5.377573,7.046527,-6.202461,8.484272,-9.106096,-9.267751,-3.460432], dtype = "float32")#candidate|1204|(630,)|const|float32
call_1203 = relay.TupleGetItem(func_668_call(relay.reshape(const_1204.astype('float32'), [7, 15, 6])), 0)
call_1205 = relay.TupleGetItem(func_670_call(relay.reshape(const_1204.astype('float32'), [7, 15, 6])), 0)
var_1218 = relay.var("var_1218", dtype = "uint32", shape = (7, 15, 11))#candidate|1218|(7, 15, 11)|var|uint32
bop_1219 = relay.minimum(bop_1199.astype('float64'), relay.reshape(var_1218.astype('float64'), relay.shape_of(bop_1199))) # shape=(7, 15, 11)
bop_1222 = relay.minimum(bop_1202.astype('float64'), relay.reshape(var_1218.astype('float64'), relay.shape_of(bop_1202))) # shape=(7, 15, 11)
func_1110_call = mod.get_global_var('func_1110')
func_1112_call = mutated_mod.get_global_var('func_1112')
call_1231 = relay.TupleGetItem(func_1110_call(), 2)
call_1232 = relay.TupleGetItem(func_1112_call(), 2)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_1241 = func_580_call()
call_1242 = func_580_call()
output = relay.Tuple([call_1203,const_1204,bop_1219,call_1231,call_1241,])
output2 = relay.Tuple([call_1205,const_1204,bop_1222,call_1232,call_1242,])
func_1248 = relay.Function([var_1198,var_1218,], output)
mod['func_1248'] = func_1248
mod = relay.transform.InferType()(mod)
mutated_mod['func_1248'] = func_1248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1248_call = mutated_mod.get_global_var('func_1248')
var_1250 = relay.var("var_1250", dtype = "float64", shape = (7, 15, 11))#candidate|1250|(7, 15, 11)|var|float64
var_1251 = relay.var("var_1251", dtype = "uint32", shape = (7, 15, 11))#candidate|1251|(7, 15, 11)|var|uint32
call_1249 = func_1248_call(var_1250,var_1251,)
output = call_1249
func_1252 = relay.Function([var_1250,var_1251,], output)
mutated_mod['func_1252'] = func_1252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_962_call = mod.get_global_var('func_962')
func_964_call = mutated_mod.get_global_var('func_964')
call_1257 = relay.TupleGetItem(func_962_call(), 0)
call_1258 = relay.TupleGetItem(func_964_call(), 0)
func_962_call = mod.get_global_var('func_962')
func_964_call = mutated_mod.get_global_var('func_964')
call_1261 = relay.TupleGetItem(func_962_call(), 0)
call_1262 = relay.TupleGetItem(func_964_call(), 0)
func_1110_call = mod.get_global_var('func_1110')
func_1112_call = mutated_mod.get_global_var('func_1112')
call_1270 = relay.TupleGetItem(func_1110_call(), 2)
call_1271 = relay.TupleGetItem(func_1112_call(), 2)
func_668_call = mod.get_global_var('func_668')
func_670_call = mutated_mod.get_global_var('func_670')
var_1273 = relay.var("var_1273", dtype = "float32", shape = (630,))#candidate|1273|(630,)|var|float32
call_1272 = relay.TupleGetItem(func_668_call(relay.reshape(var_1273.astype('float32'), [7, 15, 6])), 0)
call_1274 = relay.TupleGetItem(func_670_call(relay.reshape(var_1273.astype('float32'), [7, 15, 6])), 0)
bop_1275 = relay.bitwise_and(var_1273.astype('int16'), call_1257.astype('int16')) # shape=(7, 15, 630)
bop_1278 = relay.bitwise_and(var_1273.astype('int16'), call_1258.astype('int16')) # shape=(7, 15, 630)
func_399_call = mod.get_global_var('func_399')
func_401_call = mutated_mod.get_global_var('func_401')
const_1282 = relay.const([-1.152206,7.410576,-6.142927,-8.410797,0.466229,7.722594,-2.357582,8.238554,6.650060,1.699636,1.789494,-8.387483,1.067808,-9.719160,5.918762,-6.114831,6.823971,-0.433336,-3.767837,0.003444,-1.866266,7.569293,6.898219,0.695446,-5.879957,-1.360798,9.708018,-0.566515,-4.829879,9.420780,-6.115814,1.837563,-1.345545,3.147475,8.729973,-5.443643,-0.996089,-8.405677,-9.769540,-7.085783,3.482681,-6.694161,-3.271863,6.860973,1.766394,-0.693315,1.098145,6.365847,-5.974115,-0.595558,-2.824150,9.084582,-7.591039,-0.166855,2.872975,3.785169,-2.058701,4.757036,-9.399748,5.385384,-5.456837,7.712883,-3.782565,4.393478,-0.119534,-4.520217,-1.054708,5.285677,4.057416,9.974076,-3.851035,1.611414], dtype = "float32")#candidate|1282|(72,)|const|float32
call_1281 = relay.TupleGetItem(func_399_call(relay.reshape(const_1282.astype('float32'), [6, 6, 2])), 0)
call_1283 = relay.TupleGetItem(func_401_call(relay.reshape(const_1282.astype('float32'), [6, 6, 2])), 0)
bop_1284 = relay.floor_divide(var_1273.astype('float64'), call_1261.astype('float64')) # shape=(7, 15, 630)
bop_1287 = relay.floor_divide(var_1273.astype('float64'), call_1262.astype('float64')) # shape=(7, 15, 630)
uop_1296 = relay.rsqrt(call_1281.astype('float32')) # shape=(6, 6, 2)
uop_1298 = relay.rsqrt(call_1283.astype('float32')) # shape=(6, 6, 2)
bop_1303 = relay.equal(uop_1296.astype('bool'), relay.reshape(call_1281.astype('bool'), relay.shape_of(uop_1296))) # shape=(6, 6, 2)
bop_1306 = relay.equal(uop_1298.astype('bool'), relay.reshape(call_1283.astype('bool'), relay.shape_of(uop_1298))) # shape=(6, 6, 2)
func_748_call = mod.get_global_var('func_748')
func_752_call = mutated_mod.get_global_var('func_752')
const_1308 = relay.const([5.565010,-0.315310,-5.420312,-2.358980,8.267930,-4.397713,9.130212,7.454358,-3.009597,-5.226538,7.826228,-4.351744,-7.877888,2.648956,0.121398,-1.035864,-1.902446,1.394609,-1.768781,-4.556629,0.845353,4.910027,0.725868,9.577220,-8.535157,5.850122,-0.395707,-6.780067,9.591612,-9.767623,-4.961009,-3.795140,-8.459612,2.467550,8.435124,-0.761883,-9.737003,9.131442,-7.155375,-9.470403,-6.894867,-9.782823,8.677862,-5.348441,3.760678,3.507863,3.468322,-8.760664,-4.057224,-2.757532,0.301339,-6.092424,2.792602,-6.191955,6.903501,-4.371622,-8.765669,-9.965165,-0.586732,-6.814851,-6.491070,8.595994,5.187826,8.105884,7.455209,9.545395,-7.070638,1.301462,-3.636041,5.281739,-3.746719,9.538365,7.222174,-4.405535,-7.618614,2.210880,-7.649569,7.345918,-5.722834,4.389149,-6.444818,8.275598,9.892193,-0.729260,-3.163927,3.837653,-7.485167,3.742922,-3.195848,1.803917,-0.528744,3.070583,2.452858,2.263745,6.368408,9.825967,5.880753,-2.386341,2.103497,-5.250698,2.970607,-3.006691,6.309011,4.050422,6.526180,-5.430683,0.672102,6.415069,-8.220701,-6.171855,5.630689,-8.865577,-0.512653,1.104737,2.848214,4.320206,9.718323,-8.010341,4.818427,3.123448,-3.739664,5.270354,1.179320,-8.657674,0.283880,-1.391771,3.586498,8.223158,5.204067,0.999714,7.295074,4.172695,8.072455,6.890096,3.672089,4.184823,-6.174644,6.057454,4.729378,-0.224900,7.009175,-7.482986,3.383846,-0.419389,-8.004143,4.787297,3.707744,4.268673,1.170898,6.144439,9.140987,-8.604725,8.836877,5.529793,-1.023641,1.683750,-8.503892,-7.711141,-0.326715,4.315740,-3.670799,-4.736387,0.725122,-7.520111,-1.157936,-0.244266,0.018652,2.553263,-0.556826,4.925922,-6.961591,-5.182183,-6.705132,-5.567192,-8.828814,-7.107512,5.146047,-8.539797,-0.257036,0.264118,-5.097356,-1.972945,-9.341143,8.967346,-4.418806,6.203521,1.556320,-8.868620,-8.059282,-8.627540,-6.172005,-1.637037,4.343396,-7.673246,3.686789,-6.533664,3.326196,8.533859,0.704736,7.453077,-0.143629,-4.053734,-3.387026,3.840122,-9.551287,3.074731,-4.762583,-8.862108,-3.629415,0.913899,-6.857097,-4.188888,-6.074565,0.692918,-5.269234,-8.610364,-2.442413,-7.804677,8.722589,9.987585,-8.958806,-4.307641,-9.358612,-3.310108,2.459776,3.389620,-6.240633,-0.107284,6.048052,-8.507988,-4.292432,-9.555699,0.658700,7.249078,0.967560,-6.130641,-4.657856,-4.776177,4.885483,1.903235,9.402173,-2.902508,-1.570373,-4.951855,2.452433,6.771115,7.860312,-2.077156,6.948617,9.083247,-0.666096,-5.781972,-0.898151,-8.348678,4.251378,4.161276,-8.070689,-7.838312,-0.926848,-2.345150,6.746833,1.543804,-1.301431,-9.369720,3.160513,-9.846690,3.777255,-2.376546,4.657457,-5.736472,8.618064,8.640021,7.879548,-8.489915,1.447343,6.110042,6.548242,7.174163,-3.188650,3.605962,-4.267948,-1.663529,-5.307476,7.924921,7.243099,-9.147057,0.131356,-1.028297,-3.263790,-5.756756,7.457238,-3.090883,-8.853326,-8.688604,1.580442,3.251594,7.006638,-5.875023,-6.454193,-5.324694,9.406473,-0.611246,-0.902223,1.993538,-9.035585,-9.799938,-1.341794,-7.946852,0.147634,2.693818,-1.065710,-8.077163,-1.101272,9.658513,-6.982200,-0.803204,-2.103838,9.352914,0.674202,3.555063,-9.415966,-5.542670,6.788611,-8.177645,7.215112,6.557035,-7.390227,-5.895866,-4.727768,7.060511,7.435235,-0.455940,5.481940,-0.881229,8.395273,-6.071518,-2.777087,-9.271183,9.838794,-2.583495,-1.430825,-6.845699,4.785290,-4.598301,-8.834018,-7.793552,1.321421,4.721639,-5.795410,-3.170015,-9.914525,-6.418839,8.205337,-0.163113,1.239579,0.025874,-6.703691,-5.654933,-6.686506,-0.940635,-0.430852,-0.156283,3.540589,-6.619975,-8.731514,7.348563,8.757776,6.983327,-4.846382,5.170876,-3.517917,-8.868328,-9.551140,-8.821581,4.336244,4.493250,6.265959,8.560461,-1.691599,8.143276,-2.661575,7.032863,-7.065984,-8.181496,-0.455242,-0.370650,7.340212,0.991150,8.965319,-8.874675,-1.627400,-7.576795,-6.954721,3.027856,-2.677985,3.880360,1.146231,-8.397452,5.992865,7.988321,8.251167,-9.824585,-5.244629,-5.600758,7.956264,-5.473875,3.650639,9.441910,-1.919255,-9.567683,7.770074,-5.021611,-2.596597,-3.098236,1.112361,9.073907,0.759617,3.672498,8.112306,3.035598,4.421300,9.013803,4.483602,-7.342300,6.858825,-9.806610,-9.997999,3.992936,1.673270,-7.684746,1.423911,5.410981,3.230269,-9.735223,4.651064,8.981778,5.612572,1.626092,1.900613,1.567381,-2.105036,-7.528108,-0.949284,0.823614,8.817320,-8.588566,5.526998,-0.500215,7.264259,1.791929,-8.437915,9.949759,5.324279,-5.876025,-6.269439,3.889657,0.955228,3.061523,-8.163701,-5.918881,-5.551678,-4.786143,-8.664462,-1.444289,-6.926470,-0.963904,-5.951817,-9.753175,-8.649099,-1.671757,-4.892037,4.681623,9.387084,7.320833,2.887178,-5.785125,7.005114,8.469880,8.907853,9.650899,-2.014747,-6.820111,0.261272,-6.330137,-5.246316,-4.996018,3.070896,-4.925750,-7.732966,-3.207819,5.710662,8.750984,9.768043,7.293683,-2.998745,-8.974051,-7.610856,5.424992,-7.916223,-9.485784,-7.842471,4.308738,-8.423069,4.815276], dtype = "float64")#candidate|1308|(504,)|const|float64
call_1307 = relay.TupleGetItem(func_748_call(relay.reshape(const_1308.astype('float64'), [4, 9, 14]), relay.reshape(const_1308.astype('float64'), [4, 9, 14]), ), 0)
call_1309 = relay.TupleGetItem(func_752_call(relay.reshape(const_1308.astype('float64'), [4, 9, 14]), relay.reshape(const_1308.astype('float64'), [4, 9, 14]), ), 0)
output = relay.Tuple([call_1270,call_1272,bop_1275,const_1282,bop_1284,bop_1303,call_1307,const_1308,])
output2 = relay.Tuple([call_1271,call_1274,bop_1278,const_1282,bop_1287,bop_1306,call_1309,const_1308,])
func_1313 = relay.Function([var_1273,], output)
mod['func_1313'] = func_1313
mod = relay.transform.InferType()(mod)
mutated_mod['func_1313'] = func_1313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1314 = relay.var("var_1314", dtype = "float32", shape = (630,))#candidate|1314|(630,)|var|float32
func_1313_call = mutated_mod.get_global_var('func_1313')
call_1315 = func_1313_call(var_1314)
output = call_1315
func_1316 = relay.Function([var_1314], output)
mutated_mod['func_1316'] = func_1316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_1379 = func_580_call()
call_1380 = func_580_call()
output = call_1379
output2 = call_1380
func_1389 = relay.Function([], output)
mod['func_1389'] = func_1389
mod = relay.transform.InferType()(mod)
mutated_mod['func_1389'] = func_1389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1389_call = mutated_mod.get_global_var('func_1389')
call_1390 = func_1389_call()
output = call_1390
func_1391 = relay.Function([], output)
mutated_mod['func_1391'] = func_1391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_816_call = mutated_mod.get_global_var('func_816')
call_1403 = relay.TupleGetItem(func_815_call(), 0)
call_1404 = relay.TupleGetItem(func_816_call(), 0)
output = call_1403
output2 = call_1404
func_1409 = relay.Function([], output)
mod['func_1409'] = func_1409
mod = relay.transform.InferType()(mod)
output = func_1409()
func_1410 = relay.Function([], output)
mutated_mod['func_1410'] = func_1410
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1496 = relay.var("var_1496", dtype = "uint16", shape = (2, 13, 11))#candidate|1496|(2, 13, 11)|var|uint16
var_1497 = relay.var("var_1497", dtype = "uint16", shape = (2, 13, 11))#candidate|1497|(2, 13, 11)|var|uint16
bop_1498 = relay.right_shift(var_1496.astype('uint16'), relay.reshape(var_1497.astype('uint16'), relay.shape_of(var_1496))) # shape=(2, 13, 11)
func_1389_call = mod.get_global_var('func_1389')
func_1391_call = mutated_mod.get_global_var('func_1391')
call_1506 = func_1389_call()
call_1507 = func_1389_call()
output = relay.Tuple([bop_1498,call_1506,])
output2 = relay.Tuple([bop_1498,call_1507,])
func_1527 = relay.Function([var_1496,var_1497,], output)
mod['func_1527'] = func_1527
mod = relay.transform.InferType()(mod)
var_1528 = relay.var("var_1528", dtype = "uint16", shape = (2, 13, 11))#candidate|1528|(2, 13, 11)|var|uint16
var_1529 = relay.var("var_1529", dtype = "uint16", shape = (2, 13, 11))#candidate|1529|(2, 13, 11)|var|uint16
output = func_1527(var_1528,var_1529,)
func_1530 = relay.Function([var_1528,var_1529,], output)
mutated_mod['func_1530'] = func_1530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1110_call = mod.get_global_var('func_1110')
func_1112_call = mutated_mod.get_global_var('func_1112')
call_1565 = relay.TupleGetItem(func_1110_call(), 1)
call_1566 = relay.TupleGetItem(func_1112_call(), 1)
func_1110_call = mod.get_global_var('func_1110')
func_1112_call = mutated_mod.get_global_var('func_1112')
call_1584 = relay.TupleGetItem(func_1110_call(), 0)
call_1585 = relay.TupleGetItem(func_1112_call(), 0)
uop_1586 = relay.log(call_1584.astype('float32')) # shape=(7, 15, 1)
uop_1588 = relay.log(call_1585.astype('float32')) # shape=(7, 15, 1)
output = relay.Tuple([call_1565,uop_1586,])
output2 = relay.Tuple([call_1566,uop_1588,])
func_1590 = relay.Function([], output)
mod['func_1590'] = func_1590
mod = relay.transform.InferType()(mod)
mutated_mod['func_1590'] = func_1590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mutated_mod.get_global_var('func_1590')
call_1591 = func_1590_call()
output = call_1591
func_1592 = relay.Function([], output)
mutated_mod['func_1592'] = func_1592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1110_call = mod.get_global_var('func_1110')
func_1112_call = mutated_mod.get_global_var('func_1112')
call_1716 = relay.TupleGetItem(func_1110_call(), 1)
call_1717 = relay.TupleGetItem(func_1112_call(), 1)
uop_1756 = relay.erf(call_1716.astype('float64')) # shape=(7, 15, 1)
uop_1758 = relay.erf(call_1717.astype('float64')) # shape=(7, 15, 1)
output = relay.Tuple([uop_1756,])
output2 = relay.Tuple([uop_1758,])
func_1781 = relay.Function([], output)
mod['func_1781'] = func_1781
mod = relay.transform.InferType()(mod)
output = func_1781()
func_1782 = relay.Function([], output)
mutated_mod['func_1782'] = func_1782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1409_call = mod.get_global_var('func_1409')
func_1410_call = mutated_mod.get_global_var('func_1410')
call_1823 = func_1409_call()
call_1824 = func_1409_call()
output = call_1823
output2 = call_1824
func_1830 = relay.Function([], output)
mod['func_1830'] = func_1830
mod = relay.transform.InferType()(mod)
output = func_1830()
func_1831 = relay.Function([], output)
mutated_mod['func_1831'] = func_1831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_962_call = mod.get_global_var('func_962')
func_964_call = mutated_mod.get_global_var('func_964')
call_1834 = relay.TupleGetItem(func_962_call(), 0)
call_1835 = relay.TupleGetItem(func_964_call(), 0)
output = relay.Tuple([call_1834,])
output2 = relay.Tuple([call_1835,])
func_1842 = relay.Function([], output)
mod['func_1842'] = func_1842
mod = relay.transform.InferType()(mod)
mutated_mod['func_1842'] = func_1842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1842_call = mutated_mod.get_global_var('func_1842')
call_1843 = func_1842_call()
output = call_1843
func_1844 = relay.Function([], output)
mutated_mod['func_1844'] = func_1844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_1852 = func_1015_call()
call_1853 = func_1015_call()
uop_1860 = relay.log10(call_1852.astype('float32')) # shape=(7, 15, 1)
uop_1862 = relay.log10(call_1853.astype('float32')) # shape=(7, 15, 1)
output = relay.Tuple([uop_1860,])
output2 = relay.Tuple([uop_1862,])
func_1863 = relay.Function([], output)
mod['func_1863'] = func_1863
mod = relay.transform.InferType()(mod)
mutated_mod['func_1863'] = func_1863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1863_call = mutated_mod.get_global_var('func_1863')
call_1864 = func_1863_call()
output = call_1864
func_1865 = relay.Function([], output)
mutated_mod['func_1865'] = func_1865
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1874 = relay.var("var_1874", dtype = "bool", shape = (7, 5, 11))#candidate|1874|(7, 5, 11)|var|bool
var_1875 = relay.var("var_1875", dtype = "bool", shape = (7, 5, 11))#candidate|1875|(7, 5, 11)|var|bool
bop_1876 = relay.logical_or(var_1874.astype('bool'), relay.reshape(var_1875.astype('bool'), relay.shape_of(var_1874))) # shape=(7, 5, 11)
func_1110_call = mod.get_global_var('func_1110')
func_1112_call = mutated_mod.get_global_var('func_1112')
call_1882 = relay.TupleGetItem(func_1110_call(), 1)
call_1883 = relay.TupleGetItem(func_1112_call(), 1)
output = relay.Tuple([bop_1876,call_1882,])
output2 = relay.Tuple([bop_1876,call_1883,])
func_1890 = relay.Function([var_1874,var_1875,], output)
mod['func_1890'] = func_1890
mod = relay.transform.InferType()(mod)
mutated_mod['func_1890'] = func_1890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1890_call = mutated_mod.get_global_var('func_1890')
var_1892 = relay.var("var_1892", dtype = "bool", shape = (7, 5, 11))#candidate|1892|(7, 5, 11)|var|bool
var_1893 = relay.var("var_1893", dtype = "bool", shape = (7, 5, 11))#candidate|1893|(7, 5, 11)|var|bool
call_1891 = func_1890_call(var_1892,var_1893,)
output = call_1891
func_1894 = relay.Function([var_1892,var_1893,], output)
mutated_mod['func_1894'] = func_1894
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1930 = relay.var("var_1930", dtype = "float64", shape = (10, 8, 1))#candidate|1930|(10, 8, 1)|var|float64
uop_1931 = relay.asin(var_1930.astype('float64')) # shape=(10, 8, 1)
output = relay.Tuple([uop_1931,])
output2 = relay.Tuple([uop_1931,])
func_1944 = relay.Function([var_1930,], output)
mod['func_1944'] = func_1944
mod = relay.transform.InferType()(mod)
mutated_mod['func_1944'] = func_1944
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1945 = relay.var("var_1945", dtype = "float64", shape = (10, 8, 1))#candidate|1945|(10, 8, 1)|var|float64
func_1944_call = mutated_mod.get_global_var('func_1944')
call_1946 = func_1944_call(var_1945)
output = call_1946
func_1947 = relay.Function([var_1945], output)
mutated_mod['func_1947'] = func_1947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_678_call = mod.get_global_var('func_678')
func_679_call = mutated_mod.get_global_var('func_679')
call_2022 = func_678_call()
call_2023 = func_678_call()
func_399_call = mod.get_global_var('func_399')
func_401_call = mutated_mod.get_global_var('func_401')
const_2033 = relay.const([-6.007897,1.459132,5.817758,0.349703,5.908595,-2.049916,5.368211,-9.715236,4.402331,-0.443299,5.785890,4.983822,-4.748209,-7.394088,4.076444,-3.641686,-8.452315,-7.269161,8.401373,4.430326,4.725615,2.762318,9.960540,6.661200,3.126316,7.349658,-9.194452,-8.644177,8.062220,-8.265661,3.396573,-3.572991,-5.085895,5.614664,-4.323479,-9.099246,-5.013282,-1.546371,8.682732,8.102169,6.741561,0.190135,1.858487,-5.396848,1.961638,8.818401,-6.815939,-7.398253,-8.265755,-5.515066,-1.514278,-9.412507,-8.693711,-2.916150,-4.697037,1.675888,-5.601810,4.594825,-3.936551,-8.447997,-8.913169,4.001764,6.586812,-9.407138,1.191035,-3.511129,7.117215,6.497734,5.026752,-4.157772,4.743335,4.836291], dtype = "float32")#candidate|2033|(72,)|const|float32
call_2032 = relay.TupleGetItem(func_399_call(relay.reshape(const_2033.astype('float32'), [6, 6, 2])), 0)
call_2034 = relay.TupleGetItem(func_401_call(relay.reshape(const_2033.astype('float32'), [6, 6, 2])), 0)
func_815_call = mod.get_global_var('func_815')
func_816_call = mutated_mod.get_global_var('func_816')
call_2038 = relay.TupleGetItem(func_815_call(), 1)
call_2039 = relay.TupleGetItem(func_816_call(), 1)
output = relay.Tuple([call_2022,call_2032,const_2033,call_2038,])
output2 = relay.Tuple([call_2023,call_2034,const_2033,call_2039,])
func_2045 = relay.Function([], output)
mod['func_2045'] = func_2045
mod = relay.transform.InferType()(mod)
mutated_mod['func_2045'] = func_2045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2045_call = mutated_mod.get_global_var('func_2045')
call_2046 = func_2045_call()
output = call_2046
func_2047 = relay.Function([], output)
mutated_mod['func_2047'] = func_2047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1863_call = mod.get_global_var('func_1863')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_2048 = relay.TupleGetItem(func_1863_call(), 0)
call_2049 = relay.TupleGetItem(func_1865_call(), 0)
const_2057 = relay.const([[[-1.023800,5.348889,-1.865924,-1.931029,7.895956,8.147273,-2.456969,1.992139,-0.676805,-0.134906,6.951495,2.438406,-9.439610,-7.071113,6.187219,8.618093],[4.031549,9.657578,-7.310634,0.539054,-4.287782,-5.992344,-7.703834,0.669634,-1.542613,1.462850,4.966402,4.296287,0.091482,-3.841610,9.974279,7.026176],[-6.555022,-6.279970,-4.841436,8.448377,6.704947,8.847679,0.743008,-4.853702,-6.503437,0.764728,-7.577782,-0.898105,-9.470212,-6.508672,-8.112199,8.672449],[0.322757,-8.113150,9.099535,-0.718515,4.165569,-0.184394,6.030116,-8.281760,-9.365801,2.385306,-0.245065,7.966649,-3.130500,-2.018717,6.721139,-3.428700],[-7.857924,-0.532165,-1.908675,-8.857776,6.962339,-9.066195,8.694032,-7.369606,-1.032703,-4.815032,0.334001,-5.974624,-9.243082,5.530755,-7.930972,-9.235869],[-3.489625,-4.781861,6.484201,-9.669474,-8.424147,3.763505,-0.903147,3.692350,6.482381,9.286254,5.731501,2.347039,0.305483,9.061776,-4.250678,-4.258245],[7.266663,2.319960,3.264015,2.279115,-0.800365,1.265977,-9.457292,8.210514,-5.258965,5.415648,-4.580938,1.947665,0.618908,2.733676,-1.353490,-3.880236],[7.119416,6.227290,9.848807,-1.635229,0.320295,-5.389274,-6.990492,-2.159276,9.962610,5.775642,-0.310478,9.312911,5.016978,0.811100,-4.202621,2.687198],[1.961972,-2.097831,6.160570,-4.681088,-9.752975,3.679215,-8.041969,7.933612,1.504871,-8.341599,-0.427772,0.375676,-1.258098,9.579353,-1.614319,-9.553980],[0.706244,-4.898619,4.031909,-4.049910,-1.558800,3.132938,0.589886,-6.332771,0.793548,-1.677054,-6.231025,2.773446,-2.682931,7.337204,-6.125228,-7.332413],[-0.245639,-7.996440,7.281818,0.667750,-3.463613,-1.576496,8.075832,-7.865224,7.449353,-5.445372,-8.934587,9.095552,3.733931,2.166933,-6.227920,8.185358],[3.496581,0.974848,-4.348790,-1.636858,3.733841,-1.801051,8.212657,9.853449,1.383410,-5.735232,6.761623,-6.336091,-0.959251,-2.473506,7.325636,2.967913],[-6.848194,8.310965,4.464695,9.476287,8.330372,4.604591,1.568962,5.540231,8.082355,-3.480688,7.023021,6.525748,5.776516,2.925158,5.644846,2.079161],[6.411861,6.060517,-8.194780,1.413083,-6.257038,-9.635000,2.712068,5.286903,4.940934,8.722212,-9.528981,-9.902091,7.507260,9.593446,-5.853854,-6.667780],[9.161297,-0.538179,-5.077011,5.838476,-8.156446,-7.992400,-8.873200,-4.217565,-3.710657,-1.804124,-4.908530,-6.958444,-2.374266,8.905585,-1.494072,-2.826710]],[[8.686435,8.010119,-1.136317,-7.075472,-1.374126,-0.973623,-2.091092,-9.503365,5.994351,-6.909281,1.419076,9.866375,-5.152503,-6.079904,-0.112190,-5.972021],[6.817019,1.850264,6.618174,-1.273892,8.831469,-2.763451,-0.721217,-3.695814,5.833418,1.363041,8.667577,9.528514,5.687194,-3.098154,-0.689787,8.836818],[-9.672205,-8.270670,7.117777,6.902038,3.147057,-7.620046,-2.125255,8.818421,6.828000,-9.860313,1.382523,-9.243007,6.921950,-7.566536,-1.878856,0.892004],[6.413638,-6.752741,-7.513169,5.985827,5.976840,6.869230,-7.904335,3.211562,-5.026843,-4.654932,4.288200,-7.568820,9.637695,9.144200,7.717640,-1.061763],[-5.910334,3.429776,-4.560593,-1.079938,-9.682245,6.875511,6.464001,0.128341,-4.578171,0.550097,-1.560520,-3.379815,2.507389,9.048858,-8.301761,1.112856],[-6.738080,4.680176,1.650832,-8.967502,-8.648540,-7.197004,2.210151,8.796648,3.309289,9.571733,-7.698151,8.550056,9.996953,-9.419696,-1.633720,-2.570262],[-7.364739,1.402366,-9.587664,-0.969905,1.485172,-5.270098,-8.553931,-4.257136,-4.699905,4.429939,6.882518,-9.587134,-8.957203,-2.818211,-1.720028,4.543951],[-1.562260,-4.847889,2.851014,4.150921,4.866642,1.157387,9.932188,3.112036,7.076463,7.183954,8.640510,-3.809623,-4.915738,-6.433529,8.779769,-8.197162],[-1.517054,-4.416003,0.735957,-5.713475,2.458298,-5.939411,2.180066,5.762831,-5.180160,3.972670,-2.787480,3.656760,-1.175581,-6.991197,-8.149874,-9.755392],[2.563149,-0.792500,-1.645460,-8.868857,-3.111877,1.089171,-7.964057,-2.191971,9.864814,1.464104,9.936983,-5.721454,-0.324981,-6.702901,4.676232,-2.942339],[0.912938,3.946334,5.715330,-9.540722,-2.698064,-5.230274,-8.603735,-9.108477,-9.021252,7.793749,-9.817286,-1.625436,-5.623433,0.470070,2.397587,4.997853],[-5.360630,-4.288524,-6.184337,2.558503,-8.531382,9.570245,6.793922,-8.822375,2.497131,4.468596,-6.242129,7.732265,-2.243115,-3.686350,-8.457330,4.929895],[3.326519,-5.832020,-7.977216,-5.159778,4.145028,0.990123,1.638045,1.475441,5.858429,4.925488,-4.535160,5.523258,6.102395,-2.553726,5.943575,4.972270],[6.217050,-8.369912,2.060666,6.900426,-2.470413,8.915470,-0.777738,0.974972,-0.756027,2.844996,3.050658,2.239423,3.045127,-6.712193,9.706384,3.487244],[7.801342,-8.110891,-8.520826,-6.601493,-2.437857,9.753388,-9.533042,6.472289,7.427996,3.154255,6.945914,5.969630,-8.074943,4.444331,7.358972,-1.647651]],[[-2.114968,-7.774334,-0.293174,9.702361,-9.909607,-5.572416,0.386379,8.810742,-4.896896,3.075932,-0.267247,-8.534357,-2.070354,-3.101878,-3.235371,1.284539],[-2.322672,-7.527268,-8.664534,7.089966,-5.958421,2.901939,9.137190,-0.177080,2.263402,0.813170,-4.930643,-1.085493,5.489297,2.855009,2.122948,-3.916544],[-5.452091,4.027896,4.758699,5.548803,-7.679535,6.179772,-7.971702,2.734245,-7.987514,7.684585,2.788311,9.906261,-7.737047,-6.950302,8.938777,5.476462],[6.860495,-2.065764,-3.497121,-7.765514,-5.822918,-3.535243,7.719080,-1.516583,2.969629,7.808394,2.661045,3.190759,3.253145,-8.326509,3.944932,-9.999768],[-1.303117,6.456763,-1.485411,8.260180,9.540272,7.370409,9.243045,-0.081089,5.194892,0.964916,0.433917,2.895606,5.362920,3.716199,3.362206,0.284396],[1.658628,-7.978628,5.572632,-8.558115,-2.631605,7.316947,-5.420207,-6.129079,1.584407,-1.316385,-8.252571,6.736719,8.592797,-4.784477,-6.266104,-9.839157],[-2.553580,-7.482050,-8.755991,3.586852,-2.647535,3.166532,-0.210452,8.997657,6.681816,-0.541983,5.419364,2.397633,0.193073,3.589179,-7.070183,1.908664],[6.471434,-7.042244,-8.240656,-9.168214,-5.527728,9.372025,7.013632,5.985489,3.852366,-3.099718,3.257282,9.297457,-2.668435,8.407298,7.850787,2.648858],[-8.266566,-9.894620,2.069900,8.292274,-9.231610,5.258633,6.663108,9.921837,-9.100248,2.507943,8.195171,-2.422049,-8.112359,-1.732807,-7.836562,-0.095624],[7.626242,-9.214474,0.694716,3.981800,-9.886353,8.174357,3.138068,-9.942304,-4.070427,0.677018,8.419824,7.247745,8.277253,0.410756,-0.416984,-7.352766],[-1.429136,-3.757737,2.186639,-4.805156,-0.911692,9.411662,-0.700079,-7.643102,-3.891250,-4.900965,4.803056,3.963402,-5.018304,3.273195,-5.308012,-6.005133],[-5.318946,-9.357332,-0.481589,7.007277,-7.218622,-1.887517,0.456834,0.359164,9.523595,3.644454,-5.941224,2.981197,2.063204,4.499893,7.496447,-4.195570],[-4.746100,6.721366,2.782894,-7.976855,0.416897,-6.822939,7.690716,-5.135834,-4.612956,3.138682,-7.906081,7.281374,2.868998,8.619824,-6.074036,-4.874734],[-5.003043,-1.379739,0.294394,8.248762,3.422175,2.534326,-2.349619,1.237745,9.166651,1.054413,-3.316848,8.891319,3.670117,-4.831508,-0.546781,-5.627988],[-0.332786,5.126875,7.565684,-8.077510,-3.381096,4.948822,-6.405351,2.222575,-7.263726,8.228754,8.957537,-0.906444,-5.768556,3.686681,-9.397132,9.644859]],[[-5.763347,-8.662834,-7.383004,-7.244851,-7.543671,6.075065,5.686428,-0.633573,3.652825,-0.924227,-0.921884,1.640450,9.823679,1.284078,-1.753865,-7.921821],[5.738632,2.700719,7.307240,2.009860,9.744188,-2.034692,2.784283,-2.343022,9.174887,-2.619716,-8.339601,-2.111655,-6.538837,2.979048,-1.672892,2.356162],[-8.927204,1.495850,-8.544572,5.130719,8.255294,-4.907689,-1.362679,4.529612,6.632606,6.557347,5.086074,1.965860,8.470506,4.325022,-9.794863,-2.682129],[5.423949,2.918330,-4.248426,1.409435,-4.387085,-8.229319,7.534955,-9.479447,7.481745,-6.038296,2.126599,-0.570275,-3.671979,6.273676,-9.031426,6.005977],[0.030521,-4.108699,4.425435,-1.075067,5.557376,-1.455444,-5.881931,-4.832630,-2.724833,9.008498,-9.823126,-9.754291,6.857063,-2.958724,9.587513,5.963523],[-0.784231,-7.282440,8.025514,6.693952,-7.973817,8.933419,8.473588,-3.424329,-8.209677,9.413228,-3.368568,3.472402,8.147636,7.045299,6.076558,-4.259368],[-9.493104,8.295833,3.664246,9.389157,-3.261606,-3.486529,-8.859247,9.491211,-5.688112,3.729199,1.827996,-7.927062,-9.548771,7.884039,-1.433369,0.176814],[2.177125,2.239551,-7.635879,-2.637893,5.763820,-7.499995,1.287659,1.434966,-2.522637,-4.044161,2.084375,8.463165,2.674173,-7.467504,-6.098627,-7.033353],[-4.147587,-2.371505,-9.878538,-6.357234,8.191155,6.164971,-9.158146,3.533033,-3.293032,-1.074529,-4.761317,7.213997,6.313972,-3.675996,-5.445779,3.060492],[-5.291497,7.543209,-1.106154,-8.116542,-4.717513,-8.286918,-5.391326,9.583443,-9.861520,0.490318,3.912436,-1.932554,-1.740258,-3.090659,5.991276,0.363193],[7.145003,3.453852,-1.368832,-1.188420,9.981636,-5.979042,-6.946345,-8.317326,2.500890,3.867628,1.238602,1.667817,-0.460631,-7.018475,2.372212,9.602075],[-7.559273,-1.354072,5.996624,7.964752,-4.988364,-7.602857,7.079324,4.922541,-8.758612,-2.169486,-6.174306,1.599069,7.495216,-8.753766,-3.484849,-4.849652],[-8.310681,3.950619,0.112820,8.302096,-6.058638,-9.391754,-8.914417,0.822214,-6.343763,-2.885272,7.593249,-4.815424,7.913043,-4.431036,-8.294523,-4.420352],[0.887741,-7.595420,-9.671486,-0.274680,-0.599366,3.435256,-2.783333,9.839625,-2.141879,6.535781,-4.490292,-8.051251,1.422464,7.066511,5.330151,-5.375252],[0.382678,7.004072,-5.777965,3.626687,-6.439519,-2.981825,6.084678,-2.023647,9.996544,4.496060,0.334133,-7.589205,-4.224111,-0.727849,6.019297,6.084793]],[[-8.130190,4.086803,-2.165164,7.803784,1.697267,-0.948018,7.754229,-3.500407,-5.471847,-1.219638,1.473117,-5.794546,-2.929656,-7.774614,-4.591165,0.882503],[-6.806655,3.248270,0.262404,-7.330897,-2.506684,8.779789,7.868587,2.197930,6.145735,1.860130,-7.063463,4.831806,-7.882910,-5.008789,1.962590,5.697239],[-1.247713,-2.098482,0.591898,-6.029229,9.789060,-1.004038,9.926706,2.702965,1.733190,-0.367550,-6.996621,4.716567,8.936499,9.197755,3.029518,-7.201110],[-6.460477,6.081721,6.866655,2.036581,1.887884,1.072072,8.309310,6.139340,6.632081,-5.752335,4.590909,8.523445,-7.388387,1.658835,4.160127,7.273552],[7.798819,-5.819154,5.626566,2.408841,0.831015,9.171371,7.037413,3.699457,-0.365487,8.951241,6.727143,-7.080551,7.513635,3.799364,-1.602887,-4.583736],[0.733075,-1.735618,5.495679,0.231052,5.758551,0.725946,-0.246686,0.608063,5.627024,-9.043994,7.888650,-0.771358,7.299147,-0.832786,-3.720761,6.910470],[5.349118,-5.239277,8.999634,3.659256,2.632678,-6.324499,5.587761,-2.603289,-0.416866,-5.907245,-7.956336,-3.392233,-5.470022,3.212782,-3.034414,3.514143],[-4.018470,-8.787928,2.212427,-5.432202,-7.107820,-2.011053,8.129617,-1.209959,-9.167867,9.004831,5.397800,-7.146871,-5.989103,9.048805,-6.164267,-1.190365],[-5.303921,-9.812306,-3.012637,-0.995055,2.944371,7.472747,-8.859674,-8.417253,-6.206180,1.825119,-0.142657,4.953589,9.746704,3.424373,8.352010,-7.147272],[-9.426014,-2.822278,-9.752135,6.066904,4.524848,-5.477238,8.211384,-9.352411,-0.426235,9.294208,4.042881,-8.732633,8.918936,-9.780293,7.527663,5.559121],[-1.226552,1.698559,-6.634854,-8.888468,4.255499,1.592448,-2.299685,-7.418160,9.786082,5.279187,-9.542826,1.174593,6.339941,2.912601,2.777413,-1.838799],[-7.902482,-9.059094,-1.655137,-6.246095,1.117076,-4.616228,-3.214142,-4.147588,0.435816,-8.869341,9.851467,6.443979,-0.197571,-3.307995,0.623916,9.074631],[-3.492822,5.818283,-2.530471,-1.568497,1.964886,3.752431,3.639654,-0.243909,9.780417,-3.515946,-6.876928,5.348395,-9.031948,-8.390983,-1.086378,0.978590],[8.791611,-9.391534,0.648279,9.713308,5.274455,-5.114068,5.638156,3.349081,6.501798,0.286519,-0.340901,-4.620552,-8.300008,-3.068835,-1.958935,9.227469],[-4.912193,-6.246439,-3.490524,7.700616,-2.076683,-2.560130,-5.294067,0.086681,-2.883916,2.880235,0.171247,7.064607,1.004529,0.239053,-3.113305,3.290447]],[[-9.163210,-8.454471,-2.145513,-5.543160,1.245888,-9.351761,8.500929,8.359879,-1.180871,-2.640499,1.226531,-8.392004,1.990228,-4.369620,-8.875334,0.030313],[3.998350,-4.683860,0.524621,9.935857,9.067423,-9.274842,8.651791,-9.476876,-6.076501,7.758207,6.663840,-4.974915,8.873597,-0.730838,2.344995,-2.123563],[7.796071,-4.330036,-2.632632,7.051994,5.311095,-5.499433,6.110645,-4.025338,5.952719,3.195186,2.005980,1.708776,1.055205,1.047883,2.793493,9.832161],[-1.549163,3.897273,2.223427,-0.881527,-0.784548,3.872617,-1.242315,-9.600835,-5.685965,-7.904968,5.449608,-0.009577,2.882085,2.707896,-9.662987,9.281943],[-3.029781,9.328351,7.744122,-5.451182,-5.939070,8.489393,-9.715861,-3.803174,-8.876360,-3.860499,-9.886354,-5.288440,-2.142093,0.868806,-1.454745,5.937813],[0.116166,9.240165,0.021091,3.318537,6.511134,-2.762395,-3.858382,-5.326929,1.418800,-8.789068,-5.973847,6.115391,7.889499,2.954305,5.203146,-5.599869],[1.591621,6.230483,-9.564179,-2.816715,4.861493,6.631413,3.417779,-4.145303,-4.770590,-6.332326,2.302438,-1.776514,-1.783796,1.001011,-2.226181,3.314727],[1.321486,-1.025439,5.816333,9.256927,9.082402,-7.099203,4.354815,3.767386,3.143160,-9.444915,5.872815,0.384850,-0.983687,0.661346,9.555965,-5.455225],[3.044446,-4.780837,4.359444,-1.599040,-6.985135,8.514787,2.219657,5.233223,-7.636058,-6.094327,-0.194354,-9.081254,-0.514856,-7.036933,-0.660400,-7.550158],[1.641384,-6.204278,-2.045543,-1.813277,7.046503,-5.216215,-0.502857,2.225048,6.890678,0.272242,-5.629365,-0.302020,5.164122,-4.318672,5.694938,-6.113146],[2.768718,1.619193,3.488029,-1.151209,9.433269,9.673840,-1.311040,1.340430,-6.175829,-2.358116,-2.284407,6.693497,8.430683,5.467264,-5.891059,2.173883],[-7.584371,-8.602940,-8.829893,-5.143794,7.238728,-7.019840,-4.730839,-2.714626,-7.922400,3.637585,7.752855,-6.240851,-8.234260,-9.639565,4.276713,-2.970249],[-1.289828,9.989688,4.220250,4.015507,-6.226280,8.797290,6.699533,8.376477,-7.164760,-7.358755,-8.395938,-1.810334,-1.253331,1.778124,-9.368897,2.768986],[-6.740195,-5.330550,-2.427747,6.354223,0.738148,5.342762,-0.767205,-5.105215,-2.405720,-0.569399,4.664876,3.086133,5.908449,-7.474420,9.037478,4.819353],[-0.205533,3.902276,8.924954,3.559649,2.749515,3.129419,-6.502731,-6.557274,-4.881235,1.467525,8.756146,1.209283,2.554964,8.096203,4.164275,0.175754]],[[-6.712379,-7.319994,9.603647,-3.199844,-8.451648,-4.403034,7.509023,0.531553,1.917653,4.482939,-3.993765,-1.665821,-5.771554,-6.368292,-7.956737,-1.286960],[-7.433485,-6.285653,-2.813799,1.770982,-3.039928,0.704464,-4.252191,4.867906,9.375959,0.920687,7.592755,-0.930147,9.194321,2.960760,-7.955255,-6.590522],[-9.349600,-9.850229,6.655943,0.710643,3.083795,1.972191,-3.502093,3.366470,6.087678,8.745558,-1.925115,3.319790,-5.499497,0.165535,-8.767905,0.031192],[-4.394826,8.911809,2.707986,4.730887,-5.589417,7.034174,1.943416,-0.302848,4.302432,6.696298,3.491306,6.730161,6.054526,-5.152259,-8.303848,-4.399710],[8.969557,-4.461701,5.331156,2.949781,-0.895277,-2.019600,-2.667418,-0.011101,-5.674292,2.691645,-9.278554,3.984005,-7.474610,6.917551,7.439404,5.494589],[-2.154999,-4.379652,-7.277541,7.297007,-4.677200,-4.218586,-5.148301,-9.380426,6.634632,3.111380,-1.175691,5.861158,-5.118447,3.967049,0.050694,1.311285],[-6.605138,4.488048,0.635684,2.087499,-8.317296,-4.185895,-4.083542,9.720280,7.258280,-6.562560,0.646858,-5.331528,-6.795475,9.788580,-1.226436,1.690435],[-4.122892,7.071959,8.818566,9.031997,2.913650,7.774531,-2.318612,4.037529,3.888414,1.691916,0.906077,-5.415048,9.344158,7.279252,-0.978852,-0.562107],[1.878478,5.054626,-7.625685,-5.143599,-9.219007,-5.258954,-1.544024,-0.383686,7.535302,-1.018108,8.407968,-3.802401,9.930375,5.229617,3.902764,-1.398613],[2.287899,0.003718,2.633903,2.618153,3.088568,-4.437610,7.541997,8.161407,2.797860,-6.141845,1.281746,2.187219,-3.607166,-3.541247,5.323796,2.422251],[-4.982813,-0.222889,-7.918604,-6.839558,0.581318,-1.986541,6.144006,7.746592,0.087411,-1.502325,1.909446,6.617499,-6.453187,1.285827,6.908094,-6.651670],[8.310369,7.967909,6.080461,-2.148803,-9.141016,6.615353,-2.994283,-4.159202,-8.400869,-3.185050,5.361352,-8.183155,-0.806649,2.836210,-5.249457,2.916544],[-6.334679,9.722082,-5.826718,2.457884,-9.135249,3.741308,0.681040,5.686469,-3.894690,1.730600,2.925507,3.271116,8.418721,6.833426,-6.319205,-2.242213],[4.319264,-6.049055,1.113881,5.398149,7.313484,-3.817170,-7.647672,-2.045025,-8.830929,-1.638041,8.134431,8.397282,-9.604632,-3.730242,0.134224,-8.007510],[6.379768,7.777155,-2.631089,-5.331633,6.443013,-0.461969,-1.974566,-0.094911,6.779739,1.486218,-0.241993,7.248961,0.817716,0.877758,-8.019951,-5.995018]]], dtype = "float32")#candidate|2057|(7, 15, 16)|const|float32
bop_2058 = relay.less_equal(call_2048.astype('bool'), const_2057.astype('bool')) # shape=(7, 15, 16)
bop_2061 = relay.less_equal(call_2049.astype('bool'), const_2057.astype('bool')) # shape=(7, 15, 16)
func_1068_call = mod.get_global_var('func_1068')
func_1071_call = mutated_mod.get_global_var('func_1071')
const_2064 = relay.const([-0.606863,-3.997432,4.198812,5.066001,-7.628864,2.021396,-8.705820,-7.788474,5.913218,-9.636742,8.736924,-8.384238,-6.397854,8.438617,5.323079,-9.863003,-2.666918,-2.249969,-6.433773,1.640215,-6.576095,4.712765,-3.094927,-2.351304,-0.405755,-1.594856,2.999013,-9.813740,-7.857204,9.678080,-9.219560,-1.266933,1.110420,2.540615,-8.918880,-3.570274,4.388152,-0.372553,7.924093,-3.267405,5.264324,-8.786609,9.137898,-6.141335,-5.928360,-6.807176,8.342380,1.614955,3.652949,-5.848112,8.137313,-6.006871,6.855395,-8.122732,8.022068,-7.656993,-2.250448,0.590928,-9.670945,0.282900,-0.176158,7.468493,-9.929192,-8.028993,9.515625,-0.226938,9.703140,-8.182449,8.886940,-6.950132,5.874379,5.577347], dtype = "float32")#candidate|2064|(72,)|const|float32
call_2063 = relay.TupleGetItem(func_1068_call(relay.reshape(const_2064.astype('float32'), [72,])), 2)
call_2065 = relay.TupleGetItem(func_1071_call(relay.reshape(const_2064.astype('float32'), [72,])), 2)
output = relay.Tuple([bop_2058,call_2063,const_2064,])
output2 = relay.Tuple([bop_2061,call_2065,const_2064,])
func_2068 = relay.Function([], output)
mod['func_2068'] = func_2068
mod = relay.transform.InferType()(mod)
output = func_2068()
func_2069 = relay.Function([], output)
mutated_mod['func_2069'] = func_2069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1842_call = mod.get_global_var('func_1842')
func_1844_call = mutated_mod.get_global_var('func_1844')
call_2116 = relay.TupleGetItem(func_1842_call(), 0)
call_2117 = relay.TupleGetItem(func_1844_call(), 0)
output = relay.Tuple([call_2116,])
output2 = relay.Tuple([call_2117,])
func_2119 = relay.Function([], output)
mod['func_2119'] = func_2119
mod = relay.transform.InferType()(mod)
mutated_mod['func_2119'] = func_2119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2119_call = mutated_mod.get_global_var('func_2119')
call_2120 = func_2119_call()
output = call_2120
func_2121 = relay.Function([], output)
mutated_mod['func_2121'] = func_2121
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2134 = relay.var("var_2134", dtype = "int8", shape = (15, 5, 12))#candidate|2134|(15, 5, 12)|var|int8
const_2135 = relay.const([[[-1,-5,-5,6,-10,2,5,9,-5,8,-7,-5],[-4,-6,5,-4,6,-3,-10,4,-7,3,2,-9],[-10,-4,-1,-4,9,-10,10,3,3,-1,-6,-2],[-3,5,9,-4,-1,6,5,-7,-9,-1,10,7],[9,-4,-2,7,3,1,-6,-9,-3,-8,-4,-5]],[[3,2,-9,7,-4,4,-9,-1,5,-4,-9,9],[-7,-2,-6,-4,2,-4,-4,10,4,-5,-7,7],[2,-4,-4,5,-1,-2,6,8,3,-3,-3,-8],[7,1,-2,7,-10,9,5,7,2,3,-7,-10],[-2,-7,3,3,-1,-7,5,-8,-6,-10,10,-7]],[[9,2,10,6,2,7,1,9,-4,-4,10,-5],[9,-5,3,3,3,-7,9,7,9,9,5,9],[-4,-10,6,-1,9,4,-2,-3,4,10,-3,7],[2,-9,5,6,-2,-8,-10,-3,-6,10,-6,3],[-2,5,9,-7,-9,-5,6,-8,8,7,4,8]],[[9,-8,-2,6,3,1,-5,-10,-5,-3,-8,1],[8,5,-10,-1,-10,3,-9,8,-2,3,-9,6],[-2,5,1,-8,-6,8,-6,4,-10,-10,7,3],[8,1,-1,-1,5,4,4,2,5,-3,-10,8],[5,1,5,3,1,1,10,-6,-10,8,2,-3]],[[3,7,4,-5,3,-2,3,-6,-9,8,-10,2],[-7,-3,4,6,-3,-3,8,5,6,-4,3,3],[6,1,10,-4,-8,5,-5,1,4,3,2,7],[-7,6,8,4,-5,-8,10,9,2,-2,-7,-3],[7,-4,7,-6,2,-6,3,2,5,-2,-5,5]],[[-7,4,-9,4,6,2,9,8,10,-10,4,-3],[-6,-5,6,-8,-6,6,1,1,7,-1,-1,-8],[4,8,-1,-8,3,-10,5,1,-2,9,6,1],[5,-10,2,9,-5,6,7,-3,-9,-9,-2,-10],[-7,10,-8,7,-4,10,-2,-1,-8,-2,-1,5]],[[-9,6,5,8,4,-5,8,6,8,7,6,8],[-3,9,5,-3,8,-10,5,3,5,-2,2,6],[-5,-10,8,-7,8,4,9,10,9,10,-7,3],[-3,-8,2,-4,6,8,-2,7,-10,-5,-2,-8],[-6,-5,3,6,5,-8,-7,-4,6,9,8,2]],[[-10,-8,-4,3,7,3,-8,-6,5,1,-6,-7],[8,4,3,-5,1,-3,-2,-4,-4,8,8,-6],[8,4,-2,-8,-6,-6,8,-10,-5,-3,1,7],[-4,9,1,-4,-1,-6,-1,3,9,-6,3,6],[-3,8,-6,-9,-1,4,-4,-2,-9,9,-3,9]],[[6,-6,5,8,1,-10,-10,-7,9,-3,-2,-1],[-3,10,5,-5,7,1,-5,8,4,3,10,6],[-3,-6,4,-5,8,-3,7,3,1,-5,-2,2],[-4,-1,-7,6,6,7,7,-4,-9,5,5,1],[-1,-4,-1,10,-3,2,8,4,-7,-1,-2,9]],[[-4,-9,-4,6,-7,8,-9,5,-9,-4,4,8],[-6,6,-6,1,-1,8,1,3,-6,-9,-1,-7],[-3,7,6,9,-6,1,-1,-1,-5,2,-5,-5],[7,-6,-10,9,1,-9,3,10,-4,-3,-7,1],[-5,7,7,-1,-8,5,7,9,1,-8,7,-6]],[[-2,8,-5,-1,-2,-8,-2,5,5,8,-3,-1],[-9,1,-8,-9,-9,-8,-7,-3,-7,8,-10,-1],[-3,7,8,-2,-9,-2,-3,-7,-9,-5,4,-3],[-10,4,6,-5,4,6,-1,8,-3,-7,3,-9],[9,-7,3,-7,5,-3,5,-3,-1,1,-9,-4]],[[-1,-1,6,-7,5,9,-7,2,-8,-4,-4,-3],[6,-7,-5,7,1,-10,-9,2,-2,3,9,-3],[10,-1,-6,9,8,-9,6,-1,-6,-4,10,9],[10,3,-5,6,6,2,-2,6,-7,-3,10,2],[4,1,3,-8,-1,-2,-9,-4,6,9,-6,-7]],[[1,-6,5,9,5,5,-9,2,-4,-6,3,-10],[-7,8,-5,6,9,8,-1,3,-6,-5,1,-5],[-2,-10,5,7,-10,-3,1,2,3,-4,-5,-10],[5,-8,-3,-5,-7,1,6,2,-2,-2,6,3],[-4,-4,3,-1,-1,9,3,-2,-1,-2,2,7]],[[-1,-9,3,-8,10,-7,10,-3,7,7,-8,-10],[-4,7,6,-10,-5,6,2,6,-8,2,8,-8],[-9,-7,-6,5,-9,5,-8,-2,3,-10,6,4],[-8,-3,-4,-3,8,10,-7,5,1,1,5,4],[-5,-1,-2,-4,-3,-9,10,2,2,-3,10,4]],[[7,3,-1,8,-3,5,-5,-6,-8,7,-6,5],[10,-10,-7,2,-2,-6,1,-6,-6,-8,2,9],[-10,7,5,6,9,4,10,9,-10,-4,-10,3],[-3,-7,8,6,-4,4,2,-3,-5,8,4,9],[4,-4,6,-10,-2,-8,5,-6,7,-8,-9,-2]]], dtype = "int8")#candidate|2135|(15, 5, 12)|const|int8
bop_2136 = relay.add(var_2134.astype('int8'), relay.reshape(const_2135.astype('int8'), relay.shape_of(var_2134))) # shape=(15, 5, 12)
uop_2141 = relay.log2(bop_2136.astype('float64')) # shape=(15, 5, 12)
output = uop_2141
output2 = uop_2141
func_2146 = relay.Function([var_2134,], output)
mod['func_2146'] = func_2146
mod = relay.transform.InferType()(mod)
mutated_mod['func_2146'] = func_2146
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2147 = relay.var("var_2147", dtype = "int8", shape = (15, 5, 12))#candidate|2147|(15, 5, 12)|var|int8
func_2146_call = mutated_mod.get_global_var('func_2146')
call_2148 = func_2146_call(var_2147)
output = call_2148
func_2149 = relay.Function([var_2147], output)
mutated_mod['func_2149'] = func_2149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1781_call = mod.get_global_var('func_1781')
func_1782_call = mutated_mod.get_global_var('func_1782')
call_2167 = relay.TupleGetItem(func_1781_call(), 0)
call_2168 = relay.TupleGetItem(func_1782_call(), 0)
output = relay.Tuple([call_2167,])
output2 = relay.Tuple([call_2168,])
func_2175 = relay.Function([], output)
mod['func_2175'] = func_2175
mod = relay.transform.InferType()(mod)
output = func_2175()
func_2176 = relay.Function([], output)
mutated_mod['func_2176'] = func_2176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_962_call = mod.get_global_var('func_962')
func_964_call = mutated_mod.get_global_var('func_964')
call_2238 = relay.TupleGetItem(func_962_call(), 0)
call_2239 = relay.TupleGetItem(func_964_call(), 0)
output = call_2238
output2 = call_2239
func_2242 = relay.Function([], output)
mod['func_2242'] = func_2242
mod = relay.transform.InferType()(mod)
mutated_mod['func_2242'] = func_2242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2242_call = mutated_mod.get_global_var('func_2242')
call_2243 = func_2242_call()
output = call_2243
func_2244 = relay.Function([], output)
mutated_mod['func_2244'] = func_2244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1781_call = mod.get_global_var('func_1781')
func_1782_call = mutated_mod.get_global_var('func_1782')
call_2261 = relay.TupleGetItem(func_1781_call(), 0)
call_2262 = relay.TupleGetItem(func_1782_call(), 0)
func_1409_call = mod.get_global_var('func_1409')
func_1410_call = mutated_mod.get_global_var('func_1410')
call_2304 = func_1409_call()
call_2305 = func_1409_call()
var_2311 = relay.var("var_2311", dtype = "float64", shape = (7, 15, 16))#candidate|2311|(7, 15, 16)|var|float64
bop_2312 = relay.less(call_2261.astype('bool'), var_2311.astype('bool')) # shape=(7, 15, 16)
bop_2315 = relay.less(call_2262.astype('bool'), var_2311.astype('bool')) # shape=(7, 15, 16)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_2319 = func_580_call()
call_2320 = func_580_call()
func_1890_call = mod.get_global_var('func_1890')
func_1894_call = mutated_mod.get_global_var('func_1894')
var_2322 = relay.var("var_2322", dtype = "bool", shape = (55, 7))#candidate|2322|(55, 7)|var|bool
call_2321 = relay.TupleGetItem(func_1890_call(relay.reshape(var_2322.astype('bool'), [7, 5, 11]), relay.reshape(var_2322.astype('bool'), [7, 5, 11]), ), 0)
call_2323 = relay.TupleGetItem(func_1894_call(relay.reshape(var_2322.astype('bool'), [7, 5, 11]), relay.reshape(var_2322.astype('bool'), [7, 5, 11]), ), 0)
uop_2330 = relay.asin(call_2304.astype('float64')) # shape=(7, 15, 1)
uop_2332 = relay.asin(call_2305.astype('float64')) # shape=(7, 15, 1)
func_2068_call = mod.get_global_var('func_2068')
func_2069_call = mutated_mod.get_global_var('func_2069')
call_2333 = relay.TupleGetItem(func_2068_call(), 1)
call_2334 = relay.TupleGetItem(func_2069_call(), 1)
output = relay.Tuple([bop_2312,call_2319,call_2321,var_2322,uop_2330,call_2333,])
output2 = relay.Tuple([bop_2315,call_2320,call_2323,var_2322,uop_2332,call_2334,])
func_2338 = relay.Function([var_2311,var_2322,], output)
mod['func_2338'] = func_2338
mod = relay.transform.InferType()(mod)
var_2339 = relay.var("var_2339", dtype = "float64", shape = (7, 15, 16))#candidate|2339|(7, 15, 16)|var|float64
var_2340 = relay.var("var_2340", dtype = "bool", shape = (55, 7))#candidate|2340|(55, 7)|var|bool
output = func_2338(var_2339,var_2340,)
func_2341 = relay.Function([var_2339,var_2340,], output)
mutated_mod['func_2341'] = func_2341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2068_call = mod.get_global_var('func_2068')
func_2069_call = mutated_mod.get_global_var('func_2069')
call_2345 = relay.TupleGetItem(func_2068_call(), 2)
call_2346 = relay.TupleGetItem(func_2069_call(), 2)
func_2242_call = mod.get_global_var('func_2242')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_2355 = func_2242_call()
call_2356 = func_2242_call()
func_2146_call = mod.get_global_var('func_2146')
func_2149_call = mutated_mod.get_global_var('func_2149')
var_2377 = relay.var("var_2377", dtype = "int8", shape = (900,))#candidate|2377|(900,)|var|int8
call_2376 = func_2146_call(relay.reshape(var_2377.astype('int8'), [15, 5, 12]))
call_2378 = func_2146_call(relay.reshape(var_2377.astype('int8'), [15, 5, 12]))
bop_2387 = relay.logical_xor(call_2376.astype('int32'), relay.reshape(var_2377.astype('int32'), relay.shape_of(call_2376))) # shape=(15, 5, 12)
bop_2390 = relay.logical_xor(call_2378.astype('int32'), relay.reshape(var_2377.astype('int32'), relay.shape_of(call_2378))) # shape=(15, 5, 12)
bop_2392 = relay.multiply(call_2345.astype('uint8'), call_2355.astype('uint8')) # shape=(7, 15, 72)
bop_2395 = relay.multiply(call_2346.astype('uint8'), call_2356.astype('uint8')) # shape=(7, 15, 72)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_2402 = func_1015_call()
call_2403 = func_1015_call()
func_1842_call = mod.get_global_var('func_1842')
func_1844_call = mutated_mod.get_global_var('func_1844')
call_2404 = relay.TupleGetItem(func_1842_call(), 0)
call_2405 = relay.TupleGetItem(func_1844_call(), 0)
output = relay.Tuple([bop_2387,bop_2392,call_2402,call_2404,])
output2 = relay.Tuple([bop_2390,bop_2395,call_2403,call_2405,])
func_2406 = relay.Function([var_2377,], output)
mod['func_2406'] = func_2406
mod = relay.transform.InferType()(mod)
var_2407 = relay.var("var_2407", dtype = "int8", shape = (900,))#candidate|2407|(900,)|var|int8
output = func_2406(var_2407)
func_2408 = relay.Function([var_2407], output)
mutated_mod['func_2408'] = func_2408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2242_call = mod.get_global_var('func_2242')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_2419 = func_2242_call()
call_2420 = func_2242_call()
func_2045_call = mod.get_global_var('func_2045')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_2423 = relay.TupleGetItem(func_2045_call(), 1)
call_2424 = relay.TupleGetItem(func_2047_call(), 1)
func_748_call = mod.get_global_var('func_748')
func_752_call = mutated_mod.get_global_var('func_752')
var_2430 = relay.var("var_2430", dtype = "float64", shape = (6, 84))#candidate|2430|(6, 84)|var|float64
call_2429 = relay.TupleGetItem(func_748_call(relay.reshape(var_2430.astype('float64'), [4, 9, 14]), relay.reshape(var_2430.astype('float64'), [4, 9, 14]), ), 0)
call_2431 = relay.TupleGetItem(func_752_call(relay.reshape(var_2430.astype('float64'), [4, 9, 14]), relay.reshape(var_2430.astype('float64'), [4, 9, 14]), ), 0)
func_1842_call = mod.get_global_var('func_1842')
func_1844_call = mutated_mod.get_global_var('func_1844')
call_2434 = relay.TupleGetItem(func_1842_call(), 0)
call_2435 = relay.TupleGetItem(func_1844_call(), 0)
output = relay.Tuple([call_2419,call_2423,call_2429,var_2430,call_2434,])
output2 = relay.Tuple([call_2420,call_2424,call_2431,var_2430,call_2435,])
func_2436 = relay.Function([var_2430,], output)
mod['func_2436'] = func_2436
mod = relay.transform.InferType()(mod)
var_2437 = relay.var("var_2437", dtype = "float64", shape = (6, 84))#candidate|2437|(6, 84)|var|float64
output = func_2436(var_2437)
func_2438 = relay.Function([var_2437], output)
mutated_mod['func_2438'] = func_2438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2242_call = mod.get_global_var('func_2242')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_2532 = func_2242_call()
call_2533 = func_2242_call()
output = call_2532
output2 = call_2533
func_2548 = relay.Function([], output)
mod['func_2548'] = func_2548
mod = relay.transform.InferType()(mod)
output = func_2548()
func_2549 = relay.Function([], output)
mutated_mod['func_2549'] = func_2549
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2571 = relay.var("var_2571", dtype = "uint32", shape = (14, 6, 9))#candidate|2571|(14, 6, 9)|var|uint32
const_2572 = relay.const([[[10,1,-3,8,9,-6,-4,-9,-6],[3,7,-8,10,10,5,-2,-5,3],[-3,9,-8,8,-2,2,-6,-1,-1],[-8,4,7,-5,6,-1,7,9,-5],[-4,10,9,-5,9,10,4,-2,-5],[10,9,1,5,3,5,-1,-2,5]],[[5,8,6,5,-7,10,10,-1,8],[-1,1,6,-4,5,10,-9,1,-8],[-7,-9,-1,-6,1,-10,-9,-1,-4],[6,-6,6,-2,10,4,2,-2,-8],[4,-2,1,-5,10,1,-4,2,8],[5,-4,-5,4,2,10,9,-3,-8]],[[-2,5,10,-7,-2,4,10,-2,-6],[-3,-6,-8,-6,-10,-7,-3,3,4],[3,8,2,-7,-3,7,8,2,6],[10,-7,10,3,5,-3,-1,-2,-4],[-1,9,4,3,-5,-5,5,2,8],[-7,7,-8,3,-7,-8,-1,5,-3]],[[5,10,3,2,1,-9,8,-1,-8],[-5,6,-5,-6,3,4,8,-4,-1],[6,-4,-9,-7,6,2,-6,-2,3],[-7,2,8,-8,7,-9,-10,2,-1],[4,8,7,-4,10,-3,3,-10,10],[5,6,-1,-10,9,2,5,-9,5]],[[-4,7,7,7,-2,7,6,-1,3],[9,-10,9,10,7,8,3,3,8],[-2,1,3,-5,9,-3,-5,-10,-3],[-6,-3,-2,4,-5,-5,-8,7,10],[-7,-8,10,-1,-6,-9,-9,1,5],[5,9,10,-2,-3,-8,-6,8,1]],[[5,-3,2,7,-5,3,2,-3,7],[-6,-2,7,-10,2,7,5,5,1],[10,-9,8,8,10,-2,-5,-8,-5],[-4,10,-4,1,-6,-7,-6,-5,-3],[4,3,-1,5,-3,-2,9,-5,5],[-5,9,5,-8,-3,3,-8,-7,5]],[[5,-5,-4,-9,6,4,-1,8,-10],[-8,-3,3,-8,6,-3,-5,-10,9],[9,9,-9,-7,-3,4,7,6,-2],[-9,-2,-8,-4,5,5,-10,-1,-10],[-3,3,-1,3,-7,-9,8,3,-2],[6,4,-2,3,-1,-10,-5,7,10]],[[4,-5,2,4,-3,1,8,3,-9],[8,4,8,-4,8,-2,-9,-4,9],[-10,8,-2,9,6,-9,-7,-7,-10],[-7,-8,6,-7,-6,9,7,-10,3],[1,1,5,2,-9,-5,2,3,-8],[9,4,-4,-3,-2,-5,-5,8,6]],[[6,-5,7,-3,-1,8,-7,-5,-2],[-2,10,-8,-9,-3,-10,10,9,10],[7,-4,4,-10,-8,-10,3,-3,-7],[10,-5,5,-4,-1,2,6,7,-10],[1,-1,-4,-9,-6,10,7,-1,2],[8,-3,-8,10,-6,5,9,-7,-7]],[[3,6,10,3,5,-10,10,-3,-4],[-7,7,3,-1,-8,-3,9,-10,-3],[2,-10,10,6,-7,-2,-1,5,-2],[10,1,2,-4,9,-8,8,8,9],[-7,9,-5,5,10,6,10,-5,-5],[-4,10,6,-6,9,2,6,-2,-3]],[[6,3,-2,9,-6,-5,-3,-1,-4],[2,1,6,1,3,6,2,-8,9],[-5,-1,3,1,5,-3,-9,1,-8],[3,8,5,-4,10,-4,-9,9,8],[-8,-10,-1,3,9,1,-10,9,2],[4,2,7,4,3,-8,5,-9,10]],[[-9,-1,-5,-8,-9,-3,-2,7,2],[10,-2,9,-3,7,-1,-4,-7,1],[-9,7,5,-1,8,2,3,-7,-2],[-8,-3,9,-1,-6,-9,-2,-5,8],[-2,8,-8,9,-2,-8,-3,1,1],[-9,4,1,-2,2,6,7,9,-6]],[[-8,8,-3,6,3,3,-9,6,-10],[7,-4,9,-10,-5,-4,8,10,-1],[4,-1,5,1,-6,7,6,8,-4],[-9,3,-3,-7,-6,9,-9,5,10],[-2,3,-9,-6,6,-4,-10,3,5],[8,-1,8,-2,-10,7,-6,-2,10]],[[1,4,-9,6,-1,1,-8,-9,-3],[-6,-6,-3,-8,-3,-2,-2,7,10],[6,5,6,-5,-5,3,3,-5,8],[1,1,-8,5,5,6,9,-1,9],[-10,-2,-9,5,4,9,9,10,4],[-2,8,4,-3,5,-9,1,-9,6]]], dtype = "uint32")#candidate|2572|(14, 6, 9)|const|uint32
bop_2573 = relay.bitwise_or(var_2571.astype('uint32'), relay.reshape(const_2572.astype('uint32'), relay.shape_of(var_2571))) # shape=(14, 6, 9)
output = bop_2573
output2 = bop_2573
func_2582 = relay.Function([var_2571,], output)
mod['func_2582'] = func_2582
mod = relay.transform.InferType()(mod)
var_2583 = relay.var("var_2583", dtype = "uint32", shape = (14, 6, 9))#candidate|2583|(14, 6, 9)|var|uint32
output = func_2582(var_2583)
func_2584 = relay.Function([var_2583], output)
mutated_mod['func_2584'] = func_2584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_2589 = relay.TupleGetItem(func_1590_call(), 0)
call_2590 = relay.TupleGetItem(func_1592_call(), 0)
func_1890_call = mod.get_global_var('func_1890')
func_1894_call = mutated_mod.get_global_var('func_1894')
const_2617 = relay.const([[True,True,True,True,True,False,False],[True,True,True,False,False,True,True],[False,False,True,True,True,True,True],[False,False,True,False,True,False,False],[False,True,False,True,True,False,False],[False,False,False,True,True,False,False],[True,True,True,True,True,True,True],[True,False,False,True,False,True,True],[False,False,True,False,True,False,True],[False,False,True,False,False,False,False],[False,False,False,True,True,True,True],[True,False,False,False,True,False,True],[True,True,True,True,True,False,True],[True,False,False,True,False,False,False],[True,False,False,True,False,False,False],[True,True,True,False,False,True,False],[True,True,False,False,True,True,False],[False,True,True,True,False,False,True],[False,False,True,True,False,True,False],[False,True,True,True,False,False,False],[False,False,False,True,True,False,False],[False,True,False,True,True,True,False],[True,True,True,True,True,False,True],[True,True,True,True,False,False,True],[True,True,True,True,True,True,True],[False,False,True,True,True,True,False],[False,False,False,True,False,False,True],[True,False,False,True,False,True,False],[False,False,True,True,True,False,True],[False,False,False,False,False,True,True],[True,False,True,False,False,False,True],[False,False,False,False,False,False,True],[False,False,True,True,False,True,False],[True,True,True,True,True,True,True],[True,False,True,True,False,False,True],[True,False,False,True,False,True,True],[True,True,False,True,True,False,False],[True,True,True,False,False,False,True],[False,False,True,True,False,False,False],[True,False,True,False,True,False,True],[True,True,True,False,False,True,False],[False,True,False,True,False,True,False],[True,False,True,True,False,False,False],[False,False,True,True,True,False,True],[False,False,True,True,True,False,False],[False,True,False,False,True,False,True],[True,False,True,False,False,True,True],[False,True,False,False,False,True,False],[True,True,True,True,False,False,False],[True,False,False,True,False,False,True],[True,True,True,False,True,False,True],[True,True,False,True,True,False,True],[True,True,True,False,True,True,True],[True,True,True,False,False,False,False],[False,False,True,True,True,False,True]], dtype = "bool")#candidate|2617|(55, 7)|const|bool
call_2616 = relay.TupleGetItem(func_1890_call(relay.reshape(const_2617.astype('bool'), [7, 5, 11]), relay.reshape(const_2617.astype('bool'), [7, 5, 11]), ), 0)
call_2618 = relay.TupleGetItem(func_1894_call(relay.reshape(const_2617.astype('bool'), [7, 5, 11]), relay.reshape(const_2617.astype('bool'), [7, 5, 11]), ), 0)
uop_2623 = relay.log10(const_2617.astype('float32')) # shape=(55, 7)
output = relay.Tuple([call_2589,call_2616,uop_2623,])
output2 = relay.Tuple([call_2590,call_2618,uop_2623,])
func_2629 = relay.Function([], output)
mod['func_2629'] = func_2629
mod = relay.transform.InferType()(mod)
output = func_2629()
func_2630 = relay.Function([], output)
mutated_mod['func_2630'] = func_2630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_816_call = mutated_mod.get_global_var('func_816')
call_2631 = relay.TupleGetItem(func_815_call(), 1)
call_2632 = relay.TupleGetItem(func_816_call(), 1)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
var_2640 = relay.var("var_2640", dtype = "int8", shape = (900,))#candidate|2640|(900,)|var|int8
call_2639 = relay.TupleGetItem(func_2406_call(relay.reshape(var_2640.astype('int8'), [900,])), 0)
call_2641 = relay.TupleGetItem(func_2408_call(relay.reshape(var_2640.astype('int8'), [900,])), 0)
bop_2642 = relay.floor_mod(var_2640.astype('float32'), relay.reshape(call_2639.astype('float32'), relay.shape_of(var_2640))) # shape=(900,)
bop_2645 = relay.floor_mod(var_2640.astype('float32'), relay.reshape(call_2641.astype('float32'), relay.shape_of(var_2640))) # shape=(900,)
const_2661 = relay.const([[[-8.221858,-2.215536,-8.088732,2.004096,-9.529591],[3.322181,3.263335,-8.958477,0.577948,9.427475],[-5.909605,-4.800591,0.639289,6.320685,7.166800],[2.069379,5.344663,1.021520,-3.693572,2.324171],[4.384923,-1.739426,0.024121,-5.139506,1.220208],[1.915273,6.581890,8.599143,7.219335,-2.682221],[1.081310,-4.576376,1.881957,5.033767,-6.031445],[-9.597257,5.361357,-7.825284,4.979626,-1.900824],[5.216499,3.263422,7.484127,4.930884,8.345897],[1.965754,5.517077,-4.130922,1.905447,-2.872602],[-1.844080,-2.941450,7.880577,-6.825098,3.292446],[-5.222565,-3.572166,9.037530,-4.000633,-4.255560],[-5.023958,9.888892,6.937373,-6.363956,9.114598],[7.293228,-2.463041,7.619216,-7.173420,-6.914116],[-8.366123,-1.093967,-3.536837,0.326541,-0.585544]],[[3.207011,6.276484,-8.218829,-8.881612,-4.007050],[-5.911078,3.823378,7.913080,-2.097766,-2.199023],[2.040322,2.844320,-6.742185,0.496913,3.832688],[2.351881,1.026225,3.080042,-3.755207,-2.826751],[6.856268,-8.542411,1.101139,2.914631,3.103562],[2.591136,9.044702,0.050821,-9.598300,5.944394],[-4.543405,-9.890887,2.536442,-7.274710,6.940951],[-5.566125,4.800156,7.899204,-9.723519,-2.317276],[5.629385,-2.256586,8.533575,-3.834088,8.671347],[3.853452,-9.583897,1.689077,7.664124,9.263515],[-4.213486,7.499955,-8.852302,8.286567,5.151496],[3.163432,2.772324,4.248749,7.656332,-1.625141],[3.282566,-0.338296,-4.325344,-5.523938,1.488859],[-7.252263,5.474424,6.123227,2.324495,2.557584],[5.750350,4.432510,-6.126038,3.948652,-7.268873]],[[-4.527284,9.944939,8.825251,-2.173968,3.181093],[-6.006805,-8.795777,4.436178,4.634319,-9.167646],[7.150966,9.577395,-0.391009,-1.364902,4.682729],[6.389890,-2.472846,9.217371,-7.408329,5.207239],[5.318110,-6.023182,-4.151570,-7.187857,-4.220379],[-0.824668,-9.321339,-3.578272,3.955221,-6.668010],[1.527184,9.650664,-2.739990,7.017701,-6.786752],[-4.829238,-4.660085,4.703967,-5.896535,0.789287],[-6.525239,-1.415905,8.007370,2.523571,4.531280],[-4.594044,-1.348220,3.427531,-7.321267,8.851611],[2.982616,-8.587051,-3.319196,-1.283057,3.205763],[1.263618,3.033875,-1.173572,-6.592265,-1.969864],[3.832136,-1.567516,-1.741611,-5.881090,9.904430],[1.971245,2.023803,-8.119104,-8.154441,-1.436562],[-2.789481,1.471869,-6.066157,3.443951,-8.532790]],[[-2.604620,-0.281134,7.364754,-4.936199,7.621795],[8.712964,3.267786,-7.354197,7.868772,-6.445729],[4.821231,0.057264,3.564601,-7.520629,6.435045],[-5.370128,1.014993,-5.718929,0.836357,-7.660108],[-9.726336,3.395983,0.718126,-3.420728,-7.912602],[-1.577482,1.096295,3.058997,4.295001,8.702972],[-6.875973,8.610277,-7.613749,-9.163966,-4.801633],[-7.476384,-3.418795,-5.517906,-7.413533,-1.033739],[-8.328046,-2.935703,9.894481,-8.179662,8.077391],[5.902226,0.589521,8.535772,-3.073630,0.372944],[4.815273,-2.795361,5.909795,6.578055,8.157210],[9.063659,-4.997416,9.712129,9.855561,0.501476],[-3.309658,-6.343880,2.329637,5.284358,5.882070],[-4.657647,9.472442,-3.893473,-0.474243,-1.349873],[-8.625979,3.116396,7.065473,-7.492709,-7.012239]],[[1.805955,-9.975865,-9.523291,-8.231835,9.677230],[-3.649786,-3.266100,-3.461756,-2.014888,-7.163353],[-6.723227,-8.021085,8.245187,1.574423,-3.561638],[7.608584,-0.671953,5.395689,4.976696,-2.965738],[1.181427,4.413970,-7.392466,0.145669,-8.825509],[2.159303,-5.688925,-5.018406,8.464731,3.266172],[6.636709,-4.770383,-2.404995,-3.786813,3.578576],[-7.029058,2.952040,-7.866422,-5.645440,-6.658702],[0.684559,9.467680,-5.785899,2.738854,3.980990],[5.784962,-5.483071,-2.904553,-9.655346,-5.001900],[-6.600629,-4.192389,-9.031119,3.337759,-1.474297],[6.094681,-5.745132,7.277326,-3.734298,-6.358643],[9.445965,-5.996451,9.190802,-4.092321,3.216773],[2.507945,-2.542507,5.432912,-6.084269,6.097094],[2.228038,-2.591976,9.634527,-0.694572,2.116929]],[[-1.151847,-0.181866,-8.373092,5.136413,6.309066],[7.207858,-1.406443,5.928844,2.641434,0.412854],[-6.519560,9.779822,-8.957074,5.361002,9.969691],[3.373357,5.546222,-0.831826,-6.545484,5.641043],[9.470319,-5.464288,-5.984630,5.032269,-7.652742],[-2.080111,2.219708,4.244402,-2.252333,-5.913258],[9.188816,7.356392,-0.561614,-3.131457,-2.361240],[-0.841944,1.926399,1.594833,-5.401240,0.456637],[4.302416,-1.028424,5.404878,-8.942932,-8.794347],[8.952813,3.285690,-4.293240,0.383060,-4.737197],[-6.868662,0.670270,5.991938,3.988354,4.511723],[-3.538923,-5.838601,-1.542354,4.082820,-7.484171],[2.198518,3.343236,-2.475123,-1.283179,9.651377],[1.772834,-1.526660,1.955999,-5.165847,6.707697],[0.025571,-5.834863,-0.977675,4.627317,-6.133189]],[[6.701334,-0.049697,-2.706130,7.057696,-8.040575],[0.901613,-4.660058,-1.753625,3.432727,1.205469],[-2.538630,9.548141,-4.479327,2.392090,8.231575],[1.082367,-0.759657,1.990314,1.773213,3.367701],[0.466447,7.435855,-2.588152,1.301183,-0.956083],[3.047138,8.552645,-9.307589,-9.831733,-5.165630],[9.536651,9.134550,1.812767,-8.168653,8.632645],[-3.930809,-6.968042,-4.958387,3.313888,-4.063909],[-2.154786,-8.269818,-3.583211,-5.330217,7.176963],[-0.045120,-2.776804,-1.976066,6.270804,-5.573373],[-5.042215,3.827045,1.729124,-9.634531,-7.102940],[-9.807341,-9.824483,-0.065039,3.305397,7.859545],[5.653602,5.323319,3.033236,4.801567,-6.985977],[0.547698,-6.983403,0.738756,8.043643,-7.078951],[8.364198,-2.686675,-3.308989,-7.088581,6.140053]]], dtype = "float32")#candidate|2661|(7, 15, 5)|const|float32
bop_2662 = relay.power(call_2631.astype('float32'), const_2661.astype('float32')) # shape=(7, 15, 5)
bop_2665 = relay.power(call_2632.astype('float32'), const_2661.astype('float32')) # shape=(7, 15, 5)
uop_2669 = relay.atanh(bop_2662.astype('float64')) # shape=(7, 15, 5)
uop_2671 = relay.atanh(bop_2665.astype('float64')) # shape=(7, 15, 5)
func_2068_call = mod.get_global_var('func_2068')
func_2069_call = mutated_mod.get_global_var('func_2069')
call_2683 = relay.TupleGetItem(func_2068_call(), 1)
call_2684 = relay.TupleGetItem(func_2069_call(), 1)
func_399_call = mod.get_global_var('func_399')
func_401_call = mutated_mod.get_global_var('func_401')
call_2687 = relay.TupleGetItem(func_399_call(relay.reshape(call_2683.astype('float32'), [6, 6, 2])), 0)
call_2688 = relay.TupleGetItem(func_401_call(relay.reshape(call_2683.astype('float32'), [6, 6, 2])), 0)
func_2548_call = mod.get_global_var('func_2548')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_2693 = func_2548_call()
call_2694 = func_2548_call()
func_1527_call = mod.get_global_var('func_1527')
func_1530_call = mutated_mod.get_global_var('func_1530')
const_2697 = relay.const([10,6,3,-8,-9,-4,-5,5,7,8,8,-2,-5,-1,9,-9,-8,-1,-6,-4,7,7,10,-2,3,-7,-6,-9,3,1,2,3,4,2,6,-4,-3,-4,7,10,-8,1,5,-4,-10,2,-4,1,-10,9,-1,8,-5,9,-2,10,-7,3,-8,8,-3,-9,5,6,-7,3,5,-3,6,2,2,-8,-10,-9,-10,-8,9,-2,9,2,-1,3,-10,8,-10,-4,2,-3,4,1,-1,9,-6,6,8,-9,-7,-9,-1,-3,-9,3,-10,2,-8,-10,-3,1,-3,-5,9,2,-10,-10,-1,-2,-1,-10,3,5,-8,-2,-7,2,-2,-10,5,-6,6,6,1,6,2,1,1,-7,-4,-9,6,2,10,-10,8,10,3,1,-3,-6,-4,-10,-4,3,-10,2,8,3,-5,-5,-8,-7,10,-5,-7,-7,7,-8,-6,10,5,-1,5,3,6,5,2,5,1,6,-10,-9,-2,-9,-7,-6,10,-7,1,6,-5,-3,2,10,9,-9,1,-5,4,5,4,6,-1,10,-3,1,-5,7,-2,1,5,8,10,10,9,5,-9,9,4,-1,-4,-4,-5,-8,-8,-6,-1,-8,2,-2,7,6,8,3,-3,-8,-7,7,1,-8,-4,-1,-3,-5,1,5,7,-2,-5,7,-1,6,-7,-1,8,-7,-8,-7,-9,3,10,-8,1,1,6,5,-5,7,-4,8,10,4,4,-8,-4,3,-10,10,-2,9,-9,7,-5,-5,5,-9,-9,-4], dtype = "uint16")#candidate|2697|(286,)|const|uint16
call_2696 = relay.TupleGetItem(func_1527_call(relay.reshape(const_2697.astype('uint16'), [2, 13, 11]), relay.reshape(const_2697.astype('uint16'), [2, 13, 11]), ), 1)
call_2698 = relay.TupleGetItem(func_1530_call(relay.reshape(const_2697.astype('uint16'), [2, 13, 11]), relay.reshape(const_2697.astype('uint16'), [2, 13, 11]), ), 1)
output = relay.Tuple([bop_2642,uop_2669,call_2683,call_2687,call_2693,call_2696,const_2697,])
output2 = relay.Tuple([bop_2645,uop_2671,call_2684,call_2688,call_2694,call_2698,const_2697,])
func_2700 = relay.Function([var_2640,], output)
mod['func_2700'] = func_2700
mod = relay.transform.InferType()(mod)
mutated_mod['func_2700'] = func_2700
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2701 = relay.var("var_2701", dtype = "int8", shape = (900,))#candidate|2701|(900,)|var|int8
func_2700_call = mutated_mod.get_global_var('func_2700')
call_2702 = func_2700_call(var_2701)
output = call_2702
func_2703 = relay.Function([var_2701], output)
mutated_mod['func_2703'] = func_2703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1110_call = mod.get_global_var('func_1110')
func_1112_call = mutated_mod.get_global_var('func_1112')
call_2736 = relay.TupleGetItem(func_1110_call(), 0)
call_2737 = relay.TupleGetItem(func_1112_call(), 0)
var_2753 = relay.var("var_2753", dtype = "float32", shape = (7, 15, 2))#candidate|2753|(7, 15, 2)|var|float32
bop_2754 = relay.logical_xor(call_2736.astype('uint64'), var_2753.astype('uint64')) # shape=(7, 15, 2)
bop_2757 = relay.logical_xor(call_2737.astype('uint64'), var_2753.astype('uint64')) # shape=(7, 15, 2)
uop_2760 = relay.atan(bop_2754.astype('float32')) # shape=(7, 15, 2)
uop_2762 = relay.atan(bop_2757.astype('float32')) # shape=(7, 15, 2)
func_2338_call = mod.get_global_var('func_2338')
func_2341_call = mutated_mod.get_global_var('func_2341')
const_2779 = relay.const([-7.563740,5.897874,3.118089,9.934002,-5.475425,7.689419,5.556552,8.006137,-3.853119,3.785322,-1.331748,9.593904,1.521688,-9.124427,-6.918854,-2.919590,-0.020300,-7.068490,1.624010,3.455409,-8.251495,-7.520211,-0.457066,3.886638,2.957640,4.670953,8.868722,-5.686201,-6.599197,-6.323218,-2.469300,0.834920,-1.285013,-5.596704,8.465111,2.085253,-3.150533,4.037392,8.756890,4.047989,-1.301088,-4.068283,1.657415,-7.919322,5.282090,-6.701850,-4.516212,-2.959289,3.295708,-0.262591,2.849432,0.654878,3.453751,-0.993718,0.004702,0.769443,-0.812022,4.882807,-9.761140,0.687383,-1.800422,-4.906423,-3.294643,1.902779,2.555420,-3.240730,2.970302,4.168106,7.717065,-7.899265,7.306852,-1.731950,4.889868,-4.291923,9.547535,-1.614289,8.803222,-0.660353,9.644603,-1.654136,1.263301,4.029712,-7.155687,5.403623,-1.259487,-9.621637,7.743777,9.848499,-2.028354,4.519261,-7.533844,-4.927073,-2.808940,6.326639,-1.681151,-6.576831,-1.025954,5.550301,-9.334860,-9.972170,-4.954502,2.280323,2.872401,-6.286147,-8.155904,-1.095179,3.101105,-3.932792,6.835942,-1.671708,8.185226,-2.573020,-9.214830,-3.802344,-4.641577,-9.872473,2.291774,9.579002,-3.672842,7.397875,0.315087,4.021163,-6.474714,-7.442248,5.140436,1.977022,0.805985,5.932076,3.292768,5.908252,-8.547303,-0.404165,2.928057,4.857729,-3.046117,-3.704465,-7.396155,-1.444901,1.408363,-7.635501,1.869276,-5.865171,5.485131,7.633862,1.566989,0.999138,-9.283213,-4.904983,3.677418,7.833959,-0.497516,7.352263,-7.202382,9.813080,-8.257061,-8.836229,0.840474,-6.270594,-5.738278,-7.421977,-1.619705,-0.547477,5.616498,-4.143359,-6.617318,-4.953479,5.324910,4.150283,-9.273302,-1.052157,-2.140391,-5.097949,1.728399,7.189751,-4.473998,8.817002,3.374214,6.646926,-8.041713,8.363940,-1.259131,8.809882,7.952863,4.949255,3.057910,-7.133473,-4.102411,-5.999843,0.069667,-0.912271,0.827037,0.822662,3.547499,9.682291,-2.918344,-6.720684,1.551227,2.100324,-5.851783,-1.955645,-7.386391,2.351559,7.872807,-8.070787,8.220906,0.191210,-3.779896,1.595107,2.357245,-0.303561,2.900397,-1.059711,-1.608301,9.376433,-8.965386,6.600272,-6.075896,-0.385870,-9.194044,3.385907,5.537833,-0.541839,2.553614,3.105595,-1.289209,-3.839608,-3.817113,-7.064158,-2.407176,2.938966,4.647533,0.388432,8.374596,-1.977895,-2.403886,-5.591555,-0.231975,-6.440158,-1.309728,-9.542296,2.585868,7.954405,-4.588127,-5.613007,3.450503,1.755492,-8.746405,9.952334,-5.234226,5.550737,8.832172,-9.432392,-0.757508,5.558800,-9.577742,-8.194627,-2.476080,0.004802,8.709559,-2.365559,9.784829,-3.926669,-7.029777,-0.676927,7.447718,-3.567761,8.564403,-1.215425,5.304450,-2.592858,7.341028,5.987124,-0.284569,-8.469166,-1.245673,6.272837,4.035523,-2.734737,3.013232,-0.690442,-2.589140,0.738107,-5.708878,-4.649602,8.678450,1.501679,6.017070,-4.667616,-0.253287,9.055298,1.728405,-4.975601,-4.183794,6.838978,7.306775,-2.805806,-3.735832,0.191184,1.754984,-3.651048,2.284149,-8.032397,-8.687316,-2.834334,5.006666,6.330669,-5.283170,6.666799,-6.017336,-9.977303,6.671759,-8.121644,-9.462608,-5.190139,7.423583,-0.843226,-2.950009,7.044338,-4.114418,0.041168,4.775659,-2.203963,8.506729,5.742644,-9.232867,5.212668,-0.274124,2.079259,-4.182468,0.549290,-7.860737,-8.956351,-8.503022,5.428294,3.190233,-3.205255,-5.201624,8.742767,4.562174,7.702451,-4.203932,2.958764,-9.183261,-6.709523,-0.169768,-9.538238,7.874153,7.970766,-5.336614,-2.740970,-9.370102,8.120564,-8.770190,-2.774985,4.992163,5.675377,-1.214088,-4.590703,-6.602507,6.742086,-4.224341,2.473287,-6.195831,3.382709,-6.795326,0.122139,4.111711,1.286800,9.597207,2.234231,9.999661,-8.827706,6.989794,1.551724,8.013096,-3.979751,-3.780632,-9.573096,-4.447380,-1.073179,2.662128,2.237133,-4.565211,-5.387203,-6.171595,-0.077950,6.266084,-6.906542,7.257606,-6.013149,-7.026277,2.917626,-1.985281,-6.343500,9.697473,9.449618,-2.334412,2.167635,9.730110,-6.754485,3.761125,-8.316749,3.778214,8.204030,-8.614204,-5.929634,-8.782501,3.585753,3.010767,-6.516956,-9.844750,9.367449,-2.070863,9.761521,2.630566,-9.845138,-4.295350,1.635456,9.408344,4.592586,-8.883281,-4.452948,1.574290,2.705210,9.160913,5.336320,-2.751539,-6.235501,-9.732126,-8.419271,9.080586,-5.135209,6.228036,-4.621733,0.074773,-8.358772,1.980366,-5.665900,1.259915,9.403944,0.677104,-1.255701,1.231936,0.630751,9.908402,8.408287,-0.867812,-9.454820,9.931467,-6.605545,-9.148306,-4.098951,8.984899,-7.673497,8.508007,-6.825739,3.475131,-9.106530,7.960325,-6.377663,7.151434,-3.173085,8.950539,-2.856605,1.975786,1.551516,8.496411,5.230227,3.054829,4.012915,4.444677,2.132936,4.791281,4.305863,8.610264,7.012066,-0.196104,-2.303476,-2.653912,-7.891047,5.920058,-2.418718,-7.791369,-9.414785,6.504882,-8.327528,4.518297,2.274230,1.270502,9.166069,-3.830504,9.344225,-6.838371,8.888304,-0.573029,-6.224190,2.270898,3.088024,-7.934087,9.766731,1.126265,-7.741971,-7.784644,6.622004,5.157372,-3.237188,9.883218,-6.640402,-0.066758,3.063917,2.440581,-8.124753,-1.985118,-7.227114,9.328098,-8.917835,2.944497,2.820047,9.907030,0.366309,-0.539505,-7.681963,-4.053911,5.309980,-6.834615,2.640627,6.573612,7.359695,3.031642,-0.581102,5.142968,-5.996775,-3.386092,-0.825185,-4.125814,-4.335598,-2.696748,0.193351,8.978540,9.852763,3.844447,9.365678,-7.530234,-8.788042,5.699783,5.859479,7.593478,1.623984,6.586173,9.254531,-8.877832,-9.254108,0.374577,2.927101,4.228033,-9.279296,9.218016,3.489803,-0.116746,-1.901189,-5.172220,1.694367,7.540246,0.483272,-1.531369,-1.922455,-5.428796,0.021928,-3.461079,-2.214208,3.084803,-4.412441,8.155819,3.439862,4.881473,3.339288,3.459667,-9.963324,4.924959,5.167754,-8.130828,-1.770435,3.135445,-3.594148,-7.871338,5.423411,-6.134058,1.432177,5.019773,6.483601,-3.545798,-9.525950,6.528121,-7.649700,4.381490,9.865244,8.764397,-6.560656,0.250416,1.402133,-1.805566,-5.276329,-7.321517,-8.942961,-3.673542,7.436512,-5.394772,-5.845382,-5.920370,-0.403009,-3.978998,7.127345,-4.181862,-3.467927,9.799051,3.245257,-9.137781,-7.626653,9.837970,-6.947277,-5.149819,-7.938454,-5.323336,7.035520,4.306547,-6.453601,1.390583,-5.817642,0.083514,1.837968,-6.711119,-4.940840,-1.836998,9.591664,1.519287,4.725542,7.010720,-4.312176,-4.516410,-9.087461,-9.391336,-5.779503,6.337338,6.104939,9.698952,1.350321,8.341749,5.847177,-3.366747,-0.601430,-7.822950,6.162101,5.066766,7.587089,4.960993,-7.155100,-2.100163,1.311601,1.110719,8.249297,-8.439966,-2.654626,-1.660435,4.105162,-9.164166,2.701358,-1.765680,4.465831,-0.671177,2.973535,-2.189684,3.362776,-6.335810,-5.027709,6.270453,4.417728,-5.759360,-3.870943,5.856659,2.705174,9.608325,-5.772095,-5.213590,2.304267,7.214857,-6.933180,-1.476010,-1.815189,7.487761,-0.296081,-8.109847,-1.174888,8.056916,-0.313494,-5.001148,1.500502,-6.593193,6.239447,7.205276,7.870502,-6.268555,-6.275267,-0.571781,7.845775,-7.917589,-9.801450,2.103913,6.518455,2.863835,9.710062,-7.079403,3.139324,7.306140,3.394117,-1.517013,3.351957,-3.465851,8.236287,-2.183138,-1.852109,4.664987,-1.771098,2.667255,7.595361,2.400204,9.278212,9.550128,-8.483375,8.945226,9.763628,-8.652760,-6.240739,3.699509,2.357576,4.502643,-8.984369,3.717139,0.108912,-1.847197,8.229724,-9.317618,4.367610,-2.350533,-9.212677,8.334020,5.189949,-6.959543,4.620526,9.836850,7.359071,-5.823475,4.536127,-5.660428,1.255047,-4.359422,-7.820040,2.472323,-0.251512,4.880380,0.021369,5.704355,4.280307,3.850746,5.383425,9.268930,9.545641,-4.791196,2.985971,9.933765,0.237716,-5.761454,-8.821985,-9.881928,3.537383,4.113883,-3.575388,0.066405,-4.818555,-4.424215,6.962347,4.466836,-9.216144,-0.458902,-4.347432,-7.817305,0.352301,-2.114842,-2.214192,-8.779119,-1.524105,-1.131603,-3.782866,-7.930774,-8.373353,-1.035233,7.271323,-4.529726,0.436993,4.747756,6.391113,-7.423609,-4.042818,-3.314956,8.681787,-1.059393,6.352871,-6.600543,-4.170563,-8.015325,-4.788503,6.165761,-2.364192,2.262770,-3.986969,-0.763707,-5.364886,-1.928858,5.941539,5.374960,0.445576,-8.870177,-0.835943,7.795138,-3.656906,-4.890542,-7.645481,-2.632105,2.572084,1.874814,-3.198757,3.568006,-3.863256,-8.567767,1.428402,-0.462980,7.883048,4.113371,1.305280,6.417551,-1.369196,-4.557249,3.760252,-5.529046,-7.743765,-0.527590,2.783830,2.540108,5.049534,4.251193,7.447140,2.650796,-5.828612,1.680629,8.692427,3.276474,-4.278500,8.014060,-6.150422,-3.552296,1.142868,-3.047182,8.174203,-1.239599,3.023494,5.754763,7.789220,6.235507,1.801522,0.107514,6.397058,-1.322649,5.019463,0.127271,5.895458,-3.231180,-4.525627,6.282910,0.217574,-6.340493,8.269910,0.055296,3.358374,0.912417,4.567384,5.204309,9.351076,-2.115561,0.276242,1.607768,-0.538458,0.846568,-9.404131,-2.062946,-3.489265,-6.591075,-9.195710,-0.360846,-4.430872,-2.750948,9.145021,4.005070,8.713391,6.839324,1.140364,-7.528722,-3.533994,1.769205,-6.758169,-9.797972,-5.459957,4.566239,4.264913,-0.618515,5.522500,1.004835,6.152119,9.410571,9.321003,8.263466,7.341208,-6.652842,-0.607328,-9.266773,2.404694,0.679413,0.900352,-3.680832,0.440752,9.736306,1.125214,2.639414,7.755390,0.410479,2.826878,4.909878,-6.042677,-2.551622,4.296738,-1.442739,-3.527878,3.145215,-8.081310,-6.036347,-6.712340,-0.284106,-7.309122,-0.859960,-0.137093,-0.246151,5.109195,8.671276,8.997788,-4.950232,-8.331889,9.777949,-2.825844,1.920873,-1.907054,-6.472190,5.511682,-3.940674,-3.967081,6.218068,9.756579,-7.538908,3.863453,-7.748377,-1.759494,-2.792561,4.868820,2.777805,-8.289992,-0.296132,-7.052778,4.965320,5.710214,6.136729,3.095410,0.660894,5.627527,9.880409,1.481599,4.329778,-6.224522,-5.465804,-9.722254,6.433080,-9.058971,3.653889,2.647849,-2.582577,0.478073,-1.468656,-6.293448,4.036067,-2.652723,6.083755,-4.256739,2.855858,-7.442585,6.762930,1.286203,9.335372,-7.658562,-0.062642,8.846200,2.149638,-8.744873,6.551731,4.539404,-4.939687,8.518738,0.580476,3.950985,-4.784450,-9.684282,-9.913906,1.943568,-4.300654,-4.397988,8.527353,3.800348,-9.099815,-2.715309,8.792167,-7.187748,3.803417,4.323037,-3.457807,1.487449,-3.971363,-6.385607,9.680716,-9.766146,3.321830,-3.559493,-0.007647,5.873789,-7.510883,5.048105,8.374558,2.726027,3.669398,8.447147,4.222745,6.480171,4.883687,-0.012860,4.811094,-1.703141,-9.898742,8.628567,-7.031312,3.417397,-3.057617,-9.351489,6.448041,2.145239,-0.282324,-1.061877,9.180589,7.618109,0.545182,-6.315714,-4.115172,0.991079,6.035880,-6.259031,-9.319615,-6.210520,-8.234470,-7.058434,2.139709,-4.174138,7.278857,3.405908,-0.198986,5.432021,1.063549,-5.979467,-4.201665,-2.228177,-7.124870,9.966576,-9.756649,-8.436567,1.084272,-5.236969,-7.866694,-6.249389,1.913369,-9.697501,4.090736,8.781666,6.151690,-3.769093,-1.336009,-7.552944,0.261098,4.934280,9.841216,-7.385965,-8.413009,0.368146,-5.731731,-4.396473,-9.878136,7.606294,-3.364820,-0.474955,3.851545,5.663950,6.242989,-3.016462,-1.230455,-1.051356,5.558827,-8.016174,-1.192921,-0.531756,0.753245,-1.963710,-8.925262,1.039899,6.976752,-4.607975,3.494318,-1.303457,1.596766,6.536770,-1.859373,-0.940959,0.373748,6.895622,-9.170058,-0.087245,0.994698,3.745335,-7.204363,-0.289386,-9.594156,-9.767453,2.754783,-1.814834,-2.415464,-4.029902,-4.037495,-6.952269,3.886641,8.239393,-1.650986,2.898970,-4.186723,3.167308,-8.824736,-0.849062,-0.754431,-0.288579,7.717906,4.674344,-0.978412,-9.796697,-2.840058,-2.783741,9.057916,9.804058,9.741430,6.971575,-6.943063,8.526943,-3.666006,0.116248,-0.513312,-1.459007,9.306698,4.704936,0.884035,-3.646614,7.785913,6.920376,-7.464433,-0.138249,-9.002529,3.428604,-3.162252,3.026938,5.100612,8.308767,-9.223016,4.724172,0.962251,2.889147,5.362388,-3.255208,2.411488,6.397816,5.173931,9.224911,0.795445,-4.699412,4.007431,-5.231171,-4.868812,0.988175,-3.994031,-0.815099,0.287291,-1.640586,7.219737,7.261832,9.698330,-3.876865,-0.079571,-0.095186,4.008715,6.677393,-2.985346,1.255867,-9.647410,2.771383,6.421406,-0.285709,6.965099,3.932033,-4.177491,5.966023,2.928651,-1.283338,-5.529111,0.648480,4.040553,-7.907939,9.611273,-0.677757,-5.618112,-5.683142,-2.449938,1.171359,9.804751,-4.607999,1.431759,5.830374,-2.060076,0.586595,-8.816399,-2.303439,1.685200,8.074014,-3.611046,-2.152716,5.021771,-2.761837,-8.389999,-5.869477,8.659685,8.005253,-4.049577,8.622477,-4.101427,4.449754,-3.662280,-0.765315,3.832903,-9.362565,7.031533,-2.248448,6.942463,-7.847109,-6.588529,3.132983,-7.202309,8.178456,-1.202516,0.013015,5.617683,7.721370,-1.006173,5.331884,-0.916852,4.401087,6.092735,-9.107076,-3.227116,-5.368921,3.253239,-0.961400,-6.323207,2.255066,2.344877,3.559186,2.261230,-5.446086,-2.878136,7.179962,4.961772,-2.165557,9.896379,3.092366,-3.281782,-6.121512,0.566853,5.377600,-2.343402,-0.213989,9.090197,-1.418639,6.694557,-1.522479,2.571172,-7.643244,-8.501401,8.077119,5.406104,6.666608,-4.476462,-4.686127,1.729779,6.835486,-0.570805,7.068576,6.132798,-9.120530,-6.899101,-5.607903,1.984949,-5.889938,0.593003,0.820914,-8.873953,-9.244018,-0.403658,-6.075387,-1.006687,-5.794048,-4.252616,-0.478669,5.867795,-6.713631,9.155044,2.443656,0.947083,-0.987060,4.934145,4.086947,2.749968,-8.610341,-5.063776,1.008342,-2.978005,0.641355,7.215527,-7.345506,6.441859,-2.224052,7.796639,6.116429,8.790775,-3.051472,4.064652,-4.124530,0.948139,-0.392183,6.935517,5.836599,9.666908,-6.787925,-9.686356,-3.003668,1.603170,9.398829,-6.543335,3.551848,-0.682655,4.498848,-2.401708,-6.309681,-9.246228,7.259415,-3.299659,-8.506003,-9.308170,-8.798603,6.424559,-6.783249,0.435675,-4.633202,-9.836099,3.928641,0.987186,-3.667551,-4.855101,2.719409,3.372499,3.627626,4.566668,-4.229921,-6.693447,0.136886,5.246651,4.425234,7.558368,-1.737270,5.295718,-7.433074,-0.011833,-1.042736,-2.835710,-5.008107,4.157387,6.179188,1.343046,-4.847849,4.791427,6.897732,8.811271,9.105314,-5.242490,-2.986900,-3.632357,-4.291971,4.214428,1.883991,9.200584,1.319953,9.124565,9.384972,-6.559572,3.652364,2.974031,-1.944120,6.714087,1.069883,-1.290313,7.885926,4.843699,2.877535,6.053390,-1.885919,-2.700060,3.679898,-4.932096,-6.467795,-4.177963,-9.542994,6.845010,-8.418407,9.592440,-0.752353,9.037444,-4.811735,-7.239653,0.880722,-9.351505,-0.839394,3.888023,9.117386,-1.598508,1.998432,3.125765,9.635855,-2.540257,5.549012,5.009794,1.749105,7.414703,3.609381,-8.013160,4.894804,-8.546285,9.741901,5.046701,-3.229682,9.936632,-5.360646,0.319745,2.765268,0.263872,7.080482,-5.953072,9.459794,-2.943867,7.189826,1.947006,-3.971999,-4.633314,-1.919879,-7.751777,-9.012040,-7.236696,-7.127940,-6.665188,8.835448,-7.661502,-9.113630,-1.390939,-2.340426,1.762511,1.454946,6.313682,-8.831788,7.564426,5.790010,9.459993,2.561701,7.612773,-0.195682,2.971948,2.021456,-7.093533,5.641426,-7.066926,-2.788029,2.353084,-2.446672,0.563599,5.517176,9.681749,-2.375907,-8.655370,-7.287356,6.264267,6.647600,2.010350,-8.837597,-1.117258,-2.903133,0.300213,-3.652637,-7.422505,7.056649,-5.539953,-5.395700,-6.566404,-0.999808,3.958339,-7.095922,7.145901,2.467022,-8.921056,0.185914,3.246163,8.558950,-1.928765,-5.795305,4.487218,-4.691059,-5.480659,5.852650,0.294756,1.097592,6.815137,7.955394,2.658214,3.689616,-6.130661,-0.869347,-8.796467,-3.758040,-3.884708,3.357577,0.170422,5.365048,-9.164485,-8.402439,-5.873931,-1.723924,9.468245,9.976848,5.469530,-3.299834,5.174490,1.587453,5.317091,-2.665978,-1.325138,2.247643,1.905099,1.031863,4.929469,7.319258,5.311776,4.449593,0.571141,6.436234,5.801020,-3.927656,5.255742,-2.230984,7.031596,-3.190286,-0.411901,0.069264,-6.238391,-2.091416,-3.228517,4.024117,2.494045,-5.132125,9.856090,9.019517,-6.430906,2.655396,-8.071878,-9.692822,-6.911571,8.492377,-6.080765,-3.724775,-4.690239,-8.510413,-1.257117,-2.304057,0.391553,-8.855168,7.538979,0.285234,5.299204,9.393773,9.666355,-7.038721,-0.276408,-9.240506,-4.302680,5.408411,8.626983,-3.194572,4.392746,-6.635667,6.187835,-2.120261,-3.431750,-5.122755,-3.683838,1.451886,2.482636,-2.473168,-1.096339,-0.181124,7.868489,7.619730,-7.287635,3.314702,-9.314023,-6.693038,-7.673143,-1.259841,-1.714551,2.227049,-5.533130,-7.158741,-6.289739,2.239116,-6.193985,2.004827,2.862303,-8.050063,-5.103849,-1.717785,8.918936,3.327401,5.821535,1.093815,-1.274584,-6.100986,7.498153,8.957953,3.713141,-3.814320,-1.863606,-4.138902,-5.864389,0.861263,-7.842937,-0.969600,-1.652467,1.437498,4.785630,-5.956234,4.928999,2.958090], dtype = "float64")#candidate|2779|(1680,)|const|float64
const_2780 = relay.const([[True,False,True,True,True,False,True],[True,False,True,True,True,False,True],[False,True,False,True,True,True,False],[False,False,False,False,True,True,False],[False,False,True,True,False,False,False],[False,False,False,True,False,True,False],[True,True,True,True,True,False,False],[False,True,False,False,True,True,False],[True,False,True,True,False,False,False],[True,False,True,True,False,True,False],[False,False,True,True,False,False,True],[True,False,True,True,True,False,True],[True,True,True,False,True,False,True],[True,False,True,False,False,False,True],[False,True,False,False,False,True,False],[False,True,True,True,False,False,False],[True,False,True,False,True,False,False],[False,True,True,False,True,True,False],[False,True,False,False,True,False,True],[True,True,True,True,False,False,False],[False,False,False,False,True,True,False],[False,True,True,True,False,False,True],[False,True,True,False,True,True,False],[False,True,True,True,False,False,False],[True,False,False,True,True,False,True],[False,True,False,False,False,True,True],[True,True,False,True,True,False,True],[False,True,True,False,True,True,True],[True,True,True,False,False,True,False],[True,True,True,True,False,True,True],[False,False,True,True,False,True,False],[True,True,True,True,True,True,True],[False,False,False,True,True,True,False],[True,False,False,False,True,True,True],[True,True,True,True,True,False,True],[True,True,True,False,True,True,True],[False,False,False,False,False,False,True],[True,True,True,True,True,True,True],[False,True,True,True,False,False,True],[True,False,False,True,True,True,True],[False,False,True,False,False,True,False],[False,False,False,False,True,True,True],[True,True,False,True,False,True,True],[False,True,False,True,True,False,False],[True,True,False,True,False,True,False],[False,False,False,True,False,False,True],[False,False,False,True,True,False,False],[True,False,True,True,True,True,False],[True,True,True,False,True,True,True],[True,False,True,True,False,False,False],[True,False,True,True,False,True,False],[True,False,False,False,False,False,True],[True,True,False,False,True,True,False],[False,False,False,True,False,True,False],[False,True,True,True,False,False,False]], dtype = "bool")#candidate|2780|(55, 7)|const|bool
call_2778 = relay.TupleGetItem(func_2338_call(relay.reshape(const_2779.astype('float64'), [7, 15, 16]), relay.reshape(const_2780.astype('bool'), [55, 7]), ), 5)
call_2781 = relay.TupleGetItem(func_2341_call(relay.reshape(const_2779.astype('float64'), [7, 15, 16]), relay.reshape(const_2780.astype('bool'), [55, 7]), ), 5)
bop_2794 = relay.floor_divide(call_2736.astype('float32'), const_2779.astype('float32')) # shape=(7, 15, 1680)
bop_2797 = relay.floor_divide(call_2737.astype('float32'), const_2779.astype('float32')) # shape=(7, 15, 1680)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
var_2802 = relay.var("var_2802", dtype = "int8", shape = (900,))#candidate|2802|(900,)|var|int8
call_2801 = relay.TupleGetItem(func_2406_call(relay.reshape(var_2802.astype('int8'), [900,])), 2)
call_2803 = relay.TupleGetItem(func_2408_call(relay.reshape(var_2802.astype('int8'), [900,])), 2)
func_1527_call = mod.get_global_var('func_1527')
func_1530_call = mutated_mod.get_global_var('func_1530')
var_2807 = relay.var("var_2807", dtype = "uint16", shape = (286,))#candidate|2807|(286,)|var|uint16
call_2806 = relay.TupleGetItem(func_1527_call(relay.reshape(var_2807.astype('uint16'), [2, 13, 11]), relay.reshape(var_2807.astype('uint16'), [2, 13, 11]), ), 1)
call_2808 = relay.TupleGetItem(func_1530_call(relay.reshape(var_2807.astype('uint16'), [2, 13, 11]), relay.reshape(var_2807.astype('uint16'), [2, 13, 11]), ), 1)
output = relay.Tuple([uop_2760,call_2778,const_2780,bop_2794,call_2801,var_2802,call_2806,var_2807,])
output2 = relay.Tuple([uop_2762,call_2781,const_2780,bop_2797,call_2803,var_2802,call_2808,var_2807,])
func_2811 = relay.Function([var_2753,var_2802,var_2807,], output)
mod['func_2811'] = func_2811
mod = relay.transform.InferType()(mod)
mutated_mod['func_2811'] = func_2811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2811_call = mutated_mod.get_global_var('func_2811')
var_2813 = relay.var("var_2813", dtype = "float32", shape = (7, 15, 2))#candidate|2813|(7, 15, 2)|var|float32
var_2814 = relay.var("var_2814", dtype = "int8", shape = (900,))#candidate|2814|(900,)|var|int8
var_2815 = relay.var("var_2815", dtype = "uint16", shape = (286,))#candidate|2815|(286,)|var|uint16
call_2812 = func_2811_call(var_2813,var_2814,var_2815,)
output = call_2812
func_2816 = relay.Function([var_2813,var_2814,var_2815,], output)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2828 = relay.var("var_2828", dtype = "int8", shape = (15, 15, 14))#candidate|2828|(15, 15, 14)|var|int8
var_2829 = relay.var("var_2829", dtype = "int8", shape = (15, 15, 14))#candidate|2829|(15, 15, 14)|var|int8
bop_2830 = relay.greater(var_2828.astype('bool'), relay.reshape(var_2829.astype('bool'), relay.shape_of(var_2828))) # shape=(15, 15, 14)
output = relay.Tuple([bop_2830,])
output2 = relay.Tuple([bop_2830,])
func_2836 = relay.Function([var_2828,var_2829,], output)
mod['func_2836'] = func_2836
mod = relay.transform.InferType()(mod)
mutated_mod['func_2836'] = func_2836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2836_call = mutated_mod.get_global_var('func_2836')
var_2838 = relay.var("var_2838", dtype = "int8", shape = (15, 15, 14))#candidate|2838|(15, 15, 14)|var|int8
var_2839 = relay.var("var_2839", dtype = "int8", shape = (15, 15, 14))#candidate|2839|(15, 15, 14)|var|int8
call_2837 = func_2836_call(var_2838,var_2839,)
output = call_2837
func_2840 = relay.Function([var_2838,var_2839,], output)
mutated_mod['func_2840'] = func_2840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_2866 = func_580_call()
call_2867 = func_580_call()
var_2868 = relay.var("var_2868", dtype = "float32", shape = (7, 15, 9))#candidate|2868|(7, 15, 9)|var|float32
bop_2869 = relay.less(call_2866.astype('bool'), var_2868.astype('bool')) # shape=(7, 15, 9)
bop_2872 = relay.less(call_2867.astype('bool'), var_2868.astype('bool')) # shape=(7, 15, 9)
func_678_call = mod.get_global_var('func_678')
func_679_call = mutated_mod.get_global_var('func_679')
call_2875 = func_678_call()
call_2876 = func_678_call()
bop_2885 = relay.multiply(call_2875.astype('int8'), bop_2869.astype('int8')) # shape=(7, 15, 9)
bop_2888 = relay.multiply(call_2876.astype('int8'), bop_2872.astype('int8')) # shape=(7, 15, 9)
bop_2890 = relay.minimum(bop_2869.astype('uint16'), call_2875.astype('uint16')) # shape=(7, 15, 9)
bop_2893 = relay.minimum(bop_2872.astype('uint16'), call_2876.astype('uint16')) # shape=(7, 15, 9)
bop_2898 = relay.equal(var_2868.astype('bool'), call_2875.astype('bool')) # shape=(7, 15, 9)
bop_2901 = relay.equal(var_2868.astype('bool'), call_2876.astype('bool')) # shape=(7, 15, 9)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_2909 = func_1830_call()
call_2910 = func_1830_call()
output = relay.Tuple([bop_2885,bop_2890,bop_2898,call_2909,])
output2 = relay.Tuple([bop_2888,bop_2893,bop_2901,call_2910,])
func_2916 = relay.Function([var_2868,], output)
mod['func_2916'] = func_2916
mod = relay.transform.InferType()(mod)
mutated_mod['func_2916'] = func_2916
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2917 = relay.var("var_2917", dtype = "float32", shape = (7, 15, 9))#candidate|2917|(7, 15, 9)|var|float32
func_2916_call = mutated_mod.get_global_var('func_2916')
call_2918 = func_2916_call(var_2917)
output = call_2918
func_2919 = relay.Function([var_2917], output)
mutated_mod['func_2919'] = func_2919
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2954 = relay.const([[[-6.103845,3.540702,3.634033],[-1.373893,-3.212633,5.625533],[8.634710,-0.057180,-6.905531],[-4.718926,-2.667705,2.930290],[7.546011,-8.676447,4.102344],[8.959631,3.187684,3.057715],[0.644630,-7.183526,2.295596],[4.647284,5.509033,-2.030460],[-4.088272,8.732304,8.625689]],[[-0.806875,-4.508327,-4.514771],[-4.507897,4.121862,-5.052684],[-7.540623,-3.654506,4.346695],[-0.234417,9.418875,-4.497458],[0.585219,-4.202412,4.370618],[5.657863,-4.354931,-6.997565],[6.747315,-5.962324,-7.020304],[5.794284,-6.588005,1.443331],[-2.086456,-3.856079,8.897732]]], dtype = "float64")#candidate|2954|(2, 9, 3)|const|float64
const_2955 = relay.const([[[6.629620,3.900967,-3.249384],[-0.791938,-1.037816,7.414175],[1.470441,4.381719,-5.866269],[-8.774438,-3.745749,-3.302571],[-2.892632,-1.919609,3.051892],[-0.192785,4.390195,3.865936],[0.422544,-6.292298,-1.328850],[6.763818,6.767096,2.338811],[-6.345079,-6.933087,2.348008]],[[6.039205,3.872373,3.385828],[3.754530,-3.304284,8.771575],[-1.158681,7.499232,5.798747],[-9.985569,-8.325737,8.822519],[9.146425,5.020590,-3.721104],[-9.611147,-6.839067,-6.255955],[-1.177545,-1.272919,-7.021201],[-7.767500,-7.155802,-0.068546],[6.750488,-5.211629,-0.111630]]], dtype = "float64")#candidate|2955|(2, 9, 3)|const|float64
bop_2956 = relay.mod(const_2954.astype('float64'), relay.reshape(const_2955.astype('float64'), relay.shape_of(const_2954))) # shape=(2, 9, 3)
output = bop_2956
output2 = bop_2956
func_2987 = relay.Function([], output)
mod['func_2987'] = func_2987
mod = relay.transform.InferType()(mod)
output = func_2987()
func_2988 = relay.Function([], output)
mutated_mod['func_2988'] = func_2988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1842_call = mod.get_global_var('func_1842')
func_1844_call = mutated_mod.get_global_var('func_1844')
call_3012 = relay.TupleGetItem(func_1842_call(), 0)
call_3013 = relay.TupleGetItem(func_1844_call(), 0)
output = call_3012
output2 = call_3013
func_3018 = relay.Function([], output)
mod['func_3018'] = func_3018
mod = relay.transform.InferType()(mod)
output = func_3018()
func_3019 = relay.Function([], output)
mutated_mod['func_3019'] = func_3019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1110_call = mod.get_global_var('func_1110')
func_1112_call = mutated_mod.get_global_var('func_1112')
call_3058 = relay.TupleGetItem(func_1110_call(), 1)
call_3059 = relay.TupleGetItem(func_1112_call(), 1)
uop_3089 = relay.acos(call_3058.astype('float32')) # shape=(7, 15, 1)
uop_3091 = relay.acos(call_3059.astype('float32')) # shape=(7, 15, 1)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
var_3096 = relay.var("var_3096", dtype = "int8", shape = (1, 900))#candidate|3096|(1, 900)|var|int8
call_3095 = relay.TupleGetItem(func_2406_call(relay.reshape(var_3096.astype('int8'), [900,])), 0)
call_3097 = relay.TupleGetItem(func_2408_call(relay.reshape(var_3096.astype('int8'), [900,])), 0)
bop_3105 = relay.power(var_3096.astype('float32'), call_3058.astype('float32')) # shape=(7, 15, 900)
bop_3108 = relay.power(var_3096.astype('float32'), call_3059.astype('float32')) # shape=(7, 15, 900)
bop_3111 = relay.multiply(uop_3089.astype('uint32'), relay.reshape(call_3058.astype('uint32'), relay.shape_of(uop_3089))) # shape=(7, 15, 1)
bop_3114 = relay.multiply(uop_3091.astype('uint32'), relay.reshape(call_3059.astype('uint32'), relay.shape_of(uop_3091))) # shape=(7, 15, 1)
bop_3119 = relay.bitwise_and(bop_3105.astype('int32'), call_3058.astype('int32')) # shape=(7, 15, 900)
bop_3122 = relay.bitwise_and(bop_3108.astype('int32'), call_3059.astype('int32')) # shape=(7, 15, 900)
bop_3127 = relay.logical_xor(uop_3089.astype('int16'), bop_3105.astype('int16')) # shape=(7, 15, 900)
bop_3130 = relay.logical_xor(uop_3091.astype('int16'), bop_3108.astype('int16')) # shape=(7, 15, 900)
func_3018_call = mod.get_global_var('func_3018')
func_3019_call = mutated_mod.get_global_var('func_3019')
call_3131 = func_3018_call()
call_3132 = func_3018_call()
output = relay.Tuple([call_3095,bop_3111,bop_3119,bop_3127,call_3131,])
output2 = relay.Tuple([call_3097,bop_3114,bop_3122,bop_3130,call_3132,])
func_3137 = relay.Function([var_3096,], output)
mod['func_3137'] = func_3137
mod = relay.transform.InferType()(mod)
var_3138 = relay.var("var_3138", dtype = "int8", shape = (1, 900))#candidate|3138|(1, 900)|var|int8
output = func_3137(var_3138)
func_3139 = relay.Function([var_3138], output)
mutated_mod['func_3139'] = func_3139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_3144 = func_1015_call()
call_3145 = func_1015_call()
func_678_call = mod.get_global_var('func_678')
func_679_call = mutated_mod.get_global_var('func_679')
call_3150 = func_678_call()
call_3151 = func_678_call()
func_2836_call = mod.get_global_var('func_2836')
func_2840_call = mutated_mod.get_global_var('func_2840')
const_3167 = relay.const([8,6,-1,-5,4,-6,9,6,1,-9,-10,-1,-9,-1,-8,2,2,6,-5,-10,4,-9,-4,-10,-9,-7,9,7,-9,-8,9,-2,10,-4,-6,1,-2,3,-5,2,4,-4,7,3,-10,-2,-1,-1,10,-5,10,8,-8,10,8,9,1,-6,-7,-2,-10,-7,9,-3,3,-7,5,7,-10,9,6,1,3,6,6,6,-2,-8,-9,2,-8,7,6,-7,8,6,5,-3,-7,-8,-7,-1,-7,4,10,10,-4,-1,10,9,-5,-5,-4,-9,-7,8,-1,-7,-7,-6,4,5,4,10,-6,-3,-8,1,7,5,-9,8,-1,8,-5,-5,2,-8,-7,-2,9,-4,-4,-1,7,4,8,-7,8,-6,-2,1,4,2,-10,-2,2,8,-3,4,4,7,10,10,9,-1,9,-9,-3,-4,-7,-2,4,-2,8,8,-6,1,-1,3,6,-3,6,-10,2,2,10,-8,-5,-3,8,4,-10,-7,-7,-1,4,2,7,-1,-5,10,-8,-2,-9,-5,-8,-9,5,9,8,-8,5,6,-1,-3,-9,-2,9,9,2,-3,4,-9,9,2,-10,-4,10,9,7,6,2,3,5,-9,8,7,7,-1,-6,8,5,2,-1,7,-10,-6,-4,-6,-2,5,-1,10,-10,4,5,-3,3,-6,-6,-2,7,-1,-8,-9,1,10,8,-10,2,6,6,-10,5,-3,10,-7,5,7,4,6,9,7,-6,6,1,-7,-3,5,-6,1,6,-4,-6,6,6,5,-6,5,-1,3,-4,10,9,7,6,1,8,4,-6,-3,-2,10,-5,1,-5,-10,7,6,7,-3,-3,-8,-2,4,3,-2,8,-3,6,-8,10,-10,10,-5,1,-2,2,3,2,-2,5,-10,-4,7,-10,-1,-5,-9,6,3,-10,2,-5,-4,2,-2,9,-1,6,5,5,8,8,6,-1,-3,-4,-3,-10,5,-4,-1,10,8,-2,-4,8,8,1,-9,-4,3,7,-8,6,9,2,-3,-3,-8,3,-1,-6,-6,-6,-9,-7,-10,-10,-1,4,6,-1,-8,-1,7,-10,2,1,5,3,10,6,-4,2,5,-7,-2,10,-1,6,-5,-10,4,-7,1,-3,-9,4,-7,1,10,3,-4,-10,5,5,-4,-9,8,-7,5,1,1,9,10,2,-6,2,9,7,9,8,-8,-2,-2,-5,-9,10,10,9,-9,-9,-5,7,4,2,7,-9,-6,3,-1,4,5,-1,-3,-6,-1,-7,8,2,9,9,3,-1,10,6,2,-1,-4,-3,-3,1,-6,8,-4,7,-6,7,4,-8,-4,6,-6,5,9,1,7,-4,2,-8,-4,-10,-1,10,7,-10,6,-8,-2,4,-1,3,-7,-10,9,-5,-2,5,-4,-1,-7,-3,-8,7,2,-3,-6,-10,1,4,-9,-7,4,6,-9,8,-9,-8,1,-9,7,-5,-6,10,6,-1,2,6,10,-5,-9,6,5,-7,9,1,-7,3,-1,5,6,10,4,6,-10,-6,8,-8,-5,-1,-10,2,-9,1,7,-7,1,-1,-5,-10,1,-3,7,-2,-6,-5,-7,4,-4,-4,-10,-4,-10,6,3,10,4,-3,-7,-1,9,-9,-5,-2,5,-1,-7,-6,1,2,-7,-10,-6,-10,-9,5,-7,6,-5,-2,-4,-5,-8,-10,2,5,-4,10,9,4,1,7,4,-1,-2,1,-5,-9,-7,4,-10,-9,-3,6,-1,9,10,9,1,-2,4,-9,10,-2,6,8,-4,-10,-8,-10,-5,-8,-6,8,10,10,-3,-2,8,10,1,-10,5,-3,-6,-9,-9,5,-7,-3,-5,8,2,1,-6,-2,10,-2,-1,7,6,-8,4,-2,-10,-7,-8,5,7,-9,-8,9,-4,3,8,5,-8,10,-10,-5,9,-5,9,6,5,-8,-8,-9,10,10,-3,-3,-9,5,7,-10,-1,3,5,5,-7,-1,4,1,-3,3,7,-7,8,6,1,10,-10,-4,-4,-3,6,10,-5,3,2,-5,1,-5,-3,2,6,-8,7,-9,2,4,5,7,4,9,-5,5,8,5,-1,-7,-9,1,-8,-8,2,10,5,9,-7,-7,5,-8,-10,-6,10,-5,-10,-6,7,-3,-6,-6,10,2,6,-2,1,-5,5,-1,-5,-5,-7,5,4,2,-1,-3,-6,10,6,4,-2,-8,8,-1,10,-8,-8,8,1,4,-2,4,-3,1,-6,7,-2,4,-6,5,-4,10,7,6,2,1,8,-2,-2,10,-6,6,2,1,9,-2,10,5,-2,5,-2,7,-4,8,-10,5,-5,-5,3,5,-2,4,-8,7,-1,-5,-1,-2,-9,-2,-1,4,-10,-3,5,-6,4,6,1,4,-8,-7,-1,-7,-9,9,7,-4,-4,-9,-4,5,5,1,-7,-7,4,-7,3,5,-2,-10,8,4,-4,1,6,-7,7,6,-3,-10,-9,9,-8,3,-9,-9,-10,8,-7,-3,5,5,-6,-6,6,-5,3,-8,-10,-1,8,7,4,-2,-4,-6,-5,-1,-2,9,4,-4,7,8,-6,6,10,2,9,-4,10,-4,-1,-5,3,-2,7,-4,1,-2,10,1,-1,5,-8,3,-1,3,3,6,2,-4,5,3,-9,-10,-5,10,-3,-6,-4,-9,7,8,9,-7,-1,10,-9,9,-10,-9,-10,-10,4,6,-4,-4,6,-2,-5,8,2,-1,10,8,-10,4,-6,5,-10,-1,-5,-9,6,-7,-2,8,-2,-4,-8,4,-9,-8,-5,-8,-3,1,-3,-10,-2,1,-2,8,7,-10,-2,3,-5,10,-3,6,7,-3,-8,9,-1,-3,-7,-9,-1,-9,3,6,-2,-7,7,2,-1,-2,9,-8,-2,-3,10,-5,-9,3,6,-10,-8,-5,2,-8,-4,1,-2,2,-8,4,7,8,-6,7,-4,2,6,8,-5,-9,7,-2,9,-4,1,4,9,-3,6,-7,-9,-2,-8,-2,-5,2,3,2,10,-8,3,-6,-5,-7,2,-1,3,-5,4,-4,10,-2,1,-4,9,9,-5,4,7,5,5,10,9,-1,-5,-3,-2,-10,10,-4,-10,-9,-2,-7,4,6,-7,-7,4,-1,-2,5,-1,9,-1,-10,-7,-5,4,6,5,-7,-10,9,4,-10,6,10,-10,-1,-1,-1,-2,7,-10,5,-7,-6,-1,-9,-6,-1,6,-10,-2,9,-3,-2,-9,-4,4,-2,6,-5,6,-9,-7,-5,-4,1,-7,1,-3,9,-4,10,-4,6,-4,-6,9,3,8,10,4,-9,-6,-4,-5,-2,8,6,6,-2,7,3,3,-3,-3,-2,6,9,-4,-2,6,8,6,5,-8,-2,-5,2,-10,-9,-9,1,4,9,5,-9,-5,-6,-10,3,-10,-4,2,2,-10,7,4,7,10,-8,-7,-7,-1,-3,5,-3,-1,-9,3,-4,-2,4,-1,-4,7,7,6,-6,8,-1,5,10,-1,8,-10,-6,-5,6,1,8,-1,-4,8,7,-9,-1,-2,-2,-9,6,-7,2,5,8,10,-6,1,-2,-9,-9,9,7,-2,-6,-9,2,7,8,4,7,-3,8,4,7,1,4,-5,-3,9,-7,2,-6,3,-10,-1,-2,-2,2,-10,-1,-2,-1,5,-1,-3,-5,-10,-3,-5,2,2,4,-6,-1,-3,9,5,-2,4,-7,4,2,-2,-8,8,5,-8,3,5,-2,6,4,1,-4,-1,-2,2,10,-8,3,10,5,6,4,2,10,7,-9,-9,-5,-3,-5,2,-1,6,8,3,-6,1,-10,7,-1,5,-5,5,7,1,-7,9,-5,3,3,-7,4,-10,-3,6,1,5,10,-8,-10,-10,3,-4,-6,-4,-10,9,-10,-8,-6,-8,10,5,-5,-6,3,1,-5,6,1,-2,2,-7,-10,7,1,-5,1,10,6,-3,10,-6,-9,8,-2,-3,2,9,4,10,-5,8,-6,4,-4,2,8,-1,-8,-9,9,-7,1,-3,-5,-10,-9,-6,9,-8,4,-7,7,1,10,8,-3,2,-4,-7,-9,7,9,4,3,1,3,-2,-7,-8,7,6,-4,2,-3,-4,9,-2,-7,6,-10,9,-4,-6,8,-8,1,-2,4,10,4,2,9,2,2,-10,-3,-8,2,8,9,2,1,4,8,5,-1,-5,-2,-8,3,9,-7,-2,2,-8,7,-10,3,-4,-7,5,7,-8,-5,3,4,-7,-8,1,-9,10,8,4,3,4,-8,-8,9,4,-4,-3,1,-3,-8,-1,-3,5,-1,3,-1,-4,8,-6,9,10,-8,-6,-4,8,-1,-1,9,6,-8,-4,7,-8,1,1,-5,-7,-5,-2,10,-1,8,-5,-9,-7,-9,-6,10,-3,-9,2,5,-6,10,9,7,-1,1,2,-7,7,-1,-6,6,-3,-6,-8,6,-3,-10,-8,-2,4,7,3,6,-3,2,1,1,-2,10,-7,-4,5,-1,-2,2,-8,1,-4,-1,7,8,-1,3,3,-3,-10,-1,2,-7,-6,-8,9,-6,-10,2,10,7,-7,7,4,10,-9,-8,-4,-5,4,-5,-5,-6,9,4,7,3,2,6,3,7,-9,-3,1,-5,1,8,2,3,-3,1,10,4,5,5,5,10,-8,9,10,4,4,9,7,5,1,-10,9,1,5,10,10,6,-2,9,8,5,-7,-6,-8,-4,7,2,-1,10,10,8,1,-2,-10,6,6,8,8,8,4,-7,-10,-7,-3,-7,-8,-5,-10,1,-7,5,-8,9,-6,-4,-10,3,1,3,6,6,-6,2,-7,-5,8,10,-5,-4,5,-3,-10,-7,6,-2,9,-8,-7,2,-3,-10,10,-9,-8,-8,-2,2,-7,10,10,-8,9,5,-6,2,5,-2,-4,10,5,-7,-8,8,1,-1,-9,-9,4,-6,4,-2,10,5,-7,5,4,-9,-4,-10,-5,3,7,-2,-9,-5,-8,1,-3,3,-3,3,4,-10,1,1,-10,-9,10,1,-2,4,3,10,-4,-5,-3,4,2,-4,-5,-6,3,3,-9,-7,-9,2,6,8,-7,9,-1,7,-7,6,-8,-7,8,-8,-2,-9,-4,3,-5,4,-3,-1,-3,10,9,-4,-8,10,10,-2,-1,-5,4,-8,8,8,-2,8,7,-7,-3,3,-1,7,1,4,-4,8,7,-4,8,6,3,7,-3,-6,7,-10,-10,-10,10,-4,4,-10,-8,6,10,-7,-8,-3,-1,9,-8,-8,8,1,3,10,-7,-8,9,-2,8,2,-6,-8,3,6,-8,2,-2,4,8,3,-6,-10,-7,-2,4,2,8,-4,7,6,4,-1,-1,-2,-9,-4,-7,10,1,-10,7,-2,10,-9,5,2,3,6,6,-3,-4,-10,5,7,-5,8,9,-8,-5,-5,2,2,3,-7,7,-6,9,3,7,10,9,3,-8,-4,-7,5,-10,-5,8,-2,4,-7,-5,8,2,-5,6,8,8,-6,3,-6,-10,-6,3,-3,-7,1,-3,-5,7,-8,5,-6,8,-9,5,5,-6,-4,-2,-7,9,10,-7,1,-2,-6,4,1,-3,-4,8,4,4,-5,6,3,2,-1,10,-4,8,-1,-1,6,-5,-2,2,8,-3,10,5,-9,9,-5,-10,1,-10,-4,-7,4,-1,-8,10,8,-7,7,4,-8,-3,-1,-3,-5,-9,3,-9,9,-1,2,-10,-9,1,-8,9,7,10,-9,4,-5,2,8,-5,1,3,9,8,-4,-3,3,10,-8,-1,5,-2,8,-8,-7,-3,-9,6,4,8,-10,-10,-5,-4,-3,9,-2,-8,-6,7,1,4,8,10,1,-2,10,-7,-4,-7,7,5,-8,-8,-1,-8,6,-4,1,8,3,4,-4,8,3,7,3,7,-4,8,1,8,9,2,6,-1,-2,2,-7,5,10,-9,-3,6,3,-1,-1,4,8,9,7,-5,-6,-6,9,-4,5,-2,10,-4,-4,-9,-3,-5,6,7,4,4,-8,5,-4,-8,2,7,-10,3,5,10,-5,-3,9,-6,-1,-6,-3,-8,-10,7,-8,4,-3,-3,10,-10,-8,-6,2,-3,2,-4,10,3,-10,-4,5,6,4,8,-3,-9,-1,10,-6,-6,10,-7,-4,2,1,2,-1,-3,10,-1,2,-3,-4,6,-4,2,4,4,-8,-2,2,6,-4,10,-2,6,10,7,-10,6,7,10,5,-9,-10,-5,-7,-6,8,7,-9,-4,-2,-3,-5,-8,6,4,-2,6,4,-4,2,1,8,-2,3,-5,8,-9,8,-7,-7,-8,2,3,-5,6,-1,-9,-9,5,6,6,10,9,5,2,5,-1,4,-6,2,-8,10,-1,8,-10,-6,10,-10,-3,3,6,-5,-8,10,-10,5,-5,-3,6,2,6,10,5,-3,6,-6,-7,-9,10,6,-4,-5,-7,-3,2,7,-5,-1,9,-1,-3,5,-7,-2,4,6,10,6,4,10,-7,1,4,-2,-10,-7,-9,-3,-9,-3,5,-10,3,-2,-7,10,-9,-8,6,7,-5,9,9,8,6,-10,1,6,7,-10,2,10,4,8,8,-8,-2,-6,-10,8,8,-9,-1,4,4,-4,-5,-10,2,10,3,-6,-6,5,-7,-4,-4,-3,-7,-3,-2,-7,-3,7,-5,9,7,-3,6,-9,-5,-9,5,2,-10,2,3,-8,-6,-2,-5,9,4,5,9,4,-8,-3,-4,4,9,5,-5,8,1,-2,-9,-8,-2,5,-10,7,2,10,4,-2,-8,-7,-10,-6,-3,5,1,8,-8,-9,2,6,-6,3,-8,7,10,1,-8,-10,7,-4,-1,-4,-5,-9,8,4,2,8,-2,8,-8,1,9,-7,-1,7,-5,-2,5,-1,9,-1,-3,-10,1,-7,10,4,-3,6,-2,-5,5,9,-1,4,-8,-8,3,5,10,2,-4,-7,-5,-9,5,8,-1,1,9,-1,-10,7,-1,-5,8,10,4,-7,2,10,9,-9,-6,6,4,2,8,-7,-4,9,2,4,-7,-8,6,-8,7,9,6,1,-3,-5,-4,2,-7,-2,2,-6,6,10,4,-8,3,-6,-3,2,10,6,2,-4,9,-7,-3,-10,8,2,7,-5,-7,1,8,5,3,-3,-9,5,6,-9,-6,7,-10,-8,-9,7,-5,-8,-4,-2,6,3,4,-5,9,-9,-4,2,5,1,4,2,6,2,-4,-6,-10,6,-4,-6,7,-1,2,-5,5,1,-3,9,-2,7,5,-6,2,-3,-5,3,-4,2,-10,-3,4,4,-6,7,6,-5,9,8,-3,8,-9,1,7,-9,4,-10,7,-6,-9,-2,6,5,-9,7,-3,-2,-7,-6,-8,-9,-9,1,-5,1,-9,-8,-10,-2,-6,-3,-3,-1,-7,5,4,-10,-5,8,-7,3,-4,4,-3,-5,5,-10,-2,-1,8,6,1,4,6,-5,5,-10,-8,2,-3,4,2,10,-3,-3,-6,6,5,-3,-3,4,6,-6,-10,-8,5,3,-6,-3,4,3,-7,9,-8,-2,1,-1,-4,1,-5,-9,3,-8,-6,7,9,2,-6,7,-3,6,-9,-9,4,-8,-1,7,-10,-2,-8,-6,8,2,-9,9,-7,6,-10,8,-6,-2,5,10,6,2,8,10,8,-9,10,8,3,-5,10,-8,2,-3,9,2,3,1,4,9,-5,8,8,-5,2,3,-5,-8,1,6,5,7,-4,1,-2,-1,-9,-2,-4,6,-7,8,10,-3,-7,10,8,8,-6,1,9,4,-8,-5,-3,8,1,-6,-10,-3,7,-9,-1,-7,7,-2,10,4,-2,2,-1,-7,-6,5,-9,5,2,-9,10,-7,-3,-3,4,-3,-8,2,-5,6,-10,-1,1,-7,9,-5,1,8,-4,-9,10,-7,-6,2,7,-5,10,8,-2,-4,10,-2,5,6,-2,-10,-8,-5,-3,8,-6,9,-10,7,3,-5,-5,5,-6,1,-8,2,-5,10,3,-2,-2,-5,9,4,-3,6,-3,-8,-3,-9,-10,-9,-10,-5,-7,-4,-7,1,10,7,-4,1,-3,8,-10,9,10,4,-6,-4,5,4,-6,-7,2,-10,-8,-4,2,9,1,-9,-5,-2,2,-8,4,1,8,-6,4,5,-5,-3,10,-8,-9,3,-9,-6,1,-10,-5,6,-8,4,-6,-2,-7,-9,-8,-10,-3,-2,6,-5,-2,-5,-5,2,3,5,-4,-2,3,-10,8,7,-10,6,-7,-6,-8,-7,2,-10,5,4,-4,4,8,8,3,9,-6,-3,10,3,-2,2,-2,-1,-8,10,-1,-1,8,7,7,-9,3,-6,-3,10,1,-1,6,2,9,8,-4,-9,10,-6,-3,10,6,8,6,7,2,2,2,-4,4,10,-4,-2,6,9,-2,-5,6,-10,-1,-2,6,3,-6,8,-2,9,7,8,1,1,8,-4,9,-9,-10], dtype = "int8")#candidate|3167|(3150,)|const|int8
call_3166 = relay.TupleGetItem(func_2836_call(relay.reshape(const_3167.astype('int8'), [15, 15, 14]), relay.reshape(const_3167.astype('int8'), [15, 15, 14]), ), 0)
call_3168 = relay.TupleGetItem(func_2840_call(relay.reshape(const_3167.astype('int8'), [15, 15, 14]), relay.reshape(const_3167.astype('int8'), [15, 15, 14]), ), 0)
var_3174 = relay.var("var_3174", dtype = "bool", shape = (15, 15, 14))#candidate|3174|(15, 15, 14)|var|bool
bop_3175 = relay.divide(call_3166.astype('float64'), relay.reshape(var_3174.astype('float64'), relay.shape_of(call_3166))) # shape=(15, 15, 14)
bop_3178 = relay.divide(call_3168.astype('float64'), relay.reshape(var_3174.astype('float64'), relay.shape_of(call_3168))) # shape=(15, 15, 14)
output = relay.Tuple([call_3144,call_3150,const_3167,bop_3175,])
output2 = relay.Tuple([call_3145,call_3151,const_3167,bop_3178,])
func_3190 = relay.Function([var_3174,], output)
mod['func_3190'] = func_3190
mod = relay.transform.InferType()(mod)
var_3191 = relay.var("var_3191", dtype = "bool", shape = (15, 15, 14))#candidate|3191|(15, 15, 14)|var|bool
output = func_3190(var_3191)
func_3192 = relay.Function([var_3191], output)
mutated_mod['func_3192'] = func_3192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1110_call = mod.get_global_var('func_1110')
func_1112_call = mutated_mod.get_global_var('func_1112')
call_3295 = relay.TupleGetItem(func_1110_call(), 0)
call_3296 = relay.TupleGetItem(func_1112_call(), 0)
func_1527_call = mod.get_global_var('func_1527')
func_1530_call = mutated_mod.get_global_var('func_1530')
const_3300 = relay.const([6,-5,3,-1,-10,-5,-6,-5,-7,4,7,-4,-6,-5,6,6,-10,-2,-1,-9,-8,3,9,10,3,5,8,4,-2,2,9,-9,-9,1,-2,10,7,3,-5,2,-8,8,8,4,1,9,4,-8,-9,-2,1,10,-9,-6,7,-10,4,-3,-10,-4,2,10,3,8,8,2,4,-9,-4,-7,2,-8,-7,-1,-9,-5,-10,7,-2,-5,7,-2,-7,5,-6,4,2,-4,-6,-4,-10,8,-6,5,-1,10,8,-8,3,-8,-6,6,-6,-4,5,-9,-1,-7,3,-6,-4,10,-10,-9,-2,3,1,3,-10,-2,-9,10,-8,-6,8,-5,8,-4,-6,1,-10,-5,4,10,8,-6,3,-6,2,-3,-2,5,-8,8,4,3,6,6,-9,-3,-10,-4,7,-5,-10,1,1,-1,9,-10,-1,-8,2,-6,-2,-5,-9,7,-9,-7,3,10,-6,-10,2,-7,-4,7,-10,-6,-3,-7,2,-8,-6,-9,-3,-2,9,3,5,-4,6,6,6,2,-3,-10,3,-7,3,10,4,-4,-6,-6,-8,10,2,1,8,-7,-2,-7,7,6,9,-7,-9,-5,9,-6,10,10,-3,-1,-2,-3,7,9,-3,5,2,4,4,-4,1,-9,-7,-4,-10,1,-5,-8,4,8,4,-1,7,6,5,4,4,-8,2,3,-10,6,9,-10,3,2,1,-4,9,10,3,-1,-7,8,-2,1,-5,7,-3,9,-5,3,-6,-6,10,10,-2,-10,1,-8], dtype = "uint16")#candidate|3300|(286,)|const|uint16
call_3299 = relay.TupleGetItem(func_1527_call(relay.reshape(const_3300.astype('uint16'), [2, 13, 11]), relay.reshape(const_3300.astype('uint16'), [2, 13, 11]), ), 0)
call_3301 = relay.TupleGetItem(func_1530_call(relay.reshape(const_3300.astype('uint16'), [2, 13, 11]), relay.reshape(const_3300.astype('uint16'), [2, 13, 11]), ), 0)
func_2436_call = mod.get_global_var('func_2436')
func_2438_call = mutated_mod.get_global_var('func_2438')
var_3320 = relay.var("var_3320", dtype = "float64", shape = (36, 14))#candidate|3320|(36, 14)|var|float64
call_3319 = relay.TupleGetItem(func_2436_call(relay.reshape(var_3320.astype('float64'), [6, 84])), 1)
call_3321 = relay.TupleGetItem(func_2438_call(relay.reshape(var_3320.astype('float64'), [6, 84])), 1)
uop_3323 = relay.cosh(var_3320.astype('float64')) # shape=(36, 14)
output = relay.Tuple([call_3295,call_3299,const_3300,call_3319,uop_3323,])
output2 = relay.Tuple([call_3296,call_3301,const_3300,call_3321,uop_3323,])
func_3325 = relay.Function([var_3320,], output)
mod['func_3325'] = func_3325
mod = relay.transform.InferType()(mod)
mutated_mod['func_3325'] = func_3325
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3326 = relay.var("var_3326", dtype = "float64", shape = (36, 14))#candidate|3326|(36, 14)|var|float64
func_3325_call = mutated_mod.get_global_var('func_3325')
call_3327 = func_3325_call(var_3326)
output = call_3327
func_3328 = relay.Function([var_3326], output)
mutated_mod['func_3328'] = func_3328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2175_call = mod.get_global_var('func_2175')
func_2176_call = mutated_mod.get_global_var('func_2176')
call_3337 = relay.TupleGetItem(func_2175_call(), 0)
call_3338 = relay.TupleGetItem(func_2176_call(), 0)
output = relay.Tuple([call_3337,])
output2 = relay.Tuple([call_3338,])
func_3340 = relay.Function([], output)
mod['func_3340'] = func_3340
mod = relay.transform.InferType()(mod)
mutated_mod['func_3340'] = func_3340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3340_call = mutated_mod.get_global_var('func_3340')
call_3341 = func_3340_call()
output = call_3341
func_3342 = relay.Function([], output)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2045_call = mod.get_global_var('func_2045')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_3359 = relay.TupleGetItem(func_2045_call(), 3)
call_3360 = relay.TupleGetItem(func_2047_call(), 3)
func_2436_call = mod.get_global_var('func_2436')
func_2438_call = mutated_mod.get_global_var('func_2438')
const_3373 = relay.const([-3.444185,8.242381,3.033076,-1.421444,4.301467,9.353982,-2.555956,5.552030,5.696563,3.010421,-0.662424,-7.247560,-5.762606,-1.573704,-4.457700,2.368565,1.253969,0.523947,-4.322527,3.363560,7.247345,-3.382853,-0.803943,2.055348,6.741681,0.631255,5.868313,3.737254,2.546738,-6.249466,1.700670,-2.757746,-0.207657,-5.755912,4.102139,-1.773768,-5.654072,-5.644675,6.271390,2.972398,0.716379,-4.343774,-3.461222,-1.709400,7.440444,-1.065356,6.992555,-1.657168,-0.459264,-3.330597,-1.667043,-5.003111,6.184677,2.889270,4.986203,3.485598,-8.433818,8.589251,-3.916692,-5.926310,-4.153299,-7.938620,2.778934,8.403303,4.771123,5.768870,8.834850,9.945087,2.751272,6.635838,4.000115,2.383646,-6.977218,-9.174932,-1.703126,-7.585221,5.534220,-3.729411,2.299880,-8.468148,5.809204,5.408452,-1.390627,4.819377,4.426428,-1.186738,-4.216882,-7.241315,-2.185621,8.213854,7.320376,-6.416649,-9.476369,0.678756,-7.614985,0.636989,-5.633014,-1.464758,0.046121,-4.777575,-7.281640,3.666490,-6.962626,9.435293,-6.316102,4.184444,8.009699,6.592063,9.567423,7.694458,-4.318670,4.678815,2.616674,0.446583,-9.723162,-8.133329,-5.779413,7.067678,5.873111,-4.382051,9.333915,-5.124780,3.088955,-1.714598,-4.299898,-7.591168,-4.577540,8.782729,-9.995841,-2.970689,-4.124673,7.262069,-4.087590,1.741030,-6.657898,-3.684421,-1.715195,-2.139869,-4.659973,-7.921824,-5.145279,6.971110,-3.563847,7.039006,-8.960754,0.164825,-0.673660,0.950996,7.698190,-5.103253,-6.513621,1.421793,6.383260,-4.170124,7.281166,0.866853,-8.222955,-8.898888,8.779960,5.915082,-6.888420,5.325873,8.803256,4.019008,9.624292,-4.202843,-4.635927,-1.907635,1.569215,7.863486,2.683204,2.917514,-2.992855,0.189144,3.372261,0.457015,4.169127,-3.228599,1.681428,-7.563118,9.860348,8.258969,-6.160838,-7.689325,-4.319851,-5.949372,-1.649949,9.788435,-6.728362,-6.821985,5.833270,1.338070,-9.318349,-2.723453,5.131049,3.339295,1.728578,2.895684,-5.260920,-9.513603,7.422976,0.906698,-4.086972,-9.648641,6.507734,-1.948663,-2.879197,1.090010,9.405662,9.054127,-3.401259,3.151013,0.716763,-5.019131,-3.095318,-1.492909,7.949872,6.879050,9.855696,-1.531643,0.169241,5.573249,-9.312400,-0.168924,-8.711945,1.244399,-6.973373,7.647123,2.829569,-4.441162,-6.132178,2.964943,-9.864848,5.957986,9.710371,-0.231076,-5.890108,-2.887491,-7.300867,-3.256743,-9.678415,-7.786741,-6.454560,-1.419391,7.625608,-7.930267,-9.001812,1.516687,-8.718281,-5.310510,8.401768,-4.962212,-8.831962,-5.584552,-8.399378,-8.726772,-1.648932,6.879164,-2.988869,-5.589386,-9.851374,2.890279,9.693238,9.900087,3.056572,0.695761,-9.934411,-0.362596,-9.574783,-2.954360,9.226615,-6.400739,5.509468,-5.692028,3.773423,6.511813,5.574005,-6.882598,2.864406,3.051820,8.318040,4.938937,-2.732035,1.501114,5.816144,2.817416,-1.108553,-0.284656,-4.412830,0.714010,-4.247053,4.639693,8.263875,-4.383092,-8.435186,6.148117,-4.374292,0.440071,-0.153953,3.242757,-9.685960,-1.940445,-9.417689,-1.944425,4.632307,2.695082,-4.907448,-5.261388,-8.588754,7.521397,-3.315897,5.540020,1.421331,5.166988,0.533272,2.075657,-2.712138,-6.992249,7.302840,9.202023,-5.625660,-8.505281,3.089950,-9.147451,7.489952,-3.181836,-4.347385,-0.933587,1.325028,5.343149,-5.129158,-1.978859,-6.699518,-2.242191,-6.775699,-3.543299,-8.569371,8.382500,1.070405,5.466679,6.273801,-8.825045,6.757616,-8.117802,1.751522,7.503627,-6.893121,-1.516389,-0.776808,-9.199666,-1.710747,6.856754,5.548617,-5.748802,-1.653617,5.172606,-7.100052,7.549260,-6.423782,-6.881103,3.988954,-8.821170,9.303973,-4.073505,1.924131,-8.681554,-3.547758,-7.966349,5.704003,-7.895131,-2.389700,7.089126,-4.600926,2.640715,-4.823267,-1.275079,9.761463,-5.136257,9.562451,8.392329,8.395439,-2.962134,2.615414,-2.370677,4.476883,8.444586,-4.930791,-8.826430,0.989939,-7.138618,2.091056,-0.153509,3.170043,-9.153594,4.650065,2.754184,1.951262,-2.906423,-9.045403,1.733136,-5.260085,3.017877,-2.802410,7.033804,3.440820,2.176778,-1.796174,-3.199914,-2.645464,-3.958531,-2.394207,8.093251,9.739734,-2.226556,-4.923504,7.711147,-1.412879,6.383953,6.708070,0.233021,-5.942657,1.705416,-7.009216,-1.881752,-3.109085,-3.618415,-5.287225,8.001175,-7.551961,0.152897,1.196892,3.851158,-8.692772,-3.342233,2.267767,-9.096345,6.095239,-6.841004,8.302904,-5.538970,1.957569,-4.321376,-4.779969,9.293304,-8.131101,6.781975,1.245149,5.001744,-2.945914,8.338635,5.676747,7.388687,-1.877565,-6.487627,2.311495,8.427485,-8.531491,-4.193065,1.703509,6.763596,1.194163,-6.661901,3.214486,-9.823720,2.254337,7.796390,7.231938,7.546275,-1.950072,-8.624590,2.461447,-9.256949,8.579563,-8.898973,-6.961667,-3.124029,5.496948,-1.151223,2.829864,-2.715907,6.571734,4.572610,-3.895079,-3.770138,6.002144,-7.239186,-0.071144,-0.381908,-6.286690,6.068848,-2.718834,-3.898913,-1.033814,-4.339167,5.057072,-9.309200,-8.604586,1.425279,1.921316,1.152698,-7.206058,1.655276,-5.889127,5.871960], dtype = "float64")#candidate|3373|(504,)|const|float64
call_3372 = relay.TupleGetItem(func_2436_call(relay.reshape(const_3373.astype('float64'), [6, 84])), 2)
call_3374 = relay.TupleGetItem(func_2438_call(relay.reshape(const_3373.astype('float64'), [6, 84])), 2)
output = relay.Tuple([call_3359,call_3372,const_3373,])
output2 = relay.Tuple([call_3360,call_3374,const_3373,])
func_3376 = relay.Function([], output)
mod['func_3376'] = func_3376
mod = relay.transform.InferType()(mod)
mutated_mod['func_3376'] = func_3376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3376_call = mutated_mod.get_global_var('func_3376')
call_3377 = func_3376_call()
output = call_3377
func_3378 = relay.Function([], output)
mutated_mod['func_3378'] = func_3378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3018_call = mod.get_global_var('func_3018')
func_3019_call = mutated_mod.get_global_var('func_3019')
call_3418 = func_3018_call()
call_3419 = func_3018_call()
func_3018_call = mod.get_global_var('func_3018')
func_3019_call = mutated_mod.get_global_var('func_3019')
call_3443 = func_3018_call()
call_3444 = func_3018_call()
func_3190_call = mod.get_global_var('func_3190')
func_3192_call = mutated_mod.get_global_var('func_3192')
const_3449 = relay.const([True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,True], dtype = "bool")#candidate|3449|(3150,)|const|bool
call_3448 = relay.TupleGetItem(func_3190_call(relay.reshape(const_3449.astype('bool'), [15, 15, 14])), 2)
call_3450 = relay.TupleGetItem(func_3192_call(relay.reshape(const_3449.astype('bool'), [15, 15, 14])), 2)
output = relay.Tuple([call_3418,call_3443,call_3448,const_3449,])
output2 = relay.Tuple([call_3419,call_3444,call_3450,const_3449,])
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
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_3558 = relay.TupleGetItem(func_3457_call(), 3)
call_3559 = relay.TupleGetItem(func_3459_call(), 3)
const_3572 = relay.const([False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True], dtype = "bool")#candidate|3572|(3150,)|const|bool
bop_3573 = relay.left_shift(call_3558.astype('int8'), relay.reshape(const_3572.astype('int8'), relay.shape_of(call_3558))) # shape=(3150,)
bop_3576 = relay.left_shift(call_3559.astype('int8'), relay.reshape(const_3572.astype('int8'), relay.shape_of(call_3559))) # shape=(3150,)
output = bop_3573
output2 = bop_3576
func_3586 = relay.Function([], output)
mod['func_3586'] = func_3586
mod = relay.transform.InferType()(mod)
output = func_3586()
func_3587 = relay.Function([], output)
mutated_mod['func_3587'] = func_3587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1863_call = mod.get_global_var('func_1863')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_3620 = relay.TupleGetItem(func_1863_call(), 0)
call_3621 = relay.TupleGetItem(func_1865_call(), 0)
output = call_3620
output2 = call_3621
func_3628 = relay.Function([], output)
mod['func_3628'] = func_3628
mod = relay.transform.InferType()(mod)
output = func_3628()
func_3629 = relay.Function([], output)
mutated_mod['func_3629'] = func_3629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2119_call = mod.get_global_var('func_2119')
func_2121_call = mutated_mod.get_global_var('func_2121')
call_3673 = relay.TupleGetItem(func_2119_call(), 0)
call_3674 = relay.TupleGetItem(func_2121_call(), 0)
func_3586_call = mod.get_global_var('func_3586')
func_3587_call = mutated_mod.get_global_var('func_3587')
call_3683 = func_3586_call()
call_3684 = func_3586_call()
bop_3689 = relay.power(call_3683.astype('float64'), call_3673.astype('float64')) # shape=(7, 15, 3150)
bop_3692 = relay.power(call_3684.astype('float64'), call_3674.astype('float64')) # shape=(7, 15, 3150)
output = relay.Tuple([bop_3689,])
output2 = relay.Tuple([bop_3692,])
func_3693 = relay.Function([], output)
mod['func_3693'] = func_3693
mod = relay.transform.InferType()(mod)
output = func_3693()
func_3694 = relay.Function([], output)
mutated_mod['func_3694'] = func_3694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_816_call = mutated_mod.get_global_var('func_816')
call_3790 = relay.TupleGetItem(func_815_call(), 1)
call_3791 = relay.TupleGetItem(func_816_call(), 1)
func_668_call = mod.get_global_var('func_668')
func_670_call = mutated_mod.get_global_var('func_670')
var_3808 = relay.var("var_3808", dtype = "float32", shape = (630,))#candidate|3808|(630,)|var|float32
call_3807 = relay.TupleGetItem(func_668_call(relay.reshape(var_3808.astype('float32'), [7, 15, 6])), 0)
call_3809 = relay.TupleGetItem(func_670_call(relay.reshape(var_3808.astype('float32'), [7, 15, 6])), 0)
bop_3819 = relay.less_equal(var_3808.astype('bool'), call_3790.astype('bool')) # shape=(7, 15, 630)
bop_3822 = relay.less_equal(var_3808.astype('bool'), call_3791.astype('bool')) # shape=(7, 15, 630)
output = relay.Tuple([call_3807,bop_3819,])
output2 = relay.Tuple([call_3809,bop_3822,])
func_3829 = relay.Function([var_3808,], output)
mod['func_3829'] = func_3829
mod = relay.transform.InferType()(mod)
mutated_mod['func_3829'] = func_3829
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3830 = relay.var("var_3830", dtype = "float32", shape = (630,))#candidate|3830|(630,)|var|float32
func_3829_call = mutated_mod.get_global_var('func_3829')
call_3831 = func_3829_call(var_3830)
output = call_3831
func_3832 = relay.Function([var_3830], output)
mutated_mod['func_3832'] = func_3832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2242_call = mod.get_global_var('func_2242')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_3895 = func_2242_call()
call_3896 = func_2242_call()
uop_3897 = relay.sinh(call_3895.astype('float64')) # shape=(7, 15, 1)
uop_3899 = relay.sinh(call_3896.astype('float64')) # shape=(7, 15, 1)
output = relay.Tuple([uop_3897,])
output2 = relay.Tuple([uop_3899,])
func_3905 = relay.Function([], output)
mod['func_3905'] = func_3905
mod = relay.transform.InferType()(mod)
mutated_mod['func_3905'] = func_3905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mutated_mod.get_global_var('func_3905')
call_3906 = func_3905_call()
output = call_3906
func_3907 = relay.Function([], output)
mutated_mod['func_3907'] = func_3907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2068_call = mod.get_global_var('func_2068')
func_2069_call = mutated_mod.get_global_var('func_2069')
call_3923 = relay.TupleGetItem(func_2068_call(), 0)
call_3924 = relay.TupleGetItem(func_2069_call(), 0)
func_2548_call = mod.get_global_var('func_2548')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_3941 = func_2548_call()
call_3942 = func_2548_call()
output = relay.Tuple([call_3923,call_3941,])
output2 = relay.Tuple([call_3924,call_3942,])
func_3944 = relay.Function([], output)
mod['func_3944'] = func_3944
mod = relay.transform.InferType()(mod)
output = func_3944()
func_3945 = relay.Function([], output)
mutated_mod['func_3945'] = func_3945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3376_call = mod.get_global_var('func_3376')
func_3378_call = mutated_mod.get_global_var('func_3378')
call_3954 = relay.TupleGetItem(func_3376_call(), 0)
call_3955 = relay.TupleGetItem(func_3378_call(), 0)
output = call_3954
output2 = call_3955
func_3958 = relay.Function([], output)
mod['func_3958'] = func_3958
mod = relay.transform.InferType()(mod)
mutated_mod['func_3958'] = func_3958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3958_call = mutated_mod.get_global_var('func_3958')
call_3959 = func_3958_call()
output = call_3959
func_3960 = relay.Function([], output)
mutated_mod['func_3960'] = func_3960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_678_call = mod.get_global_var('func_678')
func_679_call = mutated_mod.get_global_var('func_679')
call_3961 = func_678_call()
call_3962 = func_678_call()
output = relay.Tuple([call_3961,])
output2 = relay.Tuple([call_3962,])
func_3963 = relay.Function([], output)
mod['func_3963'] = func_3963
mod = relay.transform.InferType()(mod)
mutated_mod['func_3963'] = func_3963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3963_call = mutated_mod.get_global_var('func_3963')
call_3964 = func_3963_call()
output = call_3964
func_3965 = relay.Function([], output)
mutated_mod['func_3965'] = func_3965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2242_call = mod.get_global_var('func_2242')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_4013 = func_2242_call()
call_4014 = func_2242_call()
uop_4017 = relay.asinh(call_4013.astype('float64')) # shape=(7, 15, 1)
uop_4019 = relay.asinh(call_4014.astype('float64')) # shape=(7, 15, 1)
bop_4020 = relay.equal(uop_4017.astype('bool'), relay.reshape(call_4013.astype('bool'), relay.shape_of(uop_4017))) # shape=(7, 15, 1)
bop_4023 = relay.equal(uop_4019.astype('bool'), relay.reshape(call_4014.astype('bool'), relay.shape_of(uop_4019))) # shape=(7, 15, 1)
func_3829_call = mod.get_global_var('func_3829')
func_3832_call = mutated_mod.get_global_var('func_3832')
const_4028 = relay.const([8.566021,-4.501115,7.351981,-6.918543,4.382829,7.789766,-5.175921,9.536036,5.121659,3.383586,7.640058,0.376365,-0.949189,-1.186006,2.359698,2.501043,9.836316,2.615195,8.360930,-2.480167,-3.230725,3.163658,8.861481,0.483972,1.033931,5.454390,-5.344194,-2.038665,-1.207021,-2.738628,9.870271,5.970503,9.557966,8.681125,-5.768301,1.297843,-6.744122,-6.953780,-5.988135,-6.860412,-6.580337,-5.767310,-4.541723,-2.250026,8.820350,-8.797942,-3.219312,2.603131,1.746663,-7.967392,-5.056321,-4.133655,-1.084956,6.138784,-6.011812,3.452755,5.358830,5.789107,-2.563634,5.811215,-8.031495,2.250954,5.625305,2.176070,2.153193,-0.969244,0.348191,-2.593377,1.083171,-2.604290,7.142818,9.408666,3.180010,-1.478469,-4.728473,-0.089385,-8.973155,2.788148,-8.124012,-3.412071,-2.326353,-4.081576,2.331947,2.422570,-4.202794,-2.739411,5.528053,-3.701801,-4.118280,3.183914,-4.293972,5.175436,3.146326,-8.670952,6.434229,8.385780,-0.111157,-5.983533,4.633122,-1.524247,9.947103,8.843194,-6.184698,-5.695476,5.704614,0.627585,3.183732,-8.954504,1.775606,-0.424701,2.142816,-6.089033,5.057523,6.129604,0.505961,-8.443371,-3.090290,4.998238,-6.229204,4.515165,6.913002,2.397289,9.127885,8.085194,8.965114,-4.677089,-5.879106,-0.861960,9.981972,-6.730517,3.987263,2.358017,-4.603535,8.860111,-1.799267,-4.003068,8.261345,-0.420340,6.407375,-5.543867,-9.204652,5.872176,7.497255,-0.902221,0.418667,6.746836,-8.324576,-3.071443,-5.533330,0.732670,-0.697991,-0.135378,6.785107,4.311075,1.732110,8.595799,-4.705827,-9.173311,-3.464805,-8.281573,3.184591,6.483761,-3.687013,-4.081604,6.635991,-8.166983,-4.967471,6.745573,2.241766,-9.434517,-7.010380,-8.217934,5.415286,7.871443,-1.068300,3.741590,5.084185,1.127015,3.000924,-5.841995,3.648133,-1.242433,-4.582249,1.223743,-6.765874,-6.297841,-8.216974,4.425103,0.097576,6.197234,-0.661868,9.563442,0.185308,-6.799480,-7.457208,7.150635,7.556108,3.461585,-8.242188,8.286319,2.768522,4.331740,8.958240,1.505865,3.610977,-7.951166,4.001235,-5.412827,-3.801267,4.788299,0.645351,-6.000448,4.144030,-0.117347,-8.506598,-8.778013,9.782290,8.077544,6.775677,5.522578,-4.575996,-8.061750,7.581288,-7.187464,9.522616,8.342524,2.864095,6.712722,0.016888,-1.288015,-7.287606,3.705106,-0.180804,-7.716728,9.459803,2.777708,7.289694,-3.275507,-2.125772,-2.864451,-6.913800,-1.038654,7.362669,-6.452279,-2.131457,-7.623977,-6.655474,-5.033009,9.543480,-7.386924,0.462695,-5.274040,8.203386,3.208998,0.519375,-1.942359,3.900069,2.519167,-7.374996,-3.018189,-6.729760,6.023559,-4.288262,-5.713412,-9.147114,6.501999,-0.560491,-2.043088,-6.251648,7.598957,2.090201,1.823076,-3.905262,6.644961,0.799211,9.046665,8.463102,-9.768034,2.136285,6.057875,6.430753,4.247439,-5.501369,6.546105,4.390296,-6.249729,-6.518562,-7.014194,7.512717,-9.986542,2.872450,-4.354354,-4.456487,-7.851318,5.806048,-7.639813,-0.455829,-6.936481,2.375824,9.963409,-2.889459,-3.706140,-4.904765,-1.558213,-7.768724,-5.320361,-7.012901,-8.113438,4.858711,-9.727582,-7.587233,3.450958,-3.915390,1.001873,2.878955,4.115732,9.261245,9.340660,-3.378758,5.918549,-9.999945,-7.296073,-9.074312,5.147042,6.745377,1.164248,-3.782949,7.370424,-8.421272,7.146508,4.065035,-3.137598,-9.739163,-6.899536,7.483456,7.570137,0.382469,-5.002890,6.709405,3.279213,-8.097402,-8.810310,0.609151,7.358964,7.513183,-8.593235,8.075338,4.498339,-2.357136,-2.052554,6.318329,8.955904,7.028843,-5.876427,4.544990,-4.063073,-9.267149,8.193458,-0.807137,-8.320833,8.269019,-2.262331,7.415916,-6.711647,-6.430245,9.948407,-1.300403,-8.333955,-9.899587,-6.863391,3.314282,5.163480,-2.673003,6.274071,-4.874702,-1.832532,-9.546439,-4.483913,-6.803514,1.092272,-7.817418,-2.510672,8.369592,-2.418804,1.758897,-8.371394,8.900328,8.322576,-1.021113,-8.451370,-2.430679,-3.831156,-8.941663,-8.145515,4.697599,0.546894,-2.745201,-5.521641,-5.748851,4.177848,-6.010461,-5.611613,-7.661531,8.990836,4.121361,4.875485,-4.181839,-0.821428,-5.380464,7.828604,2.161445,6.704983,-5.683857,9.811314,3.524307,-5.501444,-7.657514,2.775915,-8.070167,3.063940,3.988477,5.792828,-2.695927,-6.786275,-5.529031,-3.030800,-5.341612,4.949724,-0.414097,0.484666,-4.676177,7.435083,0.253814,0.168650,0.897721,1.680902,9.171913,-4.007359,-5.778435,-9.869412,-0.189496,-0.480443,2.872735,6.189007,0.908278,3.805282,-0.993983,-3.023153,9.623803,-7.536918,7.054135,6.471301,-6.973569,-9.740315,-4.583774,-0.224700,-8.227674,4.854948,-3.245137,6.230736,-2.547371,0.813468,0.112291,-4.887439,7.228424,0.471968,-4.726126,9.811012,-8.891586,1.736289,5.768327,9.115592,8.949888,2.387416,6.973930,5.181671,5.874493,-9.682178,-9.600902,7.070937,2.103752,-8.496685,-2.483637,7.527651,-2.352492,7.143272,-9.253656,0.767650,-9.497371,1.442600,4.892386,8.910800,-1.909700,2.041863,-5.415148,-0.295341,2.408153,5.000392,9.791979,-3.410773,8.746390,2.432456,-1.271419,0.339420,3.647059,-6.613929,4.022670,6.457455,5.863871,0.855778,5.458726,-1.820340,-4.630337,-9.330556,-6.194750,8.228675,6.563783,1.462514,7.767345,-9.604550,4.712013,5.099961,-9.237589,-5.239263,1.296563,6.822332,-5.983036,0.275578,0.618731,-1.709610,-2.910527,6.775572,-2.920021,2.476418,-7.060406,-1.541272,-2.244550,-2.570661,-5.049299,5.568353,-7.649200,-6.858463,-8.111672,-4.372364,-2.346904,7.178100,-8.428070,-8.340369,6.178762,9.734927,8.414189,7.360679,2.695848,-7.646741,1.698113,-6.800745,-8.794681,-1.485095,-6.266361,-9.223111,5.255935,-5.267993,-9.140172,-1.809222,-3.545749,5.285743,1.963973,-4.170379,8.018538,-7.870502,-6.393454,-6.763751,9.650077,6.104788,9.189619,-3.837877,8.293787,3.518229,8.201866,7.985312,9.547793,4.532437,1.739549,9.612660,-6.106901,0.280036,-6.306275,6.836417,-2.497665,-3.227843,-0.053452,-3.101140,7.819597,-3.004326,1.672408,-8.301504,-5.611758,2.595975,2.934855,-8.266346,-1.271482,-6.863356,-4.403070,0.354421,-0.080744,-1.135103,-8.282665,-6.595130,-4.873166,4.254067,-1.367886,-9.651935,2.105378,3.687076,5.194350,8.516014,9.698693,-7.570237,5.726158,6.504531,7.504503,2.496679,-6.481564,7.505377,-3.569240,6.714882,2.547791,6.481938,5.597284,4.293058], dtype = "float32")#candidate|4028|(630,)|const|float32
call_4027 = relay.TupleGetItem(func_3829_call(relay.reshape(const_4028.astype('float32'), [630,])), 1)
call_4029 = relay.TupleGetItem(func_3832_call(relay.reshape(const_4028.astype('float32'), [630,])), 1)
func_3958_call = mod.get_global_var('func_3958')
func_3960_call = mutated_mod.get_global_var('func_3960')
call_4039 = func_3958_call()
call_4040 = func_3958_call()
output = relay.Tuple([bop_4020,call_4027,const_4028,call_4039,])
output2 = relay.Tuple([bop_4023,call_4029,const_4028,call_4040,])
func_4056 = relay.Function([], output)
mod['func_4056'] = func_4056
mod = relay.transform.InferType()(mod)
output = func_4056()
func_4057 = relay.Function([], output)
mutated_mod['func_4057'] = func_4057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4056_call = mod.get_global_var('func_4056')
func_4057_call = mutated_mod.get_global_var('func_4057')
call_4058 = relay.TupleGetItem(func_4056_call(), 3)
call_4059 = relay.TupleGetItem(func_4057_call(), 3)
output = call_4058
output2 = call_4059
func_4067 = relay.Function([], output)
mod['func_4067'] = func_4067
mod = relay.transform.InferType()(mod)
mutated_mod['func_4067'] = func_4067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4067_call = mutated_mod.get_global_var('func_4067')
call_4068 = func_4067_call()
output = call_4068
func_4069 = relay.Function([], output)
mutated_mod['func_4069'] = func_4069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_962_call = mod.get_global_var('func_962')
func_964_call = mutated_mod.get_global_var('func_964')
call_4075 = relay.TupleGetItem(func_962_call(), 0)
call_4076 = relay.TupleGetItem(func_964_call(), 0)
uop_4077 = relay.cos(call_4075.astype('float64')) # shape=(7, 15, 1)
uop_4079 = relay.cos(call_4076.astype('float64')) # shape=(7, 15, 1)
func_4056_call = mod.get_global_var('func_4056')
func_4057_call = mutated_mod.get_global_var('func_4057')
call_4087 = relay.TupleGetItem(func_4056_call(), 0)
call_4088 = relay.TupleGetItem(func_4057_call(), 0)
func_4067_call = mod.get_global_var('func_4067')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_4106 = func_4067_call()
call_4107 = func_4067_call()
func_1944_call = mod.get_global_var('func_1944')
func_1947_call = mutated_mod.get_global_var('func_1947')
var_4113 = relay.var("var_4113", dtype = "float64", shape = (20, 4))#candidate|4113|(20, 4)|var|float64
call_4112 = relay.TupleGetItem(func_1944_call(relay.reshape(var_4113.astype('float64'), [10, 8, 1])), 0)
call_4114 = relay.TupleGetItem(func_1947_call(relay.reshape(var_4113.astype('float64'), [10, 8, 1])), 0)
bop_4115 = relay.add(uop_4077.astype('int8'), relay.reshape(call_4106.astype('int8'), relay.shape_of(uop_4077))) # shape=(7, 15, 1)
bop_4118 = relay.add(uop_4079.astype('int8'), relay.reshape(call_4107.astype('int8'), relay.shape_of(uop_4079))) # shape=(7, 15, 1)
func_2582_call = mod.get_global_var('func_2582')
func_2584_call = mutated_mod.get_global_var('func_2584')
var_4120 = relay.var("var_4120", dtype = "uint32", shape = (756,))#candidate|4120|(756,)|var|uint32
call_4119 = func_2582_call(relay.reshape(var_4120.astype('uint32'), [14, 6, 9]))
call_4121 = func_2582_call(relay.reshape(var_4120.astype('uint32'), [14, 6, 9]))
func_2175_call = mod.get_global_var('func_2175')
func_2176_call = mutated_mod.get_global_var('func_2176')
call_4122 = relay.TupleGetItem(func_2175_call(), 0)
call_4123 = relay.TupleGetItem(func_2176_call(), 0)
func_815_call = mod.get_global_var('func_815')
func_816_call = mutated_mod.get_global_var('func_816')
call_4124 = relay.TupleGetItem(func_815_call(), 1)
call_4125 = relay.TupleGetItem(func_816_call(), 1)
output = relay.Tuple([call_4087,call_4112,var_4113,bop_4115,call_4119,var_4120,call_4122,call_4124,])
output2 = relay.Tuple([call_4088,call_4114,var_4113,bop_4118,call_4121,var_4120,call_4123,call_4125,])
func_4129 = relay.Function([var_4113,var_4120,], output)
mod['func_4129'] = func_4129
mod = relay.transform.InferType()(mod)
var_4130 = relay.var("var_4130", dtype = "float64", shape = (20, 4))#candidate|4130|(20, 4)|var|float64
var_4131 = relay.var("var_4131", dtype = "uint32", shape = (756,))#candidate|4131|(756,)|var|uint32
output = func_4129(var_4130,var_4131,)
func_4132 = relay.Function([var_4130,var_4131,], output)
mutated_mod['func_4132'] = func_4132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2987_call = mod.get_global_var('func_2987')
func_2988_call = mutated_mod.get_global_var('func_2988')
call_4217 = func_2987_call()
call_4218 = func_2987_call()
output = call_4217
output2 = call_4218
func_4237 = relay.Function([], output)
mod['func_4237'] = func_4237
mod = relay.transform.InferType()(mod)
mutated_mod['func_4237'] = func_4237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4237_call = mutated_mod.get_global_var('func_4237')
call_4238 = func_4237_call()
output = call_4238
func_4239 = relay.Function([], output)
mutated_mod['func_4239'] = func_4239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3586_call = mod.get_global_var('func_3586')
func_3587_call = mutated_mod.get_global_var('func_3587')
call_4256 = func_3586_call()
call_4257 = func_3586_call()
output = call_4256
output2 = call_4257
func_4258 = relay.Function([], output)
mod['func_4258'] = func_4258
mod = relay.transform.InferType()(mod)
mutated_mod['func_4258'] = func_4258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4258_call = mutated_mod.get_global_var('func_4258')
call_4259 = func_4258_call()
output = call_4259
func_4260 = relay.Function([], output)
mutated_mod['func_4260'] = func_4260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3944_call = mod.get_global_var('func_3944')
func_3945_call = mutated_mod.get_global_var('func_3945')
call_4311 = relay.TupleGetItem(func_3944_call(), 0)
call_4312 = relay.TupleGetItem(func_3945_call(), 0)
const_4315 = relay.const([[[True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,False],[True,False,False,True,False,True,False,True,True,False,False,False,False,True,False,False],[False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False],[False,False,True,False,False,False,True,True,False,True,True,False,True,True,False,True],[False,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False],[False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True],[False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False],[False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False],[False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,False],[False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,False],[False,True,True,True,False,False,False,False,True,True,False,True,True,True,True,True],[True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False],[True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False],[False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False],[True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False]],[[False,True,False,False,True,True,False,True,True,False,True,False,True,True,True,False],[False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False],[False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False],[False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True],[False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True],[False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False],[True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False],[False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False],[False,True,False,False,True,False,False,True,False,True,True,False,True,False,True,False],[False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False],[False,False,False,True,False,False,True,False,False,False,False,True,False,True,True,False],[False,False,True,True,True,False,False,False,False,True,False,False,False,False,False,True],[False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False],[False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True],[True,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False]],[[True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,True],[False,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False],[False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True],[False,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False],[False,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True],[True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False],[False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False],[True,False,False,True,False,False,False,True,False,True,True,False,True,False,False,True],[True,False,False,True,False,True,True,False,True,True,False,False,False,False,False,True],[False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False],[True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True],[True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False],[False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False],[True,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True],[True,True,True,True,False,True,True,False,True,True,True,False,True,False,False,False]],[[True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False],[False,False,True,False,True,True,False,False,False,False,True,True,False,True,True,False],[True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True],[False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,False],[True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True],[False,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False],[True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False],[False,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True],[False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,False],[True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True],[False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False],[False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False],[False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True],[False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,True],[False,False,False,True,True,True,False,True,False,False,False,False,True,True,True,True]],[[True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False],[True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True],[False,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True],[False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,True],[False,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True],[True,False,True,True,True,False,True,True,True,True,True,False,True,False,True,False],[True,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False],[False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False],[True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True],[False,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False],[False,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True],[True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True],[True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,False],[True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False],[False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False]],[[False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True],[True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True],[False,True,False,False,True,True,False,True,False,False,False,True,True,False,True,False],[False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False],[False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,True],[False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False],[True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True],[False,False,True,True,False,True,True,False,False,False,True,False,False,True,False,True],[True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False],[True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True],[True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True],[False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False],[False,False,True,False,False,True,True,True,True,False,False,True,False,True,True,False],[False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False],[True,True,False,True,False,True,False,False,True,True,True,True,False,False,True,False]],[[False,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True],[False,False,False,True,True,True,True,True,False,False,False,False,True,False,True,True],[True,False,True,True,False,False,False,True,True,True,False,False,False,True,True,False],[True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,True],[True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True],[True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False],[True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False],[False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,False],[False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False],[True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True],[True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,False],[True,False,True,True,False,False,False,True,False,False,True,False,True,True,True,False],[True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True],[False,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False],[False,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False]]], dtype = "bool")#candidate|4315|(7, 15, 16)|const|bool
bop_4316 = relay.left_shift(call_4311.astype('int64'), relay.reshape(const_4315.astype('int64'), relay.shape_of(call_4311))) # shape=(7, 15, 16)
bop_4319 = relay.left_shift(call_4312.astype('int64'), relay.reshape(const_4315.astype('int64'), relay.shape_of(call_4312))) # shape=(7, 15, 16)
output = relay.Tuple([bop_4316,])
output2 = relay.Tuple([bop_4319,])
func_4320 = relay.Function([], output)
mod['func_4320'] = func_4320
mod = relay.transform.InferType()(mod)
output = func_4320()
func_4321 = relay.Function([], output)
mutated_mod['func_4321'] = func_4321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_4346 = relay.TupleGetItem(func_1590_call(), 0)
call_4347 = relay.TupleGetItem(func_1592_call(), 0)
func_3325_call = mod.get_global_var('func_3325')
func_3328_call = mutated_mod.get_global_var('func_3328')
const_4349 = relay.const([3.219870,6.661787,5.046571,-9.923419,5.797514,-5.681637,8.438704,-8.976614,5.167794,4.463067,-3.541441,-3.681992,4.900187,2.888404,2.914636,4.950454,-5.549887,7.847848,0.454236,6.157975,-5.199444,-4.392197,2.108093,-8.681414,5.924015,4.089590,0.068441,3.217363,4.963935,1.099405,3.124876,7.151776,5.650542,-7.789917,9.042878,-2.859809,2.878320,3.588826,9.294339,7.684892,5.047503,-4.284917,-6.467045,4.319737,-4.771129,9.739106,9.987136,8.241180,6.222081,-8.737696,8.339434,-4.691343,1.675406,9.346221,-3.478144,9.526938,2.522084,-4.272371,3.103536,-3.033503,-9.362883,-8.556313,-1.033106,-2.826821,1.124836,-8.629083,3.852264,4.905926,-2.942548,3.390334,9.317144,-0.769047,-3.007685,-7.697424,-7.179526,3.836252,-3.278862,0.046756,1.897763,-9.729492,-9.759388,-2.600300,-5.995078,-6.028662,-6.917135,9.079335,-1.272513,1.033501,-5.890703,-2.017114,-0.711510,7.513569,1.937402,9.249729,-0.841105,6.943635,4.152861,3.128816,4.722374,-7.795388,6.299248,1.903303,-0.436395,1.045426,4.948283,3.618374,0.851846,-9.818146,1.526636,-4.879754,-8.448685,-0.163229,5.601405,6.829844,4.783949,-3.224952,5.495696,-6.794508,-7.606650,-0.373229,-8.691106,9.968824,-7.818481,-9.463306,-8.819381,5.652551,1.792011,-7.933285,5.624537,7.648812,4.716879,-2.026348,-8.131576,-3.228444,-0.160242,-8.305091,9.606700,-9.517390,9.425717,2.405124,3.563249,-3.577116,5.079090,2.625023,-8.624863,8.793076,9.701498,-5.646016,7.021334,-0.851330,2.434602,-4.482339,4.266093,-3.134825,5.820300,-0.356880,1.095406,8.493167,3.297371,7.482937,-9.933867,0.227667,-4.079311,7.776171,9.002380,3.174970,-1.582954,3.688173,6.428426,-7.934838,0.648151,8.130737,-6.845401,4.453392,-0.791436,1.141682,-1.069749,-7.440683,3.198069,-1.336328,4.131571,3.914126,1.215484,0.078439,7.720946,1.625538,-0.156457,5.147240,-2.991339,-2.017310,6.378757,8.827180,0.021546,7.001808,9.733293,5.558846,5.214051,-1.742908,1.059482,4.899357,0.156541,0.711154,-6.552935,-3.891071,-6.495362,8.310271,0.879566,8.189045,-0.302694,6.819111,-2.112010,-0.274252,2.493028,-2.650918,5.603332,3.632516,-8.453229,-4.705857,7.444660,1.904340,-6.115671,-9.232406,6.081709,-1.057105,-7.854862,7.312406,-8.764406,-0.775761,-2.598613,-4.219891,8.230422,7.276394,-9.320489,-0.957314,-8.852538,4.852540,-2.134572,-5.558441,0.682665,2.375242,-8.765671,-6.196214,-9.797625,3.667088,5.674465,-2.351331,1.364979,5.522685,-4.371138,-1.286133,0.331114,6.057261,7.195269,-9.442076,-1.639216,-8.061292,-4.226752,3.162245,7.558167,-9.246692,-4.122681,6.830780,-2.004844,2.024106,-2.189138,8.098436,-3.281174,7.386153,8.792268,-1.323362,8.183487,-5.137463,-8.126609,3.578030,-7.442142,-2.410571,-8.358952,5.790934,-4.385000,3.023341,-0.668667,6.239160,2.145346,-2.534304,-2.289398,-1.648703,0.582014,9.861905,-5.713251,0.672280,-7.350594,7.888491,-3.975862,7.147848,-8.255504,4.843408,-9.789945,2.730235,-4.410766,-7.855111,-5.768191,-6.918257,4.912669,3.345058,-7.970160,6.479973,0.136369,-9.986879,3.413688,-0.934045,-4.941080,-8.306904,-8.301195,9.255144,2.954636,5.822839,-4.759327,6.959138,-9.660272,-9.546744,0.798441,4.841258,-9.774447,-3.222791,-6.698691,4.852319,2.516104,7.056129,0.064846,-4.159790,-3.949066,7.779739,7.043973,-1.063954,4.798609,3.348926,-2.363237,1.796098,-0.720078,-3.649119,9.774201,3.298028,7.778838,-6.862907,7.595430,4.188416,2.917977,8.290085,4.268592,-8.978860,-4.529020,-7.096611,-6.352295,8.540861,4.186170,1.833998,-7.500979,7.222749,9.810007,-6.312216,-5.301447,-6.181830,-7.139536,1.917817,-8.415648,9.052369,5.390615,9.001030,1.459163,-7.188110,5.419840,0.319480,-2.150157,2.739822,2.688105,8.854165,-3.616862,6.974909,2.652236,-2.452428,-0.648160,-3.536399,8.097954,0.081513,-6.904479,-1.731436,-8.437705,5.076146,-0.613648,-6.760016,6.163824,-7.193427,-8.824816,-5.552159,-6.040665,4.411812,-9.040207,-7.446307,1.129452,6.648503,3.482431,0.104778,5.394648,-2.176799,-8.205613,8.188868,-9.947700,2.259820,1.023864,-5.246013,-9.703640,-7.026009,5.933090,7.990237,4.670388,7.407945,-0.766243,-7.248720,3.298807,3.676174,4.777128,9.417897,-5.238193,-7.273381,2.672677,4.005996,-2.728179,-7.527532,-3.437126,1.095355,-7.095599,-3.876070,2.586857,6.729552,-5.033705,-1.921188,9.797619,2.194044,-2.520756,-3.958782,6.660555,-5.693346,3.470111,9.654889,-5.431771,6.647787,0.682259,8.593827,-8.643574,-1.580707,4.251201,8.546541,-8.554571,3.642413,-6.615921,-7.085907,3.990048,-7.442663,-8.032553,0.339057,-4.873354,6.760867,-2.857983,-2.905343,8.718622,4.503918,-1.632301,-5.569503,-7.373073,5.888880,3.604448,-2.649914,-4.627627,4.603914,-3.258235,2.198770,-9.348494,6.519056,0.674545,9.320474,-0.715185,-2.774303,5.892501,7.682859,-0.486156,0.505666,1.856580,-0.058085,-1.508674,-5.873458,-5.925727,5.770058,-9.438993,-8.672936,-0.916295,1.149004,-1.916546,0.532427,-5.410526,7.274897,-4.407896,-4.089176,-0.085953,8.742469], dtype = "float64")#candidate|4349|(504,)|const|float64
call_4348 = relay.TupleGetItem(func_3325_call(relay.reshape(const_4349.astype('float64'), [36, 14])), 2)
call_4350 = relay.TupleGetItem(func_3328_call(relay.reshape(const_4349.astype('float64'), [36, 14])), 2)
output = relay.Tuple([call_4346,call_4348,const_4349,])
output2 = relay.Tuple([call_4347,call_4350,const_4349,])
func_4351 = relay.Function([], output)
mod['func_4351'] = func_4351
mod = relay.transform.InferType()(mod)
output = func_4351()
func_4352 = relay.Function([], output)
mutated_mod['func_4352'] = func_4352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3586_call = mod.get_global_var('func_3586')
func_3587_call = mutated_mod.get_global_var('func_3587')
call_4409 = func_3586_call()
call_4410 = func_3586_call()
output = call_4409
output2 = call_4410
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
func_3586_call = mod.get_global_var('func_3586')
func_3587_call = mutated_mod.get_global_var('func_3587')
call_4504 = func_3586_call()
call_4505 = func_3586_call()
output = relay.Tuple([call_4504,])
output2 = relay.Tuple([call_4505,])
func_4506 = relay.Function([], output)
mod['func_4506'] = func_4506
mod = relay.transform.InferType()(mod)
mutated_mod['func_4506'] = func_4506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4506_call = mutated_mod.get_global_var('func_4506')
call_4507 = func_4506_call()
output = call_4507
func_4508 = relay.Function([], output)
mutated_mod['func_4508'] = func_4508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_4518 = relay.TupleGetItem(func_1590_call(), 1)
call_4519 = relay.TupleGetItem(func_1592_call(), 1)
output = call_4518
output2 = call_4519
func_4530 = relay.Function([], output)
mod['func_4530'] = func_4530
mod = relay.transform.InferType()(mod)
output = func_4530()
func_4531 = relay.Function([], output)
mutated_mod['func_4531'] = func_4531
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4539 = relay.const([[[-0.268670,2.675128],[6.322468,7.360748],[8.963272,5.972477],[-8.821617,-3.690807],[9.992319,-9.716789]],[[8.960108,-0.554182],[9.892845,-2.410372],[-6.156440,2.936790],[-5.395843,6.763887],[-9.564140,1.648611]],[[6.560858,-6.925043],[4.651307,-3.216910],[-1.720551,-8.896697],[8.564353,9.876782],[3.605870,9.641634]],[[1.959534,-6.407029],[8.655408,6.228303],[-7.435768,-9.486151],[-9.398575,4.646751],[3.849579,-7.210537]],[[-6.367775,0.623111],[4.987572,3.441258],[-8.660125,3.400198],[3.810796,8.507167],[8.724100,6.470283]],[[-8.865596,8.112350],[-2.310139,-2.466795],[-4.393655,6.662292],[-7.403566,4.539052],[-5.583391,-2.086030]]], dtype = "float32")#candidate|4539|(6, 5, 2)|const|float32
uop_4540 = relay.rsqrt(const_4539.astype('float32')) # shape=(6, 5, 2)
func_2811_call = mod.get_global_var('func_2811')
func_2816_call = mutated_mod.get_global_var('func_2816')
var_4560 = relay.var("var_4560", dtype = "float32", shape = (210,))#candidate|4560|(210,)|var|float32
const_4561 = relay.const([9,5,-10,-9,-2,-10,-10,-10,5,-2,-4,-9,7,-3,-5,-2,-2,4,-6,8,-8,2,-1,4,10,6,-8,3,1,6,-10,4,-9,-5,1,-4,-2,-10,9,-10,1,5,10,-5,-5,1,-3,-9,-3,-9,10,5,10,-6,9,-7,1,-2,-9,-4,-7,-10,-7,-5,5,-5,7,-10,5,-3,-1,7,-10,3,-5,4,1,4,-4,10,-1,6,-7,5,2,8,-8,-5,5,8,4,-4,5,-3,-5,10,-8,-5,5,-8,-8,10,3,-4,3,10,3,10,-2,-7,-8,6,-5,2,5,-5,-6,10,-10,2,6,9,-8,7,6,10,3,9,-10,-6,-10,-7,5,8,2,7,1,-7,-6,10,10,-5,5,9,-4,-10,5,1,-3,-5,8,-2,1,10,6,9,-10,-7,8,-10,-2,-7,8,-8,8,7,-9,-6,8,8,-6,10,-3,2,-4,4,-3,-2,8,1,3,-3,-6,-1,-5,-10,5,-8,4,10,2,-3,-4,5,3,9,5,10,-10,-8,1,-7,-6,7,-5,-10,-10,2,-8,-9,5,8,-9,-3,-1,-4,-7,-9,8,-4,2,9,-7,-7,2,-7,-3,8,5,-10,10,-9,9,-9,3,-9,7,8,-3,-8,-10,-1,-10,-6,8,-1,2,-5,-7,7,8,-6,7,9,-10,4,-2,4,2,6,6,8,9,-10,-8,8,-6,-2,-10,-5,-8,10,-4,3,-4,7,8,9,-1,-6,7,-6,10,-8,-9,-3,-9,-8,-7,10,9,1,-5,5,-9,-6,4,-1,-1,7,1,-8,2,5,6,1,3,5,4,5,-2,2,-4,-2,-2,-5,-10,-5,-1,-2,-8,-6,-8,-10,-2,6,3,-2,10,1,7,-9,1,7,-6,10,-5,4,9,4,6,-7,-7,-7,-5,3,6,-6,5,10,-6,3,9,5,-1,9,-8,-10,5,5,8,1,7,-1,-5,-4,-3,2,-6,8,-5,-7,-3,-9,-4,8,2,6,-1,2,7,-6,-2,-10,7,-6,-7,5,-9,10,-1,-5,-2,-10,7,-8,9,3,-4,10,5,2,-8,-3,3,2,4,7,-8,8,1,10,-9,1,-7,5,-8,3,-5,-5,-2,4,-4,-3,-8,-8,8,-8,2,-2,-2,-3,7,-8,-4,3,-8,3,8,4,10,6,1,-7,-5,4,-10,-10,2,-9,1,-2,1,-10,-5,6,6,3,5,-2,1,-2,10,-7,-1,9,-8,-10,-8,7,-7,-1,6,2,-6,-4,8,-9,9,1,2,-2,10,-9,-4,-4,-1,4,10,1,-10,-4,-2,-1,1,-10,3,-3,-6,3,-9,1,-3,9,2,-1,6,5,10,-10,-7,4,-4,2,7,2,-6,10,-1,-3,1,-7,1,5,-9,2,5,5,3,1,-7,-8,7,2,-8,-3,1,4,-4,-3,5,-9,1,2,-5,4,8,-5,-1,-5,2,-8,7,-4,2,-6,-1,7,-2,6,2,9,1,6,-9,-10,10,5,-9,-10,4,-8,-2,-9,-4,2,-4,-7,-5,8,6,6,-6,-3,9,8,1,2,-2,10,5,-3,4,-5,-5,-4,3,-6,2,5,-7,7,-10,-3,-10,-8,8,-6,-1,1,6,-8,-7,7,6,-3,9,-2,10,1,10,-5,-3,1,5,-2,9,-9,4,10,-2,-4,-4,9,-2,2,-10,-10,-1,8,5,7,10,2,4,6,4,6,-6,10,5,-10,2,-9,3,8,-7,-1,3,-3,-5,6,8,-5,-6,2,10,8,2,-4,-7,2,-9,3,8,2,6,3,9,8,-5,-7,-10,7,-4,-8,5,-7,5,-8,-7,-4,-8,6,-5,3,5,-4,-6,-9,-2,-3,7,1,3,4,-10,2,-7,5,3,3,9,2,-8,8,-8,-7,5,8,9,-6,2,7,6,-1,-2,-6,-2,6,9,-2,-7,3,-8,7,-5,-6,-3,-4,9,-10,10,1,6,3,-1,4,5,9,-10,-1,-1,10,2,-7,-1,-1,4,-4,9,-6,6,8,9,7,6,-2,6,5,8,-8,-8,10,1,2,5,10,-10,-3,8,6,-7,-4,-10,1,-8,7,-8,-10,2,8,-2,9,9,-10,-1,4,7,-8,-5,-7,10,1,-10,8,2,3,6,-3,3,3,-2,-1,5,5,10,4,-5,-7,-5,1,3,-1,-6,-6,-10,5,8,-8,-5,2,7,5,-3,1,7,7,-7,-9,-3,-2,-3,-4,2,3,-6,-5,5,9,2,7,-3,9,3,1,-10,8,1,-6,3,-2,-6,-6,-9,-8,4,-10,10,-6,-7,8,3,3,-7,9,-10,-10,10,-7,2,9,1,-2,-9,3,-7,-5,6,-4,-9,-2,6,5,-10,4,-10,-8,2,-3], dtype = "int8")#candidate|4561|(900,)|const|int8
var_4562 = relay.var("var_4562", dtype = "uint16", shape = (286,))#candidate|4562|(286,)|var|uint16
call_4559 = relay.TupleGetItem(func_2811_call(relay.reshape(var_4560.astype('float32'), [7, 15, 2]), relay.reshape(const_4561.astype('int8'), [900,]), relay.reshape(var_4562.astype('uint16'), [286,]), ), 3)
call_4563 = relay.TupleGetItem(func_2816_call(relay.reshape(var_4560.astype('float32'), [7, 15, 2]), relay.reshape(const_4561.astype('int8'), [900,]), relay.reshape(var_4562.astype('uint16'), [286,]), ), 3)
uop_4565 = relay.asin(uop_4540.astype('float32')) # shape=(6, 5, 2)
func_3190_call = mod.get_global_var('func_3190')
func_3192_call = mutated_mod.get_global_var('func_3192')
const_4600 = relay.const([[True,True,False,False,True,True,True,True,True,True,True,True,False,True],[True,True,True,False,False,True,True,False,False,True,False,True,False,False],[True,False,True,False,True,True,False,False,False,True,True,True,False,False],[True,True,True,False,False,False,False,False,True,True,True,False,True,True],[True,True,True,False,True,False,False,False,False,False,False,False,True,True],[False,True,True,True,False,True,True,True,True,True,True,True,False,False],[True,True,True,False,True,False,False,False,True,False,True,True,False,True],[True,True,True,True,False,False,False,True,True,True,False,True,False,True],[False,True,False,True,False,True,True,True,False,True,False,True,True,True],[False,True,False,True,False,True,True,False,False,True,True,True,True,True],[False,True,True,False,False,True,True,True,False,False,False,False,True,False],[True,False,True,True,True,False,True,True,True,False,False,True,True,True],[True,False,True,True,False,False,False,False,True,True,True,True,False,False],[False,True,False,True,False,False,True,True,False,False,True,True,False,True],[True,True,False,False,False,True,True,False,True,True,False,False,True,False],[False,True,False,False,False,False,True,False,False,False,False,False,False,True],[False,False,False,True,False,False,True,False,False,False,False,True,False,False],[False,True,False,False,False,False,False,False,True,True,True,True,False,True],[False,False,False,False,True,False,True,True,False,False,True,False,False,True],[False,False,True,False,True,False,False,True,False,False,False,True,True,True],[True,True,False,True,False,False,True,True,False,False,False,False,False,True],[True,False,False,True,True,True,True,False,True,True,False,False,True,False],[True,False,True,False,False,True,True,False,True,False,True,True,False,True],[True,False,False,False,True,False,True,False,True,False,False,True,True,False],[True,False,False,False,True,True,True,True,False,False,True,True,True,False],[False,True,True,False,False,True,False,True,True,False,True,False,False,True],[True,False,False,False,False,False,True,True,False,False,False,False,False,True],[False,True,True,False,True,False,False,True,True,True,False,False,True,True],[True,True,False,False,True,False,True,False,True,False,True,True,False,False],[True,False,True,True,False,True,False,True,True,False,False,True,True,False],[True,False,True,False,False,True,True,True,False,False,True,True,False,True],[False,False,True,True,False,False,True,False,True,True,True,True,True,True],[False,True,True,True,True,False,False,True,False,True,True,False,True,False],[True,True,True,True,True,False,False,True,True,True,False,False,False,True],[True,False,True,True,True,False,True,False,True,True,False,True,False,True],[True,True,True,False,False,True,True,True,True,True,False,False,True,False],[True,True,False,False,True,True,False,False,True,True,True,False,False,True],[True,False,False,False,True,True,False,True,False,True,False,False,True,False],[False,False,True,True,True,True,False,True,False,False,True,True,True,False],[False,True,True,True,True,True,False,False,True,False,True,True,False,True],[True,True,True,False,True,False,True,False,True,True,True,True,True,True],[True,False,True,True,True,True,False,False,False,False,False,True,True,True],[True,True,False,False,False,False,False,True,False,False,True,False,True,True],[True,True,False,False,True,True,True,True,False,False,True,True,False,False],[False,True,True,True,False,False,False,False,False,False,True,False,False,True],[False,False,False,False,True,False,False,False,True,False,True,False,False,True],[True,False,True,True,False,False,True,False,False,True,True,False,True,False],[True,False,True,True,False,True,True,True,True,False,True,True,False,True],[True,False,False,False,False,True,True,False,True,False,True,False,True,False],[False,True,False,True,True,False,True,True,True,False,False,True,False,True],[False,False,False,True,False,False,True,True,True,False,True,True,True,False],[True,False,False,True,True,True,True,False,True,False,True,False,False,True],[True,True,True,True,True,True,False,False,False,True,True,True,False,False],[False,True,True,True,True,True,True,True,False,False,True,True,False,True],[False,False,False,True,True,True,True,True,True,True,True,True,True,False],[False,True,False,True,False,True,False,True,True,True,False,True,True,False],[True,True,True,True,False,True,False,True,True,True,False,False,True,True],[True,False,True,True,True,False,False,True,True,True,False,False,False,True],[False,False,True,True,True,False,False,True,True,False,True,False,False,True],[False,True,True,True,True,False,True,False,False,True,True,False,False,True],[False,True,False,False,True,True,True,False,True,True,False,True,False,True],[True,False,False,False,True,True,True,False,False,False,False,False,False,True],[False,False,False,True,True,True,True,False,False,True,True,False,False,True],[True,False,False,False,False,False,False,True,False,False,True,False,False,True],[False,False,False,True,True,True,False,False,False,True,True,False,False,False],[False,True,True,True,True,True,False,False,True,False,True,True,False,True],[True,True,False,False,True,True,True,False,False,True,True,False,False,False],[False,True,False,True,False,True,False,True,False,False,True,True,True,True],[True,True,False,False,False,False,False,False,True,True,False,True,False,True],[True,True,True,False,False,True,True,False,False,True,True,False,False,True],[False,True,False,True,False,False,True,True,False,False,True,False,True,True],[True,False,True,True,True,False,True,True,False,False,True,False,True,False],[True,True,True,True,False,True,False,True,True,True,False,False,True,True],[False,True,False,True,True,True,False,False,False,True,True,False,True,False],[False,True,False,True,False,False,False,True,True,False,False,True,False,False],[True,True,True,True,False,True,False,True,True,True,True,True,False,False],[True,False,False,True,True,True,True,True,True,True,False,False,False,False],[True,False,False,False,True,True,True,False,True,False,True,False,True,True],[True,True,True,False,True,False,True,False,True,False,False,False,False,False],[False,False,True,False,False,True,False,True,True,False,True,False,False,True],[False,True,False,True,False,True,True,False,True,False,False,False,True,False],[False,True,True,True,True,False,True,True,True,True,False,False,True,False],[False,True,True,False,False,True,True,True,False,False,True,False,True,True],[False,False,False,True,True,True,False,False,True,True,True,False,False,True],[True,False,True,True,True,False,False,False,True,True,True,False,False,False],[False,True,True,False,True,True,True,False,False,True,False,True,False,True],[False,True,False,True,True,False,False,False,False,False,False,False,False,True],[False,False,True,False,True,True,False,False,False,False,False,True,True,False],[False,False,True,False,True,True,True,False,True,False,False,False,False,True],[False,False,False,False,False,False,False,True,True,False,True,True,False,True],[False,False,True,True,False,False,True,True,False,True,True,True,True,True],[True,True,False,True,False,True,True,False,True,True,False,False,False,True],[True,False,True,False,False,False,True,False,True,False,True,True,True,False],[False,False,False,False,False,False,True,False,True,True,False,False,False,False],[False,False,False,False,True,True,False,True,True,True,False,False,True,True],[True,True,False,False,True,False,False,True,False,True,True,False,False,False],[False,True,False,True,True,False,True,False,True,True,False,True,False,False],[True,True,True,True,False,True,True,False,True,True,True,False,False,True],[False,True,True,False,False,True,True,True,False,False,False,True,True,False],[False,True,False,False,True,True,True,True,True,False,True,False,True,True],[False,True,False,False,False,True,True,False,False,False,False,False,True,False],[False,False,False,False,False,False,False,True,True,True,False,False,True,False],[True,False,True,True,False,True,False,False,False,True,True,False,True,True],[True,False,True,True,True,True,True,True,True,False,False,False,True,False],[True,True,False,False,True,True,True,True,False,True,False,False,False,True],[True,False,False,False,False,True,True,True,False,False,False,True,False,False],[True,False,True,False,True,True,False,False,True,False,False,True,True,False],[False,False,True,True,False,True,True,False,False,False,False,False,False,False],[True,True,True,False,True,False,True,False,True,True,False,False,True,False],[False,True,False,False,True,True,True,True,False,False,True,False,False,True],[False,False,False,True,True,True,False,False,True,True,False,False,False,True],[True,False,True,True,True,False,True,False,True,False,True,False,False,False],[False,False,False,True,False,False,False,False,True,False,False,False,True,True],[False,False,False,True,False,True,False,True,True,True,True,True,True,False],[True,True,False,True,True,False,False,False,False,True,False,True,True,False],[True,True,True,False,True,True,True,True,True,False,False,False,True,True],[True,True,True,False,False,True,False,False,False,False,False,False,True,False],[False,True,False,True,False,False,True,True,True,True,False,False,True,False],[True,False,True,False,True,False,True,False,True,True,False,True,True,False],[False,True,False,False,False,False,True,False,False,True,True,False,False,True],[False,True,True,True,True,False,False,True,False,True,True,True,False,True],[True,True,True,True,False,True,True,False,True,False,False,False,True,True],[False,True,False,False,False,True,False,False,True,False,True,True,True,False],[True,True,True,False,False,False,True,True,True,False,True,False,False,False],[False,False,True,False,True,False,True,False,True,True,False,True,True,True],[False,False,True,True,True,False,True,True,False,False,False,True,False,False],[True,True,False,False,True,True,False,False,True,True,False,True,False,False],[False,True,True,False,True,False,False,False,False,True,False,False,False,False],[True,False,False,True,True,False,True,False,False,True,True,True,True,True],[False,True,False,False,True,True,True,False,False,True,True,False,False,True],[True,False,True,False,True,False,True,False,False,False,True,False,False,False],[False,True,True,False,False,True,True,True,True,False,False,True,True,True],[True,True,False,False,False,True,True,True,True,False,True,False,True,False],[False,True,False,False,False,False,True,False,True,False,False,False,False,False],[True,True,True,True,False,True,True,False,False,False,True,False,True,True],[False,False,True,False,True,False,True,True,False,False,True,True,False,True],[False,False,True,True,True,False,False,True,True,False,False,False,False,True],[False,True,False,False,True,False,False,False,False,True,True,False,True,True],[True,True,False,True,True,False,True,False,False,True,False,False,True,False],[False,False,True,False,True,False,False,True,False,False,True,False,False,True],[False,True,False,True,True,False,True,False,False,False,True,True,True,True],[True,True,True,True,True,False,True,False,False,True,True,False,True,True],[False,True,False,False,True,False,False,False,False,True,False,True,True,True],[False,False,False,True,True,True,False,False,False,True,True,False,False,False],[True,True,True,True,True,True,False,False,True,False,False,False,True,False],[True,False,False,True,False,False,False,False,False,False,False,False,True,True],[False,True,False,True,False,True,True,True,True,True,True,False,True,True],[False,False,False,True,False,False,False,False,False,False,False,False,False,True],[False,True,False,True,False,False,False,True,False,True,False,True,False,False],[True,True,True,False,True,True,True,True,True,False,False,False,False,False],[False,True,True,True,False,False,False,True,False,False,False,False,False,False],[True,False,False,True,False,False,True,True,True,False,True,True,False,True],[True,True,True,True,False,True,False,False,True,False,True,True,True,True],[False,True,False,True,True,False,False,True,False,True,True,False,False,False],[True,False,True,False,True,False,True,True,True,False,False,False,False,True],[False,True,True,False,False,True,True,False,True,False,True,False,True,False],[False,True,False,True,False,True,True,True,False,False,True,True,False,True],[False,True,False,False,False,True,False,True,False,True,True,False,True,False],[False,True,True,False,False,True,True,False,True,False,False,True,False,True],[False,True,False,False,False,False,False,False,False,False,True,False,False,False],[False,True,True,False,False,False,False,True,True,True,True,False,True,True],[True,False,False,False,True,False,False,True,True,True,True,True,True,True],[True,True,True,False,True,False,False,True,False,True,False,False,False,False],[False,False,True,False,False,False,False,True,False,False,False,True,True,True],[False,True,False,False,False,False,False,True,False,False,True,True,True,True],[True,False,True,True,False,True,True,False,True,True,True,True,False,True],[True,True,False,True,False,True,True,True,True,True,False,True,False,True],[False,True,True,True,True,False,True,True,True,False,True,False,False,False],[False,False,True,True,True,False,False,False,True,False,True,False,True,True],[True,True,True,False,True,False,True,False,False,False,False,False,True,True],[False,True,False,False,True,True,True,False,True,False,False,False,False,True],[False,True,True,False,True,False,False,False,False,True,False,False,False,False],[False,True,False,True,False,False,True,True,True,True,True,True,True,False],[True,True,True,False,False,False,False,True,False,False,True,False,True,False],[True,True,False,True,False,False,False,False,False,False,True,False,True,True],[True,False,True,False,True,False,False,True,True,False,True,True,False,False],[False,False,False,True,True,True,False,False,True,True,False,False,True,False],[False,False,True,True,False,False,True,True,False,False,False,True,False,True],[True,True,False,True,True,False,False,False,True,False,False,True,True,True],[True,False,True,True,False,False,False,False,False,True,True,False,True,False],[False,False,True,True,True,True,False,False,False,False,False,True,False,True],[False,False,False,True,False,True,False,True,True,False,True,True,False,True],[True,True,True,True,True,False,False,False,False,False,False,False,False,True],[True,True,False,False,True,False,True,True,True,False,False,False,False,False],[True,False,True,False,False,False,False,True,False,False,False,False,True,False],[False,True,True,False,False,True,False,True,True,True,True,False,True,True],[False,False,True,True,False,False,False,False,False,False,False,True,False,False],[True,True,False,False,True,False,False,True,True,False,True,True,True,False],[True,True,True,False,True,True,True,True,True,True,False,False,True,False],[True,False,False,False,True,False,False,False,False,False,False,False,False,True],[True,False,True,False,True,False,False,False,True,False,True,True,True,True],[True,True,True,False,True,True,False,False,False,True,True,False,True,True],[False,False,False,True,False,True,False,True,True,False,True,True,False,False],[False,False,False,True,True,True,True,False,True,True,False,True,False,True],[True,False,False,False,False,False,True,False,True,True,True,True,False,False],[False,False,False,False,False,False,True,True,False,False,True,True,True,False],[False,False,True,True,False,False,True,False,False,True,False,False,False,True],[True,False,True,True,True,True,True,True,False,False,True,False,False,False],[True,True,False,True,True,False,False,True,False,False,True,False,True,True],[False,True,False,True,False,True,False,True,True,True,False,True,True,True],[True,True,False,False,True,False,True,False,False,True,False,False,True,True],[True,False,True,True,False,True,True,False,True,True,True,False,True,True],[True,False,True,False,False,True,False,True,True,True,True,False,False,True],[False,False,True,True,False,False,True,False,True,False,False,False,True,True],[False,False,True,True,True,False,True,True,True,True,False,False,False,True],[False,True,True,True,True,False,False,True,False,True,False,True,True,False],[False,True,False,False,True,True,False,False,True,True,True,False,True,True],[False,True,True,True,False,False,False,True,False,False,True,False,False,True],[True,True,True,True,False,True,False,False,False,False,False,True,True,False],[True,False,True,False,False,False,True,False,False,True,False,False,True,True],[False,True,False,False,True,True,True,True,True,True,True,True,True,False],[True,True,False,False,True,True,False,True,False,True,False,False,False,False],[True,False,True,True,True,True,True,False,False,True,False,True,False,True],[True,False,True,False,True,True,False,False,True,True,False,True,False,False],[True,True,False,False,True,True,False,False,False,True,True,False,False,True],[False,True,False,True,True,False,True,False,True,True,False,False,False,False],[True,True,False,True,False,False,True,True,True,True,True,True,True,False],[False,True,True,False,False,False,True,True,False,False,True,True,True,False],[False,False,False,True,True,True,False,True,True,False,False,True,True,True],[False,False,False,False,False,True,False,False,True,True,False,True,True,True],[True,True,True,True,True,False,False,False,True,True,True,False,True,True],[True,False,False,False,True,False,False,True,False,True,True,True,False,True],[True,False,True,False,True,False,True,False,False,True,False,True,False,True],[False,True,False,True,False,False,True,True,True,False,False,True,True,True],[False,True,True,True,True,False,True,False,False,False,False,True,False,False]], dtype = "bool")#candidate|4600|(225, 14)|const|bool
call_4599 = relay.TupleGetItem(func_3190_call(relay.reshape(const_4600.astype('bool'), [15, 15, 14])), 2)
call_4601 = relay.TupleGetItem(func_3192_call(relay.reshape(const_4600.astype('bool'), [15, 15, 14])), 2)
func_1944_call = mod.get_global_var('func_1944')
func_1947_call = mutated_mod.get_global_var('func_1947')
const_4607 = relay.const([[-4.307699,4.389431,6.412724,2.540088,8.916722,-1.538470,6.533465,-4.110606,-6.922509,6.434182,5.828994,6.560002,4.925198,4.396125,7.074662,7.218132,5.897073,-8.122269,-9.506141,-8.025341,-5.866456,5.388371,-8.318248,-1.063827,-4.449806,-3.450277,-6.900777,0.952071,-6.079501,-5.304919,7.274457,-4.244429,-6.336892,2.359346,-3.464344,-8.038332,-0.308075,-5.434909,5.015049,8.720449],[-4.209655,-9.431730,3.169624,9.275784,-7.086525,6.118760,8.507475,-1.184672,6.678983,9.304450,8.235074,-2.159268,5.048806,-2.918591,8.409698,-0.066538,8.298037,7.028531,3.171568,4.113386,-2.892600,4.002671,-0.629609,0.227417,5.252313,5.632141,-5.486086,-6.022025,-2.654970,1.053609,-2.089434,5.453912,-1.201415,9.216389,4.085887,6.922923,2.193209,-7.097913,-7.936007,5.113610]], dtype = "float64")#candidate|4607|(2, 40)|const|float64
call_4606 = relay.TupleGetItem(func_1944_call(relay.reshape(const_4607.astype('float64'), [10, 8, 1])), 0)
call_4608 = relay.TupleGetItem(func_1947_call(relay.reshape(const_4607.astype('float64'), [10, 8, 1])), 0)
func_4506_call = mod.get_global_var('func_4506')
func_4508_call = mutated_mod.get_global_var('func_4508')
call_4611 = relay.TupleGetItem(func_4506_call(), 0)
call_4612 = relay.TupleGetItem(func_4508_call(), 0)
func_3958_call = mod.get_global_var('func_3958')
func_3960_call = mutated_mod.get_global_var('func_3960')
call_4624 = func_3958_call()
call_4625 = func_3958_call()
func_3018_call = mod.get_global_var('func_3018')
func_3019_call = mutated_mod.get_global_var('func_3019')
call_4633 = func_3018_call()
call_4634 = func_3018_call()
func_3340_call = mod.get_global_var('func_3340')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_4638 = relay.TupleGetItem(func_3340_call(), 0)
call_4639 = relay.TupleGetItem(func_3342_call(), 0)
output = relay.Tuple([call_4559,var_4560,const_4561,var_4562,uop_4565,call_4599,const_4600,call_4606,const_4607,call_4611,call_4624,call_4633,call_4638,])
output2 = relay.Tuple([call_4563,var_4560,const_4561,var_4562,uop_4565,call_4601,const_4600,call_4608,const_4607,call_4612,call_4625,call_4634,call_4639,])
func_4640 = relay.Function([var_4560,var_4562,], output)
mod['func_4640'] = func_4640
mod = relay.transform.InferType()(mod)
mutated_mod['func_4640'] = func_4640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4640_call = mutated_mod.get_global_var('func_4640')
var_4642 = relay.var("var_4642", dtype = "float32", shape = (210,))#candidate|4642|(210,)|var|float32
var_4643 = relay.var("var_4643", dtype = "uint16", shape = (286,))#candidate|4643|(286,)|var|uint16
call_4641 = func_4640_call(var_4642,var_4643,)
output = call_4641
func_4644 = relay.Function([var_4642,var_4643,], output)
mutated_mod['func_4644'] = func_4644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4056_call = mod.get_global_var('func_4056')
func_4057_call = mutated_mod.get_global_var('func_4057')
call_4652 = relay.TupleGetItem(func_4056_call(), 3)
call_4653 = relay.TupleGetItem(func_4057_call(), 3)
output = call_4652
output2 = call_4653
func_4655 = relay.Function([], output)
mod['func_4655'] = func_4655
mod = relay.transform.InferType()(mod)
output = func_4655()
func_4656 = relay.Function([], output)
mutated_mod['func_4656'] = func_4656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2629_call = mod.get_global_var('func_2629')
func_2630_call = mutated_mod.get_global_var('func_2630')
call_4775 = relay.TupleGetItem(func_2629_call(), 1)
call_4776 = relay.TupleGetItem(func_2630_call(), 1)
var_4785 = relay.var("var_4785", dtype = "bool", shape = (7, 5, 11))#candidate|4785|(7, 5, 11)|var|bool
bop_4786 = relay.bitwise_or(call_4775.astype('int16'), relay.reshape(var_4785.astype('int16'), relay.shape_of(call_4775))) # shape=(7, 5, 11)
bop_4789 = relay.bitwise_or(call_4776.astype('int16'), relay.reshape(var_4785.astype('int16'), relay.shape_of(call_4776))) # shape=(7, 5, 11)
func_1409_call = mod.get_global_var('func_1409')
func_1410_call = mutated_mod.get_global_var('func_1410')
call_4794 = func_1409_call()
call_4795 = func_1409_call()
func_4411_call = mod.get_global_var('func_4411')
func_4413_call = mutated_mod.get_global_var('func_4413')
call_4797 = func_4411_call()
call_4798 = func_4411_call()
bop_4801 = relay.less(bop_4786.astype('bool'), relay.reshape(var_4785.astype('bool'), relay.shape_of(bop_4786))) # shape=(7, 5, 11)
bop_4804 = relay.less(bop_4789.astype('bool'), relay.reshape(var_4785.astype('bool'), relay.shape_of(bop_4789))) # shape=(7, 5, 11)
output = relay.Tuple([call_4794,call_4797,bop_4801,])
output2 = relay.Tuple([call_4795,call_4798,bop_4804,])
func_4805 = relay.Function([var_4785,], output)
mod['func_4805'] = func_4805
mod = relay.transform.InferType()(mod)
mutated_mod['func_4805'] = func_4805
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4806 = relay.var("var_4806", dtype = "bool", shape = (7, 5, 11))#candidate|4806|(7, 5, 11)|var|bool
func_4805_call = mutated_mod.get_global_var('func_4805')
call_4807 = func_4805_call(var_4806)
output = call_4807
func_4808 = relay.Function([var_4806], output)
mutated_mod['func_4808'] = func_4808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3376_call = mod.get_global_var('func_3376')
func_3378_call = mutated_mod.get_global_var('func_3378')
call_4810 = relay.TupleGetItem(func_3376_call(), 0)
call_4811 = relay.TupleGetItem(func_3378_call(), 0)
var_4841 = relay.var("var_4841", dtype = "float32", shape = (7, 15, 14))#candidate|4841|(7, 15, 14)|var|float32
bop_4842 = relay.less_equal(call_4810.astype('bool'), var_4841.astype('bool')) # shape=(7, 15, 14)
bop_4845 = relay.less_equal(call_4811.astype('bool'), var_4841.astype('bool')) # shape=(7, 15, 14)
func_399_call = mod.get_global_var('func_399')
func_401_call = mutated_mod.get_global_var('func_401')
var_4855 = relay.var("var_4855", dtype = "float32", shape = (72,))#candidate|4855|(72,)|var|float32
call_4854 = relay.TupleGetItem(func_399_call(relay.reshape(var_4855.astype('float32'), [6, 6, 2])), 0)
call_4856 = relay.TupleGetItem(func_401_call(relay.reshape(var_4855.astype('float32'), [6, 6, 2])), 0)
output = relay.Tuple([bop_4842,call_4854,var_4855,])
output2 = relay.Tuple([bop_4845,call_4856,var_4855,])
func_4858 = relay.Function([var_4841,var_4855,], output)
mod['func_4858'] = func_4858
mod = relay.transform.InferType()(mod)
mutated_mod['func_4858'] = func_4858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4858_call = mutated_mod.get_global_var('func_4858')
var_4860 = relay.var("var_4860", dtype = "float32", shape = (7, 15, 14))#candidate|4860|(7, 15, 14)|var|float32
var_4861 = relay.var("var_4861", dtype = "float32", shape = (72,))#candidate|4861|(72,)|var|float32
call_4859 = func_4858_call(var_4860,var_4861,)
output = call_4859
func_4862 = relay.Function([var_4860,var_4861,], output)
mutated_mod['func_4862'] = func_4862
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4896 = relay.var("var_4896", dtype = "float64", shape = (13, 15, 7))#candidate|4896|(13, 15, 7)|var|float64
uop_4897 = relay.asin(var_4896.astype('float64')) # shape=(13, 15, 7)
output = relay.Tuple([uop_4897,])
output2 = relay.Tuple([uop_4897,])
func_4904 = relay.Function([var_4896,], output)
mod['func_4904'] = func_4904
mod = relay.transform.InferType()(mod)
var_4905 = relay.var("var_4905", dtype = "float64", shape = (13, 15, 7))#candidate|4905|(13, 15, 7)|var|float64
output = func_4904(var_4905)
func_4906 = relay.Function([var_4905], output)
mutated_mod['func_4906'] = func_4906
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4919 = relay.const([[[-4],[-6],[5],[9],[-1],[6],[10],[-10],[5],[-7],[-3],[-10],[2],[-5],[-5]],[[-9],[-9],[-7],[-8],[8],[7],[-5],[-5],[8],[-7],[5],[-9],[-10],[2],[-10]],[[-10],[-7],[-5],[-3],[-1],[4],[4],[6],[4],[-9],[10],[-1],[-8],[10],[8]],[[8],[10],[-7],[2],[-7],[1],[-4],[1],[-6],[4],[8],[-9],[3],[-1],[1]],[[6],[9],[9],[-10],[-6],[-5],[-8],[-3],[8],[8],[5],[4],[-4],[-3],[-1]],[[-4],[6],[-2],[9],[-5],[8],[-3],[-8],[7],[-4],[-8],[10],[4],[10],[-7]],[[-2],[7],[-6],[4],[-10],[2],[8],[6],[2],[3],[-10],[-6],[2],[2],[-7]],[[-4],[-4],[8],[1],[-9],[10],[9],[-7],[-5],[-10],[-6],[9],[9],[-1],[-3]],[[2],[9],[8],[7],[-9],[10],[-8],[-9],[-6],[5],[-1],[6],[-4],[-1],[-8]],[[5],[-4],[7],[2],[-1],[2],[2],[2],[6],[-6],[-6],[5],[-8],[7],[-6]],[[-6],[4],[-3],[-1],[-6],[-8],[8],[8],[-3],[-10],[7],[-5],[5],[1],[-3]],[[-6],[6],[-10],[-10],[-6],[5],[-5],[-7],[-3],[-9],[-7],[-8],[-1],[8],[-7]],[[-9],[-1],[-3],[-5],[-1],[-1],[8],[9],[9],[4],[-8],[6],[-7],[-1],[9]]], dtype = "uint16")#candidate|4919|(13, 15, 1)|const|uint16
const_4920 = relay.const([[[10,-2,-6],[8,-2,4],[-5,5,-9],[-3,2,-3],[8,-2,-3],[-4,3,-8],[7,-6,4],[-8,7,2],[2,2,-7],[-3,-8,-2],[3,6,4],[-7,-3,-9],[-5,6,8],[-7,-5,4],[-4,7,-1]],[[-5,-6,2],[-8,-2,-2],[-5,-8,10],[-1,6,-5],[-8,-7,-1],[3,-5,-8],[1,-6,4],[-4,6,2],[-9,10,-6],[8,-4,-8],[-7,10,10],[-9,-1,-3],[-2,5,-10],[3,-7,7],[-7,-9,1]],[[-5,-10,8],[-10,-2,3],[-5,-6,-4],[-7,-8,-9],[-10,-9,7],[-8,-6,-7],[8,-5,-10],[8,3,8],[-10,4,9],[-10,-10,-10],[9,-1,-8],[-3,-8,9],[-7,5,-10],[-9,8,-6],[-7,-8,7]],[[5,-7,5],[7,-2,-6],[-4,7,-7],[2,7,1],[7,-4,-4],[2,-9,6],[-4,1,7],[-8,-4,-10],[-4,-9,2],[-6,8,3],[-1,3,-4],[3,1,6],[3,1,-3],[-8,-5,7],[7,-6,3]],[[8,4,5],[10,8,2],[-1,9,4],[-3,8,9],[5,1,2],[-3,-10,-4],[9,-1,-7],[-10,-9,2],[-3,-6,-5],[6,-3,-5],[1,-7,-9],[3,7,2],[8,4,-2],[-1,-5,6],[3,2,-7]],[[3,7,8],[-1,3,-5],[-1,8,2],[-4,-7,-1],[-1,-2,-2],[-1,8,7],[5,7,5],[4,6,-3],[-6,-1,-8],[-3,-9,-1],[6,8,-4],[-10,-2,-9],[-10,4,9],[-4,4,5],[10,-10,-4]],[[1,-7,-2],[3,-9,10],[3,3,5],[3,-6,-9],[-1,-10,9],[6,-4,1],[3,9,-3],[2,-8,-1],[8,2,-3],[4,9,6],[9,-2,-6],[-8,-8,-1],[-5,-5,9],[-4,2,-10],[9,10,9]],[[10,10,9],[-4,5,4],[-3,10,-10],[5,-3,-1],[3,-6,-2],[1,-2,-1],[-8,-8,6],[-10,8,8],[8,-3,-2],[3,-6,10],[-5,9,5],[8,6,-8],[-7,3,10],[-5,-7,-1],[-3,-6,-5]],[[-9,9,-8],[8,10,2],[-8,8,-6],[5,9,2],[-2,-4,5],[7,8,10],[2,1,-3],[10,6,5],[8,-5,-9],[-7,-1,-1],[10,8,6],[5,-7,-10],[3,-4,-9],[1,6,-6],[-3,7,-6]],[[10,-6,6],[-8,10,9],[-10,1,1],[2,9,10],[-4,-2,8],[-9,6,9],[-9,-4,4],[8,-6,-7],[-9,9,-6],[5,3,-3],[7,-9,9],[-6,-7,-7],[4,7,2],[-6,-5,-1],[5,3,5]],[[-9,9,-5],[8,-9,2],[7,9,5],[-10,-4,-8],[-7,1,1],[5,-8,9],[-5,7,-1],[-7,-6,-4],[10,3,-10],[9,6,-7],[-7,8,-9],[1,4,-5],[8,5,10],[4,-5,4],[-10,3,6]],[[-4,2,-6],[-10,4,-4],[1,1,-5],[-5,-1,-8],[4,-9,-3],[-6,-7,10],[1,2,-4],[-2,-10,10],[4,-4,6],[9,1,6],[4,-2,2],[4,-4,7],[-5,-2,2],[8,-7,-10],[-6,2,8]],[[1,2,2],[-7,-7,5],[8,3,-2],[-4,-2,5],[-6,10,8],[10,1,-5],[5,-1,5],[-6,-3,5],[-7,-8,-3],[-10,3,1],[-1,3,2],[-5,1,1],[10,-1,8],[10,8,-6],[-10,4,-8]]], dtype = "uint16")#candidate|4920|(13, 15, 3)|const|uint16
bop_4921 = relay.minimum(const_4919.astype('uint16'), const_4920.astype('uint16')) # shape=(13, 15, 3)
func_2548_call = mod.get_global_var('func_2548')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_4927 = func_2548_call()
call_4928 = func_2548_call()
const_4932 = relay.const([[[3.487907,3.821032,-2.800630,-5.930412,5.525802,-1.802788,1.178551,-0.941022,4.233163,2.397050,2.654446,7.878397,6.348840],[-9.859675,-7.710451,9.556513,4.888207,-6.349638,5.931384,-6.173357,9.631499,-1.810042,2.226544,-4.467740,0.205725,-7.634860],[6.523536,-3.097098,-6.945390,-5.752492,-9.165050,-7.528370,-8.917723,0.982940,-4.308257,-0.892678,-5.618363,-7.500864,4.724285],[-4.706922,4.541829,-4.066259,-4.139278,1.784448,5.869851,4.695652,6.374793,-6.868367,8.789017,4.640257,2.924842,1.459552],[5.794826,-3.258619,-5.625218,8.941538,6.215352,-2.231402,-9.377420,-7.002684,2.536186,9.158359,-6.679985,6.124374,2.037938],[0.604483,-0.650004,-9.255702,-9.360409,3.710491,-8.585955,-9.547814,-1.039961,5.421406,-2.931156,-2.890130,-6.247540,7.764610],[5.991151,-5.553494,0.670887,-8.677288,-6.831580,8.495862,9.964767,0.814144,1.539943,8.245086,-1.143281,-4.816107,8.113033],[7.404991,-5.742521,-3.379387,6.343204,-9.942419,-1.217075,-4.464025,-2.578677,1.304121,-3.409268,0.754411,3.667865,6.369333],[7.244062,-2.213213,6.875792,-5.493969,-4.605696,7.497381,7.376107,2.961112,-4.820921,-7.645301,1.116839,-9.898566,-4.778124],[-5.937337,0.942584,-4.973656,6.296574,0.300314,-9.281339,8.037122,-0.261545,-4.341638,-0.621733,2.458782,6.580821,8.971335],[5.593898,4.889972,7.207516,9.301280,2.871901,-6.869106,9.217281,8.078086,2.809886,-2.903350,-5.444770,-6.872047,-5.856291],[1.089094,3.936902,5.181101,0.752434,5.492734,-4.130244,4.700679,-9.797256,-3.695199,2.273835,3.282947,-3.540444,-8.246887],[-5.988056,-8.831313,-8.866899,-2.772340,-2.576117,-8.497872,-3.677892,3.764276,9.629253,1.244351,-7.355210,9.859138,2.667235],[-4.214046,-2.437388,-7.785857,6.848937,-6.759653,6.004561,-2.285677,-2.975638,8.758176,-2.829477,3.861624,9.789697,0.702963],[-8.976727,1.058541,7.062857,-7.236756,-0.419031,-1.009749,1.971777,7.687854,2.136326,-2.552091,-5.004808,6.443129,-9.841930]],[[-0.924146,3.727737,1.722871,-6.652775,0.138099,8.991730,-5.814684,0.170899,3.133494,3.978643,6.111548,-2.568123,-1.707726],[2.426367,9.017901,-7.744232,7.840250,4.314432,8.463055,7.783568,9.506888,-1.754019,-5.335352,-5.159821,-0.730850,-6.442134],[5.703840,-5.630309,2.637230,2.102281,6.412381,2.824184,6.442471,-7.439375,-3.293562,2.300710,-6.396102,3.832502,0.576733],[-1.937984,7.015601,6.581319,-8.232221,-5.328104,3.078518,-5.270886,8.633469,7.255274,7.340662,-8.358394,0.680276,4.299643],[2.155130,-7.907252,9.501576,5.981274,0.569086,2.185793,-7.606420,-6.884691,9.219789,-6.656100,-5.492376,8.675008,9.031552],[2.255573,8.473518,-0.446336,-1.030121,-9.196727,-2.144186,-0.872722,-1.743903,5.502339,-3.722198,2.338864,-5.759960,-4.357685],[9.321499,-3.276539,2.029210,-2.881785,9.920368,-9.581861,6.612108,1.894303,-1.345294,-2.871769,6.844292,7.000749,6.410894],[3.449786,-4.355282,-1.009787,7.143640,7.173992,-6.571021,8.212454,-4.022094,6.542982,-9.122297,8.508810,7.382958,-3.486901],[1.346511,-3.019660,-1.863469,8.170832,0.074724,-5.204145,-1.225126,-3.443814,2.708315,-5.729734,2.543107,-4.607284,-2.887332],[-8.630844,2.664903,-2.639440,-3.479765,1.554561,-2.311755,5.279385,-9.477715,-7.100434,7.505788,4.906046,2.552474,7.764469],[-9.397721,-1.552693,6.370688,-1.969415,8.825712,-0.092293,2.629254,-5.457525,-9.879602,0.564058,-3.642069,0.464088,-5.456420],[-7.098399,2.121514,-6.249251,7.994045,-1.276779,2.444411,1.423669,-7.705748,-3.764905,7.717110,8.101388,5.421497,-2.986288],[9.278392,8.958277,7.659799,0.621330,9.324243,-4.964117,-0.313211,-7.327870,5.317156,4.349347,8.707799,6.068578,-4.548342],[-2.547525,0.882411,2.812681,-5.048839,7.924080,7.337211,-4.954486,-7.685774,4.757636,-9.287471,1.375250,-1.340280,1.879089],[-5.043943,-9.356489,5.982517,-4.469985,-6.639738,2.212449,7.785886,-0.547514,9.688110,4.858174,2.475333,5.999220,-2.807632]],[[7.680071,3.105252,-6.642218,4.297081,-5.603147,8.678791,6.754562,8.360927,5.563655,3.105918,9.917420,-6.309902,3.829904],[9.470934,9.600424,0.626123,-6.903158,1.335113,-8.321178,-2.921308,-4.254020,-8.820872,0.038179,-6.033761,-4.093343,-8.468852],[3.070022,-0.115625,-4.035820,5.220699,-3.176914,-2.180409,2.712026,2.591205,-1.735808,-6.448383,-4.115133,-9.309355,-1.607982],[-5.818091,0.089591,-8.458397,3.388074,1.036386,0.758624,-8.857123,5.108954,-0.998723,-7.755338,-0.852125,6.516727,3.748384],[5.874381,7.245506,6.879386,-1.996239,-0.695872,8.350074,-7.011353,9.902226,8.748229,7.625016,-0.182661,7.177233,4.637603],[6.466805,-5.403306,-1.689785,2.616917,-3.180708,4.504099,3.984063,7.390416,-6.358919,3.316178,7.686494,6.627141,6.637612],[6.751685,-9.211073,-0.104230,5.121009,0.603964,5.360615,-1.154908,7.348632,-7.040869,5.421771,4.865174,8.889335,-6.203316],[4.729282,5.769404,0.033896,7.821690,-1.916726,-0.575032,-3.816297,7.185301,-9.565794,9.977115,-3.170330,-1.137574,-1.359413],[2.294787,-4.187649,-8.378572,2.505306,-8.828077,-4.412037,-4.024776,9.361394,5.776089,-0.664805,1.673370,-1.077532,-7.214710],[7.634137,-4.896641,-5.775700,3.658860,9.449385,-6.164892,-0.573825,-6.800076,-9.410459,2.986122,0.370897,-7.717916,8.202484],[-8.937165,-7.841177,-9.889896,4.307044,7.599235,-2.537090,-0.040714,4.305776,-7.283737,2.736739,-8.555539,-1.792196,0.829247],[-0.894224,2.680502,-7.738042,9.511085,2.847910,-3.505471,9.654034,-2.130529,-2.727656,7.275149,-0.230232,9.666662,-9.401300],[1.912219,3.141525,-1.595188,-1.840043,-9.449370,9.452538,-5.109445,8.316450,0.645081,-0.903329,5.880858,-9.947103,-3.297438],[-8.021235,-8.958325,-6.740715,9.182929,3.556016,4.708342,-1.255668,-8.443910,-6.426838,-2.073370,9.713452,-5.028945,3.845828],[-3.127462,-6.454907,-1.172390,3.064842,-6.997609,4.659682,9.048627,7.979909,-4.984763,-5.663865,-9.286177,8.967624,5.713345]],[[-0.914728,7.167791,3.851166,-2.664815,-8.011267,-1.337489,9.659563,4.378571,0.387659,1.234302,-7.216026,-3.055160,-6.341967],[4.400348,8.300896,-9.890650,-7.385940,5.641674,-1.132892,1.062373,5.513221,-1.175495,-7.162585,0.393985,-5.150320,5.395367],[-2.922739,-6.930626,-7.216027,2.051005,-3.019675,8.880058,0.506704,-1.049819,-0.538356,-9.967042,9.216537,8.981249,4.350968],[3.024279,3.280703,-9.017810,-3.876150,8.346137,-1.324746,-5.722007,-0.317924,4.857826,5.930532,3.800605,8.871446,0.036615],[-3.468125,7.329268,9.741994,-6.688029,7.614066,-7.749029,9.048970,-8.183549,-0.093075,-1.604826,-3.919193,-0.494096,6.059993],[-8.715922,-4.456114,3.998518,-2.228345,-3.325234,-5.098225,-7.331927,3.016144,3.106929,-0.616838,-6.741251,5.367157,-4.837777],[-4.812827,3.873054,-9.136989,-2.140143,1.868673,-1.933600,-2.936711,0.121384,3.887919,-8.727900,-6.617859,1.715848,7.380994],[-1.606376,-5.955575,4.655805,1.052740,-0.155995,-8.864085,-2.490678,-1.647067,8.168252,5.602593,1.781553,-6.511508,2.696063],[-9.980588,-0.278083,-8.714264,-9.823591,9.485629,1.427795,-0.619452,-7.544058,8.477168,-4.752875,9.440877,-5.849895,-2.600185],[2.671863,-2.121084,8.051559,9.943345,-9.708617,-6.460486,-1.647201,-4.317131,4.231535,2.692473,9.295275,-3.781340,6.822811],[7.749837,9.725158,2.952797,8.321255,3.217906,-5.693969,-1.252961,5.720570,0.257527,-2.580307,4.518397,-4.485785,2.274521],[5.040595,1.371524,-8.069940,7.069278,-1.218144,-1.391335,-0.575531,5.052329,1.559900,2.426580,-9.703765,-1.531857,3.422244],[-8.671669,6.532866,9.297849,-8.662549,9.362681,-1.744428,-1.295751,2.335342,-4.274493,-7.809482,5.273793,7.188244,-5.426021],[6.943747,-7.927746,3.856582,0.550484,-2.973140,7.244089,8.783026,1.356853,6.304127,0.718792,2.267126,-9.205945,5.722468],[0.050474,2.813595,-5.133361,-0.640354,5.794416,-8.786674,-7.087422,0.981965,9.354322,-5.727658,-8.750561,-6.724274,5.149756]],[[2.318540,0.761804,2.233778,9.327847,6.640270,8.079683,-6.757036,7.605995,2.328297,-3.989687,6.643539,-3.803473,-0.948093],[-8.504978,-3.695144,-3.224728,6.596702,-1.723938,-9.398527,1.061658,8.967670,-8.198438,7.654342,-7.311632,0.542018,-2.996080],[-2.456615,7.963964,4.969351,9.114325,1.299260,-9.485855,-2.819413,3.350660,-4.282463,-6.739954,2.709188,-5.913690,-2.203308],[-3.554708,5.690852,-6.353952,5.527116,-6.589604,6.384053,-5.926320,-2.802801,-9.983890,0.344149,9.032495,-1.128242,9.161074],[-6.399250,0.863071,1.440351,7.955505,-3.698829,-9.038670,1.829455,-0.213500,3.996248,7.361122,6.726920,-5.123664,9.851773],[6.609121,4.825204,6.973325,-2.003221,-1.458925,-4.420845,-3.273251,6.310287,-2.519457,0.087985,-4.790573,4.733159,-1.389196],[5.614781,3.612551,2.641027,-9.490876,-2.701056,-9.784178,-4.004802,-6.187509,-6.223207,2.499666,7.653471,-2.471147,7.952097],[8.768481,-1.441175,8.336733,-1.161077,-6.975354,5.011682,-9.413405,4.994358,-9.875930,0.564729,-0.690092,2.594707,-2.787279],[-8.845207,-2.521133,2.256180,-4.940452,2.840891,8.241660,1.332608,7.907196,-6.486279,-5.650373,7.142330,-9.164622,0.286857],[-0.282419,-2.579940,4.884150,-0.720335,-9.897805,-1.913111,8.591713,2.273767,4.284961,0.786957,3.806097,6.873663,0.700597],[7.387152,3.761861,-5.014874,6.845463,-7.764703,0.049081,-8.271554,-7.402748,3.363886,4.475046,-8.695807,3.259886,3.355879],[-1.434760,-2.439883,7.051946,9.754840,-4.364698,0.354917,-4.372991,-8.781768,-1.500535,-0.884176,3.694307,-5.959168,-7.187751],[-3.675540,-7.277120,-9.104099,-0.377070,-8.844031,-8.881429,-8.723204,-5.990166,6.954890,-0.411615,-4.744999,-9.353302,6.066811],[-9.409823,-3.725830,1.722452,-0.320147,4.610193,-2.484889,4.139044,6.335827,-3.961304,-0.193486,0.490264,1.896604,-3.041397],[-3.409587,-4.206366,-0.021931,-9.738495,2.429307,6.893745,0.786263,8.280610,-4.588634,7.718592,-0.886883,-6.411037,-2.378790]],[[-5.011498,1.723317,5.329792,-2.531152,8.857413,9.353331,9.830780,1.065248,-5.410110,5.743722,-0.183406,9.442696,-0.828971],[9.313242,-9.233592,-9.721167,-9.608183,1.892752,-7.615701,6.119181,8.583498,0.891734,-0.830153,1.614866,4.442085,-5.926431],[8.538680,2.287749,4.384143,-1.966777,-7.844226,9.734290,-7.893730,0.934144,-2.109927,-0.285969,2.505426,-5.126967,0.445622],[-0.975945,5.289278,-0.276321,-0.387013,-4.998785,1.888870,-6.622320,2.429238,-5.324425,-4.593966,-4.897954,-6.291277,-8.795912],[-9.994934,3.484377,9.127299,4.593745,-3.189020,4.620525,1.180242,9.195414,-8.099472,0.312963,6.057011,2.803114,2.693124],[-8.591133,-5.873939,4.290878,7.379579,-6.181177,-1.767467,0.582544,-0.305720,-7.233797,-7.410273,-7.754545,5.884691,9.059064],[2.923839,-4.689091,-8.134704,-5.118836,-8.866060,-3.019076,7.457963,-5.212332,-6.011205,-2.008917,-0.638919,-2.054424,-7.046677],[9.786721,-2.466456,-9.852765,1.246845,-2.227516,6.726878,-7.328929,-9.859258,-8.750452,-7.509688,-6.311291,-4.727549,6.172168],[5.178490,-4.505364,-5.979989,3.077402,-3.050437,-2.118147,-8.436708,8.048719,5.733096,3.491868,-9.836240,1.132790,-3.597773],[3.624379,1.071768,4.000746,2.631058,-1.462194,3.751434,-8.427326,-8.391615,5.132908,-5.202061,-6.801691,2.441015,8.214804],[8.527967,-3.048117,-4.375907,1.217211,-2.640121,-8.423897,-7.389415,4.084551,-7.740419,0.313204,-4.939042,-5.442748,7.204017],[-0.074557,-6.352004,8.844771,7.969000,-5.989998,1.260576,3.607568,-5.518730,8.143782,-6.598917,9.427873,6.905291,7.338702],[1.984799,-0.876691,3.086367,6.509040,-7.820421,6.568079,-3.017145,-9.226796,6.091991,2.061294,5.148442,-2.959686,9.187478],[7.370274,-6.458962,-7.044424,-0.194033,0.561380,-0.716994,8.283098,2.842109,-6.876763,-8.010991,9.708389,-5.204908,-8.466732],[-8.963236,7.718424,-8.460138,-6.994594,-0.620599,-5.516498,6.084087,-2.136593,6.208778,-5.636569,-8.304424,-3.234501,3.960430]],[[8.534737,9.945826,-5.575819,-4.665800,5.951088,-1.887294,-0.375144,9.350184,2.623204,-6.403171,-6.986559,6.901060,-7.132229],[2.198068,6.630878,-3.248766,-8.355427,-7.312549,6.068525,-0.388427,8.060662,-3.864106,6.847258,-4.561341,-3.423634,-2.144292],[-4.684227,-8.761532,-3.622206,-1.476444,-7.585984,-7.792751,-3.569978,7.478976,1.570687,-2.087992,-5.737252,-5.924905,-4.512976],[-2.051951,0.382861,6.679269,0.535577,-4.746883,0.233087,5.412771,-8.245188,-3.777243,-0.409056,-8.352925,-1.603659,-8.558034],[-7.024510,-8.693549,5.842865,7.248546,-1.947095,3.130108,-4.614514,1.193411,-9.248147,-6.666027,-7.821857,5.174344,-3.231618],[-5.586255,-9.503158,-2.763067,-7.840131,-7.668229,7.298532,-9.642297,-2.010884,6.013048,-0.871081,6.642042,8.043376,8.019325],[-9.972768,-2.420763,-8.510758,1.911846,4.065502,8.797345,2.579464,-1.300462,-5.007270,-3.018259,-5.362067,4.604597,-8.012308],[6.180801,-6.083557,5.095305,1.021900,-9.930450,-8.201914,-2.575646,5.013985,5.105227,8.195930,3.321104,1.881363,4.760699],[-7.026472,-2.815395,4.674462,-4.114168,-0.838631,-5.389731,-7.576155,2.587497,1.027156,-0.922879,-9.198837,1.750412,9.383181],[5.247932,-9.231207,-6.479616,1.806124,0.821923,-9.077498,0.502408,8.576483,-7.350985,-8.845955,-5.574785,-7.028573,-7.295126],[9.070861,-8.234737,-3.476871,8.166176,-1.109875,4.604345,-1.718500,-5.164944,6.913343,8.472820,-1.262750,-7.814903,7.232500],[-4.862355,6.098893,-5.721352,-8.220557,-9.024354,-3.674212,6.521425,2.009007,3.217860,7.545786,3.594136,5.043652,8.886737],[-5.575809,-6.928415,-0.101860,3.453706,4.389061,-2.488514,2.839923,-5.752709,-9.136962,-5.432770,5.217489,9.359391,-9.917222],[1.677098,8.183700,7.270108,-7.556203,-7.547312,-7.142243,-3.935487,2.665750,5.202730,2.552102,8.083482,6.158945,-8.059132],[5.196730,2.612158,-3.545086,4.612989,5.167013,0.359991,-6.328308,-4.502153,-9.903375,-3.257104,-6.979527,-5.409924,3.376619]]], dtype = "float32")#candidate|4932|(7, 15, 13)|const|float32
bop_4933 = relay.bitwise_xor(call_4927.astype('uint8'), const_4932.astype('uint8')) # shape=(7, 15, 13)
bop_4936 = relay.bitwise_xor(call_4928.astype('uint8'), const_4932.astype('uint8')) # shape=(7, 15, 13)
uop_4937 = relay.exp(const_4920.astype('float64')) # shape=(13, 15, 3)
output = relay.Tuple([bop_4921,bop_4933,uop_4937,])
output2 = relay.Tuple([bop_4921,bop_4936,uop_4937,])
func_4944 = relay.Function([], output)
mod['func_4944'] = func_4944
mod = relay.transform.InferType()(mod)
output = func_4944()
func_4945 = relay.Function([], output)
mutated_mod['func_4945'] = func_4945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_4970 = relay.TupleGetItem(func_3457_call(), 1)
call_4971 = relay.TupleGetItem(func_3459_call(), 1)
func_3693_call = mod.get_global_var('func_3693')
func_3694_call = mutated_mod.get_global_var('func_3694')
call_4977 = relay.TupleGetItem(func_3693_call(), 0)
call_4978 = relay.TupleGetItem(func_3694_call(), 0)
uop_4983 = relay.tan(call_4970.astype('float64')) # shape=(7, 15, 1)
uop_4985 = relay.tan(call_4971.astype('float64')) # shape=(7, 15, 1)
output = relay.Tuple([call_4977,uop_4983,])
output2 = relay.Tuple([call_4978,uop_4985,])
func_4993 = relay.Function([], output)
mod['func_4993'] = func_4993
mod = relay.transform.InferType()(mod)
output = func_4993()
func_4994 = relay.Function([], output)
mutated_mod['func_4994'] = func_4994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2175_call = mod.get_global_var('func_2175')
func_2176_call = mutated_mod.get_global_var('func_2176')
call_5016 = relay.TupleGetItem(func_2175_call(), 0)
call_5017 = relay.TupleGetItem(func_2176_call(), 0)
var_5026 = relay.var("var_5026", dtype = "float64", shape = (7, 15, 2))#candidate|5026|(7, 15, 2)|var|float64
bop_5027 = relay.power(call_5016.astype('float64'), var_5026.astype('float64')) # shape=(7, 15, 2)
bop_5030 = relay.power(call_5017.astype('float64'), var_5026.astype('float64')) # shape=(7, 15, 2)
func_4067_call = mod.get_global_var('func_4067')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_5039 = func_4067_call()
call_5040 = func_4067_call()
var_5044 = relay.var("var_5044", dtype = "float64", shape = (7, 15, 2))#candidate|5044|(7, 15, 2)|var|float64
bop_5045 = relay.floor_mod(var_5026.astype('float64'), relay.reshape(var_5044.astype('float64'), relay.shape_of(var_5026))) # shape=(7, 15, 2)
func_4944_call = mod.get_global_var('func_4944')
func_4945_call = mutated_mod.get_global_var('func_4945')
call_5063 = relay.TupleGetItem(func_4944_call(), 0)
call_5064 = relay.TupleGetItem(func_4945_call(), 0)
output = relay.Tuple([bop_5027,call_5039,bop_5045,call_5063,])
output2 = relay.Tuple([bop_5030,call_5040,bop_5045,call_5064,])
func_5070 = relay.Function([var_5026,var_5044,], output)
mod['func_5070'] = func_5070
mod = relay.transform.InferType()(mod)
mutated_mod['func_5070'] = func_5070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5070_call = mutated_mod.get_global_var('func_5070')
var_5072 = relay.var("var_5072", dtype = "float64", shape = (7, 15, 2))#candidate|5072|(7, 15, 2)|var|float64
var_5073 = relay.var("var_5073", dtype = "float64", shape = (7, 15, 2))#candidate|5073|(7, 15, 2)|var|float64
call_5071 = func_5070_call(var_5072,var_5073,)
output = call_5071
func_5074 = relay.Function([var_5072,var_5073,], output)
mutated_mod['func_5074'] = func_5074
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5084 = relay.var("var_5084", dtype = "uint64", shape = (15, 6, 9))#candidate|5084|(15, 6, 9)|var|uint64
const_5085 = relay.const([[[6,8,-6,8,-10,2,-5,-7,7],[-5,-10,-1,-1,-4,2,1,-1,-8],[1,2,-7,1,1,9,1,2,2],[-2,2,-3,4,-2,2,4,6,-5],[10,4,-1,-1,8,6,9,-2,3],[-5,9,4,5,-7,5,3,5,7]],[[4,-10,3,2,-5,-5,10,-5,-5],[-2,-10,3,-10,-1,6,5,-7,-4],[-3,2,-1,-6,7,1,2,-2,4],[-10,-2,1,10,-1,1,9,10,-1],[10,-1,9,-9,-7,7,-6,6,-7],[-9,-3,6,-4,9,8,-4,-9,5]],[[6,1,3,-5,-5,9,7,9,-8],[5,1,5,-6,-8,-3,3,7,5],[1,10,-10,-8,-9,-9,3,9,8],[7,-5,8,-8,-9,4,4,3,-3],[-5,2,-7,2,-4,6,-7,7,8],[9,-8,-2,2,2,-3,10,4,-1]],[[2,-3,-4,-2,3,-2,7,-10,10],[9,-9,-9,4,10,1,10,-7,-4],[3,-2,5,9,5,-9,1,-7,9],[-5,-5,-4,8,-2,9,8,1,-10],[5,-10,-7,3,7,8,-6,-2,10],[9,-9,3,-8,2,2,-4,9,5]],[[-3,4,10,7,-7,-1,4,-4,-3],[-5,-9,-8,8,8,-8,-5,-3,10],[-5,1,7,-8,2,-7,1,3,8],[-1,-5,-6,-1,-3,-4,-8,-3,10],[1,-2,9,7,1,8,-3,-6,9],[3,-4,4,3,-6,3,8,-3,-8]],[[-10,-10,6,8,8,-10,-7,7,-3],[-9,5,5,-1,-3,-3,-5,-5,-2],[7,-10,6,-4,-7,6,3,6,-3],[7,4,-8,-2,-10,10,-10,3,-3],[-2,-4,9,-8,-7,10,7,-2,9],[10,5,-10,1,3,10,5,-5,2]],[[10,6,-6,5,-6,-6,9,8,-3],[10,-8,10,-10,-1,-5,-1,-5,-10],[3,-6,-6,-4,8,10,10,-9,-4],[-8,3,3,4,-1,-9,2,10,-1],[-10,-1,6,-4,-3,7,-10,-6,-4],[-1,1,9,-4,-3,7,-1,8,-9]],[[-7,-3,6,10,6,-10,-4,-1,2],[-6,9,3,3,6,9,-8,-10,7],[-2,3,4,8,-6,-3,-9,9,8],[5,-7,3,-8,-2,-3,-6,7,-4],[-5,-1,3,1,4,-9,1,4,-7],[-4,7,3,7,6,9,7,2,6]],[[3,-7,-7,-9,-2,-6,9,6,-6],[-5,-8,-6,-1,-2,-2,-8,6,-2],[-4,1,4,-7,-5,-9,1,3,5],[10,-4,-8,-1,-3,-4,1,-6,5],[8,-4,-4,4,-7,7,-8,-7,-9],[1,3,-8,7,-4,2,6,1,2]],[[1,3,5,-1,6,7,4,7,10],[-4,-7,-3,-10,-8,8,-6,-10,-8],[-8,-9,-6,-10,-4,8,4,-2,-2],[9,-3,5,-1,-10,-10,3,7,2],[8,-6,1,-6,-7,6,-3,-3,6],[-6,9,-5,6,8,-1,1,-4,-4]],[[10,-2,8,8,4,6,9,6,-1],[6,-2,3,5,-5,-10,6,10,-8],[-5,-10,10,-1,-9,5,-2,9,5],[7,5,-9,-2,-4,-10,-1,-1,-5],[8,-7,5,-8,5,8,7,-10,-9],[7,3,-6,-4,-1,9,-3,2,-5]],[[-4,-3,-10,8,8,2,-8,-3,-10],[7,9,10,-2,6,-5,-2,-3,7],[-7,3,-5,-5,5,6,-8,-9,9],[-4,4,-6,10,-7,2,-8,-1,6],[-7,-10,10,6,-1,6,6,-2,9],[-9,-5,-4,2,-7,3,10,-4,-10]],[[8,-4,-5,-8,10,1,-7,2,7],[-2,8,-2,1,-10,-2,-1,10,-9],[8,6,-7,-1,7,8,-7,-5,-10],[-5,8,-7,-8,3,8,3,-9,-3],[-5,-3,-6,-10,-3,-10,-1,3,-4],[2,-3,-2,-8,6,-3,6,-3,-2]],[[-1,-4,5,-7,-2,-6,5,8,4],[8,2,-9,-2,3,-5,-4,5,-1],[5,9,-10,-2,2,2,8,7,-3],[7,1,-1,-4,3,5,2,-1,7],[-5,-6,-9,-4,-8,8,-9,-7,4],[-9,4,-10,7,1,4,-1,7,7]],[[-6,2,5,-7,3,-7,3,5,-9],[8,-6,5,-7,10,-6,9,-1,-7],[-8,-1,10,8,-3,3,-8,7,10],[-6,8,2,-3,5,-3,-8,-7,-4],[6,-2,-6,2,-6,8,9,-6,9],[1,10,-6,10,-3,-5,-4,8,-2]]], dtype = "uint64")#candidate|5085|(15, 6, 9)|const|uint64
bop_5086 = relay.left_shift(var_5084.astype('uint64'), relay.reshape(const_5085.astype('uint64'), relay.shape_of(var_5084))) # shape=(15, 6, 9)
output = relay.Tuple([bop_5086,])
output2 = relay.Tuple([bop_5086,])
func_5096 = relay.Function([var_5084,], output)
mod['func_5096'] = func_5096
mod = relay.transform.InferType()(mod)
mutated_mod['func_5096'] = func_5096
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5097 = relay.var("var_5097", dtype = "uint64", shape = (15, 6, 9))#candidate|5097|(15, 6, 9)|var|uint64
func_5096_call = mutated_mod.get_global_var('func_5096')
call_5098 = func_5096_call(var_5097)
output = call_5098
func_5099 = relay.Function([var_5097], output)
mutated_mod['func_5099'] = func_5099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2242_call = mod.get_global_var('func_2242')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_5107 = func_2242_call()
call_5108 = func_2242_call()
func_2836_call = mod.get_global_var('func_2836')
func_2840_call = mutated_mod.get_global_var('func_2840')
const_5116 = relay.const([-10,5,-8,10,-9,8,-3,-1,-3,7,7,8,-10,-3,-1,-8,9,6,4,-7,-2,-7,6,-7,4,-10,1,6,9,4,6,-10,3,2,2,10,-6,1,6,-2,4,-9,4,-6,9,-2,2,-9,9,-4,-3,-7,3,5,-7,-10,-1,-8,8,-7,-6,9,-2,-4,-2,-2,-5,5,6,-9,-7,6,10,2,-7,-3,7,-10,-10,9,-5,6,9,-9,-1,2,7,-7,-1,3,7,1,-7,2,7,9,2,5,-7,8,3,8,-7,5,4,-6,-3,7,-9,-7,-2,-10,4,-6,10,-10,2,-10,-5,-7,-4,-1,9,7,9,-6,-2,3,-4,8,-3,-6,8,-5,3,-1,-4,-4,-2,-3,-6,-2,-9,-6,-6,-8,3,-5,2,-4,-2,3,-9,9,9,4,2,6,3,-6,-6,-9,8,10,3,-6,8,1,6,1,-5,-5,-1,10,-2,-2,-1,-7,-4,-9,-10,-4,-2,-8,-8,-8,-3,9,1,-7,-6,-3,-9,-3,9,2,5,-10,2,9,-8,-10,-7,7,8,5,3,8,10,5,-5,9,-4,9,6,5,-5,4,-5,2,-5,9,4,-9,1,4,-2,6,-9,-1,4,-10,2,3,-7,3,1,-9,9,9,-4,6,3,10,-8,10,9,-1,6,-8,-6,-4,-3,1,-2,2,3,-2,9,-2,-4,-6,-4,2,10,2,3,4,2,-5,-8,-10,4,-9,5,7,6,10,2,-8,4,-10,-8,2,-2,4,-6,2,8,3,7,-1,-5,10,5,-2,2,7,-6,1,7,-1,10,1,7,1,3,-6,3,8,8,10,-1,9,7,7,-5,-5,2,-5,1,4,8,-6,5,-10,1,-2,-8,-10,-1,8,-7,-3,2,-9,-3,-9,-2,3,-9,2,-4,2,5,6,-1,6,-1,9,8,-6,-3,-2,-2,-4,-8,2,-3,4,8,-8,8,9,2,3,-7,10,8,7,-9,-2,9,10,8,-2,6,5,1,-3,1,-4,5,-8,-10,-2,6,-7,-7,9,-1,-2,-8,-10,9,3,-7,6,-2,6,9,-8,-3,-2,-2,-6,9,-9,-4,-7,2,3,-6,3,5,-10,9,-9,-5,-3,-9,9,8,6,-6,-5,4,8,-6,10,2,6,-9,2,-4,-10,-5,-5,-8,-6,-6,3,-8,-10,5,6,9,7,-6,2,5,7,3,-4,2,7,1,-8,2,3,-7,3,10,-3,-10,-8,-9,4,6,-4,9,8,1,7,3,1,9,-5,-5,-7,7,9,-2,-9,2,-9,-3,1,3,9,9,6,-7,9,3,-6,-5,6,9,-8,-7,4,-3,5,-6,-4,6,3,4,5,1,-8,8,4,9,2,8,-7,-2,9,-9,-3,4,8,1,5,-7,-8,9,4,-5,-6,-2,-8,-7,2,-9,-3,-4,-2,4,-9,-10,-6,1,7,-6,-3,-5,-3,-7,10,-4,2,4,5,9,9,-10,-8,-6,-1,7,-1,4,-7,-2,8,10,6,-1,-1,4,2,6,-7,7,5,3,-8,-1,-9,-2,9,-6,-3,5,-1,-6,4,-5,4,-10,-9,4,-7,2,8,-4,3,3,9,2,10,5,1,5,-5,2,-6,-9,1,-1,-3,-7,5,4,1,-5,7,-3,1,2,2,10,-10,3,2,2,6,-4,1,-6,6,-3,3,-1,-3,2,7,-3,3,-2,-9,2,6,-8,-6,1,-8,-6,10,9,10,-9,5,6,10,-5,-2,6,-3,-7,1,-2,10,-1,-3,4,-4,-10,6,7,4,5,-10,-4,-5,1,-6,-6,1,7,-8,9,5,-10,-5,-9,10,-5,-4,5,-7,-9,9,1,3,-6,-2,-4,4,10,-3,-10,-2,5,-3,9,-7,5,2,-8,6,7,-10,-5,-6,-6,3,-4,-1,10,9,6,-6,4,6,4,-7,-2,-1,-3,-1,6,5,6,8,1,-7,-5,-7,2,2,-9,-6,-8,-5,6,10,-7,-1,-2,-3,8,2,-3,-2,-4,3,-5,-2,8,4,5,-7,8,9,8,-4,2,-10,5,-1,8,2,-3,-6,6,-8,-3,-5,-4,4,-4,10,4,-10,2,10,5,3,10,10,9,-9,2,5,8,-8,10,8,-8,5,-2,-1,-8,-5,-4,-6,-3,-7,-7,-1,-4,7,8,7,8,7,-6,-6,-1,-3,-8,-9,-2,-7,1,-5,-8,-8,-10,2,5,-7,-8,-5,6,5,7,-8,-10,-9,3,-5,-6,7,8,-3,9,-5,-3,-7,10,-4,5,7,4,-8,2,10,-8,4,-6,-8,7,3,6,8,1,-5,3,-4,2,6,7,3,-10,-9,6,-3,-5,-10,6,8,-1,6,5,-10,3,-10,-9,4,-10,8,-4,-8,7,9,7,3,-10,-1,-8,-3,-7,1,-6,7,-10,3,-6,-3,10,-10,-7,6,-9,-4,7,8,-10,10,-4,3,2,9,10,4,-4,-8,7,-10,-2,5,-10,3,-4,6,-2,3,9,-3,-4,1,-3,-8,-5,-7,1,-8,7,-10,6,10,-5,3,4,4,-5,5,2,-8,-2,-5,9,3,-7,-6,9,1,8,9,-10,-10,-6,4,-8,8,-7,4,-6,-1,-10,-6,-10,4,-2,10,5,-8,-6,-2,7,6,-3,-10,-9,-2,8,9,-6,8,7,-2,9,-5,4,-1,7,5,-10,-9,-7,-8,-10,5,-2,-5,-2,-3,-9,-5,-8,-4,-6,3,7,4,2,9,9,-7,8,9,-9,10,-3,-10,1,-3,4,-2,-9,-5,8,-2,-1,-9,-1,8,3,9,-2,4,-5,-2,-5,10,-3,-5,-2,-10,-6,-1,-7,8,-6,5,-7,5,6,-1,-4,-6,-7,-9,-8,1,10,-10,2,9,8,-7,-1,-5,10,1,-6,-2,-8,3,2,9,-7,-10,-10,8,-1,10,-1,-2,-10,6,9,-10,-1,-2,-8,-6,1,-7,-5,8,-2,-1,-3,4,5,3,10,-3,-8,-7,-10,-3,-10,-2,5,-2,-8,2,5,9,7,-8,-5,1,9,-2,-2,-10,7,-9,9,1,-4,1,10,3,-9,-8,1,-10,7,9,-8,2,-8,8,-4,-9,6,10,-7,5,4,-4,3,7,-5,9,-5,1,-4,5,1,-8,3,3,1,-7,1,3,-5,-6,-9,6,-8,9,7,1,9,3,7,1,-5,-6,2,-2,10,-9,-3,-2,3,4,-7,-8,-6,8,8,-5,8,9,9,-6,7,7,-2,10,2,7,-3,-8,9,-4,3,-10,-1,2,-10,8,-6,9,5,7,-5,7,-1,-9,-10,7,-2,-4,-6,2,7,-5,-6,2,6,-1,4,-1,4,5,-2,-5,9,-7,8,-3,1,7,-6,3,6,3,1,-5,3,-6,2,9,-3,-8,-6,-7,3,-8,-2,-1,2,-10,-9,7,7,-6,5,10,-2,10,-9,6,-2,1,5,4,-5,10,9,5,-1,5,-6,5,-3,-7,3,-6,-10,-8,-8,-2,-7,6,-10,-4,-4,8,-3,-10,-7,1,-2,4,4,7,-2,-5,-3,-5,-2,5,-7,7,-5,8,-6,3,-6,2,-9,-1,9,-10,-9,-7,-5,8,-7,-1,2,6,8,5,-6,-3,-7,-6,2,-1,10,-3,-2,6,-6,4,6,-5,7,8,9,8,8,4,-7,-1,3,-3,-5,-6,6,8,-8,-8,-6,-10,-8,1,-2,3,10,-8,10,-7,2,7,-3,-2,9,-8,6,10,-8,-9,-7,-10,8,9,-1,4,-2,-3,-5,8,7,-1,-5,9,1,4,10,-5,3,-10,-10,10,-5,-9,-10,-6,-4,-1,5,4,8,6,-1,-10,-4,-9,-3,8,-1,-10,-3,-9,-1,-6,2,6,6,-10,4,-1,8,-7,-10,9,-10,-4,5,-10,4,5,-5,-6,5,-10,-3,1,3,-2,-3,-4,-2,-5,-4,3,2,3,-1,8,4,6,1,1,-7,6,-6,10,1,-6,4,-2,-9,4,6,7,2,-7,3,6,3,-8,4,-8,7,1,-5,-8,10,6,3,-5,-9,7,-2,-3,-7,-5,-3,8,-9,3,-2,10,-2,7,10,-2,4,-2,-4,-3,-8,-2,1,10,8,4,4,-3,10,4,4,8,9,6,7,-6,6,-3,-9,7,-6,-9,-4,-9,-4,4,-10,6,4,-5,-1,-5,1,4,-3,-9,-1,-9,1,-9,10,-3,-8,2,-10,5,1,8,8,-4,-2,-9,-1,10,-6,-7,4,9,-8,6,-9,7,2,2,7,2,10,4,10,3,5,-4,-9,-3,-5,5,1,-4,9,-5,-5,-8,8,4,8,-6,7,-1,5,5,4,-4,6,-10,-5,3,-1,4,-5,-9,-6,-7,9,1,-2,3,-10,3,-6,-3,7,2,-1,1,-5,-10,-7,5,-4,9,-7,-4,-9,5,9,8,-5,5,-7,3,-9,2,-9,2,-3,1,-5,-7,3,2,1,9,-10,-4,-3,8,8,-7,-7,2,2,-2,-10,5,-2,-7,-9,-10,3,8,1,-7,8,-7,3,-6,5,-5,-8,10,7,4,-6,-7,-10,-4,-10,1,-4,-2,-10,-3,-8,-9,9,8,-1,-4,-9,-7,-3,-10,-3,-3,-9,-6,-5,1,-9,10,4,-4,10,-1,8,-8,8,-5,8,7,-5,4,2,-3,-10,9,-1,-8,-10,2,8,10,-7,-8,-5,2,-8,9,-4,2,-7,9,-3,-1,-7,-4,2,-10,9,3,2,3,2,3,4,1,6,9,6,-6,-4,5,-2,-4,2,4,-3,-6,-9,-2,-2,-4,2,10,7,8,-4,-7,7,-9,1,4,10,-10,9,-2,4,1,-3,-3,-7,-2,-5,9,-2,-2,2,8,6,-1,-9,-5,-10,10,-9,4,5,9,6,-1,-8,1,9,-2,-7,-1,7,-1,4,2,8,9,3,3,-6,8,-9,4,8,4,-2,-2,-1,-7,6,-8,7,-8,-5,-2,7,-7,-8,-4,-10,2,1,10,-6,-7,-6,7,-4,6,7,-10,-5,-9,-7,-1,-1,-8,4,-4,-5,-3,10,6,6,-3,9,7,10,9,9,6,-1,-2,-2,-5,9,-2,9,-3,10,-8,-9,3,3,9,-1,1,9,7,2,-10,2,-2,-10,8,10,10,-10,-1,4,4,6,7,1,-7,-8,3,-9,-2,9,10,5,9,1,-10,-1,-2,2,-2,-5,-7,8,-4,-5,7,-6,5,4,-9,-5,2,3,-3,-3,-1,6,1,8,-10,-2,8,3,-1,7,-2,7,8,-7,-9,6,9,6,5,-7,-6,3,9,7,-10,10,-9,-5,-8,-10,3,7,-7,3,-8,8,-1,9,-4,2,3,6,-8,10,1,5,7,5,-6,5,-1,7,1,-4,2,-9,-7,-10,-3,-2,-2,10,10,1,-6,-1,1,-8,6,7,7,7,-10,8,-7,10,9,7,5,-9,-6,7,10,10,-7,-6,-5,-8,-7,-8,7,2,-8,-7,-6,-2,-7,-10,4,3,-8,-6,1,8,10,-2,4,5,4,-2,10,-5,-5,-4,-6,10,7,7,-10,7,10,7,5,5,5,10,-3,2,9,-9,-4,-10,-5,-2,1,4,-1,5,-4,3,-10,-5,-7,5,3,-2,-2,-2,9,-3,3,2,-10,-10,-9,-4,-8,-6,-3,3,-4,7,-7,-3,2,5,-5,9,-5,-8,2,7,-8,-4,-3,-9,2,-3,4,3,3,-9,-6,2,7,-8,-1,-6,-6,-1,7,-6,-7,-8,-4,-7,1,-3,-6,8,4,-10,-9,-5,-7,5,-8,1,-9,-8,-9,10,-1,-7,-8,8,-1,9,5,8,-2,-3,4,-8,4,6,1,3,8,8,-5,10,-5,7,-4,-9,7,-9,-8,6,4,-5,-9,-6,-8,-5,-3,10,-3,-7,1,-3,9,-1,-8,-9,10,-7,4,-8,-10,-9,5,2,-6,4,6,-8,-7,2,-8,8,-8,-9,-10,7,7,4,5,1,-4,9,-2,5,-7,-7,-9,-3,1,9,8,-1,2,-8,-1,8,-5,5,5,-9,6,-7,2,-2,-1,-2,7,-5,-1,5,3,-9,-10,10,-6,-8,-6,7,-5,10,-10,-7,8,-7,5,4,5,8,10,1,-8,6,5,9,4,8,-2,2,-6,-2,1,1,-9,-1,9,-3,-4,9,4,-1,-9,-2,-5,4,3,2,-10,-8,-4,-8,-3,-9,9,6,8,-2,8,10,8,3,-10,5,-10,10,4,-8,-6,5,5,-1,-1,-9,-6,-2,-5,-8,-2,6,8,7,-4,2,-9,7,2,-6,10,-2,8,-3,-9,-1,-7,-4,-5,-8,3,8,9,-8,1,4,1,10,-1,4,5,10,2,-7,-4,-5,7,3,-7,6,6,1,-5,-9,-3,6,-10,-2,-2,-9,-7,5,8,-9,8,-4,3,-4,-8,7,-5,3,-1,8,-5,-2,-3,-6,5,-7,1,7,-9,-4,-3,-8,6,-6,8,4,2,8,3,6,9,10,7,4,8,2,-1,-10,4,7,9,-5,-7,8,-7,5,10,-6,3,-10,9,10,4,10,5,8,-9,7,-6,-4,-9,-10,4,-5,-7,-8,9,-10,-8,-1,-8,-9,1,-10,10,3,3,-10,1,-6,2,-9,-1,-6,-9,-4,-5,1,6,7,7,7,3,-9,-3,-5,6,-10,10,8,4,-6,2,6,-1,3,-3,8,-8,-10,-9,-9,-6,-5,-4,6,2,6,-1,1,-5,8,7,-4,10,-7,7,-7,5,-1,-5,-9,-1,1,9,-2,10,-4,5,-3,2,-7,6,-3,-7,1,3,7,5,4,1,8,-7,8,10,8,-3,-10,8,-1,-10,-5,2,-5,-1,1,-6,-3,1,4,3,3,4,5,9,-6,-10,-1,4,-9,6,7,9,4,1,1,-7,-2,-10,-2,-4,-9,1,7,4,10,-8,-2,9,8,2,-8,6,10,8,6,-4,8,-2,1,-3,-6,10,-9,-3,-10,6,6,7,-7,-9,7,-7,9,2,-5,-10,7,10,8,-10,-10,8,10,1,-10,-10,4,-6,7,10,2,-3,-2,4,8,-10,-2,-4,6,2,6,7,-1,4,8,8,-5,-2,7,7,-1,6,7,-8,5,-1,1,-4,8,10,1,-9,-10,1,6,-5,-7,2,8,7,9,-8,-5,-5,-8,10,-5,-4,-1,-4,-5,3,7,7,7,-1,-1,9,9,8,8,-7,-10,-8,7,7,-1,5,-8,-3,6,1,3,3,5,1,3,8,10,4,10,-3,-4,6,3,-8,5,8,1,-4,-5,2,5,-3,6,4,1,-4,8,-10,1,-9,9,-4,9,9,-5,3,-8,4,-6,-9,-8,5,-5,6,-2,2,-2,-4,-6,-6,1,-10,-8,3,5,-2,-7,10,1,-7,10,-6,10,1,10,-9,-9,-2,-5,2,6,-4,10,-6,9,5,5,-10,-9,2,-10,-2,8,-5,-8,-3,-8,1,3,10,1,9,-7,2,2,7,5,-9,5,7,9,-2,-9,9,-10,-3,-6,-8,1,-7,6,-3,5,-5,7,4,4,-7,8,-4,-6,-9,9,-3,9,-1,6,-7,7,-1,-6,2,-10,-2,2,-7,2,1,3,-2,-4,9,-9,2,2,2,-8,-7,-1,9,4,-4,-1,-10,8,7,6,-3,6,-3,-9,-6,9,-7,2,-6,1,-7,-4,7,8,6,-3,9,4,-6,6,8,-7,6,1,8,-3,-6,-1,-8,8,4,-3,-1,-4,-8,10,8,2,-7,-7,7,-1,6,6,10,10,-7,7,-7,-6,-3,-2,-6,-6,-9,1,4,9,-1,-6,10,6,-6,-5,6,-10,2,2,10,2,-5,-5,2,-9,-6,-7,-10,4,-6,10,2,4,6,1,-6,-3,-5,-9,10,-1,2,5,-1,-7,9,2,9,-5,-2,9,9,-8,-10,-3,-5,-1,2,-9,4,-3,-3,-4,9,-5,6,-8,6,1,-2,-10,-9,-4,-6,8,-8,3,-6,-2,-6,5,-1,-9,10,4,-4,-3,-5,6,9,-9,4,8,9,-4,-7,7,5,-4,5,1,4,4,10,-9,3,7,2,-9,5,7,4,1,-1,-4,-5,-8,8,6,-2,-8,5,-4,3,1,7,-2,-4,-10,-10,-1,-1,3,1,-9,6,-9,5,9,7,5,-8,6,-2,8,5,6,-10,-7,-8,-3,-6,-7,-6,-8,-6,8,4,9,4,-7,-7,-7,9,6,-2,4,-1,-10,7,1,-3,-1,-7,-2,-6,-2,-9,7,-2,-9,-4,-6,-4,-4,-4,-4,6,-5,-6,3,-3,2,-3,4,-4,4,6,4,6,-8,-5,-9,-10,3,9,-7,-3,6,7,-3,-3,-10,-7,-6,4,-3,-8,9,9,3,10,-2,-8], dtype = "int8")#candidate|5116|(3150,)|const|int8
call_5115 = relay.TupleGetItem(func_2836_call(relay.reshape(const_5116.astype('int8'), [15, 15, 14]), relay.reshape(const_5116.astype('int8'), [15, 15, 14]), ), 0)
call_5117 = relay.TupleGetItem(func_2840_call(relay.reshape(const_5116.astype('int8'), [15, 15, 14]), relay.reshape(const_5116.astype('int8'), [15, 15, 14]), ), 0)
output = relay.Tuple([call_5107,call_5115,const_5116,])
output2 = relay.Tuple([call_5108,call_5117,const_5116,])
func_5118 = relay.Function([], output)
mod['func_5118'] = func_5118
mod = relay.transform.InferType()(mod)
output = func_5118()
func_5119 = relay.Function([], output)
mutated_mod['func_5119'] = func_5119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4506_call = mod.get_global_var('func_4506')
func_4508_call = mutated_mod.get_global_var('func_4508')
call_5122 = relay.TupleGetItem(func_4506_call(), 0)
call_5123 = relay.TupleGetItem(func_4508_call(), 0)
output = call_5122
output2 = call_5123
func_5139 = relay.Function([], output)
mod['func_5139'] = func_5139
mod = relay.transform.InferType()(mod)
mutated_mod['func_5139'] = func_5139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5139_call = mutated_mod.get_global_var('func_5139')
call_5140 = func_5139_call()
output = call_5140
func_5141 = relay.Function([], output)
mutated_mod['func_5141'] = func_5141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3376_call = mod.get_global_var('func_3376')
func_3378_call = mutated_mod.get_global_var('func_3378')
call_5211 = relay.TupleGetItem(func_3376_call(), 1)
call_5212 = relay.TupleGetItem(func_3378_call(), 1)
var_5218 = relay.var("var_5218", dtype = "float64", shape = (4, 9, 14))#candidate|5218|(4, 9, 14)|var|float64
bop_5219 = relay.divide(call_5211.astype('float64'), relay.reshape(var_5218.astype('float64'), relay.shape_of(call_5211))) # shape=(4, 9, 14)
bop_5222 = relay.divide(call_5212.astype('float64'), relay.reshape(var_5218.astype('float64'), relay.shape_of(call_5212))) # shape=(4, 9, 14)
output = bop_5219
output2 = bop_5222
func_5234 = relay.Function([var_5218,], output)
mod['func_5234'] = func_5234
mod = relay.transform.InferType()(mod)
mutated_mod['func_5234'] = func_5234
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5235 = relay.var("var_5235", dtype = "float64", shape = (4, 9, 14))#candidate|5235|(4, 9, 14)|var|float64
func_5234_call = mutated_mod.get_global_var('func_5234')
call_5236 = func_5234_call(var_5235)
output = call_5236
func_5237 = relay.Function([var_5235], output)
mutated_mod['func_5237'] = func_5237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4351_call = mod.get_global_var('func_4351')
func_4352_call = mutated_mod.get_global_var('func_4352')
call_5249 = relay.TupleGetItem(func_4351_call(), 2)
call_5250 = relay.TupleGetItem(func_4352_call(), 2)
output = relay.Tuple([call_5249,])
output2 = relay.Tuple([call_5250,])
func_5251 = relay.Function([], output)
mod['func_5251'] = func_5251
mod = relay.transform.InferType()(mod)
mutated_mod['func_5251'] = func_5251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5251_call = mutated_mod.get_global_var('func_5251')
call_5252 = func_5251_call()
output = call_5252
func_5253 = relay.Function([], output)
mutated_mod['func_5253'] = func_5253
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5307 = relay.var("var_5307", dtype = "float64", shape = (6, 12, 11))#candidate|5307|(6, 12, 11)|var|float64
uop_5308 = relay.log2(var_5307.astype('float64')) # shape=(6, 12, 11)
output = uop_5308
output2 = uop_5308
func_5319 = relay.Function([var_5307,], output)
mod['func_5319'] = func_5319
mod = relay.transform.InferType()(mod)
mutated_mod['func_5319'] = func_5319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5320 = relay.var("var_5320", dtype = "float64", shape = (6, 12, 11))#candidate|5320|(6, 12, 11)|var|float64
func_5319_call = mutated_mod.get_global_var('func_5319')
call_5321 = func_5319_call(var_5320)
output = call_5321
func_5322 = relay.Function([var_5320], output)
mutated_mod['func_5322'] = func_5322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_5337 = relay.TupleGetItem(func_3457_call(), 3)
call_5338 = relay.TupleGetItem(func_3459_call(), 3)
uop_5341 = relay.log10(call_5337.astype('float64')) # shape=(3150,)
uop_5343 = relay.log10(call_5338.astype('float64')) # shape=(3150,)
func_2811_call = mod.get_global_var('func_2811')
func_2816_call = mutated_mod.get_global_var('func_2816')
var_5355 = relay.var("var_5355", dtype = "float32", shape = (210,))#candidate|5355|(210,)|var|float32
var_5356 = relay.var("var_5356", dtype = "int8", shape = (900,))#candidate|5356|(900,)|var|int8
var_5357 = relay.var("var_5357", dtype = "uint16", shape = (26, 11))#candidate|5357|(26, 11)|var|uint16
call_5354 = relay.TupleGetItem(func_2811_call(relay.reshape(var_5355.astype('float32'), [7, 15, 2]), relay.reshape(var_5356.astype('int8'), [900,]), relay.reshape(var_5357.astype('uint16'), [286,]), ), 7)
call_5358 = relay.TupleGetItem(func_2816_call(relay.reshape(var_5355.astype('float32'), [7, 15, 2]), relay.reshape(var_5356.astype('int8'), [900,]), relay.reshape(var_5357.astype('uint16'), [286,]), ), 7)
func_3376_call = mod.get_global_var('func_3376')
func_3378_call = mutated_mod.get_global_var('func_3378')
call_5363 = relay.TupleGetItem(func_3376_call(), 2)
call_5364 = relay.TupleGetItem(func_3378_call(), 2)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_5365 = func_1015_call()
call_5366 = func_1015_call()
bop_5371 = relay.greater_equal(uop_5341.astype('bool'), call_5365.astype('bool')) # shape=(7, 15, 3150)
bop_5374 = relay.greater_equal(uop_5343.astype('bool'), call_5366.astype('bool')) # shape=(7, 15, 3150)
func_4258_call = mod.get_global_var('func_4258')
func_4260_call = mutated_mod.get_global_var('func_4260')
call_5376 = func_4258_call()
call_5377 = func_4258_call()
func_2068_call = mod.get_global_var('func_2068')
func_2069_call = mutated_mod.get_global_var('func_2069')
call_5380 = relay.TupleGetItem(func_2068_call(), 1)
call_5381 = relay.TupleGetItem(func_2069_call(), 1)
bop_5389 = relay.bitwise_and(bop_5371.astype('uint32'), uop_5341.astype('uint32')) # shape=(7, 15, 3150)
bop_5392 = relay.bitwise_and(bop_5374.astype('uint32'), uop_5343.astype('uint32')) # shape=(7, 15, 3150)
func_3340_call = mod.get_global_var('func_3340')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_5397 = relay.TupleGetItem(func_3340_call(), 0)
call_5398 = relay.TupleGetItem(func_3342_call(), 0)
output = relay.Tuple([call_5354,var_5355,var_5356,var_5357,call_5363,call_5376,call_5380,bop_5389,call_5397,])
output2 = relay.Tuple([call_5358,var_5355,var_5356,var_5357,call_5364,call_5377,call_5381,bop_5392,call_5398,])
func_5403 = relay.Function([var_5355,var_5356,var_5357,], output)
mod['func_5403'] = func_5403
mod = relay.transform.InferType()(mod)
mutated_mod['func_5403'] = func_5403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5403_call = mutated_mod.get_global_var('func_5403')
var_5405 = relay.var("var_5405", dtype = "float32", shape = (210,))#candidate|5405|(210,)|var|float32
var_5406 = relay.var("var_5406", dtype = "int8", shape = (900,))#candidate|5406|(900,)|var|int8
var_5407 = relay.var("var_5407", dtype = "uint16", shape = (26, 11))#candidate|5407|(26, 11)|var|uint16
call_5404 = func_5403_call(var_5405,var_5406,var_5407,)
output = call_5404
func_5408 = relay.Function([var_5405,var_5406,var_5407,], output)
mutated_mod['func_5408'] = func_5408
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5410 = relay.const([[[-1.046826,-0.311368,-0.113974,-9.529094,5.577002,-0.897696]],[[-9.501391,-6.019334,1.505310,-6.559373,-9.339325,1.884282]],[[-5.435978,1.765175,-4.697050,-7.418181,-0.396094,-4.194783]],[[-0.072247,7.739523,5.364574,7.152398,-4.647552,-2.904490]],[[3.527979,-7.179654,9.329807,4.339004,-9.167552,-5.153126]],[[3.801437,5.126267,7.250012,-8.736729,-5.442061,-5.381969]],[[8.322413,5.589623,2.584993,-4.910601,-0.239468,-1.041224]]], dtype = "float64")#candidate|5410|(7, 1, 6)|const|float64
uop_5411 = relay.sin(const_5410.astype('float64')) # shape=(7, 1, 6)
output = uop_5411
output2 = uop_5411
func_5414 = relay.Function([], output)
mod['func_5414'] = func_5414
mod = relay.transform.InferType()(mod)
output = func_5414()
func_5415 = relay.Function([], output)
mutated_mod['func_5415'] = func_5415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4655_call = mod.get_global_var('func_4655')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_5428 = func_4655_call()
call_5429 = func_4655_call()
uop_5438 = relay.cosh(call_5428.astype('float32')) # shape=(7, 15, 1)
uop_5440 = relay.cosh(call_5429.astype('float32')) # shape=(7, 15, 1)
func_5319_call = mod.get_global_var('func_5319')
func_5322_call = mutated_mod.get_global_var('func_5322')
const_5443 = relay.const([-1.664804,-4.801591,-9.074867,7.539460,-4.766216,-3.146568,1.675386,6.228257,3.708907,-8.767081,3.739467,2.937945,6.353062,2.215574,-0.157463,-6.182697,4.123000,-5.170439,7.552165,7.338947,-2.708682,0.719839,1.663233,-8.348152,4.346863,-4.555157,-3.195332,2.445141,-0.062447,2.471158,7.666906,-5.053608,-4.638020,-6.671411,-6.262566,-3.039747,-3.278006,-7.309612,-9.174262,-2.339185,-6.219153,-2.986988,-1.963222,-4.520275,-8.359921,6.299414,0.662797,-6.306880,2.421511,-3.430419,6.409421,-9.166741,-1.846581,0.422265,6.279446,-5.792039,-9.394343,7.019498,3.585333,2.903393,1.201923,7.316481,-0.380858,-6.554031,3.661475,-9.378648,5.020408,-3.291678,8.664098,-1.312330,0.644355,-4.089110,7.180856,6.014054,1.093741,4.067843,9.910438,-9.962198,-7.266872,2.388807,0.124847,-3.331036,-5.619390,-1.195440,-0.666053,4.738826,-5.997301,5.192668,7.936526,-9.540655,-7.564385,9.890132,-1.558271,4.492536,-6.001526,-6.865348,-6.941740,4.336605,6.103574,5.049337,-5.938965,-6.041215,-0.211477,0.590145,-5.576075,1.781675,1.036852,-6.358678,-0.213139,-9.055377,1.523058,-7.830448,-7.776390,-0.069477,6.081241,9.036152,-6.562462,-9.144516,-8.648769,-2.157564,7.657586,8.473726,-6.291894,9.275302,5.540144,-1.238522,-8.194336,7.332915,-4.365756,7.122762,2.618237,0.369951,-5.589389,-6.811464,2.987226,8.723004,-7.552778,4.009868,-5.638988,0.098113,8.262204,-2.004202,-8.153663,-4.088286,-5.740257,2.863977,-3.757893,7.120206,-9.063861,8.500324,2.560873,2.253114,7.108079,-8.452605,9.171478,-5.631484,2.483929,-7.791420,-7.325863,-5.035968,-6.719569,-2.021188,7.398855,7.901836,7.302214,1.396358,6.470528,5.808341,-4.437142,3.197689,2.975201,-7.269903,-4.391432,1.316250,8.238716,2.956197,7.453252,-8.770146,-2.387446,-4.086963,3.092535,-2.899191,-7.000481,6.579108,3.025657,-9.331814,-7.428333,-9.786216,-0.471354,2.095050,4.344031,4.620910,-5.590564,3.861586,-6.010580,9.826052,-5.528681,-4.734510,2.970288,0.507548,-7.910340,0.423824,-5.349198,-5.255175,6.106946,-9.452008,-0.869421,4.015352,0.656550,5.861603,3.329922,2.847529,-3.870067,-8.892714,-0.881586,9.611517,-6.990490,5.256161,-6.580194,3.212861,-0.272831,-8.730233,8.863865,1.588856,3.113490,-1.087911,8.540193,-5.950123,-5.034630,7.836123,-0.503108,3.939235,-0.528156,4.420765,-4.260562,-0.056241,-5.629622,-0.366623,5.803009,-2.319770,-7.353238,2.869023,0.811634,-8.145056,-8.422306,-2.293129,-5.272494,1.253540,-4.277308,1.956428,4.000122,3.679070,-3.517215,-8.346526,-6.209678,-0.480625,0.881369,-7.909597,0.518066,-3.365953,9.609715,-7.509663,6.566582,-3.609959,-5.940488,-4.215056,1.270835,1.170532,5.708681,2.501980,3.558471,3.104005,4.897918,1.499353,-5.661478,3.969911,-8.255626,0.327803,0.383578,5.837821,5.453067,-0.709960,-5.024539,-5.004947,2.931523,4.986014,-5.877709,4.577627,-1.696351,-0.328578,2.611988,-7.327810,-0.765314,5.027488,7.159982,0.630864,-0.255499,-5.176005,-6.065443,1.766352,-8.079272,-6.084155,4.339080,9.882656,-2.534874,-0.896519,7.100159,7.846766,-8.457973,0.287824,9.791886,-5.950012,-4.701940,-4.467103,9.990090,-3.347809,-0.115476,-3.286699,5.995578,-6.480636,-2.020798,8.072434,6.880835,0.649926,5.574101,-7.613990,8.377472,-4.771162,7.082274,-6.976548,-7.395265,-2.381720,5.207189,-9.936979,-5.926866,-1.788892,3.742845,-7.240693,-6.438056,-5.242631,4.598232,7.241057,0.213056,-1.916774,-6.444614,-3.312533,-4.609586,-1.040296,8.359600,-4.693541,0.798047,-4.253855,-5.733759,1.801120,-3.428296,-6.074810,-8.949931,6.367137,9.657131,-0.618119,-7.598876,6.784268,-1.746580,4.499246,-3.129131,0.590300,-6.534747,7.397856,3.192279,-9.286966,-7.213887,8.290598,-9.710649,9.510765,-2.656744,0.421634,-6.672944,6.335412,-5.590630,-7.224728,-2.463636,-7.044187,-2.357368,6.835088,0.554289,4.557707,-4.285079,-7.994550,6.176871,1.006241,-2.894745,3.546565,9.859076,2.651862,1.552960,-2.302773,5.442496,-3.849088,-5.272300,2.178059,0.033134,-8.253808,2.447242,-9.338338,-2.596759,6.541381,7.959821,7.779913,6.375414,-7.060137,-8.683607,6.889830,-4.485372,8.301933,8.196263,-4.846911,-3.806789,6.991641,2.417868,-7.404426,5.273332,-2.459375,-7.784890,6.192058,-5.824302,-3.424072,-5.578070,3.807396,-8.002464,-1.477425,3.171368,-6.050856,1.819261,-9.240671,-2.311917,-6.710927,-8.268136,-3.762896,-5.860249,-2.797035,3.734342,1.449302,-2.653175,-8.596450,-6.445959,7.636906,3.791539,0.504576,5.849179,-9.732077,-1.754039,5.638746,3.526972,-2.637102,5.498276,2.940645,6.179606,-1.679866,0.952587,-4.108307,2.077362,4.932341,-1.190075,4.995125,-7.165252,3.335712,-1.160543,1.527980,-1.010435,5.557111,5.571314,-3.971063,-8.698983,-7.998907,-7.914251,8.566608,-8.538878,-5.144792,9.972032,-9.103194,4.083904,-5.910592,-5.021326,-3.192218,0.498046,-4.342804,-4.567367,-0.074930,-4.091073,-3.070807,5.410666,-2.017846,-7.717677,-0.116904,6.534054,-4.020918,-1.533914,-4.594761,-2.002547,0.529369,0.783496,-4.511889,0.666660,-9.735727,-4.384255,-3.949526,-1.227742,7.108000,0.173887,-7.667933,5.100623,-5.000082,4.367308,-5.480795,6.034787,-5.944391,-3.140306,-9.669042,6.366623,1.083644,0.558035,8.678461,-3.114714,-3.650731,6.845891,-8.480414,6.213127,-0.562171,-0.918189,0.878099,3.581751,-8.067366,-1.819849,4.828097,4.282539,3.980135,-7.701264,-5.181084,-2.357926,-8.842382,7.419230,-8.670416,9.505638,1.241395,2.170423,6.061959,-9.333039,-6.478864,-4.747435,-3.949150,-9.058346,-9.090809,6.151525,-8.694437,-3.937991,0.726380,7.975603,-8.383376,-5.226232,-5.780265,-9.825498,-0.011395,1.250895,-1.653794,-9.149958,8.003346,-9.126823,4.977167,-5.093068,5.940319,4.104808,-6.651240,-2.250901,1.453075,7.971582,7.933606,-3.607785,-6.013875,-9.837435,3.292652,-8.926027,-7.243549,1.210859,-0.105664,7.851142,-2.942384,-7.662218,8.237536,5.765783,6.107376,8.869609,5.418236,1.761313,9.310370,-2.630922,-8.934327,-0.470074,2.588031,5.518552,1.202787,-1.850333,4.829516,5.730062,8.409661,0.071652,5.011077,2.749338,-0.560947,-6.097153,0.442415,7.671265,4.136576,-9.003294,3.122214,-4.152893,-1.055265,-5.419709,3.619484,-8.532484,-2.124046,-2.112820,-0.760594,-7.580315,-3.478035,2.416783,4.805201,8.694827,-2.851488,-1.779141,4.105512,-0.503532,0.230013,7.963521,-8.616931,3.144994,-5.494748,-8.371385,-3.964953,2.155393,-3.842419,-0.838035,6.975399,-8.762358,0.090042,6.431958,-3.268150,-1.428025,-8.530373,-9.577537,9.840904,-8.926480,1.319570,0.276305,8.778833,-7.903826,9.778222,-2.764987,0.365175,-9.745194,6.691394,6.028223,9.082773,6.343025,-0.838806,9.973032,6.941852,2.253148,-1.770146,-1.545030,0.539234,1.071607,2.700182,-6.992196,5.129384,0.616275,-7.836394,-7.458283,-7.352974,-9.433511,2.195091,7.785738,2.570940,-8.342281,6.165373,7.133389,1.192833,6.102393,-3.765496,3.929320,-9.200496,-9.783199,-9.250081,-6.754266,-8.045260,8.743239,-5.125101,2.610148,5.361096,-5.475777,-8.866520,8.543725,-8.913238,7.304445,-4.545348,-7.863184,6.547536,-5.317816,9.589184,8.497576,5.937634,-5.154509,7.847238,6.570846,4.621510,2.430402,7.730846,8.273257,8.126935,1.802355,-3.150569,-2.520642,-6.612936,0.642843,4.551156,-8.603907,7.046584,0.931325,-0.849534,8.088408,-8.106561,1.861631,0.912510,0.286901,6.652795,2.868114,7.125312,-5.990652,-9.710887,8.562106,-2.076251,-8.126766,-4.515513,-9.842764,-7.114281,-1.795531,-5.155107,-9.228092,3.665663,-7.471903,-2.482337,-5.176728,0.981756,-9.794593,-4.230568,4.844309,2.623191,-4.400483,2.852471,-3.319293,-7.561135,-2.638987,-4.626374,-2.641310,6.342784,8.223058,-7.379583,8.861408,-3.825318,1.633420,5.570899,2.866995,-0.294573,4.302248,-7.697513,0.208477,-3.664642,8.461456,8.410971,-3.676970,-4.550505,-9.571240,4.379370,-2.408537,8.280524,-1.391659,-8.586094,0.692779,8.424731,3.543465,-7.270835,-6.798100,-7.721509], dtype = "float64")#candidate|5443|(792,)|const|float64
call_5442 = func_5319_call(relay.reshape(const_5443.astype('float64'), [6, 12, 11]))
call_5444 = func_5319_call(relay.reshape(const_5443.astype('float64'), [6, 12, 11]))
bop_5449 = relay.not_equal(uop_5438.astype('bool'), const_5443.astype('bool')) # shape=(7, 15, 792)
bop_5452 = relay.not_equal(uop_5440.astype('bool'), const_5443.astype('bool')) # shape=(7, 15, 792)
uop_5458 = relay.tan(const_5443.astype('float32')) # shape=(792,)
output = relay.Tuple([call_5442,bop_5449,uop_5458,])
output2 = relay.Tuple([call_5444,bop_5452,uop_5458,])
func_5470 = relay.Function([], output)
mod['func_5470'] = func_5470
mod = relay.transform.InferType()(mod)
mutated_mod['func_5470'] = func_5470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5470_call = mutated_mod.get_global_var('func_5470')
call_5471 = func_5470_call()
output = call_5471
func_5472 = relay.Function([], output)
mutated_mod['func_5472'] = func_5472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2242_call = mod.get_global_var('func_2242')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_5503 = func_2242_call()
call_5504 = func_2242_call()
output = relay.Tuple([call_5503,])
output2 = relay.Tuple([call_5504,])
func_5507 = relay.Function([], output)
mod['func_5507'] = func_5507
mod = relay.transform.InferType()(mod)
output = func_5507()
func_5508 = relay.Function([], output)
mutated_mod['func_5508'] = func_5508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3944_call = mod.get_global_var('func_3944')
func_3945_call = mutated_mod.get_global_var('func_3945')
call_5558 = relay.TupleGetItem(func_3944_call(), 1)
call_5559 = relay.TupleGetItem(func_3945_call(), 1)
func_2119_call = mod.get_global_var('func_2119')
func_2121_call = mutated_mod.get_global_var('func_2121')
call_5562 = relay.TupleGetItem(func_2119_call(), 0)
call_5563 = relay.TupleGetItem(func_2121_call(), 0)
output = relay.Tuple([call_5558,call_5562,])
output2 = relay.Tuple([call_5559,call_5563,])
func_5564 = relay.Function([], output)
mod['func_5564'] = func_5564
mod = relay.transform.InferType()(mod)
output = func_5564()
func_5565 = relay.Function([], output)
mutated_mod['func_5565'] = func_5565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mod.get_global_var('func_3905')
func_3907_call = mutated_mod.get_global_var('func_3907')
call_5575 = relay.TupleGetItem(func_3905_call(), 0)
call_5576 = relay.TupleGetItem(func_3907_call(), 0)
func_4993_call = mod.get_global_var('func_4993')
func_4994_call = mutated_mod.get_global_var('func_4994')
call_5577 = relay.TupleGetItem(func_4993_call(), 0)
call_5578 = relay.TupleGetItem(func_4994_call(), 0)
output = relay.Tuple([call_5575,call_5577,])
output2 = relay.Tuple([call_5576,call_5578,])
func_5579 = relay.Function([], output)
mod['func_5579'] = func_5579
mod = relay.transform.InferType()(mod)
mutated_mod['func_5579'] = func_5579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5579_call = mutated_mod.get_global_var('func_5579')
call_5580 = func_5579_call()
output = call_5580
func_5581 = relay.Function([], output)
mutated_mod['func_5581'] = func_5581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mod.get_global_var('func_3905')
func_3907_call = mutated_mod.get_global_var('func_3907')
call_5584 = relay.TupleGetItem(func_3905_call(), 0)
call_5585 = relay.TupleGetItem(func_3907_call(), 0)
func_3018_call = mod.get_global_var('func_3018')
func_3019_call = mutated_mod.get_global_var('func_3019')
call_5589 = func_3018_call()
call_5590 = func_3018_call()
func_1890_call = mod.get_global_var('func_1890')
func_1894_call = mutated_mod.get_global_var('func_1894')
var_5600 = relay.var("var_5600", dtype = "bool", shape = (55, 7))#candidate|5600|(55, 7)|var|bool
call_5599 = relay.TupleGetItem(func_1890_call(relay.reshape(var_5600.astype('bool'), [7, 5, 11]), relay.reshape(var_5600.astype('bool'), [7, 5, 11]), ), 1)
call_5601 = relay.TupleGetItem(func_1894_call(relay.reshape(var_5600.astype('bool'), [7, 5, 11]), relay.reshape(var_5600.astype('bool'), [7, 5, 11]), ), 1)
output = relay.Tuple([call_5584,call_5589,call_5599,var_5600,])
output2 = relay.Tuple([call_5585,call_5590,call_5601,var_5600,])
func_5602 = relay.Function([var_5600,], output)
mod['func_5602'] = func_5602
mod = relay.transform.InferType()(mod)
mutated_mod['func_5602'] = func_5602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5603 = relay.var("var_5603", dtype = "bool", shape = (55, 7))#candidate|5603|(55, 7)|var|bool
func_5602_call = mutated_mod.get_global_var('func_5602')
call_5604 = func_5602_call(var_5603)
output = call_5604
func_5605 = relay.Function([var_5603], output)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1389_call = mod.get_global_var('func_1389')
func_1391_call = mutated_mod.get_global_var('func_1391')
call_5620 = func_1389_call()
call_5621 = func_1389_call()
output = relay.Tuple([call_5620,])
output2 = relay.Tuple([call_5621,])
func_5624 = relay.Function([], output)
mod['func_5624'] = func_5624
mod = relay.transform.InferType()(mod)
output = func_5624()
func_5625 = relay.Function([], output)
mutated_mod['func_5625'] = func_5625
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5626 = relay.var("var_5626", dtype = "float32", shape = (1, 10, 10))#candidate|5626|(1, 10, 10)|var|float32
uop_5627 = relay.log2(var_5626.astype('float32')) # shape=(1, 10, 10)
func_5507_call = mod.get_global_var('func_5507')
func_5508_call = mutated_mod.get_global_var('func_5508')
call_5642 = relay.TupleGetItem(func_5507_call(), 0)
call_5643 = relay.TupleGetItem(func_5508_call(), 0)
output = relay.Tuple([uop_5627,call_5642,])
output2 = relay.Tuple([uop_5627,call_5643,])
func_5657 = relay.Function([var_5626,], output)
mod['func_5657'] = func_5657
mod = relay.transform.InferType()(mod)
mutated_mod['func_5657'] = func_5657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5658 = relay.var("var_5658", dtype = "float32", shape = (1, 10, 10))#candidate|5658|(1, 10, 10)|var|float32
func_5657_call = mutated_mod.get_global_var('func_5657')
call_5659 = func_5657_call(var_5658)
output = call_5659
func_5660 = relay.Function([var_5658], output)
mutated_mod['func_5660'] = func_5660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3586_call = mod.get_global_var('func_3586')
func_3587_call = mutated_mod.get_global_var('func_3587')
call_5677 = func_3586_call()
call_5678 = func_3586_call()
output = relay.Tuple([call_5677,])
output2 = relay.Tuple([call_5678,])
func_5679 = relay.Function([], output)
mod['func_5679'] = func_5679
mod = relay.transform.InferType()(mod)
mutated_mod['func_5679'] = func_5679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5679_call = mutated_mod.get_global_var('func_5679')
call_5680 = func_5679_call()
output = call_5680
func_5681 = relay.Function([], output)
mutated_mod['func_5681'] = func_5681
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5715 = relay.var("var_5715", dtype = "uint32", shape = (14, 5, 8))#candidate|5715|(14, 5, 8)|var|uint32
const_5716 = relay.const([[[10,-7,-3,-7,4,-1,9,3],[1,7,-10,-1,-6,-1,5,6],[-10,-2,-4,5,1,2,-7,-1],[-2,6,1,-6,-6,5,-5,-7],[-5,-7,8,-8,-9,8,-9,6]],[[-1,5,8,10,-6,-7,7,-5],[5,-3,3,3,-4,-2,1,-4],[10,6,-1,-4,-1,-10,-5,1],[7,4,-5,-6,9,2,5,4],[-5,5,-5,3,-10,-2,-9,6]],[[7,8,6,-3,-1,4,-10,1],[-9,3,7,-9,10,3,-6,-5],[-10,9,6,-10,-4,3,5,3],[-4,9,4,-8,1,4,-2,-4],[-4,8,-2,7,7,4,-7,7]],[[3,3,-3,-4,4,-4,8,9],[-1,-2,-7,1,-2,-7,1,-10],[-7,-4,6,7,-7,-6,-8,-9],[-4,-4,-1,-7,1,3,6,-10],[8,5,1,4,2,-5,9,-9]],[[-4,-5,9,9,6,4,7,8],[8,-1,-5,9,7,8,-5,-8],[-2,-3,7,-3,-5,-6,8,8],[-7,-5,4,-10,5,6,8,10],[-10,-3,6,-7,-10,3,-7,4]],[[-8,6,2,-2,7,10,5,-7],[4,10,-5,-10,2,-7,-4,4],[-1,-3,-8,3,-4,-3,2,2],[10,-7,-2,4,-10,-4,-1,6],[9,-8,-4,-4,-3,-5,-5,-10]],[[-2,-1,-3,8,-5,10,9,9],[-5,4,-7,6,-5,4,10,6],[10,6,-4,9,-5,7,-4,3],[-5,-9,-7,-2,-7,-2,-10,-1],[-6,8,-1,9,-7,-3,3,2]],[[-5,10,-7,-4,-9,-3,5,-3],[-3,10,9,2,-6,-9,-1,10],[-4,-5,5,5,-6,-4,4,-1],[-8,1,-10,5,7,8,-5,-1],[-9,1,-8,7,-7,-4,-10,-8]],[[-5,8,-1,3,7,6,-2,-2],[-5,-4,-9,8,3,9,-6,4],[7,7,4,-5,-5,-2,10,-5],[-5,8,1,-2,-8,6,7,5],[1,-3,6,-6,1,-6,-2,-3]],[[-2,-2,9,-7,-4,-10,4,-6],[-9,-2,7,6,5,-6,-6,3],[2,-3,7,7,-3,-4,-4,4],[9,8,1,3,-9,3,10,3],[9,-4,-6,-10,9,7,-6,7]],[[-4,-9,-1,3,1,-5,-9,-2],[6,7,-8,2,2,-1,10,-4],[-2,-1,3,-5,7,-5,10,-7],[5,8,-2,1,2,4,7,-8],[9,6,-3,-10,2,-9,5,1]],[[-9,-3,1,-6,-5,5,-8,-5],[-2,3,-3,-8,-8,-1,10,-3],[1,1,-2,-5,7,3,4,-4],[-10,-4,8,9,-6,9,2,-6],[-9,-5,3,-2,-9,-6,2,1]],[[-5,-4,-4,8,-5,7,-10,8],[-1,-4,2,-3,-10,6,-6,-1],[-2,5,10,-10,-10,-10,-2,-2],[3,5,2,10,8,-2,-5,-7],[-10,4,6,2,-1,-8,5,5]],[[-6,5,2,-7,-3,5,4,4],[-6,3,-10,-10,9,5,-8,4],[-3,-9,6,5,7,-7,4,4],[-8,2,1,-3,9,-8,8,-8],[-3,-6,-5,10,1,-10,9,-6]]], dtype = "uint32")#candidate|5716|(14, 5, 8)|const|uint32
bop_5717 = relay.add(var_5715.astype('uint32'), relay.reshape(const_5716.astype('uint32'), relay.shape_of(var_5715))) # shape=(14, 5, 8)
func_3693_call = mod.get_global_var('func_3693')
func_3694_call = mutated_mod.get_global_var('func_3694')
call_5734 = relay.TupleGetItem(func_3693_call(), 0)
call_5735 = relay.TupleGetItem(func_3694_call(), 0)
func_3958_call = mod.get_global_var('func_3958')
func_3960_call = mutated_mod.get_global_var('func_3960')
call_5740 = func_3958_call()
call_5741 = func_3958_call()
bop_5744 = relay.bitwise_xor(call_5740.astype('int32'), call_5734.astype('int32')) # shape=(7, 15, 3150)
bop_5747 = relay.bitwise_xor(call_5741.astype('int32'), call_5735.astype('int32')) # shape=(7, 15, 3150)
output = relay.Tuple([bop_5717,bop_5744,])
output2 = relay.Tuple([bop_5717,bop_5747,])
func_5767 = relay.Function([var_5715,], output)
mod['func_5767'] = func_5767
mod = relay.transform.InferType()(mod)
var_5768 = relay.var("var_5768", dtype = "uint32", shape = (14, 5, 8))#candidate|5768|(14, 5, 8)|var|uint32
output = func_5767(var_5768)
func_5769 = relay.Function([var_5768], output)
mutated_mod['func_5769'] = func_5769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4411_call = mod.get_global_var('func_4411')
func_4413_call = mutated_mod.get_global_var('func_4413')
call_5771 = func_4411_call()
call_5772 = func_4411_call()
const_5797 = relay.const([8,7,3,9,-4,-1,6,4,-10,-3,10,-2,5,6,1,3,9,-7,4,4,-8,-8,-2,10,-1,3,-10,-6,4,-3,9,-4,-6,1,-6,-9,-1,9,-9,-5,5,-2,4,8,-2,-5,-8,9,2,5,4,2,-1,9,1,10,6,1,-10,8,-3,-2,1,-7,9,1,-6,-9,6,-8,-5,-5,10,9,-6,-3,1,9,7,5,6,1,10,8,9,-7,4,-3,7,-8,2,-1,7,5,6,1,-7,-3,-2,3,8,-6,-1,1,-3,-2,-10,-8,-2,2,2,-1,6,5,6,-9,-9,1,6,-9,-10,-5,-5,9,5,-7,-5,-7,-2,-8,10,7,4,1,-7,-2,1,-7,-10,6,-6,-6,1,1,-4,4,-6,-5,-6,-4,-7,1,-4,6,5,-1,5,1,9,-1,-10,-10,5,-1,-2,-7,-9,-8,-5,7,8,-10,-5,1,4,10,-7,4,-8,5,8,-10,8,-10,-4,-4,6,7,8,7,8,-10,10,6,-7,-7,-3,-3,-6,-8,1,5,10,9,8,10,7,-2,3,4,-9,8,9,6,6,10,-8,5,6,3,-3,-1,-4,7,9,1,2,3,-1,-1,-3,-4,-5,-6,-6,5,6,10,-7,1,-6,-7,10,-2,-6,-7,3,9,-4,-8,-6,10,9,5,-6,-3,7,-3,-7,-9,9,2,-9,1,-6,4,2,-5,5,-6,-6,-3,8,-1,10,-7,-6,-2,-10,8,2,9,7,4,5,3,10,4,10,2,-5,-1,-8,6,4,5,6,-9,-9,7,4,3,5,-1,-5,7,1,-1,-8,10,-10,7,8,-1,8,9,7,5,3,9,8,8,-1,-10,-7,-3,5,5,8,10,-5,10,-5,5,3,-6,7,2,-4,-1,5,9,3,-3,1,9,-4,-9,-3,7,-8,7,-8,7,3,4,-1,-8,-9,7,6,-10,-4,1,5,3,10,1,1,9,-4,-2,8,-9,-10,-8,2,-9,7,4,-10,5,1,8,-4,7,-2,4,8,-8,10,9,6,-10,9,-6,3,9,-9,-5,5,-2,-3,-6,10,1,2,5,7,-10,7,7,7,-3,2,1,10,-4,-10,3,-6,1,6,3,-1,-2,-9,8,5,-2,9,-6,-7,-3,-3,-8,-3,-7,4,4,3,4,7,7,5,-8,-5,5,-5,8,7,6,-4,10,-3,5,-10,-7,1,8,-5,2,1,9,-6,-5,-2,2,6,-6,-6,-6,-10,-5,8,8,-10,-1,-8,8,-9,6,5,-1,-1,9,-8,6,-9,8,4,9,6,8,4,5,-10,7,2,8,5,-3,-4,10,1,9,3,1,9,1,-7,9,9,3,-5,7,8,-2,8,-6,-9,-6,4,-2,-9,6,-1,-3,2,6,-9,-7,10,1,-3,-8,-1,-7,-2,-8,3,-6,1,-9,-7,10,5,-3,7,4,1,2,-4,9,-9,-8,-4,-9,4,-8,2,-7,5,1,-5,2,6,-10,-5,8,-5,-6,-1,-6,4,7,3,-2,-3,-10,9,4,8,-8,2,-6,-4,-8,9,1,-7,9,2,8,-4,4,2,1,-2,2,-6,-3,-3,7,-2,-5,-7,-8,-6,4,7,-5,6,7,-4,-1,9,3,4,2,-10,-8,-1,-6,3,7,8,8,-8,1,6,-4,-10,5,-9,-2,5,-6,6,-5,3,-10,-4,4,-3,-3,1,-4,-4,-4,7,4,6,2,3,3,-7,-7,-1,-2,8,-5,-3,-1,-9,2,3,-10,7,2,-7,-5,8,-7,5,-5,-7,5,9,-6,10,-6,7,1,8,-3,-8,3,-2,-7,2,-1,4,8,1,2,4,-2,4,5,7,-10,8,-3,6,1,-3,6,8,1,-7,-1,-2,4,-6,-9,6,-8,-3,-9,10,-8,2,-2,-7,2,-7,9,-5,7,-1,-6,6,-3,4,9,-10,9,-10,-2,4,-4,-6,2,3,3,-6,1,5,-2,-6,5,9,-9,4,7,-5,1,-4,-3,10,1,6,-7,-9,-10,-1,2,8,10,-5,2,-10,1,5,10,-3,1,-6,10,7,-10,-4,10,-4,-6,7,-8,10,-10,-7,-10,1,10,10,-3,-2,7,5,-10,8,-9,3,-4,9,9,4,6,9,-5,6,7,-10,3,-4,8,8,-8,5,5,-8,1,4,-9,3,-3,1,8,6,9,-4,-1,4,-5,-3,-4,7,-3,5,3,6,-9,-7,8,-8,-1,-6,5,4,-9,-4,-8,-10,-1,2,3,1,-5,-10,-2,-2,1,7,-7,7,8,1,-2,6,6,-9,-6,-2,9,-5,-10,-3,-4,6,1,-7,7,-4,9,-2,10,5,-2,-8,-8,-1,2,7,6,7,-9,8,-2,-2,-4,7,6,3,-6,-8,-6,3,4,-3,-5,10,5,-7,2,-10,-6,2,7,-9,-6,9,5,-9,-6,-9,-3,5,7,-6,3,-5,3,10,-3,-6,7,3,9,-3,4,-6,-3,4,-4,8,6,-6,-3,10,-9,-6,-2,-10,-3,-6,7,4,4,1,-8,-5,4,-3,2,-4,-10,9,1,2,4,-1,-1,-2,-6,-7,2,9,5,-3,-5,-8,-7,-6,-8,-2,-6,5,9,6,-10,10,-5,8,-10,9,-7,-2,-5,3,-5,-6,-8,-2,-8,-4,1,8,2,-8,-6,2,5,10,-2,-5,-7,-10,10,4,10,6,-2,9,-10,-10,7,2,6,4,-4,-5,-8,6,6,-7,9,-2,-8,7,-10,-6,7,-9,-1,-8,-1,-8,7,8,5,4,9,-5,6,4,-6,-3,10,7,6,-8,10,6,9,3,-1,8,-10,6,-2,4,-3,-5,10,6,-7,2,10,5,4,-3,-4,7,-1,-1,-5,5,1,-3,-9,-6,-5,6,-8,7,10,9,3,9,8,9,5,1,3,7,-5,10,3,9,6,5,6,-9,9,4,-8,-3,6,-8,-10,-1,-8,-8,7,-2,1,-1,1,-7,10,10,-4,-10,6,9,3,-2,-3,1,8,-2,-1,10,-5,-4,8,-2,6,-5,9,10,-6,-2,5,-8,7,3,-3,1,10,2,9,10,-5,10,1,-6,4,-5,-1,1,-4,-7,-7,-6,2,-3,-1,6,10,-2,6,9,7,-9,8,6,6,1,-2,8,-7,4,-8,6,8,10,-7,6,-6,4,-6,-7,4,6,7,9,-9,-1,-7,6,6,-1,-6,9,-3,5,3,-2,2,-2,-3,10,-8,-8,8,2,1,-7,2,10,-6,3,-9,-6,-4,-7,-3,-9,-9,-6,3,1,1,3,-3,-9,10,-8,-6,9,5,6,-6,-9,-2,-2,-2,10,-10,-9,8,3,9,-8,-8,-4,6,10,-7,-4,3,5,-8,9,8,2,5,5,-7,-8,9,-7,-3,6,8,-8,-8,6,-8,8,4,-3,5,2,10,-8,-3,-3,-4,8,-10,10,-1,-4,3,6,-1,-6,-8,10,-8,8,-3,-10,9,8,-6,7,-5,6,-4,5,5,4,8,1,2,9,-10,4,-1,-1,1,4,-1,-5,-5,2,10,3,-10,7,-4,1,7,7,10,-5,-6,-10,-9,3,3,-4,-1,-4,1,-7,8,-3,5,-5,6,9,-8,10,-2,-3,-10,2,6,-6,-5,-4,-3,10,-4,7,2,5,-3,-9,-10,3,-1,-3,1,6,4,-1,-6,9,3,-4,-9,6,4,10,10,-3,-10,-10,10,9,5,-3,8,-2,5,7,-5,-8,10,2,-1,5,-5,-2,-10,-7,8,7,-1,8,-7,9,-8,10,7,10,-6,1,1,-4,-4,-5,2,-10,-2,-8,1,-10,6,-9,-9,1,5,7,-5,6,-6,4,4,3,-2,5,-8,-4,-5,7,3,1,10,-5,-1,-6,3,-6,-4,3,10,1,4,-2,10,5,7,-3,-4,-6,9,-1,-2,7,6,3,-1,3,10,6,-3,5,-7,-1,-5,5,8,6,4,7,-5,-5,-5,-4,4,-6,3,8,-10,-10,-5,10,-2,3,-10,-8,-1,1,-3,-10,7,3,7,-7,-2,3,3,-1,8,10,4,-4,3,8,2,-1,6,-6,-9,2,-1,1,8,8,-7,5,8,-6,-5,-7,6,6,5,-7,-7,8,-5,2,2,-9,-10,-2,-6,-1,5,-7,-7,-3,5,7,-8,-9,-5,-6,3,-7,2,3,-8,-8,-2,1,8,-2,-1,-2,-3,4,2,-4,-5,-9,-10,4,7,-8,7,-10,1,-7,-10,-3,-1,-8,7,9,-3,-9,-1,9,-5,10,-6,8,-2,-2,-5,5,4,-1,7,10,-8,-3,2,-8,-10,-10,9,-6,4,-3,-4,6,-2,-8,-7,-9,9,-4,7,-7,-8,-5,-6,10,-8,-2,-1,-2,-5,2,-9,7,-6,-1,2,-1,-7,-9,-7,5,-2,-10,5,-6,2,-4,-2,1,3,10,-9,8,-9,-1,6,4,4,10,5,4,3,-10,-1,2,10,1,-5,7,6,10,5,1,-9,-1,-5,2,2,-5,-1,-9,1,4,9,-1,9,-10,-7,-4,-1,1,-9,-6,-4,-4,-7,8,2,-3,-3,-9,-6,-7,-7,-9,5,4,2,-2,2,1,-8,-7,-3,3,-5,-8,-1,-3,-3,9,-2,-9,5,-1,9,6,3,10,-2,-1,7,-7,4,7,4,-7,-10,-1,10,-2,3,8,1,-1,-3,9,2,8,-8,5,-2,-6,-9,-7,-8,9,9,7,-3,3,1,-6,8,10,9,-7,6,-1,-10,-5,9,2,-1,-8,-9,2,2,4,-10,-7,-10,9,-8,2,-1,8,10,10,1,8,8,10,6,2,-10,6,-3,-3,-7,1,-3,10,1,7,-7,-1,-4,6,9,-7,-7,7,10,-3,7,7,-2,-5,8,-6,8,-1,-2,-2,5,8,-4,1,6,-3,7,5,8,4,-4,4,-10,2,-3,1,-4,9,-5,-2,-6,4,-4,5,-10,1,-1,-6,9,3,2,10,-4,-4,9,9,-8,9,5,5,4,9,-10,-8,-3,-2,4,1,-1,6,10,5,2,1,1,3,3,-3,-5,3,-10,2,-5,4,7,-5,-7,4,-8,7,2,-7,9,9,10,1,5,6,6,7,9,-10,-6,-8,-1,4,-4,-8,10,9,9,10,5,5,5,3,-6,10,7,-6,2,2,2,1,9,-2,1,-2,1,6,-9,-9,3,-9,-9,1,-7,-9,4,1,-9,-2,8,-7,-1,-4,-3,7,6,10,-1,9,3,6,-10,-3,-1,-1,6,9,-2,-8,-8,3,-1,1,4,-7,-10,6,-10,-8,3,2,-7,7,-4,4,-9,7,-10,9,8,2,-1,-7,1,-5,-5,4,-8,1,5,5,4,4,-8,-9,1,6,4,-6,-9,7,-8,7,-1,9,4,10,3,2,-6,-2,4,2,9,1,9,-3,-1,4,-9,-8,8,-2,1,-4,5,-6,4,-7,6,-3,7,3,-6,-10,3,-7,5,1,3,4,3,-9,8,2,-5,10,-10,-2,1,1,-9,4,-10,-1,-2,3,7,-4,9,10,10,-9,-4,-7,2,-10,10,6,-10,-3,6,-8,9,7,-8,3,8,8,-3,-8,5,-6,1,-5,3,-3,-3,1,5,-1,6,8,-5,3,-1,3,-8,-1,4,-9,-3,5,5,9,5,-2,-3,2,-7,8,-7,-6,-9,-5,-4,-2,-9,2,-5,4,8,-1,-6,-8,2,-5,-6,-6,-9,-10,5,7,-10,-8,9,-5,7,7,-2,10,-3,-3,-5,6,9,-6,-7,-8,3,2,-9,-10,-4,4,4,-10,-9,5,-1,10,8,-4,-3,2,10,10,4,10,7,-3,-7,7,5,2,5,-6,9,8,2,-10,7,-4,7,8,-5,4,-6,-10,5,7,-5,2,2,-8,1,7,-7,6,2,-10,5,-10,7,1,5,1,-10,-6,3,7,3,2,4,5,-2,-6,3,5,8,-1,4,3,-6,-10,-4,-5,-2,8,-4,3,-10,-10,-5,-2,-3,-7,8,4,-10,5,1,2,8,1,-5,-6,5,9,-3,4,7,-6,3,10,-4,9,6,1,3,4,6,4,-7,3,5,9,-1,6,-5,-7,-1,6,-10,-1,-9,-1,-6,8,8,-5,-9,5,-9,3,-7,-3,-9,-8,-6,-1,4,9,5,-3,-7,5,5,5,1,8,-8,-8,1,-5,-5,-1,-6,-10,8,-5,-4,-4,-10,-2,6,-3,-4,3,-9,4,5,-4,8,4,-7,-2,1,7,4,6,-1,6,10,-3,-8,-2,10,3,-7,-5,-8,-5,-4,2,-6,-10,7,-2,-3,-5,-2,3,-2,2,-5,-8,-4,4,7,-6,6,10,9,-2,9,-5,-6,-2,5,2,9,-5,-10,10,6,-8,1,-8,2,-5,7,9,-10,-2,5,7,1,-8,2,10,-4,-10,8,5,8,-8,-2,6,8,-7,1,6,7,-5,-1,-6,-3,10,-4,9,5,-7,-4,10,-5,2,2,-10,-1,-7,9,-5,-10,6,-2,-8,-4,-5,-1,10,-2,2,10,5,6,-4,-5,-9,-6,1,-2,4,-5,4,-3,-2,7,-1,5,-10,7,-7,-5,-7,3,-8,8,-1,-2,-1,-9,2,-6,-7,-10,-3,3,9,-8,8,6,-6,-1,-1,4,-9,-4,1,5,-2,-4,-2,-3,-4,7,2,-9,10,-7,-2,3,-4,-4,9,-2,6,4,-3,-7,9,1,7,-2,-10,8,-8,3,7,6,9,-7,-5,1,9,5,3,-1,-5,-7,-2,7,5,-3,-1,8,-8,-5,5,1,5,4,-3,8,8,3,10,1,3,-8,2,4,-1,10,-6,-10,8,-9,-8,9,2,-5,3,10,7,-10,-5,8,-5,4,9,10,-7,-8,-8,9,8,-4,10,-9,-5,-8,5,-8,6,10,5,5,-3,-5,10,10,-9,-9,2,10,8,8,5,4,8,-7,7,3,4,10,-3,2,-9,-5,-8,8,2,-1,-6,8,-10,6,-8,-9,8,-6,4,-7,6,3,6,2,-1,-6,-10,10,-9,9,-7,10,10,10,-4,4,-8,8,2,3,4,10,-2,-2,-7,10,1,-1,8,2,8,-3,-5,-10,10,-2,-3,-6,3,7,1,7,-1,-1,-10,10,1,2,-2,-4,-8,-7,-9,5,1,5,3,-3,10,1,9,6,5,-7,-2,1,7,10,-1,9,9,5,6,4,4,-6,9,2,-1,4,1,-3,5,4,10,-9,9,-1,-2,3,-2,-8,10,-8,-8,-4,8,-7,5,-9,9,6,-2,5,3,9,-8,8,-6,8,-7,-2,4,-9,5,3,-8,1,5,-3,7,-4,8,2,-6,-7,-7,-9,-2,-9,6,10,1,3,9,-4,1,-1,8,2,-6,-9,2,5,4,-1,-7,6,4,6,9,-10,-8,9,6,1,2,6,-8,10,-4,4,-3,9,-10,-1,-5,-7,-3,10,-10,1,3,-8,8,-2,-2,-4,-7,-4,-8,-3,-7,-5,-9,-10,-7,2,10,-10,-1,-1,-9,10,5,-2,-9,5,7,10,4,6,-3,-1,10,9,4,-4,2,10,8,-2,8,4,-7,3,6,-3,10,10,-5,-3,1,-5,-1,-2,-6,-7,2,-10,-8,2,-6,1,-9,8,-3,7,10,9,-7,-2,7,-9,-1,-10,4,2,-7,6,7,-1,4,-4,-10,-6,6,-1,-7,4,9,-6,-5,5,-3,-7,-4,1,-10,4,10,8,10,-10,10,-7,-7,-4,-3,-4,1,-7,4,4,-6,4,2,3,3,-1,7,-4,2,9,-8,-2,-6,3,-10,4,7,4,-1,-1,2,9,-9,6,-10,7,-9,6,-1,-5,-8,-6,8,4,9,-8,-9,-10,10,2,-2,10,1,7,7,-2,1,-1,10,-2,3,7,7,-4,5,6,6,-9,4,-8,5,5,10,9,-1,8,-1,8,6,2,8,9,4,1,-3,8,-1,-6,-10,4,5,5,-10,-3,-3,-6,-5,-4,-4,-6,8,-4,10,3,-6,9,-8,7,-7,2,7,2,-6,10,5,-6,-3,-1,10,-1,8,8,-6,4,7,-5,8,4,-6,-4,2,4,-10,-6,-9,-9,-7,-7,-1,-6,8,3,-1,-10,3,9,-3,3,-10,-4,-8,-7,9,7,4,-10,-9,10,2,-8,-5,-4,-10,4,6,8,-2,-8,-9,-2,-10,-9,5,-8,1,-6,3,-7,-5,-2,10,4,4,-2,6,-8,-6,7,6,10,1,4,-4,-6,3,-1,-7,4,4,4,9,8,9,-9,-1,2,7,-6,8,-1,10,-3,-4,6,-2,9,2,-7,5,4,6,-7,-2,3,3,-3,7,-9,3,-10,6,8], dtype = "int8")#candidate|5797|(3150,)|const|int8
bop_5798 = relay.bitwise_or(call_5771.astype('uint8'), relay.reshape(const_5797.astype('uint8'), relay.shape_of(call_5771))) # shape=(3150,)
bop_5801 = relay.bitwise_or(call_5772.astype('uint8'), relay.reshape(const_5797.astype('uint8'), relay.shape_of(call_5772))) # shape=(3150,)
output = bop_5798
output2 = bop_5801
func_5806 = relay.Function([], output)
mod['func_5806'] = func_5806
mod = relay.transform.InferType()(mod)
output = func_5806()
func_5807 = relay.Function([], output)
mutated_mod['func_5807'] = func_5807
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5813 = relay.var("var_5813", dtype = "float64", shape = (6, 2, 5))#candidate|5813|(6, 2, 5)|var|float64
uop_5814 = relay.atan(var_5813.astype('float64')) # shape=(6, 2, 5)
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_5824 = relay.TupleGetItem(func_3457_call(), 3)
call_5825 = relay.TupleGetItem(func_3459_call(), 3)
output = relay.Tuple([uop_5814,call_5824,])
output2 = relay.Tuple([uop_5814,call_5825,])
func_5829 = relay.Function([var_5813,], output)
mod['func_5829'] = func_5829
mod = relay.transform.InferType()(mod)
mutated_mod['func_5829'] = func_5829
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5830 = relay.var("var_5830", dtype = "float64", shape = (6, 2, 5))#candidate|5830|(6, 2, 5)|var|float64
func_5829_call = mutated_mod.get_global_var('func_5829')
call_5831 = func_5829_call(var_5830)
output = call_5831
func_5832 = relay.Function([var_5830], output)
mutated_mod['func_5832'] = func_5832
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5846 = relay.var("var_5846", dtype = "float32", shape = (10, 2, 10))#candidate|5846|(10, 2, 10)|var|float32
var_5847 = relay.var("var_5847", dtype = "float32", shape = (10, 2, 10))#candidate|5847|(10, 2, 10)|var|float32
bop_5848 = relay.power(var_5846.astype('float32'), relay.reshape(var_5847.astype('float32'), relay.shape_of(var_5846))) # shape=(10, 2, 10)
output = relay.Tuple([bop_5848,])
output2 = relay.Tuple([bop_5848,])
func_5866 = relay.Function([var_5846,var_5847,], output)
mod['func_5866'] = func_5866
mod = relay.transform.InferType()(mod)
var_5867 = relay.var("var_5867", dtype = "float32", shape = (10, 2, 10))#candidate|5867|(10, 2, 10)|var|float32
var_5868 = relay.var("var_5868", dtype = "float32", shape = (10, 2, 10))#candidate|5868|(10, 2, 10)|var|float32
output = func_5866(var_5867,var_5868,)
func_5869 = relay.Function([var_5867,var_5868,], output)
mutated_mod['func_5869'] = func_5869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mod.get_global_var('func_3905')
func_3907_call = mutated_mod.get_global_var('func_3907')
call_5883 = relay.TupleGetItem(func_3905_call(), 0)
call_5884 = relay.TupleGetItem(func_3907_call(), 0)
func_3829_call = mod.get_global_var('func_3829')
func_3832_call = mutated_mod.get_global_var('func_3832')
var_5888 = relay.var("var_5888", dtype = "float32", shape = (70, 9))#candidate|5888|(70, 9)|var|float32
call_5887 = relay.TupleGetItem(func_3829_call(relay.reshape(var_5888.astype('float32'), [630,])), 1)
call_5889 = relay.TupleGetItem(func_3832_call(relay.reshape(var_5888.astype('float32'), [630,])), 1)
func_5139_call = mod.get_global_var('func_5139')
func_5141_call = mutated_mod.get_global_var('func_5141')
call_5900 = func_5139_call()
call_5901 = func_5139_call()
func_4858_call = mod.get_global_var('func_4858')
func_4862_call = mutated_mod.get_global_var('func_4862')
const_5913 = relay.const([-0.573812,6.068799,1.626026,-6.527138,-0.473022,6.383002,1.387323,-1.282642,-7.952375,5.204121,-4.837722,7.069202,5.348531,1.057407,0.113635,-9.112184,1.408918,-9.005788,-6.232030,-5.847646,-7.942864,-5.051729,9.742028,-8.474720,-4.621930,-9.036496,1.705659,3.173794,9.483720,4.111454,-0.565901,-8.778837,-7.233672,-2.335759,2.894725,6.355153,-4.339698,-9.087285,4.438111,3.963973,-2.744595,-7.550081,7.217984,-4.219637,-0.710882,-5.919827,-2.028046,-7.342758,9.431224,2.362450,-6.450556,-5.548575,-0.852053,-9.847949,-0.865692,-7.809749,2.738838,-0.295119,-3.869355,-4.437382,6.691816,3.285760,8.844058,-0.893717,5.838067,-2.214646,-1.072707,-7.677406,6.652694,-8.522815,0.649486,-7.327636,2.531466,2.433720,-6.721905,3.112497,-0.540262,8.145914,-3.180823,-9.122372,4.969485,0.897489,-5.626181,-4.923802,5.575211,6.341742,1.451371,3.330818,-6.142189,9.445533,-0.236072,-2.048040,5.616093,3.176401,1.729837,3.016337,-4.148669,4.886111,7.773658,-6.465316,-8.248091,8.729235,5.216298,9.718951,0.685332,-1.021040,5.529644,1.602952,-9.444178,-7.996751,-3.442501,-2.464367,2.082097,5.323881,-6.609886,0.044855,8.703205,-5.445274,6.515444,1.116268,-1.648201,1.951184,-0.231018,0.381962,4.444319,0.979082,2.764554,-7.805345,6.165482,0.608141,5.065741,-9.319543,1.601527,2.312079,-7.664182,-4.899431,4.877330,-1.065565,-3.963853,-9.036591,-6.390414,9.356763,-3.345257,-2.312739,-2.599845,8.557403,-0.316671,-6.822125,-5.006596,-1.931179,-4.928808,-1.753164,-1.672362,-7.839364,-1.086172,-7.281183,-8.330423,-8.489202,3.101250,-8.215939,4.368367,3.404682,2.633355,5.869130,-0.457195,4.117597,-5.690498,-8.625302,-7.598507,0.157498,3.682471,9.728451,-0.192247,-1.380523,-5.305346,2.342428,-7.013402,3.597610,-2.295199,-5.487233,8.208726,-3.341263,1.332189,-6.151511,6.453816,-6.721678,-1.707021,-8.409512,1.875230,-8.790810,4.478645,4.060173,0.663324,1.987382,-4.305304,-6.374602,9.348144,6.099994,9.889985,5.244754,-5.046385,9.617614,5.752877,8.485694,7.735081,6.394880,4.655005,-2.150048,7.357773,-8.696037,5.913181,0.618357,3.460947,8.735887,7.133166,9.728144,-5.665874,-1.459870,-1.607520,5.689699,9.464817,-7.299051,3.409512,0.560351,0.030059,-7.716671,-1.373274,5.070810,2.266397,-5.657297,9.264134,-4.372696,2.821745,-8.601004,-2.640776,9.335461,-0.234628,-9.878175,-7.383046,-4.991800,2.249290,4.879962,2.012233,-1.307169,6.594854,5.644194,-1.463754,9.335516,-4.790503,-4.637774,7.479045,-8.281121,4.993025,2.225192,8.907465,5.533254,5.451739,-5.580664,-0.472011,0.654196,-8.797487,-5.633356,-1.499060,-6.819722,8.454228,1.815345,-0.118308,-3.947174,-7.460037,0.961769,-2.464717,-1.275935,9.886121,-3.582105,6.068685,-4.386759,-8.603151,7.326067,-3.958624,6.691295,-6.539798,-5.548776,-8.083639,-2.514046,-2.992345,-2.483313,9.248089,-7.538403,-7.564250,-3.558178,-3.772092,6.184536,5.900054,1.561872,-8.011478,-8.682659,2.754118,1.849435,7.051673,-1.960827,1.023623,-8.192512,-5.126639,-3.409256,9.127245,-0.106081,2.194146,-8.781721,-2.484014,-9.407384,-6.081387,2.459334,2.598136,-9.826448,9.008851,-4.010783,4.197484,6.134660,-3.068544,-2.533717,-0.608667,8.536816,-5.759376,-8.119423,-6.085442,9.687766,7.266214,-3.201300,8.145297,-5.973984,-9.633643,-3.838812,5.285937,8.706590,0.627410,-4.605225,-5.508374,2.263934,1.961430,-5.219422,-6.345228,7.757539,-4.236689,-5.293149,-2.326183,-5.874393,0.865204,-2.223743,-9.230368,-3.806207,-3.189831,0.892903,3.610708,9.020342,3.160877,-9.466743,-8.363382,2.962639,0.535060,-1.650383,-9.068264,-0.096407,3.111967,8.339861,-5.594893,3.463843,-3.015407,-0.583591,7.831720,-9.423525,3.747158,-8.075648,-6.370467,-1.438828,2.803195,6.649704,-9.490509,-3.511134,3.135047,9.537694,9.316915,-8.664914,-1.020091,0.654143,-1.323836,-9.561266,-4.860587,7.376320,-1.828719,9.668933,2.505351,-4.742645,-4.422002,5.613589,-3.225982,-7.634307,-2.230931,5.032760,8.766738,-3.341614,-8.756197,0.749687,-9.212346,-0.322404,-9.231700,-6.471295,-6.568653,5.982708,2.165115,-2.814540,-3.404267,-6.232767,4.891620,2.207525,-9.873085,8.575431,-2.515444,-3.219115,6.923873,7.493322,-8.652348,5.075459,-8.552952,8.960536,-3.952253,4.118359,-4.882931,8.284414,6.375278,-1.989468,-7.624037,7.888800,-8.124030,7.869603,-6.969695,-0.153679,6.101706,9.357250,-1.841777,2.272590,3.130030,6.009078,-9.592638,9.372851,9.021650,-4.889325,5.108128,-2.155038,6.090530,-3.430063,1.801883,-2.520444,-1.635489,-9.627697,-0.988671,3.722654,2.970397,-1.450248,9.301125,4.588903,2.160317,2.456121,6.807761,2.729661,5.747481,-2.968241,-0.443604,8.300779,9.213952,6.915622,-4.415766,0.120684,-0.682829,2.627121,8.679010,-5.149503,-1.248777,-6.401981,-9.769225,-7.923748,2.533015,-3.716955,5.117775,-2.888363,9.027402,9.298818,1.018944,7.850183,-7.766794,9.231968,-2.382387,-2.993007,5.249252,-0.910207,-5.641199,-2.445781,-4.447968,0.031985,-0.330805,-6.724943,-3.729293,2.042573,-6.450371,6.913819,-0.232496,-1.879057,-3.348756,5.676765,9.154169,7.595578,5.445799,6.808499,-5.838607,1.300388,3.740211,5.933768,1.650893,9.007116,6.030187,-4.891067,2.098620,-5.469874,-9.342959,-7.368029,-7.628038,1.608955,4.507986,8.367175,-4.555894,-8.798122,-9.122166,4.047687,8.796959,8.809540,7.964067,-7.193152,-5.733150,-7.478308,-0.349171,7.162470,2.348235,-2.704575,1.467207,-5.787663,6.209307,0.039379,-5.820073,9.345169,4.492491,9.555321,2.565594,-7.060075,-5.259176,-9.917363,8.717979,3.600525,-5.303028,5.102790,0.236420,1.416189,-8.230148,-9.441974,1.765593,-6.105506,-1.700694,0.412748,4.417867,-9.219701,1.989984,1.874989,-9.465248,3.079296,-2.438795,-9.493125,-9.243548,-9.022548,5.398680,-8.084642,1.576221,2.141008,-7.501403,0.831795,-4.629722,5.196708,-5.572507,-7.599731,-7.225102,7.224151,-3.675195,-5.133536,-4.033243,-3.208088,-4.702243,-4.836984,1.715635,7.799013,7.840998,-6.452563,-0.933615,1.024428,-0.600681,1.634094,1.217425,9.395967,6.889813,-2.129277,4.088189,4.088779,2.560933,6.320241,6.825841,-1.936314,5.311267,6.534917,8.983435,-8.138099,-2.583355,-2.760518,-1.488831,-6.318302,5.112154,7.071101,1.624032,-1.054105,8.574928,9.958412,2.690945,4.585460,-2.544725,-2.811083,2.390915,9.016359,6.565763,9.326228,-6.203731,1.848043,-8.380378,-5.234293,0.681716,9.475625,-6.609227,4.770321,-4.956470,-5.415598,3.597693,-3.404530,3.898374,8.830884,9.264360,-1.093197,-0.476406,-3.647699,8.717124,-1.453692,9.029521,7.605499,-7.531356,9.377115,3.416675,-6.568192,9.028820,1.705112,-6.273544,6.247218,7.500214,6.248924,5.410961,-0.924195,-7.000897,4.126778,-2.182402,1.643912,5.272900,-9.876817,-4.932291,-7.171598,3.283590,-9.746986,-7.934284,-0.413657,-3.197448,0.485447,3.873689,-3.808393,-8.448498,4.594367,-5.492705,2.128810,-1.476278,-1.728519,-9.447313,-5.080927,-2.652588,-3.208377,-2.013140,-5.129073,-0.616533,-8.862855,9.264701,-3.710760,-2.824508,4.634291,-1.551940,-4.682495,-7.749810,-9.874638,3.559438,-9.193434,0.627196,-1.618194,3.602510,-5.787580,-8.446987,5.738164,1.244286,3.754123,-1.447754,-0.877063,-5.704934,0.764752,5.463398,1.997226,-3.238344,-4.292486,-0.897119,0.619357,4.775552,-7.692152,-5.393261,-2.995642,9.613139,1.222576,-4.066950,-0.015963,-2.864652,4.861975,9.687986,6.155436,-7.815134,-8.204168,-2.938210,6.895986,3.997609,-3.358194,7.211303,-1.966942,-8.414963,-8.822155,4.120747,0.163452,-3.457882,-9.377558,-4.659220,4.434154,3.677398,4.606118,0.524761,-9.770294,-2.080053,-5.562463,7.761549,-0.789123,-8.246737,-7.787746,-6.840272,-4.883020,-8.075732,-1.730534,-8.234710,7.452479,7.911264,7.564179,2.124436,-5.290520,-1.374698,-9.511965,9.988360,-2.308541,9.099116,6.570371,-5.325594,9.108341,-8.402486,9.219825,4.325423,3.216066,-1.523993,-9.287310,-4.471041,1.938457,1.605345,-0.611363,9.835560,6.106999,6.438340,-5.961782,-5.054977,-3.134812,1.063394,9.219230,-7.996877,-1.958957,5.577145,8.961798,9.227293,5.132676,-7.347839,8.363524,-4.089911,-8.479840,0.007852,3.129731,-2.727863,7.717877,-4.658618,0.763822,6.632867,2.312906,-9.471471,-2.409846,8.999090,-1.337415,8.936882,5.007318,-3.767513,8.575312,-0.724133,4.282812,-8.448139,7.784435,0.642826,3.366427,-3.192407,-6.237753,9.938477,-2.635587,-8.336976,-2.248084,-1.365905,0.344391,-6.953153,-0.662386,7.238663,2.567757,-1.591953,-7.508050,9.437938,-6.779726,-5.729824,-1.879024,9.705194,4.254879,-5.103518,2.967095,2.645658,6.934438,5.088881,8.664525,-3.725382,-7.991147,8.375116,-7.564957,2.847656,-5.861926,3.536188,8.700454,8.329955,-3.979451,9.476239,-4.893965,-9.045174,-7.501107,5.419406,3.166442,-7.577983,0.019324,-4.889548,0.003625,-7.920406,-3.061699,-4.509779,4.411008,-4.737328,1.709173,7.047963,-8.618530,-9.048465,-4.915930,-0.100938,2.184747,1.677555,-6.713349,-6.989876,3.802859,1.938226,1.028218,-2.423821,4.164820,-2.996244,-9.275956,-5.832182,-4.360671,7.775111,7.841150,-5.860173,-4.500551,2.915151,5.313520,-9.015063,-6.410000,-5.907099,-9.867927,-9.054293,1.564521,-8.563088,5.306873,2.167462,7.318868,-4.806480,-2.494504,1.555650,-0.874479,-6.128602,2.262601,5.265522,-4.948376,1.845046,-6.236056,8.449387,-0.733537,1.149173,-5.631275,6.151872,7.642359,-3.242221,-7.891232,-0.919243,-0.437725,3.045440,-9.466582,-2.219333,-8.170832,8.577161,4.369241,4.401890,-1.133558,5.642458,4.005249,2.813476,-1.597331,-3.180652,6.849628,-0.579533,5.177332,3.538339,-9.211322,8.904829,2.770136,0.949820,5.089202,4.530750,7.861281,-6.038071,6.983717,1.141798,-9.771068,4.981623,-3.476788,8.252667,6.296044,1.582901,-2.614275,-0.247773,4.474650,7.664810,-7.260478,4.547899,8.307500,-3.182074,5.899525,7.615283,-2.317727,4.706324,-9.200964,-3.210713,-8.564637,8.320686,-8.648164,-6.199854,0.457858,-1.649339,-7.893723,7.672794,-1.135954,2.187951,5.063721,8.501382,1.681714,-9.974470,9.653149,8.688868,2.809950,7.588853,-1.311387,7.830975,3.150869,-6.297707,5.293629,1.255713,8.323668,1.043053,5.889950,-3.296919,-0.103596,-6.345780,-3.356857,8.938467,-0.288548,4.709759,-6.049155,-6.044410,5.585949,-4.248485,-9.158681,-9.867337,-7.204437,-1.280476,-1.388200,-9.446544,-1.665070,-8.877495,-2.165453,-9.479238,-3.832485,3.365103,-1.992926,-1.275186,-1.647682,5.480700,8.700888,5.524122,6.970495,5.306040,-0.245503,-4.807978,5.339885,8.344239,-3.609595,-0.363514,-3.509193,-9.627796,-5.827655,-6.646219,0.229790,9.666977,9.589799,-8.693438,9.474792,-4.249098,6.230157,-5.100393,9.933172,-9.078431,3.341236,2.196702,-2.237074,-0.994231,-7.034550,-7.996448,-0.270464,-5.914437,-3.036139,0.617896,2.869674,0.159621,-4.283192,1.852401,-0.163341,-0.649242,-5.609356,6.103299,0.891732,1.983400,-6.262990,8.768301,-4.153322,-3.629065,-3.376582,-7.458835,5.996312,-4.541774,2.052131,2.701416,0.480690,2.060342,8.670110,-5.173562,-6.398589,1.446311,6.994817,-9.509825,-4.678977,-8.263801,-8.760735,-4.925226,4.034925,2.695315,-1.991039,-5.723473,-7.434575,-9.825847,-9.254794,-5.885192,-8.630248,0.700141,-7.955580,6.237005,-8.044346,9.985683,-4.864230,-3.933661,-9.432311,-0.648761,-5.340791,-4.007824,-0.864856,7.946038,-0.988392,-4.071390,7.395252,-0.205309,0.531214,-9.729357,-4.883591,-9.212818,-3.721726,-1.139571,-1.488649,9.214566,6.194080,-1.514802,-3.912189,-4.644494,6.753502,-5.254011,-4.295900,9.759085,-3.284417,5.580177,8.863916,-7.819891,-1.596006,9.352206,4.950619,6.295920,-9.259583,2.061481,5.963096,0.398756,-9.446441,1.519583,5.712018,-4.520758,7.330026,-6.476734,4.099059,-2.669808,6.837796,-3.264893,-2.526327,5.092926,0.831180,-6.077371,-1.467132,-9.407377,3.976569,0.141078,-2.725835,-0.811573,1.453601,-5.019776,8.202625,-9.614468,-0.057192,-9.503399,-9.932401,-9.623056,-0.725876,1.175269,-5.648082,4.292853,1.927215,-7.157250,-0.394507,5.850365,3.600440,-3.350322,-4.584145,6.893060,0.925842,-6.967732,8.300969,-3.325767,3.623141,-7.904573,6.917876,7.131898,-8.775016,-1.945971,-6.698833,-0.698622,9.708501,5.775759,9.283992,6.951940,-0.628174,0.742704,-6.609635,9.270644,5.502914,9.023582,1.284023,6.311706,9.874079,-9.955850,-7.810577,0.811697,7.641791,1.904876,-1.638457,2.039501,-8.272621,-4.938825,-9.315341,-1.154505,-7.028468,-8.331992,-6.872939,9.996448,9.268304,-7.828810,5.591340,-1.669096,-1.046613,3.288658,-0.770943,9.907856,3.791153,7.544081,1.443954,3.603813,7.419669,7.148702,-6.522533,8.525883,-5.918837,2.702557,-0.043945,-0.947370,4.507014,7.110209,-7.088396,1.717223,-7.523628,-3.040313,-0.803348,7.143025,5.651554,-6.916938,-3.110357,-6.615380,1.783300,-6.161980,1.935390,-3.977032,-0.870976,-0.614872,-3.652700,4.620682,-4.973874,-9.993238,4.182590,-6.067932,-9.915942,-4.963364,7.401677,0.151202,-5.324704,-2.671243,-4.914831,9.631805,-1.824144,0.397251,3.393041,4.417675,-6.365770,-2.121151,-9.924868,9.066230,4.445628,5.306754,-0.589955,6.980557,-0.882630,-0.087567,-1.848475,7.576844,9.908825,7.923781,3.464067,-5.773875,-6.628212,-2.511309,9.390488,7.582342,7.651373,2.208434,5.148856,0.757853,-9.035587,-7.812828,9.366213,2.847304,2.088172,2.692476,-7.963670,-7.680377,-3.958827,1.989168,-3.350860,2.902577,4.053182,7.619782,4.886058,-9.604072,-2.162237,4.500211,-6.514994,-3.649634,5.939247,7.454335,9.621237,9.255905,-9.948937,-2.205630,8.730294,-6.424574,-2.433298,-4.991132,-9.029832,-6.077904,1.999415,-6.919923,-7.774547,8.314007,-2.106981,5.661247,8.315667,-6.017953,8.902623,-5.453128,-8.428854,0.119262,3.909770,-9.357960,-8.329396,-0.596346,-4.152730,-3.017311,-8.081006,8.415058,-8.692321,-4.950693,2.744564,5.647161,4.888273,6.353071,-2.239016,9.728223,-7.258179,-8.018761,-5.287533,1.451238,0.206324,8.645090,1.206424,0.762580,-5.349130,8.383482,-3.375749,-2.294301,6.695987,8.582842,3.247238,2.480138,-5.092484,-1.600197,-9.911359,-3.823858,7.526867,4.341757,-6.741769,-4.075212,2.912463,-0.040845,-6.418765,1.876928,-1.389758,-0.299077,6.245171,-7.854220,1.315193,-3.766982,-7.565690,4.543549,9.147232,-4.042022,2.623737,-8.192003,3.172836,-8.844464,1.324049,7.538659,-6.465777,2.166469,4.339125,-1.390984,7.440843,-2.570657,4.867279,0.283464,7.816641,-5.539179,1.697185,4.609325,9.906266,-7.945286,5.884810,-9.469555,7.344171,-7.875649,9.498022,1.193413,8.875296,-7.668149,-1.496495,8.841107,-3.122290,-1.220122,-9.599218,-7.321911,-8.695170,2.937916,-1.487749,9.115636,9.538262,-6.162101,-9.437127,0.448553,5.976598,-6.408866,-1.437336,4.260158,8.569596,-7.703537,1.178420,4.676425,5.801370,-4.430090,4.118547], dtype = "float32")#candidate|5913|(1470,)|const|float32
var_5914 = relay.var("var_5914", dtype = "float32", shape = (72,))#candidate|5914|(72,)|var|float32
call_5912 = relay.TupleGetItem(func_4858_call(relay.reshape(const_5913.astype('float32'), [7, 15, 14]), relay.reshape(var_5914.astype('float32'), [72,]), ), 0)
call_5915 = relay.TupleGetItem(func_4862_call(relay.reshape(const_5913.astype('float32'), [7, 15, 14]), relay.reshape(var_5914.astype('float32'), [72,]), ), 0)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
var_5919 = relay.var("var_5919", dtype = "int8", shape = (900,))#candidate|5919|(900,)|var|int8
call_5918 = relay.TupleGetItem(func_2406_call(relay.reshape(var_5919.astype('int8'), [900,])), 0)
call_5920 = relay.TupleGetItem(func_2408_call(relay.reshape(var_5919.astype('int8'), [900,])), 0)
output = relay.Tuple([call_5883,call_5887,var_5888,call_5900,call_5912,const_5913,var_5914,call_5918,var_5919,])
output2 = relay.Tuple([call_5884,call_5889,var_5888,call_5901,call_5915,const_5913,var_5914,call_5920,var_5919,])
func_5924 = relay.Function([var_5888,var_5914,var_5919,], output)
mod['func_5924'] = func_5924
mod = relay.transform.InferType()(mod)
mutated_mod['func_5924'] = func_5924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5924_call = mutated_mod.get_global_var('func_5924')
var_5926 = relay.var("var_5926", dtype = "float32", shape = (70, 9))#candidate|5926|(70, 9)|var|float32
var_5927 = relay.var("var_5927", dtype = "float32", shape = (72,))#candidate|5927|(72,)|var|float32
var_5928 = relay.var("var_5928", dtype = "int8", shape = (900,))#candidate|5928|(900,)|var|int8
call_5925 = func_5924_call(var_5926,var_5927,var_5928,)
output = call_5925
func_5929 = relay.Function([var_5926,var_5927,var_5928,], output)
mutated_mod['func_5929'] = func_5929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4056_call = mod.get_global_var('func_4056')
func_4057_call = mutated_mod.get_global_var('func_4057')
call_5934 = relay.TupleGetItem(func_4056_call(), 1)
call_5935 = relay.TupleGetItem(func_4057_call(), 1)
uop_5939 = relay.asinh(call_5934.astype('float32')) # shape=(7, 15, 630)
uop_5941 = relay.asinh(call_5935.astype('float32')) # shape=(7, 15, 630)
bop_5946 = relay.left_shift(uop_5939.astype('int32'), relay.reshape(call_5934.astype('int32'), relay.shape_of(uop_5939))) # shape=(7, 15, 630)
bop_5949 = relay.left_shift(uop_5941.astype('int32'), relay.reshape(call_5935.astype('int32'), relay.shape_of(uop_5941))) # shape=(7, 15, 630)
func_5866_call = mod.get_global_var('func_5866')
func_5869_call = mutated_mod.get_global_var('func_5869')
var_5957 = relay.var("var_5957", dtype = "float32", shape = (200,))#candidate|5957|(200,)|var|float32
call_5956 = relay.TupleGetItem(func_5866_call(relay.reshape(var_5957.astype('float32'), [10, 2, 10]), relay.reshape(var_5957.astype('float32'), [10, 2, 10]), ), 0)
call_5958 = relay.TupleGetItem(func_5869_call(relay.reshape(var_5957.astype('float32'), [10, 2, 10]), relay.reshape(var_5957.astype('float32'), [10, 2, 10]), ), 0)
func_3457_call = mod.get_global_var('func_3457')
func_3459_call = mutated_mod.get_global_var('func_3459')
call_5965 = relay.TupleGetItem(func_3457_call(), 0)
call_5966 = relay.TupleGetItem(func_3459_call(), 0)
func_2836_call = mod.get_global_var('func_2836')
func_2840_call = mutated_mod.get_global_var('func_2840')
const_5973 = relay.const([[-2,10,6,-1,-9,-4,-4,-2,5,1,-4,1,-10,-8,8,1,-5,-10,-4,-9,-1,-7,-2,-5,5,-10,-7,-2,9,-4,-4,-9,-7,-7,3,3,3,-8,-2,-1,-1,5,-2,-4,5,-10,-4,-7,1,1,3,7,-5,8,-9,4,10,5,6,-4,9,1,6,-4,3,-10,-1,-2,-1,-4,1,-10,7,4,-7,6,6,-9,5,-9,9,7,-6,6,9,-10,10,-1,5,2,-8,10,-6,-8,4,-3,7,-5,-7,2,5,-6,10,-3,7,-9,-4,8,-1,4,4,-10,-5,5,8,-2,9,-7,7,6,-5,-6,-5,10,-1,-1,2,-7,8,3,-7,-8,-10,5,-5,1,7,9,-6,-10,-3,-1,4,-2,-9,-8,-9,-5,3,8,3,8,-9,-4,5,-1,6,-5,-1,3,-3,6,-9,-1,-1,2,8,-5,-6,3,4,-2,-7,3,4,-8,8,9,7,2,8,-1,4,5,-7,-3,-2,3,4,7,-3,6,-1,1,-4,-5,6,9,3,2,-2,-1,2,4,-2,-3,-6,-8,-2,4],[-1,8,-6,-1,-1,-7,8,5,-5,-3,10,4,4,4,9,2,8,1,-7,10,-5,-8,8,2,-4,8,2,-9,-4,-2,2,4,6,-3,8,-10,2,-6,3,2,5,-1,-4,3,5,10,1,-7,-9,-9,-6,10,7,8,3,7,-2,5,9,3,-3,-1,-6,3,-9,-4,3,2,-9,-2,-10,10,-9,7,1,4,-4,-2,3,8,10,-8,-8,-3,-1,-9,5,-5,2,-4,4,1,-3,10,8,10,2,9,8,-6,8,-4,-7,-9,2,4,-1,6,7,10,4,3,7,5,-5,-6,10,-10,-10,-6,2,2,6,-7,-6,10,6,7,5,-9,-4,-7,-7,-1,-6,1,8,1,-1,-9,-5,8,-10,5,6,-10,-10,-7,4,4,-7,-7,-8,1,7,6,-8,-5,9,6,5,8,-4,2,2,-7,-1,-8,-3,8,-8,3,-1,6,2,5,-9,3,-5,1,-1,10,3,10,-6,5,5,2,10,-5,-2,-8,-1,-6,5,8,8,-5,6,6,-4,-6,2,-6,-5,-3,-1,-2,3,1],[-7,-2,-6,7,-2,2,7,6,5,10,-5,9,-5,8,-8,5,-9,2,4,7,-4,4,6,-1,-4,-3,7,4,-2,1,3,-7,1,-10,-9,-10,6,8,-6,5,1,8,1,-1,4,2,8,-2,9,5,-8,2,-1,-8,-9,-4,2,-10,3,5,-5,-9,-6,-3,4,4,-5,6,7,10,4,10,-7,8,-4,-9,9,4,-10,2,-9,4,3,9,-1,-9,6,-2,10,2,4,-6,1,10,-1,5,-1,3,10,-5,2,7,-3,-8,2,10,-5,-1,-6,-10,-5,4,-6,9,8,7,10,-7,-7,-8,9,5,2,-10,6,7,5,-9,-10,-6,-4,10,9,9,-4,-2,-2,-5,-4,-5,5,4,-5,10,1,4,9,3,1,3,-6,-6,-4,5,6,-8,1,-2,5,2,9,5,-9,-5,8,-8,5,-5,5,-6,-9,5,-10,-8,8,-3,7,-5,6,-9,-10,-1,10,-5,-5,9,9,5,10,4,-3,-7,5,-9,3,-9,4,1,5,1,7,3,-6,3,10,-4,-4,-5,4,-4],[-1,-2,-3,1,9,8,-3,-1,-7,-3,-4,2,-9,-1,-1,9,-5,7,6,-6,9,10,-2,1,9,-8,4,-3,9,5,6,-1,7,-1,-5,9,-10,10,-3,-5,6,5,3,2,-9,-1,-10,-8,-10,3,7,-3,-2,2,3,-8,-9,8,1,6,-4,-7,-7,3,-5,5,10,-8,1,10,7,3,-2,-10,9,-5,2,9,-6,-7,1,-2,1,5,-1,-4,-4,-6,7,9,1,9,5,-3,2,-3,-3,6,-8,6,6,10,8,-6,4,-9,1,-10,-7,9,-4,-4,1,3,-1,-1,-10,8,-8,10,-2,-7,-10,1,-10,9,-5,3,5,7,6,4,8,-1,-8,6,-2,5,10,9,8,-5,1,1,7,-3,-6,8,-10,-10,-2,10,-9,-7,-3,-2,4,-4,-7,-2,-2,7,1,2,4,2,8,9,-9,10,-3,-4,10,-6,4,-1,-3,6,2,7,-10,2,-3,9,9,5,-10,1,-7,-6,4,-1,6,5,5,-3,-1,7,10,-5,3,-1,8,-2,-8,10,-8,3,6,9],[9,10,-1,-3,1,9,9,9,-3,-2,1,-5,3,-10,-5,2,-5,4,-7,8,-7,4,-9,1,3,-3,7,3,5,9,-6,-3,-3,-8,4,-8,3,6,4,1,3,2,-3,2,-10,-7,-3,-7,7,-5,-9,1,7,-3,-5,6,2,1,-5,-3,-5,-1,-3,5,2,-1,4,-7,9,2,8,-5,-8,-6,-9,-7,-1,5,7,-4,-1,-1,6,8,10,1,-1,-6,1,3,-1,8,-9,6,2,-4,-4,8,5,-7,-5,10,-3,5,8,-7,10,-3,-8,-4,10,1,-5,3,-4,-2,9,7,8,-9,1,9,1,10,-2,10,-2,-5,-4,6,9,9,2,1,1,8,5,-5,9,6,10,3,-10,1,-7,2,-7,-5,10,-10,-3,2,8,-4,3,-8,9,6,-8,-3,-8,-2,-7,-5,-10,-7,3,-10,-7,8,8,4,7,-7,1,-3,-7,3,9,-1,2,3,9,6,2,7,-4,-7,3,10,-4,-10,-6,-6,-8,8,-7,5,8,2,-9,-10,-10,-4,9,-4,4,5,-6,9],[-10,-5,-9,4,6,-7,-5,-8,2,-9,-5,-7,8,1,4,9,8,-2,-6,2,2,-7,-6,3,4,-10,-4,9,10,-5,1,-10,-10,4,1,-8,-5,4,-7,-9,1,-9,8,-7,10,-3,-8,8,7,3,-9,-5,-3,6,-5,10,-6,-1,9,-3,3,-9,-10,10,10,7,4,4,8,7,6,-1,8,-9,1,-5,-7,-7,3,4,9,-3,-1,10,8,5,5,-8,-10,-10,-8,-7,-1,-2,10,-8,-7,-3,7,-10,-3,10,-2,10,7,3,7,10,4,4,10,-6,2,-7,-5,5,3,5,-4,-9,5,6,-4,3,10,4,9,9,1,2,3,5,1,-3,-5,3,4,5,6,6,3,-8,-1,-6,2,-8,5,3,3,10,8,-1,5,-10,4,-8,5,-1,-6,-9,-5,5,2,6,4,5,-1,4,-2,6,-10,5,4,-4,-5,9,9,9,-2,7,3,9,8,-8,10,10,-10,-7,-1,3,1,-5,5,-2,-1,4,10,-7,-1,-3,-1,-10,6,-7,10,2,-1,-4,10,-5],[2,4,5,2,-6,-6,8,10,-5,10,7,9,-8,6,6,9,-3,1,4,-5,-10,7,-8,1,-2,-1,2,6,-10,10,-6,-5,1,6,-3,8,-1,-1,-2,4,-3,2,4,7,-4,1,5,-6,4,-4,4,-2,6,4,6,-1,-3,-6,5,-1,8,7,-6,2,9,-8,-7,-6,4,1,9,10,-7,7,8,10,-7,-1,-2,-6,-8,-3,-7,-10,-10,2,2,-1,8,10,-5,-4,-7,-9,8,1,-10,-3,-5,9,-3,-5,4,-4,4,-2,6,3,-3,-4,8,8,-2,-6,-3,10,-7,-1,-1,-7,10,-5,-5,2,1,-8,-3,-6,5,-10,8,-2,-7,7,-9,4,-4,-8,9,7,-3,-8,9,-1,-9,-5,-1,1,-2,-7,-5,-10,1,-9,7,-2,-1,9,6,8,-9,2,10,9,4,-2,-6,-1,2,9,8,-10,-2,2,-8,-5,1,-8,-3,-2,-10,9,9,-7,9,-10,7,-7,10,-9,10,-5,5,4,10,-6,-10,-10,-4,10,1,2,2,9,1,-10,3,-1,-9,-6],[-1,-1,5,2,6,-5,-3,-7,8,-7,-3,9,-4,-4,-5,4,-1,9,-6,-7,4,-3,1,-4,-5,6,-9,4,7,-6,6,-10,-7,-5,1,-9,-6,-4,10,5,-6,-5,-8,-8,-7,-9,8,-2,-10,10,-10,6,9,4,7,-9,2,10,1,7,4,-10,5,7,-8,-7,-8,-6,-5,10,-10,5,-1,4,-2,-9,-4,9,1,-5,7,-7,6,-3,4,3,10,-7,-2,2,-9,10,-10,-7,9,9,-5,-2,-10,2,-6,-7,2,7,5,7,10,1,10,-10,9,6,6,5,-3,-1,1,-7,-1,8,-4,2,-2,-4,1,3,3,-6,-7,6,-7,7,4,2,8,5,-4,-6,2,-1,5,-6,1,-1,10,-8,-6,-8,1,-8,-9,1,-2,2,-10,-8,6,5,-4,8,6,5,-1,10,3,10,-3,-7,-9,-8,1,4,-9,-7,-5,-1,10,-1,-8,-2,-3,5,3,-2,1,1,-7,9,4,-1,10,-2,-7,-1,5,6,-6,-5,-10,-1,-6,-3,7,-9,10,2,1,2,6,-2],[9,-3,6,-3,-5,-7,5,6,-4,3,-6,-5,8,6,3,8,-4,6,-9,6,1,8,5,-10,-10,6,9,-6,1,4,8,7,-3,1,9,-7,-5,8,9,-1,-2,-7,-8,-1,-5,-4,-7,4,-3,-1,6,-5,-10,-1,3,-10,-10,-10,-1,9,4,-8,4,10,-1,-10,-6,8,-9,7,-2,9,-3,10,9,-10,5,-5,-2,-6,5,-9,-10,9,5,-3,10,-9,-10,8,8,-2,10,2,2,4,-4,10,-10,-5,-2,10,-8,-6,-7,10,6,10,9,9,-2,1,-8,9,-10,2,1,-4,2,1,-8,-9,-1,2,3,-5,6,10,-9,-1,3,8,7,7,6,1,7,10,-8,-1,-4,7,-4,-6,-6,-1,2,7,3,-1,3,3,-3,-9,-5,-4,-9,-1,-8,6,-3,6,-8,7,8,2,-9,9,-8,-2,1,4,-7,-2,1,10,7,-9,9,-10,-3,6,9,-5,8,-10,5,6,8,-8,8,-2,4,-1,9,-9,4,-8,3,-10,1,7,-7,-10,2,3,-6,4,10,2],[-7,-6,6,-5,-5,9,6,-4,10,-7,1,-2,-9,-8,2,-2,1,-9,2,-8,-1,-5,-3,-2,-2,-7,3,2,4,2,-2,-4,-4,1,-8,-3,6,-6,6,3,-6,-2,10,10,-6,9,-9,-2,-7,-9,4,4,7,-10,-7,-2,5,-4,8,8,-10,-3,-1,2,-1,-3,-2,-6,8,-3,-1,1,-6,9,-1,-9,4,-10,8,3,4,4,-4,6,-6,-8,-3,-1,6,-5,8,5,-8,7,8,5,7,-7,-10,4,1,1,2,3,3,-4,1,-3,6,-5,9,6,9,-6,8,3,5,-3,7,5,-5,-10,-8,-7,10,-9,-2,-4,8,-10,-3,6,-8,-3,7,4,8,-8,7,-1,7,-8,2,-2,4,-7,-6,3,1,10,7,-8,9,9,3,-3,-9,1,-2,4,-6,5,3,7,-5,2,2,4,9,-5,5,-5,10,-8,1,-10,-2,-3,2,-8,9,-8,-1,-2,10,-3,7,1,-3,10,8,3,7,-4,-5,8,2,5,-10,4,-4,5,2,-9,-5,-9,2,-3,-7,8],[9,6,-1,7,-7,1,5,-5,2,-1,4,9,3,3,-1,2,6,-3,2,-8,8,-2,-5,-9,-10,5,-10,8,-8,-3,-3,-1,6,7,4,7,-7,7,6,1,6,-8,10,-2,-6,-9,2,9,6,4,-3,3,1,-4,-6,3,-2,-10,6,5,7,-2,-4,4,8,9,10,3,-4,8,-5,3,1,-2,-7,10,10,2,-2,-3,6,-2,-4,8,4,-9,5,6,7,-3,-4,-8,-5,-8,9,-7,-3,-1,-6,8,-5,8,-9,7,4,-10,-3,5,-1,4,6,4,2,10,-4,-7,5,10,2,10,7,6,-2,-5,6,4,-1,-3,4,1,2,-9,-7,-1,-8,5,-2,-7,-2,9,4,-9,-10,7,8,3,10,-6,-5,-6,-9,10,3,-8,-10,2,10,8,-8,7,-7,-5,-4,-3,-10,-4,1,-2,1,-1,9,-6,7,-3,1,10,-10,-4,-7,-3,-8,-8,3,5,-4,-7,-10,-3,7,1,-6,5,-5,10,7,-1,-2,-6,-10,7,7,-8,6,-5,7,-2,-6,-9,-7,-5],[2,-1,-4,7,10,-8,9,6,-7,-10,-9,-9,9,-8,-5,-3,8,1,-1,-5,-4,9,-9,3,-8,-2,5,-3,-9,3,5,-3,9,4,4,-2,2,-4,-8,9,-9,-4,2,3,10,5,3,8,-2,4,10,4,7,5,6,3,4,-4,-7,-8,-4,-2,-1,-10,1,-10,-10,-4,-6,-2,2,-10,3,5,-10,6,-5,2,7,2,-6,8,9,-2,-3,-7,-10,-1,2,4,8,7,-6,-3,3,-2,8,-6,4,-3,-2,1,-9,6,8,-3,-10,2,-3,9,-10,6,3,-6,2,3,10,-8,4,-10,6,1,-8,-1,9,7,-3,7,5,-2,-3,-2,6,-1,6,5,9,-7,2,-7,8,-10,7,6,1,10,10,6,-2,6,-10,-1,10,5,-3,-1,-6,-3,-8,-6,6,4,10,2,7,-1,1,-6,-7,3,3,3,4,-2,-5,-3,4,7,-7,5,8,-1,-7,2,-9,-6,-8,2,4,-6,2,-2,-9,10,7,-8,-3,-6,7,6,2,8,10,-3,4,5,-3,2,-3,5],[-2,-7,-3,7,2,8,3,3,6,8,-9,7,8,-1,-6,5,9,-2,6,2,1,1,6,7,-1,-5,8,2,1,-8,-8,-4,-6,1,6,-1,5,-2,7,-4,-4,1,-1,9,4,1,-2,-1,3,-2,5,-5,7,-1,7,-3,6,-3,6,-9,9,4,-6,2,9,8,9,-4,1,9,5,-10,-7,-6,-5,3,6,7,-4,-1,5,7,-3,8,-10,-5,-2,-6,6,-2,-8,6,4,-7,-2,-1,8,-1,-1,-8,-8,6,5,-9,-3,-3,5,6,-5,-10,-1,-4,-9,3,-5,-10,3,-3,5,9,-2,-6,6,-8,5,7,-9,9,7,-7,-3,5,3,4,9,-4,10,10,4,-4,-10,-8,-4,-8,-1,3,-3,1,6,4,9,-8,9,-2,10,3,6,8,10,-1,2,-4,2,-1,-1,6,2,-8,4,4,-7,-5,-8,-5,10,7,7,8,-9,8,5,-9,-9,-6,6,-8,-6,-7,9,-1,5,-2,-1,6,1,-9,9,1,-2,1,-8,-2,4,-9,1,-2,9,-3,-4,10],[2,-2,-5,6,-2,7,8,6,-1,4,4,2,-2,2,3,-3,-1,-5,10,6,-8,3,6,-9,4,-1,-1,-10,8,-1,5,-6,-1,-7,-2,-4,-7,8,6,-2,-3,7,-8,7,10,-8,3,3,5,-6,4,1,7,-5,-9,3,2,5,10,5,-1,-5,7,10,-10,2,8,-7,3,10,-1,-1,5,-2,-10,-5,1,7,1,-3,6,7,7,9,-6,-9,1,7,-7,-3,7,8,-7,8,-4,1,6,-4,-9,-10,-1,9,10,10,-8,-4,10,-5,-7,-6,-3,1,-4,2,-9,6,3,5,-5,3,-9,-8,-9,9,5,-6,-4,-8,5,10,2,5,-5,-1,7,-2,2,-7,-3,8,-4,6,3,-6,4,2,6,-1,10,-9,-7,3,-3,10,-9,-5,5,10,-5,-6,-4,5,10,9,10,-6,1,6,-2,-1,7,3,-7,-9,1,1,6,3,2,5,-2,-10,-4,8,-5,8,-6,3,6,-8,-7,-2,5,-10,-9,-10,8,5,-6,-8,5,2,-9,-7,-7,3,3,9,-3,6],[6,5,8,5,-3,5,-1,9,2,-4,-2,2,-2,-5,10,9,9,-9,1,9,9,4,-2,9,-1,-2,-9,8,7,-6,-5,2,-6,9,7,5,-3,-5,4,-9,-4,-7,7,-4,-9,1,5,7,8,-3,5,10,-7,-3,6,5,4,5,-9,8,-9,-3,-6,-10,-8,7,10,-9,2,-7,7,10,-8,-5,-4,-7,5,9,-2,-4,-1,2,-10,-8,7,1,-9,-5,6,6,-4,2,2,-9,-2,5,-7,5,-9,10,-10,8,-3,-8,3,-8,-4,-4,-2,3,7,-7,6,-2,5,-1,-6,-4,-1,8,4,-9,-6,9,8,-4,-1,-9,-1,1,4,10,-8,9,-7,-3,2,-1,9,-8,1,1,-1,10,1,9,-1,7,3,1,2,-1,8,-5,-4,-3,5,9,-2,9,10,1,8,3,4,3,7,-4,-8,3,2,-8,-8,4,-6,7,2,7,6,3,-3,-7,10,7,-10,1,6,10,6,8,-8,8,-3,-10,-5,10,-9,10,10,-9,-10,4,-10,2,10,-8,6,-8,10,-9]], dtype = "int8")#candidate|5973|(15, 210)|const|int8
call_5972 = relay.TupleGetItem(func_2836_call(relay.reshape(const_5973.astype('int8'), [15, 15, 14]), relay.reshape(const_5973.astype('int8'), [15, 15, 14]), ), 0)
call_5974 = relay.TupleGetItem(func_2840_call(relay.reshape(const_5973.astype('int8'), [15, 15, 14]), relay.reshape(const_5973.astype('int8'), [15, 15, 14]), ), 0)
output = relay.Tuple([bop_5946,call_5956,var_5957,call_5965,call_5972,const_5973,])
output2 = relay.Tuple([bop_5949,call_5958,var_5957,call_5966,call_5974,const_5973,])
func_5976 = relay.Function([var_5957,], output)
mod['func_5976'] = func_5976
mod = relay.transform.InferType()(mod)
var_5977 = relay.var("var_5977", dtype = "float32", shape = (200,))#candidate|5977|(200,)|var|float32
output = func_5976(var_5977)
func_5978 = relay.Function([var_5977], output)
mutated_mod['func_5978'] = func_5978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_962_call = mod.get_global_var('func_962')
func_964_call = mutated_mod.get_global_var('func_964')
call_6023 = relay.TupleGetItem(func_962_call(), 0)
call_6024 = relay.TupleGetItem(func_964_call(), 0)
output = call_6023
output2 = call_6024
func_6027 = relay.Function([], output)
mod['func_6027'] = func_6027
mod = relay.transform.InferType()(mod)
mutated_mod['func_6027'] = func_6027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6027_call = mutated_mod.get_global_var('func_6027')
call_6028 = func_6027_call()
output = call_6028
func_6029 = relay.Function([], output)
mutated_mod['func_6029'] = func_6029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_6047 = func_1830_call()
call_6048 = func_1830_call()
uop_6049 = relay.acosh(call_6047.astype('float64')) # shape=(7, 15, 1)
uop_6051 = relay.acosh(call_6048.astype('float64')) # shape=(7, 15, 1)
func_5251_call = mod.get_global_var('func_5251')
func_5253_call = mutated_mod.get_global_var('func_5253')
call_6060 = relay.TupleGetItem(func_5251_call(), 0)
call_6061 = relay.TupleGetItem(func_5253_call(), 0)
output = relay.Tuple([uop_6049,call_6060,])
output2 = relay.Tuple([uop_6051,call_6061,])
func_6064 = relay.Function([], output)
mod['func_6064'] = func_6064
mod = relay.transform.InferType()(mod)
output = func_6064()
func_6065 = relay.Function([], output)
mutated_mod['func_6065'] = func_6065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5470_call = mod.get_global_var('func_5470')
func_5472_call = mutated_mod.get_global_var('func_5472')
call_6109 = relay.TupleGetItem(func_5470_call(), 0)
call_6110 = relay.TupleGetItem(func_5472_call(), 0)
output = call_6109
output2 = call_6110
func_6126 = relay.Function([], output)
mod['func_6126'] = func_6126
mod = relay.transform.InferType()(mod)
mutated_mod['func_6126'] = func_6126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mutated_mod.get_global_var('func_6126')
call_6127 = func_6126_call()
output = call_6127
func_6128 = relay.Function([], output)
mutated_mod['func_6128'] = func_6128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4506_call = mod.get_global_var('func_4506')
func_4508_call = mutated_mod.get_global_var('func_4508')
call_6140 = relay.TupleGetItem(func_4506_call(), 0)
call_6141 = relay.TupleGetItem(func_4508_call(), 0)
func_5767_call = mod.get_global_var('func_5767')
func_5769_call = mutated_mod.get_global_var('func_5769')
var_6145 = relay.var("var_6145", dtype = "uint32", shape = (560,))#candidate|6145|(560,)|var|uint32
call_6144 = relay.TupleGetItem(func_5767_call(relay.reshape(var_6145.astype('uint32'), [14, 5, 8])), 1)
call_6146 = relay.TupleGetItem(func_5769_call(relay.reshape(var_6145.astype('uint32'), [14, 5, 8])), 1)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_6150 = func_1830_call()
call_6151 = func_1830_call()
output = relay.Tuple([call_6140,call_6144,var_6145,call_6150,])
output2 = relay.Tuple([call_6141,call_6146,var_6145,call_6151,])
func_6154 = relay.Function([var_6145,], output)
mod['func_6154'] = func_6154
mod = relay.transform.InferType()(mod)
var_6155 = relay.var("var_6155", dtype = "uint32", shape = (560,))#candidate|6155|(560,)|var|uint32
output = func_6154(var_6155)
func_6156 = relay.Function([var_6155], output)
mutated_mod['func_6156'] = func_6156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6064_call = mod.get_global_var('func_6064')
func_6065_call = mutated_mod.get_global_var('func_6065')
call_6221 = relay.TupleGetItem(func_6064_call(), 0)
call_6222 = relay.TupleGetItem(func_6065_call(), 0)
output = relay.Tuple([call_6221,])
output2 = relay.Tuple([call_6222,])
func_6236 = relay.Function([], output)
mod['func_6236'] = func_6236
mod = relay.transform.InferType()(mod)
output = func_6236()
func_6237 = relay.Function([], output)
mutated_mod['func_6237'] = func_6237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6027_call = mod.get_global_var('func_6027')
func_6029_call = mutated_mod.get_global_var('func_6029')
call_6295 = func_6027_call()
call_6296 = func_6027_call()
output = call_6295
output2 = call_6296
func_6321 = relay.Function([], output)
mod['func_6321'] = func_6321
mod = relay.transform.InferType()(mod)
mutated_mod['func_6321'] = func_6321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6321_call = mutated_mod.get_global_var('func_6321')
call_6322 = func_6321_call()
output = call_6322
func_6323 = relay.Function([], output)
mutated_mod['func_6323'] = func_6323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5251_call = mod.get_global_var('func_5251')
func_5253_call = mutated_mod.get_global_var('func_5253')
call_6326 = relay.TupleGetItem(func_5251_call(), 0)
call_6327 = relay.TupleGetItem(func_5253_call(), 0)
func_3693_call = mod.get_global_var('func_3693')
func_3694_call = mutated_mod.get_global_var('func_3694')
call_6354 = relay.TupleGetItem(func_3693_call(), 0)
call_6355 = relay.TupleGetItem(func_3694_call(), 0)
output = relay.Tuple([call_6326,call_6354,])
output2 = relay.Tuple([call_6327,call_6355,])
func_6359 = relay.Function([], output)
mod['func_6359'] = func_6359
mod = relay.transform.InferType()(mod)
output = func_6359()
func_6360 = relay.Function([], output)
mutated_mod['func_6360'] = func_6360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4530_call = mod.get_global_var('func_4530')
func_4531_call = mutated_mod.get_global_var('func_4531')
call_6367 = func_4530_call()
call_6368 = func_4530_call()
output = call_6367
output2 = call_6368
func_6375 = relay.Function([], output)
mod['func_6375'] = func_6375
mod = relay.transform.InferType()(mod)
mutated_mod['func_6375'] = func_6375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6375_call = mutated_mod.get_global_var('func_6375')
call_6376 = func_6375_call()
output = call_6376
func_6377 = relay.Function([], output)
mutated_mod['func_6377'] = func_6377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5470_call = mod.get_global_var('func_5470')
func_5472_call = mutated_mod.get_global_var('func_5472')
call_6394 = relay.TupleGetItem(func_5470_call(), 0)
call_6395 = relay.TupleGetItem(func_5472_call(), 0)
func_6027_call = mod.get_global_var('func_6027')
func_6029_call = mutated_mod.get_global_var('func_6029')
call_6398 = func_6027_call()
call_6399 = func_6027_call()
func_2700_call = mod.get_global_var('func_2700')
func_2703_call = mutated_mod.get_global_var('func_2703')
var_6411 = relay.var("var_6411", dtype = "int8", shape = (900,))#candidate|6411|(900,)|var|int8
call_6410 = relay.TupleGetItem(func_2700_call(relay.reshape(var_6411.astype('int8'), [900,])), 2)
call_6412 = relay.TupleGetItem(func_2703_call(relay.reshape(var_6411.astype('int8'), [900,])), 2)
output = relay.Tuple([call_6394,call_6398,call_6410,var_6411,])
output2 = relay.Tuple([call_6395,call_6399,call_6412,var_6411,])
func_6418 = relay.Function([var_6411,], output)
mod['func_6418'] = func_6418
mod = relay.transform.InferType()(mod)
mutated_mod['func_6418'] = func_6418
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6419 = relay.var("var_6419", dtype = "int8", shape = (900,))#candidate|6419|(900,)|var|int8
func_6418_call = mutated_mod.get_global_var('func_6418')
call_6420 = func_6418_call(var_6419)
output = call_6420
func_6421 = relay.Function([var_6419], output)
mutated_mod['func_6421'] = func_6421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1781_call = mod.get_global_var('func_1781')
func_1782_call = mutated_mod.get_global_var('func_1782')
call_6430 = relay.TupleGetItem(func_1781_call(), 0)
call_6431 = relay.TupleGetItem(func_1782_call(), 0)
output = relay.Tuple([call_6430,])
output2 = relay.Tuple([call_6431,])
func_6445 = relay.Function([], output)
mod['func_6445'] = func_6445
mod = relay.transform.InferType()(mod)
output = func_6445()
func_6446 = relay.Function([], output)
mutated_mod['func_6446'] = func_6446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3958_call = mod.get_global_var('func_3958')
func_3960_call = mutated_mod.get_global_var('func_3960')
call_6460 = func_3958_call()
call_6461 = func_3958_call()
output = call_6460
output2 = call_6461
func_6474 = relay.Function([], output)
mod['func_6474'] = func_6474
mod = relay.transform.InferType()(mod)
mutated_mod['func_6474'] = func_6474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6474_call = mutated_mod.get_global_var('func_6474')
call_6475 = func_6474_call()
output = call_6475
func_6476 = relay.Function([], output)
mutated_mod['func_6476'] = func_6476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5139_call = mod.get_global_var('func_5139')
func_5141_call = mutated_mod.get_global_var('func_5141')
call_6479 = func_5139_call()
call_6480 = func_5139_call()
func_5924_call = mod.get_global_var('func_5924')
func_5929_call = mutated_mod.get_global_var('func_5929')
var_6496 = relay.var("var_6496", dtype = "float32", shape = (630,))#candidate|6496|(630,)|var|float32
var_6497 = relay.var("var_6497", dtype = "float32", shape = (72, 1))#candidate|6497|(72, 1)|var|float32
const_6498 = relay.const([-10,8,-8,6,-3,-6,3,-10,-6,-4,-3,1,5,2,-1,-7,-1,6,3,3,2,-5,-9,-8,1,9,-2,-1,-10,-2,-3,-3,-3,4,-10,10,-6,-7,-7,-2,-6,4,1,6,-10,4,7,-8,6,-6,8,-8,-10,1,-9,-8,4,-6,-9,8,-1,3,-10,10,-2,2,-2,-4,7,-2,10,5,1,-1,-4,-2,-1,-4,-5,-7,-1,-8,-1,-5,-10,7,8,4,-3,-2,1,-1,8,-3,8,-1,-1,1,-1,-2,-5,1,-3,3,-7,3,8,4,9,-8,-7,7,-7,-2,9,1,3,9,6,-1,8,5,-10,-1,-6,10,-9,-3,-7,9,9,2,-2,9,3,-5,6,7,6,-8,9,8,-5,8,-6,-10,7,-8,-4,-8,-8,10,-10,-1,4,-1,-5,3,-9,-6,8,-1,-9,-3,-7,10,4,9,-6,4,-10,-5,5,-9,-8,1,-10,-10,-3,-3,-6,4,-4,5,5,-2,-6,4,-4,6,-7,-8,9,-7,3,-1,-5,-6,-9,-9,-2,-3,-5,-8,9,2,10,4,-10,-2,-1,9,-9,4,-7,4,3,8,4,10,-9,-1,2,8,6,-4,-2,-4,-7,-9,-1,-6,2,-6,-9,4,-9,-6,-8,-3,-4,-1,10,-7,4,-3,-3,-3,10,-3,-6,-6,-2,5,7,-4,5,-9,-3,-1,-4,-3,-1,2,-6,2,-4,6,-1,5,1,10,7,8,-6,6,-3,-7,-5,-10,5,-4,8,-4,3,6,-1,7,-6,9,-5,-3,3,-7,-10,1,6,-6,-7,5,2,-1,10,2,-4,1,5,2,-6,8,3,-3,7,7,-2,2,-6,8,3,-5,10,-8,1,-2,-8,-7,2,-2,-1,-4,3,-8,1,6,-5,-2,-8,7,2,-8,-2,3,-5,6,4,-1,-6,-6,5,2,5,-3,6,-4,-1,-1,7,10,9,-10,-4,1,-9,8,9,4,-3,8,-8,2,-3,6,-6,-6,10,9,-6,-5,-7,1,-10,1,3,-5,-10,-2,-9,-6,5,-10,-7,-1,9,-10,-9,-4,5,4,-5,-10,-5,7,-3,1,-5,2,-1,-5,-1,9,-7,8,-8,-1,-1,-5,3,2,-7,3,5,-3,10,-9,2,-8,-10,-2,-9,9,-4,-8,-10,-3,5,-8,1,7,9,2,-3,-2,-9,1,-7,-7,7,-8,-6,-4,6,1,3,-1,-5,4,3,1,8,1,-4,-6,4,10,6,-2,7,-2,-3,-1,-5,-6,-10,-2,1,-6,2,8,10,9,-3,10,8,10,-6,10,7,2,5,10,9,-2,9,-8,-9,7,-2,2,1,-9,-3,10,7,9,-8,-7,-4,10,9,4,-9,-10,8,-8,5,7,8,-8,-9,-8,-6,8,4,-3,7,10,8,6,-3,-6,4,6,1,9,-1,-9,-10,6,6,-6,9,-1,-8,-5,-1,-9,4,-5,1,5,10,10,-2,5,-6,-2,-9,-3,8,-7,-1,-2,-6,-2,-2,9,-2,6,-5,-3,-4,-9,-6,9,2,-2,6,10,2,7,10,10,6,7,8,6,4,4,-8,3,1,-3,-1,9,8,9,-3,-9,6,-4,-7,-6,-4,9,5,1,9,-5,10,4,-9,5,6,2,-1,6,-7,-7,5,4,-9,-10,-3,-7,-8,-1,5,-10,2,-3,-8,-1,3,7,-5,10,6,-2,-6,1,1,-2,10,9,1,4,-3,6,2,-6,2,3,-7,-8,4,-6,3,-3,-7,2,-6,-9,1,5,-9,-2,-6,-1,-10,5,-8,10,10,-4,-6,6,3,1,3,9,6,2,-8,6,-2,5,3,-3,9,-9,-4,-8,-2,-10,6,6,-3,-5,-1,-1,1,5,1,4,-3,-6,-8,3,5,3,-3,5,-9,-6,-1,-5,5,4,-6,-6,3,-8,-6,9,4,-5,2,2,-10,2,-7,4,7,-8,8,3,-5,10,-2,5,2,-3,-9,8,3,-3,-8,-4,4,-9,-5,-4,5,-2,-7,-3,8,-5,-10,10,-6,-6,7,3,-2,-4,7,7,-5,9,7,-1,7,-6,3,-2,7,5,-10,5,-1,8,8,9,4,5,9,8,2,-5,-8,-5,-5,-8,9,6,4,-9,9,6,-6,-7,-7,-5,7,-5,6,-9,-10,-5,-10,-10,-7,9,-7,-1,5,1,1,10,-5,2,-5,-4,7,4,4,-4,-3,7,7,4,-4,-6,3,4,3,1,6,-10,9,-4,8,-2,-2,-2,6,3,-2,-6,6,-5,5,-4,-3,6,10,3,-10,8,5,-1,7,3,-4,6,-9,7,-7,5,-9,10,-10,7,9,2,-7,-6,-8,4,8,-9,1,10,-1,5,-5,9,-1,5,-4,-5,9,-5,-10,8,1,4,-7,9], dtype = "int8")#candidate|6498|(900,)|const|int8
call_6495 = relay.TupleGetItem(func_5924_call(relay.reshape(var_6496.astype('float32'), [70, 9]), relay.reshape(var_6497.astype('float32'), [72,]), relay.reshape(const_6498.astype('int8'), [900,]), ), 8)
call_6499 = relay.TupleGetItem(func_5929_call(relay.reshape(var_6496.astype('float32'), [70, 9]), relay.reshape(var_6497.astype('float32'), [72,]), relay.reshape(const_6498.astype('int8'), [900,]), ), 8)
bop_6502 = relay.right_shift(var_6496.astype('uint64'), var_6497.astype('uint64')) # shape=(72, 630)
output = relay.Tuple([call_6479,call_6495,const_6498,bop_6502,])
output2 = relay.Tuple([call_6480,call_6499,const_6498,bop_6502,])
func_6506 = relay.Function([var_6496,var_6497,], output)
mod['func_6506'] = func_6506
mod = relay.transform.InferType()(mod)
mutated_mod['func_6506'] = func_6506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6506_call = mutated_mod.get_global_var('func_6506')
var_6508 = relay.var("var_6508", dtype = "float32", shape = (630,))#candidate|6508|(630,)|var|float32
var_6509 = relay.var("var_6509", dtype = "float32", shape = (72, 1))#candidate|6509|(72, 1)|var|float32
call_6507 = func_6506_call(var_6508,var_6509,)
output = call_6507
func_6510 = relay.Function([var_6508,var_6509,], output)
mutated_mod['func_6510'] = func_6510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5679_call = mod.get_global_var('func_5679')
func_5681_call = mutated_mod.get_global_var('func_5681')
call_6524 = relay.TupleGetItem(func_5679_call(), 0)
call_6525 = relay.TupleGetItem(func_5681_call(), 0)
output = relay.Tuple([call_6524,])
output2 = relay.Tuple([call_6525,])
func_6532 = relay.Function([], output)
mod['func_6532'] = func_6532
mod = relay.transform.InferType()(mod)
mutated_mod['func_6532'] = func_6532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6532_call = mutated_mod.get_global_var('func_6532')
call_6533 = func_6532_call()
output = call_6533
func_6534 = relay.Function([], output)
mutated_mod['func_6534'] = func_6534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5624_call = mod.get_global_var('func_5624')
func_5625_call = mutated_mod.get_global_var('func_5625')
call_6622 = relay.TupleGetItem(func_5624_call(), 0)
call_6623 = relay.TupleGetItem(func_5625_call(), 0)
output = relay.Tuple([call_6622,])
output2 = relay.Tuple([call_6623,])
func_6638 = relay.Function([], output)
mod['func_6638'] = func_6638
mod = relay.transform.InferType()(mod)
output = func_6638()
func_6639 = relay.Function([], output)
mutated_mod['func_6639'] = func_6639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5507_call = mod.get_global_var('func_5507')
func_5508_call = mutated_mod.get_global_var('func_5508')
call_6680 = relay.TupleGetItem(func_5507_call(), 0)
call_6681 = relay.TupleGetItem(func_5508_call(), 0)
var_6682 = relay.var("var_6682", dtype = "float32", shape = (7, 15, 13))#candidate|6682|(7, 15, 13)|var|float32
bop_6683 = relay.greater_equal(call_6680.astype('bool'), var_6682.astype('bool')) # shape=(7, 15, 13)
bop_6686 = relay.greater_equal(call_6681.astype('bool'), var_6682.astype('bool')) # shape=(7, 15, 13)
output = bop_6683
output2 = bop_6686
func_6697 = relay.Function([var_6682,], output)
mod['func_6697'] = func_6697
mod = relay.transform.InferType()(mod)
var_6698 = relay.var("var_6698", dtype = "float32", shape = (7, 15, 13))#candidate|6698|(7, 15, 13)|var|float32
output = func_6697(var_6698)
func_6699 = relay.Function([var_6698], output)
mutated_mod['func_6699'] = func_6699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3693_call = mod.get_global_var('func_3693')
func_3694_call = mutated_mod.get_global_var('func_3694')
call_6730 = relay.TupleGetItem(func_3693_call(), 0)
call_6731 = relay.TupleGetItem(func_3694_call(), 0)
output = call_6730
output2 = call_6731
func_6737 = relay.Function([], output)
mod['func_6737'] = func_6737
mod = relay.transform.InferType()(mod)
output = func_6737()
func_6738 = relay.Function([], output)
mutated_mod['func_6738'] = func_6738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1830_call = mod.get_global_var('func_1830')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_6753 = func_1830_call()
call_6754 = func_1830_call()
output = call_6753
output2 = call_6754
func_6761 = relay.Function([], output)
mod['func_6761'] = func_6761
mod = relay.transform.InferType()(mod)
output = func_6761()
func_6762 = relay.Function([], output)
mutated_mod['func_6762'] = func_6762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1863_call = mod.get_global_var('func_1863')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_6777 = relay.TupleGetItem(func_1863_call(), 0)
call_6778 = relay.TupleGetItem(func_1865_call(), 0)
output = call_6777
output2 = call_6778
func_6782 = relay.Function([], output)
mod['func_6782'] = func_6782
mod = relay.transform.InferType()(mod)
mutated_mod['func_6782'] = func_6782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6782_call = mutated_mod.get_global_var('func_6782')
call_6783 = func_6782_call()
output = call_6783
func_6784 = relay.Function([], output)
mutated_mod['func_6784'] = func_6784
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6806 = relay.var("var_6806", dtype = "uint32", shape = (2, 10, 12))#candidate|6806|(2, 10, 12)|var|uint32
var_6807 = relay.var("var_6807", dtype = "uint32", shape = (2, 10, 12))#candidate|6807|(2, 10, 12)|var|uint32
bop_6808 = relay.bitwise_xor(var_6806.astype('uint32'), relay.reshape(var_6807.astype('uint32'), relay.shape_of(var_6806))) # shape=(2, 10, 12)
output = relay.Tuple([bop_6808,])
output2 = relay.Tuple([bop_6808,])
func_6811 = relay.Function([var_6806,var_6807,], output)
mod['func_6811'] = func_6811
mod = relay.transform.InferType()(mod)
var_6812 = relay.var("var_6812", dtype = "uint32", shape = (2, 10, 12))#candidate|6812|(2, 10, 12)|var|uint32
var_6813 = relay.var("var_6813", dtype = "uint32", shape = (2, 10, 12))#candidate|6813|(2, 10, 12)|var|uint32
output = func_6811(var_6812,var_6813,)
func_6814 = relay.Function([var_6812,var_6813,], output)
mutated_mod['func_6814'] = func_6814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5564_call = mod.get_global_var('func_5564')
func_5565_call = mutated_mod.get_global_var('func_5565')
call_6841 = relay.TupleGetItem(func_5564_call(), 1)
call_6842 = relay.TupleGetItem(func_5565_call(), 1)
output = call_6841
output2 = call_6842
func_6844 = relay.Function([], output)
mod['func_6844'] = func_6844
mod = relay.transform.InferType()(mod)
output = func_6844()
func_6845 = relay.Function([], output)
mutated_mod['func_6845'] = func_6845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3340_call = mod.get_global_var('func_3340')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_6893 = relay.TupleGetItem(func_3340_call(), 0)
call_6894 = relay.TupleGetItem(func_3342_call(), 0)
output = call_6893
output2 = call_6894
func_6916 = relay.Function([], output)
mod['func_6916'] = func_6916
mod = relay.transform.InferType()(mod)
output = func_6916()
func_6917 = relay.Function([], output)
mutated_mod['func_6917'] = func_6917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6737_call = mod.get_global_var('func_6737')
func_6738_call = mutated_mod.get_global_var('func_6738')
call_6930 = func_6737_call()
call_6931 = func_6737_call()
var_6938 = relay.var("var_6938", dtype = "float64", shape = (7, 15, 3150))#candidate|6938|(7, 15, 3150)|var|float64
bop_6939 = relay.not_equal(call_6930.astype('bool'), relay.reshape(var_6938.astype('bool'), relay.shape_of(call_6930))) # shape=(7, 15, 3150)
bop_6942 = relay.not_equal(call_6931.astype('bool'), relay.reshape(var_6938.astype('bool'), relay.shape_of(call_6931))) # shape=(7, 15, 3150)
func_399_call = mod.get_global_var('func_399')
func_401_call = mutated_mod.get_global_var('func_401')
var_6950 = relay.var("var_6950", dtype = "float32", shape = (72,))#candidate|6950|(72,)|var|float32
call_6949 = relay.TupleGetItem(func_399_call(relay.reshape(var_6950.astype('float32'), [6, 6, 2])), 0)
call_6951 = relay.TupleGetItem(func_401_call(relay.reshape(var_6950.astype('float32'), [6, 6, 2])), 0)
func_2582_call = mod.get_global_var('func_2582')
func_2584_call = mutated_mod.get_global_var('func_2584')
var_6955 = relay.var("var_6955", dtype = "uint32", shape = (756,))#candidate|6955|(756,)|var|uint32
call_6954 = func_2582_call(relay.reshape(var_6955.astype('uint32'), [14, 6, 9]))
call_6956 = func_2582_call(relay.reshape(var_6955.astype('uint32'), [14, 6, 9]))
func_6027_call = mod.get_global_var('func_6027')
func_6029_call = mutated_mod.get_global_var('func_6029')
call_6964 = func_6027_call()
call_6965 = func_6027_call()
uop_6969 = relay.acosh(call_6954.astype('float64')) # shape=(14, 6, 9)
uop_6971 = relay.acosh(call_6956.astype('float64')) # shape=(14, 6, 9)
func_5767_call = mod.get_global_var('func_5767')
func_5769_call = mutated_mod.get_global_var('func_5769')
var_6974 = relay.var("var_6974", dtype = "uint32", shape = (560,))#candidate|6974|(560,)|var|uint32
call_6973 = relay.TupleGetItem(func_5767_call(relay.reshape(var_6974.astype('uint32'), [14, 5, 8])), 0)
call_6975 = relay.TupleGetItem(func_5769_call(relay.reshape(var_6974.astype('uint32'), [14, 5, 8])), 0)
uop_6978 = relay.exp(uop_6969.astype('float32')) # shape=(14, 6, 9)
uop_6980 = relay.exp(uop_6971.astype('float32')) # shape=(14, 6, 9)
uop_6993 = relay.atan(uop_6969.astype('float64')) # shape=(14, 6, 9)
uop_6995 = relay.atan(uop_6971.astype('float64')) # shape=(14, 6, 9)
bop_6998 = relay.logical_or(uop_6978.astype('bool'), relay.reshape(uop_6969.astype('bool'), relay.shape_of(uop_6978))) # shape=(14, 6, 9)
bop_7001 = relay.logical_or(uop_6980.astype('bool'), relay.reshape(uop_6971.astype('bool'), relay.shape_of(uop_6980))) # shape=(14, 6, 9)
func_4944_call = mod.get_global_var('func_4944')
func_4945_call = mutated_mod.get_global_var('func_4945')
call_7002 = relay.TupleGetItem(func_4944_call(), 0)
call_7003 = relay.TupleGetItem(func_4945_call(), 0)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
var_7013 = relay.var("var_7013", dtype = "int8", shape = (900,))#candidate|7013|(900,)|var|int8
call_7012 = relay.TupleGetItem(func_2406_call(relay.reshape(var_7013.astype('int8'), [900,])), 2)
call_7014 = relay.TupleGetItem(func_2408_call(relay.reshape(var_7013.astype('int8'), [900,])), 2)
func_2045_call = mod.get_global_var('func_2045')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_7015 = relay.TupleGetItem(func_2045_call(), 2)
call_7016 = relay.TupleGetItem(func_2047_call(), 2)
uop_7029 = relay.atanh(bop_6998.astype('float64')) # shape=(14, 6, 9)
uop_7031 = relay.atanh(bop_7001.astype('float64')) # shape=(14, 6, 9)
var_7034 = relay.var("var_7034", dtype = "bool", shape = (14, 6, 9))#candidate|7034|(14, 6, 9)|var|bool
bop_7035 = relay.mod(bop_6998.astype('float32'), relay.reshape(var_7034.astype('float32'), relay.shape_of(bop_6998))) # shape=(14, 6, 9)
bop_7038 = relay.mod(bop_7001.astype('float32'), relay.reshape(var_7034.astype('float32'), relay.shape_of(bop_7001))) # shape=(14, 6, 9)
func_6844_call = mod.get_global_var('func_6844')
func_6845_call = mutated_mod.get_global_var('func_6845')
call_7065 = func_6844_call()
call_7066 = func_6844_call()
func_2836_call = mod.get_global_var('func_2836')
func_2840_call = mutated_mod.get_global_var('func_2840')
var_7068 = relay.var("var_7068", dtype = "int8", shape = (3150,))#candidate|7068|(3150,)|var|int8
call_7067 = relay.TupleGetItem(func_2836_call(relay.reshape(var_7068.astype('int8'), [15, 15, 14]), relay.reshape(var_7068.astype('int8'), [15, 15, 14]), ), 0)
call_7069 = relay.TupleGetItem(func_2840_call(relay.reshape(var_7068.astype('int8'), [15, 15, 14]), relay.reshape(var_7068.astype('int8'), [15, 15, 14]), ), 0)
func_4655_call = mod.get_global_var('func_4655')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_7087 = func_4655_call()
call_7088 = func_4655_call()
func_6359_call = mod.get_global_var('func_6359')
func_6360_call = mutated_mod.get_global_var('func_6360')
call_7104 = relay.TupleGetItem(func_6359_call(), 1)
call_7105 = relay.TupleGetItem(func_6360_call(), 1)
output = relay.Tuple([bop_6939,call_6949,var_6950,var_6955,call_6964,call_6973,var_6974,uop_6993,call_7002,call_7012,var_7013,call_7015,uop_7029,bop_7035,call_7065,call_7067,var_7068,call_7087,call_7104,])
output2 = relay.Tuple([bop_6942,call_6951,var_6950,var_6955,call_6965,call_6975,var_6974,uop_6995,call_7003,call_7014,var_7013,call_7016,uop_7031,bop_7038,call_7066,call_7069,var_7068,call_7088,call_7105,])
func_7106 = relay.Function([var_6938,var_6950,var_6955,var_6974,var_7013,var_7034,var_7068,], output)
mod['func_7106'] = func_7106
mod = relay.transform.InferType()(mod)
var_7107 = relay.var("var_7107", dtype = "float64", shape = (7, 15, 3150))#candidate|7107|(7, 15, 3150)|var|float64
var_7108 = relay.var("var_7108", dtype = "float32", shape = (72,))#candidate|7108|(72,)|var|float32
var_7109 = relay.var("var_7109", dtype = "uint32", shape = (756,))#candidate|7109|(756,)|var|uint32
var_7110 = relay.var("var_7110", dtype = "uint32", shape = (560,))#candidate|7110|(560,)|var|uint32
var_7111 = relay.var("var_7111", dtype = "int8", shape = (900,))#candidate|7111|(900,)|var|int8
var_7112 = relay.var("var_7112", dtype = "bool", shape = (14, 6, 9))#candidate|7112|(14, 6, 9)|var|bool
var_7113 = relay.var("var_7113", dtype = "int8", shape = (3150,))#candidate|7113|(3150,)|var|int8
output = func_7106(var_7107,var_7108,var_7109,var_7110,var_7111,var_7112,var_7113,)
func_7114 = relay.Function([var_7107,var_7108,var_7109,var_7110,var_7111,var_7112,var_7113,], output)
mutated_mod['func_7114'] = func_7114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5118_call = mod.get_global_var('func_5118')
func_5119_call = mutated_mod.get_global_var('func_5119')
call_7121 = relay.TupleGetItem(func_5118_call(), 0)
call_7122 = relay.TupleGetItem(func_5119_call(), 0)
output = call_7121
output2 = call_7122
func_7134 = relay.Function([], output)
mod['func_7134'] = func_7134
mod = relay.transform.InferType()(mod)
output = func_7134()
func_7135 = relay.Function([], output)
mutated_mod['func_7135'] = func_7135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2045_call = mod.get_global_var('func_2045')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_7165 = relay.TupleGetItem(func_2045_call(), 2)
call_7166 = relay.TupleGetItem(func_2047_call(), 2)
output = relay.Tuple([call_7165,])
output2 = relay.Tuple([call_7166,])
func_7167 = relay.Function([], output)
mod['func_7167'] = func_7167
mod = relay.transform.InferType()(mod)
mutated_mod['func_7167'] = func_7167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7167_call = mutated_mod.get_global_var('func_7167')
call_7168 = func_7167_call()
output = call_7168
func_7169 = relay.Function([], output)
mutated_mod['func_7169'] = func_7169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_7173 = func_1015_call()
call_7174 = func_1015_call()
var_7197 = relay.var("var_7197", dtype = "float64", shape = (7, 15, 9))#candidate|7197|(7, 15, 9)|var|float64
bop_7198 = relay.floor_mod(call_7173.astype('float64'), var_7197.astype('float64')) # shape=(7, 15, 9)
bop_7201 = relay.floor_mod(call_7174.astype('float64'), var_7197.astype('float64')) # shape=(7, 15, 9)
output = relay.Tuple([bop_7198,])
output2 = relay.Tuple([bop_7201,])
F = relay.Function([var_7197,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7197,], output2)
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
