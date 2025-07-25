import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_641 = relay.const(8, dtype = "uint8")#candidate|641|()|const|uint8
var_642 = relay.var("var_642", dtype = "uint8", shape = (13, 10, 6))#candidate|642|(13, 10, 6)|var|uint8
bop_643 = relay.bitwise_or(const_641.astype('uint8'), var_642.astype('uint8')) # shape=(13, 10, 6)
output = bop_643
output2 = bop_643
func_647 = relay.Function([var_642,], output)
mod['func_647'] = func_647
mod = relay.transform.InferType()(mod)
var_648 = relay.var("var_648", dtype = "uint8", shape = (13, 10, 6))#candidate|648|(13, 10, 6)|var|uint8
output = func_647(var_648)
func_649 = relay.Function([var_648], output)
mutated_mod['func_649'] = func_649
mutated_mod = relay.transform.InferType()(mutated_mod)
const_797 = relay.const([[[1,1,-9,3,-6,-8,-2],[-9,2,7,-2,9,-9,9],[10,-1,-9,-9,1,-6,4],[3,-3,-10,-2,4,-3,10],[-5,4,-10,8,-7,2,3],[-6,2,-1,-10,1,-10,-6],[5,7,-4,7,3,-7,-4],[-8,-7,-2,-4,3,7,-7],[-8,-10,-8,4,5,8,-7],[-10,-6,-8,3,-1,6,-2],[-1,-10,4,3,-6,-6,8]],[[-2,-2,8,1,10,-9,-2],[6,-7,-6,5,6,4,7],[-4,-7,-2,9,5,-9,3],[-8,2,-10,1,4,6,6],[-4,1,7,-4,-6,-8,-2],[-8,4,1,-9,3,-9,-8],[8,6,-6,-10,4,2,7],[-3,-7,-6,-6,-7,10,-7],[-10,3,-10,8,3,-8,1],[8,-10,-1,-1,-9,3,-4],[-9,-1,7,-7,-10,-2,2]],[[-1,10,5,10,8,-2,-8],[7,10,-2,-5,5,-5,-6],[10,-9,-4,-10,-10,6,2],[8,-5,-10,1,7,9,9],[-7,-3,6,9,10,9,-10],[9,-3,9,-10,-4,-1,10],[-3,5,7,-8,-1,-2,-6],[10,-8,-7,-4,10,7,8],[4,-9,-8,-8,6,7,-1],[-8,-10,3,7,-10,8,6],[3,-5,-3,-6,3,-7,10]],[[-4,-3,-1,1,2,6,9],[-1,1,-9,4,1,5,6],[2,-4,-10,-9,9,-5,-5],[2,-4,9,10,2,-1,4],[8,6,5,-6,-8,-3,4],[9,-8,-5,7,-8,3,-8],[4,8,1,1,7,-2,4],[-3,3,2,-6,-6,3,7],[3,-10,-7,-8,-6,6,-8],[-8,4,-3,-5,10,1,2],[9,10,7,10,8,-4,-9]],[[-8,1,-9,7,-3,6,2],[1,-9,-5,2,-9,-6,10],[-3,-2,-8,-7,7,-1,-4],[6,-4,2,-7,2,-7,-4],[10,-4,-5,-4,-9,-9,2],[-9,-7,-4,1,-4,-3,8],[9,-6,5,4,6,2,6],[6,-1,6,-9,1,-8,-6],[3,-4,7,-3,-10,2,-4],[5,-6,-10,3,7,8,-2],[2,1,4,-10,-5,-3,2]],[[5,10,8,1,4,-3,8],[8,-8,-7,-8,4,10,-2],[8,-8,2,3,3,7,7],[-8,-1,-4,1,-10,2,8],[5,5,-6,6,-1,9,2],[1,7,-4,-8,-9,-10,7],[-5,4,-4,3,3,9,8],[-10,-3,-10,10,1,4,8],[-1,6,9,5,-10,-7,-8],[9,-4,4,7,10,-8,7],[10,-8,10,4,5,-7,8]],[[9,8,-1,4,2,9,-1],[10,1,-3,1,-2,-5,6],[3,3,9,-8,6,6,-3],[7,-4,-4,-8,-5,-10,-4],[5,6,4,-7,-3,-1,-7],[6,-2,8,9,-2,-8,-6],[5,5,1,-9,1,6,-3],[2,4,3,-10,-3,-10,-7],[-3,9,2,1,5,8,7],[9,-1,-1,-8,2,-5,6],[1,6,-6,-5,10,4,3]],[[9,-6,-10,-9,3,-5,-5],[1,8,5,-9,10,1,-7],[3,-5,-1,-3,7,4,-1],[-6,-1,-8,-10,-4,5,-10],[-2,-1,8,-9,8,-2,8],[-6,4,5,-10,6,-9,-8],[4,3,6,3,2,5,-8],[7,-10,4,7,-3,4,7],[-10,8,-5,-2,-6,7,8],[10,-6,1,1,1,-5,-5],[6,4,6,-1,-4,-4,-7]],[[10,10,1,-6,1,8,-7],[8,3,5,9,-1,4,3],[-8,8,8,-8,3,3,-3],[-10,3,-4,2,-8,-3,-3],[-6,5,-1,-4,1,9,-7],[-2,5,-3,-9,-7,-8,-4],[-3,6,-5,7,-5,4,4],[4,8,-2,-5,1,3,7],[-2,10,5,-7,10,6,-5],[-3,-6,10,2,-6,8,3],[7,3,-8,-7,3,-5,7]],[[10,2,3,-10,-1,-5,-9],[6,6,-9,-3,4,-2,-3],[1,8,6,-5,-9,1,7],[-9,-1,-6,8,-6,4,10],[-8,-3,-5,-10,-5,1,8],[-6,-10,-1,9,7,-5,-8],[-4,5,3,3,-10,-10,-6],[1,-3,-10,1,5,9,9],[7,-2,-8,-7,6,-9,-10],[3,2,-3,8,-7,5,1],[5,7,-7,-5,6,6,-1]],[[-8,7,-1,5,1,5,2],[-3,-3,3,10,-9,-7,-6],[-6,-1,10,-8,-5,4,6],[-8,-1,-1,7,4,-6,-2],[-9,7,9,-2,5,1,10],[-8,7,7,4,4,-4,1],[-1,-4,-5,-6,8,-3,-7],[-3,-2,-5,4,8,-10,3],[9,5,-9,4,9,-8,9],[1,8,5,4,10,2,8],[-8,-7,5,1,-10,-7,5]]], dtype = "int32")#candidate|797|(11, 11, 7)|const|int32
var_798 = relay.var("var_798", dtype = "int32", shape = (11, 11, 7))#candidate|798|(11, 11, 7)|var|int32
bop_799 = relay.subtract(const_797.astype('int32'), relay.reshape(var_798.astype('int32'), relay.shape_of(const_797))) # shape=(11, 11, 7)
output = bop_799
output2 = bop_799
func_807 = relay.Function([var_798,], output)
mod['func_807'] = func_807
mod = relay.transform.InferType()(mod)
mutated_mod['func_807'] = func_807
mutated_mod = relay.transform.InferType()(mutated_mod)
var_808 = relay.var("var_808", dtype = "int32", shape = (11, 11, 7))#candidate|808|(11, 11, 7)|var|int32
func_807_call = mutated_mod.get_global_var('func_807')
call_809 = func_807_call(var_808)
output = call_809
func_810 = relay.Function([var_808], output)
mutated_mod['func_810'] = func_810
mutated_mod = relay.transform.InferType()(mutated_mod)
const_849 = relay.const(8.472041, dtype = "float32")#candidate|849|()|const|float32
const_850 = relay.const([[[2.314504,-4.955426,4.363962,4.443594],[-5.765638,9.936853,-0.237386,3.683905],[-8.787787,-8.968394,5.039068,-8.281475],[-7.579613,-2.029379,4.449532,3.983894],[-5.810799,-8.839932,-2.588653,6.052712],[4.978283,-2.434272,3.440302,-2.195136],[3.598581,6.007749,9.985615,1.265711],[-6.868624,-7.317587,4.208818,-4.651802],[2.578966,2.508893,-2.052958,1.252231],[5.525882,6.421305,1.156159,6.286071],[3.359490,5.603685,-7.085682,-2.018631],[8.549671,-8.606104,-5.830885,-9.373953],[0.647113,-3.850134,9.414251,-3.156423],[1.705967,6.419099,1.165835,1.232672]],[[6.899352,4.613285,5.639728,-7.363238],[6.377060,7.707396,7.292879,6.734810],[3.550259,-3.390480,6.292663,-1.711596],[-0.863753,-2.518880,-6.929342,-5.531788],[-7.796735,3.313909,-9.448821,-7.959392],[6.702299,8.224763,-4.180196,3.397294],[-5.959549,-4.489596,-9.103945,1.349294],[-5.725198,-6.775281,6.139854,-0.852201],[6.308428,-0.089173,8.325622,1.622193],[-1.644437,0.216298,4.739735,5.405041],[-3.336300,-6.835451,-9.681731,2.580188],[3.659108,9.037665,7.071047,-8.378709],[2.906075,-8.331690,-4.465409,2.702526],[-3.802581,7.764296,-1.292082,-5.078006]],[[-5.189424,7.109470,-4.333279,3.603857],[7.128369,-8.346229,-4.887355,3.890243],[1.415735,-0.187277,8.973280,7.840848],[-4.306691,1.120677,0.596861,7.028785],[-4.801213,-0.055450,7.057040,-8.149828],[-6.131024,6.924921,-3.617327,-6.045542],[-8.715325,4.610168,7.685022,-1.974874],[8.335567,-4.725417,6.649922,-6.950163],[-0.224689,-8.858043,-0.886554,-7.320991],[1.034263,9.255245,-3.078774,-8.802660],[-1.840209,-8.811816,-9.001123,3.410514],[2.480950,-8.441269,4.255003,-2.495186],[3.101002,0.505626,-7.261656,-5.545647],[-0.773715,8.866121,9.819002,3.547324]],[[6.583262,2.118644,-4.016906,5.603758],[-0.351630,-6.825766,-0.595674,-2.878022],[6.748378,7.715316,8.486043,-2.793200],[2.274975,0.080298,6.848116,-3.475032],[-2.571271,-5.148090,-6.123996,-0.380033],[0.249565,-9.241623,-7.002664,0.469392],[-9.145877,0.668041,-0.389919,3.938815],[5.919147,-7.461923,-0.272416,1.668243],[4.898291,3.152441,9.331443,-9.945321],[3.514908,-6.514873,1.508906,2.953091],[-6.402753,-9.058415,-3.712699,-7.726661],[-5.849218,-6.252976,3.643077,7.637275],[4.922356,-6.199244,2.698138,7.168709],[4.722800,-2.112384,7.527852,-3.989284]],[[-5.554766,-8.257492,7.011238,-3.013515],[-7.780182,-5.406488,-1.140993,-3.143977],[-0.290889,-0.395318,1.525210,-3.810114],[2.845825,-7.676211,1.189727,-0.607853],[0.203814,-9.763153,9.956798,-3.245947],[-7.536424,7.451826,-4.555808,-6.396285],[-9.815996,-9.153265,5.203037,-6.070938],[1.371245,2.054007,5.293718,-3.454157],[4.837325,7.131181,7.650228,-4.120740],[-8.572033,-2.108963,0.797563,-7.848589],[0.886941,9.697094,4.007858,8.322325],[-6.830403,1.921245,-6.839552,-2.682082],[6.900521,-7.115467,9.934974,-0.834848],[-2.839069,2.592727,4.595824,5.592843]],[[-3.211340,6.639123,-3.537394,7.360027],[-9.751607,1.429233,-6.924330,-1.238863],[6.392840,8.921967,8.590995,1.021340],[-4.336214,4.238889,-9.731897,4.430326],[8.792763,-7.437385,2.371821,8.948310],[9.921721,9.433569,-0.880297,9.844806],[-5.923705,6.521193,-5.065803,-5.307438],[3.633597,-7.624991,-5.276499,-7.276656],[9.619755,-5.410142,-1.026395,-4.523616],[-5.887174,-8.198740,3.566358,-2.019335],[-1.287713,3.521600,-6.982146,8.882359],[3.761944,2.424833,1.182177,0.542330],[6.955025,-1.426727,1.013073,1.496813],[-4.703202,8.945981,8.589532,2.969037]],[[6.617523,-9.691531,-0.247514,4.674267],[9.742850,-6.462573,-9.398120,9.827309],[6.532377,-1.041242,-3.144206,-6.288903],[4.257803,-4.226765,1.984647,-4.078773],[-8.327117,7.711000,-9.136373,-4.271555],[2.937258,2.547112,1.006250,0.144945],[-0.316609,6.835163,9.890508,5.029749],[7.792200,8.523372,4.201563,5.426344],[-8.747777,2.741247,9.970322,3.962782],[-2.297587,9.500803,8.294360,-8.665179],[-2.423571,6.139067,5.939914,-4.816237],[-6.639765,9.594367,7.660665,-0.222021],[2.174396,-5.747643,8.502876,-2.966602],[-0.269561,5.368968,-8.358121,4.137138]]], dtype = "float32")#candidate|850|(7, 14, 4)|const|float32
bop_851 = relay.floor_divide(const_849.astype('float32'), const_850.astype('float32')) # shape=(7, 14, 4)
output = relay.Tuple([bop_851,])
output2 = relay.Tuple([bop_851,])
func_856 = relay.Function([], output)
mod['func_856'] = func_856
mod = relay.transform.InferType()(mod)
mutated_mod['func_856'] = func_856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mutated_mod.get_global_var('func_856')
call_857 = func_856_call()
output = call_857
func_858 = relay.Function([], output)
mutated_mod['func_858'] = func_858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_919 = relay.TupleGetItem(func_856_call(), 0)
call_920 = relay.TupleGetItem(func_858_call(), 0)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_922 = relay.TupleGetItem(func_856_call(), 0)
call_923 = relay.TupleGetItem(func_858_call(), 0)
func_647_call = mod.get_global_var('func_647')
func_649_call = mutated_mod.get_global_var('func_649')
var_929 = relay.var("var_929", dtype = "uint8", shape = (390, 2))#candidate|929|(390, 2)|var|uint8
call_928 = func_647_call(relay.reshape(var_929.astype('uint8'), [13, 10, 6]))
call_930 = func_647_call(relay.reshape(var_929.astype('uint8'), [13, 10, 6]))
output = relay.Tuple([call_919,call_922,call_928,var_929,])
output2 = relay.Tuple([call_920,call_923,call_930,var_929,])
func_931 = relay.Function([var_929,], output)
mod['func_931'] = func_931
mod = relay.transform.InferType()(mod)
mutated_mod['func_931'] = func_931
mutated_mod = relay.transform.InferType()(mutated_mod)
var_932 = relay.var("var_932", dtype = "uint8", shape = (390, 2))#candidate|932|(390, 2)|var|uint8
func_931_call = mutated_mod.get_global_var('func_931')
call_933 = func_931_call(var_932)
output = call_933
func_934 = relay.Function([var_932], output)
mutated_mod['func_934'] = func_934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_982 = relay.TupleGetItem(func_856_call(), 0)
call_983 = relay.TupleGetItem(func_858_call(), 0)
output = relay.Tuple([call_982,])
output2 = relay.Tuple([call_983,])
func_988 = relay.Function([], output)
mod['func_988'] = func_988
mod = relay.transform.InferType()(mod)
mutated_mod['func_988'] = func_988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mutated_mod.get_global_var('func_988')
call_989 = func_988_call()
output = call_989
func_990 = relay.Function([], output)
mutated_mod['func_990'] = func_990
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1028 = relay.const([[[-6,-4],[8,10],[-7,2],[-3,1],[-1,6],[-6,10],[1,-10]]], dtype = "uint8")#candidate|1028|(1, 7, 2)|const|uint8
var_1029 = relay.var("var_1029", dtype = "uint8", shape = (9, 7, 2))#candidate|1029|(9, 7, 2)|var|uint8
bop_1030 = relay.bitwise_xor(const_1028.astype('uint8'), var_1029.astype('uint8')) # shape=(9, 7, 2)
func_931_call = mod.get_global_var('func_931')
func_934_call = mutated_mod.get_global_var('func_934')
var_1036 = relay.var("var_1036", dtype = "uint8", shape = (780,))#candidate|1036|(780,)|var|uint8
call_1035 = relay.TupleGetItem(func_931_call(relay.reshape(var_1036.astype('uint8'), [390, 2])), 2)
call_1037 = relay.TupleGetItem(func_934_call(relay.reshape(var_1036.astype('uint8'), [390, 2])), 2)
output = relay.Tuple([bop_1030,call_1035,var_1036,])
output2 = relay.Tuple([bop_1030,call_1037,var_1036,])
func_1038 = relay.Function([var_1029,var_1036,], output)
mod['func_1038'] = func_1038
mod = relay.transform.InferType()(mod)
var_1039 = relay.var("var_1039", dtype = "uint8", shape = (9, 7, 2))#candidate|1039|(9, 7, 2)|var|uint8
var_1040 = relay.var("var_1040", dtype = "uint8", shape = (780,))#candidate|1040|(780,)|var|uint8
output = func_1038(var_1039,var_1040,)
func_1041 = relay.Function([var_1039,var_1040,], output)
mutated_mod['func_1041'] = func_1041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_1043 = relay.TupleGetItem(func_856_call(), 0)
call_1044 = relay.TupleGetItem(func_858_call(), 0)
func_807_call = mod.get_global_var('func_807')
func_810_call = mutated_mod.get_global_var('func_810')
var_1050 = relay.var("var_1050", dtype = "int32", shape = (847,))#candidate|1050|(847,)|var|int32
call_1049 = func_807_call(relay.reshape(var_1050.astype('int32'), [11, 11, 7]))
call_1051 = func_807_call(relay.reshape(var_1050.astype('int32'), [11, 11, 7]))
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_1052 = relay.TupleGetItem(func_856_call(), 0)
call_1053 = relay.TupleGetItem(func_858_call(), 0)
output = relay.Tuple([call_1043,call_1049,var_1050,call_1052,])
output2 = relay.Tuple([call_1044,call_1051,var_1050,call_1053,])
func_1087 = relay.Function([var_1050,], output)
mod['func_1087'] = func_1087
mod = relay.transform.InferType()(mod)
mutated_mod['func_1087'] = func_1087
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1088 = relay.var("var_1088", dtype = "int32", shape = (847,))#candidate|1088|(847,)|var|int32
func_1087_call = mutated_mod.get_global_var('func_1087')
call_1089 = func_1087_call(var_1088)
output = call_1089
func_1090 = relay.Function([var_1088], output)
mutated_mod['func_1090'] = func_1090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_1123 = relay.TupleGetItem(func_856_call(), 0)
call_1124 = relay.TupleGetItem(func_858_call(), 0)
output = relay.Tuple([call_1123,])
output2 = relay.Tuple([call_1124,])
func_1126 = relay.Function([], output)
mod['func_1126'] = func_1126
mod = relay.transform.InferType()(mod)
output = func_1126()
func_1127 = relay.Function([], output)
mutated_mod['func_1127'] = func_1127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_1165 = relay.TupleGetItem(func_856_call(), 0)
call_1166 = relay.TupleGetItem(func_858_call(), 0)
func_1087_call = mod.get_global_var('func_1087')
func_1090_call = mutated_mod.get_global_var('func_1090')
const_1196 = relay.const([6,-3,-6,8,-10,-10,1,-5,10,2,5,-5,-4,5,8,-7,10,9,-4,-4,3,3,8,6,10,-10,-8,4,-5,3,8,10,-2,6,7,2,-5,-5,-7,-9,-8,3,-5,-10,-5,6,5,-3,-4,-4,-10,4,-5,8,-1,-10,7,-7,-10,3,-9,3,4,2,-7,-10,3,4,-4,-10,9,-3,3,9,6,1,2,9,9,5,-8,-5,-10,8,1,-10,-8,-7,5,-4,-1,-6,8,10,-7,-1,1,-5,-5,8,3,-4,-2,-3,8,-10,4,-1,-9,8,-7,10,-5,10,10,-5,5,5,2,-8,9,9,-2,-6,3,-9,-4,-8,-2,10,6,4,-5,-3,-8,5,-7,-1,-7,1,10,10,-7,-3,-7,-2,6,-6,-6,6,-8,-3,7,5,10,6,4,-2,-4,-9,-7,6,8,4,3,-9,-3,7,6,-6,5,-6,7,9,4,4,10,5,-4,-3,-1,7,7,-5,-5,9,4,9,3,5,-8,7,1,-8,-10,-1,5,6,1,3,4,-5,7,-2,-4,8,-7,9,-8,4,-8,-1,-4,-5,6,-10,9,-1,-1,-7,-9,6,9,-6,2,6,-5,-5,2,4,7,10,-3,-4,-1,9,9,8,1,-4,-3,7,7,-9,-3,7,-10,9,8,-8,-8,3,-4,-5,4,-2,-2,-7,2,-6,-10,6,-3,-3,-10,-2,-10,6,-5,-1,-2,7,1,-1,-3,-7,-3,3,9,7,-7,-10,3,10,-6,-8,-3,2,-3,6,-1,9,7,-2,-9,8,9,2,-5,-1,-3,-9,7,8,-6,6,-7,-3,-8,-3,-5,3,-10,-5,7,-5,-6,9,-8,5,-1,-1,-7,-5,3,-2,-10,10,1,-2,-3,1,3,-5,8,3,1,10,-2,3,-4,2,1,3,-9,-10,-3,-6,-2,-5,2,-10,6,1,6,3,-8,-5,1,10,-2,-4,3,1,-2,-6,6,7,5,-2,-1,-2,-2,-9,4,2,-2,-10,8,-10,8,5,1,6,8,-6,2,2,-4,6,-10,3,7,-9,-5,-7,5,6,2,2,1,2,8,9,3,-10,-8,-9,6,-1,-6,-5,8,9,-7,-3,2,4,-7,2,2,7,4,-4,1,-3,-4,10,-10,-6,-1,-7,-4,3,-6,3,6,8,5,2,9,-5,-4,7,-3,2,1,6,-10,7,3,-6,10,-1,-7,-1,10,9,10,-7,10,8,9,-5,3,7,-1,-7,6,-6,-2,-9,-2,6,8,-6,5,10,-7,4,-8,-10,-3,-10,6,2,-2,2,-1,7,-4,-8,6,-4,2,5,-9,8,3,-1,-3,-8,-3,-10,-1,-6,9,-3,-1,-10,-4,-4,9,5,10,-10,8,-10,10,-7,-9,3,8,-5,-2,-3,-1,9,9,-3,-1,-3,-2,-2,-5,3,-2,1,4,-9,10,-5,1,10,-10,-10,-5,2,8,-2,-4,4,-5,8,-3,-8,-10,-4,6,2,9,9,-7,-3,-6,7,-2,-6,7,6,10,3,-6,-1,-4,-2,-5,7,3,-6,-7,-7,-5,5,6,2,-7,7,5,-10,1,10,-3,9,-8,-5,9,5,-6,7,-4,-9,5,8,4,-7,-8,-2,-5,-6,-7,10,-4,1,7,-3,7,4,8,2,-10,6,7,10,10,-6,7,-4,-3,1,2,-5,-6,1,-10,3,-1,9,-8,1,-3,4,5,2,-4,1,7,-3,4,-6,-6,-6,9,-6,-2,-4,3,8,-7,-7,-3,4,-4,-4,2,3,-8,-4,4,-3,-6,5,6,-7,-4,-3,5,-9,-6,-7,1,-4,-1,-8,-8,-3,-8,4,-2,7,7,4,-9,1,4,-2,8,-7,-6,-3,-6,1,-7,-9,5,-6,8,-6,-3,-2,5,-3,2,3,5,-4,-4,-8,-9,-1,-5,-1,-7,1,6,-6,-9,-5,10,-1,-5,7,-2,-10,4,-7,8,-5,7,-2,1,-3,8,-3,5,3,-3,-9,7,-5,-1,-9,2,-2,10,-1,6,3,-1,10,2,-8,-4,-7,-6,-2,-9,-6,7,-2,-5,-9,-5,3,-9,-4,8,6,-8,-5,-7,3,-7,9,-6,2,3,2,-4,-4,10,3,-9,-2,-2,-1,-1,7,3,4,6,-1,-7,-7,-8,5,-10,-7,-9,-5,-3,2,-1,4,6,5,3,-10,-1,-3,-9,-8,-9,5,-2,-9,-7,9,-1,-5,-2,-8,6,-7,-5,7,-1,1,10,5,8,-6,-4,-6,9,-1,-10], dtype = "int32")#candidate|1196|(847,)|const|int32
call_1195 = relay.TupleGetItem(func_1087_call(relay.reshape(const_1196.astype('int32'), [847,])), 0)
call_1197 = relay.TupleGetItem(func_1090_call(relay.reshape(const_1196.astype('int32'), [847,])), 0)
var_1203 = relay.var("var_1203", dtype = "int32", shape = (847,))#candidate|1203|(847,)|var|int32
bop_1204 = relay.right_shift(const_1196.astype('uint64'), relay.reshape(var_1203.astype('uint64'), relay.shape_of(const_1196))) # shape=(847,)
output = relay.Tuple([call_1165,call_1195,bop_1204,])
output2 = relay.Tuple([call_1166,call_1197,bop_1204,])
func_1222 = relay.Function([var_1203,], output)
mod['func_1222'] = func_1222
mod = relay.transform.InferType()(mod)
mutated_mod['func_1222'] = func_1222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1223 = relay.var("var_1223", dtype = "int32", shape = (847,))#candidate|1223|(847,)|var|int32
func_1222_call = mutated_mod.get_global_var('func_1222')
call_1224 = func_1222_call(var_1223)
output = call_1224
func_1225 = relay.Function([var_1223], output)
mutated_mod['func_1225'] = func_1225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_1241 = relay.TupleGetItem(func_856_call(), 0)
call_1242 = relay.TupleGetItem(func_858_call(), 0)
var_1255 = relay.var("var_1255", dtype = "float32", shape = (7, 14, 4))#candidate|1255|(7, 14, 4)|var|float32
bop_1256 = relay.bitwise_or(call_1241.astype('uint16'), relay.reshape(var_1255.astype('uint16'), relay.shape_of(call_1241))) # shape=(7, 14, 4)
bop_1259 = relay.bitwise_or(call_1242.astype('uint16'), relay.reshape(var_1255.astype('uint16'), relay.shape_of(call_1242))) # shape=(7, 14, 4)
func_807_call = mod.get_global_var('func_807')
func_810_call = mutated_mod.get_global_var('func_810')
const_1276 = relay.const([3,2,-6,-8,-5,-3,-6,3,5,-3,10,6,-4,4,-9,8,-6,3,-3,8,9,3,10,9,-9,-4,-10,-10,7,2,1,-10,-2,1,-4,-5,2,-10,3,8,10,1,-4,-2,5,5,-4,2,-7,-3,-6,8,6,8,5,-1,10,5,-3,3,1,-5,-4,-2,2,6,4,5,9,-1,-3,-9,6,-5,1,8,-7,-6,10,1,-3,-1,10,1,1,-4,-4,-7,7,9,1,9,-8,8,4,1,6,-6,-10,-6,9,-7,-2,-3,-6,4,-10,5,7,8,-3,-1,-3,-7,-6,-5,-2,-7,-7,-1,5,-2,10,2,1,1,1,6,8,6,-8,-8,1,5,10,-3,-3,7,-2,-3,3,10,-5,-7,-2,9,-1,-10,-6,2,-3,8,-8,1,8,-5,-7,2,-1,-9,1,3,-6,-6,-10,-8,-3,-8,5,-3,3,-1,-2,4,-1,8,-10,-4,6,1,-10,8,9,-4,-5,-5,-2,-1,-9,-10,10,4,3,-8,-2,4,2,-3,9,-5,-4,-3,7,3,-10,10,-4,-10,6,3,-1,-8,-2,5,-10,-6,-1,1,4,5,8,4,10,7,5,2,1,-10,2,-2,6,-7,8,4,-1,-6,2,8,-3,8,7,4,3,-10,-1,-9,10,-3,-1,10,6,10,-3,2,7,6,1,1,5,-8,4,3,-3,-4,-5,-8,-10,1,-1,1,-2,-10,-8,6,2,10,-3,-2,3,-3,-10,-1,1,6,-2,10,6,6,2,-7,-6,-10,2,-7,8,3,-3,8,6,-8,1,-2,-7,-10,10,3,4,7,5,-3,6,-1,-2,-4,3,7,-9,2,9,5,9,7,3,-9,10,3,8,6,3,8,-2,-3,-4,-7,6,2,1,-7,5,-7,10,4,4,-7,10,6,-10,10,-1,-9,-10,2,-2,10,-7,-6,-6,4,-10,8,8,-9,2,-4,-8,-2,4,4,3,7,10,6,4,6,2,-4,-8,7,-4,-3,-4,5,-8,-5,-2,10,6,5,-7,3,-7,-10,-10,4,-7,-8,-1,10,1,-10,-10,2,8,5,10,-5,-5,-1,1,10,-2,3,-1,-1,-10,3,1,7,5,-5,2,-4,-6,-3,-8,-6,-1,-4,-2,3,5,-4,-3,8,-5,-3,-4,5,1,6,10,2,3,-2,-10,-8,2,3,-5,3,5,-8,-2,8,10,3,-8,-9,-10,7,-7,6,9,5,2,5,-4,6,-5,-7,10,4,4,8,-6,5,2,-3,1,-8,-7,-2,-7,5,3,-6,6,1,-3,6,-8,5,10,-2,7,8,2,-5,8,-10,3,-4,-7,-9,-7,-2,-5,4,4,-10,7,-6,-8,9,-10,7,-6,2,-7,4,7,-1,-2,10,3,8,8,9,5,-9,7,-8,-8,-6,3,-3,7,-7,-8,-6,8,1,10,-1,-9,9,8,-1,-10,-3,9,5,7,5,-10,-8,-7,-2,10,1,6,5,7,-2,5,2,-9,-1,1,-4,9,7,1,-2,-5,-10,2,6,-1,8,2,-1,-9,9,-8,-10,7,2,7,10,-6,-4,6,-10,8,5,10,-3,8,-6,7,3,3,5,-9,5,-5,-6,9,-8,-5,-7,8,-1,-1,3,5,3,1,-10,-3,8,4,-9,-1,9,9,-9,3,-3,7,4,4,-9,-7,7,-4,10,-10,-8,-7,5,3,4,3,2,-5,-3,-6,-6,-1,-5,-10,2,3,1,9,7,-1,9,8,6,-2,4,3,-2,-3,-1,1,2,-5,5,2,-5,-3,-9,-10,8,-5,-9,-2,-5,8,-7,9,-7,4,-8,6,-9,10,1,4,1,10,10,-10,9,8,9,5,2,7,-4,-3,-1,-3,-4,-10,6,6,-3,10,-6,-8,-8,2,2,9,-2,1,7,6,10,-8,-7,4,-5,-4,3,-8,4,-10,-9,4,-1,-5,-8,-2,6,-7,-6,-2,5,2,7,10,9,-10,9,2,-1,-10,9,-9,4,7,-7,1,-5,10,4,-5,-10,-5,-1,10,-3,2,2,6,-7,6,-2,-6,1,-10,7,-1,-2,-7,1,-6,-6,8,-2,-4,7,-3,-6,-7,6,-1,5,-10,-8,2,4,8,8,8,10,9,1,-10,4,1,7,2,5,8,1,-5,-8,5,-8,-6,-6,-8,10,1,7,5,-7,5,1,7,5,-6,-4,-9,-5,-1,-3,-5,8,8,-9,1,-9,10,-2,-1,7,-10,-10,3], dtype = "int32")#candidate|1276|(847,)|const|int32
call_1275 = func_807_call(relay.reshape(const_1276.astype('int32'), [11, 11, 7]))
call_1277 = func_807_call(relay.reshape(const_1276.astype('int32'), [11, 11, 7]))
output = relay.Tuple([bop_1256,call_1275,const_1276,])
output2 = relay.Tuple([bop_1259,call_1277,const_1276,])
func_1279 = relay.Function([var_1255,], output)
mod['func_1279'] = func_1279
mod = relay.transform.InferType()(mod)
mutated_mod['func_1279'] = func_1279
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1280 = relay.var("var_1280", dtype = "float32", shape = (7, 14, 4))#candidate|1280|(7, 14, 4)|var|float32
func_1279_call = mutated_mod.get_global_var('func_1279')
call_1281 = func_1279_call(var_1280)
output = call_1281
func_1282 = relay.Function([var_1280], output)
mutated_mod['func_1282'] = func_1282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_1301 = relay.TupleGetItem(func_856_call(), 0)
call_1302 = relay.TupleGetItem(func_858_call(), 0)
output = relay.Tuple([call_1301,])
output2 = relay.Tuple([call_1302,])
func_1303 = relay.Function([], output)
mod['func_1303'] = func_1303
mod = relay.transform.InferType()(mod)
output = func_1303()
func_1304 = relay.Function([], output)
mutated_mod['func_1304'] = func_1304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_1308 = relay.TupleGetItem(func_988_call(), 0)
call_1309 = relay.TupleGetItem(func_990_call(), 0)
uop_1319 = relay.asinh(call_1308.astype('float64')) # shape=(7, 14, 4)
uop_1321 = relay.asinh(call_1309.astype('float64')) # shape=(7, 14, 4)
output = uop_1319
output2 = uop_1321
func_1322 = relay.Function([], output)
mod['func_1322'] = func_1322
mod = relay.transform.InferType()(mod)
mutated_mod['func_1322'] = func_1322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mutated_mod.get_global_var('func_1322')
call_1323 = func_1322_call()
output = call_1323
func_1324 = relay.Function([], output)
mutated_mod['func_1324'] = func_1324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_1396 = relay.TupleGetItem(func_1126_call(), 0)
call_1397 = relay.TupleGetItem(func_1127_call(), 0)
func_931_call = mod.get_global_var('func_931')
func_934_call = mutated_mod.get_global_var('func_934')
const_1399 = relay.const([5,10,-4,-5,8,-4,5,-9,-8,-4,-4,1,-9,-10,-8,10,-4,-1,1,-9,-8,-7,5,-9,-1,-3,-10,-8,3,-3,-2,-4,-5,5,1,-8,-7,1,3,4,3,-6,2,-1,2,7,6,10,-6,-9,1,5,2,-1,-6,-8,6,1,10,4,5,-7,1,-4,4,-6,-3,-6,-7,-2,4,3,4,8,7,5,3,2,-9,3,-2,-2,-9,9,-5,-8,-9,-1,-4,-4,-2,10,-10,1,1,-5,-2,5,5,-5,5,1,4,-6,2,-9,8,2,-4,-7,5,-5,9,8,3,4,7,-1,-7,1,-6,6,10,2,-8,-8,-3,2,4,-3,3,7,3,3,5,-9,-2,5,-10,-7,-7,3,-9,-1,-5,4,-4,-8,-8,-6,4,-4,-10,-8,7,3,2,6,-1,6,3,-3,-10,-3,1,3,-7,-2,9,1,7,2,10,-1,-6,8,-9,-8,4,-1,-3,10,5,-8,4,-10,3,-10,-1,5,-2,-7,-6,3,-6,-4,-1,8,-6,8,-6,-1,-10,2,-4,9,2,8,-10,-7,-5,5,3,10,10,1,8,-4,5,-10,-5,-6,4,6,-2,2,1,-3,-1,-6,-3,-8,9,9,-10,-4,9,-1,-3,-1,-7,2,10,-2,10,-3,-5,4,-5,-9,-4,-7,2,-10,-6,-9,1,2,-9,-2,4,-2,8,-4,-8,7,7,-5,-3,-1,-5,1,4,-7,10,3,-9,-3,-10,-10,-2,-8,-1,6,-9,3,9,-10,-9,-7,-10,-1,5,6,10,2,2,-9,-7,9,3,-10,5,-7,-8,-3,7,7,-9,7,-8,-1,1,3,8,3,-3,-6,-6,-7,9,5,4,-8,-3,-2,4,-1,-7,4,-8,7,-4,4,-5,-4,-8,10,9,7,-3,-2,4,5,-8,5,7,-9,-4,-9,-1,5,2,-3,5,2,9,-6,-5,-2,-1,-1,10,1,1,7,5,-1,-7,-7,-4,-10,-10,4,9,-2,-7,-3,1,3,6,-5,-1,-9,3,-1,-2,10,7,-1,1,1,4,-7,9,-10,1,7,4,-10,-9,-5,-2,-7,10,7,9,1,3,-2,-9,7,-8,2,8,10,-3,-2,-10,3,-7,3,-2,1,4,8,-6,3,-9,7,-9,7,-1,-6,-10,-3,1,2,2,-9,-9,-2,-9,-10,-2,-8,-1,10,5,-5,4,9,5,9,9,6,4,-4,2,3,-10,-4,7,-4,-1,7,-8,3,10,-3,-1,-8,8,9,-5,-6,5,-5,-6,-5,10,4,-10,3,10,-10,6,7,-7,6,9,6,-1,-6,-2,4,3,-9,-5,-3,-10,-6,-1,2,9,2,1,-4,9,-1,-1,2,-3,6,-3,2,4,-10,1,4,2,-10,4,-7,-5,3,-1,1,3,-1,8,10,1,8,-3,-2,8,8,-7,2,-3,-8,-7,-10,6,-9,-5,8,-8,-8,9,-6,3,9,-8,3,-6,-6,10,7,7,4,-4,8,9,5,-5,6,-4,9,6,5,-5,-8,7,2,-1,6,9,9,9,7,-2,1,6,10,-3,5,-6,-4,-6,8,3,3,9,1,4,1,10,6,3,-7,10,6,-3,-10,-7,8,-4,3,3,-1,-3,-4,6,9,5,8,10,-3,4,-3,2,10,-2,-1,-10,-1,5,-6,-7,-10,2,8,-2,4,6,5,-9,-6,-2,4,-9,5,-2,5,-5,-2,1,-9,-2,-8,-10,-6,10,10,7,3,2,-10,-6,-4,7,8,-5,-2,-9,3,5,-10,9,6,7,2,7,4,6,-6,1,3,-10,2,7,-1,-5,5,3,2,3,1,-7,-3,2,-5,3,8,-3,5,6,-10,8,-4,9,3,1,9,-9,-8,2,-6,1,8,-4,4,8,-2,-1,7,4,1,-6,-3,5,-7,-5,1,9,-8,2,-5,-7,-7,5,8,6,5,2,-10,-9,5,2,-10,5,3,1,8,-5,6,-8,1,6,9,-6,-8,-6,9,-8,6,-8,-1,-7,6,-3,-3,-9,-9,2,4,7,-5,2,2,4,3,8,-10,4,-8,8,-2], dtype = "uint8")#candidate|1399|(780,)|const|uint8
call_1398 = relay.TupleGetItem(func_931_call(relay.reshape(const_1399.astype('uint8'), [390, 2])), 0)
call_1400 = relay.TupleGetItem(func_934_call(relay.reshape(const_1399.astype('uint8'), [390, 2])), 0)
func_1038_call = mod.get_global_var('func_1038')
func_1041_call = mutated_mod.get_global_var('func_1041')
const_1402 = relay.const([[-10,-4],[9,-8],[8,-8],[-1,-7],[-1,6],[-10,3],[-3,-2],[10,7],[7,2],[9,-7],[-1,10],[-1,-4],[-9,-4],[-7,2],[5,-2],[6,-5],[-3,8],[-9,1],[-10,-2],[7,5],[-6,-7],[-5,3],[-5,-7],[6,-3],[-10,-3],[8,9],[-2,-10],[6,-4],[-4,5],[2,-9],[3,-7],[7,10],[-10,6],[-4,7],[5,4],[3,-6],[-1,-8],[1,7],[3,-4],[3,-10],[4,3],[3,3],[-7,1],[-5,1],[-8,-8],[-6,2],[10,-4],[10,7],[1,10],[-2,-4],[-10,-1],[4,2],[10,-10],[8,10],[7,-2],[-7,1],[-1,-4],[3,-3],[4,9],[-7,9],[-2,8],[2,7],[-1,8]], dtype = "uint8")#candidate|1402|(63, 2)|const|uint8
call_1401 = relay.TupleGetItem(func_1038_call(relay.reshape(const_1402.astype('uint8'), [9, 7, 2]), relay.reshape(const_1399.astype('uint8'), [780,]), ), 2)
call_1403 = relay.TupleGetItem(func_1041_call(relay.reshape(const_1402.astype('uint8'), [9, 7, 2]), relay.reshape(const_1399.astype('uint8'), [780,]), ), 2)
func_1222_call = mod.get_global_var('func_1222')
func_1225_call = mutated_mod.get_global_var('func_1225')
var_1413 = relay.var("var_1413", dtype = "int32", shape = (847,))#candidate|1413|(847,)|var|int32
call_1412 = relay.TupleGetItem(func_1222_call(relay.reshape(var_1413.astype('int32'), [847,])), 0)
call_1414 = relay.TupleGetItem(func_1225_call(relay.reshape(var_1413.astype('int32'), [847,])), 0)
output = relay.Tuple([call_1396,call_1398,const_1399,call_1401,const_1402,call_1412,var_1413,])
output2 = relay.Tuple([call_1397,call_1400,const_1399,call_1403,const_1402,call_1414,var_1413,])
func_1426 = relay.Function([var_1413,], output)
mod['func_1426'] = func_1426
mod = relay.transform.InferType()(mod)
var_1427 = relay.var("var_1427", dtype = "int32", shape = (847,))#candidate|1427|(847,)|var|int32
output = func_1426(var_1427)
func_1428 = relay.Function([var_1427], output)
mutated_mod['func_1428'] = func_1428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_1430 = relay.TupleGetItem(func_1126_call(), 0)
call_1431 = relay.TupleGetItem(func_1127_call(), 0)
func_1038_call = mod.get_global_var('func_1038')
func_1041_call = mutated_mod.get_global_var('func_1041')
const_1451 = relay.const([5,-3,9,4,7,-7,1,-4,-3,10,-10,-1,7,4,10,1,7,6,9,9,3,-7,-10,-5,-7,-2,-7,9,6,-1,1,4,8,-5,-9,5,2,6,-2,-5,-5,9,-2,5,-2,-6,2,2,-9,9,1,8,5,-5,5,7,9,-2,-4,10,-7,10,8,1,1,3,-3,7,-5,4,-4,-9,-9,-5,2,-9,-6,8,3,1,-9,-7,-5,10,-7,-9,-7,6,-1,-9,8,10,8,-8,-9,-6,3,-1,-8,-10,5,-7,-10,-8,-4,4,4,-6,3,-5,10,1,3,-4,10,5,5,-8,5,-8,3,-2,7,1,-1,4], dtype = "uint8")#candidate|1451|(126,)|const|uint8
var_1452 = relay.var("var_1452", dtype = "uint8", shape = (1, 780))#candidate|1452|(1, 780)|var|uint8
call_1450 = relay.TupleGetItem(func_1038_call(relay.reshape(const_1451.astype('uint8'), [9, 7, 2]), relay.reshape(var_1452.astype('uint8'), [780,]), ), 0)
call_1453 = relay.TupleGetItem(func_1041_call(relay.reshape(const_1451.astype('uint8'), [9, 7, 2]), relay.reshape(var_1452.astype('uint8'), [780,]), ), 0)
output = relay.Tuple([call_1430,call_1450,const_1451,var_1452,])
output2 = relay.Tuple([call_1431,call_1453,const_1451,var_1452,])
func_1456 = relay.Function([var_1452,], output)
mod['func_1456'] = func_1456
mod = relay.transform.InferType()(mod)
mutated_mod['func_1456'] = func_1456
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1457 = relay.var("var_1457", dtype = "uint8", shape = (1, 780))#candidate|1457|(1, 780)|var|uint8
func_1456_call = mutated_mod.get_global_var('func_1456')
call_1458 = func_1456_call(var_1457)
output = call_1458
func_1459 = relay.Function([var_1457], output)
mutated_mod['func_1459'] = func_1459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_1464 = func_1322_call()
call_1465 = func_1322_call()
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
var_1469 = relay.var("var_1469", dtype = "int32", shape = (77, 11))#candidate|1469|(77, 11)|var|int32
call_1468 = relay.TupleGetItem(func_1426_call(relay.reshape(var_1469.astype('int32'), [847,])), 0)
call_1470 = relay.TupleGetItem(func_1428_call(relay.reshape(var_1469.astype('int32'), [847,])), 0)
const_1471 = relay.const([[-10,7,-3,6,2,4,-10,8,-3,9,2],[10,-1,-10,5,-2,-3,2,-1,-9,10,6],[2,-6,-2,6,4,9,-1,4,7,2,4],[-7,4,7,-9,-4,6,10,6,-9,4,-8],[8,-2,7,-8,-7,7,9,7,-8,1,-4],[-1,6,1,-9,-6,10,-6,1,-1,9,2],[-3,-7,4,4,-10,-6,-4,-8,-7,-3,-10],[5,5,2,5,1,4,6,8,6,4,6],[-1,2,9,-7,6,-2,10,-2,-7,1,-1],[-9,-9,-6,-9,1,-7,9,10,-4,-10,5],[8,4,-10,-7,4,-1,3,5,2,-5,1],[-6,2,7,-6,-1,-2,2,-10,5,6,-6],[-7,-4,-7,9,-3,-8,5,-6,-6,7,-1],[-9,9,6,4,-8,-3,10,-1,9,-4,-10],[10,1,-4,5,-9,-8,-10,6,6,-5,-8],[10,-3,-5,4,7,-3,2,-9,5,-3,8],[7,7,10,2,-6,7,-1,-8,8,-1,-4],[-8,-1,-2,-4,-8,-6,4,-9,-4,-1,6],[-3,-9,8,10,6,-8,1,-9,-2,-5,4],[-4,8,-7,1,10,-6,3,-2,9,-10,-5],[6,-5,-1,-7,-2,7,1,10,7,-3,1],[-8,-8,-3,1,9,-1,6,-9,-6,-1,2],[5,1,-1,7,-10,-9,2,-7,9,10,4],[-10,6,3,-9,1,-6,7,7,-3,9,-5],[3,1,10,10,7,7,7,3,7,-9,-6],[-2,10,-4,-7,-7,-3,-2,2,-8,-1,-6],[-7,4,3,-6,-8,6,6,-7,10,-5,4],[7,9,-9,-2,-9,-4,-2,-6,9,-9,-4],[-4,-9,-6,-9,-2,-10,-4,1,4,7,-3],[-4,-1,5,-8,6,9,-8,2,7,6,4],[4,7,7,5,-5,1,4,8,2,-5,1],[-5,-3,-6,-8,8,-8,-2,-1,5,8,3],[-9,-3,3,3,5,7,-10,8,7,-4,3],[8,-2,9,8,-9,3,9,2,-1,9,7],[-5,9,-1,5,-8,-7,7,-10,1,5,3],[-9,-5,2,-10,-5,-3,7,9,9,6,-10],[5,-9,9,-10,7,7,-10,7,-9,-7,1],[8,3,-9,-7,-1,9,9,-3,10,8,3],[6,10,-4,-8,8,-5,5,-1,3,5,3],[7,10,-7,5,-6,1,6,10,8,-10,-8],[-7,7,2,-1,3,2,-7,4,10,3,-6],[5,-5,-6,10,-1,-5,-8,-10,10,8,9],[-1,-9,2,2,-3,6,4,2,-5,10,1],[5,-8,5,8,-1,-8,10,2,-10,1,-2],[7,8,9,10,-5,-1,1,-8,3,-8,10],[3,-1,9,-10,-6,9,8,1,7,-4,-10],[-6,4,10,10,-1,5,7,-4,7,5,6],[-3,3,5,-10,-4,7,-8,1,8,3,6],[7,9,1,-1,7,-4,-8,10,5,-4,4],[-9,2,-9,-1,6,-6,-4,-1,2,3,-10],[6,-8,-4,5,-6,4,-4,-10,-7,-2,1],[10,3,10,9,-4,10,9,-4,-1,-1,-6],[-8,-9,-5,8,7,10,1,3,-1,-6,-8],[-6,-9,5,-4,6,-9,8,4,-2,5,8],[-3,5,-9,-7,-4,-1,10,5,-9,5,-6],[4,9,10,9,10,-10,-5,4,7,-5,-4],[-6,-8,-2,5,-7,5,-6,-2,4,6,-6],[4,-3,9,1,10,2,4,-4,-1,9,-9],[-2,7,-2,9,-4,-8,-4,-2,2,-4,-1],[-8,9,-7,7,3,-4,5,-3,-6,9,-3],[-2,-10,6,-1,-4,5,-10,4,-6,-7,9],[-8,8,1,-9,10,9,8,-4,4,7,5],[-2,5,8,-10,-3,9,-4,9,-5,9,-9],[-9,5,2,5,-1,8,4,-9,-5,5,-4],[-6,-4,-1,3,9,2,-7,8,-6,8,-7],[2,-7,8,2,-10,-6,7,7,-7,4,-10],[6,3,-9,5,-5,9,3,5,1,4,-2],[-5,1,-5,1,-5,5,8,1,7,-10,10],[-6,-1,-10,2,-5,1,9,10,3,-7,-7],[2,8,-6,8,4,-2,-10,-9,6,-9,10],[3,8,-9,-4,-7,6,6,4,9,7,-2],[-4,9,-4,5,6,6,-5,6,1,6,9],[-9,-5,10,8,8,4,1,4,4,7,-4],[4,2,3,3,7,6,8,3,-1,-9,-6],[5,-8,4,10,8,7,-1,5,4,-4,5],[10,2,-8,-6,-3,8,1,-7,-7,-9,2],[-5,-4,10,-3,1,-2,3,-6,-6,-2,-8]], dtype = "int32")#candidate|1471|(77, 11)|const|int32
bop_1472 = relay.divide(var_1469.astype('float32'), relay.reshape(const_1471.astype('float32'), relay.shape_of(var_1469))) # shape=(77, 11)
uop_1478 = relay.sin(const_1471.astype('float32')) # shape=(77, 11)
bop_1485 = relay.floor_mod(uop_1478.astype('float32'), relay.reshape(const_1471.astype('float32'), relay.shape_of(uop_1478))) # shape=(77, 11)
func_931_call = mod.get_global_var('func_931')
func_934_call = mutated_mod.get_global_var('func_934')
const_1493 = relay.const([-8,-8,-3,-2,-6,-9,8,-10,7,6,-8,-9,10,10,-4,8,3,4,2,-6,-7,-1,-3,7,-8,1,9,-7,-9,-10,3,4,6,3,6,-6,-2,-9,-7,6,-9,-3,8,7,10,-10,-5,-8,2,9,-1,-2,4,-10,8,-8,3,-5,-5,10,-10,-6,-5,-8,-6,-7,-3,-9,-10,10,5,3,1,-2,-2,2,3,9,-2,8,-5,4,4,5,-2,-2,-4,8,-4,-2,1,8,-1,3,-3,1,6,6,-1,-5,-7,-2,3,4,10,-4,9,-6,-9,4,-10,10,2,-7,8,-8,1,5,1,9,-7,-4,-5,7,-7,-7,-7,2,-4,6,3,6,5,-5,-3,2,9,6,-4,9,-5,-8,-3,4,1,1,6,-7,-1,9,-9,1,7,-4,-2,4,-9,-10,5,10,-3,-2,-10,-2,-1,2,4,-10,3,-1,4,10,8,-6,5,-2,8,-9,-3,7,2,6,5,6,-9,-10,-2,8,2,6,-1,6,-2,-8,-6,3,-6,-3,-6,-6,-7,9,1,-1,1,-2,8,10,5,-7,2,-8,-10,9,9,10,-6,-7,-6,9,8,10,9,5,9,-4,1,-1,-4,-8,6,1,9,-8,-6,2,10,9,-3,5,6,3,3,10,-4,2,-8,-3,-9,-4,2,9,10,-5,-2,-5,2,-8,3,4,-8,-9,-7,5,-5,-3,5,-1,1,7,6,2,9,-5,-9,10,-5,-6,-9,-10,-8,-3,6,7,8,1,-4,-4,-6,-5,-7,-2,2,-5,-9,-7,-2,9,2,7,7,-6,2,6,-6,-3,-4,5,5,6,9,-2,-4,8,8,-8,3,8,3,-3,2,5,-3,1,2,-3,-3,-9,7,-4,3,1,-7,1,-2,-10,4,-2,6,4,-3,9,3,2,7,4,10,-8,-6,-7,-5,5,-4,6,-2,-8,-9,-2,8,4,-2,5,-6,6,-2,-2,-2,8,-6,6,7,5,-4,10,-3,-7,-5,-6,7,-4,-9,-8,3,-6,2,-7,9,-5,-8,-5,1,7,-4,8,-9,10,9,8,6,1,8,-7,9,-2,-8,2,-8,-7,4,-4,8,-8,6,6,-9,-9,4,-8,7,2,4,7,2,6,7,-8,6,9,1,-3,4,-9,-8,-5,-6,2,-2,-4,1,10,-10,3,4,7,1,8,-3,-6,-6,8,8,2,9,4,-5,-7,5,-10,-4,-4,6,10,9,-10,9,-6,8,-8,-3,-6,-9,3,5,-4,-10,-3,10,-8,3,5,6,10,-9,-10,1,3,8,-5,-1,1,-7,10,2,-8,3,-7,-5,2,3,6,-7,5,7,10,9,9,-8,5,4,4,-9,8,-8,-5,4,5,2,-9,-2,-5,10,8,3,-1,9,8,-6,9,9,-5,7,6,-1,-8,-4,1,9,6,-5,10,-10,-1,5,2,-7,-8,-6,4,7,-8,7,7,-1,7,-7,1,3,6,3,1,5,-4,4,-8,-2,-4,-8,-4,-3,6,-5,-9,-8,-8,5,2,-1,-10,-8,5,-7,-8,1,3,-2,6,-5,-6,4,-7,-3,10,9,8,10,-7,4,1,9,1,-2,-9,-6,3,8,10,9,7,9,5,-1,-6,10,-2,1,10,-2,2,3,7,-5,7,6,2,-1,7,-9,-7,-10,8,4,-7,-7,4,6,3,10,-5,-4,-4,-4,-7,5,2,6,-9,7,5,-8,-4,-2,-6,-5,-9,-8,5,3,6,7,5,7,-2,-1,8,7,4,7,10,-10,2,-3,1,9,5,-5,-9,-4,7,-9,-5,-5,6,8,5,-6,-8,-3,6,-8,10,-9,8,-2,-9,9,9,-4,7,2,1,-10,6,10,7,-1,5,-4,5,9,-8,9,-4,2,-4,7,2,-6,3,10,-8,-5,-3,6,-6,4,-5,1,8,5,8,9,9,6,-3,-2,-7,2,7,-10,4,6,8,1,3,-10,-7,-8,-4,8,3,6,6,-2,7,3,7,-3,9,9,-9,2,7,2,-6,-9,-10,-3,-7,7,-8,-7,2,-7,3,4,6,8,5,7,10], dtype = "uint8")#candidate|1493|(780,)|const|uint8
call_1492 = relay.TupleGetItem(func_931_call(relay.reshape(const_1493.astype('uint8'), [390, 2])), 0)
call_1494 = relay.TupleGetItem(func_934_call(relay.reshape(const_1493.astype('uint8'), [390, 2])), 0)
var_1508 = relay.var("var_1508", dtype = "float32", shape = (77, 11))#candidate|1508|(77, 11)|var|float32
bop_1509 = relay.not_equal(bop_1485.astype('bool'), relay.reshape(var_1508.astype('bool'), relay.shape_of(bop_1485))) # shape=(77, 11)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_1522 = relay.TupleGetItem(func_1426_call(relay.reshape(bop_1472.astype('int32'), [847,])), 2)
call_1523 = relay.TupleGetItem(func_1428_call(relay.reshape(bop_1472.astype('int32'), [847,])), 2)
uop_1529 = relay.atan(var_1469.astype('float32')) # shape=(77, 11)
uop_1537 = relay.log(uop_1478.astype('float32')) # shape=(77, 11)
output = relay.Tuple([call_1464,call_1468,bop_1472,call_1492,const_1493,bop_1509,call_1522,uop_1529,uop_1537,])
output2 = relay.Tuple([call_1465,call_1470,bop_1472,call_1494,const_1493,bop_1509,call_1523,uop_1529,uop_1537,])
func_1553 = relay.Function([var_1469,var_1508,], output)
mod['func_1553'] = func_1553
mod = relay.transform.InferType()(mod)
var_1554 = relay.var("var_1554", dtype = "int32", shape = (77, 11))#candidate|1554|(77, 11)|var|int32
var_1555 = relay.var("var_1555", dtype = "float32", shape = (77, 11))#candidate|1555|(77, 11)|var|float32
output = func_1553(var_1554,var_1555,)
func_1556 = relay.Function([var_1554,var_1555,], output)
mutated_mod['func_1556'] = func_1556
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1565 = relay.var("var_1565", dtype = "float64", shape = (10, 6, 1))#candidate|1565|(10, 6, 1)|var|float64
uop_1566 = relay.sinh(var_1565.astype('float64')) # shape=(10, 6, 1)
output = uop_1566
output2 = uop_1566
func_1577 = relay.Function([var_1565,], output)
mod['func_1577'] = func_1577
mod = relay.transform.InferType()(mod)
var_1578 = relay.var("var_1578", dtype = "float64", shape = (10, 6, 1))#candidate|1578|(10, 6, 1)|var|float64
output = func_1577(var_1578)
func_1579 = relay.Function([var_1578], output)
mutated_mod['func_1579'] = func_1579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1303_call = mod.get_global_var('func_1303')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_1611 = relay.TupleGetItem(func_1303_call(), 0)
call_1612 = relay.TupleGetItem(func_1304_call(), 0)
output = call_1611
output2 = call_1612
func_1626 = relay.Function([], output)
mod['func_1626'] = func_1626
mod = relay.transform.InferType()(mod)
output = func_1626()
func_1627 = relay.Function([], output)
mutated_mod['func_1627'] = func_1627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_1642 = func_1322_call()
call_1643 = func_1322_call()
var_1644 = relay.var("var_1644", dtype = "float64", shape = (7, 14, 4))#candidate|1644|(7, 14, 4)|var|float64
bop_1645 = relay.less_equal(call_1642.astype('bool'), relay.reshape(var_1644.astype('bool'), relay.shape_of(call_1642))) # shape=(7, 14, 4)
bop_1648 = relay.less_equal(call_1643.astype('bool'), relay.reshape(var_1644.astype('bool'), relay.shape_of(call_1643))) # shape=(7, 14, 4)
output = bop_1645
output2 = bop_1648
func_1664 = relay.Function([var_1644,], output)
mod['func_1664'] = func_1664
mod = relay.transform.InferType()(mod)
var_1665 = relay.var("var_1665", dtype = "float64", shape = (7, 14, 4))#candidate|1665|(7, 14, 4)|var|float64
output = func_1664(var_1665)
func_1666 = relay.Function([var_1665], output)
mutated_mod['func_1666'] = func_1666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1626_call = mod.get_global_var('func_1626')
func_1627_call = mutated_mod.get_global_var('func_1627')
call_1671 = func_1626_call()
call_1672 = func_1626_call()
output = call_1671
output2 = call_1672
func_1673 = relay.Function([], output)
mod['func_1673'] = func_1673
mod = relay.transform.InferType()(mod)
output = func_1673()
func_1674 = relay.Function([], output)
mutated_mod['func_1674'] = func_1674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_1680 = func_1322_call()
call_1681 = func_1322_call()
func_1038_call = mod.get_global_var('func_1038')
func_1041_call = mutated_mod.get_global_var('func_1041')
const_1683 = relay.const([-10,-4,-4,4,-1,-8,-7,5,-6,-2,10,4,1,-2,-6,7,-1,-4,5,-7,-4,-9,9,10,3,-6,-6,-6,2,7,8,-5,-4,4,-6,8,-9,4,10,-5,8,3,-4,10,-8,6,-8,5,-10,3,-3,10,9,9,-10,10,6,1,-4,-7,-5,-8,-6,6,3,5,-2,7,-1,-1,-3,-10,-8,-10,-1,5,-4,10,8,-9,7,9,9,3,6,-2,8,-9,-2,-9,10,8,8,5,3,-1,7,2,-9,9,-10,6,4,4,-6,8,6,-1,3,-4,-1,-9,-4,8,5,-9,-8,-4,-10,-8,-1,4,2,6,3,-6], dtype = "uint8")#candidate|1683|(126,)|const|uint8
const_1684 = relay.const([-5,-3,2,-8,-6,8,9,-8,8,-3,7,-10,-5,-2,-9,3,4,7,-7,-1,-3,10,-8,-9,8,-1,-9,7,-5,-2,-6,10,-2,-7,2,-9,8,-9,8,5,1,-10,-8,-4,-9,-1,1,4,6,2,1,7,3,-6,-3,8,6,4,-8,-10,3,2,1,-9,7,-9,7,8,1,4,4,7,1,-5,-8,-7,-6,-8,5,6,-3,10,10,-9,-1,-2,-4,-4,-10,5,4,2,-9,7,-10,-7,7,-10,-7,-7,-1,-3,9,1,8,9,7,2,-2,1,-1,4,6,-6,-4,-1,-1,1,4,9,-7,4,2,2,-6,-7,-9,-6,6,8,-4,-4,-5,-4,8,-1,-4,8,10,9,3,4,6,7,-1,-1,-5,-7,-1,-1,4,3,-6,1,3,1,-5,-7,4,-4,-10,7,9,10,-7,-10,-1,-1,8,-3,4,-6,-1,-2,9,-10,-1,8,3,2,7,2,-7,-6,-5,-5,-7,9,-3,2,9,3,-1,1,-9,5,-7,5,-10,-6,-2,-3,1,6,5,10,-10,-3,3,6,-7,9,7,-5,-9,-1,3,9,-8,-1,-4,4,-3,-6,10,-10,10,10,-7,4,9,6,-9,-7,-1,7,-9,-9,9,9,-5,8,-2,5,-3,-3,2,4,6,8,2,-1,10,3,3,-1,-5,-8,-7,-6,1,5,-1,-7,-2,2,-2,-7,3,4,-6,-8,3,-7,8,3,5,3,6,-10,-4,-4,-7,9,-3,-8,7,1,2,2,-1,7,2,-1,9,7,-6,-8,-2,-3,-9,5,8,7,3,-10,-4,-10,7,5,5,-9,-2,3,5,10,-8,-1,-8,8,8,6,5,10,-9,9,-6,-4,5,-4,-3,4,9,10,4,9,-6,-5,2,4,-10,-7,9,-9,-9,7,-9,-5,-6,6,-3,-1,-1,-9,-2,6,3,-2,-7,9,4,-7,-6,-9,-7,2,1,8,-10,7,-7,-5,8,-5,6,10,1,-3,10,-1,1,9,-5,-6,-4,-6,-9,3,8,-2,-5,6,-2,7,3,10,-9,5,-6,8,5,-4,5,-2,7,-9,8,2,-6,-3,5,2,2,8,2,9,10,-2,3,9,-1,4,-4,1,-5,7,-8,6,10,-10,-9,-10,2,-5,-7,5,-1,-7,-7,-4,-3,-4,2,10,5,-4,9,-5,-5,8,-5,2,-3,-2,9,5,-9,-2,-3,4,-4,-2,2,4,10,-1,-6,-4,2,-1,3,3,-7,2,-1,7,3,-6,7,-2,3,-1,-4,8,-10,-7,7,5,-6,3,3,3,-9,3,-1,2,-8,-5,-7,-10,-5,2,-10,-5,5,-4,-8,-6,-7,3,-4,4,-8,-8,-5,4,7,2,-4,-4,3,-7,8,-7,2,3,-3,-10,9,5,-6,5,-8,3,-2,-1,8,7,1,10,-4,-9,-1,9,7,-5,-7,-10,-7,-5,3,-5,3,-8,-8,8,-1,-10,-6,-2,6,-5,10,-6,-10,6,-8,-4,-3,-7,-1,4,4,4,-4,2,-6,1,-4,-2,1,-6,9,1,-2,-4,7,-5,-1,-10,7,-4,-9,-10,-5,7,-8,-4,5,-10,6,-2,-1,2,5,-8,-4,-7,9,-5,-8,8,-7,5,-8,3,-7,4,1,2,8,10,10,4,-3,-4,3,-8,-2,4,-6,-3,1,2,3,-10,4,4,5,3,-9,8,-9,-4,-9,-3,7,-1,3,-10,7,-9,10,-5,1,3,-7,2,9,-8,-6,5,-7,2,10,-8,4,10,-3,6,-4,-6,2,-8,-5,1,-7,5,-1,-4,10,9,-1,7,5,10,4,2,-3,9,5,9,6,-6,10,-9,-3,-4,9,-8,5,-6,3,9,6,-4,-7,3,-7,-10,10,-7,2,-9,3,7,-5,-10,-9,-4,4,6,-3,7,-9,-8,8,3,-9,1,10,-1,-1,3,8,4,7,5,2,-3,1,-1,-9,9,7,-7,9,1,-8,9,4,-10,-7,3,9,10,7,8,-6,-1,8,1,7,7,-6,1,-2,-1,8,-8,-1,-6,10,4,1,-2,-5,-6,2,-8], dtype = "uint8")#candidate|1684|(780,)|const|uint8
call_1682 = relay.TupleGetItem(func_1038_call(relay.reshape(const_1683.astype('uint8'), [9, 7, 2]), relay.reshape(const_1684.astype('uint8'), [780,]), ), 1)
call_1685 = relay.TupleGetItem(func_1041_call(relay.reshape(const_1683.astype('uint8'), [9, 7, 2]), relay.reshape(const_1684.astype('uint8'), [780,]), ), 1)
func_1577_call = mod.get_global_var('func_1577')
func_1579_call = mutated_mod.get_global_var('func_1579')
var_1695 = relay.var("var_1695", dtype = "float64", shape = (60,))#candidate|1695|(60,)|var|float64
call_1694 = func_1577_call(relay.reshape(var_1695.astype('float64'), [10, 6, 1]))
call_1696 = func_1577_call(relay.reshape(var_1695.astype('float64'), [10, 6, 1]))
bop_1697 = relay.logical_and(const_1683.astype('bool'), call_1694.astype('bool')) # shape=(10, 6, 126)
bop_1700 = relay.logical_and(const_1683.astype('bool'), call_1696.astype('bool')) # shape=(10, 6, 126)
var_1705 = relay.var("var_1705", dtype = "uint8", shape = (13, 10, 6))#candidate|1705|(13, 10, 6)|var|uint8
bop_1706 = relay.bitwise_xor(call_1682.astype('int32'), relay.reshape(var_1705.astype('int32'), relay.shape_of(call_1682))) # shape=(13, 10, 6)
bop_1709 = relay.bitwise_xor(call_1685.astype('int32'), relay.reshape(var_1705.astype('int32'), relay.shape_of(call_1685))) # shape=(13, 10, 6)
output = relay.Tuple([call_1680,const_1684,var_1695,bop_1697,bop_1706,])
output2 = relay.Tuple([call_1681,const_1684,var_1695,bop_1700,bop_1709,])
func_1714 = relay.Function([var_1695,var_1705,], output)
mod['func_1714'] = func_1714
mod = relay.transform.InferType()(mod)
var_1715 = relay.var("var_1715", dtype = "float64", shape = (60,))#candidate|1715|(60,)|var|float64
var_1716 = relay.var("var_1716", dtype = "uint8", shape = (13, 10, 6))#candidate|1716|(13, 10, 6)|var|uint8
output = func_1714(var_1715,var_1716,)
func_1717 = relay.Function([var_1715,var_1716,], output)
mutated_mod['func_1717'] = func_1717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_1725 = relay.TupleGetItem(func_1126_call(), 0)
call_1726 = relay.TupleGetItem(func_1127_call(), 0)
output = call_1725
output2 = call_1726
func_1749 = relay.Function([], output)
mod['func_1749'] = func_1749
mod = relay.transform.InferType()(mod)
output = func_1749()
func_1750 = relay.Function([], output)
mutated_mod['func_1750'] = func_1750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1749_call = mod.get_global_var('func_1749')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_1774 = func_1749_call()
call_1775 = func_1749_call()
uop_1776 = relay.log(call_1774.astype('float32')) # shape=(7, 14, 4)
uop_1778 = relay.log(call_1775.astype('float32')) # shape=(7, 14, 4)
uop_1782 = relay.acos(call_1774.astype('float32')) # shape=(7, 14, 4)
uop_1784 = relay.acos(call_1775.astype('float32')) # shape=(7, 14, 4)
func_807_call = mod.get_global_var('func_807')
func_810_call = mutated_mod.get_global_var('func_810')
const_1791 = relay.const([-7,1,-2,2,-3,-7,10,-10,-2,1,-3,-10,7,6,-10,-1,3,-9,-4,-8,-6,7,7,-1,4,-8,8,1,-8,3,9,7,5,-6,6,8,-3,10,-4,8,4,-7,4,2,-5,1,8,-6,5,5,-10,-3,-2,10,3,4,-3,-2,8,-10,8,7,-9,-2,-6,6,-2,8,10,-9,-5,-2,3,5,9,-4,-7,6,3,10,7,-7,3,-4,-1,-7,6,-5,5,-2,-5,3,5,-8,9,10,-4,-6,10,1,5,-10,-7,-9,6,9,8,-3,-3,-3,-1,-8,-10,3,6,-3,-1,-1,-9,1,2,7,1,-4,3,7,-10,10,-1,2,-6,-6,10,-7,8,2,-9,-1,-1,5,2,-9,-6,2,1,-5,-1,-7,-8,7,4,9,10,-4,-5,-4,-2,9,1,7,7,2,3,-6,4,1,5,-1,-10,-8,7,-3,-5,9,4,-10,10,-9,-1,-5,10,-5,6,2,3,2,-3,9,5,-6,5,-4,-9,-7,-7,7,10,4,8,-3,-7,-8,-8,-8,6,6,1,-6,2,-3,10,8,-2,8,-10,8,6,8,5,-10,4,-2,-5,-7,6,6,10,7,-6,-1,-8,4,6,-1,-9,-2,7,8,-6,9,-5,-9,-8,-8,-5,-9,-9,-8,-4,-6,10,-6,5,6,-8,-5,-9,9,-3,2,-5,1,-1,-9,-6,7,-4,-2,6,-10,5,9,-8,-1,-5,-8,-3,4,-6,10,7,-9,-2,-10,10,-3,3,-9,10,3,5,6,10,4,5,1,3,5,-2,-6,-2,5,2,-8,8,-8,5,-2,3,3,2,-2,-4,2,9,-6,6,-10,-9,-1,-2,-1,2,-3,9,-5,-10,6,1,9,6,2,-9,10,-1,-7,9,-1,1,-8,-10,1,-7,1,7,-9,-7,4,-3,6,-3,-8,-2,3,-3,-4,-3,2,-6,-9,4,3,-1,7,-1,-10,9,9,9,5,-5,4,7,-8,-10,5,7,3,-7,3,-7,-2,-3,10,-5,5,-5,5,-6,7,2,-7,-2,-8,-5,6,-4,-10,1,8,-4,-5,-3,-5,5,-2,-3,-7,-3,1,4,2,6,-4,2,3,8,-9,8,9,-5,10,1,-3,10,2,3,-3,-6,8,-10,5,8,-8,-9,10,7,-4,-7,3,-4,3,-7,-8,3,10,-8,-1,1,3,-4,6,2,10,-6,9,5,7,6,6,3,3,3,8,-3,3,-3,-9,-8,6,-1,4,-5,-10,8,2,-2,-3,-9,6,-1,1,10,8,-8,-2,9,5,-8,-7,-8,10,-4,-2,3,6,1,-7,-7,6,1,-4,-5,6,-3,10,2,1,4,-2,5,2,-5,-4,-5,-10,10,9,-5,9,-8,9,-10,7,-6,-2,6,7,-2,-6,3,5,1,9,9,-2,-8,8,-3,-3,-3,-2,-8,4,9,-8,7,-6,-9,2,6,6,7,3,8,-1,-2,4,1,9,-8,-2,2,3,4,1,3,3,3,2,-5,-6,7,6,-8,7,2,2,9,5,-3,3,-6,-6,6,2,-2,-6,-8,6,-7,-3,4,5,3,9,8,3,-10,-5,-8,8,7,10,8,5,-1,-6,-6,-10,-3,-6,-3,-7,10,1,-10,10,3,-7,6,-8,-10,3,5,6,4,-9,3,-10,-7,-2,8,-6,-4,3,5,-8,-4,-3,-6,-9,1,5,-5,6,6,10,-10,6,-9,5,-8,1,5,5,2,-2,-5,6,4,1,-2,5,-7,-7,9,2,-4,-3,6,-8,3,3,9,-7,3,-2,-9,6,-7,2,-4,5,-7,5,-6,4,-5,7,-8,6,2,-8,-6,-7,-9,8,5,-1,2,8,1,7,-10,-1,-9,-4,6,2,-8,4,1,-3,5,-1,-2,-7,2,10,-10,-10,9,-10,6,4,4,-5,9,-1,4,3,2,10,6,6,2,-5,-2,3,-8,5,-6,-6,8,1,-1,7,-6,9,-8,8,-3,-10,-7,-4,-1,-8,7,2,-5,-9,-9,2,-5,7,-6,-3,7,3,-8,2,5,-6,6,-10,-3,9,-5,-7,-4,4,-1,-8,-2,-4,-9,2,6,8,8,-5,7,2,7,-4,8,-10,9,-7,10,-3,-8,4,-3,-8,-10,-1,-8,-1,-4,5,-5,1,2,4,1,-2,-4,-5,-9,-7,7,-6,-3,-10,-3,9,10,3,9,-6,7,-1,6,-8,-8,-4,5,2,8,-6,-6,3,6,10,3], dtype = "int32")#candidate|1791|(847,)|const|int32
call_1790 = func_807_call(relay.reshape(const_1791.astype('int32'), [11, 11, 7]))
call_1792 = func_807_call(relay.reshape(const_1791.astype('int32'), [11, 11, 7]))
bop_1807 = relay.minimum(uop_1782.astype('uint64'), relay.reshape(call_1774.astype('uint64'), relay.shape_of(uop_1782))) # shape=(7, 14, 4)
bop_1810 = relay.minimum(uop_1784.astype('uint64'), relay.reshape(call_1775.astype('uint64'), relay.shape_of(uop_1784))) # shape=(7, 14, 4)
uop_1819 = relay.tan(uop_1776.astype('float64')) # shape=(7, 14, 4)
uop_1821 = relay.tan(uop_1778.astype('float64')) # shape=(7, 14, 4)
output = relay.Tuple([call_1790,const_1791,bop_1807,uop_1819,])
output2 = relay.Tuple([call_1792,const_1791,bop_1810,uop_1821,])
func_1822 = relay.Function([], output)
mod['func_1822'] = func_1822
mod = relay.transform.InferType()(mod)
mutated_mod['func_1822'] = func_1822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1822_call = mutated_mod.get_global_var('func_1822')
call_1823 = func_1822_call()
output = call_1823
func_1824 = relay.Function([], output)
mutated_mod['func_1824'] = func_1824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1626_call = mod.get_global_var('func_1626')
func_1627_call = mutated_mod.get_global_var('func_1627')
call_1895 = func_1626_call()
call_1896 = func_1626_call()
func_1303_call = mod.get_global_var('func_1303')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_1902 = relay.TupleGetItem(func_1303_call(), 0)
call_1903 = relay.TupleGetItem(func_1304_call(), 0)
func_931_call = mod.get_global_var('func_931')
func_934_call = mutated_mod.get_global_var('func_934')
const_1906 = relay.const([5,-1,9,1,10,-9,3,4,6,-5,-5,-8,-4,1,-4,8,-6,10,-3,-9,6,-1,-9,5,1,2,2,-2,-7,-10,3,10,9,9,2,-4,7,-7,10,-4,3,8,8,-4,3,7,4,-7,9,4,3,-10,-3,7,-3,6,-10,3,-2,-4,3,-1,1,7,-4,-1,-8,7,2,-7,-8,-10,7,8,-10,-6,-6,-7,7,-8,6,-9,-4,8,-2,-10,-9,-9,-2,8,9,-5,5,5,8,4,-5,-2,9,3,-6,10,-1,-2,5,-7,5,3,-5,-3,-10,-1,-10,-3,3,-10,9,2,10,5,5,-2,-7,2,1,-7,2,7,-10,-1,-6,-10,1,-5,8,-6,5,3,3,3,1,-9,9,5,6,-2,6,-7,6,8,3,4,4,-9,-3,2,-4,8,-7,-3,-10,-5,-7,-3,-6,6,9,-7,-9,9,-9,-7,2,-6,-8,-3,-4,-3,3,-5,-1,8,2,2,-4,-3,-3,-7,4,5,-2,10,-9,8,-1,10,-5,1,-6,1,3,6,-6,1,6,-4,4,-6,-7,6,-9,-1,7,-4,-2,-4,10,-10,-2,-6,7,-9,-2,-6,1,-8,-8,-9,-8,7,-9,-6,2,-5,7,3,1,-8,8,3,-6,4,-9,-9,5,8,1,-2,2,-7,9,6,3,5,8,3,-1,9,7,9,-6,-5,-3,-9,-2,-7,-6,1,6,1,5,7,-10,-8,-6,8,-3,10,7,2,-6,2,-1,1,10,1,-5,-5,-7,-1,-9,-5,-1,-10,-4,2,3,-10,-9,-2,-3,6,3,3,4,3,5,6,2,-6,10,6,2,-8,9,9,6,1,7,-1,8,-4,3,8,-6,4,2,9,-8,-6,10,-10,-3,6,-5,-2,-1,3,-6,9,-7,10,-5,-5,10,1,-1,4,3,5,-7,10,-3,3,-6,-1,-7,2,2,4,-1,1,9,-5,7,8,-6,3,-3,-9,9,10,3,-6,1,8,-7,5,4,8,-9,5,-7,5,5,9,-3,7,-2,2,5,5,-7,-9,10,2,6,-7,6,-2,-5,4,-9,6,4,-5,6,-4,-10,-5,10,4,-7,-10,-2,-5,-3,-6,9,-4,-10,3,-8,-10,-10,3,-4,-10,5,-7,10,5,-8,6,3,-2,8,8,2,6,-4,-6,5,1,-5,8,-10,-1,-4,-8,8,9,-5,3,4,1,-10,6,4,5,6,7,6,4,6,6,-2,-1,9,-4,5,1,-4,-9,4,8,-7,8,2,3,6,3,6,2,-7,-10,-2,10,-6,6,4,2,10,5,1,-1,9,4,-5,-3,-3,-9,-2,10,-7,-9,-10,-2,-10,4,7,10,-7,-3,1,7,7,-8,4,-6,-4,-1,8,7,-10,-3,4,5,10,-4,-2,-4,6,9,-9,10,-1,-10,-4,-9,5,1,5,-1,-4,5,-5,-6,-10,2,9,3,-2,-9,7,3,9,-3,2,9,-8,-1,-3,5,-9,1,8,-7,6,-9,5,-6,5,-9,3,2,-2,4,9,7,6,-7,-3,-5,2,3,-5,2,-8,9,-8,-5,-4,-4,-10,-3,10,-1,6,-1,1,8,10,-5,10,4,-5,-8,7,3,2,4,-6,4,-10,-2,6,-6,-9,-9,-7,7,-9,2,-7,-3,-1,-3,-1,-10,-2,3,-2,6,-2,-2,-7,10,6,-4,-6,-5,4,-3,7,-8,-6,8,-10,3,1,-2,6,6,5,-8,7,-8,-1,7,-6,6,-8,4,-9,1,-2,-8,-4,-2,-4,-9,-4,-3,-2,3,-9,-4,3,4,-4,-2,9,-7,-6,-1,-9,-3,-1,-8,-9,3,-9,-5,-6,4,6,-6,-6,8,-2,-2,3,-4,2,-9,10,-8,-2,1,2,8,1,-4,9,-1,-3,1,-10,2,4,4,-7,5,7,-7,-1,-8,-1,9,4,-8,-5,-5,-2,7,-2,4,-3,-9,4,9,1,8,-10,9,-7,3,7,-4,-8,-7,-4,-10,-9,-7,-4,-6,6,8,-1,1,5,-9,-3,1,6,2,8,-6,10,10,4,3,-10,-7,10,-10,-6,-7], dtype = "uint8")#candidate|1906|(780,)|const|uint8
call_1905 = relay.TupleGetItem(func_931_call(relay.reshape(const_1906.astype('uint8'), [390, 2])), 2)
call_1907 = relay.TupleGetItem(func_934_call(relay.reshape(const_1906.astype('uint8'), [390, 2])), 2)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_1910 = func_1322_call()
call_1911 = func_1322_call()
const_1916 = relay.const([[[-2.993471,8.579138,6.880358,-0.645756],[-3.511899,-7.043688,5.857593,-5.125641],[2.368448,8.292788,-8.222373,-7.348158],[2.373868,-9.590202,-7.358399,2.506636],[-8.972583,-7.946687,-2.562948,5.029734],[-1.375842,-1.223649,-7.775761,5.719629],[6.294673,-2.209571,-1.127151,7.009570],[-1.835298,2.993407,7.165253,-5.017400],[-6.783090,3.555955,6.376394,5.286203],[7.966537,8.556164,-2.213545,4.910005],[1.690852,9.484487,6.273562,5.373909],[-8.898792,-5.174064,0.664968,3.261155],[-5.873926,-3.873932,-9.250181,1.515487],[7.139568,6.752721,9.039292,8.288504]],[[-0.311348,9.772212,8.757481,1.903788],[0.359630,-6.232856,-6.258379,-9.933921],[-4.297090,-7.334769,-4.656636,-3.134900],[-6.574813,-6.748330,7.213852,7.912089],[-3.696351,6.330085,8.981029,-3.281925],[-8.316864,-6.464237,-8.844774,6.571583],[7.926357,5.513852,-8.540266,-0.364797],[2.344365,-5.526400,-0.330789,-0.135863],[-5.709438,9.878232,5.991199,4.829591],[-0.027414,-8.989938,-1.550927,1.965469],[-3.478398,-9.551076,5.007553,6.550538],[1.862024,1.320432,1.136391,-6.988253],[1.683842,-8.445344,8.262280,-6.830560],[4.294669,4.755395,8.570856,3.770728]],[[2.847307,-9.805779,-9.902553,-7.522551],[0.616508,-5.615002,2.745889,2.111784],[-6.005562,7.861670,1.789545,5.196954],[4.350002,-6.554968,2.334091,-8.488736],[0.725758,7.834095,-2.445719,2.803979],[5.420103,2.450100,7.705207,4.753329],[-6.279670,7.593876,6.882594,-9.906778],[3.151818,0.738180,-5.618047,-4.384035],[-0.700956,-3.860164,5.777654,-5.190313],[5.704075,3.600991,-7.562053,-5.256064],[-0.646983,-4.250979,-9.982630,-2.920515],[-8.029682,-6.608459,0.102407,-3.793472],[3.541414,-6.745885,9.263116,6.076963],[-4.370421,7.515182,-1.771659,1.299457]],[[2.452253,-5.700649,-8.840494,-6.086340],[-6.063400,-2.461715,3.964455,1.427710],[9.549636,0.243415,-8.065630,8.756021],[6.104484,-0.594886,-0.178936,-1.724110],[6.210129,7.293674,9.173262,-4.362471],[-4.285919,9.219066,-9.471318,-2.295524],[1.347445,-0.467403,1.487696,-6.273991],[-9.708002,-7.719996,5.554925,-3.739284],[8.476896,-9.355444,5.491702,-8.800679],[6.571631,4.702183,-2.513398,0.783817],[1.561436,1.981231,9.026312,-9.163889],[-1.356303,-4.462567,1.153128,5.270301],[-8.723935,-5.659739,-0.380881,-2.881956],[-7.827587,3.664063,1.160326,-9.948874]],[[-4.505489,1.517225,-4.169804,7.280913],[-3.148262,-5.692493,9.481246,-3.509019],[2.944599,1.722555,1.692707,-1.399692],[-1.952056,-9.118943,-3.307980,-2.574559],[1.984103,0.532196,7.008468,-8.077105],[-1.510602,-1.111027,-0.515534,-9.773397],[6.106846,-6.975942,2.006174,-2.657218],[-8.506443,0.953229,-7.190284,-2.051799],[-9.307876,5.262685,-0.583986,1.529345],[-2.568614,-0.897912,0.492141,-8.118448],[0.132311,6.560697,4.702363,-7.562638],[0.843372,9.249635,8.482275,2.714419],[5.542206,-3.161851,-6.412087,-7.347403],[4.601333,-9.175562,5.516631,6.763970]],[[6.503514,2.408170,-8.211875,-0.144993],[-6.645827,9.761603,0.681832,0.313427],[4.214330,5.427029,2.289518,-4.057688],[-8.217209,3.105035,-6.240050,-8.657119],[-6.856343,-8.738792,5.631263,-3.254579],[-9.153922,-0.283085,-9.933790,-4.832274],[3.422833,9.208135,-9.352590,3.328267],[-9.356407,-7.685988,3.896396,-0.241875],[1.019494,-1.650957,-1.903808,-7.722060],[2.451369,-0.512465,-1.755899,4.829909],[-1.364674,-3.032494,3.545628,-1.361106],[9.447794,-4.472354,4.139648,-3.213431],[1.906599,-3.850188,7.366371,0.748663],[6.360538,-3.343150,-5.142963,3.078964]],[[-0.865071,9.319216,9.643717,-0.121805],[9.068174,0.053946,2.095069,6.950187],[-2.546682,-4.051112,-9.713619,-0.801969],[-1.385972,0.921012,9.351476,5.749085],[-6.301057,6.377556,-9.910923,-8.852016],[-7.299519,6.433320,6.902251,-8.964054],[-3.560005,5.229923,-2.693864,-8.987126],[-1.722376,-7.592305,-5.147850,-1.172071],[-6.294945,-0.506831,1.315060,-9.353750],[-0.394877,2.061712,-7.320140,2.982320],[0.558031,2.660296,3.936259,-8.909404],[8.833021,5.875868,-5.183029,8.810144],[4.233164,-7.745700,-3.021380,-2.871338],[-3.484665,7.819882,3.256937,0.256934]]], dtype = "float64")#candidate|1916|(7, 14, 4)|const|float64
bop_1917 = relay.multiply(call_1910.astype('uint16'), relay.reshape(const_1916.astype('uint16'), relay.shape_of(call_1910))) # shape=(7, 14, 4)
bop_1920 = relay.multiply(call_1911.astype('uint16'), relay.reshape(const_1916.astype('uint16'), relay.shape_of(call_1911))) # shape=(7, 14, 4)
output = relay.Tuple([call_1895,call_1902,call_1905,const_1906,bop_1917,])
output2 = relay.Tuple([call_1896,call_1903,call_1907,const_1906,bop_1920,])
func_1931 = relay.Function([], output)
mod['func_1931'] = func_1931
mod = relay.transform.InferType()(mod)
mutated_mod['func_1931'] = func_1931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mutated_mod.get_global_var('func_1931')
call_1932 = func_1931_call()
output = call_1932
func_1933 = relay.Function([], output)
mutated_mod['func_1933'] = func_1933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1626_call = mod.get_global_var('func_1626')
func_1627_call = mutated_mod.get_global_var('func_1627')
call_1992 = func_1626_call()
call_1993 = func_1626_call()
func_1749_call = mod.get_global_var('func_1749')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_2041 = func_1749_call()
call_2042 = func_1749_call()
uop_2044 = relay.rsqrt(call_2041.astype('float64')) # shape=(7, 14, 4)
uop_2046 = relay.rsqrt(call_2042.astype('float64')) # shape=(7, 14, 4)
output = relay.Tuple([call_1992,uop_2044,])
output2 = relay.Tuple([call_1993,uop_2046,])
func_2049 = relay.Function([], output)
mod['func_2049'] = func_2049
mod = relay.transform.InferType()(mod)
mutated_mod['func_2049'] = func_2049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2049_call = mutated_mod.get_global_var('func_2049')
call_2050 = func_2049_call()
output = call_2050
func_2051 = relay.Function([], output)
mutated_mod['func_2051'] = func_2051
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2103 = relay.var("var_2103", dtype = "float32", shape = ())#candidate|2103|()|var|float32
var_2104 = relay.var("var_2104", dtype = "float32", shape = (1, 9, 12))#candidate|2104|(1, 9, 12)|var|float32
bop_2105 = relay.equal(var_2103.astype('bool'), var_2104.astype('bool')) # shape=(1, 9, 12)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_2108 = func_1322_call()
call_2109 = func_1322_call()
uop_2134 = relay.log(var_2104.astype('float64')) # shape=(1, 9, 12)
bop_2139 = relay.floor_divide(uop_2134.astype('float64'), relay.reshape(var_2104.astype('float64'), relay.shape_of(uop_2134))) # shape=(1, 9, 12)
output = relay.Tuple([bop_2105,call_2108,bop_2139,])
output2 = relay.Tuple([bop_2105,call_2109,bop_2139,])
func_2168 = relay.Function([var_2103,var_2104,], output)
mod['func_2168'] = func_2168
mod = relay.transform.InferType()(mod)
mutated_mod['func_2168'] = func_2168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mutated_mod.get_global_var('func_2168')
var_2170 = relay.var("var_2170", dtype = "float32", shape = ())#candidate|2170|()|var|float32
var_2171 = relay.var("var_2171", dtype = "float32", shape = (1, 9, 12))#candidate|2171|(1, 9, 12)|var|float32
call_2169 = func_2168_call(var_2170,var_2171,)
output = call_2169
func_2172 = relay.Function([var_2170,var_2171,], output)
mutated_mod['func_2172'] = func_2172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_2179 = relay.TupleGetItem(func_856_call(), 0)
call_2180 = relay.TupleGetItem(func_858_call(), 0)
func_1577_call = mod.get_global_var('func_1577')
func_1579_call = mutated_mod.get_global_var('func_1579')
const_2187 = relay.const([0.190576,5.677888,0.724422,5.418381,6.382905,-8.647545,7.508998,0.299216,4.062637,-5.390848,-8.977467,8.994366,-0.404504,-7.782869,7.630985,7.575065,6.054921,8.974093,7.569498,2.341738,-5.238186,1.492284,-0.324032,0.372428,-9.358353,-8.490932,1.965423,-6.440219,1.646686,6.168225,-0.221542,5.563656,7.298977,-0.442139,-4.517762,-7.342162,-7.773180,-8.956044,-0.726149,-3.338299,-5.409613,-1.999656,-8.056032,2.938861,0.364983,-5.182692,8.548221,3.680151,7.661163,6.278836,-0.133990,-3.905757,-6.947791,6.551404,-6.654163,9.062356,-8.571120,-9.539522,-2.178144,-8.580749], dtype = "float64")#candidate|2187|(60,)|const|float64
call_2186 = func_1577_call(relay.reshape(const_2187.astype('float64'), [10, 6, 1]))
call_2188 = func_1577_call(relay.reshape(const_2187.astype('float64'), [10, 6, 1]))
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_2191 = func_1322_call()
call_2192 = func_1322_call()
func_1087_call = mod.get_global_var('func_1087')
func_1090_call = mutated_mod.get_global_var('func_1090')
var_2207 = relay.var("var_2207", dtype = "int32", shape = (847,))#candidate|2207|(847,)|var|int32
call_2206 = relay.TupleGetItem(func_1087_call(relay.reshape(var_2207.astype('int32'), [847,])), 1)
call_2208 = relay.TupleGetItem(func_1090_call(relay.reshape(var_2207.astype('int32'), [847,])), 1)
uop_2216 = relay.log(call_2186.astype('float32')) # shape=(10, 6, 1)
uop_2218 = relay.log(call_2188.astype('float32')) # shape=(10, 6, 1)
func_1222_call = mod.get_global_var('func_1222')
func_1225_call = mutated_mod.get_global_var('func_1225')
call_2238 = relay.TupleGetItem(func_1222_call(relay.reshape(var_2207.astype('int32'), [847,])), 1)
call_2239 = relay.TupleGetItem(func_1225_call(relay.reshape(var_2207.astype('int32'), [847,])), 1)
output = relay.Tuple([call_2179,const_2187,call_2191,call_2206,var_2207,uop_2216,call_2238,])
output2 = relay.Tuple([call_2180,const_2187,call_2192,call_2208,var_2207,uop_2218,call_2239,])
func_2247 = relay.Function([var_2207,], output)
mod['func_2247'] = func_2247
mod = relay.transform.InferType()(mod)
mutated_mod['func_2247'] = func_2247
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2248 = relay.var("var_2248", dtype = "int32", shape = (847,))#candidate|2248|(847,)|var|int32
func_2247_call = mutated_mod.get_global_var('func_2247')
call_2249 = func_2247_call(var_2248)
output = call_2249
func_2250 = relay.Function([var_2248], output)
mutated_mod['func_2250'] = func_2250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1673_call = mod.get_global_var('func_1673')
func_1674_call = mutated_mod.get_global_var('func_1674')
call_2260 = func_1673_call()
call_2261 = func_1673_call()
output = call_2260
output2 = call_2261
func_2263 = relay.Function([], output)
mod['func_2263'] = func_2263
mod = relay.transform.InferType()(mod)
output = func_2263()
func_2264 = relay.Function([], output)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2291 = relay.var("var_2291", dtype = "float64", shape = (11, 12, 5))#candidate|2291|(11, 12, 5)|var|float64
uop_2292 = relay.sin(var_2291.astype('float64')) # shape=(11, 12, 5)
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_2294 = relay.TupleGetItem(func_1822_call(), 3)
call_2295 = relay.TupleGetItem(func_1824_call(), 3)
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_2300 = relay.TupleGetItem(func_1822_call(), 3)
call_2301 = relay.TupleGetItem(func_1824_call(), 3)
func_1749_call = mod.get_global_var('func_1749')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_2316 = func_1749_call()
call_2317 = func_1749_call()
output = relay.Tuple([uop_2292,call_2294,call_2300,call_2316,])
output2 = relay.Tuple([uop_2292,call_2295,call_2301,call_2317,])
func_2321 = relay.Function([var_2291,], output)
mod['func_2321'] = func_2321
mod = relay.transform.InferType()(mod)
mutated_mod['func_2321'] = func_2321
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2322 = relay.var("var_2322", dtype = "float64", shape = (11, 12, 5))#candidate|2322|(11, 12, 5)|var|float64
func_2321_call = mutated_mod.get_global_var('func_2321')
call_2323 = func_2321_call(var_2322)
output = call_2323
func_2324 = relay.Function([var_2322], output)
mutated_mod['func_2324'] = func_2324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2049_call = mod.get_global_var('func_2049')
func_2051_call = mutated_mod.get_global_var('func_2051')
call_2367 = relay.TupleGetItem(func_2049_call(), 0)
call_2368 = relay.TupleGetItem(func_2051_call(), 0)
func_647_call = mod.get_global_var('func_647')
func_649_call = mutated_mod.get_global_var('func_649')
const_2372 = relay.const([[-8],[-10],[10],[-4],[8],[-10],[7],[10],[5],[-9],[-8],[9],[6],[9],[-10],[8],[4],[2],[7],[-8],[7],[-10],[2],[-4],[-9],[5],[-5],[3],[4],[9],[-10],[1],[5],[9],[9],[-9],[-3],[-1],[-2],[-4],[-9],[6],[-5],[7],[2],[-3],[-3],[6],[8],[-1],[1],[3],[10],[1],[-10],[-1],[-7],[-7],[10],[2],[-10],[-2],[-9],[-10],[-4],[-6],[-1],[-10],[-5],[-3],[9],[-8],[-4],[7],[-8],[4],[3],[-10],[6],[1],[-3],[6],[-8],[-6],[-1],[-1],[-4],[-5],[3],[2],[10],[-9],[6],[7],[-9],[2],[7],[-7],[8],[1],[-4],[-8],[-1],[-9],[-6],[6],[-9],[-8],[4],[6],[6],[-7],[-8],[2],[-8],[5],[-7],[-10],[-5],[-3],[-10],[-6],[-3],[5],[-2],[1],[1],[-2],[2],[6],[7],[2],[4],[2],[-1],[-2],[-7],[-1],[5],[-8],[-10],[-6],[8],[-1],[2],[-10],[1],[-4],[-4],[-4],[-5],[-5],[7],[1],[-5],[-10],[9],[-6],[-3],[-7],[8],[-7],[9],[-4],[10],[-7],[4],[-5],[9],[2],[6],[-9],[-7],[-2],[-5],[7],[-4],[2],[6],[6],[4],[10],[7],[-1],[-1],[10],[-7],[4],[7],[-6],[5],[-6],[10],[4],[-4],[1],[-6],[-7],[6],[9],[3],[7],[-10],[3],[7],[10],[5],[-10],[-7],[-10],[-7],[-10],[1],[5],[-7],[7],[4],[9],[-6],[-3],[-4],[-4],[-10],[3],[-9],[10],[-3],[8],[-8],[-3],[5],[-5],[5],[5],[6],[4],[-1],[-6],[-3],[10],[-1],[9],[-9],[-10],[-9],[-3],[7],[5],[10],[3],[8],[-6],[6],[-1],[1],[2],[-2],[-6],[7],[9],[10],[-10],[8],[9],[5],[-3],[-1],[-3],[-1],[7],[-6],[5],[-1],[8],[-8],[-6],[8],[5],[3],[-5],[-8],[-3],[-9],[6],[-3],[-3],[-2],[-6],[9],[3],[-2],[6],[-6],[8],[-7],[-10],[-3],[-3],[-1],[2],[2],[10],[4],[-8],[-1],[-10],[1],[5],[-1],[7],[-7],[-4],[-9],[-5],[-6],[2],[-4],[3],[-10],[3],[-4],[-8],[-3],[4],[-7],[-1],[-7],[-7],[1],[-7],[-10],[-6],[-3],[4],[-2],[7],[-2],[-2],[-10],[-8],[-7],[-3],[3],[1],[3],[1],[-4],[8],[10],[3],[9],[-9],[-6],[5],[-9],[-5],[9],[1],[10],[-5],[9],[-6],[7],[-2],[-6],[-6],[-6],[-5],[7],[-8],[-2],[-3],[1],[-4],[-7],[3],[7],[8],[-3],[-10],[5],[3],[2],[-4],[9],[-5],[7],[3],[-3],[8],[-10],[-5],[10],[10],[4],[-2],[7],[-10],[5],[-7],[-8],[-5],[-2],[2],[9],[-5],[-2],[-5],[-2],[6],[6],[-6],[-3],[-9],[-4],[3],[9],[-6],[8],[6],[1],[4],[10],[8],[6],[-1],[-3],[-3],[-7],[5],[1],[3],[5],[10],[-9],[-1],[-8],[6],[6],[-3],[9],[3],[2],[8],[-10],[-9],[10],[10],[-1],[-1],[9],[-5],[-8],[-6],[-6],[-9],[2],[4],[-9],[1],[5],[10],[-2],[-3],[3],[5],[7],[-6],[2],[1],[10],[10],[-1],[-5],[-9],[2],[8],[1],[4],[-5],[7],[6],[2],[9],[5],[-10],[10],[-6],[8],[-3],[-10],[1],[9],[-8],[-6],[-8],[4],[7],[10],[-8],[5],[-10],[9],[8],[-9],[-4],[-8],[-9],[-9],[-9],[-1],[-9],[5],[-9],[-3],[-9],[-6],[-3],[-7],[2],[-6],[7],[1],[2],[-4],[-6],[2],[-9],[3],[-1],[6],[5],[7],[7],[-1],[-1],[5],[-10],[3],[-10],[-4],[1],[-4],[-10],[-10],[-3],[1],[8],[-8],[-3],[6],[-7],[-2],[-9],[2],[4],[-6],[10],[7],[8],[3],[4],[1],[-1],[9],[-1],[7],[-7],[-8],[6],[6],[4],[6],[3],[-7],[1],[-4],[3],[6],[-6],[9],[-3],[-7],[9],[-9],[-3],[-6],[-8],[-2],[6],[-3],[9],[-1],[-5],[-8],[6],[-2],[6],[-9],[5],[2],[4],[9],[-10],[6],[2],[4],[-9],[6],[2],[8],[-3],[-6],[10],[-6],[7],[4],[-5],[5],[6],[1],[3],[9],[-10],[7],[-9],[1],[5],[-1],[-7],[9],[2],[-5],[-6],[2],[4],[-10],[-1],[-8],[-2],[-5],[1],[-10],[-7],[1],[-7],[-8],[-4],[8],[5],[-4],[5],[3],[-2],[7],[7],[-4],[-9],[-5],[7],[-10],[6],[5],[-3],[2],[5],[5],[9],[-6],[-1],[5],[-6],[-8],[-7],[-3],[9],[-9],[3],[5],[-9],[4],[-2],[-1],[-8],[-3],[9],[-1],[-9],[2],[-2],[-10],[-8],[5],[5],[9],[-6],[7],[3],[8],[7],[2],[-1],[3],[-4],[8],[9],[8],[-7],[1],[3],[-7],[3],[7],[-1],[7],[8],[6],[-4],[1],[-3],[3],[-7],[9],[4],[-5],[10],[-5],[5],[8],[9],[-6],[7],[-6],[10],[-9],[4],[-6],[5],[-4],[-7],[-7],[2],[-1],[6],[-5],[-5],[9],[2],[2],[-3],[-6],[5],[10],[7],[-10],[-5],[-3],[-10],[4],[-4],[-10],[1],[-10],[7],[6],[5],[8],[3],[-1],[-2],[-9],[9],[-3],[-6],[7],[-7],[10],[10],[-10],[4]], dtype = "uint8")#candidate|2372|(780, 1)|const|uint8
call_2371 = func_647_call(relay.reshape(const_2372.astype('uint8'), [13, 10, 6]))
call_2373 = func_647_call(relay.reshape(const_2372.astype('uint8'), [13, 10, 6]))
output = relay.Tuple([call_2367,call_2371,const_2372,])
output2 = relay.Tuple([call_2368,call_2373,const_2372,])
func_2379 = relay.Function([], output)
mod['func_2379'] = func_2379
mod = relay.transform.InferType()(mod)
mutated_mod['func_2379'] = func_2379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2379_call = mutated_mod.get_global_var('func_2379')
call_2380 = func_2379_call()
output = call_2380
func_2381 = relay.Function([], output)
mutated_mod['func_2381'] = func_2381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2379_call = mod.get_global_var('func_2379')
func_2381_call = mutated_mod.get_global_var('func_2381')
call_2442 = relay.TupleGetItem(func_2379_call(), 2)
call_2443 = relay.TupleGetItem(func_2381_call(), 2)
output = relay.Tuple([call_2442,])
output2 = relay.Tuple([call_2443,])
func_2444 = relay.Function([], output)
mod['func_2444'] = func_2444
mod = relay.transform.InferType()(mod)
output = func_2444()
func_2445 = relay.Function([], output)
mutated_mod['func_2445'] = func_2445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2379_call = mod.get_global_var('func_2379')
func_2381_call = mutated_mod.get_global_var('func_2381')
call_2460 = relay.TupleGetItem(func_2379_call(), 0)
call_2461 = relay.TupleGetItem(func_2381_call(), 0)
output = relay.Tuple([call_2460,])
output2 = relay.Tuple([call_2461,])
func_2468 = relay.Function([], output)
mod['func_2468'] = func_2468
mod = relay.transform.InferType()(mod)
output = func_2468()
func_2469 = relay.Function([], output)
mutated_mod['func_2469'] = func_2469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2263_call = mod.get_global_var('func_2263')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_2492 = func_2263_call()
call_2493 = func_2263_call()
output = call_2492
output2 = call_2493
func_2511 = relay.Function([], output)
mod['func_2511'] = func_2511
mod = relay.transform.InferType()(mod)
mutated_mod['func_2511'] = func_2511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2511_call = mutated_mod.get_global_var('func_2511')
call_2512 = func_2511_call()
output = call_2512
func_2513 = relay.Function([], output)
mutated_mod['func_2513'] = func_2513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2049_call = mod.get_global_var('func_2049')
func_2051_call = mutated_mod.get_global_var('func_2051')
call_2548 = relay.TupleGetItem(func_2049_call(), 0)
call_2549 = relay.TupleGetItem(func_2051_call(), 0)
func_2468_call = mod.get_global_var('func_2468')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_2553 = relay.TupleGetItem(func_2468_call(), 0)
call_2554 = relay.TupleGetItem(func_2469_call(), 0)
func_1303_call = mod.get_global_var('func_1303')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_2562 = relay.TupleGetItem(func_1303_call(), 0)
call_2563 = relay.TupleGetItem(func_1304_call(), 0)
uop_2569 = relay.sin(call_2562.astype('float32')) # shape=(7, 14, 4)
uop_2571 = relay.sin(call_2563.astype('float32')) # shape=(7, 14, 4)
func_1749_call = mod.get_global_var('func_1749')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_2590 = func_1749_call()
call_2591 = func_1749_call()
output = relay.Tuple([call_2548,call_2553,uop_2569,call_2590,])
output2 = relay.Tuple([call_2549,call_2554,uop_2571,call_2591,])
func_2607 = relay.Function([], output)
mod['func_2607'] = func_2607
mod = relay.transform.InferType()(mod)
mutated_mod['func_2607'] = func_2607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2607_call = mutated_mod.get_global_var('func_2607')
call_2608 = func_2607_call()
output = call_2608
func_2609 = relay.Function([], output)
mutated_mod['func_2609'] = func_2609
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2637 = relay.var("var_2637", dtype = "int8", shape = (9, 15, 13))#candidate|2637|(9, 15, 13)|var|int8
var_2638 = relay.var("var_2638", dtype = "int8", shape = (9, 15, 13))#candidate|2638|(9, 15, 13)|var|int8
bop_2639 = relay.less(var_2637.astype('bool'), relay.reshape(var_2638.astype('bool'), relay.shape_of(var_2637))) # shape=(9, 15, 13)
const_2658 = relay.const([[[True,False,False,False,False,False,False,True,True,True,False,True,False],[True,True,True,False,True,True,True,True,True,True,True,False,True],[True,True,True,False,True,False,False,True,False,True,True,False,False],[True,True,False,False,False,False,True,True,False,True,False,False,False],[True,True,True,True,False,False,False,True,False,True,True,True,True],[True,False,False,False,False,True,True,True,True,True,True,True,False],[True,False,True,True,False,False,True,False,False,True,False,False,True],[True,False,False,False,True,False,False,True,False,False,True,True,True],[False,True,False,True,True,False,True,False,True,False,True,False,False],[True,False,False,True,True,True,True,True,True,False,True,True,False],[True,False,True,True,True,True,False,False,True,True,False,False,False],[True,False,True,False,False,False,False,True,True,True,False,True,False],[False,True,False,True,True,True,True,False,False,True,False,False,True],[True,False,True,True,False,False,False,True,False,False,True,False,True],[False,True,False,True,False,False,True,False,True,False,True,True,True]],[[False,False,True,False,True,False,False,False,True,False,False,True,True],[True,False,False,True,True,True,True,True,False,True,True,True,True],[True,False,False,False,True,False,False,False,True,True,False,True,True],[True,False,True,True,True,False,True,False,False,False,True,True,False],[True,False,True,True,True,False,True,True,False,False,False,False,False],[True,True,False,False,False,True,False,False,False,False,False,True,False],[False,False,True,True,False,False,True,True,True,False,False,False,False],[False,False,False,True,False,True,False,False,True,True,False,False,True],[False,False,True,False,False,False,False,True,True,False,True,True,True],[True,True,True,True,True,False,False,True,True,False,False,True,True],[False,False,True,False,True,True,False,True,True,False,True,True,True],[False,True,False,True,True,True,True,False,True,False,False,True,False],[True,True,False,True,False,False,True,True,False,True,True,False,False],[False,False,True,False,True,True,True,False,True,False,True,False,True],[False,False,True,True,False,True,True,True,False,True,True,True,True]],[[False,False,False,False,False,False,True,True,False,False,True,False,False],[False,False,False,False,True,False,False,True,False,True,False,True,False],[False,False,True,True,True,True,False,True,False,False,False,True,False],[False,True,True,False,False,True,True,False,True,False,False,True,True],[False,False,True,True,False,True,False,False,True,True,True,True,True],[True,True,True,False,True,True,False,False,False,False,True,True,False],[False,True,False,False,True,True,False,False,False,True,False,False,True],[True,False,False,False,True,False,True,False,False,True,True,False,True],[True,False,True,False,False,True,False,True,True,True,False,False,True],[False,True,True,True,False,False,True,False,False,False,False,False,False],[True,True,True,True,False,True,False,True,True,False,True,True,True],[False,False,True,False,False,False,True,True,True,True,False,False,False],[False,False,False,False,False,True,True,True,True,False,False,True,True],[False,True,False,True,True,True,False,False,True,False,False,True,True],[True,False,True,True,False,False,True,True,False,True,False,False,True]],[[True,False,True,False,True,True,False,False,True,True,True,True,True],[False,True,False,True,False,True,False,False,True,False,False,False,True],[False,False,False,False,True,True,False,False,False,False,False,False,False],[True,True,True,False,False,True,True,False,True,True,False,True,True],[True,True,True,True,True,False,True,True,False,False,False,True,True],[False,True,True,False,True,False,True,False,False,False,True,True,False],[False,False,False,True,False,True,True,True,True,False,True,False,True],[False,True,True,True,False,False,False,True,False,True,True,False,True],[True,False,False,False,False,True,False,True,False,False,False,True,False],[True,True,True,False,False,True,True,False,False,True,False,False,False],[False,True,True,False,False,False,False,True,False,True,False,False,False],[False,True,False,False,True,False,True,False,False,False,False,True,False],[False,False,False,True,False,False,False,True,True,True,True,True,False],[True,False,False,True,False,False,False,True,False,True,True,False,False],[True,False,False,False,False,False,False,False,True,False,False,False,True]],[[True,True,False,True,True,True,True,True,False,False,True,True,True],[False,False,False,False,False,True,False,False,True,False,True,True,False],[False,True,False,False,False,False,True,False,True,False,True,False,True],[True,False,True,False,True,True,True,True,True,True,False,True,False],[True,True,True,False,True,True,True,True,False,True,True,True,True],[False,False,False,True,True,False,True,False,False,True,True,True,False],[False,True,True,True,True,False,False,False,True,True,True,False,True],[True,False,False,True,True,True,True,False,False,False,False,True,True],[False,False,False,False,True,True,True,False,False,False,False,True,False],[True,False,True,False,True,True,False,False,False,True,True,True,True],[True,True,True,False,False,False,True,True,False,False,False,True,False],[False,True,False,True,True,False,False,False,False,True,True,False,True],[True,True,False,False,True,True,False,False,False,False,False,True,True],[False,True,True,True,True,False,False,True,True,True,True,True,False],[True,True,True,True,False,True,True,True,True,False,False,True,False]],[[False,False,True,True,True,True,False,True,True,True,True,True,True],[False,True,False,False,True,False,True,False,True,True,True,False,False],[True,False,True,False,True,True,False,False,True,False,True,True,True],[False,True,False,False,False,False,True,False,False,False,False,True,False],[False,True,False,False,True,True,True,False,True,False,False,False,False],[True,False,True,False,True,False,True,True,False,True,True,True,False],[False,True,False,True,True,False,False,True,True,False,False,False,False],[False,False,False,False,False,True,False,True,False,True,True,True,False],[True,True,True,False,True,True,True,True,True,True,False,True,False],[True,True,True,True,False,True,True,False,True,True,False,True,False],[False,False,False,True,False,True,False,True,False,True,True,True,True],[False,False,True,True,True,False,True,False,True,True,True,False,True],[False,True,True,True,True,True,True,True,True,True,True,True,False],[True,True,True,False,False,True,True,True,True,False,True,False,False],[False,True,True,False,False,True,True,False,False,False,True,True,False]],[[False,False,True,False,False,False,True,False,False,True,True,True,False],[False,True,True,False,True,True,True,False,True,False,True,False,False],[True,False,True,False,False,False,False,True,False,True,True,True,True],[False,False,False,True,False,True,True,True,True,False,False,True,True],[True,True,False,True,True,False,True,False,False,False,False,True,True],[False,False,True,True,True,True,True,True,False,True,False,True,False],[False,False,False,True,True,True,False,True,False,True,True,False,True],[False,False,False,True,True,False,True,False,False,False,True,True,True],[False,True,False,True,True,False,True,False,True,False,True,True,False],[False,False,True,False,True,True,False,True,False,True,False,True,False],[False,True,True,True,True,True,False,True,True,False,True,False,False],[False,True,True,True,True,True,True,False,True,False,False,True,False],[False,True,False,False,True,False,True,False,True,False,False,False,True],[True,False,False,True,False,False,False,True,True,True,True,False,False],[False,True,False,False,True,False,True,True,False,False,True,False,False]],[[False,False,False,False,False,True,False,False,True,False,True,True,False],[False,True,True,True,True,True,False,True,True,True,True,False,False],[False,False,True,False,True,True,False,True,False,False,True,False,True],[False,True,False,True,True,False,False,False,True,True,True,True,False],[True,False,False,True,False,False,False,True,False,True,True,False,False],[True,True,True,True,False,True,False,False,True,True,False,True,True],[False,True,True,True,True,False,False,True,True,False,True,True,False],[True,False,True,False,True,False,True,False,True,True,False,False,True],[True,True,True,False,True,True,True,False,True,True,False,True,False],[True,True,False,True,True,True,True,False,True,False,False,False,True],[False,True,True,False,False,False,True,False,False,False,True,False,False],[False,True,False,True,True,False,True,True,True,False,True,False,True],[False,True,True,True,False,True,False,True,True,True,True,True,True],[True,True,False,True,False,True,False,False,False,False,False,True,True],[True,False,False,False,True,True,True,False,False,True,False,False,False]],[[True,True,True,False,False,False,False,True,False,False,False,False,False],[False,False,True,False,False,False,False,False,False,True,True,True,True],[True,False,True,False,False,True,True,True,True,False,False,True,True],[False,True,True,False,False,True,True,True,True,True,True,True,True],[False,False,True,True,False,False,False,True,False,False,False,False,False],[False,False,False,True,True,False,True,False,False,True,True,True,False],[True,False,True,False,False,True,True,True,True,True,True,True,False],[False,True,True,False,True,True,False,True,False,True,True,True,True],[False,False,False,True,False,True,False,False,False,False,True,True,True],[False,False,False,True,False,False,True,True,False,False,False,False,False],[True,True,True,False,False,True,True,True,True,True,False,True,True],[False,True,True,True,False,True,True,False,True,False,True,False,True],[True,False,False,False,False,True,True,False,True,False,True,False,True],[False,False,True,True,True,False,False,False,True,False,False,True,True],[True,True,False,True,False,True,True,False,True,False,True,True,False]]], dtype = "bool")#candidate|2658|(9, 15, 13)|const|bool
bop_2659 = relay.bitwise_or(bop_2639.astype('int32'), relay.reshape(const_2658.astype('int32'), relay.shape_of(bop_2639))) # shape=(9, 15, 13)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_2689 = func_1322_call()
call_2690 = func_1322_call()
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_2701 = relay.TupleGetItem(func_988_call(), 0)
call_2702 = relay.TupleGetItem(func_990_call(), 0)
output = relay.Tuple([bop_2659,call_2689,call_2701,])
output2 = relay.Tuple([bop_2659,call_2690,call_2702,])
func_2707 = relay.Function([var_2637,var_2638,], output)
mod['func_2707'] = func_2707
mod = relay.transform.InferType()(mod)
mutated_mod['func_2707'] = func_2707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2707_call = mutated_mod.get_global_var('func_2707')
var_2709 = relay.var("var_2709", dtype = "int8", shape = (9, 15, 13))#candidate|2709|(9, 15, 13)|var|int8
var_2710 = relay.var("var_2710", dtype = "int8", shape = (9, 15, 13))#candidate|2710|(9, 15, 13)|var|int8
call_2708 = func_2707_call(var_2709,var_2710,)
output = call_2708
func_2711 = relay.Function([var_2709,var_2710,], output)
mutated_mod['func_2711'] = func_2711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1673_call = mod.get_global_var('func_1673')
func_1674_call = mutated_mod.get_global_var('func_1674')
call_2741 = func_1673_call()
call_2742 = func_1673_call()
const_2762 = relay.const([[[5.165619,-3.119214,5.082234,7.697762],[-1.351140,-2.270688,0.529691,1.235495],[-9.128217,0.854223,4.027444,0.206826],[-5.560658,6.603794,-1.798249,-6.835492],[-5.616758,3.117417,-1.835968,9.763496],[-6.594671,9.015821,6.761411,2.154885],[3.683469,-3.177850,-8.679983,-1.058963],[-4.019936,-3.351382,-6.671749,-3.384956],[1.089343,6.961754,9.101737,-9.383390],[-9.841332,5.986228,-5.791795,3.662385],[7.952482,-3.163708,1.084791,7.064703],[7.225811,1.898253,-8.261283,-2.833855],[3.138772,0.773874,-2.310819,1.721077],[-7.020925,-8.953489,9.681020,-2.795585]],[[-4.857755,-7.598654,3.588342,1.653094],[8.500391,-2.884539,9.216322,7.791795],[-3.889217,3.078117,-2.141590,-2.001587],[8.519863,3.901149,-9.273500,3.098655],[0.082796,5.854523,5.139632,7.188441],[3.921531,2.392131,-3.355253,3.904620],[5.155845,6.766531,3.820842,-7.325801],[2.412052,-7.832638,3.191473,-5.204167],[3.470790,6.582293,-3.987104,-3.982080],[0.397657,-3.140269,-8.668967,-3.879073],[-8.566463,-9.242208,9.397628,-0.229214],[-3.638280,6.163089,9.165144,-2.251036],[5.687399,2.355257,-9.077294,6.262291],[6.639566,7.855627,9.102516,-5.258308]],[[-0.489336,-5.384047,2.751362,-6.571757],[0.893034,-8.595758,1.538032,4.816344],[-3.683928,-1.175288,-3.516162,-0.335767],[-2.400439,-2.759501,-6.486822,7.282439],[2.824106,-6.604323,3.911331,-2.160668],[-9.736758,5.742909,-1.558829,-3.628743],[5.102090,2.242412,-8.115199,-5.362860],[-2.147921,2.976601,9.945157,8.304870],[-5.937859,3.453320,-8.540224,-6.301181],[-8.398733,-2.517170,-2.565282,-9.369431],[1.934637,-8.735942,8.743925,-9.854352],[6.450147,-1.153019,8.648483,7.044629],[-8.147741,5.233641,-6.495613,3.620058],[5.485429,8.369970,8.108146,9.678657]],[[-1.733186,-7.838856,-4.525323,5.385983],[-7.817945,-6.770387,5.818472,3.320133],[2.011222,-5.758268,-2.322579,-6.650398],[5.401110,-8.700357,8.959212,5.368699],[3.079428,-1.535928,3.660841,8.063480],[4.385563,9.342036,2.425020,-6.567479],[8.492351,-6.707279,4.411781,2.360602],[4.477960,7.729466,9.333543,-3.221685],[-4.690979,0.033934,-4.261416,-4.477532],[-9.287062,-3.483223,-1.770985,-1.129488],[6.347472,-5.777239,-5.331068,4.521773],[5.227860,-5.745162,6.089886,1.208333],[8.759267,1.709292,9.500682,-2.737697],[6.736863,0.966673,2.289204,2.106412]],[[-0.297070,0.159768,4.375586,-5.437996],[0.693013,-5.500724,8.471988,3.826339],[-6.536068,-2.780698,-4.019035,4.460158],[6.372108,6.575503,5.552253,3.222315],[-7.465590,-6.877276,4.300875,-9.047651],[4.302795,-8.077886,-8.058319,-3.944743],[-4.383365,-3.426944,8.958784,3.902079],[-7.559903,8.294520,2.949685,-1.747914],[-7.986557,-9.667157,8.925859,-7.729000],[6.002034,-9.998438,-3.154617,-2.166343],[4.193986,6.873869,-3.461894,-9.454767],[-9.321262,-5.246126,-4.551326,4.412086],[9.529857,1.120124,8.679838,-6.981663],[-6.211100,-5.589154,9.843233,2.842886]],[[-2.471727,4.763928,8.816802,3.685489],[7.708223,-3.381215,-2.309540,-0.399624],[5.231639,7.441367,-5.430100,1.139319],[-1.472499,8.371847,-8.015332,-9.090487],[-3.834799,4.940457,6.550425,7.607845],[7.491335,3.879023,2.211986,9.617475],[4.986592,6.729234,-6.115321,-6.878389],[7.374076,-3.859281,-7.220430,-1.275913],[-1.572379,6.946376,-6.470176,7.542101],[-3.851747,-1.228730,-4.963439,-6.683174],[-8.201559,4.154686,-8.322001,8.280904],[-8.359876,7.720215,-3.522595,6.697909],[8.433417,2.284816,8.200391,1.372469],[9.482155,8.957839,-7.968979,4.306019]],[[-9.854098,1.628071,-7.898010,-4.427749],[2.035290,7.433983,2.821329,-4.722461],[6.722024,-8.857353,-0.451884,-7.045015],[5.770302,-4.810325,4.452337,-5.206054],[-7.885603,-0.001007,-6.737347,8.997043],[-6.794934,-6.715403,7.624246,5.973693],[-7.098897,7.996123,5.075250,-7.429520],[-2.937982,-4.537857,-7.640385,1.287691],[3.480375,5.531631,-1.969704,3.683050],[7.207717,-4.136752,-9.052750,-4.295031],[2.244115,-4.599337,2.652793,-7.805966],[7.144660,-5.257875,0.437333,-2.744132],[7.342136,7.345144,1.010740,0.069608],[-6.609862,4.948763,6.986492,3.006106]]], dtype = "float32")#candidate|2762|(7, 14, 4)|const|float32
bop_2763 = relay.equal(call_2741.astype('bool'), relay.reshape(const_2762.astype('bool'), relay.shape_of(call_2741))) # shape=(7, 14, 4)
bop_2766 = relay.equal(call_2742.astype('bool'), relay.reshape(const_2762.astype('bool'), relay.shape_of(call_2742))) # shape=(7, 14, 4)
func_2321_call = mod.get_global_var('func_2321')
func_2324_call = mutated_mod.get_global_var('func_2324')
const_2768 = relay.const([0.457732,0.549997,5.474350,-6.711744,8.371628,0.381626,6.201847,-3.110039,-4.078398,1.708193,8.061628,8.453822,-6.406366,5.899560,-2.050757,7.269217,6.177724,-4.051254,2.454151,1.748870,-2.696047,-3.097704,7.764866,-3.032978,-3.861229,-1.132195,5.021463,2.031055,-3.814788,8.247108,4.640259,-2.019009,2.298777,6.301399,5.767234,5.090886,9.953278,7.618462,-6.303822,9.628961,-9.953130,7.821633,6.793157,5.514003,5.728877,-8.297822,2.653632,2.407210,1.052810,8.159363,1.664948,7.884426,-4.274728,-9.971617,-8.532063,7.052893,1.726836,-0.577209,3.339676,7.082360,-0.330623,2.229954,-8.777320,-8.714975,1.308601,1.859797,-3.576448,-3.856216,9.634107,-9.752623,-1.127822,-6.276890,-7.405967,-7.927858,2.032911,-9.191674,6.923520,4.607376,3.678080,9.711181,-7.140581,5.132477,4.651600,2.721390,-8.735274,5.244068,-3.818226,3.399050,-6.027544,-5.280956,6.826505,-0.871948,1.241775,-1.929286,2.203267,3.159790,-0.921873,3.589775,-3.588300,8.767841,-3.797745,0.280934,-5.189077,5.846643,-9.601631,-4.339975,-8.599545,-3.510089,0.527674,-7.244354,5.498088,-4.150071,7.274650,9.602656,-2.099804,-6.193899,6.726344,5.755322,-1.994324,2.372519,6.197583,-0.710933,-6.400577,2.777497,-6.359428,-6.438924,2.606101,8.981516,-3.107678,2.999498,2.783646,0.532357,9.075721,5.899289,4.175347,7.566660,-8.078781,1.598862,-0.463382,-8.356402,-4.173047,-1.159048,2.966714,-5.868571,9.036237,4.369258,-3.716780,4.933172,8.608717,9.034320,7.235708,4.861703,9.730593,-3.507118,7.691772,-3.404296,-6.777478,-8.116593,-6.369012,2.965938,-0.587004,7.477408,-8.174551,-1.838647,7.811805,-9.594393,-6.842651,-0.051446,-6.467670,-1.713416,-9.967659,-7.146824,2.620040,-5.355067,8.195649,0.655648,-8.807468,-9.467777,-4.771420,5.979628,5.744961,-4.733495,0.433361,5.436490,-8.762107,-5.631942,-0.979502,7.031573,0.067920,6.960392,8.940149,-6.244242,5.317473,-6.350213,4.134610,8.850432,-0.204545,5.427027,4.794533,0.848226,-2.167256,-5.338085,-6.053676,-3.635707,7.525360,8.531995,1.824103,5.043088,-6.135284,-3.923367,2.375196,-0.859501,0.260597,5.340880,-5.031154,-8.664475,-9.746646,3.318225,-7.563434,-2.377208,-0.888657,3.582028,3.917695,-5.215661,-6.072788,-3.442179,7.709127,3.373497,-7.828865,1.088634,-0.828385,1.498097,-0.496549,9.755982,-6.734097,-5.584494,5.760017,-1.000453,-3.125132,8.517019,9.310027,-3.470965,-6.251651,-7.033653,8.808118,-1.657604,8.819098,-1.715559,-0.213868,0.113791,-9.038403,5.117880,0.401492,-1.669996,7.400466,-8.094889,8.540127,8.991319,5.031727,-0.771295,5.883518,-0.846871,-2.714836,-6.071280,-5.215924,-8.343294,2.293424,0.011212,4.493750,3.658514,8.759717,-7.595413,-6.591073,-1.844056,4.986752,-1.418073,7.063692,6.352746,-4.606716,2.839034,5.859042,9.939937,4.191134,8.129578,-2.205914,4.686407,5.182637,8.170215,3.246615,7.781444,-6.485858,5.448880,-6.967688,-5.021753,-0.907080,3.153182,9.013461,8.851940,2.065217,8.870510,8.106717,1.273210,-2.529779,-8.538852,7.943123,-5.921740,-5.571170,2.482181,0.382185,8.458926,6.408306,0.810768,9.934594,-7.324980,-2.728395,-5.143806,-8.340565,-4.363278,-8.026878,2.067555,-0.018306,-2.063071,0.488360,1.538207,2.453589,3.371614,4.499737,7.519427,4.145541,-3.406060,3.760657,9.325987,-1.676106,3.514701,-1.219514,-1.094262,-6.593525,9.978262,7.283004,-9.256738,7.313261,8.227887,4.749311,8.049663,-6.628485,-2.967252,3.778478,-7.820876,9.549412,-3.793982,-4.490568,-0.878167,2.449412,-4.335584,-3.786243,6.049713,-1.619306,-9.145907,8.682216,-6.578953,2.578228,-2.040244,-2.930159,1.116675,-4.558904,-7.046227,-8.852987,1.190026,-1.948026,-6.391425,2.766636,6.135806,0.490085,2.273039,1.113631,-4.715495,-3.161315,2.029406,4.641725,-0.708856,3.708249,-2.980434,1.795370,1.782683,-7.221287,-3.806614,-0.212515,5.884604,6.520834,-0.459418,6.752672,-9.816365,7.195393,-5.467783,-9.558941,-2.366281,3.496868,2.286397,6.529984,7.938702,1.463772,8.666180,0.799518,4.276749,9.133393,1.271919,-5.024261,-3.516779,-5.738958,6.528742,3.184705,-2.986598,-2.714706,2.050726,-6.485602,9.322845,-3.774323,0.888539,-6.057779,-6.033333,0.494224,-4.797921,8.454808,6.270511,6.919502,-4.830148,4.961464,-2.063773,5.933769,3.252270,-1.368949,2.718535,7.293229,-0.054168,1.520219,0.841449,-2.067081,-9.300847,-1.672670,9.678739,-0.869984,-9.220472,-9.872498,-0.742113,-0.651128,-8.630980,-5.762036,0.810991,-1.458218,0.110798,-8.637299,-9.831618,-3.585542,7.190956,3.551353,3.715554,-2.173798,4.299015,-5.113596,-3.759265,3.432119,0.509327,-9.171073,6.572426,-2.626483,-5.257824,1.657155,5.853461,-5.669950,-4.195858,-9.742105,9.605503,4.539194,4.360584,-4.541613,-1.946549,-0.384074,-9.870904,-4.714544,-2.205441,-6.247171,3.444540,1.081635,-0.991131,6.554326,8.179300,-6.676563,2.066987,6.816641,2.906205,-7.233609,6.437348,9.762941,-1.650592,2.168412,-7.131842,6.613774,4.403082,-6.924635,-1.025408,-7.175233,3.748626,5.353436,-8.877036,-7.922190,-7.107337,1.409088,0.523370,8.732635,-3.170959,-1.804309,2.833772,6.419791,8.046405,-1.435062,9.102872,2.212187,7.738402,4.700389,-3.839537,7.922598,1.640946,-9.890020,6.118059,-1.302641,2.345468,-0.120794,-1.613385,0.289945,5.214862,-8.884300,8.115081,-2.169718,-8.313042,-3.689323,8.774345,3.087765,2.071377,8.103645,-6.938869,-6.551047,6.952392,-1.671554,-6.943161,9.611211,8.888230,8.133050,9.055796,3.977352,5.946663,-5.039297,2.517463,8.459251,-0.577914,1.885419,-6.402523,-7.418949,-4.949415,-9.760102,-4.962488,-1.064110,2.363512,-2.178365,1.623444,-8.147229,-4.701519,0.798362,-2.095912,-6.842812,-1.033986,0.341537,6.462975,-3.904613,-6.816084,7.031665,-6.941775,-8.838767,4.169886,-2.124620,-5.102603,5.945838,-8.117466,-3.343991,-6.884398,7.041794,-0.634065,9.266891,-0.762866,2.317730,-7.722605,0.112231,3.845557,-2.641157,6.662602,2.590475,0.672389,-1.981825,-6.270871,7.793596,9.320598,8.196933,8.223413,1.193666,-1.484232,7.025406,4.881789,2.472675,-4.829316,7.906409,-1.766771,-7.423902,-2.927064,4.815747,9.264541,4.701988,0.685142,4.444622,1.902330,-4.815318,0.918352,7.843463,2.862545,5.252512,-9.150500,9.053554,-4.209154,3.842712,-4.832548,2.136795,0.756660,-1.127837,4.265713,9.642281,-0.359168,-3.630918,0.157591,4.284900,-7.940067,8.433163,6.300668,2.156460,-9.044964,-5.512294,-5.808307,-3.836631,-7.234133,-3.239546,-9.650122,6.857778,-8.659730,7.911558,9.159141,-7.968176,4.620483,-6.301024,-7.325134,-9.814490,-6.820824,9.631423,-2.244855], dtype = "float64")#candidate|2768|(660,)|const|float64
call_2767 = relay.TupleGetItem(func_2321_call(relay.reshape(const_2768.astype('float64'), [11, 12, 5])), 0)
call_2769 = relay.TupleGetItem(func_2324_call(relay.reshape(const_2768.astype('float64'), [11, 12, 5])), 0)
func_1222_call = mod.get_global_var('func_1222')
func_1225_call = mutated_mod.get_global_var('func_1225')
const_2792 = relay.const([-1,9,-6,1,5,-2,9,-8,-7,1,-4,-6,1,2,-3,7,-7,1,-9,7,-10,-7,-3,9,-3,-4,7,4,7,9,6,-5,-2,-6,-1,-5,2,-10,-6,-4,9,6,7,-5,7,-4,2,5,8,-7,4,7,-7,-2,-6,-3,-4,3,10,-4,4,1,-9,-1,8,5,-1,2,9,-10,10,-4,-2,-4,6,9,-7,-5,-7,-3,-4,8,1,3,4,9,-7,-6,9,-3,-1,-3,5,7,4,-8,8,-4,-6,1,2,-1,10,-10,-9,-3,7,1,4,5,-7,8,7,-6,-1,-2,-6,4,2,6,8,4,-5,-9,-2,-1,-5,8,-1,6,3,6,3,-7,3,8,5,7,6,1,2,1,-10,-1,3,-4,-7,6,-8,5,-8,-3,3,-5,9,1,7,-9,10,8,7,-10,2,-2,-10,-4,-8,-3,10,-3,3,8,-5,5,-7,9,-6,-8,-6,1,-7,-6,3,-9,-7,-9,4,8,-6,-5,7,7,-4,4,-5,-5,9,7,-1,4,-9,-6,-2,-4,-9,-1,4,2,3,7,-8,-10,6,-10,4,-4,-6,-7,7,9,10,-4,10,-2,1,-2,-4,7,-10,4,10,-8,-10,-7,6,-5,-9,-1,-7,3,4,9,8,5,-5,-1,-1,-3,3,10,-7,-6,-5,5,-1,10,-6,3,-6,-1,9,6,-2,-1,-9,4,5,4,10,4,10,7,4,9,8,9,-1,-9,3,7,10,-2,5,7,-5,-7,6,10,-3,7,8,-1,2,9,-10,1,-10,-7,7,8,-6,7,-8,1,8,5,6,3,7,-5,-10,9,9,7,-1,-10,-10,8,-5,-1,6,7,3,-10,-5,7,3,-7,3,10,9,-8,6,10,4,-2,-7,-10,2,1,9,1,6,-6,-2,-3,-6,-1,-7,-2,2,1,7,-2,-3,4,-4,6,5,-1,8,-1,4,-7,-4,-4,-6,-8,6,2,6,3,-3,2,-1,-6,-4,3,10,9,-10,-10,7,7,-7,-5,5,3,-7,5,-5,-6,1,-8,-1,4,-9,-8,-10,2,-6,-2,-4,-10,-1,10,-7,6,-10,-8,1,-2,6,-9,-7,-8,9,-5,-7,6,9,4,4,5,-4,5,-6,-8,-9,9,-9,10,-6,-2,9,9,-8,5,2,-6,-2,2,7,10,-8,-3,-7,6,9,6,-10,5,9,7,-9,-8,3,-9,-1,-8,10,-7,-6,10,-4,3,-3,-1,-8,2,3,-8,-1,7,-10,4,-8,-8,-5,-10,-5,5,3,10,4,1,-3,4,-10,7,-7,1,-3,10,5,9,4,10,9,3,2,-1,-6,9,5,5,9,5,-3,2,-6,-2,4,-10,-9,-4,-8,6,-9,10,-2,-8,-1,5,-10,5,-5,-4,6,1,8,8,10,10,10,-7,-2,-5,8,10,6,-1,10,-3,-1,6,10,5,-10,1,-2,-4,1,-1,1,6,7,-2,3,5,-8,5,-7,-9,-7,6,-9,8,-10,-1,-10,-10,-4,-4,-6,5,2,-3,2,7,-2,-1,-3,-5,7,4,4,-4,6,7,9,-9,4,3,4,5,10,9,6,6,1,-3,-6,5,-7,6,-6,10,-7,-6,-10,6,-9,-3,8,-10,-1,-6,-2,-9,-5,4,9,1,-6,6,-8,-5,-7,3,8,-6,6,6,-3,6,7,9,-5,-2,5,-4,8,1,-8,1,-6,6,9,10,4,-1,-8,-7,-9,2,4,-9,5,-10,-2,10,-9,2,8,-1,-9,-3,1,10,10,-5,9,-9,-4,9,1,6,6,8,-1,4,1,9,-1,3,-10,-6,-2,3,-5,2,2,5,-5,1,2,-5,5,5,2,7,-6,-1,9,4,6,9,-3,7,-5,-3,-4,-10,-4,-6,2,-10,-6,7,-7,-9,-7,3,3,8,-8,7,-9,4,-1,-10,6,1,1,9,-9,10,-7,5,-3,-7,4,-5,-10,-4,1,-6,-4,-9,5,2,6,-9,5,2,7,-10,-3,3,6,-6,3,-4,-9,3,-2,-5,5,1,7,1,-3,4,8,1,5,10,9,7,8,-9,3,9,5,-1,5,6,-2,6,-8,-3,4,2,-1,9,-9,10,-10,3,10,10,5,-3,-6,7,6,8,-5,-1,-9,6,9,-1,6,6,7,9,-2,9,3,-2,5,-7,10,7,-10,-9,-8,8,6,9,-8,5,3,7,-7,-5,1,-3,1,2,2,10,6,3,2], dtype = "int32")#candidate|2792|(847,)|const|int32
call_2791 = relay.TupleGetItem(func_1222_call(relay.reshape(const_2792.astype('int32'), [847,])), 0)
call_2793 = relay.TupleGetItem(func_1225_call(relay.reshape(const_2792.astype('int32'), [847,])), 0)
func_2468_call = mod.get_global_var('func_2468')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_2795 = relay.TupleGetItem(func_2468_call(), 0)
call_2796 = relay.TupleGetItem(func_2469_call(), 0)
output = relay.Tuple([bop_2763,call_2767,const_2768,call_2791,const_2792,call_2795,])
output2 = relay.Tuple([bop_2766,call_2769,const_2768,call_2793,const_2792,call_2796,])
func_2801 = relay.Function([], output)
mod['func_2801'] = func_2801
mod = relay.transform.InferType()(mod)
mutated_mod['func_2801'] = func_2801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mutated_mod.get_global_var('func_2801')
call_2802 = func_2801_call()
output = call_2802
func_2803 = relay.Function([], output)
mutated_mod['func_2803'] = func_2803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_2813 = func_1322_call()
call_2814 = func_1322_call()
const_2818 = relay.const([[[-4.500612,-5.389458,4.992126,-9.126890],[-1.818508,-4.891952,-9.344959,3.817721],[-0.895920,1.105456,-6.333890,3.641345],[6.511720,-9.782795,-2.903641,-7.902149],[-9.433213,6.421125,8.797767,-1.356769],[9.502519,-9.764642,5.984294,0.116130],[-1.413795,7.907580,0.561705,-5.171178],[-5.987351,-5.727419,-7.032971,9.917162],[7.290443,1.639944,9.762747,-4.290268],[-2.034346,-6.542351,-1.230620,7.069461],[-1.016218,6.618189,1.141927,7.926781],[7.523016,-5.893312,-5.608163,-8.041653],[-3.658955,9.008115,7.009681,5.238722],[-9.905673,-7.240589,0.576399,6.060491]],[[-7.755012,1.377717,-7.085940,5.690025],[-7.372125,-2.231775,-7.502652,-5.124957],[-1.617525,-0.143598,-1.380677,2.195257],[0.620780,4.635683,2.992223,-4.955699],[-1.196776,-5.578945,-2.081911,-3.441682],[5.231055,-5.766414,2.626852,6.530602],[-8.713569,-4.977186,5.634451,2.898082],[6.384929,2.771574,8.317997,-8.254844],[-0.235113,-3.746550,-3.356914,3.030732],[0.748432,6.427009,9.546242,-4.579613],[-8.644425,-5.275118,-3.416417,-1.660054],[-2.658930,0.736633,-5.524238,7.142258],[-1.650118,6.386539,-7.733682,-9.358496],[-0.483148,2.126123,-6.606398,5.127259]],[[-5.567898,-1.974720,4.014472,-2.133215],[2.323656,0.122589,8.635486,-2.762118],[0.548963,-4.034989,-3.954713,6.981239],[2.713881,-8.431263,7.434876,-0.468611],[8.791305,-0.231974,-1.385364,8.893698],[-8.001320,9.450466,4.239762,7.656445],[7.416525,5.574779,7.845142,8.465170],[6.699665,-3.393387,3.214019,-3.681378],[-2.965256,-3.742103,1.542882,-7.908079],[-4.289099,9.074201,2.910229,-6.236426],[-9.805849,-9.429982,5.147276,-1.774303],[-1.409203,0.874775,-7.138296,-9.299760],[-0.111508,8.330330,-7.395517,-9.859324],[0.032783,6.699943,-3.600124,1.035371]],[[5.567170,-7.823906,5.949070,3.141023],[-9.219590,-1.859893,-2.980019,8.449960],[2.677243,-9.506297,-5.061033,-5.211071],[-3.410989,-5.062482,-6.008228,3.686167],[1.120244,-3.580990,2.889930,-1.031066],[-3.127685,-9.325125,-9.322838,0.050094],[-0.116486,7.959780,-4.849271,-6.528353],[5.945526,-7.802391,-7.831767,9.358744],[4.385195,6.182457,7.280016,-0.192877],[-7.724161,-2.655273,-7.340271,-8.777701],[5.746382,6.601979,8.130129,-5.772542],[-5.845554,-9.459983,0.815565,5.538197],[0.320155,3.724812,-6.475285,-2.596007],[-0.388925,1.789784,1.322009,8.698469]],[[-2.846537,-5.304016,-5.911566,-4.326442],[0.691875,2.441469,1.446093,-3.531620],[7.479892,6.265273,4.730222,-0.298997],[7.129522,1.446277,7.756827,7.860364],[8.591340,-9.247364,1.768908,5.084463],[0.761968,8.521174,6.646481,-9.980659],[1.478104,-4.106994,5.530696,-9.288261],[0.897477,7.056799,-8.071115,-2.263440],[3.512310,9.346298,8.745101,8.986276],[6.955028,3.622461,-3.269079,-1.842738],[-3.528702,6.792429,1.377236,-0.827853],[5.060464,-4.371020,-2.854274,9.811551],[6.449632,-7.355899,6.046318,7.430712],[-2.962496,9.379350,-6.448991,-8.536971]],[[6.745317,7.774285,8.969929,2.280775],[8.537953,-1.924353,-6.057776,4.930385],[-2.832764,-9.849978,-5.698160,7.575515],[8.837104,4.199412,-0.914245,-3.673699],[2.098928,-6.082962,2.039026,1.730894],[6.289659,-8.173458,-2.547514,5.327872],[-9.663767,-2.721311,-2.270166,8.501696],[2.801208,2.717756,7.755790,7.810727],[7.316005,1.124387,8.053613,-8.203912],[3.001046,-4.395922,-8.433064,-5.008402],[4.382590,1.612447,-0.355284,8.959821],[-4.201531,0.715978,-4.984329,-0.291214],[8.632374,-8.249276,8.278159,0.454430],[-8.501842,-8.262921,-6.126609,1.067903]],[[0.389637,9.033009,8.500372,2.337353],[2.622003,5.159526,5.387619,-6.801056],[-7.161710,8.110103,8.920608,-0.724422],[-9.165561,-8.431137,7.823767,3.142757],[5.471787,4.414039,4.968822,-3.000302],[7.050889,7.508857,5.894154,3.242034],[-6.203202,9.230409,-8.260221,5.781955],[-8.167618,3.560820,7.524425,2.073547],[9.669657,-2.001729,0.043912,4.398291],[-5.838373,-3.519170,-1.492694,6.892228],[-2.719514,-4.515008,-8.037766,-7.026845],[-9.376500,4.107022,-1.133586,-9.384744],[1.413797,-2.922649,8.922275,1.178741],[-3.242541,4.694756,-6.662146,-3.166043]]], dtype = "float64")#candidate|2818|(7, 14, 4)|const|float64
bop_2819 = relay.greater(call_2813.astype('bool'), relay.reshape(const_2818.astype('bool'), relay.shape_of(call_2813))) # shape=(7, 14, 4)
bop_2822 = relay.greater(call_2814.astype('bool'), relay.reshape(const_2818.astype('bool'), relay.shape_of(call_2814))) # shape=(7, 14, 4)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_2837 = relay.TupleGetItem(func_2801_call(), 0)
call_2838 = relay.TupleGetItem(func_2803_call(), 0)
output = relay.Tuple([bop_2819,call_2837,])
output2 = relay.Tuple([bop_2822,call_2838,])
func_2842 = relay.Function([], output)
mod['func_2842'] = func_2842
mod = relay.transform.InferType()(mod)
output = func_2842()
func_2843 = relay.Function([], output)
mutated_mod['func_2843'] = func_2843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2511_call = mod.get_global_var('func_2511')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_2852 = func_2511_call()
call_2853 = func_2511_call()
output = relay.Tuple([call_2852,])
output2 = relay.Tuple([call_2853,])
func_2881 = relay.Function([], output)
mod['func_2881'] = func_2881
mod = relay.transform.InferType()(mod)
mutated_mod['func_2881'] = func_2881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2881_call = mutated_mod.get_global_var('func_2881')
call_2882 = func_2881_call()
output = call_2882
func_2883 = relay.Function([], output)
mutated_mod['func_2883'] = func_2883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_2884 = relay.TupleGetItem(func_2881_call(), 0)
call_2885 = relay.TupleGetItem(func_2883_call(), 0)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
const_2888 = relay.const([7,-10,-9,6,-7,8,-9,-4,10,8,-8,6,4,9,10,-10,4,-3,-8,-2,-1,8,5,-6,-9,-4,-9,-6,2,2,5,-8,-1,3,1,-6,-6,-4,-6,5,-7,4,-1,-1,-6,-2,7,4,-2,7,2,6,8,6,-2,-3,10,-5,8,4,10,-8,8,5,7,-1,-5,-7,-9,-1,4,8,-3,-4,8,6,-4,5,6,-1,-1,-2,-1,1,1,-1,-8,-10,-3,-2,2,10,-4,-9,-4,3,-5,2,-5,-8,-7,-3,9,5,-10,4,7,-10,-9,-1,-9,6,1,-2,1,3,6,-2,-1,-6,6,-3,-5,3,-3,-7,-9,8,1,6,-9,-9,-9,1,-9,-1,8,5,-10,-7,5,7,7,3,7,-1,10,-1,-2,-9,9,4,-5,-3,1,9,-4,-9,-4,-10,-4,7,-2,3,1,4,3,1,9,4,-4,6,-9,-8,5,-6,-8,5,1,3,-1,4,-7,5,-9,-7,-1,-10,6,-5,-5,-2,-4,-4,-4,-7,-3,10,-7,5,-3,6,5,-8,3,2,4,2,10,5,4,10,4,-7,-6,-5,-7,4,-7,3,-6,10,10,10,-10,5,-6,1,-6,10,-3,2,6,-3,8,4,10,8,8,9,2,3,-8,9,-3,7,-2,7,3,-2,6,9,-4,8,-4,1,3,-5,6,-7,10,6,-1,3,-7,-8,-5,-10,1,-10,-7,10,-4,-10,-8,-1,1,4,4,-7,-2,-3,2,-3,-1,6,3,9,1,-10,-8,-9,10,-2,-9,-3,-6,8,-10,-8,6,-3,2,-8,1,3,-9,-8,-4,-3,-1,-3,-5,-2,-6,9,6,4,-4,-2,2,-2,-6,2,-3,2,-5,9,-10,6,5,9,-9,-1,7,6,9,-2,10,-4,3,7,2,8,10,9,1,-7,3,1,-1,1,9,-4,9,4,-5,10,8,1,-3,-3,8,-5,10,-3,5,3,-9,-4,5,2,8,7,-1,-6,-9,-1,9,-10,-1,1,6,1,1,4,3,5,-10,-9,-1,5,2,-8,1,-1,10,-2,6,-4,1,2,-5,-5,-9,6,-9,-1,7,3,7,2,-8,6,8,-2,9,2,2,9,-2,-3,-5,2,-4,-10,1,-8,6,4,5,2,-9,-8,-4,4,1,8,2,8,7,6,-1,6,10,3,7,9,-2,8,-5,3,-8,4,1,5,-1,5,-7,3,-10,-3,4,2,1,3,2,2,6,-9,7,4,-9,3,-9,-3,3,-7,-10,-2,-1,-4,2,3,1,7,-8,-9,-2,-10,7,2,-3,-4,10,-3,4,1,5,-3,6,6,3,-10,8,-7,-5,-4,10,1,-5,-10,-2,-4,-7,-5,9,8,9,-8,-7,-1,-8,3,2,-7,-8,5,-1,9,7,10,7,9,-5,-10,-6,7,5,-9,5,3,6,-5,8,3,-10,-3,-3,3,-1,-2,-4,-8,-10,6,-6,1,7,-7,4,2,6,-10,-6,-9,-6,4,2,10,1,-9,5,9,10,8,-9,-5,-4,4,-8,8,5,-5,-6,-1,1,5,2,9,-1,5,7,-5,-6,2,-3,7,4,3,9,6,3,-7,7,-8,-4,10,-2,-2,-5,2,5,-4,-5,9,-2,-5,8,4,9,6,5,-5,-3,5,3,6,9,9,10,8,-2,-8,5,8,4,-9,1,5,-3,4,8,-4,-3,-2,10,4,3,4,4,3,-7,-4,-8,-4,9,-7,-9,5,3,-4,5,4,-10,7,-2,1,-5,-10,3,-6,-2,-9,-5,5,-2,-2,7,-7,6,-10,-4,-8,7,4,3,-4,6,-8,-10,10,9,10,-7,2,1,-2,4,-6,9,1,-1,-7,-10,7,-5,1,6,-2,8,-6,8,4,7,3,1,8,-10,-10,-7,8,3,-9,-1,-3,5,-8,5,-4,-3,8,10,-5,-10,-9,-1,10,8,-2,-10,-8,4,7,7,2,6,-1,8,7,10,-7,-6,-4,8,-3,-2,-3,-6,-4,10,10,-7,-4,-8,5,10,-10,8,-1,1,5,5,-8,8,2,9,6,5,-3,5,-3,-7,-1,7,1,8,-1,-6,3,-2,-2,9,7,9,8,-5,9,6,-8,4,2,7,-4,-2,-7,-4,-5,8,-10,1,3,1,-9,3,-1,-9,8,6,-1,1,-3,8,9,-10,-6,-6,-7,2,3,3,2,-7,-2,-2,-3,2,7,6,9,-2,-6,-4,7,-9,1,6], dtype = "int32")#candidate|2888|(847,)|const|int32
call_2887 = relay.TupleGetItem(func_1426_call(relay.reshape(const_2888.astype('int32'), [847,])), 4)
call_2889 = relay.TupleGetItem(func_1428_call(relay.reshape(const_2888.astype('int32'), [847,])), 4)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_2891 = relay.TupleGetItem(func_1931_call(), 1)
call_2892 = relay.TupleGetItem(func_1933_call(), 1)
output = relay.Tuple([call_2884,call_2887,const_2888,call_2891,])
output2 = relay.Tuple([call_2885,call_2889,const_2888,call_2892,])
func_2894 = relay.Function([], output)
mod['func_2894'] = func_2894
mod = relay.transform.InferType()(mod)
output = func_2894()
func_2895 = relay.Function([], output)
mutated_mod['func_2895'] = func_2895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2444_call = mod.get_global_var('func_2444')
func_2445_call = mutated_mod.get_global_var('func_2445')
call_2941 = relay.TupleGetItem(func_2444_call(), 0)
call_2942 = relay.TupleGetItem(func_2445_call(), 0)
var_2944 = relay.var("var_2944", dtype = "uint8", shape = (780, 5))#candidate|2944|(780, 5)|var|uint8
bop_2945 = relay.greater_equal(call_2941.astype('bool'), var_2944.astype('bool')) # shape=(780, 5)
bop_2948 = relay.greater_equal(call_2942.astype('bool'), var_2944.astype('bool')) # shape=(780, 5)
output = relay.Tuple([bop_2945,])
output2 = relay.Tuple([bop_2948,])
func_2954 = relay.Function([var_2944,], output)
mod['func_2954'] = func_2954
mod = relay.transform.InferType()(mod)
var_2955 = relay.var("var_2955", dtype = "uint8", shape = (780, 5))#candidate|2955|(780, 5)|var|uint8
output = func_2954(var_2955)
func_2956 = relay.Function([var_2955], output)
mutated_mod['func_2956'] = func_2956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1673_call = mod.get_global_var('func_1673')
func_1674_call = mutated_mod.get_global_var('func_1674')
call_2961 = func_1673_call()
call_2962 = func_1673_call()
func_2263_call = mod.get_global_var('func_2263')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_2966 = func_2263_call()
call_2967 = func_2263_call()
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_2971 = relay.TupleGetItem(func_1126_call(), 0)
call_2972 = relay.TupleGetItem(func_1127_call(), 0)
output = relay.Tuple([call_2961,call_2966,call_2971,])
output2 = relay.Tuple([call_2962,call_2967,call_2972,])
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
func_2379_call = mod.get_global_var('func_2379')
func_2381_call = mutated_mod.get_global_var('func_2381')
call_3274 = relay.TupleGetItem(func_2379_call(), 1)
call_3275 = relay.TupleGetItem(func_2381_call(), 1)
func_2954_call = mod.get_global_var('func_2954')
func_2956_call = mutated_mod.get_global_var('func_2956')
var_3277 = relay.var("var_3277", dtype = "uint8", shape = (3900,))#candidate|3277|(3900,)|var|uint8
call_3276 = relay.TupleGetItem(func_2954_call(relay.reshape(var_3277.astype('uint8'), [780, 5])), 0)
call_3278 = relay.TupleGetItem(func_2956_call(relay.reshape(var_3277.astype('uint8'), [780, 5])), 0)
var_3288 = relay.var("var_3288", dtype = "bool", shape = (780, 5))#candidate|3288|(780, 5)|var|bool
bop_3289 = relay.less_equal(call_3276.astype('bool'), relay.reshape(var_3288.astype('bool'), relay.shape_of(call_3276))) # shape=(780, 5)
bop_3292 = relay.less_equal(call_3278.astype('bool'), relay.reshape(var_3288.astype('bool'), relay.shape_of(call_3278))) # shape=(780, 5)
output = relay.Tuple([call_3274,var_3277,bop_3289,])
output2 = relay.Tuple([call_3275,var_3277,bop_3292,])
func_3293 = relay.Function([var_3277,var_3288,], output)
mod['func_3293'] = func_3293
mod = relay.transform.InferType()(mod)
mutated_mod['func_3293'] = func_3293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3293_call = mutated_mod.get_global_var('func_3293')
var_3295 = relay.var("var_3295", dtype = "uint8", shape = (3900,))#candidate|3295|(3900,)|var|uint8
var_3296 = relay.var("var_3296", dtype = "bool", shape = (780, 5))#candidate|3296|(780, 5)|var|bool
call_3294 = func_3293_call(var_3295,var_3296,)
output = call_3294
func_3297 = relay.Function([var_3295,var_3296,], output)
mutated_mod['func_3297'] = func_3297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2607_call = mod.get_global_var('func_2607')
func_2609_call = mutated_mod.get_global_var('func_2609')
call_3368 = relay.TupleGetItem(func_2607_call(), 3)
call_3369 = relay.TupleGetItem(func_2609_call(), 3)
func_2379_call = mod.get_global_var('func_2379')
func_2381_call = mutated_mod.get_global_var('func_2381')
call_3373 = relay.TupleGetItem(func_2379_call(), 2)
call_3374 = relay.TupleGetItem(func_2381_call(), 2)
uop_3375 = relay.log2(call_3373.astype('float64')) # shape=(780, 1)
uop_3377 = relay.log2(call_3374.astype('float64')) # shape=(780, 1)
uop_3383 = relay.exp(call_3368.astype('float32')) # shape=(7, 14, 4)
uop_3385 = relay.exp(call_3369.astype('float32')) # shape=(7, 14, 4)
func_2321_call = mod.get_global_var('func_2321')
func_2324_call = mutated_mod.get_global_var('func_2324')
var_3394 = relay.var("var_3394", dtype = "float64", shape = (660,))#candidate|3394|(660,)|var|float64
call_3393 = relay.TupleGetItem(func_2321_call(relay.reshape(var_3394.astype('float64'), [11, 12, 5])), 0)
call_3395 = relay.TupleGetItem(func_2324_call(relay.reshape(var_3394.astype('float64'), [11, 12, 5])), 0)
func_2049_call = mod.get_global_var('func_2049')
func_2051_call = mutated_mod.get_global_var('func_2051')
call_3396 = relay.TupleGetItem(func_2049_call(), 0)
call_3397 = relay.TupleGetItem(func_2051_call(), 0)
bop_3399 = relay.floor_divide(uop_3375.astype('float32'), var_3394.astype('float32')) # shape=(780, 660)
bop_3402 = relay.floor_divide(uop_3377.astype('float32'), var_3394.astype('float32')) # shape=(780, 660)
func_1664_call = mod.get_global_var('func_1664')
func_1666_call = mutated_mod.get_global_var('func_1666')
call_3412 = func_1664_call(relay.reshape(call_3396.astype('float64'), [7, 14, 4]))
call_3413 = func_1664_call(relay.reshape(call_3396.astype('float64'), [7, 14, 4]))
bop_3418 = relay.equal(bop_3399.astype('bool'), uop_3375.astype('bool')) # shape=(780, 660)
bop_3421 = relay.equal(bop_3402.astype('bool'), uop_3377.astype('bool')) # shape=(780, 660)
func_3293_call = mod.get_global_var('func_3293')
func_3297_call = mutated_mod.get_global_var('func_3297')
const_3441 = relay.const([-2,-5,-9,-4,-3,2,-4,-1,3,6,-4,6,-6,2,-4,1,-8,-10,3,4,5,-5,10,3,-7,-1,-7,-6,1,-4,1,-3,-2,-5,-9,10,-6,-2,10,-4,-8,9,-2,-10,-5,10,-2,6,-5,6,2,7,2,6,9,-10,-3,-2,-5,7,-9,-9,-1,-4,8,10,7,-7,9,10,1,4,-10,-8,9,9,4,10,3,-4,5,10,-3,2,10,1,3,-7,10,-7,3,-8,4,-4,1,9,-2,-1,-3,9,4,-7,3,-9,9,3,-4,1,-6,-6,-5,-4,-3,3,7,-1,2,-9,10,-10,-6,3,4,9,-10,-9,-1,1,-10,-9,-6,10,-6,5,-7,-7,9,-4,-5,-5,9,8,-8,3,3,5,-2,-7,5,6,-8,6,2,-2,-4,-10,10,-4,-8,6,-9,-1,7,-9,4,4,-8,-1,10,-7,-2,-7,6,-1,-8,-6,-2,-8,-6,1,2,-2,-6,1,8,-10,5,-3,9,-5,-2,4,7,3,10,-3,-1,-5,8,5,-3,6,-6,-1,2,-2,7,10,-9,-9,-9,3,7,-9,5,-3,-2,-10,-8,1,-7,6,-10,-9,-1,10,-9,10,-3,3,4,8,-2,2,7,2,8,-9,-6,1,-5,7,-4,-1,7,-4,-9,9,-1,3,-6,-4,-3,-5,1,6,7,-1,-4,9,-8,4,-7,9,4,6,5,4,-4,8,-7,3,-2,6,-9,-7,7,-2,-4,2,1,8,1,7,-3,1,3,-5,-10,-1,5,4,1,6,-7,3,-8,7,5,5,10,7,9,8,-2,-8,9,8,-10,-5,-5,-6,-3,10,-8,3,10,1,3,-1,-8,-1,1,-7,6,-9,-2,1,1,-3,-8,-4,8,10,-5,-6,9,10,-9,-2,-8,-5,7,8,-9,6,-7,8,6,-5,-10,-3,-10,-9,-9,1,4,-10,4,-1,-8,2,7,-1,9,-5,-8,-6,-1,-7,-7,-10,6,2,-7,-3,-9,-10,-5,1,-8,-3,-7,7,5,10,2,-3,-9,6,-7,1,-4,-4,6,4,-4,-2,-5,8,-1,-4,-10,1,9,5,8,3,9,-10,-3,-8,-1,-7,-9,8,7,3,6,-7,3,4,8,-3,7,3,-10,-6,-3,-9,9,-4,-9,4,-3,4,-10,9,-6,-6,-8,2,4,-8,4,-1,3,1,-2,-1,5,3,4,5,4,4,4,9,5,-5,3,3,-9,9,-9,-8,-6,10,-3,-9,-10,-9,10,-10,-3,5,1,3,-2,5,5,-6,4,-8,-4,-4,-1,-7,-10,7,4,-1,-9,6,9,3,-3,-2,8,4,10,-4,-2,3,10,7,-1,8,5,1,5,5,-6,7,-8,6,10,10,-5,-5,-2,-8,1,2,1,-9,1,4,-2,3,-1,-9,-1,4,1,-10,10,-3,-5,8,-10,10,-2,1,5,-7,3,9,6,-9,-3,-9,6,-5,-10,-6,-3,-4,-3,10,-6,-8,6,2,-1,10,-9,-8,-4,5,7,4,10,-4,2,-4,-4,9,10,-3,-2,8,3,-6,8,-8,-5,-6,10,-9,-7,-1,5,-10,-3,9,-3,7,-2,2,6,-6,2,-5,3,7,9,8,9,-3,10,-8,-9,-10,9,1,-10,6,1,6,-7,4,10,2,-2,2,6,-7,-4,-8,-7,-8,-7,10,-8,-2,1,1,-9,-1,-7,-3,2,8,6,-10,-4,-1,7,-1,-10,-9,8,-2,-2,-8,-5,-2,10,4,-7,-9,5,3,3,-6,-4,6,5,-1,-1,8,7,-5,-1,4,-5,8,-5,3,-3,-3,-4,-1,6,-7,-10,-5,6,-5,-10,2,2,-7,-1,4,-1,-2,-5,3,-6,8,-7,2,-4,-10,-8,4,-4,-6,3,-10,-7,9,-5,3,7,7,6,-9,8,7,-4,5,-3,-5,-3,1,7,-3,-4,-6,-8,5,4,-6,-1,-10,5,-5,10,-5,8,4,5,10,6,8,-10,-9,5,1,-2,5,8,-6,-1,-1,6,-4,5,-10,-1,4,-9,10,-10,-4,-9,10,8,-6,-8,9,2,-4,-9,-5,-3,4,4,8,4,-4,10,2,9,-6,-3,-10,-8,4,-1,10,10,5,-7,-5,6,5,3,-1,-3,1,4,5,-10,-1,-7,-4,-4,-8,4,3,-3,4,-6,-10,4,9,7,-9,-10,-7,-3,4,9,-10,5,3,-4,4,3,-10,-9,4,10,2,-6,-9,-9,-6,-4,3,4,5,-4,7,-7,4,-4,10,4,8,-1,10,-9,-10,5,-2,9,6,-10,-3,-9,-1,-7,-1,-4,-2,-5,5,-9,8,-8,4,10,3,2,-7,2,4,-10,10,-3,1,5,1,-10,-1,-1,-8,-2,1,6,4,5,-9,4,-10,-6,-4,-6,-6,-6,-7,-1,-8,-7,-8,6,-4,2,7,-5,-1,-10,3,-10,4,-5,4,9,8,10,10,-7,-10,-8,-5,6,5,10,3,6,-7,2,8,3,7,3,1,10,1,10,2,-9,-3,-6,1,6,4,9,-7,-7,6,-2,9,10,-3,-3,6,3,-3,6,2,1,-9,-5,3,-3,-9,5,10,-10,-6,9,7,3,-2,3,10,7,6,-6,-1,5,-5,-1,-6,7,2,-5,-7,-10,-5,10,-8,-7,-8,-3,-3,10,-3,-2,-2,10,-4,-4,3,-1,-6,6,-9,-2,5,7,-6,-7,-9,-7,-9,-4,3,-5,1,-5,-6,-5,-3,1,2,7,4,-6,-2,-2,3,-3,6,-3,1,-6,-10,-1,7,2,-9,-7,10,3,-10,2,-5,-10,-2,-7,-2,1,5,-4,5,2,-4,4,-4,-7,-6,-10,3,-9,4,9,1,7,-3,8,8,9,-1,-5,3,-1,-8,-7,2,7,6,-1,5,4,-10,3,4,-7,6,-4,-3,-6,-8,3,3,-4,-5,7,-5,-7,3,3,3,-6,4,-8,5,-10,-8,-10,5,1,1,2,-9,2,-9,1,9,-1,-7,1,-4,4,-6,-5,2,-10,4,-8,-1,4,7,3,5,8,4,4,10,10,-4,-6,-2,9,10,-10,-10,-4,4,-3,-3,2,2,-5,-6,8,-3,8,3,-3,7,-6,10,7,7,-2,3,-8,-10,7,10,-7,2,-10,5,9,-9,-2,-7,4,9,6,1,-8,9,-8,3,-3,3,1,9,1,-9,8,9,1,9,1,3,3,-5,2,8,-2,-1,10,-6,-7,-3,-2,6,-2,1,4,-3,6,8,5,-5,9,-1,-3,4,-4,4,1,1,2,-9,8,3,-9,3,-9,2,-4,10,1,-7,1,3,1,7,6,2,-7,9,6,-1,-10,-4,5,-2,-8,-3,2,10,10,9,-1,-1,5,-6,3,7,-10,8,7,-4,-2,-1,-3,-10,-8,10,-9,10,10,-7,3,6,7,1,-7,6,-1,6,9,6,6,-7,-6,2,-2,1,-3,1,3,3,-8,-1,-7,3,-4,1,5,-6,-4,-9,7,2,-8,-1,6,3,4,-10,-1,-7,2,-5,-8,7,1,-8,7,2,2,4,-7,9,1,2,-2,6,-9,-2,4,-10,-7,-5,6,-8,1,6,1,1,7,-3,-4,-7,-10,1,8,8,8,10,3,4,-1,1,-10,-3,6,7,5,-3,3,-8,3,-8,9,7,-5,-5,-3,-8,9,-1,-9,6,-2,-8,3,6,10,-9,2,-3,8,3,6,-6,5,1,6,8,6,-3,-2,7,2,4,-1,-1,7,-2,-7,10,-6,6,10,-9,9,-7,10,-4,-9,8,-5,3,-3,5,-5,-2,5,4,1,2,-7,3,-5,2,5,-6,-1,2,-3,-5,-1,-1,4,-4,9,7,6,-5,-6,3,-9,2,7,3,1,10,5,-10,7,4,-9,3,-10,6,-7,5,-9,5,3,8,6,-7,1,9,-3,-5,-3,-10,9,9,5,2,-3,10,5,-9,9,-3,5,-8,5,3,-6,-3,6,-10,5,5,-9,3,6,-6,-10,-5,10,-5,9,-7,10,-9,-9,9,3,2,-8,7,-7,-9,1,-1,-9,10,-6,-4,-6,-5,4,-10,8,10,-7,10,-9,2,-4,4,1,1,10,6,-10,2,-4,2,4,-8,10,-6,10,10,-3,7,-10,-3,-6,8,-9,10,1,-7,-6,8,4,7,-2,-8,-1,10,5,-2,2,5,-10,-9,10,8,1,-2,-9,-1,-5,-5,5,-10,9,-9,1,4,-2,-2,7,8,5,-6,-8,3,-7,-2,6,-3,3,5,8,5,10,-2,-9,-6,-10,-7,9,-6,2,1,1,2,5,-9,-7,-5,-4,-6,7,7,6,8,6,4,-1,6,6,-5,5,8,-10,9,-1,-7,6,-6,8,10,9,1,-6,1,5,6,1,10,-8,3,3,-8,6,3,-9,7,4,7,5,3,5,9,-3,7,-7,1,-2,9,2,-1,5,-10,-6,-1,6,-2,-5,-8,10,-10,-6,7,9,-6,-7,1,-5,-1,7,-1,-7,-5,-3,-1,-8,10,-1,2,2,-10,-4,-3,1,9,7,2,-2,4,-9,6,7,9,-2,7,-10,-3,7,5,-9,7,-4,-7,3,-2,8,8,-6,3,-2,2,-9,-10,10,-6,10,4,-10,4,6,-6,6,10,-4,1,-7,-10,7,-3,-5,-7,-10,-3,-4,6,3,-4,7,-2,-1,9,-8,-4,-8,4,-6,10,-2,8,10,-5,7,3,-7,7,9,-6,4,2,7,-5,4,8,-8,3,-10,10,-2,-1,7,-9,-3,-1,-4,-9,8,-3,7,10,6,3,4,3,-4,4,-4,8,-7,6,-2,4,7,4,-9,-1,-8,10,10,9,-2,7,-8,-3,4,8,-4,-7,2,-7,6,3,-6,7,10,10,-10,6,-2,3,-10,-3,5,-5,3,-5,2,4,-5,-4,8,-5,-2,6,-3,9,10,-8,-4,-2,-5,-6,9,6,3,-6,-5,9,5,-1,-4,2,4,1,-4,-5,-1,7,2,-3,3,-6,-2,6,-10,-8,7,8,-1,-9,1,-6,-6,-4,6,5,-7,-10,6,8,10,10,-9,9,5,-7,-4,1,-3,10,10,-3,-6,8,8,8,6,-7,4,5,6,8,-4,-1,3,10,-9,-2,3,-7,-10,9,10,-8,-2,6,6,7,4,-9,-1,2,-10,-5,8,6,-6,1,10,2,6,-7,3,-4,-2,-6,4,3,4,-8,9,-8,8,-2,-1,-8,6,9,1,-8,8,8,-2,5,10,-8,-7,5,-8,-4,3,7,-9,-9,-2,7,-9,-4,-9,-6,-4,7,3,-9,-9,1,4,1,4,8,-7,10,2,-8,2,-10,-10,-10,-9,3,1,-7,-2,2,8,-4,5,-10,5,-9,-4,5,-6,-5,3,10,-2,1,-7,9,-5,10,-6,-8,-10,2,-6,8,-2,-4,2,1,2,9,-6,-7,-3,10,9,4,7,-7,-1,-4,9,7,5,-7,-9,8,-5,6,-2,-9,4,-4,9,3,-6,4,6,-9,9,-8,2,-4,1,-7,4,-7,9,-9,-5,-10,-9,8,-4,-4,3,-1,-10,-2,-5,-3,6,9,-3,6,1,9,-8,5,2,-7,3,-9,-5,3,1,10,8,-3,-10,-7,2,-10,2,4,-7,10,9,3,10,3,-2,9,4,8,-8,4,-2,-10,-10,-10,-5,6,-10,9,5,-3,7,-6,3,-3,-1,-3,-1,-7,9,-9,10,10,2,-1,-1,3,-6,7,5,2,-8,8,8,-4,5,-1,7,-4,-1,8,-9,8,-4,-7,-8,4,4,9,9,8,5,10,1,4,1,3,-5,-7,7,-7,-5,-3,2,2,5,9,9,3,3,3,-1,4,-7,-4,-9,9,3,4,4,-9,7,-1,7,-8,1,-4,6,-10,-3,7,-7,-5,-10,8,-6,-5,4,1,9,-2,1,-5,-6,-1,-9,-10,-7,-7,-5,-3,1,-5,-1,6,6,-10,-4,5,8,-2,4,-3,8,-10,-4,-7,10,-10,8,8,-4,10,-3,-1,-1,-10,-4,10,5,-6,-4,6,4,-2,3,-6,-2,6,-3,8,7,-3,-3,4,4,8,2,-9,-1,-9,-4,-3,3,-4,6,4,-2,-6,-9,-2,10,-8,-6,-9,1,1,-4,2,4,6,7,-3,5,5,-10,7,-9,-10,-6,-1,-6,-2,7,-8,9,-10,3,7,-3,-6,-1,10,-9,-4,9,2,10,-8,6,-7,-1,3,-10,-4,7,5,2,-10,8,-8,1,-4,1,-7,7,6,-3,-4,1,10,-7,-8,2,3,-1,-7,-10,3,-5,2,8,-2,7,6,3,8,2,-10,-3,2,-4,6,4,-9,4,10,7,3,-7,4,6,9,-7,10,-4,5,5,-3,-3,-5,4,-6,-9,-7,-9,-6,4,-3,-6,2,-7,-9,-8,-1,-7,-9,4,-3,6,9,2,10,-3,-6,8,-1,5,-7,-4,-6,-5,-3,-10,-1,-6,-2,8,-4,-5,-1,8,-7,-2,8,5,9,10,-8,-10,-7,-9,-7,-8,-7,-1,5,-8,4,9,10,-7,1,-2,-8,-7,-1,3,-3,-8,6,-9,-9,-5,1,-5,5,9,-9,-6,5,1,2,-5,5,-7,3,3,-5,4,-10,4,-1,1,7,-7,3,-10,2,-1,-9,7,6,-3,-6,-4,6,-2,-4,6,-10,-4,1,-7,-1,7,7,-3,3,4,3,-8,8,5,-10,-3,-4,-3,-1,5,9,2,-7,2,1,1,-4,4,-8,-5,-9,-1,3,5,6,-6,3,4,-4,-2,-10,8,4,7,-10,10,-1,2,7,-2,1,-10,7,-4,8,-4,1,-6,6,6,-8,-9,9,4,1,1,-3,8,-2,-1,-10,-3,-10,7,2,4,-2,-8,-4,-9,10,1,-10,5,1,4,-10,-2,6,6,3,-8,5,-5,2,-8,-3,-8,-5,-5,-7,-8,8,9,9,1,-7,4,9,-5,-5,-3,-1,3,2,-4,1,-7,-2,-2,-4,-3,-4,-5,8,3,-2,-6,-7,-10,-1,1,-6,8,7,-1,4,1,10,-10,7,-6,2,-3,2,-2,-10,2,1,6,-1,8,10,3,9,-10,9,-7,-9,9,-8,4,-4,-3,-8,3,-7,-5,2,7,-3,8,-5,2,7,-3,2,10,4,1,6,1,6,-10,-6,-2,4,-1,-4,10,4,-6,-3,-4,-4,8,10,-3,7,-9,-10,4,-10,2,-9,7,10,-2,2,7,-1,-5,-4,9,2,6,8,6,6,4,-4,1,-4,6,-10,-1,-8,4,-3,-5,3,-6,3,1,-4,7,7,2,2,7,-1,-3,-3,2,9,2,1,5,2,3,2,-3,-7,-10,3,9,4,-4,8,-4,5,1,3,-8,-3,-10,1,5,10,-5,3,-10,5,-5,-2,-1,6,-3,-9,6,3,8,1,2,-9,6,-2,-10,-10,1,5,-1,4,-1,-6,-5,-3,3,-6,-7,1,-6,2,9,2,-6,-1,-9,-10,6,-5,2,-3,4,-9,6,-6,2,-8,-2,10,9,-4,6,7,7,-4,2,6,-9,-8,-5,-7,4,10,8,-3,-3,3,8,-3,2,6,7,1,-6,-10,5,10,3,-5,-9,-5,-5,2,-8,10,2,-5,9,4,-9,6,10,-5,-5,-5,9,5,-10,-9,1,10,7,-2,-5,2,1,-8,-4,-5,3,1,1,8,-4,10,6,1,-9,-10,9,8,9,-2,-1,4,-8,6,3,-1,-10,-4,-4,2,6,-8,5,7,-4,-9,-10,6,7,9,7,9,-2,-4,6,8,9,8,-3,-7,6,9,8,3,-1,-7,2,-6,7,-1,-7,6,6,-7,1,-6,-2,2,-2,9,-9,2,2,-6,-9,3,-5,-9,5,9,-1,-2,10,5,10,5,-10,-1,-6,-3,-3,10,-5,8,-6,5,-2,2,-10,-3,-3,-2,-7,5,-9,10,-7,1,-9,4,-5,-3,-4,8,4,-6,2,-7,-2,-6,-3,4,-7,3,-3,-3,4,7,1,-5,9,-9,1,1,2,-4,-4,-6,3,-6,4,5,5,9,-9,2,-6,-8,1,-10,-7,-8,3,1,-3,2,-6,7,-1,1,1,-6,6,-7,3,10,4,-8,-1,-4,-6,4,-3,7,-1,4,2,10,3,-3,-5,-6,-10,-7,-5,-9,-5,-5,6,-4,8,1,-7,-8,-8,-7,-5,-3,9,-7,-1,5,1,-6,-2,6,-10,10,7,8,-10,-2,9,-1,5,1,4,2,4,2,10,-5,-4,8,6,7,-2,-2,-4,7,9,-7,-4,10,-1,-5,10,-1,-9,-6,-6,3,-3,7,6,-9,4,9,7,9,2,8,5,8,10,-1,8,2,-6,9,5,-8,3,8,-9,-9,10,-4,-1,-1,8,-7,5,-6,-10,-5,-2,-5,-2,-7,7,-3,5,2,-2,7,4,-4,3,9,4,10,9,-1,8,4,-5,-2,4,6,-8,8,7,10,2,7,5,2,-3,-5,-10,-6,-5,7,4,-7,-6,-6,-7,-7,6,-6,1,5,2,7,-6,-9,1,10,9,2,2,-2,-2,9,5,9,5,2,-3,-1,1,-9,6,-2,9,-4,-9,4,-5,1,10,6,5,5,8,-6,6,3,-9,8,-6,10,9,9,7,-4,2,-4,-1,-3,-3,-7,-8,-2,3,2,-2,-5,8,-5,-3,-2,2,-2,-3,1,7,8,8,10,-9,1,7,-4,-1,10,1,-1,-9,5,9,9,-4,9,6,3,2,-9,-9,5,-4,-6,-8,6,-9,9,-9,-3,-7,6,2,9,3,-6,-10,4,6,9,-8,-3,-7,6,3,10,-2,1,6,-1,-9,3,7,-3,1,9,8,6,-4,-1,2,5,8,1,8,-6,6,-8,9,8,-5,9,8,-7,8,9,9,-5,2,4,-7,-8,-10,-7,-8,-10,9,6,-5,-10,-1,6,-3,-1,-6,-6,5,-5,2,3,7,3,-3,3,-2,-4,4,-4,-10,3,-10,-10,-4,-10,-8,-6,-8,-9,10,2,7,-6,5,-7,7,-2,10,3,-8,-10,-8,1,7,-9,-4,-2,7,3,10,-9,-1,-5,7,-4,-1,-1,-1,4,-2,9,-4,-10,-1,-4,-4,-9,8,-5,1,9,-4,-10,-3,-6,-7,-5,-6,-3,8,7,4,7,9,6,3,-2,6,-3,6,5,2,6,5,-4,-1,-4,-6,-7,-7,5,-8,7,8,-4,7,8,9,9,5,6,-8,-1,3,1,2,-10,-4,-6,-6,9,-10,-5,2,5,-9,3,1,-2,-3,4,1,-8,10,-9,6,2,-4,-7,10,2,-2,9,-9,10,5,7,-10,1,1,-8,6,3,4,-6,3,-6,-3,10,7,5,-4,8,-7,3,10,5,1,8,1,4,2,-8,-4,-8,-8,2,5,-5,-10,-2,-2,-6,6,-2,8,10,-5,-4,9,-1,4,9,5,4,4,6,3,-3,-8,6,9,5,-6,-3,10,4,-7,-5,-8,-10,7,2,-9,-10,8,-2,-4,10,-5,-7,-7,1,3,-8,7,5,3,-5,-10,9,1,-4,-8,8,-7,8,-5,10,5,1,4,-7,3,1,-4,-3,2,3,4,-3,6,7,-10,-1,4,8,-10,-7,4,-8,8,5,-1,-10,-10,7,6,-9,-10,-3,4,2,-4,-9,-7,-9,10,-5,-2,5,-9,2,-6,-2,-3,1,-6,-3,2,-9,1,-3,1,10,-2,9,-9,9,-2,-4,-5,2,9,-2,-7,1,-10,-7,-10,-6,5,-6,-4,10,5,1,-10,-3,-8,10,-7,-3,5,10,10,10,9,10,10,-1,7,-4,5,-3,-2,8,6,-8,5,8,4,-1,-5,-10,4,-7,3,5,1,-3,-5,-4,-6,3,2,7,9,-9,-10,7,-10,4,-10,-5,10,-3,1,-7,-4,6,-10,-2,-2,3,-1,7,-9,-7,1,7,10,-8,1,-7,4,3,-6,-4,7,10,10,-9,8,7,10,3,-5,-10,-8,3,10,-7,10,-5,-1,-5,2,-9,10,4,-9,9,-9,2,5,9,-3,2,-10,-2,-3,1,1,-10,5,10,-10,-7,7,6,9,9,-4,9,9,-4,-6,-10,4,-7,-3,-2,-5,3,10,-6,-9,-3,6,-6,3,9,-6,8,10,-8,4,7,-8,-1,-2,-9,2,5,-6,-2,2,10,-2,-5,-4,5,-2,7,-5,-10,5,-9,3,-4,-4,10,10,1,8,4,10,10,-2,-3,7,-3,5,1,3,-9,-4,2,-10,-7,10,2,9,-5,1,7,3,10,1,6,-7,-2,7,-6,-6,5,2,-9,9,3,1,-8,9,2,9,5,-4,-8,8,8], dtype = "uint8")#candidate|3441|(3900,)|const|uint8
call_3440 = relay.TupleGetItem(func_3293_call(relay.reshape(const_3441.astype('uint8'), [3900,]), relay.reshape(const_3441.astype('bool'), [780, 5]), ), 2)
call_3442 = relay.TupleGetItem(func_3297_call(relay.reshape(const_3441.astype('uint8'), [3900,]), relay.reshape(const_3441.astype('bool'), [780, 5]), ), 2)
func_3293_call = mod.get_global_var('func_3293')
func_3297_call = mutated_mod.get_global_var('func_3297')
call_3449 = relay.TupleGetItem(func_3293_call(relay.reshape(call_3440.astype('uint8'), [3900,]), relay.reshape(call_3440.astype('bool'), [780, 5]), ), 0)
call_3450 = relay.TupleGetItem(func_3297_call(relay.reshape(call_3440.astype('uint8'), [3900,]), relay.reshape(call_3440.astype('bool'), [780, 5]), ), 0)
uop_3454 = relay.log(uop_3375.astype('float32')) # shape=(780, 1)
uop_3456 = relay.log(uop_3377.astype('float32')) # shape=(780, 1)
uop_3457 = relay.tan(uop_3454.astype('float32')) # shape=(780, 1)
uop_3459 = relay.tan(uop_3456.astype('float32')) # shape=(780, 1)
uop_3460 = relay.cos(uop_3383.astype('float32')) # shape=(7, 14, 4)
uop_3462 = relay.cos(uop_3385.astype('float32')) # shape=(7, 14, 4)
bop_3463 = relay.add(uop_3454.astype('uint16'), relay.reshape(uop_3375.astype('uint16'), relay.shape_of(uop_3454))) # shape=(780, 1)
bop_3466 = relay.add(uop_3456.astype('uint16'), relay.reshape(uop_3377.astype('uint16'), relay.shape_of(uop_3456))) # shape=(780, 1)
var_3481 = relay.var("var_3481", dtype = "float32", shape = (780, 10))#candidate|3481|(780, 10)|var|float32
bop_3482 = relay.divide(uop_3457.astype('float32'), var_3481.astype('float32')) # shape=(780, 10)
bop_3485 = relay.divide(uop_3459.astype('float32'), var_3481.astype('float32')) # shape=(780, 10)
output = relay.Tuple([call_3393,call_3396,call_3412,bop_3418,call_3440,const_3441,call_3449,uop_3460,bop_3463,bop_3482,])
output2 = relay.Tuple([call_3395,call_3397,call_3413,bop_3421,call_3442,const_3441,call_3450,uop_3462,bop_3466,bop_3485,])
func_3503 = relay.Function([var_3394,var_3481,], output)
mod['func_3503'] = func_3503
mod = relay.transform.InferType()(mod)
var_3504 = relay.var("var_3504", dtype = "float64", shape = (660,))#candidate|3504|(660,)|var|float64
var_3505 = relay.var("var_3505", dtype = "float32", shape = (780, 10))#candidate|3505|(780, 10)|var|float32
output = func_3503(var_3504,var_3505,)
func_3506 = relay.Function([var_3504,var_3505,], output)
mutated_mod['func_3506'] = func_3506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_3679 = relay.TupleGetItem(func_988_call(), 0)
call_3680 = relay.TupleGetItem(func_990_call(), 0)
output = relay.Tuple([call_3679,])
output2 = relay.Tuple([call_3680,])
func_3681 = relay.Function([], output)
mod['func_3681'] = func_3681
mod = relay.transform.InferType()(mod)
output = func_3681()
func_3682 = relay.Function([], output)
mutated_mod['func_3682'] = func_3682
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3710 = relay.const([[[-3,-7,-3,4,10,-10,-6,8,-1,9,6,-2,-10],[5,8,-3,-1,5,1,-9,-9,-9,-2,-10,10,10],[5,-4,-10,4,3,8,10,-1,-3,5,7,-6,-10]],[[2,6,-6,4,7,-9,4,10,7,5,2,-8,9],[10,-4,2,10,8,8,-6,-7,-7,8,-5,7,4],[-2,-8,-8,6,7,-6,5,-3,-7,7,-3,-9,2]],[[-5,-7,-10,-1,-10,7,1,-4,-2,-2,-10,-3,4],[-1,-8,-6,4,4,-10,4,-4,-6,6,-1,-6,3],[-1,-7,4,-8,3,-7,-5,2,-8,5,-9,6,-10]],[[-4,-1,4,-3,8,9,10,-10,-10,8,2,10,7],[-10,-5,-3,7,-5,-7,-4,-4,3,-6,2,9,9],[5,3,-1,8,-3,6,-4,-5,-7,-10,-3,-6,-7]],[[4,-10,1,2,-9,7,10,8,-2,-5,5,-5,3],[-9,6,9,4,-4,-5,9,1,3,5,-5,6,-3],[10,-8,-7,-5,-5,-4,-2,-3,7,2,7,-7,-7]],[[-1,-2,3,-6,6,10,-6,-6,3,1,6,10,-3],[-3,1,-5,-4,1,-9,-10,10,-8,2,-9,1,-3],[-7,7,9,-2,-2,5,2,-3,4,-7,3,3,9]],[[-2,-1,1,7,-7,8,7,4,7,-1,-8,4,-9],[1,4,-1,2,1,-9,-9,-5,6,10,5,8,6],[10,1,8,-9,-2,9,6,5,-10,-4,5,6,-1]],[[-1,-8,-7,8,8,-8,6,-1,3,-7,-3,-5,2],[6,-3,3,-10,-2,1,-2,6,8,-1,-9,6,-3],[4,3,-5,-8,-8,4,-1,-4,6,1,-8,-4,-8]],[[1,10,3,1,-4,7,-7,-2,-4,7,5,-3,-5],[-7,-10,-3,-1,5,9,-1,2,-4,4,2,-8,5],[-4,2,-9,-10,8,-2,-6,-4,-4,-7,-3,-7,-6]],[[-5,8,8,8,1,10,8,5,-8,8,-8,-5,1],[8,4,-7,-8,9,-6,5,4,-1,5,4,-8,3],[7,5,-7,5,8,-2,-6,-10,6,2,-3,6,-10]]], dtype = "int16")#candidate|3710|(10, 3, 13)|const|int16
const_3711 = relay.const([[[9,-4,-1,4,1,5,-4,4,-5,-1,1,1,-1],[1,-5,-10,6,-5,-6,-6,-4,10,-9,-8,-1,5],[-8,-7,3,-8,8,5,1,10,8,6,-1,1,-3]],[[6,9,-7,8,-5,2,1,1,-6,7,-2,4,-6],[4,-4,-8,2,-2,4,5,-10,3,8,7,-6,10],[7,4,10,3,-7,-6,8,-8,-5,2,-1,-7,8]],[[-3,-6,2,10,9,6,-5,4,-9,-9,-7,-1,10],[-5,-1,10,-7,10,10,-7,-9,4,5,-5,-4,-3],[-9,-3,8,-7,-1,4,3,-7,-3,3,-9,-6,-9]],[[-1,5,4,-10,-6,-5,7,10,-3,-5,-6,-7,10],[8,-2,-9,7,-7,-10,10,-7,-9,-2,-8,-9,-7],[1,4,2,9,8,-7,2,10,2,7,6,6,4]],[[4,6,8,5,-1,7,-1,8,2,1,-1,3,-4],[4,8,1,1,1,-7,5,-5,7,-5,-3,2,-10],[-9,-9,-1,-3,10,9,3,3,8,7,-8,1,-9]],[[2,-10,-4,-3,-6,-7,3,4,9,2,9,-9,3],[-3,1,-1,-3,5,-2,2,5,6,7,2,1,-9],[3,-9,5,3,3,-1,6,6,8,-5,-7,3,-3]],[[1,8,-4,-10,-1,4,3,9,6,3,3,-7,-6],[-1,8,5,-8,3,-6,-7,-10,-1,2,8,-5,-9],[-4,-7,1,-1,-4,2,9,-5,8,10,-7,-2,10]],[[7,3,-4,-2,-7,-10,4,3,7,-1,5,-6,-9],[7,-2,-3,2,4,-3,10,-9,-6,-4,9,3,6],[1,-4,-7,-2,-7,9,-9,7,7,-1,8,7,8]],[[-5,-8,-8,5,9,-10,2,-4,-7,1,-6,-3,-3],[6,-5,8,7,3,4,7,1,-4,7,1,2,9],[-10,-9,-3,5,-1,-2,-10,2,-4,-9,8,-5,1]],[[8,7,5,10,-10,-9,5,-9,-6,1,-7,9,-9],[7,-4,1,6,-1,-7,3,6,-6,1,5,6,-5],[10,-7,5,-6,-6,10,6,1,2,5,-7,6,-6]]], dtype = "int16")#candidate|3711|(10, 3, 13)|const|int16
bop_3712 = relay.less_equal(const_3710.astype('bool'), relay.reshape(const_3711.astype('bool'), relay.shape_of(const_3710))) # shape=(10, 3, 13)
output = bop_3712
output2 = bop_3712
func_3722 = relay.Function([], output)
mod['func_3722'] = func_3722
mod = relay.transform.InferType()(mod)
mutated_mod['func_3722'] = func_3722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3722_call = mutated_mod.get_global_var('func_3722')
call_3723 = func_3722_call()
output = call_3723
func_3724 = relay.Function([], output)
mutated_mod['func_3724'] = func_3724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3722_call = mod.get_global_var('func_3722')
func_3724_call = mutated_mod.get_global_var('func_3724')
call_3735 = func_3722_call()
call_3736 = func_3722_call()
output = call_3735
output2 = call_3736
func_3749 = relay.Function([], output)
mod['func_3749'] = func_3749
mod = relay.transform.InferType()(mod)
mutated_mod['func_3749'] = func_3749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3749_call = mutated_mod.get_global_var('func_3749')
call_3750 = func_3749_call()
output = call_3750
func_3751 = relay.Function([], output)
mutated_mod['func_3751'] = func_3751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2842_call = mod.get_global_var('func_2842')
func_2843_call = mutated_mod.get_global_var('func_2843')
call_3773 = relay.TupleGetItem(func_2842_call(), 1)
call_3774 = relay.TupleGetItem(func_2843_call(), 1)
func_3503_call = mod.get_global_var('func_3503')
func_3506_call = mutated_mod.get_global_var('func_3506')
var_3781 = relay.var("var_3781", dtype = "float64", shape = (660,))#candidate|3781|(660,)|var|float64
const_3782 = relay.const([8.071877,8.889025,-0.005429,-1.187411,-2.059742,1.540573,5.621735,9.509556,9.610083,1.016379,-1.032267,6.998521,-0.959134,4.466104,7.022262,2.538649,-4.232533,-7.344554,-7.852280,-0.748667,8.577239,-4.859999,6.836057,9.475199,-8.167632,-3.575431,-1.151152,0.406535,-1.114813,-7.936671,-7.219582,-9.895509,3.607256,7.444129,-1.074028,-8.475419,-5.308260,-1.976578,-5.860280,-5.227429,7.798058,9.662426,5.453774,-9.699592,4.576990,4.733148,-3.106150,-7.627838,-5.794723,-5.856084,-1.494376,-5.896071,9.294727,-6.071422,0.656984,-9.315071,0.668100,-1.876517,-8.573081,-3.524840,4.164992,6.627735,-6.583271,4.856954,-3.461729,5.591068,7.642083,1.138054,-2.240356,-7.829584,-4.069052,-3.156725,4.462108,-7.192718,9.128645,5.083227,-8.909089,3.293090,7.869053,6.186649,-8.588091,-3.969351,7.223017,-3.153887,1.292928,8.115792,-5.706250,-6.677928,-4.140596,3.748235,0.510351,-7.063053,-0.074468,-0.279974,1.356051,7.244440,-8.485270,8.720217,2.785328,-3.131581,-1.120545,-2.224193,4.744015,-1.646983,-5.471297,-5.719177,8.209075,8.432598,-4.403842,8.249341,-9.811426,0.231192,-3.891707,-7.162021,-7.321156,-3.487773,-2.707957,4.552592,7.250697,5.557137,-8.636835,-7.900043,-8.319737,9.524573,6.912078,-2.598479,0.972889,2.306179,-8.089780,9.096047,-1.148170,-8.961505,-9.719555,-6.465401,1.979266,4.496675,1.962016,2.235857,-1.849207,-2.508189,6.876040,8.426744,-0.637589,-5.506924,-8.064734,-7.595183,-5.523100,0.681541,-2.709051,-0.233337,8.111755,1.491304,2.320425,-9.525852,9.926458,-6.575671,-6.201077,6.627661,-5.244135,0.757239,2.627001,2.266958,-1.923673,6.488043,-8.374644,3.782690,3.460677,0.450902,4.860355,-6.459502,-4.390856,-8.664433,-9.709960,-7.619420,6.462265,8.098224,7.834507,-9.998347,2.443841,-1.259986,-2.169557,2.323937,6.741567,-5.762012,4.368303,7.587091,1.516539,-0.023670,-2.346181,-8.417175,-1.336209,-5.159976,-0.956331,-6.963872,-3.732840,-5.385466,-8.921960,4.240407,-3.356428,-6.473744,-8.224829,7.585953,4.589463,-1.862173,-0.846521,-6.545113,-6.608853,-1.905358,0.576983,7.391284,-7.016746,-1.931001,6.074741,-2.199991,-7.169589,4.004838,-9.419926,-0.377701,-2.278020,1.990822,-0.576214,-1.137269,9.287040,4.558525,9.011593,-9.331890,-2.059973,-8.925038,-2.325228,3.415847,8.369164,-4.369554,-7.564028,-2.288345,8.503739,1.749597,9.874835,-4.288993,5.443582,9.758893,-0.625929,-3.411026,2.861946,6.777811,9.455177,-0.216660,8.066686,-4.243719,9.477572,9.148171,0.060683,-5.013976,-4.524786,6.244901,9.217273,-5.705882,-1.377488,-4.598954,7.367474,-1.147706,6.854317,3.671585,2.694745,-5.433367,-9.974794,3.368818,-3.933350,-8.883496,-3.175733,-4.350770,9.380851,-4.531401,3.471241,5.368124,-8.812389,5.568040,-2.446667,-6.859454,5.149302,-2.113462,-6.146009,6.642132,-6.780074,1.043539,3.350118,-6.340291,-9.363735,-0.173819,3.176539,-3.524637,9.223439,5.358157,6.368337,6.984426,-3.926510,-1.681588,4.170559,-2.264394,-3.606016,3.498938,1.151928,-2.003581,-2.920075,-3.644614,-3.944017,2.257794,-4.702599,3.660918,-1.969114,-1.346153,-0.600791,-4.493122,-0.535796,8.586014,-6.977791,-2.624487,-4.144329,-8.164075,-3.051961,2.103104,6.791760,-1.454938,9.873975,0.563389,9.335845,1.017413,4.959050,8.926180,-7.820232,-1.462013,9.136894,-5.009531,1.668370,-6.007585,3.482411,-9.699816,-0.085455,7.241748,-2.017421,-1.007718,-8.219192,5.273356,8.527674,-2.549405,-8.620400,-5.329794,6.063423,7.735763,4.866010,-2.970834,6.737009,-7.474398,-4.237213,-4.821719,-2.491456,-5.854057,-5.176204,-2.382384,-4.675458,9.384184,3.365613,6.756025,-0.924701,1.304810,-3.649574,1.615112,-4.210274,-7.447024,4.098746,5.613960,1.711988,-5.567361,-0.725530,3.966653,4.780996,8.454059,-1.657829,-4.800686,2.471088,1.488727,8.686155,-9.844455,-8.731319,-1.743399,5.580893,5.194792,7.132663,-4.208500,4.781888,3.431822,-4.160635,7.162339,2.738148,4.097459,-0.904960,-5.990691,5.045124,8.083123,4.046551,6.808056,-4.537541,7.387421,8.769557,1.939636,0.354347,6.270243,8.153905,7.710232,-6.781678,3.893475,5.972469,6.696029,-8.356632,-3.816060,-8.240556,-7.281024,-2.566136,2.060521,3.300596,-1.178578,8.537923,-3.347866,4.785258,3.993161,6.698902,-3.154661,-2.612287,6.860023,-7.576501,6.779969,-8.664255,8.114650,3.282175,-8.579966,6.833110,-6.962062,-6.110703,1.371041,-2.588318,-4.520062,-3.058296,-8.472163,-6.544436,2.869806,4.900498,5.044278,4.065163,-5.995056,5.587089,7.528423,-2.291125,3.376508,5.710693,-8.483257,8.078796,9.610718,5.395132,7.661106,5.496280,-4.832881,4.736349,-2.394076,2.401383,1.801446,8.494835,1.511447,-6.491143,0.239689,-7.774580,5.452255,-8.662377,3.381659,-0.261792,0.375506,1.763367,-3.943655,8.540608,3.184247,-0.116663,-2.881586,-8.968463,0.063733,-1.326214,-3.483475,-8.181838,3.444555,-1.903775,-4.391300,9.034256,-9.677580,1.799135,4.309835,-0.090837,0.231704,8.608983,-2.126708,-5.238841,3.402777,-7.291482,5.459086,9.744314,0.026906,6.500542,5.822074,2.405605,7.745026,-5.236666,-7.519688,-8.613146,5.837232,3.327247,0.702850,5.152209,-7.353677,-8.560628,-2.956684,-8.186924,8.237516,9.612698,-5.891419,-0.611418,-7.271510,-5.852698,6.901786,-1.326780,4.029848,8.943572,7.130424,1.185843,-4.140417,2.905084,8.621008,3.636034,7.569685,8.773139,0.385839,-6.861156,3.121504,-8.100935,1.610608,6.043394,-5.603151,8.508011,-0.788759,-2.912938,-7.707947,0.043448,4.377198,-3.519498,-1.747113,9.744855,2.797092,4.231175,-4.077699,-4.166591,-0.006636,-0.333879,-4.252086,8.089616,-6.127037,4.741797,8.353383,0.160596,7.383057,-2.769211,5.624261,-8.749718,7.137096,2.655251,4.307580,2.159944,-1.349453,7.673159,9.221316,7.150622,-8.447695,-5.474645,4.793324,-7.622247,5.114110,-8.420031,-8.198838,4.250727,-1.238628,-1.752383,-4.938679,-4.612208,0.280461,1.172329,-7.595385,9.649221,-5.579493,-6.360514,7.450429,-1.488852,9.928811,5.316727,0.202149,7.296083,-6.176827,-6.712365,4.741394,5.478731,-7.045537,5.711404,7.679574,7.606900,-2.374039,1.618183,-4.825544,-3.783014,3.056269,-6.300178,4.998317,-3.831374,0.193811,-3.751686,4.686479,9.209042,2.830420,-5.090893,3.801595,-7.501436,-7.412819,1.140860,6.063998,-4.364073,-7.252191,-7.355347,9.979870,1.360838,6.227489,6.121854,9.700296,-9.830659,-2.353838,4.838330,-9.138922,8.459001,8.698161,7.148076,1.449738,9.988372,-6.802502,3.900544,3.826724,-5.976477,-9.668865,3.083846,6.348622,-5.884624,4.028809,2.271413,0.152719,-3.976433,-5.382601,-3.278213,1.767857,8.211698,4.392513,5.728031,0.251528,3.068725,-2.846292,5.679634,-4.206198,9.269275,0.234289,8.512441,9.653941,6.645271,7.880033,2.857558,-9.719710,9.218987,7.490614,-9.273122,-7.335460,8.482608,-8.760686,-7.182423,-5.771967,-7.336280,6.262220,4.186921,9.967408,-9.381947,-5.273042,-7.869583,-4.400819,-9.536622,-6.055117,-3.246565,-5.922478,2.640576,-5.758755,0.722434,9.845870,-9.814057,6.750310,-3.324139,-3.433652,6.077188,-2.883198,5.225511,6.993687,7.261148,-2.821569,8.905375,5.611397,-7.356160,-8.175488,-8.484754,5.105107,-6.288276,-3.035691,-5.173908,8.692144,4.742908,8.684935,-2.622839,-5.023009,-9.597954,4.593024,1.257865,4.949438,-0.904077,5.648779,8.220376,6.748686,0.045108,-9.885255,6.614169,-9.227487,-1.085576,2.020133,-7.408910,-0.954025,9.804417,-5.590852,-7.346142,-8.611457,-5.625372,8.224598,-6.639246,2.406051,8.460294,3.485928,-7.287710,7.506644,4.580432,3.836822,7.215376,4.086817,-7.162436,3.908722,3.720759,4.100652,-6.847191,4.267975,-1.459707,-4.747608,8.461415,-9.147660,3.661498,-1.499266,-5.313312,5.603437,0.240531,-3.161974,-3.840473,-6.445068,2.881584,1.950732,-2.184764,9.596897,-6.014255,-9.882692,1.301699,6.720217,2.996201,-2.798068,3.658933,5.539107,-9.793664,-1.702018,8.823130,-1.187825,7.860083,-6.781796,-8.468035,-1.329330,-0.973443,-9.056685,5.842542,-7.360149,4.557028,-8.156503,-3.723651,8.949296,-1.490666,-1.638316,-2.234259,-2.094845,-8.288983,-4.717706,-8.504116,9.562871,2.057535,0.068070,4.069590,1.539766,-1.362068,-8.417228,1.069743,8.097487,2.251769,-4.852746,-6.406179,6.801791,1.017317,1.666653,-8.459879,-8.522481,5.158882,-6.292994,-2.569242,6.201083,-6.849178,6.101839,-9.672932,2.200550,-2.153539,5.856183,-1.229177,-4.893776,-1.725520,-8.957555,-9.412422,1.864225,-2.208604,7.742542,6.074959,3.202259,-4.562661,-4.797887,8.952349,-1.377355,7.937288,-5.733594,3.241842,2.788285,-2.407776,-7.452709,3.608179,-1.520496,-1.407451,-5.304109,8.893676,2.354567,-1.580473,-0.252730,0.301765,-4.645991,-5.429476,-0.584883,3.095417,-8.642997,2.137849,-7.308871,-0.924262,-2.135806,-1.818138,-6.243179,-6.101041,5.512340,3.514126,-0.833278,9.977717,0.214720,0.254536,0.832162,-6.073695,3.520282,-8.618666,-7.166824,-7.992631,2.508118,4.691486,-0.092003,0.453239,-3.145511,6.728384,8.151627,9.864070,0.618369,8.212601,7.991856,-3.375905,5.909219,2.237540,0.049734,4.369946,-1.034316,-8.418298,-3.721219,1.241970,8.305049,-1.158265,1.878950,0.718545,-3.908428,9.633363,-0.229759,-9.211557,-5.188257,3.630639,-8.113800,0.075688,6.126131,1.498753,0.438538,9.268470,-1.578054,-3.149600,2.548026,-3.656142,-5.666497,-1.095547,5.005432,-0.718461,-9.261650,7.969472,-1.145027,3.252326,-7.287482,-3.024427,8.686814,-0.418828,4.129832,4.920514,3.427363,-5.882948,3.232467,-6.401344,-5.427890,0.933046,5.535913,2.535451,9.479686,0.750524,5.831301,9.069369,0.521504,-3.226056,-1.835553,-6.761663,6.236419,2.410277,1.809406,5.294087,4.094707,-5.307440,0.666314,-3.852875,-4.688589,0.026796,1.479526,0.370467,-4.933573,0.879185,2.272794,-7.973793,3.358117,-7.711315,-1.445010,-7.798355,-4.170513,-1.393198,-5.860921,-9.361214,-0.030552,-4.200969,-4.932906,1.955878,-7.460774,-1.353103,-3.006200,-1.088370,-2.952089,-7.163648,4.684165,-8.763252,6.180125,2.401820,-7.211485,-6.404005,4.183550,-4.157605,-5.049734,4.480152,0.372137,2.643215,-6.458343,7.735986,-9.285475,6.560907,-8.215586,9.957822,-0.780333,9.944285,-2.356872,-2.521181,-0.704414,0.739542,-1.867411,5.418581,-8.418404,1.845548,4.277243,-3.194460,-0.930467,1.926307,7.260802,-5.250457,3.834971,-3.541798,9.218649,-7.778871,-9.051899,3.130778,-6.147193,-9.191560,7.699357,9.676882,-0.902878,-8.814877,-7.642973,7.991665,-1.863972,5.873741,1.846225,6.108659,-9.548598,-0.969935,0.706818,4.437754,4.491088,8.083834,0.719192,8.764272,-4.893044,-1.804965,0.524668,-5.153392,7.581323,2.771710,-8.681436,-5.919340,-9.434584,1.333821,-3.578840,1.551548,-8.573719,-0.338143,-6.438253,3.267915,6.253596,5.217100,0.854958,-1.107667,2.216966,3.639255,-5.195811,9.029433,-2.007154,-5.122072,3.898874,-1.623753,-2.432386,-5.673503,-9.484444,2.136935,2.236435,-4.780320,1.365398,-4.694411,2.938284,-4.548156,3.767831,-4.236262,-4.644019,-8.203256,9.440163,4.853057,2.472102,-5.244953,4.517973,4.705242,-0.193888,6.889945,-4.385933,-4.060721,5.835277,6.669659,-7.125272,-9.502519,-1.942676,6.243200,-7.483649,-3.778465,-5.185851,9.054580,-5.402439,-6.803711,3.907880,-4.686276,6.805207,4.982919,2.077363,2.531982,-1.838167,-8.191100,-5.838338,-8.546378,-9.591014,-4.565781,1.808805,-3.129019,-2.434990,-3.573505,-0.536874,1.965481,-6.152171,-1.792293,2.953105,5.225625,-2.044755,4.485772,3.026739,8.462842,-2.760579,-4.071096,9.370646,9.198392,-6.164384,9.872749,7.039264,-3.575982,9.481248,4.798686,4.137933,5.234858,3.054423,-9.380676,-4.173064,-4.159969,-8.036556,0.468407,-7.082480,7.317020,-0.922637,5.653017,-8.442242,1.933782,0.797477,-0.445164,-7.568877,-6.929404,-1.207806,-0.767704,-3.027336,9.924295,-2.560220,-5.480076,-4.543303,1.952788,1.062944,-0.181814,-3.692278,8.513972,-0.927304,-7.092992,3.854080,-0.128025,-7.076997,7.712783,-3.722672,8.652464,9.154773,5.947137,4.463988,-5.628889,5.370617,-6.712078,2.569337,4.138173,-6.820242,-7.806789,-3.513876,3.483961,6.317095,5.817478,-8.696288,-5.235465,6.202992,1.589587,-8.184831,2.701448,-5.657169,-8.927630,0.532396,4.590225,8.720118,-3.547662,0.160419,-1.444709,-6.401559,-6.746528,-5.592859,-1.635761,-6.087228,6.546578,9.059967,-2.337744,-8.716323,8.511230,1.783508,3.135749,-8.119082,-9.930130,-7.382780,1.059630,0.279074,0.766503,-7.736733,1.506419,4.274434,-2.863403,8.563439,-1.318678,9.487795,0.837399,-3.249440,2.249400,-2.361771,-2.182492,8.590244,1.433317,4.563181,-6.507160,-8.316336,-1.769022,-6.597241,4.649846,-1.197379,-5.425320,2.912765,-5.134024,-7.849571,6.925627,2.085624,5.208237,9.590433,2.725742,6.155618,-9.786583,3.355900,5.977100,5.866127,6.159721,-2.570841,9.284385,-0.988909,-3.642822,-8.136493,4.845746,3.728871,-8.546869,-2.802572,-9.996703,2.856397,1.231065,5.113048,0.677627,0.130052,-2.265684,-0.074439,-9.545860,3.399321,4.385546,-5.943366,-8.482467,-6.785569,-2.922931,-7.881693,-3.123421,1.000486,5.660209,9.287671,-4.175911,0.043307,-5.243397,-1.116955,-9.212514,3.168452,6.377455,5.335892,-3.008772,-5.237773,-9.971248,0.038484,5.847829,-3.812866,5.137988,7.647725,5.749792,7.848791,-3.835097,-4.452044,7.219599,-0.653915,5.452102,-5.128443,3.622063,-6.976695,-2.588378,0.152128,-4.058366,-2.860356,3.442759,7.069763,-4.117282,-2.409717,3.843718,-1.627654,3.622703,5.511359,-0.817349,-4.773568,1.244409,9.755084,-3.130012,8.036615,-4.518853,-3.729314,8.760889,-1.382661,-0.431696,-1.382050,7.072474,1.310130,7.677533,6.115461,-3.860608,-5.017725,-4.198315,5.793557,-5.999816,-8.084487,-9.792070,-0.807066,-9.726652,-7.294202,0.092394,-4.596693,2.544236,4.527310,1.249849,-8.764490,-7.719241,6.715271,-9.374670,3.169011,9.952767,4.665226,9.684504,4.660114,2.807595,-9.422644,-3.615033,1.455807,-7.631676,-7.641369,-8.184658,-8.098157,5.757203,3.940651,-2.051438,-4.190421,-8.419426,-2.017139,1.418922,-4.762917,0.914170,-8.760305,7.242470,2.609006,-8.679913,7.210373,-9.255634,-5.081585,3.037319,0.375475,-5.577028,1.903126,7.455658,-8.398551,6.287816,0.670219,-8.944704,-1.026918,-0.759110,4.428906,-4.734863,5.514846,-5.798987,-6.159227,0.449320,-8.148659,-0.611966,8.797137,7.606391,-4.509065,-7.342301,0.917856,2.946119,-3.996153,0.161011,5.013881,6.856045,-3.937847,-1.545258,7.033659,-0.563643,3.238679,-2.139459,-7.185458,0.535440,-1.644927,1.413092,-4.314425,-8.987594,-7.492541,-4.603335,1.101452,-7.041507,-5.915528,-2.694825,-6.870759,3.346259,1.845064,-9.174986,7.020705,2.885489,9.619243,8.604754,5.536008,0.938968,4.474392,1.911955,7.564217,-3.976432,-3.275494,2.531890,0.667133,6.131788,-6.111756,-3.096126,0.216622,-7.485618,-2.402304,-7.100360,8.312259,7.830288,6.392049,7.588055,-8.488991,-8.779942,-9.279426,-5.432674,-8.227697,4.879778,3.307991,-1.176172,7.469889,-7.479486,-1.180250,0.718048,-1.915240,-9.029523,-4.675698,-9.622688,2.640138,7.576450,-8.986800,2.835284,0.236032,-4.201347,2.148386,8.334971,3.196987,-1.880503,-1.548175,0.056343,8.272989,9.053807,8.456978,-5.225258,-1.709011,-3.894329,5.454434,-5.733869,-0.973595,-4.693627,6.916555,-6.550819,1.917720,3.202523,9.933808,-5.573173,-5.557018,-7.063472,1.668182,1.069873,-4.141045,-2.738649,5.795063,9.769993,1.390772,3.632319,7.989286,1.987473,7.274835,0.651139,0.565424,3.772345,9.326689,0.587167,-1.561727,-8.829964,4.397965,6.259889,6.162346,-9.367495,-1.993305,-0.916224,-6.670683,-0.914625,-5.080739,-8.030309,2.536823,8.803963,9.123104,8.715201,7.944303,-7.454463,-4.496159,-4.929904,-1.877054,2.525734,-2.360589,9.136552,0.151101,-5.901856,5.336347,-3.271420,-0.697377,8.348860,-4.394563,-0.051014,-8.716505,-7.800297,-3.401066,4.055548,-9.386391,7.895589,-8.968483,9.408448,-1.425648,3.886392,-5.947495,-8.467972,4.261578,-0.085002,-9.228230,-6.179831,3.674451,4.121371,7.182744,3.689677,9.838249,-0.560657,3.819015,-9.770102,-6.987737,7.554961,8.669766,0.525535,9.423374,-3.005768,-9.656567,-0.037054,-8.508555,0.246557,-5.723751,7.092496,2.197036,6.839425,6.686108,-6.215820,2.788314,-8.098242,4.173865,-1.869716,3.947677,-5.676853,1.231300,0.211726,3.891266,1.337338,2.032580,4.391744,-1.454665,8.642005,-9.827055,6.959747,5.648964,-7.003619,-5.588665,9.027559,-4.992402,8.190376,1.089516,5.758037,-4.039317,-7.122233,0.567988,-9.973463,4.154873,9.593827,-2.164076,3.353322,-6.511626,-2.775576,-7.481760,-8.233932,-3.177750,-8.130741,-9.821414,-0.902261,-9.745148,6.236076,-7.176539,-4.146945,8.039505,-2.874517,-0.013783,-5.989103,0.922335,4.037589,-9.839386,-9.047295,-1.066418,-8.834089,-3.111182,9.541685,-5.368681,-3.357056,-3.512836,-1.592271,-5.225244,6.113754,-8.755633,0.630647,7.386153,-3.187227,-3.738934,-0.333256,8.768974,-9.897482,6.806748,7.046228,-3.812243,-0.037646,-4.477772,-8.711040,5.402763,4.827736,2.626846,-8.435137,-8.239298,3.027139,5.966906,7.577023,-3.262394,7.985210,4.364313,1.510327,-4.426884,-2.782993,-1.214479,-2.329910,6.242505,-8.138639,-8.830244,4.291271,8.203866,-7.430045,-0.490510,0.773972,7.995252,-5.720017,7.348010,-5.029538,5.875826,-2.646433,1.196144,-9.332387,6.669028,-9.270264,2.870239,-9.479635,-7.380407,5.612841,-3.079004,2.105931,3.653075,-3.008529,-0.297532,7.525901,4.068667,6.202203,-1.212735,7.782119,-5.553405,7.182255,4.102650,-4.132969,-4.097025,-9.666973,1.997959,-8.480497,4.652995,1.699978,9.619551,-0.630269,0.443556,-9.317794,6.519373,4.169444,6.047282,3.648639,-3.067091,-4.640796,8.580755,7.246806,-8.435212,-5.893988,-9.294386,2.318362,-6.829898,-2.269674,-5.256371,1.544736,7.346134,1.831860,8.735446,1.869760,1.131721,4.003629,5.282294,6.839541,-2.901052,6.524091,7.781466,9.827870,-4.748370,6.836282,-3.780273,-3.408962,7.921881,-6.655047,-0.833459,-5.611515,1.163840,1.359807,-3.239142,-8.582169,-2.542201,7.257829,6.900669,2.704552,7.176048,-1.423421,7.789724,7.548770,-5.519900,5.032579,3.282465,-7.894848,5.607820,1.764599,-9.342741,9.486547,-3.588438,8.106829,6.497213,2.244544,4.088725,-1.840689,3.848815,-1.547802,1.387952,-5.930218,7.471731,1.277585,-0.831913,5.353055,-1.579273,0.980612,8.023862,-5.936717,9.453277,7.717189,8.973554,8.053354,6.529097,9.012392,-1.373915,-5.107272,-6.584773,-6.720634,-8.495721,-0.221060,-8.899131,1.306638,-9.884678,-8.391462,-1.970191,-4.325521,4.267767,-4.501533,8.279952,7.681359,9.150554,-6.030881,0.735270,9.611279,-5.896567,5.774085,6.547217,-8.872337,-2.428602,-4.972396,0.541901,9.473260,-9.033648,4.374087,9.637945,0.885338,-9.920883,-6.959457,1.513674,-1.198589,1.487678,-3.253019,-8.663170,-4.419618,-0.126042,7.822888,-1.027031,-1.767939,-0.490155,-5.498468,7.447919,4.087327,2.291215,6.236284,1.142688,-1.027488,3.521628,2.016224,-1.473470,7.837670,-4.055148,-5.075357,1.967898,-2.143162,-2.005097,2.592511,-8.192970,-4.686077,-0.089811,-0.992060,8.328429,1.514934,-5.400938,-0.897772,-1.519503,5.176985,1.472145,8.875797,-0.564660,-2.397783,2.248110,-9.702760,-5.454634,1.071093,4.446063,-3.552162,6.283638,6.059233,6.645576,-2.292831,0.810805,-4.329805,7.305869,0.006264,4.930740,-0.247632,9.814865,8.875717,3.725717,6.118897,-7.127597,2.553336,6.517628,0.425897,0.029730,-8.878139,7.653092,5.713449,0.445026,9.350410,-5.940776,8.075489,-7.315306,-9.434304,1.469494,-3.371778,3.798833,8.186124,1.046767,0.863150,-9.368727,5.243581,2.566559,-1.264231,-1.867725,5.535783,-8.416979,-6.004185,2.044244,-8.779967,-1.178112,0.841143,3.044763,-8.609137,6.844230,9.530941,-6.422267,-6.066849,5.339078,-8.835644,-6.385439,-7.397743,-5.749396,1.582874,9.164188,-3.682155,6.416436,-1.676668,5.263515,2.905255,-8.113742,-4.444227,0.419529,-4.980458,-4.828438,-7.939411,4.694794,1.791210,-3.711780,1.433493,-0.170241,9.308857,2.280369,-0.081925,1.551493,-1.365416,-5.732229,-3.292193,7.901416,-5.261776,2.545716,-9.459296,-5.252343,-5.079580,-7.098585,-9.044791,9.333423,-9.462349,3.681298,2.701000,-6.693338,2.656353,3.006639,5.878185,-6.695925,-4.063096,-9.659390,-0.411793,-7.615143,9.049285,1.113703,8.772246,-6.819739,3.322762,3.596176,-9.387648,-0.443919,-3.483147,9.824818,-6.572329,-8.074919,0.467231,2.443652,9.261291,-0.224062,3.507498,-1.666672,-1.439622,-3.238255,1.496900,7.574075,-7.916362,0.735986,5.946112,-4.635395,-5.734493,-0.078383,7.347405,-5.369803,4.455091,-0.538474,-1.757013,3.692942,6.681303,-3.867420,5.708095,-2.054583,-4.518580,6.115450,-0.263796,3.534213,-4.170296,-8.131014,-3.292308,-1.180727,8.060225,-1.350463,7.529645,-8.056550,9.287775,7.014387,-6.575019,-2.577811,2.774721,-9.198590,4.457079,3.697076,6.791703,-0.392137,-2.800109,0.881143,7.193628,4.625310,-7.776941,8.121006,-9.819866,-4.362818,-7.042757,7.940296,-2.357621,8.074903,-4.949243,8.050567,-3.797886,6.396005,-8.732805,-0.127685,-3.890452,5.466555,1.541880,-1.486454,4.100956,2.182125,-9.555095,-6.816531,-0.150091,-9.425856,-2.307205,4.873984,6.554467,6.887507,5.049506,9.297989,1.477268,-2.732451,3.382857,-5.633142,-8.201086,-1.281430,0.423482,8.048092,-2.218248,-0.185472,-3.726677,0.639651,-8.474205,6.942654,-6.184409,6.359386,5.324503,9.576330,-6.271908,-3.583569,0.649809,8.315453,1.558711,-1.455516,5.685460,-7.211319,-8.999146,4.243148,-3.168463,6.105171,-0.994815,-6.615769,-2.640249,-0.525403,2.295461,6.049470,-0.699836,7.829042,-3.789557,5.632167,-6.705912,9.002771,-0.660242,5.102878,1.398556,9.261336,4.168952,-8.598987,3.686668,1.976526,1.461784,0.016794,2.453954,0.387430,2.704962,3.713540,-0.140314,-0.799978,-9.684654,1.242424,-7.417225,3.120518,-4.921936,-5.476937,-5.430539,-1.927543,-9.640475,3.247579,1.537617,1.189848,-9.155388,-6.207945,7.256863,3.795880,8.186212,-2.918611,7.170833,6.501808,6.733150,-2.232848,8.818261,1.903529,-9.583653,-6.927661,0.200521,-7.920107,-1.530351,-6.917371,-4.115727,3.999159,-9.083602,5.012619,7.240175,0.788998,-7.947449,4.589594,-9.502509,-2.033602,1.514605,-2.255283,-5.481343,-1.723443,-6.785795,5.305334,-9.510957,-5.188235,-5.064328,5.103219,-1.586078,-6.037326,-2.785011,3.287078,-1.166355,3.894154,-1.135296,-1.732592,2.084133,7.666445,5.870152,-7.828214,-3.766783,-1.847150,-2.142343,-4.117850,-3.378268,-5.024066,-1.702902,2.887734,3.948591,9.946327,0.933794,-3.043764,-8.060352,-8.617992,-5.014539,-2.018972,8.172968,9.730439,-0.081248,-9.380381,-4.246518,9.572990,-9.055122,9.288170,5.243075,1.751101,-8.292761,0.636069,-9.757563,-6.253389,-1.440320,5.406085,5.814114,-6.569366,-6.579133,-8.070837,2.155022,-8.133362,1.659935,3.555007,-3.616453,1.561747,-1.299345,7.181684,-8.862411,-1.529608,-4.060594,-9.665963,-1.643693,8.486528,4.750967,-3.367947,5.826516,6.575111,-4.868532,-6.144424,0.058477,-1.918822,-6.513960,-9.924624,2.878508,-6.137853,-4.437250,-2.450860,4.245497,-6.397714,7.880991,0.641739,6.974842,4.980394,9.693812,-7.726621,7.328266,-9.043787,-6.647928,-5.979539,1.294679,-0.180993,2.201681,1.938508,-4.906948,-8.399856,-6.717723,6.544842,-5.508380,7.126380,-1.975685,-1.144157,-8.522506,8.866497,-4.864546,3.091285,-0.044342,2.006595,-4.879042,-2.372056,-6.873496,-0.342887,-3.424368,-7.350707,4.038836,-7.810121,6.871824,5.183853,-6.539764,9.285570,9.706321,-3.362342,-9.340277,6.822940,-6.785976,1.084077,-5.090316,5.254632,0.182683,4.319164,-3.659029,-2.318773,9.367037,4.449368,4.291146,-6.503045,5.184218,-5.014871,-1.309999,-6.871040,-4.102717,-5.764762,-1.888961,7.274405,0.136980,-2.326936,3.085878,-6.359086,-4.852606,-5.312689,-4.718561,-4.059550,6.679861,3.209745,2.737550,6.860062,5.584340,-1.260160,8.039566,-1.517699,7.715507,-8.694658,3.195356,0.388501,2.871161,5.411685,-9.026008,0.791390,8.765972,2.014253,0.183057,-1.256596,-1.160380,-6.799853,-6.185260,1.813338,9.578880,-9.583938,-8.340933,-4.830908,9.805882,1.430073,-1.200828,-7.007136,0.672844,-4.975675,-8.417403,3.611558,4.143851,-7.339195,-5.940907,7.154476,-8.874644,4.676112,5.849988,-7.139585,8.423495,-9.302080,-0.463347,9.124224,1.553573,-3.170724,-6.767594,-8.297512,0.543960,-7.713917,-4.287581,8.811382,1.849074,6.033560,2.735369,-7.732348,4.363229,-0.999182,4.490995,9.697774,1.721919,-3.362380,-6.661271,6.557152,0.381666,1.678435,-3.083882,-1.813908,1.216580,-1.533103,1.476576,-7.019702,-4.800787,3.379952,-5.491096,-9.406257,-6.229204,-1.886243,7.157550,9.786208,4.790384,4.737462,1.049896,4.287982,0.588862,4.990353,-4.723035,-5.313648,-2.875341,-5.470856,-6.783900,-1.536159,2.675543,5.236905,1.209654,-0.907856,-4.999346,-4.484959,7.014072,-6.167423,5.180565,-0.109844,4.370413,-0.399977,-5.870547,7.164546,2.603134,2.036221,-0.952196,-8.979594,9.213132,-9.581129,-6.144124,-6.258173,-6.206588,-6.535140,-8.532623,-8.227686,2.578696,-3.126954,6.087580,7.488736,5.028614,-2.440616,8.088654,9.903664,5.144870,-2.780678,-9.688173,4.363440,-8.339734,8.614137,-0.207534,-1.754265,-6.551420,5.463694,-2.376873,1.697329,-5.170516,9.808160,-9.278048,-6.020571,-5.340601,2.082368,4.618199,-7.293863,-3.481668,4.218783,4.539851,0.604399,-1.995330,7.079289,1.204700,-7.633322,-3.076707,0.538768,4.743077,-0.241984,2.620604,-9.365048,8.078537,-2.621975,-2.454048,-3.058564,1.508749,-3.800535,6.926086,5.109550,-6.646521,-5.660699,2.044263,1.642488,3.268408,3.007575,5.238826,-1.359196,-8.751640,-9.684181,-8.813237,-6.553771,-8.015519,8.374407,-6.910699,-7.593572,-2.101489,-1.139403,4.406630,-9.291594,6.397482,6.443542,-6.649894,4.327450,-6.304824,1.344736,4.939633,-0.672991,-6.576993,8.253977,-7.036358,1.695454,-3.635890,8.614178,8.298325,-9.208508,1.093531,0.138040,8.656630,-8.989567,5.884890,-2.891125,4.045447,-2.741858,-0.453314,-2.325585,-7.955838,-8.029788,9.436413,-3.533166,2.911986,-4.085641,-6.000047,-7.065885,-8.818698,5.946807,8.195746,-6.940600,-1.489078,-1.732277,-4.793625,-5.839902,9.009301,2.355734,-6.396083,6.043514,0.225369,-9.628764,-3.091554,0.945112,2.215410,-2.883070,1.316546,9.092680,5.001716,-7.467020,-2.782555,-3.038780,1.347514,9.973082,7.281465,-8.769158,-1.202385,-8.913837,3.102040,7.526192,-2.519805,9.515453,9.843631,-5.425367,3.757534,-6.246460,4.061372,8.975878,4.033224,-0.443038,0.333642,5.442954,4.593615,-1.352056,5.509486,3.404722,2.703264,4.192565,3.992591,-0.779373,2.440937,-2.832224,3.413831,5.623158,-0.152827,-4.589562,-1.461438,2.092673,1.937440,2.080775,-6.436192,5.657617,0.122583,-0.497247,-1.170368,2.209432,4.094759,-7.241374,6.171855,2.686782,4.669132,-3.570084,0.289697,1.398031,0.158216,-4.277005,4.245263,-9.242925,-2.689851,1.825134,5.552942,-4.358507,-4.009903,7.019630,6.855473,-6.671029,-4.957080,-8.026718,-1.431048,9.186131,-7.309934,3.157074,9.821139,2.065319,-1.591803,-9.708141,1.539601,5.832988,3.227354,-1.505160,7.767738,6.424572,3.536322,-2.119880,5.119231,2.643465,8.047577,3.246508,-4.276719,-5.389772,8.383513,-0.674000,-6.244606,-5.776720,3.594694,-9.140292,5.424398,-3.360931,4.792038,9.779076,-7.954897,7.193891,5.237027,-7.638053,5.654154,4.749269,6.059419,4.001400,4.385511,1.919692,-7.366936,3.542087,6.455384,-1.486863,-1.224347,9.213357,0.948210,-3.698211,7.669538,-1.371786,-2.740576,0.699706,-7.892461,2.406379,8.816665,-7.419744,-9.185978,8.185202,1.091387,-2.556157,3.383639,5.012509,-4.231693,-1.878814,-4.229696,-4.069425,-0.450320,5.954691,4.471742,-8.885666,7.347893,-0.154752,-4.758725,-5.342083,-0.108434,-8.701899,-5.083507,-2.724706,5.581769,3.779005,4.098388,-4.603535,9.038985,-5.685627,-4.133719,6.802990,2.034600,2.500426,-1.299851,-0.663244,3.944405,-9.835583,-6.328235,-8.127179,8.990767,8.527754,-9.275632,-2.613267,8.102241,-0.423660,4.605479,-5.143512,6.221742,1.357118,5.040973,-6.401776,-2.027847,-0.174867,3.514824,-1.866416,-7.477282,-3.552711,-0.180590,8.887825,4.866308,9.109560,4.565689,-1.566998,-5.337349,-8.612338,9.375173,-4.974838,-1.386876,-0.865663,7.160990,-2.013828,-8.585576,-3.745223,-0.813721,9.228042,6.825927,-2.045951,-2.086318,-9.823929,-8.409192,-9.899429,9.196778,6.384118,1.545512,-4.733610,2.222045,1.395476,3.252505,-0.627196,0.811732,0.267487,-3.729661,9.373733,-3.778764,6.215330,6.793543,-0.683911,-8.121015,-6.961241,5.475089,8.021621,1.275222,9.304786,-0.672942,-2.369441,3.882763,1.659604,-2.543439,-5.818523,-9.604532,2.450810,1.549436,-3.968896,-8.801475,7.113904,8.803078,-4.564378,6.239950,1.602352,6.788572,9.553957,-7.559519,-9.427377,-1.328819,9.128327,4.791393,-5.582566,0.521326,-9.776758,3.551253,6.337931,-0.197983,9.501848,4.711419,-2.442563,2.346947,3.132197,-4.650022,-1.026708,-2.237524,2.445486,-8.569855,-9.644495,-6.582828,7.197565,2.962997,4.797609,-8.851104,8.582075,9.033708,-6.303289,-2.858611,-0.147577,-6.758613,7.538246,0.472802,-0.165455,-4.066486,1.968391,7.360785,-9.176042,2.295919,3.919040,-5.508746,-7.042599,-2.841867,-9.370977,-6.995093,3.574407,2.550023,-8.888638,0.721366,3.348526,4.197764,-3.485685,3.979858,0.725571,-0.612739,0.043390,-3.795021,5.354017,-8.798436,7.202268,-4.772232,0.728224,5.604381,-9.580637,-6.638651,-3.947044,-0.227105,3.978273,4.032079,3.402716,7.928498,-4.903515,-1.567558,-9.962386,-4.428397,5.459845,-9.409523,-4.832427,-7.092430,-3.953844,-5.897746,1.103115,8.876225,7.828416,9.939590,3.558393,9.617722,-2.290032,9.428352,-6.749075,-4.292501,-6.790171,4.629266,-7.941875,-7.767815,-3.583019,7.593571,7.523129,-8.236584,4.385026,8.412103,-6.044542,6.516260,-8.533490,2.550749,-9.390705,1.927630,-1.795861,3.339812,-2.973917,5.796302,5.308036,-1.983331,-3.408645,5.325421,7.309405,-5.190874,4.037483,-5.074547,-4.234680,-8.620441,-9.463616,9.561830,-7.632355,9.725619,-2.467291,-2.785202,-0.197405,6.245608,5.011376,-5.186191,4.809819,3.394967,-1.474160,3.364694,7.884217,6.551953,2.970807,6.377294,-9.319578,-8.693882,5.866077,-7.018536,-1.590665,-5.874781,-0.863952,-1.765839,8.464710,-6.590350,4.402119,-2.336649,7.391991,-9.789404,6.891906,7.888973,6.861236,-1.238101,-4.580143,-7.349700,-3.283776,-8.900126,9.462477,9.218769,-4.252965,5.802012,0.272334,1.546484,6.288418,7.045560,3.909292,-6.139691,-9.448413,7.922251,9.146811,1.171494,5.952956,-3.768345,-1.302052,4.570101,6.030546,1.605219,6.129989,-3.205892,-7.087295,8.557021,-3.834738,-7.191425,-9.199437,6.282490,3.337967,-2.243144,-7.347322,-3.701636,-2.993537,-0.083115,-0.702991,-9.375898,-7.409383,-7.910363,-9.763898,-2.309974,-1.819489,9.243088,-6.986896,-6.893689,-8.555740,-5.232321,-6.329031,9.362936,4.730067,-9.058940,2.282377,8.628016,7.239740,7.448014,6.254169,-1.502226,-2.130106,-2.822335,-5.703146,5.626049,8.719230,-5.313447,-8.088769,-2.049804,6.637126,7.736245,7.831391,-6.031897,-0.116210,-3.803713,7.947832,5.405875,5.587269,-4.153663,0.314126,-6.063661,-5.920733,-0.978762,-0.970969,-9.779922,9.534614,8.308303,-9.572302,-5.155605,4.371669,-5.369224,7.278892,-3.189248,0.979511,2.107004,-1.540075,-0.312841,-0.600109,0.934648,2.240152,-2.738729,7.855476,-9.456317,2.684283,7.062984,2.670786,9.096373,8.537060,8.900783,-6.011026,6.070789,-0.482280,5.382957,-4.701075,-0.242963,-7.760284,3.326504,-3.502188,2.008502,-2.305925,-8.298689,-3.784643,-7.799357,6.584346,8.758157,-2.106431,5.854428,-2.619115,8.091567,7.877122,-9.027742,-2.277379,-0.414799,6.506813,-0.875446,-2.135934,-3.679702,-2.711833,-6.369320,-2.101868,-5.097553,6.319052,-9.126322,-2.344815,-9.430396,7.497828,-8.190934,-4.361323,-3.503241,-8.302489,2.127448,6.262167,-6.363965,4.299793,2.253053,-2.889881,-4.292909,4.163329,4.285663,0.069573,-5.947043,-3.016312,-9.583537,1.980429,3.024977,-2.511461,-8.160850,-8.127437,8.994379,9.274855,3.484998,-0.593221,8.005345,-9.405244,-4.277021,2.049445,-7.114333,5.402811,-3.581748,5.569426,-0.877654,8.016287,5.172948,3.325032,5.229676,-4.511117,-6.510918,-3.854213,-5.470532,-0.174150,-3.348306,2.569513,-1.337807,-0.010282,2.697210,-3.787243,7.960733,-2.474978,1.786691,9.717223,8.931038,8.528670,3.235643,0.658556,0.484169,-9.089593,9.775071,-0.581276,-5.163604,7.999926,1.994870,4.452992,1.570671,7.631353,-0.902151,6.934317,-9.511989,4.027101,-8.466860,-6.086755,2.607242,-0.723677,-2.003195,-3.240296,0.406202,2.141923,5.208496,0.825997,-2.922248,6.812107,4.825196,-5.505917,0.904172,2.011075,0.003622,6.702159,-9.565545,1.141135,2.315931,1.054149,9.644184,6.339212,-4.613911,0.773459,0.352311,9.610239,0.175519,1.074472,8.535468,2.141830,-8.864308,0.577144,-3.532887,6.627132,-5.894267,-3.624500,0.268558,-6.139401,-5.784049,1.749300,-0.149351,-8.848830,-0.459457,4.386244,9.238637,-1.995160,8.308114,-7.717556,9.222469,5.427794,1.842848,4.387848,3.345820,-7.469837,-2.484010,-5.454855,-0.235061,-9.882350,-7.500666,-5.077216,-6.170964,4.236613,1.810827,8.940199,3.705977,-5.177449,-0.500428,-4.287308,-3.803080,7.688087,-8.852068,4.321674,4.302836,3.465798,7.469059,0.181955,2.586200,-7.533624,-4.072627,3.901666,-9.673063,-8.432551,9.705768,3.234629,5.425600,-7.212863,-0.189583,-7.056105,-1.724252,9.226545,-8.566163,0.434037,3.702299,-9.397471,-5.594842,1.750565,9.224506,2.746959,-0.444366,-6.855506,-1.551024,5.183681,6.976853,-9.931261,-3.739784,4.718627,-6.406785,-8.712634,-0.185425,0.535549,-2.008060,-3.909869,7.763339,-7.752680,-3.451740,6.398821,-1.719170,4.292335,3.504853,9.925580,3.223094,-5.150874,8.787682,3.976114,1.087597,-0.355711,8.192395,6.740804,4.076054,7.510936,6.937532,-8.866505,1.675180,9.067231,6.382118,-9.009942,2.153535,-3.670336,9.913662,2.278237,-6.679258,-4.678491,-2.097888,-8.207794,-3.835618,9.211647,3.866655,2.654129,9.915730,7.559659,9.898493,0.230581,-8.488947,0.954200,1.962217,-5.183215,0.049895,4.177645,-3.780503,2.781000,0.448705,-0.397959,-5.830294,-7.449846,-2.902989,-0.394394,8.854948,1.092160,6.064623,-7.817386,9.923675,-9.768595,1.005975,-6.369304,-8.168184,-6.836652,-2.658760,-9.750428,-9.480364,-8.551304,-9.038974,-5.172753,-4.137128,8.000901,3.785954,-2.421796,-8.483275,2.686573,-7.773258,5.771890,7.370658,7.744540,9.148381,-5.059127,-8.512726,-0.544425,9.376204,-8.372650,-5.829784,1.204469,0.981740,-0.848239,-8.446147,-1.840092,1.184669,6.826236,1.564469,-7.430514,-4.148661,2.078282,7.049218,5.266057,-4.735619,-5.182652,7.015601,-8.043376,7.108264,-4.031539,-2.118642,9.452622,4.513610,-1.542461,5.182550,0.078876,3.914427,-3.624677,-7.501859,2.347536,3.256306,-4.669140,1.142346,-0.527463,8.845753,5.856116,8.538353,-7.684773,4.611287,8.737050,9.868116,8.858288,8.006251,-3.260219,8.690864,1.214039,2.660741,-4.493592,-8.689821,-5.952371,4.458888,-5.099913,-9.003241,8.394759,8.567984,-9.839599,7.502796,-8.969749,8.561187,1.313906,-9.580013,3.080637,-6.504005,4.029007,-6.352123,-7.224110,6.027185,-1.047018,6.884669,8.105545,0.810923,-0.711904,0.770942,6.847268,7.387916,-2.304348,1.848479,3.759190,3.436066,5.104571,-8.078808,1.937185,-7.239972,8.461109,-0.441263,-0.899206,-4.855260,-6.331000,3.447644,-8.112886,-4.999212,3.675798,5.716496,2.114604,0.131543,-2.716426,5.297794,5.845878,-8.099701,0.780750,5.953378,-2.653034,-2.729417,-8.047890,-8.201744,-7.712891,4.047428,8.007524,2.118469,1.233345,8.241799,-8.090574,8.015802,-0.479302,0.895772,-0.007540,2.959616,-7.619478,-6.112193,-5.289491,-0.785365,5.551801,-5.166252,-1.704765,-7.641225,-9.829584,1.383227,-4.633797,-1.676142,-8.743020,-4.555398,-9.893118,8.664693,-4.841672,0.954840,4.072137,5.999302,4.741287,5.548756,5.156865,3.194748,2.137966,0.986006,-4.891921,-6.351398,2.742981,9.618157,-0.919292,-7.641054,-7.726334,6.502292,7.849306,3.836099,-0.463476,-2.424781,-6.756749,3.994798,4.511216,6.923695,-2.580780,-6.232757,-0.721817,-8.441614,2.158395,1.972289,-0.720646,5.552532,-1.956367,0.205035,1.942367,-3.107600,8.354249,2.116417,-3.319198,-0.912323,-2.559212,-6.813472,6.676476,9.345991,-1.614081,-0.612797,-5.239704,-1.386807,-7.859920,2.934427,-4.930772,1.740480,-8.172490,-9.920251,0.710954,3.606534,2.083612,7.454364,-9.142359,1.705488,4.523473,-1.926035,1.980679,-7.774837,-7.855115,5.856946,-3.108272,-4.922264,4.575619,0.292852,-7.975388,-8.803360,7.395159,-3.329336,8.298884,-2.855257,0.817699,-6.308162,6.058144,6.321738,-6.444317,-0.475982,2.299550,0.386512,9.527523,-2.660249,-4.499902,-5.633343,-7.143944,4.297429,-9.944030,-2.325137,-6.490499,6.882185,-9.734183,4.739269,8.050027,8.217400,8.023017,-3.799371,3.656806,-6.828998,2.021193,5.231065,8.121908,2.712554,-8.479383,8.059141,-9.453576,5.147677,5.360574,-9.954527,-9.751545,-2.774398,-5.026218,4.556996,5.389234,0.270318,-7.443303,-6.010148,-7.300844,1.623177,1.037388,3.222433,0.972019,-1.756955,-9.691529,-0.236614,-7.294882,-6.075937,9.329708,6.533885,8.470247,3.153554,9.672791,5.521993,-0.869476,4.189562,5.270207,1.732542,8.581257,-3.696982,-3.866722,-0.553185,3.083419,-2.310260,-3.243991,2.901715,-7.797963,0.415795,-8.585842,6.508237,-8.940192,-0.822771,-1.912540,-5.692538,-6.265066,6.816364,1.907124,3.510541,-3.541175,0.707238,2.646608,-9.791126,-5.713087,-6.629563,-9.059884,8.997842,-9.705236,-7.730233,8.053763,-0.395197,2.609149,3.200226,8.015337,1.002258,-2.414126,6.876864,2.125594,6.701655,7.643968,-3.522195,-6.676942,-8.644950,-9.357043,8.683649,-7.320460,8.548427,6.536119,-1.649060,7.517360,-7.921044,9.397130,-7.692576,3.549346,-0.259225,6.823456,-1.840407,-1.631012,-2.467165,5.199169,-6.861678,1.961458,-0.274563,-3.429612,0.283608,-3.105560,3.835864,4.976948,4.942088,-1.729881,-0.920213,-8.030400,1.855489,1.074505,3.663182,3.737057,-2.484223,6.385538,1.868640,-4.694458,-5.643600,-5.637959,-5.518464,8.456242,-8.535720,9.076838,8.489794,4.275654,-9.459840,-5.659588,5.355473,5.354236,-5.013250,-8.919744,2.522581,-0.736893,-1.810283,8.723988,5.413405,-5.283001,-5.942967,-0.629501,1.126902,-8.606240,-9.513809,-4.903371,-3.231528,-6.201124,-3.934371,-5.147464,4.917788,5.395690,5.141394,-9.146364,7.348329,-4.933921,-3.932608,2.811693,-0.165137,9.268614,-5.488313,3.121329,6.097348,9.548732,-5.599276,7.255839,0.781278,4.852061,-6.600572,6.993460,-0.869380,7.357403,-3.088237,9.901092,0.136237,3.495269,-0.879784,-9.895172,-1.167970,1.841977,-5.473879,-3.006604,-1.985522,-1.714756,3.901259,-3.222271,-0.780995,-3.108250,2.856827,4.463094,-5.970449,-5.961580,3.931626,8.963333,3.641095,5.218317,0.209852,5.264549,8.179698,-4.947342,6.538818,7.790543,4.759111,-4.825507,2.700930,5.870060,-1.329846,-3.205516,-9.009898,-4.164988,-8.917088,7.165297,6.784108,6.588008,8.861817,-3.227113,5.986906,-5.568807,0.340043,7.226721,-4.801831,6.764428,-1.385063,1.549308,4.249620,-8.886008,7.478509,0.454534,-4.694498,8.128176,1.780584,-1.951033,6.974307,8.576453,6.867296,3.456962,9.139762,3.724302,-1.873182,-0.227296,-3.972547,-5.917336,9.816264,-3.509839,-8.468229,2.361937,9.321644,-4.637260,-8.326093,-2.378484,-2.127625,8.182290,-8.785704,-6.627921,0.980832,-4.495250,8.325210,0.598094,-8.236875,9.299937,-8.172469,-2.349668,-5.179811,-8.357844,-0.784783,7.024153,8.973356,-5.290472,9.205270,-2.935904,-8.923466,-8.922597,4.399245,-6.440587,9.334489,4.397444,-7.078769,-5.502766,-4.575898,7.560814,2.090277,-4.220565,8.576249,-5.195024,7.179445,-3.010819,9.739587,3.173280,-6.665056,-8.394526,2.240806,2.595645,-0.521700,5.668731,9.731726,3.149296,8.678564,1.721751,0.697533,5.986904,-4.804596,-8.173526,-3.067406,3.561974,2.250866,-7.878172,2.336767,-9.804791,8.032517,-7.152208,-4.695543,7.900731,6.463231,-8.533750,-9.561854,7.065517,5.182565,-5.592852,-2.070872,8.736956,-7.018176,-8.732409,5.524139,4.516727,-4.354058,3.081571,9.366324,-0.046319,2.944114,4.309109,-2.930155,7.552888,-0.741720,0.774808,0.736660,-3.647224,6.266125,4.234574,7.128515,5.052352,-1.607108,-6.425675,-1.977769,1.043340,-3.116073,2.937344,2.601421,-2.129670,4.892192,-4.635055,-9.985756,-7.246821,-2.646521,2.515594,-3.961696,1.470201,4.527958,-3.392584,3.898656,-3.058273,1.235178,-8.268590,-9.124139,-8.391122,6.968512,-3.866914,-9.543573,3.309374,-2.561691,-4.360157,0.149965,4.441896,-9.545916,-9.627124,5.491792,2.499633,1.066986,-4.006926,-9.579547,9.835967,6.034184,-9.435907,-4.750809,-0.970576,-3.360900,6.263918,1.687144,-0.282737,-2.262702,9.099329,1.547793,-1.984497,-1.570101,-0.561186,-4.694559,-8.161257,9.314993,1.761833,-0.731964,-8.892800,-0.001280,3.408000,6.506605,3.173148,-4.009517,5.206602,9.381965,-7.048494,-8.611496,3.649923,-4.994460,6.230539,-7.341037,8.048033,-7.086665,4.509857,0.300007,-2.977355,-7.854431,4.311320,-6.306073,7.442154,-1.715269,-4.921432,-6.181762,2.841211,8.856804,5.796384,6.170007,1.267094,-9.682770,7.741907,4.805193,-0.523854,7.911231,-2.429981,5.958709,-3.669053,-1.741056,-8.150211,-3.042094,9.802183,-4.737786,2.944640,-1.062811,-6.945260,3.228428,-1.198272,8.676476,-4.472700,-8.494468,3.106405,-9.622582,-7.572896,-1.560511,-4.467207,-5.245715,-6.935109,-9.692928,0.063923,-1.874239,6.385986,6.333864,-8.804895,5.434722,2.256683,-6.207303,2.259461,-9.833791,9.160528,-6.431741,9.553408,5.715300,-5.131024,5.515502,-8.294390,8.584068,2.867826,-5.366990,5.796179,3.509801,8.501347,6.269365,-8.446412,-7.583873,-1.025386,3.627265,-1.830612,-9.127428,-7.050665,-5.301829,1.113390,4.132893,-7.963569,0.979561,5.819352,-6.745855,-6.319939,8.840931,-1.251607,-0.182524,-0.151916,-0.820941,-3.805482,1.305074,8.065072,-4.754797,5.775380,0.324669,8.434862,-6.646043,9.238987,0.892691,-7.345240,7.900830,9.066246,-9.777532,9.384217,-6.834659,3.960261,8.456271,9.308697,6.144534,7.481787,-1.386042,6.784302,4.426343,2.744823,-4.842319,2.134683,-4.714416,3.902710,-2.449472,-2.766093,2.132927,4.497423,-9.199074,-6.602659,4.975806,-8.142560,-6.967545,-1.688198,2.771680,-7.107635,-8.755257,1.135338,-4.400683,7.350735,2.525223,9.318639,6.364012,7.834824,6.089451,3.765051,5.366251,-0.971097,-5.841301,8.348297,3.664428,0.848928,4.153861,-6.619301,-0.095962,4.521533,3.283027,-5.031095,6.400326,-5.910666,3.257364,7.176736,-7.333721,-1.571885,4.514644,-2.489778,1.463205,-5.839418,-0.450401,5.734679,-3.784398,-5.968368,1.078195,-5.190292,0.641350,-0.739458,-0.762331,3.991940,7.194677,4.164288,-7.268808,0.760921,-8.709388,-2.271604,6.913921,8.783741,-9.539521,8.956829,-7.101417,-0.077204,7.287094,-7.767100,7.988130,-3.890903,9.598802,5.765383,6.426681,0.147323,-5.078184,-3.390478,3.532215,5.371067,1.186526,-8.840591,-8.916214,0.143200,0.773722,6.303617,-2.855065,2.416326,-2.029281,7.816787,-7.321856,3.213493,-6.619597,-0.579774,7.449672,-8.667301,-8.153343,-2.532090,6.487251,-2.178164,9.746040,1.681089,4.829151,4.559506,5.552581,2.709608,1.093423,-1.353050,-1.295209,-7.145186,-7.634031,3.108745,4.455799,5.892569,7.902792,4.990579,-4.977509,-3.410035,7.787697,0.367235,-9.778835,-9.313513,2.332615,-1.356508,6.731754,6.003596,5.205988,5.233418,-7.913720,6.465801,-7.569064,-8.287412,-8.508519,5.615812,-8.242590,-6.998143,6.951591,-5.798306,-9.874842,8.311697,6.809522,0.811655,7.345462,4.066243,-4.707638,3.917125,4.132865,0.503901,6.094696,-2.081720,4.285392,-5.156234,0.116199,4.643772,3.467712,-2.458558,7.187003,1.273325,-5.042263,-8.141493,-8.413289,7.618870,6.663925,0.684275,7.489715,-8.570182,-0.972982,-8.776216,5.293968,2.993704,-9.843618,-6.511969,-2.443317,-2.691781,-5.669527,7.267697,-1.996112,6.515038,3.223957,-6.840994,-2.891678,0.235021,-3.323218,-8.934844,3.668843,-3.729007,4.463818,7.085159,9.053150,-7.186511,-2.851897,-1.343787,7.857288,-5.227606,-8.650096,0.749140,3.341533,8.685141,-4.559522,5.058802,-7.929366,6.938640,-5.117626,5.395156,-6.096202,-4.892225,8.753801,-9.361767,-5.553337,5.289626,9.807881,5.228547,4.962457,-9.104078,-1.691481,8.102180,-1.700160,2.280331,8.490798,-3.300717,-5.310842,-8.821810,9.945244,-0.610669,0.727300,-4.817392,0.998718,6.579337,-6.058681,-7.446924,6.167474,5.998484,2.070039,6.776837,5.411075,-9.310141,-0.155411,2.519762,8.331812,9.044638,2.672780,-1.694427,1.921352,5.214713,7.132258,-0.716847,9.644507,-7.807211,-1.339774,1.848818,4.214167,-8.728665,-6.558956,8.596072,4.461079,-6.325102,-5.743669,4.374999,-4.624721,-3.285051,6.405962,8.792170,-6.302681,3.021456,7.065695,1.100496,-6.806781,-0.800508,6.880349,7.986539,-8.777749,-3.789745,-7.105575,-0.508350,-5.079156,-8.717707,8.235542,8.090163,-9.163588,3.914254,5.974813,-6.568724,-0.090579,4.425197,9.526612,-0.372647,-7.262142,-8.605403,5.616477,-6.674766,8.118023,8.797544,-7.880241,4.360525,7.691733,-6.959400,7.527516,-5.987603,6.455609,2.291636,-4.300565,-2.502322,-9.809617,3.722229,5.595829,-6.542688,7.198481,5.715062,-0.414086,-7.862636,0.805710,-8.238789,5.883344,-8.747042,-8.266713,4.616633,-7.114988,-1.587753,0.959269,-7.868047,9.391998,2.047770,-0.327041,-2.983319,1.514398,-1.306721,8.000442,5.593051,6.119721,1.313641,-5.076834,6.585841,-6.074005,7.936662,1.780900,-4.235143,-8.502582,5.915235,-9.798960,8.111961,-6.638284,2.412786,9.748090,3.200167,-8.837247,-7.583211,6.189531,6.502682,7.678121,5.161711,-5.955876,8.843989,-7.349682,2.209120,-0.463166,-0.013657,-3.537790,-8.561335,2.846021,5.982483,-5.104766,-5.128779,3.547928,5.449441,-0.628933,2.766665,-2.176217,-6.039580,-7.068637,-8.556995,-5.121045,7.208070,-7.033052,-2.625544,0.189607,1.599753,-0.247845,-9.987769,-0.550843,-9.799116,-3.277984,6.122256,1.500223,7.333143,-0.852273,-4.611365,6.472556,8.300683,-8.212947,2.280363,8.214279,0.347427,-6.075905,3.647465,-9.457055,3.781855,-8.543334,6.553016,-1.817145,6.006040,-0.155209,-6.708658,9.527680,6.328491,3.326407,-6.237010,-5.924268,-3.646267,6.215894,7.847444,-2.232261,-8.741436,8.528143,-8.282918,9.030725,-5.833758,0.074702,3.407152,0.093853,-8.217549,1.912280,8.297734,7.492892,-6.498202,-5.033786,-9.721329,-3.471842,8.069949,-0.597986,-6.404702,6.823711,-0.151644,5.096404,9.977678,-4.938023,3.016176,-5.167172,9.852826,7.442986,-2.575667,4.875984,-6.528240,-4.597121,-2.444000,4.729582,-6.593584,4.734425,8.339835,-0.657711,0.490094,1.244087,-0.831881,-6.878576,5.704311,7.238967,0.320677,-5.086550,-8.674510,6.643335,7.403280,5.776146,6.786884,-3.031869,6.715384,5.992574,-4.421119,-3.390079,0.564037,-4.179499,-9.887020,-6.897622,9.038849,2.339734,9.513595,-5.493472,0.495870,-9.074208,-2.692359,7.024530,1.466068,5.419130,1.376552,-0.310519,-7.969752,8.785571,-2.422731,-1.816402,-6.404044,-9.267950,-5.621705,9.433925,-1.434013,-7.341495,-0.218320,6.638670,-4.184918,7.925654,-2.718964,-2.514812,0.983139,7.095738,-5.753567,6.748973,0.762809,-1.568363,-4.750506,0.327743,-5.822525,9.583569,5.338355,-6.755029,6.130916,-8.073745,-0.438989,-3.915596,-5.159013,3.646077,8.976685,-3.922526,-7.067834,-6.221776,-8.110559,-6.786703,3.946479,6.434343,-9.029595,9.021866,-9.158060,5.754344,-7.949582,-3.634025,5.486551,9.414871,-0.347158,5.016032,8.645609,9.188769,7.770499,-3.454414,6.144951,7.114387,6.896798,-9.833313,-7.144884,-8.537439,5.896685,-8.774889,4.913677,-8.719673,8.870891,-2.340367,9.753070,-6.432476,0.984108,-1.808999,-4.113618,-2.436112,-8.327597,6.553040,-4.720038,8.699499,-7.591375,-1.823670,-0.337019,7.136085,-3.789884,-0.224096,4.956100,-1.970300,9.043345,-9.978759,8.527477,4.570897,1.497585,-6.926151,5.334255,9.418316,9.176656,5.544630,-6.428323,4.149140,-4.531386,0.038614,-9.038038,3.312089,-0.615367,-0.929430,-6.681919,7.506849,-3.138810,-9.324483,2.474631,-8.192348,2.090237,-8.793661,-9.045557,3.991209,6.607189,4.587222,-6.786323,7.338884,-4.175419,-7.100510,-4.912464,-8.191419,-3.407341,-2.182940,-0.457894,-4.427271,-3.658686,-4.234288,1.368317,7.930986,-1.221255,-7.221535,1.796479,6.189044,0.430396,4.991110,2.605779,6.358890,-9.264986,6.842190,-1.246281,-5.371834,4.858384,6.143529,-5.881966,5.194204,4.545504,-4.351330,-6.328930,-0.560073,6.237751,5.152116,7.455451,-1.765524,-9.520954,6.092280,-4.706069,0.678134,-8.722191,-7.179824,5.988354,4.587380,1.717495,-6.017138,7.445370,-7.420360,-6.093218,9.146427,-8.960903,2.399816,7.441553,6.655378,-3.685452,3.914873,3.691631,-1.430404,-3.803831,-5.306554,7.251847,4.537873,7.015982,4.474328,9.652189,-9.950021,1.322649,-7.002192,-2.224652,-0.694303,-6.044041,2.488435,1.589510,-6.806770,8.489914,1.050497,6.774406,1.654927,-8.491580,-5.631914,7.495934,5.913684,-3.024242,5.158056,7.864350,-5.976135,-1.635032,-6.241954,7.300263,6.929554,5.507485,7.998990,8.711028,0.329476,8.915717,2.038498,-1.667261,6.177934,-2.092835,2.253215,-5.806739,2.857925,0.998738,-5.719384,-7.471740,1.104285,8.014419,6.455474,4.202070,-3.821872,-3.632644,1.870720,7.635752,-6.092354,-0.243792,9.311365,2.688986,6.916926,-8.613455,3.762825,9.259900,-6.183485,0.584364,4.790460,5.982945,9.416454,5.540368,-2.575771,-0.466631,-6.170300,2.577603,2.833645,-0.181517,6.589924,2.406718,5.933549,-0.906816,5.953820,4.678789,-7.153397,-4.163370,1.704900,7.791112,-8.199042,-9.132601,-2.903808,0.509715,-7.813365,-6.500951,-4.606920,-6.735684,-2.939372,-0.243986,-0.311692,-8.895425,-1.971264,-0.685898,-2.383097,7.630068,0.512019,1.540412,8.933007,-5.537956,-8.750326,-4.296386,-4.534487,-3.500809,2.535314,-2.486610,9.455885,-4.937748,8.857156,8.505392,-8.337521,4.175619,-9.544250,4.079618,1.283338,7.330743,-4.816140,-3.965858,-6.147010,2.524712,1.029716,9.218707,-4.606712,-8.272774,-8.786444,2.713341,6.591020,8.049655,3.832530,6.183772,-8.350689,-7.434926,-9.804940,1.485214,-0.046551,-7.876896,-3.822204,-5.789138,-5.440654,-2.062504,-8.125129,7.023124,-1.494694,4.241917,-1.736123,-2.429092,2.710562,6.493816,-6.785810,-7.816161,-6.801942,-1.621610,-0.384047,9.455796,-1.668388,0.149618,-1.475571,-8.371889,8.700802,-8.682957,-8.672529,-7.403170,-3.987200,-5.240773,-9.981516,9.990826,4.137790,6.963427,-6.572388,-0.431317,2.877827,7.180255,1.465115,-7.796424,5.919592,-1.582397,-1.068796,5.699245,-5.933446,8.585072,-6.212292,7.587401,-7.689644,5.074567,-3.939777,7.222479,0.118987,8.999784,-3.739362,-8.395279,-3.375597,-1.152683,9.613916,9.124055,3.532745,3.059486,2.489724,8.469255,7.770203,-0.526592,9.922295,8.989164,-4.975143,0.584906,5.751243,-8.543004,-7.710330,-2.424174,-0.743569,5.602085,-9.016939,6.249366,-6.278988,0.941234,4.775235,6.602863,-1.966398,-0.988525,8.670736,5.833645,4.530550,-6.659345,-0.046158,6.003818,8.420099,-7.035929,6.606556,7.925594,8.169077,-6.863507,8.560650,5.348099,-0.845824,-3.325679,8.035797,-3.253724,-1.678141,-7.075962,3.768096,7.794715,-0.078789,-0.999990,-2.818026,1.558612,8.035606,-5.369175,8.824000,-0.030898,4.366014,0.402758,-6.545614,2.333311,8.258753,-1.629197,-1.545572,6.467542,6.649656,-8.835593,3.110248,0.644009,5.805149,9.304765,9.921312,8.621223,2.589690,4.492158,-4.964023,-6.626773,-6.575709,5.467136,-4.650670,-4.748272,-7.371759,5.137802,-5.233214,-5.151441,2.235152,7.733555,2.242178,1.440929,3.997548,5.015620,-7.053762,8.016344,-1.852716,5.229794,3.554001,-8.775059,-6.078866,-7.967641,7.509606,9.959436,-3.570037,1.380990,8.206445,-8.519510,-8.122358,-1.106866,4.423173,1.875054,-4.393857,1.822253,-5.116173,-5.071819,5.859337,-8.870803,6.439641,1.580128,-5.074377,-6.630670,-9.192514,-9.721463,-1.876077,2.263710,6.655414,2.667550,9.589808,5.240118,-4.291843,-6.245886,-4.250227,-4.428469,-0.765523,-2.528424,8.019309,-7.944794,9.963283,-1.245424,-8.196488,-8.189514,-3.866516,4.684434,-0.343127,-7.919793,-4.228662,-5.252472,1.101899,8.213857,2.407784,-6.489365,-7.334862,-1.697930,0.623194,8.300709,-2.944839,7.623546,9.198708,-4.674749,-8.428930,-5.420924,4.510316,0.458548,-7.878205,3.736271,-5.108253,-6.185047,-6.438167,5.614476,1.028897,5.707614,-6.894139,-8.409888,-8.155393,6.056747,8.317251,1.809506,-3.020108,9.028354,1.797173,-3.879340,-7.502319,-5.918920,5.350894,6.448871,-3.778113,-0.868086,9.513527,-2.400728,6.914533,-5.686978,-2.787081,-1.483339,8.017448,6.154093,-4.075062,-7.920219,-4.591227,9.258924,-8.220696,-0.714486,-2.449592,7.392096,9.490975,4.653575,6.770094,-5.497307,5.673478,6.342936,-8.456131,-8.210360,-4.290755,-0.222338,7.678141,8.698171,-0.555141,1.132303,-4.849101,-8.509664,-1.687882,4.380585,-9.084356,0.749144,-1.804165,-3.368421,5.152178,3.319628,7.802110,-5.031403,2.001017,1.903481,7.381797,-6.253455,0.038485,-5.587602,-6.392691,-9.041811,8.622161,2.804739,-6.524779,-3.283162,-2.593333,5.599459,4.073681,-4.122537,5.601966,-6.492147,-1.728160,4.662463,-5.623935,-6.395878,6.909119,6.618365,-9.232036,-7.360916,-2.015351,0.136322,-5.317156,-6.954508,-7.306121,-3.918620,-6.877880,1.225259,-2.959948,4.914939,-6.086553,0.119599,-9.435403,-1.959441,4.633792,6.667103,9.851849,-2.440197,1.053545,-1.273048,-7.726249,-0.418076,0.235637,3.379379,-4.956835,-1.272758,-0.667824,-2.886638,-7.452667,-5.016676,3.422058,1.787612,-6.543882,-0.390967,2.792046,8.960695,7.273133,-7.428859,4.674395,-4.765823,-7.953223,-2.756692,6.933289,5.105216,1.626560,7.012835,4.486969,-3.932736,9.914918,-5.367416,7.021767,-2.725069,6.003430,0.931026,-6.528186,-1.122073,5.321230,-3.079539,1.351599,-8.501985,2.292977,2.266683,5.212877,-4.750482,-7.759867,1.720525,-3.084956,-8.097969,-1.416277,6.029810,-0.941672,-4.336883,-5.920769,-8.829397,-1.590296,4.820262,-4.295335,7.772977,-5.854072,-7.041304,-3.436332,-4.923994,4.116982,-1.304311,-5.475750,3.591701,6.659912,-8.756328,-8.065000,2.725888,-2.164102,-8.820956,1.951541,-9.826560,8.715852,-6.337678,-9.503371,-5.297711,1.027362,9.449048,-0.679496,-6.875608,-3.569002,-1.752777,1.065685,-2.361782,-1.971369,4.243456,-0.226024,3.608225,-5.225576,5.857025,-3.021305,4.375843,-4.460473,3.835832,9.630699,-3.722296,9.137746,-5.059751,-6.942680,-8.033388,4.245804,-0.708674,1.683602,3.955403,1.464995,-0.798068,-0.131439,6.025099,-9.741225,-9.940357,6.881088,-1.669062,8.630265,2.201311,4.899753,-1.896058,4.193039,-4.447452,-4.957095,6.364289,-3.573604,5.902935,0.264212,8.057337,9.049021,1.344414,-8.534461,4.937708,-3.659634,1.886144,-6.774674,-7.979504,-9.880611,-0.563592,-4.588109,-1.279818,0.310652,4.243704,-7.043183,1.948614,-6.324471,-2.368637,-6.531703,-6.792578,6.158219,-2.794491,2.917223,9.769536,4.728531,-3.957703,4.145829,-7.607637,-1.596970,2.852136,-9.836314,6.643544,4.527529,3.061108,9.911580,-6.374416,6.625666,4.293825,8.964449,-7.407376,-7.164898,-0.782369,7.201578,2.007533,0.721175,-4.294155,7.418828,-7.070056,-4.090408,-8.655553,-9.020172,-9.203940,5.552430,-1.842056,-9.675621,7.554030,-0.377353,2.381467,-8.508026,1.862324,2.585795,2.118094,2.322775,-5.388905,9.952403,-9.528046,5.974514,6.280067,-1.877367,-8.553532,-6.204615,5.210439,2.254946,-0.845054,1.180862,0.518943,9.922974,5.090651,2.789014,-5.431946,-8.685601,-3.602813,1.142057,-0.877703,0.047219,0.004007,-2.619375,-6.890656,1.774620,4.445455,1.980411,4.396055,6.565280,0.918914,-5.593751,0.371591,-2.674949,1.026559,0.880093,9.083123,-5.741292,-6.574180,-0.645661,-9.630321,2.824233,-8.002043,3.480497,-8.802319,9.568245,0.916649,7.163102,-6.801421,-4.287370,-6.023544,-3.656919,-2.960027,-7.912315,5.893696,-1.539368,-6.343059,-6.491169,-9.942008,-5.265842,-0.705836,-4.475356,-0.779654,1.937802,-9.625612,-0.194506,2.283759,-4.640730,5.245309,4.374400,8.506525,-1.691751,2.207890,1.694690,-4.534878,-0.555430,4.322258,-1.747546,3.098534,-5.926034,8.147104,-6.564612,3.932327,8.921652,1.269048,-2.978005,-9.810786,-4.485180,8.155122,2.010280,9.090477,-8.754680,-4.885499,-3.603209,-4.920363,0.750239,3.902628,9.360935,4.103776,0.843078,9.760312,8.751175,7.442923,6.877505,0.164777,-7.393509,6.253541,9.532596,-1.667955,6.627774,4.892443,-9.078350,-2.989287,1.693871,-1.708967,-0.360679,-8.895283,4.489341,9.786318,-8.809290,0.276173,0.103442,-3.622809,0.911870,0.073155,4.057576,4.546560,6.350631,3.327300,1.279249,-6.445633,7.361674,-8.223359,-0.361161,-7.594439,-0.098138,1.054019,-0.164834,9.144755,-6.243779,-5.745620,9.765742,-5.565751,9.335317,6.634655,1.777923,-3.955784,4.961746,-1.945800,-2.359380,-0.839177,-5.345219,-3.972654,6.196226,-4.836862,-9.707433,-3.454571,9.438737,2.499626,-7.061844,9.073610,-2.363385,7.670960,-2.292615,6.681818,-5.288247,-7.334228,0.661877,9.969649,-2.949507,0.595977,-2.925835,-6.688328,-8.899909,-3.937518,-6.963391,-4.595178,5.582399,-5.161704,4.707853,-2.985956,-8.856198,4.475970,0.278367,-4.859212,-8.017992,3.951632,1.496512,-8.642568,3.421493,1.113041,4.494524,-0.782953,5.309686,-9.902348,-7.801280,-4.813608,0.656667,-8.323959,-9.293274,-9.169775,-4.865249,2.873248,7.768275,8.683858,-4.452294,3.249893,4.217847,-8.989818,-7.558171,7.306759,9.087735,6.808576,2.374855,5.615787,6.644772,1.460869,9.122796,5.975825,-3.427135,8.503243,7.213425,-0.829547,-3.660164,1.279744,-6.483658,0.906282,-2.645220,-6.524671,6.390891,0.766158,-8.380859,-7.221503,0.470079,-5.849083,4.343916,-6.097056,-8.038391,8.546304,3.009122,-4.204081,3.860606,4.162021,-9.146467,-8.615404,-7.039242,-6.525068,-4.116037,-4.835307,1.082720,1.524633,3.952358,8.537384,6.781801,-0.528383,-2.431335,-3.881935,1.853495,6.912266,7.661864,9.320755,-0.982006,-0.577055,-0.660978,-4.906317,-7.781890,-4.527333,-6.047853,5.594410,-5.705259,-3.581158,-9.226394,0.920753,8.989184,-6.367347,-8.715092,-3.229940,3.018760,0.959416,9.054669,8.677538,9.272453,3.047464,-7.275786,6.471746,1.297020,2.384174,-1.947031,4.157497,0.589063,4.300643,0.202030,-1.375284,-1.054761,-3.674144,-9.686348,4.549862,-3.089271,7.582191,-6.642833,8.552169,-7.417560,7.697513,3.289133,-9.517024,-5.804484,-3.048194,9.080102,6.654479,-3.745205,-2.608821,6.812949,4.345186,-1.519054,-3.033244,9.902065,-9.317634,-1.373574,4.261646,-3.566933,3.503242,4.864298,-5.920337,-9.808025,-9.144149,-1.068365,3.568483,8.207461,1.207550,7.956881,-3.083622,1.161601,8.668243,-0.886727,-3.826813,-2.464848,-3.747399,2.155602,8.237177,-9.226312,8.466997,-7.058550,-4.006999,6.291956,3.282700,-4.093497,4.783865,9.603224,9.621343,0.328961,-7.302042,4.242988,8.960249,-9.952843,8.634803,6.715717,4.414001,7.808992,2.379869,7.936624,-9.108753,-4.005684,1.723494,-7.934110,6.045352,-4.588139,8.866205,-1.168185,7.067730,4.666743,8.715425,3.270939,-2.784579,3.446232,8.573486,6.128130,-9.291302,7.864537,4.234986,-3.233590,-5.955663,-9.338743,2.755524,-6.159374,2.626364,5.593176,-7.135030,9.675746,5.242608,-6.166632,9.249205,-6.634084,5.130701,-0.724192,4.085892,-7.882840,9.824989,-8.921304,8.475553,6.489120,-1.151441,-1.786320,5.473588,-2.295968,-3.583700,2.496819,-0.173016,6.721873,-1.613137,-1.074275,-6.443727,7.093807,4.659103,-5.836408,-2.959378,-7.196633,-3.847518,-0.001327,-0.564686,3.886516,5.611648,6.887670,-0.056883,-3.398543,-6.636632,6.368750,9.198959,-8.262272,-4.177584,2.222888,2.848615,2.374282,-6.041560,2.307130,-4.381639,9.848134,-6.830823,8.304290,8.946261,3.950311,-2.719917,1.029980,0.552430,6.091901,-2.783438,-7.145745,-9.553643,-3.759854,3.188706,1.259855,-7.721102,-1.712429,2.391604,0.074359,1.132080,-3.932974,8.089114,3.169736,-2.571994,-6.014065,0.723712,-7.055808,4.952755,3.501999,-1.347383,-9.226843,6.528780,2.622611,3.644491,-9.464196,2.917720,-5.639403,-3.410059,1.130797,-4.635012,8.539072,6.480719,4.461360,-6.041225,4.455642,-4.156939,8.834534,-2.095034,-4.385187,-1.132596,-5.154987,-5.349346,-3.105450,-5.645890,9.630334,-8.506395,0.767004,-2.031499,-9.979756,1.025489,8.904153,5.230337,3.252578,-1.725827,0.438655,-9.581616,-3.697581,7.640826,2.537366,1.416815,-5.326591,-5.435637,7.530086,1.461497,1.549617,1.649076,-9.696186,-5.881762,6.733220,9.859118,6.978188,-1.848183,-7.770741,-6.462142,-5.442042,-9.993056,3.216411,-8.311721,5.253661,-8.382718,-8.914485,-0.579731,2.046114,-8.192175,2.597718,0.185570,-4.704290,-6.259330,2.993862,-1.421115,-8.605195,7.101791,5.880914,-0.313680,8.053399,-3.015260,7.708899,-3.169418,0.969145,8.541288,-6.698200,7.957432,-2.182985,-7.529179,-4.640430,4.532145,5.683584,6.027979,-4.284146,-7.349775,-6.066823,3.494882,6.166446,-2.758233,9.047624,9.181415,2.194067,-1.293186,-0.879643,3.798517,8.029306,-3.792907,4.800543,-0.249133,8.233889,0.015067,4.448487,5.238298,-4.016888,0.186136,2.830739,-1.565650,1.625986,2.959788,9.293125,-6.859338,3.335752,2.474470,-7.286699,6.308027,-9.896144,-6.456035,5.664833,-6.091884,8.018355,8.010718,-5.765763,9.305047,-3.883117,-2.487890,-6.466753,0.384378,8.534002,-2.930155,-0.302221,7.875058,1.064687,-3.745170,-6.633324,-0.964167,-5.570960,-0.185274,6.895662,-2.480664,-4.557454,4.420765,2.273792,6.956543,-1.071173,6.617379,4.050446,1.372779,-5.031065,8.585446,5.048011,-4.112325,-7.882842,-9.258143,6.616163,9.886465,0.379081,-7.704706,0.621354,9.819817,7.704892,-0.534502,-4.058874,1.047758,1.684470,6.884660,7.151539,-0.729586,-9.895484,3.588547,4.969821,-3.732731,-6.695900,-6.565709,-8.627966,5.828867,-2.917160,-3.887577,9.855763,0.726240,-3.108965,4.329456,-0.238617,4.987417,2.264226,-3.204302,-8.788180,0.744243,8.936835,-3.652058,-0.016712,-9.720923,-4.272250,0.883906,-3.571262,-8.433724,9.107690,-4.281449,-5.819292,-3.362988,8.982350,-2.277973,4.356038,-1.637013,4.200089,-9.636820,-8.066215,-1.544079,8.272403,-1.609343,-0.982327,9.843957,5.038571,-2.148991,9.582885,8.084520,3.373111,-6.648240,6.443692,-1.457762,-6.064351,-7.404205,1.761147,3.841330,-1.224271,-5.727386,-1.145892,-9.992527,-4.195704,5.589963,-1.375673,-2.921467,8.800986,-0.095973,0.356746,0.193755,-0.657050,-4.331916,2.126154,-3.418985,4.076013,-0.762369,-4.047991,7.532107,4.590943,6.571570,4.044398,-3.812492,-0.306586,-1.000467,7.401783,5.228506,9.961665,3.723620,8.474847,3.753526,-4.683669,9.465455,-1.640421,2.418528,9.114908,3.255680,-5.758130,2.989119,5.431347,-9.513058,-7.451850,-5.120375,2.202610,-4.205378,1.223768,-3.528461,4.846915,8.255794,-5.755914,-6.911320,7.565482,3.511038,4.305954,-2.776290,-6.094625,8.993410,5.440466,-4.771817,4.967816,7.682567,-8.936513,-0.853196,5.716639,-0.626792,1.689457,-6.364782,-0.742185,-2.613328,-5.393057,-2.322535,-0.162183,5.488306,9.386495,-1.865799,-9.495707,-1.425435,4.200265,4.467946,-1.864697,5.296285,-4.832343,-9.420630,1.144440,-0.915917,7.866276,-4.442241,-5.706116,4.474000,9.649095,-7.373019,-0.414580,8.143321,0.473036,-5.677221,-6.665528,2.993305,3.212700,1.842579,7.607029,9.176735,3.969414,-4.963465,8.798620,5.483288,6.911653,0.640639,-4.890343,-3.762208,2.904237,2.150362,-4.519707,-8.967383,-7.828756,-1.119949,5.340819,4.584897,8.116768,-3.685535,4.132381,4.706298,5.644344,-6.413108,3.026057,8.427645,-9.126428,-4.064209,-5.745269,-9.961396,4.706149,-3.086180,-4.496876,9.262142,3.678843,4.848177,6.462588,6.228040,6.372767,9.562549,-2.738018,9.640455,4.040256,9.859542,-8.280970,3.992576,-4.849195,-1.236838,1.851771,-2.615337,2.088478,4.157396,9.524833,0.411214,2.381281,1.241319,4.569532,-2.445556,1.467014,-8.482202,2.842636,2.412483,5.741765,5.537347,5.977675,4.063190,2.735754,6.136005,-0.265647,5.260171,8.733376,7.666713,6.796001,-6.233418,-7.776828,-6.092656,-2.305272,0.776531,4.314728,-6.974443,2.885527,5.102854,-5.634501,1.718378,0.513403,-1.655086,6.676270,4.764541,9.354340,0.380321,0.782669,-1.095445,4.741013,0.712523,-7.092673,8.884432,-1.882624,-8.891976,-7.366345,6.763875,-6.646264,-6.791215,2.412329,-8.347798,4.300894,-6.565762,6.941005,-7.409517,6.798022,6.748279,7.176217,9.623613,1.653252,5.002313,1.497093,5.321087,-4.336364,1.776729,9.530029,3.244861,-4.095431,4.330712,-2.397456,-4.428264,-0.049143,3.485169,3.630254,7.145789,-5.562994,-0.345930,5.341564,1.402889,9.602328,2.298949,-4.117136,-1.590765,9.666169,-9.754541,5.044828,2.904094,-3.414794,-3.942356,0.322030,-9.670940,-7.661008,8.700505,-9.789328,8.284230,1.190106,-5.832505,8.559358,-4.351996,0.763518,-7.284307,-6.170908,-6.514828,-3.571889,-6.325105,-6.858748,8.404564,7.981768,-8.558800,7.320044,4.152098,-9.893311,-2.305280,-6.630878,-7.979011,9.643941,7.315017,-3.634871,-7.987958,-3.191650,-0.317167,5.519358,2.388660,-2.821686,-3.097142,1.158890,6.776246,-7.595924,-8.404936,-0.501775,-1.341862,2.316449,3.966937,1.919771,5.309246,-6.668767,-2.461493,0.701369,-4.590137,8.651497,-0.826613,9.455952,-6.830597,3.908126,-9.844765,-2.701202,-7.037954,-3.519003,5.120608,1.605360,6.896776,1.301728,-8.930621,8.930724,-2.596074,0.416505,-0.919128,-6.496245,-1.058588,0.092145,-1.351921,6.549356,8.521218,-8.102054,0.981539,5.077242,-2.603103,-5.772983,-2.145313,5.172148,-7.609379,7.280916,6.149033,-1.795620,0.796574,0.789723,5.240864,-7.252774,-3.015868,6.827400,3.495637,2.399470,5.554041,-2.535301,0.582624,1.321272,-7.865198,-7.005324,-0.962739,-9.431191,-8.095489,6.496156,-1.281185,7.850103,7.155504,5.783997,8.751780,-9.629516,-5.844130,-4.167602,-8.685240,-9.664763,-0.567692,7.299291,4.729028,3.189881,9.100665,4.375960,-6.322935,-8.386196,8.792105,-0.947588,-9.179388,-3.143797,7.859027,0.896452,-6.096644,7.639228,-9.930713,4.831597,-2.132143,-3.125013,-3.860123,4.886364,-8.316712,-8.718824,0.488838,-4.460146,9.380131,9.609957,-1.690451,-4.399936,-3.897529,4.897888,-1.640759,-6.890441,9.856837,-3.501596,-4.634291,6.166869,-4.292358,-4.555935,-9.342497,5.805323,9.268070,3.307021,8.300190,-9.924617,0.581712,6.943816,8.323297,-3.720296,-9.389985,-3.060833,-2.971441,7.461124,4.758973,3.144055,-0.897747,4.452913,6.799313,7.776804,-4.790328,-0.235858,-0.731684,-4.258181,0.007488,-7.784636,4.872814,-3.723640,-4.823319,-8.456097,9.476371,-5.167460,6.405664,-6.135887,-7.110947,6.608510,7.140732,-2.651785,3.886915,5.547036,7.977653,-0.062245,-0.881328,-6.285309,-0.972711,-9.693742,-2.029841,-8.190043,-0.664864,-4.649600,-8.187965,-2.240048,0.183773,4.136877,4.534974,3.451974,7.426801,9.794230,-9.653760,-2.904589,6.932599,7.968609,1.284966,6.019347,-8.558726,-3.813909,2.233939,-3.789064,8.382472,-8.800066,9.448690,9.542646,2.556582,-6.767371,6.106590,7.062004,-0.382674,-4.750888,-7.005075,8.353524,-7.674986,6.938203,-5.423202,-9.499170,-2.184955,-5.313580,5.091519,-5.983234,6.673267,-7.091740,9.642143,2.597341,-2.664663,-4.224611,0.196760,2.768568,6.973787,5.144536,8.122842,-8.556599,-5.713822,8.775699,-0.799447,8.192000,-3.810625,-9.760846,2.339894,7.495385,-6.827309,-3.143265,-1.642719,1.903326,-4.377708,6.912401,-0.348604,7.516630,5.718247,-9.013698,-5.278158,7.390825,-1.978073,8.544724,1.859078,4.328672,-1.519086,4.159682,-6.706808,-3.953450,3.987557,-6.772460,1.539820,0.318111,-1.893394,5.335749,3.642178,7.095404,-3.840595,2.518233,-8.494075,9.755284,-5.207340,6.577454,8.299984,0.761452,0.561201,5.532486,-9.930272,4.634375,-9.769746,7.728510,9.500956,3.518860,1.527542,7.948650,-7.968898,-3.194092,3.112753,7.310286,-4.166333,-0.644076,-9.951333,-4.696120,-9.056895,9.989160,-1.992415,-3.469185,7.473321,-7.361702,-6.593384,-0.501124,-3.533740,2.365515,-1.326974,3.255842,6.174521,7.559276,0.191157,-0.628538,1.992162,-3.366513,0.657765,-9.634140,4.572027,4.687793,-4.996669,-3.552171,3.127904,9.814304,-5.640087,-5.636639,-0.307052,4.329916,2.786560,2.220319,5.388860,9.039932,-4.071596,9.195573,-4.074348,1.295305,7.787446,8.244270,1.511783,-3.560694,3.205819,4.585349,-6.847574,9.518361,4.143366,7.534584,2.104815,6.359622,-1.213364,5.533692,5.540752,8.917853,-3.873515,7.908194,9.098060,5.789561,-7.065989,-4.312735,7.353195,5.879321,-9.066569,8.109438,5.354023,4.128441,3.992668,-1.422953,9.289752,1.084395,-9.678148,5.894050,3.966253,0.098621,-6.391093,-8.699022,1.022486,-9.449286,-4.348659,5.490438,-9.177703,9.690374,0.924449,-0.053323,-6.472641,-6.741022,9.875721,-8.034973,-9.172866,-5.535551,-0.732008,-4.204080,-5.470556,0.079656,-1.951084,-7.393626,-4.147838,3.876265,5.676474,-0.857052,1.401545,0.784495,9.509314,9.990714,2.696103,-0.590887,1.324002,4.806221,9.719670,-2.648770,-3.531310,-0.847101,4.793531,-2.155542,1.256099,-8.769114,-8.391401,2.176877,1.708194,8.762477,6.839010,-0.981088,7.040113,-5.637134,5.708068,-1.946164,-0.450977,-4.436681,-2.001417,-3.996214,7.155413,7.502752,-3.169697,8.503678,7.280405,-7.390193,-3.011711,7.976918,5.130094,-5.523409,4.947668,-9.346401,1.352417,2.927142,7.802384,-7.531652,-2.141607,-3.013266,-7.481244,-5.195147,7.890151,-7.321651,-6.988605,9.898937,-4.743552,-3.574582,-6.514756,7.572657,3.544004,-0.408176,-5.821888,7.194194,-7.604012,-6.814187,-2.658852,-3.026799,8.129924,1.003970,2.533898,0.698490,2.929779,2.563861,-8.131352,3.330855,1.643083,4.651022,-2.535426,-8.491909,-3.518726,-9.378081,5.285119,-1.309520,0.616175,-8.345958,-9.551297,-0.762327,9.303951,-3.636805,-4.074711,7.747930,6.849702,-1.957842,-1.729166,-1.155169,1.416558,8.194862,9.331792,2.267851,5.480474,0.505448,-0.051401,1.782580,7.297197,8.823885,-1.138948,5.216091,9.307627,6.867594,-6.987811,2.092017,-9.726343,7.326863,-6.058208,8.822880,-1.977172,-0.145397,-0.234559,6.633114,4.556073,-8.993380,9.989798,4.241336,1.468811,-0.879997,-7.549825,4.061170,-3.320211,-6.476713,9.435355,7.485550,7.718210,-4.727243,8.492278,5.190917,6.315715,-0.555987,-5.271820,4.664262,8.150969,7.745970,7.866415,-7.218255,1.268890,1.032467,-8.001844,5.157104,-4.629282,-1.868849,0.956396,-6.852092,9.151115,6.775983,-0.080277,6.159290,5.210702,1.468698,1.583064,-0.326894,-7.524894,9.668944,-4.344595,-4.223937,6.287368,9.449932,5.296209,9.088447,-5.219849,-9.079957,7.986325,-5.742948,-0.155804,-1.441396,-1.292416,0.260349,-0.610686,9.321348,6.859222,6.626335,-1.410182,6.248140,-3.992809,-3.399287,7.596437,3.300172,-8.456110,6.529164,6.146923,-6.368556,8.155867,-1.537397,1.160383,-3.318851,-7.281909,0.947860,-5.153331,-1.469655,6.021646,-3.438104,3.369896,8.294295,2.293549,-4.607742,-5.197966,-4.835790,-5.214752,3.691463,7.292238,-6.724300,9.344544,-5.451968,-5.277077,-6.295577,-2.455331,4.474303,-5.831001,7.971832,1.732303,-4.781407,1.553471,8.795135,-5.057096,2.020882,5.316537,3.596285,5.479575,-8.017046,-4.890681,8.768835,8.635506,-0.159065,9.560769,-7.476878,6.098050,4.956565,5.663470,0.901273,6.192554,5.412793,-2.583776,-0.034163,0.880315,-2.935069,9.806480,-1.584426,-5.889315,4.338938,-6.916284,-7.945875,-6.210549,-8.062174,8.217186,7.551371,-2.812878,2.552182,3.660389,-3.302400,-2.433417,-1.388115,-4.720708,0.938904,2.226717,2.960484,-2.844383,-3.786341,8.564936,-7.393615,-1.757755,6.745700,3.317110,8.000165,-6.710598,4.626695,-4.976414,5.390497,-8.393861,9.326577,9.414048,4.992622,1.460814,-5.273344,3.472967,1.111807,9.443397,-8.922904,3.439887,3.212008,-1.600154,-6.767638,6.329905,4.528433,-6.065193,8.920562,1.260925,9.919964,-5.684820,8.673428,5.749076,3.244812,-5.072267,4.381194,-5.045287,7.422990,0.700151,7.505265,4.819373,-1.918665,-4.091000,9.050553,-9.890303,-8.032351,9.511783,-8.645532,-2.367676,5.860610,-8.590958,-2.243129,1.904975,4.931569,1.578310,2.511646,2.207219,8.130829,-3.100200,-0.298920,9.634296,9.408124,-7.663540,8.680405,-6.473984,3.710854,9.896292,4.367833,-1.735817,5.169085,8.885548,-4.324485,-7.235823,-2.483390,8.418876,-1.226685,5.225633,2.133279,8.947445,-9.438601,5.347549,-6.658284,6.666496,4.751391,-9.795780,-4.528266,-9.031491,5.299359,-1.809269,7.285323,-3.564656,-4.269446,0.772585,9.788937,1.468037,-5.219424,-0.826993,9.926036,-4.325273,4.413449,-9.789786,5.238250,-4.652794,6.227821,-4.689916,-6.396830,-1.500248,5.380586,-2.550752,5.551841,-0.019349,-2.365381,-5.961106,7.722507,7.899888,-2.770519,-5.393183,-6.839922,-7.099187,1.792597,-5.508415,7.122747,-9.387945,-7.962199,8.266591,-2.092733,-6.803135,-2.303529,3.402233,7.525606,-9.865871,-5.486280,6.312087,-2.050779,-6.127344,8.418566,7.724050,-1.725568,3.667078,4.959247,-1.369089,-9.452584,-4.239087,7.612442,-4.496652,-3.572769,-1.058622,6.945911,6.866400,5.770075,7.209904,-6.714493,8.506649,9.745597,-4.594737,-0.681757,-7.521175,9.541859,2.628674,-2.641024,7.474292,2.266414,5.200576,-4.989364,-7.683057,5.107097,-1.654324,-5.578013,-6.695165,-1.339775,-5.577040,8.424762,5.952782,-3.102558,0.381383,3.821675,9.791784,2.582691,4.329546,-1.219641,6.480281,-2.380236,3.285330,-3.661219,-4.154421,-7.108194,9.881681,2.907897,-9.776927,4.197863,9.202839,8.745385,3.022162,8.056924,-5.709452,-7.933334,7.316444,6.081859,-4.093471,-9.213482,-3.180244,1.934231,-2.570400,-0.121547,-8.573700,2.694605,-6.449989,7.244173,9.075581,1.211476,-1.581072,7.628853,-2.010544,-4.619809,-4.124933,3.515513,-6.196736,-4.953195,2.141164,9.254329,3.818680,4.559085,3.818457,1.351620,-0.071303,-0.295297,5.385494,-9.552129,-4.786867,-2.271220,-9.056693,2.778661,-4.297768,7.825459,8.599984,-2.185201,6.953759,-6.691687,-6.352153,1.172996,-3.422323,8.493836,-0.214132,7.330710,-6.813788,0.165398,8.504901,0.378205,6.774408,-3.802948,-5.361850,7.102964,-1.506420,-3.662611,2.790305,7.187422,-9.802649,6.744458,6.655660,4.290905,-1.312148,-9.145529,-8.192459,-7.261694,-7.326778,-7.993520,4.768711,0.150745,4.604737,-2.681497,5.383599,0.471512,-1.214544,-3.020425,0.921445,1.696578,4.844332,-5.103735,-4.378356,7.889680,5.346537,6.739085,4.244255,-0.170271,-1.124064,7.250328,9.213274,7.003570,-6.945879,3.030356,-5.846156,5.898626,-5.106925,8.736894,-0.649661,5.004180,-5.385189,-1.154355,7.235571,-3.079820,6.084429,-7.217180,-9.868155,-5.280138,6.162827,6.253917,8.949270,1.682248,-0.416732,-2.178757,3.222888,-5.435824,-9.443116,3.111594,2.044897,6.707892,-9.324282,9.998577,-7.118739,5.928856,9.045214,1.745100,7.347092,-1.522849,4.227189,1.379623,8.635367,-0.500804,-5.295981,7.138448,2.871700,0.020781,-8.799118,5.770393,-6.568430,9.903692,8.446099,-5.232535,5.667429,-3.817222,6.262921,-1.728119,4.145881,-4.760770,-8.755224,4.612563,4.034574,3.409370,-3.612996,-2.816519,3.465723,-5.065253,-1.285028,-3.973891,-1.520560,-1.691964,-6.877415,-8.427691,5.878960,1.637413,-1.989491,9.884890,7.574865,-3.368197,5.065098,4.788588,-8.260469,3.993025,-3.085485,-7.940622,-4.835600,5.022210,7.032276,-3.325275,-0.373067,8.152365,0.208462,-6.278516,0.492282,-8.794601,2.496897,-5.805020,3.514976,-2.919760,0.847018,-6.301334,1.252691,-2.007527,6.955606,3.143607,-4.836423,2.315908,-7.115911,2.320770,-1.518711,-0.135248,4.083824,5.352474,5.036345,-0.220534,-0.519783,-5.622335,-3.385700,8.202482,-9.540181,-6.855486,0.542327,-3.403439,7.257855,8.722100,3.834407,-3.337309,-0.721950,7.647254,0.611908,-5.509069,2.245229,-3.673408,4.924672,1.583523,-4.784283,2.332327,6.797358,9.222502,7.048656,-6.946012,5.215524,1.264905,-4.101913,5.289133,-1.766552,-7.544143,-0.439536,-8.070454,-9.288153,4.597572,1.346020,-3.091650,-1.394977,4.790908,-0.011052,-5.728450,-4.700920,-3.570921,2.656225,7.766332,3.999237,2.282312,-8.298331,-5.347752,4.637461,4.973768,-6.485116,-0.868777,-2.159067,-1.619842,0.657138,-1.496301,-3.473202,0.158787,-8.687887,5.768599,-5.418846,3.901563,-8.163934,0.749119,-3.491322,-5.008355,-1.475826,6.375997,4.103417,6.357264,3.879598,-2.962368,-1.098803,9.896608,-9.023846,1.916187,8.346289,6.079461,-9.891719,7.141304,-6.436943,8.617841,-6.774561,9.630142,-5.953266,4.089740,-0.135509,6.836263,7.258726,5.082157,2.105124,-5.043061,8.493524,5.851245,-8.556531,-5.985012,-2.029285,5.599072,3.276951,-7.421442,9.955838,4.617863,-1.143140,9.124746,6.670183,0.016335,7.014828,3.638833,-6.726167,-8.957401,5.462881,4.209841,-9.747886,5.799276,9.936422,2.757440,4.922690,-0.172569,0.863708,8.623899,-4.019041,5.426193,-5.111806,-8.165491,0.708443,3.686669,-2.731679,4.018458,5.483960,-5.266208,-8.733200,4.634939,-8.060856,6.363612,7.428658,-1.488363,-3.401841,2.369063,-8.387106,8.351661,-8.380782,-7.669832,1.602930,7.794779,-6.827464,2.683785,8.046648,-8.904289,-1.647248,4.325312,-7.868560,2.085883,-6.514886,2.358403,-4.000688,-8.188040,1.721682,8.772596,-1.833846,2.119709,-6.277065,-6.647357,-4.870756,9.585682,-2.093981,-8.846647,-5.702971,5.417158,8.427904,6.249223,1.392472,-6.057538,7.635953,7.969963,4.178092,-6.371680,0.134336,0.269745,-3.324960,-0.018963,-6.076822,7.208649,-7.631723,2.851534,-8.700717,-0.590874,-1.186914,-1.893066,-6.047094,-7.864602,3.131602,-7.567431,4.537790,-6.304225,-6.867800,-0.705355,9.357867,-3.963028,8.917635,3.069410,-9.146055,1.576482,8.637744,-4.905559,-3.468616,9.327135,-0.663067,-5.912330,5.576289,0.698417,-1.493299,-0.984526,8.486104,3.012601,-7.644615,-4.420389,-7.001012,-3.747663,-9.593696,-0.638000,6.693594,-1.552596,2.879873,3.540854,2.126330,-4.273337,-7.064148,6.944340,0.450959,-3.236905,-1.730823,9.791128,8.268941,-8.750865,-5.847299,-0.622800,-9.363531,4.306819,0.421765,-8.189529,9.533735,-0.068378,-1.411634,-7.210908,0.882205,1.520653,5.790203,-1.816410,-2.694445,-4.651390,2.925460,-4.840897,3.575845,1.793660,-5.680135,2.521942,7.288513,-6.775229,-8.752413,3.396643,9.652935,5.527939,9.211035,9.590610,-2.160969], dtype = "float32")#candidate|3782|(7800,)|const|float32
call_3780 = relay.TupleGetItem(func_3503_call(relay.reshape(var_3781.astype('float64'), [660,]), relay.reshape(const_3782.astype('float32'), [780, 10]), ), 0)
call_3783 = relay.TupleGetItem(func_3506_call(relay.reshape(var_3781.astype('float64'), [660,]), relay.reshape(const_3782.astype('float32'), [780, 10]), ), 0)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_3784 = relay.TupleGetItem(func_856_call(), 0)
call_3785 = relay.TupleGetItem(func_858_call(), 0)
const_3786 = relay.const([0.604472,-2.203000,-0.781311,6.984779,-2.994523,2.773683,3.943845,-5.762360,4.969097,3.658448,2.879574,-6.007282,-3.308175,2.476643,9.566982,8.383486,2.575408,-3.796113,3.959789,-3.660317,-4.880319,-2.544859,-8.127458,-0.520423,-1.250134,-5.629608,-7.993560,0.977910,6.797312,1.933414,-9.752681,2.129764,6.490972,6.971285,-7.040611,-3.134830,9.416272,-9.654699,3.331979,1.680365,-4.776812,5.017917,0.590675,6.083376,9.331415,7.072206,7.513664,-7.838367,-0.797626,1.882999,7.677217,-8.784066,-1.901218,-4.467916,3.007193,3.332315,7.070661,-7.460618,-0.835853,-2.554070,-9.462533,5.877187,-1.804033,-0.597569,9.209203,9.919827,1.961570,2.220962,-7.862118,-2.695551,-4.942875,-1.966305,-0.809255,-7.349559,-3.174015,4.719714,-5.293793,3.741839,-2.228073,-7.497991,3.091870,-5.593615,5.861350,6.429658,1.661686,9.555168,9.311912,8.296148,-5.014492,-2.861315,-6.310561,9.909097,-3.634152,-9.571796,9.246092,-9.338262,-6.225931,0.856048,6.324627,-5.291465,-3.895718,-8.946693,4.367161,-8.939063,9.636995,-4.587058,-6.488647,-0.645238,-3.513671,2.613580,4.756292,2.089023,-3.991227,4.314953,8.563780,-4.459024,1.016899,7.375931,-8.619846,-5.957616,2.003780,-2.154625,4.398782,-4.120333,3.303986,4.744763,-1.141777,-7.163651,1.396790,-8.230177,6.140142,7.788661,0.238996,3.227147,-0.774942,7.244644,0.323242,6.087662,-8.002161,-5.376882,8.901067,5.872502,-2.899263,-7.305514,5.288423,-9.005950,7.867421,-2.183730,7.319445,-9.613122,3.878974,0.721169,3.679265,8.215093,-6.426927,2.593129,9.423236,7.207031,0.270587,-5.541303,-3.581348,4.388961,-4.439565,-0.155601,-9.152556,1.083042,-7.181382,-8.398243,6.656712,-0.832294,4.087794,0.921413,-9.109533,4.684486,-9.247010,-7.350526,-4.791874,-2.040379,3.784264,-8.674725,1.077374,-7.309613,-3.041340,-7.173503,-6.692371,-3.544192,-1.739686,3.785699,-7.489078,-4.534338,-1.432608,-7.968553,9.445318,0.638003,3.893821,-7.623382,0.654571,0.741286,1.915358,0.297004,-0.510959,1.625597,1.976398,2.442753,6.979839,-1.614258,-0.115863,5.916759,4.582676,6.672999,-0.205114,4.413144,-3.225338,-4.954096,-5.404634,7.162661,7.067036,-5.596945,5.923589,-6.859096,4.767028,-7.329683,0.019580,8.559656,-6.043343,-0.572886,-4.287838,-8.570968,-9.764804,-1.748928,-1.122256,8.402730,6.208537,-3.338286,7.826236,1.850964,3.755455,-8.600352,5.953952,0.385985,-4.188884,8.856846,-0.120123,4.099490,-5.528485,0.442258,-8.169345,-4.379035,-2.794030,-0.539715,0.510823,1.431311,-3.051224,-3.996192,0.416963,9.263604,6.130224,8.059979,3.726348,-9.391428,-2.840531,-9.784790,-7.479898,-1.405674,-6.270894,-6.850034,3.347812,-6.644083,5.450956,0.609333,0.505911,1.039916,2.094923,-6.019013,9.406714,-0.269477,-0.617989,-2.015485,0.122792,-5.324862,-1.559603,-2.348241,-2.407648,3.603319,9.454180,-3.223308,7.381759,3.644088,-4.662656,3.111616,-9.492257,-6.511485,1.267039,3.379292,4.777404,-7.148714,-8.057030,3.813860,6.583900,-6.732700,-3.457935,1.988186,-6.841435,-4.875510,-9.273385,0.929706,-3.273931,-6.225457,-2.757047,-2.554489,1.865032,2.502884,8.823076,-1.497240,7.711626,1.683642,2.270325,-7.505102,4.947502,3.598381,-9.801016,-8.323102,-8.763974,-6.691200,-8.998219,-2.550938,3.200341,2.901371,4.355247,-9.520307,1.247184,-8.507240,-5.501106,-9.558145,8.040559,-1.699179,-1.200045,-9.367632,1.560047,-0.360996,-8.435427,4.614113,-1.758439,-6.286047,-5.750807,5.503548,5.418550,-1.038592,-6.372406,1.619063,-2.765036,0.592803,1.081427,8.385406,2.473363,-8.965399,3.291028,1.377275,1.629632,2.912927,-9.209913,3.500024,-6.670004,-5.163527,-0.799039,-6.740269,0.173167,-3.363414,-7.139368,0.726823,7.763453,8.950572,8.393942,-1.111359,-6.350701,-7.545775,-0.930494,-4.656087,6.392821,7.494003,7.833206,5.980570,-8.530447,4.497554,2.339859,-4.324571,-5.576482,1.824545,-3.503722,-7.321842,5.824758,-3.950195,-7.748776,-4.874885,6.932485,-3.716337,-9.040302,5.207572,2.080814,0.660904,2.010125,4.299387,3.282157,4.410983,-6.381672,-1.445309,-2.172512,-7.642085,-0.206332,-3.444113,-3.505423,-6.086005,-0.556276,6.721019,-5.543825,1.653641,-3.197176,3.036363,6.956637,-3.946681,6.669387,-4.161686,6.416629,-7.152606,9.953071,3.562392,6.729909,-1.725395,1.761897,8.265577,-0.584749,0.911915,1.891897,-4.939696,4.509811,5.924299,-3.189518,-9.437335,-2.811850,9.831398,5.243811,0.379767,-3.770367,6.862047,-1.597884,9.888857,6.658102,7.240299,9.929570,0.671574,-5.462004,4.637704,-9.374040,-9.042787,1.271370,2.306408,-6.781251,6.630536,-4.917162,-4.325875,-6.108572,-9.205743,-6.364414,-9.432581,8.418660,-1.819089,-4.533631,-7.793858,8.472753,3.870769,-5.432625,-6.830538,-5.635666,1.608017,-2.862639,3.235606,0.815207,-4.011409,8.144397,-7.889394,-9.781986,0.831143,-3.422287,-8.541777,-5.108907,-1.130448,-8.376714,-8.594436,6.474895,0.335041,5.466143,-0.827709,-4.899610,0.023645,8.300757,5.848497,-4.386582,6.668216,-7.488902,4.986652,0.330035,-4.669489,-3.583227,-2.040716,-7.013561,0.898227,-0.177098,0.243021,-6.372539,9.449313,-5.135014,0.695512,0.046459,5.419409,-6.195229,-2.573387,6.409322,6.886719,3.962334,1.884955,-4.001352,-1.622433,-7.176690,2.375889,-7.430453,-9.509615,0.939458,3.435583,-2.727180,3.133721,0.778463,8.798973,-8.683906,-3.515591,-6.926567,8.073332,-0.763157,-4.275742,5.652148,9.560576,-9.478606,-9.870456,-1.656821,-5.896588,3.582994,4.618484,9.396211,2.767778,-9.841943,-3.704588,8.206099,1.165112,0.226528,-8.054713,4.914398,-9.531543,2.872574,-8.992719,-2.128661,6.163312,-2.167703,5.373648,3.251683,5.066652,-1.216457,-1.792528,3.961885,-4.899005,9.217199,-5.688966,-5.599229,-9.911615,1.816508,0.928858,8.344255,6.874058,-0.782794,-2.892103,6.062099,1.309258,4.336514,5.317620,0.499568,6.100959,-9.849681,8.654927,-4.083497,2.204280,-7.120357,5.967227,6.825852,1.872100,9.036147,2.176881,5.064437,5.753431,-3.839379,-0.794934,-7.769203,6.679229,2.388281,8.472503,-9.828335,0.339063,-4.813365,1.637664,-3.058923,8.209033,-9.854942,-7.718160,3.885397,-8.903871,1.568125,2.770399,-3.332123,-4.565540,5.468358,2.596590,-9.929299,2.035045,1.742837,-1.769687,9.018355,-6.064405,-0.365283,-4.841797,-0.142113,-9.546422,0.572669,6.618305,-9.032291,9.692876,5.757964,4.060880,9.817136,-5.616070,7.391304,-6.888235,-0.784339,-8.686034,-1.822316,-0.016628,5.052316,-8.837206,-6.365953,-8.285590,2.718516,6.601042,-2.057121,9.777570,0.098160,1.007126,-5.473379,7.957138,-4.005427,-2.502834,-7.111787,5.420034,8.990361,-3.889421,9.093381,-6.351112,-5.372573,7.025481,-9.639287,7.173755,1.070220,3.297827,-7.771433,-5.024171,-6.055363,3.815665,-8.272685,9.440537,-2.851408,3.820679,-9.446204,5.978621,1.576075,-1.327121,5.105355,1.668162,-1.793451,-5.151690,-5.589883,0.650957,6.941084,5.532427,9.085585,8.442618,9.577079,2.109766,-9.573471,-5.460004,2.764064,-0.353552,-3.748429,7.999350,-2.605473,-9.053499,3.433627,5.868451,-4.775932,-9.821586,4.663011,-8.845076,-6.742878,6.059231,-5.378426,0.333660,-0.345278,-2.569912,0.488920,2.586164,1.481903,-6.619601,4.753277,-5.859017,0.010315,3.735565,-0.432763,9.756953,1.443820,-7.086477,-4.058928,7.943035,7.875134,-0.047252,-8.982726,-4.208154,8.500700,-9.176377,-1.986901,-8.542999,3.908608,2.575738,9.803003,-6.703118,3.536525,-8.131612,-9.138949,-8.810061,0.671759,0.576544,-1.736634,-6.111646,-3.383431,-0.473135,4.953425,-5.327970,-4.841643,-2.926550,-2.883056,-7.751824,7.369552,-6.649258,-4.418421,8.771136,3.061152,4.315674,-1.288342,0.246848,-1.877791,-7.294357,-0.556223,-7.563837,-2.924385,9.563341,-7.451606,-3.171735,-6.613792,2.204413,4.891216,0.153175,1.560745,-7.171196,-3.395326,7.475514,6.197009,-0.862695,-6.456101,-2.714544,0.420863,-5.364346,7.063598,-4.273644,2.276445,-7.513052,-9.056378,0.967094,1.797434,-9.200518,5.098955,-4.138413,9.531457,-7.172008,-1.771619,-5.080027,-3.640874,5.345069,9.107415,-2.114247,7.924553,9.780654,-5.426922,-7.171325,-2.041619,3.640516,-0.678268,-8.613682,-0.237498,1.904504,3.591969,-1.596773,-2.881330,4.802630,7.967893,-2.986886,-1.943973,2.251650,-7.626811,-5.886367,-0.370412,-6.378196,-9.207218,-5.238679,-6.183551,7.208407,9.292867,1.964622,2.241203,9.447598,-4.635602,0.898674,7.125714,8.463414,-2.458786,-9.768095,6.689954,6.274522,8.786944,-0.382632,-0.198184,4.738682,-2.310196,2.275656,4.373685,-6.411236,2.357772,-2.206336,-3.336907,-4.076648,-0.563156,2.646593,-7.171011,8.804633,-2.817834,8.202643,5.773570,-5.208027,6.866985,7.931630,-4.712685,3.756070,7.608790,-6.604719,4.028513,4.145078,7.839282,-1.991014,8.079819,7.288976,2.978698,-0.740480,0.297514,-2.814527,1.922055,6.398524,-8.034675,7.112479,1.140039,0.660416,-7.313962,-9.712067,-8.120300,1.834059,-3.788467,2.827936,1.548516,-0.029600,0.108255,-1.832356,-5.243743,-7.054412,-6.630712,-9.962817,-5.863326,-3.101002,-2.373558,-1.281898,7.503519,4.419568,9.044273,-1.323608,-5.097625,1.177740,4.763585,-3.272559,-3.209025,-6.225740,-5.416048,-0.944098,6.833894,-4.448543,9.368591,-7.876811,-6.390802,-4.425602,-6.999941,6.772440,7.946292,-2.508453,-3.714641,-3.467526,-9.904103,3.196076,5.535849,8.243861,-3.412827,9.762752,-1.282672,5.156199,7.667615,-5.920431,-3.604025,-2.206687,1.852415,-5.668425,-0.337460,-5.790412,-9.290252,7.802899,6.834396,-3.679997,-4.570087,0.532039,4.339914,-8.957707,-5.160572,-2.504755,-3.469566,-6.052844,-5.211385,1.701689,7.015328,3.315597,1.850791,4.919042,4.586763,-6.072398,7.134907,-6.707214,-3.254519,0.849766,-6.300246,1.909922,4.165734,-2.573053,6.079929,-1.960121,6.135982,-1.232464,-6.813970,8.805435,0.709982,-6.046293,2.898982,4.920838,2.027717,-2.032724,-9.707686,-0.416986,2.736171,3.551580,-7.143801,4.326911,6.069215,-5.289644,9.098618,0.698671,9.970567,-2.857702,8.610248,7.674507,-4.944608,-3.705823,4.153890,-2.101296,2.531810,5.661810,2.330742,8.924109,-7.001076,9.703530,7.341891,-1.969557,-5.060047,4.563413,-5.280830,-9.594831,-8.666388,-1.126027,1.017370,-3.751662,-6.370831,-3.599553,-4.929165,7.073404,0.899721,-3.920495,3.065620,0.148834,3.388887,8.501639,5.110342,2.194812,-6.867574,-3.998454,-5.087452,-5.938426,-2.557690,5.615511,-6.777187,-1.003297,7.666252,-9.967009,3.583733,-4.785041,-0.033345,4.475259,7.170184,0.079280,-5.327113,2.343291,-7.723635,5.330108,-1.510147,1.910750,6.984264,-3.758066,9.885788,-3.148767,-1.684418,8.636523,-8.199932,0.875616,4.479049,-1.057263,-2.141695,0.226439,0.948768,1.769976,0.940172,7.488408,-7.388099,5.969321,-1.975175,8.091348,-9.927745,-9.015535,3.506833,-7.640681,-8.833566,-3.364710,-2.360576,-3.034058,-6.197020,5.271465,-8.032803,8.928671,-9.383739,-6.309357,-6.508008,5.179659,9.185070,8.670415,6.683055,9.347408,-7.807639,-8.475730,6.485749,1.348065,6.113095,3.320510,6.877484,-9.498656,1.837905,-7.003308,-9.053901,-0.536999,0.578150,-4.733192,1.456884,1.145248,3.253782,-4.106548,-4.683733,8.204873,-5.442267,9.081123,2.761152,8.070968,6.522550,-6.512769,-6.192725,7.627318,-0.430986,-2.878827,6.242597,-5.857129,-0.712516,-1.795756,-2.506263,-6.391921,-2.884420,-7.990581,1.316857,9.983120,5.438184,1.457311,-1.145862,-5.969385,-4.536683,7.464826,-6.737842,9.323491,-1.492251,4.812400,6.596399,-5.630080,0.177998,6.383099,-2.683721,5.499209,-5.187700,0.165212,2.666317,0.052105,4.689891,-5.314090,-5.380529,-0.593958,1.010906,9.282994,0.733258,-7.949359,-0.459874,6.709868,-4.381356,4.595057,0.664661,-7.067478,-2.635805,0.044412,-2.803789,3.522435,3.987929,6.592144,5.240014,3.964160,-8.438564,4.113246,0.363661,-2.784440,-8.828427,-5.621735,-1.141159,-8.716671,-4.849680,-9.251161,3.669124,-1.570288,0.171736,2.743070,-9.990791,5.046776,8.905897,-4.783876,-0.461071,-3.525599,-3.721101,-1.623221,3.652412,7.651071,-1.934070,-8.001804,9.483926,-4.307755,8.665394,7.194796,-7.188435,-2.062774,3.298965,-1.505317,2.211250,-7.486675,2.326597,3.756901,-3.501544,1.616397,-3.462219,-9.699222,-2.499386,4.519697,2.755095,0.328630,5.278469,7.007324,-9.635592,-0.197661,-9.656167,8.874859,-2.691130,6.469194,3.716971,9.134816,-1.104020,5.893228,9.603004,-1.808546,2.051191,-6.981312,-6.669915,-1.831419,-7.455667,-9.346798,7.124806,-7.537449,-4.984471,-7.233633,-6.144305,-3.755078,-3.604285,7.866486,-2.308019,-6.249722,-4.246432,-3.009961,-9.297699,5.561446,-4.900230,4.196882,-6.030966,2.249049,3.648565,-4.211716,4.577754,6.179323,9.268880,7.723738,-0.102746,7.169266,0.188126,1.276768,-5.541049,-9.214446,0.115353,6.826141,8.710548,-4.978655,-7.911390,9.628994,7.008695,1.420658,6.974417,-8.008314,-4.380338,-0.663724,-4.352703,8.920393,0.807846,8.784211,-2.948063,-5.646871,5.516099,-8.552264,7.821349,2.585872,-1.447968,5.176003,-8.001637,-6.099583,-7.140941,-6.406061,-2.888883,4.350180,7.111691,-7.568712,2.207099,3.503966,-8.703331,4.665673,0.266970,-7.213203,4.667089,-4.306301,-2.109690,2.365855,3.607336,3.238653,1.736143,5.501905,8.308373,-4.919739,-2.982660,3.097390,-0.502486,5.301344,1.461883,0.396105,0.389309,-6.299449,-3.731434,-3.671250,1.527404,-3.439915,6.309232,4.024907,0.842189,1.428175,-3.224035,-6.704285,3.895410,-6.274750,-4.379519,-7.846425,6.546127,6.926242,-5.514985,-8.656149,2.340572,-1.283742,-7.884605,2.032679,-2.588460,-0.560877,4.886644,6.536334,-0.540727,9.580817,4.375040,-2.098814,7.184798,5.239136,-2.071145,6.110290,-8.884787,-8.555183,-0.222481,-1.266543,-4.503456,1.674951,-7.925370,5.992663,-7.526173,5.165265,-8.345519,4.679498,4.772647,3.088581,-7.203975,6.050802,-2.901879,0.176528,0.658088,2.412403,-7.045941,5.235366,6.127509,1.374157,6.453950,-5.067131,6.834668,8.852880,-3.337358,-1.673092,-3.104716,3.171310,9.384906,2.879747,-5.117029,-4.830484,8.818092,1.938841,-0.444868,-8.211032,0.073757,6.992668,-9.644004,7.478251,5.913544,2.425754,0.132853,4.939652,-8.497198,8.871248,7.105477,9.707452,7.409233,-7.236260,-0.982359,-0.351771,5.487306,-2.120293,-8.961813,-3.094748,5.275905,0.720377,-8.913931,6.907491,3.932236,2.513011,-3.748526,4.768041,-2.869491,-0.367751,7.400940,-7.413867,-3.091169,-0.932915,0.254812,7.785838,9.523259,3.856282,7.451676,-2.728100,-6.159299,5.481234,-0.964879,-2.542314,-2.085730,8.349770,6.874245,-4.252633,-9.530093,3.300594,6.405519,-9.001410,9.536833,-7.971542,-5.502116,-3.423481,4.633678,-2.055466,-4.472001,-0.819843,6.153894,-5.323627,8.244382,-9.888974,-6.983197,4.229011,-2.680346,-3.937101,-0.480287,-7.286064,2.501381,8.550050,8.746786,-5.582536,-6.983238,-8.216057,3.169638,1.718611,-2.217163,-3.592784,4.602722,-0.208675,-6.968813,6.522682,-1.051140,6.656362,-1.130390,-0.310840,-1.280865,-3.688380,4.259638,-0.639949,9.271969,1.676795,-4.208305,-0.934880,-2.932367,6.414460,7.261332,8.012550,1.057509,0.424579,4.569739,4.026869,6.746639,-2.726885,-6.584849,2.279993,-5.881149,5.915057,-2.020992,-0.358278,5.724950,8.688602,6.488904,-1.050864,-0.867102,-5.872064,3.915138,9.242365,6.642030,8.109219,5.665420,-4.885885,7.390775,-0.224817,0.023400,-5.946365,-0.867471,-5.452942,-3.316072,-1.955705,-3.948446,-3.617232,-2.035443,-0.885930,-1.153603,-4.781389,-3.424924,8.376115,-3.981175,-0.064110,7.860540,-9.010381,-5.133066,6.189850,7.948307,0.836941,-1.250318,7.497797,-7.450285,1.993614,9.857844,-5.286159,-8.654324,-6.465263,7.614265,-7.530169,0.576776,-3.993306,1.745223,0.565484,-2.427108,5.036276,-0.914254,2.450832,-7.083505,8.610956,-6.164737,-1.822542,-0.626694,-3.631453,0.824996,-4.218777,7.040361,-6.105671,-3.722100,-8.172239,4.350006,4.067588,-6.624430,-8.714494,6.804232,5.545469,9.549932,-6.785761,-6.000884,8.251063,-3.235188,-3.059924,-8.102790,-6.507595,-2.388508,5.812449,-0.366887,-9.741470,-5.458528,-1.251133,-3.274724,3.556474,7.898097,6.208764,-7.964345,5.154633,-0.651679,2.668062,-9.745035,7.746548,-2.334491,-9.915718,-6.799394,8.318996,6.389435,-0.382278,9.523067,2.010177,-4.617160,-3.494950,1.820145,9.828051,-2.930557,8.675815,-5.248200,7.560138,8.282380,-5.072328,-2.135028,-4.144879,7.327529,-9.613505,2.283288,1.706965,-4.718130,-3.669558,3.426336,-0.363999,-8.644450,-3.343205,-3.246398,8.071089,-4.972914,9.780120,-8.308292,-7.240221,3.645734,-6.643339,0.920090,-1.320514,-9.082289,5.784596,-4.088136,3.623611,8.974821,4.933071,1.417332,-9.343110,-0.473364,5.089760,2.992489,-3.975223,-9.895392,5.426604,-0.010308,4.185316,5.001471,-6.246409,-7.712277,-7.343742,-1.017103,-7.804975,6.160432,9.630417,-5.219364,-4.634792,-9.161504,-3.644703,8.057850,-2.795645,5.512868,-0.704047,7.422037,-1.957739,-1.961856,8.198087,0.352213,8.233781,-3.909178,-8.976482,7.901512,3.768187,-0.362908,-2.293161,4.958522,2.870880,-1.791823,0.232920,4.522396,-8.372211,8.466209,-9.242186,6.596488,4.112305,-8.472425,-5.307451,-0.545528,5.387607,-5.296469,-5.721414,3.598846,-1.719887,-2.481221,5.920797,-4.878823,0.307302,2.447004,-0.200027,0.547261,8.456469,4.818714,0.681179,4.109798,-4.249583,-9.241971,0.201931,8.202970,-0.007849,-5.014154,0.827775,1.405863,-3.613330,-6.329472,4.084517,-4.995851,5.344136,-2.550291,8.597241,6.606283,1.649394,-5.010170,7.147479,4.742111,9.295395,1.342121,-5.515400,-7.165015,-1.382824,8.524918,-4.545510,-8.830043,0.085831,6.688173,-8.298624,3.728519,-3.123512,-4.574274,2.014470,6.670344,2.322840,2.448169,4.599276,-2.361448,-7.065681,8.983521,0.711602,-3.709274,7.055571,6.246296,-6.393666,1.807839,1.869544,7.139986,9.271301,4.874183,6.467754,-3.101346,-0.923203,-8.439096,-5.274546,-6.349377,3.410370,1.148212,-1.879662,-8.480068,8.988768,7.588889,-1.186922,3.887910,-3.401995,-6.320410,8.402804,-1.109976,-2.124042,-4.230753,8.597439,-4.766274,6.223749,6.960023,4.022558,-1.973888,3.854027,3.296173,-3.245533,-6.877562,3.577133,7.789375,4.092410,1.005363,-8.022130,5.950117,-1.854518,7.670082,3.909017,7.060919,-7.903007,9.363688,4.467168,2.820523,1.484435,-1.981445,6.110220,9.375795,-4.582002,-5.886829,-4.194875,-9.962606,9.931684,-8.779412,-4.704027,9.797659,4.277864,-7.770459,1.213867,1.348396,0.691565,-8.872690,5.976934,-2.472388,-9.762259,-6.821630,-4.414518,2.873814,-7.135644,-1.843280,6.135762,-6.735374,-8.401312,3.617300,-7.064976,-4.383986,8.783622,-8.785291,-9.902975,-2.871784,9.557474,1.916971,3.398453,-7.038138,-6.860906,-5.758226,-9.763004,-2.011588,6.947979,8.497550,-3.000095,-5.906716,-9.029373,-0.020685,5.051251,7.776072,-7.106395,-1.230928,6.841617,0.234452,1.146269,8.456750,-0.670167,-9.333904,4.429531,-9.949177,5.188924,7.282744,1.783092,-3.462283,-6.427609,-3.828943,-6.857038,-7.472158,0.738857,6.369840,1.711365,-0.727962,-8.240341,-8.204367,-2.790197,-0.213188,1.036480,3.279281,7.720883,3.292075,5.867047,-2.514004,-3.182392,9.002084,8.030376,-6.449373,5.991579,-1.165840,1.660013,-8.103674,1.220452,3.964886,-1.657934,-0.672682,-7.323734,-6.200225,3.062148,6.035260,3.232755,7.622497,4.461775,-0.604227,-8.223876,-2.199238,7.437480,-5.021308,9.493764,4.116647,-5.317103,-7.697165,1.708472,8.504551,5.760646,-4.073191,7.218413,2.501015,0.560050,-3.841428,8.795963,5.042049,0.080414,1.946042,2.258789,-2.247392,-7.810868,-6.342723,4.737280,-1.307323,-5.197459,-9.470987,-7.639135,-1.939005,7.612146,-0.226158,9.958874,9.846562,5.798558,-5.739152,8.605834,-3.510563,4.221105,0.057054,-3.878753,8.207864,-2.789196,3.776788,-0.099572,-5.283938,-8.581983,-3.856311,-3.032401,-2.572795,-6.781558,-4.634349,2.895996,-0.885917,7.602550,-2.451267,5.030317,-9.311755,2.369950,6.855880,6.028319,8.725343,-2.596335,5.427451,4.186444,-0.649981,-2.707187,3.963425,5.461141,-6.727608,5.227293,2.093152,2.332219,-5.837303,6.431819,-9.818191,4.315040,-3.697058,2.098558,-1.521896,7.308563,-7.638944,5.966124,6.983929,9.724520,2.329388,-6.454252,-0.285062,-2.153152,-9.103111,-4.985546,-6.887730,-0.980844,0.097664,-2.221117,-0.015329,-7.543311,-7.934250,-2.378607,-9.166802,6.318549,-0.795773,-7.468043,4.738523,3.461438,-6.347349,-9.937590,8.931668,2.556405,-5.641851,-5.095499,2.994518,-1.167500,-2.558559,-4.439264,-4.282388,-8.526278,9.323140,2.276831,2.402688,6.256191,-8.459566,-4.770961,-4.766298,-6.144207,-8.903974,-1.790503,1.178103,3.319381,8.656013,6.086336,1.889265,9.048490,-4.743924,-3.705903,7.529060,-1.975766,8.027267,-4.348417,-1.442997,4.772287,6.852522,0.310915,-9.332371,5.531696,-7.973823,0.708480,-6.991727,-4.507034,-4.561882,0.607639,-4.654086,9.294477,-6.555415,-5.296120,1.895114,1.314185,4.364444,2.886022,2.786973,8.233040,5.494131,-9.819101,0.329871,1.789889,7.770245,-4.882303,-0.289357,9.686483,5.660098,9.438630,3.222201,8.648751,0.781266,-7.718725,4.797926,-8.362564,2.446886,7.525751,-8.778480,-1.431560,8.810292,5.720212,-7.384743,-5.695284,-8.166344,-7.079540,7.919024,-5.302244,6.495161,7.239528,0.754750,3.594855,-0.979081,9.899611,5.115990,-5.039476,-7.902686,-6.195811,3.349612,-7.929493,0.226493,7.477048,4.704244,6.861936,2.934365,9.431625,2.788054,5.234720,0.150320,-6.429572,-9.738235,5.732353,-2.991871,2.754379,9.916310,-6.344966,5.593063,0.575753,8.545009,4.919121,9.940772,6.816237,4.224081,7.650181,-6.220165,-5.009714,-0.349718,8.067443,3.354596,-8.637115,0.794795,8.708752,6.991297,8.914212,-4.335921,2.646030,8.302709,-9.896117,3.543145,-3.914499,8.136345,-4.967053,-7.528597,-6.936982,-4.872632,-0.836285,7.841325,-5.004664,-4.757274,-2.084921,-8.800253,8.206393,-9.856860,2.596887,9.140755,2.098051,-3.413925,-7.985674,-9.176951,-5.706991,-4.139892,-0.933778,8.716284,-9.629893,-1.729907,-3.053735,-0.449078,-7.807929,8.030832,-7.768216,2.151997,6.756595,3.062143,2.146907,-8.038554,-7.162412,-2.769254,9.111896,-0.464075,-3.981919,-6.364332,9.637036,-5.472835,8.720890,6.866011,-8.564575,-5.026657,-6.492422,2.754629,6.638397,-7.785671,-1.702381,-2.525135,-9.852241,0.003678,5.337227,0.231085,-4.511729,-3.373603,0.382060,2.784195,6.128107,2.519505,4.471739,6.357682,-6.257614,8.024532,-8.860618,-6.750314,-5.842719,8.178696,0.738077,-0.211399,-2.484215,-1.586258,5.984492,6.836091,4.374102,-7.846095,-9.451014,7.657064,0.263544,3.260449,-3.794783,-0.194517,-5.959327,-8.400939,-5.454402,6.448790,4.825499,-2.124954,-1.651269,9.370384,-4.163577,-2.699248,0.983645,-3.337808,-2.209305,2.347395,8.006084,3.045077,1.579376,-5.123765,4.887989,9.513681,0.617247,7.266725,7.139194,8.245608,-5.167016,-3.503793,9.456980,6.731956,1.674725,-0.629872,-3.748059,-9.679664,7.837198,-4.185119,-7.922668,1.694036,3.166846,2.178085,-4.596649,0.217272,5.218838,-8.810847,-4.238385,-4.259060,-1.670601,-5.030857,2.000127,1.988437,1.272680,2.048814,7.729152,0.248432,9.205389,4.257013,4.579676,-5.490657,0.773338,4.799129,-3.094868,3.132910,-9.949878,-8.501895,-4.056582,-8.979411,3.169064,5.940396,3.253247,3.430619,-8.016388,-4.091070,5.294953,-3.565210,8.277737,-6.323242,3.767743,8.712707,-3.373317,3.050338,3.107405,-1.327433,9.364753,0.033007,2.808549,8.221644,7.367974,1.676017,2.047000,8.195699,-2.143246,-1.981540,2.511463,6.327726,8.378314,-6.687087,9.398838,9.411268,0.642304,8.493929,-7.367304,-5.936086,-6.871410,-5.149507,4.542955,-6.660540,-8.840103,9.251882,-3.173240,1.809142,-1.519790,-9.378203,-9.791254,-9.252176,-5.587255,-2.019224,7.691435,4.926155,8.450553,0.141425,0.746009,-5.894578,-9.061335,-3.144306,-4.982801,3.284111,1.150034,-0.056624,8.523635,3.714295,-8.874089,-8.079299,-8.235410,2.852022,-5.974053,-5.470802,1.240449,0.154365,0.246563,-7.829983,4.797137,-4.988777,-9.562600,-4.201549,5.647849,9.612146,-2.846836,5.704950,3.871889,-4.376092,9.243121,-7.686149,5.491227,9.666158,8.762922,-9.698389,5.820662,6.021222,-7.251595,8.985328,-2.858974,4.939405,2.313879,5.342267,-0.958600,-3.418840,9.214150,-5.569222,-3.525642,6.598937,7.131306,-8.265252,-1.567808,-7.606994,7.927215,-1.286619,2.989737,-4.821585,3.438323,1.326465,5.954825,3.596120,-9.389675,5.542459,6.447463,-1.268690,2.408154,4.445341,9.243825,-2.543422,-3.268924,-2.564192,-6.296245,-7.780453,-9.756102,0.908326,4.468026,-8.955142,-3.694889,-6.963577,-1.790679,0.636518,6.694564,8.414690,-0.914679,3.775463,3.662789,-5.993249,1.310063,8.563687,2.174690,1.265996,3.707531,-7.119938,-5.816547,-4.285749,-9.080866,-0.959485,-3.412513,-9.491753,4.912341,5.766084,4.938224,-7.434898,-6.312741,-9.598920,6.042548,-0.577044,-8.956864,-5.576664,9.023497,2.381688,-7.175981,1.764266,-0.560777,-6.770267,-4.938198,-5.705196,3.437832,-9.625597,-0.187866,6.666644,-1.167243,-3.805952,8.234103,9.951007,0.036428,-5.592839,-7.214559,6.356895,3.108447,-3.933197,3.382928,3.199579,-1.024221,2.957430,-4.737900,-1.591146,-0.138379,4.616710,4.917740,8.341118,-5.586709,6.009202,3.025491,9.240890,-1.616435,-7.124970,-1.021961,-6.189078,9.947638,1.580629,1.230106,4.807029,-5.239217,9.430594,1.811167,0.503768,-5.421975,4.585172,1.658371,-9.550094,-7.312606,5.950536,-1.092100,2.471131,5.573217,5.707089,-2.808931,1.093002,-2.094374,2.073240,7.539982,0.071401,2.537208,5.312575,2.479253,-0.111919,2.609039,-3.831253,8.566963,9.731970,-2.017149,0.872122,7.709587,3.391831,6.518087,-5.074005,6.848813,-4.179501,-3.547873,5.101440,3.091047,3.172559,-1.017630,-2.967882,-4.603009,-2.801356,4.877508,2.928923,-8.982192,-3.124315,4.971579,-6.098828,-7.489374,5.904923,5.068143,-3.513918,-9.195138,1.431509,7.218920,1.983415,9.581244,-9.135636,1.780475,-2.272745,-0.440935,-5.996106,5.822910,4.121732,9.898424,-1.174521,9.970701,-1.692996,-3.777389,-3.411228,0.286993,6.032978,-9.693706,9.546883,-5.477376,7.457665,-5.548461,-7.721227,9.152626,1.577649,9.326957,5.113058,-0.784558,-3.054759,1.015260,-2.290628,-3.518911,9.242533,4.960304,5.710530,-3.850613,6.349956,-5.849349,-3.117388,5.238043,-6.784212,8.644380,4.850251,4.765057,4.874844,4.344480,-9.062854,7.663935,-1.491643,-4.873539,-8.836551,-5.829958,-7.319606,-2.944759,-1.081142,-6.183243,-4.623051,-7.551430,-4.603246,9.404771,-1.182175,5.846316,7.994781,4.162056,-0.271796,1.521864,-5.657369,-2.788302,-6.825674,-9.295971,-7.579292,3.590299,-6.093912,-4.653498,-8.010286,-3.740567,-6.418329,3.387747,3.602680,3.392461,-2.609315,-9.968215,1.330335,5.026994,4.966993,-6.013064,0.554285,-3.347010,-7.710052,-4.989842,7.860390,3.108256,-9.338815,9.279113,1.520110,6.807079,5.331894,4.381353,-5.599582,-2.964661,-4.422896,7.986066,-0.419760,9.689942,7.590895,3.201321,9.218317,-9.690506,8.462581,3.032983,2.475355,6.132523,-7.523237,9.282855,6.111259,6.923138,-8.080240,3.963826,-6.172901,4.449809,-6.697999,-2.440433,-3.668166,-2.427418,-9.271260,-7.393796,-8.831302,-0.682149,-1.614884,-0.115792,4.525494,0.671582,-8.377335,6.448426,-0.516188,-5.144639,4.556760,-6.779149,-5.132352,-6.126037,-9.114351,-1.242383,-1.483661,3.288918,-2.886396,-8.533847,9.255787,5.152877,2.643200,3.889491,-2.112471,-0.663071,-6.325423,7.312864,0.686380,-2.197071,-9.996182,8.361657,0.172650,-5.818185,-4.035457,-3.397504,-6.107331,5.367927,-0.815946,1.378602,3.367149,-7.244515,-7.305389,-4.744405,7.997871,9.024624,3.383998,-6.119952,-2.411565,-5.273205,-2.975187,-9.181784,-5.265821,-6.886182,-7.945215,5.282581,7.062101,-6.535262,1.130313,-7.998191,8.932174,8.952481,-8.394428,8.049846,-9.485368,9.202558,-6.522963,0.953709,4.685320,2.753269,-3.915631,3.532587,5.519781,2.722898,-7.940983,2.471604,-3.636207,-1.561033,7.665792,5.938149,6.661495,-1.338967,-4.255734,3.026563,8.264812,-3.915438,5.875426,8.476536,9.520888,-4.109459,-8.099127,3.068273,-6.518692,2.489151,1.606704,4.468916,4.598899,0.471220,0.923842,-1.750016,7.589026,-7.319108,-2.424475,1.762061,1.204275,-8.973269,-4.156517,-1.730060,1.500021,-3.984618,-6.111590,-2.311487,2.910948,8.796333,-5.327908,1.786348,-8.703520,-2.611116,9.899377,-0.068986,4.462771,9.493704,-7.366938,-6.657414,9.821128,7.637319,-8.677970,-0.220649,5.930283,6.966566,0.541839,3.594064,-5.737393,-6.021136,-0.514016,-0.048105,3.783000,2.869224,5.687678,-7.223043,-6.305931,-5.815818,4.129680,-5.455856,4.789649,-8.297024,-3.823524,-5.485215,5.882217,-9.450516,-7.849311,-1.392143,-6.940333,6.709899,0.837902,9.617535,2.317926,6.037832,-7.281809,6.376939,6.106054,-8.665396,-5.416708,-7.177085,9.931105,2.541326,-5.208963,-0.457658,6.981955,-7.321840,9.690877,-7.854018,-6.098222,0.433002,0.951714,-5.088713,-4.040824,-5.433438,0.561318,-0.225770,9.709484,-4.656978,9.299284,2.009944,6.561286,-3.744101,7.187187,1.811632,-4.944046,-8.349137,-2.148727,-6.465939,0.300266,6.587339,1.320999,8.572883,1.408571,-9.291286,-1.522776,5.282883,-6.864002,-1.660490,-9.273265,6.728717,-7.741705,-0.781478,-7.827066,5.552410,2.766867,-6.472463,1.805055,9.303529,-2.218391,8.742527,4.578482,-3.817916,-3.797638,9.936645,-0.882961,6.385139,-4.810371,7.735993,-7.454303,-1.754636,1.472416,5.243710,6.918217,8.394207,-6.364111,-3.445436,9.418010,2.024513,-6.422150,-5.187572,0.039800,1.218691,1.932280,-6.649421,-9.515980,8.437512,-9.253245,-8.654698,-1.665321,1.829093,-3.120817,-3.336366,-5.074655,-4.876336,1.097838,3.891892,-9.733938,-9.030537,-5.237078,-6.812935,-2.850232,-1.411856,-0.622181,-3.834789,8.831836,8.450115,7.101161,4.909748,-5.565219,-2.456031,9.256211,-0.335297,2.596607,2.130829,-2.227094,-5.860351,-5.379271,8.407722,4.934188,9.020651,0.019632,-5.869036,-2.442227,-4.957671,4.735638,-9.940032,-0.670529,3.966667,-9.530440,0.276917,-6.901406,3.453522,8.896957,8.557006,-0.059596,0.575390,6.761233,-6.155395,8.572160,-6.069078,-3.930670,6.093044,-3.349217,-6.247993,-8.590829,7.640874,0.525261,7.740550,7.724592,1.082182,6.068471,3.183375,-6.114525,-5.982241,-3.344708,9.905539,-0.687408,9.548805,1.992722,8.781815,-9.366719,-0.408678,4.184024,-8.347891,-4.767319,-2.588092,-5.072364,-3.805710,3.351145,-6.821036,-1.730437,-3.047889,3.196521,6.907919,8.216000,-4.250417,2.733643,9.084174,-9.933425,0.388143,1.261003,-5.042731,1.255163,7.339637,8.417218,-6.077694,5.018671,-5.206607,-6.893168,5.347264,-8.768117,4.505883,-7.227930,-0.970244,-7.356762,8.266196,8.735705,1.171333,-2.760596,-3.661605,8.564742,8.386855,3.619712,4.777365,0.273126,-1.497050,-0.969248,0.479399,-2.815999,8.217959,9.744912,7.339265,-0.007118,6.012157,3.007988,-1.567668,-7.145532,1.275593,-3.218954,-6.298574,5.759899,8.234865,-6.272343,-3.272657,6.643192,-3.911486,-0.532831,6.798170,-2.369570,1.111097,-1.696074,-3.633383,-6.009201,0.268882,-3.602835,-6.141146,-7.106152,8.897379,8.901244,4.604108,6.127511,3.381832,9.130680,-3.126289,-7.166611,3.304527,-7.908628,5.960772,0.253104,3.320679,-7.410689,6.326940,7.498509,-1.357284,-7.231528,0.908729,7.948521,5.226852,-0.727104,-8.069785,-2.029262,6.260694,-4.883963,7.595717,5.147114,8.858944,-8.893501,-7.174518,-6.767597,-0.768185,6.269308,-2.988917,7.108905,4.660058,-3.886914,-5.612886,-6.552572,6.224985,-2.362002,-7.045989,2.259629,-5.114299,9.785565,4.934720,2.292469,-4.027602,-5.248993,2.873246,2.438567,6.697037,-9.584387,-2.550313,8.191435,6.062806,-7.336060,-7.924322,-2.207335,5.197026,9.155565,5.770514,9.837626,5.203742,-9.270711,3.797406,-5.281472,9.600274,-8.196382,5.970033,8.593933,9.463948,-8.544228,7.268837,-5.957083,-7.708758,-7.935159,-7.052025,-4.431629,6.012829,-7.810347,-4.545501,9.935770,-8.202379,9.746301,2.254476,-2.854430,-6.533803,-2.950652,6.178843,-7.061635,7.036814,9.589640,-6.475993,5.337388,9.544124,-1.563945,-4.279798,2.036318,8.597823,-7.867579,-8.728191,-8.485736,-9.538762,-4.629961,4.489572,7.893097,0.314951,0.445484,-2.032995,8.579124,-6.667166,8.984789,7.346703,1.915570,1.657134,-4.200940,2.253470,-7.740085,6.019545,1.800693,-4.384355,4.961566,-3.085813,5.244962,-0.453571,-8.601015,7.191575,6.003497,-2.264490,7.423724,3.382872,5.959012,-5.499588,-5.549170,9.835269,9.098423,-8.693493,4.357288,0.449178,-9.439769,-2.907446,-3.228448,-0.633925,-1.543403,4.583382,1.214642,2.042890,2.893119,-0.514628,-8.723696,0.905947,7.388786,-2.333757,-0.330192,-0.993969,1.414515,1.770826,-6.264985,-9.904257,5.173342,-9.000375,-2.199898,6.565468,-7.565800,0.528262,9.777304,-2.615748,-7.639002,-2.326215,-7.390547,6.911947,8.722713,1.483505,9.272147,-2.860499,5.947305,1.526827,9.242910,2.509470,-9.412341,-7.896638,-8.246619,8.568456,8.618623,2.483743,-9.121071,-7.404968,-3.064558,4.712775,2.678639,-9.469759,-3.256082,-3.235259,-7.428333,6.780467,-6.731987,4.986459,-6.137407,0.293618,-1.612673,3.866073,-2.857240,-9.378401,-5.790587,-6.930776,0.070807,-0.955171,-7.375302,1.607208,5.385597,2.538809,-1.376679,-7.484395,5.423760,3.417180,-4.873236,-6.287215,-2.763552,8.625794,-6.145244,-4.268527,-5.148058,-7.946385,5.742577,-8.968549,-4.500248,-9.857399,-8.115123,-2.300801,-5.010042,0.474865,-6.910444,0.872481,-0.586842,2.387966,-9.474214,-1.847604,4.687857,6.824753,4.114847,1.797019,-1.990877,-7.774982,-3.672596,-0.168176,-7.233407,2.512859,-1.109678,7.808369,-1.091025,2.390742,-8.707466,8.064799,-9.252754,-4.757530,-7.595733,-6.605996,3.729546,4.763788,1.304660,5.352220,0.756889,-7.934011,0.690164,-3.532022,9.772164,2.610810,-0.579185,5.299714,1.635470,-4.657215,5.687499,-5.797659,8.413193,-3.647199,-9.867721,2.566740,-8.540929,0.906974,4.281671,2.315470,9.739606,8.958993,-7.000369,3.316049,-3.910026,4.176790,-3.764380,5.408762,-7.871189,-9.040310,5.624131,-4.399835,0.358278,8.131958,-4.923873,2.571889,6.751461,4.426324,1.341287,-4.837836,-9.349088,1.987385,5.791889,-3.873733,-0.902757,-4.433500,-6.112727,-1.446032,-3.464233,5.488317,-2.808798,0.250578,0.199459,4.997283,6.198507,-4.415000,-5.806877,-7.276361,-0.132812,6.742360,4.539136,-8.037509,-9.811036,1.581230,2.529179,1.114520,-6.231767,6.177914,6.126023,-5.974949,-2.872435,-0.964755,8.531550,4.598763,-9.778320,-2.672915,-1.898766,5.436115,7.244605,-2.935936,5.045155,2.077796,-3.985942,7.318395,8.114638,-9.327841,9.907791,-6.879012,0.603410,-4.950397,-4.313130,9.661146,-2.090643,-3.541091,9.118935,-4.022932,-2.625920,-3.600989,-6.979329,2.337794,-1.652000,-3.883268,-5.425820,-6.240271,-9.207163,9.909885,1.056501,2.368419,-3.806222,-9.727139,-2.972106,-0.886722,-8.723877,7.171009,8.284418,-5.251019,-1.934941,5.778655,-6.852196,-7.273010,-5.005013,2.868752,-0.209841,7.365766,-1.748857,1.845794,-6.896554,-1.840867,-5.270311,-5.774907,-1.382386,0.044754,5.847660,8.480004,-7.159229,-1.831071,-0.247171,4.749330,-8.032054,3.048967,-8.175904,-1.352578,-0.826954,1.810567,-7.529604,-7.406145,-6.965225,-7.525775,-9.610136,0.547015,5.895958,-0.069255,-3.662821,8.370531,-3.498842,2.583615,6.776595,-9.625503,-0.202133,-6.498223,1.076974,3.312888,4.006337,5.985027,-1.668205,-9.114391,-4.587282,8.848689,-9.949026,8.921977,3.731199,2.634135,-0.080098,-3.212557,0.652940,-5.900280,-7.844350,1.938203,8.267126,5.628635,7.233854,2.817140,-3.887783,-7.973652,8.566760,-6.151978,5.054685,7.953189,4.469188,-8.937832,7.247112,4.903999,3.579391,3.578326,6.677845,-2.384408,-7.984240,-6.651979,-8.944449,-3.768649,-6.382383,-9.154042,-5.370987,-0.953577,9.696866,5.245094,2.015053,-0.900651,4.894369,8.707736,4.503079,0.651118,9.576294,-7.997511,6.764844,-9.552294,3.351298,3.126314,-7.492846,5.337398,-0.257859,-0.899344,1.932471,-0.255475,-0.478034,9.385099,0.755205,-6.873884,-4.051230,-3.201325,1.892315,-1.660986,9.534387,-7.884845,4.257311,-8.022723,-7.264264,2.587493,0.181874,-5.077619,6.891667,4.205996,2.403081,6.446920,9.554967,1.849353,-1.130207,3.501056,6.982623,-3.083920,-6.166727,-8.514780,1.225128,-0.450668,-2.956569,6.000271,5.880394,-9.838211,-4.472356,-8.313366,-8.165351,-5.830941,8.018730,-1.956920,0.591345,1.357439,4.603110,5.105650,6.303172,-5.938033,-1.812865,3.883438,-2.598666,-9.513454,-9.480199,-2.432619,-6.596999,5.637453,7.172949,-6.697478,-6.151994,-0.529207,-2.915981,1.078317,6.928593,5.906551,9.537561,7.891136,-4.969153,-3.251114,8.428067,1.903270,6.877243,3.726838,6.404122,5.689643,-7.624855,7.121629,0.275408,-8.329469,-5.690803,1.856712,7.195583,-7.440657,-7.122430,-1.893781,2.018401,-7.671299,-6.452310,8.488724,2.966001,-8.944414,-0.492152,-9.088752,-6.427352,2.071370,-7.055614,-9.425405,4.952346,-6.317157,6.745713,5.130115,-4.398827,3.688024,-3.411585,-8.964731,9.586195,0.459768,1.705712,-8.554462,-7.606796,-7.320905,-6.694646,-6.600950,3.260353,4.478203,3.269637,-4.677736,-5.431339,7.112998,-1.362989,5.147368,-4.717349,-3.235725,-2.408842,1.860131,-6.899346,-8.098874,-1.977442,-2.653910,9.530868,-2.972000,4.883108,-3.076525,-7.574770,-0.307800,-7.531219,-2.690115,-6.201784,-2.826398,2.542329,3.275964,7.100689,-7.684262,4.222214,-6.131598,4.193314,7.392445,4.973057,-1.235787,3.450699,-5.451772,-6.676454,-2.405334,6.305540,-2.910441,-1.224408,-9.165609,0.947860,4.893698,-5.827403,4.502499,-2.234285,-2.024021,-3.349503,0.304409,7.890950,9.750242,1.706117,-2.653515,-5.078819,4.185348,-2.246493,6.823549,8.516659,-8.548285,-8.491523,1.214872,9.556983,-9.369895,-2.667964,0.835501,8.202309,-6.910082,9.075596,-5.699535,2.189024,-5.654467,2.645537,6.786628,2.090973,-3.829559,8.372170,-6.515127,0.124663,-3.415030,9.408617,6.085757,3.673402,5.619884,-1.003987,-4.043076,9.579324,-7.874571,-6.137141,8.533449,5.190689,9.460829,4.250391,5.091546,-0.003343,9.959308,-7.686947,8.297216,-9.054491,-2.848043,-9.886274,-8.466790,4.175729,-6.165760,-2.277279,8.616257,-3.193609,-6.183863,3.141328,-0.807987,3.850370,1.765827,9.549849,1.959536,8.944162,-9.117324,4.536625,0.471543,7.502921,-8.363602,-5.662073,-4.686900,6.540675,-5.904725,-7.467669,-0.590957,-8.894613,9.652653,-5.837718,3.230497,-0.919705,6.538877,-7.860921,4.801165,6.368421,7.439103,5.103523,-3.951460,-9.742214,5.507514,9.238486,3.864155,5.032016,0.018623,3.411891,0.782402,8.288562,2.804695,-4.151645,5.971153,1.337742,9.540564,-7.819302,3.614230,-5.367909,-1.033524,-4.849937,-9.725809,-2.361686,-1.683237,-7.237730,-0.741719,-6.888020,-1.497548,-3.507298,-3.625227,-4.428118,-8.101743,6.977167,-9.078345,8.015616,-5.544303,-5.318350,5.330680,-2.280213,-0.623762,-9.434268,-7.203280,7.041704,0.136341,8.867516,9.451575,0.510515,-9.449366,8.182556,-6.257602,3.211344,-0.247955,3.105636,7.247051,1.986773,4.680325,-5.546741,1.747008,-5.643273,2.876214,-6.604721,2.497630,-4.814738,7.651240,-5.502632,-6.359781,-1.042963,3.636475,9.130285,3.658254,1.186605,-4.910923,5.334379,6.506947,-2.573125,4.566248,8.787108,-8.754643,-6.567012,2.140025,0.031415,5.023244,-8.118991,-7.737585,8.726207,4.440037,-4.498691,-5.845920,0.761121,4.591462,-3.628354,-7.980594,2.295802,0.085258,-6.230400,7.532035,7.831110,5.022659,9.138556,6.936937,-2.359590,6.385437,-8.287924,-4.022062,5.700852,3.471500,-0.742893,4.975789,-3.968963,2.852672,7.251154,-0.582734,8.534406,9.907182,8.835840,1.663385,5.631405,-6.176992,-0.714054,1.249956,-0.668173,2.162401,-9.523161,7.347885,-3.326580,-8.928856,7.317321,-5.929258,-0.739593,3.691757,-4.745910,5.820963,-8.694441,6.092445,-4.641040,-9.061420,6.676097,6.108491,4.734563,-8.773569,-9.692054,0.731831,9.324895,-3.147100,8.699882,-6.249537,7.908808,7.043395,6.379651,-1.590783,8.384527,6.635674,5.460146,3.444896,4.344379,-4.519424,-4.442108,2.524087,0.333918,7.439008,1.856587,-5.670910,-8.662249,-6.160895,-1.249578,9.376442,-1.768757,-0.511115,-5.140841,-6.839105,5.217105,7.409376,-0.384075,7.678438,-2.150788,3.034163,-3.740969,-3.414143,5.848707,7.883463,-3.774715,-8.397233,0.908655,-3.881938,-6.412611,2.977192,7.224430,4.461007,0.772218,5.555688,8.379814,6.768368,-5.923260,-8.802256,4.614476,7.520438,4.823675,-6.021228,-6.998945,-2.577613,0.517874,-7.485705,-3.500057,-9.175434,-1.430294,9.613595,-9.165177,-0.104044,3.366026,3.678079,-4.744861,-4.204749,-1.722845,-2.696762,7.351735,0.043384,-8.109840,9.493830,6.836727,-3.730370,8.372076,1.126149,-3.757433,-3.176205,1.613217,-3.330307,-9.815852,4.896562,2.440266,6.479233,-7.775344,8.347659,-6.755413,5.393362,7.415206,2.097789,5.983002,-0.948965,-2.179260,2.698975,-2.420843,1.479732,-8.096964,4.582738,-6.558647,-5.230343,3.185940,5.137718,-7.643659,0.587113,-8.828749,-7.608815,-4.639964,-0.979713,1.052739,-1.396055,0.778580,-1.213478,-4.517937,-7.841116,-9.035251,0.678546,-8.049977,4.353229,6.938889,-1.499007,-0.606164,8.141058,-5.413746,7.898351,-8.497559,2.333590,-0.431114,6.613969,-5.081804,7.253255,4.154635,-4.610234,-6.864378,-6.035032,1.059143,7.958384,-4.837502,-3.331900,-9.441855,-8.498473,7.603138,3.101275,-0.030365,-7.131606,-5.115074,5.973931,-0.424398,3.463281,-0.267805,-2.050374,7.653041,0.491394,-7.173556,-8.543531,4.826161,3.195358,-0.923907,-4.549736,-7.730158,7.648570,2.201766,-1.028210,4.292863,-6.947697,9.587228,6.036456,-9.227162,-7.914741,-2.559649,-4.890428,-5.848484,-4.423262,-8.762719,5.115265,5.421231,6.376705,0.538213,-8.044189,0.300725,-4.838103,2.874809,2.523785,-9.684710,-5.615132,-4.304618,7.651691,0.279599,-5.140652,-3.226385,-5.399909,-8.841658,-6.258536,9.748250,-5.465524,7.827938,3.970479,-2.383962,9.552910,8.878183,5.720000,-5.446050,-4.932294,-8.567194,4.845286,-9.760718,-3.053152,4.922776,-9.373254,8.078916,6.232580,-2.665887,8.767575,-3.752579,5.039441,7.042524,9.142279,7.041384,2.698114,-7.109274,5.535798,-8.377402,-5.312085,-1.054394,-5.623660,4.664240,8.398198,-9.291335,3.552534,7.248669,-9.210546,5.680327,-5.371591,3.998797,0.402461,-6.864302,-0.846559,-4.122482,-8.858542,-1.344318,8.868754,-3.375406,6.502604,3.722736,3.763045,5.192847,3.271751,-3.813318,-5.704383,7.849109,7.941537,-8.074499,-9.515392,-1.755821,5.024712,6.999649,8.082402,0.232823,2.869156,8.992069,0.625666,-1.454254,6.266493,-8.423124,8.373777,8.120923,0.572172,-0.121719,1.333149,-9.778357,2.261459,5.024655,-5.804416,5.982948,5.720093,-2.807758,-0.635877,-6.005159,6.058635,8.275027,-7.364297,-6.170384,-6.348763,-2.075972,3.226910,-3.760844,-7.933643,6.251512,8.593588,-3.925577,9.152664,2.651640,-9.969384,-0.606626,3.505777,-5.299394,-4.686706,7.840656,9.287457,-1.590625,4.842945,-2.869986,-6.185475,-9.972235,-5.347414,5.896418,0.161810,8.956237,-2.267304,-5.065952,4.652362,2.853258,1.003404,-2.869053,-3.052505,7.212681,-5.510217,-7.145081,-0.056092,-7.255494,3.234353,-1.678441,-7.682006,-7.390515,1.150354,-2.495636,6.277723,0.971286,5.932724,-0.497864,-0.016809,5.891650,2.567889,-7.059088,-9.382852,-8.753971,-1.300279,-6.236734,8.676202,1.568824,1.813544,2.326686,7.188013,0.404033,1.206397,9.529743,-3.608562,-1.477563,-7.204152,0.446392,9.085433,-1.259689,-6.037581,-3.134003,-8.478045,5.093383,-6.458737,-0.757285,9.323890,-3.482203,8.189355,-3.739313,-6.539059,7.765578,2.124726,5.743286,9.184005,-9.000422,-4.820485,6.201940,-1.950601,0.905322,7.741777,5.798750,4.887613,7.776027,6.601758,-6.932003,-8.280108,-7.690331,-1.105103,-3.748928,6.002200,-4.813466,-5.751569,-6.094913,-4.262097,3.082061,-7.710922,-5.554208,-7.684570,-9.219499,1.672806,5.252607,6.153772,-3.635005,6.330934,7.374389,9.316476,-6.157952,4.428773,2.009321,-1.011981,6.491521,1.393510,5.341802,-8.926608,4.982759,-4.216090,4.306169,-3.690695,-0.266685,7.293081,-8.000995,4.813542,-5.010882,-6.907421,-7.717869,-7.098086,7.184610,7.157311,8.221880,-8.686247,5.825821,6.940456,-1.284438,-7.429126,5.426660,-5.669867,4.735318,-0.252958,-5.068527,9.933495,-3.952111,7.401518,7.657503,-9.668894,-4.697768,3.469811,6.641127,-8.371276,-0.129528,-1.861676,-7.439222,2.176435,-2.696159,4.189665,-0.750868,8.580514,-8.996589,-8.526923,3.896596,-2.096544,-9.903863,-6.017231,-5.922951,5.144368,3.067576,-9.416528,4.043124,0.846595,-9.302356,-2.979120,9.878007,2.877462,-0.295278,8.356537,-4.184487,8.917933,1.119954,-0.256228,4.975724,-9.317042,-0.346468,-1.339453,7.204179,2.402757,0.699283,-5.628747,-8.621799,-9.558378,-6.338917,-3.705858,-5.466953,5.409977,6.917170,6.896357,6.965626,-8.644653,7.552537,0.801689,-2.923436,-9.450532,3.604603,6.322499,-5.849327,-8.680100,0.481804,4.147322,8.425431,-6.987462,-0.502003,3.538562,8.686577,0.545769,-1.058087,0.912617,-4.233195,-9.396188,7.954085,3.577104,-3.516407,-1.625069,-2.560825,3.544732,-2.275607,0.428635,4.482126,-6.857915,-2.354637,4.742383,5.918917,3.261083,-2.449988,5.023052,1.009830,0.991332,-6.200967,-5.496794,9.725911,-7.802251,6.149601,8.824390,-5.036642,2.842454,9.273185,-0.209523,-5.994289,-1.436590,9.497247,-7.918148,-3.989642,-3.930991,7.498463,-0.803533,-7.436271,-5.341587,-9.865116,2.573762,0.631412,9.618619,4.183259,1.696184,3.897402,0.964254,7.366768,-3.123693,9.487641,4.707387,6.882488,-2.085123,-8.559561,7.409235,-4.208782,-6.479938,9.175199,-8.631808,0.136106,-4.640668,-2.651724,0.055470,8.945174,4.460662,7.917163,2.667010,-0.634958,-6.797968,-8.900512,8.461603,-4.628443,5.849199,1.179490,3.271415,7.781226,-0.665939,7.200669,-3.957340,0.125176,3.078401,-4.020986,0.701882,-3.944182,1.517341,7.837249,8.468778,-9.071113,3.700422,9.509851,-1.110479,9.069197,-0.398829,2.648392,5.884052,-9.273997,1.277733,-4.778627,-9.773084,-6.823648,2.307038,-7.377931,-4.044808,1.739961,2.705872,-0.340351,-9.232156,-5.085586,-6.703232,2.837244,-4.583303,-4.454356,-5.290991,-4.362622,-1.579922,-3.330437,-3.084912,-6.186763,-5.956342,-1.320386,-2.389327,8.843926,-2.813810,8.322559,2.312976,5.383218,1.710950,6.289348,-9.882062,-3.843501,9.333130,-8.066527,4.011716,-1.179019,6.656056,5.472860,9.111583,-8.492637,-3.727436,-0.889283,-0.133504,0.885581,7.151151,0.136300,-7.273275,-4.031075,-4.132780,2.540286,-6.459044,0.324327,9.575155,9.620617,-6.906826,-4.894664,-7.086954,-9.250985,-8.094771,-1.438975,6.070073,8.960619,7.624935,9.812833,1.439653,3.203533,-3.038267,8.580894,-1.014120,-4.692424,-6.312639,3.486485,0.942552,7.602106,-4.987244,3.699756,9.946517,6.949332,7.317684,-5.673083,-4.022554,-3.528423,2.135949,-1.745827,-3.902549,-6.447016,3.202611,6.799600,0.352271,7.756225,-9.211054,7.078064,7.218304,-5.536791,6.747099,5.563684,2.456404,-5.644399,7.773687,-7.095246,5.123580,-9.804318,-4.651661,0.488204,-7.873382,3.005891,-4.178351,-8.789201,-6.869486,-0.768090,-8.556375,2.703431,9.678886,-8.428631,-4.602968,-0.003531,9.857300,-3.047742,7.893296,9.705553,-6.831392,-6.799121,-0.973169,8.067655,-1.451125,-2.391084,5.626181,-9.460829,-5.151175,-3.548882,6.022801,-3.150556,9.279703,-2.737987,4.735388,3.047486,6.980786,-8.819844,-0.622589,-9.939990,5.180612,0.753989,-0.890200,3.570851,-7.984671,1.282155,-4.015771,-7.147945,-1.838485,-9.185229,4.798197,-6.777650,-5.371699,-8.622168,-1.203598,7.957403,2.843604,-6.389932,-3.606666,-4.303292,1.808605,-5.218661,-7.938516,-6.567254,1.045343,-6.909980,-5.576020,9.547476,1.741756,0.983738,-6.370570,6.358648,-8.738349,6.897943,7.465241,0.645808,3.385532,-5.117032,3.736870,9.321975,-5.236849,0.813508,-7.556396,4.916935,-9.695765,6.371646,1.063128,-8.202802,-1.989718,-9.758569,-0.385902,5.547409,7.037509,8.186551,-6.681679,0.077415,-7.721855,1.793399,-0.521725,-0.956711,6.718357,5.131242,-9.172666,-4.182128,-4.469253,-2.074734,1.414860,-6.676585,6.898918,7.748731,-0.910590,-0.984684,9.525966,2.558054,-1.879540,-1.692649,3.431094,-0.129163,4.160849,4.124371,9.220971,-5.277320,8.082967,9.661384,-1.216058,-8.656050,-5.203136,7.548323,-8.036238,2.888119,-3.653968,-3.030976,1.039943,3.687597,-1.934072,-0.114522,-3.346771,-0.584502,-0.530092,2.228432,-6.147229,9.479790,-5.855706,-7.941718,-6.620331,-8.602815,0.090171,-4.289879,0.605724,4.531133,-2.719709,-8.919716,6.511649,-3.758676,-9.362699,-3.733392,1.475068,4.268425,9.657072,-2.156885,8.685350,-0.174824,-7.307269,-2.840619,6.865152,5.543981,4.509469,-6.118679,-7.436584,-8.725056,-4.753102,8.456000,4.186801,-7.960143,-8.575498,-8.129946,5.893163,-6.413915,4.828325,1.955546,-6.584368,9.488156,-9.795303,-6.323707,-7.002365,-1.751860,-4.796016,4.779257,-4.577332,-0.585985,-0.648212,0.231759,5.296322,9.256335,-7.570232,9.791053,6.316359,-1.386863,4.903518,-1.469794,-8.848951,-4.721480,-0.360580,-0.064795,4.677401,1.883092,5.088198,3.882721,-5.509623,0.130207,-2.403239,-9.977576,4.858206,1.478496,7.530600,6.782346,-7.737025,-2.463744,5.088328,-8.536867,4.960707,-6.545212,-4.073665,-2.280881,5.344476,9.254389,-9.703949,6.210133,-7.359874,-8.127014,5.320521,6.319056,-4.210069,-0.651687,-0.284605,-7.170988,2.230442,-9.465775,1.994557,-2.759208,0.522884,-6.851996,7.774538,0.863135,-2.765220,-4.526315,6.895226,-2.871581,2.582188,4.718617,5.627428,-0.210695,3.793945,-9.693976,6.525792,1.558796,-2.919779,-8.702418,0.574485,2.308471,-9.064179,4.343435,-7.662399,2.049024,2.474578,2.105299,-3.636040,9.586957,6.443645,-2.788909,-3.875358,0.695527,8.158506,6.561490,6.155423,9.463839,-9.675272,-1.972189,-9.372604,-8.780825,-6.750413,-9.953343,3.779468,-8.538367,6.074529,4.084327,-0.168022,-5.498072,3.056014,1.716475,-6.016823,-1.719704,9.999527,0.342492,-0.170275,9.359357,-4.731477,9.634016,3.495804,-7.174117,1.412065,0.477165,-0.875175,9.378482,9.154762,-2.989572,6.353130,-8.793706,9.430763,-5.019038,9.205418,1.634460,8.803582,-7.465971,-3.823101,4.122284,-5.751344,-2.626262,-4.811421,-7.767470,-1.462280,-5.872111,2.515729,-0.935251,-3.622912,-7.031686,2.685692,0.476193,1.646541,8.009535,-2.577182,8.024931,8.377363,3.655574,2.827238,7.721531,6.751624,-6.171911,-4.995290,9.097520,7.005049,2.464969,9.460492,-4.461027,-1.348414,5.163250,-7.622938,1.403671,-7.994512,-3.165394,7.664550,7.621432,0.282037,0.471440,-1.206404,-1.094388,0.495539,-5.135673,3.354025,6.434896,2.219463,-3.170574,8.403689,4.919792,2.578143,1.693099,-9.893540,6.081199,-3.296572,8.746618,2.558279,2.044347,1.355113,-3.434840,-7.746812,-6.002397,-8.376281,7.377327,1.520896,3.072232,-9.996101,0.846690,9.503141,-5.637618,8.929444,-7.444771,-7.041166,6.162957,-6.741649,-6.085540,9.337287,-7.960490,3.528690,2.145342,-3.250906,3.540325,-6.619254,3.432595,3.641073,0.350245,-5.411614,-7.318248,5.590981,-9.920720,6.745716,-1.700240,-5.940654,-6.494361,7.343016,-4.817673,-6.149133,-0.133562,-3.821846,-6.149485,-1.601745,-5.440410,0.458481,7.674120,9.181800,-6.249456,-1.324855,6.388943,9.621623,-4.302149,-9.516283,7.537175,8.650284,1.179839,3.031020,0.775856,9.381260,-8.189531,-7.162559,-5.795908,-2.144712,-0.441743,8.259679,8.833221,4.279394,7.150183,-0.209524,-3.525453,6.529453,0.142974,8.910714,-6.042702,-6.475565,-7.214807,-1.930849,-7.971783,3.486575,9.635340,9.336775,-8.489586,-8.468222,-1.596306,-7.069596,-5.300934,-3.103341,-7.463304,4.012424,-0.379768,-7.533550,-5.368003,3.750107,2.620632,-6.565282,-3.992340,1.357514,-1.461174,-0.092338,-8.175652,-7.608699,-1.033338,-6.549986,-2.750655,2.214818,7.976413,9.992443,-1.746203,6.672162,-3.122510,-3.650733,4.660056,6.569931,-1.688977,-9.477912,-2.897799,3.832555,3.734080,3.276260,3.863646,-2.486972,-8.060012,6.922366,8.892486,-1.159988,-8.462638,-9.666095,-9.156486,7.175436,0.349499,3.057641,-4.330068,0.905693,-9.197860,-1.254595,3.969756,5.029025,-3.560338,5.743526,5.821107,4.387444,-7.306698,4.158771,7.672211,2.476417,-6.553874,-6.211048,-4.104281,-0.248136,2.523836,-8.195801,4.930639,-6.050657,-3.272514,5.781845,-6.782318,2.348855,-6.725861,0.306987,-5.133271,2.356837,-3.415552,5.901182,8.156741,5.997145,-8.970780,4.375181,8.208718,-8.686977,2.223311,2.166930,-2.273952,1.105132,2.087331,1.385202,9.480262,-6.512849,-3.663756,-8.989537,4.264992,-2.363632,-4.092581,-4.513812,-7.876738,3.528129,-2.928235,8.046591,-7.523867,-4.680972,9.764996,9.971681,-7.200054,-1.660898,1.174639,-9.910269,5.396041,2.008674,-9.033530,6.330447,-7.378349,5.708329,-6.933940,8.003214,0.790688,-6.820154,6.272149,4.892591,-9.129181,4.423473,5.814260,-6.088844,-8.967098,-8.404474,1.443748,9.589187,-1.365179,1.949854,6.943530,3.940409,-6.638573,-0.131679,3.638660,5.587540,1.674883,-3.062479,-8.516344,2.570084,-0.563027,9.774718,-1.823200,2.449715,2.976102,2.314418,0.312047,6.177774,-2.695229,-7.490246,-2.950809,7.325814,-5.897444,-2.777149,9.710657,8.666491,9.013173,5.013350,-4.645551,-3.157111,9.966163,-0.642166,5.204435,-5.735536,6.853524,9.784937,-9.125098,-2.505618,-6.323612,7.056754,-0.333461,1.015078,-7.856574,0.213139,1.440708,-6.743561,2.695607,-2.479720,7.606003,7.610157,1.209661,-5.863166,3.591866,-0.395106,7.603730,1.260069,-8.898600,6.313227,-8.823768,7.064685,-3.682980,-0.802324,9.812956,-2.696451,-2.656351,2.231053,0.845129,3.400765,-0.788456,-5.729059,-6.214122,-0.809322,8.131468,4.663462,-9.263524,0.181113,-0.581157,2.902347,-2.049310,-8.950955,1.429624,-1.160456,4.127437,1.657627,5.601998,9.616977,-1.200739,0.323506,8.442160,1.463732,9.615333,2.116699,-6.984828,8.367987,-2.155267,8.092969,-3.196580,-5.823420,-0.009749,9.744895,-7.495504,8.667224,-4.804307,-0.485164,5.909186,-3.994863,-7.418784,-6.288123,-3.175066,-3.015038,-0.784793,-7.922410,7.847425,-3.546209,-7.403469,-9.319454,6.598052,4.241226,-3.560199,0.412027,7.585195,-5.228662,6.541703,6.700748,8.074007,9.671795,5.116418,-4.058693,-7.092368,-9.313282,-6.997211,8.359114,-4.794721,-6.179418,-1.929350,-9.620765,3.023489,-2.686377,-0.391230,-8.308713,7.824099,4.886910,2.086438,0.716171,-1.557767,-1.282329,-3.185756,-3.281642,9.190597,7.619515,4.337965,2.992039,4.240934,1.352563,3.346936,9.672907,0.346780,-9.781061,-4.770393,6.148447,6.758739,7.735866,6.134953,7.325310,-3.031112,5.149454,-3.867465,-0.050895,-4.856717,4.155700,4.500395,-4.890649,0.251798,8.711531,-2.826795,1.363100,3.627587,-1.238556,-7.234613,5.414222,-4.255804,-9.469193,2.939277,-0.616036,1.392936,-4.444595,-7.063631,7.342432,0.893348,2.169904,4.600515,6.725843,-5.112327,-0.288869,5.876473,9.246729,-2.029191,0.999880,1.881504,0.738539,1.499621,1.442766,-9.702049,-6.619806,-7.206679,9.603636,-8.531899,-5.393955,-6.936629,2.578623,-9.040719,-2.231175,5.058650,-2.099403,1.063897,4.193123,9.782552,0.253299,0.927374,6.412226,3.574840,-6.583336,-3.145918,-4.400577,9.380642,-5.200612,5.743072,-8.420785,-3.533635,2.665451,-8.235379,6.936842,0.391748,4.580321,-9.968760,-1.476535,3.077598,2.377210,9.738473,7.993109,6.296500,-8.983324,-8.380270,2.534360,-0.437357,-5.632570,1.927991,-1.017864,-8.981608,-4.488007,3.021701,7.987478,9.775621,-2.771993,-2.944840,6.706670,2.100754,-3.296473,-0.800266,5.757109,-5.919758,7.890462,7.521662,1.400303,1.379083,-1.705100,-9.933439,6.090625,-2.177506,3.344682,7.511800,-3.580601,-2.363352,-7.556440,3.097763,9.120607,-4.870845,0.387954,1.037896,2.274024,-7.891383,7.408716,6.833372,-4.277583,-1.792198,3.009100,-9.250603,-7.772099,-7.180158,4.363797,-0.647380,-2.567004,3.262091,-1.738574,-4.055706,7.877138,8.344104,4.129552,-8.043713,-7.690521,8.247450,-2.492012,-0.609980,7.367413,-4.975581,-6.327707,6.059001,1.848720,-7.607837,4.772195,4.471896,-3.400665,3.461647,-0.797850,2.636116,-4.828960,-3.625565,5.353689,-7.773268,6.524352,4.266569,7.540829,-7.192746,-1.177607,3.633577,9.015711,-2.540527,9.030688,-9.622241,3.087069,0.960950,-5.483709,7.009854,-2.017556,-7.502249,-6.349770,6.814569,6.684411,-3.385803,-5.072540,5.625625,-1.056909,9.862930,-4.259167,6.527644,-5.131159,6.265923,-1.095810,-2.588166,-4.637649,6.880777,-3.733155,2.659848,-1.071987,3.875632,0.804241,5.165148,2.339595,1.076672,-3.112543,0.224915,5.670223,7.046856,1.468153,-9.547047,5.597609,-0.983388,-4.146674,2.513526,3.699821,-6.152405,0.683593,2.323796,-9.995863,-2.965642,1.126918,4.759576,4.538210,3.958880,-2.770217,-4.196424,8.864500,-1.443219,-4.774610,-4.354562,-0.438231,-8.787219,-0.538959,-0.355643,1.035756,7.135026,9.139152,8.370247,-9.714474,4.351632,2.024413,-3.824458,1.484679,-5.731605,-2.155469,6.656244,3.963478,-1.728017,6.782408,9.553803,-0.730325,-7.150833,7.269901,-4.932193,-0.142132,3.917733,6.850079,-2.369091,-0.732863,6.109958,2.549013,1.010739,-9.393942,9.288365,7.038755,-6.058437,4.496733,9.295898,7.314875,-5.381932,5.628432,2.809058,9.801647,4.646229,-3.291009,-7.734295,-1.881546,0.809130,-7.470302,-0.493908,6.140091,1.199958,2.873057,1.897097,-4.657227,-3.308363,6.833644,-1.307243,4.367452,-3.105753,-5.390341,-4.759962,7.024006,-7.135239,-9.936671,0.725658,1.014483,-0.298320,9.671145,1.367869,-4.730478,6.162102,6.679494,-0.024551,-2.788905,5.730319,-1.417565,3.082575,9.877799,2.971793,-9.174816,2.037554,8.858869,0.302861,7.446670,-7.176929,-1.244412,-9.176064,2.519802,7.279470,5.172393,1.224114,-5.209943,7.325229,-4.642308,5.408998,8.244864,-3.330576,-3.727226,8.724396,7.935741,9.964128,-2.450725,7.426245,8.091508,4.348279,3.748989,-8.153941,7.932032,4.770041,-1.590154,-6.652882,0.690194,-6.396283,-0.951044,-3.353884,0.868798,-4.818143,9.454136,0.395356,-3.631442,3.482348,6.523062,0.006635,-4.520647,-4.791014,4.252442,-4.605124,-4.384188,-9.349027,2.530924,-8.393741,9.220968,-7.674682,-4.101953,1.280167,-5.218412,2.616953,-3.104316,-1.168707,4.142066,4.250575,0.675104,-9.015664,-8.122785,7.051325,0.176968,-5.267726,-2.299104,2.492718,-6.834224,0.161368,2.478080,6.833331,1.075154,-0.796774,-8.453546,7.516197,-5.163766,6.844543,-7.134113,-2.479348,-8.180447,-6.571570,7.958125,-9.725211,-4.006543,-1.000774,-6.639004,8.873964,3.078760,-6.940677,8.203405,2.707687,6.839637,-2.683757,5.003096,3.270893,3.154940,-7.167570,8.744116,2.560723,-6.463911,-5.594535,8.822714,-5.930836,8.793081,-0.917719,-6.148963,-9.937505,1.524247,-1.028334,5.790995,-6.716250,4.333503,1.939745,9.746981,7.994898,-6.747368,-2.493817,7.897424,-7.754189,-8.838179,-9.242673,6.313198,-9.006329,6.976177,3.057771,0.689482,-0.579837,0.384484,0.780031,-6.033817,-4.583431,-0.599005,-4.710606,-6.647719,5.710211,6.028553,5.661053,-4.080825,6.206752,-0.732429,6.006051,8.680314,5.763899,8.318734,9.025424,6.387811,6.881695,4.823680,9.505127,-3.595360,-5.115080,-4.931424,-0.740552,6.072005,8.031288,4.454336,3.958560,-6.986878,0.060706,-0.470137,9.914031,-0.167121,9.462845,-7.989419,2.825577,5.973925,-3.115776,-7.038702,5.568350,4.800006,2.843588,5.747071,7.991670,8.834217,2.681915,0.852989,1.383583,6.044144,6.069492,-5.952618,9.714810,-3.202357,9.106825,-2.318581,1.527562,0.279542,-0.213138,1.412801,-5.853226,-8.019912,-4.671245,-2.529367,-2.518421,0.937550,4.428960,-8.180398,3.157602,7.538239,4.768565,0.195508,4.986892,-2.017928,3.635688,3.475984,-1.972046,-8.154715,2.455969,7.568590,-9.134932,-0.906431,-2.057825,-5.298028,7.935763,-5.143062,-1.368732,5.015640,9.269258,4.746395,-9.982825,-3.739020,8.585249,8.670741,-9.210339,-5.212446,3.449354,-5.201707,6.347346,-4.372140,-6.451743,-8.554556,-7.352207,-6.080284,6.963567,7.383635,-9.107628,-5.472030,-7.827775,2.576883,-5.994318,1.134451,-5.966349,7.852335,6.483447,-4.924894,3.583478,-5.059395,3.014326,1.233743,-7.123140,-0.056061,-7.207024,-9.224708,-5.978489,9.861786,8.534234,9.207222,7.072145,-6.646449,-1.841871,-7.194804,8.756530,4.424497,-4.548553,6.536501,6.258614,8.113313,-0.573572,-9.455974,7.446893,-7.409180,3.946389,-8.292363,-6.060624,9.935725,-0.072430,-8.387131,-1.140871,-8.977905,-6.824935,4.513500,1.896542,-4.011901,3.932224,-0.345246,-1.207980,1.922780,-4.097356,-3.221470,-7.896044,4.149377,-3.779503,-6.755861,-9.234614,8.628141,-8.208332,-6.173638,1.198027,-0.093521,-9.717464,-8.997056,5.791375,-5.700645,2.448654,-2.475770,-3.132669,-0.674181,-3.876679,6.884484,2.067113,5.109255,0.098537,8.903596,-2.834694,9.663420,8.807224,-7.414364,-4.808149,-0.600531,4.464740,7.819926,8.913976,-9.517064,4.101792,-6.874994,-5.109459,-3.118125,4.103608,0.829114,0.873921,-7.604516,-9.307204,6.175779,0.204172,-9.784685,4.154778,-7.804834,-5.648418,-1.453047,-2.078688,-9.310061,-2.018694,9.111651,1.382190,-9.677872,8.662164,5.649298,0.649318,-5.173956,-2.175121,3.928549,7.655894,-1.214975,6.707130,5.346170,0.863009,-1.437820,-6.945250,-9.175107,-2.946357,6.506867,5.751632,5.960561,9.323512,-4.374350,6.089809,8.214915,8.063784,-9.623397,-1.358087,9.789503,0.461466,-8.386671,7.936663,8.907551,8.024481,9.666333,6.558891,0.803533,8.527540,8.695145,5.823676,0.148689,-5.419269,2.629581,6.072071,9.825427,3.234802,-2.722839,-3.882048,-0.845744,-4.429792,-4.923986,9.127777,2.709344,8.068664,8.534933,8.533456,-5.229088,-8.026474,4.211590,-5.360988,-6.373345,-6.125442,-8.644494,3.161068,-7.156243,-0.028865,1.994488,-1.678406,-5.130921,1.757426,-2.649106,-4.180878,5.539713,4.844961,-2.327921,9.797173,5.705185,-8.049377,-2.871455,-9.662356,6.199383,2.584255,-9.081355,1.408175,-5.659642,-0.296689,-4.649837,7.642050,1.283683,-8.046904,-5.634710,0.075758,5.787422,2.865405,4.837857,-1.372726,-8.344418,4.931832,8.311593,-7.640543,-7.498442,-8.738319,7.148078,-5.709751,-8.131095,5.072185,-8.903693,-3.175443,-7.390295,0.840455,-8.315611,-7.025466,9.666827,6.816605,4.755998,-0.545926,3.423957,-8.393123,-9.323007,9.769288,3.186919,9.370771,5.175838,0.539188,8.928717,9.596571,-5.433924,7.372234,-7.158838,-3.364619,-5.727477,6.635933,4.559547,-0.053930,-7.267633,8.281905,-6.216963,2.817319,-2.489526,0.259537,4.880040,6.374442,5.293415,1.815303,-7.378677,1.606509,6.540782,-4.127354,-2.259028,-4.930044,-5.588028,-0.417648,5.510554,4.783668,-8.215724,9.680558,2.120171,3.584300,2.086544,-8.145916,-3.171644,-7.212803,-3.450744,-6.035583,-2.647307,9.227304,-4.991831,3.418622,7.625172,-9.169651,-9.682575,4.201064,-4.602338,-6.268123,-2.716538,0.893272,-8.903203,-5.840679,-7.912885,8.775530,8.203789,-7.006221,-3.742921,2.043792,-7.381025,1.165368,-0.363882,-0.442828,3.261890,-8.248248,-8.837030,-0.319484,-4.090380,7.144376,5.452335,7.473352,-5.255951,3.202401,8.916717,-8.755628,-6.575410,-2.850146,3.660014,0.994402,1.795922,-5.396367,-2.821123,-8.603013,0.080135,5.369348,-3.308684,4.451740,-0.368538,2.964822,-5.418963,2.157215,1.992391,7.660458,0.977195,7.107319,-9.210756,-4.840004,-3.535233,3.932136,-2.187318,2.470807,1.039707,8.026391,1.996980,-6.296115,6.689577,-6.861535,5.972582,3.611343,-5.975449,-6.117646,-6.657940,5.710563,3.035969,-1.651896,-3.956717,4.489493,-6.012153,1.582427,4.610660,2.980415,-8.489705,-9.199711,2.282934,-9.375344,-8.554944,9.172863,3.511657,-6.200880,2.808163,-0.072389,-3.603815,-3.832649,6.921945,-1.497112,5.232421,7.098468,4.886160,4.108279,3.528751,-5.389638,-4.779548,-2.803181,4.673603,2.666648,5.458625,-4.769064,8.563174,-5.492179,-8.983462,3.960676,5.466562,5.551742,-9.023644,0.617631,-0.524225,-3.785127,1.631162,-5.138368,8.732594,-1.482728,-7.371550,-0.164976,1.738610,-0.410956,6.665976,5.546121,-5.519014,3.896898,3.621274,-9.358046,-1.277049,9.626936,9.473152,-7.882730,8.787087,3.086021,5.592345,7.798471,-5.537831,6.454365,7.919747,-3.773520,7.148786,0.445487,5.145839,9.328232,-0.882990,5.371392,-1.302681,-6.407764,-3.563830,5.139525,1.453077,-5.270815,-7.190393,0.535286,-7.159988,1.293498,4.030841,1.962603,-8.584301,-2.937979,4.834021,-3.858500,-8.606115,6.222184,-1.172771,-8.537928,3.939316,-4.466765,-3.334685,8.508072,4.192975,8.287848,9.757151,9.820516,2.841927,-9.766114,-8.502891,-8.394934,1.370351,2.807582,8.098128,1.963300,3.393551,-3.139668,6.305125,-4.667592,1.870895,7.979221,-1.760300,-8.286812,5.529469,-3.897805,-5.998997,-7.832131,-9.278983,6.763771,1.713960,-5.357005,-2.724968,8.258649,3.089528,9.637443,3.306419,9.636061,3.284484,5.454047,1.265771,-2.859477,-8.415764,5.544874,3.051988,-1.223788,-4.516526,5.713343,-4.355496,-8.037815,-2.598885,-2.352666,2.481936,-4.127176,5.351002,6.261495,4.071899,-4.823297,-0.266145,9.670178,2.708746,-5.229380,-1.516730,-2.314207,-6.597512,-4.579455,-0.473007,-8.539023,3.796831,8.259874,-7.763706,7.514733,-7.604743,-2.898740,2.267230,-7.961745,7.907289,-4.604995,-6.180799,-1.456626,-2.340361,-3.136026,0.393822,-3.140280,2.806670,-4.314497,-0.241759,4.071230,4.449945,9.563038,2.299777,0.786816,-9.132804,8.051179,3.475180,-7.117849,-2.749399,-0.159850,3.588198,-7.756404,-0.281357,6.229776,-6.614781,-4.500251,-2.752516,2.220952,8.859566,-0.124098,-8.793462,5.459210,-5.894432,3.349242,-8.171817,-5.224690,-0.159167,-4.722401,9.146144,3.786641,-3.445547,-6.497851,1.885621,5.362316,-5.649135,5.036883,6.476046,-8.180283,-0.603807,-9.602765,-7.328791,-2.490720,-0.413509,6.405693,-8.552047,2.944174,-8.599934,7.674673,0.635878,9.859099,5.864507,7.676898,0.401137,-1.477304,5.380601,-9.173297,5.718127,4.494837,6.741851,-0.534697,5.854699,-6.517951,6.076725,-7.641004,-5.390096,-9.024150,-3.319815,-3.139546,-9.234181,5.527591,-9.629560,6.658926,-9.813916,1.487396,6.033330,-1.644124,2.194661,3.344279,-8.007107,-1.698097,9.612459,-8.206201,-5.559021,6.825242,6.905050,-2.644745,-1.982385,-9.437320,-0.411207,-4.119773,4.724873,9.826472,2.982623,7.536826,-3.509264,4.582639,-1.976159,1.326874,-0.628953,9.204112,5.054670,9.314987,8.148139,-2.469618,3.217627,-6.067549,6.218625,-1.214162,-5.655468,9.531843,2.617156,-0.605020,-0.998849,-3.805194,-5.658453,9.600271,3.132599,1.694640,-3.428253,0.312660,-7.793242,-5.374892,7.953246,-5.387726,-5.556823,-0.953367,-2.440009,7.186406,-4.875494,-5.498629,-9.849492,-7.237464,-9.902758,-3.699944,9.710874,3.413572,5.413780,-0.933979,-3.844341,-9.882865,-1.969124,-5.176656,1.621339,3.160743,0.748052,-0.050438,6.313456,0.469855,-9.576436,-2.557436,4.550336,5.887847,0.218476,9.741653,4.615589,-2.017046,-1.478572,-2.236692,3.151568,0.723407,0.749900,-4.496998,-5.881655,3.755750,8.829758,6.972858,1.301825,-3.370058,-4.330408,-7.747870,0.091887,7.081032,3.420189,-8.623479,1.666608,3.964588,1.798954,-3.099101,2.264504,1.272245,8.003595,-6.883064,9.807047,-0.435171,-8.893787,5.442296,5.509416,-7.185298,2.334992,9.813983,-4.250350,2.029452,-6.422237,-9.062425,9.912854,1.244727,-9.785685,0.181258,-0.730457,1.353284,-1.607608,-2.100524,4.331823,-6.267608,7.069486,1.966821,-1.859945,-5.812103,-5.152515,4.267299,-8.702124,9.902152,-4.856030,-6.071329,-0.143510,8.869356,3.985698,-8.480896,-2.675800,7.810163,6.411183,-0.837963,8.401254,-0.525591,4.751957,-1.959504,-4.829964,-9.434974,-6.392901,4.399620,-7.736262,-8.283442,9.495546,-2.622149,3.885426,3.360463,-1.760780,9.944123,-7.763910,-4.207926,8.774050,8.472115,-6.479974,-4.896893,5.460892,6.565031,-4.558366,0.202048,-6.241568,-4.672131,3.895990,-1.257735,4.258336,2.905032,-5.234901,3.410171,-7.562681,5.454133,-1.717135,-5.301815,-3.503318,9.264608,2.252866,-1.936514,-0.130819,6.553299,-5.384188,0.492032,1.813185,-0.816289,-6.701300,3.925424,-3.068150,0.785431,-3.539226,-4.820147,8.980546,-7.069330,-3.685134,8.386988,4.099244,-4.899552,-4.494060,7.399624,0.920361,9.560119,2.855501,-8.883220,-4.078734,-1.993393,6.288713,9.187140,-7.880107,7.991024,-2.552471,6.882515,-6.217194,4.961113,8.454483,-3.918519,-1.927655,8.130633,0.215726,-1.649302,6.337889,-4.820497,3.697278,-5.951095,5.378120,9.010173,-4.614860,6.788924,-0.141812,5.831132,5.839699,-4.157748,-1.797754,2.211389,-3.695528,3.761042,-0.079280,-0.783289,7.066616,1.948233,2.032908,-6.905595,2.611121,-0.720525,-5.823991,-2.738921,3.746833,-7.266778,-3.575339,0.621094,5.473376,-6.893995,1.665909,9.235989,6.144540,4.365193,0.185227,-9.248518,-0.130248,7.413108,9.752364,-3.936181,-7.922400,-7.904261,6.465461,2.874722,-9.063984,-5.344622,4.950780,-9.317285,3.673933,3.561067,6.811895,4.767709,-6.130042,-6.553333,-4.409948,-4.779180,1.186615,9.122886,0.834591,6.476759,1.052002,9.358145,-5.519298,2.146044,9.995781,-6.350668,3.675670,-8.968266,-9.517844,8.532354,-2.718778,-6.441026,-3.852969,-8.605796,-8.315539,1.329988,8.563220,-5.391312,-9.917032,3.044578,-6.884044,-9.779655,-1.255139,9.774116,3.629194,7.356098,5.935517,-8.139709,-7.227619,5.493829,-8.106556,-4.930177,6.964330,9.657060,-1.109375,7.835034,6.273533,-9.153059,2.165319,-0.230554,-7.725741,-0.863700,0.127847,0.097494,4.087812,6.083088,3.664568,4.474679,-8.750409,-5.016342,-8.469630,-8.237046,0.859821,0.120739,-6.691181,-8.758237,5.296268,-4.395993,3.687721,-0.490891,-6.191018,-0.409883,3.438902,-0.463187,5.268685,3.363495,4.140877,6.104916,-3.539577,6.691487,-6.373015,-5.394979,-8.516077,9.422032,-2.219470,-0.735915,6.565565,3.805435,-3.638503,-7.390318,-0.015593,7.609123,3.264482,9.107593,4.447146,9.326364,-2.069460,-5.349896,-1.484448,-4.700933,8.847534,-1.822582,1.130159,-9.886622,7.496034,6.437940,-6.767622,9.835863,1.274377,7.549681,4.176816,7.223560,-2.844692,-9.668771,8.747554,-0.075499,1.566791,9.894067,-9.782804,1.905613,-7.225541,3.229400,4.030839,3.726007,5.511267,-0.099010,5.751402,-0.902344,1.384580,-9.241636,1.082772,5.468128,7.437448,-2.679342,-1.926499,-5.532608,-8.212398,9.447142,-2.557099,4.208724,-9.619012,8.958594,1.160229,1.571350,-3.628799,4.986241,-3.343056,5.228185,0.215733,1.077199,9.084306,-7.169706,-0.107246,0.408235,-0.686942,-8.474531,-6.341542,-8.145384,-6.878060,-0.835605,-7.587294,-4.558825,5.201077,-3.472547,6.561007,-4.780586,0.455033,9.317129,7.824601,7.175474,3.754151,-5.777671,9.767440,8.537832,-2.432831,-4.624938,7.606633,-2.820741,-4.930255,1.536458,-3.478704,-7.863091,-2.909153,1.529848,6.095757,-9.348914,9.210130,-0.469571,0.214819,-1.558691,-0.361688,-5.288699,3.298987,-8.432632,-7.810572,-5.811504,4.938151,-0.574379,-2.014573,4.525242,-8.958851,-4.826599,-0.437420,-1.328202,-3.410839,-7.198600,-7.033199,-7.646533,0.821076,8.504790,-1.523593,-1.549521,4.385565,6.608611,2.666708,5.917320,-1.794832,6.897034,-7.631968,3.736077,-3.383256,4.495699,-4.071614,-6.382973,-5.010263,0.524479,0.113712,4.290835,7.484423,-8.524597,5.374636,-6.392132,9.403357,0.005069,-3.620294,-2.743025,-2.851114,9.652912,2.458018,-8.962477,0.653385,-3.825234,8.590980,0.015713,0.006237,1.460260,4.712545,-5.666163,3.262974,3.808247,-0.052404,-1.238572,4.717786,-1.641737,-9.983816,5.134366,-8.556353,-7.317433,1.724964,-4.581765,-9.069865,8.257238,-6.758813,-1.634541,8.857329,1.613150,-5.739373,-6.950334,3.838088,-8.018099,9.894169,9.336063,-6.841260,-9.284204,-8.916315,-2.653374,-8.749160,-7.734954,0.310524,0.300154,-9.033482,2.866028,-9.862254,7.112410,-6.984461,9.479766,2.862201,5.704889,2.604230,3.754720,9.059247,-6.135257,4.870135,-9.425615,9.973303,-1.132035,-0.385734,-8.643642,3.714650,-6.601163,-8.097675,-7.161501,-8.367162,4.781947,7.740040,7.677130,-9.668858,-2.779884,7.007961,-4.621114,-0.164556,-7.403447,-7.060746,-3.119753,-1.186344,2.198590,-7.860523,-2.947753,-3.636486,-0.632936,-5.322777,-7.132335,9.909289,8.539966,1.269029,-2.557816,-7.362117,-6.857228,4.483556,-6.450068,9.498061,-7.943245,8.755513,-5.441100,-9.655877,2.459084,8.688367,8.086782,9.684853,1.524104,8.007552,-9.325727,-7.081393,-8.158357,7.050337,-1.230880,8.597278,8.448094,2.770159,-9.373084,-9.973306,7.870968,3.533727,0.213016,9.381505,8.890541,-3.764200,-9.078037,-8.425846,-9.122097,0.309067,-4.975430,-6.584774,-5.949089,8.550518,2.387918,-9.754864,2.488771,-5.193941,-4.579995,6.666028,-1.115049,-5.048254,7.157676,5.902387,-0.996639,-2.903518,7.599612,-3.951809,-9.699850,-8.257651,-5.187772,-7.307682,-3.868645,-0.743210,-7.310870,-8.985353,8.298442,9.071714,4.560558,-9.765372,-3.668010,-1.567251,9.092299,6.438971,1.699641,-9.188582,-6.511523,3.461587,9.760885,-5.607343,-3.214458,-2.315565,8.619492,-5.861024,-2.386386,-7.559773,8.773693,1.077726,-9.158087,-8.312742,-8.524773,3.107720,-0.688407,-5.260806,-9.747656,4.176072,8.584560,-0.764598,-6.745628,-7.008722,1.512111,9.410596,6.635674,-9.154131,6.059172,7.975045,0.756027,-5.707033,-3.676798,4.058474,0.535229,4.782210,-1.132313,7.993023,-3.804705,3.670969,8.252896,-5.746833,8.388657,-6.062562,1.438360,8.746364,-0.813840,-8.161480,-6.440638,9.198077,9.732373,-0.490144,-6.725798,-7.415264,4.183398,-8.495077,-5.762857,-5.582274,9.441465,-9.083304,-3.236869,4.481204,7.541149,8.280200,0.026340,-3.145667,7.168300,-7.282683,-1.148744,-0.386015,6.126742,-3.659447,3.029465,6.876977,0.729971,-2.355038,4.646317,-2.738971,5.657692,-6.326498,-3.958497,6.749144,-4.930023,7.128552,-3.474681,-7.763113,1.602816,2.551443,6.038156,1.826051,-4.641137,1.318948,-8.293687,3.548618,1.058311,-2.303088,-7.602400,-8.098363,-0.743579,8.246831,2.397809,-0.586914,6.409510,-9.231247,-2.844935,0.485938,4.704525,6.558315,9.433407,5.099656,-6.024097,-7.076445,-1.034288,2.286305,8.078708,3.429598,6.472459,6.539452,-2.362923,7.466266,8.740068,0.584901,5.922610,-0.077065,9.007293,-4.248444,-0.207484,-7.640160,3.932020,9.298958,4.210769,0.053386,-1.417508,1.745327,-7.559873,0.118633,5.093081,-9.161844,4.344092,4.415009,6.358869,5.291925,4.615938,-4.633926,6.099522,5.868034,-3.862742,6.283183,5.466506,3.647749,-1.692390,1.825000,-0.124048,-3.874631,8.099528,-9.210138,4.147506,-2.241644,-8.352634,3.576568,-1.240156,-8.063682,-9.281176,8.635156,-7.731165,6.977436,5.686268,-2.836229,7.485733,-2.939699,5.141247,2.487024,-7.256799,2.698084,-9.462037,-8.198450,1.621293,6.256489,3.333477,2.549258,-1.072222,-5.871170,8.483151,9.980901,4.298958,5.768322,-5.909091,-9.048373,-2.279579,8.648165,-4.423541,8.544079,-0.902856,8.995111,0.363081,3.220402,-6.595385,-7.365623,7.242753,-5.483694,1.223934,4.232086,-4.412878,-4.371083,6.259395,6.707986,3.783668,4.483127,9.936973,3.584928,7.732961,-2.556577,-7.027439,4.878162,-9.297200,5.326645,-0.905512,-1.774168,-3.660015,6.980928,-0.759620,9.094075,-1.097619,-7.809207,-1.799344,-9.053894,-4.386403,5.084699,0.879956,-1.207297,-3.699692,4.999528,-2.303864,5.645057,-7.751851,-1.779765,3.321265,9.369930,-7.550604,3.454371,7.128734,-5.005281,2.628000,5.884443,8.345736,-9.418632,6.525378,-2.976926,5.667567,-6.254781,-5.658300,6.397853,-4.731725,4.841482,-1.654314,5.770580,3.504440,5.272508,0.947717,4.664418,6.607621,-0.661058,-9.939033,-5.844310,-7.454004,0.814703,-7.243101,-1.590429,5.445658,0.778545,3.826255,-3.031233,1.627488,6.794910,-3.857085,3.180747,-9.902144,-6.510645,-6.596570,5.627497,5.934190,3.690719,9.566537,-9.501276,-9.124742,-0.547318,7.755339,-2.780324,-6.642664,4.790155,-2.604040,-8.193303,1.093330,3.376200,-3.442220,-8.965308,-6.206020,8.540186,-9.230572,-5.744583,3.325865,-3.705536,8.043634,2.488208,-1.545458,-4.047605,1.890740,8.089062,1.535743,-0.613412,0.782685,2.882574,0.698236,3.201036,1.238522,-9.642333,-2.001236,1.869684,0.631460,-0.639464,4.351275,-7.586024,0.324194,5.818957,8.356731,-8.240296,1.497603,-5.491922,-0.518817,-7.029965,8.269301,9.043633,0.200144,-7.729324,0.598009,-2.589347,1.992200,-0.060791,-7.752823,-6.680019,4.542323,9.367972,-6.958695,6.799677,0.523611,-0.968758,-6.333346,1.172727,-5.277126,-7.492826,-4.420799,2.182616,-4.031340,-3.730869,3.024412,-1.285914,-9.002985,4.980722,3.396360,2.990399,-5.959386,0.203971,1.134054,-1.366179,-1.814641,-0.775336,6.029727,3.613128,1.328366,7.598238,-5.485240,2.767367,5.837399,7.906406,-3.937357,5.107365,4.080986,2.685724,6.739724,-1.166281,1.808583,-2.396835,-3.502375,-5.268754,-0.820597,1.986924,7.625895,5.618811,7.203484,3.394438,3.798411,4.152438,7.572527,-7.319807,-2.776232,8.577969,9.735635,8.550852,9.838331,1.928179,4.625346,-4.122423,1.673659,3.802516,-5.472243,-2.289417,2.813710,-6.932426,3.876058,-9.430555,-8.817773,5.534320,4.489919,8.077633,-7.779786,-0.794970,5.903225,-9.782285,-8.603995,-8.885198,-6.522253,7.312221,-3.155582,-9.504046,-4.421441,2.932402,-9.577945,-3.870883,4.786108,-3.107853,-2.017307,6.753113,2.208454,-0.536995,9.365762,9.106733,-6.118530,-5.646073,-3.677174,-2.898651,4.272067,2.805629,-4.973048,6.448848,-5.338618,9.661968,8.837743,-1.013047,-1.127050,-9.003003,1.394093,1.687748,-2.197922,-5.749049,-1.785145,4.654235,1.555405,-0.908498,-6.047832,1.578862,3.345439,1.110339,-0.233440,-4.625593,0.042879,-6.638744,-7.722572,-9.916089,5.405178,2.341445,5.708315,5.017505,-2.922402,-9.524066,-8.013625,3.663892,-6.032998,-1.481668,-8.475857,4.213987,2.144718,0.011874,8.042836,8.525405,-9.384999,-9.658282,5.115169,-8.250930,5.890604,8.904494,9.813945,-1.078904,9.902680,-6.079022,2.187107,3.145206,9.038032,-8.308592,-4.204168,-1.065471,-6.417975,-3.804297,-1.306505,1.125234,8.901356,4.839143,2.302328,-7.973532,-1.184662,4.231324,-5.186158,9.322384,2.977203,-5.475779,7.909134,-9.753785,-2.562549,8.923591,-1.512024,-3.939746,7.573471,-1.089623,8.063928,-3.702680,7.541478,0.834859,-1.057617,2.903963,-8.679719,-8.238780,-5.551838,-0.497774,5.001448,-5.025599,-8.228971,-2.188719,-7.699938,0.930540,8.177124,-7.882323,8.240668,3.603366,-7.862137,0.534066,-7.279001,-1.035924,-0.956263,5.157134,-4.487241,5.116236,3.583682,6.045010], dtype = "float32")#candidate|3786|(7800,)|const|float32
bop_3787 = relay.floor_divide(const_3782.astype('float64'), relay.reshape(const_3786.astype('float64'), relay.shape_of(const_3782))) # shape=(7800,)
uop_3790 = relay.sqrt(const_3782.astype('float32')) # shape=(7800,)
func_1626_call = mod.get_global_var('func_1626')
func_1627_call = mutated_mod.get_global_var('func_1627')
call_3792 = func_1626_call()
call_3793 = func_1626_call()
func_2894_call = mod.get_global_var('func_2894')
func_2895_call = mutated_mod.get_global_var('func_2895')
call_3800 = relay.TupleGetItem(func_2894_call(), 3)
call_3801 = relay.TupleGetItem(func_2895_call(), 3)
var_3817 = relay.var("var_3817", dtype = "float32", shape = (7800,))#candidate|3817|(7800,)|var|float32
bop_3818 = relay.mod(uop_3790.astype('float64'), relay.reshape(var_3817.astype('float64'), relay.shape_of(uop_3790))) # shape=(7800,)
output = relay.Tuple([call_3773,call_3780,var_3781,call_3784,bop_3787,call_3792,call_3800,bop_3818,])
output2 = relay.Tuple([call_3774,call_3783,var_3781,call_3785,bop_3787,call_3793,call_3801,bop_3818,])
func_3845 = relay.Function([var_3781,var_3817,], output)
mod['func_3845'] = func_3845
mod = relay.transform.InferType()(mod)
var_3846 = relay.var("var_3846", dtype = "float64", shape = (660,))#candidate|3846|(660,)|var|float64
var_3847 = relay.var("var_3847", dtype = "float32", shape = (7800,))#candidate|3847|(7800,)|var|float32
output = func_3845(var_3846,var_3847,)
func_3848 = relay.Function([var_3846,var_3847,], output)
mutated_mod['func_3848'] = func_3848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1626_call = mod.get_global_var('func_1626')
func_1627_call = mutated_mod.get_global_var('func_1627')
call_3880 = func_1626_call()
call_3881 = func_1626_call()
output = call_3880
output2 = call_3881
func_3884 = relay.Function([], output)
mod['func_3884'] = func_3884
mod = relay.transform.InferType()(mod)
mutated_mod['func_3884'] = func_3884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3884_call = mutated_mod.get_global_var('func_3884')
call_3885 = func_3884_call()
output = call_3885
func_3886 = relay.Function([], output)
mutated_mod['func_3886'] = func_3886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_3927 = relay.TupleGetItem(func_1126_call(), 0)
call_3928 = relay.TupleGetItem(func_1127_call(), 0)
output = relay.Tuple([call_3927,])
output2 = relay.Tuple([call_3928,])
func_3929 = relay.Function([], output)
mod['func_3929'] = func_3929
mod = relay.transform.InferType()(mod)
mutated_mod['func_3929'] = func_3929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3929_call = mutated_mod.get_global_var('func_3929')
call_3930 = func_3929_call()
output = call_3930
func_3931 = relay.Function([], output)
mutated_mod['func_3931'] = func_3931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2468_call = mod.get_global_var('func_2468')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_3953 = relay.TupleGetItem(func_2468_call(), 0)
call_3954 = relay.TupleGetItem(func_2469_call(), 0)
func_1714_call = mod.get_global_var('func_1714')
func_1717_call = mutated_mod.get_global_var('func_1717')
var_3985 = relay.var("var_3985", dtype = "float64", shape = (60,))#candidate|3985|(60,)|var|float64
var_3986 = relay.var("var_3986", dtype = "uint8", shape = (780,))#candidate|3986|(780,)|var|uint8
call_3984 = relay.TupleGetItem(func_1714_call(relay.reshape(var_3985.astype('float64'), [60,]), relay.reshape(var_3986.astype('uint8'), [13, 10, 6]), ), 2)
call_3987 = relay.TupleGetItem(func_1717_call(relay.reshape(var_3985.astype('float64'), [60,]), relay.reshape(var_3986.astype('uint8'), [13, 10, 6]), ), 2)
func_2842_call = mod.get_global_var('func_2842')
func_2843_call = mutated_mod.get_global_var('func_2843')
call_3989 = relay.TupleGetItem(func_2842_call(), 0)
call_3990 = relay.TupleGetItem(func_2843_call(), 0)
func_3503_call = mod.get_global_var('func_3503')
func_3506_call = mutated_mod.get_global_var('func_3506')
const_3993 = relay.const([-3.951944,-7.348158,8.762614,-4.301593,-4.588669,8.246949,-4.077742,0.517248,-5.135772,2.124269,-4.570275,7.954579,5.641670,-7.251036,6.036870,-4.381863,-2.619909,-4.597677,-0.935608,-2.575412,-2.598760,2.745298,-6.472290,6.850495,-2.159318,-4.985204,-7.936644,6.471675,4.135767,-0.950959,-5.889719,-3.358972,3.287560,-4.883887,6.305937,-4.840379,-0.901362,-1.856891,2.128841,0.469763,-1.171699,-3.247119,0.088383,-0.268434,5.450433,-1.025842,-2.055808,-8.380870,1.476656,3.773006,6.901576,-4.402109,6.152115,-3.097973,-0.660295,-1.259806,6.906043,-9.492020,5.549321,4.716247,3.853609,-5.021658,-0.520094,-6.766173,6.279221,-0.251679,1.101258,3.024979,8.676381,7.101513,5.680593,-5.009709,-6.653841,-2.142432,-4.945015,-6.293801,8.396127,3.668272,3.610575,6.634599,0.529853,1.250747,-6.049141,5.399033,-9.470344,7.194951,-7.384934,5.934516,-8.828541,-8.629827,6.986303,2.518215,5.791213,3.702011,-2.194039,-0.271819,-3.891921,-5.090937,-3.555425,0.344115,0.272924,-9.399064,-6.212347,-9.379745,0.021011,4.825055,-5.740379,2.266764,2.288706,-2.214360,1.353761,3.015344,1.235708,-6.246287,8.161162,-6.223600,0.915001,9.316467,-0.002722,-1.987318,-1.684810,9.233528,-3.596038,5.944489,2.508538,8.938127,-9.444708,-7.695305,6.086620,0.356765,-5.940831,7.001959,-9.769775,-4.283931,-8.792209,0.284836,-1.090334,4.605563,2.864623,2.990868,7.842839,-3.499595,7.303791,1.923871,4.324169,-2.092580,-9.276743,5.838328,-0.956274,-1.345592,8.268006,1.472622,-5.791183,-6.368613,5.377101,-3.667334,9.034794,-7.666715,6.036959,1.948759,-9.288275,4.405440,8.678850,-3.992093,-8.258762,-5.125203,-8.817117,6.872956,6.675982,-4.462976,1.067881,1.519144,6.679227,-7.601814,0.542386,-5.417972,0.964298,-3.217726,-2.803857,-2.518599,3.848584,-1.817457,-7.104301,-9.016468,-5.916922,6.883333,7.371430,-0.448385,-5.858865,-0.466524,-6.941794,-4.194186,-9.904996,-5.400775,0.001593,9.703722,4.623045,-3.277666,9.079763,1.794964,8.279334,-7.349211,1.838577,-8.164853,5.269978,3.037677,6.110710,3.147828,9.098438,-3.538611,-5.605206,1.747265,-0.886745,3.896255,1.254786,3.999559,1.427845,5.150102,-4.398074,0.055880,-5.914999,2.505993,-7.700387,7.085611,-3.316947,-6.519477,7.715350,-6.403706,5.655831,-9.195669,9.158129,4.118467,8.296146,7.256923,-5.290431,1.227429,-8.007925,-7.204728,9.901747,-6.624644,-4.696337,-2.302901,-2.632254,5.690807,-8.607074,-2.556212,3.760343,0.723662,7.958595,-1.786904,7.396385,-3.430980,-1.492647,-5.680616,5.949493,8.135528,5.431101,5.773543,-9.699958,3.763442,-0.844249,-6.961309,5.817985,-8.174861,6.614340,2.678556,-3.404925,-3.743935,-2.598493,-3.963062,5.457111,1.416200,3.976093,-8.749928,8.716782,7.182541,-1.926331,3.065818,8.078644,-2.157260,-7.917690,1.958957,5.843267,3.175910,-2.497009,6.191079,9.172854,-9.990189,-3.034452,0.527990,-7.765350,0.054332,-1.141616,-8.209195,0.105892,-3.500784,-2.008347,-3.566165,3.558431,-0.403026,-5.122936,8.135454,-8.097518,-1.605079,0.012240,4.761513,-1.454384,-4.768586,2.010533,-2.208378,9.975546,2.842689,-4.188420,7.162463,8.049842,8.079924,-9.287042,-7.636455,-2.173858,6.518149,-1.777523,5.247474,2.845320,8.961201,6.390265,4.870714,1.111948,-6.370861,3.402775,9.152561,8.419705,-9.224837,-0.429985,2.680315,2.791795,-7.018862,4.633951,2.659413,1.791057,5.722859,-6.461504,4.920179,6.107701,-7.692930,1.566635,-2.263323,-2.524750,-8.050401,3.679456,-1.993955,-4.256176,-0.265909,-1.636221,2.928139,-6.829540,-8.468932,8.289377,-8.980157,-8.948795,3.053934,8.249587,-5.518601,-5.636959,-9.914037,-1.418678,8.304981,1.848973,-1.569566,9.893115,6.891070,5.369303,-1.497442,0.539838,0.639886,8.216236,0.355692,-6.354905,9.245454,8.249158,-8.306109,-1.316880,-3.264758,5.350818,1.766821,-0.824655,2.361749,0.960395,8.096558,-1.528136,-3.726201,7.791492,-5.149051,2.063066,9.014193,6.629313,6.281806,5.717406,1.379260,-2.154495,4.254684,3.850834,-3.243129,-7.358562,6.597036,9.506124,8.739307,-1.402700,-0.903616,9.729177,-3.218734,-4.141661,-5.774877,5.011639,-8.969284,-2.274941,5.472075,-6.287111,-8.592471,0.373918,-1.208507,1.309074,5.536062,2.659512,-7.386154,3.484555,-2.854105,-8.856729,8.832568,-9.477586,0.523007,3.199513,8.612226,1.531859,9.626528,1.252455,2.270000,1.489354,-1.516938,-0.087175,8.326257,4.070669,1.833506,-1.626291,-9.740214,1.430990,0.257750,-9.831016,-0.330827,5.052144,-7.947549,3.144867,0.960375,-8.034216,-1.207775,-7.561340,5.515283,9.278248,1.933824,8.967701,-5.922961,-0.960346,-2.984145,-9.662866,-9.754092,-4.321295,0.194699,-0.247708,-4.578304,-7.640400,4.200685,-5.755189,5.514695,-6.913557,9.794742,-6.603424,-4.661648,2.898048,4.193837,6.577462,1.555082,-1.727466,-7.349355,-6.878691,7.575822,8.480237,7.949811,9.393596,1.239075,-8.258840,-3.915643,-2.339070,5.343834,2.583199,-1.783013,-4.590297,-7.990921,-0.174974,3.952801,5.404848,4.057458,4.462453,-6.782404,5.431808,-9.251606,-6.161826,-7.421783,6.196444,-8.118429,-6.221485,-3.124336,6.494256,6.369196,0.783858,-8.946806,-5.004138,0.070532,-8.006870,-2.582591,5.158064,7.959297,9.533347,-1.017909,1.551575,0.315417,8.769604,-5.737035,-0.110196,-1.670838,-1.149827,-6.325080,8.163579,6.936709,2.988778,8.221222,-0.669357,-2.477373,8.139747,4.385361,-3.990753,-3.850042,-1.992443,-1.367157,4.667139,-2.985384,8.304427,-2.676850,-3.115762,-3.080918,5.315643,-0.890816,7.002326,-4.665662,5.805848,5.573431,-5.547848,-7.287114,0.518500,-4.352452,2.859314,-6.826435,7.159747,3.042251,-1.980562,-4.075176,-7.078086,-1.989492,2.659605,-4.801866,-8.081035,-6.044597,0.633097,5.517223,6.143978,2.894642,-4.634789,1.027532,-0.024290,4.613831,4.032375,5.448667,-3.802292,6.377253,-4.747968,-0.444764,1.843463,9.870760,2.048968,0.798525,-5.955706,-3.722425,9.946241,8.962310,-7.193611,-9.810393,-3.341523,9.974701,5.625387,-8.389981,-5.137808,-6.326888,-2.074155,8.738988,-1.683746,-2.027005,9.642232,1.434902,5.108863,6.825100,1.131529,2.485329,4.738700,-6.234960,1.640614,-5.026928,-2.476475,6.465647,-9.733565,-5.849262,-2.362040,-7.487373,8.511515,-6.568398,-6.661122,3.958203,6.435948,9.036242,0.556287,-0.295833,-2.317159,8.647799,3.495736,9.518466,8.307503,9.758844,5.002306,5.779684,0.402979,6.365488,9.606625,-8.972496,8.327760,7.816099,4.609738,5.944378,-4.981341,-2.175966,1.945444,-3.154594,-0.873500,-4.473380,4.123871,-0.260895,6.047942,-7.395141,-6.931510,-5.954105,-5.776670,4.430092,3.454510,9.082542], dtype = "float64")#candidate|3993|(660,)|const|float64
const_3994 = relay.const([-9.120969,2.124534,0.517235,-4.956919,5.801238,-8.078068,-2.360326,-3.799938,6.584445,-4.621021,-5.983721,5.163139,-7.851204,-8.986929,4.636842,-7.036499,4.201003,-5.935172,-3.173539,0.127082,7.251454,-4.889956,-3.401805,5.188345,9.842153,2.058394,9.051620,1.765765,6.544324,7.383371,-8.330519,-0.013725,9.399720,-5.531960,7.314975,2.862025,7.519750,-3.098540,-8.563540,5.867817,2.927526,-9.172375,-1.059963,-3.089349,5.389149,-3.848856,-8.986518,9.149731,4.152585,7.463700,9.124270,1.797659,-3.797105,-8.656844,7.932313,8.923896,-3.959248,5.103713,5.436562,-9.723279,3.858395,-6.500838,-8.352533,4.169396,-9.282578,-8.667336,-1.994439,-4.843148,-9.094493,3.782140,0.316630,-6.577581,-9.067325,-6.279529,-4.833467,-7.308515,5.137858,3.454121,-7.032274,5.052885,9.761488,-5.927536,3.754191,-6.773797,9.973724,-4.909494,-1.274949,-3.034806,-5.988637,8.005825,-8.427916,1.756661,-2.091454,6.194461,7.975675,3.022630,-2.920605,-4.988111,0.379461,9.941622,3.304745,3.743655,1.289036,-6.134450,-2.602212,-4.709275,-5.287419,-1.701538,-0.001785,6.367352,-8.624747,-0.229919,3.667148,-8.338742,6.393754,1.784906,7.436684,4.006915,3.430559,1.881617,9.527564,-9.279853,6.356420,-9.209626,-8.005478,9.334515,1.403813,3.555853,8.489433,5.061802,-5.800653,8.654772,0.308958,-7.715003,-7.798762,-5.431926,0.758259,2.863800,0.987629,-8.479361,-4.364258,-8.654268,5.532227,-1.994671,5.760295,2.783228,-6.237501,-3.683713,9.732532,-2.787667,-8.074913,9.426383,8.404128,-0.783556,7.302610,-1.437970,-4.866890,4.520666,6.887484,-5.941667,2.988099,-0.078266,-4.423391,1.068492,1.334060,-1.227383,-8.868164,9.054223,-3.457451,-1.507279,-7.433028,7.437727,9.757386,-5.860172,-5.037847,6.303984,-2.975719,-6.534433,-9.449887,3.882902,4.409714,3.157960,2.643041,-2.221244,-6.497281,1.196103,5.000814,-7.891869,2.160327,3.107253,4.807849,2.752897,-2.481912,1.407375,5.045575,-3.926326,-4.580632,-5.181282,-8.392394,8.600112,5.252681,4.145490,-3.670090,0.866106,-9.560005,8.946239,-7.505392,-9.518700,-6.794347,1.774453,-8.496088,7.471524,-2.821264,-8.629080,-2.973910,3.840329,7.996275,-7.877469,-5.040926,5.054103,9.148530,4.817684,-3.042301,-0.371179,1.152534,-4.391747,-3.167994,-5.130015,-6.026138,0.016588,-4.693406,-1.379122,-7.398801,2.792698,7.086792,8.345703,-7.701936,-0.601690,-7.496868,7.635828,-9.644584,5.532905,5.659230,0.535713,0.524563,-4.517210,-3.539906,5.386570,-5.666404,7.236767,7.459024,-4.236337,3.994737,-7.174538,4.281642,2.118418,-7.986039,-7.061101,-8.724993,3.241314,5.339567,-1.327993,-1.115959,-7.608376,-9.839179,-9.191105,-8.164548,3.893552,2.306082,-4.474513,-2.765570,0.528929,-9.858967,-8.415068,2.516602,-2.559200,-2.677408,-4.430646,-5.931756,1.146846,1.181838,5.565097,-3.920395,5.476466,-8.998661,-1.725129,-8.426515,6.783187,-4.331956,3.959994,9.134710,-0.495371,-1.107979,2.200268,9.145243,-9.544665,-7.666060,-2.559292,-6.655685,9.367826,7.298289,9.170045,6.801957,0.596126,8.605532,9.857292,-4.872272,-0.448187,8.317056,-8.041442,-4.738095,9.966566,-0.111776,7.842489,9.739131,5.151667,-8.407634,-5.941302,-4.533542,0.281225,0.879383,-0.447766,-3.282327,-7.700879,-3.526638,-1.835381,7.421621,-6.469774,-1.032865,4.446386,-5.327198,-4.503886,6.601668,-4.248549,-2.563046,5.534891,-1.662516,-2.249170,-5.089123,-8.025678,0.202667,5.977305,-4.156499,-6.638434,0.387331,4.516939,-3.251287,1.252894,-4.077165,7.472778,5.115691,-6.889093,7.790747,5.750368,-2.956371,-3.569579,-8.492687,-0.779267,3.952568,1.263814,-6.735634,-9.199734,8.713805,3.820112,5.341762,-7.395583,2.821228,0.535811,4.371425,2.365598,-1.387496,9.243706,4.730464,-6.476090,-4.823294,-9.122898,-4.891693,-1.400955,-5.956886,1.054039,-4.485798,-3.182496,4.419550,-8.186990,-8.250559,-4.425105,-6.645828,-3.221487,8.483713,-8.360564,-5.792374,6.839975,-8.026202,-0.312251,7.511264,-4.527949,-5.037336,4.889598,-4.588044,-4.214936,7.402936,-1.815013,2.569210,-7.681320,7.950635,-8.198141,6.331795,-4.574882,6.366541,-3.116144,-3.368254,4.112660,3.030103,-9.159388,-2.615110,2.721547,3.375577,4.306463,-8.620978,-4.603595,6.912170,1.574373,-7.855143,-4.857687,3.583206,-6.394000,8.227713,-0.398908,-1.836859,3.192257,1.104289,8.860787,-3.962980,0.872145,-4.751460,-4.384932,4.193963,-8.622892,7.702027,9.843533,0.060706,-3.945138,9.396730,2.915842,-3.147416,0.970087,2.413501,-7.079170,8.006333,-5.229355,2.424150,6.454086,6.675130,-5.764688,-0.830093,1.015199,9.253812,9.230085,-7.190411,2.302129,0.357078,-5.812347,7.770563,-8.860461,0.226488,-8.737862,3.179825,2.256320,8.775270,8.674285,1.433836,5.958721,-1.308911,-8.912943,0.616530,8.708024,-2.661955,-5.421974,9.814103,-6.742150,0.567449,7.057537,7.402485,6.213738,0.658390,-1.204812,3.337777,6.134195,-1.069700,-1.600769,6.160950,-0.096942,-6.398635,6.401626,4.732223,-9.670670,-4.058986,1.036805,-6.584103,-5.225124,2.526283,-1.265938,-6.115559,3.503031,0.143733,9.418164,2.845607,-8.212761,-7.170531,0.081967,-6.616312,-1.473115,-5.121615,-0.216063,4.073172,-6.001230,8.206636,4.045042,-8.264781,2.665824,0.667428,6.989735,-8.118468,-6.819690,9.241115,6.996238,3.090274,3.533723,8.931493,-8.738071,-0.404943,-2.739050,2.180151,-6.357303,-1.053338,-0.172096,-9.970090,-8.179771,4.039573,5.591121,9.970483,-3.110722,-6.845208,-4.451104,0.255103,-3.073105,1.880865,-2.894812,8.715280,-0.335355,-3.063162,9.574695,-7.695536,4.743745,-6.048779,8.448425,5.874210,-8.746481,9.160420,-2.855989,4.927617,-8.385515,2.137479,2.404270,5.240110,-5.330150,-5.876154,-2.031043,3.234365,5.500127,-6.163395,1.299386,-2.055207,-9.241730,-0.405549,9.672974,6.297654,-5.520019,-6.973079,1.282135,-9.792152,7.538996,7.607836,2.109372,6.594779,-3.179381,7.705633,-0.782117,4.257407,8.187202,3.621073,2.254943,6.443636,3.634681,-0.287510,4.452034,-1.543234,1.371378,0.460592,-0.344946,4.072661,-4.657999,8.376575,5.124911,5.233677,-8.219636,1.633499,-1.206513,-4.798879,-7.011130,-3.902107,7.107275,-0.620699,4.637994,2.243173,-1.204370,-3.700930,-7.461149,6.687591,9.449714,-6.192664,5.129442,0.559796,-7.053498,7.962015,-8.892883,1.669089,-9.232449,0.742540,6.770123,-9.577764,5.609428,-6.344179,-6.681113,6.218360,6.572270,6.556677,8.387814,-3.442937,-7.915117,-1.196089,8.598305,-9.905136,5.114943,1.060059,6.431323,6.876078,6.125074,-0.675564,1.867498,5.943475,3.203955,-4.119707,0.797726,1.293307,-7.917984,4.890122,0.844958,-9.106177,8.872931,8.377060,0.324476,0.843192,-3.699755,-2.580710,-2.791123,-7.261359,-5.748479,-3.028927,5.232552,-2.279511,-3.547397,-6.496695,1.351831,-2.917024,-6.802577,2.312403,-7.784870,-1.328157,-2.281467,1.134546,-4.703304,8.150994,-2.451345,3.138436,3.457614,6.055462,1.396255,4.019651,-9.370658,1.063527,1.839867,-3.954179,5.606010,-1.449073,9.597186,-0.992842,-4.400904,5.567050,-5.335837,-9.271775,-3.900417,6.715269,8.282966,-1.121636,-5.697406,9.523676,0.422709,-9.975557,-0.881124,-1.104789,-9.650173,-0.544551,-1.253599,8.892159,-3.608585,-4.653962,6.411002,-9.171363,-1.769136,2.348781,-3.208363,-9.565703,-2.764653,-1.741753,-6.123197,4.137303,-4.315742,1.620815,7.821187,8.777557,-3.180956,-3.880053,5.169525,0.668538,4.238847,-9.802580,8.937354,2.377486,5.959662,-8.302470,2.164171,-8.751338,9.080565,-9.726704,-9.653802,-7.443776,-1.159039,1.065454,4.014717,0.090210,5.641269,-9.569774,5.168159,-1.369648,-1.563082,-1.966571,-4.891526,1.343361,-3.217525,-0.084578,3.720364,4.931879,5.156688,0.195370,0.184744,-4.168707,-1.297374,3.635045,-0.365821,2.446709,4.768638,-7.123436,-6.817433,7.549537,-5.236153,-6.991879,4.518368,5.070790,-7.862892,0.571609,9.883352,-2.303670,2.486356,3.663383,6.140128,-0.712257,-7.437050,6.979297,-1.589266,3.197724,-1.591988,-5.650347,-5.340442,0.807289,-0.665549,-2.466206,-4.930049,9.425091,4.260885,4.954432,1.434894,2.445509,5.731213,3.938090,6.004296,-9.075050,-9.330782,4.807348,-7.481735,5.679460,-5.247141,-3.522169,-9.009610,-2.430420,4.078362,-8.325004,1.489686,-8.294824,-1.651325,-1.186030,3.433052,-0.876039,3.491791,-4.501593,-9.412938,-5.690054,6.897410,4.753587,-6.704427,9.795553,7.692110,5.823174,9.770267,8.965821,6.298066,-0.917432,-4.515689,-0.282113,-4.117137,5.550198,-9.331210,4.683828,6.779087,5.891689,-1.024288,8.983416,-7.793479,-6.239250,-8.686822,-3.019691,2.882614,-7.329072,3.844983,4.442262,7.800929,-5.435306,-4.116147,-1.723236,-6.374897,-1.002883,-5.111483,-1.283161,-6.764313,5.750373,5.088222,-7.805818,-5.845416,-5.973637,8.619888,5.297330,3.138389,-2.903167,-8.573574,7.801207,-4.921659,6.063608,9.363673,9.793518,9.056706,-1.864790,-3.494794,9.807546,-3.209938,-1.624094,-1.684878,-9.156620,8.435656,0.154303,7.839862,-9.220439,-0.870729,3.418507,-9.876959,0.302372,0.192686,-8.801486,-9.704992,-6.550192,2.382137,-2.478050,-2.236957,6.178200,3.692284,1.435732,1.656592,-6.628765,-3.508071,1.549701,9.630904,-6.172694,5.139719,-9.790823,-0.009411,-2.727759,-3.212625,2.732031,7.540094,-9.927487,-9.556545,-8.423138,-2.289170,5.302545,-3.233184,9.502203,-4.137295,-9.314302,-5.795704,9.624458,4.871615,-6.280251,1.663626,-3.111748,5.755311,3.065624,6.377910,0.370544,3.992812,-3.140267,-1.210784,6.357804,1.774180,-5.246426,-6.152428,-9.655491,5.417795,5.077961,0.931843,3.936696,7.063071,-1.519064,-1.364235,-6.683506,-5.473517,7.750807,-2.591646,8.237212,-9.469626,3.797625,-9.758757,-6.042447,-3.406558,-9.585114,-2.416241,-9.674387,-3.048894,-3.906709,1.659906,-8.794243,8.247679,-2.983895,-7.242077,9.660065,3.093467,-2.927278,-9.430866,5.607597,-1.968438,-3.958254,6.009852,-5.401506,9.644491,4.570124,0.611743,8.701700,1.305793,-1.391496,9.821317,5.512834,-4.529170,-8.809324,-8.217985,-9.752014,6.750877,7.545423,0.688549,8.394374,-3.698327,9.396213,-5.277073,-2.859854,-6.821849,-4.346356,-4.386609,-4.273788,5.576856,-7.134095,-6.627509,-7.022598,5.227102,5.055986,-1.098745,-0.350501,3.393700,-7.077209,-8.661067,0.826770,-4.432246,-8.726445,4.350298,0.436813,-3.059806,5.571191,-9.565499,-7.448676,5.354595,4.126415,-4.922605,2.321303,3.099820,-6.191496,-6.210182,1.657031,7.227618,-4.299379,-1.928572,3.179902,5.897605,-4.677414,-0.866260,4.619840,-1.040226,8.661104,-5.010275,-5.173238,0.144043,3.301925,-0.950405,-1.018397,4.485503,4.232733,-1.769365,-9.982630,1.515265,-7.085449,2.653508,4.039161,-9.380555,5.055644,0.437391,-8.825188,-1.012797,5.357793,-0.105821,-7.351589,-1.997321,-6.168678,-7.661825,-8.089549,5.211312,3.940332,-9.656748,-6.541428,-1.653247,-4.998777,7.595019,-9.302771,-7.866812,-8.730226,0.222001,-1.631144,-9.172143,-3.751707,3.348737,-4.968359,7.626931,-8.635180,0.411160,-5.941121,-1.294475,8.340179,-4.900437,1.054335,7.648196,9.172941,-1.495749,-6.564618,-9.082838,0.878422,4.376006,-6.420721,9.520656,6.992687,2.916194,-1.317990,-4.144203,1.450061,1.555047,2.451693,1.500438,9.121816,1.348792,-9.243824,4.945612,7.485129,-7.133023,3.595363,-3.444942,-4.269728,3.068981,8.263569,-6.119586,-1.829909,5.674222,9.875969,-6.352981,-1.679316,-3.175237,-5.472448,-9.739376,6.654746,2.967808,4.859911,4.492633,-5.099976,-5.345873,-8.434281,-6.635454,4.515220,-1.671701,-8.017164,0.642263,-0.169633,-5.672553,2.076964,8.341772,8.880092,-2.983231,-6.614434,-9.899873,-6.358904,9.514578,0.641321,8.897201,8.971234,9.868939,-0.112351,3.328079,8.095049,5.250037,-7.441831,5.704317,-7.720393,-8.200810,8.344411,5.705985,-5.033924,-6.888526,-5.866059,-0.629329,8.507552,-2.214502,-9.472340,7.151633,6.203278,4.105740,1.968090,2.044768,-3.666000,-6.070827,-2.668748,0.603461,-7.704359,-2.954486,8.735289,8.017000,6.483266,-9.597954,4.041751,7.151431,3.871699,-5.115764,5.482985,-7.471792,-7.913274,8.999239,-3.111895,6.861666,-2.603056,6.269861,-0.939486,-7.141254,-0.671445,7.190848,-1.072645,-2.222532,6.063421,-9.791643,-0.184338,-0.648480,-2.717549,6.467004,-0.862230,0.581849,0.020136,-5.671973,9.856221,2.846203,-2.588658,1.042927,2.499285,-3.728807,8.391345,4.314136,0.902250,-2.696117,9.504164,-8.324383,-3.531179,-4.616299,-3.910540,3.596808,3.743092,-5.841647,1.629977,7.008795,0.546290,-6.557555,-3.352460,3.800646,7.809468,0.507547,8.235777,9.578177,-3.398699,6.107251,-8.110332,-4.099578,1.616701,3.779398,9.524238,0.632296,-0.052549,8.814986,1.851172,-3.389778,-5.376860,8.405694,7.056503,3.863770,-9.055239,1.173033,4.092532,9.333968,-9.067238,0.587317,1.306512,-4.298632,-6.823485,-8.227081,-4.941705,1.036263,8.223491,5.526040,1.284222,-7.230267,1.653227,-2.193538,2.521779,-1.847130,6.701097,4.999995,-4.089411,-4.197686,3.379277,3.786762,-8.299101,-2.392043,4.892264,-8.606525,-0.568722,8.799445,-8.526402,-4.635141,7.331349,1.701694,6.228569,0.352834,4.914038,-8.426692,-2.234862,-9.317326,-7.075326,-6.480281,-1.398094,-5.087683,0.423872,6.382061,-0.591272,-7.248916,-9.242479,-5.359072,-1.535054,8.474074,4.436619,3.433158,2.526824,-8.895046,-7.536449,-5.728586,-2.316698,-2.648371,-7.024020,9.904448,1.618837,-3.469067,-3.764435,8.185018,-1.669183,-3.486558,2.480405,1.351973,3.008203,-0.499988,8.146899,8.168452,-1.081410,1.117696,5.290211,0.234938,-6.931691,-7.170810,-5.079337,-1.726519,-6.768909,-2.040947,-8.960706,3.219659,-3.647810,2.350558,-4.511004,6.492888,-4.421089,4.126186,6.325029,4.570763,-6.488339,-9.823699,4.487968,4.444909,3.780655,1.856179,9.630246,-5.472137,0.702088,6.047970,-8.480618,-7.497732,-2.986595,-1.965947,-1.993282,6.156854,5.119327,3.514538,-8.000039,-7.238152,-2.558181,7.556187,-9.151582,8.592709,-0.934900,8.256834,3.632459,2.209353,7.608146,-0.007528,5.653366,-0.477445,2.081224,-6.218133,-5.951030,-0.164549,-6.662554,7.899596,4.088059,-4.524904,1.181674,-0.526574,1.340003,-1.623967,6.965933,-9.062430,8.404691,3.578668,-0.562224,-7.235172,-3.752094,-4.836476,8.340282,-4.670804,-3.848152,-8.910170,-9.882850,3.817826,-4.970830,9.629585,-0.385596,6.732190,-2.454796,-8.460744,-2.542054,-2.694629,7.552376,4.728771,-9.250232,8.111906,7.990019,-5.248832,-9.941883,7.363494,-3.654186,-1.361013,8.336430,-4.445042,-6.641843,-3.243438,9.020288,-0.611098,1.837259,4.926686,7.428871,5.711409,-9.040669,-9.564619,1.154470,-1.163737,-7.226001,-6.758046,-5.145220,-8.818159,7.341634,9.911492,1.497861,-2.928227,7.330034,-0.366603,-6.112564,1.823242,5.584637,-6.743579,-6.537356,-7.405082,4.765338,-6.056041,1.282132,6.390095,1.380518,-6.851839,-2.824117,-0.963998,-2.609743,-3.114714,-9.523820,-0.632614,7.865580,-7.302908,6.230004,5.099172,8.488015,-0.805874,-8.017557,8.958824,-1.347867,-6.915944,-0.379628,-9.648797,5.707582,-1.883485,4.085799,8.251850,8.841525,-0.464357,2.208004,5.393591,5.005643,0.800723,3.510144,8.408922,-4.351078,-3.126720,-2.774790,-8.769968,0.421969,2.631869,8.682902,-0.195491,-4.489630,0.688304,-0.387630,-1.248224,-8.056842,1.129929,0.010876,1.643965,-8.093856,-0.217467,-9.148866,-9.266135,6.566170,-4.377857,-7.148269,1.732657,8.334672,-1.644131,-1.967801,8.215969,7.325460,-6.367897,-5.478484,-2.209117,-1.020684,5.324505,6.943640,-8.474077,-5.741815,0.016531,9.013724,1.676444,0.984644,-1.972888,8.076628,-4.056339,-1.632968,7.030258,-4.130821,6.194465,-4.522025,-0.603172,-7.821535,3.065941,1.934196,-9.176323,1.861677,-0.873750,9.158037,-4.917031,-3.639549,3.970718,-3.613648,8.583991,2.040585,9.178051,-9.643662,5.199885,-6.064554,0.039967,-6.152686,6.927720,2.486305,-2.715292,-9.864816,3.036383,-3.838202,-4.863377,9.346481,5.074583,-0.968220,4.552358,-0.896216,-3.103856,2.371162,9.250370,5.320973,0.289948,-9.846567,7.390495,4.726998,5.247511,-9.349203,-6.562986,-8.580815,-1.781047,-6.619555,3.828049,-6.503834,5.516101,7.800921,5.447852,0.399953,9.440966,9.142922,4.876026,-1.952940,-4.913096,-5.487132,-2.988555,-9.128092,6.207277,-4.069390,-7.356145,-0.201966,-9.065539,-7.204641,-0.352469,7.954778,7.551596,7.123126,7.892145,2.122383,-7.214209,-2.054763,-3.983056,8.341858,0.842813,-5.092344,-9.188682,5.959247,-2.409653,8.396807,-7.965914,2.313781,9.514123,-7.559607,-2.419169,-1.648838,1.863744,3.101150,2.261251,6.209154,2.959960,-8.573280,3.637912,-1.756147,2.141040,-0.597436,-1.345610,7.526645,-9.053397,-9.409244,-3.018419,4.248693,4.079804,0.049044,9.360603,2.574890,3.072428,4.717807,-4.071033,-1.406711,5.373601,6.526268,-2.708150,5.540524,-0.542064,2.017417,-4.944338,-5.566199,-9.496516,-1.576823,-1.324846,-5.427577,-7.675318,-0.055081,1.010210,-5.391359,-2.376577,6.831469,3.321651,9.163127,-6.900466,-6.110162,-1.882708,6.478268,-5.820935,-7.990501,0.468113,-2.538821,-0.002396,-9.010950,-2.620600,-9.634030,-5.932780,7.185585,-3.072683,9.889516,-5.358376,6.355566,-5.538161,9.448898,2.034202,-6.628217,-2.380589,-5.565478,7.129975,-0.585651,4.068720,-2.795741,-1.942057,6.195926,8.267174,-6.262224,-9.530693,-7.929960,-3.295087,-2.365545,3.475984,-7.131345,5.365218,3.094685,-6.114929,-9.756549,-9.843902,7.091769,4.802617,-2.478766,-4.460646,-9.926875,-2.663046,0.364772,-6.258814,-5.475051,-9.626863,8.384566,3.177808,3.184483,-4.439848,-8.538579,-8.204100,-7.588692,-1.979747,-9.336660,6.475140,-8.433466,2.650245,-4.476277,5.403064,-5.118721,3.968170,5.779654,-8.544422,-9.273376,9.691808,0.152235,9.164611,7.596094,-8.867314,-0.315404,-9.158534,-6.088482,-8.140316,5.158957,2.655468,-4.301221,0.035739,-8.524245,-4.406204,-8.484658,7.251464,5.530550,6.656519,-7.720141,0.288702,8.742918,6.434286,3.861168,-1.704552,7.177265,-4.260861,6.081195,-3.328504,7.656793,-6.896684,-7.655078,-3.751531,-7.967801,-3.106151,8.791866,7.241826,0.377545,-5.392871,9.180794,4.398255,3.237634,-1.441317,1.768497,-5.703403,9.807459,-9.755442,-8.124401,4.566386,4.073310,9.947727,2.591033,4.699349,-6.351700,-5.232772,5.244563,-6.621213,8.633685,1.073538,7.815896,-4.190438,-8.980625,-8.383974,8.658881,-6.027717,2.865740,8.148239,-9.909389,5.912286,8.634290,-9.443738,8.932394,9.148505,5.240162,0.102111,-4.846189,1.815395,9.432451,1.637395,-4.860727,7.995174,6.928253,-6.972012,5.221881,-2.182613,0.580509,6.115625,-0.230432,-2.006823,4.768655,-4.204613,9.363539,8.556121,-6.942795,0.551033,-9.903238,-0.120352,1.142637,9.019717,6.765195,2.307113,6.504256,2.101086,6.914260,5.249943,-4.613422,-4.814050,-2.911992,-3.244034,-0.820030,0.244577,-5.142677,4.434324,-6.175159,-1.253545,-9.299821,6.186856,5.082576,7.661574,-0.839749,6.715206,8.869042,-9.862730,4.779588,-7.586753,-3.995504,-3.886837,9.840566,-6.096714,2.055498,7.720382,6.504794,4.425886,-5.333106,3.393986,6.394078,7.844399,3.295028,-3.447473,-7.686502,-2.415349,-1.675149,6.604469,-2.592987,-6.102024,-1.917157,-9.913924,-0.466236,-4.849380,-0.960129,1.019448,0.742283,-2.570566,-2.092103,8.187525,7.912909,6.063701,8.586756,-0.555625,-2.116060,0.126354,-0.603005,-5.583206,9.526168,4.524784,7.493871,6.701621,9.001974,9.308249,2.613143,-7.942166,-7.165205,-4.053072,-6.829628,-4.113356,0.064957,-6.175837,3.620456,-6.886237,2.451349,-0.369044,-6.017768,0.980613,-7.791363,0.529680,-7.705649,-0.405398,1.814959,-8.023846,1.962110,4.718357,-8.888851,3.852858,-9.209697,-8.073411,4.950649,-4.634112,-3.215078,-6.015275,-2.480974,-0.074984,1.337853,-9.763331,-5.878615,9.656109,7.942100,-5.126069,-7.994235,9.653990,-5.412996,-6.495346,-1.440834,2.304784,2.394678,4.951166,-3.214612,-2.287826,3.932039,-4.768938,7.658003,3.114747,-8.588377,-6.201178,9.574548,-9.379252,0.009640,-0.208682,2.006568,-1.371594,7.905121,3.483243,-7.325477,9.859617,-8.473990,7.374770,1.910465,-3.605625,-6.052698,-6.588851,-3.736342,8.533382,-2.498007,2.254531,-8.422288,-8.739424,-4.884951,3.959691,2.337475,-0.263960,-7.671603,6.587018,-2.380371,-1.361599,-8.064701,8.815879,7.011171,-1.502232,-4.557278,7.352280,7.959731,-7.102936,3.183636,-2.841882,-4.246247,-3.780892,-6.293497,3.493958,9.571117,-2.871989,-2.815564,-9.304724,-0.831199,1.720971,0.089082,0.028374,-1.768584,-6.196886,8.013906,-0.213592,1.783209,9.261616,-0.040668,-7.367085,-8.460440,2.671177,-1.584412,-0.888643,-2.325507,0.764412,-5.294935,2.552743,-0.465963,8.910679,-3.460404,-3.398715,-1.078891,-0.767257,-9.401103,9.111317,5.085691,0.966434,-0.759687,-7.939993,-9.666287,-4.485268,3.568700,4.889019,3.849682,1.706229,7.811954,4.778084,2.603253,-8.630974,0.498201,-1.109339,6.986870,-5.017203,4.467301,-1.598497,7.530761,8.424008,-3.106342,-0.704290,8.219963,-2.162389,1.433057,-2.357924,8.393456,-3.450430,-7.498279,2.086317,7.134606,-5.263268,-2.762105,-6.941802,1.000392,-1.455413,-0.996036,-6.646263,6.101233,-5.831662,-2.874566,7.044017,-2.323869,-2.301779,6.114757,-9.678958,-4.531288,3.980794,5.234862,-9.090616,2.745789,1.768313,3.743076,8.290338,-0.681157,-2.076745,3.218358,-7.443808,6.536091,-4.637183,-9.444908,8.083156,6.361276,0.111555,-6.705319,-3.339207,8.473527,-0.052892,8.548187,5.654455,0.947214,-2.011512,3.749571,-1.918487,-1.083902,5.631631,7.440108,0.437161,-7.823459,-8.730096,-7.484575,-8.509411,-8.115707,-6.194974,8.608391,4.124134,6.540369,1.390546,-3.432575,-3.841316,-3.912692,3.277495,-8.073039,9.373852,3.373703,-3.869541,-5.904979,2.724117,2.368865,-9.384952,7.063870,4.672888,2.240699,-9.187958,5.622314,-0.356080,-9.326354,7.108893,-3.233443,6.458189,-9.008571,8.367005,7.139047,1.550507,4.318391,5.622533,4.035535,7.858381,7.494792,-4.049055,-6.414155,-0.298331,-5.298932,-6.710158,-3.913618,6.380416,1.587107,6.653576,7.663401,2.100608,-6.211988,-4.654165,0.937920,7.425571,6.596690,0.736138,-8.723751,-2.692112,-7.386679,-3.882323,3.851892,5.597686,-5.518690,6.986442,-0.767455,-7.455647,1.309819,-1.512073,8.663268,2.236015,-6.032324,-3.099957,-0.363280,6.987412,8.455051,-7.890975,6.334711,9.801042,-3.319035,-8.305267,0.021550,-6.192506,2.466756,-1.784542,-9.177869,4.839661,-7.633485,2.653056,-6.627830,4.207041,-6.510200,-3.642859,-8.737381,-7.294668,-5.575794,7.180363,8.039615,-3.523088,-4.972961,1.726708,-5.912871,8.957183,0.156627,-6.239840,-9.866530,6.309858,0.646541,-2.174250,-1.140645,-6.241553,0.735583,-2.383459,9.861178,0.226819,5.042335,-4.261599,0.418836,9.905734,5.093064,4.707285,8.920708,-4.240500,-8.895127,-6.892878,6.505973,-1.578988,-0.196133,-5.698815,8.947877,-8.605455,-0.353528,9.149561,-6.454390,-5.919385,-4.711675,3.130669,1.408525,-9.008300,7.396716,-5.164114,7.700155,3.231947,3.598233,-4.910960,-8.847372,-6.705607,3.053652,-8.574138,-8.783674,9.496967,-6.090271,-4.311165,3.338118,-0.808838,-5.322881,9.289582,0.076335,2.976556,-1.469048,6.441179,-1.760529,-2.496873,7.480320,-0.954139,7.642704,-2.114579,-3.492164,0.984280,9.324536,-1.403422,-7.112332,-5.388053,6.663456,2.846350,9.043523,-2.961374,-0.544530,4.924536,5.975931,7.529730,-3.915643,9.882831,-7.943471,-6.527721,-6.646729,1.140296,-6.011602,-5.726218,-6.533803,-2.126587,-3.664059,0.846898,5.445190,0.974551,-4.963575,6.941129,-4.510097,-5.183388,-1.479224,9.112233,7.330443,7.785590,-2.162298,3.222618,0.725298,-1.538648,-3.199290,-8.437455,-2.998034,9.966766,-7.939425,2.118416,7.225402,-3.545689,-1.946326,-2.303541,-9.071565,-4.164589,4.002302,1.287613,1.216503,-5.131572,-7.585773,6.379505,-5.068946,7.723503,3.708474,-1.830208,-1.148053,-7.574197,-0.972111,8.409000,0.206954,8.691350,1.403238,7.376337,-7.373225,8.525041,6.817385,2.880393,3.304810,-2.490913,-7.646908,2.283006,9.968185,9.410424,-0.987815,3.774975,-9.523732,-9.328716,2.312138,-4.569514,0.134496,-0.040359,-9.821332,0.236928,3.946486,5.583286,-8.426633,-4.191301,-6.276248,9.779285,-4.415374,-1.467682,4.037109,0.528768,1.700941,-2.783648,2.435396,3.711356,-0.186763,0.303709,-3.214598,3.561369,7.156109,4.045734,-8.247263,-9.725152,7.346838,8.703441,1.160768,0.971577,2.951763,9.667273,1.652571,-4.076116,9.330448,7.454627,-5.842401,-3.432182,-0.659433,-9.425605,-2.661826,-3.615904,1.426843,-2.247563,-2.800620,5.926439,8.990345,-0.384179,1.515514,3.463916,-3.106047,2.975148,5.672501,-9.862712,1.364573,-2.760253,2.041620,9.646718,4.846399,0.641660,8.184311,9.971716,9.377367,3.549902,-9.381317,-1.652864,8.962376,-0.904176,7.074612,5.407156,9.979667,8.544484,-0.649211,3.907441,-6.474145,0.323196,-3.611876,4.601086,-0.640286,-8.212973,1.565028,2.498248,-5.978164,9.536960,-2.583793,-7.036097,3.277882,-7.514570,-9.889046,2.550168,-6.921912,1.307052,2.135318,-5.200388,7.953265,-0.978070,1.283460,-7.796886,9.456969,-1.157380,-8.967394,5.546554,-5.603339,5.346250,-0.309325,9.892258,3.167500,8.149141,8.958901,-6.323058,-2.253848,9.985918,-7.535886,-8.498258,-4.526909,7.951404,7.539848,-8.508434,-9.503721,2.932882,-2.424801,8.745900,0.771884,-2.814228,-8.770035,6.201913,4.388935,1.860837,-5.267725,-6.544913,-3.097148,0.633306,-7.338129,5.861117,0.018535,9.203976,2.706472,1.360161,1.870707,-4.736066,-7.460608,2.705451,-3.323290,8.509940,-9.356477,8.167593,4.296652,-5.146478,-5.918835,-8.898297,-8.687613,6.310370,-9.597702,-3.084305,-6.436124,-4.507521,2.249056,5.519326,-0.907474,-5.086108,-5.793950,6.134983,0.061281,3.082747,5.630248,8.783981,-4.199989,1.623068,-6.046669,-7.602174,-9.652152,1.938048,-7.519478,-2.847746,-6.327221,2.765864,-7.031006,-0.007381,7.727232,-2.195461,-0.983428,-2.492841,-9.876381,6.924350,-5.585356,-1.789959,-2.898874,-1.769238,-1.776930,0.718506,9.708664,4.768347,4.415263,7.276257,6.727700,9.153983,-2.666985,-5.998510,-3.880324,6.013675,-5.043505,4.694312,0.815490,8.522795,-1.923693,-6.036886,-5.894742,-1.467504,-5.832084,-3.516610,8.635593,2.510594,5.783806,-4.586716,5.441079,-7.173582,0.955592,3.030892,2.559575,-8.130465,1.076927,-6.198662,-6.171457,-7.902958,-3.684279,0.608201,-1.360523,2.930838,-6.799343,2.261696,3.304831,7.333171,-3.005872,-9.308773,-0.638872,7.387450,2.416472,7.537218,-9.087475,-0.299494,-2.481141,-1.020337,-5.037782,-1.742812,-5.082033,5.141585,-6.123946,-1.440763,1.276520,-9.847378,-8.838905,4.309699,4.280924,9.005265,-1.074460,2.941039,7.798162,-4.776895,4.118901,1.250925,-5.469238,-4.081445,1.872726,9.943049,2.928172,-5.252050,-3.724758,4.511366,-9.204515,0.399564,5.499335,5.524770,8.975639,-1.066508,7.257823,-3.277234,-8.182216,-6.577032,8.279826,-7.405272,3.062096,-8.182842,8.537302,-0.843171,9.728473,-6.552551,-9.028268,7.861335,8.769000,-8.746562,0.872234,7.105619,5.640650,-2.460068,8.202524,7.412196,7.559972,-9.575051,-8.340057,8.384061,5.435301,-6.739483,6.547078,0.868163,3.310974,8.942576,-7.930522,1.061955,-5.569922,-0.163817,-5.749232,4.744576,-7.932161,-8.398245,-0.259778,-1.476492,-2.208005,2.943272,-7.799036,-0.767066,-9.215626,2.065566,-7.558825,6.521999,-5.977927,3.024142,8.428045,-4.456707,-4.848557,-4.036702,-3.526947,-6.388392,7.803795,7.727687,-2.317650,-8.323467,2.798073,2.593405,-9.898014,7.537295,0.675512,6.985001,7.187980,-9.697739,3.317801,-4.561432,6.047316,-5.471095,-5.517062,-4.327914,2.720830,9.748294,-4.808639,4.506991,5.013356,7.422737,4.846352,-7.578068,6.952885,-7.430816,0.015803,-3.954183,-5.923559,-4.799942,-6.403552,9.093860,8.126579,7.942496,-9.911535,-8.518110,9.827993,-2.351589,-8.480790,4.516348,0.270300,-2.704858,-6.382012,9.420787,6.632875,6.663453,-7.217680,-7.422458,3.219074,-3.988517,-6.721606,-4.056355,-6.087556,-3.991258,6.368127,-8.313197,2.108228,5.566110,-3.880185,-1.899170,-9.643722,5.891920,4.258770,-2.853855,2.060721,-2.254410,9.956063,2.235161,3.164281,1.556100,4.623155,8.602345,-4.869872,-4.601406,1.920338,3.043453,-8.630150,-9.802221,-7.667426,6.835009,0.248019,7.388342,-7.370677,5.011027,-3.474595,-5.917501,-6.478969,-4.848432,-3.822235,1.032614,-9.499564,-0.909756,-3.555719,-6.702582,2.297199,-9.846186,5.591420,-7.973017,9.821315,2.259497,-7.923513,9.152830,4.190323,3.082949,0.505191,9.725106,7.068365,-7.876483,-6.817932,-3.622396,-7.454821,3.840577,-9.483114,2.914485,0.009265,1.575484,-2.097255,-5.890914,9.645248,-9.968631,3.203547,-4.260586,4.511212,-2.360844,6.406722,5.205952,1.248466,6.409874,-4.029059,8.797267,1.207224,6.516450,-3.079961,7.852518,-4.181565,-5.303512,9.790169,-2.173626,1.704699,-7.001961,-2.366568,6.506329,-3.634602,9.914987,3.594709,-3.301569,-5.214922,8.843867,-2.909181,-5.303698,-5.380777,-9.084346,3.263221,-9.629691,6.406940,1.810062,-4.071723,9.474550,9.811825,-1.445385,-2.102247,1.858498,-7.284022,6.116977,9.705374,4.337301,-8.011251,9.186497,7.385326,-6.486518,-8.399348,-6.611370,-6.238131,-1.313114,-8.123868,0.596144,6.144588,3.090049,4.549538,-1.486232,-2.965323,-2.258945,5.583199,-4.221408,3.177005,4.542819,-6.623175,-9.918668,-9.626736,-9.319779,7.284307,8.892572,-4.265145,9.177053,6.129972,-2.912878,2.754746,-0.059909,-3.758935,9.439177,4.251870,-3.601509,-0.246691,4.444093,9.077147,-5.010102,0.805868,0.266759,-9.649987,6.684993,9.206982,-0.666420,-1.648202,9.724576,0.488485,-8.807531,-0.619410,7.945497,2.231078,5.195002,-9.716084,-6.515305,2.389698,-0.430414,-5.606957,9.571088,1.094167,-4.927897,-5.270758,6.525437,2.467889,-5.175340,-6.621482,-0.530264,-3.914238,-2.929376,4.481254,-7.696118,-0.074269,4.195164,-5.203862,-5.301743,-5.169699,7.724384,4.885897,-2.176781,-1.925442,-7.920973,-9.211440,2.168687,-6.885807,-1.654261,-9.876596,-0.357913,1.724945,2.248437,-6.722073,3.020518,-0.709658,8.124380,0.049184,-9.848830,-1.934161,-7.643021,-5.578943,-3.718058,0.401436,-0.110030,7.051313,9.663375,-4.920728,6.229642,-0.878027,8.858630,9.522241,-0.169718,5.232070,6.799864,8.450143,-0.275453,1.380617,-9.944652,3.330654,-1.873900,4.599147,6.481452,-4.729182,-9.620434,-5.221216,8.651441,-9.305184,-8.122594,7.114157,-0.312038,-3.263713,-7.946810,8.882600,-9.349594,9.985973,1.158850,-0.701573,6.954204,2.037988,-9.886806,7.353383,-3.120087,5.207785,5.353917,-3.339287,-9.158428,3.237185,-1.034356,9.065474,0.257247,6.067755,-7.901304,-1.181561,-2.950220,5.122171,3.852713,-5.535706,7.139147,-5.104744,-8.192744,-4.514510,0.659115,9.924926,-0.517728,4.160573,-9.785678,-0.437695,-2.706979,-6.324185,9.256292,9.311389,-1.776394,-5.958877,-7.750672,6.386780,6.760176,4.341303,4.514460,-7.202978,7.633384,3.515781,-2.560409,-7.764952,-1.185148,2.818009,7.139303,-3.414638,-7.445589,2.663509,-2.612049,-2.109567,-4.080210,-0.599796,-8.902560,8.657924,-3.433695,3.009136,-1.049899,-0.752906,-3.614870,-3.570739,-8.213070,-8.693913,7.930530,1.818940,-3.609070,4.729140,5.057444,-2.167593,-9.618411,-6.007022,-6.365121,1.890390,4.833794,-3.123883,9.764800,5.977860,6.778718,9.690809,1.327142,-2.031135,-2.149644,-6.125614,-7.169362,1.118325,-5.687821,3.270554,-3.220247,-5.450303,-6.322554,4.371781,2.322653,-0.447111,-6.415013,-1.872464,-3.471089,5.231356,-2.731571,7.861595,-6.013671,-8.977607,-7.828325,-8.764754,-8.403015,-4.843905,3.313424,5.703344,6.291877,2.839138,5.481366,0.215655,7.164537,-9.658060,4.999007,-9.806025,-8.570004,-1.166396,-0.612579,3.421007,0.699505,-8.494786,-7.997315,-4.222638,2.182550,3.107857,5.902428,-8.626451,-5.671869,-0.053668,-5.922896,7.707255,4.747389,8.707339,-7.337892,8.603055,1.530488,-5.714279,3.767361,3.203671,9.677922,8.330664,3.209697,7.031239,-2.597073,1.233171,-2.976284,7.182497,4.159225,6.346826,-1.913924,0.356183,-0.110890,8.001200,-9.122015,-0.166037,2.660052,-7.455119,-9.291058,-3.027324,-6.780844,5.716103,5.679806,-4.915820,-0.653720,-5.479019,-2.263535,-6.550659,-9.679176,-1.139005,-9.010719,-4.999659,-5.649143,-7.724417,-6.994344,6.770402,7.190134,2.280272,-9.530757,7.504463,5.441186,1.673662,0.995363,0.960007,2.724448,6.675349,-1.651010,5.046103,-2.206303,1.736411,6.587646,7.600939,-1.596009,6.684330,1.304138,0.633780,-6.175163,-4.906087,-7.673480,7.791543,-3.625212,1.852408,-8.451280,0.971878,-1.557313,2.994787,-0.216055,-8.771456,0.362862,8.519094,-1.467823,-0.355983,7.694158,4.153515,-8.698075,5.073494,9.605731,6.832422,9.471471,-9.618243,-3.507578,3.770554,3.151812,3.229721,6.326161,2.809192,4.038242,1.819384,-3.599769,-8.182176,0.924965,3.844360,-9.091046,3.028878,-0.378831,3.753573,9.613109,3.384718,3.884817,-5.758936,0.359231,-5.300179,0.008361,2.831729,-3.539946,-9.000265,1.298350,-4.611051,-4.503842,7.049890,-6.834337,0.375987,-1.603559,-0.757521,6.204533,-9.076803,-1.316097,5.265930,-3.275306,7.565113,-2.872896,2.698781,-7.099057,0.407072,3.386576,0.336365,-9.075337,2.522399,2.718429,-3.668152,-2.551218,8.270265,8.848488,-3.366039,6.833705,8.626236,5.327677,4.019222,-9.148495,3.922480,3.281652,9.953014,9.660921,-9.994435,-8.256709,-1.824333,-1.134345,7.452262,-4.461004,2.016632,-3.425623,-7.660260,8.360615,3.048400,-7.985428,2.154052,9.759133,3.252265,-3.055843,4.398199,-0.136360,2.068483,7.130323,8.732006,5.480194,4.083126,2.300971,7.635152,0.812470,-8.622995,3.794139,8.164231,4.387141,-6.401417,8.024464,-9.901059,7.191434,-5.645598,3.706133,-6.467593,-0.525322,-4.806395,2.358237,8.415016,-5.398144,9.366986,3.573116,-8.178629,6.862870,-1.476097,-6.959917,3.908220,0.040022,-9.055280,7.881526,8.697908,-2.392353,2.034362,5.158807,-7.479242,-6.669140,-1.981871,-4.396408,-3.695970,4.386340,-9.999687,-7.823213,7.122409,9.087966,-1.087671,-8.781395,1.280302,6.605114,1.607879,1.511518,-1.431905,9.236423,0.656916,1.353109,5.386847,1.202563,-0.402846,9.190226,9.047635,1.060934,5.022967,9.405755,-3.078299,8.527752,9.348584,2.522581,0.119015,-9.206269,-4.470059,-7.554669,-3.790851,-8.154461,3.114255,-2.294382,-3.269262,-7.137055,-0.172012,-8.707891,-8.370740,-8.693799,-6.946513,4.387469,-2.660699,4.103250,9.094855,-3.245089,3.129533,-6.373194,9.021766,4.428256,-1.749510,7.102377,4.247574,6.576963,-6.667193,4.228024,2.660821,-5.142761,6.239809,6.070038,8.512325,-7.748989,-3.704035,-4.649081,-2.679033,7.092515,8.710169,0.258932,5.249732,6.663368,-2.688561,-2.496631,6.312533,4.075669,-8.550478,-2.083010,-1.130095,-2.772454,9.043367,-3.801545,-3.139364,9.387591,4.070788,-7.821316,4.116944,-1.922501,2.784404,-2.674709,7.901600,5.910339,-9.162453,0.434253,-6.394747,4.156343,-2.212890,6.569386,2.959094,4.243963,1.042541,0.915449,0.503831,-0.108056,8.268383,4.203838,-6.096111,-4.362324,-3.336411,-3.822319,-8.276333,4.272509,0.857695,8.857321,5.404260,5.700216,3.414548,2.857968,-7.110962,1.559251,-7.354054,-9.276047,1.600485,6.734187,4.309165,-3.686427,0.181975,-4.124690,7.395474,-3.033250,-2.079270,9.581032,-1.175713,-6.508645,8.372174,-5.660633,5.857030,-7.908836,-1.545165,-3.272878,1.689891,9.797729,-2.648116,-5.306714,8.265300,-2.258404,-2.341380,3.135742,5.543466,-7.186051,1.928346,-4.944468,8.029023,6.066385,4.774425,1.215389,7.093802,7.724602,1.867054,2.591956,-3.681286,-3.592934,6.560876,-5.457349,-8.397137,5.815565,8.110486,-6.680189,8.452772,-4.397864,0.586041,0.166026,-1.888520,2.600387,-5.640475,4.626419,-5.702100,-5.638815,0.533450,-6.227750,7.302828,-6.868321,-3.520619,5.810411,-6.252837,-4.824938,-3.723057,-1.506089,-4.991433,-0.379496,-0.200923,-5.357293,4.170534,0.371426,6.259508,-6.587304,6.775760,9.915000,4.526566,2.617981,1.375481,-6.887914,-4.555110,-0.322905,-1.357035,0.681888,-3.434248,5.073029,-5.169714,1.262923,8.363227,-2.454278,-4.048634,-8.125221,5.552342,5.907067,3.517878,-1.256035,1.470228,-4.882787,6.993356,-0.356740,3.392010,3.045923,-0.074506,6.686905,7.779786,7.522112,-9.090300,7.163457,0.397385,-3.331049,-3.297529,-5.999654,2.592472,3.041105,1.217145,5.275111,-4.744855,-8.321825,1.866877,-2.208075,-6.635124,-8.690504,2.917282,-7.418526,-6.721995,5.958070,3.164623,-7.449931,-4.854993,0.040268,-5.065480,7.811116,6.501478,0.116674,5.503592,9.610645,6.633810,-3.449034,-8.794308,-1.352202,9.085354,2.710470,3.876447,-3.759761,-3.195824,4.168909,-3.336601,5.934319,8.759654,-4.045716,-4.240129,-1.405696,7.027081,-0.526522,9.623004,-0.027724,-9.480887,6.112594,-0.847999,4.027463,6.805808,9.534930,4.649585,4.688076,1.438411,-1.644173,-0.902702,-8.045862,5.643674,4.905930,9.213168,-7.656386,8.130822,9.830764,5.215383,-3.124757,-8.929905,-1.252729,-0.059542,-3.305577,3.483326,9.795885,2.317460,6.042222,-7.616218,2.642881,-4.020622,4.016223,8.689769,2.122594,-6.206529,8.151791,8.964377,-2.472081,3.674651,-9.426444,4.308698,-1.099282,6.861188,-1.163640,-6.382528,4.513963,1.206131,9.006224,7.437589,7.058061,-9.829612,-7.827990,-2.128419,-6.613047,8.714749,-2.640713,-5.508393,0.380331,-2.774135,-2.073841,3.540354,3.358268,-5.029048,4.910872,-7.313137,3.556144,7.122331,-4.585347,2.125346,-8.199218,8.140781,7.561713,5.201246,5.250218,-8.676072,1.651255,2.913056,-9.977673,0.725182,-5.663542,-7.370210,-3.363841,1.957481,2.959373,8.050076,-9.154691,-1.753637,0.614481,-7.391499,3.768227,-6.815028,8.974442,-6.774018,7.972109,2.849282,3.244742,-0.290860,-5.722320,-6.603505,-9.313331,5.737058,6.717646,-6.626391,4.732792,0.258349,-4.241742,4.548729,-4.830906,3.717724,9.383361,3.556633,5.153792,4.575335,2.839103,7.971486,8.156251,-7.475720,7.769322,5.009052,-8.865561,2.705621,-0.175785,-1.137380,-3.041231,2.073425,-2.606968,-2.861346,-5.575389,3.138151,-9.219691,8.960871,7.434239,-2.303024,-0.901575,-7.650829,-4.111227,5.675496,-8.620901,9.807744,-3.903094,6.521681,3.310960,-3.472971,8.010587,-4.816604,-4.167164,1.953349,4.037643,-7.016667,-6.642275,-0.523783,4.163722,8.002935,8.304919,-2.601712,0.629242,7.766735,-4.165767,-8.280806,6.084464,2.121218,-5.803970,-6.456137,-0.450096,-6.761942,9.605163,1.335618,-7.982110,-7.277360,-4.463435,4.219423,-1.416029,-8.211129,-5.618692,-0.569598,6.025282,-1.051850,9.405084,-1.727573,1.872848,-7.716383,3.246029,6.298010,-8.987826,-4.446779,0.540360,4.776351,-1.566374,-6.181225,-1.498898,-9.873947,-4.789603,-7.785019,7.897312,0.321286,0.969249,9.020489,4.845976,-9.292344,3.114929,-3.615104,6.014504,-7.700376,-2.575967,-1.761127,-1.713506,-8.306122,5.812422,-6.669877,9.738199,-7.221922,5.943411,-2.062104,-8.190972,-5.961473,9.616623,-1.151400,-4.822194,-2.424936,0.460955,-7.220920,5.242675,-0.640526,2.675292,-0.089422,-7.643869,3.189184,-1.743176,8.656429,-4.673984,-4.899059,-6.303085,-7.344368,-2.348094,2.407508,-4.923461,5.377566,2.042381,-2.178270,-3.231663,8.314066,9.147072,-7.893134,-3.015235,2.462733,0.922067,-8.099729,-0.699302,5.156713,6.317913,8.081014,-4.977361,-0.652862,-7.245829,-6.596079,8.145049,-5.128951,-8.965439,-8.932690,-3.826776,3.879226,-3.413665,2.017237,6.936413,9.942105,-5.514414,-0.533824,2.464194,-5.435366,6.206114,-0.255263,-6.862703,-4.136546,7.347506,-0.718483,-3.126665,6.639691,2.015168,0.745357,2.164970,-4.098761,9.555793,-6.208727,4.591629,9.195748,3.929975,9.701226,-7.602729,-9.658459,-0.753980,7.815289,6.404629,3.660961,1.698332,5.219966,6.924147,-6.326173,-4.521121,4.716981,3.064498,-1.431505,-3.350564,5.157497,1.236311,-9.795887,-8.283339,-5.813738,8.396898,-8.092666,6.912021,7.839230,0.216484,9.729069,8.134990,3.200597,5.280723,4.836795,6.046923,-6.415579,6.972328,2.262329,-2.904907,7.658729,0.623085,7.968428,3.500464,-7.231381,-1.883630,-8.803924,-1.649193,9.918057,2.473211,-2.055329,4.632383,-6.784064,4.414078,-5.007157,9.336652,8.053035,0.991404,0.611919,-1.253817,-9.902620,-6.471217,-7.706738,-0.479144,-9.642593,-5.426133,9.871758,-2.221826,-2.429078,3.065318,1.543826,-1.241948,7.826280,8.706950,-5.213387,-3.068618,7.325570,8.269622,-0.434133,0.290551,-6.655165,2.528579,0.220889,2.248505,0.653502,-7.879777,2.252629,-8.009806,-4.286101,-3.079962,8.159640,8.914215,0.833078,-9.080308,4.055680,-9.015683,6.468670,7.325534,7.867819,0.147795,9.624037,-3.667134,-7.701441,1.407025,-2.218229,-0.242860,5.530088,-9.986601,-5.049164,-1.241807,-9.988969,4.657599,-9.024877,-9.160716,8.230017,-2.778823,8.173148,-5.234103,6.895071,4.867252,6.628391,6.048494,1.338074,8.431314,-9.670291,4.003822,-4.951143,5.565220,7.173268,3.915972,3.987532,9.692290,-8.436620,-1.730686,-5.852097,3.433990,9.360763,-8.120541,5.436249,2.326840,5.533184,-5.997390,3.295840,-0.719073,-7.416146,-1.391554,5.462720,-6.216011,7.376300,-7.305440,-7.874955,7.019447,-3.202521,9.394275,3.215852,-3.400009,0.820146,-4.886005,-7.484710,-5.375722,-2.654969,-5.346938,-1.972598,2.967921,2.791236,4.129666,-8.047207,-4.434250,-3.177914,-9.999495,-3.372631,-6.767569,4.783295,-6.172486,2.985565,-2.597857,1.675830,-2.012486,-9.403389,2.123590,6.372853,6.578013,5.375837,-1.494240,9.061248,6.023294,7.344138,-1.339510,7.203155,-5.485641,9.908403,-5.465847,7.069892,-6.400526,5.890571,-8.093937,1.897595,-4.338604,9.562377,-8.445431,4.419327,-8.036662,-3.233217,9.313268,0.649035,-4.258722,1.830377,-8.287472,6.357194,-7.381056,-1.443569,8.318962,-4.680432,9.381750,8.405446,3.708306,2.610523,8.986886,-7.066609,1.086561,1.705653,-0.812916,7.678049,9.152422,1.315350,6.344449,-9.829145,8.641699,-4.774134,-6.420326,8.045375,-8.005192,5.751641,-7.218961,-2.805862,-2.591629,1.891184,-8.606835,1.815375,-0.893535,8.349760,-3.468854,-5.550067,5.780724,-5.468128,-5.757181,7.737220,5.781908,3.049160,-8.812256,9.435554,9.523871,3.016553,2.221721,0.202176,2.394696,1.264203,6.502395,-5.644626,-3.468745,-7.064106,-0.076323,3.028901,9.090618,8.032544,5.684774,-6.331078,3.129304,-3.636312,-2.269506,-3.098814,1.134373,5.516208,-2.660952,6.797152,9.353085,6.048565,2.159773,9.753209,7.312830,-4.855967,5.286009,6.530125,-0.991146,-4.755832,-2.609382,-2.452998,-2.508267,-4.442191,6.322764,-2.591673,3.418096,-9.239443,-5.111252,3.640390,-9.391143,-6.799450,-2.511526,2.309446,-0.588572,8.550951,-6.577757,-2.989420,-3.993816,1.633047,-1.971010,-3.968704,-4.833411,-3.425395,-2.637785,-6.505823,8.288940,-7.228808,5.264222,-9.922612,8.668087,-9.823730,3.949239,6.031767,7.534955,-9.735400,-4.967674,2.743171,5.877434,7.545197,-2.881987,5.869038,4.309283,9.796994,1.649462,-7.660567,-5.841288,-2.156524,8.968887,7.704258,4.863213,-3.211696,-0.937294,-4.838893,0.723268,9.768669,0.093379,5.479009,-1.494808,9.321595,-2.591856,8.470465,-5.917671,-2.249420,6.990774,-9.232213,5.544582,-0.697164,1.368039,-5.382640,-4.975394,-8.055625,-9.959208,-4.003834,-5.823773,-6.365070,4.801813,8.172346,0.450982,8.137733,3.066534,8.885354,-2.697820,-5.294755,-7.370924,-5.065624,-5.659874,5.862879,-3.186618,-6.961908,5.150449,4.349738,-3.407519,7.208351,9.429441,-4.554314,-9.918002,2.415068,5.451168,-8.629312,-6.507553,-6.081277,0.425655,6.679987,-8.736716,7.796809,-9.711393,-2.818176,5.226557,1.419753,3.243901,-0.351906,3.338350,-6.766086,2.120445,7.024570,-9.802634,2.253184,2.738187,6.275768,-9.072552,6.518595,-2.328816,1.265345,1.587639,-4.129619,-3.101724,1.950806,-7.164380,-6.183354,-9.844600,-6.373200,2.003392,8.400097,-3.206228,-9.120826,7.775306,-8.354112,-8.699601,0.977072,-2.903262,-6.391635,-0.213735,-2.078176,7.820459,4.611826,-4.791812,-7.414071,6.995435,-4.938670,1.004993,-8.227572,4.668164,-8.587684,-4.312004,4.091713,9.733932,3.164149,4.615830,-0.558782,-7.354197,8.966396,9.257115,-4.075150,2.192970,0.853804,-5.951099,6.665831,-0.387724,2.813427,6.040305,2.950383,-6.586491,6.824147,-7.339262,-0.653708,9.067854,-7.481138,-0.702574,6.542944,1.791763,-3.301859,-8.336047,8.241133,7.156779,2.686291,-0.312703,2.216511,2.111802,-0.047154,-6.426886,-3.369329,-9.110987,4.432790,6.952944,-5.692802,3.387464,-9.592459,-8.022807,-7.179928,-3.414090,5.693974,-3.231264,6.878027,1.396803,8.154610,3.514812,4.171181,-1.163416,-9.817261,0.013742,1.890862,6.711385,-7.017332,1.622244,8.240082,-4.937123,-5.385276,5.162480,-6.489034,-7.371919,-6.233653,2.401148,3.566639,-6.788545,5.330239,3.593686,-8.414527,0.691324,-6.880015,3.598342,-5.815747,-0.823110,-4.706546,9.189889,-0.731510,9.791982,3.932184,-5.546870,-6.991280,-4.670477,-6.112747,-5.138895,-6.689059,2.184602,7.991347,-2.769883,-3.695646,-7.772866,-7.568914,9.992306,2.362504,0.717558,5.961936,-0.284822,7.882286,-7.669994,-9.405814,-1.902113,-8.763763,8.357657,8.201203,9.908159,2.251077,-3.569300,3.991041,-8.365704,-8.566998,3.619275,-6.512973,-9.640412,-9.334323,1.680308,8.538537,2.210003,-6.095130,0.216203,-6.200314,3.036599,0.449951,4.620122,-2.283803,0.970828,-2.740621,-4.061309,-2.575893,-7.664631,6.300297,3.352710,6.484707,-4.212206,-2.207600,5.219399,8.989241,-1.895072,8.030727,1.484519,7.984216,-1.747341,-3.589898,-1.614733,4.550477,8.748840,1.943932,-1.536526,-3.664179,-3.741659,-2.979061,1.976988,-0.485063,-6.596944,-1.347732,1.204814,2.054080,5.885242,3.516027,-0.026468,-4.938331,9.274654,1.110293,-1.647935,6.457991,-3.181411,9.207481,6.970884,9.520456,2.992353,7.107379,8.972060,-3.034616,-4.630040,9.089126,7.293312,4.885617,6.260790,-3.434853,-6.138411,-8.009430,2.532298,-5.942749,4.793545,3.054696,2.674260,-4.219569,0.333146,2.546421,-6.143739,-2.808861,-5.070584,-2.133919,-3.206428,-6.890151,-9.410329,6.146618,-0.191197,-2.439281,3.321839,-2.247050,4.614469,-1.532223,3.737858,-2.400317,-6.234522,5.335156,-0.488741,-6.017291,-0.251244,7.228545,7.874847,6.602121,2.456857,7.507340,1.749669,1.735982,-4.437721,9.027551,-7.469981,8.849230,-1.730213,5.989662,0.021597,-3.376672,-2.022826,-5.477952,-5.883258,4.680340,-3.644665,4.612160,-3.546640,-9.122565,-8.556988,3.916801,3.092624,7.617433,1.115578,5.599258,-5.644916,9.503093,9.302598,-9.907589,5.590306,9.386914,-8.045680,2.178079,-5.101628,-5.050633,9.136026,6.178080,-8.730407,-0.826529,0.623260,-2.755558,4.565455,8.609474,-2.551432,3.679463,5.098765,3.071711,2.430648,5.321598,-8.979684,-4.051977,5.688624,-8.634334,-5.694814,8.037710,-6.722476,4.895164,9.735397,5.689461,-2.575912,1.376041,3.243743,1.902938,5.531374,-3.510288,-7.629874,0.971687,-6.382386,-5.695028,3.266287,0.940089,8.640734,5.684285,3.979725,-2.989797,5.637086,4.975881,-7.619660,7.874425,2.229165,2.259046,-7.285444,4.555250,7.261526,6.072815,-2.822090,-4.147508,9.075214,-9.643696,-8.465025,-1.241494,6.919954,5.100348,9.453811,7.229250,-0.146322,-2.744984,-7.881614,-6.632520,7.733969,-6.726684,-8.649131,-8.659741,-8.529309,-3.203635,3.827828,9.278982,-5.431615,6.260039,0.236928,8.433692,1.634759,6.131022,9.990860,8.075830,0.880413,-3.146791,0.114298,-1.173548,-4.637452,-4.954643,4.970852,-4.407145,-3.386129,7.095187,-7.684512,-6.760495,1.666495,2.303939,2.965624,6.032621,-5.124320,-5.540492,-3.938749,-8.983985,7.658894,5.979331,-1.273503,-8.128631,4.575120,-2.692990,-0.155384,8.776561,-1.425798,8.997253,-6.183060,1.716753,-0.667101,-9.911918,-0.971590,8.027812,5.888311,-6.241763,-8.531401,4.433692,2.134734,-4.518860,-1.017513,8.216227,-7.987261,-5.851234,2.964496,-0.953127,8.658225,7.754484,8.672039,2.830594,8.185470,-5.037392,-8.688747,9.449693,8.147908,-3.796269,3.397224,6.059057,-1.361825,-7.516794,3.866236,0.971009,8.997347,-7.833896,-1.487133,-7.685154,1.706544,8.913548,-5.092622,4.316573,-5.890259,6.894513,8.514542,-7.250610,-9.868770,-7.158094,9.277530,-0.027847,-7.317271,1.486417,-0.076408,-4.452182,-0.932001,0.645004,-3.987703,-1.329510,-8.682630,-4.407372,-6.421487,3.112124,-9.384401,-9.255578,-8.851169,-8.807237,9.478582,3.725841,7.839299,-2.823531,1.125872,-4.349442,-3.517970,3.839174,-6.305952,6.726839,-5.534482,1.323033,-2.327813,-0.025455,-3.691789,4.945927,-8.375014,6.123131,-3.867697,4.695662,-3.560890,0.378500,-9.218684,3.212487,-9.376451,-7.427972,-8.011131,8.637633,6.479787,6.998394,6.200949,-8.266290,1.416201,2.096652,4.874478,5.563244,5.939991,-1.568931,6.135341,-3.535204,-4.703982,-3.138740,7.955322,3.510017,9.561056,-8.207688,1.086497,-5.643017,0.816879,-0.401289,-3.519758,-3.593322,-3.680121,-6.551366,-0.843471,-4.382897,8.310847,2.029063,-0.168678,0.324050,9.901941,-3.798080,-2.578585,9.195200,5.141623,-8.699108,-8.971468,4.409943,-9.888387,-8.912062,-9.056249,5.838417,-4.587275,-1.887512,-0.918641,-7.855929,-3.512660,-6.412227,-4.785550,-4.934447,-0.609316,2.499760,6.127073,5.764048,-2.051530,-6.111562,-3.779167,-2.831111,7.036618,-4.046898,8.480060,3.495048,5.331354,-9.110461,-6.896448,0.493897,-0.857392,2.931537,8.735569,2.597473,-5.703111,4.508111,8.608306,9.645270,-8.823464,-2.872171,7.497851,4.794511,-2.620515,-0.176842,-9.037030,8.288286,-0.088206,-8.634386,0.267031,-3.528456,-8.251689,2.360920,2.834642,-9.806953,-2.627904,4.071669,-9.295119,-9.963024,6.365468,9.655492,6.023355,-0.749125,0.437033,3.708903,-1.025566,9.877343,4.547658,-7.264442,0.702075,5.470311,-0.234864,0.637125,5.865915,5.214758,-9.579532,0.784584,0.853298,-5.452888,-5.814661,3.226762,4.913018,6.446020,7.279727,3.716944,-8.470976,-4.382508,-5.329533,-0.944384,-5.084636,-8.990040,-6.870361,-2.799821,3.534815,0.731132,-3.493761,-3.885352,3.475124,6.394730,8.325866,0.916441,5.725886,-8.787506,-9.150980,1.628652,-1.877144,2.596282,8.934251,-0.001548,-7.409655,7.152468,2.242963,-5.459689,7.568901,0.625055,4.647960,2.734416,4.508931,-7.510343,-8.069658,-6.646283,9.524475,4.701728,1.172562,5.362268,9.390280,-5.341543,-1.457857,9.864546,-4.605547,-5.146385,-9.903214,-6.143928,-7.476747,3.487491,6.244064,5.033957,0.424776,5.639916,1.552669,3.387839,8.655432,6.265972,-3.195748,-8.175315,4.151372,-5.322228,-7.565915,3.505432,1.537173,2.163247,-8.122869,7.769036,5.684066,-2.863378,4.788510,-8.912934,-8.022664,-4.796411,-9.858873,6.823532,-1.966466,4.108187,5.620992,4.531543,3.260184,8.938666,2.345800,-1.053814,7.575270,5.127747,-7.684123,-5.102631,3.727910,7.403062,8.688187,-4.305641,1.597714,-4.628732,-7.649857,3.832696,-3.257004,-3.159975,-3.885720,-7.916300,3.361308,-7.386504,6.427387,-3.860667,-5.426840,0.063478,9.603192,8.415295,1.579792,8.499304,2.996915,-8.371311,6.336621,6.514036,8.596716,1.040028,-4.806567,-1.198989,-2.905569,-2.905106,-6.155382,-2.585321,6.091689,-7.977191,6.648068,9.314211,0.599730,-1.422578,-5.736786,-3.157439,-0.748337,-1.089204,7.315167,-7.417807,-4.450200,-3.730848,-0.306620,-3.565695,-2.033363,0.844665,-6.803203,-3.659551,-5.477554,-7.342263,1.514524,-2.083541,-3.820313,-2.434151,9.572591,-7.729896,6.511847,-5.850640,0.397446,-3.217979,-5.633459,-1.181306,-6.394574,-6.808716,0.639220,1.364811,5.622633,-9.855667,-7.081726,7.742468,-4.748673,7.339044,8.111987,9.964218,-6.324737,-3.071195,0.851400,0.124265,-5.572455,-7.839601,-0.085852,-0.077979,0.331636,-2.346230,5.858825,1.023781,5.675492,6.922402,1.311969,1.793155,-8.044638,-0.829709,-7.187020,2.420351,6.344355,0.153071,8.093636,6.545049,-3.969119,2.759416,9.132017,2.239092,0.348586,9.571340,-5.894682,4.640860,0.216622,-1.051917,8.181054,-1.827712,-6.226334,9.498794,5.019040,-4.702536,-1.914225,1.563201,4.708326,-6.262947,2.001137,2.363333,-1.246798,9.866957,-9.084009,-1.960953,5.466069,-0.259324,-0.973680,-7.571021,-5.304925,3.691682,-0.481094,-4.454167,-1.324902,-1.629401,0.295816,6.222542,-8.689857,3.045906,-2.561423,2.730180,-4.648231,6.170238,4.948709,-3.416735,4.383397,-2.995212,-4.472685,5.114266,8.172393,-2.532518,0.417948,-7.598285,-6.102178,-2.292369,4.141283,3.632755,3.564992,-0.002742,-7.018706,-5.560156,3.982737,8.345125,9.958174,-3.940821,-3.839784,8.537595,-3.718325,-1.558234,2.427615,3.866060,-8.326072,-4.535449,-9.480619,-9.704853,1.003583,-5.403952,8.207063,-3.089594,-6.156912,8.805650,-5.824708,-3.679794,-5.703265,5.893943,9.484157,7.985486,2.845473,9.656895,-6.877239,-8.143458,-6.714236,-6.333684,-7.016208,-0.852804,6.784053,-4.138821,4.391260,-5.367051,1.203152,3.031121,8.843174,-2.858405,3.231337,-4.343275,5.479362,0.817498,2.702660,1.241436,2.632034,-2.324433,9.638823,-2.731012,3.763304,-2.436982,-0.839427,9.307149,-7.749818,8.038909,0.878397,-0.380375,-9.942267,-7.508880,3.058616,-5.094231,0.375620,-1.204278,9.307354,0.728102,4.529088,7.975096,-6.872746,6.072741,-3.981067,-3.511013,-8.866312,-3.274924,-1.155762,-4.642008,-8.200891,-3.543367,0.090556,-5.157253,1.238090,9.871201,8.901280,7.321872,3.662552,5.000704,9.921537,4.562965,-2.498088,-3.746772,-3.061937,-7.189615,9.081306,7.130666,3.166223,7.660128,7.433506,-2.235917,0.783604,-7.091415,-5.456269,-6.679393,5.911058,-0.192720,3.111601,8.411516,9.783053,-5.308208,-4.431598,-3.895498,2.362601,2.187622,-0.903698,-9.248530,0.016420,2.525652,-7.571830,1.620890,8.337161,2.349756,-8.671573,5.391302,-3.306226,0.265123,6.582655,4.336592,2.751469,8.159700,-3.547300,-9.030845,0.569513,7.331834,9.007715,3.371730,-0.501299,-1.996514,7.277582,1.341216,4.009651,5.243708,-5.546353,-1.070275,4.159161,9.360600,1.882878,0.235098,4.194713,-5.459419,8.968377,-4.390050,-6.063142,-3.723944,-6.143777,2.852534,-6.043747,-6.146045,4.012363,9.583651,-7.850736,-7.277681,-4.949036,-2.711811,6.825754,-6.495577,3.461466,-1.202796,7.053513,5.453396,-9.772683,-6.203744,9.036098,2.441678,7.998911,3.844698,-1.478243,9.142418,7.825048,-4.540771,-3.767173,8.666004,6.538791,6.410906,3.036989,-0.395633,8.881612,-1.461081,5.171218,-0.913005,-1.812397,7.738133,9.411571,9.877420,-1.161235,0.450896,9.821941,-3.999940,9.587962,4.656888,1.824952,-9.232376,-4.941693,2.336904,0.789398,-1.246190,-3.758601,-1.353021,-5.951071,-9.318926,6.141647,1.361203,7.503452,-0.913990,0.940942,4.359636,8.939609,-6.431409,-5.178406,-3.045603,3.748601,-6.828152,-3.360676,4.221975,-1.078217,0.896988,-9.021836,-7.725225,3.941651,-1.760827,2.282326,2.267618,2.798284,-9.368385,7.438846,9.581081,-1.436739,-1.465492,-1.451413,2.870626,-4.375927,1.369391,-5.519091,-4.483483,-4.106389,-8.390923,-3.874901,-3.660900,5.625041,2.014378,5.436161,7.949465,-9.855891,-0.254182,-1.913347,-8.886656,8.937488,3.213487,2.011766,2.814731,-8.236614,6.761906,6.438511,-8.362317,1.471054,1.481854,2.594755,-0.396220,9.176636,-3.664562,-2.147738,-1.082064,-0.382437,7.319950,0.786357,0.244737,6.773828,-5.058554,3.229499,8.500667,-8.377624,7.760509,-2.970126,-1.044253,8.145784,6.841107,7.628359,8.854684,0.792679,9.433595,4.760397,-6.444374,-5.712019,9.669411,9.190104,-4.049150,7.581325,9.522760,7.383681,9.726332,5.835038,-5.027518,-7.175370,-1.537624,4.189201,-3.278229,0.901291,4.390766,8.748593,9.698358,5.137565,2.663934,1.598711,-5.188692,-2.971196,8.976162,-3.431697,-4.164444,5.917479,-1.836940,-9.394613,9.622320,5.798428,4.579772,7.549190,-3.454640,-8.422838,-2.276789,-9.077581,-2.907398,-1.935723,-7.736803,-7.640113,-1.057611,-4.793309,-3.089685,1.005154,-0.426185,-2.915971,-9.170419,-7.811986,-8.607857,-5.296996,-3.455910,-4.824443,0.890048,8.014215,1.500808,-8.794140,4.254189,6.718919,8.399124,-6.386684,6.757022,-2.421601,-2.800702,-6.593669,5.072630,7.355051,-2.607237,7.987007,5.230863,2.839161,-9.783732,-2.691644,-7.193125,8.118757,-1.222530,8.468983,-7.729346,6.237853,-6.865414,4.467782,-2.631166,-6.018616,-8.512948,-9.523741,-6.916069,9.976437,1.480027,-8.143893,5.464803,-5.739214,1.315888,4.774700,7.020626,7.382043,8.539355,4.829872,9.687178,-8.714338,9.053554,1.185294,-1.886328,-7.196141,-9.591181,-3.508300,-3.472888,-4.883554,-3.863762,5.455459,-5.047310,-5.490852,-4.847951,-6.499982,8.257658,1.670733,3.803503,-7.981459,4.764717,-0.183719,1.367147,4.990069,8.745032,-2.305473,-5.420724,5.187293,-1.529284,-3.460830,2.472964,-7.599851,6.526875,-5.346111,5.916011,-1.965195,1.670277,-0.951021,5.797162,8.091237,3.980555,5.122696,2.862661,2.464104,-7.740034,-9.643502,-5.782991,-4.268716,6.177186,-1.301894,5.340053,1.961147,3.380022,8.419286,-4.561736,4.832551,-0.620529,8.087222,8.398695,9.686435,-2.469899,-2.821499,8.620198,-4.924858,0.658731,1.218909,4.132328,7.769072,-4.871471,-6.653119,1.328427,6.417200,-5.079632,-7.612248,9.422951,2.390092,2.476465,-9.203133,-3.481018,7.386887,1.362115,-9.755916,-2.207333,-9.370917,-1.117088,2.486801,-1.964025,-1.989496,3.361327,6.352137,-4.590725,-8.181162,-1.955091,-1.553134,0.068560,-7.847533,-7.497071,1.979173,-8.380990,-2.118665,-0.794507,2.515301,-4.053720,4.225217,-8.233013,-7.953004,5.096363,-8.264437,1.736455,-3.053186,1.871373,5.534347,5.336189,-2.752920,-4.436015,7.144022,-4.190952,-0.801460,-8.647322,-7.612676,-6.615166,3.615258,0.995817,2.178871,6.065839,3.755280,-4.021687,-1.092410,3.742200,3.809482,8.384424,1.212851,8.974262,-9.908833,8.320091,-7.588144,5.270222,-5.261185,-2.726667,2.913571,7.850466,-8.274400,-5.811197,-4.137836,9.943118,0.485134,-4.356988,-1.180858,-7.119804,7.680868,6.038881,0.544604,2.581730,3.273239,7.729088,0.021792,0.190728,-5.029720,5.896813,4.964704,3.524058,4.103626,2.943703,1.687699,1.579189,-2.388301,9.213204,0.796625,8.871862,-5.204893,-8.158126,0.375169,0.894387,5.724270,-1.708408,1.623963,5.942757,9.419703,-1.457575,8.783454,7.004301,-8.120265,4.499529,-4.028664,-4.557576,-1.833237,-4.796205,-7.019565,4.956921,-0.524866,-5.178665,2.959631,4.580975,7.970838,-8.707805,1.026501,-4.220431,-4.510661,7.960475,-6.246896,3.550499,-3.955466,-4.330716,5.396171,-7.478532,-3.607922,7.436519,9.993642,-9.019849,-5.686089,4.213798,8.695405,3.176772,7.722570,-8.941856,-6.039804,-6.868694,0.550081,8.456918,2.306760,7.812242,-6.785197,5.309680,7.677211,-3.339695,-6.341817,5.271064,4.870655,4.379316,2.116800,-5.065746,5.105257,9.047798,-8.038205,7.015696,-2.032077,2.719232,0.379956,-2.681941,-1.652956,-3.581748,-8.919417,-2.664060,-4.088479,0.414290,2.449799,9.901857,-1.808934,-6.866703,7.375824,-0.506442,-9.338663,2.089784,0.769380,-7.931144,-6.002089,-2.954984,-6.630239,8.127411,5.639342,-9.972425,-6.259284,9.247463,-4.943520,5.172981,-7.540567,-5.034328,0.965146,-6.690329,7.539539,1.547343,-3.146143,8.724604,-8.151673,7.516449,2.608066,7.413387,-8.279116,-2.793997,-4.051486,-7.395463,-7.563488,3.619257,-3.131869,-6.736020,-2.264874,-5.401876,5.278871,6.536327,-8.041493,5.768473,-7.852541,6.532874,-4.021432,-7.404426,-5.528928,8.540923,6.398274,-8.608545,-8.366792,1.987642,-5.053552,5.148557,3.522594,-5.520374,-0.144319,4.896788,-3.141607,0.953482,4.879226,4.953220,-7.601693,-2.418924,8.089075,-1.480116,5.761803,-5.971732,6.078847,0.739285,-9.158829,-3.651921,-5.898825,6.081368,-8.805874,1.146780,-1.316278,0.938403,9.106410,-1.229948,2.778646,-2.566289,8.141851,-4.231933,2.012417,2.547505,5.681411,-6.876921,-1.235937,-9.973118,-3.339329,-6.542131,-7.553079,2.294670,6.275711,-3.135313,-7.606673,5.354690,6.005564,-6.508646,5.917840,-5.253475,2.306782,-0.980320,8.045861,1.967345,-2.004405,-6.178283,8.596999,-0.524001,-3.900112,5.181012,-0.764982,-9.671851,7.490050,-9.527540,-4.259223,5.392758,2.928641,7.422734,0.626524,-2.782690,-5.652187,-4.811076,-5.381067,-6.218854,-3.288310,-7.348785,-4.413102,-9.707110,6.672825,9.170675,-2.420750,-4.548844,-7.495091,-4.422862,-0.409920,-9.711101,3.642449,-8.895544,6.564978,-8.601184,1.513543,-8.680585,8.003599,8.809062,7.952613,6.785119,2.126659,3.551948,8.344843,7.717104,-5.008863,6.402901,5.038126,-6.055554,-1.711825,-1.631501,7.547721,-8.820960,9.212285,3.586251,-4.441678,-4.950422,-7.217341,3.098483,4.228988,6.657774,-9.637094,-6.095527,4.080474,7.022063,4.365078,3.538879,-3.443046,-5.623923,6.876080,8.061674,-0.946691,1.067634,2.083728,-8.438823,-6.774748,7.765336,-9.410902,-2.172699,-3.913626,-1.251313,0.608584,-9.422891,5.599066,4.728768,-0.121910,-4.442356,3.273081,-9.676696,-1.271932,6.136840,-9.669402,-2.800664,-5.756065,-2.896573,-2.372663,5.735274,-3.807231,8.897024,-4.611011,-2.836303,3.161663,6.386006,2.888416,-5.208829,-9.030782,-2.417245,-9.514729,-9.399054,4.035106,5.739596,6.322045,8.696135,-4.684126,8.478643,6.073544,4.842598,-3.884954,5.598738,-6.324651,8.023011,-6.766239,-3.911150,-6.582594,2.028430,9.477570,6.048615,8.149470,4.776294,-5.889171,-0.822843,-4.882607,-6.841058,-9.691668,-6.241463,4.534835,-7.423282,5.880126,-7.882284,8.644804,4.979044,-6.206259,2.009966,3.818442,6.542430,7.530884,-4.019892,-2.976514,-5.711777,-8.313236,0.271083,-5.497433,2.018904,-2.038217,-8.091787,-4.616744,7.664998,-7.517082,-5.034084,5.114463,3.541084,-9.876132,-3.588220,8.315893,0.167042,-4.498074,4.414194,-1.169784,-4.560090,9.721016,-3.866469,9.799050,-2.922337,-1.139012,1.600601,4.718865,-9.614161,-4.919441,-4.411370,7.156073,-0.359568,-3.888738,4.726547,-8.761242,-9.796551,-4.902652,2.465493,-0.674492,6.701285,4.252707,-7.360468,-5.625361,-7.252649,7.424881,-2.953817,-6.593724,-1.401961,-3.698356,-8.091312,-9.218196,-9.715176,1.603482,-2.537542,-7.070485,2.736368,-7.128853,-1.738450,-0.655753,-5.041186,9.985417,3.540591,2.533465,-6.282458,0.456087,-0.130782,8.032962,-1.000085,1.320633,-1.688743,-1.804933,9.012416,9.991934,4.396919,-1.740596,-1.870377,-6.566618,1.084916,5.626817,-5.192430,-6.854311,-5.381396,2.755682,4.214973,9.513220,-6.053380,4.566709,1.974184,8.748962,-3.045172,-7.296446,7.324303,-2.232841,-8.096081,8.302532,-9.480199,7.020822,8.506916,0.820886,8.943185,4.063062,9.503199,1.750747,9.808575,1.329821,-0.486705,-4.510367,4.350640,9.782880,5.738830,-6.196741,-2.794424,-8.241204,-5.161148,-0.746737,9.903682,-9.258371,-9.660424,4.032540,-0.335400,-2.909919,-4.816614,2.463502,3.988763,5.112821,4.535301,2.895169,1.968797,2.141471,4.838237,-6.280854,6.594752,0.470819,-1.021053,-5.641668,-9.391697,-4.740882,0.311771,-8.901410,-9.505714,2.416663,4.497623,3.608620,7.768288,-9.536286,3.390642,0.172693,7.206390,-1.850958,5.673832,0.011454,7.720912,-0.347930,7.914651,-1.877401,-7.592931,1.934535,-0.627961,-3.600742,0.753826,-9.832498,9.332481,-0.529410,6.856556,2.096730,8.579723,-5.933483,-3.602800,6.724821,9.578545,0.702130,-0.044177,4.860796,1.326442,-9.448379,-8.103412,0.360808,-7.000030,8.762320,4.504215,-4.187106,7.979192,6.680506,0.825386,4.907646,-3.976442,-6.852495,0.543979,0.805751,0.516705,7.860035,9.626487,-6.029049,-2.546087,0.660533,-8.246528,-1.855618,-7.744321,2.872864,3.128934,-2.754734,3.129858,-7.284931,-4.109725,7.633610,2.459443,9.729655,-6.236147,-8.892192,9.404034,-5.785960,3.958706,2.324692,-5.717904,4.560572,5.733043,-3.075785,-9.966061,7.740122,-7.517682,-7.740460,-8.258106,-1.698533,8.276389,5.568898,-4.825129,-1.355134,5.445029,3.833326,-4.498160,0.250230,-1.713690,-7.247085,-3.039176,9.471539,7.020770,-0.146291,-0.933643,-5.352121,2.397581,-9.113108,1.782612,7.989149,2.883584,-1.881527,2.567130,5.765915,2.999881,-9.229300,-3.756271,6.967297,9.473504,9.919859,-7.934239,-1.345567,8.138025,-7.025679,6.374960,2.862471,-9.406909,5.210233,2.771455,-1.259705,-6.707752,-9.635667,-5.183889,-4.795167,9.087080,0.544361,7.624434,8.975149,4.122506,6.063535,9.277136,9.366262,0.585975,1.482022,3.935666,9.599984,-9.011319,-3.438386,0.517935,1.977306,-0.776412,2.875130,-7.416164,3.152240,-8.929179,-7.615131,8.383678,7.619320,-9.764385,-9.400647,-7.651165,-7.945096,9.812102,-2.544230,0.588919,-7.127833,-1.025996,-8.075318,-0.542616,-0.838966,-2.632362,1.155525,-4.484505,-7.033855,4.505992,8.324819,0.315449,6.014618,-7.972803,8.937455,2.489979,-7.693460,4.531114,-7.052517,-3.729210,-0.894594,7.100275,-6.468023,8.089633,5.421925,7.286277,-2.419974,-4.488639,-5.208756,0.284108,-3.192676,4.828183,6.637473,1.798140,-1.367646,-3.506367,4.490765,-1.507644,-9.644374,-8.443976,4.362053,-7.898585,-2.298319,7.294992,0.678091,6.302625,7.665119,-0.840514,9.282995,-4.463424,3.329935,3.320520,-0.209439,0.144400,5.881321,-1.185874,7.750993,-1.609181,0.240224,-1.479342,7.603938,7.136225,-7.721858,5.873060,9.997255,-5.218563,-5.379278,9.012167,9.845860,0.467761,8.572507,6.534825,-5.572149,-0.913246,6.027343,4.057582,-5.208000,7.474369,-5.348177,9.219779,-0.840363,9.280534,1.392406,-1.817510,9.013781,0.441242,2.210649,5.396752,-3.886652,-1.497639,0.192034,-3.403734,-9.246062,-9.757495,-2.752209,-8.996736,5.818381,-9.476512,0.726938,-3.897570,-6.969798,9.724807,-5.150759,-1.250126,-3.397842,1.449903,-6.610939,-4.463037,0.545507,2.572571,-4.916812,3.717424,5.633833,-2.332652,-4.058301,8.075581,-9.521256,-5.543709,-0.916650,7.161750,7.857384,-4.406296,7.644125,-2.780497,0.893043,-6.376823,-5.748002,-1.382749,8.222462,-5.195528,1.506621,3.555498,-2.597352,-0.436059,-9.203496,2.143063,-0.059061,8.661493,-6.793584,5.791745,6.037487,9.169416,8.656330,-7.771535,-5.417235,-5.926201,-8.385171,8.635255,9.947870,9.895320,-8.755079,-0.349777,-7.874952,-5.906735,8.631109,9.135258,9.161319,-0.648213,-7.357100,-5.653344,6.975732,-0.150609,-9.713591,-4.553650,5.029942,9.731969,5.282928,4.030944,9.175745,-3.162264,7.431082,6.926659,3.714807,0.042356,-9.701978,-2.883806,-4.838333,-3.716450,9.944833,-6.156425,-0.536277,-3.189579,6.785052,-6.473983,8.895779,-3.639479,-0.811263,5.817330,3.001329,9.717889,-3.238481,-4.272868,-8.171572,4.064791,7.560507,-6.288869,8.069342,6.644457,-8.456504,4.281360,4.889381,-3.834332,-0.807868,7.543442,-2.176779,4.176614,-3.843255,3.218271,-7.489013,-2.610905,1.883982,-8.204331,4.442712,0.437623,0.813920,5.460291,-8.590017,-4.066399,-3.579065,0.671203,-1.618258,6.753490,-3.451646,7.714537,-5.390457,-3.703945,-9.310935,-6.051410,6.564023,-6.282899,4.595972,2.079624,7.339979,-6.729051,8.176609,0.244228,-9.316926,-5.925987,6.863285,-4.047553,-5.924125,9.221781,5.508730,-5.180614,-0.613655,2.556194,2.360611,9.063311,-8.402389,-5.167935,2.037395,7.802703,-2.751702,-7.440645,6.683670,7.037807,-7.022344,-8.508186,4.148061,-8.867120,5.953960,3.190602,-7.304478,-3.209206,-8.130698,-6.610432,-3.941778,8.248711,4.832136,-3.540579,-7.484018,-0.145209,5.235676,-5.940763,-4.618230,-3.512205,-5.630865,-0.226984,-3.956962,5.438376,9.685720,1.789651,8.219305,-4.292557,-4.933523,1.253155,7.726587,8.181982,5.015747,1.206361,-3.064700,3.276482,2.628446,1.785949,-0.300018,-1.851058,-7.615864,2.796530,-3.540540,0.409245,7.497185,-8.942381,-0.471177,5.704719,2.048175,8.117230,-7.711012,1.705192,-2.024374,6.429529,2.248406,-2.048547,4.701355,-3.008570,-7.430143,5.291646,-9.010863,-1.974664,3.347590,-8.344154,-9.879074,5.071774,1.128027,-5.341386,0.337653,-4.931439,8.472885,8.247649,3.786316,-3.522221,9.489719,2.657561,0.256798,-2.226094,1.912387,-1.761297,9.094274,-7.121108,-1.728061,-4.719759,-2.670775,-6.581738,-0.454544,2.079559,8.774448,6.870165,0.339195,6.701982,-4.619801,2.108836,-3.941682,3.152747,8.917484,-0.919508,-4.503771,-7.458112,-4.298646,-7.201468,-3.557422,-0.081424,8.804976,-2.091559,-9.611526,-5.335322,6.714282,-4.347924,5.154456,6.431817,6.518724,-4.304607,4.362114,-3.726205,2.987385,-8.723633,-5.802222,-1.735438,-4.912616,-1.239548,-4.555304,6.756528,5.706902,9.825619,7.360931,0.290122,3.530644,-1.213436,-4.518399,-0.055617,0.649765,9.308555,2.973964,9.199569,-5.257365,-2.498688,-1.667979,2.129528,0.818141,-1.020381,6.990962,9.692140,0.448735,1.910641,-7.567152,-5.804241,-3.704972,-8.945921,5.087282,1.173010,9.722526,-4.523322,7.134364,3.012411,-6.513778,9.436622,-5.837483,-4.616576,-2.804425,3.032713,3.498620,-9.007409,-0.983633,6.848461,9.988656,0.481916,-6.345296,-4.263976,0.353074,-2.890446,-6.817612,-0.635595,-8.707019,-5.377392,-7.360877,-9.686524,5.327681,-1.063169,0.284040,0.056080,-7.462716,6.078099,-2.733715,0.764169,-2.041253,-9.510154,0.444910,9.709810,6.262561,8.303253,9.533239,-2.171011,-3.272725,-2.735962,-2.601717,-2.926028,8.941837,-2.206756,-2.564264,2.841775,6.787320,1.113909,-6.024160,8.206060,-3.232761,-0.346959,-3.357572,9.258512,3.097055,-6.099129,7.875255,-2.099442,-0.478552,1.600835,-8.962756,4.246150,-9.072495,9.676805,0.678140,-8.126218,2.491466,-6.042014,4.614770,-2.127896,0.682507,1.858795,-1.534315,3.251442,-0.230371,8.265119,-1.825930,-2.595904,3.457505,4.074202,-8.440099,-5.852454,-3.273681,3.950963,-0.437259,-8.083465,-1.385991,5.872200,-3.777820,-7.141811,1.075204,0.985510,-5.646021,-1.180694,5.341314,5.797899,6.783448,1.537514,-3.394467,-4.006509,8.712600,-8.959126,-2.386539,-1.621113,0.068814,6.267011,-9.982335,-2.922341,-9.679386,-1.042106,-7.334502,-7.945076,3.623929,-8.545020,-3.354728,3.936587,8.295966,-8.085996,9.708967,-0.929814,2.432911,6.625838,4.330606,-6.709696,-9.915551,0.552154,-0.373146,-6.473311,-4.526366,4.077877,6.748679,-1.293260,2.094119,-8.050192,9.272030,8.658307,-1.445203,-5.880016,-7.932826,-6.583035,5.111295,6.067439,1.534092,1.881085,-8.500607,-2.270278,7.718045,6.994125,7.177248,5.961111,-4.638457,5.066817,1.503715,-1.777779,1.096973,-1.105583,4.524675,-9.039850,-6.640204,-2.904062,6.688236,-1.244028,2.835541,0.728234,-9.933835,6.818292,7.403023,6.273951,-8.742331,-8.650422,-0.564809,-2.426639,-4.355158,-3.492263,-7.514828,-0.031528,-4.084192,6.326296,-8.216969,-3.382307,5.612906,0.097684,2.469637,-6.806679,8.426071,4.279633,9.210722,3.776192,-1.741908,-4.703223,-7.039406,-7.548268,-2.095414,-8.237036,-2.471863,1.803618,-8.167304,-7.010813,1.562478,7.575358,3.666821,9.257155,-0.773780,8.817567,-1.758718,3.160262,-2.615243,0.488881,3.035629,0.610029,7.424166,-9.977601,6.992001,4.112453,0.309791,2.122447,1.626002,0.193660,7.103171,-9.821516,9.095956,-0.033659,-8.751006,-0.339788,2.807702,4.052382,-4.075486,-9.407873,9.871795,-9.118337,-6.313242,8.318013,-0.696172,3.906505,6.949247,-6.548275,-6.487347,-3.219959,-0.827700,-1.195572,-9.040845,-6.148832,2.296390,2.222495,-7.247720,9.920782,0.967534,-8.668977,-6.739783,-3.593934,-6.126711,-8.940984,3.725761,5.899071,9.130582,-7.922527,2.425165,-6.068799,3.618205,7.433955,4.764601,0.715276,-8.004418,0.865886,1.042775,-8.043051,-6.001018,-8.164888,-0.978804,3.326600,-2.811912,2.948490,5.940386,-6.507373,3.822950,-2.674966,8.972363,-4.812550,-2.891755,-2.629892,5.049605,4.556905,9.546714,2.550863,8.517744,1.435620,-4.456705,3.213040,-8.777332,4.720707,-1.711293,-9.781933,7.737554,6.736366,-8.390879,6.591134,-7.746710,2.612758,0.483077,4.557991,-9.476645,-0.947409,-5.240620,-2.503619,8.775798,-4.568969,7.607267,2.549539,1.975923,-5.058608,-4.892226,0.159987,-4.965857,-2.374146,-3.879286,-0.044430,-6.196728,9.136441,8.423512,9.885557,7.714222,-5.406487,8.850605,4.355917,-4.312078,-1.391369,-6.152483,9.271523,8.593286,-0.417856,-3.417807,-9.667027,8.288285,8.403288,0.788277,2.102252,-1.859859,2.759215,-0.382519,1.276037,1.736654,7.281452,8.292785,-3.106914,3.799317,-0.639975,-5.663583,-7.646276,9.717967,-4.072976,0.574416,2.403213,2.624826,6.152920,-3.151694,-0.553925,-2.550382,8.641541,-3.106553,-5.132595,-8.752665,9.034633,5.720534,-5.284335,3.985424,9.139033,-8.280681,1.720141,-0.137369,2.028629,7.627290,-1.458233,-7.857418,9.170695,8.958401,-2.984301,0.833912,-5.901477,9.876207,2.361055,2.518546,5.651293,1.955640,5.476050,6.997187,-1.474031,-6.504415,3.443340,-1.590468,-8.448405,-3.715754,4.924831,-3.157531,8.564416,-4.853573,3.087117,9.566009,-8.617777,8.933858,-4.779758,-4.431174,5.980769,6.978996,1.854027,2.187525,-0.593082,-3.989024,7.524886,7.745620,0.316242,1.051862,-0.976934,1.380047,-8.135921,-5.195204,-9.095563,1.347803,-0.951656,-6.745389,9.655679,5.082200,1.956874,1.204407,-3.084167,5.297762,4.949343,-6.797839,-9.344325,-3.212019,-9.946269,6.112118,1.956459,-6.875459,-8.973146,-3.250984,9.006009,8.460217,8.854889,8.129816,8.448194,7.865707,-8.531761,-6.801300,-8.745745,9.785634,-6.932636,7.291808,6.009947,9.926440,-8.837015,3.979954,3.927480,-3.508210,-2.814314,-6.828756,5.233033,-1.289191,-2.397953,-2.087150,1.919920,5.303841,-4.229377,7.833425,6.172341,4.141091,-7.130772,4.146623,3.701119,9.124354,2.248391,-4.120231,1.987654,-6.072389,4.887157,-6.481320,-7.247173,-8.671784,-0.545370,0.764221,-0.325120,3.180263,4.489103,-0.601751,5.862753,-3.669410,-1.068943,1.876305,5.099722,8.990442,-9.482319,9.584350,2.069876,9.203512,-2.426857,1.378880,-4.075111,9.854106,9.304465,-7.610267,4.006688,-2.123948,6.065640,-2.306837,5.601199,-0.432972,5.522487,0.585608,5.259558,8.161785,1.033853,8.140582,9.786432,7.626744,-8.716173,2.523113,3.571749,4.855624,5.696423,6.991211,7.951666,-2.790684,-3.634569,-7.742415,6.137565,1.240351,-8.080035,-4.772574,2.597462,6.538508,2.383947,-7.792633,-3.345653,-0.211836,6.316921,-2.532871,5.890862,5.175672,-7.122523,3.411767,5.362804,-5.794926,4.252400,-7.960231,5.682893,6.824990,-3.546916,9.492824,1.412416,3.440562,0.064042,-3.515727,-3.901191,-3.245318,9.200581,-4.043801,-6.209692,-1.722804,4.012073,3.889700,-0.177854,-1.883364,-3.692774,7.187076,5.953869,-0.373495,2.483262,6.924096,-4.056967,-5.405514,9.876037,6.783002,-9.204126,-9.808935,-0.383691,-2.306506,-8.369363,2.298065,-5.002341,-2.777686,4.131442,-8.026985,2.875633,0.141801,-2.610928,6.546275,-7.834644,3.793315,6.460701,1.013625,3.007236,-9.355679,-9.965941,-9.241837,7.465880,-6.873681,0.585090,7.681936,-2.016438,6.042617,-8.527370,-8.447377,1.188601,5.056296,1.081415,-0.850704,-5.295823,-4.420876,-0.190584,4.042473,-4.454992,5.111259,8.420430,-5.954804,4.330393,-6.802229,9.406371,-9.322532,-7.806739,4.424905,-3.756133,3.653375,-9.422377,9.692830,-5.920104,-3.446491,-9.203330,6.856575,-8.947406,4.985053,7.431966,-0.978906,4.648728,1.206292,-3.739095,9.885000,-2.410568,-3.110728,9.800504,7.530493,-5.684563,-6.578556,6.021516,-2.680079,5.405194,7.195478,7.450842,8.753310,1.214275,4.874093,2.508146,-9.850665,3.419524,1.141888,8.648629,-2.902089,-8.671187,-2.074626,-2.548598,-4.177836,6.648465,-0.311316,3.789890,0.803439,-1.481108,-9.626696,4.234548,8.144319,4.210814,7.033445,-6.677862,5.919068,-9.055232,-1.963089,-8.310554,0.267992,3.467372,0.972040,8.453486,7.355892,2.992519,-6.615496,-2.924785,6.734898,-7.339668,-7.821345,-2.502645,0.363430,-7.932223,-9.391606,-7.496445,-0.884382,8.196147,-4.291633,-7.061572,5.157324,-4.882648,-5.537355,8.690613,-1.951976,4.403452,-1.038809,-8.059356,-4.985237,-1.716655,-2.967626,-2.203024,-2.943410,-8.847620,0.737359,-5.446444,-5.646089,-2.067982,1.477027,-5.507029,6.311602,3.184893,3.548995,6.897360,-5.148530,-7.207744,3.928576,8.567129,5.242907,-4.094759,-7.896116,3.655235,1.518975,4.601982,7.482868,7.818719,1.557064,6.873828,-4.376028,2.350721,-7.450460,6.687142,-3.164830,8.586940,-3.855802,-9.367864,-0.797945,6.347198,5.615316,-2.946671,-5.580320,2.337494,-3.037715,6.348407,-7.541654,2.412192,-9.134197,-7.985932,6.062648,-9.664286,2.172821,-9.966394,-8.725415,-8.400815,0.268233,5.519636,-8.326809,6.874536,4.147611,2.977207,9.109142,-0.801841,-4.101308,8.602052,-1.183187,9.176999,-8.634388,1.657315,-7.755684,3.222197,-5.415721,3.581950,7.874195,-3.632955,6.388666,-8.955829,-3.879316,0.721837,5.492813,5.392350,-6.799894,-5.511767,-1.964737,-8.100425,4.908820,-5.571033,-9.274958,-0.804383,5.976140,-3.749496,-8.856741,9.150583,6.358591,0.681072,0.407338,-7.319036,-3.450355,3.966632,-5.389271,6.534968,4.190593,4.841786,1.600988,7.494736,-3.666924,-2.264478,4.269876,-1.282578,-6.916164,1.230516,-0.006596,1.684393,-8.992385,0.065721,-5.069384,-5.572134,0.850254,9.796247,6.768086,1.752271,-1.058363,3.886534,3.466387,-3.959657,4.971986,-0.326476,3.968165,-1.175157,-5.297667,-5.633873,-4.262259,-6.922529,2.377998,2.060652,-1.988646,-2.074088,-3.062687,-6.039547,6.048414,0.226890,2.855047,-8.879132,8.782282,-9.635987,2.515980,1.495121,-8.089767,0.304446,3.056189,-3.169165,6.939211,8.094653,-7.365721,5.149781,-7.010176,5.367221,-5.293869,8.666562,-4.067948,8.580394,-4.624982,-0.287527,-1.058767,-4.483468,-2.700015,-6.173168,-4.863129,3.112446,3.598592,-1.504410,1.557318,1.416541,-7.467346,2.339019,6.069752,-5.271714,9.304325,-2.831319,-1.392659,-8.731904,2.068223,-0.594020,-3.518850,5.059224,-2.381124,0.622663,8.926817,-0.443434,0.855959,-7.911940,-1.860162,6.302476,6.056231,-7.312721,-0.173374,-2.781205,6.982785,3.890381,-1.961883,0.902845,4.503221,-0.647459,-5.689914,-7.859704,0.563819,-1.077062,6.985705,6.183188,0.141167,-6.844044,-3.202599,7.957089,2.354830,0.385615,2.733969,-4.598094,-7.635409,3.862253,1.231098,-1.961934,2.208764,2.582426,-5.553248,3.852060,-7.942678,-2.919099,8.032871,-2.069518,-8.642557,-4.954875,-7.998155,-8.975339,-3.142198,7.990024,2.546936,-2.501358,-2.952640,3.478722,-0.886434,-6.017381,-6.445922,-0.657519,9.806322,-4.679719,-5.518952,0.821117,-1.895704,0.218412,-4.416562,-3.003531,4.479379,-2.773677,-6.003399,-9.585136,-3.747048,8.485690,3.835764,-1.031314,-1.053358,3.141593,-5.833682,-8.637318,-2.940777,2.014290,-1.645896,2.168654,-4.110161,-6.097973,8.742146,4.009263,3.810076,9.511390,-4.845981,1.911883,-8.121998,-4.950582,-8.248315,6.140807,-9.607014,5.846679,2.339414,-1.096342,-9.578673,-1.866042,-5.008253,9.108701,4.162288,-0.782154,2.795146,-0.537826,-4.156863,-5.125137,1.855702,-5.787070,-5.477807,4.567400,-3.907384], dtype = "float32")#candidate|3994|(7800,)|const|float32
call_3992 = relay.TupleGetItem(func_3503_call(relay.reshape(const_3993.astype('float64'), [660,]), relay.reshape(const_3994.astype('float32'), [780, 10]), ), 4)
call_3995 = relay.TupleGetItem(func_3506_call(relay.reshape(const_3993.astype('float64'), [660,]), relay.reshape(const_3994.astype('float32'), [780, 10]), ), 4)
func_1553_call = mod.get_global_var('func_1553')
func_1556_call = mutated_mod.get_global_var('func_1556')
var_3999 = relay.var("var_3999", dtype = "int32", shape = (847,))#candidate|3999|(847,)|var|int32
call_3998 = relay.TupleGetItem(func_1553_call(relay.reshape(var_3999.astype('int32'), [77, 11]), relay.reshape(var_3999.astype('float32'), [77, 11]), ), 7)
call_4000 = relay.TupleGetItem(func_1556_call(relay.reshape(var_3999.astype('int32'), [77, 11]), relay.reshape(var_3999.astype('float32'), [77, 11]), ), 7)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_4007 = relay.TupleGetItem(func_1426_call(relay.reshape(call_3998.astype('int32'), [847,])), 3)
call_4008 = relay.TupleGetItem(func_1428_call(relay.reshape(call_3998.astype('int32'), [847,])), 3)
output = relay.Tuple([call_3953,call_3984,var_3985,var_3986,call_3989,call_3992,const_3993,const_3994,call_3998,var_3999,call_4007,])
output2 = relay.Tuple([call_3954,call_3987,var_3985,var_3986,call_3990,call_3995,const_3993,const_3994,call_4000,var_3999,call_4008,])
func_4009 = relay.Function([var_3985,var_3986,var_3999,], output)
mod['func_4009'] = func_4009
mod = relay.transform.InferType()(mod)
mutated_mod['func_4009'] = func_4009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4009_call = mutated_mod.get_global_var('func_4009')
var_4011 = relay.var("var_4011", dtype = "float64", shape = (60,))#candidate|4011|(60,)|var|float64
var_4012 = relay.var("var_4012", dtype = "uint8", shape = (780,))#candidate|4012|(780,)|var|uint8
var_4013 = relay.var("var_4013", dtype = "int32", shape = (847,))#candidate|4013|(847,)|var|int32
call_4010 = func_4009_call(var_4011,var_4012,var_4013,)
output = call_4010
func_4014 = relay.Function([var_4011,var_4012,var_4013,], output)
mutated_mod['func_4014'] = func_4014
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4055 = relay.var("var_4055", dtype = "float32", shape = (10, 1, 3))#candidate|4055|(10, 1, 3)|var|float32
uop_4056 = relay.rsqrt(var_4055.astype('float32')) # shape=(10, 1, 3)
uop_4060 = relay.erf(var_4055.astype('float64')) # shape=(10, 1, 3)
output = relay.Tuple([uop_4056,uop_4060,])
output2 = relay.Tuple([uop_4056,uop_4060,])
func_4067 = relay.Function([var_4055,], output)
mod['func_4067'] = func_4067
mod = relay.transform.InferType()(mod)
mutated_mod['func_4067'] = func_4067
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4068 = relay.var("var_4068", dtype = "float32", shape = (10, 1, 3))#candidate|4068|(10, 1, 3)|var|float32
func_4067_call = mutated_mod.get_global_var('func_4067')
call_4069 = func_4067_call(var_4068)
output = call_4069
func_4070 = relay.Function([var_4068], output)
mutated_mod['func_4070'] = func_4070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2468_call = mod.get_global_var('func_2468')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_4109 = relay.TupleGetItem(func_2468_call(), 0)
call_4110 = relay.TupleGetItem(func_2469_call(), 0)
output = call_4109
output2 = call_4110
func_4118 = relay.Function([], output)
mod['func_4118'] = func_4118
mod = relay.transform.InferType()(mod)
mutated_mod['func_4118'] = func_4118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4118_call = mutated_mod.get_global_var('func_4118')
call_4119 = func_4118_call()
output = call_4119
func_4120 = relay.Function([], output)
mutated_mod['func_4120'] = func_4120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_4184 = relay.TupleGetItem(func_2881_call(), 0)
call_4185 = relay.TupleGetItem(func_2883_call(), 0)
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_4200 = relay.TupleGetItem(func_1822_call(), 3)
call_4201 = relay.TupleGetItem(func_1824_call(), 3)
func_2707_call = mod.get_global_var('func_2707')
func_2711_call = mutated_mod.get_global_var('func_2711')
var_4206 = relay.var("var_4206", dtype = "int8", shape = (1755,))#candidate|4206|(1755,)|var|int8
call_4205 = relay.TupleGetItem(func_2707_call(relay.reshape(var_4206.astype('int8'), [9, 15, 13]), relay.reshape(var_4206.astype('int8'), [9, 15, 13]), ), 2)
call_4207 = relay.TupleGetItem(func_2711_call(relay.reshape(var_4206.astype('int8'), [9, 15, 13]), relay.reshape(var_4206.astype('int8'), [9, 15, 13]), ), 2)
output = relay.Tuple([call_4184,call_4200,call_4205,var_4206,])
output2 = relay.Tuple([call_4185,call_4201,call_4207,var_4206,])
func_4214 = relay.Function([var_4206,], output)
mod['func_4214'] = func_4214
mod = relay.transform.InferType()(mod)
mutated_mod['func_4214'] = func_4214
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4215 = relay.var("var_4215", dtype = "int8", shape = (1755,))#candidate|4215|(1755,)|var|int8
func_4214_call = mutated_mod.get_global_var('func_4214')
call_4216 = func_4214_call(var_4215)
output = call_4216
func_4217 = relay.Function([var_4215], output)
mutated_mod['func_4217'] = func_4217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2468_call = mod.get_global_var('func_2468')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_4300 = relay.TupleGetItem(func_2468_call(), 0)
call_4301 = relay.TupleGetItem(func_2469_call(), 0)
func_3293_call = mod.get_global_var('func_3293')
func_3297_call = mutated_mod.get_global_var('func_3297')
const_4303 = relay.const([[-6,-6,9,10,3,4,5,-6,6,4,10,2,6,-5,-1,1,3,-4,1,2,10,-7,1,-1,-1,-10],[10,2,-3,-10,-3,-2,2,1,-9,-7,-10,-3,10,-9,-8,3,1,5,-4,10,8,4,-7,-3,-9,-7],[-5,-1,4,-5,10,-10,3,7,-10,5,-9,2,-5,6,5,4,-4,6,-6,8,-9,9,4,1,2,-6],[4,-9,-2,4,8,7,4,10,4,-8,-6,9,10,8,6,5,1,-1,-10,-10,5,-2,1,-1,-10,10],[-3,-8,8,8,-9,4,-8,-2,-9,9,-10,-3,3,-7,-2,-10,5,9,-5,5,-10,5,3,-8,-10,6],[-2,-2,-4,7,-6,-10,-7,2,8,6,-8,7,10,2,6,1,-9,-2,-2,9,-8,-8,-10,6,10,5],[5,-7,-1,5,9,5,9,-8,-8,8,6,2,-6,3,4,-4,-1,-2,-2,-2,-4,-6,6,-5,-1,-4],[-9,-4,-7,-3,-4,-10,7,-9,-10,9,-10,7,9,4,-5,8,5,8,-6,4,7,-6,7,-3,-8,1],[7,8,1,5,-10,-9,4,8,-8,1,8,2,-7,-2,-9,-5,-2,2,4,-1,-2,-1,8,8,6,5],[-9,9,2,-10,-6,-7,9,6,-9,-10,-5,-7,2,3,5,2,-5,-9,-6,-9,-6,-3,-8,-10,5,-5],[-3,-7,10,-3,-8,-10,-9,1,9,-8,-8,2,1,10,2,-6,10,9,5,-4,8,7,4,-3,-10,10],[1,4,3,-7,3,-9,-9,2,2,-7,1,-8,-4,10,1,3,-3,1,3,1,3,1,-10,-4,-1,3],[-4,9,-3,3,-10,-5,5,6,-5,-6,-9,-8,9,1,2,-2,-6,-8,1,-2,-8,-1,-2,3,-8,-6],[3,7,-6,2,2,-6,-6,-7,6,5,6,-8,-6,8,9,10,7,-6,6,1,-3,-8,3,-5,7,-4],[-7,-5,-7,-7,-6,2,6,6,-7,2,4,-8,-7,6,2,-9,6,4,-7,-10,9,6,-10,-1,-9,-9],[-3,10,2,4,-9,7,-4,-9,-1,4,2,9,-4,1,3,6,8,6,3,-8,-2,8,-3,7,-7,-7],[-4,-3,7,10,5,-6,4,-7,-5,-1,-7,2,-7,5,3,5,8,-4,3,5,-1,-4,-4,-4,-3,5],[-4,-9,10,-5,4,8,9,7,7,-1,-2,5,-6,-6,-2,7,9,-6,-10,2,2,-7,4,-2,-5,-3],[-10,6,7,-2,-4,4,-7,-4,1,4,-8,4,-7,6,3,-1,-8,-6,-9,-6,9,8,-2,6,8,9],[-3,7,1,-3,3,-7,1,5,-2,-2,-3,-1,-3,-8,-9,7,2,-1,7,9,-8,-8,10,8,6,-6],[-2,-2,4,-6,-1,-4,-6,7,-8,3,3,-4,7,-6,4,10,9,-1,-3,5,-1,-6,5,-2,2,-9],[-7,9,-5,-4,6,-2,-7,-9,1,4,-4,-1,-6,2,-8,-2,-3,8,-7,-4,-8,10,-1,-6,5,-4],[-2,10,8,7,-2,-1,-1,3,-1,1,-3,-3,-3,7,-10,-9,-8,2,2,1,8,10,-3,7,10,-3],[2,7,6,-3,5,-9,-2,8,-8,-9,5,6,-2,9,-3,-5,8,-8,4,-1,5,1,-10,-3,-1,7],[-2,1,-7,6,-3,-5,-2,7,4,6,-7,9,9,-6,-4,4,7,10,6,-4,-8,1,-1,8,6,9],[5,9,-7,4,-9,7,-6,1,-4,2,-5,-4,3,4,-9,1,10,-8,6,-10,2,2,-6,-1,-8,-4],[8,-9,-1,-10,-7,-4,10,4,6,2,3,8,-5,-10,4,3,-4,-4,-5,-7,5,9,-5,-5,9,3],[-9,1,-1,-6,7,-8,-4,-9,-9,1,-10,-3,-7,10,-6,-8,-3,1,-2,-1,-8,1,3,1,8,10],[-4,5,-1,-7,-5,2,-6,1,9,4,-3,9,6,-10,2,2,-2,7,-9,2,9,-1,-8,10,6,-7],[2,-5,-6,3,-4,1,-10,-3,3,5,1,7,-10,-1,5,-5,3,-5,4,4,3,-8,-6,-3,8,2],[-4,1,10,-10,1,3,-5,3,-6,-9,-6,1,-8,4,-2,5,7,-8,9,3,-3,-4,-5,-8,-5,2],[-2,5,7,5,-6,-3,-8,2,-1,9,-3,10,9,-9,-5,-8,-3,-8,-10,10,-5,1,-8,-5,9,-10],[-5,8,-10,-10,9,-3,-1,-5,-6,-9,1,-6,-2,-5,3,1,10,3,10,5,1,6,-9,-3,7,5],[1,-7,2,-3,-9,-6,6,9,5,7,-9,8,-3,2,2,-10,-9,-5,10,8,2,10,-5,6,-2,4],[4,-9,4,9,-9,10,-7,-8,2,-6,-4,-4,5,7,-1,-9,2,5,9,3,-4,-5,7,-6,3,-5],[10,4,-9,1,1,-6,7,-10,-7,8,3,2,9,8,2,1,-3,7,7,2,9,-2,1,-7,-4,-10],[8,-8,10,1,1,5,-10,-6,2,4,7,-8,-7,-7,-9,9,-10,4,-4,3,-10,9,-3,-4,2,6],[3,8,-10,2,-3,-5,-9,3,6,7,4,-4,1,-2,8,-10,4,3,-2,-1,6,-6,-7,-8,-4,-8],[3,7,-2,4,-7,-2,-4,-2,10,1,-1,2,-7,2,-7,10,-4,3,6,-9,4,3,-6,6,10,3],[8,3,8,-7,-8,5,5,-2,-5,-3,10,-1,-3,-2,6,-8,1,-10,-9,-3,7,8,6,-3,9,-4],[-4,-7,3,3,7,6,3,6,-4,-8,9,-2,-6,-7,-3,-7,-5,-5,6,-10,7,10,1,-3,-6,-7],[-9,-9,-4,-3,7,-1,6,3,-3,-4,6,-2,1,3,10,-2,6,7,8,-6,-2,7,2,10,10,6],[8,-4,-7,8,-6,-8,2,4,-5,-6,7,5,-3,5,-10,3,10,9,-4,-7,-9,-5,-10,2,-9,-4],[-2,-6,-5,10,3,-3,1,-4,-1,7,6,3,-3,1,3,-8,4,10,6,-5,3,6,2,-9,1,-4],[-8,-10,2,-2,-7,-10,6,-10,-1,-3,-3,-8,-1,1,-5,-8,4,3,-1,2,5,9,-3,-4,-2,-9],[-10,-1,6,-2,8,3,1,-7,8,10,-1,-5,-8,9,7,-8,-4,5,-2,10,-10,2,-8,-4,10,2],[-5,-6,-5,6,2,7,2,6,3,-1,-3,-4,4,9,-6,-5,-9,5,-5,-6,-2,5,-6,-7,10,-4],[3,-2,-8,8,4,-4,-4,9,-1,-10,-9,-8,-5,6,2,-6,7,-3,3,-10,7,-1,4,-4,-4,-9],[-7,-8,9,8,3,10,6,-7,-5,7,1,-2,-8,2,-9,5,-6,-10,8,-10,-6,2,-2,-10,-6,-8],[4,5,-6,-4,-8,3,-3,-2,-3,-3,-3,-10,4,1,-6,10,-6,-4,2,7,6,-7,-3,1,1,4],[8,8,-5,-3,-7,2,8,6,-3,-1,5,9,6,3,-3,3,10,-3,-10,5,-9,-3,-3,6,-3,5],[6,-5,6,-2,-4,10,6,-8,-10,-6,-2,-6,9,10,-1,-10,-9,-9,-5,-3,6,5,-7,-2,8,7],[-6,-2,7,7,-7,2,3,10,-2,7,8,-2,4,3,-2,9,-5,3,5,9,8,-9,-3,-9,3,5],[-9,-6,2,5,2,-2,-7,9,6,5,9,6,-4,-9,2,-8,-2,4,-4,8,2,-2,-6,2,-1,7],[-2,2,-8,3,-6,1,-7,-3,-3,-6,-10,6,1,7,5,-2,5,-3,8,4,-8,3,1,6,-5,-1],[-3,1,4,-8,10,-8,-7,-1,-8,8,-10,-3,8,-7,4,-10,-4,2,6,7,-3,4,-7,-4,10,2],[6,-2,-5,-7,-6,7,-7,8,-1,3,3,6,2,4,4,1,5,2,2,-8,-8,10,6,-1,4,-2],[1,6,8,5,-10,-1,2,5,-5,-6,-8,10,-4,-10,5,5,10,9,-1,-9,5,-6,-5,4,-3,-5],[-5,-6,6,-7,-10,4,6,-7,2,-10,7,-5,-4,-4,-9,8,2,5,10,8,6,9,9,-9,-3,7],[4,4,-3,4,7,-8,-6,8,4,-5,10,-2,-9,10,-1,-5,1,10,-10,-7,-6,8,7,7,2,4],[5,10,9,7,-9,3,-4,5,7,10,7,5,-4,7,-4,7,-9,3,-9,5,5,-7,1,4,3,1],[-2,8,-1,-1,8,-4,6,-2,-10,-2,-5,5,-2,3,-2,7,-3,9,2,8,-1,6,2,4,-4,-8],[-7,2,3,-5,10,-9,9,-6,2,-10,8,10,-3,-3,-3,6,7,9,5,-5,8,-9,-3,-7,-3,-8],[10,-3,4,-1,-9,7,7,4,-2,9,2,-8,-5,2,9,-8,-9,5,7,8,-1,9,-3,-9,1,-6],[6,-10,8,-8,3,9,9,3,7,9,6,-7,-3,5,-4,7,-4,2,10,-8,-8,-2,10,2,-7,-7],[-10,-4,-3,-7,2,9,-2,8,3,-2,5,-9,-9,2,3,-1,-6,-6,-7,-7,6,5,-9,9,-8,-4],[-6,10,5,3,3,-10,10,9,-10,6,-2,-5,1,4,4,-4,10,-6,-8,-2,-3,-2,-10,-2,-7,8],[7,-2,-7,10,2,-4,10,9,8,-10,6,6,3,8,-6,9,10,-4,6,10,9,-2,5,8,-5,-6],[2,-6,-2,5,1,-1,-5,-9,8,1,-5,-8,-6,-4,7,-1,4,4,-4,-5,-10,9,3,6,-9,-1],[-10,7,-5,9,2,1,-9,-3,-1,-9,9,6,-8,-3,9,-3,3,7,2,-10,-7,-2,3,9,-8,-4],[-10,6,5,7,5,7,2,4,1,10,-4,-4,2,10,6,6,6,-2,-3,-7,8,6,9,6,5,-7],[10,5,-7,-1,-7,-6,9,4,-8,-10,-6,-8,8,6,-2,2,4,-4,-2,-3,2,-2,9,4,-10,4],[5,-2,8,8,-10,-3,-8,9,-4,1,-2,-10,10,8,10,-7,-6,8,8,5,6,6,7,-6,-8,8],[9,-10,-1,10,-10,6,9,-1,10,6,-4,-10,6,1,-2,-3,-6,-9,-1,10,-9,7,-2,4,4,8],[10,8,-5,-1,9,-7,9,6,8,-9,-4,-4,7,-10,7,9,-7,5,-10,-10,-4,-8,6,1,9,10],[8,-10,1,-8,-8,-6,-5,-9,-9,6,8,6,-7,8,7,-9,-2,-4,1,-3,-8,-5,2,-10,5,-4],[-9,6,7,1,-4,3,-9,10,6,10,2,6,1,5,-3,10,-1,-7,-2,4,-9,1,1,-10,7,-10],[-5,-3,4,2,-8,9,-1,-8,5,9,9,3,-5,1,-1,9,9,2,-9,-1,7,6,6,-10,-8,-6],[3,8,-2,-8,-10,-1,-8,-4,-5,3,7,-9,3,-8,10,-9,5,9,-8,2,-3,-9,-4,-9,10,-3],[1,-9,-1,7,-1,4,-4,5,1,2,-10,6,-3,-5,7,9,-9,-4,7,4,8,6,-3,5,-8,-10],[7,-2,-1,5,-4,5,5,4,3,-4,7,4,-2,-6,6,-1,-1,3,-2,1,-3,9,-8,-3,-10,1],[-6,-9,-3,-1,10,2,-6,5,-5,4,-3,-9,-6,9,9,5,-4,-6,-9,6,2,3,6,8,2,-1],[-6,5,5,10,-3,-9,-9,-4,5,-10,-9,-7,-10,-8,6,9,-4,-4,8,10,10,10,8,10,5,2],[-2,3,-1,-4,2,9,-8,2,-8,9,6,7,-5,-9,6,6,-8,10,10,8,-7,-6,9,-1,4,3],[9,-4,-7,-5,-4,-9,-10,4,2,9,-9,4,-7,-7,5,1,-9,8,-1,9,6,10,8,3,7,1],[1,6,-2,-10,-2,-3,-7,-9,6,4,7,-7,1,8,3,4,7,-1,2,8,-2,6,-3,-10,4,-10],[-1,7,6,7,-5,3,-10,2,8,7,2,1,-8,-4,-6,-3,-3,6,6,-9,4,-4,8,8,8,6],[-9,-5,8,9,-6,-1,-5,-10,-8,-1,-3,-1,-10,9,-4,-8,-3,-2,-4,7,7,1,-2,-2,-10,-7],[7,7,6,-7,-2,5,-8,8,-10,-2,-2,-9,-3,-9,4,-7,-1,-10,2,-9,-2,10,3,-10,5,-10],[-4,-3,9,-10,-7,6,3,7,5,10,10,5,-9,8,8,3,6,7,-10,-10,7,-7,2,-6,9,4],[7,7,-6,-2,-3,-6,-2,6,-3,-9,2,9,-1,3,-2,-3,8,-2,3,1,-10,-4,-2,-4,-7,-3],[10,-3,8,3,2,-8,-4,-5,6,-2,2,9,-6,-7,8,10,-4,1,10,4,9,-2,-2,-1,-2,-5],[9,-8,-6,6,7,-4,-10,4,10,-3,10,4,-4,-2,-6,-1,-10,-9,-4,-10,2,1,-8,3,-3,-5],[-4,8,-3,-2,-7,5,-2,4,9,6,-6,5,-1,10,-7,-8,-5,6,-7,7,3,-1,-8,2,7,-9],[4,6,4,-1,2,-9,8,-5,6,-8,5,4,6,-1,4,5,5,5,-9,2,8,8,-9,-2,4,3],[-1,5,3,-10,7,6,7,3,10,7,7,5,-8,-10,-6,4,-10,-5,-4,-9,-10,-6,8,5,5,7],[7,9,-8,-8,3,-4,-2,5,5,8,1,-4,-3,9,3,1,10,5,-2,4,6,6,10,3,-7,1],[-5,9,4,-6,-5,-6,1,-3,-6,-8,-9,-10,8,-2,-4,-3,8,5,-9,10,1,9,9,5,-10,-8],[9,-8,1,4,-3,-2,-8,-4,1,-10,-3,-4,-10,-10,4,-1,-5,-2,9,2,2,2,3,8,3,6],[-7,-8,1,-9,-7,-2,7,9,-1,-7,-6,-4,6,-5,-9,5,-3,-3,3,3,-10,2,-8,-5,-5,1],[-1,2,-6,8,-10,-9,10,-1,-4,4,-7,5,-1,-6,3,6,4,-3,7,-6,-6,1,-9,-10,-7,8],[3,1,4,-8,7,-10,4,-9,-7,-9,2,-3,-2,-3,-9,5,4,6,5,4,-10,3,2,-6,-9,-3],[4,-1,1,7,4,-10,2,-8,-9,-9,9,-4,5,1,4,-4,-2,-7,8,-10,8,1,-7,-6,-1,5],[8,2,-9,9,7,-4,-8,-9,-6,9,1,5,8,2,8,-1,9,4,-6,-1,-6,-1,7,9,1,9],[-7,-9,6,6,1,4,5,-7,-9,-6,-5,-9,9,6,-5,1,9,-9,-3,1,-6,-3,-3,2,1,6],[4,-6,3,-2,-7,4,-5,1,10,4,-6,-5,-9,10,-4,6,2,-9,-6,-7,8,-6,-4,2,8,-10],[-3,5,3,-4,4,2,-3,-4,6,1,1,-6,6,-1,-4,-3,7,10,5,-4,5,-6,-1,-9,-10,-10],[10,7,5,-2,-8,-5,3,2,3,-5,-6,-9,1,-5,-8,5,-2,-6,10,-6,-1,1,8,9,3,-10],[-7,7,6,-3,6,4,10,-5,-8,-7,1,2,-5,-3,-7,7,-3,-5,6,-7,6,10,-3,-4,-5,-9],[-3,10,-2,-6,9,4,-10,2,5,-8,-3,6,-5,-7,3,9,-7,-4,3,7,-3,-3,-9,9,-6,-6],[-9,-7,3,5,1,2,4,-8,-3,-8,-5,-1,7,10,-9,6,-7,2,-8,5,-2,9,10,2,4,2],[-10,6,3,3,-10,-1,4,8,2,-3,-10,-10,-2,6,2,-5,-10,-2,-7,-6,5,-6,1,-1,9,7],[8,2,10,6,-5,-6,2,-8,4,5,-3,6,-7,9,1,-5,-3,-9,-4,-5,-3,-4,7,-3,-7,-10],[-9,4,-5,2,-9,7,6,3,8,-9,-8,-8,-4,-8,1,-1,6,8,10,-9,9,-9,1,-6,-1,-2],[5,-6,4,10,-3,6,8,-1,4,-7,8,-9,-9,8,8,-3,-3,-4,2,-2,6,-4,-2,5,7,-10],[-8,-5,-3,-1,6,-6,10,8,5,-8,-8,7,9,5,-4,2,3,8,-10,-9,-2,7,-6,-5,5,-3],[-6,-2,-2,1,-1,7,10,-1,6,-9,4,2,1,10,3,-6,6,3,6,-6,-9,-4,-10,-3,3,-5],[-10,-9,-4,-4,4,5,-9,-10,6,-5,-8,-8,-1,7,3,-3,10,-3,-10,-1,-8,-4,9,-3,9,10],[4,-8,-8,-1,8,5,7,-2,2,3,2,-6,-1,-5,-8,10,4,-9,4,5,-5,9,6,-10,5,-10],[-1,9,9,2,3,-9,1,-1,-7,8,7,-7,9,5,1,2,-6,-3,6,-10,9,-6,-7,-7,3,8],[3,5,3,5,-7,-5,9,-6,3,-4,5,-3,8,5,-5,3,10,-1,8,-6,-4,-8,7,8,9,-2],[-3,-5,5,4,4,-2,-5,-7,9,-10,2,-6,9,9,-7,2,-4,-2,-6,-2,4,-7,5,6,7,6],[3,8,-3,1,8,9,8,-2,10,7,8,-4,7,-6,5,4,4,-1,-1,-7,4,10,9,-8,-7,-2],[-8,9,-8,2,7,-3,-7,7,7,-6,4,-4,-1,-4,5,5,-4,-1,-9,8,-8,-8,7,5,-3,-4],[-9,10,1,10,9,1,10,-8,4,7,-8,9,2,1,6,-10,6,-7,-3,-2,10,6,7,9,1,-5],[10,-6,7,8,5,-8,-8,-5,-2,5,-2,2,-6,-1,6,8,10,-8,3,10,-4,6,-3,-6,2,7],[-10,-3,9,-3,-10,10,-5,6,-6,6,7,3,5,-5,9,-10,10,-7,-9,-3,-3,10,-1,8,5,9],[-5,1,2,-8,-7,-3,-4,-3,3,2,9,6,8,-9,-5,4,1,-2,9,-7,10,3,-10,-5,-4,-9],[-6,-5,8,-9,4,-2,7,1,6,2,8,10,-4,1,1,-1,6,3,-3,6,6,-4,4,8,-5,-7],[-8,9,1,9,3,-9,7,-2,4,8,5,-10,-9,-2,3,-5,6,4,-7,7,5,6,8,2,5,-2],[2,-3,4,-5,-5,-9,-8,6,10,-3,1,-6,-7,-3,-8,5,6,-3,3,7,-2,-7,-3,-4,-8,7],[8,10,-10,10,-5,8,-4,4,-10,-5,9,-3,-9,-5,-5,8,-6,9,-1,-3,-7,-10,3,8,6,8],[-9,10,-7,3,-7,-3,9,-8,4,-7,-4,10,10,3,-5,-3,-1,10,-8,-7,-6,-10,6,-5,1,9],[-8,5,9,6,-10,-6,-2,8,-1,-6,7,10,-4,-6,-7,-8,-4,-5,-2,8,-9,-2,3,10,-5,1],[-10,7,-5,7,-8,7,10,8,2,-4,2,-10,6,-9,6,-4,10,-8,-4,9,2,5,-7,-5,-9,-9],[-5,-8,-1,-1,-6,3,6,-2,-8,6,6,-3,-6,-3,-7,8,3,4,-2,3,10,3,-9,8,-4,9],[-6,3,3,7,-10,4,10,1,5,-9,10,-10,-6,6,3,-2,-10,-10,-2,-4,3,-8,-8,-6,-3,-5],[-6,-1,3,6,5,-2,-4,-7,-1,-1,-9,-7,7,7,8,-4,8,1,-5,5,3,-6,-2,-3,3,7],[-2,8,-10,1,8,-4,-1,8,-2,-7,-2,3,-5,9,10,-10,4,2,-3,-4,8,-9,-5,-8,-10,3],[7,10,-2,-10,6,-5,-7,6,1,3,10,-10,-7,-3,3,-10,9,4,8,-4,-3,-7,-7,10,-3,-7],[5,9,8,-10,5,1,10,5,-9,-4,-7,3,-4,-2,-8,-9,8,6,9,7,7,-7,-3,-5,-3,-5],[10,6,2,10,-9,-4,8,-3,7,-10,-7,-1,1,-5,5,-7,-9,-8,1,3,-8,6,-1,2,8,2],[8,8,-9,6,-2,-10,7,1,7,-7,5,2,4,-3,7,10,9,7,-10,2,7,2,-2,-2,-9,6],[4,-7,4,-3,-5,8,-10,10,7,1,-5,-8,5,6,2,-7,1,-7,4,-8,2,1,-1,3,6,-4],[6,-8,3,-7,9,1,8,7,-7,-10,-10,-2,-3,-9,-8,10,4,-7,5,1,-7,-3,10,6,-4,-8],[-9,-3,3,3,-4,5,4,-4,5,-10,8,9,3,5,4,-10,-2,-9,-7,-8,9,1,-7,-2,-2,9],[6,-8,-3,-6,6,2,-1,7,-5,-2,-10,8,10,4,-2,2,8,9,-2,-8,3,8,-3,3,-10,2],[8,9,-10,9,-3,2,-8,-5,-5,9,-5,1,10,5,9,-9,-9,-4,-9,-3,-4,8,-7,10,-5,2],[-6,7,-9,5,4,-6,10,4,-4,6,3,10,4,-3,-1,-1,10,-10,-2,6,8,-1,-5,-8,5,7],[-7,-9,8,-1,9,-3,-10,5,-7,10,-6,-4,9,9,7,1,4,-4,-3,9,-5,-8,-7,-8,5,-2]], dtype = "uint8")#candidate|4303|(150, 26)|const|uint8
call_4302 = relay.TupleGetItem(func_3293_call(relay.reshape(const_4303.astype('uint8'), [3900,]), relay.reshape(const_4303.astype('bool'), [780, 5]), ), 2)
call_4304 = relay.TupleGetItem(func_3297_call(relay.reshape(const_4303.astype('uint8'), [3900,]), relay.reshape(const_4303.astype('bool'), [780, 5]), ), 2)
bop_4309 = relay.floor_divide(const_4303.astype('float64'), relay.reshape(call_4302.astype('float64'), relay.shape_of(const_4303))) # shape=(150, 26)
bop_4312 = relay.floor_divide(const_4303.astype('float64'), relay.reshape(call_4304.astype('float64'), relay.shape_of(const_4303))) # shape=(150, 26)
uop_4316 = relay.atan(bop_4309.astype('float64')) # shape=(150, 26)
uop_4318 = relay.atan(bop_4312.astype('float64')) # shape=(150, 26)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
var_4328 = relay.var("var_4328", dtype = "int32", shape = (847,))#candidate|4328|(847,)|var|int32
call_4327 = relay.TupleGetItem(func_1426_call(relay.reshape(var_4328.astype('int32'), [847,])), 1)
call_4329 = relay.TupleGetItem(func_1428_call(relay.reshape(var_4328.astype('int32'), [847,])), 1)
bop_4344 = relay.add(uop_4316.astype('int8'), relay.reshape(bop_4309.astype('int8'), relay.shape_of(uop_4316))) # shape=(150, 26)
bop_4347 = relay.add(uop_4318.astype('int8'), relay.reshape(bop_4312.astype('int8'), relay.shape_of(uop_4318))) # shape=(150, 26)
func_3681_call = mod.get_global_var('func_3681')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_4354 = relay.TupleGetItem(func_3681_call(), 0)
call_4355 = relay.TupleGetItem(func_3682_call(), 0)
output = relay.Tuple([call_4300,call_4327,var_4328,bop_4344,call_4354,])
output2 = relay.Tuple([call_4301,call_4329,var_4328,bop_4347,call_4355,])
func_4356 = relay.Function([var_4328,], output)
mod['func_4356'] = func_4356
mod = relay.transform.InferType()(mod)
var_4357 = relay.var("var_4357", dtype = "int32", shape = (847,))#candidate|4357|(847,)|var|int32
output = func_4356(var_4357)
func_4358 = relay.Function([var_4357], output)
mutated_mod['func_4358'] = func_4358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2263_call = mod.get_global_var('func_2263')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_4380 = func_2263_call()
call_4381 = func_2263_call()
func_3884_call = mod.get_global_var('func_3884')
func_3886_call = mutated_mod.get_global_var('func_3886')
call_4382 = func_3884_call()
call_4383 = func_3884_call()
output = relay.Tuple([call_4380,call_4382,])
output2 = relay.Tuple([call_4381,call_4383,])
func_4386 = relay.Function([], output)
mod['func_4386'] = func_4386
mod = relay.transform.InferType()(mod)
mutated_mod['func_4386'] = func_4386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mutated_mod.get_global_var('func_4386')
call_4387 = func_4386_call()
output = call_4387
func_4388 = relay.Function([], output)
mutated_mod['func_4388'] = func_4388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2511_call = mod.get_global_var('func_2511')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_4414 = func_2511_call()
call_4415 = func_2511_call()
func_3293_call = mod.get_global_var('func_3293')
func_3297_call = mutated_mod.get_global_var('func_3297')
var_4418 = relay.var("var_4418", dtype = "uint8", shape = (1950, 2))#candidate|4418|(1950, 2)|var|uint8
call_4417 = relay.TupleGetItem(func_3293_call(relay.reshape(var_4418.astype('uint8'), [3900,]), relay.reshape(var_4418.astype('bool'), [780, 5]), ), 1)
call_4419 = relay.TupleGetItem(func_3297_call(relay.reshape(var_4418.astype('uint8'), [3900,]), relay.reshape(var_4418.astype('bool'), [780, 5]), ), 1)
uop_4424 = relay.erf(var_4418.astype('float64')) # shape=(1950, 2)
output = relay.Tuple([call_4414,call_4417,uop_4424,])
output2 = relay.Tuple([call_4415,call_4419,uop_4424,])
func_4428 = relay.Function([var_4418,], output)
mod['func_4428'] = func_4428
mod = relay.transform.InferType()(mod)
var_4429 = relay.var("var_4429", dtype = "uint8", shape = (1950, 2))#candidate|4429|(1950, 2)|var|uint8
output = func_4428(var_4429)
func_4430 = relay.Function([var_4429], output)
mutated_mod['func_4430'] = func_4430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2263_call = mod.get_global_var('func_2263')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_4435 = func_2263_call()
call_4436 = func_2263_call()
output = call_4435
output2 = call_4436
func_4462 = relay.Function([], output)
mod['func_4462'] = func_4462
mod = relay.transform.InferType()(mod)
mutated_mod['func_4462'] = func_4462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4462_call = mutated_mod.get_global_var('func_4462')
call_4463 = func_4462_call()
output = call_4463
func_4464 = relay.Function([], output)
mutated_mod['func_4464'] = func_4464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3681_call = mod.get_global_var('func_3681')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_4604 = relay.TupleGetItem(func_3681_call(), 0)
call_4605 = relay.TupleGetItem(func_3682_call(), 0)
func_1222_call = mod.get_global_var('func_1222')
func_1225_call = mutated_mod.get_global_var('func_1225')
const_4613 = relay.const([[8,3,-1,-9,9,9,10,-1,-4,-1,-10,-7,4,-9,-9,9,6,1,10,2,-5,1,4,-8,-4,1,1,-7,1,1,4,7,-2,9,-10,3,4,1,-6,6,-9,4,-6,-6,-6,7,7,-3,-6,-2,5,-2,-1,-7,-1,7,-4,1,-1,-7,3,10,-9,2,-7,-2,2,-1,6,-8,-5,-8,-7,8,-7,8,8,2,2,1,-8,2,-6,3,-3,10,7,6,8,-3,-9,-4,10,2,-10,1,-7,-10,-6,-6,3,10,5,-5,9,7,10,5,-7,-3,-2,-7,-7,-4,7,5,-8,-1,10,6,-5,-9,2,8,-3,-8,-5,-5,-9,5,-9,-9,5,7,-7,7,6,8,10,-7,7,9,10,4,3,7,-10,-8,-6,2,-10,7,5,-3,-3,9,6,2,1,7,-3,-5,-3,-2,8,4,3,3,7,4,-6,10,2,-10,-5,-9,1,5,-7,-3,-1,2,-8,-3,-10,-5,-1,-8,6,-7,3,9,-10,-8,-1,1,-9,7,7,-2,-6,-1,3,-9,-7,8,-2,4,1,-6,-2,-6,9,8,-3,3,9,-6,3,-9,-2,10,4,-6,7,-1,9,10,1,6,-10,1,2,10,-3,-8,6,10,4,-6,8,-10,5,6,7,9,-8,-5,-8,-8,5,-7,-3,-10,-1,-6,6,-7,-5,6,-5,-1,5,-5,-2,5,8,6,-7,8,7,-8,-9,5,-7,8,-5,-7,5,-7,-7,-4,-4,-6,-9,10,8,8,-2,3,-3,3,8,-2,6,-9,2,9,4,-7,-2,8,5,-9,-10,-6,1,-4,-1,-1,-6,9,-4,3,4,10,7,7,-5,-6,-7,1,-6,-1,1,-6,-2,6,3,-3,-9,4,10,-7,8,-3,8,6,-7,10,9,-9,-1,9,4,5,-5,-1,-2,2,-2,4,-7,3,-5,3,9,5,7,-5,5,8,9,-5,-8,1,-1,9,7,-3,-4,-8,-10,-2,8,2,7,3,9,-9,6,8,-6,7,-8,-6,1,-7,7,-10,7,8,1,-2,-1,9,10,7,4,-9,-8,-7,1,2,5,4,-3,8,6,-6,10,6,-1,-5,-9,-7,3,6,10,-1,7,7,-8,5,4,10,-5,3,9,10,6,3,-1,-1,-4,-6,-10,4,-9,-1,-10,-8,-5,-2,-8,-2,-2,-4,-3,-4,9,-1,-6,-6,-4,9,-6,-1,-5,-7,7,-9,-4,2,8,-6,9,-6,2,9,9,-10,-2,-9,-5,-1,-6,3,-3,-1,2,-10,7,-5,9,3,-9,-4,5,9,-10,2,1,7,-10,-7,-6,-3,-6,-1,2,5,-6,-4,4,1,-2,-1,-8,-8,-7,-3,3,-7,4,-4,-2,8,9,9,3,-7,-4,-9,5,3,4,6,-1,6,10,4,10,10,-3,-1,10,3,-4,-8,-2,4,6,3,2,-5,-9,4,10,-9,4,1,-7,10,9,-2,-7,-6,6,-4,-9,3,-9,-9,5,-4,-7,-5,-1,8,2,-10,-8,-6,6,-5,9,4,8,-7,-3,-2,-5,-5,-3,-6,-4,-8,5,-7,1,7,-1,-8,-6,2,3,10,-4,-4,-9,-3,-7,5,4,2,-5,5,-1,5,-5,7,-2,8,3,4,-2,-2,10,10,1,-7,-2,2,-5,-3,5,-10,8,-4,2,10,7,-3,-1,-10,7,-9,-2,-2,-8,-7,6,10,7,-4,4,-3,8,-9,-10,-3,6,8,3,-5,7,-3,-1,-7,-9,-7,5,-5,7,5,-2,-6,2,-8,-6,-5,-5,5,1,4,3,4,-3,-2,-4,-10,9,7,-10,6,8,-8,-10,-8,-5,5,-6,-5,-10,1,-5,-2,-5,-6,4,2,5,-4,2,-10,-8,2,-5,-5,5,-1,-5,7,-2,6,6,9,-7,-8,6,-6,2,10,-7,2,-3,4,-8,9,-7,5,4,-7,-8,9,-5,-10,-5,4,-7,5,1,-7,2,8,-10,3,8,6,6,-10,2,-6,2,8,10,7,-3,-2,-10,-4,-5,6,-8,-1,-10,3,-1,-9,-3,-2,10,-4,-6,8,7,8,-1,-7,-9,-3,-9,10,-9,5,-6,5,-8,9,-7,2,8,-8,-6,-10,-3,-5,3,-2,-4,4,-4,8,-8,-6,1,-1,-7,2,1,-10,6,7,-3,-2,6,1,-5,-3,-3,9,4,4,6,7,-7,2,-4,-3,-9,-6,-8,-6,3,5,-8,-1,-2,-4,-1,8,9,1,8,-2,8]], dtype = "int32")#candidate|4613|(1, 847)|const|int32
call_4612 = relay.TupleGetItem(func_1222_call(relay.reshape(const_4613.astype('int32'), [847,])), 1)
call_4614 = relay.TupleGetItem(func_1225_call(relay.reshape(const_4613.astype('int32'), [847,])), 1)
var_4624 = relay.var("var_4624", dtype = "int32", shape = (2, 847))#candidate|4624|(2, 847)|var|int32
bop_4625 = relay.less(const_4613.astype('bool'), var_4624.astype('bool')) # shape=(2, 847)
uop_4628 = relay.erf(var_4624.astype('float32')) # shape=(2, 847)
func_2263_call = mod.get_global_var('func_2263')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_4631 = func_2263_call()
call_4632 = func_2263_call()
bop_4646 = relay.greater_equal(uop_4628.astype('bool'), relay.reshape(bop_4625.astype('bool'), relay.shape_of(uop_4628))) # shape=(2, 847)
uop_4649 = relay.cos(uop_4628.astype('float32')) # shape=(2, 847)
func_3293_call = mod.get_global_var('func_3293')
func_3297_call = mutated_mod.get_global_var('func_3297')
const_4654 = relay.const([-2,-8,3,7,5,-4,-4,-3,-2,10,-1,1,6,-7,-4,10,3,2,-7,-7,-9,-3,3,-7,10,-4,8,2,5,-4,4,-6,1,-2,9,1,2,10,-1,2,-4,4,-4,-5,-6,9,-10,8,4,-2,-1,8,8,-1,-7,-10,-1,-3,1,-3,9,-8,8,-2,7,-5,6,4,-3,3,-9,-1,7,7,-5,6,4,-3,-1,-5,1,-1,-3,-3,1,6,-10,2,10,7,10,9,7,-6,-1,9,1,10,-4,-10,-8,-8,-3,8,-10,1,6,5,4,-2,-4,-6,2,1,-7,-2,7,-5,-10,4,-6,1,-4,5,-10,2,1,-1,2,-8,2,5,-10,10,3,-2,-8,3,1,-10,9,7,10,3,-7,-2,-1,-8,9,-10,1,-5,5,3,-8,-7,6,8,-1,9,-10,-8,-10,-1,-6,5,-5,6,-8,7,1,6,-9,3,-3,-1,3,-5,8,4,-1,9,9,9,4,5,2,-3,4,-5,6,4,-5,-2,7,7,5,3,3,1,-7,-3,8,4,-9,2,4,7,-5,4,-5,7,9,3,-1,1,3,-9,-9,-4,3,-6,-10,-10,-1,6,-7,7,-2,-10,-7,2,-5,10,5,4,9,-7,-2,5,-1,-1,-3,-6,1,9,7,9,-4,5,4,-9,1,6,-5,9,2,-6,-10,-2,-8,-10,-2,-4,9,-6,-3,8,3,7,4,5,8,3,-6,9,-5,7,-10,-2,4,-4,4,-9,5,-6,4,7,5,-9,4,-4,-9,-6,4,7,-7,5,2,-8,-1,-8,-8,-8,6,7,-9,8,-4,6,2,7,4,-1,-7,-5,-7,-5,9,-1,5,2,-7,-2,5,-8,-1,6,-7,2,-8,-2,2,-2,-5,4,9,3,-8,-8,1,10,10,-9,-5,-3,-10,9,-6,-10,2,-10,2,8,8,-5,-1,-3,2,-10,-3,-1,-9,4,3,-6,-10,7,-2,3,8,-1,4,-2,7,5,-6,-2,9,2,-10,7,9,-3,7,-2,-6,6,8,6,1,-5,8,-5,5,-8,-8,-6,-7,7,-5,-10,2,10,-5,5,-10,4,10,-6,9,-2,7,3,5,9,-6,2,7,8,-8,8,3,-7,-3,10,5,8,-9,9,10,-5,-8,-4,9,-7,-7,7,10,5,-5,7,6,-5,6,-9,3,-3,-1,6,-3,8,-1,-9,7,4,8,5,9,-1,5,3,5,6,5,7,6,-7,8,-8,10,10,-5,4,-6,-1,4,-6,-10,-7,8,-2,-7,3,-4,2,-5,2,7,6,-10,2,-10,2,-5,-6,3,7,-8,-5,1,8,8,-8,5,-8,-2,10,-3,4,3,10,10,6,-8,-2,-8,7,-10,3,-8,2,-3,1,-5,3,7,-4,1,-6,-10,-1,9,-4,-2,6,-8,-1,-1,9,9,5,-5,2,-2,-8,9,1,-9,8,-4,3,-5,6,-7,3,7,10,1,-2,2,-5,1,-10,-3,-2,-5,2,9,7,3,4,9,3,-7,3,7,2,-4,-8,1,7,-7,7,6,-6,3,8,3,2,-8,-1,2,5,-4,-6,-5,2,-1,9,-10,-4,-2,-4,6,5,2,-1,9,-2,-8,-7,-1,-4,7,-8,6,-1,6,5,1,6,-8,-8,2,10,-8,3,-8,-10,8,-4,-1,7,2,7,-4,9,-1,-8,8,-3,5,-6,2,-7,-5,9,8,3,-7,-5,5,-4,-10,-1,10,-5,-9,7,-8,-4,-7,-10,6,-7,4,-8,4,9,-4,-2,-4,9,-7,-7,-1,7,1,-5,1,-3,-1,-7,-3,-1,-7,-3,-10,-4,-9,10,-1,7,8,-8,3,-7,-2,-1,1,6,-5,-8,-1,1,-5,-1,-2,8,-10,9,10,10,-10,-9,-3,10,-5,-4,-3,8,8,6,-8,7,1,-3,-4,4,-4,-7,-9,-8,5,1,-6,8,10,3,-8,-8,-10,1,4,8,-10,6,9,-4,-3,-4,7,7,6,5,-2,-3,6,6,9,9,-6,9,-6,-2,1,1,8,3,-8,5,5,-4,-2,-2,-4,-10,-5,-8,3,1,-7,-2,-10,6,7,-2,9,-3,6,-4,6,3,-5,2,2,-4,6,2,2,6,1,-2,-3,3,-10,-10,-1,8,3,-3,-1,-3,-4,-5,-5,8,8,-8,6,-8,8,-5,-8,-6,2,5,-8,-10,-7,1,-5,-10,10,4,9,4,-10,10,-3,9,8,9,-6,10,-6,-5,-1,-4,3,9,-9,-1,6,-7,10,2,-1,5,2,3,10,8,3,4,-1,-9,-10,7,6,2,-9,-3,7,-2,-7,6,-2,-9,-8,2,8,10,-6,1,-1,7,9,-4,1,-5,8,-4,-8,5,7,-5,-3,-4,-2,-10,-10,-6,-8,-5,-6,-5,-4,7,5,-9,-1,9,1,-2,8,7,8,5,4,5,2,6,-1,9,-7,10,5,2,1,-9,6,7,9,-2,-3,5,-8,-5,-6,-7,-5,10,4,-7,6,8,-4,-5,-6,-8,-3,8,5,-10,-8,-3,4,4,-5,-7,-7,-2,9,-3,-4,5,3,-1,-7,-1,-8,9,-6,-1,1,2,2,-6,1,5,-10,5,6,-4,-6,9,9,-7,-8,-6,8,-9,-1,-1,-4,-8,-1,-10,8,1,10,10,-7,-6,7,7,1,-8,-9,-3,-9,1,-3,-6,-6,-2,6,-10,1,9,-10,-7,-10,-1,6,-6,-4,-5,-8,5,8,4,3,7,10,4,-2,-10,6,3,-7,6,-8,8,2,1,5,3,1,-10,6,2,-6,2,6,-3,6,4,-4,9,-8,-5,-8,-10,6,10,5,2,4,3,-1,3,-10,3,-1,-8,-5,-3,1,9,-5,-1,-1,-4,-9,5,3,-1,-6,7,-1,8,7,-8,-9,8,-8,-6,4,-5,5,4,9,3,2,-3,-4,-8,6,-1,-6,9,-8,4,3,6,1,-7,7,-4,-1,-3,-1,8,-10,-2,-10,10,-6,-1,-6,-8,-6,7,-7,4,9,-3,-2,-10,1,-9,-3,-10,-5,-7,-7,10,-9,9,-8,-4,-4,-7,-9,9,9,1,-6,2,-4,-4,3,6,-9,-10,2,3,-2,-2,-9,10,-10,-1,-4,10,1,8,-10,-8,9,-7,1,-7,-2,3,-2,1,-4,8,5,-5,-4,10,7,-2,-5,9,8,-8,-9,-4,-4,4,-9,-7,2,1,-6,1,-9,2,-1,10,1,4,3,-10,4,6,-8,-8,-6,8,9,7,-2,4,2,-7,-3,10,10,4,5,7,-2,6,3,-2,-3,2,8,3,1,-10,2,2,-1,3,-6,-9,-7,-8,9,7,-9,-9,7,6,1,-2,-7,2,1,-3,-10,-7,7,9,7,10,-5,4,1,9,7,5,-8,-9,-6,7,-5,3,10,-10,8,-3,-6,-6,-9,9,8,10,-2,-8,3,4,-10,10,1,-8,-7,-3,-10,-2,-3,4,6,1,5,8,-7,-6,1,8,5,10,-7,-6,1,-7,-10,10,-7,6,10,-9,-8,3,-10,-3,7,8,-8,10,-4,-6,9,8,6,-7,-8,3,-3,7,-9,8,-4,9,-3,-1,-7,-1,10,-2,3,-3,8,-9,6,2,-4,1,-1,2,-1,-10,2,5,-1,10,-4,7,1,-3,-1,2,7,7,-4,-1,4,1,3,7,3,-9,10,-1,3,-10,8,2,-3,-3,-10,2,-8,-1,1,4,-7,2,-9,10,4,-8,2,-8,-1,-4,7,-6,-8,-5,-4,4,-2,-9,-7,4,-9,-6,2,-7,-6,3,-4,-10,3,3,6,9,2,-10,-8,-2,7,-7,-3,10,-3,5,-2,-2,-4,-6,-4,10,-2,-7,-5,7,-9,8,1,3,3,-5,-5,-3,4,9,2,-4,-8,-7,3,6,2,-6,-4,-9,5,3,1,-8,3,10,5,-4,-8,9,-6,-3,-8,1,6,-8,-2,-2,7,5,-9,7,-3,-10,-1,10,1,6,-2,1,5,-10,10,-9,4,-7,2,-9,-7,4,6,-7,-1,8,10,-1,1,-3,5,-10,-9,-2,-2,-4,9,-9,5,-6,9,-10,-5,7,2,9,-3,6,7,-2,10,8,-7,-6,2,-9,-8,-3,9,1,9,1,-8,-5,7,-3,-5,-8,-9,5,8,4,2,-9,9,-4,-1,-2,4,-3,7,9,1,4,-4,1,2,8,-5,7,-8,-2,-8,7,6,-4,-7,6,-2,8,-9,10,6,-5,4,5,-3,-10,-5,-4,8,-5,2,-3,-10,-2,9,10,9,-8,-5,6,2,-10,4,10,-3,7,6,4,2,-7,-10,-8,-2,2,9,-7,6,2,5,-2,-6,-6,10,10,-7,-2,-6,6,5,5,-7,-7,-4,-3,-10,7,-5,-10,-4,4,1,-8,6,-3,1,-7,2,1,4,5,10,-1,7,-9,-6,-2,-1,-2,-4,10,-4,-4,-2,6,-3,-9,3,10,-1,-10,-4,-2,5,-3,-10,6,9,-4,-7,6,-1,2,5,3,3,-3,-8,-1,10,1,7,5,9,9,-10,-7,2,-5,3,2,-3,-10,-9,-3,-7,8,4,-1,3,-1,7,-5,7,-7,-10,-6,-2,-4,-9,10,3,-7,-9,2,-10,-6,2,7,1,-2,1,-4,4,5,-6,7,-3,8,5,-6,6,-4,-3,-8,5,5,-7,10,-6,-5,2,-2,8,-6,2,10,2,-6,4,-9,-3,-4,1,2,-1,-10,8,-5,-3,-1,-3,-3,-2,-9,-3,5,3,8,3,1,-8,-6,-4,5,4,-2,-7,-9,6,-5,-8,-4,-10,-5,4,-7,-9,-1,6,10,-1,4,-1,-7,2,-5,2,1,4,5,2,-10,-4,3,6,9,-10,-3,7,8,-2,2,-2,6,-9,-4,2,1,5,-6,-9,-8,10,-2,1,-6,2,-9,-1,10,5,-2,-8,-4,8,5,7,-8,5,3,9,1,9,6,6,-1,-2,9,-5,4,-5,3,-10,-10,-1,3,4,3,-5,-3,-5,-3,9,-6,8,-10,-8,-8,3,3,3,-6,-1,10,8,-10,-10,-1,-8,-5,-6,9,5,-2,7,2,3,-7,-7,-4,-10,7,7,1,4,2,-9,3,10,4,-3,5,6,-2,-9,-5,9,1,9,-3,-9,2,6,4,3,1,-4,-9,10,-3,-8,-8,-2,6,10,-4,-2,9,-2,-4,-10,-10,-3,7,10,10,10,-8,-6,4,2,7,4,2,8,2,10,6,-1,-7,-5,-1,-5,-7,-1,-9,7,-7,-1,-9,-6,8,-1,1,7,4,-7,7,4,-4,-5,10,-8,-4,-7,-7,4,-8,8,-8,9,7,7,-9,9,7,-6,-5,3,3,-2,4,-4,2,4,-8,-2,-9,10,1,3,1,-5,4,-6,8,5,-6,4,2,-8,1,5,10,-1,-3,8,-2,2,1,-2,8,2,-8,-9,-6,-9,10,10,9,2,-4,8,5,1,-8,6,-2,-9,7,-9,7,-2,3,-7,-1,-6,1,-2,-6,4,-8,9,1,8,-5,10,8,1,4,-6,8,10,8,8,7,-5,4,-2,-3,10,-9,2,-2,9,-10,1,-6,9,-4,-5,9,-3,7,8,8,-8,10,-4,-10,10,-7,7,-3,7,-3,8,6,7,-1,-1,-2,-5,8,7,-2,9,-8,-3,3,10,-2,-10,-4,-2,-1,-3,2,7,9,10,-1,-1,5,1,3,6,2,6,4,-10,-10,9,-10,4,10,-3,2,3,-7,3,-8,7,-6,3,-10,-4,5,-4,10,6,-1,5,2,-9,2,1,5,-9,3,-9,-6,-5,8,8,7,-10,-5,-4,-2,-10,-8,-6,10,-2,-9,8,-7,6,2,3,-2,-10,9,7,-8,8,9,7,-1,-4,3,6,7,-3,-10,2,9,-2,-7,-2,6,-1,5,-6,-10,-9,-4,-10,8,4,2,-1,-8,-1,-2,10,-2,4,-10,8,-1,-2,1,-8,5,-1,5,-8,-5,-10,2,6,10,5,-10,-1,-9,6,4,1,5,6,3,5,-5,-6,4,2,4,5,8,3,-8,7,2,-1,1,-6,-3,4,-5,-4,-2,2,-4,10,-4,9,-3,-4,-6,1,-2,2,8,-3,6,-2,6,6,1,-1,-10,-5,-9,-9,3,4,9,-1,4,1,-1,-10,-5,6,4,-10,-10,-9,-5,-5,10,-2,-5,-7,-6,9,-9,6,-7,1,2,8,-6,10,-7,10,4,8,6,10,-4,-1,10,-9,10,8,3,1,-5,3,-5,1,6,9,-5,-3,-8,3,2,4,-4,-3,2,-8,-6,-1,3,-10,-5,10,8,10,8,5,-5,-3,3,8,3,-2,-7,3,9,1,-4,4,4,9,5,-5,3,1,-7,1,7,10,8,-5,9,-1,-7,-5,8,7,10,-6,-2,-8,8,-9,-3,-8,-4,-10,-1,4,-5,-10,-4,6,1,-6,-9,-9,6,-9,-9,-1,-1,4,3,9,8,1,-8,-8,9,9,-10,4,-8,-4,1,10,8,2,-3,-9,10,-4,7,5,-8,5,-5,-4,3,2,3,5,-7,1,8,10,10,-6,8,4,-10,-5,-7,9,-5,3,4,-1,5,-8,4,2,-6,10,2,1,2,-8,-5,8,-10,9,-8,-3,-2,5,3,-9,-6,2,-4,1,-8,-6,5,-4,6,-1,4,7,-6,-4,-8,7,-4,1,3,4,10,-6,-8,2,-4,8,6,3,-8,1,2,9,9,1,-1,-5,9,-5,-2,10,-7,-3,6,5,5,-1,7,10,-9,10,-10,-10,-8,5,-2,-5,5,-4,-4,-4,-6,-5,-4,-9,-7,-4,5,5,1,-3,-7,5,-6,3,-7,-10,-4,4,-1,-3,-3,7,-3,9,-4,-8,-1,-5,2,-7,-6,2,4,-10,-10,-5,-9,8,7,-5,-10,-4,-8,7,6,8,5,-4,5,-5,-6,-7,5,7,5,-4,7,-5,8,6,10,-6,6,-3,3,-8,-10,-3,10,-6,-2,-9,10,-5,-10,2,4,6,-9,3,-8,-10,5,3,3,-2,2,5,9,-10,-10,-10,10,6,-6,-1,9,-3,7,2,9,-7,7,-3,-2,7,5,6,-5,3,1,-6,-5,5,-6,2,-10,6,-10,8,-4,-4,4,2,-4,1,-1,6,-7,-10,7,-8,-2,8,5,-6,1,-8,1,4,-7,3,-3,5,-9,3,-6,4,-7,-2,8,-3,-7,4,1,5,5,5,6,-8,-5,-10,-1,-1,-7,-5,10,-2,9,6,7,9,1,10,5,2,-8,-3,7,9,8,6,2,-6,5,-10,-7,-4,4,-6,3,-9,8,-2,-7,-8,-5,-4,2,9,-3,-10,9,-9,-10,-9,2,-6,9,7,10,-10,8,3,3,-7,-2,-7,1,-3,-10,3,-10,2,8,-5,5,-3,-7,-2,10,-9,6,-3,-3,-7,-7,-6,-3,8,10,-10,-9,7,-1,8,-6,-4,-4,-1,-3,1,1,9,-8,3,-10,-2,-8,-7,-5,2,2,6,-3,3,5,8,-3,-10,-5,10,8,4,-10,6,-6,1,-4,-3,5,-5,-2,-6,9,8,1,-9,2,6,6,9,10,-9,-8,1,8,4,8,-9,-8,-1,6,1,-5,2,-8,-3,-5,-3,3,-6,10,5,2,7,2,10,-9,-8,5,-8,-4,-3,1,2,10,9,8,9,9,-9,-5,-8,7,3,-9,8,1,-10,7,-8,-10,6,2,-7,3,-1,4,-5,7,-4,8,-10,3,-1,4,5,8,-3,1,1,-7,-4,-2,-1,-8,5,-6,5,7,-8,-7,4,-8,-6,-6,-5,-7,-3,10,10,-6,4,-2,-1,-6,7,-2,1,-7,-1,3,-7,2,1,-3,-10,8,2,2,6,-10,3,3,4,-10,4,-10,6,-10,-4,8,1,-7,-5,-4,-10,3,8,7,5,-8,3,-9,-10,5,-1,9,8,-4,-6,3,5,-1,-9,7,-8,-4,-5,-9,1,10,-7,-3,4,10,-6,-7,-7,3,9,-2,7,7,9,6,9,4,-4,1,-6,9,3,2,6,-8,9,1,7,7,-3,-8,10,8,-8,-9,1,-6,-6,4,8,-7,5,-3,4,-10,5,-1,9,7,8,4,6,2,10,5,2,-3,8,9,5,10,7,-5,1,-8,7,-8,3,8,8,1,3,-6,1,-6,-7,8,-8,-2,4,7,1,-8,-7,-8,-8,-6,-7,4,10,-6,-6,10,-9,4,4,7,-1,2,9,-5,-2,-2,3,-9,-5,9,1,-9,6,6,-9,7,-5,-7,10,-5,-3,3,2,1,7,1,1,-10,5,7,8,3,-3,-2,-10,-7,-2,1,2,-1,1,-1,-6,-9,9,-7,10,-10,10,-9,-9,-5,9,-4,5,-2,-1,-1,5,10,-6,1,-6,-2,-5,9,7,4,10,-9,-5,-3,3,3,-6,4,-9,9,-5,4,-1,-3,-8,6,-7,5,5,8,4,8,4,3,6,-1,-2,-3,5,-3,5,1,2,3,7,-5,-5,-2,-4,4,-4,1,7,1,1,7,3,7,-7,3,6,-5,-3,-1,10,9,10,4,-3,3,10,10,-9,9,1,-10,-3,7,-3,-5,4,1,-3,3,-1,-1,-6,4,-10,-3,-6,8,-9,-7,3,-7,7,1,2,-7,-8,-4,1,-10,-1,-6,8,-8,8,9,-1,-8,-4,-8,1,-9,-8,-3,-1,2,8,10,-1,-10,6,-2,-8,5,7,10,1,-9,4,-7,-7,-6,-8,-8,7,-10,1,-9,-10,3,-8,-7,6,-7,8,-7,5,-9,-2,-2,6,1,3,6,-4,1,4,2,-6,10,7,8,-3,-6,3,-1,9,-6,-3,6,-3,-1,6,7,-6,-5,-6,-4,-9,3,8,3,-7,-10,3,-8,-4,3,4,-10,-1,-1,8,-6,-6,3,5,3,-6,2,8,8,-9,-2,3,3,-8,10,2,5,7,3,-3,-3,9,8,7,9,-9,1,2,-7,-8,6,-3,7,-8,-1,5,10,3,-1,-8,-6,-1,10,-9,-2,1,7,1,-5,4,-2,2,-3,3,-3,4,7,-8,-9,-1,-4,-10,-6,4,-2,7,-7,5,4,-6,9,10,-7,1,5,-8,-4,-9,1,-4,-2,-6,-2,9,-1,4,-6,5,3,9,8,7,6,-4,1,-2,9,-2,-1,6,7,-3,6,-4,6,7,1,-5,1,-5,-7,7,-5,6,1,9,4,1,-9,-9,8,-8,9,7,-5,4,7,10,10,7,10,1,7,-3,7,-5,7,6,-9,10,5,-7,-5,4,3,-9,7,-4,-4,-5,1,9,-3,6,10,-5,-9,-7,9,2,-3,4,4,8,-7,8,3,5,-4,10,-8,9,9,-4,5,2,-8,8,6,-10,9,2,7,1,-2,-5,8,-8,8,-7,7,-1,-8,6,6,-9,-6,-10,2,-4,2,3,-3,-9,2,-6,-9,-5,-7,-3,9,-10,4,-7,1,9,1,5,4,7,-4,-4,-1,10,-1,10,4,2,10,-4,-1,6,8,5,7,-7,-6,-2,1,-4,-4,10,-8,5,2,-9,-6,-4,-6,4,3,-4,4,8,9,-6,10,-10,10,6,-7,-4,2,9,9,1,5,-4,3,-4,6,5,8,2,-1,2,5,-4,6,-5,7,6,3,-10,-2,1,6,3,9,2,6,-1,9,-8,-7,7,-10,5,-5,-2,-1,6,-8,1,-6,9,-6,5,-6,-10,7,-6,-4,-4,9,-7,-8,-8,-2,6,-2,2,-5,-3,3,5,-3,-8,-3,-6,-10,-3,-6,7,-1,-9,-7,-3,9,5,-1,1,3,-3,-4,1,1,-4,-8,-8,3,-2,-8,5,10,1,-2,5,6,4,-6,5,2,8,-10,6,4,4,-2,-3,-10,-4,-9,-10,9,-4,-10,6,-8,-9,-3,-4,5,-10,8,7,-10,-10,4,-3,-3,-9,7,4,-10,-8,10,-9,-1,-1,-4,6,-1,-2,-8,7,-5,-6,-10,10,7,-2,-9,3,-9,8,3,7,2,-9,8,4,2,6,2,3,-3,6,3,-1,-2,-6,-4,-10,-4,-7,-7,-6,10,-5,5,10,3,1,5,-10,10,5,1,-10,-4,-9,-7,2,-4,-10,6,-10,-7,-9,-2,3,-7,8,2,4,5,9,-8,-1,-9,-5,10,6,-4,-10,-3,10,1,-7,6,-9,5,-4,10,-9,-6,-5,-10,6,7,-2,-8,10,10,2,-9,6,-10,8,8,2,2,2,10,5,3,8,10,3,-5,4,8,9,2,10,7,-8,1,10,-10,-9,-4,6,-6,2,8,7,-7,5,-6,-1,-9,3,-1,-1,1,3,8,-7,-2], dtype = "uint8")#candidate|4654|(3900,)|const|uint8
call_4653 = relay.TupleGetItem(func_3293_call(relay.reshape(const_4654.astype('uint8'), [3900,]), relay.reshape(const_4654.astype('bool'), [780, 5]), ), 0)
call_4655 = relay.TupleGetItem(func_3297_call(relay.reshape(const_4654.astype('uint8'), [3900,]), relay.reshape(const_4654.astype('bool'), [780, 5]), ), 0)
output = relay.Tuple([call_4604,call_4612,call_4631,bop_4646,uop_4649,call_4653,const_4654,])
output2 = relay.Tuple([call_4605,call_4614,call_4632,bop_4646,uop_4649,call_4655,const_4654,])
func_4657 = relay.Function([var_4624,], output)
mod['func_4657'] = func_4657
mod = relay.transform.InferType()(mod)
mutated_mod['func_4657'] = func_4657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4658 = relay.var("var_4658", dtype = "int32", shape = (2, 847))#candidate|4658|(2, 847)|var|int32
func_4657_call = mutated_mod.get_global_var('func_4657')
call_4659 = func_4657_call(var_4658)
output = call_4659
func_4660 = relay.Function([var_4658], output)
mutated_mod['func_4660'] = func_4660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2379_call = mod.get_global_var('func_2379')
func_2381_call = mutated_mod.get_global_var('func_2381')
call_4662 = relay.TupleGetItem(func_2379_call(), 2)
call_4663 = relay.TupleGetItem(func_2381_call(), 2)
uop_4668 = relay.log10(call_4662.astype('float32')) # shape=(780, 1)
uop_4670 = relay.log10(call_4663.astype('float32')) # shape=(780, 1)
bop_4671 = relay.greater_equal(uop_4668.astype('bool'), relay.reshape(call_4662.astype('bool'), relay.shape_of(uop_4668))) # shape=(780, 1)
bop_4674 = relay.greater_equal(uop_4670.astype('bool'), relay.reshape(call_4663.astype('bool'), relay.shape_of(uop_4670))) # shape=(780, 1)
output = relay.Tuple([bop_4671,])
output2 = relay.Tuple([bop_4674,])
func_4675 = relay.Function([], output)
mod['func_4675'] = func_4675
mod = relay.transform.InferType()(mod)
output = func_4675()
func_4676 = relay.Function([], output)
mutated_mod['func_4676'] = func_4676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2894_call = mod.get_global_var('func_2894')
func_2895_call = mutated_mod.get_global_var('func_2895')
call_4741 = relay.TupleGetItem(func_2894_call(), 3)
call_4742 = relay.TupleGetItem(func_2895_call(), 3)
output = relay.Tuple([call_4741,])
output2 = relay.Tuple([call_4742,])
func_4743 = relay.Function([], output)
mod['func_4743'] = func_4743
mod = relay.transform.InferType()(mod)
mutated_mod['func_4743'] = func_4743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4743_call = mutated_mod.get_global_var('func_4743')
call_4744 = func_4743_call()
output = call_4744
func_4745 = relay.Function([], output)
mutated_mod['func_4745'] = func_4745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3722_call = mod.get_global_var('func_3722')
func_3724_call = mutated_mod.get_global_var('func_3724')
call_4749 = func_3722_call()
call_4750 = func_3722_call()
uop_4755 = relay.log10(call_4749.astype('float32')) # shape=(10, 3, 13)
uop_4757 = relay.log10(call_4750.astype('float32')) # shape=(10, 3, 13)
output = uop_4755
output2 = uop_4757
func_4758 = relay.Function([], output)
mod['func_4758'] = func_4758
mod = relay.transform.InferType()(mod)
output = func_4758()
func_4759 = relay.Function([], output)
mutated_mod['func_4759'] = func_4759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3749_call = mod.get_global_var('func_3749')
func_3751_call = mutated_mod.get_global_var('func_3751')
call_4840 = func_3749_call()
call_4841 = func_3749_call()
uop_4848 = relay.tan(call_4840.astype('float64')) # shape=(10, 3, 13)
uop_4850 = relay.tan(call_4841.astype('float64')) # shape=(10, 3, 13)
output = uop_4848
output2 = uop_4850
func_4862 = relay.Function([], output)
mod['func_4862'] = func_4862
mod = relay.transform.InferType()(mod)
output = func_4862()
func_4863 = relay.Function([], output)
mutated_mod['func_4863'] = func_4863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_4924 = relay.TupleGetItem(func_988_call(), 0)
call_4925 = relay.TupleGetItem(func_990_call(), 0)
output = relay.Tuple([call_4924,])
output2 = relay.Tuple([call_4925,])
func_4975 = relay.Function([], output)
mod['func_4975'] = func_4975
mod = relay.transform.InferType()(mod)
mutated_mod['func_4975'] = func_4975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4975_call = mutated_mod.get_global_var('func_4975')
call_4976 = func_4975_call()
output = call_4976
func_4977 = relay.Function([], output)
mutated_mod['func_4977'] = func_4977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3681_call = mod.get_global_var('func_3681')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_4981 = relay.TupleGetItem(func_3681_call(), 0)
call_4982 = relay.TupleGetItem(func_3682_call(), 0)
output = call_4981
output2 = call_4982
func_4990 = relay.Function([], output)
mod['func_4990'] = func_4990
mod = relay.transform.InferType()(mod)
mutated_mod['func_4990'] = func_4990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4990_call = mutated_mod.get_global_var('func_4990')
call_4991 = func_4990_call()
output = call_4991
func_4992 = relay.Function([], output)
mutated_mod['func_4992'] = func_4992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4990_call = mod.get_global_var('func_4990')
func_4992_call = mutated_mod.get_global_var('func_4992')
call_5108 = func_4990_call()
call_5109 = func_4990_call()
output = call_5108
output2 = call_5109
func_5122 = relay.Function([], output)
mod['func_5122'] = func_5122
mod = relay.transform.InferType()(mod)
mutated_mod['func_5122'] = func_5122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5122_call = mutated_mod.get_global_var('func_5122')
call_5123 = func_5122_call()
output = call_5123
func_5124 = relay.Function([], output)
mutated_mod['func_5124'] = func_5124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_5129 = relay.TupleGetItem(func_1931_call(), 4)
call_5130 = relay.TupleGetItem(func_1933_call(), 4)
output = relay.Tuple([call_5129,])
output2 = relay.Tuple([call_5130,])
func_5178 = relay.Function([], output)
mod['func_5178'] = func_5178
mod = relay.transform.InferType()(mod)
output = func_5178()
func_5179 = relay.Function([], output)
mutated_mod['func_5179'] = func_5179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5195 = relay.var("var_5195", dtype = "float32", shape = (13, 4, 4))#candidate|5195|(13, 4, 4)|var|float32
uop_5196 = relay.sinh(var_5195.astype('float32')) # shape=(13, 4, 4)
output = relay.Tuple([uop_5196,])
output2 = relay.Tuple([uop_5196,])
func_5201 = relay.Function([var_5195,], output)
mod['func_5201'] = func_5201
mod = relay.transform.InferType()(mod)
mutated_mod['func_5201'] = func_5201
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5202 = relay.var("var_5202", dtype = "float32", shape = (13, 4, 4))#candidate|5202|(13, 4, 4)|var|float32
func_5201_call = mutated_mod.get_global_var('func_5201')
call_5203 = func_5201_call(var_5202)
output = call_5203
func_5204 = relay.Function([var_5202], output)
mutated_mod['func_5204'] = func_5204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2511_call = mod.get_global_var('func_2511')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_5231 = func_2511_call()
call_5232 = func_2511_call()
output = relay.Tuple([call_5231,])
output2 = relay.Tuple([call_5232,])
func_5242 = relay.Function([], output)
mod['func_5242'] = func_5242
mod = relay.transform.InferType()(mod)
output = func_5242()
func_5243 = relay.Function([], output)
mutated_mod['func_5243'] = func_5243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4990_call = mod.get_global_var('func_4990')
func_4992_call = mutated_mod.get_global_var('func_4992')
call_5273 = func_4990_call()
call_5274 = func_4990_call()
output = call_5273
output2 = call_5274
func_5279 = relay.Function([], output)
mod['func_5279'] = func_5279
mod = relay.transform.InferType()(mod)
output = func_5279()
func_5280 = relay.Function([], output)
mutated_mod['func_5280'] = func_5280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3884_call = mod.get_global_var('func_3884')
func_3886_call = mutated_mod.get_global_var('func_3886')
call_5350 = func_3884_call()
call_5351 = func_3884_call()
output = call_5350
output2 = call_5351
func_5357 = relay.Function([], output)
mod['func_5357'] = func_5357
mod = relay.transform.InferType()(mod)
output = func_5357()
func_5358 = relay.Function([], output)
mutated_mod['func_5358'] = func_5358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_5366 = relay.TupleGetItem(func_4386_call(), 0)
call_5367 = relay.TupleGetItem(func_4388_call(), 0)
func_1087_call = mod.get_global_var('func_1087')
func_1090_call = mutated_mod.get_global_var('func_1090')
var_5378 = relay.var("var_5378", dtype = "int32", shape = (847, 1))#candidate|5378|(847, 1)|var|int32
call_5377 = relay.TupleGetItem(func_1087_call(relay.reshape(var_5378.astype('int32'), [847,])), 1)
call_5379 = relay.TupleGetItem(func_1090_call(relay.reshape(var_5378.astype('int32'), [847,])), 1)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_5394 = relay.TupleGetItem(func_2881_call(), 0)
call_5395 = relay.TupleGetItem(func_2883_call(), 0)
bop_5398 = relay.left_shift(var_5378.astype('uint16'), relay.reshape(call_5377.astype('uint16'), relay.shape_of(var_5378))) # shape=(847, 1)
bop_5401 = relay.left_shift(var_5378.astype('uint16'), relay.reshape(call_5379.astype('uint16'), relay.shape_of(var_5378))) # shape=(847, 1)
uop_5411 = relay.erf(bop_5398.astype('float64')) # shape=(847, 1)
uop_5413 = relay.erf(bop_5401.astype('float64')) # shape=(847, 1)
bop_5414 = relay.bitwise_and(uop_5411.astype('int64'), relay.reshape(var_5378.astype('int64'), relay.shape_of(uop_5411))) # shape=(847, 1)
bop_5417 = relay.bitwise_and(uop_5413.astype('int64'), relay.reshape(var_5378.astype('int64'), relay.shape_of(uop_5413))) # shape=(847, 1)
output = relay.Tuple([call_5366,call_5394,bop_5414,])
output2 = relay.Tuple([call_5367,call_5395,bop_5417,])
func_5437 = relay.Function([var_5378,], output)
mod['func_5437'] = func_5437
mod = relay.transform.InferType()(mod)
var_5438 = relay.var("var_5438", dtype = "int32", shape = (847, 1))#candidate|5438|(847, 1)|var|int32
output = func_5437(var_5438)
func_5439 = relay.Function([var_5438], output)
mutated_mod['func_5439'] = func_5439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5462 = relay.var("var_5462", dtype = "float32", shape = (7, 5, 13))#candidate|5462|(7, 5, 13)|var|float32
uop_5463 = relay.log10(var_5462.astype('float32')) # shape=(7, 5, 13)
bop_5468 = relay.floor_divide(var_5462.astype('float64'), relay.reshape(uop_5463.astype('float64'), relay.shape_of(var_5462))) # shape=(7, 5, 13)
func_5201_call = mod.get_global_var('func_5201')
func_5204_call = mutated_mod.get_global_var('func_5204')
const_5484 = relay.const([-5.430592,-0.778901,-0.702943,-9.408526,9.818528,-4.213518,-2.303923,-6.039636,8.083420,-1.727638,7.830895,-3.152398,-0.287976,1.405510,0.865575,-1.331855,6.169206,9.923801,-3.546620,-0.399285,-5.494337,8.963711,4.516490,-6.306416,-2.908001,-5.608989,3.907203,5.590832,5.487817,3.308820,3.789552,-8.461421,2.535843,-8.490985,6.839246,9.738794,-5.865615,-6.856778,-2.746056,-3.776683,3.301784,-1.527187,8.452572,4.470140,-4.718906,-2.681637,-8.026405,3.913430,-3.472764,0.220727,-8.353178,3.795078,9.797042,-1.601283,-2.637531,-4.478905,-4.448308,-6.198897,0.374119,-8.407109,9.475666,1.412166,-8.608004,8.877606,7.860294,-0.100065,3.548533,-7.723742,-5.302129,-8.134556,9.316719,-4.950839,-7.628551,7.130087,-0.717448,6.620864,-3.450552,3.486085,0.904926,1.045940,-3.766036,-0.847125,9.271279,-9.254289,-3.367329,7.730052,-0.172865,1.315755,-5.725905,-2.828715,-4.034436,-9.494066,-0.151776,0.841740,-0.223163,-6.062807,6.120290,-9.941078,8.694953,-8.965411,-9.282064,2.889103,2.046634,9.323897,-3.654016,8.977728,4.151687,0.731498,0.511889,-3.312364,-6.252681,-0.805493,7.082108,-0.294129,-3.643108,-8.753104,-1.336430,7.048907,-9.871188,-0.909502,-4.201129,-4.820605,8.416524,8.756468,-4.131192,0.992557,4.960394,-1.459747,-4.798067,4.588176,2.159769,4.144548,-7.797140,-7.410147,8.781046,1.222998,-0.903880,-3.190993,2.847940,-6.624911,8.412711,-2.970322,-4.420108,3.105170,-5.024076,6.458048,1.679922,1.085132,6.364913,-9.204809,-0.816568,-7.427790,9.963287,9.485114,-6.431070,8.403518,3.386573,-8.173894,-7.336480,-6.667075,8.873432,9.906983,1.817350,-9.623704,-3.595847,5.118077,-9.078743,3.977715,-7.949899,-3.743784,-2.407065,-5.363791,-3.405348,2.517326,2.718128,8.944300,5.387479,8.567440,2.886410,3.942665,-3.144231,6.264933,-9.283447,0.476380,9.407256,-9.763672,9.988687,8.379223,5.787739,-7.032484,-5.194862,3.771988,-1.009280,-7.868969,-4.173838,9.793180,9.887649,7.401739,1.548531,-1.316132,8.651461,1.064258,-2.181485,-8.593451,0.561716,-9.235739,-9.421199,-2.549372], dtype = "float32")#candidate|5484|(208,)|const|float32
call_5483 = relay.TupleGetItem(func_5201_call(relay.reshape(const_5484.astype('float32'), [13, 4, 4])), 0)
call_5485 = relay.TupleGetItem(func_5204_call(relay.reshape(const_5484.astype('float32'), [13, 4, 4])), 0)
output = relay.Tuple([bop_5468,call_5483,const_5484,])
output2 = relay.Tuple([bop_5468,call_5485,const_5484,])
func_5486 = relay.Function([var_5462,], output)
mod['func_5486'] = func_5486
mod = relay.transform.InferType()(mod)
var_5487 = relay.var("var_5487", dtype = "float32", shape = (7, 5, 13))#candidate|5487|(7, 5, 13)|var|float32
output = func_5486(var_5487)
func_5488 = relay.Function([var_5487], output)
mutated_mod['func_5488'] = func_5488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5279_call = mod.get_global_var('func_5279')
func_5280_call = mutated_mod.get_global_var('func_5280')
call_5524 = func_5279_call()
call_5525 = func_5279_call()
func_2842_call = mod.get_global_var('func_2842')
func_2843_call = mutated_mod.get_global_var('func_2843')
call_5527 = relay.TupleGetItem(func_2842_call(), 0)
call_5528 = relay.TupleGetItem(func_2843_call(), 0)
func_5279_call = mod.get_global_var('func_5279')
func_5280_call = mutated_mod.get_global_var('func_5280')
call_5534 = func_5279_call()
call_5535 = func_5279_call()
output = relay.Tuple([call_5524,call_5527,call_5534,])
output2 = relay.Tuple([call_5525,call_5528,call_5535,])
func_5542 = relay.Function([], output)
mod['func_5542'] = func_5542
mod = relay.transform.InferType()(mod)
output = func_5542()
func_5543 = relay.Function([], output)
mutated_mod['func_5543'] = func_5543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2511_call = mod.get_global_var('func_2511')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_5589 = func_2511_call()
call_5590 = func_2511_call()
func_3884_call = mod.get_global_var('func_3884')
func_3886_call = mutated_mod.get_global_var('func_3886')
call_5597 = func_3884_call()
call_5598 = func_3884_call()
output = relay.Tuple([call_5589,call_5597,])
output2 = relay.Tuple([call_5590,call_5598,])
func_5608 = relay.Function([], output)
mod['func_5608'] = func_5608
mod = relay.transform.InferType()(mod)
mutated_mod['func_5608'] = func_5608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5608_call = mutated_mod.get_global_var('func_5608')
call_5609 = func_5608_call()
output = call_5609
func_5610 = relay.Function([], output)
mutated_mod['func_5610'] = func_5610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_5657 = relay.TupleGetItem(func_1822_call(), 2)
call_5658 = relay.TupleGetItem(func_1824_call(), 2)
func_3929_call = mod.get_global_var('func_3929')
func_3931_call = mutated_mod.get_global_var('func_3931')
call_5679 = relay.TupleGetItem(func_3929_call(), 0)
call_5680 = relay.TupleGetItem(func_3931_call(), 0)
func_3005_call = mod.get_global_var('func_3005')
func_3007_call = mutated_mod.get_global_var('func_3007')
call_5681 = relay.TupleGetItem(func_3005_call(), 2)
call_5682 = relay.TupleGetItem(func_3007_call(), 2)
uop_5701 = relay.erf(call_5679.astype('float32')) # shape=(7, 14, 4)
uop_5703 = relay.erf(call_5680.astype('float32')) # shape=(7, 14, 4)
func_4990_call = mod.get_global_var('func_4990')
func_4992_call = mutated_mod.get_global_var('func_4992')
call_5704 = func_4990_call()
call_5705 = func_4990_call()
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_5709 = func_1322_call()
call_5710 = func_1322_call()
var_5711 = relay.var("var_5711", dtype = "float32", shape = (7, 14, 4))#candidate|5711|(7, 14, 4)|var|float32
bop_5712 = relay.right_shift(uop_5701.astype('int8'), relay.reshape(var_5711.astype('int8'), relay.shape_of(uop_5701))) # shape=(7, 14, 4)
bop_5715 = relay.right_shift(uop_5703.astype('int8'), relay.reshape(var_5711.astype('int8'), relay.shape_of(uop_5703))) # shape=(7, 14, 4)
func_4990_call = mod.get_global_var('func_4990')
func_4992_call = mutated_mod.get_global_var('func_4992')
call_5730 = func_4990_call()
call_5731 = func_4990_call()
func_3005_call = mod.get_global_var('func_3005')
func_3007_call = mutated_mod.get_global_var('func_3007')
call_5735 = relay.TupleGetItem(func_3005_call(), 1)
call_5736 = relay.TupleGetItem(func_3007_call(), 1)
output = relay.Tuple([call_5657,call_5681,call_5704,call_5709,bop_5712,call_5730,call_5735,])
output2 = relay.Tuple([call_5658,call_5682,call_5705,call_5710,bop_5715,call_5731,call_5736,])
func_5742 = relay.Function([var_5711,], output)
mod['func_5742'] = func_5742
mod = relay.transform.InferType()(mod)
mutated_mod['func_5742'] = func_5742
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5743 = relay.var("var_5743", dtype = "float32", shape = (7, 14, 4))#candidate|5743|(7, 14, 4)|var|float32
func_5742_call = mutated_mod.get_global_var('func_5742')
call_5744 = func_5742_call(var_5743)
output = call_5744
func_5745 = relay.Function([var_5743], output)
mutated_mod['func_5745'] = func_5745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4862_call = mod.get_global_var('func_4862')
func_4863_call = mutated_mod.get_global_var('func_4863')
call_5771 = func_4862_call()
call_5772 = func_4862_call()
output = relay.Tuple([call_5771,])
output2 = relay.Tuple([call_5772,])
func_5781 = relay.Function([], output)
mod['func_5781'] = func_5781
mod = relay.transform.InferType()(mod)
output = func_5781()
func_5782 = relay.Function([], output)
mutated_mod['func_5782'] = func_5782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5242_call = mod.get_global_var('func_5242')
func_5243_call = mutated_mod.get_global_var('func_5243')
call_5829 = relay.TupleGetItem(func_5242_call(), 0)
call_5830 = relay.TupleGetItem(func_5243_call(), 0)
output = relay.Tuple([call_5829,])
output2 = relay.Tuple([call_5830,])
func_5842 = relay.Function([], output)
mod['func_5842'] = func_5842
mod = relay.transform.InferType()(mod)
output = func_5842()
func_5843 = relay.Function([], output)
mutated_mod['func_5843'] = func_5843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3722_call = mod.get_global_var('func_3722')
func_3724_call = mutated_mod.get_global_var('func_3724')
call_5875 = func_3722_call()
call_5876 = func_3722_call()
output = relay.Tuple([call_5875,])
output2 = relay.Tuple([call_5876,])
func_5878 = relay.Function([], output)
mod['func_5878'] = func_5878
mod = relay.transform.InferType()(mod)
output = func_5878()
func_5879 = relay.Function([], output)
mutated_mod['func_5879'] = func_5879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_5908 = relay.TupleGetItem(func_1126_call(), 0)
call_5909 = relay.TupleGetItem(func_1127_call(), 0)
func_3929_call = mod.get_global_var('func_3929')
func_3931_call = mutated_mod.get_global_var('func_3931')
call_5917 = relay.TupleGetItem(func_3929_call(), 0)
call_5918 = relay.TupleGetItem(func_3931_call(), 0)
output = relay.Tuple([call_5908,call_5917,])
output2 = relay.Tuple([call_5909,call_5918,])
func_5940 = relay.Function([], output)
mod['func_5940'] = func_5940
mod = relay.transform.InferType()(mod)
mutated_mod['func_5940'] = func_5940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5940_call = mutated_mod.get_global_var('func_5940')
call_5941 = func_5940_call()
output = call_5941
func_5942 = relay.Function([], output)
mutated_mod['func_5942'] = func_5942
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5983 = relay.var("var_5983", dtype = "int64", shape = (11, 11, 1))#candidate|5983|(11, 11, 1)|var|int64
var_5984 = relay.var("var_5984", dtype = "int64", shape = (11, 11, 15))#candidate|5984|(11, 11, 15)|var|int64
bop_5985 = relay.bitwise_and(var_5983.astype('int64'), var_5984.astype('int64')) # shape=(11, 11, 15)
uop_5991 = relay.log(var_5983.astype('float32')) # shape=(11, 11, 1)
uop_6008 = relay.atanh(var_5984.astype('float32')) # shape=(11, 11, 15)
bop_6010 = relay.greater_equal(uop_5991.astype('bool'), var_5984.astype('bool')) # shape=(11, 11, 15)
func_647_call = mod.get_global_var('func_647')
func_649_call = mutated_mod.get_global_var('func_649')
const_6014 = relay.const([[-10,-6,5,9,-1,5,-7,-3,8,-7,2,-6,-4,8,-10,6,9,3,1,-9,10,-8,-6,2,-2,-2,-8,1,3,7,-2,-5,6,8,-9,-4,1,-8,2,-3,-8,1,5,-9,-9,-2,-3,5,-7,9,-10,-7,-4,9,6,2,-7,9,5,8,6,7,1,9,7,-3,10,7,4,9,6,-3,4,-4,-2,3,6,-9,3,2,7,-4,-5,10,7,-1,-1,-7,-8,2,-7,2,-4,-8,-1,7,-6,-7,-4,-2,4,-5,10,10,4,2,8,3,-6,-10,-3,-7,6,2,8,-10,-9,-9,-8,1,-10,3,6,1,1,9,6,3,-9,-3,-8,1,-9,-8,-7,1,1,-7,-2,-1,8,6,-7,8,-3,2,6,-1,-2,-4,-10,-8,8,10,-2,4],[-10,-5,-1,-2,8,8,-7,-10,1,-8,8,-4,1,-10,-4,4,7,10,4,2,5,-7,10,1,-3,2,5,10,9,-9,-4,-6,2,-7,-7,-2,1,-5,7,2,-5,1,-10,7,1,-10,-9,-4,-4,1,9,6,-3,1,-8,-9,-7,4,3,5,-9,7,-5,3,1,1,-7,10,-9,-9,-3,-10,1,8,-7,-8,-9,-6,-3,4,-5,3,-1,4,-5,-6,5,3,-10,-2,3,5,2,-8,2,-8,-6,-1,-8,-8,-9,-3,8,2,6,-7,1,-3,-3,9,-1,-4,-10,6,9,-10,8,-5,-1,4,-9,6,-3,5,8,-1,1,-7,-10,8,7,-10,-1,-1,1,10,8,-4,-5,-7,2,-3,5,3,-1,7,-9,2,5,4,1,-8,2,-8,-10,9],[4,5,1,7,1,1,2,-3,7,4,5,-6,3,-3,8,-7,5,-4,-1,8,6,5,-3,6,8,-9,-2,-8,-9,-10,-5,1,-10,-6,-9,-5,4,-4,8,8,-2,7,-1,10,9,9,8,6,9,1,8,3,-5,10,9,-1,8,4,4,1,4,7,-2,-10,-7,-8,-8,-9,-8,-8,9,-7,-7,6,4,5,9,-10,9,1,2,2,-10,2,-10,-6,-10,-5,5,10,-1,9,-1,1,2,5,-9,5,8,9,10,4,-2,8,-2,-9,5,3,9,-5,3,-7,7,-6,-9,-2,2,-8,-6,-4,-5,3,2,-6,-9,-6,-3,9,-4,4,1,2,-1,-10,9,7,-8,5,-8,5,-4,-2,-3,-6,7,10,-7,1,-3,6,6,7,6,8,-3,-1],[-5,3,-5,4,-8,-10,-5,2,4,1,3,-8,9,3,10,-10,-9,4,1,-8,2,-5,-8,6,-7,4,4,1,9,-7,1,5,-10,6,6,-2,9,-7,4,-1,-10,-3,6,-8,-9,5,2,-10,10,6,9,6,5,4,-5,-4,-9,-9,-2,-1,2,1,-7,-6,8,-3,-10,-4,10,-6,-5,2,-7,1,8,10,-8,-5,5,-2,-5,-9,-3,2,3,2,10,1,5,-9,-4,4,-2,-10,2,10,-8,2,4,-7,-2,4,-3,9,9,-10,7,-8,4,-7,-10,2,8,9,8,10,5,1,-10,-3,-8,-3,-8,7,-9,-8,3,-6,4,4,1,1,9,3,2,-10,2,7,-6,-2,9,5,2,1,-5,9,9,4,-1,7,7,-4,-3,-9,-5,6],[-2,4,-2,-1,1,5,-7,-10,-9,2,6,-5,8,10,8,7,-8,-6,-7,-9,5,10,2,2,7,-7,1,4,9,-5,1,-7,-3,1,-7,6,-2,-6,6,-8,-2,-6,9,6,-3,5,1,6,4,-1,6,3,-6,6,6,5,-1,5,-10,-9,10,-10,7,-6,-1,-2,-6,7,-5,-4,-9,1,7,-3,4,1,-8,-6,4,6,9,-4,-4,-7,-4,-9,9,4,-5,4,-8,7,7,-1,-5,6,-2,9,1,-6,-8,-9,-7,4,9,3,-6,-3,4,-3,8,3,2,-7,-9,-10,-8,-7,-2,-8,10,8,4,8,-5,8,-2,5,-2,-9,-7,-1,7,-1,8,2,3,-5,-3,-4,6,2,-3,-2,-1,-8,-9,3,-7,-7,-4,-3,8,1,-3,-10]], dtype = "uint8")#candidate|6014|(5, 156)|const|uint8
call_6013 = func_647_call(relay.reshape(const_6014.astype('uint8'), [13, 10, 6]))
call_6015 = func_647_call(relay.reshape(const_6014.astype('uint8'), [13, 10, 6]))
output = relay.Tuple([bop_5985,uop_6008,bop_6010,call_6013,const_6014,])
output2 = relay.Tuple([bop_5985,uop_6008,bop_6010,call_6015,const_6014,])
func_6047 = relay.Function([var_5983,var_5984,], output)
mod['func_6047'] = func_6047
mod = relay.transform.InferType()(mod)
var_6048 = relay.var("var_6048", dtype = "int64", shape = (11, 11, 1))#candidate|6048|(11, 11, 1)|var|int64
var_6049 = relay.var("var_6049", dtype = "int64", shape = (11, 11, 15))#candidate|6049|(11, 11, 15)|var|int64
output = func_6047(var_6048,var_6049,)
func_6050 = relay.Function([var_6048,var_6049,], output)
mutated_mod['func_6050'] = func_6050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6084 = relay.var("var_6084", dtype = "int64", shape = (13, 12, 16))#candidate|6084|(13, 12, 16)|var|int64
var_6085 = relay.var("var_6085", dtype = "int64", shape = (13, 12, 16))#candidate|6085|(13, 12, 16)|var|int64
bop_6086 = relay.left_shift(var_6084.astype('int64'), relay.reshape(var_6085.astype('int64'), relay.shape_of(var_6084))) # shape=(13, 12, 16)
output = relay.Tuple([bop_6086,])
output2 = relay.Tuple([bop_6086,])
func_6092 = relay.Function([var_6084,var_6085,], output)
mod['func_6092'] = func_6092
mod = relay.transform.InferType()(mod)
var_6093 = relay.var("var_6093", dtype = "int64", shape = (13, 12, 16))#candidate|6093|(13, 12, 16)|var|int64
var_6094 = relay.var("var_6094", dtype = "int64", shape = (13, 12, 16))#candidate|6094|(13, 12, 16)|var|int64
output = func_6092(var_6093,var_6094,)
func_6095 = relay.Function([var_6093,var_6094,], output)
mutated_mod['func_6095'] = func_6095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5178_call = mod.get_global_var('func_5178')
func_5179_call = mutated_mod.get_global_var('func_5179')
call_6105 = relay.TupleGetItem(func_5178_call(), 0)
call_6106 = relay.TupleGetItem(func_5179_call(), 0)
output = relay.Tuple([call_6105,])
output2 = relay.Tuple([call_6106,])
func_6125 = relay.Function([], output)
mod['func_6125'] = func_6125
mod = relay.transform.InferType()(mod)
mutated_mod['func_6125'] = func_6125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6125_call = mutated_mod.get_global_var('func_6125')
call_6126 = func_6125_call()
output = call_6126
func_6127 = relay.Function([], output)
mutated_mod['func_6127'] = func_6127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2444_call = mod.get_global_var('func_2444')
func_2445_call = mutated_mod.get_global_var('func_2445')
call_6128 = relay.TupleGetItem(func_2444_call(), 0)
call_6129 = relay.TupleGetItem(func_2445_call(), 0)
output = call_6128
output2 = call_6129
func_6130 = relay.Function([], output)
mod['func_6130'] = func_6130
mod = relay.transform.InferType()(mod)
output = func_6130()
func_6131 = relay.Function([], output)
mutated_mod['func_6131'] = func_6131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2444_call = mod.get_global_var('func_2444')
func_2445_call = mutated_mod.get_global_var('func_2445')
call_6136 = relay.TupleGetItem(func_2444_call(), 0)
call_6137 = relay.TupleGetItem(func_2445_call(), 0)
uop_6138 = relay.rsqrt(call_6136.astype('float64')) # shape=(780, 1)
uop_6140 = relay.rsqrt(call_6137.astype('float64')) # shape=(780, 1)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_6143 = relay.TupleGetItem(func_988_call(), 0)
call_6144 = relay.TupleGetItem(func_990_call(), 0)
func_1664_call = mod.get_global_var('func_1664')
func_1666_call = mutated_mod.get_global_var('func_1666')
call_6147 = func_1664_call(relay.reshape(call_6143.astype('float64'), [7, 14, 4]))
call_6148 = func_1664_call(relay.reshape(call_6143.astype('float64'), [7, 14, 4]))
bop_6150 = relay.bitwise_and(uop_6138.astype('int8'), relay.reshape(call_6136.astype('int8'), relay.shape_of(uop_6138))) # shape=(780, 1)
bop_6153 = relay.bitwise_and(uop_6140.astype('int8'), relay.reshape(call_6137.astype('int8'), relay.shape_of(uop_6140))) # shape=(780, 1)
uop_6157 = relay.asin(call_6143.astype('float32')) # shape=(7, 14, 4)
uop_6159 = relay.asin(call_6144.astype('float32')) # shape=(7, 14, 4)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_6161 = func_1322_call()
call_6162 = func_1322_call()
func_2894_call = mod.get_global_var('func_2894')
func_2895_call = mutated_mod.get_global_var('func_2895')
call_6166 = relay.TupleGetItem(func_2894_call(), 0)
call_6167 = relay.TupleGetItem(func_2895_call(), 0)
var_6170 = relay.var("var_6170", dtype = "float32", shape = (7, 14, 4))#candidate|6170|(7, 14, 4)|var|float32
bop_6171 = relay.mod(call_6143.astype('float64'), relay.reshape(var_6170.astype('float64'), relay.shape_of(call_6143))) # shape=(7, 14, 4)
bop_6174 = relay.mod(call_6144.astype('float64'), relay.reshape(var_6170.astype('float64'), relay.shape_of(call_6144))) # shape=(7, 14, 4)
output = relay.Tuple([call_6147,bop_6150,uop_6157,call_6161,call_6166,bop_6171,])
output2 = relay.Tuple([call_6148,bop_6153,uop_6159,call_6162,call_6167,bop_6174,])
func_6177 = relay.Function([var_6170,], output)
mod['func_6177'] = func_6177
mod = relay.transform.InferType()(mod)
mutated_mod['func_6177'] = func_6177
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6178 = relay.var("var_6178", dtype = "float32", shape = (7, 14, 4))#candidate|6178|(7, 14, 4)|var|float32
func_6177_call = mutated_mod.get_global_var('func_6177')
call_6179 = func_6177_call(var_6178)
output = call_6179
func_6180 = relay.Function([var_6178], output)
mutated_mod['func_6180'] = func_6180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_6185 = relay.TupleGetItem(func_988_call(), 0)
call_6186 = relay.TupleGetItem(func_990_call(), 0)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_6208 = relay.TupleGetItem(func_856_call(), 0)
call_6209 = relay.TupleGetItem(func_858_call(), 0)
output = relay.Tuple([call_6185,call_6208,])
output2 = relay.Tuple([call_6186,call_6209,])
func_6223 = relay.Function([], output)
mod['func_6223'] = func_6223
mod = relay.transform.InferType()(mod)
output = func_6223()
func_6224 = relay.Function([], output)
mutated_mod['func_6224'] = func_6224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3722_call = mod.get_global_var('func_3722')
func_3724_call = mutated_mod.get_global_var('func_3724')
call_6241 = func_3722_call()
call_6242 = func_3722_call()
uop_6248 = relay.atan(call_6241.astype('float64')) # shape=(10, 3, 13)
uop_6250 = relay.atan(call_6242.astype('float64')) # shape=(10, 3, 13)
output = relay.Tuple([uop_6248,])
output2 = relay.Tuple([uop_6250,])
func_6251 = relay.Function([], output)
mod['func_6251'] = func_6251
mod = relay.transform.InferType()(mod)
output = func_6251()
func_6252 = relay.Function([], output)
mutated_mod['func_6252'] = func_6252
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6257 = relay.var("var_6257", dtype = "float32", shape = (16, 13, 12))#candidate|6257|(16, 13, 12)|var|float32
uop_6258 = relay.atanh(var_6257.astype('float32')) # shape=(16, 13, 12)
func_6177_call = mod.get_global_var('func_6177')
func_6180_call = mutated_mod.get_global_var('func_6180')
const_6269 = relay.const([8.601352,3.030559,-4.269403,-0.414180,-2.341989,-2.694269,-5.708160,9.276626,-0.693840,-2.534625,6.555268,8.695897,5.506829,-0.507080,-7.260342,-8.053155,5.291695,7.142700,1.559296,0.637131,5.020244,8.818180,3.209766,-3.186070,7.713216,-2.466471,-3.933747,-6.854276,5.717597,-2.889162,5.003446,8.166006,-9.469048,-5.561825,-2.288501,3.375397,8.154620,-1.544859,-7.096042,9.148052,4.787604,-5.452079,3.497678,9.461998,9.106559,-7.821541,6.740886,0.228055,-9.536846,9.221215,5.376769,6.876049,3.991885,-5.981836,-3.252950,-9.131510,0.606228,6.831140,6.375156,-5.365414,-9.374274,8.657133,-4.196104,3.162846,-6.315829,-6.650702,-1.011478,9.914622,2.457485,1.040101,5.917378,3.651511,-7.804737,0.855415,-1.988235,4.018279,-0.661026,-8.292890,5.677982,1.506867,-6.093547,-6.565509,8.352440,4.681804,6.321495,-7.232237,-8.267415,4.545735,-5.106325,-8.809170,-6.046708,5.813774,7.094405,-4.729897,-2.717019,-2.803696,0.854536,4.616452,-0.430582,9.320663,8.785698,-3.529836,1.086045,-0.940286,-8.803761,-3.516402,-0.129371,1.176913,8.791262,0.331145,-7.987811,4.623303,-1.128522,-9.527106,3.411778,-3.653892,-5.064143,-4.334076,-5.058181,7.284181,1.921858,-4.520069,-8.844128,3.882422,6.572929,9.966912,4.739634,2.962264,8.545549,-9.807732,1.612290,2.460091,-0.207884,0.256417,-0.951674,3.077767,6.957440,-8.359945,-0.940971,9.639552,-0.933573,2.986971,3.092005,5.364183,-5.816325,2.426990,-0.684409,7.792707,-1.971575,0.750868,-1.972227,7.637881,-9.064192,6.856981,5.422985,-1.137405,0.615207,7.579833,-6.150923,5.939583,1.546592,-7.316344,4.640095,-3.459237,2.636872,-0.810313,-5.110808,4.335663,5.222512,6.869946,6.334473,-1.081132,8.825664,-5.149512,-6.367327,6.973855,-5.111866,8.018858,2.389082,-1.505942,-5.060707,-0.510725,-0.323575,6.481224,-8.471335,-7.733286,7.922075,-0.122260,3.241060,-4.744619,-2.863545,0.405853,-5.909345,-3.404519,-4.464073,-0.234898,-7.480235,6.492721,-3.292116,-0.778082,-2.707090,-0.501496,-8.800961,-2.723068,6.764633,8.930670,-7.608661,0.957252,-3.150641,1.207393,-9.018857,3.002069,-8.093372,5.523233,0.351841,-0.542627,-9.117263,7.096470,5.376319,-5.719249,8.343524,7.763210,-5.322547,-9.240601,-0.492232,7.128555,7.488556,3.347962,-7.052670,-7.149279,4.611279,5.054705,1.961401,-5.721884,-0.934910,-3.261782,-0.795742,-9.006455,-3.176655,3.777732,-7.460589,4.573100,0.349840,1.016115,3.963731,-8.755009,-1.223659,-1.918287,-1.508065,6.765345,-3.097818,-3.758298,4.816300,7.506759,6.733099,-4.465510,-9.734869,5.290655,2.303112,3.887579,-3.840386,2.478792,3.418927,7.389193,-2.045710,-4.840667,-7.101069,9.845308,6.153013,7.206647,-5.972782,-8.244259,3.284466,-4.973498,5.923691,6.188806,8.814866,-6.572064,-7.536689,4.882925,-2.556631,1.398643,-2.518019,-9.946327,-5.066016,0.024235,-9.728193,8.589401,7.760006,-5.260144,4.940929,6.011998,-5.855548,0.954677,5.890907,3.765590,-8.335583,-3.611784,9.617636,6.212839,-8.158105,-1.341706,-2.457604,-0.643124,-2.982246,-4.863072,-9.457935,-4.999329,-7.070735,7.877755,-0.262308,4.682257,-1.880104,-3.989408,3.662017,6.805379,-7.751268,-4.141257,6.204209,-0.579300,7.763807,0.726619,-2.746442,-0.377188,9.613136,-0.402240,-8.849330,-1.685551,5.499293,-1.076292,-1.370475,-1.215566,-6.747362,-5.779891,1.507278,2.688306,4.947566,-5.611438,-7.974922,-9.920398,0.043118,-0.215478,9.276722,-1.633292,1.566578,5.331905,-7.201964,-5.935121,-8.893579,-3.783281,0.593676,-5.873699,-2.035282,7.177431,9.646062,-8.574736,-6.822146,-2.235303,2.191018,1.095952,4.275939,8.225363,-1.115362,-4.585695,-1.218613,4.451339,-0.691205,-7.567461,-2.360045,-0.927915,-0.118615,-6.673175,6.304880,-0.495571,6.165257,5.356094,-2.414609,-2.272592,-5.479002,6.380208,5.579836,-3.589227,-1.660209,-9.891934,-7.244309,-8.568204,7.999277,-6.381843,3.575657,-5.590540,-2.305860,4.646342], dtype = "float32")#candidate|6269|(392,)|const|float32
call_6268 = relay.TupleGetItem(func_6177_call(relay.reshape(const_6269.astype('float32'), [7, 14, 4])), 3)
call_6270 = relay.TupleGetItem(func_6180_call(relay.reshape(const_6269.astype('float32'), [7, 14, 4])), 3)
func_2168_call = mod.get_global_var('func_2168')
func_2172_call = mutated_mod.get_global_var('func_2172')
const_6277 = relay.const(-9.656667, dtype = "float32")#candidate|6277|()|const|float32
const_6278 = relay.const([[2.012142,-2.004090,0.320842,-4.753768,-1.652634,-0.433737],[6.530720,-3.211072,-1.897819,-2.068714,-1.800831,3.078921],[2.935783,9.030302,-3.911213,2.935285,8.279425,4.093017],[6.403683,4.456043,-5.474243,3.398758,5.460253,7.251610],[-1.521338,-4.450434,-5.130196,2.004144,-4.129028,7.381889],[-1.684286,-9.170873,-2.090928,-7.437258,3.125191,-8.123559],[2.060121,0.959842,7.002184,7.220395,4.371952,-2.063215],[0.854754,9.068368,-0.972865,-8.101072,1.521314,8.550505],[3.792046,1.082698,9.934091,-4.180331,-0.483364,1.068052],[-2.968357,8.477350,-3.943872,5.271427,9.456356,7.789578],[3.218053,-1.729494,-7.954671,8.190174,1.948075,-1.514632],[-4.716635,-6.403108,2.275117,-1.223696,-3.560131,6.301128],[4.806422,-7.557112,6.872772,-0.225217,4.359047,4.379410],[-2.301380,1.392692,-6.686632,-9.793896,-7.384131,8.616318],[-0.449746,-9.002958,4.516994,5.978389,-3.606373,0.030405],[6.592983,6.802026,-8.404162,-9.786869,7.807548,-6.832672],[-6.637633,-4.839717,5.694747,-6.331483,3.450719,-9.580779],[-0.945372,6.111488,2.546296,-7.483545,-9.819664,-9.961196]], dtype = "float32")#candidate|6278|(18, 6)|const|float32
call_6276 = relay.TupleGetItem(func_2168_call(relay.reshape(const_6277.astype('float32'), []), relay.reshape(const_6278.astype('float32'), [1, 9, 12]), ), 1)
call_6279 = relay.TupleGetItem(func_2172_call(relay.reshape(const_6277.astype('float32'), []), relay.reshape(const_6278.astype('float32'), [1, 9, 12]), ), 1)
func_2607_call = mod.get_global_var('func_2607')
func_2609_call = mutated_mod.get_global_var('func_2609')
call_6291 = relay.TupleGetItem(func_2607_call(), 1)
call_6292 = relay.TupleGetItem(func_2609_call(), 1)
output = relay.Tuple([uop_6258,call_6268,const_6269,call_6276,const_6277,const_6278,call_6291,])
output2 = relay.Tuple([uop_6258,call_6270,const_6269,call_6279,const_6277,const_6278,call_6292,])
func_6309 = relay.Function([var_6257,], output)
mod['func_6309'] = func_6309
mod = relay.transform.InferType()(mod)
var_6310 = relay.var("var_6310", dtype = "float32", shape = (16, 13, 12))#candidate|6310|(16, 13, 12)|var|float32
output = func_6309(var_6310)
func_6311 = relay.Function([var_6310], output)
mutated_mod['func_6311'] = func_6311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5242_call = mod.get_global_var('func_5242')
func_5243_call = mutated_mod.get_global_var('func_5243')
call_6412 = relay.TupleGetItem(func_5242_call(), 0)
call_6413 = relay.TupleGetItem(func_5243_call(), 0)
func_4214_call = mod.get_global_var('func_4214')
func_4217_call = mutated_mod.get_global_var('func_4217')
const_6417 = relay.const([5,4,3,-1,2,7,10,-6,7,9,-3,-6,-5,-8,8,-5,7,6,-3,-8,5,-8,9,5,9,-6,2,-1,2,10,-1,3,-6,-9,-10,-3,-2,-9,5,1,-9,-6,8,-9,-9,10,-6,9,6,1,2,-10,-3,9,4,-3,4,-5,7,5,-5,-7,2,2,-1,-5,-7,9,-5,-9,8,-1,3,7,9,7,8,6,-7,7,1,5,6,-7,2,-1,10,-3,7,-5,1,-2,-6,-9,7,5,8,8,-3,7,3,-8,-10,-7,10,-5,6,9,8,-6,-4,6,8,7,1,7,-4,8,-5,-10,9,-5,7,-6,4,1,-1,-3,3,10,-6,7,-9,3,-1,10,-10,-4,1,-1,2,-6,-1,1,8,7,6,1,8,-3,7,-1,-8,-4,-5,-5,-7,9,7,3,9,7,-3,-5,4,-1,9,10,7,6,8,-8,-2,4,-6,5,6,-3,4,-1,-5,-1,-4,-4,2,-2,1,7,6,-3,8,-8,-1,5,-10,-4,-1,-1,-6,8,5,10,2,1,9,-10,3,-5,-2,10,9,7,10,4,5,6,2,7,-3,1,2,3,1,10,10,-5,3,-6,-4,-9,-4,10,-10,7,-5,9,2,-3,-10,8,2,-9,-7,-7,7,9,-2,-7,-4,-8,-5,-6,-1,-1,3,-10,-3,9,-4,-9,4,-2,5,-1,-4,-9,7,7,8,8,-7,4,7,-8,-2,2,4,-4,-3,-1,-5,-7,10,2,-2,-9,9,9,-7,-5,-5,-6,-10,10,-5,-2,3,-5,-5,-1,7,8,-3,10,-5,10,-3,-8,7,8,-9,6,-2,-5,8,-6,5,-1,-10,-8,-9,4,5,4,-10,-5,3,-2,-2,1,-4,7,10,8,2,-6,4,-10,2,10,6,-10,7,-1,-1,-1,1,4,7,-3,8,7,-9,-1,-10,-2,6,-5,-6,-4,-1,3,2,-3,-1,-7,6,-1,10,6,2,-6,2,3,-10,-6,-1,-2,8,1,10,10,-9,-10,2,-1,-4,5,10,5,-7,8,-3,9,6,3,-8,-3,-4,8,-1,-2,-7,2,-9,5,9,1,6,5,2,9,1,-8,6,-2,-4,1,-3,9,9,7,-1,-2,-10,10,-7,3,10,-2,7,3,-8,3,5,-5,-7,-4,3,-5,5,9,4,-9,-3,-3,6,-4,-10,10,-10,-2,9,7,-6,-9,10,4,-9,-10,-5,-5,-3,-7,-5,-10,4,-3,-10,7,3,-8,3,6,-4,-8,-1,3,-3,7,-9,-4,1,-8,-6,-6,2,-1,-5,-8,-3,-9,3,-10,-4,6,-6,-6,8,7,-8,4,-6,-4,-1,-1,1,1,-3,10,-10,9,-7,-2,-9,-10,1,-9,-8,-9,7,3,1,2,7,-1,8,-2,7,9,-2,-6,-4,1,6,-1,3,1,-8,-9,-6,-1,-10,-9,-8,4,-1,4,-3,-7,8,-4,-2,4,-9,-6,-3,1,-1,-10,-1,8,7,5,-6,3,-10,2,3,3,-8,8,5,5,-10,-2,1,2,1,-10,-2,8,9,4,-7,3,-6,-9,10,7,-10,2,-9,1,-4,7,-1,7,-7,1,8,3,7,-4,-5,1,-10,-9,7,-8,-9,6,10,-2,-2,2,9,3,7,-6,-8,10,-10,-6,-6,-8,7,-5,-5,5,9,1,-3,3,2,2,6,8,8,-3,-8,9,2,2,2,9,5,9,-4,7,4,8,9,6,-9,4,-9,-3,-9,-10,-4,-2,9,-6,8,9,-3,3,-4,-1,-7,2,-10,-9,-2,9,10,-7,-5,-1,6,-6,-8,1,8,-5,-9,-3,2,5,10,1,7,8,1,-6,9,6,-1,-1,2,-5,5,-7,7,2,-8,-9,3,9,-7,2,9,5,-6,-10,-2,-9,-1,3,-10,7,-10,-7,4,-6,2,-6,6,4,10,2,9,1,8,9,-1,-8,-3,-5,-2,7,-8,7,-6,8,5,10,-9,-5,4,-7,-10,-5,1,-1,10,-6,-1,-4,6,-5,-2,-6,-3,-10,-4,-10,-1,9,-7,-4,6,-7,3,-6,-3,-9,-3,8,5,-10,4,-3,-9,8,1,-4,1,4,5,10,-10,-5,-5,8,2,9,10,-4,4,-6,3,4,3,8,9,-10,-9,1,-9,-6,-6,10,8,-4,5,1,-2,-3,-4,-5,-1,1,1,5,-10,-2,9,10,-5,2,-6,9,8,1,5,7,2,-7,10,2,5,4,-5,1,-1,-9,8,3,1,9,3,-1,4,5,-10,-3,10,-10,4,-4,-6,1,10,-9,-9,7,6,6,-6,3,-9,-2,4,5,-3,4,-9,-3,-1,10,-5,-4,6,9,3,9,-8,3,3,1,-5,7,-2,-3,-5,4,1,-8,-8,-9,1,-4,-9,5,3,9,-3,-1,9,7,-10,-3,-9,-8,-10,-9,-6,-3,10,-8,4,-10,-4,-3,7,-6,-2,-10,1,-9,6,3,-5,-9,-4,7,-4,4,-9,2,8,-5,-6,1,-2,8,2,-1,10,9,7,-2,4,9,-5,-1,1,-1,-2,4,-5,-3,-8,2,-6,-1,-9,-4,-9,8,5,6,9,3,-10,-7,-3,-1,-7,-8,6,-10,2,-9,8,-6,-1,1,10,3,-4,6,-1,10,-10,4,10,10,-7,-5,-10,-2,-3,-1,10,4,4,-3,5,-2,-2,10,10,5,10,-4,1,1,10,7,-6,4,-1,5,-8,8,5,3,-7,-3,-8,-7,-3,-3,10,1,-2,-6,-1,8,9,-1,-5,10,-3,-9,9,10,-4,-5,4,10,2,-9,-8,2,5,2,8,-2,-4,-9,-8,-5,3,-5,-9,-5,3,-3,2,-10,1,-5,-3,-7,9,-10,-7,7,6,-7,1,5,7,-6,-5,4,-8,2,-7,6,9,2,2,7,3,2,-7,9,7,1,-10,10,5,9,3,9,-3,9,10,3,2,-9,-6,-3,4,7,-10,-3,-8,-8,-8,-4,-7,6,1,-3,7,-3,2,6,-9,-9,-9,-3,-5,-2,7,-3,1,2,-1,6,-6,-10,5,4,2,-3,6,-10,7,3,9,8,5,3,-2,-3,10,-7,-3,8,-4,6,9,2,-9,-9,1,8,5,2,-4,8,-10,8,-7,7,-9,3,1,3,-10,-10,-10,-7,-2,4,3,10,6,7,4,5,8,-1,-5,1,-5,-4,-1,-1,9,-1,-5,6,-8,-5,6,8,-1,-5,3,2,8,4,7,4,-1,8,7,7,6,10,5,-6,-10,3,-10,3,8,-9,5,3,-8,1,-5,-1,-2,1,-2,2,-1,-5,-7,-8,8,-2,-9,-8,-5,4,-7,9,9,-5,-10,-3,3,1,-8,6,4,-8,4,4,7,1,5,3,3,-5,6,-3,7,10,-3,-1,8,-4,9,4,-7,8,-5,6,-9,-1,10,-6,10,-2,4,-1,-7,5,-2,10,3,9,-10,-6,-7,-6,2,4,9,4,3,4,-8,-6,5,10,-7,-6,6,-6,2,2,5,6,3,-5,-5,8,7,6,1,2,4,5,-3,-5,-2,-6,4,-10,2,-5,4,2,9,-5,-3,8,-6,-9,1,-1,2,1,1,-5,7,-2,5,-2,2,-5,-4,-2,6,-7,-7,2,-8,-7,4,-2,4,-2,7,-3,3,2,3,-10,-5,-5,-7,-4,-10,4,3,-5,-9,7,-2,5,-2,-5,-10,1,-3,-8,3,-5,-2,-7,2,-3,-10,9,5,-7,10,2,-8,5,-9,-10,-4,-5,4,1,-5,-9,9,7,1,-10,8,2,7,7,-10,-8,4,1,7,-3,8,-7,1,8,-8,4,-2,-3,-4,5,-9,-8,-8,8,1,-8,-5,-6,9,-8,-4,-6,-9,-5,9,-6,-3,-1,3,6,3,3,-1,2,-2,-10,3,5,4,4,10,-4,-4,3,6,-1,7,9,-2,-1,-3,3,4,-9,-7,-4,3,-1,-2,-2,6,-9,9,5,9,8,-7,-8,-10,-1,-10,-6,-10,-7,1,-1,5,4,-8,-7,-4,-6,7,-6,-1,-6,2,1,10,6,-1,10,9,-2,-2,-1,-6,-1,-3,2,4,4,-1,-7,6,2,-2,-5,-6,-7,8,7,7,4,5,-5,-3,2,-5,-5,-2,-10,9,5,-2,4,-10,-1,10,-8,-3,-1,-1,2,-4,9,-6,-2,4,-8,10,6,2,-9,-7,7,-8,-8,-3,-7,1,-5,-6,-10,4,7,-10,6,-2,-6,9,-9,-4,-10,-1,-4,-4,9,-5,10,-9,-5,-10,2,-5,-1,6,5,-8,8,3,-2,-2,7,-10,-9,4,7,-7,3,1,-10,3,8,-10,1,-8,-10,-3,-8,-6,3,4,-1,3,7,-10,-3,-2,-4,-5,6,7,-4,7,-3,-2,10,-8,-9,4,5,10,-7,-6,5,-6,-7,-10,-3,-4,7,-5,-3,7,2,-7,7,4,2,-5,-3,9,-3,-10,6,-5,3,-10,-2,8,10,2,5,-3,6,-3,10,9,-2,2,-5,3,-6,6,-1,4,2,-3,10,5,4,4,-1,-9,-2,-3,7,-8,-8,-3,-9,-4,-2,9,1,-9,1,10,6,4,-8,8,-2,10,-1,1,-1,2,-2,-7,-2,-7,-10,4,6,-6,5,-2,10,-9,7,10,4,1,-2,8,-5,-8], dtype = "int8")#candidate|6417|(1755,)|const|int8
call_6416 = relay.TupleGetItem(func_4214_call(relay.reshape(const_6417.astype('int8'), [1755,])), 2)
call_6418 = relay.TupleGetItem(func_4217_call(relay.reshape(const_6417.astype('int8'), [1755,])), 2)
func_3929_call = mod.get_global_var('func_3929')
func_3931_call = mutated_mod.get_global_var('func_3931')
call_6442 = relay.TupleGetItem(func_3929_call(), 0)
call_6443 = relay.TupleGetItem(func_3931_call(), 0)
func_4009_call = mod.get_global_var('func_4009')
func_4014_call = mutated_mod.get_global_var('func_4014')
var_6449 = relay.var("var_6449", dtype = "float64", shape = (60,))#candidate|6449|(60,)|var|float64
const_6450 = relay.const([6,-1,-2,-10,5,-7,7,6,-7,-10,-9,2,-2,7,6,9,10,2,6,1,3,-8,6,-6,6,-1,-10,4,4,10,-3,-3,-7,-7,7,4,5,-10,-5,-5,2,-3,9,-8,3,2,-7,1,9,8,-7,6,6,5,2,-10,6,-9,-3,5,-5,1,3,7,-3,8,9,2,-7,5,-6,4,-10,-4,-1,10,7,9,5,-2,3,8,1,9,8,-7,-1,-6,-5,-6,1,-4,9,-10,1,3,-1,8,-3,-2,-3,3,10,-6,2,-1,8,-3,7,3,7,-2,9,2,6,-10,3,-2,-5,-7,-10,9,-4,-7,8,-10,6,-5,1,6,3,8,-3,10,9,-6,8,7,10,2,3,-2,4,-7,-5,4,-1,6,3,4,7,-8,-7,-6,10,2,-2,6,2,-2,-6,-6,9,3,-2,-3,-8,2,8,10,-8,5,9,-5,-3,-1,-5,8,-1,-7,9,-9,-3,-2,-1,-2,9,10,-7,10,-3,-2,7,4,10,-10,3,8,2,-8,-4,-3,-8,-10,7,-8,10,9,-8,9,4,1,-1,-3,6,-8,-6,3,4,-10,3,1,5,-5,3,-5,3,4,2,7,-3,-10,5,-2,7,10,-9,7,1,9,4,-10,-1,-1,4,-4,-4,-3,-10,-8,6,-8,8,-8,-7,-4,-2,-10,-9,-7,10,1,6,2,8,2,9,8,7,-8,-5,-7,-7,2,-7,-2,-10,8,-6,1,-2,9,-5,1,-2,-6,3,6,10,9,-6,-4,-3,-2,5,-2,-6,-10,-9,3,-4,-8,2,-9,3,8,1,6,6,-3,-1,8,8,-8,-9,-6,-8,9,10,2,10,-3,-2,2,-8,9,-10,7,-4,-2,-4,7,-7,-1,8,2,-3,-6,-5,5,3,-3,10,10,-2,9,5,7,-4,-10,-4,-10,-1,-6,-5,2,-4,3,-4,9,9,4,-6,7,3,-4,-2,-8,9,1,-4,3,7,-5,9,9,-4,2,-7,-1,8,9,-8,-3,10,2,-7,5,1,5,4,7,-10,-7,8,7,-3,-6,-3,9,-4,-9,-8,-5,4,8,-7,-5,6,1,-10,-9,-5,6,-7,1,-8,2,-3,-6,8,-5,10,1,-4,9,-3,6,5,-5,-9,-4,7,4,5,-6,-3,-8,-3,-7,1,10,6,1,-10,-6,3,5,-7,9,-8,-5,-8,-1,9,-9,-8,4,4,7,-2,-2,-4,6,-7,-3,1,-3,-8,1,6,10,8,-8,-1,-6,-8,1,-7,-1,-9,-9,-2,-1,-1,-10,2,-1,-5,-3,-3,-1,-9,-3,7,-3,8,-9,6,-1,-2,-4,-2,-7,3,3,-8,7,7,8,-3,4,-4,-4,-5,-9,-7,-3,7,5,-9,6,-5,7,-4,-7,7,-10,6,-3,-2,-10,-3,-7,-3,2,1,1,2,9,6,-3,-9,4,-1,-6,7,-2,-9,3,-1,7,-3,-9,10,-1,6,-7,-10,-10,-6,-4,4,-3,4,8,1,1,-6,8,-10,10,6,-1,-8,7,-1,9,8,-10,-10,-10,-6,6,3,7,5,-9,7,-7,-3,1,7,9,3,-8,10,5,-10,7,7,9,1,4,8,-3,8,-4,5,8,5,-5,5,2,-3,1,2,5,-9,-3,2,7,1,3,-7,8,-1,8,2,-3,10,8,-5,-9,-2,1,-8,2,-2,-7,-9,2,5,6,-3,-6,-3,6,5,-2,6,9,-2,3,-9,6,3,-8,9,10,10,-4,8,3,-5,-2,-8,5,3,5,-8,10,8,-2,9,-8,5,4,-4,-1,-1,10,-4,-9,-4,-9,-5,2,6,-10,-5,7,-2,5,7,-5,-7,-6,-1,-7,9,-7,-6,8,4,-10,8,-9,8,8,-10,-4,9,7,6,7,4,2,5,-4,7,6,-3,10,8,9,-3,4,-6,4,-7,-9,-6,-10,8,10,10,-3,-10,4,-10,-6,7,-5,-1,5,3,-10,3,-2,4,8,-9,-8,-5,6,5,-8,-2,-5,5,2,2,-9,-1,-7,4,-10,-6,1,-1,7,-1,-10,2,-7,-5,-5,2,-3], dtype = "uint8")#candidate|6450|(780,)|const|uint8
var_6451 = relay.var("var_6451", dtype = "int32", shape = (847,))#candidate|6451|(847,)|var|int32
call_6448 = relay.TupleGetItem(func_4009_call(relay.reshape(var_6449.astype('float64'), [60,]), relay.reshape(const_6450.astype('uint8'), [780,]), relay.reshape(var_6451.astype('int32'), [847,]), ), 6)
call_6452 = relay.TupleGetItem(func_4014_call(relay.reshape(var_6449.astype('float64'), [60,]), relay.reshape(const_6450.astype('uint8'), [780,]), relay.reshape(var_6451.astype('int32'), [847,]), ), 6)
output = relay.Tuple([call_6412,call_6416,const_6417,call_6442,call_6448,var_6449,const_6450,var_6451,])
output2 = relay.Tuple([call_6413,call_6418,const_6417,call_6443,call_6452,var_6449,const_6450,var_6451,])
func_6460 = relay.Function([var_6449,var_6451,], output)
mod['func_6460'] = func_6460
mod = relay.transform.InferType()(mod)
var_6461 = relay.var("var_6461", dtype = "float64", shape = (60,))#candidate|6461|(60,)|var|float64
var_6462 = relay.var("var_6462", dtype = "int32", shape = (847,))#candidate|6462|(847,)|var|int32
output = func_6460(var_6461,var_6462,)
func_6463 = relay.Function([var_6461,var_6462,], output)
mutated_mod['func_6463'] = func_6463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_6469 = relay.TupleGetItem(func_2881_call(), 0)
call_6470 = relay.TupleGetItem(func_2883_call(), 0)
func_3884_call = mod.get_global_var('func_3884')
func_3886_call = mutated_mod.get_global_var('func_3886')
call_6472 = func_3884_call()
call_6473 = func_3884_call()
func_5437_call = mod.get_global_var('func_5437')
func_5439_call = mutated_mod.get_global_var('func_5439')
var_6488 = relay.var("var_6488", dtype = "int32", shape = (847,))#candidate|6488|(847,)|var|int32
call_6487 = relay.TupleGetItem(func_5437_call(relay.reshape(var_6488.astype('int32'), [847, 1])), 2)
call_6489 = relay.TupleGetItem(func_5439_call(relay.reshape(var_6488.astype('int32'), [847, 1])), 2)
func_6125_call = mod.get_global_var('func_6125')
func_6127_call = mutated_mod.get_global_var('func_6127')
call_6495 = relay.TupleGetItem(func_6125_call(), 0)
call_6496 = relay.TupleGetItem(func_6127_call(), 0)
output = relay.Tuple([call_6469,call_6472,call_6487,var_6488,call_6495,])
output2 = relay.Tuple([call_6470,call_6473,call_6489,var_6488,call_6496,])
func_6503 = relay.Function([var_6488,], output)
mod['func_6503'] = func_6503
mod = relay.transform.InferType()(mod)
var_6504 = relay.var("var_6504", dtype = "int32", shape = (847,))#candidate|6504|(847,)|var|int32
output = func_6503(var_6504)
func_6505 = relay.Function([var_6504], output)
mutated_mod['func_6505'] = func_6505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_6594 = relay.TupleGetItem(func_988_call(), 0)
call_6595 = relay.TupleGetItem(func_990_call(), 0)
output = call_6594
output2 = call_6595
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
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_6638 = func_6597_call()
call_6639 = func_6597_call()
output = call_6638
output2 = call_6639
func_6640 = relay.Function([], output)
mod['func_6640'] = func_6640
mod = relay.transform.InferType()(mod)
mutated_mod['func_6640'] = func_6640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6640_call = mutated_mod.get_global_var('func_6640')
call_6641 = func_6640_call()
output = call_6641
func_6642 = relay.Function([], output)
mutated_mod['func_6642'] = func_6642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5781_call = mod.get_global_var('func_5781')
func_5782_call = mutated_mod.get_global_var('func_5782')
call_6660 = relay.TupleGetItem(func_5781_call(), 0)
call_6661 = relay.TupleGetItem(func_5782_call(), 0)
uop_6666 = relay.log2(call_6660.astype('float64')) # shape=(10, 3, 13)
uop_6668 = relay.log2(call_6661.astype('float64')) # shape=(10, 3, 13)
output = relay.Tuple([uop_6666,])
output2 = relay.Tuple([uop_6668,])
func_6671 = relay.Function([], output)
mod['func_6671'] = func_6671
mod = relay.transform.InferType()(mod)
mutated_mod['func_6671'] = func_6671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6671_call = mutated_mod.get_global_var('func_6671')
call_6672 = func_6671_call()
output = call_6672
func_6673 = relay.Function([], output)
mutated_mod['func_6673'] = func_6673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1749_call = mod.get_global_var('func_1749')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_6688 = func_1749_call()
call_6689 = func_1749_call()
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_6738 = func_4758_call()
call_6739 = func_4758_call()
func_2049_call = mod.get_global_var('func_2049')
func_2051_call = mutated_mod.get_global_var('func_2051')
call_6746 = relay.TupleGetItem(func_2049_call(), 0)
call_6747 = relay.TupleGetItem(func_2051_call(), 0)
func_2468_call = mod.get_global_var('func_2468')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_6768 = relay.TupleGetItem(func_2468_call(), 0)
call_6769 = relay.TupleGetItem(func_2469_call(), 0)
output = relay.Tuple([call_6688,call_6738,call_6746,call_6768,])
output2 = relay.Tuple([call_6689,call_6739,call_6747,call_6769,])
func_6802 = relay.Function([], output)
mod['func_6802'] = func_6802
mod = relay.transform.InferType()(mod)
mutated_mod['func_6802'] = func_6802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mutated_mod.get_global_var('func_6802')
call_6803 = func_6802_call()
output = call_6803
func_6804 = relay.Function([], output)
mutated_mod['func_6804'] = func_6804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4462_call = mod.get_global_var('func_4462')
func_4464_call = mutated_mod.get_global_var('func_4464')
call_6891 = func_4462_call()
call_6892 = func_4462_call()
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_6915 = relay.TupleGetItem(func_1822_call(), 0)
call_6916 = relay.TupleGetItem(func_1824_call(), 0)
func_4862_call = mod.get_global_var('func_4862')
func_4863_call = mutated_mod.get_global_var('func_4863')
call_6923 = func_4862_call()
call_6924 = func_4862_call()
output = relay.Tuple([call_6891,call_6915,call_6923,])
output2 = relay.Tuple([call_6892,call_6916,call_6924,])
func_6939 = relay.Function([], output)
mod['func_6939'] = func_6939
mod = relay.transform.InferType()(mod)
output = func_6939()
func_6940 = relay.Function([], output)
mutated_mod['func_6940'] = func_6940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5279_call = mod.get_global_var('func_5279')
func_5280_call = mutated_mod.get_global_var('func_5280')
call_7020 = func_5279_call()
call_7021 = func_5279_call()
func_4009_call = mod.get_global_var('func_4009')
func_4014_call = mutated_mod.get_global_var('func_4014')
var_7049 = relay.var("var_7049", dtype = "float64", shape = (60,))#candidate|7049|(60,)|var|float64
var_7050 = relay.var("var_7050", dtype = "uint8", shape = (780,))#candidate|7050|(780,)|var|uint8
var_7051 = relay.var("var_7051", dtype = "int32", shape = (847,))#candidate|7051|(847,)|var|int32
call_7048 = relay.TupleGetItem(func_4009_call(relay.reshape(var_7049.astype('float64'), [60,]), relay.reshape(var_7050.astype('uint8'), [780,]), relay.reshape(var_7051.astype('int32'), [847,]), ), 7)
call_7052 = relay.TupleGetItem(func_4014_call(relay.reshape(var_7049.astype('float64'), [60,]), relay.reshape(var_7050.astype('uint8'), [780,]), relay.reshape(var_7051.astype('int32'), [847,]), ), 7)
func_4428_call = mod.get_global_var('func_4428')
func_4430_call = mutated_mod.get_global_var('func_4430')
var_7060 = relay.var("var_7060", dtype = "uint8", shape = (3900,))#candidate|7060|(3900,)|var|uint8
call_7059 = relay.TupleGetItem(func_4428_call(relay.reshape(var_7060.astype('uint8'), [1950, 2])), 0)
call_7061 = relay.TupleGetItem(func_4430_call(relay.reshape(var_7060.astype('uint8'), [1950, 2])), 0)
uop_7062 = relay.sin(var_7051.astype('float32')) # shape=(847,)
var_7064 = relay.var("var_7064", dtype = "float32", shape = (847,))#candidate|7064|(847,)|var|float32
bop_7065 = relay.add(uop_7062.astype('float64'), relay.reshape(var_7064.astype('float64'), relay.shape_of(uop_7062))) # shape=(847,)
uop_7068 = relay.sqrt(uop_7062.astype('float64')) # shape=(847,)
output = relay.Tuple([call_7020,call_7048,var_7049,var_7050,call_7059,var_7060,bop_7065,uop_7068,])
output2 = relay.Tuple([call_7021,call_7052,var_7049,var_7050,call_7061,var_7060,bop_7065,uop_7068,])
func_7077 = relay.Function([var_7049,var_7050,var_7051,var_7060,var_7064,], output)
mod['func_7077'] = func_7077
mod = relay.transform.InferType()(mod)
mutated_mod['func_7077'] = func_7077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7077_call = mutated_mod.get_global_var('func_7077')
var_7079 = relay.var("var_7079", dtype = "float64", shape = (60,))#candidate|7079|(60,)|var|float64
var_7080 = relay.var("var_7080", dtype = "uint8", shape = (780,))#candidate|7080|(780,)|var|uint8
var_7081 = relay.var("var_7081", dtype = "int32", shape = (847,))#candidate|7081|(847,)|var|int32
var_7082 = relay.var("var_7082", dtype = "uint8", shape = (3900,))#candidate|7082|(3900,)|var|uint8
var_7083 = relay.var("var_7083", dtype = "float32", shape = (847,))#candidate|7083|(847,)|var|float32
call_7078 = func_7077_call(var_7079,var_7080,var_7081,var_7082,var_7083,)
output = call_7078
func_7084 = relay.Function([var_7079,var_7080,var_7081,var_7082,var_7083,], output)
mutated_mod['func_7084'] = func_7084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2468_call = mod.get_global_var('func_2468')
func_2469_call = mutated_mod.get_global_var('func_2469')
call_7092 = relay.TupleGetItem(func_2468_call(), 0)
call_7093 = relay.TupleGetItem(func_2469_call(), 0)
func_1553_call = mod.get_global_var('func_1553')
func_1556_call = mutated_mod.get_global_var('func_1556')
const_7123 = relay.const([-2,4,7,5,5,7,-3,-9,-2,10,-10,-2,-8,-3,9,-6,9,6,2,-7,1,10,-3,-10,-9,8,-3,-4,-5,5,-2,-2,2,7,3,-3,-8,-10,-4,-3,3,6,2,-8,-6,-10,5,-1,3,-3,2,1,-10,10,-3,9,-4,3,-5,-6,3,3,-9,-7,2,7,5,-7,-10,1,10,1,-6,-4,5,-4,-6,-6,-1,7,2,-1,-5,4,-5,-9,6,3,-2,3,-8,6,5,-1,7,-4,-6,-8,3,-4,-8,7,3,-3,8,-4,4,10,-4,-8,1,-1,-6,5,2,10,-4,-3,-7,-4,4,-1,10,10,4,-4,-7,-1,-6,4,8,8,-1,1,-7,6,4,2,1,-7,-7,4,-8,8,-3,-1,-6,-5,10,-8,-4,2,2,-2,-5,1,-10,9,10,-1,10,4,-1,-3,-8,9,5,-9,-5,-9,-8,4,5,-5,9,-6,9,4,-10,2,10,-9,5,2,-7,-10,-3,-4,-8,-1,-6,-7,-6,5,-10,5,10,-6,10,-5,-9,3,-9,-10,5,-3,6,-7,1,-2,1,-2,9,-4,-6,-7,3,-8,-6,-1,-10,3,-4,-2,-2,-9,-10,-4,1,-2,-8,-5,-9,-5,-3,-8,-1,-9,-3,2,-5,-10,4,-6,3,-3,6,-4,-2,2,3,6,-4,9,-8,-3,-3,-8,9,1,1,-5,-1,4,5,-7,-9,-2,-2,8,-5,-10,8,-3,-3,10,-8,3,-1,-3,6,-7,-6,5,2,-7,6,5,-7,-10,-5,-6,-3,-4,-7,-3,8,-5,-10,4,4,1,9,4,4,-6,-4,2,1,-6,-3,-1,-8,9,7,-2,-3,2,6,-7,2,9,-8,-5,-7,7,-9,-4,5,7,-5,4,1,-1,2,7,-3,-9,-7,10,-7,-5,7,7,3,3,-4,-7,3,-10,-5,-6,-3,-9,-1,-4,8,-7,9,7,8,9,7,5,-1,4,3,-4,6,9,-2,6,-4,-5,6,2,-3,4,-6,-1,-7,5,-4,-8,-2,-10,2,6,-10,9,-4,10,2,9,-6,-7,5,2,-2,-2,9,-1,-9,-7,10,6,8,3,-1,-10,-3,9,10,7,-2,-6,-2,-2,-6,1,6,3,-5,-4,9,3,-2,9,-4,5,7,6,10,10,8,3,-1,8,3,4,7,-5,2,2,-10,1,-8,-7,-5,-6,2,-9,-6,-1,-10,-2,-2,9,-10,-9,9,10,-5,8,5,4,-3,-10,-9,-7,-4,9,5,10,-8,8,9,7,-6,-5,-10,8,-10,-2,9,-10,-10,1,-7,-3,-1,4,-10,3,7,8,-7,-1,-7,7,-2,-9,8,-8,-4,-1,3,-5,8,10,8,-5,6,-3,8,-7,9,-3,-9,-3,3,7,1,10,4,7,9,8,-7,-6,-10,-5,2,-7,8,-3,-4,-4,4,6,-3,-1,-4,-8,9,6,-9,-10,7,-2,-7,-6,7,8,6,-3,-7,-3,-1,-4,5,10,8,-4,7,-2,5,7,-9,-5,-1,4,-3,8,8,-4,1,8,4,-8,10,-5,-7,-6,9,1,-2,-7,2,10,-9,-4,8,10,3,-3,10,-7,2,5,-9,-1,-1,-7,-4,-4,1,3,-9,-3,3,-5,-4,9,-10,-7,-1,3,7,-7,-8,3,-1,9,9,10,8,2,10,9,-6,-10,-7,10,-2,4,-10,-9,1,-8,-2,2,-6,5,8,5,-4,-2,7,-4,9,-10,3,9,-9,-4,-7,-4,-1,-8,-3,-2,9,8,5,6,-8,-4,-6,-6,-2,-10,5,10,1,4,3,2,9,8,10,8,10,10,5,-3,-6,-5,-6,-8,5,2,-7,9,-2,10,1,-3,-1,9,9,-2,6,8,4,-9,-10,-6,3,5,-10,-9,-4,-4,-5,1,-6,3,-2,-1,8,5,1,7,5,-1,-10,10,3,8,-6,4,-4,1,7,-4,4,-5,1,2,5,-4,4,-8,5,-6,7,-2,-6,-10,-7,-10,-4,-9,-8,-10,2,9,-6,-4,-4,-4,10,-3,1,3,-8,10,-9,-6,9,9,9,-9,4,-10,4,1,-1,2,8,9,-10,9,-7,-6,10,-8,-5,4,8,10,-9,8,5,-10,-7,10,-8,-9,-3,-1,-4,2,4,1,-1,8,1,-7,-7,-9,8,4,-10,10,1,6,10,7,3,8,8,-3,-1,3,-9,-2,4,2,-10,5,6,9,7,-10,1,-6,5,7,-10,-3,5,-8,3,2,4], dtype = "int32")#candidate|7123|(847,)|const|int32
call_7122 = relay.TupleGetItem(func_1553_call(relay.reshape(const_7123.astype('int32'), [77, 11]), relay.reshape(const_7123.astype('float32'), [77, 11]), ), 6)
call_7124 = relay.TupleGetItem(func_1556_call(relay.reshape(const_7123.astype('int32'), [77, 11]), relay.reshape(const_7123.astype('float32'), [77, 11]), ), 6)
func_1553_call = mod.get_global_var('func_1553')
func_1556_call = mutated_mod.get_global_var('func_1556')
call_7146 = relay.TupleGetItem(func_1553_call(relay.reshape(const_7123.astype('int32'), [77, 11]), relay.reshape(const_7123.astype('float32'), [77, 11]), ), 1)
call_7147 = relay.TupleGetItem(func_1556_call(relay.reshape(const_7123.astype('int32'), [77, 11]), relay.reshape(const_7123.astype('float32'), [77, 11]), ), 1)
func_4743_call = mod.get_global_var('func_4743')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_7151 = relay.TupleGetItem(func_4743_call(), 0)
call_7152 = relay.TupleGetItem(func_4745_call(), 0)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_7153 = relay.TupleGetItem(func_1931_call(), 4)
call_7154 = relay.TupleGetItem(func_1933_call(), 4)
func_3884_call = mod.get_global_var('func_3884')
func_3886_call = mutated_mod.get_global_var('func_3886')
call_7174 = func_3884_call()
call_7175 = func_3884_call()
output = relay.Tuple([call_7092,call_7122,const_7123,call_7146,call_7151,call_7153,call_7174,])
output2 = relay.Tuple([call_7093,call_7124,const_7123,call_7147,call_7152,call_7154,call_7175,])
func_7178 = relay.Function([], output)
mod['func_7178'] = func_7178
mod = relay.transform.InferType()(mod)
mutated_mod['func_7178'] = func_7178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7178_call = mutated_mod.get_global_var('func_7178')
call_7179 = func_7178_call()
output = call_7179
func_7180 = relay.Function([], output)
mutated_mod['func_7180'] = func_7180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_7181 = func_4758_call()
call_7182 = func_4758_call()
func_2954_call = mod.get_global_var('func_2954')
func_2956_call = mutated_mod.get_global_var('func_2956')
const_7191 = relay.const([7,-1,-2,-5,6,8,1,-8,-7,5,-8,4,-4,-3,8,-7,6,7,10,2,-7,-1,-10,-1,3,-1,-8,6,-6,7,3,-2,-3,-8,-1,8,1,-6,10,10,-3,6,-7,-7,1,10,7,4,-1,2,-5,1,10,6,7,3,8,3,-2,-10,-4,9,-2,-1,5,6,4,5,7,5,-9,5,-10,3,-1,-6,-5,6,6,-4,-9,-3,10,-8,-1,-2,-1,-6,-7,2,-3,-3,-1,-10,6,-2,-4,9,-4,2,10,-4,1,4,2,-8,-4,5,-1,6,1,-4,2,-9,-10,2,5,3,-9,-5,-2,-5,-5,-4,7,6,8,3,1,6,6,-3,5,8,4,-2,10,3,-10,-4,6,7,7,-4,5,-4,-10,-2,5,-9,-5,5,10,1,-6,-1,4,-8,9,1,-4,4,2,-10,-8,-7,-2,8,-2,-4,-5,-5,-2,-2,-5,-6,8,2,6,10,-1,-6,-9,4,5,-2,-2,1,-7,6,6,2,10,5,-6,-9,-1,-1,-9,-2,3,-7,10,-1,-1,-1,-7,-10,-7,-4,-9,3,7,-10,6,-1,5,-6,-5,4,-3,2,7,8,6,-8,-4,7,-4,-8,-9,1,-6,-1,-3,-7,-9,6,-1,-2,8,-4,-3,-4,7,9,-10,2,-7,-4,-9,9,-10,-7,-1,7,-1,4,3,-10,9,-6,10,-4,4,-1,1,-2,7,1,8,-9,-1,2,-10,-4,-4,9,-2,-4,3,1,5,6,-5,-2,-6,-2,4,3,-6,3,1,5,7,2,-3,5,-6,-2,7,-4,4,4,-9,2,-7,-7,-10,-2,2,-8,-6,-6,3,5,-3,5,-4,7,-9,3,5,4,4,4,-1,2,-3,-2,-6,6,-4,9,3,5,7,8,8,9,2,-8,4,-10,8,-3,7,-4,-4,2,8,-9,-5,-7,3,-5,-9,-5,4,-8,-7,7,-2,-8,-5,-4,-10,-10,-2,-8,-2,7,9,-4,9,-5,5,-4,-4,-3,-5,-4,10,9,-10,6,-1,5,8,5,1,8,2,3,4,-5,-3,-5,-2,8,1,-3,-8,6,-6,-5,-1,-3,5,-10,-3,10,-3,-2,9,-6,3,-7,-8,9,2,-2,-7,5,-2,10,10,-3,7,10,5,-8,-5,-1,8,6,-4,-4,-5,2,5,-5,4,-10,5,-6,-7,-1,1,-5,2,8,10,-8,2,2,-3,-2,7,9,5,-2,-2,-3,7,-10,9,-6,2,6,5,1,7,7,9,-5,1,-5,2,-4,5,-9,-3,-5,-8,-1,1,3,7,-1,5,-9,5,9,-1,8,10,2,2,-10,-10,-3,3,8,-5,-6,-7,9,10,-1,5,-1,-5,-8,-2,-7,-9,3,8,4,2,-8,-7,-1,4,-10,-1,4,3,5,10,8,-4,-3,-6,-10,7,9,2,2,2,-7,-2,1,2,-1,-7,2,-3,4,2,-8,-1,-4,7,-10,-8,3,9,5,9,-4,6,8,10,7,-5,2,3,10,10,10,9,7,-9,-1,-8,-5,-10,-4,-4,-4,-7,6,10,2,5,9,-7,-4,-1,-7,10,5,-4,2,-1,8,3,-10,9,5,1,-2,4,-7,10,6,-7,-2,4,-2,2,-3,-5,8,-4,-1,-8,-5,8,-7,-7,10,8,6,8,4,-7,5,-1,-7,-5,-10,-9,5,-9,8,7,-2,4,6,-6,-1,9,-7,8,-5,-2,6,-2,-1,-5,-8,8,9,8,3,-8,-6,-2,-9,-5,-5,-3,-10,-4,-7,1,5,-5,-1,-2,4,-3,-6,3,7,-2,-7,-3,-10,-8,-8,-2,8,9,-8,-8,-8,-5,5,-2,6,-5,6,9,-7,-1,-6,9,-10,-5,-9,3,3,-4,3,-3,9,-5,-5,1,3,-8,6,-5,8,-5,1,4,3,2,-5,9,2,1,8,1,3,-10,-9,-5,5,1,7,1,7,-8,-10,-8,-10,-2,-8,-2,2,-2,-9,5,-9,1,4,-4,5,5,10,8,2,-8,2,-3,-2,-5,-4,-4,-7,-6,6,5,-3,-7,-4,3,-6,4,1,-2,4,5,-8,-8,-3,-9,6,10,-4,2,-3,-2,6,-9,-5,3,8,5,8,-4,-10,9,7,-3,8,9,-10,2,-6,6,-2,3,6,10,3,-4,9,7,7,-6,-9,8,-5,7,3,-5,2,-9,-5,-2,-2,-1,2,-6,-2,-5,9,-10,6,-8,-1,-6,-10,-1,3,-5,-2,6,6,4,-6,1,-2,10,8,-7,-10,6,-7,6,2,6,8,7,-4,6,-10,5,-7,8,-4,8,9,3,1,-7,-9,-5,5,-2,5,-10,4,4,4,-7,-10,-10,7,6,-3,10,-8,-10,9,5,-2,8,2,-7,8,5,-9,7,-10,-5,-8,4,2,-10,-8,6,9,5,-7,-2,-6,-3,1,2,-2,2,-4,7,-2,4,1,-7,-5,6,5,-7,2,-6,9,-6,-7,-1,7,-4,5,7,9,8,8,-5,1,-2,1,8,5,1,2,-10,9,8,-3,10,2,-3,-2,-1,-10,6,10,1,7,9,3,-10,3,-6,6,-8,2,7,10,6,3,-1,-5,-2,6,2,1,2,2,2,-4,4,-2,9,-3,3,-5,10,-9,-2,4,-6,8,8,-6,7,1,-5,4,-4,-8,-2,-3,3,-7,-1,-1,-3,-3,-8,-3,8,-8,-4,6,1,9,7,8,-6,-6,-5,1,5,-2,4,8,7,4,10,3,4,-7,-4,2,1,6,-7,5,-3,-5,-10,1,-10,-1,7,-4,-4,3,-5,7,-4,-3,1,3,4,-3,2,4,-10,-2,8,9,6,-1,10,-6,-2,5,6,-7,7,-7,-5,1,-5,-4,1,-9,9,8,8,4,-5,-3,-9,3,2,5,10,-5,-10,-2,-6,10,10,3,-5,8,-5,3,3,2,-8,7,4,5,-2,-7,-7,-4,-6,-5,-3,1,5,-6,1,-8,-4,7,4,1,8,-4,6,9,6,-3,8,9,-7,4,2,7,4,3,7,-5,4,9,9,4,-4,4,-10,-5,-9,-4,-8,6,-6,-9,-5,-7,6,-10,6,10,-10,3,-9,-6,-5,9,3,5,-6,-4,9,-1,9,-1,5,8,6,-7,8,-3,-4,-8,8,10,-10,-5,8,-5,7,-4,5,-2,-3,-6,-2,8,1,-5,-9,-3,9,-7,3,-6,8,-7,-3,-6,7,9,-10,5,3,10,-5,3,10,3,-6,6,-10,-6,1,9,-5,5,-7,9,-10,-6,-2,3,2,9,-6,9,9,6,9,-10,-6,-2,-7,5,-1,-4,-9,-7,4,9,1,5,5,-2,9,-1,-6,9,7,1,-4,-1,4,6,-3,10,-2,6,8,-2,-9,-5,-9,8,-8,-1,4,7,-1,-7,-5,10,2,5,-5,1,3,9,-2,-7,6,3,2,-7,3,7,1,-7,5,-6,-8,-2,-5,-2,-8,7,9,-3,2,-5,-5,4,2,-2,-3,7,7,6,-2,7,9,3,4,10,7,-2,10,10,-9,-8,1,8,7,-10,-2,9,10,1,8,-3,-9,-7,3,10,10,-8,5,8,10,1,6,-3,-1,-4,6,-2,-2,-3,-8,9,-2,8,-1,-1,8,-4,1,-1,-4,9,-10,-6,-4,9,1,-10,3,2,6,-6,5,-9,7,-9,4,-2,1,-9,6,-6,4,-2,4,2,7,-6,-7,-9,2,-7,7,1,7,2,-7,-2,4,1,-10,-10,10,1,9,-6,-9,-7,4,4,-9,-7,-7,-1,-3,-9,-3,1,-2,-5,-4,4,-3,2,1,1,2,-8,6,-10,-2,-3,-7,-10,-9,-2,7,-8,6,-10,-6,9,-10,7,-8,7,7,5,-6,-6,4,-8,5,1,-6,10,-3,-9,10,9,4,-8,-5,8,-1,-6,4,6,-2,1,-10,-9,4,8,-6,1,-2,-5,-5,-8,-7,1,-10,1,4,9,6,8,8,3,-2,5,5,-3,-3,7,7,3,3,-9,-9,10,8,3,-6,1,-1,4,-6,-8,-9,-1,1,6,-10,-10,5,2,1,-9,-2,-5,-7,-10,-5,2,-1,10,6,7,-1,5,-8,9,-2,6,-1,8,-9,10,7,10,6,-2,-8,-8,-8,6,10,7,8,-8,4,8,6,-9,-2,3,-1,-10,-7,-7,-1,-3,10,5,-5,6,2,-5,2,1,5,1,2,6,-10,-4,-5,2,-7,3,3,-3,1,-1,-4,-6,10,-6,9,-2,4,-9,-1,6,1,1,-9,7,2,3,-2,-6,6,-5,-5,-7,-2,-2,9,-2,9,4,-2,6,-9,-2,7,5,2,-2,8,-8,6,-3,9,-7,3,-4,2,-8,10,6,-8,5,-3,-6,6,1,-5,-1,2,-3,-1,9,-9,-8,5,-10,-5,2,10,10,6,-10,-6,3,10,2,-3,7,-5,4,-9,4,7,-3,-8,5,-4,2,9,-7,-3,10,-9,-1,4,-8,-8,-10,-10,6,-5,9,7,9,-9,4,-7,-8,-5,-3,-4,5,-3,1,-5,-1,-7,2,-4,-1,-9,-4,1,-3,3,-7,-8,1,5,-7,6,-5,-10,6,-7,-6,-1,-3,2,-1,3,-2,-2,6,-2,10,-3,-10,1,9,-2,-4,-5,7,4,-2,10,10,6,9,-1,5,-5,10,-8,6,4,-5,9,-6,-2,10,2,-1,-7,6,1,-5,6,-6,2,6,-4,-5,-3,-5,-7,6,-4,10,9,-1,-7,9,-10,8,7,-10,-5,5,5,-2,3,-4,4,10,7,-6,-6,6,1,1,-7,2,-5,-9,-5,3,-8,-6,-8,-8,8,1,-2,-3,2,5,-5,1,-2,-8,-9,8,7,-2,10,4,-5,-5,4,9,2,-5,-1,-4,-7,3,-5,-5,-4,-9,-6,-6,10,7,-9,-9,-2,-5,3,9,6,-9,-2,-3,-1,1,-9,-10,8,2,6,6,6,-5,5,-10,-6,9,-3,-2,-9,4,2,7,-3,-7,10,1,9,4,9,-2,-3,3,-7,2,10,6,-2,-1,-1,8,-4,-9,4,-4,9,8,-10,8,5,-3,-8,8,3,-6,10,8,-2,8,10,9,-9,-1,-7,6,1,-1,-10,8,10,10,6,5,-4,-4,-6,-6,-1,4,10,-3,9,1,-3,-3,-2,3,10,8,3,-10,6,-4,5,-6,-7,-5,1,6,-4,6,-1,-4,9,4,-3,-10,10,-7,-1,-9,9,5,-9,-5,9,9,-2,-10,6,-2,-8,-9,6,3,-6,-6,-6,9,1,10,-7,7,-3,-10,-10,-7,5,-7,1,-10,2,-6,-6,-8,10,6,-7,7,-1,7,9,10,-2,-9,-6,-2,5,-1,-2,10,6,-9,1,3,1,1,-5,-6,-9,2,3,6,-1,-1,-5,-4,8,-4,-9,9,6,-2,3,8,2,-7,-5,3,1,10,6,7,-7,-3,7,-8,3,1,-5,-10,-10,-2,-10,-10,10,9,4,-1,6,-9,7,-5,7,-8,7,-1,-5,-4,9,-7,6,8,1,-2,5,-1,3,5,-2,-4,1,7,-10,2,-9,-10,-7,6,8,-7,1,7,2,4,5,4,-5,3,-6,-5,-7,9,-1,-4,-2,4,-8,9,-3,5,-3,7,10,1,6,-10,-1,7,-3,-3,-1,-2,7,9,6,-9,3,-7,5,-8,6,-6,-6,-8,-3,5,7,-2,-9,-6,7,6,-3,-2,2,1,-9,-4,-9,5,3,-7,9,5,-4,-5,-8,10,5,-10,-3,5,-8,-6,-1,-1,3,3,7,10,-10,-2,-5,10,6,4,-10,3,8,-5,2,-3,1,-5,-5,2,7,4,8,-1,-3,-6,-6,9,8,-4,9,5,5,-2,2,-8,10,2,-5,6,10,8,-1,-1,-2,-1,-4,3,-4,-2,9,-7,1,10,-2,3,-6,-7,10,8,-7,-3,5,2,10,-8,-3,9,4,-1,4,8,5,-1,-7,8,-7,-3,-8,-4,9,9,-4,-6,-8,7,-1,5,2,2,4,1,5,-6,9,1,-9,-1,-1,-3,6,-2,-5,-4,3,-4,7,8,1,5,1,9,-8,-5,7,-7,-10,-9,-6,-1,10,5,3,7,5,-4,-10,8,-3,-5,3,-7,-3,-7,1,7,5,7,5,-2,8,9,-10,5,2,-8,-4,-7,1,-3,3,-4,-1,-8,6,9,9,3,-4,7,-8,2,-9,-6,-4,5,-2,10,9,-2,-2,-3,6,2,-2,-8,1,-4,-1,-3,1,4,6,-9,-4,1,9,-4,-10,8,3,-4,-8,-7,9,1,9,-5,1,-9,2,-8,-6,7,1,7,3,-10,-2,-7,-10,-4,6,-1,3,10,10,8,2,-1,3,7,-3,-7,6,7,2,3,1,5,-4,1,4,-1,9,7,1,-9,1,-1,-8,4,-10,-10,-3,-6,1,-2,-9,9,-6,-1,10,-3,-4,1,3,-5,-2,-5,-9,1,-10,-5,9,-8,-2,-6,-7,-7,-3,6,-2,10,-6,-1,8,7,7,9,-7,3,-6,-4,-7,-5,-9,-10,-1,-7,7,-10,-1,3,10,-4,-8,6,5,6,-3,4,-3,-5,5,9,-1,7,7,-10,1,-4,2,-3,-2,-8,-4,-8,-7,9,-8,-1,9,-3,-7,3,-8,9,7,-6,4,5,-6,-5,6,4,4,5,5,-10,-10,2,-10,-7,-4,-5,4,-6,-2,5,5,-4,-5,2,8,2,-5,-5,5,1,4,6,7,-10,3,9,-3,4,-3,-9,8,-8,-8,-7,6,2,5,7,2,-3,3,10,6,-7,2,-9,-7,-3,-1,-8,10,6,-8,9,2,-4,3,-2,-1,9,5,4,-6,-9,-9,5,-6,7,6,5,-8,-5,-4,2,-8,-9,-9,-6,-1,-4,-1,10,-2,3,-2,7,1,1,-9,-3,3,9,-6,-7,-8,-9,-9,-8,7,8,4,-9,7,2,-2,2,-6,7,4,1,4,2,-1,6,-2,7,-2,-10,-6,-5,-5,6,-8,7,7,-3,-10,-6,-5,-8,7,-2,-4,7,5,10,9,-5,-9,6,-10,6,-5,-2,-5,9,8,10,-4,-1,9,10,7,2,8,1,8,-8,2,-5,-10,10,6,9,-8,-10,2,-4,5,-5,5,-1,-5,-8,-10,-5,-7,-10,4,-2,2,1,2,-4,-1,-10,-7,1,-1,-1,4,-3,1,-4,5,-9,-10,2,6,-8,3,5,-10,-3,9,-4,-10,-6,4,-5,-7,-5,-5,-8,-3,7,-6,-7,1,1,-4,3,-6,2,-10,-7,3,6,1,6,2,-9,8,-9,5,-8,-5,-2,1,-10,-3,2,1,4,3,7,5,-6,-3,1,4,-7,-2,1,3,6,8,-3,-5,-2,-7,6,4,-7,8,5,7,3,10,-3,-5,10,7,4,-10,-2,7,1,1,-10,-5,-3,6,-2,-9,-1,1,2,7,-2,4,6,-4,-3,-4,-6,-8,1,-4,-2,7,-1,-9,8,9,-2,6,2,-4,6,8,9,2,1,5,1,1,10,-5,5,-10,4,-3,-7,3,-7,7,8,5,7,7,2,10,-7,2,-6,6,-10,8,8,-3,4,-8,-1,-6,-5,-6,10,-8,-8,6,5,-4,3,-2,-5,5,-7,4,7,6,-2,8,-6,-8,7,8,5,6,-6,-6,-3,10,5,-8,5,-4,-8,-8,7,1,-9,-5,-3,-10,-9,-9,9,-4,5,-7,-8,7,1,2,-3,-3,4,-7,-1,5,5,-4,-5,-1,2,9,8,8,3,-7,-3,-9,10,-5,2,1,-3,-6,-5,9,4,7,-5,-1,-3,5,1,-4,-7,-2,-8,-8,9,-1,10,2,-7,-6,-2,-1,5,2,7,7,-6,4,-1,6,6,-4,7,-8,3,-9,1,1,-5,2,-10,9,-7,1,-5,7,4,6,5,10,-8,-4,-10,-6,7,-10,-6,-4,-9,-10,2,6,9,1,-5,-4,1,-3,3,7,-7,1,-5,-10,-2,1,-8,-3,-8,-10,5,-8,-2,-7,-2,6,-1,-7,-4,1,7,-9,8,1,6,10,7,-8,-3,-5,9,-6,-10,7,8,-9,9,-2,-10,4,4,7,-4,-2,8,-1,3,-7,8,7,1,3,-4,8,7,9,-6,5,-1,-6,-6,-6,-4,-2,-7,10,-6,10,9,-5,-8,10,-3,5,-5,3,-9,2,5,6,4,-2,1,4,7,-8,6,-2,-6,4,-9,-3,-9,-2,9,-6,5,7,9,-8,1,-3,6,9,-4,3,10,-2,3,3,1,8,7,-4,5,3,9,-6,-3,9,5,-1,-10,-6,-8,-6,8,6,7,2,-1,-1,-2,5,9,-5,8,1,-2,2,8,8,9,-1,-2,-2,9,3,-8,1,4,4,-3,-9,-4,2,8,7,-3,-8,3,-8,-3,8,-7,1,-4,-3,-9,-3,-5,4,6,-3,-2,-2,10,1,-10,5,5,-9,2,-9,6,6,6,5,1,-1,-8,10,-4,9,8,-1,1,-6,-4,4,5,-1,9,-5,1,-5,-10,7,6,7,-2,-10,10,8,1,4,-1,8,-1,2,8,3,4,3,-7,-5,9,-4,3,3,-3,1,1,5,2,-6,-5,-10,8,-9,4,-2,3,-1,7,2,10,3,3,-3,-5,9,7,-9,3,-8,3,-9,7,5,-4,3,10,-5,-5,-10,-7,-2,-8,-9,-10,9,8,-2,-8,10,-3,3,-2,8,9,10,7,-2,5,-8,-10,-8,7,-5,8,6,-8,-7,-9,8,5,4,9,8,9,9,-5,8,-9,-6,6,-2,-2,5,-6,-9,-10,-2,1,3,6,-9,-10,-2,10,8,9,-2,-1,-2,9,-9,-8,-8,-10,1,4,8,7,-3,-5,6,-2,-5,-5,-3,2,-3,-2,-9,3,-10,-8,-1,8,5,-6,7,9,-5,3,-9,8,3,-7,4,-10,9,3,-4,-5,-4,2,-2,-5,5,5,-1,10,-4,-6,-6,-1,6,-4,-4,-1,-9,10,-4,-8,-3,7,-7,9,1,-8,-4,2,4,10,5,4,6,7,9,1,10,7,4,-9,-3,-3,-7,-7,-1,8,-2,-1,-6,-10,-4,6,-8,9,1,8,6,-3,6,-3,10,-4,4,1,-4,5,-2,9,-6,-4,10,-10,-3,7,-4,-10,-2,7,10,5,8,1,3,-10,2,-3,-7,-7,8,4,4,8,-8,3,-2,-3,10,-2,6,1,7,-8,-9,-7,-9,-10,-4,-3,5,2,6,-10,9,-1,-4,-3,-6,-5,6,-1,2,-9,2,-9,-8,4,8,2,6,2,-4,2,6,5,1,6,-1,-10,-5,-10,9,6,-10,5,-10,7,-4,7,6,1,-10,-1,-1,4,9,8,-9,-5,3,-6,-1,-8,-2,4,-7,-7,3,9,-8,-10,6,7,2,-6,-4,-7,-5,-9,-10,-7,1,5,2,7,-7,-7,7,-10,-5,-4,-1,3,6,7,6,-6,-7,-10,4,-7,6,-6,7,2,6,-3,6,5,10,1,-5,5,-9,9,4,-6,1,5,-10,1,2,-3,10,2,9,7,10,5,7,-3,-1,3,-3,-1,-3,8,-8,6,10,-7,-1,2,6,-1,1,-4,-4,-4,5,-1,10,6,2,-6,-7,-9,9,10,-9,8,8,2,-9,1,2,2,1,9,-7,-4,-10,-5,-6,-4,-7,-7,-2,-6,-3,-5,-7,8,7,1,-2,10,-8,1,-9,1,7,10,-6,2,-3,6,-6,-10,-2,8,-6,8,-3,-1,5,-8,-1,2,5,7,-1,-10,9,-1,-10,5,-7,-1,-3,3,-4,10,9,3,6,-4,4,7,5,-4,-4,5,3,2,-8,-6,3,-10,-10,10,4,6,-9,3,8,3,6,5,-3,9,-1,-6,3,-9,-8,10,5,1,-6,10,-2,9,-10,-1,-1,-4,3,9,5,-8,8,-6,3,-9,-2,6,3,-3,-10,-5,3,3,9,-4,1,1,2,-2,-5,-8,1,2,-9,-6,1,10,-1,2,7,8,9,-7,5,6,2,10,7,-7,8,5,-5,5,-10,-7,4,4,5,2,3,-1,-3,-10,4,9,3,3,-1,-3,7,5,-5,5,-2,-1,7,2,4,4,-3,10,-9,1,5,-10,-6,-4,-5,3,5,4,6,4,10,-6,1,9,2,3,-4,8,9,10,-10,-3,7,-7,-3,-2,8,-8,-5,2,-6,5,-7,1,6,10,-6,-2,-2,5,9,10,5,-10,-6,-10,-7,-2,9,-10,5,-2,5,-6,-3,2,-8,1,4,-6,6,-3,-2,-7,10,-3,-9,8,8,-1,-4,-3,9,8,7,-2,-1,-6,-1,1,2,6,10,7,7,9], dtype = "uint8")#candidate|7191|(3900,)|const|uint8
call_7190 = relay.TupleGetItem(func_2954_call(relay.reshape(const_7191.astype('uint8'), [780, 5])), 0)
call_7192 = relay.TupleGetItem(func_2956_call(relay.reshape(const_7191.astype('uint8'), [780, 5])), 0)
output = relay.Tuple([call_7181,call_7190,const_7191,])
output2 = relay.Tuple([call_7182,call_7192,const_7191,])
func_7194 = relay.Function([], output)
mod['func_7194'] = func_7194
mod = relay.transform.InferType()(mod)
mutated_mod['func_7194'] = func_7194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7194_call = mutated_mod.get_global_var('func_7194')
call_7195 = func_7194_call()
output = call_7195
func_7196 = relay.Function([], output)
mutated_mod['func_7196'] = func_7196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5178_call = mod.get_global_var('func_5178')
func_5179_call = mutated_mod.get_global_var('func_5179')
call_7203 = relay.TupleGetItem(func_5178_call(), 0)
call_7204 = relay.TupleGetItem(func_5179_call(), 0)
output = relay.Tuple([call_7203,])
output2 = relay.Tuple([call_7204,])
func_7205 = relay.Function([], output)
mod['func_7205'] = func_7205
mod = relay.transform.InferType()(mod)
mutated_mod['func_7205'] = func_7205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7205_call = mutated_mod.get_global_var('func_7205')
call_7206 = func_7205_call()
output = call_7206
func_7207 = relay.Function([], output)
mutated_mod['func_7207'] = func_7207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7208 = relay.var("var_7208", dtype = "int16", shape = (1, 15, 15))#candidate|7208|(1, 15, 15)|var|int16
const_7209 = relay.const([[[7,-9,-10,3,-10,4,2,6,10,-7,-9,4,1,7,9],[-9,4,1,-8,-4,3,6,1,-1,7,3,8,-1,-7,6],[8,4,5,8,10,-4,9,10,-1,2,1,-4,-3,2,5],[5,5,-5,-5,-6,4,-1,1,2,-4,-9,-10,-6,2,-10],[-5,-10,6,-1,-10,-9,-8,-7,4,10,-4,3,-4,4,8],[-2,-2,-3,10,1,-10,2,3,-4,9,-4,-3,-6,7,-2],[7,-8,-8,7,-3,-8,1,1,-9,10,9,2,1,10,9],[3,-7,3,9,3,-10,-7,1,6,2,-10,2,-6,10,-2],[-9,-3,5,-2,-5,8,-4,-6,-2,-4,10,7,6,4,-9],[-2,-1,-5,-10,3,-1,-1,-8,1,1,4,1,-3,5,2],[-6,-4,-1,7,7,-9,3,-7,-8,2,-4,-3,10,-2,7],[-10,-10,2,-3,-3,1,1,3,-6,6,2,-6,5,-3,2],[-4,-5,-7,6,-7,2,-2,-1,-3,-5,9,-9,4,-3,-4],[9,9,2,2,-8,8,7,5,4,9,6,-9,-2,-10,2],[-2,-10,6,9,-10,6,-6,-10,3,10,-5,7,-3,9,-8]]], dtype = "int16")#candidate|7209|(1, 15, 15)|const|int16
bop_7210 = relay.not_equal(var_7208.astype('bool'), relay.reshape(const_7209.astype('bool'), relay.shape_of(var_7208))) # shape=(1, 15, 15)
bop_7214 = relay.less(var_7208.astype('bool'), relay.reshape(const_7209.astype('bool'), relay.shape_of(var_7208))) # shape=(1, 15, 15)
func_2321_call = mod.get_global_var('func_2321')
func_2324_call = mutated_mod.get_global_var('func_2324')
const_7219 = relay.const([[5.020127,0.165589,9.077644,-3.281605,7.116000,2.149986,7.815330,-6.714817,-6.335542,7.455399,-6.234218,8.509562,4.356014,7.947758,6.257182,-9.794417,-4.463194,-2.158096,6.245446,-4.467977,-0.459892,1.824087,-5.011320,-6.449455,-2.046399,-5.606459,0.881817,8.070351,-7.240304,6.857041,8.980493,-4.904684,8.475480,-1.459561,-1.328877,6.201700,-0.477588,-6.104617,-4.953498,7.330471,9.563165,4.636949,-2.039984,2.465859,2.399710,-6.724633,-2.794208,-1.549955,-4.134823,-5.388687,0.495072,5.736680,-0.344880,9.045238,-7.584241,-8.123230,-0.330984,0.498876,-6.440523,-1.640567,5.364194,1.293754,9.651173,4.583634,-2.854730,-8.207693,0.210247,2.887694,-3.404658,-1.255775,-5.831764,-0.809081,-1.764963,8.061338,-4.552003,-2.013292,-6.955500,6.916701,3.047581,6.090751,5.296029,6.594069,1.703403,-4.567470,7.081964,0.422129,3.921393,2.221273,6.706081,0.857082,-0.528596,4.726388,0.710238,-9.006045,0.419460,-9.881568,-3.602488,0.597071,-9.095122,2.869762,-3.048246,1.510216,-5.309614,8.822731,9.736620,8.079126,-4.616744,2.659603,5.300334,-4.659064,8.959174,5.758982,-2.553707,-1.625404,2.154246,4.313308,-6.897752,1.573614,5.048369,-6.924526,5.643824,-8.880437,-5.184630,2.399268,9.127560,-7.756999,-3.218737,-4.950516,-1.439088,-7.523624,-4.781697,3.397611,-3.296376,2.920872,9.178554,0.091850,9.755602,-0.909726,1.250090,-5.580399,0.358358,1.275201,-0.881256,-4.578735,-2.368999,-0.216921,-0.790416,9.522528,7.797539,-8.607584,-1.985723,6.418568,2.395475,8.003821,-7.223955,-6.100227,-9.705140,8.407371,0.695496,8.908072,-0.138100,7.276920,6.695838,-8.464309,9.719275,7.395990,-9.129800,-7.405124,-3.743999,-6.501724,5.061440,-7.983491,-0.521405,-5.330554,-5.518398,-2.509536,-2.390308,7.876977,-7.145018,-0.123529,3.366147,-6.455629,-5.592082,1.887218,-0.773855,3.900911,-9.831278,-6.850066,-5.016282,6.290687,-4.905994,6.473223,5.781088,2.934728,-7.947660,9.325172,0.552146,2.374359,-6.766715,4.626863,-3.923811,-4.167332,-9.467961,-2.774954,-1.927014,5.795605,7.657581,6.283928,-7.383536,-5.074575,-1.139239,-8.869300,5.118023,3.309728,-7.848103,1.778183,-6.167578,-6.144766,-0.287507,5.862130,-1.096544,0.532019,4.506211,-5.413444,7.594429,0.836051,-7.759121,-0.401517,8.779412,-7.870524,-7.500571,8.259231,2.427281,0.619903,-2.973402,-7.704158,-1.150837,-3.604749,-5.775081,2.698805,1.810640,9.081796,-7.227889,-7.090711,-4.249105,6.111748,-8.376984,9.710731,-1.310431,8.749908,0.139517,4.927498,0.835962,9.447884,-4.850735,-3.673771,6.520191,-0.054521,9.599042,-1.160901,2.844250,-3.369372,-4.426714,1.121641,-5.725314,6.371003,6.482761,9.197437,-1.405128,-9.812351,2.451961,-1.491295,0.522738,-5.633555,5.927456,-1.607273,9.835420,-9.885692,-9.129231,-2.769800,-8.622656,-0.788291,5.543564,1.009975,-3.300831,-6.783556,-1.875718,6.424070,3.752648,-1.812672,-9.226143,5.426177,9.290014,9.172113,-0.309287,-5.171662,4.889813,-5.686013,6.991740,-9.102347,8.580593,5.770666,9.635966,8.122499,8.108937,-0.301731,-2.679840,8.922287,3.109164,5.913226,-3.052920,8.695886,-8.376594,-2.324780,0.095126,-9.226559,-4.470862,-1.953052,-9.524757,-4.433384,5.357121,7.511751,2.077995,3.592081,4.327484,-6.954268,-1.240457,9.344724,7.926013,-3.833068,-5.017949,4.765167,7.072999,-2.602601,-9.675808,8.698505,2.873049,3.012927,6.960541,-6.535043,-1.939465,-3.813503,-7.043955,7.406917,-7.914903,-7.371913,-7.301703,9.026571,7.547250,1.481608,-4.649865,8.166977,2.824609,-3.259788,1.563914,0.501378,4.499089,-3.203882,1.700100,0.535790,-8.291418,-8.795432,-8.324190,-5.506479,-9.904635,3.868025,-0.230384,-9.894239,5.444874,-1.661368,8.615563,-9.044662,2.533626,-9.151515,4.241589,-1.327402,5.062301,-1.355618,-5.238397,3.242257,4.747614,-9.709387,3.017180,3.834239,6.553528,7.318672,-1.623157,-0.350982,0.243946,-9.825229,-3.834302,-7.626451,-8.851415,9.638858,6.780200,8.302061,7.623556,-3.086915,-4.476971,-1.352968,3.894581,7.043981,2.946903,4.825243,-3.813985,1.683334,9.828435,7.275301,3.973014,-5.580350,4.610874,6.013657,9.043608,-9.013561,5.879866,-1.456460,-9.333988,-3.816183,5.455128,-2.862317,-3.768697,-2.289774,4.356084,1.644936,5.686802,1.301054,5.519364,7.522735,-3.979935,-5.804458,-9.325854,-8.280332,-8.591291,2.620100,8.385578,-8.407780,4.833130,4.150143,-7.885651,4.924073,-4.081715,-2.580250,5.803532,9.077987,2.548583,-8.819219,-5.763490,5.841918,4.970881,-9.368044,-3.648725,-8.890872,3.645641,9.644963,-2.743379,4.932785,0.616080,-9.530495,-4.036515,5.872405,-4.544159,3.695657,-6.521374,6.523848,5.260484,-4.574971,-1.901911,-7.084783,-4.302939,0.255605,-8.541347,-4.610947,2.499778,7.981127,-9.466445,6.710149,-1.963119,5.206920,2.153540,-6.819101,-2.105047,9.241106,-8.780224,-8.266410,2.767405,2.467412,4.425832,7.392323,6.240207,-5.849339,4.070728,-8.931992,-2.814266,0.876833,-0.873481,4.672526,-4.104414,-5.443984,-9.060612,-3.983635,-9.987267,5.418913,6.968069,-3.508558,2.909970,-0.648042,5.722877,-3.426389,-7.560218,3.936814,-3.216132,4.596278,2.443212,2.811907,-4.900555,3.296513,0.384270,-8.033645,-6.497213,8.601685,5.436259,-8.062684,-2.386949,7.874586,-9.736701,-0.360395,4.290171,-1.936714,5.261423,-8.298070,6.906827,-4.167174,-0.333827,0.805394,-5.708433,2.279098,-0.012574,-0.555580,-2.528556,4.581843,-2.897076,4.023193,2.392184,9.103614,6.277881,-5.684966,8.821753,-7.146177,-8.414784,-2.885365,-2.963911,-3.846809,-5.331016,-0.627931,-2.767794,6.261235,6.597854,-0.580787,-8.705252,8.430751,5.188360,-9.309661,-3.669265,0.979842,-7.491094,0.306962,3.218075,6.903909,-4.457965,-7.119960,5.364735,-2.893022,6.169937,6.211873,-1.154715,4.356760,5.889797,-0.506136,-1.448125,-1.848796,-4.382019,-5.664695,6.899195,9.793294,3.903517,0.211266,6.368340,0.552397,-1.652051,9.173950,9.764584,6.261484,-9.645211,-2.422381,0.637596,-1.803088,6.122101,5.555826,-0.165346,-6.690523,-2.439674,9.377872,6.798916,-0.998066,2.242213,-2.802865,2.995859,3.802314,-2.619057,-7.421664,-7.355889,1.189742,6.927556,3.146676,8.945194,9.458937,7.450400,8.057699,8.057419,-9.650238,4.281870,9.384836,-6.239344,9.378932,4.333153,-9.364479,-5.051308,3.445185,-0.690187,1.459344,-9.192634,-0.016028,7.433584,8.367765,7.555088,-6.208653,-1.334312,7.588741,-3.054100,5.973268,9.403271,-9.497893,1.224680,7.732857,-9.181346,5.684099,-1.226529,-2.186844,-4.929269,-5.806701,2.296035,-1.417799,1.593968,8.462514,-4.182648,3.346840,-5.776953,5.319798,7.744656,-9.589670]], dtype = "float64")#candidate|7219|(1, 660)|const|float64
call_7218 = relay.TupleGetItem(func_2321_call(relay.reshape(const_7219.astype('float64'), [11, 12, 5])), 3)
call_7220 = relay.TupleGetItem(func_2324_call(relay.reshape(const_7219.astype('float64'), [11, 12, 5])), 3)
output = relay.Tuple([bop_7210,bop_7214,call_7218,const_7219,])
output2 = relay.Tuple([bop_7210,bop_7214,call_7220,const_7219,])
func_7222 = relay.Function([var_7208,], output)
mod['func_7222'] = func_7222
mod = relay.transform.InferType()(mod)
mutated_mod['func_7222'] = func_7222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7223 = relay.var("var_7223", dtype = "int16", shape = (1, 15, 15))#candidate|7223|(1, 15, 15)|var|int16
func_7222_call = mutated_mod.get_global_var('func_7222')
call_7224 = func_7222_call(var_7223)
output = call_7224
func_7225 = relay.Function([var_7223], output)
mutated_mod['func_7225'] = func_7225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_7232 = relay.TupleGetItem(func_4386_call(), 1)
call_7233 = relay.TupleGetItem(func_4388_call(), 1)
func_1279_call = mod.get_global_var('func_1279')
func_1282_call = mutated_mod.get_global_var('func_1282')
call_7234 = relay.TupleGetItem(func_1279_call(relay.reshape(call_7232.astype('float32'), [7, 14, 4])), 2)
call_7235 = relay.TupleGetItem(func_1282_call(relay.reshape(call_7232.astype('float32'), [7, 14, 4])), 2)
uop_7247 = relay.atanh(call_7232.astype('float64')) # shape=(7, 14, 4)
uop_7249 = relay.atanh(call_7233.astype('float64')) # shape=(7, 14, 4)
func_2263_call = mod.get_global_var('func_2263')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_7250 = func_2263_call()
call_7251 = func_2263_call()
func_2168_call = mod.get_global_var('func_2168')
func_2172_call = mutated_mod.get_global_var('func_2172')
var_7268 = relay.var("var_7268", dtype = "float32", shape = ())#candidate|7268|()|var|float32
var_7269 = relay.var("var_7269", dtype = "float32", shape = (108,))#candidate|7269|(108,)|var|float32
call_7267 = relay.TupleGetItem(func_2168_call(relay.reshape(var_7268.astype('float32'), []), relay.reshape(var_7269.astype('float32'), [1, 9, 12]), ), 0)
call_7270 = relay.TupleGetItem(func_2172_call(relay.reshape(var_7268.astype('float32'), []), relay.reshape(var_7269.astype('float32'), [1, 9, 12]), ), 0)
func_2247_call = mod.get_global_var('func_2247')
func_2250_call = mutated_mod.get_global_var('func_2250')
call_7292 = relay.TupleGetItem(func_2247_call(relay.reshape(call_7234.astype('int32'), [847,])), 0)
call_7293 = relay.TupleGetItem(func_2250_call(relay.reshape(call_7234.astype('int32'), [847,])), 0)
func_2379_call = mod.get_global_var('func_2379')
func_2381_call = mutated_mod.get_global_var('func_2381')
call_7306 = relay.TupleGetItem(func_2379_call(), 2)
call_7307 = relay.TupleGetItem(func_2381_call(), 2)
output = relay.Tuple([call_7234,uop_7247,call_7250,call_7267,var_7268,var_7269,call_7292,call_7306,])
output2 = relay.Tuple([call_7235,uop_7249,call_7251,call_7270,var_7268,var_7269,call_7293,call_7307,])
func_7312 = relay.Function([var_7268,var_7269,], output)
mod['func_7312'] = func_7312
mod = relay.transform.InferType()(mod)
var_7313 = relay.var("var_7313", dtype = "float32", shape = ())#candidate|7313|()|var|float32
var_7314 = relay.var("var_7314", dtype = "float32", shape = (108,))#candidate|7314|(108,)|var|float32
output = func_7312(var_7313,var_7314,)
func_7315 = relay.Function([var_7313,var_7314,], output)
mutated_mod['func_7315'] = func_7315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3884_call = mod.get_global_var('func_3884')
func_3886_call = mutated_mod.get_global_var('func_3886')
call_7325 = func_3884_call()
call_7326 = func_3884_call()
func_6177_call = mod.get_global_var('func_6177')
func_6180_call = mutated_mod.get_global_var('func_6180')
call_7329 = relay.TupleGetItem(func_6177_call(relay.reshape(call_7325.astype('float32'), [7, 14, 4])), 4)
call_7330 = relay.TupleGetItem(func_6180_call(relay.reshape(call_7325.astype('float32'), [7, 14, 4])), 4)
func_5242_call = mod.get_global_var('func_5242')
func_5243_call = mutated_mod.get_global_var('func_5243')
call_7365 = relay.TupleGetItem(func_5242_call(), 0)
call_7366 = relay.TupleGetItem(func_5243_call(), 0)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_7368 = func_1322_call()
call_7369 = func_1322_call()
func_7077_call = mod.get_global_var('func_7077')
func_7084_call = mutated_mod.get_global_var('func_7084')
var_7376 = relay.var("var_7376", dtype = "float64", shape = (60,))#candidate|7376|(60,)|var|float64
const_7377 = relay.const([[10],[4],[-8],[-7],[8],[9],[-6],[5],[10],[-4],[6],[3],[5],[4],[5],[-2],[3],[5],[6],[-6],[1],[-8],[-4],[4],[-6],[4],[2],[-5],[-7],[-8],[6],[7],[8],[9],[-5],[-10],[2],[7],[3],[-2],[8],[3],[5],[-7],[-9],[-7],[7],[-2],[-8],[-8],[-10],[1],[-6],[-10],[10],[2],[-9],[-7],[2],[-7],[1],[6],[7],[-10],[1],[-10],[-6],[-2],[1],[-5],[-5],[-8],[1],[1],[1],[6],[1],[9],[-2],[-7],[-9],[-3],[-9],[-9],[-9],[1],[9],[-2],[-5],[6],[10],[-8],[-4],[1],[8],[-8],[-4],[-1],[-9],[3],[-3],[4],[4],[-4],[9],[-6],[2],[10],[-3],[-3],[-10],[7],[5],[8],[8],[-2],[8],[5],[-1],[10],[9],[-1],[-2],[-10],[-3],[-5],[5],[8],[1],[3],[-7],[-8],[-10],[6],[2],[-3],[4],[5],[-4],[-10],[-7],[1],[-6],[-3],[5],[6],[-9],[-9],[-7],[-2],[3],[-1],[9],[4],[10],[-4],[6],[10],[-6],[-10],[-9],[5],[1],[8],[-10],[-1],[6],[-3],[-8],[2],[-8],[7],[-2],[9],[10],[-1],[8],[-6],[3],[-8],[-4],[10],[-3],[-7],[-10],[10],[-7],[-4],[-6],[9],[4],[4],[7],[10],[-5],[2],[9],[1],[5],[-2],[-9],[2],[1],[-5],[1],[-2],[3],[7],[-9],[-7],[-9],[-4],[-1],[10],[-5],[10],[9],[9],[10],[-5],[-7],[5],[5],[7],[1],[8],[7],[8],[-7],[3],[-5],[7],[6],[1],[8],[-6],[5],[5],[3],[3],[10],[-4],[3],[2],[-10],[-3],[1],[-8],[4],[1],[-7],[8],[-8],[1],[-7],[-7],[-4],[-1],[-3],[-9],[1],[10],[10],[6],[-7],[-9],[-6],[6],[10],[-5],[-2],[3],[3],[4],[-10],[-1],[-5],[-10],[8],[2],[-5],[-10],[5],[-4],[5],[-3],[4],[-4],[-1],[-3],[3],[9],[-4],[4],[9],[5],[-6],[6],[3],[6],[1],[-5],[-7],[-2],[-1],[-7],[-8],[4],[-9],[3],[-6],[-3],[-5],[2],[9],[6],[-1],[-5],[-3],[-5],[1],[-9],[-2],[2],[-3],[9],[-3],[-10],[1],[6],[3],[-2],[-6],[3],[3],[4],[-1],[4],[5],[-5],[8],[8],[8],[10],[3],[3],[-10],[10],[-3],[7],[-2],[1],[-3],[-7],[10],[-7],[-9],[10],[4],[-1],[7],[-4],[-9],[5],[9],[10],[-1],[5],[8],[2],[-5],[6],[5],[-3],[7],[-7],[6],[-3],[8],[-8],[10],[-6],[-1],[-4],[-2],[-6],[-9],[-3],[10],[7],[-10],[4],[-8],[2],[5],[-10],[-2],[-5],[-9],[1],[-9],[-10],[-9],[5],[9],[-9],[-6],[4],[9],[7],[9],[-10],[-6],[-3],[8],[-6],[-1],[5],[9],[9],[2],[6],[10],[10],[-9],[-5],[6],[9],[-10],[9],[-10],[-5],[3],[-1],[2],[10],[-10],[9],[-8],[1],[-6],[6],[-2],[6],[-9],[2],[-1],[-2],[-8],[7],[-5],[-1],[-5],[6],[9],[-9],[-6],[9],[-9],[-3],[-3],[10],[3],[8],[-5],[1],[-4],[-6],[3],[2],[-1],[-9],[3],[-6],[6],[-3],[-4],[2],[-6],[-9],[7],[-2],[2],[-2],[10],[-9],[3],[8],[9],[-10],[-3],[3],[-7],[5],[3],[-4],[-5],[3],[-4],[4],[-7],[5],[-4],[-7],[6],[7],[2],[9],[3],[5],[-9],[10],[5],[3],[8],[-3],[4],[-6],[2],[-1],[-3],[-10],[-10],[-4],[-4],[-3],[-8],[-6],[6],[-2],[9],[-1],[5],[1],[-3],[8],[3],[-8],[-8],[6],[-1],[-4],[1],[4],[1],[6],[-1],[-3],[6],[-6],[6],[-2],[-3],[-2],[5],[2],[8],[-9],[-5],[-10],[6],[8],[-3],[-8],[7],[-6],[7],[4],[2],[-10],[5],[-7],[7],[5],[6],[10],[-1],[1],[-1],[3],[-2],[-3],[-8],[-8],[2],[-9],[7],[9],[9],[-6],[9],[-7],[6],[2],[-7],[-7],[5],[8],[6],[6],[-2],[-4],[-1],[3],[-7],[5],[6],[-4],[-1],[2],[-3],[-7],[-1],[-2],[8],[7],[-2],[-1],[4],[-5],[4],[4],[-1],[4],[7],[10],[-7],[10],[1],[-8],[-9],[3],[4],[8],[-7],[-8],[10],[-2],[-2],[-5],[-2],[-1],[-1],[8],[-3],[4],[-1],[-5],[8],[-4],[4],[-7],[6],[7],[6],[7],[6],[-9],[-8],[-10],[-5],[-3],[1],[3],[3],[6],[1],[-6],[-3],[-3],[5],[-6],[-9],[-10],[2],[-8],[-4],[3],[-10],[5],[-4],[-3],[-4],[-2],[-1],[5],[6],[-9],[-4],[3],[-8],[-3],[3],[10],[-10],[9],[5],[1],[-2],[-6],[9],[-1],[3],[-1],[10],[3],[7],[2],[1],[5],[6],[7],[7],[-3],[-2],[-4],[-2],[-7],[8],[2],[-4],[-5],[2],[-2],[7],[4],[3],[-7],[1],[1],[-8],[-4],[1],[-5],[-1],[-4],[3],[-7],[7],[8],[9],[9],[5],[-2],[5],[2],[10],[6],[-7],[-8],[-10],[-5],[-4],[-10],[4],[-4],[1],[-4],[-1],[-5],[-2],[10],[4],[3],[6],[2],[-6],[1],[-9],[-10],[10],[-3],[9],[-9],[8],[7],[-2],[-3],[-4],[10]], dtype = "uint8")#candidate|7377|(780, 1)|const|uint8
var_7378 = relay.var("var_7378", dtype = "int32", shape = (847,))#candidate|7378|(847,)|var|int32
var_7379 = relay.var("var_7379", dtype = "uint8", shape = (3900,))#candidate|7379|(3900,)|var|uint8
call_7375 = relay.TupleGetItem(func_7077_call(relay.reshape(var_7376.astype('float64'), [60,]), relay.reshape(const_7377.astype('uint8'), [780,]), relay.reshape(var_7378.astype('int32'), [847,]), relay.reshape(var_7379.astype('uint8'), [3900,]), relay.reshape(var_7378.astype('float32'), [847,]), ), 0)
call_7380 = relay.TupleGetItem(func_7084_call(relay.reshape(var_7376.astype('float64'), [60,]), relay.reshape(const_7377.astype('uint8'), [780,]), relay.reshape(var_7378.astype('int32'), [847,]), relay.reshape(var_7379.astype('uint8'), [3900,]), relay.reshape(var_7378.astype('float32'), [847,]), ), 0)
func_5122_call = mod.get_global_var('func_5122')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_7392 = func_5122_call()
call_7393 = func_5122_call()
output = relay.Tuple([call_7325,call_7329,call_7365,call_7368,call_7375,var_7376,const_7377,var_7378,var_7379,call_7392,])
output2 = relay.Tuple([call_7326,call_7330,call_7366,call_7369,call_7380,var_7376,const_7377,var_7378,var_7379,call_7393,])
func_7394 = relay.Function([var_7376,var_7378,var_7379,], output)
mod['func_7394'] = func_7394
mod = relay.transform.InferType()(mod)
mutated_mod['func_7394'] = func_7394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7394_call = mutated_mod.get_global_var('func_7394')
var_7396 = relay.var("var_7396", dtype = "float64", shape = (60,))#candidate|7396|(60,)|var|float64
var_7397 = relay.var("var_7397", dtype = "int32", shape = (847,))#candidate|7397|(847,)|var|int32
var_7398 = relay.var("var_7398", dtype = "uint8", shape = (3900,))#candidate|7398|(3900,)|var|uint8
call_7395 = func_7394_call(var_7396,var_7397,var_7398,)
output = call_7395
func_7399 = relay.Function([var_7396,var_7397,var_7398,], output)
mutated_mod['func_7399'] = func_7399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4975_call = mod.get_global_var('func_4975')
func_4977_call = mutated_mod.get_global_var('func_4977')
call_7431 = relay.TupleGetItem(func_4975_call(), 0)
call_7432 = relay.TupleGetItem(func_4977_call(), 0)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_7440 = relay.TupleGetItem(func_988_call(), 0)
call_7441 = relay.TupleGetItem(func_990_call(), 0)
output = relay.Tuple([call_7431,call_7440,])
output2 = relay.Tuple([call_7432,call_7441,])
func_7442 = relay.Function([], output)
mod['func_7442'] = func_7442
mod = relay.transform.InferType()(mod)
output = func_7442()
func_7443 = relay.Function([], output)
mutated_mod['func_7443'] = func_7443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2607_call = mod.get_global_var('func_2607')
func_2609_call = mutated_mod.get_global_var('func_2609')
call_7447 = relay.TupleGetItem(func_2607_call(), 2)
call_7448 = relay.TupleGetItem(func_2609_call(), 2)
func_1303_call = mod.get_global_var('func_1303')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_7459 = relay.TupleGetItem(func_1303_call(), 0)
call_7460 = relay.TupleGetItem(func_1304_call(), 0)
func_931_call = mod.get_global_var('func_931')
func_934_call = mutated_mod.get_global_var('func_934')
const_7464 = relay.const([7,4,-4,8,-1,8,2,-8,3,6,8,10,-3,7,-6,-7,8,3,-8,10,1,-3,-4,-7,-5,-5,-2,8,4,3,-6,4,-4,5,-5,1,5,-9,7,5,9,-4,5,-10,7,-10,4,6,1,9,-8,-2,-6,-1,-6,-6,6,-8,2,-3,-9,-4,9,10,3,3,-10,4,5,1,-4,8,7,-5,2,-9,-3,4,3,9,5,-9,9,3,3,-7,10,-8,-9,-5,-1,4,9,5,3,-10,-5,3,4,-10,-9,3,2,6,4,-4,8,-8,-5,-9,-6,5,9,5,-6,-10,4,6,-5,-7,4,2,9,-8,-3,-3,5,-10,7,-8,2,8,3,2,-6,5,-2,1,8,-8,-6,2,8,-6,9,8,3,-9,-9,4,-2,5,-7,5,-6,10,3,-3,-4,-8,6,6,3,8,6,9,-1,2,-3,-7,2,-10,1,-10,6,-10,5,2,1,1,-1,5,-7,4,-6,8,2,4,3,8,1,2,2,-5,-5,10,9,2,2,5,-10,-5,10,4,5,-5,-10,4,4,-6,-8,-8,4,2,-7,6,-9,-8,2,4,-3,-4,9,-4,-7,-3,7,-1,-1,-6,9,6,3,-9,-5,10,6,-1,-2,-8,-5,4,-2,2,-8,-4,10,-7,5,8,2,7,4,3,-3,6,3,10,5,-3,-10,-3,8,-3,-7,2,-3,-7,9,2,2,1,-8,-3,5,-7,2,5,-2,-2,1,8,4,-10,7,8,2,7,2,-4,-7,-2,-2,10,7,-5,-5,-2,-10,4,6,1,1,9,-9,10,5,4,9,3,5,6,-1,-8,1,-10,-4,-7,8,-8,-9,4,10,-3,-1,7,-4,-5,1,8,7,-1,1,-6,3,8,2,-8,-10,-1,9,7,1,10,9,-4,-8,-9,-4,-9,-1,-1,-1,-3,-1,-1,2,-4,4,-5,-4,1,-5,-10,-5,7,8,-7,8,9,6,-10,10,1,1,-6,4,-6,8,-7,-7,-9,2,-3,9,10,1,-4,-7,4,-9,-3,-10,10,-7,10,-1,10,-8,4,6,-3,-7,10,9,1,6,3,-5,1,1,-9,-2,-6,3,-8,-3,5,-5,3,1,-4,-10,-3,1,10,-7,4,7,10,7,10,-8,-1,2,-8,8,7,10,-6,4,-3,-6,-2,7,4,9,-6,-8,1,1,-2,3,8,9,-4,-3,-8,6,-1,-2,-4,10,10,-7,10,8,6,1,-5,-1,7,-8,10,-5,-6,9,-7,-2,-6,6,6,8,-7,7,3,-3,-1,-5,6,3,6,3,-8,8,3,-2,10,-2,-2,9,6,-6,-6,7,3,-5,1,-10,-3,5,-4,7,-10,1,8,7,-5,-3,6,-2,-10,-7,6,-2,-8,5,5,-6,-10,4,8,-4,-6,1,-6,10,1,-9,-5,-6,-7,4,4,4,6,2,3,4,-2,9,1,4,-7,1,-3,4,9,-9,-10,6,4,10,5,-5,1,5,-5,6,-3,5,-3,3,9,-4,8,6,10,-9,10,-4,-2,-4,9,3,6,-7,9,10,3,-8,4,4,8,2,1,-2,4,-2,-8,4,-2,-1,-10,-8,5,-5,8,6,5,7,-2,1,-6,1,-7,-6,-8,2,9,3,6,6,9,3,8,2,-8,7,7,8,5,-4,2,-10,-6,9,-3,7,5,-8,9,-2,-4,-10,9,6,1,-4,6,8,-9,5,1,3,-1,8,2,6,1,8,4,-1,-4,10,10,-5,6,-10,3,1,-4,-5,-1,4,-6,1,6,5,-10,1,6,9,-5,6,-2,-3,8,-5,-8,-10,-3,4,-4,9,-7,-5,8,4,-3,-3,-9,-3,6,-7,-9,1,-9,-1,-6,-8,3,-8,7,6,2,7,10,10,10,-10,-4,8,6,6,-10,-6,10,-5,8,7,5,-1,5,-8,-9,-1,9,-4,-1,-8,-9,-5,2,3,3,10,-5,-2,-4,-5,-1,4,10,-9,-2,-3,3,9,-9,-5,-6,2,-6,2,-7,3,-5,-1,6,-5,7,1,-7,-7,-5,-1,-7,-10,9], dtype = "uint8")#candidate|7464|(780,)|const|uint8
call_7463 = relay.TupleGetItem(func_931_call(relay.reshape(const_7464.astype('uint8'), [390, 2])), 3)
call_7465 = relay.TupleGetItem(func_934_call(relay.reshape(const_7464.astype('uint8'), [390, 2])), 3)
func_7205_call = mod.get_global_var('func_7205')
func_7207_call = mutated_mod.get_global_var('func_7207')
call_7470 = relay.TupleGetItem(func_7205_call(), 0)
call_7471 = relay.TupleGetItem(func_7207_call(), 0)
output = relay.Tuple([call_7447,call_7459,call_7463,const_7464,call_7470,])
output2 = relay.Tuple([call_7448,call_7460,call_7465,const_7464,call_7471,])
func_7472 = relay.Function([], output)
mod['func_7472'] = func_7472
mod = relay.transform.InferType()(mod)
mutated_mod['func_7472'] = func_7472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7472_call = mutated_mod.get_global_var('func_7472')
call_7473 = func_7472_call()
output = call_7473
func_7474 = relay.Function([], output)
mutated_mod['func_7474'] = func_7474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5608_call = mod.get_global_var('func_5608')
func_5610_call = mutated_mod.get_global_var('func_5610')
call_7496 = relay.TupleGetItem(func_5608_call(), 1)
call_7497 = relay.TupleGetItem(func_5610_call(), 1)
output = call_7496
output2 = call_7497
func_7508 = relay.Function([], output)
mod['func_7508'] = func_7508
mod = relay.transform.InferType()(mod)
mutated_mod['func_7508'] = func_7508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7508_call = mutated_mod.get_global_var('func_7508')
call_7509 = func_7508_call()
output = call_7509
func_7510 = relay.Function([], output)
mutated_mod['func_7510'] = func_7510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_7527 = relay.TupleGetItem(func_1126_call(), 0)
call_7528 = relay.TupleGetItem(func_1127_call(), 0)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
const_7568 = relay.const([10,3,-10,-5,-4,-8,10,-2,7,-4,-10,7,7,-7,9,-10,1,-4,6,4,2,10,-9,-6,4,9,-9,8,-2,-10,-10,-2,2,5,-7,-10,10,2,-4,6,-8,-2,3,-5,-6,8,3,-8,-9,-5,-2,5,6,-1,-6,8,2,-3,9,-2,2,2,3,2,-5,-8,3,10,1,-10,8,2,-8,-9,-2,-4,2,-10,8,-8,-1,1,-10,-3,-2,-9,-1,-2,-4,7,-1,-2,9,-9,6,-9,2,10,10,-4,-6,-5,-3,-9,-10,-5,-9,6,-9,-4,-2,1,-4,-9,-6,-9,5,-1,-4,5,7,7,-5,4,9,8,-1,-7,-1,1,9,-2,-5,1,5,5,6,-8,6,6,1,9,4,-9,2,4,10,-6,-1,6,2,8,5,8,1,7,9,-4,-3,10,4,9,-2,-3,-3,-10,2,3,-5,9,5,8,3,7,-8,1,2,6,-6,-8,-7,4,-8,7,9,1,-3,8,-4,1,-3,-2,4,-1,-8,-9,-9,6,-9,-5,10,-2,7,-6,8,-1,-2,6,-2,6,7,-6,-8,6,-5,6,8,-8,-10,4,-4,9,-9,-9,3,2,1,-8,10,6,6,-1,-2,7,-3,-1,9,2,8,-10,9,3,-10,8,-7,-5,8,7,-7,3,-9,-7,-8,-6,-10,-7,8,8,-1,10,-3,-10,3,1,4,-9,2,-9,5,-7,2,6,4,-10,2,-2,6,-6,-3,-8,4,-10,-1,7,4,3,-7,-10,4,-5,-1,-1,-1,4,5,1,-9,-8,-9,8,-8,-3,-3,6,-2,-6,-8,-8,6,-2,-5,-2,3,-7,-4,6,-10,-7,-10,10,1,-5,-5,-7,6,-3,2,7,5,8,9,-3,2,9,2,6,-7,4,5,-4,3,-3,-5,10,2,-1,-3,9,-4,-9,-10,-4,9,1,-1,4,2,-1,-6,7,1,1,2,-9,-10,7,-7,-9,8,10,-4,-5,2,3,7,7,8,1,-8,8,-3,10,-5,8,-10,5,3,-2,6,-4,-3,-10,-9,-3,-3,6,6,-6,8,4,-2,-4,9,-1,-9,-7,-6,-5,7,-5,-9,-6,9,-5,6,5,-10,-3,4,5,7,-8,-8,9,1,8,6,-6,-6,2,-2,-9,7,-3,-6,-4,10,-7,5,8,1,-9,-7,-2,5,4,2,-10,-3,-9,1,3,5,4,7,9,5,5,-10,7,-10,5,-2,2,-9,-6,6,4,9,-5,-7,4,-10,-5,5,-8,-3,-10,9,2,-5,-8,8,-6,9,5,4,7,-8,8,6,-10,-10,-4,2,-7,-6,10,7,3,5,-2,-9,7,-5,3,-1,-10,1,8,-2,2,1,4,-8,-4,6,4,-4,3,5,1,-6,5,-7,-5,-9,6,9,-8,6,-9,-7,-6,-3,-2,-4,2,-4,-1,1,9,-1,10,5,-6,-7,1,-6,-6,-7,-7,9,-3,6,5,10,-7,-9,10,2,-2,8,4,-2,5,7,2,-1,3,1,-5,2,-1,-7,-4,8,10,1,2,-4,-5,-8,1,4,-7,1,-5,3,3,-6,1,-3,9,-4,-7,9,1,9,-7,5,-7,5,9,-7,-10,-9,6,-9,-6,-8,-1,-5,6,-6,6,-6,-8,-4,-1,-9,-3,-9,2,5,-2,1,2,8,9,-1,-3,-1,-10,-8,-5,1,7,8,-9,-7,10,4,3,1,6,-10,-1,-2,5,1,10,9,-5,7,4,4,-10,-7,2,7,-10,-1,-6,-1,6,1,5,1,1,-3,-10,10,-7,4,-4,1,10,4,-6,6,-8,-6,-1,4,-7,-6,6,-8,2,4,7,-10,9,2,3,-7,-7,6,2,-9,-7,-5,-2,5,8,-7,-7,9,-5,1,-9,8,1,-3,2,-1,8,1,2,-1,7,5,-9,10,-5,1,-9,-1,3,-3,-5,-5,2,-2,-1,-5,3,10,4,7,3,5,-8,-10,10,7,10,10,-7,-6,-5,5,-1,-1,7,6,5,1,10,4,7,-5,3,-8,-8,-9,7,1,2,-5,-10,-10,6,6,-3,6,-4,-6,6,7,2,7,1,7,1,-2,-7,-6,4,-7,-4,6,3,5,9,5,10,-1,1,-6,-2,-5,-1,-9,7,-1,-8,9,2,-3,7,-2,-8,-10,1,-5,-4,-1,3,1,6,1,10,7,5,3,-6,9,-8,-6,4,-1,2,-3,-1,-5,8,-5,7,2,-2,1,2,3,-10,-8], dtype = "int32")#candidate|7568|(847,)|const|int32
call_7567 = relay.TupleGetItem(func_1426_call(relay.reshape(const_7568.astype('int32'), [847,])), 2)
call_7569 = relay.TupleGetItem(func_1428_call(relay.reshape(const_7568.astype('int32'), [847,])), 2)
uop_7570 = relay.log10(const_7568.astype('float32')) # shape=(847,)
func_5279_call = mod.get_global_var('func_5279')
func_5280_call = mutated_mod.get_global_var('func_5280')
call_7575 = func_5279_call()
call_7576 = func_5279_call()
func_6460_call = mod.get_global_var('func_6460')
func_6463_call = mutated_mod.get_global_var('func_6463')
const_7581 = relay.const([[-0.457679],[6.218197],[2.344364],[4.735106],[-4.993589],[2.537191],[-0.853169],[3.993731],[4.729406],[7.777446],[1.291748],[7.128701],[3.171773],[8.020399],[8.563822],[3.462018],[-2.329038],[3.907199],[-7.137484],[-8.931658],[-0.136448],[-0.499383],[-6.658590],[6.545617],[-9.837787],[6.330931],[-8.476930],[-2.230515],[9.811246],[-5.714064],[-9.970827],[-0.960632],[-9.516518],[-5.715208],[-3.062757],[5.834148],[-4.030720],[-1.671087],[-3.834676],[-7.533929],[-8.152313],[-7.044756],[-1.832592],[-5.289499],[-4.622295],[-2.636011],[7.874659],[0.565377],[-2.210604],[-1.718290],[-0.060426],[-5.499826],[5.303102],[1.739843],[-5.661911],[9.842846],[4.959612],[9.143524],[-4.336289],[9.943066]], dtype = "float64")#candidate|7581|(60, 1)|const|float64
call_7580 = relay.TupleGetItem(func_6460_call(relay.reshape(const_7581.astype('float64'), [60,]), relay.reshape(uop_7570.astype('int32'), [847,]), ), 5)
call_7582 = relay.TupleGetItem(func_6463_call(relay.reshape(const_7581.astype('float64'), [60,]), relay.reshape(uop_7570.astype('int32'), [847,]), ), 5)
output = relay.Tuple([call_7527,call_7567,uop_7570,call_7575,call_7580,const_7581,])
output2 = relay.Tuple([call_7528,call_7569,uop_7570,call_7576,call_7582,const_7581,])
func_7587 = relay.Function([], output)
mod['func_7587'] = func_7587
mod = relay.transform.InferType()(mod)
output = func_7587()
func_7588 = relay.Function([], output)
mutated_mod['func_7588'] = func_7588
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7594 = relay.var("var_7594", dtype = "uint16", shape = (14, 12, 8))#candidate|7594|(14, 12, 8)|var|uint16
var_7595 = relay.var("var_7595", dtype = "uint16", shape = (14, 12, 8))#candidate|7595|(14, 12, 8)|var|uint16
bop_7596 = relay.left_shift(var_7594.astype('uint16'), relay.reshape(var_7595.astype('uint16'), relay.shape_of(var_7594))) # shape=(14, 12, 8)
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_7600 = func_6597_call()
call_7601 = func_6597_call()
func_7312_call = mod.get_global_var('func_7312')
func_7315_call = mutated_mod.get_global_var('func_7315')
var_7603 = relay.var("var_7603", dtype = "float32", shape = ())#candidate|7603|()|var|float32
var_7604 = relay.var("var_7604", dtype = "float32", shape = (108,))#candidate|7604|(108,)|var|float32
call_7602 = relay.TupleGetItem(func_7312_call(relay.reshape(var_7603.astype('float32'), []), relay.reshape(var_7604.astype('float32'), [108,]), ), 5)
call_7605 = relay.TupleGetItem(func_7315_call(relay.reshape(var_7603.astype('float32'), []), relay.reshape(var_7604.astype('float32'), [108,]), ), 5)
output = relay.Tuple([bop_7596,call_7600,call_7602,var_7603,var_7604,])
output2 = relay.Tuple([bop_7596,call_7601,call_7605,var_7603,var_7604,])
func_7616 = relay.Function([var_7594,var_7595,var_7603,var_7604,], output)
mod['func_7616'] = func_7616
mod = relay.transform.InferType()(mod)
var_7617 = relay.var("var_7617", dtype = "uint16", shape = (14, 12, 8))#candidate|7617|(14, 12, 8)|var|uint16
var_7618 = relay.var("var_7618", dtype = "uint16", shape = (14, 12, 8))#candidate|7618|(14, 12, 8)|var|uint16
var_7619 = relay.var("var_7619", dtype = "float32", shape = ())#candidate|7619|()|var|float32
var_7620 = relay.var("var_7620", dtype = "float32", shape = (108,))#candidate|7620|(108,)|var|float32
output = func_7616(var_7617,var_7618,var_7619,var_7620,)
func_7621 = relay.Function([var_7617,var_7618,var_7619,var_7620,], output)
mutated_mod['func_7621'] = func_7621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2049_call = mod.get_global_var('func_2049')
func_2051_call = mutated_mod.get_global_var('func_2051')
call_7656 = relay.TupleGetItem(func_2049_call(), 1)
call_7657 = relay.TupleGetItem(func_2051_call(), 1)
func_7205_call = mod.get_global_var('func_7205')
func_7207_call = mutated_mod.get_global_var('func_7207')
call_7671 = relay.TupleGetItem(func_7205_call(), 0)
call_7672 = relay.TupleGetItem(func_7207_call(), 0)
output = relay.Tuple([call_7656,call_7671,])
output2 = relay.Tuple([call_7657,call_7672,])
func_7675 = relay.Function([], output)
mod['func_7675'] = func_7675
mod = relay.transform.InferType()(mod)
output = func_7675()
func_7676 = relay.Function([], output)
mutated_mod['func_7676'] = func_7676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_7771 = relay.TupleGetItem(func_2881_call(), 0)
call_7772 = relay.TupleGetItem(func_2883_call(), 0)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_7774 = func_4118_call()
call_7775 = func_4118_call()
output = relay.Tuple([call_7771,call_7774,])
output2 = relay.Tuple([call_7772,call_7775,])
func_7793 = relay.Function([], output)
mod['func_7793'] = func_7793
mod = relay.transform.InferType()(mod)
output = func_7793()
func_7794 = relay.Function([], output)
mutated_mod['func_7794'] = func_7794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1673_call = mod.get_global_var('func_1673')
func_1674_call = mutated_mod.get_global_var('func_1674')
call_7811 = func_1673_call()
call_7812 = func_1673_call()
output = call_7811
output2 = call_7812
func_7813 = relay.Function([], output)
mod['func_7813'] = func_7813
mod = relay.transform.InferType()(mod)
mutated_mod['func_7813'] = func_7813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7813_call = mutated_mod.get_global_var('func_7813')
call_7814 = func_7813_call()
output = call_7814
func_7815 = relay.Function([], output)
mutated_mod['func_7815'] = func_7815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2894_call = mod.get_global_var('func_2894')
func_2895_call = mutated_mod.get_global_var('func_2895')
call_7823 = relay.TupleGetItem(func_2894_call(), 0)
call_7824 = relay.TupleGetItem(func_2895_call(), 0)
func_6460_call = mod.get_global_var('func_6460')
func_6463_call = mutated_mod.get_global_var('func_6463')
var_7840 = relay.var("var_7840", dtype = "float64", shape = (1, 60))#candidate|7840|(1, 60)|var|float64
const_7841 = relay.const([4,4,2,-4,8,1,-2,-6,-7,7,-1,10,-10,-2,-1,-9,-3,-2,1,-7,9,-4,-6,10,-9,1,-1,-6,7,7,-3,6,1,4,1,-3,-7,5,-7,1,3,8,4,7,1,1,4,9,5,-7,3,9,5,7,9,10,1,8,-1,9,10,-4,-7,-10,-8,-9,5,3,1,5,-10,-4,2,-6,-8,3,-5,2,1,6,-9,10,-4,7,7,-9,-7,-7,4,10,-8,-10,1,7,-6,-3,10,2,-8,-1,-8,-3,-3,4,4,9,-8,-5,5,-2,4,7,-9,-8,-5,-6,-9,-10,9,-2,-9,-7,2,-5,-5,-7,2,-3,-2,-2,1,-3,-6,5,-8,-10,-9,-5,10,-7,9,-4,-7,-6,9,7,-5,-2,-3,6,-7,-10,3,5,-7,8,6,9,-10,-4,2,-9,-4,-7,2,-10,-2,-3,-8,-10,-3,-1,10,-2,-4,9,10,2,-3,-10,-4,3,-1,-3,-9,3,1,8,-3,-2,-7,-2,9,10,5,-6,-10,-5,9,9,-10,7,6,3,-8,-6,-5,3,-2,-5,-2,-6,-2,-3,-10,9,5,-9,3,-10,-6,5,5,-5,-2,-6,3,-5,4,6,-10,-1,-10,4,4,-4,10,-2,-9,2,9,-6,-9,-9,-8,-6,-1,3,-9,7,-3,-6,2,8,8,3,-7,10,-9,-8,6,-7,-10,10,-9,5,-8,5,-2,1,10,-7,-4,-2,8,2,-1,-2,-9,-10,-9,-10,-9,-9,5,-1,6,1,-7,-3,-10,-10,3,-2,4,1,-1,2,-4,-1,3,-4,-9,10,-8,2,7,-1,-2,3,6,-1,4,7,6,-9,-1,9,7,-8,2,5,10,2,-10,9,-2,5,4,6,-9,1,7,1,-9,3,7,-5,-3,-10,-3,-10,-9,-10,6,-5,2,-6,5,-7,4,-8,-7,7,-7,4,6,-6,7,-2,-4,10,2,-7,1,1,-1,8,9,7,-4,7,-4,-7,-1,-6,5,-2,-1,-3,-10,-2,3,-10,-5,10,9,1,2,-6,8,-9,9,-1,-10,-7,-1,5,8,6,-2,5,4,5,-6,1,5,9,1,6,-4,-6,-3,9,-4,-9,1,-6,-1,-1,1,3,1,-2,9,6,3,10,-2,-1,4,-1,-5,-10,-9,5,4,-8,9,-1,-9,4,8,-10,-3,-7,1,1,-6,-2,5,-8,7,-6,-7,-5,-6,8,2,-4,-9,1,-10,7,5,-4,-9,1,-8,4,-6,2,7,5,8,-6,2,-10,-10,-10,-8,-7,-5,-5,-5,-10,8,-2,10,6,-9,-6,10,3,2,-6,8,-7,10,-7,1,-8,7,-5,9,6,6,9,9,5,-5,-2,-2,7,-3,1,-2,-4,-10,8,2,7,8,-3,10,-8,9,-10,-1,7,1,-9,-8,2,1,9,-5,-1,-4,2,2,-9,-10,-6,-3,-6,-10,7,-5,7,-10,9,-3,-10,5,-3,10,2,10,-4,10,7,-4,-9,5,6,10,-1,-8,-4,-3,-1,-8,6,2,10,9,-1,6,-1,-6,6,-2,3,-10,-2,3,-5,-8,-8,10,-2,9,-9,5,-4,4,-9,9,-6,-8,-1,2,3,-8,10,-10,6,-10,-4,4,8,-10,-6,-8,9,9,-10,-9,-2,-3,-6,9,-4,-8,3,-6,3,7,-8,-2,-2,8,-5,-4,-3,-1,2,2,6,4,-5,-8,8,-8,10,-3,2,-6,-8,3,-7,-2,-2,-5,-8,8,1,10,1,8,-9,-8,2,-9,2,2,6,-8,-10,-7,-2,-2,10,4,1,7,-1,-2,-6,-3,-2,-10,1,-7,1,-1,-10,7,6,-5,3,10,6,-9,4,-3,-9,7,2,-2,9,-7,-8,-10,8,-3,7,7,5,8,-7,8,-5,-7,8,-10,-3,-7,-5,-5,-2,6,-4,-3,-10,-10,3,5,2,4,1,10,-5,5,4,5,-10,7,5,-3,-2,-1,1,-2,-8,-7,-2,-3,4,7,9,5,-2,-1,2,-1,7,7,10,2,-10,6,-6,1,8,7,9,-5,4,-9,2,-9,3,-8,9,-2,-9,-1,9,4,-9,5,2,-10,-7,-3,10,-9,-9,-6,7,5,6,2,9,3,6,7,-7,4,-7,-3,8,2,9,6,-5,3,-9,9,2,6,-1,7,2,-1,8,-8,8,-4,7,2,-2,-5,3,-9,-5,2,-7,-3,-10,-8,2,7,-3,4,2,1,-2,-5,10,9,-6,-3,-2,2], dtype = "int32")#candidate|7841|(847,)|const|int32
call_7839 = relay.TupleGetItem(func_6460_call(relay.reshape(var_7840.astype('float64'), [60,]), relay.reshape(const_7841.astype('int32'), [847,]), ), 7)
call_7842 = relay.TupleGetItem(func_6463_call(relay.reshape(var_7840.astype('float64'), [60,]), relay.reshape(const_7841.astype('int32'), [847,]), ), 7)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_7857 = relay.TupleGetItem(func_856_call(), 0)
call_7858 = relay.TupleGetItem(func_858_call(), 0)
output = relay.Tuple([call_7823,call_7839,var_7840,const_7841,call_7857,])
output2 = relay.Tuple([call_7824,call_7842,var_7840,const_7841,call_7858,])
func_7859 = relay.Function([var_7840,], output)
mod['func_7859'] = func_7859
mod = relay.transform.InferType()(mod)
mutated_mod['func_7859'] = func_7859
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7860 = relay.var("var_7860", dtype = "float64", shape = (1, 60))#candidate|7860|(1, 60)|var|float64
func_7859_call = mutated_mod.get_global_var('func_7859')
call_7861 = func_7859_call(var_7860)
output = call_7861
func_7862 = relay.Function([var_7860], output)
mutated_mod['func_7862'] = func_7862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2607_call = mod.get_global_var('func_2607')
func_2609_call = mutated_mod.get_global_var('func_2609')
call_7908 = relay.TupleGetItem(func_2607_call(), 1)
call_7909 = relay.TupleGetItem(func_2609_call(), 1)
func_5178_call = mod.get_global_var('func_5178')
func_5179_call = mutated_mod.get_global_var('func_5179')
call_7945 = relay.TupleGetItem(func_5178_call(), 0)
call_7946 = relay.TupleGetItem(func_5179_call(), 0)
func_2842_call = mod.get_global_var('func_2842')
func_2843_call = mutated_mod.get_global_var('func_2843')
call_7955 = relay.TupleGetItem(func_2842_call(), 1)
call_7956 = relay.TupleGetItem(func_2843_call(), 1)
func_7813_call = mod.get_global_var('func_7813')
func_7815_call = mutated_mod.get_global_var('func_7815')
call_7959 = func_7813_call()
call_7960 = func_7813_call()
func_6223_call = mod.get_global_var('func_6223')
func_6224_call = mutated_mod.get_global_var('func_6224')
call_7970 = relay.TupleGetItem(func_6223_call(), 0)
call_7971 = relay.TupleGetItem(func_6224_call(), 0)
func_2263_call = mod.get_global_var('func_2263')
func_2264_call = mutated_mod.get_global_var('func_2264')
call_7984 = func_2263_call()
call_7985 = func_2263_call()
output = relay.Tuple([call_7908,call_7945,call_7955,call_7959,call_7970,call_7984,])
output2 = relay.Tuple([call_7909,call_7946,call_7956,call_7960,call_7971,call_7985,])
func_7986 = relay.Function([], output)
mod['func_7986'] = func_7986
mod = relay.transform.InferType()(mod)
mutated_mod['func_7986'] = func_7986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7986_call = mutated_mod.get_global_var('func_7986')
call_7987 = func_7986_call()
output = call_7987
func_7988 = relay.Function([], output)
mutated_mod['func_7988'] = func_7988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6251_call = mod.get_global_var('func_6251')
func_6252_call = mutated_mod.get_global_var('func_6252')
call_7994 = relay.TupleGetItem(func_6251_call(), 0)
call_7995 = relay.TupleGetItem(func_6252_call(), 0)
func_5122_call = mod.get_global_var('func_5122')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_8023 = func_5122_call()
call_8024 = func_5122_call()
func_1087_call = mod.get_global_var('func_1087')
func_1090_call = mutated_mod.get_global_var('func_1090')
const_8026 = relay.const([-4,-5,7,-8,-2,10,-7,-8,8,10,-2,-3,-5,2,-6,10,-6,-7,-10,-1,9,4,-10,-4,8,10,-7,8,2,5,3,-9,2,-3,2,7,-7,9,1,-8,7,10,-2,7,-8,-1,-10,1,8,-4,-8,-4,-10,-2,6,2,7,9,-10,-5,-9,-9,-9,-8,-4,7,-3,-9,-6,6,3,7,-1,1,-3,2,-5,10,3,2,2,1,2,8,1,2,-1,-3,-5,6,3,1,-8,3,-9,-9,6,-6,-8,-6,8,2,-7,4,1,2,-5,-1,4,-4,-1,-3,3,-5,6,1,-1,7,-7,-2,10,-2,8,10,1,4,7,9,9,-10,-7,-10,3,8,8,-2,-3,5,-10,-3,9,5,5,5,-9,-8,7,5,-7,3,3,6,-10,9,-6,-4,-8,-10,-2,6,3,8,-5,-1,7,10,1,-8,-6,2,-9,-8,5,9,-4,-9,-2,6,-1,10,3,8,5,-5,-10,5,-3,-6,3,-6,-4,-4,1,2,7,9,-3,1,2,-10,-3,4,8,-4,7,7,-4,-8,9,10,3,5,6,-3,-4,-3,-8,4,-8,8,-10,-9,-6,-3,8,-2,-3,-8,-4,9,1,-6,-10,-6,1,-6,-9,-7,-3,-9,-2,-3,-7,-5,-9,1,-8,-1,-9,7,-1,1,7,2,-8,10,-1,6,1,8,-6,1,8,-2,-9,9,3,7,-9,9,-1,7,3,9,-3,-3,-10,2,-6,-6,-5,-2,-4,8,9,9,10,1,9,7,-1,-4,-7,-8,3,6,7,-6,-9,4,-6,10,-1,9,-3,6,9,4,6,-6,3,9,-2,-3,-3,-10,2,-5,3,4,2,-1,-2,6,-4,-9,8,9,4,2,-8,6,-4,-2,-7,-4,-8,2,7,-8,-2,-10,-6,10,-10,7,7,-8,4,-10,6,-2,9,4,3,1,-10,8,1,-6,-2,-8,6,-2,6,3,-5,6,-2,4,-4,-3,-5,2,10,-4,3,-1,-10,1,-4,7,1,7,-6,1,3,6,-6,3,-6,-8,1,-8,-2,-4,-3,-10,-6,8,-8,-4,4,9,10,-5,1,7,-3,-2,4,-3,-6,-3,-2,6,1,-10,-2,4,3,8,3,5,-2,10,10,5,8,2,-1,9,8,7,-8,-2,2,-4,-7,10,-3,-5,8,3,-8,-8,-1,2,-6,-9,-2,7,3,1,-10,7,-3,-10,-4,7,-8,-2,-1,10,3,-4,-2,-1,2,-3,2,10,6,-6,-3,-4,-9,-9,1,10,1,-1,4,-6,-5,-1,-2,-4,-10,-1,-7,-1,-9,9,-2,-6,-4,3,-8,-8,-1,9,1,4,-6,-2,7,-9,6,10,8,10,-10,2,6,-2,1,10,7,-1,8,5,-9,-6,2,-6,10,4,10,10,8,-1,-5,8,7,-4,5,2,2,2,4,6,-1,-5,-8,7,7,4,-10,-4,4,-4,5,-4,6,5,-3,5,1,6,-5,9,10,-5,-8,7,-7,4,9,-3,5,4,-8,1,-8,-1,10,6,5,-10,10,-6,10,-3,7,3,-3,-9,5,10,-9,-8,-5,10,-6,3,-10,7,9,7,5,2,-9,10,-3,9,5,2,10,8,-4,3,9,2,-7,8,10,-1,10,-5,4,-6,9,-7,-2,6,5,10,7,-6,2,10,3,-5,5,-8,1,-5,4,3,8,-3,-9,1,-6,2,-2,-4,-6,-9,-6,-7,3,-1,-8,6,-4,-1,4,10,-8,10,7,-4,-2,3,4,-6,5,-5,-2,7,3,-10,9,-9,-6,-6,2,7,4,1,-1,-4,-6,7,3,-3,-3,3,5,-8,10,6,-3,7,3,7,7,-10,2,1,3,-2,-1,8,-9,-8,10,3,7,1,8,-3,9,9,1,1,-6,-10,-9,4,5,-7,6,-8,-7,-2,-7,3,-8,-1,2,3,-4,4,3,3,10,1,-9,-8,8,-3,-6,-2,9,-5,5,9,-3,7,3,-4,-10,-8,5,-5,-5,-9,7,5,-7,8,-10,-5,2,-9,-2,9,-9,10,2,-7,8,-7,-7,2,3,-6,-7,-6,-3,-5,7,6,8,7,3,-6,-10,-5,-5,1,-7,1,-9,4,-1,8,2,5,10,-1,-8,6,-1,-2,-10,-4,-9,-2,1,2,-6,3,2,7,10,7,-6,-5,-5,-1,10,-1,-2,9,10,9,-10,1,8,6,-7,-7,7,10,-9,-7,10,-7,-3,-8,-8,9,7], dtype = "int32")#candidate|8026|(847,)|const|int32
call_8025 = relay.TupleGetItem(func_1087_call(relay.reshape(const_8026.astype('int32'), [847,])), 3)
call_8027 = relay.TupleGetItem(func_1090_call(relay.reshape(const_8026.astype('int32'), [847,])), 3)
output = relay.Tuple([call_7994,call_8023,call_8025,const_8026,])
output2 = relay.Tuple([call_7995,call_8024,call_8027,const_8026,])
func_8029 = relay.Function([], output)
mod['func_8029'] = func_8029
mod = relay.transform.InferType()(mod)
output = func_8029()
func_8030 = relay.Function([], output)
mutated_mod['func_8030'] = func_8030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_8048 = relay.TupleGetItem(func_2881_call(), 0)
call_8049 = relay.TupleGetItem(func_2883_call(), 0)
output = call_8048
output2 = call_8049
func_8051 = relay.Function([], output)
mod['func_8051'] = func_8051
mod = relay.transform.InferType()(mod)
mutated_mod['func_8051'] = func_8051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8051_call = mutated_mod.get_global_var('func_8051')
call_8052 = func_8051_call()
output = call_8052
func_8053 = relay.Function([], output)
mutated_mod['func_8053'] = func_8053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7508_call = mod.get_global_var('func_7508')
func_7510_call = mutated_mod.get_global_var('func_7510')
call_8056 = func_7508_call()
call_8057 = func_7508_call()
output = relay.Tuple([call_8056,])
output2 = relay.Tuple([call_8057,])
func_8067 = relay.Function([], output)
mod['func_8067'] = func_8067
mod = relay.transform.InferType()(mod)
mutated_mod['func_8067'] = func_8067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8067_call = mutated_mod.get_global_var('func_8067')
call_8068 = func_8067_call()
output = call_8068
func_8069 = relay.Function([], output)
mutated_mod['func_8069'] = func_8069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5122_call = mod.get_global_var('func_5122')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_8146 = func_5122_call()
call_8147 = func_5122_call()
func_2511_call = mod.get_global_var('func_2511')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_8152 = func_2511_call()
call_8153 = func_2511_call()
output = relay.Tuple([call_8146,call_8152,])
output2 = relay.Tuple([call_8147,call_8153,])
func_8171 = relay.Function([], output)
mod['func_8171'] = func_8171
mod = relay.transform.InferType()(mod)
output = func_8171()
func_8172 = relay.Function([], output)
mutated_mod['func_8172'] = func_8172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8029_call = mod.get_global_var('func_8029')
func_8030_call = mutated_mod.get_global_var('func_8030')
call_8208 = relay.TupleGetItem(func_8029_call(), 0)
call_8209 = relay.TupleGetItem(func_8030_call(), 0)
output = call_8208
output2 = call_8209
func_8219 = relay.Function([], output)
mod['func_8219'] = func_8219
mod = relay.transform.InferType()(mod)
mutated_mod['func_8219'] = func_8219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8219_call = mutated_mod.get_global_var('func_8219')
call_8220 = func_8219_call()
output = call_8220
func_8221 = relay.Function([], output)
mutated_mod['func_8221'] = func_8221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5842_call = mod.get_global_var('func_5842')
func_5843_call = mutated_mod.get_global_var('func_5843')
call_8224 = relay.TupleGetItem(func_5842_call(), 0)
call_8225 = relay.TupleGetItem(func_5843_call(), 0)
output = call_8224
output2 = call_8225
func_8226 = relay.Function([], output)
mod['func_8226'] = func_8226
mod = relay.transform.InferType()(mod)
output = func_8226()
func_8227 = relay.Function([], output)
mutated_mod['func_8227'] = func_8227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3929_call = mod.get_global_var('func_3929')
func_3931_call = mutated_mod.get_global_var('func_3931')
call_8274 = relay.TupleGetItem(func_3929_call(), 0)
call_8275 = relay.TupleGetItem(func_3931_call(), 0)
func_4356_call = mod.get_global_var('func_4356')
func_4358_call = mutated_mod.get_global_var('func_4358')
const_8317 = relay.const([3,-3,-3,5,-5,10,-8,5,-9,-3,-7,-4,-4,9,4,-8,1,-1,-10,-10,1,-5,8,-10,10,-2,4,3,10,-7,8,-3,-7,-5,-5,2,-5,-2,6,10,7,-7,9,1,2,4,-3,2,3,9,-2,-3,-7,-2,1,10,-5,3,7,-3,-9,-10,6,-2,-9,9,1,2,1,10,-7,1,5,8,-5,-2,10,9,-4,-6,-4,-8,-9,3,-4,9,1,-3,-4,-10,-4,7,4,9,-9,-5,-10,-7,3,6,-3,1,6,4,-7,-1,7,-6,-4,-9,9,-7,6,7,-6,-1,9,6,-7,5,5,6,2,10,-6,2,-4,-4,4,2,-4,10,-4,-9,5,5,-8,9,-3,-9,-10,2,-7,-6,10,1,-2,7,7,9,8,1,6,-9,3,-8,6,-8,-8,5,4,-2,-9,2,-5,-8,-6,-10,-3,1,-6,8,1,-6,-10,-9,-9,1,-1,1,-6,10,10,-4,10,8,6,-7,-3,8,-6,-10,-7,10,-3,-4,4,1,-4,8,10,-8,-3,3,-10,1,-5,8,1,-10,2,3,7,-9,-9,-5,-4,-5,-9,-5,7,-4,9,6,1,4,9,-7,-3,7,5,3,4,8,-6,2,-9,10,8,7,2,-3,1,7,-8,10,-6,-5,-2,-4,6,-4,4,-4,-9,-4,-4,-2,-6,-3,-3,2,-5,-10,1,-7,-3,3,-6,2,10,6,4,1,9,6,6,-1,-6,1,-6,4,1,9,-6,3,-8,2,-9,3,8,9,-9,6,-1,3,-5,-9,6,-4,-10,10,5,1,8,1,-5,-9,-1,2,-4,-1,1,5,-9,-10,5,-8,-4,4,5,8,-6,-4,6,8,10,10,1,-9,-4,1,10,10,10,-8,1,-3,-2,1,3,-7,1,4,-3,-4,1,8,7,-5,-4,-10,-8,-2,-1,10,6,-9,-7,1,-8,-8,-2,-10,6,6,8,-7,-8,-9,-5,5,8,-8,-6,4,-6,3,-3,-7,-8,-3,8,5,10,-6,-2,-6,-4,-5,3,-4,-4,-7,10,7,6,6,-9,-1,-4,-4,8,7,6,2,-1,-8,-5,-3,-8,5,-10,9,4,10,9,-6,-6,10,-5,1,9,3,6,-1,8,-10,6,10,3,10,4,10,-9,9,-3,1,2,7,2,4,-1,8,6,-9,-6,3,-5,7,1,7,8,5,-2,10,10,3,8,1,7,-5,9,2,-8,7,9,-5,-3,-7,-5,-8,10,-8,-3,2,-1,5,-4,-5,8,-6,-7,3,3,5,-8,-5,-6,-5,-4,-1,6,8,-2,6,6,-6,3,4,-1,6,-4,8,-3,-1,1,-3,-5,-1,-3,-9,-9,3,6,9,-8,7,-5,-4,-7,5,-6,-9,7,-7,6,-1,-3,-6,4,4,-2,4,7,4,-2,4,-7,-6,-2,7,1,3,-4,2,-6,-10,9,-6,1,-10,8,8,8,4,-10,-8,-10,-6,-9,2,5,4,7,2,-9,-8,8,-6,3,6,8,-6,-4,5,-3,9,-1,3,2,-4,8,9,2,-2,-3,10,-4,-2,-1,2,-3,1,5,-2,7,-9,1,-1,-1,-8,5,8,6,-10,8,-10,-4,-7,-5,7,6,-9,1,-10,6,1,-7,3,-10,10,-8,8,-3,2,-3,-2,-4,-8,2,9,9,1,10,9,10,5,4,-9,-10,5,-1,-4,9,-10,-1,10,1,-6,-5,9,8,3,-1,9,5,-5,-10,-1,-3,1,-2,-4,2,1,8,-5,6,-8,-2,6,-10,6,-10,-10,-8,6,2,10,-3,3,3,-10,6,5,7,-5,-4,9,-8,8,-2,5,-6,9,-7,5,-10,6,4,-4,-3,-8,-10,1,-5,-3,3,2,2,-3,2,7,-2,8,6,-7,-10,6,-3,5,7,-7,-5,-2,-8,6,-4,4,7,3,3,-2,6,-1,6,9,6,-6,4,-10,4,4,2,-3,1,2,-6,7,6,-3,5,-8,7,-6,1,-3,5,-2,-9,-5,10,4,-6,10,-8,4,4,-8,5,9,-1,10,2,-10,6,-9,5,-2,4,-2,-4,10,8,6,2,-9,10,9,-3,2,6,-6,7,-1,2,5,-10,4,3,-1,-9,-7,10,-10,-7,-2,4,-6,-8,1,-2,7,-1,10,-5,8,1,-3,-3,6,3,-5,-8,7,-9,7,7,1,-7,4,4,-5,1,-8,1,8,-3,-3,3,-8,-2,-4,-1,9,-8], dtype = "int32")#candidate|8317|(847,)|const|int32
call_8316 = relay.TupleGetItem(func_4356_call(relay.reshape(const_8317.astype('int32'), [847,])), 0)
call_8318 = relay.TupleGetItem(func_4358_call(relay.reshape(const_8317.astype('int32'), [847,])), 0)
output = relay.Tuple([call_8274,call_8316,const_8317,])
output2 = relay.Tuple([call_8275,call_8318,const_8317,])
func_8329 = relay.Function([], output)
mod['func_8329'] = func_8329
mod = relay.transform.InferType()(mod)
output = func_8329()
func_8330 = relay.Function([], output)
mutated_mod['func_8330'] = func_8330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
call_8335 = relay.TupleGetItem(func_856_call(), 0)
call_8336 = relay.TupleGetItem(func_858_call(), 0)
func_1279_call = mod.get_global_var('func_1279')
func_1282_call = mutated_mod.get_global_var('func_1282')
call_8348 = relay.TupleGetItem(func_1279_call(relay.reshape(call_8335.astype('float32'), [7, 14, 4])), 1)
call_8349 = relay.TupleGetItem(func_1282_call(relay.reshape(call_8335.astype('float32'), [7, 14, 4])), 1)
func_2511_call = mod.get_global_var('func_2511')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_8350 = func_2511_call()
call_8351 = func_2511_call()
output = relay.Tuple([call_8335,call_8348,call_8350,])
output2 = relay.Tuple([call_8336,call_8349,call_8351,])
func_8362 = relay.Function([], output)
mod['func_8362'] = func_8362
mod = relay.transform.InferType()(mod)
output = func_8362()
func_8363 = relay.Function([], output)
mutated_mod['func_8363'] = func_8363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7793_call = mod.get_global_var('func_7793')
func_7794_call = mutated_mod.get_global_var('func_7794')
call_8425 = relay.TupleGetItem(func_7793_call(), 1)
call_8426 = relay.TupleGetItem(func_7794_call(), 1)
func_7442_call = mod.get_global_var('func_7442')
func_7443_call = mutated_mod.get_global_var('func_7443')
call_8431 = relay.TupleGetItem(func_7442_call(), 0)
call_8432 = relay.TupleGetItem(func_7443_call(), 0)
func_6177_call = mod.get_global_var('func_6177')
func_6180_call = mutated_mod.get_global_var('func_6180')
call_8471 = relay.TupleGetItem(func_6177_call(relay.reshape(call_8431.astype('float32'), [7, 14, 4])), 2)
call_8472 = relay.TupleGetItem(func_6180_call(relay.reshape(call_8431.astype('float32'), [7, 14, 4])), 2)
func_2607_call = mod.get_global_var('func_2607')
func_2609_call = mutated_mod.get_global_var('func_2609')
call_8475 = relay.TupleGetItem(func_2607_call(), 0)
call_8476 = relay.TupleGetItem(func_2609_call(), 0)
func_6047_call = mod.get_global_var('func_6047')
func_6050_call = mutated_mod.get_global_var('func_6050')
const_8485 = relay.const([-8,-10,-10,-9,-8,-3,5,-1,7,6,4,8,-9,1,2,10,9,-7,10,-3,2,-5,6,-8,8,3,-5,5,6,6,1,1,7,-7,3,-5,8,4,10,8,-5,1,4,7,-1,1,10,-10,-10,-6,-8,10,5,-1,7,2,-2,3,8,-9,5,-8,2,4,4,-4,2,-8,9,1,-1,-7,5,-1,2,-9,8,5,-7,1,-10,-6,3,1,-5,6,-5,-9,5,-3,-9,-7,2,-8,-1,-10,8,-5,-2,-10,9,3,1,6,3,6,-4,9,-2,-4,-8,6,-2,6,7,3,4,-4,9,2,1], dtype = "int64")#candidate|8485|(121,)|const|int64
const_8486 = relay.const([8,10,-3,-7,-1,-8,3,-1,9,-10,1,9,-6,-1,8,4,10,-8,-10,-3,-9,6,-2,-6,-2,-8,-2,2,-8,7,-8,4,4,-8,-8,-7,-1,-8,-1,-6,3,-3,-10,5,7,6,4,5,1,-4,4,5,-4,10,9,6,1,7,4,1,-5,-1,6,-10,-9,5,6,1,-5,5,7,6,-3,-1,-6,-10,-9,1,-7,4,5,-1,1,3,3,10,1,9,-10,1,-3,6,-4,-9,9,-6,3,7,9,10,8,-3,-7,-3,3,10,6,7,-6,-10,-8,-1,-4,-4,10,7,5,9,4,-8,7,-2,5,-3,-6,6,-9,-6,7,4,-6,-7,10,-5,-7,1,9,7,3,-5,-2,2,9,-4,7,-6,-8,-6,-7,5,1,8,-9,6,-6,8,5,1,7,-2,3,9,-9,2,-5,-1,-2,10,5,-3,10,-1,3,-9,-7,-7,9,2,3,7,2,8,-9,5,-4,-9,2,-9,1,-5,3,9,-10,-1,8,10,-7,5,-7,-2,-1,-7,-10,-5,-8,-1,4,2,-4,6,-2,1,-5,5,-7,4,9,-8,-10,2,-7,7,-5,-5,4,1,10,-5,-8,-8,9,-4,1,-9,-7,9,4,-5,-6,7,4,8,-2,10,5,-7,-7,-5,3,1,5,-5,-7,7,3,-5,-4,4,6,-7,9,7,5,6,6,-7,7,-9,4,-8,-1,-5,-6,2,2,-4,3,9,-5,-5,2,3,6,6,9,-7,8,7,1,-5,1,4,-3,2,-7,9,9,-1,-4,-4,-2,3,-3,4,-4,-8,10,-6,4,1,5,3,1,-8,10,8,-3,1,-3,-1,-4,1,3,-9,7,10,-9,3,-6,3,-5,7,-1,-3,3,-3,-6,-3,2,-8,1,9,1,-9,7,3,4,7,10,2,-7,-4,-9,-2,10,-10,-7,10,2,-5,3,10,-9,3,-8,-5,-9,-10,6,9,-3,7,-7,10,-8,10,-2,-9,7,10,-8,-4,4,7,-7,7,5,-2,3,-4,6,2,-4,8,-4,9,-3,-1,7,10,4,6,1,4,1,-7,-1,4,2,7,2,10,-8,-4,-10,-1,-2,-6,8,-9,7,5,-4,3,4,-4,3,2,6,8,-10,2,7,-5,7,3,9,-2,-10,-1,-5,9,-10,1,8,-3,10,10,-3,-4,10,-6,9,4,-5,4,-1,-7,-5,-6,-2,1,4,1,8,-8,7,7,-4,-5,-5,6,-1,4,5,-1,1,-9,3,2,7,8,-4,10,-4,-6,4,-5,-6,3,1,8,-3,-8,-7,8,10,8,10,3,-2,5,2,-3,10,-10,9,4,-5,8,5,-3,-3,1,10,-1,5,-2,-5,5,-10,-8,-3,9,-7,7,7,6,-5,-5,-3,1,2,2,6,-5,-2,-3,5,2,-3,3,3,1,-6,-2,1,-4,-7,-10,-4,9,-8,-1,-8,-5,4,-2,7,2,8,-10,-9,1,1,-9,6,10,-2,-5,6,3,9,-4,7,-8,1,-3,2,-6,-5,1,5,-3,4,9,-1,-7,-8,-5,-6,1,2,-8,9,-1,-1,6,-4,4,9,8,-6,10,-8,2,-9,3,-8,-6,-5,3,-7,-1,-10,-1,-8,8,-5,-9,-3,-9,5,-4,1,2,-6,1,4,6,-6,-4,5,-8,2,5,8,10,4,-6,3,-2,-3,-2,-6,2,5,-4,-9,3,10,7,-2,3,10,-2,7,1,8,10,4,-5,7,-1,4,8,-2,3,-5,-9,-8,-9,6,7,-5,-7,9,8,-5,-4,3,-2,10,-10,-2,9,1,-4,-10,-10,-8,-6,10,4,-4,-4,-2,-3,-2,5,-1,5,-4,6,2,1,-2,-6,10,10,10,-1,10,3,7,5,4,-10,9,-2,-2,10,9,-10,9,5,4,10,-1,6,-2,-6,3,7,-1,-4,4,-9,-3,4,-9,-9,-6,-8,3,7,-7,6,-8,-3,-3,-4,-10,-2,3,4,8,6,-6,2,-10,-7,-1,-6,-7,10,3,-9,-8,-7,8,3,-9,-9,-5,4,-8,-10,-5,8,5,-2,-1,-3,-1,-9,4,-4,-3,7,3,-3,2,2,10,-9,-7,3,-1,8,-9,-10,1,7,6,3,-3,2,10,5,3,6,7,9,-8,-8,6,-1,2,4,-1,-7,3,-2,-3,-4,-2,-6,10,7,-4,6,-2,10,6,-2,-3,1,-10,1,-9,2,5,-10,-5,4,1,3,10,9,-9,3,2,10,-9,7,-5,-1,9,7,10,7,-5,7,6,-1,7,-9,-2,-2,9,10,2,-6,3,-7,7,4,-6,7,-7,9,6,4,6,-8,-9,10,-10,-2,-10,-5,5,-10,10,-3,10,2,7,-4,4,-9,-10,4,-5,-2,7,5,9,-3,5,-8,7,10,8,8,-8,4,-7,-8,7,1,-9,8,-2,-9,-8,-1,-6,10,5,-5,6,-10,10,-5,-2,-2,3,-1,2,1,6,6,2,-8,-5,-1,4,4,-3,-10,-5,6,-2,-2,-6,6,-4,-5,-8,7,-6,2,10,-4,5,8,6,-10,2,3,-5,-9,1,9,-9,-3,-3,-4,3,7,-4,9,-10,6,-1,7,8,-8,2,-8,-2,-5,-6,-1,1,-8,-3,-2,-6,-5,9,-6,10,8,1,-2,-9,-1,7,5,-10,-2,-7,-7,5,3,-4,5,-5,7,-10,-1,7,3,4,4,8,6,-10,-2,7,-1,4,-6,-8,5,1,5,7,-1,-6,4,1,-1,5,8,-9,-4,6,2,-10,-1,4,-8,-6,2,4,-5,-8,-7,-10,-8,5,-3,-9,-4,3,-9,-1,-10,5,-8,9,-5,-10,3,-9,-10,-10,-5,10,-9,5,2,4,5,-3,10,6,1,8,-7,-5,-3,-2,6,-8,-6,3,-2,-9,6,-2,6,-2,6,-2,-8,10,4,8,5,-2,-10,9,2,9,-4,4,8,8,7,7,-9,-5,-10,-10,2,5,9,-5,6,10,-6,-1,-2,8,-10,-5,5,-1,-4,1,-7,7,4,8,8,9,6,-6,-10,-10,-3,-1,-6,3,-7,5,3,-1,-5,-7,9,-5,-8,3,-9,-8,7,-1,4,-2,-10,-5,2,10,-5,10,-2,8,10,-6,2,1,5,-2,-8,2,-1,9,-10,-1,-5,-10,-8,5,-8,8,8,1,1,-4,8,-7,2,-4,-6,-9,8,7,6,5,-4,-5,-2,6,2,4,-6,8,-8,10,7,-4,9,-2,-3,10,-10,10,3,-5,5,-4,-2,-9,-7,4,-8,-1,-2,-3,-10,4,8,-3,-9,-6,10,7,4,-10,-5,-5,7,-10,-8,7,6,9,-7,-6,3,-3,4,2,-6,-7,1,1,-7,-8,-6,3,6,5,-6,-10,-5,-1,4,6,-10,-8,4,-10,2,4,-10,-9,2,-10,5,7,-6,8,2,8,7,-4,7,2,9,-9,-6,7,-2,-4,10,8,10,4,10,-7,-9,-9,-2,-10,-8,3,-7,10,9,6,-7,-3,-10,2,-10,8,7,-10,8,-3,-8,8,5,3,-4,-3,-5,2,7,7,3,9,-5,-1,10,9,8,-1,9,-1,5,6,2,5,-1,9,10,-4,-8,9,-8,-5,-8,-3,10,-2,8,5,5,1,4,10,7,-8,8,2,8,4,4,4,1,-1,3,1,7,4,10,-5,7,-2,3,-10,-3,-8,4,-3,6,-4,-1,7,-6,9,-6,-5,-2,-5,-2,7,-1,-2,-4,10,8,-1,10,7,10,4,-2,8,-7,-10,-9,-6,-1,5,-3,7,8,10,-9,-4,5,-6,8,-1,-6,3,8,-8,-8,-4,8,4,-3,-6,1,1,1,-3,9,1,4,3,-5,-1,-3,-4,8,9,-2,2,-8,-1,10,7,9,7,3,-5,2,-1,-1,-6,-3,-2,3,-2,9,-1,9,-10,-5,4,-8,6,5,5,-2,-8,-9,2,4,-4,-1,-2,10,-1,-1,-2,-1,9,6,5,4,-3,-2,4,10,1,-10,2,-6,-6,5,6,-6,6,-6,8,-4,2,7,-4,-1,-10,1,-2,4,-4,5,9,-4,3,-7,1,-3,9,-6,-9,-1,7,-1,-9,-6,-8,-2,2,5,7,8,5,-8,1,9,-10,-9,2,-7,-8,1,-5,6,-10,-3,-3,4,2,4,7,-3,4,7,3,5,8,9,3,-3,6,-2,6,-9,-10,-2,-6,6,-9,6,-7,-5,-10,-10,-10,6,8,-9,5,-5,-10,-4,5,8,4,-6,-6,-8,3,-9,-3,-3,6,7,9,-8,2,7,5,9,-1,10,6,-6,-8,-4,-4,3,-8,-1,6,-7,-5,-6,-2,-8,2,4,6,6,7,-6,-8,8,1,4,1,6,8,6,8,6,-10,7,8,-3,-5,5,9,-1,5,8,9,-3,5,-6,1,-3,2,-10,-3,-7,-1,-4,-6,-1,-2,-8,-2,-7,-8,1,7,-2,-4,-9,-5,-5,-9,-7,8,5,-8,1,1,10,-1,1,-5,-6,7,-3,-2,-9,1,-5,5,-9,2,-4,7,4,-2,-5,2,-5,-7,-1,1,9,5,1,3,-4,1,9,1,4,-2,2,10,-1,8,-5,2,-10,-9,9,-2,-8,1,9,-3,-7,3,9,5,-2,1,-1,-3,-2,-2,4,-3,7,4,-8,-10,-3,2,-8,-1,-1,8,-7,-3,-3,7,-10,-2,6,4,2,-7,-9,-7,8,-9,-2,1,8,-6,10,10,6,9,-7,-4,-9,6,-9,-8,2,-6,-6,2,2,7,-3,-3,9,1,-7,7,-5,3,-7,-3], dtype = "int64")#candidate|8486|(1815,)|const|int64
call_8484 = relay.TupleGetItem(func_6047_call(relay.reshape(const_8485.astype('int64'), [11, 11, 1]), relay.reshape(const_8486.astype('int64'), [11, 11, 15]), ), 0)
call_8487 = relay.TupleGetItem(func_6050_call(relay.reshape(const_8485.astype('int64'), [11, 11, 1]), relay.reshape(const_8486.astype('int64'), [11, 11, 15]), ), 0)
output = relay.Tuple([call_8425,call_8431,call_8471,call_8475,call_8484,const_8485,const_8486,])
output2 = relay.Tuple([call_8426,call_8432,call_8472,call_8476,call_8487,const_8485,const_8486,])
func_8502 = relay.Function([], output)
mod['func_8502'] = func_8502
mod = relay.transform.InferType()(mod)
output = func_8502()
func_8503 = relay.Function([], output)
mutated_mod['func_8503'] = func_8503
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8504 = relay.var("var_8504", dtype = "int64", shape = (5, 5, 10))#candidate|8504|(5, 5, 10)|var|int64
const_8505 = relay.const([[[-4,9,2,3,-5,9,1,-5,10,8],[7,4,3,-8,-7,-6,-3,-2,1,6],[-6,-2,-1,-5,-3,2,5,3,-3,6],[5,5,-9,2,4,3,-5,9,2,-4],[7,6,-5,9,8,-10,-9,3,-1,5]],[[-3,5,3,-3,-8,-1,-4,-8,-6,8],[6,8,-2,1,-6,-9,5,6,-8,5],[7,-2,3,-9,-10,-4,5,-10,-3,-2],[-7,9,-5,-8,-5,2,8,-10,-7,-1],[-7,3,-7,1,-6,-10,-6,-5,-3,5]],[[-5,-9,-2,-6,-1,5,-4,-2,-3,-2],[7,-4,-2,-3,1,4,-6,10,1,6],[7,-9,-10,-1,-3,-6,8,3,-6,-4],[6,-4,10,-10,-4,-4,-8,1,4,-4],[6,9,-7,-3,-1,-3,-6,1,3,-10]],[[8,9,6,5,-3,-9,9,4,-2,-1],[5,-2,-1,10,4,2,-1,-9,2,-9],[5,7,-5,9,9,4,6,-6,9,-2],[5,7,8,4,-2,-6,-8,10,-3,5],[-3,-3,-5,7,-6,-8,-4,6,3,-3]],[[-1,-5,-9,4,-5,3,6,-6,-6,4],[1,-10,9,8,-3,8,-9,3,-7,1],[4,2,9,-10,1,6,7,1,-3,-7],[-10,-10,-9,9,10,10,4,-5,-1,10],[2,-6,-4,-5,5,-3,9,6,-8,4]]], dtype = "int64")#candidate|8505|(5, 5, 10)|const|int64
bop_8506 = relay.maximum(var_8504.astype('int64'), relay.reshape(const_8505.astype('int64'), relay.shape_of(var_8504))) # shape=(5, 5, 10)
func_5178_call = mod.get_global_var('func_5178')
func_5179_call = mutated_mod.get_global_var('func_5179')
call_8510 = relay.TupleGetItem(func_5178_call(), 0)
call_8511 = relay.TupleGetItem(func_5179_call(), 0)
func_7178_call = mod.get_global_var('func_7178')
func_7180_call = mutated_mod.get_global_var('func_7180')
call_8522 = relay.TupleGetItem(func_7178_call(), 3)
call_8523 = relay.TupleGetItem(func_7180_call(), 3)
func_6460_call = mod.get_global_var('func_6460')
func_6463_call = mutated_mod.get_global_var('func_6463')
const_8527 = relay.const([[-6.473461,2.751669,0.943402,-4.610490,7.866980,2.076335,-3.733339,-3.655157,6.023314,-9.001573,-1.051210,1.008546,3.574764,6.173374,-5.752199,-8.863978,-8.196017,7.629448,-9.518870,-9.360892,1.491582,7.261189,7.041865,8.230784,-2.556573,4.872696,8.548975,7.473023,9.538096,-7.854882,8.089284,-5.126189,0.595252,2.353085,6.424640,5.441507,8.463232,0.797233,-1.403741,4.696576,-1.179560,-6.237402,-9.313730,8.244398,-1.039142,9.887329,-9.027288,9.233167,-1.228087,-5.447865,-8.791545,-2.851171,-1.153618,8.284034,-5.119010,1.611279,6.858395,5.957800,4.412462,5.647459]], dtype = "float64")#candidate|8527|(1, 60)|const|float64
var_8528 = relay.var("var_8528", dtype = "int32", shape = (847,))#candidate|8528|(847,)|var|int32
call_8526 = relay.TupleGetItem(func_6460_call(relay.reshape(const_8527.astype('float64'), [60,]), relay.reshape(var_8528.astype('int32'), [847,]), ), 6)
call_8529 = relay.TupleGetItem(func_6463_call(relay.reshape(const_8527.astype('float64'), [60,]), relay.reshape(var_8528.astype('int32'), [847,]), ), 6)
func_7442_call = mod.get_global_var('func_7442')
func_7443_call = mutated_mod.get_global_var('func_7443')
call_8550 = relay.TupleGetItem(func_7442_call(), 1)
call_8551 = relay.TupleGetItem(func_7443_call(), 1)
output = relay.Tuple([bop_8506,call_8510,call_8522,call_8526,const_8527,var_8528,call_8550,])
output2 = relay.Tuple([bop_8506,call_8511,call_8523,call_8529,const_8527,var_8528,call_8551,])
func_8553 = relay.Function([var_8504,var_8528,], output)
mod['func_8553'] = func_8553
mod = relay.transform.InferType()(mod)
mutated_mod['func_8553'] = func_8553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8553_call = mutated_mod.get_global_var('func_8553')
var_8555 = relay.var("var_8555", dtype = "int64", shape = (5, 5, 10))#candidate|8555|(5, 5, 10)|var|int64
var_8556 = relay.var("var_8556", dtype = "int32", shape = (847,))#candidate|8556|(847,)|var|int32
call_8554 = func_8553_call(var_8555,var_8556,)
output = call_8554
func_8557 = relay.Function([var_8555,var_8556,], output)
mutated_mod['func_8557'] = func_8557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2049_call = mod.get_global_var('func_2049')
func_2051_call = mutated_mod.get_global_var('func_2051')
call_8568 = relay.TupleGetItem(func_2049_call(), 0)
call_8569 = relay.TupleGetItem(func_2051_call(), 0)
output = call_8568
output2 = call_8569
func_8575 = relay.Function([], output)
mod['func_8575'] = func_8575
mod = relay.transform.InferType()(mod)
mutated_mod['func_8575'] = func_8575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8575_call = mutated_mod.get_global_var('func_8575')
call_8576 = func_8575_call()
output = call_8576
func_8577 = relay.Function([], output)
mutated_mod['func_8577'] = func_8577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7793_call = mod.get_global_var('func_7793')
func_7794_call = mutated_mod.get_global_var('func_7794')
call_8588 = relay.TupleGetItem(func_7793_call(), 0)
call_8589 = relay.TupleGetItem(func_7794_call(), 0)
func_8029_call = mod.get_global_var('func_8029')
func_8030_call = mutated_mod.get_global_var('func_8030')
call_8590 = relay.TupleGetItem(func_8029_call(), 1)
call_8591 = relay.TupleGetItem(func_8030_call(), 1)
func_5878_call = mod.get_global_var('func_5878')
func_5879_call = mutated_mod.get_global_var('func_5879')
call_8601 = relay.TupleGetItem(func_5878_call(), 0)
call_8602 = relay.TupleGetItem(func_5879_call(), 0)
func_807_call = mod.get_global_var('func_807')
func_810_call = mutated_mod.get_global_var('func_810')
const_8615 = relay.const([6,-1,9,7,-4,-4,6,-2,-6,-10,7,-8,1,-8,-2,1,1,10,9,9,-10,8,7,-8,7,4,4,-2,9,-1,9,10,-3,-1,-2,6,5,9,6,-7,-7,-8,10,7,-3,2,-2,3,-7,-10,5,8,-1,-6,-6,3,-1,-6,2,4,-4,9,-1,3,-7,4,10,3,-2,-10,1,2,6,-7,-3,-8,-7,5,7,5,-3,-7,-4,-4,-1,-5,-2,6,-6,8,4,-8,-3,9,1,6,-5,-6,-3,-5,9,-9,-8,-8,-8,6,4,-2,-7,9,-5,3,-5,-8,3,5,7,2,-8,2,9,-7,3,10,-8,-1,1,2,-5,6,-8,-10,4,-10,2,-6,3,-4,3,-8,4,-6,3,4,-2,6,1,5,-9,8,1,2,9,10,-3,-5,-8,-3,10,-9,-8,-4,-2,-6,6,-2,-8,-10,-4,9,9,-6,6,7,7,-10,-2,5,3,-7,-5,-7,5,10,-10,-9,-4,7,6,-7,2,9,-4,-8,-6,-8,-3,-4,4,10,-4,4,-7,1,7,-6,7,-10,10,6,2,6,8,-6,3,-6,-8,-8,-1,8,-7,6,-2,3,-4,-9,-4,4,5,6,-7,-9,-3,1,4,-4,6,4,-4,-1,7,-9,-6,-5,-2,-1,5,7,4,2,7,-8,-3,2,-1,-10,-6,-1,1,-1,9,5,9,2,7,-3,1,9,6,-5,-8,-7,-3,5,6,-6,-8,-1,-10,2,8,-4,-9,-4,6,-3,-2,7,9,-9,9,-10,-4,-6,3,-4,5,9,-2,-8,2,-5,10,-2,-3,3,-4,-9,-5,7,-4,10,-10,1,4,2,-1,-10,8,-1,3,-5,7,7,10,2,6,1,-1,-10,4,-10,-9,-5,2,-2,-9,4,-2,10,5,-5,-3,7,-1,-8,-8,-9,9,-6,1,8,4,10,2,-9,1,10,-2,-8,3,-7,6,-10,3,8,5,-6,9,-6,-7,10,10,-3,-6,-5,-9,-9,-10,10,6,-9,-5,3,-2,-4,5,8,1,-6,-2,-5,-3,6,5,9,5,4,7,-3,-8,10,1,9,-7,1,5,-2,10,4,-5,9,-4,-1,2,-10,1,4,-5,-5,7,4,2,10,4,-9,8,-1,3,-3,-6,-5,-2,2,-1,4,5,-10,3,-10,6,8,-9,6,2,9,4,-6,5,8,5,6,7,8,5,-9,-9,-5,-7,-2,-4,-7,-7,7,-3,1,-4,-9,-4,2,-4,2,-7,4,2,3,9,4,-6,-1,3,-8,-1,-9,5,4,-2,5,-5,-5,4,-3,-9,10,-8,-6,-3,10,-5,-8,-10,-2,-1,4,-5,-5,9,4,4,5,5,3,-8,-3,-9,3,-5,4,3,6,-8,-9,-8,9,8,-4,-7,-2,-7,8,-8,-7,-6,-3,-10,-7,1,-9,10,10,2,-1,-10,-4,10,3,2,4,-3,-7,7,3,-3,-6,-10,8,-10,-1,-4,5,4,3,-10,-4,-4,-7,-8,-7,-3,-3,-9,5,10,10,-10,7,5,-1,-6,1,7,-1,8,-7,10,6,-1,-9,-8,6,-5,3,4,8,-1,2,-5,-5,2,6,2,-3,4,5,-2,1,7,-9,9,2,4,-10,-6,4,8,10,-3,-4,-5,-10,-1,6,6,-8,-1,-7,-4,-6,3,-10,1,3,-3,10,8,-6,-10,9,-6,-2,-7,3,-5,6,2,-9,6,-6,8,8,7,-7,6,2,-2,2,3,-3,-6,-6,-4,1,8,-8,5,-2,-10,7,2,-10,6,-6,-7,7,7,-4,-10,-1,-2,5,-5,-10,-6,2,8,4,4,-3,8,-8,5,6,-9,-4,-5,8,7,-6,-7,-3,-10,1,7,-9,-5,-2,1,8,6,-10,-2,-3,-6,-2,-7,8,-3,3,2,-7,-1,9,-8,9,-10,6,-7,3,-8,-8,1,4,6,2,-1,7,7,-3,5,-8,1,9,3,-3,6,-7,7,8,1,1,10,-4,-4,-1,-9,5,1,7,-5,-6,-10,-7,6,-10,7,1,-9,-4,3,1,-2,-1,-10,8,9,-6,9,-7,9,4,-9,3,3,1,3,-8,-10,-2,1,6,4,-10,5,9,-7,10,-9,3,10,-8,10,2,6,2,3,-7,10,-9,-7,7,-3,-9,9,2,8,6,5,5,1,-9,5,-1,-5,10,-1,3,5,6,-4,7,8,7,1,-9,1,-7,5,-3,-10,-10,9,5,-7,-10,-9,2,-8], dtype = "int32")#candidate|8615|(847,)|const|int32
call_8614 = func_807_call(relay.reshape(const_8615.astype('int32'), [11, 11, 7]))
call_8616 = func_807_call(relay.reshape(const_8615.astype('int32'), [11, 11, 7]))
func_7194_call = mod.get_global_var('func_7194')
func_7196_call = mutated_mod.get_global_var('func_7196')
call_8619 = relay.TupleGetItem(func_7194_call(), 0)
call_8620 = relay.TupleGetItem(func_7196_call(), 0)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_8622 = relay.TupleGetItem(func_2881_call(), 0)
call_8623 = relay.TupleGetItem(func_2883_call(), 0)
uop_8627 = relay.asinh(const_8615.astype('float64')) # shape=(847,)
func_8226_call = mod.get_global_var('func_8226')
func_8227_call = mutated_mod.get_global_var('func_8227')
call_8639 = func_8226_call()
call_8640 = func_8226_call()
func_4675_call = mod.get_global_var('func_4675')
func_4676_call = mutated_mod.get_global_var('func_4676')
call_8655 = relay.TupleGetItem(func_4675_call(), 0)
call_8656 = relay.TupleGetItem(func_4676_call(), 0)
output = relay.Tuple([call_8588,call_8590,call_8601,call_8614,call_8619,call_8622,uop_8627,call_8639,call_8655,])
output2 = relay.Tuple([call_8589,call_8591,call_8602,call_8616,call_8620,call_8623,uop_8627,call_8640,call_8656,])
func_8660 = relay.Function([], output)
mod['func_8660'] = func_8660
mod = relay.transform.InferType()(mod)
output = func_8660()
func_8661 = relay.Function([], output)
mutated_mod['func_8661'] = func_8661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2444_call = mod.get_global_var('func_2444')
func_2445_call = mutated_mod.get_global_var('func_2445')
call_8677 = relay.TupleGetItem(func_2444_call(), 0)
call_8678 = relay.TupleGetItem(func_2445_call(), 0)
func_3845_call = mod.get_global_var('func_3845')
func_3848_call = mutated_mod.get_global_var('func_3848')
var_8688 = relay.var("var_8688", dtype = "float64", shape = (10, 66))#candidate|8688|(10, 66)|var|float64
const_8689 = relay.const([-9.710946,2.173877,4.261664,7.825254,-8.137300,5.513606,3.629476,-4.263296,-6.643844,9.833004,-3.200598,-2.460287,4.803732,2.738999,0.453557,-3.495565,9.815628,0.172611,-5.920557,-5.504493,-6.075042,-1.131785,-3.795944,5.210993,3.832879,9.806699,-5.840946,-5.937441,-6.998153,-4.234559,-1.725905,1.264459,-2.658818,-5.980600,-0.539940,9.941979,3.898122,-1.654962,-7.516623,-6.662263,-2.966207,1.924597,2.042067,-7.398059,-2.914952,2.487139,-6.954631,-6.571134,-8.349105,4.573198,2.017783,8.038153,-8.174387,-4.945347,-9.435063,-6.382433,-7.714822,6.423653,-1.228700,3.816537,0.265929,6.829115,-1.337961,-0.297665,2.403287,3.643090,8.226003,7.634810,-6.619762,-8.481724,-2.729912,-9.204781,3.682058,-8.644076,3.531675,-7.769730,-8.459749,-3.338080,2.919606,9.562838,3.343696,2.375186,-2.890080,-6.354818,-5.792028,3.966346,-3.995992,2.549809,6.731589,0.941591,-8.892211,1.536360,4.748427,2.683005,6.918735,7.405468,8.605478,6.503200,9.612659,-0.292751,-8.237383,-8.930104,8.758295,-5.264706,2.213066,-1.831392,8.759889,6.433980,3.654684,3.309206,7.697182,6.034429,4.271641,-7.819682,2.676438,-3.916930,-4.208906,-6.311602,7.193156,8.637491,-5.583022,-0.593294,4.618698,-2.299447,-4.298432,2.239999,9.202841,-3.377429,8.357005,9.193729,6.979291,9.951632,7.200770,-5.314142,-2.660643,3.273164,9.549417,7.131961,2.432406,3.658896,2.840356,-6.402995,-2.026068,-4.004984,0.722918,-3.222977,5.552730,6.521762,7.389589,0.582808,7.146936,-1.978669,-4.229752,0.100618,4.571528,8.555375,-8.140476,4.015556,-0.498987,-2.447216,-2.057234,1.559263,-3.746444,-1.170241,-5.964270,-4.107498,-8.545112,-7.870188,-9.838701,2.518942,-5.318019,-6.635248,-4.932948,9.732959,1.556500,-3.173060,-9.925028,-3.886621,-7.434288,-2.397375,-0.518149,-4.984090,5.642896,-2.435082,1.526958,-5.365222,-2.316022,-4.088030,-6.246833,-3.998855,0.870082,9.563874,-9.595728,4.621674,-4.448414,0.288388,-3.998351,-4.047002,-3.080903,7.294943,-6.924396,2.725981,-2.136374,5.903043,-5.358090,9.598716,-6.758346,2.188314,-5.312229,-6.044239,9.180510,8.339234,3.961059,4.500179,-8.369417,6.310783,-4.340960,-0.699341,-3.873283,-3.997651,7.924847,1.853983,-5.997293,-0.643658,0.699335,-1.436280,-2.967156,-6.136761,6.334817,8.026021,-6.654383,-0.244823,3.985295,6.138602,-4.157183,-4.356123,9.291949,7.790950,6.773698,-1.654616,-1.941179,5.480032,8.902230,7.559626,2.370817,-8.295172,8.580670,3.116925,2.511279,6.095848,-9.374594,5.868082,4.559511,8.194688,-0.516168,3.686586,-4.875610,3.594624,-2.484452,-8.895030,9.449598,5.037522,6.266389,-5.912004,3.116345,-8.059487,2.465091,-6.061793,4.336765,4.243626,9.800340,-7.285183,9.124092,3.690727,-2.764250,-1.452737,6.307856,0.011865,-6.305715,8.424695,3.026570,9.804240,-1.398170,4.474812,4.269407,0.792809,7.688425,6.546662,-2.555433,-4.248235,-9.003213,-2.386537,-1.515070,4.223011,7.254082,-8.936527,-8.050687,-6.559066,5.314027,-0.344713,-7.235893,-5.662471,-1.311524,0.228733,-1.254196,6.759473,-5.396834,-2.306773,6.078849,5.059277,8.972281,9.720727,3.970719,-3.771285,4.041410,2.471509,-6.458902,4.246200,1.107337,6.191664,-3.145356,0.289997,6.472396,7.853196,6.303180,6.715129,4.526206,-7.237262,-1.484721,2.567185,-2.363496,-5.565127,-1.076916,1.831943,-9.256930,-9.951256,9.103888,6.090493,5.188184,-2.491694,6.636099,3.074658,-0.329936,6.979234,-4.928439,5.835205,8.152530,-7.834605,1.997843,-6.150061,-6.432885,7.531220,-0.177433,-9.013009,3.115735,-8.356881,0.173451,8.817490,0.286693,-1.390056,-1.692850,-1.264937,2.780578,4.452176,-9.509355,-4.736771,-9.171922,1.902512,-4.645437,0.693817,-2.511250,-1.225960,1.633491,8.704236,-0.856674,1.543551,3.667191,1.082506,-3.056237,-5.381632,-7.405704,7.623977,-9.548455,1.153972,7.043295,-8.782316,-9.967981,7.662672,1.214693,-5.358706,-0.020298,-1.348857,-2.561062,0.659216,-4.377357,8.733744,-3.835007,-6.845213,2.338639,-2.082030,-6.253471,-4.918449,1.525243,-0.443185,0.450877,1.995171,-5.398640,4.785558,8.564268,1.705160,-6.893140,-2.153346,-4.436729,8.694019,-7.176269,-2.973309,6.465558,6.638877,-5.083817,2.575089,-7.738311,3.758114,-4.340036,3.913313,3.575674,0.929982,-8.678962,8.502096,-5.731360,-4.262549,-5.129384,4.593928,-7.680198,-9.707189,5.608670,-2.719599,-6.626650,-5.828310,-0.676662,-6.101094,2.347080,-0.508270,9.654294,-3.946827,-0.522455,-1.589505,2.377598,-3.122201,-1.438890,-2.572952,-8.891019,-9.855747,-4.503699,9.227890,-1.847595,7.334061,-8.538799,1.484366,4.740266,3.884842,8.404051,-2.818090,-8.759236,-0.924428,1.805590,-9.744627,8.417185,7.423110,4.702437,-3.058957,-0.069516,3.207218,3.457330,2.159731,-9.309429,1.201865,-6.911478,-3.109591,-5.891818,-0.821057,2.489387,-0.079547,7.146260,0.609479,-0.068771,-8.623802,2.147272,6.011319,4.651276,3.070484,-1.350760,5.022116,-6.288672,4.165627,-3.847501,-7.798335,-9.758102,-5.567490,-4.021719,-3.302616,9.350697,-6.416439,3.288008,-1.118406,-3.054548,-0.933123,-6.766059,7.274230,-2.404178,4.007485,-9.436270,-5.963459,-2.444015,-4.462009,-7.636026,-2.809039,-2.611982,-3.588598,-0.957910,-1.365755,-6.475397,7.891197,-1.096774,5.785058,4.357865,0.997251,2.713465,-4.868292,-6.791938,-7.905612,-0.968162,-6.462262,9.912477,-4.237410,5.388705,-8.526383,8.069089,-9.881099,4.691458,-9.759210,8.269394,-2.721120,-7.354127,-0.242458,-5.261768,2.024438,4.451099,5.703809,5.003054,8.906847,-2.388501,-6.056555,1.141193,3.865503,8.130589,-0.723826,3.607089,1.393939,9.891208,-8.497635,-7.731306,-2.390467,3.985787,7.453335,0.058951,-7.918105,-5.315624,-0.745257,1.803583,-5.130369,7.027545,8.336011,-7.961954,-2.978931,3.088331,4.858255,1.525580,1.285742,1.205118,2.452568,4.906989,-2.606392,-8.671945,-9.401423,-2.139141,-5.335686,1.689729,-4.573369,-6.384091,2.913158,3.242334,-9.108057,3.803617,3.634259,-8.813768,1.923436,-8.500307,2.797166,-5.189538,5.567578,3.778440,2.190608,5.378138,-2.014290,-0.595691,4.560374,-3.136863,-9.544365,-8.277154,-4.605023,-9.611733,-9.609458,2.972584,-2.133558,5.544293,-4.756050,5.288549,0.439523,4.777268,7.855035,-1.893672,8.800794,-1.279665,-4.552331,9.860337,0.037930,-6.956218,1.520407,7.685400,-6.492715,4.136932,3.792620,-8.587248,2.525617,-8.917878,1.366670,-1.577359,7.391049,7.873796,3.388959,-1.096167,-2.592641,-8.113593,-9.733427,6.730148,0.364096,7.816535,-4.088613,0.414030,6.800204,-8.105549,-1.898362,5.202702,3.759665,3.482789,-1.748313,1.450630,2.874716,-8.770766,0.345859,-3.580098,-6.010809,-9.935224,3.993317,-8.132035,2.690612,9.988149,1.297087,-2.107519,2.600014,6.638394,1.839584,0.566833,8.534740,2.208720,1.939263,2.454104,1.378448,-3.823003,0.114429,-7.131566,2.918541,6.924782,-9.396017,2.463843,5.867844,2.839154,5.778752,3.933678,-8.819823,-6.347688,-5.722406,0.182313,7.925645,-8.325129,5.549838,4.026364,4.980301,1.792769,-7.703061,8.563576,-8.388195,5.606602,3.485443,-1.022807,0.705652,-2.856425,-6.182735,5.560087,2.703819,-1.860186,-5.662695,-0.927733,-3.181627,-4.259361,-6.683782,0.076937,-6.835651,8.471925,9.363159,-9.610138,-7.478450,0.050213,-9.055415,-8.192150,-6.957428,-5.185050,-4.526340,-3.016756,9.963630,-0.478074,7.388566,-1.435172,-9.774116,5.938864,0.096601,-9.969155,-6.525212,-3.146555,-9.469347,7.778392,6.782446,-2.536581,-0.892867,0.829038,2.623350,6.021062,8.751078,-9.983152,1.607384,4.645939,9.497422,-3.966794,1.377984,9.830802,4.850100,2.290475,-1.618705,4.253804,-7.147333,-3.131182,-8.692712,-1.356604,9.881732,0.062393,5.622497,2.519894,-5.628234,-2.135371,-2.762951,5.785373,-6.331715,6.328055,-2.770082,6.273155,0.063820,-9.403053,-0.067454,5.803620,-7.505250,-9.419516,6.901028,-6.267141,-7.636485,-2.797398,-9.110614,-1.657303,-7.883206,-4.710092,-6.334658,7.321425,2.211061,5.868002,1.126710,-4.367702,7.583479,9.121240,-3.256050,-2.110228,-3.740347,-6.419310,3.064511,-4.544876,-5.802776,-4.392124,-2.750937,-9.438583,-3.152594,5.621778,-4.964781,5.860495,0.802431,-4.853394,-4.955039,-6.904137,2.836296,-3.677814,9.548112,-2.278517,0.393824,9.118618,8.230443,5.027775,7.979418,7.907156,-1.679109,-1.086025,1.737156,-4.856104,8.851046,-4.012665,0.630831,9.841519,2.462030,-6.738267,8.719083,9.167544,6.994510,-6.330647,3.676374,-3.909104,-1.384584,9.432827,3.602606,7.386402,-5.905773,-4.342216,-7.079309,6.267419,4.994111,-5.109788,3.788928,5.446091,8.658001,1.847754,6.008064,-2.942347,-1.626605,3.268615,6.129508,5.989579,7.730945,3.773174,4.025627,6.632414,-6.612250,6.052377,0.191313,-7.533578,-1.497794,-6.532200,1.613002,4.253556,-9.042055,-1.748195,-0.793023,-9.314785,5.493545,8.004637,-9.183238,6.205943,3.726575,-4.405267,-8.681795,4.148066,-6.491313,-5.921431,-5.077593,-9.097537,9.348132,9.452582,-4.417843,2.786155,5.784123,-0.838822,6.367750,5.883680,7.008766,-3.318425,-8.831834,-9.119762,2.615976,5.048023,4.141399,-4.177967,-0.312764,-8.276054,3.865986,-0.815052,-5.672595,-6.715528,-6.065909,-5.624477,2.675170,4.453576,-4.899202,1.980123,3.186096,-8.029744,-7.170573,1.800838,-1.663585,7.212405,4.521337,-6.967029,-7.851497,4.098647,-7.054252,-4.886630,-7.590354,-8.115631,-0.862168,-7.013784,-7.072906,-8.170105,-1.735050,2.561494,3.970138,-9.327596,-9.532751,-4.367182,-4.299102,9.936099,-0.446395,-2.035116,-0.469186,8.470119,-4.520976,-7.832269,-8.246746,8.995894,-2.130974,8.932430,8.886926,-0.158332,8.527173,8.072658,-4.030585,-8.520767,-3.119199,-2.516691,7.711951,7.210212,0.123053,-0.395457,-9.792647,-8.758828,-3.106284,-4.328632,-4.961810,6.771998,-1.400723,3.181717,-0.153207,0.616381,-7.195081,6.632657,5.724064,-8.260868,-7.166419,4.283585,-3.205655,1.881880,5.062867,3.674911,-8.265209,8.125024,2.515306,5.739981,3.267452,-9.065620,-4.876515,9.051804,9.311904,1.762259,1.978211,-6.096991,-8.444211,-5.471749,-3.435393,6.574419,9.922832,2.439790,8.662290,-5.757646,2.444070,5.073116,-0.022126,4.903079,-2.805776,7.006287,6.625168,6.373859,6.793898,-2.963117,4.883727,-0.858504,-2.857087,9.130606,-7.232939,-0.741458,7.001938,-9.414577,8.449481,3.954377,-8.260810,5.146017,-4.840464,7.551695,-1.933488,6.712652,-9.215910,-1.981996,4.417313,-3.177633,6.804373,4.706587,-6.454992,-4.772452,-5.446604,9.859644,-5.812564,-6.573539,-5.593094,-7.651285,0.338404,-1.783649,9.111243,3.619802,3.175518,0.425943,-0.087937,9.679998,-2.132491,-3.926714,6.213309,8.114475,-5.334862,-1.524137,7.872045,-8.738554,7.922532,-8.244801,9.257649,0.008030,-4.675027,-8.986636,-6.165583,0.881280,9.216717,2.900134,-8.030571,9.429887,-0.267041,9.697811,-9.007489,2.142941,-0.039306,9.954067,1.395197,-0.796742,4.072762,-8.195205,-4.188783,-1.699158,-0.644293,-0.878078,-7.574792,2.441626,-3.577758,-9.879933,-4.839456,-9.049619,-1.487373,3.430661,-6.312082,4.837076,-1.886504,8.854596,9.176306,-2.985721,4.781801,-0.257284,-3.970482,0.454288,-8.750852,-8.045645,8.919482,-6.361065,-1.754416,2.720121,3.001761,-2.501144,-0.931674,8.227911,1.728663,7.231534,-8.229536,-1.917569,-3.913056,4.407492,0.074141,4.460690,-4.959014,-8.200842,1.593975,-8.710868,-2.205336,-7.586904,-4.511552,2.701951,-8.382424,1.115136,-7.087751,1.162261,4.514716,-6.949329,-4.219144,6.300100,2.296636,3.604884,7.484052,7.309651,-6.915861,-4.596540,1.417379,-9.285454,4.014165,6.868119,2.368136,-5.923610,0.927551,-4.090924,-0.725075,2.846593,1.120267,3.550961,-5.570978,4.583492,-3.594659,8.373272,1.526250,9.211645,1.275368,-9.436821,-1.215945,5.559351,3.487477,5.388817,6.784492,3.612725,-5.735508,5.163456,-2.802672,7.754013,7.647620,-3.068170,9.248772,0.863574,-5.197821,4.931866,-3.202222,1.918469,-8.116873,0.132150,0.892025,4.413535,7.547228,-3.212767,0.137799,2.659483,-0.091211,4.365314,9.471275,8.022124,-3.923608,-7.681790,6.101759,5.872278,5.773337,-2.908913,0.646875,-6.866517,-1.438568,-2.481496,-7.708842,-3.115594,-0.108215,-9.477663,-9.544467,7.526317,6.042936,8.116354,6.215571,-5.271717,-4.760942,2.410977,-3.497304,-7.818899,-8.426459,-8.122496,-8.640281,-6.181204,-8.146306,5.077415,-4.382477,-8.646987,-2.758730,-1.788632,-6.232816,-1.710401,3.215849,-2.779899,6.135867,4.428456,-4.882904,1.964357,-6.384756,4.577611,-3.472029,-5.237596,2.527759,-8.871489,-3.953882,-8.785508,-9.838972,7.733817,-3.546698,6.683262,8.115480,-2.957796,5.916034,-5.808424,1.450565,-9.510334,-8.611914,-9.864650,2.984298,-7.290182,4.417070,-2.555461,5.829206,-4.499956,-2.031999,-8.925443,-9.619678,4.088171,-2.382847,8.827548,0.843248,0.854642,-7.621435,9.940542,1.293872,-4.048465,-3.049013,-2.130196,-0.882073,-8.512645,-6.669347,-0.990338,4.232470,-1.907325,-7.689578,4.252752,-8.425232,6.747372,-8.764588,-1.814703,-8.351743,-5.253833,-6.176722,2.547163,3.908847,4.206129,-9.023633,-6.954402,6.179552,6.772124,8.790979,7.546652,9.160139,-5.156712,3.683547,0.128851,4.927822,3.384452,-9.940349,2.798320,-9.259304,-2.135645,-2.618302,-5.876644,7.682528,8.396317,-6.833289,-7.913545,-1.052341,8.630642,-0.103288,4.047760,-6.064349,7.073567,1.630187,8.551192,2.978323,-0.934983,-3.572517,4.827826,-5.395804,-4.584304,0.027249,7.437908,-5.520721,9.623285,7.512574,-9.389620,0.930903,3.531381,-8.765339,-2.283709,-7.024946,-2.769063,6.930533,-9.106717,-8.430425,-0.475064,-9.218702,5.197319,-9.354133,1.043255,-3.941984,-5.428117,7.889773,-3.810678,-0.304605,1.959727,-3.899404,0.739683,2.665865,5.319009,3.350404,2.695511,3.027349,-8.692072,4.280112,-3.268992,0.056883,-2.038409,-0.955304,8.703399,2.724731,1.970027,-2.001240,-1.285038,-9.619794,6.130049,8.446699,5.692028,-4.659862,9.458368,1.902694,5.656558,-4.870081,1.913195,-7.210879,5.806151,3.813555,5.835575,9.291048,1.542581,-9.479869,6.356484,1.222539,-3.127388,-1.405607,-1.418472,9.434285,6.385535,3.566666,-2.454083,7.134203,8.951569,-1.293952,-2.598806,-6.790886,-6.132338,-8.873207,6.183149,-0.564903,1.145614,8.783243,2.010621,9.899175,-8.774251,6.242406,3.475176,-9.556305,-6.833593,7.143840,-2.827803,-9.288133,-5.577861,7.662428,7.476051,-2.648351,-1.347920,-6.783708,-1.602362,-6.771372,-1.020675,-9.554848,-2.564423,-0.221105,3.237953,1.536126,-8.473975,-9.634985,3.763038,-7.118814,-6.598791,1.164895,-0.450137,-2.820177,-6.218183,2.267480,-1.781981,-7.994891,-8.449678,8.471558,-4.445915,5.606890,1.643300,-8.307540,2.026534,9.213808,5.547967,4.857034,-5.656406,-6.536007,-8.111027,3.791953,8.029652,-8.177367,-1.095008,-5.837482,-1.495270,7.866532,5.540043,-4.785453,-8.711884,-6.479367,6.967360,8.684882,6.295380,-1.877306,8.505863,7.404486,3.683815,-0.769196,1.708521,-4.922081,3.777036,9.703696,8.388937,2.655602,3.549171,0.157680,1.925737,-9.879446,0.258938,6.090003,-3.617068,5.411081,-7.585652,-6.186595,-3.193565,3.957999,-0.516086,9.002828,5.223018,-0.137491,-3.247870,7.442255,-4.118757,2.002422,-6.534639,4.595563,4.061169,-0.074593,-7.485328,8.688696,8.510991,-2.629042,-8.091154,-4.288464,5.351175,-3.663539,-4.487154,0.790912,-8.092098,-8.302521,1.728918,0.486704,8.350402,-3.818699,-2.891622,-8.440534,8.406105,-2.889258,-3.172252,1.969519,9.662680,-7.927350,6.919884,-6.721187,-4.092446,-9.105843,-4.951675,-4.866006,4.036883,-4.376363,-9.691377,6.520745,6.018767,3.077748,-9.608351,3.235310,6.211858,-8.401730,-7.173133,-1.028023,6.028410,-9.572503,-3.906439,5.686863,-6.336450,-2.241598,4.532263,-4.409783,7.849438,-3.137792,-5.115262,5.269786,3.640972,-7.703829,-5.367125,-1.480798,2.902405,-2.619640,9.470379,2.349755,3.143423,9.581596,8.750670,3.045415,1.049160,9.425687,-4.577146,6.523650,-0.289400,6.196315,-0.055121,-6.987071,-2.162989,-3.074262,1.621991,5.645081,5.090536,8.830513,-3.716794,3.021261,-2.373183,2.463289,7.920324,1.838957,-6.654578,-2.835491,-3.182657,-4.422299,5.397574,8.861833,-4.177349,8.957310,6.878974,6.899286,-7.721161,9.453001,8.368608,3.904900,-8.419748,-4.543152,6.147212,6.922546,4.484235,-1.951998,-8.301497,6.878334,6.043333,-8.306945,9.564463,-8.382330,-2.867942,0.383156,9.573465,-6.390480,3.065370,-7.278592,-0.161881,-5.004768,-5.428025,-5.556041,-2.624401,7.679289,8.929756,-0.676192,6.770269,-8.515392,5.370380,6.528102,-5.508195,-3.280497,-8.073569,-5.890449,-6.896597,4.353289,4.334028,-3.509423,0.591940,0.836504,5.285727,-7.469522,0.161267,9.785162,-5.640369,1.202024,-4.706233,-7.642137,-4.881262,4.842224,9.778422,3.831858,4.280251,7.823550,-8.046814,7.186184,-9.301995,-5.130073,-9.354429,-0.736751,4.788418,8.655573,5.377404,-0.009180,-8.756211,8.130246,-1.309354,-3.302762,-3.714261,1.818686,9.986777,-1.208864,-8.275506,5.087764,-5.458198,3.224980,3.790846,-3.087393,-5.356826,-2.505916,-5.534548,-5.622813,8.161014,-7.535772,-2.590873,-2.258407,-9.070958,-0.774722,0.238752,7.594183,7.697039,4.915073,6.583895,-5.391489,9.721340,-1.145762,-5.271362,-9.216211,-0.159420,6.679328,-8.877682,-0.995059,-4.801975,5.223297,-2.449430,-8.195096,9.669870,-7.058096,2.830790,-3.068476,8.968652,-8.148579,-7.702792,9.391270,-8.573608,8.869644,-0.481489,3.614916,-2.550003,0.270502,-5.132830,6.451189,2.937688,-9.412538,-2.489012,7.442196,-0.467124,3.513571,9.456885,9.571481,3.990359,-9.167217,-1.636614,-1.962349,2.298394,7.397564,1.972233,0.594296,-4.945105,4.338737,9.757069,-0.382602,9.694383,-6.154522,0.147381,-9.671002,-5.686927,-4.322143,-6.239041,-0.450639,-9.807183,5.543361,-0.460505,7.237490,1.902302,8.761324,0.855325,-8.960445,7.862080,9.192670,-3.632903,8.722881,1.515983,7.143137,-2.106619,1.332604,6.855293,4.920409,5.103244,-1.589102,8.109225,7.253800,1.322722,7.015737,-0.811281,2.857933,-5.288504,-8.689234,4.578723,-2.946297,9.756523,-0.891907,-5.606962,-7.544963,-6.550836,-0.025532,-3.387561,7.774860,0.202171,-3.048708,4.952865,-0.729025,-2.672163,1.140364,-5.268112,1.553044,2.648333,-5.693804,1.575712,-1.072515,9.023595,-2.236935,-1.677693,-3.580363,-9.833069,-6.040595,-8.147166,-1.982018,5.038254,-2.450344,2.504165,6.310375,-3.898640,-7.588440,-3.126024,3.611862,-0.064434,2.790743,2.384958,-0.715980,-2.296041,-3.398004,-5.024358,9.021898,-7.730373,3.173645,4.546596,9.153527,9.251245,-6.669216,-2.650490,3.943249,0.048364,6.386826,-8.260697,-3.079363,-2.700793,-0.779381,4.925204,-1.220607,0.534627,6.588065,-3.126198,-5.999790,0.447943,2.363083,4.515168,-6.479389,6.143026,8.473314,8.520027,-8.420799,-6.096920,-0.641004,-5.041447,-4.743844,7.052797,0.501713,-9.175909,1.435802,-2.856336,8.256537,1.420046,-4.378242,5.136243,3.545721,2.939272,1.546456,-7.490974,-3.739152,-7.603690,-3.845274,-1.379287,-1.307638,-4.220494,-7.712750,-1.121601,-5.829717,1.097902,3.876753,-6.797749,-1.876485,-9.285921,-2.496274,2.728320,-3.398042,3.218371,3.822135,-3.009673,-4.139352,6.351472,2.311933,-7.025149,-9.389319,-4.542178,-5.136703,-2.633801,-0.642269,-3.420509,4.315064,7.118324,-7.208888,-4.506900,3.923320,5.887753,4.730233,-9.296813,-6.150312,-3.860734,2.781111,-2.653177,-6.470306,-9.097283,-5.441295,8.887148,-8.607784,6.097910,7.416344,5.280924,-0.436546,-9.788541,3.773730,-4.705564,0.328343,-2.380388,9.556862,-7.519080,2.047295,-3.747347,-4.844076,1.583813,1.993754,1.998361,6.185236,0.541572,2.159254,6.845068,-4.918944,-2.133260,0.996190,-7.841767,-6.979401,-0.314387,8.531085,6.250475,-4.211092,7.162020,4.807774,-6.018326,0.689315,-4.035009,2.399861,6.815635,5.052861,5.454008,6.239869,2.504560,-7.519630,5.303204,-1.055357,2.557523,-6.096966,-9.630812,6.102232,-3.698584,-8.722500,9.234111,-4.272913,-3.063996,7.342635,-2.607847,4.408612,-6.159535,1.055231,-4.155589,-5.284255,-3.223512,-5.711678,-8.677809,4.947240,-0.295575,9.899637,0.377831,-1.950986,1.170946,6.157917,-0.200029,0.360712,5.513419,7.087092,-1.976686,1.656089,-3.118634,-8.235122,-5.219248,9.737828,6.930501,-4.386541,-0.495850,-9.765803,-5.217398,-0.623764,2.615380,1.644941,-3.234853,-4.287296,-6.804978,-3.376098,2.380384,0.069055,-4.623861,-6.318454,0.305000,0.017737,0.093548,0.244172,9.490429,5.767759,6.742170,9.922777,1.755084,4.130993,-5.341044,-4.552016,-7.832294,2.890078,-6.771297,-0.790531,-7.088511,6.511342,-4.415676,-8.981253,-3.089734,-7.123018,-3.194795,-1.975067,9.638509,-8.139485,6.852577,9.401060,-9.189924,-0.518353,-0.303521,9.862500,-1.001968,-4.550099,8.709104,0.216615,-8.173047,-6.459933,4.420448,-0.159872,-0.748316,-8.380675,2.707848,7.146026,-6.041097,-9.094208,-1.409344,-6.427260,6.037711,3.073017,6.281712,-8.013085,-9.029216,-1.506957,8.875490,-0.493716,2.749411,9.474214,-5.166491,8.854027,0.174033,7.896252,5.519082,-2.981931,9.218218,2.946843,-1.995644,-5.130779,-8.360853,8.531766,-7.923338,9.878132,-8.706132,-3.280215,7.984370,-6.856915,-7.952879,1.395250,4.146161,-9.544465,6.976719,8.939231,9.925787,9.583463,-9.092410,-3.230838,-0.743013,2.465876,-0.265302,-2.002048,7.739937,-0.389103,-7.550866,1.711586,-0.015835,-5.569034,3.576839,2.838082,-6.077183,5.784141,3.042103,1.655327,0.512723,4.245773,-7.724441,-6.367022,-1.870919,9.213455,-8.870844,-1.658116,-5.432502,-1.101976,-6.806469,9.138823,-2.054212,6.533172,-2.996816,-9.400288,8.067242,5.482313,9.634322,7.862191,0.514583,-9.819309,7.860154,-7.349467,-5.733330,-3.663941,-1.615078,4.573799,-2.571843,0.140095,5.883064,-6.822081,3.181308,-9.796201,9.070102,-3.584074,2.725629,-9.794359,8.025010,-4.301481,-6.359468,-1.909621,-6.261872,8.520604,-8.008748,1.933153,-3.543277,6.999210,-2.957163,-9.163324,0.061961,-0.011370,-2.690455,-8.859831,2.753420,1.765856,7.326578,-5.334107,8.759943,-1.386547,-8.859563,4.478422,7.407026,-7.402857,-7.491180,-8.857605,8.500626,-1.783648,3.214658,9.179379,-3.525536,-1.537714,-2.084175,4.891317,3.067273,-6.176077,-3.861580,-0.204434,-1.715782,5.413795,-6.278174,-1.404971,-2.438862,4.154746,3.899892,-5.983958,8.416035,9.038027,9.935530,1.280879,-0.865832,7.060444,6.433720,9.803307,-5.942178,-0.995517,-8.634044,3.377883,-1.790504,-9.226178,1.229733,7.100677,-8.580213,0.391433,9.205924,-5.514542,-0.340565,-0.419808,2.833689,6.223797,-8.827047,-7.562783,-5.424650,0.655036,-1.171322,2.561781,-0.479334,-5.098084,7.043538,3.877149,-0.411924,0.761810,9.069397,-0.889493,2.765909,-7.375371,-1.365150,-2.160592,-1.568479,0.539408,7.558384,0.308176,3.945395,-7.361307,3.374229,5.533677,5.018555,-3.668435,9.349499,-5.749093,-5.704455,-4.100463,9.515581,5.258847,1.502138,1.026559,1.034271,-4.395539,-7.895613,-3.131015,-4.549617,-6.424549,-4.018141,-1.477539,9.859038,-3.994993,-0.553995,-7.197536,5.826185,2.996208,-6.904925,1.769964,5.512930,-0.313395,1.116635,0.773872,1.553482,6.521923,-9.785752,7.138292,-7.101952,2.093554,-7.285647,6.790063,-8.116337,-6.299247,3.253948,-0.795688,-9.594800,-2.316087,0.437109,2.921012,5.454905,-4.010880,4.531109,-2.496965,6.813542,-3.293721,9.988706,3.784539,-2.563908,6.256671,-5.774313,3.312339,-8.074265,-2.618573,8.352894,-4.657356,-3.867934,9.756700,-2.097767,-6.528911,7.865395,-5.585986,-3.022849,-6.929472,0.549666,-2.945378,-4.245922,-6.933123,7.672099,-2.147463,3.608802,-9.811217,-9.433902,9.934735,4.110172,-3.340106,-1.317159,9.841719,3.551492,9.241488,9.599242,-3.998661,3.334950,8.716269,2.235744,-8.138637,-8.605599,-4.103043,-1.245755,-8.294695,0.921657,-2.943480,7.322018,-1.390298,-3.682575,6.069445,9.939504,4.601811,3.649198,-8.841558,-1.441368,3.641146,2.431559,5.138232,9.579182,6.643083,7.848798,-3.455590,5.149614,3.694847,-7.394986,-7.370648,-9.317378,9.112886,-2.936010,-1.292768,-6.170344,0.392932,4.757415,3.848544,-5.116688,-7.844182,-1.051709,-7.014421,0.227722,5.927407,5.675650,-8.764555,9.069305,8.287721,9.002517,1.306907,1.661893,2.222407,4.314597,8.601927,6.049399,5.124531,-3.949000,0.325215,4.882626,0.467234,-0.534098,-1.165807,6.487636,9.813834,3.949317,-1.274775,-9.192809,-5.842324,-4.135809,4.164699,1.465589,-6.176060,2.180638,8.735572,-8.702339,7.568902,-2.154053,3.870162,6.485353,-0.123693,0.542763,2.310095,-6.320761,9.261459,2.001086,-3.985675,-3.620013,-6.995280,9.251846,-1.760170,-6.886621,-9.778314,-4.869955,2.311246,0.084379,-8.660481,-5.307713,-2.706959,9.634145,-6.245439,-1.103663,0.409030,8.595890,-2.985890,-8.554343,-0.580321,-3.161316,6.952496,-3.575395,-3.819705,9.988332,-8.088752,-8.901743,-6.997558,8.855077,-7.859050,-3.278501,-5.647680,5.382526,-7.284297,4.468099,9.852845,6.205639,-6.169596,5.000488,2.087435,-0.190247,-3.447637,-8.738392,-5.901988,8.321872,-9.423662,1.773961,9.094400,5.372081,-9.969835,4.147718,6.441783,-5.994716,-4.767718,-2.144312,-5.054996,-2.318282,-6.692036,-1.797953,-7.869927,6.540605,6.504849,9.995998,-9.255078,-3.544098,9.130889,-4.479650,-1.084802,5.437029,-8.476266,2.362249,-8.601298,9.024399,-6.077670,1.186120,-7.956131,2.982665,9.416826,-8.542938,-0.350502,-3.143185,-0.101245,-9.315497,-6.466512,-7.669384,6.333303,3.923208,7.461988,-9.028759,-1.663203,-9.256176,7.524981,-3.113739,-1.046404,-3.607578,0.920071,-9.574160,5.878100,2.646723,-9.194654,-4.622480,7.377324,8.520741,-9.168015,-6.350265,-8.313713,1.001539,5.463285,-7.038406,9.186136,-7.526390,-7.535436,-4.509967,8.679890,2.609887,3.426638,6.492929,1.418635,1.010469,7.056653,1.532595,-6.931491,0.615205,-8.395858,1.656375,-8.067016,3.364915,8.633465,-1.137275,1.997511,-3.810330,3.750329,8.040595,6.788848,-0.719256,-7.367305,-9.793953,1.738361,-1.025047,1.298279,1.447109,0.082804,-3.765318,-2.565379,5.869007,-7.691505,2.724664,-2.150012,9.192255,5.531712,-6.610093,4.802023,8.844710,-1.816465,-6.765840,9.880227,6.061929,-4.882761,7.622582,-4.239706,-4.972853,9.128689,-2.070763,-5.325525,5.219277,7.439831,-0.567921,-4.380372,8.296710,6.660131,-2.589301,1.585645,-4.244758,-8.988711,7.973620,-1.028803,5.519200,1.162349,0.555336,2.235393,6.105197,-3.984560,5.311501,9.710989,2.683020,0.382667,-8.498981,8.139268,-2.499129,-6.681475,-2.012822,-5.794251,-8.228513,3.336287,6.187823,-5.513003,-1.376509,-7.441476,0.979165,-3.856731,9.612617,6.325073,8.408791,-2.997634,-2.999701,7.847436,1.759430,-0.361096,0.239858,-4.956209,7.516201,3.789609,8.999321,4.836135,-1.535193,-7.756275,8.981753,6.508410,-7.240327,9.657468,-5.096647,-0.332431,-1.057067,-5.277385,-8.753855,-6.164344,4.338924,8.637665,-5.662330,-4.167397,9.840321,-5.560093,-7.978941,4.909568,5.945607,4.409664,3.453687,5.873430,-5.053446,5.235685,-7.938468,-4.730052,1.891779,0.402727,2.056162,-1.380992,-1.152323,1.666392,-9.815139,4.203977,1.438037,-0.432166,-3.874990,-7.673843,0.414030,-8.534284,-0.891426,4.942007,-8.506498,3.421118,-6.430489,-6.504487,-6.670662,1.058023,-0.525867,-5.488557,2.511416,-7.745115,-9.278010,4.419100,-4.728946,-3.195523,-2.670920,6.038782,-1.120081,-5.270359,-8.103071,6.520116,1.744230,-4.353596,1.177335,2.623772,5.399393,2.216111,3.763926,8.095933,-0.553423,-6.188690,6.150865,0.667525,-0.710051,9.187038,2.606304,0.968488,3.081330,-3.850690,-3.822836,-6.350280,-5.107885,6.648038,-7.567748,2.306568,-2.828558,2.817458,1.766119,9.485133,3.165469,3.383012,1.952734,3.742193,-8.197444,-6.967646,3.880067,-6.345119,-3.743962,8.758881,-2.900192,6.664006,-8.657609,-0.187114,1.420814,3.503125,-3.555669,0.284771,7.083081,6.239660,5.460305,-0.518117,-6.108689,-9.463317,5.703526,8.128368,-0.740287,-4.999858,4.456508,5.421404,7.569348,5.995760,5.427397,3.518289,8.926344,-7.139350,-6.374329,-1.915080,3.657918,2.536255,-6.087554,-0.413258,5.241590,-6.929666,7.842497,-7.176866,-1.233998,9.991915,-0.941342,6.280798,8.848634,-7.453007,-1.476399,-4.621752,5.466982,-0.476980,-7.117097,6.462155,-7.312498,-1.560612,1.647935,-1.513192,8.305040,0.207175,-9.167967,4.894436,-2.542912,-5.961512,-0.784530,-8.844725,-1.765085,-6.616578,1.815786,5.745010,3.740313,7.005056,-2.119959,-7.632911,4.301037,3.837172,-0.705322,3.298401,3.867982,-0.981434,-5.848547,9.260032,5.271427,4.608209,2.574051,-2.398643,6.780889,7.900137,9.789987,3.180091,7.997440,6.431516,2.947551,-5.379887,-0.731918,1.482060,4.287077,9.453797,-4.869220,5.863719,3.224516,-8.164999,-6.184857,-1.603075,9.932017,-2.742948,1.428123,3.609007,5.828561,4.537146,-2.298906,-9.800914,6.192762,-5.637168,0.109655,-2.647016,-0.023722,8.268917,-2.337908,-6.605200,8.643665,4.113444,-1.266545,2.016112,-9.719655,8.077602,4.737651,6.282112,-7.306327,-7.923920,3.608860,-5.155763,4.691143,-3.595152,-3.920330,-6.492311,-0.082278,-8.425143,-0.497276,-9.974558,-4.799209,4.785185,0.510730,-5.434898,-5.380592,7.817613,2.167317,7.023889,6.863876,7.140322,2.613970,4.911613,0.158459,-8.770862,-5.006173,-1.977359,5.142919,-6.003527,-2.635362,-8.796347,-1.599005,1.671027,6.400875,-1.085454,-2.690885,-8.760366,8.586793,1.804332,7.408948,-6.302130,-5.939534,-1.415604,-3.630193,2.690184,-7.406889,-8.086489,4.006041,-1.611269,-0.391204,-6.219493,-3.801601,-2.305754,-1.310697,-7.536683,-4.112381,8.641589,-9.300624,-9.294040,4.167874,8.400739,2.337782,-9.559472,3.209823,9.508624,8.086244,1.367941,5.530621,-2.234740,0.887087,7.746251,7.911171,6.592372,4.362036,6.694420,7.677972,-4.834472,-6.759506,4.544623,0.702978,4.807248,-8.265703,4.300084,6.057016,-0.563844,-5.069470,-2.233673,-0.577237,4.130001,8.847408,-9.194294,-7.908595,9.314157,5.873469,-4.812553,5.687469,-4.317169,-9.717928,1.511714,9.708258,5.114683,-6.279855,8.327695,2.232971,-1.350406,9.953161,2.804725,0.329192,-7.891469,5.037381,0.600931,6.462139,1.155711,5.687600,2.311198,-9.829745,6.829853,-0.155218,2.271392,9.585303,-5.402429,3.181833,-7.429876,-7.344008,6.095991,-1.216036,-5.623070,-2.888043,3.508189,1.457174,-7.444137,8.498413,-5.038744,1.446280,9.306245,1.301704,3.283100,6.619797,2.735810,2.280322,-2.518587,4.420313,6.073459,-1.192694,-4.457313,0.296142,2.941851,-6.877280,-4.173135,5.032756,-5.250916,5.213212,9.340423,-0.397413,-3.891932,-5.863557,9.504117,9.613256,3.742837,0.389475,2.978339,9.971395,-0.885352,-8.488630,5.914376,-1.163801,-4.216347,4.662300,3.981458,-6.205413,3.580462,-6.278956,5.886938,4.634658,6.984212,-5.327389,3.977715,1.446366,1.495522,-2.021673,7.287260,-0.386685,-6.451251,-0.145339,6.912311,8.751253,5.268337,5.031727,-0.924482,8.548524,-8.372035,-5.646970,0.097935,0.576336,-4.984656,0.852841,-8.568708,1.638748,-1.382510,-5.923312,0.787053,-9.905225,4.135012,4.495298,7.709848,9.917525,-1.796022,4.174127,5.674317,-7.057149,2.290063,-3.801109,0.786328,-4.834635,7.209729,-2.667648,7.614733,5.144687,-2.232103,-1.700538,1.403482,6.613372,1.550060,-5.743657,5.125455,-3.823529,-4.903658,1.339945,8.252924,2.093238,-2.481513,0.172371,9.987265,0.506577,3.726059,1.748031,8.896016,-0.782144,3.815559,-5.931387,2.991696,6.408381,3.907026,4.238014,4.889837,2.949543,-3.335793,8.199534,3.124149,-4.718003,-4.628021,5.788999,-1.796764,-8.453819,-2.368987,5.774196,-4.820488,-7.927114,6.955549,-1.809787,-9.298740,-6.411826,-6.310195,-6.148871,-2.213653,-4.223432,-1.168914,9.402686,2.508008,2.303990,-9.652580,1.626086,3.029640,-0.090446,0.885838,4.461595,-6.265881,0.706615,5.866073,-6.015607,-5.899821,-2.465228,-1.352505,8.592037,-1.049999,-4.023675,5.590424,3.967277,3.438534,5.134201,-1.831467,-1.837573,5.239787,4.670403,-2.788025,-4.858735,-1.434524,0.363127,-1.514844,-0.911226,5.471247,5.620837,-8.164300,-9.872133,-0.724324,-8.478857,-8.504928,1.414969,-0.112637,7.569421,-2.624489,0.144484,-6.661838,-9.069228,-6.654055,8.464229,6.650638,-1.447764,8.097789,8.481730,5.321967,-6.142228,-7.612004,3.573963,-3.368349,8.652679,-7.792366,1.212536,-3.307611,-1.166905,-7.666349,-6.052711,-7.875303,8.287638,1.423591,-3.684260,4.412303,9.359123,-1.686035,-8.549404,9.545362,-1.093767,3.960151,-6.484745,9.950792,-9.650644,3.975598,2.324428,6.211367,6.920243,3.600937,0.254668,8.316975,-6.976485,3.255869,-7.204107,2.616875,7.690489,9.367874,-7.220283,-1.650229,-7.972883,5.415720,3.834500,5.930493,-5.932456,-0.393561,3.026906,-4.097863,-2.669849,-6.142115,-6.182034,2.040508,-8.082053,3.038196,2.304147,5.876395,5.052411,8.211169,-3.319253,-0.230815,1.808754,-3.830873,-0.017076,-5.719231,6.934492,3.712668,-9.436572,7.288130,5.217103,9.656290,-3.711243,0.286471,-6.921933,-9.173577,3.703816,6.920958,-9.102034,2.890000,-0.046149,1.757802,-2.393578,9.339068,8.024773,-8.346060,9.485557,2.074709,-9.140626,-1.926251,1.444686,3.195289,1.958431,0.864175,9.565701,-3.625318,-8.113278,6.015178,-1.136093,-4.682347,9.286126,6.586264,-3.748023,-7.577909,5.348740,0.553804,3.340592,1.593285,3.025101,-0.362843,4.154818,-6.654580,-6.600180,-8.622110,-2.069421,-9.177051,6.766672,5.817390,-5.553998,4.810571,-6.565191,-1.928057,2.705413,-8.994082,-1.873724,7.248971,4.847793,-4.212185,2.603037,-8.493120,5.918813,4.167142,-8.684998,-6.371830,-0.051290,-9.689962,2.618577,6.326777,-5.585612,6.131924,-3.272038,-3.646966,1.730749,-2.194046,-6.041754,-7.543852,7.903400,-8.686322,-8.792011,9.047316,-7.719814,9.452331,-6.481104,5.550715,-1.279992,-6.235339,8.177593,-8.266271,7.005894,-2.106023,-3.326722,5.579965,-7.448269,2.862688,-0.395618,-8.865935,7.226518,-3.588377,-8.352211,-3.322822,0.822144,6.935212,-6.009993,4.701338,-8.419146,9.131181,-4.387007,8.394780,-2.934288,-7.633381,3.468157,-8.954064,-8.202743,-5.265190,-0.771898,-0.678838,4.214905,-3.808843,2.049286,6.728447,0.774368,-1.289825,7.636243,8.204367,6.372364,4.061491,-6.870441,3.978959,-6.784787,2.559275,-3.643005,-7.664066,6.593469,8.042001,-2.637254,4.592202,5.874353,-0.523193,9.866181,2.879141,0.211616,0.161962,-2.143069,-1.139629,-3.886103,7.311027,4.233212,4.476658,-8.330542,-3.533922,1.237766,2.850016,2.974932,-8.849223,3.390530,7.335620,-3.726058,-0.429576,2.405098,3.610946,-7.562208,8.769894,2.116458,-6.014670,8.418294,-1.417280,-7.368055,-3.243227,7.608900,-3.469826,-3.169976,5.526422,-1.290302,4.628699,9.433743,-3.612300,3.291642,4.969222,-5.935875,-8.058073,-2.403926,-2.790189,-6.033990,4.647992,1.500462,-1.574425,1.092848,-2.802871,0.440069,-3.350192,8.650762,-4.155612,-5.536258,6.500080,-7.382214,-1.102256,-6.514242,0.661452,7.481752,8.370216,9.081742,-9.552071,7.616881,-0.799419,-3.520646,1.925146,1.668077,-2.653865,-3.352701,-6.199336,-6.992137,2.767050,-1.147544,4.938683,1.217094,-4.736122,0.549681,-9.366607,-3.653848,6.914470,7.105131,-1.231228,8.915266,-5.257898,-0.708915,-5.255557,8.675652,3.874271,-2.450109,-0.823657,0.892049,-8.308117,1.406110,-6.885745,-2.054281,4.923184,-1.823212,-7.837967,-0.809204,2.568881,-6.388713,1.919418,-4.581104,5.854922,-9.013621,-3.344561,-3.229504,-9.256481,4.947989,1.346036,-7.017323,8.722471,-8.482957,-4.137133,-6.244295,4.725539,4.430251,1.987132,-8.561360,1.674165,-8.318485,-3.065958,-8.757409,-9.489673,4.215760,8.991686,-3.773357,2.230149,8.270245,-5.001917,4.902559,-6.958273,-8.447298,-0.149994,-9.474978,8.588540,-4.169255,2.466535,-4.785811,-4.434737,-7.250047,-8.459664,6.536711,2.797097,2.173806,-9.310769,-5.519230,-9.110932,-1.741058,0.166694,-8.936603,1.585824,-2.777066,3.312742,7.477175,0.945383,-1.125216,-6.265205,6.489919,-2.713972,1.668744,5.450902,7.682558,9.591899,0.617295,-7.964460,8.016457,-1.208339,-3.711599,9.932697,3.845955,4.534286,-5.602741,8.402552,-1.681607,-3.965082,5.124671,4.415390,5.969534,-6.448310,8.563516,-9.249763,4.564073,-8.618003,8.214312,6.378458,-8.645352,-8.508274,-3.709759,-4.847630,7.078095,7.447484,9.733803,9.853438,1.740452,0.607293,-3.814533,9.771162,-9.067455,0.629689,9.895199,-5.986554,-3.777106,-3.149790,7.611187,0.830052,-5.703888,1.828189,3.986852,-1.062113,-4.423564,1.622055,-5.501142,-7.479679,-4.912680,-6.508733,-3.495825,-8.171167,8.780558,-5.247526,4.291432,8.466849,-6.338728,5.642231,9.638085,-6.255866,4.894392,-6.655432,-7.243845,-8.705508,-3.849961,0.144174,-7.152076,6.293869,-5.059557,-4.670911,1.769660,4.669984,-8.589838,9.221761,6.548902,1.144556,6.566621,-2.364264,3.639841,9.729080,0.840029,-7.017305,-5.628106,9.501211,2.365332,-8.278477,2.657288,-1.960702,1.535594,2.832879,8.139467,2.179988,-0.324935,7.277214,5.470333,9.795888,1.085452,-5.684489,-0.619714,-0.478168,7.135992,-4.552907,4.806925,-0.631878,0.138064,7.734759,-7.433122,1.910953,-3.578332,-8.062087,5.463049,-6.201215,-1.011958,-8.995030,-9.515820,-1.036575,-9.937931,-5.100770,-8.915189,-7.461267,-2.269210,-6.308862,-1.052464,2.627521,-0.859466,-9.923700,3.765821,-3.028094,0.068244,-4.774430,-5.278060,1.137692,-2.097707,-5.263511,-2.742382,-7.622620,-9.671201,-1.648244,-8.308575,0.060611,9.227187,7.214375,-9.139058,-8.583536,-8.227915,0.694673,-6.887212,7.324783,-6.899261,4.050301,-3.128696,8.155040,-5.021764,-5.405059,6.398596,-5.978197,3.500431,5.885608,6.371594,-8.776417,1.822422,-3.416270,-6.515708,-7.350325,2.726206,-2.318301,9.840768,-5.389546,2.303942,-9.483229,-9.728134,2.703507,-9.163237,5.309828,0.654740,-6.020196,8.838809,-8.748392,-9.821738,-2.559970,-7.974367,-5.612129,-3.471240,8.642595,6.415229,-6.222160,-2.517379,9.825676,0.633076,1.938371,-9.082772,9.911205,-9.991888,-6.390224,-5.275569,8.563784,5.529088,-7.004948,-3.762714,4.073751,8.586953,-1.291857,1.260216,6.214417,-3.577023,9.155635,-5.145761,5.120802,-6.445648,7.286575,-8.705135,4.509990,-8.062070,-3.223294,-7.039222,-8.614354,8.171122,4.814356,2.854356,5.009063,2.620193,-5.472229,2.799757,2.108229,8.335529,-6.923204,3.379624,1.894567,3.941281,-4.339685,0.925988,-8.565831,5.504179,-6.043327,-5.892840,6.475965,-3.033293,3.384789,6.523703,-0.268227,5.484813,-6.446628,-4.570987,1.002231,3.522978,6.512353,-2.362097,-7.549120,-6.466755,-0.930031,-7.770696,-4.845346,-8.015554,0.061350,-3.965005,-9.086836,-3.760460,-7.540298,3.854978,0.539490,-4.200094,5.947397,-0.576231,-7.548079,-0.020962,9.627960,-2.320436,-0.385096,4.284400,-5.020446,6.794304,6.194207,-9.417045,-8.079143,0.386046,-2.724888,5.239378,5.002973,5.403271,-4.544634,-3.123187,1.286050,9.252156,8.792956,2.902318,9.601203,5.405207,-1.260367,-1.979641,2.905984,-3.588643,3.713704,5.374996,4.925181,4.302826,4.897022,8.687696,-2.108853,-3.358693,5.906543,-5.631527,-5.271528,-0.399534,7.202219,5.129577,-6.136611,-5.510875,7.466394,-9.217042,5.046494,-1.228207,-7.964503,6.126539,5.128347,-0.279677,9.480365,9.884996,-9.001023,-0.535235,-1.232824,-5.708169,-5.667476,6.671152,5.972645,-8.217331,3.970134,2.549429,8.726459,-9.136025,-2.129607,0.705217,7.160119,4.951278,-1.149165,7.310605,1.640278,-0.222726,7.217742,-8.315906,8.656416,5.499407,5.691081,-2.519269,4.154789,3.114273,-3.713030,3.485346,1.388966,1.362531,-6.791939,2.827725,6.504067,2.140009,8.199893,5.869411,1.324377,9.001808,3.143293,5.071646,-4.393818,-6.484634,4.544325,7.127898,-8.005417,5.532796,1.146455,-9.934610,-2.820108,1.562992,7.776411,-5.941917,5.471960,-2.738478,-0.881693,0.138054,-7.773308,5.609930,1.966415,9.810366,0.026706,2.219485,4.610425,6.012627,5.114201,0.803168,1.691483,3.938688,6.543999,4.151002,6.558086,-2.291861,-8.375472,-4.521702,-9.185363,3.643103,-1.248225,9.586703,1.852280,7.916817,3.014168,7.568299,-7.055726,-4.911136,-2.467940,2.234272,-7.891312,-3.156909,6.467923,6.330666,-2.064411,-3.618696,0.368664,-7.540415,-3.826365,8.276754,-1.631265,1.292998,-4.700914,-7.958300,8.667417,-7.114978,6.953068,1.418720,3.765375,8.410163,6.372569,-6.468986,4.944656,8.991385,-5.572840,3.750025,-0.085347,-4.492206,-8.841222,8.997343,-7.557949,-4.344512,-5.127344,6.478245,-4.173283,6.274530,-0.714319,-1.658026,-7.101238,2.065914,-5.270828,8.579878,2.645201,2.207278,-0.803808,-7.327927,3.835561,8.727039,-0.694708,5.309417,6.467743,-7.726448,3.748692,3.528310,5.356054,-7.632223,1.383365,-6.702621,2.714751,0.966136,-4.501681,2.745596,-2.637765,-1.812099,1.247665,0.457675,-7.025984,-2.486854,-9.295048,-0.417860,-5.339778,2.493829,-9.266194,2.096633,-9.985838,-4.465065,-4.579270,-7.169677,-0.430168,7.623264,-4.011575,-0.322580,-4.431882,-7.029289,-3.424339,-9.951082,-4.804178,-6.358808,1.304592,-3.121483,-4.509413,1.301117,-4.559253,8.268601,-6.222970,-5.458697,1.144453,9.451230,6.831490,-8.357649,-6.163378,8.607290,1.490985,-4.553627,0.140740,-0.041992,1.850412,-0.549688,2.560988,-5.672360,-5.240906,-1.589681,0.024212,5.751613,-8.658409,-9.684360,6.605337,2.150975,2.098366,1.363045,-8.723249,8.884373,3.949647,-9.546641,4.651521,-8.309169,0.069102,-3.661439,8.486474,-8.800438,7.541640,-0.828916,-9.000599,3.323721,7.549641,-1.516767,-8.767545,2.288301,1.624158,-8.910950,-8.714513,-7.461908,-6.258376,-8.613314,-7.560984,3.677963,7.820798,-1.307965,2.279296,-9.597666,4.944139,-5.398844,-3.572044,0.996254,4.911456,-9.641712,6.566344,-8.089341,1.740943,3.053192,3.514977,-1.399833,-1.183073,-3.639602,-8.106909,5.821064,9.475645,-7.244666,0.666530,2.793324,7.274339,2.679763,-4.619197,-1.747343,-1.428960,0.669860,-0.093373,8.002422,6.805190,-0.158202,-3.915055,6.820352,-2.514752,4.171569,4.299285,-0.192477,-2.610534,1.859131,2.535425,1.373997,2.348960,1.979538,-2.091059,1.296747,-1.832168,8.351365,4.266174,-0.135486,-4.375208,5.247611,-9.965262,7.170827,6.668903,8.368051,-7.083225,2.042026,-7.826807,-6.329676,9.186801,-5.285581,0.368889,-2.174433,-7.430601,-8.775703,-2.023930,-8.291739,-0.603923,2.371771,3.758895,-7.794719,5.443775,3.994781,4.762112,-5.152685,5.927785,-9.080958,2.306759,0.553788,-4.931041,-5.193718,-4.099211,8.239084,-0.150777,-6.435379,-9.498159,-8.469138,-0.347947,9.373167,1.693628,-0.427026,-3.571424,8.530153,1.471749,0.844181,7.038136,-8.820622,-3.428348,-8.878479,4.034930,-3.961776,6.645975,6.410495,5.451027,6.445232,1.128276,3.322487,5.167705,9.941226,-8.296831,-9.446632,-7.541159,0.450709,-6.007242,-0.525455,-2.399669,9.340217,2.422738,-5.266393,2.608087,3.698472,4.912131,-3.280035,2.222676,-9.832729,-8.241499,0.706659,0.178395,-7.036568,-5.403426,2.410668,5.200165,3.289930,-4.077115,2.573662,6.374300,-7.321060,-3.784668,9.433814,-4.355938,3.619037,-6.986871,8.819456,1.618068,-5.030695,-6.169773,-2.569582,-0.255936,-6.524045,8.328627,6.355558,-1.581076,-5.664566,-5.566168,8.547288,0.217944,-1.662707,2.210655,6.073038,8.176000,4.686917,-3.452418,2.062970,8.274481,6.408658,-9.473510,7.370346,-3.698042,1.708312,-7.016806,2.729874,3.496666,2.669473,7.913124,6.886067,-0.728293,9.606171,-6.694353,-5.677197,-3.818101,0.061405,-4.157584,-0.106700,-6.866684,8.957668,-9.362336,-1.858529,-7.764828,-2.317223,-2.169977,-5.076423,-0.721886,9.744031,4.587238,-2.021897,6.606005,-6.581786,6.092797,-2.543859,-3.144189,-6.915738,-6.106957,-6.537253,-5.518292,5.797729,-6.782236,-3.111939,0.395856,3.285092,9.885768,-7.757399,0.708949,-6.592597,4.705904,-3.531864,-0.843737,-9.952013,0.733809,-7.352422,-7.344073,5.319614,6.131540,4.599241,6.870083,6.954905,9.517223,-0.967250,-2.949242,2.826109,8.223329,2.009068,-3.223959,3.834767,-5.663882,3.194041,6.239067,7.393868,-0.996520,9.466494,-5.303382,-2.413313,-6.651822,-2.254598,3.503609,8.837590,-6.794121,6.281700,-9.985295,-3.732218,-3.136394,9.968648,-8.222304,-0.436930,-8.638337,4.712184,8.799110,-4.740106,-3.426848,-0.413439,-8.410994,-5.916265,1.571798,5.802154,-7.368996,-3.689250,4.254372,-3.770380,7.576642,6.718774,-9.226978,-6.726848,-5.733443,-2.969331,3.093430,8.830667,-2.110860,-5.622649,8.565370,2.194878,-9.733969,-2.766555,-6.481680,6.873894,9.927371,3.299840,1.766997,4.938227,-4.282895,-1.180068,9.401900,4.507155,-5.341826,6.987755,6.199021,9.630229,-1.564904,0.226549,2.825013,-7.535425,1.940895,-0.565820,9.905841,7.494032,1.923302,-8.760798,9.202664,-3.974470,1.486354,6.388824,6.507521,-3.970071,-1.738518,-1.779287,4.710827,-4.451627,-3.462800,7.972655,5.497432,7.828286,8.031317,4.146421,8.906352,-0.583259,9.928343,5.402350,-1.758663,-3.700239,6.559365,-0.452590,-4.461832,-5.534460,-9.817793,-1.127635,-1.882496,-2.778344,5.997524,-8.574459,-2.489529,-8.876147,-8.161846,-6.394965,0.583184,2.217609,9.723452,9.095129,-8.743589,-3.577244,-3.295434,-4.754889,-9.647022,-1.738365,-1.070442,-3.512474,5.792384,-6.340396,-9.511074,-1.118338,-4.495212,-5.057491,-8.523973,8.042475,1.230732,3.266957,-2.508195,-8.406338,-6.199034,8.918178,3.756109,5.805129,-5.278469,-4.459787,-2.596901,-5.054471,-6.425160,-3.066439,7.261310,-5.629409,0.542555,-0.477636,9.879016,-7.476165,1.064195,9.233066,3.226444,5.003004,-1.284823,-3.778196,-6.621080,0.835399,-0.721709,7.720746,3.435478,-2.029648,8.764242,6.126075,-4.231718,7.756637,1.838195,-4.443167,2.288249,-2.717672,-9.156648,1.558790,4.073374,0.240355,-8.340582,3.731000,-9.437321,3.351127,-2.423941,8.403870,-4.944354,-2.469841,1.157102,6.790190,-3.904617,-2.170839,-6.877673,-0.112063,6.592108,2.897234,-6.677054,8.513146,5.109085,2.401089,7.386151,-1.325846,7.459375,3.925980,2.418560,9.856283,-0.636412,-0.770030,6.660186,8.769923,0.646346,3.609222,6.601259,-0.795383,7.572215,2.306907,-8.480391,-3.742852,-2.338932,-9.162667,-5.311422,-1.773867,-6.334387,-4.761495,1.607497,-6.213542,-7.856609,-4.747835,-7.091318,-8.966755,-8.834087,2.018754,7.869972,-3.106711,8.461910,-4.899794,5.319054,0.325965,9.215585,7.513028,5.385513,3.904665,3.940892,1.570135,5.264880,8.371522,5.313513,-1.205442,8.301062,2.263894,-4.896223,-3.860216,-3.588857,5.100423,3.439591,-6.656476,-4.016870,1.470212,2.534834,7.609996,-8.421285,6.707383,5.170058,8.636427,-3.381698,-5.233363,-3.455113,-7.051942,-4.258525,-3.852728,4.902665,-9.881044,0.127060,8.545894,-7.825167,2.406789,-3.733326,1.940765,-5.244537,-8.221886,2.985435,7.018341,2.301408,-4.711205,2.618657,-7.873942,7.360545,-7.934791,-3.877315,9.683902,8.190978,5.233751,2.078669,7.697883,7.946046,2.599930,-2.034536,-0.770002,-1.964843,0.390572,-5.840726,-1.907182,-0.953046,-5.833154,2.400425,-5.785054,-4.622019,-2.091066,-5.827609,5.540610,8.331721,-8.166903,-5.778861,5.027295,6.165988,-5.831113,-2.797999,5.190445,-5.583651,2.007069,7.213472,-5.596777,-2.733865,-1.044106,-4.931841,-3.239820,-1.592856,-8.087447,-5.499797,6.451804,-5.630651,9.226616,4.090343,-9.412972,-4.471664,9.138497,4.172957,9.136916,-4.427955,-0.650518,2.689517,-9.504087,2.699372,-1.110607,-4.640573,3.049677,-7.506666,-0.046231,8.629375,0.746309,-8.232062,8.942513,-8.157323,6.665407,-7.828132,6.226170,6.594184,8.761664,-9.304137,-7.873496,-5.406058,-1.109493,-8.604540,-6.947563,6.254538,1.332812,-0.759962,5.386327,7.834754,9.712867,-4.176590,5.388011,-5.360036,-5.139137,1.692307,2.586020,-1.959348,-7.283405,-0.723590,-0.686924,-5.677697,-8.218315,-6.334500,8.422429,-9.119227,-3.274981,4.966843,-0.211862,-6.256726,7.982940,2.061369,2.546963,-2.167379,-1.854399,-6.297629,-2.565674,-1.899171,5.474453,-2.240904,-5.372378,7.492176,3.050888,2.299253,-8.912185,-6.484492,9.216075,8.875708,1.363035,-7.462326,-0.932693,-6.534291,4.062900,8.819979,7.785451,4.815856,1.981866,-2.497248,5.501577,-6.925158,-2.183679,7.303272,3.082270,-3.050500,-3.516730,-9.380114,-0.690252,7.539763,-9.832567,-9.568009,-5.804391,0.079162,9.467769,-3.359628,5.609105,-3.143268,0.279011,2.765169,-9.669382,6.681575,-1.052634,-2.025342,-7.161851,-1.560370,-8.684251,7.042089,-6.459977,-0.029317,-1.157515,7.900735,-9.233476,4.295322,7.845503,-4.260434,2.976210,5.758555,0.511974,-8.737785,9.326749,-6.925217,6.563856,8.594458,6.108298,7.752150,-9.549720,8.709804,8.518603,0.135568,-2.523597,-2.573187,5.942347,2.435027,4.276403,3.377641,1.921072,0.227953,2.777529,-7.605580,-9.872163,-6.103146,-6.744041,3.339388,0.850583,8.040006,-7.819332,8.948064,8.960770,3.562709,-7.635712,9.889377,-6.718087,-3.697636,8.754004,-1.786368,6.165447,2.476929,1.464725,6.697858,1.477799,-0.940170,-4.132548,4.881201,-8.125142,6.026724,6.440429,-8.154147,2.859584,8.044630,-9.127256,-5.130189,6.385257,2.681824,1.243477,6.299454,1.511176,-7.921628,9.652108,0.924148,-5.958415,-3.979512,-7.714313,-6.293143,6.143490,-8.657966,0.399179,9.332909,-8.405737,4.215165,3.645865,-3.286391,-5.567647,7.411094,2.592234,-9.617061,0.022973,0.694539,9.648031,9.772788,-4.988001,-0.294257,-4.056665,-9.055593,8.037667,-9.086934,-5.984550,3.303482,-9.619472,-2.526065,-1.913208,9.564253,8.440855,2.473558,-8.148761,8.072894,-8.900048,6.475283,-9.934351,-4.593436,9.980984,-4.528417,5.586448,1.560614,-4.423328,2.255902,-1.441265,-6.284282,-7.596161,-6.951605,-7.352264,0.114194,-0.200003,-1.727077,-0.598462,-5.341627,9.597784,8.017680,-3.241118,-1.023200,-8.915250,8.313644,1.936408,-9.448831,5.995980,-4.335049,-6.705263,5.799169,-7.755439,2.421877,-7.789060,7.346423,4.420959,-3.625461,3.582241,-9.009310,2.426724,-4.128679,-6.044371,-3.637970,1.665102,2.730091,-3.815892,-7.063536,-0.630329,5.722026,2.766472,5.002058,5.156361,4.125434,-2.235509,-8.202517,7.217701,-6.878788,2.311620,-7.036290,-9.988869,-0.908058,-8.240963,1.326888,7.119138,5.745923,6.235423,0.862753,-7.911317,3.106408,-8.757823,-9.198921,-1.309094,2.025110,7.555538,3.192391,-8.524552,-7.955618,-0.261389,0.813017,-4.240205,5.871164,5.345398,-0.451550,0.383704,2.556315,3.344173,9.407578,-0.702045,0.639637,-3.071699,4.640247,4.330447,2.895984,-7.872929,2.865379,9.267749,-3.527776,1.844735,0.480125,6.597366,-3.767018,-1.800383,-5.184895,3.172219,7.325685,-1.045344,-1.777416,-9.812916,-7.707501,-1.616372,-6.389576,-8.056150,2.173142,2.038532,-2.352540,2.755350,-7.529580,-5.361209,-3.514375,-9.724954,-3.642533,1.266492,-2.336794,-3.162380,-6.674345,-8.095288,0.616411,5.431195,-4.039830,9.461158,5.949152,-8.707733,-4.582898,7.464221,-9.661262,-3.752880,-1.748427,4.750852,-4.723470,2.260255,-5.101309,4.600877,-9.753011,-2.378306,8.982469,3.812059,-6.165231,-5.454653,2.271835,-7.142899,-5.810238,-9.537851,-0.839531,2.133465,6.986733,7.776101,3.683621,8.199873,2.232383,-2.956612,3.692171,-2.880073,2.423491,7.260266,-1.386240,-1.098896,-4.017279,5.212187,-3.679679,7.455796,-0.003635,-0.368759,6.351195,2.873741,7.407482,-3.997143,-9.568225,0.768215,9.958524,-6.912616,-8.428380,-6.782638,8.622415,2.404969,8.597718,0.569789,2.235145,4.110400,-6.589046,7.074628,-4.929079,-9.045302,-5.532878,1.558240,-9.694709,2.439112,-8.065273,-0.842326,-0.325599,-1.796246,-1.208857,3.996637,4.124586,3.729579,8.536168,5.111860,-1.339260,-7.490230,8.552280,-3.873626,4.924032,-2.130433,-4.513715,7.644361,-8.498580,-8.839940,-6.934921,-9.147239,-7.877326,1.560048,2.282994,3.378974,-7.270806,-1.744438,8.673718,-6.539849,5.901631,8.904281,8.354700,-2.243665,-4.786620,-0.623700,-5.727871,-9.255518,-4.226073,-8.072804,-8.934088,1.727673,-3.848894,6.969551,6.485168,-0.538353,-7.535904,-5.442560,8.263890,-6.516498,9.050266,-7.956983,3.483902,-8.225905,-4.596328,5.824445,-0.529111,2.370436,0.617091,2.318064,-8.103822,6.192204,8.006488,-1.651909,-7.762225,-9.676077,-4.335445,3.267867,9.733163,2.584448,-2.392058,-5.843869,-9.358659,4.084184,-8.446526,-6.179752,8.824048,-5.166204,6.358627,0.211432,5.740426,4.688855,-0.707649,8.579428,-1.051626,7.606342,-2.101164,3.885856,3.597548,-6.788405,0.987052,1.126412,-3.194776,0.804685,-4.377284,6.879270,-7.631676,8.055969,7.592793,-8.733146,-3.266184,-1.523719,-1.862155,4.584417,7.409821,9.923466,-4.626770,0.246906,-8.272425,-7.959463,9.055134,-1.094383,-1.391570,-7.818828,0.776204,4.386504,-1.330630,-2.538101,6.709810,-5.148893,3.656188,-2.657429,-7.397778,-2.879017,-6.598204,-2.261331,-5.802060,-9.568351,-4.535317,-4.907591,3.885745,7.552473,9.144987,-1.954280,9.692314,2.015514,3.392834,-6.635662,3.742650,-4.481225,9.457985,7.903482,-3.961982,-2.076113,-0.026431,-4.253314,-2.031691,3.394446,9.347729,8.042487,7.437945,2.433673,-1.962371,-4.712621,-3.597972,6.359209,8.642737,0.228543,-9.854617,4.896963,-0.746897,1.615770,6.305632,-5.676585,-1.888340,-8.802516,5.624927,-6.224697,2.487707,7.668092,-2.247190,-0.752894,-5.429651,9.458448,2.298764,6.024276,-3.430451,0.630535,-7.869517,-1.738517,0.910258,-7.705773,-4.454470,-5.861176,8.170906,7.594900,-8.306109,-9.616184,0.672215,-5.372988,-3.195000,-5.215597,-2.656606,-2.728674,8.743830,2.863640,4.416672,7.072148,8.953963,-1.901703,-2.470027,-9.145299,4.793223,9.994037,-0.479058,0.205676,7.574955,0.144158,6.758283,-8.482114,-4.414621,9.436602,7.019414,2.060157,-8.923288,-3.640848,7.159563,-9.197892,1.163705,2.889519,4.238315,-4.735977,-7.453237,-2.433579,0.066236,-7.855010,-3.926137,-9.606550,2.109200,-8.252915,8.495113,-7.129485,4.353571,1.756626,-6.360350,-2.518809,2.798988,-1.718406,-0.787425,-9.119943,-1.625012,2.793503,-6.030611,-5.375694,6.375511,-4.636540,8.297399,3.099157,8.772615,4.177005,9.512552,9.124852,-3.415798,-9.053625,-8.541779,3.211084,-0.519686,7.639281,-8.697460,-3.967977,3.004669,-9.921933,9.872807,4.146516,-1.816741,-5.228926,7.774494,-5.545117,4.977623,-3.474715,0.028469,-3.656712,2.221153,9.967431,-8.535247,6.458972,-5.540782,-8.169653,-4.204045,-0.080904,4.700943,-2.173350,-7.595912,-7.679912,-5.673720,5.990103,-5.138019,3.110736,1.610357,2.909114,-3.056161,0.173011,-4.208704,-1.916095,-3.579163,7.214864,3.409384,-3.024300,6.097360,5.472695,5.303230,8.322632,4.253194,9.910352,5.620132,-9.069911,-2.712404,-4.255824,3.904245,7.551866,5.698289,9.153897,-8.341920,-6.910715,5.722491,2.374600,-0.067737,-4.575539,5.738842,3.235130,6.717024,-6.076544,8.518219,-9.742738,7.585844,-2.529237,1.960606,8.737771,4.070571,0.035151,-7.971147,-5.567997,0.729808,-6.579729,-0.914373,-1.146586,5.305169,7.486482,6.462443,2.506104,7.487582,-5.165775,-9.419187,2.048962,9.137171,-7.890686,5.226790,8.370844,6.352674,-1.074322,2.155440,0.257002,1.579105,4.201974,8.433388,-5.313249,3.744020,5.767674,-1.985272,3.515479,1.942168,3.823491,-9.990913,7.826153,-5.134372,-8.651309,-9.140559,-2.008143,-2.906307,2.218782,2.756343,2.739469,-1.381649,-8.516661,1.713259,-7.190381,4.328666,2.186650,-6.450635,9.002711,-9.482224,-7.710172,-2.021011,6.444895,5.844822,-6.515971,-6.709432,6.711062,-9.442042,7.207839,7.199887,-9.045975,-4.967466,3.658830,-2.272709,5.102050,-4.203214,-5.179063,0.364497,9.315119,-0.403340,9.092394,0.778073,9.478015,-0.872836,9.803581,-4.187772,-9.651514,-6.500277,-3.104107,-5.063993,8.073743,0.326395,4.289248,6.182866,4.479319,-8.232010,-7.362749,3.010735,8.968868,1.020375,-8.986620,-8.021718,-1.359805,-6.115446,-6.908927,-8.962208,3.898412,3.428027,-2.601942,7.382406,-0.606673,-4.789018,-0.256439,-4.664748,3.264246,-7.161584,1.599584,-0.631388,3.039646,-0.452926,-7.324965,-8.791970,3.185783,-8.625570,-3.021737,7.585053,-1.161793,-0.806412,-7.374972,-3.192000,-6.133330,9.422143,-8.532869,5.847886,-7.708408,0.936875,-8.451378,-5.648221,2.340876,-5.335358,-4.049311,-7.730663,8.813302,8.401949,1.351388,-8.564520,1.781580,9.312629,2.429837,5.889100,5.795768,-6.407339,-3.649829,2.478673,-5.759694,-7.701242,2.006801,8.071195,2.979990,-0.549496,-6.053598,-2.712839,-8.805416,4.164647,-4.225691,6.303510,0.851741,6.183959,-8.978100,9.579389,-7.459031,-9.899548,-0.984869,5.370933,-5.374540,-9.480143,-9.915854,-2.893498,2.444717,-0.611858,0.412718,5.980036,-1.335123,-0.158175,4.680839,3.153851,3.646306,8.329105,4.968647,2.542759,6.749658,-7.417163,-1.431836,-6.479527,0.233389,7.389502,6.772250,7.431016,-2.692274,-1.209768,-0.127985,7.170224,9.836365,1.292319,7.797741,5.443591,4.540043,-4.568620,-7.375640,7.022707,-0.214814,-2.882961,8.980080,1.421332,-5.681070,7.813578,5.077589,-1.440154,1.815453,5.058358,4.459385,6.639874,-5.130477,-5.382990,1.290937,-4.316697,0.503967,7.313528,2.599440,-6.330361,-2.873632,-6.693500,-6.377514,7.281194,-4.782688,7.313784,0.633982,-2.355350,-8.943531,-7.519378,-3.539914,5.316883,-2.519835,-2.136021,8.582332,8.932191,-6.229522,7.700446,-1.032633,3.843191,0.505873,-8.584517,8.540454,2.948613,-3.078121,0.166049,-2.518976,-0.790505,9.063885,-2.618751,9.437118,7.801665,3.211011,-6.349945,9.086826,2.157621,-5.237364,9.550356,-4.107606,-3.778596,-0.500847,-6.530388,-6.997294,9.664711,1.784467,2.859710,5.848946,4.811900,6.306621,2.723924,9.370107,-0.959571,-3.652611,3.155679,-0.915123,0.208731,-0.135154,7.765730,-0.145856,-3.987764,4.852843,-6.564686,-6.332160,5.642820,-5.383363,-2.217370,0.655865,5.864925,-2.135319,4.433241,-5.285489,-7.384030,-6.518700,-5.171990,-1.482622,-2.179243,-3.065407,2.714865,-9.555606,-1.923285,2.964606,-4.138839,8.780205,-3.882140,0.203919,-2.581340,8.572258,-7.756618,9.032996,-5.822027,7.677257,5.483981,-3.265139,3.233578,2.568397,6.645931,-7.408074,-4.630628,0.588895,-1.777153,-8.303792,1.212860,2.127287,2.035846,-5.394056,-4.988751,-8.500941,6.151341,-7.397650,-1.571554,-0.437035,-8.821319,9.443427,6.045042,-7.493967,7.077480,-3.892738,-7.428674,-4.769994,-2.854249,1.228901,6.375518,-5.284398,-5.083340,7.847921,0.336702,-7.401431,-4.730026,-1.966931,3.213651,2.944640,3.062817,4.953135,6.203884,2.549799,-6.840579,1.997935,-9.106161,-8.361394,-6.025165,5.547029,5.871140,-0.478320,-4.689978,1.226058,0.135050,-0.955221,1.448909,-9.895772,-6.095726,-4.632503,-7.421991,-6.657347,-7.228260,-1.681388,-5.114164,-8.091854,3.414961,1.351785,8.295122,3.834194,-0.843151,8.702236,8.548552,-5.623819,5.842210,-8.975113,-0.818456,-8.010225,6.030806,-5.163899,8.836774,-9.202548,0.465749,-3.473134,-5.224443,5.920228,4.914517,-6.338393,-8.986139,-8.547122,-6.200548,1.052417,5.097356,2.793879,-1.830314,-2.394783,-1.867384,0.823419,6.325410,-7.575447,8.232137,-8.334808,-4.780325,-2.450883,7.994741,-0.053221,6.693219,9.076764,3.410453,-3.462430,-0.800681,6.298895,3.319123,-2.102722,-2.598958,-9.580340,-7.539546,9.993897,-6.795358,7.084750,-4.329544,1.837911,6.678498,6.233267,4.854915,0.792921,-6.002191,-5.519230,9.811560,-5.165708,9.065582,4.321428,8.136651,-2.842224,-6.566495,-1.435476,9.647678,7.420050,-0.848931,9.391344,-9.946141,5.782512,-4.653304,-2.811163,-6.169218,1.478743,4.909710,6.608080,8.581086,-3.742405,5.693381,8.035396,-8.742023,4.377372,9.935735,-2.958945,7.345774,-1.886976,5.112852,8.224762,-4.821606,3.124291,-8.274220,-2.632019,-7.801684,2.457498,7.815716,-4.062138,3.431303,-5.954018,1.905103,-8.902134,-2.387590,-5.693354,9.325498,7.663689,-0.929962,-9.871537,9.260789,9.112677,1.246733,7.619024,1.580445,1.449462,-2.110334,1.912392,-6.422300,-0.820258,-6.490279,6.651584,0.006301,4.576344,7.206456,-2.782297,4.353929,4.846974,-1.887086,3.932110,-6.619140,3.652306,0.111518,-7.543581,-0.287973,-0.159663,9.662750,6.972305,8.229215,9.414332,-4.008508,9.490390,4.065908,-4.134479,-4.825178,8.450268,-7.379121,8.843918,0.437986,-5.936159,-0.185449,-8.386889,-0.762846,-0.271836,1.458457,-9.043935,9.988374,9.126648,-9.481311,5.777561,1.697385,-2.129092,5.549971,9.394827,7.041498,-0.441695,2.908206,-6.706875,-7.415669,5.145138,-8.789221,4.956562,2.113803,-8.031686,4.577332,-6.329031,-1.702551,-0.725071,-7.117814,-6.418844,9.316177,-4.359958,3.222630,-0.571938,9.702324,6.979605,-3.869896,-8.036755,1.795933,5.755563,-9.492948,-1.199396,-4.166774,-0.844488,-3.564157,6.331433,9.550149,-5.438647,-7.676665,5.065089,-5.670096,1.203295,7.023023,0.322482,-7.031603,7.242351,-4.519743,2.054770,0.732872,-1.172819,-9.703220,2.251313,9.143866,-1.399161,1.916553,5.794499,7.732148,-4.582073,-9.640365,7.359517,-0.345561,1.689766,-9.270895,-0.385687,-7.748784,-1.075556,-1.977717,5.463935,7.314925,0.199377,1.092443,0.493902,4.834577,5.530941,9.688089,-0.904582,-0.472221,-7.594224,-6.552229,-4.163309,4.001057,8.036498,-6.845837,5.814355,-5.166378,-4.678799,-4.551866,-1.496172,5.366411,9.739329,2.460778,4.488208,-3.005026,-1.140955,-5.845268,8.800278,0.431053,5.565392,9.221085,-5.221332,2.399052,3.545551,-1.040324,8.154747,-1.107821,-3.385827,-5.477749,6.356174,1.197989,3.571578,-5.851340,-4.954578,7.019722,3.766297,-7.740594,-7.862516,5.155368,8.056029,-3.206551,6.241794,-0.017899,-1.760947,6.976178,6.038873,8.028817,-6.648857,2.100827,-3.892428,-7.434830,-2.249940,4.612679,-1.971151,-8.224493,-0.970375,-7.081411,0.245421,5.880513,6.855265,0.165034,2.510624,0.523379,-9.298885,-6.102039,5.983603,3.611067,-2.190080,1.080276,4.244647,-5.377776,-6.154322,0.467940,2.077187,9.865026,-1.053238,3.332331,1.203923,9.865137,-7.774558,-0.060390,7.312124,8.327251,-5.905866,-0.940868,-8.186123,6.692070,-0.442964,8.477904,7.151762,-5.945061,2.442616,-2.521205,5.057234,6.368818,2.836845,2.970551,2.101546,-5.758537,8.701739,6.498254,-2.681187,-2.008248,2.593301,-0.641889,-1.627912,-6.940259,3.857870,7.313063,2.155072,-6.849249,-0.531831,8.159679,-0.907600,-5.819386,-9.966127,5.846692,-5.012635,8.884957,9.156675,4.664914,3.978876,-8.141443,-0.286493,6.126550,-3.876208,-6.273642,1.564188,-9.041820,-5.452967,-8.162424,-3.346599,2.454536,4.196838,-1.367522,-3.232441,2.788613,-0.007860,-5.205275,5.362453,-9.953362,8.537107,-6.209908,-7.153215,-3.595587,4.289730,4.884043,6.450348,5.231280,-7.700747,7.915726,5.768662,-9.590701,-1.572259,-2.899636,-6.814176,0.780108,3.438027,-4.052662,-6.605240,-9.273443,8.433281,8.530227,-2.199275,-5.369798,3.285517,-5.737350,-9.240122,-4.135251,5.187595,-6.211981,7.079839,-3.141425,7.370561,-7.315061,3.982901,-8.869960,-1.998688,8.572608,-5.120878,2.088722,-8.439152,-3.898471,-4.911926,0.119541,6.646232,2.382091,-5.323427,9.656885,0.832818,0.416092,0.753539,1.682614,-0.738841,-0.854065,-1.457464,-2.325075,3.299606,5.051733,9.192904,-1.483660,-9.977374,9.032630,0.974920,2.014919,-8.346494,6.801508,-5.494139,3.969759,-2.250447,1.209239,-1.013190,0.723253,-5.476885,9.789968,4.554160,-6.849476,-5.366978,-9.964082,-8.879524,-5.339821,0.348188,-8.012057,-7.109735,-4.565983,-2.190826,-4.662373,7.945517,-6.472559,-2.464388,4.568182,1.837298,-8.825754,8.011902,1.013965,-1.666128,-8.373209,-0.634446,0.853679,-8.340752,3.361451,3.245983,4.313453,8.717585,-5.719276,-6.149226,4.456263,1.067465,1.488473,5.216011,-6.926697,-6.583671,2.659768,-7.668790,2.902707,-4.238699,3.011524,-5.794082,-8.338381,-4.056921,-0.121018,-1.546805,9.137102,9.560103,-1.034240,0.085779,-6.639852,1.394875,-9.123046,-7.230739,-1.159349,-4.168800,-6.410313,5.602323,-2.375197,9.592647,-7.857066,5.235613,0.518269,-6.277261,0.871549,-4.807582,5.439791,5.622097,2.906826,4.226765,-4.998049,4.778932,1.335640,8.775805,2.378329,-8.756030,-1.448876,6.769528,-2.119450,1.850532,2.695059,4.092930,4.232581,0.679145,-4.791400,-2.750809,-3.910158,0.989102,-1.097971,-5.099817,2.040912,3.290833,-1.812656,4.796149,-2.611225,-7.820258,-9.238711,-2.300623,-7.829608,5.690651,2.876633,4.345130,0.986132,7.769686,9.562348,3.797488,-4.369590,-4.685065,8.133368,9.533840,-3.647185,-9.749044,9.586096,-0.380944,-2.825844,-8.672525,1.502990,7.015820,-1.840442,7.798728,-3.909048,-0.695501,7.830845,1.162573,-2.622100,8.085007,-6.002663,8.440760,-2.634372,2.319814,2.271878,-4.832247,1.761678,-8.849125,-4.133529,1.272779,-2.118085,3.616385,-4.986404,9.263103,6.019004,0.247430,-2.117470,3.368125,-4.515914,9.178884,-6.171839,5.057497,1.603495,5.399538,2.342228,3.695344,-8.177404,7.377851,4.359329,7.992508,5.637756,0.673146,-4.418521,5.572220,6.799746,-7.464992,-1.784023,-8.693513,7.717548,-3.631189,-0.674330,5.460861,-5.042680,-4.139960,3.397282,9.072113,-3.059043,-2.995661,8.782227,-9.041312,-9.877401,7.256049,-1.308239,-8.760138,9.449799,-5.635108,-3.175739,9.719083,-7.328142,1.860083,6.331119,5.105271,9.302870,-0.389224,5.215964,6.943356,-4.469524,-8.761540,-0.799397,-8.857899,8.060405,-1.795896,-0.321909,7.289323,7.287193,-9.725910,6.697165,-2.164306,7.557494,4.784099,7.994459,-6.477390,2.054231,-0.688134,-2.512288,-5.495182,9.757387,8.135091,-1.823089,4.765691,8.725904,-8.654880,9.052889,3.074714,-2.694725,6.733097,-8.946698,7.757694,-2.593404,1.177815,-6.468001,9.859203,-4.833023,-7.507680,2.534629,-6.609001,8.621993,6.378671,-9.785629,-8.616002,4.403061,-7.011293,1.530661,-1.601305,-9.837402,-8.024607,2.113467,-3.525794,5.376874,-5.290757,-4.017455,7.490498,5.710380,-1.166798,-8.374343,-8.658355,-2.144631,5.407337,-0.951273,-2.301648,7.225305,-4.177930,-0.141005,2.265400,1.241200,-8.300277,-0.582406,7.390465,-4.292701,6.894655,-0.623569,-2.847349,2.084769,8.404154,9.096258,-2.798856,-0.877804,8.273291,8.280472,-1.043430,-0.211429,3.578450,5.593632,2.107902,-5.227442,-9.613219,-6.150671,-7.594024,-4.569890,-0.121183,4.557698,-1.545978,9.582572,-7.623667,-0.345023,7.653590,8.327696,-2.818467,2.298303,-9.658297,-0.665834,0.933335,0.005219,-8.552829,1.705586,-5.673283,5.473405,-0.780587,-6.948292,-6.413536,-8.293488,-6.647175,-9.646683,-0.059097,-8.792399,2.763363,1.110277,8.472268,-2.783303,-1.298687,-0.653232,-2.558326,1.887521,-3.471100,0.423678,8.259676,-6.101075,2.485929,-8.462624,1.574610,-3.602386,3.422541,3.432035,3.635105,0.544126,6.671920,-7.929536,3.739065,-1.798493,4.297106,-4.675461,5.960439,-6.049597,6.913449,-6.080664,8.971262,-1.395007,-6.639136,-1.182130,0.288672,4.285745,2.097593,5.788497,-9.250292,8.817070,5.869810,-4.013232,-5.869768,-1.101450,0.546608,-8.758881,3.137254,4.465792,-8.690104,2.012940,9.983393,-5.377482,-1.590557,-5.379401,-0.449227,1.530526,5.076639,-9.416858,-2.578293,-9.986186,-7.308229,0.092031,9.590971,8.723038,-2.211562,2.542782,-5.143465,-0.492698,4.453541,2.590271,-0.746270,-8.600969,-3.761457,-6.441860,5.141727,-0.560195,2.457694,9.871579,-6.344518,4.481632,-0.740968,0.057788,-6.279958,1.942840,-8.782148,1.503295,5.600668,-9.344369,6.943831,5.236592,1.775964,-7.494141,2.219534,0.794903,-2.690287,-4.264205,-3.793062,2.653842,9.251765,-6.958704,6.320143,8.581920,5.776860,-3.442743,-2.287248,6.162774,5.983115,-9.302028,-5.118275,7.979288,-9.042338,7.054551,9.973114,-8.848237,1.454137,-6.874675,-6.417907,-1.003348,4.574447,-5.405591,-9.221022,-6.011395,6.794460,-2.743808,-9.442306,3.920128,5.731923,5.561568,1.572015,3.807628,8.007867,-6.822879,4.299374,0.694251,6.868548,-3.162871,-1.694517,-7.353943,-3.053759,8.006001,-9.944024,0.515861,8.986450,-7.773695,-7.853429,4.947299,7.763940,-8.734525,-0.166077,1.980504,3.283296,3.363612,-8.575265,-4.955214,-0.109526,-1.050775,-8.649114,-4.110929,-1.510054,-2.342480,7.511704,-8.988853,1.204239,3.525546,8.044913,-7.028203,9.429873,-1.696445,6.606672,-7.067480,-5.685540,-7.246161,-3.841938,-0.014685,6.213015,-6.296768,-9.853532,3.881324,1.524553,-1.059318,7.156146,4.915984,-5.371405,0.392709,-8.460154,-6.397283,-5.100322,8.171516,7.436581,2.076468,1.615888,3.344355,2.838086,6.030789,-4.105676,7.021033,-4.424565,-3.022850,-2.962884,-7.737262,2.139081,4.898440,6.533956,-2.399773,-0.765944,2.336610,7.405496,5.249270,0.306583,2.376284,-3.146232,-1.966725,-3.716660,-9.896873,-1.924261,5.791685,9.753993,0.633745,-9.427223,8.935185,2.954619,-3.138693,-2.790831,6.308702,-4.914540,4.852500,5.944572,-3.160120,-7.014081,-0.172746,8.587175,-6.505901,-0.090162,-1.574638,9.152536,9.305022,-9.764632,-7.515580,-0.718777,6.716555,-2.541348,0.377486,-6.361477,4.498189,-7.651645,0.749928,-3.782124,-4.083893,8.594206,9.218863,2.360936,3.559472,-0.675069,-0.965593,-5.551914,4.244046,-2.793865,-1.665393,-6.022442,4.454776,-0.120685,0.214592,-0.077959,2.998482,-8.673424,-9.939186,-9.270961,2.910584,6.603950,2.362379,2.275496,6.089217,0.588926,-6.699768,2.959765,0.687237,-9.544930,-7.008541,-8.938310,-8.152351,-0.767111,-6.227482,1.187573,3.874818,2.551846,-8.017362,-5.188327,-3.295557,2.237357,2.531542,-8.889234,-0.611875,3.571107,3.234829,8.438453,-6.586818,7.719291,-9.653846,7.859880,2.852322,-3.429631,9.809941,6.502663,-2.139398,7.830228,-8.760850,-1.889512,-0.775874,3.088290,-6.616625,-5.525585,6.419966,2.568441,-3.930535,7.825250,-4.583085,1.052306,-1.451518,2.975760,0.544520,5.092192,9.982913,2.613107,7.171204,5.590071,8.850457,1.209655,4.263546,-9.195704,3.237365,-7.595208,3.195997,3.152684,-6.753699,-8.928230,2.289797,0.684498,-8.984885,9.242589,-7.745616,0.991737,-6.388125,-7.473996,2.726644,4.569128,-9.618689,-2.459829,6.884724,-8.800827,6.944521,8.089075,-9.419128,2.872810,1.388105,-5.350819,6.645675,2.767308,-4.809598,-2.760122,-3.481446,-9.353764,9.748916,-5.222196,7.171437,-5.318614,-4.035873,8.847885,0.526715,2.482545,7.401219,-5.497212,5.948905,-8.956002,8.548587,6.274849,-4.420486,-0.454292,9.559472,-7.918885,3.478068,6.431751,2.514209,-1.921098,8.632340,3.308545,-3.939931,9.346042,-9.353738,6.672617,-1.274403,0.652366,2.425330,-5.310967,0.548080,1.412689,-0.067721,-0.837723,6.874199,-7.926827,-7.877811,-1.547332,5.349933,-8.376249,4.309531,3.976949,-8.026686,0.710815,-8.102089,-6.942713,-2.691402,6.850663,-6.709782,-8.825131,-5.773707,-3.980028,6.593613,2.669123,5.170890,-0.043574,-4.208734,-9.715238,-7.984069,-7.064707,-5.855889,-7.180673,-3.642197,3.895790,0.438329,-1.024238,-4.897302,-5.911716,9.944758,-6.094091,2.808779,-9.056097,-6.697897,1.637468,-8.599732,8.711673,-2.040051,3.789231,3.520766,-4.795729,5.745790,2.680854,6.975953,1.587503,0.293787,3.343306,-8.420327,-5.217835,8.853346,9.956546,8.524317,-6.502705,4.406790,-9.321676,-6.878578,8.058320,-7.065577,1.582497,9.371986,-8.531299,-2.240450,0.223140,8.731095,7.760852,4.027944,-5.283993,4.873491,7.433685,1.374020,-9.185819,-0.258612,9.070860,-2.330619,-2.555494,7.344016,-2.968829,0.886804,-0.377052,-0.660972,7.649068,-6.393012,-1.606317,-0.618151,-7.867949,-3.085787,0.703404,4.673733,2.976659,2.159499,3.656438,-4.695611,-8.006156,4.119216,7.407209,-2.355487,-9.397907,-3.915522,-3.714434,-1.145154,-3.922315,3.750534,6.464779,-1.655458,-7.257421,-8.782490,-9.596552,-5.666085,-3.076145,4.086585,2.011150,-9.649609,6.416334,-8.242246,5.736778,-7.236146,4.495668,6.009145,-5.717267,3.845182,6.145231,-1.315131,2.369280,-5.612069,2.351011,2.422769,4.933622,-2.371886,-3.273926,9.337383,0.407169,-3.154685,0.893442,2.261478,3.700502,9.469326,-8.294951,4.778268,-0.162485,-6.114874,0.145335,-6.120183,1.146777,4.493461,4.992272,-7.260008,2.784403,-0.178592,-6.699153,-7.349931,-6.016321,7.025041,-7.557667,-6.231939,-6.753893,-4.491348,-4.251417,4.108823,1.358760,-8.856689,7.828472,7.497766,3.025762,5.106105,4.935812,4.178962,7.887846,-3.803797,4.482182,-4.964912,8.699510,-2.549150,8.433421,-0.901386,-5.756394,-9.052788,2.733421,-9.366271,4.614663,-3.113624,-0.840211,-7.435094,-6.279218,6.322319,-6.095002,-0.368636,-0.410338,4.965962,-6.663418,-3.686170,-1.059212,-7.289610,-9.878644,-7.082682,-6.118413,-7.217697,1.751476,5.144297,7.034967,3.701285,-0.058849,-1.103265,-2.932498,0.333645,5.611686,-7.127219,-0.515361,7.000656,1.508467,-7.115590,-8.508344,-9.322708,9.405550,-9.726463,-0.892845,-1.706750,0.515727,2.881916,8.898187,-2.098178,-2.051403,-1.035568,4.256233,3.686668,-4.135742,-5.971829,-0.053885,-7.202811,-8.607377,6.722252,-7.371578,-8.449554,-7.847577,-7.668293,-3.854498,-6.635514,4.146782,0.502064,-5.827945,1.805477,-5.775621,1.668703,2.399902,-2.501988,-2.608429,-8.736774,-5.309547,-7.813817,1.479416,-1.384798,2.379803,-4.006513,8.788732,6.074200,1.953127,-5.132338,1.743485,-8.163683,4.726196,-2.965475,-7.505684,0.562115,7.870952,8.070925,-1.193266,-9.128410,-4.945929,-7.025683,-1.632752,5.619349,-7.979181,2.742562,-9.504874,-6.053755,8.927515,2.717130,-2.606208,-3.243459,8.969147,-5.041641,9.988322,4.326081,9.777067,6.105183,-2.122883,2.489951,9.293237,-3.270488,3.592794,8.717403,0.410602,-0.952320,9.595566,-4.986563,9.550776,-6.409529,7.339862,-2.842004,6.545032,3.579528,1.235506,6.481568,8.150326,-3.125902,-9.325466,3.005610,-5.552365,2.694570,-3.827993,-3.931410,-8.377257,-0.105990,6.980399,0.541697,7.063219,-9.235920,2.369882,4.304331,0.435835,6.512088,9.407814,5.220653,7.155114,-0.253018,-7.166057,0.311512,9.718485,4.114990,-0.983347,-8.444648,6.045046,-9.067843,-5.708097,6.845183,9.305836,3.708683,-7.716266,8.534699,-5.703984,3.457447,-4.165533,0.557722,2.812954,-4.936450,9.085273,3.064986,0.425323,-1.783771,0.335537,4.643074,-7.684999,6.284616,-5.172736,-2.212520,-8.236676,9.132959,-2.821748,7.557485,8.995504,-7.105377,-9.675875,7.051431,4.766232,9.068185,-2.921683,-6.158472,1.015681,5.231198,-0.396252,-5.287185,5.286904,2.432049,2.905173,4.570483,9.784259,8.389728,9.929326,3.518137,-4.677750,5.955034,-0.859145,-5.613492,-0.553129,1.287435,9.537904,0.685089,2.441490,3.287641,2.326541,-7.757115,-7.473371,-1.264800,-9.749427,-0.781951,-4.758642,7.006996,9.030094,9.546277,1.632690,-1.048370,-5.014536,-0.453529,7.834252,-6.170803,-7.114841,9.955067,6.315902,1.495673,1.161707,-4.925521,4.810837,-6.441777,1.294685,-4.793573,-3.820376,-6.857805,1.418817,4.317769,-6.491703,3.316683,-6.910375,9.251308,3.471664,1.615148,-2.171540,-0.433438,-8.167051,2.457600,-6.525736,-2.277884,-4.311842,-0.675975,8.001232,-6.639626,1.411674,7.501394,-5.418237,8.652759,8.362884,2.754256,2.463028,9.412934,-5.638180,1.828903,4.518284,-4.325448,-8.636778,9.836653,-8.637119,5.530071,4.426926,9.150525,1.784483,9.871161,4.650459,3.618128,7.999728,-2.471172,5.910712,-3.922238,-5.322064,-2.146988,3.963406,-4.473957,-0.272039,-8.411180,-6.995957,7.914847,-2.600296,-9.109054,3.719044,-9.975920,9.848687,8.028677,2.740112,5.267157,-7.863943,-9.493360,9.699060,2.931750,9.247764,6.474135,1.351442,3.000171,-3.749104,7.499198,4.328131,-1.255901,7.635907,0.516665,9.937572,-2.592657,9.959361,-2.517166,7.315525,-4.349367,5.648126,3.354204,-8.341036,-7.776260,-7.040942,3.619884,-5.374263,-1.286705,4.132701,-4.687015,-5.968453,-9.638748,9.350527,-0.343864,-0.371477,7.006217,6.241559,-4.582400,-2.938992,-0.085996,-6.245961,-5.423506,5.486355,-8.118576,5.796865,6.140087,7.390690,8.647274,-6.806576,-6.549546,-1.450323,-8.143738,-4.832685,3.415038,-8.989578,3.349310,9.288686,5.113863,1.780236,5.739397,-6.641763,-1.932803,-5.718757,-6.392273,-0.886578,6.933467,6.835544,-5.809565,-7.991806,-5.842143,8.654821,-9.654367,6.614398,0.172073,0.097885,6.808904,2.293997,-6.800068,6.452053,7.113821,1.778836,-1.927098,-1.984460,-5.222649,8.350436,1.110273,-3.787717,6.806128,7.651900,-4.570196,-1.298103,-3.519210,-5.683969,7.573613,-8.137090,5.869165,-7.672649,-4.871467,-3.268962,1.086313,9.242555,-0.518654,-3.339475,7.129208,-1.483203,6.639261,-4.741356,-9.915434,-6.082572,-7.581312,-9.157750,-6.814515,-6.139142,-3.389474,8.264316,-9.649192,-1.554533,-7.720087,-9.702324,4.448641,-0.235727,4.325348,-6.765933,8.050182,-0.766902,8.640958,0.747808,2.767652,-6.360117,-4.590031,3.532075,-1.536370,3.370503,2.723545,7.312601,-6.233043,3.030234,-6.970901,8.551688,-9.654839,5.172167,0.745622,0.321755,-4.092878,-1.276312,3.562325,1.933114,9.576859,-9.493025,4.121589,6.635247,7.203332,4.904292,7.587870,5.931013,-0.808906,3.617191,7.007632,-1.588714,7.805936,-4.169125,9.591205,-4.474598,-0.173813,4.218564,-1.760831,5.322310,5.004057,0.231091,-0.447905,-0.542165,-6.820300,-2.428582,-7.725923,0.761951,1.895661,-2.510820,-6.984411,9.040446,9.678002,-1.280918,-9.646233,-9.316461,-4.014272,-0.059854,-2.226165,-7.276234,-0.409822,9.013113,2.257872,-0.149500,-0.300687,6.228618,-2.884120,-5.441872,4.656056,8.384288,-7.512156,9.983569,-1.191631,0.034381,-0.723624,0.779504,-4.576856,6.745768,1.037381,-0.708583,-2.293806,-8.858783,4.638751,6.206348,6.788111,-1.581630,-9.571834,3.022590,8.183348,5.715594,-6.343469,-7.291448,2.593468,-8.142036,-6.111423,9.755886,5.741524,2.572978,-6.958648,2.109915,7.217794,9.733891,-2.960464,-3.473737,-9.349351,5.563290,-1.898314,2.023808,-5.157937,7.410615,4.741208,2.451473,-2.059429,1.026227,5.932731,5.744899,-1.943669,-4.572601,6.078133,-4.571646,1.824151,-3.788659,7.893906,9.570124,5.037343,-2.360628,5.372049,8.467502,-5.293606,-3.154380,-5.575123,2.854659,1.870133,2.675203,-5.816427,-0.157355,9.932155,-5.539613,-0.067588,-9.899630,-1.255024,-8.482441,9.163293,0.328726,-8.751078,7.880587,9.419405,6.120355,8.056773,0.740781,-2.180244,1.602625,-1.626756,6.917432,8.299523,2.812597,-2.303460,-2.722363,8.702185,-6.881156,5.715035,-4.088424,-1.841860,8.356182,-3.580824,8.790238,-8.095678,1.227084,-2.411626,-1.357712,-8.122254,7.290755,2.026844,-6.284914,-9.011449,6.228143,3.859604,-0.832499,9.069746,6.369998,0.534132,0.307845,2.131844,-9.120834,5.619241,7.104090,-5.487770,-3.274362,-8.935894,6.142390,8.906384,3.116031,-3.964115,-6.603523,8.044041,-1.921663,4.713554,2.224083,-9.786314,-9.469883,-6.799961,1.094984,3.741521,-3.011721,3.603634,-6.296475,-8.304000,2.350848,0.378163,1.110891,6.984819,3.125900,7.081965,6.771236,7.083225,5.055856,4.511135,-5.456026,-4.824828,8.197887,-0.681178,1.136910,4.825419], dtype = "float32")#candidate|8689|(7800,)|const|float32
call_8687 = relay.TupleGetItem(func_3845_call(relay.reshape(var_8688.astype('float64'), [660,]), relay.reshape(const_8689.astype('float32'), [7800,]), ), 5)
call_8690 = relay.TupleGetItem(func_3848_call(relay.reshape(var_8688.astype('float64'), [660,]), relay.reshape(const_8689.astype('float32'), [7800,]), ), 5)
output = relay.Tuple([call_8677,call_8687,var_8688,const_8689,])
output2 = relay.Tuple([call_8678,call_8690,var_8688,const_8689,])
func_8692 = relay.Function([var_8688,], output)
mod['func_8692'] = func_8692
mod = relay.transform.InferType()(mod)
var_8693 = relay.var("var_8693", dtype = "float64", shape = (10, 66))#candidate|8693|(10, 66)|var|float64
output = func_8692(var_8693)
func_8694 = relay.Function([var_8693], output)
mutated_mod['func_8694'] = func_8694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4990_call = mod.get_global_var('func_4990')
func_4992_call = mutated_mod.get_global_var('func_4992')
call_8768 = func_4990_call()
call_8769 = func_4990_call()
output = relay.Tuple([call_8768,])
output2 = relay.Tuple([call_8769,])
func_8785 = relay.Function([], output)
mod['func_8785'] = func_8785
mod = relay.transform.InferType()(mod)
mutated_mod['func_8785'] = func_8785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8785_call = mutated_mod.get_global_var('func_8785')
call_8786 = func_8785_call()
output = call_8786
func_8787 = relay.Function([], output)
mutated_mod['func_8787'] = func_8787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_8788 = func_4118_call()
call_8789 = func_4118_call()
output = relay.Tuple([call_8788,])
output2 = relay.Tuple([call_8789,])
func_8826 = relay.Function([], output)
mod['func_8826'] = func_8826
mod = relay.transform.InferType()(mod)
output = func_8826()
func_8827 = relay.Function([], output)
mutated_mod['func_8827'] = func_8827
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8844 = relay.var("var_8844", dtype = "float64", shape = (3, 9, 13))#candidate|8844|(3, 9, 13)|var|float64
uop_8845 = relay.sqrt(var_8844.astype('float64')) # shape=(3, 9, 13)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_8862 = func_4118_call()
call_8863 = func_4118_call()
output = relay.Tuple([uop_8845,call_8862,])
output2 = relay.Tuple([uop_8845,call_8863,])
func_8864 = relay.Function([var_8844,], output)
mod['func_8864'] = func_8864
mod = relay.transform.InferType()(mod)
mutated_mod['func_8864'] = func_8864
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8865 = relay.var("var_8865", dtype = "float64", shape = (3, 9, 13))#candidate|8865|(3, 9, 13)|var|float64
func_8864_call = mutated_mod.get_global_var('func_8864')
call_8866 = func_8864_call(var_8865)
output = call_8866
func_8867 = relay.Function([var_8865], output)
mutated_mod['func_8867'] = func_8867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8502_call = mod.get_global_var('func_8502')
func_8503_call = mutated_mod.get_global_var('func_8503')
call_8879 = relay.TupleGetItem(func_8502_call(), 5)
call_8880 = relay.TupleGetItem(func_8503_call(), 5)
output = relay.Tuple([call_8879,])
output2 = relay.Tuple([call_8880,])
func_8892 = relay.Function([], output)
mod['func_8892'] = func_8892
mod = relay.transform.InferType()(mod)
mutated_mod['func_8892'] = func_8892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8892_call = mutated_mod.get_global_var('func_8892')
call_8893 = func_8892_call()
output = call_8893
func_8894 = relay.Function([], output)
mutated_mod['func_8894'] = func_8894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mod.get_global_var('func_1322')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_8897 = func_1322_call()
call_8898 = func_1322_call()
func_8029_call = mod.get_global_var('func_8029')
func_8030_call = mutated_mod.get_global_var('func_8030')
call_8899 = relay.TupleGetItem(func_8029_call(), 0)
call_8900 = relay.TupleGetItem(func_8030_call(), 0)
output = relay.Tuple([call_8897,call_8899,])
output2 = relay.Tuple([call_8898,call_8900,])
func_8901 = relay.Function([], output)
mod['func_8901'] = func_8901
mod = relay.transform.InferType()(mod)
output = func_8901()
func_8902 = relay.Function([], output)
mutated_mod['func_8902'] = func_8902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7442_call = mod.get_global_var('func_7442')
func_7443_call = mutated_mod.get_global_var('func_7443')
call_8980 = relay.TupleGetItem(func_7442_call(), 0)
call_8981 = relay.TupleGetItem(func_7443_call(), 0)
output = call_8980
output2 = call_8981
func_8988 = relay.Function([], output)
mod['func_8988'] = func_8988
mod = relay.transform.InferType()(mod)
mutated_mod['func_8988'] = func_8988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8988_call = mutated_mod.get_global_var('func_8988')
call_8989 = func_8988_call()
output = call_8989
func_8990 = relay.Function([], output)
mutated_mod['func_8990'] = func_8990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6130_call = mod.get_global_var('func_6130')
func_6131_call = mutated_mod.get_global_var('func_6131')
call_9012 = func_6130_call()
call_9013 = func_6130_call()
uop_9019 = relay.cos(call_9012.astype('float32')) # shape=(780, 1)
uop_9021 = relay.cos(call_9013.astype('float32')) # shape=(780, 1)
func_1626_call = mod.get_global_var('func_1626')
func_1627_call = mutated_mod.get_global_var('func_1627')
call_9053 = func_1626_call()
call_9054 = func_1626_call()
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_9056 = relay.TupleGetItem(func_2881_call(), 0)
call_9057 = relay.TupleGetItem(func_2883_call(), 0)
bop_9059 = relay.floor_mod(uop_9019.astype('float32'), relay.reshape(call_9012.astype('float32'), relay.shape_of(uop_9019))) # shape=(780, 1)
bop_9062 = relay.floor_mod(uop_9021.astype('float32'), relay.reshape(call_9013.astype('float32'), relay.shape_of(uop_9021))) # shape=(780, 1)
bop_9072 = relay.greater(bop_9059.astype('bool'), relay.reshape(uop_9019.astype('bool'), relay.shape_of(bop_9059))) # shape=(780, 1)
bop_9075 = relay.greater(bop_9062.astype('bool'), relay.reshape(uop_9021.astype('bool'), relay.shape_of(bop_9062))) # shape=(780, 1)
output = relay.Tuple([call_9053,call_9056,bop_9072,])
output2 = relay.Tuple([call_9054,call_9057,bop_9075,])
func_9089 = relay.Function([], output)
mod['func_9089'] = func_9089
mod = relay.transform.InferType()(mod)
output = func_9089()
func_9090 = relay.Function([], output)
mutated_mod['func_9090'] = func_9090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6640_call = mod.get_global_var('func_6640')
func_6642_call = mutated_mod.get_global_var('func_6642')
call_9103 = func_6640_call()
call_9104 = func_6640_call()
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_9107 = relay.TupleGetItem(func_2881_call(), 0)
call_9108 = relay.TupleGetItem(func_2883_call(), 0)
func_7077_call = mod.get_global_var('func_7077')
func_7084_call = mutated_mod.get_global_var('func_7084')
const_9118 = relay.const([[-0.346101,-9.747650,6.520649,-8.711914,-9.671590,4.363318,-5.337911,1.344262,-5.018855,-4.655776,4.374327,-1.059032,-1.115179,-7.549753,0.686874,7.383667,-0.553394,7.041445,-9.899054,5.173632],[-7.971213,-8.216733,-5.586019,3.399116,-5.161407,4.566573,4.918322,-0.413754,2.553463,-8.038839,2.062401,2.551166,-6.573642,4.669500,-5.356330,8.249700,-7.277244,-8.322009,-0.420999,4.348804],[4.066502,-3.865248,-7.374396,-7.473575,0.657319,8.113025,-6.150529,8.190590,1.590375,1.990402,6.391715,-6.021348,-6.697535,-5.593466,8.021789,8.293369,2.333295,0.251108,3.212276,7.490033]], dtype = "float64")#candidate|9118|(3, 20)|const|float64
var_9119 = relay.var("var_9119", dtype = "uint8", shape = (780,))#candidate|9119|(780,)|var|uint8
const_9120 = relay.const([7,-6,10,-5,-6,-3,-2,8,7,-6,-6,-3,10,-9,3,6,3,-9,1,-1,4,-6,9,10,5,2,-9,-4,-4,-7,7,1,7,-3,5,-9,-2,-3,-1,4,1,9,3,-8,6,-8,-3,3,8,-8,3,-9,-2,-5,-9,9,7,9,3,8,7,10,-6,9,10,6,5,-8,2,-2,-2,-1,10,10,-1,1,-6,-7,-6,6,-6,-9,8,9,-1,-10,-1,4,3,5,4,-2,-6,3,-7,-8,-1,-3,-4,-10,-1,-8,3,4,-5,10,4,10,-2,4,3,-2,8,-5,8,-7,-6,-5,-6,5,-9,-1,-8,5,-3,9,10,10,9,-2,1,-9,-4,-7,3,-4,-8,5,3,6,-8,1,8,-8,9,5,-9,8,-7,8,9,-2,4,-5,-5,6,-7,3,-10,-4,1,8,4,-7,-3,10,-4,8,-8,-8,3,-10,1,-8,4,-10,1,-7,6,-3,9,-10,6,5,-3,10,-9,8,4,2,8,-5,2,2,-7,8,10,1,9,3,10,-10,6,8,-4,7,4,8,5,-3,-5,-8,-10,3,6,-1,-9,-7,7,-4,8,2,5,-6,-10,-1,-2,1,10,1,-10,-4,1,6,9,-10,3,-6,2,7,5,-8,-8,10,3,-8,4,-3,-5,5,-3,8,-7,-4,-10,-2,10,-1,6,-8,5,-3,-8,-3,9,5,-5,6,1,2,1,-6,1,-1,1,8,-5,-4,-9,-6,-7,8,5,-3,-6,-8,8,-7,-3,7,-8,-9,-8,-6,8,-5,4,-6,-7,-7,-5,-9,-1,3,7,-6,-9,-7,-8,1,-6,2,10,-1,8,-2,-3,7,9,7,-3,10,10,6,4,-5,-6,10,-4,4,9,6,-9,7,4,-4,7,-1,-5,4,-6,10,5,-9,3,10,3,5,8,10,3,2,-9,-8,10,4,10,-2,-5,3,-6,1,8,1,-7,-9,4,2,-4,8,2,-2,7,9,-4,-2,-3,10,-9,7,-2,6,-8,1,-9,-6,2,-5,-9,-1,-7,3,-5,1,-6,8,7,-5,-4,-4,5,6,-7,6,-7,9,1,-6,-7,-10,7,2,-4,6,-3,-3,-2,8,1,-5,5,4,6,-2,-7,7,-2,8,7,-6,-6,-1,-7,8,-6,-6,-7,-5,-10,-7,1,1,-4,-9,-2,-3,3,7,-4,-8,9,9,6,-10,-3,3,2,5,-2,-9,1,-1,6,6,4,-2,2,1,-7,4,10,4,-1,10,-5,-8,-2,5,-8,10,7,-6,-5,-6,-8,2,10,-9,-5,4,9,10,-2,9,-6,-3,3,3,-8,8,-1,-3,-6,-2,3,-1,-8,4,-6,10,-4,-8,-4,-2,-9,-8,1,-1,-4,-8,-1,-1,-1,-10,8,10,5,-8,8,9,10,-10,-9,-10,6,-1,-6,-5,-9,-4,5,10,2,6,8,9,-5,1,-10,8,-8,10,-3,-2,9,9,4,3,7,-7,-7,3,5,-5,-6,10,3,-1,-6,9,1,-1,-7,-10,-2,-7,3,-2,-7,-3,1,8,-5,10,-4,-1,5,9,-4,6,7,-6,5,-9,4,-7,7,-9,-6,6,-8,-4,-8,-6,-3,-10,-8,-3,4,-7,-3,-5,10,3,-5,-6,7,-9,-5,9,9,-2,-6,10,-4,8,9,-10,-9,7,-3,8,-4,-8,4,-1,-5,-10,6,10,-4,1,-2,-4,-3,7,-5,9,4,10,-3,10,4,10,7,3,-8,7,-5,-3,2,-6,4,6,-1,5,7,-3,-3,-2,4,-4,-10,-6,-1,-3,8,-10,3,10,2,9,1,2,-6,6,2,4,-10,10,9,2,3,2,8,3,9,9,3,-4,10,10,-10,5,-7,9,10,-5,-5,-10,-1,3,4,-8,7,-7,1,-8,-6,-1,10,10,5,-3,-4,-5,6,5,-2,-9,6,-4,5,-10,-5,-3,10,4,-9,-6,-10,10,-9,-7,9,-9,-2,-3,-5,8,-1,6,4,-7,-9,-8,3,6,-4,-4,9,-7,6,-1,-1,4,2,3,2,-1,-4,9,-8,1,7,2,-9,-10,8,-10,10,1,4,10,-6,8,-9,-1,-3,8,8,-8,10,5,-1,5,9,-5,-1,-10,3,1,6,-10,4,8,9,-10,6,-5,10,-10,7,1,-10,9,10,7,1,4,-5,-9,10,1,7,-5,-7,6,-10,-6,-10,4,-4,-6,8,2,4,-10,-1,4,-9,6,6,2,1,-8,2], dtype = "int32")#candidate|9120|(847,)|const|int32
var_9121 = relay.var("var_9121", dtype = "uint8", shape = (3900,))#candidate|9121|(3900,)|var|uint8
call_9117 = relay.TupleGetItem(func_7077_call(relay.reshape(const_9118.astype('float64'), [60,]), relay.reshape(var_9119.astype('uint8'), [780,]), relay.reshape(const_9120.astype('int32'), [847,]), relay.reshape(var_9121.astype('uint8'), [3900,]), relay.reshape(const_9120.astype('float32'), [847,]), ), 2)
call_9122 = relay.TupleGetItem(func_7084_call(relay.reshape(const_9118.astype('float64'), [60,]), relay.reshape(var_9119.astype('uint8'), [780,]), relay.reshape(const_9120.astype('int32'), [847,]), relay.reshape(var_9121.astype('uint8'), [3900,]), relay.reshape(const_9120.astype('float32'), [847,]), ), 2)
func_6503_call = mod.get_global_var('func_6503')
func_6505_call = mutated_mod.get_global_var('func_6505')
call_9124 = relay.TupleGetItem(func_6503_call(relay.reshape(const_9120.astype('int32'), [847,])), 3)
call_9125 = relay.TupleGetItem(func_6505_call(relay.reshape(const_9120.astype('int32'), [847,])), 3)
func_8226_call = mod.get_global_var('func_8226')
func_8227_call = mutated_mod.get_global_var('func_8227')
call_9146 = func_8226_call()
call_9147 = func_8226_call()
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_9180 = func_6597_call()
call_9181 = func_6597_call()
uop_9185 = relay.atan(const_9118.astype('float32')) # shape=(3, 20)
func_6130_call = mod.get_global_var('func_6130')
func_6131_call = mutated_mod.get_global_var('func_6131')
call_9188 = func_6130_call()
call_9189 = func_6130_call()
bop_9194 = relay.logical_or(uop_9185.astype('bool'), relay.reshape(const_9118.astype('bool'), relay.shape_of(uop_9185))) # shape=(3, 20)
output = relay.Tuple([call_9103,call_9107,call_9117,var_9119,const_9120,var_9121,call_9124,call_9146,call_9180,call_9188,bop_9194,])
output2 = relay.Tuple([call_9104,call_9108,call_9122,var_9119,const_9120,var_9121,call_9125,call_9147,call_9181,call_9189,bop_9194,])
func_9214 = relay.Function([var_9119,var_9121,], output)
mod['func_9214'] = func_9214
mod = relay.transform.InferType()(mod)
mutated_mod['func_9214'] = func_9214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9214_call = mutated_mod.get_global_var('func_9214')
var_9216 = relay.var("var_9216", dtype = "uint8", shape = (780,))#candidate|9216|(780,)|var|uint8
var_9217 = relay.var("var_9217", dtype = "uint8", shape = (3900,))#candidate|9217|(3900,)|var|uint8
call_9215 = func_9214_call(var_9216,var_9217,)
output = call_9215
func_9218 = relay.Function([var_9216,var_9217,], output)
mutated_mod['func_9218'] = func_9218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_9285 = func_4758_call()
call_9286 = func_4758_call()
func_5842_call = mod.get_global_var('func_5842')
func_5843_call = mutated_mod.get_global_var('func_5843')
call_9322 = relay.TupleGetItem(func_5842_call(), 0)
call_9323 = relay.TupleGetItem(func_5843_call(), 0)
output = relay.Tuple([call_9285,call_9322,])
output2 = relay.Tuple([call_9286,call_9323,])
func_9327 = relay.Function([], output)
mod['func_9327'] = func_9327
mod = relay.transform.InferType()(mod)
output = func_9327()
func_9328 = relay.Function([], output)
mutated_mod['func_9328'] = func_9328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4743_call = mod.get_global_var('func_4743')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_9339 = relay.TupleGetItem(func_4743_call(), 0)
call_9340 = relay.TupleGetItem(func_4745_call(), 0)
output = call_9339
output2 = call_9340
func_9347 = relay.Function([], output)
mod['func_9347'] = func_9347
mod = relay.transform.InferType()(mod)
mutated_mod['func_9347'] = func_9347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9347_call = mutated_mod.get_global_var('func_9347')
call_9348 = func_9347_call()
output = call_9348
func_9349 = relay.Function([], output)
mutated_mod['func_9349'] = func_9349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5878_call = mod.get_global_var('func_5878')
func_5879_call = mutated_mod.get_global_var('func_5879')
call_9435 = relay.TupleGetItem(func_5878_call(), 0)
call_9436 = relay.TupleGetItem(func_5879_call(), 0)
func_8575_call = mod.get_global_var('func_8575')
func_8577_call = mutated_mod.get_global_var('func_8577')
call_9439 = func_8575_call()
call_9440 = func_8575_call()
output = relay.Tuple([call_9435,call_9439,])
output2 = relay.Tuple([call_9436,call_9440,])
func_9441 = relay.Function([], output)
mod['func_9441'] = func_9441
mod = relay.transform.InferType()(mod)
mutated_mod['func_9441'] = func_9441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9441_call = mutated_mod.get_global_var('func_9441')
call_9442 = func_9441_call()
output = call_9442
func_9443 = relay.Function([], output)
mutated_mod['func_9443'] = func_9443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8329_call = mod.get_global_var('func_8329')
func_8330_call = mutated_mod.get_global_var('func_8330')
call_9482 = relay.TupleGetItem(func_8329_call(), 2)
call_9483 = relay.TupleGetItem(func_8330_call(), 2)
output = relay.Tuple([call_9482,])
output2 = relay.Tuple([call_9483,])
func_9491 = relay.Function([], output)
mod['func_9491'] = func_9491
mod = relay.transform.InferType()(mod)
mutated_mod['func_9491'] = func_9491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9491_call = mutated_mod.get_global_var('func_9491')
call_9492 = func_9491_call()
output = call_9492
func_9493 = relay.Function([], output)
mutated_mod['func_9493'] = func_9493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8502_call = mod.get_global_var('func_8502')
func_8503_call = mutated_mod.get_global_var('func_8503')
call_9586 = relay.TupleGetItem(func_8502_call(), 1)
call_9587 = relay.TupleGetItem(func_8503_call(), 1)
output = call_9586
output2 = call_9587
func_9610 = relay.Function([], output)
mod['func_9610'] = func_9610
mod = relay.transform.InferType()(mod)
mutated_mod['func_9610'] = func_9610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9610_call = mutated_mod.get_global_var('func_9610')
call_9611 = func_9610_call()
output = call_9611
func_9612 = relay.Function([], output)
mutated_mod['func_9612'] = func_9612
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9665 = relay.var("var_9665", dtype = "uint8", shape = (3, 3, 7))#candidate|9665|(3, 3, 7)|var|uint8
const_9666 = relay.const([[[6,-8,-3,6,-10,-6,8],[6,-1,4,-8,-4,5,-4],[5,-10,-10,-4,9,-6,10]],[[-5,-9,8,3,-10,6,-1],[10,-1,3,-8,2,-9,-5],[-9,7,5,-4,-6,4,9]],[[9,-5,7,-6,9,-7,-7],[1,9,6,3,-2,6,-5],[3,2,-4,-1,-3,3,-10]]], dtype = "uint8")#candidate|9666|(3, 3, 7)|const|uint8
bop_9667 = relay.less(var_9665.astype('bool'), relay.reshape(const_9666.astype('bool'), relay.shape_of(var_9665))) # shape=(3, 3, 7)
func_5279_call = mod.get_global_var('func_5279')
func_5280_call = mutated_mod.get_global_var('func_5280')
call_9672 = func_5279_call()
call_9673 = func_5279_call()
func_1456_call = mod.get_global_var('func_1456')
func_1459_call = mutated_mod.get_global_var('func_1459')
const_9676 = relay.const([-7,3,7,-4,7,9,2,4,9,-6,-2,4,-6,3,2,6,-10,-7,6,-7,9,5,-1,-3,-8,1,2,6,-2,-6,2,4,-2,10,6,10,-3,-7,5,-7,9,-3,-3,8,7,-4,7,-2,10,-4,-9,-2,-1,-1,10,-9,3,-9,10,-6,1,-7,-7,-7,3,5,-8,-8,-5,5,-4,4,6,-8,3,5,-3,4,5,10,5,-2,2,1,-7,-5,-1,-10,4,-5,-1,3,-5,7,10,-10,3,-7,-1,2,-5,1,-6,4,1,9,2,-8,-8,-8,2,-3,-7,-10,9,8,-1,-9,-2,-8,-4,2,8,-2,-5,-7,6,2,2,-4,5,4,-1,-2,-8,5,-9,6,9,6,-8,-2,4,-10,7,-7,5,8,-4,10,-3,4,4,-9,-7,8,9,10,6,-10,-3,5,6,-8,6,-4,5,-2,7,-1,-8,10,8,1,-1,9,5,3,-9,-4,1,5,4,-6,-1,-5,-7,-6,-6,-1,7,-10,1,-6,6,-7,-7,-4,10,-4,-8,-1,4,10,-6,5,-8,-6,10,-1,-1,3,1,-9,-9,5,1,-2,3,5,2,3,-6,-9,10,-1,10,-6,-3,-3,9,-2,4,-3,6,8,-9,8,-9,-2,-8,-7,8,1,-2,6,4,10,-1,-7,-3,7,-6,-7,-1,-4,-1,1,-8,-3,-9,-10,6,-3,4,-4,-6,1,5,9,-9,6,3,1,2,-2,2,5,3,-3,-9,6,-9,9,6,-9,-10,7,4,5,-4,6,8,-2,-9,-7,-5,6,-9,7,3,-10,-2,-6,-5,-4,-7,-4,2,-5,-4,-1,-5,-2,-10,-8,4,-7,3,3,-6,8,7,-10,10,2,-10,-3,-8,9,-4,2,-5,6,-4,-7,-6,-6,8,4,3,-4,-6,10,-3,-3,-4,-9,-6,6,-2,10,9,-2,2,-7,-9,10,9,1,-8,1,1,-10,2,7,-2,-5,3,-10,-3,-3,-9,10,-4,-1,7,-4,-3,5,4,-3,-9,7,-4,-10,-7,9,-8,5,-2,-4,-10,5,-5,-1,2,-5,-10,4,1,-3,7,-4,5,-6,-6,5,-1,9,1,-6,4,6,4,-2,-2,-3,8,-3,-7,-9,-1,10,5,1,9,-10,9,-9,-6,9,-7,-8,-2,-8,-3,-3,-9,8,2,1,7,6,-7,-10,-7,2,3,-9,-2,7,1,-10,3,-6,9,8,-9,1,-1,-9,-2,-2,-3,-2,-7,-10,9,1,-2,-10,-4,-7,5,1,1,-8,-2,-7,-3,-10,10,-9,2,2,8,-4,-2,-7,1,7,-9,2,-5,-4,10,9,6,8,9,-3,-5,3,-8,-6,-10,8,8,-1,-2,1,1,-1,-9,6,-10,9,3,-3,-4,-9,-2,4,-10,-2,9,4,3,-6,4,-2,-8,2,-1,-4,3,-9,-2,-4,-7,-3,-10,-6,-2,-7,4,-3,-8,-4,7,4,-1,5,-8,-4,-5,-9,5,10,-8,4,-6,-4,1,3,-8,-7,4,2,3,6,6,5,-3,-9,-1,2,-1,2,-6,9,6,5,-10,-1,-7,-10,-2,-4,-9,-5,7,10,6,9,8,10,-4,3,3,6,1,-3,-1,8,-10,-2,2,7,3,4,4,7,-8,-1,-6,-9,4,-10,8,5,-2,-7,9,4,9,-3,-1,-10,-3,-8,-7,6,10,6,-5,-10,-8,-5,2,-8,9,-4,4,-9,-5,5,-5,-5,8,-5,-4,2,-1,-10,-8,3,-2,8,-1,2,-4,-1,-10,6,-8,1,-5,6,1,10,-4,9,-2,-1,-3,-2,-2,8,7,-9,6,-9,-4,10,2,-7,4,2,2,-10,6,6,3,1,-9,-9,2,-5,-4,4,-4,2,-6,4,6,6,6,-4,-5,8,-9,6,-6,10,7,-6,6,9,-2,1,-6,2,9,8,-2,6,5,5,-5,1,-8,3,5,-7,2,5,-6,-10,6,7,-8,1,4,-5,8,1,5,3,3,-8,-9,6,3,-8,-4,7,9,5,4,4,-10,-10,-8,-6,3,9,9,7,9,-1,2,7,7,-5,-6,5,-4,10], dtype = "uint8")#candidate|9676|(780,)|const|uint8
call_9675 = relay.TupleGetItem(func_1456_call(relay.reshape(const_9676.astype('uint8'), [1, 780])), 2)
call_9677 = relay.TupleGetItem(func_1459_call(relay.reshape(const_9676.astype('uint8'), [1, 780])), 2)
output = relay.Tuple([bop_9667,call_9672,call_9675,const_9676,])
output2 = relay.Tuple([bop_9667,call_9673,call_9677,const_9676,])
func_9694 = relay.Function([var_9665,], output)
mod['func_9694'] = func_9694
mod = relay.transform.InferType()(mod)
mutated_mod['func_9694'] = func_9694
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9695 = relay.var("var_9695", dtype = "uint8", shape = (3, 3, 7))#candidate|9695|(3, 3, 7)|var|uint8
func_9694_call = mutated_mod.get_global_var('func_9694')
call_9696 = func_9694_call(var_9695)
output = call_9696
func_9697 = relay.Function([var_9695], output)
mutated_mod['func_9697'] = func_9697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4975_call = mod.get_global_var('func_4975')
func_4977_call = mutated_mod.get_global_var('func_4977')
call_9708 = relay.TupleGetItem(func_4975_call(), 0)
call_9709 = relay.TupleGetItem(func_4977_call(), 0)
func_7813_call = mod.get_global_var('func_7813')
func_7815_call = mutated_mod.get_global_var('func_7815')
call_9712 = func_7813_call()
call_9713 = func_7813_call()
func_8785_call = mod.get_global_var('func_8785')
func_8787_call = mutated_mod.get_global_var('func_8787')
call_9714 = relay.TupleGetItem(func_8785_call(), 0)
call_9715 = relay.TupleGetItem(func_8787_call(), 0)
func_1664_call = mod.get_global_var('func_1664')
func_1666_call = mutated_mod.get_global_var('func_1666')
call_9720 = func_1664_call(relay.reshape(call_9708.astype('float64'), [7, 14, 4]))
call_9721 = func_1664_call(relay.reshape(call_9708.astype('float64'), [7, 14, 4]))
output = relay.Tuple([call_9708,call_9712,call_9714,call_9720,])
output2 = relay.Tuple([call_9709,call_9713,call_9715,call_9721,])
func_9727 = relay.Function([], output)
mod['func_9727'] = func_9727
mod = relay.transform.InferType()(mod)
output = func_9727()
func_9728 = relay.Function([], output)
mutated_mod['func_9728'] = func_9728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2049_call = mod.get_global_var('func_2049')
func_2051_call = mutated_mod.get_global_var('func_2051')
call_9745 = relay.TupleGetItem(func_2049_call(), 0)
call_9746 = relay.TupleGetItem(func_2051_call(), 0)
output = call_9745
output2 = call_9746
func_9755 = relay.Function([], output)
mod['func_9755'] = func_9755
mod = relay.transform.InferType()(mod)
mutated_mod['func_9755'] = func_9755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9755_call = mutated_mod.get_global_var('func_9755')
call_9756 = func_9755_call()
output = call_9756
func_9757 = relay.Function([], output)
mutated_mod['func_9757'] = func_9757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8826_call = mod.get_global_var('func_8826')
func_8827_call = mutated_mod.get_global_var('func_8827')
call_9792 = relay.TupleGetItem(func_8826_call(), 0)
call_9793 = relay.TupleGetItem(func_8827_call(), 0)
output = relay.Tuple([call_9792,])
output2 = relay.Tuple([call_9793,])
func_9803 = relay.Function([], output)
mod['func_9803'] = func_9803
mod = relay.transform.InferType()(mod)
output = func_9803()
func_9804 = relay.Function([], output)
mutated_mod['func_9804'] = func_9804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mod.get_global_var('func_6802')
func_6804_call = mutated_mod.get_global_var('func_6804')
call_9812 = relay.TupleGetItem(func_6802_call(), 0)
call_9813 = relay.TupleGetItem(func_6804_call(), 0)
output = call_9812
output2 = call_9813
func_9820 = relay.Function([], output)
mod['func_9820'] = func_9820
mod = relay.transform.InferType()(mod)
mutated_mod['func_9820'] = func_9820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9820_call = mutated_mod.get_global_var('func_9820')
call_9821 = func_9820_call()
output = call_9821
func_9822 = relay.Function([], output)
mutated_mod['func_9822'] = func_9822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7675_call = mod.get_global_var('func_7675')
func_7676_call = mutated_mod.get_global_var('func_7676')
call_9866 = relay.TupleGetItem(func_7675_call(), 1)
call_9867 = relay.TupleGetItem(func_7676_call(), 1)
func_8219_call = mod.get_global_var('func_8219')
func_8221_call = mutated_mod.get_global_var('func_8221')
call_9885 = func_8219_call()
call_9886 = func_8219_call()
func_3681_call = mod.get_global_var('func_3681')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_9890 = relay.TupleGetItem(func_3681_call(), 0)
call_9891 = relay.TupleGetItem(func_3682_call(), 0)
output = relay.Tuple([call_9866,call_9885,call_9890,])
output2 = relay.Tuple([call_9867,call_9886,call_9891,])
func_9898 = relay.Function([], output)
mod['func_9898'] = func_9898
mod = relay.transform.InferType()(mod)
mutated_mod['func_9898'] = func_9898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9898_call = mutated_mod.get_global_var('func_9898')
call_9899 = func_9898_call()
output = call_9899
func_9900 = relay.Function([], output)
mutated_mod['func_9900'] = func_9900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8226_call = mod.get_global_var('func_8226')
func_8227_call = mutated_mod.get_global_var('func_8227')
call_9952 = func_8226_call()
call_9953 = func_8226_call()
output = call_9952
output2 = call_9953
func_9954 = relay.Function([], output)
mod['func_9954'] = func_9954
mod = relay.transform.InferType()(mod)
mutated_mod['func_9954'] = func_9954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9954_call = mutated_mod.get_global_var('func_9954')
call_9955 = func_9954_call()
output = call_9955
func_9956 = relay.Function([], output)
mutated_mod['func_9956'] = func_9956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5878_call = mod.get_global_var('func_5878')
func_5879_call = mutated_mod.get_global_var('func_5879')
call_9964 = relay.TupleGetItem(func_5878_call(), 0)
call_9965 = relay.TupleGetItem(func_5879_call(), 0)
output = relay.Tuple([call_9964,])
output2 = relay.Tuple([call_9965,])
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
func_4462_call = mod.get_global_var('func_4462')
func_4464_call = mutated_mod.get_global_var('func_4464')
call_9990 = func_4462_call()
call_9991 = func_4462_call()
output = relay.Tuple([call_9990,])
output2 = relay.Tuple([call_9991,])
func_9997 = relay.Function([], output)
mod['func_9997'] = func_9997
mod = relay.transform.InferType()(mod)
output = func_9997()
func_9998 = relay.Function([], output)
mutated_mod['func_9998'] = func_9998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5608_call = mod.get_global_var('func_5608')
func_5610_call = mutated_mod.get_global_var('func_5610')
call_9999 = relay.TupleGetItem(func_5608_call(), 0)
call_10000 = relay.TupleGetItem(func_5610_call(), 0)
func_7472_call = mod.get_global_var('func_7472')
func_7474_call = mutated_mod.get_global_var('func_7474')
call_10014 = relay.TupleGetItem(func_7472_call(), 4)
call_10015 = relay.TupleGetItem(func_7474_call(), 4)
func_5940_call = mod.get_global_var('func_5940')
func_5942_call = mutated_mod.get_global_var('func_5942')
call_10020 = relay.TupleGetItem(func_5940_call(), 0)
call_10021 = relay.TupleGetItem(func_5942_call(), 0)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_10033 = relay.TupleGetItem(func_1126_call(), 0)
call_10034 = relay.TupleGetItem(func_1127_call(), 0)
output = relay.Tuple([call_9999,call_10014,call_10020,call_10033,])
output2 = relay.Tuple([call_10000,call_10015,call_10021,call_10034,])
func_10036 = relay.Function([], output)
mod['func_10036'] = func_10036
mod = relay.transform.InferType()(mod)
output = func_10036()
func_10037 = relay.Function([], output)
mutated_mod['func_10037'] = func_10037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5122_call = mod.get_global_var('func_5122')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_10041 = func_5122_call()
call_10042 = func_5122_call()
func_5178_call = mod.get_global_var('func_5178')
func_5179_call = mutated_mod.get_global_var('func_5179')
call_10044 = relay.TupleGetItem(func_5178_call(), 0)
call_10045 = relay.TupleGetItem(func_5179_call(), 0)
func_4009_call = mod.get_global_var('func_4009')
func_4014_call = mutated_mod.get_global_var('func_4014')
var_10052 = relay.var("var_10052", dtype = "float64", shape = (60,))#candidate|10052|(60,)|var|float64
const_10053 = relay.const([[-5],[4],[-3],[-8],[3],[2],[8],[-9],[-7],[4],[-8],[-1],[9],[3],[-1],[-6],[5],[10],[4],[-7],[-2],[8],[2],[-8],[-6],[-8],[-5],[5],[-4],[9],[-3],[-4],[5],[-4],[-3],[-8],[2],[4],[-3],[3],[-7],[4],[-10],[8],[-9],[-3],[-2],[-1],[-2],[7],[-8],[2],[-1],[5],[1],[3],[-9],[-1],[-8],[-6],[6],[9],[6],[-6],[-5],[-4],[8],[-4],[-2],[-4],[7],[2],[6],[8],[2],[1],[5],[7],[-2],[-10],[6],[1],[-1],[4],[3],[10],[-5],[9],[-6],[5],[1],[8],[-8],[7],[-8],[6],[-4],[7],[-1],[1],[-8],[6],[-5],[-5],[2],[-1],[-6],[8],[3],[-5],[-6],[-4],[-9],[6],[-3],[5],[-9],[-7],[6],[5],[1],[-2],[6],[2],[-7],[2],[-7],[4],[1],[-5],[-10],[-8],[-3],[-5],[-8],[-8],[8],[-6],[2],[-6],[5],[4],[8],[8],[-9],[-4],[7],[-10],[-8],[9],[7],[2],[9],[-2],[8],[-2],[7],[4],[6],[-5],[-9],[6],[10],[4],[2],[3],[-3],[5],[-5],[-3],[-6],[-5],[-2],[10],[-1],[3],[-3],[-5],[6],[2],[-3],[7],[2],[-7],[10],[1],[6],[-1],[-4],[-6],[-6],[-6],[9],[-6],[9],[3],[5],[-1],[4],[5],[10],[2],[-1],[-6],[-5],[-10],[1],[-2],[7],[5],[5],[1],[10],[8],[-10],[9],[-10],[-5],[5],[-8],[4],[-3],[-5],[-5],[-4],[10],[10],[1],[1],[-7],[-4],[-8],[9],[-7],[-7],[-7],[6],[5],[-7],[-4],[3],[-10],[3],[-5],[1],[-5],[10],[9],[-9],[6],[-5],[8],[-4],[-1],[-3],[10],[10],[1],[1],[8],[-9],[7],[6],[-1],[-4],[2],[1],[-1],[3],[6],[8],[2],[-5],[-1],[-10],[-6],[-2],[10],[-9],[-5],[-9],[4],[-7],[7],[-6],[5],[-8],[-2],[-1],[-7],[4],[10],[6],[-5],[1],[10],[9],[2],[-1],[-5],[3],[-3],[-9],[1],[-9],[-1],[-4],[10],[10],[-7],[-7],[1],[-2],[-1],[1],[10],[-6],[-4],[-9],[4],[-5],[-1],[-5],[1],[6],[4],[-6],[1],[-7],[3],[-8],[3],[-7],[8],[-2],[-1],[7],[-8],[-3],[-8],[6],[6],[7],[3],[10],[4],[-10],[-4],[4],[2],[6],[2],[7],[8],[8],[3],[-5],[7],[-6],[8],[6],[-8],[10],[5],[5],[7],[1],[7],[-9],[8],[-8],[-1],[-9],[9],[-1],[-3],[-2],[5],[-2],[4],[-6],[-1],[2],[4],[2],[9],[2],[6],[-10],[-7],[3],[-8],[-1],[-5],[-1],[-10],[-1],[3],[8],[5],[9],[1],[5],[5],[4],[6],[3],[2],[-7],[7],[-7],[-7],[8],[2],[-9],[-6],[-10],[-4],[-6],[-10],[-2],[-8],[10],[-1],[7],[7],[4],[2],[7],[-8],[10],[7],[-2],[-3],[-1],[-9],[-9],[1],[8],[-6],[-1],[1],[-8],[9],[-9],[-2],[-10],[-7],[1],[3],[4],[6],[-10],[5],[-9],[5],[6],[7],[-10],[-9],[-3],[6],[-9],[10],[-4],[3],[-6],[5],[6],[-5],[3],[-6],[7],[2],[10],[-6],[2],[10],[6],[1],[-2],[10],[-3],[-3],[-5],[3],[10],[4],[3],[-7],[-7],[7],[5],[-1],[7],[1],[-8],[5],[-7],[10],[1],[-9],[-3],[10],[-1],[8],[-10],[-9],[2],[5],[4],[7],[8],[5],[4],[-7],[-1],[6],[9],[7],[-3],[-10],[-1],[7],[9],[-3],[8],[8],[5],[3],[-1],[4],[7],[3],[8],[-8],[8],[-3],[6],[-2],[-1],[-1],[4],[7],[3],[9],[-2],[-3],[7],[-7],[-9],[-5],[4],[3],[9],[9],[10],[-1],[7],[6],[-7],[3],[9],[10],[-3],[10],[-3],[-6],[4],[-9],[5],[-5],[5],[-9],[-1],[4],[1],[-1],[5],[-6],[-8],[10],[-3],[10],[-8],[-2],[-6],[7],[-2],[-6],[3],[-5],[9],[-5],[-5],[3],[-7],[-7],[-9],[-10],[4],[9],[-1],[-1],[-3],[6],[-9],[10],[-6],[2],[-6],[-7],[8],[-3],[-8],[4],[-7],[4],[-9],[8],[6],[-10],[4],[-2],[-5],[-2],[-9],[-5],[-2],[4],[1],[4],[8],[3],[6],[9],[-7],[4],[-9],[4],[3],[6],[-6],[9],[-9],[-7],[-8],[10],[2],[-5],[-7],[8],[-3],[7],[-1],[9],[-8],[5],[8],[-1],[-6],[9],[3],[2],[-5],[2],[1],[-7],[-4],[-10],[5],[10],[6],[7],[-1],[9],[9],[3],[-7],[5],[-4],[-5],[-7],[-1],[7],[6],[3],[-7],[-3],[-1],[5],[2],[-9],[-5],[-10],[10],[7],[10],[8],[-7],[-5],[8],[2],[6],[-2],[-8],[6],[10],[-4],[2],[3],[-9],[7],[-8],[-3],[9],[1],[7],[-5],[-7],[-10],[3],[-4],[3],[-5],[-2],[-9],[1],[-8],[-1],[8],[-8],[-1],[2],[-8],[2],[-5],[-5],[-5],[-7],[-5],[9],[9],[10],[-2],[10],[-4],[9],[-5],[-9],[2],[-2],[4],[6],[-6],[-10],[-3],[5],[-10],[1],[7],[-10],[-10],[-6],[1],[-10],[7],[-10],[9],[-2],[10],[-8],[-10],[4],[7],[10],[7],[-6],[-8],[-3]], dtype = "uint8")#candidate|10053|(780, 1)|const|uint8
var_10054 = relay.var("var_10054", dtype = "int32", shape = (847,))#candidate|10054|(847,)|var|int32
call_10051 = relay.TupleGetItem(func_4009_call(relay.reshape(var_10052.astype('float64'), [60,]), relay.reshape(const_10053.astype('uint8'), [780,]), relay.reshape(var_10054.astype('int32'), [847,]), ), 6)
call_10055 = relay.TupleGetItem(func_4014_call(relay.reshape(var_10052.astype('float64'), [60,]), relay.reshape(const_10053.astype('uint8'), [780,]), relay.reshape(var_10054.astype('int32'), [847,]), ), 6)
func_4009_call = mod.get_global_var('func_4009')
func_4014_call = mutated_mod.get_global_var('func_4014')
call_10060 = relay.TupleGetItem(func_4009_call(relay.reshape(var_10052.astype('float64'), [60,]), relay.reshape(const_10053.astype('uint8'), [780,]), relay.reshape(var_10054.astype('int32'), [847,]), ), 2)
call_10061 = relay.TupleGetItem(func_4014_call(relay.reshape(var_10052.astype('float64'), [60,]), relay.reshape(const_10053.astype('uint8'), [780,]), relay.reshape(var_10054.astype('int32'), [847,]), ), 2)
func_1038_call = mod.get_global_var('func_1038')
func_1041_call = mutated_mod.get_global_var('func_1041')
const_10067 = relay.const([[6,-5,6,-9,-4,6,-1,8,5,-10,2,9,6,-10,-9,2,-2,6,-4,6,-5,1,9,-2,9,-3,-1,-8,2,1,-4,7,-1,-6,9,-2,4,10,7,10,-5,8],[7,2,-3,1,7,5,-2,-2,-3,-5,10,-10,9,-2,3,8,-5,9,5,-7,-7,-10,-1,10,-7,-3,-2,5,-5,4,8,-9,-4,2,8,4,10,-2,6,-7,9,-1],[4,-10,4,6,8,4,-2,1,-4,5,9,-8,-1,8,-4,-1,-3,-7,5,-9,-7,-4,9,-10,10,-10,-7,4,3,10,-8,-8,-3,8,-6,-10,-9,-5,2,5,3,3]], dtype = "uint8")#candidate|10067|(3, 42)|const|uint8
call_10066 = relay.TupleGetItem(func_1038_call(relay.reshape(const_10067.astype('uint8'), [9, 7, 2]), relay.reshape(const_10053.astype('uint8'), [780,]), ), 1)
call_10068 = relay.TupleGetItem(func_1041_call(relay.reshape(const_10067.astype('uint8'), [9, 7, 2]), relay.reshape(const_10053.astype('uint8'), [780,]), ), 1)
bop_10071 = relay.subtract(call_10060.astype('float32'), const_10053.astype('float32')) # shape=(780, 60)
bop_10074 = relay.subtract(call_10061.astype('float32'), const_10053.astype('float32')) # shape=(780, 60)
output = relay.Tuple([call_10041,call_10044,call_10051,var_10052,var_10054,call_10066,const_10067,bop_10071,])
output2 = relay.Tuple([call_10042,call_10045,call_10055,var_10052,var_10054,call_10068,const_10067,bop_10074,])
F = relay.Function([var_10052,var_10054,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10052,var_10054,], output2)
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
